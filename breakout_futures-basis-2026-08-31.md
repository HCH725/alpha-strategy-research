---
schema: strategy-research-record-v1
title: "Price Level Breakout Family Representative (Futures Basis)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - breakout_futures-basis
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/月度抛物线突破策略Monthly-Parabolic-Breakout-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Price Level Breakout Family Representative (Futures Basis)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 月度抛物线突破策略Monthly-Parabolic-Breakout-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/月度抛物线突破策略Monthly-Parabolic-Breakout-Strategy.md

## Economic mechanism
### Source-reported
> The Monthly Parabolic Breakout Strategy identifies strong buy signals when the RSI hits a 36-month high and one of two MACD signals also reaches a 36-month high. It is ideal for catching once-in-a-lifetime breakouts.

### Research interpretation
Price Level Breakout logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Futures Basis.

## Signal
> This strategy is mainly based on the RSI and MACD indicators. RSI is used to judge whether a stock is overbought or oversold. MACD is used to discover the momentum and strength of price changes.  

Specifically, the strategy first manually calculates the 14-day RSI. Then it calculates MACD1 as the difference between 4-day and 9-day EMAs, and MACD2 as the difference between 12-day and 26-day EMAs.

On this basis, it records the highest values of RSI, MACD1 and MACD2 in the last 36 months. When this month's RSI exceeds the 36-month high, and either MACD1 or MACD2 also exceeds its 36-month high, a strong buy signal is generated.  

This signal combines the new high judgments of RSI and MACD over different time periods. It can effectively identify great buying opportunities in the rare major trends, capturing such chances.

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/月度抛物线突破策略Monthly-Parabolic-Breakout-Strategy.md
