---
schema: strategy-research-record-v1
title: "ATR Volatility Family Representative (Tick-level data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - atr_tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动态阻力与支撑的双K线形态ATR风险控制量化交易策略-Dynamic-Resistance-and-Support-Dual-Candlestick-Pattern-ATR-Risk-Management-Quantitative-Trading-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ATR Volatility Family Representative (Tick-level data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 动态阻力与支撑的双K线形态ATR风险控制量化交易策略-Dynamic-Resistance-and-Support-Dual-Candlestick-Pattern-ATR-Risk-Management-Quantitative-Trading-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动态阻力与支撑的双K线形态ATR风险控制量化交易策略-Dynamic-Resistance-and-Support-Dual-Candlestick-Pattern-ATR-Risk-Management-Quantitative-Trading-Strategy.md

## Economic mechanism
### Source-reported
> The "Dynamic Resistance and Support Dual Candlestick Pattern ATR Risk Management Quantitative Trading Strategy" is a trading system that combines multiple classic indicators from technical analysis. This strategy is primarily based on the dynamic identification of support and resistance levels, integrated with the powerful reversal signal of Engulfing Patterns, and employs the ATR (Average True Range) indicator for risk management. The strategy fuses three dimensions in its trading decisions: price structure, candlestick pattern recognition, and volatility analysis, using multiple confirmations to increase the reliability of trading signals. The strategy design employs a dynamic method for calculating support and resistance levels, which can flexibly adapt to different market environments through the lookback period parameter, while using a fixed risk-reward ratio of 1:2 to set stop-loss and take-profit targets, embodying a strict risk management philosophy.

### Research interpretation
ATR Volatility logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Tick-level data.

## Signal
> The core principles of this strategy are based on three key technical elements: support and resistance level determination, candlestick pattern recognition, and ATR risk management.

First, the strategy determines dynamic resistance and support levels by calculating the highest and lowest prices within a specified lookback period (default 50 periods). These price levels have historically had a significant impact on market movements and may do so again. The resistance level is determined by the highest price within the lookback period, representing areas of concentrated selling pressure; the support level is determined by the lowest price within the lookback period, representing areas of concentrated buying pressure.

Second, the strategy identifies two powerful reversal patterns—Bullish Engulfing and Bearish Engulfing. A Bullish Engulfing pattern appears during a downtrend, consisting of a small bearish candle followed by a larger bullish candle, where the body of the second bullish candle completely covers ("engulfs") the body of the previous bearish candle, indicating that buying pressure has overcome selling pressure and potentially signaling an upward trend reversal. A Bearish Engulfing pattern is the opposite, appearing during an uptrend, consisting of a small bullish candle followed by a larger bearish candle, similarly indicating a shift in power and potentially signaling a downward trend reversal.

Third, entry signals must simultaneously meet both pattern confirmation and price position conditions:
- Buy signal: Must have both a Bullish Engulfing pattern and the current closing price above the support level
- Sell signal: Must have both a Bearish Engulfing pattern and the current closing price below the resistance level

Finally, the strategy uses the ATR indicator for risk management. ATR measures market volatility and is used to set stop-loss positions that adapt to current market conditions. The stop-loss distance is set at 1.5 times the ATR value, and t...

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
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
- Construct explicit PyBroker implementation honoring `Tick-level data` and the detailed signal rules.
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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动态阻力与支撑的双K线形态ATR风险控制量化交易策略-Dynamic-Resistance-and-Support-Dual-Candlestick-Pattern-ATR-Risk-Management-Quantitative-Trading-Strategy.md
