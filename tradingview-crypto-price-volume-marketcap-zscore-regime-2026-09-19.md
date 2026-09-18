---
schema: strategy-research-record-v1
title: Crypto Price-Volume-Market-Cap Z-Score Regime Filter
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-19
sources:
  - https://www.tradingview.com/script/DACjwujO-Z-Score-Regime-Detector/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Price-Volume-Market-Cap Z-Score Regime Filter

## Provenance

Public TradingView open-source indicator page, **Z-Score Regime Detector**, author/page identity `RWCS_LTD`, published 2025-11-23. Stable source: https://www.tradingview.com/script/DACjwujO-Z-Score-Regime-Detector/ . Source reviewed as of 2026-09-19.

The source explicitly describes a crypto-oriented regime detector based on rolling Z-scores of chart price, volume, and total crypto market capitalization from `CRYPTOCAP:TOTAL`.

## Economic mechanism

### Source-reported

The author argues that standardizing price, volume, and total crypto market capitalization onto comparable Z-score scales can expose underlying market regime. The source characterizes market capitalization as a broader crypto-market context variable and volume as a reference for accumulation/distribution or stress.

The source defines a bullish regime when both the price Z-score and market-cap Z-score are above the volume Z-score, and a bearish regime when both are below the volume Z-score. It separately defines bullish bias when price Z-score is above market-cap Z-score and bearish bias when market-cap Z-score is above price Z-score.

### Research interpretation

The falsifiable hypothesis is that the relative standardized state of a traded asset's price, aggregate crypto capitalization, and trading volume contains incremental information about whether directional crypto signals should be enabled or suppressed. The potentially distinct data dependency is the cross-market `CRYPTOCAP:TOTAL` series rather than a price-only technical regime classifier.

The economic interpretation is not established by the source. In particular, comparing the Z-score of volume directly with Z-scores of price and market capitalization is a heuristic ordering rule; standardization makes the series dimensionless but does not by itself establish that their ordinal relationship has economic meaning.

A possible use as a directional strategy gate is **research-proposed**, not source-validated: permit long-oriented hypotheses during the source-defined bullish regime and short-oriented hypotheses during the bearish regime, then test whether this improves out-of-sample outcomes versus the same primary signal without the gate.

## Signal

Source-reported normalized logic:

- Compute rolling Z-scores for chart close, chart volume, and `CRYPTOCAP:TOTAL` over a user-defined period.
- Bullish regime: `Z(price) > Z(volume)` AND `Z(CRYPTOCAP:TOTAL) > Z(volume)`.
- Bearish regime: `Z(price) < Z(volume)` AND `Z(CRYPTOCAP:TOTAL) < Z(volume)`.
- Bullish bias: `Z(price) > Z(CRYPTOCAP:TOTAL)`.
- Bearish bias: `Z(CRYPTOCAP:TOTAL) > Z(price)`.

The public description does not specify a unique required lookback value, a complete entry/exit system, holding period, re-entry rule, position sizing, or whether regime and bias must be combined. Those items are **underspecified** and must not be inferred from the descriptive page.

Signal formation should be reconstructed using only information available at the relevant completed bar. Any use of the regime as a trading filter is **research-proposed** unless it exactly follows additional source-visible logic.

## Required data

- Instrument / universe: crypto asset being analyzed; exact supported universe is not restricted by the source description.
- Cross-market dependency: TradingView `CRYPTOCAP:TOTAL` total crypto market-cap series.
- Fields: chart close and chart volume plus the `CRYPTOCAP:TOTAL` value required for rolling standardization.
- Timeframe: underspecified; the source does not state one mandatory timeframe in the reviewed public description.
- Rolling history: enough observations for the user-defined Z-score period; exact mandatory period is underspecified.
- Timestamp alignment: chart series and `CRYPTOCAP:TOTAL` must be aligned point-in-time without using a later aggregate-market observation for an earlier chart signal.
- Venue / market type: underspecified. Chart volume can differ materially across spot and perpetual venues.
- Missing-data treatment for `CRYPTOCAP:TOTAL`: underspecified.

## Execution assumptions

The source is an indicator/regime classifier rather than a complete executable trading strategy. It does not provide a complete signal-to-order model, order type, same-bar versus next-bar fill convention, fees, spread, slippage, impact, funding, leverage, margin, shorting, latency, or partial-fill model.

For later testing, execution assumptions must belong to the primary strategy being gated and must be held identical between gated and ungated controls. This control design is **research-proposed**.

## Evidence

### Source-reported

The source explains the regime and bias logic and states that the framework is intended to assess market strength or stress using normalized price, volume, and crypto-market-cap metrics. No independently verified performance statistic is established here, and no source-reported return, Sharpe, CAGR, drawdown, or win-rate figure is recorded.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-reported negative empirical result was identified in the reviewed public description. Absence is not evidence of no negative result.

A structural concern is already visible from the rule itself: Z-scoring makes heterogeneous series dimensionless, but ranking `Z(price)` and `Z(market cap)` against `Z(volume)` does not guarantee a causal or economically stable relationship. The shared crypto-market component between an individual asset price and total market capitalization can also create mechanically correlated regime labels.

## Falsification plan

1. Reconstruct the three rolling Z-score series point-in-time with explicit timestamp alignment and no future aggregate-market observations.
2. Test the source-defined bullish/bearish regime as a gate on simple fixed baseline signals rather than optimizing a new strategy around it.
3. Compare gated versus ungated baselines out of sample after identical fees, spread, slippage, and funding assumptions.
4. Ablate `CRYPTOCAP:TOTAL`: compare the full three-series rule with price-volume only, price-market-cap only, and a price-only trend/regime baseline.
5. Replace the cross-series ordinal comparisons with placebo permutations or lagged/shuffled volume and market-cap controls. Persistent performance under placebo would weaken the claimed mechanism.
6. Segment BTC/ETH versus smaller-cap assets to test whether the aggregate market-cap dependency merely proxies the dominant assets already embedded in `CRYPTOCAP:TOTAL`.
7. Sweep only a bounded set of Z-score lookbacks declared before OOS evaluation; reject parameter choices that require narrow tuning.
8. Test spot and perpetual implementations separately because chart volume, funding, and venue structure differ.
9. Reject the hypothesis if the full regime gate fails to provide stable incremental OOS value over simpler controls, or if any apparent gain is explained by lookback selection, aggregate-market mechanical correlation, or timestamp leakage.

## Crypto portability

direct

The source is explicitly framed for crypto and directly uses `CRYPTOCAP:TOTAL`. Portability across crypto venues remains unproven because chart volume differs by venue and market type, while the total-market-cap series is an external aggregate dependency. Crypto's 24/7 candle boundaries and timestamp alignment must remain fixed across tests.

## Limitations

- Complete trading entry/exit logic: **underspecified**.
- Mandatory Z-score lookback: **underspecified** in the reviewed public description.
- Venue and spot/perpetual specification: **underspecified**.
- Exact missing-data and cross-symbol synchronization behavior: **underspecified**.
- Economic justification for directly ordering price/market-cap Z-scores against volume Z-score: **unproven**.
- Incremental predictive value beyond simpler price-only or market-cap filters: **unproven**.
- Not independently reproduced.

## Implementation status

Research capture only. No implementation or backtest in our research stack has been completed.

## Adoption boundary

This record is research material only. It is not validated alpha and is not approved for implementation, paper trading, testnet, or live trading. Any conversion of the indicator into a directional entry/exit system is **research-proposed** unless separately sourced and validated.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted from this GitHub-only Scout run.

## Sources

- TradingView — RWCS_LTD, **Z-Score Regime Detector**, published 2025-11-23, reviewed 2026-09-19: https://www.tradingview.com/script/DACjwujO-Z-Score-Regime-Detector/
