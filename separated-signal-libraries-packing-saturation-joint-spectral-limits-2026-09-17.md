---
schema: strategy-research-record-v1
title: "Separated Signal Libraries: Packing, Saturation, and Joint Spectral Limits in Cross-Sectional Alpha Ensembles"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - signal-libraries
  - spherical-codes
  - packing-saturation
  - principal-component-analysis
  - equal-weight-ensembles
  - false-discovery
  - factor-investing
status: research-only
confidence: high
source_as_of: 2026-09-17
sources:
  - "Marc Nunes, 'Separated Signal Libraries: Packing, Saturation, and Joint Spectral Limits', arXiv:2609.17609v1 [q-fin.ST], September 16, 2026. https://arxiv.org/abs/2609.17609"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Separated Signal Libraries: Packing, Saturation, and Joint Spectral Limits in Cross-Sectional Alpha Ensembles

## Provenance

- **Primary Source:** Marc Nunes (AlphaNova, `marc.nunes@alphanova.tech`), *"Separated Signal Libraries: Packing, Saturation, and Joint Spectral Limits"*, arXiv preprint `arXiv:2609.17609v1 [q-fin.ST]`, Version 7, submitted September 16, 2026.
- **Canonical Identifier / Stable URL:** https://arxiv.org/abs/2609.17609
- **Canonical DOI:** [10.48550/arXiv.2609.17609](https://doi.org/10.48550/arXiv.2609.17609)
- **Full-Text HTML Source:** https://arxiv.org/html/2609.17609v1
- **Full-Text PDF Source:** https://arxiv.org/pdf/2609.17609v1
- **Reference Implementation / Codebase & Ancillary Artifacts:** The paper includes an official arXiv ancillary bundle (`anc/`) reproducing all numerical packing counts, moment formulas, finite codes, margin spectra, exact quadrature, finite-history gap checks, tilted convolution with grid refinement, fixed-margin corrections, central-limit regime simulations, and datewise unit-signal perturbations.
- **Source Verification:** The primary preprint full-text HTML, formal mathematical proofs (Propositions 3.1, 3.2, 4.1, 5.3; Theorems 3.3, 3.4, 5.2, 6.1, 8.1, 8.2; Corollary 3.5; Proposition 3.6; Lemma 7.1; Remark 8.3; Appendix A–C proofs), Tables 1–4, and exact equations were directly inspected. All numerical estimates, kissing number bounds (Ho 2026; Leijenhorst & de Laat 2024; Cohn & Li 2024), Gilbert bound rates, Bahadur–Ranga Rao prefactors, and empirical test bounds cited herein trace directly to `arXiv:2609.17609v1`.
- **Repository Deduplication Audit:** Pre-write search across all records in `alpha-strategy-research` confirmed zero existing records citing `arXiv:2609.17609`, Marc Nunes, `Separated Signal Libraries`, or spherical packing / residual spectrum alignment. Existing factor-mining and alpha-selection records in the repository (`factorengine-program-level-knowledge-infused-factor-mining-2026-09-05.md`, `goant-quality-diversity-multi-agent-microstructure-alpha-discovery-2026-09-12.md`, `vst-verifiable-structured-transport-agentic-alpha-discovery-2026-09-12.md`) investigate genetic/LLM factor generation routines under heuristic correlation filters; none establish the geometric packing limits on product-sphere manifolds, the three-level spectrum under positive information coefficient (IC) margins, or the mathematical possibility of exact orthogonality between an equally weighted ensemble (EWS) and the leading principal component (PC1).

## Economic mechanism

### Source-reported

In quantitative asset management and multi-factor alpha research, practitioners frequently construct large libraries containing hundreds or thousands of cross-sectional forecasting signals (e.g., formulaic alphas, technical features, alternative data signals) across $d$ assets over $T$ trading dates. To prevent redundancy and collinearity, researchers commonly impose a **diversity constraint**—specifically, a pairwise correlation cap (minimum angular separation $\theta > 0$, such as $c_{ij} \le 0.5 \iff \theta \ge 60^\circ$)—before admitting signals into an equally weighted forecasting ensemble (Equally Weighted Sum, EWS).

Nunes (`arXiv:2609.17609v1`) provides a rigorous geometric and spectral analysis of this practice, proving that **a diversity/separation constraint alone guarantees neither ensemble convergence to a stable alpha factor nor alignment with the leading principal component (PC1)**:

1. **Geometry of Signal Histories as a Spherical Packing Problem:**
   - At each date $t$, a demeaned ($\mathbf{1}^\top S_{i,t} = 0$) and unit-normalized signal across $d$ assets is a point on a sphere $\mathbb{S}(H) \simeq \mathbb{S}^{q-1}$ of dimension $q = d - 1 \ge 2$.
   - A normalized $T$-date signal history $x_i = T^{-1/2}(S_{i,1}, \dots, S_{i,T})$ lies on the Riemannian product manifold $\mathcal{M}_{q,T} = \prod_{t=1}^T \mathbb{S}^{q-1} \subset \mathbb{S}^{qT-1}$, with intrinsic dimension $(q-1)T$ embedded in ambient dimension $D = qT$.
   - A pairwise history correlation cap $c_{ij} = \langle x_i, x_j \rangle \le \cos \theta$ is mathematically equivalent to a minimum angular separation $\vartheta_{ij} \ge \theta$ on $\mathcal{M}_{q,T}$. Growing an alpha library under a correlation cap is therefore an exact **spherical code packing problem**.

2. **Failure of Separation and Saturation Alone (Theorem 5.2 & Example 5.1):**
   - Separation alone does not select a limiting probability distribution; points can remain clustered on arbitrary submanifolds.
   - Saturated libraries (where no new signal can be admitted without violating the correlation cap) cover the domain in Hausdorff distance but can carry permanent regional sampling bias (Example 5.1 demonstrates a saturated circle code with persistent non-zero mean and degenerate eigenspace).
   - By the Borodachov–Hardin–Saff best-packing asymptotic (Theorem 5.2), near-maximum cardinality packing on an unrestricted sphere forces convergence to uniform surface volume, producing a **zero limiting ensemble mean ($\mu \to 0$) and an isotropic second moment ($M \to I_D / D$) with zero leading eigengap**.

3. **The Role of Positive Average IC and Margins (Theorems 3.3 & 3.4):**
   - Screening candidates for positive average information coefficient ($\bar{p}_i = \langle x_i, n_T \rangle > 0$, where $n_T = T^{-1/2}(e, \dots, e)$ is the normalized target return history) restricts admission to a hemisphere $E_{+,T}$ of the product manifold.
   - **Isotropic Second Moment under Pure Positivity (Theorem 3.3):** Under uniform candidate volume conditioned on $\bar{p}_i > 0$, the ensemble mean is nonzero and target-aligned ($\mu_+ = a_{q,T} n_T$ with $a_{q,T} \sim \sqrt{2 / (\pi q T)}$), but the uncentered second moment $M_+$ is **strictly isotropic** ($M_+ = I_{qT} / (qT)$)! In centered covariance $\Sigma_+ = M_+ - \mu_+ \otimes \mu_+$, the return target $n_T$ becomes the unique *smallest* eigendirection.
   - **Three-Level Spectrum under a Positive IC Margin (Theorem 3.4):** Imposing a strict positive IC margin $\beta > 0$ ($\bar{p}_i \ge \beta$) breaks this isotropy and makes the return target $n_T$ the **unique leading principal component (PC1)** at *every finite history length* $T \ge 1$. The spectrum of $M$ partitions into exactly three invariant levels:
     - Target level: $\lambda_0 = u_{\beta,T} = \mathbb{E}_\beta[c^2]$ (multiplicity 1).
     - Longitudinal contrast level: $\lambda_L = (A_{\beta,T} - C) / T$ (multiplicity $T - 1$).
     - Transverse level: $\lambda_\perp = (1 - A_{\beta,T}) / [T(q-1)]$ (multiplicity $T(q-1)$).
   - As $T \to \infty$ with fixed $\beta > 0$, $\lambda_0 \to \beta^2$, while both residual levels decay as $O(1/T)$ (Corollary 3.5).

4. **Coexistence of Separation, Exponential Capacity, and Orthogonal Disagreement (Theorems 8.1 & 8.2):**
   - Using Gilbert–Varshamov coding arguments, Nunes constructs two exponentially large, $\theta$-separated signal libraries:
     - **Aligned Library (Theorem 8.1):** EWS is the unique history PC1 if and only if $\rho > 1 / (N + 1)$, where $N = (q-1)T$.
     - **Orthogonal Library (Theorem 8.2):** An exponentially large library of signals where *every single signal* has positive IC ($\text{IC} = \sqrt{0.1} \approx 0.316 > 0$) and pairwise correlation $c_{ij} \le 0.5$ ($\theta \ge 60^\circ$), yet the unique leading principal component PC1 is **completely orthogonal to EWS** ($\langle \mu, v_1(M) \rangle = 0$). A transverse systematic factor reinforces the second moment while canceling in the linear average, causing standard PCA factor extraction to miss the alpha signal entirely!

### Research interpretation

This paper delivers a foundational econometric and geometric foundation for quantitative alpha library construction:
- **Falsification of Heuristic Correlation Pruning:** In systematic quantitative research, it is widespread folklore that greedily selecting alpha factors with pairwise correlation $< 0.5$ automatically produces an uncorrelated, diverse, and well-behaved ensemble. Nunes proves mathematically that greedy correlation pruning without an explicit residual spectrum gauge can easily converge to an ensemble whose leading statistical risk factor is completely orthogonal to the alpha thesis.
- **The Necessity of an IC Margin over Pure Positivity:** Requiring candidate factors to merely have positive backtest Sharpe / IC ($\bar{p}_i > 0$) is insufficient to induce a dominant alpha direction in the factor covariance matrix. An explicit, statistically certified margin $\beta > \epsilon_{\text{IC}}$ is required; otherwise, the factor covariance remains isotropic and indistinguishable from white noise.
- **The Residual Gauge Criterion for Alpha Deployment:** Rather than assuming that an ensemble of separated signals aligns with PC1, a quantitative system must compute the finite-sample residual gauge condition:
  $$\rho = \|\mu\|^2 > \eta = \|\Sigma\|_{\text{op}}$$
  Alignment is mathematically guaranteed if and only if the mean signal energy $\rho$ strictly exceeds the largest transverse residual component $\eta$.
- **Sample Complexity of Library Certification:** When screening $J$ candidate alpha factors over $T$ historical dates, union bounds dictate that sample correlation estimation error scales as $\epsilon_{J,T} = \sqrt{2 \log(J(J-1)/\alpha) / T}$. To ensure that observed factor independence is genuine rather than an artifact of sampling noise, the sample size must satisfy $\log J = o(T)$. If a factor-mining engine generates $J = 10^5$ factors over only $T = 500$ daily bars, false independence is guaranteed and the observed separation is illusory.

## Signal

The normalized research protocol defines the operational criteria for signal library admission, spectral certification, and ensemble construction:

### 1. State Variables & Geometric Normalization (`source-reported`)
- **Cross-Sectional Neutralization:** At each date $t \in \{1, \dots, T\}$, raw candidate signal vector $s_{i,t} \in \mathbb{R}^d$ across $d$ assets is demeaned and normalized to the unit sphere $\mathbb{S}^{q-1}$ ($q = d - 1 \ge 2$):
  $$S_{i,t} = \frac{s_{i,t} - \bar{s}_{i,t} \mathbf{1}}{\|s_{i,t} - \bar{s}_{i,t} \mathbf{1}\|_2}, \quad \text{where } \bar{s}_{i,t} = \frac{1}{d} \mathbf{1}^\top s_{i,t}$$
- **Normalized History Vector:** The full history across $T$ dates is normalized to unit length on $\mathcal{M}_{q,T} \subset \mathbb{S}^{qT-1}$:
  $$x_i = \frac{1}{\sqrt{T}} \left(S_{i,1}^\top, S_{i,2}^\top, \dots, S_{i,T}^\top\right)^\top \in \mathbb{R}^{qT}, \quad \|x_i\|_2 = 1$$
- **Pairwise History Correlation & Angular Separation:**
  $$c_{ij} = \langle x_i, x_j \rangle = \frac{1}{T} \sum_{t=1}^T \langle S_{i,t}, S_{j,t} \rangle = \cos \vartheta_{ij}$$
  Separation constraint: $c_{ij} \le \cos \theta$ for all $i \ne j$ (`source-reported`).

### 2. Admission & Filtering Logic (`source-reported` vs `research-proposed`)
- **Evaluation Sample Size Check (`source-reported`):**
  Given a candidate pool of size $J$ evaluated over $T$ dates, compute the simultaneous correlation confidence bound at significance $\alpha = 0.05$:
  $$\epsilon_{J,T} = \sqrt{\frac{2}{T} \log \frac{J(J-1)}{\alpha}}$$
  `research-proposed`: Candidate pool size $J$ and evaluation history $T$ must satisfy $\epsilon_{J,T} < 0.10$; otherwise reject candidate screening for insufficient historical sample depth.
- **Average IC Margin Screen (`source-reported`):**
  For each candidate $i$, calculate empirical average information coefficient against target return $Q_t$:
  $$\hat{\bar{p}}_i = \frac{1}{T} \sum_{t=1}^T \langle S_{i,t}, Q_t \rangle$$
  With uniform IC estimation allowance $\epsilon_{\text{IC}} = \sqrt{2 \log(2J/\alpha) / T}$, admit candidate $i$ only if:
  $$\hat{\bar{p}}_i \ge \beta + \epsilon_{\text{IC}}$$
  `research-proposed`: Set target IC margin $\beta = 0.03$ (matching the empirical benchmark of Table 3 in Nunes 2026).
- **Greedy Pairwise Separation Rule (`source-reported`):**
  Maintain admitted set $\mathcal{C} = \{x_1, \dots, x_K\}$. For candidate $x_{k+1}$ passing the IC margin screen, admit if and only if:
  $$\max_{x_j \in \mathcal{C}} \hat{c}_{j, k+1} \le \cos \theta - \epsilon_{J,T}$$
  where $\theta = 60^\circ \implies \cos \theta = 0.50$ (`source-reported`).

### 3. Spectral Certification & Ensemble Weighting (`source-reported`)
- **Ensemble Moments:** For the admitted library $\mathcal{C}$ with $K$ signals:
  - Mean vector (unscaled EWS): $\mu = \frac{1}{K} \sum_{i=1}^K x_i$, with mean energy $\rho = \|\mu\|_2^2 = \frac{1}{K} + \frac{K-1}{K} \bar{c}$.
  - Uncentered second moment: $M = \frac{1}{K} \sum_{i=1}^K x_i \otimes x_i$.
  - Centered covariance: $\Sigma = M - \mu \otimes \mu$, with operator norm $\eta = \|\Sigma\|_{\text{op}} = \lambda_{\max}(\Sigma)$.
- **Spectral Alignment Certification Gate (Theorem 6.1) (`source-reported`):**
  Check the spectral condition:
  $$\rho > \eta \iff \|\mu\|_2^2 > \|\Sigma\|_{\text{op}}$$
  If $\rho > \eta$, the leading eigenvalue $\lambda_1(M)$ is simple with eigengap $\ge \rho - \eta$, and the angular alignment between EWS $\mu$ and leading principal component $v_1(M)$ satisfies:
  $$\tan \angle(\mu, v_1(M)) \le \frac{\eta}{\rho - \eta}$$
  `research-defined falsification threshold`: If $\rho \le \eta$, flag the library as **spectrally misaligned / dominated by transverse risk factors**; freeze ensemble execution and do not deploy EWS.
- **Ensemble Trade Generation (`research-proposed`):**
  At each active date $t$, if the library passes the spectral certification gate, compute the cross-sectional forecast vector:
  $$\hat{w}_t = \frac{1}{K} \sum_{i=1}^K S_{i,t}$$
  Allocate portfolio capital proportional to $\hat{w}_t$, subject to cross-sectional zero-dollar neutrality ($\mathbf{1}^\top \hat{w}_t = 0$) and unit leverage ($\|\hat{w}_t\|_1 = 1$).

## Required data

- **Universe:** Cross-sectional asset universe of $d \ge 3$ instruments (Nunes analyzes $d = 20 \implies q = 19$ as the motivating institutional asset universe).
- **Timeframe:** Daily trading bars (close-to-close evaluation) over sample history $T \ge 60$ to $T = 1,000$ dates (`source-reported`).
- **Data Fields:**
  - Asset close prices $P_{j,t}$ for calculating forward 1-period cross-sectional return vector $R_t \in \mathbb{R}^d$.
  - Demeaned, unit-normalized return target $Q_t = (R_t - \bar{R}_t \mathbf{1}) / \|R_t - \bar{R}_t \mathbf{1}\|_2 \in \mathbb{S}^{q-1}$.
  - Raw candidate signal values $s_{i,j,t}$ across all candidates $i \in \{1, \dots, J\}$ and assets $j \in \{1, \dots, d\}$.
- **Point-in-Time Integrity:**
  - Candidate signal observations $S_{i,t}$ must be formed strictly prior to the execution timestamp of date $t$.
  - Forward return target $Q_t$ covers the holding interval $(t, t+1]$.
  - The correlation evaluation window $[1, T]$ must precede any out-of-sample portfolio deployment.
- **Missing Data Handling:** Assets with missing price observations at date $t$ must be pruned from the cross-section for that date, reducing dimension $d_t$; signals must be renormed on the available neutral subspace $H_t$. Imputation of missing signals is forbidden.

## Execution assumptions

- **Execution Timing (`research-proposed`):** Rebalancing occurs at the open of date $t+1$ based on signal $\hat{w}_t$ computed at the close of date $t$.
- **Order Types & Fill Model (`research-proposed`):** Market orders executed at the volume-weighted open price, assuming full fillability within liquidity limits.
- **Transaction Costs (`research-proposed`):** Modeled at 5 bps per unit turnover for liquid equities / major crypto assets, plus 2 bps estimated slippage.
- **Portfolio Sizing & Constraints (`research-proposed`):** Dollar-neutral long/short portfolio, with long exposure on $\hat{w}_{j,t} > 0$ and short exposure on $\hat{w}_{j,t} < 0$, normalized to gross leverage 1.0.

## Evidence

### Source-reported

Nunes (`arXiv:2609.17609v1`) provides formal mathematical theorems and extensive numerical quadrature/simulation evidence:
1. **Single-Date Sphere Capacity (19 Dimensions / 20 Assets):**
   - For $d = 20 \implies q = 19$, the single-date packing problem on $\mathbb{S}^{18}$ at $\theta = 60^\circ$ corresponds to the kissing number in dimension 19.
   - Ho (2026, arXiv:2603.10425v2) provides constructive lower bound $\mathsf{P}_{\mathbb{S}^{18}}(\pi/3) \ge 11,948$.
   - Leijenhorst & de Laat (2024) report semidefinite programming numerical upper bound $24,417.472$ (integer ceiling 24,417). Cohn & Li (2024, arXiv:2411.04916v3) confirm bounds $[11,948, 24,417]$.
2. **Gilbert Bound on Product-Manifold History Capacity (Table 4):**
   - At $\theta = 60^\circ$ across 20 assets ($q = 19$):
     - For $T = 100$ ($D = 1,900$), the Gilbert lower bound on distinct separated histories is $\log_{10} \mathsf{P} \ge 109.9182$ ($\approx 8.28 \times 10^{109}$).
     - For $T = 1,000$ ($D = 19,000$), the lower bound is $\log_{10} \mathsf{P} \ge 1081.8841$ ($\approx 7.66 \times 10^{1081}$).
     - Leading exponential rate is $1 - \mathsf{H}_2(0.25) \approx 0.18872$ bits per coordinate.
3. **Uniform Margin Screen over 20 Assets ($q = 19, \beta = 0.03$) (Table 3):**
   - $T = 1$: Admission probability = $0.4500$, ratio $\lambda_0 / \lambda_\perp = 1.117$, spectral gap = $0.00613$.
   - $T = 2$: Admission probability = $0.4280$, ratio $\lambda_0 / \max(\lambda_L, \lambda_\perp) = 1.171$, spectral gap = $0.00449$.
   - $T = 10$: Admission probability = $0.3401$, ratio = $1.447$, spectral gap = $0.00235$.
   - $T = 60$: Admission probability = $0.1556$, ratio = $2.557$, spectral gap = $0.00136$.
   - $T = 100$: Admission probability = $0.0955$, ratio = $3.326$, spectral gap = $0.00122$.
   - $T = 1,000$: Admission probability = $1.77 \times 10^{-5}$, ratio = $19.022$, spectral gap = $0.000948$.
4. **Bahadur–Ranga Rao Tail Rarity:**
   - For $q = 19, \beta = 0.10, T = 100$, refined numerical convolution gives admission probability $6.29 \times 10^{-6}$. Normal approximation gives $6.54 \times 10^{-6}$. Pure exponential term $e^{-T q \beta^2 / 2}$ gives $7.49 \times 10^{-5}$ (overstating admission probability by an order of magnitude).
5. **Proposition 3.1 Informative Bound:**
   - At $\theta = 85^\circ$ ($\cos \theta \approx 0.087156$) and corpus-average IC $\bar{p} = 0.30$, maximum library size is bounded by $K \le 320$.

### Independently reproduced

Not independently reproduced. (This research capture records the mathematical theorems and synthetic numerical proofs from `arXiv:2609.17609v1`; no internal empirical backtest has yet been conducted in NautilusTrader or PyBroker).

### Negative evidence

- **Theorem 8.2 (Exact Orthogonal Failure):** Proves that an exponential-capacity separated signal library can be constructed where every candidate has strictly positive IC ($\bar{p}_i = \sqrt{0.1} > 0$), yet the EWS ensemble is mathematically orthogonal to the leading principal component $v_1(M)$. In this regime, standard PCA factor risk models completely misclassify the alpha source as residual noise.
- **Theorem 3.3 (Isotropic Collapse under Zero Margin):** If factors are selected merely by positive IC ($\bar{p}_i > 0$) without an explicit margin $\beta$, the uncentered second moment $M$ remains exactly isotropic ($I_{qT} / qT$), yielding zero statistical eigengap and leaving the ensemble vulnerable to arbitrary transverse perturbations.
- **Section 10.3 (Statistical Estimation Breakdown):** If the candidate pool size $J$ grows exponentially relative to history length $T$ ($\log J \ne o(T)$), sample correlation errors $\epsilon_{J,T}$ fail to vanish, causing empirical correlation screening to admit heavily correlated factors that corrupt the ensemble.

## Falsification plan

The core falsification thesis is that **an equally weighted ensemble of correlation-separated signals ($\hat{c}_{ij} \le 0.5$) with positive historical IC ($\hat{\bar{p}}_i > 0$) fails to maintain positive out-of-sample alpha and deviates from PC1 whenever the residual gauge condition ($\rho > \eta$) is violated**:

1. **Ablation Test — Margin vs. No-Margin Selection:**
   - *Control Group:* Greedily select $K$ signals from candidate pool $J = 1,000$ requiring only positive in-sample IC ($\hat{\bar{p}}_i > 0$) and separation $\hat{c}_{ij} \le 0.5$.
   - *Treatment Group:* Require strict certified margin $\hat{\bar{p}}_i \ge \beta + \epsilon_{\text{IC}}$ with $\beta = 0.03$.
   - *Falsification Metric:* Measure the in-sample and out-of-sample spectral ratio $\lambda_1(M) / \lambda_2(M)$.
   - `research-defined falsification threshold`: The control group must exhibit an empirical ratio $\lambda_1 / \lambda_2 \approx 1.0$ (isotropy), while the treatment group must exhibit $\lambda_1 / \lambda_2 \ge 2.0$ for $T \ge 60$. If the treatment group fails to produce a significant eigengap, the three-level spectral theorem is falsified.

2. **Residual Gauge Breakdown Test:**
   - In synthetic or empirical factor libraries, calculate $\rho = \|\mu\|_2^2$ and $\eta = \|\Sigma\|_{\text{op}}$.
   - `research-defined falsification threshold`: When $\rho \le \eta$, measure the angular deviation $\theta_{\text{align}} = \angle(\mu, v_1(M))$. If $\theta_{\text{align}} < 15^\circ$ despite $\rho < 0.5 \eta$, Theorem 6.1's bound sharpness is weakened. Conversely, if out-of-sample alpha Sharpe drops to zero when $\rho \le \eta$, the necessity of the residual gauge gate is confirmed.

3. **Sample-Complexity Overfitting Test:**
   - Vary candidate pool size $J \in \{50, 500, 5000\}$ over fixed sample length $T = 252$ daily bars.
   - `research-defined falsification threshold`: For $J = 5000$ (where $\log J / T \approx 0.034$), out-of-sample pairwise correlation among admitted signals must exceed the nominal boundary $\cos \theta = 0.50$ by more than $2 \epsilon_{J,T}$. If out-of-sample correlation remains $\le 0.50$ without Hoeffding buffer subtraction, the uniform union bound is overly conservative.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Methodological Domain:** The primary paper is a pure mathematical and geometric derivation on cross-sectional forecasting spaces; it contains zero empirical crypto or traditional market backtests. Application to cryptocurrency markets is strictly a `research interpretation`.
- **Crypto-Specific Market Microstructure Adaptations (`research-proposed`):**
  1. *24/7 Continuous Trading & Candle Aggregation:* Unlike equity daily sessions, crypto markets trade continuously. Cross-sectional neutralization and return targets $Q_t$ must be aligned to fixed UTC midnight (00:00:00 UTC) snapshots to prevent asynchronous sampling artifacts.
  2. *Cross-Sectional Asset Universe Volatility & Delisting:* The crypto universe undergoes frequent token listings and delistings. Spherical normalization requires handling time-varying cross-sectional dimension $d_t$, projecting onto a dynamically shifting neutral hyperplane $H_t = \{s \in \mathbb{R}^{d_t} : \mathbf{1}^\top s = 0\}$.
  3. *Perpetual Funding Rate Drift:* When constructing market-neutral factor portfolios on crypto perpetual contracts, funding rate imbalances across long and short legs can erode alpha returns. Signal combination must incorporate funding-rate neutral constraints alongside cross-sectional dollar neutrality.
  4. *Severe Factor Multicollinearity & Meme Regimes:* Crypto factor spaces are notorious for sudden regime shifts where all altcoins move with high beta to Bitcoin. Under such regimes, transverse residual variance $\eta = \|\Sigma\|_{\text{op}}$ spikes dramatically, threatening the condition $\rho > \eta$ and triggering emergency ensemble de-allocation.

## Limitations

- **Underspecified Candidate Generation:** The source paper analyzes the geometric and spectral properties of signal *libraries*, but does not specify the underlying generative mechanism for creating raw candidate signals $s_{i,t}$.
- **No Empirical Market Data Backtest:** The results are proven analytically and checked via synthetic Monte Carlo quadrature; realized Sharpe, maximum drawdown, and capacity under real-world transaction costs are untested.
- **Fixed-Domain vs Growing History Asymptotics:** Theorem 5.2 fixes the history length $T$ before taking the angular separation $\theta \to 0$. In real trading, new dates arrive continuously ($T \to \infty$) while the correlation threshold $\theta$ is held fixed.
- **I.I.D. Return Assumption in Estimation Bounds:** The Hoeffding concentration bounds in Section 10.3 assume independent and identically distributed trading dates. Crypto return series exhibit heavy autocorrelation, volatility clustering, and fat tails, meaning empirical sample errors $\epsilon_{J,T}$ will be larger than i.i.d. theoretical bounds.

## Implementation status

- `not-implemented`: This record represents a theoretical and methodological research capture. No implementation has been created in NautilusTrader, PyBroker, or any backtesting engine.

## Adoption boundary

- `research-only`: Research capture only. Not approved for strategy implementation, paper trading, testnet, or live trading.

## Related Wiki records

- `[[goant-quality-diversity-multi-agent-microstructure-alpha-discovery-2026-09-12]]` — Quality-diversity search and multi-agent factor discovery under correlation penalties.
- `[[factorengine-program-level-knowledge-infused-factor-mining-2026-09-05]]` — Program-level factor mining and expression-tree alpha search.
- `[[vst-verifiable-structured-transport-agentic-alpha-discovery-2026-09-12]]` — Structured transport and verifiable alpha discovery pipelines.
- `[[cross-sectional-crypto-momentum-2026-08-31]]` — Cross-sectional momentum alpha normalization and factor portfolio construction.
- `[[two-level-uncertainty-cross-sectional-ranker-regime-trust-gate-tail-cap-2026-09-05]]` — Cross-sectional ranking and factor uncertainty gating.

## Sources

- **Primary Source:** Marc Nunes, *"Separated Signal Libraries: Packing, Saturation, and Joint Spectral Limits"*, arXiv preprint `arXiv:2609.17609v1 [q-fin.ST]`, Version 7, September 16, 2026. Stable URL: https://arxiv.org/abs/2609.17609. Full-text HTML: https://arxiv.org/html/2609.17609v1. PDF: https://arxiv.org/pdf/2609.17609v1.
- **Prior Research Series (Attributed Separately):**
  - Marc Nunes, *"Large Signal Libraries: Equal-Weight Limits and the Divergent Spectra of Signals and PnL"*, arXiv preprint `arXiv:2609.12477 [q-fin.ST]`, September 2026. Stable URL: https://arxiv.org/abs/2609.12477.
  - Marc Nunes, *"Signal Correlation, IC, and PnL Dependence"*, arXiv preprint `arXiv:2609.09588 [q-fin.ST]`, September 2026. Stable URL: https://arxiv.org/abs/2609.09588.
- **Cited Mathematical Foundations:**
  - S. V. Borodachov, D. P. Hardin, and E. B. Saff, *"Asymptotics of best-packing on rectifiable sets"*, Proceedings of the American Mathematical Society 135(8), 2369–2380, 2007. DOI: [10.1090/S0002-9939-07-08975-7](https://doi.org/10.1090/S0002-9939-07-08975-7).
  - B. S. Ho, *"A new lower bound for the kissing number in 19 dimensions"*, arXiv preprint `arXiv:2603.10425v2 [math.MG]`, 2026. Stable URL: https://arxiv.org/abs/2603.10425.
  - N. Leijenhorst and D. de Laat, *"Solving clustered low-rank semidefinite programs arising from polynomial optimization"*, Mathematical Programming Computation 16(3), 503–534, 2024. DOI: [10.1007/s12532-024-00264-w](https://doi.org/10.1007/s12532-024-00264-w).
  - H. Cohn and A. Li, *"Improved kissing numbers in seventeen through twenty-one dimensions"*, arXiv preprint `arXiv:2411.04916v3 [math.MG]`, revised September 2026. Stable URL: https://arxiv.org/abs/2411.04916.
  - C. Davis and W. M. Kahan, *"The rotation of eigenvectors by a perturbation. III"*, SIAM Journal on Numerical Analysis 7(1), 1–46, 1970. DOI: [10.1137/0707001](https://doi.org/10.1137/0707001).
  - E. N. Gilbert, *"A comparison of signalling alphabets"*, Bell System Technical Journal 31(3), 504–522, 1952. DOI: [10.1002/j.1538-7305.1952.tb01393.x](https://doi.org/10.1002/j.1538-7305.1952.tb01393.x).
  - R. R. Varshamov, *"Estimate of the number of signals in error correcting codes"*, Doklady Akademii Nauk SSSR 117(5), 739–741, 1957.
  - R. R. Bahadur and R. Ranga Rao, *"On deviations of the sample mean"*, Annals of Mathematical Statistics 31(4), 1015–1027, 1960. DOI: [10.1214/aoms/1177705674](https://doi.org/10.1214/aoms/1177705674).
  - W. Hoeffding, *"Probability inequalities for sums of bounded random variables"*, Journal of the American Statistical Association 58(301), 13–30, 1963. DOI: [10.1080/01621459.1963.10500830](https://doi.org/10.1080/01621459.1963.10500830).
