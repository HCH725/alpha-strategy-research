---
schema: strategy-research-record-v1
title: BRaG Barycenter-Based Adversarial Inverse Reinforcement Learning Control Barrier Functions
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reinforcement-learning
  - inverse-reinforcement-learning
  - imitation-learning
  - wasserstein-barycenter
  - control-barrier-functions
  - multi-expert
  - portfolio-optimization
status: research-only
confidence: medium
source_as_of: "2026-08-16"
sources:
  - "Arishi Orra, Himanshu Choudhary, and Manoj Thakur, 'Learning Stock Trading Policies via Barycenter-Based Adversarial Inverse Reinforcement Learning', arXiv:2608.15770v1 [q-fin.TR, cs.LG], August 16, 2026. https://arxiv.org/abs/2608.15770"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BRaG: Barycenter-Based Adversarial Inverse Reinforcement Learning with Control Barrier Functions

## Provenance

- **Primary Source:** Arishi Orra, Himanshu Choudhary, and Manoj Thakur (School of Mathematical & Statistical Sciences, Indian Institute of Technology Mandi, India), *"Learning Stock Trading Policies via Barycenter-Based Adversarial Inverse Reinforcement Learning"*, arXiv preprint `arXiv:2608.15770v1 [q-fin.TR, cs.LG]`, submitted August 16, 2026.
- **Canonical Abstract URL:** https://arxiv.org/abs/2608.15770
- **Canonical HTML URL:** https://arxiv.org/html/2608.15770v1
- **Canonical PDF URL:** https://arxiv.org/pdf/2608.15770v1
- **DOI:** `10.48550/arXiv.2608.15770`
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Primary Source Data Periods:**
  - GAIL pretraining window: January 1, 2010 to December 31, 2020 (11 years).
  - PPO environment fine-tuning window: January 1, 2021 to December 31, 2023 (3 years).
  - Out-of-sample test window: January 1, 2024 to September 30, 2025 (21 months).
- **Pre-Write Deduplication Audit:**
  - Repository-wide search for `2608.15770`, `BRaG`, `Barycenter`, `Control Barrier Function`, `CBF`, and `GAIL` returned zero existing matches.
  - Distinct from `questrader-self-supervised-auxiliary-task-discovery-rl-trading-2026-09-02.md` (arXiv:2608.15841v1): while sharing co-authors, QUES-Trader focuses on discovering self-supervised auxiliary tasks (masked prediction, temporal contrastive learning) to stabilize single-agent PPO representations. BRaG introduces a completely different architecture: multi-expert distribution aggregation via a performance-weighted sliced Wasserstein barycenter, adversarial inverse reinforcement learning (GAIL) pretraining, and discrete-time control barrier functions (CBFs) that project actions into a safe drawdown-invariant subspace at execution time.
  - Distinct from `fineft-risk-aware-ensemble-rl-vae-routing-crypto-futures-2026-09-03.md`: FiNeFT utilizes variational autoencoder latent routing across crypto perpetual regimes without Wasserstein geometric barycenters, inverse reinforcement learning, or CBF quadratic-program action repair.

## Economic mechanism

### Source-reported

Reinforcement learning (RL) models sequential trading as a Markov Decision Process (MDP). However, direct deployment of deep reinforcement learning (DRL) in financial markets faces three core structural failures:
1. **Delayed, Sparse, and Noisy Rewards:** Financial markets exhibit low signal-to-noise ratios. Reward functions based purely on realized P&L induce high gradient variance and unstable exploration policies that overfit short-term market noise or collapse into local minima (Moody et al., 1998; Liu et al., 2020).
2. **Narrow Expert Bias in Imitation Learning:** Standard Inverse Reinforcement Learning (IRL) or behavioral cloning relies on demonstrations from a single expert or strategy style. In dynamic markets, a single style (e.g. trend-following or mean-reversion) fails when macro regimes switch, leading to brittle policy transfers.
3. **Absence of Hard Downside Risk Guarantees:** Classical DRL optimizes expectations (cumulative reward) and cannot enforce hard safety constraints. Soft reward penalties (e.g., negative penalties for drawdowns) frequently lead to constraint violations during out-of-distribution market panics.

BRaG resolves these issues through three structural innovations:
- **Wasserstein Barycenter Consensus:** Instead of naive demonstration pooling, BRaG aggregates multiple heterogeneous expert policies (momentum, mean-reversion, trend-following, and deep RL) by computing a Sharpe-ratio-weighted sliced Wasserstein barycenter over state-action distributions. This geometric consensus preserves multi-modal trading behavior while filtering out individual expert idiosyncratic noise.
- **Adversarial Imitation Pretraining:** Using Generative Adversarial Imitation Learning (GAIL), the agent learns an implicit surrogate reward from the barycenter demonstrations, initializing policy weights in a stable, expert-aligned subspace before facing market feedback.
- **Control Barrier Function (CBF) Invariance:** Explicit portfolio drawdown limits are enforced via discrete-time control barrier functions. Whenever an exploratory or greedy action risks violating the pre-set drawdown threshold under conservative volatility assumptions, the action is dynamically projected onto the safe action boundary via a quadratic program at execution time.

### Research interpretation

The underlying thesis is that **multi-expert geometric consensus coupled with control-theoretic safety projection decouples policy discovery from downside ruin**.

In pure RL, exploration in financial state spaces carries catastrophic downside risk: an exploratory action in a high-volatility regime can liquidate capital before the agent learns the penalty. Conversely, pure imitation learning is capped by the performance of the demonstrated experts and cannot adapt to novel market regimes.

BRaG structures the learning process into an informationally separated hierarchy:
1. **Prior Distribution Anchoring:** The sliced Wasserstein barycenter extracts the geometry of consensus across multiple orthogonal investment styles (cross-sectional momentum, time-series momentum, moving average crossover, Bollinger mean-reversion, and RL). Weighting by positive Sharpe ratio ensures that outperforming regimes dominate the reference distribution.
2. **Exploration Cold-Start Stabilization:** GAIL pretraining solves the exploration dilemma by transforming noisy market P&L into a dense distributional-matching surrogate reward, ensuring the policy begins environment interaction with positive baseline competence.
3. **Path-Dependent Risk Decoupling:** The control barrier function acts as an external safety filter independent of policy parameters. By establishing a forward-invariant safe set $B(V_t) \ge 0$, the portfolio guarantees an analytical drawdown ceiling $\delta_{\max}$, allowing aggressive return extraction during favorable trends without risking portfolio destruction during regime collapses.

## Signal

The decision and execution signal pipeline operates as follows:

### 1. State Formulation ($s_t \in \mathbb{R}^{10n+1}$)
For a universe of $n$ assets at trading day $t$:
- Available cash balance: $b_t \in \mathbb{R}_+$ (1 scalar).
- Current share holdings vector: $h_t = [h_{t,1}, \dots, h_{t,n}]^\top \in \mathbb{Z}^n$.
- Asset closing price vector: $p_t = [p_{t,1}, \dots, p_{t,n}]^\top \in \mathbb{R}_+^n$.
- Technical indicators: 8 technical indicators computed for each asset $i \in \{1, \dots, n\}$ ($8n$ features).
- Total state dimension: $\dim(s_t) = 10n + 1$. For $n = 30$ assets, $\dim(s_t) = 301$.

### 2. Action Space ($a_t \in \mathcal{A}$)
The raw action proposed by the policy $\pi_\theta(a_t|s_t)$ is an $n$-dimensional discrete vector:
$$a_t = [a_{t,1}, \dots, a_{t,n}]^\top, \quad a_{t,i} \in \{-m, \dots, 0, \dots, m\}$$
where $m$ is the maximum number of shares allowed to be traded per asset in a single period. The action cardinality is $(2m+1)^n$. Positive entries denote purchases, negative entries denote sales, and zero denotes holding.

### 3. Transition Dynamics & Market Reward
Following action execution, state variables update:
- Holdings update:
  $$h_{t+1} = h_t + a_t$$
- Cash balance update (accounting for transaction fee rate $c = 0.001$):
  $$b_{t+1} = b_t - p_t^\top a_t - c \sum_{i=1}^n p_{t,i} |a_{t,i}|$$
- Marked-to-market portfolio value:
  $$V_t = b_t + p_t^\top h_t$$
- True environment percentage return reward:
  $$r_t = \frac{V_{t+1} - V_t}{V_t} = \frac{b_{t+1} + p_{t+1}^\top h_{t+1} - (b_t + p_t^\top h_t)}{b_t + p_t^\top h_t}$$

### 4. Multi-Expert Demonstrations and Sliced Wasserstein Barycenter
A collection of $K = 5$ heterogeneous expert trading policies $\{\pi_k\}_{k=1}^K$ is evaluated on validation data:
1. **Time-Series Momentum (TSMOM):** $s_{i,t} = \mathrm{sign}(r_{i,t-L:t-1})$ based on 12-month lookback returns (Moskowitz et al., 2012).
2. **Cross-Sectional Momentum (CSMOM):** $s_{i,t} = \mathrm{rank}(r_{i,t-L:t-1})$, buying top-decile and shorting bottom-decile relative performers (Jegadeesh & Titman, 2002).
3. **Moving Average Crossover:** $s_t = +1$ if $\mathrm{MA}_f(t) > \mathrm{MA}_s(t)$, $-1$ otherwise, filtering noise with dual fast/slow trend filters (Brock et al., 1992).
4. **Bollinger Bands:** Mean-reversion trigger when price breaches $\mu_t \pm k \sigma_t$ envelopes (Kirkpatrick & Dahlquist, 2010).
5. **DRL Agent:** Autonomous PPO agent trained on historical data.

Each expert induces an empirical state-action distribution $\mu_k$ over trajectories $\mathcal{D}_k = \{(s_\tau^{(k)}, a_\tau^{(k)})\}_{\tau=1}^{N_k}$. Experts are assigned non-negative weights proportional to their positive Sharpe ratios:
$$\alpha_k = \frac{\tilde{S}_k}{\sum_{j=1}^K \tilde{S}_j}, \quad \tilde{S}_k = \max\left(\mathrm{Sharpe}(\pi_k), 0\right)$$
The consensus distribution $\mu_{\mathrm{bar}}$ minimizes the performance-weighted 2-Wasserstein distance:
$$\mu_{\mathrm{bar}} = \arg\min_\mu \sum_{k=1}^K \alpha_k W_2^2(\mu, \mu_k)$$
To render high-dimensional computation tractable, a sliced Wasserstein approximation is employed:
- Sample random 1D unit projection vectors $v \in \mathbb{R}^{d_s+d_a}$, $\|v\|_2 = 1$.
- For each projection, compute the barycenter quantile function from sorted projected expert samples $\hat{z}_k^{(v)}$:
  $$\hat{z}_{\mathrm{bar}}^{(v)}(q) = \sum_{k=1}^K \alpha_k \hat{z}_k^{(v)}(q)$$
- Aggregate across multiple projection slices and back-project to recover pseudo-expert demonstration dataset $\mathcal{D}_{\mathrm{bar}}$.
- **Feasibility Projection:** Because back-projection from 1D slices lacks a unique inverse mapping, reconstructed actions are checked against current portfolio cash $b_t$ and holdings $h_t$; violating actions are clipped to the nearest feasible boundary before entering $\mathcal{D}_{\mathrm{bar}}$.

### 5. Adversarial Imitation Learning via GAIL
- Discriminator $D_\phi: \mathcal{S} \times \mathcal{A} \to (0, 1)$ parameterizes the probability that a state-action pair originates from the pseudo-expert dataset $\mathcal{D}_{\mathrm{bar}}$ rather than policy trajectory $\mathcal{D}_\pi$:
  $$\max_\phi \mathbb{E}_{(s,a) \sim \mathcal{D}_{\mathrm{bar}}} [\log D_\phi(s, a)] + \mathbb{E}_{(s,a) \sim \mathcal{D}_\pi} [\log(1 - D_\phi(s, a))]$$
- The surrogate imitation reward signal provided to the policy is:
  $$r_I(s_t, a_t) = -\log\left(1 - D_\phi(s_t, a_t)\right)$$
- The policy $\pi_\theta$ maximizes discounted surrogate rewards using PPO with clipped objective:
  $$L^{\mathrm{PPO}}(\theta) = \hat{\mathbb{E}}_t \left[ \min\left(r_t(\theta) \hat{A}_t, \mathrm{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t\right) \right]$$
  where $r_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{\mathrm{old}}}(a_t|s_t)}$.

### 6. Risk-Constrained Action Selection via Control Barrier Functions (CBFs)
- Let $V_t^{\max} = \max_{\tau \le t} V_\tau$ be the running peak portfolio value.
- Portfolio drawdown is $D_t = \frac{V_t^{\max} - V_t}{V_t^{\max}}$.
- The barrier function enforcing maximum allowable drawdown $\delta_{\max} \in (0, 1)$ is:
  $$B(V_t) = \delta_{\max} - D_t = \delta_{\max} - \frac{V_t^{\max} - V_t}{V_t^{\max}}$$
  The system is safe when $B(V_t) \ge 0$.
- To evaluate safety at step $t+1$, expected asset returns are bounded conservatively over a rolling window (20 days):
  $$\hat{R}_{t+1} = \mu_t - \kappa \sigma_t$$
  where $\mu_t, \sigma_t \in \mathbb{R}^n$ are rolling mean and standard deviation of daily asset returns, and $\kappa = 1$ is the risk sensitivity coefficient.
- The conservative predicted portfolio value under candidate action $a_t$ is:
  $$\hat{V}_{t+1} = \hat{b}_{t+1} + \left(p_t \odot (\mathbf{1} + \hat{R}_{t+1})\right)^\top (h_t + a_t)$$
  where $\hat{b}_{t+1} = b_t - p_t^\top a_t - c \sum_{i=1}^n p_{t,i} |a_{t,i}|$.
- The discrete-time forward invariance CBF condition is:
  $$B(\hat{V}_{t+1}) - B(V_t) + \alpha_{\textbf{CBF}} B(V_t) \ge 0$$
  where $\alpha_{\textbf{CBF}} = 0.1$ governs the restoration decay rate toward the safe set.
- **Execution Repair (Quadratic Program):** If the candidate policy action $a_t$ violates the condition, it is projected onto the safe boundary:
  $$a_t^{\mathrm{safe}} = \arg\min_{a \in \mathcal{A}} \|a - a_t\|_2^2 \quad \text{s.t.} \quad B(\hat{V}_{t+1}) - B(V_t) + \alpha_{\textbf{CBF}} B(V_t) \ge 0$$
- **Training Soft Regularization:** A soft barrier penalty proportional to $\max(0, -[B(\hat{V}_{t+1}) - B(V_t) + \alpha_{\textbf{CBF}} B(V_t)])$ with coefficient $\lambda_{\mathrm{CBF}} \in [0.01, 0.1]$ is added to the PPO loss function to discourage repeated violations during training.

### 7. Two-Stage Training Protocol
- **Stage 1 (Imitation Pretraining):** Policy $\pi_\theta$ is trained for 100 epochs on 2010–2020 data using the GAIL surrogate reward $r_I(s,a)$. All actions are filtered through the CBF.
- **Stage 2 (Environment Fine-Tuning):** Policy weights are initialized from Stage 1 and fine-tuned on 2021–2023 data using the true market reward $r_t$ (net percentage return). The CBF remains active throughout.
- **Deployment (Testing):** Evaluated strictly out-of-sample on unseen data from 2024-01-01 to 2025-09-30 with frozen weights and active CBF projection.

## Required data

- **Universe & Instruments:**
  - 4 major global equity indices, each represented by a fixed basket of 30 liquid constituent equities ($n = 30$):
    1. United States: Dow Jones Industrial Average (DJI) — 30 constituent stocks.
    2. United Kingdom: FTSE 100 — 30 largest constituent stocks by market capitalization.
    3. India: BSE Sensex — 30 constituent stocks.
    4. Taiwan: TAIEX / TWII — 30 largest constituent stocks by market capitalization.
- **Venue & Data Vendor:** Yahoo Finance API (`https://finance.yahoo.com/`), covering historical daily data from January 1, 2010 to September 30, 2025.
- **Market Type:** Cash equity spot.
- **Timeframe:** Daily bars ($1\text{D}$).
- **Data Fields Required:**
  - Daily closing prices $p_t \in \mathbb{R}_+^n$.
  - Daily returns $R_t = (p_t - p_{t-1}) \oslash p_{t-1}$.
  - Eight technical indicators per asset.
  - Cash balance $b_t$ and holdings $h_t$.
- **Temporal Partitions:**
  - GAIL pretraining: 2010-01-01 to 2020-12-31 (11 years).
  - PPO fine-tuning: 2021-01-01 to 2023-12-31 (3 years).
  - Out-of-sample evaluation: 2024-01-01 to 2025-09-30 (21 months).
- **Hyperparameter Specifications (Bayesian Optimization via Hyperopt):**
  - PPO Policy/Value Networks: Hidden dimension $\in [2, 512]$, layers $\in [1, 8]$, activations $\in \{\text{ReLU}, \text{Tanh}, \text{Sigmoid}\}$, learning rate $\in [10^{-8}, 10^{-1}]$, dropout $\in [0, 0.5]$, discount factor $\gamma \in [0.9, 0.99]$, PPO epochs $\in [5, 50]$, value loss coefficient $\in [0.01, 0.5]$, entropy coefficient $\in [0.01, 0.1]$.
  - GAIL Discriminator: Hidden dimension $\in [2, 512]$, layers $\in [1, 8]$, activations $\in \{\text{ReLU}, \text{Tanh}, \text{Sigmoid}\}$, dropout $\in [0, 0.5]$.
  - Control Barrier Function (CBF): Rolling volatility window $= 20$ trading days, $\kappa = 1.0$, $\alpha_{\textbf{CBF}} = 0.1$, CBF penalty coefficient $\in [0.01, 0.1]$.

## Execution assumptions

- **Decision & Execution Cadence:** Daily rebalance at market close. Decisions are formed using closing prices and technical indicators at day $t$; trades execute at close $t$.
- **Initial Portfolio Value:** $1,000,000$ units of local index currency.
- **Transaction Costs:** Proportional transaction fee of $0.10\%$ ($10\text{ bps}$) deducted from cash on both buy and sell volumes ($c = 0.001$).
- **Action Limits:** Discrete share trading per period capped at $|a_{t,i}| \le m$.
- **Shorting & Leverage:** Long/short holdings permitted in the discrete action formulation; no explicit margin borrowing rate or collateral liquidation engine modeled beyond the discrete cash accounting equation.
- **Execution Omissions:** No bid-ask spread crossing, order book queue latency, market impact function, or intraday price slippage are modeled in the daily simulator.

## Evidence

### Source-reported

All quantitative performance figures below trace directly to Arishi Orra, Himanshu Choudhary, and Manoj Thakur (*arXiv:2608.15770v1*, Tables 1, 2, 3, 4, 5, 6, and Figures 1–4). Evaluations cover the out-of-sample period (January 1, 2024 to September 30, 2025, 21 months). For all learning-based models, results represent the mean and standard deviation across five independent random seeds (Table 3):

#### 1. Cross-Market Out-of-Sample Benchmark Performance (Tables 1 & 3)

| Index / Market | Model Class | Strategy / Baseline | Cumulative Return (%) | Annualized Return (%) | Sharpe Ratio | Max Drawdown (%) | Win Ratio (%) |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **DJI (US)** | Benchmark | Market Index | 22.81% | 12.58% | 0.883 | 16.37% | 54.13% |
| | Benchmark | Buy-and-Hold | 30.56% | 16.52% | 1.117 | 15.92% | 55.15% |
| | Classical | Mean-Variance (MVO) | 19.65% | 10.90% | 0.976 | 10.66% | 53.44% |
| | Baseline | Random Trading | $18.68 \pm 5.42\%$ | $10.38 \pm 3.15\%$ | $0.71 \pm 0.18$ | $17.14 \pm 3.85\%$ | $47.91 \pm 2.45\%$ |
| | Rule Expert | CSMOM | 24.24% | 13.33% | 0.661 | 29.98% | 53.21% |
| | Rule Expert | TSMOM | 25.32% | 13.90% | 0.914 | 13.50% | 49.31% |
| | Rule Expert | Bollinger Bands | 25.63% | 14.06% | 0.814 | 15.99% | 54.36% |
| | Rule Expert | MA Crossover | 31.93% | 17.32% | 1.062 | 18.44% | 47.94% |
| | Standard DRL | A2C | $37.19 \pm 3.41\%$ | $20.00 \pm 1.84\%$ | $1.07 \pm 0.12$ | $23.63 \pm 2.15\%$ | $55.05 \pm 1.34\%$ |
| | Standard DRL | DDPG | $38.27 \pm 4.12\%$ | $20.55 \pm 2.21\%$ | $1.17 \pm 0.14$ | $19.72 \pm 2.84\%$ | $54.19 \pm 1.65\%$ |
| | Standard DRL | PPO | $35.59 \pm 2.87\%$ | $17.67 \pm 1.52\%$ | $1.16 \pm 0.10$ | $16.21 \pm 1.64\%$ | $55.73 \pm 1.15\%$ |
| | Advanced DRL| VS-DRL (Zhang 2019) | $36.96 \pm 3.85\%$ | $19.89 \pm 1.95\%$ | $1.19 \pm 0.13$ | $19.35 \pm 2.45\%$ | $57.14 \pm 1.45\%$ |
| | Advanced DRL| SRRS (Rodinos 2023) | $12.28 \pm 2.15\%$ | $6.91 \pm 1.12\%$ | $0.46 \pm 0.16$ | $21.52 \pm 3.12\%$ | $50.01 \pm 1.85\%$ |
| | Advanced DRL| RSHF (Orra 2025) | $35.71 \pm 2.94\%$ | $19.25 \pm 1.65\%$ | $1.29 \pm 0.11$ | $15.70 \pm 1.85\%$ | $54.59 \pm 1.25\%$ |
| | Advanced DRL| Adaptive (Yang 2020) | $24.02 \pm 2.65\%$ | $13.22 \pm 1.43\%$ | $0.95 \pm 0.14$ | $16.40 \pm 2.05\%$ | $55.28 \pm 1.55\%$ |
| | Advanced DRL| DREB (Orra 2024) | $42.52 \pm 3.10\%$ | $22.63 \pm 1.75\%$ | $1.41 \pm 0.09$ | $17.97 \pm 1.75\%$ | $57.34 \pm 1.15\%$ |
| | **Ours** | **BRaG** | **$53.98 \pm 1.95\%$** | **$28.26 \pm 1.05\%$** | **$1.47 \pm 0.06$** | **$17.96 \pm 1.25\%$** | **$58.05 \pm 0.85\%$** |
| **FTSE 100 (UK)** | Benchmark | Market Index | 20.44% | 11.86% | 1.018 | 13.43% | 55.33% |
| | Benchmark | Buy-and-Hold | 8.60% | 4.82% | 0.426 | 17.29% | 51.03% |
| | Advanced DRL| DREB | $43.90 \pm 3.25\%$ | $23.10 \pm 1.85\%$ | $1.38 \pm 0.10$ | $12.41 \pm 1.55\%$ | $53.74 \pm 1.25\%$ |
| | Standard DRL | PPO | $32.29 \pm 3.14\%$ | $17.30 \pm 1.75\%$ | $1.11 \pm 0.11$ | $13.46 \pm 1.65\%$ | $54.22 \pm 1.35\%$ |
| | **Ours** | **BRaG** | **$64.24 \pm 2.41\%$** | **$32.70 \pm 1.25\%$** | **$1.63 \pm 0.07$** | **$11.36 \pm 1.15\%$** | **$57.51 \pm 0.95\%$** |
| **Sensex (India)**| Benchmark | Market Index | 11.78% | 6.70% | 0.549 | 14.96% | 51.35% |
| | Benchmark | Buy-and-Hold | 16.14% | 9.09% | 0.698 | 15.91% | 53.24% |
| | Advanced DRL| RSHF | $23.23 \pm 2.75\%$ | $12.92 \pm 1.55\%$ | $0.85 \pm 0.12$ | $16.24 \pm 1.95\%$ | $53.47 \pm 1.45\%$ |
| | Advanced DRL| DREB | $18.67 \pm 2.15\%$ | $10.48 \pm 1.35\%$ | $0.66 \pm 0.11$ | $17.41 \pm 1.85\%$ | $51.39 \pm 1.35\%$ |
| | Standard DRL | PPO | $21.39 \pm 2.75\%$ | $11.94 \pm 1.55\%$ | $0.78 \pm 0.12$ | $15.35 \pm 1.95\%$ | $51.62 \pm 1.45\%$ |
| | **Ours** | **BRaG** | **$34.07 \pm 1.85\%$** | **$18.61 \pm 1.05\%$** | **$1.04 \pm 0.08$** | **$15.19 \pm 1.35\%$** | **$55.07 \pm 0.95\%$** |
| **TWII (Taiwan)**| Benchmark | Market Index | 43.28% | 23.95% | 1.041 | 28.69% | 55.06% |
| | Benchmark | Buy-and-Hold | 51.43% | 28.12% | 1.053 | 33.76% | 53.68% |
| | Standard DRL | DDPG | $95.38 \pm 6.15\%$ | $49.48 \pm 3.45\%$ | $1.61 \pm 0.08$ | $26.45 \pm 4.15\%$ | $56.53 \pm 2.15\%$ |
| | Advanced DRL| DREB | $76.95 \pm 4.35\%$ | $40.61 \pm 2.45\%$ | $1.50 \pm 0.11$ | $21.79 \pm 2.85\%$ | $54.87 \pm 1.55\%$ |
| | Standard DRL | PPO | $66.45 \pm 4.12\%$ | $35.57 \pm 2.25\%$ | $1.44 \pm 0.12$ | $26.49 \pm 2.95\%$ | $55.11 \pm 1.65\%$ |
| | **Ours** | **BRaG** | **$106.84 \pm 3.55\%$** | **$54.34 \pm 1.95\%$** | **$1.73 \pm 0.16$** | **$28.36 \pm 2.15\%$** | **$60.82 \pm 1.15\%$** |

- **Multi-Market Dominance:** BRaG ranked #1 in cumulative return, annualized return, and Sharpe ratio across all four international equity markets. Relative cumulative return improvements over the strongest competing baseline were:
  - DJI: $+26.9\%$ relative over DREB (53.98% vs 42.52%).
  - FTSE 100: $+46.3\%$ relative over DREB (64.24% vs 43.90%).
  - Sensex: $+46.7\%$ relative over RSHF (34.07% vs 23.23%).
  - TWII: $+12.0\%$ relative over DDPG (106.84% vs 95.38%).
- **Variance Reduction Across Seeds:** Across 5 random initializations, BRaG displayed the lowest standard deviation in cumulative returns ($\pm 1.95\%$ on DJI vs $\pm 4.12\%$ for DDPG and $\pm 3.10\%$ for DREB).

#### 2. Expert Weighting Ablation (Table 4, DJI)
Evaluating the Sharpe-based weighting scheme versus equal weighting across the 5 experts:
- **Sharpe-based weighting:** Cumulative Return $53.977\%$, Sharpe Ratio $1.472$, Max Drawdown $17.958\%$.
- **Equal weighting:** Cumulative Return $48.502\%$, Sharpe Ratio $1.281$, Max Drawdown $20.133\%$.
Equal weighting causes a $5.48$ percentage point drop in return, a $0.191$ drop in Sharpe, and a $2.18$ percentage point increase in maximum drawdown.

#### 3. Component-Wise Framework Ablation (Table 5, DJI)
Isolating the contribution of each architectural module:
- **Full BRaG:** Cumulative Return **$53.977\%$**, Sharpe Ratio **$1.472$**, Max Drawdown **$17.958\%$**.
- **Without GAIL Pretraining (PPO + CBF from scratch):** Cumulative Return collapses to $33.501\%$ (a $20.48$ percentage point drop) and Sharpe ratio drops to $1.245$. Max drawdown is $15.796\%$.
- **Without PPO Fine-Tuning (GAIL imitation only + CBF):** Cumulative Return drops to $42.378\%$ and Sharpe ratio drops to $1.335$. Max drawdown is $16.953\%$.
- **Without Control Barrier Function (GAIL + PPO unconstrained):** Cumulative Return is $52.951\%$, Sharpe ratio drops to $1.258$, and Max Drawdown explodes to **$25.874\%$** (an $7.92$ percentage point deterioration).

#### 4. Expert Aggregation Comparison (Table 6, DJI)
Testing alternative methods of utilizing multi-expert demonstrations:
- **Best Single Expert (TSMOM):** Cumulative Return $27.235\%$, Sharpe Ratio $1.205$, Max Drawdown $14.982\%$.
- **Uniform Expert Sampling (Naive Pooling):** Cumulative Return $46.445\%$, Sharpe Ratio $1.285$, Max Drawdown $20.181\%$.
- **Sharpe-Weighted Sampling (No Barycenter):** Cumulative Return $50.213\%$, Sharpe Ratio $1.388$, Max Drawdown $18.875\%$.
- **Full BRaG (Sliced Wasserstein Barycenter):** Cumulative Return **$53.977\%$**, Sharpe Ratio **$1.472$**, Max Drawdown **$17.958\%$**.

### Independently reproduced

Not independently reproduced. Research capture only.

### Negative evidence

- **CBF Does Not Improve Raw Profitability:** As demonstrated in Table 5, removing the Control Barrier Function yields a comparable cumulative return ($52.951\%$ vs $53.977\%$). The CBF function is strictly a downside risk damper (preventing MDD from rising to $25.874\%$) rather than an alpha generator. In trending bull markets, CBF constraints clip profitable leverage and momentum exposure.
- **Underspecified Technical Indicator States:** While Section 3 specifies that the state space includes "eight most commonly used technical indicators corresponding to each stock", the text does not enumerate the exact names, formulas, or lookback windows for these eight indicators. An external researcher must impute standard FinRL indicator defaults (e.g. MACD, RSI, CCI, ADX).
- **Reliance on Closed-Universe Yahoo Finance Equity Closes:** The empirical results are established exclusively on liquid, large-cap index constituents (DJI, FTSE 100, Sensex, TWII). In less liquid or fragmented markets, execution at the exact daily close with zero market impact is unrealistic.
- **Computational Cost of Sliced Wasserstein Projections & GAIL:** Training requires multi-stage optimization (computing sliced Wasserstein projections across thousands of state-action pairs, training a GAN discriminator, and performing dual PPO stages), rendering real-time retraining or high-frequency adaptation computationally prohibitive.

## Falsification plan

1. **Transaction Cost & Slippage Break-Even Stress Test:** Re-evaluate BRaG across all four index datasets under escalating proportional fee schedules ($c \in \{0.001, 0.002, 0.003, 0.005\}$) and simulated next-bar execution with 5 bps adverse slippage. **Failure threshold:** Net annualized return falling below the Buy-and-Hold benchmark or Sharpe ratio falling below $0.50$ at $c = 0.002$ (20 bps).
2. **Adversarial Expert Contamination Test:** Replace two of the five expert policies with inverted or random trading agents (negative Sharpe) without filtering them out of the barycenter calculation. **Failure threshold:** If the policy trained on contaminated barycenter trajectories achieves identical or higher Sharpe ratio than the true Sharpe-weighted barycenter, the hypothesis that Wasserstein geometric consensus captures meaningful expert alpha is falsified as spurious policy regularization.
3. **Out-of-Sample Market Crash Verification (2025 Q4–2026 Q3):** Evaluate frozen BRaG weights on market data post-September 2025 across an acute drawdown episode ($>20\%$ market index drop). **Failure threshold:** Realized portfolio drawdown exceeding $\delta_{\max} \times 1.25$ (a $25\%$ overshoot of the pre-declared barrier limit) demonstrates failure of the discrete-time CBF forward invariance assumption.
4. **Permuted Technical Feature Placebo Test:** Randomly shuffle the 8 technical indicator time series across assets while keeping price and cash series intact. **Failure threshold:** If the resulting policy matches $>85\%$ of the return and Sharpe of the base model, the claim that the agent learns predictive multi-factor trading behavior rather than simple price trend tracking is falsified.

## Crypto portability

**Adapted / Unproven (Ported Hypothesis)**

The primary publication evaluates BRaG exclusively on cash equities (US, UK, Indian, and Taiwanese stock indices). Applying this framework to cryptocurrency markets represents a ported research hypothesis subject to substantial structural differences:
- **Absence of Discrete Daily Sessions:** Equities feature clear daily closes (e.g. 16:00 EST) and overnight halts, providing clean synchronization boundaries for the 20-day rolling CBF covariance window ($\mu_t, \sigma_t$). Crypto operates 24/7/365; daily rebalancing at 00:00 UTC exposes the portfolio to substantial intraday volatility and weekend liquidity thins where CBF projections may become stale.
- **Perpetual Funding Rate Dynamics:** Crypto long/short exposure in derivatives markets is subject to 8-hour funding rate payments. In prolonged bull runs or basis dislocations, funding costs can exceed 20–50% annualized, creating a severe cash drag that is completely omitted from the equity cash transition equation.
- **Extreme Volatility & Tail Jumps:** The CBF safety projection relies on a Gaussian-like lower bound $\hat{R}_{t+1} = \mu_t - \kappa \sigma_t$. In crypto markets characterized by heavy-tailed jump diffusions, liquidation cascades, and flash crashes, price drops often exceed $5\sigma$, causing instantaneous discrete-time violations of the barrier condition before the quadratic program can execute an action repair.
- **Exchange Fragmentation & Taker Fees:** Equity trades assume a uniform 10 bps fee. In crypto, taker fees across tier-0 accounts often range from 4–7 bps plus significant bid-ask spread crossing and depth impact during volatile market liquidations.

## Limitations

- **Not Independently Reproduced:** All performance claims originate from arXiv:2608.15770v1 and have not been replicated on independent infrastructure or within NautilusTrader.
- **Underspecified Feature Representation:** The exact definitions and parameters of the 8 technical indicators composing the state space are not enumerated in the primary text.
- **Simplified Execution Mechanics:** Trades execute instantaneously at closing prices without modeling market impact, partial fills, limit order queue delays, or borrow fees for short positions.
- **Static Universe Assumption:** A fixed universe of 30 stocks per index is utilized throughout the 15-year sample, introducing survivorship bias for constituents selected based on modern market capitalization.

## Implementation status

`not-implemented`. Research capture only. Neither the sliced Wasserstein barycenter engine, the GAIL pretraining loop, nor the control barrier function quadratic projection has been integrated into PyBroker, NautilusTrader, paper trading, or live execution engines.

## Adoption boundary

`research-only`. `adoption: not-approved`. `approval_scope: research-only`. Inclusion in this repository serves strictly as normalized research material and does not constitute authorization for live trading, capital allocation, or strategy deployment.

## Related Wiki records

- `[[questrader-self-supervised-auxiliary-task-discovery-rl-trading-2026-09-02]]`: Auxiliary self-supervised task discovery for stabilizing reinforcement learning representations in stock trading (Orra et al., 2026).
- `[[fineft-risk-aware-ensemble-rl-vae-routing-crypto-futures-2026-09-03]]`: Ensemble reinforcement learning with VAE regime routing for cryptocurrency futures.
- `[[crypto-drl-execution-overlay-multi-pair-trading-2026-09-01]]`: Deep reinforcement learning execution overlays for multi-asset crypto trading.
- `[[sinkhorn-robust-rl-high-frequency-market-making-2026-09-02]]`: Distributionally robust reinforcement learning using optimal transport and Sinkhorn divergences for market making.
- `[[dynamic-portfolio-optimization-cvar-stochastic-control-hjb-2026-09-02]]`: Continuous-time portfolio optimization under CVaR terminal constraints.

## Sources

- Arishi Orra, Himanshu Choudhary, and Manoj Thakur, "Learning Stock Trading Policies via Barycenter-Based Adversarial Inverse Reinforcement Learning," *arXiv preprint* `arXiv:2608.15770v1 [q-fin.TR, cs.LG]`, submitted August 16, 2026. Canonical abstract URL: https://arxiv.org/abs/2608.15770. Canonical full text HTML: https://arxiv.org/html/2608.15770v1. Full text PDF: https://arxiv.org/pdf/2608.15770v1. DOI: https://doi.org/10.48550/arXiv.2608.15770.
- J. Ho and S. Ermon, "Generative adversarial imitation learning," in *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 29, 2016, pp. 4565–4573.
- J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, "Proximal policy optimization algorithms," arXiv:1707.06347, 2017.
- A. Y. Ng and S. Russell, "Algorithms for inverse reinforcement learning," in *Proc. 17th International Conf. on Machine Learning (ICML)*, 2000, pp. 663–670.
- J. Fu, K. Luo, and S. Levine, "Learning robust rewards with adversarial inverse reinforcement learning," arXiv:1710.11248, 2017.
- N. Jegadeesh and S. Titman, "Cross-sectional and time-series determinants of momentum returns," *The Review of Financial Studies*, vol. 15, no. 1, pp. 143–157, 2002.
- T. J. Moskowitz, Y. H. Ooi, and L. H. Pedersen, "Time series momentum," *Journal of Financial Economics*, vol. 104, no. 2, pp. 228–250, 2012.
- W. Brock, J. Lakonishok, and B. LeBaron, "Simple technical trading rules and the stochastic properties of stock returns," *The Journal of Finance*, vol. 47, no. 5, pp. 1731–1764, 1992.
- C. D. Kirkpatrick II and J. R. Dahlquist, *Technical Analysis: The Complete Resource for Financial Market Technicians*, FT Press, 2010.
- H. M. Markowitz, "Foundations of portfolio theory," *The Journal of Finance*, vol. 46, no. 2, pp. 469–477, 1991.
- V. Mnih et al., "Asynchronous methods for deep reinforcement learning," in *Proc. 33rd International Conf. on Machine Learning (ICML)*, 2016, pp. 1928–1937.
- T. P. Lillicrap et al., "Continuous control with deep reinforcement learning," arXiv:1509.02971, 2015.
- J. Moody, L. Wu, Y. Liao, and M. Saffell, "Performance functions and reinforcement learning for trading systems and portfolios," *Journal of Forecasting*, vol. 17, no. 5-6, pp. 441–470, 1998.
- Y. Liu, Q. Liu, H. Zhao, Z. Pan, and C. Liu, "Adaptive quantitative trading: an imitative deep reinforcement learning approach," in *Proc. AAAI Conf. on Artificial Intelligence*, vol. 34, no. 02, 2020, pp. 2128–2135.
- H. Yang, X. Liu, S. Zhong, and A. Walid, "Deep reinforcement learning for automated stock trading: an ensemble strategy," in *Proc. 1st ACM International Conf. on AI in Finance (ICAIF)*, 2020, pp. 1–8.
- Z. Zhang, S. Zohren, and S. Roberts, "Deep reinforcement learning for trading," arXiv:1911.10107, 2019.
- G. Rodinos, P. Nousi, N. Passalis, and A. Tefas, "A Sharpe ratio based reward scheme in deep reinforcement learning for financial trading," in *IFIP International Conf. on Artificial Intelligence Applications and Innovations*, 2023, pp. 15–23.
- A. Orra, A. Bhambu, H. Choudhary, and M. Thakur, "Dynamic reinforced ensemble using Bayesian optimization for stock trading," in *Proc. 5th ACM International Conf. on AI in Finance (ICAIF)*, 2024, pp. 361–369.
- A. Orra, H. Choudhary, A. Sharma, and M. Thakur, "Enhancing deep reinforcement learning for stock trading: a reward shaping approach via expert feedback," *Knowledge and Information Systems*, pp. 1–20, 2025.
- H. Choudhary, A. Orra, M. Thakur, X. Gao, and P. K. Sahu, "A CVaR-constrained safe reinforcement learning framework with action repair for practical portfolio optimization," *IEEE Transactions on Artificial Intelligence*, 2026.
- J. Snoek, H. Larochelle, and R. P. Adams, "Practical Bayesian optimization of machine learning algorithms," in *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 25, 2012, pp. 2951–2959.
