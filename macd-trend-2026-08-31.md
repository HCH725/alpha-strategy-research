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
  - macd-trend
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动量熔断MACD策略Momentum-Breakdown-MACD-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MACD Trend Family Representative

This document represents the normalized candidate for the **MACD Trend** strategy family. Hundreds of variants and parameterized versions exist in the source repository; this record captures the core economic mechanism and signal logic.

## Provenance

- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 动量熔断MACD策略Momentum-Breakdown-MACD-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动量熔断MACD策略Momentum-Breakdown-MACD-Strategy.md
- Note: This candidate represents 133 variants/duplicates found in the source corpus. See `coverage_manifest.csv` for full lineage.

## Economic mechanism
### Source-reported
The source describes this strategy as:
> 动量熔断MACD策略主要是利用MACD指标和动量指标的组合,形成交易信号,属于趋势跟踪策略。该策略首先计算快线EMA和慢线EMA,然后计算MACD值,再计算MACD的信号线。同时计算价格的动量值。当动量值和MACD差值形成零轴上方交叉时产生买入信号;当动量值和MACD差值形成零轴下方交叉时产生卖出信号,属于双重确认形成交易信号的策略。

### Research interpretation
Momentum and trend following based on MACD line and signal crossovers.

## Signal
Source logic described as:
> This strategy is mainly based on the combination of MACD and Momentum indicators. 

The MACD indicator is a trend-following indicator, consisting of the fast EMA, slow EMA, and MACD histogram. The fast EMA usually has a parameter of 12 days, and the slow EMA has a parameter of 26 days. The calculation formulas are:

Fast EMA = EMA(close price, 12)

Slow EMA = EMA(close price, 26) 

MACD = Fast EMA - Slow EMA

Signal Line = EMA(MACD, 9)

When the fast EMA crosses above the slow EMA, it means the short-term uptrend is stronger than the long-term trend, which is a buy signal. When the fast EMA crosses below the slow EMA, it means the long-term downtrend is stronger than the short-term trend, which is a sell signal.

The Momentum indicator reflects the speed of price movement, and its calculation formula is:

Momentum = Today's closing price - Closing price N days ago

Where N is usually set to 10. When today's closing price rises above that of N days ago, the momentum value is positive, indicating an uptrend. When today's closing price falls below that of N days ago, the momentum value is negative, indicating a downtrend.

This strategy combines the MACD indicator with the Momentum indicator. The criteria for generating trading signals is: when the difference between the MACD difference and the momentum difference crosses above the zero level, it generates a buy signal, forming an above-zero crossover. When the difference crosses below the zero level, it generates a sell signal, forming a below-zero crossover. This belongs to a dual confirmation mechanism for producing trading signals, which can filter out some false signals and achieve trend following.

*Normalized Signal Interpretation:*
- Entry: Based on MACD Trend indicators crossing thresholds or each other.
- Exit: Reverse signal or predefined stop/profit.
- Parameter set: Highly variable across 133 family variants.

## Required data
- Market type: Crypto Spot or Perpetual Futures
- Timeframe: Configurable (commonly 15m, 1h, 4h)
- Features: OHLCV

## Execution assumptions
- Signal-to-order timing: Assumes execution on the next bar open after signal generation on candle close.
- Fees and slippage: Not rigidly accounted for in pure indicator logic; requires standard institutional bps assumptions.

## Evidence
### Source-reported
Sources typically report positive backtest equity curves, but these are highly susceptible to parameter overfitting across the 133 variants. Not independently reproduced.

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动量熔断MACD策略Momentum-Breakdown-MACD-Strategy.md
