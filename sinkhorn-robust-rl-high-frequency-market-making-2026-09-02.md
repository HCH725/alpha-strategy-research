---
schema: strategy-research-record-v1
title: "Sinkhorn-Robust Reinforcement Learning for High-Frequency Market Making: Two-Dimensional Robustness Decomposition, Hawkes Order Flow, and Adaptive Quoting"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-making
  - high-frequency-trading
  - reinforcement-learning
  - distributionally-robust-optimization
  - sinkhorn-divergence
  - optimal-transport
  - hawkes-process
status: research-only
confidence: high
source_as_of: 2026-08-24
sources:
  - "Ying Chen, Hoa Nguyen, Julian Sester, Hoang Hai Tran, Yijiong Zhang, 'Robustness in Sequential Decision Making under Evolving Uncertainty: Evidence from High-Frequency Market Making', arXiv preprint arXiv:2607.08291v1 [q-fin.TR], July 13, 2026 (revised August 24, 2026). DOI: 10.48550/arXiv.2607.08291. Stable URL: https://arxiv.org/abs/2607.08291"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Sinkhorn-Robust Reinforcement Learning for High-Frequency Market Making: Two-Dimensional Robustness Decomposition, Hawkes Order Flow, and Adaptive Quoting

## Provenance

- **Primary Source:** Ying Chen (National University of Singapore), Hoa Nguyen (Grasshopper Asset Management), Julian Sester (National University of Singapore), Hoang Hai Tran (Tsinghua University), and Yijiong Zhang (National University of Singapore), *"Robustness in Sequential Decision Making under Evolving Uncertainty: Evidence from High-Frequency Market Making"*, arXiv preprint `arXiv:2607.08291v1 [q-fin.TR]`, submitted July 13, 2026, revised August 24, 2026. DOI: [10.48550/arXiv.2607.08291](https://doi.org/10.48550/arXiv.2607.08291). Stable URL: [https://arxiv.org/abs/2607.08291](https://arxiv.org/abs/2607.08291).
- **Primary Subject Area:** Trading and Market Microstructure (`q-fin.TR`), Mathematical Finance (`q-fin.MF`).
- **Context & Motivation:** In electronic limit order book (LOB) markets, liquidity providers face evolving non-stationary market regimes, volatility bursts, adverse selection, and transient liquidity dry-outs. While classical stochastic control models (Avellaneda-Stoikov, Guéant-Tapia-Manziuk, Cartea-Jaimungal) provide closed-form quoting heuristics under stylized Poisson arrival assumptions, they suffer severe degradation under model misspecification. Standard robust Markov decision processes (MDPs) treat robustness as a single scalar radius around a reference model, failing to disentangle the plausibility of model deviations from the behavioral conservatism of the agent. Chen et al. resolve this by proposing a distributionally robust reinforcement learning framework powered by Sinkhorn divergence ambiguity sets, decomposing robustness into two economically distinct dimensions: **uncertainty tolerance** $\bar{\varepsilon}$ (the transport budget of plausible distribution shift) and **action robustness** $\delta$ (the entropic regularizer governing how aggressively the policy responds to adverse scenarios).

## Economic mechanism

### Source-reported

1. **Two-Dimensional Robustness Decomposition:**
   - *Uncertainty Tolerance ($\bar{\varepsilon}$):* Sets the radius of the Sinkhorn ball around the nominal transition kernel $\widehat{\mathbb{P}}$. Economically, this governs how much distribution shift the market maker considers plausible in future order arrival intensities, fill ratios, and mid-price returns.
   - *Action Robustness ($\delta$):* Governs the entropic regularization of the optimal transport plan. Smaller $\delta$ forces the adversary to concentrate probability mass onto isolated worst-case scenarios, inducing highly conservative decision rules; larger $\delta$ spreads uncertainty smoothly across perturbed states, resulting in temperate, stable policy adaptation.
2. **State-Dependent Quoting Adaptation:** Robustness does not merely widen spreads uniformly. Under price or execution stress, robust agents widen spreads to demand higher compensation for adverse selection. Conversely, under persistent directional order-flow imbalances (e.g., strong buy-order waves), the robust policy selectively tightens quotes and reduces quote dispersion to actively offload accumulating inventory, substantially dampening directional inventory drawdowns.
3. **Liquidity-Conditioned Robustness Value:** In liquid regimes, robust quoting stabilizes Sharpe ratios and caps inventory drawdowns without hurting fill rates. In illiquid regimes, excessive action robustness over-widens quotes, suppressing execution opportunities and lowering net profitability. Robustness is therefore an adaptive state-dependent control lever rather than a static safeguard.

### Research interpretation

The falsifiable thesis is that **jointly optimizing continuous bid/ask spreads and order participation rates under Sinkhorn distributionally robust dynamic programming significantly stabilizes out-of-sample inventory PnL and Sharpe ratios across non-stationary regimes, with action robustness ($\delta$) exerting a statistically dominant influence over uncertainty tolerance ($\bar{\varepsilon}$)**:
- By decomposing transition dynamics into a deterministic historical shift $\pi(x)$ and a stochastic innovation $Z_{t+1}$ modeled via deep neural ensembles, the inner infimum over probability measures collapses into a tractable 1D dual optimization via Sinkhorn duality, solvable at high frequency.
- The inclusion of discrete-time Hawkes self-excitation states ($Z^{\text{bid}}, Z^{\text{ask}}$) and Order Flow Imbalance (OFI) allows the policy network to anticipate order clustering and dynamically shade quotes before toxic flow exhausts book depth.

## Signal

### 1. High-Frequency State Representation

At decision epoch $t$, the market maker observes a rolling window of history length $m$:
$$X_t = \left( I^t, R^t, N^{t,\text{bid}}, N^{t,\text{ask}}, V^{t,\text{bid}}, V^{t,\text{ask}}, \delta^{t,\text{tick}}, \delta^{t,\text{rel}}, D^{t,\text{micro}}, \nu^t, \text{OFI}^t, Z^{t,\text{bid}}, Z^{t,\text{ask}}, \tau^t \right) \in \mathbb{R}^{14m}$$
where key microstructure state features include:
- $I_t$: Current accumulated inventory.
- $R_t$: Log mid-price returns over the decision interval.
- $D_t^{\text{micro}} = S_t^{\text{micro}} - S_t$: Microprice deviation from mid-price:
  $$S_t^{\text{micro}} = \frac{V_t^{\text{bid,best}} S_t^{\text{ask,best}} + V_t^{\text{ask,best}} S_t^{\text{bid,best}}}{V_t^{\text{bid,best}} + V_t^{\text{ask,best}}}$$
- $\nu_t$: EWMA running return volatility: $\nu_t^2 = \lambda_{\nu} \nu_{t-1}^2 + (1 - \lambda_{\nu}) R_t^2$.
- $\text{OFI}_t$: Level-1 Order Flow Imbalance:
  $$\text{OFI}_t = \Delta V_t^{\text{bid}} \mathbf{1}_{\{\Delta S_t^{\text{bid}} \ge 0\}} - \Delta V_t^{\text{ask}} \mathbf{1}_{\{\Delta S_t^{\text{ask}} \le 0\}}$$
- $Z_t^{\text{bid}}, Z_t^{\text{ask}}$: Hawkes order arrival self-excitation state:
  $$Z_t^{\text{side}} = e^{-\beta \Delta t} Z_{t-1}^{\text{side}} + \alpha N_{t-1}^{\text{side}}$$
- $\tau_t = T - t$: Remaining time-to-close windows.

### 2. Continuous Action Space

At each decision epoch $t$, the market maker selects a 4-dimensional continuous action:
$$a_t = \left( \delta_t^{\text{bid}}, \, \delta_t^{\text{ask}}, \, q_t^{\text{bid}}, \, q_t^{\text{ask}} \right) \in A = [\underline{C_S}, \overline{C_S}]^2 \times [\underline{C_q}, \overline{C_q}]^2$$
where $\delta_t^{\text{bid}}, \delta_t^{\text{ask}}$ denote posted half-spreads (in ticks or bps) relative to mid-price $S_t$, and $q_t^{\text{bid}}, q_t^{\text{ask}} \in [0, 1]$ represent order sizes parameterized as participation fractions of incoming market volume.

### 3. Additive One-Period Reward Functional

The time-$t$ terminal risk-adjusted objective decomposes into an additive Markov reward:
$$r(X_t, a_t, X_{t+1}) = \delta_t^{\text{bid}} Q_{t+1}^{\text{bid}} + \delta_t^{\text{ask}} Q_{t+1}^{\text{ask}} - \frac{\gamma_t}{2} I_{t+1}^2 \sigma^2 \Delta_t - c_t \left( Q_{t+1}^{\text{bid}} + Q_{t+1}^{\text{ask}} \right)$$
where:
- $Q_{t+1}^{\text{bid}} = q_t^{\text{bid}} V_{t+1}^{\text{bid}} \varphi^{\text{bid}}(\delta_t^{\text{bid}})$ is the executed fill volume.
- $I_{t+1} = I_t + Q_{t+1}^{\text{bid}} - Q_{t+1}^{\text{ask}}$ is the updated inventory.
- $\gamma_t = \gamma \left( 1 + \frac{1}{\xi(T - t) + 1} \right)$ is the time-varying horizon inventory aversion parameter.
- $c_t$ is exchange maker fee or per-trade transaction cost.

### 4. Sinkhorn Ambiguity Set & Robust Bellman Operator (Proposition 2.2)

Let $\widehat{\mathbb{P}}(X_t, a_t)$ denote the reference innovation law generated by a deep neural ensemble. The entropic optimal transport (Sinkhorn) ambiguity set is:
$$\mathcal{B}_{\varepsilon, \delta}\left(\widehat{\mathbb{P}}(X_t, a_t)\right) = \left\{ \mathbb{P} \in \mathcal{M}_1(\Omega_{\text{rnd}}) : W_\delta(\mathbb{P}, \widehat{\mathbb{P}}(X_t, a_t)) \le \varepsilon \right\}$$
where:
$$W_\delta(\mathbb{P}_1, \mathbb{P}_2) = \inf_{\gamma \in \Pi(\mathbb{P}_1, \mathbb{P}_2)} \left\{ \mathbb{E}_\gamma [c(\tilde{x}, \tilde{z})] + \delta \mathcal{H}(\gamma \mid \mathbb{P}_1 \otimes \nu) \right\}$$
Using Sinkhorn duality (Theorem 2.3), the robust Bellman equation simplifies to:
$$\mathcal{T} V(x) = \sup_{a \in A} \sup_{\lambda > 0} \left\{ -\lambda \bar{\varepsilon} - \delta \lambda \mathbb{E}_{\tilde{x} \sim \widehat{\mathbb{P}}(x, a)} \left[ \log \mathbb{E}_{\tilde{z} \sim Q_{\tilde{x}, \delta}} \left[ \exp\left( -\frac{r^C(x, a, \Phi_\pi(x, a, \tilde{z})) + \alpha V(\Phi_\pi(x, a, \tilde{z}))}{\delta \lambda} \right) \right] \right] \right\}$$
where $Q_{\tilde{x}, \delta}(d\tilde{z}) \propto e^{-c(\tilde{x}, \tilde{z})/\delta} \nu(d\tilde{z})$ is the Sinkhorn perturbation kernel.

### 5. Policy Training via Sinkhorn-Robust Fitted Actor–Critic

- **Critic:** Parameterized neural network $V_\theta(x)$ minimizing Bellman temporal-difference error under the tilted worst-case distribution.
- **Actor:** Parameterized policy network $\mu_\phi(x)$ outputting continuous action means with Gaussian exploration, updated via deterministic policy gradients.
- **Dual Variable:** Scalar multiplier $\lambda > 0$ updated via stochastic gradient ascent on the outer dual objective.

## Required data

- **Universe:** Single-asset high-frequency equities (e.g., Nasdaq LOB data: AAPL, MSFT, INTC) or perpetual futures.
- **Timeframe:** High-frequency millisecond tick and trade prints aggregated into uniform discrete decision epochs $\Delta t \in [100\text{ms}, 1\text{s}]$.
- **Data Feeds:** Level-1 and Level-2 LOB depth (best bid/ask prices, top-5 queue volumes), market order trade flow (direction, execution size), microprice, and trade timestamps.
- **Innovation Forecasting:** Deep ensemble of $K=5$ probabilistic neural networks modeling conditional innovations $Z_{t+1} \mid (X_t, a_t)$.

## Execution assumptions

- **Execution Model:** Passive limit order posting at quoted spreads $S_t - \delta_t^{\text{bid}}$ and $S_t + \delta_t^{\text{ask}}$ with participation fractions $q_t^{\text{bid}}, q_t^{\text{ask}}$.
- **Fill Simulation:** Fill ratios $\varphi^{\text{side}}(\delta) = \exp(-\kappa \delta)$ calibrated against historical fill intensities from order book queue depletion.
- **Transaction Costs:** Proportional exchange fee/rebate schedule ($c_t = -0.2\text{ bps}$ maker rebate or $+0.5\text{ bps}$ fee).
- **Terminal Liquidation:** Quadratic terminal penalty $\gamma_T I_T^2$ forcing inventory closure before session end.

## Evidence

### Source-reported

All quantitative figures below are directly reported by Ying Chen, Hoa Nguyen, Julian Sester, Hoang Hai Tran, and Yijiong Zhang (arXiv:2607.08291v1, revised August 2026):

1. **Simulation Performance across 6 Market Environments (Table 1):**
   - **Stable Baseline Regime:**
     - Greedy benchmark: Sharpe = **38.19**, Volatility = **49.37**, Max Drawdown = **-6.26**.
     - Validation-Sharpe Robust policy ($(\bar{\varepsilon}, \delta) = (4, 1)$): Sharpe = **47.03** (**+23.1%** improvement), Volatility = **39.23** (**-20.5%** reduction), Max Drawdown = **-4.61** (**+26.4%** improvement).
     - Validation-PnL Robust policy ($(\bar{\varepsilon}, \delta) = (10^{-4}, 0.1)$): Preserves raw PnL close to greedy while mitigating tail risk.
   - **Price Stress Regime:**
     - Robust policy improves Sharpe by **21.8%**, reduces volatility by **20.1%**, and improves drawdowns by **15.8%**.
   - **Liquidity Dry-out Regime:**
     - Robust policy increases Sharpe from **31.47** to **41.62** (**+32.3%**), while average inventory exposure drops by **85.1%**.
   - **Directional Order-Flow Imbalance Regimes:**
     - *Buy-arrival imbalance:* Sharpe improves from **16.92** to **28.37** (**+67.7%**), volatility falls by **40.2%**, and terminal inventory accumulation drops from **-88.15** to **-34.05** (**-61.4%**).
     - *Sell-arrival imbalance:* Sharpe improves from **12.88** to **23.43** (**+81.9%**), volatility falls by **45.3%**, and inventory drops from **125.04** to **53.38** (**-57.3%**).

2. **Adaptive Quoting Behavior Dynamics (Table 2):**
   - Under price and fill stress, the robust policy widens bid/ask spreads by **8.4% to 10.5%** (e.g., mean bid spread widens from 0.083 to 0.090 ticks) to capture wider liquidity premiums.
   - Under directional order-flow imbalance, the robust policy **narrows** spreads by **1.6% to 7.1%** (e.g., under buy imbalance, bid narrows from 0.070 to 0.065 ticks; ask narrows from 0.125 to 0.120 ticks) and reduces spread variance by **25.0% to 52.2%**, aggressively providing counterparty liquidity to clear inventory.

3. **Dominance of Action Robustness:**
   - Hyperparameter heatmaps and Shapley value feature importance confirm that **action robustness ($\delta$) exerts a substantially stronger empirical impact on policy stability than uncertainty tolerance ($\bar{\varepsilon}$)**.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- None identified in the reviewed paper; absence is not evidence of no negative result.
- Authors explicitly demonstrate that in low-liquidity environments, excessive robustness ($\bar{\varepsilon} > 5, \delta < 0.1$) reduces net profitability: the agent sets excessively defensive spreads, collapsing fill rates and starving the strategy of spread capture revenue.

## Falsification plan

1. **Ablation of Hawkes Self-Excitation States ($Z^{\text{bid}} = Z^{\text{ask}} = 0$):** Retrain the actor-critic network without Hawkes features. If out-of-sample inventory drawdowns under order-flow imbalance do not worsen by $\ge 30\%$, the Hawkes self-excitation mechanism is redundant.
2. **Action Robustness ($\delta$) Perturbation Test:** Vary $\delta \in [0.01, 10.0]$ under fixed $\bar{\varepsilon} = 1.0$. If policy spread decisions and inventory volatility show no statistically significant shift across $\delta$, the two-dimensional robustness thesis is falsified.
3. **Execution Latency Injection:** Inject an artificial round-trip cancellation/replacement delay of $50\text{ms}$ to $500\text{ms}$. If adverse selection cancels out $>75\%$ of the PnL advantage over Avellaneda-Stoikov, the RL policy overfits to instantaneous quote updates.
4. **Rejection Threshold:** Reject the market-making policy if realized daily Sharpe ratio drops below $1.5$ under a $0.5\text{ bps}$ maker fee schedule over 20 consecutive trading sessions.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Crypto LOB Microstructure:** Applicable to high-frequency perpetual books (e.g., Binance BTCUSDT, ETHUSDT, Hyperliquid perps).
- **Asymmetric Toxicity & Latency Arbitrage:** Crypto perpetual order books face aggressive toxic taker flow from cross-exchange latency arbitrage and liquidation bots. The fill probability model $\varphi^{\text{side}}(\delta)$ must incorporate mark-index price divergence and toxic taker flags.
- **Inventory Carrying & Funding Drift:** Unlike equity sessions that close daily ($T = 6.5\text{h}$), crypto trades 24/7. The terminal liquidation penalty must be replaced by continuous funding-rate-aware inventory penalization.

## Limitations

- **Single Representative Agent:** The model does not account for strategic feedback where other competing market makers simultaneously adjust their quotes in response to the agent's actions.
- **Fill Function Stationarity:** The empirical backtest uses a stationary parametric fill probability model calibrated from training data; in live flash-crash events, fill probabilities deviate from historical curves.
- **Computational Training Overhead:** Training deep ensemble innovation models and Sinkhorn-robust actor-critic networks requires substantial GPU training time, though inference latency remains sub-millisecond.

## Implementation status

`not-implemented` in the quantitative production stack.

## Adoption boundary

Research capture only. A record being present in this repository does not constitute authorization for deployment, implementation in PyBroker/Nautilus, or allocation of capital in paper, testnet, or live trading.

## Related Wiki records

- `[[quant/sequential-limit-order-execution-quoting-signal-adaptive-triangular-hjb-2026-09-02]]`
- `[[quant/market-making-online-lob-action-dependent-feedback-2026-09-02]]`
- `[[quant/hawkes-self-exciting-lob-return-sign-forecasting-coe-2026-09-02]]`

## Sources

1. Ying Chen, Hoa Nguyen, Julian Sester, Hoang Hai Tran, Yijiong Zhang, *"Robustness in Sequential Decision Making under Evolving Uncertainty: Evidence from High-Frequency Market Making"*, arXiv preprint `arXiv:2607.08291v1 [q-fin.TR]`, July 13, 2026 (revised August 24, 2026). DOI: [10.48550/arXiv.2607.08291](https://doi.org/10.48550/arXiv.2607.08291). Stable URL: [https://arxiv.org/abs/2607.08291](https://arxiv.org/abs/2607.08291).
