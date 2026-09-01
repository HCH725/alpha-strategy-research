---
schema: strategy-research-record-v1
title: "Constant Function Market Maker (CFMM) Arbitrage-Free Valuation and Delta-Hedging via Price-Intrinsic Liquidity Coordinates and Carr-Madan Option Spanning"
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - amm
  - cfmm
  - carr-madan
  - options-replication
  - delta-hedging
  - impermanent-loss
  - lvr
  - volatility-smile
status: research-only
confidence: high
source_as_of: 2026-03
sources:
  - "Jimmy Risk, Shen-Ning Tung, Tai-Ho Wang, 'Pricing and hedging for liquidity provision in Constant Function Market Making', arXiv:2603.01344v1 [q-fin.MF], March 2026. https://arxiv.org/abs/2603.01344"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Constant Function Market Maker (CFMM) Arbitrage-Free Valuation and Delta-Hedging via Price-Intrinsic Liquidity Coordinates and Carr-Madan Option Spanning

## Provenance

- **Primary Source:** Jimmy Risk (Cal Poly Pomona), Shen-Ning Tung (National Tsing Hua University), and Tai-Ho Wang (Baruch College, CUNY), "Pricing and hedging for liquidity provision in Constant Function Market Making", *arXiv preprint arXiv:2603.01344v1 [q-fin.MF]*, March 2026. URL: [https://arxiv.org/abs/2603.01344](https://arxiv.org/abs/2603.01344).
- **Related Foundational Literature:**
  - P. Carr and D. Madan (2001), "Towards a theory of volatility trading", *Option Valuation: Analysis and New Developments*, pp. 417–427.
  - A. Adams et al. (2021), "Uniswap v3 Core", Technical Whitepaper.
  - J. Milionis, C. C. Moallemi, T. Roughgarden, and A. L. Zhang (2022), "Automated Market Making and Loss-Versus-Rebalancing", *arXiv:2208.06046*.
  - S. F. Singh et al. (2025), "Modeling Loss-Versus-Rebalancing in Automated Market Makers via Continuous-Installment Options", *AFT 2025*, LIPIcs Vol. 327.
- **Context:** Automated Market Maker liquidity provision has traditionally been analyzed in token reserve coordinates $(x, y)$, obscuring the financial relationship between liquidity, price volatility, and option-theoretic hedging. Risk, Tung, and Wang (2026) introduce a coordinate transformation to marginal price $p$ and intrinsic liquidity $\lambda$, proving that bonding curves, reserve curves, and pool value functions are strictly linear in $\lambda$. This enables analytical Carr-Madan decomposition of Impermanent Loss (IL) into continuous strips of European options and exact dynamic delta-hedging calibrated to external Deribit volatility surfaces.

## Economic mechanism

### Source-reported

1. **Coordinate System Transformation:** Rather than parameterizing Constant Function Market Makers (CFMMs) by token reserves $(x_1, \dots, x_n) \in \mathbb{R}_+^n$ subject to $F(x) = k$, the bonding curve is canonically mapped to marginal exchange price $p$ and intrinsic liquidity scale parameter $\lambda$. For any homogeneous trading function $F$, token reserves decompose linearly:
   $$x(p, \lambda) = \lambda \cdot \phi_x(p), \quad y(p, \lambda) = \lambda \cdot \phi_y(p)$$
   where $\phi_x(p)$ and $\phi_y(p)$ are scale-invariant shape functions determined solely by the invariant curve geometry (e.g., constant product $xy=k$ or concentrated liquidity bounds $[p_a, p_b]$).
2. **Linear Value Function:** The mark-to-market value of a liquidity provider's position at spot price $p$ is strictly linear in intrinsic liquidity:
   $$V(p, \lambda) = x(p, \lambda) \cdot p + y(p, \lambda) = \lambda \cdot \psi(p)$$
   where $\psi(p) = p \phi_x(p) + \phi_y(p)$ represents the normalized unit value profile.
3. **Carr-Madan Spanning of Impermanent Loss:** Because $\psi(p)$ is concave in $p$ ($\psi''(p) < 0$), the payoff of holding an AMM LP position relative to a buy-and-hold benchmark is analytically replicated by a static portfolio of European options via the Carr-Madan formula:
   $$V(S_T, \lambda) = V(S_0, \lambda) + \Delta_0(S_T - S_0) - \int_0^{S_0} \omega(K) (K - S_T)^+ dK - \int_{S_0}^\infty \omega(K) (S_T - K)^+ dK$$
   where the continuous option weight density $\omega(K)$ is given precisely by the second derivative of the pool value function:
   $$\omega(K) = -\frac{\partial^2 V(K, \lambda)}{\partial K^2} = -\lambda \psi''(K) > 0$$
4. **Path-Dependent Last-Passage Time & LVR Connection:** Risk, Tung, and Wang link the accumulated divergence between hedged LP value and fee revenue to the last-passage time distribution of the price process, reinterpreting Loss-Versus-Rebalancing (LVR) as the cost of continuously rolling the delta-replicating option portfolio across discrete blocks.

### Research interpretation

The falsifiable thesis is an **on-chain liquidity provision valuation and automated delta-neutral volatility harvesting mechanism**:
1. **Implied Volatility Surface Calibration:** By equating the expected fee yield of a CFMM pool to the Carr-Madan option strip cost, one can extract the "CFMM-implied volatility smile" $\sigma_{\text{CFMM}}(K)$. When $\sigma_{\text{CFMM}}(K) > \sigma_{\text{Deribit}}(K)$ (i.e., AMM trading fees exceed external option premia), an LP can capture a positive risk-adjusted volatility risk premium by providing liquidity in the CFMM while buying dynamic delta/gamma hedges on Deribit or CEX perpetuals.
2. **Analytical Delta-Hedging:** Because $V(p, \lambda) = \lambda \psi(p)$, the exact delta of the LP position is $\Delta(p) = \frac{\partial V}{\partial p} = \lambda \phi_x(p) + \lambda p \phi_x'(p) + \lambda \phi_y'(p) = \lambda \phi_x(p)$ (by the marginal pricing condition $p \phi_x' + \phi_y' = 0$). Hedging the LP position requires maintaining a short perpetual/futures position of exactly $-\lambda \phi_x(p)$ units of the base token.

## Signal

### Analytical Parameterization & Greeks for Uniswap v3

For a concentrated liquidity position with price range $[p_a, p_b]$ and intrinsic liquidity $\lambda = L$:

1. **Reserves Functions:**
   $$\phi_x(p) = \begin{cases} \frac{1}{\sqrt{p_a}} - \frac{1}{\sqrt{p_b}} & p < p_a \\ \frac{1}{\sqrt{p}} - \frac{1}{\sqrt{p_b}} & p_a \le p \le p_b \\ 0 & p > p_b \end{cases}$$
   $$\phi_y(p) = \begin{cases} 0 & p < p_a \\ \sqrt{p} - \sqrt{p_a} & p_a \le p \le p_b \\ \sqrt{p_b} - \sqrt{p_a} & p > p_b \end{cases}$$

2. **LP Position Value Profile $\psi(p)$:**
   $$\psi(p) = \begin{cases} p \left(\frac{1}{\sqrt{p_a}} - \frac{1}{\sqrt{p_b}}\right) & p < p_a \\ 2\sqrt{p} - \frac{p}{\sqrt{p_b}} - \sqrt{p_a} & p_a \le p \le p_b \\ \sqrt{p_b} - \sqrt{p_a} & p > p_b \end{cases}$$

3. **Option Density Weight $\omega(K)$ (Carr-Madan Spanning):**
   $$\omega(K) = -L \psi''(K) = \begin{cases} \frac{L}{2 K^{3/2}} & K \in [p_a, p_b] \\ 0 & \text{otherwise} \end{cases}$$

4. **Dynamic Greeks:**
   - **Delta:** $\Delta_{\text{LP}}(p) = L \cdot \left(\frac{1}{\sqrt{p}} - \frac{1}{\sqrt{p_b}}\right)$ for $p \in [p_a, p_b]$.
   - **Gamma:** $\Gamma_{\text{LP}}(p) = -\frac{L}{2 p^{3/2}} < 0$.
   - **Required Short Hedge:** $Q_{\text{hedge}}(p) = -L \left(\frac{1}{\sqrt{p}} - \frac{1}{\sqrt{p_b}}\right)$ perpetual contracts.

### Algorithmic Implementation Architecture

```python
import math
import dataclasses
from typing import Optional, Dict

@dataclasses.dataclass
class CfmmPositionValuation:
    spot_price: float
    lower_tick_price: float
    upper_tick_price: float
    liquidity_l: float
    lp_value_usd: float
    lp_delta_base: float
    lp_gamma: float
    carr_madan_option_density: float
    target_perp_hedge_qty: float

def evaluate_cfmm_concentrated_position(
    spot_p: float,
    p_a: float,
    p_b: float,
    liquidity_l: float
) -> CfmmPositionValuation:
    """
    Computes analytical CFMM valuation, Greeks, Carr-Madan option density,
    and required perpetual delta hedge using Risk-Tung-Wang (2026) framework.
    """
    assert p_a < p_b, "Lower tick price must be strictly less than upper tick price"
    assert spot_p > 0 and liquidity_l > 0, "Price and liquidity must be positive"

    sqrt_p = math.sqrt(spot_p)
    sqrt_pa = math.sqrt(p_a)
    sqrt_pb = math.sqrt(p_b)

    if spot_p < p_a:
        # 100% token X (base asset)
        x_reserves = liquidity_l * ((1.0 / sqrt_pa) - (1.0 / sqrt_pb))
        y_reserves = 0.0
        val = spot_p * x_reserves
        delta = x_reserves
        gamma = 0.0
        option_density = 0.0
    elif spot_p > p_b:
        # 100% token Y (quote asset / USD)
        x_reserves = 0.0
        y_reserves = liquidity_l * (sqrt_pb - sqrt_pa)
        val = y_reserves
        delta = 0.0
        gamma = 0.0
        option_density = 0.0
    else:
        # Active in-range position
        x_reserves = liquidity_l * ((1.0 / sqrt_p) - (1.0 / sqrt_pb))
        y_reserves = liquidity_l * (sqrt_p - sqrt_pa)
        val = spot_p * x_reserves + y_reserves
        delta = x_reserves
        gamma = -liquidity_l / (2.0 * (spot_p ** 1.5))
        option_density = liquidity_l / (2.0 * (spot_p ** 1.5))

    # Required external delta hedge in perpetual futures
    target_hedge_qty = -delta

    return CfmmPositionValuation(
        spot_price=spot_p,
        lower_tick_price=p_a,
        upper_tick_price=p_b,
        liquidity_l=liquidity_l,
        lp_value_usd=val,
        lp_delta_base=delta,
        lp_gamma=gamma,
        carr_madan_option_density=option_density,
        target_perp_hedge_qty=target_hedge_qty
    )
```

## Required data

- **CFMM Pool State:** Uniswap v3 / Balancer on-chain state variables: `slot0` (current sqrt price, tick), active tick liquidity bitmap $L(t)$, pool fee tier $\gamma_{\text{fee}} \in \{5\text{ bps}, 30\text{ bps}, 100\text{ bps}\}$.
- **Centralized Perpetual / Spot Feeds:** High-frequency 1-second OHLCV + top-of-book depth from Binance/OKX/Coinbase to compute instantaneous delta hedge adjustments.
- **External Options Surface:** Deribit ETH/BTC implied volatility surface (interpolated across strikes $K \in [p_a, p_b]$ and tenors $T \in [1\text{d}, 30\text{d}]$) to assess whether CFMM fee yields exceed Black-Scholes replication costs.
- **Gas / On-Chain Transaction Costs:** Base fee + priority fee tracking on Ethereum mainnet or Arbitrum to evaluate rebalancing friction.

## Execution assumptions

- **Delta Rebalancing Cadence:** Rebalance external perpetual hedge when $|\Delta_{\text{actual}} - \Delta_{\text{target}}| / \Delta_{\text{target}} > \tau_{\text{rebal}}$ (typical threshold $\tau_{\text{rebal}} = 5\%$) or on periodic 15-minute intervals.
- **Execution Venue for Hedge:** Binance / OKX / Hyperliquid perpetual futures using maker/taker limit orders with fee assumptions of $\le 2\text{ bps}$ taker.
- **Slippage & Funding:** Spot-perpetual basis and funding rate costs must be factored into continuous hedging drag.

## Evidence

### Source-reported

- Risk, Tung, and Wang (arXiv:2603.01344v1, March 2026) report:
  1. **Linearity Verification:** Proves that for all homogeneous CFMM trading functions $F(x) = k$, value functions satisfy $V(p, \lambda) = \lambda \psi(p)$, ensuring dimensional consistency and eliminating non-linear reserve scaling artifacts.
  2. **Empirical Smile Consistency:** Calibrating the Carr-Madan option density to Uniswap v3 ETH/USDC pool data (0.05% and 0.30% fee tiers) alongside Deribit ETH options data demonstrates that the CFMM-implied volatility smile exhibits consistent negative skew and volatility curvature matching institutional crypto options markets.
  3. **Path-Dependent Hedging Tracking:** Applying the last-passage time analytical bounds reduces hedging tracking error relative to standard discrete Black-Scholes daily delta rebalancing by over **$25\%$** during high-volatility market regimes.

### Independently reproduced

- `not independently reproduced`.

### Negative evidence

- **Toxic Flow & LVR Asymmetry:** When toxic flow (arbitrageurs trading against stale oracle prices) dominates uninformed retail swap volume, pool fee income fails to cover the option premium implied by Carr-Madan spanning, resulting in net negative returns even with perfect delta hedging.
- **Rebalancing Gas Drag on L1:** On Ethereum L1, high gas fees during volatility spikes make continuous delta rebalancing prohibitively expensive, requiring wider no-trade bands that increase unhedged gamma risk.

## Falsification plan

1. **Backtest Design:** Simulate a delta-hedged Uniswap v3 ETH/USDC LP strategy across 2023–2026 using historical on-chain swap logs and Binance ETH-USDT perpetual order flow.
2. **Ablation & Benchmark:** Compare (a) unhedged LP, (b) naive daily Black-Scholes hedged LP, and (c) Risk-Tung-Wang Carr-Madan intrinsic-liquidity hedged LP.
3. **Falsification Thresholds:**
   - If the Carr-Madan intrinsic-liquidity hedge fails to reduce portfolio variance by at least **$50\%$** compared to the unhedged LP baseline across the full out-of-sample test, reject the risk-reduction hypothesis.
   - If net return after fees and perpetual rebalancing costs is strictly negative over 6 consecutive months in low-volatility regimes, reject the volatility harvesting thesis.

## Crypto portability

- **Portability:** `direct`.
- **Domain Focus:** Native to decentralized exchange AMMs (Uniswap v3, Balancer) and crypto derivatives venues (Deribit, Binance Futures, Hyperliquid).

## Limitations

- `not independently reproduced`;
- **Jump Risk:** Carr-Madan static replication assumes continuous price paths; discontinuous jumps through tick ranges $[p_a, p_b]$ incur slippage and unhedged gap losses;
- **Funding Rate Drag:** Sustained positive or negative funding rates on perpetual hedges can erode fee yields over long holding periods.

## Implementation status

- `not-implemented`. Research capture only; no live or testnet execution modules.

## Adoption boundary

- `research-only`, `not-approved`.
- This record captures theoretical and empirical research on AMM pricing and delta hedging. It does not constitute trading authorization.

## Related Wiki records

- `[[quant/defi-amm-continuous-installment-options-lvr-delta-hedge-2026-09-01]]`
- `[[quant/defi-amm-amortizing-perpetual-options-lvr-hedge-2026-09-01]]`
- `[[quant/crypto-uniswap-v3-just-in-time-jit-liquidity-provision-price-impact-2026-09-01]]`
- `[[quant/defi-amm-jump-diffusion-lvr-decomposition-optimal-block-time-2026-09-01]]`

## Sources

1. Jimmy Risk, Shen-Ning Tung, Tai-Ho Wang, "Pricing and hedging for liquidity provision in Constant Function Market Making", *arXiv preprint arXiv:2603.01344v1 [q-fin.MF]*, March 2026. DOI: [10.48550/arXiv.2603.01344](https://doi.org/10.48550/arXiv.2603.01344). URL: [https://arxiv.org/abs/2603.01344](https://arxiv.org/abs/2603.01344).
