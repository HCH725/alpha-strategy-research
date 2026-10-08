# alpha-strategy-research

**English** | [繁體中文](README.zh-TW.md)

## 📊 HB_READY PASS Strategy Pool

**Admitted strategies on main: 39** <!-- HB_READY_POOL_COUNT -->

This count includes only root-level strategy records whose frontmatter has `hb_ready_status: PASS`; it is not a count of every Markdown file or every record on `main`.

## 📌 Current Backtest Baseline

**v1.0 research campaign — 2026-10-05 (not HB_READY admission limits)**

- Current research campaign universe (not a PASS whitelist): `BTCUSDT`, `ETHUSDT`, `BNBUSDT`, `SOLUSDT`, `XRPUSDT`, `DOGEUSDT`, `LINKUSDT`
- Current campaign timeframes (not a PASS whitelist): `1h` / `4h` / `1d`
- Base matrix: `7 symbols × 3 timeframes × 2 leverage settings = 42 cells` before parameter expansion
- Backtest scope: full available historical Kline range for each symbol × timeframe; no cherry-picked window
- Current campaign DCA experiment: Base Order `6%` + Safety Order `6%` + Safety Order `6%` = max `18%`; this is not an HB_READY admission prerequisite and is a separately declared derivative if it changes source trade events
- DCA spacing and strategy parameters are research-defined by Hermes; final OOS data must not be used to retune them
- Futures setup: Binance USDT-M perpetual, Isolated, `3×` and `5×`, single-strategy stage does not compound
- Costs: campaign target is pinned Binance non-VIP USDⓈ-M fees plus historical funding; the pinned generic simulator has not yet demonstrated historical funding accounting, so no campaign may claim complete realized-funding performance without a verified implementation
- Engine rule: Hummingbot is canonical; Qlib is trusted for mass screening only after event-level parity
- Promotion rule: only `PASS` records are eligible for current Qlib screening; survivor candidates are later re-run in Hummingbot for trade-by-trade validation
- First-pass hard filters remain `ROI > 0` and `Sharpe ≥ 1.0`; metric semantics must align to the Hummingbot benchmark
- [Backtest Baseline v1.0 →](docs/hb-backtest-baseline-v1.0.md)
- [Archived visual baseline v0.1 →](docs/hb-backtest-baseline-v0.1.html)

Public canonical strategy-research corpus for normalized, source-backed strategy records. **HB_READY six-gate engine expressibility** is a per-record status, not a condition for preserving research on `main`.

## Current contract

Effective **2026-10-08 (UTC+8)** for six-gate admission; historical research records and existing PASS labels are unchanged pending explicit re-review:

- `main` is the canonical strategy-research corpus, not a PASS-only pool.
- A root-level strategy record means normalized, source-backed research; its presence on `main` does not imply HB_READY.
- Every record carries `hb_ready_status: PASS | NOT_LOSSLESS | NOT_ASSESSED`. Read HB_READY from this field.
- Only `PASS` records may enter the current Hummingbot/Qlib performance-research downstream. `NOT_LOSSLESS` and `NOT_ASSESSED` are valid records on `main` and must not be discarded solely because current Hummingbot cannot express them losslessly.
- Scheduled Scouts pre-filter for HB_READY candidates and keep using same-repository `research/*` admission PRs. Automated Scout PRs require `PASS` to merge; a `NOT_LOSSLESS` Scout candidate is closed.
- Reconstructed or legacy research records use a non-Scout branch such as `reconstruction/*` or `maintenance/*` and may merge after independent provenance/research review with `NOT_LOSSLESS` or `NOT_ASSESSED`. They remain ordinary root-level strategy records and are not auto-consumed downstream. The branch distinction is process-only, not a content class.
- Historical survivor/Qlib evidence belongs in the normal Provenance and Evidence sections, labeled historical and not as current Hummingbot reproduction. Keep same-family variants in one strategy-family record with multiple historical evidence entries unless evidence establishes materially different core mechanisms. No special survivor folder, class, or tag is required.
- Scheduled Scouts do **not** push strategy records directly to `main`.
- For automated Scout admission, the Hermes Auditor GitHub webhook review applies the six-gate HB_READY contract. A source-verifiable missing fact may be repaired on the same PR branch and re-reviewed; a source that cannot support lossless semantics is not merged through this lane.
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

- `PASS`: this fully specified source-native or disclosed derived strategy passes all six causality/rule/pinned-engine expressibility requirements; eligible for current Hummingbot/Qlib performance-research downstream (not a guarantee of Qlib parity or profitability).
- `NOT_LOSSLESS`: a material rule, data dependency, or execution model is incomplete, unverified, or incompatible with pinned Hummingbot; valid research on `main`, but not eligible for that downstream.
- `NOT_ASSESSED`: current six-gate HB_READY review has not been completed; valid research on `main`, but not eligible for that downstream.

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

## HB_READY six-gate admission

**Removed as independent bans:** single trading pair, the `1h/4h/1d` decision-timeframe whitelist, OHLCV-only signals, and same-bar-close-only execution. No market, frequency, data category, or execution convention is disqualified *by its name alone*. Removal of a policy ban is **not** evidence that the pinned Hummingbot backtester can actually execute it. Gate 5 must demonstrate the required path, rather than assume support.

A candidate can be **source-native** (reproducing the primary-source rules) or an **explicitly derived executable strategy** (separately identified, with immutable primary-source lineage and all researcher-designed changes disclosed in existing `Provenance`, `Signal`, `Execution assumptions`, and `Limitations` sections). An adapted strategy is **never** evidence that the original source strategy itself passed. A reviewer may verify source facts but must not silently invent an adaptation to rescue a PR.

Every `hb_ready_status: PASS` record must satisfy **all six** requirements for the *specific version declared in that record*:

1. **Deterministic, reproducible signals.** Explicit formula/model artifact, source data, indicator variant, lookbacks, smoothing, thresholds, comparisons, state transitions and priority. Fitted/ML signals require pinned model/preprocessing/training cutoff and point-in-time inference inputs. Missing decision-critical rules cannot be guessed.
2. **Unambiguous trade direction.** Long/short intent is explicit or a side is explicitly disabled; market/contract permissions must be realistic.
3. **Complete entry, exit and risk rules.** Entry, signal/opposite exits, SL/TP/trailing/time limits and any intentionally disabled behavior are explicit; no hidden Hummingbot defaults.
4. **Complete position and re-entry state.** Pyramiding, simultaneous exposure, cooldown, size dependencies, safety orders and re-entry/state transitions are explicit or demonstrably irrelevant. Research-designed DCA may change entry/exit events; such an overlay is a **declared derivative/execution experiment**, not automatically event-neutral or source-native.
5. **Demonstrated pinned-engine and data-model compatibility.** Identify the exact Hummingbot package/image/commit and applicable controller/executor, connector, market(s), data feed(s), decision/availability timestamps, fills, costs, leverage/margin and accounting. Demonstrate that **all materially required** multi-asset synchronization/shared capital, lower or multi-timeframe alignment, non-OHLCV point-in-time inputs, next-open/maker/intrabar execution, and real costs can actually be modeled on the *specified* engine path. Unsupported or unverified requirements cannot receive PASS; a documented feature, generic executor name, or one supported interval is insufficient. Missing trade prices must not silently default to fabricated values. The currently verified subset may be narrower than Hummingbot's advertised capabilities. Source-native equivalence is assessed against the source; a disclosed derivative is assessed against **its own fully specified strategy**, not falsely represented as lossless source reproduction. Pin fees/funding/precision and flag unsupported economic terms; do not report hypothetical zero funding as realized funding.
6. **Warmup, point-in-time availability and causality.** Lookbacks/warmup are defined; no repainting, future bars/extrema, negative-shift leakage, full-sample leakage or use of incomplete higher-timeframe candles as completed signals. A signal's decision time must not precede the point when its inputs were available; fill order and same-bar ambiguities need explicit, supported semantics.

**PASS means admissible to *model-consistent research*, not profitability, economic realism, guaranteed source-native equivalence, Qlib parity, survivor status or Paper/Testnet/Live permission.** Profitable net-of-fee returns are a later performance/OOS question, **not** an HB_READY admission threshold. For new execution/data paths, pin the evidence and verify representative event-level Qlib/Hummingbot parity **before Qlib mass screening**, not before preserving a strategy record.

If any of the six requirements is materially incomplete, unverifiable or unsupported by the pinned engine, the automated Scout `research/*` PR is `NOT_LOSSLESS` and closed with the specific remaining blocker. Non-Scout research may still be preserved on `main` with `NOT_LOSSLESS` or `NOT_ASSESSED` after independent review. The existing status values and root-level `strategy-research-record-v1` format remain unchanged. Neither historical Survivor evidence nor removal of four bans retroactively upgrades a record to PASS.

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
5. pre-filter for HB_READY, then apply the six HB_READY gates without reinstating the old market/timeframe/data/timing bans;
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

Hummingbot is the canonical backtest/execution semantic benchmark. Before Qlib mass screening, the two engines must demonstrate event-level parity for the **specific declared source-native or derived executable strategy**, data, actual execution model, costs and pinned assumptions—not merely matching metrics.

For PASS records, HB_READY verifies the declared source-native or explicitly derived executable rules against the pinned Hummingbot model, without asserting profitability or source-native equivalence for adaptations. Standardized DCA/capital/leverage is a **downstream research experiment**, not a prerequisite for admission. Materially changed trade events require an independently specified derived strategy, full cost/causality checks and new evidence; source-native provenance must not be overwritten.

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

> **If `hb_ready_status: PASS`, downstream systems may treat the declared strategy as having passed the six-gate pinned-engine expressibility review (not Qlib parity or live readiness); presence on `main` alone means research preservation only.**

That is the purpose of this repository.
