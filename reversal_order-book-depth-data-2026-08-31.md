---
schema: strategy-research-record-v1
title: "Price Reversal Family Representative (Order book / Depth data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reversal_order-book-depth-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/自适应趋势跟踪与反转识别策略基于ZigZag与Aroon指标的量化交易系统-Adaptive-Trend-Following-and-Reversal-Detection-Strategy-A-Quantitative-Trading-System-Based-on-ZigZag-and-Aroon-Indicators.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Price Reversal Family Representative (Order book / Depth data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 自适应趋势跟踪与反转识别策略基于ZigZag与Aroon指标的量化交易系统-Adaptive-Trend-Following-and-Reversal-Detection-Strategy-A-Quantitative-Trading-System-Based-on-ZigZag-and-Aroon-Indicators.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/自适应趋势跟踪与反转识别策略基于ZigZag与Aroon指标的量化交易系统-Adaptive-Trend-Following-and-Reversal-Detection-Strategy-A-Quantitative-Trading-System-Based-on-ZigZag-and-Aroon-Indicators.md

## Economic mechanism
### Source-reported
> This strategy is an adaptive trading system that combines the ZigZag indicator with the Aroon indicator. The ZigZag indicator filters market noise and identifies significant price movements, while the Aroon indicator confirms trend strength and potential reversal points. Through the synergistic combination of these two indicators, the strategy maintains sensitivity to trends while also capturing market turning points in a timely manner.

### Research interpretation
Price Reversal logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Order book / Depth data.

## Signal
> The core logic of the strategy is based on the following key elements:
1. The ZigZag indicator filters short-term fluctuations by setting a depth parameter (zigzagDepth), retaining only statistically significant price movements.
2. The Aroon indicator generates Aroon Up and Aroon Down lines by calculating the time interval between highest and lowest prices (aroonLength).
3. Entry signals are triggered by two concurrent conditions:
   - Long positions are opened when Aroon Up crosses above Aroon Down and ZigZag shows an upward trend
   - Short positions are opened when Aroon Down crosses above Aroon Up and ZigZag shows a downward trend
4. Exit signals are triggered by Aroon indicator crossovers:
   - Long positions are closed when Aroon Down crosses above Aroon Up
   - Short positions are closed when Aroon Up crosses above Aroon Down

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/自适应趋势跟踪与反转识别策略基于ZigZag与Aroon指标的量化交易系统-Adaptive-Trend-Following-and-Reversal-Detection-Strategy-A-Quantitative-Trading-System-Based-on-ZigZag-and-Aroon-Indicators.md
