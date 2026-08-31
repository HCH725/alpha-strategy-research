---
schema: strategy-research-record-v1
title: "Genuine Arbitrage / Relative Value Family Representative (OHLCV)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - arbitrage_ohlcv
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于MACD柱色和线性回归的高频对冲策略High-Frequency-Hedging-Strategy-Based-on-MACD-Bar-Color-and-Linear-Regression.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Genuine Arbitrage / Relative Value Family Representative (OHLCV)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 基于MACD柱色和线性回归的高频对冲策略High-Frequency-Hedging-Strategy-Based-on-MACD-Bar-Color-and-Linear-Regression.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于MACD柱色和线性回归的高频对冲策略High-Frequency-Hedging-Strategy-Based-on-MACD-Bar-Color-and-Linear-Regression.md

## Economic mechanism
### Source-reported
> This strategy combines MACD bar color and linear regression indicators to achieve high-frequency reversal trading, which is especially suitable for short-term arbitrage and hedging. It belongs to a typical market-neutral strategy.

### Research interpretation
Genuine Arbitrage / Relative Value logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: OHLCV.

## Signal
> The strategy consists of the following main components:

1. MACD bar color as the trend judging indicator. When the MACD bar color is green, it indicates an upward trend, so no short orders should be placed. When the MACD bar is red, it indicates a downward trend, so no long orders should be placed.

2. Linear regression as the key trading signal indicator. Go long when price crosses above the linear regression line, and go short when price crosses below the line. 

3. PAC Channel formed by EMA of high, low and close prices to determine the direction of the linear regression line. Trading signals are only generated when the linear regression direction aligns with the channel trend.

4. EMA 89 as the stop loss line. Close positions when price crosses back above this line.

The logic for trade signals is:

Long signal: Linear regression crosses above PAC lower band AND linear regression is sloping up AND MACD bar is not red.

Short signal: Linear regression crosses below PAC upper band AND linear regression is sloping down AND MACD bar is not green.

Exit signal: Price crosses below EMA 89.

This strategy combines trend judgment and key price levels to achieve high frequency hedging trading.

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于MACD柱色和线性回归的高频对冲策略High-Frequency-Hedging-Strategy-Based-on-MACD-Bar-Color-and-Linear-Regression.md
