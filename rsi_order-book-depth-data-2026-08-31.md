---
schema: strategy-research-record-v1
title: "RSI Based Mean Reversion Family Representative (Order book / Depth data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - rsi_order-book-depth-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多时间周期RSI-SMA动态交叉自适应交易系统-Multi-Timeframe-RSI-SMA-Dynamic-Crossover-Adaptive-Trading-System.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RSI Based Mean Reversion Family Representative (Order book / Depth data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 多时间周期RSI-SMA动态交叉自适应交易系统-Multi-Timeframe-RSI-SMA-Dynamic-Crossover-Adaptive-Trading-System.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多时间周期RSI-SMA动态交叉自适应交易系统-Multi-Timeframe-RSI-SMA-Dynamic-Crossover-Adaptive-Trading-System.md

## Economic mechanism
### Source-reported
> The Multi-Timeframe RSI-SMA Dynamic Crossover Adaptive Trading System is an advanced quantitative trading strategy that combines Relative Strength Index (RSI) and Simple Moving Average (SMA) crossover signals. What makes this strategy unique is its ability to automatically adjust indicator parameters, risk levels, and filtering conditions according to different timeframes (from 1-minute to monthly charts), achieving cross-timeframe trading adaptability. Through in-depth analysis of the Pine Script code, it's evident that the strategy employs an intelligent parameter adjustment mechanism that automatically optimizes RSI periods, SMA periods, ATR multipliers, take-profit percentages, and volume requirements across different timeframes, thereby maintaining consistent performance in short-term, medium-term, and long-term trading.

### Research interpretation
RSI Based Mean Reversion logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Order book / Depth data.

## Signal
> 该策略的核心原理是基于RSI与其SMA均线的交叉信号,结合了多重确认过滤条件和动态风险管理系统。具体运作原理如下:

1. **智能参数自适应**: 策略通过`timeframe.period`函数检测当前图表时间周期,然后使用switch结构为各项指标分配最优参数。例如,RSI周期从1分钟图表的10期扩展到月线图表的28期;SMA周期从20期到200期不等;ATR乘数从1.5倍增加到4.5倍;止盈目标从3%增加到10%。

2. **动态指标计算**: 
   - 自适应RSI-SMA: 使用优化后的周期计算RSI值和RSI的SMA均线
   - 智能成交量过滤: 根据时间周期调整成交量要求,1分钟图要求成交量为20期平均的2倍,而月线图则仅要求0.5倍
   - 趋势确认: 使用快速EMA和慢速EMA的交叉来确认上升趋势,确保顺势而为

3. **入场条件**: 
   - RSI上穿其SMA均线
   - 成交量大于动态阈值
   - 确认上升趋势(快速EMA > 慢速EMA)
   - 收盘价大于开盘价(看涨蜡烛)
   - 收盘价突破5周期高点

4. **退出条件**: 
   - RSI下穿其SMA均线
   - 价格跌破5周期低点

5. **风险管理**: 
   - 动态止损: 基于ATR的倍数设置(从1.5倍到4.5倍),适应不同时间周期的波动特性
   - 动态止盈: 基于入场点设置3%到10%的百分比目标,随时间周期扩大

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- Order book / Depth data

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
- Construct explicit PyBroker implementation honoring `Order book / Depth data` and the detailed signal rules.
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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多时间周期RSI-SMA动态交叉自适应交易系统-Multi-Timeframe-RSI-SMA-Dynamic-Crossover-Adaptive-Trading-System.md
