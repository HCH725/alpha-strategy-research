---
schema: strategy-research-record-v1
title: "Dependence Uncertainty and the Concentration Paradox: Majorization Bounds, Worst-Case Risk Regimes, and Weighted Robust Portfolio Selection"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - dependence-uncertainty
  - majorization-order
  - concentration-paradox
  - robust-optimization
  - expected-shortfall
  - value-at-risk
  - range-var
  - weighted-robustness
status: research-only
confidence: high
source_as_of: 2026-09-17
sources:
  - "Peng Liu and Yang Liu, 'Portfolio Diversification and Concentration under Dependence Uncertainty: A Majorization Approach', arXiv preprint arXiv:2609.04496v1 [q-fin.PM, math.PR], submitted September 3, 2026. https://arxiv.org/abs/2609.04496"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Dependence Uncertainty and the Concentration Paradox: Majorization Bounds, Worst-Case Risk Regimes, and Weighted Robust Portfolio Selection

## Provenance

- **Primary Academic Source:** Peng Liu (School of Mathematics, Statistics and Actuarial Science, University of Essex, Colchester, UK, `peng.liu@essex.ac.uk`) and Yang Liu (School of Science and Engineering, The Chinese University of Hong Kong, Shenzhen, China, `yangliu16@cuhk.edu.cn`), *"Portfolio Diversification and Concentration under Dependence Uncertainty: A Majorization Approach"*, arXiv preprint `arXiv:2609.04496v1 [q-fin.PM, math.PR]`, submitted September 3, 2026.
- **Canonical arXiv URL:** https://arxiv.org/abs/2609.04496
- **Canonical Full-Text HTML:** https://arxiv.org/html/2609.04496v1
- **Canonical Full-Text PDF:** https://arxiv.org/pdf/2609.04496v1
- **DOI:** [10.48550/arXiv.2609.04496](https://doi.org/10.48550/arXiv.2609.04496)
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0) / arXiv perpetual non-exclusive license.
- **Direct Primary-Source Verification:** The complete preprint full text (Sections 1–9, Theorems 1–5, Propositions 1–7, Remarks 1–3, Numerical Illustrations 7.1–7.4, Tables 1–6, Figures 1–2, and References [1]–[57]) was directly retrieved and audited. All mathematical formulations, majorization consistency equivalences, worst-case convolution bounds, simplex vertex concentration proofs, and numerical calibration tables trace directly to `arXiv:2609.04496v1`.
- **Repository Deduplication Audit:** Pre-write search across all records in `alpha-strategy-research` confirmed zero prior citations of `arXiv:2609.04496`, Peng Liu, or Yang Liu's dependence uncertainty majorization framework. Existing portfolio optimization and distributional robustness records in the repository:
  - `wasserstein-robust-portfolio-hyperplane-dual-lp-2026-09-02.md` (Hsieh & Gan 2026, arXiv:2608.07032) studied certified Wasserstein bounds via supporting hyperplane majorization for nonlinear concave utility functions; it did not study majorization ordering of portfolio weight vectors, copula ambiguity sets with fixed marginals, or the concentration paradox for tail-risk functionals.
  - `special-markowitz-thermodynamic-joint-regularisation-returns-covariance-2026-09-17.md` (Reinhardt 2026, arXiv:2609.14029) and `evar-parity-tempered-stable-returns-risk-budgeting-2026-09-13.md` (Choi 2026, arXiv:2609.11905) investigated joint thermodynamic free energy covariance shrinkage and entropic VaR Euler risk budgeting, both assuming known joint distributions.
  - `defi-g3m-automated-market-maker-verifiable-portfolio-mandate-2026-09-02.md` (Feinstein, Florescu & O'Leary 2026, arXiv:2608.02917) investigated verifiable portfolio replication via AMM pools.
  - In contrast, Liu & Liu (2026) prove the structural "concentration paradox": when the copula is fully ambiguous, robust optimization under Value-at-Risk, Expected Shortfall, and Range-VaR mathematically penalizes diversification and drives allocations to simplex vertices, establishing the exact theoretical foundation for why diversification fails under unconstrained copula stress and providing a weighted robustness framework to control the transition.

## Economic mechanism

### Source-reported

Modern Portfolio Theory dating back to Markowitz (1952) identifies diversification as the foundational mechanism for risk reduction. When asset return distributions and their joint dependencies (copula) are known or accurately estimated, spreading capital across assets with correlations below unity lowers overall portfolio volatility.

However, in financial market stress regimes, asset return marginals are often reasonably identifiable from historical univariate time series, but their joint dependence structure becomes severely unstable, non-stationary, or completely ambiguous:
- Historical correlations breakdown during systemic liquidity crunches (e.g., the 2023 collapse of Silicon Valley Bank, where seemingly uncorrelated interest-rate risks, deposit runs, and asset-backed security durations aligned simultaneously).
- When a risk manager evaluates portfolios across an ambiguity set $\mathcal{E}_n(\mathbf{F}) = \{ F_{\mathbf{X}} : X_i \sim F_i, i=1,\dots,n \}$ with fixed marginals but completely unknown dependence, worst-case risk evaluation alters the geometry of the objective function.
- Liu & Liu (2026) discover that under complete dependence uncertainty, widely-used risk measures (Expected Shortfall, Value-at-Risk, Range-VaR, and Standard Deviation under location-scale families) trigger a **"concentration paradox"**: worst-case risk bounds are maximized by diversified portfolios (such as the equal-weight portfolio) and minimized by concentrated portfolios.
- Consequently, maximizing risk-adjusted return under worst-case dependence recommends concentrating 100% of capital into a single asset (a vertex of the probability simplex $\Delta_n$). By concentrating, an investor eliminates exposure to adverse tail-dependence couplings (such as comonotonicity) that can occur across multi-asset portfolios in a crisis.

### Research interpretation

The economic thesis separates into two falsifiable regimes governed by dependence uncertainty:
1. **Credible Copula Regime (Low Ambiguity):** Diversification across assets reduces idiosyncratic risk when joint dependence is constrained within narrow bounds. Here, asset weight averaging via doubly stochastic matrices $\boldsymbol{\beta} = \Lambda \boldsymbol{\lambda}$ reduces risk if the risk functional is quasi-convex (Theorem 1).
2. **Extreme Copula Ambiguity Regime (Systemic Stress):** When correlations and tail copulas cannot be trusted, holding multiple assets creates structural exposure to adversarial joint tail events. Holding multiple assets allows nature (or adversarial market-wide liquidity cascades) to synchronize losses across all holdings. The robust mini-max response is to identify the single asset with the highest standalone risk-adjusted tail profile ($j^* = \arg\max_j \{ \mathbb{E}[-X_j] - \kappa \rho(X_j) \}$) and hold zero weight in all other assets.
3. **Regulated Transition via Weighted Robustness:** Real-world portfolios need not swing discontinuously between 100% diversified and 100% concentrated. Liu & Liu's weighted robustness framework introduces a weight $\omega \in [0, 1]$ balancing the empirical joint reference model (weight $1-\omega$) against the comonotonic worst-case penalty (weight $\omega$), structurally analogous to the Basel FRTB Expected Shortfall framework.

## Signal

The trading and allocation signal represents the robust capital allocation vector $\boldsymbol{\lambda}^* \in \Delta_n$ derived under the four uncertainty regimes in Sections 5, 6, and 8 of Liu & Liu (`arXiv:2609.04496v1`, `source-reported`).

### 1. Mathematical Framework & Notation (`source-reported`)

- **Asset Universe:** $n$ assets with negative return vector $\mathbf{X} = (X_1, \dots, X_n)^\top \in \mathcal{X}^n$, where higher values denote larger losses.
- **Portfolio Simplex:** $\Delta_n = \{ \boldsymbol{\lambda} \in [0, 1]^n : \sum_{i=1}^n \lambda_i = 1 \}$ (no short-selling).
- **Majorization Order:** A weight vector $\boldsymbol{\beta}$ is dominated by $\boldsymbol{\lambda}$ ($\boldsymbol{\beta} \preceq \boldsymbol{\lambda}$) if and only if there exists a doubly stochastic matrix $\Lambda \in \mathcal{Q}_n$ such that $\boldsymbol{\beta} = \Lambda \boldsymbol{\lambda}$. $\boldsymbol{\beta}$ is strictly "more diversified" than $\boldsymbol{\lambda}$.
- **Risk Functionals:**
  - Value-at-Risk: $\mathrm{VaR}_\alpha^+(X) = \inf\{ x \in \mathbb{R} : F_X(x) > \alpha \}$.
  - Expected Shortfall: $\mathrm{ES}_\alpha(X) = \frac{1}{1-\alpha} \int_\alpha^1 \mathrm{VaR}_u(X) du$.
  - Range-VaR: $R_{\beta, \alpha}(X) = \frac{1}{\alpha} \int_\beta^{\beta+\alpha} \mathrm{VaR}_u(X) du$ for $0 \le \beta < \beta+\alpha \le 1$.
  - Standard Deviation: $\mathrm{SD}(X) = \sqrt{\operatorname{Var}(X)}$.

### 2. Allocation Policies Across Uncertainty Regimes (`source-reported`)

#### Regime A: Known Dependence & Quasi-Convex Consistency (Theorem 1)
- Objective: $\inf_{\boldsymbol{\lambda} \in \Delta_n} \rho(\boldsymbol{\lambda}^\top \mathbf{X})$.
- Theorem 1 establishes that weak consistency with the majorization order ($S_\rho(\boldsymbol{\beta}) \le \max_{k} S_\rho(\Pi_k \boldsymbol{\lambda})$ for $\boldsymbol{\beta} \preceq \boldsymbol{\lambda}$) holds if and only if $\rho$ is **quasi-convex**:
  $$\rho(\lambda X + (1-\lambda)Y) \le \max\{\rho(X), \rho(Y)\}, \quad \forall \lambda \in [0, 1].$$
- If $\mathbf{X}$ is exchangeable, quasi-convexity guarantees that diversification monotonically reduces risk: $\boldsymbol{\beta} \preceq \boldsymbol{\lambda} \implies S_\rho(\boldsymbol{\beta}) \le S_\rho(\boldsymbol{\lambda})$.

#### Regime B: Complete Dependence Uncertainty & Simplex Vertex Concentration (Theorems 3–5)
When only marginals $\mathbf{F} = (F_1, \dots, F_n)$ are known and the copula is unconstrained:
- Objective:
  $$\sup_{\boldsymbol{\lambda} \in \Delta_n} \inf_{F_{\mathbf{X}} \in \mathcal{E}_n(\mathbf{F})} \left\{ \mathbb{E}[-\boldsymbol{\lambda}^\top \mathbf{X}] - \kappa \rho(\boldsymbol{\lambda}^\top \mathbf{X}) \right\}$$
- **Expected Shortfall / Subadditive-Comonotonic Measures (Proposition 5):**
  $$\boldsymbol{\lambda}^* = \mathbf{e}_{j^*}, \quad j^* = \arg\max_{j=1,\dots,n} \{ \mathbb{E}[-X_j] - \kappa \mathrm{ES}_\alpha(X_j) \}$$
- **Right-Quantile Value-at-Risk $\mathrm{VaR}_\alpha^+$ (Theorem 3):**
  Under decreasing tail marginal densities ($\mathbf{F} \in (\mathcal{M}_D^\alpha)^n$) or $n=2$:
  $$\boldsymbol{\lambda}^* = \mathbf{e}_{j^*}, \quad j^* = \arg\max_{j=1,\dots,n} \{ \mathbb{E}[-X_j] - \kappa \mathrm{VaR}_\alpha^+(X_j) \}$$
- **Range-VaR $R_{\beta, \alpha}$ (Theorem 4):**
  Under decreasing tail marginal densities ($\mathbf{F} \in (\mathcal{M}_D^{1-\alpha-\beta})^n$):
  $$\boldsymbol{\lambda}^* = \mathbf{e}_{j^*}, \quad j^* = \arg\max_{j=1,\dots,n} \{ \mathbb{E}[-X_j] - \kappa R_{\beta, \alpha}(X_j) \}$$
- **Standard Deviation $\mathrm{SD}$ (Theorem 5):**
  - Worst case is comonotonic coupling.
  - If $F_1, \dots, F_n$ belong to the same location-scale family, concentration is strictly optimal:
    $$\boldsymbol{\lambda}^* = \mathbf{e}_{j^*}, \quad j^* = \arg\max_{j=1,\dots,n} \{ \mathbb{E}[-X_j] - \kappa \mathrm{SD}(X_j) \}$$
  - If marginals have heterogeneous shapes (e.g. Normal vs Laplace or Normal vs Lognormal), comonotonic correlation is strictly less than 1 ($\operatorname{Corr}(Z, \exp(Z)) = 1/\sqrt{e-1} \approx 0.7629$), restoring an interior diversified optimum over an intermediate risk-aversion window.

#### Regime C: Structured Wasserstein and Moment Uncertainty (Propositions 6–7)
- **Wasserstein Ambiguity Ball $\mathcal{M}_{a,p,\varepsilon}^n(F_0)$ (Proposition 6):**
  $$\sup_{F_{\mathbf{X}} \in \mathcal{M}_{a,p,\varepsilon}^n(F_0)} \rho_g(\boldsymbol{\lambda}^\top \mathbf{X}) = \rho_g(\boldsymbol{\lambda}^\top \mathbf{X}_0) + \kappa \varepsilon \|\boldsymbol{\lambda}\|_b \|g'\|_q$$
  where $1/a + 1/b = 1$ and $1/p + 1/q = 1$. The $\ell_b$ norm penalty $\|\boldsymbol{\lambda}\|_b$ directly penalizes concentration and encourages diversification as the ambiguity radius $\varepsilon$ increases.
- **Moment Uncertainty Set $\mathcal{U}_n(\boldsymbol{\mu}, \Sigma)$ (Proposition 7):**
  $$\sup_{F_{\mathbf{X}} \in \mathcal{U}_n(\boldsymbol{\mu}, \Sigma)} \rho_g(\boldsymbol{\lambda}^\top \mathbf{X}) = \boldsymbol{\lambda}^\top \boldsymbol{\mu} + \kappa v_{g^*} \sqrt{\boldsymbol{\lambda}^\top \Sigma \boldsymbol{\lambda}}$$
  reducing the robust objective to a deterministic Markowitz-type mean-volatility program with scaling constant $v_{g^*} = \sqrt{\int_0^1 ((g^*)'(t) - g(1))^2 dt}$.

#### Regime D: Weighted Robustness Allocation Model (Section 8)
- Objective across robustness weight $\omega \in [0, 1]$ for multivariate elliptical/normal returns $\mathbf{X} \sim N(\boldsymbol{\mu}, \Sigma)$:
  $$\min_{\boldsymbol{\lambda} \in \Delta_n} \left\{ \boldsymbol{\lambda}^\top \boldsymbol{\mu} + \omega c_p \boldsymbol{\lambda}^\top \boldsymbol{\sigma} + (1-\omega) c_p \sqrt{\boldsymbol{\lambda}^\top \Sigma \boldsymbol{\lambda}} \right\}$$
  where $c_p = \frac{\phi(\Phi^{-1}(p))}{1-p}$, $\boldsymbol{\sigma} = (\sigma_1, \dots, \sigma_n)^\top$ is the vector of marginal standard deviations, and $\Sigma$ is the reference covariance matrix.
- The Karush-Kuhn-Tucker (KKT) stationarity condition for the optimal allocation $\boldsymbol{\lambda}^*$ is:
  $$\boldsymbol{\mu} + c_p \left( \omega \boldsymbol{\sigma} + (1-\omega) \frac{\Sigma \boldsymbol{\lambda}^*}{\sqrt{(\boldsymbol{\lambda}^*)^\top \Sigma \boldsymbol{\lambda}^*}} \right) - \nu \mathbf{1}_n - \boldsymbol{\eta} = \mathbf{0}, \quad \eta_i \lambda_i^* = 0, \quad \boldsymbol{\eta} \ge \mathbf{0}.$$

### 3. Empirical Discretization & Portfolio Rebalancing Engine (`research-proposed`)

For quantitative portfolio implementation in liquid equity or crypto markets:
- **Rebalance Cadence:** Weekly or monthly rebalancing at Friday close (`research-proposed`).
- **Marginal Parameter Estimation:** Fit parametric marginals (Normal, Student-$t$, skewed-$t$, or Empirical Quantiles) using rolling 252-day lookback windows (`research-proposed`).
- **Ambiguity Weight Adaptation ($\omega_t$):** Dynamically calibrate $\omega_t \in [0, 1]$ to the systemic stress regime via rolling copula stability:
  $$\omega_t = \min\left(1.0, \, \max\left(0.0, \, \frac{\bar{\rho}_{t, 30\text{d}} - \bar{\rho}_{t, 252\text{d}}}{\sigma_{\rho, 252\text{d}}}\right)\right) \quad (\text{research-proposed})$$
  where $\bar{\rho}$ is the average cross-sectional pairwise asset correlation. When market correlation spikes during liquidations, $\omega_t \to 1$ shifting capital toward the single lowest-risk asset; in quiet markets, $\omega_t \to 0$ restoring standard Markowitz/mean-ES diversification.

## Required data

- **Asset Universe:** Multi-asset cross-section ($n$ liquid cash equities, ETFs, or spot/perpetual crypto assets).
- **Return Series:** Daily adjusted closing prices to compute negative log returns $X_{i, t} = -\ln(P_{i, t} / P_{i, t-1})$.
- **Marginal Loss Quantiles:** Empirical or parametric estimates of:
  - Mean loss: $\mathbb{E}[X_i]$
  - Standard deviation: $\mathrm{SD}(X_i)$
  - Tail quantiles: $\mathrm{VaR}_{0.99}^+(X_i)$ and Range-VaR $R_{0.01, 0.10}(X_i)$
  - Expected Shortfall: $\mathrm{ES}_{0.975}(X_i)$
- **Reference Covariance Matrix:** $\Sigma \in \mathbb{R}^{n \times n}$ estimated via shrinkage (Ledoit-Wolf) on rolling 252-day return windows.
- **Stress / Ambiguity Indicator:** Cross-sectional pairwise correlation dispersion or rolling copula distance for setting $\omega_t$ (`research-proposed`).

## Execution assumptions

- **Rebalancing Execution (`research-proposed`):** Target weights $\boldsymbol{\lambda}^*$ executed via VWAP orders over the 30-minute market close auction window.
- **Transaction Costs & Turnover (`research-proposed`):** Transaction fee modeled at 5 bps for equities / 5 bps taker for crypto per rebalance.
- **No-Shorting Constraint (`source-reported`):** Portfolio weights strictly non-negative $\boldsymbol{\lambda} \in \Delta_n = \{ \boldsymbol{\lambda} \ge 0, \sum_i \lambda_i = 1 \}$.
- **Turnover Damping (`research-proposed`):** To avoid discontinuous vertex jumping when $\kappa$ or $\omega$ crosses switching boundaries, implement a minimum turnover threshold of 2.5% before trade execution (`research-proposed`).

## Evidence

### Source-reported

All analytical theorems, numerical illustration values, switching points, and sensitivity metrics below are directly reported by Liu & Liu (`arXiv:2609.04496v1`, September 2026, Section 7, Tables 1–6 and Figures 1–2):

#### 1. Baseline Marginal Inputs for 3-Asset Numerical Illustration (Section 7, Table 2)
The assets are constructed with uncoupled Gaussian generators $Z_1, Z_2, Z_3 \sim N(0, 1)$ such that no single asset dominates in both mean loss and risk:
- **Asset 1 (High Mean, High Volatility Normal):**
  $X_1 = 4.0 + 2.6 Z_1$
  $\mathbb{E}[X_1] = 4.0000$, $\mathrm{SD}(X_1) = 2.6000$, $\mathrm{VaR}_{0.99}^+(X_1) = 10.0485$, $R_{0.01, 0.10}(X_1) = 8.1960$.
- **Asset 2 (Moderate Mean, Moderate Volatility Normal):**
  $X_2 = 4.8 + 0.9 Z_2$
  $\mathbb{E}[X_2] = 4.8000$, $\mathrm{SD}(X_2) = 0.9000$, $\mathrm{VaR}_{0.99}^+(X_2) = 6.8937$, $R_{0.01, 0.10}(X_2) = 6.2525$.
- **Asset 3 (Low Mean, Low Volatility Shifted Lognormal):**
  $X_3 = 5.3 + 0.2 \cdot \frac{\exp(Z_3) - \sqrt{e}}{\sqrt{e(e-1)}}$
  $\mathbb{E}[X_3] = 5.3000$, $\mathrm{SD}(X_3) = 0.2000$, $\mathrm{VaR}_{0.99}^+(X_3) = 6.0951$, $R_{0.01, 0.10}(X_3) = 5.6327$.

#### 2. Tail-Risk Concentration Regimes and Switching Points (Section 7.1, Table 3)
Under full copula ambiguity, the robust optimizer $\boldsymbol{\lambda}^*$ is strictly concentrated in a single vertex $\mathbf{e}_i$:
- **For $\mathrm{VaR}_{0.99}^+$:**
  - $0 \le \kappa < 0.2536$: $\boldsymbol{\lambda}^* = \mathbf{e}_1 = (1, 0, 0)$ (Asset 1 optimal)
  - $0.2536 < \kappa < 0.6261$: $\boldsymbol{\lambda}^* = \mathbf{e}_2 = (0, 1, 0)$ (Asset 2 optimal)
  - $\kappa > 0.6261$: $\boldsymbol{\lambda}^* = \mathbf{e}_3 = (0, 0, 1)$ (Asset 3 optimal)
  - Switching thresholds: $\kappa_{12} = \frac{4.8 - 4.0}{10.0485 - 6.8937} = 0.2536$; $\kappa_{23} = \frac{5.3 - 4.8}{6.8937 - 6.0951} = 0.6261$.
- **For Range-VaR $R_{0.01, 0.10}$:**
  - $0 \le \kappa < 0.4116$: $\boldsymbol{\lambda}^* = \mathbf{e}_1 = (1, 0, 0)$
  - $0.4116 < \kappa < 0.8067$: $\boldsymbol{\lambda}^* = \mathbf{e}_2 = (0, 1, 0)$
  - $\kappa > 0.8067$: $\boldsymbol{\lambda}^* = \mathbf{e}_3 = (0, 0, 1)$
  - Switching thresholds: $\kappa_{12} = \frac{4.8 - 4.0}{8.1960 - 6.2525} = 0.4116$; $\kappa_{23} = \frac{5.3 - 4.8}{6.2525 - 5.6327} = 0.8067$.

#### 3. Worst-Case Mean–SD Portfolios and Heterogeneous-Shape Diversification (Section 7.2, Table 4)
Because Asset 3 is lognormal while Assets 1 & 2 are normal, $\operatorname{Corr}(Z, \exp(Z)) = 1/\sqrt{e-1} \approx 0.7629 < 1.0$. Comonotonic covariance matrix $\Sigma_c$ has entries $\Sigma_{c, 12} = 2.34$, $\Sigma_{c, 13} = 0.3967$, $\Sigma_{c, 23} = 0.1373$.
- $\kappa = 0.00$: $\boldsymbol{\lambda}^* = (1, 0, 0)$, $V_{\mathrm{SD}} = -4.0000$
- $\kappa = 0.25$: $\boldsymbol{\lambda}^* = (1, 0, 0)$, $V_{\mathrm{SD}} = -4.6500$
- $\kappa = 0.50$: $\boldsymbol{\lambda}^* = (0, 1, 0)$, $V_{\mathrm{SD}} = -5.2500$
- $\kappa = 0.75$: $\boldsymbol{\lambda}^* = (0, 0.2035, 0.7965)$, $V_{\mathrm{SD}} = -5.4395$ (strictly diversified mixture of Assets 2 & 3)
- $\kappa = 1.00$: $\boldsymbol{\lambda}^* = (0, 0.0082, 0.9918)$, $V_{\mathrm{SD}} = -5.4999$ (slight mixture)
- $\kappa = 1.25$: $\boldsymbol{\lambda}^* = (0, 0, 1)$, $V_{\mathrm{SD}} = -5.5500$ (fully concentrated in Asset 3)

#### 4. Value of Dependence Information and Concentration Index HHI (Section 7.3, Table 5)
Comparing independent reference model $\Sigma_0 = \operatorname{diag}(6.76, 0.81, 0.04)$ against comonotonic model $\Sigma_c$:
- $\kappa = 0.50$:
  - Independent: $\boldsymbol{\lambda}_0^* = (0.3280, 0.6720, 0)$, $\mathrm{HHI}_0 = 0.5592$
  - Worst-case: $\boldsymbol{\lambda}_c^* = (0, 1, 0)$, $\mathrm{HHI}_c = 1.0000$
  - Robustness premium $\Delta(\kappa) = J_c^*(\kappa) - J_0^*(\kappa) = 0.1897$
- $\kappa = 0.75$:
  - Independent: $\boldsymbol{\lambda}_0^* = (0.2214, 0.7126, 0.0660)$, $\mathrm{HHI}_0 = 0.5612$
  - Worst-case: $\boldsymbol{\lambda}_c^* = (0, 0.2035, 0.7965)$, $\mathrm{HHI}_c = 0.6758$
  - Robustness premium $\Delta(\kappa) = 0.1372$
- $\kappa = 1.00$:
  - Independent: $\boldsymbol{\lambda}_0^* = (0.0591, 0.2120, 0.7289)$, $\mathrm{HHI}_0 = 0.5797$
  - Worst-case: $\boldsymbol{\lambda}_c^* = (0, 0.0082, 0.9918)$, $\mathrm{HHI}_c = 0.9838$
  - Robustness premium $\Delta(\kappa) = 0.0977$
- $\kappa = 1.25$:
  - Independent: $\boldsymbol{\lambda}_0^* = (0.0416, 0.1580, 0.8003)$, $\mathrm{HHI}_0 = 0.6672$
  - Worst-case: $\boldsymbol{\lambda}_c^* = (0, 0, 1)$, $\mathrm{HHI}_c = 1.0000$
  - Robustness premium $\Delta(\kappa) = 0.0832$

#### 5. Tail-Shape Sensitivity (Section 7.4, Table 6)
Varying lognormal shape parameter $\eta \in [0.20, 1.50]$ holding mean (5.3) and SD (0.2) constant:
- $\eta = 0.20$: $\mathrm{VaR}_{0.99}^+(X_3) = 5.8553, \kappa_{23}^{\mathrm{VaR}} = 0.4815$; $R_{0.01, 0.10}(X_3) = 5.6523, \kappa_{23}^{\mathrm{RVaR}} = 0.8331$.
- $\eta = 0.55$: $\mathrm{VaR}_{0.99}^+(X_3) = 6.0034, \kappa_{23}^{\mathrm{VaR}} = 0.5616$; $R_{0.01, 0.10}(X_3) = 5.6753, \kappa_{23}^{\mathrm{RVaR}} = 0.8663$.
- $\eta = 1.00$: $\mathrm{VaR}_{0.99}^+(X_3) = 6.0951, \kappa_{23}^{\mathrm{VaR}} = 0.6261$; $R_{0.01, 0.10}(X_3) = 5.6327, \kappa_{23}^{\mathrm{RVaR}} = 0.8067$.
- $\eta = 1.50$: $\mathrm{VaR}_{0.99}^+(X_3) = 5.9617, \kappa_{23}^{\mathrm{VaR}} = 0.5365$; $R_{0.01, 0.10}(X_3) = 5.5083, \kappa_{23}^{\mathrm{RVaR}} = 0.6719$.
- Switching threshold $\kappa_{12}$ remains identical ($0.2536$ for VaR, $0.4116$ for RVaR) because marginals 1 & 2 are unchanged.

#### 6. Weighted Robustness FRTB-Style Blend (Section 8)
For 3-asset Gaussian returns $\boldsymbol{\mu} = (4.9, 4.1, 5.5)^\top$, $\boldsymbol{\sigma} = (1.8, 0.2, 1.0)^\top$, $\rho_{12} = 0.30, \rho_{13} = 0.20, \rho_{23} = 0.25$:
- At $\omega = 0$ (full trust in reference joint model), the optimizer solves standard mean–ES, producing a diversified interior allocation.
- At $\omega = 1$ (full robustness), the objective collapses to $\min_i \mathrm{ES}_p(X_i)$, which concentrates 100% into Asset 2 because $\mathrm{ES}_p(X_2) = 4.1 + 0.2 c_p$ is strictly smaller than Asset 1 ($4.9 + 1.8 c_p$) and Asset 3 ($5.5 + 1.0 c_p$).

### Independently reproduced

Not independently reproduced. All analytical theorems, mathematical proofs, and numerical calibration tables represent third-party reported findings from Liu & Liu (`arXiv:2609.04496v1`).

### Negative evidence

- **Fragility of Naive Diversification in Tail Stress:** Proposition 3 mathematically proves that for identically distributed assets under complete copula uncertainty, the equal-weight portfolio $\boldsymbol{\lambda} = (1/n, \dots, 1/n)$ produces the *highest* possible worst-case risk, while the single-asset concentrated portfolio produces the *lowest*. This confirms that 1/n diversification offers zero protection against adversarial tail dependence.
- **Severe Discontinuous Turnover Under Extreme Ambiguity:** In Regime B ($\omega = 1$), a tiny change in estimated standalone asset expected return or tail quantile can cause the optimal portfolio to switch 100% of capital from one vertex to another (e.g., from Asset 1 to Asset 2 when $\kappa$ passes 0.2536), generating 200% round-trip portfolio turnover and severe transaction fee drag.
- **Suboptimal in Non-Stressed Regimes:** If market dependence is stable and well-captured by the reference covariance matrix, holding a concentrated vertex portfolio sacrifices the classical Sharpe ratio benefits of Markowitz diversification.

## Falsification plan

1. **Copula Breakdown Stress Test (`research-proposed`):**
   - Compare the realized drawdown of an equal-weight portfolio ($1/n$) versus the weighted robust portfolio ($\omega = 0.5$) and the fully robust concentrated portfolio ($\omega = 1.0$) across historical liquidity crises (e.g., March 2020 COVID crash, May 2022 Terra/Luna contagion, November 2022 FTX collapse).
   - `research-defined falsification threshold`: If the realized maximum drawdown of the weighted robust portfolio ($\omega = 0.5$) is not at least 15% lower than the equal-weight baseline during copula correlation breakdown regimes ($\bar{\rho}_{\mathrm{realized}} > 0.85$), reject the hypothesis that dependence-uncertainty optimization prevents tail contagion.
2. **Turnover & Fee Attrition Boundary (`research-proposed`):**
   - Measure net-of-cost CAGR across weekly rebalancing when transitioning between $\omega = 0$ and $\omega = 1$.
   - `research-defined falsification threshold`: If transaction costs from simplex vertex switches erase more than 40% of the gross risk-adjusted return improvement over a 3-year walk-forward test, the unconstrained vertex allocation model is falsified as an operational strategy.
3. **Marginal Distributional Heterogeneity Test (`research-proposed`):**
   - Evaluate whether mixing assets from distinct distributional families (e.g., heavy-tailed crypto returns combined with Gaussian or lognormal fixed income proxies) restores an interior diversified solution under worst-case Standard Deviation, as predicted by Theorem 5 and Example 1.
   - `research-defined falsification threshold`: If the optimal weights under empirical comonotonic covariance do not produce an interior solution ($0.05 \le \lambda_i^* \le 0.95$ for all $i$) when marginal tail indices differ significantly (Kolmogorov-Smirnov test $p < 0.01$), reject the distributional shape mitigation hypothesis.

## Crypto portability

- **Portability Status:** Adapted / Unproven (`research-proposed`).
- **Cryptocurrency-Specific Considerations:**
  - *Extreme Tail Dependence and Comonotonicity:* Crypto assets exhibit severe co-movement during market sell-offs: cross-sectional correlations between Bitcoin, Ethereum, and altcoins frequently surge from 0.40 to >0.85 during liquidation cascades. Under such conditions, standard Markowitz diversification completely fails, exactly matching the theoretical regime where Liu & Liu's "concentration paradox" applies.
  - *Location-Scale Family Violation:* In crypto, major assets (BTC, ETH) exhibit different tail exponents (Pareto $\alpha \approx 2.5–3.0$) compared to highly speculative micro-cap tokens ($\alpha < 1.8$). Under Theorem 5, this marginal shape heterogeneity can be exploited to construct non-vertex robust portfolios even under extreme dependence ambiguity.
  - *Perpetual Funding Rate Drag:* Concentrating in a single crypto asset on perpetual futures exposes the portfolio to directional funding rate bleed. The allocation model must be adapted to incorporate funding yield into the expected loss vector $\boldsymbol{\mu}$.
  - *24/7 Liquidity Fragmentation:* Crypto assets trade continuously without an official closing auction. Rebalancing must occur via TWAP/VWAP algorithms over low-volatility UTC windows (e.g., 00:00–01:00 UTC) rather than relying on closing auction mechanisms.

## Limitations

- **Complete Ambiguity Conservatism (`source-reported`):** Fully unconstrained copula ambiguity ($\omega = 1$) assumes nature selects the worst possible joint coupling (e.g., comonotonicity or sharp convolution upper bounds), which is frequently overly pessimistic during normal market functioning.
- **Discontinuous Simplex Vertex Switching (`source-reported`):** The pure worst-case optimizers in Theorems 3–5 are piece-wise constant upper envelopes of affine functions, causing discrete jumps in portfolio weights as risk aversion $\kappa$ traverses critical thresholds ($\kappa_{12}, \kappa_{23}$).
- **Parameter Sensitivity of Switching Thresholds (`research-proposed`):** Switching thresholds $\kappa_{ij} = (m_j - m_i)/(r_i^\rho - r_j^\rho)$ depend directly on small differences between marginal tail quantiles, making vertex selection vulnerable to sampling noise in sample quantile estimates.
- **Short-Selling Exclusion (`source-reported`):** The mathematical formulation strictly enforces $\boldsymbol{\lambda} \in \Delta_n$ (non-negative long-only weights); extensions to long-short portfolios require different dual representation bounds.

## Implementation status

- `not-implemented`: No optimization engine, majorization solver, or weighted robustness allocation policy has been integrated into NautilusTrader or our quantitative research repository.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- This record serves exclusively as upstream quantitative research on robust portfolio optimization and dependence uncertainty. It does not constitute investment advice and does not authorize paper, testnet, or live capital allocation.

## Related Wiki records

- `[[quant/wasserstein-robust-portfolio-hyperplane-dual-lp-2026-09-02]]` — Certified Wasserstein robust portfolio optimization using supporting hyperplanes.
- `[[quant/special-markowitz-thermodynamic-joint-regularisation-returns-covariance-2026-09-17]]` — Joint thermodynamic regularization of return and covariance matrices.
- `[[quant/evar-parity-tempered-stable-returns-risk-budgeting-2026-09-13]]` — Entropic Value-at-Risk parity and risk budgeting for tempered stable returns.
- `[[quant/separated-signal-libraries-packing-saturation-joint-spectral-limits-2026-09-17]]` — Signal library packing limits and spectral bounds under equal weighting.

## Sources

1. Peng Liu and Yang Liu, *"Portfolio Diversification and Concentration under Dependence Uncertainty: A Majorization Approach"*, arXiv preprint `arXiv:2609.04496v1 [q-fin.PM, math.PR]`, submitted September 3, 2026.
   - Canonical URL: https://arxiv.org/abs/2609.04496
   - Full-text HTML: https://arxiv.org/html/2609.04496v1
   - Full-text PDF: https://arxiv.org/pdf/2609.04496v1
   - DOI: [10.48550/arXiv.2609.04496](https://doi.org/10.48550/arXiv.2609.04496)
2. Harry Markowitz, *"Portfolio Selection"*, *The Journal of Finance*, 7(1):77–91, 1952. DOI: [10.1111/j.1540-6261.1952.tb01525.x](https://doi.org/10.1111/j.1540-6261.1952.tb01525.x).
3. Basel Committee on Banking Supervision (BCBS), *"Minimum Capital Requirements for Market Risk (FRTB)"*, Bank for International Settlements, February 2019.
4. Georg Ch. Pflug and Mathias Pohl, *"A Review on Ambiguity in Stochastic Portfolio Optimization"*, *Set-Valued and Variational Analysis*, 26(4):733–757, 2018. DOI: [10.1007/s11228-017-0466-2](https://doi.org/10.1007/s11228-017-0466-2).
5. Jose Blanchet, Henry Lam, and Yang Liu, *"Distributionally Robust Risk Aggregation and the Value-at-Risk under Dependence Uncertainty"*, Working Paper / arXiv preprint, 2025. Cited in Liu & Liu (2026).
6. Albert W. Marshall, Ingram Olkin, and Barry C. Arnold, *"Inequalities: Theory of Majorization and Its Applications"*, 2nd edition, Springer Series in Statistics, 2011. DOI: [10.1007/978-0-387-68276-1](https://doi.org/10.1007/978-0-387-68276-1).
