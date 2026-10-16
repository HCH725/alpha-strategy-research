---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Alorse MACD12-26-9 crossover DMI14-gated, vStop20/2 trend-exit long-flat"
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
  - https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/momentum/MACD%20%2B%20DMI.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alorse MACD12-26-9 crossover DMI14-gated, vStop20/2 trend-exit long-flat

## Provenance

Source full Pine v4 at `Alorse/pinescript-strategies@8fb3837ddcd137f1450c3e82d654ff3df24d54d5` `strategies/momentum/MACD + DMI.pine`: https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/momentum/MACD%20%2B%20DMI.pine. Original `pyramiding=0`, initial 1000 USD, default 10% current equity, 0.01% nominal commission; `process_orders_on_close` absent and Pine default market fill next-bar OPEN. Author's comment “Works better on 3h,1h,2h,4h” is not a coded input, eligibility prerequisite or performance endorsement.

## Economic mechanism

Price MACD line crossing its signal confirms a momentum turn only if directional indicator DI+ exceeds DI−. A second bearish MACD/DI gate or trailing volatility-stop **crossunder** closes. Distinct from main's ordinary MACD-signal-cross reversal (no DMI gate, no volStop exit), and from other DMI winner streak rules.

## Signal — exact source semantics

- Source `[pos_dm,neg_dm,avg_dm]=dmi(14,14)`, where pos_dm = +DI14, neg_dm = -DI14, avg_dm = ADX14 (calculated but ADX not consulted for order gating). `[macd, macd_signal, macd_histogram] = macd(close,12,26,9)`; standard EMA12-EMA26 and EMA9 of spread. Histogram unused by orders.
- `length=20` ATR for stop-state, `src=close`, `factor=2.0`. Source's custom function `volStop(src,atrlen,atrfactor)` carries variables `var max=src`, `var min=src`, `var uptrend=true`, `var stop=0.0` across bars. `atrM=nz(atr(20)*2.0,tr)`; each bar `max:=max(max,src)`, `min:=min(min,src)` (original author variable names shadow built-in max/min in prose; derive with running extrema but don't change recurrence), `stop:=nz(uptrend?max(stop,max-atrM):min(stop,min+atrM),src)`, `uptrend:=(src-stop)>=0.0`. If `uptrend != nz(uptrend[1],true)`, reset extremes to current `src` and `stop := uptrend ? max-atrM : min+atrM`; output `[vStop,uptrend]`. Prior-trend branch matters, not an ordinary ATR stop-order.
- `tales = crossunder(macd,macd_signal) AND pos_dm<neg_dm` (the original nested conditional explicitly returns FALSE when same crossunder occurs and pos_dm>neg_dm; DI tie also false).
- `closeLong = tales OR crossunder(close,vStop)` with strict previous close>=previous vStop and current close<current vStop.
- `entryLong = crossover(macd,macd_signal) AND pos_dm>neg_dm`; `strategy.entry("long",true,when=entryLong)`. `strategy.close("long",when=closeLong)`.
- ONE long or flat; no short, no actual `strategy.exit` price-stop/target/limit/trailing order, no safety/scale-in/time exit/cooldown. Volatility-stop is a **signal-based market close on crossing**, not an intrabar order that would fill at threshold. `pyramiding=0`, held position ignores repeat longEntry; reentry eligible after flat on later signal.
- MACD bullish crossover and bearish crossunder are mutually exclusive, but the vStop crossunder can coincide with bullish entry, so explicit state-dependent **derived net-transition specification**: if held long and closeLong -> sell all, otherwise held no action; if FLAT and entryLong -> buy one, else flat. This models the source's `strategy.close` while flat as no-op and same-direction entry while long as no-op, and ensures one MARKET order per action tick; overlap not ignored.
- Single-timeframe completed OHLC (source ATR(true range) needs high/low/close, DMI needs HLC, EMA close). Researcher-declared conservative 120 complete bars flat warmup to stabilize EMA26/9, DMI14 and custom ATR20 stop-state recursion, not claimed as Pine user input. No request.security or lookahead.

## Execution assumptions — declared native Hummingbot SPOT research derivative

Original signal calculated at fully completed bar t, stored then a `binance` BTC-USDT spot MARKET order at the **next engine candle t+1 CLOSE** using prior signal only; NOT the original source Pine next-open fill. No future candle read at decision. Fixed initial 1000 USDT capital, BUY fixed 100 USDT stake (different from source's 10% current-equity), SELL exactly quantized filled BTC amount, no compounding; one long, no naked shorts, 0.01% one-way modeled fee via `run_backtesting(...,backtesting_resolution='1h',trade_cost=0.0001)` (not real Binance maker/taker fee guarantee), spread/slippage absent, no futures leverage/funding/liq in spot instrument. House 3x/5x DCA later is separate execution model.

**Pinned code evidence**: `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, dated 2026-09-20T12:10:22Z, `hummingbot/VERSION=dev-2.17.0` matches mandatory 20260920 version. `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` has completed-ohlcv `prepare_market_data`, per-tick `controller.determine_executor_actions` and `simulate_executor` routing `OrderExecutorConfig` to `OrderExecutorSimulator`; `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` simulates MARKET at first row CLOSE with `trade_cost*notional` and `POSITION_HOLD`; `BacktestPositionHold._process_order` nets BTC BUY/SELL and tracks realized PnL and fees; `BacktestingDataProvider` loads `binance_BTC-USDT_1h` candles, Binance trading rules, amount quantization. The already implemented `controllers/generic/pmm_mister.py` demonstrates native MARKET `OrderExecutorConfig` action. MACD+DMI signal calculation/controller is **not implemented**, not claimed as engine builtin.

**Version-pinned first-party tests inspected, not executed**: `test_backtest_position_hold.py` `test_buy_sell_netting`, `test_full_netting_closes_position`, `test_netted_position_realized_pnl_in_summary`; `test_backtesting_final_tick_ledger.py` native spot OrderExecutorConfig POSITION_HOLD and terminal record handling; `test_backtesting_engine_directional.py` Binance candle-driven action/engine fixture. No new program code, simulator, DSL or Gate. No strategy trade-by-trade results claimed.

## Evidence

Source Pine program read complete at SHA; full source signal variables and volStop recurrence preserved. No author's profit estimate carried and no independent backtest run performed. Engine evidence demonstrates static primitive, not actual binary digest.

## Falsification plan

Cross-check +DI/-DI against dmi14, MACD12/26/9 strict cross and custom recursive volStop20/2 with previous trend state. Test simultaneous closeLong/entryLong and held/flat single-action net decision. Delayed t->t+1 CLOSE fills, one-way cost 0.0001, quantity/balance rule checks, no source-native next-open equivalence claimed. Long must not close merely because price is below vStop absent **crossunder**.

## Crypto portability

No hard BTC/daily chart rule; researcher spot BTC-USDT 1h chosen to make one reviewable engine model. Futures/DCA/7-pair grid outside this declared derivative.

## Limitations

Pine uses `max` and `min` as mutable local series names and built-in function names. The record explicitly pins mathematical running extrema and their source update order; any Pine compile ambiguity must be independently checked, not silently substituted. No protected stop order; signal-only exit may incur slippage/gaps. Model one-way fee omits spread.

## Implementation status

`not-implemented`; no production or Hummingbot/Qlib/n8n changes.

## Adoption boundary

`research-only`, `not-approved`. All original trading predicates pinned; the bounded research execution deviations are disclosed and require independent six-gate PASS before merge.

## Sources

- Original https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/momentum/MACD%20%2B%20DMI.pine
- Native pinned version https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION
- Tests https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/test/hummingbot/strategy_v2/backtesting
- Policy https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
