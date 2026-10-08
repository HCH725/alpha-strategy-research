# alpha-strategy-research

**English** | [繁體中文](README.zh-TW.md)

## 📊 HB_READY PASS Strategy Pool

**Admitted strategies on main: 44** <!-- HB_READY_POOL_COUNT -->

Every root-level strategy record on `main` MUST have `hb_ready_status: PASS`. This count is the number of those records; it must match the number of root-level strategy records, excluding the two READMEs. Historical research with non-PASS statuses is preserved outside `main`.

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
- Qlib Research Survivor → Hummingbot first-pass hard filters: `Annualized Net Return ≥ 10%` and `Sharpe ≥ 1.0` on the same run/sample; `Net Strategy ROI` is report-only, not an independent hard filter. These are downstream performance criteria, not HB_READY admission gates
- Annualized net return uses the complete equity curve net of verified fees, slippage and funding costs under the same canonical Hummingbot model, over a fixed continuous tradable evaluation period from the first legally possible post-warmup signal to the predetermined end, including flat time—not from the first winning trade. See v1.0 for invalid-run exclusions, retained metrics and the planned/unverified metric implementation boundary
- [Backtest Baseline v1.0 →](docs/hb-backtest-baseline-v1.0.md)
- [Archived visual baseline v0.1 →](docs/hb-backtest-baseline-v0.1.html)

**HB_READY PASS-only strategy pool:** Every strategy record on `main` must satisfy all six Hummingbot expressibility gates. Non-PASS research remains accessible on non-main Git branches or in existing PR/history; it is never promoted by relabeling.

## Current contract

**Effective 2026-10-08 (UTC+8): `main` is PASS-only, with no exceptions for historical reconstruction or manual review.**

- Every root-level strategy Markdown record on `main` (except `README.md` and `README.zh-TW.md`) MUST include frontmatter `hb_ready_status: PASS` supported by an independent review of the existing six gates. Non-PASS, absent, invalid, or unreviewed status is a merge blocker, **regardless of branch name, reviewer, or PR type**.
- `NOT_LOSSLESS` and `NOT_ASSESSED` remain valid assessment labels **outside `main` only**: draft, rejected or archived research may live on PR branches, an existing archive branch or immutable Git history. Do not delete its scientific provenance; do not bypass by marking it PASS.
- Automated Scouts may propose exactly one strategy via `research/*` PR; only source-verifiable remediation and a completed six-gate PASS permit an exact-head merge; failure closes the Scout PR.
- Non-Scout `reconstruction/*` / legacy PRs have **no admission exemption**. If they add or modify strategy records, require the same six-gate PASS review before merge; otherwise keep the PR unmerged or retain the research on a non-main branch. For current batch PR #58, its `NOT_LOSSLESS` records MUST NOT be merged as-is.
- Maintenance/docs PRs receive COMMENT-only review (never auto-merge), but their diffs must still preserve the PASS-only `main` invariant; removal/archiving of pre-existing non-PASS records is allowed **only without relabeling** and after verifying a recoverable branch/history reference.
- Previously preserved non-PASS families (AEAP/SEADS, QuantaAlpha, Wasserstein) were snapshotted in `archive/non-pass-research-20261008` before their removal from `main`; the 17-family reconstruction PR #58 remains an unmerged source. No new repository, folder, status or data pipeline is introduced.
- Current Hummingbot/Qlib performance research may trust `main` for HB_READY admission status **only**, not for profitability, Qlib parity or Testnet/Mainnet authorization. Historical Survivor metrics remain research evidence and never override the six gates.
- The README HB_READY pool count must equal the count of root-level strategy records on `main`; any mismatch fails the admission integrity check.

The detailed reviewer policy is [`.github/HB_READY_REVIEW.md`](.github/HB_READY_REVIEW.md).

### Pinned admission baseline

Current automated Scout HB_READY admission is evaluated against:

- Hummingbot package: `20260920`
- Hummingbot VERSION: `dev-2.17.0`

A newer Hummingbot build does **not** silently broaden eligibility. The admission contract must be explicitly reviewed and updated before new engine semantics are assumed.

## Repository meaning and workflow

`main` is a canonical pool of six-gate HB_READY **PASS-only** strategies. A PASS means the precisely described source-native or disclosed derived strategy can be causally expressed under the pinned Hummingbot benchmark; it is **not** a profitability, Qlib parity or live-trading approval.

Workflow: public source → `research/*` or `reconstruction/*` candidate branch → independent six-gate audit → only verified `hb_ready_status: PASS` may merge into `main`. `NOT_LOSSLESS` or `NOT_ASSESSED` may be preserved in the existing archive branch/PR/Git history but never on `main`. Maintenance/documentation changes remain COMMENT-only and may not create a bypass for non-PASS strategies.

Previously approved PASS records remain PASS subject to future explicit re-review if new evidence identifies a semantic error. Do not retroactively upgrade historical Survivor records.

All records remain `status: research-only` and `adoption: not-approved` unless a separate downstream authorization changes them.

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

If any of the six requirements is materially incomplete, unverifiable or unsupported by the pinned engine, the strategy record MUST NOT merge into `main`, whether it is a Scout, reconstruction, historical or other PR. Scout `research/*` PRs are closed as `NOT_LOSSLESS` with precise reasons; other non-PASS research can remain on a non-main branch or PR for further work. Existing assessment labels and `strategy-research-record-v1` format remain unchanged; no archive bypass or automatic upgrade of historical survivors is permitted.

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

Non-Scout legacy/reconstruction strategy PRs MUST also pass the six HB_READY gates to merge into `main`; status `NOT_LOSSLESS` / `NOT_ASSESSED` means preserve outside `main`, never merge by exception. Maintenance/documentation/configuration PRs receive COMMENT-only review, with a required PASS-only integrity check if they touch root-level strategy records or pool counts.

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

A draft or archived research record outside `main` may preserve strategy-critical gaps under `NOT_LOSSLESS` or `NOT_ASSESSED`; `main` may not contain such gaps or non-PASS statuses. Automated Scout admission still requires PASS and closes NOT_LOSSLESS candidates.

Examples of strategy-critical gaps:

- unknown indicator length;
- unknown threshold;
- ambiguous entry timing;
- ambiguous exit rule;
- unknown direction;
- unknown pyramiding/re-entry behavior when material;
- execution convention that changes trade timing;
- required unsupported data.

For all strategy PR types, such a candidate must be repaired from primary evidence or submitted as a fully disclosed derived strategy before it can receive PASS; otherwise it remains outside `main`. A Scout PR without a verifiable repair is closed as `NOT_LOSSLESS`.

## File naming

Use lowercase, hyphen-separated filenames without spaces.

Preferred pattern:

```text
<strategy-or-topic-slug>-<YYYY-MM-DD>.md
```

Do not use ambiguous suffixes such as `latest`, `final`, or `new`.

## Downstream boundary

This repository's `main` owns **only independently reviewed HB_READY PASS strategy records**. Any incomplete/non-PASS research is preserved on other branches, PRs or existing Git history, not merged into `main`.

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
Annualized Net Return ≥ 10% AND Sharpe ≥ 1.0
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

> **Every strategy record in `main` must be independently reviewed `hb_ready_status: PASS`. No historical/reconstruction/manual exemption; PASS is not Qlib parity, profitability or live trading approval.**

That is the purpose of this repository.

