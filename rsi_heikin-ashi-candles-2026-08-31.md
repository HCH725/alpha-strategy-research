---
schema: strategy-research-record-v1
title: "RSI Based Mean Reversion Family Representative (Heikin-Ashi candles)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - rsi_heikin-ashi-candles
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/ATR-RSI增强型趋势追踪交易系统-ATR-RSI-Enhanced-Trend-Following-Trading-System.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RSI Based Mean Reversion Family Representative (Heikin-Ashi candles)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: ATR-RSI增强型趋势追踪交易系统-ATR-RSI-Enhanced-Trend-Following-Trading-System.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/ATR-RSI增强型趋势追踪交易系统-ATR-RSI-Enhanced-Trend-Following-Trading-System.md

## Economic mechanism
### Source-reported
> The ATR-RSI Enhanced Trend Following Trading System is an advanced quantitative trading strategy that combines Average True Range (ATR), Relative Strength Index (RSI), and Exponential Moving Average (EMA). This strategy utilizes the UT Bot alert system as its core, identifying potential trading opportunities through ATR trailing stops, RSI filtering, and EMA crossovers. The system also incorporates a Heikin Ashi candle option to reduce market noise and improve signal quality. This multi-indicator fusion approach aims to capture strong market trends while managing risk through percentage-based exit points.

### Research interpretation
RSI Based Mean Reversion logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Heikin-Ashi candles.

## Signal
> 1. ATR Trailing Stop: Uses ATR to calculate dynamic stop-loss levels that adjust with market volatility, providing a flexible foundation for trend following.

2. RSI Filter: Allows buying only when RSI is above 50 and selling when below 50, ensuring trade direction aligns with overall market momentum.

3. EMA Crossover: Utilizes crossovers between a 1-period EMA and the ATR trailing stop line to generate trade signals, providing additional trend confirmation.

4. Heikin Ashi Option: Offers the choice to use smoothed candles to reduce false signals and improve trend identification accuracy.

5. Percentage-Based Exits: Sets fixed percentage profit and stop-loss levels based on entry price to manage risk-reward for each trade.

6. Non-Repainting Design: Ensures historical backtest results are consistent with real-time trading performance.

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- Heikin-Ashi candles

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
- Construct explicit PyBroker implementation honoring `Heikin-Ashi candles` and the detailed signal rules.
- Test out-of-sample against structurally relevant assets.
- For hybrid candidates: isolate components via ablation to verify standalone predictive power of the core indicator.

## Crypto portability
direct

## Limitations
- underspecified parameter robustness
- not independently reproduced
- Pine Script `security()` call explicitly uses lookahead, severe leakage risk.

## Implementation status
not-implemented

## Adoption boundary
This is research material only. Not approved for trading.

## Related Wiki records
None

## Sources
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/ATR-RSI增强型趋势追踪交易系统-ATR-RSI-Enhanced-Trend-Following-Trading-System.md
