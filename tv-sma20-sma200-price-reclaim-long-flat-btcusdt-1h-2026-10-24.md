---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "TradingView 20/200 SMA trend-pullback reclaim, long-flat spot execution derivative"
created: 2026-10-24
updated: 2026-10-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-24
sources:
  - https://www.tradingview.com/script/ZqnuKIAw-20-200-SMA-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# 20/200 SMA trend-pullback reclaim — independent long-flat spot derivative

## Provenance and immutable identity

- Primary TradingView publication: https://www.tradingview.com/script/ZqnuKIAw-20-200-SMA-Strategy/ ; stable script ID **ZqnuKIAw**, title **20 / 200 SMA Strategy**, author **gpmpastorsc**, published **2026-05-17** (as displayed by the public page; inspected 2026-10-24). The page is marked **OPEN-SOURCE SCRIPT**.
- What the *author's page* actually states: SMA(20) versus SMA(200) determines trend; the named **Trend Pullback Entry** mode enters long when SMA20 > SMA200 and price crosses **back above** SMA20; it also describes a short-side counterpart, two other entry modes, a 100-point TP, opposing-candle-beyond-SMA200 default SL, alternate stops and optional filters. The page's textual description, not the full Pine code, was available for this review. No source Pine revision/hash or exact original default toggle settings are claimed.
- **This is an independently specified DERIVED executable strategy, not a Pine/source-native clone.** The following are *researcher decisions*, not author facts: select only the named Trend Pullback long entry mode; use BTC-USDT Binance spot 1h; define strict cross arithmetic; disable all source stop/target/short/filter variants; add explicit close-below-SMA20 or regime-loss exits; use one 0.001 BTC unleveraged spot position; execute stored signals at the next completed engine candle's close; use the pinned research cost and accounting convention below. These changes materially alter entry/exit/fill events. No claim of original TradingView order/event/backtest equivalence.
- Frozen derivative identity: `TV-ZqnuKIAw / gpmpastorsc / trend-pullback-only / BTC-USDT spot 1h / SMA20-SMA200 / long-flat / t-signal to t+1-close MARKET / 0.001 BTC / fee 0.001-per-side / 2026-10-24`. No later silent parameter changes.

## Economic mechanism

In an established SMA20-above-SMA200 uptrend, buy a completed-close reclaim of SMA20 following a price dip; hold only while price remains above the shorter average and the SMA regime remains bullish. This is a trend-continuation pullback, **not** a plain SMA20/SMA200 golden-cross strategy. Its close-reclaim edge is independent of whether the two averages cross on the entry bar.

## Signal — exact derivative (Gate 1, 2 and 3)

- Venue/feed: `binance` spot `BTC-USDT`, one completed `1h` OHLCV series; order logic uses **close** only, plus timestamps. No HTF, other symbol, trade tape, on-chain data, model fitting, indicator optimization or external signal.
- `S20[t] = (sum(close[t-i], i=0..19))/20`; `S200[t] = (sum(close[t-i], i=0..199))/200`. Finite, positive, fully available completed closes only; no EMA or alternative SMA source.
- `uptrend[t] = S20[t] > S200[t]` (strict; equality is NOT bullish).
- `reclaim[t] = close[t-1] <= S20[t-1] AND close[t] > S20[t]`; a tie on the previous bar is allowed, a tie on current bar blocks entry. This precise strict-edge convention is **derived**, not attributed to unseen Pine.
- `lose20[t] = close[t-1] >= S20[t-1] AND close[t] < S20[t]`. A tie on current bar does not exit by this leg.
- **Flat entry:** `uptrend[t] AND reclaim[t]`, provided no order is pending, schedules one BUY for execution at the close of completed bar t+1.
- **Held exit:** `lose20[t] OR S20[t] <= S200[t]`, provided no order is pending, schedules one SELL of the entire actual filled base quantity at completed bar t+1 close. If held and no exit, hold; if flat and no entry, remain flat. Exit has priority whenever held. No simultaneous long and short; never short.
- **Risk / disabled legs:** No protective price stop, no take-profit, no trailing, no timeout, no intrabar triggers, no 100-point source TP, no opposing-candle source SL, no optional filters, no reverse short. The two stated signal exits are the *only* planned liquidation paths; the resulting unprotected drawdown risk is deliberate and disclosed, not a hidden engine default.
- Source-native settings are **not** implied: the author offers several modes and stops; this record neither chooses an unverified original default nor relabels this derivative as the original Pine strategy.

## Position, order and cost state (Gate 4)

- Initial simulated cash `1000 USDT`; one unleveraged long only, desired entry size `0.001 BTC` (not a fraction of changing equity). No compounding, BO/SO ladder, pyramiding, scale-in/out, concurrency, cross-pair exposure, cooldown or automatic stop/retry. No additional BUY while held or while a BUY is pending.
- States `FLAT`, `BUY_PENDING`, `LONG(q_actual)`, `SELL_PENDING(q_actual)`. A signal at completed bar t stores one action. On completed t+1, first execute the pending MARKET action using that row's *real* close and actual available spot rules, then evaluate t+1's newly completed signal against the resulting actual state for **earliest t+2** execution. This ordering forbids same-bar lookahead and repeated orders. A rejected BUY returns to FLAT without replay; a rejected SELL retains LONG and is explicitly a failed/blocked exit requiring evidence, not a fabricated flat. End-of-data pending actions expire without a phantom fill.
- At BUY, use `min_base_amount_increment` to quantize requested 0.001 BTC down; reject zero, insufficient quote cash, non-finite/absent candle price or failed applicable exchange minimums; no substitute price, no fill if rule validation is unavailable. At SELL use **actual** held filled base amount, not the nominal request, and close only that long; any dust/rejection must remain visible in the position ledger.
- Backtest `trade_cost=0.001` of filled quote notional **on each filled side**, explicit fixed research assumption, not a claim of actual Binance VIP/taker fees. Simulated MARKET fill price is the execution candle close, not observed spread/slippage/order-book price; the simulator does not reproduce real market impact. Spot has no perpetual funding, isolated leverage, margin borrowing, liquidation or futures mark/index PnL; none is silently assigned a zero historical futures value. Track average acquisition price, quote turnover, realized/unrealized PnL and charged simulated fees in the existing net-position ledger. No backtest results are claimed.

## Exact pinned Hummingbot compatibility (Gate 5)

- Verified by GitHub source reads at **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`**: `hummingbot/VERSION` prints `dev-2.17.0`, matching policy's pinned package vintage `20260920`. This is source-level capability evidence; no container digest or test execution is invented.
- `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`: `BacktestingEngineBase.run_backtesting` takes explicit `trade_cost`; `prepare_market_data` merges timestamped candle rows; `simulate_execution` processes controller `CreateExecutorAction(OrderExecutorConfig)` and routes to `simulate_executor`; `BacktestPositionHold` nets spot BUY/SELL and tracks position cost/PnL. A strategy-specific controller to emit the specified one-bar-delayed actions is **not implemented**.
- `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`: `OrderExecutorSimulator.simulate` with `ExecutionStrategy.MARKET` fills at first simulated row's **close** and records that row's timestamp, `filled_amount_quote`, `cum_fees_quote = trade_cost * amount_quote`, `CloseType.POSITION_HOLD`. This supports the **derived t+1 close** action, not a source next-open or true exchange-taker execution.
- `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py`: `get_candles_df(connector_name, trading_pair, interval)` accesses `binance_BTC-USDT_1h`; `initialize_trading_rules` and `quantize_order_amount` expose spot size precision. This provider also has a price fallback in `get_price_by_type`; this derivative **must not use it**: absent/nonfinite execution-row close is a failed fill, never price 1 or a fabricated quote.
- Model boundary: one symbol, one completed-candle timeframe, spot MARKET netting only. No unverified next-open/maker/limit/intrabar/futures/multi-asset path is required. Simulator fees are modeled; actual fees, spread, funding and fills remain unverified. Passing this Gate means expressible *in this bounded pinned backtest model*, not that a ready-to-run controller exists or that it reproduces the source's Pine fills.

## Point-in-time causality and warmup (Gate 6)

- `S200[t]` first exists at completed bar #200; `reclaim`/`lose20` need both current and prior defined S20. Require **201 fully completed consecutive 1h bars** before the first entry/exit decision, with valid timestamp order and no missing required closes. The t signal becomes available only at `end_of_bar(t)`; store it then. Fill at t+1's completed close, after that later close is observed by the pinned simulator; no use of t+1 close to form the original t signal.
- Timestamp must be the exchange candle's **open** or explicitly normalized to it; completion is open+3600 seconds. Reject ambiguous timestamps, gaps needed for indicator windows, future bars, partial bars, revisions and invalid prices; do not forward-fill missing close. No `request.security`, repainting pivots, negative shift, future extrema or full-sample normalization.
- For a held position, first eligible exit is after the same warmup; at last available candle an unfilled pending order stays pending/expired, not an invented close.

## Evidence and falsification

- **Source-reported only:** the public TradingView prose names the SMA20/SMA200 trend regime and the trend-pullback cross-back-above-SMA20 long setup. It also names other modes, a 100-point TP, stop alternatives and optional filters, **none of which is silently adopted**.
- **Engine code independently inspected:** exact immutable source paths and fill/position/cost methods above. No strategy-specific implementation, simulation, trade-level parity, profitability, or independently reproduced performance exists yet.
- **Negative evidence:** cannot claim Pine-native equivalence without inspecting its actual revision/code and broker-emulator settings. If future source inspection contradicts even the page-stated trend-pullback description, the record requires source-fact remediation/rejection by independent Auditor, not a silent change.
- Falsify the derived implementation by testing: strict close reclaim while S20>S200; ties; no entry on plain S20/S200 cross without reclaim; no re-buy while held; first close-under-S20 or regime loss triggers SELL; t signal executes only at t+1 close; missing close/precision failure produces no phantom fill; per-leg modeled fees and netted average cost; warmup/gap guards. Compare source Pine event timing separately if full Pine becomes available; never label that comparison already performed.

## Deduplication

Current `main` at pre-write SHA `b6330df9bbd85a1e3e5597cdbc04610a04ebecfa`: search for script ID `ZqnuKIAw`, author and 20/200 pullback found no same-source strategy; open research PR search found no same URL or materially identical 20/200 price-reclaim rule. Nearby `golden-cross-sma-regime-gated-long` is a **9/50 cross gated by SMA100** and `eterna-sma-50-200-crossover` is a **50/200 MA crossover**; neither is a **price reclaim of SMA20 while SMA20>SMA200**. `double-seven-connors-pullback` uses rolling seven-bar lows with an SMA200 gate, not this event mechanism. No trivial length variant or exact duplicate is asserted.

## Limitations / adoption boundary

- The original author's Pine is **not** reconstructed losslessly. The derivative deliberately removes the source's TP/SL variants and defines its own signal exits and fill timing; its performance can diverge materially.
- A real strategy-specific Hummingbot controller is not implemented; no Qlib parity or strategy backtest has been run. Hummingbot `dev-2.17.0` code expressibility does not certify a deployment.
- `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`. No Paper/Testnet/Live authorization, no survivor or profitability assertion.

## Sources

- Primary TradingView: https://www.tradingview.com/script/ZqnuKIAw-20-200-SMA-Strategy/
- Immutable pinned engine: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Pinned market executor: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py
- Pinned net-position backtester: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/backtesting_engine_base.py
- Pinned data provider: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/backtesting_data_provider.py
