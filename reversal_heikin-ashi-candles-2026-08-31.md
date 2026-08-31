---
schema: strategy-research-record-v1
title: "Price Reversal Family Representative (Heikin-Ashi candles)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reversal_heikin-ashi-candles
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多指标组合趋势反转策略Multi-Indicator-Trend-Reversal-Trading-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Price Reversal Family Representative (Heikin-Ashi candles)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 多指标组合趋势反转策略Multi-Indicator-Trend-Reversal-Trading-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多指标组合趋势反转策略Multi-Indicator-Trend-Reversal-Trading-Strategy.md

## Economic mechanism
### Source-reported
> 这是一个利用多个指标进行组合,识别价格趋势反转点的策略。基本思路是,单一指标很难完美识别趋势的转折点,因此选取多个具有类似功能的指标进行组合,当多个指标发出同向信号时,我们就可以相对确定趋势发生反转的高概率情况,从而进行交易操作。

### Research interpretation
Price Reversal logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Heikin-Ashi candles.

## Signal
> The strategy selects 5 different indicators for combination. These 5 indicators all have the ability to judge price trends. They are:  

1. Coral Trend Indicator: Uses a combination of triple or higher order exponential smoothing moving averages to determine price trends
2. SSL Channel: Combines moving averages to determine price channels and trends  
3. Heikin Ashi RSI: Combines RSI indicator with intraday averages to determine trends
4. MACD DEMA: Combines double exponential moving averages and MACD to determine trends  
5. WaveTrend Oscillator: Determines trends according to price channels

The trading logic of the strategy is that of the above 5 indicators, any 1 or more can be selected for combination. Only when multiple selected indicators give buy/sell signals simultaneously on a bar, will we open long/short positions accordingly.  

For example, if we select 2 indicators: Coral Trend and SSL Channel. We will only go long when both of them give buy signals at the same time; and only go short when both of them give sell signals at the same time.  

Through such multi-indicator verification, the reliability of trading signals can be greatly improved and avoid misleading by individual indicators.

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多指标组合趋势反转策略Multi-Indicator-Trend-Reversal-Trading-Strategy.md
