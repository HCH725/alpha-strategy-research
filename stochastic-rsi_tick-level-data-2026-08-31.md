---
schema: strategy-research-record-v1
title: "Stochastic RSI Reversal/Crossover Family Representative (Tick-level data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - stochastic-rsi_tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/随机相对强弱指数与蜡烛图确认的动态交易系统-Dynamic-Trading-System-with-Stochastic-RSI-and-Candlestick-Confirmation.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Stochastic RSI Reversal/Crossover Family Representative (Tick-level data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 随机相对强弱指数与蜡烛图确认的动态交易系统-Dynamic-Trading-System-with-Stochastic-RSI-and-Candlestick-Confirmation.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/随机相对强弱指数与蜡烛图确认的动态交易系统-Dynamic-Trading-System-with-Stochastic-RSI-and-Candlestick-Confirmation.md

## Economic mechanism
### Source-reported
> This strategy is a composite trading system that combines Stochastic Relative Strength Index (Stochastic RSI) with candlestick pattern confirmation. The system generates automated trading signals by analyzing SRSI indicator's overbought and oversold levels along with price action confirmation through candlestick patterns. The strategy employs advanced technical indicator combinations, incorporating both trend-following and reversal trading characteristics, demonstrating strong market adaptability.

### Research interpretation
Stochastic RSI Reversal/Crossover logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Tick-level data.

## Signal
> The core logic of the strategy is built on several key elements:
1. Uses 14-period RSI as the foundation to calculate Stochastic RSI values as the primary signal source
2. Applies 3-period simple moving averages to Stochastic RSI's K and D lines for signal smoothing
3. Sets 80 and 20 as overbought and oversold thresholds for market condition assessment
4. Incorporates current candlestick's open and close price relationship for trend confirmation
5. Generates long signals when K line crosses above oversold level with bullish candlestick
6. Triggers short signals when K line crosses below overbought level with bearish candlestick
7. Implements corresponding stop-loss when K line crosses overbought/oversold levels

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/随机相对强弱指数与蜡烛图确认的动态交易系统-Dynamic-Trading-System-with-Stochastic-RSI-and-Candlestick-Confirmation.md
