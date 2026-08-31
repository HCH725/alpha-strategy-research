---
schema: strategy-research-record-v1
title: Delta-Neutral Spot-Perpetual Funding Arbitrage
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - arbitrage
  - funding-rate
  - relative-value
status: research-only
confidence: high
source_as_of: 2022-12-31
sources:
  - "Fundamentals of Perpetual Futures (He, Manela, Ross, von Wachter) - arXiv:2212.06888"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Delta-Neutral Spot-Perpetual Funding Arbitrage

## Provenance

- **Source:** "Fundamentals of Perpetual Futures" by He, Manela, Ross, & von Wachter
- **Venue:** arXiv:2212.06888
- **Target:** General theoretical pricing and empirical testing on cryptocurrency perpetual futures.

## Economic mechanism
### Source-reported
The paper derives no-arbitrage pricing for perpetual futures using a "random-maturity arbitrage" framework. Because perpetuals never expire, they anchor to the underlying spot price via periodic funding payments. Holding a delta-neutral portfolio (e.g., long spot and short perpetual when funding is positive) mathematically captures this funding premium.

### Research interpretation
Spot-Perpetual Funding Arbitrage is a relative-value basis strategy. It exploits structural demand imbalances in the crypto derivatives market, where speculative long leverage often drives perpetual prices above spot prices, resulting in positive funding rates paid by longs to shorts. By shorting the perpetual and longing the spot asset in equal sizes, a trader becomes delta-neutral (immune to directional price moves) and collects the funding rate as yield. The economic mechanism is liquidity provision to leveraged speculators.

## Signal

- **Signal formation:** Continuous or periodic evaluation of the perpetual funding rate relative to transaction and borrowing costs.
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
- **Margin/Leverage:** Requires margin to short the perpetual. Spot acts as hedge but capital efficiency depends on whether the exchange offers cross-margin / unified accounts.
- **Basis Risk:** The perpetual price could temporarily surge higher than spot (basis widening), requiring excess margin to prevent the short perp leg from being liquidated before the funding yield compensates.

## Evidence
### Source-reported
The source evaluates historical implied deviations and theoretical no-arbitrage conditions rather than providing an executable historical trading rule.

### Independently reproduced
Not independently reproduced.

### Negative evidence
None identified in the reviewed sources; absence is not evidence of no negative result. The primary failure modes are basis blowouts (triggering liquidation), exchange counterparty risk (e.g., FTX collapse), and rate flipping (extended negative funding periods eroding yield).

## Falsification plan

- Backtest the strategy accounting for full spot and perpetual transaction fees across historical bull and bear regimes.
- Test the frequency of "rate flips" (funding turning negative) and whether exit costs in those regimes wipe out accumulated yield.
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
- He, Manela, Ross, von Wachter, "Fundamentals of Perpetual Futures".
