---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: krmdstn Vorse4 Chaikin-zero IMI14 MACD PSAR four-confirmation BTCUSDT spot 1h long-flat independent derivative
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-04-02
sources:
  - https://www.tradingview.com/script/onghOt7e/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Vorse4 Chaikin-zero / IMI14 / MACD / PSAR four-confirmation — BTC-USDT spot 1h independent derivative

## Provenance

**Primary first-party TradingView source:** *Vorse4*, **krmdstn**, published **2023-04-02**, public **open-source indicator**, immutable public script ID `onghOt7e`, https://www.tradingview.com/script/onghOt7e/ ; directly inspected first-party publication text **2026-10-29**. This is an indicator, **not** a source-native TradingView strategy or a verified original backtest. The public HTML text gives the author's conceptual decision conditions but not the complete Pine revision bytes or defaults. No claim of full Pine equivalence or copied proprietary source.

**Verified source-reported signal facts:** The author combines **Chaikin Oscillator**, **Intraday Momentum Index (IMI)**, **MACD** and **Parabolic SAR**. A BUY requires a positive Chaikin crossover, IMI > 50, bullish MACD-line/signal-line crossover and price above PSAR **simultaneously**. A SELL requires the reverse Chaikin crossover, IMI < 50, bearish MACD-line/signal-line crossover and price below PSAR **simultaneously**. The page does not identify what the Chaikin "positive crossover" crosses, indicator periods/smoothing/initialization, quantity, stops, timing, fees, pyramiding, or whether indicator arrows are executable orders.

**Explicit independent researcher-derived strategy, NOT source-native:** Fix Chaikin's ambiguous "positive/negative crossover" to **zero-line cross** of EMA3(ADL)-EMA10(ADL); define IMI14, MACD12/26/9, Wilder-style PSAR(0.02,0.02,0.20), all exact seeds/tie cases below. Interpret the four-way BUY as spot LONG entry and four-way SELL as full long exit, disabling short entries; use one Binance BTC-USDT spot 1h stream, fixed 0.001 BTC, no DCA, no extra stop/TP, and a completed-bar synthetic MARKET-close execution convention with a hypothetical fixed fee. These choices are **researcher-designed**, not claimed author defaults. The original script's chart arrows and any original backtest are not reproduced.

**Immutable candidate identity:** `TV:onghOt7e:krmdstn:2023-04-02 | derived-v1-CHO(ADL-EMA3-10)-zero-cross-IMI14-MACD12-26-9-PSAR0p02-0p02-0p20-four-way | binance-BTC-USDT-spot-1h-LONG-FLAT-0p001BTC | effective-completed-close-MARKET | 2026-10-29`. Any parameter, signal, market, execution, risk or state change is a **new derivative**, not a silent revision.

**Dedup evidence:** At main SHA `9b7eec4f896004873cf057f0685384c160a877f2`, 430 root-level strategy records and README count 430. GitHub code searches for `onghOt7e` and `Vorse4` returned no existing record; no matching source in the ten open research PRs. Related `chaikin-oscillator-ad-zero-cross-momentum-divergence-two-sided-btcusdt-4h-2026-10-12.md` uses an ADL/Chaikin momentum-divergence mechanism, `imi-50-midline-cross-flip-two-sided-btcusdt-1d-2026-10-15.md` uses standalone IMI threshold flips, and PSAR/MACD records use different gating. This **four-way simultaneous** Chaikin+IMI+MACD+PSAR event is materially distinct; parameter-only variations are not separately proposed.

## Economic mechanism

### Source-reported

The author's premise is conjunctive confirmation of money flow, intrabar candle momentum, price-trend momentum and a trailing trend reference. Its four simultaneous BUY/SELL indicator conditions are source-reported. No win rate, expectancy, profitability, or Pine-reproduced results are adopted.

### Research interpretation

This derivative tests whether a Chaikin money-flow zero reversal **coincident with** a MACD signal crossover, positive IMI regime and bullish PSAR price relation can isolate rare aligned reversals. Exiting requires all four bearish conditions simultaneously; that is deliberately stringent and may leave a position open for long periods. It is **not** a safety stop or a recommendation to trade.

## Signal

**Gate 1 — fully pinned formulas and state;** bar index `t` starts at 0; `O,H,L,C,V` are real finite Binance spot hourly OHLCV observations. Compute on **completed** consecutive bars only, with no smoothing library defaults or training/fitting.

1. **Chaikin ADL and oscillator.** For each completed bar, `MFM[t] = (2*C[t]-H[t]-L[t])/(H[t]-L[t])` if `H[t]>L[t]`, otherwise `MFM[t]=0`. `MFV[t]=MFM[t]*V[t]`; `ADL[0]=MFV[0]`, `ADL[t]=ADL[t-1]+MFV[t]`. For any `EMA_n(X)`, set `EMA_n(X)[0]=X[0]`, then `EMA_n(X)[t]=2/(n+1)*X[t]+(1-2/(n+1))*EMA_n(X)[t-1]`. `CHO[t]=EMA_3(ADL)[t]-EMA_10(ADL)[t]`. Bullish Chaikin event `CHO[t-1]<=0 && CHO[t]>0`; bearish `CHO[t-1]>=0 && CHO[t]<0`. Zero at the current bar is **not** a crossing.
2. **IMI14.** `up[t]=max(C[t]-O[t],0)`, `down[t]=max(O[t]-C[t],0)`; `IMI14[t]=100*sum(up[t-13..t])/(sum(up[t-13..t])+sum(down[t-13..t]))`. Require all 14 valid bars and **positive** denominator; if all 14 candles are dojis, IMI is undefined and no signal. Long filter strictly `IMI14[t]>50`; sell filter strictly `IMI14[t]<50`; equality is neither.
3. **MACD.** `F[t]=EMA_12(C)[t]`, `S[t]=EMA_26(C)[t]`, `M[t]=F[t]-S[t]`, `G[t]=EMA_9(M)[t]`, seeded `M[0]=G[0]=0` using the EMA rule above. Bull event `M[t-1]<=G[t-1] && M[t]>G[t]`; bear event `M[t-1]>=G[t-1] && M[t]<G[t]`. Strict on the current bar, non-strict on the previous.
4. **Parabolic SAR (researcher-frozen Wilder-style).** Parameters `start=0.02, step=0.02, cap=0.20`. Seed at completed bar 1: trend UP when `C[1]>=C[0]`, else DOWN; UP `SAR[1]=min(L[0],L[1]), EP[1]=max(H[0],H[1])`; DOWN `SAR[1]=max(H[0],H[1]), EP[1]=min(L[0],L[1])`; `AF[1]=0.02`. For `t>=2`, `candidate=SAR[t-1]+AF[t-1]*(EP[t-1]-SAR[t-1])`. If prior trend UP, clamp `candidate=min(candidate,L[t-1],L[t-2])`; if `L[t]<candidate`, reverse DOWN and set `SAR[t]=EP[t-1], EP[t]=L[t], AF[t]=0.02`. Otherwise remain UP, `SAR[t]=candidate`; if `H[t]>EP[t-1]`, set `EP[t]=H[t], AF[t]=min(0.20,AF[t-1]+0.02)`, else retain EP/AF. If prior trend DOWN, clamp `candidate=max(candidate,H[t-1],H[t-2])`; if `H[t]>candidate`, reverse UP and set `SAR[t]=EP[t-1], EP[t]=H[t], AF[t]=0.02`. Otherwise remain DOWN and, only if `L[t]<EP[t-1]`, update `EP[t]=L[t], AF[t]=min(0.20,AF[t-1]+0.02)`; else retain EP/AF. Equality does not reverse or update EP. Long filter `C[t]>SAR[t]`; bearish filter `C[t]<SAR[t]`. These precise tie/seed choices are **not** recovered source Pine defaults.
5. **Conjunctive entry and exit.** Define `B[t]` as bullish Chaikin zero-cross **AND** IMI14>50 **AND** bullish MACD signal-cross **AND** C>PSAR on the **same completed t**. Define `S[t]` as bearish Chaikin zero-cross **AND** IMI14<50 **AND** bearish MACD signal-cross **AND** C<PSAR on the **same completed t**. No "recent within N bars" substitution, delayed catch-up, indicator repaint or OR shortcut. While FLAT and armed, `B[t]` requests one BUY 0.001 BTC; while LONG, `S[t]` requests one SELL of the **actual filled held BTC quantity**. No short/reversal order. If both were somehow true (the strict cross predicates preclude it), EXIT has priority and there is no same-bar reentry.

**Gate 2:** `binance` spot BTC-USDT, LONG/FLAT only; no leverage, borrowing, futures, hedging, short or negative base inventory.

**Gate 3:** No stop loss, take profit, trailing stop, intrabar touch, time stop, limit/maker orders, stop orders, discretionary override, end-of-sample forced liquidation, or implicit Hummingbot triple-barrier. The only discretionary-looking "turning zones" in the source are **not** traded. If no bearish four-way event appears, hold until sample end without a fictitious closing fill. This is a material risk limitation, not a hidden default.

**Gate 4 — fill-confirmed state machine:** `FLAT_ARMED -> BUY_PENDING -> LONG -> SELL_PENDING -> FLAT_DISARMED`. Initialize `FLAT_ARMED` only after warmup if `B[t-1]` is false; otherwise wait for a later `B=false` bar to arm. After confirmed BUY POSITION_HOLD fill, mark LONG at actual simulated fill price/quantity. While LONG, ignore B; on S request SELL, retain LONG until the SELL fill is confirmed. On confirmed full SELL return `FLAT_DISARMED`; require at least one later valid completed bar with `B=false` to re-arm, then a **new** B event on a subsequent bar. Failed, unfilled or missing MARKET fills **halt the research run** instead of creating phantom exposure or silently reissuing. At most one pending order and one 0.001 BTC position; no pyramiding, DCA/safety orders, concurrent positions, partial profit taking, compounding, rebalancing, cooldown beyond the explicit re-arm, or same-bar exit/reentry. Entry requires sufficient actual quote balance; reject/stop if connector quantity/precision/min-notional requirements are unmet, never silently resize.

## Required data

**Gate 6 — availability and warmup.** One Binance spot BTC-USDT `1h` stream with UTC **bar-open** timestamp `T[t]`, valid `O,H,L,C>0`, `H>=max(O,C)`, `L<=min(O,C)`, finite `V>=0`, and exactly 3600-second consecutive opens. Use at least **120 complete valid prior hourly bars** before the first decision (first eligible bar index `t>=120`), covering IMI14, EMA26/9 and PSAR initialization. EMA/ADL/PSAR seeds are from the earliest valid bar in the contiguous warmup, not from future or full-sample data. A gap or malformed candle invalidates features and resets the 120-bar continuity warmup and all indicator seeds; while LONG, preserve real inventory and refrain from decisions until continuity is restored. Never backfill missing candles/prices or fabricate an exit during a gap.

A bar's final high/low/close/volume and indicators are available only at `T[t]+3600s` or later. Signals are evaluated **after** the complete t bar; no use of `t+1` information, incomplete candles, lookahead extrema, future-shifted indicator, multi-timeframe merge, ML model or retrospective threshold tuning. At sample end, mark any open position only at the last **observed valid** close, not with a simulated sell.

## Execution assumptions

**Gate 5 — pinned Hummingbot bounded historical model.** Package `20260920`, VERSION `dev-2.17.0`, inspected source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`; `hummingbot/VERSION` blob `fa1dd206a0e288710d6d68e195d4f030960fc6fb` confirms the version. Source files inspected through the connected GitHub app this cycle, not current unpinned master. Prior merged Alpha PR **#414** describes a 902/902 wheel byte-match and 33-assert representative capability validation of this pinned path; this Scout **did not independently rehash the wheel or rerun tests**. No unverified binary digest or live compatibility is claimed.

- **Actual market/feed:** `BinanceSpotCandles`, `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` blob `5d0c938af574aca5f8dcba5ba28121797eae4dd0`; Binance `/api/v3/klines` and `constants.py` blob `6d505dff42b60b356931df13eeeecd1e28b426f9` explicitly include `1h`. REST parsing uses row[0] **open timestamp** and row[1..5] O/H/L/C/V. No secondary market, order book, lower timeframe, perpetual funding, mark price, shared capital or external feature.
- **Controller/executor:** a **strategy-specific not-yet-implemented controller** computes all four features/state and enforces effective close-time availability. `BacktestingEngineBase.run_backtesting(...,backtesting_resolution="1h",trade_cost=0.0002)` in `backtesting_engine_base.py` blob `7d1e552dd7ee62df4f83f10950b8d593cd1106e6` calls `update_processed_data`, then `prepare_market_data`, per-row `update_state` and `determine_executor_actions`. `CreateExecutorAction(OrderExecutorConfig)` routes to `OrderExecutorSimulator` (blob `3b4e82e91896db9074295ca2a8a087dde2499eab`). Config: `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=TradeType.BUY/SELL`, `position_action=OPEN/CLOSE`, `amount=Decimal("0.001")` for BUY and actual held amount for SELL, `execution_strategy=ExecutionStrategy.MARKET`, `price=None`, `leverage=1`. `OrderExecutorConfig` in `data_types.py` blob `67715e3d14a1edf636defa95a7bbe5c73b8cff90` has these fields. A generic executor name alone does **not** calculate this strategy.
- **Exact bounded fill and time model:** the pinned MARKET simulator fills at the **first supplied historical row's observed close** and marks `CloseType.POSITION_HOLD`. This derivative uses a **synthetic completed-bar close-effective fill** on the signal bar, after its inputs are complete. The engine's `prepare_market_data` uses backward `merge_asof` on **bar-open** timestamp labels; the controller must explicitly gate decision availability to `T+3600` and preserve the effective-close event ledger, not treat the bar's opening timestamp as a legal decision time. A post-close real order is **not** guaranteed to receive that historical close; this is a declared historical abstraction, not an executable live-price claim. If effective timestamp gating cannot be implemented, Gate 5/6 must be rejected in implementation. No next-open, intrabar, maker or stop fill is claimed.
- **Fill/position ledger:** `BacktestPositionHold` defined in the pinned `backtesting_engine_base.py` nets confirmed BUY/SELL base, tracks weighted entry, realized **gross** PnL and quote fees separately. Controller changes state on confirmed `POSITION_HOLD` fills, never order intent. Default `terminated_executors_window=3600` can omit historical fills at the 1h boundary; use a persistent fill-confirmed state or `terminated_executors_window=None` and check the hold ledger, never assume an old fill from an empty view. The final-tick executor flush exists in this pinned code, but no fictitious close is inserted.
- **Costs and price integrity:** `trade_cost=0.0002` is a declared **hypothetical 0.02% of fill notional on each BUY and SELL**, as `cum_fees_quote=trade_cost*amount*observed_close` in the inspected simulator; **not** Binance's realized fee tier. Research round-trip net for matched quantity `q`: `q*(P_sell-P_buy)-0.0002*q*(P_buy+P_sell)`; reconcile fill ledger and fees rather than calling the engine's gross position PnL or `pnl_timeseries` fee-inclusive net equity. No separate slippage/spread/market-impact is simulated: **not** a claim that real costs are zero. Spot funding **does not apply**; no futures funding or margin is invented. Check observed finite positive `close_bt` before action and mark; the provider's missing-price fallback `Decimal("1")` must **never** substitute for an actual BTC price. Tick/lot precision, min-notional, liquidity, partial fills and actual fills remain unverified live constraints; refuse invalid orders rather than fabricate them.

## Evidence

### Source-reported

The 2023-04-02 krmdstn TradingView page reports the four simultaneous positive/negative Chaikin/IMI/MACD/PSAR arrow conditions. The indicator does not publish a verified strategy PnL or exact executable order model in the retrieved public text.

### Independently reproduced

**None.** No original Pine execution, signal-by-signal replay, Hummingbot/Qlib backtest, event-level parity, performance or real fill reproduction was performed. This record proposes a fully specified **derived** six-gate PASS candidate for **independent Hermes Auditor** review; Scout's PASS frontmatter is **not** independent approval.

### Negative evidence and six-gate checklist

- Source-native default periods, Chaikin crossover reference, PSAR seed, fees, size and timing were **not recovered**; every one is expressly frozen as a researcher derivative, not attributed to the author.
- Gate 1: exact CHO/ADL, IMI14, MACD12/26/9, PSAR recurrences, ties, same-bar conjunction and seeds.
- Gate 2: realistic spot LONG/FLAT; short disabled.
- Gate 3: all-four entry/exit, risk exits explicitly disabled; no hidden stops.
- Gate 4: single 0.001 BTC fill-confirmed position, no DCA/concurrency, pending/re-arm defined.
- Gate 5: directly inspected pinned Binance 1h candles → custom controller → MARKET OrderExecutorSimulator → POSITION_HOLD ledger; synthetic close fill, explicit hypothetical fees, real-price validation, nonapplicable spot funding and unverified live limitations.
- Gate 6: 120 completed prior bars, strict UTC continuity, availability `T+3600`, no future leakage.
- Auditor must reject if the four-way source description was misread, source/derived boundary is blurred, effective-close clock is not representable, or any pinned engine/cost/position invariant fails. A PASS is neither source-native parity nor profitability or trading authorization.

## Falsification plan

On a future authorized engineering run, independently compute the four indicator series and simultaneous crossing events from a frozen real BTC-USDT 1h tape; verify tie cases, PSAR reversals, all-doji IMI, missing/zero-volume candles, warmup/gap resets, rare sell-event holding, fill-confirmed re-arm, and actual observed-price requirement. Validate representative Hummingbot controller event/fill/fee/clock parity before using a new execution primitive in large Qlib screening. No such run was performed by this Scout.

## Crypto portability

BTC-USDT spot 1h and fixed 0.001 BTC are **this derivative's** chosen identity, not HB_READY admission prerequisites. Other markets, short/futures, intrabar stops, maker orders or BO/SO 6/6/6 research overlays require separate disclosed execution/strategy evidence; DCA would alter trade events. No 7-coin/1h-4h-1d whitelist or profitability threshold is imposed at admission.

## Limitations

Potentially extremely sparse simultaneous signals and no protective stop may cause extended exposure or large drawdown. Source Pine bytes/defaults were unavailable; no native-equivalence claim. The historical completed-close MARKET model is not a live fill guarantee. Package digest was not rehashed in this cycle, and actual exchange fees, slippage, precision, PnL, Qlib parity, Survivor status and live safety are unverified.

## Implementation status

`not-implemented`: no dedicated controller, executable Qlib recipe, container deployment, paper trading, backtest or trading artifact was created by this research Scout. Research admission is separate from executable materialization.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. Do not merge or approve this PR in Scout. Independent Hermes Auditor GitHub Webhook Review owns exact-head PASS audit/merge or NOT_LOSSLESS closure. README post-merge count belongs solely to the existing signed webhook receiver.

## Related Wiki records

None identified; no Wiki changes.

## Sources

- https://www.tradingview.com/script/onghOt7e/ — krmdstn, *Vorse4*, published 2023-04-02, first-party public description inspected 2026-10-29.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting — pinned backtesting implementation and simulator.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — previously merged representative pinned-engine capability evidence; **not** this strategy's independent review.
