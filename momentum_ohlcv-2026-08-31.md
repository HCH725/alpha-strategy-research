---
schema: strategy-research-record-v1
title: "Momentum Family Representative (OHLCV)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - momentum_ohlcv
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多指标综合分析量化交易策略趋势动量与波动性协同预测模型-Multi-Indicator-Comprehensive-Analysis-Quantitative-Trading-Strategy-Trend-Momentum-and-Volatility-Collaborative-Prediction-Model.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Momentum Family Representative (OHLCV)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 多指标综合分析量化交易策略趋势动量与波动性协同预测模型-Multi-Indicator-Comprehensive-Analysis-Quantitative-Trading-Strategy-Trend-Momentum-and-Volatility-Collaborative-Prediction-Model.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多指标综合分析量化交易策略趋势动量与波动性协同预测模型-Multi-Indicator-Comprehensive-Analysis-Quantitative-Trading-Strategy-Trend-Momentum-and-Volatility-Collaborative-Prediction-Model.md

## Economic mechanism
### Source-reported
> The Multi-Indicator Comprehensive Analysis Quantitative Trading Strategy is a quantitative trading method based on the integrated analysis of multiple technical indicators. This strategy incorporates 30 different technical indicators, including trend indicators, momentum indicators, volatility indicators, volume indicators, and other specialized indicators, forming a complete trading signal system through the collaborative analysis of these indicators. The strategy primarily utilizes mutual verification and filtering mechanisms between multiple indicators to identify market trends while combining momentum and volatility analysis to find high-probability trading opportunities. The strategy employs strict entry conditions and ATR-based dynamic stop-loss and take-profit settings, aiming to balance returns and risks.

### Research interpretation
Momentum logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: OHLCV.

## Signal
> The core principle of this strategy lies in creating a mutually verifying trading decision system through multi-dimensional market analysis. The strategy first defines five major categories of indicator systems:

1. **Trend Indicators**: Including SMA50, SMA200, EMA20, EMA50, and ADX. These indicators are used to confirm the primary market direction, with rising or falling ADX used to identify strengthening or weakening trends.

2. **Momentum Indicators**: Including RSI, MACD, Stochastic, CCI, and Momentum. These indicators primarily measure the speed and strength of price movements, identifying potential overbought or oversold areas.

3. **Volatility Indicators**: Including Bollinger Bands, Average True Range (ATR), and Keltner Channel. These indicators assess market volatility and determine potential price breakouts.

4. **Volume Indicators**: Including OBV, Money Flow Index (MFI), VWAP, and Chaikin indicator. These indicators confirm the authenticity of price trends by analyzing volume changes.

5. **Other Specialized Indicators**: Including Parabolic SAR, Supertrend, Williams %R, Fibonacci Retracement, and some modified indicators based on moving averages.

The strategy's trading logic is based on the comprehensive analysis of these indicators, with specific trading signal conditions as follows:

- **Long Conditions**: Requires ADX trend rising, RSI not exceeding 70, MACD line above signal line, Stochastic K greater than 20, CCI greater than -100, price breaking through the upper Bollinger Band, OBV greater than its 20-day moving average, sudden volume increase, golden cross formation, and price above the 200-day moving average.

- **Short Conditions**: Requires ADX trend falling, RSI greater than 30, MACD line below signal line, Stochastic D less than 80, CCI less than 100, price falling below the lower Bollinger Band, OBV less than its 20-day moving average, sudden volume increase, death cross formation, and price below the 200-day moving average.

Once a trad...

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多指标综合分析量化交易策略趋势动量与波动性协同预测模型-Multi-Indicator-Comprehensive-Analysis-Quantitative-Trading-Strategy-Trend-Momentum-and-Volatility-Collaborative-Prediction-Model.md
