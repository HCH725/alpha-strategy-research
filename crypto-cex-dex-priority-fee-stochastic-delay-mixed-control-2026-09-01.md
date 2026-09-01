---
schema: strategy-research-record-v1
title: Mixed Continuous-Impulse Control for Cross-Venue CEX-DEX Statistical Arbitrage with Stochastic Execution Delays and Endogenous Priority Fees
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cex-dex
  - latency-arbitrage
  - priority-fees
  - impulse-control
  - viscosity-solutions
  - statistical-arbitrage
  - market-microstructure
status: research-only
confidence: high
source_as_of: 2026-02
sources:
  - "Philippe Bergault, Yadh Hafsi, and Leandro Sánchez-Betancourt, 'Trading in CEXs and DEXs with Priority Fees and Stochastic Delays', arXiv:2602.10798v2 [q-fin.TR], February 2026. Oxford Working Papers in Mathematical and Computational Finance (MCF 26-03). https://arxiv.org/abs/2602.10798"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Mixed Continuous-Impulse Control for Cross-Venue CEX-DEX Statistical Arbitrage with Stochastic Execution Delays and Endogenous Priority Fees

## Provenance

- **Primary Source:** Philippe Bergault, Yadh Hafsi, and Leandro Sánchez-Betancourt (Imperial College London / Oxford-Man Institute / University of Oxford), "Trading in CEXs and DEXs with Priority Fees and Stochastic Delays", *arXiv preprint arXiv:2602.10798v2 [q-fin.TR]*, first submitted February 11, 2026; revised February 19, 2026. URL: [https://arxiv.org/abs/2602.10798](https://arxiv.org/abs/2602.10798). Also published as *Oxford Working Papers in Mathematical and Computational Finance*, Report No. MCF 26-03.
- **Foundational Lineage:**
  - B. Bruder and H. Pham (2009), "Impulse control problem on finite horizon with execution delay", *Stochastic Processes and their Applications*, 119(5), pp. 1436–1469.
  - Á. Cartea, F. Drissi, and M. Monga (2023), "Execution and statistical arbitrage with signals in multiple automated market makers", *IEEE ICDCSW 2023*, pp. 37–42.
  - A. Capponi, R. Jia, and S. Yu (2026), "Price discovery on decentralized exchanges", *The Review of Financial Studies*, hhag002.
- **Empirical Calibration Data:** Model parameters calibrated using high-frequency ETH-USDC market data across Binance (CEX) and Uniswap v3/v2 (DEX), evaluating optimal execution over finite time horizons with multiple pending orders.

## Economic mechanism

### Source-reported

1. **Dual-Venue Microstructure Divergence:** In modern cryptocurrency markets, centralized exchanges (CEXs) operate continuous central limit order books (CLOBs) with sub-millisecond execution, while decentralized exchanges (DEXs / AMMs) execute trades discretely inside blocks subject to asynchronous, stochastic transaction confirmation delays.
2. **Controllable Latency via Priority Fees:** On decentralized exchanges (e.g., Ethereum, Arbitrum, Solana), liquidity takers face an endogenous trade-off between immediacy and execution risk: paying a higher priority fee $\mathfrak{p}_i$ to block builders/validators increases the arrival intensity $\ell_i$ (reducing the expected stochastic confirmation delay $\tau \sim \text{Exp}(\ell_i)$).
3. **Mixed Control Formulation:** The trader's problem combines:
   - An absolutely continuous control $\nu_t$, representing continuous inventory management and liquid hedging on the CEX.
   - A discrete impulse control sequence $(\tau_n, I_n, \xi_n)_{n \ge 1}$, representing discrete order submissions to the DEX with intervention time $\tau_n$, chosen priority fee tier $I_n \in \{1, \dots, N\}$, and signed trade volume $\xi_n \in [-\bar{V}, \bar{V}]$.
4. **Multiple Pending Orders:** The model accommodates up to $K$ simultaneous asynchronous pending orders undergoing independent Poisson confirmation processes, preventing inventory lockup while trades remain unconfirmed in the mempool/builder auction.

### Research interpretation

The falsifiable thesis is an **optimal latency-cost trade-off and inventory-constrained cross-venue statistical arbitrage mechanism**:
1. **Dynamic Exercise Boundary:** Dislocation between the CEX mid-price $S_t$ and the DEX pool price $Z_t$ triggers DEX impulse intervention only when $|S_t - Z_t|$ exceeds a state-dependent free boundary. When $|S_t - Z_t|$ is small, the trader continues purely with continuous CEX inventory unwinding.
2. **Strategic Priority Escalation:** When price dislocations $|S_t - Z_t|$ are large, the expected arbitrage surplus justifies paying top-tier priority fees to minimize execution delay and front-running/slippage risk. As dislocations shrink or time-to-horizon approaches maturity, optimal priority fees shift dynamically based on residual inventory penalty $\Xi (Q_T)^2$ and running inventory risk $\phi \int_t^T (Q_r)^2 dr$.
3. **Sub-optimality of Fixed Fees:** Heuristic fixed-priority fee selection or static gas bidding leads to severe fee overpayment on small dislocations and toxic execution delays on large dislocations.

## Signal

### Mathematical Specification

1. **State Dynamics:**
   - **CEX Reference Price ($S_t$):** Martingale diffusion representing efficient off-chain benchmark:
     $$dS_t = \sigma^S dW_t^S$$
   - **DEX Pool Price ($Z_t$):** Mean-reverting jump-diffusion capturing AMM price adjustment, noise trading, and endogenous execution impact:
     $$dZ_t = \kappa (S_t - Z_t) dt + \sigma^Z dW_t^Z + \sum_{\tilde{\tau}_n = t} h(\xi_n, Z_{\tilde{\tau}_n^-})$$
     where $\kappa > 0$ is the cross-venue arbitrage realignment rate, and $h(\xi, Z) = \psi(Z) \xi = \frac{2 Z^{3/2}}{d} \xi$ represents the price impact of a trade of size $\xi$ on an AMM with reserve depth $d$.
   - **Trader Inventory ($Q_t$):**
     $$Q_t = q + \int_0^t \nu_r dr + \sum_{\tilde{\tau}_n \le t} \xi_n$$
   - **Cash Process ($Y_t$):**
     $$dY_t = -\nu_t (S_t + k \nu_t) dt - \sum_{\tilde{\tau}_n = t} \left[ \xi_n \left( Z_{\tilde{\tau}_n^-} + \frac{Z_{\tilde{\tau}_n^-}^{3/2}}{d} \xi_n \right) + \mathfrak{p}_{I_n} \right]$$
     where $k > 0$ is the CEX quadratic execution cost parameter and $\mathfrak{p}_{I_n}$ is the priority fee.

2. **Performance Objective:**
   $$\max_{\alpha \in \mathcal{A}_K} \mathbb{E}\left[ \int_0^T \left( -\nu_t (S_t + k \nu_t) - \phi Q_t^2 \right) dt + Q_T S_T - \Xi (Q_T)^2 - \sum_{\tilde{\tau}_n \le T} c(\tilde{\tau}_n, Z_{\tilde{\tau}_n^-}, \xi_n, I_n) \right]$$
   where $c(t, z, \xi, i) = \xi \left( z + \frac{z^{3/2}}{d} \xi \right) + \mathfrak{p}_i$.

3. **Optimal Continuous CEX Trading Rate:**
   $$\nu^* = \frac{1}{2k} \left( \frac{\partial v}{\partial q} - S_t \right)$$

4. **HJB Quasi-Variational Inequality (HJB-QVI):**
   For pending order count $\sum_{i=1}^N \langle \mathfrak{i}, e_i \rangle < K$:
   $$\min\left\{ -\frac{\partial v}{\partial t} - \mathcal{L}^{\nu^*} v - \mathcal{J} v - f(t, y, \nu^*), \; v - \mathcal{M}v \right\} = 0$$
   where $\mathcal{M}$ is the non-local intervention operator:
   $$\mathcal{M}v(t, y) = \max_{i \in \{1, \dots, N\}, \, \xi \in [-\bar{V}, \bar{V}]} v(t, s, q, z, \mathfrak{i} + e_i, \mathfrak{v} + \xi e_i)$$
   and $\mathcal{J}$ is the pending-order Poisson execution jump operator:
   $$\mathcal{J}v(t, y) = \sum_{i=1}^N \mathbf{1}_{\{\langle \mathfrak{i}, e_i \rangle > 0\}} \ell_i \left( v(t, s, q + \xi_i, z + h(\xi_i, z), \mathfrak{i} - e_i, \mathfrak{v} - \xi_i e_i) - v(t, y) - c(t, z, \xi_i, i) \right)$$

### Algorithmic Execution Workflow

```python
import dataclasses
from typing import List, Tuple, Optional
import numpy as np

@dataclasses.dataclass
class CexDexOrderDecision:
    cex_continuous_rate: float       # Optimal trading rate nu* on CEX
    should_submit_dex_impulse: bool  # True if state enters impulse exercise region
    dex_target_volume: float        # Trade volume xi* for DEX
    dex_priority_tier: int          # Priority fee index I* in {1, ..., N}
    expected_delay_sec: float       # Expected latency 1 / ell_{I*}

def evaluate_cex_dex_policy(
    s_cex: float,
    z_dex: float,
    inventory_q: float,
    pending_orders_count: int,
    max_pending_k: int,
    k_cex_cost: float,
    d_dex_depth: float,
    value_gradient_dq: float,
    exercise_boundary_dislocation: float,
    fee_tiers: List[float],         # [p_1, p_2, ..., p_N]
    intensity_tiers: List[float],   # [ell_1, ell_2, ..., ell_N]
    max_trade_vol: float = 5.0
) -> CexDexOrderDecision:
    """
    Evaluates optimal CEX continuous rate and DEX impulse decision
    under mixed stochastic control with priority fee selection.
    """
    # 1. First-order optimal continuous CEX trading rate
    nu_star = (value_gradient_dq - s_cex) / (2.0 * k_cex_cost)
    
    # 2. Check if maximum pending orders reached
    if pending_orders_count >= max_pending_k:
        return CexDexOrderDecision(
            cex_continuous_rate=nu_star,
            should_submit_dex_impulse=False,
            dex_target_volume=0.0,
            dex_priority_tier=0,
            expected_delay_sec=0.0
        )
        
    # 3. Dislocation check against dynamic exercise boundary
    dislocation = s_cex - z_dex
    if abs(dislocation) < exercise_boundary_dislocation:
        # Inside continuation region: wait, do not submit DEX order
        return CexDexOrderDecision(
            cex_continuous_rate=nu_star,
            should_submit_dex_impulse=False,
            dex_target_volume=0.0,
            dex_priority_tier=0,
            expected_delay_sec=0.0
        )
        
    # 4. In exercise region: determine optimal direction, size, and priority tier
    direction = 1.0 if dislocation > 0 else -1.0
    target_xi = direction * min(max_trade_vol, abs(dislocation) * d_dex_depth / (4.0 * (z_dex ** 1.5)))
    
    # Select priority tier: higher dislocation and urgency -> higher intensity ell_i
    # For large dislocations, marginal surplus exceeds fee increment (p_{i+1} - p_i)
    if abs(dislocation) > 2.0 * exercise_boundary_dislocation:
        best_tier_idx = len(fee_tiers) - 1  # Maximum priority fee
    elif abs(dislocation) > 1.4 * exercise_boundary_dislocation:
        best_tier_idx = len(fee_tiers) // 2
    else:
        best_tier_idx = 0                  # Base priority fee
        
    expected_delay = 1.0 / intensity_tiers[best_tier_idx]
    
    return CexDexOrderDecision(
        cex_continuous_rate=nu_star,
        should_submit_dex_impulse=True,
        dex_target_volume=target_xi,
        dex_priority_tier=best_tier_idx + 1,
        expected_delay_sec=expected_delay
    )
```

## Required data

- **CEX Market Data:** High-frequency L2 order book quotes and trades for reference pair (e.g., Binance ETH/USDT, Coinbase ETH/USD) to compute $S_t$.
- **DEX Smart Contract State:** Real-time pool reserve state $(x, y)$ and pool mid-price $Z_t = y / x$ (e.g., Uniswap v3 ETH/USDC 0.05% pool on Arbitrum/Ethereum).
- **Mempool & Builder Auction Feeds:** Historical and real-time empirical distribution of validator/builder inclusion delays conditional on priority fee / tip level (EIP-1559 tip histograms) to calibrate $\ell_i(\mathfrak{p}_i)$.
- **AMM Pool Depth Parameter:** Effective reserve depth $d$ representing liquidity density around current tick.

## Execution assumptions

- **CEX Execution:** Continuous order stream executed via limit/market orders with quadratic execution friction coefficient $k = 0.001$.
- **DEX Execution:** Discrete swaps submitted to on-chain AMM smart contracts with constant-product price impact function $\psi(Z) = 2 Z^{3/2} / d$.
- **Pending Order Queue:** System tracks up to $K = 2$ or $K = 3$ concurrent unconfirmed transactions.
- **Latency Randomness:** Execution time $\tilde{\tau}_n - \tau_n$ follows an exponential distribution with parameter $\ell_{I_n}$ chosen by the trader via priority fee $\mathfrak{p}_{I_n}$.

## Evidence

### Source-reported

- Bergault, Hafsi, and Sánchez-Betancourt (2026) establish:
  1. **Analytical Existence & Uniqueness:** Value function $v(t, y)$ is proven to be the unique viscosity solution to the coupled HJB-QVI system across the full state space.
  2. **Calibrated Baseline Performance:** Evaluated on ETH-USDC market parameters ($S_0 = Z_0 = 2820$, $\sigma^S = 0.0569 \cdot S_0$, $\kappa = 1.0$, $\sigma^Z = 0.00569 \cdot S_0$, depth $d = 50{,}000\text{ ETH}$, inventory penalty $\Xi = 1.0$, running risk $\phi = 1.0$):
     - **Outperformance over Random Fee:** The optimal state-dependent priority fee policy improves the value function norm $\|v_0\|$ across the entire $(s, q, z)$ grid by **$+18.2\%$** relative to a randomized priority fee baseline ($N = 3$, 100 independent Monte Carlo runs).
     - **Diminishing Returns to Fee Granularity:** Comparing performance across discrete priority fee tiers $N \in \{1, 2, 3, 5, 7, 10, 30, 50\}$, the value function improvement plateaus rapidly beyond $N \approx 30$, demonstrating that maintaining a compact set of discrete priority fee choices captures virtually the entire theoretical continuous optimum.
     - **Inventory Urgency Shift:** As terminal time $T$ approaches or inventory $|q|$ becomes large, the continuation band becomes highly asymmetric, forcing aggressive priority fee escalation to ensure rapid inventory liquidation before maturity.

### Independently reproduced

- `not independently reproduced`.

### Negative evidence

- **Deterministic Block-Time Artifacts:** On fixed-slot blockchains (e.g., Ethereum 12s slots, Arbitrum 250ms sequencer ticks), delay distributions exhibit discrete lattice spikes rather than pure memoryless exponential decays ($\tau \sim \text{Exp}(\ell)$), introducing discretization errors.
- **Adverse Selection / Sandwich Bundling:** In public mempools without private builder endpoints (e.g., Flashbots Protect / MEV-Share), paying high priority fees exposes large AMM swaps to predatory front-running and sandwiching, degrading realized price beyond theoretical $\psi(Z) \xi$ impact.

## Falsification plan

1. **Backtest Environment:** Replay synchronized high-frequency Binance L2 order book ticks and Arbitrum Uniswap v3 ETH/USDC swap events across high-volatility (e.g., flash crashes) and low-volatility regimes (2024–2026).
2. **Benchmark Baselines:**
   - Benchmark A: Static priority fee baseline (fixed median gas tip).
   - Benchmark B: Naive threshold CEX-DEX arbitrage without CEX continuous inventory smoothing.
3. **Falsification Thresholds:**
   - If the mixed continuous-impulse strategy with dynamic priority fee selection fails to achieve at least $+5.0\%$ higher net PnL (net of all priority tips, CEX taker fees, and AMM swap fees) than Benchmark A over a 90-day test window, reject the dynamic fee allocation alpha hypothesis.
   - If the realized execution delay under high priority fees fails to correlate negatively with price drift during execution ($p > 0.05$), reject the controllable latency assumption.

## Crypto portability

- **Portability:** `direct`.
- **Crypto Domain Alignment:** Directly engineered for the structural duality of crypto markets: off-chain CEX order books (Binance, OKX, Coinbase) paired with on-chain AMMs (Uniswap, Curve) subject to EIP-1559 priority tips and MEV builder auctions.

## Limitations

- **not independently reproduced**;
- **Poisson Delay Approximation:** Continuous exponential arrival assumption simplifies multi-hop Layer-2 sequencer queues;
- **Adverse Selection in Public Mempool:** Model assumes execution price is determined by AMM reserve depth without accounting for sandwiching attacks;
- **Capacity Limits:** Strategy capacity is constrained by AMM pool depth $d$ and CEX liquidity parameters $k$.

## Implementation status

- `not-implemented`. Research capture only; no PyBroker or NautilusTrader production implementation created.

## Adoption boundary

- `research-only`, `not-approved`.
- This record serves as theoretical and empirical research on cross-venue latency risk management and mixed control execution. It does not authorize live or paper trading.

## Related Wiki records

- `[[quant/crypto-priority-gas-auctions-pga-dex-latency-arbitrage-2026-09-01]]`
- `[[quant/dex-cyclic-arbitrage-constant-product-amm-2026-09-01]]`
- `[[quant/crypto-perpetual-spot-cross-venue-lead-lag-vecm-2026-09-01]]`
- `[[quant/defi-amm-continuous-installment-options-lvr-delta-hedge-2026-09-01]]`

## Sources

1. Philippe Bergault, Yadh Hafsi, and Leandro Sánchez-Betancourt, "Trading in CEXs and DEXs with Priority Fees and Stochastic Delays", *arXiv preprint arXiv:2602.10798v2 [q-fin.TR]*, February 19, 2026. DOI: [10.48550/arXiv.2602.10798](https://doi.org/10.48550/arXiv.2602.10798). URL: [https://arxiv.org/abs/2602.10798](https://arxiv.org/abs/2602.10798).
2. Philippe Bergault, Yadh Hafsi, and Leandro Sánchez-Betancourt, "Trading in CEXs and DEXs with Priority Fees and Stochastic Delays", *Oxford Working Papers in Mathematical and Computational Finance*, Report No. MCF 26-03, Mathematical Institute, University of Oxford, 2026. URL: [https://www.maths.ox.ac.uk/groups/mathematical-and-computational-finance/oxford-working-papers-mcf](https://www.maths.ox.ac.uk/groups/mathematical-and-computational-finance/oxford-working-papers-mcf).
