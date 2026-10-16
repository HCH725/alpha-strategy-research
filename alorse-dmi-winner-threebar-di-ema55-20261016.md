---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Alorse DMI Winner triple DI dominance / ADX13 / EMA55 long-flat spot derivative"
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
  - https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/momentum/DMI%20Winner.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alorse DMI Winner triple DI dominance / ADX13 / EMA55 long-flat spot derivative

## Provenance

- Original program read in full, Pine v5: https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/momentum/DMI%20Winner.pine; source pinned to `Alorse/pinescript-strategies` `8fb3837ddcd137f1450c3e82d654ff3df24d54d5`, path `strategies/momentum/DMI Winner.pine`.
- Source declaration: `pyramiding=0`, initial_capital 1000 USD, `percent_of_equity=20`, commission 0.01% per side, no process_orders_on_close, default market execution next bar's **OPEN**. Author date gate Feb 2021 to Feb 2099 is a backtest-window setting, not strategy timeframe.
- This is explicitly a **DERIVED EXECUTION strategy** using EXACT original signals/default long direction but spot BTC-USDT Binance 1h, one-bar-lag next-candle-CLOSE fills, fixed initial capital stake 200 USDT and 0.01% modeled research fee per side. Next-close differs materially from source next-open, fixed-stake differs from source 20% of *current* equity. These choices are researcher-declared, never disguised as original Pine trade fills.
- Current main `dmi-swings-contrarian-adx` and `adx-di-cross-strength-gated` trade different DMI rules. Neither has this source's **three consecutive DI dominance and ADX>23 + EMA55 + candle-color** entry with inverse full short condition exit. Earlier PR #239 rejected missing engine evidence, not signal formula; this fresh head pins the existing supported capability.

## Economic mechanism

Trend-continuation confirmation: three bars of consistent upward DI dominance and ADX trend intensity above 23, price above EMA55 and a bullish candle. Long remains open until a complete reverse-direction three-bar DI and EMA/candle filter event, not until any simple DI line crossing.

## Signal

Source defaults as-coded:

- DMI `[diplus,diminus,adx] = ta.dmi(len=14,lensig=13)`; `keyLevel=23`, check **strict** `adx>23` at completed candle t.
- `src=close`; `hasMa=true`, `maType='EMA'`, `maLen=55`, thus `ma=EMA(close,55)`; if `hasMa` were false, filters would become unconditional, but default true is pinned. Optional SMA instead of EMA is not included.
- `longCond[t] = (DI+[t]>DI−[t]) AND (DI+[t−1]>DI−[t−1]) AND (DI+[t−2]>DI−[t−2])`.
- `shortCond[t] = (DI+[t]<DI−[t]) AND (DI+[t−1]<DI−[t−1]) AND (DI+[t−2]<DI−[t−2])`.
- `longEntry[t] = longCond[t] AND adx[t]>23 AND close[t]>EMA55[t] AND close[t]>open[t]`.
- `shortEntry[t] = shortCond[t] AND adx[t]>23 AND close[t]<EMA55[t] AND close[t]<open[t]`.
- `showLong=true`, `showShort=false`; source's default branch is `if showLong and not showShort and inDateRange: strategy.entry('Long',strategy.long,when=longEntry); strategy.close('Long',when=shortEntry)`. Thus inverse `shortEntry` is solely the **long EXIT condition**, not a short order. The record represents exactly the source default long-flat version, without inventing shorts.
- Source `startTime=timestamp("Feb 01 2021 23:59:59")`, `endTime=timestamp("Feb 01 2099 23:59:59")`: inDateRange gates BOTH source order calls. Record keeps this date eligibility; full-history research may independently declare a different test window but must label the variant, not pretend the source didn't gate it.
- `useSL=false` default, so Long 10% price stop `strategy.exit('Stop Loss','Long',stop=avg_price*0.9)` is NOT active; this code's stop exists *only* if toggled on. Short-side stop not in source. No active source TP, trailing, separate time exit, safety order, cooldown or pyramiding. Repeated qualifying long entries while long = ignored via `pyramiding=0`; reentry after flat on a later longEntry allowed.
- Entry and exit on the same bar are impossible: DI+[t]>DI−[t] contradicts DI+[t]<DI−[t]. Hold state therefore has only one event per source signal candle.

## Required data / causality

- One `binance` spot `BTC-USDT 1h` historical OHLC series: DI/ADX uses high,low,close (Wilder RMA smoothing), EMA55 uses close, candle direction uses open. No multiple assets, multi-timeframe request, future-extrema or security/lookahead.
- Conservative declared **100 fully completed candles** warmup for EMA55 and RMA14/ADX13 smoothing and t−2 access; no decision before then. Source code itself defines calculations as soon as built-ins are non-na; 100-bar flat warmup is an explicit researcher specification, not a claimed author default. Signals only after completed t; stored t signal evaluated on simulator row t+1, filled t+1 close. End-of-data unfilled events are not invented.
- On each engine row, if flat and previous completed source candle longEntry, buy once; if held and previous source candle shortEntry, sell all; otherwise hold. A signal while flat that would close is a no-op; duplicate entries suppressed. No co-firing and no ambiguity.

## Execution assumptions — reused pinned Hummingbot native path

- The same **existing** audited source-aligned Hummingbot benchmark path accepted for another source-specific spot derivative, not a new service: `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, committed September 20 2026 at 12:10:22 UTC, and its `hummingbot/VERSION=dev-2.17.0`, consistent with mandated pinned package `20260920` / VERSION `dev-2.17.0`. Static source evidence, not claim of image digest or test execution.
- `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`: `BacktestingEngineBase.run_backtesting(...,backtesting_resolution="1h",trade_cost=0.0001)` over completed OHLCV, `simulate_execution()` iterating timestamp rows with `controller.determine_executor_actions()`; `CreateExecutorAction(OrderExecutorConfig)` routed to native `OrderExecutorSimulator`.
- `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`: `ExecutionStrategy.MARKET` fills at the first current simulation df row CLOSE with cost `trade_cost×filled_amount_quote` and `POSITION_HOLD` ledger.
- `BacktestPositionHold._process_order` nets buy/sell, tracks quantity, realized PnL, average cost and fees. SELL of precisely held BTC closes exposure without naked short, no stop/limit intrabar fills required.
- `BacktestingDataProvider` keyed `binance_BTC-USDT_1h`; `initialize_trading_rules('binance')`, `quantize_order_amount` for spot quantity. Reject missing actual candle/quantity below min-notional instead of imagining fills. The existing native market OrderExecutorConfig+CreateExecutorAction construction is illustrated by `controllers/generic/pmm_mister.py`; **the DMI calculation implementation itself has not been written** and is not asserted to exist.
- Pre-existing test source at pinned commit: `test/hummingbot/strategy_v2/backtesting/test_backtest_position_hold.py` has `test_buy_sell_netting`, `test_full_netting_closes_position`, `test_netted_position_realized_pnl_in_summary`; `test_backtesting_final_tick_ledger.py` tests spot Binance OrderExecutor POSITION_HOLD and end-row ledger, and `test_backtesting_engine_directional.py` validates representative perpetual signal->action->executor and adjustable trade_cost. They were inspected, **not newly run**.
- Account: 1000 initial USDT, one **fixed** 200 USDT BUY per position quantized to BTC base increment; exact filled quantity is sold at exit, flat between positions, no compounding. Source originally has 20% of varying equity, admitted derivation chooses fixed 20%-of-*initial*, openly different economic behavior. Mode is **spot**, thus no 3x/5x isolated perpetual margin, mark funding or liquidation to mock. Spot test model charges `trade_cost=0.0001` per filled side (0.01%, same nominal source commission, **not** a claim of live fee tier); spread/slippage unmodeled, never claim realized futures funding.
- Future house BO/SO DCA, leverage or different pair/timeframe research is separately declared experiment; not an unstated component of this source-native signal or bounded spot derivative.

## Evidence

### Source-reported

Original complete Pine program provides default long-only DI dominance, ADX/EMA/candle gates, optional long stop off and inverse condition exit. No source profit or simulated current performance claimed.

### Independently reproduced

No actual strategy trades or Hummingbot/Qlib parity generated by this admission. Real first-party engine sources and preexisting test files inspected at the exact version-matching commit cited; modeled execution expressibility is narrower than live/perpetual execution realism.

### Negative evidence

- DMI Winner does **not** enter on a single DI cross; it requires three contemporaneous/past bar signs and a full combination.
- `showShort=false` makes the mirrored shortEntry a long close, not a SHORT. Optional `useSL=false` leaves no active stop; stop is **not** implicitly on.
- Source next-open and 20%-equity sizing differ from explicitly defined execution-only spot derivative. DCA is not source-native.

## Falsification plan

Compare DMI14/ADX13/EMA55 on complete bars to Pine; assert entry exactly 3 consecutive DI+ wins AND ADX>23 AND close>EMA55 AND bullish candle in source date range; exit mirrors full bearish predicate, not DI-only. Derived market action strictly on next candle t+1 CLOSE, cost 0.0001/leg, sell actual BTC balance; no short orders, no duplicate long, no pre-warmup or after source date window entry; measure Pine next-OPEN to HB next-CLOSE execution differences separately.

## Crypto portability

Original indicator has no BTC or author's daily backtest hardcoding. Chosen spot BTC-USDT 1h only pins a reviewable concrete model. Tests at other assets/times are separate settings; perpetual house campaign costs/funding must be assessed independently.

## Limitations

No default protective stop; adverse hold risk until a fully qualified mirror shortEntry. Source can stay long for long time if EMA/candle filter blocks exit. Spot fee/slippage model is bounded and is not proof of live futures economics. No implemented strategy controller or actual backtest replay.

## Implementation status

`not-implemented`. GitHub research record only, no changes to Qlib/Hummingbot/n8n/strategy runner.

## Adoption boundary

`research-only`, `not-approved`; independent six-gate PASS required for this derived model, not a survivor, Testnet or Mainnet authorization.

## Sources

- Primary https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/momentum/DMI%20Winner.pine
- Engine code https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Engine version https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION
- Engine tests https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/test/hummingbot/strategy_v2/backtesting
- Admission contract https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
