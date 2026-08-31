---
schema: strategy-research-record-v1
title: "Bollinger Band Breakout/Reversion Family Representative (OHLCV)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bollinger_ohlcv
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多层级布林带趋势跟踪与反转交易策略-Multi-level-Bollinger-Bands-Trend-Following-and-Reversal-Trading-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bollinger Band Breakout/Reversion Family Representative (OHLCV)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 多层级布林带趋势跟踪与反转交易策略-Multi-level-Bollinger-Bands-Trend-Following-and-Reversal-Trading-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多层级布林带趋势跟踪与反转交易策略-Multi-level-Bollinger-Bands-Trend-Following-and-Reversal-Trading-Strategy.md

## Economic mechanism
### Source-reported
> The Multi-level Bollinger Bands Trend Following and Reversal Trading Strategy is a comprehensive trading system based on the Bollinger Bands indicator. This strategy cleverly combines trend following and reversal trading characteristics by capturing market opportunities through the interaction between price and the upper and lower Bollinger Bands. The system has designed a three-layer exit mechanism, including zone judgment, moving average crossover, and trailing stop profit, which maximizes profit capture while effectively controlling risk. This strategy is applicable to various market environments and time periods, particularly suitable for highly volatile financial markets.

### Research interpretation
Bollinger Band Breakout/Reversion logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: OHLCV.

## Signal
> The core principle of this strategy is to use Bollinger Bands as a dynamic reference range for price fluctuations, combined with carefully designed multi-level entry and exit rules.

The entry logic is divided into two parts:
1. Long entry conditions: Enter long when the price crosses above the lower Bollinger Band (Crossover Lower Band), or when the price touches below the lower band and then rebounds (i.e., the low price is below the lower band but the closing price is above the lower band).
2. Short entry conditions: Enter short when the price crosses below the upper Bollinger Band (Crossunder Upper Band), or when the price touches above the upper band and then falls back (i.e., the high price is above the upper band but the closing price is below the upper band).

The exit logic includes three protective measures:
1. First layer (zone judgment): Starting from the X-th bar after entry, exit when the closing price enters a specific area of the Bollinger Bands. Specifically, for long positions, close the position if the price falls to the first 1/3 area between the lower band and the middle band; for short positions, close the position if the price rises to the first 1/3 area between the upper band and the middle band.
2. Second layer (moving average crossover): Starting from the Y-th bar after entry, close the position if the closing price crosses the 20-period moving average (MA20).
3. Third layer (trailing stop profit): Activate the trailing stop profit mechanism when the price breaks through the opposite edge of the Bollinger Bands, and automatically exit once the profit retraces by Z%, securing most of the gains.

Bollinger Bands parameters can be flexibly adjusted, including the moving average period (default 20) and standard deviation multiplier (default 2.0). Exit settings can also be adjusted according to market characteristics, including X (default 3), Y (default 10), and trailing stop profit retreat percentage Z (default 30%).

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多层级布林带趋势跟踪与反转交易策略-Multi-level-Bollinger-Bands-Trend-Following-and-Reversal-Trading-Strategy.md
