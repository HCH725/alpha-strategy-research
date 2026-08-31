---
schema: strategy-research-record-v1
title: "Moving Average Crossover/Trend Family Representative (Renko charts)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - ma_renko-charts
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/逐级铺垫的均线兼顾策略Level-by-Level-Build-Up-Moving-Average-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Moving Average Crossover/Trend Family Representative (Renko charts)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 逐级铺垫的均线兼顾策略Level-by-Level-Build-Up-Moving-Average-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/逐级铺垫的均线兼顾策略Level-by-Level-Build-Up-Moving-Average-Strategy.md

## Economic mechanism
### Source-reported
> The Level by Level Build Up Moving Average Strategy is a trading strategy based on RENKO charts. It uses moving average indicators to smooth price and crossovers between moving averages of different timeframes as trading signals. Meanwhile, it also uses the ATR indicator to determine stop loss levels for more reasonable stops.

### Research interpretation
Moving Average Crossover/Trend logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Renko charts.

## Signal
> The core logic of this strategy includes:

1. Use input to select RENKO timeframe and ATR period

2. Calculate RENKO price and color. Turn to up when price breaks above previous RENKO price plus current ATR. Turn to down when price falls below previous RENKO price minus current ATR.

3. Use two integers BUY and SELL to record current long and short positions. 

4. When up breakout, if no short position then go long. If already short then close short position.
   When down breakout, if no long position then go short. If already long then close long position.

5. Plot RENKO chart using plot.

With this logic, the strategy can open long or short when price breaks previous level, and close positions when price reverse. Using ATR to determine breakout range makes stop loss more reasonable based on current volatility.

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- Renko charts

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
- Construct explicit PyBroker implementation honoring `Renko charts` and the detailed signal rules.
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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/逐级铺垫的均线兼顾策略Level-by-Level-Build-Up-Moving-Average-Strategy.md
