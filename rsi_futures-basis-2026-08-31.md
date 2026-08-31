---
schema: strategy-research-record-v1
title: "RSI Based Mean Reversion Family Representative (Futures Basis)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - rsi_futures-basis
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/增强型布林带相对强弱指标交易策略-Enhanced-Bollinger-Bands-RSI-Trading-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RSI Based Mean Reversion Family Representative (Futures Basis)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 增强型布林带相对强弱指标交易策略-Enhanced-Bollinger-Bands-RSI-Trading-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/增强型布林带相对强弱指标交易策略-Enhanced-Bollinger-Bands-RSI-Trading-Strategy.md

## Economic mechanism
### Source-reported
> This strategy combines two technical indicators, Bollinger Bands and Relative Strength Index (RSI). It uses Bollinger Bands to capture the price fluctuation range and RSI to confirm the overbought and oversold status of the price, which serves as the basis for judging trading signals. When the price breaks through the lower band of Bollinger Bands and RSI is below 30, a long signal is generated; when the price breaks through the upper band and RSI is above 70, a short signal is generated.

####Strategy Principle
1. Calculate the upper, middle and lower bands of Bollinger Bands. The middle band is the simple moving average of the closing price, and the upper and lower bands are the middle band plus or minus a certain standard deviation.

2. Calculate the RSI indicator. RSI is used to measure the magnitude of price increases and decreases over a period of time to determine the overbought and oversold status of the price.

3. Generate trading signals. When the closing price breaks through the lower band of Bollinger Bands and RSI is below 30, a long signal is generated; when the closing price breaks through the upper band and RSI is above 70, a short signal is generated.

4. Execute trades. Set limit orders based on trading signals, short when breaking through the upper band of Bollinger Bands, and long when breaking through the lower band. At the same time, cancel the previous pending orders in the opposite direction.

####Advantage Analysis
1. Bollinger Bands can well quantify...

### Research interpretation
RSI Based Mean Reversion logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Futures Basis.

## Signal
> 1. 计算布林带上轨、中轨和下轨。中轨为收盘价的简单移动平均线,上下轨为中轨加减一定的标准差。

2. 计算RSI指标。RSI用于衡量一段时间内价格的涨跌幅度,以此判断价格的超买超卖状态。

3. 产生交易信号。当收盘价突破布林带下轨且RSI低于30时,产生做多信号;当收盘价突破布林带上轨且RSI高于70时,产生做空信号。

4. 执行交易。根据交易信号设置限价单,突破布林带上轨做空,下轨做多。同时,取消之前方向的挂单。

####优势分析
1. 布林带能够很好地量化价格的波动范围,RSI指标能够很好地量化价格的超买超卖程度,二者结合能够比较可靠地预测价格的反转时机。

2. 限价单的设置能够避免错误开仓或追高杀跌,止损单的设置能够控制风险。

3. 取消之前方向挂单的设置可防止策略过于频繁交易。

####风险分析
1. 趋势性行情下可能会出现较大回撤。布林带和RSI指标更适合用于判断震荡市的反转点,对于趋势行情的把握能力较弱。

2. 参数设置对策略表现影响较大。布林带的参数设置会影响到价格突破的频率,RSI指标的参数设置会影响到超买超卖信号的灵敏度,需要根据不同市场特点和交易周期进行优化。

####优化方向
1. 可以考虑增加趋势判断指标,如MAC 布林带和RSI指标结合趋势指标可进行多空仓位的自适应调整。D等,与

2. 可以考虑使用动态参数优化的方法,根据价格的波动率、趋势强度等特征,自适应调整布林带和RSI指标的参数,提高策略的适应性。

3. 可以在策略中加入资金管理和仓位管理模块,根据账户资金量、风险偏好、历史回撤等因素,动态调整每次交易的资金量和杠杆率。

####总结
该策略通过布林带和RSI指标的结合,可以比较有效地捕捉价格的超买超卖状态,并以此作为交易信号。但是,该策略在趋势性行情下表现可能欠佳,并且策略表现对参数设置较为敏感。未来可以考虑引入趋势判断、动态参数优化、资金管理等模块,以进一步提升策略的稳健性和盈利能力。

||

####Overview
This strategy combines two technical indicators, Bollinger Bands and Relative Strength Index (RSI). It uses Bollinger Bands to capture the price fluctuation range and RSI to confirm the overbought and oversold status of the price, which serves as the basis for judging trading signals. When the price breaks through the lower band of Bollinger Bands and RSI is below 30, a long signal is generated; when the price breaks through the upper band and RSI is above 70, a short signal is generated.

####Strategy Principle
1. Calculate the upper, middle and lower bands of Bollinger Bands. The middle band is the simple moving average of the closing price, and the upper and lower bands are the middle band plus or minus a certain standard deviation.

2. Calculate the RSI indicator. RSI is used to measure the magnitude of price increases and decreases over a period of time to determine the overbought and oversold status of the price.

3. Generate trading signals. When the closing price breaks through the lower band of Bollinger Bands and RSI is below 30, a long signal is generated; when the closing price breaks through the upper band and RSI ...

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/增强型布林带相对强弱指标交易策略-Enhanced-Bollinger-Bands-RSI-Trading-Strategy.md
