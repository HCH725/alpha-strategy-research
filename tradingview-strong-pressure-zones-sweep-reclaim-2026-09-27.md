---
schema: strategy-research-record-v1
title: "TradingView Strong Pressure Zones Sweep-Reclaim"
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-27
sources:
  - "https://www.tradingview.com/script/27MBFCQ0-Strong-Pressure-Zones-ProjectSyndicate/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Strong Pressure Zones Sweep-Reclaim

## Provenance

- Public TradingView open-source indicator: **Strong Pressure Zones | ProjectSyndicate**, author **ProjectSyndicate**.
- Stable source: https://www.tradingview.com/script/27MBFCQ0-Strong-Pressure-Zones-ProjectSyndicate/
- TradingView canonical script identity: `27MBFCQ0`.
- Source reviewed as of 2026-09-27.
- The source describes an indicator and discretionary trade framing, not an independently validated strategy. No Pine source code is reproduced here.

## Economic mechanism

### Source-reported

The author frames confirmed swing pivots as potential pools of resting liquidity. A pivot pool is weighted by formation-bar volume times range, and later interaction distinguishes ordinary holds from deeper sweeps. The headline reversal event is a sweep through a zone followed by a close back through the zone within a reclaim window. The source interprets this as stop/liquidity consumption followed by failed acceptance. A decisive close beyond the zone, or failure to reclaim within the window, is instead treated as a genuine break and the zone may flip into a breaker.

For BTC pairs, the source states that pressure magnitude aggregates Binance, Coinbase, and Bitstamp volume; other symbols use native volume. The source also describes a live 0-10 strength score combining relative pressure magnitude with defense quality, including held retests, volume, rejection-wick depth, defended sweeps, and idle decay.

### Research interpretation

The falsifiable alpha hypothesis is **liquidity-sweep mean reversion conditioned on ex-ante level significance and subsequent reclaim**: failed excursions beyond recently confirmed, participation-heavy swing levels may have more short-horizon reversal information than unweighted sweep/reclaim events.

Component roles:

- Level formation: confirmed swing-high and swing-low pivots.
- Ex-ante level weighting: formation-bar volume × range, ranked relative to other live pools.
- Primary event: zone sweep followed by close-based reclaim.
- Confirmation/context: live strength score and optional RSI extreme.
- Alternative state: accepted break/no timely reclaim flips the level into a continuation-oriented breaker.

The incremental claim is not that sweep/reclaim alone reverses, but that pressure/defense conditioning improves the information content of the reclaim. This must be tested by ablation against simpler pivot and sweep/reclaim baselines.

## Signal

Source-supported normalized logic:

1. Confirm swing pivots after the required right-side bars; exact pivot lengths/defaults are not stated in the reviewed public description.
2. Create a long-pressure pool from a confirmed swing low and a short-pressure pool from a confirmed swing high.
3. At formation, pressure magnitude is based on bar volume × bar range and ranked against other live pools.
4. Track multiple live zones; overlapping zones may be suppressed and zones older than a configurable maximum age are removed.
5. A hold is a wick interaction that closes back inside without satisfying the configured minimum sweep depth.
6. A sweep requires price to pierce a zone border by the configured minimum sweep depth.
7. A reclaim occurs when price subsequently closes back through the zone within the configured reclaim window. Confirmation can be configured to the near border, midline, or far border.
8. Bullish framing: sweep below a long-pressure pool, then reclaim; bearish framing is symmetric above a short-pressure pool.
9. The source's discretionary trade framing says to enter in the reclaim direction, place the stop beyond the sweep extreme, target the opposite side of the pool first and then the next pool/unswept level.
10. The source suggests focusing on strong pools, explicitly giving `7+` as an example, and describes an optional RSI extreme filter.

Underspecified in the reviewed public description: pivot lengths, exact zone-width construction, minimum sweep-depth default/formula, reclaim-window default, strength-score algebra and weights, decay formula, overlap rule, maximum-age default, RSI length/thresholds, exact multi-exchange aggregation synchronization, order timestamp, fill price, re-entry, pyramiding, and fully mechanical target selection.

No missing operational value above is silently filled. Any future choice needed to mechanize these gaps is **research-proposed**.

## Required data

- Instruments: source claims broad cross-market applicability; BTC receives a special multi-exchange volume treatment.
- Crypto portability target: BTC pairs are directly described by the source.
- OHLCV sufficient for native-symbol level construction and sweep/reclaim state.
- BTC pressure aggregation additionally requires point-in-time volume from Binance, Coinbase, and Bitstamp.
- Confirmed swing logic requires strict causal handling: a pivot becomes available only after its confirmation bars have elapsed.
- Timestamp/candle-boundary alignment across BTC venues is required for any multi-exchange implementation.
- Venue symbol mapping, quote currency normalization, missing-bar handling, volume-unit normalization, and spot/perpetual identity are not specified by the source.

## Execution assumptions

The source provides discretionary execution guidance but not a complete fill model.

- Signal confirmation: reclaim is evaluated on the reclaim bar close and is fixed after that bar closes; the live forming bar can flicker.
- Entry: described as "on the reclaim" in the reclaim direction; whether this means same-close or next-bar execution is underspecified.
- Stop: beyond the sweep extreme; exact buffer is underspecified.
- First target: opposite side of the pool; later target: next pool/unswept level. Exact selection and order semantics are underspecified.
- Market vs limit order: not stated.
- Fees, spread, slippage, impact/capacity, latency, partial fills, leverage/margin, funding and borrow/shorting: not stated.
- No execution assumption omitted by the source is treated as zero.

## Evidence

### Source-reported

The source explains the construction and labels the 0-10 strength framework as descriptive rather than a backtested edge. It does not report Sharpe, CAGR, profit factor, drawdown, win rate, trade count, statistical significance, or an independently validated out-of-sample result for the sweep/reclaim thesis.

The source explicitly notes that swing pivots confirm only after several bars and states that reclaim is close-based and fixed once the reclaim bar closes.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source explicitly says the 0-10 strength ranking is a descriptive attention framework, not a backtested edge.
- Pivot confirmation is delayed by construction; any backtest that assigns the pivot to its historical pivot bar before confirmation would introduce look-ahead.
- The source provides no independent performance evidence for the proposed reversal edge.
- BTC aggregation spans venues whose volume units, symbols and candle boundaries may differ; the reviewed description does not specify normalization.
- Strength is relative to other live pools and includes persistent defense counts plus decay, making the state path-dependent and requiring careful point-in-time reconstruction.
- Exact score weights and several detection defaults are not stated in the reviewed description.
- None identified beyond the above in the reviewed source; absence is not evidence of no additional negative result.

## Falsification plan

All acceptance/failure thresholds below are **research-defined falsification thresholds**; implementation choices required because the source is incomplete are **research-proposed**.

1. **Causal reconstruction gate.** Rebuild pivots strictly from their confirmation timestamp. Any apparent edge that disappears when signals are shifted from pivot occurrence to pivot availability falsifies the usable version.
2. **Primary baseline.** Compare pressure-weighted sweep/reclaim against a plain confirmed-pivot sweep/reclaim rule using identical execution and holding logic. The pressure layer must add stable OOS information; otherwise reject its incremental-alpha claim.
3. **Magnitude ablation.** Compare volume × range weighting with volume-only, range-only, and unweighted pivots.
4. **Defense-score ablation.** Compare magnitude-only pools against the full strength framework and against a simple retest-count control.
5. **BTC aggregation ablation.** Compare single-venue volume with Binance+Coinbase+Bitstamp point-in-time aggregation. Reject the aggregation claim if improvement is unstable or explained by timestamp/unit mismatch.
6. **Reclaim-depth test.** Freeze near-border, midline, and far-border variants before OOS evaluation; do not select the best variant on the test set.
7. **Cost sensitivity.** Apply realistic venue-specific fees, spread and slippage. Reject deployable alpha if net OOS expectancy is non-positive at realistic costs.
8. **Regime stability.** Test trend, range, high/low volatility, bull/bear, and major liquidation-event regimes separately.
9. **Timing audit.** Compare next-bar executable fills with any same-close approximation. Material performance dependent on optimistic same-close fills is a falsification.
10. **Forward OOS.** Freeze all source-supported and research-proposed parameters before a forward holdout. Reject if the pressure-conditioned rule fails to outperform the plain sweep/reclaim baseline on risk-adjusted net returns with adequate trade count.

## Crypto portability

**direct** for the BTC-specific hypothesis because the source explicitly describes BTC pairs and a Binance+Coinbase+Bitstamp aggregation mode.

Risks remain material: spot versus perpetual identity is unspecified; venue fragmentation and volume-unit normalization matter; funding and mark/index price matter if ported to perpetuals; crypto trades 24/7 so candle boundaries must be frozen consistently.

## Limitations

- **underspecified:** multiple detector defaults, score algebra, execution details and target selection.
- **not independently reproduced:** no internal empirical validation was performed in this Scout cycle.
- **data gap:** no complete fee/slippage/funding/capacity model and no published backtest statistics in the reviewed source.
- **unproven:** whether pressure/defense conditioning adds alpha beyond a simpler causal sweep/reclaim baseline.
- The source is an open-source TradingView indicator, but this record normalizes only the public description and does not redistribute Pine code.

## Implementation status

Research record only. No implementation in the research stack, Qlib full backtest, candidate-pool promotion, Paper, Testnet, or Live validation has been performed.

## Adoption boundary

This artifact is **research-only**, **not-implemented**, and **not-approved**. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor/leaderboard entry, is profitable, or is approved for Paper, Testnet, or Live trading.

## Related Wiki records

No stable Hermes Wiki Brain link was verified in this GitHub-only run; none is fabricated.

Repository-local related record reviewed for deduplication:

- `tradingview-lp-sweep-reclaim-breakout-grading-2026-09-17.md` — related sweep/reclaim family, but materially distinct: its primary construction grades a prior-window extreme reclaim / Donchian breakout framework, whereas this record's distinctive hypothesis forms confirmed-pivot pressure pools weighted by volume × range, maintains path-dependent defense strength, and on BTC adds multi-exchange volume aggregation.

## Sources

- https://www.tradingview.com/script/27MBFCQ0-Strong-Pressure-Zones-ProjectSyndicate/ — ProjectSyndicate, **Strong Pressure Zones | ProjectSyndicate**, public open-source TradingView indicator, reviewed 2026-09-27.
