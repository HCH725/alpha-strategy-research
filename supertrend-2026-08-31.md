---
schema: strategy-research-record-v1
title: "Supertrend Family Representative"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - supertrend
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于SuperTrend的长线交易策略Long-Term-Trading-Strategy-Based-on-SuperTrend.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Supertrend Family Representative

This document represents the normalized candidate for the **Supertrend** strategy family. Hundreds of variants and parameterized versions exist in the source repository; this record captures the core economic mechanism and signal logic.

## Provenance

- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 基于SuperTrend的长线交易策略Long-Term-Trading-Strategy-Based-on-SuperTrend.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于SuperTrend的长线交易策略Long-Term-Trading-Strategy-Based-on-SuperTrend.md
- Note: This candidate represents 89 variants/duplicates found in the source corpus. See `coverage_manifest.csv` for full lineage.

## Economic mechanism
### Source-reported
The source describes this strategy as:
> This strategy identifies long opportunities using the SuperTrend indicator. It uses ATR and a multiplier to determine dynamic support levels for long entry. The focus is on long trades.

### Research interpretation
Trend following using ATR-based trailing stops to stay in prevailing trends.

## Signal
Source logic described as:
> 1. The upper and lower bands are calculated based on ATR period, multiplier. Breaking upper band indicates uptrend, breaking lower band indicates downtrend.

2. The current trend is tracked, with 1 for uptrend and -1 for downtrend. Price breaking above upper band switches trend from down to up, generating buy signal. Breaking below lower band switches from up to down, generating sell signal.

3. A moving average is added as a trend filter. Buy only if price is above MA when breaking above upper band. Sell only if price is below MA when breaking below lower band. This avoids fake breakouts. 

4. Visual helpers highlight trends, signals etc to assist with decision making.

*Normalized Signal Interpretation:*
- Entry: Based on Supertrend indicators crossing thresholds or each other.
- Exit: Reverse signal or predefined stop/profit.
- Parameter set: Highly variable across 89 family variants.

## Required data
- Market type: Crypto Spot or Perpetual Futures
- Timeframe: Configurable (commonly 15m, 1h, 4h)
- Features: OHLCV

## Execution assumptions
- Signal-to-order timing: Assumes execution on the next bar open after signal generation on candle close.
- Fees and slippage: Not rigidly accounted for in pure indicator logic; requires standard institutional bps assumptions.

## Evidence
### Source-reported
Sources typically report positive backtest equity curves, but these are highly susceptible to parameter overfitting across the 89 variants. Not independently reproduced.

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于SuperTrend的长线交易策略Long-Term-Trading-Strategy-Based-on-SuperTrend.md
