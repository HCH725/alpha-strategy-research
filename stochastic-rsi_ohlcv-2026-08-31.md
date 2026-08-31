---
schema: strategy-research-record-v1
title: "Stochastic RSI Reversal/Crossover Family Representative (OHLCV)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - stochastic-rsi_ohlcv
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多指标交叉动量趋势追踪策略Hull与EMA结合RSI和双重随机震荡器的量化交易系统-Multi-Indicator-Crossover-Momentum-Trend-Following-Strategy-Quantitative-Trading-System-Combining-Hull-with-EMA-RSI-and-Dual-Stochastic-Oscillators.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Stochastic RSI Reversal/Crossover Family Representative (OHLCV)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 多指标交叉动量趋势追踪策略Hull与EMA结合RSI和双重随机震荡器的量化交易系统-Multi-Indicator-Crossover-Momentum-Trend-Following-Strategy-Quantitative-Trading-System-Combining-Hull-with-EMA-RSI-and-Dual-Stochastic-Oscillators.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多指标交叉动量趋势追踪策略Hull与EMA结合RSI和双重随机震荡器的量化交易系统-Multi-Indicator-Crossover-Momentum-Trend-Following-Strategy-Quantitative-Trading-System-Combining-Hull-with-EMA-RSI-and-Dual-Stochastic-Oscillators.md

## Economic mechanism
### Source-reported
> The Multi-Indicator Crossover Momentum Trend-Following Strategy is a high-precision quantitative trading system that combines the Hull Moving Average (HMA) with a shifted Exponential Moving Average (EMA), integrated with the Relative Strength Index (RSI) and dual Stochastic Oscillators as momentum filters. This strategy aims to capture high-probability trend breakouts, achieve precise entries and exits, while providing strict risk management mechanisms. The core logic is based on moving average crossover signals, confirmed by multiple momentum indicators to reduce false breakouts and improve trading win rates.

### Research interpretation
Stochastic RSI Reversal/Crossover logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: OHLCV.

## Signal
> This strategy is built on several key technical components:

1. **Hull Moving Average (HMA) and Shifted EMA Crossover**: The strategy uses a 12-period Hull Moving Average and a 5-period EMA shifted forward by 2 bars as the primary signal generation mechanism. HMA is known to react faster than traditional moving averages, while the shifted EMA adds a predictive quality, allowing earlier detection of trend changes.

2. **Multi-layer Momentum Filtering**: The strategy incorporates RSI(14) and two Stochastic Oscillators with different parameter settings (12,3,3 and 5,3,3) as confirmation indicators. This multi-layer filtering mechanism ensures that trade signals are triggered only when the trend has sufficient momentum.

3. **Precise Entry Conditions**:
   - Long Entry: Price closes above both HMA and shifted EMA, RSI is above 50, both Stochastic Oscillators' %K values are above 50, and HMA crosses above the shifted EMA.
   - Short Entry: Price closes below both HMA and shifted EMA, RSI is below 50, both Stochastic Oscillators' %K values are below 50, and HMA crosses below the shifted EMA.

4. **Strict Risk Management**: Stop-loss is set at the lowest point (for longs) or highest point (for shorts) of the previous 2 candles, with take-profit set at 1.65 times the stop-loss distance, creating a favorable risk-reward ratio.

The logic behind the strategy is that high-probability trading signals form only when price, moving averages, and multiple momentum indicators all confirm the same direction, thus reducing the impact of market noise.

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多指标交叉动量趋势追踪策略Hull与EMA结合RSI和双重随机震荡器的量化交易系统-Multi-Indicator-Crossover-Momentum-Trend-Following-Strategy-Quantitative-Trading-System-Combining-Hull-with-EMA-RSI-and-Dual-Stochastic-Oscillators.md
