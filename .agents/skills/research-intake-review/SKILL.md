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

## Deterministic control-plane mechanics — CONTROL PLANE V6

Research judgment stays in this skill and with ChatGPT. The repo-local helper owns deterministic mechanics:

```text
.agents/skills/research-intake-review/review_state.py
```

The v6 entrypoint owns bootstrap/verification mechanics without duplicating state logic:

```text
.agents/skills/research-intake-review/intake_control.py
```

Scheduled ChatGPT reads the current skill through v6 bootstrap output, not a CatDesk dedicated read. After CatDesk guidance, launch the entrypoint through CatDesk `run_command`; it reads `SKILL.md` + canonical state using normal local file IO, computes policy SHA-256, runs helper `validate`/`preflight`, and returns structured JSON including policy text/hash, state summary, pending summary, frozen batch manifest, untracked visibility-only list, version contract, and failure class (`ok`/`transient`/`deterministic`). A CatDesk dedicated-read `INVALID_ARGUMENT` never prevents bootstrap because bootstrap never calls that surface; CatDesk `run_command` itself is still required for local invocation.

Version contract (frozen for this release): the v6 entrypoint operates over frozen state schema/control v5. `SUPPORTED_STATE_VERSIONS=(5,)` is enforced in `intake_control.py` (`bootstrap`/`status`/`ingest-pending`/`apply`); any other `state_control_version` is rejected deterministically with `unsupported state_control_version`; no canonical migration is performed here. Bootstrap output carries `version_contract` (`entrypoint v6`, `supported_state_versions [5]`).

The control plane is intentionally small. **There is no long-lived review lease.** State mutation uses a short kernel-managed file mutex plus one compare-and-swap on `last_reviewed_commit`. The mutex exists only while a helper process performs a state read/check/write and is released automatically by the OS if that process exits; it cannot become a stale lease. Two runs may read the same immutable batch, but only the run whose base checkpoint still matches may commit review state. A losing run stops before Wiki Brain ingestion.

Required invariants:
- `run_lease` is retained only as a deprecated compatibility field and must be `null`;
- one artifact path belongs to exactly one decision bucket;
- `last_review_findings` must agree with the current decision bucket for every item it records;
- every current `REMEDIATE` item has exactly one durable `remediation_backlog` entry, and no non-REMEDIATE path remains in that backlog;
- a remediation entry stores `path`, immutable `blob` when available, reason, and first/last-seen metadata;
- a later PASS / PASS-WITH-CAVEAT / REJECT removes that artifact from the remediation backlog;
- checkpoint movement is atomic under the short state mutex and guarded by `base_checkpoint == last_reviewed_commit`;
- `apply` must prove `reviewed_snapshot` descends from the base checkpoint and that the review payload exactly covers the strategy diff for that frozen range;
- every PASS / PASS-WITH-CAVEAT has exactly one matching new `pending_ingestion` entry tied to reviewed commit/path/blob/decision;
- each pending entry stores the exact deterministic Wiki content plus SHA-256; its decision must match the current PASS/PASS-WITH-CAVEAT bucket;
- Wiki Brain is written only from durable `pending_ingestion` created by the successful checkpoint CAS.

A transient CatDesk/shell/browser/auditor failure therefore affects only the current run. It must not leave a lock or lease that blocks later runs.

### Preflight and state mechanics

Scheduled runs use the repo-local deterministic helper for `validate`, `preflight`, `apply`, and `complete-ingestion` exclusively through `intake_control.py`, which imports `review_state` functions/subcommands and never duplicates CAS/coverage logic. Generic shell work should still be minimized; the helper centralizes the short OS mutex, atomic JSON writes, Git ancestry checks, frozen-diff coverage checks, rename-aware diffing, and batch selection. A transient command failure is retried once, then the run stops without state mutation. Failures are explicit as `transient` (fetch/network transport whitelist only, retryable: could-not-resolve/unable-to-access/connection/timeout/temporary/no-route/hung-up/failed-to-fetch, plus fetch timeout) vs `deterministic` (invariant/CAS/coverage/contract/bad-revision/bad-object/not-a-git-repository/does-not-appear-to-be-a-git-repository/no-such/invalid-checkpoint/unsupported-version, not retryable; deterministic wins on overlap; bare git noise without transport proof is deterministic fail-closed).

Preflight uses committed Git history and selects the oldest immutable batch of at most five root-level strategy Markdown artifacts, preserving an indivisible first commit if it alone exceeds five. Root-level untracked strategy Markdown is visibility-only and is never reviewed, staged, deleted, or treated as reviewed. `status` (`bootstrap --no-fetch`) is the offline-safe read-only diagnostic: validate + version gate + state/pending summary + local untracked list, no fetch, no mutation. `ingest-pending --dry-run` previews guarded Wiki writes without mutating Wiki/state. `apply` always fresh-fetches `origin/main` first with timeout=60s; the delegated `preflight` fetch is likewise bounded (`fetch_timeout=60s` default in `review_state.preflight`, `TimeoutExpired` maps to `transient` in bootstrap); the version gate runs before fetch; on fetch/network transport failure it aborts as `transient` and never advances the checkpoint on stale remote (diagnostic `status` remains allowed offline); on bad-revision/object/not-a-repo (including `does not appear to be a git repository`)/invalid-checkpoint it aborts as `deterministic`.

Pending ingestion is executed only by `intake_control.py execute_ingestion`: it writes only the exact durable `wiki_content` to canonical `/Users/hong/.hermes/wiki/quant/`, enforces the two-layer wiki_path boundary (Layer 1 canonical invariant in `review_state.validate_state`: `quant/` prefix, `.md` suffix, no `..`, not absolute — global deterministic abort; Layer 2 executor-local hardening in `is_safe_wiki_path`/`guarded_target`: backslash/NUL, single-dot segment, double-slash, whitespace, empty part, symlink, resolved containment — per-item blocked; no semantic drift, Layer 2 never loosens Layer 1), verifies existing hash or `expected_existing_sha256` before overwrite, atomically writes, post-write rechecks target/parent symlinks and resolved containment (best-effort local fail-closed, not an atomic sandbox), read-back verifies hash, and only then calls `complete-ingestion`; a blocked item remains pending.

## Incremental review procedure

Normal scheduled review is commit-delta based and uses **small immutable batches**.

1. Read CatDesk operating guidance, then launch the v6 entrypoint through CatDesk `run_command` and read the current skill through its bootstrap output (not a dedicated read). Run the deterministic invariant validator via bootstrap. If validation fails (`deterministic`), stop without mutating review state. `INVALID_ARGUMENT` from a dedicated read never blocks bootstrap because bootstrap uses local file IO.
2. Process any existing `pending_ingestion` first via `intake_control.py ingest-pending` (dry-run with `--dry-run` for preview). Each pending item is tied to reviewed commit/path/blob/decision and contains the exact Wiki target, exact `wiki_content`, and `wiki_content_sha256`. Never regenerate the Wiki record during ingestion. If the target is absent, create that exact content; if it already has the same hash, treat it as an idempotent success; if it differs, do not overwrite unless an `expected_existing_sha256` stored with the pending item still matches the current target. Read the result back, verify the pending hash, then use `complete-ingestion` to remove only that exact pending item and record the successful Wiki path.
3. Run deterministic preflight from `last_reviewed_commit` to current `origin/main`. Require the checkpoint to be an ancestor. Select the oldest immutable batch and treat its full SHA as `SNAPSHOT_HEAD` / `batch_head`.
4. Read each strategy artifact from immutable `SNAPSHOT_HEAD` content and review only that frozen material. Never mix a later remote revision into the batch. For a deleted artifact, read the last immutable content from the base side, record status `D`, resolve it as `REJECT`, and never create pending ingestion for it.
5. If the selected committed delta has zero strategy artifacts, verify any contract-affecting documentation/skill change and apply an empty review payload so the checkpoint advances across metadata-only history.
6. Resolve each strategy artifact provisionally to one of the four decisions.
7. Use the independent Hermes `auditor` selectively:
   - mandatory before final `PASS` or `PASS-WITH-CAVEAT` when ChatGPT generated, normalized, materially modified, or previously adjudicated the artifact;
   - recommended for genuine material ambiguity or reviewer conflict;
   - not required merely to reconfirm an already-clear `REMEDIATE` or `REJECT`.
   The auditor finds faults but never owns promotion or final judgment.
8. ChatGPT makes the final decision. `REMEDIATE` and `REJECT` remain outside Wiki Brain. Every `REMEDIATE` retains its durable reason in `remediation_backlog`.
9. Build one review-update payload with the original `base_checkpoint`, `reviewed_snapshot`, each item's exact Git status/path/blob/decision/reason/auditor status, deferred remote information, and **one new pending-ingestion record for every PASS/PASS-WITH-CAVEAT**. Each pending record must carry the exact deterministic Wiki content and SHA-256. Do not write accepted items to Wiki Brain yet.
10. Run `apply` via `intake_control.py apply` (fresh-fetch guarded; fetch failure aborts as `transient` with no offline advancement). Under the short OS mutex it must re-check the checkpoint CAS, prove `reviewed_snapshot` ancestry, and prove the payload exactly covers the frozen strategy diff. CAS or coverage mismatch aborts without Wiki writes. On success, checkpoint, decision buckets, remediation backlog, findings, deferred information, and pending ingestion advance atomically. A newer REMEDIATE/REJECT for the same staging path cancels any older unresolved pending entry for that path.
11. Re-run state validation. Only after successful state apply may this run process the newly durable pending Wiki entries, using the exact content/hash already stored in state. Read back every exact canonical Wiki file and verify its hash before completion.
12. Atomically clear only the successfully completed pending entries and append their canonical paths to `ingested_wiki_records`. If ingestion or cleanup fails, leave the pending entry durable for the next run; do not roll back the reviewed checkpoint.

Do not advance the checkpoint halfway through a partially reviewed batch. A failed pre-CAS batch is retried from the same base checkpoint. A post-CAS Wiki failure is retried from `pending_ingestion`; it does not cause the research review to repeat.

## Version-race rule

GitHub `main` may advance while a review is in progress. Finish only the selected immutable `SNAPSHOT_HEAD` batch and never mix newer artifacts into it.

Before state mutation, refresh the remote tip. If it advanced beyond `SNAPSHOT_HEAD`, preserve the newer full SHA and delta as `deferred_remote_head` / `deferred_delta`. Remote advancement by itself does not invalidate the batch; only a changed canonical `last_reviewed_commit` causes the checkpoint CAS to fail.

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
