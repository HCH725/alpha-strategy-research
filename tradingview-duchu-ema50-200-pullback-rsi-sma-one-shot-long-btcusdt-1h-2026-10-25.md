---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradingView duchu EMA50/200 pullback RSI14/SMA14 one-shot long-flat BTCUSDT 1h derivative
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-06-11
sources:
  - https://www.tradingview.com/script/gBAYGb5q-EMA-50-200-Pullback-RSI-SMA-RSI/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# duchu EMA50/200 pullback + RSI/SMA one-shot — independent executable research derivative

## Provenance

**Primary TradingView publication:** [EMA 50/200 Pullback + RSI/SMA RSI](https://www.tradingview.com/script/gBAYGb5q-EMA-50-200-Pullback-RSI-SMA-RSI/) by **duchu**, public open-source **indicator** (not an authored order-executing strategy), published **2025-06-11**, script ID **gBAYGb5q**; the author's public first-party description was directly inspected on **2026-10-25**. The full original Pine code and its exact revision bytes were **not** retrieved; this is not a source-native or lossless Pine reconstruction.

**Verified source-described concepts (not claims of exact Pine implementation):** EMA fast/slow defaults 50/200; a bullish EMA cross establishes a bullish trend; acceptable absolute EMA separation defaults to **0.4%–1%**; after a new trend the author waits for price to touch/cross EMA50; RSI length **14** crosses its RSI **SMA14** for bullish/bearish signals; only the first buy/sell signal after an EMA trend cross is issued. The author explicitly calls the publication a signal **indicator**, not a complete trading system. Source describes a bearish sell *signal*, not an executable long exit. No source-native stop, size, exchange, candle interval, fee, fill clock, RSI zero-denominator convention, pullback latch or cash accounting was independently established.

**Independent derived strategy, deliberately NOT attributed to duchu:** researcher defines (1) BTC-USDT Binance **spot 1h**, long/flat only; (2) explicit EMA SMA seeds, Wilder RSI seeds and precise EMA-distance denominator; (3) strict completed-bar EMA-cross epoch, pullback high/low-touch latch, subsequent RSI/SMA bullish crossover and one-shot consumption; (4) bearish RSI/SMA cross **or** loss of EMA bull regime as the *long exit* (the author's bearish indicator signal is not silently presented as a native exit); (5) no shorts, stops, targets, trailing or time exit; (6) fixed 0.001 BTC, single-position state, 250-bar warmup, no DCA/pyramiding and no immediate reentry within the same EMA epoch; (7) synthetic same-completed-bar-close MARKET fill, confirmed-executor handoff, and fee/cash assumptions detailed below. These researcher choices are part of this independent derivative, not claims about the author's indicator.

**Immutable research identity:** `TV:gBAYGb5q:duchu:2025-06-11:derived-v1:BinanceSpot:BTC-USDT:1h:EMA50-200:SMAseed:RSI14-Wilder-SMA14:pullback-touch:one-shot:close-MARKET:2026-10-25`. Changing market, timeframe, formulas, seed, signal order, fill, exit, state, size or costs creates a distinct candidate. No TradingView author backtest or profitability claim is imported.

## Economic mechanism

Research hypothesis: an EMA50-over-EMA200 bullish regime that has first experienced a completed-bar price retest of EMA50, followed by a fresh RSI14/SMA(RSI14,14) bullish cross while the two EMAs remain moderately separated, may express renewed trend momentum. Exit at loss of RSI relative strength or the EMA regime. This is a hypothesis, not an empirically verified alpha claim; unprotected gap/sideways losses are possible.

## Signal — complete deterministic derived specification

**Feed:** one Binance Spot BTC-USDT 1h OHLCV series with strictly increasing UTC candle-opening timestamps `T[t]`, exactly 3600 seconds apart, all candles completed. Require finite positive O/H/L/C, `H>=max(O,C)`, `L<=min(O,C)`, finite nonnegative V. Missing, duplicate, invalid, misordered, partially complete or non-contiguous bars **invalidate the run** before feature preparation: no forward fill, `dropna`-bridged signal, fabricated price or silent clock repair. No other market or data feed is read.

**Indexing:** `t=0` is first validated bar. `EMA_N` of close is undefined until `t=N-1`; at that bar initialize `EMA_N[t]=mean(C[0..N-1])`; for subsequent bars `EMA_N[t]=2/(N+1)*C[t]+(1-2/(N+1))*EMA_N[t-1]`. N is exactly 50 or 200. No centered windows, future observations or optimization.

**RSI14:** `delta[t]=C[t]-C[t-1]` for `t>=1`; gains `max(delta,0)`, losses `max(-delta,0)`. At `t=14`, initialize mean gain/loss using exactly `delta[1..14]`. Thereafter Wilder recurrence `avgG[t]=(13*avgG[t-1]+gain[t])/14`, likewise `avgL`. RSI = `100*avgG/(avgG+avgL)`; if both averages are zero RSI=50, if only loss zero RSI=100, if only gain zero RSI=0. `RSI_SMA14[t]` is arithmetic mean of 14 defined RSI values `RSI[t-13..t]`, first valid `t=27`. No hidden library indicator defaults.

**Edges:** `bull_cross[t] = EMA50[t-1] <= EMA200[t-1] AND EMA50[t] > EMA200[t]`; `bear_regime[t] = EMA50[t] <= EMA200[t]`. `rsi_up[t] = RSI[t-1] <= RSI_SMA14[t-1] AND RSI[t] > RSI_SMA14[t]`; `rsi_down[t] = RSI[t-1] >= RSI_SMA14[t-1] AND RSI[t] < RSI_SMA14[t]`. Exact equality is not a cross on the current bar. `distance[t] = 100*(EMA50[t]-EMA200[t])/EMA200[t]`, a positive percent only in a bullish regime; entry permits inclusive `0.4 <= distance <= 1.0`. The author's absolute-distance idea is restricted to the long-bullish leg; this denominator is researcher-defined.

**Warmup:** require at least **250 completed bars** before any actionable regime cross, pullback or order. At `t<250`, calculate indicators only; do not carry an unobserved pre-warmup bull epoch into trading. If bullish at bar 250 without a new `bull_cross` at or after bar 250, remain unarmed until a future fresh bullish cross. This explicitly discards earlier signals rather than peeking before the defined research window.

**One-shot state machine (all evaluated on completed bar t):**
1. Reconcile any previous pending MARKET order using the pinned-engine confirmed-fill procedure in Execution assumptions **before** this bar's decisions. If the expected confirmation is missing/mismatched, **halt** (do not infer a fill from a requested action or invent an order price). While any order remains pending, submit no new order.
2. At an actionable `bull_cross`, **only if FLAT with no pending order**, start a fresh bullish epoch: `armed=true`, `pullback_seen=false`, `used=false`, `cross_bar=t`. A cross is a setup, **not** a same-bar entry. A bull cross while LONG/pending is ignored for re-arming. Whenever `bear_regime` is true, disarm and clear the pullback latch. The next re-arm requires a *new* bullish cross after becoming FLAT.
3. While FLAT, armed, unused, `t>cross_bar` and `EMA50>EMA200`, set `pullback_seen=true` if `L[t] <= EMA50[t] <= H[t]` (completed-bar wick touches the current EMA; this precise wick rule and persistent latch are researcher choices). The latch remains set through subsequent bullish-regime bars. Only when `pullback_seen`, `rsi_up[t]`, and the inclusive EMA distance gate are all true **on the current completed bar**, request exactly one BUY. If RSI crossed earlier, wait for a *new* RSI crossover; no retroactive entry. Mark this epoch consumed on the BUY request; a failed/unconfirmed fill halts the run, never silently re-arms.
4. While LONG, the first bar with `rsi_down[t]` **OR** `bear_regime[t]` requests one full-position SELL. Exit has priority over any entry/arming logic. No same-bar SELL+BUY reversal. If LONG and a new bull cross occurs, no new BUY is allowed. After confirmed SELL, remain FLAT and consumed/disarmed until a later fresh bull cross.
5. FLAT exit flags are no-ops; LONG entry flags are no-ops. No short, negative exposure, pyramiding, safety order, DCA, shared-capital concurrency, fractional rebalance, time-based cooldown, stop-loss, take-profit, trailing stop, time limit or end-of-data forced close. The one-shot bullish-epoch rule is the only re-entry guard. An open LONG at end-of-data remains open and is marked to the final observed valid close.

## Required data and causality (Gate 6)

Single 1h spot feed, historical completed bars only. The Binance REST candle timestamp is the **bar open** (verified `row[0]` in pinned `BinanceSpotCandles._parse_rest_candles`), so the **economic decision and model close-fill effective time** are `T[t]+3600s`, never `T[t]`. The pinned backtester uses `T[t]` as a row index and its MARKET simulator fills at that row's close; this is a **synthetic same-close research convention**, not a claim that a real trader could observe the close and then transact at the already completed historical close. No intrabar high/low is used for stop fills: the wick touch is only a **bar-completion signal predicate**. No repainting, negative shifts, future extrema, full-sample normalization, higher-timeframe partial bar or future price. The bar at which a pullback is recognized cannot be traded before its close.

## Execution assumptions — pinned real Hummingbot model (Gate 5)

**Policy pin:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`; bounded executable source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. The package-to-commit correspondence was **independently verified in merged Alpha PR #414** (wheel SHA-256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148`, 902/902 shipped Python files matched); this Scout cites that prior independent evidence and **did not rehash the wheel**. The pinned source `setup.py` uses a different version literal `20260729`, so the label is not independently re-established here. All engine paths below were **directly read via connected GitHub** at the immutable commit this cycle:

- `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` blob `6d505dff42b60b356931df13eeeecd1e28b426f9` explicitly includes `1h`; `binance_spot_candles.py` blob `5d0c938af574aca5f8dcba5ba28121797eae4dd0` maps `BTC-USDT` to `BTCUSDT` and reads REST open-time/OHLCV. `BacktestingEngineBase.prepare_market_data` copies `open_bt/high_bt/low_bt/close_bt/volume_bt` into the simulation rows, uses an epoch timestamp index, and drops NaNs. Therefore continuity/validity is checked **before** entering that function, never inferred from its `dropna`.
- `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` blob `7d1e552dd7ee62df4f83f10950b8d593cd1106e6`: `simulate_execution` performs `update_state(row)` then `controller.determine_executor_actions()` and routes `CreateExecutorAction` to `OrderExecutorSimulator`. The `OrderExecutorConfig` at `hummingbot/strategy_v2/executors/order_executor/data_types.py` blob `67715e3d14a1edf636defa95a7bbe5c73b8cff90` supports `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=BUY/SELL`, `amount=Decimal("0.001")`, `execution_strategy=MARKET`, `price=None`, `leverage=1`; no position-executor barrier is requested.
- `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` blob `3b4e82e91896db9074295ca2a8a087dde2499eab`: MARKET fills at the first provided candle's **close**, records `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, `current_position_average_price=close`, terminates as `CloseType.POSITION_HOLD`. `executor_simulator_base.py` blob `f77fc6104aef554b8ce7484481015311da1222a5` exposes that filled amount, side, status, close type and timestamp through `get_executor_info_at_timestamp`.
- **Load-bearing confirmed-fill handoff:** instantiate the existing `BacktestingEngineBase(terminated_executors_window=None)` (this constructor parameter is present in the pinned source). Do **not** use its default `3600s` terminated-executor visibility window: at a 1h or slower cadence it can hide a filled executor before the controller reads it. With `None`, `_reset_simulation_state` sets the bounded-view deque to `None`, `_record_terminated_executor` appends to `stopped_executors_info`, `_prune_terminated_executors_view` returns without pruning, and `update_executors_info` hands the controller the full terminated ledger. At the **next** completed-bar tick after a requested BUY or SELL, match the unique submitted `OrderExecutorConfig.id` in `controller.executors_info` with `status=TERMINATED`, `close_type=POSITION_HOLD`, matching side, `filled_amount_quote>0`, expected fill-row index/close and full Q; **only then** transition BUY_PENDING→LONG or SELL_PENDING→FLAT and book cash. This is a specified **existing engine configuration and path**, not a new checker/controller service or assumption that a requested action equals a fill. A missing, mismatched or partial confirmation halts research. The controller must never rely on the lagging `controller.positions_held` list as the authoritative next-bar position state; the `_pending_position_hold_executors` queue is only converted at the following update. The existing `BacktestPositionHold.add_executor` nets the subsequent opposite-side SELL against the BUY, recording gross realized PnL and separate fees.
- **Cash/cost ledger:** start with 10,000 USDT unborrowed cash, zero BTC, single symbol/strategy. Research `trade_cost=0.001` per side (assumed, **not** claimed as actual exchange fee). Before BUY require `cash >= 0.001*C[t]*(1+0.001)`; otherwise skip this entry signal and consume its epoch (no order). On confirmed BUY debit `Q*fill_close + confirmed_cum_fees_quote`; on confirmed SELL credit `Q*fill_close - confirmed_cum_fees_quote`. While LONG, equity = cash + Q*last_valid_close; after SELL equity = cash. Cross-check confirmed fill price/fee against the simulator's model; mismatch halts. Engine gross PnL labels are not net-of-fee equity. Spot funding and perpetual margin/funding are **not applicable**, not modeled as hypothetical zero perpetual funding. Research slippage=0, full-size close fill, no lot/tick rounding and no order-book depth model are explicitly **synthetic**; exchange precision, true fees, latency, partial fills and real execution are unverified and **not** claimed supported for live trading.
- At final simulated row, `simulate_execution` performs a final terminated-executor ledger flush. Reconcile final outstanding pending order against this returned ledger for final accounting only; no extra strategy decision or fabricated exit. The above `None` setting uses the pinned engine's own supported path; it may have a larger memory cost for many trades, but introduces no new component. No multi-asset sync, non-OHLCV input, next-open, maker, intrabar fill or futures capability is required.

## Six-gate assessment — proposed PASS, independent review required

1. **Determinism:** exact EMA/RSI seed and recurrence, distance denominator, crossing comparisons, pullback latch, order of operations, warmup and fixed parameter set above; no model training or tuning.
2. **Direction:** Binance BTC-USDT unlevered spot LONG/FLAT; SHORT explicitly disabled.
3. **Entry/exit/risk:** one-shot EMA epoch + completed wick-touch + RSI-up + EMA distance entry; RSI-down or bearish EMA regime exit; stops/targets/trailing/time exits all explicitly disabled; no hidden default barriers.
4. **State:** FLAT/BUY_PENDING/LONG/SELL_PENDING, unique order-ID confirmation, one 0.001 BTC position, epoch consumption, no DCA, pyramiding, cooldown or simultaneous orders; pending/missing fill handling defined.
5. **Pinned engine:** immutable package/version evidence, actual spot 1h data, MARKET OrderExecutor close-fill, executor-info handoff with `terminated_executors_window=None`, opposite-side position netting, explicit synthetic fee/cash/equity and no futures-funding assumptions; the **default** 3600-second window is specifically excluded.
6. **Causality:** 250 complete-bar warmup, no pre-warmup arming, effective close timestamps, only current/past OHLCV, no missing-data fabrication or future bar reads.

**Status interpretation:** `hb_ready_status: PASS` is this researcher's six-gate expressibility **proposal**, subject to independent Hermes Auditor exact-head review; it is not self-approved, source-native, Qlib parity, survivor, profitable, Hummingbot Certified, or Paper/Testnet/Live authorized. No dedicated controller or executable Qlib recipe is claimed implemented.

## Evidence, deduplication and limitations

**Source evidence:** directly inspected TradingView first-party publication/author/date and its written 50/200 EMA, 0.4%–1% distance, EMA touch, RSI14/SMA14 cross, one-signal-per-regime concepts. Full Pine unavailable; exact Pine native behavior, source-native fees/position/fills, and all author performance are **not verified**. This candidate's exact execution/indicator variants and bearish-signal-as-exit are **researcher-defined** and disclosed; no original strategy performance was independently reproduced.

**Engine evidence:** directly inspected pinned GitHub source blobs listed above; previously merged independent wheel/source verification in [Alpha PR #414](https://github.com/HCH725/alpha-strategy-research/pull/414). No strategy backtest, synthetic-performance claim, Qlib/Hummingbot event parity, wheel rehash, container operation or trading was performed.

**Dedup snapshot:** current `main@815d33dbbfd3d1209310acb252e07401c71602a0` has 331 root strategy records, README count 331. Independent Hermes audit of prior `main@40620f2fd55bd2836540659bfdb7768cf3f68205` found 330/330 PASS; connected GitHub compare shows the only later changes were the independently reviewed new PASS Strategy-2 ETH record and the README counter update. Current new record's frontmatter was read and is PASS; no non-PASS strategy admission is inferred from numeric counts alone. GitHub code search on current main for exact TradingView ID `gBAYGb5q` and author `duchu` returned no records; title/EMA50/200+RSI-SMA pullback search found no same signal-state rule. Open `research/*` PRs were enumerated and none cites this TradingView source or this EMA-distance-gated, latched-pullback, one-shot RSI/SMA crossover mechanism. Similar EMA/RSI trend records differ in source, trigger ordering, pullback latch, distance filter and exit. No legacy or admission exception is requested.

**Limitations:** independent derived research hypothesis; author Pine not accessible; close-only MARKET simulation is not live-realizable post-candle fill; actual exchange costs, liquidity, precision, partial fills, slippage and latency are unknown. This does not prove profitability or Qlib parity. No Qlib/Hummingbot backtest, trading, deployments or pipeline modifications were performed.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review alone owns source-fact remediation, exact-head PASS merge, or NOT_LOSSLESS close. Scout does not approve, merge, close or write main/README.

## Sources

- TradingView primary source: https://www.tradingview.com/script/gBAYGb5q-EMA-50-200-Pullback-RSI-SMA-RSI/
- Pinned Hummingbot engine source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independent wheel-to-source verification: https://github.com/HCH725/alpha-strategy-research/pull/414
