"""Guard the root-level Alpha Strategy PASS-only main invariant.

Run on the proposed merged tree; never count PR/other-branch research as admitted.
This checks metadata integrity, not independent proof of backtest expressibility.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
README_NAMES = {"README.md", "README.zh-TW.md"}
STATUS_RE = re.compile(r"^hb_ready_status:\s*(\S+)\s*$", re.MULTILINE)
COUNT_RE = re.compile(r"Admitted strategies on main:\s*(\d+)")

def get_status(body):
    if not body.startswith("---\n"):
        return None
    sections = body.split("---", 2)
    if len(sections) < 3:
        return None
    match = STATUS_RE.search(sections[1])
    return match.group(1).strip("'\"") if match else None


class MainPassOnlyTest(unittest.TestCase):
    def test_every_root_strategy_is_pass(self):
        paths = sorted(p for p in ROOT.glob("*.md") if p.name not in README_NAMES)
        self.assertGreater(len(paths), 0)
        invalid = [(p.name, get_status(p.read_text(encoding="utf-8")))
                   for p in paths if get_status(p.read_text(encoding="utf-8")) != "PASS"]
        self.assertEqual(invalid, [], f"Non-PASS strategy in main-bound tree: {invalid}")

    def test_pool_counter_matches_root_strategy_count(self):
        paths = [p for p in ROOT.glob("*.md") if p.name not in README_NAMES]
        body = (ROOT / "README.md").read_text(encoding="utf-8")
        match = COUNT_RE.search(body)
        self.assertIsNotNone(match, "README HB_READY_POOL_COUNT missing")
        self.assertEqual(int(match.group(1)), len(paths))

    def test_non_pass_never_becomes_pass_through_parser(self):
        for status in ("NOT_LOSSLESS", "NOT_ASSESSED", "UNKNOWN"):
            self.assertNotEqual(get_status(f"---\nhb_ready_status: {status}\n---\n"), "PASS")
        self.assertIsNone(get_status("# no frontmatter"))
        self.assertEqual(get_status("---\nhb_ready_status: PASS\n---\n"), "PASS")


if __name__ == "__main__":
    unittest.main()
