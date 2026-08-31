---
schema: strategy-research-record-v1
title: "Stochastic RSI (Renko) Family Representative"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - stochastic-rsi-renko_renko-charts
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/K线Stochastic-RSI交易策略Renko-Stochastic-RSI-Trading-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Stochastic RSI (Renko) Family Representative

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: K线Stochastic-RSI交易策略Renko-Stochastic-RSI-Trading-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/K线Stochastic-RSI交易策略Renko-Stochastic-RSI-Trading-Strategy.md

## Economic mechanism
### Source-reported
> This is a Stochastic RSI trading strategy designed for use on Renko charts. It generates buy and sell signals using the crossover and crossunder of Stochastic RSI K and D lines. The strategy is specialized for Renko charts and can effectively filter market noise and identify trends.

### Research interpretation
Stochastic RSI (Renko) logic. Explicit Renko Stochastic RSI strategy. Data dependency: Renko charts

## Signal
> The trading signals are primarily based on the Stochastic RSI indicator, which combines the advantages of RSI and Stochastic oscillator.

First, the RSI value over a period is calculated, then Stochastic RSI is computed based on the RSI values. Stochastic RSI contains two lines:

- K line: Moving average of RSI values over a period, represents the fast Stochastic RSI line

- D line: Moving average of the K line, represents the slow Stochastic RSI line

When K line crosses above D line, a buy signal is generated. When K line crosses below D line, a sell signal is generated.

In addition, this strategy is only applied on Renko charts, which filters market noise by constructing bars based on price change threshold, identifying trend direction.

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- Renko charts

## Execution assumptions
- Signal-to-fill timing: underspecified; implementation must choose and test a causal execution convention.
- Fees/slippage/latency: underspecified; standard institutional assumptions must be supplied.

## Evidence
### Source-reported
Source claims vary by variant. Not independently reproduced.

### Independently reproduced
Not independently reproduced.

### Negative evidence
None identified in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan
- Construct explicit PyBroker implementation honoring `Renko charts` and the detailed signal rules.
- Test out-of-sample against structurally relevant assets.
- For hybrid candidates: isolate components via ablation to verify standalone predictive power of the core indicator.

## Crypto portability
direct

## Limitations
- underspecified parameter robustness
- not independently reproduced
- leakage/repainting risk: manual semantic review required for hidden repainting in original source code.

## Implementation status
not-implemented

## Adoption boundary
This is research material only. Not approved for trading.

## Related Wiki records
None

## Sources
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/K线Stochastic-RSI交易策略Renko-Stochastic-RSI-Trading-Strategy.md
