---
schema: strategy-research-record-v1
title: "Momentum Family Representative (Order book / Depth data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - momentum_order-book-depth-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/趋势动量策略-之字形多重周期动态波段择时系统-Trend-Momentum-Strategy-Multi-Period-Dynamic-ZigZag-Wave-Timing-System.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Momentum Family Representative (Order book / Depth data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 趋势动量策略-之字形多重周期动态波段择时系统-Trend-Momentum-Strategy-Multi-Period-Dynamic-ZigZag-Wave-Timing-System.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/趋势动量策略-之字形多重周期动态波段择时系统-Trend-Momentum-Strategy-Multi-Period-Dynamic-ZigZag-Wave-Timing-System.md

## Economic mechanism
### Source-reported
> This strategy is a multi-dimensional trading system that combines the ZigZag indicator with the Williams %R indicator. It identifies significant swing highs and lows using the ZigZag indicator while confirming entry points with the Williams %R when the market reaches overbought or oversold conditions. This combination captures major market trend reversals while using momentum confirmation to improve trading accuracy.

### Research interpretation
Momentum logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Order book / Depth data.

## Signal
> The core logic is based on two main components:
1. The ZigZag indicator identifies significant swing points using depth and deviation parameters to filter market noise and determine trend direction. A new swing low indicates the start of an uptrend, while a new swing high indicates the start of a downtrend.
2. The Williams %R indicator calculates market momentum by comparing current price to the highest price within a specific period. Values crossing above -80 indicate oversold conditions (potential buy), while crossing below -20 indicate overbought conditions (potential sell).

Trading rules are as follows:
- Long Entry: ZigZag identifies a new swing low and Williams %R crosses up from oversold zone
- Short Entry: ZigZag identifies a new swing high and Williams %R crosses down from overbought zone
- Stop Loss is set at 1% and Take Profit at 2%

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
- None explicitly detected in structural scan; manual semantic review required for hidden repainting.

## Implementation status
not-implemented

## Adoption boundary
This is research material only. Not approved for trading.

## Related Wiki records
None

## Sources
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/趋势动量策略-之字形多重周期动态波段择时系统-Trend-Momentum-Strategy-Multi-Period-Dynamic-ZigZag-Wave-Timing-System.md
