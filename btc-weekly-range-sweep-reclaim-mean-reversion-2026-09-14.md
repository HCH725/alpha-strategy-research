---
schema: strategy-research-record-v1
title: "BTC Perpetual Previous-Week Sweep-Reclaim Mean Reversion to Weekly Equilibrium"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - perpetual-futures
  - mean-reversion
  - liquidity-sweep
  - multi-timeframe
status: research-only
confidence: medium
source_as_of: 2026-09-14
sources:
  - "https://www.tradingview.com/script/vDtK5OfB/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BTC Perpetual Previous-Week Sweep-Reclaim Mean Reversion to Weekly Equilibrium

## Provenance

- **Primary source:** TheMrD, "Master Strategy: BTC W1 Mean Reversion [Institutional SOP]," TradingView public open-source Pine Script page, published 2025-12-25, accessed 2026-09-14.
- **Stable public URL:** https://www.tradingview.com/script/vDtK5OfB/
- **Source type:** TradingView open-source indicator. This Scout directly inspected both the public description and Pine source on 2026-09-14.
- **Source scope:** The author frames the indicator for BTC/USDT perpetual futures and instructs use on a 4-hour chart. The Pine code uses `syminfo.tickerid`, so venue/symbol are inherited from the chart. The reviewed source page displayed MEXC BTCUSDT perpetual, but the description is not limited to MEXC.
- **Evidence boundary:** This is an indicator / signal framework, not a TradingView `strategy()` backtest. The source does not publish a return series, Sharpe ratio, CAGR, drawdown, win rate, or independent out-of-sample validation.
- **Deduplication:** No occurrence of source identity `vDtK5OfB` was found in the staging repository or Hermes Wiki Brain. Related records use materially different reversal signals, so this prior-week sweep/reclaim construction clears the incremental-write threshold as a distinct signal family.

## Economic mechanism

### Source-reported

The source describes a weekly-range "deviation" play. The prior completed week's high and low define the current week's range. A move beyond either boundary is treated as a possible liquidity / stop sweep. If price subsequently closes back inside the range on the 4-hour decision timeframe, the source interprets the excursion as rejection rather than acceptance and targets rotation toward the previous week's midpoint (`EQ`).

The source adds three quality controls intended to avoid fading genuine directional expansion: a daily ADX filter blocks signals above 25; a weekly-range-width filter blocks unusually narrow or wide prior-week ranges; and an acceptance test blocks mean reversion if two preceding 4-hour closes remain outside the swept weekly boundary.

### Research interpretation

The falsifiable mechanism is **failed auction / failed breakout mean reversion around a salient higher-timeframe reference level**. Stops and breakout orders can cluster just beyond previous-week extremes. A sufficiently large excursion beyond such a level may attract liquidity-taking flow, but a quick 4-hour close back inside the prior-week range indicates failure to establish value outside the range. If the excursion was mostly transient order-flow pressure rather than new information, price may rotate toward the range midpoint as liquidity normalizes.

The ADX and range-width filters are regime gates rather than alpha by themselves. The two-close acceptance test explicitly supplies the competing hypothesis: sustained closes outside the boundary indicate a true breakout, not a sweep.

This mechanism is plausible but **not empirically validated by the source**. Terms such as "liquidity sweep" and "institutional" are source framing, not independently established causal facts.

## Signal

**Specification status:** The indicator signal is largely reconstructable from the open-source Pine code, but the end-to-end trading strategy remains **underspecified** because order expiry, fill handling, position sizing, holding-period cap, and same-bar exit precedence are not defined.

### Formation timestamp and availability

- Decision timeframe default: **4 hours** (`240`).
- On a new 4-hour bar, the code evaluates the **previous completed 4-hour bar** (`[1]`).
- Previous-week high (`PWH`) and low (`PWL`) come from the **last completed weekly bar** via `request.security(..., "W", [high[1], low[1]], lookahead=barmerge.lookahead_off)`.
- The daily ADX gate uses the prior daily value (`adx_val[1]`) with `lookahead_off`.
- The source does not specify a UTC timezone or venue-independent weekly-session boundary. TradingView symbol/session aggregation is therefore a **timestamp-boundary data gap** that must be frozen before reproduction.

### Lookbacks and fixed source parameters

- Previous-week range: prior completed weekly high and low.
- Weekly equilibrium: `(PWH + PWL) / 2`.
- Maximum sweep-to-reclaim delay: **3 completed 4-hour bars**.
- Minimum sweep distance: **0.15%** beyond PWH/PWL.
- Dynamic sweep threshold: enabled by default; actual threshold is the larger of 0.15% and a volatility-scaled term based on **0.25 × 1-hour ATR(14)** divided by the relevant weekly boundary.
- Weekly range-width gate: enabled by default; `(PWH-PWL)/PWL` must be **2%-25%**, inclusive.
- Trend gate: prior daily **ADX(14,14) <= 25**; signals are blocked above 25.
- Stop buffer: **0.25 × 1-hour ATR(14)** beyond the local three-bar extreme.
- The source does not state a separate warm-up count. Reproduction requires enough history for the previous weekly bar, 1-hour ATR(14), and daily DMI/ADX(14,14).

### Short setup — source-reported from open-source code

1. Short sweep threshold = max(0.15%, `0.25 × ATR_1h(14) / PWH × 100%`) when dynamic thresholding is enabled.
2. Register a sweep when the completed 4-hour high exceeds `PWH × (1 + threshold)`.
3. Track bars since the latest short-side sweep; reset state when weekly levels roll.
4. Treat the outside move as **accepted** if the two preceding completed 4-hour closes are both above PWH.
5. Generate a short reclaim signal when the just-completed 4-hour close is below PWH, the sweep occurred no more than 3 bars ago, acceptance is false, prior daily ADX is not above 25, and prior-week range width passes 2%-25%.
6. If long and short signals occur simultaneously, cancel both.
7. Suggested entry: **sell limit at PWH**.
8. Suggested target: **weekly EQ**.
9. Suggested stop: highest high across the latest three completed 4-hour bars plus `0.25 × ATR_1h(14)`.

### Long setup — source-reported from open-source code

1. Long sweep threshold = max(0.15%, `0.25 × ATR_1h(14) / PWL × 100%`) when dynamic thresholding is enabled.
2. Register a sweep when the completed 4-hour low falls below `PWL × (1 - threshold)`.
3. Track bars since the latest long-side sweep; reset state when weekly levels roll.
4. Treat the outside move as **accepted** if the two preceding completed 4-hour closes are both below PWL.
5. Generate a long reclaim signal when the just-completed 4-hour close is above PWL, the sweep occurred no more than 3 bars ago, acceptance is false, prior daily ADX is not above 25, and prior-week range width passes 2%-25%.
6. If long and short signals occur simultaneously, cancel both.
7. Suggested entry: **buy limit at PWL**.
8. Suggested target: **weekly EQ**.
9. Suggested stop: lowest low across the latest three completed 4-hour bars minus `0.25 × ATR_1h(14)`.

### Underspecified trading fields

The source does **not** define limit-order lifetime, weekly-roll cancellation, partial fills, position sizing, maximum holding period after fill, no-exit handling, same-bar stop/target precedence, overlapping-position policy, leverage, or margin rules. These omissions prevent treating the source as a fully executable strategy without additional `research-proposed` rules.

## Required data

- **Instrument:** BTC/USDT perpetual futures as framed by the source; exact exchange contract is not hard-coded.
- **Venue:** chart symbol / TradingView data venue. The page reviewed on 2026-09-14 displayed MEXC BTCUSDT perpetual, but cross-venue behavior is unproven and venue selection is underspecified.
- **Timeframes:** weekly OHLC; 4-hour OHLC/time; 1-hour data for ATR(14); daily data for DMI/ADX(14,14).
- **Fields:** high, low, close, timestamps. No volume, funding, open interest, order-book, liquidation, or trade-sign data are used by the source signal.
- **Point-in-time:** prior completed weekly range only; completed 4-hour bars for decision logic; `lookahead_off` on multi-timeframe requests.
- **Timestamp/session:** TradingView exchange/session convention; exact timezone / weekly cut is **underspecified**.
- **Missing data:** source gives no stale/missing-bar handling or imputation rule.
- **Costs:** fees, spread, slippage, market impact, and perpetual funding are omitted from the indicator and must be modeled separately in any tradability test.

## Execution assumptions

### Source-reported

- Signal is evaluated on completed 4-hour information.
- After a reclaim, the source suggests a **limit order at PWH for shorts or PWL for longs**, rather than immediate entry at the reclaim close.
- Target is weekly EQ.
- Stop is a three-4H-bar swing extreme plus/minus 0.25 × 1-hour ATR(14).
- Alerts are emitted once per bar close.

### Underspecified / omitted by source

No limit-order timeout or queue/fill model; no maker/taker fee assumption; no spread/slippage/impact or latency model; no funding treatment; no leverage/margin rules; no capacity limit; and no partial-fill/cancel-replace/failure handling.

### Research-proposed falsification harness only

For later historical testing — **not part of the source strategy and not implementation authorization** — a minimal deterministic harness can be frozen as follows:

- After a valid 4-hour reclaim, rest the source-specified limit at PWH/PWL for at most the next **3 completed 4-hour bars**, then cancel unfilled; also cancel on weekly rollover. This is `research-proposed`.
- If filled, use the source-specified EQ target and SL. If both are crossed within one OHLC bar and intrabar ordering is unavailable, count the stop first. This conservative precedence is `research-proposed`.
- Force-close any surviving position at weekly rollover. This bounded holding-period rule is `research-proposed`.
- Apply venue-specific maker/taker fees, historical spread/slippage where available, and realized funding during holding. These are `research-proposed` test requirements, not source assumptions.

## Evidence

### Source-reported

- The TradingView author presents the setup as BTC/USDT perpetual previous-week range mean reversion: sweep beyond PWH/PWL, 4-hour reclaim, entry at the weekly boundary, target at weekly equilibrium, with ADX / range / acceptance filters.
- The source code uses closed-bar references and `lookahead_off` for multi-timeframe requests, and the page describes the implementation as non-repainting.
- No performance statistics, sample period, trade count, transaction-cost result, or out-of-sample result are published on the reviewed page. No profitability figure is therefore preserved here.

### Independently reproduced

not independently reproduced

### Negative evidence

- The source provides **no empirical performance evidence**; it is an indicator, not a backtested TradingView strategy.
- The liquidity-sweep explanation is narrative rather than identified microstructure evidence; the same pattern can arise from ordinary volatility around a salient technical level.
- Limit entry at PWH/PWL after reclaim creates material selection/fill risk because many valid reclaims may never retrace to the proposed entry.
- Fees, spread, slippage, market impact, and perpetual funding are absent, so gross chart patterns cannot be interpreted as net alpha.
- No formal failed replication was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

All numerical decision rules below are **research-defined falsification thresholds**, not source-reported criteria.

1. **Strict post-publication OOS.** Freeze the source signal and `research-proposed` fill harness; test BTC perpetual data beginning **2025-12-26** without retuning. **Failure rule:** reject tradable-alpha interpretation if net expectancy per filled trade is <= 0 after fees, spread/slippage, and funding, or if a block-bootstrap 95% confidence interval for mean net trade return includes zero. **Action:** retain only as a descriptive technical pattern.
2. **Venue robustness.** Reproduce on at least three liquid BTC perpetual venues (e.g. Binance, Bybit, OKX; MEXC may be additional). **Failure rule:** weaken the general claim if positive net expectancy appears on only one venue or changes sign on two or more major venues. **Action:** classify as venue-specific.
3. **Timestamp / weekly-boundary audit.** Recompute weekly levels under explicitly frozen UTC and venue-native weekly boundaries. **Failure rule:** reject timing robustness if >20% of signals change identity/direction or net expectancy changes sign solely from the weekly cut. **Action:** mark session convention as a critical data dependency.
4. **Parameter-neighborhood stability.** Perturb minimum sweep 0.10%-0.30%, reclaim window 2-4 4H bars, ADX cutoff 20-30, and SL ATR buffer 0.15-0.40. **Failure rule:** reject parameter robustness if fewer than 50% of local cells retain positive net expectancy or only the published default is profitable. **Action:** classify defaults as sample-sensitive.
5. **Filter ablation.** Compare full signal with no ADX, no weekly-width gate, no two-close acceptance gate, and raw weekly-boundary reclaim. **Failure rule:** weaken the filter thesis if the full rule does not improve net expectancy or downside-adjusted return versus raw reclaim. **Action:** do not attribute alpha to unsupported components.
6. **Placebo / shuffled-level test.** Replace PWH/PWL with prior-range-preserving pseudo-levels or shuffle signal weeks while retaining volatility regimes. **Failure rule:** reject weekly-level specificity if real-signal net expectancy does not exceed the 95th percentile of placebo outcomes. **Action:** attribute any remaining effect to generic reversal rather than previous-week liquidity levels.
7. **Competing explanation.** Compare with a 4-hour overextension/reversal rule matched on excursion size and volatility but not anchored to PWH/PWL. **Failure rule:** weaken the liquidity-sweep narrative if matched generic reversals perform equally or better after costs. **Action:** classify any edge as generic volatility-conditioned mean reversion.
8. **Fill / cost / funding stress.** Separately report signaled, fillable, and filled trades under realistic cost assumptions. **Failure rule:** reject tradability if fewer than 30% of signals obtain the boundary limit fill within the `research-proposed` 3-bar expiry, or conservative net expectancy is non-positive under an ordinary non-VIP venue fee schedule. **Action:** keep research-only.
9. **Regime breakdown.** Segment by volatility, daily ADX, prior-week width, funding, and event weeks. **Failure rule:** reject broad robustness if all positive expectancy concentrates in one regime representing <25% of filled observations. **Action:** require a point-in-time regime gate before further research.
10. **Leakage / repaint audit.** Reimplement using only observations available at each 4-hour decision close and independently verify multi-timeframe merge semantics. **Failure rule:** any unfinished weekly/daily/4H observation that materially changes historical signals invalidates the reconstruction. **Action:** discard contaminated results and correct timing first.

## Crypto portability

**direct** — the source is explicitly designed around BTC/USDT perpetual futures and 24/7 crypto price bars.

Risks: weekly boundaries can differ by symbol/venue; funding can alter multi-bar returns; liquidity/spread differ across Binance, Bybit, OKX, MEXC and others; mark/index/liquidation data are absent, so "liquidity sweep" must not be conflated with observed forced liquidations; venue outages, contract specification, stablecoin quote risk, and fragmented liquidity can alter both signals and fills.

## Limitations

- **not independently reproduced**.
- Source is an indicator, not a strategy backtest; no source performance evidence exists.
- End-to-end lifecycle is **underspecified**: order expiry, sizing, maximum hold, partial fills, and exit precedence are omitted.
- Timestamp / weekly-session convention is **underspecified**.
- Venue selection is **underspecified**; description is BTC/USDT perpetual generally while the reviewed chart displayed MEXC.
- No cost, spread, slippage, impact, funding, leverage, or liquidation model is provided.
- The "liquidity sweep" mechanism is inferred from price action, not order-book, trade-sign, liquidation, or open-interest data.
- The 1-hour ATR and multi-timeframe alignment have not been independently reproduced outside TradingView.
- The phrase "institutional-grade" is marketing/source framing, not evidence of institutional use, quality, or profitability.

## Implementation status

`not-implemented` — no implementation, historical backtest, Paper, Testnet, or Live validation was performed by this Scout. Only public-source inspection and research normalization were completed.

This capture does not modify the quantitative runtime, create a strategy family, or authorize implementation.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`.

Presence in the staging repository does **not** mean profitable, independently validated, approved for implementation, approved for Paper/Testnet, or approved for Live. Later implementation/adoption requires separate Research Intake Review and explicit authorization.

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]] — canonical research-record contract.
- [[quant/crypto-short-horizon-15min-mean-reversion-taker-flow-2026-09-01]] — related mean-reversion family, but based on 15-minute return sign / taker flow rather than weekly sweeps.
- [[quant/crypto-perp-crowded-flush-reversal-microstructure-2026-09-12]] — related perpetual reversal family, but based on funding / open-interest liquidation-cascade evidence rather than weekly price-level rejection.

No matching Wiki record with the same TradingView source identity or materially same weekly sweep/reclaim construction was identified before writing.

## Sources

1. TheMrD. "Master Strategy: BTC W1 Mean Reversion [Institutional SOP]." TradingView, published 2025-12-25. Public open-source Pine Script page. Accessed 2026-09-14. https://www.tradingview.com/script/vDtK5OfB/
