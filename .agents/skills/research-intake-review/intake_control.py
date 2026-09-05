#!/usr/bin/env python3
"""Research Intake Review CONTROL PLANE V6 entrypoint.

Version contract (frozen for this release): v6 entrypoint operates over frozen
state schema/control v5. SUPPORTED_STATE_VERSIONS=(5,); unknown versions are
rejected deterministically; no canonical migration is performed here.

Launched locally by Hermes `default` from the repository workdir. Reads
SKILL.md and canonical state using normal local file IO, computes policy
SHA-256, runs review_state validate/preflight, and returns structured JSON.
Uses review_state functions for validate/preflight/apply/complete-ingestion
semantics; never duplicates CAS/coverage logic.

Failure classes: transient = fetch/network transport only (retryable, whitelist
below); deterministic = invariant/CAS/coverage/contract/bad-revision/object/
not-a-repo/invalid-checkpoint (not retryable). The recurring Hermes execution
path is local and does not depend on CatDesk.

Wiki safety is two layers: (1) canonical invariant owned by
review_state.validate_state (quant/ prefix, .md suffix, no .., no absolute)
aborts ingestion globally as deterministic; (2) executor-local hardening in
is_safe_wiki_path/guarded_target (backslash, dot segment, double-slash,
whitespace, symlink, resolved containment) blocks only that item. The executor
is best-effort local fail-closed, not an atomic sandbox: it checks before and
rechecks target/parents after write, then read-back verifies hash.

Fetch/network calls made directly by this entrypoint use timeout=60s; the
delegated review_state.preflight fetch is likewise bounded (fetch_timeout=60s
default, TimeoutExpired maps to transient here).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import review_state as rs
except ImportError:  # allow `python intake_control.py` from skill dir
    from . import review_state as rs  # type: ignore

CONTROL_PLANE = "v6"
CONTROL_PLANE_VERSION = 6
# Frozen contract: v6 entrypoint over state schema/control v5 only.
SUPPORTED_STATE_VERSIONS = (5,)
FETCH_TIMEOUT_S = 60
FAIL_OK = "ok"
FAIL_TRANSIENT = "transient"
FAIL_DETERMINISTIC = "deterministic"

# ponytail: tight whitelist; deterministic takes precedence over transient.
# Transport-only retryable markers (fetch/network). Anything else (bad
# revision/object, not-a-repo, invalid checkpoint/contract) is deterministic.
_TRANSIENT_HINTS = (
    "could not resolve",
    "unable to access",
    "connection refused",
    "connection reset",
    "connection timed out",
    "connection ",
    "timed out",
    "timeout",
    "timedout",
    "temporary failure",
    "network is unreachable",
    "network unreachable",
    "no route to host",
    "name resolution",
    "getaddrinfo",
    "failed to connect",
    "the remote end hung up",
    "remote end hung up",
    "unable to connect",
    "could not read from remote",
    "failed to fetch",
    "fetch failed",
    "transient fetch failed",
    "operation timed out",
)
_DETERMINISTIC_HINTS = (
    "bad revision",
    "unknown revision",
    "unknown commit",
    "bad object",
    "ambiguous argument",
    "not a git repository",
    "does not appear to be a git repository",
    "not a commit",
    "no such",
    "invalid checkpoint",
    "checkpoint cas",
    "cas failed",
    "coverage",
    "pending ingestion",
    "invariant",
    "hash mismatch",
    "bucket",
    "malformed",
    "unsafe wiki",
    "unknown decision",
    "duplicate",
    "deleted artifact",
    "rename",
    "descendant",
    "ancestry",
    "unsupported state_control_version",
    "unsupported version",
)


def _version_contract_note() -> dict:
    return {
        "entrypoint": CONTROL_PLANE,
        "entrypoint_version": CONTROL_PLANE_VERSION,
        "supported_state_versions": list(SUPPORTED_STATE_VERSIONS),
        "note": "v6 entrypoint over frozen state schema/control v5; no canonical migration in this release",
    }


def _check_supported_version(data: dict) -> str | None:
    """Return deterministic error string if state_control_version unsupported, else None."""
    ver = data.get("state_control_version")
    if ver not in SUPPORTED_STATE_VERSIONS:
        return (
            f"unsupported state_control_version {ver!r}; "
            f"supported={list(SUPPORTED_STATE_VERSIONS)} "
            "(v6 entrypoint over frozen v5; no migration)"
        )
    return None


def _classify_git_failure(msg: str) -> str:
    """Tight classifier: deterministic markers win; else transient whitelist; else deterministic."""
    low = (msg or "").lower()
    if any(k in low for k in _DETERMINISTIC_HINTS):
        return FAIL_DETERMINISTIC
    if any(k in low for k in _TRANSIENT_HINTS):
        return FAIL_TRANSIENT
    # Bare git/origin/fetch noise without transport proof is deterministic
    # (fail-closed: do not mask contract errors as retryable).
    return FAIL_DETERMINISTIC

DEFAULT_STATE = Path("/Users/hong/workspace/alpha-strategy-review-state.json")
DEFAULT_REPO = Path("/Users/hong/workspace/alpha-strategy-research")
DEFAULT_SKILL = Path(__file__).with_name("SKILL.md")
DEFAULT_WIKI_ROOT = Path("/Users/hong/.hermes/wiki")
DEFAULT_MAX_ARTIFACTS = 5


class BlockedIngestion(Exception):
    pass


def read_policy_text(skill_path: Path) -> str:
    # ponytail: local IO only; never CatDesk dedicated read.
    return skill_path.read_text(encoding="utf-8")


def policy_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def summarize_state(data: dict) -> dict:
    snap = data.get("current_snapshot", {})
    return {
        "last_reviewed_commit": data.get("last_reviewed_commit"),
        "last_reviewed_at": data.get("last_reviewed_at"),
        "state_control_version": data.get("state_control_version"),
        "run_lease": data.get("run_lease"),
        "bucket_counts": {b: len(snap.get(b, [])) for b in rs.BUCKETS},
        "pending_ingestion_count": len(data.get("pending_ingestion", [])),
        "ingested_wiki_records_count": len(data.get("ingested_wiki_records", [])),
        "remediation_backlog_count": len(data.get("remediation_backlog", [])),
    }


def summarize_pending(data: dict) -> dict:
    items = []
    for e in data.get("pending_ingestion", []):
        items.append({
            "reviewed_commit": e.get("reviewed_commit"),
            "path": e.get("path"),
            "blob": e.get("blob"),
            "decision": e.get("decision"),
            "wiki_path": e.get("wiki_path"),
            "wiki_content_sha256": e.get("wiki_content_sha256"),
            "has_expected_existing_sha256": e.get("expected_existing_sha256") is not None,
        })
    return {"count": len(items), "items": items}


def list_untracked_local(repo: Path) -> list[str]:
    """Local `git status` visibility-only list. Never reviews/stages/deletes."""
    proc = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=all"],
        cwd=repo, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"git status failed: {proc.stderr.strip()}")
    out: list[str] = []
    for line in proc.stdout.splitlines():
        if line.startswith("?? ") and rs.is_strategy_path(line[3:]):
            out.append(line[3:])
    return sorted(out)


def _catdesk_note() -> dict:
    # Backward-compatible diagnostics field retained for callers/tests. The
    # recurring Hermes path is fully local and has no CatDesk dependency.
    return {
        "dedicated_read_required": False,
        "invocation": "local-hermes",
        "read_invalid_argument_tolerated": True,
        "note": "bootstrap uses local file IO; recurring Hermes execution has no CatDesk dependency",
    }


def bootstrap(state_path: Path = DEFAULT_STATE, repo: Path = DEFAULT_REPO,
              skill_path: Path = DEFAULT_SKILL, max_artifacts: int = DEFAULT_MAX_ARTIFACTS,
              fetch: bool = True) -> dict:
    """Read-only bootstrap. Never mutates state. Returns structured JSON."""
    try:
        policy_text = read_policy_text(skill_path)
    except Exception as exc:
        return {"control_plane": CONTROL_PLANE, "failure_class": FAIL_DETERMINISTIC,
                "error": f"policy read failed: {exc}", "catdesk": _catdesk_note()}
    phash = policy_sha256(policy_text)
    try:
        data = rs.load_json(state_path)
    except Exception as exc:
        return {"control_plane": CONTROL_PLANE, "control_plane_version": CONTROL_PLANE_VERSION,
                "policy_sha256": phash, "failure_class": FAIL_DETERMINISTIC,
                "error": f"state read failed: {exc}", "catdesk": _catdesk_note(),
                "version_contract": _version_contract_note()}
    ver_err = _check_supported_version(data)
    errors = rs.validate_state(data)
    if ver_err:
        errors = [ver_err] + list(errors)
    state_summary = summarize_state(data)
    pending_summary = summarize_pending(data)
    base = {"control_plane": CONTROL_PLANE, "control_plane_version": CONTROL_PLANE_VERSION,
            "policy_path": str(skill_path), "policy_text": policy_text, "policy_sha256": phash,
            "state_path": str(state_path), "repo": str(repo),
            "state_summary": state_summary, "pending_summary": pending_summary,
            "version_contract": _version_contract_note(),
            "catdesk": _catdesk_note()}
    if errors:
        try:
            untracked = list_untracked_local(repo)
        except Exception:
            untracked = []
        base.update({"ok": False, "failure_class": FAIL_DETERMINISTIC,
                     "state_errors": errors,
                     "untracked_strategy_artifacts": untracked,
                     "untracked_note": "visibility-only; never reviewed, staged, deleted, or treated as reviewed"})
        return base
    if not fetch:
        try:
            untracked = list_untracked_local(repo)
        except Exception as exc:
            msg = str(exc)
            fclass = _classify_git_failure(msg)
            # Local status failure is contract/deterministic unless proven transport.
            return {**base, "ok": False, "failure_class": fclass,
                    "error": f"untracked list failed: {exc}", "offline": True}
        return {**base, "ok": True, "failure_class": FAIL_OK, "offline": True,
                "preflight": {"fetch_skipped": True, "base_checkpoint": data.get("last_reviewed_commit")},
                "batch": None,
                "untracked_strategy_artifacts": untracked,
                "untracked_note": "visibility-only; never reviewed, staged, deleted, or treated as reviewed"}
    try:
        pf = rs.preflight(state_path, repo, max_artifacts, fetch_timeout=FETCH_TIMEOUT_S)
    except Exception as exc:
        msg = str(exc)
        # TimeoutExpired has no message body; treat as transient transport.
        if isinstance(exc, subprocess.TimeoutExpired):
            msg = f"fetch timeout after {FETCH_TIMEOUT_S}s: {msg}"
            fclass = FAIL_TRANSIENT
        else:
            fclass = _classify_git_failure(msg)
        transient = (fclass == FAIL_TRANSIENT)
        try:
            untracked = list_untracked_local(repo)
        except Exception:
            untracked = []
        return {**base, "ok": False, "failure_class": fclass, "offline": transient,
                "error": msg,
                "untracked_strategy_artifacts": untracked,
                "untracked_note": "visibility-only; never reviewed, staged, deleted, or treated as reviewed"}
    if not pf.get("ok"):
        # history_reconciliation_required or state errors -> deterministic
        return {**base, "ok": False, "failure_class": FAIL_DETERMINISTIC,
                "preflight": pf,
                "batch": {"base_checkpoint": pf.get("base"), "origin_main": pf.get("origin_main"),
                          "batch_head": None, "batch_items": []},
                "untracked_strategy_artifacts": pf.get("untracked_strategy_artifacts", []) if isinstance(pf, dict) else [],
                "untracked_note": "visibility-only; never reviewed, staged, deleted, or treated as reviewed",
                "error": "preflight not ok (history reconciliation or invariant)"}
    batch = {"base_checkpoint": pf.get("base_checkpoint"), "origin_main": pf.get("origin_main"),
             "batch_head": pf.get("batch_head"), "batch_items": pf.get("batch_items", []),
             "batch_artifact_count": pf.get("batch_artifact_count"),
             "total_unreviewed_artifact_count": pf.get("total_unreviewed_artifact_count"),
             "deferred": pf.get("deferred"), "deferred_items": pf.get("deferred_items", [])}
    return {**base, "ok": True, "failure_class": FAIL_OK, "offline": False,
            "preflight": pf, "batch": batch,
            "untracked_strategy_artifacts": pf.get("untracked_strategy_artifacts", []),
            "untracked_note": "visibility-only; never reviewed, staged, deleted, or treated as reviewed"}


def status_report(state_path: Path = DEFAULT_STATE, repo: Path = DEFAULT_REPO,
                  skill_path: Path = DEFAULT_SKILL) -> dict:
    """Offline-safe read-only status. No fetch, no mutation."""
    return bootstrap(state_path, repo, skill_path, fetch=False)


def is_safe_wiki_path(wiki_path: str) -> tuple[bool, str]:
    """Executor-local hardening; canonical invariant stays in review_state.validate_state.

    Layer 1 (canonical, global deterministic abort via validate_state): must be
    under quant/, end .md, no .. segment, not absolute. Layer 2 (here, per-item
    BlockedIngestion): backslash/NUL, single-dot segment, double-slash,
    leading/trailing whitespace, empty part. No semantic drift: this function
    never loosens Layer 1, only adds Layer 2 fail-closed checks.
    """
    if not wiki_path or not isinstance(wiki_path, str):
        return False, "empty wiki_path"
    if "\\" in wiki_path or "\x00" in wiki_path:
        return False, "bad separator"
    p = Path(wiki_path)
    if p.is_absolute() or wiki_path.startswith("/"):
        return False, "absolute path"
    if ".." in p.parts or "." in p.parts:
        return False, "dotdot escape"
    if not wiki_path.startswith("quant/"):
        return False, "must be under quant/"
    if not wiki_path.endswith(".md"):
        return False, "must end .md"
    if "//" in wiki_path or wiki_path.strip() != wiki_path:
        return False, "whitespace/double-slash"
    if any(part == "" for part in wiki_path.split("/")):
        return False, "empty part"
    return True, "ok"


def guarded_target(wiki_root: Path, wiki_path: str) -> Path:
    """Best-effort local fail-closed guard (not an atomic sandbox).

    Checks lexical containment, refuses symlink on target and on every existing
    parent prefix up to the resolved root, then checks resolved containment.
    TOCTOU between check and write cannot be eliminated without a sandbox, so
    execute_ingestion rechecks target/parents after write before read-back hash.
    """
    ok, reason = is_safe_wiki_path(wiki_path)
    if not ok:
        raise BlockedIngestion(f"unsafe wiki_path {wiki_path!r}: {reason}")
    root = wiki_root.expanduser()
    root.mkdir(parents=True, exist_ok=True)
    try:
        root_res = root.resolve()
    except Exception as exc:
        raise BlockedIngestion(f"wiki root unresolvable: {exc}")
    if root_res.is_symlink():
        raise BlockedIngestion("wiki root is symlink")
    target = root_res / wiki_path
    # lexical containment (before symlink check)
    try:
        target.relative_to(root_res)
    except ValueError:
        raise BlockedIngestion("path escape outside wiki root")
    # refuse symlink on target itself
    if os.path.islink(target):
        raise BlockedIngestion(f"target is symlink: {wiki_path}")
    # refuse symlink on any existing parent prefix up to root
    cur = target.parent
    while True:
        if os.path.islink(cur):
            raise BlockedIngestion(f"parent is symlink: {cur}")
        if cur == root_res or cur.parent == cur:
            break
        # stop when we reach root_res; parents above root not checked
        try:
            cur.relative_to(root_res)
        except ValueError:
            break
        cur = cur.parent
        if len(str(cur)) < len(str(root_res)):
            break
    # resolved containment (follows non-symlink prefixes; if a missing part
    # resolves outside due to .. it would already be rejected lexically)
    try:
        res = target.resolve(strict=False)
        res.relative_to(root_res)
    except ValueError:
        raise BlockedIngestion("resolved path escapes wiki root")
    return target


def _sha_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _sha_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _atomic_write_text(target: Path, content: str) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    if os.path.islink(target.parent):
        raise BlockedIngestion("parent became symlink before write")
    fd, tmp_name = tempfile.mkstemp(prefix=".wiki.", suffix=".tmp", dir=target.parent)
    tmp = Path(tmp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(content)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, target)
        dir_fd = os.open(target.parent, os.O_RDONLY)
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)
    finally:
        if tmp.exists():
            try:
                tmp.unlink()
            except FileNotFoundError:
                pass


def _recheck_post_write(root_res: Path, target: Path, wiki_path: str) -> None:
    """Post-write fail-closed recheck: target/parents must not be symlinks and must stay under root."""
    if os.path.islink(target):
        raise BlockedIngestion(f"target became symlink after write: {wiki_path}")
    cur = target.parent
    while True:
        if os.path.islink(cur):
            raise BlockedIngestion(f"parent became symlink after write: {cur}")
        if cur == root_res or cur.parent == cur:
            break
        try:
            cur.relative_to(root_res)
        except ValueError:
            raise BlockedIngestion("post-write parent escapes wiki root")
        cur = cur.parent
        if len(str(cur)) < len(str(root_res)):
            break
    try:
        res = target.resolve(strict=False)
        res.relative_to(root_res)
    except ValueError:
        raise BlockedIngestion("post-write resolved path escapes wiki root")


def execute_ingestion(state_path: Path = DEFAULT_STATE,
                      wiki_root: Path = DEFAULT_WIKI_ROOT,
                      dry_run: bool = False) -> dict:
    """Deterministic pending-ingestion executor. Uses review_state.complete-ingestion.

    Writes only exact durable wiki_content, refuses symlink/path escape,
    verifies existing hash or expected_existing_sha256 before overwrite,
    atomically writes, post-write rechecks target/parent symlinks (best-effort
    local fail-closed, not an atomic sandbox), read-back verifies, then calls
    complete-ingestion. Blocked items remain pending.
    """
    data = rs.load_json(state_path)
    ver_err = _check_supported_version(data)
    errors = rs.validate_state(data)
    if ver_err:
        errors = [ver_err] + list(errors)
    if errors:
        raise RuntimeError("state invariant failure before ingestion: " + "; ".join(errors))
    pending = list(data.get("pending_ingestion", []))
    completed: list[dict] = []
    blocked: list[dict] = []
    wrote: list[dict] = []
    for entry in pending:
        path = entry.get("path", "<unknown>")
        wiki_path = entry.get("wiki_path", "")
        content = entry.get("wiki_content")
        want = entry.get("wiki_content_sha256")
        if not entry.get("reviewed_commit") or not path or not entry.get("blob") \
                or entry.get("decision") not in ("PASS", "PASS-WITH-CAVEAT") \
                or not wiki_path or content is None or not want:
            blocked.append({"path": path, "wiki_path": wiki_path, "reason": "malformed pending entry"})
            continue
        if _sha_text(str(content)) != want:
            raise RuntimeError(f"pending content hash mismatch for {path}")
        try:
            target = guarded_target(wiki_root, str(wiki_path))
        except BlockedIngestion as exc:
            blocked.append({"path": path, "wiki_path": wiki_path, "reason": str(exc)})
            continue
        if target.exists():
            if not target.is_file() or os.path.islink(target):
                blocked.append({"path": path, "wiki_path": wiki_path, "reason": "target not regular file"})
                continue
            cur_hash = _sha_file(target)
            if cur_hash == want:
                completed.append({"reviewed_commit": entry["reviewed_commit"], "path": path,
                                  "blob": entry["blob"], "decision": entry["decision"],
                                  "wiki_path": str(wiki_path), "wiki_content_sha256": want})
                continue
            exp = entry.get("expected_existing_sha256")
            if not exp or exp.lower() != cur_hash.lower():
                blocked.append({"path": path, "wiki_path": wiki_path, "reason": "guarded-overwrite-mismatch: existing differs and expected_existing_sha256 absent/mismatch"})
                continue
        if dry_run:
            wrote.append({"path": path, "wiki_path": wiki_path, "would_write": True})
            # in dry-run, count as would-complete (verified logically) but do not mutate
            completed.append({"reviewed_commit": entry["reviewed_commit"], "path": path,
                              "blob": entry["blob"], "decision": entry["decision"],
                              "wiki_path": str(wiki_path), "wiki_content_sha256": want})
            continue
        _atomic_write_text(target, str(content))
        # Post-write fail-closed recheck before trusting read-back (TOCTOU).
        try:
            root_res = wiki_root.expanduser().resolve()
        except Exception as exc:
            raise BlockedIngestion(f"wiki root unresolvable post-write: {exc}")
        try:
            _recheck_post_write(root_res, target, str(wiki_path))
        except BlockedIngestion as exc:
            blocked.append({"path": path, "wiki_path": wiki_path, "reason": str(exc)})
            continue
        back = _sha_file(target)
        if back != want:
            raise RuntimeError(f"read-back hash mismatch for {wiki_path}")
        wrote.append({"path": path, "wiki_path": str(target), "bytes": len(str(content).encode("utf-8"))})
        completed.append({"reviewed_commit": entry["reviewed_commit"], "path": path,
                          "blob": entry["blob"], "decision": entry["decision"],
                          "wiki_path": str(wiki_path), "wiki_content_sha256": want})
    if dry_run:
        return {"updated": False, "dry_run": True, "would_complete_count": len(completed),
                "would_complete": completed, "blocked": blocked, "blocked_count": len(blocked),
                "failure_class": FAIL_OK}
    if not completed:
        return {"updated": False, "completed_count": 0, "blocked": blocked,
                "blocked_count": len(blocked), "pending_ingestion_count": len(pending),
                "failure_class": FAIL_OK}
    fd, tmp_name = tempfile.mkstemp(prefix=".complete.", suffix=".json", dir="/tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump({"completed": completed}, fh, ensure_ascii=False, indent=2)
        result = rs.complete_ingestion(state_path, Path(tmp_name))
    finally:
        try:
            Path(tmp_name).unlink()
        except FileNotFoundError:
            pass
    result.update({"blocked": blocked, "blocked_count": len(blocked), "failure_class": FAIL_OK})
    return result


def apply_review(state_path: Path, payload_path: Path, repo: Path) -> dict:
    """Guarded apply: fresh fetch first (no offline advancement), then delegate.

    Uses review_state.apply_update for CAS + frozen-diff coverage; never duplicates.
    Version gate runs before fetch so unknown state versions fail deterministic
    without network. Fetch uses timeout=60s; transport failures are transient,
    bad-revision/object/not-a-repo/invalid-checkpoint are deterministic.
    """
    try:
        pre_data = rs.load_json(state_path)
    except Exception as exc:
        raise RuntimeError(f"state read failed: {exc}")
    ver_err = _check_supported_version(pre_data)
    if ver_err:
        raise RuntimeError(f"state invariant failure before apply: {ver_err}")
    try:
        proc = subprocess.run(["git", "fetch", "origin", "main", "--quiet"],
                              cwd=repo, text=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, timeout=FETCH_TIMEOUT_S)
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"transient fetch failed (timeout after {FETCH_TIMEOUT_S}s), refusing offline apply: {exc}")
    if proc.returncode != 0:
        detail = proc.stderr.strip()
        fclass = _classify_git_failure(detail or "git fetch failed")
        if fclass == FAIL_TRANSIENT:
            raise RuntimeError(f"transient fetch failed, refusing offline apply: {detail}")
        raise RuntimeError(f"deterministic fetch/contract failure, refusing apply: {detail}")
    return rs.apply_update(state_path, payload_path, repo)


def main() -> int:
    ap = argparse.ArgumentParser(description="Intake Review control plane v6")
    ap.add_argument("--state", type=Path, default=DEFAULT_STATE)
    ap.add_argument("--repo", type=Path, default=DEFAULT_REPO)
    ap.add_argument("--skill", type=Path, default=DEFAULT_SKILL)
    ap.add_argument("--wiki-root", type=Path, default=DEFAULT_WIKI_ROOT)
    ap.add_argument("--max-artifacts", type=int, default=DEFAULT_MAX_ARTIFACTS)
    sub = ap.add_subparsers(dest="command", required=True)
    b = sub.add_parser("bootstrap", help="read-only v6 bootstrap (validate+preflight)")
    b.add_argument("--no-fetch", action="store_true", help="offline diagnostic: skip fetch")
    sub.add_parser("status", help="read-only offline status (no fetch, no mutation)")
    ig = sub.add_parser("ingest-pending", help="guarded pending-ingestion executor")
    ig.add_argument("--dry-run", action="store_true", help="preview without wiki/state mutation")
    al = sub.add_parser("apply", help="guarded apply (fetch + CAS + coverage)")
    al.add_argument("--payload", type=Path, required=True)
    args = ap.parse_args()
    try:
        if args.command == "bootstrap":
            res = bootstrap(args.state, args.repo, args.skill, args.max_artifacts, fetch=not args.no_fetch)
            print(json.dumps(res, ensure_ascii=False, indent=2))
            if not res.get("ok"):
                return 3 if res.get("failure_class") == FAIL_TRANSIENT else 2
            return 0
        if args.command == "status":
            res = status_report(args.state, args.repo, args.skill)
            print(json.dumps(res, ensure_ascii=False, indent=2))
            if not res.get("ok"):
                return 3 if res.get("failure_class") == FAIL_TRANSIENT else 2
            return 0
        if args.command == "ingest-pending":
            res = execute_ingestion(args.state, args.wiki_root, dry_run=args.dry_run)
            print(json.dumps(res, ensure_ascii=False, indent=2))
            return 0
        if args.command == "apply":
            res = apply_review(args.state, args.payload, args.repo)
            print(json.dumps(res, ensure_ascii=False, indent=2))
            return 0
    except BlockedIngestion as exc:
        print(json.dumps({"ok": False, "failure_class": FAIL_DETERMINISTIC, "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 2
    except RuntimeError as exc:
        msg = str(exc)
        # Tight whitelist: deterministic markers win; else transient transport; else deterministic.
        fclass = _classify_git_failure(msg)
        # Explicit transient prefix from fetch wrapper stays transient unless a
        # deterministic marker also matches (classifier already handles precedence).
        if "transient fetch failed" in msg.lower() and fclass != FAIL_DETERMINISTIC:
            fclass = FAIL_TRANSIENT
        print(json.dumps({"ok": False, "failure_class": fclass, "error": msg}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 3 if fclass == FAIL_TRANSIENT else 2
    except Exception as exc:
        print(json.dumps({"ok": False, "failure_class": FAIL_DETERMINISTIC, "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
