---
schema: strategy-research-record-v1
title: "RIEnet: End-to-End Neural Shrinkage of Indefinite Pairwise Correlation Matrices for Incomplete Return Panels"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - covariance-estimation
  - random-matrix-theory
  - nonlinear-shrinkage
  - neural-networks
  - incomplete-panels
  - market-impact
status: research-only
confidence: high
source_as_of: 2026-08-31
sources:
  - "Christian Bongiorno and Lorenzo Villassero, 'End-to-End Neural Shrinkage of Indefinite Pairwise Correlation Matrices for Small-Cap-Inclusive Portfolios', arXiv:2608.30446v1 [q-fin.PM, q-fin.ST], August 31, 2026. DOI: 10.48550/arXiv.2608.30446. https://arxiv.org/abs/2608.30446"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RIEnet: End-to-End Neural Shrinkage of Indefinite Pairwise Correlation Matrices for Incomplete Return Panels

## Provenance

- **Primary Source:** Christian Bongiorno (Université Paris-Saclay, CentraleSupélec, Laboratoire de Mathématiques et Informatique pour la Complexité et les Systèmes) and Lorenzo Villassero (Université Paris-Saclay), *"End-to-End Neural Shrinkage of Indefinite Pairwise Correlation Matrices for Small-Cap-Inclusive Portfolios"*, arXiv preprint `arXiv:2608.30446v1 [q-fin.PM, q-fin.ST]`, published August 31, 2026. Full text: [https://arxiv.org/html/2608.30446v1](https://arxiv.org/html/2608.30446v1).
- **Primary Categories:** Portfolio Management (`q-fin.PM`), Statistical Finance (`q-fin.ST`).
- **Empirical Venue / Dataset:** Continuous 26-year point-in-time US equity simulation (January 4, 2000 – December 30, 2025; 6,537 trading sessions) covering up to 1,500 US common stocks and ADRs on NYSE, Nasdaq, and NYSE American.
- **Execution Simulation:** Institutional closing-auction simulator accounting for integer-share sizing, commissions (IBKR Pro tiered schedule), regulatory fees (SEC/FINRA), stock splits, cash dividends, corporate actions, borrowing/financing costs, and exchange/market-cap specific square-root market impact.

## Economic mechanism

### Source-reported

In quantitative portfolio construction (e.g. Global Minimum Variance or mean-variance optimization), universe definitions that include small-cap, recently listed (IPOs), intermittently traded, or temporarily suspended securities produce **incomplete (ragged) return panels**.

Standard practices face a severe dilemma:
1. **Complete-Case Deletion:** Discarding assets or truncating lookbacks to common dates discards massive historical information (in the evaluated 1,500-stock universe, $17.15\%$ of stock-rebalances have $< 1,200$ days of history, and $3.48\%$ have $< 252$ days).
2. **Pairwise-Complete Cross-Moments:** Estimating correlations on maximum pairwise overlaps preserves all data, but because each matrix entry $(i, j)$ is computed on a different sample subset and sample size $T_{ij}$, the resulting correlation matrix $\mathbf{C}_\cap$ is **indefinite** (possesses negative eigenvalues). This violates positive semidefiniteness, produces negative portfolio variances, and falls outside the scope of standard Random Matrix Theory (RMT) nonlinear shrinkage estimators (e.g. Ledoit-Wolf Quadratic Inverse Shrinkage / QIS).

Bongiorno and Villassero introduce **RIEnet for Incomplete Panels**, a dimension-agnostic, rotation-invariant neural covariance estimator. The network preserves the full pairwise spectrum, projects signed eigenvalues through a Bidirectional Gated Recurrent Unit (BiGRU) conditioned on factor-aligned effective sample lengths $\tau_k = \sum_{i,j} Q_{\cap,ik}^2 Q_{\cap,jk}^2 T_{ij}$, and directly outputs positive inverse eigenvalues $\lambda_{k, \text{NN}}^{-1} > 0$. The reconstructed covariance $\mathbf{\Sigma}_{\text{NN}}$ is guaranteed positive definite and is trained end-to-end to minimize realized out-of-sample 5-day GMV variance.

### Research interpretation

This architecture provides a breakthrough in high-dimensional risk modeling:
1. **End-to-End Gradient-Optimized Spectral Filtering:** Instead of performing heuristic ad-hoc two-step repairs (e.g. Higham nearest-correlation projection followed by linear shrinkage), RIEnet learns the optimal non-linear spectral distortion operator directly from downstream realized portfolio variance.
2. **Resolution of Ragged Data without Imputation Noise:** By conditioning the spectral transform on the exact factor-level overlap concentration ratio $q_k = n / \tau_k$, the model adaptively contracts noisy eigen-directions dominated by short-history assets while preserving genuine common risk factors.

## Signal

### 1. Marginally Standardized Pairwise Cross-Moment Matrix
Let $\mathbf{R} \in \mathbb{R}^{\Delta t_{\text{in}} \times n}$ be the ragged return panel with binary mask $\mathbf{M} \in \{0, 1\}^{\Delta t_{\text{in}} \times n}$.
- Overlap count matrix: $\mathbf{T} = \mathbf{M}^\top \mathbf{M}$.
- Marginal sample moments (full available history per asset):
  $$\bar{R}_i = \frac{1}{T_{ii}} \sum_{t=1}^{\Delta t_{\text{in}}} M_{ti} R_{ti}, \qquad \hat{\sigma}_i^2 = \frac{1}{T_{ii} - 1} \sum_{t=1}^{\Delta t_{\text{in}}} M_{ti} (R_{ti} - \bar{R}_i)^2$$
- Standardized pairwise cross-moment:
  $$C_{\cap, ij} = \frac{1}{T_{ij} - 1} \sum_{t=1}^{\Delta t_{\text{in}}} M_{ti} M_{tj} \left(\frac{R_{ti} - \bar{R}_i}{\hat{\sigma}_i}\right) \left(\frac{R_{tj} - \bar{R}_j}{\hat{\sigma}_j}\right) \quad (\text{with } C_{\cap, ii} = 1)$$
- Eigendecomposition: $\mathbf{C}_\cap = \mathbf{Q}_\cap \mathbf{\Lambda}_\cap \mathbf{Q}_\cap^\top$, where signed eigenvalues $\lambda_{\cap, 1} \le \ldots \le \lambda_{\cap, n}$ may include negative values.

### 2. Factor-Aligned Sample Information
For each spectral factor $k$, the effective sample length $\tau_k$ is the overlap matrix weighted by squared eigenvector loadings:
$$\tau_k = \sum_{i=1}^n \sum_{j=1}^n Q_{\cap, ik}^2 Q_{\cap, jk}^2 T_{ij}$$
Concentration ratio: $q_k = n / \tau_k$.

### 3. Neural Spectral Shrinkage (BiGRU)
Input token for factor $k$:
$$\mathbf{x}_k = \left[\lambda_{\cap, k}, \, \text{sign}(\lambda_{\cap, k}) \sqrt{|\lambda_{\cap, k}|}, \, \frac{k}{n}, \, q_k, \, \sqrt{q_k}, \, 1\right]^\top \in \mathbb{R}^6$$
Sequence processed by a 32-hidden-unit Bidirectional GRU:
$$\overrightarrow{\mathbf{h}}_k = \text{GRU}_{\text{fwd}}(\mathbf{x}_k, \overrightarrow{\mathbf{h}}_{k-1}), \qquad \overleftarrow{\mathbf{h}}_k = \text{GRU}_{\text{bwd}}(\mathbf{x}_k, \overleftarrow{\mathbf{h}}_{k+1})$$
Output inverse eigenvalue:
$$\lambda_{k, \text{NN}}^{-1} = \text{softplus}\left(\mathbf{w}^\top [\overrightarrow{\mathbf{h}}_k; \overleftarrow{\mathbf{h}}_k] + b\right) > 0$$

### 4. Positive-Definite Covariance Reconstruction
Rescaled eigenvectors: $\tilde{Q}_{\cap, ik} = Q_{\cap, ik} \sqrt{\lambda_{k, \text{NN}} / \sum_{m=1}^n Q_{\cap, im}^2 \lambda_{m, \text{NN}}}$.
Reconstructed correlation and covariance:
$$\mathbf{C}_{\text{NN}} = \tilde{\mathbf{Q}}_\cap \mathbf{\Lambda}_{\text{NN}} \tilde{\mathbf{Q}}_\cap^\top, \qquad \mathbf{\Sigma}_{\text{NN}} = \mathbf{D}_{\text{NN}} \mathbf{C}_{\text{NN}} \mathbf{D}_{\text{NN}}$$
where $\mathbf{D}_{\text{NN}} = \text{diag}(\hat{\sigma}_{1, \text{NN}}, \ldots, \hat{\sigma}_{n, \text{NN}})$ from the marginal volatility MLP branch.

### 5. Portfolio Construction
The regularized covariance $\mathbf{\Sigma}_{\text{NN}}$ is passed to the standard long-only GMV quadratic program:
$$\min_{\mathbf{w}} \mathbf{w}^\top \mathbf{\Sigma}_{\text{NN}} \mathbf{w} \quad \text{s.t.} \quad \sum_{i=1}^n w_i = 1, \quad w_i \ge 0$$
Weights are rounded to increments of $0.1\%$ and rebalanced every 5 trading days.

## Required data

- **Universe:** Point-in-time US Equities (NYSE, Nasdaq, NYSE American) up to 1,500 assets ranked by market cap.
- **Filters:** Price $\$10 \le P \le \$2,000$; shares outstanding $\ge 5\text{M}$; minimum 20-session history; cross-sectional IQR volatility filter.
- **Lookback Window:** $\Delta t_{\text{in}} = 1,200$ trading days (approx. 5 years).
- **Timeframe / Fields:** Daily split/dividend-adjusted close-to-close returns $R_{ti}$, volume, and binary observation mask $M_{ti}$.
- **Point-in-Time Separation:** Signal generated prior to closing auction without execution-day close lookahead.

## Execution assumptions

- **Execution Cadence:** Every 5 trading sessions (weekly rebalance).
- **Starting Capital:** USD 1,000,000 continuous portfolio simulation.
- **Fee Structure:** IBKR Pro tiered commissions (per-share tiered with $\$0.35$ minimum and $1.0\%$ notional cap) + SEC/FINRA transaction fees.
- **Financing:** Short cash financed at Federal Funds Effective Rate + 100 bps spread.
- **Market Impact Model:** Square-root closing auction model:
  $$\Delta P_{ti} = P_{ti} \cdot \kappa_{g(i, t)} \sqrt{\frac{|\Delta S_{ti}|}{\langle V_{ti} \rangle_{10\text{d}}}}$$
  with calibrated exchange/cap coefficients ($\kappa = 0.45\%$ to $2.66\%$).

## Evidence

### Source-reported

All metrics below are directly reported by Bongiorno & Villassero (arXiv:2608.30446v1, August 2026) across the 26-year out-of-sample period (2000–2025, 6,537 sessions) after full broker execution simulation:

#### 1. Out-of-Sample Performance Summary (2000–2025)
| Estimator | 5-Day Realized Vol (Ann.) | CAGR | Sharpe Ratio | Max Drawdown | Russell 1000 Beta | Median Positions |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **RIEnet (Proposed)** | **11.17%** | **9.30%** | **0.814** | **-41.3%** | **0.500** | 57.6 |
| **Factor (Imputation)** | 14.08% | 7.33% | 0.580 | -49.4% | 0.592 | 16.5 |
| **QIS (Quadratic Inverse)** | 14.41% | 8.07% | 0.560 | -54.9% | 0.799 | 754.1 |
| **Ridge (Sequential Reg)** | 14.43% | 6.70% | 0.528 | -52.4% | 0.589 | 16.6 |
| **Bootstrap (Anderson)** | 14.73% | 6.20% | 0.485 | -53.9% | 0.601 | 18.0 |
| **Anderson (Nearest Corr)**| 15.01% | 5.37% | 0.420 | -56.3% | 0.607 | 17.5 |
| **MLE (Sample Cov)** | 15.65% | 4.88% | 0.375 | -62.3% | 0.655 | 23.4 |
| **Equal Weight (Benchmark)**| 19.34% | 9.07% | 0.488 | -56.0% | 1.125 | 1500.0 |

#### 2. Statistical Significance & Model Confidence Set
- **Risk Reduction:** RIEnet achieves a **20.7% relative volatility reduction** over the next-best covariance estimator (Factor: 11.17% vs 14.08%).
- **Sharpe Improvement:** **+40.3% Sharpe ratio gain** over the next-best estimator (0.814 vs 0.580).
- **Model Confidence Set (MCS):** Using 10,000 stationary bootstrap replications (Hansen et al. 2011), RIEnet is the **only estimator retained in the 99.9% Model Confidence Set** across block lengths of 5, 10, 11, 20, and 40 days.

#### 3. Execution Drag & Turnover Analysis
- RIEnet incurs **$2.57$ bps market impact** and **$0.92$ bps explicit fees** per dollar traded ($1.49\%$ total CAGR drag).
- While QIS has lower drag ($1.17\%$), RIEnet delivers much lower net volatility ($11.17\%$ vs $14.41\%$) and higher net CAGR ($9.30\%$ vs $8.07\%$).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Computational Complexity of Neural Shrinkage:** Requires performing daily/weekly eigendecompositions of large matrices ($1,500 \times 1,500$) and evaluating the BiGRU forward pass.
- **Turnover vs Concentration Tradeoff:** Highly regularized models like QIS produce diffuse allocations (754 positions) with lower per-trade impact; RIEnet selects moderate concentration (57.6 effective positions), which requires monitoring liquidity in lower-cap assets to prevent capacity constraints.
- **Absence of Alpha Tilting in Benchmark:** The empirical test evaluates pure GMV; combining RIEnet with aggressive momentum or fundamental alpha signals has not been reported.

## Falsification plan

1. **Synthetic Noise Stress Test:** Generate synthetic multi-asset return panels where true covariance is identity $\mathbf{I}_n$ plus Gaussian noise with varying missingness fractions ($10\%$ to $50\%$). If RIEnet fails to beat linear shrinkage or nearest-correlation projection in estimating the ground-truth inverse covariance, the learned shrinkage mapping is falsified.
2. **Dimension Scaling Invariance Test:** Train RIEnet on $N=100$ assets and evaluate directly on $N=3,000$ assets without fine-tuning. If realized volatility degrades below sample covariance MLE, the dimension-agnostic parameterization hypothesis is falsified.
3. **Execution Cost Capacity Boundary:** Scale simulated portfolio AUM from $\$1\text{M}$ to $\$500\text{M}$. Identify the AUM scale at which market impact on the 57.6 selected positions erases the 20.7% volatility reduction advantage over Equal Weight / QIS.

## Crypto portability

- **Status:** Adapted / Unproven.
- **Research Interpretation:** The underlying research evaluated US equities. Porting RIEnet to cryptocurrency markets requires addressing:
  1. **Extreme Missingness / Listing Turnover:** Crypto asset universes (e.g. top 500 altcoins on Binance/Bybit or DEX tokens) exhibit extreme history fragmentation, newly launched tokens, and sudden delistings. Pairwise indefinite correlation matrices are pervasive in crypto panels.
  2. **Non-Stationary Volatility & Jumps:** Crypto returns exhibit fat-tailed jump diffusions and rough volatility ($H < 0.1$), requiring the marginal volatility branch MLP to incorporate jump-robust estimators or Parkinson/Garman-Klass volatility.
  3. **High Correlation Regime Spikes:** During systemic market liquidations (BTC crashes), cross-crypto correlations jump toward 1.0, stressing the BiGRU inverse spectrum mapper.

## Limitations

- **Long-Only GMV Focus:** Evaluated primarily on long-only Global Minimum Variance; long/short cross-sectional factor portfolios may exhibit different turnover dynamics.
- **Execution Model Dependency:** Assumes square-root market impact calibrated on US equity closing auctions.

## Implementation status

- `not-implemented`: Research capture only. No production implementation in PyBroker, Nautilus, Paper, Testnet, or Live systems.

## Adoption boundary

- `research-only`: Advanced covariance estimation and portfolio optimization research. Not approved for live fund allocation.

## Related Wiki records

- `[[quant/observable-matrix-dynamics-portfolio-optimization-2026-09-02]]`
- `[[quant/crypto-adaptive-trend-following-asymmetric-portfolio-2026-09-01]]`
- `[[quant/alpha-combination-breadth-executable-bridge-2026-08-28]]`

## Sources

1. Christian Bongiorno and Lorenzo Villassero, *"End-to-End Neural Shrinkage of Indefinite Pairwise Correlation Matrices for Small-Cap-Inclusive Portfolios"*, arXiv preprint `arXiv:2608.30446v1 [q-fin.PM, q-fin.ST]`, submitted August 31, 2026. DOI: [10.48550/arXiv.2608.30446](https://doi.org/10.48550/arXiv.2608.30446). Full text: [https://arxiv.org/html/2608.30446v1](https://arxiv.org/html/2608.30446v1).
2. Nicholas J. Higham, *"Computing the Nearest Correlation Matrix—A Problem from Finance"*, IMA Journal of Numerical Analysis 22(3): 329-343, 2002.
3. Olivier Ledoit and Michael Wolf, *"Analytical Nonlinear Shrinkage of Large-Dimensional Covariance Matrices"*, The Annals of Statistics 48(5): 3043-3065, 2020.
4. Peter R. Hansen, Asger Lunde, and James M. Nason, *"The Model Confidence Set"*, Econometrica 79(2): 453-497, 2011.
