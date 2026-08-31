---
schema: strategy-research-record-v1
title: "Bollinger Bands Family Representative"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bollinger-bands_ohlcv
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/RSI-布林通道整合策略动态自适应的多指标交易系统-RSI-Bollinger-Bands-Integration-Strategy-A-Dynamic-Self-Adaptive-Multi-Indicator-Trading-System.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bollinger Bands Family Representative

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: RSI-布林通道整合策略动态自适应的多指标交易系统-RSI-Bollinger-Bands-Integration-Strategy-A-Dynamic-Self-Adaptive-Multi-Indicator-Trading-System.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/RSI-布林通道整合策略动态自适应的多指标交易系统-RSI-Bollinger-Bands-Integration-Strategy-A-Dynamic-Self-Adaptive-Multi-Indicator-Trading-System.md

## Economic mechanism
### Source-reported
> The RSI-Bollinger Bands Integration Strategy is a quantitative trading system that combines the Relative Strength Index (RSI), Bollinger Bands (BB), and Average True Range (ATR). This strategy aims to capture overbought and oversold market conditions while managing risk through dynamic profit-taking and stop-loss levels. The core idea is to enter trades when the price touches the lower Bollinger Band and the RSI is in the oversold territory, and exit when the RSI reaches overbought levels. By integrating multiple technical indicators, the strategy seeks to maintain stability and adaptability across various market conditions.

### Research interpretation
Bollinger Bands logic. Standard Bollinger strategy verified by code. Data dependency: OHLCV

## Signal
> 1. Entry Conditions:
   - Current closing price is below the lower Bollinger Band of the previous candle
   - Previous candle is bullish (close higher than open)
   - RSI(9) of the previous candle is less than or equal to 25

2. Exit Conditions:
   - RSI(9) exceeds 75
   - Or when dynamic take-profit/stop-loss levels are hit

3. Risk Management:
   - Uses ATR(10) to dynamically set take-profit and stop-loss levels
   - Stop-loss is set at entry price minus (stop_risk * ATR)
   - Take-profit is set at entry price plus (take_risk * ATR)

4. Position Sizing:
   - Uses 20% of the account equity for each trade

5. Visualization:
   - Marks buy signals on the chart
   - Displays current take-profit and stop-loss levels for open positions

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/RSI-布林通道整合策略动态自适应的多指标交易系统-RSI-Bollinger-Bands-Integration-Strategy-A-Dynamic-Self-Adaptive-Multi-Indicator-Trading-System.md
