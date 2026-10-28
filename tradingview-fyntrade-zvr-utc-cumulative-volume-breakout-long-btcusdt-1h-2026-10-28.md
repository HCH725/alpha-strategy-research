---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Zanger Volume Ratio UTC time-normalized cumulative-volume breakout — independent BTC-USDT spot 1h long-flat derivative"
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
status: research-only
confidence: medium
source_as_of: 2025-07-08
sources:
  - https://www.tradingview.com/script/hckcY7Dp-Zanger-Volume-Ratio-ZVR/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ZVR time-normalized cumulative-volume breakout — independently derived BTC-USDT 1h research strategy

## Provenance

**Public primary source checked 2026-10-28:** TradingView [Zanger Volume Ratio (ZVR)](https://www.tradingview.com/script/hckcY7Dp-Zanger-Volume-Ratio-ZVR/), author **fyntrade**, first published 2025-02-06, updated **2025-07-08**, public stable script ID **hckcY7Dp**. Its description credits original related work by **The_Peaceful_Lizard**, describes cumulative volume so far in a session divided by historical average cumulative volume for a matching elapsed period (default **20 days**), and says the July update supports non-intraday frames. A reading of 200% represents 2x the same-time historical baseline. This source is an **indicator**, not a published entry/exit strategy. The full Pine bytes, session anchoring specifics, warmup implementation, and numerical source-code parity were **not retrieved or verified**; none are asserted.

**Independent executable derivative, not source-native/lossless:** Preserve only the **time-of-day-aligned session cumulative-volume ratio** concept and 20-prior-day comparison. Researcher-defined additions are: UTC calendar-day sessions for 24/7 crypto, Binance BTC-USDT **spot 1h** base-asset volume, price breakout above the prior 20 hourly highs, 200% newly-crossed ZVR entry threshold, long-only posture, stop at a completed close 3% below actual modeled entry, SMA20-close exit, maximum 24-bar hold, fixed 0.001 BTC size, 10,000 USDT starting cash, no leverage, modeled MARKET close fills, fees, and exact failure handling. These are proposed research choices, **not rules or proven performance from Dan Zanger or fyntrade**; unlike the original display-only indicator, this derivative generates orders.

**Frozen identity:** `TV:hckcY7Dp:fyntrade:2025-07-08 | independent-ZVR-derived-v1:2026-10-28 | BinanceSpot:BTC-USDT:UTC1h | L=20 prior UTC days same elapsed hour; reset 00UTC | ZVR cross from <200% to >=200% within same UTC day | close>max(prior20 high) | LONG/FLAT | close stop 0.97x entry or close<=SMA20 or age>=24 | Q=.001 BTC | close-only MARKET model | fee=.001 per filled side | 480h warmup`. Changing any timing/session boundary, feature definition, trigger, state, risk or execution convention creates a different derivative identity.

**Dedup performed 2026-10-28:** Connected GitHub main searches for `Zanger Volume Ratio`, `ZVR`, and `pacing` yielded no materially identical strategy record; searches for `cumulative volume`, `RVOL`, and volume breakout find different indicators. Open PR search for `Zanger` returned none. Related admitted systems are `forven-atr-volume-breakout-long-flat-ethusdt-1h-2026-10-17.md` (ATR/Donchian + volume versus recent 20 *bars*), `dual-ema-engulfing-volume-long-btcusdt-1h-2026-10-07.md` (EMA engulfing + volume), `tradingview-vlenarcic-volume-cci-stoch-vwap-cross-long-btcusdt-4h-2026-10-25.md` (session VWAP plus CCI/Stoch of volume), and `donchian-20-10-breakout-btcusdt-1h-2026-10-06.md` (price-only channel). None uses **today's UTC-day cumulative volume divided by the previous 20 days' same-elapsed-hour cumulative volume**, so this is a materially distinct participation-normalization mechanism, not a trivial threshold tweak. No claim of an exhaustive whole-repository byte-for-byte census is made.

## Economic mechanism

### Source-reported

The source explains that a high ZVR reveals participation unusually strong **for the current time of day**, rather than treating any large early-session raw volume as abnormal. This alone supplies no directional edge, trade, risk plan, or evidence of crypto profitability.

### Research interpretation

Hypothesis only: require a *fresh* time-normalized cumulative volume expansion of at least 2x on the same completed hourly candle as a close above the prior 20-hour price high. This is expected to test whether exceptional participation corroborates a short-horizon breakout. A 24-hour maximum hold constrains the intended horizon. There is **no measured expectancy or success claim**.

## Signal

**Complete, researcher-defined version v1:**

1. Read a **single** strictly chronological Binance BTC-USDT spot **UTC-aligned 1h** OHLCV sequence, with candle **opening** epoch timestamp `T[t]` and actual real `O[t],H[t],L[t],C[t],V[t]` (volume in base BTC). Exact consecutive open spacing **3600 seconds**, UTC hour/minute alignment, positive finite prices, finite nonnegative volume, `L<=min(O,C)<=max(O,C)<=H` are mandatory. Any gaps, duplicated timestamps, impossible OHLCV, incomplete final candle or missing price **abort the research segment**; do not forward-fill or infer bars. Bar `t` becomes known only at `T[t]+3600` seconds.
2. Define UTC date `D[t]`, opening UTC hour `h[t]` ∈ {0,...,23}. `Cum[D,h]=sum_{j=0..h} V[D,j]` over the **completed** hourly bars from UTC 00:00 through hour `h` (included). Daily cumulative volume resets at UTC 00:00. The previous **20 entire UTC days** `D-1,...,D-20` must each contain every hour 00..23; evaluate their `Cum[D-k,h]` at the same **elapsed hour**, not same raw volume of a 1h bar. `Base[D,h]=(sum_{k=1..20} Cum[D-k,h])/20`. If any required day's hour is missing, abort (not shorten the history); if `Base<=0`, ZVR is undefined and the entry predicate is false.
3. `ZVR[t]=100*Cum[D[t],h[t]]/Base[D[t],h[t]]`. The **entry edge** is `ZVR[t]>=200` AND (if `h[t]==0`, there was no prior same-session reading, so count this as a fresh crossing; otherwise `ZVR[t-1]<200` from the **same UTC date**). Equality at 200 qualifies on the current side; prior equality 200 does not count as a new crossing. If the previous same-day ZVR is undefined, entry is false. At midnight the prior calendar day reading is not compared to the current day.
4. `PriceBreak[t]=(C[t]>max(H[t-20],...,H[t-1]))` using the **20 immediately preceding** complete hourly bars, excluding the current high. Exact equality fails. Require a valid `PriceBreak[t]` on **the same bar** as the ZVR entry edge; otherwise that edge is lost, not queued.
5. `SMA20[t]=(sum_{i=0..19} C[t-i])/20`, valid after 20 complete hourly closes. It includes the current **completed** candle only for exit evaluation; it is not an intrabar trailing stop.
6. **Warmup:** 20 complete prior UTC days = **480 consecutive 1h bars** before the first eligible decision; also require the previous 20 highs and SMA20. Begin FLAT, zero pending orders, no earlier inferred holdings. First possible decision occurs on the first **completed** hour of UTC day 21, after 480 complete hours, not on the first dataset row; if insufficient actual history, no trades. Indicator state is maintained during warmup but never causes queued orders.
7. **Entry** when FLAT, no order pending, and both conditions (3) and (4) hold on a completed bar `t`: submit a BUY `MARKET` for exactly `Q=Decimal("0.001") BTC` at that **same observed completed bar close `C[t]`** in the pinned historical close-fill simulator. It is a research idealization, not a promise of an executable live close. Full fill requires finite actual `C[t]>0` and modeled available cash at least `Q*C[t]*(1+f)`, `f=Decimal("0.001")`. On confirmed full fill, save actual modeled entry `P=C[t]`, bar index `e=t`, `Stop=P*Decimal("0.97")`, and position LONG. No fill => no inventory: invalid, missing, partial, rejected or ambiguous fill **aborts** rather than silently assuming success.
8. **Exit and explicit priority:** On a **subsequent** completed bar `u>e`, while LONG with no pending order, exit at `C[u]` as a full MARKET SELL if (a) `C[u]<=Stop` (close-triggered 3% reference, priority 1); else (b) `C[u]<=SMA20[u]` (close-based trend invalidation, priority 2); else (c) `u-e>=24` (at most 24 elapsed completed 1h bars since entry, priority 3). Equality at stop, SMA and age threshold triggers. If multiple true conditions, log only highest-priority reason, one SELL. **All checks use a completed close, not intrabar low/high; realized loss may exceed 3%.** The SELL fills the actual same-bar `C[u]` under the same idealized historical model, never at the Stop/SMA threshold, and credits `Q*C[u]*(1-f)`.
9. **Position state and re-entry:** States exactly FLAT and LONG(Q), at most one pending action. On confirmed SELL return FLAT and record `lastExitBar=u`. Do not evaluate a new BUY on the same exit bar; subsequent entry needs a **new same-day ZVR upcross** (or a new day's initial-hour qualifying event), with `t>lastExitBar`. Edges observed while LONG/pending are discarded, never queued. No pyramiding, scaling, reversals, shorts, leverage, borrowing, maker/limit orders, DCA, safety orders, compounding, fixed TP, intrabar/trailing orders, discretionary overrides, forced sample-end liquidation, or unstated controller defaults.
10. **End-of-sample:** If holding a full Q, report inventory and mark it at the last *actually observed completed* close, separately from realized net PnL. If the sample ends with insufficient next bars, do not invent future fills, midnight reset, a stop price or a terminal close.

**Cash/fees (frozen modeled economics):** initial `cash=Decimal("10000") USDT`, `BTC=0`. BUY cash decrement `Q*P*(1+f)`; SELL increment `Q*C*(1-f)`; net realized round-trip `Q*(exit-entry)-f*Q*(entry+exit)`. Fees are a **hypothetical research 0.1% per filled side**, not verified Binance costs; separate gross PnL/fees from net PnL. This derivative uses spot, so perpetual funding/margin/liquidation are **inapplicable**, not invented as zero USDT-M realizations. No real slippage/spread/latency model exists; simulated close-fill slippage is zero **only as an engine assumption**, not market evidence.

## Required data

One historical Binance spot BTC-USDT **1h** feed with completed O/H/L/C/base-asset-V and raw candle-open timestamp, plus precisely **20 fully completed UTC-day histories** before any decision. No second timeframe, external sessions, stock-exchange open, non-OHLCV data, news, order book, macro data or future bar. The UTC-day boundaries are researcher-defined and specifically **not** presented as TradingView's stock-market session implementation. The controller must compute the 20-day same-elapsed-hour baseline from point-in-time observations; **never** average over future days or the complete current day before it closes. All feature timestamps must mean **bar close availability**. Research results on 4h/1d are not implied by this 1h admission; adapting slot counts to 6/1 requires an explicitly pinned new derivative or frozen downstream version.

## Execution assumptions

**Pinned engine examined from GitHub 2026-10-28:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`; Hummingbot package `20260920`, source VERSION `dev-2.17.0`. Static first-party repo files read for this candidate: `hummingbot/VERSION` (`dev-2.17.0`), `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py`, `binance_spot_candles.py`, `strategy_v2/backtesting/backtesting_engine_base.py`, `strategy_v2/backtesting/backtesting_data_provider.py`, `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, and `strategy_v2/executors/order_executor/data_types.py`. This review is **static code-path expressibility only**; no Hummingbot wheel/image digest, candidate controller, executed backtest or Qlib equivalence was verified in this turn.

- **Feed:** `BinanceSpotCandles.INTERVALS` includes `1h`; REST parser maps kline `row[0]` to candle **opening timestamp** and `row[1..5]` to actual OHLC/base volume. `BacktestingDataProvider.get_candles_feed` retrieves historical candles for `start_time - max_records*interval_seconds` through `end_time`. The future minimal controller configuration must explicitly request **max_records >= 480** (e.g. `520`) and verify 20 preceding *complete* UTC days rather than relying on the shorter unspecified default; `get_candles_df` trims to the run window and feature preparation must compute warmup on buffered feed before trimming. Unavailable history aborts; no extra market-data service is assumed.
- **Controller/event path:** `BacktestingEngineBase.simulate_execution` iterates its prepared candles, `update_state(row)`, `controller.determine_executor_actions()`, then `CreateExecutorAction` → `simulate_executor`. A **minimal strategy-specific controller remains to be implemented**; its previous-20-day UTC arithmetic/state is a pure calculation over the existing feed, not a demonstrated already-running strategy. `prepare_market_data` may `merge_asof` and `dropna`, so validate contiguous raw data **before** that path and reject a row/feature timestamp that would create lookahead.
- **Market order:** `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1)` is supported by the inspected config. `OrderExecutorSimulator` consumes the first supplied historical row, takes its **actual `close`** for MARKET price, computes `filled_amount_quote=Q*close` and `cum_fees_quote=trade_cost*Q*close`, and returns `POSITION_HOLD`. The engine's raw row/fill label is the **open timestamp**; the causal **effective** historical close-fill time in this derivative is `open_timestamp+3600`. Never claim that the close was observable at its opening, or that an order can trade a known close instantaneously in live execution.
- **Accounting:** `BacktestPositionHold` nets BUY/SELL base fills, reports gross realized/unrealized quote PnL and separately accumulates `cum_fees_quote`. Candidate accounting must explicitly subtract both-side fees, persist all fills across the `terminated_executors_window` horizon (or use a confirmed-fill ledger), enforce affordability with 10,000 USDT modeled spot cash, mark open Q with actual final close and avoid fabricated trade prices. `BacktestingDataProvider.get_price_by_type` can default missing prices to `Decimal("1")`: this fallback is **prohibited** for this strategy. `run_backtesting(trade_cost=0.001)` pins the modeled fee. Exchange-specific live order precision, min-notional, partial fills, true fee tier, slippage and latency are unverified.
- **Scope:** Single pair, one candle interval, time-of-day calculations derived from UTC timestamp, same-completed-close MARKET model and unleveraged spot position hold use already inspected primitives. There is no unverified futures funding, shared-capital multi-market synchronization, limit/maker queue, external tick input, intrabar touch, next-open prediction, synthetic price, or higher-timeframe feature. This is **engineering feasibility under the pinned historic simulator**, not materialized controller proof or economic/live parity.

## Evidence

### Source-reported

Official ZVR public indicator page (fyntrade, updated 2025-07-08): ratio of current session cumulative volume to same-elapsed-time historical cumulative average, default 20-day historical lookback. The author describes volume pacing and colored high-RVOL display; **the source does not publish a complete trading system**. Exact Pine calculations/session implementation have **not** been reconstructed.

### Independently reproduced

**Not independently reproduced.** No ZVR Pine-to-UTC-crypto numerical parity, actual BTC signal events, Qlib/Hummingbot backtest, 42-cell screening, profits, OOS or certified execution evidence. Only the listed immutable pinned Hummingbot static data/order paths were inspected.

### Negative evidence

The original is an **indicator** without direction/risk/re-entry rules; any entry/exit here is wholly researcher-authored. A 200% flag may not predict continuation; at daily reset, same-day cumulative volume is early, noisy, and not comparable to US-equity regular sessions. Intrabar ZVR may temporarily exceed 200 but disappear by candle close: this version intentionally waits for the completed 1h bar. Same-close MARKET fills and close-based 3% stop can materially understate realistic latency and tail risk. No return/Sharpe, Survivor, or HB Certified claim is supported.

## Falsification plan

Once separately selected, check against an independent sequential Python implementation and the pinned Hummingbot controller using actual 1h OHLCV: (a) 20 preceding UTC dates with 24 bars each, midnight reset, same-slot cumulative volume, first-hour threshold, late-hour equal-to-200 boundary; (b) gaps/NaNs, zero baseline, incomplete last bar, a new ZVR cross without price breakout, a price breakout on a noncross bar, and an exit/re-entry co-print; (c) 3% close-stop gap (fill actual close, not stop), SMA20 equality, 24-bar age, insufficient modeled cash, failed/partial fill and sample-end mark; (d) open-label versus completed-close effective timestamps and no future-leak in `merge_asof`. Compare events, fills, fee-net cash/position ledger, not merely final ROI. If any new primitive is exposed, validate it once before mass Qlib screening. Subsequent IS-only hypothesis tests may consider thresholds/horizons as **new frozen versions**; neither 200% nor 20-day lookback is a pool-wide HB_READY gate.

## Crypto portability

The idea carries across 24/7 cryptocurrency pairs only with explicit **venue-specific base-volume definitions and UTC-session anchoring**. The 1h derivative is pinned to BTC-USDT Binance **spot**, not identical to USDT-M futures or NYSE session ZVR. The current seven-coin × 1h/4h/1d × 3×/5× campaign is **downstream** and would require separate declared venue/interval/leverage/fee/funding models; it is not a silent property of this spot 1h PASS candidate. No blanket performance or market permission claim.

## Limitations

No access to original Pine bytes, no TradingView-authorized strategy return series, and no demonstration of parameter validity outside the declared derivative. The 20 previous-day samples may embed weekends/weekday effects and abnormal recent events. No true intrabar/stop execution; modeled loss can exceed 3%; fixed .001 BTC and modeled fees may be unrepresentative of later portfolio scaling. Candidate-specific executable implementation is absent; the six-gate assessment is about **defined expressibility**, not achieved Qlib readiness or HB parity.

## Implementation status

`not-implemented`. A future selected strategy requires a **minimal specific controller or equivalent existing executable recipe** computing UTC same-slot cumulative ratios and signals with the frozen parameters, then reusable engine run artifacts. Do not introduce a ZVR Manager, adapter registry, generic strategy compiler, new queue or second admission layer.

## Adoption boundary

**Author-proposed `hb_ready_status: PASS`, pending independent exact-head six-gate audit and GitHub PR review.** Six claimed gates: (1) deterministic fully pinned formulas and windows; (2) explicit spot long/flat; (3) explicit price/volume entry and close/time exits with other risk legs disabled; (4) one fixed confirmed position and exact re-entry/order state; (5) inspected pinned Binance spot 1h data + OrderExecutor historical MARKET-close + fee/spot ledger paths; (6) 480-hour warmup, UTC point-in-time same-hour history and effective close timestamps. **Do not merge on the author's proposed status alone.** Only after independent `HB_READY: PASS` for the immutable PR head may a reviewer exact-head squash-merge into PASS-only main. No Qlib, Hummingbot, n8n, survivor, paper/testnet or live action is authorized by this record.

## Related Wiki records

No Wiki Brain or Survivor claim. The cited existing Alpha Research volume/breakout relatives are research comparisons only.

## Sources

- TradingView first-party indicator: https://www.tradingview.com/script/hckcY7Dp-Zanger-Volume-Ratio-ZVR/
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Admission contract: https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
