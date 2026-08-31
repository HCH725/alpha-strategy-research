---
schema: strategy-research-record-v1
title: "Ichimoku Cloud Family Representative (OHLCV)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - ichimoku_ohlcv
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/一目均衡趋势跟踪策略Ichimoku-Balance-Line-trend-following-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Ichimoku Cloud Family Representative (OHLCV)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 一目均衡趋势跟踪策略Ichimoku-Balance-Line-trend-following-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/一目均衡趋势跟踪策略Ichimoku-Balance-Line-trend-following-Strategy.md

## Economic mechanism
### Source-reported
> The Ichimoku Balance Line strategy is a trend following strategy that combines the Conversion Line and Base Line from the Ichimoku Cloud indicator and the moving average EMA to determine the trend direction. It enters long positions when the Conversion Line crosses above the Base Line and the price is above the 200-day EMA; closes positions when the Conversion Line crosses below the Base Line. This strategy incorporates multiple indicators to determine the trend direction, which allows effectively following the trend and achieving excess returns.

### Research interpretation
Ichimoku Cloud logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: OHLCV.

## Signal
> The strategy primarily uses the following indicators:

1. Conversion Line: The midpoint of the Donchian Channel, representing the shortest-term trend of the price, similar to a 9-day moving average.

2. Base Line: The midpoint of the Donchian Channel, representing the medium-term trend of the price, similar to a 26-day moving average.

3. Lagging Span: The displaced moving average of the closing price, displacement period is 120 days, used to determine support and resistance.

4. Lead 1: The average of the Conversion Line and the Base Line, representing the long-term trend. 

5. Lead 2: The midpoint of the 120-day Donchian Channel, representing the longest-term trend.

6. EMA200: The 200-day exponential moving average judging the major trend direction.

When the Conversion Line crosses above the Base Line, it signals the short-term moving average is crossing above the long-term moving average, which is a bullish golden cross signal indicating the trend is strengthening for going long. If the price is also above the 200-day EMA, it indicates the major trend is upward, making the long signal more reliable.

When the Conversion Line crosses below the Base Line, it is a death cross signal indicating the trend is turning weak, and positions should be closed for stop loss.

By combining crossover signals of multiple moving averages, the strategy can effectively determine trend reversal points for trend following. Using the long-term moving average filter avoids incorrect signals caused by short-term market fluctuations.

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- OHLCV

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
- Construct explicit PyBroker implementation honoring `OHLCV` and the detailed signal rules.
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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/一目均衡趋势跟踪策略Ichimoku-Balance-Line-trend-following-Strategy.md
