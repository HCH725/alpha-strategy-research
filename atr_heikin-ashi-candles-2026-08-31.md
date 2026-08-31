---
schema: strategy-research-record-v1
title: "ATR Volatility Family Representative (Heikin-Ashi candles)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - atr_heikin-ashi-candles
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动态ATR追踪止损交易策略市场波动性自适应系统-Dynamic-ATR-Trailing-Stop-Trading-Strategy-Market-Volatility-Adaptive-System.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ATR Volatility Family Representative (Heikin-Ashi candles)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 动态ATR追踪止损交易策略市场波动性自适应系统-Dynamic-ATR-Trailing-Stop-Trading-Strategy-Market-Volatility-Adaptive-System.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动态ATR追踪止损交易策略市场波动性自适应系统-Dynamic-ATR-Trailing-Stop-Trading-Strategy-Market-Volatility-Adaptive-System.md

## Economic mechanism
### Source-reported
> The Dynamic ATR Trailing Stop Trading Strategy is a quantitative trading system based on the Average True Range (ATR) indicator. The core of this strategy lies in utilizing market volatility to dynamically calculate a trailing stop line, thereby capturing price trend changes and automatically executing buy and sell operations. This strategy generates buy signals when price breaks above the trailing stop line and sell signals when price falls below the trailing stop line, while automatically closing positions during trend reversals to protect existing profits and control risk. The system also provides an intuitive graphical interface and automated alert functionality to help traders better monitor market dynamics.

### Research interpretation
ATR Volatility logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Heikin-Ashi candles.

## Signal
> 该策略的核心原理基于使用ATR指标动态计算追踪止损水平。策略实现主要包括以下几个关键部分：

1. **动态追踪止损计算**：
   - 使用ATR指标测量市场波动性：`xATR = ta.atr(c)`，其中c为ATR计算周期
   - 通过感应参数a调整止损距离：`nLoss = a * xATR`
   - 根据价格位置动态调整追踪止损线：`xATRTrailingStop := src > nz(xATRTrailingStop[1], 0) ? src - nLoss : src + nLoss`，这意味着在上升趋势中，止损线会跟随价格上移，但保持一定距离；在下降趋势中则相反

2. **信号生成逻辑**：
   - 买入信号：当价格向上突破追踪止损线时 `buyCondition = ta.crossover(src, xATRTrailingStop)`
   - 卖出信号：当价格向下跌破追踪止损线时 `sellCondition = ta.crossunder(src, xATRTrailingStop)`

3. **仓位管理**：
   - 买入信号触发时，先关闭所有卖出仓位，然后开立新的买入仓位
   - 卖出信号触发时，先关闭所有买入仓位，然后开立新的卖出仓位
   - 价格与追踪止损线交叉时自动平仓，防止大幅度的市场反转造成损失

4. **图形显示**：
   - 蓝色线显示追踪止损水平
   - 绿色标记表示买入信号，红色标记表示卖出信号
   - 根据价格与追踪止损线的位置关系，K线颜色动态调整为绿色(上升趋势)或红色(下降趋势)

5. **自定义参数**：
   - 感应参数a：控制追踪止损线的敏感度，值越小越敏感
   - ATR周期c：控制ATR计算的时间窗口
   - 平滑选项h：可选择使用平滑K线(Heikin Ashi)计算信号

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
- None explicitly detected in structural scan; manual semantic review required for hidden repainting.

## Implementation status
not-implemented

## Adoption boundary
This is research material only. Not approved for trading.

## Related Wiki records
None

## Sources
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动态ATR追踪止损交易策略市场波动性自适应系统-Dynamic-ATR-Trailing-Stop-Trading-Strategy-Market-Volatility-Adaptive-System.md
