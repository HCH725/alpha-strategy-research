---
schema: strategy-research-record-v1
title: Cross-Venue Bounded Liquidity Loss Versus Rebalancing and Harmonic Arbitrage Bounds
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - amm
  - lvr
  - loss-versus-rebalancing
  - bounded-liquidity
  - dex-dex-arbitrage
  - slippage
  - flashbots
  - market-microstructure
status: research-only
confidence: high
source_as_of: 2025-12
sources:
  - "Christoph Schlegel and Quintus Kilbourn, 'Arbitrage with Bounded Liquidity', arXiv:2507.02027v2 [q-fin.MF, q-fin.TR], Flashbots Research, July 2025 (revised December 2025). DOI: 10.48550/arXiv.2507.02027. https://arxiv.org/abs/2507.02027"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Venue Bounded Liquidity Loss Versus Rebalancing and Harmonic Arbitrage Bounds

## Provenance

- **Primary Source:** Christoph Schlegel and Quintus Kilbourn (Flashbots), "Arbitrage with Bounded Liquidity", arXiv:2507.02027v2 [q-fin.MF, q-fin.TR], submitted July 2025, revised December 2025. DOI: [10.48550/arXiv.2507.02027](https://doi.org/10.48550/arXiv.2507.02027). Full text: [https://arxiv.org/html/2507.02027v2](https://arxiv.org/html/2507.02027v2).
- **Theoretical Foundation:** Generalization of the canonical Loss-Versus-Rebalancing (LVR) framework introduced by Milionis, Moallemi, Roughgarden, and Zhang (2022) to environments where the reference market has finite, imperfect liquidity and non-zero quadratic trading costs.

## Economic mechanism

### Source-reported

1. **Failure of the Infinite-Liquidity Reference Market Assumption:** Canonical LVR models quantify adverse selection suffered by passive AMM liquidity providers (LPs) by assuming the existence of an infinitely liquid external market where arbitrageurs can rebalance instantaneously at frictionless mid-price. In reality, arbitrageurs operate between two imperfectly liquid markets (e.g., DEX-DEX arbitrage across Uniswap and Sushiswap, or DEX-CEX arbitrage on altcoin pairs with thin order books), where trading incurs quadratic slippage costs.
2. **Quadratic Slippage & Effective Harmonic Liquidity:** When trading costs on at least one market are quadratic in trade size ($C(\Delta x) = \frac{Q (\Delta x)^2}{x(Q)}$), the marginal cost of arbitrage expands with volume. For two Constant Product Market Maker (CPMM) pools with reserves $L_1$ and $L_2$, the instantaneous arbitrage gains and LVR extracted between the venues depend on the **harmonic mean of their marginal liquidities**:
   $$L_{\mathrm{eff}} = \frac{L_1 L_2}{L_1 + L_2} = \frac{1}{\frac{1}{L_1} + \frac{1}{L_2}}$$
3. **Asymmetric Leakage Suppression:** A dominant pool ($L_1 \gg L_2$) leaks significantly less LVR per unit of TVL than predicted by standard LVR models. The shallow counter-venue ($L_2$) imposes severe slippage that caps the profitable arbitrage rebalancing capacity:
   $$\frac{\mathrm{LVR}_1}{V_1} = \frac{\sigma^2}{8} \cdot \frac{L_2}{L_1 + L_2} \xrightarrow{L_1 \gg L_2} 0$$

### Research interpretation

The falsifiable thesis is a **cross-venue liquidity capacity and adverse selection scaling mechanism**:
1. **DEX-DEX Arbitrage Bound:** Classical cross-DEX arbitrage algorithms that model target price alignment without quadratic reference friction systematically overestimate profitable trade sizes, leading to negative net PnL from second-leg slippage.
2. **LP Capital Allocation Alpha:** Passive LP capital deployed in a dominant pool incurs diminishing adverse selection as its market share increases relative to secondary pools, creating a structural incentive for liquidity concentration.
3. **Active Liquidity Provision Edge:** Active market makers who dynamically adjust marginal depth around the expected post-arbitrage equilibrium price internalize arbitrage flow and transfer LVR leakage to passive LPs.

## Signal

### 1. Market Setup & Price Process

- **Two Venues:** Token pair $(A, B)$ traded on Venue 1 (reserves $x^*(Q)$) and Venue 2 (reserves $\tilde{x}^*(Q)$), where Token $B$ is the numéraire.
- **Equilibrium Price Process ($Q_t$):** Post-arbitrage equilibrium exchange rate follows Geometric Brownian Motion (GBM):
  $$dQ_t = \mu Q_t dt + \sigma Q_t dB_t$$
  micro-founded via Donsker's theorem on continuous noise trader arrival with order flow fraction $\pi \in [0, 1]$ arriving on Venue 1 and $1-\pi$ on Venue 2.

### 2. Quadratic Slippage Cost Model

- On Venue 2, selling $\Delta x$ of Token $A$ yields $Q \Delta x - C(Q, \Delta x)$ of Token $B$, where:
  $$C(Q, \Delta x) = \frac{Q (\Delta x)^2}{\tilde{x}^*(Q)}$$
- For a CPMM with invariant $x(Q) \cdot y(Q) = K^2$, exact slippage is $C(\Delta x) = \frac{Q (\Delta x)^2}{x(Q) + \Delta x}$. Proposition 1 in the source proves that higher-order Taylor terms vanish almost surely under quadratic variation of Brownian paths, making the quadratic cost exact in the continuous limit:
  $$\lim_{N \to \infty} \sum_{i=1}^N \left| C(\Delta x_i) - \tilde{C}(\Delta x_i) \right| = 0 \quad \text{a.s.}$$

### 3. Closed-Form Bounded-Liquidity LVR Theorems

#### Theorem 2.1 (One-Way Price Discovery)
When Venue 2 is the primary price discovery market, total arbitrage gains $\mathrm{ARB}_{[0, T]}$ and LVR take the closed form:
$$\mathrm{LVR} = \mathrm{ARB} = \int_0^T \frac{\sigma^2}{2} Q_t \cdot \frac{x^*(Q_t) |x^{*\prime}(Q_t)|}{1 + \frac{|x^{*\prime}(Q_t)|}{|\tilde{x}^{*\prime}(Q_t)|}} dt$$

#### Theorem 2.2 (Two-Way Order Flow on Dual CPMMs)
When both venues are CPMMs with liquidity parameters $L_1 = K_1$ and $L_2 = K_2$, and noise orders split as $(\pi, 1-\pi)$:
$$\mathrm{ARB} = \int_0^T \frac{\sigma^2}{8} \sqrt{Q_t} \cdot \left[ \pi \frac{L_1 L_2}{L_1 + L_2} + (1 - \pi) \frac{L_1 L_2}{L_1 + L_2} \right] dt = \int_0^T \frac{\sigma^2}{8} \sqrt{Q_t} \cdot \left( \frac{1}{L_1} + \frac{1}{L_2} \right)^{-1} dt$$

### 4. Optimal Arbitrage Sizing Rule

For discrete observed prices $P_1$ on Venue 1 and $P_2$ on Venue 2 with $P_1 > P_2$:
$$\Delta x^* = \frac{P_1 - P_2}{2 \left( \frac{P_1}{x_1} + \frac{P_2}{x_2} \right)}$$
Execution is triggered if and only if expected gross profit $\Pi(\Delta x^*) > \text{Gas Fee} + \text{Taker Fees}$.

## Required data

- **On-Chain DEX Data:**
  - Full-depth pool reserves $(x_1, y_1)$ and $(x_2, y_2)$ sampled per block.
  - Pool invariants $K_1 = \sqrt{x_1 y_1}$ and $K_2 = \sqrt{x_2 y_2}$.
  - Tick-level swap events and transaction indices.
- **Reference Venue / Order Book Data:**
  - L2 order book snapshots around mid-price to evaluate empirical slope $|\tilde{x}^{\prime}(Q)|$.
- **Statistical Estimators:**
  - Realized volatility $\sigma$ estimated via continuous quadratic variation over rolling 1-hour windows.
  - Order flow arrival split $\hat{\pi}$ estimated via rolling 24-hour volume fractions.

## Execution assumptions

- **Execution Venue:** Ethereum Mainnet / Arbitrum / Base / Optimism EVM smart contract execution.
- **Atomicity:** Backrun / spatial arbitrage transactions submitted via MEV-Boost bundles (Flashbots / Builder RPC) to ensure zero-risk atomic execution across both pools in a single transaction.
- **Fee Structure:** Zero priority gas auction cost under failure; builder priority fee deducted from gross arbitrage margin.
- **Slippage Constraint:** Quadratic slippage evaluated on both legs simultaneously.

## Evidence

### Source-reported

- **Closed-Form Derivation:** Rigorous mathematical proofs for Theorem 2.1, Theorem 2.2, and Proposition 1 establishing the harmonic capacity scaling under Itô calculus and Donsker's invariance principle.
- **Standard LVR Overestimation:** The source demonstrates analytically that canonical infinite-liquidity LVR overestimates true extractable MEV by a factor of:
  $$\text{Overestimation Factor} = \frac{L_1 + L_2}{L_2} = 1 + \frac{L_1}{L_2}$$
  When $L_1 = L_2$, standard LVR overstates arbitrage leakage by exactly 100% (2x actual extracted value).

### Independently reproduced

- `not independently reproduced`.

### Negative evidence

- **CLOB Large-Cap Tick Granularity:** For highly liquid major pairs on centralized exchanges (e.g., BTC/USDT and ETH/USDT on Binance), order book liquidity is heavily concentrated at the tightest 1-cent tick spread. In this regime, marginal cost is constant rather than linear/quadratic for small trade sizes ($C(x) = c x$). In pure continuous-time diffusion, continuous constant marginal cost causes the variation sum $\lim \sum c |\Delta x_i|$ to diverge, indicating that discrete batching or inventory warehousing is required in practice.

## Falsification plan

1. **Cross-DEX Arbitrage Extraction Test:**
   - **Sample:** 12 months of atomic DEX-DEX arbitrage transactions on Ethereum (Uniswap v2/v3 vs Sushiswap/Curve) across token pairs with varying liquidity ratios $L_1 / L_2 \in [0.1, 10.0]$.
   - **Metric:** Empirical realized arbitrage profit per block vs. theoretical harmonic capacity $\frac{\sigma^2}{8} \sqrt{Q} \frac{L_1 L_2}{L_1 + L_2} \Delta t$.
   - **Falsification Threshold:** If observed extracted profits systematically scale linearly with $L_1$ rather than harmonic mean $\frac{L_1 L_2}{L_1 + L_2}$ ($R^2 < 0.30$ or slope coefficient on $L_2 / (L_1 + L_2)$ not statistically significant at $p < 0.01$), reject the bounded-liquidity quadratic slippage thesis.
2. **Ablation / Parameter Perturbation:** Perturb estimated volatility $\sigma$ by $\pm 25\%$ and examine stability of the optimal trade size $\Delta x^*$.

## Crypto portability

- **Portability:** `direct`.
- **Crypto-Specific Alignment:** Specifically derived for decentralized automated market makers (Uniswap v2, Uniswap v3, Sushiswap) and MEV atomic bundle execution in cryptocurrency markets.

## Limitations

- **No Multi-Block Inventory Accumulation:** The model assumes instantaneous rebalancing without inventory holding. In practice, sophisticated arbitrageurs accumulate inventory across blocks to amortize fixed transaction fees and reduce market impact.
- **Zero Fixed Fee Assumption:** The continuous-time derivation abstracts away discrete pool swap fees ($\gamma$) and gas costs, which create a no-arbitrage inaction band.

## Implementation status

- `not-implemented` in our production quant stack.
- Research capture only; no PyBroker or Nautilus execution files created.

## Adoption boundary

- `research-only`, `not-approved`.
- This record serves as a theoretical reference for AMM liquidity modeling and cross-venue MEV arbitrage estimation. It does not authorize paper, testnet, or live trading.

## Related Wiki records

- `[[quant/crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31]]`
- `[[quant/defi-amm-jump-diffusion-lvr-decomposition-optimal-block-time-2026-09-01]]`
- `[[quant/cross-exchange-crypto-spatial-arbitrage-2026-08-31]]`

## Sources

- Christoph Schlegel and Quintus Kilbourn, "Arbitrage with Bounded Liquidity", arXiv:2507.02027v2 [q-fin.MF, q-fin.TR], Flashbots Research, July 2025 (revised December 2025). DOI: [10.48550/arXiv.2507.02027](https://doi.org/10.48550/arXiv.2507.02027). https://arxiv.org/abs/2507.02027.
- A. Milionis, C. C. Moallemi, T. Roughgarden, and B. Zhang, "Automated Market Making and Loss-Versus-Rebalancing", arXiv:2208.06046 [q-fin.TR], 2022.
