---
schema: strategy-research-record-v1
title: "Cross-Sectional Probit-Gaussianized Ridge and XGBoost Walk-Forward Ensemble with Market-Neutral MACD Bandpass Filter on Crypto Perpetuals (Sijelmassi 2026)"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - cross-sectional-momentum
  - machine-learning
  - ridge-regression
  - xgboost
  - walk-forward-cross-validation
  - probit-transform
  - macd-bandpass
  - turnover-drag
status: research-only
confidence: medium
source_as_of: 2026-07-03
sources:
  - "Sijelmassi Iliass, 'Crypto perps alpha - Cross-sectional ML on hourly cryptocurrency perpetual futures', GitHub repository, commit 9faca06b944d333b8169158ed0ef8cdbe8707662, July 3, 2026. https://github.com/IliassSjm/crypto-perps-alpha"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Sectional Probit-Gaussianized Ridge and XGBoost Walk-Forward Ensemble with Market-Neutral MACD Bandpass Filter on Crypto Perpetuals (Sijelmassi 2026)

## Provenance

- **Primary Source Repository:**
  - Repository URL: https://github.com/IliassSjm/crypto-perps-alpha
  - Full Immutable Commit SHA: `9faca06b944d333b8169158ed0ef8cdbe8707662`
  - Commit Date: 2026-07-03 01:51:36 UTC
  - Author: Sijelmassi Iliass (`IliassSjm`), HEC Paris
  - Project Title: *Crypto perps alpha: Cross-sectional ML on hourly cryptocurrency perpetual futures*
  - Institutional / Academic Context: Developed as the 1st-place course capstone project (out of 13 teams on held-out out-of-sample Sharpe) for *Predicting Financial Markets with Machine Learning* (HEC Paris, Spring 2026).
- **Inspected Primary Source Code Paths:**
  - `README.md` (empirical validation results, cost sensitivity table, architecture overview)
  - `src/alpha_config.py` (hyperparameters, dates, walk-forward windows, feature definitions)
  - `src/alpha_utils.py` (label construction, feature normalization, IC filtering, correlation deduplication, walk-forward CV, evaluation metrics)
  - `src/step1_features.py` (feature generation, Spearman IC filtering, correlation pruning, conditioner-feature interactions)
  - `src/step2_polymodel.py` (polynomial regression baseline)
  - `src/step3_ridge.py` (Ridge walk-forward cross-validation)
  - `src/step4_xgboost.py` (PCA-augmented XGBoost walk-forward cross-validation)
  - `src/step5_evaluate.py` (z-score ensembling, MACD sellback bandpass, master orthogonal blend, PnL analytics)
  - `oi_divergence_alpha.py` (standalone open interest vs. price divergence study)
  - `tests/test_pipeline.py` (pure unit tests for normalization, IC calculation, correlation deduplication, and dollar neutrality)
  - `notebooks/alpha_strategy.ipynb` (interactive end-to-end walk-forward notebook)
- **Direct Primary-Source Verification:**
  - All mathematical definitions, training parameters, lag-specific Sharpe metrics, and cost-sensitivity thresholds were retrieved directly from the repository source code and documentation at commit `9faca06b944d333b8169158ed0ef8cdbe8707662`.
  - No search engine snippets, secondary blog summaries, or model hallucinations were used to derive signal rules or empirical statistics.
- **Repository Deduplication Audit:**
  - Audited all existing markdown records in `alpha-strategy-research`. Zero prior records cite `IliassSjm/crypto-perps-alpha`, Sijelmassi Iliass, or HEC Paris quantitative coursework.
  - Related cross-sectional perpetual records (`crypto-cross-sectional-lead-lag-rotation-hyperliquid-perps-2026-09-13.md`, `crypto-cross-sectional-meme-momentum-funding-dynamic-rotation-2026-09-14.md`, `apff-multi-asset-perpetual-adaptive-factor-factory-2026-09-16.md`) investigate lead-lag cross-correlation, dynamic meme momentum, or rule-based factor weighting. None implement the probit-Gaussianized rank label, heavy L2 regularized Ridge combined with PCA-augmented XGBoost, and the market-neutral MACD(2,6) bandpass sellback filter formulated here.

## Economic mechanism

### Source-reported

1. **Probit-Gaussianized Rank Labeling for Tail Alpha:**
   - Standard Mean Squared Error (MSE) loss functions in supervised regression allocate gradient updates proportional to squared deviations across the entire cross-sectional distribution, wasting modeling capacity on central noisy observations.
   - By calculating a smoothed 2-hour forward return divided by 24-hour rolling volatility, ranking it cross-sectionally to $[0.001, 0.999]$, and applying the inverse Gaussian CDF ($\text{probit} = \Phi^{-1}(\text{rank})$), the distribution tails are stretched to approximately $\pm 3.0$.
   - This mathematical transformation forces MSE learners (Ridge and XGBoost) to prioritize gradient descent on the extreme relative outperformers and underperformers where long/short dollar-neutral alpha is concentrated.
2. **Collinearity Management via Ridge vs. PCA-XGBoost:**
   - High-dimensional cross-sectional features (316 selected features including 300 conditioner interactions) suffer from extreme multicollinearity.
   - Ridge regression applies an aggressive $L_2$ regularization penalty ($\alpha = 10,000.0$) directly on standardized features without dimension reduction, shrinking redundant coefficients uniformly.
   - XGBoost augments the standardized feature space with 20 principal components derived dynamically within each rolling training fold, allowing gradient-boosted decision trees to split on orthogonal market-wide variance drivers alongside localized idiosyncratic features.
3. **Market-Neutral MACD(2,6) Bandpass Sellback Filter:**
   - Raw machine-learning predictions exhibit short-term momentum over lags 0–2h but suffer severe decay that reverses into negative Sharpe by lag 6, signaling a mean-reverting microstructure cycle rather than simple overfitting.
   - An exponential moving average (EMA) difference filter ($\text{EMA}_2(\text{pred}) - \text{EMA}_6(\text{pred})$) acts as a bandpass filter that isolates the ~6-hour cyclical reversal while eliminating slower persistent trend drifts.
   - Hourly cross-sectional de-meaning strictly eliminates market beta drift, guaranteeing hourly dollar neutrality.
4. **Microstructure Decay and Transaction Cost Reality:**
   - The edge operates at high gross turnover (~0.35 of gross book per hour).
   - Zero-fee gross Sharpe reaches 9.75 at lag 0, but break-even execution cost is approximately 1.2 basis points (bps) per side. Realistic taker fees (4–5 bps on major crypto exchanges) overwhelm the signal, indicating that the raw signal represents a fast-decaying microstructure phenomenon requiring passive maker execution or turnover dampening rather than aggressive market orders.

### Research interpretation

- **Microstructure Inventory and Liquidity Imbalance:**
  - The rapid decay from lag 0 (Sharpe 9.75) to lag 1 (Sharpe 3.29) and lag 2 (Sharpe 1.67) indicates that the signal exploits transient order book liquidity voids and aggressive flow imbalances rather than multi-day fundamental drift.
  - The probit rank label effectively trains the models to predict which altcoins are experiencing temporary liquidity exhaustion relative to the broader universe.
- **Bandpass Filtering as Dynamic Mean-Reversion Timing:**
  - The MACD(2,6) filter effectively measures the acceleration or deceleration of model conviction. When the fast prediction EMA($\text{span}=2$) begins to drop below the slow EMA($\text{span}=6$), the strategy begins unwinding or reversing positions before the empirical mean-reversion crash occurs at lag 6.
- **Economic Viability Constraints:**
  - A turnover of 35% per hour equates to a complete portfolio turnover every ~2.8 hours. At this velocity, taker-based execution is provably unprofitable. The alpha is economically viable only under passive quoting (post-only maker orders capturing negative/zero maker fees) or within an institutional execution engine utilizing internal crossing and turnover-netting no-trade bands.

## Signal

### Signal Formation and Timeline
- **Observation Frequency:** Hourly bar close ($t$) (`source-reported`).
- **Data Availability Lag:** Features use closed historical hourly bars up to $t$; predictions formed immediately at close ($t$) (`source-reported`).
- **Execution Horizons Evaluated:** Lags $0, 1, 2, 3, 6, 12$ hours (`source-reported`).
- **Rebalance Cadence:** Hourly rebalance of continuous dollar-neutral portfolio weights (`source-reported`).

### Label Construction
1. **Raw Forward Return Smoothing:**
   $$\tilde{r}_{t \to t+2} = r_{t \to t+1} + r_{t+1 \to t+2}$$
   where $r_{t \to t+1} = \text{shift}(-1)$ and $r_{t+1 \to t+2} = \text{shift}(-2)$ (`source-reported`).
2. **Rolling Volatility Normalization:**
   $$\sigma_{i, t} = \text{rolling\_std}_{24}(r_{i, \tau}, \text{min\_periods}=6)$$
   $$y_{\text{vol\_adj}, i, t} = \frac{\tilde{r}_{t \to t+2, i}}{\sigma_{i, t}}$$
   Zero standard deviations are replaced with NaN (`source-reported`).
3. **Cross-Sectional Rank Transform:**
   $$\text{rank}_{i, t} = \text{rank}_{\text{pct}}(y_{\text{vol\_adj}, \cdot, t}).\text{clip}(0.001, 0.999)$$
   Clipping prevents asymptotic infinite values in the inverse normal CDF (`source-reported`).
4. **Probit Gaussianization:**
   $$y_{i, t} = \Phi^{-1}(\text{rank}_{i, t})$$
   where $\Phi^{-1}$ is the standard normal probit quantile function (`scipy.stats.norm.ppf`) (`source-reported`). Missing values are filled with 0.0 (`source-reported`).

### Feature Engineering & Filtering (Step 1)
- **Raw Input Fields (6):** `return`, `close`, `nb_trades`, `volume_usd`, `funding_rate`, `open_interest_value` (`source-reported`).
- **Transformation Styles (13):**
  - `level`: raw series
  - `delta_1`, `delta_2`, `delta_3`: percentage changes over 1, 2, 3 hours
  - `shift_1`, `shift_2`, `shift_3`: lagged values
  - `mean_3`, `mean_6`, `mean_24`: rolling means
  - `std_3`, `std_6`, `std_24`: rolling standard deviations
  - Evaluated on raw fields producing 78 simple features (`source-reported`).
- **External Feature & Conditioner Panels:**
  - 266 pre-calculated external feature CSV panels (`feature_*.csv`) (`source-reported`).
  - 35 external market regime conditioner panels (`conditioner_*.csv`) (`source-reported`).
- **Feature Normalization:**
  $$\hat{f}_{i, t} = \text{rank}_{\text{pct}}(f_{\cdot, t}) - 0.5$$
  centered in $[-0.5, 0.5]$ (`source-reported`).
- **Information Coefficient (IC) Filter:**
  - Univariate Spearman rank correlation between normalized feature and training label $y_{\text{train}}$ (`source-reported`).
  - Minimum sample size: 100 valid paired observations (`source-reported`).
  - Inclusion threshold: $|\text{IC}| > 0.001$ (`source-reported`).
- **Correlation Deduplication (Training Set Only):**
  - Evaluated on a random sample of 100,000 timestamps from the training period (`RandomState(42)`) (`source-reported`).
  - Pairwise Spearman correlation matrix computed (`source-reported`).
  - Pruning threshold: $|\rho| > 0.95$. When two features exceed 0.95 correlation, the feature with lower $|\text{IC}|$ is discarded (`source-reported`).
- **Conditioner $\times$ Feature Interactions:**
  - Top 30 base features by $|\text{IC}|$ and top 10 regime conditioners by $|\text{IC}|$ are selected (`source-reported`).
  - 300 interaction terms constructed with sign-flip protection:
    $$\text{interact}_{j, k} = \hat{f}_{j} \times (\hat{c}_{k} + 0.5)$$
    Shifting the conditioner by $+0.5$ places it in $[0, 1]$, modulating feature magnitude without inverting sign (`source-reported`).
  - Total selected feature matrix: 316 features (`source-reported`).

### Model Architectures & Walk-Forward Protocol
- **Walk-Forward Cross-Validation Split:**
  - Rolling 12-month training window (`TRAIN_MONTHS = 12`) (`source-reported`).
  - Rolling 1-month out-of-sample prediction window (`PREDICT_MONTHS = 1`), stepped monthly (`source-reported`).
  - In-sample training range: `2023-01-24` to `2024-01-24` (`source-reported`).
  - Out-of-sample validation range: `2024-01-25` to `2024-07-24` (`source-reported`).
  - Pure hold-out test range: `2024-07-25` to `2025-01-24` (`source-reported`).
- **Model 1: Ridge Regression (`src/step3_ridge.py`):**
  - Features standardized using `StandardScaler` fit strictly on the training fold (`source-reported`).
  - Ridge regression with $L_2$ penalty $\alpha = 10,000.0$ (`source-reported`).
  - No PCA applied to Ridge; heavy $L_2$ handles feature collinearity (`source-reported`).
- **Model 2: PCA-Augmented XGBoost (`src/step4_xgboost.py`):**
  - Dynamic PCA fit on training fold: $n_{\text{components}} = \min(20, N_{\text{features}}, N_{\text{samples}})$ (`source-reported`).
  - 20 principal components appended to the standardized feature matrix: $X_{\text{augmented}} = [X, X_{\text{PCA}}]$ (`source-reported`).
  - Hyperparameters:
    - `n_estimators`: 1000 (`source-reported`)
    - `learning_rate`: 0.02 (`source-reported`)
    - `max_depth`: 4 (`source-reported`)
    - `min_child_weight`: 20 (`source-reported`)
    - `subsample`: 0.05 (`source-reported`)
    - `colsample_bytree`: 0.3 (`source-reported`)
    - `tree_method`: `"hist"` (`source-reported`)
- **Model 3: Polynomial Regression Baseline (`src/step2_polymodel.py`):**
  - Degrees 1, 2, 3, 4 tested on top 30 features (`source-reported`).
  - Showed negative out-of-sample contribution; ensemble weight set to 0.0 (`source-reported`).

### Signal Combination & Post-Processing (`src/step5_evaluate.py`)
1. **Cross-Sectional Z-Scoring:**
   $$Z(S)_{i, t} = \frac{S_{i, t} - \mu_{t}(S)}{\sigma_{t}(S)}$$
   Missing standard deviations replaced with 0.0 (`source-reported`).
2. **Base Ensemble:**
   $$S_{\text{ens}} = 0.40 \times Z(\hat{y}_{\text{Ridge}}) + 0.60 \times Z(\hat{y}_{\text{XGB}})$$
   (`source-reported`).
3. **MACD(2,6) Sellback Bandpass Filter:**
   $$\text{fast}_t = \text{EMA}(S_{\text{ens}}, \text{span}=2)$$
   $$\text{slow}_t = \text{EMA}(S_{\text{ens}}, \text{span}=6)$$
   $$\text{macd}_t = \text{fast}_t - \text{slow}_t$$
   $$S_{\text{sellback}, i, t} = \text{macd}_{i, t} - \frac{1}{N_t} \sum_{j=1}^{N_t} \text{macd}_{j, t}$$
   Strict hourly de-meaning enforces dollar-neutrality (`source-reported`).
4. **Master Orthogonal Blend:**
   - Combines Value (ML ensemble), Momentum/Deceleration (MACD sellback), and Micro-Reversal (lag-1 return fade):
     $$S_{\text{rev}, i, t} = Z(-r_{i, t})$$
     $$S_{\text{master}} = 0.30 \times Z(S_{\text{ens}}) + 0.50 \times Z(S_{\text{sellback}}) + 0.20 \times S_{\text{rev}}$$
   (`source-reported`).

### Portfolio Weight Allocation
- Continuous rank-based dollar-neutral positioning:
  $$P_{i, t} = \text{rank}_{\text{cs}}(S_{i, t})$$
  $$P_{\text{norm}, i, t} = \frac{P_{i, t}}{\sum_{j} |P_{j, t}|}$$
  $$w_{i, t} = P_{\text{norm}, i, t} - \frac{1}{N_t} \sum_{j} P_{\text{norm}, j, t}$$
  Gross leverage $\sum |w_{i, t}| = 1.0$; net exposure $\sum w_{i, t} = 0.0$ (`source-reported`).

## Required data

- **Asset Universe:** Cross-section of cryptocurrency perpetual futures listed across major centralized venues (411 unique perpetual symbols cumulatively, ~212 active instruments per hourly bar) (`source-reported`).
- **Data Timeframe:** Hourly bar intervals (`1h`) (`source-reported`).
- **Required OHLCV & Microstructure Fields:**
  - `close`: hourly close price (`source-reported`)
  - `return`: hourly log/percentage close-to-close return (`source-reported`)
  - `nb_trades`: hourly trade count (`source-reported`)
  - `volume_usd`: hourly quoted dollar volume (`source-reported`)
  - `funding_rate`: 8-hour periodic funding rate recorded hourly (`source-reported`)
  - `open_interest_value`: aggregate open interest in USD (`source-reported`)
- **Point-in-Time Discipline:**
  - Feature transforms use only past closed bars up to timestamp $t$ (`source-reported`).
  - Feature selection (IC filter and correlation pruning) fit once on training data (`2023-01-24` to `2024-01-24`) and frozen (`source-reported`).
  - PCA and model fits updated monthly using only preceding 12-month rolling windows (`source-reported`).
- **Missing Data Handling:**
  - Standard deviations $\le 0$ replaced with NaN (`source-reported`).
  - Unaligned series reindexed against master return index and filled with 0.0 (`source-reported`).

## Execution assumptions

- **Signal-to-Execution Delay:**
  - Tested across execution lags $0, 1, 2, 3, 6, 12$ hours (`source-reported`).
  - Lag 0 assumes execution at the close of bar $t$ ($PnL_t = w_{t-1} \cdot r_t$) (`source-reported`).
  - Lag $k$ applies positions shifted by $1 + k$ bars (`source-reported`).
- **Transaction Costs & Slippage:**
  - Cost model: $\text{Fee}_t = \text{TC} \times \sum_i |\Delta w_{i, t}|$ (`source-reported`).
  - Evaluated at $\text{TC} = 0.0000$ (0 bps), $\text{TC} = 0.0001$ (1 bp per side), and $\text{TC} = 0.0002$ (2 bps per side) (`source-reported`).
  - Slippage and market impact: Omitted in primary backtest (`source-reported`).
- **Execution Fill Model:**
  - Infinite liquidity at hourly close mid-price (`source-reported`).
- **Borrow & Leverage:**
  - Long/short continuous weights; short positions assumed frictionless via perpetual contracts (`source-reported`).
  - Gross book normalized to 1.0 ($1\times$ leverage) (`source-reported`).
- **Research-Proposed Operational Parameters (`research-proposed`):**
  - Execution order type: Passive post-only limit orders placed at bid/ask with 10-second cancel/replace cadence (`research-proposed`).
  - Venue: Binance USDT-margined perpetuals or OKX USDT perpetuals (`research-proposed`).
  - Fee assumption: VIP3+ tier with maker fee $\le 0.00\%$ and taker fee $\le 0.02\%$ (`research-proposed`).
  - No-trade band: Position rebalancing threshold $\Delta w_{i} < 0.002$ suppressed to reduce turnover from 0.35 to $<0.10$ per hour (`research-proposed`).

## Evidence

### Source-reported

- **Out-of-Sample Validation Period Performance (`2024-01-25` to `2024-07-24`):**
  - Hourly annualization factor: $\sqrt{24 \times 365} \approx 93.59$.
  - Annual risk-free rate assumption: 5.0% ($r_{\text{hourly}} = (1 + 0.05)^{1/(24 \times 365)} - 1$).
  - Annualized Sharpe Ratio across Execution Lags (zero transaction costs):

| Signal Configuration | Lag 0 | Lag 1 | Lag 2 | Lag 3 | Lag 6 | Lag 12 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Ridge only** | 8.76 | 0.82 | −0.74 | −2.28 | −3.29 | −2.77 |
| **XGBoost only** | 5.20 | 0.83 | −0.15 | −1.69 | −3.04 | −2.22 |
| **Ensemble (40% Ridge / 60% XGBoost)** | 6.90 | 0.67 | −0.34 | −1.89 | −3.51 | −2.33 |
| **Ensemble + MACD(2,6) Sellback** | 9.75 | 3.29 | 1.67 | 1.92 | −1.18 | −1.35 |
| **Master Orthogonal Blend** | 6.80 | 2.07 | 0.39 | 0.89 | −2.00 | −1.31 |

- **Cost Sensitivity of MACD Sellback Signal:**
  - At $\text{TC} = 0.0$ bps: Sharpe = 9.75 (`source-reported`).
  - At $\text{TC} = 1.0$ bp per side: Sharpe collapses to 1.44 (`source-reported`).
  - At $\text{TC} = 2.0$ bps per side: Sharpe drops below 0.0 (negative net return) (`source-reported`).
- **Turnover and Break-Even Economics:**
  - Gross hourly turnover: ~0.35 of total gross book per hour (`source-reported`).
  - Break-even cost threshold: ~1.2 bps per side (`source-reported`).
- **Competition Outcome:**
  - Ranked 1st of 13 teams on held-out test period (`2024-07-25` to `2025-01-24`) in HEC Paris quantitative ML tournament (`source-reported`).
- **Standalone Open Interest Divergence Alpha (`oi_divergence_alpha.py`):**
  - Formulation: $\alpha_{\text{OI}} = -(\Delta\text{OI}_{\%} - r_t)$ (`source-reported`).
  - Fades aggressive participant positioning (OI rising while price falls indicates short build-up; OI rising while price rises indicates long build-up) (`source-reported`).
  - Statistically significant positive OLS slope when regressing next-hour return $r_{t+1}$ on $\alpha_{\text{OI}}$ on training data (`source-reported`).

### Independently reproduced

- `Not independently reproduced.`
- Primary data panel (`data_in_sample.csv` and CSV feature directories, ~6.5 GB) is proprietary course data not distributed in the public GitHub repository.

### Negative evidence

- **Severe Transaction Cost Fragility:**
  - The strategy fails completely under realistic crypto retail taker fees (4–5 bps per side), with Sharpe turning negative at 2.0 bps per side (`source-reported`).
- **Extreme Microstructure Decay:**
  - For Ridge and XGBoost individually, performance collapses by over 80% from Lag 0 to Lag 1, turning negative at Lag 2 (`source-reported`).
  - For the MACD sellback signal, Sharpe drops from 9.75 (Lag 0) to 3.29 (Lag 1) and 1.67 (Lag 2), turning negative by Lag 6 (`source-reported`).
- **Polynomial Feature Expansion Failure:**
  - Nonlinear polynomial expansion up to degree 4 generated negative out-of-sample contribution and was forced to zero weight in the final ensemble (`source-reported`).

## Falsification plan

1. **Passive Execution Feasibility Audit:**
   - **Protocol:** Backtest the signal in NautilusTrader with tick-level order book and trade flow data across top 50 Binance perpetuals (`research-proposed`).
   - **Test Metric:** Net Sharpe after simulating passive post-only limit order fills at bid/ask with realistic queue placement and adverse selection (`research-proposed`).
   - **Decision Rule:** If realized fill rate drops below 40% or adverse selection cost exceeds 1.5 bps per executed trade, the hypothesis that high-frequency ML alpha can be captured passively is falsified (`research-defined falsification threshold`).
2. **Turnover Netting & No-Trade Band Robustness:**
   - **Protocol:** Apply a deadband threshold $\tau \in [0.001, 0.005]$ to weight rebalancing $\Delta w_{i, t}$ to restrict hourly turnover from 0.35 to $<0.10$ (`research-proposed`).
   - **Decision Rule:** If reducing turnover to $\le 0.10$ causes Lag-1 gross Sharpe to drop below 1.0, the strategy cannot be rescued by standard turnover management (`research-defined falsification threshold`).
3. **Out-of-Sample Horizon Walk-Forward Test:**
   - **Protocol:** Extend the rolling 12-month walk-forward framework through 2025–2026 data (`research-proposed`).
   - **Decision Rule:** If Lag-1 out-of-sample gross Sharpe drops below 1.0 across any continuous 6-month evaluation window, the signal is falsified due to factor crowding or structural microstructure shifts (`research-defined falsification threshold`).
4. **Regime Conditioning & Spread Stress:**
   - **Protocol:** Partition evaluation hours by cross-sectional median bid-ask spread and realized volatility (`research-proposed`).
   - **Decision Rule:** If alpha is concentrated exclusively in hours where quoted spread exceeds 3 bps (where fills cannot occur at mid), the edge is an artifact of mid-quote pricing illusion (`research-defined falsification threshold`).

## Crypto portability

- **Portability Classification:** `direct` (`source-reported`).
- **Asset Class Alignment:** Designed and evaluated directly on cryptocurrency perpetual futures contracts across an 18-month historical panel.
- **Perpetual-Specific Dynamics:**
  - *Funding Rates:* Funding rate levels and changes are explicitly incorporated as input features and conditioners (`source-reported`).
  - *24/7 Continuous Trading:* Hourly walk-forward windows operate continuously without weekend or overnight session gaps (`source-reported`).
  - *Shorting Friction:* Crypto perpetuals allow frictionless symmetric shorting without equity-style borrow locates or short borrow fees (`source-reported`).
  - *Liquidation Risk & Tail Squeezes:* Extreme funding and open-interest spikes create liquidation cascades; the MACD sellback filter partially mitigates being caught in tail cascades by detecting momentum deceleration (`research-interpretation`).

## Limitations

- **Proprietary Feature Transparency Gap:** The exact mathematical definitions of the 266 external CSV features (`feature_*.csv`) and 35 conditioners (`conditioner_*.csv`) are not explicitly enumerated in the repository, representing a data provenance gap (`source-reported`).
- **Zero-Cost Pricing Illusion:** The headline Sharpe of 9.75 is entirely theoretical, as it assumes costless instantaneous execution at bar close; net alpha under taker fees is zero or negative (`source-reported`).
- **Lack of Market Impact Modeling:** At a turnover of 35% per hour across ~212 instruments, portfolio capacity is heavily constrained by market impact in less liquid altcoins (`research-interpretation`).
- **Not Independently Reproduced:** Pipeline has not been executed on our internal NautilusTrader / PyBroker cluster (`research-only`).

## Implementation status

- `not-implemented`
- No code from this repository has been merged into `nautilus-quant-system`, PyBroker backtest suites, paper trading, or live execution bots.

## Adoption boundary

- `not-approved`
- Research capture only. This record documents an empirical academic study on ML signal decay and turnover friction on crypto perpetuals. It does not authorize capital allocation, testnet deployment, or live trading.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `crypto-cross-sectional-lead-lag-rotation-hyperliquid-perps-2026-09-13.md`
- `btcusdt-ppo-continuation-audit-imbalance-override-2026-09-14.md`
- `apff-multi-asset-perpetual-adaptive-factor-factory-2026-09-16.md`

## Sources

- **Primary Source Code and Documentation:**
  - Repository: https://github.com/IliassSjm/crypto-perps-alpha
  - Full Commit SHA: `9faca06b944d333b8169158ed0ef8cdbe8707662`
  - Author: Sijelmassi Iliass (`IliassSjm`), HEC Paris
  - Release Date: 2026-07-03 01:51:36 UTC
  - Key Inspected Files:
    - `README.md` (https://github.com/IliassSjm/crypto-perps-alpha/blob/9faca06b944d333b8169158ed0ef8cdbe8707662/README.md)
    - `src/alpha_config.py` (https://github.com/IliassSjm/crypto-perps-alpha/blob/9faca06b944d333b8169158ed0ef8cdbe8707662/src/alpha_config.py)
    - `src/alpha_utils.py` (https://github.com/IliassSjm/crypto-perps-alpha/blob/9faca06b944d333b8169158ed0ef8cdbe8707662/src/alpha_utils.py)
    - `src/step1_features.py` (https://github.com/IliassSjm/crypto-perps-alpha/blob/9faca06b944d333b8169158ed0ef8cdbe8707662/src/step1_features.py)
    - `src/step2_polymodel.py` (https://github.com/IliassSjm/crypto-perps-alpha/blob/9faca06b944d333b8169158ed0ef8cdbe8707662/src/step2_polymodel.py)
    - `src/step3_ridge.py` (https://github.com/IliassSjm/crypto-perps-alpha/blob/9faca06b944d333b8169158ed0ef8cdbe8707662/src/step3_ridge.py)
    - `src/step4_xgboost.py` (https://github.com/IliassSjm/crypto-perps-alpha/blob/9faca06b944d333b8169158ed0ef8cdbe8707662/src/step4_xgboost.py)
    - `src/step5_evaluate.py` (https://github.com/IliassSjm/crypto-perps-alpha/blob/9faca06b944d333b8169158ed0ef8cdbe8707662/src/step5_evaluate.py)
    - `oi_divergence_alpha.py` (https://github.com/IliassSjm/crypto-perps-alpha/blob/9faca06b944d333b8169158ed0ef8cdbe8707662/oi_divergence_alpha.py)
    - `tests/test_pipeline.py` (https://github.com/IliassSjm/crypto-perps-alpha/blob/9faca06b944d333b8169158ed0ef8cdbe8707662/tests/test_pipeline.py)
    - `notebooks/alpha_strategy.ipynb` (https://github.com/IliassSjm/crypto-perps-alpha/blob/9faca06b944d333b8169158ed0ef8cdbe8707662/notebooks/alpha_strategy.ipynb)
