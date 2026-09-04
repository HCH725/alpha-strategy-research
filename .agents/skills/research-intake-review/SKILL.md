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

Research judgment stays in this skill and with ChatGPT. The repo-local helper remains the reference implementation and manual integrity checker:

```text
.agents/skills/research-intake-review/review_state.py
```

Scheduled runs are **shell-free**: they must not invoke CatDesk `run_command` or `start_command` for validation, Git preflight, state application, or lease mechanics. The scheduled control plane uses CatDesk dedicated `search`/`edit`/browser operations and GitHub immutable commit history. The helper remains available for interactive/manual diagnostics and must stay semantically aligned with these invariants.

Required invariants:
- `run_lease` is either `null` or a valid lease object with `run_id`, owner, offset-aware `started_at`, and positive `stale_after_minutes`;
- one artifact path belongs to exactly one decision bucket;
- `last_review_findings` must agree with the current decision bucket for every item it records;
- every current `REMEDIATE` item must have exactly one durable `remediation_backlog` entry, and no non-REMEDIATE path may remain in that backlog;
- a remediation entry stores `path`, immutable `blob` when available, reason, and first/last-seen metadata;
- a later PASS / PASS-WITH-CAVEAT / REJECT removes that artifact from the remediation backlog;
- checkpoint updates use compare-and-swap semantics against both the base checkpoint and active `run_id` read at run start.

Before and after every state-changing scheduled run, ChatGPT must perform the equivalent invariant check directly from the canonical state using CatDesk dedicated reads/searches. Any invariant failure is a control-plane block. For manual maintenance, `review_state.py validate` remains the executable cross-check, but the recurring automation must not call it through a shell.

### Run lease

The recurring automation must not create/delete a shell-level lock file. The single-run lease lives directly in the canonical state as `run_lease` and is acquired/released with CatDesk's dedicated atomic guarded edit operation.

Canonical idle form:

```json
"run_lease": null
```

Active form:

```json
"run_lease": {
  "run_id": "<unique-run-id>",
  "owner": "ChatGPT (GPT-5.6 Sol)",
  "started_at": "<offset-aware ISO-8601 timestamp>",
  "stale_after_minutes": 180
}
```

Lease protocol:
- Read and validate the canonical state through CatDesk dedicated search/read surfaces; do not invoke a shell validator in a scheduled run.
- Generate a unique `run_id` without a shell command.
- Acquire by one CatDesk guarded edit that replaces the exact idle text `"run_lease": null` with the active lease object. This guarded edit is the compare-and-swap: if another run won first, the edit fails and this run must stop without overlap.
- If a lease already exists, do not overwrite it unless its `started_at` is more than 180 minutes old. A stale reclaim must atomically replace the exact old lease object with the new lease object in one guarded edit; never clear then set in two steps.
- Every state application must verify both `run_id == run_lease.run_id` and `base_checkpoint == last_reviewed_commit` before any checkpoint movement. This prevents a stale/reclaimed run from advancing state.
- Release only by a CatDesk guarded edit that replaces the exact current lease object for this `run_id` with `null`.
- CatDesk connector/safety failures should be refreshed/retried once as usual. A failed guarded edit caused by CAS mismatch is not an infrastructure error; it means another run owns the lease.

This design preserves overlap protection while keeping the recurring workflow off generic shell execution.

### Preflight visibility

Scheduled preflight uses GitHub's immutable compare/commit history through the CatDesk browser, not local `git` shell commands. It must identify the committed strategy artifacts waiting for review and the remote commit sequence from the checkpoint to the current `main` tip.

Root-level untracked local strategy Markdown is a best-effort visibility warning in shell-free scheduled mode because GitHub cannot see uncommitted local files. Known local-only artifacts should still be surfaced when visible through CatDesk dedicated file search. Untracked files are never reviewed, staged, deleted, or treated as reviewed by Intake Review. Lack of a complete untracked listing must not silently turn local-only content into reviewed content.

## Incremental review procedure

Normal scheduled review is commit-delta based and uses **small immutable batches**.

1. Read CatDesk operating guidance, the current repo-local skill, and canonical state through dedicated CatDesk file surfaces. Perform the invariant checklist above directly from state; do not call `run_command` or `start_command` for scheduled control-plane work.
2. Acquire `run_lease` directly in the state using the CatDesk guarded-edit CAS protocol above. Keep the generated `run_id`. If another non-stale review owns the lease, stop this run without changing state.
3. Process any existing `pending_ingestion` first. Pending items remain tied to their reviewed commit/path/blob.
4. Use the CatDesk browser to open GitHub's immutable compare view from `last_reviewed_commit` to the current full SHA of `main`. Require the checkpoint to be on the ancestor path; divergence or non-comparable history is `history_reconciliation_required`. Select the small batch from the compare commit sequence in oldest-to-newest order, accumulating root-level strategy Markdown changes up to five artifacts. If adding the next commit would exceed five, stop at the previous commit; if the first indivisible commit itself exceeds five, review that commit as one batch. The selected full SHA is `SNAPSHOT_HEAD` / `batch_head`.
5. Read each changed strategy artifact from the immutable GitHub `SNAPSHOT_HEAD` (`blob/<SNAPSHOT_HEAD>/<path>` or equivalent raw/contents view) and record its immutable object identity when exposed. Review only that frozen content.
6. Treat `batch_head`, never local `HEAD` or a moving remote tip, as `SNAPSHOT_HEAD`. Root-level untracked local Markdown remains a best-effort visibility warning only in shell-free scheduled mode and is never reviewed or mutated.
7. Review only strategy artifacts materially added, modified, renamed, or removed in `last_reviewed_commit..SNAPSHOT_HEAD`. Documentation/skill-only changes do not require strategy review unless they change this contract. If the selected committed delta contains **zero** strategy artifacts, verify any contract-affecting documentation/skill change, then apply an empty review payload so the checkpoint can advance across that non-strategy delta; otherwise the same metadata-only delta would repeat forever.
8. Resolve each changed strategy artifact provisionally to one of the four decisions.
9. Use the independent Hermes `auditor` selectively:
   - mandatory before final `PASS` or `PASS-WITH-CAVEAT` when ChatGPT generated, normalized, materially modified, or previously adjudicated the artifact;
   - recommended for genuine material ambiguity or reviewer conflict;
   - not required merely to reconfirm an already-clear `REMEDIATE` or `REJECT`.
   The auditor finds faults but never owns promotion or final judgment.
10. ChatGPT makes the final decision. Only `PASS` and `PASS-WITH-CAVEAT` are eligible for Wiki Brain ingestion, and caveats must travel with the Wiki record.
11. `REMEDIATE` and `REJECT` remain outside Wiki Brain. Every `REMEDIATE` must retain its durable reason in `remediation_backlog`; a later remediation commit simply becomes a new Git delta and is reviewed normally.
12. Build one review-update payload containing `run_id`, reviewed snapshot, base checkpoint, item paths/blobs/decisions/reasons, auditor status where applicable, ingestion results, pending ingestion, and deferred remote information.
13. Apply the complete review result to canonical state with one CatDesk guarded edit/CAS. Before mutation, verify the exact active `run_id` still owns `run_lease` and `last_reviewed_commit` still equals the base checkpoint. Update checkpoint, decision buckets, remediation backlog, last findings, pending ingestion, ingested Wiki records, and deferred information consistently while preserving the active lease. Any CAS mismatch aborts rather than overwrites newer state.
14. Read/search the state back through CatDesk and repeat the invariant checklist directly. Read back every Wiki Brain record created or enriched by this run before considering ingestion complete.
15. Release the state lease through one CatDesk guarded edit that replaces this run's exact lease object with `"run_lease": null`. Never use a shell lock cleanup command.

Do not advance the checkpoint halfway through a partially reviewed batch. A failed batch is retried from the same base checkpoint. The recurring workflow must remain shell-free except for an explicitly required independent auditor invocation when no dedicated auditor surface exists.

## Version-race rule

GitHub `main` may advance while a review is in progress. Finish only the selected immutable `SNAPSHOT_HEAD` batch and never mix newer artifacts into it.

Before state mutation, refresh the GitHub `main` tip. If it advanced beyond `SNAPSHOT_HEAD`, preserve the newer full SHA and strategy delta as `deferred_remote_head` / `deferred_delta`; the next run continues from the newly advanced checkpoint toward the then-current remote tip.

The state lease protects local state from overlapping scheduled/manual runs; the immutable GitHub batch protects reviewed content from remote movement. Both protections remain required.

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
