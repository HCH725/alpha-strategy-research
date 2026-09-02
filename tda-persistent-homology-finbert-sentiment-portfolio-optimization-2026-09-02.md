---
schema: strategy-research-record-v1
title: "Topological Data Analysis and FinBERT News Sentiment Portfolio Optimization: Persistent Homology Filtering and Dynamic Rebalanced Mean-Variance"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - topological-data-analysis
  - persistent-homology
  - natural-language-processing
  - finbert
  - sentiment-analysis
  - portfolio-optimization
  - mean-variance
status: research-only
confidence: high
source_as_of: 2026-07-23
sources:
  - "Divyanee Garg, 'Portfolio Optimization under Dynamic Rebalancing via Topological Data Analysis and News Sentiments', arXiv preprint arXiv:2607.21170v1 [q-fin.PM], July 23, 2026. DOI: 10.48550/arXiv.2607.21170. Stable URL: https://arxiv.org/abs/2607.21170"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Topological Data Analysis and FinBERT News Sentiment Portfolio Optimization: Persistent Homology Filtering and Dynamic Rebalanced Mean-Variance

## Provenance

- **Primary Source:** Divyanee Garg (Indian Institute of Technology / academic preprint), *"Portfolio Optimization under Dynamic Rebalancing via Topological Data Analysis and News Sentiments"*, arXiv preprint `arXiv:2607.21170v1 [q-fin.PM]`, submitted July 23, 2026. DOI: [10.48550/arXiv.2607.21170](https://doi.org/10.48550/arXiv.2607.21170). Stable URL: [https://arxiv.org/abs/2607.21170](https://arxiv.org/abs/2607.21170).
- **Primary Subject Area:** Portfolio Management (`q-fin.PM`).
- **Context & Motivation:** Traditional portfolio diversification models rely on Pearson correlation or Euclidean distance to group and select assets. However, linear correlation assumes Gaussian return distributions and fails during non-linear dependency regimes, extreme co-movements, or market crashes. Furthermore, univariate return series fail to capture market sentiment and behavioral shifts that precede price trends. Garg introduces a two-stage active management framework: (1) constructing a natural 4-dimensional point cloud per asset using technical indicators (RSI, Stochastic Oscillator, MACD) augmented with firm-level financial news sentiment extracted via FinBERT; (2) computing multi-scale topological features via Vietoris–Rips persistent homology ($H_0$ connected components and $H_1$ 1-dimensional loops); (3) clustering assets with Average Wasserstein Distance (AWD) on Persistence Diagrams (PD) or Average Persistence Landscape (APL) $L^p$ distance; and (4) allocating capital across the filtered asset subset using a Dynamic Rebalancing Mean-Variance (DRMV) model subject to transaction costs, turnover penalties, holding bounds, and an asset-retention mechanism.

## Economic mechanism

### Source-reported

1. **Multidimensional Behavioral and Technical Representation:** Historical price indicators (RSI, SO, MACD) reflect past momentum and mean-reversion pressure, while FinBERT news sentiment captures real-time investor attention, forward-looking expectations, and behavioral shifts not yet fully reflected in asset prices. Combining them into a 4D point cloud eliminates the need for heuristic artificial phase-space reconstructions (e.g., Takens' delay embedding).
2. **Topological Invariant Asset Filtering:** Persistent homology tracks the birth and death of geometric features (connected components $H_0$ and topological loops $H_1$) across Vietoris–Rips filtration scales $\epsilon$. Assets that share similar return distributions can still exhibit radically different non-linear geometric loops and voids. Clustering by topological distance groups structurally similar assets, enabling the selection of topologically dissimilar assets from different clusters to achieve true diversification.
3. **Dynamic Rebalancing with Asset Retention:** Frequent rebalancing (3-day, 5-day, 10-day) captures short-lived sentiment shocks. However, unconstrained rebalancing induces excessive turnover. An asset-retention mechanism explicitly penalizes changes between current allocations and previous weights $w_{t-1}$, dynamically mitigating transaction-cost drag while preserving high-Sharpe assets across consecutive windows.

### Research interpretation

The falsifiable thesis is that **filtering an equity or multi-asset investment universe using persistent homology distances on joint technical-sentiment point clouds generates higher risk-adjusted returns (Sharpe, STARR, Sterling) and lower drawdowns during market stress than full-universe Markowitz or correlation-clustered portfolios**:
- The non-linear loop structure ($H_1$) detects cyclic co-movement and transient structural patterns that Pearson correlation overlooks.
- In stressed regimes (such as geopolitical conflicts), naive and market-cap benchmarks experience broad correlation breakdown toward 1.0, whereas topologically distinct assets provide decorrelated return drivers.

## Signal

### 1. 4D Point Cloud Feature Construction

For each asset $i \in \{1, \dots, N_{\text{univ}}\}$ and in-sample lookback trading day $t_1 \in \{1, \dots, T_1\}$, construct the 4-dimensional feature vector:
$$Z_{t_1}^i = \left( \operatorname{RSI}_{t_1}^i, \, \operatorname{SO}_{t_1}^i, \, \operatorname{MACD}_{t_1}^i, \, S_{t_1}^i \right)^\top \in \mathbb{R}^4$$
where:
- $\operatorname{RSI}_{t_1}^i$: 14-day Relative Strength Index.
- $\operatorname{SO}_{t_1}^i$: Stochastic Oscillator $\%K$ and $\%D$ indicator.
- $\operatorname{MACD}_{t_1}^i$: Moving Average Convergence Divergence difference line (12-day EMA minus 26-day EMA).
- $S_{t_1}^i$: Daily average sentiment score extracted from firm-level financial news headlines via FinBERT:
  $$S_t = P_{\text{pos}} - P_{\text{neg}}$$
  where $P_{\text{pos}}$ and $P_{\text{neg}}$ are posterior probabilities from FinBERT. For non-trading days, news sentiment is rolled to the next active trading session.
- Standardization: Continuous features are standardized across the in-sample window $T_1$ to eliminate scale bias prior to filtration.

### 2. Vietoris–Rips Filtration and Persistent Homology

For asset point cloud $\mathcal{Z}_i = \{Z_{t_1}^i\}_{t_1=1}^{T_1} \subset \mathbb{R}^4$, construct the Vietoris–Rips simplicial complex $R(\mathcal{Z}_i, \epsilon)$ across increasing scale parameter $\epsilon > 0$:
- An edge between points $z_a, z_b \in \mathcal{Z}_i$ is formed if $\|z_a - z_b\| < 2\epsilon$.
- An $m$-simplex is included if all pairwise vertex distances are $< 2\epsilon$.
- Compute homology groups: $H_0$ (connected components) and $H_1$ (1-dimensional cycles/loops).
- Record birth scale $b$ and death scale $d$ for each topological feature, yielding the Persistence Diagram (PD) $\mathcal{D}_{\mathcal{Z}_i} = \{(b_k, d_k)\}_{k=1}^K$ with $0 \le b_k \le d_k$.

### 3. Topological Dissimilarity Measures

Two alternative topological distance formulations are evaluated:

1. **Average Wasserstein Distance (AWD) on PDs:**
   $$d_{W,p}(\mathcal{D}_{\mathcal{Z}_i}, \mathcal{D}_{\mathcal{Z}_j}) = \inf_{\gamma} \left( \sum_{u \in \mathcal{D}_{\mathcal{Z}_i}} \|u - \gamma(u)\|_\infty^p \right)^{1/p}$$
   The AWD is the average of Wasserstein distances across dimensions $r \in \{0, 1\}$:
   $$\operatorname{AWD}(i, j) = \frac{1}{2} \left( d_{W,p}^{(0)}(\mathcal{D}_{\mathcal{Z}_i}, \mathcal{D}_{\mathcal{Z}_j}) + d_{W,p}^{(1)}(\mathcal{D}_{\mathcal{Z}_i}, \mathcal{D}_{\mathcal{Z}_j}) \right)$$

2. **Average Persistence Landscape (APL) Distance:**
   Transform birth-death pairs into triangular functions $\Lambda_{(b, d)}(t) = \max(0, \min(t - b, d - t))$. The $k$-th landscape function $\zeta_k(t)$ is the $k$-th largest value of $\{\Lambda_{(b_i, d_i)}(t)\}$. The $L^p$ distance between landscapes $\zeta^i$ and $\zeta^j$ is:
   $$\|\zeta^i - \zeta^j\|_p = \left( \sum_{k=1}^\infty \int_\mathbb{R} |\zeta_k^i(t) - \zeta_k^j(t)|^p dt \right)^{1/p}$$
   The APL distance averages over homology dimensions $r \in \{0, 1\}$.

### 4. Agglomerative Clustering and In-Cluster Sharpe Selection

- Form pairwise distance matrix $D \in \mathbb{R}^{N_{\text{univ}} \times N_{\text{univ}}}$ using AWD or APL.
- Apply agglomerative hierarchical clustering with Ward's or average linkage.
- Asset Filtering Rule:
  - Clusters with size $n_c = 1$ are treated as outliers and discarded.
  - For clusters with $n_c \ge 2$, rank assets by in-sample Sharpe ratio in descending order.
  - Select top $k_c = \lceil \rho n_c \rceil$ assets, where selection ratio $\rho = 0.10$ (top 10%).
  - The filtered investment universe $\mathcal{S}_t = \bigcup_{c} \mathcal{S}_{t,c}$ forms a sparse, diversified candidate pool.

### 5. Dynamic Rebalanced Mean-Variance (DRMV) Optimization

At rebalancing epoch $t$, solve the constrained convex program over filtered set $\mathcal{S}_t$:
$$\min_{w_t} \quad w_t^\top \Sigma_t w_t - \lambda_{\text{risk}} \mu_t^\top w_t + c_{\text{cost}} \sum_{i \in \mathcal{S}_t} |w_{t,i} - w_{t-1,i}^+|$$
subject to:
$$w_t^\top \mathbf{1} = 1$$
$$l_i \le w_{t,i} \le u_i, \quad \forall i \in \mathcal{S}_t \quad (\text{long-only box constraints: } l_i = 0, u_i = 0.10)$$
$$w_{t,j} = 0, \quad \forall j \notin \mathcal{S}_t$$
where $w_{t-1,i}^+$ is the drifted asset weight prior to rebalancing, $c_{\text{cost}}$ is the proportional transaction cost penalty, and $\lambda_{\text{risk}}$ is the risk-tolerance parameter corresponding to confidence levels $\alpha \in \{0.95, 0.99\}$.

## Required data

- **Universe:** S&P 500 constituents (cross-sectional equity universe).
- **Timeframe:** Daily open, high, low, close prices; rebalancing cadence evaluated at 3-day, 5-day, and 10-day intervals.
- **Lookback Window:** $T_1 = 3$ months (approx. 63 trading days) rolling in-sample estimation window.
- **News Headline Stream:** Firm-level financial news headlines obtained via Refinitiv Eikon / LSEG Workspace API.
- **NLP Model:** Pre-trained FinBERT model for sentence-level financial sentiment inference ($P_{\text{pos}}, P_{\text{neg}}, P_{\text{neu}}$).
- **Benchmark Proxies:** Naive equal-weight ($1/N$), S&P 500 market index (SPY), Buy-and-Hold sentiment/indicator portfolios ($\text{B\&H}_S$, $\text{B\&H}_I$).

## Execution assumptions

- **Rebalancing Cadence:** Discrete multi-day execution at 3-day, 5-day, and 10-day horizons.
- **Execution Price:** Market close or next-day opening price.
- **Transaction Costs:** Proportional transaction costs evaluated at 10 bps ($0.10\%$), penalizing weight turnover $|w_{t,i} - w_{t-1,i}^+|$.
- **Portfolio Constraints:** Long-only simplex ($w \ge 0, \sum w_i = 1$), maximum individual asset holding cap $u_i = 10\%$, no short-selling.
- **Asset Retention:** Dynamic retention mechanism retains overlapping assets between successive rebalancing windows, suppressing unnecessary turnover.

## Evidence

### Source-reported

All quantitative figures below are directly reported by Divyanee Garg (arXiv:2607.21170v1, July 2026):

1. **Full-Year Rolling Out-of-Sample Performance (January 2025 – December 2025):**
   - **3-Day Rebalancing Horizon ($\alpha = 0.95$):**
     - $(\text{DRMV})_{\text{APLS}}$ (Average Persistence Landscape with Sentiment) achieved a Cumulative Return (CR) of **2.18968**, attaining the highest mean return, Sharpe Ratio (SR), STARR ratio, and Sterling ratio across all tested sentiment-based models.
     - $(\text{DRMV})_{\text{AWDS}}$ (Average Wasserstein Distance with Sentiment) ranked second in return and risk-adjusted metrics.
     - Both TDA-sentiment models statistically significantly outperformed indicator-only models ($(\text{DRMV})_{\text{APLI}}$, $(\text{DRMV})_{\text{AWDI}}$), correlation-filtered models ($(\text{DRMV})_{\text{ACS}}$, $(\text{DRMV})_{\text{ACI}}$), Euclidean-filtered models ($(\text{DRMV})_{\text{AES}}$, $(\text{DRMV})_{\text{AEI}}$), and the full-universe benchmark without clustering $(\text{DRMV})_A$ (confirmed via one-sided bootstrap $t$-tests and Sharpe tests at $p < 0.05$).
   - **Horizon Decay Across Rebalancing Frequencies ($\alpha = 0.95$):**
     - Cumulative return for $(\text{DRMV})_{\text{APLS}}$ decreased monotonically as rebalancing frequency was reduced: **2.18968** (3-day) $\to$ **2.04184** (5-day) $\to$ **1.92273** (10-day).
     - Higher rebalancing frequency successfully exploits short-lived market sentiment shocks, though it incurs higher gross transaction costs.
   - **Benchmark Comparison (Table 7 vs Tables 4–6):**
     - All filtering-based DRMV strategies significantly outperformed passive benchmarks: Naïve ($1/N$), Market Index, and Buy-and-Hold ($\text{B\&H}_S$, $\text{B\&H}_I$).

2. **Geopolitical Stress Window Performance (U.S.–Israel–Iran Conflict, October 2025 – March 2026):**
   - Stress Evaluation Period: January 2026 to March 2026 out-of-sample holding.
   - Benchmark Failures: Naïve ($1/N$) and Market Index portfolios generated **negative average returns** over this crisis window.
   - Robustness of TDA-Sentiment Models:
     - Under $\alpha = 0.95$, $(\text{DRMV})_{\text{AWDS}}$ achieved the highest mean return, maximum return, and cumulative return, while $(\text{DRMV})_{\text{APLS}}$ delivered the highest Sharpe and STARR ratios.
     - Under $\alpha = 0.99$, $(\text{DRMV})_{\text{APLS}}$ achieved the highest mean return, SR, STARR, and cumulative return.
     - All proposed TDA filtering strategies delivered strictly positive returns and positive risk-adjusted performance throughout the conflict period.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- None identified in the reviewed paper; absence is not evidence of no negative result.
- Author notes that sentiment-enhanced strategies exhibit a marginal increase in volatility compared to conservative Euclidean distance filtering ($(\text{DRMV})_{\text{AES}}$), which yielded smaller Maximum Drawdown (MDD) and Average Drawdown (ADD) at the expense of lower returns.
- More frequent rebalancing (3-day) generates substantially higher turnover, increasing transaction-cost drag if executed with taker fees.

## Falsification plan

1. **Ablation of News Sentiment ($S_t = 0$):** Run identical TDA pipeline using only 3D technical point clouds (RSI, SO, MACD). If the 3D model matches or exceeds the 4D sentiment-augmented model in out-of-sample Sharpe ratio net of transaction costs, the NLP sentiment alpha thesis is falsified.
2. **Topological vs. Random Clustering Placebo:** Replace persistent homology distance matrices with random cluster assignments while retaining the top-10% Sharpe filtering rule. If random clustering matches TDA risk-adjusted performance, topological structure provides zero true filtering signal.
3. **Execution Cost Sensitivity Stress:** Escalate proportional transaction costs from $10\text{ bps}$ to $25\text{ bps}$ and $50\text{ bps}$. If net returns of the 3-day rebalancing strategy fall below the 10-day rebalancing strategy or below the buy-and-hold benchmark, the strategy overfits to zero/low transaction-friction regimes.
4. **Rejection Threshold:** Reject the strategy if the out-of-sample Sharpe ratio under 5-day rebalancing fails to exceed the passive S&P 500 ETF (SPY) buy-and-hold Sharpe ratio over a 2-year backtest.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Textual Sentiment Extraction in Crypto:** Financial news headline coverage for mid-cap crypto tokens is sparse and dominated by promotional PR, clickbait, and bot-generated noise. FinBERT must be fine-tuned on crypto-native corpora (e.g., Crypto-BERT on Twitter/X, Telegram, and Discord) or replaced with on-chain metric feeds.
- **Point Cloud Dimensionality:** The 4D representation can be ported to crypto by combining technical oscillators (RSI, funding-rate z-score, open interest momentum) with social sentiment.
- **High Friction & Turnover Drag:** Given higher crypto taker fees ($4\text{ to }6\text{ bps}$) and volatile spreads, a 3-day rebalancing cadence will incur severe fee drag. The rebalancing window must be lengthened (e.g., weekly) or conditioned on threshold triggers.

## Limitations

- **News Availability Bias:** The empirical sample relies on large-cap S&P 500 equities with abundant institutional news coverage via Refinitiv; illiquid equities or small-cap assets with sparse headlines suffer from stale sentiment scores ($S_t = 0$).
- **Computational Complexity of Persistence Homology:** Computing Vietoris–Rips filtrations scales cubically with the number of time points in the point cloud ($O(T_1^3)$). Expanding $T_1$ beyond 3 months causes noticeable preprocessing latency.
- **Hyperparameter Dependency:** The cluster filtering proportion $\rho = 0.10$ and minimum cluster size $n_c \ge 2$ are fixed heuristically without multi-regime cross-validation.

## Implementation status

`not-implemented` in the quantitative production stack.

## Adoption boundary

Research capture only. A record being present in this repository does not constitute authorization for deployment, implementation in PyBroker/Nautilus, or allocation of capital in paper, testnet, or live trading.

## Related Wiki records

- `[[quant/foreign-exchange-spatiotemporal-graph-statistical-arbitrage-2026-09-02]]`
- `[[quant/equity-analyst-coverage-network-graph-attention-momentum-spillover-2026-09-02]]`
- `[[quant/loop-gain-matrix-letf-rebalancing-crypto-closing-pressure-2026-09-02]]`

## Sources

1. Divyanee Garg, *"Portfolio Optimization under Dynamic Rebalancing via Topological Data Analysis and News Sentiments"*, arXiv preprint `arXiv:2607.21170v1 [q-fin.PM]`, July 23, 2026. DOI: [10.48550/arXiv.2607.21170](https://doi.org/10.48550/arXiv.2607.21170). Stable URL: [https://arxiv.org/abs/2607.21170](https://arxiv.org/abs/2607.21170).
