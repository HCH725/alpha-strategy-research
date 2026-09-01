---
schema: strategy-research-record-v1
title: "Amortizing Perpetual Options (AmPOs): Fungible Continuous-Installment Derivatives for On-Chain Volatility Trading and AMM Loss-Versus-Rebalancing Hedging"
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - options
  - perpetual-options
  - continuous-installment-options
  - amortizing-options
  - amm
  - lvr
  - volatility-trading
  - risk-neutral-valuation
status: research-only
confidence: high
source_as_of: 2026-07
sources:
  - "Zachary Feinstein, 'Amortizing Perpetual Options', arXiv:2512.06505v4 [q-fin.PR], December 2025 (revised May 2026). Published in SIAM Journal on Financial Mathematics, Vol. 17, No. 3, July 2026. https://arxiv.org/abs/2512.06505"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Amortizing Perpetual Options (AmPOs): Fungible Continuous-Installment Derivatives for On-Chain Volatility Trading and AMM Loss-Versus-Rebalancing Hedging

## Provenance

- **Primary Source:** Zachary Feinstein (Stevens Institute of Technology / School of Business), "Amortizing Perpetual Options", *arXiv preprint arXiv:2512.06505v4 [q-fin.PR]*, first submitted December 2025; revised May 2026. Published as Short Communication in *SIAM Journal on Financial Mathematics (SIFIN)*, Vol. 17, No. 3, July 2026. URL: [https://arxiv.org/abs/2512.06505](https://arxiv.org/abs/2512.06505).
- **Related Foundational Works:**
  - P. Ciurlia and I. Roko (2005), "Valuation of American continuous-installment options", *Computational Economics*, 25(1), pp. 143–165.
  - D. Ackerer, J. Hugonnier, and U. Jermann (2023), "Perpetual futures pricing", *Mathematical Finance*, 34(2).
  - G. Angeris, T. Chitra, A. Evans, and M. Lorig (2023), "A primer on perpetuals", *SIAM Journal on Financial Mathematics*, 14(1), pp. SC17–SC30.
  - S. F. Singh et al. (2025), "Modeling Loss-Versus-Rebalancing in Automated Market Makers via Continuous-Installment Options", *AFT 2025*, LIPIcs Vol. 327.
- **Context:** Continuous-installment (CI) options provide non-linear payoff structures without fixed expirations, but traditional CI contracts lapse when holders fail to pay explicit cash installments, creating non-fungible contracts unsuitable for decentralized exchange (DEX) order books and AMMs. Feinstein (2025/2026) solves this by replacing explicit installment payments with an implicit deterministic decay of the claimable notional ($N_t = N_0 e^{-qt}$), creating the first fully fungible perpetual option design with a positive cost-of-carry.

## Economic mechanism

### Source-reported

1. **Failure of Traditional Installment Options on Exchanges:** Standard continuous-installment (CI) options grant dual optionality (exercise or lapse). Because lapsing depends on idiosyncratic counterparty payment streams, individual contracts possess distinct payment histories and cannot trade as standardized, fungible ERC-20 tokens on central limit order books (CLOBs) or AMMs.
2. **Implicit Payment via Notional Amortization:** An Amortizing Perpetual Option (AmPO) funds the continuous installment stream $c_t N_t dt$ by continuously selling a fraction of the option notional back to the pool/underwriter at current market premium $V_t$. For an exogenous amortization rate $q_t \ge 0$, the claimable notional decays exponentially:
   $$N_t = N_{t_0} \exp\left( -\int_{t_0}^t q_s ds \right)$$
3. **No Lapsing Rationality:** A rational holder never voluntarily cancels an AmPO ($V_t \ge 0$ always), eliminating discrete lapsing logic. When the option is deep out-of-the-money, notional decays continuously towards zero, creating an endogenous, smooth economic termination without requiring high-frequency oracle liquidations.
4. **Isomorphism to Dividend-Paying Perpetual American Options:** Feinstein proves that an AmPO with amortization rate $q$ is analytically isomorphic to a vanilla perpetual American option on an underlying asset with augmented risk-free rate $r + q$ and effective dividend yield $\delta + q$.

### Research interpretation

The falsifiable thesis is an **on-chain volatility harvesting and AMM Loss-Versus-Rebalancing (LVR) delta/gamma immunization mechanism**:
1. **Fungible Volatility Primitive:** Standardized AmPO tokens (e.g., canonical fixed rates $q \in \{3\text{ bps/day}, 10\text{ bps/day}, 50\text{ bps/day}\}$) can be traded on secondary DEX CLOBs and AMM liquidity pools without oracle dependency or liquidator gas auctions.
2. **LVR Hedging for Automated Market Makers:** Because AMM LP positions suffer from continuous adverse selection equivalent to short continuous-installment options (Singh et al., 2025), holding long AmPO options provides an exact gamma-replicating hedge that neutralizes LVR drag while remaining fully fungible on-chain.
3. **Optimal Volatility Positioning:** While call/put AmPO premia decrease monotonically in amortization rate $q$, positional Vega per dollar invested exhibits non-monotonic behavior, allowing quantitative option traders to construct budget-optimized directional and neutral volatility strategies with optimal $q^*$.

## Signal

### Analytical Pricing & Boundary Formulation

Under the Black-Scholes geometric Brownian motion framework ($dS_t = r S_t dt + \sigma S_t dW_t$) with constant amortization rate $q > 0$:

1. **Call AmPO Pricing:**
   - Characteristic root:
     $$\alpha_C = \sqrt{\left(\frac{r}{\sigma^2} + \frac{1}{2}\right)^2 + \frac{2q}{\sigma^2}} - \frac{r}{\sigma^2} + \frac{1}{2} > 1$$
   - Optimal exercise boundary:
     $$\bar{S}_C = \frac{\alpha_C K}{\alpha_C - 1}$$
   - Option premium ($S_0 \le \bar{S}_C$):
     $$C_0(S_0, K, r, \sigma, q) = \frac{K}{\alpha_C - 1} \left( \frac{(\alpha_C - 1) S_0}{\alpha_C K} \right)^{\alpha_C}$$

2. **Put AmPO Pricing:**
   - Characteristic root:
     $$\alpha_P = \sqrt{\left(\frac{r}{\sigma^2} + \frac{1}{2}\right)^2 + \frac{2q}{\sigma^2}} + \frac{r}{\sigma^2} - \frac{1}{2} > 0$$
   - Optimal exercise boundary:
     $$\bar{S}_P = \frac{\alpha_P K}{1 + \alpha_P}$$
   - Option premium ($S_0 \ge \bar{S}_P$):
     $$P_0(S_0, K, r, \sigma, q) = \frac{K}{1 + \alpha_P} \left( \frac{(1 + \alpha_P) S_0}{\alpha_P K} \right)^{-\alpha_P}$$

3. **Greeks & Economic Theta:**
   - **Economic Theta:** While nominal $\partial V_0 / \partial t = 0$ (perpetual contract), the economic time decay incurred by the holder is:
     $$\Theta_{\text{economic}} = -q V_0 < 0$$
   - **Positional Vega:**
     $$\nu_0 = \frac{\partial V_0}{\partial \sigma} = \frac{\partial V_0}{\partial \alpha} \frac{\partial \alpha}{\partial \sigma}$$
   - **Optimal Positional Leverage:** To maximize volatility exposure per dollar of collateral, maximize $\frac{\nu_0(q)}{V_0(q)}$ subject to target leverage.

### Algorithmic Implementation Architecture

```python
import math
import dataclasses
from typing import Tuple

@dataclasses.dataclass
class AmpoValuation:
    premium: float
    exercise_boundary: float
    economic_theta: float
    delta: float
    gamma: float
    vega: float
    effective_maturity_days: float

def price_call_ampo(
    s_price: float,
    k_strike: float,
    r_rate: float,
    sigma_vol: float,
    q_amortization: float
) -> AmpoValuation:
    """
    Computes analytical pricing, optimal exercise boundary, and Greeks
    for an Amortizing Perpetual Call Option (AmPO).
    """
    sigma_sq = sigma_vol ** 2
    drift_term = (r_rate / sigma_sq) + 0.5
    alpha_c = math.sqrt(drift_term ** 2 + (2.0 * q_amortization / sigma_sq)) - (r_rate / sigma_sq) + 0.5
    
    # Optimal exercise boundary
    s_bar_c = (alpha_c * k_strike) / (alpha_c - 1.0)
    
    if s_price >= s_bar_c:
        # Immediate exercise region
        premium = s_price - k_strike
        delta = 1.0
        gamma = 0.0
        vega = 0.0
    else:
        # Continuation region
        scaling = (alpha_c - 1.0) * s_price / (alpha_c * k_strike)
        premium = (k_strike / (alpha_c - 1.0)) * (scaling ** alpha_c)
        delta = (alpha_c / s_price) * premium
        gamma = (alpha_c * (alpha_c - 1.0) / (s_price ** 2)) * premium
        
        # Positional Vega derivation
        d_alpha_d_sigma = -(2.0 / sigma_vol) * (
            (drift_term * (r_rate / sigma_sq) + (2.0 * q_amortization / sigma_sq)) / 
            math.sqrt(drift_term ** 2 + (2.0 * q_amortization / sigma_sq)) - (r_rate / sigma_sq)
        )
        d_v_d_alpha = premium * (math.log(scaling) - (1.0 / (alpha_c - 1.0)))
        vega = d_v_d_alpha * d_alpha_d_sigma

    economic_theta = -q_amortization * premium
    # Approximate effective maturity in days (annualized basis)
    eff_maturity_days = (1.0 / q_amortization) * 365.0 if q_amortization > 0 else float('inf')

    return AmpoValuation(
        premium=premium,
        exercise_boundary=s_bar_c,
        economic_theta=economic_theta,
        delta=delta,
        gamma=gamma,
        vega=vega,
        effective_maturity_days=eff_maturity_days
    )
```

## Required data

- **Underlying Spot / Index Price ($S_t$):** High-integrity spot feed from liquid CEX/DEX aggregators (Binance, Coinbase, Chainlink oracle benchmarks).
- **Implied & Realized Volatility ($\sigma$):** Deribit BTC/ETH options implied volatility surface to calibrate benchmark pricing and comparative mispricings.
- **Risk-Free / Staking Yield ($r$):** Base staking yield or DeFi borrow rate (e.g., Aave/Compound USDC rate, Lido stETH yield).
- **DEX Smart Contract Pool State:** On-chain AMM reserves and secondary market order book depth for AmPO tokenized series.

## Execution assumptions

- **Fungible Token Standard:** AmPO contracts deployed as standardized ERC-20 tokens where balance $B_t = B_{t_0} e^{-q (t - t_0)}$ decays deterministically via rebasing or internal share accounting.
- **Physical vs. Cash Settlement:** Exercise settles atomically via smart contract against pooled collateral (USDC or underlying crypto asset).
- **Transaction Costs:** Standard EVM/L2 gas costs on trade submission and atomic redemption; no continuous installment gas overhead.

## Evidence

### Source-reported

- Feinstein (2025/2026) establishes:
  1. **Fixed-Point Uniqueness:** Proves the AmPO value process is the unique fixed point of the continuous-installment operator $\mathcal{C}$ in class $\mathbb{V}$.
  2. **Numerical Case Study ($r = 5\%$, $\sigma = 50\%$, $S_0 = 100$, $K = 100$ ATM Call):**
     - **Notional Retention:** At the effective maturity date $T_{\text{eff}}$ (where dated American option premium equals AmPO premium), the AmPO retains over **$65\%$** of its original claimable notional even under high amortization rates ($q \approx 1.0$), demonstrating substantial residual optionality relative to expired dated options.
     - **Safety Ratio (Gamma Stability):** The ratio of AmPO Gamma to dated American option Gamma ($\Gamma_0 / \Gamma_A$) remains below **$80\%$** across all amortization rates, providing greater price stability against sharp underlying spot fluctuations.
     - **Cost Efficiency (Theta Ratio):** The ratio of AmPO economic Theta to dated American Theta ($-q C_0 / \Theta_A$) remains strictly below **$80\%$**, proving that AmPO notional decay is more cost-effective than standard time decay in dated options.
     - **Optimal Bearish Volatility Leverage:** For an ATM put with budget constraint $\$100$, the optimal amortization rate that maximizes positional Vega is precisely **$q^* \approx 19.26\%$** per annum.

### Independently reproduced

- `not independently reproduced`.

### Negative evidence

- **Endogenous Rate Manipulation Vulnerability:** If amortization $q_t = c / V_t$ is made dependent on option market price $V_t$ rather than fixed exogenously, a deep OTM option ($V_t \to 0$) experiences $q_t \to \infty$, triggering instant notional annihilation. Malicious traders could manipulate spot or pool prices to zero out long open interest. Exogenous fixed rates ($q \equiv \text{const}$) are required to eliminate this exploit vector.
- **Rebasing Token Friction:** Managing exponential token supply decay on Layer-1 or Layer-2 AMMs requires specialized rebase-aware automated market makers (similar to stETH / AMPL pools) to avoid routing rounding errors.

## Falsification plan

1. **Backtest Design:** Simulate AmPO portfolios across historical BTC and ETH price histories (2020–2026), comparing delta-hedged AmPO portfolios against standard rolling Deribit 30-day dated options.
2. **AMM LVR Hedge Test:** Apply long AmPO puts/calls to hedge a Uniswap v3 ETH/USDC 0.05% concentrated liquidity pool.
3. **Falsification Thresholds:**
   - If the delta-hedged AmPO strategy incurs higher cumulative turnover costs and hedging slippage than standard rolling dated options over a 12-month backtest, reject the cost-efficiency hypothesis.
   - If fixed-rate AmPO hedging fails to reduce AMM LP variance and LVR by at least $40\%$ relative to an unhedged LP position, reject the LVR immunization claim.

## Crypto portability

- **Portability:** `direct`.
- **Crypto Domain Alignment:** Engineered directly for decentralized finance protocols, solving the core barrier that prevented continuous-installment derivatives from trading on blockchain order books (DEXs) and AMM liquidity pools.

## Limitations

- **not independently reproduced**;
- **Black-Scholes Volatility Assumption:** Analytical closed-form formulas assume constant volatility $\sigma$ and continuous diffusion; stochastic volatility or jump-diffusion extensions require numerical PDEs;
- **Secondary Market Liquidity:** AmPO liquidity requires standardizing a small set of canonical amortization tiers ($q$) to avoid liquidity fragmentation across strikes.

## Implementation status

- `not-implemented`. Research capture only; no PyBroker or NautilusTrader execution modules created.

## Adoption boundary

- `research-only`, `not-approved`.
- This record provides a mathematical foundation for tokenized perpetual option derivatives and AMM hedging research. It does not authorize live or testnet deployment.

## Related Wiki records

- `[[quant/defi-amm-continuous-installment-options-lvr-delta-hedge-2026-09-01]]`
- `[[quant/defi-everlasting-options-proactive-market-making-delta-hedge-2026-09-01]]`
- `[[quant/crypto-options-volatility-risk-premium-zscore-2026-08-31]]`
- `[[quant/defi-amm-jump-diffusion-lvr-decomposition-optimal-block-time-2026-09-01]]`

## Sources

1. Zachary Feinstein, "Amortizing Perpetual Options", *arXiv preprint arXiv:2512.06505v4 [q-fin.PR]*, December 2025 (revised May 2026). DOI: [10.48550/arXiv.2512.06505](https://doi.org/10.48550/arXiv.2512.06505). URL: [https://arxiv.org/abs/2512.06505](https://arxiv.org/abs/2512.06505).
2. Zachary Feinstein, "Amortizing Perpetual Options", *SIAM Journal on Financial Mathematics*, Vol. 17, No. 3, pp. SC1–SC14, July 2026. DOI: [10.1137/25M1632145](https://doi.org/10.1137/25M1632145).
