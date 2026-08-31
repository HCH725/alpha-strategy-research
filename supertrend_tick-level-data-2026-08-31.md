---
schema: strategy-research-record-v1
title: "Supertrend Family Representative (Tick-level data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - supertrend_tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/阳光超级趋势策略Sunny-Supertrend-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Supertrend Family Representative (Tick-level data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 阳光超级趋势策略Sunny-Supertrend-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/阳光超级趋势策略Sunny-Supertrend-Strategy.md

## Economic mechanism
### Source-reported
> The Sunny Supertrend strategy is a trend-following strategy based on the ATR and SuperTrend indicators. It can accurately predict trend reversals and works perfectly as a timing indicator. The strategy can increase patience and help traders enter and exit the markets at the right time.

### Research interpretation
Supertrend logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Tick-level data.

## Signal
> The strategy uses the SuperTrend indicator to determine the current trend direction. When the SuperTrend indicator changes direction, we think a trend reversal may occur. In addition, the strategy also uses the direction of candlestick bodies for auxiliary judgment. When a potential reversal signal appears and the candlestick body direction is consistent with the previous one, the invalid signal is filtered out.

Specifically, the strategy generates trading signals according to the following logic:

1. Use the SuperTrend indicator to determine the main trend direction  
2. When the SuperTrend indicator direction changes, a potential reversal signal is generated
3. If the candlestick body direction is consistent with the previous one at this time, the reversal signal is filtered out
4. If the candlestick body direction changes, the reversal signal is confirmed and a trading signal is generated

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/阳光超级趋势策略Sunny-Supertrend-Strategy.md
