---
schema: strategy-research-record-v1
title: "ATR Volatility Family Representative"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - atr-volatility
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/数字货币期货多品种ATR策略教学.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ATR Volatility Family Representative

This document represents the normalized candidate for the **ATR Volatility** strategy family. Hundreds of variants and parameterized versions exist in the source repository; this record captures the core economic mechanism and signal logic.

## Provenance

- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 数字货币期货多品种ATR策略教学.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/数字货币期货多品种ATR策略教学.md
- Note: This candidate represents 77 variants/duplicates found in the source corpus. See `coverage_manifest.csv` for full lineage.

## Economic mechanism
### Source-reported
The source describes this strategy as:
> No description provided.

### Research interpretation
Volatility tracking, typically for adaptive trailing stops or breakout thresholds.

## Signal
Source logic described as:
> See source code.

*Normalized Signal Interpretation:*
- Entry: Based on ATR Volatility indicators crossing thresholds or each other.
- Exit: Reverse signal or predefined stop/profit.
- Parameter set: Highly variable across 77 family variants.

## Required data
- Market type: Crypto Spot or Perpetual Futures
- Timeframe: Configurable (commonly 15m, 1h, 4h)
- Features: OHLCV

## Execution assumptions
- Signal-to-order timing: Assumes execution on the next bar open after signal generation on candle close.
- Fees and slippage: Not rigidly accounted for in pure indicator logic; requires standard institutional bps assumptions.

## Evidence
### Source-reported
Sources typically report positive backtest equity curves, but these are highly susceptible to parameter overfitting across the 77 variants. Not independently reproduced.

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
- **FMZ Runtime Semantics**: Check `exchange.GetRecords()` and `exchange.GetTicker()` timestamp alignment. Ensure signal executes on the next bar open, not interpolating current bar close.

## Implementation status
not-implemented

## Adoption boundary
This is research material only. Not approved for trading.

## Related Wiki records
None identified.

## Sources
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/数字货币期货多品种ATR策略教学.md
