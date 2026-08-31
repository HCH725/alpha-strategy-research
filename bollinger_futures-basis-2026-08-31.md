---
schema: strategy-research-record-v1
title: "Bollinger Band Breakout/Reversion Family Representative (Futures Basis)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bollinger_futures-basis
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/布林带结合快速与慢速移动平均线的多维趋势强化量化交易策略-Bollinger-Bands-with-Dual-SMA-Momentum-Enhanced-Quantitative-Trading-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bollinger Band Breakout/Reversion Family Representative (Futures Basis)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 布林带结合快速与慢速移动平均线的多维趋势强化量化交易策略-Bollinger-Bands-with-Dual-SMA-Momentum-Enhanced-Quantitative-Trading-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/布林带结合快速与慢速移动平均线的多维趋势强化量化交易策略-Bollinger-Bands-with-Dual-SMA-Momentum-Enhanced-Quantitative-Trading-Strategy.md

## Economic mechanism
### Source-reported
> The Bollinger Bands with Dual SMA Momentum Enhanced Quantitative Trading Strategy is a trend-following system specifically designed for market volatility. This strategy cleverly integrates the volatility channel of Bollinger Bands with a dual moving average trend confirmation mechanism, forming a multi-condition filtering trading decision framework. The core of the strategy lies in capturing strong signals when prices break through the upper Bollinger Band, and confirming trend direction through the positional relationship between fast and slow moving averages. It only enters long positions when multiple conditions are simultaneously satisfied, thereby improving trading accuracy and reliability.

### Research interpretation
Bollinger Band Breakout/Reversion logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Futures Basis.

## Signal
> The technical principles of this strategy are built on the synergistic effect of three core indicators:

1. **Bollinger Bands System**: The strategy employs a 21-period Bollinger Band with a standard deviation multiplier of 2.0, and flexibly allows selection of the basis moving average type (SMA, EMA, SMMA, WMA, or VWMA) based on parameter settings. Bollinger Bands capture the range of price volatility, providing a volatility perspective reference for trading.

2. **Dual Moving Average System**: The strategy introduces a 6-period Fast Simple Moving Average (Fast SMA) and a 45-period Slow Simple Moving Average (Slow SMA), forming a dual moving average system. The crossover and positional relationship between these two moving averages can effectively identify and confirm the current trend's direction and strength.

3. **Multi-Condition Entry Mechanism**: The strategy only establishes long positions when all the following conditions are met:
   - Closing price breaks above the upper Bollinger Band (close > upper)
   - Closing price is above the Slow Moving Average (close > slowSma)
   - Fast Moving Average is above the Slow Moving Average (fastSma > slowSma)

This multi-condition design ensures that positions are only entered when a strong upward trend is confirmed by multiple technical indicators, effectively filtering out false breakouts and weak signals.

The position closing conditions are similarly based on clear technical indicator signals. When the closing price falls below the lower Bollinger Band or the Fast Moving Average drops below the Slow Moving Average, the strategy will automatically close positions. This design enables the strategy to cut losses or lock in profits in a timely manner, avoiding losses caused by trend reversals.

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/布林带结合快速与慢速移动平均线的多维趋势强化量化交易策略-Bollinger-Bands-with-Dual-SMA-Momentum-Enhanced-Quantitative-Trading-Strategy.md
