---
schema: strategy-research-record-v1
title: "Bollinger Band Breakout/Reversion Family Representative (Heikin-Ashi candles)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bollinger_heikin-ashi-candles
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于布林带突破的FiboBuLL波浪策略FiboBuLL-Wave-Strategy-Based-on-Bollinger-Bands-Breakout.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bollinger Band Breakout/Reversion Family Representative (Heikin-Ashi candles)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 基于布林带突破的FiboBuLL波浪策略FiboBuLL-Wave-Strategy-Based-on-Bollinger-Bands-Breakout.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于布林带突破的FiboBuLL波浪策略FiboBuLL-Wave-Strategy-Based-on-Bollinger-Bands-Breakout.md

## Economic mechanism
### Source-reported
> The FiboBuLL Wave strategy is adapted from the filter version of the Bollinger Bands study, which can be found under my scripts page. The strategy goes long when the price closes above the upper band and goes short when the price closes below the lower band.

Bollinger Bands is a classic indicator that uses a simple moving average of 20 periods, along with plots of upper and lower bands that are 2 standard deviations away from the middle band. These bands help visualize price volatility and trend based on where the price is relative to the bands.   

The strategy does not take into account any other parameters such as Volume / RSI / Fundamentals etc, so user must use discretion based on confirmations from other indicators or fundamentals. The strategy results are purely based on long and short trades and do not take into account any user defined targets or stop losses.

It works best when there is continuation the bar after price closes above/below upper/lower bands. It is definitely beneficial to use this strategy or the Bollinger Bands filter along with other indicators to get early glimpse of breach/fail of bands on candle close during BB squeeze or based on volatility.

The strategy can be used on Heikin Ashi candles for spotting trends but HA candles are not recommended for trade entries as they don't reflect true price of the asset.

### Research interpretation
Bollinger Band Breakout/Reversion logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Heikin-Ashi candles.

## Signal
> FiboBuLL波浪策略的核心原理是基于布林带指标判断价格的突破。布林带由中轨、上轨和下轨组成。中轨是收盘价的21周期简单移动平均线;上轨由中轨加上距离中轨上方1倍标准差计算得出,它反映了价格的上方波动范围;下轨由中轨减去距离中轨下方1倍标准差计算得出,反映价格下方波动范围。

当收盘价上穿上轨时产生做多信号;当收盘价下穿下轨时产生做空信号。做多做空后,再次突破相反轨道时平仓。

该策略使用barssince函数跟踪价格相对于上下轨的突破情况。当上轨突破的柱数小于下轨时产生做多信号,当下轨突破的柱数小于上轨柱数时产生做空信号。

通过调整中轨周期参数以及标准差倍数参数,可以改变布林带的突破灵敏度,从而调整入场时机。

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于布林带突破的FiboBuLL波浪策略FiboBuLL-Wave-Strategy-Based-on-Bollinger-Bands-Breakout.md
