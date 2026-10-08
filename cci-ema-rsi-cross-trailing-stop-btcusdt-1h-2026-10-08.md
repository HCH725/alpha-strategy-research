---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: CCI-gated dual-RSI-cross trend system with close-evaluated trailing stops on BTCUSDT 1h bars
created: 2026-10-08
updated: 2026-10-08
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2022-05-09
sources:
  - https://www.fmz.com/strategy/362029
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/CCI-EMA-with-RSI-Cross-Strategy.md
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The FMZ page prose claims trades are taken only during the normal trading session and closed 15 minutes before the session close, but every session construct in the pinned Pine block is commented out (`//open_session`, `//session`, `//validSession`, `//... and validSession`). The admitted rule pins the code: no session filter exists and the system is always active. The prose claim is recorded as a source-internal contradiction, not repaired."
---
# CCI-gated dual-RSI-cross trend system with close-evaluated trailing stops on BTCUSDT 1h bars

## Provenance

Primary source read end to end (FMZ strategy page live plus GitHub mirror cross-check):

- FMZ strategy: https://www.fmz.com/strategy/362029 (`CCI + EMA with RSI Cross Strategy`, Pine title `CCI + EMA with RSI Cross Strategy`, `//@version=5`, code copyright `rwestbrookjr`).
- Last modified (as printed in the page data): 2022-05-09 17:00:24 (live page renders this as "4 years ago"; consistent).
- FMZ backtest block pinned on the page: `start: 2022-01-01 00:00:00`, `end: 2022-05-07 23:59:00`, `period: 1h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` — single pair; the `1h` figure is the script decision timeframe adopted as the research frame.
- Live re-verification (2026-10-08): the FMZ page returns HTTP 200 (754,652 bytes); the page title, the `rwestbrookjr` copyright line, `process_orders_on_close=true`, the exact declaration (`strategy("CCI + EMA with RSI Cross Strategy", overlay=true, margin_long=100, margin_short=100, process_orders_on_close=true)`), the exact entry lines (`strategy.entry("Long", strategy.long)`, `strategy.entry("Short", strategy.short)`), the exact exit lines (`strategy.close("Long")`, `strategy.close("Short")`), the stop-ratchet lines (`math.max(stopValue, longStop[1])`, `math.min(stopValue, shortStop[1])`), and the backtest header all match the mirror. No live-page fact contradicts the mirror.
- Mirror: `fmzquant/strategies` file `CCI-EMA-with-RSI-Cross-Strategy.md` at commit `7853bb2bf262c4567ac238d3552d97f0e50cb801`, carrying the same Pine block and a `Detail` link back to FMZ 362029.
- Censuses over the pinned block: `request.*` 0, `security(` 0, `timeframe(` 0, `strategy.exit` 0, `strategy.order` 0, `input.time` 0, `volume` 0, `open` 0 in trading logic (series read: `close` and `hlc3` only). `strategy.opentrades` occurs only inside commented-out lines. Session inputs occur only inside commented-out lines.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-08): working-tree searches for `362029`, `cci-ema-with-rsi`, `cciBull`, `cciBear`, `longStop`, `Trail Loss`, `ta.cci`, and Commodity Channel return 0 strategy records — no CCI-family mechanism exists on `main`. Open `research/*` PRs: only #48 (Larry Williams 3-EMA channel streak long) and #49 (Gaussian channel StochRSI-gated breakout long) — different mechanisms, indicators, and sources. Closest records are different mechanism classes: `rsi-classic-level-reversal-btcusdt-1h-2026-10-07.md` (single RSI-27 versus its own SMA-10 average, always-in-market reversal) and `rsi-ma-crossover-reversal-btcusdt-1d-2026-10-07.md` (same always-in-market structure). Five-axis distinction: mechanism differs (CCI-threshold gate plus fast/slow RSI cross plus slow-EMA price filter plus ratcheting close-evaluated trailing stop with genuine flat states, versus single-RSI-versus-its-average reversal with no flat state), signal construction differs (three-gate conjunction on `cci > 50` / `crossover(rsi9, rsi20)` / `close > EMA20` versus one RSI/average cross), exits differ (ratcheted close-level stop versus opposite-signal reversal), horizon is `1h` BTCUSDT, source identity differs (FMZ 362029, `© rwestbrookjr`).

## Economic mechanism

### Source-reported

A two-sided trend-capture system: it waits until momentum broadens (CCI pushes beyond ±50), faster RSI (9) confirms by crossing its slower sibling (20) in the same direction, and price sits on the trend side of EMA-20 — then rides the leg until price closes back through a slow-EMA-anchored trailing level that only ever tightens.

### Research interpretation

Triple-gate trend entry with an asymmetric hold: the CCI gate demands a volatility-normalized push, the RSI cross demands short-horizon momentum confirmation, and the EMA-20 price filter vetoes counter-trend crosses. The exit is a close-evaluated ratchet, not an intrabar stop order — the book can only transact at completed-bar closes, so the "trailing stop" is a deterministic close-level rule with no intrabar path dependence. No leverage, sizing, or cost edge is embedded in the signal; the source `margin_*` lines are capital configuration replaced event-neutrally by the house overlay (see Execution assumptions).

## Signal

Exact rule as pinned (Pine v5, defaults quoted — inputs unmodified):

- Inputs: `fastLen = 9`, `slowLen = 20` (EMA lengths, `close` price); RSI lengths 9/20 with `input.source(close)` both pinned to `close`; `cciLength = 20`, `src = hlc3`, `cciCut = 50`; `trstp = 0.67` (Trail Loss, price units).
- Trend state: `fastEMA = ta.ema(close, 9)`, `slowEMA = ta.ema(close, 20)`; `Bull = fastEMA > slowEMA`, `Bear = fastEMA < slowEMA`. `Bull`/`Bear` gate only the stop ratchet below; the commented-out entry variants that used them are inert, not admitted.
- Dual RSI (explicit Wilder form, written out, not a built-in call): `up1 = ta.rma(math.max(ta.change(close), 0), 9)`, `down1 = ta.rma(-math.min(ta.change(close), 0), 9)`, `rsi = down1 == 0 ? 100 : up1 == 0 ? 0 : 100 - (100 / (1 + up1 / down1))`, mirrored for `rsi2` with length 20. The ternaries are coded divide-by-zero guards, not reviewer additions.
- CCI (hand-rolled, exact calls pinned): `ma = ta.sma(hlc3, 20)`, `cci = (hlc3 - ma) / (0.015 * ta.dev(hlc3, 20))`; `cciBull = cci > 50`, `cciBear = cci < -50`. Strict inequalities: `cci == ±50` fires neither gate — the boundary case is defined, not ambiguous.
- Entry long: `longCondition = cciBull and ta.crossover(rsi, rsi2) and close > slowEMA`, live via `if (longCondition)` → `strategy.entry("Long", strategy.long)`.
- Entry short: `shortCondition = cciBear and ta.crossunder(rsi, rsi2) and close < slowEMA`, live via `if (shortCondition)` → `strategy.entry("Short", strategy.short)`. `ta.crossover`/`ta.crossunder` carry strict prior-bar semantics as written.
- Trailing levels (position-aware state, fully explicit): `longStop := Bull or position_size > 0 ? math.max(slowEMA - 0.67, longStop[1]) : 0.0`; `shortStop := Bear or position_size < 0 ? math.min(slowEMA + 0.67, shortStop[1]) : 999999`. The ratchet only ever tightens while its regime/position clause holds and snaps to its inert sentinel otherwise.
- Exit long: `longExit = close < longStop` → `strategy.close("Long")`. Exit short: `shortExit = close > shortStop` → `strategy.close("Short")`. Both exits are evaluated on the completed-bar close — there are 0 `strategy.exit` calls, hence no stop/limit order, no intrabar touch fill, and no same-bar TP/SL ordering ambiguity anywhere in the rule.
- Opposite-signal behavior: a short entry while long (or long entry while short) reverses the book under Pine default entry semantics; `strategy.close("Long")`/`strategy.close("Short")` each address only their own entry id, so a cross-id close with no matching open position is a deterministic no-op. No silent Hummingbot defaults are relied upon.
- Inert code, provably excluded: `rsiBull`/`rsiBear` are written once and read zero times; all `//`-prefixed alternate conditions, session lines, `entry_price`-based exits, `plotshape` lines, and the `fill` line never execute. The session filter the prose describes does not exist in the executable rule (see Contradictions).
- Stop loss / take profit / trailing-stop *orders* / time limit: explicitly none (0 `strategy.exit`, 0 `stop=`/`limit=`). The trailing *level* above is a close-evaluated exit condition, recorded as what it is — not as a stop order.

## Required data

- Completed `1h` bars of BTCUSDT: `close` and `hlc3` only. No `open`, `high`, `low`, or `volume` in the trading logic; no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session/time, or cross-venue state is read.
- Single decision timeframe `1h` (backtest `period: 1h`). `basePeriod: 15m` is FMZ demo-execution granularity; with 0 intrabar orders and close-gated evaluation it cannot alter any admitted event.
- Warmup: longest lookback is 20 bars (EMA-20, RSI-20 rma chain, CCI-20 sma/dev). First fully-defined evaluation at 20 completed `1h` bars; no signal is evaluable before that. No repainting, no negative shift, no future reference, no full-sample normalization. A 20-bar window of exactly equal `hlc3` makes `ta.dev` zero and `cci` `na`, which deterministically fires no gate.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (source venue is Binance USDT-M BTC futures; the house overlay runs Isolated futures at 3×/5×, so both directions need no naked-spot construction).
- Order timing: all four live order calls run under `process_orders_on_close = true`: completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. `calc_on_every_tick` is unset (default false). No next-bar-open, maker-touch, queue, or intrabar-path-dependent fill.
- Sizing/capital: `margin_long = 100, margin_short = 100` and the unset quantity inputs are event-neutral capital configuration, replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3×/5×) and never presented as source-native behavior. The source declares no commission model; the pinned house cost assumptions apply as pure accounting and do not alter signal, timing, direction, or exits.
- Concurrency: at most one open position (single entry id per side, default single-position declaration); no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The FMZ page ships a single backtest-chart image with no numeric caption — no ROI, Sharpe, win rate, drawdown, or trade-count figures appear anywhere in the artifact. Recorded as an explicit gap, not filled: this record claims no source-reported performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Entry/exit co-fire is impossible per side: long entry needs `close > slowEMA` while the active long stop never exceeds `slowEMA - 0.67` (and is `0.0` when reset, which no BTC close undercuts); short side mirrors. Entry-before-exit code order therefore needs no priority ruling.
2. Boundary ties are defined: `cci == 50` (or `-50`) satisfies neither gate; `fastEMA == slowEMA` sets neither `Bull` nor `Bear`.
3. `strategy.close` on a flat book, or against the non-open side's id, is a deterministic no-op — it opens nothing and inverts nothing.
4. `ta.dev(hlc3, 20) == 0` yields `na` CCI, which fires no gate rather than a stale signal.
5. Enabling the commented-out session filter, EMA-regime entry variants, or `entry_price`-based exits would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 9/20 EMAs, 9/20 close-RSIs, CCI(hlc3, 20, ±50), $0.67 trail offset, both sides, `1h` BTCUSDT, same-bar-close fills are frozen.

- F1 — CCI-gate relevance: removing the `cciBull`/`cciBear` gate (RSI-cross plus EMA filter only) must not improve net expectancy; fail ⇒ the CCI leg adds nothing.
- F2 — Exit relevance: replacing the ratcheting close-stop with a fixed 24-bar time exit must not improve net expectancy; fail ⇒ the trailing-level leg is decorative.
- F3 — Cross sensitivity: the (9, 20) RSI-cross pair must not be dominated by both the (5, 20) and (14, 30) variants net of costs; fail on both sides ⇒ the pair choice is arbitrary rather than structural.
- F4 — Session discipline: adding any session/time filter must be evaluated as a separate variant, never silently merged; the admitted record stays always-active as coded.

## Crypto portability

Pinned to BTCUSDT (Binance USDT-M lineage) under the house overlay. The two-sided close-derived logic ports to perps without structural change; no funding-dependent leg, no stablecoin-specific assumption, no cross-venue state. Spot deployment would require disabling the short side — a different, unpinned rule, not a repair of this one.

## Limitations

- No price-level risk exit: the ratchet trails `slowEMA ∓ 0.67`, so a vertical adverse move exits only at the next completed-bar close below/above the level — gap risk is fully retained.
- Trail offset is microscopic in BTC price units ($0.67): in fast markets the stop hugs the EMA and whipsaws; the record pins the value as written rather than "fixing" it.
- Whipsaw regime: RSI 9/20 crosses fire repeatedly in range-bound chop while CCI flickers around ±50; the triple gate attenuates but cannot eliminate this.
- Source demo window is four months (2022-01-01 → 2022-05-07); full-history behavior is unreported by the source and unclaimed here.
- FMZ prose advertises session filtering and pre-close flattening that the code does not implement; anyone deploying on prose alone would trade a different system.

## Implementation status

- `implementation_status: not-implemented`.
- Normalized rule is fully specified above; no Hummingbot/Qlib/n8n/survivor/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`, `status: research-only`.
- This record is semantic normalization only. It is not profitability validation, not a survivor promotion, and not Paper/Testnet/Mainnet authorization. Only `hb_ready_status: PASS` records may enter the current Hummingbot/Qlib performance-research downstream, subject to that workflow's own gates.

## Related Wiki records

None.

## Sources

- Primary: https://www.fmz.com/strategy/362029 (live page re-verified 2026-10-08, HTTP 200, 754,652 bytes; last modified 2022-05-09 17:00:24).
- Mirror: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/CCI-EMA-with-RSI-Cross-Strategy.md (same Pine block, links back to FMZ 362029).
- Pine v5 `strategy()` declaration semantics (first-party reference): https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- Pine v5 `strategy.entry` semantics: https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry
- Strategy execution model (broker emulator, `process_orders_on_close`): https://www.tradingview.com/pine-script-docs/concepts/strategies/
