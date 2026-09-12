---
schema: strategy-research-record-v1
title: "Pairs Selection via Dynamic Time Warping (DTW) and Optimal Causal Path (OCP) Hierarchical Clustering: Regime-Dependent Asymmetry, Thermal Path Falsification, and Look-Ahead Candidate Reversal"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - pairs-trading
  - dynamic-time-warping
  - optimal-causal-path
  - thermal-optimal-path
  - hierarchical-clustering
  - cointegration
  - kalman-filter
  - regime-switching
  - falsification
  - look-ahead-bias
  - equities
status: research-only
confidence: high
source_as_of: 2026-09-12
sources:
  - "Wyatt Earls (WyattEarls), 'DTW-OTP-Pairs-Trading: Research repository exploring pair-trading strategies using Dynamic Time Warping (DTW) variants and the Optimal Thermal Path (OTP) framework, benchmarked against correlation-based and cointegration methods', GitHub repository WyattEarls/DTW-OTP-Pairs-Trading (commit eaf13d18fba4079c827d91ba35bd025e7968da68, September 12, 2026). Paths: README.md, papers/Pairs Selection via DTW and OCP Clustering: Evidence of Regime-Dependent Performance on the S&P 500.md, papers/draft.md, Examples/DTW-OCP-TOP-naive_clustering_comparison_SP_500.ipynb, Examples/Four-way-comparison-bull-and-bear-market-analysis.ipynb, Examples/08_OCP_Clustering.ipynb, Examples/09_DTW_OCP_Clustering_SP500.ipynb. Stable URL: https://github.com/WyattEarls/DTW-OTP-Pairs-Trading"
  - "Wyatt Earls, 'Pairs Selection via DTW and OCP Clustering: Evidence of Regime-Dependent Performance on the S&P 500' (September 2026). Path: papers/Pairs Selection via DTW and OCP Clustering: Evidence of Regime-Dependent Performance on the S&P 500.md"
  - "Wyatt Earls, 'Pairs Selection via DTW and OCP Clustering: Evidence of Regime-Dependent Performance on the S&P 500' (extended draft, September 2026). Path: papers/draft.md"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Pairs Selection via Dynamic Time Warping (DTW) and Optimal Causal Path (OCP) Hierarchical Clustering: Regime-Dependent Asymmetry, Thermal Path Falsification, and Look-Ahead Candidate Reversal

## Provenance

- **Author / Research Lab:** Wyatt Earls (`WyattEarls`).
- **Primary Source Codebase:** Public GitHub repository `https://github.com/WyattEarls/DTW-OTP-Pairs-Trading`.
- **Immutable Commit SHA:** `eaf13d18fba4079c827d91ba35bd025e7968da68` (main branch HEAD, September 12, 2026 04:20:07 UTC).
- **Inspected Primary Source Files:**
  - `README.md`: Project description framing pair trading with DTW variants, the Optimal Thermal Path (OTP) framework, and benchmarks against correlation and cointegration.
  - `papers/Pairs Selection via DTW and OCP Clustering: Evidence of Regime-Dependent Performance on the S&P 500.md`: Academic research paper detailing methodology, dendrogram partitions, pairwise Adjusted Rand Index (ARI) comparisons, example pair dynamics (LLY-RF), 20-year Test period pooled performance, transaction cost sensitivity, and regime-conditional bull vs. bear market Sharpe comparisons.
  - `papers/draft.md`: Extended monograph documenting universe construction, rolling Sharpe ratio calculation, mathematical formulation of DTW vs. OCP distance metrics, look-ahead bias contamination and candidate reversal proofs, Kalman filter state-space formulation, regime-dependent entry thresholds, and trade-count heterogeneity.
  - `Examples/DTW-OCP-TOP-naive_clustering_comparison_SP_500.ipynb`: 20-year empirical research notebook (2005–2025) executing data extraction from historical S&P 500 rosters, 52-week rolling Sharpe calculation, parallelized DTW, OCP, and TOP distance matrix calculation, Ward-linkage hierarchical clustering ($k=2, 4, 7$), cluster validation indices, intra-cluster Engle-Granger cointegration testing with Benjamini-Hochberg FDR control, continuous multi-period Kalman filter tracking, spread volatility regime segmentation, Z-score signal generation, transaction cost deduction ($0, 5, 10, 20$ bps), and 5,000-iteration block bootstrap significance tests.
  - `Examples/Four-way-comparison-bull-and-bear-market-analysis.ipynb`: Regime analysis notebook evaluating locked Test-period weekly returns across 59 independently published bear-market weeks (Q4 2018 correction, 2020 COVID crash, 2022 bear market) vs. 359 bull-market weeks, computing Sortino, Calmar, drawdown, and Benjamini-Hochberg corrected bootstrap differences against naive buy-and-hold.
  - `Examples/08_OCP_Clustering.ipynb` & `Examples/09_DTW_OCP_Clustering_SP500.ipynb`: Exploratory implementations of OCP alignment dynamic programming and hierarchical cluster dendrogram generation.
- **Repository Deduplication Audit:** A comprehensive audit of all strategy records in `alpha-strategy-research` confirmed zero pre-existing captures citing Wyatt Earls or repository `WyattEarls/DTW-OTP-Pairs-Trading`. Existing statistical arbitrage and pairs trading records in the repository examine distinct mechanisms, universes, and selection protocols:
  - `tether-pairs-trading-fdr-kalman-half-life-net-beta-2026-09-12.md` (Gite 2026) evaluated sector-constrained pairs with FDR, half-life scoring, and net beta.
  - `johansen-cointegration-etf-pairs-friction-asymmetry-falsification-2026-09-12.md` (Batra 2026) investigated a 60-pair ETF universe under Johansen cointegration with friction asymmetry barriers.
  - `sp500-pairs-trading-forensic-falsification-unbounded-beta-kalman-phantom-pnl-2026-09-12.md` (Nguyen 2026) investigated unbounded beta drift and phantom P&L in Kalman filters when equity prices diverge.
  - `sp500-sector-pairs-causal-residual-pca-area-asymmetry-2026-09-12.md` (Nock 2026) evaluated S&P 500 equity sector pairs using causal residualization and PCA hedge ratio asymmetry.
  - `sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12.md` (pdwi2020 2026) evaluated multi-asset Johansen cointegration with OU ablation and Hansen SPA.
  - `pairs-trading-adf-stationarity-filter-walk-forward-falsification-2026-09-12.md` (sefaav 2026) investigated walk-forward ADF stationarity filtering across liquid equity pairs.
  - `ou-first-passage-time-bands-fdr-stability-portfolio-stat-arb-2026-09-12.md` (Riego 2026) evaluated Ornstein-Uhlenbeck first-passage time bands and FDR stability.
  Wyatt Earls' research provides an independent, source-grounded comparative evaluation of elastic distance metrics (unconstrained DTW, causality-constrained OCP, and finite-temperature TOP) for pre-filtering large equity universes ($N=267$) prior to cointegration testing, demonstrating empirical regime-dependent performance asymmetry, a severe candidate-prolificacy reversal caused by look-ahead bias, and empirical falsification of the Thermal Optimal Path hypothesis.

## Economic mechanism

### Source-reported

In classical equity pairs trading, pairwise cointegration screening across an unconstrained universe of $N$ equities requires evaluating $\frac{N(N-1)}{2}$ candidate combinations, inducing massive multiple-testing contamination and identifying spurious statistical relationships that collapse out-of-sample. Traditional pre-filtering relying on static linear correlation or Euclidean distance fails because financial time series exhibit time-varying phase shifts, asymmetric lead-lag latencies, and non-synchronous repricing.

The author examines whether elastic time-series distance metrics can group equities into structurally coherent clusters based on co-movement in their rolling risk-adjusted return profiles (52-week rolling Sharpe ratios). Dynamic Time Warping (DTW) permits non-linear, elastic alignment between two series without directional constraints. Optimal Causal Path (OCP, Stübinger 2019) introduces a strict causality constraint ($j \ge i$ in the dynamic programming grid), ensuring that an observation in one series can only be matched to contemporaneous or past observations in the other, explicitly capturing lead-lag dynamics. Thermal Optimal Path (TOP, Liu et al. 2022) generalizes OCP into a statistical mechanics framework at finite temperature $T$, computing free energy across an ensemble of near-optimal causal paths rather than concentrating probability on a single deterministic trajectory.

The primary economic premise tested across a 20-year S&P 500 dataset (2005–2025) is that pairs identified through temporal alignment clustering exploit lead-lag informational diffusion and transient liquidity shocks. The author investigates whether this statistical arbitrage mechanism delivers consistent alpha across market environments, or whether its risk-adjusted edge is structurally confined to market drawdowns.

### Research interpretation

The hypothesized mechanism is **regime-conditional liquidity provision and lead-lag structural convergence under elastic cluster pre-selection**.

The strategy pipeline operates as a multi-stage quantitative filter:
1. **Rolling Performance Feature Space:** Rather than raw log prices, the distance metrics align 52-week rolling Sharpe ratio time series, grouping assets that share macroeconomic factor exposures and risk-adjusted cyclicality.
2. **Elastic Alignment Clustering:** Ward-linkage hierarchical clustering partitions the universe into disjoint clusters ($k=2, 4, 7$), dramatically restricting the pairwise search space and reducing the multiple-testing burden before formal statistical testing.
3. **FDR-Controlled Cointegration Screening:** Intra-cluster pairs are tested for stationary cointegrating residuals using the Engle-Granger two-step procedure with Benjamini-Hochberg False Discovery Rate control ($\alpha = 0.05$).
4. **Continuous State-Space Kalman Tracking:** A two-dimensional random-walk Kalman filter dynamically models the time-varying hedge ratio and intercept across the multi-period lifecycle without periodic retraining or parameter reset shocks.
5. **Regime-Gated Signal Generation:** Entry thresholds expand or contract based on rolling spread volatility, entering mean-reverting positions when spread dislocations exceed statistical noise thresholds.

The fundamental empirical finding of this research is that market-neutral pairs trading derived from elastic clustering functions primarily as a **crisis drawdown buffer** rather than an absolute-return growth engine. In severe market sell-offs (bear regimes), institutional deleveraging and liquidity flight dislocate cointegrated assets, creating wide, highly profitable mean-reverting spreads while directional equity markets plummet. In sustained bull markets, strong persistent trends cause spreads to drift, generating lower risk-adjusted returns than simple equity beta exposure.

## Signal

### Formation timestamp
- **Data frequency:** Weekly closing prices resampled to Wednesday close (`W-WED`, `Close` adjusted for splits and dividends, `Examples/DTW-OCP-TOP-naive_clustering_comparison_SP_500.ipynb`, Cell 2) (`source-reported`).
- **Signal formation:** Evaluated at the Wednesday weekly close using trailing price and spread data up to week $t$ (`source-reported`).
- **Execution convention:** 1-bar lagged execution (`signal.shift(1) * spread_diff`, Cell 23 and Cell 27) (`source-reported`). Positions triggered on Wednesday close $t$ take effect for return capture over week $t+1$, completely avoiding same-bar look-ahead bias.

### Lookback windows
- **Rolling Sharpe ratio feature window:** Rolling $W_{\text{Sharpe}} = 52$ weeks (1 year) (`source-reported`).
- **Formation / Train period:** 2005-01-01 to 2010-12-31 (6 calendar years, 313 weekly observations), used for distance matrix computation, hierarchical clustering, and intra-cluster cointegration screening (`source-reported`).
- **Validation period:** 2011-01-01 to 2017-12-31 (7 calendar years, 365 weekly observations), used for threshold multiplier optimization ($M = 0.75$) under a 50% pair activity floor (`source-reported`).
- **Test period (Out-of-Sample):** 2018-01-01 to 2025-12-31 (7 calendar years, 418 weekly observations), strictly locked for reportable performance (`source-reported`).
- **Spread Z-score normalization window:** Rolling $W_Z = 52$ weeks (`ZSCORE_WINDOW = 52`, Cell 0) (`source-reported`).
- **Spread volatility regime window:** Rolling $W_{\text{vol}} = 26$ weeks (`VOL_WINDOW = 26`, Cell 0) (`source-reported`).

### Mathematical formulation

#### 1. Elastic Distance Metrics on Rolling Sharpe Space
For two stocks with 52-week rolling Sharpe time series $x = (x_1, \dots, x_n)$ and $y = (y_1, \dots, y_m)$ ($n = m = 313$ on Train):

- **Dynamic Time Warping (DTW):**
  Unconstrained dynamic programming alignment minimizing cumulative Euclidean distance:
  $$D_{\text{DTW}}(i, j) = |x_i - y_j| + \min \begin{cases} D_{\text{DTW}}(i-1, j) \\ D_{\text{DTW}}(i, j-1) \\ D_{\text{DTW}}(i-1, j-1) \end{cases}$$
  computed via fast C-accelerated `dtaidistance.dtw.distance_matrix_fast` (`source-reported`).

- **Optimal Causal Path (OCP):**
  Causality-constrained dynamic programming blocking matches where $j < i$:
  $$D_{\text{OCP}}(i, j) = \begin{cases} |x_i - y_j| + \min \{ D(i-1, j), D(i, j-1), D(i-1, j-1) \} & \text{for } j \ge i \\ +\infty & \text{for } j < i \end{cases}$$
  Because causality is directional, the symmetric distance is defined as:
  $$D_{\text{OCP}}^{\text{sym}}(x, y) = \min(D_{\text{OCP}}(x, y), D_{\text{OCP}}(y, x))$$
  penalizing series pairs lacking a stable temporal lead-lag structure (`source-reported`).

- **Thermal Optimal Path (TOP):**
  Finite-temperature ensemble average over paths, computing partition function $Z$ and free energy $F$ at temperature $T = 0.5$:
  $$\ln Z(i, j) = -\frac{|x_i - y_j|}{T} + \ln \sum_{(i', j') \in \text{preds}} \exp(\ln Z(i', j')) \quad (j \ge i)$$
  $$D_{\text{TOP}}^{\text{sym}}(x, y) = \min(-T \ln Z(x, y), -T \ln Z(y, x))$$
  evaluated numerically using the log-sum-exp stabilization trick (`source-reported`).

#### 2. Hierarchical Clustering and Cointegration Screening
- Ward-linkage hierarchical clustering applied to condensed distance matrices for $k \in \{2, 4, 7\}$. Across all methods, $k=2$ is mathematically identified as optimal by three independent cluster validation indices: Silhouette score, Calinski-Harabasz index, and Davies-Bouldin index (`source-reported`).
- For each cluster, every pairwise combination of log-price series $(\ln P_A, \ln P_B)$ is tested via Engle-Granger two-step cointegration (`statsmodels.tsa.stattools.coint`).
- Benjamini-Hochberg False Discovery Rate (FDR) control applied across all intra-cluster tests per method at family-wise significance level $\alpha = 0.05$ (`source-reported`).

#### 3. Continuous Online State-Space Kalman Filter
For each significant pair, a two-dimensional state-space model is formulated on log prices:
- Observation equation:
  $$y_t = \begin{bmatrix} x_t & 1 \end{bmatrix} \begin{bmatrix} \beta_t \\ \alpha_t \end{bmatrix} + v_t, \quad v_t \sim \mathcal{N}(0, R), \quad R = 1.0$$
- State transition equation:
  $$\begin{bmatrix} \beta_t \\ \alpha_t \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} \beta_{t-1} \\ \alpha_{t-1} \end{bmatrix} + w_t, \quad w_t \sim \mathcal{N}(0, Q), \quad Q = 10^{-5} \cdot I_2$$
- Initial state: $\mu_0 = [0, 0]^T$, $\Sigma_0 = \mathbf{1}_{2 \times 2}$ (`source-reported`).
- Spread definition:
  $$S_t = y_t - \beta_t x_t - \alpha_t$$
- The Kalman filter is initialized on Train (2005–2010) and rolled forward continuously through Validation (2011–2017) and Test (2018–2025) as a single online process without state re-initialization or parameter resetting (`source-reported`).

#### 4. Volatility Regime Classification
Spread rolling volatility is computed over $W_{\text{vol}} = 26$ weeks:
$$\sigma_{S, t} = \text{std}(S_{t-25:t})$$
The baseline median volatility $\tilde{\sigma}_S$ is locked from Train-period data:
- `high_vol` regime: $\sigma_{S, t} > 1.5 \cdot \tilde{\sigma}_S$ (`VOL_THRESHOLD = 1.5`) (`source-reported`).
- `low_vol` regime: $\sigma_{S, t} < \frac{\tilde{\sigma}_S}{1.5}$ (`source-reported`).
- `normal` regime: all other weeks (`source-reported`).

#### 5. Regime-Dependent Entry / Exit Rules
Spread Z-score is computed over rolling window $W_Z = 52$ weeks:
$$Z_t = \frac{S_t - \mu_{S, t}(52)}{\sigma_{S, t}(52)}$$
Base thresholds tuned on Validation with locked multiplier $M = 0.75$:
- **Standard entry threshold:** $Z_{\text{entry}} = 1.75 \times 0.75 = 1.3125$ (`STANDARD_ENTRY = 1.75`) (`source-reported`).
- **High-volatility entry threshold:** $Z_{\text{entry}} = 2.25 \times 0.75 = 1.6875$ (`HIGH_VOL_ENTRY = 2.25`) (`source-reported`).
- **Low-volatility entry threshold:** $Z_{\text{entry}} = 1.25 \times 0.75 = 0.9375$ (`LOW_VOL_ENTRY = 1.25`) (`source-reported`).
- **Exit threshold:** $|Z_t| \le 0.5$ (`EXIT_THRESHOLD = 0.5`) (`source-reported`).
- **Stop-loss threshold:** $|Z_t| \ge 3.25$ against the position (`STOP_LOSS = 3.25`) (`source-reported`).

#### State Transition Logic:
- Long spread position (long stock 1, short stock 2): Triggered when $Z_t < -Z_{\text{entry}}(t)$ while position is flat ($P_t = 0 \to P_{t+1} = +1$). Closed when $Z_t > -0.5$ or stopped out when $Z_t < -3.25$.
- Short spread position (short stock 1, long stock 2): Triggered when $Z_t > +Z_{\text{entry}}(t)$ while position is flat ($P_t = 0 \to P_{t+1} = -1$). Closed when $Z_t < +0.5$ or stopped out when $Z_t > +3.25$.

## Required data

- **Universe:** S&P 500 historical constituents as of January 1, 2005, sourced from survivorship-bias-free repository `fja05680/sp500` (`S&P 500 Historical Components & Changes.csv`). Delisting date suffixes (`-YYYYMM`) stripped. Filtered to 267 stocks with complete, non-flatlined trading history across the 2005–2025 window (`source-reported`).
- **Venue & Market Type:** US Equities, spot cash markets (`source-reported`).
- **Timeframe & Session:** Weekly Wednesday close (`W-WED`), adjusted for splits and dividends via `yfinance` (`source-reported`).
- **Fields:** Adjusted closing prices (`Close`).
- **Data Vendor Constraint (Provenance Gap):** Yahoo Finance does not serve historical data for corporate entities that were delisted, acquired, or taken private prior to the query date. The effective universe is therefore restricted to January 2005 constituents whose data remains retrievable in 2026, introducing potential survivorship conditioning across the 20-year span (`source-reported`).
- **Benchmark Series:** S&P 500 index (`^GSPC`) weekly closing returns over identical date ranges (`source-reported`).
- **Risk-Free Rate:** Annualized risk-free rate fixed at $R_f = 4.5\%$ ($r_{\text{weekly}} = \frac{0.045}{52} \approx 0.000865$) (`source-reported`).

## Execution assumptions

- **Execution Cadence:** Weekly Wednesday close, orders placed for execution with a 1-week lag (`signal.shift(1)`), eliminating same-bar look-ahead bias (`source-reported`).
- **Order Model:** Assumed market-on-close execution at the published weekly price (`research-proposed`).
- **Portfolio Construction:** Equal-dollar weighting across all active cointegrated pairs within each method's portfolio at each time step ($w_i = \frac{1}{N_{\text{active}}}$) (`source-reported`).
- **Transaction Cost Accounting:** Dedicated two-sided friction model penalizing every position change by $2 \times \text{cost\_bps}$ (one fee per leg):
  $$\Delta \text{pos}_t = |\text{pos}_t - \text{pos}_{t-1}| > 0 \implies R_{t}^{\text{net}} = R_{t}^{\text{gross}} - 2 \cdot \frac{\text{cost\_bps}}{10^4}$$
  Evaluated across four discrete friction tiers: $0, 5, 10, 20$ bps per leg (`source-reported`).
- **Short Borrow Frictions:** Unmodeled in primary source codebase (`research-proposed` limitation). S&P 500 large-cap short borrow fees are assumed general collateral (25–50 bps annualized), but hard-to-borrow spikes during market dislocations are not tracked.
- **Slippage and Impact:** Market impact and order book depth are not explicitly modeled; large-cap S&P 500 constituents are assumed to absorb weekly rebalancing flow without substantial price impact (`research-proposed`).

## Evidence

### Source-reported

#### 1. Out-of-Sample Test Period Performance (2018–2025, 418 Weeks, 0 bps Friction)
All metrics computed out-of-sample over 418 weekly periods from 2018-01-03 to 2025-12-31 (`Examples/DTW-OCP-TOP-naive_clustering_comparison_SP_500.ipynb`, Cells 28–31):

| Metric | DTW (17 pairs) | OCP (20 pairs) | TOP (16 pairs) | Naive Buy-Hold (^GSPC) |
| :--- | :--- | :--- | :--- | :--- |
| **Total Cumulative Return** | **+88.72%** (0.8872) | **+94.86%** (0.9486) | +60.26% (0.6026) | — |
| **Annualized Sharpe Ratio** | **0.7827** (0.783) | **0.6960** (0.696) | 0.2710 (0.271) | 0.3853 (0.385) |
| **Sortino Ratio** | **1.2840** | **1.0528** | 0.3936 | 0.5245 |
| **Calmar Ratio** | **0.9471** | **0.6733** | 0.3405 | 0.3055 |
| **Maximum Drawdown** | **-11.65%** (-0.1165) | **-17.53%** (-0.1753) | -22.02% (-0.2202) | -18.65% (Bull) / -81.74% (Bear) |
| **Weekly Win Rate** | **58.61%** (245/418) | **58.13%** (243/418) | 56.46% (236/418) | — |
| **Active Pairs Ratio** | 100% (17/17) | 100% (20/20) | 100% (16/16) | — |

#### 2. Transaction Cost Sensitivity (Test Period Sharpe Ratio)
Testing robustness to friction deductions applied to both legs on every position transition (`Examples/DTW-OCP-TOP-naive_clustering_comparison_SP_500.ipynb`, Cell 33):

| Strategy | 0 bps | 5 bps | 10 bps | 20 bps |
| :--- | :--- | :--- | :--- | :--- |
| **DTW** | **0.7827** | **0.7258** | **0.6688** | **0.5541** |
| **OCP** | **0.6960** | **0.6490** | **0.6018** | **0.5075** |
| **Naive Buy-Hold** | 0.3853 | 0.3789 | 0.3724 | 0.3589 |
| **TOP** | 0.2710 | 0.2313 | 0.1915 | 0.1119 |

DTW and OCP retain Sharpe ratios of $0.5541$ and $0.5075$ at 20 bps friction per leg, substantially exceeding naive buy-and-hold ($0.3589$). TOP degrades below naive buy-and-hold at only 5 bps friction.

#### 3. Regime-Conditional Asymmetry (Bear vs. Bull Markets, 2018–2025)
Evaluating performance partitioned into 59 independently documented bear-market weeks (Q4 2018 correction, 2020 COVID crash, 2022 bear market) vs. 359 bull-market weeks (`Examples/Four-way-comparison-bull-and-bear-market-analysis.ipynb`, Cells 1–4):

| Regime | Strategy | Sharpe | Sortino | Calmar | Max Drawdown | Weeks |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Bear Market** | **DTW** | **+0.1156** | **+0.1630** | **+0.5122** | **-10.67%** | 59 |
| **Bear Market** | **OCP** | **-0.1972** | **-0.2714** | **+0.2992** | **-9.22%** | 59 |
| **Bear Market** | **TOP** | -1.6591 | -1.8773 | -0.5670 | -23.42% | 59 |
| **Bear Market** | **Naive Buy-Hold** | -2.6112 | -2.7422 | -0.8919 | -81.74% | 59 |
| **Bull Market** | **Naive Buy-Hold** | **1.3693** | **2.2462** | **1.3723** | -18.65% | 359 |
| **Bull Market** | **DTW** | **0.8919** | **1.5086** | **1.3911** | **-8.59%** | 359 |
| **Bull Market** | **OCP** | **0.8186** | **1.2525** | **1.2228** | **-10.87%** | 359 |
| **Bull Market** | **TOP** | 0.5798 | 0.8827 | 0.7872 | -13.86% | 359 |

#### 4. Statistical Significance Testing (5,000-Iteration Block Bootstrap, Block Size = 8 Weeks)
Applying circular block bootstrap with Benjamini-Hochberg FDR correction across pairwise differences (`Examples/Four-way-comparison-bull-and-bear-market-analysis.ipynb`, Cell 3):

- **Bear Market Comparisons (59 weeks):**
  - **DTW vs. Naive:** Sharpe diff $= +2.7269$ ($95\%\text{ CI } [0.9342, 4.4190]$, raw $p = 0.0020$, BH-corrected $p = 0.0060$) $\to$ **Statistically Significant**.
  - **OCP vs. Naive:** Sharpe diff $= +2.4140$ ($95\%\text{ CI } [1.2510, 3.5252]$, raw $p = 0.0000$, BH-corrected $p = 0.0000$) $\to$ **Statistically Significant**.
  - **DTW vs. TOP:** Sharpe diff $= +1.7748$ ($95\%\text{ CI } [0.4753, 3.1863]$, raw $p = 0.0080$, BH-corrected $p = 0.0120$) $\to$ **Statistically Significant**.
  - **OCP vs. TOP:** Sharpe diff $= +1.4619$ ($95\%\text{ CI } [0.4673, 2.4662]$, raw $p = 0.0080$, BH-corrected $p = 0.0120$) $\to$ **Statistically Significant**.
  - **DTW vs. OCP:** Sharpe diff $= +0.3129$ ($95\%\text{ CI } [-1.3514, 2.1073]$, raw $p = 0.7576$, BH-corrected $p = 0.7576$) $\to$ **Not Significant** (indistinct).
  - **TOP vs. Naive:** Sharpe diff $= +0.9521$ ($95\%\text{ CI } [-0.3060, 2.0697]$, raw $p = 0.1680$, BH-corrected $p = 0.2016$) $\to$ **Not Significant**.
- **Bull Market Comparisons (359 weeks):**
  - None of the pairwise differences reach statistical significance after Benjamini-Hochberg correction (all BH-corrected $p \ge 0.4018$). Although Naive point-estimate Sharpe exceeds DTW and OCP by $\sim 0.48$ to $0.55$, the difference is not statistically distinguishable from zero under block bootstrapping.

#### 5. Look-Ahead Bias Contamination and Candidate Reversal Proof (10-Year Study, 2014–2023)
In the companion 10-year study (`papers/draft.md`), the author evaluated the effect of information leakage by comparing full-sample candidate screening against strict Train-only screening:
- **Full-Sample Contamination (2014–2023):** Cointegration testing run across the entire period yielded 46 unique OCP candidate pairs vs. 21 unique DTW candidate pairs, creating the illusion that OCP was twice as prolific. Backtest Sharpe ratios were wildly inflated, with OCP-only pairs averaging Sharpe $11.06$ and a single pair (`CHRW/JNJ`) recording Sharpe $181.38$ on a single trade.
- **Strict Train-Only Partitioning (2014–2017):** Restricting clustering and cointegration strictly to Train reversed the prolificacy ordering: DTW identified 65 unique candidate pairs vs. OCP's 40 unique pairs. Only 10 of 27 final candidate pairs (37%) generated any trades in Test. Active pairs recorded median Sharpe of $8.18$ (DTW-only) and $2.56$ (joint DTW+OCP), eliminating the implausible triple-digit Sharpe artifacts.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Empirical Falsification of Thermal Optimal Path (TOP):** Despite achieving the highest pairwise clustering agreement with OCP ($ARI = 0.740$ at $k=2$), TOP decisively underperformed OCP across all metrics in the Test period (Sharpe $0.2710$ vs. $0.6960$, Sortino $0.3936$ vs. $1.0528$, Calmar $0.3405$ vs. $0.6733$, Bear Sharpe $-1.6591$ vs. $-0.1972$). Under 5,000-iteration block bootstrap testing, TOP's underperformance relative to OCP in bear markets is statistically significant ($p = 0.0120$ BH-corrected). Averaging across an ensemble of near-optimal paths at finite temperature $T=0.5$ dilutes the sharp lead-lag boundaries captured by OCP, generating excessive noise and unviable transaction drag.
2. **Pooled Test Period Indistinguishability from Naive Buy-and-Hold:** Across the full 7-year Test period (2018–2025, 418 weeks), neither DTW (Sharpe diff $+0.3973$, $p = 0.5792$ BH-corrected) nor OCP (Sharpe diff $+0.3107$, $p = 0.6330$ BH-corrected) demonstrated statistically significant Sharpe outperformance over simple S&P 500 buy-and-hold in the unconditional pooled sample. The statistical edge is entirely regime-specific.
3. **Severe Bull Market Return Drag:** In sustained equity bull runs (such as 2021), market-neutral pairs strategies significantly lag broad equity beta. Naive buy-and-hold achieved a bull-market Sharpe of $1.3693$ and Sortino of $2.2462$, compared to DTW's $0.8919$ and OCP's $0.8186$.
4. **Candidate Inactivity and Repricing Jumps:** In the 10-year study, 63% of candidate pairs generated zero trades during the out-of-sample window. Among active pairs, performance was heavily concentrated in discrete repricing jumps (e.g., `BIIB/KSS`, `ALLE/ICE`, and `LH/WAT` with Sharpe $11.95$ over only 4 trades), demonstrating vulnerability to small-sample estimation noise.
5. **Adjusted Rand Index Decoupling from Trading Realities:** High clustering agreement between methods did not translate into comparable PnL. OCP and TOP shared $ARI = 0.740$ yet diverged by $0.425$ in Sharpe, whereas DTW and OCP had a lower $ARI = 0.618$ but virtually identical bear-market performance ($p = 0.7576$), confirming that geometric clustering similarity does not imply economic co-viability.

## Falsification plan

To falsify the hypothesis that elastic clustering (DTW/OCP) identifies genuine regime-conditional statistical arbitrage alpha:

1. **Bear-Market Alpha Falsification Test:**
   - *Protocol:* Execute the exact DTW/OCP pipeline across alternative market crisis regimes omitted from the Test sample (e.g., the 2008 Global Financial Crisis, August 2015 flash crash, or 2026+ out-of-sample downturns).
   - *Data:* Daily/weekly log returns of S&P 500 constituents with strict point-in-time membership.
   - *Decision Rule (`research-defined falsification threshold`):* If the portfolio Sharpe ratio of DTW or OCP during bear-market weeks falls below zero ($\text{Sharpe}_{\text{bear}} < 0.0$) or fails to outperform the benchmark by at least $1.0$ Sharpe point at 10 bps friction, the crisis-alpha hypothesis is falsified.
2. **Dynamic Beta Neutrality and Factor Exposure Test:**
   - *Protocol:* Regress weekly portfolio spread returns against the Fama-French 5-factor model plus momentum (Carhart 4-factor / Fama-French 5-factor) and the S&P 500 index return:
     $$R_{p, t} = \alpha + \beta_{\text{Mkt}} R_{\text{Mkt}, t} + \beta_{\text{SMB}} \text{SMB}_t + \beta_{\text{HML}} \text{HML}_t + \epsilon_t$$
   - *Decision Rule (`research-defined falsification threshold`):* If the multi-factor regression intercept $\alpha$ is statistically indistinguishable from zero ($t_\alpha < 2.0$, $p > 0.05$) or if market beta $|\beta_{\text{Mkt}}|$ exceeds $0.15$ during bear periods, the apparent alpha is falsified as unhedged directional market beta.
3. **Surrogate Shuffle / Placebo Test:**
   - *Protocol:* Generate 500 surrogate universes by phase-randomizing the rolling Sharpe ratio series while preserving univariate power spectra, or randomly re-assigning stocks to pseudo-clusters of identical size distributions.
   - *Decision Rule (`research-defined falsification threshold`):* If the empirical Test-period Sharpe ratio of DTW or OCP falls below the 95th percentile of the randomized cluster distribution ($p_{\text{placebo}} > 0.05$), the clustering distance metric has zero economic identification power and is falsified as data snooping.
4. **Short Borrow and Locates Cost Stress:**
   - *Protocol:* Deduct actual historical stock loan fees (Markit / rebate rate data) and simulate hard-to-borrow short recalls during market stress periods.
   - *Decision Rule (`research-defined falsification threshold`):* If net annualized Sharpe drops by more than $50\%$ or falls below $0.30$ under a realistic borrow fee schedule ($50$ bps general collateral, $300$ bps for hard-to-borrow tails), the tradability of the strategy is falsified.

## Crypto portability

Portability classification: **adapted / unproven** (`research-proposed`).

The author exclusively studies US cash equities (S&P 500 constituents). Porting DTW/OCP clustering pairs trading to cryptocurrency markets requires adapting the framework to cryptocurrency perpetual and spot dynamics:

1. **Continuous 24/7 Session vs. Weekly Wednesday Sampling:** Crypto markets trade continuously without weekend or holiday breaks. A weekly Wednesday snapshot ignores substantial intraday volatility and liquidation cascades. Adapting the model requires high-frequency sampling (e.g., 4-hour or 8-hour bars aligned to funding intervals) (`research-proposed`).
2. **Perpetual Funding Rate Drag:** In crypto perpetual futures, holding short and long legs incurs continuous 8-hour funding rates. If pair components exhibit persistent funding rate differentials, the cost can easily exceed $15–30\%$ annualized, rapidly eroding the thin spread alpha (`research-proposed`).
3. **Extreme Cross-Sectional Turnover and Delisting:** S&P 500 equities exhibit multi-decade survival; crypto tokens have high mortality, sudden delisting, and regulatory halting risks. Running a 6-year Train period to trade forward for 7 years is impossible in crypto, where the universe shifts dynamically over 6–12 months (`research-proposed`).
4. **Cross-Exchange Basis and Execution Fragmentation:** Crypto liquidity is fragmented across Binance, OKX, Bybit, and decentralized venues. Basis divergence between mark price, index price, and order book top-of-book creates severe slippage during liquidation dislocations (`research-proposed`).
5. **Portability Verdict:** The core concept of causality-constrained alignment (OCP) identifying lead-lag informational propagation is theoretically well-suited to crypto (e.g., BTC/ETH leading mid-cap altcoins), but requires a rolling walk-forward refit window (e.g., 90-day Train, 30-day Test) and explicit funding rate integration before any empirical claim can be substantiated (`research-proposed`).

## Limitations

- **Retail Data Survivorship Gap (`source-reported`):** yfinance does not preserve historical prices for constituents delisted prior to the 2026 query date. While the initial roster was survivorship-free as of January 2005 (`fja05680/sp500`), only 267 of 495 stocks survived data extraction, introducing conditioning on long-term survival.
- **Unmodeled Short Borrow Frictions (`research-proposed`):** The backtest engine does not deduct short borrow financing costs or model locate availability during severe market stress events.
- **Weekly Frequency and Discrete Repricing (`source-reported`):** Weekly sampling aggregates away execution microstructure. Individual pair performance is heavily reliant on a small number of discrete repricing jumps rather than continuous mean reversion.
- **Static Formation-Period Bias (`source-reported`):** Pairs are selected once on the 6-year Train window and held fixed across the subsequent 14 years. A rolling walk-forward re-clustering scheme was not implemented.
- **Unhedged Beta Exposure (`research-proposed`):** Dynamic Kalman hedge ratios ($\beta_t$) fluctuate, creating time-varying net market dollar exposure ($\beta_{\text{net}} \ne 0$) that can leak market risk into supposedly neutral spreads.
- **Thermal Optimal Path Failure (`source-reported`):** TOP free-energy ensemble averaging was empirically falsified, proving that temperature-based path averaging degrades the precision of lead-lag pair selection.

## Implementation status

`not-implemented`.

This record represents a research capture and empirical evaluation. No production implementation has been deployed to `nautilus-quant-system`, PyBroker, NautilusTrader, Paper, Testnet, or Live environments.

## Adoption boundary

`research-only`, `not-approved`.

Approval scope is strictly research-only. Inclusion of this document in `alpha-strategy-research` does not constitute approval for live capital deployment, paper trading, or automated execution. Any implementation decision requires independent validation within NautilusTrader, execution modeling with explicit funding and borrow schedules, and approval by quantitative review.

## Related Wiki records

- `[[quant/sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12]]`
- `[[quant/sp500-sector-pairs-causal-residual-pca-area-asymmetry-2026-09-12]]`
- `[[quant/sp500-pairs-trading-forensic-falsification-unbounded-beta-kalman-phantom-pnl-2026-09-12]]`
- `[[quant/tether-pairs-trading-fdr-kalman-half-life-net-beta-2026-09-12]]`
- `[[quant/johansen-cointegration-etf-pairs-friction-asymmetry-falsification-2026-09-12]]`
- `[[quant/pairs-trading-adf-stationarity-filter-walk-forward-falsification-2026-09-12]]`
- `[[quant/ou-first-passage-time-bands-fdr-stability-portfolio-stat-arb-2026-09-12]]`
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/sharpe-deflated-multiple-testing-2026-08-27]]`

## Sources

1. **Wyatt Earls (`WyattEarls`)**, *"DTW-OTP-Pairs-Trading: Research repository exploring pair-trading strategies using Dynamic Time Warping (DTW) variants and the Optimal Thermal Path (OTP) framework, benchmarked against correlation-based and cointegration methods"*. Public GitHub repository, immutable commit `eaf13d18fba4079c827d91ba35bd025e7968da68`, committed September 12, 2026.
   - Repository: [https://github.com/WyattEarls/DTW-OTP-Pairs-Trading](https://github.com/WyattEarls/DTW-OTP-Pairs-Trading)
   - Commit Tree: [https://github.com/WyattEarls/DTW-OTP-Pairs-Trading/tree/eaf13d18fba4079c827d91ba35bd025e7968da68](https://github.com/WyattEarls/DTW-OTP-Pairs-Trading/tree/eaf13d18fba4079c827d91ba35bd025e7968da68)
2. **Wyatt Earls**, *"Pairs Selection via DTW and OCP Clustering: Evidence of Regime-Dependent Performance on the S&P 500"*. Technical manuscript and research paper, September 2026.
   - Source Path: [`papers/Pairs Selection via DTW and OCP Clustering: Evidence of Regime-Dependent Performance on the S&P 500.md`](https://github.com/WyattEarls/DTW-OTP-Pairs-Trading/blob/eaf13d18fba4079c827d91ba35bd025e7968da68/papers/Pairs%20Selection%20via%20DTW%20and%20OCP%20Clustering:%20Evidence%20of%20Regime-Dependent%20Performance%20on%20the%20S%26P%20500.md)
3. **Wyatt Earls**, *"Pairs Selection via DTW and OCP Clustering: Evidence of Regime-Dependent Performance on the S&P 500 (Extended Monograph & Draft)"*, September 2026.
   - Source Path: [`papers/draft.md`](https://github.com/WyattEarls/DTW-OTP-Pairs-Trading/blob/eaf13d18fba4079c827d91ba35bd025e7968da68/papers/draft.md)
4. **Wyatt Earls**, *"DTW vs OCP vs TOP Clustering — S&P 500, 20-Year Three-Period Framework Notebook"*. Jupyter Notebook, September 2026.
   - Source Path: [`Examples/DTW-OCP-TOP-naive_clustering_comparison_SP_500.ipynb`](https://github.com/WyattEarls/DTW-OTP-Pairs-Trading/blob/eaf13d18fba4079c827d91ba35bd025e7968da68/Examples/DTW-OCP-TOP-naive_clustering_comparison_SP_500.ipynb)
5. **Wyatt Earls**, *"Bull/Bear Market Regime Analysis — Four-Way Comparison Notebook"*. Jupyter Notebook, September 2026.
   - Source Path: [`Examples/Four-way-comparison-bull-and-bear-market-analysis.ipynb`](https://github.com/WyattEarls/DTW-OTP-Pairs-Trading/blob/eaf13d18fba4079c827d91ba35bd025e7968da68/Examples/Four-way-comparison-bull-and-bear-market-analysis.ipynb)
6. **Wyatt Earls**, *"OCP and DTW Clustering Exploratory Notebooks"*. Jupyter Notebooks, September 2026.
   - Source Paths: [`Examples/08_OCP_Clustering.ipynb`](https://github.com/WyattEarls/DTW-OTP-Pairs-Trading/blob/eaf13d18fba4079c827d91ba35bd025e7968da68/Examples/08_OCP_Clustering.ipynb), [`Examples/09_DTW_OCP_Clustering_SP500.ipynb`](https://github.com/WyattEarls/DTW-OTP-Pairs-Trading/blob/eaf13d18fba4079c827d91ba35bd025e7968da68/Examples/09_DTW_OCP_Clustering_SP500.ipynb), [`Examples/06_Cointegration_in_Clusters_Test.ipynb`](https://github.com/WyattEarls/DTW-OTP-Pairs-Trading/blob/eaf13d18fba4079c827d91ba35bd025e7968da68/Examples/06_Cointegration_in_Clusters_Test.ipynb)
7. **Johannes Stübinger (2019)**, *"Optimal causal paths in pairs trading"* (Financial Markets and Portfolio Management). Methodological origin for the causality-constrained dynamic programming path algorithm.
8. **Liu et al. (2022)**, *"Thermal Optimal Path method in financial lead-lag analysis"*. Methodological origin for the finite-temperature ensemble formulation.
