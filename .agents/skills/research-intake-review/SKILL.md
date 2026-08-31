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
ChatGPT / Antigravity research
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

Reject a new record when it adds no material knowledge beyond an existing strategy family or canonical record.

Material incremental value may include:
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

## Incremental review procedure

Normal scheduled review is commit-delta based.

1. Read the local review checkpoint.
2. Fetch the latest `origin/main`.
3. Snapshot the exact HEAD being reviewed.
4. If HEAD equals `last_reviewed_commit`, there is no new intake work.
5. Otherwise review only the strategy artifacts added or modified in `last_reviewed_commit..HEAD`.
6. Resolve each changed artifact to one of the four decisions.
7. For material ambiguity or reviewer conflict, request an independent auditor challenge; the auditor finds faults but does not own the final decision.
8. Only `PASS` and `PASS-WITH-CAVEAT` are eligible for Wiki Brain ingestion.
9. `REMEDIATE` and `REJECT` remain outside Wiki Brain.
10. After the entire snapshot has been reviewed, update the checkpoint to the reviewed HEAD. A later remediation commit becomes a new delta and is reviewed normally.

Do not advance the checkpoint halfway through a partially reviewed batch.

## Version-race rule

If `origin/main` changes while a review is in progress, finish the review against the snapshotted commit. Do not silently mix artifacts from two HEADs.

After the snapshot is complete, the next run handles the newer delta.

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
