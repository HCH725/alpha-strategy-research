---
schema: strategy-research-record-v1
title: "Long-Only Cryptocurrency Portfolio Allocation via Multi-Layer Perceptron Return-Rank Prediction and Exponential Weight Decay"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - machine-learning
  - cross-sectional
  - ranking
  - portfolio-management
status: research-only
confidence: medium
source_as_of: 2025-12-09
sources:
  - "https://arxiv.org/abs/2512.08124"
  - "https://doi.org/10.48550/arXiv.2512.08124"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The primary source evaluates annualized metrics using non-standard equity annualization conventions (scaling daily sums and standard deviations by sqrt(250) in Eq. 4-5 instead of compounding over 365 daily crypto trading days). Furthermore, universe construction selects the top 10 market cap coins as of 2023-11-01 (the end of the backtest sample), introducing an explicit survivorship and look-ahead conditioning bias."
---

# Long-Only Cryptocurrency Portfolio Allocation via Multi-Layer Perceptron Return-Rank Prediction and Exponential Weight Decay

## Provenance

- **Primary Source:** Zijiang Yang (Department of Computer Science and Engineering, New York University), *"Long-only cryptocurrency portfolio management by ranking the assets: a neural network approach"*, arXiv preprint `arXiv:2512.08124v1 [q-fin.PM]`, submitted December 9, 2025.
- **Canonical arXiv URL:** [https://arxiv.org/abs/2512.08124](https://arxiv.org/abs/2512.08124)
- **Canonical DOI:** [https://doi.org/10.48550/arXiv.2512.08124](https://doi.org/10.48550/arXiv.2512.08124)
- **Primary Source Inspection:** The full LaTeX source (`conference_101719.tex`) and associated figures were directly downloaded from arXiv source package `2512.08124.tar.gz` and audited. All mathematical formulations, feature derivations, network dimensions, parameters, baseline tables, and transaction cost sensitivity tables in this record trace directly to the primary LaTeX document.
- **Deduplication Check:** A repository-wide and Wiki Brain search confirmed no existing records referencing `2512.08124`, author Zijiang Yang, or the specific non-linear rank-power objective ($(rank(r_t))^n$) paired with exponential decay portfolio smoothing.

## Economic mechanism

### Source-reported

The author argues that forecasting absolute future returns ($r_t$) for individual cryptocurrencies in isolation is inherently noisy and difficult due to severe non-stationarity, extreme volatility (daily standard deviation reaching ~5%, with tail moves between -42% and +74%), and shifting market regimes. Traditional online portfolio selection algorithms typically fail across full market cycles:
1. **Follow-the-winner (momentum)** strategies (such as Cover's Universal Portfolio `UP` and Helmbold's Exponential Gradient `EG`) perform decently during bull markets but lag or overfit in choppy, stagnant regimes.
2. **Follow-the-loser (mean-reversion)** strategies (such as Anti-correlation, `CWMR`, `OLMAR`, `PAMR`, `RMR`) suffer catastrophic drawdowns (approaching -96%) in cryptocurrency markets because underperforming assets (e.g., EOS decaying from 1.0 down to 0.4) often experience structural abandonment rather than reverting to a historical mean.

Instead of predicting absolute price returns, the paper hypothesizes that **relative cross-sectional return rankings** contain cleaner, more learnable predictive structure. By predicting the ordinal rank of next-day returns across the asset basket and exponentiating the rank (e.g., $(rank(r_t))^2$), the model amplifies the relative capital allocation toward top-tier momentum leaders while dampening noise from middle-ranked assets. To prevent excessive transaction costs arising from frequent daily weight reallocations, an exponential decay filter is applied across consecutive portfolio weight vectors.

### Research interpretation

The underlying alpha mechanism is a **cross-sectional momentum amplification and risk-budgeting model**:
- **Cross-Sectional Interaction vs. Time-Series Modeling:** Rather than learning 10 separate univariate forecasting models, a single fully-connected Multi-Layer Perceptron (MLP) receives the concatenated features of all assets in the universe simultaneously. This architecture allows hidden neurons to capture cross-asset relative dispersion, market-wide trend alignment, and joint volatility shocks.
- **Non-Linear Rank-Power Objective:** Training against $(rank(r_t))^n$ with $n=2$ acts as an asymmetric utility transform. It penalizes misrankings at the extreme right tail (the strongest relative performers) more heavily than in the median, effectively steering capital toward high-conviction relative winners.
- **Turnover Damper:** Without execution smoothing, daily rank fluctuations induce severe rebalancing turnover that erodes alpha. The single-period memory decay filter acts as a low-pass filter on portfolio weights, balancing responsive cross-sectional tilt against trade execution drag.
- **Beta Confounding:** Because the strategy enforces a long-only constraint ($\sum w_i = 1, w_i \ge 0$), the portfolio retains near-unity exposure to the cryptocurrency market beta. Consequently, the strategy should be understood as a dynamic relative-strength asset allocation overlay on crypto market beta, rather than a market-neutral statistical arbitrage.

## Signal

### Feature Space Construction

At each daily timestep $t$, four technical and statistical features are computed for each asset $j \in \{1, \dots, n\}$ using a trailing lookback window of $N = 80$ days:
1. **Last Return ($r_{t-1, t}$):** The single-day return from $t-1$ to $t$:
   $$r_{t-1, t} = \frac{p_{t, j}}{p_{t-1, j}} - 1$$
2. **Trailing Volatility:** The sample standard deviation of daily returns over the $N$-day lookback window:
   $$\sigma_{j, t} = \sqrt{\frac{1}{N-1} \sum_{k=0}^{N-1} \left(r_{t-k, j} - \bar{r}_{j, t}\right)^2}$$
3. **Trailing Sharpe Ratio:** The annualized/sample ratio of mean return to volatility over the $N$-day lookback window:
   $$SR_{j, t} = \frac{\bar{r}_{j, t}}{\sigma_{j, t}}$$
4. **Return Rank Correlation:** The Spearman rank correlation between past daily returns and time indices over the lookback window, measuring trend persistence and monotonicity for individual assets.

For $n = 10$ assets, each asset produces 4 features, forming an input feature vector $\mathbf{f}_t$ of dimension $d = 40$ at day $t$.

### Target Construction

The target vector $\mathbf{b}_t$ corresponds to the relative return ranking of the assets at day $t+1$:
1. Calculate the realized next-day return for each asset $j$:
   $$r_{t+1, j} = \frac{p_{t+1, j}}{p_{t, j}} - 1$$
2. Compute the cross-sectional ordinal rank $rank(r_{t+1, j}) \in \{1, 2, \dots, n\}$, where $1$ denotes the lowest return and $n = 10$ denotes the highest return on day $t+1$.
3. Apply the power transform:
   $$b_{t, j} = \left(rank(r_{t+1, j})\right)^n$$
   The primary model specifies $n = 2$ ($returnRank^2$), mapping ranks $1, \dots, 10$ to target values $1, 4, 9, 16, 25, 36, 49, 64, 81, 100$.

### Model Architecture & Training Schedule (Algorithm 1)

- **Model Type:** Multi-Layer Perceptron (MLP) regressor.
- **Hidden Layers:** 2 fully connected hidden layers of size $(20, 20)$ neurons.
- **Input Dimension:** 40 (4 features $\times$ 10 assets).
- **Output Dimension:** 10 (raw portfolio weight scores for the 10 assets).
- **Initialization Seed:** Fixed seed = 10.
- **Objective Function:** Mean squared error (L2 loss) over the rolling training window:
   $$\min_\Theta \sum_{k=t-N}^{t-1} \left\| model(\mathbf{f}_k; \Theta) - \mathbf{b}_k \right\|_2^2$$
- **Lookback Window:** $N = 80$ days.
- **Retraining Frequency:** Every $m = 10$ trading days, the MLP weights $\Theta$ are updated by minimizing the L2 loss on the trailing $N$-day feature/target matrices $\mathbf{F}_{t-N, t-1}$ and $\mathbf{B}_{t-N, t-1}$. On intermediate days, the existing model weights are reused.

### Weight Normalization & Decay Smoothing

1. **Raw Predictions:** At evaluation time $t$, evaluate the model on current feature vector $\mathbf{f}_t$:
   $$\hat{\mathbf{w}}_t = \max\left(0, model(\mathbf{f}_t)\right)$$
2. **Simplex Normalization:** Enforce long-only unit investment:
   $$\hat{\mathbf{w}}_t \leftarrow \frac{\hat{\mathbf{w}}_t}{\sum_{j=1}^n \hat{w}_{t, j}}$$
3. **Exponential Weight Decay Filter:** To curb turnover and trading costs, smooth the predicted weight vector using historical allocation:
   $$\tilde{\mathbf{w}}_t = \frac{\sum_{i=1}^l \alpha^i \tilde{\mathbf{w}}_{t-i} + \hat{\mathbf{w}}_t}{1 + \sum_{i=1}^l \alpha^i}$$
   With calibrated parameters decay rate $\alpha = 0.7$ and decay lag $l = 1$:
   $$\tilde{\mathbf{w}}_t = \frac{0.7 \tilde{\mathbf{w}}_{t-1} + \hat{\mathbf{w}}_t}{1 + 0.7} = \frac{0.7}{1.7} \tilde{\mathbf{w}}_{t-1} + \frac{1}{1.7} \hat{\mathbf{w}}_t \approx 0.4118 \tilde{\mathbf{w}}_{t-1} + 0.5882 \hat{\mathbf{w}}_t$$
4. **Execution & Holding:** Allocate wealth according to $\tilde{\mathbf{w}}_t$ at day $t$, holding through day $t+1$. Realized portfolio return is $R_t = \tilde{\mathbf{w}}_t^T \mathbf{r}_t$.

## Required data

- **Universe:** 10 cryptocurrencies selected by market capitalization: Bitcoin (BTC), Ethereum (ETH), EOS, Ethereum Classic (ETC), Bitcoin Cash (BCH), Tron (TRX), Cardano (ADA), Ripple (XRP), Chainlink (LINK), and Binance Coin (BNB).
- **Venue / Provider:** Historical daily cryptocurrency pricing extracted from CoinGecko (`https://www.coingecko.com/en/coins/bitcoin/historical_data#panel`).
- **Market Type:** Spot prices (USD quote equivalent).
- **Timeframe:** Daily frequency ($T = 1,309$ trading days).
- **Fields:** Daily closing prices ($p_{t, j}$).
- **Point-in-Time Availability:** The features $r_{t-1, t}$, $\sigma_{j, t}$, $SR_{j, t}$, and rank correlation require only data up to day $t$. However, CoinGecko daily closing prints reflect volume-weighted averages across multiple global exchanges rather than an executable order book print at an exact timestamp.
- **Survivorship & Conditioning Gap:** The 10 assets were chosen based on market cap rankings as of **2023-11-01** (the end of the evaluation period) rather than point-in-time selection in May 2020. This constitutes an empirical survivorship and selection bias.

## Execution assumptions

- **Rebalancing Cadence:** Daily rebalancing at close/open.
- **Position Constraint:** Long-only portfolio ($\sum w_i = 1$, $w_{i, j} \ge 0$). Shorting and leverage are prohibited.
- **Execution Price:** Executed at the reported daily price without modeled bid-ask spread or intraday price impact.
- **Friction Modeling:** Evaluated under a parameter sweep of fixed proportional transaction fees: $c \in \{0.00\%, 0.025\%, 0.05\%, 0.075\%, 0.10\%, 0.125\%, 0.15\%\}$.
- **Turnover Mitigation:** Controlled explicitly via the exponential decay parameter $\alpha = 0.7, l = 1$.
- **Funding / Borrow:** Not applicable to spot implementation; no borrow fees or perpetual funding rates are incurred.

## Evidence

### Source-reported

All figures below are directly cited from the primary source paper (`arXiv:2512.08124v1`, Tables III, IV, and V) over the out-of-sample test period from **2020-05-01 to 2023-11-01** (1,309 daily observations), covering three distinct market phases: Bullish (2020/05/01–2021/07/01), Bearish (2021/07/01–2022/07/01), and Stagnant (2022/07/01–2023/11/01).

#### Table III: Benchmark and Traditional Strategy Comparison (Zero Fee)

| Strategy Class | Algorithm | Profit Factor | Sharpe Ratio | Information Ratio (vs UCRP) | Annualized Return (%) | Max Drawdown (%) | Win Pct (%) | Annualized Volatility (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Benchmark** | Buy-and-Hold (BAH, Uniform) | 1.10 | 0.83 | -0.21 | 52.82 | 77.38 | 54.20 | 63.83 |
| **Benchmark** | Universal Const. Rebal. (UCRP) | 1.10 | 0.86 | 0.00 | 55.89 | 79.53 | 55.05 | 64.83 |
| **Benchmark** | Best Const. Rebal. (BCRP, Hindsight) | 1.16 | 1.11 | 0.61 | 75.65 | 71.22 | 54.43 | 68.40 |
| **Follow-the-Winner** | Universal Portfolio (UP, Cover) | 1.10 | 0.86 | -0.04 | 55.84 | 79.14 | 55.12 | 64.63 |
| **Follow-the-Winner** | Exponential Gradient (EG, Helmbold)| 1.10 | 0.86 | -0.01 | 55.88 | 79.31 | 55.05 | 64.70 |
| **Follow-the-Loser** | Anti-correlation (Borodin) | 1.00 | 0.35 | -0.67 | 26.31 | 88.83 | 51.22 | 74.63 |
| **Follow-the-Loser** | CWMR (Confidence-Weighted) | 0.89 | -0.20 | -1.67 | -16.13 | 95.52 | 50.69 | 79.10 |
| **Follow-the-Loser** | OLMAR (Moving Average Rev.) | 0.92 | 0.00 | -1.22 | 0.19 | 95.66 | 51.22 | 82.40 |
| **Follow-the-Loser** | PAMR (Passive Aggressive) | 0.89 | -0.20 | -1.67 | -16.01 | 95.65 | 50.76 | 79.10 |
| **Follow-the-Loser** | RMR (Robust Median Reversion) | 0.93 | 0.07 | -0.96 | 6.28 | 96.15 | 51.61 | 87.37 |
| **Pattern Matching** | BNN (Non-parametric Kernel) | 1.06 | 0.70 | 0.03 | 57.80 | 83.71 | 51.68 | 82.97 |
| **Pattern Matching** | CORN (Correlation-Driven) | 1.05 | 0.63 | -0.07 | 52.29 | 84.04 | 51.20 | 82.93 |

#### Table IV: Machine Learning Model Performance (Zero Fee)

| Model Architecture | Target Formulation | Profit Factor | Sharpe Ratio | Information Ratio (vs UCRP) | Annualized Return (%) | Max Drawdown (%) | Win Pct (%) | Annualized Volatility (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **MLP (Proposed)** | Raw return ($r_t$) | 1.10 | 0.87 | 0.01 | 55.95 | **76.67** | 54.66 | 64.32 |
| **MLP (Proposed)** | Linear rank ($returnRank$) | 1.11 | 0.90 | 0.22 | 57.81 | 79.61 | 54.89 | 63.99 |
| **MLP (Proposed)** | **Squared rank ($returnRank^2$)** | **1.13** | **1.01** | **0.94** | **64.26** | 77.40 | 55.05 | **63.58** |
| **MLP (Proposed)** | Cubic rank ($returnRank^3$) | 1.11 | 0.91 | 0.26 | 58.20 | 78.72 | 54.97 | 63.90 |
| **MLP (Proposed)** | Quartic rank ($returnRank^4$) | 1.10 | 0.87 | -0.08 | 55.19 | 79.98 | 55.20 | 63.71 |
| **XGBoost** | Raw return ($r_t$) | 1.10 | 0.87 | 0.20 | 57.69 | 81.90 | 55.28 | 66.01 |
| **XGBoost** | Linear rank ($returnRank$) | 1.11 | 0.90 | 0.32 | 58.75 | 80.16 | 54.97 | 65.18 |
| **XGBoost** | Squared rank ($returnRank^2$) | 1.09 | 0.79 | -0.60 | 50.67 | 82.22 | 54.20 | 64.42 |
| **XGBoost** | Cubic rank ($returnRank^3$) | 1.09 | 0.81 | -0.36 | 52.72 | 81.05 | 54.59 | 64.74 |
| **XGBoost** | Quartic rank ($returnRank^4$) | 1.10 | 0.87 | 0.07 | 56.54 | 79.16 | 54.66 | 65.28 |
| **Random Forest** | Raw return ($r_t$) | 1.11 | 0.91 | 0.38 | 59.46 | 81.09 | 54.97 | 65.64 |
| **Random Forest** | Linear rank ($returnRank$) | 1.11 | 0.92 | 0.29 | 58.62 | 79.90 | **55.58** | 63.69 |
| **Random Forest** | Squared rank ($returnRank^2$) | 1.11 | 0.88 | 0.06 | 56.46 | 81.16 | 55.50 | 63.96 |
| **Random Forest** | Cubic rank ($returnRank^3$) | 1.11 | 0.90 | 0.25 | 58.20 | 80.13 | 54.97 | 64.44 |
| **Random Forest** | Quartic rank ($returnRank^4$) | 1.10 | 0.86 | -0.03 | 55.58 | 81.52 | 55.05 | 64.41 |
| **kNN ($k=15$)** | Raw return ($r_t$) | 1.11 | 0.89 | 0.27 | 58.23 | 81.78 | 54.43 | 65.24 |
| **kNN ($k=15$)** | Linear rank ($returnRank$) | 1.12 | 0.94 | 0.51 | 60.42 | 79.39 | 54.43 | 64.36 |
| **kNN ($k=15$)** | Squared rank ($returnRank^2$) | 1.11 | 0.91 | 0.31 | 58.66 | 79.25 | 54.66 | 64.32 |
| **kNN ($k=15$)** | Cubic rank ($returnRank^3$) | 1.11 | 0.89 | 0.19 | 57.60 | 79.84 | 55.20 | 64.53 |
| **kNN ($k=15$)** | Quartic rank ($returnRank^4$) | 1.10 | 0.86 | -0.01 | 55.77 | 80.46 | 55.20 | 64.56 |

#### Table V: Transaction Fee Stress Testing for MLP($returnRank^2$)

| Fee Rate | Profit Factor | Sharpe Ratio | Information Ratio (vs UCRP) | Annualized Return (%) | Max Drawdown (%) | Win Pct (%) | Annualized Volatility (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **0.00% (0 bps)** | 1.13 | 1.01 | 0.94 | 64.26 | 77.40 | 55.05 | 63.58 |
| **0.025% (2.5 bps)** | 1.13 | 0.99 | 0.81 | 63.06 | 78.04 | 55.05 | 63.59 |
| **0.050% (5 bps)** | 1.12 | 0.97 | 0.67 | 61.86 | 78.71 | 54.97 | 63.59 |
| **0.075% (7.5 bps)** | 1.12 | 0.95 | 0.54 | 60.65 | 79.37 | 54.97 | 63.59 |
| **0.100% (10 bps)** | 1.12 | 0.93 | 0.40 | 59.45 | 80.00 | 54.97 | 63.59 |
| **0.125% (12.5 bps)** | 1.11 | 0.92 | 0.27 | 58.25 | 80.61 | 54.97 | 63.60 |
| **0.150% (15 bps)** | 1.11 | 0.90 | 0.13 | 57.05 | 81.21 | 54.82 | 63.60 |

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Mean Reversion Disaster in Crypto:** The empirical evidence demonstrates that traditional mean-reversion strategies (`CWMR`, `PAMR`, `OLMAR`) fail completely in crypto, generating negative Sharpe ratios (-0.20 to 0.00) and devastating drawdowns (exceeding 95.5%). Betting on laggards in crypto is structurally impaired by token attrition and abandonment.
2. **Deep Drawdowns Inherent in Long-Only Crypto:** Despite generating positive relative alpha (IR = 0.94 vs UCRP), the MLP($returnRank^2$) strategy suffered a peak-to-trough maximum drawdown of **77.40%** during the 2021-2022 bear market. It offers minimal downside capital preservation against crypto market crashes.
3. **Diminishing Returns from Higher Rank Powers:** Moving from $n=2$ to $n=3$ or $n=4$ degrades strategy performance: Sharpe drops from 1.01 ($n=2$) to 0.91 ($n=3$) and 0.87 ($n=4$), with Information Ratio turning negative (-0.08) at $n=4$. Over-concentrating capital into the top-predicted asset introduces uncompensated idiosyncratic variance.

## Falsification plan

To falsify the hypothesis that MLP-driven cross-sectional return ranking generates genuine alpha:

1. **Point-in-Time Universe Audit:** Re-run the backtest using a strictly point-in-time universe selected on the 1st of each month by trailing 30-day volume/market cap. If the excess return over UCRP vanishes when survivorship bias is eliminated (e.g., when including tokens that failed or lost top-10 status during 2020-2023, such as LUNA/FTT), the thesis is falsified as selection artifact.
2. **Rank Shuffling / Permutation Test:** Randomly permute the asset identity assignments within the feature matrix $\mathbf{F}_t$ while preserving individual asset time-series dynamics. If the permuted model achieves comparable Information Ratios, the cross-sectional interaction claim of the MLP is refuted.
3. **Execution Delay & Spread Stress Test:** Introduce a realistic 1-bar execution delay (predicting at $t$, submitting limit/market orders at $t+1$ open or VWAP) and impose exchange-realistic maker/taker fees (e.g., 5 bps taker + 5 bps bid-ask spread). If net Sharpe drops below the naive UCRP benchmark (0.86), the strategy's excess edge is refuted by execution latency and market friction.
4. **Sub-Period Regime Decomposition:** Evaluate whether Information Ratio remains positive during extended bear markets when evaluated on an excess return basis. If the strategy underperforms UCRP during bear markets, the excess return is merely a bull-market beta amplifier.

## Crypto portability

- **Portability Status:** `direct`
- **Asset Class Native:** The source paper directly evaluates the strategy on a 10-asset cryptocurrency basket using daily CoinGecko price data.
- **Spot vs. Perpetual Adaptation:**
  - *Spot:* Directly implementable as formulated (long-only, no funding or borrow required).
  - *Perpetual:* Porting to perpetual futures would allow long/short cross-sectional ranking (e.g., long top quintile, short bottom quintile), converting the beta-dominated portfolio into a market-neutral relative-strength strategy. However, perpetual trading introduces 8-hour funding rate drag, liquidation thresholds, and basis divergence between spot and perp mark prices.
- **Session & Settlement:** Crypto operates 24/7/365. The daily boundary must be standardized (e.g., 00:00 UTC) across all venues to avoid asynchronous pricing errors in the feature matrices.

## Limitations

1. **Survivorship & Look-Ahead Bias in Universe Selection:** The universe of 10 coins was selected based on market capitalization as of November 1, 2023. This implicitly selects tokens that survived and grew over the 2020–2023 sample, ignoring failed or delisted tokens.
2. **Non-Standard Annualization Formulas:** As noted in the frontmatter contradiction, Equations 4 and 5 in the primary paper apply a $\sqrt{250}$ scaling factor to daily sums and standard deviations rather than standard compounding or $\sqrt{365}$ daily continuous-crypto scaling.
3. **Aggregated Data Friction:** Using CoinGecko consolidated daily prices masks intraday volatility, liquidity depth, and execution slippage that would occur on real centralized exchanges (e.g., Binance, OKX).
4. **Long-Only Beta Exposure:** The strategy is 100% invested in crypto spot assets at all times, subjecting capital to catastrophic ~80% drawdowns during systemic market declines.
5. **Hyperparameter Tuning Transparency:** The lookback window ($N = 80$), retraining frequency ($m = 10$), hidden dimensions ($(20, 20)$), and decay parameters ($\alpha = 0.7, l = 1$) were tested in-sample without a fully partitioned walk-forward optimization protocol.

## Implementation status

No implementation in NautilusTrader, PyBroker, or any execution harness has been performed.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

This record is a normalized academic capture for research staging and intake review. It does not authorize paper trading, testnet deployment, or live execution.

## Related Wiki records

- `[[quant/phase9-factor-taxonomy-and-cross-sectional-sorts-2026-08-28]]`
- `[[quant/phase10-universe-lifecycle-survivorship-2026-08-28]]`
- `[[quant/phase8-financial-ml-sample-leakage-contract-2026-08-28]]`
- `[[quant/signal-to-executable-pnl-costs-2026-08-28]]`
- `[[quant/sharpe-deflated-multiple-testing-2026-08-27]]`
- `[[quant/strata-selective-state-space-intraday-raw-bars-cross-sectional-ranking-2026-09-02]]`
- `[[quant/crypto-adaptive-trend-following-asymmetric-portfolio-2026-09-01]]`

## Sources

1. **Primary Academic Source:** Zijiang Yang, *"Long-only cryptocurrency portfolio management by ranking the assets: a neural network approach"*, arXiv preprint `arXiv:2512.08124v1 [q-fin.PM]`, submitted December 9, 2025. URL: [https://arxiv.org/abs/2512.08124](https://arxiv.org/abs/2512.08124).
2. **Primary LaTeX Source Package:** Extracted from `https://arxiv.org/src/2512.08124` (`conference_101719.tex`, `assetprice.png`, `port_and_alpha3.png`). Verified Table I (prediction target), Table II (daily return statistics), Table III (traditional algorithms), Table IV (machine learning algorithms), Table V (transaction fee sensitivity), and Algorithm 1 (MLP trading algorithm).
3. **Data Source:** CoinGecko historical daily pricing for BTC, ETH, EOS, ETC, BCH, TRX, ADA, XRP, LINK, BNB from 2020-05-01 to 2023-11-01. URL: [https://www.coingecko.com/en/coins/bitcoin/historical_data#panel](https://www.coingecko.com/en/coins/bitcoin/historical_data#panel).
