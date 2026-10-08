---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Cumulative-RSI dual-threshold breakout long with close-only exits on BTCUSDT 1h bars
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
  - https://www.fmz.com/strategy/430328
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/累积RSI突破策略Cumulative-RSI-Breakout-Strategy.md
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The FMZ page prose (both Chinese and English) describes the signal as the cumulative RSI crossing Bollinger-Band rails computed from years of history ('上穿布林带上轨' / 'crosses above the Bollinger Band upper rail'). The pinned Pine block contains zero Bollinger calls and no rolling-band construction; entry and exit are fixed-threshold crossovers of cumRSI through 60 and 282. The admitted rule pins the code; the Bollinger description is recorded as a source-internal contradiction, not repaired."
  - "The FMZ prose describes the exit as the indicator crossing below the lower rail ('下穿下轨平仓' / close on cross below). The pinned code exits only on an upward crossover, ta.crossover(cumRSI, ob=282). The admitted rule pins the code direction; the prose exit direction is recorded as a source-internal contradiction, not repaired."
  - "The Strategy Arguments table labels the 94 input 'Oversold Level' and the 20 input 'Overbought Level', but the code feeds 94 into the upper exit threshold (ob = 282) and 20 into the lower entry threshold (os = 60). The admitted rule pins numeric semantics (entry = rise through 60, exit = rise through 282); the English labels are recorded as swapped, not repaired."
---

# Cumulative-RSI dual-threshold breakout long with close-only exits on BTCUSDT 1h bars

## Provenance

Primary source read end to end (FMZ strategy page live plus GitHub mirror cross-check):

- FMZ strategy: https://www.fmz.com/strategy/430328 (`累积RSI突破策略Cumulative-RSI-Breakout-Strategy`, Pine title `Cumulative RSI Strategy`, `//@version=5`, code header `Author = TradeAutomation`, page uploader `ChaoZhang`).
- FMZ backtest block pinned on the page: `start: 2023-09-26 00:00:00`, `end: 2023-10-26 00:00:00`, `period: 1h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` — single pair; the `1h` figure is the script decision timeframe adopted as the research frame.
- Live re-verification (2026-10-08): the FMZ page returns HTTP 200 (783,057 bytes); the page title, the `ChaoZhang` author line, `process_orders_on_close=true`, the `math.sum(rsi, cumlen)` construction, the entry/exit `crossover(cumRSI, os/ob)` lines, and the backtest header (2023-09-26 → 2023-10-26, `1h`/`15m`, `Futures_Binance` BTC_USDT) all match the mirror. No live-page fact contradicts the mirror.
- Mirror: `fmzquant/strategies` file `累积RSI突破策略Cumulative-RSI-Breakout-Strategy.md` at commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30), carrying the same Pine block and a `Detail` link back to FMZ 430328.
- Censuses over the pinned block: `request.*` 0, `security(` 0, `timeframe(` 0, `strategy.exit` 0, `strategy.order` 0, `volume` 0, `high`/`low` 0, Bollinger/`bb`/`stdev` 0. Series read: `close` only, plus `time` (only inside the provably always-true `InDateRange` gate below). `plot` lines never execute trading logic.

Licence and rights: the Pine block is published under MPL-2.0 on the FMZ page. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-08): working-tree searches for `430328`, `cumRSI`, `Cumulative RSI Strategy`, and `math.sum(rsi` return no strategy record using this source or signal — the sole `Cumulative RSI` hit is a passing mention inside `drm-dynamic-rsi-momentum-btcusdt-1d-2026-10-06.md` noting that file was never admitted (that record is a QuantNomad dynamic-RSI-momentum construction, different source and mechanism). Open `research/*` PRs: only #48 (Larry Williams 3-EMA channel streak long) and #49 (Gaussian channel StochRSI-gated breakout long) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `oversold-rsi-tight-sl-long-btcusdt-1h` (single-RSI level reversal with tight stop), `rsi-classic-level-reversal-btcusdt-1h` (classic RSI level cross), `rsi-ma-crossover-reversal-btcusdt-1d` (RSI-vs-MA cross), `cci-ema-rsi-cross-trailing-stop-btcusdt-1h` (CCI-gated dual-RSI cross with trailing stop). Five-axis distinction: mechanism differs (summed-RSI accumulation with dual fixed-threshold upward crossovers, versus single-RSI levels or RSI-vs-MA crosses), signal construction differs (`math.sum(ta.rsi(close,3),3)` through 60/282 versus raw RSI or cross relations), exits differ (close-evaluated rise-through-282 with no stop versus tight stops/trailing), horizon is `1h` BTCUSDT, source identity differs (FMZ 430328, `TradeAutomation`/`ChaoZhang`).

## Economic mechanism

### Source-reported

A mid-length trend-capture system: summing three consecutive 3-period RSI readings filters single-bar noise, so only a sustained multi-bar push lifts the accumulator through the entry threshold; the position is then held until buying pressure cumulates to an extreme (rise through 282 of 300), which the source treats as the leg's exhaustion point. An optional 100-period EMA uptrend gate (default off) is offered to skip entries printed below the medium trend.

### Research interpretation

Dual-threshold accumulation breakout with a close-evaluated hold: the entry demands the 3-bar RSI sum to rise through 60 (i.e. average RSI 20 across the window — a lift off deeply washed-out readings), so flat chop that never washes out cannot trigger it. The hold has exactly one exit leg — the sum rising through 282 (average RSI 94) — so legs end only on cumulated overbought extremes, never on time, price targets, or trailing levels. Both events are completed-bar-close comparisons under `process_orders_on_close=true`: there are 0 `strategy.exit` calls, hence no stop/limit order, no intrabar touch fill, and no same-bar TP/SL ordering ambiguity. No leverage, sizing, or cost edge is embedded in the signal; the source `initial_capital`/`default_qty_*`/`commission_*`/`slippage`/`margin_long` lines are capital configuration replaced event-neutrally by the house overlay (see Execution assumptions).

## Signal

Exact rule as pinned (Pine v5, defaults quoted — inputs unmodified; the `TrendFilterInput=false` default branch is pinned and the `true` branch is excluded as an unpinned alternative):

- Indicator: `rsi = ta.rsi(close, 3)`; `cumRSI = math.sum(rsi, 3)` (sum of the current plus two prior RSI-3 readings; theoretical range 0–300).
- Thresholds (exact arithmetic as written): `os = 100*3*20*0.01 = 60` (from the input labeled "Overbought Level", defval 20); `ob = 100*3*94*0.01 = 282` (from the input labeled "Oversold Level", defval 94). Labels are swapped in source (see Contradictions); numerics are pinned.
- Entry long: `strategy.entry("Long", strategy.long, when = ta.crossover(cumRSI, os))`. Strict prior-bar semantics (prior bar `cumRSI <= 60`, current bar `cumRSI > 60`); equality on either side fires nothing.
- Exit long: `strategy.close("Long", when = ta.crossover(cumRSI, ob))`. Strict upward crossover through 282 only — a falling cumRSI never exits, however far it falls.
- Direction: long-only. Zero short entries exist in the pinned block; the short side is explicitly disabled (no short rule to implement).
- Stop-loss / take-profit / trailing-stop / time limit / opposite-signal exit: explicitly none (0 `strategy.exit`, no `stop=`/`limit=`, no short side, no time-limit construct). A position whose cumRSI never rises through 282 is held indefinitely — recorded as the coded semantic, not repaired.
- Date gate: `InDateRange = time >= timestamp(2010-01-01) and time < timestamp(2099-01-01)` under pinned defaults — provably always-true over the source demo window and any full-history backtest. The `strategy.close_all()` under `not InDateRange` is dead code under these defaults. Altering the date inputs would be a different, unpinned rule.
- Excluded unpinned branch: `TrendFilterInput=true` (entry additionally gated by `close > ta.ema(close,100)`). The EMA-100 line is computed but read zero times on the pinned default path — provably inert here, disclosed, not admitted.
- Inert code, provably excluded: all `plot` lines, `comment=`/`alert_message=` strings (display/transport only), and the `Start/End Time` display inputs of the sibling Low-High file family (not present here).

## Required data

- Completed `1h` bars of BTCUSDT: `close` only (RSI, accumulation, EMA reference, and both crossover tests), plus `time` (only for the always-true `InDateRange` gate). No `open`, no `high`/`low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read.
- Single decision timeframe `1h` (backtest `period: 1h`). `basePeriod: 15m` is FMZ demo-execution granularity; with 0 intrabar orders and close-gated evaluation it cannot alter any admitted event.
- Warmup: `ta.rsi(close,3)` seeds its RMA at the 3rd bar; the 3-sample `math.sum` is first defined at the 5th bar; `ta.crossover` needs one prior bar. First fully-defined evaluation at 6 completed `1h` bars; no signal is evaluable before that. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (source venue is Binance USDT-M BTC futures; the house overlay runs Isolated futures at 3×/5×, long-only for this record since the short side is disabled as coded — no naked-spot construction needed).
- Order timing: both live order calls run under `process_orders_on_close = true`: completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. `calc_on_every_tick` is unset (default false). No next-bar-open, maker-touch, queue, or intrabar-path-dependent fill.
- Sizing/capital: `initial_capital = 25000`, `default_qty_type = strategy.percent_of_equity`, `default_qty_value = 110`, `margin_long = 75`, `commission_type = strategy.commission.cash_per_contract`, `commission_value = .0035`, `slippage = 1` are event-neutral capital/accounting configuration, replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3×/5×) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (Pine v5 default 0: no additional same-direction entry while the single `Long` position is held). At most one open long; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The FMZ page ships a backtest-chart image with no numeric caption — no ROI, Sharpe, win rate, drawdown, or trade-count figures are cited anywhere in this record. The prose claim of decade-long outperformance of buy-and-hold is qualitative only ("10年回测效果优异", "significantly outperforming buy and hold") with zero numbers attached. Recorded as an explicit gap, not filled: this record claims no source-reported performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Flat-book determinism: with no open position, `strategy.close("Long", ...)` is a deterministic engine no-op — only a genuine rise-through-60 can open.
2. Boundary ties are defined: any `cumRSI == 60` / `== 282` equality fails that leg's strict `crossover`; the accumulator needs a strict cross, not a touch.
3. Same-bar entry/exit co-fire resolves deterministically at the single close price: if cumRSI leaps from ≤60 to >282 in one bar, both legs fire — the entry call precedes the close call in code, so the bar opens-and-flats at one price with no P&L. With 0 `strategy.exit` calls there is no stop/limit ordering question for the reviewer to rule on.
4. One-sided exit semantic: a cumRSI that peaks at 281.9 and collapses never exits — the position rides the full drawdown by code design. Downstream must reproduce this, not "fix" it with a stop.
5. Enabling the EMA-100 trend gate, the Bollinger prose construction, the prose downward exit, or any non-default input would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: RSI(3) summed over 3 bars on `close`, entry rise-through-60, exit rise-through-282, long-only, `1h` BTCUSDT, same-bar-close fills are frozen.

- F1 — Accumulation relevance: replacing `cumRSI` with raw `ta.rsi(close,3)` and thresholds scaled to single-RSI equivalents (entry rise through 20, exit rise through 94) must not improve net expectancy; fail ⇒ the summation adds nothing.
- F2 — Exit relevance: replacing the rise-through-282 leg with a fixed 50-bar time exit (entry leg kept) must not improve net expectancy; fail ⇒ the extreme-accumulation exit is decorative.
- F3 — Entry-threshold relevance: moving only the entry threshold to 100 (exit kept at 282) must not improve net expectancy; fail ⇒ the washed-out-entry thesis is arbitrary.
- F4 — Parameter sensitivity: the (3, 3) length set must not be dominated net of costs by both the (2, 2) and (5, 5) neighbor sets; fail on both sides ⇒ the set choice is arbitrary rather than structural.

## Crypto portability

Pinned to BTCUSDT (Binance USDT-M lineage) under the house overlay. The long-only close-derived logic ports to perps without structural change; no funding-dependent leg, no stablecoin-specific assumption, no cross-venue state. Spot deployment needs no modification for the long side (no shorting required).

## Limitations

- No adverse protection of any kind: no stop-loss, no take-profit, no trailing level, no time exit — both decisions evaluate at the completed hourly close, and the sole exit requires an extreme upward accumulation event. A leg that never reaches 282 is held through arbitrary drawdown, including vertical adverse moves that exit only if/when a later bar's close prints the crossover.
- Rare-exit regime: cumRSI must average 94 across three bars to exit; in listless markets exits can be far apart and turnover near zero — long flat-holds with full exposure are the normal state, not a malfunction.
- Late-exit truncation works both ways: the 282 trigger fires only after the overbought extreme is already printed, so fast reversals from the peak are fully ridden back down.
- Whipsaw around 60: an accumulator hovering near the entry line can re-fire entries on successive rises after each 282-exit; each re-entry pays the pinned house costs with no structural edge claimed here.
- Source demo window is one month (2023-09-26 → 2023-10-26); full-history behavior is unreported by the source and unclaimed here.
- FMZ prose advertises Bollinger rails, a downward exit, and swapped overbought/oversold labels that the code does not implement; anyone deploying on prose alone would trade a different system.

## Implementation status

- `implementation_status: not-implemented`.
- Normalized rule is fully specified above; no Hummingbot/Qlib/n8n/survivor/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`, `status: research-only`.
- This record is semantic normalization only. It is not profitability validation, not a survivor promotion, and not Paper/Testnet/Mainnet authorization. Only `hb_ready_status: PASS` records may enter the current Hummingbot/Qlib performance-research downstream, subject to that workflow's own gates.

## Related Wiki records

None.

## Sources

- Primary: https://www.fmz.com/strategy/430328 (live page re-verified 2026-10-08, HTTP 200, 783,057 bytes; backtest block 2023-09-26 → 2023-10-26, `period: 1h`, Binance USDT-M BTC).
- Mirror: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/累积RSI突破策略Cumulative-RSI-Breakout-Strategy.md (same Pine block, links back to FMZ 430328; commit date 2025-04-30).
- Pine `strategy()` declaration semantics (first-party reference): https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- Strategy execution model (broker emulator, `process_orders_on_close`): https://www.tradingview.com/pine-script-docs/concepts/strategies/
