---
schema: strategy-research-record-v1
title: "Moving Average Crossover/Trend Family Representative (Heikin-Ashi candles)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - ma_heikin-ashi-candles
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/双均线交叉趋势跟踪策略Dual-Moving-Average-Crossover-Trend-Tracking-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Moving Average Crossover/Trend Family Representative (Heikin-Ashi candles)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 双均线交叉趋势跟踪策略Dual-Moving-Average-Crossover-Trend-Tracking-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/双均线交叉趋势跟踪策略Dual-Moving-Average-Crossover-Trend-Tracking-Strategy.md

## Economic mechanism
### Source-reported
> This strategy utilizes the dual moving average crossover principle combined with a trend tracking indicator to determine and follow trends. The main idea is to go long when the short period moving average crosses above the long period moving average and go short when the short period moving average crosses below the long period moving average. The overall trend direction is also determined by the 100-day moving average to avoid false breakouts.

### Research interpretation
Moving Average Crossover/Trend logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Heikin-Ashi candles.

## Signal
> The strategy consists mainly of a dual moving average crossover system and a trend tracking system. 

The dual moving average crossover system contains a fast EMA1 and slow EMA2. The default periods are 10 days for EMA1 and 20 days for EMA2. A buy signal is generated when EMA1 crosses above EMA2. A sell signal is generated when EMA1 crosses below EMA2.

The 100-day EMA (EMA100) is added to determine the overall trend direction. Buy signals are only generated when the price is in an upward trend (price is above the 100-day EMA). Sell signals are only generated when the price is in a downward trend (price is below the 100-day EMA). This filters out most false breakout situations.

Buy and sell arrows are also plotted on the candles to visually display the trading signals.

The trend tracking system uses intraday and cycle day lines to confirm the trend direction again. Intraday uses 5-min and 60-min Heikin-Ashi moving averages while the cycle uses 8-day and 12-day moving averages of the daily line. 

Trading signals are only generated when the intraday and cycle judgments agree. This further filters out most noise in the non-major trend directions.

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- Heikin-Ashi candles

## Execution assumptions
- Source-derived execution logic is underspecified in pure technical descriptions unless detailed in the signal logic block above. Assumes generic next-bar execution unless tick-level data is strictly required.
- Fees and slippage not strictly accounted for.

## Evidence
### Source-reported
Source claims vary by variant. Not independently reproduced.

### Independently reproduced
Not independently reproduced.

### Negative evidence
None identified in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan
- Construct explicit PyBroker implementation honoring `Heikin-Ashi candles` and the detailed signal rules.
- Test out-of-sample against structurally relevant assets.
- For hybrid candidates: isolate components via ablation to verify standalone predictive power of the core indicator.

## Crypto portability
direct

## Limitations
- underspecified parameter robustness
- not independently reproduced
- None explicitly detected in structural scan; manual semantic review required for hidden repainting.

## Implementation status
not-implemented

## Adoption boundary
This is research material only. Not approved for trading.

## Related Wiki records
None

## Sources
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/双均线交叉趋势跟踪策略Dual-Moving-Average-Crossover-Trend-Tracking-Strategy.md
