---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Hull-MA/EMA 5-bar crossover two-sided reversal trend system on BTCUSDT 1d bars
created: 2026-10-08
updated: 2026-10-08
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2025-04-30
sources:
  - https://www.fmz.com/strategy/430563
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于HULL-SMA和EMA交叉的趋势策略Trend-Strategy-Based-on-HULL-SMA-and-EMA-Crossover.md
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
---

# Hull-MA/EMA 5-bar crossover two-sided reversal trend system on BTCUSDT 1d bars

## Provenance

Primary source read end to end (FMZ strategy page live plus GitHub mirror cross-check):

- FMZ strategy: https://www.fmz.com/strategy/430563 (`基于HULL-SMA和EMA交叉的趋势策略`, Pine title `HULL EMA Crossover`, `//@version=5`, page author `ChaoZhang`, mirror last-modified 2023-10-30).
- FMZ backtest block pinned on the page: `start: 2022-10-23 00:00:00`, `end: 2023-10-29 00:00:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` — single pair; the `1d` figure is the script decision timeframe adopted as the research frame.
- Live re-verification (2026-10-08): the FMZ page returns HTTP 200 (750,303 bytes); the page title, the `ChaoZhang` author attribution, the full embedded Pine block (`strategy("HULL EMA Crossover", overlay = true, process_orders_on_close = true)`, `HULL_INP = input.int(5, "Hull EMA Value")`, `EMA_INP = input(5, "EMA Value")`, `HULL_EMA = ta.hma(close, HULL_INP)`, `EMA = ta.ema(close, EMA_INP)`, the `ta.crossover` pair, the four `inSession`-gated `strategy.entry`/`strategy.close` lines, the commented EOD block, and the backtest header) all match the mirror line for line. No live-page fact contradicts the mirror.
- Mirror: `fmzquant/strategies` file `基于HULL-SMA和EMA交叉的趋势策略Trend-Strategy-Based-on-HULL-SMA-and-EMA-Crossover.md` at commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30), carrying the same Pine block and a `Detail` link back to FMZ 430563.
- Censuses over the pinned block: `request.*` 0, `security(` 0, `timeframe(` 0, `strategy.exit` 0, `strategy.order` 0, `input.time` 0, `volume` 0, `stop=` 0, `limit=` 0, `profit=` 0, `loss=` 0, `varip` 0, `pyramiding` 0, `calc_on_every_tick` 0. Series read: `close` only (`time` is read solely inside the commented-out EOD block, which never executes). `plot` lines never execute trading logic.

Licence and rights: the pinned block carries an MPL-2.0 header (`© spiritedPerson95700`). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-08): working-tree searches for `430563`, `spiritedPerson`, and `HULL EMA Crossover` return 0 strategy records; `ta.hma` matches only the `flying-dragon-offset-ma-band-trend-btcusdt-1d-2026-10-06.md` signal (`ta.hma(close, 35)` with 4/6-bar historical offsets, close-vs-lagged-level band system, `pyramiding=3`) and passing mentions inside the EHMA dedup prose. Open `research/*` PRs: only #48 (Larry Williams 3-EMA channel streak long, FMZ 451075) and #49 (Gaussian channel StochRSI-gated breakout long, FMZ 482888) plus the non-Scout #36 (QuantaAlpha price-volume family) — different mechanisms, indicators, and sources. Closed Scout PRs #6 (WaveTrend tie semantics), #10 (golden/dead cross, FMZ 435513), #17 (MACD histogram, FMZ 433919), #20 (Ichimoku-RSI, FMZ 427447) concern different constructions and sources. Closest pool records are different mechanism classes: `ehma-range-band-breakout-btcusdt-1d-2026-10-05.md` (custom borserman exponential-Hull recursion with a symmetric ±2% envelope, strict close-vs-band inequalities, 0 crossover calls), `flying-dragon-offset-ma-band-trend-btcusdt-1d-2026-10-06.md` (close versus 6-bar-lagged HMA(35) level, offset band system), `ema-20-50-cross-btcusdt-1h-2026-10-06.md` (bare EMA-vs-EMA single cross, long-only, window-gated, `1h`), `ema-cloud-7-20-trend-btcusdt-1d-2026-10-07.md` (close-vs-fast plus fast-vs-slow alignment conjunctions, 0 crossover calls), `triple-ema-volstop-tp-long-btcusdt-1d-2026-10-08.md` (triple-EMA simultaneous-cross conjunction with dual-leg OR exit and vol-stop), `rsi-ma-crossover-reversal-btcusdt-1d-2026-10-07.md` (RSI crossing its own SMA, oscillator-vs-average). Five-axis distinction: mechanism differs (contemporaneous fast-Hull-vs-slow-EMA cross with immediate two-sided reversal), signal construction differs (`ta.crossover(HULL_EMA, EMA)` / `ta.crossover(EMA, HULL_EMA)` on `ta.hma(close, 5)` versus `ta.ema(close, 5)` — no band, no offset, no oscillator, no third average), exits differ (explicit close plus opposite-side entry on the same cross bar, no stop/limit/time leg), horizon is `1d` BTCUSDT, source identity differs (FMZ 430563, `ChaoZhang`).

## Economic mechanism

### Source-reported

A medium-term two-way trend system: Hull smoothed MA (length 5) is the fast line, EMA (length 5) the slow line; a fast-over-slow cross opens long, a slow-over-fast cross closes the long and opens short, so the system rides whichever side the micro-trend points to and reverses on the turn.

### Research interpretation

Pure two-average cross reversal with no filter and no risk leg. The Hull MA reacts faster than the same-length EMA by construction (weighted averages plus square-root length), so the cross fires on micro-trend turns while the EMA leg smooths chop. Both legs are live at all times (`inSession` is hardcoded `true`); the system is always positioned after its first cross except on the exact bars where both series are `na`. No leverage, sizing, or cost edge is embedded in the signal; the declaration carries no capital/accounting lines at all, so the house overlay supplies them event-neutrally (see Execution assumptions).

## Signal

Exact rule as pinned (Pine v5, defaults quoted — inputs unmodified):

- Declaration: `strategy("HULL EMA Crossover", overlay = true, process_orders_on_close = true)`. `calc_on_every_tick` is unset (default false).
- Inputs: `HULL_INP = input.int(5, "Hull EMA Value")`, `EMA_INP = input(5, "EMA Value")` (untyped `input(5, …)` takes the int default). Session gate `inSession = true` hardcoded — provably always-true.
- Averages: `HULL_EMA = ta.hma(close, HULL_INP)` on `close`; `EMA = ta.ema(close, EMA_INP)` on `close`. First-party deterministic builtins, no variant/smoothing/source choice left open; divisor paths are positive weight-sum constants, so no data-dependent zero-divisor exists anywhere in the chain.
- Crosses (strict v5 semantics — a tie on either bar fires neither leg, see Negative evidence): `buy = ta.crossover(HULL_EMA, EMA)`; `short = ta.crossover(EMA, HULL_EMA)`; aliases `sell = short`, `cover = buy`.
- Long leg: `strategy.entry("long", direction = strategy.long, comment = "Buy")` when `buy`; `strategy.close("long", comment = "Sell")` when `sell`.
- Short leg: `strategy.entry("short", direction = strategy.short, comment = "Short")` when `short`; `strategy.close("short", comment = "Cover")` when `cover`.
- Direction: two-sided. Both entries are explicit; neither side is disabled.
- Stop-loss / take-profit / trailing / time limit: explicitly none (0 `strategy.exit`, 0 `stop=`/`limit=`/`profit=`/`loss=`, commented EOD block never executes, no time-limit construct). Opposite-signal reversal is the sole exit path.
- Inert code, provably excluded: `prevSignal` (write-only for order logic — assigned but never read by any `when`/order condition; the opening `if (prevSignal == '')` seeds it once and no decision references it), the commented EOD block (`hour(time)`/`minute(time)` conditions, dead assignments), `overlay`/`comment` cosmetics, and both `plot` lines.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (both averages, both crosses). No `open`, no `high`/`low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any executable line.
- Single decision timeframe `1d` (backtest `period: 1d`). `basePeriod: 1h` is FMZ demo-execution granularity; with 0 intrabar orders and close-gated evaluation it cannot alter any admitted event.
- Warmup: longest live window is 5 bars (`ta.hma(close, 5)` inner `wma(·, 5)`; `ta.ema(close, 5)`); the `crossover` prior-bar reference needs one further bar. First fully-defined evaluation at 6 completed `1d` bars; no signal is evaluable before that. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (source venue is Binance USDT-M BTC futures; the house overlay runs Isolated futures at 3×/5×, two-sided for this record since both directions are coded — no naked-spot construction needed).
- Order timing: all four live order calls run under `process_orders_on_close = true`: completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. `calc_on_every_tick` is unset (default false). No next-bar-open, maker-touch, queue, or intrabar-path-dependent fill.
- Sizing/capital: the declaration sets no quantity, capital, commission, slippage, or margin lines — pure event-neutral absence, replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3×/5×) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (Pine v5 language default: no additional same-direction entry while positioned — the same default-convergence earlier PASS reviews accepted). The default is provably moot here beyond the language rule: strict-cross construction makes a second same-side cross impossible while holding that side without an intervening opposite cross, and the opposite cross always closes and reverses first. Single engine position; re-entry is allowed immediately after any close whenever the cross conjunction fires again (no cooldown specified — explicitly none, not invented). No shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The FMZ page and mirror ship one backtest-chart image with no numeric caption — no ROI, Sharpe, win rate, drawdown, or trade-count figures are cited anywhere in this record. The prose makes only qualitative claims (earlier trend detection, whipsaw/false-signal warnings, parameter-sensitivity cautions) plus its own risk disclosures. The live page carries no numeric performance for this strategy (the only `收益`-family hits on the page are site-chrome and unrelated-strategy text). Recorded as an explicit gap, not filled: this record claims no source-reported performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Flat-book determinism: with no open position both `strategy.close` legs are deterministic no-ops; only a genuine cross can open.
2. Same-bar mutual exclusivity is proven, not assumed: `buy` needs `HULL_EMA[t-1] <= EMA[t-1]` with `HULL_EMA[t] > EMA[t]`; `short` needs the mirror. Both can never hold on one bar (exact prior-bar equality admits at most one strict current-bar inequality; `na` on either series makes both false). Entry and exit therefore never co-fire — no call-order priority is required.
3. Boundary ties are defined: `HULL_EMA == EMA` on either compared bar fires neither `ta.crossover` leg (strict v5 semantics) — the tie case holds position, it never invents an order.
4. Same-side re-adds are unreachable while holding that side: a second `buy` cross requires an intervening bar with `HULL_EMA <= EMA`, but any bar printing the reverse cross fires `sell`/`short` first — the position is always closed and reversed before a same-side signal can recur.
5. The dead state is pinned, not removed: flipping `HULL_INP`, `EMA_INP`, or `inSession`, or reviving the commented EOD block, would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `ta.hma(close, 5)` versus `ta.ema(close, 5)` contemporaneous cross, two-sided immediate reversal, `1d` BTCUSDT, same-bar-close fills are frozen.

- F1 — Smoother relevance: replacing `ta.hma(close, 5)` with `ta.sma(close, 5)` (same length, different smoother, exit logic kept) must not improve net expectancy; fail ⇒ the Hull construction adds nothing over a plain average.
- F2 — Exit relevance: replacing the opposite-cross close-plus-reverse with a fixed 20-bar time exit (entries kept, no short leg) must not improve net expectancy; fail ⇒ the reversal exit leg is decorative.
- F3 — Parameter sensitivity: the (5, 5) set must not be dominated net of costs by both the (3, 3) and (10, 10) neighbor sets; fail on both sides ⇒ the set choice is arbitrary rather than structural.
- F4 — Short-leg relevance: the two-sided rule must beat its long-only ablation (short entries and short closes removed, long leg kept) net of costs; fail ⇒ the short side earns no keep and the system is a long system wearing a two-sided costume.

## Crypto portability

Pinned to BTCUSDT (Binance USDT-M lineage) under the house overlay. The close-derived two-sided logic ports to perps without structural change; no funding-dependent leg, no stablecoin-specific assumption, no cross-venue state. Spot deployment would require dropping the short leg, which is a different, unpinned rule — not admitted here.

## Limitations

- No adverse-stop protection: exits print only on the reverse cross, so an adverse drift that never crosses back is ridden indefinitely; on `1d` bars gap risk is fully retained. The source's own risk section concedes whipsaw losses and weak-trend bleed.
- Micro-cross frequency: two 5-bar averages on daily bars re-cross often in range-bound chop; every cross turns the full position, so sideways regimes grind through costs by construction.
- Fixed symmetric speeds: both legs share length 5, so the system cannot separate fast-trigger from slow-confirmation regimes — trend strength is unmeasured by design.
- Source demo window is about one year (2022-10-23 → 2023-10-29); full-history behavior is unreported by the source and unclaimed here.
- Single-exchange lineage: the rule reads only closes, but the pinned demo venue is Binance USDT-M BTC futures; other venues' closes are an untested substitution.

## Implementation status

- `implementation_status: not-implemented`.
- Normalized rule is fully specified above; no Hummingbot/Qlib/n8n/survivor/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`, `status: research-only`.
- This record is semantic normalization only. It is not profitability validation, not a survivor promotion, and not Paper/Testnet/Mainnet authorization. Only `hb_ready_status: PASS` records may enter the current Hummingbot/Qlib performance-research downstream, subject to that workflow's own gates.

## Related Wiki records

None.

## Sources

- Primary: https://www.fmz.com/strategy/430563 (live page re-verified 2026-10-08, HTTP 200, 750,303 bytes; backtest block 2022-10-23 → 2023-10-29, `period: 1d`, Binance USDT-M BTC).
- Mirror: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于HULL-SMA和EMA交叉的趋势策略Trend-Strategy-Based-on-HULL-SMA-and-EMA-Crossover.md (same Pine block line for line, links back to FMZ 430563; commit date 2025-04-30).
- Pine `strategy()` declaration semantics (first-party reference): https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- Strategy execution model (broker emulator, `process_orders_on_close`): https://www.tradingview.com/pine-script-docs/concepts/strategies/
