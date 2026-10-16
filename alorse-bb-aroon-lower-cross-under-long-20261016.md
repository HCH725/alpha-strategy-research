---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Alorse BB + Aroon lower-band crossunder, Aroon-Up gated long-flat research derivative"
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
  - https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/mean-reversion/BB%20%2B%20Aroon.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alorse BB + Aroon lower-band crossunder, Aroon-Up gated long-flat research derivative

## Provenance

- Primary original program inspected end-to-end: https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/mean-reversion/BB%20%2B%20Aroon.pine, commit `8fb3837ddcd137f1450c3e82d654ff3df24d54d5`, file `strategies/mean-reversion/BB + Aroon.pine`, Pine v5.
- Source strategy: `pyramiding=0`, `default_qty_type=percent_of_equity`, `default_qty_value=100`, `commission_value=0.1` percent. No `process_orders_on_close`, thus source's market orders fill next bar's open; no calc-on-every-tick.
- This candidate is an **explicitly derived research EXECUTION version** of unchanged source signals. It chooses spot `BTC-USDT` on `binance` `1h` feed, causal t-to-(t+1)-CLOSE market fills, one fixed 100 USDT allocation of initial 1000 USDT, and a nominal model fee 0.1% per side. Spot and sizing/timing deviate from the original Pine percent-of-current-equity, original next-open fills and research venue. Never present as an author-native or economically equivalent backtest.
- Engine evidence anchored not to latest master but to existing `HCH725/hummingbot` commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`, dated 2026-09-20T12:10:22Z; its `hummingbot/VERSION` is **dev-2.17.0**, matching pinned Hummingbot VERSION and September-20 benchmark vintage. Full-source inspection and preexisting tests below. No user-supplied fill logs or image digest is invented.
- Distinct from existing Aroon oscillator (oscillator midline/rail two-sided) and Bollinger breakout family (price cross *above* band); this rule combines an unusual lower-band **crossunder**, prior-high recency filter and two independent exits. PR #238 is source-specific, not a duplicated strategy.

## Economic mechanism

Countertrend long after close breaks the lower Bollinger band, conditional on a recently printed rolling high. Source code intentionally enters on a down-cross rather than a recovery-cross; neither a generic dip-buy nor Aroon midline reversal is a valid substitute.

## Signal

Pinned source defaults:

- `src=close`, `lengthBB=20`, `mult=2.0`. `basis=SMA(close,20)`, `dev=2.0*STDEV(close,20)`, `upper=basis+dev`, `lower=basis-dev`.
- `lengthAr=288`; `AroonUP = 100*(highestbars(high,289)+288)/288`, where the highestbars result is the negative/nonpositive offset of the most recently observed window extreme. `AroonDown` is calculated but never used to trade.
- `Confirmation=90`, `Stop=70`.
- `Bullish[t]=crossunder(close,lower)` := `close[t-1]>=lower[t-1]` AND `close[t]<lower[t]`.
- `Bearish[t]=crossunder(close,upper)` := `close[t-1]>=upper[t-1]` AND `close[t]<upper[t]`.
- `entry[t] = Bullish[t] AND AroonUP[t]>90`; original `strategy.entry('Long', strategy.long, when=entry)`.
- `exit[t] = Bearish[t] OR AroonUP[t]<70`; original `strategy.close('Long',when=exit)`.
- Long-only; no live Short entry. No programmed price-stop, take-profit, trailing stop, time exit, cooldown, safety orders, cross-asset legs or portfolio add-ons. `pyramiding=0`, only one held long. Can re-enter after flat on the next signal.
- **Same-source-bar overlap handling (explicitly declared net-transition derivative):** both band crossunders could coexist on a large gap/moving bands. The state machine first checks whether it holds Long. If held and exit=true, schedule SELL full held quantity; if held and exit=false, stay long and suppress repeated entry; if FLAT and entry=true, schedule BUY; otherwise remain flat. A source `strategy.close('Long')` while flat is a no-op; an entry while already long is rejected by pyramiding=0. Thus even when entry and exit are both true, *flat→long* and *long→flat* are deterministic based on prior actual position, never create two simultaneous orders. This priority is a **researcher-declared state normalization**, not an undocumented Pine/market assumption. Signals unchanged, but execution is explicitly derived.

## Required data and point-in-time

- One symbol historical **completed** `open/high/low/close` candles from `binance BTC-USDT 1h` (open is used solely to compare against original next-open semantics, not source signal). Source indicators need close/high only and 289 complete high bars plus prior complete Bollinger value. Warmup 290 fully completed bars; no trading before the next signal bar.
- No request.security, multi-timeframe, provisional HTF, future price or non-OHLCV signal. For signal bar t use at most `close[t], high[t]` and earlier. At next available simulator bar `t+1`, execute the stored completed-t decision at its **close**; t+1's own signal is never used for that fill. No end-of-history phantom order.

## Execution assumptions — exact preexisting Hummingbot code path

- `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` has `hummingbot/VERSION=dev-2.17.0`. Specifically inspect `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`: `BacktestingEngineBase.run_backtesting(controller_config,start,end,backtesting_resolution='1h',trade_cost=0.001)`, `prepare_market_data` merges timestamped spot OHLCV, `simulate_execution` visits each row and routes controller `CreateExecutorAction(OrderExecutorConfig)` through `simulate_executor` to `OrderExecutorSimulator`. The trade_cost is an **explicit run input override**; generic default is different.
- `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`: `execution_strategy=MARKET` fills at first simulated df row's `close` with timestamp of that row; fee `trade_cost * amount_quote`; returns `POSITION_HOLD`.
- `BacktestPositionHold._process_order` in backtesting engine nets BUY and SELL against one spot long and carries average acquisition cost, quote turnover and realized PnL/fees; a SELL for exactly the held base amount flattens it, never opens short.
- `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` `get_candles_df` keyed by `binance_BTC-USDT_1h`; `initialize_trading_rules('binance')` and `quantize_order_amount` use actual Binance spot trade size increment. For any amount below min order notional or missing actual candle, omit that execution with explicit failure; no fake price, balance or automatic accept.
- This primitive's `OrderExecutorConfig(MARKET)` `CreateExecutorAction` already appears at `controllers/generic/pmm_mister.py` for existing controller actions. Here a strategy-specific controller's source-signal calculation **has not been implemented**, as allowed by `implementation_status: not-implemented`; the admission verifies the already-existing execution primitive, not a finished strategy implementation. No new DSL/registry/admission gate.
- Existing version-pinned tests at `test/hummingbot/strategy_v2/backtesting/test_backtest_position_hold.py`: `test_buy_sell_netting`, `test_full_netting_closes_position`, `test_netted_position_realized_pnl_in_summary`; `test_backtesting_final_tick_ledger.py` has Binance spot `OrderExecutorConfig`, POSITION_HOLD and final-row accounting cases. Tests inspected at this SHA but **not run** in this admission; no strategy-level backtest claimed.
- 1000 USDT starting research capital; 100 USDT entry notional, no compounding (source 100%-of-*current* equity is different and explicitly not modeled). Match exit BTC amount to actual filled/quantized BUY base quantity. Fixed `trade_cost=0.001` (0.1% one-way) chosen to numerically match original source's commission; not purported actual Binance taker fee or VIP tier. Spread/slippage/maker queue NOT modeled, and results not sold as real net PnL. Spot has no perpetual funding or liquidation, so missing historical futures funding is not silently entered as zero. House 3x/5x futures and BO6/SO6/SO6 DCA are *separate* potential research variants, not the admitted spot signal record.

## Evidence

### Source-reported

The full original Pine file supplies BB20/2, AroonUp288/90/70 and the down-cross entry and two exits. No independent backtest statistics or source-proven profitability claimed.

### Independently reproduced

No real backtest or execution parity run was performed. Version-aligned source code and preexisting tests are inspectable at the cited immutable SHA. Gate5 is a bounded research simulator expressibility statement, not an assertion about live fills or a particular binary digest.

### Negative evidence

The unusual lower-band crossunder is NOT changed to a common oversold recovery. Stop=70 is an Aroon exit threshold, not a price stop. `AroonDown` not active. The risk of overlap is handled by explicit state-dependent **single action**, not ignored. All original vs derived timing, capital and fill differences are disclosed.

## Falsification plan

For each completed bar: recalc both strict band-crossunders, AroonUP from the 289 high window, thresholds 90/70; assert source signal match and warmup 290. For the derived run, when flat enter only on source entry; when held exit on source exit, or hold; action from t fills at t+1 close and pays 0.001 each filled leg. Probe rare simultaneous entry/exit by adversarial band shifts to confirm net-state priority. Compare source Pine t+1 open fills separately and report divergence rather than calling it parity.

## Crypto portability

Signals depend on one OHLC market, not author's BTC daily backtest preference. 1h BTC-USDT spot is a bounded selected research variant; 4h/1d and other coin or futures/DCA runs require their own explicit market and cost assumptions rather than silent universal compatibility.

## Limitations

Source has no protective price stop; drawdown is unbounded until signal exit. Pinned simulator trade_cost does not include spread, actual funding, true maker depth or mark-price liquidation. No source-native next-open fill parity or deployed controller is asserted.

## Implementation status

`not-implemented`; no engine code, Qlib/n8n implementation, Testnet, or live trading was changed.

## Adoption boundary

`research-only`, `not-approved`. Six-gate reviewer is independent, PASS if supported for this explicitly derived spot version only; source-native economics and futures certification remain unclaimed.

## Sources

- Primary https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/mean-reversion/BB%20%2B%20Aroon.pine
- Engine https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Engine version https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION
- Existing test folder https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/test/hummingbot/strategy_v2/backtesting
- HB_READY contract https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
