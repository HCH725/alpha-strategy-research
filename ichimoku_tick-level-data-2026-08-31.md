---
schema: strategy-research-record-v1
title: "Ichimoku Cloud Family Representative (Tick-level data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - ichimoku_tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/ICH云带扭转策略ICHIMOKU-KUMO-TWIST-STRATEGY.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Ichimoku Cloud Family Representative (Tick-level data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: ICH云带扭转策略ICHIMOKU-KUMO-TWIST-STRATEGY.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/ICH云带扭转策略ICHIMOKU-KUMO-TWIST-STRATEGY.md

## Economic mechanism
### Source-reported
> The Ichimoku Kumo Twist strategy utilizes the conversion line, baseline, and leading span lines of the Ichimoku indicator to construct trading signals as a trend following strategy. It identifies short-term and medium-term trend reversal points by watching for twists in the Ichimoku clouds to find lower risk breakout points and overbought/oversold opportunities. The strategy can be used for intraday trading as well as multi-week intermediate-term trading.

### Research interpretation
Ichimoku Cloud logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Tick-level data.

## Signal
> The strategy primarily uses three Ichimoku lines – the conversion line, baseline, and leading span 1, along with the high and low prices of the candlesticks to calculate the upper and lower cloud boundaries. The conversion line calculates the midpoint of the high and low over the past 9 candles, representing the short-term mean. The baseline calculates the midpoint of the high and low over the past 26 candles as the long-term mean. Leading span 1 is the average of the conversion and baseline lines. Leading span 2 is the midpoint price of the past 52 candles. 

Buy signals are generated when the leading span 1 crosses over leading span 2, while sell signals are generated when leading span 1 crosses under leading span 2. The trading strategy simply tracks the bullish and bearish crosses of the short and medium-term means to capture trend changes.

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/ICH云带扭转策略ICHIMOKU-KUMO-TWIST-STRATEGY.md
