# alpha-strategy-research

**English** | [繁體中文](README.zh-TW.md)

## 📊 HB_READY PASS Strategy Pool

**Admitted strategies on main: 10** <!-- HB_READY_POOL_COUNT -->

This count includes only root-level strategy records whose frontmatter has `hb_ready_status: PASS`; it is not a count of every Markdown file or every record on `main`.

## 📌 Current Backtest Baseline

**v1.0 — 2026-10-05**

- Universe: `BTCUSDT`, `ETHUSDT`, `BNBUSDT`, `SOLUSDT`, `XRPUSDT`, `DOGEUSDT`, `LINKUSDT`
- Timeframes: `1h` / `4h` / `1d`
- Base matrix: `7 symbols × 3 timeframes × 2 leverage settings = 42 cells` before parameter expansion
- Backtest scope: full available historical Kline range for each symbol × timeframe; no cherry-picked window
- House execution overlay: every `hb_ready_status: PASS` strategy entering current Hummingbot/Qlib performance research uses Base Order `6%` + Safety Order `6%` + Safety Order `6%` = max `18%`
- DCA spacing and strategy parameters are research-defined by Hermes; final OOS data must not be used to retune them
- Futures setup: Binance USDT-M perpetual, Isolated, `3×` and `5×`, single-strategy stage does not compound
- Costs: pinned Binance non-VIP USDⓈ-M fees plus historical realized funding; no silent zero-cost assumptions
- Engine rule: Hummingbot is canonical; Qlib is trusted for mass screening only after event-level parity
- Promotion rule: only `PASS` records are eligible for current Qlib screening; survivor candidates are later re-run in Hummingbot for trade-by-trade validation
- First-pass hard filters remain `ROI > 0` and `Sharpe ≥ 1.0`; metric semantics must align to the Hummingbot benchmark
- [Backtest Baseline v1.0 →](docs/hb-backtest-baseline-v1.0.md)
- [Archived visual baseline v0.1 →](docs/hb-backtest-baseline-v0.1.html)

Public canonical strategy-research corpus for normalized, source-backed strategy records. **LOSSLESS HB_READY** is a per-record status, not a condition for a record to be preserved on `main`.

## Current contract

Effective **2026-10-06 (UTC+8)**:

- `main` is the canonical strategy-research corpus, not a PASS-only pool.
- A root-level strategy record means normalized, source-backed research; its presence on `main` does not imply HB_READY.
- Every record carries `hb_ready_status: PASS | NOT_LOSSLESS | NOT_ASSESSED`. Read HB_READY from this field.
- Only `PASS` records may enter the current Hummingbot/Qlib performance-research downstream. `NOT_LOSSLESS` and `NOT_ASSESSED` are valid records on `main` and must not be discarded solely because current Hummingbot cannot express them losslessly.
- Scheduled Scouts pre-filter for HB_READY candidates and keep using same-repository `research/*` admission PRs. Automated Scout PRs require `PASS` to merge; a `NOT_LOSSLESS` Scout candidate is closed.
- Reconstructed or legacy research records use a non-Scout branch such as `reconstruction/*` or `maintenance/*` and may merge after independent provenance/research review with `NOT_LOSSLESS` or `NOT_ASSESSED`. They remain ordinary root-level strategy records and are not auto-consumed downstream. The branch distinction is process-only, not a content class.
- Historical survivor/Qlib evidence belongs in the normal Provenance and Evidence sections, labeled historical and not as current Hummingbot reproduction. Keep same-family variants in one strategy-family record with multiple historical evidence entries unless evidence establishes materially different core mechanisms. No special survivor folder, class, or tag is required.
- Scheduled Scouts do **not** push strategy records directly to `main`.
- For automated Scout admission, OpenCode GitHub review is the LOSSLESS HB_READY gate. A source-verifiable missing fact may be repaired on the same PR branch and re-reviewed; a source that cannot support lossless semantics is not merged through this lane.
- Passing Scout strategy PRs are squash-merged to `main`. There is no separate validated-strategy repository; downstream eligibility is determined by `hb_ready_status: PASS`, not by presence on `main` alone.

The detailed reviewer policy is [`.github/HB_READY_REVIEW.md`](.github/HB_READY_REVIEW.md).

### Pinned admission baseline

Current automated Scout HB_READY admission is evaluated against:

- Hummingbot package: `20260920`
- Hummingbot VERSION: `dev-2.17.0`

A newer Hummingbot build does **not** silently broaden eligibility. The admission contract must be explicitly reviewed and updated before new engine semantics are assumed.

## Repository meaning

This repository is the canonical corpus of normalized, source-backed strategy research. A root-level record on `main` means the research is preserved in the ordinary strategy-record format; it does not by itself establish HB_READY.

The per-record `hb_ready_status` field defines current engine expressibility:

- `PASS`: source-core signal and causal trade-event semantics can be reconstructed without material approximation under the pinned Hummingbot semantics; eligible for current Hummingbot/Qlib performance-research downstream.
- `NOT_LOSSLESS`: a material source rule is underspecified or incompatible with current Hummingbot; valid research on `main`, but not eligible for that downstream.
- `NOT_ASSESSED`: current LOSSLESS HB_READY review has not been completed; valid research on `main`, but not eligible for that downstream.

Non-PASS records must not be discarded merely because current Hummingbot cannot express them losslessly. A status of `PASS` does **not** mean:

- the strategy is profitable;
- the source-reported performance has been independently reproduced;
- the strategy is a survivor;
- it has passed Hummingbot or Qlib performance validation;
- it is approved for Paper, Testnet, Mainnet, or live trading.

All records remain research-only unless a later workflow explicitly changes that status.

## Current flow

```text
public primary source
        ↓
scheduled Scout (pre-filter HB_READY)
        ↓
research/<scout>-<slug>-<YYYYMMDD-HHMM>
        ↓
automated Scout PR review
        ↓
PASS → exact-head squash merge; NOT_LOSSLESS → close Scout PR

legacy / reconstructed research
        ↓
reconstruction/* or maintenance/* PR
        ↓
independent provenance + research review
        ↓
ordinary root-level record (PASS / NOT_LOSSLESS / NOT_ASSESSED)

main = canonical strategy-research corpus
        ↓
current Hummingbot/Qlib performance research selects PASS only
```

Automated Scout strategy PRs must not be left indefinitely in `REQUEST_CHANGES`. The non-Scout legacy/reconstruction path is ordinary research review; it is not subject to Scout auto-close and does not create a separate record class.

## LOSSLESS HB_READY hard gate

Every strategy record marked `hb_ready_status: PASS` must satisfy all applicable requirements below.

### 1. Market structure

- one trading pair per run;
- preserve source market/contract identity when it changes signal data, bars, timing, direction, or source applicability; otherwise, the house overlay may choose an explicitly labeled research market;
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

The source must define or make provably irrelevant any behavior that can change the trade-event sequence, timing, direction, or exits:

- pyramiding / repeated entry;
- maximum same-side concurrency;
- cooldown;
- re-entry behavior;
- position-aware state used by later signals or exits.

Source sizing and fixed-vs-compounding behavior may be replaced by the house overlay only when that replacement is event-neutral. The overlay must not invent missing signal, entry, exit, or re-entry rules. If unresolved behavior can change the trade-event sequence, timing, direction, or exits, the strategy is not LOSSLESS.

### 9. Cost / engine-model compatibility

Hard-gate behavior the strategy edge or event logic materially depends on when the current backtester cannot model it losslessly, including:

- maker/taker asymmetry;
- spread capture;
- queue priority;
- partial fills;
- unsupported slippage / impact;
- funding-dependent signal or event logic;
- liquidation / margin mechanics used by the strategy;
- leverage effects that change signal or trade events.

Pure PnL/accounting costs that do not materially affect the strategy edge or event logic may be normalized using pinned house assumptions; record those assumptions explicitly and do not present them as source-reported rules. The overlay must not substitute a different price series when source contract identity is material.

### 10. Warmup / causality

- all indicator lookbacks must be known so warmup can be derived;
- no repainting;
- no future-bar reference;
- no negative shift that leaks future information;
- no future extrema;
- no full-sample normalization that leaks future data;
- no other look-ahead leakage.

### Admission rule

If any material source-core signal or trade-event rule requires approximation, semantic invention, or unresolved interpretation, the record cannot be `PASS`. An automated Scout admission PR with this outcome is `NOT_LOSSLESS` and is closed; an ordinary non-Scout research record may remain on `main` with its non-PASS status after independent review. House overlays may replace only event-neutral sizing, capital, or accounting assumptions; they must never invent missing signal, entry, exit, or re-entry rules, or substitute a different price series when contract identity is material.

## GitHub review and auto-remediation

For automated Scout `research/*` admission PRs, the reviewer may repair a strategy only when the corrected fact is explicitly verifiable from a primary source, for example:

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
- the record has `hb_ready_status: PASS`;
- reviewer records the evidence;
- merge uses the exact reviewed head SHA;
- PR is squash-merged to `main`.

`HB_READY: NOT_LOSSLESS`

- source is materially underspecified, incompatible, or would require invention;
- reviewer records the exact blocker;
- automated Scout `research/*` admission PR is closed.

Non-Scout legacy/reconstruction strategy records use a non-`research/*` branch and ordinary independent provenance/research review; they may be merged as `NOT_LOSSLESS` or `NOT_ASSESSED` and must not be auto-consumed downstream. This branch distinction is not a content-class distinction. Maintenance/documentation/configuration PRs also receive ordinary review and are not automatically merged or closed by the Scout HB_READY policy.

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
5. pre-filter for HB_READY, then apply the LOSSLESS HB_READY hard gate before writing;
6. create at most **one** candidate PR;
7. automated Scout PRs merge only with `hb_ready_status: PASS`; `NOT_LOSSLESS` candidates close;
8. zero candidates is a valid successful cycle;
9. never lower the gate to satisfy cadence.

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

Same-family survivor variants should normally be consolidated into one strategy-family record with multiple historical Evidence entries unless evidence demonstrates materially different core mechanisms. Put historical survivor/Qlib evidence under the ordinary Provenance/Evidence sections and label it historical, not current Hummingbot reproduction. No special survivor folder, class, or tag is required.

## Strategy record schema

Current records use:

```yaml
schema: strategy-research-record-v1
```

The schema remains `strategy-research-record-v1`; `hb_ready_status` is an additive field, not a schema-version change.

Required frontmatter:

```yaml
---
schema: strategy-research-record-v1
hb_ready_status: PASS | NOT_LOSSLESS | NOT_ASSESSED
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

A research record may preserve strategy-critical gaps when its `hb_ready_status` is `NOT_LOSSLESS` or `NOT_ASSESSED`; it must not be marked `PASS` while such a gap remains. Automated Scout admission still requires PASS and closes NOT_LOSSLESS candidates.

Examples of strategy-critical gaps:

- unknown indicator length;
- unknown threshold;
- ambiguous entry timing;
- ambiguous exit rule;
- unknown direction;
- unknown pyramiding/re-entry behavior when material;
- execution convention that changes trade timing;
- required unsupported data.

For automated Scout admission, such a candidate must be repaired from the primary source before it can receive PASS; otherwise that Scout PR is closed as `NOT_LOSSLESS`. An ordinary non-Scout research record may preserve the gap on `main` after independent review, with a non-PASS status.

## File naming

Use lowercase, hyphen-separated filenames without spaces.

Preferred pattern:

```text
<strategy-or-topic-slug>-<YYYY-MM-DD>.md
```

Do not use ambiguous suffixes such as `latest`, `final`, or `new`.

## Downstream boundary

This repository owns **research normalization + explicit per-record HB_READY status**. The automated Scout lane admits only PASS strategies; other source-backed research may be preserved on `main` after ordinary independent review.

Current intended downstream model:

```text
alpha-strategy-research/main
        ↓
filter: hb_ready_status == PASS
        ↓
standardized research overlay
(DCA: 6% + 6% + 6%, Isolated, 3× / 5×)
        ↓
Qlib large-scale screening
        ↓
survivor candidates
        ↓
future Survivor Repo
        ↓
Hummingbot re-validation
        ↓
event-level parity confirmed
        ↓
Formal Survivor
        ↓
later Testnet / live qualification
```

Hummingbot is the canonical backtest/execution semantic benchmark. Qlib is the mass-screening engine only after the two engines have demonstrated event-level parity on the same source core strategy, data, house overlay, and pinned assumptions—not source-native sizing.

For PASS records, HB_READY preserves the source strategy's core signal and causal trade-event semantics. The standardized DCA/capital/leverage layer is an explicit **research execution overlay** applied downstream only to PASS strategies; it may replace event-neutral source sizing but must not invent missing signal, entry, exit, or re-entry rules, substitute a different price series when contract identity is material, or be misrepresented as source-native behavior.

For parity, matching final ROI or Sharpe is not sufficient. Signal time, entry/exit time, direction, price, position size under the same house overlay, Safety Orders and close transitions must agree trade by trade.

The automatic repo-to-Hummingbot/Qlib execution bridge is **not defined by this repository README as already active**. The new Survivor Repo is also not created yet. Formal large-scale screening resumes only after Hummingbot ↔ Qlib parity is proven.

The old Research Intake Review → Wiki ingestion → preparation backlog → n8n → Qlib-first automatic flow is deprecated and is not the current admission or execution contract.

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

> **If `hb_ready_status: PASS`, downstream systems may trust current LOSSLESS HB_READY semantics; presence on `main` alone means research preservation only.**

That is the purpose of this repository.
