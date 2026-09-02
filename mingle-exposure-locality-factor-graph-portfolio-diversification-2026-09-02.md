---
schema: strategy-research-record-v1
title: "MINGLE: Mutually-Informed Graph Locality and Factor Exposures for Portfolio Diversification via Joint ADMM Regularization"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-diversification
  - factor-models
  - graph-learning
  - admm
  - exposure-locality
  - risk-parity
  - cross-sectional-equity
status: research-only
confidence: high
source_as_of: 2026-08-06
sources:
  - "Sara Chehab, Giorgos Iacovides, Parisa Yazdanparast, Danilo Mandic, 'Beyond Co-Movement: Locality by Exposures Enables a Joint Factor-Graph Framework for Portfolio Diversification', arXiv:2608.06618v1 [q-fin.PM, q-fin.ST, cs.LG], August 6, 2026. DOI: 10.48550/arXiv.2608.06618. https://arxiv.org/abs/2608.06618"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MINGLE: Mutually-Informed Graph Locality and Factor Exposures for Portfolio Diversification via Joint ADMM Regularization

## Provenance

- **Primary Source:** Sara Chehab, Giorgos Iacovides, Parisa Yazdanparast, Danilo Mandic (Imperial College London), *"Beyond Co-Movement: Locality by Exposures Enables a Joint Factor-Graph Framework for Portfolio Diversification"*, arXiv preprint `arXiv:2608.06618v1 [q-fin.PM, q-fin.ST, cs.LG]`, published August 6, 2026. DOI: [10.48550/arXiv.2608.06618](https://doi.org/10.48550/arXiv.2608.06618). Full text: [https://arxiv.org/abs/2608.06618](https://arxiv.org/abs/2608.06618).
- **Primary Subject Areas:** Portfolio Management (`q-fin.PM`), Statistical Finance (`q-fin.ST`), Machine Learning (`cs.LG`).
- **Context:** Traditional portfolio construction relies either on empirical correlation graphs (which conflate transient co-movement and idiosyncratic noise with structural relationships) or on statistical factor models (e.g., PCA/factor analysis, which ignore relational graph topologies across assets). Chehab, Iacovides, Yazdanparast, and Mandic propose the **Mutually-INformed Graph-Locality and Exposures (MINGLE)** framework, which defines graph locality directly through latent systematic factor exposure profiles rather than raw return correlations. Solved via a unified Alternating Direction Method of Multipliers (ADMM) optimization, MINGLE jointly learns latent factor dynamics and graph adjacency to construct well-conditioned covariance estimators for optimal portfolio diversification.

## Economic mechanism

### Source-reported

1. **Failure of Return Co-Movement Networks:** Constructing financial graphs using empirical Pearson correlation coefficients creates dense, noisy networks. During market distress, correlations spike toward unity across all assets, destroying graph modularity and generating ill-conditioned covariance matrices that destabilize Markowitz and risk-parity allocations.
2. **Exposure-Locality Principle:** True economic similarity between assets arises from shared sensitivities to fundamental systematic drivers (e.g., interest rates, inflation, commodity shocks, consumer demand), not temporary contemporaneous price movements. By enforcing that assets connected on the graph must possess smooth (similar) latent factor exposure vectors $b_i, b_j \in \mathbb{R}^K$, the network topology filters out idiosyncratic noise.
3. **Mutual Regularization via ADMM:** Learning the latent factors $F$, factor exposures $B$, and graph adjacency matrix $W$ simultaneously ensures that:
   - Factor exposures regularize the graph structure against noise.
   - Graph Laplacian smoothness regularizes factor estimation against in-sample overfitting.

### Research interpretation

The falsifiable thesis is that **regularizing latent factor decomposition via graph Laplacian Dirichlet smoothness on factor exposure profiles ($\operatorname{Tr}(B^\top L B)$) yields a better-conditioned covariance matrix that systematically outperforms sample-covariance and standard PCA factor models in risk-adjusted out-of-sample portfolio Sharpe ratio and drawdown control across global equity markets**:
- Redefining graph edge weights as functions of latent exposure similarity prevents spurious correlation links.
- The resulting structured covariance matrix $\Sigma_{\mathrm{MINGLE}} = B B^\top + \operatorname{diag}(\Psi)$ dampens estimation error in portfolio weight optimization, reducing turnover and transaction drag.

## Signal

### 1. Joint Optimization Formulation (MINGLE)

Let $X \in \mathbb{R}^{T \times N}$ be the matrix of centered asset returns for $N$ assets over $T$ time periods. MINGLE solves:
$$\min_{F \in \mathbb{R}^{T \times K}, B \in \mathbb{R}^{N \times K}, W \in \mathcal{W}} \frac{1}{2} \| X - F B^\top \|_F^2 + \alpha \operatorname{Tr}\left( B^\top L(W) B \right) + \beta \| W \|_F^2 - \gamma \mathbf{1}^\top \log(W \mathbf{1})$$
subject to:
$$\mathcal{W} = \{ W \in \mathbb{R}^{N \times N} \mid W = W^\top \ge 0, \operatorname{diag}(W) = 0 \}$$
where:
- $F \in \mathbb{R}^{T \times K}$: Latent systematic factor return matrix ($K \ll N$).
- $B \in \mathbb{R}^{N \times K}$: Factor exposure matrix, where row $b_i^\top$ is the factor loading vector of asset $i$.
- $W \in \mathbb{R}^{N \times N}$: Symmetric, non-negative graph adjacency matrix.
- $L(W) = \operatorname{diag}(W \mathbf{1}) - W$: Combinatorial graph Laplacian matrix.
- $\operatorname{Tr}(B^\top L(W) B) = \frac{1}{2} \sum_{i,j} W_{ij} \| b_i - b_j \|_2^2$: Dirichlet smoothness penalty enforcing exposure locality.
- $\beta \| W \|_F^2$: Frobenious norm penalty controlling graph density / sparsity.
- $-\gamma \mathbf{1}^\top \log(W \mathbf{1})$: Logarithmic degree barrier preventing isolated vertices (guarantees positive degree $d_i > 0$).

### 2. ADMM Splitting & Coordinate Updates

The non-convex joint problem is partitioned into convex sub-problems solved iteratively until convergence:
1. **Factor Update ($F$-step):** Holding $B$ fixed, the unconstrained least-squares solution is:
   $$F^{(k+1)} = X B^{(k)} \left( (B^{(k)})^\top B^{(k)} \right)^{-1}$$
2. **Exposure Update ($B$-step):** Holding $F$ and $W$ fixed, $B$ satisfies the matrix Sylvester equation:
   $$B^{(k+1)} (F^{(k+1)})^\top F^{(k+1)} + 2 \alpha L(W^{(k)}) B^{(k+1)} = X^\top F^{(k+1)}$$
   solved efficiently via vectorization or Bartels-Stewart decomposition.
3. **Graph Adjacency Update ($W$-step):** Holding $B$ fixed, the edge optimization decouples column-wise into independent quadratic programs with logarithmic barrier:
   $$w_i^{(k+1)} = \arg\min_{w_i \ge 0} \frac{1}{2} w_i^\top (\alpha D_i + 2\beta I) w_i - \gamma \log(\mathbf{1}^\top w_i)$$
   where $D_{ij} = \| b_i - b_j \|_2^2$ is the Euclidean distance between factor exposures.

### 3. Portfolio Weight Allocation

From the converged factor loadings $B^*$ and residual variance $\Psi^* = \operatorname{diag}(\frac{1}{T} \| X - F^* (B^*)^\top \|_F^2)$:
1. Construct structured covariance matrix:
   $$\hat{\Sigma}_{\mathrm{MINGLE}} = B^* (B^*)^\top + \Psi^*$$
2. Solve the Global Minimum Variance (GMV) or Risk Parity (RP) optimization problem:
   - **GMV:** $w^* = \frac{\hat{\Sigma}_{\mathrm{MINGLE}}^{-1} \mathbf{1}}{\mathbf{1}^\top \hat{\Sigma}_{\mathrm{MINGLE}}^{-1} \mathbf{1}}$
   - **Risk Parity:** $w_i \left( \hat{\Sigma}_{\mathrm{MINGLE}} w \right)_i = \frac{1}{N} w^\top \hat{\Sigma}_{\mathrm{MINGLE}} w \quad \forall i$.
3. Rebalance portfolio weights monthly or quarterly.

## Required data

- **Universe:** 300 global large-cap equities (the 100 most liquid constituents each from S&P 500, Nikkei 225, and STOXX Europe 600 as of 2017).
- **Timeframe:** Daily adjusted closing prices over multi-year evaluation periods.
- **Fields:**
  - Daily total returns $R_{i,t} = (P_{i,t} + D_{i,t}) / P_{i,t-1} - 1$.
  - GICS sector and industry classifications (used for ground-truth modularity and sector alignment validation).
- **Point-in-Time Data Cleanliness:** Survivorship bias controlled via rolling index constituent inclusion; returns centered over rolling lookback windows $T \in [126, 252]$ trading days.

## Execution assumptions

- **Rebalancing Frequency:** Monthly (21 trading days) and Quarterly (63 trading days) rebalancing cadence.
- **Execution Timing:** Market-on-Close (MOC) or Next-Day Open prices.
- **Transaction Costs:** 10 bps, 25 bps, and 50 bps linear round-trip transaction cost stress models.
- **Position Constraints:** Long-only ($w_i \ge 0, \sum w_i = 1$) and Long-Short ($|w_i| \le 0.05, \sum w_i = 0$).

## Evidence

### Source-reported

All quantitative comparisons and topological metrics trace directly to Chehab, Iacovides, Yazdanparast, & Mandic (arXiv:2608.06618v1, Sections 4–5, Figures 2–6, Tables 1–4):
1. **Economic Sector Modularity & Graph Quality:**
   - The MINGLE exposure-similarity graph achieves substantially higher **Normalized Mutual Information (NMI)** with ground-truth GICS sectors ($NMI > 0.65$) compared to correlation-based graphs ($NMI < 0.35$), proving that MINGLE reconstructs authentic fundamental industry clusters without supervision.
2. **Out-of-Sample Portfolio Performance:**
   - Minimum Variance portfolios constructed via MINGLE achieve **higher annualized Sharpe ratios (0.85–1.15 across US, Europe, and Japan)** compared to sample-covariance benchmarks (0.55–0.78) and standard PCA factor models (0.70–0.88).
   - Realized portfolio annualized volatility is reduced by $12\text{--}20\%$ relative to sample covariance across all three geographical indices.
3. **Turnover & Transaction Cost Resilience:**
   - Because MINGLE exposure graphs evolve smoothly over time, **monthly portfolio turnover is reduced by 35%** compared to sample-covariance portfolios, maintaining superior net returns even under 50 bps transaction fee stress.
4. **Covariance Conditioning:**
   - The condition number of $\hat{\Sigma}_{\mathrm{MINGLE}}$ is lower by a factor of 10 to 50 compared to the sample covariance matrix, eliminating extreme weight instability in Markowitz inversions.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- None identified in the reviewed source; absence is not evidence of no negative result.
- However, if the true market return generating process is dominated by idiosyncratic non-linear jumps rather than linear factor exposures (e.g., during sudden single-stock corporate fraud or short squeezes), the linear factor decomposition $X \approx F B^\top$ explains less return variance.

## Falsification plan

1. **Exposure Smoothness Ablation:** Set $\alpha = 0$ (decoupling the graph from factor exposures and reducing MINGLE to standard unregularized PCA). If the full MINGLE model ($\alpha > 0$) does not achieve higher out-of-sample Sharpe ratio ($p < 0.05$) and lower turnover across rolling 5-year walk-forward tests, the exposure-graph coupling mechanism is falsified.
2. **Randomized Graph Topology Placebo:** Replace the learned adjacency matrix $W$ with an Erdős-Rényi random graph or randomly permuted edge weights. If the placebo graph achieves comparable portfolio variance reduction, the specific exposure-locality topology provides no real risk edge.
3. **Factor Rank Misspecification Test:** Vary the number of latent factors $K$ across $\{1, 3, 5, 10, 20\}$. If portfolio performance degrades sharply when $K \neq K^*$, the strategy is hypersensitive to latent dimensionality tuning.

## Crypto portability

**Portability Status:** `adapted` / `unproven`.

- **Traditional Asset Origin:** Evaluated on large-cap equities (S&P 500, Nikkei 225, STOXX 600).
- **Crypto-Specific Adaptation:**
  - Applicable to cross-sectional crypto asset allocation across the top 50–100 liquid spot and perpetual tokens.
  - **Crypto Thematic Sectors:** Instead of GICS sectors, crypto assets cluster into Layer 1, Layer 2, DeFi, AI tokens, Meme coins, and RWA (Real World Assets). MINGLE can learn latent market drivers (Bitcoin beta, Ethereum ecosystem flow, liquidity risk factor) and construct exposure-similarity graphs across tokens.
- **Portability Risks:**
  - *High Market-Wide Beta:* Crypto assets exhibit much higher market correlation with Bitcoin ($\rho > 0.70$) than equities exhibit with the market index, which can compress latent factor distinctiveness.
  - *Listing Instability:* Rapid token turnover, protocol deprecation, and short historical lifetimes require robust handling of missing data and dynamic universe reconstitution.

## Limitations

- **Hyperparameter Sensitivity:** Requires tuning three regularization weights $(\alpha, \beta, \gamma)$ and the latent factor rank $K$.
- **Computational Complexity:** Solving the Sylvester equation and quadratic programs per ADMM iteration across large universes ($N > 1,000$) scales as $O(N^3)$, requiring GPU acceleration for tick or intraday rebalancing.
- **Linear Factor Assumption:** Assumes linear factor relationships $X = F B^\top + E$; non-linear cross-asset co-dependencies (copula or neural interactions) are not captured.

## Implementation status

`not-implemented`

No implementation has been conducted in the local research repository, PyBroker, NautilusTrader, paper, testnet, or live trading systems.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

This record is an upstream research capture. It does not authorize strategy implementation, backtesting promotion, or production deployment.

## Related Wiki records

- `[[observable-matrix-dynamics-portfolio-optimization-2026-09-02]]`
- `[[foreign-exchange-spatiotemporal-graph-statistical-arbitrage-2026-09-02]]`
- `[[portfolio-bayesian-parametric-policies-policy-risk-regularization-2026-09-02]]`

## Sources

- Sara Chehab, Giorgos Iacovides, Parisa Yazdanparast, Danilo Mandic, *"Beyond Co-Movement: Locality by Exposures Enables a Joint Factor-Graph Framework for Portfolio Diversification"*, arXiv preprint `arXiv:2608.06618v1 [q-fin.PM, q-fin.ST, cs.LG]`, submitted August 6, 2026. DOI: `10.48550/arXiv.2608.06618`. URL: [https://arxiv.org/abs/2608.06618](https://arxiv.org/abs/2608.06618).
