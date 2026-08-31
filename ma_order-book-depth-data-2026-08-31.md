---
schema: strategy-research-record-v1
title: "Moving Average Crossover/Trend Family Representative (Order book / Depth data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - ma_order-book-depth-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多重时框EMA交叉趋势跟踪策略结合支阻力与智能追踪止损系统-Multi-Timeframe-EMA-Crossover-Trend-Following-Strategy-with-Support-Resistance-and-Smart-Trailing-Stop-System.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Moving Average Crossover/Trend Family Representative (Order book / Depth data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 多重时框EMA交叉趋势跟踪策略结合支阻力与智能追踪止损系统-Multi-Timeframe-EMA-Crossover-Trend-Following-Strategy-with-Support-Resistance-and-Smart-Trailing-Stop-System.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多重时框EMA交叉趋势跟踪策略结合支阻力与智能追踪止损系统-Multi-Timeframe-EMA-Crossover-Trend-Following-Strategy-with-Support-Resistance-and-Smart-Trailing-Stop-System.md

## Economic mechanism
### Source-reported
> This strategy is a trend-following trading system that incorporates multi-timeframe analysis, primarily based on crossover signals from three different exponential moving averages (EMAs), supplemented with higher timeframe support and resistance levels. The core of the strategy lies in utilizing the crossing relationships between EMA5, EMA8, and EMA13 to generate buy and sell signals, while implementing a percentage-based smart trailing stop mechanism to protect profits and limit potential losses. The entire system is designed to focus on trading with the trend while providing clear entry and exit rules and a risk management framework.

### Research interpretation
Moving Average Crossover/Trend logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Order book / Depth data.

## Signal
> Through in-depth code analysis, the operational principles of this strategy are as follows:

1. Signal Generation:
   - Buy Signal: Triggered when the short-term EMA5 simultaneously crosses above the medium-term EMA8 and long-term EMA13
   - Sell Signal: Triggered when the short-term EMA5 simultaneously crosses below the medium-term EMA8 and long-term EMA13

2. Higher Timeframe Filtering:
   - The strategy incorporates high and low points from the 1-hour chart as support and resistance levels
   - These levels are displayed on the chart as red (resistance) and green (support) lines, helping traders identify potential price reversal zones

3. Risk Management:
   - Implements a percentage-based trailing stop based on user-defined parameters (default 0.10%)
   - For long positions, the stop loss is set at trailOffset percentage below the highest price
   - For short positions, the stop loss is set at trailOffset percentage above the lowest price
   - The stop loss level continuously adjusts as the price moves in a favorable direction, locking in profits

4. Graphical Feedback:
   - Trade exit points are highlighted on the chart with cross markers
   - Trailing stop levels are marked with circles, providing intuitive visualization of risk control levels

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- Order book / Depth data

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
- Construct explicit PyBroker implementation honoring `Order book / Depth data` and the detailed signal rules.
- Test out-of-sample against structurally relevant assets.
- For hybrid candidates: isolate components via ablation to verify standalone predictive power of the core indicator.

## Crypto portability
direct

## Limitations
- underspecified parameter robustness
- not independently reproduced
- Pine Script `security()` call explicitly uses lookahead, severe leakage risk.

## Implementation status
not-implemented

## Adoption boundary
This is research material only. Not approved for trading.

## Related Wiki records
None

## Sources
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多重时框EMA交叉趋势跟踪策略结合支阻力与智能追踪止损系统-Multi-Timeframe-EMA-Crossover-Trend-Following-Strategy-with-Support-Resistance-and-Smart-Trailing-Stop-System.md
