---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Alorse BB Winner LITE candle penetration gate long-flat"
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
  - https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/mean-reversion/BB%20Winner%20LITE.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alorse BB Winner LITE candle penetration gate long-flat

Source pinned commit `8fb3837ddcd137f1450c3e82d654ff3df24d54d5`, exact file `strategies/mean-reversion/BB Winner LITE.pine` (read end-to-end): https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/mean-reversion/BB%20Winner%20LITE.pine

## Provenance and mechanism

Original program Pine v4; `strategy("Bollinger Bands Winner LITE [Alorse]")`, pyramiding=0, source size `10% equity`, `initial_capital=1000`, source commission 0.01%. Source code includes optional `showShort=false`, i.e. default is **long-flat**, not two-sided. Draw-only `isBB=true`, `offset=0`, `version=1.0.4` have no impact on trading. Research derivative changes only venue, sizing and fill timing disclosed in Execution below.

**Entry isn't any lower Bollinger touch:** it picks a candle range penetration point below lower BB and excludes a deeper *body-based* penetration point. This is distinct from existing Bollinger threshold breakout long and from other Alorse BB+Aroon down-cross.

## Signal — original strict rules

- `src=close`; `length=20`; `mult=2.0`. `basis=sma(close,20)`, `dev=2*stdev(close,20)`, `upper=basis+dev`, `lower=basis-dev`.
- `candleper=0.30` (input 30 percent), `candle_size=high-low`, `buyzone=low+(high-low)*0.30`, `sellzone=high-(high-low)*0.30`.
- `body_size=abs(close-open)`; `bs60=body_size*0.6`; `bsBuy=low+bs60`, `bsSell=high-bs60` (bsSell calculated but **unused** by active orders).
- `buy=(buyzone<lower) AND NOT(bsBuy<lower)` (**strict** lower tests), so buyzone must be below BB lower and bsBuy >= lower; no candle-color filter exists.
- Default `showShort=false`: `strategy.entry("Long", true, when=buy)`; `strategy.close("Long",when=sellzone>upper)`. Optional `showShort=true` would instead **remove the default Long exit** and add a Short entry on `sellzone>upper` — that is *not* default, not part of this record.
- No SL/TP order, stop/trailing, forced time exit, cooldown or DCA in source; at most one position, re-enter after flat. Entry and exit may coexist if a wide bar straddles both bands. **Explicit derivative net-state decision**: if previously Long and sellzone>upper then SELL; else if flat and buy then BUY; otherwise HOLD (simultaneous overlap is resolved from previous position, never both orders). While long other BUY ignored; while flat a `strategy.close` does nothing.
- Warmup 20 completed OHLC bars, sufficient for BB20 and current candle body/range. No request.security, HTF or repaint dependency. Source fill next-bar-OPEN, disclosed next-bar-CLOSE derivative below.

## Required data, point-in-time and execution

This candidate is an **explicit execution derivative**, not a source-native Pine execution clone. Venue `binance` spot `BTC-USDT`; decision candles `1h` (author's backtest timeframe never filters strategy admission). Compute every source indicator from **completed candle t** with no partial bar and apply the stored t signal to MARKET order on the following simulator row **t+1 at CLOSE**, not at Pine's native next-bar OPEN. No t+1 input is read by t's signal; no phantom fill at end of history. No futures contract, liquidation, leverage, historical perpetual funding or hidden DCA. One held long at maximum; no shorts or over-allocation; exit SELL equals actual filled BTC quantity. Start capital 1000 USDT; 100 USDT fixed notional BUY (10% initial capital, no compounding), distinct from author's dynamic percent-of-equity sizing, explicitly derived. `BacktestingEngineBase.run_backtesting(controller_config,start,end,backtesting_resolution="1h",trade_cost=0.0001)` uses one-way 0.01% fixed fee as *research approximation* numerically matching the source commission when supplied; not an asserted Binance real fee tier, spread, or maker execution. Quantize BTC amount to actual connector base increment and skip invalid min-notional orders, never fill synthetic prices.

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
