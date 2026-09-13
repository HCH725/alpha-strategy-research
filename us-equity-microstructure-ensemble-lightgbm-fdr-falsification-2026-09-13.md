---
schema: strategy-research-record-v1
title: "US Equity Intraday Microstructure Ensemble: LightGBM Walk-Forward Information Coefficient, Two-Tier Cross-Sectional Ranking, and Benjamini-Hochberg Multiple-Testing Falsification"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equities
  - us-equities
  - market-microstructure
  - order-flow-imbalance
  - vpin
  - hawkes-process
  - lightgbm
  - walk-forward
  - information-coefficient
  - benjamini-hochberg
  - multiple-testing
  - falsification
  - negative-evidence
status: research-only
confidence: high
source_as_of: 2026-09-13
sources:
  - "https://github.com/Breeganzo/AlphaFlow/tree/c5ad8357e7a8b5118afc8aafc06c74735395bc65"
  - "https://github.com/Breeganzo/AlphaFlow/blob/c5ad8357e7a8b5118afc8aafc06c74735395bc65/README.md"
  - "https://github.com/Breeganzo/AlphaFlow/blob/c5ad8357e7a8b5118afc8aafc06c74735395bc65/RESEARCH.md"
  - "https://github.com/Breeganzo/AlphaFlow/blob/c5ad8357e7a8b5118afc8aafc06c74735395bc65/notebooks/reproduce.ipynb"
  - "https://github.com/Breeganzo/AlphaFlow/blob/c5ad8357e7a8b5118afc8aafc06c74735395bc65/alpha_flow/config/settings.py"
  - "https://github.com/Breeganzo/AlphaFlow/blob/c5ad8357e7a8b5118afc8aafc06c74735395bc65/alpha_flow/core/vpin.py"
  - "https://github.com/Breeganzo/AlphaFlow/blob/c5ad8357e7a8b5118afc8aafc06c74735395bc65/alpha_flow/core/ofi_calculator.py"
  - "https://github.com/Breeganzo/AlphaFlow/blob/c5ad8357e7a8b5118afc8aafc06c74735395bc65/alpha_flow/core/hawkes.py"
  - "https://github.com/Breeganzo/AlphaFlow/blob/c5ad8357e7a8b5118afc8aafc06c74735395bc65/alpha_flow/core/amihud.py"
  - "https://github.com/Breeganzo/AlphaFlow/blob/c5ad8357e7a8b5118afc8aafc06c74735395bc65/alpha_flow/core/spread_tracker.py"
  - "https://github.com/Breeganzo/AlphaFlow/blob/c5ad8357e7a8b5118afc8aafc06c74735395bc65/alpha_flow/core/lee_ready.py"
  - "https://github.com/Breeganzo/AlphaFlow/blob/c5ad8357e7a8b5118afc8aafc06c74735395bc65/alpha_flow/core/vwap.py"
  - "https://github.com/Breeganzo/AlphaFlow/blob/c5ad8357e7a8b5118afc8aafc06c74735395bc65/alpha_flow/core/volume_clock.py"
  - "https://github.com/Breeganzo/AlphaFlow/blob/c5ad8357e7a8b5118afc8aafc06c74735395bc65/alpha_flow/analysis/intraday_engine.py"
  - "https://github.com/Breeganzo/AlphaFlow/blob/c5ad8357e7a8b5118afc8aafc06c74735395bc65/alpha_flow/analysis/signal_classification.py"
  - "https://github.com/Breeganzo/AlphaFlow/blob/c5ad8357e7a8b5118afc8aafc06c74735395bc65/alpha_flow/analysis/portfolio_engine.py"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# US Equity Intraday Microstructure Ensemble: LightGBM Walk-Forward Information Coefficient, Two-Tier Cross-Sectional Ranking, and Benjamini-Hochberg Multiple-Testing Falsification

## Provenance

- **Primary Source Codebase:** `Breeganzo/AlphaFlow` (*AlphaFlow: Market-microstructure alpha research engine with a fully deterministic long-short signal, walk-forward validation and Benjamini-Hochberg correction across ~50 tickers*), authored by Breeganzo (`source-reported`).
- **Canonical Source Identity:** GitHub repository `https://github.com/Breeganzo/AlphaFlow` at immutable commit SHA `c5ad8357e7a8b5118afc8aafc06c74735395bc65` (committed 2026-09-13 02:22:02 UTC) (`source-reported`).
- **Primary Research Monograph:** `RESEARCH.md` (31,872 bytes) in `Breeganzo/AlphaFlow` detailing econometric foundations, walk-forward LightGBM modeling, SHAP importance, alpha decay half-life, two-tier portfolio architecture, and multiple-testing false discovery rate falsification (`source-reported`).
- **Executable Reproduction Artifact:** `notebooks/reproduce.ipynb` in `Breeganzo/AlphaFlow`, providing end-to-end reproduction of the 50-stock cross-sectional panel, Benjamini-Hochberg FDR threshold table, and summary metrics (`source-reported`).
- **Key Implementation Paths Directly Inspected:**
  - `alpha_flow/config/settings.py`: Pinned 50 S&P 500 ticker universe, walk-forward windows (`WF_TRAIN_WINDOW=252`, `WF_TEST_WINDOW=21`, `WF_HORIZON=1`), signal classification constants (`SIGNAL_RANK_FRACTION=0.20`, `SIGNAL_SIGNIFICANCE_ALPHA=0.10`, `SIGNAL_CROSS_Z_MIN=0.50`), and risk management settings (`source-reported`).
  - `alpha_flow/core/vpin.py`: Bulk Volume Classification (BVC) rolling VPIN ($window=20$) and outer z-score normalisation ($norm\_window=60$) (`source-reported`).
  - `alpha_flow/core/ofi_calculator.py`: Bar-level Order Flow Imbalance proxy using close-vs-open volume partitioning and rolling 20-bar z-score (`source-reported`).
  - `alpha_flow/core/hawkes.py`: Hawkes self-exciting process intensity z-score via L-BFGS-B maximum likelihood estimation (`source-reported`).
  - `alpha_flow/core/amihud.py`: Rolling Amihud illiquidity ratio ($window=21$) and Kyle's lambda price impact regression clipped to $[-6, 6]$ (`source-reported`).
  - `alpha_flow/core/spread_tracker.py`: Corwin-Schultz high-low spread estimator with exponential smoothing (`SPREAD_SMOOTH=5` bars) (`source-reported`).
  - `alpha_flow/core/lee_ready.py`: Lee-Ready tick test trade direction indicator (`source-reported`).
  - `alpha_flow/core/vwap.py`: Intraday session-reset VWAP deviation z-score ($window=20$) (`source-reported`).
  - `alpha_flow/core/volume_clock.py`: Dollar-volume-thresholded volume clock imbalance z-score (`source-reported`).
  - `alpha_flow/analysis/intraday_engine.py`: 13-feature matrix construction, 1st/99th percentile winsorization, strictly sequential walk-forward loop with 1-bar embargo gap, LightGBM Regressor fitting, out-of-sample Spearman rank IC, IC Information Ratio ($IC\_IR$), Newey-West/t-distribution p-values, Moreira-Muir volatility targeting, and SHAP TreeExplainer attribution (`source-reported`).
  - `alpha_flow/analysis/signal_classification.py`: Two-tier architecture separating Tier-1 tradeable rank spread (top/bottom quintiles with adaptive $\ge 0.5\sigma$ dispersion gate) from Tier-2 Benjamini-Hochberg FDR significance testing (`source-reported`).
  - `alpha_flow/analysis/portfolio_engine.py`: Multi-stock long-short portfolio aggregation, Corwin-Schultz half-spread transaction cost deductions at monthly rebalance dates, and risk-adjusted performance metrics (`source-reported`).
- **Deduplication Audit:** A comprehensive audit across all strategy records in this repository confirms zero pre-existing records citing `Breeganzo`, `AlphaFlow`, or this 13-feature microstructure LightGBM walk-forward ensemble. Prior microstructure records in the repository evaluate isolated indicators or distinct methodologies (e.g. `order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12.md` on NASDAQ LOBSTER data, `binance-perpetual-order-flow-imbalance-horizon-decay-queue-imbalance-falsification-2026-09-13.md` on Binance 100 ms `bookTicker` OFI decay, `crypto-volume-synchronized-probability-of-toxicity-vpin-microstructure-2026-08-31.md` on standalone VPIN breakout thresholds, and `hawkes-order-flow-imbalance-self-excitation-microstructure-2026-09-12.md` on bivariate Hawkes point processes). Breeganzo's study provides an independent, multi-asset econometric falsification demonstrating that across 50 US large-cap equities, while naive single-ticker tests exhibit apparently significant t-statistics, **zero tickers survive Benjamini-Hochberg FDR multiple-testing correction** ($Q=0.10$), and daily OFI collapses to zero ($IC \approx -0.007$), isolating the fundamental trade-off between cross-sectional rank-spread monetisation and time-series statistical significance.

## Economic mechanism

### Source-reported

1. **Order Flow Imbalance and Price Impact (Chordia et al. 2002; Kyle 1985):**
   When informed market participants execute large orders, their private information is revealed through directional imbalances in order flow. Under Kyle's lambda framework, net aggressive buying depletes resting liquidity and induces price adjustments ($\Delta P = \lambda \cdot \text{signed\_volume} + \epsilon$). At intraday horizons, persistent order imbalances generate short-lived directional drift (`source-reported`).
2. **Volume-Synchronized Probability of Informed Trading (VPIN, Easley et al. 2012):**
   Traditional calendar-time sampling obscures periods of rapid information arrival. Using Bulk Volume Classification (BVC), VPIN measures the volume imbalance across price ranges:
   $$\text{buy\_frac} = \frac{close - low}{high - low}, \quad VPIN = \frac{1}{n} \sum \frac{|V_{buy} - V_{sell}|}{V_{bar}}$$
   High VPIN values signal elevated flow toxicity and adverse selection, predicting short-term volatility expansion and price impact (`source-reported`).
3. **Self-Exciting Order Arrival Dynamics (Hawkes, Bacry et al. 2015):**
   Order flow exhibits clustering and endogenous feedback, where the arrival of one trade increases the conditional probability of subsequent trades:
   $$\lambda(t) = \mu + \sum_{t_i < t} \alpha e^{-\beta(t - t_i)}$$
   Elevated Hawkes intensity identifies regimes of self-reinforcing liquidity cascades and momentum, particularly in high-beta assets (`source-reported`).
4. **Institutional VWAP Mean Reversion (Almgren & Chriss 2001):**
   Institutional execution algorithms (TWAP/VWAP) benchmark against the volume-weighted average price. When market price extends beyond $\pm 2\sigma$ from session VWAP, algorithmic execution schedules systematically create mean-reverting resistance, penalizing fills far from the benchmark (`source-reported`).
5. **The Multiple-Testing Fallacy (Harvey, Liu & Zhu 2016; Benjamini & Hochberg 1995):**
   In a universe of $N=50$ assets, standard uncorrected hypothesis testing ($|t| > 2.0$, $p < 0.05$) is guaranteed to produce 2 to 3 false discoveries by pure chance. To ensure that an observed Information Coefficient represents genuine skill rather than selection bias, the Benjamini-Hochberg False Discovery Rate (FDR) procedure controls the expected proportion of false positives across the entire testing panel (`source-reported`).

### Research interpretation

- **The Bar-Level Order Flow Resolution Barrier:**
  The source highlights a fundamental econometric friction: true Order Flow Imbalance requires high-frequency tick data with trade-by-trade classification (Lee-Ready tick test on Level 1/Level 2 order books). When forced to operate on bar-level OHLCV data, the proxy classifies an entire bar as buyer- or seller-initiated based solely on $close \ge open$. This aggregation discards intra-bar price trajectories and queue dynamics, creating an upper bound on Information Coefficients ($\approx 1.0\%\text{--}1.5\%$) and causing daily-resolution OFI to degenerate entirely ($IC = -0.007$).
- **Cross-Sectional Rank Spread vs. Per-Name Significance:**
  A central methodological insight is the structural distinction between individual time-series significance and cross-sectional portfolio monetisation. In an equity long-short book, profitability depends on the rank spread—whether the top quintile outperforms the bottom quintile on average—governed by Grinold & Kahn's Fundamental Law ($IR \approx IC \times \sqrt{N}$). Even when zero individual stocks clear an FDR multiple-testing hurdle (confirming that no single stock's predictability is individually proven), the aggregate cross-sectional rank spread can still generate a positive gross Sharpe (+0.42), provided execution costs and turnover do not consume the margin.

## Signal

### Feature Construction (13 Intraday Microstructure Features)

All features are evaluated on 1-hour OHLCV bars across each ticker's time series (`source-reported`):
1. **OFI z-score (`ofi_zscore`):**
   $$\text{buy\_vol} = V \cdot \mathbf{1}_{\{close \ge open\}}, \quad \text{sell\_vol} = V \cdot \mathbf{1}_{\{close < open\}}$$
   $$\text{raw\_ofi} = \frac{\text{buy\_vol} - \text{sell\_vol}}{V}, \quad \text{ofi\_zscore} = \frac{\text{raw\_ofi} - \mu_{20}}{\sigma_{20}}$$
   where $\mu_{20}$ and $\sigma_{20}$ are the 20-bar rolling mean and sample standard deviation (`source-reported`).
2. **Amihud Illiquidity (`amihud`):**
   $$ILLIQ_t = \frac{|r_t|}{P_t \cdot V_t} \times 10^6$$
   averaged over a 21-day rolling window (`source-reported`).
3. **Kyle's Lambda (`kyle_lambda`):**
   Rolling OLS regression coefficient of bar price change on signed volume: $\Delta P_t = \lambda \cdot \text{sign\_vol}_t + \epsilon_t$, normalized via 100-bar rolling z-score and clipped to $[-6, +6]$ (`source-reported`).
4. **Corwin-Schultz Spread (`cs_spread`):**
   Bid-ask spread estimator derived from 2-day high-low price ratios, smoothed via exponential moving average with halflife of 5 bars (`source-reported`).
5. **Lee-Ready Tick Sign (`tick_sign`):**
   Directional indicator: $+1$ if $P_t > P_{t-1}$, $-1$ if $P_t < P_{t-1}$, forward-filled on zero-tick bars (`source-reported`).
6. **VWAP Deviation z-score (`vwap_zscore`):**
   Session VWAP with daily reset at 00:00 UTC:
   $$VWAP_t = \frac{\sum_{\tau \in \text{day}} TP_\tau \cdot V_\tau}{\sum_{\tau \in \text{day}} V_\tau}, \quad TP = \frac{H+L+C}{3}$$
   $$vwap\_zscore_t = \frac{P_t - VWAP_t}{\sigma_{20}}$$
   where $\sigma_{20}$ is the 20-bar rolling standard deviation of price around VWAP (`source-reported`).
7. **Volume Clock Imbalance (`volume_zscore`):**
   Normalized volume imbalance $(V_{buy} - V_{sell})/V$ sampled on $\$1,000,000$ volume thresholds, z-scored over 20 bars (`source-reported`).
8. **Hawkes Self-Excitation Intensity (`hawkes_zscore`):**
   Maximum likelihood estimation of baseline intensity $\mu$, excitement $\alpha=0.5$, and decay $\beta=0.3$, transformed into a rolling z-score (`source-reported`).
9. **VPIN Toxicity z-score (`vpin_zscore`):**
   Bulk Volume Classification bar VPIN smoothed over 20 bars, then z-scored over a 60-bar outer normalization window:
   $$buy\_frac = \text{clip}\left(\frac{close - low}{high - low}, 0, 1\right), \quad bar\_vpin = \frac{|2 \cdot buy\_frac - 1| \cdot V}{V}$$
   $$VPIN_{20} = \frac{1}{20} \sum_{i=0}^{19} bar\_vpin_{t-i}, \quad vpin\_zscore = \frac{VPIN_{20} - \mu_{60}}{\sigma_{60}}$$
   (`source-reported`).
10. **1-Hour Lagged Return (`ret_1h`):** $(P_{t-1} - P_{t-2})/P_{t-2}$ (`source-reported`).
11. **3-Hour Lagged Return (`ret_3h`):** $(P_{t-1} - P_{t-4})/P_{t-4}$ (`source-reported`).
12. **6-Hour Lagged Return (`ret_6h`):** $(P_{t-1} - P_{t-7})/P_{t-7}$ (`source-reported`).
13. **Volume Ratio (`vol_ratio`):** $V_t / \text{rolling\_mean}(V, 20)$ (`source-reported`).

### Prediction Target & Model Architecture

- **Prediction Target:** $y_t = ret.shift(-1) = (P_{t+1} - P_t)/P_t$ (1-bar-ahead return) (`source-reported`).
- **Data Preprocessing:** Features are winsorized at the 1st and 99th percentiles across the training set (`source-reported`).
- **Machine Learning Regressor:** LightGBM Regressor (`LGBMRegressor`) with hyperparameters: `n_estimators=300`, `learning_rate=0.05`, `max_depth=4`, `num_leaves=15`, `min_child_samples=10`, `subsample=0.8`, `colsample_bytree=0.8`, `random_state=42` (`source-reported`).
- **Walk-Forward Validation Protocol:**
  - Rolling training window: $1,260$ hourly bars ($\approx 252$ trading days / 1 year) (`source-reported`).
  - Out-of-sample test window: $105$ hourly bars ($\approx 21$ trading days / 1 month) (`source-reported`).
  - Embargo gap: $1$ bar between train end and test start to eliminate forward-label target leakage (`source-reported`).
  - Number of folds: 19 to 27 sequential walk-forward folds per ticker (`source-reported`).

### Two-Tier Signal Classification & Portfolio Mapping

1. **Directional Adjustment:**
   Because Spearman rank IC measures correlation rather than direction, an asset with negative mean IC is contrarian-useful. The tradeable directional signal flips sign accordingly (`source-reported`):
   $$signal\_dir = \text{sign}(\overline{IC}), \quad latest\_signal = signal\_dir \cdot \hat{y}_t$$
2. **Tier-1 Tradeable Book (`classify_signal`):**
   - Candidate Selection: Quintile split (`SIGNAL_RANK_FRACTION=0.20`), selecting the top 20% (10 tickers) as BUY candidates and bottom 20% (10 tickers) as SELL candidates (`source-reported`).
   - Adaptive Dispersion Gate (`SIGNAL_CROSS_Z_MIN=0.50`): A candidate is confirmed only if its directional signal is at least $0.5$ standard deviations away from the cross-sectional mean ($z_{cross} \ge +0.5$ for BUY, $z_{cross} \le -0.5$ for SELL) (`source-reported`).
   - Sign Consistency Check: Long candidates require $latest\_signal \ge 0$; short candidates require $latest\_signal \le 0$ (`source-reported`).
3. **Tier-2 High-Conviction Annotation (`is_high_conviction`):**
   - Computes two-sided p-values for each ticker's mean IC against $H_0: IC = 0$ using Student's t-distribution with $N_{folds}-1$ degrees of freedom (`source-reported`).
   - Evaluates the Benjamini-Hochberg (1995) FDR threshold across all $m=50$ p-values at target false discovery rate $Q=0.10$:
     $$p_{(k)} \le \frac{k}{m} \cdot Q$$
   - A ticker is flagged as high-conviction if its individual p-value is $\le$ the BH threshold. This acts as an audit annotation and is deliberately **not** used to gate the Tier-1 book (`source-reported`).
4. **Execution & Volatility Targeting (`research-proposed`):**
   - Order execution: Market-on-Open at bar $t+1$ (`research-proposed`).
   - Moreira & Muir (2017) Volatility Targeting: Position weight scaled by $w_t = \text{clip}(target\_vol / \sigma_{20}, 0.1, 2.0)$, where $target\_vol = 0.15 / \sqrt{1638} \approx 0.0037$ per hourly bar (`source-reported`).
   - Holding Period: 105 hourly bars (monthly rebalance) or position exit upon signal sign reversal (`source-reported` / `research-proposed`).

## Required data

- **Asset Class / Universe:** US Equities — 50 large-cap S&P 500 constituents covering all 11 GICS sectors (`AAPL`, `MSFT`, `NVDA`, `META`, `GOOGL`, `AMZN`, `AVGO`, `ORCL`, `AMD`, `INTC`, `TSM`, `JPM`, `BAC`, `V`, `GS`, `WFC`, `MS`, `BLK`, `C`, `AXP`, `MA`, `JNJ`, `UNH`, `LLY`, `PFE`, `ABBV`, `MRK`, `TMO`, `TSLA`, `HD`, `MCD`, `NKE`, `SBUX`, `KO`, `PEP`, `WMT`, `COST`, `XOM`, `CVX`, `COP`, `EOG`, `CAT`, `HON`, `BA`, `RTX`, `GE`, `DIS`, `T`, `VZ`, `NFLX`) (`source-reported`).
- **Venue & Data Product:** Alpaca Market Data IEX feed (free tier, covering 2–5% of US equity volume) with Yahoo Finance fallback (`source-reported`).
- **Sampling Interval:** 1-hour uniform OHLCV bars over a 730-calendar-day sample period ($\approx 3,276$ hourly bars per ticker) (`source-reported`).
- **Data Fields Required:**
  - `open`, `high`, `low`, `close` (float64)
  - `volume` (float64)
  - DatetimeIndex with US Eastern market hours awareness (`source-reported`).
- **Causality & Leakage Controls:**
  - Rolling walk-forward splits; zero backward lookahead in training folds (`source-reported`).
  - 1-bar embargo gap separating train and test folds to prevent target-return overlap (`source-reported`).
  - Outlier handling: Feature clipping at 1st and 99th percentiles using training-fold quantiles only (`source-reported`).

## Execution assumptions

- **Execution Timing:** Signals calculated at the close of hourly bar $t$ are assumed to execute on the opening print of bar $t+1$ (`source-reported` / `research-proposed`).
- **Transaction Cost Model:**
  - Evaluated in portfolio engine using Corwin-Schultz (2012) estimated half-spread deducted per leg on each monthly rebalance (`source-reported`).
  - Average realized half-spread across the 50-ticker panel: $\approx 5.0\text{ bps}$ ($0.0005$) (`source-reported`).
  - Commission assumption: zero in baseline Alpaca paper engine; $1.0\text{ bp}$ per share in institutional stress models (`research-proposed`).
  - Market impact: Omitted in primary walk-forward simulations; represented as a future research requirement (`source-reported`).
- **Rebalance Frequency:** Every 105 hourly bars ($\approx 21$ trading days / 1 month) (`source-reported`).
- **Leverage & Shorting Constraints:** Dollar-neutral long-short portfolio with gross leverage capped at $2.0\times$ under Moreira-Muir volatility scaling (`source-reported`). Short borrowing availability is assumed frictionless for S&P 500 large caps (`research-proposed`).

## Evidence

### Source-reported

All quantitative metrics below trace directly to `RESEARCH.md` (§4) and `notebooks/reproduce.ipynb` (§4, §6, §9) evaluated across the 50-ticker panel over ~730 days of hourly data (`source-reported`).

#### 1. Cross-Sectional Hourly Performance Summary (50-Ticker Panel)

| Metric | Source-Reported Value |
| :--- | :--- |
| **Universe Size** | 50 S&P 500 large-cap equities |
| **Feature Count** | 13 intraday microstructure features |
| **Walk-Forward Folds** | 19 to 27 folds per ticker |
| **Tradeable Book (Tier 1)** | 10 Long / 10 Short / 30 Hold (top/bottom 20% quintile) |
| **Average Absolute IC ($\overline{\|IC\|}$)** | **1.42%** (median 1.12%, max 5.24%) |
| **Tickers with Uncorrected $\|t\| > 2.0$** | **3 of 50** (6.0%) |
| **Tickers with Uncorrected $p < 0.10$** | **4 of 50** (8.0%) |
| **High-Conviction Tickers Surviving BH-FDR ($Q=0.10$)** | **0 of 50** (0.0%) |
| **Average Gross Annualized Sharpe** | **+0.42** |
| **Average Sortino Ratio** | **+0.63** |
| **Average Directional Hit Rate** | **50.2%** |
| **Daily-Resolution OFI Mean IC** | **-0.007** ($\approx 0$, confirming daily OHLCV failure) |

#### 2. Strongest Single-Ticker Signals (Before Multiple-Testing Correction)

| Ticker | Out-of-Sample IC | IC SEM | IC t-stat | p-value | Gross Sharpe |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TSM** | +5.24% | 2.05% | +2.55 | 0.018 | +1.77 |
| **ORCL** | -4.22% | 1.51% | -2.79 | 0.011 | +1.94 |
| **KO** | +4.13% | 2.60% | +1.59 | 0.125 | +1.07 |
| **EOG** | +3.74% | 1.94% | +1.93 | 0.067 | +0.95 |
| **WMT** | -3.85% | 2.24% | -1.72 | 0.098 | +0.46 |
| **NFLX** | +3.22% | 1.39% | +2.32 | 0.030 | +1.41 |

#### 3. Benjamini-Hochberg FDR Multiple-Testing Elimination Table

Under Benjamini-Hochberg procedure with false discovery rate $Q=0.10$ across $m=50$ simultaneous tests, each ranked p-value $p_{(k)}$ must satisfy $p_{(k)} \le \frac{k}{50} \times 0.10$ (`source-reported`):

| Rank ($k$) | Ticker | Uncorrected p-value | BH Threshold ($\frac{k}{50} \times 0.10$) | Survives FDR? |
| :--- | :--- | :--- | :--- | :--- |
| **1** | ORCL | 0.0110 | **0.0020** | **NO** |
| **2** | TSM | 0.0180 | **0.0040** | **NO** |
| **3** | NFLX | 0.0300 | **0.0060** | **NO** |
| **4** | EOG | 0.0670 | **0.0080** | **NO** |
| **5** | WMT | 0.0980 | **0.0100** | **NO** |
| **6** | KO | 0.1250 | **0.0120** | **NO** |
| ... | ... | ... | ... | **NO** |

**Empirical Verdict:** Because the best p-value in the entire 50-stock batch (0.011) fails to clear the required first-rank threshold of $0.0020$, **exactly zero tickers survive multiple-testing correction** (`source-reported`).

#### 4. SHAP Feature Attribution & Collinearity Audit

- **High-Beta Equities (TSLA, NVDA):** Hawkes self-excitation intensity z-score (`hawkes_zscore`) ranks #1 in SHAP importance, validating endogenous order clustering in high-volatility assets (`source-reported`).
- **Stable Large-Caps (AAPL, JPM):** OFI z-score (`ofi_zscore`) dominates SHAP importance, aligning with classical adverse selection literature (`source-reported`).
- **VPIN Toxicity Contribution:** VPIN z-score (`vpin_zscore`) provides non-collinear explanatory power; maximum pairwise correlation with any other feature is $|\rho| = 0.31$ (highest overall matrix correlation is $|\rho| = 0.38$ between VWAP z and Kyle $\lambda$) (`source-reported`).

### Independently reproduced

- Not independently reproduced. All metrics and tabular regressions represent primary research outputs reported by Breeganzo in GitHub repository `Breeganzo/AlphaFlow` (commit `c5ad8357e7a8b5118afc8aafc06c74735395bc65`). No internal simulation has been run in our stack.

### Negative evidence

1. **Complete Multiple-Testing Falsification (0 of 50 Surviving Stocks):**
   When Benjamini-Hochberg FDR control ($Q=0.10$) is applied to correct for the 50 simultaneous hypothesis tests, zero tickers survive. The 3 tickers with $|t| > 2.0$ (6%) and 4 tickers with $p < 0.10$ (8%) fall entirely within the expected random discovery rate under the null hypothesis of zero predictive skill (`source-reported`).
2. **Degeneration of Daily-Resolution Order Flow Imbalance:**
   Evaluating the identical OFI signal on daily OHLCV bars produces an average Information Coefficient of $-0.007$ ($\approx 0$). This proves that bar-level approximations cannot capture order flow dynamics once the aggregation window exceeds the sub-hourly latency envelope of institutional order execution (`source-reported`).
3. **Transaction Cost Vulnerability:**
   Average gross Sharpe ratio across the 50-stock panel is modest (+0.42) with an average hit rate of 50.2%. Because Corwin-Schultz half-spreads average ~5.0 bps per rebalance, increasing portfolio turnover or shortening the rebalancing horizon from monthly (105 bars) to daily or intraday quickly erodes net returns to zero or negative territory (`source-reported`).

## Falsification plan

1. **Tick-Level Data Upgrade (TAQ / Databento) Falsification Test:**
   - *Test:* Replace the bar-level OFI proxy ($close \ge open$) and BVC VPIN with true Lee-Ready trade classification computed on trade-by-trade Level 1/Level 2 tick data across the identical 50-stock universe.
   - *Decision Rule:* If average absolute Information Coefficient fails to exceed $3.0\%$ or if fewer than 5 tickers survive Benjamini-Hochberg FDR correction at $Q=0.10$ (`research-defined falsification threshold`), reject the hypothesis that order flow imbalance possesses economically viable stand-alone alpha in liquid large-cap US equities.
2. **Shuffled-Target Placebo Audit:**
   - *Test:* Permute the forward target returns $y_t$ across time within each ticker to destroy temporal autocorrelation while preserving marginal return distributions. Re-run the walk-forward LightGBM pipeline across 500 Monte Carlo iterations.
   - *Decision Rule:* If the observed average $|IC| = 1.42\%$ fails to exceed the 95th percentile of the shuffled placebo distribution ($|IC|_{null, 95\%} \approx 1.25\%$) (`research-defined falsification threshold`), confirm that the reported walk-forward IC is indistinguishable from feature overfitting.
3. **Subperiod & Crisis Regime Stability Test:**
   - *Test:* Evaluate the 13-feature LightGBM model across severe market drawdown regimes (e.g. 2020 COVID crash, 2022 rate hike regime) rather than calm 2-year windows.
   - *Decision Rule:* If max drawdown exceeds $-25\%$ or if net Sharpe drops below $-0.50$ during volatile regimes (`research-defined falsification threshold`), reject the claim that volatility targeting and Hawkes intensity stabilize drawdown risk.
4. **Turnover & Execution Friction Stress Test:**
   - *Test:* Apply an institutional execution friction model (5.0 bps half-spread + 1.0 bp commission + 2.0 bps square-root market impact) while sweeping rebalance frequencies from 1 hour to 105 hours.
   - *Decision Rule:* If net Sharpe is negative across all rebalance frequencies $\le 21$ hours (1 trading day) (`research-defined falsification threshold`), confirm that intraday microstructure signals cannot be executed actively and serve only as passive execution filters.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven` (`research-proposed`).
- **Rationale:** The source investigates US cash equities exclusively using Alpaca/yfinance hourly bars. The mechanism has not been demonstrated on crypto assets by the cited source.
- **Portability Specifics & Microstructure Considerations:**
  - *Native Tick Feeds vs Heuristic Proxies:* Unlike US equities where true tick data requires paid institutional feeds (TAQ/SIP/Databento), major crypto perpetual exchanges (Binance, Bybit, OKX, Hyperliquid) broadcast continuous public Level 2 order books and real-time trade streams containing explicit aggressor flags (`is_buyer_maker`). This eliminates the need for heuristic Lee-Ready proxies or bar-level volume splitting, allowing direct calculation of true OFI and VPIN (`research-proposed`).
  - *24/7 Trading vs Daily Session Resets:* US equity VWAP resets at the 09:30 EST market open. In crypto's 24/7 continuous market, resetting VWAP at 00:00 UTC is an arbitrary calendar boundary rather than an economically enforced institutional auction reset (`research-proposed`).
  - *Perpetual Funding Rate Drag & Cascade Dynamics:* Crypto perpetuals incur 8-hour funding rate payments and liquidation cascade spikes. Holding long-short baskets across 50 altcoin perpetuals introduces cross-venue funding dispersion and liquidation contagion that dominate the ~1.4% gross IC margin (`research-proposed`).
  - *Taker Fee Barrier:* Binance VIP0 standard taker fees (5.0 bps per side, 10.0 bps round-trip) are substantially higher than US equity half-spreads, making high-turnover implementations of this model structurally unviable in crypto for non-VIP tiers (`research-proposed`).

## Limitations

- **Bar-Level Proxy Limitation:** The study utilizes hourly OHLCV bars rather than true tick-by-tick order book depth or Level 3 trade prints, forcing reliance on a crude close-versus-open volume partition for OFI.
- **Survivorship Bias:** The 50-ticker universe is constructed from current S&P 500 index members rather than point-in-time historical constituents, introducing survivorship distortion over the 2-year backtest window.
- **Low Signal Magnitude vs Cost Barrier:** An average absolute IC of $1.42\%$ and gross Sharpe of $+0.42$ provide minimal cushion against execution frictions, slippage, and borrow costs.
- **IEX Feed Coverage Gap:** Alpaca's free IEX feed captures only 2% to 5% of total US consolidated equity volume, meaning volume clock and VPIN calculations represent a thin sample of aggregate market liquidity.
- **Equal-Weighted Sizing Simplicity:** Paper trading utilizes fixed 10-share or flat-notional sizing without risk-parity or industry exposure constraints.

## Implementation status

- Frontmatter: `implementation_status: not-implemented`
- The strategy and feature extraction pipelines are fully implemented and verified in Breeganzo's upstream repository `Breeganzo/AlphaFlow` (commit `c5ad8357e7a8b5118afc8aafc06c74735395bc65`).
- No implementation exists in our local research stack (NautilusTrader, PyBroker, paper trading, testnet, or live trading).

## Adoption boundary

- Frontmatter: `status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.
- This record serves strictly as a quantitative research capture and falsification benchmark for intraday microstructure ensemble modeling and multiple-testing false discovery rate dynamics.
- It does not authorize strategy adoption, automated signal generation, paper trading, testnet execution, or capital deployment.

## Related Wiki records

- `[[quant/crypto-volume-synchronized-probability-of-toxicity-vpin-microstructure-2026-08-31]]` — Evaluates volume-synchronized probability of toxicity (VPIN) in cryptocurrency markets.
- `[[quant/hawkes-order-flow-imbalance-self-excitation-microstructure-2026-09-12]]` — Evaluates bivariate Hawkes self-exciting point processes on limit order book dynamics.
- `[[quant/order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12]]` — Evaluates contemporaneous-to-predictive decoupling and taker cost barriers for order flow imbalance.
- `[[quant/binance-perpetual-order-flow-imbalance-horizon-decay-queue-imbalance-falsification-2026-09-13]]` — Evaluates sub-second OFI horizon decay and static queue imbalance dominance on Binance USD-M futures.
- `[[quant/sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12]]` — Evaluates multiple testing controls and cointegration screening across S&P 500 pairs.

## Sources

- **Primary Research Codebase:** Breeganzo, *AlphaFlow: Market-microstructure alpha research engine with a fully deterministic long-short signal, walk-forward validation and Benjamini-Hochberg correction across ~50 tickers*, GitHub repository `https://github.com/Breeganzo/AlphaFlow` at commit SHA `c5ad8357e7a8b5118afc8aafc06c74735395bc65` (committed 2026-09-13 02:22:02 UTC) (`source-reported`).
- **Research Monograph:** `RESEARCH.md` in `Breeganzo/AlphaFlow` (commit `c5ad8357e7a8b5118afc8aafc06c74735395bc65`) (`source-reported`).
- **Reproducible Research Notebook:** `notebooks/reproduce.ipynb` in `Breeganzo/AlphaFlow` (`source-reported`).
- **Signal Configuration & Universe Specification:** `alpha_flow/config/settings.py` in `Breeganzo/AlphaFlow` (`source-reported`).
- **Microstructure Feature Implementations:** `alpha_flow/core/vpin.py`, `alpha_flow/core/ofi_calculator.py`, `alpha_flow/core/hawkes.py`, `alpha_flow/core/amihud.py`, `alpha_flow/core/spread_tracker.py`, `alpha_flow/core/lee_ready.py`, `alpha_flow/core/vwap.py`, and `alpha_flow/core/volume_clock.py` in `Breeganzo/AlphaFlow` (`source-reported`).
- **Walk-Forward ML & Classification Engines:** `alpha_flow/analysis/intraday_engine.py`, `alpha_flow/analysis/signal_classification.py`, and `alpha_flow/analysis/portfolio_engine.py` in `Breeganzo/AlphaFlow` (`source-reported`).
- **Foundational Econometric Literature:**
  - Almgren, R. & Chriss, N. (2001). *Optimal Execution of Portfolio Transactions*. Journal of Risk, 3(2), 5–39 (`source-reported`).
  - Amihud, Y. (2002). *Illiquidity and stock returns*. Journal of Financial Markets, 5(1), 31–56 (`source-reported`).
  - Bacry, E., Mastromatteo, I. & Muzy, J.F. (2015). *Hawkes Processes in Finance*. Market Microstructure and Liquidity, 1(01) (`source-reported`).
  - Benjamini, Y. & Hochberg, Y. (1995). *Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing*. Journal of the Royal Statistical Society: Series B (Methodological), 57(1), 289–300 (`source-reported`).
  - Chordia, T., Roll, R. & Subrahmanyam, A. (2002). *Order imbalance, liquidity, and market returns*. Journal of Financial Economics, 65(1), 111–130 (`source-reported`).
  - Corwin, S.A. & Schultz, P. (2012). *A Simple Way to Estimate Bid-Ask Spreads from Daily High and Low Prices*. Journal of Finance, 67(2), 719–759 (`source-reported`).
  - Easley, D., López de Prado, M. & O'Hara, M. (2012). *Flow Toxicity and Liquidity in a High-Frequency World*. Review of Financial Studies, 25(5), 1457–1493 (`source-reported`).
  - Grinold, R.C. & Kahn, R.N. (2000). *Active Portfolio Management* (2nd ed.). McGraw-Hill (`source-reported`).
  - Harvey, C.R., Liu, Y. & Zhu, H. (2016). *… and the Cross-Section of Expected Returns*. Review of Financial Studies, 29(1), 5–68 (`source-reported`).
  - Kyle, A.S. (1985). *Continuous Auctions and Insider Trading*. Econometrica, 53(6), 1315–1335 (`source-reported`).
  - Lee, C.M.C. & Ready, M.J. (1991). *Inferring Trade Direction from Intraday Data*. Journal of Finance, 46(2), 733–746 (`source-reported`).
  - López de Prado, M. (2018). *Advances in Financial Machine Learning*. John Wiley & Sons (`source-reported`).
  - Moreira, A. & Muir, T. (2017). *Volatility-Managed Portfolios*. Journal of Finance, 72(4), 1611–1644 (`source-reported`).
