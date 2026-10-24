---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "TradingConToto six-filter ADX/DI EMA2400-4800 gap breakout long-flat (explicit derived v1, BTCUSDT spot 1h)"
created: 2026-10-24
updated: 2026-10-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
status: research-only
confidence: medium
source_as_of: 2025-09-06
sources:
  - https://www.tradingview.com/script/cK5NVkdF/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingConToto six-filter ADX/DI EMA-gap breakout — derived v1

## Provenance and immutable research identity

- Primary public TradingView open-source strategy: **Supertrend [TradingConToto]**, script ID **cK5NVkdF**, author **toto_scalper_23**, publication **2025-09-06**. Source page: https://www.tradingview.com/script/cK5NVkdF/ (public page read 2026-10-24 Asia/Taipei). The accessible page labels the publication open-source but did **not** expose the full Pine text or a Pine revision SHA to this Scout; no source-code-level or lossless Pine equivalence is claimed.
- **Immutable identity for this proposal:** `TV:cK5NVkdF:published-2025-09-06:derived-btcusdt-spot-1h-v1:2026-10-24`. This is a frozen *research rule set*, not a claim that TradingView's mutable publication has an immutable source-code commit. Later source edits or parameter choices require a different record/version.
- **Source-native facts verified from the author's publication:** the six simultaneous long filters are `+DI > -DI`, `ADX > mean(ADX)`, `close > EMA63`, `close > EMA4800`, `close > high[1]`, and `EMA2400 - EMA4800 > k × ATR`; long entry only when flat; exit if `+DI < -DI` OR `close < EMA63`. The author says no fixed trailing stop or TP, pyramiding 0, 1h recommended, 10% equity source sizing, source example commission 0.01% per side and slippage one tick. The page does not supply the numerical `k`, DI/ADX/ATR lengths, ADX-mean lookback, or their precise Pine smoothing/seed choices. Those are **not source facts**.
- **Independent derived executable strategy, NOT source-native reproduction.** Researcher-designed changes are explicitly frozen below: Binance BTC-USDT spot/1h; Wilder DI/ADX(14)/ATR(14) and SMA20-of-ADX; gap coefficient `k=1.0`; EMA/SMA seed convention; completed-bar decision followed by *next* bar close execution; fixed 0.001 BTC unit, 1000 USDT cash ledger, fee model 0.001 per side, and 5000-bar warmup. These are deliberate choices, **not inferred TradingView defaults**. The source's 10%-equity sizing, 0.01% commission, one-tick slippage and unspecified Pine order-fill timing are **not** reproduced.
- This derived record claims neither historical TradingView performance nor any independently reproduced returns, trades, Sharpe, Qlib parity, Survivor/HB Certified, Paper/Testnet/Live approval.

## Signal — complete frozen derived-v1 mathematics

All indices below denote consecutive **fully completed Binance spot 1h OHLCV candles**, chronological, UTC, no higher/lower timeframe or external data. `t` is a completed signal candle; `t-1` is the preceding completed candle. Prices must be finite and strictly positive; invalid or missing OHLC, duplicate/nonmonotone timestamps, or a gap in the required candle sequence causes a fail-closed no-trade/error, never a fabricated close.

1. `EMA_n(close)` uses `alpha=2/(n+1)`, seeded by the simple arithmetic mean of the **first n consecutive closes**, then `EMA[t]=alpha*close[t]+(1-alpha)*EMA[t-1]`; compute `EMA63`, `EMA2400`, `EMA4800`. No future samples or full-sample normalization.
2. `TR[t]=max(high[t]-low[t], abs(high[t]-close[t-1]), abs(low[t]-close[t-1]))`. `up=high[t]-high[t-1]`, `down=low[t-1]-low[t]`. `+DM=up` if `up>down and up>0`, otherwise 0; `-DM=down` if `down>up and down>0`, otherwise 0; ties set both to zero. Wilder `RMA14` of TR/+DM/-DM, each seeded by the first 14 valid values, uses `RMA[t]=(13*RMA[t-1]+x[t])/14`.
3. `+DI=100*RMA14(+DM)/RMA14(TR)`; `-DI=100*RMA14(-DM)/RMA14(TR)`. `DX=100*abs(+DI-(-DI))/(+DI+(-DI))`; `ADX=RMA14(DX)`; `ATR=RMA14(TR)`. A zero denominator makes that bar's DI/DX unavailable (no entry/exit evaluation until valid); no silent zero imputation. `meanADX=SMA20(ADX)`, the arithmetic mean of the current and preceding 19 *available completed* ADX values, not an all-history/future mean.
4. At completed bar `t`, `enter[t]` is the AND of: `+DI[t]>-DI[t]`; `ADX[t]>meanADX[t]`; `close[t]>EMA63[t]`; `close[t]>EMA4800[t]`; `close[t]>high[t-1]`; `EMA2400[t]-EMA4800[t]>1.0*ATR[t]`. Strict inequalities throughout. `exit[t]` is `(+DI[t]<-DI[t]) OR (close[t]<EMA63[t])`. The long-entry and exit conditions cannot simultaneously be true given their opposing strict comparisons. A tie means no trigger.
5. Signals are **state conditions**, not crossover edges. On each eligible bar, enter only when logically FLAT and not pending; exit only when logically LONG and not pending. No short orders, reversal, scaling, safety orders, pyramiding, time stop, take profit, fixed SL, trailing SL, or opposite-side short exposure. No cooldown; after a confirmed exit, the earliest new entry is a later bar's independently valid `enter` signal. No same-row re-entry.

## Required data, availability and causality

- `binance` connector, `BTC-USDT` **spot** trading pair, single `1h` feed, OHLC; volume is present in feed but **not used** by the signal. No futures funding, margin, leverage, OI, order book, maker queue, cross-pair state, multi-timeframe alignment or intrabar path dependency.
- **Warmup:** first **5000 consecutive completed 1h candles** are strictly flat and not eligible for any orders. This exceeds the EMA4800 seed and DI/ADX/SMA20 initialization. If 5000 valid bars plus a later executable bar are unavailable, reject the dataset; do not shorten the warmup or synthesize history.
- TradingView source execution timing is not asserted. Derived timing is **signal on completed bar t; market order on bar t+1 CLOSE**, with no look at bar t+1 before its close. The pinned Hummingbot simulator indexes Binance candles by **opening timestamp** but prices MARKET executions at the row's **close**. Consequently a fill on candle whose raw opening timestamp is `T` has economic availability time `T+3600 seconds`; event logs/replay must preserve both raw timestamp and effective close timestamp. A bar-t decision is available at `open[t]+3600`; its earliest derived fill is `open[t+1]+3600`. No same-bar-lookahead or source-native next-open equivalence is claimed.
- At each backtest row, the strategy-specific controller must use only the **one-bar-lagged** frozen signal, not a feature from that row to decide its order. A pending BUY/SELL prevents duplicates until the actual executor fill/failure is reconciled. The controller's logical FLAT/LONG state is based on confirmed filled quantity, **not** an assumption that `positions_held` is updated on the same tick. An unconfirmed or failed fill remains pending/halts new orders; never assume it filled. At most one MARKET action per candle; no same-bar exit-and-entry.
- An order submitted for the final dataset row is not treated as a successful position transition unless a corresponding real simulator fill/ledger event exists. Open positions at the end are marked to the final *observed* close for reporting, not force-closed at a fabricated next price.

## Execution assumptions — pinned Hummingbot model, NOT an implementation

- **Engine pin:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`; Hummingbot package `20260920`, `hummingbot/VERSION=dev-2.17.0`. No claim about later Hummingbot builds.
- **Actual pinned-code compatibility evidence (read, not run):**
  - `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py`: `INTERVALS` includes `1h`; `binance_spot_candles.py` maps BTC-USDT to Binance symbol BTCUSDT and reads historical klines; the candle timestamp is the exchange candle **open** time.
  - `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py`: fetches historical candle data and Binance trading rules; `get_candles_df` selects a pinned connector/pair/interval; `quantize_order_amount` uses exchange min-base increment. Its `get_price_by_type` contains a dangerous `Decimal("1")` fallback: **this derived controller MUST NOT rely on that fallback**. Explicitly require a real positive observed `close_bt` before every order.
  - `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`: `run_backtesting(..., backtesting_resolution="1h", trade_cost=...)` prepares real candle rows, calls `controller.determine_executor_actions()`, dispatches `OrderExecutorConfig` to `OrderExecutorSimulator`, updates `positions_held`, and accumulates `BacktestPositionHold` ledger. `BacktestPositionHold._process_order` nets BUY/SELL against average entry, books realized/unrealized PnL and quote fees. Its position-hold view can lag an executor tick; hence explicit pending/filled state above.
  - `hummingbot/strategy_v2/executors/order_executor/data_types.py` defines `OrderExecutorConfig` with `ExecutionStrategy.MARKET`, `side`, `amount`, `connector_name`, `trading_pair`; `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` fills MARKET at the **first selected row's close**, with `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, and `POSITION_HOLD` for netting. This is a deterministic **close-price model**, not proof of real-world taker fills, slippage or maker execution.
- **Controller binding:** a strategy-specific `ControllerBase`-style signal/action implementation (currently **not implemented**) must emit one `OrderExecutorConfig` MARKET BUY or SELL through the above pinned `BacktestingEngineBase` path; it is not represented as an already installed native controller. No new generic compiler, admission registry, or alternate simulator is requested by this record.
- **Sizing and account state:** initial modeled spot quote cash `1000 USDT`, no borrowing/compounding, one long of **0.001 BTC** per accepted BUY; SELL exactly the confirmed filled BTC quantity. Maintain a single explicit cash/base ledger, subtract BUY notional plus fee, add SELL proceeds minus fee, never permit negative BTC or quote cash. Before BUY, validate amount increment/minimum notional against actual Binance trading rules and check cash covers `0.001*observed_fill_close*(1+0.001)`. If rules, price, cash or exact fill are unavailable, **no order**; do not fabricate a price, round to a different strategy size, or assume a fill. Trading-rule values are checked/snapshotted at a future research run, not falsely claimed as presently verified.
- **Research costs:** pin `trade_cost=0.001` (0.10% of filled quote notional **per side**) solely as a researcher-declared hypothetical fee model. This is NOT the author's 0.01%-per-side example or an observed Binance fee. The simulator has no spread/market-impact/slippage model on this MARKET path; its close-price fill is a limitation, **not evidence of realized zero slippage**. No funding applies to spot (not an assertion of zero futures funding). No liquidation/margin/futures PnL is modeled. A later spot-fee/precision snapshot or a futures experiment would be separate execution evidence, not a silent change here.
- No Qlib or Hummingbot backtest, no empirical engine execution of this new controller, and no event-level parity were performed for this Scout submission. Gate 5 evidence here is **source-level verification of the pinned existing candle/MARKET/position-hold primitives and explicit exclusions**; it does not certify a strategy implementation or live fills.

## Six-gate HB_READY research assessment (submitted for independent review)

1. **Determinism:** six AND filters, DI/ADX/ATR/EMA formula, lengths, seed conventions, coefficient, comparisons, missing-data policy, and signal/exit priority frozen above. Unknown source inputs are declared as **derived**, never guessed as Pine facts.
2. **Direction:** long/flat only on BTC-USDT spot, short and reversal explicitly disabled.
3. **Entry/exit/risk:** six-filter flat entry; two-condition OR exit; no stop, target, trailing, time-exit, or hidden default. Unbounded adverse excursion is a disclosed strategy risk.
4. **Position state:** one fixed 0.001 BTC unit, no SO/DCA/pyramiding, pending-fill reconciliation, one action per candle, no same-row reentry, no cooldown, cash/fee accounting and fail-closed insufficient-funds behavior.
5. **Pinned engine:** exact Hummingbot commit/version and inspected real `BinanceSpotCandles` 1h, `BacktestingDataProvider`, `OrderExecutorSimulator` MARKET first-row-close, `BacktestPositionHold` netting and fee code; actual spot-only scope, raw-open/effective-close timestamp map, model limitations and no fake prices or funding.
6. **Causality:** 5000 completed-bar warmup; only t-1 completed-bar signal drives bar-t close fill; no future sample, full-sample mean, repainting, intrabar trigger, or incomplete HTF use.

## Limitations and independent review boundary

The accessible primary TradingView publication describes the six filters and exits but does not expose its full Pine code, coefficient `k`, ADX lookback or precise smoothing. **This is a deliberately distinct, researcher-defined executable version** with all missing choices pinned above. It cannot be advertised as lossless source-native. If the independent Hermes Auditor finds the published facts wrong, a pinned engine path unverified/unsupported, a cost/ledger incompatibility, or another material gap, it must return `HB_READY: NOT_LOSSLESS` and close this Scout PR, not silently rescue it by inventing semantics.

`hb_ready_status: PASS` here is a **Scout-submitted candidate assertion for independent six-gate audit**, not an auditor verdict, Qlib parity, profitability, implementation, survivor, HB certification or trading approval. No implementation, backtest, runtime, cron, workflow or main-branch change is authorized by this research-only record.
