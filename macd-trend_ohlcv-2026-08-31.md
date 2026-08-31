---
schema: strategy-research-record-v1
title: "MACD Trend Family Representative"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - macd-trend_ohlcv
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多指标趋势动量融合策略-RSI-MACD-双重超趋势跟踪系统-Multi-Indicator-Trend-Momentum-Fusion-Strategy-RSI-MACD-Dual-Supertrend-Tracking-System.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MACD Trend Family Representative

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 多指标趋势动量融合策略-RSI-MACD-双重超趋势跟踪系统-Multi-Indicator-Trend-Momentum-Fusion-Strategy-RSI-MACD-Dual-Supertrend-Tracking-System.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多指标趋势动量融合策略-RSI-MACD-双重超趋势跟踪系统-Multi-Indicator-Trend-Momentum-Fusion-Strategy-RSI-MACD-Dual-Supertrend-Tracking-System.md

## Economic mechanism
### Source-reported
> This strategy is a comprehensive trading system that integrates multiple technical indicators, primarily combining the Relative Strength Index (RSI), Moving Average Convergence Divergence (MACD), dual Supertrend indicators, and an Average True Range (ATR)-based risk management mechanism. Through multi-level indicator confirmation, the strategy builds a trading framework that both tracks trends and captures momentum shifts, effectively filtering market noise and reducing the risk of false signals. The core logic is to first confirm the market's dominant trend using dual Supertrends (factors 2 and 7), then verify trend direction through MACD crossovers and momentum changes, and finally identify optimal entry points using RSI overbought/oversold zones, while implementing comprehensive risk control through ATR-based stop-loss, breakeven, and trailing stop mechanisms.

### Research interpretation
MACD Trend logic. Standard MACD strategy verified by code. Data dependency: OHLCV

## Signal
> The operation mechanism of this strategy is based on four key components: trend identification, momentum confirmation, entry conditions, and risk management.

1. **Trend Identification**: Employs dual Supertrend indicators (factors 2 and 7) as trend filters. The Supertrend indicator is designed to track the market's dominant trend and filter out market noise. By using two Supertrend indicators with different parameters, the strategy requires both indicators to simultaneously confirm the same direction, greatly enhancing the reliability of trend signals.

2. **Momentum Confirmation**: Uses MACD (5,13,9) to detect early trend reversals. The strategy requires the crossover of the MACD line and signal line as the first layer of confirmation, and demands continuous MACD movement (rising or falling) as the second layer of confirmation, ensuring the capture of genuine momentum shifts rather than short-term fluctuations.

3. **Entry Conditions**:
   - Long Conditions: RSI below 35 (oversold zone), MACD line crosses above the signal line and continues to rise, both Supertrend indicators show an uptrend (direction1 and direction2 both equal 1)
   - Short Conditions: RSI above 65 (overbought zone), MACD line crosses below the signal line and continues to fall, both Supertrend indicators show a downtrend (direction1 and direction2 both equal -1)

4. **Risk Management**:
   - Stop Loss Setting: Dynamic stop loss based on ATR, positioned 1x ATR below (for longs) or above (for shorts) the entry price
   - Moving Stop Loss to Breakeven: When price moves 1x ATR in the favorable direction, stop loss is moved to the entry price
   - Profit Target: Set at 2.5x ATR above (for longs) or below (for shorts) the entry price
   - Trailing Stop: Uses a 1x ATR trailing stop that adjusts as price moves in the favorable direction, locking in profits

The core code implements a custom Supertrend function for calculating Supertrend levels and direction, and combines it with dynamic calculations of...

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- OHLCV

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
- Construct explicit PyBroker implementation honoring `OHLCV` and the detailed signal rules.
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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多指标趋势动量融合策略-RSI-MACD-双重超趋势跟踪系统-Multi-Indicator-Trend-Momentum-Fusion-Strategy-RSI-MACD-Dual-Supertrend-Tracking-System.md
