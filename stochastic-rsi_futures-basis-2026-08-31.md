---
schema: strategy-research-record-v1
title: "Stochastic RSI Reversal/Crossover Family Representative (Futures Basis)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - stochastic-rsi_futures-basis
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于双均线交叉RSI和随机指标的短线量化交易策略-Short-term-Quantitative-Trading-Strategy-Based-on-Dual-Moving-Average-Crossover-RSI-and-Stochastic-Indicators.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Stochastic RSI Reversal/Crossover Family Representative (Futures Basis)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 基于双均线交叉RSI和随机指标的短线量化交易策略-Short-term-Quantitative-Trading-Strategy-Based-on-Dual-Moving-Average-Crossover-RSI-and-Stochastic-Indicators.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于双均线交叉RSI和随机指标的短线量化交易策略-Short-term-Quantitative-Trading-Strategy-Based-on-Dual-Moving-Average-Crossover-RSI-and-Stochastic-Indicators.md

## Economic mechanism
### Source-reported
> This strategy combines dual moving average crossover, RSI, and stochastic indicators to seek high-probability trading opportunities in short-term trading through the joint confirmation of multiple technical indicators. The strategy uses the crossover of 20-day and 50-day moving averages as the main trading signal, and incorporates RSI and stochastic indicators as auxiliary judgments to double-check the trading signals. In addition, the strategy also employs ATR as the basis for stop-loss and take-profit, managing positions with a fixed risk-reward ratio, striving to obtain stable returns while controlling risks.

### Research interpretation
Stochastic RSI Reversal/Crossover logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Futures Basis.

## Signal
> 1. Calculate the 20-day and 50-day moving averages. When the short-term average crosses above the long-term average, it generates a long signal; conversely, it generates a short signal.
2. Introduce the RSI indicator as an auxiliary judgment, only considering establishing positions when the RSI indicator has not reached the overbought or oversold range.
3. Introduce the stochastic indicator as an auxiliary judgment, only considering establishing positions when the stochastic indicator's K line has not reached the overbought or oversold range.
4. Use ATR to calculate stop-loss and take-profit levels, setting stop-loss and take-profit prices according to a 1:2 risk-reward ratio.
5. When going long, the stop-loss level is the lowest price minus ATR, and the take-profit level is the highest price plus 2 times ATR; when going short, the stop-loss level is the highest price plus ATR, and the take-profit level is the lowest price minus 2 times ATR.

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于双均线交叉RSI和随机指标的短线量化交易策略-Short-term-Quantitative-Trading-Strategy-Based-on-Dual-Moving-Average-Crossover-RSI-and-Stochastic-Indicators.md
