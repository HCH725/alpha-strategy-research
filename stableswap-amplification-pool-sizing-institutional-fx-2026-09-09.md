---
schema: strategy-research-record-v1
title: "StableSwap Amplification-Adjusted Pool Sizing for Institutional On-Chain FX Liquidity Provision"
created: 2026-09-09
updated: 2026-09-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - defi
  - amm
  - stableswap
  - curve
  - liquidity-provision
  - fx
  - institutional
  - pool-sizing
  - lvr
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - "Ryan Fang, Ivan Bardziyan, Jessica Wang, Mayank Anand, 'Viable Pool Sizing for On-Chain FX Liquidity: Amplification, Capital, and Resilience', arXiv:2608.30957v1 [cs.CE], August 31, 2026. https://arxiv.org/abs/2608.30957"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# StableSwap Amplification-Adjusted Pool Sizing for Institutional On-Chain FX Liquidity Provision

## Provenance

- **Primary source:** Ryan Fang (Royal Bank of Canada), Ivan Bardziyan (Royal Bank of Canada), Jessica Wang (Royal Bank of Canada), Mayank Anand (Borealis AI), *"Viable Pool Sizing for On-Chain FX Liquidity: Amplification, Capital, and Resilience"*, arXiv preprint `arXiv:2608.30957v1 [cs.CE]`, submitted August 31, 2026.
- **Canonical DOI:** 10.48550/arXiv.2608.30957
- **Abstract & metadata:** https://arxiv.org/abs/2608.30957
- **Full-text PDF:** https://arxiv.org/pdf/2608.30957
- **Source/data as-of:** August 31, 2026 (preprint).
- **Code/data availability:** Not stated in the paper; no public repository linked.

## Economic mechanism

### Source-reported

The authors identify that neither constant-product (CPMM) nor constant-sum (CSMM) AMMs satisfy the three simultaneous requirements of institutional FX liquidity provision: competitive slippage (≤2 bps), positive return, and shock resilience. StableSwap (Curve Finance, 2020) interpolates between CPMM and CSMM via an amplification factor A, concentrating liquidity near a target rate. Using a Merton jump-diffusion price process and the LVR (loss-versus-rebalancing) framework, the authors map the joint (A, TVL) space to identify configurations that satisfy all three requirements simultaneously. Capital efficiency gains from higher A are offset by shock fragility, and the two constraints bind in different regions of the parameter space.

### Research interpretation

The hypothesized mechanism is that StableSwap LP return on capital is determined by the interaction of three factors: (1) fee revenue from trading flow, (2) LVR capture from rebalancing against arbitrageurs, and (3) gas costs. The optimal pool configuration (A, TVL) maximizes this return subject to slippage and resilience constraints. The minimum viable pool size scales as TVL/Q ≈ 1000/A, establishing a capital floor that decreases with amplification. However, high-A pools become fragile under large one-sided shocks, establishing a practical amplification ceiling.

## Signal

- **Formation timestamp:** Not a signal per se; this is a pool design/sizing framework. The "signal" is the optimal (A, TVL) configuration for a given institution's flow profile.
- **Lookback:** N/A (design-time sizing, not runtime signal).
- **Entry (LP deployment):** Deploy StableSwap pool with amplification factor A and TVL such that TVL/Q ≥ 1000/A (research-proposed minimum viability threshold, calibrated from simulation). The Q (trade size) should reflect expected institutional flow magnitude.
- **Exit:** N/A (continuous LP position; no discrete exit signal).
- **Holding period:** Continuous; the pool operates as long as it remains viable under the resilience constraint.
- **Parameters:**
  - A ∈ [10, 500] (practical range; A ≤ 10 causes slippage > 200 bps under 10× shock; A ≥ 500 causes reserve drain up to 60%).
  - Fee f = 1 bp (10⁻⁴) — protocol-level fee for stable pairs, matching tight institutional inter-dealer spreads.
  - Oracle update threshold θ_peg = 0.1% (repegging trigger).
  - Gas cost threshold c_gas = 5 × 10⁻⁷ (rebalancing trigger; ≈$0.05 per rebalance on $100K trade).
  - TVL/Q ≈ 1000/A (minimum viable pool size scaling relationship — research-proposed, calibrated from simulation).
- **Parameters source:** All parameters are from the paper's simulation setup and are labeled as source-reported within the simulation context. The 1000/A scaling relationship is source-reported from bisection calibration.

## Required data

- **Instrument:** StableSwap AMM pool (Curve Finance or equivalent) for near-pegged asset pairs.
- **Universe:** Institutional FX pairs deployed on-chain (EUR/USD, USD/CAD, etc.) or crypto-native stablecoin pairs (USDC/USDT, DAI/USDC).
- **Venue:** On-chain StableSwap deployment (e.g., Curve Finance); oracle source for off-chain reference rate.
- **Market type:** On-chain spot liquidity provision.
- **Timeframe:** Continuous; pool operates 24/7.
- **Fields:** Pool reserves (x, y), oracle price (p*), trade history (Q_t, direction), fee revenue, LVR per rebalancing event, gas costs, pool imbalance.
- **Point-in-time:** Oracle price must be available with low latency for repegging; off-chain FX rates typically available from institutional data vendors.
- **Timestamp:** UTC; on-chain block timestamps.
- **Missing-data:** Not explicitly addressed for crypto-native deployment; oracle latency and availability assumptions from institutional FX may not transfer directly.

## Execution assumptions

- **Signal-to-order timing:** Pool is pre-configured; no runtime signal-to-order delay for LP deployment.
- **Rebalancing:** Bot compares P_AMM_t to spot S_t; if |P_AMM_t − S_t| > c_gas, executes price-alignment trade via binary search for q*.
- **Repegging:** Independent oracle update when |p* − S_t|/p* > θ_peg; re-centers invariant without executing a trade.
- **Order type:** Market orders for rebalancing trades (bot executes against invariant).
- **Fill model:** Deterministic (AMM invariant guarantees fill at computed price).
- **Fees:** 1 bp (10⁻⁴) per trade, paid by taker; accrues to LP as sole liquidity provider.
- **Slippage:** Derived from StableSwap invariant; second derivative ∂²P_AMM/∂Q² ∝ 1/(A · D²).
- **Gas cost:** Conservative L2 estimate of $0.05 per rebalance on $100K trade; total gas burned ≈$0.0003 over 500 steps vs. fee revenue ≈$5,400 (ratio ≈10⁻⁷).
- **Leverage:** Not applicable (spot LP position).
- **Funding:** Not applicable.
- **Market impact:** Pool price impact modeled via StableSwap invariant; institutional flow modeled as one-sided shocks of 5×, 10×, 20× Q at 50-step intervals.
- **Capacity:** Limited by TVL; higher TVL increases slippage resilience but reduces ROC.

## Evidence

### Source-reported

Source-reported results from Merton jump-diffusion simulation (σ = 5%, λ = 1.5 yr⁻¹, jumps ±2%, µ = 0):

- **Minimum viable pool size:** TVL/Q ≈ 1000/A (within 5% across all tested A values).
- **ROC at minimum viable pool size:** ≈0.054% per horizon; A-invariant (nearly constant across tested A values).
- **Low-A fragility (A ≤ 10):** Slippage exceeds 200 bps under a 10× shock.
- **High-A fragility (A ≥ 500):** Reserve drain up to 60% under adversarial flow.
- **Resilience experiment (σ = 8%, λ = 3.0):** Elevated stress scenario confirms the capital floor and amplification ceiling.
- **Gas cost insensitivity:** ROC is determined almost entirely by f · Q · N_steps / TVL; gas costs are negligible relative to fee revenue.

All performance figures are from simulation, not live deployment or historical backtest against real market data. The simulation uses a stylized Merton jump-diffusion calibrated to G10 FX parameters, not empirical crypto or FX market data.

### Independently reproduced

Not independently reproduced. No code or data repository is provided in the paper.

### Negative evidence

Source-reported limitations:
- ROC at minimum viable pool size is thin (≈0.054% per horizon), suggesting the strategy is capital-intensive relative to return.
- The paper explicitly identifies two regimes that fall outside TSI's scope: single-asset divergence and slow geopolitical compounding (though this is from a different paper's framework).
- The Merton jump-diffusion model with calibrated parameters (σ = 5%, λ = 1.5, jumps ±2%) may not capture the full range of crypto-native volatility and jump dynamics.
- No empirical validation on real StableSwap pool data or live on-chain deployment.

## Falsification plan

- **Required sample:** Historical StableSwap pool data (reserves, trades, oracle prices) for stablecoin pairs on Curve Finance over a period spanning at least one major depeg event (e.g., USDC depeg, UST collapse).
- **Baseline:** Compare ROC against simple CPMM LP (Uniswap v2) and concentrated liquidity LP (Uniswap v3) for the same pairs.
- **Cost sensitivity:** Stress test ROC under varying fee levels (0.5 bp, 1 bp, 5 bp), gas costs (L1 vs. L2), and oracle latency.
- **Parameter perturbation:** Vary A and TVL independently to verify the 1000/A scaling relationship holds in live market conditions.
- **Out-of-sample:** Test across multiple stablecoin pairs and different market regimes (low vol, high vol, depeg events).
- **Failure metric:** If ROC at minimum viable pool size is negative after accounting for gas, IL, and adverse selection in live conditions, the sizing framework fails.
- **Action on failure:** Re-evaluate whether the 1000/A scaling relationship holds under empirical market conditions; consider dynamic A adjustment.

## Crypto portability

**Adapted**

The paper's primary application is institutional on-chain FX (G10 currency pairs deployed on StableSwap), not native crypto trading. However, the underlying StableSwap mechanism is the same one used in Curve Finance for stablecoin pairs (USDC/USDT, DAI/USDC, etc.), making the sizing framework directly applicable to crypto-native StableSwap deployments.

Crypto-specific portability considerations:
- **Stablecoin vs. FX:** Stablecoin pairs (USDC/USDT) have different volatility and jump dynamics than G10 FX. USDC depeg events (March 2023) represent extreme scenarios not fully captured by the ±2% jump calibration.
- **Oracle availability:** On-chain stablecoin pairs may have different oracle dynamics than institutional FX; oracle latency and manipulation risk differ.
- **24/7 operation:** StableSwap pools operate continuously; the paper's simulation uses daily steps, which may not capture intraday dynamics.
- **Venue fragmentation:** Curve Finance is the dominant StableSwap venue; concentration risk exists.
- **Gas costs:** L2 deployment (as assumed in the paper) may not be available for all stablecoin pairs; L1 gas costs could be material for smaller pools.
- **Fee competition:** The 1 bp fee assumption matches institutional FX but may face competition from lower-fee Curve pools.
- **Regulatory/counterparty risk:** Institutional FX on-chain may face different regulatory constraints than crypto-native stablecoin pairs.

## Limitations

- **Simulation-only:** All results are from Merton jump-diffusion simulation; no live deployment or historical backtest against real StableSwap pool data.
- **Thin ROC:** ≈0.054% per horizon at minimum viable pool size suggests the strategy requires large capital deployment for meaningful absolute returns.
- **Stylized market model:** The Merton jump-diffusion with G10 FX parameters (σ = 5%, λ = 1.5) may not capture crypto-native volatility, jump dynamics, or regime changes.
- **Single LP assumption:** The model assumes a single institutional LP; competitive dynamics with other LPs are not modeled.
- **No code/data:** No public repository or dataset provided; reproducibility is limited.
- **Not independently reproduced:** No external validation of the simulation results.
- **Institutional focus:** The paper targets institutional FX deployment, not retail DeFi LP; scaling assumptions may differ for smaller pools.
- **Underspecified crypto portability:** The paper does not explicitly address crypto-native StableSwap deployment (e.g., Curve stablecoin pairs); portability is research-proposed.

## Implementation status

No implementation in our research stack (PyBroker, NautilusTrader, Paper, Testnet, or Live). This is a research capture of an external academic preprint.

## Adoption boundary

This record represents research material only. It does not constitute:
- Proof that StableSwap LP is profitable in live conditions;
- Validation of the 1000/A sizing relationship under empirical crypto market conditions;
- Approval for paper trading, testnet, or live deployment;
- A recommendation to deploy capital on StableSwap pools.

## Related Wiki records

- `[[quant/amm-lvr-jump-floor-optimal-block-time-2026-09-08]]` (related LVR/AMM literature, different focus on block-time optimization)
- `[[quant/crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31]]` (related LVR framework, different focus on toxic arbitrage)
- `[[quant/defi-concentrated-liquidity-amm-dynamic-fee-staleness-proxy-lvr-compensation-2026-09-02]]` (related concentrated liquidity LVR, different focus on dynamic fees)

## Sources

1. Ryan Fang, Ivan Bardziyan, Jessica Wang, Mayank Anand. *"Viable Pool Sizing for On-Chain FX Liquidity: Amplification, Capital, and Resilience"*. arXiv preprint `arXiv:2608.30957v1 [cs.CE]`, submitted August 31, 2026.
   - DOI: https://doi.org/10.48550/arXiv.2608.30957
   - Abstract: https://arxiv.org/abs/2608.30957
   - PDF: https://arxiv.org/pdf/2608.30957
