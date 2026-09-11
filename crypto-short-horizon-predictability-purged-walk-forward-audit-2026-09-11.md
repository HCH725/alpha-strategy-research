---
schema: strategy-research-record-v1
title: "Crypto Short-Horizon Return Predictability: Purged Walk-Forward Audit with Nested-Model Tests and Multiple-Testing Control"
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - machine-learning
  - predictability
  - walk-forward-cross-validation
  - clark-west-test
  - multiple-testing
  - transaction-costs
status: research-only
confidence: medium
source_as_of: 2026-07-28
sources:
  - "https://github.com/ITheClixs/crypto-return-predictability"
  - "https://github.com/ITheClixs/crypto-return-predictability/tree/83881c7cd01ce45aca94dc7f050ccf22685a4a44"
  - "https://github.com/ITheClixs/crypto-return-predictability/blob/83881c7cd01ce45aca94dc7f050ccf22685a4a44/reports/results.md"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Short-Horizon Return Predictability: Purged Walk-Forward Audit with Nested-Model Tests and Multiple-Testing Control

## Provenance

- **Primary Source:** Mehmet Demir Guven. *Are Short-Horizon Cryptocurrency Returns Predictable Out of Sample? A purged walk-forward study with nested-model tests, transaction costs, and multiple-testing control*. Department of Computer Science, ETH Zürich.
- **Repository & Commit:** `https://github.com/ITheClixs/crypto-return-predictability` at immutable commit SHA `83881c7cd01ce45aca94dc7f050ccf22685a4a44` (committed 2026-07-28T18:22:23Z).
- **Stable URLs:**
  - Repository: [https://github.com/ITheClixs/crypto-return-predictability](https://github.com/ITheClixs/crypto-return-predictability)
  - Immutable tree: [https://github.com/ITheClixs/crypto-return-predictability/tree/83881c7cd01ce45aca94dc7f050ccf22685a4a44](https://github.com/ITheClixs/crypto-return-predictability/tree/83881c7cd01ce45aca94dc7f050ccf22685a4a44)
  - Results report: [https://github.com/ITheClixs/crypto-return-predictability/blob/83881c7cd01ce45aca94dc7f050ccf22685a4a44/reports/results.md](https://github.com/ITheClixs/crypto-return-predictability/blob/83881c7cd01ce45aca94dc7f050ccf22685a4a44/reports/results.md)
  - Full results table: [https://github.com/ITheClixs/crypto-return-predictability/blob/83881c7cd01ce45aca94dc7f050ccf22685a4a44/reports/results.csv](https://github.com/ITheClixs/crypto-return-predictability/blob/83881c7cd01ce45aca94dc7f050ccf22685a4a44/reports/results.csv)
- **Primary Data Analyzed in Source:**
  - Assets: Daily OHLCV price series for Bitcoin (BTC), Ethereum (ETH), and Solana (SOL) from Binance spot.
  - History length: January 1, 2019 to July 18, 2026 (BTC and ETH: 2,756 daily bars; SOL: 2,130 daily bars from August 2020 listing).
  - Out-of-sample test window: July 23, 2020 through July 17, 2026 (2,189 test days across 35 walk-forward folds for BTC and ETH; 1,748 test days across 28 folds for SOL).
- **Source Quality:** High-quality computational econometrics and empirical finance codebase from ETH Zürich. Implements strictly leak-free expanding-window walk-forward validation with a 5-day post-train embargo, nested-model Clark-West tests adjusting for estimation noise under the martingale null, Benjamini-Hochberg (FDR) and Holm-Bonferroni (FWER) multiple-testing adjustments across 18 model-asset-horizon combinations, realistic 17 bps per-side fee and slippage modeling, Pesaran-Timmermann directional timing tests, and Deflated Sharpe Ratios (DSR).

## Economic mechanism

### Source-reported

Cryptocurrency return predictability literature is rife with exaggerated claims driven by lookahead leakage, unpurged cross-validation, selection bias across hyperparameter grids, ignoring transaction frictions, and relying on standard $t$-tests or Diebold-Mariano tests against nested nulls. 

Under the efficient market hypothesis in its weak form, log prices follow a martingale difference sequence where the optimal out-of-sample point forecast under squared error loss is the prevailing price (the zero return null $\hat{y}_{t+h|t} = 0$). Standard regression models (e.g., Ridge, Elastic Net) and non-linear learners (Gradient Boosted Trees) estimate conditional expectations $E[y_{t+h} \mid X_t]$. However:
1. **The Nested-Model Bias in Mean Squared Error:** Because linear models nest the martingale null, when the null of no predictability is true, the larger model estimates parameters that are purely noise. In finite samples, this estimation noise inflates the out-of-sample mean squared prediction error (MSPE) of the larger model relative to the null ($MSPE_1 > MSPE_0$). A standard Diebold-Mariano (1995) test is severely undersized and biased toward failing to reject no predictability. The Clark and West (2007) test explicitly corrects for this upward shift in sample MSPE by computing:
   $$f_{t+h} = (y_{t+h} - \hat{y}_{0,t+h})^2 - \left[ (y_{t+h} - \hat{y}_{1,t+h})^2 - (\hat{y}_{0,t+h} - \hat{y}_{1,t+h})^2 \right]$$
   and testing whether $E[f_{t+h}] > 0$ via a one-sided $t$-statistic.
2. **Economic vs. Statistical Divergence:** A model may exhibit a positive Clark-West test statistic (indicating weak statistical predictability) yet fail to produce positive economic value once realistic transaction costs (taker fees, half-spread, market impact) are incurred. Conversely, an overfitted model may accidentally harvest a massive drift or market run in backtests (producing an attractive gross Sharpe ratio), yet possess negative out-of-sample explanatory power ($R^2_{OS} < 0$) and fail directional market-timing tests (Pesaran and Timmermann, 1992).

### Research interpretation

This research serves as a critical **methodological audit and falsification benchmark** for cryptocurrency alpha claims:

1. **Shrinkage as the Sole Resilient Predictor:** Across 18 machine-learning configurations, only heavily regularized linear models (Ridge regression with $\alpha=1.0$ and Elastic Net with $\alpha=10^{-3}, \rho=0.5$) applied to BTC at the 1-day horizon exhibit statistically significant out-of-sample predictability that survives multiple testing at a 5% False Discovery Rate (FDR). Non-linear models (XGBoost / GBM) fail multiple-testing corrections across all evaluated assets and horizons.
2. **The "Economic Winner" Illusion:** The apparent top-performing trading models by annualized net Sharpe ratio (GBM on ETH 1d with Sharpe 0.91; GBM on ETH 7d with Sharpe 0.92) are statistical illusions. Both exhibit negative out-of-sample $R^2$ ($-0.0768$ and $-0.0635$), fail Clark-West multiple-testing adjustments ($p_{adj} \ge 0.192$), fail Pesaran-Timmermann directional timing ($p \ge 0.354$), and produce Sharpe ratios that are statistically indistinguishable from a passive Buy-and-Hold allocation on ETH (Sharpe 0.80).
3. **Turnover Friction Kills Weak Linear Predictability:** While Ridge and Elastic Net demonstrate genuine statistical predictability on BTC 1-day (Clark-West $p = 0.004$ and $p = 0.005$, surviving Benjamini-Hochberg at $p_{adj} = 0.046$), their net annualized Sharpe ratios after 17 bps execution cost are depressed to 0.51 and 0.33, with extreme maximum drawdowns ($-65.69\%$ and $-74.28\%$). Their 95% bootstrap confidence intervals heavily overlap zero ($[-0.18, +1.23]$ for Ridge; $[-0.35, +1.02]$ for Elastic Net), showing that converting marginal statistical predictability into viable standalone trading alpha is barred by execution turnover.

## Signal

- **Target Definition:** Forward log return over horizon $h \in \{1, 7\}$ calendar days:
  $$y_t^{(h)} = \log\left(\frac{C_{t+h}}{C_t}\right)$$
- **Feature Set (12 Scale-Free Indicators):** All features are strictly backward-looking transformations of past daily OHLCV bars:
  1. `ret_1`: 1-day log return $\log(C_t / C_{t-1})$
  2. `ret_5`: 5-day log return $\log(C_t / C_{t-5})$
  3. `ret_10`: 10-day log return $\log(C_t / C_{t-10})$
  4. `ret_21`: 21-day log return $\log(C_t / C_{t-21})$
  5. `vol_10`: 10-day annualized rolling volatility $\text{std}(r_{t-9 \dots t}) \times \sqrt{365}$
  6. `vol_21`: 21-day annualized rolling volatility $\text{std}(r_{t-20 \dots t}) \times \sqrt{365}$
  7. `rsi_14`: 14-day Relative Strength Index, scaled by $1/100$ into $[0, 1]$
  8. `macd_hist`: Moving Average Convergence Divergence histogram (fast EMA 12, slow EMA 26, signal EMA 9), normalized by closing price $C_t$
  9. `sma_ratio_7_21`: Simple Moving Average ratio $\text{SMA}(C_t, 7) / \text{SMA}(C_t, 21) - 1$
  10. `dist_sma_50`: Normalized distance to 50-day moving average $C_t / \text{SMA}(C_t, 50) - 1$
  11. `range_14`: 14-day normalized True Range $\text{ATR}(14) / C_t$
  12. `volume_z_21`: 21-day rolling z-score of trade volume $(V_t - \mu_V) / \sigma_V$
- **Feature Preprocessing & Leak Prevention:**
  - Within each walk-forward training fold, feature columns are standardized to zero mean and unit variance.
  - Test fold features are transformed strictly using the *training fold's* mean and standard deviation:
    $$X_{\text{test}}^{\text{norm}} = \frac{X_{\text{test}} - \hat{\mu}_{\text{train}}}{\hat{\sigma}_{\text{train}}}$$
- **Walk-Forward Cross-Validation Design:**
  - **Window Type:** Expanding window.
  - **Minimum Training Length:** 504 calendar days (~2 years of daily observations).
  - **Test Block Length:** 63 calendar days (~1 quarter).
  - **Embargo Window:** 5 calendar days dropped between the end of the training set and the start of the test block to completely purge target-overlap and autoregressive leakage.
  - **Number of Folds:** 35 sequential folds for BTC and ETH (evaluating 2,189 days out-of-sample from 2020-07-23 to 2026-07-17); 28 sequential folds for SOL (evaluating 1,748 days out-of-sample from 2021-10-08 to 2026-07-17).
- **Candidate Forecasting Models:**
  1. `random_walk` (Martingale Null): $\hat{y}_{t+h|t} = 0$.
  2. `historical_mean` (Unconditional Drift Null): $\hat{y}_{t+h|t} = \frac{1}{T_{\text{train}}} \sum_{s=1}^{T_{\text{train}}} y_s^{(h)}$.
  3. `ar1`: Univariate OLS autoregression on the 1-day lagged return $y_t^{(1)}$.
  4. `ridge`: L2-penalized linear regression with penalty $\alpha = 1.0$, estimated via closed-form SVD.
  5. `elastic_net`: Combined L1/L2 penalized regression with $\alpha = 10^{-3}$ and L1 ratio $\rho = 0.5$, solved via coordinate descent.
  6. `gbm`: XGBoost regressor with `max_depth = 3`, `learning_rate = 0.03`, `n_estimators = 100`, `subsample = 0.8`, `colsample_bytree = 0.8`, and random state fixed at 42.

## Required data

- **Universe:** Liquid major crypto spot pairs: BTC/USDT, ETH/USDT, SOL/USDT.
- **Venue:** Binance spot exchange (downloaded via ccxt / Binance public archive).
- **Market Type:** Spot cash crypto (also applicable to perpetual futures).
- **Timeframe:** Daily OHLCV bars (timestamped at 00:00:00 UTC).
- **Sample Range:** January 1, 2019 to July 18, 2026 (7.5 years continuous).
- **Fields:** Open, High, Low, Close, Volume.
- **Missing Data Handling:** Zero forward filling permitted; datasets are verified continuous with zero missing daily timestamps.

## Execution assumptions

- **Position Generation:** Directional sign allocation:
  $$w_t = \text{sign}(\hat{y}_t) \in \{-1, +1\}$$
  (Long if model forecasts positive forward return, Short if model forecasts negative forward return). Alternatively evaluated in long-only mode ($w_t = \mathbb{I}(\hat{y}_t > 0)$).
- **Execution Cadence:** Non-overlapping $h$-day holding intervals ($t, t+h, t+2h, \dots$). Positions are established at the close of day $t$ and liquidated/rebalanced at the close of day $t+h$.
- **Transaction Cost Structure (17 bps Per Side):**
  - Exchange taker fee: 10 bps (0.10%, matching Binance VIP0 standard spot/perpetual taker schedule).
  - Execution slippage: 5 bps (0.05%).
  - Half-spread: 2 bps (0.02%).
  - Total round-turn cost: 34 bps (0.34%).
  - Turnover penalty per rebalance:
    $$\Delta \text{Cost}_t = c \cdot |w_t - w_{t-h}|, \quad c = 0.0017$$
- **Borrow & Short Constraints:** Evaluated assuming symmetric two-sided margin/perpetual execution with zero explicit borrow fee (source-evaluated under perpetual swap mechanics where shorting carries no special borrow rate aside from funding rate parity).
- **Operational Execution Default:** `research-proposed`: Orders executed at 00:00:00 UTC using market/taker orders on Binance or Hyperliquid perpetual contracts.

## Evidence

### Source-reported

All metrics below are transcribed verbatim from the out-of-sample backtests and statistical tests reported in Mehmet Demir Guven (2026, `reports/results.md` and `reports/results.csv`):

#### 1. Statistical Predictability & Nested Model Tests Across 18 ML Settings

Evaluated over the full out-of-sample period (2020-07-23 to 2026-07-17, 2,189 days for BTC/ETH; 1,748 days for SOL). 
$R^2_{OS} = 1 - \frac{\sum (y - \hat{y})^2}{\sum (y - 0)^2}$. Clark-West (CW) test against Random Walk null; Diebold-Mariano (DM) test against Random Walk null; Holm-Bonferroni (FWER) and Benjamini-Hochberg (FDR) adjusted $p$-values across all 18 configurations:

| Asset | Horizon ($h$) | Model | Out-of-Sample $R^2$ ($R^2_{OS}$) | Clark-West $t$-stat | CW $p$-value | CW Holm Adj $p$ | CW BH Adj $p$ | DM $p$-value |
|:---|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **BTC** | **1d** | **Ridge** | **-0.0079** | **+2.62** | **0.0044** | **0.079** | **0.046\*** | 0.941 |
| **BTC** | **1d** | **Elastic Net** | **+0.0031** | **+2.57** | **0.0051** | **0.086** | **0.046\*** | 0.323 |
| BTC | 1d | GBM | -0.0407 | +1.77 | 0.0384 | 0.537 | 0.173 | 0.999 |
| BTC | 7d | Ridge | -0.0163 | +0.66 | 0.2546 | 1.000 | 0.458 | 0.924 |
| BTC | 7d | Elastic Net | -0.0125 | +0.81 | 0.2082 | 1.000 | 0.416 | 0.892 |
| BTC | 7d | GBM | -0.0722 | +0.55 | 0.2905 | 1.000 | 0.475 | 0.985 |
| ETH | 1d | Ridge | -0.0163 | +1.59 | 0.0558 | 0.726 | 0.201 | 0.989 |
| ETH | 1d | Elastic Net | -0.0055 | +1.98 | 0.0240 | 0.360 | 0.144 | 0.803 |
| ETH | 1d | GBM | -0.0768 | +1.43 | 0.0768 | 0.845 | 0.230 | 1.000 |
| ETH | 7d | Ridge | -0.0152 | +0.61 | 0.2694 | 1.000 | 0.462 | 0.906 |
| ETH | 7d | Elastic Net | -0.0142 | +0.55 | 0.2917 | 1.000 | 0.475 | 0.887 |
| ETH | 7d | GBM | -0.0635 | +0.76 | 0.2248 | 1.000 | 0.426 | 0.981 |
| SOL | 1d | Ridge | -0.0094 | +1.11 | 0.1332 | 1.000 | 0.342 | 0.852 |
| SOL | 1d | Elastic Net | -0.0042 | +1.47 | 0.0706 | 0.845 | 0.230 | 0.697 |
| SOL | 1d | GBM | -0.0558 | +1.03 | 0.1506 | 1.000 | 0.354 | 0.999 |
| SOL | 7d | Ridge | -0.0163 | +1.86 | 0.0315 | 0.472 | 0.158 | 0.908 |
| SOL | 7d | Elastic Net | -0.0069 | +1.52 | 0.0645 | 0.838 | 0.230 | 0.761 |
| SOL | 7d | GBM | -0.0883 | +0.89 | 0.1873 | 1.000 | 0.399 | 0.992 |

**Key Statistical Findings:**
- Under the standard Diebold-Mariano test, **0 of 18 ML settings** beat the random walk on squared error loss ($p < 0.05$). Seven models are statistically significantly *worse* than random walk ($p > 0.95$).
- Under the Clark-West nested model test, **5 settings** reject the no-predictability null at unadjusted $p < 0.05$.
- Controlling for Family-Wise Error Rate (FWER) via Holm-Bonferroni, **0 of 18 settings survive**.
- Controlling for False Discovery Rate (FDR) via Benjamini-Hochberg at $q = 0.05$, **exactly 2 settings survive**: Ridge BTC 1d ($p_{\text{adj}} = 0.046$) and Elastic Net BTC 1d ($p_{\text{adj}} = 0.046$).

#### 2. Directional Accuracy & Market Timing (Pesaran-Timmermann Test)

Directional accuracy (fraction of times $\text{sign}(\hat{y}) = \text{sign}(y)$) and Pesaran-Timmermann (PT) test for non-trivial sign-timing skill:

| Asset | Horizon | Model | Directional Accuracy | PT $z$-stat | PT $p$-value |
|:---|:---:|:---|:---:|:---:|:---:|
| **BTC** | **1d** | **Ridge** | **50.6%** | **-0.28** | **0.609** |
| **BTC** | **1d** | **Elastic Net** | **49.8%** | **-0.86** | **0.806** |
| BTC | 1d | GBM | 47.9% | -1.97 | 0.975 |
| ETH | 1d | Ridge | 50.8% | +0.47 | 0.318 |
| ETH | 1d | Elastic Net | 50.4% | +0.28 | 0.391 |
| ETH | 1d | GBM | 49.6% | -0.37 | 0.646 |
| SOL | 1d | Ridge | 50.2% | +0.07 | 0.472 |
| SOL | 1d | Elastic Net | 50.3% | +0.08 | 0.468 |
| SOL | 1d | GBM | 48.7% | -1.13 | 0.871 |

**Key Directional Finding:**
- **Zero of the 18 settings exhibit statistically significant market-timing skill** ($p < 0.05$). Directional hit rates hover tightly between 47.9% and 53.6%, demonstrating that statistical predictability detected by Clark-West is driven by magnitude sizing or asymmetry in extreme states rather than consistent sign classification.

#### 3. Economic Trading Performance (Net of 17 bps Execution Costs)

Full out-of-sample backtest metrics for directional strategies ($w_t = \text{sign}(\hat{y}_t)$), comparing ML models to the unconditional Historical Mean drift null and passive Buy-and-Hold:

| Asset | Horizon | Model | Net Annualized Return | Net Sharpe Ratio | 95% Bootstrap CI | Max Drawdown | Trades / Changes | Deflated Sharpe Ratio (DSR) | Probabilistic Sharpe Ratio (PSR) |
|:---|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **BTC** | **1d** | **Ridge** | **+23.44%** | **0.51** | **[-0.18, 1.23]** | **-65.69%** | 496 | 0.63 | 0.89 |
| **BTC** | **1d** | **Elastic Net** | **+12.69%** | **0.33** | **[-0.35, 1.02]** | **-74.28%** | 539 | 0.45 | 0.79 |
| BTC | 1d | GBM | -2.96% | 0.04 | [-0.64, 0.73] | -84.97% | 592 | 0.16 | 0.54 |
| BTC | 1d | Hist Mean | +27.23% | 0.58 | [-0.10, 1.30] | -76.62% | 0 | — | 0.93 |
| BTC | Buy&Hold | Benchmark | +27.23% | 0.58 | [-0.10, 1.30] | -76.62% | 0 | — | 0.93 |
| ETH | 1d | Ridge | +16.03% | 0.33 | [-0.35, 1.03] | -79.79% | 517 | 0.45 | 0.79 |
| ETH | 1d | Elastic Net | +2.70% | 0.11 | [-0.56, 0.80] | -84.34% | 520 | 0.22 | 0.61 |
| ETH | 1d | GBM | +55.06% | 0.91 | [+0.22, 1.63] | -73.34% | 526 | 0.90 | 0.99 |
| ETH | Buy&Hold | Benchmark | +46.85% | 0.80 | [+0.10, 1.54] | -81.56% | 0 | — | 0.99 |
| ETH | 7d | Ridge | +22.86% | 0.44 | [-0.27, 1.15] | -75.98% | 85 | 0.56 | 0.85 |
| ETH | 7d | Elastic Net | +19.34% | 0.39 | [-0.31, 1.12] | -79.62% | 89 | 0.51 | 0.82 |
| ETH | 7d | GBM | +56.91% | 0.92 | [+0.25, 1.66] | -64.71% | 90 | 0.91 | 0.99 |
| SOL | 1d | Ridge | +4.94% | 0.15 | [-0.56, 0.89] | -92.93% | 409 | 0.26 | 0.65 |
| SOL | 1d | Elastic Net | +10.22% | 0.22 | [-0.48, 0.95] | -91.24% | 408 | 0.33 | 0.71 |
| SOL | 1d | GBM | -21.46% | -0.19 | [-0.91, 0.54] | -97.05% | 425 | 0.05 | 0.33 |
| SOL | 7d | Ridge | +22.06% | 0.30 | [-0.41, 1.05] | -93.89% | 73 | 0.42 | 0.76 |
| SOL | 7d | Elastic Net | +22.06% | 0.30 | [-0.41, 1.05] | -93.89% | 73 | 0.42 | 0.76 |
| SOL | 7d | GBM | +45.83% | 0.55 | [-0.17, 1.34] | -92.20% | 68 | 0.67 | 0.92 |
| SOL | Buy&Hold | Benchmark | +38.64% | 0.49 | [-0.21, 1.25] | -95.89% | 0 | — | 0.88 |

#### 4. The Economic vs. Statistical Divergence Audit

- **The Statistical Winners (Ridge & Elastic Net on BTC 1d):**
  - Reject the null of no predictability under Clark-West ($p = 0.0044$ and $p = 0.0051$; Benjamini-Hochberg $p_{\text{adj}} = 0.046$).
  - Yet generate net Sharpe ratios of only **0.51** and **0.33**, *underperforming* passive Buy-and-Hold BTC (Sharpe **0.58**) and suffering maximum drawdowns of $-65.69\%$ and $-74.28\%$.
  - 95% bootstrap confidence intervals for Sharpe span zero ($[-0.18, 1.23]$ and $[-0.35, 1.02]$).
- **The Economic "Winners" (GBM on ETH 1d and 7d):**
  - Exhibit eye-catching net Sharpe ratios of **0.91** and **0.92** (net returns $+55.06\%$ and $+56.91\%$).
  - However, both have heavily negative out-of-sample $R^2$ ($-0.0768$ and $-0.0635$).
  - Both fail Clark-West multiple-testing adjustments ($p_{\text{adj}} = 0.230$ and $p_{\text{adj}} = 0.426$).
  - Both fail Pesaran-Timmermann directional timing ($p = 0.646$).
  - Both are statistically indistinguishable from Buy-and-Hold ETH (Sharpe 0.80) because ETH experienced an enormous secular drift during the out-of-sample window, and the models simply stayed net long during the bull trend.

#### 5. Sensitivity to Execution Timing (Schedule Phase Dependence)

For the 7-day rebalancing horizon, shifting the anchor day across the 7 possible starting offsets (offset 0 through 6) reveals severe phase sensitivity:
- ETH 7-day GBM net Sharpe varies from **0.49** to **1.05** depending entirely on which day of the week positions are rolled.
- SOL 7-day Ridge net Sharpe varies from **-0.08** to **+0.52**.
- This proves that single-phase multi-day rebalance backtests in crypto are heavily confounded by day-of-week calendar noise.

#### 6. Transaction Cost Sensitivity & Break-Even Frictions

Testing net performance across a cost grid from 0 bps to 50 bps per side:
- **Ridge BTC 1d:** Gross Sharpe = 0.88; Break-even one-way transaction cost = **41 bps**.
- **Elastic Net BTC 1d:** Gross Sharpe = 0.72; Break-even one-way transaction cost = **28 bps**.
- At typical retail taker fees (20–40 bps plus slippage), all net alpha across all regularized models drops to zero or turns negative.

### Independently reproduced

Not independently reproduced. All results cited are third-party empirical findings from the ETH Zürich codebase repository.

### Negative evidence

- **Pervasive Out-of-Sample MSPE Degradation:** Across all 18 machine learning setups, 17 exhibit negative out-of-sample $R^2$ (down to $-0.0883$). Only Elastic Net on BTC 1d manages a marginally positive $R^2_{OS}$ of $+0.0031$ (+0.31%). The ML models generate larger squared forecast errors than simply predicting zero return.
- **Complete Failure of Non-Linear Learners:** XGBoost (GBM) performs worst across all statistical tests, generating $R^2_{OS}$ between $-0.0407$ and $-0.0883$ and Clark-West adjusted $p$-values between $0.173$ and $0.475$. Tree-based partitioning catastrophically overfits noisy crypto return histories despite shallow trees (`max_depth = 3`) and heavy regularization.
- **Absence of Sign Predictability:** Not a single evaluated model demonstrates statistically significant directional sign accuracy under the Pesaran-Timmermann test ($p \ge 0.318$ across all assets).
- **Catastrophic Drawdowns:** Every single ML model produces maximum drawdowns exceeding $-64\%$ (up to $-97.05\%$ on SOL), offering virtually zero downside risk protection compared to passive spot holding.
- **Failure Under Conservative FWER Control:** If an allocator insists on controlling Family-Wise Error Rate (FWER) across the 18 model trials via Holm-Bonferroni, zero models survive at the 5% level ($p_{\text{adj}} \ge 0.079$).

## Falsification plan

1. **Transaction Cost Stress Test on Microstructure Data:**
   - Run the Ridge BTC 1-day model with realistic tick-level execution slippage and exchange fees on Binance Futures or Hyperliquid.
   - `research-defined falsification threshold`: If the net annualized Sharpe ratio drops below 0.30 or if one-way transaction costs exceed 25 bps, reject the tradeability of daily regularized linear models.
2. **True Out-of-Sample Forward Rolling Walk (Post-July 2026):**
   - Evaluate the Ridge and Elastic Net BTC 1-day models strictly on forward unseen data generated after July 18, 2026 for a minimum of 180 calendar days.
   - `research-defined falsification threshold`: If the out-of-sample Clark-West test statistic on post-July 2026 returns fails to achieve $t > 1.645$ ($p < 0.05$) or if the cumulative net return is negative, falsify the hypothesis that short-horizon BTC return predictability is stationary.
3. **Multi-Start Phase Averaging (Ensemble Roll Schedule):**
   - Eliminate schedule phase dependence by deploying an ensemble that allocates $1/h$ capital to each of the $h$ interleaved rebalancing schedules ($s \in \{0, 1, \dots, h-1\}$).
   - `research-defined falsification threshold`: If the phase-averaged 7-day model Sharpe ratio drops below 0.35 across BTC, ETH, and SOL, reject all 7-day horizon predictability claims as calendar noise artifacts.
4. **Perpetual Funding Rate Drag Audit:**
   - Incorporate actual historical 8-hour perpetual swap funding rates into the short leg of the directional unit bets ($w_t = \text{sign}(\hat{y}_t)$).
   - `research-defined falsification threshold`: If net funding payments erode more than 30% of gross profits, or if net Sharpe drops below 0.25, reject standalone directional long/short implementation on perpetual swaps.
5. **Multi-Asset Panel Cross-Sectional Null:**
   - Evaluate the models on an expanded panel of top 30 liquid altcoins rather than the isolated trio (BTC, ETH, SOL).
   - `research-defined falsification threshold`: If the median Clark-West $p$-value across the 30 altcoins exceeds 0.20 or if the Benjamini-Hochberg FDR at 5% discovers zero surviving models, conclude that return predictability is completely absent outside of BTC.

## Crypto portability

- **Portability Status:** Native cryptocurrency research.
- **Primary Source Asset Class:** Cryptocurrency spot/perpetuals (BTC, ETH, SOL).
- **Execution Viability:**
  - The strategy is native to crypto, but the source empirical findings confirm that **standalone directional trading based on daily ML return forecasts is commercially non-viable** once realistic exchange taker fees (10 bps) and slippage (5 bps) are accounted for.
  - To become viable, the weak statistical predictability identified in Ridge/Elastic Net must be ported into **execution scheduling algorithms (e.g., TWAP/VWAP execution alpha)** or **cross-sectional ranking overlays** where turnover is naturally amortized, rather than traded as a naive discrete long/short switcher.

## Limitations

- **Small Asset Universe:** Empirical evaluations are confined to BTC, ETH, and SOL; smaller-cap tokens or altcoin cross-sections were not evaluated.
- **Discrete Daily Sampling:** The paper relies on 00:00:00 UTC daily closing bars; intraday dynamics (e.g., hourly funding cycles, US/Asian market open liquidity shifts) are unmodeled.
- **Linear Model Dominance via Attrition:** Ridge and Elastic Net survived multiple testing primarily because their parameter estimates are aggressively shrunk toward zero, preventing explosive MSPE inflation rather than capturing complex predictive structures.
- **High Drawdown Profile:** Max drawdowns between $-65\%$ and $-97\%$ make unhedged, un-levered deployment psychologically and commercially impossible for institutional mandates.
- **Not Independently Reproduced:** Metrics are documented directly from Guven (2026) and have not been executed on internal proprietary backtesters.

## Implementation status

`not-implemented`. This record is a research capture, methodological benchmark, and falsification audit. No code has been deployed to production execution engines (NautilusTrader, PyBroker, Hummingbot), and no live, testnet, or paper trading is approved.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- A strategy research record being added to this repository serves as a permanent research artifact and audit trail. It does not constitute approval for live risk deployment, capital allocation, or automated trading.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` (canonical strategy research specification)
- `[[quant/crypto-cross-sectional-momentum-delay-and-lookback-2026-09-02]]` (cross-sectional momentum and horizon decay in crypto)
- `[[quant/crypto-bitcoin-cvar-risk-aware-q-learning-adaptive-controller-2026-09-02]]` (reinforcement learning risk controls in crypto)
- `[[quant/expected-shortfall-factor-model-common-tail-loss-severity-2026-09-11]]` (latent tail loss severity and cross-sectional asset pricing)
- `[[quant/crypto-cross-sectional-extreme-downside-risk-var-2026-09-01]]` (extreme downside risk pricing in cryptocurrency assets)

## Sources

1. Guven, Mehmet Demir. "Are Short-Horizon Cryptocurrency Returns Predictable Out of Sample? A purged walk-forward study with nested-model tests, transaction costs, and multiple-testing control." Department of Computer Science, ETH Zürich, 2026. Codebase repository: [https://github.com/ITheClixs/crypto-return-predictability](https://github.com/ITheClixs/crypto-return-predictability). Immutable commit SHA: `83881c7cd01ce45aca94dc7f050ccf22685a4a44`.
2. Out-of-Sample Performance and Statistical Tests: `reports/results.md` and `reports/results.csv` in same repository. Out-of-sample test window July 2020 to July 2026 (2,189 days for BTC/ETH, 1,748 days for SOL). 18 ML settings evaluated.
3. Nested Model Econometric Testing: Clark, Todd E., and Kenneth D. West. "Approximately normal tests for equal predictive accuracy in nested models." *Journal of Econometrics* 138, no. 1 (2007): 291-311.
4. Multiple Testing Frameworks: Benjamini, Yoav, and Yosef Hochberg. "Controlling the false discovery rate: a practical and powerful approach to multiple testing." *Journal of the Royal Statistical Society: Series B (Methodological)* 57, no. 1 (1995): 289-300; Holm, Sture. "A simple sequentially rejective multiple test procedure." *Scandinavian Journal of Statistics* (1979): 65-70.
5. Backtest Overfitting & Deflated Sharpe Ratio: Bailey, David H., and Marcos López de Prado. "The Deflated Sharpe Ratio: correcting for selection bias, backtest overfitting, and non-normality." *Journal of Portfolio Management* 40, no. 5 (2014): 94-107.
