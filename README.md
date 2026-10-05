# alpha-strategy-research

**English** | [繁體中文](README.zh-TW.md)

## 📊 HB_READY Strategy Pool

**Admitted strategies on main: 4**

## 📌 Current Backtest Baseline

**v0.1 — 2026-10-05**

- Universe: `BTCUSDT`, `ETHUSDT`, `BNBUSDT`, `SOLUSDT`, `XRPUSDT`, `DOGEUSDT`, `LINKUSDT`
- Timeframes: `1h` / `4h` / `1d`
- Backtest scope: full available historical Kline range for each symbol × timeframe; no cherry-picked window
- Per-strategy capital: Base Order `6%` + Safety Order `6%` + Safety Order `6%` = max `18%`
- Futures setup: Isolated; test both `3×` and `5×`; single-strategy backtests do not compound
- Research variables: strategy parameters and DCA spacing; keep the strategy skeleton fixed
- First-pass hard filters: `ROI > 0` and `Sharpe ≥ 1.0`
- [Open the full visual baseline →](docs/hb-backtest-baseline-v0.1.html)

Public canonical strategy-research repository for strategies that have passed the current **LOSSLESS HB_READY** GitHub admission gate.

## Current contract

Effective **2026-10-05 (UTC+8)**:

- `main` is the canonical pool of admitted strategy records.
- A root-level strategy Markdown record on `main` means it has passed GitHub review for **LOSSLESS HB_READY** under the current pinned Hummingbot semantics.
- Scheduled Scouts do **not** push strategy records directly to `main`.
- Every new strategy enters through a same-repository `research/*` pull request.
- OpenCode GitHub review is the admission gate.
- If a missing fact is explicitly recoverable from a primary source, the reviewer may repair the same PR branch and re-review it.
- If the source itself cannot support a complete lossless strategy, the PR is closed.
- A passing strategy PR is squash-merged to `main`.
- There is no separate validated-strategy repository and no second semantic suitability gate after merge.

The detailed reviewer policy is [`.github/HB_READY_REVIEW.md`](.github/HB_READY_REVIEW.md).

### Pinned admission baseline

Current strategy admission is evaluated against:

- Hummingbot package: `20260920`
- Hummingbot VERSION: `dev-2.17.0`

A newer Hummingbot build does **not** silently broaden eligibility. The admission contract must be explicitly reviewed and updated before new engine semantics are assumed.

## Repository meaning

This repository is intentionally narrow.

A strategy record on `main` means:

> The source strategy is complete enough, causal enough, and compatible enough to be represented by the pinned Hummingbot backtester **1:1 without material approximation**.

It does **not** mean:

- the strategy is profitable;
- the source-reported performance has been independently reproduced;
- the strategy is a survivor;
- the strategy has passed Hummingbot or Qlib performance validation;
- the strategy is approved for Paper, Testnet, Mainnet, or live trading.

All admitted records remain research-only unless a later workflow explicitly changes that status.

## Current flow

```text
public primary source
        ↓
ChatGPT / Hermes Scout
        ↓
research/<scout>-<slug>-<YYYYMMDD-HHMM>
        ↓
GitHub pull request
        ↓
OpenCode LOSSLESS HB_READY review
        ├─ source-backed fact missing
        │      ↓
        │  repair same PR branch
        │      ↓
        │  synchronize → fresh review
        │
        ├─ HB_READY: PASS
        │      ↓
        │  exact-head squash merge
        │
        └─ HB_READY: NOT_LOSSLESS
               ↓
             close PR
        ↓
main = canonical HB_READY strategy pool
```

Automated strategy PRs must not be left indefinitely in `REQUEST_CHANGES`.

## LOSSLESS HB_READY hard gate

Every admitted strategy must satisfy all applicable requirements below.

### 1. Market structure

- one trading pair per run;
- spot or perpetual applicability must be explicit or deterministically inferable from the primary source;
- no cross-sectional ranking;
- no pair-spread strategy;
- no shared portfolio-capital logic across symbols;
- no multi-pair shared state;
- spot strategies must not require naked shorting.

### 2. Timeframe

- current decision timeframe must be one of `1h`, `4h`, or `1d`;
- current Scouts should prefer a single decision timeframe;
- multi-timeframe candidates are out of the normal Phase-1 lane unless exact causal alignment can be demonstrated without changing source semantics.

### 3. Data dependency

The core trading signal must be computable from candle data available to the current Hummingbot backtester:

- OHLCV;
- deterministic, causal indicators derived from those candles.

A strategy is not admitted when its edge materially requires unsupported data such as:

- funding;
- open interest;
- mark/index price;
- liquidation feed;
- trade/aggressor feed;
- L2/order book;
- on-chain data;
- options / IV / Greeks;
- sentiment or news;
- macro data;
- cross-venue state.

### 4. Deterministic signal

Every strategy-critical rule must be explicit enough that two independent implementers would produce the same causal signal logic.

As applicable, the record must preserve:

- indicator/formula variant;
- source price;
- lookback;
- smoothing method;
- threshold;
- crossover / comparison semantics;
- AND / OR logic;
- state transitions;
- conflict priority.

Missing strategy-critical values must not be invented.

### 5. Direction

- long and short rules must both be explicit; or
- one side must be explicitly disabled.

### 6. Entry / exit / risk semantics

The source strategy must make all applicable behavior explicit:

- entry;
- signal exit;
- opposite-signal exit;
- stop loss;
- take profit;
- trailing stop;
- time limit;
- no-exit / disabled behavior.

Do not rely on silent Hummingbot defaults.

### 7. Execution timing

Current lossless admission requires compatibility with:

```text
completed bar
    ↓
signal decision
    ↓
same-bar close execution
```

The current lane rejects strategies that materially require:

- next-bar-open execution;
- maker-touch / queue semantics;
- intrabar path ordering;
- any fill convention the pinned Hummingbot backtester cannot reproduce 1:1.

Never approximate next-open with close.

### 8. Position / re-entry / gating

Where material, the source must define or make provably irrelevant:

- sizing behavior;
- fixed vs compounding sizing;
- pyramiding / repeated entry;
- maximum same-side concurrency;
- cooldown;
- re-entry behavior.

If ambiguity can change trade count, timing, direction, or amount, the strategy is not LOSSLESS.

### 9. Cost / engine-model compatibility

The strategy edge must not depend materially on behavior the current backtester cannot model losslessly, including:

- maker/taker asymmetry;
- spread capture;
- queue priority;
- partial fills;
- unsupported slippage / impact;
- funding PnL;
- liquidation / margin mechanics;
- leverage effects not reproduced by the backtester.

If the source does not state a cost model and costs are not part of the signal or trade-sequence semantics, record the gap explicitly. A later benchmark fee is a runtime assumption, not a source-reported strategy rule.

### 10. Warmup / causality

- all indicator lookbacks must be known so warmup can be derived;
- no repainting;
- no future-bar reference;
- no negative shift that leaks future information;
- no future extrema;
- no full-sample normalization that leaks future data;
- no other look-ahead leakage.

### Admission rule

If **any material strategy rule requires approximation, semantic invention, or unresolved interpretation**, the strategy is `NOT_LOSSLESS` and must not be merged.

## GitHub review and auto-remediation

The reviewer may repair a strategy PR only when the corrected fact is explicitly verifiable from a primary source, for example:

- public Pine/source code;
- immutable GitHub source;
- paper methods / tables / figures;
- official first-party strategy documentation.

Examples of acceptable repair:

- omitted indicator length;
- threshold;
- source price;
- timeframe;
- `process_orders_on_close`;
- pyramiding;
- explicit direction;
- source-declared stop / target;
- source-declared execution or cost assumption.

The reviewer must **not**:

- invent a parameter;
- choose among plausible variants;
- add a stop / target / cooldown;
- convert next-bar-open into same-bar-close;
- remove a material data dependency;
- redesign a strategy merely to make it HB_READY.

### Terminal review outcomes

`HB_READY: AUTO_REMEDIATED`

- reviewer repairs only source-verifiable facts on the same PR branch;
- commits only the corrected strategy file;
- stops;
- the resulting `synchronize` webhook triggers a fresh review.

`HB_READY: PASS`

- current immutable PR head passes every admission gate;
- reviewer records the evidence;
- merge uses the exact reviewed head SHA;
- PR is squash-merged to `main`.

`HB_READY: NOT_LOSSLESS`

- source is materially underspecified, incompatible, or would require invention;
- reviewer records the exact blocker;
- PR is closed.

Maintenance/documentation/configuration PRs are **not** strategy-admission PRs. They receive ordinary review and are not automatically merged or closed by the HB_READY strategy policy.

## Scout contract

Current active scheduled writers:

- **ChatGPT TradingView HB-Ready Scout** — hourly at `:14` Asia/Taipei; TradingView-only.
- **Hermes HB-Ready Quant Research Scout** — hourly at `:35` Asia/Taipei; broader public-source research.

Antigravity and MiMo scheduled strategy-research lanes remain disabled.

For every Scout cycle:

1. read current `README.md` and `.github/HB_READY_REVIEW.md`;
2. inspect current `main`;
3. deduplicate against both `main` and open `research/*` PRs;
4. read the primary source directly;
5. apply the LOSSLESS HB_READY hard gate before writing;
6. create at most **one** candidate PR;
7. zero candidates is a valid successful cycle;
8. never lower the gate to satisfy cadence.

### PR-only write rule

A scheduled Scout that finds one valid candidate must:

1. create a same-repository branch beginning with `research/`;
2. use a unique branch name, normally including Scout identity, strategy slug, and Asia/Taipei timestamp;
3. add exactly **one** new root-level strategy Markdown record;
4. make no unrelated file changes;
5. open a PR to `main`;
6. stop after verifying the PR.

The Scout must not:

- push a strategy directly to `main`;
- approve its own PR;
- merge its own PR;
- close its own PR;
- bypass GitHub review;
- write to Hummingbot, Qlib, n8n, survivor, Paper, Testnet, or Live systems.

## Public source contract

Eligible sources include public, traceable material such as:

- TradingView public strategy / idea / script pages;
- GitHub implementations;
- FMZ;
- papers / preprints;
- reputable public research;
- public technical documentation.

Reject or skip:

- private content;
- paid-only / invite-only content;
- inaccessible source logic;
- marketing-only pages;
- generic explainers without reconstructable rules;
- materially underspecified strategy sources.

### Provenance

For GitHub sources, preserve:

- repository URL;
- full commit SHA;
- exact file path;
- relevant source URL.

For TradingView sources, preserve the stable public URL and source/as-of date. Public Pine/source logic may be inspected, but large copyrighted source blocks should not be copied into this repository.

For papers, preserve the stable paper identity, version/date, and exact table/figure/section provenance for quantitative claims where available.

## Deduplication

Before opening a PR, search current `main` and open `research/*` PRs.

Do not create a new candidate when the same canonical source identity and materially identical normalized rule already exist.

Exact duplicates, paraphrases, and trivial parameter variants are not new strategies.

A source may justify another record only when it contains a materially distinct trading mechanism, signal construction, market/universe, horizon/regime, or material data dependency.

## Strategy record schema

Current records use:

```yaml
schema: strategy-research-record-v1
```

Required frontmatter:

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
  - <traceable public source>
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---
```

`confidence` describes confidence in the research interpretation, not expected profitability.

### Required document structure

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

Keep unavailable information explicit rather than deleting required sections.

For newly researched material, normally state:

```text
Not independently reproduced.
```

unless independent reproduction actually occurred.

### Strategy-critical source gaps

A research record may describe non-critical provenance limitations, but an admitted strategy must not contain an unresolved strategy-critical gap.

Examples of strategy-critical gaps:

- unknown indicator length;
- unknown threshold;
- ambiguous entry timing;
- ambiguous exit rule;
- unknown direction;
- unknown pyramiding/re-entry behavior when material;
- execution convention that changes trade timing;
- required unsupported data.

Such a candidate must be repaired from the primary source before merge or closed as `NOT_LOSSLESS`.

## File naming

Use lowercase, hyphen-separated filenames without spaces.

Preferred pattern:

```text
<strategy-or-topic-slug>-<YYYY-MM-DD>.md
```

Do not use ambiguous suffixes such as `latest`, `final`, or `new`.

## Downstream boundary

This repository owns **research normalization + HB_READY admission** only.

Current intended downstream model:

```text
alpha-strategy-research/main
        │
        ├── thin deterministic translation → Hummingbot Controller/config
        │                                   → Hummingbot backtest
        │
        └── thin deterministic translation → Qlib signal/adapter
                                            → Qlib backtest
```

The same canonical strategy semantics must feed both engines.

Downstream translators may change format, but must not reinterpret or invent:

- indicators / parameters;
- timing;
- entry / exit;
- sizing;
- pyramiding;
- cooldown / re-entry;
- execution semantics.

Qlib may be more expressive than Hummingbot, but strategies admitted here intentionally stay inside the stricter current Hummingbot-lossless subset.

The automatic repo-to-Hummingbot/Qlib execution bridge is **not defined by this repository README as already active**. Backtest dispatch, result reconciliation, survivor promotion, Testnet, and Live execution remain separate workflows.

The old Research Intake Review → Wiki ingestion → preparation backlog → Qlib-first automatic flow is no longer the current admission contract and must not be inferred from historical commits.

## Public-repository hygiene

This is a public repository.

Never commit:

- credentials, tokens, API keys, or secrets;
- private account, wallet, or portfolio information;
- private chats;
- paid/private research content;
- local-machine secrets or private Hermes configuration;
- copyrighted source material that should not be redistributed.

Normalize and cite source logic instead of copying large source passages.

## Principle

The repository should remain simple:

> **If a strategy record is on `main`, downstream systems may trust that its source semantics have already passed the current LOSSLESS HB_READY admission gate.**

That is the purpose of this repository.
