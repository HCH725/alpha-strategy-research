---
schema: strategy-research-record-v1
title: "Hybrid LSTM-XGBoost Multi-Horizon Return Prediction and Volatility-Penalized Investment Scoring (Mostafa et al. 2026)"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - machine-learning
  - deep-learning
  - lstm
  - xgboost
  - multi-horizon
  - equity-cross-sectional
  - base-rate-falsification
  - composite-scoring
status: research-only
confidence: medium
source_as_of: 2026-09-11
sources:
  - "Seif ElDein Mostafa, Yahia Ahmed, Farah Darwish, and Marwa Solayman, 'A Hybrid LSTM–XGBoost Framework for Multi-Horizon Stock Return Prediction Across Diversified Equity Portfolios', arXiv:2609.13125v1 [cs.LG], submitted September 11, 2026. https://arxiv.org/abs/2609.13125"
  - "Boris Marjanovic, 'Price-Volume Data for All US Stocks and ETFs', Kaggle dataset, 2017. https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Hybrid LSTM-XGBoost Multi-Horizon Return Prediction and Volatility-Penalized Investment Scoring (Mostafa et al. 2026)

## Provenance

- **Primary Source:**
  - Authors: Seif ElDein Mostafa, Yahia Ahmed, Farah Darwish, and Marwa Solayman.
  - Institutional Affiliation: Faculty of Computer Science, October University for Modern Sciences and Arts (MSA University), Giza, Egypt (`source-reported`).
  - Corresponding Emails: `seifeldin.mostafa2@msa.edu.eg`, `yahia.ahmed3@msa.edu.eg`, `fdarwish@msa.edu.eg`, `mmsolayman@msa.edu.eg` (`source-reported`).
  - Title: *A Hybrid LSTM–XGBoost Framework for Multi-Horizon Stock Return Prediction Across Diversified Equity Portfolios*
  - Publication: arXiv preprint `arXiv:2609.13125v1 [cs.LG]`, submitted Friday, September 11, 2026 (`source-reported`).
  - Abstract URL: https://arxiv.org/abs/2609.13125
  - Full-Text HTML: https://arxiv.org/html/2609.13125v1
  - Full-Text PDF: https://arxiv.org/pdf/2609.13125v1
  - Canonical DOI: [10.48550/arXiv.2609.13125](https://doi.org/10.48550/arXiv.2609.13125)
  - License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).
- **Underlying Dataset & Universe:**
  - Source: Boris Marjanovic (2017), *"Price-Volume Data for All US Stocks and ETFs"*, Kaggle repository (`source-reported`).
  - Sample Span: Daily OHLCV data from January 2010 through mid-2016 (test set evaluation culminates in June 2016) (`source-reported`).
  - Universe: 14 U.S. large-cap equities across six industry sectors (`source-reported`):
    - Technology: Apple (AAPL), Nvidia (NVDA), Microsoft (MSFT), Alphabet (GOOGL).
    - Financials: JPMorgan Chase (JPM), Goldman Sachs (GS).
    - Healthcare: Johnson & Johnson (JNJ), Pfizer (PFE).
    - Energy: ExxonMobil (XOM), Chevron (CVX).
    - Consumer: Amazon (AMZN), Walmart (WMT).
    - Industrials: Boeing (BA), Caterpillar (CAT).
- **Repository Deduplication Audit:**
  - Full grep audit across all `.md` records in `alpha-strategy-research`:
    - Zero existing records cite `arXiv:2609.13125`, Mostafa, Solayman, or MSA University.
  - Related gradient-boosting and recurrent hybrid records in the repository:
    - `equity-cross-regime-bayesian-optimisation-xgboost-tabnet-hybrid-2026-09-02.md`: Focuses on XGBoost vs TabNet with Bayesian optimization across market regimes.
    - `crypto-perps-cross-sectional-probit-ridge-xgboost-macd-sellback-2026-09-16.md`: Combines probit Ridge and XGBoost for cross-sectional crypto perpetual funding and MACD exhaustion sellbacks.
    - `hybrid-xgboost-finbert-regime-adaptive-equity-2026-09-04.md`: Fuses FinBERT text sentiment features with XGBoost.
    - `vertifusex-penultimate-temporal-fusion-triple-barrier-cooldown-2026-09-16.md`: Merges LSTM, Bi-LSTM, and St-LSTM penultimate layers via an affine projection for equity indices.
  - Material Differences & Distinctiveness:
    - *Two-Stage Architecture:* Uses a 2-layer stacked LSTM exclusively as a pre-trained, frozen 64-dimensional temporal embedding extractor from 60-day sequences of 5 raw/indicator market features, concatenated with 14 cross-sectional technical indicators into a 78-dimensional input for downstream XGBoost gradient-boosted regression.
    - *Multi-Horizon Horizon Structure:* Concurrently evaluates forward cumulative returns across four horizons ($d \in \{30, 90, 252, 365\}$ trading days) under a multi-stock pooled training paradigm with per-stock chronological MinMax scaling.
    - *Empirical Falsification of Long-Horizon Directional Accuracy:* Documents that headline directional accuracy rising to 97.6% at 365 days is an illusion driven by the positive base rate of returns in secular bull markets (naive always-positive predictor achieves 97.8%, outperforming the model across all horizons by -0.2 to -8.0 percentage points).
    - *Composite Multi-Horizon Investment Scoring:* Formulates a closed-form composite ranking score combining 30d, 90d, and 252d predictions with an all-horizon sign-consistency bonus ($B_c = \pm 10$) and a 20-day realized volatility risk penalty ($-100 \sigma_{20}$).

## Economic mechanism

### Source-reported

1. **Complementary Representational Biases of LSTM and XGBoost:**
   - Financial time series exhibit high non-stationarity, low signal-to-noise ratios, and complex non-linear dynamics (`source-reported`).
   - Standalone Long Short-Term Memory (LSTM) networks capture long-range temporal dependencies and momentum through gated memory cells, but struggle with direct multi-week return magnitude regression when fed unstructured price sequences alone (`source-reported`).
   - Gradient-boosted decision trees (XGBoost) excel at capturing non-linear interactions, sharp thresholds, and interactions among hand-crafted tabular technical indicators, but operate on static cross-sectional snapshots without an intrinsic mechanism to encode temporal ordering across multi-week lookback windows (`source-reported`).
   - Combining the two models into a two-stage pipeline allows the LSTM to compress 60-day historical trajectories into a dense 64-dimensional temporal embedding $\mathbf{h}_T$, which is concatenated with 14 engineered technical indicators to provide XGBoost with both historical temporal dynamics and instantaneous market-structure indicators (`source-reported`).
2. **Cross-Sectional Generalization via Multi-Stock Pooling:**
   - Single-asset forecasting models frequently overfit to ticker-specific idiosyncratic noise or local sample regimes (`source-reported`).
   - Pooling observations from 14 diversified equities across six distinct industry sectors into a unified training corpus forces the LSTM feature extractor and the XGBoost regressor to learn shared cross-sectional dynamics and sector-invariant market patterns (`source-reported`).
   - Per-stock chronological MinMax scaling ensures that cross-asset nominal price disparities (e.g., Berkshire/high-dollar vs low-dollar equities) do not distort the gradient optimization or tree split criteria (`source-reported`).
3. **Multi-Horizon Investment Scoring with Volatility Penalty:**
   - Single-horizon forecasts can be noisy and vulnerable to transient mean reversion (`source-reported`).
   - An actionable investment score requires multi-horizon alignment: the composite score weights short-term ($d=30$), medium-term ($d=90$), and long-term ($d=252$) cumulative return forecasts with weights 20, 30, and 50 respectively, rewards unanimous sign agreement with a $\pm 10$ consistency bonus, and penalizes turbulence using the trailing 20-day realized volatility ($\sigma_{20}$) multiplied by 100 (`source-reported`).

### Research interpretation

- **Latent Sequential Filter vs. Static Tabular Regressor:**
  - The LSTM operates effectively as a non-linear, adaptive state-space filter that projects sequential price-volume momentum and MACD trajectory into an orthogonal coordinate space.
  - The downstream XGBoost trees then partition this hybrid space, enabling regime-dependent decision boundaries (e.g., executing trend-following rules only when the LSTM temporal embedding indicates low regime transition probability).
- **Asymmetric Sector Utility of Sequential Embeddings:**
  - The empirical results show that the addition of the LSTM temporal embedding improves RMSE over standalone XGBoost on 7 of 14 stocks, concentrated heavily in high-beta/high-volatility growth stocks (NVDA, AMZN) and cyclical macro equities (JPM, WMT, CVX).
  - In contrast, low-beta defensive names (JNJ, PFE) show zero benefit or minor degradation from temporal embeddings. This indicates that complex sequential temporal memory provides marginal value in smooth, mean-reverting defensive equities where classical snapshot indicators already capture the available information.
- **Base-Rate Drift Illusion in Financial Machine Learning:**
  - The paper provides an important methodological lesson for financial ML: high long-horizon classification metrics (e.g., 97.6% directional accuracy at 1 year) are predominantly artifacts of market drift during secular bull markets.
  - Benchmarking against a naive "always long" baseline falsifies claims of predictive skill, proving that true alpha must be measured either through risk-adjusted cross-sectional rank IC or through excess accuracy over the prevailing asset-specific base rate.

## Signal

### Preprocessing and Feature Pipelines

1. **Chronological Splitting and Normalization (`source-reported`):**
   - For each equity, data is partitioned strictly chronologically into:
     - In-sample Training: 70% (`source-reported`).
     - Validation: 15% (`source-reported`).
     - Out-of-sample Test: 15% (`source-reported`).
   - Shuffling is strictly prohibited to avoid look-ahead bias (`source-reported`).
   - Per-stock MinMax scaling to $[0, 1]$ is fitted strictly on the training partition and applied to validation and test partitions (`source-reported`).
   - Forward-fill imputation resolves internal missing data; post-indicator warm-up rows containing NaN or infinite values are dropped (`source-reported`).
2. **LSTM Input Features ($T = 60$ trading days) (`source-reported`):**
   - Window: Rolling 60 trading days ($T=60$), sequential dimension $M = 5$ (`source-reported`):
     1. Volume Ratio: Daily volume normalized by its 20-day simple moving average ($V_t / \text{SMA}_{20}(V)_t$) (`source-reported`).
     2. Daily Return: $r_t = (P_t - P_{t-1}) / P_{t-1}$ (`source-reported`).
     3. RSI: 14-day Relative Strength Index (`source-reported`).
     4. MACD Line: $\text{EMA}_{12}(P)_t - \text{EMA}_{26}(P)_t$ (`source-reported`).
     5. MACD Signal: 9-day EMA of the MACD Line (`source-reported`).
   - Input tensor shape: $\mathbf{X}_t \in \mathbb{R}^{60 \times 5}$ (`source-reported`).
3. **LSTM Feature Extractor Architecture (`source-reported`):**
   - Stacked 2-layer LSTM with hidden dimension $H = 64$ per layer (`source-reported`):
     $$\mathbf{h}_t^{(1)}, \mathbf{c}_t^{(1)} = \text{LSTM}_1(\mathbf{x}_t, \mathbf{h}_{t-1}^{(1)}, \mathbf{c}_{t-1}^{(1)})$$
     $$\mathbf{h}_t^{(2)}, \mathbf{c}_t^{(2)} = \text{LSTM}_2(\text{Dropout}_{0.5}(\mathbf{h}_t^{(1)}), \mathbf{h}_{t-1}^{(2)}, \mathbf{c}_{t-1}^{(2)})$$
   - Dropout: $p = 0.5$ between layer 1 and layer 2 (`source-reported`).
   - Initial states: $\mathbf{h}_0 = \mathbf{0}, \mathbf{c}_0 = \mathbf{0}$ (`source-reported`).
   - Pre-training Objective: Scaled cumulative return scalar prediction $\hat{y} = \mathbf{W}\mathbf{h}_T^{(2)} + \mathbf{b}$ minimized via MSE loss (`source-reported`):
     $$\mathcal{L}_{\text{LSTM}} = \frac{1}{N} \sum_{i=1}^N (\hat{y}_i - y_i)^2$$
   - Optimizer: Adam, initial learning rate $\eta = 5 \times 10^{-4}$, weight decay $10^{-4}$ (`source-reported`).
   - Learning Rate Scheduler: `ReduceLROnPlateau` halving learning rate (factor 0.5) if validation loss fails to improve for 8 consecutive epochs (`source-reported`).
   - Gradient norm clipping: 1.0 (`source-reported`).
   - Mini-batch size: 64 with shuffling (`source-reported`).
   - Training duration: Max 300 epochs with early stopping patience of 40 epochs on validation loss; best validation checkpoint restored (`source-reported`).
   - Feature Extraction: Once trained, the LSTM parameters are frozen; the 64-dimensional hidden vector at the final time step $\mathbf{h}_T \in \mathbb{R}^{64}$ is extracted as the temporal embedding for each observation (`source-reported`).
4. **Fourteen Hand-Crafted Technical Indicators ($\mathbf{f}_{\text{tech}} \in \mathbb{R}^{14}$) (`source-reported`):**
   - Trend / Moving Averages (all lagged by 1 trading day to prevent contemporaneous bar leakage):
     1. SMA 5-day (`source-reported`).
     2. SMA 10-day (`source-reported`).
     3. SMA 15-day (`source-reported`).
     4. SMA 30-day (`source-reported`).
     5. EMA 9-day (`source-reported`).
   - Momentum & Oscillators:
     6. RSI (14-day window) (`source-reported`).
     7. MACD line ($\text{EMA}_{12} - \text{EMA}_{26}$) (`source-reported`).
     8. MACD signal line (9-day EMA of MACD) (`source-reported`).
     9. MACD histogram ($\text{MACD} - \text{Signal}$) (`source-reported`).
   - Volatility:
     10. Rolling 20-day standard deviation of daily returns ($\sigma_{20}$) (`source-reported`).
   - Rate of Change:
     11. 10-day Rate of Change ($\text{ROC}_{10} = (P_t - P_{t-10}) / P_{t-10}$) (`source-reported`).
     12. 21-day Rate of Change ($\text{ROC}_{21} = (P_t - P_{t-21}) / P_{t-21}$) (`source-reported`).
   - Volume:
     13. 1-day Volume percentage change ($\Delta V_t / V_{t-1}$) (`source-reported`).
     14. 20-day Volume ratio ($V_t / \text{SMA}_{20}(V)_t$) (`source-reported`).
   - Normalization: Scaled to $[-1, 1]$ via MinMaxScaler fitted strictly on training data (`source-reported`).
5. **Hybrid Feature Vector Construction (`source-reported`):**
   - Concatenation of the 64-dimensional LSTM temporal embedding with the 14 scaled technical indicators (`source-reported`):
     $$\mathbf{z} = [\mathbf{h}_T \parallel \mathbf{f}_{\text{tech}}] \in \mathbb{R}^{78}$$
6. **XGBoost Regressor & Optimization (`source-reported`):**
   - Objective: `reg:squarederror` (`source-reported`).
   - Target: Cumulative forward return $R_t^{(d)} = \sum_{k=1}^d r_{t+k}$ for $d \in \{30, 90, 252, 365\}$ trading days (`source-reported`).
   - 3-Fold Cross-Validation Grid Search Hyperparameter Ranges (`source-reported`):
     - `n_estimators`: $\{100, 200, 300, 400\}$ (`source-reported`).
     - `learning_rate`: $\{0.001, 0.005, 0.01, 0.05\}$ (`source-reported`).
     - `max_depth`: $\{4, 6, 8, 10\}$ (`source-reported`).
     - `gamma`: $\{0.001, 0.005, 0.01, 0.02\}$ (`source-reported`).
   - Multi-Stock Pooling: All 14 equities are pooled into a single tabular dataset for training the horizon-specific XGBoost models (`source-reported`).

### Multi-Horizon Composite Scoring Rule

The primary source defines a composite decision score $S_i$ for equity $i$ across horizons (`source-reported`):
$$S = 20 \hat{R}^{(30)} + 30 \hat{R}^{(90)} + 50 \hat{R}^{(252)} + B_c - 100 \sigma_{20}$$

Where:
- $\hat{R}^{(30)}, \hat{R}^{(90)}, \hat{R}^{(252)}$ are the model-predicted cumulative returns for 30, 90, and 252 trading days (`source-reported`).
- $B_c$ is a sign-consistency bonus (`source-reported`):
  $$B_c = \begin{cases} +10 & \text{if } \text{sgn}(\hat{R}^{(30)}) = \text{sgn}(\hat{R}^{(90)}) = \text{sgn}(\hat{R}^{(252)}) = +1 \\ -10 & \text{if } \text{sgn}(\hat{R}^{(30)}) = \text{sgn}(\hat{R}^{(90)}) = \text{sgn}(\hat{R}^{(252)}) = -1 \\ 0 & \text{otherwise} \end{cases}$$
- $\sigma_{20}$ is the realized 20-day standard deviation of daily returns, weighted by $-100$ as an explicit risk/uncertainty penalty (`source-reported`).

### Categorical Ratings & Operational Decision Boundaries

- **Source-Reported Rating Categories (June 2016 Snapshot):**
  - `STRONG BUY`: Score $S > 15$ (GS: +20.22, MSFT: +20.19, BA: +17.94, JPM: +16.91, CAT: +16.89, WMT: +16.26) (`source-reported`).
  - `BUY`: $5 < S \le 15$ (AAPL: +12.92, XOM: +12.86, PFE: +6.75) (`source-reported`).
  - `HOLD`: $0 \le S \le 5$ (GOOGL: +4.26, CVX: +0.46, JNJ: +0.08) (`source-reported`).
  - `STRONG SELL`: $S < -15$ (NVDA: -15.23, AMZN: -16.35) (`source-reported`).
- **Research-Proposed Operational Trading Rules:**
  - *Note:* The primary source presents this as a return-forecasting and investment-scoring framework; it does not specify trade execution timestamps, order types, portfolio weights, or stop-loss rules (`source-reported gap`).
  - *Universe & Liquidity Filter (`research-proposed`):* Equities in universe must maintain trailing 30-day average daily volume (ADV) $> \$10\text{M}$ and minimum price $>\$5.00$.
  - *Rebalance Cadence (`research-proposed`):* Monthly rebalance executed at the market close on the last trading day of each calendar month.
  - *Portfolio Allocation (`research-proposed`):* Long top $K$ equities with $S > 15$ (`STRONG BUY`), Short bottom $K$ equities with $S < -15$ (`STRONG SELL`), with dollar-neutral weights scaled inversely to 20-day volatility ($w_i \propto 1 / \sigma_{20, i}$). If no assets meet the threshold, capital remains in cash.
  - *Execution Timing & Fill Model (`research-proposed`):* Market-on-Open (MOO) order execution on day $t+1$ following the monthly score generation at close of day $t$.
  - *Risk Cutoff (`research-proposed`):* Trailing stop loss per position triggered if adverse excursion exceeds $2.5 \times \sigma_{20}$ from entry price.

## Required data

- **Instruments & Universe:**
  - US equities: 14 large-cap equities (AAPL, NVDA, MSFT, GOOGL, JPM, GS, JNJ, PFE, XOM, CVX, AMZN, WMT, BA, CAT) (`source-reported`).
- **Venue & Market Type:**
  - US cash equity markets (NYSE, NASDAQ) (`source-reported`).
- **Timeframe & Session Structure:**
  - Daily OHLCV bars, regular US trading hours (09:30–16:00 ET) (`source-reported`).
- **Required Fields:**
  - Open, High, Low, Close, Volume (`source-reported`).
- **Point-in-Time & Availability:**
  - Technical indicators are computed using data strictly up to day $t-1$ for moving averages, and day $t$ close for momentum/volatility (`source-reported`).
  - Predictions are formed at the close of day $t$ for forward horizons $t+30, t+90, t+252, t+365$ (`source-reported`).
- **Missing Data Handling:**
  - Forward-fill imputation followed by dropping residual NaNs after indicator computation (`source-reported`).
- **Transaction Costs & Slippage Assumptions:**
  - Primary paper omits transaction fees, borrow costs, and slippage (`source-reported gap`).
  - `research-proposed` evaluation standard: 5 bps per share execution fee + 5 bps bid-ask half-spread/slippage ($10\text{ bps}$ round-trip) for US large caps.

## Execution assumptions

- **Signal-to-Order Latency:**
  - Signal computed at close of day $t$; order routed for execution at open of day $t+1$ (`research-proposed`).
- **Order Type & Fill Model:**
  - Market-on-Open (MOO) or VWAP over first 15 minutes of trading session (`research-proposed`).
- **Borrow & Shorting:**
  - Long/Short implementation assumes borrow availability at standard general collateral rates (50 bps annualized) for large-cap equities (`research-proposed`).
- **Capacity & Participation:**
  - Large-cap US equities easily absorb tens of millions in AUM at monthly rebalancing frequency (`research-proposed`).

## Evidence

### Source-reported

1. **Global Model Comparison on 30-Day Horizon (Table III / Table 8 in Source):**
   - Evaluated out-of-sample on the test partition across all 14 equities pooled (`source-reported`):
     - **LSTM-Only Baseline:**
       - Test RMSE: `0.2799` (`source-reported`).
       - Test MAE: `0.2600` (`source-reported`).
       - Test $R^2$: `-7.73` (`source-reported`).
       - Directional Accuracy: `40.1%` (`source-reported`).
     - **XGBoost-Only Baseline (14 Technical Indicators):**
       - Test RMSE: `0.0951` (`source-reported`).
       - Test MAE: `0.0739` (`source-reported`).
       - Test $R^2$: `-0.008` (`source-reported`).
       - Directional Accuracy: `59.2%` (`source-reported`).
     - **Proposed Hybrid (LSTM Embedding + XGBoost):**
       - Test RMSE: `0.0949` (`source-reported`).
       - Test MAE: `0.0743` (`source-reported`).
       - Test $R^2$: `-0.003` (`source-reported`).
       - Directional Accuracy: `58.5%` (`source-reported`).
2. **Per-Stock Performance on 30-Day Horizon (Table IV / Table 9 in Source):**
   - Out-of-sample RMSE and Directional Accuracy (%) per stock (`source-reported`):
     - `AAPL`: LSTM RMSE 0.2198 (54.6%), XGBoost RMSE 0.1010 (45.4%), Hybrid RMSE 0.1014 (45.4%).
     - `NVDA`: LSTM RMSE 0.3494 (13.9%), XGBoost RMSE 0.1628 (83.2%), Hybrid RMSE **0.1603** (**84.5%**).
     - `MSFT`: LSTM RMSE 0.3063 (41.6%), XGBoost RMSE 0.0822 (58.4%), Hybrid RMSE **0.0810** (58.4%).
     - `GOOGL`: LSTM RMSE 0.2844 (47.5%), XGBoost RMSE 0.0781 (52.5%), Hybrid RMSE 0.0788 (**52.9%**).
     - `JPM`: LSTM RMSE 0.2339 (43.3%), XGBoost RMSE 0.0787 (56.7%), Hybrid RMSE **0.0781** (56.7%).
     - `GS`: LSTM RMSE 0.1982 (61.3%), XGBoost RMSE 0.0990 (38.7%), Hybrid RMSE 0.0994 (38.7%).
     - `JNJ`: LSTM RMSE 0.2917 (24.4%), XGBoost RMSE 0.0469 (75.6%), Hybrid RMSE 0.0522 (60.1%).
     - `PFE`: LSTM RMSE 0.2620 (45.0%), XGBoost RMSE 0.0660 (55.0%), Hybrid RMSE 0.0680 (52.9%).
     - `XOM`: LSTM RMSE 0.2719 (33.2%), XGBoost RMSE 0.0683 (66.8%), Hybrid RMSE 0.0684 (66.8%).
     - `CVX`: LSTM RMSE 0.3262 (35.4%), XGBoost RMSE 0.1016 (64.6%), Hybrid RMSE **0.1011** (64.6%).
     - `AMZN`: LSTM RMSE 0.3838 (25.6%), XGBoost RMSE 0.1270 (67.6%), Hybrid RMSE **0.1246** (**74.4%**).
     - `WMT`: LSTM RMSE 0.2531 (32.4%), XGBoost RMSE 0.0714 (67.6%), Hybrid RMSE **0.0705** (67.6%).
     - `BA`: LSTM RMSE 0.2359 (47.1%), XGBoost RMSE 0.0931 (52.9%), Hybrid RMSE 0.0942 (52.9%).
     - `CAT`: LSTM RMSE 0.2386 (56.3%), XGBoost RMSE 0.0985 (43.7%), Hybrid RMSE 0.0987 (43.7%).
   - Summary: Hybrid achieves lowest RMSE on 7 of 14 equities (NVDA, MSFT, JPM, CVX, AMZN, WMT, tie on XOM) (`source-reported`).
3. **Multi-Horizon Performance of Hybrid Model (Table V / Table 10 in Source):**
   - 30-day: RMSE `0.0949`, MAE `0.0764`, $R^2$ `-0.041`, Dir. Acc. `57.0%` (`source-reported`).
   - 90-day: RMSE `0.1510`, MAE `0.1108`, $R^2$ `-0.107`, Dir. Acc. `64.4%` (`source-reported`).
   - 252-day: RMSE `0.3258`, MAE `0.2106`, $R^2$ `-0.208`, Dir. Acc. `84.9%` (`source-reported`).
   - 365-day: RMSE `0.4331`, MAE `0.2600`, $R^2$ `-0.214`, Dir. Acc. `97.6%` (`source-reported`).
4. **Falsification of Directional Accuracy vs. Naive Always-Positive Base Rate (Table VII / Table 12 in Source):**
   - 30-day: Hybrid Dir. Acc. `57.0%` vs. Naive Base Rate `59.9%` $\to$ Gap `-2.9 pp` (`source-reported`).
   - 90-day: Hybrid Dir. Acc. `64.4%` vs. Naive Base Rate `72.4%` $\to$ Gap `-8.0 pp` (`source-reported`).
   - 252-day: Hybrid Dir. Acc. `84.9%` vs. Naive Base Rate `91.2%` $\to$ Gap `-6.3 pp` (`source-reported`).
   - 365-day: Hybrid Dir. Acc. `97.6%` vs. Naive Base Rate `97.8%` $\to$ Gap `-0.2 pp` (`source-reported`).
5. **Investment Scores & Ratings at Test End (June 2016 Snapshot, Table VI / Table 11 in Source):**
   - GS: Score `+20.22`, Financials, `STRONG BUY` (`source-reported`).
   - MSFT: Score `+20.19`, Technology, `STRONG BUY` (`source-reported`).
   - BA: Score `+17.94`, Industrials, `STRONG BUY` (`source-reported`).
   - JPM: Score `+16.91`, Financials, `STRONG BUY` (`source-reported`).
   - CAT: Score `+16.89`, Industrials, `STRONG BUY` (`source-reported`).
   - WMT: Score `+16.26`, Consumer, `STRONG BUY` (`source-reported`).
   - AAPL: Score `+12.92`, Technology, `BUY` (`source-reported`).
   - XOM: Score `+12.86`, Energy, `BUY` (`source-reported`).
   - PFE: Score `+6.75`, Healthcare, `BUY` (`source-reported`).
   - GOOGL: Score `+4.26`, Technology, `HOLD` (`source-reported`).
   - CVX: Score `+0.46`, Energy, `HOLD` (`source-reported`).
   - JNJ: Score `+0.08`, Healthcare, `HOLD` (`source-reported`).
   - NVDA: Score `-15.23`, Technology, `STRONG SELL` (`source-reported`).
   - AMZN: Score `-16.35`, Consumer, `STRONG SELL` (`source-reported`).

### Independently reproduced

- Not independently reproduced.

### Negative evidence

1. **Catastrophic Failure of Standalone LSTM:**
   - Standalone LSTM achieves an $R^2$ of `-7.73` and a directional accuracy of only `40.1%` (below random chance), proving that attempting to directly predict multi-week return magnitudes from sequential OHLCV and indicator streams without tree-based ensembling or tabular feature scaffolding is wholly unviable (`source-reported`).
2. **Persistence of Negative Out-of-Sample $R^2$ Across All Horizons:**
   - Both standalone XGBoost ($R^2 = -0.008$) and the proposed Hybrid ($R^2 = -0.003$ to $-0.214$) produce negative $R^2$ values across all horizons, proving that neither model outperforms the unconditional historical mean for predicting raw return magnitude (`source-reported`).
3. **Directional Accuracy Underperformance Relative to Trivial Drift:**
   - When benchmarked against an unconditional naive predictor that always bets positive, the Hybrid underperforms across all four horizons by between `-0.2 pp` and `-8.0 pp` (`source-reported`). The high raw directional accuracy at 252d (84.9%) and 365d (97.6%) is an illusion created by bull market sample drift (`source-reported`).
4. **Structural Shift Vulnerability (The 2016 NVDA/AMZN Failure):**
   - At the conclusion of the evaluation period (June 2016), the framework assigned its most aggressive bearish rating (`STRONG SELL`) to NVDA (Score `-15.23`) and AMZN (Score `-16.35`) due to recent trailing volatility and negative medium-term return predictions (`source-reported`).
   - In subsequent market history (2016–2021), NVDA and AMZN experienced unprecedented secular growth driven by data center, deep learning, and cloud infrastructure adoption. A model relying purely on backward-looking technical indicators and short lookbacks will short high-convexity structural winners during early breakout phases.
5. **Marginality of Global Improvement:**
   - The global RMSE improvement of the Hybrid model over standalone XGBoost is only `0.0002` (0.0949 vs 0.0951), winning on exactly 7 of 14 equities (`source-reported`). Without per-sector conditioning, the global alpha contribution of the LSTM embedding is marginal.

## Falsification plan

1. **Modern Out-of-Sample Extension (2016–2026 Walk-Forward Audit):**
   - *Test:* Re-train the exact hybrid architecture using chronological walk-forward windows on S&P 500 equities through 2026.
   - *Metric:* Cross-sectional Spearman Rank Information Coefficient (Rank IC) of the composite score $S_t$ against realized 30-day and 90-day returns.
   - *Research-Defined Falsification Threshold:* Falsified if mean Rank IC $< 0.02$ or if the t-statistic of Rank IC is $< 2.0$.
   - *Action:* Reject the composite scoring formula if Rank IC is indistinguishable from zero.
2. **Ablation of LSTM Embeddings vs. Standalone XGBoost:**
   - *Test:* Compare the risk-adjusted performance of a long-short portfolio driven by the Hybrid model against one driven strictly by XGBoost-Only with the 14 technical indicators.
   - *Metric:* Out-of-sample annualized Sharpe ratio difference ($\Delta \text{Sharpe} = \text{Sharpe}_{\text{Hybrid}} - \text{Sharpe}_{\text{XGBoost}}$) net of $10\text{ bps}$ round-trip transaction costs.
   - *Research-Defined Falsification Threshold:* Falsified if $\Delta \text{Sharpe} \le 0.15$ or if a Wilcoxon signed-rank test on per-asset monthly PnL yields $p > 0.05$.
   - *Action:* If falsified, discard the LSTM pre-training stage and retain only the simpler, faster tabular gradient-boosting baseline.
3. **Temporal Sequence Shuffling Placebo Control:**
   - *Test:* Randomly permute the chronological order of the 60-day lookback window fed into the LSTM while preserving the marginal distribution of features.
   - *Research-Defined Falsification Threshold:* Falsified if the shuffled-window embedding achieves test RMSE within $1\%$ of the unshuffled sequential embedding.
   - *Action:* If true, this proves the LSTM is not learning sequential memory dynamics, but merely acting as a noisy non-linear pooling operator.
4. **Transaction Cost and Rebalancing Sensitivity:**
   - *Test:* Simulate a monthly dollar-neutral top-quintile long / bottom-quintile short portfolio across varying fee/slippage levels ($0, 5, 10, 20\text{ bps}$ per trade).
   - *Research-Defined Falsification Threshold:* Falsified if net annualized return drops below $0\%$ at round-trip costs of $10\text{ bps}$.

## Crypto portability

- **Portability Classification:** `adapted / unproven`.
- **Porting Rationale & Adaptations:**
  - The core architecture (stacked-LSTM sequence encoder + tabular gradient-boosted regressor) can be ported to cryptocurrency liquid perpetual contracts (e.g., BTC, ETH, SOL, and top 20 altcoins).
  - *Data Modality Adaptations:*
    - Re-calibrate lookback window $T$: In 24/7 crypto markets, 60 daily bars represent two full calendar months; an 8-hour or 4-hour bar interval ($T = 60 \times 4\text{h} = 10\text{ days}$) is more appropriate to capture rapid regime cycles.
    - Mandatory Feature Expansion: Raw volume and moving averages must be augmented with perpetual funding rates, spot-perpetual basis, open interest percentage changes, and liquidation flow volume.
- **Crypto-Specific Risks & Frictions:**
  - *Extreme Tail Volatility & Shorting Costs:* The composite score relies on trailing volatility penalties ($-100 \sigma_{20}$). In crypto, sudden $40\%$ flash crashes or short squeezes would cause extreme score instability.
  - *Funding Drag:* Holding multi-month positions (90d, 252d) in crypto perpetuals entails substantial cumulative funding payments that can easily exceed predicted returns.
  - *Survivorship & Regime Shifts:* The crypto altcoin universe experiences rapid token turnover and severe structural breaks that invalidate static pooled training models.

## Limitations

1. **Underspecified Execution & Sizing in Primary Source:**
   - The paper provides return predictions and a composite scoring metric, but specifies no formal portfolio allocation rules, position sizing, rebalancing calendar, or execution timestamps (`underspecified`).
2. **Absence of Transaction Cost Modeling:**
   - Zero transaction costs, commissions, borrow fees, or slippage are accounted for in the primary source (`data gap`).
3. **Historical Sample Truncation:**
   - The primary empirical dataset ends in mid-2016, omitting a decade of subsequent market structure evolution (e.g., algorithmic execution growth, retail option flows, zero-commission trading, COVID-19 shock, 2022 inflation cycle) (`data gap`).
4. **Severe Autocorrelation in Overlapping Cumulative Targets:**
   - Evaluating 252-day and 365-day cumulative returns on daily rolling data introduces massive serial correlation across consecutive samples. This artificially compresses standard error estimates unless Newey-West or Hansen-Hodrick corrections are explicitly applied (`methodological limitation`).
5. **Base-Rate Inflation of Classification Metrics:**
   - Directional accuracy figures exceeding 80% on long horizons are largely driven by positive market drift rather than genuine predictive alpha (`provenance caveat`).

## Implementation status

- Frontmatter: `implementation_status: not-implemented`.
- No prototype, backtest, or live trading script for this strategy currently exists in our research repository or execution engines.
- Research capture only; does not authorize implementation in PyBroker, NautilusTrader, paper trading, testnet, or live trading.

## Adoption boundary

- Frontmatter: `status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.
- This record represents an audited research capture of an external academic publication.
- A record being present in this repository does not indicate that the strategy is profitable, validated, or approved for paper, testnet, or live capital deployment.

## Related Wiki records

- `[[equity-cross-regime-bayesian-optimisation-xgboost-tabnet-hybrid-2026-09-02]]`
- `[[crypto-perps-cross-sectional-probit-ridge-xgboost-macd-sellback-2026-09-16]]`
- `[[hybrid-xgboost-finbert-regime-adaptive-equity-2026-09-04]]`
- `[[vertifusex-penultimate-temporal-fusion-triple-barrier-cooldown-2026-09-16]]`
- `[[wavefuse-wavelet-denoised-cwwt-vertical-attention-fusion-2026-09-16]]`

## Sources

- Seif ElDein Mostafa, Yahia Ahmed, Farah Darwish, and Marwa Solayman, "A Hybrid LSTM–XGBoost Framework for Multi-Horizon Stock Return Prediction Across Diversified Equity Portfolios", arXiv preprint `arXiv:2609.13125v1 [cs.LG]`, submitted September 11, 2026. https://arxiv.org/abs/2609.13125
- Full-Text HTML: https://arxiv.org/html/2609.13125v1
- Boris Marjanovic, "Price-Volume Data for All US Stocks and ETFs", Kaggle dataset, 2017. https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs
- Thomas Fischer and Christopher Krauss, "Deep learning with long short-term memory networks for financial market predictions", *European Journal of Operational Research*, Vol. 270, No. 2 (2018), pp. 654–669. DOI: 10.1016/j.ejor.2017.11.027
- Tianqi Chen and Carlos Guestrin, "XGBoost: A Scalable Tree Boosting System", in *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining* (2016), pp. 785–794. DOI: 10.1145/2939672.2939785
- Christopher Krauss, Xuan Anh Do, and Nicolas Huck, "Deep neural networks, gradient-boosted trees, random forests: Statistical arbitrage on the S&P 500", *European Journal of Operational Research*, Vol. 259, No. 2 (2017), pp. 689–702. DOI: 10.1016/j.ejor.2016.10.031
