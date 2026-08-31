---
schema: strategy-research-record-v1
title: "Moving Average Crossover/Trend Family Representative (Renko charts
- Futures Basis)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - ma_futures-basis-renko-charts
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于EMA和Supertrend结合的多时间框架趋势跟踪策略-Multi-timeframe-Trend-Following-Strategy-Based-on-EMA-and-Supertrend-Combination.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Moving Average Crossover/Trend Family Representative (Renko charts
- Futures Basis)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 基于EMA和Supertrend结合的多时间框架趋势跟踪策略-Multi-timeframe-Trend-Following-Strategy-Based-on-EMA-and-Supertrend-Combination.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于EMA和Supertrend结合的多时间框架趋势跟踪策略-Multi-timeframe-Trend-Following-Strategy-Based-on-EMA-and-Supertrend-Combination.md

## Economic mechanism
### Source-reported
> The Multi-timeframe Trend Following Strategy Based on EMA and Supertrend Combination is a comprehensive quantitative trading system that primarily captures market trends and generates trading signals through a combination of multiple moving averages and the Supertrend indicator. The strategy employs three exponential moving averages (EMAs) of different periods as a preliminary judgment of trend direction, while incorporating the ATR-based (Average True Range) Supertrend indicator as the main basis for entry and exit points. The strategy is particularly suitable for Renko charts, which filter market noise and more clearly display price movement trends.

### Research interpretation
Moving Average Crossover/Trend logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Renko charts
- Futures Basis.

## Signal
> The core principle of this strategy is based on a collaborative confirmation mechanism of multi-layered technical indicators, including the following key components:

1. **Multiple EMA Crossover System**: The strategy uses three exponential moving averages with different periods (9, 15, and 15) to determine the overall market trend direction. When the fast EMA (9-period) is above the slow EMA (15-period), it is identified as an uptrend; conversely, it is a downtrend.

2. **Supertrend Indicator**: Upper and lower bands are calculated based on ATR (Average True Range). When the price breaks through the upper band, it switches to a bullish trend; when it breaks through the lower band, it switches to a bearish trend. The strategy uses a 10-period ATR with a multiplier parameter of 3.0.

3. **Trend Confirmation Mechanism**: The strategy only generates trading signals when the EMA trend direction aligns with the Supertrend direction, which reduces the probability of false signals.

4. **Signal Generation Logic**:
   - Buy signal: When Supertrend switches from downtrend to uptrend, and simultaneously the fast EMA is above the slow EMA
   - Sell signal: When Supertrend switches from uptrend to downtrend, and simultaneously the fast EMA is below the slow EMA

5. **Position Management**: The strategy uses a percentage of equity (100%) as the default position size, providing a dynamic position adjustment mechanism based on account size.

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- Renko charts
- Futures Basis

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
- Construct explicit PyBroker implementation honoring `Renko charts
- Futures Basis` and the detailed signal rules.
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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于EMA和Supertrend结合的多时间框架趋势跟踪策略-Multi-timeframe-Trend-Following-Strategy-Based-on-EMA-and-Supertrend-Combination.md
