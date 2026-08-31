---
schema: strategy-research-record-v1
title: "Moving Average Crossover/Trend Family Representative (Renko charts
- Tick-level data
- Futures Basis)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - ma_futures-basis-renko-charts-tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/久期均线交叉Renko策略Long-term-Moving-Average-Crossover-Renko-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Moving Average Crossover/Trend Family Representative (Renko charts
- Tick-level data
- Futures Basis)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 久期均线交叉Renko策略Long-term-Moving-Average-Crossover-Renko-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/久期均线交叉Renko策略Long-term-Moving-Average-Crossover-Renko-Strategy.md

## Economic mechanism
### Source-reported
> This strategy is a moving average crossover strategy based on Renko candlestick charts. It uses the TEMA indicator to construct crossover signals and combines long-term moving averages for filtering, aiming to identify trends on Renko charts and generate buy and sell signals.

### Research interpretation
Moving Average Crossover/Trend logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Renko charts
- Tick-level data
- Futures Basis.

## Signal
> The main signal source of this strategy comes from the golden cross and death cross of the short-term TEMA indicator and SMA indicator. Specifically, the logic is:

When the short-term TEMA crosses over the short-term SMA, go long; when the short-term TEMA crosses below the short-term SMA, close positions.

In addition, the strategy also sets two optional parameters avg_protection and gain_protection to adjust the entry and stop loss logic:

- When avg_protection>0, only buy when the close price is lower than the current average holding price, which can reduce the cost basis;

- When gain_protection>0, only sell when the close price exceeds the entry price by a certain percentage to lock in profits.

Finally, the strategy also uses a long-term SMMA indicator as a trend filter. Only when the close price is below SMMA will a long signal be triggered.

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- Renko charts
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
- Construct explicit PyBroker implementation honoring `Renko charts
- Tick-level data
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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/久期均线交叉Renko策略Long-term-Moving-Average-Crossover-Renko-Strategy.md
