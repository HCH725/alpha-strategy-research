---
schema: strategy-research-record-v1
title: "Cryptocurrency Portfolio Optimization via Stable Consensus Clustering of Price Correlation Networks and Predictive Return Forecasting"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cryptocurrency
  - portfolio-optimization
  - correlation-network
  - consensus-clustering
  - louvain-modularity
  - arima-forecasting
  - modern-portfolio-theory
  - ledoit-wolf-shrinkage
status: research-only
confidence: medium
source_as_of: 2025-05-29
sources:
  - https://arxiv.org/abs/2505.24831
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cryptocurrency Portfolio Optimization via Stable Consensus Clustering of Price Correlation Networks and Predictive Return Forecasting

## Provenance

- **Primary Academic Source:** Ruixue Jing (Department of Economics, Ghent University), Ryota Kobayashi (National Institute of Informatics / SOKENDAI, Tokyo), and Luis E. C. Rocha (Department of Economics / Department of Physics and Astronomy, Ghent University), *"Optimising cryptocurrency portfolios through stable clustering of price correlation networks"*, arXiv preprint `arXiv:2505.24831v2 [q-fin.PM]`, first submitted May 29, 2025, revised 2025.
- **Canonical arXiv URL:** https://arxiv.org/abs/2505.24831
- **Full Text HTML:** https://arxiv.org/html/2505.24831
- **Digital Object Identifier (DOI):** https://doi.org/10.48550/arXiv.2505.24831
- **Licence:** arXiv.org perpetual non-exclusive license.
- **Award Recognition:** Recognized with the Best Poster Award at NetSci 2025.
- **Repository Deduplication Audit:** A comprehensive audit of all existing `.md` records in `alpha-strategy-research` confirms zero prior citations of `2505.24831`, Ruixue Jing, Ryota Kobayashi, or Luis E. C. Rocha. Existing records touching network graphs or clustering (`dynamic-knowledge-graph-community-gated-signal-propagation-2026-09-04.md`, `spectral-graph-topological-crash-rally-detection-correlation-network-2026-09-04.md`, `crypto-stat-arb-signed-sponge-clustering-market-mode-residual-2026-09-12.md`, `crypto-correlation-clustered-pairs-trading-structural-metadata-stability-2026-09-15.md`) focus on corporate supply-chain knowledge graphs, cross-asset equity crash detection, signed graph Laplacian market-mode extraction, or hourly crypto pairs trading mean-reversion. None implement consensus Louvain clustering across shifting correlation windows with forward-looking ARIMA log-return forecasting, cluster-representative asset sampling, and Ledoit-Wolf shrinkage MPT Sharpe ratio allocation across multi-day horizons.

## Economic mechanism

### Source-reported

Cryptocurrency markets display pronounced collective dynamics, high non-stationarity, and episodic correlation spikes where naive asset-level diversification collapses during market downturns. The authors argue that while global modularity in crypto correlation networks is structurally low ($\langle Q \rangle \approx 0.12$) due to a dominant market mode (strongly driven by Bitcoin), the market possesses persistent local community structures.

Standard community detection algorithms (such as the Louvain heuristic) are stochastic and sensitive to temporal noise, yielding transient partitions that vary across algorithmic runs and sliding observation windows. To resolve this, the authors propose a **consensus clustering framework**:
1. Evaluating price correlation networks over $n = 30$ shifted time intervals or stochastic realizations.
2. Building an $N \times N$ consensus co-membership similarity matrix $\tilde{S}$ where entries represent the proportion of times two cryptocurrencies co-occur in the same Louvain community.
3. Applying a majority threshold $\theta_M = 0.5$ to isolate robust, temporally stable clusters ("risk classes").
4. Incorporating forward-looking time-series return forecasts (ARIMA) into the network construction to capture evolving trend directions before they fully materialize in backward-looking rolling correlations.
5. Constructing a diversified portfolio by selecting one representative asset per cluster at random, and computing risk-adjusted optimal weights under Modern Portfolio Theory (MPT) using the Ledoit-Wolf constant-variance shrinkage covariance matrix to maximize the portfolio Sharpe ratio.

### Research interpretation

The economic thesis is that **cryptocurrency market co-movement is organized into hierarchical risk communities that share common systemic drivers, liquidity cascades, or sector/narrative dependencies. Naive asset selection overconcentrates risk in the dominant Bitcoin-correlated cluster. Extracting temporally persistent consensus clusters partitions the universe into quasi-orthogonal risk classes; selecting assets across distinct consensus clusters enforces true structural diversification, while integrating forward-looking log-return forecasts (ARIMA) prevents backward-looking correlation lag and stabilizes left-tail risk over multi-day holding horizons.**

In this hybrid framework:
- **Regime / Structural Filter:** Correlation network distance filtering ($d_{ij} < 1$, corresponding to $\rho_{ij} > 0.5$) and Louvain consensus modularity clustering ($\theta_M = 0.5$) identify persistent co-movement risk classes.
- **Forecasting Component:** Forward-looking ARIMA log-return prediction provides anticipated returns $\hat{r}$ across the forecast horizon $\Delta_h$.
- **Asset Selection Rule:** Uniform random selection of one asset per identified stable cluster guarantees representation across all distinct market sub-communities.
- **Portfolio Construction:** Ledoit-Wolf shrinkage covariance estimation with Sharpe ratio maximization calculates non-negative weights ($w_i \ge 0, \sum w_i = 1$) under Modern Portfolio Theory.

## Signal

### Data Transformation and Stationarity (Source-Reported)

1. **Daily Log Returns:** For cryptocurrency $i$ at day $t$ with closing price $P_{i,t}$ in USD:
   $$r_{i,t} = \ln\left(\frac{P_{i,t}}{P_{i,t-1}}\right)$$
   Stationarity is verified across all assets via Augmented Dickey-Fuller (ADF) tests ($p < 0.001$).

2. **Rolling Walk-Forward Evaluation Schedule:**
   - Total study timeline: 1,613 days (November 15, 2017 to April 15, 2022).
   - Number of rolling study periods: $n_s = 42$ periods.
   - Training window: $\Delta_T = 351$ days ($[t_0 - \Delta_T, t_0]$).
   - Test investment horizon: $\Delta_h \in \{1, 2, \dots, 14\}$ days ($[t_0, t_0 + \Delta_h]$).
   - Rolling step: $t_0$ advances by $30$ calendar days per period.

### Price Prediction Engine (Source-Reported)

Three forecasting models were evaluated on the training data:
- **ARIMA($p,d,q$):** Orders $(p,d,q)$ fitted per asset by minimizing the Akaike Information Criterion (AIC).
- **LSTM:** Multi-layer recurrent neural network with Mean Squared Error (MSE) loss, dropout, and sequence length tuning.
- **Naive Benchmark:** $\hat{r}_{i, t_0 + h} = r_{i, t_0}$.
- *Finding:* ARIMA achieved the lowest average median MSE across 42 study periods and outperformed LSTM across 13 of 14 forecast horizons (Table 3), while requiring substantially lower computational resources.

### Correlation Network & Consensus Louvain Clustering (Source-Reported)

1. **Correlation Estimation Window:**
   - Window length $\Delta_c = 30$ days of daily log returns.
   - Pearson correlation coefficient $\rho_{ij}$ computed between assets $i$ and $j$.
2. **Metric Distance Transformation:**
   $$d_{ij} = \sqrt{2(1 - \rho_{ij})}$$
   Edges are retained only if $d_{ij} < \sqrt{2(1 - \theta_\rho)} = 1$, corresponding to $\theta_\rho = 0.5$ (i.e. $\rho_{ij} > 0.50$).
3. **Louvain Modularity Optimization:**
   $$Q = \frac{1}{2m} \sum_{ij} \left[\rho_{ij} - \frac{k_i k_j}{2m}\right] \delta(c_i, c_j)$$
   where $k_i, k_j$ are weighted node degrees, $m$ is total edge weight, and $\delta(c_i, c_j) = 1$ if nodes belong to the same community.
4. **Consensus Aggregation across $n = 30$ Windows:**
   - To remove stochastic Louvain variability and window-boundary sensitivity, the detection window is shifted backwards by 1 day across $n = 30$ intervals:
     - For historical variants (Baseline, S): intervals span $[t_0 - \Delta_c - k + 1, t_0 - k + 1]$ for $k = 1, \dots, 30$.
     - For predictive variants (P, P-S): intervals incorporate predicted returns over $[t_0 + \Delta_h - \Delta_c - k + 1, t_0 + \Delta_h - k + 1]$.
   - Co-occurrence matrix $S \in \mathbb{R}^{N \times N}$ records count of joint community membership:
     $$\tilde{s}_{ij} = \frac{s_{ij}}{n} \in [0, 1]$$
5. **Stable Cluster Partitioning:**
   - Majority filtering: retain edges with $\tilde{s}_{ij} \ge \theta_M = 0.50$.
   - The resulting connected components form the set of stable clusters $\mathcal{C} = \{C_1, C_2, \dots, C_K\}$.

### Portfolio Selection & Optimization (Source-Reported)

1. **Cluster Asset Sampling:**
   - From each identified cluster $C_k \in \mathcal{C}$, select exactly one cryptocurrency uniformly at random:
     $$a_k \sim \text{Uniform}(C_k)$$
     yielding a selected asset subset $\mathcal{A} = \{a_1, \dots, a_K\}$.
2. **Sharpe Ratio Maximization under MPT:**
   $$\max_\mathbf{w} \frac{\mathbf{w}^T \boldsymbol{\mu} - r_f}{\sqrt{\mathbf{w}^T \hat{\Sigma}_{\text{LW}} \mathbf{w}}}$$
   subject to:
   $$\mathbf{e}^T \mathbf{w} = 1, \quad w_i \ge 0 \quad \forall i \in \mathcal{A}$$
   - Annualized risk-free rate $r_f = 0.02$ ($0.005\%$ daily hurdle).
   - Expected returns $\boldsymbol{\mu}$: estimated from historical/predicted returns via PyPortfolioOpt.
   - Covariance Matrix $\hat{\Sigma}_{\text{LW}}$: regularized using the Ledoit-Wolf constant-variance target shrinkage estimator:
     $$\hat{\Sigma}_{\text{LW}} = \delta^\star F + (1 - \delta^\star) C$$
     where $F = \bar{\sigma}^2 I$ is the constant-variance identity target and $\delta^\star$ is the optimal shrinkage intensity.

### Operational Strategy Rules (`research-proposed`)

Because the primary paper focuses on econometric portfolio performance across fixed holding horizons without specifying a live order execution protocol, the following rules are `research-proposed`:
- **Execution Timestamp:** Evaluated at daily close (00:00 UTC); target portfolio rebalance executed at 00:05 UTC (`research-proposed`).
- **Rebalance Cadence:** Fixed holding horizon $\Delta_h = 7\text{ days}$ or $\Delta_h = 14\text{ days}$ matching the author's primary evaluation horizons (`research-proposed`).
- **Cluster Random Sampling Aggregation:** Rather than single-seed random sampling, average asset weights across 100 Monte Carlo cluster draws to eliminate single-draw variance (`research-proposed`).
- **Position Sizing / Leverage:** Fully invested long-only equity ($\sum w_i = 1.0$), zero leverage ($1.0\times$), max single asset cap $\le 25\%$ (`research-proposed`).
- **Emergency De-risking Gate:** If portfolio rolling 3-day drawdown exceeds $8.0\%$, liquidate to USDT/cash until the next 30-day reconstitution date (`research-proposed`).

## Required data

- **Universe:** Daily closing prices in USD for active cryptocurrencies.
  - Source universe: Top 1,000 cryptocurrencies by market capitalization on February 22, 2022, filtered for continuous trading history from November 15, 2017 to April 15, 2022 ($T = 1,613$ days) and fewer than 10 missing daily prints, yielding $N = 157$ assets.
- **Venues / Data Aggregators:** Primary data aggregated across Investing.com, CoinMarketCap, CoinDesk, CoinCodex, and MarketWatch.
- **Fields:** Daily closing market price $P_{i,t}$ in USD at midnight UTC.
- **Point-in-Time Availability:** Training windows strictly precede the investment horizon $[t_0, t_0 + \Delta_h]$. No lookahead bias is introduced; predictions are generated solely from data available at $t_0$.
- **Missing Data Handling:** Excluded assets with $>10$ missing days. Stale or suspended prices are dropped.
- **Benchmarking Data:** Equal-weighted universe proxy (MKT) and Planar Maximally Filtered Graph (PMFG) portfolios used as empirical controls.

## Execution assumptions

- **Source-Reported Settings:**
  - Frictionless execution in primary statistical evaluation (gross returns reported in Tables 5 and 6).
  - Authors explicitly discuss practical fee thresholds: typical crypto exchange fees of $0.10\%$–$0.20\%$ ($10$–$20\text{ bps}$) per side.
  - Implied daily excess returns ($1.39\%$ on Day 1 to $0.15\%$ on Day 14 for P(ARIMA)) provide a sufficient economic buffer against fees at short to medium horizons.
- **Research-Proposed Operational Settings:**
  - **Order Type:** TWAP / limit orders over a 30-minute rebalance window around midnight UTC (`research-proposed`).
  - **Fee Model:** Spot exchange fee of $5.0\text{ bps}$ maker / $10.0\text{ bps}$ taker (`research-proposed`).
  - **Slippage Model:** Modeled at $10.0\text{ bps}$ for liquid large caps (BTC, ETH, LTC) and $30.0\text{ bps}$ for smaller market-cap cluster constituents (`research-proposed`).
  - **Holding Horizon Execution:** Open positions at $t_0$ close, hold passively until $t_0 + \Delta_h$, close at $t_0 + \Delta_h$ close (`research-proposed`).

## Evidence

### Source-reported

All quantitative values below are transcribed directly from Ruixue Jing, Ryota Kobayashi, and Luis E. C. Rocha (arXiv:2505.24831v2, Tables 1, 3, 4, 5, and 6):

1. **Prediction Accuracy Across 42 Study Periods (Table 3, Average Median MSE $\times 10^{-3}$):**
   - **Day 1 ($\Delta_h = 1$):** ARIMA **$1.35$** vs. LSTM $1.58$ vs. Naive $2.88$
   - **Day 3 ($\Delta_h = 3$):** ARIMA **$1.84$** vs. LSTM $1.97$ vs. Naive $3.06$
   - **Day 5 ($\Delta_h = 5$):** ARIMA **$1.71$** vs. LSTM $1.94$ vs. Naive $3.26$
   - **Day 7 ($\Delta_h = 7$):** ARIMA **$1.90$** vs. LSTM $1.94$ vs. Naive $2.80$
   - **Day 10 ($\Delta_h = 10$):** ARIMA **$1.94$** vs. LSTM $2.04$ vs. Naive $3.91$
   - **Day 14 ($\Delta_h = 14$):** ARIMA **$1.48$** vs. LSTM $1.57$ vs. Naive $2.97$
   - *Conclusion:* ARIMA demonstrates superior return prediction over LSTM and Naive across almost all horizons, while requiring substantially lower compute.

2. **Network Modularity Statistics (Table 4):**
   - **Baseline:** Mean Modularity $\langle Q \rangle = 0.124$, Standard Deviation $\sigma = 0.087$
   - **P(ARIMA):** $\langle Q \rangle = 0.123$, $\sigma = 0.084$
   - **S (Shifting):** $\langle Q \rangle = 0.121$, $\sigma = 0.071$
   - **P(ARIMA)-S:** $\langle Q \rangle = 0.122$, $\sigma = 0.069$
   - *Finding:* Low global modularity ($\approx 0.12$) confirms the pervasive common market component in crypto, but shifting-window consensus clustering compresses the standard deviation of community partitions by $\sim 20\%$, producing more consistent cluster definitions over time.

3. **Portfolio Performance Across Horizons (Table 5):**
   - **Average Trade (AT, %):**
     - Day 1: Baseline $+1.82\%$, P(ARIMA) $+1.39\%$, S $+1.59\%$, P(ARIMA)-S $+1.70\%$
     - Day 5: Baseline $+0.62\%$, P(ARIMA) $+0.59\%$, S $+0.32\%$, P(ARIMA)-S $+0.51\%$
     - Day 9: Baseline $+0.10\%$, P(ARIMA) $+0.16\%$, S $+0.04\%$, P(ARIMA)-S $+0.03\%$
     - Day 10: Baseline $+0.05\%$, P(ARIMA) $+0.27\%$, S $-0.05\%$, P(ARIMA)-S $-0.05\%$
     - Day 14: Baseline $-0.05\%$, **P(ARIMA) $+0.15\%$**, S $-0.25\%$, P(ARIMA)-S $-0.21\%$
   - **Win Rate (WR):**
     - Day 1: Baseline $0.69$, P(ARIMA) $0.71$, S $0.74$, P(ARIMA)-S $0.74$
     - Day 5: Baseline $0.57$, P(ARIMA) $0.71$, S $0.60$, P(ARIMA)-S $0.60$
     - Day 10: Baseline $0.48$, P(ARIMA) $0.55$, S $0.57$, P(ARIMA)-S $0.57$
     - Day 14: Baseline $0.50$, **P(ARIMA) $0.60$**, S $0.55$, P(ARIMA)-S $0.57$
   - **Profit Factor (PF):**
     - Day 1: Baseline $4.97$, P(ARIMA) $3.35$, S $3.57$, P(ARIMA)-S $4.48$
     - Day 5: Baseline $2.17$, P(ARIMA) $2.47$, S $1.49$, P(ARIMA)-S $1.96$
     - Day 10: Baseline $1.09$, P(ARIMA) $1.58$, S $0.91$, P(ARIMA)-S $0.90$
     - Day 14: Baseline $0.92$, **P(ARIMA) $1.32$**, S $0.65$, P(ARIMA)-S $0.67$

4. **Tail Risk and Downside Metrics (Table 6):**
   - **Value-at-Risk 5% ($\text{VaR}_{5\%}^{\text{(loss)}}$, %):**
     - Day 1: Baseline $3.04\%$, P(ARIMA) $3.08\%$, S $2.09\%$, P(ARIMA)-S $1.76\%$
     - Day 14: Baseline $2.08\%$, **P(ARIMA) $1.74\%$**, S $3.21\%$, P(ARIMA)-S $2.51\%$
   - **Marginal Expected Shortfall 5% ($\text{MES}_{5\%}^{\text{(loss)}}$, %):**
     - Day 1: Baseline $3.46\%$, P(ARIMA) $2.66\%$, S $-4.62\%$, P(ARIMA)-S $-4.68\%$
     - Day 14: Baseline $1.99\%$, **P(ARIMA) $1.43\%$**, S $2.76\%$, P(ARIMA)-S $1.87\%$
   - **Omega Ratio ($\Omega$, benchmark $r_t = 0$):**
     - Day 1: Baseline $4.97$, P(ARIMA) $3.35$, S $3.57$, P(ARIMA)-S $4.48$
     - Day 5: Baseline $2.17$, P(ARIMA) $2.47$, S $1.49$, P(ARIMA)-S $1.96$
     - Day 10: Baseline $1.09$, P(ARIMA) $1.58$, S $0.91$, P(ARIMA)-S $0.90$
     - Day 14: Baseline $0.92$, **P(ARIMA) $1.32$**, S $0.65$, P(ARIMA)-S $0.67$

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Performance Decay Beyond 5–7 Days:** All strategies without forward predictive updates experience rapid edge erosion beyond a 5-day holding period. By Day 10, both the shifting strategy (S) and shifted-predictive strategy (P-S) turn negative on Average Trade ($-0.05\%$) with Profit Factor falling below $1.0$ ($0.91$ and $0.90$).
- **Baseline Strategy Breakdown at Day 14:** The un-augmented historical Baseline strategy turns unprofitable at Day 14 ($\text{AT} = -0.05\%$, $\text{PF} = 0.92$, $\Omega = 0.92$).
- **Shifted Consensus Tail Spikes:** Strategies that incorporate window shifting without forward-looking price anchoring (S and P(ARIMA)-S) suffer severe spikes in Marginal Expected Shortfall around Days 11–13 ($\text{MES} = 4.64\%$ and $4.70\%$), indicating that shifting backward-looking windows without trend forecasting can select temporarily insulated clusters that suddenly converge with market crashes.
- **PMFG Benchmark Underperformance:** The Planar Maximally Filtered Graph (PMFG) benchmark fails to consistently outperform the equal-weighted market proxy (Figure 7), demonstrating that topological planar filtering alone does not yield a dependable alpha edge in crypto.

## Falsification plan

1. **Random Cluster Partitioning Placebo Test:**
   - Replace the Louvain consensus clusters with randomly generated clusters of identical size distributions, then apply the same Ledoit-Wolf MPT optimization.
   - *Research-defined falsification threshold:* If the true consensus-clustering portfolio fails to achieve at least a $25\%$ higher Average Trade and $0.30$ higher Omega ratio than the random-cluster baseline over $\Delta_h \in [5, 14]$, the hypothesis of structural risk-class alpha is falsified.
2. **Post-2022 Out-of-Sample Market Stress Test:**
   - Evaluate the P(ARIMA) strategy on out-of-sample cryptocurrency price data spanning May 2022 through December 2025 (encompassing the Terra/Luna collapse, FTX bankruptcy, and subsequent bull market).
   - *Research-defined falsification threshold:* If P(ARIMA) 14-day Average Trade becomes negative ($\text{AT} < 0.0\%$) or Win Rate drops below $48\%$ ($\text{WR} < 0.48$) over this out-of-sample period, the strategy's temporal persistence is falsified.
3. **Transaction Fee & Rebalance Drag Hurdle:**
   - Deduct $15\text{ bps}$ per-side transaction cost ($30\text{ bps}$ round-trip) and $10\text{ bps}$ slippage from the simulated trades.
   - *Research-defined falsification threshold:* If net Average Trade at $\Delta_h = 7\text{ days}$ falls below $+0.10\%$ ($10\text{ bps}$), the strategy is classified as operationally non-viable due to turnover drag.
4. **ARIMA Lookahead Leakage Audit:**
   - Verify that AIC model selection and differencing order estimation in ARIMA strictly utilize data prior to $t_0$.
   - *Research-defined falsification threshold:* If any in-sample information from $[t_0, t_0 + \Delta_h]$ is detected in feature normalization or ARIMA estimation, the research capture is invalidated.

## Crypto portability

**direct (spot) / adapted (perpetual futures)**

- **Demonstrated Directly in Crypto Spot Markets:** Unlike ported traditional-equity strategies, the cited source evaluates this exact framework on a 157-token cryptocurrency universe across 5 years of daily market data (2017–2022).
- **Crypto-Specific Operational Dynamics:**
  - **Spot Portability (Direct):** Direct implementation on spot exchanges (Binance, Coinbase, Kraken, OKX) is structurally feasible for high-liquidity constituents.
  - **Perpetual Futures Adaptation (Adapted / Unproven):** Porting the strategy to perpetual futures introduces funding rate drag. Because the strategy is long-only, holding perp positions in high-funding altcoins can erase the $0.15\%$–$0.59\%$ multi-day edge.
  - **Liquidity & Small-Cap Tail Risk:** While top-cap assets (BTC, ETH, LTC, XRP) have deep liquidity, smaller tokens appearing in consensus clusters (e.g. OCN, DLT, FUEL analyzed in Table 1) suffer from severe bid-ask spreads, low market depth, and exchange delisting risk.
  - **Survivorship & Reconstitution:** The paper's universe filtering (requiring continuous trading from 2017 to 2022) introduces survivorship bias. A live production system must implement dynamic rolling universes with point-in-time liquidity filtering.

## Limitations

- **Survivorship Bias in Filtered Universe:** Filtering for tokens continuously active over 1,613 days ($N = 157$ from 5,450 initial tokens) selects historical survivors, overstating average returns and understating delisting / terminal drawdown risks.
- **Random Single-Asset Cluster Selection Variance:** The author's selection rule selects one token per cluster uniformly at random. A single randomized draw introduces portfolio path variance; operational deployment requires ensembling across multiple draws (`research-proposed`).
- **Absence of Realized Transaction Costs:** The primary results are reported gross of trading fees and bid-ask spreads. At a 14-day holding horizon, the net margin ($+0.15\%$) leaves a narrow buffer against multi-asset rebalancing fees.
- **Compute Overhead of Daily ARIMA Re-estimation:** Fitting ARIMA across 157 assets over 351-day rolling windows requires ongoing computational infrastructure, though it remains significantly more tractable than deep-learning models.

## Implementation status

`not-implemented`

No implementation of this consensus-clustering correlation network framework or ARIMA predictive MPT portfolio strategy exists in our research stack (`nautilus-quant-system`, PyBroker, or NautilusTrader).

## Adoption boundary

`research-only` | `adoption: not-approved` | `approval_scope: research-only`

This record is an upstream research capture. It does not constitute strategy approval, does not authorize live or paper execution, and does not claim verified production alpha.

## Related Wiki records

- `[[quant/dynamic-knowledge-graph-community-gated-signal-propagation-2026-09-04]]` — Louvain community modularity clustering applied to equity knowledge graphs.
- `[[quant/spectral-graph-topological-crash-rally-detection-correlation-network-2026-09-04]]` — Correlation network topology and eigenvalue spectra for market regime detection.
- `[[quant/crypto-stat-arb-signed-sponge-clustering-market-mode-residual-2026-09-12]]` — Signed graph Laplacian clustering for crypto statistical arbitrage.

## Sources

- **Primary Source:** Ruixue Jing, Ryota Kobayashi, and Luis E. C. Rocha, *"Optimising cryptocurrency portfolios through stable clustering of price correlation networks"*, arXiv preprint `arXiv:2505.24831v2 [q-fin.PM]`, first submitted May 29, 2025; revised 2025.
  - Canonical URL: https://arxiv.org/abs/2505.24831
  - Full Text HTML: https://arxiv.org/html/2505.24831
  - DOI: https://doi.org/10.48550/arXiv.2505.24831
- **Key Methodological References Cited in Primary Source:**
  - Vincent D. Blondel, Jean-Loup Guillaume, Renaud Lambiotte, and Etienne Lefebvre (2008), *"Fast unfolding of communities in large networks"*, *Journal of Statistical Mechanics: Theory and Experiment*, 2008(10):P10008. (Louvain algorithm).
  - Olivier Ledoit and Michael Wolf (2004), *"A well-conditioned estimator for large-dimensional covariance matrices"*, *Journal of Multivariate Analysis*, 88(2):365–411. (Ledoit-Wolf shrinkage).
  - Alexander Brauneis and Roland Mestel (2019), *"Cryptocurrency-portfolios in a mean-variance framework"*, *Finance Research Letters*, 28:259–264.
  - Ruixue Jing and Luis E. C. Rocha (2023), *"A network-based strategy of price correlations for optimal cryptocurrency portfolios"*, *Finance Research Letters*, 58:104503.
  - Con Keating and William F. Shadwick (2002), *"An introduction to Omega"*, *The Alternative Investment Management Association (AIMA) Newsletter*.
  - Viral V. Acharya, Lasse H. Pedersen, Thomas Philippon, and Matthew Richardson (2017), *"Measuring systemic risk"*, *The Review of Financial Studies*, 30(1):2–47. (Marginal Expected Shortfall).
