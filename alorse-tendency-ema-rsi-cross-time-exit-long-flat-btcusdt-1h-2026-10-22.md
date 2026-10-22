---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Alorse Tendency EMA10/20 cross + EMA100 rail RSI-gated time-exit long-flat spot derivative"
created: 2026-10-22
updated: 2026-10-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-22
sources:
  - https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/trend/Tendency%20EMA%20%2B%20RSI.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alorse Tendency EMA10/20 cross + EMA100 rail RSI-gated time-exit long-flat spot derivative

## Provenance

- Original program read in full, Pine v5: https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/trend/Tendency%20EMA%20%2B%20RSI.pine; source pinned to `Alorse/pinescript-strategies` `8fb3837ddcd137f1450c3e82d654ff3df24d54d5`, path `strategies/trend/Tendency EMA + RSI.pine` (56 lines, 2334 bytes, SHA-256 `7d351e0b5bb51f088f721afc5cf9c9b992f075500212d962caff77430dd20136`, GitHub blob `4b1d17e041dab62010961fe394cef2ba77c70384`, byte-identical by blob-hash check).
- Source declaration: `pyramiding=0`, `initial_capital=1000` USD, `default_qty_type=strategy.percent_of_equity`, `default_qty_value=10`, `commission_type=strategy.commission.percent`, `commission_value=0.1` percent per side. No `process_orders_on_close`, thus source's market orders fill next bar's **OPEN**.
- This is explicitly a **DERIVED EXECUTION strategy** using EXACT original signals/default long direction but spot BTC-USDT Binance 1h, one-bar-lag next-candle-CLOSE fills, fixed initial capital stake 100 USDT and 0.1% modeled research fee per side. Next-close differs materially from source next-open, fixed-stake differs from source 10% of *current* equity. These choices are researcher-declared, never disguised as original Pine trade fills.
- Dedup: no `main` record pins this file (exact `Tendency EMA` zero hits across all root records and all currently open `research/*` PRs). Nearest EMA-cross records (`ema-20-50-cross` 1h, `freqtrade-strategy001` HA EMA-cross 5m, `freqtrade-multima` TEMA-stack 4h, `eterna-sma-50-200` 4h) use different average lengths, regime rails, candle gates and exits. None has this source's **EMA10/20 cross + EMA100 rail + bullish-candle entry with RSI70-or-24-bar-in-profit exit**.

## Economic mechanism

### Source-reported

Trend-following golden-cross entry gated by a slow regime rail and candle direction; exits take overbought profit (RSI) or free capital from stale winners (in-profit time exit). The 56-line file carries no performance table, trade count, window, or cost-basis claim.

### Research interpretation

The EMA10/20 cross catches early trend legs while the EMA100 rail keeps trades on the dominant-trend side; the bullish-candle filter skips cross bars that already reversed intraday. The RSI>70 exit harvests overbought extensions; the 24-bar in-profit time exit releases dead capital only when green, never selling losers on the clock.

## Signal

Source defaults as-coded:

- Inputs pinned: RSI `len=14` on `src=close` (`rsi=ta.rsi(close,14)`); `len_a=10` (`out_a=ta.ema(close,10)`), `len_b=20` (`out_b=ta.ema(close,20)`), `len_c=100` (`out_c=ta.ema(close,100)`); `showLong=true`, `showShort=false`, `closeAfterXBars=true`, `xBars=24`.
- `entryLong[t] = crossover(out_a,out_b)[t] AND out_a[t]>out_c[t] AND close[t]>open[t]`, where crossover is true exactly when `out_a` moves from at/below `out_b` on completed bar t−1 to above on completed bar t.
- `exitLong[t] = (rsi[t]>70) OR (nPastBars[t]>=24 AND close[t]>entry_price)` (second arm active only because `closeAfterXBars=true` default is pinned).
- `entryShort`/`exitShort` are the mirror image, but `showShort=false` default means the only short order call can never fire; the record pins exactly the default long-flat version without inventing shorts.
- `bought[t] = (opentrades[t]==1 AND position_size[t]>position_size[t−1])`; `entry_price = ta.valuewhen(bought, open, 0)` — the open of the bar on which the position stepped up (source next-open fill bar's open). `nPastBars` increments each bar while `position_size!=0` and resets to 0 when flat.
- Orders: `strategy.entry('Long',strategy.long,when=entryLong and showLong)`; `strategy.close('Long',when=exitLong)`. No `strategy.exit` with stop/limit anywhere in the long branch: no stop-loss, no take-profit, no trailing, no separate time stop, no cooldown, no date-range gate. Repeated qualifying long entries while long are ignored via `pyramiding=0`; re-entry after flat on a later `entryLong` is allowed.
- Same-candle co-fire (`entryLong` and `exitLong` both true) is logically possible (cross-up bar with RSI already >70). Researcher execution semantics (disclosed, not source-claimed): exit is evaluated only when a position carried into the bar is held, entry only when flat; a co-firing candle resolves to the single state-consistent event (flat→enter, held→exit) with no same-row round-trip.

## Required data

- One `binance` spot `BTC-USDT 1h` historical OHLC series: EMA10/20/100 use close, RSI14 uses close, candle direction uses open/close. No multiple assets, multi-timeframe request, `security()` call, future-extrema, or lookahead input anywhere in the 56 lines.
- Conservative declared **150 fully completed candles** warmup for EMA100 seeding, RSI14 smoothing and t−1 crossover access; no decision before then. Source code itself computes built-ins as soon as they are non-na; the 150-bar flat warmup is an explicit researcher specification, not a claimed author default. Signals only after completed t; stored t signal evaluated on simulator row t+1, filled t+1 close. End-of-data unfilled events are not invented.

## Execution assumptions

- The same **existing** audited source-aligned Hummingbot benchmark path accepted for other source-specific spot derivatives, not a new service: `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, committed September 20 2026 at 12:10:22 UTC, and its `hummingbot/VERSION=dev-2.17.0`, consistent with mandated pinned package `20260920` / VERSION `dev-2.17.0`. Commit, VERSION, engine, simulator, data-provider and test files below were read/grepped live at this exact commit by this run; no test was executed.
- `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`: `BacktestingEngineBase.run_backtesting(...,backtesting_resolution,trade_cost)` over completed OHLCV, `simulate_execution()` iterating timestamp rows with `controller.determine_executor_actions()`; `CreateExecutorAction(OrderExecutorConfig)` routed to native `OrderExecutorSimulator` on the sliced row window. `BacktestPositionHold._process_order` nets buy/sell, tracks average cost and realized PnL; SELL of precisely held BTC closes exposure without naked short, no stop/limit intrabar fills required.
- `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` (read in full): `ExecutionStrategy.MARKET` fills at the first current simulation df row, `entry_price` = that row's CLOSE, fee `trade_cost×filled_amount_quote`, `CloseType.POSITION_HOLD` ledger.
- `BacktestingDataProvider` keyed `binance_BTC-USDT_1h` with `get_candles_df(connector,pair,interval,max_records)`; `initialize_trading_rules('binance')`, `quantize_order_amount`/`quantize_order_price` for venue increments. Reject missing actual candle/quantity below min-notional instead of imagining fills. The existing native market OrderExecutorConfig+CreateExecutorAction construction is illustrated by root-level `controllers/generic/pmm_mister.py`; **the Tendency EMA/RSI calculation implementation itself has not been written** and is not asserted to exist.
- Pre-existing tests at pinned commit, names verified present, **inspected, not newly run**: `test/hummingbot/strategy_v2/backtesting/test_backtest_position_hold.py` (`test_buy_sell_netting`, `test_full_netting_closes_position`, `test_netted_position_realized_pnl_in_summary`); `test_backtesting_final_tick_ledger.py` (final-tick POSITION_HOLD ledger accounting); `test_backtesting_engine_directional.py::test_backtest_directional` (representative signal->action->executor run). Modeled execution expressibility is narrower than live/perpetual execution realism.
- Account: 1000 initial USDT, one **fixed** 100 USDT BUY per position quantized to BTC base increment; exact filled quantity is sold at exit, flat between positions, no compounding. Source originally has 10% of varying equity; admitted derivation chooses fixed 10%-of-*initial*, openly different economic behavior. Mode is **spot**, thus no isolated perpetual margin, mark funding or liquidation to mock. Spot test model charges `trade_cost=0.001` per filled side (0.1%, same nominal source commission, **not** a claim of live fee tier); spread/slippage unmodeled, never claim realized futures funding.
- Future house BO/SO DCA, leverage or different pair/timeframe research is separately declared experiment; not an unstated component of this source signal or bounded spot derivative.

## Evidence

### Source-reported

Original complete 56-line Pine program provides default long-only EMA10/20 cross + EMA100 rail + bullish-candle entry, RSI70-or-24-bar-in-profit exit, `pyramiding=0`, 10%-of-equity sizing and 0.1%/side commission. No source profit or simulated performance claimed.

### Independently reproduced

No actual strategy trades or Hummingbot/Qlib parity generated by this admission. Real first-party engine sources and preexisting test files inspected at the exact version-matching commit cited; modeled execution expressibility is narrower than live/perpetual execution realism.

### Negative evidence

- Tendency does **not** enter on an EMA touch or on RSI alone; entry needs the strict cross-up plus rail plus green candle on the same completed bar.
- `showShort=false` makes the mirror cross a dead branch, not a SHORT; the time exit is conditional on profit (`close>entry_price`), not a hard 24-bar stop; there is no stop-loss, take-profit, trailing, or cooldown in the long branch.
- Source next-open fills and 10%-of-current-equity compounding differ from the explicitly defined execution-only spot derivative. DCA is not source-native.

## Falsification plan

Recompute EMA10/20/100 and RSI14 on completed 1h bars; assert entry exactly on cross-up bars with `out_a>out_c` and green candle inside no date gate; assert exit exactly on RSI>70 or (bars-held≥24 with close above derived fill); assert no pre-warmup (150-bar) signals, no short orders, no duplicate entries while held, sells of exact held quantity; assert co-fire candles produce the single state-consistent event. Measure Pine next-OPEN to HB next-CLOSE execution differences separately.

## Crypto portability

Original indicator has no BTC or author backtest-window hardcoding. Chosen spot BTC-USDT 1h only pins a reviewable concrete model. Tests at other assets/times are separate settings; perpetual house campaign costs/funding must be assessed independently.

## Limitations

No protective stop; a non-overbought sideways hold can persist until the in-profit time exit (or indefinitely while red). RSI>70 exits can cut strong trends early. Spot fee/slippage model is bounded and is not proof of live futures economics. No implemented strategy controller or actual backtest replay.

## Implementation status

`not-implemented`. GitHub research record only, no changes to Qlib/Hummingbot/n8n/strategy runner.

## Adoption boundary

`research-only`, `not-approved`; independent six-gate PASS required for this derived model, not a survivor, Testnet or Mainnet authorization.

## Related Wiki records

None.

## Sources

- Primary https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/trend/Tendency%20EMA%20%2B%20RSI.pine
- Engine code https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Engine version https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION
- Engine tests https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/test/hummingbot/strategy_v2/backtesting
- Admission contract https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
