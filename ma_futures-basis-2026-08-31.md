---
schema: strategy-research-record-v1
title: "Moving Average Crossover/Trend Family Representative (Futures Basis)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - ma_futures-basis
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/EMA动态趋势追踪交易策略-EMA-Dynamic-Trend-Following-Trading-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Moving Average Crossover/Trend Family Representative (Futures Basis)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: EMA动态趋势追踪交易策略-EMA-Dynamic-Trend-Following-Trading-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/EMA动态趋势追踪交易策略-EMA-Dynamic-Trend-Following-Trading-Strategy.md

## Economic mechanism
### Source-reported
> This strategy uses technical indicators such as Exponential Moving Average (EMA), highest price, lowest price, and Average True Range (ATR) to identify the current trend direction by analyzing the relationship between price and EMA, highest price, and lowest price. It generates a buy signal when the price breaks above the lowest price and a sell signal when the price breaks below the highest price or reaches the dynamic resistance level, aiming to capture trend movements and achieve excess returns.

####Strategy Principle
1. Calculate ATR to measure market volatility and provide a basis for constructing dynamic channels.
2. Calculate the highest and lowest prices as the foundation for determining trend direction.
3. Calculate EMA_HL, which is the EMA of the highest and lowest prices, as the centerline of the dynamic channel.
4. Calculate EMA_HIGHEST and EMA_LOWEST by adding and subtracting a certain multiple of ATR from EMA_HL to obtain the upper and lower bands.
5. Calculate SELL_LINE by adding a certain multiple of ATR to the highest price to create a dynamic resistance level.
6. Generate a buy signal when EMA_LOWEST breaks above the lowest price and the closing price is below EMA_MID.
7. Generate a sell signal when EMA_HIGHEST breaks below the highest price and the closing price is above EMA_MID, or when the highest price reaches SELL_LINE.

####Strategy Advantages
1. Utilizes EMA, highest price, lowest price, and other indicators to comprehensively judge the trend, result...

### Research interpretation
Moving Average Crossover/Trend logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Futures Basis.

## Signal
> 1. 计算ATR,用于衡量市场波动率,为构建动态通道提供依据。
2. 计算最高价和最低价,作为判断趋势方向的基础。
3. 计算EMA_HL,即最高价和最低价的EMA,作为动态通道的中轴线。
4. 计算EMA_HIGHEST和EMA_LOWEST,即在EMA_HL的基础上加减ATR乘以一定比例得到的上下轨。
5. 计算SELL_LINE,即在最高价的基础上加上ATR乘以一定比例得到的动态阻力位。
6. 判断多头信号:当EMA_LOWEST向上突破最低价且收盘价低于EMA_MID时,产生买入信号。
7. 判断空头信号:当EMA_HIGHEST向下突破最高价且收盘价高于EMA_MID时,或者最高价触及SELL_LINE时,产生卖出信号。

####策略优势
1. 利用EMA、最高价、最低价等指标综合判断趋势,信号可靠性高。
2. 引入ATR作为波动率衡量标准,构建动态通道,适应不同市场状态。
3. 设置SELL_LINE动态阻力位,及时锁定利润,控制回撤风险。
4. 参数可调,适应不同品种和周期,具有一定的普适性和灵活性。

####策略风险
1. 趋势识别可能存在滞后,导致入场时机不够理想。
2. 参数设置不当可能导致信号频繁,增加交易成本。
3. 对于震荡市,策略表现可能不佳,需要结合其他方法判断。
4. 极端行情下,如快速变盘,策略可能失效,需要设置止损。

####策略优化方向
1. 引入更多指标,如成交量、波动率等,丰富趋势判断维度,提高信号可靠性。
2. 对参数进行优化,如ATR倍数、EMA周期等,找到最优参数组合,提高策略稳定性。
3. 加入仓位管理,如根据ATR动态调整仓位,控制单笔风险敞口。
4. 设置止损和止盈,控制单笔最大亏损和最大收益,提高风险收益比。
5. 结合其他策略,如突破策略、均值回归策略等,形成策略组合,提高整体稳健性。

####总结
该策略利用EMA、最高价、最低价等技术指标,结合ATR构建动态通道,通过突破最高价和最低价产生交易信号,以捕捉趋势行情,是一个简单实用的趋势追踪策略。策略参数可调,适应性和灵活性较好,但在震荡市表现可能欠佳,需要通过引入更多指标、优化参数、加入风控等方式进一步优化和改进。

||

####Overview
This strategy uses technical indicators such as Exponential Moving Average (EMA), highest price, lowest price, and Average True Range (ATR) to identify the current trend direction by analyzing the relationship between price and EMA, highest price, and lowest price. It generates a buy signal when the price breaks above the lowest price and a sell signal when the price breaks below the highest price or reaches the dynamic resistance level, aiming to capture trend movements and achieve excess returns.

####Strategy Principle
1. Calculate ATR to measure market volatility and provide a basis for constructing dynamic channels.
2. Calculate the highest and lowest prices as the foundation for determining trend direction.
3. Calculate EMA_HL, which is the EMA of the highest and lowest prices, as the centerline of the dynamic channel.
4. Calculate EMA_HIGHEST and EMA_LOWEST by adding and subtracting a certain multiple of ATR from EMA_HL to obtain the upper and lower bands.
5. Calculate SELL_LINE by adding a certain multiple of ATR to the highe...

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- Futures Basis

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
- Construct explicit PyBroker implementation honoring `Futures Basis` and the detailed signal rules.
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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/EMA动态趋势追踪交易策略-EMA-Dynamic-Trend-Following-Trading-Strategy.md
