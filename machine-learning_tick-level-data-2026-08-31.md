---
schema: strategy-research-record-v1
title: "Machine Learning Family Representative (Tick-level data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - machine-learning_tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多维度K近邻算法与烛台形态的量价分析交易策略-Multi-Dimensional-KNN-Algorithm-with-Volume-Price-Candlestick-Pattern-Trading-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Machine Learning Family Representative (Tick-level data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 多维度K近邻算法与烛台形态的量价分析交易策略-Multi-Dimensional-KNN-Algorithm-with-Volume-Price-Candlestick-Pattern-Trading-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多维度K近邻算法与烛台形态的量价分析交易策略-Multi-Dimensional-KNN-Algorithm-with-Volume-Price-Candlestick-Pattern-Trading-Strategy.md

## Economic mechanism
### Source-reported
> This strategy is a comprehensive trading system that combines K-Nearest Neighbors (KNN) machine learning algorithm, candlestick pattern recognition, and volume analysis. Through multi-dimensional analysis methods including moving average channels, volume threshold validation, and probability statistics, the strategy forms a three-dimensional analysis framework to capture potential trading opportunities.

### Research interpretation
Machine Learning logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Tick-level data.

## Signal
> **Features:** Underspecified, see original text.
**Target:** Underspecified, see original text.

*Original Text:*
The core logic of the strategy is built upon several key elements:
1. Using Simple Moving Average (SMA) and standard deviation to construct price channels for identifying overbought and oversold areas
2. Identifying nine classic candlestick patterns through programmatically defined conditions, including Hammer, Shooting Star, Engulfing patterns, etc.
3. Incorporating KNN algorithm to learn from historical price movements and predict future price directions
4. Using volume as a signal confirmation indicator, requiring volume to be above the set threshold when signals trigger
5. Calculating probability distributions for upward and downward movements as one of the signal filtering conditions

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多维度K近邻算法与烛台形态的量价分析交易策略-Multi-Dimensional-KNN-Algorithm-with-Volume-Price-Candlestick-Pattern-Trading-Strategy.md
