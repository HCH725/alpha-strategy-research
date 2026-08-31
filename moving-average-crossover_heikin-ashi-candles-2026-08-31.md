---
schema: strategy-research-record-v1
title: "Moving Average Crossover Family Representative"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - moving-average-crossover_heikin-ashi-candles
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动态ATR追踪止损与均线交叉组合策略-Dynamic-ATR-Trailing-Stop-with-EMA-Cross-Combination-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Moving Average Crossover Family Representative

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 动态ATR追踪止损与均线交叉组合策略-Dynamic-ATR-Trailing-Stop-with-EMA-Cross-Combination-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动态ATR追踪止损与均线交叉组合策略-Dynamic-ATR-Trailing-Stop-with-EMA-Cross-Combination-Strategy.md

## Economic mechanism
### Source-reported
> This strategy is a comprehensive trading system that combines ATR dynamic trailing stop-loss and EMA crossovers, integrating multiple technical indicators for trade filtering and risk control. Operating on a 15-minute timeframe, the strategy utilizes multiple dimensions of indicators including EMA, ATR volatility, RSI, and volume to determine trading signals while employing dynamic trailing stops for risk management.

### Research interpretation
Moving Average Crossover logic. Standard MA crossover verified by code. Data dependency: Heikin-Ashi candles

## Signal
> The core logic includes several key components:
1. Entry conditions with multiple filters:
   - Price above/below 100-period EMA
   - 1-hour 100 EMA trend confirmation
   - Price crossover with ATR trailing stop line
   - RSI between 30-70 in neutral zone
   - Current volume above 20-period average volume
2. Risk control system:
   - Dynamic trailing stop based on 3x ATR
   - Take profit set at 2x ATR
3. Exit mechanism:
   - 15 and 17 period EMA crossover signals on consecutive bars
   - Trailing stop or take profit trigger

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- Heikin-Ashi candles

## Execution assumptions
- Signal-to-fill timing: underspecified; implementation must choose and test a causal execution convention.
- Fees/slippage/latency: underspecified; standard institutional assumptions must be supplied.

## Evidence
### Source-reported
Source claims vary by variant. Not independently reproduced.

### Independently reproduced
Not independently reproduced.

### Negative evidence
None identified in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan
- Construct explicit PyBroker implementation honoring `Heikin-Ashi candles` and the detailed signal rules.
- Test out-of-sample against structurally relevant assets.
- For hybrid candidates: isolate components via ablation to verify standalone predictive power of the core indicator.

## Crypto portability
direct

## Limitations
- underspecified parameter robustness
- not independently reproduced
- leakage/repainting risk: manual semantic review required for hidden repainting in original source code.

## Implementation status
not-implemented

## Adoption boundary
This is research material only. Not approved for trading.

## Related Wiki records
None

## Sources
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动态ATR追踪止损与均线交叉组合策略-Dynamic-ATR-Trailing-Stop-with-EMA-Cross-Combination-Strategy.md
