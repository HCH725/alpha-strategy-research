---
schema: strategy-research-record-v1
title: "Decision-Focused Sparse Tangent Portfolio Optimization with DPP-Compliant QCQP and Differentiable Top-k Operator"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - decision-focused-learning
  - sparse-portfolio
  - tangent-portfolio
  - sharpe-ratio-maximization
  - cvxpy-layers
  - differentiable-top-k
  - equity
  - cross-sectional
status: research-only
confidence: medium
source_as_of: 2026-07-01
sources:
  - "https://arxiv.org/abs/2607.00581"
  - "https://doi.org/10.48550/arXiv.2607.00581"
  - "https://arxiv.org/html/2607.00581v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Decision-Focused Sparse Tangent Portfolio Optimization with DPP-Compliant QCQP and Differentiable Top-k Operator

## Provenance

- **Primary Source:** Haeun Jeon, Seunghoon Choi, Hyunglip Bae, Yongjae Lee, and Woo Chang Kim, *"Decision-focused Sparse Tangent Portfolio Optimization"*, arXiv preprint `arXiv:2607.00581v1 [cs.LG, q-fin.CP]`, published 1 July 2026 (accepted to ICML 2026). DOI: `10.48550/arXiv.2607.00581`.
- **Primary Source Text:** Complete author LaTeX source package downloaded and extracted directly from `https://arxiv.org/e-print/2607.00581` (snapshot July 2026), including `oscar_dfl.tex`, `reference_oscar_dfl.bib`, `algorithm.sty`, and figures in `figs/`.
- **Public Access URL:** https://arxiv.org/abs/2607.00581 and HTML full text at https://arxiv.org/html/2607.00581v1.
- **Source/Data As-Of:** 2026-07-01.
- **Source-Identity Deduplication:** Repository-wide audit confirmed zero matching records for `2607.00581`, `Haeun Jeon`, `Woo Chang Kim`, `Yongjae Lee`, `OSCAR`, `cardinality-constrained Sharpe`, or `sparse tangent portfolio`. Existing portfolio optimization records in this repository (e.g., `observable-matrix-dynamics-portfolio-optimization-2026-09-02.md`, `dynamic-portfolio-optimization-cvar-stochastic-control-hjb-2026-09-02.md`, `mingle-exposure-locality-factor-graph-portfolio-diversification-2026-09-02.md`) address fundamentally distinct mechanisms, continuous matrix dynamics, factor graphs, or unconstrained stochastic control. Jeon et al. (2026) uniquely introduces an end-to-end Decision-Focused Learning (DFL) framework that embeds a Disciplined Parametrized Programming (DPP)-compliant QCQP tangency layer coupled with a smooth, differentiable top-$k$ operator that strictly enforces exact portfolio cardinality $k$.

## Economic mechanism

### Source-reported

In modern portfolio theory, Markowitz's mean-variance model and Sharpe ratio maximization construct diversified portfolios balancing expected return against covariance risk. However, holding all $N$ assets in a universe is practically prohibitive due to excessive monitoring overhead, exchange connectivity, custodial complexity, and transaction costs. Consequently, portfolio managers require sparse portfolios that restrict the number of active holdings via an explicit cardinality constraint $\mathrm{Card}(w) \le k$.

Enforcing strict cardinality turns an otherwise smooth convex optimization problem into an NP-hard combinatorial search over $\binom{N}{k}$ possible asset subsets. Standard machine learning workflows address this through a decoupled "predict-then-optimize" (Prediction-Focused Learning, PFL) paradigm:
1. A machine learning model (e.g., multi-layer perceptron) is trained to minimize statistical loss (such as Mean Squared Error, MSE) on historical return forecasts $\hat{\mu}$.
2. The point predictions $\hat{\mu}$ are fed into an external combinatorial or heuristic optimizer to select $k$ assets and assign weights.

The authors demonstrate that PFL suffers from a structural objective mismatch: statistical loss treats all forecast errors symmetrically across all assets, ignoring the fact that downstream portfolio performance is determined by relative rankings, covariance interactions, and discrete selection truncation. Under tight sparsity constraints, minor forecasting errors in borderline assets cascade through the discrete selection stage, triggering catastrophic selection mistakes and substantial out-of-sample Sharpe ratio degradation.

To eliminate this mismatch, the authors propose an end-to-end Decision-Focused Learning (DFL) architecture:
1. **Differentiable QCQP Homogenization:** By applying classical homogenization ($y = tw$) and Cholesky factorization of the covariance matrix ($\Sigma = L_\Sigma L_\Sigma^\top$), the non-convex fractional Sharpe ratio maximization problem is reformulated into a Disciplined Parametrized Programming (DPP)-compliant convex Quadratically Constrained Quadratic Program (QCQP) where problem parameters enter affinely.
2. **Differentiable Top-$k$ Selection:** Instead of a discontinuous hard top-$k$ mask, asset selection in the Cholesky-transformed space ($x = |L_\Sigma^\top w^{(0)}|$) is executed via a smooth, parameterized sigmoid operator whose scalar shift $t(x)$ is solved via a 1D bisection search. This operator preserves an exact sum-to-$k$ constraint while admitting an analytical, closed-form vector-Jacobian product (VJP) with a diagonal-minus-rank-one Jacobian structure.
3. **End-to-End Gradient Propagation:** Backpropagation flows through the final QCQP re-optimization layer, through the smooth top-$k$ selection layer, and through the initial QCQP tangency layer directly into the neural network weights $\theta$, explicitly training the forecaster to maximize downstream portfolio Sharpe ratio rather than generic statistical fit.

### Research interpretation

This is an end-to-end portfolio construction and structural allocation methodology, not an isolated directional signal.

The falsifiable core hypothesis is: **Training return-forecasting neural networks directly through a differentiable downstream decision layer (composed of a DPP-compliant QCQP tangency solver paired with a smooth top-$k$ Cholesky-space selection operator) minimizes out-of-sample portfolio suboptimality and produces systematically higher realized Sharpe ratios under fixed cardinality constraints than decoupled predict-then-optimize (MSE-trained) baselines, with the performance advantage expanding monotonically as asset universe size $N$ increases.**

Key structural failure modes:
- **Downside Risk & Drawdown Explosion under Short-Selling:** Because the core QCQP formulation allows unconstrained short positions ($w_i < 0$), maximizing the Sharpe ratio without leverage caps or margin constraints can cause aggressive leverage on high-beta or volatile assets, substantially expanding Maximum Drawdown (MDD) during market shocks.
- **Turnover Friction:** Daily unpenalized rebalancing across sparse subsets produces frequent discrete switches in active constituent membership; without an explicit L1 turnover penalty in the objective, execution transaction costs can eliminate empirical Sharpe gains.
- **Covariance Conditioning Breakdown:** The DPP-compliant formulation relies on Cholesky factorization $\Sigma = L_\Sigma L_\Sigma^\top$; if the rolling covariance matrix becomes ill-conditioned or near-singular, diagonal shrinkage ($\lambda = 0.10$) and eigenvalue jitter are strictly necessary to avoid non-convergent or exploding gradient steps during backpropagation.

## Signal

The decision-focused sparse tangent portfolio strategy executes a daily three-stage differentiable forward pipeline during inference and a dual-loss gradient update during training.

### 1. Mathematical Foundations & Structural Properties

- **Scale Invariance (Proposition 3.1):** For any scaling factor $\lambda > 0$, the portfolio Sharpe ratio is scale-invariant with respect to weights:
  $$\mathrm{SR}(\lambda w) = \frac{\mu^\top (\lambda w)}{\sqrt{(\lambda w)^\top \Sigma (\lambda w)}} = \mathrm{SR}(w)$$
  Therefore, the portfolio budget constraint $\mathbf{1}^\top w = 1$ can be omitted during unconstrained tangency optimization without altering the optimal ray direction.

- **Geometric Equivalence via Cholesky Factor (Proposition 3.2):** For any two portfolios $w_1, w_2 \in \mathbb{R}^n$ and the unconstrained tangency portfolio $\hat{w} = \Sigma^{-1}\mu$ (with $\Sigma = L_\Sigma L_\Sigma^\top$):
  $$\mathrm{SR}(w_1) \ge \mathrm{SR}(w_2) \iff \cos \theta(L_\Sigma^\top w_1, L_\Sigma^\top \hat{w}) \ge \cos \theta(L_\Sigma^\top w_2, L_\Sigma^\top \hat{w})$$
  where $\theta(u, v) = \arccos\left(\frac{u^\top v}{\|u\|_2 \|v\|_2}\right)$. Maximizing the Sharpe ratio is geometrically identical to minimizing the angle between the Cholesky-transformed portfolio vector $L_\Sigma^\top w$ and the Cholesky-transformed tangency portfolio $L_\Sigma^\top \hat{w}$.

- **Optimal Sparse Support Selection (Proposition 3.3):** The subset of $k$ assets that minimizes this angle corresponds exactly to the indices of the $k$ largest elements of the element-wise absolute vector $|L_\Sigma^\top \hat{w}|$:
  $$K^* = \arg\max_{K \in \mathcal{K}} \sum_{i \in K} |(L_\Sigma^\top \hat{w})_i|^2$$

### 2. Differentiable DPP-Compliant QCQP Formulation

Standard fractional Sharpe maximization $\max_w \frac{w^\top \mu}{\sqrt{w^\top \Sigma w}}$ is non-convex and non-DPP.
Applying homogenization with scalar $t \ge 0$ and change of variable $y = tw$:
$$\max_{y, t} y^\top \mu \quad \text{s.t.} \quad \mathbf{1}^\top y = t, \; \sqrt{y^\top \Sigma y} \le 1, \; t \ge 0$$
Because $\Sigma$ enters nonlinearly inside $\sqrt{y^\top \Sigma y}$, parameters do not enter affinely. Substituting the Cholesky factor $\Sigma = L_\Sigma L_\Sigma^\top$ yields the DPP-compliant Second-Order Cone / QCQP formulation:
$$\max_{y, t} y^\top \mu \quad \text{s.t.} \quad \mathbf{1}^\top y = t, \; \|L_\Sigma y\|_2 \le 1, \; t \ge 0$$
This problem satisfies Disciplined Parametrized Programming (DPP) rules, allowing exact, implicit-differentiation solution maps via `CVXPYlayers`.
Unnormalized weights are recovered as $w = y / (t + \epsilon_t)$, where $\epsilon_t = 10^{-6}$ is a numerical offset preventing division-by-zero instabilities.

### 3. Differentiable Top-$k$ Operator

Let $x = |L_\Sigma^\top w^{(0)}| \in \mathbb{R}^n$ denote the selection score vector.
The smooth top-$k$ operator maps $x \mapsto p(x) \in (0, 1)^n$ such that:
$$p_i(x) = \sigma\left(\beta (x_i + t(x))\right), \quad i = 1, \dots, n$$
subject to the exact mass constraint:
$$\sum_{i=1}^n p_i(x) = k$$
where $\sigma(z) = \frac{1}{1 + e^{-z}}$ is the logistic sigmoid, and $\beta > 0$ is a sharpness parameter controlling approximation steepness.

- **Forward Pass:** Since $\sigma$ is strictly monotonically increasing, $\sum_{i=1}^n \sigma(\beta(x_i + t))$ is strictly monotonic in $t$. The unique root $t^*(x)$ is determined via a 1D bisection search between saturation bounds $[t_{\min}, t_{\max}]$ executed for exactly 32 iterations.
- **Backward Pass:** Applying the chain rule to the mass constraint:
  $$\frac{\partial p_i(x)}{\partial x_j} = \sigma'(\beta(x_i + t(x))) \left(\delta_{ij} + \frac{\partial t(x)}{\partial x_j}\right)$$
  Differentiating $\sum_{i=1}^n p_i(x) = k$ with respect to $x_j$ gives:
  $$\frac{\partial t(x)}{\partial x_j} = - \frac{v_j(x)}{S(x)}, \quad \text{where } v_i(x) = \sigma'(\beta(x_i + t(x))) \text{ and } S(x) = \sum_{i=1}^n v_i(x)$$
  The Jacobian $J(x)$ possesses an exact diagonal-minus-rank-one structure:
  $$J(x) = \mathrm{diag}(v(x)) - \frac{v(x) v(x)^\top}{S(x)}$$
  For incoming gradient $g \in \mathbb{R}^n$, the Vector-Jacobian Product (VJP) is evaluated in $\mathcal{O}(n)$ time without matrix instantiation:
  $$g^\top J(x) = g \odot v(x) - \frac{\langle g, v(x) \rangle}{S(x)} v(x)$$

### 4. Algorithm Flow & Training Objective (Algorithm 1)

1. **Input Representation:** Historical daily return window $X_t \in \mathbb{R}^{100 \times n}$ over the preceding 100 trading days.
2. **Predictive Network:** Two fully connected layers with 512 and 256 neurons, ReLU activations:
   $$\hat{\mu}_{t+1} = f_\theta(X_t) \in \mathbb{R}^n$$
3. **Exogenous Covariance Regularization:** Rolling sample covariance $\hat{\Sigma}_t$ regularized via Ledoit-Wolf-style diagonal shrinkage:
   $$\Sigma_t = (1 - \lambda)\hat{\Sigma}_t + \lambda \left(\frac{\mathrm{Tr}(\hat{\Sigma}_t)}{n}\right) I_n, \quad \lambda = 0.10$$
   Cholesky decomposition yields $L_{\Sigma_t}$ such that $\Sigma_t = L_{\Sigma_t} L_{\Sigma_t}^\top$.
4. **Initial Continuous Solve:** Solve DPP-QCQP with $(\hat{\mu}_{t+1}, L_{\Sigma_t})$ to obtain preliminary unconstrained weights $w_t^{(0)}$.
5. **Differentiable Top-$k$ Selection:** Compute $s_t = |L_{\Sigma_t}^\top w_t^{(0)}|$ and obtain soft assignment vector:
   $$p_t = \mathrm{SoftTop}\text{-}k(s_t; k, \beta)$$
6. **Re-Optimization Over Selected Support:** Element-wise modulate expected returns:
   $$\mu'_t = \hat{\mu}_{t+1} \odot p_t$$
   Solve the second DPP-QCQP with $(\mu'_t, L_{\Sigma_t})$ to yield final sparse portfolio weights $w_t^* = w^*(\mu'_t; \Sigma_t)$.
7. **Loss Function:**
   $$\mathcal{L}_{\mathrm{Task}} = \alpha \mathcal{L}_{\mathrm{DFL}} + (1 - \alpha)\mathcal{L}_{\mathrm{MSE}}$$
   where:
   - $\mathcal{L}_{\mathrm{DFL}} = - y_{t+1}^\top w_t^*$ (negative realized portfolio return, equivalent to regret minimization omitting constant terms).
   - $\mathcal{L}_{\mathrm{MSE}} = \frac{1}{n} \|\hat{\mu}_{t+1} - y_{t+1}\|_2^2$ (auxiliary supervised MSE on next-day realized return vector $y_{t+1}$).
   - Default mixing parameter: $\alpha = 0.5$.
8. **Inference Execution:** At decision time, final weights $w_t^*$ are allocated at market close and held until the subsequent close ($t+1$).

## Required data

- **Universe:** Four equity index constituent pools with stable membership over the 10-year sample period (January 2016 to December 2025):
  - EuroStoxx50: $N = 47$ constituents.
  - FTSE100: $N = 93$ constituents.
  - KOSPI200: $N = 162$ constituents.
  - Nikkei225: $N = 208$ constituents.
- **Time Horizon & Cadence:** Daily closing prices; daily returns computed as $r_t = (P_t - P_{t-1}) / P_{t-1}$.
- **Lookback Window:** Rolling 100 trading days for both neural network input features $X_t \in \mathbb{R}^{100 \times n}$ and rolling covariance estimation $\hat{\Sigma}_t \in \mathbb{R}^{n \times n}$.
- **Point-in-Time Partitioning:** Chronological 80/20 train/test split. Training period: January 2016 through approximately December 2023; Out-of-sample test period: January 2024 through December 2025.
- **Missing Data Handling:** Constituents entering or exiting the index during 2016–2025 were excluded by design (stable membership requirement).

## Execution assumptions

- **Execution Cadence:** Daily rebalancing at market close ($t$).
- **Fill Timing:** Return realized over $(t, t+1]$ is modeled as $r_{p, t} = (w_t^*)^\top r_{t+1}$.
- **Order Model:** Instantaneous fill at closing price; zero execution latency assumed.
- **Transaction Costs & Slippage:** Omitted in the author's primary reported benchmark experiments (0 bps maker/taker, 0 bps slippage).
- **Short-Selling:** Unconstrained short selling allowed ($w_i \in \mathbb{R}$, no borrow fees, short rebate, or borrow availability limits modeled).
- **Leverage / Margin:** Scale-invariant normalized weights; no explicit gross leverage ceiling $\|w\|_1 \le L_{\max}$ enforced in the core QCQP layer.

## Evidence

### Source-reported

All empirical results are extracted directly from the author's published LaTeX source package (`oscar_dfl.tex`), Table 1, Table 2, Table 3, and Appendix C. All values represent mean $\pm$ standard deviation across 5 independent random seeds.

#### 1. Out-of-Sample Daily Sharpe Ratios Across Markets and Cardinality Levels (Table 1)

Cardinality budget is set as $k = \mathrm{round}(\rho \cdot N)$ for $\rho \in \{10\%, 15\%, 20\%\}$.

| Market | $N$ | $k$ | Historic OSCAR | Historic SD-relax | Historic mSSRM | PFL OSCAR | PFL SD-relax | PFL mSSRM | DFL (Ours) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **EuroStoxx50** | 47 | 5 | $0.156 \pm 0.000$ | $0.077 \pm 0.000$ | $0.148 \pm 0.000$ | $0.809 \pm 0.025$ | **$0.982 \pm 0.087$** | $0.821 \pm 0.074$ | $0.955 \pm 0.014$ |
| | 47 | 7 | $0.198 \pm 0.000$ | $-0.037 \pm 0.000$ | $0.149 \pm 0.000$ | $0.827 \pm 0.023$ | **$1.041 \pm 0.066$** | $0.846 \pm 0.089$ | $0.972 \pm 0.016$ |
| | 47 | 9 | $0.228 \pm 0.000$ | $-0.045 \pm 0.000$ | $0.152 \pm 0.000$ | $0.841 \pm 0.020$ | **$1.116 \pm 0.058$** | $0.889 \pm 0.081$ | $0.983 \pm 0.016$ |
| **FTSE100** | 93 | 9 | $0.269 \pm 0.000$ | $0.198 \pm 0.000$ | $0.167 \pm 0.000$ | $0.776 \pm 0.025$ | $0.931 \pm 0.052$ | $0.782 \pm 0.044$ | **$0.983 \pm 0.016$** |
| | 93 | 14 | $0.322 \pm 0.000$ | $0.245 \pm 0.000$ | $0.234 \pm 0.000$ | $0.853 \pm 0.022$ | **$1.073 \pm 0.061$** | $0.841 \pm 0.049$ | $1.049 \pm 0.034$ |
| | 93 | 19 | $0.396 \pm 0.000$ | $0.254 \pm 0.000$ | $0.237 \pm 0.000$ | $0.888 \pm 0.020$ | **$1.142 \pm 0.057$** | $0.873 \pm 0.047$ | $1.071 \pm 0.021$ |
| **KOSPI200** | 162 | 16 | $0.426 \pm 0.000$ | $0.727 \pm 0.000$ | $0.319 \pm 0.000$ | $0.887 \pm 0.017$ | $1.182 \pm 0.042$ | $1.372 \pm 0.052$ | **$1.958 \pm 0.022$** |
| | 162 | 24 | $0.485 \pm 0.000$ | $0.814 \pm 0.000$ | $0.332 \pm 0.000$ | $0.918 \pm 0.010$ | $1.684 \pm 0.037$ | $1.491 \pm 0.058$ | **$2.030 \pm 0.062$** |
| | 162 | 32 | $0.527 \pm 0.000$ | $0.845 \pm 0.000$ | $0.325 \pm 0.000$ | $0.935 \pm 0.009$ | $1.793 \pm 0.118$ | $1.586 \pm 0.171$ | **$2.098 \pm 0.016$** |
| **Nikkei225** | 208 | 21 | $0.258 \pm 0.000$ | $0.198 \pm 0.000$ | $0.273 \pm 0.000$ | $0.567 \pm 0.014$ | $0.743 \pm 0.103$ | $0.614 \pm 0.092$ | **$0.862 \pm 0.060$** |
| | 208 | 31 | $0.284 \pm 0.000$ | $0.243 \pm 0.000$ | $0.276 \pm 0.000$ | $0.620 \pm 0.012$ | $0.812 \pm 0.111$ | $0.662 \pm 0.094$ | **$0.878 \pm 0.040$** |
| | 208 | 42 | $0.295 \pm 0.000$ | $0.248 \pm 0.000$ | $0.280 \pm 0.000$ | $0.649 \pm 0.011$ | $0.886 \pm 0.126$ | $0.721 \pm 0.107$ | **$0.946 \pm 0.130$** |

*Key Takeaway:* In smaller universes ($N=47, 93$), SD-relaxation PFL occasionally achieves slightly higher raw Sharpe ratios but exhibits substantial standard deviations ($0.052 - 0.087$). In larger universes ($N=162, 208$), DFL decisively outperforms all baselines, achieving Sharpe ratios of **2.098** on KOSPI200 ($k=32$) versus PFL OSCAR 0.935 and PFL SD-relaxation 1.793.

#### 2. Loss Mixing Sensitivity ($\alpha$) on EuroStoxx50 (Table 2)

| $\alpha$ Parameter | $\rho = 10\%$ ($k=5$) | $\rho = 15\%$ ($k=7$) | $\rho = 20\%$ ($k=9$) |
| :--- | :--- | :--- | :--- |
| $\alpha = 0.0$ (Pure MSE) | $0.809 \pm 0.025$ | $0.827 \pm 0.023$ | $0.841 \pm 0.020$ |
| $\alpha = 0.1$ | $0.826 \pm 0.025$ | $0.852 \pm 0.024$ | $0.862 \pm 0.013$ |
| $\alpha = 0.5$ (Default Mixed) | $0.955 \pm 0.014$ | $0.972 \pm 0.016$ | $0.983 \pm 0.016$ |
| $\alpha = 0.9$ | $1.041 \pm 0.081$ | $1.084 \pm 0.083$ | $1.140 \pm 0.154$ |
| $\alpha = 1.0$ (Pure DFL) | $1.165 \pm 0.106$ | $1.056 \pm 0.125$ | $0.940 \pm 0.097$ |

*Observation:* $\alpha = 0.5$ delivers the tightest seed-to-seed stability (lowest standard deviation, $\le 0.016$), whereas higher DFL weights ($\alpha \ge 0.9$) produce higher peak means but 5x-10x wider variance across seeds due to flat/noisy decision landscapes.

#### 3. Maximum Drawdown (MDD) Comparisons (Table 3)

| Market | Method | $\rho = 10\%$ | $\rho = 15\%$ | $\rho = 20\%$ |
| :--- | :--- | :--- | :--- | :--- |
| **EuroStoxx50** | PFL | $0.474 \pm 0.257$ | $0.340 \pm 0.079$ | $0.317 \pm 0.113$ |
| | DFL | $0.310 \pm 0.105$ | $0.403 \pm 0.109$ | $0.390 \pm 0.055$ |
| **FTSE100** | PFL | $0.497 \pm 0.095$ | $0.495 \pm 0.099$ | $0.497 \pm 0.102$ |
| | DFL | $0.710 \pm 0.100$ | $0.605 \pm 0.209$ | $0.607 \pm 0.129$ |
| **KOSPI200** | PFL | $0.775 \pm 0.109$ | $0.790 \pm 0.121$ | $0.796 \pm 0.128$ |
| | DFL | $0.952 \pm 0.021$ | $0.945 \pm 0.033$ | $0.925 \pm 0.055$ |
| **Nikkei225** | PFL | $0.484 \pm 0.192$ | $0.528 \pm 0.199$ | $0.558 \pm 0.202$ |
| | DFL | $0.543 \pm 0.095$ | $0.559 \pm 0.100$ | $0.599 \pm 0.136$ |

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Downside Tail Risk Escalation:** Table 3 documents that DFL portfolios exhibit severe drawdowns, reaching $95.2\%$ on KOSPI200 and $71.0\%$ on FTSE100. Because the unconstrained tangency QCQP permits arbitrary short selling, the network aggressively leverages negative predictions without a downside buffer.
2. **Turnover & Rebalancing Drag:** Rebalancing daily over a discrete support $k$ generates substantial portfolio turnover. Without transaction fees modeled in the paper, live implementation would incur severe friction that could erode the reported Sharpe ratio advantage.
3. **Survivorship Selection Bias:** By restricting the asset universe to constituents that maintained continuous index membership across the entire 10-year period (2016–2025), failed, merged, or delisted firms are excluded, introducing look-ahead survivorship bias into historical covariance structures.
4. **Instability of SDP Baselines:** The SD-relaxation baseline showed extreme volatility swings and seed sensitivity in large markets, necessitating its exclusion from several multi-market time-series evaluations.

## Falsification plan

To falsify or confirm whether the DFL sparse tangent advantage constitutes genuine alpha rather than backtest artifacts, the following sequential tests must be executed:

1. **Frictional Cost Barrier:** Evaluate the strategy under realistic execution costs (5 bps taker fee per trade, 2 bps slippage, and an annualized 200 bps borrow cost for short positions).
   - *Failure rule:* If net Sharpe ratio drops below that of an equal-weighted $1/N$ benchmark or buy-and-hold index ETF, the hypothesis that DFL creates net exploitable alpha is falsified.
2. **Point-in-Time Dynamic Universe Audit:** Re-run the backtest on an uncurated point-in-time constituent dataset (including delisted and insolvent entities at each timestamp $t$).
   - *Failure rule:* If out-of-sample Sharpe degrades by more than 40% compared to the survivorship-filtered baseline, the performance is classified as survivorship-driven.
3. **L1 Turnover Penalty Regularization:** Add an explicit turnover penalty $\tau \|w_t - w_{t-1}\|_1$ to the downstream QCQP formulation.
   - *Failure rule:* If the DFL gradient cannot backpropagate effectively through the penalized layer or if Sharpe ratio converges to that of a static baseline, the differentiability advantage is disproven.
4. **Long-Only Constraint Enforcement:** Restrict portfolio weights to the non-negative simplex ($w \ge 0, \mathbf{1}^\top w = 1$).
   - *Failure rule:* If DFL loses its relative advantage over PFL when short-selling is prohibited, the reported outperformance is attributable solely to unconstrained short leverage rather than superior support selection.
5. **Shuffled-Label / Synthetic Permutation Placebo:** Shuffle the target return labels $y_{t+1}$ randomly across assets while keeping covariance fixed during training.
   - *Failure rule:* If the model produces positive test Sharpe ratios on permuted labels, the architecture is overfitting to static covariance structure rather than learning predictive alpha.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- The primary source tested exclusively traditional equity indices. No cryptocurrency, digital asset, or tokenized derivative was tested in the paper.

### Crypto-Native Portability Risks & Structural Adaptations

1. **Spot vs. Perpetual Dynamics:** In crypto spot markets, short-selling requires margin borrowing against specific collateral pools with variable borrow rates and liquidation thresholds. In contrast, USD-margined perpetual futures (e.g., Binance USDT-margined perps, Bybit, Hyperliquid) provide native short positioning, making perpetual contracts the appropriate target instrument for unconstrained long/short tangency allocations.
2. **Funding Rate Carry Exposure:** Holding net long or net short perpetual positions over multi-day periods accrues funding rate payments every 8 hours (or 1 hour on certain DEXs). A sparse portfolio that concentrates $k$ positions into heavily crowded funding-negative or funding-positive assets will experience substantial carry drag unless funding payments are explicitly modeled in the expected return vector $\hat{\mu}$.
3. **Covariance Matrix Instability:** Crypto asset universes display regime-dependent correlation spikes during market crashes ($\rho \to 1.0$) and high idiosyncratic volatility. Rolling 100-day covariance estimates $\hat{\Sigma}_t$ frequently become ill-conditioned, necessitating higher shrinkage intensity ($\lambda \ge 0.25$) and strict positive-definiteness enforcement before Cholesky factorization.
4. **24/7 Continuous Trading & Candle Boundaries:** Unlike equity markets with standardized 16:00 local closes, crypto markets trade continuously. Rebalancing must be synchronized to a fixed UTC timestamp (e.g., 00:00 UTC) with strict lookback boundaries to prevent forward look-ahead leakage.
5. **Universe Reconstitution:** Rapid listing and delisting of crypto tokens require dynamic liquidity filters (e.g., top-50 perpetual contracts by 30-day average daily volume) rather than static index constituent lists.

## Limitations

1. **Zero Friction Assumption:** Complete omission of trading fees, slippage, and borrow costs in reported experiments.
2. **Extreme Maximum Drawdown:** Realized test drawdowns exceeding 90% in large universes due to unconstrained short-selling.
3. **Survivorship Bias:** Filtered universe of 10-year stable index survivors ignores bankrupt and delisted companies.
4. **Computational Training Overhead:** Differentiating through CVXPYlayers and the 32-step bisection top-$k$ operator increases GPU training wall-clock time by roughly an order of magnitude compared to standard MSE training.
5. **Tailored to Tangency Sharpe Formulation:** The geometric Cholesky equivalence (Propositions 3.2 and 3.3) is specific to the Sharpe ratio; extending this framework to CVaR, Sortino, or drawdown-penalized objectives requires distinct mathematical transformations.

## Implementation status

`not-implemented`

No implementation of this strategy, differentiable decision layer, or neural architecture has been integrated into PyBroker, NautilusTrader, paper-trading, testnet, or live-trading execution engines.

## Adoption boundary

`research-only` / `not-approved`

This document represents a theoretical and empirical research capture for quantitative analysis and hypothesis formulation. It does not constitute authorization for deployment, capital allocation, backtest validation sign-off, or live execution.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/strategy-research-record-spec-v1]]`

## Sources

- **Primary Paper:** Haeun Jeon, Seunghoon Choi, Hyunglip Bae, Yongjae Lee, and Woo Chang Kim, *"Decision-focused Sparse Tangent Portfolio Optimization"*, arXiv preprint `arXiv:2607.00581v1 [cs.LG, q-fin.CP]`, published 1 July 2026, accepted at ICML 2026. DOI: `10.48550/arXiv.2607.00581`. https://arxiv.org/abs/2607.00581 and https://arxiv.org/html/2607.00581v1.
- **Primary LaTeX Source Files:** Author source package from arXiv e-print snapshot `https://arxiv.org/e-print/2607.00581` (July 2026), specifically `oscar_dfl.tex`, `reference_oscar_dfl.bib`, and data tables therein.
- **Author Code Repository Reference:** https://github.com/feuerwerksh/Diffble-card-SR (public URL referenced in paper abstract; snapshot as-of 2026-07-01).
- **Underlying Foundations Cited in Primary Source:**
  - H. Bae, H. Jeon, M. Park, Y. Lee, and W. C. Kim, *"A Cholesky decomposition-based asset selection heuristic for sparse tangent portfolio optimization"*, arXiv:2502.11701, 2025.
  - T. D. Ahle, *"A differentiable Top-k layer for PyTorch"*, https://thomasahle.com/blog/differentiable_topk.html, 2022.
  - A. Agrawal, R. Verschueren, S. Diamond, and S. Boyd, *"Differentiable convex optimization layers"*, NeurIPS, Vol. 32, 2019.
  - G. Iyengar and W. Kang, *"Inverse conic programming with applications"*, Operations Research Letters, 33(3):319–330, 2005.
  - M. J. Kim, J. H. Kim, J. R. Jang, and W. C. Kim, *"Sparse tangent portfolio selection via semi-definite relaxation"*, Operations Research Letters, 44(4):540–543, 2016.
  - Y. Lin, Z.-R. Lai, and C. Li, *"A globally optimal portfolio for m-sparse Sharpe ratio maximization"*, NeurIPS, Vol. 37, 2024.
