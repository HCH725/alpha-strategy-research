---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "SoftKill21 PSAR/CMF20/RSI50/ADX14-EMA14 four-way agreement — independently derived BTC-USDT spot 1h long-flat"
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-29
sources:
  - https://www.tradingview.com/script/yFwSIDYf-Full-strategy-Psar-adx-cmf-rsi/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Four-way PSAR + Chaikin Money Flow + RSI + ADX/EMA confirmation — independent derivative

## Provenance

Primary TradingView public **open-source** strategy page: **Full strategy Psar+ adx + cmf + rsi**, author **SoftKill21**, published **2021-04-13**, stable script identity **yFwSIDYf**. Public URL: https://www.tradingview.com/script/yFwSIDYf-Full-strategy-Psar-adx-cmf-rsi/ . Directly read the first-party page on **2026-10-29**. Its accessible description, not its Pine source bytes, is the evidence for the source's four-way mechanism. The complete Pine text, exact source revision, original indicator lengths/seeds, order timing, sizing, costs and position state are **not accessible** through this read; do not imply a source-native or byte-identical reproduction.

**Source-reported facts only:** the author describes **long-only** trading; enter when PSAR indicates an uptrend, CMF is positive, RSI (with a relatively long length) exceeds the 50 midpoint, and ADX exceeds an EMA of ADX. The described exit checks the opposite: PSAR downtrend, negative money flow, RSI below 50 and ADX below its EMA. No independently checked source code or quantitative performance is available from this page.

**Independently specified derivative, NOT the author's exact Pine strategy:** Binance BTC-USDT **spot** UTC **1h**; the precise PSAR recursion/seed below with AF 0.02/0.02/0.20; **CMF20**, **Wilder RSI50**, **Wilder ADX14**, **EMA14 of ADX14**; all four conditions must simultaneously hold for entry and all four opposite conditions for exit; 200 complete-bar warmup; one fixed **0.001 BTC** long; initial cash **10,000 USDT**; pending action at decision bar t executed as an idealized MARKET order at the **observed completed close of t+1**; a hypothetical **0.1% fee on each filled side**; no SL/TP/trailing, short, DCA, partial orders or cooldown. Every numeric length, strict equality rule, SAR initialization, time/venue, order state and economic assumption in this derivative is a **researcher choice**, not a fact asserted about the original script. Original PSAR/CMF/RSI/ADX directionality and four-way agreement are the only adopted source-native concepts.

**Immutable derivative identity:** TV:yFwSIDYf:SoftKill21:published-20210413:read-20261029 | independently-derived-v1-20261029 | BINANCE:BTC-USDT:SPOT:UTC-1h | PSAR-Wilder-start0.02-step0.02-cap0.20-seed-t1 | CMF20-sign | RSI-Wilder50-mid50 | ADX-Wilder14-vs-EMA14 | four-way-AND-entry-and-opposite-AND-exit | LONG-FLAT | Q0.001BTC:cash10000USDT | warmup200 | signal-completed-t-to-MARKET-completed-close-t+1 | fee0.001-per-filled-side. Any changed seed, comparator, direction, exit aggregation, fill, sizing or venue is a distinct strategy.

**Dedup at pre-write main SHA 9b495adcb4c92e171aacc026d5f020f3370ca307:** the complete nontruncated main tree contains **426** root strategy Markdown records and the README static count is **426**. Seven distributed sampled frontmatters are PASS; this is **not** a 426-record status audit. GitHub default-branch code search found no script ID yFwSIDYf or SoftKill21; all-state PR searches found no matching ID/author; the ten open research PRs have different primary sources. Closest admitted PSAR relatives include bare PSAR flip, PSAR+EMA50 reversal, and CHOP/DMI/PSAR reversal; CMF relatives use CMF sign or CMF velocity without this four-indicator conjunctive gate. This source and four-way PSAR+CMF+long-RSI+ADX-vs-own-EMA entry **and** four-way opposite exit are materially different from those mechanisms, not a parameter-only variant.

## Economic mechanism

### Source-reported

The author seeks alignment of trend direction (PSAR), positive/negative Chaikin money flow, momentum above/below the RSI midpoint, and ADX strength relative to its own EMA. Source description contains no verified historical returns, fees, fill data, parameter table or risk guarantees.

### Research interpretation

Four independent sign/regime tests are deliberately conjunctive. The long may remain open through individual bearish sub-signals because **all four bearish tests** are required to exit. This can reduce turnover but may prolong severe losses. That is a falsifiable hypothesis, not a profitable-strategy claim.

## Signal

**Data/clock:** one ordered stream of fully closed Binance BTC-USDT spot 1h candles indexed t=0,1,..., with exchange open timestamp T[t] and effective completed-bar availability E[t]=T[t]+3600 seconds (UTC). All arithmetic uses chronological float64 OHLCV, deterministic arithmetic, no training/fitting, no full-sample ranking. Inputs must be finite, O/H/L/C strictly positive, H>=max(O,C), L<=min(O,C), volume finite and >=0, unique timestamps exactly 3600 seconds apart. Any missing, duplicate, unfinished, invalid, interpolated, synthetic or gap-bridged candle aborts the research run, not a silent fill or reset.

**1. PSAR (research-pinned Wilder-style, computed from completed H/L/C):** at t=1 initialize BULL if C[1]>=C[0], otherwise BEAR; EP=max(H[0],H[1]) for BULL or min(L[0],L[1]) for BEAR; SAR[1]=min(L[0],L[1]) for BULL or max(H[0],H[1]) for BEAR; AF=0.02. SAR[0] and trend[0] are undefined. For every t>=2, tentative SAR = prior SAR + prior AF*(prior EP-prior SAR). If prior BULL, clamp tentative SAR to min(tentative,L[t-1],L[t-2]); if L[t]<=clamped SAR, flip to BEAR with SAR[t]=prior EP, EP[t]=L[t], AF[t]=0.02; otherwise stay BULL with SAR[t]=clamped SAR, EP[t]=max(prior EP,H[t]), and AF[t]=min(0.20,prior AF+0.02) **only if H[t]>prior EP**, else retain prior AF. For prior BEAR, clamp tentative SAR to max(tentative,H[t-1],H[t-2]); if H[t]>=clamped SAR, flip to BULL with SAR[t]=prior EP, EP[t]=H[t], AF[t]=0.02; otherwise stay BEAR with SAR[t]=clamped SAR, EP[t]=min(prior EP,L[t]), and AF[t]=min(0.20,prior AF+0.02) **only if L[t]<prior EP**, else retain prior AF. SAR comparisons use the completed candle's H/L only after E[t]; this is NOT an intrabar executable stop order. PSAR_UP[t] means state BULL and C[t]>SAR[t]; PSAR_DOWN[t] means state BEAR and C[t]<SAR[t]. Equality is neither.

**2. CMF20:** for each bar define money-flow multiplier MFM[t]=(2*C[t]-H[t]-L[t])/(H[t]-L[t]) if H[t]>L[t], otherwise 0. Money-flow volume MFV[t]=MFM[t]*V[t]. At t>=19, CMF[t]=sum(MFV[t-19..t])/sum(V[t-19..t]) if the 20-bar volume sum is positive, otherwise 0. Undefined before t=19. No forward-filled volume. POSITIVE_CMF iff CMF>0; NEGATIVE_CMF iff CMF<0; equality neutral.

**3. Wilder RSI50:** deltas D[t]=C[t]-C[t-1] for t>=1; G=max(D,0), L=max(-D,0). At t=50, seed avgGain=mean(G[1..50]), avgLoss=mean(L[1..50]); afterward recur avgX[t]=(49*avgX[t-1]+X[t])/50. If both averages are zero RSI=50; if only avgLoss is zero RSI=100; if only avgGain is zero RSI=0; otherwise RSI=100-100/(1+avgGain/avgLoss). Undefined before t=50. Bullish iff RSI>50, bearish iff RSI<50; equality neutral.

**4. Wilder ADX14 versus EMA14(ADX):** for t>=1, TR=max(H[t]-L[t],abs(H[t]-C[t-1]),abs(L[t]-C[t-1])); up=H[t]-H[t-1], down=L[t-1]-L[t]; +DM=up iff up>down and up>0, else 0; -DM=down iff down>up and down>0, else 0. Seed Wilder RMA14 of TR,+DM,-DM as arithmetic means of t=1..14; afterward recur RMA=(13*prior+current)/14. DI_plus and DI_minus are 100 times respective smoothed DM divided by smoothed TR; when TR denominator is zero both DI=0. DX=100*abs(DI_plus-DI_minus)/(DI_plus+DI_minus), or 0 when denominator is zero. Seed ADX[27]=mean(DX[14..27]); afterward ADX=(13*priorADX+DX)/14. ADX undefined before 27. Seed EMA14(ADX)[27]=ADX[27], then EMA[t]=(2/15)*ADX[t]+(13/15)*EMA[t-1]. Bullish strength iff ADX>EMA14(ADX); bearish strength iff ADX<EMA14(ADX); equality neutral. All seeds and ties here are researcher-defined.

**Four-way decision:** BUY_COND[t] = PSAR_UP[t] AND CMF20[t]>0 AND RSI50[t]>50 AND ADX14[t]>EMA14(ADX14)[t]. SELL_COND[t] = PSAR_DOWN[t] AND CMF20[t]<0 AND RSI50[t]<50 AND ADX14[t]<EMA14(ADX14)[t]. The conditions are mutually exclusive; no opposite signal can be simultaneously true. They are **levels, not crosses**: while FLAT, a true BUY_COND on a legal decision bar requests one entry; while LONG, a true SELL_COND requests one exit. A false or neutral conjunction does nothing. No partial-agreement exit, stop or profit target is silently substituted. Every decision is evaluated only at E[t].

## Required data

Exactly one Binance Spot BTC-USDT 1h OHLCV stream with actual open-time stamps, O/H/L/C/V and full 200 consecutive-bar prehistory; no second timeframe, cross-asset inputs, order book, tick data, fundamentals, funding, ML features or synthetic prices. For first trade, all 200 completed candles t=0..199 are warmup-only; earliest signal is t=200, earliest simulated fill E[201]. Every feature is computed incrementally from past/current **completed** bars. No current candle is treated as complete before E[t]. No lookahead, negative shifts, future extrema, full-sample normalization or repainting.

## Execution assumptions

**Direction and order state (Gates 2–4):** Binance BTC-USDT spot LONG/FLAT only. Start with FLAT, 10,000 USDT and zero BTC. State machine FLAT -> BUY_PENDING -> LONG -> SELL_PENDING -> FLAT; one 0.001 BTC unit and at most one pending action. A true BUY_COND while FLAT at E[t] queues a MARKET BUY for the next bar; a true SELL_COND while LONG queues a MARKET SELL of the **confirmed full inventory**. While pending, do not evaluate or queue another action. At row t+1, dispatch the saved t decision and fill at the **actual completed C[t+1]** with effective fill time E[t+1], then mark the confirmed state. Ignore signals on the fill bar; a later completed bar can re-enter if the full four-way entry conjunction is true. No pyramiding, short, reverse, leverage, borrowing, DCA, safety orders, partial TP, compounding, cooldown, concurrent position, session restriction or time limit. SL, TP, trailing, breakeven, and forced terminal liquidation are **explicitly disabled**. An unclosed long at tape end is marked unrealized at the last real close; a final pending action without a following real candle remains unfilled. Missing-price, partial, rejected, stale, insufficient-cash, unconfirmed or otherwise unreconciled fill **aborts**; do not fabricate a completed trade.

**Pinned Hummingbot Gate 5:** source repository https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 , package **20260920**, VERSION **dev-2.17.0** (VERSION read directly from pinned GitHub commit on 2026-10-29). The existing merged Alpha PR #414 records 902/902 pinned source/wheel byte agreement and a 33-assert representative validation for this engine; **not rerun** in this Scout. The pinned Binance Spot candle feed (hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py and constants.py, read this cycle) exposes 1h, parses real Binance Klines row[0] open time and rows[1..5] O/H/L/C/V. BacktestingEngineBase.run_backtesting -> simulate_execution -> update_state(row) -> controller.determine_executor_actions() -> simulate_executor(OrderExecutorConfig) is the actual inspected per-row path. A minimal future **strategy-specific** controller would hold the above decision/state and dispatch the prior bar's queued action on row t+1, not pretend Hummingbot ships a PSAR/CMF/RSI/ADX strategy. The pinned OrderExecutorConfig accepts connector_name=binance, trading_pair=BTC-USDT, BUY/SELL, amount Decimal(0.001), position_action OPEN/CLOSE, execution_strategy MARKET, leverage=1. Pinned OrderExecutorSimulator.simulate uses the first supplied row's **actual close** as MARKET fill, filled_amount_quote=amount*close, cum_fees_quote=trade_cost*amount*close and CloseType.POSITION_HOLD; BacktestPositionHold nets confirmed BUY/SELL position quantities and tracks realized PnL separately from fees. This demonstrates the **bounded historical next-completed-close MARKET model** only, not a live market-at-close guarantee.

**Timestamp guard:** raw Binance Kline timestamp T[t] is bar **open**; a controller may dispatch at row t+1 only using t's saved decision. The model's fill and available information are effective at E[t+1], not falsely at T[t+1]. The price used for fill/mark must be finite positive observed C[t+1]. The pinned BacktestingDataProvider.get_price_by_type can return Decimal(1) for an absent pair; explicitly reject that fallback and abort on missing actual market price. No invented open, midpoint, spread, impact or maker fills. The engine's default recent-executor window may expire old records; reconcile the **complete** terminated-executor/position-hold history, not a truncated 3600s view.

**Spot ledger/cost model:** hypothetical fee rate f=0.001 per confirmed side (not claimed as historical Binance tier), initial cash 10000 USDT, initial BTC=0. BUY Q=0.001 at actual P debits Q*P*(1+f) and credits Q BTC; SELL debits confirmed Q BTC and credits Q*P*(1-f). Matched fee-inclusive realized PnL = Q*(P_sell-P_buy)-f*Q*(P_buy+P_sell). Track cash/inventory with Decimal from executor-confirmed fills; require sufficient cash, positive finite prices, no oversell, and reconcile net BTC and USDT totals with BacktestPositionHold within 1e-9 BTC / 1e-8 USDT diagnostic tolerance; any discrepancy blocks the run. Market min-notional/lot/precision and historical tier fees are **not independently verified**, so this is research accounting, not a claim of executable live orders. Spread/slippage/latency are unmodeled, not reported as observed zero. This is **unlevered spot**, so perpetual-futures funding is inapplicable; no fictitious realized zero-funding data are supplied.

## Evidence

### Source-reported

TradingView author SoftKill21 (2021-04-13) reports the PSAR/CMF/RSI-midpoint/ADX-vs-EMA long-only four-way entry and opposite exit idea, without independently verifiable performance or full accessible Pine source. Source-native claims are limited to those qualitative facts.

### Independently reproduced

**Not independently reproduced.** No candidate-specific Hummingbot/Qlib backtest, event-level parity, fee-realistic simulation, performance, OOS, Survivor or trading authorization was performed. The pinned engine source paths were inspected; PR #414's prior capability evidence is reused, not falsely presented as a new candidate run.

### Negative evidence

Original Pine bytes, exact PSAR/CMF/RSI/ADX seeds, all default lengths, author execution settings, fill semantics, original costs and full exit-state code are not accessible from the primary-source text. This record is an **independent derivative**, never lossless source reconstruction. A four-way opposite exit can leave a long exposed for an unlimited period. Source performance and reproducible historical trade counts are unavailable. Missing or partial actual candle data, unsupported real fill/precision/fee behavior, and any mismatch with pinned source/wheel or ledger reconciliation block the bounded execution claim. Seven sampled main records were PASS, not a complete 426-record admission audit.

## Falsification plan

After separate downstream authorization, compare frozen four-way conjunction against (a) PSAR-only trend state, (b) the same PSAR+CMF+RSI without the ADX/EMA gate, and (c) the same entry with any-single-bearish-factor exit, **as separately labeled hypotheses**, never silently altering this admitted record. Evaluate full contiguous tradable windows with explicit modeled fees and flat time, no hindsight tuning; test indicator seeds, zero-range/zero-volume/RSI zero denominator, PSAR equality and reversal, ADX/EMA equality, long hold through mixed signals, t/t+1 effective timestamps, missing-price fallback, failed fills, and terminal open inventory. Before mass Qlib screening of a new execution path, require representative Qlib/Hummingbot event-level capability parity, not a new HB_READY gate.

## Crypto portability

BTC-USDT spot 1h is the sole pinned market/frame. ETH/SOL/other assets, futures/perpetual, 3x/5x leverage, BO/SO 6/6/6 or different frames are **separate downstream experiments**, not requirements or verified equivalences of this source/derivative. Any new venue, precision, funding, shared-capital or execution primitive requires its own demonstrated path.

## Limitations

Researcher-selected lengths and state semantics can materially differ from SoftKill21's actual Pine; no claims of source-native order-event parity. Next-completed-close MARKET historical fills are idealized; they do not prove realizable close prices. No risk stop, no realistic spread/slippage, no actual tier fees, no live exchange-order acceptance, no strategy-specific controller implementation, and no demonstrated profitability. PASS is expressibility under the bounded pinned model, not certification of returns or permission to trade.

## Implementation status

**not-implemented**: a minimal strategy-specific controller, candle validation, order-state ledger and Replay artifact would be needed if separately selected for downstream execution. No code, backtest, container, cron, trading or pipeline change is part of this Scout.

## Adoption boundary

**hb_ready_status: PASS is the Scout's proposed six-gate finding, pending independent Hermes Auditor GitHub Webhook Review**, not an independently completed audit. status=research-only; implementation_status=not-implemented; adoption=not-approved; approval_scope=research-only. Only an exact-head independent PASS permits merge; NOT_LOSSLESS closes this Scout PR. The existing signed webhook receiver alone owns README count bookkeeping after a verified merge. No main files or prior strategy statuses are modified.

## Related Wiki records

None asserted. Existing PSAR, CMF and ADX family records are comparators, not proof of this strategy's performance or source-native identity.

## Sources

1. First-party TradingView: https://www.tradingview.com/script/yFwSIDYf-Full-strategy-Psar-adx-cmf-rsi/ (SoftKill21, 2021-04-13; read 2026-10-29).
2. Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 (package 20260920; VERSION dev-2.17.0; engine/data/ledger files directly inspected 2026-10-29).
3. Existing pinned source/wheel capability evidence (not candidate backtest): https://github.com/HCH725/alpha-strategy-research/pull/414 .
