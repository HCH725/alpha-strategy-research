---
schema: strategy-research-record-v1
title: TradingView Bitcoin SOPR 150-Day DEMA / 365-Day WMA Regime Crossover
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - bitcoin
  - on-chain
  - sopr
  - regime
status: research-only
confidence: medium
source_as_of: 2025-01-10
sources:
  - https://www.tradingview.com/script/TVe3qKzx-SOPR-QuantumResearch/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Bitcoin SOPR 150-Day DEMA / 365-Day WMA Regime Crossover

## Provenance

- Public TradingView open-source script: `SOPR | QuantumResearch`, published 2025-01-10.
- Stable source URL: https://www.tradingview.com/script/TVe3qKzx-SOPR-QuantumResearch/
- The page identifies the underlying daily series as Glassnode `BTC_SOPR` and describes a short/long smoothing crossover. The source also describes the indicator as Rocheur's SOPR indicator; this record preserves the TradingView page identity rather than inferring authorship beyond the page.
- Source as-of date: 2025-01-10.

## Economic mechanism

### Source-reported

The source states that SOPR measures whether spent outputs are being realized at profit or loss. It smooths SOPR into a shorter-term series using a 150-day DEMA and a longer-term series using a 365-day WMA. It labels the regime bullish when the shorter series is above the longer series, bearish when it is below, and neutral when equal.

### Research interpretation

This is a slow **realized-profitability regime-diffusion** hypothesis rather than the usual SOPR=1 support/resistance rule. If recent realized profitability improves persistently relative to its one-year baseline, the 150-day DEMA should cross above the 365-day WMA before or during a durable risk-on regime; sustained deterioration should produce the inverse. The distinct question is whether the cross-horizon SOPR trend spread contains incremental forward-return information beyond raw SOPR, SOPR=1 behavior, and price trend.

## Signal

Source-specified components:

- Input: daily Glassnode BTC SOPR.
- Short series: DEMA of SOPR, default length 150 days.
- Long series: WMA of SOPR, default length 365 days.
- Bullish state: short series > long series.
- Bearish state: short series < long series.
- Neutral state: equality.

The source page does not specify a complete position lifecycle, order timing, holding period, sizing rule, stop, or execution venue. Therefore no source-reported trading rule is inferred.

Research-proposed tests:

1. Treat the sign of `DEMA150(SOPR) - WMA365(SOPR)` as a daily regime state using only data available at signal time.
2. Separately test crossover events and continuous regime-state conditioning.
3. Test parameter neighborhoods rather than treating 150/365 as privileged constants.
4. Compare against simpler `SMA150(SOPR)-SMA365(SOPR)`, raw SOPR, SOPR relative to 1, and price 150/365 trend controls.

All four items above are research-proposed, not source-reported execution rules.

## Required data

- Bitcoin daily price returns for outcome measurement.
- Point-in-time daily BTC SOPR compatible with the source's Glassnode series.
- Historical availability timestamps or conservative publication lag for SOPR.
- At least 365 prior daily observations before the long smoother is valid.
- UTC date alignment between on-chain observations and tradable BTC price bars.

## Execution assumptions

The source does not specify execution assumptions. For research, any tradable implementation must delay orders until the SOPR observation used by the signal was actually available. Same-bar fills using a not-yet-final daily on-chain value are prohibited. Fees, spread, slippage, funding, leverage, and sizing remain unspecified until a later implementation stage.

## Evidence

### Source-reported

The TradingView page describes the 150-day DEMA versus 365-day WMA comparison as bullish/bearish/neutral market-state classification. No independently verified performance statistic is claimed in this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The reviewed source provides no traceable Sharpe, CAGR, drawdown, hit rate, or formal out-of-sample evidence for the crossover. The long smoothing windows also imply substantial lag, and the specific 150/365 pair may encode historical tuning. Absence of further negative evidence in the reviewed source is not evidence of robustness.

## Falsification plan

1. Reconstruct the two smoothed SOPR series point-in-time and verify that no future daily SOPR value enters signal formation.
2. Compare forward BTC returns conditional on bullish versus bearish states across multiple market cycles, with walk-forward and leave-one-cycle-out evaluation.
3. Baselines: raw SOPR, SOPR above/below 1, the existing SOPR support/resistance formulation, simple price momentum, and a 150/365 price moving-average regime.
4. Ablate smoothing choice: DEMA/WMA versus same-family SMA/SMA and EMA/EMA. If the claimed transformation adds no stable OOS information, reject the transformation layer.
5. Stress neighboring horizons around 150 and 365 days. If usefulness exists only at the exact source pair, treat it as parameter fragility and reject the hypothesis.
6. Apply realistic on-chain publication delays and shift-placebo tests. Any edge that disappears under conservative availability timing fails the point-in-time requirement.
7. The hypothesis is weakened or rejected if the SOPR trend spread has no stable incremental OOS predictive value after controlling for price trend and simpler SOPR states.

## Crypto portability

**Direct for Bitcoin.** SOPR is crypto-native on-chain data and the source explicitly uses Bitcoin SOPR. Portability to other assets is unproven even though the source discusses selectable crypto support elsewhere; chain accounting, provider methodology, liquidity, and market structure can differ materially.

## Limitations

- not independently reproduced
- source page does not provide a complete trading lifecycle
- provider methodology / revisions can affect historical SOPR
- daily on-chain publication timing must be modeled point-in-time
- exact 150/365 horizons may be historically tuned
- slow filters may react only after substantial price movement

## Implementation status

No implementation or backtest in the internal research stack has been completed.

`implementation_status: not-implemented`

## Adoption boundary

Research material only. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor, is profitable, or is approved for Paper, Testnet, or Live trading.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `[[bitcoin-onchain-sopr-spent-output-profit-ratio-2026-08-31]]` — existing SOPR level/support-resistance and cycle-reversal family; this record isolates a materially different slow cross-horizon SOPR trend regime.

## Sources

1. TradingView, `SOPR | QuantumResearch`, public page, published 2025-01-10: https://www.tradingview.com/script/TVe3qKzx-SOPR-QuantumResearch/
