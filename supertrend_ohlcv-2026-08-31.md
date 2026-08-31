---
schema: strategy-research-record-v1
title: "Supertrend Family Representative (OHLCV)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - supertrend_ohlcv
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动态资金管理型SuperTrend趋势跟踪5倍风险回报策略-Dynamic-Position-Sizing-SuperTrend-Trend-Following-Strategy-with-51-Reward-Risk-Ratio.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Supertrend Family Representative (OHLCV)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 动态资金管理型SuperTrend趋势跟踪5倍风险回报策略-Dynamic-Position-Sizing-SuperTrend-Trend-Following-Strategy-with-51-Reward-Risk-Ratio.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动态资金管理型SuperTrend趋势跟踪5倍风险回报策略-Dynamic-Position-Sizing-SuperTrend-Trend-Following-Strategy-with-51-Reward-Risk-Ratio.md

## Economic mechanism
### Source-reported
> The Dynamic Position Sizing SuperTrend Trend-Following Strategy with 5:1 Reward-Risk Ratio is an advanced trend-following system based on the SuperTrend indicator that combines trend identification with precise capital management techniques by dynamically calculating position sizes to control risk. The core features of this strategy include utilizing ATR (Average True Range) to determine market volatility, grouping trades in the same direction, and establishing a fixed 5:1 reward-to-risk ratio for each trade group. The system supports multiple pyramiding entries in the same direction while maintaining strict risk management, with each entry risking only 1% of the account equity. This design allows the strategy to fully capitalize on strong trends while maintaining low risk levels.

### Research interpretation
Supertrend logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: OHLCV.

## Signal
> This strategy is based on the SuperTrend indicator's trend determination mechanism, combined with advanced techniques of grouped trading and dynamic position management. The main working principles are as follows:

1. **SuperTrend Indicator Calculation**: First, the ATR value is calculated, then basic upper and lower bands are obtained by adding and subtracting the ATR multiplier from the midpoint price (HL2). The key innovation lies in using recursive smoothing techniques to calculate the final bands, which improves the indicator's stability and reliability.

2. **Trend Determination Logic**: The trend is determined by comparing the closing price with the previous final bands. When the closing price breaks above the upper band, the trend turns upward; when it breaks below the lower band, the trend turns downward; otherwise, the original trend is maintained.

3. **Signal Generation Mechanism**: Buy signals are generated when the trend changes from downward to upward; sell signals are generated when the trend changes from upward to downward.

4. **Grouped Trade Management**: The strategy groups trades in the same direction and records the initial stop level (SuperTrend value) for each group. This allows the system to uniformly manage multiple related trades, improving capital efficiency.

5. **Dynamic Position Calculation**: The position size for each trade is calculated according to the formula `math.floor(strategy.equity * 0.01 / stopDistance)`, ensuring that each additional entry risks only 1% of the account.

6. **Risk-Reward Setup**: The system automatically sets a 5:1 risk-reward ratio for each trade group, with the profit target set at 5 times the stop distance, significantly improving the strategy's expected return.

7. **Intelligent Exit Mechanism**: Includes three exit conditions: stop loss (initial SuperTrend level), take profit (5 times stop distance), and conditional exits during trend reversals (accepting loss, reaching profit target, or moving to break...

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动态资金管理型SuperTrend趋势跟踪5倍风险回报策略-Dynamic-Position-Sizing-SuperTrend-Trend-Following-Strategy-with-51-Reward-Risk-Ratio.md
