---
schema: strategy-research-record-v1
title: "SDOT: Semi-Discrete Optimal Transport Non-Lipschitz Scenario Generation for Market-Neutral Mean-CVaR Optimization on S&P 500 (arXiv 2609.27785v1)"
created: 2026-09-28
updated: 2026-09-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - optimal-transport
  - cvar-optimization
  - market-neutral
  - tail-risk
  - generative-models
  - sp500
  - jump-diffusion
status: research-only
confidence: medium
source_as_of: 2026-08-17
sources:
  - https://arxiv.org/abs/2609.27785
  - https://arxiv.org/html/2609.27785v1
  - https://arxiv.org/pdf/2609.27785v1
  - https://doi.org/10.48550/arXiv.2609.27785
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "CAGR vs Sharpe scaling discrepancy: In Table 5, SDOT reports CAGR 0.95% and Annualized Volatility 1.36% with Sharpe 0.70 (arithmetic ratio 0.95 / 1.36 = 0.6985, consistent with zero risk-free rate), while SPY reports CAGR 10.87% and Volatility 18.95% with Sharpe 0.64 (arithmetic ratio 10.87 / 18.95 = 0.5736, conflicting with the printed 0.64) - arithmetic vs geometric return and risk-free rate conventions are unreconciled in the source."
  - "Economic return magnitude vs headline claim: The abstract and conclusion claim SDOT yields the 'best risk-adjusted market-neutral strategy under CVaR optimization (Sharpe 0.70, max drawdown -2.60%)', but the realized CAGR is only 0.95% per year on a 2x gross-leveraged book over 21 years (2005-2026, 5,406 trading days) - absolute economic return is sub-1% per annum before institutional short-borrowing or carrying costs - unreconciled."
  - "Bootstrap scenario degeneration: Section 5.5 and Table 5 report that under identical Rockafellar-Uryasev LP mean-CVaR optimization, historical Bootstrap yields w = 0 at every single rebalance for 258 months because atomic scenarios cause the CVaR penalty to dominate all potential gains, proving that active portfolio selection is entirely dependent on scenario continuity mechanics rather than empirical return data alone - unreconciled."
  - "Screening model contradiction: Phase 5 selects the 100 constituent stocks for the portfolio backtest using a Gaussian (multivariate normal) fit to all active S&P 500 constituents, despite Sections 3.4 and 5.2 proving mathematically and empirically that Gaussian generators understate tail risk and fail to generate valid tail structure - unreconciled."
  - "Out-of-sample regime collapse in static evaluation: In Phase 4 (train 1962-2004, test 2005-2026 without annual retraining), SDOT tail_3sigma drops to 0.33 +/- 0.03 (statistically indistinguishable from Bootstrap at 0.38 +/- 0.03) with CVaR relative errors of 38-82%, proving that SDOT alone does not predict out-of-sample regime shifts across crises (GFC/COVID) without rolling annual retraining - unreconciled."
---

# SDOT: Semi-Discrete Optimal Transport Non-Lipschitz Scenario Generation for Market-Neutral Mean-CVaR Optimization on S&P 500

## Provenance

- **Primary Source:** Ryan M. Engel (Simudyne, UK and Stony Brook University, USA), Kibaek Lee (Simudyne, UK), and Namid Stillman (Simudyne, UK), *"Financial Tail Risk Beyond Lipschitz Continuity via Semi-Discrete Optimal Transport"*, arXiv preprint `arXiv:2609.27785v1 [q-fin.RM, cs.CE, q-fin.CP, stat.ML]`.
- **Submission History:** Submitted to arXiv on 17 August 2026 (`[v1] Mon, 17 Aug 2026 15:43:08 UTC`), announced in the September 2026 batch (`arXiv:2609.27785`).
- **Publication Status:** Working paper preprint. No journal reference or publisher DOI is stated on the arXiv landing page.
- **License:** arXiv.org perpetual non-exclusive license.
- **Canonical DOI:** [10.48550/arXiv.2609.27785](https://doi.org/10.48550/arXiv.2609.27785).
- **Stable URLs:**
  - Abstract: https://arxiv.org/abs/2609.27785
  - HTML Full Text: https://arxiv.org/html/2609.27785v1
  - PDF Full Text: https://arxiv.org/pdf/2609.27785v1
- **Primary Source Inspection:** The complete PDF (`2609.27785.pdf`, 817 KB, 8 pages, SHA-256: `9bcf3c11438a2e584f27f0ec68910ebaa541ea5d3d4b6559db233e1eaae6966f`) and experimental HTML full text were retrieved and read directly on 2026-09-28. Every formula, empirical table, parameter value, and baseline metric cited in this record was verified against the primary document text.
- **Pre-write Deduplication Audit (2026-09-28):** Complete repository search using `git grep` and `grep -r` across all tracked files, manifests, worktrees, and Hermes Wiki Brain for `2609.27785`, `Semi-Discrete Optimal Transport`, `SDOT`, `Ryan M. Engel`, `Kibaek Lee`, and `Namid Stillman` returned **zero prior records**. Related risk-budgeting, optimal transport, and extreme-value captures in the repository (e.g. `entropic-value-at-risk-parity-tempered-stable-returns-2026-09-11.md`, `market-informed-network-husler-reiss-jeam-financial-extremes-2026-09-12.md`, and `wasserstein-distributional-risk-bounds-covariance-free-portfolio-2026-09-02.md`) investigate different frameworks (parametric EVaR risk budgeting, Hüsler-Reiss graphical models, distributionally robust Wasserstein covariance-free LP); none address Semi-Discrete Optimal Transport power-diagram non-Lipschitz scenario generation or Rockafellar-Uryasev LP mean-CVaR market-neutral optimization.

## Economic mechanism

### Source-reported

1. **Heavy Tails in Financial Returns:** Daily constituent returns of equity markets exhibit heavy tails and severe excess kurtosis (the authors report an empirical kurtosis of 87.7 across S&P 500 constituents after filtering data artifacts). Portfolio risk management programs optimizing tail-risk measures like Conditional Value-at-Risk (CVaR) rely on scenario generators that faithfully reflect these extreme probabilities.
2. **Lipschitz Architectural Obstruction in Deep Generative Models:** Modern neural density generators (Normalizing Flows like Real-NVP/Glow, Continuous Normalizing Flows [CNF] / FFJORD, OT-Flow, Denoising Diffusion Probabilistic Models [DDPM], Flow Matching [FM], and Generative Adversarial Networks [GANs]) sample by mapping a simple base distribution (typically standard Gaussian $\mathcal{N}(0, I_k)$) through a learned transport map $T: \mathbb{R}^d \to \mathbb{R}^d$. Neural networks composed of affine layers and standard nonlinearities (e.g. ReLU, GELU, Sigmoid) are globally Lipschitz with constant $\mathrm{Lip}(G) \le \prod_i \|W_i\|_2$.
3. **Gaussian Concentration Bound (Borell-TIS):** By the Borell-TIS inequality, any $L$-Lipschitz mapping of a standard Gaussian base distribution produces a target whose 1D projections $\psi \circ G$ are sub-Gaussian with variance proxy at most $L^2$:
   $$\mathbb{P}(|\psi(G(Z)) - m| > t) \le 2 \exp\left(-\frac{t^2}{2 L^2}\right)$$
   Consequently, every portfolio return $w^\top r$ with $\|w\|_2 \le 1$ remains sub-Gaussian under any finite Lipschitz generator. Targets with tails heavier than Gaussian (such as jump-diffusions whose MGF grows doubly exponentially) cannot be matched at any finite Lipschitz constant.
4. **Monge-Ampère Distortion Equation:** The Brenier optimal transport map $T = \nabla u$ satisfies the Monge-Ampère equation $\det(D^2 u(x)) = f(x) / g(\nabla u(x))$. This establishes an operator-norm lower bound on local map distortion:
   $$\|DT(x)\|_{\mathrm{op}} \ge \left(\frac{f(x)}{g(T(x))}\right)^{1/d}$$
   Where the target density $g$ has an interior trough (e.g. the transition region between the Gaussian diffusive core and the jump component), $g(T(x))$ becomes very small, forcing the learned map to exhibit violent local expansion. In practice, neural generators either:
   - Stay with a moderate Lipschitz constant, thereby **compressing tails** (understating extreme losses); or
   - Force a large Lipschitz constant to match tail events, thereby **inflating tails and exploding cross-seed estimator variance**.
5. **Semi-Discrete Optimal Transport (SDOT) Solution:** Rather than altering the source distribution, SDOT relaxes the continuity requirement of the transport map. Based on the geometric variational formulation of Gu et al. (2016), SDOT partitions the source continuous space into a power diagram $\mathcal{D}(h) = \bigcup_{i=1}^n W_i(h)$, where each cell $W_i(h)$ corresponds to one empirical observation $y_i$. At the variational energy minimizer $h^*$, each cell holds exactly $1/n$ of the source probability measure:
   $$w_i(h^*) = \mu(W_i(h^*)) = \frac{1}{n}$$
   Tail observations are reached by crossing discrete cell boundaries (a jump) rather than by stretching a continuous function. The model generates continuous, non-atomic scenarios via a piecewise-linear extension (Algorithms 1 & 2) that filters cell pairs by their dihedral angle on the lifted paraboloid.
6. **Portfolio Mean-CVaR Optimization:** Under the Rockafellar-Uryasev linear programming formulation, optimizing a market-neutral portfolio with zero net exposure and gross leverage limits depends strictly on the estimated tail loss quantiles of individual long-short pairs. Generators with sub-Gaussian tails understate tail losses, leading to spurious risk taking or severe drawdowns. SDOT's absolutely continuous, heavy-tailed scenarios provide realistic loss boundaries that prevent capital destruction during market stress events.

### Research interpretation

- **Hypothesis:** Asset return tails cannot be captured by Lipschitz-continuous neural generators without introducing either severe tail compression or volatile variance spikes. By relaxing map regularity via Semi-Discrete Optimal Transport (SDOT) power diagrams, non-Lipschitz cell boundaries allow tail risk frequencies to be inherited directly from empirical data while supporting absolutely continuous scenario sampling. When paired with Rockafellar-Uryasev LP mean-CVaR optimization under a zero-net-exposure market-neutral mandate, this tail-calibrated scenario distribution penalizes spurious cross-sectional correlations, limiting drawdowns during systemic market dislocations while producing stable, low-volatility risk-adjusted alpha.
- **Component Roles:**
  - *Generative Scenario Engine:* SDOT piecewise-linear generator (Algorithms 1 & 2) trained annually on historical daily returns of S&P 500 constituents.
  - *Universe Screening Filter:* Model-agnostic preliminary screen using a multivariate normal fit over all active constituents, generating 10,000 scenarios, solving full-universe mean-CVaR, and selecting the top 100 stocks by absolute weight magnitude.
  - *Asset Allocation Engine:* Rockafellar-Uryasev LP mean-CVaR optimization program solved via HiGHS on $S = 10,000$ generated return scenarios over $D = 100$ stocks.
  - *Portfolio Constraints:* Zero net exposure ($\sum w_i = 0$), gross leverage $\sum |w_i| \le 2.0$ ($2\times$), and individual asset weight cap $|w_i| \le 0.05$ (5%).
  - *Execution & Risk Mandate:* Monthly rebalancing, annual generator retraining on expanding historical windows, and transaction cost modeling at 5 basis points proportional to turnover.

## Signal

The strategy operates as a monthly rebalanced market-neutral cross-sectional portfolio driven by scenario-based mean-CVaR optimization:

### 1. Data Ingestion & Preprocessing
- **Source Universe:** All common stock constituents of the S&P 500 spanning 1962–2026 (644 distinct historical symbols, 3.6 million daily rows).
- **Constituent Filtering:** Returns outside an asset's official index membership window are zeroed to eliminate survivorship bias (`source-reported`).
- **Data Cleaning Filter:** Hard threshold dropping any daily return with $|r_t| > 0.95$ (`source-reported`). The source reports this eliminates 669 delisted-ticker artifacts while preserving all historical market crash events (e.g. October 1987, 2008 GFC, March 2020 COVID).

### 2. Annual Universe Screening
- At each annual retraining boundary, fit a multivariate normal distribution $\mathcal{N}(\mu, \Sigma)$ to all currently active S&P 500 constituents using expanding historical daily return data (`source-reported`).
- Generate 10,000 preliminary scenarios from this parametric distribution and solve the full-universe mean-CVaR optimization (`source-reported`).
- Select the top 100 stocks ranked by absolute weight magnitude ($|w_i|$) to form the active 100-asset trading universe for the upcoming year (`source-reported`).

### 3. Scenario Generation via SDOT (Algorithms 1 & 2)
- **Algorithm 1 — Monte Carlo Semi-Discrete OT Solver:**
  - Source domain is the uniform hypercube $[-1/2, 1/2]^d$ with $d = 100$.
  - At iteration $k$, sample $M$ Sobol quasi-Monte Carlo points $\{x_j\}_{j=1}^M$.
  - Assign each sample to its nearest power cell:
    $$i^*(x_j) = \arg\max_{i \in \{1,\dots,N\}} \{\langle x_j, y_i \rangle + h_i\}$$
    evaluated via parallel matrix multiplication on GPU (`source-reported`).
  - Calculate empirical cell volumes $\hat{w}_i = \#\{j \mid i^*(x_j) = i\} / M$.
  - Compute gradient $\nabla_h E(h) = \nu - \hat{w}(h)$, where $\nu_i = 1/N$.
  - Update dual potential vector $h$ via Adam with gauge centering $h \leftarrow h - \bar{h}$ (`source-reported`).
  - If gradient convergence stalls as measured by $\|\nabla_h E\|_2$, adaptively double Sobol batch size $M$ (`source-reported`).
- **Algorithm 2 — Piecewise-Linear Generation:**
  - Draw uniform samples from the source domain and identify their top-$K$ nearest cells via power diagram assignment (`source-reported`).
  - Compute the dihedral angle of the supporting planes on the lifted paraboloid for candidate cell pairs (`source-reported`).
  - Filter pairs by a dihedral angle threshold, retaining only pairs meeting at shallow angles and rejecting steep boundaries (`source-reported`).
  - Interpolate novel scenarios between accepted pairs: $P_{\mathrm{gen}} = (1 - w) P_i + w P_j$, where $w \in [0, 1]$ controls dissimilarity (`source-reported`).
  - Generate $S = 10,000$ joint return scenarios for the $D = 100$ screened stocks (`source-reported`).

### 4. Portfolio Allocation Program (Rockafellar-Uryasev LP)
- Solve the Rockafellar-Uryasev linear program for mean-CVaR optimization using the $S = 10,000$ scenarios over $D = 100$ assets (`source-reported`):
  $$\min_{w^+, w^-, \gamma, u} \left\{ \gamma + \frac{1}{(1 - \alpha) S} \sum_{s=1}^S u_s - \lambda \mathbb{E}[w^\top r_s] \right\}$$
  subject to:
  $$u_s \ge - (w^+ - w^-)^\top r_s - \gamma, \quad u_s \ge 0, \quad \forall s \in \{1,\dots,S\}$$
  $$\sum_{i=1}^D (w_i^+ - w_i^-) = 0 \quad (\text{zero net exposure / dollar neutral})$$
  $$\sum_{i=1}^D (w_i^+ + w_i^-) \le 2.0 \quad (\text{gross leverage} \le 2\times)$$
  $$0 \le w_i^+ \le 0.05, \quad 0 \le w_i^- \le 0.05 \quad (\text{max single-stock position} \le 5\%)$$
- Solved using the HiGHS dual revised simplex solver through `scipy.optimize.linprog` with sparse constraint matrices (10,201 variables, solves in $<1$ second) (`source-reported`).

### Underspecified Operational Fields & Research Proposals
- `research-proposed`: Exact mean-CVaR scalarization weighting parameter $\lambda$. The text specifies "CVaR-dominant optimization" and "CVaR-minimizing optimization" with inequality leverage constraints where the zero portfolio is feasible. For concrete implementation, $\lambda$ is set to $0.0$ (pure CVaR minimization subject to non-negative expected return) or a small constant $\lambda = 0.1$.
- `research-proposed`: The optimization confidence level $\alpha$ for Phase 5 backtesting is not explicitly identified as 1% vs 5% (Phase 1–3 report both, Table 5 reports realized CVaR 5%). Proposed default: $\alpha = 0.05$ (95% confidence CVaR).
- `research-proposed`: Algorithm 2 hyperparameter defaults: top-$K$ nearest cells $K = 5$, dihedral angle threshold $\theta_{\max} = 15^\circ$, and dissimilarity parameter $w \sim \mathrm{Uniform}(0, 1)$.
- `research-proposed`: Rebalance execution timestamp: monthly close-to-open rebalancing (rebalance evaluated on the last trading day of the calendar month at market close, executed on the first trading day of the subsequent month at the opening price).
- `research-proposed`: Short borrow fee model: flat 50 basis points per annum borrowing cost applied to the short leg $\sum w_i^-$, absent from the source's cost schedule.

## Required data

- **Universe:** S&P 500 index constituent stocks historical panel (1962–2026, 644 distinct tickers).
- **Constituent Membership Schedule:** Exact historical point-in-time index constituent entry and exit dates to enforce survivorship-bias-free filtering.
- **Price Fields:** Daily OHLCV bars (adjusted close for return calculation, open prices for order execution).
- **Preprocessing Constraints:** Hard outlier filter dropping daily returns $|r_t| > 0.95$.
- **Timeframe & Resolution:** Daily closing returns for model training, annual cadence for generator retraining, monthly cadence for portfolio rebalancing.
- **Hardware & Software Dependencies:** Single NVIDIA V100 GPU (or modern CUDA equivalent), JAX 0.5.0, HiGHS LP solver via SciPy.

## Execution assumptions

- **Net Exposure:** Exactly 0.0 (dollar-neutral long/short book) (`source-reported`).
- **Gross Leverage Limit:** Maximum $2.0\times$ gross exposure ($\sum |w_i| \le 2.0$) (`source-reported`).
- **Position Limits:** Maximum absolute weight of 5.0% per individual constituent ($|w_i| \le 0.05$) (`source-reported`).
- **Rebalance Frequency:** Monthly rebalancing across 258 calendar months (January 2005 through 2026, 5,406 trading days) (`source-reported`).
- **Transaction Costs:** Flat 5 basis points (0.05%) charged linearly on portfolio turnover: $\text{Fee}_t = 0.0005 \times \sum_{i=1}^D |w_{i,t} - w_{i,t^-}|$ (`source-reported`).
- **Execution Timing (`research-proposed`):** End-of-month signal calculation with execution at the market open on the first trading day of the month.
- **Slippage Model (`research-proposed`):** Zero slippage modeled in source; research proposes adding 3 basis points half-spread slippage per trade for realistic institutional execution.
- **Borrow Availability (`research-proposed`):** Source assumes unconstrained shorting across top-100 S&P 500 constituents; research proposes restricting shorting to names with $>10$ days to cover and borrowing fee $<100$ bps.

## Evidence

### Source-reported

All figures, tables, and comparative metrics below are directly extracted from Ryan M. Engel, Kibaek Lee, and Namid Stillman (`arXiv:2609.27785v1`, August/September 2026):

#### 1. Synthetic Merton Calibration & Distortion Sweep (Table 1 & Section 5.1)
- **Moment-Matching Fit:** Nelder-Mead on closed-form moment formulas calibrated to S&P 500 empirical distribution: $\sigma = 0.001$, $\lambda = 8.06$ annualized, $\Delta = 1/252$, $\mu_J = -0.006$, $\sigma_J = 0.132$, achieving loss $= 2.53 \times 10^{-10}$ with kurtosis 93.8 (vs empirical 87.7).
- **Phase 2 Regimes (Table 1):**
  - *Base (calibrated):* $\lambda = 8.06$, $\mu_J = -0.006$, $\sigma_J = 0.132$, Kurtosis $= 93.8$, $g_{\min} = 9.5 \times 10^{-2}$, $L^* / \hat{\sigma} = 18.2$.
  - *Moderate:* $\lambda = 2.0$, $\mu_J = -0.05$, $\sigma_J = 0.3$, Kurtosis $= 377.8$, $g_{\min} = 1.0 \times 10^{-2}$, $L^* / \hat{\sigma} = 46.6$.
  - *Heavy:* $\lambda = 1.0$, $\mu_J = -0.05$, $\sigma_J = 0.4$, Kurtosis $= 755.9$, $g_{\min} = 3.9 \times 10^{-3}$, $L^* / \hat{\sigma} = 68.8$.
  - *Extreme:* $\lambda = 0.45$, $\mu_J = -0.08$, $\sigma_J = 0.5$, Kurtosis $= 1,679$, $g_{\min} = 1.4 \times 10^{-3}$, $L^* / \hat{\sigma} = 112.5$.
  - *Density Trough:* Deepens $68\times$ from Base to Extreme, local distortion $L^*$ at the trough rises $6\times$, with minimum attained at $r^*$ between $-4 \times 10^{-4}$ and $-5 \times 10^{-4}$ (6 to 8 core standard deviations $\sigma \sqrt{\Delta} = 6.3 \times 10^{-5}$ from origin on the loss side).

#### 2. Phase 2 Generator Regularity Sweep (Table 2, Mean ± Std over 5 Seeds, 10,000 Samples in $\mathbb{R}^{100}$)
*Energy, MMD, SW1 scaled by $10^3$:*
- **Base Regime (Kurtosis 93.8):**
  - **SDOT (ours):** $\mathrm{tail}_{3\sigma} = 0.88 \pm 0.01$, $\mathrm{tail}_{4\sigma} = 0.85 \pm 0.01$, Energy $= 0.92 \pm 0.20$, MMD $= 1.77 \pm 0.50$, SW1 $= 1.75 \pm 0.07$.
  - Bootstrap: $1.00 \pm 0.01$, $1.00 \pm 0.01$, $0.28 \pm 0.02$, $-0.05 \pm 0.04$, $0.34 \pm 0.01$.
  - Gaussian: $0.16 \pm 0.00$, $0.01 \pm 0.00$, $4.37 \pm 0.36$, $0.52 \pm 0.14$, $3.71 \pm 0.04$.
  - Flow Matching (FM): $1.12 \pm 0.03$, $1.08 \pm 0.03$, $2.80 \pm 0.51$, $2.28 \pm 0.45$, $2.42 \pm 0.17$.
  - CNF: $0.96 \pm 1.06$, $0.70 \pm 1.00$, $25.0 \pm 36.8$, $49.4 \pm 64.4$, $7.57 \pm 5.27$.
  - OT-Flow: $0.64 \pm 0.21$, $0.28 \pm 0.18$, $21.9 \pm 21.0$, $34.0 \pm 35.4$, $6.34 \pm 2.45$.
  - DDPM: $1.32 \pm 0.09$, $1.04 \pm 0.07$, $19.2 \pm 2.3$, $25.9 \pm 3.7$, $14.6 \pm 0.5$.
  - WGAN: $1.19 \pm 1.28$, $0.44 \pm 0.58$, $8.24 \pm 13.1$, $10.6 \pm 16.5$, $4.27 \pm 4.37$.
- **Moderate Regime (Kurtosis 377.8):**
  - **SDOT (ours):** $0.94 \pm 0.01$, $0.93 \pm 0.00$, $0.37 \pm 0.06$, $0.15 \pm 0.18$, $1.04 \pm 0.11$.
  - FM: $1.01 \pm 0.08$, $1.02 \pm 0.07$, $10.4 \pm 1.5$, $4.27 \pm 1.67$, $4.37 \pm 0.61$.
  - CNF: $81.7 \pm 5.9$, $65.4 \pm 7.3$, $762 \pm 74.6$, $337 \pm 14.1$, $71.2 \pm 8.4$.
  - OT-Flow: $0.34 \pm 0.04$, $0.02 \pm 0.00$, $41.0 \pm 1.3$, $13.7 \pm 1.1$, $10.9 \pm 0.2$.
  - DDPM: $5.56 \pm 1.81$, $3.74 \pm 1.23$, $36.5 \pm 13.4$, $26.4 \pm 13.2$, $17.3 \pm 5.1$.
  - WGAN: $3.82 \pm 1.63$, $1.40 \pm 0.51$, $25.1 \pm 19.4$, $11.8 \pm 11.2$, $8.01 \pm 3.93$.
- **Heavy Regime (Kurtosis 755.9):**
  - **SDOT (ours):** $0.93 \pm 0.02$, $0.93 \pm 0.02$, $0.28 \pm 0.14$, $0.22 \pm 0.64$, $0.75 \pm 0.17$.
  - FM: $1.40 \pm 0.11$, $1.24 \pm 0.09$, $14.8 \pm 1.4$, $9.32 \pm 1.47$, $5.04 \pm 0.27$.
  - CNF: $160 \pm 32.1$, $109 \pm 39.5$, $726 \pm 149$, $343 \pm 18.3$, $71.3 \pm 13.9$.
  - OT-Flow: $0.60 \pm 0.06$, $0.03 \pm 0.00$, $64.7 \pm 1.4$, $35.3 \pm 2.9$, $13.4 \pm 0.1$.
  - DDPM: $9.07 \pm 5.24$, $5.61 \pm 3.54$, $35.9 \pm 10.5$, $32.9 \pm 8.9$, $9.76 \pm 3.76$.
  - WGAN: $3.04 \pm 3.15$, $1.25 \pm 1.58$, $25.6 \pm 5.5$, $16.2 \pm 5.6$, $8.12 \pm 1.15$.
- **Extreme Regime (Kurtosis 1,679):**
  - **SDOT (ours):** $0.91 \pm 0.02$, $0.89 \pm 0.02$, $0.11 \pm 0.01$, $0.08 \pm 0.08$, $0.75 \pm 0.12$.
  - Bootstrap: $1.00 \pm 0.02$, $1.00 \pm 0.02$, $0.10 \pm 0.01$, $-0.10 \pm 0.02$, $0.31 \pm 0.01$.
  - Gaussian: $3.40 \pm 0.35$, $0.29 \pm 0.06$, $83.5 \pm 0.8$, $75.5 \pm 1.6$, $14.4 \pm 0.2$.
  - FM: $4.88 \pm 1.94$, $2.76 \pm 0.80$, $18.4 \pm 3.1$, $98.5 \pm 4.9$, $5.01 \pm 0.69$.
  - CNF: $311 \pm 34.0$, $201 \pm 49.1$, $630 \pm 67.4$, $357 \pm 33.9$, $58.5 \pm 6.8$.
  - OT-Flow: $1.56 \pm 0.30$, $0.10 \pm 0.04$, $78.2 \pm 0.9$, $82.7 \pm 2.1$, $13.1 \pm 0.2$.
  - DDPM: $48.7 \pm 10.0$, $35.0 \pm 7.5$, $49.4 \pm 11.1$, $109 \pm 6.8$, $16.1 \pm 3.1$.
  - WGAN: $10.9 \pm 2.41$, $6.80 \pm 1.98$, $14.2 \pm 2.4$, $341 \pm 58.1$, $5.88 \pm 0.80$.
  - *Extreme Ratio Comparison:* SDOT's energy distance ($1.09 \times 10^{-4}$) is $169\times$ better than FM ($1.84 \times 10^{-2}$) and $5,780\times$ better than CNF ($6.30 \times 10^{-1}$).

#### 3. Cross-Domain Transfer & Real Held-Out Evaluation (Table 3, Mean ± Std over 5 Seeds)
- **Phase 3 — Synthetic-to-Real Transfer (1962–2026 S&P 500 Constituent Data):**
  - **SDOT (ours):** $\mathrm{tail}_{3\sigma} = 1.17 \pm 0.11$, $\mathrm{tail}_{4\sigma} = 1.95 \pm 0.15$, $\mathrm{tail}_{5\sigma} = 2.71 \pm 0.33$, $\mathrm{tail}_{6\sigma} = 3.40 \pm 0.70$, Energy $= 14.9 \pm 1.4$, MMD $= 46.3 \pm 5.2$, SW1 $= 6.85 \pm 0.31$, CVaR error $\epsilon_{1\%} = 21.8 \pm 1.9\%$, $\epsilon_{5\%} = 13.6 \pm 1.1\%$.
  - Bootstrap: $1.33 \pm 0.13$, $2.28 \pm 0.18$, $3.27 \pm 0.38$, $4.23 \pm 0.82$, Energy $20.1 \pm 1.0$, MMD $58.9 \pm 4.7$, SW1 $8.50 \pm 0.31$, $\epsilon_{1\%} = 17.0 \pm 1.7\%$, $\epsilon_{5\%} = 12.8 \pm 1.8\%$.
  - CNF: $\mathrm{tail}_{3\sigma} = 0.11$, $\mathrm{tail}_{5\sigma} = 0.00$, Energy $13.6$, $\epsilon_{1\%} = 62.9 \pm 1.7\%$, $\epsilon_{5\%} = 47.0 \pm 2.3\%$.
- **Phase 4 — Real S&P 500 Chronological Split (Train 1962–2004, Test 2005–2026):**
  - All static models without annual retraining exhibited large CVaR relative errors of 38%–82% across GFC and COVID crises.
  - SDOT: $\mathrm{tail}_{3\sigma} = 0.33 \pm 0.03$, $\mathrm{tail}_{4\sigma} = 0.28 \pm 0.04$, Energy $8.89 \pm 1.14$, $\epsilon_{1\%} = 51.3 \pm 3.3\%$, $\epsilon_{5\%} = 49.4 \pm 3.0\%$.
  - Bootstrap: $\mathrm{tail}_{3\sigma} = 0.38 \pm 0.03$, $\mathrm{tail}_{4\sigma} = 0.34 \pm 0.03$, Energy $9.11 \pm 1.38$, $\epsilon_{1\%} = 51.2 \pm 3.0\%$, $\epsilon_{5\%} = 51.2 \pm 2.8\%$.

#### 4. Preprocessing Data Cleaning Ablation (Table 4, Phase 4 Test Period 2005–2026)
- Raw baseline: 0 rows dropped, Kurtosis $= 69,245 \pm 41,552$.
- Winsorize 99.9th percentile: 7,166 clipped, Kurtosis $= 10.6 \pm 0.4$ (erases heavy tails).
- Winsorize 99.99th percentile: 720 clipped, Kurtosis $= 900.2 \pm 420.0$ (boundary clipping spikes).
- Hard $|r| > 1.00$: 409 dropped, Kurtosis $= 262.6 \pm 135.8$ (retains delisted ticker $-99.97\%$ price record artifacts).
- **Hard $|r| > 0.95$ (chosen):** 669 dropped, Kurtosis $= 87.7 \pm 25.5$ (preserves genuine market crash events while removing spurious delistings).
- Hard $|r| > 0.75$: 768 dropped, Kurtosis $= 54.7 \pm 10.4$.
- Hard $|r| > 0.50$: 932 dropped, Kurtosis $= 33.9 \pm 4.8$.

#### 5. Phase 5 — 21-Year Out-of-Sample Portfolio Backtest (Table 5, 2005–2026)
*Evaluation over 258 months (5,406 trading days) with monthly rebalancing, annual retraining, zero net exposure, $2\times$ gross leverage, 5% max single weight, net of 5 bps transaction costs. All figures in percent except Sharpe and Sortino:*
- **SDOT (ours):** **Sharpe 0.70**, **Sortino 1.16**, **CAGR 0.95%**, **Annualized Volatility 1.36%**, **Max Drawdown -2.60%**, **Realized CVaR 5% -0.18%**. (Ranked #1 across all generative models).
- **CNF:** Sharpe 0.40, Sortino 0.62, CAGR 0.41%, Vol 1.06%, Max DD -7.52%, CVaR 5% -0.15%.
- **WGAN:** Sharpe 0.21, Sortino 0.32, CAGR 1.45%, Vol 9.63%, Max DD -28.4%, CVaR 5% -1.30%.
- **Minimum Variance:** Sharpe 0.04, Sortino 0.06, CAGR 0.01%, Vol 6.82%, Max DD -33.0%, CVaR 5% -0.96%.
- **DDPM:** Sharpe -0.05, Sortino -0.07, CAGR -0.13%, Vol 1.98%, Max DD -14.5%, CVaR 5% -0.34%.
- **OT-Flow:** Sharpe -0.12, Sortino -0.18, CAGR -1.18%, Vol 6.86%, Max DD -35.7%, CVaR 5% -1.01%.
- **Flow Matching (FM):** Sharpe -0.23, Sortino -0.30, CAGR -0.23%, Vol 0.95%, Max DD -11.1%, CVaR 5% -0.14%.
- **Market Reference SPY (buy-and-hold):** Sharpe 0.64, Sortino 0.90, CAGR 10.87%, Vol 18.95%, Max DD -55.2%, CVaR 5% -2.90%.
- **Excluded Baseline Behavior:** Bootstrap and Gaussian generators produce $w = 0$ at every monthly rebalance, taking zero risk and generating zero active return over the entire 21-year backtest.

### Independently reproduced

`Not independently reproduced.`

### Negative evidence

1. **Sub-1% Annualized Return Drag:** Realized CAGR of the SDOT market-neutral strategy is only 0.95% per year at $2\times$ gross leverage. While the Sharpe ratio is 0.70 and Max Drawdown is minimal at -2.60%, the strategy's low absolute return makes it highly susceptible to unmodeled operational costs, such as institutional borrowing fees, securities lending rebates, margin interest, or execution slippage.
2. **Total Inaction of Historical Bootstrap:** Under the identical Rockafellar-Uryasev LP formulation, historical Bootstrap produces $w = 0$ for all 258 rebalance periods. The zero portfolio is chosen because atomic scenarios concentrate mass at exact historical points, causing the CVaR penalty to eliminate all positive expected return combinations. The strategy's active trading is thus an artifact of the piecewise-linear continuous smoothing in SDOT rather than an edge extracted directly from raw historical data.
3. **Severe Nonstationarity Without Rolling Retraining:** In Phase 4, when trained once on 1962–2004 and tested statically on 2005–2026, SDOT tail ratios collapse to $0.33 \pm 0.03$ (identical to Bootstrap at $0.38 \pm 0.03$) with 38%–82% CVaR relative errors. The model possesses no intrinsic forward-looking capability and requires frequent (annual) retraining to assimilate new tail regimes.
4. **Gaussian Pre-Screening Bias:** The initial universe reduction from all S&P 500 constituents to 100 assets is performed by fitting a multivariate normal (Gaussian) distribution. Assets exhibiting extreme idiosyncratic skewness or jump dynamics that do not appear in the Gaussian mean-CVaR screening may be prematurely excluded before SDOT ever models them.
5. **High Computation and Complexity of Variational Solver:** Although the LP solves in $<1$ second, SDOT training involves iterative Sobol Monte Carlo sampling with adaptive batch doubling on a GPU. In high dimensions ($d = 100$), cell volume approximation scales as $O(1/\sqrt{M})$, requiring substantial GPU compute during retraining cycles.
6. **Absence of Real Transaction Cost and Borrow Frictions:** The backtest applies a simple 5 bps linear fee on turnover. It completely ignores short-sale borrow constraints, hard-to-borrow fees, margin financing costs, bid-ask spread variations during market crises, and market impact on less liquid constituent names.

## Falsification plan

- **F1 — Out-of-Sample Rolling Forward Walk (2026–2031):** Evaluate SDOT on daily S&P 500 constituent returns out-of-sample starting from 2026-10-01 under the identical annual retraining schedule. Treat the hypothesis as refuted if out-of-sample Sharpe drops below `0.25` or annualized volatility exceeds `4.0%` over a minimum 3-year evaluation window (`research-defined falsification threshold`).
- **F2 — Transaction Cost Sensitivity Ladder:** Sweep round-trip transaction costs from 0 to 25 bps (0, 5, 10, 15, 20, 25 bps) with an additional 50 bps annualized short borrow fee on short legs. Treat the strategy as economically non-viable if net CAGR turns negative at or below `10 bps` total round-turn friction (`research-defined falsification threshold`).
- **F3 — Dihedral Angle Threshold Ablation:** Vary the dihedral angle threshold in Algorithm 2 across $\{5^\circ, 10^\circ, 15^\circ, 30^\circ, 60^\circ, 90^\circ\}$. If tail preservation metrics (tail$_{3\sigma}$, tail$_{4\sigma}$) degrade by $>25\%$ or portfolio Sharpe collapses below `0.30`, classify the strategy as hypersensitive to non-physical geometric tuning (`research-defined falsification threshold`).
- **F4 — Synthetic Jump-Diffusion Placebo Test:** Generate 100 synthetic market datasets with pure Gaussian increments (zero jump intensity, $\lambda = 0$). If SDOT continues to select active long-short portfolios that claim to harvest tail structure when no tail structure exists, conclude the portfolio selection is fitting sampling noise (`research-defined falsification threshold`).
- **F5 — Screen Permutation Control:** Replace the Gaussian 100-stock pre-screening filter with: (a) 100 most liquid stocks by dollar volume, (b) 100 randomly sampled stocks, and (c) full 500-stock universe. If SDOT performance collapses on the 100 most liquid names (Sharpe $<0.20$), attribute the reported performance to illiquidity bias in smaller constituents (`research-defined falsification threshold`).
- **F6 — Factor Exposure & Beta Neutrality Audit:** Regress the realized monthly return series against the Fama-French 5-factor model plus momentum and short-term reversal factors. If the Fama-French alpha intercept $t$-statistic is $<1.96$ or market beta differs significantly from zero ($|t_\beta| > 2.0$), reject the claim of pure market-neutral tail risk alpha (`research-defined falsification threshold`).
- **F7 — Rebalance Timing Luck Stress Test:** Shift the monthly rebalancing date across all 20 trading days of each month (day 1 through day 20). If the dispersion of 21-year CAGR exceeds `0.50%` or more than 30% of day-shifts produce a Sharpe $<0.30$, reject the strategy as confounded by rebalance timing luck (`research-defined falsification threshold`).
- **F8 — Execution Delay & Fill Realism:** Introduce a 1-day execution lag between scenario generation (day $T$ close) and execution (day $T+1$ close vs day $T+2$ open). If Sharpe drops by $>50\%$, reject the strategy as reliant on unrealistic simultaneous close execution (`research-defined falsification threshold`).

## Crypto portability

- **Portability Classification:** `unproven` (`research interpretation`).
- **Porting Rationale & Divergences:**
  - *Absence of Historical constituent panel:* S&P 500 provides a 64-year survivorship-bias-free panel with clear corporate action accounting. Crypto lacks a comparable multi-decade index; constituent turnover across top-100 altcoins exceeds 50% every 2–3 years, creating extreme survival and listing bias.
  - *Extreme Tail Kurtosis:* Top crypto assets exhibit kurtosis values exceeding 200–1,000 routinely, placing crypto directly in the "Heavy" to "Extreme" regime of Table 1. While SDOT theoretically handles extreme distortion better than neural models, crypto jump clustering and cross-token tail co-dependence (cascading liquidations) violate the static IID scenario assumptions.
  - *Perpetual Funding Rate Drag:* In equity market neutrality, shorting stocks yields a short rebate (collateral yield minus borrow fee). In crypto perpetuals, market-neutral books are subject to dynamic 8-hour funding rates. If long legs hold altcoins that pay funding while short legs pay funding during bull regimes, funding costs can exceed 15–30% annualized, immediately wiping out a sub-1% CAGR.
  - *24/7 Trading & Mark-Price Liquidation:* Monthly rebalancing is dangerously slow for crypto tail risk; extreme tail dislocations (e.g. 50% intraday liquidation cascades) occur over minutes to hours. A monthly rebalanced $2\times$ gross-leveraged crypto portfolio faces terminal liquidation risk without continuous dynamic deleveraging overlays.
- **Porting Requirements:** Any future crypto adaptation would require: (1) shifting from monthly to daily or 8-hour rebalancing; (2) incorporating perpetual funding rate forecasts directly into the LP objective; and (3) adding intraday margin liquidation constraints based on exchange mark-price rules.

## Limitations

- **Low Absolute Economic Return:** 0.95% annualized CAGR on a $2\times$ leveraged portfolio provides almost zero margin of safety against institutional borrowing fees, exchange trading commissions, or unexpected execution slippage.
- **Dependency on Piecewise-Linear Smoothing:** The contrast with Bootstrap reveals that active positions are driven entirely by synthetic continuous interpolation between power cells rather than raw empirical data points.
- **Regime Nonstationarity:** Without frequent annual retraining, the model fails to capture structural breaks, yielding 50%+ relative CVaR estimation errors across market crises.
- **Single Asset-Class Testing:** The empirical backtest is exclusively conducted on US large-cap equities (S&P 500); no empirical verification exists for foreign equities, commodities, fixed income, or digital assets.
- **Underspecified Optimization Details:** Key scalarization hyperparameters in the Rockafellar-Uryasev LP and Algorithm 2 dihedral thresholds are omitted from the text, requiring research-proposed default values for reproduction.

## Implementation status

- `not-implemented`.
- This research record represents a source-verified literature capture and normalization. No implementation exists in the current quantitative research stack, PyBroker, NautilusTrader, paper trading, testnet, or live trading workflows.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- A record being present in this repository does not authorize implementation, paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — Authoritative strategy research record specification contract.
- `[[quant/entropic-value-at-risk-parity-tempered-stable-returns-2026-09-11]]` — EVaR risk budgeting under heavy-tailed tempered stable distributions.
- `[[quant/crypto-bitcoin-cvar-risk-aware-q-learning-adaptive-controller-2026-09-02]]` — CVaR risk-constrained reinforcement learning in crypto derivatives.
- `[[quant/expected-shortfall-factor-model-common-tail-loss-severity-2026-09-11]]` — Tail-risk factor modeling and expected shortfall loss attribution.
- `[[quant/wasserstein-distributional-risk-bounds-covariance-free-portfolio-2026-09-02]]` — Distributionally robust Wasserstein LP optimization under distributional ambiguity.
- `[[quant/simple-dynamic-stock-bond-gold-markowitz-volatility-control-2026-09-11]]` — Dynamic multi-asset allocation under volatility control and Markowitz optimization.

## Sources

1. **Primary Research Paper:** Ryan M. Engel, Kibaek Lee, and Namid Stillman. *"Financial Tail Risk Beyond Lipschitz Continuity via Semi-Discrete Optimal Transport."* arXiv preprint `arXiv:2609.27785v1 [q-fin.RM, cs.CE, q-fin.CP, stat.ML]`, submitted 17 August 2026, announced September 2026.
   - Abstract: https://arxiv.org/abs/2609.27785
   - HTML Full Text: https://arxiv.org/html/2609.27785v1
   - PDF Full Text: https://arxiv.org/pdf/2609.27785v1
   - Canonical DOI: https://doi.org/10.48550/arXiv.2609.27785
2. **Algorithmic Foundations Cited in Primary Source:**
   - X. Gu, F. Luo, J. Sun, and S. Yau (2016). *"Variational Principles for Minkowski Type Problems, Discrete Optimal Transport, and Discrete Monge–Ampère Equations."* Asian Journal of Mathematics, 20(2):383–398.
   - D. An, Y. Guo, N. Lei, Z. Luo, S. Yau, and X. Gu (2020). *"AE-OT: A New Generative Model Based on Extended Semi-Discrete Optimal Transport."* International Conference on Learning Representations (ICLR).
   - R. T. Rockafellar and S. Uryasev (2000). *"Optimization of Conditional Value-at-Risk."* Journal of Risk, 2(3):21–41.
   - R. T. Rockafellar and S. Uryasev (2002). *"Conditional Value-at-Risk for General Loss Distributions."* Journal of Banking & Finance, 26(7):1443–1471.
   - C. Borell (1975). *"The Brunn–Minkowski Inequality in Gauss Space."* Inventiones Mathematicae, 30(2):207–216.
   - P. Jaini, I. Kobyzev, Y. Yu, and M. A. Brubaker (2020). *"Tails of Lipschitz Triangular Flows."* International Conference on Machine Learning (ICML), PMLR 119:4673–4681.
