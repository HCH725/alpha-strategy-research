#!/usr/bin/env python3
"""Stdlib unit/integration tests for Research Intake Review CONTROL PLANE V6.

Covers: bootstrap without CatDesk read (behavioral, no source-text checks),
run_lease null invariant, version-contract gate (unknown version deterministic),
runtime delegation to review_state (validate/preflight/apply/complete),
tight transient/deterministic classification (does-not-appear deterministic),
bounded preflight fetch timeout with no semantic drift, CAS loser abort, frozen
coverage mismatch abort, rename old_path mismatch, deleted-D must be REJECT,
indivisible-first-commit batch, accepted item requires matching pending,
exact-hash idempotent ingestion, guarded overwrite, path escape/symlink
rejection + post-write recheck, untracked visibility-only, dry-run/status
offline. Uses only stdlib unittest + temp dirs; never touches canonical state/wiki.
"""

import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1] / ".agents" / "skills" / "research-intake-review"
sys.path.insert(0, str(SKILL_DIR))
import intake_control as ic
import review_state as rs


def run_git(repo: Path, *args: str) -> str:
    proc = subprocess.run(["git", *args], cwd=repo, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc.stdout.strip()


def init_repo(tmp: Path, name: str = "repo") -> Path:
    repo = tmp / name
    repo.mkdir(parents=True, exist_ok=True)
    run_git(repo, "init", "-b", "main")
    run_git(repo, "config", "user.email", "test@example.com")
    run_git(repo, "config", "user.name", "Test")
    run_git(repo, "config", "commit.gpgsign", "false")
    return repo


def commit_file(repo: Path, rel: str, content: str, msg: str) -> str:
    p = repo / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    run_git(repo, "add", rel)
    run_git(repo, "commit", "-m", msg, "--quiet")
    return run_git(repo, "rev-parse", "HEAD")


def add_origin_and_push(repo: Path, tmp: Path, name: str = "origin.git") -> Path:
    origin = tmp / name
    proc = subprocess.run(["git", "init", "--bare", str(origin)], text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise RuntimeError(f"bare init failed: {proc.stderr}")
    run_git(repo, "remote", "add", "origin", str(origin))
    run_git(repo, "push", "-u", "origin", "main", "--quiet")
    return origin


def minimal_state(base: str) -> dict:
    return {
        "schema": "alpha-strategy-research-review-state-v1",
        "repository": "test",
        "branch": "main",
        "run_lease": None,
        "last_reviewed_commit": base,
        "last_reviewed_at": "2026-09-05T00:00:00+08:00",
        "current_snapshot": {"pass": [], "pass_with_caveat": [], "remediate": [], "reject": []},
        "last_review_findings": {"reviewed_snapshot": base, "base_checkpoint": base,
                                 "decisions": {"pass": 0, "pass_with_caveat": 0, "remediate": 0, "reject": 0},
                                 "items": []},
        "remediation_backlog": [],
        "pending_ingestion": [],
        "ingested_wiki_records": [],
        "deferred_remote_head": base,
        "deferred_delta": [],
        "state_control_version": 5,
    }


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def blob_of(repo: Path, rev: str, rel: str) -> str:
    return run_git(repo, "rev-parse", f"{rev}:{rel}")


class IntakeControlV6Test(unittest.TestCase):
    def setUp(self):
        self.tmpd = tempfile.TemporaryDirectory()
        self.tmp = Path(self.tmpd.name)
        self.skill = self.tmp / "SKILL.md"
        self.skill.write_text("# test policy v6\ncontent\n", encoding="utf-8")
        self.wiki = self.tmp / "wiki"

    def tearDown(self):
        self.tmpd.cleanup()

    def test_bootstrap_without_catdesk_read(self):
        repo = init_repo(self.tmp, "repo1")
        base = commit_file(repo, "a-2026-09-05.md", "hello\n", "init")
        st = self.tmp / "state.json"
        write_json(st, minimal_state(base))
        # simulate CatDesk dedicated-read INVALID_ARGUMENT env; bootstrap must ignore it
        # (behavioral: uses only local file IO, returns local policy text/hash).
        os.environ["CATDESK_READ_ERROR"] = "INVALID_ARGUMENT"
        try:
            res = ic.bootstrap(st, repo, self.skill, fetch=False)
        finally:
            os.environ.pop("CATDESK_READ_ERROR", None)
        self.assertTrue(res.get("ok"))
        self.assertEqual(res.get("failure_class"), "ok")
        self.assertEqual(res.get("policy_text"), "# test policy v6\ncontent\n")
        self.assertEqual(res.get("policy_sha256"), sha_text("# test policy v6\ncontent\n"))
        for key in ("policy_text", "policy_sha256", "state_summary", "pending_summary",
                    "untracked_strategy_artifacts", "failure_class", "version_contract"):
            self.assertIn(key, res, f"missing {key}")
        self.assertFalse(res["catdesk"]["dedicated_read_required"])
        self.assertTrue(res["catdesk"]["read_invalid_argument_tolerated"])
        # version contract is explicit in output (no source-text inspection).
        vc = res.get("version_contract", {})
        self.assertEqual(vc.get("entrypoint"), "v6")
        self.assertIn(5, vc.get("supported_state_versions", []))
        self.assertEqual(res["state_summary"].get("state_control_version"), 5)

    def test_run_lease_null_invariant(self):
        repo = init_repo(self.tmp, "repo2")
        base = commit_file(repo, "a-2026-09-05.md", "x\n", "init")
        st = self.tmp / "state.json"
        data = minimal_state(base)
        data["run_lease"] = {"run_id": "r1", "owner": "x", "started_at": "2026-09-05T00:00:00+08:00", "stale_after_minutes": 180}
        write_json(st, data)
        errs = rs.validate_state(data)
        self.assertTrue(any("run_lease" in e for e in errs))
        res = ic.bootstrap(st, repo, self.skill, fetch=False)
        self.assertEqual(res.get("failure_class"), "deterministic")
        self.assertFalse(res.get("ok"))
        # valid null passes
        data["run_lease"] = None
        write_json(st, data)
        res2 = ic.bootstrap(st, repo, self.skill, fetch=False)
        self.assertEqual(res2.get("failure_class"), "ok")

    def _repo_with_diff(self, tag: str):
        repo = init_repo(self.tmp, f"repo-{tag}")
        base = commit_file(repo, "base-2026-09-05.md", "base\n", "base")
        add_origin_and_push(repo, self.tmp / f"origin-{tag}", f"origin-{tag}.git")
        # second commit with one strategy file
        head = commit_file(repo, "new-strategy-2026-09-05.md", "new\n", "add strategy")
        run_git(repo, "push", "origin", "main", "--quiet")
        return repo, base, head

    def test_cas_loser_abort(self):
        repo, base, head = self._repo_with_diff("cas")
        st = self.tmp / "state-cas.json"
        write_json(st, minimal_state(base))
        blob = blob_of(repo, head, "new-strategy-2026-09-05.md")
        payload = {"base_checkpoint": base, "reviewed_snapshot": head,
                   "reviewed_at": "2026-09-05T00:00:00+08:00",
                   "items": [{"status": "A", "path": "new-strategy-2026-09-05.md", "blob": blob,
                              "decision": "REJECT", "reason": "dup", "auditor_status": "not-required"}],
                   "pending_ingestion": []}
        pp = self.tmp / "payload-cas.json"
        write_json(pp, payload)
        # first apply wins
        r1 = rs.apply_update(st, pp, repo)
        self.assertTrue(r1.get("updated"))
        # loser with same stale base must abort
        with self.assertRaises(RuntimeError) as ctx:
            rs.apply_update(st, pp, repo)
        self.assertIn("CAS", str(ctx.exception))
        # intake_control guarded apply also enforces CAS (fetch succeeds, then CAS fails)
        with self.assertRaises(RuntimeError) as ctx2:
            ic.apply_review(st, pp, repo)
        self.assertIn("CAS", str(ctx2.exception))

    def test_frozen_coverage_mismatch_abort(self):
        repo = init_repo(self.tmp, "repo-cov")
        base = commit_file(repo, "base-2026-09-05.md", "b\n", "base")
        add_origin_and_push(repo, self.tmp / "origin-cov", "origin-cov.git")
        commit_file(repo, "s1-2026-09-05.md", "1\n", "s1")
        commit_file(repo, "s2-2026-09-05.md", "2\n", "s2")
        run_git(repo, "push", "origin", "main", "--quiet")
        head = run_git(repo, "rev-parse", "HEAD")
        st = self.tmp / "state-cov.json"
        write_json(st, minimal_state(base))
        b1 = blob_of(repo, head, "s1-2026-09-05.md")
        # payload covers only s1, missing s2
        payload = {"base_checkpoint": base, "reviewed_snapshot": head,
                   "reviewed_at": "2026-09-05T00:00:00+08:00",
                   "items": [{"status": "A", "path": "s1-2026-09-05.md", "blob": b1,
                              "decision": "REJECT", "reason": "x", "auditor_status": "not-required"}],
                   "pending_ingestion": []}
        pp = self.tmp / "payload-cov.json"
        write_json(pp, payload)
        with self.assertRaises(RuntimeError) as ctx:
            rs.apply_update(st, pp, repo)
        self.assertIn("cover", str(ctx.exception).lower())

    def test_accepted_item_requires_matching_pending(self):
        repo, base, head = self._repo_with_diff("pend")
        st = self.tmp / "state-pend.json"
        write_json(st, minimal_state(base))
        blob = blob_of(repo, head, "new-strategy-2026-09-05.md")
        payload = {"base_checkpoint": base, "reviewed_snapshot": head,
                   "reviewed_at": "2026-09-05T00:00:00+08:00",
                   "items": [{"status": "A", "path": "new-strategy-2026-09-05.md", "blob": blob,
                              "decision": "PASS", "reason": "good", "auditor_status": "not-required"}],
                   "pending_ingestion": []}
        pp = self.tmp / "payload-pend.json"
        write_json(pp, payload)
        with self.assertRaises(RuntimeError) as ctx:
            rs.apply_update(st, pp, repo)
        self.assertIn("pending ingestion must exactly match", str(ctx.exception))

    def _pending_state(self, repo: Path, base: str, strategy: str, blob: str,
                       decision: str, wiki_path: str, content: str, exp_existing=None):
        st = minimal_state(base)
        bucket = rs.DECISION_TO_BUCKET[decision]
        st["current_snapshot"][bucket] = [strategy]
        entry = {"reviewed_commit": base, "path": strategy, "blob": blob,
                 "decision": decision, "wiki_path": wiki_path,
                 "wiki_content": content, "wiki_content_sha256": sha_text(content)}
        if exp_existing is not None:
            entry["expected_existing_sha256"] = exp_existing
        st["pending_ingestion"] = [entry]
        return st

    def test_exact_hash_idempotent_ingestion(self):
        repo = init_repo(self.tmp, "repo-idem")
        base = commit_file(repo, "a-2026-09-05.md", "a\n", "init")
        strategy = "idem-2026-09-05.md"
        blob = "0" * 40
        content = "idempotent wiki body\n"
        wiki_path = "quant/idem-test-2026-09-05.md"
        st_path = self.tmp / "state-idem.json"
        write_json(st_path, self._pending_state(repo, base, strategy, blob, "PASS", wiki_path, content))
        target = self.wiki / wiki_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        res = ic.execute_ingestion(st_path, self.wiki, dry_run=False)
        self.assertEqual(res.get("completed_count"), 1)
        self.assertEqual(res.get("blocked_count"), 0)
        data = json.loads(st_path.read_text(encoding="utf-8"))
        self.assertEqual(data.get("pending_ingestion"), [])
        self.assertIn(wiki_path, data.get("ingested_wiki_records", []))
        self.assertEqual(target.read_text(encoding="utf-8"), content)

    def test_guarded_overwrite(self):
        repo = init_repo(self.tmp, "repo-guard")
        base = commit_file(repo, "a-2026-09-05.md", "a\n", "init")
        strategy = "guard-2026-09-05.md"
        blob = "1" * 40
        old = "old body\n"
        new = "new body\n"
        wiki_path = "quant/guard-test-2026-09-05.md"
        # success when expected matches
        st1 = self.tmp / "state-g1.json"
        write_json(st1, self._pending_state(repo, base, strategy, blob, "PASS-WITH-CAVEAT",
                                            wiki_path, new, exp_existing=sha_text(old)))
        tgt = self.wiki / wiki_path
        tgt.parent.mkdir(parents=True, exist_ok=True)
        tgt.write_text(old, encoding="utf-8")
        r1 = ic.execute_ingestion(st1, self.wiki, dry_run=False)
        self.assertEqual(r1.get("completed_count"), 1)
        self.assertEqual(tgt.read_text(encoding="utf-8"), new)
        # blocked when expected mismatches
        st2 = self.tmp / "state-g2.json"
        write_json(st2, self._pending_state(repo, base, strategy, blob, "PASS",
                                            wiki_path, "another\n", exp_existing="0" * 64))
        tgt.write_text("different existing\n", encoding="utf-8")
        before = tgt.read_text(encoding="utf-8")
        r2 = ic.execute_ingestion(st2, self.wiki, dry_run=False)
        self.assertEqual(r2.get("completed_count"), 0)
        self.assertEqual(r2.get("blocked_count"), 1)
        self.assertEqual(tgt.read_text(encoding="utf-8"), before)
        data2 = json.loads(st2.read_text(encoding="utf-8"))
        self.assertEqual(len(data2.get("pending_ingestion")), 1)
        # blocked when no expected and differs
        st3 = self.tmp / "state-g3.json"
        write_json(st3, self._pending_state(repo, base, strategy, blob, "PASS", wiki_path, "another2\n"))
        r3 = ic.execute_ingestion(st3, self.wiki, dry_run=False)
        self.assertEqual(r3.get("blocked_count"), 1)

    def test_path_escape_symlink_rejection(self):
        repo = init_repo(self.tmp, "repo-esc")
        base = commit_file(repo, "a-2026-09-05.md", "a\n", "init")
        # Lexical escapes are caught by state invariants -> deterministic abort, no write.
        for bad in ("../escape.md", "quant/../escape.md", "/tmp/evil.md", "quant/../../etc/passwd"):
            st = self.tmp / f"state-esc-{abs(hash(bad))}.json"
            write_json(st, self._pending_state(repo, base, "esc-2026-09-05.md", "2" * 40,
                                               "PASS", bad, "evil\n"))
            with self.assertRaises(RuntimeError, msg=bad) as ctx:
                ic.execute_ingestion(st, self.wiki, dry_run=False)
            self.assertIn("unsafe", str(ctx.exception).lower() + "invariant")
            # also direct guard refuses
            with self.assertRaises(ic.BlockedIngestion):
                ic.guarded_target(self.wiki, bad)
            self.assertFalse((self.tmp / "escape.md").exists())
        # symlink target rejection
        qdir = self.wiki / "quant"
        qdir.mkdir(parents=True, exist_ok=True)
        outside = self.tmp / "outside.md"
        outside.write_text("outside\n", encoding="utf-8")
        link = qdir / "link-2026-09-05.md"
        try:
            link.symlink_to(outside)
        except FileExistsError:
            pass
        st4 = self.tmp / "state-sym.json"
        write_json(st4, self._pending_state(repo, base, "sym-2026-09-05.md", "3" * 40,
                                            "PASS", "quant/link-2026-09-05.md", "newlink\n"))
        r4 = ic.execute_ingestion(st4, self.wiki, dry_run=False)
        self.assertEqual(r4.get("blocked_count"), 1)
        self.assertEqual(outside.read_text(encoding="utf-8"), "outside\n")
        # parent symlink rejection
        realdir = self.tmp / "realdir"
        realdir.mkdir(exist_ok=True)
        parent_link = qdir / "sublink"
        if parent_link.exists() or parent_link.is_symlink():
            if parent_link.is_symlink():
                parent_link.unlink()
        parent_link.symlink_to(realdir)
        st5 = self.tmp / "state-psym.json"
        write_json(st5, self._pending_state(repo, base, "psym-2026-09-05.md", "4" * 40,
                                            "PASS", "quant/sublink/file-2026-09-05.md", "x\n"))
        r5 = ic.execute_ingestion(st5, self.wiki, dry_run=False)
        self.assertEqual(r5.get("blocked_count"), 1)

    def test_untracked_visibility_only(self):
        repo = init_repo(self.tmp, "repo-unt")
        base = commit_file(repo, "tracked-2026-09-05.md", "t\n", "init")
        st = self.tmp / "state-unt.json"
        write_json(st, minimal_state(base))
        # untracked strategy + non-strategy + nested (nested not strategy)
        (repo / "new-untracked-2026-09-05.md").write_text("u\n", encoding="utf-8")
        (repo / "README.md").write_text("readme\n", encoding="utf-8")
        (repo / "notes.txt").write_text("txt\n", encoding="utf-8")
        sub = repo / "sub"
        sub.mkdir(exist_ok=True)
        (sub / "nested-2026-09-05.md").write_text("n\n", encoding="utf-8")
        res = ic.bootstrap(st, repo, self.skill, fetch=False)
        self.assertIn("new-untracked-2026-09-05.md", res["untracked_strategy_artifacts"])
        self.assertNotIn("README.md", res["untracked_strategy_artifacts"])
        self.assertNotIn("notes.txt", res["untracked_strategy_artifacts"])
        self.assertNotIn("sub/nested-2026-09-05.md", res["untracked_strategy_artifacts"])
        self.assertIn("visibility-only", res["untracked_note"])
        # committed diff must not include untracked
        items = rs.diff_strategy_items(repo, base, base)
        self.assertEqual(items, [])

    def test_dry_run_and_status_offline(self):
        repo = init_repo(self.tmp, "repo-dry")
        base = commit_file(repo, "a-2026-09-05.md", "a\n", "init")
        strategy = "dry-2026-09-05.md"
        content = "dry body\n"
        wiki_path = "quant/dry-test-2026-09-05.md"
        st = self.tmp / "state-dry.json"
        write_json(st, self._pending_state(repo, base, strategy, "5" * 40, "PASS", wiki_path, content))
        r = ic.execute_ingestion(st, self.wiki, dry_run=True)
        self.assertTrue(r.get("dry_run"))
        self.assertEqual(r.get("would_complete_count"), 1)
        self.assertFalse((self.wiki / wiki_path).exists())
        data = json.loads(st.read_text(encoding="utf-8"))
        self.assertEqual(len(data.get("pending_ingestion")), 1)
        # status offline with no origin must still succeed
        s = ic.status_report(st, repo, self.skill)
        self.assertTrue(s.get("ok"))
        self.assertTrue(s.get("offline"))
        # apply with broken remote must refuse as transient (no offline advancement)
        bad_repo = init_repo(self.tmp, "repo-badremote")
        b2 = commit_file(bad_repo, "a-2026-09-05.md", "a\n", "init")
        run_git(bad_repo, "remote", "add", "origin", "/nonexistent/origin.git")
        st2 = self.tmp / "state-bad.json"
        write_json(st2, minimal_state(b2))
        pp = self.tmp / "payload-bad.json"
        write_json(pp, {"base_checkpoint": b2, "reviewed_snapshot": b2, "items": [], "pending_ingestion": []})
        with self.assertRaises(RuntimeError) as ctx:
            ic.apply_review(st2, pp, bad_repo)
        self.assertIn("fetch", str(ctx.exception).lower())
        # misconfigured origin is a contract failure: deterministic, no offline advancement
        self.assertIn("deterministic", str(ctx.exception).lower())

    def test_runtime_delegation_validate_preflight_apply_complete(self):
        # Behavioral delegation: patch review_state functions and verify the
        # entrypoint actually calls them at runtime (no source-text checks).
        from unittest import mock
        repo = init_repo(self.tmp, "repo-deleg")
        base = commit_file(repo, "a-2026-09-05.md", "a\n", "init")
        add_origin_and_push(repo, self.tmp / "origin-deleg", "origin-deleg.git")
        st = self.tmp / "state-deleg.json"
        write_json(st, minimal_state(base))
        # bootstrap(fetch=True) must call validate_state + preflight
        with mock.patch.object(rs, "validate_state", wraps=rs.validate_state) as mv, \
             mock.patch.object(rs, "preflight", wraps=rs.preflight) as mp:
            res = ic.bootstrap(st, repo, self.skill, fetch=True)
            self.assertTrue(mv.called, "bootstrap must call review_state.validate_state")
            self.assertTrue(mp.called, "bootstrap must call review_state.preflight")
            self.assertTrue(res.get("ok"))
        # status (fetch=False) must call validate_state but not preflight
        with mock.patch.object(rs, "validate_state", wraps=rs.validate_state) as mv2, \
             mock.patch.object(rs, "preflight", wraps=rs.preflight) as mp2:
            s = ic.status_report(st, repo, self.skill)
            self.assertTrue(mv2.called)
            self.assertFalse(mp2.called, "status must not call preflight (offline)")
            self.assertTrue(s.get("ok"))
        # apply_review must delegate to apply_update (fetch succeeds via local origin)
        head = commit_file(repo, "deleg-2026-09-05.md", "d\n", "add")
        run_git(repo, "push", "origin", "main", "--quiet")
        blob = blob_of(repo, head, "deleg-2026-09-05.md")
        payload = {"base_checkpoint": base, "reviewed_snapshot": head,
                   "reviewed_at": "2026-09-05T00:00:00+08:00",
                   "items": [{"status": "A", "path": "deleg-2026-09-05.md", "blob": blob,
                              "decision": "REJECT", "reason": "dup", "auditor_status": "not-required"}],
                   "pending_ingestion": []}
        pp = self.tmp / "payload-deleg.json"
        write_json(pp, payload)
        with mock.patch.object(rs, "apply_update", wraps=rs.apply_update) as ma:
            r = ic.apply_review(st, pp, repo)
            self.assertTrue(ma.called, "apply_review must call review_state.apply_update")
            self.assertTrue(r.get("updated"))
        # execute_ingestion must delegate to complete_ingestion on success
        st2 = self.tmp / "state-deleg2.json"
        content = "deleg wiki\n"
        write_json(st2, self._pending_state(repo, base, "x-2026-09-05.md", "9" * 40,
                                            "PASS", "quant/deleg-2026-09-05.md", content))
        # fix bucket membership for pending entry: add to pass bucket
        d2 = json.loads(st2.read_text(encoding="utf-8"))
        d2["current_snapshot"]["pass"] = ["x-2026-09-05.md"]
        # last_reviewed_commit must match pending reviewed_commit (base already does)
        write_json(st2, d2)
        with mock.patch.object(rs, "complete_ingestion", wraps=rs.complete_ingestion) as mc:
            r2 = ic.execute_ingestion(st2, self.wiki, dry_run=False)
            self.assertTrue(mc.called, "execute_ingestion must call review_state.complete_ingestion")
            self.assertEqual(r2.get("completed_count"), 1)

    def test_unknown_state_version_rejected(self):
        repo = init_repo(self.tmp, "repo-ver")
        base = commit_file(repo, "a-2026-09-05.md", "a\n", "init")
        st = self.tmp / "state-ver.json"
        data = minimal_state(base)
        data["state_control_version"] = 99
        write_json(st, data)
        res = ic.bootstrap(st, repo, self.skill, fetch=False)
        self.assertFalse(res.get("ok"))
        self.assertEqual(res.get("failure_class"), "deterministic")
        self.assertIn("unsupported state_control_version", str(res.get("state_errors")))
        # ingestion gate is deterministic
        with self.assertRaises(RuntimeError) as ctx:
            ic.execute_ingestion(st, self.wiki, dry_run=True)
        self.assertIn("unsupported state_control_version", str(ctx.exception))
        # apply gate runs before fetch: deterministic even with no origin
        pp = self.tmp / "payload-ver.json"
        write_json(pp, {"base_checkpoint": base, "reviewed_snapshot": base, "items": [], "pending_ingestion": []})
        with self.assertRaises(RuntimeError) as ctx2:
            ic.apply_review(st, pp, repo)
        self.assertIn("unsupported state_control_version", str(ctx2.exception))

    def test_transient_deterministic_classification(self):
        # Transport whitelist -> transient
        for msg in ("fatal: unable to access 'https://x': Could not resolve host",
                    "fatal: connection timed out",
                    "fetch timeout after 60s: timed out",
                    "fatal: the remote end hung up unexpectedly"):
            self.assertEqual(ic._classify_git_failure(msg), "transient", msg)
        # Contract errors -> deterministic (precedence over fetch/transport words).
        # Regression: 'does not appear to be a git repository' (misconfigured
        # origin) is deterministic, not transient.
        for msg in ("fatal: bad revision 'deadbeef'",
                    "fatal: bad object deadbeef",
                    "fatal: not a git repository (or any parent)",
                    "fatal: '/tmp/nope.git' does not appear to be a git repository",
                    "fatal: ambiguous argument 'x..y'",
                    "checkpoint CAS failed: current=abc expected=def",
                    "review payload does not cover frozen strategy delta",
                    "pending ingestion must exactly match accepted items",
                    "state invariant failure before apply: x",
                    "unsupported state_control_version 99",
                    "some random git error without whitelist"):
            self.assertEqual(ic._classify_git_failure(msg), "deterministic", msg)

    def test_does_not_appear_deterministic_regression(self):
        # End-to-end: misconfigured origin surfaces as deterministic, and apply
        # refuses without advancing state.
        repo = init_repo(self.tmp, "repo-noappear")
        b2 = commit_file(repo, "a-2026-09-05.md", "a\n", "init")
        run_git(repo, "remote", "add", "origin", "/nonexistent/origin.git")
        st = self.tmp / "state-noappear.json"
        write_json(st, minimal_state(b2))
        pp = self.tmp / "payload-noappear.json"
        write_json(pp, {"base_checkpoint": b2, "reviewed_snapshot": b2, "items": [], "pending_ingestion": []})
        with self.assertRaises(RuntimeError) as ctx:
            ic.apply_review(st, pp, repo)
        msg = str(ctx.exception)
        self.assertIn("fetch", msg.lower())
        self.assertIn("deterministic", msg.lower())
        self.assertEqual(ic._classify_git_failure(msg), "deterministic")
        # state file untouched by the refused apply
        data = json.loads(st.read_text(encoding="utf-8"))
        self.assertEqual(data.get("last_reviewed_commit"), b2)

    def test_preflight_fetch_timeout_bounded_no_drift(self):
        import inspect
        from unittest import mock
        # signature carries a bounded default
        sig = inspect.signature(rs.preflight)
        self.assertIn("fetch_timeout", sig.parameters)
        self.assertEqual(sig.parameters["fetch_timeout"].default, 60)
        self.assertEqual(getattr(rs, "FETCH_TIMEOUT_S", 60), 60)
        self.assertEqual(ic.FETCH_TIMEOUT_S, 60)
        # fetch goes through with the timeout kwarg (capture, then delegate)
        repo = init_repo(self.tmp, "repo-timeout")
        base = commit_file(repo, "a-2026-09-05.md", "a\n", "init")
        add_origin_and_push(repo, self.tmp / "origin-timeout", "origin-timeout.git")
        st = self.tmp / "state-timeout.json"
        write_json(st, minimal_state(base))
        real_git = rs.git
        seen = {}
        def spy_git(r, *a, **k):
            if a[:3] == ("fetch", "origin", "main"):
                seen.update(k)
            return real_git(r, *a, **k)
        with mock.patch.object(rs, "git", side_effect=spy_git):
            res = rs.preflight(st, repo, 5)
        self.assertTrue(res.get("ok"))
        self.assertEqual(seen.get("timeout"), 60)
        # explicit kwarg from the entrypoint matches the default: no drift
        with mock.patch.object(rs, "git", side_effect=spy_git):
            res2 = ic.bootstrap(st, repo, self.skill, fetch=True)
        self.assertTrue(res2.get("ok"))
        self.assertEqual(res.get("batch_head"), res2["batch"]["batch_head"])
        self.assertEqual(res.get("batch_items"), res2["batch"]["batch_items"])
        # TimeoutExpired during preflight maps to transient in bootstrap
        before = st.read_text(encoding="utf-8")
        with mock.patch.object(rs, "preflight", side_effect=subprocess.TimeoutExpired("git fetch", 60)):
            res3 = ic.bootstrap(st, repo, self.skill, fetch=True)
        self.assertFalse(res3.get("ok"))
        self.assertEqual(res3.get("failure_class"), "transient")
        self.assertTrue(res3.get("offline"))
        self.assertEqual(st.read_text(encoding="utf-8"), before)

    def test_rename_old_path_mismatch(self):
        repo = init_repo(self.tmp, "repo-rename")
        base = commit_file(repo, "oldname-2026-09-05.md", "old\n", "base")
        add_origin_and_push(repo, self.tmp / "origin-rename", "origin-rename.git")
        run_git(repo, "mv", "oldname-2026-09-05.md", "newname-2026-09-05.md")
        run_git(repo, "commit", "-m", "rename", "--quiet")
        head = run_git(repo, "rev-parse", "HEAD")
        run_git(repo, "push", "origin", "main", "--quiet")
        expected = rs.diff_strategy_items(repo, base, head)
        self.assertEqual(len(expected), 1)
        exp = expected[0]
        self.assertTrue(str(exp.get("status", "")).startswith("R"))
        st = self.tmp / "state-rename.json"
        write_json(st, minimal_state(base))
        # wrong old_path must abortdeterministically via entrypoint delegation
        bad = {"base_checkpoint": base, "reviewed_snapshot": head,
               "reviewed_at": "2026-09-05T00:00:00+08:00",
               "items": [{"status": exp["status"], "path": exp["path"], "old_path": "wrong-2026-09-05.md",
                          "blob": "0" * 40, "decision": "REJECT", "reason": "x", "auditor_status": "not-required"}],
               "pending_ingestion": []}
        pp_bad = self.tmp / "payload-rename-bad.json"
        write_json(pp_bad, bad)
        with self.assertRaises(RuntimeError) as ctx:
            ic.apply_review(st, pp_bad, repo)
        self.assertIn("rename", str(ctx.exception).lower())
        # correct old_path succeeds
        good = {"base_checkpoint": base, "reviewed_snapshot": head,
                "reviewed_at": "2026-09-05T00:00:00+08:00",
                "items": [{"status": exp["status"], "path": exp["path"], "old_path": exp.get("old_path"),
                           "blob": "0" * 40, "decision": "REJECT", "reason": "x", "auditor_status": "not-required"}],
                "pending_ingestion": []}
        pp_good = self.tmp / "payload-rename-good.json"
        write_json(pp_good, good)
        r = ic.apply_review(st, pp_good, repo)
        self.assertTrue(r.get("updated"))

    def test_deleted_must_reject(self):
        repo = init_repo(self.tmp, "repo-del")
        base = commit_file(repo, "gone-2026-09-05.md", "gone\n", "base")
        add_origin_and_push(repo, self.tmp / "origin-del", "origin-del.git")
        run_git(repo, "rm", "gone-2026-09-05.md", "--quiet")
        run_git(repo, "commit", "-m", "delete", "--quiet")
        head = run_git(repo, "rev-parse", "HEAD")
        run_git(repo, "push", "origin", "main", "--quiet")
        expected = rs.diff_strategy_items(repo, base, head)
        self.assertEqual(len(expected), 1)
        self.assertTrue(str(expected[0].get("status", "")).startswith("D"))
        st = self.tmp / "state-del.json"
        write_json(st, minimal_state(base))
        # PASS on deleted must abort
        bad = {"base_checkpoint": base, "reviewed_snapshot": head,
               "reviewed_at": "2026-09-05T00:00:00+08:00",
               "items": [{"status": expected[0]["status"], "path": "gone-2026-09-05.md",
                          "blob": "0" * 40, "decision": "PASS", "reason": "x", "auditor_status": "not-required"}],
               "pending_ingestion": [{"reviewed_commit": head, "path": "gone-2026-09-05.md",
                                      "blob": "0" * 40, "decision": "PASS",
                                      "wiki_path": "quant/gone-2026-09-05.md",
                                      "wiki_content": "x\n", "wiki_content_sha256": sha_text("x\n")}]}
        pp_bad = self.tmp / "payload-del-bad.json"
        write_json(pp_bad, bad)
        with self.assertRaises(RuntimeError) as ctx:
            ic.apply_review(st, pp_bad, repo)
        self.assertIn("REJECT", str(ctx.exception))
        # REJECT on deleted succeeds with empty pending
        good = {"base_checkpoint": base, "reviewed_snapshot": head,
                "reviewed_at": "2026-09-05T00:00:00+08:00",
                "items": [{"status": expected[0]["status"], "path": "gone-2026-09-05.md",
                           "decision": "REJECT", "reason": "gone", "auditor_status": "not-required"}],
                "pending_ingestion": []}
        pp_good = self.tmp / "payload-del-good.json"
        write_json(pp_good, good)
        r = ic.apply_review(st, pp_good, repo)
        self.assertTrue(r.get("updated"))

    def test_indivisible_first_commit(self):
        repo = init_repo(self.tmp, "repo-indiv")
        base = commit_file(repo, "base-2026-09-05.md", "b\n", "base")
        add_origin_and_push(repo, self.tmp / "origin-indiv", "origin-indiv.git")
        # single commit with 6 strategy artifacts (> max 5) must stay indivisible
        for i in range(6):
            p = repo / f"s{i}-2026-09-05.md"
            p.write_text(f"{i}\n", encoding="utf-8")
            run_git(repo, "add", f"s{i}-2026-09-05.md")
        run_git(repo, "commit", "-m", "six at once", "--quiet")
        head = run_git(repo, "rev-parse", "HEAD")
        run_git(repo, "push", "origin", "main", "--quiet")
        st = self.tmp / "state-indiv.json"
        write_json(st, minimal_state(base))
        res = ic.bootstrap(st, repo, self.skill, fetch=True)
        self.assertTrue(res.get("ok"), res.get("error"))
        batch = res.get("batch", {})
        self.assertEqual(batch.get("batch_head"), head)
        self.assertEqual(batch.get("batch_artifact_count"), 6)
        self.assertEqual(batch.get("total_unreviewed_artifact_count"), 6)
        self.assertFalse(batch.get("deferred"))


if __name__ == "__main__":
    unittest.main()
