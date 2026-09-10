---
schema: strategy-research-record-v1
title: "Perpetual Futures for Stocks: Unified Pricing and Price Discovery via the Funding Rate"
created: 2026-09-10
updated: 2026-09-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - perpetual-futures
  - funding-rate
  - price-discovery
  - pre-ipo
status: research-only
confidence: medium
source_as_of: 2026-09-09
sources:
  - https://arxiv.org/abs/2609.05433
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Perpetual Futures for Stocks: Unified Pricing and Price Discovery via the Funding Rate

## Provenance

- **Paper:** Aditya Gupta and Nicholas G. Polson. "Perpetual Futures for Stocks: The SpaceX Pre-IPO Market." arXiv preprint `arXiv:2609.05433v1 [q-fin.PR]`, September 2026.
- **URL:** https://arxiv.org/abs/2609.05433
- **PDF:** https://arxiv.org/pdf/2609.05433
- **arXiv ID:** 2609.05433v1
- **Submission date:** September 9, 2026
- **Authors:** Aditya Gupta (Stochastic Process, New York), Nicholas G. Polson (Booth School of Business, University of Chicago)
- **Venue:** Preprint (not yet published in a journal)
- **Category:** q-fin.PR (Pricing of Securities)
- **JEL codes:** G12, G13, G14, C11
- **Keywords:** perpetual futures, funding rate, price discovery, no arbitrage, martingale pricing, non-linear filtering, stochastic volatility, time change, market segmentation, pre-IPO equity, generative Bayesian computation

## Economic mechanism

### Source-reported

The paper provides a unified pricing framework for perpetual futures that nests both Shiller's 1993 design (settling against observable flows like dividends or rents) and the crypto basis-pegged design (settling against spot price). The key insight is that the funding rule alone separates the two designs: Shiller's design is self-anchoring (settles on a real flow, needs no external price), while the crypto design is basis-anchored (needs an observable spot). Both are the same instrument with two different benchmarks.

The funding rate is shown to simultaneously serve as:
1. A discount rate (in the present value representation)
2. A clock (in the random time change representation)
3. An observer gain (in the filtering/price discovery representation)
4. A learning rate (in the Bayesian learning interpretation)

The paper demonstrates that stochastic volatility moves the basis only through the carry, so a volatility risk premium—not volatility itself—can break the peg. The pre-IPO premium is shown to be structural (driven by market segmentation) rather than behavioral.

### Research interpretation

The mechanism suggests several falsifiable hypotheses for crypto perpetual futures trading:

1. **Funding rate as a learning signal:** The funding rate encodes information about the market's expectation of the future spot price, weighted by the funding intensity. Higher funding rates may indicate stronger directional conviction among informed traders.

2. **Volatility risk premium channel:** If stochastic volatility only affects the basis through the carry (futures-forward adjustment), then volatility itself should not systematically distort the perpetual-spot peg unless volatility is priced. This implies that simple volatility-based funding rate predictions may be misspecified.

3. **Market segmentation premium:** The basis may contain a structural component driven by market segmentation (different investor pools with different constraints), not just speculative positioning. This could create predictable basis patterns across different perpetual contracts.

4. **Funding rate convergence post-listing:** For pre-IPO or newly listed perpetual contracts, the funding rate should converge to the securities lending fee once the underlying becomes borrowable.

## Signal

### Source-reported

The paper does not propose a specific trading strategy. It provides a theoretical framework for pricing perpetual futures and analyzing the basis.

### Research interpretation (research-proposed)

Possible signal constructions derived from the framework:

1. **Basis decomposition signal:** Decompose the perpetual-spot basis into (a) carry component, (b) volatility risk premium component, and (c) market segmentation component. Trade the segmentation component if it shows mean-reversion.

2. **Funding rate convergence signal:** For newly listed perpetual contracts, monitor the funding rate relative to the expected securities lending fee. Large deviations may indicate mispricing that will converge post-listing.

3. **Cross-contract funding rate spread:** Compare funding rates across perpetual contracts with different underlying assets. The spread should reflect differences in carry, volatility risk premium, and segmentation.

**Parameters:** All thresholds and parameters are research-proposed, not source-specified.

## Required data

- **Universe:** Perpetual futures contracts (crypto and equity perpetuals)
- **Market type:** Perpetual futures, spot markets for underlying
- **Timeframe:** Daily or intraday funding rate observations
- **Fields required:**
  - Perpetual price (Ft)
  - Spot/index price (St)
  - Funding rate (gt)
  - Funding intensity (κ)
  - Underlying asset volatility
  - Securities lending fee (for equity perpetuals)
  - Market capitalization / float (for segmentation analysis)
- **Point-in-time:** Funding rate observations must be timestamped and availability-lag-aware
- **Missing-data assumptions:** Funding rates are observed at discrete intervals; continuous-time approximations require interpolation

## Execution assumptions

- **Signal-to-order timing:** Research-proposed: daily rebalancing based on funding rate observations
- **Fill model:** Not specified in source; research-proposed: market order at funding settlement
- **Fees:** Not specified in source; research-proposed: standard perpetual futures taker fees
- **Slippage:** Not specified in source; research-proposed: proportional to order size
- **Funding:** The framework itself models funding; actual funding costs are observed, not assumed
- **Leverage:** Not specified in source; research-proposed: 1x (no leverage)
- **Position limits:** Not specified in source; research-proposed: single contract per trade

## Evidence

### Source-reported

The paper provides the following empirical findings for the SpaceX pre-IPO market (June 2026):

- The perpetual consensus price forecast the secondary clearing price more accurately than the bookbuilt offer price
- The pre-IPO premium was structural (driven by market segmentation) rather than behavioral
- The basis should collapse toward zero as the float grows (across December lockup expiry)
- The funding rate should converge to the securities lending fee post-listing

These results are source-reported and have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The paper notes that:
- The peg can be broken by a volatility risk premium (not just volatility)
- Market segmentation creates structural basis that may not mean-revert quickly
- The framework assumes frictionless markets for the main propositions; real-world frictions (funding caps, margin requirements) can create bands where the basis is not enforced

## Falsification plan

1. **Basis collapse test:** Measure the perpetual-spot basis before and after December lockup expiry. If the premium persists, the segmentation reading is rejected in favor of a bubble explanation. (Source-proposed)

2. **Funding rate convergence test:** Compare the perpetual funding rate to the securities lending fee post-listing. If they do not converge, the price discovery mechanism is misspecified. (Source-proposed)

3. **Volatility insensitivity test:** Regress the basis on realized volatility and on the carry component separately. If volatility has a direct effect on the basis (beyond carry), the stochastic volatility result is falsified. (Source-proposed)

4. **Cross-contract spread test:** Compare funding rate spreads across contracts with different segmentation characteristics. If spreads do not correlate with segmentation measures, the structural premium hypothesis is weakened. (Research-proposed)

5. **Out-of-sample test:** Apply the framework to other pre-IPO perpetual markets (if available) to test generalizability. (Research-proposed)

## Crypto portability

**direct**

The paper explicitly bridges the Shiller perpetual design with the crypto basis-pegged design, providing a unified framework. The crypto perpetual futures pricing results of He, Manela, Ross, and von Wachter (2022) are nested within the general framework.

Crypto-specific considerations:
- The framework assumes continuous-time funding; real crypto perpetuals have discrete 8-hour funding intervals
- Funding rate caps (|gt| ≤ ḡ) create a band where the basis is not enforced; the paper acknowledges this but does not fully model the dynamics outside the band
- Cross-exchange fragmentation in crypto may create additional segmentation effects not captured by the single-market equilibrium
- The framework does not account for liquidation mechanics or auto-deleveraging

## Limitations

- **Theoretical framework:** The paper provides pricing theory, not a backtested trading strategy
- **Single case study:** The SpaceX pre-IPO market is the only empirical application; generalizability is untested
- **Data availability:** For equity perpetuals, the data is limited to a single episode
- **Assumptions:** The main propositions assume frictionless markets; real-world frictions (funding caps, margin requirements, partial fills) can distort results
- **Not independently reproduced**
- **Pre-IPO-specific dynamics:** Market segmentation effects may be stronger for pre-IPO assets than for crypto perpetuals with established spot markets

## Implementation status

not-implemented

No implementation in our research stack. This is a theoretical framework paper; no backtested strategy or live implementation is provided.

## Adoption boundary

research-only

This record represents normalized research material only. It does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]] (schema specification)
- No directly related strategy research records share the same source identity.
- Adjacent records that discuss perpetual futures funding rates:
  - `crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31.md` (different mechanism: funding rate carry vs. unified pricing theory)
  - `crypto-perpetual-no-arbitrage-deviation-2026-08-31.md` (different focus: no-arbitrage bounds vs. price discovery)

## Sources

1. Aditya Gupta and Nicholas G. Polson. "Perpetual Futures for Stocks: The SpaceX Pre-IPO Market." arXiv preprint `arXiv:2609.05433v1 [q-fin.PR]`, September 9, 2026. https://arxiv.org/abs/2609.05433.
