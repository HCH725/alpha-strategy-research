---
schema: strategy-research-record-v1
title: "Price Level Breakout Family Representative (Heikin-Ashi candles
- Tick-level data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - breakout_heikin-ashi-candles-tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/三次蜡烛突破动量平滑平均交易策略-Triple-Candle-Breakout-Momentum-Heikin-Ashi-Trading-System.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Price Level Breakout Family Representative (Heikin-Ashi candles
- Tick-level data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 三次蜡烛突破动量平滑平均交易策略-Triple-Candle-Breakout-Momentum-Heikin-Ashi-Trading-System.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/三次蜡烛突破动量平滑平均交易策略-Triple-Candle-Breakout-Momentum-Heikin-Ashi-Trading-System.md

## Economic mechanism
### Source-reported
> The Triple Candle Breakout Momentum Heikin-Ashi Trading System is a trend-following strategy based on Heikin-Ashi candlestick charts that identifies consecutive market trends and enters trades after momentum confirmation. The core concept involves observing three consecutive Heikin-Ashi candles of the same color, waiting for a reversal candle to appear, and then entering the market when price breaks through the high or low of that reversal candle. This approach aims to capture momentum breakouts following trend reversals, improving entry timing precision and reducing false signals. The strategy is particularly effective for medium to long-term trend following, as it uses Heikin-Ashi candles to smooth price data, filter market noise, and incorporates strict entry and exit conditions to ensure reliable trading signals.

### Research interpretation
Price Level Breakout logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Heikin-Ashi candles
- Tick-level data.

## Signal
> The core of this strategy is the Heikin-Ashi candlestick technique, a modified candlestick chart originating from Japan that smooths price fluctuations by calculating averages of open, close, high, and low prices. Unlike traditional candlesticks, Heikin-Ashi candles more clearly display trend direction while reducing the impact of market noise.

The strategy operates as follows:

1. **Calculating Heikin-Ashi Values**:
   - HA Close = (Open + High + Low + Close) / 4
   - HA Open = (Previous HA Open + Previous HA Close) / 2
   - HA High = Maximum value among High, HA Open, and HA Close
   - HA Low = Minimum value among Low, HA Open, and HA Close

2. **Long Entry Logic**:
   - Identify three consecutive red (bearish) HA candles, followed by a green (bullish) candle
   - Record the high of this green candle
   - Trigger a long entry signal when the next candle breaks above the high of that green candle

3. **Long Exit Logic**:
   - After a long entry, wait for the first red HA candle to form
   - Record the low of this red candle
   - Trigger a long exit signal when price breaks below the low of that red candle

4. **Short Entry Logic**:
   - Identify three consecutive green (bullish) HA candles, followed by a red (bearish) candle
   - Record the low of this red candle
   - Trigger a short entry signal when the next candle breaks below the low of that red candle

5. **Short Exit Logic**:
   - After a short entry, wait for the first green HA candle to form
   - Record the high of this green candle
   - Trigger a short exit signal when price breaks above the high of that green candle

This design ensures that traders only enter the market after confirming trend momentum, increasing the probability of successful trades.

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/三次蜡烛突破动量平滑平均交易策略-Triple-Candle-Breakout-Momentum-Heikin-Ashi-Trading-System.md
