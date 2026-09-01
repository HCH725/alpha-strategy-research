---
schema: strategy-research-record-v1
title: "Market Making and Break-Even Fee Design under Noise-Perturbed Order Flow: The Closed-Form Privacy Subsidy in Shielded Exchanges"
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-making
  - privacy-preserving-exchanges
  - kyles-lambda
  - adverse-selection
  - order-flow-noise
  - privacy-subsidy
  - break-even-fees
  - microstructure
status: research-only
confidence: high
source_as_of: 2026-05
sources:
  - "Yuki Nakamura, 'The Privacy Subsidy: Kyle's \\lambda under Noise-Perturbed Order-Flow Observation', arXiv:2605.15746v2 [q-fin.TR, q-fin.MF], May 2026. https://arxiv.org/abs/2605.15746"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Market Making and Break-Even Fee Design under Noise-Perturbed Order Flow: The Closed-Form Privacy Subsidy in Shielded Exchanges

## Provenance

- **Primary Source:** Yuki Nakamura, "The Privacy Subsidy: Kyle's $\lambda$ under Noise-Perturbed Order-Flow Observation", *arXiv preprint arXiv:2605.15746v2 [q-fin.TR, q-fin.MF]*, first submitted May 2026; revised May 2026. URL: [https://arxiv.org/abs/2605.15746](https://arxiv.org/abs/2605.15746).
- **Related Foundational Literature:**
  - A. S. Kyle (1985), "Continuous auctions and insider trading", *Econometrica*, 53(6), pp. 1315–1335.
  - C. Dwork (2006), "Differential Privacy", *Automata, Languages and Programming (ICALP)*.
  - J. Milionis, C. C. Moallemi, T. Roughgarden, and A. L. Zhang (2022), "Automated Market Making and Loss-Versus-Rebalancing", *arXiv:2208.06046*.
  - Y. Nakamura (2026), "The Privacy Subsidy in Continuous-Time Kyle: Cumulative Welfare under Noise-Perturbed Order-Flow Observation", *arXiv:2605.25631*.
- **Context:** Privacy-preserving crypto exchanges (e.g., zero-knowledge CLOBs, shielded automated market makers, differential-privacy order flow aggregators) inject artificial noise or batch-delay mechanisms into observable order flow to protect trader confidentiality. However, when market makers must price trades using noisy aggregated signals while settling against actual underlying order flow, informational misalignment generates an adverse selection loss. Nakamura (2026) solves for the unique linear Kyle equilibrium in closed form, establishing the "Privacy Subsidy"—the exact mathematical break-even fee required to sustain liquidity provision under order flow perturbation.

## Economic mechanism

### Source-reported

1. **Information Structure & Noise Channel:**
   - Underlying fundamental asset value: $v \sim \mathcal{N}(p_0, \sigma_v^2)$.
   - Noise/uninformed trader order flow: $u \sim \mathcal{N}(0, \sigma_u^2)$.
   - Informed trader order: $x = \beta (v - p_0)$, observing $v$ privately.
   - Aggregate net order flow: $y = x + u$.
   - **Privacy Channel:** The market maker does not observe $y$ directly, but rather a noise-perturbed signal:
     $$\tilde{y} = y + \varepsilon, \quad \varepsilon \sim \mathcal{N}(0, \sigma_\varepsilon^2)$$
     where $\varepsilon$ is independent Gaussian privacy noise injected by the protocol (e.g., differentially private aggregation or threshold decryption noise).
2. **Linear Kyle Equilibrium with Privacy Noise:**
   - Market maker quoting rule: $p(\tilde{y}) = p_0 + \lambda \tilde{y}$.
   - Informed trader aggressiveness: $\beta(\sigma_\varepsilon) = \frac{\sigma_u}{\sigma_v} \cdot \frac{1}{\sqrt{1 + \frac{\sigma_\varepsilon^2}{\sigma_u^2}}}$.
   - Price impact coefficient: $\lambda(\sigma_\varepsilon) = \frac{\sigma_v}{2\sigma_u} \cdot \sqrt{1 + \frac{\sigma_\varepsilon^2}{\sigma_u^2}}$.
   - **Reciprocal Invariance:** The product of informed aggressiveness and price impact remains invariant to noise intensity:
     $$\lambda(\sigma_\varepsilon) \cdot \beta(\sigma_\varepsilon) = \frac{1}{2}$$
3. **The Privacy Subsidy:**
   - Because the market maker sets clearing price $p(\tilde{y}) = p_0 + \lambda(y + \varepsilon)$ but settles actual volume $y$, the expected single-period profit of the market maker is strictly negative:
     $$\mathbb{E}[\Pi_{\text{MM}}] = \mathbb{E}[(p(\tilde{y}) - v) \cdot y] = -\lambda \sigma_\varepsilon^2 = -\frac{\sigma_v}{2\sigma_u} \sqrt{1 + \frac{\sigma_\varepsilon^2}{\sigma_u^2}} \cdot \sigma_\varepsilon^2 < 0$$
   - This negative expected value represents a direct wealth transfer from liquidity providers to traders—the **Privacy Subsidy** $\mathcal{S}(\sigma_\varepsilon) = \lambda(\sigma_\varepsilon) \sigma_\varepsilon^2$.
   - For small privacy noise ($\sigma_\varepsilon \ll \sigma_u$), the subsidy scales quadratically: $\mathcal{S} \approx \frac{\sigma_v}{2\sigma_u} \sigma_\varepsilon^2$.
4. **Analogy to Loss-Versus-Rebalancing (LVR):** Nakamura shows that while LVR measures LP adverse selection due to temporal price staleness ($\Delta t > 0$), the Privacy Subsidy measures LP adverse selection due to signal noise coarseness ($\sigma_\varepsilon > 0$).

### Research interpretation

The falsifiable thesis is an **adverse-selection-compensated market making and fee-setting mechanism for privacy-preserving crypto markets**:
1. **Dynamic Break-Even Quoting Spread:** A rational market maker on a shielded exchange cannot quote symmetric tight spreads. To break even against the privacy subsidy, the market maker must widen their baseline half-spread $s_{\text{MM}}$ or demand a protocol rebate equal to:
   $$s_{\text{MM}}^*(\sigma_\varepsilon) = \frac{\mathcal{S}(\sigma_\varepsilon)}{\mathbb{E}[|y|]} = \frac{\lambda(\sigma_\varepsilon) \sigma_\varepsilon^2}{\sqrt{\frac{2}{\pi} (\beta^2 \sigma_v^2 + \sigma_u^2)}} = \frac{\sigma_v \sigma_\varepsilon^2 \sqrt{\pi}}{2 \sqrt{2} \sigma_u^2}$$
2. **Adverse Selection Exploitation:** If a privacy-preserving venue subsidizes noise without charging this minimum fee, external statistical arbitrageurs can systematically exploit the pricing error $\lambda \varepsilon$ by sending offsetting flows on transparent CEX venues.

## Signal

### Mathematical Valuation & Spread Formulation

Given market parameters $(\sigma_v, \sigma_u, \sigma_\varepsilon, p_0)$:

1. **Equilibrium Constants:**
   $$\eta = \sqrt{1 + \frac{\sigma_\varepsilon^2}{\sigma_u^2}}$$
   $$\beta = \frac{\sigma_u}{\sigma_v \eta}$$
   $$\lambda = \frac{\sigma_v \eta}{2 \sigma_u}$$

2. **Per-Trade Break-Even Surcharge / Minimum Half-Spread:**
   $$\text{Subsidy Rate (USD per period)} = \lambda \cdot \sigma_\varepsilon^2 = \frac{\sigma_v \eta \sigma_\varepsilon^2}{2 \sigma_u}$$
   $$\text{Break-Even Fee (bps)} = \frac{\text{Subsidy Rate}}{\mathbb{E}[\text{Volume}]} \times 10^4 = \frac{\sigma_v \sigma_\varepsilon^2 \sqrt{\pi}}{2 \sqrt{2} \sigma_u^2 \cdot p_0} \times 10^4$$

3. **Optimal Quoting Policy for Automated Market Makers:**
   - Quoted Bid: $P_{\text{bid}}(\tilde{y}) = p_0 + \lambda \tilde{y} - s_{\text{MM}}^*(\sigma_\varepsilon)$
   - Quoted Ask: $P_{\text{ask}}(\tilde{y}) = p_0 + \lambda \tilde{y} + s_{\text{MM}}^*(\sigma_\varepsilon)$

### Algorithmic Implementation Architecture

```python
import math
import dataclasses
from typing import Dict

@dataclasses.dataclass
class PrivacySubsidyEquilibrium:
    noise_ratio: float
    beta_informed_intensity: float
    lambda_price_impact: float
    invariant_beta_lambda_product: float
    per_period_privacy_subsidy_usd: float
    break_even_half_spread_bps: float

def compute_privacy_subsidy_equilibrium(
    spot_price: float,
    sigma_v_asset_vol: float,
    sigma_u_noise_flow_vol: float,
    sigma_eps_privacy_noise_vol: float
) -> PrivacySubsidyEquilibrium:
    """
    Computes closed-form Kyle equilibrium and break-even privacy subsidy
    under Nakamura (2026) noise-perturbed order flow framework.
    """
    assert spot_price > 0 and sigma_v_asset_vol > 0 and sigma_u_noise_flow_vol > 0, "Parameters must be positive"
    assert sigma_eps_privacy_noise_vol >= 0, "Privacy noise must be non-negative"

    # Noise ratio eta
    noise_variance_ratio = (sigma_eps_privacy_noise_vol ** 2) / (sigma_u_noise_flow_vol ** 2)
    eta = math.sqrt(1.0 + noise_variance_ratio)

    # Informed trader aggressiveness beta
    beta = sigma_u_noise_flow_vol / (sigma_v_asset_vol * eta)

    # Price impact coefficient lambda
    lambda_impact = (sigma_v_asset_vol * eta) / (2.0 * sigma_u_noise_flow_vol)

    # Theoretical invariant product
    invariant_prod = beta * lambda_impact

    # Per-period dollar transfer from LPs to traders (Privacy Subsidy)
    privacy_subsidy_usd = lambda_impact * (sigma_eps_privacy_noise_vol ** 2)

    # Expected order flow volume E[|y|]
    # Var[y] = beta^2 * sigma_v^2 + sigma_u^2 = sigma_u^2 / eta^2 + sigma_u^2 = sigma_u^2 * (1 + 1/eta^2)
    var_y = (beta ** 2) * (sigma_v_asset_vol ** 2) + (sigma_u_noise_flow_vol ** 2)
    expected_abs_volume = math.sqrt(2.0 * var_y / math.pi)

    # Break-even half spread in basis points
    break_even_spread_usd = privacy_subsidy_usd / expected_abs_volume if expected_abs_volume > 0 else 0.0
    break_even_half_spread_bps = (break_even_spread_usd / spot_price) * 10000.0

    return PrivacySubsidyEquilibrium(
        noise_ratio=eta,
        beta_informed_intensity=beta,
        lambda_price_impact=lambda_impact,
        invariant_beta_lambda_product=invariant_prod,
        per_period_privacy_subsidy_usd=privacy_subsidy_usd,
        break_even_half_spread_bps=break_even_half_spread_bps
    )
```

## Required data

- **Shielded Venue Microstructure Feed:** Aggregated noisy batch order flow $\tilde{y}_t$, settlement volume logs $y_t$, and protocol privacy noise configuration $\sigma_\varepsilon$ from target ZK-Rollup / shielded DEX contracts.
- **Underlying High-Frequency Volatility ($\sigma_v$):** Binance / Coinbase 1-second mark price tick data to calibrate fundamental asset drift variance $\sigma_v^2$.
- **Uninformed Flow Variance ($\sigma_u$):** Historical retail trade volume distributions on baseline transparent venues to estimate natural noise trader dispersion $\sigma_u^2$.

## Execution assumptions

- **Settlement Dynamics:** Protocol batches transactions over epoch $\Delta t$ and publishes noisy order flow $\tilde{y}$; trades settle atomically at price $P(\tilde{y})$.
- **Market Maker Inventory:** Single-period terminal liquidation or continuous inventory neutralization via external liquid CEX order books.
- **Zero Fixed Frictions:** Assumes zero protocol gas tax; all spread requirements derive strictly from adverse selection and privacy noise.

## Evidence

### Source-reported

- Yuki Nakamura (arXiv:2605.15746v2, May 2026) proves analytically:
  1. **Unique Linear Kyle Equilibrium:** Establishes the existence of a unique linear Bayesian equilibrium where price impact $\lambda(\sigma_\varepsilon) = \frac{\sigma_v}{2\sigma_u} \sqrt{1 + \frac{\sigma_\varepsilon^2}{\sigma_u^2}}$ increases monotonically with privacy noise variance $\sigma_\varepsilon^2$.
  2. **Product Invariance:** Proves that $\beta(\sigma_\varepsilon) \cdot \lambda(\sigma_\varepsilon) \equiv \frac{1}{2}$ holds identically for all noise levels $\sigma_\varepsilon \ge 0$, exactly preserving Kyle's classical informational efficiency ratio.
  3. **Closed-Form Privacy Subsidy:** Formally derives the exact transfer $\mathcal{S}(\sigma_\varepsilon) = \lambda \sigma_\varepsilon^2$, establishing that liquidity provision in privacy-preserving venues experiences an irreducible adverse selection loss quadratic in noise magnitude ($\mathcal{S} \sim \mathcal{O}(\sigma_\varepsilon^2)$) for small perturbations.

### Independently reproduced

- `not independently reproduced`.

### Negative evidence

- **Liquidity Death Spiral:** If protocol designers fail to implement the analytical break-even fee $s_{\text{MM}}^*(\sigma_\varepsilon)$, rational liquidity providers withdraw capital, causing $\sigma_u \to 0$, which causes price impact $\lambda \to \infty$ and collapses pool liquidity.
- **Adversarial Noise Estimation:** If informed traders can learn the realization of the privacy noise $\varepsilon$ before block settlement (e.g., via side-channel timing or mempool inspection), the privacy subsidy loss increases beyond the theoretical Gaussian bound.

## Falsification plan

1. **Simulation Verification:** Implement a Monte Carlo agent-based model simulating informed Bayesian traders, uninformed zero-intelligence traders, and a competitive market maker across varying noise levels $\sigma_\varepsilon \in [0, 5 \sigma_u]$.
2. **Empirical Falsification Rules:**
   - If empirical market maker PnL does not converge to $-\lambda \sigma_\varepsilon^2$ within $\pm 5\%$ across $10^6$ simulated batches, reject the analytical privacy subsidy formula.
   - If an automated market maker quoting the analytical spread $s_{\text{MM}}^*(\sigma_\varepsilon)$ suffers persistent negative net returns after $10^5$ trades against informed flow, reject the break-even compensation hypothesis.

## Crypto portability

- **Portability:** `direct`.
- **Domain Focus:** Directly targets the design and quantitative market making of privacy-preserving decentralized exchanges, ZK-Rollup dark pools, and shielded AMM protocols on Ethereum, Aztec, and Penumbra.

## Limitations

- `not independently reproduced`;
- **Gaussian Noise Assumption:** Closed-form solutions assume Gaussian privacy noise; discrete laplacian noise (used in standard differential privacy) introduces truncation bounds that require numerical integration;
- **Single-Period Framework:** While extended to continuous time in Nakamura (2026b), multi-period inventory persistence introduces dynamic hedging costs.

## Implementation status

- `not-implemented`. Research capture only; no live market maker or smart contract modules created.

## Adoption boundary

- `research-only`, `not-approved`.
- This record provides a mathematical foundation for market making on privacy-preserving venues. It does not authorize live deployment.

## Related Wiki records

- `[[quant/crypto-high-frequency-kyles-lambda-price-impact-reversal-2026-08-31]]`
- `[[quant/crypto-volume-synchronized-probability-of-toxicity-vpin-microstructure-2026-08-31]]`
- `[[quant/crypto-multilevel-order-flow-imbalance-intraday-2026-08-31]]`
- `[[quant/hawkes-driven-otc-market-making-volterra-riccati-2026-09-01]]`

## Sources

1. Yuki Nakamura, "The Privacy Subsidy: Kyle's $\lambda$ under Noise-Perturbed Order-Flow Observation", *arXiv preprint arXiv:2605.15746v2 [q-fin.TR, q-fin.MF]*, May 2026. DOI: [10.48550/arXiv.2605.15746](https://doi.org/10.48550/arXiv.2605.15746). URL: [https://arxiv.org/abs/2605.15746](https://arxiv.org/abs/2605.15746).
2. Yuki Nakamura, "The Privacy Subsidy in Continuous-Time Kyle: Cumulative Welfare under Noise-Perturbed Order-Flow Observation", *arXiv preprint arXiv:2605.25631v1 [q-fin.TR]*, May 2026. DOI: [10.48550/arXiv.2605.25631](https://doi.org/10.48550/arXiv.2605.25631). URL: [https://arxiv.org/abs/2605.25631](https://arxiv.org/abs/2605.25631).
