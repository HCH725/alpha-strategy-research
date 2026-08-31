---
schema: strategy-research-record-v1
title: "Supertrend Family Representative (Heikin-Ashi candles
- Tick-level data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - supertrend_heikin-ashi-candles-tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于Heikin-Ashi的超级趋势-trailing-stop损策略SuperTrend-Trailing-Stop-Strategy-Based-on-Heikin-Ashi.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Supertrend Family Representative (Heikin-Ashi candles
- Tick-level data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 基于Heikin-Ashi的超级趋势-trailing-stop损策略SuperTrend-Trailing-Stop-Strategy-Based-on-Heikin-Ashi.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于Heikin-Ashi的超级趋势-trailing-stop损策略SuperTrend-Trailing-Stop-Strategy-Based-on-Heikin-Ashi.md

## Economic mechanism
### Source-reported
> Underspecified in source.

### Research interpretation
Supertrend logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Heikin-Ashi candles
- Tick-level data.

## Signal
> 1. Calculate Heikin Ashi candlesticks: open, close, high, low prices.
2. Calculate SuperTrend indicator: upper band and lower band based on ATR and price.  
3. Determine the trend direction combining Heikin Ashi close and SuperTrend bands.
4. When Heikin Ashi close gets closer to SuperTrend upper band, it signals an uptrend; when Heikin Ashi close gets closer to SuperTrend lower band, it signals a downtrend.
5. Use SuperTrend upper band as trailing stop loss in uptrends, and lower band in downtrends.

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于Heikin-Ashi的超级趋势-trailing-stop损策略SuperTrend-Trailing-Stop-Strategy-Based-on-Heikin-Ashi.md
