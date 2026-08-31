---
schema: strategy-research-record-v1
title: "Price Reversal Family Representative (Futures Basis)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reversal_futures-basis
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动态Keltner通道动量反转策略-Dynamic-Keltner-Channel-Momentum-Reversal-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Price Reversal Family Representative (Futures Basis)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 动态Keltner通道动量反转策略-Dynamic-Keltner-Channel-Momentum-Reversal-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动态Keltner通道动量反转策略-Dynamic-Keltner-Channel-Momentum-Reversal-Strategy.md

## Economic mechanism
### Source-reported
> The Dynamic Keltner Channel Momentum Reversal Strategy is a sophisticated trading system that combines multiple technical indicators. This strategy primarily utilizes Keltner Channels, Exponential Moving Average (EMA), and Average True Range (ATR) to identify potential entry and exit points in the market. Its core idea is to capture momentum moves after a market pullback while incorporating trend-following elements.

The main components of the strategy include:
1. Keltner Channels: Used to identify overbought and oversold conditions.
2. Exponential Moving Average (EMA): Serves as a trend filter.
3. Average True Range (ATR): Employed for dynamic stop-loss placement.

The strategy's entry conditions are carefully designed, requiring the price to touch the outer band of the Keltner Channel, then pull back to the middle band, with the closing price above or below the EMA. This design aims to capture potential reversals or trend continuations after significant market movements.

Exit conditions are also based on the Keltner Channels, with the strategy automatically closing positions when the price reaches or exceeds the respective channel boundaries. Additionally, the strategy employs a dynamic stop-loss mechanism based on ATR, providing flexibility and adaptability to risk management.

### Research interpretation
Price Reversal logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Futures Basis.

## Signal
> The core principles of the Dynamic Keltner Channel Momentum Reversal Strategy can be broken down into the following key components:

1. Keltner Channel Setup:
   The strategy uses a 20-period Simple Moving Average (SMA) as the basis for the Keltner Channel, with the channel width set to 6 times the ATR. This setup allows the channel to dynamically adapt to changes in market volatility.

2. Trend Filtering:
   A 280-period EMA is used as a long-term trend indicator. This helps ensure that trade direction aligns with the overall market trend.

3. Entry Conditions:
   - Long Entry: Requires the upper band to be touched within the past 120 periods, the current candle's wick to touch the middle band, and the closing price to be above the EMA.
   - Short Entry: Requires the lower band to be touched within the past 120 periods, the current candle's wick to touch the middle band, and the closing price to be below the EMA.

4. Exit Conditions:
   - Long Exit: When the high price reaches or exceeds the upper band.
   - Short Exit: When the low price reaches or falls below the lower band.

5. Risk Management:
   Uses a 35-period ATR to calculate dynamic stop-losses, with the stop distance set to 5.5 times the ATR. This method automatically adjusts stop levels based on market volatility.

The strategy's design philosophy is to look for potential reversal or trend continuation opportunities after significant market movements (touching the outer Keltner Channel band). The middle band touch requirement helps confirm price pullbacks, while the EMA ensures trade direction aligns with the overall trend.

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/动态Keltner通道动量反转策略-Dynamic-Keltner-Channel-Momentum-Reversal-Strategy.md
