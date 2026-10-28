---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "PuestoGlobal symmetrical-triangle downside false-break recovery — independently specified BTC-USDT spot 1h long-flat derivative"
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
source_as_of: 2025-08-16
sources:
  - https://www.tradingview.com/script/g353R1oY/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Symmetrical-triangle downside false-break recovery — independent research derivative

## Provenance

- **Primary TradingView source:** PuestoGlobal, *Symmetrical Triangle Strategy (Real and Trap confirmation)*, published **2025-08-16**, public open-source script identity **g353R1oY**, https://www.tradingview.com/script/g353R1oY/. The first-party public description was read on 2026-10-28. The full Pine source bytes/version were **not** retrieved, so no claim of exact Pine, chart-pivot, fill, or event parity is made.
- **Source-reported mechanism only:** the author describes a triangle whose last pivots (H3/L3) may be broken; a strong volume/RSI-confirmed breakout trades with the break, while a weak break creates a pending *trap* that enters against the break after price returns inside the triangle. An optional EMA confirmation and a trap timeout are described. The source explicitly says its strategy is an entry system **without stop loss or take profit**. The public prose does not expose complete pivot/tie formulas, default lengths, thresholds, sizing, candle timing, state transitions, or executable fills.
- **Independent, explicitly derived strategy (NOT source-native):** this record selects only the **downside-break → return-inside → LONG** trap leg. The researcher independently defines strict 3-left/3-right pivots, two-high/two-low converging linear boundaries, 1h Binance spot, a weak-break OR filter (volume20 ×1.2 / RSI14 ≤45), three-bar trap timeout, fixed entry-frozen midpoint target, ATR14-based close stop, twelve-bar time exit, no optional EMA, a single 0.001-BTC position, completed-close historical MARKET simulation, 0.1%-per-side modeled fees, and complete deterministic state. **Every listed difference can change events**; it is not a repair of missing native Pine facts or an assertion that the author's original passes HB_READY.
- **Frozen identity:** TV:g353R1oY|PuestoGlobal|2025-08-16|independent-triangle-downtrap-v1-2026-10-28|BinanceSpot-BTC-USDT-UTC1h|strict-pivot-3L3R-next-bar|last-two-descending-highs-last-two-ascending-lows-linear-lines|weak-volume20x1.2-OR-WilderRSI14le45|reentry-3bars|midpoint-target|low-minus-ATR14-stop|12bar-timeout|Q0.001BTC|cash10000USDT|same-completed-close-MARKET|fee0.001|warmup150. Altering any signal, anchor, timing, cost, execution or state convention defines another strategy.
- **Dedup:** on connected GitHub main SHA 2d6c484fd06a11c870995b191265042f708b99db, 410 root strategy Markdown files match README 410; 13 spread-out records sampled were PASS. GitHub code/source-ID search for g353R1oY and PR search for the source or triangle mechanism found no match; all ten open research/* PRs concern other sources. Main includes ordinary breakout/pivot and R-Breaker reversal families but no frozen converging-triangle downside-failure recovery/three-bar pending state. This is a bounded search, not an exhaustive mathematical equivalence proof.

## Economic mechanism

### Source-reported
A weak triangle breakdown can fail: if price re-enters the pattern, the original publication proposes trading against the failed move, rather than treating every breakout as genuine.

### Research interpretation
Testable hypothesis only: a downward false break of converging pivot boundaries followed by a quick close back inside may mean-revert toward the entry-time triangle midpoint. No profitability, Sharpe, win rate, Survivor or independently reproduced TradingView result is asserted.

## Signal — complete independent derived specification (Gates 1–4 and 6)

1. **Data/time:** one Binance BTC-USDT spot UTC 1h OHLCV stream. Bar t (zero-based) has opening Unix timestamp T[t] exactly one hour after T[t-1]; its O/H/L/C/base-BTC V are available only at **T[t]+3600**, after the complete bar closes. Require finite positive O/H/L/C, finite V≥0, L≤min(O,C)≤max(O,C)≤H, no duplicates, gaps, unfinished candles or forward fills. A missing/invalid bar, missing executable close or inconsistent fill aborts the entire run even when LONG; never fabricate prices, fills or a terminal liquidation.
2. **Volume:** Vmean20[t] = sum(V[t-i], i=0..19)/20 including the current *completed* bar. Require Vmean20[t]>0 for a candidate breakdown. WeakVolume[t] iff V[t] ≤ 1.2 × Vmean20[t] (equality is weak).
3. **Wilder RSI14:** Δ[i]=C[i]-C[i-1]. At t=14 seed avgGain=sum(max(Δ[i],0),i=1..14)/14 and avgLoss=sum(max(-Δ[i],0),i=1..14)/14; subsequently G[t]=(13G[t-1]+max(Δ[t],0))/14, Ls[t]=(13Ls[t-1]+max(-Δ[t],0))/14. RSI=100−100/(1+G/Ls), with zero-loss/positive-gain=100, zero-gain/positive-loss=0, both zero=50. WeakRSI[t] iff RSI[t]≤45. A breakdown is weak iff WeakVolume[t] OR WeakRSI[t]; no other RSI, trend or EMA filter is used.
4. **Wilder ATR14:** TR[0]=H[0]−L[0]; for i>0, TR[i]=max(H[i]−L[i], abs(H[i]−C[i-1]), abs(L[i]−C[i-1])). Seed ATR[13]=mean(TR[0..13]); then ATR[t]=(13ATR[t-1]+TR[t])/14. A buy requires finite ATR[e]>0. No future volatility, intrabar stop or rolling post-entry recalibration.
5. **Strict causal pivots:** pivot high center j≥3 iff H[j] is **strictly greater** than each H[j−3..j−1] and H[j+1..j+3]; pivot low center j≥3 iff L[j] is strictly less than all six adjacent lows. Equal extrema disqualify a pivot. Center j is confirmed only on the completed close of j+3; its information becomes usable **from j+4 onward**. Maintain two latest confirmed highs and two latest confirmed lows by ascending center index. Ties between simultaneous high/low confirmations update both pools first, then consider one pattern.
6. **Triangle creation:** only when FLAT, with no pending trap, and at least one new pivot confirmation on bar f, select latest two highs (h1<h2) and latest two lows (l1<l2). Require all four center indices ≥f−100; H[h2]<H[h1] and L[l2]>L[l1] (strict convergence). Freeze this four-pivot tuple once; repeated bars without a new pivot cannot recreate it. For integer k≥f define U[k]=H[h2]+(H[h2]−H[h1])×(k−h2)/(h2−h1), D[k]=L[l2]+(L[l2]−L[l1])×(k−l2)/(l2−l1). Require finite U[f],D[f],U[f+1],D[f+1], U>D on both bars, and no reused tuple. Activate only at **f+1**; a newly confirmed pivot never revises a frozen pattern. If a new eligible tuple confirms while FLAT/no pending, retire the older pattern and replace it. A pattern expires when k−f>60 or U[k]≤D[k], whichever occurs first.
7. **Downside weak-break arm:** on an active unconsumed pattern and a completed bar b≥f+1, require D[b−1]≤C[b−1]≤U[b−1], C[b]<D[b], Vmean20[b]>0, and (WeakVolume[b] OR WeakRSI[b]). Record pending (pattern ID,b,L[b]), valid only for bars b+1 through b+3. **No order is placed on breakdown bar b.** Ignore any further pivot confirmations while pending; do not silently replace the frozen boundaries.
8. **Trap recovery BUY:** on the first completed bar e∈[b+1,b+3] for which U[e]>D[e], C[e−1]≤D[e−1], and **D[e]<C[e]<U[e]**, calculate P=C[e], target=(U[e]+D[e])/2, stop=min(L[b],L[e])−ATR[e]. Require target>P, stop<P, ATR[e]>0 and adequate fee-inclusive cash. Otherwise, if a recovery edge occurs but its bracket is invalid, consume/retire the pattern without buying. If C[e]≥U[e], U[e]≤D[e], the pattern expires, or the b+3 close passes without valid recovery, cancel pending and retire the pattern; do not queue a later trade. Submit one MARKET BUY of Q=Decimal("0.001") BTC at the **actual completed C[e]** on the pinned historical close-fill path. Only a verified full fill creates LONG and freezes P, target, stop, entry bar e and the consumed pattern ID. Never trade on the breakdown bar.
9. **LONG exit/priority:** on a subsequent completed bar u>e, evaluate in order: (a) C[u]≤frozen stop; else (b) C[u]≥frozen target; else (c) u−e≥12. At the first true condition submit exactly one full-Q MARKET SELL at **actual C[u]** (not at stop/target); record the highest-priority reason. Close thresholds are completed-close checks, **not** intrabar high/low touches or exchange stop/limit orders. After verified full fill return FLAT; the consumed triangle cannot rearm, and a new distinct confirmed pivot tuple must arise before another setup.
10. **State/position:** deterministic states FLAT/no-pattern, FLAT/armed-pattern, FLAT/pending-trap, LONG. Only one active triangle, one pending event, one position and at most one order/action per completed bar. Start cash Decimal("10000") USDT, base inventory 0; BUY needs cash≥Q×P×(1+f), f=Decimal("0.001"). On full BUY subtract Q×P×(1+f); on full SELL add Q×P×(1−f); realized net round trip Q×(P_sell−P_buy)−f×Q×(P_buy+P_sell). Update state and cash **only from confirmed executor fills**. Missing, stale, rejected, partial, inconsistent or nonfinite fills abort rather than being assumed. No shorts, reversal, leverage, margin, pyramiding, DCA/safety orders, concurrency, compounding, cooldown beyond the pattern-consumption rule, maker/limit execution, trailing stop, discretionary exits or other orders. Do not enter again on an exit bar.
11. **Warmup/end:** require **150 consecutive valid completed prior 1h candles** before any first eligible decision (t≥150), and all necessary confirmed pivot/indicator history. No first decision on incomplete bar, no future pivot center, no use of same-bar unconfirmed pivot. If LONG at last valid completed candle, report inventory and actual-close mark-to-market separately; **no fabricated final SELL**. Do not count the warmup as tradable time.

## Required data

Only one UTC-hourly Binance spot BTC-USDT OHLCV feed and its actual open timestamps, high/low/close/base volume. All features and projected triangle lines use already confirmed pivots and fully completed candles; no external ML, order book, second timeframe, portfolio synchronization, future extrema, intrabar fill, futures funding or mark price is required. Raw feed continuity, 150-bar predecision buffer and actual last-candle completion must be checked before provider backtest-window truncation; requesting max_records alone is insufficient.

## Execution assumptions — pinned Gate 5

- **Immutable engine:** Hummingbot package label **20260920**, VERSION **dev-2.17.0**, source commit **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3**. Connected GitHub inspection this cycle verified VERSION, BinanceSpotCandles interval **1h**, REST Kline timestamp/open/high/low/close/base-volume parsing, BacktestingDataProvider, BacktestingEngineBase and OrderExecutorSimulator. The package label differs from historical setup.py distribution version; independent PR #414 previously reported SHA256 **ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148**, 902/902 Python files byte-identical and representative 33-assert execution validation. This Scout **did not re-hash the installed wheel**; the prior audited binding is cited, not freshly claimed.
- **Causal feed/join:** BinanceSpotCandles supports 1h; REST row[0] is the bar-open epoch, row[1..5] O/H/L/C/base volume. BacktestingDataProvider retrieves a buffered historical feed but get_candles_df truncates to the run window; the strategy-specific feature preparation must first check actual contiguous pre-run history. BacktestingEngineBase.prepare_market_data performs backward merge_asof with raw-open candle timestamp. Index causal feature rows by **T[t]**, not T[t]+3600; store availability_at/decision_at/logical_fill_at as **T[t]+3600** separately. The simulator's timestamp is the raw-open **label**, not a claim of pre-close information. The historical same-close MARKET fill is an explicit idealization, not a guaranteed achievable live price.
- **Executor/fill:** OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1). Pinned OrderExecutorSimulator MARKET selects first supplied row, fills at that row's **actual close**, computes filled_amount_quote=Q×close, cum_fees_quote=trade_cost×filled_amount_quote, and CloseType.POSITION_HOLD. Use a controller-owned confirmed-fill ledger rather than lagging terminated-executor views; each new order requires a valid price row and confirmed fill. Strategy-specific controller is **not implemented** but every state transition and data requirement is declared here.
- **Fees/accounting:** run_backtesting(trade_cost=0.001) supplies **hypothetical 0.1% per-side fees**, not observed Binance fees. BacktestPositionHold accumulates gross exposure/PnL and cum_fees_quote; reconstruct fee-inclusive cash/equity from executor fills, not gross net_pnl_quote alone. Float→Decimal reconciliation tolerances are 1e-9 BTC inventory and 1e-8 USDT fees; abort if exceeded. Explicitly forbid BacktestingDataProvider.get_price_by_type fallback Decimal("1") when prices are missing. MARKET simulator has no separate slippage primitive for this path; additional simulated slippage **zero is a modeling idealization**, not observed spread or execution realism. Spot funding, liquidation and futures margin are **inapplicable** (not fabricated zero funding). Exchange precision, minimum notional, tiered fees, live fills and latency are not independently verified.
- **Bounded expressibility:** the only execution primitive is one verified spot 1h completed-close MARKET/POSITION_HOLD path with one position, OHLCV-derived state and close-based bracket/time exit. This reuses pinned static and representative engine evidence, not an unverified intrabar/maker/multi-timeframe path. It is **not** an implemented candidate backtest, source-native Pine parity, Qlib/Hummingbot parity or production authorization.

## Evidence

### Source-reported
PuestoGlobal's public 2025-08-16 TradingView description directly states triangle breakout vs failed-break trap, volume/RSI quality confirmation, reentry inside the pattern, optional EMA confirmation, opportunity timeout, and **no native stop loss or take profit**. Full Pine source was not available through the public page retrieval; no native pivot default, execution parameter, code-version or performance metric is asserted.

### Independently reproduced
**Not independently reproduced for this derivative.** The pinned source-level execution primitives were inspected via connected GitHub, and prior independent PR #414 wheel/source plus representative event-path validation is cited. No strategy-specific controller, TradingView event replay, Hummingbot backtest, Qlib parity, OOS, profitability or survivor measurement occurred.

### Negative evidence
Native H3/L3 exact construction, filter thresholds, trap timeout, EMA state, original order fills and full Pine code remain unavailable. Every decision-critical replacement is explicitly **researcher-defined**, including the two-pivot converging-line definition, weakness thresholds, selected long-only leg, midpoint target, ATR stop and time exit. They cannot be represented as native facts or as an original strategy's HB_READY PASS. Same-close fills, assumed 0.1% costs and absent market-impact simulation may materially overstate performance.

## Falsification plan

With separate downstream authorization, independently replay strict 3L/3R ties, center-to-confirmation lag, four-pivot ordering and activation, line projections and apex, equal-threshold weak filters, b+1..b+3 recovery edge, invalid target rejection, expiration and pattern consumption, frozen ATR stop/midpoint target, twelve-bar timeout, close-only gap behavior, fill and fee ledger, rejected/partial fill abort and end-sample inventory. Compare raw-open join labels T[t] to logical availability T[t]+3600 and check no early pivot activation. Validate representative new engine primitives only if introduced before mass Qlib screening; none is authorized in this Scout.

## Crypto portability

The admission proposal is **only** Binance BTC-USDT spot 1h, one long position and the frozen derivative. Original TradingView real-breakout/short legs, other markets/timeframes, futures leverage/funding and any 6/6/6 DCA campaign overlay are not part of this identity; none is a universal HB_READY admission prerequisite.

## Limitations

Frontmatter PASS is **Scout's proposed six-gate result awaiting independent Hermes Auditor review**, not a self-approved merge. No claim of source-native fidelity, strategy-specific implementation, actual replay, real costs, Qlib parity, Survivor/HB Certified or Paper/Testnet/Live suitability. Only the independent Hermes Auditor GitHub Webhook Review may remediate source-verifiable facts, merge an exact-head PASS or close a NOT_LOSSLESS Scout PR. Only the existing signed webhook receiver owns post-merge README bookkeeping.

## Implementation status

not-implemented: the strategy-specific controller, causal pivot/triangle state and execution ledger are not deployed or added by this PR.

## Adoption boundary

status: research-only; implementation_status: not-implemented; adoption: not-approved; approval_scope: research-only. One proposed root-level research record only.

## Related Wiki records

None. No additional registry, checker, downstream gate or Wiki artifact is created.

## Sources

- https://www.tradingview.com/script/g353R1oY/ — PuestoGlobal, *Symmetrical Triangle Strategy (Real and Trap confirmation)*, 2025-08-16, first-party TradingView publication.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine source inspected via connected GitHub.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — previously independently audited wheel/source and representative execution primitive evidence, not rerun here.
