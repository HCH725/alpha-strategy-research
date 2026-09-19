---
schema: strategy-research-record-v1
title: TradingView Volume / OI Footprint Delta-Level Reaction
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-19
sources:
  - https://www.tradingview.com/script/J9a6nWwM-Volume-Open-Interest-Footprint-By-Leviathan/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Volume / OI Footprint Delta-Level Reaction

## Provenance

- **Primary source:** TradingView public open-source indicator, *Volume / Open Interest "Footprint" - By Leviathan*.
- **Author / page identity:** `LeviathanCapital`, TradingView.
- **Stable public URL:** https://www.tradingview.com/script/J9a6nWwM-Volume-Open-Interest-Footprint-By-Leviathan/
- **Publication date shown by source:** 2023-04-05.
- **Source as-of:** 2026-09-19.
- The source exposes an open-source indicator description and states that it constructs a footprint-style profile from aggregated volume or open-interest data over the chart's visible range.

## Economic mechanism

### Source-reported

The source reports three footprint views: total activity, up/down activity, and delta. For volume, delta represents buy volume minus sell volume; for open interest, the analogous view contrasts OI increase and decrease. It can draw levels where delta is positive. The author describes these levels as possible points of interest, support/resistance, or targets because they identify price zones associated with increased buy pressure or position opening.

### Research interpretation

The falsifiable hypothesis is that price levels containing unusually positive historical volume delta or OI delta may encode locally concentrated aggressive demand or position formation and therefore alter the conditional distribution of subsequent price reactions when revisited.

This does **not** assume that a positive-delta level must act as support. Competing hypotheses are: (1) rejection/bounce, consistent with persistent local demand or defended positioning; (2) breakout/continuation, if the level instead marks exhausted or trapped positioning; and (3) no directional information beyond ordinary volume-at-price or price structure.

The source's support/resistance interpretation is a hypothesis, not verified evidence.

## Signal

The source indicator itself is primarily a visualization/context tool and does not specify a canonical trading strategy.

Source-supported construction:

- Choose `Volume` or `Open Interest` as the footprint source.
- Build a price-binned footprint over the chart's visible range.
- Choose among `Total`, `UP/DOWN`, and `Delta` representations.
- For volume, delta is buy volume minus sell volume.
- For OI, the footprint distinguishes OI increase versus decrease and can express their delta.
- Positive-delta levels can be drawn as price zones.
- `Resolution` controls the number of rows in the footprint.
- Volume can be aggregated from up to eight sources; the source warns that base- versus quote-currency reporting must be handled correctly through its RQC setting.

The following operationalization is **research-proposed**, not source-reported:

1. At a strictly point-in-time formation timestamp, freeze a historical lookback window and its price-bin boundaries; do not use the future chart-visible range.
2. Construct volume-delta and OI-delta profiles separately.
3. Define candidate positive-delta zones using only information available at formation time; threshold and bin-resolution grids must be predeclared rather than selected from future performance.
4. When price subsequently revisits a frozen zone, measure forward returns and excursion over fixed horizons.
5. Test bounce/rejection and breakout/continuation as competing outcomes rather than assigning direction ex ante.

Canonical entry, exit, holding period, re-entry rule, sizing rule, profile lookback, delta threshold, zone width and trading timeframe are **underspecified** by the source.

## Required data

- Crypto spot and/or perpetual instruments for portability research; the source is not restricted to one crypto instrument in the retrieved description.
- OHLCV with timestamp-consistent candle boundaries.
- Volume data from selected venues, including correct base/quote denomination metadata when aggregating venues.
- For the OI variant: point-in-time open-interest series from supported derivatives venues.
- Sufficient price resolution to assign activity into profile rows/bins.
- Venue and contract metadata to prevent invalid aggregation across incompatible units.
- Point-in-time profile formation windows and immutable bin definitions for leakage-safe testing.

Exact supported volume venues and OI feeds are not fully enumerated in the reviewed public description and should not be invented.

## Execution assumptions

The source does not define a complete execution model.

For research, signals must be formed only after all data needed for a frozen profile is available. Same-bar fills at a level touched intrabar would require explicit intrabar sequencing and should not be assumed from OHLC bars. A conservative baseline should use next-observable-price or next-bar execution after a qualifying reaction/break condition.

Fees, spread, slippage, market impact, funding, leverage, margin, order type, partial fills and latency are **underspecified** by the source and must be modeled explicitly before any performance claim.

## Evidence

### Source-reported

The source describes positive delta levels as potential support/resistance, targets, or other points of interest. No independently verified Sharpe, CAGR, win rate, drawdown, or other performance statistic is reported here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-reported negative empirical result was identified in the reviewed page; absence is not evidence of no negative result. The indicator's dependence on the chart's visible range is a material research risk because a naïve historical implementation could allow future observations to change profile bins and levels retroactively.

## Falsification plan

1. **Leakage-safe reconstruction:** replace the source visualization's chart-visible range with frozen rolling or anchored windows whose endpoints are known at signal formation. Any result that disappears under frozen point-in-time profiles materially weakens the thesis.
2. **Direction competition:** test rejection/bounce, breakout/continuation, and unsigned volatility response around frozen positive-delta levels. Reject a directional interpretation if only volatility changes reliably.
3. **Component ablation:** compare ordinary volume-at-price, volume delta, OI distribution, and OI delta. Require delta-based levels to add out-of-sample information beyond total activity at the same price bins.
4. **Price-structure baseline:** compare against mechanically defined prior highs/lows and generic support/resistance levels. If footprint levels do not improve conditional outcomes, reject incremental alpha.
5. **Random/placebo levels:** preserve the same number and spacing of levels but randomize their price placement within the historical range. A real signal should outperform this placebo out of sample.
6. **Aggregation ablation:** where multi-venue data are available, compare aggregated profiles with single-venue profiles after unit normalization. Reject the aggregation thesis if added venues do not improve stability or transferability.
7. **Resolution robustness:** vary predeclared profile row counts and formation windows. Large performance dependence on a narrow binning choice is evidence of overfitting.
8. **Regime and universe robustness:** test liquid crypto assets across volatility, trend and liquidity regimes and across spot/perpetual markets where data permit.
9. **Cost sensitivity:** apply realistic fees, spread and slippage to any event-driven implementation. Reject economically unusable variants even if gross directional statistics survive.
10. **OOS requirement:** parameter and threshold choices must be fixed before final holdout evaluation; failure to retain incremental value versus simple baselines is a reject result.

## Crypto portability

**direct** for the research hypothesis because the TradingView source explicitly supports aggregated volume/open-interest analysis and is presented in a crypto/order-flow context.

Crypto-specific risks include venue fragmentation, inconsistent base/quote volume reporting, contract denomination, missing OI feeds, spot/perpetual differences, 24/7 candle boundaries, exchange outages and symbol-history changes. Cross-venue aggregation must normalize units before profile construction.

## Limitations

- The source is an indicator/context tool, not a fully specified strategy.
- Canonical lookback, threshold, zone width, timeframe, entry, exit, holding period and sizing are **underspecified**.
- The source's visible-range construction is not directly suitable for leakage-safe historical testing without a research-proposed frozen-window transformation.
- Buy/sell volume classification and OI increase/decrease profiling may depend on TradingView data semantics that require independent reconstruction before validation.
- Multi-venue aggregation can create false signals if quote/base units or contract specifications are mixed.
- Not independently reproduced.

## Implementation status

No implementation in the research stack has been completed. No backtest, runtime integration, paper trading, testnet or live validation was performed in this Scout cycle.

## Adoption boundary

Research material only. Presence in this repository does not mean profitable, validated alpha, approved implementation, paper-trading approval, testnet approval, or live-trading approval.

Any frozen-window profile, revisit rule, threshold, directional mapping, execution rule or parameter introduced above is `research-proposed` until independently implemented and tested.

## Related Wiki records

No stable Hermes Wiki Brain record was resolved under this GitHub-only operating boundary; no Wiki link is fabricated.

## Sources

- TradingView — LeviathanCapital, *Volume / Open Interest "Footprint" - By Leviathan*, published 2023-04-05, public open-source script, accessed/as-of 2026-09-19: https://www.tradingview.com/script/J9a6nWwM-Volume-Open-Interest-Footprint-By-Leviathan/
