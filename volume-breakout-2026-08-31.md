---
schema: strategy-research-record-v1
title: "Volume Confirmed Breakout Family Representative"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - volume-breakout
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多重目标智能波动率动量交易策略-Multi-Target-Intelligent-Volume-Momentum-Trading-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Volume Confirmed Breakout Family Representative

This document represents the normalized candidate for the **Volume Confirmed Breakout** strategy family. Hundreds of variants and parameterized versions exist in the source repository; this record captures the core economic mechanism and signal logic.

## Provenance

- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 多重目标智能波动率动量交易策略-Multi-Target-Intelligent-Volume-Momentum-Trading-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多重目标智能波动率动量交易策略-Multi-Target-Intelligent-Volume-Momentum-Trading-Strategy.md
- Note: This candidate represents 70 variants/duplicates found in the source corpus. See `coverage_manifest.csv` for full lineage.

## Economic mechanism
### Source-reported
The source describes this strategy as:
> No description provided.

### Research interpretation
Price breakouts confirmed by significant volume expansion, filtering out low-participation false moves.

## Signal
Source logic described as:
> See source code.

*Normalized Signal Interpretation:*
- Entry: Based on Volume Confirmed Breakout indicators crossing thresholds or each other.
- Exit: Reverse signal or predefined stop/profit.
- Parameter set: Highly variable across 70 family variants.

## Required data
- Market type: Crypto Spot or Perpetual Futures
- Timeframe: Configurable (commonly 15m, 1h, 4h)
- Features: OHLCV

## Execution assumptions
- Signal-to-order timing: Assumes execution on the next bar open after signal generation on candle close.
- Fees and slippage: Not rigidly accounted for in pure indicator logic; requires standard institutional bps assumptions.

## Evidence
### Source-reported
Sources typically report positive backtest equity curves, but these are highly susceptible to parameter overfitting across the 70 variants. Not independently reproduced.

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多重目标智能波动率动量交易策略-Multi-Target-Intelligent-Volume-Momentum-Trading-Strategy.md
