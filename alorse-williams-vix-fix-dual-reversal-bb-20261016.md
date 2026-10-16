---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Alorse Williams Vix Fix extreme-two-bar low-band long, inverse WVF upper-band exit"
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
  - https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/momentum/Williams%20Vix%20Fix.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alorse Williams Vix Fix extreme-two-bar low-band long, inverse WVF upper-band exit

Source pinned commit `8fb3837ddcd137f1450c3e82d654ff3df24d54d5`, exact file `strategies/momentum/Williams Vix Fix.pine` (read end-to-end): https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/momentum/Williams%20Vix%20Fix.pine

## Provenance and mechanism

Original Pine v4 combines **two successive bars of Williams Vix Fix stress**, a below-lower-price-Bollinger condition, and an upper-price-Bollinger exit; unlike existing `wvf-stochrsi-filtered-bottom`, no StochRSI enters this rule. Source default pyramiding0, initial 1000, 10% current equity, 0.01% commission. Long-only; exact source not a generic WVF cross.

## Signal — complete source-default calculations

- `src=close`, `bbl=20`, `mult=2.0`; price BB `basis=SMA(close,20)`, `upper/lower=basis ± 2*STDEV(close,20)`.
- `pd=20`; `lb=50`; `ph=0.85` from user input 85%, `pl=0.99` from 99%. `wvf[t]=100*(highest(close,20)-low[t])/highest(close,20)`; `upperBand[t]=sma(wvf,20)+2*stdev(wvf,20)`; `rangeHigh[t]=highest(wvf,50)*0.85`.
- `wvfInv[t]=100*(high[t]-lowest(close,20))/lowest(close,20)`; `upperBandInv=sma(wvfInv,20)+2*stdev(wvfInv,20)`; `rangeHighInv=lowest(wvfInv,50)*0.99`. These are calculated even if their default exit predicate is redundant.
- `buy = (wvf[t]>=upperBand[t] OR wvf[t]>=rangeHigh[t]) AND (wvf[t-1]>=upperBand[t-1] OR wvf[t-1]>=rangeHigh[t-1]) AND close[t]<lower[t]`. Note TWO consecutive WVF extreme bars and strict below price BB.
- Exact source `sellCond = (wvfInv<=upperBandInv OR wvfInv<=rangeHighInv) AND (wvfInv[t-1]<=upperBandInv[t-1] OR wvfInv[t-1]<=rangeHighInv[t-1]) AND close<upper ? false : true`; `sell = sellCond AND close>upper`; `strategy.close("Long",when=sell)`. **Logical reduction for finite non-Na inputs**: `close>upper` makes `close<upper` false, hence `sellCond=true` and exit exactly `close>upper`. Preserve the source code path and explicitly identify this redundancy, do NOT invent an inverse-WVF execution requirement.
- `strategy.entry("Long",true,when=buy)`. No short path, stop/TP order/trailing/time exit/cooldown/DCA, pyramiding0. Entry close<lower and exit close>upper are mutually exclusive. Warmup: highest(close,20), wvf 20-BB and max50, and its **previous-bar** value — conservative 72 completed bars flat (source-native built-in Na readiness after enough history, 72 researcher-defined fence). No future values, no security call; source next-open fill differs from research derivative next-close below.

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
