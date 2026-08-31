---
schema: strategy-research-record-v1
title: Perpetual Futures No-Arbitrage Deviation
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - arbitrage
  - relative-value
status: research-only
confidence: high
source_as_of: 2022-12-31
sources:
  - "Fundamentals of Perpetual Futures (He, Manela, Ross, von Wachter) - https://arxiv.org/abs/2212.06888 (DOI: 10.48550/arXiv.2212.06888)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Perpetual Futures No-Arbitrage Deviation

## Provenance

- **Source:** "Fundamentals of Perpetual Futures" by He, Manela, Ross, & von Wachter
- **Venue:** arXiv:2212.06888, https://arxiv.org/abs/2212.06888, DOI: 10.48550/arXiv.2212.06888
- **Target:** General theoretical pricing and empirical testing on cryptocurrency perpetual futures.

## Economic mechanism
### Source-reported
The paper derives no-arbitrage prices/bounds for perpetual futures using a "random-maturity arbitrage" framework. Because perpetuals never expire, they anchor to the underlying spot price via periodic funding payments. An implied arbitrage strategy exploits deviations from those no-arbitrage values.

### Research interpretation
Rather than a generic fixed long-spot/short-perp funding carry rule, this approach relies on calculating theoretical no-arbitrage bounds for the perpetual contract based on prevailing interest rates, funding structures, and spot prices. The economic mechanism is relative-value basis trading, engaging when the market price significantly deviates from the calculated no-arbitrage price bounds.

## Signal

- **Signal formation:** Continuous or periodic evaluation of the perpetual price against the theoretical no-arbitrage bounds.
- **Entry:** underspecified (Source derives no-arbitrage pricing bounds rather than a plug-and-play threshold rule).
- **Exit:** underspecified.
- **Position sizing:** underspecified.
- **Specification:** underspecified.

## Required data

- **Instrument:** High-liquidity crypto assets with both spot and perpetual futures markets (e.g., BTC, ETH).
- **Venue:** underspecified.
- **Timeframe:** underspecified.
- **Fields:** Spot price, Perpetual mark price, Perpetual index price, current and predicted Funding Rates.
- **Other:** Borrowing rates for capital, exchange fee tiers.

## Execution assumptions

- **Signal-to-order timing:** underspecified.
- **Order types:** underspecified.
- **Fees:** Maker/Taker fees on both spot and perp legs; withdrawal/deposit fees if transferring collateral.
- **Margin/Leverage:** Requires margin to short/long the perpetual. Spot acts as hedge but capital efficiency depends on whether the exchange offers cross-margin / unified accounts.
- **Basis Risk:** The perpetual price could temporarily surge higher or drop lower than spot (basis widening), requiring excess margin to prevent liquidation.

## Evidence
### Source-reported
The paper reports high Sharpe ratios for an implied arbitrage strategy that exploits deviations from their derived no-arbitrage bounds. This statement is a source-reported claim based on their theoretical framework and historical sample, not our validation.

### Independently reproduced
Not independently reproduced.

### Negative evidence
None identified in the reviewed sources; absence is not evidence of no negative result. The primary failure modes are basis blowouts (triggering liquidation), exchange counterparty risk, and rate flipping.

## Falsification plan

- Backtest the strategy accounting for full spot and perpetual transaction fees across historical bull and bear regimes, specifically targeting deviations from no-arbitrage bounds rather than generic funding rates.
- Evaluate the impact of basis widening on a standard margin account to determine maximum drawdown and capital efficiency requirements.

## Crypto portability

direct

The strategy relies intrinsically on the crypto-native perpetual funding rate mechanism.

## Limitations

underspecified (optimal entry/exit thresholds)
unproven (internally)

## Implementation status

not-implemented

## Adoption boundary

research-only

## Related Wiki records

## Sources
- He, Manela, Ross, von Wachter, "Fundamentals of Perpetual Futures", https://arxiv.org/abs/2212.06888, DOI: 10.48550/arXiv.2212.06888
