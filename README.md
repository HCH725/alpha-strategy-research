# alpha-strategy-research

Public staging repository for external alpha-strategy research normalized for direct Hermes Wiki Brain ingestion.

## Purpose

This repository is the handoff layer between **Antigravity external research** and **ChatGPT review / Wiki Brain ingestion**.

Operating flow:

```text
External public sources
(GitHub / FMZ / papers / blogs / public research)
        ↓
Antigravity
find alpha ideas → understand → normalize → push here
        ↓
ChatGPT
review / audit
        ↓
ChatGPT writes approved knowledge directly into Hermes Wiki Brain
        ↓
Hermes uses the knowledge for research, synthesis and later validation
```

Antigravity does **not** write to Hermes Wiki Brain. The artifact pushed here should already be in Wiki Brain-native form so ChatGPT can review and promote it without another translation pass.

---

## Antigravity: read this README before every research run

Your job is to search public external sources for potentially useful **alpha strategies or alpha hypotheses**, then convert each worthwhile item into the exact research-record format below and push it to this repository.

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

All strategy records must use the existing Hermes Wiki Brain schema:

```text
strategy-research-record-v1
```

Do not invent another candidate schema.

### Required frontmatter

Every new external strategy record must begin with:

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

For papers, blogs, FMZ, TradingView or other public sources, preserve the most stable URL and the source/data as-of date.

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

Example:

```text
Source reports Sharpe 2.1 over the stated sample. This result has not been independently reproduced.
```

#### Independently reproduced

For new Antigravity discoveries, normally write:

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

## Research rules for Antigravity

1. **Search for alpha, not marketing claims.** A high reported return is not itself an alpha thesis.
2. **Single and hybrid strategies are both allowed.** Preserve meaningful component structure.
3. **Normalize before pushing.** The file pushed here must already be usable as a Wiki Brain `strategy-research-record-v1` artifact.
4. **Keep provenance.** External claims must remain traceable to their source.
5. **Do not claim independent validation that has not happened.**
6. **Do not silently repair missing information.** Mark gaps explicitly.
7. **Do not copy large source-code blocks unnecessarily.** Prefer normalized logic plus source references.
8. **Do not confuse risk management with alpha.** Stops, sizing, leverage, DCA, grid or martingale rules should be identified separately from the predictive signal.
9. **Do not confuse complexity with quality.** Multi-indicator combinations need a coherent thesis and remain unvalidated until tested.
10. **Do not write to Hermes Wiki Brain.** Push the normalized research artifact here. ChatGPT performs the review and, if accepted, writes it into Wiki Brain directly.

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

Antigravity may use the local GitHub CLI / Git tooling to update this repository.

For each research run:

1. Read this README.
2. Search public external sources for worthwhile alpha candidates.
3. Normalize each worthwhile candidate into `strategy-research-record-v1` format.
4. Preserve source provenance and label all third-party results as source-reported.
5. Commit the resulting Markdown record(s).
6. Push them to this repository.
7. Stop there. ChatGPT will perform review and direct Wiki Brain ingestion separately.

The goal is simple:

> **Antigravity output should already equal Wiki Brain-ready input.**

This minimizes repeated interpretation, repeated summarization and unnecessary token consumption across Antigravity, ChatGPT and Hermes.
