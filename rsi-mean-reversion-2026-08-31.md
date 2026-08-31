---
schema: strategy-research-record-v1
title: "RSI Mean Reversion Family Representative"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - rsi-mean-reversion
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/K线Stochastic-RSI交易策略Renko-Stochastic-RSI-Trading-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RSI Mean Reversion Family Representative

This document represents the normalized candidate for the **RSI Mean Reversion** strategy family. Hundreds of variants and parameterized versions exist in the source repository; this record captures the core economic mechanism and signal logic.

## Provenance

- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: K线Stochastic-RSI交易策略Renko-Stochastic-RSI-Trading-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/K线Stochastic-RSI交易策略Renko-Stochastic-RSI-Trading-Strategy.md
- Note: This candidate represents 394 variants/duplicates found in the source corpus. See `coverage_manifest.csv` for full lineage.

## Economic mechanism
### Source-reported
The source describes this strategy as:
> This is a Stochastic RSI trading strategy designed for use on Renko charts. It generates buy and sell signals using the crossover and crossunder of Stochastic RSI K and D lines. The strategy is specialized for Renko charts and can effectively filter market noise and identify trends.

### Research interpretation
Mean reversion based on RSI overbought/oversold levels.

## Signal
Source logic described as:
> The trading signals are primarily based on the Stochastic RSI indicator, which combines the advantages of RSI and Stochastic oscillator.

First, the RSI value over a period is calculated, then Stochastic RSI is computed based on the RSI values. Stochastic RSI contains two lines:

- K line: Moving average of RSI values over a period, represents the fast Stochastic RSI line

- D line: Moving average of the K line, represents the slow Stochastic RSI line

When K line crosses above D line, a buy signal is generated. When K line crosses below D line, a sell signal is generated.

In addition, this strategy is only applied on Renko charts, which filters market noise by constructing bars based on price change threshold, identifying trend direction.

*Normalized Signal Interpretation:*
- Entry: Based on RSI Mean Reversion indicators crossing thresholds or each other.
- Exit: Reverse signal or predefined stop/profit.
- Parameter set: Highly variable across 394 family variants.

## Required data
- Market type: Crypto Spot or Perpetual Futures
- Timeframe: Configurable (commonly 15m, 1h, 4h)
- Features: OHLCV

## Execution assumptions
- Signal-to-order timing: Assumes execution on the next bar open after signal generation on candle close.
- Fees and slippage: Not rigidly accounted for in pure indicator logic; requires standard institutional bps assumptions.

## Evidence
### Source-reported
Sources typically report positive backtest equity curves, but these are highly susceptible to parameter overfitting across the 394 variants. Not independently reproduced.

### Independently reproduced
Not independently reproduced.

### Negative evidence
None identified in the reviewed sources; absence is not evidence of no negative result. High risk of parameter curve-fitting.

## Falsification plan
- Implement cleanly in PyBroker.
- Test across 2020-2026 on major pairs (BTC, ETH, SOL) using out-of-sample data.
- Ablation: Disable any secondary confirming indicators to test if the primary signal possesses standalone predictive power.
- Failure metric: Sharpe < 1.0 out-of-sample or excessive sensitivity to minor parameter changes (e.g. MA length +/- 2).

## Crypto portability
direct

## Limitations
- underspecified parameter robustness
- not independently reproduced
- **Pine Script Semantics**: Verify `calc_on_every_tick` is false, and ensure historical data references (`[1]`) are used to prevent same-bar lookahead bias. Check `security()` calls for repainting.

## Implementation status
not-implemented

## Adoption boundary
This is research material only. Not approved for trading.

## Related Wiki records
None identified.

## Sources
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/K线Stochastic-RSI交易策略Renko-Stochastic-RSI-Trading-Strategy.md
