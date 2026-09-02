---
schema: strategy-research-record-v1
title: "Same-Day Open-to-Close Directional Prediction on SPY: Walk-Forward Tree Ensembles, Threshold Conditioning, and Sample-Support Degradation"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equity
  - etf
  - spy
  - machine-learning
  - xgboost
  - random-forest
  - logistic-regression
  - walk-forward
  - threshold-conditioning
  - intraday-direction
status: research-only
confidence: medium
source_as_of: 2026-08-30
sources:
  - "Alex Chen, 'A Statistical-Finance Benchmark for Same-Day Directional Stock Prediction: Walk-Forward Evidence from SPY', arXiv:2608.26106v1 [q-fin.ST, cs.LG], August 2026. Stable URL: https://arxiv.org/abs/2608.26106. Full text HTML: https://arxiv.org/html/2608.26106v1. Supporting archive: https://osf.io/6thqk"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Same-Day Open-to-Close Directional Prediction on SPY: Walk-Forward Tree Ensembles, Threshold Conditioning, and Sample-Support Degradation

## Provenance

- **Primary Source:** Alex Chen, *"A Statistical-Finance Benchmark for Same-Day Directional Stock Prediction: Walk-Forward Evidence from SPY"*, arXiv preprint `arXiv:2608.26106v1 [q-fin.ST, cs.LG]`, August 2026.
- **Identifier:** `arXiv:2608.26106v1`
- **Stable URL:** [https://arxiv.org/abs/2608.26106](https://arxiv.org/abs/2608.26106)
- **Full Text HTML:** [https://arxiv.org/html/2608.26106v1](https://arxiv.org/html/2608.26106v1)
- **Supporting Data/Code Archive:** Open Science Framework (OSF) repository: [https://osf.io/6thqk](https://osf.io/6thqk).
- **Core Dataset:** Daily SPDR S&P 500 ETF (SPY) OHLC price history from Yahoo Finance, spanning February 1, 1993 through March 15, 2024 (7,837 trading days). Auxiliary cross-sectional screen covers 541 U.S. equities over identical walk-forward specifications.

## Economic mechanism

### Source-reported

The paper investigates whether daily equity price direction from market open to market close can be statistically predicted using only information available at the opening bell. The economic intuition is that the opening price embeds overnight information accumulation, global market sentiment, and order imbalances formed during pre-market auctions. When coupled with recent lagged price levels ($t-1$ and $t-2$), this opening observation reflects whether the open represents an overreaction (mean reversion) or an initial price discovery jump that persists through the cash session (drift continuation). 

The author emphasizes that while tree ensembles extract non-linear interactions between opening levels and recent ranges, direct classification models (Logistic Regression) capture sign transitions more reliably than regression-derived direction, and threshold conditioning isolates higher-conviction moves at the cost of rapid sample size depletion.

### Research interpretation

The underlying alpha hypothesis is an **intraday drift / initial-balance continuation hypothesis conditioned on overnight gap realization**:

1. **Information Assimilation vs. Noise:** The opening price $p_1^{(t)}$ relative to previous close $p_2^{(t-1)}$ and lagged open $p_1^{(t-1)}$ creates an anchoring reference. If price moves strongly at the open in a direction supported by recent multi-day momentum, institutional rebalancing and liquidity seekers following execution algorithms (e.g., VWAP/TWAP) create persistent one-way flow across the regular trading hours (RTH) session.
2. **Threshold Conviction Filtering:** Small predicted moves ($\delta_t < 0.5\%$) represent microstructure noise and bid-ask bounce where directional accuracy hovers near chance ($58.4\%$). Large predicted moves ($\delta_t \ge 1.0\%$) reflect substantial regime shifts or news catalysts where momentum persistence is higher ($72.7\%$).
3. **Statistical vs. Economic Friction Reality:** The source author rigorously separates statistical predictability from deployable economic alpha: although continuous regression tree models achieve high reported $R^2$ ($0.980$) and illustrative long/flat backtests post high gross returns, the edge is highly sensitive to the shrinkage of trade opportunities (from 799 days to 154 at $1.0\%$ threshold and only 3 at $3.5\%$) and execution slippage across market opens.

## Signal

### Formation timestamp

- **Observation Point:** Exactly at the market open ($t_{\text{open}} = 09:30$ US Eastern Time). The day-$t$ opening price $p_1^{(t)}$ is observed and immediately appended to the lagged feature vector.
- **Tradability:** Actionable immediately after the open (e.g., $09:30:05$–$09:31:00$ ET) for execution over the regular cash session.
- **Horizon:** Intraday hold; exit occurs at or near the official cash close ($t_{\text{close}} = 16:00$ US Eastern Time).

### Lookback and Feature Construction

For opening price series $p_1 = \text{open}$ and target price series $p_2 \in \{\text{high}, \text{low}, \text{close}\}$ (with primary focus on $p_2 = \text{close}$):

The feature vector at day $t$ is strictly 5-dimensional:
$$\mathbf{x}^{(t)} = \big[p_1^{(t-2)},\; p_2^{(t-2)},\; p_1^{(t-1)},\; p_2^{(t-1)},\; p_1^{(t)}\big]$$

- No day-$t$ high, low, or close is included in $\mathbf{x}^{(t)}$ (strict look-ahead exclusion by construction).
- Sampling: 1-day step, expanding historical window up to $t-1$.

### Target and Decision Logic

The primary target is the same-day close price:
$$y^{(t)} = p_2^{(t)} = \text{close}^{(t)}$$

1. **Continuous Price Forecast:** The regression model (XGBoost or Random Forest) generates point estimate $\hat{y}_t = \hat{p}_2^{(t)}$.
2. **Directional Extraction:**
   $$\text{Direction}_t = \begin{cases} +1 \; (\text{Up/Long}) & \text{if } \hat{y}_t \ge y_{t-1} \\ -1 \; (\text{Down/Flat or Short}) & \text{if } \hat{y}_t < y_{t-1} \end{cases}$$
3. **Threshold-Conditioned Filter:**
   Calculate predicted absolute percentage move:
   $$\delta_t = \frac{|\hat{y}_t - y_{t-1}|}{y_{t-1}} \times 100$$
   A trade is taken if and only if $\delta_t \ge \tau$, where $\tau \in [0.0\%, 3.5\%]$.
4. **Direct Classifier Variant:** Logistic Regression directly predicts the binary outcome $\mathbb{1}_{[y_t \ge y_{t-1}]}$ from $\mathbf{x}^{(t)}$.

### Exit and Holding Period

- **Holding Period:** Exactly one regular trading session (enter on open at $t$, exit on close at $t$).
- **No-trade Condition:** If $\delta_t < \tau$, position remains flat.
- **Overnight Risk:** Zero overnight inventory carry under the strict open-to-close specification.

### Parameters

- **Baseline XGBoost:** Objective `reg:squarederror`, default tree depth and shrinkage in stock pipeline.
- **Tuned XGBoost Evaluated:** 100 estimators, learning rate $\eta = 0.05$, max depth $= 6$, min child weight $= 4$, subsample $= 0.7$, colsample by tree $= 0.7$ (reported in Appendix A.2 as failing to outperform default XGBoost on directional accuracy).
- **Threshold Grid $\tau$:** Evaluated at $0.0\%, 0.5\%, 1.0\%, 1.5\%, 2.0\%, 2.5\%, 3.0\%, 3.5\%$.
- **Walk-Forward Split:** Expanding window; test period fixed at final 800 trading days (approximately April 2021 through March 2024).

## Required data

- **Instrument:** SPDR S&P 500 ETF Trust (SPY); cross-sectional screen evaluates 541 large/mid-cap U.S. equities.
- **Venue:** U.S. Equity Cash Market (NYSE Arca for SPY; primary listings on NYSE/NASDAQ for screen stocks).
- **Timeframe:** Daily bars (Open, High, Low, Close, Volume).
- **Fields Used in Signal:** Open ($p_1$), Close ($p_2$); High and Low are analyzed as auxiliary forecast targets.
- **Point-in-Time Integrity:** Expanding-window walk-forward; training set utilizes data strictly prior to day $t$ ($1 \dots t-1$); prediction made after day-$t$ open is posted.
- **Timestamp / Timezone:** US Eastern Time (America/New_York). 09:30 open, 16:00 close.
- **Missing Data Handling:** Standard exchange calendar; non-trading days omitted.

## Execution assumptions

- **Order Type:** Market-on-Open (MOO) or market order immediately following the 09:30 open print; Market-on-Close (MOC) order for cash-session exit at 16:00.
- **Fill Model:** Execution assumed at reported open and close prices in the primary benchmark.
- **Execution Cost Sensitivity (Appendix B.3):** Evaluated across fixed slippage/commission tiers: $0\text{ bps}$, $5\text{ bps}$, $10\text{ bps}$, and $20\text{ bps}$ round-trip.
- **Borrow / Shorting:** Illustrated primarily as long/flat. Shorting availability on SPY is frictionless, but auxiliary single-stock screen faces varying locate/borrow fees not modeled.
- **Latency Sensitivity:** Modest; signal computation on a 5-element vector requires $<1\text{ ms}$; orders can be routed within seconds of market open.

## Evidence

### Source-reported

All figures, statistical test values, confidence intervals, and metrics trace directly to Alex Chen (*arXiv:2608.26106v1*, Sections 3–5, Tables 1–6, 14–15):

#### 1. Main SPY Close-Target Benchmark (Last 800 Trading Days, Table 1)
- **Logistic Regression (Direct Classification):** Directional Accuracy $= 71.09\%$. (Strongest overall directional classifier).
- **Random Forest (Bagging Tree Ensemble):** MAPE $= 0.785\%$, Directional Accuracy $= 61.20\%$, Precision $= 66.77\%$, Recall $= 52.14\%$, F1 $= 58.56\%$.
- **XGBoost (Boosting Tree Ensemble):** MAPE $= 0.882\%$, Directional Accuracy $= 58.45\%$ (95% bootstrap CI: $[54.94\%, 62.08\%]$), Precision $= 65.94\%$, Recall $= 43.33\%$, F1 $= 52.30\%$.
- **LightGBM:** MAPE $= 1.275\%$, Directional Accuracy $= 52.82\%$, Precision $= 62.87\%$, Recall $= 25.00\%$, F1 $= 35.78\%$.
- **Naive Momentum Baseline:** Directional Accuracy $= 50.25\%$.
- **Naive Always-Up Baseline:** Directional Accuracy $= 52.57\%$.
- **Random Baseline:** Directional Accuracy $= 49.94\%$.

#### 2. Regression Fit Quality (Table 14)
- **XGBoost:** $\text{MSE} = 21.882$, $\text{RMSE} = 4.678$, $\text{MAE} = 3.737$, $R^2 = 0.980$.
- **Random Forest:** $\text{MSE} = 17.568$, $\text{RMSE} = 4.191$, $\text{MAE} = 3.307$, $R^2 = 0.984$.
- **Tuned XGBoost:** $\text{MSE} = 45.881$, $\text{RMSE} = 6.774$, $\text{MAE} = 5.661$, $\text{MAPE} = 1.318\%$, $R^2 = 0.957$ (shows hyperparameter tuning on complex trees degrades generalization).
- **LightGBM:** $\text{MSE} = 47.450$, $\text{RMSE} = 6.888$, $\text{MAE} = 5.483$, $R^2 = 0.956$.

#### 3. Threshold-Conditioned Accuracy & Sample Depletion (Table 2)
As the predicted move threshold $\tau$ increases, directional accuracy increases, but trade support collapses rapidly:
- $\tau = 0.0\%$: $N = 799$, Accuracy $= 58.4\%$
- $\tau = 0.5\%$: $N = 420$, Accuracy $= 61.9\%$
- $\tau = 1.0\%$: $N = 154$, Accuracy $= 72.7\%$
- $\tau = 1.5\%$: $N = 54$, Accuracy $= 79.6\%$
- $\tau = 2.0\%$: $N = 20$, Accuracy $= 90.0\%$
- $\tau = 2.5\%$: $N = 10$, Accuracy $= 90.0\%$
- $\tau = 3.0\%$: $N = 5$, Accuracy $= 100.0\%$
- $\tau = 3.5\%$: $N = 3$, Accuracy $= 100.0\%$

#### 4. Hypothesis Testing: XGBoost vs. Random Forest (Table 3)
- **Diebold–Mariano Test (Squared Forecast Errors):** Statistic $= 3.657$, $p < 0.001$. Statistically rejects equal predictive accuracy in favor of Random Forest for price regression.
- **McNemar Test (Paired Directional Misclassifications):** Statistic $= 3.150$, $p = 0.076$. Fails to reject equal directional classification ability at the $5\%$ significance level.

#### 5. Regime-Specific Subsamples (Table 8)
- **2007–2012 (Crisis):** $N_{\text{train}} = 1,056$, $N_{\text{test}} = 452$, $\text{MAPE} = 0.827\%$, Accuracy $= 60.98\%$.
- **2013–2019 (Bull):** $N_{\text{train}} = 1,232$, $N_{\text{test}} = 528$, $\text{MAPE} = 0.756\%$, Accuracy $= 55.60\%$.
- **2020–2023 (COVID):** $N_{\text{train}} = 629$, $N_{\text{test}} = 269$, $\text{MAPE} = 0.836\%$, Accuracy $= 65.30\%$.

#### 6. Execution-Illustrative Long/Flat Backtest (Table 15, Appendix B.3)
Evaluated on SPY over 300 executed trades (test sequence):
- **$0\text{ bps}$ cost:** Total Return $= 239.36\%$, Sharpe $= 3.456$, Max Drawdown $= 5.76\%$ (vs Buy & Hold Return $34.63\%$).
- **$5\text{ bps}$ cost:** Total Return $= 192.17\%$, Sharpe $= 3.043$, Max Drawdown $= 6.45\%$.
- **$10\text{ bps}$ cost:** Total Return $= 151.52\%$, Sharpe $= 2.626$, Max Drawdown $= 7.16\%$.
- **$20\text{ bps}$ cost:** Total Return $= 86.36\%$, Sharpe $= 1.785$, Max Drawdown $= 8.89\%$.

#### 7. Auxiliary Cross-Sectional Stock Screen (Table 9, Section 4.6)
Across 541 U.S. equities evaluated with threshold-accuracy Area Under Curve (AUC):
- **Close Target:** Median AUC across all stocks $= 350.50$ (IQR $[330.36, 367.58]$). Only 11 of 541 stocks achieved $\text{AUC} > 400$.
- **SPY Outlier Status:** SPY ranked 4th out of 541 stocks for close-target AUC ($\text{AUC} = 415.24$), behind only JNJ ($420.09$), WY ($417.78$), and PPG ($415.67$).

### Independently reproduced

Not independently reproduced. Findings are derived from arXiv:2608.26106v1 and its accompanying OSF experiment artifacts.

### Negative evidence

- **Regression vs. Classification Mismatch:** Predicting continuous price levels to derive direction produces inferior classification accuracy ($58.45\%$ for XGBoost, $61.20\%$ for RF) compared to direct binary classification ($71.09\%$ for Logistic Regression).
- **Hyperparameter Overfitting:** Attempting to tune XGBoost (depth 6, subsampling 0.7) doubled MSE ($45.881$ vs $21.882$) and worsened MAPE ($1.318\%$ vs $0.882\%$), illustrating that tree regularization can easily destroy delicate daily signals.
- **Support Collapse under Threshold Filtering:** Apparent win rates of $90\%–100\%$ are non-deployable statistical artefacts resting on tiny sample counts ($N = 20, 10, 5, 3$), precluding statistical significance.
- **Asset Selection Bias (SPY is an Outlier):** In the 541-stock universe screen, close-target predictability was poor for the vast majority of equities (median AUC 350.50). SPY ranked in the top 0.7% (4th of 541). Extrapolating SPY's same-day predictability to a general equity universe represents extreme favorable-case selection bias.
- **Regime Degradation in Steady Bull Markets:** Directional accuracy dropped to $55.60\%$ during 2013–2019, only slightly above the naive always-up baseline ($52.57\%$).

## Falsification plan

1. **Out-of-Sample Horizon Test (2024–2026):** Evaluate walk-forward performance on SPY from March 16, 2024 to September 2026. If directional accuracy drops below $52.5\%$ (the unconditional upward drift baseline), the hypothesis of persistent directional predictability is falsified.
2. **Cross-Sectional Non-Outlier Test:** Test the identical walk-forward model across a randomly selected 50-stock basket from the S&P 500 median AUC quantile ($330 \le \text{AUC} \le 365$). If average net return after 5 bps friction is non-positive, confirm that the edge is unique to broad index ETF liquidity dynamics rather than a general equity pricing phenomenon.
3. **Execution Delay Degradation Test:** Introduce simulated execution delays of 1, 5, 15, and 30 minutes after open (sampling price at 09:31, 09:35, 09:45, 10:00). If directional accuracy decays toward 50% within the first 15 minutes, the edge is purely an opening auction artifact rather than full-day drift.
4. **Permutation / Shuffled Open Test:** Randomly shuffle the day-$t$ opening price $p_1^{(t)}$ relative to lagged vector $[p_1^{(t-2)}, p_2^{(t-2)}, p_1^{(t-1)}, p_2^{(t-1)}]$. If the permuted feature set yields equivalent directional accuracy, falsify the claim that opening gap structure contains causal information.

## Crypto portability

**Adapted / Unproven.** The source paper explicitly investigates U.S. equities (SPY ETF) and notes that crypto data is outside its scope.

Porting same-day open-to-close directional prediction to cryptocurrency perpetual markets involves substantial structural differences:
- **Absence of Cash Open / Close Auctions:** Crypto trades 24/7/365 without an official NYSE 09:30 open or 16:00 close auction. An adapted strategy must define arbitrary session boundaries (e.g., UTC 00:00 to 24:00, or Asia/London/New York liquidity session cutoffs).
- **Perpetual Funding Rate Drag:** Holding positions across 8-hour funding timestamps (00:00, 08:00, 16:00 UTC) incurs funding payments that alter net directional payoff.
- **Continuous High-Frequency Volatility:** Crypto markets exhibit frequent intraday flash crashes and wick liquidations that violate the smooth open-to-close holding path assumed in daily bar benchmarks.
- **Microstructure Differences:** Liquid crypto perps (e.g., BTCUSDT, ETHUSDT) exhibit distinct order book dynamics, where aggressor flow imbalance and liquidation cascades dominate opening price discovery rather than institutional auction imbalances.

## Limitations

- **Single-Instrument Primary Focus:** Primary statistical hypothesis tests are conducted solely on SPY close.
- **No Realistic Slippage in Primary Results:** Primary benchmark assumes exact fills at open and close prints; opening bar spread and slippage on volatile days can exceed 5–10 bps.
- **Severe Support Decay:** The reported 90%+ accuracy figures are based on fewer than 20 observations out of 800 days.
- **Model Fragility:** Small changes in hyperparameters (tuning) degraded performance substantially.
- **Look-Back Horizon Limitation:** The 5-element feature vector ignores higher-order volatility dynamics, volume, and order-book state.

## Implementation status

`not-implemented`. No implementation in PyBroker, NautilusTrader, paper trading, testnet, or live environments has been conducted.

## Adoption boundary

`research-only`. This capture serves as a normalized research record and statistical benchmark. It does not constitute an approved trading strategy, does not guarantee profitability, and does not authorize deployment in paper, testnet, or live trading.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/tree-ensemble-tabular-financial-forecasting]]`
- `[[quant/intraday-momentum-gap-reversal-boundaries]]`

## Sources

1. Alex Chen, *"A Statistical-Finance Benchmark for Same-Day Directional Stock Prediction: Walk-Forward Evidence from SPY"*, arXiv preprint `arXiv:2608.26106v1 [q-fin.ST, cs.LG]`, August 2026. DOI: [10.48550/arXiv.2608.26106](https://doi.org/10.48550/arXiv.2608.26106). Stable URL: [https://arxiv.org/abs/2608.26106](https://arxiv.org/abs/2608.26106). Full text HTML: [https://arxiv.org/html/2608.26106v1](https://arxiv.org/html/2608.26106v1).
2. Supporting replication material and experiment scripts: Open Science Framework (OSF) archive: [https://osf.io/6thqk](https://osf.io/6thqk).
