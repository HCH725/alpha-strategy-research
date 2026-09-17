---
schema: strategy-research-record-v1
title: "Special Markowitz: Thermodynamic Formalism for the Joint Regularisation of Returns and Covariance"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - markowitz
  - thermodynamic-formalism
  - joint-shrinkage
  - spectral-regularisation
  - stein-loss
  - random-matrix-theory
status: research-only
confidence: high
source_as_of: 2026-09-17
sources:
  - "David Reinhardt, 'Special Markowitz: Thermodynamic Formalism for the Joint Regularisation of Returns and Covariance', arXiv:2609.14029v2 [q-fin.ST], September 15, 2026. https://arxiv.org/abs/2609.14029"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Special Markowitz: Thermodynamic Formalism for the Joint Regularisation of Returns and Covariance

## Provenance

- **Primary Academic Source:** David Reinhardt (studio entropica, Schäftlarn/Isartal, Germany, `dr.david.reinhardt@entropica.studio`), *"Special Markowitz: Thermodynamic Formalism for the Joint Regularisation of Returns and Covariance"*, arXiv preprint `arXiv:2609.14029v2 [q-fin.ST]`, submitted September 12, 2026, revised September 15, 2026.
- **Canonical arXiv URL:** https://arxiv.org/abs/2609.14029
- **Canonical Full-Text HTML:** https://arxiv.org/html/2609.14029v2
- **Canonical Full-Text PDF:** https://arxiv.org/pdf/2609.14029v2
- **DOI:** [10.48550/arXiv.2609.14029](https://doi.org/10.48550/arXiv.2609.14029)
- **Licence:** Creative Commons Attribution Non-Commercial No Derivatives 4.0 International (CC BY-NC-ND 4.0).
- **Direct Primary-Source Verification:** The complete preprint full text (Sections 1–14, Definitions 3.1–9.1, Propositions 4.3–13.1, Theorem 7.1, Remarks 2.1–14.1, References [1]–[9]) was read and mathematically verified. All characterization results, first-order conditions, Hessian evaluations, thermodynamic pressure formulas, conjugacy relationships, and asymptotic random matrix theory calibrations cited herein trace directly to `arXiv:2609.14029v2`.
- **Repository Deduplication Audit:** Pre-write search across all 683 records in `alpha-strategy-research` confirmed zero prior citations of `arXiv:2609.14029`, David Reinhardt's portfolio research, or the "Special Markowitz" thermodynamic variational architecture. Existing shrinkage and portfolio optimization records in the repository (`evar-parity-tempered-stable-returns-risk-budgeting-2026-09-13.md`, `two-stage-adaptive-shrinkage-golden-criterion-equity-premium-2026-09-02.md`, `wasserstein-robust-portfolio-hyperplane-dual-lp-2026-09-02.md`, `smart-predict-then-optimize-spo-plus-robust-portfolio-2026-09-05.md`) focus on Entropic Value-at-Risk parity under tempered stable distributions, two-stage shrinkage for univariate equity premium predictors, or distributionally robust linear programs under Wasserstein balls; none establish the joint thermodynamic variational principle for returns and covariance, the characterization of the Stein loss from scale-invariant coupling, the modal Gibbs weight persistence equality, or the spectral ridge formulation.

## Economic mechanism

### Source-reported

In quantitative portfolio allocation, Markowitz mean-variance optimization requires two empirical inputs: an estimated expected return vector $\hat{\mu} \in \mathbb{R}^n$ and an estimated covariance matrix $\hat{\Sigma} \in \mathrm{Pos}(n)$. Standard empirical estimates suffer from severe estimation noise, which Markowitz optimization inverts and amplifies into extreme, unstable, and uninvestable portfolio weights.

Historically, quantitative finance has addressed this problem in a fragmented, uncoupled manner:
1. **Covariance-Only Shrinkage:** Linear shrinkage (Ledoit & Wolf 2004) or analytical non-linear shrinkage (Ledoit & Wolf 2020) shrinks the sample covariance matrix toward an identity or factor target, but leaves the expected return vector $\hat{\mu}$ unregularized.
2. **Return-Only Shrinkage:** Black-Litterman (1992) or Bayes-Stein estimators shrink expected returns toward an equilibrium or grand mean, but typically take the covariance matrix as given or shrink it independently under an unrelated heuristic.

Reinhardt (`arXiv:2609.14029v2`) introduces **Special Markowitz (SM)**, solving the joint regularisation of returns and covariance from a unified thermodynamic variational principle relative to a reference prior state $(\mu_{\mathrm{ref}}, \Sigma_{\mathrm{ref}})$:
- **Relative Spectral Geometry:** The problem is formulated on the whitened relative operator $A = \Sigma_{\mathrm{ref}}^{-1/2} \hat{\Sigma} \Sigma_{\mathrm{ref}}^{-1/2} = U \Lambda U^\top$ (Definition 3.1). The orthogonal eigenvectors $\{u_k\}$ define the natural coordinate basis, and the eigenvalues $\lambda_k > 0$ measure empirical variance deviations relative to the reference state.
- **Spectral Reliability Potential Field:** Each eigenmode $k$ carries an information persistence $\psi_k \in (0, 1]$, representing the estimated fraction of its empirical data signal that is statistically reliable. Its natural additive coordinate is the spectral reliability potential $\Phi_k = -\ln \psi_k \in [0, \infty)$ (Definition 4.1), with corresponding exponential Gibbs weight $\psi_k = e^{-\Phi_k}$ and reference coupling strength $s_k = e^{\Phi_k} - 1 \ge 0$.
- **Uniqueness of Logarithmic Potential (Proposition 4.3):** Multiplicative composition of independent reliability filters ($\psi_{A \circ B} = \psi_A \psi_B$) and additive potential coordinates ($\Phi_{AB} = \Phi_A + \Phi_B$) uniquely characterizes $\Phi = -c \ln \psi$ ($c > 0$) as the only continuous homomorphism from $((0, 1], \times)$ to $([0, \infty), +)$ vanishing at full reliability.
- **Uniqueness of Stein Loss (Proposition 5.4):** Imposing scale-invariant reliability coupling (Principle 5.1) and common persistence (Principle 5.2) within the class of additively separable smooth divergences uniquely forces the covariance loss to be the **Stein divergence** (relative entropy of Gaussian covariance matrices):
  $$D_{\mathrm{Stein}}(\sigma, \lambda) = \frac{\sigma}{\lambda} - \ln \frac{\sigma}{\lambda} - 1$$
  The linear ratio $\sigma/\lambda$ measures variance displacement while the logarithmic term $-\ln(\sigma/\lambda)$ provides an entropic barrier preventing eigenvalue collapse.
- **The Coupling Identity (Theorem 7.1):** Minimizing the separable modal free energy functional $F = \sum_k F_k$ on the spectral submanifold contracts both return deviations and covariance deviations toward the reference by the **exact same Gibbs weight** $e^{-\Phi_k}$:
  $$m_k^* = e^{-\Phi_k} \delta_k, \quad \sigma_k^* - 1 = e^{-\Phi_k} (\lambda_k - 1)$$
  Reliable modes ($\Phi_k \approx 0 \implies \psi_k \approx 1$) preserve empirical signal and risk; unreliable modes ($\Phi_k \gg 1 \implies \psi_k \to 0$) relax completely to the reference state $(\mu_{\mathrm{ref}}, \Sigma_{\mathrm{ref}})$.
- **Relative Markowitz Solution (Proposition 11.1):** In whitened coordinates, optimal portfolio weights decompose into:
  $$w_k^{\mathrm{SM}} = \frac{m_k^*}{\sigma_k^*} = \frac{\delta_k}{\lambda_k + e^{\Phi_k} - 1} = \frac{\delta_k}{\lambda_k + s_k}$$
  This simultaneously resolves into: (i) a **spectral ridge** with mode-dependent ridge $s_k = e^{\Phi_k} - 1$; (ii) a **reliability gate** $w_k^{\mathrm{SM}} = R_k w_k^{\mathrm{Markowitz}}$ with attenuation factor $R_k = \frac{\lambda_k}{\lambda_k + s_k} \in [0, 1]$; and (iii) **joint shrinkage** where a single parameter governs both return and risk.

### Research interpretation

Special Markowitz replaces arbitrary, uncoordinated tuning of alpha signals and risk models with a mathematically rigorous, thermodynamically grounded framework:
- **Elimination of Alpha-Risk Mismatch:** In traditional multi-asset quantitative trading, researchers frequently fit predictive return models (cross-sectional momentum, mean-reversion, factor forecasts) and independently estimate a high-dimensional covariance matrix (e.g. sample covariance with Ledoit-Wolf shrinkage). Because return forecasts along low-variance sample eigenvectors are inherently noisy, inverting an independently regularized covariance matrix over-allocates capital to statistically spurious return fluctuations. Special Markowitz enforces that if an eigenmode is statistically noisy (high $\Phi_k$), its return forecast is shrunk by the exact same proportion as its covariance deviation, completely shutting down spurious leverage along ill-conditioned directions.
- **Representation of Modern Spectral Filtering:** As shown in Section 13.1, Agnostic Risk Parity (ARP; Benichou et al. 2017) corresponds to an SM spectral potential $\Phi_k^{\mathrm{ARP}} = \ln(1 + \sqrt{\lambda_k}/c - \lambda_k)$, while Marchenko-Pastur bulk truncation corresponds to setting $\Phi_k = \infty$ for eigenvalues inside the noise bulk $[\lambda_-, \lambda_+]$ and $\Phi_k = -\ln \rho_k^2$ for supercritical spikes exceeding the Baik-Ben Arous-Péché (BBP) threshold $\theta_{\mathrm{crit}} = \sqrt{n/T_{\mathrm{obs}}}$.
- **Decoupled Thermodynamic Architecture:** The additivity of the SM pressure functional $P_{\mathrm{SM}}(\Phi) = \sum_k P_k(\Phi_k)$ and the vanishing of cross-susceptibilities $\frac{\partial^2 P}{\partial \Phi_j \partial \Phi_k} = 0$ ($j \ne k$) prove that under stable eigenbases, portfolio optimization is cleanly separable into independent single-mode scalar subproblems.

## Signal

The normalized quantitative specification defines the complete end-to-end data transformation, relative operator spectral decomposition, reliability potential assignment, regularized equilibrium state calculation, and portfolio weight generation:

### 1. Mathematical Definitions & Input States (`source-reported`)

- **Universe Dimension:** $n$ assets.
- **Reference State (`source-reported`):** Prior distribution $\mathcal{N}(\mu_{\mathrm{ref}}, \Sigma_{\mathrm{ref}})$, where $\Sigma_{\mathrm{ref}} \in \mathrm{Pos}(n)$ is symmetric positive-definite, and $\mu_{\mathrm{ref}} \in \mathbb{R}^n$.
  - In equity/crypto cross-sections, typical reference benchmarks are the market-cap weighted index return / diagonal sample variance matrix, or an empirical factor model benchmark (`research-proposed`).
- **Empirical State (`source-reported`):** Sample mean return $\hat{\mu} \in \mathbb{R}^n$ and sample covariance $\hat{\Sigma} \in \mathrm{Pos}(n)$ estimated over an observation window of length $T_{\mathrm{obs}}$.
- **Whitened Relative Operator (`source-reported`):**
  $$A = \Sigma_{\mathrm{ref}}^{-1/2} \hat{\Sigma} \Sigma_{\mathrm{ref}}^{-1/2} \in \mathrm{Pos}(n)$$
  Since $A$ is symmetric and positive-definite, compute its exact eigendecomposition:
  $$A = U \Lambda U^\top, \quad \Lambda = \mathrm{diag}(\lambda_1, \lambda_2, \dots, \lambda_n), \quad \lambda_k > 0, \quad U^\top U = I_n$$
- **Whitened Return Difference (`source-reported`):**
  $$\delta\mu_w = \Sigma_{\mathrm{ref}}^{-1/2} (\hat{\mu} - \mu_{\mathrm{ref}}) \in \mathbb{R}^n$$
  Project onto the eigenbasis $\{u_k\}$:
  $$\delta_k = u_k^\top \delta\mu_w = u_k^\top \Sigma_{\mathrm{ref}}^{-1/2} (\hat{\mu} - \mu_{\mathrm{ref}}), \quad k = 1, \dots, n$$

### 2. Spectral Reliability Potential Calibration (`source-reported` & `research-proposed`)

Each eigenmode $k \in \{1, \dots, n\}$ is assigned an information persistence $\psi_k \in (0, 1]$ and potential $\Phi_k = -\ln \psi_k \in [0, \infty)$:

1. **Random Matrix Theory (RMT) Spiked Covariance Calibration (`source-reported`):**
   - Concentration ratio: $\gamma = n / T_{\mathrm{obs}}$.
   - Marchenko-Pastur noise bulk boundaries:
     $$\lambda_- = (1 - \sqrt{\gamma})^2, \quad \lambda_+ = (1 + \sqrt{\gamma})^2$$
   - Baik-Ben Arous-Péché (BBP) critical spike threshold: $\theta_{\mathrm{crit}} = \sqrt{\gamma}$.
   - **Noise Bulk Modes ($\lambda_k \le \lambda_+$):**
     The sample eigenvector is asymptotically orthogonal to the true population eigenvector.
     $$\psi_k \to 0 \implies \Phi_k \to \infty \quad (\text{practically } \Phi_k \ge 10.0, \, s_k \ge 22000) \quad (\text{source-reported})$$
   - **Supercritical Spike Modes ($\lambda_k > \lambda_+$):**
     Estimated population spike strength $\hat{\theta}_k = \frac{\lambda_k + 1 - \gamma + \sqrt{(\lambda_k + 1 - \gamma)^2 - 4\lambda_k}}{2} - 1$ (`research-proposed`).
     Asymptotic sample-to-population eigenvector squared overlap (Benaych-Georges & Nadakuditi 2011; `source-reported`):
     $$\rho_k^2 = \frac{1 - \gamma / \hat{\theta}_k^2}{1 + \gamma / \hat{\theta}_k} \in (0, 1]$$
     Assign information persistence and potential:
     $$\psi_k = \rho_k^2, \quad \Phi_k = -\ln \rho_k^2 \quad (\text{source-reported})$$

2. **Alternative Calibration: Agnostic Risk Parity Representation (`source-reported`):**
   - For a conservative spectral damping with constant $c \le 1 / \sqrt{\lambda_{\max}}$:
     $$\Phi_k^{\mathrm{ARP}} = \ln \left( 1 + \frac{\sqrt{\lambda_k}}{c} - \lambda_k \right)$$

3. **Alternative Calibration: Bootstrap Resampling Stability (`research-proposed`):**
   - Compute the empirical eigenvector stability across $B = 200$ stationary block-bootstraps of the returns:
     $$\psi_k = \max\left( \varepsilon_{\min}, \, \frac{1}{B} \sum_{b=1}^B |u_k^\top u_k^{(b)}| \right), \quad \Phi_k = -\ln \psi_k$$

### 3. Regularized Equilibrium State Computation (`source-reported`)

Given the potential field $(\Phi_1, \dots, \Phi_n)$:
- **Gibbs Weights:** $\psi_k = e^{-\Phi_k} \in (0, 1]$.
- **Reference Coupling Strength:** $s_k = e^{\Phi_k} - 1 \ge 0$.
- **Regularized Whitened Return Deviations:**
  $$m_k^* = e^{-\Phi_k} \delta_k = \psi_k \delta_k$$
- **Regularized Whitened Eigenvalues:**
  $$\sigma_k^* = e^{-\Phi_k} \lambda_k + (1 - e^{-\Phi_k}) \cdot 1 = 1 + \psi_k (\lambda_k - 1)$$
- **Regularized Physical Return Vector:**
  $$\mu^* = \mu_{\mathrm{ref}} + \Sigma_{\mathrm{ref}}^{1/2} U m^* = \mu_{\mathrm{ref}} + \Sigma_{\mathrm{ref}}^{1/2} \sum_{k=1}^n e^{-\Phi_k} \delta_k u_k$$
- **Regularized Physical Covariance Matrix:**
  $$\Sigma^* = \Sigma_{\mathrm{ref}}^{1/2} U \mathrm{diag}(\sigma_1^*, \dots, \sigma_n^*) U^\top \Sigma_{\mathrm{ref}}^{1/2}$$

### 4. Portfolio Weight Allocation (`source-reported` & `research-proposed`)

- **Whitened Relative Markowitz Weights (`source-reported`):**
  $$w_k^{\mathrm{SM}} = \frac{m_k^*}{\sigma_k^*} = \frac{\delta_k}{\lambda_k + e^{\Phi_k} - 1} = \frac{\delta_k}{\lambda_k + s_k} = R_k \left( \frac{\delta_k}{\lambda_k} \right)$$
  where the reliability gate $R_k = \frac{\lambda_k}{\lambda_k + s_k} = \frac{\psi_k \lambda_k}{1 + \psi_k (\lambda_k - 1)} \in [0, 1]$.
- **Unconstrained Asset-Space Portfolio Weight Vector (`source-reported`):**
  Transform back from whitened coordinates to physical asset weights:
  $$w^* = \Sigma_{\mathrm{ref}}^{-1/2} U w^{\mathrm{SM}} = \Sigma_{\mathrm{ref}}^{-1/2} \sum_{k=1}^n \frac{\delta_k}{\lambda_k + e^{\Phi_k} - 1} u_k$$
- **Portfolio Normalization & Leverage Constraints (`research-proposed`):**
  - Gross leverage constraint: $L_{\max} = 1.0$ (fully invested long-only or dollar-neutral long-short).
  - For long-short dollar-neutral allocation:
    $$w_i^{\mathrm{final}} = \frac{w_i^* - \bar{w}^*}{\sum_{j=1}^n |w_j^* - \bar{w}^*|}, \quad \text{where } \bar{w}^* = \frac{1}{n} \sum_{j=1}^n w_j^*$$
  - Single-name position cap: $|w_i^{\mathrm{final}}| \le 0.10$ (10% gross allocation limit; `research-proposed`).
  - Portfolio rebalance interval: monthly (or weekly for high-volatility universes; `research-proposed`).

## Required data

- **Universe:** Cross-section of $n$ liquid tradable instruments (e.g. top 50/100 US equities by market capitalization, or top 20–30 liquid cryptocurrency perpetual contracts).
- **Timeframe / Sampling:** Daily close prices (or 8-hour / 1-hour candles for crypto); observation estimation window $T_{\mathrm{obs}} \ge 250$ trading days (ensuring $T_{\mathrm{obs}} > n$ so sample covariance $\hat{\Sigma}$ is full rank).
- **Fields:** Adjusted close prices, volume, and market capitalization (if market-cap weighting is chosen for the reference state).
- **Data Quality & Alignment:** Point-in-time cross-sectional returns; zero forward-looking bias in returns calculation ($r_t = (P_t - P_{t-1}) / P_{t-1}$); no survivor-biased universes.
- **Reference State Inputs (`research-proposed`):**
  - Prior return $\mu_{\mathrm{ref}} = 0$ (uninformed / neutral drift assumption) or historical trailing cross-sectional mean.
  - Prior covariance $\Sigma_{\mathrm{ref}} = \mathrm{diag}(\hat{\sigma}_1^2, \dots, \hat{\sigma}_n^2)$ (diagonal variance benchmark) or equal-correlation target $\Sigma_{\mathrm{ref}} = \bar{\rho} \hat{\sigma} \hat{\sigma}^\top + (1 - \bar{\rho}) \mathrm{diag}(\hat{\sigma}^2)$.

## Execution assumptions

- **Execution Timing (`research-proposed`):** Signal formed at bar close $T$; orders executed at next bar open $T+1$ (avoiding same-bar execution leakage).
- **Order Types (`research-proposed`):** TWAP market orders or peg-to-mid limit orders over a 30-minute execution window following rebalance.
- **Transaction Costs & Slippage (`research-proposed`):** 5 bps per side for large-cap US equities; 7 bps taker fee + 3 bps slippage (10 bps one-way) for crypto perpetuals.
- **Turnover & Rebalancing Buffer (`research-proposed`):** To prevent excessive trading on minor weight changes, execute rebalancing trades only if $\sum_{i=1}^n |w_{i,t}^{\mathrm{final}} - w_{i,t-1}^{\mathrm{current}}| > 0.05$ (5% portfolio turnover threshold).

## Evidence

### Source-reported

- **Theoretical Proofs & Algebraic Equivalences:** The primary source (`arXiv:2609.14029v2`) provides complete, rigorous mathematical proofs of all foundational theorems:
  - Unique characterization of the logarithmic coordinate $\Phi = -\ln \psi$ via Cauchy's functional equation under multiplicative filter composition (Proposition 4.3).
  - Unique characterization of the Stein loss $D_{\mathrm{Stein}}(\sigma, \lambda) = \sigma/\lambda - \ln(\sigma/\lambda) - 1$ as the only divergence compatible with scale-invariant linear deviation shrinkage (Proposition 5.4).
  - Exact Coupling Identity establishing identical Gibbs-weight attenuation $e^{-\Phi_k}$ across return and covariance deviations (Theorem 7.1).
  - Closed-form expression for the modal pressure functional $P_k(\Phi_k) = -F_k^*(\Phi_k)$, its strict monotonicity ($P_k' < 0$), strict convexity ($\chi_k = P_k'' > 0$), and real-analyticity on $[0, \infty)$ (Proposition 8.4).
  - Decoupling of modal cross-susceptibilities $\frac{\partial^2 P}{\partial \Phi_j \partial \Phi_k} = 0$ ($j \ne k$) (Proposition 8.6).
  - Exact recovery of Agnostic Risk Parity as a specialized potential $\Phi_k^{\mathrm{ARP}} = \ln(1 + \sqrt{\lambda_k}/c - \lambda_k)$ (Section 13.1).
- **Empirical Market Data Disclaimer:** The source explicitly notes: *"No market-data empirical results are presented"* (theoretical and foundational mathematical paper establishing the thermodynamic variational architecture).

### Independently reproduced

- `not independently reproduced`.

### Negative evidence

- **Sensitivity to Eigenvector Instability (General Markowitz Breakdown):** As noted in Remarks 8.7 and 14.1 of the paper, the exact separability and additive pressure of Special Markowitz depend strictly on the stability of the empirical eigenbasis $\{u_k\}$ of the whitened operator $A$. In regimes of heavy-tailed, non-Gaussian returns, structural breaks, or rapid correlation drift, eigenvectors rotate significantly out-of-sample. When eigenvectors are unstable, cross-modal interactions $J_{jk} V_{jk}$ arise, breaking the additive pressure functional ($\frac{\partial^2 P}{\partial \Phi_j \partial \Phi_k} \ne 0$) and causing modal misalignment.
- **Reference State Misspecification:** If the chosen reference prior $(\mu_{\mathrm{ref}}, \Sigma_{\mathrm{ref}})$ is poorly calibrated (e.g. assuming zero correlation when true correlations are strongly positive), shrinking unreliable modes toward an invalid reference can degrade out-of-sample Sharpe ratios compared to uniform $1/n$ weighting.

## Falsification plan

To disconfirm the validity and empirical utility of Special Markowitz joint regularization, execute the following controlled tests:

1. **Benchmark Comparison Against Decoupled Shrinkage:**
   - **Baseline 1:** Sample Markowitz (unregularized sample mean and covariance).
   - **Baseline 2:** Ledoit-Wolf non-linear covariance shrinkage + unregularized sample return.
   - **Baseline 3:** Ledoit-Wolf non-linear covariance shrinkage + Black-Litterman / Bayes-Stein return shrinkage.
   - **Baseline 4:** $1/n$ Equal-Weight benchmark.
   - **Failure Criterion (`research-defined falsification threshold`):** If Special Markowitz (with RMT BBP spike calibration) fails to achieve a statistically significant higher out-of-sample Sharpe ratio ($p < 0.05$ under Ledoit-Wolf 2008 bootstrap test) or fails to reduce realized out-of-sample portfolio volatility compared to Baseline 2 over a 5-year rolling evaluation window, the hypothesis that joint thermodynamic regularization outperforms decoupled shrinkage is falsified.

2. **Ablation of Joint Coupling (Testing the Coupling Identity):**
   - Construct an uncoupled variant where covariance is shrunk using Gibbs weight $\psi_k^{\mathrm{cov}} = e^{-\Phi_k}$, but return deviations are shrunk using an independent parameter $\psi_k^{\mathrm{ret}} = e^{-\theta_k}$ with $\theta_k \ne \Phi_k$.
   - **Failure Criterion (`research-defined falsification threshold`):** If uncoupled optimization systematically and robustly outperforms the joint Coupling Identity ($\theta_k = \Phi_k$) across multiple asset classes, the core modeling principle of Common Persistence (Principle 5.2) is rejected.

3. **Transaction Cost & Turnover Stress:**
   - Evaluate realized net Sharpe across varying one-way transaction cost tiers: 0 bps, 5 bps, 10 bps, 20 bps, and 30 bps.
   - **Failure Criterion (`research-defined falsification threshold`):** If net excess returns over $1/n$ become negative at transaction costs $\le 10$ bps due to excessive eigenvector turnover during monthly rebalancing, the operational tradability of SM is falsified.

## Crypto portability

- **Classification:** `adapted` / `unproven` (research interpretation; primary source investigates general mathematical portfolio theory with classical equity/multivariate Gaussian reference models, and does not demonstrate empirical performance on cryptocurrency assets).
- **Crypto-Specific Market Structure Considerations:**
  1. **High Volatility & Short Lookback Windows:** In crypto markets, asset cross-correlations shift rapidly across bull/bear regimes. A rolling estimation window $T_{\mathrm{obs}} = 250$ days may average across distinct structural regimes. Using 4-hour or 8-hour candles with $T_{\mathrm{obs}} = 300$ bars (50–100 days) may be required to maintain point-in-time relevance (`research-proposed`).
  2. **Perpetual Funding Rates as a Drift Component:** In cryptocurrency perpetual contracts, funding rate payments ($f_t$) act as an explicit carrying cost or yield. The reference return $\mu_{\mathrm{ref}}$ must incorporate expected 8-hour funding rates: $\mu_{\mathrm{ref}, i} = -f_i$ (`research-proposed`).
  3. **Heavy Tails & Non-Gaussian Shocks:** Crypto returns exhibit extreme kurtosis and jump clustering, which challenges the Gaussian relative entropy derivation of the Stein loss. The risk of eigenvector rotation between rebalance periods is significantly elevated.
  4. **Liquidity Fragmentation & Execution Slippage:** Crypto perpetual liquidity is concentrated in BTC and ETH. Expanding the universe beyond the top 20 tokens introduces wide spreads and severe market impact, making the low-volatility eigenmodes difficult to trade in physical asset space.

## Limitations

- **No Empirical Backtest in Source:** The primary paper is a foundational mathematical and theoretical contribution; it does not provide historical backtest statistics (CAGR, Sharpe, max drawdown) on empirical price series. All quantitative implementations and trading backtests remain unproven hypotheses.
- **Gaussian Loss Assumption:** The characterization of the Stein loss relies on Gaussian relative entropy geometry. In asset classes with heavy tails, jump diffusion, or asymmetric skewness, the Stein loss may under-penalize extreme joint tail risk.
- **Assumption of Eigenbasis Stability:** The theory operates on the spectral submanifold $\mathcal{M}_A$, assuming that the eigenvectors $\{u_k\}$ of the whitened operator $A$ diagonalize the true population structure. If sample eigenvectors deviate drastically from population directions, modal filtering cannot fully compensate for basis rotation error.

## Implementation status

- `not-implemented`: This record represents an external research capture and theoretical normalization. No code or strategy pipeline has been implemented in PyBroker, NautilusTrader, paper trading, testnet, or live environments.

## Adoption boundary

- `research-only`: This record is captured for theoretical analysis, research intake, and systematic hypothesis testing within Loop A (Hermes Research Loop).
- `not-approved`: Not approved for implementation, backtesting promotion, paper trading, testnet verification, or live capital allocation.

## Related Wiki records

- Pre-write inspection across `alpha-strategy-research` identified the following related records:
  - `separated-signal-libraries-packing-saturation-joint-spectral-limits-2026-09-17.md` (Spectral decomposition, spherical packing, and principal component limits in cross-sectional factor ensembles)
  - `evar-parity-tempered-stable-returns-risk-budgeting-2026-09-13.md` (Entropic Value-at-Risk parity under non-Gaussian return distributions)
  - `two-stage-adaptive-shrinkage-golden-criterion-equity-premium-2026-09-02.md` (Adaptive shrinkage parameter tuning in predictive return modeling)
  - `wasserstein-robust-portfolio-hyperplane-dual-lp-2026-09-02.md` (Distributionally robust portfolio optimization under Wasserstein ambiguity sets)
  - `smart-predict-then-optimize-spo-plus-robust-portfolio-2026-09-05.md` (Decision-focused surrogate losses for portfolio optimization)

## Sources

- David Reinhardt, *"Special Markowitz: Thermodynamic Formalism for the Joint Regularisation of Returns and Covariance"*, arXiv preprint `arXiv:2609.14029v2 [q-fin.ST]`, September 15, 2026. Stable URL: https://arxiv.org/abs/2609.14029. Full text HTML: https://arxiv.org/html/2609.14029v2. DOI: https://doi.org/10.48550/arXiv.2609.14029.
- J. Baik, G. Ben Arous, S. Péché, *"Phase transition of the largest eigenvalue"*, Annals of Probability 33(5), 1643–1697 (2005). DOI: https://doi.org/10.1214/009117905000000233.
- F. Benaych-Georges, R. R. Nadakuditi, *"The eigenvalues and eigenvectors of finite, low rank perturbations of large random matrices"*, Advances in Mathematics 227(1), 494–521 (2011). DOI: https://doi.org/10.1016/j.aim.2011.01.019.
- R. Benichou, Y. Lempérière, E. Sérié, J. Kockelkoren, P. Seager, J.-P. Bouchaud, M. Potters, *"Agnostic Risk Parity: Taming Known and Unknown-Unknowns"*, Journal of Investment Strategies 6(3), 1–12 (2017). arXiv:1610.08818. DOI: https://doi.org/10.21314/JOIS.2017.078.
- O. Ledoit, M. Wolf, *"A well-conditioned estimator for large-dimensional covariance matrices"*, Journal of Multivariate Analysis 88(2), 365–411 (2004). DOI: https://doi.org/10.1016/S0047-259X(03)00096-4.
- O. Ledoit, M. Wolf, *"Analytical nonlinear shrinkage of large-dimensional covariance matrices"*, Annals of Statistics 48(5), 3043–3065 (2020). DOI: https://doi.org/10.1214/19-AOS1921.
- D. Ruelle, *"Thermodynamic Formalism: The Mathematical Structures of Equilibrium Statistical Mechanics"*, 2nd ed., Cambridge University Press (2004).
