---
schema: strategy-research-record-v1
title: Modern VWAP KER/ATR Regime-Gated Mean-Reversion and Trend-Continuation Signals
created: 2026-10-01
updated: 2026-10-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-01
sources:
  - https://www.tradingview.com/script/eNmPfTmZ-Modern-VWAP-GBB/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Modern VWAP KER/ATR Regime-Gated Mean-Reversion and Trend-Continuation Signals

## Provenance

Primary source: GoodBadBitcoin, "Modern VWAP [GBB]," public open-source TradingView indicator, published August 4, 2026. Stable TradingView source: https://www.tradingview.com/script/eNmPfTmZ-Modern-VWAP-GBB/ (canonical script id `eNmPfTmZ`), reviewed 2026-10-01.

The source is public and traceable. This record normalizes the published description rather than reproducing the Pine source.

## Economic mechanism

### Source-reported

The author argues that a conventional session VWAP is awkward for Bitcoin because the market does not have a natural daily close; midnight UTC is a convention rather than an economic event. The indicator therefore supports periodic or confirmed-swing anchors, then conditions two signal families on a market regime classified from Kaufman Efficiency Ratio (KER) and ATR.

The source assigns mean reversion to ranging regimes and trend continuation to trending regimes. It uses VWAP plus volume-weighted sigma bands as the reference geometry, with optional KER-adaptive band widths.

### Research interpretation

The falsifiable hypothesis is that **conditioning VWAP signals on a KER/ATR regime classification adds incremental information relative to the same VWAP signals without regime gating**.

Component roles:

- Baseline: anchored VWAP of HLC3 with volume-weighted deviation bands.
- Anchor state: Session, Week, Month, or confirmed Swing pivot.
- Regime: KER + ATR quadrant, exact thresholds underspecified in the reviewed description.
- Mean-reversion signal: excursion outside the two-sigma band followed by re-entry, allowed only in the ranging regime.
- Trend-continuation signal: pullback to VWAP that holds within three bars, allowed only in the trending regime.
- Direction filter for trend continuation: side occupancy, requiring 8 of the previous 10 closes on one side of VWAP.
- Optional adaptation: KER scales the sigma multiplier; this is off by default.

The economic interpretation is that price displacement from an accepted volume-weighted reference may revert when directional efficiency is low, while pullbacks to the same reference may resume when directional efficiency is high. This interpretation is a research hypothesis, not independently verified evidence.

## Signal

Source-reported normalized logic:

- Signal evaluation occurs on confirmed bars.
- Primary VWAP input is HLC3 accumulated from the selected anchor.
- Bands are one, two, and three sigma, where sigma is the volume-weighted deviation around VWAP rather than standard deviation of closes.
- Periodic anchors: Session, Week, Month.
- Swing anchor: confirmed pivot high or low; default pivot length 10, configurable 5 to 50. On confirmation, accumulators are rebuilt from the pivot bar.
- Composite mode can display up to three anchored VWAP instances, but signals and regime state use Instance A only.
- Default instances: A = Session, B = Swing, C disabled with Week selected.
- Mean reversion: in the ranging regime, price closes outside the two-sigma band and subsequently closes back inside. The source states that a candle crossing the entire channel does not fire.
- Trend continuation: in the trending regime, price pulls back to VWAP and holds within three bars.
- Trend direction uses side occupancy: 8 of the last 10 closes above or below VWAP, not VWAP slope.
- Optional KER-adaptive bands are off by default; default KER weight is 0.5 on a 0-to-1 setting range.

Underspecified in the reviewed source description:

- KER lookback and exact formula implementation;
- ATR lookback, normalization, and exact KER/ATR quadrant thresholds;
- exact directional mapping and state transition details for mean-reversion re-entry;
- exact definition of a VWAP pullback that "holds within three bars";
- whether multiple signals may occur before a regime or anchor reset;
- exits, holding period, re-entry restrictions, position sizing, and complete order lifecycle;
- exact session boundary/timezone behavior beyond the author's observation that midnight UTC is a convention.

No missing operational value is silently supplied here. Any future choice needed to make the rule executable is `research-proposed` unless recovered from the public source.

## Required data

Source-reported requirements:

- OHLCV bars, including HLC3 and volume;
- timestamps sufficient to construct Session, Week, and Month anchors;
- historical price and volume needed for confirmed swing pivots, KER, ATR, side occupancy, and VWAP deviation bands.

The source is explicitly motivated by Bitcoin/24-7 markets but describes a general indicator rather than fixing one venue, spot/perpetual market type, or chart timeframe in the reviewed description.

Point-in-time constraint: a swing anchor is only knowable after its pivot is confirmed. Any research implementation must preserve that confirmation lag and must not retrospectively treat the pivot bar as known at the pivot timestamp. Rebuilding the accumulator from the pivot bar after confirmation is source-reported display/calculation behavior; trading evaluation must remain causal.

Venue, missing-volume behavior, exchange aggregation, and cross-venue volume treatment are data gaps.

## Execution assumptions

The source publishes an indicator, not a complete order-execution strategy.

Source-reported:
- signals are labelled on confirmed bars;
- four alert conditions exist, one for each signal family/direction.

Underspecified:
- order type;
- signal-to-order delay;
- same-bar versus next-bar execution;
- fill model;
- fees, spread, slippage, market impact, and capacity;
- leverage, margin, borrow/short mechanics, and funding;
- partial fills and failure handling;
- exit and holding-period rules.

For a later causal backtest, executing no earlier than the next tradable observation after a confirmed signal would be `research-proposed`, not source-reported.

## Evidence

### Source-reported

The reviewed TradingView description explains construction, defaults, signal families, and causal design choices, but it does not report a strategy return, Sharpe ratio, CAGR, drawdown, win rate, profit factor, or statistical test for these signals.

The author states that the baseline matches TradingView's built-in VWAP when the same anchor is used. This is a construction/parity claim, not evidence of alpha.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-reported profitability evidence is supplied in the reviewed description.

The source does not establish that the KER/ATR regime gate adds predictive value over ungated VWAP signals, that KER-adaptive bands improve outcomes, or that auto-anchoring improves out-of-sample performance.

Swing anchors create a material causal-timing hazard because the pivot bar is recognized only after confirmation; a naive historical implementation could leak future information by acting as though the anchor were known at the pivot itself.

No transaction-cost or execution study is reported in the reviewed description.

## Falsification plan

1. Reconstruct the source logic causally, preserving swing-pivot confirmation delay. Failure to do so invalidates the test.
2. Primary ablation: compare each signal family with and without the KER/ATR regime gate while holding VWAP anchor, bands, timing, and execution constant.
3. Compare the regime-gated composite against simple fixed-rule baselines: two-sigma re-entry without regime gating and VWAP pullback/side-occupancy continuation without regime gating.
4. Separately ablate Session, Week, Month, and confirmed-Swing anchors; do not select the best anchor on the final test sample.
5. Separately test fixed bands versus KER-adaptive bands. The adaptive-band toggle must not be conflated with the regime gate.
6. Use chronological out-of-sample evaluation across bull, bear, high-volatility, low-volatility, trending, and ranging periods.
7. Apply realistic fees, spread, slippage, and next-tradable-observation execution.
8. Report signal count, turnover, expectancy, drawdown, Sharpe, and performance by regime. A result driven by a small number of episodes materially weakens the thesis.
9. Research-defined falsification threshold: reject the incremental regime-gating hypothesis if the gated version fails to improve net out-of-sample risk-adjusted performance over its otherwise identical ungated baseline, or if the advantage disappears under reasonable cost assumptions.
10. Run placebo/permutation checks on regime labels to test whether the claimed benefit exceeds what could arise from selecting a convenient partition of the sample.

## Crypto portability

**direct**, at the hypothesis level: the source explicitly frames the design around Bitcoin's 24/7 market and the absence of a natural daily opening bell.

Portability remains venue-sensitive. Crypto volume is fragmented across exchanges, perpetual volume differs from spot volume, funding and mark/index mechanics matter for derivatives, and session boundaries are conventional. Results from one venue or candle boundary must not be assumed to transfer unchanged to another.

## Limitations

- Not independently reproduced.
- Profitability evidence: data gap.
- KER/ATR regime thresholds: underspecified.
- Exit and holding-period logic: underspecified.
- Execution and cost model: underspecified.
- Venue and market type: underspecified.
- Swing-pivot anchoring requires strict point-in-time handling.
- Optional adaptive bands and regime gating are separate mechanisms and must be ablated separately.
- A public indicator description is not evidence that the normalized hypothesis is profitable.

## Implementation status

Research-only. No implementation in the research stack has been completed. No Qlib full backtest has been run for this record.

## Adoption boundary

This record is research material only. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, is profitable or validated alpha, or is approved for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

No stable related Hermes Wiki Brain record was resolved in this GitHub-only Scout run; no Wiki link is fabricated.

## Sources

- GoodBadBitcoin, "Modern VWAP [GBB]," TradingView, public open-source indicator, published August 4, 2026; reviewed 2026-10-01: https://www.tradingview.com/script/eNmPfTmZ-Modern-VWAP-GBB/
