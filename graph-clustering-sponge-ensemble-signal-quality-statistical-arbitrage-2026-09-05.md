---
schema: strategy-research-record-v1
title: "Statistical Arbitrage via SPONGE Signed Graph Clustering and Machine Learning Ensemble Signal Quality Filtering: Dynamic Kelly Sizing and Time-Decaying Risk Barriers in US Equities"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - pairs-trading
  - graph-clustering
  - sponge-clustering
  - machine-learning
  - ensemble-learning
  - histgradientboosting
  - kelly-criterion
  - mean-reversion
  - market-neutral
status: research-only
confidence: high
source_as_of: 2024-06-15
sources:
  - "Adam Korniejczuk and Robert Ślepaczuk, 'Statistical arbitrage in multi-pair trading strategy based on graph clustering algorithms in US equities market', arXiv:2406.10695v1 [q-fin.TR], June 2024. https://arxiv.org/abs/2406.10695"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Statistical Arbitrage via SPONGE Signed Graph Clustering and Machine Learning Ensemble Signal Quality Filtering: Dynamic Kelly Sizing and Time-Decaying Risk Barriers in US Equities

## Provenance

- **Primary Source:** Adam Korniejczuk and Robert Ślepaczuk (Quantitative Finance Research Group, Department of Quantitative Finance, Faculty of Economic Sciences, University of Warsaw), *"Statistical arbitrage in multi-pair trading strategy based on graph clustering algorithms in US equities market"*, arXiv preprint `arXiv:2406.10695v1 [q-fin.TR]`, dated June 15, 2024.
- **Canonical arXiv URL:** [https://arxiv.org/abs/2406.10695](https://arxiv.org/abs/2406.10695)
- **Direct HTML Full Text:** [https://arxiv.org/html/2406.10695v1](https://arxiv.org/html/2406.10695v1)
- **Primary LaTeX Source Package:** Inspected directly from official arXiv source bundle `arXiv:2406.10695` containing `arXiv_paper.tex` (936 lines) and associated figures. All mathematical formulas, network hyperparameters, calibration procedures, cross-validation grids, and empirical performance metrics in this record trace directly to this primary LaTeX source.
- **Pre-Write Deduplication & Identity Audit:** A comprehensive repository-wide audit verified zero matches for `2406.10695`, `Korniejczuk`, or this specific multi-pair graph clustering statistical arbitrage methodology across all 373 existing markdown records. While the repository contains statistical arbitrage records utilizing high-frequency order flow, quantum photonic clustering (`gaussian-boson-sampling-asset-clustering-statistical-arbitrage-2026-09-02.md`), or LSTM factor residual modeling (`statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05.md`), this record investigates an independent, non-overlapping paradigm: the extension of the Cartea, Cucuringu, and Jin (2023) SPONGE signed graph clustering framework through a multi-model soft-voting machine learning ensemble meta-classifier (optimizing Brier score on in-sample signals), dynamic Kelly criterion fraction allocation, and time-decaying probability-weighted exit barriers to overcome the crippling transaction-cost drag of high-frequency statistical arbitrage.

## Economic mechanism

### Source-reported

In classical statistical arbitrage and pairs trading (Gatev et al. 2006; Avellaneda & Lee 2008), pairs or clusters of securities are formed based on historical correlation, cointegration, or fundamental sector groupings (e.g. Fama-French 48 industries). Trading rules exploit short-term price divergences from an established equilibrium, anticipating that market forces will drive asset prices back toward parity.

However, classical pairs trading faces two severe limitations:
1. **Proliferation & Alpha Decay:** Increased adoption of simple distance, correlation, or cointegration metrics has degraded returns over the last two decades (Bredthauer & Stübinger 2017; Do & Faff 2012).
2. **Combinatorial Fragility & Fixed Sector Flaws:** Pre-defined industrial sectors fail to capture dynamic cross-industry relationships, supply-chain links, and latent macroeconomic exposures that evolve continuously over time.

Cartea, Cucuringu, and Jin (2023) introduced a graph-theoretic approach to statistical arbitrage:
- Equities are represented as vertices in an undirected, signed, weighted graph where edge weights correspond to Pearson correlations of asset returns over a rolling window.
- Graph clustering algorithms—specifically the Signed Positive Over Negative Generalized Eigenproblem ($\text{SPONGE}_{sym}$; Cucuringu et al. 2019)—partition the market into endogenous, time-varying clusters without imposing arbitrary sector boundaries.
- Trading signals are formed by opening long positions in stocks whose trailing cumulative returns fall below their cluster mean and shorting stocks whose returns exceed their cluster mean.

**The Transaction-Cost Bottleneck:** The original Cartea et al. (2023) baseline trades at a high frequency (rebalancing every 3 trading days with a 5-day lookback window). When realistic equity transaction costs (0.05% per trade) are applied, the strategy collapses:
- Annualized return crashes from 10.24% (Sharpe 1.17) without transaction costs to 2.44% (Sharpe 0.28) with costs.
- Cumulative transaction costs incurred are four times larger than the net profit generated by the strategy, turning periods of modest growth into multi-year drawdowns and stagnation.

**The Authors' Proposed Solution:** Korniejczuk & Ślepaczuk propose resolving this transaction-cost problem through an integrated four-pillar framework:
1. *Turnover Reduction:* Extend the rebalancing period from 3 days to 10 trading days, and the correlation lookback window from 5 days to 30 days.
2. *Signal Quality Meta-Classification:* Train an ensemble of machine learning classifiers (MLP, AdaBoost, HistGradientBoosting, SGD, Logistic Regression) using both graph-theoretic and price-action features to predict whether a raw mean-reversion signal has a high probability of profitability, executing only the top ~10% highest-conviction signals ($P \ge 0.60$).
3. *Optimal Capital Allocation via Kelly Criterion:* Scale position sizes using the Kelly criterion fraction $f = 2P - 1$, allocating more capital to signals with higher modeled win probabilities.
4. *Time-Variant, Probability-Weighted Risk Barriers:* Dynamically lower take-profit and stop-loss barriers as time elapses within the 10-day holding cycle, weighted by the model's estimated win probability, to lock in profits early and cut risk on stale positions.

### Research interpretation

1. **Graph Clustering as Latent Structure Recovery:** Unlike rigid GICS sectors, signed graph clustering on correlation matrices dynamically isolates clusters of equities sharing joint exposure to unobserved risk factors, liquidity regimes, or supply-chain shocks. The $\text{SPONGE}_{sym}$ algorithm explicitly leverages negative correlations as repulsive forces and positive correlations as attractive forces, identifying balanced clusters that minimize internal friction.
2. **Meta-Labeling / Signal Quality Filtering as an Alpha Enhancer:** The machine learning classifiers are not tasked with forecasting the direction of stock prices (a notoriously noisy task). Instead, they act as an *execution hurdle / meta-label filter* on pre-generated mean-reversion signals. By predicting the likelihood of reaching a profit barrier ($T = 4\%$) or finishing positive at the rebalance boundary, the ensemble drastically improves the signal-to-noise ratio and eliminates marginal trades that bleed transaction costs.
3. **Severe Right-Tail Distressed Stock Vulnerability:** Crucially, the authors' own sensitivity analysis uncovers a vital structural vulnerability: the extraordinary headline return (49.33% ARC) is heavily dependent on two specific distressed, low-liquidity, high-volatility microcap/penny stocks that were historically present in the S&P 500 index during the backtest: El Paso / Emporium Petroleum (ticker `EP`) and Ocean Thermal Energy Corp (ticker `CPWR`). Excluding these two names collapses ARC from 49.33% to 10.73% and extends maximum loss duration to 9.38 years. This proves that a large portion of the reported performance does not stem from pure, diversified market-neutral statistical arbitrage, but from a systemic bias toward buying deeply oversold, distressed assets with extreme right-tail skewness that occasionally stage massive relief rallies.

## Signal

The trading signal operates as a multi-stage quantitative pipeline executed every 10th trading day:

### 1. Graph Construction and SPONGE Clustering (`source-reported`)
- **Universe:** Active constituents of the S&P 500 on trading day $t$ (tracked dynamically from historical constituent records).
- **Lookback Window:** $W = 30$ trading days of daily adjusted close returns.
- **Adjacency Matrix:** Symmetrical correlation matrix $A \in \mathbb{R}^{G \times G}$ where $G$ is the number of active stocks on day $t$.
- **Signed Laplacian Formulation:**
  - Decompose $A = A^+ - A^-$, where $A_{ij}^+ = \max(A_{ij}, 0)$ and $A_{ij}^- = \max(-A_{ij}, 0)$.
  - Degree matrices: $D^+ = \text{diag}(\sum_{j=1}^G A_{ij}^+)$ and $D^- = \text{diag}(\sum_{j=1}^G A_{ij}^-)$.
  - Symmetrically normalized Laplacians:
    $$L_{sym}^+ = (D^+)^{-1/2}(D^+ - A^+)(D^+)^{-1/2} = I - (D^+)^{-1/2}A^+(D^+)^{-1/2}$$
    $$L_{sym}^- = (D^-)^{-1/2}(D^- - A^-)(D^-)^{-1/2} = I - (D^-)^{-1/2}A^-(D^-)^{-1/2}$$
  - Solve the generalized eigenproblem: find the $K$ smallest generalized eigenvectors of $(L_{sym}^+ + \tau^- I, L_{sym}^- + \tau^+ I)$.
  - Optimal number of clusters $K$: determined by the smallest number of eigenvectors required to explain 90% of total correlation matrix variance.
  - $K$-means++ algorithm applied to the resulting $K$-dimensional Euclidean coordinates to partition vertices into $K$ disjoint clusters $\{C_1, C_2, \dots, C_K\}$.

### 2. Raw Signal Generation (`source-reported`)
- For each cluster $C_k$, compute the mean 5-day cumulative return of all constituent stocks:
  $$\overline{R}_{C_k} = \frac{1}{|C_k|} \sum_{i \in C_k} R_i^{(5)}$$
  where $R_i^{(5)}$ is the cumulative return of stock $i$ over the trailing 5 trading days.
- **Raw Directional Triggers:**
  - If $R_i^{(5)} < \overline{R}_{C_k}$: candidate **Long** signal (stock is oversold relative to its cluster).
  - If $R_i^{(5)} > \overline{R}_{C_k}$: candidate **Short** signal (stock is overbought relative to its cluster).

### 3. Feature Extraction for Signal Quality Classifier (`source-reported`)
For each generated candidate signal, 14 normalized features are extracted:
- **Graph-Based Features:**
  1. *Local Vertex Degree:* $\frac{\sum_{n=1}^S e_{i,n} - 1}{S - 1}$ (where $e_{i,n}$ is edge weight, $S = |C_k|$ is cluster/sub-graph size).
  2. *Global Vertex Degree:* $\frac{\sum_{n=1}^G e_{i,n} - 1}{G - 1}$ (where $G$ is full graph size).
  3. *Graph Density:* $\frac{\sum_{i=1}^S (\sum_{n=1}^S e_{i,n} - 1)}{S(S - 1)}$.
  4. *Cluster Size:* $\frac{|C_k|}{G}$.
  5. *Normalized Number of Clusters:* $\frac{K}{G}$.
- **Conventional Price-Action Features:**
  6. Cumulative return deviation from cluster mean over last 5 days: $R_i^{(5)} - \overline{R}_{C_k}$.
  7. Sign of deviation: $+1$ for long candidates, $-1$ for short candidates.
  8. Mean cluster return over trailing 10 trading days.
  9. Mean individual stock return over trailing 10 trading days.
  (Plus additional derived metrics totaling 14 features, normalized using `MinMaxScaler`).

### 4. Machine Learning Ensemble Quality Classifier (`source-reported`)
- **In-Sample Training Dataset:** Formed from the first 1,500 trading days (2000 to approx. March 2006). A signal is labeled positive ($Y=1$) if cumulative return reaches take-profit threshold $T = 4\%$ at daily close within the 10-day holding cycle, OR if cumulative return at the 10th-day rebalance exceeds transaction costs (no net loss). Otherwise $Y=0$. Split: 80% training, 20% validation.
- **Tuned Classifiers (optimizing Brier score):**
  1. *Multi-layer Perceptron (MLP):* 2 hidden layers $(64, 64)$, ReLU activation, constant lr, Adam solver, batch size 200, $\alpha = 10^{-6}$. (Validation Brier: 0.243, Precision: 0.568).
  2. *AdaBoost:* 100 estimators, learning rate 0.001. (Validation Brier: 0.247, Precision: 0.544).
  3. *HistGradientBoosting (LightGBM):* Learning rate 0.1, auto early stopping, max iter 100. (Validation Brier: 0.218, Precision: 0.653 — best individual model).
  4. *SGD Classifier:* Modified Huber loss, L2 penalty, $\alpha = 0.001$, max iter 200, optimal learning rate. (Validation Brier: 0.247, Precision: 0.547).
  5. *Logistic Regression:* $C = 8$, L2 penalty, lbfgs solver, max iter 75, balanced class weight. (Validation Brier: 0.249, Precision: 0.580).
- **Soft-Voting Ensemble Combination:**
  $$P(\text{Profitable}) = \frac{1}{3} P_{\text{HistGB}} + \frac{1}{6} P_{\text{MLP}} + \frac{1}{6} P_{\text{AdaBoost}} + \frac{1}{6} P_{\text{SGD}} + \frac{1}{6} P_{\text{LogReg}}$$
- **Probability Filter Threshold:** Only candidate signals with $P \ge 0.60$ (corresponding to the 90th percentile of predicted probabilities on validation data) are accepted for trading. Signals with $P < 0.60$ are discarded.

### 5. Position Sizing via Kelly Criterion (`source-reported`)
- For each accepted signal $i$ with win probability $P_i \ge 0.60$, the unscaled Kelly fraction is:
  $$f_i = 2P_i - 1$$
- Fractions are normalized separately across long and short baskets:
  $$w_i^{\text{long}} = \frac{f_i}{\sum_{k \in \text{Long}} f_k}, \quad w_j^{\text{short}} = \frac{f_j}{\sum_{k \in \text{Short}} f_k}$$
  ensuring dollar-neutral market exposure ($\sum w^{\text{long}} = 1.0$, $\sum w^{\text{short}} = 1.0$).

### 6. Dynamic Risk Management: Time-Variant & Probability-Weighted Barriers (`source-reported`)
- Positions are held for a maximum of 10 trading days ($TD \in \{1, 2, \dots, 9\}$ days elapsed since rebalance).
- **Time-Variant, Probability-Weighted Take Profit:**
  $$Threshold_{tp}(TD, P_i) = THR \times \frac{10 - TD}{10} \times P_i$$
  with base scaling factor $THR = 0.08$. As $TD$ increases, the take-profit barrier monotonically tightens.
- **Time-Variant, Probability-Weighted Stop Loss:**
  $$Threshold_{sl}(TD, P_i) = 0.05 \times \frac{10 - TD}{10} \times P_i$$
  with base scaling factor $0.05$.
- Barriers are evaluated at the daily adjusted close. If either barrier is breached, the position is immediately liquidated at close, and the released capital remains in cash until the next scheduled rebalance date.
- Intraday fill model and execution delay: `research-proposed` (source assumes execution at adjusted close; in live deployment, order must execute at next-bar open or TWAP over the subsequent session to eliminate close-to-close lookahead and bid-ask crossing).
- Hard liquidity and penny-stock filter: `research-proposed` (to eliminate distressed penny-stock distortion, reject any stock with unadjusted price $< \$5.00$ or trailing 30-day median dollar volume $< \$10\text{M}$).

## Required data

- **Asset Universe:** Active historical constituents of the S&P 500 index. Sourced dynamically from historical constituent change logs (Farrell 2024 repository).
- **Time Horizon & Cadence:** Daily frequency, spanning January 1, 2000 to December 31, 2022.
  - In-sample model training & validation: First 1,500 trading days (2000–03.2006).
  - Out-of-sample backtest: March 2006 to December 2022 (4,225 trading days / 16.8 years).
- **Price Fields:** Daily adjusted closing prices (Yahoo Finance). Used for return calculation, correlation matrix estimation, signal triggers, and barrier evaluations.
- **Point-in-Time Integrity:** Constituent membership updated dynamically to reflect historical S&P 500 additions and deletions, mitigating survivorship bias in the index itself (though individual delisted stock price history in Yahoo Finance remains a known limitation).
- **Missing Data Handling:** On dates where individual constituent data is unavailable, the universe size $G$ contracts dynamically; graph features are normalized by $G$ to maintain comparability.

## Execution assumptions

- **Source Assumptions (`source-reported`):**
  - **Transaction Costs:** 0.05% (5 basis points) per trade, applied to both opening and closing transactions (total round-trip cost 0.10%).
  - **Execution Timing:** All entries, exits, take-profit liquidations, and stop-loss closes are assumed to execute exactly at the daily adjusted closing price.
  - **Fractional Shares:** Perfectly fractional share execution assumed.
  - **Financing & Shorting:** Zero short borrow fees, zero margin interest, and zero cash drag on uninvested capital; short positions deposit requires no excess margin capital.
  - **Slippage & Impact:** Zero slippage or market impact assumed.
- **Research Enhancements (`research-proposed`):**
  - **Next-Bar Execution:** Signals generated at bar close $t$ must execute at open of bar $t+1$ or via VWAP over the first 30 minutes of trading to eliminate lookahead bias.
  - **Slippage & Market Impact:** Apply square-root impact model $\Delta P = \eta \sigma \sqrt{Q/V}$ with base slippage of 5–15 bps, especially critical given the high performance sensitivity to low-volume stocks.
  - **Short Borrow Cost:** Incorporate an explicit annual borrow fee (50 bps for general collateral, 300–1000 bps for hard-to-borrow distressed names).

## Evidence

### Source-reported

All empirical figures below trace directly to Adam Korniejczuk & Robert Ślepaczuk (`arXiv:2406.10695v1`, June 2024), evaluated out-of-sample over 4,225 trading days (March 2006 to December 2022):

#### 1. Out-of-Sample Performance Comparison (Table 8 & Table 9)
| Strategy / Benchmark | ARC (%) | ASD (%) | IR* (Sharpe) | Sortino | MDD (%) | MLD (Years) | Calmar (CR) | IR** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Proposed Base Strategy (0.05% TC)** | **49.33%** | 38.01% | **1.30** | **3.38** | 31.98% | 2.10 | **1.54** | **2.00** |
| Cartea et al. Benchmark (0.05% TC) | 1.13% | 9.16% | 0.14 | 0.29 | 34.30% | 2.59 | 0.04 | 0.01 |
| Cartea et al. Benchmark (w/o TC) | 9.01% | **9.14%** | 0.96 | 1.77 | **20.68%** | **1.54** | 0.44 | 0.42 |
| SPY ETF Buy-and-Hold | 9.12% | 20.11% | 0.45 | 0.70 | 55.19% | 4.85 | 0.17 | 0.08 |

- **Student's t-Test vs SPY (Table 9):** Information Ratio difference test yields $t = 2118.84$, $df = 4225$, $p < 0.00001$ ($SE = 0.0004$), rejecting the null hypothesis that strategy IR* does not exceed SPY.

#### 2. Risk Management & Kelly Sizing Sensitivity (Table 10)
- **Base Case (Time-Variant Stops + Kelly):** ARC 49.33%, ASD 38.01%, IR* 1.30, Sortino 3.38, MDD 31.98%, CR 1.54.
- **Flat Base Case + Kelly (Constant Stops):** ARC **52.63%**, ASD 40.29%, IR* **1.31**, Sortino 3.25, MDD 36.05%, CR 1.46.
- **Flat Base Case (No Kelly, Constant Stops):** ARC 50.33%, ASD 38.95%, IR* 1.29, Sortino 3.26, MDD 33.94%, CR 1.48.
- *Finding:* Kelly sizing slightly increases returns (+2.3% to +3.3%) at the expense of higher volatility and drawdown duration. Time-variant probability stops provide modest downside tail protection (reducing MDD from 36.05% to 31.98%), but differences in IR* are marginal (< 2%).

#### 3. Ensemble Architecture Sensitivity (Table 11)
- **Base Case (HistGB Double Weight):** ARC **49.33%**, IR* **1.30**, Sortino **3.38**, MDD **31.98%**.
- **HistGradientBoosting Alone:** ARC 31.58%, IR* 0.91, Sortino 1.89, MDD 50.70%.
- **Equally Weighted Ensemble:** ARC 28.91%, IR* 0.76, Sortino 1.54, MDD 63.95%.
- **Base Case w/o Threshold Rounding (0.602 vs 0.60):** ARC 47.15%, IR* 1.21, Sortino 3.11, MDD 38.83%.

#### 4. Transaction Cost Robustness (Table 12)
- **0% TC:** ARC 54.55%, IR* 1.43, Sortino 3.74, MDD 31.72%.
- **0.05% TC (Base):** ARC 49.33%, IR* 1.30, Sortino 3.38, MDD 31.98%.
- **0.075% TC:** ARC 46.78%, IR* 1.23, Sortino 3.20, MDD 32.11%.
- **0.10% TC:** ARC 44.27%, IR* 1.16, Sortino 3.03, MDD 32.24%.
- *Finding:* The strategy exhibits high immunity to transaction costs; doubling fees to 10 bps per trade causes only a 10.7% decline in IR* (from 1.30 to 1.16).

#### 5. Stop Loss Threshold Sensitivity (Table 13)
- **1% Stop:** ARC 41.54%, IR* 1.18, MDD 32.08%.
- **3% Stop:** ARC 41.93%, IR* 1.17, MDD **28.58%**.
- **5% Stop (Base):** ARC **49.33%**, IR* **1.30**, MDD 31.98%.
- **10% Stop:** ARC 46.00%, IR* 1.18, MDD 41.05%.

#### 6. Rebalance Cadence & Lookback Sensitivity (Table 17)
- **10-day rebalance & 30-day lookback (Base Case):** ARC **49.33%**, IR* **1.30**, MDD **31.98%**.
- **3-day rebalance & 5-day lookback (Cartea baseline with ML):** ARC **-100.0%** (TOTAL BANKRUPTCY), IR* -2.85, MDD 100%.
- **10-day rebalance & 5-day lookback:** ARC 16.78%, IR* 0.50, MDD 54.02%.
- **15-day rebalance & 30-day lookback:** ARC 9.54%, IR* 0.20, MDD 37.67%.
- **10-day rebalance & 45-day lookback:** ARC 37.34%, IR* 0.62, MDD 67.02%.

### Independently reproduced

`Not independently reproduced.` All figures, optimization parameters, cross-validation scores, and ablation metrics cited above represent direct extractions from Korniejczuk & Ślepaczuk (`arXiv:2406.10695v1`, 2024).

### Negative evidence

1. **Extreme Distressed Penny-Stock Dependency (Table 14 & Figure 13):**
   - When the two highest-volatility, low-volume constituents—Emporium Petroleum (`EP`) and Ocean Thermal Energy Corp (`CPWR`)—are excluded from the backtest universe:
     - ARC plunges by **38.6 percentage points** (from 49.33% down to **10.73%**).
     - IR* drops from **1.30 to 0.54** (barely above SPY's 0.45).
     - Sortino collapses from **3.38 to 0.83**.
     - Maximum Drawdown expands from **31.98% to 51.44%**.
     - Maximum Loss Duration blows out from **2.10 years to an intolerable 9.38 years**!
   - This demonstrates that over 75% of the excess compounding generated between 2010 and 2016 was driven by a tiny handful of distressed micro-cap trades hitting extreme take-profit thresholds.
2. **Total Collapse under Baseline Rebalancing Cadence (Table 17):**
   - Forcing the model to run at Cartea et al.'s 3-day rebalancing frequency with 5-day lookback resulted in immediate -100% loss (portfolio bankruptcy), proving that the ML classifiers completely fail when forced into high-turnover regimes with mismatched feature lookbacks.
3. **Severe Degradation under Unrounded Probability Cutoff (Table 11):**
   - Merely changing the acceptance threshold from the rounded $P = 0.60$ to the exact empirical 90th percentile $P = 0.602$ reduced ARC from 49.33% to 47.15% and increased MDD from 31.98% to 38.83%, indicating notable threshold sensitivity.
4. **Post-2016 Stagnation:**
   - As acknowledged by the authors, the equity curve plateaus significantly after 2016, mirroring the general alpha decay observed across statistical arbitrage strategies in US equities.

## Falsification plan

To determine whether the proposed strategy captures a genuine, repeatable market-neutral alpha or merely an unreplicable distressed microcap anomaly, the following empirical tests are mandated:

1. **Out-of-Sample Walk-Forward Extension (2023–2026):**
   - *Test:* Run the fully frozen model pipeline (using models trained on 2000–2005 data) on daily S&P 500 constituents from January 2023 through August 2026.
   - *Decision Rule (`research-defined falsification threshold`):* If net Information Ratio $IR^* < 0.60$ or annualized return $ARC < 10.0\%$ over this out-of-sample window, the strategy is falsified as suffering from irreversible post-sample regime obsolescence.
2. **Liquidity and Penny-Stock Elimination Audit:**
   - *Test:* Impose a strict liquidity gate removing all stocks with unadjusted share price $< \$5.00$ or trailing 30-day median daily dollar volume $< \$10\text{M}$ at the time of signal formation.
   - *Decision Rule (`research-defined falsification threshold`):* If the liquidity-filtered portfolio generates net $ARC < 12.0\%$ or net $IR^* < 0.50$ across 2006–2022, the economic mechanism is falsified as a microcap illiquidity/distress anomaly rather than statistical arbitrage.
3. **Execution Delay & Realistic Borrow/Slippage Stress Test:**
   - *Test:* Re-run the backtest shifting execution from adjusted close $t$ to open of bar $t+1$, incorporating 10 bps slippage per trade and an explicit short borrow fee schedule (minimum 100 bps annual, 500 bps for high-volatility names).
   - *Decision Rule (`research-defined falsification threshold`):* If net Sortino ratio drops below 1.00 or max drawdown exceeds 45.0%, the strategy is falsified as an artifact of frictionless close-price accounting.
4. **Shuffled Cluster Identity (Placebo Test):**
   - *Test:* Randomly permute the cluster assignments $\{C_1, \dots, C_K\}$ across stocks at each rebalance date while maintaining cluster sizes, and re-run signal generation and ML filtering.
   - *Decision Rule (`research-defined falsification threshold`):* If the SPONGE clustering portfolio does not outperform the 95th percentile of 500 randomized cluster placebo iterations ($p > 0.05$), the hypothesis that SPONGE graph topology provides structural alpha is rejected.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`. The cited source evaluates only US equities (S&P 500). Any crypto deployment constitutes a ported hypothesis and research interpretation.
- **Crypto-Specific Adaptation Requirements:**
  1. *Perpetual Futures Multi-Asset Universe:* In crypto, shorting spot assets involves borrow availability friction and exchange fragmentation. The strategy must be adapted to trade high-liquidity perpetual futures contracts (e.g. top 50 perpetual pairs on Binance/Bybit/OKX).
  2. *Funding Rate Drag:* Perpetual contracts incur funding payments every 8 hours. If the strategy goes long an oversold token with deeply negative funding and shorts an overbought token with positive funding, it collects carry; conversely, adverse funding can rapidly erode statistical arbitrage margins. An explicit funding rate hurdle must be incorporated into the signal quality classifier.
  3. *Continuous 24/7 Market Alignment:* Crypto lacks daily market closes. The 10-day rebalance cycle and 30-day rolling correlation windows must be defined using standardized 00:00 UTC boundary intervals.
  4. *High Volatility & Tail Contagion:* Crypto asset correlations spike toward +1.0 during market crashes, causing cluster boundaries to collapse into a single macro factor. SPONGE clustering must be paired with dynamic spectral filtering or a volatility-gated cash circuit breaker.

## Limitations

- **Distressed Stock Sensitivity:** As documented in Table 14, over 75% of excess compounding is concentrated in two distressed penny stocks. The strategy's claimed 49.33% return is not broadly distributed across the 500-stock universe.
- **Frictional Omissions in Primary Source:** The primary study ignores short borrow fees, margin financing costs, bid-ask spread crossing, and intraday market impact, evaluating performance at adjusted daily close prices.
- **Data Gap & Yahoo Finance Survivorship Issues:** Yahoo Finance data contains survivorship gaps for historical bankruptcies and corporate restructuring, which may distort historical cluster returns.
- **Static Feature Lookback Inflexibility:** Features like 10-day cluster returns are hardcoded; when rebalance frequency was varied in sensitivity tests, the model experienced severe breakdown.

## Implementation status

`not-implemented`. This record represents theoretical and empirical research captured from arXiv:2406.10695v1. No implementation in `nautilus-quant-system`, PyBroker, or NautilusTrader has been performed. No backtest campaign has been initiated, and no strategy code has been written to production repositories.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- **Trading Authorization:** None. This research capture does not authorize paper trading, testnet deployment, or live execution. Any future adoption requires resolving the distressed penny-stock dependency, implementing next-bar execution with borrow/slippage costs, and validating performance under independent NautilusTrader backtesting.

## Related Wiki records

- [[quant/statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05]]
- [[quant/gaussian-boson-sampling-asset-clustering-statistical-arbitrage-2026-09-02]]
- [[quant/signature-optimal-execution-statistical-arbitrage-quadratic-reduction-2026-09-02]]
- [[quant/two-level-uncertainty-cross-sectional-ranker-regime-trust-gate-tail-cap-2026-09-05]]
- [[quant/crypto-walk-forward-window-optimization-double-oos-momentum-2026-09-04]]

## Sources

1. Adam Korniejczuk and Robert Ślepaczuk, *"Statistical arbitrage in multi-pair trading strategy based on graph clustering algorithms in US equities market"*, arXiv preprint `arXiv:2406.10695v1 [q-fin.TR]`, submitted June 15, 2024.
   - Abstract: [https://arxiv.org/abs/2406.10695](https://arxiv.org/abs/2406.10695)
   - Full text HTML: [https://arxiv.org/html/2406.10695v1](https://arxiv.org/html/2406.10695v1)
   - Full text PDF: [https://arxiv.org/pdf/2406.10695v1](https://arxiv.org/pdf/2406.10695v1)
2. Álvaro Cartea, Mihai Cucuringu, and Qi Jin, *"Correlation Matrix Clustering for Statistical Arbitrage Portfolios"*, Proceedings of the Fourth ACM International Conference on AI in Finance (ICAIF '23), November 2023, pp. 557–564. DOI: [10.1145/3604237.3626880](https://doi.org/10.1145/3604237.3626880). SSRN: [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4560455](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4560455)
3. Mihai Cucuringu, Peter Davies, Aldo Glielmo, and Hemant Tyagi, *"SPONGE: A Generalized Eigenproblem for Clustering Signed Networks"*, Proceedings of the 22nd International Conference on Artificial Intelligence and Statistics (AISTATS 2019), PMLR 89:1088-1098. arXiv: `arXiv:1904.08575`.
4. John L. Kelly, *"A New Interpretation of Information Rate"*, Bell System Technical Journal, Vol. 35, No. 4, 1956, pp. 917–926.
5. Evan Gatev, William N. Goetzmann, and K. Geert Rouwenhorst, *"Pairs Trading: Performance of a Relative-Value Arbitrage Rule"*, The Review of Financial Studies, Vol. 19, No. 3, 2006, pp. 797–827.
