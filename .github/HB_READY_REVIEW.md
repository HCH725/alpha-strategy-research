# HB_READY GitHub Review Contract — Six-Gate Engine Capability

Effective: 2026-10-08 (UTC+8)

This file defines **the same six-gate HB_READY strategy admission requirement for EVERY branch and PR type** targeting `HCH725/alpha-strategy-research` `main`, including Scout, historical reconstruction, maintenance PRs that touch strategy records, and manual contributions. Only automation actions differ by PR type.

## Scope

This review answers one question only:

> Is this specific, fully declared source-native or explicitly derived strategy causally reproducible and actually expressible by the pinned Hummingbot backtest model, with no hidden execution or data assumptions?

Pinned baseline:

- Hummingbot package: `20260920`
- Hummingbot VERSION: `dev-2.17.0`

**Effective 2026-10-08, `main` is PASS-only.** Every root-level strategy Markdown record on `main` (excluding the two READMEs) MUST carry independently verified `hb_ready_status: PASS`. `NOT_LOSSLESS`, `NOT_ASSESSED`, missing or invalid statuses may exist **only outside `main`**, including PR branches, `archive/non-pass-research-20261008`, and Git history. No legacy/reconstruction/manual review exception. PASS indicates bounded pinned-engine semantics, not profitable or live-tradable performance. Verify the post-change root strategy count equals the PASS count and the README pool count.

## Strategy PR shape

Automated Scout admission PRs must:

- target `main`;
- originate from the same repository;
- use a head branch beginning with `research/`;
- add exactly one root-level strategy Markdown record;
- contain no unrelated modifications.

They must receive `hb_ready_status: PASS` to merge through this lane; a `NOT_LOSSLESS` candidate is closed.

Non-Scout, reconstructed, legacy and manual strategy PRs have **the exact same six-gate PASS requirement** before any root-level strategy record may merge into `main`. They may receive COMMENT-only review and manual merge **only after PASS**, never an automatic PASS exemption. Unqualified research stays in existing non-main branches/PRs/history. PR #58 (17 non-PASS reconstructed families) must not merge as-is. Maintenance/docs/config PRs remain COMMENT-only (never auto-merge/close), but changes touching strategy records or counts must preserve the PASS-only `main` invariant. Removing previously committed non-PASS records is permitted after they are verifiably preserved on an existing archive Git branch; never relabel them to PASS merely to meet the invariant.

## HB_READY admission: six enforceable requirements

**Removed as independent bans:** single trading pair, the `1h/4h/1d` decision-timeframe whitelist, OHLCV-only signals, and same-bar-close-only execution. No market, frequency, data category, or execution convention is disqualified *by its name alone*. Removal of a policy ban is **not** evidence that the pinned Hummingbot backtester can actually execute it. Gate 5 must demonstrate the required path, rather than assume support.

A candidate can be **source-native** (reproducing the primary-source rules) or an **explicitly derived executable strategy** (separately identified, with immutable primary-source lineage and all researcher-designed changes disclosed in existing `Provenance`, `Signal`, `Execution assumptions`, and `Limitations` sections). An adapted strategy is **never** evidence that the original source strategy itself passed. A reviewer may verify source facts but must not silently invent an adaptation to rescue a PR.

Every `hb_ready_status: PASS` record must satisfy **all six** requirements for the *specific version declared in that record*:

1. **Deterministic, reproducible signals.** Explicit formula/model artifact, source data, indicator variant, lookbacks, smoothing, thresholds, comparisons, state transitions and priority. Fitted/ML signals require pinned model/preprocessing/training cutoff and point-in-time inference inputs. Missing decision-critical rules cannot be guessed.
2. **Unambiguous trade direction.** Long/short intent is explicit or a side is explicitly disabled; market/contract permissions must be realistic.
3. **Complete entry, exit and risk rules.** Entry, signal/opposite exits, SL/TP/trailing/time limits and any intentionally disabled behavior are explicit; no hidden Hummingbot defaults.
4. **Complete position and re-entry state.** Pyramiding, simultaneous exposure, cooldown, size dependencies, safety orders and re-entry/state transitions are explicit or demonstrably irrelevant. Research-designed DCA may change entry/exit events; such an overlay is a **declared derivative/execution experiment**, not automatically event-neutral or source-native.
5. **Demonstrated pinned-engine and data-model compatibility.** Identify the exact Hummingbot package/image/commit and applicable controller/executor, connector, market(s), data feed(s), decision/availability timestamps, fills, costs, leverage/margin and accounting. Demonstrate that **all materially required** multi-asset synchronization/shared capital, lower or multi-timeframe alignment, non-OHLCV point-in-time inputs, next-open/maker/intrabar execution, and real costs can actually be modeled on the *specified* engine path. Unsupported or unverified requirements cannot receive PASS; a documented feature, generic executor name, or one supported interval is insufficient. Missing trade prices must not silently default to fabricated values. The currently verified subset may be narrower than Hummingbot's advertised capabilities. Source-native equivalence is assessed against the source; a disclosed derivative is assessed against **its own fully specified strategy**, not falsely represented as lossless source reproduction. Pin fees/funding/precision and flag unsupported economic terms; do not report hypothetical zero funding as realized funding.
6. **Warmup, point-in-time availability and causality.** Lookbacks/warmup are defined; no repainting, future bars/extrema, negative-shift leakage, full-sample leakage or use of incomplete higher-timeframe candles as completed signals. A signal's decision time must not precede the point when its inputs were available; fill order and same-bar ambiguities need explicit, supported semantics.

**PASS means downstream admission to *model-consistent research*, not profitability, economic realism, guaranteed source-native equivalence, Qlib parity, survivor status or Paper/Testnet/Live permission.** Profitable net-of-fee returns are a later performance/OOS question, **not** an HB_READY admission threshold. Reuse verified engine capabilities; validate a new execution primitive/data requirement once with representative evidence before screening that requires it. This is an engineering capability check, not another strategy admission.

If any of the six requirements is materially incomplete, unverifiable or unsupported by the pinned engine, that strategy MUST NOT merge into `main`, irrespective of PR type. Automated Scout `research/*` PRs are `NOT_LOSSLESS` and closed with exact reasons; non-Scout PRs are left unmerged/commented or preserved on non-main branches. Three status values continue to exist for research **outside** `main`; on `main` every strategy record MUST be PASS. The root-level `strategy-research-record-v1` format is unchanged. No retroactive Survivor upgrade.

## Auto-remediation

Reviewer remediation is allowed only when the missing/corrected fact is explicitly recoverable from a primary source, including:

- public Pine/source code;
- immutable GitHub implementation;
- paper methods / tables / figures;
- official first-party strategy documentation.

Examples of allowed repair:

- omitted indicator length;
- threshold;
- source price;
- timeframe;
- `process_orders_on_close`;
- pyramiding;
- direction;
- source-declared stop/target;
- source-declared transaction-cost assumption.

The reviewer must **not**:

- invent parameters;
- choose among plausible strategy variants;
- add a stop/target/cooldown;
- silently convert next-bar-open into close;
- silently drop required data or market/portfolio dependencies;
- secretly create an adapted strategy from a source-native PR. A deliberate derived strategy must have its own documented specification and provenance, not be made through reviewer auto-remediation.

## Terminal states

### HB_READY: PASS

When the current immutable PR head satisfies every gate:

1. set the record's `hb_ready_status: PASS` and submit a GitHub review comment beginning `HB_READY: PASS`;
2. summarize the source-backed evidence;
3. squash-merge using the exact reviewed head SHA;
4. stop after the confirmed exact-head merge. The **existing signed GitHub Webhook Receiver**, upon receiving this repo's verified merged `pull_request.closed` event, performs deterministic post-merge README bookkeeping: re-fetch the merged PR and current `main` from GitHub, verify every root-level strategy frontmatter is `hb_ready_status: PASS` (excluding the two READMEs), then update **only** the `<!-- HB_READY_POOL_COUNT -->` line using the current README blob SHA. Read back `main` and README to verify; on a concurrent update conflict, re-fetch and retry once. If verification or synchronization fails, log the specific bookkeeping failure without relabeling any strategy or retrying the merge. This is an extension of the current webhook receiver, **not** a new service or admission path.

PASS-count synchronization is post-merge bookkeeping only and must not depend on the Hermes Auditor finishing within its execution timeout. The merge and README update remain separate GitHub commits, so a short-lived count lag alone does **not** imply a non-PASS strategy on `main`. Independently verify strategy frontmatter before diagnosing an admission breach; preserve the existing README-count integrity test. Only the existing webhook receiver performs this bookkeeping, so Hermes must not also write the README after merge. Never create a separate scheduler, reviewer, repair daemon or admission path.

### HB_READY: AUTO_REMEDIATED

When all missing facts are recoverable:

1. submit a review comment beginning `HB_READY: AUTO_REMEDIATED`;
2. modify only the strategy Markdown on the same PR branch;
3. commit as `review: complete HB_READY semantics`;
4. stop; the resulting `synchronize` webhook performs a fresh review of the new head.

### HB_READY: NOT_LOSSLESS

When the declared strategy is materially incomplete, unverifiable, or unsupported by the pinned execution/data model in an automated Scout `research/*` admission PR:

1. submit a review comment beginning `HB_READY: NOT_LOSSLESS`;
2. identify exact blocker(s);
3. close the PR.

This terminal auto-close applies only to automated Scout admission PRs. For non-Scout PRs the reviewer comments on any non-PASS strategy and **MUST NOT approve its merge into `main`**; the record can remain on a PR/non-main branch. No exception based on provenance quality or historical Survivor claims.

Automated Scout strategy PRs must not remain indefinitely in REQUEST_CHANGES.

## Downstream invariant

Every root-level strategy record on `main` MUST have an independently reviewed six-gate `hb_ready_status: PASS`. Historical/non-PASS research remains outside `main` in existing branches, PRs or Git history. The **pinned Hummingbot admission baseline and all six gates above remain unchanged**. `implementation_status` describes strategy-specific engineering artifacts, not admission; `not-implemented` never retroactively revokes a PASS. Do not add `QLIB_READY`, implementation admission, another eligibility flag, a second admission registry or a generic strategy compiler.

**Admission is not executable materialization:** a PASS record does not itself guarantee a Hummingbot controller/executor, reproducible config, data/feed bindings or suitable engine capabilities. If a selected strategy lacks a runnable artifact, record a concrete engineering implementation gap and build/verify the smallest strategy-specific binding. Unsupported or unverified new engine/data capabilities require representative validation before use; this is not a new HB_READY admission gate and must not be mislabeled as strategy rejection. Preserve the strategy's immutable provenance and distinguish any research-derived execution version from its source-native rules.

**Proposed Hummingbot-only downstream campaign (not deployed by this contract):** Hermes selects a PASS strategy and freezes its source/config/data and engine assumptions; using existing Condor/Hummingbot MCP connectivity, it dispatches a Hummingbot backtest, analyzes trade events/equity/cost/risk and records hypotheses, results, revisions and failures in Wiki Brain. A promising but inadequate candidate may undergo one falsifiable change per round, then **Hermes must dispatch it back through MCP to Hummingbot**. Unpromising work stops with recorded reasons; research finalists are frozen before a separate one-time OOS check. Wiki Brain is an evidence-linked research memory, not a replacement for GitHub or OOS discipline. The new engine and MCP path must be verified before any operational claim.

The proposed research campaign uses seven pairs (`BTCUSDT`, `ETHUSDT`, `BNBUSDT`, `SOLUSDT`, `XRPUSDT`, `DOGEUSDT`, `LINKUSDT`), `1h/4h/1d`, isolated Binance USDT-M perpetual and separately modeled `3×/5×`: **42 baseline cells per frozen revision**, not a mandatory HB_READY market/timeframe whitelist or parameter grid. The optional declared DCA experiment uses BO/SO1/SO2 = `6%/6%/6%` of initial capital, max `18%`; it is never an admission prerequisite. DCA or other material changes to original trade events require explicitly identified derived research. Freeze initial capital, data and IS/OOS windows, fees/slippage/funding limitations and fill semantics; missing cells/economic terms must not be treated as valid zeros or successful full coverage.

The former Qlib/MLflow research screening, n8n/Node01–13 routing, dual-engine parity and historical `performance_claimable`/Survivor assertions are **legacy provenance only**, not requirements to rebuild. The historical 10% annualized net return / Sharpe 1.0 screening rule and discussed 8% alternative **do not define an approved new promotion threshold**. Neither is an HB_READY gate or live-trading authorization. Preserve historical evidence without relabeling it as current Hummingbot execution. This documentation-only PR changes no strategy files and deploys nothing.

The existing `hb_ready_status` field alone governs admission: no non-PASS record may merge to `main` through human, maintenance, non-Scout or bot routes. PR #58 remains unmergeable as-is unless each relevant record independently satisfies all six gates. Maintenance/documentation PRs remain COMMENT-only and must not auto-merge. No historical survivor is silently upgraded, and PASS never grants Paper/Testnet/Mainnet execution permission.
