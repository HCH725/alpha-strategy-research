#!/usr/bin/env python3
"""Deterministic state helper for Research Intake Review.

This file owns mechanics only: small immutable batch selection, state invariants,
remediation bookkeeping, checkpoint compare-and-swap writes, and durable Wiki
ingestion handoff. State control v5 intentionally has no long-lived review lease:
only the base checkpoint may authorize a completed frozen batch. Research judgment
remains in SKILL.md and ChatGPT.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import datetime as dt
import fcntl
import hashlib
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
# ponytail: bounded fetch for preflight (backward-compatible default; other
# local git calls stay unbounded). intake_control passes this explicitly.
FETCH_TIMEOUT_S = 60


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


@contextmanager
def state_mutex(state_path: Path):
    """Short kernel-managed mutex for atomic state read/check/write sections.

    The sidecar file is persistent, but the lock itself is held by the kernel and
    is released automatically on process exit. It is not a lease and cannot become
    stale or orphaned.
    """
    lock_path = state_path.with_name(state_path.name + ".mutex")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a+", encoding="utf-8") as lock_fh:
        fcntl.flock(lock_fh.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(lock_fh.fileno(), fcntl.LOCK_UN)


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


def git(repo: Path, *args: str, check: bool = True, timeout: int | None = None) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
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
        errors.append("run_lease is deprecated in state control v5 and must be null")

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
        for entry in backlog:
            if not isinstance(entry, dict):
                errors.append("remediation_backlog entries must be objects")
                continue
            required_keys = ("path", "blob", "reason", "reason_status", "first_seen", "last_seen", "last_reviewed_commit")
            missing_keys = [key for key in required_keys if key not in entry]
            if missing_keys:
                errors.append(f"remediation backlog entry missing key(s) for {entry.get('path')}: {missing_keys}")
        backlog_paths = [entry.get("path") for entry in backlog if isinstance(entry, dict)]
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

    pending = data.get("pending_ingestion", [])
    if not isinstance(pending, list):
        errors.append("pending_ingestion must be a list")
    else:
        seen_pending: set[tuple] = set()
        seen_wiki_paths: set[str] = set()
        for entry in pending:
            if not isinstance(entry, dict):
                errors.append("pending_ingestion entries must be objects")
                continue
            required = ("reviewed_commit", "path", "blob", "decision", "wiki_path", "wiki_content", "wiki_content_sha256")
            missing = [key for key in required if not entry.get(key)]
            if missing:
                errors.append(f"pending ingestion missing required field(s) for {entry.get('path')}: {missing}")
                continue
            decision = entry.get("decision")
            if decision not in ("PASS", "PASS-WITH-CAVEAT"):
                errors.append(f"pending ingestion has invalid decision for {entry.get('path')}: {decision}")
                continue
            bucket = DECISION_TO_BUCKET[decision]
            actual_bucket = memberships.get(entry.get("path"), [])
            if actual_bucket != [bucket]:
                errors.append(
                    f"pending ingestion bucket mismatch for {entry.get('path')}: {decision} vs {actual_bucket}"
                )
            wiki_path = str(entry.get("wiki_path"))
            if not wiki_path.startswith("quant/") or not wiki_path.endswith(".md") or ".." in Path(wiki_path).parts or Path(wiki_path).is_absolute():
                errors.append(f"pending ingestion has unsafe wiki_path: {wiki_path}")
            content = str(entry.get("wiki_content"))
            digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
            if digest != entry.get("wiki_content_sha256"):
                errors.append(f"pending ingestion content hash mismatch for {entry.get('path')}")
            expected_existing = entry.get("expected_existing_sha256")
            if expected_existing is not None and (
                not isinstance(expected_existing, str)
                or len(expected_existing) != 64
                or any(ch not in "0123456789abcdef" for ch in expected_existing.lower())
            ):
                errors.append(f"pending ingestion has invalid expected_existing_sha256 for {entry.get('path')}")
            key = (
                entry.get("reviewed_commit"),
                entry.get("path"),
                entry.get("blob"),
                decision,
                wiki_path,
            )
            if key in seen_pending:
                errors.append(f"pending_ingestion contains duplicate entry for {entry.get('path')}")
            seen_pending.add(key)
            if wiki_path in seen_wiki_paths:
                errors.append(f"pending_ingestion contains multiple unresolved writes for {wiki_path}")
            seen_wiki_paths.add(wiki_path)

    ingested = data.get("ingested_wiki_records", [])
    if not isinstance(ingested, list):
        errors.append("ingested_wiki_records must be a list")
    elif len(ingested) != len(set(ingested)):
        errors.append("ingested_wiki_records contains duplicates")

    return errors


def migrate_state(state_path: Path, repo: Path) -> dict:
    with state_mutex(state_path):
        return _migrate_state_locked(state_path, repo)


def _migrate_state_locked(state_path: Path, repo: Path) -> dict:
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
    data["run_lease"] = None
    data.setdefault("pending_ingestion", [])
    data["state_control_version"] = 5
    atomic_write_json(state_path, data)
    return data


def preflight(state_path: Path, repo: Path, max_artifacts: int,
              fetch_timeout: int | None = FETCH_TIMEOUT_S) -> dict:
    data = load_json(state_path)
    errors = validate_state(data)
    if errors:
        return {"ok": False, "state_errors": errors}

    # Bounded fetch: TimeoutExpired propagates to the caller (intake_control
    # maps it to transient). All CAS/diff/batch semantics below are unchanged.
    git(repo, "fetch", "origin", "main", "--quiet", timeout=fetch_timeout)
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


def apply_update(state_path: Path, payload_path: Path, repo: Path) -> dict:
    with state_mutex(state_path):
        return _apply_update_locked(state_path, payload_path, repo)


def _apply_update_locked(state_path: Path, payload_path: Path, repo: Path) -> dict:
    data = load_json(state_path)
    errors = validate_state(data)
    if errors:
        raise RuntimeError("state invariant failure before apply: " + "; ".join(errors))

    payload = load_json(payload_path)
    base = payload["base_checkpoint"]
    snapshot_head = payload["reviewed_snapshot"]
    if data.get("last_reviewed_commit") != base:
        raise RuntimeError(
            f"checkpoint CAS failed: current={data.get('last_reviewed_commit')} expected={base}"
        )

    ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", base, snapshot_head],
        cwd=repo,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0
    if not ancestor:
        raise RuntimeError(f"reviewed_snapshot is not a descendant of base checkpoint: {base}..{snapshot_head}")

    expected_items = diff_strategy_items(repo, base, snapshot_head)
    expected_by_path = {item["path"]: item for item in expected_items}
    payload_items = payload.get("items", [])
    payload_paths = [item.get("path") for item in payload_items]
    if len(payload_paths) != len(set(payload_paths)):
        raise RuntimeError("review payload contains duplicate artifact paths")
    if set(payload_paths) != set(expected_by_path):
        missing = sorted(set(expected_by_path) - set(payload_paths))
        extra = sorted(set(payload_paths) - set(expected_by_path))
        raise RuntimeError(f"review payload does not cover frozen strategy delta: missing={missing} extra={extra}")

    accepted_by_path: dict[str, dict] = {}
    touched_paths: set[str] = set()
    for item in payload_items:
        path = item["path"]
        expected = expected_by_path[path]
        if item.get("status") != expected.get("status"):
            raise RuntimeError(
                f"status mismatch for {path}: payload={item.get('status')} expected={expected.get('status')}"
            )
        if expected.get("old_path") and item.get("old_path") != expected.get("old_path"):
            raise RuntimeError(f"rename old_path mismatch for {path}")
        decision = item.get("decision")
        if decision not in DECISION_TO_BUCKET:
            raise RuntimeError(f"unknown decision for {path}: {decision}")
        if str(expected.get("status", "")).startswith("D") and decision != "REJECT":
            raise RuntimeError(f"deleted artifact must resolve to REJECT: {path}")
        if decision in ("PASS", "PASS-WITH-CAVEAT"):
            if str(expected.get("status", "")).startswith("D"):
                raise RuntimeError(f"deleted artifact cannot enter pending ingestion: {path}")
            if not item.get("blob"):
                raise RuntimeError(f"accepted artifact requires immutable blob identity: {path}")
            accepted_by_path[path] = item
        touched_paths.add(path)
        if item.get("old_path"):
            touched_paths.add(item["old_path"])

    new_pending = payload.get("pending_ingestion", [])
    pending_paths = [entry.get("path") for entry in new_pending]
    if len(pending_paths) != len(set(pending_paths)):
        raise RuntimeError("review payload contains duplicate pending-ingestion paths")
    if set(pending_paths) != set(accepted_by_path):
        missing = sorted(set(accepted_by_path) - set(pending_paths))
        extra = sorted(set(pending_paths) - set(accepted_by_path))
        raise RuntimeError(f"pending ingestion must exactly match accepted items: missing={missing} extra={extra}")
    for entry in new_pending:
        path = entry["path"]
        item = accepted_by_path[path]
        if entry.get("reviewed_commit") != snapshot_head:
            raise RuntimeError(f"pending reviewed_commit mismatch for {path}")
        if entry.get("blob") != item.get("blob") or entry.get("decision") != item.get("decision"):
            raise RuntimeError(f"pending identity mismatch for {path}")
        if not entry.get("wiki_path") or not entry.get("wiki_content") or not entry.get("wiki_content_sha256"):
            raise RuntimeError(f"pending ingestion requires wiki_path/content/hash for {path}")
        digest = hashlib.sha256(str(entry["wiki_content"]).encode("utf-8")).hexdigest()
        if digest != entry.get("wiki_content_sha256"):
            raise RuntimeError(f"pending content hash mismatch for {path}")

    snapshot = data.setdefault("current_snapshot", {bucket: [] for bucket in BUCKETS})
    backlog = {entry.get("path"): entry for entry in data.get("remediation_backlog", []) if entry.get("path")}
    reviewed_at = payload.get("reviewed_at") or now_iso()

    normalized_items: list[dict] = []
    counts = {bucket: 0 for bucket in BUCKETS}
    for item in payload_items:
        decision = item["decision"]
        bucket = DECISION_TO_BUCKET[decision]
        path = item["path"]
        old_path = item.get("old_path")
        paths_to_remove = {path}
        if old_path:
            paths_to_remove.add(old_path)
        existing_backlog_entry = backlog.get(path, {})
        for existing_bucket in BUCKETS:
            snapshot[existing_bucket] = [p for p in snapshot.setdefault(existing_bucket, []) if p not in paths_to_remove]
        for previous_path in paths_to_remove:
            backlog.pop(previous_path, None)
        snapshot[bucket].append(path)
        counts[bucket] += 1

        normalized = dict(item)
        normalized_items.append(normalized)
        if decision == "REMEDIATE":
            backlog[path] = {
                "path": path,
                "blob": item.get("blob"),
                "reason": item.get("reason"),
                "reason_status": "structured" if item.get("reason") else "missing",
                "first_seen": existing_backlog_entry.get("first_seen") or reviewed_at,
                "last_seen": reviewed_at,
                "last_reviewed_commit": snapshot_head,
            }

    pending = [entry for entry in data.get("pending_ingestion", []) if entry.get("path") not in touched_paths]
    pending.extend(dict(entry) for entry in new_pending)
    data["pending_ingestion"] = pending

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
    data["state_control_version"] = 5

    errors = validate_state(data)
    if errors:
        raise RuntimeError("state invariant failure before write: " + "; ".join(errors))
    atomic_write_json(state_path, data)
    return {
        "updated": True,
        "last_reviewed_commit": snapshot_head,
        "decisions": counts,
        "remediation_backlog_count": len(data["remediation_backlog"]),
        "pending_ingestion_count": len(data.get("pending_ingestion", [])),
    }


def complete_ingestion(state_path: Path, payload_path: Path) -> dict:
    with state_mutex(state_path):
        return _complete_ingestion_locked(state_path, payload_path)


def _complete_ingestion_locked(state_path: Path, payload_path: Path) -> dict:
    data = load_json(state_path)
    payload = load_json(payload_path)
    pending = list(data.get("pending_ingestion", []))
    ingested = data.setdefault("ingested_wiki_records", [])

    completed_count = 0
    for completed in payload.get("completed", []):
        key = (
            completed.get("reviewed_commit"),
            completed.get("path"),
            completed.get("blob"),
            completed.get("decision"),
            completed.get("wiki_path"),
        )
        completed_hash = completed.get("wiki_content_sha256")
        match_index = None
        for index, entry in enumerate(pending):
            entry_key = (
                entry.get("reviewed_commit"),
                entry.get("path"),
                entry.get("blob"),
                entry.get("decision"),
                entry.get("wiki_path"),
            )
            if entry_key == key:
                if completed_hash != entry.get("wiki_content_sha256"):
                    raise RuntimeError(f"completed Wiki content hash does not match pending item: {key}")
                match_index = index
                break
        wiki_path = completed.get("wiki_path")
        if match_index is None:
            if wiki_path and wiki_path in ingested:
                continue
            raise RuntimeError(f"pending ingestion item not found for completion: {key}")
        pending.pop(match_index)
        if wiki_path and wiki_path not in ingested:
            ingested.append(wiki_path)
        completed_count += 1

    data["pending_ingestion"] = pending
    data["state_control_version"] = 5
    errors = validate_state(data)
    if errors:
        raise RuntimeError("state invariant failure before ingestion completion write: " + "; ".join(errors))
    atomic_write_json(state_path, data)
    return {
        "updated": bool(completed_count),
        "completed_count": completed_count,
        "pending_ingestion_count": len(pending),
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

    complete_cmd = sub.add_parser("complete-ingestion")
    complete_cmd.add_argument("--payload", type=Path, required=True)

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
            result = apply_update(args.state, args.payload, args.repo)
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0
        if args.command == "complete-ingestion":
            result = complete_ingestion(args.state, args.payload)
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
