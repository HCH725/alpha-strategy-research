---
schema: strategy-research-record-v1
title: "Stochastic RSI Reversal/Crossover Family Representative (Tick-level data
- Futures Basis)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - stochastic-rsi_futures-basis-tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多因子均值回归策略结合随机相对强弱指标与布林带的均值回归交易系统-Multi-Factor-Mean-Reversion-Strategy-A-Mean-Reversion-Trading-System-Combining-Stochastic-RSI-and-Bollinger-Bands.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Stochastic RSI Reversal/Crossover Family Representative (Tick-level data
- Futures Basis)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 多因子均值回归策略结合随机相对强弱指标与布林带的均值回归交易系统-Multi-Factor-Mean-Reversion-Strategy-A-Mean-Reversion-Trading-System-Combining-Stochastic-RSI-and-Bollinger-Bands.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多因子均值回归策略结合随机相对强弱指标与布林带的均值回归交易系统-Multi-Factor-Mean-Reversion-Strategy-A-Mean-Reversion-Trading-System-Combining-Stochastic-RSI-and-Bollinger-Bands.md

## Economic mechanism
### Source-reported
> This strategy is a multi-factor mean reversion trading system that combines the Stochastic Relative Strength Index (Stochastic RSI) and Bollinger Bands. It operates on a 5-minute timeframe, primarily designed to capture price reversion opportunities during market overbought and oversold conditions. The core concept of the strategy is to buy when the price is at the lower Bollinger Band and the Stochastic RSI is below 0.1 (oversold region), and to sell when the price is at the upper Bollinger Band and the Stochastic RSI is above 0.9 (overbought region). This multi-factor combination effectively enhances the reliability of trading signals, filtering out potential false signals that might arise from using a single indicator.

### Research interpretation
Stochastic RSI Reversal/Crossover logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Tick-level data
- Futures Basis.

## Signal
> The strategy is based on the combination of two technical indicators:

1. **Stochastic Relative Strength Index (Stochastic RSI)**:
   - First, calculate the basic RSI value: `rsi = ta.rsi(request.security(syminfo.tickerid, "5", close), length)`
   - Then calculate the stochastic based on RSI: `k = ta.sma(ta.stoch(rsi, rsi, rsi, length), smoothK)`
   - Next, calculate the smoothed moving average of K: `d = ta.sma(k, smoothD)`
   - Finally, take the average of K and D lines as the Stochastic RSI: `stochRSI = (k + d) / 2`

2. **Bollinger Bands**:
   - Middle Band (Basis): 20-period simple moving average: `basis = ta.sma(request.security(syminfo.tickerid, "5", close), bbLength)`
   - Standard Deviation: `dev = bbStdDev * ta.stdev(request.security(syminfo.tickerid, "5", close), bbLength)`
   - Upper Band: Middle Band plus 2 times standard deviation: `upperBand = basis + dev`
   - Lower Band: Middle Band minus 2 times standard deviation: `lowerBand = basis - dev`

Trading Logic:
- Buy Condition: `stochRSI < 0.1 and close <= lowerBand` (Stochastic RSI below 0.1 and price touching or breaking through the lower Bollinger Band)
- Sell Condition: `stochRSI > 0.9 and close >= upperBand` (Stochastic RSI above 0.9 and price touching or breaking through the upper Bollinger Band)

Exit Logic:
- Long Position Close: Stochastic RSI rises above 0.2: `exitBuyCondition = stochRSI > 0.2`
- Short Position Close: Stochastic RSI falls below 0.8: `exitSellCondition = stochRSI < 0.8`

The strategy also sets entry price, stop loss, and take profit parameters, but in the code, the stop loss values are set to 0 and 1, and take profit values are set to 0.8 and 0.2 respectively. These parameters need to be optimized based on the actual trading asset.

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- Tick-level data
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
- Construct explicit PyBroker implementation honoring `Tick-level data
- Futures Basis` and the detailed signal rules.
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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多因子均值回归策略结合随机相对强弱指标与布林带的均值回归交易系统-Multi-Factor-Mean-Reversion-Strategy-A-Mean-Reversion-Trading-System-Combining-Stochastic-RSI-and-Bollinger-Bands.md
