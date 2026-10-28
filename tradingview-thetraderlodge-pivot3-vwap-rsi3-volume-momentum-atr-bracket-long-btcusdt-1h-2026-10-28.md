---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "TradingView thetraderlodge pivot-3 breakout with volume, momentum, RSI3 and UTC VWAP gates — independent BTC-USDT spot 1h long-flat derivative"
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
source_as_of: 2025-08-22
sources:
  - https://www.tradingview.com/script/4juJumUH-Instant-Breakout-Strategy-with-RSI-VWAP/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Pivot-3 breakout with volume/momentum/RSI3/UTC-VWAP confirmation — independent research derivative

## Provenance

- **Primary first-party TradingView publication:** thetraderlodge, *Instant Breakout Strategy with RSI & VWAP*, published **2025-08-22**, public immutable script identifier **4juJumUH**, described as **Pine Script v6** and open-source: https://www.tradingview.com/script/4juJumUH-Instant-Breakout-Strategy-with-RSI-VWAP/ . The author's full public description was read directly on 2026-10-28; the complete Pine source bytes were **not** retrieved. This record does not assert Pine-code parity, original fills, or source-native losslessness.
- **Source-description facts only:** the author describes ta.pivothigh/ta.pivotlow with left/right default 3, bullish close breakout of latest pivot high and bearish close breakdown of latest pivot low; optional volume surge above 1.5 times the 20-bar average, open-to-close momentum greater than 1%, RSI3 above/below 50, and price above/below VWAP; ATR14 stop/target multipliers 1.0/9.0; the optional filters are **OFF by default**; the original is a long/short strategy optimized for **1-second** bars. The description does not provide full Pine tie behavior, session VWAP anchor, precise ATR order execution, trade size, cooldown, commission or original full state machine.
- **Independent derivative, NOT the original TradingView strategy:** This research version **turns all four optional filters ON**, changes decision timeframe to Binance BTC-USDT **spot 1h**, selects LONG/FLAT only, defines strict confirmed pivot ties and delayed activation, UTC daily HLC3-volume VWAP, exact indicator seeds, same-completed-close historical MARKET fills, close-triggered entry-frozen ATR bracket, one fixed BTC unit size, modeled costs and an explicit position/pivot-consumption ledger. All these choices are **researcher-defined**, including bearish-breakout-as-long-exit and close-triggered rather than intrabar ATR exits; they may materially change trade events. The original short leg, 1-second timing, intrabar stops and any other unspecified source behaviors are **not** claimed to survive.
- **Immutable derivative identity:** TV:4juJumUH|thetraderlodge|2025-08-22|independent-derived-v1-2026-10-28|BinanceSpot-BTC-USDT-UTC1h|pivot-strict-3L3R-next-bar-active|all-filters-on-volume20x1.5-momentum1pct-RSI3-Wilder-UTCday-HLC3-VWAP|long-flat|ATR14-close-stop1-target9|Q0.001BTC-cash10000USDT|same-completed-close-MARKET|fee0.001-per-side|warmup100-prior-bars. Any altered timing, pivot, filter, risk, size or fill convention creates a different strategy identity.
- **Dedup on current main and open research PRs:** main at c009187f780b6b097260f3c7b00e80e1b067e25d has 409 root strategy records and README count 409. Connected GitHub source-ID search for 4juJumUH and open-PR search found none. Related main records include pivot-point-breakout-kaufman (unfiltered pivot extreme/high-low event), forven-atr-volume-breakout (prior-high plus ATR/volume, no RSI/VWAP), tradingview-vlenarcic-volume-cci-stoch-vwap-cross (MA/VWAP cross with volume oscillators, no pivot breakout), and thetraderlodge ANWxAWqY (Bollinger reclaim). None shares the exact strict pivot + simultaneous volume/open-close momentum/RSI3/UTC-session VWAP conjunction with frozen ATR close-bracket. The 10 open research/* PRs returned by the GitHub pulls endpoint concern other source IDs and mechanisms. No exhaustive semantic equivalence proof is claimed.

## Economic mechanism

### Source-reported
The author's description proposes confirming a pivot-level price breakout with unusually high volume, same-bar price momentum, RSI direction and VWAP location, then using ATR-scaled exits. It reports no independently reproduced expectancy for this derivative.

### Research interpretation
Hypothesis only: a freshly confirmed structural breakout accompanied by all four independent participation/direction filters may reduce weak breakouts. An entry-frozen ATR14 close bracket tests asymmetric 1:9 reference exits; this is **not** a guaranteed 1:9 realized reward/risk ratio because fills occur at observed closes. No backtest, profitability or survivor claim is made.

## Signal — complete independent derived specification (Gates 1–4 and 6)

1. **Single data stream and time:** Binance BTC-USDT spot UTC-aligned **1h** OHLCV. Bar t has opening Unix timestamp T[t] divisible by 3600, strictly increasing in exact 3600-second steps; its O/H/L/C/base-BTC V are usable only once the full bar completes at T[t]+3600. Require finite positive O,H,L,C, finite V>=0, L<=min(O,C)<=max(O,C)<=H, and no duplicate/missing/uncompleted bars. A gap, missing VWAP session opening bar, invalid price/volume, or ambiguous last candle **aborts the research run**, including when already LONG; do not synthesize a fill, silently skip, forward-fill or substitute a price.
2. **Volume and momentum:** Vmean20[t]=sum(V[t-i],i=0..19)/20 (includes current completed volume); VolumeSurge[t] iff Vmean20[t]>0 AND V[t]>1.5*Vmean20[t]. BullMomentum[t] iff (C[t]-O[t])/O[t]>0.01; BearMomentum[t] iff (C[t]-O[t])/O[t]<-0.01. All current-side inequalities strict; exact threshold equality fails.
3. **RSI3 Wilder:** delta[i]=C[i]-C[i-1]; initial avgGain[3]=sum(max(delta[i],0),i=1..3)/3, avgLoss[3]=sum(max(-delta[i],0),i=1..3)/3; thereafter avgGain[t]=(2*avgGain[t-1]+max(delta[t],0))/3 and avgLoss analogously. RSI=100-100/(1+avgGain/avgLoss). If avgLoss=0 and avgGain>0 set RSI=100; if both zero set RSI=50; if avgGain=0 and avgLoss>0 set RSI=0. BullRSI iff RSI>50; BearRSI iff RSI<50. No full-sample initialization.
4. **UTC-day VWAP:** daily session runs UTC 00:00–23:59:59 with exactly 24 expected hourly opens. For each *completed* bar of the current UTC day through t, TP[i]=(H[i]+L[i]+C[i])/3 and VWAP[t]=sum(TP[i]*V[i])/sum(V[i]). Reset both sums on UTC 00:00; do not include earlier days, later current-day bars, exchange-local time or an incomplete bar. Require the current UTC day's 00:00 bar and all subsequent completed hours without gaps. If cumulative volume is zero, VWAP is undefined and both VWAP filters are false. BullVWAP iff C[t]>VWAP[t]; BearVWAP iff C[t]<VWAP[t].
5. **ATR14 Wilder:** TR[0]=H[0]-L[0]; for i>=1 TR[i]=max(H[i]-L[i],abs(H[i]-C[i-1]),abs(L[i]-C[i-1])). ATR[13]=mean(TR[0..13]); for t>=14 ATR[t]=(13*ATR[t-1]+TR[t])/14. Entry requires finite ATR[t]>0. No future volatility or recalculation of an entry-frozen bracket.
6. **Strict causal pivots:** a pivot high at center j>=3 exists iff H[j] is **strictly greater** than each of the three preceding and three following highs; pivot low iff L[j] is strictly smaller than each of those six lows. Equal highs/lows reject a pivot. A pivot at j can be **confirmed only at the completed close of j+3** and is **active only from bar j+4 onward**; its earlier chart placement must not be traded at j. Maintain latest activated high and low separately, replacing older levels on new activation; an activated replacement resets that side's consumed flag. Without a confirmed active pivot that side has no signal.
7. **Break edges and consumption:** for the latest active, unconsumed pivot high PH[t], HighBreak[t]=(C[t-1]<=PH[t] AND C[t]>PH[t]); for active unconsumed pivot low PL[t], LowBreak[t]=(C[t-1]>=PL[t] AND C[t]<PL[t]). Both comparisons use **the same currently active level** (never mix the prior bar's older level). Equality on previous bar arms an edge; equality on current bar fails. A level is consumed only by a successfully filled corresponding trade; it cannot generate repeated trades until a newer confirmed pivot replaces it. Signals while in the wrong position state are ignored, not queued.
8. **Entry:** after at least **100 consecutive valid fully completed prior hourly bars** (first eligible t>=100, zero-based), while FLAT, no pending order and no same-bar exit, require HighBreak[t] AND VolumeSurge[t] AND BullMomentum[t] AND BullRSI[t] AND BullVWAP[t] AND ATR[t]>0. Submit exactly one simulated MARKET BUY of Q=Decimal("0.001") BTC on the **same completed bar close C[t]** using the pinned historical OrderExecutor simulator. On confirmed full fill record entry price P=C[t], entry bar e=t, fixed Stop=P-ATR[t]*1.0, fixed Target=P+ATR[t]*9.0; mark high pivot consumed. This is a research same-close idealization, not a real-time guaranteed fill.
9. **Exit and priority:** only on a **subsequent** completed bar u>e while LONG with no pending order, first test (a) C[u]<=Stop; else (b) C[u]>=Target; else (c) LowBreak[u] AND VolumeSurge[u] AND BearMomentum[u] AND BearRSI[u] AND BearVWAP[u]. If any fires, submit one full-Q MARKET SELL at **actual C[u]**, never at Stop/Target/PL. In simultaneous conditions log the first reason in order (a),(b),(c). On a confirmed full fill return FLAT, save lastExitBar=u, and consume the low pivot only if reason (c). Entry is **never** reconsidered on the exit bar. The stop/target are **close-based reference thresholds**, not exchange stop/limit orders or intrabar high/low touches; a gap can materially exceed the nominal stop.
10. **Position state:** exactly FLAT or LONG(Q) with a strategy-owned confirmed-fill ledger and at most one order/action per bar. Initial modeled cash=Decimal("10000") USDT and BTC=0. Before BUY require cash>=Q*C[t]*(1+f), f=Decimal("0.001"). Confirm BUY/SELL full fill and fee from executor results before mutating inventory; missing, rejected, partial, stale, inconsistent or nonfinite fills **abort**, never assume success. Entry signals while LONG and bearish signals while FLAT are no-ops; after a confirmed exit, a **new unconsumed high pivot** and later qualifying high-break edge are required to re-enter. No cooldown beyond no same-bar reentry. No short, reversal, leverage, margin, pyramiding, DCA, safety orders, concurrency, compounding, maker/limit order, discretionary override, trailing stop, time exit, other TP/SL, or forced terminal liquidation.
11. **End of sample:** if LONG at the last actually completed valid close, report Q inventory and mark-to-market separately from realized PnL; do not invent a terminal SELL, future price or unobserved bar. Any missing pre-run buffer, including the UTC day's opening bar needed for VWAP, invalidates the corresponding run rather than weakening warmup or backfilling an artificial price.

## Required data

Exactly one Binance spot BTC-USDT 1h historical OHLCV stream and UTC timestamps; all features are deterministic from **past and current completed** bars. No second market, shared-capital synchronization, lower/higher timeframe, external order book, intrabar tick, future pivot, ML artifact, funding feed or exchange session calendar. Validate at least 100 actual contiguous **pre-decision completed** candles including the full current UTC day from 00:00; request adequate raw provider buffer and check returned coverage before the provider trims the backtest interval. A configured max_records alone is not proof that the cached feed contains the requested history.

## Execution assumptions — pinned Gate 5

- **Pinned model identifiers:** Hummingbot package label **20260920**, VERSION **dev-2.17.0**, immutable source **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3**. Direct connected-GitHub reads on 2026-10-28 verified VERSION, Binance spot 1h constants/parser, BacktestingDataProvider, BacktestingEngineBase, OrderExecutorSimulator and OrderExecutorConfig. The pinned setup.py distribution version differs from the package label; the independent PR #414 auditor reported wheel SHA256 ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148 and 902/902 shipped Python files byte-identical to this source commit. This Scout **did not re-download or re-hash the wheel**, so it relies on that prior independent binding rather than asserting new wheel verification.
- **Data feed:** BinanceSpotCandles supports **1h** and parses REST Kline open epoch row[0] with actual O/H/L/C/base volume row[1..5]. BacktestingDataProvider requests historical start_time minus max_records*interval, caches feeds and get_candles_df truncates to the requested run window. The strategy-specific controller must validate **actual raw buffered history**, full UTC session and consecutive completed bars **before** truncation/feature generation; a cached feed or max_records request is not proof of coverage. No fabricated OHLCV or price fallback.
- **Controller and join:** The pinned BacktestingEngineBase.prepare_market_data does backward merge_asof(left_on="timestamp_bt",right_on="timestamp"), then maps timestamp to raw candle-open and supplies each row to update_state → determine_executor_actions → simulate_executor. Precompute **causal** features using only the completed current and earlier candles; feature join key MUST equal the raw opening timestamp T[t], never T[t]+3600, or the signal would shift one bar. Store logical feature_available_at, decision_at and historical_fill_effective_at separately as **T[t]+3600**. The simulator row index and printed fill timestamp are raw-open labels T[t]; they are **not** claims of decision before close. The historical same-close fill is an idealized engine convention, not achievable live after observing the close at a guaranteed identical price. Strategy-specific controller is **not implemented**; its required signal/state machine is fully specified above.
- **Executor and fill:** OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1). Pinned OrderExecutorSimulator MARKET selects the first supplied row, fills at that row's **actual close**, computes filled_amount_quote=Q*close and cum_fees_quote=trade_cost*filled_amount_quote, with CloseType.POSITION_HOLD. Controller must use its own **confirmed-fill state** to avoid lagging position-hold views or terminated-executor window effects. Abort on absent, inconsistent, partial or nonfinite fills; no alternative LIMIT, intrabar, next-open or market-impact path is asserted.
- **Modeled costs/accounting:** run_backtesting(trade_cost=0.001) fixes a **hypothetical 0.1% fee per filled side**. BUY cash decreases by Q*P*(1+f), SELL cash increases by Q*P*(1-f); realized net round-trip PnL = Q*(P_sell-P_buy)-f*Q*(P_buy+P_sell). BacktestPositionHold nets BUY/SELL base exposure and tracks gross PnL and cum_fees_quote separately; fee-inclusive cash/equity must be reconstructed from **all actual executor fills** (not a gross-only net_pnl_quote label). The simulator's float-to-Decimal conversions require reconciliation with tolerances **1e-9 BTC inventory and 1e-8 USDT fee**; discrepancies beyond tolerance abort, and tiny residuals are reported rather than silently written off. BacktestingDataProvider.get_price_by_type can fall back to Decimal("1") on missing prices: **explicitly prohibit** this fallback, and use only the verified candle close. There is no separate simulator slippage model for this MARKET path: additional modeled slippage is zero **as an idealization**, not observed spread/latency or a real fee quote. Spot funding/margin/liquidation are **inapplicable**, not invented as zero perpetual funding. Real exchange minimum notional, precision, fills, fee tier and live costs remain unverified.
- **Scope and capability:** one spot pair, one verified 1h feed, fully specified OHLCV-derived indicators, causal confirmed pivots and a completed-close MARKET/POSITION_HOLD event path require **no new engine primitive** beyond the previously independently reviewed pinned path (e.g. PR #414). This is static expressibility and reused primitive evidence, **not** a strategy-specific implemented controller, actual candidate backtest, executed trade, Qlib/Hummingbot parity, or production trading authorization.

## Evidence

### Source-reported
First-party TradingView 4juJumUH (thetraderlodge, 2025-08-22, Pine v6) explicitly describes pivot 3/3, volume multiplier 1.5 on volume SMA20, >1% open/close momentum, RSI3 >/< 50, VWAP direction, ATR14 x1/x9, and optional filters default **OFF** on an originally 1-second, long/short strategy. Full Pine bytes were not accessible in this research run; no original strategy events or backtest metrics are represented as independently verified.

### Independently reproduced
**None for this candidate.** This Scout inspected the pinned Hummingbot static execution path through the GitHub connector and reused previously independently audited wheel/source binding and representative MARKET/POSITION_HOLD primitive evidence in PR #414. No new controller, actual BTC replay, source-Pine event parity, Qlib parity, profitability or OOS measurement was performed.

### Negative evidence
The source does **not** verify this derivative's UTC VWAP anchor, strict pivot ties, activation delay, RSI/ATR seed conventions, enabled filters, one-hour timeframe, bracket-at-close execution, fixed size, modeled fees or full position state. Those are explicitly independent research decisions, not source-native facts. Historical same-close fills may understate real latency and risk. Nominal 1x ATR stop and 9x ATR target are not guaranteed realized price bounds. No claimed Survivor/HB Certified/real trading status.

## Falsification plan

After separate authorization for downstream research, compare a sequential independent indicator/event implementation with a strategy-specific pinned Hummingbot controller: pivot equal-high rejection, confirmation at j+3 and activation j+4, newly replaced pivot level, no same-bar pivot lookahead, UTC midnight VWAP reset, zero-volume session, Wilder RSI3/ATR14 seeds, strict volume/momentum threshold ties, simultaneous bracket/bearish-break priority, gap-through-stop actual-close fill, consumed pivot rearm, partial/rejected fill abort, full fee-net ledger and sample-end open inventory. Test raw-open feature join T versus effective completed-close T+3600 without shifting events; only newly unverified engine primitives require representative parity validation before large Qlib screening. No backtest or trade in this Scout cycle.

## Crypto portability

Only the declared Binance BTC-USDT **spot 1h** instance is evaluated. The original TradingView 1-second version and short-side behavior are not admitted by this record. Other pairs, frequencies, futures leverage/funding, 6/6/6 DCA or seven-coin campaign scope require separately frozen and verified downstream research specifications; none is an HB_READY entry prerequisite.

## Limitations

The frontmatter PASS is **Scout's six-gate admission proposal**, not an independent Hermes Auditor verdict. Original Pine source bytes unavailable; no source-native parity, installed wheel rehash, deployed strategy-specific controller, live price/fill guarantee, realized fees, candidate Qlib parity, Survivor or Paper/Testnet/Live approval. Independent Hermes Auditor GitHub Webhook Review alone decides exact-head PASS merge, source-fact remediation or NOT_LOSSLESS close. The existing signed webhook receiver alone updates README count after a confirmed accepted merge.

## Implementation status

not-implemented: the derived strategy-specific controller and feature-state implementation are not present in this research PR. No backtesting, deployment, container, cron or workflow change is authorized or performed.

## Adoption boundary

status: research-only; implementation_status: not-implemented; adoption: not-approved; approval_scope: research-only. This single record is a proposed research candidate only.

## Sources

- https://www.tradingview.com/script/4juJumUH-Instant-Breakout-Strategy-with-RSI-VWAP/ — thetraderlodge, 2025-08-22, public Pine v6 strategy description read 2026-10-28.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine files read using connected GitHub.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — previously independent wheel/source and representative engine-path audit, not re-executed here.
