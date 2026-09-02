# alpha-strategy-research

**English** | [繁體中文](README.zh-TW.md)

Public staging repository for external alpha-strategy research normalized for direct Hermes Wiki Brain ingestion.

## Purpose

This repository is the handoff layer between **three independent Research Scouts (ChatGPT / Hermes / Antigravity)** and **ChatGPT Research Intake Review / Wiki Brain ingestion**.

Operating flow:

```text
External public sources
(GitHub / FMZ / TradingView / papers / blogs / public research)
        ↓
ChatGPT / Hermes / Antigravity (independent, parallel scouts)
find alpha ideas → understand → normalize → push here
        ↓
ChatGPT
Research Intake Review
(PASS / PASS-WITH-CAVEAT / REMEDIATE / REJECT)
        ↓
ChatGPT writes accepted knowledge directly into Hermes Wiki Brain
        ↓
Hermes uses the knowledge for research, synthesis and later validation
```

Valid public source contract for all three Scouts: GitHub / FMZ / TradingView / papers / blogs / public research. For TradingView, only public, traceable strategy/idea/script/research URLs are valid — preserve the stable URL and as-of date; private or paid/invite-only scripts are not valid sources.

**No Scout writes to Hermes Wiki Brain.** Each Scout's only output channel is this repository. The artifact pushed here should already be in Wiki Brain-native form so ChatGPT can review and ingest it without another translation pass.

## Where this repository fits

This repository is the **upstream research and knowledge-handoff layer** of a broader quantitative workflow. It does not perform formal strategy validation or trading execution itself.

After ChatGPT Research Intake Review and Wiki Brain ingestion, Hermes can use accepted knowledge to synthesize testable hypotheses. Those hypotheses may then move into [`nautilus-quant-system`](https://github.com/HCH725/nautilus-quant-system), where PyBroker is used for isolated strategy research and NautilusTrader provides the formal historical verdict and canonical accounting layer.

```text
External public sources
(GitHub / FMZ / TradingView / papers / blogs / public research)
        ↓
ChatGPT / Hermes / Antigravity research scouts (independent, parallel)
        ↓
alpha-strategy-research
        ↓
ChatGPT Research Intake Review
        ↓
Hermes Wiki Brain
        ↓
Hermes hypothesis / synthesis  ── Loop A (low-frequency, theory/evidence-driven; one thesis/family per iteration → bounded meaningful branches → experiment spec)
        ↓
nautilus-quant-system
PyBroker Experiment & Attrition Loop (Loop B: deterministic campaign expansion → N provisional candidates → batch screens → dedupe/invalid/reject/pass accounting; high-throughput, no LLM per candidate; rejected do not enter Nautilus) → Gate (signal parity, fail-closed) → NautilusTrader high-fidelity historical verdict (survivors only)
        ↓
feedback / lineage / reuse  ── outer evidence-based feedback (survivor summary / failure taxonomy / information gain → stop / refine / new batch; not a fixed backtest count)
        ↓
later gated Paper → Binance Demo/Testnet → Live progression
```

*A strategy record being present here therefore means only that it is normalized research material. It does **not** mean that the idea has passed PyBroker/Nautilus validation, paper trading, testnet, or live-trading approval. In the canonical pipeline this repository feeds **Loop A** (Hermes Research Loop).*

---

## Research Scouts: read this README before every research run

Your job is to search public external sources for potentially useful **alpha strategies or alpha hypotheses**, then convert each worthwhile item into the exact research-record format below and push it to this repository.

You are one of three independent, parallel Research Scouts (ChatGPT / Hermes / Antigravity). Each Scout operates autonomously and targets the same repository. Do not duplicate or overwrite another Scout's existing artifact; inspect recent commits before producing new records.

Valid public sources: GitHub / FMZ / TradingView / papers / blogs / public research. For TradingView, only public, traceable strategy/idea/script/research URLs are valid — preserve the stable URL and as-of date; private or paid/invite-only scripts are not valid sources.

Scout dedup contract: same canonical source identity + materially same normalized rule => do not create a new artifact. Same source but materially distinct hypothesis/signal/horizon/mechanism may be independent (independent only when the core hypothesis differs materially in at least one of mechanism, signal construction, universe/market type, horizon/regime, or material data dependency).

Strategies may be:

- single-signal strategies;
- multi-signal strategies;
- composite / hybrid strategies;
- regime + signal + confirmation combinations;
- cross-sectional, time-series, relative-value, spread, basis, funding, volatility, order-flow, market-microstructure or other defensible alpha ideas.

A hybrid strategy is valid. Do **not** force a multi-component strategy into separate records if its economic thesis depends on the components working together. Instead, preserve the component roles clearly inside `Economic mechanism` and `Signal`.

Examples of valid hybrid structure:

```text
regime filter
+ entry signal
+ confirmation filter
+ exit / risk logic
```

Avoid treating arbitrary indicator stacking as stronger evidence. A complicated rule set with no coherent economic or behavioral mechanism should be described as such.

---

## Canonical Wiki Brain schema

The authoritative strategy-research contract is versioned in Hermes Wiki Brain. At the time of this README update, the current canonical specification is:

```text
quant/strategy-research-record-spec-v1.md
schema: strategy-research-record-v1
```

The `v1` label above describes the **current** canonical version; it is not a permanent hardcoded contract. Before every scheduled local Scout run, resolve and read the current versioned `quant/strategy-research-record-spec-v*.md` specification in Wiki Brain and use the `schema` and required structure declared by that specification. If a newer canonical specification exists, it overrides the schema examples in this README. If the canonical specification cannot be resolved, fail closed rather than guessing.

Do not invent another candidate schema and do not silently migrate older records. Existing records remain valid under the schema version they were created with unless an explicit versioned migration rule says otherwise.

### Required frontmatter

The example below reflects the current v1 specification. New records must use the exact frontmatter required by the canonical specification resolved at run time:

```yaml
---
schema: strategy-research-record-v1
title: <strategy title>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: low | medium | high
source_as_of: <source/data as-of date>
sources:
  - <traceable source URL or repository reference>
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---
```

For newly discovered external strategies, the following defaults are mandatory unless independently verified evidence already exists in our own research system:

```yaml
status: research-only
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
```

`confidence` describes confidence in the **research interpretation**, not confidence that the strategy is profitable and not authorization to trade it.

---

## Required document structure

Use this structure for every strategy record. If information is unavailable, keep the section and state the gap explicitly rather than deleting it.

```markdown
# <Title>

## Provenance

## Economic mechanism
### Source-reported
### Research interpretation

## Signal

## Required data

## Execution assumptions

## Evidence
### Source-reported
### Independently reproduced
### Negative evidence

## Falsification plan

## Crypto portability

## Limitations

## Implementation status

## Adoption boundary

## Related Wiki records

## Sources
```

### 1. Provenance

Record enough information to reproduce where the idea came from.

For GitHub sources, preserve:

- repository URL;
- **full commit SHA**;
- exact file path;
- relevant source URL.

Do not use only `main`, `master`, `latest`, a tag, or a shortened SHA when a fixed commit is available.

For TradingView sources, only public, traceable strategy/idea/script/research URLs are valid — preserve the stable URL and as-of date; private or paid/invite-only scripts are not valid sources. For papers, blogs, FMZ or other public sources, preserve the most stable URL and the source/data as-of date.

### 2. Economic mechanism

Separate what the original source claims from our normalized interpretation.

`Source-reported` should describe the author's stated rationale without upgrading it into a fact.

`Research interpretation` should state the hypothesized mechanism in falsifiable terms, for example:

- trend persistence;
- liquidity provision / mean reversion;
- volatility expansion after compression;
- crowded positioning / funding pressure;
- cross-sectional momentum;
- basis convergence;
- order-flow imbalance;
- behavioral or structural market effects.

For a hybrid strategy, explicitly identify the role of each component, e.g.:

```text
Regime: 200 EMA trend filter
Primary signal: Donchian breakout
Confirmation: volume expansion
Risk / exit: ATR stop
```

Do not assume every component contributes alpha; later research may require ablation tests.

### 3. Signal

Normalize the trading logic so a researcher can understand and, where possible, reconstruct it independently.

Include as applicable:

- signal formation timestamp;
- lookback window;
- long entry;
- short entry;
- exit;
- holding period;
- re-entry rules;
- parameters;
- position-sizing logic;
- multi-timeframe dependencies;
- whether the rule is fully specified or underspecified.

Do not paste large amounts of source code when a normalized rule is sufficient. Keep the source link / commit / path for auditability.

### 4. Required data

State the actual data needed, including as applicable:

- instrument / universe;
- venue;
- market type (spot / perpetual / futures / options);
- timeframe;
- OHLCV fields;
- funding;
- mark / index / basis data;
- trades / aggressor side;
- order book / depth;
- open interest;
- options surface / Greeks;
- timestamp and timezone requirements;
- point-in-time / availability requirements;
- missing-data assumptions.

### 5. Execution assumptions

Record material assumptions such as:

- signal-to-order timing;
- next-bar vs same-bar execution;
- market / limit order;
- fill model;
- fees;
- spread;
- slippage;
- impact / capacity;
- funding;
- leverage / margin;
- borrow / shorting;
- latency;
- partial fills / failures.

If the source omits them, say so.

### 6. Evidence

Keep three evidence classes separate.

#### Source-reported

Third-party backtest, Sharpe, win rate, CAGR, drawdown or profitability claims belong here.

Never rewrite a source-reported claim as our verified result.

Every source-reported performance figure, parameter, threshold, win rate, Sharpe, t-statistic, CAGR, drawdown, or other quantitative claim must trace to a specific source listed in `## Sources` (for example a stable URL/DOI, commit SHA, or page/table reference). If the exact figure cannot be traced, omit it or state the provenance gap explicitly; never invent precision. Figures from equities, commodities, traditional futures, or other non-crypto samples must identify that asset class and must not be presented as crypto evidence.

For each source-reported empirical claim, verify that the cited author(s), paper title, sample/universe, methodology, and reported result all belong to the same source. Never merge a sample, method, statistic, or finding from a different paper merely because the papers study a similar topic. If multiple papers are used, attribute each claim to its own source explicitly.

Example:

```text
Source reports Sharpe 2.1 over the stated sample. This result has not been independently reproduced.
```

#### Independently reproduced

For newly discovered Scout research, normally write:

```text
Not independently reproduced.
```

Only record our own evidence when it actually exists and is traceable.

#### Negative evidence

Record known failures, contrary findings, unstable regimes, transaction-cost sensitivity, data problems or other evidence against the thesis.

If none was found, write something equivalent to:

```text
None identified in the reviewed sources; absence is not evidence of no negative result.
```

### 7. Falsification plan

State what would disprove or materially weaken the hypothesis.

Prefer specific items such as:

- required sample;
- relevant regimes;
- baseline / control;
- ablation tests for hybrid strategies;
- cost sensitivity;
- out-of-sample requirement;
- failure metric or threshold;
- what action follows failure.

### 8. Crypto portability

Use one of these interpretations where useful:

```text
direct
adapted
unproven
not applicable
```

A strategy whose mechanism originates from traditional-asset research must not be labeled `direct` unless the cited source itself demonstrates that mechanism in crypto markets. Otherwise use `adapted` or `unproven`, and state under Research interpretation that this is a ported hypothesis rather than crypto empirical evidence.

Explain any crypto-specific portability risks, especially:

- spot vs perpetual differences;
- funding;
- 24/7 session structure;
- venue fragmentation;
- liquidity;
- mark / index price;
- contract specification;
- timestamp / candle boundaries.

### 9. Limitations

Preserve ambiguity rather than inventing certainty.

Useful explicit markers include:

```text
underspecified
not independently reproduced
data gap
unproven
```

### 10. Implementation status

For newly researched external material, normally state that no implementation in our research stack has been completed.

Do not imply PyBroker, Nautilus, paper, testnet or live verification unless it actually occurred.

### 11. Adoption boundary

Every newly collected external strategy is research material only.

A record being present in this repository does **not** mean:

- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

### 12. Related Wiki records

Link known related concepts or strategy families when identifiable. Use Wiki-style links where a stable Hermes Wiki Brain page is known, for example:

```markdown
[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]
```

Do not fabricate Wiki links.

### 13. Sources

List the exact public sources used for the record.

---

## File naming

Use lowercase, hyphen-separated filenames without spaces.

Preferred pattern for a concrete research capture:

```text
<strategy-or-topic-slug>-<YYYY-MM-DD>.md
```

Examples:

```text
bitcoin-negative-funding-contrarian-reversal-2026-08-31.md
volatility-compression-volume-breakout-2026-08-31.md
cross-sectional-crypto-momentum-2026-08-31.md
```

Do not use ambiguous suffixes such as:

```text
latest
final
new
v2-final-final
```

unless the document itself is a versioned specification.

---

## Research rules for all Scouts

1. **Search for alpha, not marketing claims.** A high reported return is not itself an alpha thesis.
2. **Single and hybrid strategies are both allowed.** Preserve meaningful component structure.
3. **Normalize before pushing.** The file pushed here must already comply with the current canonical Wiki Brain strategy-research schema resolved at run time.
4. **Keep provenance.** External claims must remain traceable to their source.
5. **Do not claim independent validation that has not happened.**
6. **Do not silently repair missing information.** Mark gaps explicitly.
7. **Do not copy large source-code blocks unnecessarily.** Prefer normalized logic plus source references.
8. **Do not confuse risk management with alpha.** Stops, sizing, leverage, DCA, grid or martingale rules should be identified separately from the predictive signal.
9. **Do not confuse complexity with quality.** Multi-indicator combinations need a coherent thesis and remain unvalidated until tested.
10. **Do not write to Hermes Wiki Brain.** Push the normalized research artifact here. ChatGPT performs Research Intake Review and, if accepted, writes it into Wiki Brain directly.

---

## Public-repository hygiene

This is a public repository. Only use public research material and public-safe normalized records.

Do not commit:

- API keys, tokens, credentials or secrets;
- private account, wallet or portfolio information;
- private Telegram / Discord / paid-source content;
- Hermes private configuration;
- local-machine secrets;
- copyrighted source material that cannot legally be redistributed.

Where redistribution rights are unclear, cite and normalize the idea instead of copying the original work wholesale.

---

## Push workflow

Any Scout may use the local GitHub CLI / Git tooling to update this repository.

For each research run:

1. Read this README.
2. Search public external sources for worthwhile alpha candidates.
3. Resolve the current canonical Wiki Brain strategy-research specification, then normalize each worthwhile candidate to the schema it declares.
4. Preserve source provenance and label all third-party results as source-reported.
5. Commit the resulting Markdown record(s).
6. Push them to this repository.
7. Stop there. ChatGPT will perform Research Intake Review and direct Wiki Brain ingestion separately.

The goal is simple:

> **Scout output should already equal Wiki Brain-ready input.**

This minimizes repeated interpretation, repeated summarization and unnecessary token consumption across Antigravity, ChatGPT and Hermes.

---

## Scheduled Research Scouts

Each Research Scout runs on its own schedule and is intentionally **high-frequency but low-output**. Its job is to keep looking, not to manufacture a quota.

For every scheduled run:

1. Sync and inspect the latest `origin/main` before researching. Do not overwrite or casually rewrite another scout's existing artifact.
2. Read this README on every run for the workflow contract, then resolve and read the current canonical versioned Wiki Brain strategy-research specification for the record schema.
3. Search public, traceable sources (GitHub / FMZ / TradingView / papers / blogs / public research; TradingView limited to public, traceable strategy/idea/script/research URLs with stable URL and as-of date preserved, private/paid not valid) for new alpha strategies or falsifiable alpha hypotheses.
4. Check existing repository records and sources before creating anything. Scout dedup: same canonical source identity + materially same normalized rule => do not create a new artifact; same source but materially distinct hypothesis/signal/horizon/mechanism may be independent (independent only when the core hypothesis differs materially in at least one of mechanism, signal construction, universe/market type, horizon/regime, or material data dependency). Exact duplicates, trivial paraphrases, and materially identical captures should produce no new artifact.
5. Produce **at most 3** new strategy records in one run. **Zero is a valid and successful result. Never manufacture candidates to satisfy a quota.** Three is a hard ceiling, not a target; prefer zero or one strong record over filling available slots with marginal material.
6. Preserve hybrid/composite structure when the thesis depends on multiple components. Do not collapse a hybrid into one prominent indicator.
7. If strategy identity, signal semantics, causal timing, required data, provenance, or public-use rights are materially ambiguous, do not guess. Skip that candidate for this run rather than emitting false precision.
8. Every emitted artifact must already satisfy the current canonical strategy-research schema and remain `research-only`, `not-implemented`, and `not-approved`.
9. Commit only artifacts intentionally created or corrected by the current run. If no candidate clears the bar, create no empty commit.
10. Push explicitly to `origin main`, verify the remote contains the commit, then stop. Do not write to Hermes Wiki Brain, PyBroker, Nautilus, Paper, Testnet, or Live workflows.
11. Fail closed on dirty unrelated worktree state, merge/rebase conflict, repository-sync failure, source/provenance failure, secret/public-safety concern, or push failure. Report the exact block instead of creating a fallback artifact elsewhere.

The scheduled scouts and the ChatGPT Research Intake Review process are deliberately separate. A successful Scout push means only that a research artifact entered the public staging pool; it does **not** mean the artifact passed Research Intake Review or entered Wiki Brain.

**No Scout may directly promote or write to Hermes Wiki Brain.** All Wiki Brain ingestion goes through ChatGPT Research Intake Review exclusively.
