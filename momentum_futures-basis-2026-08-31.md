---
schema: strategy-research-record-v1
title: "Momentum Family Representative (Futures Basis)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - momentum_futures-basis
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动量跨市高效盈利策略Momentum-Swing-Effective-Profit-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Momentum Family Representative (Futures Basis)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 动量跨市高效盈利策略Momentum-Swing-Effective-Profit-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动量跨市高效盈利策略Momentum-Swing-Effective-Profit-Strategy.md

## Economic mechanism
### Source-reported
> The Momentum Swing Effective Profit Strategy is a quantitative trading strategy designed to capture profitable opportunities in mid-term financial markets by integrating swing trading principles and momentum indicators. The strategy utilizes a combination of technical indicators including moving averages, crossover signals, and volume analysis to generate buy and sell signals. The goal is to identify market trends and capitalize on price momentum for profits.

### Research interpretation
Momentum logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Futures Basis.

## Signal
> The buy signal is determined by multiple factors including A1, A2, A3, XG and weeklySlope. Specifically:

A1 Condition: Checks for specific price relationships, verifying the ratio of highest price to closing price is less than 1.03, ratio of opening price to lowest price is less than 1.03, and ratio of highest price to previous closing price is greater than 1.06. This condition looks for a specific pattern indicating potential bullish momentum.

A2 Condition: Checks for price relationships related to closing price, verifying ratio of closing price to opening price is greater than 1.05 or ratio of closing price to previous closing price is greater than 1.05. This condition looks for signs of upward price movement and momentum. 

A3 Condition: Focuses on volume, checking if current volume crosses above the highest volume over the last 60 periods. This condition aims to identify increased buying interests and potentially confirms the strength of the potential upward price movement.

XG Condition: Combines the A1 and A2 conditions and checks if they are true for both the current and previous bars. It also verifies the ratio of closing price to 5-period EMA crosses above the 9-period SMA of the same ratio. This condition helps identify potential buy signals when multiple factors align, indicating strong bullish momentum and potential entry point.

Weekly Trend Factor: Calculates the slope of 50-period SMA on a weekly timeframe. It checks if the slope is positive, indicating an overall upward trend on a weekly basis. This condition provides additional confirmation that the stock is in an upward trend.

When all these conditions are met, the buy condition is triggered, indicating a favorable time to enter a long position.

The sell condition is relatively simple in the strategy:

Sell Signal: The sell condition simply checks if the closing price crosses below the 10-period EMA. When this condition is met, it indicates a potential reversal or weakening of the upward price ...

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
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
- Construct explicit PyBroker implementation honoring `Futures Basis` and the detailed signal rules.
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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动量跨市高效盈利策略Momentum-Swing-Effective-Profit-Strategy.md
