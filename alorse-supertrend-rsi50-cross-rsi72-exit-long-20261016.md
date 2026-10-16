---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Alorse Supertrend bullish-regime RSI50 upward-cross RSI72 exit"
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/trend/Supertrend%20%2B%20RSI.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alorse Supertrend bullish-regime RSI50 upward-cross RSI72 exit

Source pinned commit `8fb3837ddcd137f1450c3e82d654ff3df24d54d5`, exact file `strategies/trend/Supertrend + RSI.pine` (read end-to-end): https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/trend/Supertrend%20%2B%20RSI.pine

## Provenance and mechanism

Original Pine v5 trend-confirmed RSI midpoint momentum rather than basic Supertrend flip. Author defaults source dynamic `20% equity`, initial 1000 USD and 0.01% source commission; researcher chooses fixed **200 USDT** (20% initial) for this strategy instead of the 100-USDT common base below, a declared sizing derivation. Source default long true / short false. Existing single Supertrend and RSI family records have different event logic.

## Signal — exact default decision predicates

- `[_,direction] = ta.supertrend(factor=3.0,atrPeriod=10)`: TradingView Wilder ATR ST, `direction<0` indicates bullish; `ta.change(direction)>0` indicates bearish trend flip (including a change from -1 to +1).
- `src=close`, `lenRSI=14`, `RSI=ta.rsi(close,14)`.
- `showLong=true`, `showShort=false`; default `RSIoverbought=72`, `RSIoversold=28`; `TPPercent=1.2` is **calculated only**, and its `strategy.exit` orders are COMMENTED OUT. No source active take-profit despite field name.
- `entryLong=(direction<0) AND RSI[t-1]<50 AND RSI[t]>50` (strict cross through 50; equality doesn't count).
- `exitLong=(RSI>72) OR (ta.change(direction)>0)`; `strategy.entry("Long",strategy.long,when=entryLong)` and `strategy.close("Long",when=exitLong)`.
- Source optional short logic (inactive by default): `entryShort=(direction>0) AND RSI[t-1]>50 AND RSI[t]<50`; `exitShort=(RSI<28) OR (ta.change(direction)<0)`. Do not add Short path under the default.
- No live SL, TP, trailing, time exit, cooldown, safety orders. Source `pyramiding=0`, repeat entry suppressed, re-enter after flat. Entry and exit *can* cofire only if RSI goes from below 50 to above 72 in the same bar; **state-dependent derivative ordering**: while already long exit wins; while flat entry wins and exit close would be a no-op. Always at most one net transition.
- Conservative warmup 100 complete 1h candles for Wilder RSI14 and ST10 settlement, researcher-declared rather than a source input. No `request.security`, future leaks or other data modalities; next-open source filled as next-close research derivative below.

## Required data, point-in-time and execution

This candidate is an **explicit execution derivative**, not a source-native Pine execution clone. Venue `binance` spot `BTC-USDT`; decision candles `1h` (author's backtest timeframe never filters strategy admission). Compute every source indicator from **completed candle t** with no partial bar and apply the stored t signal to MARKET order on the following simulator row **t+1 at CLOSE**, not at Pine's native next-bar OPEN. No t+1 input is read by t's signal; no phantom fill at end of history. No futures contract, liquidation, leverage, historical perpetual funding or hidden DCA. One held long at maximum; no shorts or over-allocation; exit SELL equals actual filled BTC quantity. Start capital 1000 USDT; 200 USDT fixed notional BUY (20% initial capital, no compounding), distinct from author's dynamic percent-of-equity sizing, explicitly derived. `BacktestingEngineBase.run_backtesting(controller_config,start,end,backtesting_resolution="1h",trade_cost=0.0001)` uses one-way 0.01% fixed fee as *research approximation* numerically matching the source commission when supplied; not an asserted Binance real fee tier, spread, or maker execution. Quantize BTC amount to actual connector base increment and skip invalid min-notional orders, never fill synthetic prices.

Code path, frozen and verified at **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3** from 2026-09-20, whose `hummingbot/VERSION` is literally `dev-2.17.0`, matching the canonical pinned package `20260920` version:
- `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` `run_backtesting` obtains completed connector candle feed, `prepare_market_data` merges OHLCV and the strategy's cached signal features, `simulate_execution` iterates timestamp rows and calls `controller.determine_executor_actions` then routes `CreateExecutorAction(OrderExecutorConfig)` to `OrderExecutorSimulator`.
- `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` `ExecutionStrategy.MARKET` fills at its first simulated row's CLOSE, charges `trade_cost*filled_amount_quote`, returns `POSITION_HOLD`.
- `BacktestPositionHold._process_order` nets same-pair BUY and SELL, tracks cost basis, realized PnL and fees; full SELL flattens.
- `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` keys feeds by `binance_BTC-USDT_1h`, loads trading rules, applies base-amount and price increments.
- Existing first-party `controllers/generic/pmm_mister.py` demonstrates controller actions using a MARKET `OrderExecutorConfig`. The actual strategy-specific indicator/controller code is **not yet implemented** and is not an admission requirement; this is an existing simulator primitive, no new framework.
- Preexisting tests, inspected in the **same pinned source revision**, not executed by us: `test_backtest_position_hold.py` (`test_buy_sell_netting`, `test_full_netting_closes_position`, `test_netted_position_realized_pnl_in_summary`), `test_backtesting_final_tick_ledger.py` (Binance spot `OrderExecutorConfig`, `POSITION_HOLD`, final row ledger), `test_backtesting_engine_directional.py` (representative Binance perpetual candle/action/engine and adjustable `trade_cost`). This code-level proof is not a binary image digest or strategy backtest.

## Evidence

Source rules below inspected from the complete pinned Pine file. No source profit or independently reproduced returns or fills are claimed. The proposed PASS concerns expressibility of this **declared derived spot/next-close strategy only**, not profitability, source-native next-open economics, Qlib parity, futures 3x/5x or live trading.

## Falsification plan

For every bar after the declared warmup independently recompute all original indicator series and strict comparisons; assert the same *source decision events*. Assert one position max, while-long entry no-op, flat exit no-op, zero unexpected shorts, fill on next simulation candle close with quote fee 0.0001 per filled leg, and exact quantity netting. Compare original Pine next-open prices separately to disclose derivative fill timing gap.

## Crypto portability

Source indicators have no mandatory BTC daily chart setting. The sole reviewed execution derivative pins spot BTC-USDT 1h. Other instruments, 4h/1d, 3x/5x isolated perpetual plus BO/SO DCA are explicitly separate research campaigns, not silently asserted compatible with this spec.

## Implementation status

`not-implemented`. No Qlib/Hummingbot/n8n source code or live trading was changed.

## Adoption boundary

`research-only`, `not-approved`. An independent existing six-gate reviewer must verify the version-pinned engine capabilities and source predicates, not infer a strategy-specific executed test.

## Sources

- Engine code https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Engine VERSION https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION
- Existing tests https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/test/hummingbot/strategy_v2/backtesting
- Existing six gates https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
