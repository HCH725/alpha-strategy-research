---
schema: strategy-research-record-v1
title: "Momentum Family Representative (Tick-level data
- Futures Basis)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - momentum_futures-basis-tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于动能量化追趋策略Heiken-Ashi-Momentum-Quant-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Momentum Family Representative (Tick-level data
- Futures Basis)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 基于动能量化追趋策略Heiken-Ashi-Momentum-Quant-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于动能量化追趋策略Heiken-Ashi-Momentum-Quant-Strategy.md

## Economic mechanism
### Source-reported
> This strategy is based on the daily Heiken Ashi candlesticks, combined with momentum analysis across different timeframes, to dynamically determine the underlying support behind the current price and identify entry and exit points.

### Research interpretation
Momentum logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Tick-level data
- Futures Basis.

## Signal
> 1. Calculate the close prices of Heiken Ashi candlesticks across different timeframes, as the basis for subsequent momentum analysis.  

2. Calculate the percentage change between open prices and historical close prices over different periods, for both monthly and daily timeframes. This reflects the momentum strength behind the current price relative to historical levels.

3. Take the averages of the daily and monthly momentum fluctuations respectively. This filters out some noise and derives more stable momentum benchmarks.   

4. Based on the average momentum fluctuations, we can calculate the market support force truly reflected by the current price, i.e. the dynamic momentum threshold exclusive of market noise. 

5. When the close price breaks above momentum threshold, long positions are initiated on monthly basis. When price closes below threshold, positions are closed.

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- Tick-level data
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
- Construct explicit PyBroker implementation honoring `Tick-level data
- Futures Basis` and the detailed signal rules.
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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/基于动能量化追趋策略Heiken-Ashi-Momentum-Quant-Strategy.md
