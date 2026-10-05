# LOSSLESS HB_READY GitHub Review Contract

Effective: 2026-10-06 (UTC+8)

This file defines the automated GitHub PR admission gate for new strategy records in `HCH725/alpha-strategy-research`.

## Scope

This review answers one question only:

> Can the source core strategy's signal and causal trade-event semantics be reconstructed without material approximation and evaluated by the pinned Hummingbot backtester under the same explicitly labeled house overlay?

Pinned baseline:

- Hummingbot package: `20260920`
- Hummingbot VERSION: `dev-2.17.0`

A strategy merged to `main` is therefore already considered **LOSSLESS HB_READY**. This is semantic/backtest expressibility only; it is not profitability validation, survivor promotion, Paper/Testnet/Live approval, or trading authorization.

## Strategy PR shape

Automated strategy PRs must:

- target `main`;
- originate from the same repository;
- use a head branch beginning with `research/`;
- add exactly one root-level strategy Markdown record;
- contain no unrelated modifications.

Maintenance/documentation/config PRs are ordinary review PRs and are never auto-merged or auto-closed by this strategy-admission policy.

## Hard admission requirements

Every applicable item must be explicit and source-faithful:

1. **Market structure**
   - single trading pair per run;
   - preserve source market/contract identity when it changes signal data, bars, timing, direction, or source applicability; otherwise, the house overlay may choose an explicitly labeled research market;
   - no cross-sectional ranking, pair spread, shared portfolio capital, portfolio rebalance, or multi-pair shared state;
   - spot cannot require naked shorting.

2. **Timeframe**
   - exactly one decision timeframe: `1h`, `4h`, or `1d`;
   - multi-timeframe strategies are rejected unless exact causal alignment is demonstrably lossless under the pinned engine.

3. **Data**
   - core signal uses OHLCV and deterministic causal candle-derived indicators only;
   - reject required funding, OI, mark/index price, liquidation feed, trade/aggressor feed, L2/order book, on-chain, options/Greeks, sentiment/news, macro, cross-venue state, or other unsupported external state.

4. **Signal determinism**
   - exact formula/indicator variant;
   - source price;
   - lookback;
   - smoothing method;
   - thresholds;
   - comparison/crossover semantics;
   - AND/OR/state-transition logic;
   - conflict priority.

5. **Direction**
   - long and short rules explicit, or one side explicitly disabled.

6. **Entry / exit / risk**
   - exact entry;
   - signal exit / opposite-signal exit;
   - SL / TP / trailing / time limit / no-exit semantics;
   - every applicable field explicit or explicitly none/disabled;
   - no silent Hummingbot defaults.

7. **Execution timing**
   - compatible with completed-bar decision + same-bar-close execution;
   - next-bar-open, maker-touch/queue, or intrabar-path-dependent strategies are NOT_LOSSLESS.

8. **Position / re-entry / gating**
   - pyramiding / repeated-entry, max same-side concurrency, cooldown, re-entry, and position-aware state must be explicit or provably irrelevant whenever they can change the trade-event sequence, timing, direction, or exits;
   - source sizing and fixed-vs-compounding behavior may be replaced by the house overlay only when event-neutral;
   - the overlay must not invent missing signal, entry, exit, or re-entry rules.

9. **Cost / engine-model compatibility**
   - maker/taker asymmetry, spread capture, queue position, partial fills, unsupported slippage/impact, funding, margin, liquidation, or leverage are hard gates when the strategy edge or event logic materially depends on behavior the pinned backtester cannot model losslessly;
   - pure PnL/accounting costs may be normalized using pinned house assumptions when they do not materially affect the strategy edge or event logic;
   - the overlay must not substitute a different price series when source contract identity is material.

10. **Warmup / causality**
    - all lookbacks known so warmup can be derived;
    - no repainting, future reference, negative shift, future extrema, full-sample normalization, or look-ahead leakage.

Any material approximation, unresolved source interpretation, or invented source-core signal or trade-event rule means **NOT_LOSSLESS**. The house overlay must never invent missing signal, entry, exit, or re-entry rules, or substitute a different price series when contract identity is material.

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
- convert next-bar-open into close;
- remove a material data dependency;
- alter the strategy to fit Hummingbot.

## Terminal states

### HB_READY: PASS

When the current immutable PR head satisfies every gate:

1. submit a GitHub review comment beginning `HB_READY: PASS`;
2. summarize the source-backed evidence;
3. squash-merge using the exact reviewed head SHA;
4. after the merge succeeds, re-read current `main`, count root-level strategy Markdown records (exclude `README.md` and `README.zh-TW.md`), and update only the `<!-- HB_READY_POOL_COUNT -->` line in `README.md` to that exact count.

The pool-count synchronization is post-merge bookkeeping only. It must never affect HB_READY admission, alter a strategy record, or create a second review/control path.

### HB_READY: AUTO_REMEDIATED

When all missing facts are recoverable:

1. submit a review comment beginning `HB_READY: AUTO_REMEDIATED`;
2. modify only the strategy Markdown on the same PR branch;
3. commit as `review: complete HB_READY semantics`;
4. stop; the resulting `synchronize` webhook performs a fresh review of the new head.

### HB_READY: NOT_LOSSLESS

When the source is materially underspecified or incompatible:

1. submit a review comment beginning `HB_READY: NOT_LOSSLESS`;
2. identify exact blocker(s);
3. close the PR.

Automated strategy PRs must not remain indefinitely in REQUEST_CHANGES.

## Downstream invariant

HB_READY admission remains a source-semantics gate: the source strategy's core signal and causal trade-event semantics—including timing, direction, entries, exits, and any event-affecting position behavior—must be reconstructed without material approximation. Source sizing or fixed-vs-compounding behavior may be replaced only when event-neutral under the house overlay.

After admission, the performance-research workflow applies one explicit **house execution overlay** to every strategy:

- Base Order = 6% of initial capital;
- Safety Order 1 = 6%;
- Safety Order 2 = 6%;
- Isolated margin;
- 3× and 5× leverage tested separately;
- DCA spacing and strategy parameters are research-defined before final OOS evaluation.

This overlay is intentionally not source-native semantics and must never be presented as such. It may replace event-neutral source sizing, capital, leverage, and pure accounting assumptions, but must not invent missing signal, entry, exit, or re-entry rules or substitute a different price series when source contract identity is material.

Hummingbot is the canonical benchmark engine. Qlib may be used for large-scale screening only after the two engines demonstrate event-level parity on the same source core strategy, data, house overlay, and pinned assumptions—not source-native sizing. Matching only final performance metrics is insufficient: signal time, entry/exit time, direction, price, position size under the same overlay, Safety Orders and close transitions must match trade by trade.

There is no second semantic suitability gate after merge. A future Survivor Repo is a performance-promotion output, not another HB_READY admission layer.
