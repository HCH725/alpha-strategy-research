---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Triple-EMA simultaneous-breakout long with ATR vol-stop and fixed take-profit on BTCUSDT 1d bars
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
  - https://www.fmz.com/strategy/435972
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/三重EMA趋势跟踪策略Triple-EMA-Trend-Following-Strategy.md
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The FMZ page prose claims the system opens long positions when price crosses above all three EMAs and short positions when price crosses below all three, but the pinned Pine block contains exactly one live entry (`strategy.entry(id=\"long\", long = true, ...)`) and zero short entries. The admitted rule pins the code: long-only, short side disabled. The prose short side is recorded as a source-internal contradiction, not repaired."
  - "The FMZ page prose describes the three EMAs as 7-, 14- and 21-period, but the pinned Pine block wires `ema_2 = ema(close, input(12))`. The admitted rule pins the code value 12. The prose figure 14 is recorded as a source-internal contradiction, not repaired."
---

# Triple-EMA simultaneous-breakout long with ATR vol-stop and fixed take-profit on BTCUSDT 1d bars

## Provenance

Primary source read end to end (FMZ strategy page live plus GitHub mirror cross-check):

- FMZ strategy: https://www.fmz.com/strategy/435972 (`三重EMA趋势跟踪策略|Triple EMA Trend Following Strategy`, Pine title `Three EMAs Trend-following Strategy (by Coinrule)`, `//@version=4`, author `ChaoZhang`).
- FMZ backtest block pinned on the page: `start: 2023-01-01 00:00:00`, `end: 2023-06-16 00:00:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` — single pair; the `1d` figure is the script decision timeframe adopted as the research frame.
- Live re-verification (2026-10-08): the FMZ page returns HTTP 200 (800,578 bytes); the page title, the `ChaoZhang` author line, `process_orders_on_close=true`, the exact declaration (`strategy(shorttitle='Three EMAs Trend-following Strategy',title='Three EMAs Trend-following Strategy (by Coinrule)', overlay=true, initial_capital = 1000, process_orders_on_close=true, ...)`), the single entry line (`strategy.entry(id="long", long = true, when = go_long and window())`), the single exit line (`strategy.close("long", when = closeLong and window())`), and the backtest header all match the mirror. No live-page fact contradicts the mirror.
- Mirror: `fmzquant/strategies` file `三重EMA趋势跟踪策略Triple-EMA-Trend-Following-Strategy.md` at commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30), carrying the same Pine block and a `Detail` link back to FMZ 435972.
- Censuses over the pinned block: `request.*` 0, `security(` 0, `timeframe(` 0, `strategy.exit` 0, `strategy.order` 0, `input.time` 0, `volume` 0. Series read: `close`, `high`, `low` (via `tr`/`atr`), and `time` (only inside the provably always-true `window()` gate below). `plot` lines never execute trading logic.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-08): working-tree searches for `435972`, `Three EMAs`, `triple-ema`, `volStop`, and `vStop` return 0 strategy records — no triple-EMA mechanism exists on `main`. Open `research/*` PRs: only #48 (Larry Williams 3-EMA channel streak long) and #49 (Gaussian channel StochRSI-gated breakout long) — different mechanisms, indicators, and sources. Closest records are different mechanism classes: `ema-20-50-cross-btcusdt-1h-2026-10-06.md` (dual EMA-vs-EMA cross), `ema-cloud-7-20-trend-btcusdt-1d-2026-10-07.md` (dual-EMA cloud), `dual-ema-engulfing-volume-long-btcusdt-1h-2026-10-07.md` (dual EMA plus engulfing plus volume). Five-axis distinction: mechanism differs (simultaneous price-over-three-EMAs breakout conjunction plus ATR volatility trailing stop plus fixed-percentage take-profit, versus EMA-vs-EMA crosses), signal construction differs (triple `crossover(close, ema_N)` conjunction on lengths 7/12/21 versus two-EMA relational crosses), exits differ (close-evaluated 4% level plus `crossunder(close, vStop)` versus opposite-signal reversal), horizon is `1d` BTCUSDT, source identity differs (FMZ 435972, `ChaoZhang`).

## Economic mechanism

### Source-reported

A long-only trend-following system: it waits until price confirms strength by crossing above three EMAs (7, 12, 21 per the code) on the same bar — filtering weak drifts that clear only the fast average — then rides the leg under an ATR-anchored volatility stop that trails new highs, capped by a fixed 4% take-profit.

### Research interpretation

Triple-conjunction breakout entry with a two-legged close-evaluated hold: the entry demands same-bar confirmation across all three averages, so single-EMA whipsaws cannot trigger it. The hold pairs a volatility-adaptive trailing level (`vStop`, ATR length 20 × 3.0 on `close`) with a fixed 4% level off the position average price. Both exits are completed-bar-close comparisons — there are 0 `strategy.exit` calls, hence no stop/limit order, no intrabar touch fill, and no same-bar TP/SL ordering ambiguity. No leverage, sizing, or cost edge is embedded in the signal; the source `initial_capital`/`default_qty_*`/`commission_*` lines are capital configuration replaced event-neutrally by the house overlay (see Execution assumptions).

## Signal

Exact rule as pinned (Pine v4, defaults quoted — inputs unmodified):

- Inputs: EMA lengths 7/12/21 on `close` (v4 built-in `ema()`); `Take_profit = 4` (percent, divided by 100); volStop `length = 20`, `factor = 3.0`, `src = close`; `window()` date gate defaults `2020-01-01` → `2112-12-31`.
- Averages: `ema_1 = ema(close, 7)`, `ema_2 = ema(close, 12)`, `ema_3 = ema(close, 21)`. Pinned at 12 for the middle leg per the code (see Contradictions).
- Volatility stop (exact recursion as written): `atrM = nz(atr(atrlen) * atrfactor, tr)`; `max`/`min` track running extremes of `src`; `stop := nz(uptrend ? max(stop, max - atrM) : min(stop, min + atrM), src)`; `uptrend := src - stop >= 0.0`; on regime flip (`uptrend != nz(uptrend[1], true)`) reset `max/min := src` and `stop := uptrend ? max - atrM : min + atrM`. Returns `[vStop, uptrend]`; only `vStop` is read by any exit.
- Entry long: `go_long = crossover(close, ema_1) and crossover(close, ema_2) and crossover(close, ema_3)`, live via `strategy.entry(id="long", long = true, when = go_long and window())`. All three `crossover` calls carry strict prior-bar semantics (prior bar `close <= ema`, current bar `close > ema`); equality on either side fires nothing.
- Take-profit level: `longTakeProfit = strategy.position_avg_price * (1 + 0.04)`.
- Exit long: `closeLong = close > longTakeProfit or crossunder(close, vStop)`, live via `strategy.close("long", when = closeLong and window())`. Both legs are completed-bar-close comparisons — no stop/limit order exists anywhere in the rule.
- Direction: long-only. Zero short entries exist in the pinned block; the short side is explicitly disabled (no short rule to implement). The prose short side is excluded as contradiction, not admitted.
- Stop-loss / trailing-stop *orders* / time limit / opposite-signal exit: explicitly none (0 `strategy.exit`, 0 `stop=`/`limit=`, no short side, no time-limit construct). The ATR trailing *level* above is a close-evaluated exit condition, recorded as what it is — not as a stop order.
- Date gate: `window() => time >= start and time <= finish` with defaults spanning 2020-01-01 to 2112-12-31 — provably always-true over the source demo window and any full-history backtest under pinned defaults. Altering the inputs would be a different, unpinned rule.
- Inert code, provably excluded: `uptrend` (second tuple element) is computed but read zero times outside the function; `showDate`, `start`/`finish` display inputs and all `plot` lines never touch order logic.

## Required data

- Completed `1d` bars of BTCUSDT: `close` (averages, crosses, TP level), `high`/`low` (only inside `tr`/`atr` for the volatility stop), and `time` (only for the always-true `window()` gate). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read.
- Single decision timeframe `1d` (backtest `period: 1d`). `basePeriod: 1h` is FMZ demo-execution granularity; with 0 intrabar orders and close-gated evaluation it cannot alter any admitted event.
- Warmup: longest lookback is 21 bars (EMA-21); ATR(20) is fully defined at 20 bars and the `uptrend[1]` regime reference needs one further bar. First fully-defined evaluation at 21 completed `1d` bars; no signal is evaluable before that. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (source venue is Binance USDT-M BTC futures; the house overlay runs Isolated futures at 3×/5×, long-only for this record since the short side is disabled as coded — no naked-spot construction needed).
- Order timing: both live order calls run under `process_orders_on_close = true`: completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. `calc_on_every_tick` is unset (default false). No next-bar-open, maker-touch, queue, or intrabar-path-dependent fill.
- Sizing/capital: `initial_capital = 1000`, `default_qty_type = strategy.percent_of_equity`, `default_qty_value = 100`, and `commission_type/commission_value = 0.1%` are event-neutral capital/accounting configuration, replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3×/5×) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (Pine v4 default: no additional same-direction entry while the single `long` position is held). At most one open long; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The FMZ page ships a backtest-chart image with no numeric caption — no ROI, Sharpe, win rate, drawdown, or trade-count figures are cited anywhere in this record. Recorded as an explicit gap, not filled: this record claims no source-reported performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Flat-book determinism: with no open position `strategy.position_avg_price` is `na`, so `close > longTakeProfit` is `na` (false) — the TP leg cannot fire flat; only a genuine triple cross can open.
2. Boundary ties are defined: any `close == ema_N` equality fails that leg's strict `crossover`; `close == vStop` fails the strict `crossunder`; `src - stop == 0` keeps `uptrend` true by the `>=` rule.
3. Same-bar entry/exit co-fire resolves deterministically at the single close price (open-and-flat at one price, no P&L): on the entry bar `strategy.position_avg_price` equals the fill (the same close), so `close > avg * 1.04` is false and only a simultaneous `crossunder(close, vStop)` could also close — and with 0 `strategy.exit` calls there is no stop/limit ordering question for the reviewer to rule on.
4. Early-bar `nz()` fallbacks (`atr` → `tr`, `uptrend[1]` → `true`, `stop` → `src`) are coded deterministic values, not reviewer inventions.
5. Enabling the prose short side, the prose 14-period middle EMA, or any non-default input would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: EMA set (7, 12, 21) on `close`, simultaneous-cross conjunction, volStop(20, 3.0), 4% TP, long-only, `1d` BTCUSDT, same-bar-close fills are frozen.

- F1 — Triple-conjunction relevance: replacing `go_long` with a single `crossover(close, ema(close, 12))` must not improve net expectancy; fail ⇒ the triple gate adds nothing.
- F2 — Exit relevance: replacing the `vStop` leg with a fixed 30-bar time exit (TP leg kept) must not improve net expectancy; fail ⇒ the volatility-trailing leg is decorative.
- F3 — TP relevance: removing the 4% TP leg (volStop exit only) must not improve net expectancy; fail ⇒ the fixed TP leg is decorative.
- F4 — Parameter sensitivity: the (7, 12, 21) set must not be dominated net of costs by both the (5, 10, 20) and (9, 15, 30) neighbor sets; fail on both sides ⇒ the set choice is arbitrary rather than structural.

## Crypto portability

Pinned to BTCUSDT (Binance USDT-M lineage) under the house overlay. The long-only close-derived logic ports to perps without structural change; no funding-dependent leg, no stablecoin-specific assumption, no cross-venue state. Spot deployment needs no modification for the long side (no shorting required).

## Limitations

- No adverse-gap protection: both exits evaluate at the completed daily close, so a vertical adverse move exits only at the next `1d` close — gap risk is fully retained, and on `1d` bars gaps can be large.
- Fixed 4% TP caps every winner at 4% above average entry regardless of trend strength; in one-sided trends this truncates the right tail by construction — the record pins the value as written rather than "fixing" it.
- Triple-simultaneous-cross entries are rare by design; long droughts with zero exposure are the normal state, not a malfunction.
- Whipsaw regime: in range-bound chop, price can pierce all three tightly-clustered EMAs on the same bar and reverse the next day; the conjunction attenuates but cannot eliminate this.
- Source demo window is under six months (2023-01-01 → 2023-06-16); full-history behavior is unreported by the source and unclaimed here.
- FMZ prose advertises a short side and 14-period middle EMA that the code does not implement; anyone deploying on prose alone would trade a different system.

## Implementation status

- `implementation_status: not-implemented`.
- Normalized rule is fully specified above; no Hummingbot/Qlib/n8n/survivor/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`, `status: research-only`.
- This record is semantic normalization only. It is not profitability validation, not a survivor promotion, and not Paper/Testnet/Mainnet authorization. Only `hb_ready_status: PASS` records may enter the current Hummingbot/Qlib performance-research downstream, subject to that workflow's own gates.

## Related Wiki records

None.

## Sources

- Primary: https://www.fmz.com/strategy/435972 (live page re-verified 2026-10-08, HTTP 200, 800,578 bytes; backtest block 2023-01-01 → 2023-06-16, `period: 1d`, Binance USDT-M BTC).
- Mirror: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/三重EMA趋势跟踪策略Triple-EMA-Trend-Following-Strategy.md (same Pine block, links back to FMZ 435972; commit date 2025-04-30).
- Pine `strategy()` declaration semantics (first-party reference): https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- Strategy execution model (broker emulator, `process_orders_on_close`): https://www.tradingview.com/pine-script-docs/concepts/strategies/
