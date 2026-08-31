---
schema: strategy-research-record-v1
title: "Bollinger Band Breakout/Reversion Family Representative (Tick-level data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bollinger_tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/趋势区间突破策略Trend-Breakout-Strategy-Based-on-Bollinger-Bands.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bollinger Band Breakout/Reversion Family Representative (Tick-level data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 趋势区间突破策略Trend-Breakout-Strategy-Based-on-Bollinger-Bands.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/趋势区间突破策略Trend-Breakout-Strategy-Based-on-Bollinger-Bands.md

## Economic mechanism
### Source-reported
> This is a trend following strategy based on Bollinger Bands. It uses Bollinger Bands to calculate price channels and combines candlestick patterns to determine trend direction. Long/short positions will be opened when price breaks out of the Bollinger Bands. This strategy works well for stocks with obvious trends and aims to capture mid-term trend profits.

### Research interpretation
Bollinger Band Breakout/Reversion logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Tick-level data.

## Signal
> This strategy uses the upper band, middle band and lower band of Bollinger Bands to determine price ranges. The upper and lower bands envelope price movements while the middle band is the moving average. Band width changes based on price volatility. When price breaks above the upper band, it signals an upward breakout and a long entry. When price breaks below the lower band, it signals a downward breakout and a short entry.

After determining trend direction with Bollinger Bands breakout, the strategy also confirms it with candlestick patterns. If the candle body aligns with the trend, such as bullish candle in an uptrend, a position will be opened. If the candle body shows reverse pattern, such as bearish candle in an uptrend, the signal will be ignored. This design aims to avoid false breakout risks. 

The detailed trading signals rules are:

1. Calculate upper band, middle band and lower band of Bollinger Bands to determine price range

2. When price breaks above upper band, it signals an upward/long trend

3. If the candlestick is bullish, confirm the trend and go long

4. When price breaks below lower band, it signals a downward/short trend

5. If the candlestick is bearish, confirm trend and go short 

6. Set stop loss and take profit based on percentage

By entering on Bollinger Bands breakouts and confirming with candlesticks, this strategy can effectively identify trend direction and get good entries during early trend stages. Profits are taken during mid-term trends.

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/趋势区间突破策略Trend-Breakout-Strategy-Based-on-Bollinger-Bands.md
