---
schema: strategy-research-record-v1
title: "MACD Momentum Trend Family Representative (Heikin-Ashi candles
- Tick-level data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - macd_heikin-ashi-candles-tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动量均线交叉和MACD过滤的海肯阿什蜡烛策略Momentum-Crossover-Moving-Average-and-MACD-Filter-Heikin-Ashi-Candlestick-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MACD Momentum Trend Family Representative (Heikin-Ashi candles
- Tick-level data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 动量均线交叉和MACD过滤的海肯阿什蜡烛策略Momentum-Crossover-Moving-Average-and-MACD-Filter-Heikin-Ashi-Candlestick-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动量均线交叉和MACD过滤的海肯阿什蜡烛策略Momentum-Crossover-Moving-Average-and-MACD-Filter-Heikin-Ashi-Candlestick-Strategy.md

## Economic mechanism
### Source-reported
> This strategy utilizes the Heikin-Ashi candlestick technique combined with moving average crossover signals and MACD indicator for filtration to construct a trend-following strategy. The strategy can capture market trends in different timeframes, generating trading signals through moving average crossovers, and then filtering out false signals via the MACD indicator, demonstrating high profitability in backtests.

### Research interpretation
MACD Momentum Trend logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Heikin-Ashi candles
- Tick-level data.

## Signal
> 本策略主要运用三大技术指标:

1. 海肯阿什蜡烛技术。该技术通过修改收盘价构建出“无影线”的蜡烛线。这可以更清晰地表现出价格的真实趋势,过滤掉过多的市场噪音。

2. 指数移动均线(EMA)。快速EMA用于捕捉短期趋势,慢速EMA用于判断长期趋势方向。当快速EMA上穿慢速EMA时产生买入信号;当快速EMA下穿慢速EMA时产生卖出信号。

3. MACD指标。该指标结合快慢EMA,当MACD主线高于Signal线时为看涨信号,当主线低于Signal线时为看跌信号。

本策略的交易信号来自快速EMA和慢速EMA的金叉死叉。为了过滤假Signals,策略引入MACD指标进行辅助判断,只有当MACD指标发出同向信号时才会生成最终的交易信号,这大大降低了错误交易的概率。

具体来说,当快速EMA上穿慢速EMA(金叉)和MACD主线高于Signal线(看涨信号)同时出现时,产生买入信号;当快速EMA下穿慢速EMA(死叉)和MACD主线低于Signal线(看跌信号)同时出现时,产生卖出信号。

这种结合均线交叉和MACD指标的过滤方式,可以有效识别市场关键的转折点,顺势捕捉价格趋势。

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- Heikin-Ashi candles
- Tick-level data

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
- Tick-level data` and the detailed signal rules.
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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动量均线交叉和MACD过滤的海肯阿什蜡烛策略Momentum-Crossover-Moving-Average-and-MACD-Filter-Heikin-Ashi-Candlestick-Strategy.md
