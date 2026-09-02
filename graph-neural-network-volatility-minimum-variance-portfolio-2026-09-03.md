---
schema: strategy-research-record-v1
title: "Cross-Sectional Volatility Forecasting and Minimum-Variance Portfolio Construction via Macro-Conditioned Graph Neural Networks"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - volatility-forecasting
  - graph-neural-networks
  - portfolio-optimization
  - minimum-variance
  - cross-sectional
status: research-only
confidence: medium
source_as_of: 2026-05-19
sources:
  - "https://arxiv.org/abs/2605.19278"
  - "https://doi.org/10.48550/arXiv.2605.19278"
  - "https://github.com/waderylan/sp500-gnn/commit/31768802d0e2581085a303e78b4d83c04f7b5253"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The primary source evaluates equity volatility over 465 current S&P 500 constituents (2015-2025), introducing index survivorship bias. Furthermore, while macro-conditioned GNNs deliver superior minimum-variance Sharpe ratios (up to 0.984 vs 0.635 for HAR), they fail to beat passive benchmarks in inverse-volatility weighting, produce negative excess returns under volatility targeting, and suffer severe losses under long-short volatility ranking (Sharpe -1.137 to -1.779), establishing that statistical forecast accuracy, ranking quality, and portfolio optimization utility decouple across different execution rules."
---

# Cross-Sectional Volatility Forecasting and Minimum-Variance Portfolio Construction via Macro-Conditioned Graph Neural Networks

## Provenance

- **Primary Source:** Rylan Wade (Department of Industrial and Systems Engineering, University of Southern California), *"Do Better Volatility Forecasts Lead to Better Portfolios? Evidence from Graph Neural Networks"*, arXiv preprint `arXiv:2605.19278v2 [q-fin.PM]`, revised May 19, 2026.
- **Canonical arXiv URL:** [https://arxiv.org/abs/2605.19278](https://arxiv.org/abs/2605.19278)
- **Canonical DOI:** [https://doi.org/10.48550/arXiv.2605.19278](https://doi.org/10.48550/arXiv.2605.19278)
- **Primary Source Code Implementation:** [https://github.com/waderylan/sp500-gnn](https://github.com/waderylan/sp500-gnn)
  - **Immutable Commit SHA:** `31768802d0e2581085a303e78b4d83c04f7b5253`
  - **Core Implementation Files:** `src/models.py`, `src/portfolio.py`, `src/graphs.py`, `src/features.py`, `config.py`.
- **Direct Audit:** The complete LaTeX source package (`main.tex`, `custom.bib`) and the full Python implementation repository were directly retrieved, unpacked, and audited. Every quantitative metric, hyperparameter, model topology, and empirical finding cited in this record traces directly to the author's primary text and code.
- **Deduplication Check:** An exhaustive search against all repository records and Hermes Wiki Brain confirmed zero prior captures of `2605.19278`, author Rylan Wade, or the `waderylan/sp500-gnn` codebase.

## Economic mechanism

### Source-reported

Realized volatility in equity markets exhibits strong persistence and clustering, but shocks do not occur in isolation. When turbulence impacts an individual firm, it propagates through sector peers, correlated counterparty positions, and broader market connections before reflecting in that stock's own lagged price history. Traditional univariate volatility models—such as the Heterogeneous Autoregressive (HAR-RV) model or univariate Long Short-Term Memory (LSTM) networks—model each asset's volatility autoregressively and cannot explicitly propagate cross-sectional contagion.

Graph Neural Networks (specifically GraphSAGE) can represent equities as nodes and economic/statistical relationships as edges, allowing neighborhood feature aggregation to condition each stock's volatility forecast on the recent behavior of linked neighbors. However, graph structure is only beneficial if edges represent relationships that remain informative out-of-sample:
1. **Dynamic return correlations** track live co-movement and volatility contagion, but during crisis regimes the graph becomes hyper-dense (e.g., density rising from 0.092 to 0.933 during the March 2020 COVID shock), causing GNN representations to oversmooth and compress cross-sectional variance.
2. **Fixed GICS sector classifications** provide stable structural boundaries that prevent oversmoothing, but lag dynamic market shifts.
3. **Directed Granger causality** captures asymmetric lead-lag volatility spillovers, but assumes static relationships that can decay when market regimes shift.
4. **Macro-regime features** (VIX, credit spreads, Treasury slope) provide market-wide state awareness, preventing graph models from misinterpreting idiosyncratic shocks as broad systemic crises.

Crucially, the author reports a core empirical insight: **the model with the lowest forecast MSE (GNN-Correlation + Macro 63d, MSE = 0.0298), the model with the highest cross-sectional ranking accuracy (GNN-Ensemble + Macro, Rank IC = 0.438), and the model with the highest portfolio Sharpe ratio (GNN-Sector + Macro, Sharpe = 0.984) are three distinct models**. Statistical forecast accuracy does not automatically translate into economic portfolio value unless the portfolio construction mechanism directly exploits the cross-sectional dispersion captured by the model.

### Research interpretation

The strategy operates as a **cross-sectional volatility-dispersion and risk-budgeting engine**:
- **Information Propagation Channel:** GraphSAGE aggregates 1-hop neighbor embeddings, effectively computing a localized spatial moving average of cross-sectional risk. When coupled with macro regime features, the node representations separate market-wide risk shocks from idiosyncratic firm-level volatility.
- **Covariance Structuring for Minimum Variance:** When used to parameterize the diagonal of a covariance matrix ($\Sigma = D_{\hat{\sigma}} C D_{\hat{\sigma}}$) in a constrained minimum-variance quadratic program, the GNN's forward-looking dispersion estimates enable the optimizer to down-weight stocks prior to volatility spikes while keeping portfolio turnover low (0.406 vs 1.012 for HAR).
- **Decoupling of Ranking from Directional Alpha:** In long-short volatility portfolios (buying the lowest-volatility quintile and shorting the highest-volatility quintile), the strategy fails catastrophically (Sharpe -1.137 to -1.779) during regimes where high-volatility equities (such as mega-cap tech and AI beneficiaries) simultaneously drive market returns. Volatility ranking is a risk-allocation signal, not a standalone return predictor.

## Signal

### Prediction Target

- **Target Variable:** One-week-ahead realized volatility ($RV_{t+1}$), defined as the annualized standard deviation of daily log returns within calendar week $t+1$ (Monday through Friday):
  $$\sigma_{i, t+1} = \sqrt{252} \cdot \sqrt{\frac{1}{K-1} \sum_{k=1}^K \left(r_{i, k} - \bar{r}_i\right)^2}$$
  where $K$ is the number of trading days in week $t+1$ (weeks with $K < 3$ trading days are excluded).
- **Observation & Execution Timing:** Features are computed through Friday close of week $t$. Predictions are generated over the weekend and applied to portfolio rebalancing at the open of Monday in week $t+1$.

### Feature Space

At each week $t$, every stock $i \in \{1, \dots, N\}$ has a 10-dimensional feature vector:
1. **Realized Volatilities:** Trailing RV over 5, 10, 21, and 63 trading days.
2. **Volatility Ratio:** Short-to-long ratio ($RV_{5d} / RV_{63d}$), capturing short-term volatility spikes relative to baseline.
3. **Momentum:** 5-day and 20-day cumulative price momentum.
4. **Volume Dynamics:** Log-transformed 5-day and 20-day rolling volume, and the volume ratio ($Vol_{5d} / Vol_{20d}$).
5. **Feature Normalization:** Cross-sectionally winsorized at the 1st and 99th percentiles each week, then z-scored across all stocks. Outliers post-z-score clipped to $[-6.0, 6.0]$.

### Macro & Regime Context Features

A 7-dimensional macro feature vector shared across all nodes:
1. VIX index closing level and 1-week change ($\Delta VIX$).
2. SPY realized volatility over 21 trading days and SPY 1-week return.
3. 10-Year minus 2-Year U.S. Treasury yield spread (FRED series `T10Y2Y`).
4. U.S. Corporate Investment Grade option-adjusted credit spread (ICE BofA).
5. Average pairwise return correlation across all $N$ stocks over the trailing 63 days.
6. Graph density of the correlation network under the $|\rho| \ge 0.30$ threshold.
7. Macro features are normalized using in-sample (2015–2022) training statistics.

### Graph Construction Topologies

1. **GNN-Correlation (Dynamic):** Undirected edge between stock $i$ and $j$ if their rolling Pearson return correlation $|\rho_{ij}| \ge 0.30$. Evaluated over lookback windows $W \in \{21, 63, 126, 252\}$ trading days. Recomputed each week.
2. **GNN-Sector (Static/Annual):** Undirected edge between stocks belonging to the same GICS sector (11 sectors). Reclassified annually.
3. **GNN-Granger (Static/Directed):** Directed edge from stock $i \to j$ if stock $i$'s 5-day lagged returns Granger-cause stock $j$'s returns at $p < 0.05$ after Bonferroni correction over the 2015–2022 training period (yielding 13,886 directed edges). Edge directionality is preserved during message passing via `SAGEConv(..., flow="source_to_target")`.
4. **GNN-Ensemble:** Weighted linear combination of predictions from Correlation, Sector, and Granger models, weighted inversely by their 2023 validation MSE.

### Neural Network Architecture & Training

- **Backbone:** 3-layer GraphSAGE architecture.
- **Hidden Dimension:** 256 units per layer.
- **Activation & Regularization:** ReLU activations, Dropout $p = 0.30$.
- **Normalization:** No BatchNorm (BatchNorm was shown to collapse cross-sectional variance across node embeddings, degrading Rank IC).
- **Optimizer:** Adam with learning rate $\eta = 10^{-3}$.
- **Loss Function:** Mean Squared Error on standardized volatility targets:
  $$\mathcal{L}_{\text{MSE}} = \frac{1}{N} \sum_{i=1}^N \left(\hat{\sigma}_{i, t+1} - \sigma_{i, t+1}\right)^2$$
- **Training Strategy:** 2015–2022 training split, early stopping with patience of 10 epochs based on 2023 validation MSE. Maximum epochs = 150.

### Portfolio Allocation Construction (Minimum Variance)

Given predicted volatilities $\hat{\sigma}_{t+1} \in \mathbb{R}^N$ and realized correlation matrix $C_t \in \mathbb{R}^{N \times N}$ computed over trailing 252 days:
1. Construct the synthetic covariance matrix:
   $$\hat{\Sigma}_{t+1} = \text{diag}(\hat{\sigma}_{t+1}) \cdot C_t \cdot \text{diag}(\hat{\sigma}_{t+1})$$
2. Solve the constrained quadratic program:
   $$\min_{w_{t+1}} w_{t+1}^\top \hat{\Sigma}_{t+1} w_{t+1} \quad \text{subject to} \quad \sum_{i=1}^N w_{i, t+1} = 1, \quad 0 \le w_{i, t+1} \le 0.05$$
3. Quadratic optimization is solved using the OSQP operator-splitting solver. Post-solve weights are clipped to $[0, 0.05]$ and re-normalized to enforce $\sum w_i = 1$.

## Required data

- **Universe:** 465 liquid U.S. equities selected from S&P 500 constituents with $\ge 95\%$ trading-day coverage from January 1, 2015, through December 31, 2025.
- **Data Source:** Daily OHLCV equity bars from Yahoo Finance (`yfinance`); risk-free benchmark from Federal Reserve Economic Data (FRED 3-month Treasury bill rate `DTB3`).
- **Macro Inputs:** Daily VIX index, SPY ETF, 10Y–2Y Treasury constant maturity spread, and Moody's BAA/AAA corporate credit spreads.
- **Timeframe:** Daily price bars aggregated to Monday-anchored calendar weeks.
- **Point-in-Time Discipline:** Features at week $t$ use data strictly through Friday close of week $t$. Weekly rebalance occurs on Monday open of week $t+1$.
- **Missing Data Handling:** Non-positive or NaN predicted volatilities are floored to $10^{-6}$ prior to covariance matrix construction. Features missing $< 5\%$ are imputed with zero post-z-scoring (sample mean).

## Execution assumptions

- **Execution Cadence:** Weekly rebalance on Monday market open.
- **Transaction Costs:** 10 basis points (0.10%) one-way transaction cost applied per unit of portfolio turnover:
  $$\text{Cost}_t = 0.0010 \times \sum_{i=1}^N |w_{i, t} - w_{i, t}^-|$$
  where $w_{i, t}^-$ is the portfolio weight drift just before rebalancing.
- **Position Constraints:** Long-only ($\sum w_i = 1, w_i \ge 0$), maximum single-stock weight cap of 5.0% ($w_i \le 0.05$).
- **Benchmark Risk-Free Rate:** Subtracted using the prevailing FRED 3-month Treasury bill rate (`DTB3`) to compute annualized Sharpe ratios.
- **Slippage & Market Impact:** Not modeled in the primary source beyond the 10 bps fixed cost. Capacity and market-impact decay are marked as provenance gaps.

## Evidence

### Source-reported

All empirical results below are directly reported by Rylan Wade (arXiv:2605.19278v2, May 2026) evaluated over **103 out-of-sample test weeks from January 2024 through December 2025**:

#### 1. Statistical Forecast Accuracy & Ranking (103 Test Weeks)

| Model | Forecast MSE | Forecast MAE | $R^2$ | Directional Acc. | Mean Rank IC | ICIR |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **HAR (per-stock baseline)** | 0.0329 | 0.1129 | 0.131 | 0.707 | 0.405 | 3.473 |
| **HAR (pooled baseline)** | 0.0331 | 0.1133 | 0.124 | 0.703 | 0.392 | 3.437 |
| **LSTM (univariate baseline)** | 0.0324 | 0.1096 | 0.142 | 0.709 | 0.429 | **4.363** |
| **GNN-Correlation (no macro)** | 0.0322 | 0.1076 | 0.148 | 0.712 | 0.417 | 3.440 |
| **GNN-Sector (no macro)** | 0.0336 | 0.1208 | 0.110 | 0.682 | 0.383 | 3.399 |
| **GNN-Granger (no macro)** | 0.0337 | 0.1190 | 0.108 | 0.688 | 0.375 | 3.663 |
| **GNN-Ensemble (no macro)** | 0.0320 | 0.1127 | 0.153 | 0.700 | 0.416 | 3.577 |
| **GNN-Corr + Macro 21d** | 0.0311 | 0.1043 | 0.177 | **0.725** | 0.412 | 3.915 |
| **GNN-Corr + Macro 63d** | **0.0298** | **0.1042** | **0.210** | 0.722 | 0.426 | 3.657 |
| **GNN-Corr + Macro 126d** | 0.0321 | 0.1080 | 0.150 | 0.719 | 0.415 | 3.525 |
| **GNN-Corr + Macro 252d** | 0.0309 | 0.1070 | 0.183 | 0.720 | 0.429 | 3.680 |
| **GNN-Sector + Macro** | 0.0315 | 0.1107 | 0.166 | 0.704 | 0.428 | 3.850 |
| **GNN-Granger + Macro** | 0.0314 | 0.1077 | 0.168 | 0.714 | 0.429 | 4.064 |
| **GNN-Ensemble + Macro** | 0.0316 | 0.1073 | 0.164 | 0.715 | **0.438** | 3.935 |

#### 2. Portfolio Performance Comparison Across Four Allocation Rules

##### A. Minimum-Variance Portfolios (10 bps transaction cost, max 5% weight cap)

| Strategy Specification | Annualized Return | Annualized Volatility | Sharpe Ratio | Maximum Drawdown | Average Weekly Turnover |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **HAR (per-stock)** | 0.113 | 0.099 | 0.635 | -0.127 | 1.012 |
| **HAR (pooled)** | 0.124 | 0.102 | 0.729 | -0.119 | 0.913 |
| **LSTM** | 0.112 | 0.110 | 0.564 | -0.114 | 0.591 |
| **GNN-Correlation (no macro)** | 0.118 | 0.118 | 0.581 | -0.128 | 0.606 |
| **GNN-Sector (no macro)** | 0.104 | 0.110 | 0.492 | -0.089 | 0.533 |
| **GNN-Granger (no macro)** | 0.096 | 0.112 | 0.412 | -0.130 | 0.676 |
| **GNN-Corr + Macro 21d** | 0.137 | 0.105 | 0.828 | -0.103 | 0.720 |
| **GNN-Corr + Macro 63d** | 0.133 | 0.105 | 0.794 | **-0.092** | 0.670 |
| **GNN-Sector + Macro** | **0.153** | 0.104 | **0.984** | -0.097 | 0.406 |
| **GNN-Granger + Macro** | **0.156** | 0.109 | **0.973** | -0.101 | 0.499 |
| **GNN-Ensemble + Macro** | 0.149 | 0.109 | 0.914 | -0.099 | **0.357** |

##### B. Inverse-Volatility Weighting ($w_i \propto 1/\hat{\sigma}_i$)

- **Equal-Weight Baseline:** Annual Return = 12.0%, Annual Vol = 13.7%, **Sharpe = 0.513**, Max DD = -17.1%, Turnover = 0.000.
- **HAR per-stock:** Annual Return = 10.0%, Annual Vol = 12.6%, Sharpe = 0.396, Max DD = -15.5%, Turnover = 0.163.
- **GNN-Sector + Macro (best GNN):** Annual Return = 11.0%, Annual Vol = 12.9%, **Sharpe = 0.468**, Max DD = -15.9%, Turnover = 0.050.
- **Result:** **No model beats passive Equal Weight under inverse-volatility allocation.**

##### C. Volatility-Targeted Portfolios (10% Annualized Target)

- All models produced **negative Sharpe ratios** after subtracting the risk-free rate (ranging from -0.085 for GNN-Corr+Macro 21d to -0.365 for GNN-Corr+Macro 126d; HAR per-stock = -0.219).
- **Result:** Volatility targeting underperformed passive cash holding during the 2024–2025 high-interest-rate environment.

##### D. Long-Short Volatility Portfolios (Long Q1 Calm, Short Q5 Turbulent)

- All models produced **severe negative returns and drawdowns**:
  - GNN-Correlation (no macro): Return = -26.4%, Vol = 17.7%, Sharpe = **-1.779**, Max DD = **-42.5%**, Turnover = 0.967.
  - HAR per-stock: Return = -16.9%, Vol = 16.2%, Sharpe = -1.349, Max DD = -35.9%, Turnover = 1.330.
  - GNN-Ensemble + Macro: Return = -14.9%, Vol = 17.5%, Sharpe = -1.137, Max DD = -37.3%, Turnover = 0.552.
- **Result:** In the 2024–2025 bull market, high-volatility equities (technology, semiconductors, AI leaders) delivered the highest positive returns, causing the short leg of the volatility trade to suffer structural adverse momentum.

### Independently reproduced

Not independently reproduced. Empirical findings and parameter tables are extracted from the primary LaTeX document and repository snapshot at commit `31768802d0e2581085a303e78b4d83c04f7b5253`.

### Negative evidence

1. **Failure of Raw Graphs Without Macro Features:** Without macro conditioning, both GNN-Sector (MSE = 0.0336, Sharpe = 0.492) and GNN-Granger (MSE = 0.0337, Sharpe = 0.412) underperform the simple linear pooled HAR baseline (MSE = 0.0331, Sharpe = 0.729).
2. **Graph Oversmoothing in Market Crises:** Table 2 reveals that during the March 2020 COVID shock, graph density under the $|\rho| \ge 0.30$ threshold exploded to 0.933 (mean degree 432.7 out of 464 possible neighbors), causing neighborhood aggregation to become nearly uniform across the universe and destroying cross-sectional differentiation.
3. **Decoupling of Error Metrics and Strategy Value:** GNN-Correlation + Macro 63d achieved the best point forecast MSE (0.0298), but GNN-Sector + Macro delivered a substantially higher Sharpe ratio (0.984 vs 0.794) with 39% lower turnover (0.406 vs 0.670), demonstrating that minimizing squared error is suboptimal for portfolio execution.
4. **Catastrophic Failure in Long-Short Construction:** Standalone volatility ranking failed completely across all 14 evaluated models in the 2024–2025 regime, generating drawdowns between -34.4% and -42.5%.

## Falsification plan

1. **Survivorship Bias Stress Test:** Reconstruct the 2015–2025 panel using point-in-time index constituent memberships (incorporating delisted and acquired firms). If the out-of-sample minimum-variance Sharpe advantage of GNN-Sector + Macro degrades by $> 0.30$ relative to HAR, the reported outperformance is an artifact of survivorship conditioning.
2. **Bear Market & Volatility Spike Walk-Forward:** Evaluate the minimum-variance allocation across market crash regimes (e.g., 2008 GFC or 2022 rate-hike bear market). If graph density exceeds 0.75 and portfolio turnover spikes $> 1.50$, triggering severe drawdown amplification, the neighborhood aggregation mechanism fails during the exact regimes it is designed to mitigate.
3. **Graph Topology Ablation:** Shuffle node labels while preserving graph topology (Erdős–Rényi random graph baseline with matching density). If the randomized graph matches or exceeds GNN-Sector + Macro Sharpe ratio, the graph topology provides zero genuine economic information.
4. **Cost Sensitivity Threshold:** Increase transaction costs from 10 bps to 25 bps. If average weekly turnover (0.406) erodes Sharpe below the pooled HAR baseline (0.729), the execution edge is commercially unviable.

## Crypto portability

**Portability Classification:** `adapted` / `unproven`.

- **Traditional Asset Origin:** The empirical mechanism is established exclusively on large-cap U.S. equities (S&P 500).
- **Crypto Portability Hurdles:**
  1. **Continuous 24/7 Trading:** Crypto lacks discrete weekend calendar boundaries. Weekly Monday-anchored aggregation must be adapted to rolling 7-day windows or 8-hour funding intervals.
  2. **Absence of GICS Sector Structure:** Cryptocurrencies lack formal, audited industrial classifications. Token categorizations (e.g., L1, DeFi, Layer-2, AI, Memes) are fluid, unstandardized, and experience rapid regime turnover.
  3. **Hyper-Correlated Market Regimes:** Altcoin returns exhibit substantially higher baseline cross-correlations with Bitcoin ($\rho > 0.70$ during market drawdowns). A static threshold of $|\rho| \ge 0.30$ would produce an almost fully connected graph continuously, causing permanent oversmoothing and eliminating cross-sectional feature variance.
  4. **Funding Rate & Borrow Drag:** In crypto perpetual futures, shorting high-volatility tokens incurs volatile and asymmetric funding rates. In negative funding regimes, shorting high-volatility names produces severe cash-flow bleed.
  5. **Token Lifecycle & Survivorship:** The crypto universe experiences rapid turnover, exchange delistings, and protocol insolvencies. Survivorship-safe point-in-time universe filtering is significantly harder to maintain than in S&P 500 equities.

## Limitations

- **Survivorship Bias:** Universe is conditioned on surviving S&P 500 constituents through December 2025.
- **Short Out-of-Sample Window:** The test period is limited to 103 weeks (2024–2025), a persistent bull market dominated by high-beta tech leadership.
- **Static Granger Topology:** Granger causality edges are computed once on the 2015–2022 training period and held fixed, ignoring structural shifts in lead-lag relationships.
- **Execution Simplifications:** Slippage, market depth, bid-ask spread variations, and borrow fees for the short leg are omitted.
- **Data Vendor Dependency:** Daily prices collected via Yahoo Finance (`yfinance`), which is subject to retroactive dividend/split adjustments and unrecorded corporate actions.

## Implementation status

`not-implemented`. No implementation of GraphSAGE volatility forecasting, graph topology caching, or OSQP minimum-variance portfolio allocation exists in the repository, PyBroker, or NautilusTrader.

## Adoption boundary

`research-only`. This record is an analytical capture of external public research. It does not constitute strategy adoption, implementation authorization, or permission for paper, testnet, or live trading. Any future implementation requires formal research intake review, point-in-time universe reconstruction, and independent out-of-sample backtesting.

## Related Wiki records

- [[quant/commodity-futures-network-momentum-lead-lag-graph-learning-2026-09-02]] — Network momentum and graph learning for lead-lag relationships in commodity futures (arXiv:2501.07135).
- [[quant/cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02]] — Cross-sectional topological anomaly scores and return predictability (arXiv:2606.08586).
- [[quant/cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02]] — Deep parametric portfolio policies for multi-asset timing (arXiv:2607.00475).
- [[quant/volatility-process-arch-garch-2026-08-28]] — Time-varying volatility modeling, ARCH/GARCH processes, and volatility clustering.
- [[quant/portfolio-covariance-and-shrinkage-2026-08-28]] — High-dimensional covariance matrix estimation and shrinkage for portfolio optimization.

## Sources

1. Rylan Wade. *"Do Better Volatility Forecasts Lead to Better Portfolios? Evidence from Graph Neural Networks."* arXiv preprint `arXiv:2605.19278v2 [q-fin.PM / q-fin.ST]`, revised May 19, 2026. Stable URL: [https://arxiv.org/abs/2605.19278](https://arxiv.org/abs/2605.19278). DOI: [10.48550/arXiv.2605.19278](https://doi.org/10.48550/arXiv.2605.19278).
2. Rylan Wade. *"sp500-gnn: Graph Neural Network for S&P 500 Volatility and Portfolio Optimization."* GitHub repository, commit `31768802d0e2581085a303e78b4d83c04f7b5253`. URL: [https://github.com/waderylan/sp500-gnn](https://github.com/waderylan/sp500-gnn).
3. Corsi, F. (2009). *"A simple approximate long-memory model of realized volatility."* Journal of Financial Econometrics, 7(2), 174-196.
4. Hamilton, W., Ying, Z., & Leskovec, J. (2017). *"Inductive representation learning on large graphs."* Advances in Neural Information Processing Systems (NeurIPS 2017), 30.
5. Federal Reserve Bank of St. Louis (FRED). *"3-Month Treasury Bill Secondary Market Rate (DTB3)."* [https://fred.stlouisfed.org/series/DTB3](https://fred.stlouisfed.org/series/DTB3).
