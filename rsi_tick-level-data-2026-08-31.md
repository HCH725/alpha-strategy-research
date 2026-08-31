---
schema: strategy-research-record-v1
title: "RSI Based Mean Reversion Family Representative (Tick-level data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - rsi_tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于DMI和RSI的趋势跟随策略Trend-Following-Strategy-Based-on-DMI-and-RSI.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RSI Based Mean Reversion Family Representative (Tick-level data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 基于DMI和RSI的趋势跟随策略Trend-Following-Strategy-Based-on-DMI-and-RSI.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于DMI和RSI的趋势跟随策略Trend-Following-Strategy-Based-on-DMI-and-RSI.md

## Economic mechanism
### Source-reported
> This strategy combines the DMI indicator to determine the trend direction and the RSI indicator to determine overbought and oversold conditions, implementing a relatively complete trend following trading strategy. When the DMI indicator judges that a trend appears and the RSI indicator shows overbought or oversold, long or short positions are taken accordingly. At the same time, a moving stop loss is set to lock in profits.

##Strategy Logic  
1. Use DMI indicator to judge trend direction
   - DMI consists of three lines: +DI indicates uptrend, -DI indicates downtrend, ADX judges strength of the trend  
   - When +DI>-DI, it is an uptrend, go long; when -DI>+DI, it is a downtrend, go short
2. Use RSI indicator to judge overbought and oversold
   - RSI compares average gain and loss over a period to determine overbought or oversold
   - RSI below 30 is oversold, above 70 is overbought
3. Combining DMI to determine trend direction and RSI for overbought/oversold can better capture market rhythm
   - When DMI shows uptrend and RSI oversold, good timing for long
   - When DMI shows downtrend and RSI overbought, good timing for short
4. Set moving stop loss to lock in profits  

##Advantage Analysis 
This is a relatively mature and steady trend following strategy with the following strengths:
1. Combining trend and overbought/oversold avoids frequent trading in range-bound market
2. Popular indicators DMI and RSI with easy parameter tuning and thorough practical verification
3. Tr...

### Research interpretation
RSI Based Mean Reversion logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Tick-level data.

## Signal
> 1. 使用DMI指标判断趋势方向
   - DMI由三条曲线组成:+DI表示上升趋势,-DI表示下降趋势,ADX判断趋势的力度
   - 当+DI>-DI时为上升趋势,做多;当-DI>+DI时为下降趋势,做空
2. 使用RSI指标判断超买超卖
   - RSI通过比较一段时期内的平均收盘涨幅和跌幅来判断是否超买或超卖
   - RSI低于30为超卖,高于70为超买
3. 结合DMI判断趋势方向和RSI判断超买超卖,可以较好地把握市场节奏
   - DMI判断有上升趋势且RSI超卖时,为较好的做多时机
   - DMI判断有下降趋势且RSI超买时,为较好的做空时机
4. 设置移动止损来锁定利润

##优势分析
这是一个较为成熟稳定的趋势跟随策略,具有以下优势:
1. 结合趋势判断和超买超卖判断,避免在震荡市中频繁交易
2. 使用流行指标DMI和RSI,参数选择容易,实践验证充分
3. 设置移动止损来锁定利润,可以一定程度避免止损
4. 规则清晰易懂,程序实现简单,容易实践

##风险分析
该策略也存在一些风险需要注意:
1. DMI和RSI都容易产生假信号,可能会导致不必要的亏损
2. 移动止损设置不当可能会过早止损或止损幅度太大
3. 无法有效过滤震荡行情,容易被套住
4. 跟随趋势策略,在趋势反转时无法及时止损

##优化方向
该策略还可以从以下几个方面进行优化:
1. 结合波动率指标过滤震荡行情
2. 结合 candle 形态判断,避免假突破
3. 在关键支撑阻力位置附近设置适当止损限制亏损
4. 增加机器学习模型判断趋势ython
5. 动态优化DMI和RSI的参数

##总结
本策略整体是一个较为稳定实用的趋势跟随策略,通过DMI判断趋势方向,RSI判断超买超卖,从而把握住中长线的交易机会。同时设置移动止损来锁定利润。该策略参数选择简单,交易规则清晰,容易实践。但也存在被套和止损不够及时的风险。通过一些参数和模型优化,可以使该策略的效果更好。

|| 

##Overview
This strategy combines the DMI indicator to determine the trend direction and the RSI indicator to determine overbought and oversold conditions, implementing a relatively complete trend following trading strategy. When the DMI indicator judges that a trend appears and the RSI indicator shows overbought or oversold, long or short positions are taken accordingly. At the same time, a moving stop loss is set to lock in profits.

##Strategy Logic  
1. Use DMI indicator to judge trend direction
   - DMI consists of three lines: +DI indicates uptrend, -DI indicates downtrend, ADX judges strength of the trend  
   - When +DI>-DI, it is an uptrend, go long; when -DI>+DI, it is a downtrend, go short
2. Use RSI indicator to judge overbought and oversold
   - RSI compares average gain and loss over a period to determine overbought or oversold
   - RSI below 30 is oversold, above 70 is overbought
3. Combining DMI to determine trend direction and RSI for overbought/oversold can better capture market rhythm
   - When DMI shows uptrend and RSI oversold, good timing for long
   - When DMI shows downtrend and RSI overbought, good timing for sh...

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
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
- Construct explicit PyBroker implementation honoring `Tick-level data` and the detailed signal rules.
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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于DMI和RSI的趋势跟随策略Trend-Following-Strategy-Based-on-DMI-and-RSI.md
