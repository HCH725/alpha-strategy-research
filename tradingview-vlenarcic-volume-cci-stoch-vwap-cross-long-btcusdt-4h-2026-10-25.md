---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradingView vlenarcic volume-CCI/Stochastic spike-gated session VWAP/SMA crossover — independent BTCUSDT spot 4h derivative
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-12-01
sources:
  - https://www.tradingview.com/script/WXXcgwAQ-Volume-Momentum-Strategy-MA-VWAP-Cross/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Volume-spike-gated session VWAP/SMA crossover — independently derived research strategy

## Provenance and immutable identity

- Primary TradingView source: **Volume Momentum Strategy [MA/VWAP Cross]**, author **vlenarcic**, public script ID **WXXcgwAQ**, publication **2025-12-01**, described as **Pine Script v6** and **open-source**. Primary page: https://www.tradingview.com/script/WXXcgwAQ-Volume-Momentum-Strategy-MA-VWAP-Cross/ (public description inspected 2026-10-25). The complete Pine code was **not** reliably recovered from the public page; no source-code parity or original strategy backtest result is asserted.
- Author-description facts, distinguished from the independent derivative: (a) the principal directional triggers are an MA crossing above/below a session VWAP of HLC3; the MA type can be SMA/EMA/Hull; (b) the page describes volume CCI and volume Stochastic, with default **CCI > 100** and **Stochastic > 80**, as a **visual spike marker only**, **not a trading filter** in the published version; (c) the published strategy describes session/time restrictions, a close-all mechanism, and configurable percentage/dollar stop/target features, but their complete code/defaults are not available in the readable description.
- **Explicit independent derivative, not source-native/lossless.** This record deliberately **promotes the author's non-trading volume-spike visualization to an actual ENTRY gate**, selects SMA20/volume CCI20/volume Stoch14, restricts to Binance BTC-USDT **spot 4h** candles, defines a UTC-daily session VWAP, changes the short signal into long-position exit management, replaces the original unspecified time/stop/target/close-all rules with the fully defined exit below, pins one 0.001 BTC position, a 50-bar warmup, market-close simulator fills, costs and missing-data behavior. These are **researcher-defined changes**, not claims about original Pine code or defaults.
- Immutable derived identity: `TV-WXXcgwAQ | derived-v1-volumeCCI20>100-volumeStoch14>80-SMA20xUTCsessionVWAP-long-flat | BinanceSpot-BTC-USDT-4h | 2026-10-25`. Any altered gate, indicator definition, session anchor, exit, fill, or market is a different derivative.

## Economic mechanism

Hypothesis, not observed performance: a 20-bar average crossing above the current UTC session's volume-weighted fair-value line may be more selective when the crossover bar simultaneously exhibits an extreme volume CCI and a high rank of volume within the preceding 14 bars. The volume pair is an **entry filter invented for this derivative**; it is not attributed to the source author's actual order conditions. The strategy is long/flat and can remain in a losing position until a close below VWAP; there is no claim of profitable returns or risk protection.

## Signal — complete derived specification

- Venue and series: Binance BTC-USDT **spot**, consecutive **4h** UTC OHLCV candles. Bar `t` has an open-time label `T[t]` divisible by 14,400 seconds and becomes decision-available only at `T[t]+14400`. OHLCV must be finite, `high >= low > 0`, `close > 0`, `volume >= 0`; otherwise the bar is invalid and no event may be fabricated.
- Daily session: UTC 00:00 through 23:59:59, exactly six expected 4h candles. For each completed candle in the current UTC session, `typical[t]=(high[t]+low[t]+close[t])/3`; `sessionVWAP[t]=sum(typical[i]*volume[i] for i from session's 00:00 candle through t)/sum(volume[i] for same i)`. The sum **resets at each UTC 00:00**. If session cumulative volume is zero, VWAP is undefined and all signal comparisons fail. A missing/invalid candle in a session disables entry and exit signals for that entire session, restarting at the next UTC 00:00; a position is held, not liquidated at an invented price.
- `sma20[t] = sum(close[t-i], i=0..19)/20`, simple arithmetic mean (not EMA or HMA). Requires 20 consecutive completed closes.
- `vmean20[t] = sum(volume[t-i], i=0..19)/20`; `vdev20[t] = sum(abs(volume[t-i]-vmean20[t]), i=0..19)/20`; `vCCI20[t] = (volume[t]-vmean20[t])/(0.015*vdev20[t])`. This pins the current-window mean absolute deviation definition. When `vdev20=0`, CCI is undefined and the entry gate is false.
- `vLow14[t]=min(volume[t-i], i=0..13)`; `vHigh14[t]=max(volume[t-i], i=0..13)`; `vStoch14[t]=100*(volume[t]-vLow14[t])/(vHigh14[t]-vLow14[t])`. This is a stochastic of **volume itself** (`ta.stoch(volume,volume,volume,14)` concept), not a price Stochastic or a smoothed %D. Equal 14-bar min/max means undefined and entry false.
- Strict spike gate: `spike[t] = (vCCI20[t] > 100) AND (vStoch14[t] > 80)`. Equality at 100 or 80 is **false**. Both conditions are **researcher-promoted entry gates**, not source-native order logic.
- Cross: `crossUp[t] = (sma20[t-1] <= sessionVWAP[t-1]) AND (sma20[t] > sessionVWAP[t])`. To avoid an artificial cross caused solely by the UTC VWAP reset, `crossUp[t]` is **forced false on the first 00:00 bar of a UTC day**; the previous and current VWAP observations must be from the **same** UTC session. This suppression is a researcher rule. Equality on the previous bar arms a cross; equality on the current bar does not.
- `entry[t] = crossUp[t] AND spike[t]`. `exit[t] = sma20[t] < sessionVWAP[t]` (**strict level exit**, not a source-native short order or a crossunder requirement). The exit is **not** gated by the spike. The exit may fire on a session's first 00:00 bar; `sma20==VWAP` is hold.
- **State and priority:** initially FLAT. At each valid completed bar, first inspect the state carried into the bar. FLAT + entry -> one MARKET BUY of **0.001 BTC** at that bar's close -> LONG. LONG + exit -> one MARKET SELL of exactly **0.001 BTC** at that bar's close -> FLAT. Otherwise no order. Signals are mutually exclusive on every valid bar because entry needs `sma20>VWAP` and exit needs `sma20<VWAP`. Entries while LONG are ignored; exits while FLAT are ignored. No same-bar flip or second entry, no pyramiding, no partial exit, no safety orders/DCA, no averaging, no cooldown; the next later qualifying crossover may re-enter.
- **All other order/risk behaviors disabled by this derivative:** naked shorting, short reversal, margin/leverage, protective stop-loss, take-profit, trailing stop, intrabar touch order, maker/limit orders, time limit, scheduled close-all, source time-window filter, cross-asset synchronization, shared-capital portfolio logic, compounding, and forced liquidation at dataset end. A remaining final position stays open and is marked to the last available close for reporting; no terminal sale is invented.
- **Warmup and missing data:** require **50 consecutive valid completed 4h bars** and a fully valid current UTC session; no entry/exit before that point. An invalid/missing bar breaks the consecutive warmup and suspends signals until a fresh 50-bar contiguous sequence and a fresh complete-to-date session are available. While suspended, a held position remains open. All lookbacks are nonnegative and only refer to bars at or before the decision bar.

## Required data and point-in-time causality

Only the single BTC-USDT spot 4h OHLCV stream is used; no lower-frame bars, other market, funding, OI, order book, mark/index prices, non-OHLCV inputs, or real-time partial-candle updates. The VWAP reset is based on the current candle's **known UTC open-time label**; the current candle's price/volume are consumed **only after its 4h close**. There is no lookahead, `request.security`, future pivot, negative shift, full-sample fit, ML model, or repainting. All 50 seed bars are completed before any decision. No missing price/volume is filled with zero, last-known, or a synthetic observation.

## Execution assumptions — pinned Hummingbot engine/data proof

**Admission baseline:** Hummingbot package `20260920`, `hummingbot/VERSION=dev-2.17.0`, pinned repository `HCH725/hummingbot` commit **`8b0e067e80ab62f10846d518dcb5a8218527ddb3`**. The following files at that exact commit were read through GitHub during this Scout cycle:

1. **Actual candle path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` explicitly lists `"4h":"4h"`. `binance_spot_candles/binance_spot_candles.py` parses Binance REST `/api/v3/klines` `row[0]` as candle **open timestamp** and `row[1..5]` as OHLCV; its websocket parser explicitly maps `k.t`, `k.o/h/l/c/v`. `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` `prepare_market_data` carries `open_bt/high_bt/low_bt/close_bt/volume_bt` into processed rows. The derived controller can calculate SMA, volume CCI/Stochastic and session VWAP from **only these columns**, using the pinned formulas and UTC timestamp, without an unsupported data feed.
2. **Controller/executor:** `backtesting_engine_base.py` `simulate_execution` iterates processed candles, calls `update_state(row)` and `controller.determine_executor_actions()`, and accepts `CreateExecutorAction`. `hummingbot/strategy_v2/executors/order_executor/data_types.py` defines `OrderExecutorConfig` with `connector_name`, `trading_pair`, `side`, `amount`, `execution_strategy=MARKET`, and `leverage=1`; `price=None` is valid for MARKET, and `hummingbot/strategy_v2/executors/validation.py` explicitly skips `None` in `require_positive`. The declared controller is a not-yet-implemented **strategy-specific state machine**, not an additional service or admission gate.
3. **Fill path and clock:** `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` `simulate` for `ExecutionStrategy.MARKET` takes the first supplied candle, fills at that row's **close**, calculates `filled_amount_quote = amount * close` and `cum_fees_quote = trade_cost * filled_amount_quote`, then returns `POSITION_HOLD`. The engine's raw `fill_timestamp` is the candle's **open-time label**, not a real exchange fill timestamp. The derived research event's causal/effective timestamp is explicitly normalized to `open_timestamp+14400` (the 4h close). This is a **research close-fill convention**, not a claim that an actual market order can execute at a close known only after completion.
4. **Position and economics:** `backtesting_engine_base.py` `BacktestPositionHold` nets BUY/SELL base quantities, tracks weighted average cost, realized gross quote PnL and `cum_fees_quote`. Use one `Q=0.001 BTC` spot position, `leverage=1`, no futures funding (**not applicable** on spot, not modeled as a realized zero stream), no margin/liquidation. Pin simulator `trade_cost=0.001` **per side**, charged as 0.1% of filled quote notional. Derived realized **net** quote PnL = matched gross quote PnL minus **both sides' cumulative fees**; unrealized PnL and cash/equity must separately include fees. The simulator fills at the supplied close and has no independent slippage/impact model (effective modeled slippage 0 **by this simulator**, never a claim of actual zero slippage). Exchange min-notional, tick/lot rounding, market liquidity and partial fills are **not verified** and are explicitly out of scope for live execution; the record makes no real-world precision or realized-economics claim.
5. **No unverified primitive smuggled in:** No maker queue, next-open, intrabar high/low touch, cross-timeframe alignment, multi-asset shared capital, funding settlement, order-book or external state is required. The strategy is expressible as one completed-candle calculation plus MARKET-close OrderExecutor actions on the existing spot 4h path. The exact UTC session VWAP is a deterministic calculation over the already exposed `volume`/OHLC columns, not an assumption of a hidden built-in VWAP feature.

**Scope of verification:** static code-path compatibility only; no Hummingbot/Qlib run, actual trade, implementation, or event-level parity has been performed. Hermes independent auditor must re-check all six gates and the exact immutable head before any merge. Representative Qlib/HB parity is a separate prerequisite before screening an unverified execution path at scale. `hb_ready_status: PASS` here means the **submitted researcher's six-gate claim awaiting independent review**, not an independently granted approval.

## Six-gate evidence for independent reviewer

1. **Determinism:** every formula, window, smoothing/none, strict comparison, UTC reset, zero-denominator convention, gap handling, and state priority is pinned; source-native facts are explicitly separated from researcher-defined choices.
2. **Direction:** Binance BTC-USDT spot, LONG/FLAT; no short or leveraged position.
3. **Entry/exit/risk:** simultaneous MA/VWAP crossover and two-volume-indicator spike gate, exit on MA-below-VWAP level, all alternative exits and risk controls explicitly disabled.
4. **State:** one 0.001 BTC unit, one concurrent position, no DCA, no add, no partial, no cooldown; exact transitions and final-open-position behavior.
5. **Engine:** immutable package/version/commit; actual 4h Binance spot OHLCV source, controller/OrderExecutor MARKET close fill, 4h timestamp normalization, fee, spot accounting and precision limitations evidenced above.
6. **Causality:** 50 completed contiguous bars, current-session-only VWAP, first-session-bar cross suppression, missing-data fail-closed rule, no future read or partial candle.

## Evidence, deduplication and negative evidence

- **Source-reported:** TradingView author description (vlenarcic, 2025-12-01) supports MA/VWAP directional cross, HLC3 session VWAP, SMA/EMA/Hull selectable, and volume CCI/Stoch spike as **visual only**. It describes optional session/close-all/risk features without their exact default code. No source performance is cited.
- **Independently reproduced:** None. The six-gate argument uses static pinned-engine source inspection, not a reproduced strategy backtest.
- **Main snapshot/dedup (2026-10-25):** `main` SHA `af39dc33df419c07ffe4b5ef1917a6184fd44a4f`; README reports **313** admitted and the GitHub main tree has **313** root-level strategy Markdown files. This numeric match does **not** claim every existing file's frontmatter was independently re-audited this cycle. GitHub code search for TradingView script ID `WXXcgwAQ` returned no match; open research PR search for that identity and the proposed VWAP volume-momentum family returned none.
- **Nearest mechanisms differ materially:** `forven-vwap-rolling-cross-long-flat-btcusdt-1h-2026-10-17.md` crosses **close** versus a **rolling 20-bar VWAP**, with no session reset, no SMA-vs-VWAP cross and no simultaneous volume-CCI/Stoch gate; `vwap-bounce-band-reversal-two-sided-btcusdt-1h-2026-10-12.md` uses **price wick/0.5% VWAP deviation-band touch plus EMA50 trend** with two-sided positions, not a volume-spike-gated MA cross. This record is neither a paraphrase nor a trivial parameter variant.
- **Negative evidence / limitations:** full original Pine unavailable; the author's original CCI/Stoch are *not* an order filter; no original defaults for MA period, indicator lengths, sizing, cost, stop/target or time gates are asserted. Current derivative has no protective stop and can hold through a severe drawdown; spike-plus-cross may be rare; a UTC VWAP reset is a researcher choice; fee model is simulated, slippage/precision are not exchange-realistic; 4h close-fill normalization is mandatory for causal accounting. None of these are presented as source-native, profitability evidence, or production authorization.

## Falsification plan (downstream only; not executed)

Freeze this derivative before research. Test whether (a) the two-volume-indicator gate improves out-of-sample expectancy over the same SMA20/session-VWAP cross without the spike gate, (b) UTC session VWAP beats a fixed rolling 6-bar VWAP, and (c) a different exit (strict crossunder instead of level-below) changes net expectancy. These are **future hypotheses**, not current admission rules, backtest results or permission to optimize on OOS. No campaign, Qlib/HB backtest, paper/testnet/live execution or runtime modification is authorized by this record.
