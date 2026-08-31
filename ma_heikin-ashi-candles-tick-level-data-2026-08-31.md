---
schema: strategy-research-record-v1
title: "Moving Average Crossover/Trend Family Representative (Heikin-Ashi candles
- Tick-level data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - ma_heikin-ashi-candles-tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/均线趋势追踪策略Trend-Following-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Moving Average Crossover/Trend Family Representative (Heikin-Ashi candles
- Tick-level data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 均线趋势追踪策略Trend-Following-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/均线趋势追踪策略Trend-Following-Strategy.md

## Economic mechanism
### Source-reported
> The trend following strategy is a trend trading strategy based on the crossover of moving averages. It uses the crossover of an exponential moving average (EMA) and a Hull moving average (HMA) to determine the trend direction and generate trading signals accordingly. The strategy aims to follow the longer-term price trend rather than short-term oscillations.

### Research interpretation
Moving Average Crossover/Trend logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Heikin-Ashi candles
- Tick-level data.

## Signal
> The strategy employs two moving averages with different parameters: a faster EMA and a slower HMA. The EMA reacts faster to price changes and is used to judge short-term trends, while the HMA responds slower and tracks long-term trend direction.

When the faster EMA crosses above the slower HMA, it is viewed as a start of an upward trend, and the strategy will place a long order at market price on the next bar open. When the EMA crosses below the HMA, it is seen as the beginning of a downward trend, and the strategy will go short at market price on the next bar open.

To optimize entry timing, the strategy incorporates a Heikin-Ashi option. When enabled, the buy and sell signals will be based on Heikin-Ashi bars instead of normal candlesticks. Heikin-Ashi bars can filter out short-term price oscillations on the original candlesticks and reduce false signals. 

The strategy also employs a stop loss setting. When the position loss reaches the preset stop loss percentage, the position will be closed out at market price, capping the maximum loss per trade.

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- Heikin-Ashi candles
- Tick-level data

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
- Construct explicit PyBroker implementation honoring `Heikin-Ashi candles
- Tick-level data` and the detailed signal rules.
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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/均线趋势追踪策略Trend-Following-Strategy.md
