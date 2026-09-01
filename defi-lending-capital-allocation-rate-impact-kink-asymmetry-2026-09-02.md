---
schema: strategy-research-record-v1
title: "Endogenous Rate-Impact Capital Allocation and Structural Kink Non-Optimality on Decentralized Lending Platforms"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - lending-protocols
  - morpho
  - aave
  - capital-allocation
  - interest-rate-models
  - endogenous-price-impact
  - kinked-rate
  - portfolio-optimization
status: research-only
confidence: high
source_as_of: 2026-08-25
sources:
  - "Bastien Baude, Vincent Danos, and Hamza El Khalloufi, 'Capital allocation on decentralized lending platforms', arXiv:2608.24206v1 [q-fin.MF], August 25, 2026. DOI: 10.48550/arXiv.2608.24206. https://arxiv.org/abs/2608.24206"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Endogenous Rate-Impact Capital Allocation and Structural Kink Non-Optimality on Decentralized Lending Platforms

## Provenance

- **Primary Source:** Bastien Baude (CentraleSupélec, Université Paris-Saclay), Vincent Danos (CNRS, École Normale Supérieure, Université PSL), and Hamza El Khalloufi (Université Paris 1 Panthéon-Sorbonne / Morpho Labs), *"Capital allocation on decentralized lending platforms"*, arXiv preprint `arXiv:2608.24206v1 [q-fin.MF]`, submitted August 25, 2026. Full text: [https://arxiv.org/html/2608.24206v1](https://arxiv.org/html/2608.24206v1).
- **Primary Categories:** Mathematical Finance (`q-fin.MF`), Portfolio Management (`q-fin.PM`).
- **Empirical Venue / Dataset:** Real-world on-chain telemetry from Ethereum Morpho lending markets spanning January 1, 2026, to April 1, 2026, retrieved via Morpho's GraphQL API (`https://api.morpho.org/graphql`). The dataset evaluates two pools:
  1. *Prime-inspired markets:* 3 markets matching the Gauntlet USDC Prime Vault (`0xdd0f28e19C1780eb6396170735D45153D261490d`).
  2. *Core-inspired markets:* 10 markets matching the Gauntlet USDC Core Vault (`0x8eB67A509616cd6A7c1B3c8C21D48FF57df3d458`) across diverse collateral types (cbBTC, wstETH, sUSDe, ezETH, etc.), plus secondary evaluation on the 4 largest WETH lending pools (WETH/wstETH, WETH/weETH, WETH/osETH, WETH/tBTC).

## Economic mechanism

### Source-reported

In decentralized lending protocols (such as Morpho and Aave), interest rates are determined endogenously by deterministic Interest Rate Models (IRMs) as a function of the utilization rate $\bar{u}_i = \bar{B}_i / \bar{S}_i \le 1$, where $\bar{B}_i$ is total borrowed capital and $\bar{S}_i$ is total supplied capital.

When a liquidity provider (lender) supplies capital $x_i \ge 0$ to market $i$, the post-deposit total supply expands to $\bar{S}_i + x_i$, shifting the post-deposit utilization rate downward:
$$u_i(x_i) = \frac{\bar{B}_i}{\bar{S}_i + x_i}$$
This introduces two opposing forces into the lender's cash flow $f_i(x_i) = x_i \cdot s_i(u_i(x_i)) = x_i \cdot u_i(x_i) \cdot b_i(u_i(x_i))$:
1. **Quantity effect (+):** Depositing more capital increases the lender's proportional share of the pool's generated interest.
2. **Dilution / Rate-Impact effect (-):** Depositing more capital dilutes pool utilization, lowering the borrow rate $b_i(u_i)$ and compounding the drop in the supply APY $s_i(u_i) = u_i b_i(u_i)$.

Under the standard piecewise-linear "kinked" IRM (used by Aave and Euler):
$$b_i(u) = \begin{cases} r_{\text{base}} + r_{\text{slope1}} \frac{u}{u^*} & \text{if } u \le u^* \\ r_{\text{base}} + r_{\text{slope1}} + r_{\text{slope2}} \frac{u - u^*}{1 - u^*} & \text{if } u > u^* \end{cases}$$
the objective function is **only piecewise concave** (unlike borrower-side optimization which is globally concave).

The paper proves two foundational structural theorems:
1. **Closed-Form Root Solution:** For linear and adaptive rate curves, the first-order condition (FOC) reduces via Cardano's formula to a unique interior cubic root $\kappa(p_i, q_i)$ below the inflation peak.
2. **Kink Non-Optimality (Corollary 1):** Assuming $r_{\text{slope2}} / (1 - u^*) > r_{\text{slope1}} / u^*$ (the slope above the target utilization is steeper than below, which holds across all production lending protocols), the allocation that brings utilization *exactly* to the target kink $x_i^{(\text{kink})} = \frac{\bar{B}_i}{u^*} - \bar{S}_i$ is **never optimal for the lender**. 

This creates a fundamental structural asymmetry: borrowers are attracted to the kink (where borrow costs are minimized before penalty steepening), whereas lenders are repelled from the kink (as dilution accelerates immediately above it), driving endemic rate volatility and regime jumps in decentralized credit markets.

### Research interpretation

This model formalizes how a quantitative yield-harvesting fund, automated vault curator (e.g., Morpho Vault, MetaMorpho), or basis arbitrageur should allocate capital across fragmented lending pools.

Key quantitative takeaways:
1. **Bang-Bang Switching vs Allocation Bands:** For small capital sizes (low dilution impact), optimal capital jumps discontinuously to the single highest-yielding market (bang-bang allocation). For large capital sizes (high dilution impact), capital is forced into wide allocation bands across the largest liquidity pools, behaving asymptotically as a single aggregated pool.
2. **Kink Boundary Repulsion:** Vault managers attempting to target the kink utilization rate $u^*$ operate at a mathematically sub-optimal local saddle/inflection point. The true optimum is always located strictly on the pre-kink branch or strictly on the post-kink branch.

## Signal

### 1. Optimization Formulation
Let $\xi$ be total loanable budget in the numeraire (e.g., USDC), allocated across $n$ lending pools $x_1, \ldots, x_n \ge 0$ and an external fixed-rate risk-free yield opportunity $x_0 \ge 0$ earning rate $r > 0$:
$$\max_{x_0, x_1, \ldots, x_n} \sum_{i=1}^n x_i \cdot u_i(x_i) \cdot b_i(u_i(x_i)) + r \cdot x_0 \quad \text{s.t.} \quad \sum_{i=0}^n x_i = \xi, \quad x_i^{\min} \le x_i \le x_i^{\max}, \quad x_0 \ge 0$$

### 2. Linear Rate Closed-Form Allocator (Proposition 1)
For market $i$, assuming $r_{\text{base}} < r_{\text{slope1}} \frac{\bar{u}_i}{u^*}$, define:
$$p_i = \frac{3 \bar{S}_i}{2} \left(1 - \frac{r_{\text{base}} u^*}{r_{\text{slope1}} \bar{u}_i}\right), \qquad q_i(\lambda) = -\frac{\bar{S}_i^3}{2} \left(\frac{\lambda u^*}{r_{\text{slope1}} \bar{u}_i^2} + \frac{r_{\text{base}} u^*}{r_{\text{slope1}} \bar{u}_i}\right)$$
Discriminant:
$$\Delta_i(\lambda) = q_i(\lambda)^2 + p_i^3 > 0$$
The unique interior unconstrained maximizer is given by Cardano's formula:
$$\kappa(p_i, q_i(\lambda)) = \sqrt[3]{-q_i(\lambda) + \sqrt{\Delta_i(\lambda)}} + \sqrt[3]{-q_i(\lambda) - \sqrt{\Delta_i(\lambda)}} - \bar{S}_i$$
With risk limits $x_i^{\min} \le x_i \le x_i^{\max}$, the candidate allocation is:
$$x_i^*(\lambda) = \text{clip}\left(\kappa(p_i, q_i(\lambda)), x_i^{\min}, x_i^{\max}\right)$$

### 3. Lagrange Multiplier Resolution & Market Regimes
- **Saturated Regime ($\lambda^* = r$):** If $\sum_{i=1}^n x_i^*(r) \le \xi$, all pools are saturated at the marginal rate $r$. The remaining budget goes to the external reserve:
  $$x_0^* = \xi - \sum_{i=1}^n x_i^*(r)$$
- **Unsaturated Regime ($\lambda^* > r$):** If $\sum_{i=1}^n x_i^*(r) > \xi$, the external reserve is zero ($x_0^* = 0$). The optimal multiplier $\lambda^* > r$ is solved via 1D Brent's method satisfying:
  $$\sum_{i=1}^n x_i^*(\lambda^*) = \xi$$

### 4. Kinked Rate Discrete Regime Enumeration (Proposition 2 & Algorithm)
For kinked IRMs, the state space splits into:
- Regime 1 (pre-kink, $u \le u^*$): parameterized by $(r_{\text{base}}, r_{\text{slope1}})$.
- Regime 2 (post-kink, $u > u^*$): parameterized by $(r_{\text{base}}', r_{\text{slope1}}')$.
Admissible regimes $\mathcal{M}_i$:
$$\mathcal{M}_i = \begin{cases} \{1\} & \text{if } \bar{u}_i < u^* \\ \{2\} \cup \left(\{1\} \text{ if } x_i^{(\text{kink})} \le \xi \text{ and } \lambda_i^1 \ge r\right) & \text{if } \bar{u}_i \ge u^* \end{cases}$$
The algorithm enumerates the feasible combinatorial regime vectors $m \in \prod_{i=1}^n \mathcal{M}_i$, computes the exact candidate allocations, and selects the regime maximizing total portfolio interest.

### 5. Adaptive IRM Parametrization (Morpho AdaptiveCurveIRM)
Morpho replaces static slopes with an adaptive curve:
$$r_{\text{base}} = 0, \quad r_{\text{slope1}} = r_{\text{target}}, \quad r_{\text{slope2}} = (k_d - 1) r_{\text{target}}$$
With production constants $u^* = 0.9$ and $k_d = 4$, the conditions for unique solvability hold whenever current utilization $\bar{u}_i > 30\%$.

## Required data

- **Universe / Venues:** On-chain decentralized lending markets on Ethereum (specifically Morpho Blue / MetaMorpho isolated markets and Aave v3 pools).
- **Underlying Assets:** Homogeneous loan token pool (e.g. USDC or WETH) across multiple collateral pairings (cbBTC, wstETH, sUSDe, ezETH, tBTC, osETH).
- **Market State Telemetry (Point-in-Time):**
  - $\bar{S}_i$: Total supplied assets in pool $i$ at block timestamp $t$.
  - $\bar{B}_i$: Total borrowed assets in pool $i$ at block timestamp $t$.
  - $\bar{u}_i = \bar{B}_i / \bar{S}_i$: Current pool utilization.
  - IRM Parameters: $u^*$ (target utilization), $r_{\text{base}}$, $r_{\text{slope1}}$, $r_{\text{slope2}}$ (or $r_{\text{target}}, k_d$ for Morpho).
  - External baseline rate $r$ (e.g. Maker DSR / Aave supply rate / US Treasury bill yield on-chain).
- **Sampling Frequency:** 1-day moving averages (to filter out flash-loan / MEV intra-block noise) evaluated at daily rebalancing epochs.

## Execution assumptions

- **Execution Model:** On-chain atomic reallocation transactions via batch multi-calls or Morpho Bundler.
- **Gas Costs:** Gas costs for supply/withdraw reallocations are modeled.
- **Slippage / Market Impact:** The price impact on interest rates is *fully internalized and exact* within the objective function $f_i(x_i)$.
- **Rebalancing Cadence:** Daily rebalance (24-hour discrete steps).
- **Capital Constraints:** Low-capital regime ($100k) representing negligible market impact; high-capital regime ($100m) representing severe endogenous pool dilution.

## Evidence

### Source-reported

All figures below are directly reported by Baude, Danos, and El Khalloufi (arXiv:2608.24206v1, August 2026) evaluated over Morpho Ethereum markets (January 1 – April 1, 2026):

#### 1. USDC Backtest Performance (Jan 1, 2026 – Apr 1, 2026)
- **Low-Capital Case ($\$100\text{k}$ budget):**
  - *Core-inspired strategy (10 pools):* **11.45% APY** (highest yield; captures attractive fragmented lending spreads).
  - *Prime-inspired strategy (3 pools):* **9.02% APY**.
  - *USDC/cbBTC benchmark:* **8.98% APY**.
- **High-Capital Case ($\$100\text{m}$ budget - severe dilution):**
  - *Core-inspired strategy:* **7.21% APY** (dilution lowers APY by 4.24 percentage points).
  - *Prime-inspired strategy:* **6.85% APY** (outperforms benchmark due to larger aggregate pool capacity).
  - *USDC/cbBTC benchmark:* **5.83% APY**.

#### 2. Solver Optimality vs SLSQP Local Trap Benchmark (Synthetic 5-Market Test)
- **Proposed Closed-Form Cardano / Discrete Regime Solver:** **11.82% APY** (execution time 1.2 ms).
- **Single-start SLSQP (initialized at $x_0 = \xi$):** **8.41% APY** (trapped in local suboptimal post-kink saddle).
- **Multi-start SLSQP:** **11.82% APY** (execution time 18.5 ms, 15x slower).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Endogenous Yield Degradation with Scale:** As capital scales from $\$100\text{k}$ to $\$100\text{m}$, realized APY monotonically collapses (e.g. from 11.45% to 7.21% on Morpho Core). Beyond $\$250\text{m}$, the entire decentralized lending market converges to a single aggregate rate, eliminating cross-pool alpha.
- **Bang-Bang Gas Drag in Low-Capital Regime:** In fragmented high-spread pools, unconstrained low-capital optimization creates high churn (switching 100% of capital between markets every 24–48 hours), which can incur excessive Ethereum L1 gas fees if not throttled by minimum reallocation thresholds ($\Delta x > \delta_{\text{gas}}$).
- **Collateral Tail Risk:** Core-inspired markets provide higher APYs because they price higher smart contract or depeg risk of niche collateral (e.g. sUSDe, ezETH). The optimization model assumes zero default/bad-debt losses; empirical yield spreads reflect unhedged credit risk.

## Falsification plan

1. **Ablation of Endogenous Impact:** Compare the rate-impact Cardano allocator against a naive "greedy" allocator that routes capital purely to the highest current spot rate $\arg\max_i s_i(\bar{u}_i)$. If the naive allocator achieves identical or higher realized APY at $\$50\text{m}+$ scale, the endogenous impact model is falsified.
2. **Kink Boundary Test:** Force allocation directly onto the kink $x_i = x_i^{(\text{kink})}$ across all markets with $\bar{u}_i > u^*$. Verify whether net realized portfolio yield is strictly lower than the closed-form pre/post-kink solution.
3. **Transaction Cost Stress Test:** Introduce variable Ethereum L1 gas costs ($20–100 Gwei). Identify the critical budget threshold $\xi_{\text{crit}}$ below which daily rebalancing gas erases all cross-market yield advantage.
4. **Nash Multi-Agent Dynamic Simulation:** Simulate 5 competing vaults running the same algorithm simultaneously. Verify whether game-theoretic race conditions induce cyclical rate oscillation and utilization destabilization.

## Crypto portability

- **Status:** Direct.
- **Protocol Application:** Directly designed for and calibrated on Ethereum DeFi protocols (Morpho Blue, MetaMorpho Vaults, Aave v3, Spark Protocol, Compound v3).
- **Cross-Chain Portability:** Can be directly deployed to Arbitrum, Base, and Solana (e.g. Kamino, MarginFi) lending protocols utilizing piece-wise linear or dynamic interest rate models.

## Limitations

- **Single-Agent Static Formulation:** Assumes the allocator is the sole active participant during each daily rebalancing window; does not account for strategic front-running by competing yield aggregators (Yearn, MetaMorpho).
- **Exogenous Borrow Demand:** Treats borrower demand $\bar{B}_i$ as constant over the 24h interval, whereas borrowers also react to rate changes by repaying or migrating debt.
- **Credit / Bad-Debt Exclusion:** Does not include quantitative haircuts for collateral liquidations or oracle failure risk.

## Implementation status

- `not-implemented`: Research capture only. No production implementation in PyBroker, Nautilus, Paper, Testnet, or Live systems.

## Adoption boundary

- `research-only`: Theoretical and empirical framework for DeFi capital allocation. Not approved for automated capital routing or live execution.

## Related Wiki records

- `[[quant/defi-lending-collateral-liquidation-discount-arbitrage-2026-09-01]]`
- `[[quant/crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31]]`
- `[[quant/defi-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31]]`

## Sources

1. Bastien Baude, Vincent Danos, and Hamza El Khalloufi, *"Capital allocation on decentralized lending platforms"*, arXiv preprint `arXiv:2608.24206v1 [q-fin.MF]`, August 25, 2026. DOI: [10.48550/arXiv.2608.24206](https://doi.org/10.48550/arXiv.2608.24206). Full text: [https://arxiv.org/html/2608.24206v1](https://arxiv.org/html/2608.24206v1).
2. Bastien Baude, Vincent Danos, and Hamza El Khalloufi, *"Leveraged positions on decentralized lending platforms"*, arXiv preprint `arXiv:2601.14005 [q-fin.MF]`, January 2026.
3. Aave Protocol Whitepaper v1.0, 2020. [https://github.com/aave/aave-protocol/blob/master/docs/Aave_Protocol_Whitepaper_v1_0.pdf](https://github.com/aave/aave-protocol/blob/master/docs/Aave_Protocol_Whitepaper_v1_0.pdf).
4. Morpho Labs, *"AdaptiveCurveIRM Specification"*, 2023. [https://docs.morpho.org/morpho/contracts/irm/adaptive-curve-irm/](https://docs.morpho.org/morpho/contracts/irm/adaptive-curve-irm/).
