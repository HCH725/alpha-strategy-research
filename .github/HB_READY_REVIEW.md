# HB_READY GitHub Review Contract — Six-Gate Engine Capability

Effective: 2026-10-08 (UTC+8)

This file defines the automated GitHub PR admission gate for scheduled Scout strategy records in `HCH725/alpha-strategy-research`; it does not gate every strategy record preserved in the corpus.

## Scope

This review answers one question only:

> Is this specific, fully declared source-native or explicitly derived strategy causally reproducible and actually expressible by the pinned Hummingbot backtest model, with no hidden execution or data assumptions?

Pinned baseline:

- Hummingbot package: `20260920`
- Hummingbot VERSION: `dev-2.17.0`

`main` is the canonical strategy-research corpus, not a PASS-only pool. A root-level strategy record represents normalized, source-backed research; presence on `main` alone does not imply HB_READY. Each record's `hb_ready_status` is `PASS`, `NOT_LOSSLESS`, or `NOT_ASSESSED`; only `PASS` is eligible for current Hummingbot/Qlib performance-research downstream. PASS is semantic/backtest expressibility only, not profitability validation, survivor promotion, Paper/Testnet/Live approval, or trading authorization.

## Strategy PR shape

Automated Scout admission PRs must:

- target `main`;
- originate from the same repository;
- use a head branch beginning with `research/`;
- add exactly one root-level strategy Markdown record;
- contain no unrelated modifications.

They must receive `hb_ready_status: PASS` to merge through this lane; a `NOT_LOSSLESS` candidate is closed.

Non-Scout reconstructed/legacy research records use a non-`research/*` branch (for example `reconstruction/*` or `maintenance/*`) and receive independent provenance/research review. They may merge as `NOT_LOSSLESS` or `NOT_ASSESSED`, remain ordinary root-level strategy records, and must not be auto-consumed downstream. This branch distinction is process-only and creates no content class, folder, or tag. Maintenance/documentation/config PRs are also ordinary review PRs and are never auto-merged or auto-closed by the Scout admission policy.

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

**PASS means admissible to *model-consistent research*, not profitability, economic realism, guaranteed source-native equivalence, Qlib parity, survivor status or Paper/Testnet/Live permission.** Profitable net-of-fee returns are a later performance/OOS question, **not** an HB_READY admission threshold. For new execution/data paths, pin the evidence and verify representative event-level Qlib/Hummingbot parity **before Qlib mass screening**, not before preserving a strategy record.

If any of the six requirements is materially incomplete, unverifiable or unsupported by the pinned engine, the automated Scout `research/*` PR is `NOT_LOSSLESS` and closed with the specific remaining blocker. Non-Scout research may still be preserved on `main` with `NOT_LOSSLESS` or `NOT_ASSESSED` after independent review. The existing status values and root-level `strategy-research-record-v1` format remain unchanged. Neither historical Survivor evidence nor removal of four bans retroactively upgrades a record to PASS.

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
4. after the merge succeeds, re-read current `main`, count root-level strategy records whose frontmatter says `hb_ready_status: PASS` (exclude `README.md` and `README.zh-TW.md`), and update only the `<!-- HB_READY_POOL_COUNT -->` line in `README.md` to that exact PASS count.

The PASS-count synchronization is post-merge bookkeeping only. It must never affect HB_READY admission, alter a strategy record, or create a second review/control path.

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

This terminal auto-close applies only to automated Scout admission PRs. It does not discard or prohibit ordinary non-Scout `NOT_LOSSLESS` research records that pass independent provenance/research review.

Automated Scout strategy PRs must not remain indefinitely in REQUEST_CHANGES.

## Downstream invariant

Only `hb_ready_status: PASS` strategies may enter current Hummingbot/Qlib performance research; research preservation on `main` is independent. Pinned Hummingbot backtesting is the model benchmark. Qlib mass screening requires representative event-level parity on the exact activated strategy, data, execution assumptions and engine route, not a matching Sharpe/MDD alone. An admission PASS by itself does not prove such parity or live economics.

The current **research campaign** optionally applies the declared house BO=6%, SO1=6%, SO2=6%, isolated 3×/5× and research-defined DCA spacing. These are downstream experiment settings, **not HB_READY source requirements**. If DCA, sizing, direction, risk or event timing changes a source strategy, record the execution as a separate, explicitly derived strategy with its own evidence, not as an event-neutral or source-native overlay. Do not claim that a path with unverified funding, fills, margin or causality is model-compatible merely because the Hummingbot API accepts a config.

The existing status field alone governs selection; do not add a second admission registry. Never upgrade old evidence automatically, change historical PR #58 status, deploy Qlib/Hummingbot or interpret PASS as trading authorization.