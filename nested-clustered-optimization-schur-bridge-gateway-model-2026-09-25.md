---
schema: strategy-research-record-v1
title: "Nested Clustered Optimization on a Schur Bridge: Gateway-Conditioned Low-Rank Cross-Cluster Coupling with Exact Out-of-Sample Interior Damping (arXiv:2609.21271)"
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - nested-clustered-optimization
  - schur-complement
  - gateway-model
  - vecchia-approximation
  - minimum-variance
  - estimation-error-damping
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - "Peter Cotton, 'Nested Clustered Optimization Is One End of a Schur Bridge, and the Interior Is Sometimes Provably Better', arXiv preprint arXiv:2609.21271v1 [q-fin.MF, math.OC, q-fin.PM], submitted September 18, 2026. DOI: 10.48550/arXiv.2609.21271. Stable URL: https://arxiv.org/abs/2609.21271. Full text HTML: https://arxiv.org/html/2609.21271v1. Full text PDF: https://arxiv.org/pdf/2609.21271v1. Ancillary verification code: https://arxiv.org/src/2609.21271v1/anc/verify_schur_nco_bridge.py"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Nested Clustered Optimization on a Schur Bridge: Gateway-Conditioned Low-Rank Cross-Cluster Coupling with Exact Out-of-Sample Interior Damping (arXiv:2609.21271)

## Provenance

- **Primary Academic Source:** Peter Cotton (Intech Investments / Microprediction), *"Nested Clustered Optimization Is One End of a Schur Bridge, and the Interior Is Sometimes Provably Better"*, arXiv preprint `arXiv:2609.21271v1 [q-fin.MF, math.OC, q-fin.PM]`, submitted **Fri, 18 Sep 2026 18:31:02 UTC**.
- **Canonical Digital Object Identifier (DOI):** [10.48550/arXiv.2609.21271](https://doi.org/10.48550/arXiv.2609.21271) (resolves HTTP 200).
- **Canonical URLs:**
  - Landing / Abstract: [https://arxiv.org/abs/2609.21271](https://arxiv.org/abs/2609.21271)
  - Full-Text HTML: [https://arxiv.org/html/2609.21271v1](https://arxiv.org/html/2609.21271v1)
  - Full-Text PDF: [https://arxiv.org/pdf/2609.21271v1](https://arxiv.org/pdf/2609.21271v1) (400,663 bytes, 23 pages)
  - Primary Ancillary Code Package: [https://arxiv.org/src/2609.21271v1/anc/verify_schur_nco_bridge.py](https://arxiv.org/src/2609.21271v1/anc/verify_schur_nco_bridge.py) (1,141 lines Python verification suite)
- **Publication / Review Status (`source-reported`):** Submitted as an arXiv working paper under the Creative Commons Attribution 4.0 International license (`CC BY 4.0`). No journal reference or publisher DOI appears on the landing page as of 2026-09-25 (`preprint only`).
- **Code Audit & Local Verification (`independently reproduced audit`):** The primary paper includes an author-provided standalone Python verification package `verify_schur_nco_bridge.py` in its arXiv ancillary files (`anc/`). This script was downloaded and executed in full on 2026-09-25 under Python 3.11 with NumPy 2.4.6; all 32 analytical assertions (Propositions 1–9, exact bivariate jets, rational error checks, degenerate partitions, and singular covariance regularizations) evaluated cleanly and returned `certificate ok`.
- **Repository Deduplication (2026-09-25):** Whole-repository ripgrep across all 962 tracked `.md` files and coverage manifests (`coverage_manifest.csv`) confirmed zero prior records containing `2609.21271`, `10.48550/arXiv.2609.21271`, `Schur Bridge`, `gateway model`, `schur-nco-bridge`, or `verify_schur_nco_bridge`. The only other record citing author Peter Cotton is `crypto-otc-order-imbalance-skew-width-symmetry-2026-09-02.md` (`arXiv:2608.07690`), which investigates structural symmetries in market maker inventory carrying costs, an unrelated market-microstructure topic.

## Economic mechanism

### Source-reported

1. **The Structural Blind Spot of Nested Clustered Optimization (NCO):** In two-tier cluster allocation (López de Prado 2020), assets are partitioned into clusters $I_1, \dots, I_k$. The inner step optimizes each cluster strictly on its own diagonal covariance block $\Sigma_{ii}$, producing normalized cluster portfolios $v_i$. The outer step optimizes across these cluster portfolios using the $k \times k$ matrix $V^\top \Sigma V$. The inner tier is completely blind to cross-cluster covariance: the only mechanism by which one cluster responds to another is its scalar budget.
2. **The Unconstrained Global Minimum-Variance Benchmark via Block Inversion:** For any partition $(I_i, -i)$ where $-i$ denotes all assets outside cluster $i$, block matrix inversion shows that the unconstrained global minimum-variance direction $\Sigma^{-1} \mathbf{1}$ satisfies:
   $$(\Sigma^{-1} \mathbf{1})_{I_i} = Q_i^{-1} b_i$$
   where $Q_i = \Sigma_{ii} - \Sigma_{i,-i} \Sigma_{-i,-i}^{-1} \Sigma_{-i,i}$ is the Schur complement of cluster $i$ against all other assets, and $b_i = \mathbf{1}_{I_i} - \Sigma_{i,-i} \Sigma_{-i,-i}^{-1} \mathbf{1}_{-i}$ is the companion constraint vector. The blocks of the global minimum-variance portfolio are generalized minimum-variance directions on their full conditional covariances. There is no outer cross-cluster optimizer in the global unconstrained solution; all cross-cluster information enters exclusively through the Schur conditioning. However, evaluating $Q_i$ directly requires inverting an $(n - |I_i|) \times (n - |I_i|)$ matrix per cluster, destroying the computational and stability advantages of clustering.
3. **The Gateway Model (Low-Rank Cross-Cluster Conditioning):** To eliminate the $(n - |I_i|)$ inversion without ignoring cross-cluster covariance, Cotton borrows the concept of "knots" from spatial statistics and Vecchia approximations. In each cluster $I_i$, one member is designated as the knot $p_i \in I_i$, with remaining members $J_i = I_i \setminus \{p_i\}$. Under the Gateway Model (Definition 1), the regression residuals of $J_i$ on $p_i$ are uncorrelated with every asset outside $I_i$. That is, all correlation between cluster $i$ and the outside world passes entirely through its knot.
4. **Sufficiency of Knots (Proposition 1):** Under the Gateway Model, conditioning cluster $i$ on the knots of all other clusters $P_{-i} = \{p_j : j \neq i\}$ is mathematically identical to conditioning on all $n - |I_i|$ external assets:
   $$Q_i = \Sigma_{ii} - \Sigma_{i, P_{-i}} \Sigma_{P_{-i}, P_{-i}}^{-1} \Sigma_{P_{-i}, i}, \quad b_i = u_{I_i} - \Sigma_{i, P_{-i}} \Sigma_{P_{-i}, P_{-i}}^{-1} u_{P_{-i}}$$
   The required linear solve collapses from dimension $(n - |I_i|)$ to $(k - 1)$.
5. **The Schur Bridge:** Introducing a damping parameter $\gamma \in [0, 1]$ into the knot-conditioned pair defines a continuous bridge:
   $$Q_i(\gamma) = \Sigma_{ii} - \gamma \Sigma_{i, P_{-i}} \Sigma_{P_{-i}, P_{-i}}^{-1} \Sigma_{P_{-i}, i}, \quad b_i(\gamma) = u_{I_i} - \gamma \Sigma_{i, P_{-i}} \Sigma_{P_{-i}, P_{-i}}^{-1} u_{P_{-i}}$$
   - At $\gamma = 0$: exact NCO (nested clustered optimization on uncoupled diagonal blocks).
   - At $\gamma = 1$: exact global unconstrained minimum-variance portfolio $\Sigma^{-1} u$ under the gateway model.
   - For $\gamma \in (0, 1)$: a regularized interior allocation balancing intra-cluster risk reduction against cross-cluster hedging.
6. **Invariance of Member Part (Proposition 4):** Under the Gateway Model, as $\gamma$ moves along the bridge, the portfolio weights assigned to the intra-cluster member residuals $d_{i, J_i} = E_i^{-1} (u_{J_i} - \beta_i u_{p_i})$ depend on neither $\gamma$ nor any other cluster. Only the knot exposures $\kappa_i(\gamma)$ move along the bridge.
7. **Provable Interior Optimality under Estimation Error (Propositions 7 & 8):** When covariance $\Sigma$ is estimated with noise $\widehat{\Sigma}_\tau = \Sigma + \tau E$, sample inversion error creates an out-of-sample penalty. Cotton proves that the optimal damping shift satisfies $\widetilde{\gamma}(\tau) = 1 - \frac{G'(1)}{V_0''(1)} \tau^2 + O(\tau^4)$. When $G'(1) > 0$, the out-of-sample optimal portfolio lies strictly in the interior $\gamma^* \in (0, 1)$, proving that neither heuristic NCO ($\gamma = 0$) nor unconstrained Markowitz ($\gamma = 1$) is optimal.

### Research interpretation

- **Falsifiable Hypothesis:** In financial asset markets with sectoral, supply-chain, or factor clustering, inter-cluster dependencies are dominated by low-rank gateway assets (e.g., sector ETF proxies, mega-cap benchmark constituents, or benchmark index leaders), while member residual correlations across clusters are small. If this gateway property holds approximately, damping the low-rank cross-cluster Schur complement by an interior parameter $\gamma \in (0, 1)$ achieves lower realized out-of-sample portfolio variance than both unconstrained Markowitz inversion (which overfits noisy cross-cluster correlations) and heuristic NCO (which discards cross-cluster hedging entirely).
- **Component Roles in the Composite System:**
  - *Clustering / Partition Layer:* Decomposes the $n$-asset universe into $k$ disjoint sub-universes ($I_1, \dots, I_k$).
  - *Gateway / Knot Identification Layer:* Identifies the representative anchor asset $p_i$ per cluster (e.g., maximum market cap or first principal component alignment).
  - *Intra-Cluster Residual Layer:* Evaluates intra-cluster betas $\beta_i$ and residual covariance $E_i$, fixing member positions $d_{i, J_i}$ invariant to external market movements.
  - *Schur Bridge Damping Layer ($\gamma$):* Regulates the degree of cross-cluster hedging based on estimation risk.
  - *Outer Portfolio Synthesis Layer:* Allocates capital across clusters via the low-dimensional $k \times k$ ridge-augmented covariance matrix.

## Signal

All mathematical relationships below are `source-reported` from Cotton (arXiv:2609.21271v1) unless labeled `research-proposed`.

### Step 1: Universe Partition and Knot Selection

- Let $\Sigma \succ 0$ be the $n \times n$ covariance matrix of $n$ assets.
- Partition assets into $k$ disjoint clusters $I_1, \dots, I_k$ such that $\bigcup_{i=1}^k I_i = \{1, \dots, n\}$ and $I_i \cap I_j = \emptyset$ for $i \neq j$.
- In each cluster $I_i$, designate one member as the knot $p_i \in I_i$, with remaining members $J_i = I_i \setminus \{p_i\}$.
- Knot set: $P = \{p_1, \dots, p_k\}$ of size $k$. For cluster $i$, other knots are $P_{-i} = P \setminus \{p_i\}$ of size $k - 1$.
- *Knot Selection Rule (`source-reported` heuristic, Remark 4):* In a latent cluster factor model $r_m = \lambda_m f_j + \eta_m$, choose the knot $p \in I_j$ that maximizes $\rho_p = \lambda_p^2 \operatorname{Var}(f_j) / \sigma_p^2$, approximated by the constituent most aligned with the cluster's first principal component.

### Step 2: Intra-Cluster Decomposition and Residuals

- For each cluster $i$, compute the regression slope of remaining members $J_i$ onto knot $p_i$:
  $$\beta_i = \frac{\Sigma_{J_i, p_i}}{\sigma_{p_i}^2}$$
- Compute the intra-cluster residual covariance matrix:
  $$E_i = \Sigma_{J_i, J_i} - \beta_i \beta_i^\top \sigma_{p_i}^2$$
- Compute the scalar cluster precision proxy:
  $$\delta_i = (\mathbf{1}_{J_i} - \beta_i)^\top E_i^{-1} (\mathbf{1}_{J_i} - \beta_i)$$
  *(Note: If every member has unit beta to its knot, $\delta_i = 0$, member weights vanish, and cluster weight concentrates entirely on the knot).*

### Step 3: Damped Knot-Conditioned Pair

For a target vector $u$ ($u = \mathbf{1}$ for minimum variance; $u = \mu$ for maximum Sharpe ratio):
- Cross-knot regression coefficients onto other knots $P_{-i}$:
  $$a_i = \Sigma_{p_i, P_{-i}} \Sigma_{P_{-i}, P_{-i}}^{-1} u_{P_{-i}}$$
  $$c_i = \Sigma_{p_i, P_{-i}} \Sigma_{P_{-i}, P_{-i}}^{-1} \Sigma_{P_{-i}, p_i}$$
- For chosen damping parameter $\gamma \in [0, 1]$, define the conditioned pair for cluster $i$:
  $$Q_i(\gamma) = \Sigma_{ii} - \gamma \Sigma_{i, P_{-i}} \Sigma_{P_{-i}, P_{-i}}^{-1} \Sigma_{P_{-i}, i}$$
  $$b_i(\gamma) = u_{I_i} - \gamma \Sigma_{i, P_{-i}} \Sigma_{P_{-i}, P_{-i}}^{-1} u_{P_{-i}}$$
- Direction vector $d_i(\gamma) = Q_i(\gamma)^{-1} b_i(\gamma)$ of length $|I_i|$.
- *Decoupled Closed Form (Proposition 4):*
  - Member part ($J_i$): $d_{i, J_i} = E_i^{-1} (u_{J_i} - \beta_i u_{p_i})$ (completely independent of $\gamma$ and external clusters).
  - Knot exposure ($\kappa_i = d_{i, p_i} + \beta_i^\top d_{i, J_i}$):
    $$\kappa_i(\gamma) = \frac{u_{p_i} - \gamma a_i}{\sigma_{p_i}^2 - \gamma c_i}$$
  - Knot weight: $d_{i, p_i}(\gamma) = \kappa_i(\gamma) - \beta_i^\top d_{i, J_i}$.

### Step 4: Outer Tier Synthesis and Portfolio Assembly

- Form the $n \times k$ block-diagonal matrix $D_\gamma$, where column $i$ contains direction $d_i(\gamma)$ supported on index set $I_i$.
- Compute the bridge portfolio (`source-reported`, unnormalized form, Eq. 9):
  $$w_\gamma \propto D_\gamma (D_\gamma^\top \Sigma D_\gamma)^{-1} D_\gamma^\top u$$
  normalized such that $\mathbf{1}^\top w_\gamma = 1$.
- *Two-Tier Representation (when all cluster totals $\mathbf{1}^\top d_i(\gamma) \neq 0$):*
  Define normalized cluster portfolios $v_i = d_i(\gamma) / (\mathbf{1}^\top d_i(\gamma))$. Then $V = [v_1, \dots, v_k]$, and the outer cluster budgets are given by:
  $$\alpha \propto (V^\top \Sigma V)^{-1} V^\top u, \quad w_\gamma = V \alpha$$
- *Outer Covariance Ridge Identity (Proposition 3):*
  $$V^\top \Sigma V = K_\gamma \Sigma_{PP} K_\gamma + \Delta$$
  where $K_\gamma = \operatorname{diag}(\kappa_1, \dots, \kappa_k)$ and $\Delta = \operatorname{diag}(v_{1, J_1}^\top E_1 v_{1, J_1}, \dots, v_{k, J_k}^\top E_k v_{k, J_k})$. The member residuals provide a strictly positive diagonal ridge that raises the smallest eigenvalue of the outer problem.

### Step 5: Regularized Effective Exposure Path for Rank-Deficient Knots (Proposition 9)

If the knot covariance $S = \Sigma_{PP} \succeq 0$ is singular with $\mathbf{1} \in \operatorname{range}(S)$:
- Compute the pseudoinverse direction $h = S^\dagger \mathbf{1}$.
- Parametrize the portfolio by effective exposure $\lambda \in [0, 1]$:
  $$\bar{\kappa}_i(\lambda) = \frac{1 - \lambda}{s_i} + \lambda h_i, \quad s_i = S_{ii}$$
- Outer matrix $\bar{K} S \bar{K} + \Delta$ is strictly positive definite, continuous in $\lambda$, yielding exact NCO at $\lambda = 0$ and true global minimum variance at $\lambda = 1$.

### Operational & Tradable Rules (`research-proposed`)

The theoretical paper assumes continuous rebalancing and known or perturbed covariance matrices. For empirical backtesting and execution, the following rules are `research-proposed`:
- *Rebalancing Cadence:* Rebalance daily or weekly at the official market close (`research-proposed`).
- *Rolling Estimation Window:* Trailing $T = 252$ trading days of daily return observations (`research-proposed`).
- *Covariance Estimator:* Empirical covariance regularized via Ledoit-Wolf constant-correlation shrinkage (`research-proposed`).
- *Clustering Algorithm:* Hierarchical agglomerative clustering using Ward's minimum-variance criterion on the correlation distance matrix $D_{ij} = \sqrt{2(1 - \rho_{ij})}$, setting cluster count $k = \max(2, \lfloor \sqrt{n} \rfloor)$ (`research-proposed`).
- *Default Damping Choice:* In the absence of calibrated noise variance, set default $\gamma = 0.5$ (`research-proposed`).

## Required data

- **Universe / Instruments:** Cross-section of $n$ liquid tradable assets (e.g., S&P 500 equities, liquid US equity sector ETFs, or high-liquidity crypto perpetual contracts).
- **Timeframe / Data Fields:** Daily (or higher-frequency bar) OHLCV series. Adjusted closing prices for equity dividends/splits; mark prices for crypto perpetuals.
- **Covariance Inputs:** Historical rolling returns $r_{i, t} = \ln(P_{i, t} / P_{i, t-1})$. Minimum sample length $T > n$ for full-rank empirical covariance, or $T > k$ when shrinkage / Gateway Model conditioning is deployed.
- **Cluster Metadata:** Static sectoral classifications (e.g., GICS sectors/industries) or dynamic point-in-time correlation clusters updated at rebalance boundaries.
- **Missing Data Handling (`research-proposed`):** Strict point-in-time synchronization. Assets with trading halts or missing bars must be forward-filled or dropped from the active universe prior to covariance estimation; pairwise non-synchronized covariance estimation is strictly prohibited to prevent non-positive semidefinite matrices.

## Execution assumptions

- **Source Assumptions (`source-reported`):**
  - Fully invested, unconstrained long-short weights ($\sum_i w_i = 1$; negative weights permitted).
  - Frictionless execution: zero commissions, zero bid-ask spread, zero market impact, zero borrow costs.
  - Zero latency: portfolio rebalancing is instantaneous at the observation timestamp.
- **Operational Reality & Research Assumptions (`research-proposed`):**
  - Order type: Market-on-Close (MOC) or passive limit orders executed at VWAP over a 15-minute closing auction window.
  - Transaction cost model: 5 bps per side for liquid US equities / ETFs; 10 bps taker fee / slippage for crypto perpetual contracts.
  - Short borrowing: For equities, annual stock borrow fee assumed at 50 bps baseline; for crypto perpetuals, continuous funding rate payments applied to net directional exposure.
  - Leverage / Margin: Portfolio gross leverage capped at $\sum_i |w_i| \le 2.0$ (`research-proposed`).

## Evidence

### Source-reported

All mathematical proofs, analytical derivatives, and exact numerical figures below are directly transcribed from Cotton (arXiv:2609.21271v1, Sections 3–9 and companion verification code):

1. **Analytical Exactness Theorems:**
   - *Proposition 1 (Sufficiency of Knots):* Under the gateway condition $R_j(p_j) = 0$, conditioning cluster $i$ on other knots $P_{-i}$ matches conditioning on all $n - |I_i|$ assets to machine precision (verified numerically with error $< 1.21 \times 10^{-13}$).
   - *Proposition 2 (Bridge Endpoints):* At $\gamma = 0$, $w_0$ exactly equals NCO (error $< 4.45 \times 10^{-16}$). At $\gamma = 1$, stacked directions $d_1$ equal the unconstrained minimum-variance direction $\Sigma^{-1} \mathbf{1}$ (error $< 1.77 \times 10^{-12}$).
   - *Proposition 3 (Outer Covariance Ridge):* $V^\top \Sigma V = K \Sigma_{PP} K + \Delta$ verified to within $5.69 \times 10^{-14}$.
   - *Proposition 4 (Invariance of Member Directions):* $d_{i, J_i}$ across all $\gamma \in [0, 1]$ varies by $< 5.23 \times 10^{-13}$.
2. **Exact Numerical Examples of Interior Optimality:**
   - *Symmetric Identical Clusters with Two-Point Noise ($Z \in \{0, 2c\}$):*
     Formula for optimal damping: $\gamma^* = \frac{1 + (k-1)c}{1 + 2(k-1)c}$.
     For $k = 2$, $c = 1/4$, and member precision $\delta = 1$:
     - Unique global optimum: $\gamma^* = 2/3 \approx 0.6667$.
     - Out-of-sample variance improvements:
       $$F(0) - F(2/3) = \frac{1}{576} \approx 0.001736$$
       $$F(1) - F(2/3) = \frac{1}{900} \approx 0.001111$$
       Both NCO ($\gamma = 0$) and full unconstrained Markowitz ($\gamma = 1$) are provably inferior to the interior bridge.
   - *Ten-Cluster Model ($k = 10, c = 1/4$):*
     Curvature ratio: $G'(1) / V_0''(1) = \frac{8 - \delta}{1 + 13\delta/4}$.
     - Critical member threshold: $\delta = 8$.
     - When $\delta < 8$ (e.g., $\delta = 4$): $G'(1) > 0$, shift is $-2/7$, optimum is strictly interior.
     - When $\delta > 8$ (e.g., $\delta = 12$): $G'(1) < 0$, shift is $+1/10$, constrained optimum stays at $\gamma^* = 1$ under small noise.
     - However, under larger noise $\tau = 1/4$ ($Z \in \{0, 1/2\}$), the same $\delta = 12$ model shifts to an interior optimum $\gamma^* = 10/11 \approx 0.9091$.
   - *Quartic Asymmetric Example (2 clusters, $\Sigma_{33}=4, \Sigma_{13}=1/2, Z \in \{0, 1\}$):*
     Population variance derivative sign governed by quartic $P(x) = 49x^4 + 84x^3 - 21x^2 + 48x - 6$.
     - Unique optimum: $\gamma^* \approx 0.5587$.
     - Exact variance gaps: $F(0) - F(1/2) = 3/1210 \approx 0.002479$; $F(1) - F(1/2) = 5/1452 \approx 0.003444$.
     - Under small symmetric noise $Z = 1/2 \pm \tau$: $G'(1) = \frac{31779128936}{554523204167} > 0$, $V_0''(1) = \frac{48136}{3571279}$, predicting $\widetilde{\gamma}(0.05) \approx 0.9894$ (against numerical optimum $0.9896$).
   - *Three-Cluster Asymmetric Model with Full Coupling Local Optimality:*
     $V_0''(1) \approx 2.3949$, $G'(1) \approx -0.0585 < 0$, proving that full coupling $\gamma^* = 1$ is a strict local minimizer for all small $\tau$. Spot checks at $\tau = 1/10$ and $\tau = 1/100$ confirm $F(\gamma, \tau) > F(1, \tau)$ for $\gamma \in \{0.999, 0.99, 0.9, 0.5, 0\}$.
   - *Duplicated Knots / Singular Covariance:*
     - Standard bridge variance at $\gamma < 1$: $3/8 = 0.375$.
     - Local pseudoinverse at $\gamma = 1$: $1/2 = 0.500$.
     - True global unconstrained minimum variance: $1/3 \approx 0.3333$ (weights $[1/6, 1/3, 1/6, 1/3]$).
     - Proposition 9 effective exposure bridge $\bar{\kappa}_i(\lambda) = \frac{1-\lambda}{s_i} + \lambda h_i$ smoothly bridges variance from $3/8$ down to $1/3$.
3. **Computational Complexity:**
   - No $n \times n$ matrix inversion is ever formed.
   - Maximum linear solve dimension is $\max(k, \max_i |I_i|)$, identical to standard NCO.
   - Additional operations over NCO: $k \times (k-1)$ cross-knot products and a single $(k-1) \times (k-1)$ solve per cluster (computable via rank-1 downdates of $\Sigma_{PP}^{-1}$).

### Independently reproduced

- `Not independently reproduced` on empirical market backtests. The cited preprint is a mathematical and theoretical portfolio-construction treatise; it contains no empirical equity, commodity, or crypto backtest.
- The author's companion computational script `verify_schur_nco_bridge.py` was directly downloaded and executed on 2026-09-25 using Python 3.11 with NumPy 2.4.6. All analytical assertions, rational error bounds, and exact bivariate jets passed with zero failures (`certificate ok`).

### Negative evidence

1. **Violation of the Gateway Assumption:** When member residuals across clusters are correlated ($R_j(p_j) \neq 0$), the sufficiency of knots fails. The knot-conditioned Schur complement only approximates the true full conditional covariance, leaving an omitted risk correction $\Delta_i = \Sigma_{i,-i} \Sigma_{-i,-i}^{-1} \Sigma_{-i,i} - \Sigma_{i, P_{-i}} \Sigma_{P_{-i}, P_{-i}}^{-1} \Sigma_{P_{-i}, i} \succ 0$.
2. **Failure under Portfolio Constraints:** The exact equivalence between the stacked directions and the global optimum holds *only* for unconstrained, fully invested long-short portfolios. Under long-only constraints ($w_i \ge 0$), cardinality limits, or box bounds, no block decomposition is exact.
3. **Zero Cluster Total Divergence:** When a cluster direction sums to zero ($\mathbf{1}^\top d_i(\gamma) = 0$), normalized cluster portfolios $v_i = d_i / (\mathbf{1}^\top d_i)$ explode. The unnormalized formulation $w_\gamma \propto D_\gamma (D_\gamma^\top \Sigma D_\gamma)^{-1} D_\gamma^\top u$ must be used to avoid division by zero.
4. **Lack of Empirical Market Verification:** The paper explicitly acknowledges in Section 10 that empirical validation across historical market regimes is left to future work. Whether real financial correlation matrices satisfy the gateway model closely enough to yield economic alpha after trading costs is unproven.

## Falsification plan

To test whether the Schur Bridge provides demonstrable alpha or risk-reduction edge over standard baselines, the following 10 operational tests are pre-declared:

- **F1 (Empirical Gateway Residual Test):** On rolling 252-day windows across S&P 500 equities, evaluate the norm of the cross-cluster residual matrix $\|R_j(p_j)\|_F / \|\Sigma_{I_j, -j}\|_F$.
  - *Research-defined falsification threshold:* If the relative residual norm exceeds $0.35$ on more than $20\%$ of rolling windows, reject the Gateway Model as an accurate physical description of asset covariance.
- **F2 (Out-of-Sample Realized Variance Horse Race):** Compare out-of-sample realized portfolio variance of Schur Bridge ($\gamma = 0.5$) against standard NCO ($\gamma = 0$), sample Markowitz ($\gamma = 1$), Ledoit-Wolf shrinkage, and $1/N$ equal-weighting across a 10-year rolling backtest.
  - *Research-defined falsification threshold:* Reject the Schur Bridge hypothesis if its realized out-of-sample variance is not statistically lower than both NCO and sample Markowitz at the $5\%$ significance level ($p < 0.05$ via Ledoit-Wolf variance bootstrap).
- **F3 (Transaction Cost & Turnover Stress):** Evaluate net Sharpe ratio and net cumulative return under realistic execution costs (5 bps for US equities; 10 bps for crypto perps) across daily and weekly rebalancing.
  - *Research-defined falsification threshold:* If net Sharpe drops below zero or turnover exceeds $25\%$ per rebalance, reject practical implementability.
- **F4 (Damping Parameter Sensitivity):** Sweep $\gamma \in [0, 1]$ in steps of $0.05$.
  - *Research-defined falsification threshold:* If the realized out-of-sample variance profile is monotonically increasing or decreasing across all regimes (showing no interior local minimum across rolling windows), reject the interior optimality hypothesis.
- **F5 (Knot Selection Perturbation):** Compare knot selection by 1st principal component alignment vs. market cap weighting vs. random cluster member selection.
  - *Research-defined falsification threshold:* If random knot selection produces equivalent or superior variance to PC1 knot selection, reject the factor-alignment knot selection theory.
- **F6 (Clustering Robustness):** Compare GICS industry classification against $k$-means and hierarchical agglomerative tree clustering.
  - *Research-defined falsification threshold:* If clustering method changes realized variance by more than $30\%$ or renders the outer matrix singular, flag clustering instability.
- **F7 (Market Crash / Correlation Spike Regime):** Evaluate performance during extreme market drawdown periods (e.g., 2008 GFC, March 2020 COVID crash) when cross-asset correlations spike toward 1.
  - *Research-defined falsification threshold:* If realized drawdown exceeds unconstrained Markowitz by more than $200$ bps, reject risk-mitigation properties in high-correlation regimes.
- **F8 (Long-Only Projected Heuristic):** Project the Schur Bridge weights onto the simplex ($w_i \ge 0, \sum_i w_i = 1$) via quadratic programming.
  - *Research-defined falsification threshold:* If the projected long-only Schur portfolio fails to outperform long-only NCO or Hierarchical Risk Parity (HRP), conclude that the bridge's advantages are strictly confined to unconstrained long-short trading.
- **F9 (Singular Covariance Stress):** Test on universes where $n > T$ (e.g., $n = 500$ stocks, $T = 60$ days).
  - *Research-defined falsification threshold:* If Proposition 9 effective exposure regularizer ($\lambda$) produces ill-conditioned weights with condition number $> 10^6$, reject singular robustness claims.
- **F10 (Cross-Asset Portability Test):** Run identical pipeline across US Equities, Global Liquid Commodity Futures, and Top-20 Crypto Perpetuals.
  - *Research-defined falsification threshold:* If the strategy fails to produce positive information ratio relative to $1/N$ across at least 2 of the 3 asset classes, reject cross-asset universality.

## Crypto portability

- **Portability Classification:** `adapted / unproven` (`research interpretation`).
- **Rationale for Classification:** The primary paper is an analytical mathematics and statistical mechanics paper with zero crypto market empirical testing. Porting the Gateway Schur Bridge to crypto assets is a novel research adaptation with significant unverified structural hurdles:
  - *Absence of Natural Knots:* In equities, mega-cap balance sheets and sector ETFs act as natural gateway knots. In crypto, Bitcoin (`BTC`) dominates market-wide correlation, but altcoin sectors (Layer-1, Layer-2, DeFi, Memes) exhibit turbulent, non-stationary cross-token linkages that may severely violate the Gateway Model residual condition.
  - *Perpetual Funding Rate Drag:* Unconstrained long-short weights require holding short positions in volatile altcoins, incurring substantial negative funding rate carry during bull regimes or positive funding during crashes, which is not modeled by pure covariance minimization.
  - *24/7 Continuous Trading & Timestamp Alignment:* Unlike equity daily closes with synchronized auction prices, crypto markets trade continuously across fragmented exchanges (Binance, Bybit, OKX, DEXes), creating stale pricing and asynchronous covariance distortion.
  - *Liquidation Clusters & Extreme Fat Tails:* Crypto asset returns exhibit severe non-Gaussian jump dynamics, heavy tails, and endogenous liquidation cascades, which can distort quadratic risk measures and undermine linear regression residual assumptions.

## Limitations

1. **Theoretical and Empirical Gap:** `unproven` in live trading and `not independently reproduced` on historical market datasets.
2. **Gateway Model Dependence:** The mathematical optimality strictly requires that member residuals have zero cross-cluster correlation. In real-world multi-asset universes, cross-industry supply chains and multi-factor exposures routinely violate this assumption.
3. **Unconstrained Long-Short Requirement:** The closed-form decoupling of member weights and knot exposures holds strictly for unconstrained portfolios. Imposing long-only constraints ($w_i \ge 0$) breaks the analytic bridge.
4. **Underspecified Operational Parameters:** Rebalancing cadence, estimation lookback window, covariance shrinkage target, and transaction cost budget are completely absent from the source paper and must be supplied by the researcher (`research-proposed`).
5. **Turnover and Cost Sensitivity:** Moving toward $\gamma = 1$ increases sensitivity to sample noise, which can generate high portfolio turnover and excessive trading fees that rapidly overwhelm variance reduction gains.

## Implementation status

- `not-implemented`.
- No prototype, backtest, or production card has been executed in Qlib, PyBroker, NautilusTrader, or live execution engines.
- This record serves strictly as a normalized research-only capture of an external mathematical portfolio-optimization theory.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- A strategy record being present in this repository does **not** mean:
  - Passed Research Intake Review;
  - Entered Hermes Wiki Brain;
  - Entered the production candidate pool (`/results/_handoff/candidates.json`);
  - Completed Qlib full-backtest validation;
  - Became a frozen survivor or leaderboard entry;
  - Approved for paper trading, testnet, or live trading.

## Related Wiki records

- `[[quant/portfolio-covariance-and-shrinkage-2026-08-28]]` — Foundation review of covariance estimation error, Ledoit-Wolf shrinkage, and sample noise in portfolio optimization.
- `[[quant/volatility-targeting-risk-parity-constrained-2026-08-28]]` — Constrained risk budgeting and heuristic clustering allocation methods (HRP, NCO).
- `[[quant/phase9-factor-covariance-redundancy-risk-decomposition-2026-08-28]]` — Factor covariance modeling, low-rank approximations, and residual risk decomposition.
- `[[quant/crypto-otc-order-imbalance-skew-width-symmetry-2026-09-02]]` — Prior research record by the same primary author (Peter Cotton, arXiv:2608.07690).
- `[[quant/path-portfolio-optimization-signature-defect-lift-2026-09-02]]` — Path signature regularization and non-Euclidean portfolio optimization.

## Sources

1. Peter Cotton. *"Nested Clustered Optimization Is One End of a Schur Bridge, and the Interior Is Sometimes Provably Better."* arXiv preprint `arXiv:2609.21271v1 [q-fin.MF, math.OC, q-fin.PM]`, submitted September 18, 2026.
   - Abstract URL: [https://arxiv.org/abs/2609.21271](https://arxiv.org/abs/2609.21271)
   - Full-text HTML: [https://arxiv.org/html/2609.21271v1](https://arxiv.org/html/2609.21271v1)
   - Full-text PDF: [https://arxiv.org/pdf/2609.21271v1](https://arxiv.org/pdf/2609.21271v1)
   - Canonical DOI: [10.48550/arXiv.2609.21271](https://doi.org/10.48550/arXiv.2609.21271)
   - Ancillary Python Verification Code: [https://arxiv.org/src/2609.21271v1/anc/verify_schur_nco_bridge.py](https://arxiv.org/src/2609.21271v1/anc/verify_schur_nco_bridge.py)
2. Marcos López de Prado. *Machine Learning for Asset Managers*. Cambridge University Press, 2020. (Cited by Cotton as the canonical definition of Nested Clustered Optimization).
3. Peter Cotton. *"Schur complementary allocation: a unification of hierarchical risk parity and minimum variance portfolios."* arXiv preprint `arXiv:2411.05807`, 2024.
4. Anthony V. Vecchia. *"Estimation and model identification for continuous spatial processes."* Journal of the Royal Statistical Society: Series B 50(2): 297–312, 1988.
