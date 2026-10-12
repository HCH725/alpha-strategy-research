---
schema: strategy-research-record-v1
hb_ready_status: NOT_ASSESSED
title: OtherSideBJ-inspired strong-momentum EMA pullback with risk-sized 3R/5R scale-out on BTCUSDT 1h (explicit derivative proposal)
created: 2026-10-12
updated: 2026-10-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: low
source_as_of: 2026-10-12
sources:
  - https://x.com/othersidebj/status/2109475443929972794
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# OtherSideBJ-inspired strong-momentum pullback and 3R/5R scale-out (BTCUSDT 1h derivative proposal)

## Provenance

- Primary attribution supplied directly by the researcher: X / @OtherSideBJ (另一面), https://x.com/othersidebj/status/2109475443929972794 . The researcher supplied four screenshots with this post. The X page could not be independently fetched in this research session; the following source-reported summary is constrained to the visible screenshots. `source_as_of` is the date the researcher supplied them, **not** a verified post publication date.
- Screenshot 1: rank strong US stocks by 1/3/6-month gains, favor >30% and top ~20–30%, avoid thin-volume issues; observe tightening consolidation, rising lows, 9/21 EMA recovery.
- Screenshot 2: identify daily support using 9/21/50-day EMA, anchored VWAP, previous highs/lows and unfilled gaps; then use 1/5/15-minute candles to buy a support retest/rebound and a break above the preceding candle high.
- Screenshot 3: predefine stop (intraday structural low or trigger candle's prior low); size as account risk divided by per-share loss (example 10,000 USD, 0.5%=50 USD, 20 entry, 19.50 stop, 100 shares).
- Screenshot 4: sell part near 3R/5R and use EMA9 / price structure to follow the remainder.
- **This is an explicitly researcher-designed crypto derivative, NOT a lossless encoding of the post.** Source examples use US equities, daily screening and minute execution, discretionary support/AVWAP/consolidation and unspecified partial-exit percentages. The pinned derivative below substitutes BTCUSDT perpetual 1h candles, objective EMA9 touch and breakout, an absolute 30-day return gate rather than cross-sectional ranking, an explicit 6-bar structural stop, 40/40/20 scale-out fractions, a 3x leverage cap, and specified bar/fill priorities. None of these invented thresholds or platform adaptations are attributed to @OtherSideBJ.
- Reproducibility boundary: X screenshots are attached to the user's conversation, not presently stored in GitHub. Source text, images and full original implementation are **not** independently verified. Do not promote this record as a source-native clone.

## Economic mechanism

### Source-reported

The illustrated workflow attempts to avoid buying weak names, enter an uptrend on a controlled pullback at support only after momentum resumes, limit ex ante dollar loss, realize part of upside at reward multiples, and follow the remaining trend.

### Research interpretation

A regime-conditioned continuation strategy: require substantial prior momentum, let price revisit a fast average without breaking the slower trend filter, enter on the first hourly confirmation of renewed buying, cap risk at a predetermined structural stop, then scale out at fixed risk multiples. Neither positive expectancy nor crypto transferability has been established.

## Signal

**Proposed deterministic research rules for ONE pinned market and timeframe (subject to HB_READY reviewer evidence):**

- Market: `BTCUSDT` Binance USDⓈ-M perpetual; direction **LONG only**; decision frame `1h`; indicator inputs all from completed, gap-checked Binance futures **hourly** OHLCV candles (UTC hourly boundaries).
- Let `O[t], H[t], L[t], C[t], V[t]` be hourly bar `t` and let `EMA_n[t]` be the standard recursive exponential moving average of closes with `alpha = 2/(n+1)`, seeded at bar `n-1` by the arithmetic mean of its first `n` closes. No lookahead or future-centered indicator.
- Evaluate signals once when bar `t` closes. Only trade after at least **721 fully completed contiguous hourly bars** from the evaluation dataset have been consumed (720-bar return + current), with the same warmup/trading-start convention for both engines.
- Absolute strength gate: `C[t]/C[t-720] - 1 >= 0.30` (a trailing 30-day hourly close-to-close return of at least 30%). This **replaces** the source's across-stock percentile/rank and its 3/6-month discretionary comparisons.
- Uptrend at signal bar: `C[t] > EMA9[t] > EMA21[t] > EMA50[t]` AND `EMA9[t] > EMA9[t-3]`. All inequalities strict.
- Prior-bar pullback: `L[t-1] <= EMA9[t-1]`, `C[t-1] >= EMA21[t-1]`, and `EMA9[t-1] > EMA21[t-1] > EMA50[t-1]`. A completed prior bar must have touched the fast EMA without closing under the mid EMA.
- Entry confirmation on `t`: `C[t] > H[t-1]`, `C[t] > EMA9[t]`, and the uptrend and strength gates are true. This only signals when **flat**, with no other outstanding entry/exit. Queue one market LONG entry for `O[t+1]`; never fill at an already-observed `C[t]`.
- Fixed initial stop at entry confirmation: `S = min(L[t-6], ..., L[t-1]) - one_tick`, where `one_tick` is historical symbol tick size from the exchange-instrument precision metadata effective at the entry timestamp. On filling at `P=O[t+1]`, require `P>S>0` and set `R=P-S`. Otherwise skip entry; no re-optimization of the stop after observing future bars.
- For each open position hold three persistent virtual tranches of original rounded quantity: **40% TP1 at `P+3R`**, **40% TP2 at `P+5R`**, and **remainder as runner**. All tranches retain the same fixed initial stop `S`. If a completed bar closes below its `EMA9`, the **runner only** closes at the next bar open. TP1/TP2 that remain unfilled do not receive the EMA9 runner exit. If no position remains, clear flags, stop and target state.
- Intrabar stop/target convention **proposed for verification, not declared as proven by Hummingbot**: process the stop first if hourly `L <= S`, close **all remaining** quantity at `S`, or at `O` if that bar opened below `S` (adverse gap). If stop not touched, fill TP1 then TP2 when `H >= respective target` at exactly each target (no positive gap improvement). If stop and one or both targets lie within the same candle's OHLC range, treat the stop as having filled first. A runner signal generated from the bar close cannot retroactively fill inside that bar and schedules its market exit at the following open. If a queued runner exit and a market gap occur, execute at next open, before any later intrabar orders. A bar with a pending signal, entry and exits is evaluated in chronological order; no same-close execution. These rules require explicit event-level engine verification at Gate 5.
- No shorts; no trailing stop; no discretionary support redraw; no momentum add-ons; no safety orders / DCA for this **base derivative**; no pyramiding; at most one total active position; no cooldown beyond flat-on-entry gating; re-entry on a fresh qualifying bar only. No end-of-test forced liquidation is silently assumed: mark residual exposure to market at the deterministic test end and report separately from realized P&L.

## Required data

- Contiguous full-history Binance USDⓈ-M BTCUSDT 1h OHLCV with reliable candle-close timestamps and explicit missing-bar handling; source gaps invalidate affected decision/stop paths and should invalidate affected evaluation segments rather than be forward-filled.
- Symbol contract metadata effective at execution time: quantity increment, tick size, minimum notional, margin/leverage and order precision; historical fee schedule, spread/slippage inputs and actual funding timestamps/rates for meaningful net-performance studies. A venue metadata or funding gap must be flagged, not zero-filled.
- No daily/low-timeframe lookahead: all strategy signals use only 1h data. The source's daily EMA, AVWAP, 1/5/15-minute cues, gaps and cross-sectional stock screening are deliberately **not** claimed to be reproduced.
- Warmup 721 contiguous complete hourly bars before trading; `t-720`, `t-6` and every EMA predecessor exist. All signals on completed candles; `t+1` open is unknown at `t` decision time.

## Execution assumptions

- Explicit research instrument: BTCUSDT Binance USDT-margined **isolated** perpetual, leverage **3x** for v1. A 5x or other-symbol run must record a separately pinned evaluation configuration (not silently claim identical outcomes). Cash equity starts at a fixed research `E0` (e.g. 1,000 USDT); no added funds; accounting equity includes realized P&L, costs and unrealized P&L.
- Risk budget per new trade `B = 0.005 * E_entry` (0.5% contemporaneous equity before new entry). Candidate base quantity `q_risk = B/(P-S)`; exposure-capped `q_cap = 0.06*E_entry*3/P` (a 6%-equity initial-margin allocation at 3x). Order quantity is floor-to-venue-quantity-increment of `min(q_risk, q_cap)`. Reject entries below instrument minimums; do not round up and do not use fictitious fills. Account for entry/exit fees, funding and slippage as costs; 0.5% is **price-stop-only planning risk**, not a guarantee of capped realized loss.
- Partial quantities: `q1=floor_to_step(0.40*q)`, `q2=floor_to_step(0.40*q)`, `q_runner=q-q1-q2`; skip setup if the planned partial orders are not individually venue-valid. Positions use actual filled quantity, not an unrealized theoretical quantity.
- The assumed market-at-next-open / OHLC stop-first path, partial stop orders, two TP limits, reduce-only flags, fills and cancellation sequencing MUST be tested against pinned **Hummingbot package 20260920, VERSION dev-2.17.0**, on an identified controller/executor/connector/backtesting route. Merely knowing Hummingbot has controllers is insufficient. **Exact route, partial-fill accounting, historical precision, and intrabar collision semantics have not been verified; Gate 5 is OPEN.**
- Evaluate realistic non-VIP USDⓈ-M maker/taker fees, spread/slippage, time-varying funding, quantity rounding, gap fills, margin and liquidation under the same frozen assumptions in both engines. Current campaign funding implementation is not fully verified, so never label a hypothetical/no-funding result as historically net realized P&L.
- **No DCA in this defined base derivative.** The house BO 6% + SO1/SO2 6% overlay alters path, size, price, liquidation and risk and would need its own declared derived configuration plus a separate six-gate review / parity check before campaign use.

## Evidence

### Source-reported

Four user-supplied X screenshots: (1) strong-stock selection and consolidation, (2) daily support plus lower-timeframe trigger, (3) precommitted stop and 0.5%-risk sizing example, (4) partial 3R/5R profit-taking and EMA9 runner management. No sample backtest, profit, Sharpe, annualized return or crypto performance is provided in the screenshots. X post's full text is unverified.

### Independently reproduced

Not independently reproduced. No code was deployed, no Hummingbot or Qlib runs were performed, no trade-event parity was measured.

### Negative evidence

- Source screenshots do **not** define a complete algorithm, precise support threshold, AVWAP anchor, EMA method, stop lookback, exit-tranche sizes, fee/funding/slippage assumptions, or execution collision ordering.
- The 30-day fixed +30% absolute screen can be inactive for extended periods on BTCUSDT. This is a falsifiable characteristic, not grounds to change threshold after looking at OOS.
- Model-convenient intrabar collision resolution and assumed precise fill prices may differ from real venue fills and the pinned Hummingbot controller; cannot be called HB_READY PASS without actual proof.
- No claim of profitability, 0.5% maximum actual loss, native source equivalence, Hummingbot backtest completeness, Qlib parity or deployability.

## Falsification plan

1. Reviewer first checks provenance and distinguish all invented derivative rules, then all six HB_READY gates. In particular **verify Gate 5 experimentally for the exact pinned Hummingbot execution path** (bar-close trigger -> next open, TP1/TP2 partials, stop-first candle collision, runner exit/size flags, costs/precision). If unsupported, reject / keep outside `main`, never fabricate PASS.
2. Compare trade event logs on controlled synthetic OHLCV sequences: (a) no momentum/no trade; (b) EMA retest + breakout; (c) invalid opening gap through stop; (d) bar touches stop and both profit targets; (e) TP1 only followed by runner EMA exit; (f) TP1+TP2 then stop of runner; (g) rounded partial lots invalid; (h) missing candle and data warmup. Verify deterministic fills, quantities, position exposure and P&L.
3. If Gate 5 succeeds, verify representative event-level parity between Hummingbot and Qlib **before** mass Qlib screening; log data and implementation hashes.
4. Freeze parameters, use complete post-warmup historical evaluation, IS/OOS split and a pre-registered OOS boundary; report all trades including no-trade windows, fees, funding, liquidation, Sharpe, annualized net return and max drawdown. Do not optimize on final OOS.
5. Rejection outcomes include lack of engine support, lookahead, absent trade-event parity, return insufficient after full costs or failure of campaign downstream risk/performance gates. No automatic Survivor/Testnet/Mainnet promotion.

## Crypto portability

This file is a **single-market derivative** rather than the original U.S. equity cross-sectional method. Extension to other house symbols or 4h/1d periods is a further research configuration requiring a fully specified timeframe-relative lookback, signal migration and exact-engine validation. Do not implicitly carry a 720-hour 30-day cutoff across timeframes.

## Limitations

- Research only; six-gate admission NOT YET ASSESSED. Source post is attributed by supplied URL and screenshots, **not verified source code**. Reviewer must not reclassify researcher-designed parameters as source-native.
- Major semantic adaptations: stock universe -> perpetual future, multi-horizon percentile -> fixed threshold, minute entry -> hourly entry, discretionary support -> EMA touch, unspecified tranche sizes -> 40/40/20, 3R/5R limit-style intrabar fills, 3x risk-capped sizing.
- Engine compatibility, partial target/stop collision behavior, data precision, historical funding and true cost accounting are pending independent verification. This record must remain outside PASS-only `main` unless all six gates are demonstrated.
- This record contains a **fully described proposed research algorithm**, not executable Hummingbot controller code and not a certificate of HB_READY readiness.

## Implementation status

Not implemented. Proposed as exactly one strategy research PR; GitHub's existing reviewer decides whether to accept, request changes or leave this record off `main`. No external watchdog/service/manager, engine configuration, README count, n8n, Qlib, Survivor repository, or local environment was changed.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; not for Testnet or Mainnet. `NOT_ASSESSED` explicitly blocks merging to `main`; only an independent full six-gate assessment with verified pinned-engine support may change that.

## Related Wiki records

No Wiki Brain record created or assumed. Future post-run analysis belongs to the existing Wiki Brain research process.

## Sources

- Source X post: https://x.com/othersidebj/status/2109475443929972794 — @OtherSideBJ / 另一面; four supplied screenshots; original live content not independently fetched.
- Admission rules: https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md (six-gate PASS-only review and source-native/derived distinction).
- Research contract: https://github.com/HCH725/alpha-strategy-research/blob/main/README.md .
