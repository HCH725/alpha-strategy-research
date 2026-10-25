---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Skyrexio KST 10-15-20-30 Alligator-Jaw LSMA200 CHOP14 ATR14 close-bracket long-flat BTCUSDT 1h independent derivative
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-06-27
sources:
  - https://www.tradingview.com/script/Pv1GvUVs-KST-Strategy-Skyrexio/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Skyrexio KST + Alligator jaw + LSMA200 + CHOP14 with ATR close-bracket — independent long-flat derivative

## Provenance

**Primary TradingView source:** *KST Strategy [Skyrexio]*, author **Skyrexio**, published **2025-06-27**, public open-source strategy listing, stable script ID **Pv1GvUVs**: https://www.tradingview.com/script/Pv1GvUVs-KST-Strategy-Skyrexio/ . Author's publicly readable strategy description was inspected on **2026-10-26**; its detailed Methodology, Strategy settings and Justification of Methodology give the actual signal concept, all four ROC/SMA lengths, LSMA/CHOP defaults and ATR stop/target concept. **Full Pine source bytes, script revision/hash, order calls, and exact built-in indicator variants were not recovered.** No source-native/lossless Pine equivalence is claimed.

**Source-described facts (not researcher inventions):** LONG only; KST line crosses above its own signal; close above Williams Alligator jaw and filtering MA; optional CHOP filter enabled by default, CHOP < 50, length 14; default LSMA length 200; KST ROC lengths 10/15/20/30 with SMA smoothing 10/10/10/15 and 10-bar KST signal; 14-period ATR; source stop based on *entry-candle low minus 1.5 ATR*, source target based on *entry-candle close plus 3.5 ATR*; source exits when candle high/low touches levels. The author illustrates **BTC/USDT 1h**, 0.1% Binance commission, 5-tick slippage and 60%-of-capital position sizing. The page also describes Alligator jaw as a 13-period smoothed average displayed eight bars forward. Its explanatory CHOP equation mentions summed ATR, without recoverable Pine code resolving the precise summation variant. The source's claimed backtest results are **source-reported only** and are neither independently reproduced nor adopted here.

**Explicit independent derived executable rule — not the author's Pine:** Researcher fixes (a) Binance BTC-USDT **spot 1h** and single fixed **0.001 BTC** long, instead of the source's illustrative percentage-of-capital sizing; (b) causal *unshifted* 13-period SMMA of median price for the jaw decision, rather than using the eight-bar forward *display offset* as future information; (c) canonical sum-of-true-range CHOP14 and Wilder-RMA ATR14, and exact LSMA endpoint/ROC conventions; (d) full-bar-close evaluation with MARKET simulator close fills and **future completed-close** SL/TP checks instead of the source's intrabar high/low touches; (e) no original-source slippage claim, only declared idealized simulator fill and modeled fee; (f) fixed 220-valid-bar warmup, data guards, single-position state, no DCA, and all disabled exits below. These changes **materially alter entry/exit economics and potentially trade events**. The derivative is independently assessable only under the frozen rules below.

**Immutable identity:** `TV-Pv1GvUVs-Skyrexio | derived-v1-KST-10-15-20-30-SMA10-10-10-15-signal10-jaw13-unshifted-LSMA200-CHOP14lt50-ATR14-SL1p5-TP3p5-close | BinanceSpot-BTC-USDT-1h | 2026-10-26`. A different data/clock/fill/indicator/size/exit variant requires a different frozen identity.

## Economic mechanism

The author combines multi-horizon rate-of-change acceleration (KST) with a short-term jaw and a longer-term regression-trend filter, avoiding choppy regimes; volatility scales exits. This derivative tests whether a fresh momentum crossover within that filtered bullish regime can support a one-position long with a **fixed-at-entry** ATR-distance close-trigger bracket. It is a research hypothesis, not a claim of profitable or faithfully reproduced TradingView performance.

## Signal

Let `t` index **consecutive, valid, completed UTC hourly Binance spot candles**, with `O[t],H[t],L[t],C[t],V[t]`. The first hourly candle opens at UTC hour `T[t]`, and its entire O/H/L/C/V is available only at `T[t]+3600` seconds. All windows include the current **completed** bar and no future bars. Numeric comparisons use strict inequalities except crossover's prior equality allowance.

- `ROC_n[t] = 100 * (C[t]/C[t-n] - 1)` for `n in {10,15,20,30}`; reject undefined/nonpositive denominators.
- `KST[t] = SMA10(ROC10)[t] + 2*SMA10(ROC15)[t] + 3*SMA10(ROC20)[t] + 4*SMA15(ROC30)[t]`. `KSTsignal[t] = SMA10(KST)[t]`. Arithmetic SMA means equal weights over the stated trailing number of finite values.
- `median[t]=(H[t]+L[t])/2`. `jaw13` is Wilder-style SMMA13 of median: seed with the arithmetic average of the first 13 valid median values, then `jaw13[t] = (12*jaw13[t-1] + median[t])/13`. **Compare C[t] to jaw13[t] with no forward displacement**; the source's +8 is a display description, not a future-value dependency in this derivative.
- `LSMA200[t]`: ordinary least-squares fit of the last 200 **closes** against `x=0..199` (oldest to newest), with intercept `a` and slope `b`; `LSMA200[t]=a+199*b`. If the fit is not finite, signal invalid.
- `TR[t] = max(H[t]-L[t], abs(H[t]-C[t-1]), abs(L[t]-C[t-1]))`. `ATR14[t]` is Wilder RMA14 of TR (seed with mean of first 14 valid TR, then `(13*ATR14[t-1]+TR[t])/14`); positive finite ATR required for entry.
- `HH14[t]=max(H[t-13..t])`, `LL14[t]=min(L[t-13..t])`, `CHOP14[t]=100*log10(sum(TR[t-13..t])/(HH14[t]-LL14[t]))/log10(14)`. If denominator <=0, any TR undefined, or log argument <=0, CHOP is undefined and entry is false. This **sum-of-TR** implementation is researcher-defined and not falsely attributed to inaccessible Pine.
- `kst_up[t] = KST[t-1] <= KSTsignal[t-1] AND KST[t] > KSTsignal[t]`, all four values finite.
- **LONG entry (FLAT only):** after warmup, `kst_up[t]` AND `C[t] > jaw13[t]` AND `C[t] > LSMA200[t]` AND `CHOP14[t] < 50` AND `ATR14[t]>0`. Strict equality fails the price and CHOP gates. No additional signal filter, session gate, volume gate or discretionary override.
- On a confirmed full BUY fill from signal bar `e`, freeze **SL = L[e] - 1.5*ATR14[e]** and **TP = C[e] + 3.5*ATR14[e]**. Reject an entry if `SL <= 0`, `SL >= C[e]`, `TP <= C[e]`, or any level is undefined; do not fabricate a bracket.
- **LONG exit (only for bars t > e):** at the first subsequent completed bar for which `C[t] <= SL` **or** `C[t] >= TP`, submit a full MARKET SELL for the held base amount at that bar's close. If neither condition holds, hold. Bracket levels never trail or recalculate. On a valid close, SL and TP cannot both be hit simultaneously because `SL < TP`; if data are invalid, no order.
- **No KST cross-down exit, opposite signal exit, partial target, intrabar stop/limit, trailing stop, breakeven move, forced time exit or terminal forced SELL.** Source intrabar high/low triggers are **not** being represented as equivalent. Open terminal position remains marked at last valid close, not fictitiously liquidated.

## Position state, risk and disabled behaviors

Exactly `FLAT -> PENDING_BUY -> LONG -> PENDING_SELL -> FLAT` on **confirmed full simulator fills**. Submit a BUY of fixed `0.001 BTC` only from FLAT; submit a SELL of the filled held amount only from LONG. A submitted order is **not** treated as a confirmed fill. Pending states suppress all further actions; a failed/expired BUY reverts to FLAT with no assumed fill, a failed/expired SELL retains LONG and retries only at a later valid decision where exit condition persists. One action maximum per completed bar. Exit has priority while LONG; entry triggers while LONG or pending are ignored. No same-bar entry and exit, no same-bar re-entry after SELL; a fresh `kst_up` on a later eligible bar is required. Cooldown = zero **additional** bars; the exit bar itself is not eligible for a new entry.

No short, leverage, margin, futures, hedging, simultaneous positions, pyramiding, DCA/BO/SO overlays, scaling, compounding, equity-percentage sizing, automatic liquidation, maker/limit/stop orders, partial fills or unmentioned Hummingbot executor risk defaults. No trade if insufficient modeled base/quote balance, invalid OHLCV or missing/zero fill price; do not substitute synthetic prices. Fixed base size is a research quantity, not a claim of real Binance minimum-notional/precision compliance.

## Required data and point-in-time causality

Binance BTC-USDT spot **1h** O/H/L/C/V only; strictly hourly UTC open timestamps increasing by 3600 seconds, finite positive prices, `H >= max(O,C)`, `L <= min(O,C)`, finite nonnegative volume. Reject duplicate/missing/out-of-order candles; do not interpolate, forward-fill, or infer a missing close. **220 consecutive completed valid hourly bars** of warmup before first entry: KST's 30-bar ROC, 15-bar smoothing, 10-bar signal and prior-bar crossover, LSMA200 and all other indicators are then defined. The SMMA seed is reset with each newly validated contiguous segment. On a data gap or invalid bar, suppress decisions/fills and require 220 new consecutive valid bars before new entries. If already LONG, retain actual held exposure and frozen bracket, suppress invalid-bar exit fills, and resume close-exit decisions only on valid subsequent completed bars; no fabricated gap-close or future-bar inference. If there is no further valid close, retain marked/unresolved open exposure.

All features at `t` use only `<=t` completed observations. No higher-timeframe lookahead, plotted Alligator forward offset as future data, repainting pivots, hindsight extrema, model fitting beyond trailing 200-bar LSMA, or unconfirmed candles. Source's 1h is an author **example**, not a universal eligibility restriction.

## Execution assumptions — pinned Hummingbot engine (Gate 5)

Admission baseline: Hummingbot package label `20260920`, VERSION `dev-2.17.0`; source tree **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3**. Direct read through connected GitHub app this cycle confirmed `hummingbot/VERSION` = `dev-2.17.0`; package image digest / byte-for-byte package-to-source match **not reverified**, and this record does not claim one. This is the already independently reviewed **spot MARKET first-row-close / POSITION_HOLD** research primitive (see PR #417), not proof of implementation of this particular indicator/controller.

- **Feed:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` explicitly supports `1h` via `/api/v3/klines`; `binance_spot_candles.py` parses Binance row[0] timestamp and row[1..5] O/H/L/C/V. Controller feature construction must enforce valid completed bars and 220-bar warmup; Hummingbot does not supply this new KST/CHOP strategy automatically.
- **Controller/executor:** `BacktestingEngineBase.simulate_execution` iterates prepared rows, `update_state(row)`, then `controller.determine_executor_actions()`; `CreateExecutorAction` with `OrderExecutorConfig`, `ExecutionStrategy.MARKET` and BUY/SELL uses `OrderExecutorSimulator.simulate`. Direct source inspection confirms MARKET fills at first supplied row's **close** and `filled_amount_quote = amount_base * close`, `cum_fees_quote = trade_cost * filled_amount_quote`, `CloseType.POSITION_HOLD`. The full fill is a **simulator assumption**, not exchange execution proof.
- **Clock:** Binance kline timestamp is **bar OPEN**. Engine's `prepare_market_data` uses `merge_asof(...,direction="backward")` and raw `timestamp_bt`, which alone does NOT make the just-completed close known at that open. The declared derivative controller evaluates only when the bar has completed at `T[t]+3600`, and its research event/fill ledger must normalize the same-row close to **close-effective T[t]+3600**, never raw open `T[t]`. Same-completed-close fill is an idealized research convention, not a promise a post-close real order could obtain the observed close; **no intrabar high/low fill** is claimed.
- **Position ledger:** `BacktestPositionHold` nets equal-base BUY/SELL and separately accumulates gross realized PnL and `cum_fees_quote`; `positions_held` conversion is delayed after POSITION_HOLD termination. Use persistent pending/fill-confirmed controller state and `terminated_executors_window=None` so the one-hour terminated-executor view does not erase fill/cooldown evidence. Controller must not use a just-sent order as proof of position, or native `net_pnl_quote` as guaranteed fee-inclusive net equity.
- **Costs:** set `trade_cost=0.001` **per filled side** (0.1% source-reported illustrative Binance commission) and **zero additional modeled slippage** because this simulator's MARKET path has no separate slippage parameter. This explicitly **omits** the source's 5-tick slippage; zero *modeled* slippage is NOT zero realized spread/latency/slippage. For completed `q=0.001 BTC` round trip, modeled net quote PnL `q*(sell_close-buy_close) - 0.001*q*(buy_close+sell_close)`. An open LONG carries paid BUY fee. Spot funding is inapplicable (not assumed zero futures funding). Real fee tiers, exchange precision, minimum notional, partial fills and liquidity remain unverified; no live authorization.
- **Prior independent primitive audit:** `HCH725/alpha-strategy-research#417`, final review `HB_READY: PASS` on 2026-10-25, independently inspected this same immutable source, Binance spot candles, MARKET close fill, fee ledger, timestamp caveat and POSITION_HOLD netting. This reuses that reviewed **engine capability**; it does not transfer candidate-specific strategy approval, actual package hash, backtest, Qlib parity or profitability.

## Evidence — six admission gates

1. **Deterministic signals:** all four ROC windows/smoothing weights, signal crossing, causal jaw SMMA13, LSMA200 endpoint, CHOP14 TR formula, ATR14 RMA, strict gates, bracket freezes and invalid-data rules are pinned. Inaccessible Pine differences are explicitly **derived**, never invented as source facts.
2. **Direction:** one Binance BTC-USDT spot LONG/FLAT, short and margin explicitly disabled.
3. **Entry/exit/risk:** one filtered KST up-cross entry; frozen entry-bar low/close ATR bracket checked on **future closes**; every other exit/stop/target mode disabled.
4. **Position/re-entry:** 0.001 BTC single filled position, explicit pending and retry semantics, no DCA, no concurrent exposure, no same-bar re-entry, no additional cooldown.
5. **Pinned engine:** concrete immutable source/version, 1h Binance spot feed, action/executor first-row MARKET close, completed-bar effective timestamp, fee and POSITION_HOLD accounting, full-fill and precision limitations, independent prior primitive review.
6. **Causality:** 220 valid completed-bar warmup, trailing-only OLS and indicators, unshifted jaw (no lookahead), close-effective decisions, invalid-price guards, no fabricated missing bars or fills.

**Source-reported:** author/date/public URL, strategy ingredients/defaults and original intrabar SL/TP concepts, example fee/slippage and example performance (not reproduced). **Researcher-defined:** the frozen indicator variants, spot market, sizing, clock, close-only exits, disabled behaviors and modeled economics above. **Independently reproduced performance:** none. **Historical survivor/HB Certified/Qlib parity:** none claimed.

## Deduplication

At initial main commit `fc9aadb0d5eb847e4edf5cfab6df19b965e3ccd2`, tree is untruncated, **334 root-level strategy Markdown files**, and README static count **334** (no count-only drift). Main filenames and GitHub code search show no `Pv1GvUVs` or Skyrexio KST source. All **11** open research/* PRs were checked; none names or cites this TradingView source or the KST + Alligator-jaw + LSMA200 + CHOP14 + frozen ATR close-bracket rule. Existing `kst-signal-cross-trend-two-sided-btcusdt-1h-2026-10-09.md` is a **different FMZ source** with KST-only two-sided cross reversals, no jaw/LSMA/CHOP regime gating and no ATR stop/target. Existing Alligator and CHOP/DMI/PSAR families likewise do not implement this confluence/exit state. This is not a trivial KST parameter variant.

## Falsification plan

Subject to separate downstream approval, test the frozen filtered KST against an unfiltered KST ablation using predeclared IS/OOS, and separately measure event differences from high/low intrabar exits (which this derivative intentionally does **not** claim to reproduce). Before large-scale Qlib screening of a **new** data/execution primitive, require representative Qlib/Hummingbot event-level parity; no candidate-specific profitability, Qlib run, parity, or survivor status is asserted by Scout.

## Crypto portability

The declared strategy uses a single 24/7 spot hourly OHLCV feed and no equity session or funding input. Other symbols/timeframes, the optional seven-coin/three-timeframe research campaign, DCA BO/SO 6/6/6 or futures leverage are **not** prerequisites and are **not** covered by this frozen identity; adapting them requires an explicit new derivative/economic model.

## Limitations

Full original Pine implementation and source revision were unavailable; author-prose ATR/CHOP smoothing and Alligator plotted displacement are not claimed to be the author's actual executable Pine calculations. The close-only bracket can diverge substantially from original intrabar stops/targets. The same-row close fill is an idealized pinned simulator convention and ignores actual post-close latency, order-book spread, 5-tick source slippage, lot/tick/min-notional constraints and partial fills. No performance or deployment claims. The Hummingbot source commit is verified; the package build digest is not independently matched this cycle. A missing/gapped data segment may leave a held position unresolved rather than invent a fill.

## Implementation status

**not-implemented**: no dedicated KST/CHOP controller, Qlib executable recipe, candidate replay or simulator run created. The PASS frontmatter is a **Scout-proposed, six-gate research eligibility claim pending independent Hermes Auditor review**, not self-approval or live authorization. A selected strategy may require minimal specific executable materialization; this is not a second HB_READY admission gate.

## Adoption boundary

**research-only; adoption not-approved.** Independent Hermes Auditor GitHub Webhook Review alone may correct source-verifiable facts, PASS-merge the exact reviewed PR head, or close NOT_LOSSLESS. Scout must not approve/merge/close or change main, README, schedules, containers, Qlib, Hummingbot, Paper, Testnet or Live.

## Related Wiki records

None asserted.

## Sources

- https://www.tradingview.com/script/Pv1GvUVs-KST-Strategy-Skyrexio/ — Skyrexio, public open-source strategy description, 2025-06-27, checked 2026-10-26; no full Pine body copied.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned Hummingbot source, read through connected GitHub app.
- https://github.com/HCH725/alpha-strategy-research/pull/417 — independent audit of reused spot MARKET close-fill/POSITION_HOLD primitive.
