---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Alorse Flawless Victory v1 Bollinger-1SD RSI14 pullback and upper-band exit"
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
  - https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/other/Flawless%20Victory.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alorse Flawless Victory v1 Bollinger-1SD RSI14 pullback and upper-band exit

## Provenance

Primary full Pine v4 code inspected at pinned 8fb3837ddcd137f1450c3e82d654ff3df24d54d5, `strategies/other/Flawless Victory.pine`: https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/other/Flawless%20Victory.pine. Original file credits Bunghole, collected in Alorse repository; do not misattribute sole authorship. Original strategy opens long with `pyramiding=0`, initial capital `100000`, `default_qty_value=100%` of equity, source commission not declared. The file contains THREE alternative variants `v1=true`, `v2=false`, `v3=false`. Only v1 is executable in default configuration; v2/v3 stop/target order blocks are unreachable by default. The 100%-equity source economics are **not** carried as a claim of equivalent research sizing.

## Economic mechanism

Long pullback below the price BB20 lower envelope (narrow 1 standard deviation) simultaneously with RSI14<42. Exit on *both* breakout above BB20 upper envelope and RSI14>70. Different from Alorse BB Winner candle-zone penetration and from baseline chartart dual joint-cross: these are **level** predicates and BB standard deviation is 1, not BB2.

## Signal and source-default state

- `v1=true`, `v2=false`, `v3=false`. `len=14`; RSI uses explicitly coded Wilder: `up=rma(max(change(close),0),14)`, `down=rma(-min(change(close),0),14)`, `rsi=down==0?100:up==0?0:100−100/(1+up/down)`. These edge branches matter and must remain.
- `length1=20`, `src1=close`, `mult1=1.0`; `basis1=sma(close,20)`, `lower1=basis1−stdev(close,20)`, `upper1=basis1+stdev(close,20)`.
- `RSILowerLevel1=42`, `RSIUpperLevel1=70`. `Buy_1=close<lower1 AND rsi<42`; `Sell_1=close>upper1 AND rsi>70` (strict comparisons).
- Only default active calls: `strategy.entry("Long",strategy.long,when=Buy_1)`, `strategy.close("Long",when=Sell_1)`. The second `v2` has BB17/1 and RSI42/76 with stop6.604%/TP2.328%, the `v3` has MFI and RSI with stop8.882%/TP2.317% — they are genuine OPTIONAL source variations but **disabled here**. Do not leak their SL/TP into v1.
- No source v1 stop, take profit, trailing, time exit, optional shorts, cooldown or DCA. Long only or flat. `pyramiding=0` suppresses duplicate entries. Can re-enter after flat without cooldown. Buy requires `close<lower1`, Sell requires `close>upper1`, mutually exclusive even when stdev=0.
- RSI and Bollinger warmup researcher-declared **40 complete bars** (source original may form earlier partial indicators, but no safe pre-warmup trades admitted); point-in-time current and past close only, no `request.security`, no repaint, no HTF, non-price data or future bars. The v1 trade decision uses no MFI/volume despite those unused display/optional variant calculations.

## Execution assumptions (explicit version-pinned, derived)

Scope: **spot** `binance BTC-USDT 1h`, no perpetual funding/leverage/liq. Exact signal at completed bar t, persisted then executed as a native simulator MARKET BUY/SELL at bar `t+1` CLOSE, not source Pine's `t+1` OPEN; t+1 signal cannot influence that fill. If no next candle exists, no order filled. One flat/long position; when a held long is signaled Sell, market SELL exactly held BTC amount. Fixed initial research capital 1000 USDT, fixed 100-USDT single entry, quantized to connector base increment and subject to minimum notional, no compounding; source initial 100000 and 100% varying-equity allocation are **explicitly not equivalent**. No source commission declared; the research derivative **sets** a frozen notional fee of 0.01% per filled order side (`trade_cost=0.0001`), without claiming original author fee or real exchange maker/taker tier. Slippage, spread, maker fills omitted and no backtest profitability claimed.

Engine: `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, 2026-09-20T12:10:22Z with `hummingbot/VERSION=dev-2.17.0`, matching mandatory 20260920 version snapshot, NOT latest master. Existing `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` `BacktestingEngineBase.run_backtesting(...backtesting_resolution="1h",trade_cost=0.0001)` -> completed OHLCV `prepare_market_data` -> per-tick `controller.determine_executor_actions()` -> `CreateExecutorAction(OrderExecutorConfig)` -> `simulate_executor()`. Existing `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` `ExecutionStrategy.MARKET` fills at first sim-row CLOSE and `trade_cost*notional`, returns `POSITION_HOLD`. `BacktestPositionHold._process_order` nets BUY/SELL and tracks cost/realized PnL; `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` validates Binance spot feed/trading rules and quantizes BTC quantity. `controllers/generic/pmm_mister.py` demonstrates native MARKET OrderExecutorConfig actions; **strategy-specific signal controller not yet implemented**.

Pinned pre-existing tests read (not run): `test/hummingbot/strategy_v2/backtesting/test_backtest_position_hold.py` BUY/SELL netting/complete close/realized summary tests; `test_backtesting_final_tick_ledger.py` spot Binance OrderExecutor POSITION_HOLD and final-tick accounting; `test_backtesting_engine_directional.py` representative Binance candles/actions and adjustable trade cost. No live fills, no actual experimental backtest, no binary digest proof, no unsupported futures economics. Independent reviewer must verify this exact bounded native path for Gate 5.

## Evidence

Primary source inspected end to end, source version v1 and disabled v2/v3 explicitly distinguished. No source backtest profit adopted or independently reproduced here. v1 is a separately reviewable original source-default variant, not v2/v3 cherry-picked by performance.

## Falsification plan

Assert RSI Wilder edge cases and BB20 ± one STD, entry when close<lower1 and RSI<42, exit only close>upper1 and RSI>70; no short, stop, TP, time, cooldown or v2/v3 leakage. Complete t signal -> t+1 CLOSE market fill, 0.0001 per side and equal-quantity netted SELL. Compare Pine next-open source prices and source 100% sizing separately; never claim direct event-price or profit parity.

## Crypto portability

No source hard-coded BTC daily requirement. 1h spot BTC-USDT is the bounded registered research derivative, not an assumption that author's source tested or recommended that combination. Futures/3x/5x/BO-SO DCA are separate downstream studies.

## Limitations

Source-default v1 has no protective stop; below-lower-BB+RSI oversold can compound paper drawdowns without guaranteed recovery. Fixed 100 USDT research notional vs source 100% equity changes PnL and must not be conflated. Spot simulation price model omits spread/slippage.

## Implementation status

`not-implemented`, no change to any live Hummingbot, Qlib, n8n or market.

## Adoption boundary

`research-only`, `not-approved`. PASS solely for independently reviewed expressible research derivative, not profitability or live trading approval.

## Sources

- Primary https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/other/Flawless%20Victory.pine
- Engine/version https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION
- Engine tests https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/test/hummingbot/strategy_v2/backtesting
- Policy https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
