---
schema: strategy-research-record-v1
title: "Moving Average Crossover/Trend Family Representative (Heikin-Ashi candles
- Futures Basis)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - ma_futures-basis-heikin-ashi-candles
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/ATR动态趋势跟踪与均线交叉交易策略-ATR-Dynamic-Trend-Following-and-EMA-Crossover-Trading-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Moving Average Crossover/Trend Family Representative (Heikin-Ashi candles
- Futures Basis)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: ATR动态趋势跟踪与均线交叉交易策略-ATR-Dynamic-Trend-Following-and-EMA-Crossover-Trading-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/ATR动态趋势跟踪与均线交叉交易策略-ATR-Dynamic-Trend-Following-and-EMA-Crossover-Trading-Strategy.md

## Economic mechanism
### Source-reported
> This is a trend following strategy based on the ATR (Average True Range) indicator, combining dynamic stop-loss and EMA crossover signals. The strategy calculates ATR to determine market volatility and uses this information to establish a dynamic trailing stop line. Trading signals are generated when price and EMA (Exponential Moving Average) break through the ATR trailing stop line. The strategy also offers the option to use regular or Heikin Ashi candles for calculations, adding flexibility.

### Research interpretation
Moving Average Crossover/Trend logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Heikin-Ashi candles
- Futures Basis.

## Signal
> The core logic of the strategy is based on the following key calculations:
1. Using ATR indicator to measure market volatility with adjustable period
2. Calculating dynamic stop-loss distance based on ATR value, adjusted by sensitivity parameter a
3. Building ATR trailing stop line that dynamically adjusts with price movement
4. Using 1-period EMA crossover with ATR trailing stop line to determine trading signals
5. Opening long positions when EMA breaks above ATR trailing stop line, short when breaking below
6. Option to use regular closing price or Heikin Ashi HLC3 price as calculation basis

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- Heikin-Ashi candles
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
- Construct explicit PyBroker implementation honoring `Heikin-Ashi candles
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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/ATR动态趋势跟踪与均线交叉交易策略-ATR-Dynamic-Trend-Following-and-EMA-Crossover-Trading-Strategy.md
