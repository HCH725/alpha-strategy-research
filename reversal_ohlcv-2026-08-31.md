---
schema: strategy-research-record-v1
title: "Price Reversal Family Representative (OHLCV)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reversal_ohlcv
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多指标联动反转点捕捉交易策略-Multi-Indicator-Reversal-Point-Capture-Trading-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Price Reversal Family Representative (OHLCV)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 多指标联动反转点捕捉交易策略-Multi-Indicator-Reversal-Point-Capture-Trading-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多指标联动反转点捕捉交易策略-Multi-Indicator-Reversal-Point-Capture-Trading-Strategy.md

## Economic mechanism
### Source-reported
> The Multi-Indicator Reversal Point Capture Trading Strategy is a quantitative trading approach designed specifically to identify potential market reversal points. This strategy cleverly combines momentum indicators, volatility measures, and trend alignment filters through multi-layered technical analysis to identify both bullish and bearish reversal signals. The core principle requires multiple market conditions to be simultaneously satisfied before entering a trade, ensuring signal reliability. The strategy integrates RSI for divergence detection, Bollinger Bands for volatility measurement, ADX and DMI for trend strength confirmation, ATR for risk control, and Volume SMA for trade volume confirmation. Through this organic combination of indicators, the strategy can identify trading opportunities with statistical advantages across different market environments.

### Research interpretation
Price Reversal logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: OHLCV.

## Signal
> The strategy operates on a multidimensional market analysis framework, primarily through the collaborative work of these technical indicators:

1. RSI (Relative Strength Index): Set to an 8-period length, primarily used to detect divergences between price and momentum. When price makes a new low while RSI doesn't, it may indicate a bullish reversal; conversely, when price makes a new high while RSI doesn't, it may signal a bearish reversal.

2. Bollinger Bands (BB): Set to a 20-period length with a standard deviation multiplier of 2. Used to measure market volatility and identify statistically extreme price levels. Price breaking above the upper band or below the lower band may indicate trend changes.

3. ADX (Average Directional Index) and DMI (Directional Movement Index): Used to quantify trend strength, with an ADX threshold set at 20. Additional filters check the alignment of directional indicators (DI+ and DI-) to confirm trend direction.

4. ATR (Average True Range): Provides volatility measurement used to set stop-loss levels and determine risk through trailing stops.

5. Volume SMA (Simple Moving Average of Volume): Helps confirm signal strength by comparing current volume with a 20-period average.

Trade entry conditions are designed with strict requirements for multiple confirmations:

- Bullish Entry: Requires RSI divergence (price making a new low while RSI doesn't), price needs to be above the specified Bollinger Band level, volume and trend conditions must be met, and it must pass the risk-reward ratio test.

- Bearish Entry: Uses mirror logic of the bullish entry, checking for bearish divergence, ensuring price is below the appropriate Bollinger Band level, and confirming volume, trend strength, and risk-reward criteria.

Trade execution and exit strategy are equally well-designed:

- Dynamic Stop-Loss: Uses ATR value to dynamically set stop-loss positions.
- Trailing Stops: Implemented as a percentage of closing price (0.5%).
- Multiple Exit Conditio...

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- OHLCV

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
- Construct explicit PyBroker implementation honoring `OHLCV` and the detailed signal rules.
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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多指标联动反转点捕捉交易策略-Multi-Indicator-Reversal-Point-Capture-Trading-Strategy.md
