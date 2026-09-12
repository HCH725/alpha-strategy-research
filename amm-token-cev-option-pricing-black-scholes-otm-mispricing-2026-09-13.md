---
schema: strategy-research-record-v1
title: AMM Token CEV Option Pricing and Black-Scholes OTM Put Mispricing (Bittensor dTAO)
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - defi
  - amm
  - options
  - cev-model
  - bittensor
  - volatility-skew
  - structural-mispricing
status: research-only
confidence: high
source_as_of: 2026-03-31
sources:
  - "Philip Z. Maymin, 'Option Pricing on Automated Market Maker Tokens', arXiv:2603.29763v1 [q-fin.PR], March 31, 2026. DOI: https://doi.org/10.48550/arXiv.2603.29763"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AMM Token CEV Option Pricing and Black-Scholes OTM Put Mispricing (Bittensor dTAO)

## Provenance

- **Paper:** Philip Z. Maymin, "Option Pricing on Automated Market Maker Tokens." arXiv:2603.29763v1 [q-fin.PR], March 31, 2026.
- **DOI:** https://doi.org/10.48550/arXiv.2603.29763
- **Author:** Philip Z. Maymin, Dolan School of Business, Fairfield University (pmaymin@fairfield.edu).
- **Author disclosure:** Co-owner of Djinn, a project operating on the Bittensor network.
- **Sample:** Cross-sectional variance elasticity test across 90 Bittensor subnets; delta-hedged backtest across 82 subnets. Data from August 8, 2025, through February 23, 2026, retrieved from the Taostats API.
- **Universe:** Bittensor Dynamic TAO (dTAO) subnets — AMM-native tokens whose sole price discovery mechanism is a constant-product AMM (no external order book, no oracle).
- **Source URL:** https://arxiv.org/abs/2603.29763

## Economic mechanism

### Source-reported

Tokens traded exclusively through a constant-product AMM (x·y = k) follow a constant elasticity of variance (CEV) price process rather than geometric Brownian motion (GBM). When net staking flow into the pool follows a Brownian diffusion, the token price follows a CEV process with exponent β = w (the numeraire weight in the pool), and volatility parameter δ = σ_f / √(2k), where σ_f is flow volatility and k is the pool invariant. For the standard constant-product AMM, β = 1/2.

This CEV structure generates a structural leverage effect: as price falls, the TAO reserve shrinks, the pool becomes shallower in dollar terms, and the same staking flow produces larger proportional price changes. This is a mechanical consequence of the bonding curve, not capital structure.

The normalized implied volatility skew depends only on β, not on pool depth k or flow volatility σ_f. Black-Scholes systematically underprices 20%-out-of-the-money puts by roughly 6% in implied volatility terms at every pool depth. Conversely, Black-Scholes overprices OTM calls.

### Research interpretation

The falsifiable hypothesis is that AMM-native tokens have a structural negative volatility skew that Black-Scholes misprices in the wings. The leverage effect is endogenous to the AMM design, not a risk premium. This creates a potential trading opportunity: buying OTM puts on AMM tokens priced via Black-Scholes, or selling OTM calls, captures the structural mispricing. The magnitude is concentration-independent (the normalized skew is universal for constant-product AMMs), so it persists across pool depths.

A second testable implication: realized return variance scales as P^(β-1) = P^(-1/2) for constant-product AMMs, which can be estimated from on-chain data without traded options.

## Signal

Source-supported signal definition:

1. **Universe:** Tokens traded exclusively through constant-product AMMs (e.g., Bittensor dTAO subnets, potentially other AMM-native DeFi tokens).
2. **Hypothesis:** Black-Scholes implied volatility skew on these tokens is structurally wrong. OTM puts are underpriced relative to the CEV model; OTM calls are overpriced.
3. **Concrete example from source:** 90-day 20%-OTM puts on three representative Bittensor subnets are priced 10–28% higher under CEV than Black-Scholes (matched ATM vol): 12.1% vs 11.1% of spot (shallow pool), 0.52% vs 0.41% (medium), 0.43% vs 0.34% (deep).
4. **Directional hypothesis:**
   - Buy OTM puts on AMM-native tokens when priced by Black-Scholes (CEV fair value exceeds BS price).
   - Sell OTM calls on AMM-native tokens (CEV fair value is below BS price).
   - The edge is structural and persists at every pool depth for constant-product AMMs.

**Underspecified trading rules:** The paper provides pricing theory, not a canonical executable portfolio rule. The following are underspecified and must not be treated as source-reported:
- Strike selection threshold (the 20%-OTM example is illustrative, not prescriptive).
- Optimal maturity.
- Position sizing, entry timing, or exit rules.
- Overlap or correlation management across subnets.
- Whether to trade via on-chain options protocols (if available) or OTC.

## Required data

- **Instruments:** AMM-native tokens with constant-product AMMs (Bittensor dTAO subnets; potentially Uniswap V3 concentrated-liquidity positions treated locally as constant-product).
- **Venue:** On-chain AMM pools (Bittensor Taostats API for on-chain data).
- **Market type:** Options on AMM-native tokens (currently limited; no active options markets on Bittensor subnets as of the paper).
- **Timeframe:** Daily on-chain reserve data for variance elasticity estimation; hourly or finer for flow volatility estimation.
- **Required fields:** TAO reserve (τ), alpha reserve (α), pool invariant (k = τ·α), price (p = τ/α), daily net TAO flow changes.
- **Derived fields:** Flow volatility (σ_f, annualized from daily flow standard deviation), realized return variance (rolling 14-day), variance elasticity (log variance regressed on log price controlling for pool depth and flow volatility).
- **Point-in-time:** On-chain data is fully timestamped; no look-ahead issues.
- **Missing-data assumption:** Subnets with degenerate price paths (price range exceeding 100×, zero price variance, or non-positive reserves) are excluded.

## Execution assumptions

The source does **not** present a complete net-of-cost trading strategy. The CEV pricing model is presented as a theoretical framework.

For an executable test, the following assumptions would need to be specified:
- **Transaction costs:** Bittensor dTAO pools currently charge no explicit swap fee, making the zero-fee model directly applicable. However, AMM slippage is the primary friction.
- **Slippage / market impact:** For a hedge trade of Δα units, slippage cost ≈ Δα²/(2τ). The replication premium is bounded by (16/3)·σ_f²·τ/(k³) per hedging interval, which scales as O(k^(-3/2)).
- **Fill model:** AMM trades execute deterministically against the bonding curve (no partial fills, no adversarial fills); however, price impact is first-order.
- **Funding:** Not applicable for AMM-native tokens (no perpetual contracts).
- **Leverage / margin:** Not applicable for the pricing framework; relevant for options trading if options markets develop.
- **Latency:** On-chain confirmation latency (Bittensor block time ~12 seconds); front-running risk near option expiry for shallow pools.

## Evidence

### Source-reported

1. **Variance elasticity test (90 subnets):** Median variance elasticity of -0.369 (IQR [-0.486, -0.274]), with 94% of subnets showing negative slopes. Strongly rejects GBM null (slope = 0; t = -24.1, p ≈ 0) and is broadly consistent with CEV prediction (slope = -0.5; t = -4.6, p ≈ 0). The attenuation from -0.5 to -0.369 is attributed to: (i) discrete jump-like staking events, (ii) measurement noise from overlapping rolling windows, and (iii) some pools operating with effective weights slightly above 0.5.

2. **Delta-hedged backtest (82 subnets):** CEV and Black-Scholes ATM call hedging errors are nearly identical (median MAE 0.97% of spot for both). Only 17 of 82 subnets (21%) show lower hedging error under CEV. The slope of CEV/BS error ratio on 1/k is negative and insignificant, confirming that ATM pricing differences are negligible at all pool depths. This is consistent with the theory: the normalized skew is universal for β = 1/2, so ATM prices are nearly identical.

3. **Wing pricing discrepancy:** Black-Scholes underprices 20%-OTM puts by roughly 6% in implied volatility terms at every pool depth. Concrete example: 90-day 20%-OTM puts priced 10–28% higher under CEV than Black-Scholes across shallow, medium, and deep pools.

4. **Monte Carlo validation:** For deep pools (k = 8,250), maximum deviation between MC and CEV closed-form is <0.5% of spot. For shallow pools (k = 2,293), MC exceeds CEV by 1–3% of spot due to diffusion-limit violations.

All figures are source-reported. The sample covers August 8, 2025, through February 23, 2026.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The variance elasticity attenuation (median -0.369 vs predicted -0.5) means the actual skew is shallower than the theoretical prediction, though still strongly negative and statistically distinguishable from zero.
- ATM hedging performance is empirically indistinguishable between CEV and Black-Scholes, meaning the CEV framework's practical advantage is concentrated in the wings (OTM options), where no active market currently exists on Bittensor.
- The diffusion assumption for staking flows is violated: Shapiro–Wilk tests reject normality, median excess kurtosis is 10.7, and jump days (~7.7% of days) account for a median 47% of total realized variance. However, cross-sectional hedging errors remain modest (median MAE 0.97% of spot), suggesting robustness to moderate diffusion violations.
- AMM token prices are vulnerable to manipulation near option expiry (cost of moving price is ~τ, which for shallow pools may be small relative to option payoff).
- The paper does not demonstrate that the mispricing generates net alpha after replication frictions, because no active options market on AMM-native tokens exists to test against.

## Falsification plan

1. **Variance elasticity test on independent AMM-native tokens:** If realized return variance does not scale as P^(β-1) for constant-product AMMs on other protocols (not Bittensor), the CEV mechanism is weakened.
2. **Wing pricing verification via on-chain options:** If and when options on AMM-native tokens are traded (e.g., on Panoptic or other DeFi options protocols), the CEV-implied OTM put/call price differential should be observable. If OTM put prices match Black-Scholes rather than CEV, the structural mispricing hypothesis is rejected.
3. **Pool weight sensitivity:** If the normalized skew varies with pool weight w (not just β = w), the universality result (Proposition 5) is falsified.
4. **Emission effect:** If token emissions (which deepen the pool over time) systematically change the observed skew beyond the CEV prediction, the deterministic emission model is insufficient.
5. **Jump-diffusion extension:** If a jump-diffusion CEV model provides materially better fit than the diffusion CEV for subnets with frequent whale transactions, the diffusion approximation is rejected for those subnets.
6. **Concentrated liquidity:** If Uniswap V3 concentrated-liquidity positions (where the effective k varies with price range) produce skew patterns inconsistent with the local CEV approximation, the framework's applicability to V3 is weakened.

Pre-specify pool depth categories and maturity ranges. Failure at the variance elasticity level should not be rescued by unconstrained parameter adjustment.

## Crypto portability

**Direct** for AMM-native tokens on constant-product AMMs (Bittensor dTAO, potentially other DeFi protocols with AMM-only price discovery).

**Adapted / unproven** for:
- Tokens with both AMM and order-book price discovery (the endogenous price process is confounded by external market forces).
- Uniswap V3 concentrated-liquidity positions (local CEV applies within range, but range boundaries introduce barriers).
- Tokens on constant-weighted-product AMMs with w ≠ 0.5 (the CEV exponent changes; the framework extends but the specific 6% OTM put mispricing figure does not transfer).
- Options on non-AMM crypto assets (the leverage effect is structural to AMMs, not a general crypto property).

Crypto-specific portability risks: 24/7 on-chain settlement, MEV/front-running near option expiry, emission-driven pool deepening changing the effective δ over time, whale trade jumps violating the diffusion approximation.

## Limitations

- **Not independently reproduced.**
- **No active options market:** The structural mispricing is a theoretical prediction. No options on AMM-native tokens (Bittensor dTAO or similar) are actively traded, so the mispricing cannot be directly exploited or falsified with market prices.
- **Single-venue evidence:** All empirical results are from Bittensor subnets. Generalization to other AMM-native token ecosystems is untested.
- **Diffusion approximation violated:** Heavy-tailed staking flows (median kurtosis 10.7) and jump days (~7.7% of days, contributing ~47% of variance) are acknowledged limitations.
- **Author conflict of interest:** The author is co-owner of Djinn, a project on the Bittensor network. Disclosure is provided in the paper.
- **Working-paper risk:** The source is a March 2026 arXiv working paper.
- **Variance elasticity attenuation:** The observed median elasticity (-0.369) is closer to zero than the theoretical prediction (-0.5), meaning the actual skew is shallower than the model predicts.
- **ATM hedging indistinguishable:** The CEV framework's practical advantage over Black-Scholes is concentrated in the wings, where no market data exists for validation.

## Implementation status

Not implemented in the research stack. No PyBroker, NautilusTrader, Paper, Testnet, or Live reproduction has been performed.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. Presence in the Alpha Strategy Pool does not imply validated alpha, executable profitability, implementation approval, paper-trading approval, testnet approval, or live-trading approval.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted in this Scout cycle.

Related strategy-pool records include:
- `decentralized-ai-subnet-constant-product-amm-size-premium-2026-09-01.md` — same author (Maymin), same Bittensor dTAO ecosystem, but studies factor pricing (size premium, market premium) across subnets rather than option pricing and CEV dynamics. Materially distinct hypothesis, mechanism, and signal.
- `defi-amm-delta-neutral-optimal-hedge-liquidation-constraint-2026-09-11.md` — DeFi AMM hedging, but focuses on LP delta-neutral positions rather than option pricing on AMM tokens.

## Sources

1. Maymin, P. Z. (2026). "Option Pricing on Automated Market Maker Tokens." arXiv:2603.29763v1 [q-fin.PR]. Stable abstract: https://arxiv.org/abs/2603.29763
2. Full public working paper PDF, March 2026 version: https://arxiv.org/pdf/2603.29763
