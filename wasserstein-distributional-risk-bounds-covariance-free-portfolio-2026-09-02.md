---
schema: strategy-research-record-v1
title: "Wasserstein Distributional Risk Bounds: Covariance-Free Portfolio Optimization via LLM Article Embedding Clouds"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - optimal-transport
  - wasserstein-distance
  - distribution-valued-characteristics
  - covariance-free
  - language-model-embeddings
  - certified-diversification
  - convex-programming
status: research-only
confidence: medium
source_as_of: 2026-08-29
sources:
  - "Marcus Gawronsky and Chun-Sung Huang, 'Portfolio Risk Bounds without Cross-Asset Return Covariances: Distributional Fields from Language-Model Representations', arXiv preprint arXiv:2608.29692v1 [q-fin.PM, q-fin.CP, cs.LG], August 29, 2026. DOI: 10.48550/arXiv.2608.29692. Stable URL: https://arxiv.org/abs/2608.29692"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Wasserstein Distributional Risk Bounds: Covariance-Free Portfolio Optimization via LLM Article Embedding Clouds

## Provenance

- **Primary Source:** Marcus Gawronsky (School of Computing and Information Systems, Singapore Management University / Quantitative Research) and Chun-Sung Huang (Department of Economics, National Taiwan University / Institute of Economics, Academia Sinica), *"Portfolio Risk Bounds without Cross-Asset Return Covariances: Distributional Fields from Language-Model Representations"*, arXiv preprint `arXiv:2608.29692v1 [q-fin.PM, q-fin.CP, cs.LG]`, submitted August 29, 2026. DOI: [10.48550/arXiv.2608.29692](https://doi.org/10.48550/arXiv.2608.29692). Stable URL: [https://arxiv.org/abs/2608.29692](https://arxiv.org/abs/2608.29692). Full text HTML: [https://arxiv.org/html/2608.29692v1](https://arxiv.org/html/2608.29692v1).
- **Core Empirical Datasets:**
  - **U.S. Equity Return Panel:** 52 U.S. firms with complete return histories from March 19, 2018 to December 30, 2022 (1,207 trading days) sourced from Yahoo Finance adjusted close prices (simple returns $R_i$).
  - **Textual News Corpus:** Nasdaq per-symbol corporate news archive spanning 2018 through 2022, processed into equal-sized empirical article clouds per firm.
  - **Embedding Representations:** Primary representation encoded via frozen Qwen3-Embedding-8B (4,096 dimensions, row-normalized, accessed via OpenRouter). Robustness ladders evaluated at 1,024, 256, and 64 coordinates, alongside Qwen3-Embedding-4B, BAAI BGE-large-en-v1.5, and locally trained 320-coordinate EttaX encoders across Wikipedia training snapshots (2017, 2020, 2026).
- **Related Foundational Literature:**
  - Markowitz, H. (1952), "Portfolio selection", *The Journal of Finance* 7(1), 77–91 — canonical mean-variance formulation.
  - Ledoit, O. & Wolf, M. (2004), "A well-conditioned estimator for large-dimensional covariance matrices", *Journal of Multivariate Analysis* 88(2), 365–411 — structured covariance shrinkage.
  - Kelly, B., Pruitt, S., & Su, Y. (2019), "Characteristics are covariances: A unified model of risk and return", *Journal of Financial Economics* 134(3), 501–524 — Instrumented Principal Component Analysis (IPCA).
  - Kusner, M. et al. (2015), "From word embeddings to document distances", *ICML 2015* — optimal transport on empirical word distributions (Word Mover's Distance).
  - Gawronsky, M. & Huang, C.-S. (2026b), "Pairwise covariance envelopes from Wasserstein separation" / (2026a), "Wasserstein-barycentric interaction fields for spatial factor models", *arXiv:2608.29669*.

## Economic mechanism

### Source-reported

1. **Failure of Return Covariance Estimation in Finite Panels:** An unrestricted covariance matrix for $n$ assets contains $n(n+1)/2$ entries, but a sample of length $T$ has rank at most $\min(T-1, n)$. Short histories create severe estimation error in the largest eigenvalues while optimization is excessively sensitive to the weakest sample directions (error maximization).
2. **Distribution-Valued Characteristics & Optimal Transport Separation:** Rather than collapsing a firm's public corporate disclosures into a single scalar or average sentiment vector, the firm is represented as a full empirical probability distribution $C_i$ of article embeddings. Balanced quadratic Wasserstein distance $W_2(C_i, C_j)$ measures the minimal root-mean-square displacement required to morph one firm's information cloud into another.
3. **Maintained Transmission Restrictions (Carrier and Slack):** Under a maintained anti-Lipschitz carrier $t: \mathcal{X} \to \mathcal{H}$ with constant $L > 0$ ($d_\mathcal{H}(t(x), t(x')) \ge L^{-1} d_\mathcal{X}(x, x')$) and firm-specific slack radii $\tau_i$ ($\|u_i(x) - t(x)\| \le \tau_i$), observable semantic distance certifies a lower bound on latent systematic exposure separation:
   $$\ell_{ij} = [L^{-1} W_2(C_i, C_j) - (\tau_i + \tau_j)]_+$$
4. **Coherent Portfolio Variance Bound:** By the Hilbert-space polarization identity, when all exposure marginals belong to one coherent joint law $J$, the systematic portfolio variance under normalized risk weights $q$ is strictly upper-bounded:
   $$\operatorname{Var}(S_q) \le 1 - \mathcal{C}(q)$$
   where $\mathcal{C}(q) = \frac{1}{2} \sum_{i,j} q_i q_j \ell_{ij}^2$ is the certified diversification credit.
5. **Carrier Invariance at Zero Slack:** In the canonical zero-slack specification ($\tau_i = 0$), $\ell_{ij} = L^{-1} W_2(C_i, C_j)$. The carrier constant $L$ scales the certified variance reduction by $L^{-2}$ but does **not** alter the normalized risk allocation $q^*$. The optimal portfolio is uniquely determined by observed $W_2$ information geometry without estimating cross-asset return covariances.

### Research interpretation

The falsifiable quantitative thesis is that **distributional semantic separation in public firm disclosures provides an ex-ante certified upper bound on portfolio risk that achieves low-variance allocations without requiring return covariance estimation**:
1. **Economic Orthogonality of Information Distributions:** Firms that operate in distinct supply chains, regulatory environments, and customer ecosystems discuss fundamentally different operational subjects in public news. Because text embeddings reflect operational fundamentals, positive Wasserstein transport distance between article clouds certifies that the underlying firms cannot share collinear systematic risk factors.
2. **Covariance-Free Decision Formulation:** By minimizing the certified upper bound $1 - \mathcal{C}(q)$, an allocator derives a risk-minimizing portfolio that is immune to sample-covariance instability, structural breaks, and return co-movement noise.
3. **Convex Risk Minimization:** When the pairwise floor matrix satisfies Schoenberg's criterion for conditional negative definiteness, the objective $q \mapsto 1 - \mathcal{C}(q)$ is strictly convex along the simplex, guaranteeing rapid, global quadratic programming convergence without non-convex local traps.

## Signal

### Mathematical Formulation and Optimization Program

#### 1. Information Distance Extraction
For each firm $i \in \{1, \dots, n\}$, let $C_i = \frac{1}{K} \sum_{k=1}^K \delta_{x_{i,k}}$ be the empirical distribution of $K$ row-normalized article embedding vectors $x_{i,k} \in \mathbb{R}^d$ generated by frozen Qwen3-Embedding-8B ($d=4,096$).
The pairwise quadratic Wasserstein-2 distance is:
$$W_2^2(C_i, C_j) = \min_{\pi \in \Pi(C_i, C_j)} \sum_{k=1}^K \sum_{l=1}^K \pi_{kl} \|x_{i,k} - x_{j,l}\|_2^2$$
where $\Pi(C_i, C_j)$ is the transport polytope with marginals $\frac{1}{K} \mathbf{1}_K$.

#### 2. Certified Diversification Credit & Objective
Under the canonical zero-slack specification ($\tau_i = 0$), define the symmetric, zero-diagonal squared-distance matrix $M \in \mathbb{R}^{n \times n}$:
$$M_{ij} = W_2^2(C_i, C_j) \quad (i \ne j), \quad M_{ii} = 0$$
The certified portfolio diversification credit for normalized risk weights $q \in \Delta_n$ is:
$$\mathcal{C}(q) = \frac{1}{2} q^\top M q = \sum_{i < j} q_i q_j W_2^2(C_i, C_j)$$
The information-certified risk minimization program (the "news-only allocation") solves:
$$\max_{q \in \mathcal{Q}} \quad \frac{1}{2} q^\top M q \iff \min_{q \in \mathcal{Q}} \quad 1 - \frac{1}{2} q^\top M q$$
subject to:
$$\sum_{i=1}^n q_i = 1, \quad 0 \le q_i \le \text{cap} \quad (\text{e.g. } \text{cap} = 12.5\% \text{ or } 15.0\%)$$

#### 3. Convexity Verification (Theorem 5)
By Schoenberg's criterion, the objective $1 - \mathcal{C}(q)$ is convex on the simplex if and only if the double-centered matrix:
$$H = -\frac{1}{2} \left(I - \frac{1}{n} \mathbf{1}\mathbf{1}^\top\right) M \left(I - \frac{1}{n} \mathbf{1}\mathbf{1}^\top\right)$$
is positive semidefinite (isometric embedding in Hilbert space), which is verified empirically for the frozen distance matrix.

#### 4. Capital Weight Translation
For standardized assets with unit marginal volatility scales ($\sigma_i = 1$), capital weights $x$ equal risk weights: $x_i = q_i$. For heterogeneous asset volatilities, capital weights are recovered via:
$$x_i = \frac{q_i / \sigma_i}{\sum_{j=1}^n (q_j / \sigma_j)}$$
requiring only univariate marginal volatility estimates $\sigma_i$, completely bypassing the estimation of $n(n-1)/2$ return covariances.

## Required data

- **Public Textual Corpus:**
  - Corporate news articles, regulatory filings (SEC 10-K/10-Q/8-K), press releases, or protocol governance updates tagged by asset symbol.
  - Per-symbol balanced article sampling (e.g. $K=50$ to $K=200$ articles per asset per year) ordered deterministically by URL/text hash to avoid support imbalance.
- **Pre-trained Dense Vector Encoder:**
  - Frozen sentence/document embedding model (e.g., Qwen3-Embedding-8B, 4,096 dimensions, row-normalized).
- **Price / Return Series (Marginal Scales Only):**
  - Daily adjusted close prices to compute univariate asset volatilities $\sigma_i$ (or standard deviations of rolling returns).
  - No cross-asset return covariance matrix or high-frequency tick data is required.
- **Point-in-Time Controls:** All text articles must be strictly timestamped prior to the portfolio construction cutoff date; no future revisions or post-dated articles admitted.

## Execution assumptions

- **Portfolio Rebalancing Cadence:** Low frequency: annual, semi-annual, or quarterly rebalancing.
- **Order Types & Execution:** Passive TWAP or VWAP execution across liquid large-cap equities or tokens; daily rebalancing turnover is low ($13.2\%$ to $26.8\%$ annual one-way turnover).
- **Transaction Costs & Capacity:** 5–10 bps round-trip transaction costs in equities; capacity is high due to the diversified, capped long-only structure (effective $N \approx 24$ names across 52 assets).
- **Shorting / Margin:** Long-only simplex constraints ($q_i \ge 0$); no borrow, shorting, or leverage required.

## Evidence

### Source-reported

All empirical figures trace directly to Marcus Gawronsky and Chun-Sung Huang (arXiv:2608.29692v1, Section 6, Tables 1–4):

1. **In-Sample Variance Percentiles Across Reference Populations (Table 1):**
   Evaluated on the 52-firm U.S. equity panel (2018–2022, 1,207 days) against Monte Carlo draws from four prespecified Dirichlet-capped long-only reference populations $\mathcal{G}_k$:
   - **Population 1 (Uniform $\alpha = 1.0$, cap = 12.5%):** News-only allocation variance percentile = **0.720%**; Equal Risk weighting percentile = **28.630%**.
   - **Population 2 (Uniform $\alpha = 1.0$, cap = 15.0%):** News-only allocation variance percentile = **0.690%**; Equal Risk weighting percentile = **28.415%**.
   - **Population 3 (Matched concentration $\alpha = 0.8$, cap = 12.5%, mean effective $N=24.23$ matching candidate $23.65$):** News-only allocation variance percentile = **0.890%**; Equal Risk weighting percentile = **25.400%**.
   - **Population 4 (Concentrated $\alpha = 0.5$, cap = 12.5%, mean effective $N=19.01$):** News-only allocation variance percentile = **1.330%**; Equal Risk weighting percentile = **21.060%**.
   - In all four populations, the news-only allocation constructed without return covariances lands in the bottom ~1% of feasible portfolio variance, vastly outperforming inverse-volatility equal risk weighting.
2. **Realized Standardized Variance Calibration (Table 2):**
   - The news-only allocation achieves a realized standardized variance that is **8.310392% lower** than the equal-risk (inverse-volatility) benchmark.
   - It remains **35.558038% above** the ex-post in-sample sample GMV optimum (confirming that information geometry provides a valid upper-bound certificate rather than an exact replacer of the in-sample empirical GMV).
3. **Allocation Anatomy and Sector Attribution (Table 3, Figure 2):**
   - Maximum single-firm position weight: **12.112251%**;
   - Effective number of names: $N = 23.65$ (positive allocations on 38 of 52 firms);
   - Additive credit decomposition: **87.101723%** of certificate credit originates from cross-sector pairs, and **12.898277%** from within-sector pairs.
4. **Expanding Information Cutoff Stability (2018–2022, Figure 3):**
   - Across 5 annual cutoffs, effective $N$ remains bounded between $22.95$ and $24.56$;
   - Maximum asset weight remains between $8.315607\%$ and $12.112251\%$;
   - One-way annual turnover ranges from $13.222253\%$ to $26.827403\%$, with no abnormal dislocation during the 2020 COVID shock ($14.47\%$ turnover from 2019 to 2020).
5. **Representation Sensitivity Ladder (Table 4 & Section D.1):**
   - Qwen3-8B compressed to 1,024 coordinates yields virtually identical performance to the full 4,096-coordinate baseline;
   - BAAI BGE-large-en-v1.5 at 1,024 coordinates achieves comparable low-variance percentiles;
   - Extreme truncation to 64 coordinates non-monotonically alters weights and lowers the in-sample variance rank.

### Independently reproduced

`not independently reproduced`.

### Negative evidence

- The representation ladder shows non-monotonic sensitivity to extreme coordinate width compression (64 coordinates), demonstrating that aggressive embedding truncation alters the underlying metric space geometry.
- Locally trained EttaX encoders across three Wikipedia training snapshots (V0 2017, V1 2020, V3 2026) fail the post-specified statistical equivalence criterion, confirming that optimal transport distances are sensitive to encoder training corpora.
- Information geometry alone cannot prevent portfolio drawdown when macroeconomic liquidity shocks drive cross-asset correlations to unity.
- None identified in the reviewed sources beyond the above; absence is not evidence of no negative result.

## Falsification plan

1. **Backtest Design:** Implement the news-only Wasserstein-2 portfolio allocation on an out-of-sample expanding window from 2023 to 2026 across the S&P 100 universe, updating embeddings annually.
2. **Control Baselines:** Compare against: (a) Equal Weight ($1/N$); (b) Inverse-Volatility (Equal Risk); (c) Ledoit-Wolf analytical shrinkage GMV; (d) Linear factor model GMV.
3. **Falsification Thresholds (pre-declared):**
   - If the news-only allocation fails to achieve lower realized portfolio variance than the inverse-volatility equal-risk benchmark across at least 3 out of 4 out-of-sample test years, reject the covariance-free information certificate hypothesis.
   - If the pairwise floor matrix violates the Schoenberg conditional negative definiteness condition on more than 10% of rebalance periods, reject the global convexity guarantee.
   - If transaction costs from annual turnover exceed the realized variance reduction benefit relative to $1/N$, reject operational adoption.
4. **Ablation & Stress Checks:** Test performance under randomized (shuffled) text-to-asset assignments (placebo test); evaluate whether the certificate survives using raw unnormalized vs. normalized embeddings.

## Crypto portability

- **Portability:** `adapted` (research interpretation; original empirical evidence is derived exclusively from U.S. equities and Nasdaq news).
- **Crypto-Specific Adaptation Requirements:**
  - **Text Corpus Substitution:** Traditional financial news archives must be substituted with crypto-native textual corpora: developer GitHub commit logs, whitepapers, governance forum proposals (Discourse/Snapshot), and audit reports.
  - **Dominant Market Beta:** In crypto markets, Bitcoin beta dominates cross-sectional variance (cross-asset correlations often reach 0.70–0.95 during bear markets). High semantic distance between protocol whitepapers (e.g. DeFi lending vs. AI agent token) does not necessarily guarantee low return correlation during systemic liquidations.
  - **Tokenomics & Emissions:** Unlike equities where market cap reflects enterprise equity, crypto tokens experience aggressive inflation, unlock schedules, and liquidity pool staking incentives that override fundamental business differentiation.

## Limitations

- `not independently reproduced`;
- **In-Sample Evaluation:** The primary 2018–2022 panel evaluation is descriptive and in-sample, establishing location within feasible populations rather than a point-in-time trading track record;
- **Survivor Panel Bias:** The 52-firm universe requires continuous 5-year news and price histories, omitting distressed, delisted, or newly listed firms;
- **Unidentified Transmission Parameters:** The theoretical anti-Lipschitz carrier constant $L$ and firm slack radii $\tau_i$ are maintained structural assumptions that cannot be directly estimated from text data alone.

## Implementation status

- `not-implemented`. Research capture only; no live, paper, or testnet trading modules have been constructed or authorized.

## Adoption boundary

- `research-only`, `not-approved`.
- This record captures theoretical optimal transport and portfolio risk research. It does not constitute authorization for deployment in PyBroker, Nautilus, paper, testnet, or live trading systems.

## Related Wiki records

- `[[quant/wasserstein-robust-portfolio-hyperplane-dual-lp-2026-09-02]]` — Order-1 Wasserstein distributionally robust optimization.
- `[[quant/tda-persistent-homology-finbert-sentiment-portfolio-optimization-2026-09-02]]` — Topological data analysis and FinBERT Wasserstein clustering for portfolio selection.
- `[[quant/kellyboost-growth-optimal-gbdt-portfolio-construction-2026-09-02]]` — Growth-optimal machine learning portfolio construction.

## Sources

1. Marcus Gawronsky and Chun-Sung Huang, *"Portfolio Risk Bounds without Cross-Asset Return Covariances: Distributional Fields from Language-Model Representations"*, arXiv preprint `arXiv:2608.29692v1 [q-fin.PM, q-fin.CP, cs.LG]`, submitted August 29, 2026. DOI: [10.48550/arXiv.2608.29692](https://doi.org/10.48550/arXiv.2608.29692). Stable URL: [https://arxiv.org/abs/2608.29692](https://arxiv.org/abs/2608.29692). Full text HTML: [https://arxiv.org/html/2608.29692v1](https://arxiv.org/html/2608.29692v1).
2. Markowitz, H. (1952), "Portfolio selection", *The Journal of Finance* 7(1), 77–91. DOI: [10.1111/j.1540-6261.1952.tb01525.x](https://doi.org/10.1111/j.1540-6261.1952.tb01525.x).
3. Ledoit, O. & Wolf, M. (2004), "A well-conditioned estimator for large-dimensional covariance matrices", *Journal of Multivariate Analysis* 88(2), 365–411. DOI: [10.1016/S0047-259X(03)00096-4](https://doi.org/10.1016/S0047-259X(03)00096-4).
4. Kelly, B., Pruitt, S., & Su, Y. (2019), "Characteristics are covariances: A unified model of risk and return", *Journal of Financial Economics* 134(3), 501–524. DOI: [10.1016/j.jfineco.2019.05.009](https://doi.org/10.1016/j.jfineco.2019.05.009).
5. Kusner, M., Sun, Y., Kolkin, N., & Weinberger, K. (2015), "From word embeddings to document distances", *Proceedings of the 32nd International Conference on Machine Learning (ICML 2015)*, pp. 957–966.
