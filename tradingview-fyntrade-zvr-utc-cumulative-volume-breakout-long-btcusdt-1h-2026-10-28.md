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

**Public primary source and independent audit checked 2026-10-28:** TradingView [Zanger Volume Ratio (ZVR)](https://www.tradingview.com/script/hckcY7Dp-Zanger-Volume-Ratio-ZVR/), author **fyntrade**, public script ID **hckcY7Dp**, source page updated **2025-07-08** (page's first-published display: 2025-02-07; local-time date displays may differ). The description credits **The_Peaceful_Lizard** and characterizes same-elapsed-time cumulative-volume comparison with a default **20**-session lookback. It is a **display-only indicator**, not a published trading strategy. The independent Hermes review on [PR #554](https://github.com/HCH725/alpha-strategy-research/pull/554) accessed and inspected the publicly available 97-line Pine; **the original Pine includes the current session among its mature 20-session averaging ring (current + up to 19 previous sessions)**. That is **NOT** this derivative's prior-20-complete-UTC-day denominator. No copied Pine bytes or source-native numerical equivalence is claimed; the primary-source variant and session conventions must not be conflated.

**Independent executable derivative, not source-native/lossless:** Preserve only the **time-of-day-aligned session cumulative-volume ratio concept**; deliberately **exclude the current UTC day from the mean and compare against 20 fully completed previous UTC days** (researcher-designed deviation from source Pine's current-inclusive ring). Other researcher-defined additions: 24/7 UTC crypto sessions, Binance BTC-USDT **spot 1h** base-asset volume, close breakout above prior 20 hourly highs, 200% newly-crossed ZVR entry threshold (not the source display color comparison), long-only posture, close-based 3% reference stop, SMA20-close exit, maximum 24-bar hold, fixed 0.001 BTC size, 10,000 USDT starting cash, modeled same-completed-close MARKET fills, hypothetical 0.1% fees and failure handling. These are untested research choices, **not source-author rules, published trades or demonstrated profitability**.

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
6. **Warmup:** Require the 20 fully completed **preceding UTC dates** (all 24 hours/day = 480 bars), plus all completed hours of current UTC day through the decision bar, prior 20 hourly highs and SMA20. At a run start during current-day hour `h`, a valid feature can require **480+h** preceding hourly bars and the current bar (so `480` records in a source buffer is *not* sufficient for arbitrary run start hour). Begin FLAT, zero pending orders, no earlier inferred holdings; never infer missing pre-run position. Earliest decision after a clean 20-day UTC warmup is on the first completed hour of day 21. Validate contiguous actual raw history before the provider trims the backtesting window; abort rather than forward-fill, assume cache expansion or trade on insufficient history.
7. **Entry** when FLAT, no order pending, and both conditions (3) and (4) hold on a completed bar `t`: submit a BUY `MARKET` for exactly `Q=Decimal("0.001") BTC` at that **same observed completed bar close `C[t]`** in the pinned historical close-fill simulator. It is a research idealization, not a promise of an executable live close. Full fill requires finite actual `C[t]>0` and modeled available cash at least `Q*C[t]*(1+f)`, `f=Decimal("0.001")`. On confirmed full fill, save actual modeled entry `P=C[t]`, bar index `e=t`, `Stop=P*Decimal("0.97")`, and position LONG. No fill => no inventory: invalid, missing, partial, rejected or ambiguous fill **aborts** rather than silently assuming success.
8. **Exit and explicit priority:** On a **subsequent** completed bar `u>e`, while LONG with no pending order, exit at `C[u]` as a full MARKET SELL if (a) `C[u]<=Stop` (close-triggered 3% reference, priority 1); else (b) `C[u]<=SMA20[u]` (close-based trend invalidation, priority 2); else (c) `u-e>=24` (at most 24 elapsed completed 1h bars since entry, priority 3). Equality at stop, SMA and age threshold triggers. If multiple true conditions, log only highest-priority reason, one SELL. **All checks use a completed close, not intrabar low/high; realized loss may exceed 3%.** The SELL fills the actual same-bar `C[u]` under the same idealized historical model, never at the Stop/SMA threshold, and credits `Q*C[u]*(1-f)`.
9. **Position state and re-entry:** States exactly FLAT and LONG(Q), at most one pending action. On confirmed SELL return FLAT and record `lastExitBar=u`. Do not evaluate a new BUY on the same exit bar; subsequent entry needs a **new same-day ZVR upcross** (or a new day's initial-hour qualifying event), with `t>lastExitBar`. Edges observed while LONG/pending are discarded, never queued. No pyramiding, scaling, reversals, shorts, leverage, borrowing, maker/limit orders, DCA, safety orders, compounding, fixed TP, intrabar/trailing orders, discretionary overrides, forced sample-end liquidation, or unstated controller defaults.
10. **End-of-sample:** If holding a full Q, report inventory and mark it at the last *actually observed completed* close, separately from realized net PnL. If the sample ends with insufficient next bars, do not invent future fills, midnight reset, a stop price or a terminal close.

**Cash/fees (frozen modeled economics):** initial `cash=Decimal("10000") USDT`, `BTC=0`. BUY cash decrement `Q*P*(1+f)`; SELL increment `Q*C*(1-f)`; net realized round-trip `Q*(exit-entry)-f*Q*(entry+exit)`. Fees are a **hypothetical research 0.1% per filled side**, not verified Binance costs; separate gross PnL/fees from net PnL. This derivative uses spot, so perpetual funding/margin/liquidation are **inapplicable**, not invented as zero USDT-M realizations. No real slippage/spread/latency model exists; simulated close-fill slippage is zero **only as an engine assumption**, not market evidence.

## Required data

One historical Binance spot BTC-USDT **1h** feed with actual completed O/H/L/C/base-asset-V and raw candle-open timestamp. Compute the previous 20 **fully completed** UTC days' same-elapsed-hour baseline point-in-time; never include future days or the full unfinished current day. No second timeframe, external session, non-OHLCV data, order book or future candle. **Two distinct timestamp semantics are mandatory:** (a) for the existing `prepare_market_data` backward `merge_asof`, `features.timestamp` is **raw candle-open join key `T[t]`**, matching `timestamp_bt=T[t]`; **never shift this join key by +3600 or use the close-availability timestamp as the right join key**; (b) the logically effective `feature_available_at`, `decision_at` and `historical_fill_effective_at` for this idealized same-completed-close model are all **`T[t]+3600`**, and must be kept as separately named metadata (not as the merge key). Source trading date and UTC hour are derived from the candle **open** `T[t]`, not from its after-midnight availability date. Model decisions must only use this row's completed C/V and earlier rows; this historic same-close convention is **not live executable at a previously known price**. 4h/1d or futures research is not implied by this spot 1h derivative.

## Execution assumptions

**Pinned engine examined from GitHub 2026-10-28:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`; Hummingbot package `20260920`, source VERSION `dev-2.17.0`. Static first-party repo files read for this candidate: `hummingbot/VERSION` (`dev-2.17.0`), `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py`, `binance_spot_candles.py`, `strategy_v2/backtesting/backtesting_engine_base.py`, `strategy_v2/backtesting/backtesting_data_provider.py`, `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, and `strategy_v2/executors/order_executor/data_types.py`. This review is **static code-path expressibility only**; no Hummingbot wheel/image digest, candidate controller, executed backtest or Qlib equivalence was verified in this turn.

- **Feed and warmup:** The Binance spot `1h` candle parser assigns opening timestamps and actual OHLC/base volume. `BacktestingDataProvider.get_candles_feed` requests raw buffered history relative to run start while `get_candles_df` truncates to the run window. Compute UTC cumulative/20-day baseline on actual **raw buffered feed before truncation**, validate consecutive 3600-second bars and 20 entire past UTC days, then join/truncate. For arbitrary run-start hour `h`, at least `480+h` preceding bars plus the current completed bar must be in the **actual returned history**; a candidate request `max_records=520` is a working example, **not proof** of effective buffer span, because cache hits may not expand to the later requested buffer. Check actual coverage and abort if too short; never silently shorten the baseline. No extra data service is assumed.
- **Controller/event path and exact join contract:** The pinned `BacktestingEngineBase.prepare_market_data` performs `pd.merge_asof(backtesting_candles, features, left_on="timestamp_bt", right_on="timestamp", direction="backward")`, overwrites output `timestamp` with `timestamp_bt`, and exposes that row to `update_state(row)` → `determine_executor_actions()` → `simulate_executor`. Therefore compute a completed bar `t`'s signal using this same raw bar and earlier complete bars, and write that feature on **`features.timestamp=T[t]`**, not `T[t]+3600`; a prospective `feature_available_at=T[t]+3600` column is **informational** and never used as `merge_asof` right key. The row index and engine's timestamps remain raw-open labels, but the strategy's effective observation/decision/fill meaning is the **completed bar end**. `dropna` must not obscure missing raw bars; reject discontinuities before merge. No next-bar shift, forward signal, pending ZVR edge or future-day data. Minimal strategy-specific controller is not yet implemented; HB_READY is about reproducible pinned-model expressibility, not existing deployable artifact.
- **Historical MARKET fill, same row:** Existing `OrderExecutorConfig` with Binance `BTC-USDT` spot, side BUY/SELL, `amount=Decimal("0.001")`, `position_action=OPEN/CLOSE`, `execution_strategy=MARKET`, `price=None`, `leverage=1` enters `OrderExecutorSimulator` on the current selected row; MARKET fills at **that row's actual close C[t]**, not at its opening price and not the following close. Its printed `fill_timestamp` is the **raw-open index `T[t]`** only; the effective model fill instant and feature availability are `T[t]+3600`. The simulator idealizes an immediate fill at the just-known completed close with zero slippage: **historical execution convention only**, not guaranteed live fill/latency or a logically earlier trade. Distinguish label from effective time in any report, and never invent a price.
- **Accounting:** `BacktestPositionHold` nets BUY/SELL base fills, reports gross realized/unrealized quote PnL and separately accumulates `cum_fees_quote`. Candidate accounting must explicitly subtract both-side fees, persist all fills across the `terminated_executors_window` horizon (or use a confirmed-fill ledger), enforce affordability with 10,000 USDT modeled spot cash, mark open Q with actual final close and avoid fabricated trade prices. `BacktestingDataProvider.get_price_by_type` can default missing prices to `Decimal("1")`: this fallback is **prohibited** for this strategy. `run_backtesting(trade_cost=0.001)` pins the modeled fee. Exchange-specific live order precision, min-notional, partial fills, true fee tier, slippage and latency are unverified.
- **Scope:** Single pair, one candle interval, time-of-day calculations derived from UTC timestamp, same-completed-close MARKET model and unleveraged spot position hold use already inspected primitives. There is no unverified futures funding, shared-capital multi-market synchronization, limit/maker queue, external tick input, intrabar touch, next-open prediction, synthetic price, or higher-timeframe feature. This is **engineering feasibility under the pinned historic simulator**, not materialized controller proof or economic/live parity.

### Point-in-time join verification — synthetic fixture (not market returns)

At UTC **2026-10-27 23:00**, the bar `T=23:00` carries `D=Oct27,h=23` and is observed only at **Oct28 00:00**. Its same-bar ZVR edge, if any, is keyed by `features.timestamp=Oct27 23:00` and uses `C[23:00]`; its **effective** decision/idealized fill is Oct28 00:00. The following bar `T=Oct28 00:00` is `D=Oct28,h=0` (new cumulative session) and only becomes available Oct28 01:00. **Never** use the availability date to assign `D[t]` or to join features. A simulated cross/exit is attached to the raw row that generated it; no cross is carried to the next row.

The independent [PR #554 auditor review](https://github.com/HCH725/alpha-strategy-research/pull/554) exercised the **actual pinned `prepare_market_data` method AST with pandas** on synthetic rows: opens `[0,3600,7200]`, features `[false,true,false]`. When feature join keys equal raw opens `[0,3600,7200]`, the true event stays on raw row **3600** (effective close **7200**); with incorrect close-availability keys `[3600,7200,10800]`, it shifts to raw row **7200** (effective close **10800**). For this revised record, a separate pure-stdlib bisect semantic check on the user's workspace confirmed those two mappings plus the midnight availability boundary. **The prior failure was an inconsistent feature join contract**, not a policy ban on same-bar historical close simulation. This is bounded engine-primitive evidence, not a candidate controller implementation, actual-market backtest, Qlib parity, realistic live trading proof or source-Pine numerical parity.

## Evidence

### Source-reported

The official ZVR page (fyntrade, updated 2025-07-08) describes cumulative volume pacing relative to elapsed session time, default 20-day lookback. Its public Pine (inspected in independent PR #554 review) **includes the current session in the rolling reference**, and has display/threshold conventions that differ from this derivative's **prior 20 completed UTC dates and >=200 first-cross** choice. **No source-native strategy exists on the cited indicator page.**

### Independently reproduced

**Bounded primitive independently reproduced; source-native signal parity NOT reproduced.** Previous independent PR #554 auditor reproduced the pinned-engine timestamp/join ambiguity using the actual immutable method in a pandas AST test; this revision specifies the raw-open join-key correction. This author rechecked the join semantics and UTC midnight using isolated synthetic data. No actual BTC event output, dedicated Hummingbot controller/backtest, Pine-to-UTC-crypto numerical parity, 42-cell screening, Qlib parity, profitability, OOS, HB Certified or live result is claimed.

### Negative evidence

The original is an **indicator** without direction/risk/re-entry rules; any entry/exit here is wholly researcher-authored. A 200% flag may not predict continuation; at daily reset, same-day cumulative volume is early, noisy, and not comparable to US-equity regular sessions. Intrabar ZVR may temporarily exceed 200 but disappear by candle close: this version intentionally waits for the completed 1h bar. Same-close MARKET fills and close-based 3% stop can materially understate realistic latency and tail risk. No return/Sharpe, Survivor, or HB Certified claim is supported.

## Falsification plan

Once separately selected, check against an independent sequential Python implementation and the pinned Hummingbot controller using actual 1h OHLCV: (a) 20 preceding UTC dates with 24 bars each, midnight reset, same-slot cumulative volume, first-hour threshold, late-hour equal-to-200 boundary; (b) gaps/NaNs, zero baseline, incomplete last bar, a new ZVR cross without price breakout, a price breakout on a noncross bar, and an exit/re-entry co-print; (c) 3% close-stop gap (fill actual close, not stop), SMA20 equality, 24-bar age, insufficient modeled cash, failed/partial fill and sample-end mark; (d) open-label versus completed-close effective timestamps and no future-leak in `merge_asof`. Compare events, fills, fee-net cash/position ledger, not merely final ROI. If any new primitive is exposed, validate it once before mass Qlib screening. Subsequent IS-only hypothesis tests may consider thresholds/horizons as **new frozen versions**; neither 200% nor 20-day lookback is a pool-wide HB_READY gate.

## Crypto portability

The idea carries across 24/7 cryptocurrency pairs only with explicit **venue-specific base-volume definitions and UTC-session anchoring**. The 1h derivative is pinned to BTC-USDT Binance **spot**, not identical to USDT-M futures or NYSE session ZVR. The current seven-coin × 1h/4h/1d × 3×/5× campaign is **downstream** and would require separate declared venue/interval/leverage/fee/funding models; it is not a silent property of this spot 1h PASS candidate. No blanket performance or market permission claim.

## Limitations

No immutable version-pinned original Pine source snapshot is incorporated, and numerical source-Pine parity is neither claimed nor the aim of this **explicit derivative**. Public Pine was independently accessible to the PR #554 auditor; its ring includes current-session observations, unlike this prior-20-complete-days specification. No TradingView-authorized trade series or parameter validity outside the declared derivative. Same-close simulation and close-based 3% stop do not establish live fill feasibility or a maximum loss. Fixed .001 BTC and hypothetical fees may not reflect production trade rules. No dedicated runnable controller, measured returns or HB/Qlib parity; admission is about specified engine-model expressibility, not implementation status.

## Implementation status

`not-implemented`. A future selected strategy requires a **minimal specific controller or equivalent existing executable recipe** computing UTC same-slot cumulative ratios and signals with the frozen parameters, then reusable engine run artifacts. Do not introduce a ZVR Manager, adapter registry, generic strategy compiler, new queue or second admission layer.

## Adoption boundary

**Author-proposed `hb_ready_status: PASS`, pending fresh independent six-gate review of this *new* immutable PR head.** Claim limited to (1) deterministic fully declared derivative; (2) spot long/flat; (3) explicit completed-close entry/exit/risk; (4) fixed position and re-entry state; (5) pinned 1h feed, current-row MARKET-close simulator, **raw-open feature join key T[t]** and separately effective `T[t]+3600` timing with modeled ledger; (6) actual 20 complete UTC days + current-day prehistory, no future bars, point-in-time close observation. Reuse previous auditor's concrete engine-primitive check as supporting evidence but **do not treat prior NOT_LOSSLESS as PASS**. Reviewer must independently verify this revised contract. No merge unless a fresh `HB_READY: PASS` is posted for the exact new head; no changes to Hummingbot/Qlib/n8n, main policy, Survivor or live trading.

## Related Wiki records

No Wiki Brain or Survivor claim. The cited existing Alpha Research volume/breakout relatives are research comparisons only.

## Sources

- TradingView first-party indicator: https://www.tradingview.com/script/hckcY7Dp-Zanger-Volume-Ratio-ZVR/
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Admission contract: https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
