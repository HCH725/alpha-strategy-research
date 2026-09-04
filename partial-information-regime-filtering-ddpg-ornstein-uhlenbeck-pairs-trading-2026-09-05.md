---
schema: strategy-research-record-v1
title: "Partial-Information Optimal Pairs Trading via Decoupled GRU Regime-Filtering and Deep Deterministic Policy Gradients (prob-DDPG) on Latent-State Ornstein-Uhlenbeck Processes"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - pairs-trading
  - reinforcement-learning
  - deep-reinforcement-learning
  - ddpg
  - gated-recurrent-unit
  - gru
  - ornstein-uhlenbeck
  - partial-information
  - markov-regime-switching
  - mean-reversion
  - intraday-high-frequency
status: research-only
confidence: high
source_as_of: 2025-10-31
sources:
  - "Andrea Macrì, Sebastian Jaimungal, and Fabrizio Lillo, 'Deep reinforcement learning for optimal trading with partial information', arXiv:2511.00190v1 [q-fin.TR], October 31, 2025. https://arxiv.org/abs/2511.00190"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Partial-Information Optimal Pairs Trading via Decoupled GRU Regime-Filtering and Deep Deterministic Policy Gradients (prob-DDPG) on Latent-State Ornstein-Uhlenbeck Processes

## Provenance

- **Primary Source:** Andrea Macrì (Scuola Normale Superiore, Pisa), Sebastian Jaimungal (Department of Statistical Sciences, University of Toronto; Oxford-Man Institute for Quantitative Finance, University of Oxford), and Fabrizio Lillo (Scuola Normale Superiore, Pisa; Dipartimento di Matematica, University of Bologna), *"Deep reinforcement learning for optimal trading with partial information"*, arXiv preprint `arXiv:2511.00190v1 [q-fin.TR]` (cross-listed `cs.LG`), submitted October 31, 2025.
- **Canonical arXiv Abstract URL:** [https://arxiv.org/abs/2511.00190](https://arxiv.org/abs/2511.00190)
- **Canonical DOI:** [https://doi.org/10.48550/arXiv.2511.00190](https://doi.org/10.48550/arXiv.2511.00190)
- **Full-Text HTML Source:** [https://arxiv.org/html/2511.00190v1](https://arxiv.org/html/2511.00190v1)
- **Primary LaTeX Source Package:** Audited directly from unpacked source files `Optimal_Trading_with_Partial_Information.tex`, `preamble.tex`, `biblio.bib`, and figures in `arXiv:2511.00190` (downloaded from `https://arxiv.org/src/2511.00190`). All mathematical equations, neural network hyperparameters, training routines, and empirical tables in this record trace directly to the primary LaTeX source.
- **Pre-Write Deduplication & Identity Audit:** An exhaustive audit across all 379 markdown strategy records in `alpha-strategy-research` confirmed zero existing records matching `2511.00190`, `Macrì`, `Macri`, `prob-DDPG`, `hid-DDPG`, or `reg-DDPG`. While existing pairs trading records in the repository examine deep LSTM factor replication (`statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05.md`), exploratory continuous-time optimal stopping (`exploratory-reinforcement-learning-sequential-optimal-stopping-pairs-trading-2026-09-05.md`), or signature kernels (`signature-optimal-execution-statistical-arbitrage-quadratic-reduction-2026-09-02.md`), none investigate continuous-action Actor-Critic control under partial-information Markov regime switching where filtering of latent mean-reversion equilibrium states is decoupled from policy optimization.

## Economic mechanism

### Source-reported

In continuous-time statistical arbitrage and pairs trading, the price differential or synthetic co-integrated portfolio is conventionally modeled as an Ornstein–Uhlenbeck (OU) mean-reverting diffusion:
$$dS_t = \kappa_t (\theta_t - S_t) \, dt + \sigma_t \, dW_t$$
where $\theta_t > 0$ is the long-run equilibrium level toward which the process reverts, $\kappa_t \ge 0$ is the mean-reversion speed, and $\sigma_t > 0$ is the diffusion volatility.

In real financial markets, however, these parameters are non-stationary and unobservable: structural shifts, company fundamentals, microstructural rebalancing, and macro regimes cause discrete, stochastic shifts in $\theta_t$, $\kappa_t$, and $\sigma_t$. When parameters are latent, classical fixed-threshold pairs trading (e.g., static or rolling $Z$-scores) and standard stochastic control heuristics break down:
1. **The Falling Knife Phenomenon:** If the equilibrium mean drops from $\theta = 1.1$ to $\theta = 0.9$, an observed spread level of $S_t = 0.95$ appears undervalued relative to historical averages. A naive trader enters a long position, expecting an upward reversion, but the asset is in fact overvalued relative to its new latent regime ($\theta = 0.9$), causing severe capital loss.
2. **Failure of End-to-End Black-Box RL (`hid-DDPG`):** Feeding raw recurrent hidden states from a Gated Recurrent Unit (GRU) directly into an Actor-Critic architecture bundles representation learning with policy optimization. This causes severe action clustering, counter-intuitive rebalancing (e.g., selling when spread is low and inventory is positive), and degraded out-of-sample rewards due to overfitting to noisy continuous representations.
3. **Failure of Direct Price Forecasting (`reg-DDPG`):** Training a model to forecast the one-step-ahead signal level $\tilde{S}_{t+1}$ yields negligible value for reinforcement learning in high-frequency diffusions. Single-step point forecasts in high-noise environments have low signal-to-noise ratio and fail to communicate the multi-horizon drift induced by the latent equilibrium regime.
4. **Superiority of Decoupled Probabilistic Filtering (`prob-DDPG`):** Macrì, Jaimungal, and Lillo demonstrate that optimal trading under partial information requires separating state estimation from policy optimization. By training a GRU classifier offline to output the posterior probability distribution $\Phi_{t,k} = \mathbb{P}(\theta_t = \phi_k \mid \{S_u\}_{u=t-W}^t)$ across latent regimes, and conditioning the Deep Deterministic Policy Gradient (DDPG) agent on the state tuple $(S_t, I_t, \Phi_t)$, the agent learns economically interpretable, regime-conditional inventory rebalancing policies that substantially outperform both end-to-end RL and classical rolling $Z$-score baselines.

### Research interpretation

The proposed strategy captures **structural-regime-aware relative-value alpha**. Rather than assuming that cointegration spreads fluctuate around a static zero or constant rolling mean, it treats the spread as a piecewise-stationary jump-diffusion whose equilibrium anchor jumps between unobserved discrete states.

By formalizing the problem as a partially observable Markov decision process (POMDP) and solving it via a two-stage architecture:
1. Stage 1 acts as a non-linear Bayesian filter (a GRU parameterized as an approximate filter) that transforms an unobservable continuous path history into a low-dimensional simplex of regime probabilities $\Phi_t \in \Delta^{K-1}$.
2. Stage 2 solves the continuous-inventory Hamilton-Jacobi-Bellman (HJB) control problem via DDPG actor-critic optimization, adjusting inventory $I_{t+1}$ smoothly to balance mean-reversion drift against transaction cost friction $\lambda |I_{t+1} - I_t|$.

This architecture effectively resolves the "regime-shift hazard" in statistical arbitrage: when the posterior probability indicates a regime transition, the agent rapidly sheds inventory or flips directional exposure before the naive spread-divergence signal triggers large losses.

## Signal

### Mathematical Formulation and State Space

The trading signal represents an autonomous, discrete-time, continuous-action inventory rebalancing policy executed at fixed time intervals $\tau$ (or $\Delta t$).

#### 1. Observable Information and Signal Window
- At discrete decision time $t \in \mathbb{N}$, the agent observes:
  - Current signal / synthetic portfolio level: $S_t \in \mathbb{R}$.
  - Current inventory holding: $I_t \in [-I_{\max}, I_{\max}]$.
  - Rolling window of historical observations of length $W+1$: $\{S_u\}_{u=t-W}^t \in \mathbb{R}^{W+1}$.

#### 2. Stage 1: Latent Regime Filtering Network (`prob-DDPG`)
- **Input:** Min-max normalized window sequence $\mathbf{Z}_t = [S_{t-W}, S_{t-W+1}, \dots, S_t] \in \mathbb{R}^{b \times (W+1)}$.
- **Recurrent Encoder (GRU):** Composed of $d_l$ recurrent layers with hidden dimension $d_h$. For sequence step $k \in \{0, \dots, W\}$ and previous hidden state $\mathbf{h}_{k-1} \in \mathbb{R}^{d_h}$:
  - Reset gate: $\mathbf{p}_k = \sigma(\mathbf{U}_p \mathbf{h}_{k-1} + \mathbf{H}_p \mathbf{Z}_k + \tilde{\mathbf{b}}_p)$
  - Update gate: $\mathbf{z}_k = \sigma(\mathbf{U}_z \mathbf{h}_{k-1} + \mathbf{H}_z \mathbf{Z}_k + \tilde{\mathbf{b}}_z)$
  - Candidate state: $\tilde{\mathbf{h}}_k = \tanh(\mathbf{U}_h (\mathbf{p}_k * \mathbf{h}_{k-1}) + \mathbf{H}_h \mathbf{Z}_k + \tilde{\mathbf{b}}_h)$
  - Updated hidden state: $\mathbf{h}_k = (1 - \mathbf{z}_k) * \mathbf{h}_{k-1} + \mathbf{z}_k * \tilde{\mathbf{h}}_k$
  where $\sigma(\cdot)$ is the logistic sigmoid, $\tanh(\cdot)$ is hyperbolic tangent, and $*$ is element-wise multiplication.
- **Classification Head:** The final hidden state $\mathbf{h}_W$ is passed through a multi-layer perceptron (MLP) with 5 fully connected layers (64 nodes each, SiLU activations) terminating in a SoftMax layer:
  $$\Phi_{t,k} = \mathbb{P}(\theta_t = \phi_k \mid \{S_u\}_{u=t-W}^t) = \frac{\exp(g_k(\mathbf{h}_W))}{\sum_{j=1}^K \exp(g_j(\mathbf{h}_W))}, \quad k \in \{1, \dots, K\}$$
- **Loss Function:** Trained offline via categorical cross-entropy against true or estimated historical regimes:
  $$\mathcal{L}_{\text{filter}} = - \frac{1}{b} \sum_{i=1}^b \sum_{k=1}^K y_k^{(i)} \log \Phi_{t,k}^{(i)}$$

#### 3. Stage 2: Actor-Critic Optimal Inventory Rebalancing (DDPG)
- **Augmented State Vector:**
  $$\mathbf{G}_t = \left(S_t, I_t, \Phi_{t,1}, \Phi_{t,2}, \dots, \Phi_{t,K}\right)$$
  normalized into $[0, 1]^{K+2}$.
- **Actor Network $\pi(\mathbf{G}_t \mid \mu_\pi)$:**
  - Feed-forward neural network with $l_{\text{NN}}$ hidden layers of $d_{\text{NN}}$ nodes, SiLU activation functions.
  - Final layer with $\tanh$ activation scaled by $I_{\max}$:
    $$a_t = I_{t+1} = I_{\max} \cdot \tanh(\mathbf{W}_\pi \mathbf{h}_{\text{actor}} + \mathbf{b}_\pi) \in [-I_{\max}, I_{\max}]$$
- **Critic Network $Q(\mathbf{G}_t, a_t \mid \mu_Q)$:**
  - Feed-forward neural network with input dimension $(K+3)$ (state vector $\mathbf{G}_t$ concatenated with action $a_t = I_{t+1}$).
  - Evaluates expected discounted return $Q(\mathbf{G}_t, a_t)$.
- **Target Network & Soft Update:**
  - Target networks $\pi_{\text{tgt}}$ and $Q_{\text{tgt}}$ updated via Polyak averaging:
    $$\mu_{Q_{\text{tgt}}} \leftarrow \tau_{\text{soft}} \mu_Q + (1 - \tau_{\text{soft}}) \mu_{Q_{\text{tgt}}}, \quad \mu_{\pi_{\text{tgt}}} \leftarrow \tau_{\text{soft}} \mu_\pi + (1 - \tau_{\text{soft}}) \mu_{\pi_{\text{tgt}}}$$
    with soft update coefficient $\tau_{\text{soft}} = 0.001$ (`source-reported`).
- **Reward Function:**
  The per-step reward accounting for mark-to-market portfolio gains and proportional transaction costs $\lambda \ge 0$ is:
  $$r_t = \Delta BV_t - \lambda |I_{t+1} - I_t| = I_{t+1} (S_{t+1} - S_t) - \lambda |I_{t+1} - I_t|$$
  where $q_t = I_{t+1} - I_t$ is the trading volume executed at time $t$.
- **Critic Optimization:**
  One-step Bellman squared error loss:
  $$\mathcal{L}_1(\mu_Q) = \frac{1}{b} \sum_{i=1}^b \left( Q(\mathbf{G}_t^{(i)}, I_{t+1}^{(i)} \mid \mu_Q) - \left[ r_t^{(i)} + \gamma Q_{\text{tgt}}(\mathbf{G}_{t+1}^{(i)}, \pi_{\text{tgt}}(\mathbf{G}_{t+1}^{(i)} \mid \mu_{\pi_{\text{tgt}}}) \mid \mu_{Q_{\text{tgt}}} \right] \right)^2$$
- **Actor Optimization (Policy Gradient):**
  $$\nabla_{\mu_\pi} \mathcal{L}_2 \approx \frac{1}{b} \sum_{i=1}^b \left[ \left. \nabla_a Q(\mathbf{G}_t^{(i)}, a \mid \mu_Q) \right|_{a = \pi(\mathbf{G}_t^{(i)} \mid \mu_\pi)} \cdot \nabla_{\mu_\pi} \pi(\mathbf{G}_t^{(i)} \mid \mu_\pi) \right]$$
- **Exploration Noise:**
  Additive exploration noise during training: $I_{t+1} = \pi(\mathbf{G}_t \mid \mu_\pi) + \mathcal{N}(0, \varepsilon_m)$ where $\varepsilon_m = \max(a / (a + m), \varepsilon_{\min})$ with $a = 100$ (`source-reported`), decaying monotonically with training iteration $m$.

### Architecture Comparison (Benchmark Baselines in Source)

The source evaluates three structural paradigms:
1. `prob-DDPG` (Proposed): Decoupled two-step architecture. First trains GRU classifier for $\Phi_t$, then feeds $(S_t, I_t, \Phi_t)$ into DDPG.
2. `hid-DDPG` (End-to-End One-Step): Trains GRU jointly with DDPG, passing raw hidden state $o_t = \mathbf{h}_W \in \mathbb{R}^{d_h}$ directly into DDPG alongside $(S_t, I_t)$.
3. `reg-DDPG` (Predictive Two-Step): First trains GRU regressor to forecast next signal value $\tilde{S}_{t+1}$, then feeds $(S_t, I_t, \tilde{S}_{t+1})$ into DDPG.
4. `Rolling Z-Score` (Classical Heuristic Benchmark): Inventory chosen inversely proportional to the rolling $Z$-score of the spread:
   $$I_{t+1} = - \text{clip}\left(\frac{S_t - \mu_W(S)}{\sigma_W(S)}, -I_{\max}, I_{\max}\right)$$
   using identical window $W = 100$.

## Required data

### Synthetic Experiment Specification (`source-reported`)
- Data Generating Process: Continuous Ornstein-Uhlenbeck SDE:
  $$dS_t = \kappa_t (\theta_t - S_t) \, dt + \sigma_t \, dW_t$$
- Simulation Step: $\Delta t = 0.2$, episode length $n = 2,000$ steps (`source-reported`).
- Invariant Starting Distribution: $S_{t-W} \sim \mathcal{N}(\mu_{\text{inv}}, 3 \sigma_{\text{inv}})$ where $\sigma_{\text{inv}} = \frac{\sigma}{2\kappa}$ and $\mu_{\text{inv}} = 1.0$ (`source-reported`).
- Markov Regime Setups:
  1. $\theta_t \in \{0.9, 1.0, 1.1\}$, constant $\kappa = 5.0$, $\sigma = 0.2$. Transition rate matrix:
     $$A_\theta = \begin{bmatrix} -0.1 & 0.05 & 0.05 \\ 0.05 & -0.1 & 0.05 \\ 0.05 & 0.05 & -0.1 \end{bmatrix}$$
  2. $\theta_t \in \{0.9, 1.0, 1.1\}$, $\kappa_t \in \{3.0, 7.0\}$, constant $\sigma = 0.2$. Transition rate matrix:
     $$A_\kappa = \begin{bmatrix} -0.1 & 0.1 \\ 0.1 & -0.1 \end{bmatrix}$$
  3. $\theta_t \in \{0.9, 1.0, 1.1\}$, $\kappa_t \in \{3.0, 7.0\}$, $\sigma_t \in \{0.1, 0.3\}$. Transition rate matrix:
     $$A_\sigma = \begin{bmatrix} -0.1 & 0.1 \\ 0.1 & -0.1 \end{bmatrix}$$

### Empirical Market Data Specification (`source-reported`)
- **Venue & Market:** NASDAQ equity market.
- **Instruments:**
  - Asset 1: Intel Corporation common stock (`INTC`).
  - Asset 2: Merrill Lynch Semiconductor ETF (`SMH`), where INTC represents approximately 20% of ETF holdings.
- **Data Source:** LOBSTER database (limit order book events up to Level 1: best bid and ask).
- **Event Filtering:** Trade events only (every element represents a transaction), reconstructed into a 1-second sampled mid-price series:
  $$S_t = \frac{P_t^{\text{bid}} + P_t^{\text{ask}}}{2}$$
- **Sample Period:** August 29, 2025 to September 5, 2025 (`source-reported`):
  - Training Set: August 29, 2025 to September 4, 2025 (72,700 1-second observations).
  - Out-of-Sample Testing Set: September 5, 2025 (19,789 1-second observations).
- **Cointegration Vector Construction (`source-reported`):**
  - Johansen test on INTC and SMH confirms cointegration at the 5% significance level: Trace Stat = 27.456 (Critical Value = 18.399, Reject $H_0$), Max-Eigenvalue Stat = 19.222 (Critical Value = 17.148, Reject $H_0$).
  - Discrete VAR(1) model fitted on mid-price changes: $\Delta \mathbf{S}_t = \vec{A} + \mathbf{B} \Delta \mathbf{S}_{t-1} + \vec{\varepsilon}_t$.
    - Estimated coefficients: $B_{11}(\Delta S_{\text{SMH}}) = 0.999^{***}$, $B_{12}(\Delta S_{\text{INTC}}) = 0.00001$, $A_{\text{SMH}} = 0.021$; $B_{21}(\Delta S_{\text{SMH}}) = 0.0007$, $B_{22}(\Delta S_{\text{INTC}}) = 0.996^{***}$, $A_{\text{INTC}} = 0.003$.
  - Continuous mean-reversion drift matrix: $\kappa = (\mathbb{I} - \mathbf{B}) / \Delta t$.
  - Eigenvalue decomposition: $\kappa = U^{-1} \Lambda U$ with diagonal matrix $\Lambda = \text{diag}(8.67 \cdot 10^{-5}, 3.59 \cdot 10^{-4})$.
  - Maximal mean-reverting eigenvector (second row of $U^{-1}$) defines the stationary synthetic spread portfolio:
    $$\tilde{S}_t = 2.856 \times S_t^{\text{smh}} - 0.804 \times S_t^{\text{intc}}$$
- **Empirical Regime Estimation:**
  - Min-max normalization applied to $\tilde{S}_t$ over the training set.
  - Hamilton (1989) two-state Markov switching model fitted to $\tilde{S}_t$ yields two equilibrium regimes: $\theta_1 = 0.2216$ and $\theta_2 = 0.5658$ (`source-reported`).

## Execution assumptions

### Source-Reported Execution Model
- **Trading Cadence:** Discrete updates at $\Delta t = 1$ second (empirical) and $\Delta t = 0.2$ (simulated).
- **Execution Fill Price:** Fills are assumed to execute instantly at the prevailing mid-price $S_t$ (`source-reported`).
- **Transaction Cost Model:** Proportional linear transaction cost parameter $\lambda = 0.05$ per unit volume:
  $$\text{Cost}_t = \lambda |I_{t+1} - I_t|$$
  applied to every inventory adjustment (`source-reported`).
- **Inventory Bounds:** Hard bounds $I_t \in [-I_{\max}, I_{\max}]$ with $I_{\max} = 10$, $I_{\min} = -10$ enforced via tanh actor scaling (`source-reported`).
- **Initial Conditions:** All testing episodes start with $I_0 = 0$ inventory and normalized initial spread $S_0 = 1.0$ (`source-reported`).
- **Market Impact:** Zero permanent market impact assumed; trading actions do not perturb the underlying mid-price process (`source-reported`).

### Research-Proposed Execution Caveats & Gaps
- **Spread Crossing and Adverse Selection:** `research-proposed`: The primary source evaluates returns against mid-prices with a static penalty $\lambda = 0.05$. In real Level 1 execution, adjusting inventory at 1-second cadence incurs half-spread crossing fees ($P^{\text{ask}} - P^{\text{mid}}$ on buys, $P^{\text{mid}} - P^{\text{bid}}$ on sells) plus adverse selection from toxic flow.
- **Taker Fee & Slippage:** `research-proposed`: On NASDAQ equity pairs or crypto perpetuals, 1-second continuous rebalancing will generate prohibitive taker fees unless orders are executed via passive limit orders with queuing priority models or rebalancing is down-sampled to 5s-1m intervals.

## Evidence

### Source-reported

All numerical performance figures, parameter choices, and empirical statistics below are directly transcribed from the primary source (`arXiv:2511.00190v1`, Tables 1, 2, 3, 4, 6, 7, 8, 9 and Figures 5, 6, 7, 11, 12):

#### 1. Synthetic Simulation Performance (Table 4)
Evaluated after $n = 2,000$ trades across $M = 500$ independent out-of-sample test episodes with transaction cost $\lambda = 0.05$:

| Simulation Environment | Model / Architecture | Average Cumulative Reward | Std. Dev. | Source Location |
| :--- | :--- | :--- | :--- | :--- |
| **Setup 1: $\theta_t$ Markov Chain** | `hid-DDPG` (One-step) | $15.70$ | $1.39$ | Table 4, arXiv:2511.00190v1 |
| ($\kappa = 5.0, \sigma = 0.2$ constant) | `reg-DDPG` (Two-step regressor) | $8.69$ | $0.60$ | Table 4, arXiv:2511.00190v1 |
| | `prob-DDPG` (Two-step regime filter) | **$25.65$** | **$3.35$** | Table 4, arXiv:2511.00190v1 |
| **Setup 2: $\theta_t, \kappa_t$ Markov Chains** | `hid-DDPG` (One-step) | $8.08$ | $1.54$ | Table 4, arXiv:2511.00190v1 |
| ($\sigma = 0.2$ constant) | `reg-DDPG` (Two-step regressor) | $2.95$ | $0.30$ | Table 4, arXiv:2511.00190v1 |
| | `prob-DDPG` (Two-step regime filter) | **$15.59$** | **$3.83$** | Table 4, arXiv:2511.00190v1 |
| **Setup 3: $\theta_t, \kappa_t, \sigma_t$ Markov Chains** | `hid-DDPG` (One-step) | $1.29$ | $3.49$ | Table 4, arXiv:2511.00190v1 |
| (Fully stochastic 3-parameter regimes) | `reg-DDPG` (Two-step regressor) | $-0.07$ | $0.11$ | Table 4, arXiv:2511.00190v1 |
| | `prob-DDPG` (Two-step regime filter) | **$4.51$** | **$3.75$** | Table 4, arXiv:2511.00190v1 |

#### 2. Real Market Pairs Trading Performance (Table 9)
Evaluated on NASDAQ high-frequency trade data for the cointegrated pair SMH / INTC on September 5, 2025 (19,789 1-second out-of-sample observations, transaction cost $\lambda = 0.05$):

| Strategy / Model | Average Cumulative Reward | Std. Dev. | Realized Net Result | Source Location |
| :--- | :--- | :--- | :--- | :--- |
| **`prob-DDPG` (Proposed)** | **$+0.1795$** | **$0.1329$** | **Consistently positive returns** | Table 9, arXiv:2511.00190v1 |
| **`hid-DDPG` (One-step baseline)** | **$-0.2883$** | **$0.1282$** | Negative returns (underperformed) | Table 9, arXiv:2511.00190v1 |
| **Rolling $Z$-Score ($W=100$)** | **$-0.8432$** | **$0.4341$** | Severe losses (churned by fees) | Table 9, arXiv:2511.00190v1 |

#### 3. Exact Hyperparameters Confirmed in Primary Source
- DDPG Training: Adam learning rate $\eta = 0.001$, discount factor $\gamma = 0.999$, batch size $b = 512$ (simulated) / $b = 64$ (empirical), training episodes $N = 10,000$, soft target update parameter $\tau_{\text{soft}} = 0.001$.
- Network Topologies:
  - `prob-DDPG`: GRU encoder $d_l = 5$ layers, $d_h = 20$ nodes ($d_l = 6, d_h = 64$ for empirical); Actor MLP $l_{\text{NN}} = 5$ layers, $d_{\text{NN}} = 64$ nodes; Critic MLP $l_{\text{NN}} = 5$ layers, $d_{\text{NN}} = 64$ nodes.
  - `hid-DDPG`: GRU encoder $d_l = 1$ layer ($d_l = 2$ for 3-MC), $d_h = 10$ nodes; Actor/Critic MLP $l_{\text{NN}} = 4$ layers, $d_{\text{NN}} = 20$ nodes.
  - `reg-DDPG`: GRU encoder $d_l = 5$ layers, $d_h = 20$ nodes, lookback window $W = 50$, predict horizon $1$.

### Independently reproduced

Not independently reproduced. All empirical findings and simulation results above represent source-reported metrics published by Macrì, Jaimungal, and Lillo (arXiv:2511.00190v1, October 2025).

### Negative evidence

1. **Failure of Point-Forecasting (`reg-DDPG`):** Direct regression of next-step signal value $\tilde{S}_{t+1}$ completely fails in complex environments. In the 3-regime setup ($\theta_t, \kappa_t, \sigma_t$), `reg-DDPG` delivers an average reward of $-0.07 \pm 0.11$. The authors observe that the agent collapses into near-zero trading activity ($q_t \approx 0$), as single-step point forecasts in high-noise diffusions contain near-zero actionable direction.
2. **Catastrophic Failure of Rolling $Z$-Score under Friction:** The classical rolling $Z$-score benchmark produced an average cumulative reward of $-0.8432 \pm 0.4341$ on the out-of-sample test day. In high-frequency 1-second trading, threshold crossing generates excessive portfolio turnover, and without regime filtering, the heuristic repeatedly buys falling spreads whose equilibrium mean has downshifted.
3. **End-to-End Joint RL Instability (`hid-DDPG`):** While `hid-DDPG` achieves positive rewards in stylized simulations, it produces negative cumulative returns on real market data ($-0.2883 \pm 0.1282$). Inspecting action policies reveals that raw GRU hidden states cause erratic, non-interpretable clustering of buy/sell actions that fail to generalize out-of-sample.

## Falsification plan

### Operational Falsification Protocols

1. **Full Bid-Ask Spread Crossing & Order-Book L2 Queue Simulation:**
   - *Protocol:* Replace mid-price execution with explicit order book fill simulation on NASDAQ LOBSTER data or Binance tick data. Buys execute at ask; sells execute at bid.
   - *Falsification Metric:* Net cumulative reward after exchange fee schedules (e.g., 1.5 bps taker fee on NASDAQ, 4 bps on crypto).
   - *Research-Defined Falsification Threshold:* If `prob-DDPG` cumulative reward degrades below $0.0$ or realizes an annualized out-of-sample Sharpe ratio $< 0.8$, the hypothesis that latent regime filtering overcomes microstructural execution friction is falsified.
2. **Look-Ahead & Regime-Fitting Leakage Test:**
   - *Protocol:* In the empirical study, Hamilton (1989) regime states were estimated on the in-sample training window. Test the filter using an expanding-window online Hamilton filter or rolling online Dirichlet process Gaussian Mixture Model where regime anchors $\theta_k$ are updated strictly on historical data without full-sample lookahead.
   - *Research-Defined Falsification Threshold:* If out-of-sample regime classification accuracy drops below 60% or cumulative trading rewards decrease by $> 50\%$ compared to static regime anchors, the reported alpha is driven by in-sample regime pre-knowledge.
3. **Cointegration Breakdown / Spurious Pair Placebo Test:**
   - *Protocol:* Pair assets that pass short-term correlation tests but fail long-term Johansen cointegration (e.g., synthetically generated non-cointegrated random walks with matching drift and volatility).
   - *Research-Defined Falsification Threshold:* The agent must detect lack of mean-reversion drift and contract inventory to $|I_t| \approx 0$. If the policy incurs drawdowns exceeding $10 \times I_{\max} \cdot \sigma$, the architecture lacks true structural resilience and blindly overtrades spurious mean-reversion.
4. **Timeframe Down-Sampling Stress Test:**
   - *Protocol:* Evaluate policy performance across down-sampled frequencies: $\Delta t \in \{5\text{s}, 15\text{s}, 1\text{m}, 5\text{m}\}$.
   - *Research-Defined Falsification Threshold:* If cumulative returns degrade monotonically to negative values when rebalancing frequency decreases to 1-minute bars, the strategy is an artifact of 1-second quote bouncing rather than genuine economic equilibrium reversion.

## Crypto portability

- **Portability Status:** `adapted` / `unproven` (`research-proposed`). The primary paper evaluates the framework exclusively on simulated diffusions and NASDAQ equity high-frequency LOB data (INTC vs SMH). Applying this methodology to cryptocurrency markets represents a ported research hypothesis that has not been demonstrated by the authors.

### Crypto-Specific Microstructural Adaptation Risks (`research-proposed`)
1. **Perpetual Futures Basis & Funding Drag:**
   - In crypto, pairs trading is typically conducted between perpetual swap contracts (e.g., ETH/USDT vs BTC/USDT or SOL/USDT).
   - Perpetual contracts incur 8-hour funding rates:
     $$\text{Funding PnL}_t = - \sum_{i \in \{\text{long}, \text{short}\}} I_{i,t} P_{i,t} \cdot F_{i,t}$$
   - If the long leg trades at a persistent positive funding premium relative to the short leg, holding the synthetic spread across multi-hour regimes can completely consume mean-reversion gross margin. The reward function must be adapted:
     $$r_t^{\text{crypto}} = \Delta BV_t - \lambda |I_{t+1} - I_t| - \text{FundingCost}_t$$
2. **Non-Stationary Cointegration in Altcoins:**
   - Crypto token relationships rarely exhibit stationary cointegration over extended periods; narrative shifts, token unlocks, and protocol exploits induce permanent cointegration breaks.
   - An online Johansen or Engle-Granger test must serve as an outer regime gate: if eigenvalue test statistics fall below the 95% critical threshold, the entire pair trading book must be unwound to cash.
3. **Execution Latency and WebSocket Disconnections:**
   - 1-second rebalancing over public exchange REST/WebSocket APIs introduces non-negligible network jitter (50–300 ms). An agent attempting 1-second continuous rebalancing will suffer adverse selection from centralized exchange Colocation/VIP market makers. Execution intervals should be down-sampled to $15\text{s} - 1\text{m}$ (`research-proposed`).

## Limitations

- **Mid-Price Fill Fiction:** The empirical backtest evaluates trades against 1-second filtered mid-prices with a flat $\lambda = 0.05$ penalty. It does not model LOB depth consumption, queue wait times, or partial fills.
- **Short Empirical Out-of-Sample Window:** The empirical NASDAQ evaluation is conducted over a single day (September 5, 2025, 19,789 seconds) following five days of training (August 29 - September 4, 2025). While 19,789 high-frequency observations provide statistical power for tick dynamics, one calendar day cannot capture macro regime switches, FOMC releases, or multi-week cointegration drift.
- **Pre-Determined Regime Count:** The Hamilton filter assumes a fixed number of regimes ($K=2$ in empirical data, $K=3$ in simulation). If the market enters a novel structural regime outside $\{\theta_1, \theta_2\}$, the SoftMax probabilities will be forced to misclassify the state, potentially causing substantial adverse inventory accumulation.
- **Zero Permanent Market Impact:** The model assumes the agent's trades do not move the mid-price. In larger capital deployments, trading $I_{\max} = 10$ round-lots every few seconds would generate self-adverse price impact.

## Implementation status

- `not-implemented`: This research capture represents an initial theoretical and empirical ingestion of `arXiv:2511.00190v1`.
- No prototype code exists in `nautilus-quant-system`, PyBroker, or NautilusTrader.
- No live, testnet, or paper execution has been conducted.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- This record is an academic research intake document. It does not constitute investment advice, an implementation authorization, or permission to deploy capital in paper, testnet, or live trading environments.

## Related Wiki records

- `[[quant/microstructure-mean-reversion-optimal-symmetric-band-waiting-option-2026-09-02]]` — Microstructure mean reversion and optimal band waiting times.
- `[[quant/crypto-eth-fiat-bucket-market-neutral-pairs-2026-08-31]]` — Market-neutral pairs trading structure in cryptocurrency spot/fiat markets.
- `[[quant/crypto-intraday-sign-mean-reversion-15m-walk-forward-2026-09-01]]` — Intraday mean reversion and walk-forward verification protocols.
- `[[quant/sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02]]` — Physics-informed RL frameworks for constrained portfolio control.
- `[[quant/finsmart-market-aligned-reinforcement-learning-sentiment-alpha-2026-09-02]]` — Reinforcement learning under non-stationary market regimes.

## Sources

1. **Andrea Macrì, Sebastian Jaimungal, and Fabrizio Lillo**, *"Deep reinforcement learning for optimal trading with partial information"*, arXiv preprint `arXiv:2511.00190v1 [q-fin.TR]`, submitted October 31, 2025.
   - Canonical Abstract URL: [https://arxiv.org/abs/2511.00190](https://arxiv.org/abs/2511.00190)
   - Canonical DOI: [https://doi.org/10.48550/arXiv.2511.00190](https://doi.org/10.48550/arXiv.2511.00190)
   - Full-Text HTML: [https://arxiv.org/html/2511.00190v1](https://arxiv.org/html/2511.00190v1)
   - LaTeX Source Bundle: Unpacked from `https://arxiv.org/src/2511.00190` (`Optimal_Trading_with_Partial_Information.tex`).
2. **Hamilton, J. D.** (1989), *"A new approach to the economic analysis of nonstationary time series and the business cycle"*, *Econometrica*, 57(2), 357–384. DOI: [10.2307/1912559](https://doi.org/10.2307/1912559).
3. **Lillicrap, T. P., et al.** (2015), *"Continuous control with deep reinforcement learning"*, arXiv preprint `arXiv:1509.02971`. DOI: [10.48550/arXiv.1509.02971](https://doi.org/10.48550/arXiv.1509.02971).
4. **Cartea, Á., Jaimungal, S., and Penalva, J.** (2015), *Algorithmic and High-Frequency Trading*, Cambridge University Press. DOI: [10.1017/CBO9781316335918](https://doi.org/10.1017/CBO9781316335918).
5. **Johansen, S.** (1991), *"Estimation and Hypothesis Testing of Cointegration Vectors in Gaussian Vector Autoregressive Models"*, *Econometrica*, 59(6), 1551–1580. DOI: [10.2307/2938278](https://doi.org/10.2307/2938278).
