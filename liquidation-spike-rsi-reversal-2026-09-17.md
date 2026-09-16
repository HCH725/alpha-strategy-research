---
schema: strategy-research-record-v1
title: Liquidation-Spike RSI Reversal
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-17
sources:
  - https://www.tradingview.com/script/Aef557RY-Liquidation-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Liquidation-Spike RSI Reversal

## Provenance

Public TradingView open-source strategy page, **Liquidation Strategy**, author/page identity `llbot`, published 2025-09-13. Stable source: https://www.tradingview.com/script/Aef557RY-Liquidation-Strategy/ . Source reviewed as of 2026-09-17. The source requires TradingView's Liquidations indicator and states that liquidation data should be linked from Bybit or OKX charts.

## Economic mechanism

### Source-reported

The author describes a crypto strategy that enters around extreme liquidation events. A long is triggered when the linked long-liquidation series spikes above a configured positive threshold; a short is triggered when the linked short-liquidation series falls below a configured negative threshold. An optional EMA-multiplier filter can require the liquidation observation to be extreme relative to its moving-average baseline. Trade exits are governed by RSI crossing its smoothed series.

### Research interpretation

The falsifiable hypothesis is **forced-flow exhaustion / post-liquidation reversal**: an unusually large liquidation event may represent price-insensitive forced execution that temporarily pushes price away from a short-horizon equilibrium; once the forced flow is exhausted, price may mean-revert. The liquidation threshold is the primary event signal. The optional EMA-relative test is an event-severity filter. RSI/smoothed-RSI crossover is exit timing, not independent evidence that liquidation events contain alpha.

The source's directional labels deserve empirical scrutiny: the page states long entries follow spikes in the `long liquidation` input and short entries follow negative `short liquidation` observations. Whether those series/sign conventions correspond to economically sensible reversal direction depends on the exact TradingView Liquidations data semantics and must be verified point-in-time rather than inferred from the labels.

## Signal

**Source-reported normalized rule:**

- Formation: evaluate linked liquidation series on chart observations; exact intrabar versus confirmed-bar evaluation is **underspecified** on the public page.
- Long entry: long-liquidation input exceeds a user-set positive threshold.
- Short entry: short-liquidation input is below a user-set negative threshold.
- Optional filter: compare liquidation magnitude with an EMA-derived threshold/multiplier; exact EMA length and multiplier defaults are **underspecified** on the public description.
- Long exit: RSI crosses below its smoothed version.
- Short exit: RSI crosses above its smoothed version.
- Holding period: event-driven until the corresponding RSI exit; no fixed holding period is stated.
- Re-entry/pyramiding behavior: **underspecified**.
- Liquidation threshold defaults, RSI length, RSI smoothing method/length, and precise order timing are **underspecified** in the public description.

No missing parameter is promoted here into a source-reported fact.

## Required data

- Crypto instrument with compatible liquidation data.
- Source specifically directs users to Bybit or OKX charts.
- TradingView Liquidations indicator outputs for long and short liquidation series, linked into the strategy inputs.
- Price OHLC required for RSI and order evaluation; volume is not stated as a required signal input.
- Chart timeframe: **underspecified**.
- Liquidation-event timestamp and price-bar timestamp must be aligned point-in-time; availability latency and historical revisions must be tested rather than assumed.
- Missing liquidation observations and exchange outages: source handling is **underspecified**.

## Execution assumptions

The public page does not specify a realistic execution model. Same-bar versus next-bar fill, order type, spread, slippage, fees, market impact, funding, leverage, margin, liquidation risk of the strategy itself, latency, and partial-fill handling are **underspecified**.

A future test must prevent look-ahead by establishing when the liquidation observation becomes available relative to the executable price. Liquidation spikes can coincide with stressed spreads and discontinuous price moves, so zero-cost or frictionless fills would be especially weak assumptions for this hypothesis.

## Evidence

### Source-reported

The reviewed TradingView page describes the strategy logic and required Bybit/OKX liquidation inputs. No independently verified performance statistic is recorded here. Any TradingView Strategy Tester output visible interactively is not treated as evidence unless its sample, settings, costs, and exact figure are traceably captured.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No explicit negative empirical result was identified on the reviewed source page; absence is not evidence of no negative result. The source leaves important execution and parameter details underspecified, and liquidation-event trading is plausibly highly sensitive to data semantics, latency, spread and slippage.

## Falsification plan

1. Reconstruct the exact TradingView liquidation-series semantics and verify the long/short sign convention before testing returns.
2. Use point-in-time Bybit/OKX liquidation observations with synchronized executable OHLC data; reject any implementation that uses future-complete event data.
3. Event-study forward returns after liquidation spikes across multiple normalized severity buckets (absolute threshold and EMA-relative/z-score alternatives) and horizons before accepting the author's directional mapping.
4. Compare the source-style rule against controls: unconditional entries, matched high-volatility bars without liquidation spikes, liquidation spike alone, EMA-relative severity alone, and the full entry-plus-RSI-exit rule.
5. Separate long-liquidation and short-liquidation events and test both continuation and reversal directions. This directly falsifies a potentially incorrect sign interpretation.
6. Require chronological out-of-sample evaluation across BTC/ETH and additional liquid perpetuals, multiple volatility regimes, and both Bybit and OKX where comparable data exist.
7. Stress fees, spread, latency and slippage aggressively around liquidation events. If apparent edge disappears under plausible stressed execution, treat the hypothesis as execution-fragile rather than validated alpha.
8. Failure condition: no stable cost-adjusted directional edge out of sample, reversed sign across venues/regimes, or dependence on unavailable/revised liquidation information materially weakens or rejects the hypothesis.

## Crypto portability

direct

The source is explicitly designed around crypto-exchange liquidation data and names Bybit/OKX. Portability is nevertheless venue-specific: liquidation definitions, sign conventions, contract specifications, reporting latency, mark/index mechanics, funding, and liquidity differ by exchange. A signal reconstructed from one venue must not be assumed portable to another without evidence.

## Limitations

- Several operational parameters are **underspecified** on the public description.
- Liquidation-series sign and semantic interpretation must be independently verified.
- Point-in-time data availability is unverified.
- Execution costs during forced-liquidation events may dominate a short-horizon reversal effect.
- No independent reproduction has occurred.
- A public TradingView script is evidence of a testable hypothesis, not evidence of profitability.

## Implementation status

Research record only. No implementation or backtest in the research stack has been completed.

## Adoption boundary

This record is research material only. It is not validated alpha and is not approved for implementation, paper trading, testnet, or live trading. Presence in this repository does not imply profitability.

## Related Wiki records

No stable related Hermes Wiki record is asserted here.

## Sources

- TradingView — llbot, **Liquidation Strategy**, published 2025-09-13, reviewed 2026-09-17: https://www.tradingview.com/script/Aef557RY-Liquidation-Strategy/
