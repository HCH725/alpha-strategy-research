---
schema: strategy-research-record-v1
title: "Moving Average Crossover/Trend Family Representative (Tick-level data
- Futures Basis)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - ma_futures-basis-tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于双均线交叉量化策略The-EMA-Cross-Quantitative-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Moving Average Crossover/Trend Family Representative (Tick-level data
- Futures Basis)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 基于双均线交叉量化策略The-EMA-Cross-Quantitative-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于双均线交叉量化策略The-EMA-Cross-Quantitative-Strategy.md

## Economic mechanism
### Source-reported
> This strategy is based on the cross signals of two exponential moving averages (EMAs) for trading. When the short-term EMA crosses above the long-term EMA, it opens a long position; when the short-term EMA crosses below the long-term EMA, it closes the position. The strategy also introduces a stop-loss mechanism and a trading time filter to control risks and optimize strategy performance.

### Research interpretation
Moving Average Crossover/Trend logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Tick-level data
- Futures Basis.

## Signal
> This strategy uses two EMAs with different periods as the basis for trend judgment. Compared to simple moving averages (SMAs), EMAs can respond to price changes more quickly and have a more reasonable weight distribution. When the short-term EMA crosses above the long-term EMA, it indicates that the price may form an upward trend, and a long position is opened; conversely, when the short-term EMA crosses below the long-term EMA, it indicates that the upward trend may end, and the position is closed.

In addition to the moving average cross signals, the strategy also introduces a stop-loss mechanism. On the one hand, a fixed percentage stop-loss is set, that is, when the price drops by more than a specific percentage relative to the opening price, the position is forcibly closed to control losses; on the other hand, it is also possible to choose to close the position when the closing price is lower than the closing price of the previous candlestick. These two stop-loss methods can effectively control the strategy drawdown.

Moreover, the strategy also introduces a trading time filter. Users can set the start and end times of allowed trading by themselves, thus avoiding trading during specific time periods (such as holidays, non-trading hours, etc.).

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于双均线交叉量化策略The-EMA-Cross-Quantitative-Strategy.md
