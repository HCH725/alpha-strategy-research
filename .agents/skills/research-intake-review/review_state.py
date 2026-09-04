#!/usr/bin/env python3
"""Deterministic state helper for Research Intake Review.

This file owns mechanics only: small immutable batch selection, state invariants,
remediation bookkeeping, and atomic checkpoint writes. The single-run lease is
held inside the canonical state and acquired/released by CatDesk guarded edits.
This helper is the manual/reference implementation for integrity checks; scheduled
runs are shell-free and reproduce its invariants through dedicated CatDesk tools
plus immutable GitHub history. Research judgment remains in SKILL.md and ChatGPT.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

BUCKETS = ("pass", "pass_with_caveat", "remediate", "reject")
DECISION_TO_BUCKET = {
    "PASS": "pass",
    "PASS-WITH-CAVEAT": "pass_with_caveat",
    "REMEDIATE": "remediate",
    "REJECT": "reject",
}
DEFAULT_STATE = Path("/Users/hong/workspace/alpha-strategy-review-state.json")
DEFAULT_REPO = Path("/Users/hong/workspace/alpha-strategy-research")
DEFAULT_MAX_ARTIFACTS = 5


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")


def parse_iso(value: str) -> dt.datetime:
    parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def atomic_write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    tmp = Path(tmp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, path)
        dir_fd = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)
    finally:
        if tmp.exists():
            tmp.unlink()


def git(repo: Path, *args: str, check: bool = True) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and proc.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc.stdout.strip()


def is_strategy_path(path: str) -> bool:
    p = Path(path)
    return len(p.parts) == 1 and p.suffix == ".md" and not p.name.startswith("README")


def diff_strategy_items(repo: Path, base: str, head: str) -> list[dict]:
    if base == head:
        return []
    out = git(repo, "diff", "--name-status", "-M", f"{base}..{head}")
    items: list[dict] = []
    seen: set[str] = set()
    for line in out.splitlines():
        if not line.strip():
            continue
        fields = line.split("\t")
        status = fields[0]
        if status.startswith(("R", "C")) and len(fields) >= 3:
            old_path, new_path = fields[1], fields[2]
            if is_strategy_path(old_path) or is_strategy_path(new_path):
                key = new_path if is_strategy_path(new_path) else old_path
                if key not in seen:
                    items.append({"status": status, "path": key, "old_path": old_path, "new_path": new_path})
                    seen.add(key)
            continue
        if len(fields) >= 2:
            candidate = fields[1]
            if is_strategy_path(candidate) and candidate not in seen:
                items.append({"status": status, "path": candidate})
                seen.add(candidate)
    return items


def select_batch_head(repo: Path, base: str, remote_head: str, max_artifacts: int) -> tuple[str, list[dict]]:
    commits = git(repo, "rev-list", "--reverse", f"{base}..{remote_head}").splitlines()
    if not commits:
        return base, []

    chosen = base
    chosen_items: list[dict] = []
    for commit in commits:
        items = diff_strategy_items(repo, base, commit)
        if len(items) > max_artifacts and chosen != base:
            break
        chosen = commit
        chosen_items = items
        if len(items) >= max_artifacts:
            break
    return chosen, chosen_items


def validate_state(data: dict) -> list[str]:
    errors: list[str] = []

    lease = data.get("run_lease")
    if lease is not None:
        if not isinstance(lease, dict):
            errors.append("run_lease must be null or an object")
        else:
            required = ("run_id", "owner", "started_at", "stale_after_minutes")
            missing = [key for key in required if not lease.get(key)]
            if missing:
                errors.append(f"run_lease missing required field(s): {missing}")
            try:
                if lease.get("started_at"):
                    parse_iso(str(lease["started_at"]))
            except Exception:
                errors.append("run_lease.started_at must be ISO-8601")
            if lease.get("stale_after_minutes") is not None:
                try:
                    if int(lease["stale_after_minutes"]) <= 0:
                        errors.append("run_lease.stale_after_minutes must be positive")
                except Exception:
                    errors.append("run_lease.stale_after_minutes must be an integer")

    snapshot = data.get("current_snapshot", {})
    memberships: dict[str, list[str]] = {}
    for bucket in BUCKETS:
        values = snapshot.get(bucket, [])
        if not isinstance(values, list):
            errors.append(f"current_snapshot.{bucket} must be a list")
            continue
        for path in values:
            memberships.setdefault(path, []).append(bucket)
    for path, buckets in memberships.items():
        if len(buckets) != 1:
            errors.append(f"decision bucket conflict for {path}: {buckets}")

    findings = data.get("last_review_findings", {})
    for item in findings.get("items", []):
        decision = item.get("decision")
        path = item.get("path")
        bucket = DECISION_TO_BUCKET.get(decision)
        if not bucket:
            errors.append(f"unknown last_review_findings decision for {path}: {decision}")
            continue
        actual = memberships.get(path, [])
        if actual != [bucket]:
            errors.append(f"last finding mismatch for {path}: {decision} vs {actual}")

    backlog = data.get("remediation_backlog", [])
    if not isinstance(backlog, list):
        errors.append("remediation_backlog must be a list")
    else:
        backlog_paths = [entry.get("path") for entry in backlog]
        if len(backlog_paths) != len(set(backlog_paths)):
            errors.append("remediation_backlog contains duplicate paths")
        expected = set(snapshot.get("remediate", []))
        actual = {path for path in backlog_paths if path}
        missing = expected - actual
        extra = actual - expected
        if missing:
            errors.append(f"remediation_backlog missing {len(missing)} current REMEDIATE item(s)")
        if extra:
            errors.append(f"remediation_backlog contains {len(extra)} non-REMEDIATE item(s)")

    return errors


def migrate_state(state_path: Path, repo: Path) -> dict:
    data = load_json(state_path)
    snapshot = data.setdefault("current_snapshot", {bucket: [] for bucket in BUCKETS})
    last_findings = data.get("last_review_findings", {})

    # Repair only explicit last-review decision mismatches. Never infer a new decision.
    for item in last_findings.get("items", []):
        path = item.get("path")
        bucket = DECISION_TO_BUCKET.get(item.get("decision"))
        if not path or not bucket:
            continue
        for existing_bucket in BUCKETS:
            if path in snapshot.setdefault(existing_bucket, []):
                snapshot[existing_bucket] = [p for p in snapshot[existing_bucket] if p != path]
        snapshot[bucket].append(path)

    existing_backlog = {entry.get("path"): entry for entry in data.get("remediation_backlog", []) if entry.get("path")}
    latest_reasons = {item.get("path"): item for item in last_findings.get("items", []) if item.get("decision") == "REMEDIATE"}
    checkpoint = data.get("last_reviewed_commit")
    reviewed_at = data.get("last_reviewed_at")

    backlog: list[dict] = []
    for path in snapshot.get("remediate", []):
        entry = existing_backlog.get(path, {})
        latest = latest_reasons.get(path)
        blob = entry.get("blob")
        if not blob and checkpoint:
            try:
                blob = git(repo, "rev-parse", f"{checkpoint}:{path}")
            except Exception:
                blob = None
        reason = latest.get("reason") if latest else entry.get("reason")
        reason_status = "structured" if reason else entry.get("reason_status", "legacy-unstructured")
        backlog.append({
            "path": path,
            "blob": latest.get("blob") if latest and latest.get("blob") else blob,
            "reason": reason,
            "reason_status": reason_status,
            "first_seen": entry.get("first_seen"),
            "last_seen": reviewed_at,
            "last_reviewed_commit": checkpoint,
        })
    data["remediation_backlog"] = backlog
    data.setdefault("run_lease", None)
    data["state_control_version"] = 4
    atomic_write_json(state_path, data)
    return data


def preflight(state_path: Path, repo: Path, max_artifacts: int) -> dict:
    data = load_json(state_path)
    errors = validate_state(data)
    if errors:
        return {"ok": False, "state_errors": errors}

    git(repo, "fetch", "origin", "main", "--quiet")
    base = data["last_reviewed_commit"]
    remote_head = git(repo, "rev-parse", "origin/main")
    ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", base, remote_head],
        cwd=repo,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0
    if not ancestor:
        return {"ok": False, "history_reconciliation_required": True, "base": base, "origin_main": remote_head}

    batch_head, batch_items = select_batch_head(repo, base, remote_head, max_artifacts)
    all_items = diff_strategy_items(repo, base, remote_head)
    untracked = [
        line[3:]
        for line in git(repo, "status", "--porcelain", "--untracked-files=all").splitlines()
        if line.startswith("?? ") and is_strategy_path(line[3:])
    ]
    deferred_items = diff_strategy_items(repo, batch_head, remote_head) if batch_head != remote_head else []
    return {
        "ok": True,
        "base_checkpoint": base,
        "origin_main": remote_head,
        "batch_head": batch_head,
        "batch_items": batch_items,
        "batch_artifact_count": len(batch_items),
        "total_unreviewed_artifact_count": len(all_items),
        "deferred": batch_head != remote_head,
        "deferred_items": deferred_items,
        "untracked_strategy_artifacts": untracked,
        "untracked_strategy_artifact_count": len(untracked),
    }


def apply_update(state_path: Path, payload_path: Path) -> dict:
    data = load_json(state_path)
    payload = load_json(payload_path)
    run_id = payload.get("run_id")
    lease = data.get("run_lease")
    if not run_id:
        raise RuntimeError("review update payload missing run_id")
    if not isinstance(lease, dict) or lease.get("run_id") != run_id:
        raise RuntimeError(
            f"run lease CAS failed: current={lease.get('run_id') if isinstance(lease, dict) else None} expected={run_id}"
        )
    base = payload["base_checkpoint"]
    snapshot_head = payload["reviewed_snapshot"]
    if data.get("last_reviewed_commit") != base:
        raise RuntimeError(
            f"checkpoint CAS failed: current={data.get('last_reviewed_commit')} expected={base}"
        )

    snapshot = data.setdefault("current_snapshot", {bucket: [] for bucket in BUCKETS})
    backlog = {entry.get("path"): entry for entry in data.get("remediation_backlog", []) if entry.get("path")}
    reviewed_at = payload.get("reviewed_at") or now_iso()

    normalized_items: list[dict] = []
    counts = {bucket: 0 for bucket in BUCKETS}
    for item in payload.get("items", []):
        decision = item["decision"]
        bucket = DECISION_TO_BUCKET.get(decision)
        if not bucket:
            raise RuntimeError(f"unknown decision: {decision}")
        path = item["path"]
        old_path = item.get("old_path")
        paths_to_remove = {path}
        if old_path:
            paths_to_remove.add(old_path)
        for existing_bucket in BUCKETS:
            snapshot[existing_bucket] = [p for p in snapshot.setdefault(existing_bucket, []) if p not in paths_to_remove]
        for previous_path in paths_to_remove:
            backlog.pop(previous_path, None)
        snapshot[bucket].append(path)
        counts[bucket] += 1

        normalized = dict(item)
        normalized_items.append(normalized)
        if decision == "REMEDIATE":
            existing = backlog.get(path, {})
            backlog[path] = {
                "path": path,
                "blob": item.get("blob"),
                "reason": item.get("reason"),
                "reason_status": "structured" if item.get("reason") else "missing",
                "first_seen": existing.get("first_seen") or reviewed_at,
                "last_seen": reviewed_at,
                "last_reviewed_commit": snapshot_head,
            }
        else:
            backlog.pop(path, None)

    for wiki_path in payload.get("ingested_wiki_records", []):
        if wiki_path not in data.setdefault("ingested_wiki_records", []):
            data["ingested_wiki_records"].append(wiki_path)

    if "pending_ingestion" in payload:
        data["pending_ingestion"] = payload["pending_ingestion"]

    data["remediation_backlog"] = sorted(backlog.values(), key=lambda x: x["path"])
    data["last_reviewed_commit"] = snapshot_head
    data["last_reviewed_at"] = reviewed_at
    data["last_review_findings"] = {
        "reviewed_snapshot": snapshot_head,
        "base_checkpoint": base,
        "decisions": counts,
        "items": normalized_items,
    }
    data["deferred_remote_head"] = payload.get("deferred_remote_head", snapshot_head)
    data["deferred_delta"] = payload.get("deferred_delta", [])
    data["state_control_version"] = 4

    errors = validate_state(data)
    if errors:
        raise RuntimeError("state invariant failure before write: " + "; ".join(errors))
    atomic_write_json(state_path, data)
    return {
        "updated": True,
        "last_reviewed_commit": snapshot_head,
        "decisions": counts,
        "remediation_backlog_count": len(data["remediation_backlog"]),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE)
    parser.add_argument("--repo", type=Path, default=DEFAULT_REPO)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate")
    sub.add_parser("migrate")

    pf = sub.add_parser("preflight")
    pf.add_argument("--max-artifacts", type=int, default=DEFAULT_MAX_ARTIFACTS)

    apply_cmd = sub.add_parser("apply")
    apply_cmd.add_argument("--payload", type=Path, required=True)

    args = parser.parse_args()
    try:
        if args.command == "validate":
            errors = validate_state(load_json(args.state))
            result = {"ok": not errors, "errors": errors}
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0 if not errors else 2
        if args.command == "migrate":
            data = migrate_state(args.state, args.repo)
            errors = validate_state(data)
            result = {"ok": not errors, "errors": errors, "remediation_backlog_count": len(data.get("remediation_backlog", []))}
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0 if not errors else 2
        if args.command == "preflight":
            result = preflight(args.state, args.repo, args.max_artifacts)
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0 if result.get("ok") else 5
        if args.command == "apply":
            result = apply_update(args.state, args.payload)
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
