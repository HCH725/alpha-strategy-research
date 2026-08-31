---
schema: strategy-research-record-v1
title: "Machine Learning Family Representative (OHLCV)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - machine-learning_ohlcv
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/KNN-机器学习策略基于-K-近邻算法的趋势预测交易系统-KNN-Machine-Learning-Strategy-Trend-Prediction-Trading-System-Based-on-K-Nearest-Neighbors-Algorithm.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Machine Learning Family Representative (OHLCV)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: KNN-机器学习策略基于-K-近邻算法的趋势预测交易系统-KNN-Machine-Learning-Strategy-Trend-Prediction-Trading-System-Based-on-K-Nearest-Neighbors-Algorithm.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/KNN-机器学习策略基于-K-近邻算法的趋势预测交易系统-KNN-Machine-Learning-Strategy-Trend-Prediction-Trading-System-Based-on-K-Nearest-Neighbors-Algorithm.md

## Economic mechanism
### Source-reported
> This strategy employs the K-Nearest Neighbors (KNN) machine learning algorithm to predict price trends. By selecting different price computation methods (such as HL2, VWAP, SMA, etc.) as input values and various target values (such as price action, VWAP, volatility, etc.) for evaluation, the KNN algorithm identifies the K historical data points closest to the current market state. The strategy then makes long or short predictions based on the trend direction of these K data points. Additionally, the strategy applies a moving average to smooth the prediction results and improve stability. Finally, trading decisions are made according to the predicted results, and the current market trend prediction is visually demonstrated through changes in the background color.

### Research interpretation
Machine Learning logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: OHLCV.

## Signal
> **Features:** for the KNN algorithm.
**Target:** (e.

*Original Text:*
1. Select a price computation method (e.g., HL2, VWAP, SMA) as the input value for the KNN algorithm.
2. Choose an evaluation target (e.g., price action, VWAP, volatility) as the target value for the KNN algorithm.
3. Set the number of nearest neighbors (K) and smoothing period to adjust the sensitivity of the KNN algorithm and the smoothness of the prediction results.
4. For each new price data point, use the KNN algorithm to find the K historical data points closest to the current market state.
5. Based on the trend direction (bullish or bearish) of these K data points, vote to obtain the current market trend prediction.
6. Smooth the prediction results using a moving average to improve stability.
7. Generate trading signals (long or short) based on the smoothed prediction results and visually demonstrate the current market trend prediction through changes in the background color.

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/KNN-机器学习策略基于-K-近邻算法的趋势预测交易系统-KNN-Machine-Learning-Strategy-Trend-Prediction-Trading-System-Based-on-K-Nearest-Neighbors-Algorithm.md
