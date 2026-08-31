---
schema: strategy-research-record-v1
title: "Price Reversal Family Representative (Tick-level data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reversal_tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于随机指标与烛台模式的自动化市场反转交易策略-Automated-Market-Reversal-Trading-Strategy-Based-on-Stochastic-Indicator-and-Candlestick-Patterns.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Price Reversal Family Representative (Tick-level data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 基于随机指标与烛台模式的自动化市场反转交易策略-Automated-Market-Reversal-Trading-Strategy-Based-on-Stochastic-Indicator-and-Candlestick-Patterns.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于随机指标与烛台模式的自动化市场反转交易策略-Automated-Market-Reversal-Trading-Strategy-Based-on-Stochastic-Indicator-and-Candlestick-Patterns.md

## Economic mechanism
### Source-reported
> The Automated Market Reversal Trading Strategy Based on Stochastic Indicator and Candlestick Patterns is a quantitative trading system that combines classic candlestick pattern recognition with stochastic indicator trend confirmation. The core design concept of this strategy is to identify key market reversal points by capturing potential trend turning opportunities in overbought or oversold areas. Implemented in Pine Script on the TradingView platform, this strategy provides a complete automated trading process including signal generation, risk management, and chart labeling functions. The strategy can identify multiple classic candlestick patterns such as hammer, shooting star, engulfing patterns, and more, while using the stochastic oscillator for trend confirmation, providing higher reliability and precision for trading decisions. The system incorporates a dynamic stop-loss and take-profit mechanism based on ATR (Average True Range), effectively controlling individual trade risk and improving capital management efficiency.

### Research interpretation
Price Reversal logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Tick-level data.

## Signal
> This strategy is based on two core technical principles: candlestick pattern recognition and trend confirmation filtering.

First, for candlestick pattern recognition, the strategy analyzes the structure of each candlestick through precise mathematical calculations, including the proportional relationships between the body, upper shadow, and lower shadow. The system defines a series of parameters to quantify the characteristics of different patterns, such as requiring the hammer pattern to have a lower shadow length exceeding twice the body length, with the body occupying less than 50% of the total length, and minimal upper shadow. The patterns identified include:
- Bullish signals: Hammer, Inverted Hammer, Bullish Engulfing, and Tweezer Bottom
- Bearish signals: Hanging Man, Shooting Star, Bearish Engulfing, and Tweezer Top

Second, the strategy introduces the Stochastic Oscillator as a trend confirmation tool, ensuring that reversal signals are only captured in overbought or oversold zones. By setting a threshold (default 80), when the stochastic indicator is above the threshold, it's considered an overbought zone (bearish area), and when below (100-threshold), it's considered an oversold zone (bullish area). The strategy also employs a smoothing algorithm to process the stochastic indicator, reducing noise interference and enhancing signal reliability.

The trade execution logic is as follows:
1. Long signals: When bullish candlestick patterns are identified in oversold areas (bearZone), the system enters a long position
2. Short signals: When bearish candlestick patterns are identified in overbought areas (bullZone), the system enters a short position

For risk management, the strategy employs an ATR-based dynamic stop-loss and take-profit mechanism:
- Long trades: Take Profit = Entry Price + (ATR × 1.5), Stop Loss = Entry Price - (ATR × 1.0)
- Short trades: Take Profit = Entry Price - (ATR × 1.5), Stop Loss = Entry Price + (ATR × 1.0)

This design allows the st...

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于随机指标与烛台模式的自动化市场反转交易策略-Automated-Market-Reversal-Trading-Strategy-Based-on-Stochastic-Indicator-and-Candlestick-Patterns.md
