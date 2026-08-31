---
schema: strategy-research-record-v1
title: "Price Level Breakout Family Representative (Tick-level data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - breakout_tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于量价关系的多指标波动率突破交易系统-Multi-Indicator-Volatility-Breakout-Trading-System-Based-on-Volume-Price-Relationship.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Price Level Breakout Family Representative (Tick-level data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 基于量价关系的多指标波动率突破交易系统-Multi-Indicator-Volatility-Breakout-Trading-System-Based-on-Volume-Price-Relationship.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于量价关系的多指标波动率突破交易系统-Multi-Indicator-Volatility-Breakout-Trading-System-Based-on-Volume-Price-Relationship.md

## Economic mechanism
### Source-reported
> The Multi-Indicator Volatility Breakout Trading System Based on Volume-Price Relationship is a comprehensive quantitative trading strategy that combines volume spike detection, ATR volatility channels, and RSI momentum filtering. The core concept of this strategy is to capture instances of sudden volume surges in the market, viewing them as potential trading opportunities, while incorporating price dynamics and technical indicators for multi-level filtering to enhance the precision of trading decisions. The strategy utilizes ATR volatility channels as references for stop-loss and take-profit levels, and leverages the RSI indicator to avoid excessive buying or selling, creating a complete trading system framework.

### Research interpretation
Price Level Breakout logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Tick-level data.

## Signal
> The operation of this strategy is based on the following key modules:

1. **Volume Spike Detection**: The strategy first defines the "VolSpike" concept by comparing the current volume with the total volume of the previous N candles. When the current candle's volume exceeds the sum of the previous N candles, it is identified as a volume spike signal. This abnormal trading volume typically indicates a potential directional change in the market.

2. **ATR Volatility Channels**: The strategy calculates the Average True Range (ATR) and creates upper and lower bands as reference ranges for price volatility. These channels not only serve to visualize market volatility but are also directly used to set stop-loss positions. The ATR channel calculation employs user-adjustable periods and multipliers, allowing the strategy to adapt to different market environments.

3. **RSI Momentum Filtering**: Trading signals are filtered through the Relative Strength Index (RSI) to avoid trading during extreme overbought or oversold conditions. Users can set upper and lower threshold values for RSI, and the strategy will only consider opening positions when the RSI value is between these thresholds.

4. **Candlestick Pattern Analysis**: The strategy also incorporates candlestick pattern analysis by measuring the ratio of the candlestick body to its upper and lower shadows, filtering out signals from candles with excessively long shadows, which helps avoid entering markets that might quickly reverse.

5. **Trade Execution Logic**:
   - When a volume spike is detected and the RSI filtering conditions and candlestick pattern requirements are met, the strategy will determine the entry direction based on the position of the closing price relative to the opening price.
   - Long condition: Closing price greater than opening price (bullish candle) and the upper shadow does not exceed the maximum set ratio.
   - Short condition: Closing price less than opening price (bearish candle) and the lower ...

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于量价关系的多指标波动率突破交易系统-Multi-Indicator-Volatility-Breakout-Trading-System-Based-on-Volume-Price-Relationship.md
