---
name: research-intake-review
description: Review external alpha strategy research before Hermes Wiki Brain ingestion without turning intake review into strategy validation.
---

# Research Intake Review

## Purpose

This skill defines the review gate between `alpha-strategy-research` and Hermes Wiki Brain.

Its job is narrow: determine whether an external strategy artifact has been understood, normalized, classified, and bounded correctly enough to enter Wiki Brain as **research-only knowledge**.

It does **not** determine whether a strategy is profitable, robust, production-ready, paper-ready, testnet-ready, or live-ready.

## Ownership boundary

- Scheduled Research Intake Review is owned by **ChatGPT**.
- Hermes `default` should understand this skill as backup professional knowledge and may use it only when explicitly asked to assist or take over.
- Learning this skill does **not** assign Hermes the recurring review job.
- The `auditor` profile may independently challenge a review when requested, but it is not the final decision-maker.
- Final intake judgment and Wiki Brain promotion remain with ChatGPT unless the user explicitly changes ownership.

## Position in the research pipeline

```text
ChatGPT / Hermes / Antigravity research
        ↓
alpha-strategy-research
        ↓
Research Intake Review
        ↓
Hermes Wiki Brain (research-only knowledge)
        ↓
Hermes hypothesis / synthesis
        ↓
PyBroker research screening
        ↓
Nautilus authoritative historical validation
```

Never collapse these stages.

## What Intake Review must answer

Review only the minimum questions needed to protect Wiki Brain quality.

### 1. Provenance

Confirm the strategy can be traced back to the actual source.

For GitHub sources, prefer:
- repository URL;
- full commit SHA;
- exact source file path;
- immutable source URL.

Do not accept model-generated summaries, marketing pages, screenshots, branch-only links, or unverifiable descriptions as equivalent to a fixed primary source.

### 2. Strategy identity

Confirm the normalized record describes the strategy the source actually implements.

Do not reduce a hybrid strategy to one indicator merely because that indicator appears prominently.

Preserve materially required components, especially:
- core trigger;
- confirmation/filter conditions;
- regime/state logic;
- derived-data construction;
- exit/risk state when it materially changes strategy behavior.

Example: `RSI + MACD + dual Supertrend + ATR exits` must not silently become `Standard MACD Trend`.

### 3. Signal semantics

Check that entry, exit, direction, timing, filters, state transitions, and important parameters match the source.

Small wording differences are acceptable only when they do not change implementation semantics.

Material mismatches require remediation.

Examples of material mismatches:
- `MACD > signal` rewritten as a crossover;
- current-bar logic rewritten as previous-bar logic;
- optional logic rewritten as mandatory;
- bar-count cooldown rewritten as minutes;
- unused variables described as active execution rules.

### 4. Required data

Derive data requirements from the actual signal path, not from title keywords or surrounding prose.

Examples:
- ordinary OHLCV logic is not `Futures Basis` just because the source mentions futures;
- Heikin-Ashi is not mandatory when it is an optional disabled input;
- session VWAP requires timestamp/session/reset semantics in addition to OHLCV;
- Renko requires brick construction semantics, not merely the label `Renko charts`;
- higher-timeframe filters require explicit alignment rules.

### 5. Claim boundary

Separate:
- source-reported claims;
- reviewer interpretation;
- independently reproduced evidence.

Marketing language such as "stable", "adaptive", "filters noise", "reduces false signals", or "works across markets" remains source-reported unless independently demonstrated.

Do not convert source claims into our own economic mechanism or validation conclusion.

### 6. Incremental knowledge / deduplication

Wiki Brain is not a catalog of every parameter variation.

Canonicalize source identity first (DOI / arXiv ID / canonical URL / GitHub repo + immutable commit + path / TradingView stable public strategy/idea/script URL — TradingView limited to public, traceable strategy/idea/script/research URLs; preserve the stable URL and as-of date; private/paid/invite-only sources are not valid).

Then apply deduplication:

- Same canonical source identity + materially same normalized rule/hypothesis => REJECT duplicate (no new Wiki record). Do not create a second record for the same source-hypothesis pair.
- Different source but same core hypothesis => never create a second canonical Wiki strategy record. If the credible new source adds material evidence, use PASS or PASS-WITH-CAVEAT for evidence enrichment and ingest by updating the existing canonical Wiki record with the new provenance/evidence (and caveat or negative evidence when applicable). If it adds no material incremental evidence, use REJECT with a duplicate/no-increment reason. Still use only PASS / PASS-WITH-CAVEAT / REMEDIATE / REJECT; do not add a fifth state.
- Same canonical source identity but materially distinct hypothesis/signal/horizon/mechanism => may be independent; independent only when the core hypothesis differs materially in at least one of mechanism, signal construction, universe/market type, horizon/regime, or material data dependency.

Scout dedup mirrors this: same canonical source identity + materially same normalized rule => do not create a new artifact; same source but materially distinct hypothesis/signal/horizon/mechanism may be independent under the same material-difference test.

Material incremental value (beyond simple dedup) may include:
- a genuinely different mechanism;
- a materially different signal construction;
- a new data dependency;
- a crypto-specific adaptation;
- important negative evidence;
- a new regime dependency;
- meaningful execution/cost evidence.

A different title, timeframe, parameter, or indicator permutation alone is not enough.

## What Intake Review must NOT do

Do not turn this gate into another backtesting system.

Intake Review does not require:
- Sharpe evaluation;
- full OOS testing;
- parameter optimization;
- portfolio construction;
- complete transaction-cost modeling;
- live-execution realism;
- profitability judgment;
- Paper/Testnet/Live approval.

Those belong downstream to Hermes hypothesis formation, PyBroker research, Nautilus validation, and later trading authorization.

## Decisions

Use only four outcomes.

### PASS

The artifact is source-faithful, correctly bounded, sufficiently specified for research knowledge, and adds meaningful knowledge.

It may enter Wiki Brain as `research-only`.

### PASS-WITH-CAVEAT

The core knowledge is correct and useful, but one or more explicit limitations remain.

The caveat must travel with the Wiki record.

Typical examples:
- precise execution timing remains underspecified;
- a derived-data construction needs downstream implementation decisions;
- the source provides a valid signal but no independent evidence.

### REMEDIATE

The underlying source is useful, but the normalized artifact materially misstates identity, signal semantics, data requirements, or claim boundaries.

Do not ingest until corrected and re-reviewed.

### REJECT

Do not create a new Wiki record when the artifact is untraceable, materially false, non-alpha utility/risk logic mislabeled as alpha, or adds no incremental knowledge.

Duplicate/no-increment cases are handled as `REJECT` with the reason stated; no fifth decision state is required.

## Deterministic control-plane mechanics

Research judgment stays in this skill and with ChatGPT. Mechanical state transitions must use the repo-local helper:

```text
.agents/skills/research-intake-review/review_state.py
```

The helper exists only to make the control plane deterministic. It does not decide whether a strategy should pass.

Required invariants:
- one artifact path belongs to exactly one decision bucket;
- `last_review_findings` must agree with the current decision bucket for every item it records;
- every current `REMEDIATE` item must have a durable `remediation_backlog` entry;
- a remediation entry stores `path`, immutable `blob` when available, reason, and first/last-seen metadata;
- a later PASS / PASS-WITH-CAVEAT / REJECT removes that artifact from the remediation backlog;
- checkpoint updates use compare-and-swap semantics against the base checkpoint read at run start;
- checkpoint JSON is written atomically (`tmp + fsync + replace`), never by partial in-place mutation.

Before and after every state-changing review run, execute the helper's `validate` command. Any invariant failure is a control-plane block and must be repaired before new review decisions are committed.

### Lock lease

Use the helper's atomic single-run lock. The lock records `run_id`, owner, and start time.

- If a non-stale lock exists, do not overlap the review.
- A lock older than 180 minutes may be reclaimed as stale by the helper.
- Release only a lock whose `run_id` matches the current run.
- A transient CatDesk failure while invoking the helper should be retried once with identical parameters. Do not silently bypass overlap protection.

### Preflight visibility

Preflight must report both:
- committed strategy artifacts waiting for review; and
- root-level untracked strategy Markdown files.

Untracked files are visibility warnings only. They are not reviewed until committed, and they must never be staged, deleted, or treated as reviewed by Intake Review.

## Incremental review procedure

Normal scheduled review is commit-delta based and uses **small immutable batches**.

1. Read CatDesk operating guidance, then run `review_state.py validate`.
2. Acquire the single-run lock through `review_state.py acquire-lock`. If another non-stale review owns it, stop this run without changing state.
3. Read the checkpoint and process any existing `pending_ingestion` first. Pending items remain tied to their reviewed commit/path/blob.
4. Run `review_state.py preflight --max-artifacts 5`. The helper fetches `origin/main`, verifies the checkpoint is an ancestor, reports untracked strategy files, and chooses a deterministic `batch_head` containing at most five changed strategy artifacts where possible. If the first single commit itself contains more than five strategy artifacts, review that commit as one indivisible batch.
5. Treat `batch_head`, not local `HEAD`, as `SNAPSHOT_HEAD`. Never use an out-of-date local branch tip as the review snapshot.
6. Review only strategy artifacts materially added, modified, renamed, or removed in `last_reviewed_commit..SNAPSHOT_HEAD`. Documentation/skill-only changes do not require strategy review unless they change this contract. If the selected committed delta contains **zero** strategy artifacts, verify any contract-affecting documentation/skill change, then apply an empty review payload so the checkpoint can advance across that non-strategy delta; otherwise the same metadata-only delta would repeat forever.
7. Resolve each changed strategy artifact provisionally to one of the four decisions.
8. Use the independent Hermes `auditor` selectively:
   - mandatory before final `PASS` or `PASS-WITH-CAVEAT` when ChatGPT generated, normalized, materially modified, or previously adjudicated the artifact;
   - recommended for genuine material ambiguity or reviewer conflict;
   - not required merely to reconfirm an already-clear `REMEDIATE` or `REJECT`.
   The auditor finds faults but never owns promotion or final judgment.
9. ChatGPT makes the final decision. Only `PASS` and `PASS-WITH-CAVEAT` are eligible for Wiki Brain ingestion, and caveats must travel with the Wiki record.
10. `REMEDIATE` and `REJECT` remain outside Wiki Brain. Every `REMEDIATE` must retain its durable reason in `remediation_backlog`; a later remediation commit simply becomes a new Git delta and is reviewed normally.
11. Build one review-update payload containing the reviewed snapshot, base checkpoint, item paths/blobs/decisions/reasons, auditor status where applicable, ingestion results, pending ingestion, and deferred remote information.
12. Apply that payload only through `review_state.py apply`. The helper performs compare-and-swap checkpoint protection, moves artifacts between decision buckets deterministically, updates the remediation ledger, validates invariants, and atomically writes the state file.
13. Run `review_state.py validate` again and read back any Wiki Brain records created by this run.
14. Release the lock through `review_state.py release-lock --run-id <run_id>`.

Do not advance the checkpoint halfway through a partially reviewed batch. A failed batch is retried from the same base checkpoint.

## Version-race rule

`origin/main` may advance while a review is in progress. Finish only the selected `SNAPSHOT_HEAD` batch and never mix newer artifacts into it.

If the helper selected a small batch before the current remote tip, preserve the newer remote tip as deferred work. The next run continues from the newly advanced checkpoint toward the then-current `origin/main`.

The lock lease protects local state from overlapping scheduled/manual runs; the immutable Git batch protects reviewed content from remote movement. Both protections remain required.

## Wiki Brain ingestion boundary

A record accepted by this gate must still retain the existing research boundaries:

```yaml
status: research-only
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
```

Presence in Wiki Brain means only that the research knowledge is worth preserving and reusing.

It does not mean:
- independently reproduced;
- profitable;
- PyBroker-validated;
- Nautilus-validated;
- approved for Paper, Testnet, or Live trading.

## Handover rule for Hermes

If the user explicitly asks Hermes to take over Research Intake Review in the future, Hermes should:

1. read this skill first;
2. inspect the current checkpoint and latest repo HEAD;
3. review only the unreviewed commit delta;
4. preserve the four-decision model and downstream boundaries;
5. use an independent auditor when appropriate;
6. never infer that prior familiarity with the skill grants permanent ownership of the scheduled review.
