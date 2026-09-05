---
schema: strategy-research-record-v1
title: "Dynamic Johansen Cointegration and Deep Weighted Ensemble (DNN-LSTM) for Real-Time Cryptocurrency Pairs Trading"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - pairs-trading
  - statistical-arbitrage
  - dynamic-cointegration
  - deep-learning
  - dnn
  - lstm
  - ensemble-learning
  - cryptocurrency
  - conformal-prediction
status: research-only
confidence: high
source_as_of: 2026-01-30
sources:
  - "https://doi.org/10.3389/fams.2026.1749337"
  - "https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2026.1749337/full"
  - "https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2026.1749337/xml"
  - "Johannes Tshepiso Tsoku and Katleho Makatjane, 'Deep learning-based pairs trading: real-time forecasting of co-integrated cryptocurrency pairs', Frontiers in Applied Mathematics and Statistics, Volume 12, Article 1749337, published 30 January 2026. DOI: 10.3389/fams.2026.1749337"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Dynamic Johansen Cointegration and Deep Weighted Ensemble (DNN-LSTM) for Real-Time Cryptocurrency Pairs Trading

## Provenance

- **Primary Source:** Johannes Tshepiso Tsoku (Department of Business Statistics and Operations Research, North West University, Mafikeng, South Africa) and Katleho Makatjane (Department of Statistics and Population Studies, University of the Western Cape, Cape Town, South Africa), *"Deep learning-based pairs trading: real-time forecasting of co-integrated cryptocurrency pairs"*, published in *Frontiers in Applied Mathematics and Statistics*, Section: Statistics and Probability, Volume 12, Article 1749337 (received November 18, 2025; accepted January 12, 2026; published January 30, 2026).
- **Canonical DOI:** [10.3389/fams.2026.1749337](https://doi.org/10.3389/fams.2026.1749337)
- **Canonical Web Full Text:** [https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2026.1749337/full](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2026.1749337/full)
- **Canonical Machine-Readable XML:** [https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2026.1749337/xml](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2026.1749337/xml)
- **Direct Primary-Source Verification:** The complete peer-reviewed XML article source was directly inspected. All empirical metrics, statistical test tables, network architectural parameters, mathematical loss functions, prediction interval equations, and trading performance metrics were verified against the primary document without secondary intermediaries.
- **Repository Deduplication Audit:** A comprehensive audit of all existing records in `alpha-strategy-research` confirmed zero prior captures referencing `1749337`, `10.3389/fams.2026.1749337`, `Tsoku`, `Makatjane`, or the specific combination of dynamic Johansen cointegration with a performance-adaptive weighted DNN-LSTM ensemble on cryptocurrency pairs.
  - While adjacent statistical arbitrage records exist in the repository (e.g., `partial-information-regime-filtering-ddpg-ornstein-uhlenbeck-pairs-trading-2026-09-05.md` focusing on POMDP/DDPG control on commodity/equity spreads; `statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05.md` examining Warsaw equities under Avellaneda-Lee PCA replication; and `crypto-drl-execution-overlay-multi-pair-trading-2026-09-01.md` focusing on PPO/DDPG execution overlays on static cointegration), this record uniquely captures a time-varying Johansen cointegrating vector coupled to an adaptive performance-weighted deep neural ensemble (DNN + LSTM) with distribution-free conformal prediction intervals.

## Economic mechanism

### Source-reported

Pairs trading represents an established market-neutral statistical arbitrage strategy designed to exploit temporary relative mispricings between economically linked assets. The classical formulation posits that two or more non-stationary price series share a stationary linear combination representing a long-run equilibrium. Deviations from this equilibrium represent transient pricing inefficiencies that are expected to mean-revert as arbitrage capital enters the market.

However, standard econometric implementations—such as the Engle-Granger two-step method or static Johansen cointegration—suffer from severe empirical degradation in real markets, particularly within cryptocurrency ecosystems:
1. **Structural Instability of Equilibrium:** Traditional models assume a fixed, time-invariant cointegrating vector over multi-year horizons. In cryptocurrency markets, technological forks, protocol upgrades, regulatory crackdowns, exchange insolvencies, and speculative capital rotation frequently alter inter-asset relationships. Assuming static cointegration leads to model misspecification, false rejections of intermittent equilibrium, or severe divergence losses when the historical hedge ratio breaks down.
2. **Linearity Constraints of Residual Modeling:** Standard pairs trading relies on linear mean-reversion rules (e.g., static Bollinger bands or Ornstein-Uhlenbeck drift). These assume symmetric Gaussian noise, failing to model heavy tails, volatility clustering, and nonlinear state-dependent reversion dynamics.
3. **Rigidity of Static Ensembles:** Conventional machine learning ensembles (bagging, boosting, stacking, or uniform voting) apply static weights across time. When market regimes shift rapidly (e.g., from quiet consolidation to liquidating cascade), static ensembles cannot adapt their allocation toward the model architecture best suited to the prevailing regime.

To overcome these structural failures, Tsoku & Makatjane (2026) introduce a tri-partite quantitative framework:
- **Dynamic Johansen Cointegration:** Extends the Johansen vector autoregressive cointegration test to allow both the rank and the cointegrating vector $\boldsymbol{\beta}_t$ to vary over time, capturing regime-dependent equilibrium shifts and supporting the Adaptive Market Hypothesis (Lo 2004).
- **Complementary Base Learners:** Employs a Deep Neural Network (DNN) with multi-layer ReLU activations to capture complex, nonlinear, cross-sectional mappings, and a Long Short-Term Memory (LSTM) recurrent network with gated memory cells (input, forget, output gates) to capture sequential memory, persistence, and proportional deviations.
- **Dynamic Weighted Ensemble (DWE):** Continuously updates model contribution weights in real time based on recent out-of-sample forecast accuracy, prioritizing the architecture exhibiting the lowest tracking error in the current market environment.
- **Uncertainty Quantification via Conformal Prediction:** Constructs distribution-free 99% prediction interval widths (PIW) around ensemble spread forecasts to quantify time-varying model confidence and filter out trades during explosive, uncalibrated regime breaks.

### Research interpretation

From a market-microstructure and statistical arbitrage perspective, the strategy formalizes an adaptive relative-value pipeline:
- **Regime-Adaptive Equilibrium Vector:** The dynamically estimated cointegrating vector extracts a non-stationary log-price linear combination whose residuals form a stationary, mean-reverting process. In the multi-asset crypto basket ($ETH, BNB, XRP, LTC, USDT$), the stablecoin $USDT$ acts as the dominant numeraire anchor (reflecting its structural peg to the fiat dollar), while the volatile tokens provide relative-value elasticity.
- **Dual-Engine Signal De-biasing:** LSTMs are structurally advantaged in tracking proportional trends and local autocorrelation (achieving the lowest MAPE in empirical testing), but tend to exhibit higher variance in point magnitude. DNNs excel at bounding global magnitude and benchmark-relative deviations (lowest Theil's U). The dynamic weighting mechanism functions as an online Bayesian-like precision-weighting filter, dampening idiosyncratic error spikes from either base learner.
- **Percentile-Based Asymmetric Thresholding:** Rather than using arbitrary fixed standard deviation bands ($\pm 2\sigma$), the entry logic relies on empirical 10th and 90th percentiles of the ensemble-predicted dynamic score. This ensures that trading alerts fire only when the predicted spread deviation represents an extreme historical tail event, filtering out intermediate noise.

## Signal

### Signal Architecture and Mathematical Formulation

The strategy operates in four sequential stages: dynamic cointegration estimation, spread generation, deep ensemble trajectory forecasting, and percentile-gated signal generation.

#### 1. Dynamic Cointegration & Spread Formation
Let $\mathbf{P}_t = [P_{\text{USDT},t}, P_{\text{ETH},t}, P_{\text{BNB},t}, P_{\text{XRP},t}, P_{\text{LTC},t}]^T$ denote the vector of cryptocurrency closing prices at bar $t$. Prices are transformed to log space: $\mathbf{x}_t = \ln(\mathbf{P}_t)$.

A dynamic lagged Johansen procedure (Franses 2005) is estimated across rolling windows:
$$\Delta \mathbf{x}_t = \boldsymbol{\Pi}_t \mathbf{x}_{t-1} + \sum_{i=1}^{k-1} \boldsymbol{\Gamma}_{i,t} \Delta \mathbf{x}_{t-i} + \boldsymbol{\mu}_t + \boldsymbol{\epsilon}_t$$
where $\boldsymbol{\Pi}_t = \boldsymbol{\alpha}_t \boldsymbol{\beta}_t^T$.

The null hypothesis of cointegration rank $r \le 0$ is evaluated via the Johansen trace statistic:
$$\lambda_{\text{trace}}(r) = -T \sum_{i=r+1}^p \ln(1 - \hat{\lambda}_i)$$
where $\hat{\lambda}_i$ are the ordered squared canonical correlations (eigenvalues).

The leading cointegrating vector $\boldsymbol{\beta}_t = [\beta_{\text{USDT},t}, \beta_{\text{ETH},t}, \beta_{\text{BNB},t}, \beta_{\text{XRP},t}, \beta_{\text{LTC},t}]^T$ is extracted. The instantaneous equilibrium spread $S_t$ is computed as:
$$S_t = \boldsymbol{\beta}_t^T \mathbf{x}_t = \sum_{j=1}^5 \beta_{j,t} \ln(P_{j,t})$$

The raw spread is standardized into a dynamic Z-score:
$$Z_t = \frac{S_t - \mu_{S,t}}{\sigma_{S,t}}$$
where $\mu_{S,t}$ and $\sigma_{S,t}$ are the rolling sample mean and standard deviation of $S_t$ over the active lookback window (`source-reported`).

#### 2. Deep Base Learners (DNN & LSTM)
The standardized spread sequence $\{Z_{t-k}, \dots, Z_t\}$ is fed into two parallel deep learning architectures to forecast the forward spread deviation $\hat{Z}_{t+1}$:
- **Deep Neural Network (DNN):** Stacks $L=2$ hidden dense layers:
  $$\mathbf{y}^l = \text{ReLU}(\mathbf{W}^l \mathbf{y}^{l-1} + \mathbf{b}^l)$$
  Architecture (`source-reported`):
  - Input Layer: 3 input nodes representing lagged spread features.
  - Hidden Layer 1: 3 nodes with ReLU activation and Dropout probability $p = 0.3$.
  - Hidden Layer 2: 2 nodes with ReLU activation and Dropout probability $p = 0.2$.
  - Output Layer: 1 linear unit predicting $\hat{Z}_{t+1}^{\text{DNN}}$.
- **Long Short-Term Memory (LSTM):** Computes recurrent memory states via:
  $$\begin{aligned}
  \mathbf{i}_t &= \sigma(\mathbf{W}_i \mathbf{x}_t + \mathbf{U}_i \mathbf{h}_{t-1} + \mathbf{b}_i) \\
  \tilde{\mathcal{C}}_t &= \tanh(\mathbf{W}_c \mathbf{x}_t + \mathbf{U}_c \mathbf{h}_{t-1} + \mathbf{b}_c) \\
  \mathbf{f}_t &= \sigma(\mathbf{W}_f \mathbf{x}_t + \mathbf{U}_f \mathbf{h}_{t-1} + \mathbf{b}_f) \\
  \mathcal{C}_t &= \mathbf{f}_t \odot \mathcal{C}_{t-1} + \mathbf{i}_t \odot \tilde{\mathcal{C}}_t \\
  \mathbf{o}_t &= \sigma(\mathbf{W}_o \mathbf{x}_t + \mathbf{U}_o \mathbf{h}_{t-1} + \mathbf{b}_o) \\
  \mathbf{h}_t &= \mathbf{o}_t \odot \tanh(\mathcal{C}_t)
  \end{aligned}$$
  yielding forward point prediction $\hat{Z}_{t+1}^{\text{LSTM}}$.

Both models are trained by backpropagation minimizing Mean Squared Error (MSE) via the Adam optimizer with early stopping and learning rate scheduling:
$$\mathcal{L} = \frac{1}{N} \sum_{t=1}^N (Z_t - \hat{Z}_t)^2$$

#### 3. Dynamic Weighted Ensemble (DWE) & Prediction Intervals
The ensemble combines the individual forecasts via performance-adaptive weights:
$$\hat{Z}_{t+1}^{\text{ensemble}} = \sum_{i=1}^M w_i(t+1) f_i(t+1)$$
where $M=2$ (DNN, LSTM), and weights $w_i(t+1)$ are dynamically updated based on recent out-of-sample prediction accuracy (such that $\sum w_i = 1$) (`source-reported`).

Ensemble forecast variance and distribution-free prediction interval width (PIW) are computed as:
$$\hat{\sigma}_{t+1}^2 = \frac{1}{M} \sum_{i=1}^M \left(f_i(t+1) - \hat{Z}_{t+1}^{\text{ensemble}}\right)^2$$
$$\text{PIW}_{t+1}^{\text{ensemble}} = 2 \cdot q_{\alpha/2}^{\text{dyn}} \cdot \hat{\sigma}_{t+1}$$
where $q_{\alpha/2}^{\text{dyn}}$ is the empirical error quantile corresponding to a 99% confidence level ($\alpha = 0.01$) derived from Temporal Conformal Prediction (`source-reported`).

#### 4. Trading Decision Rules
Signals are evaluated conditionally on the predicted ensemble score $\hat{Z}_{t+1}^{\text{ensemble}}$ relative to empirical rolling percentile thresholds ($Q_{0.10}$ and $Q_{0.90}$):
- **Long Entry (BUY Signal):**
  $$\text{Trigger when } \hat{Z}_{t+1}^{\text{ensemble}} \le Q_{0.10}$$
  - *Mechanism:* The spread is statistically undervalued relative to the cointegrated equilibrium basket and is predicted to mean-revert upward toward the mean.
  - *Action:* Establish a long position in the undervalued synthetic asset combination (or long asset A / short asset B in pairwise execution) (`source-reported`).
- **Short Entry (SELL Signal):**
  $$\text{Trigger when } \hat{Z}_{t+1}^{\text{ensemble}} \ge Q_{0.90}$$
  - *Mechanism:* The spread is statistically overbought relative to the equilibrium vector and is projected to mean-revert downward.
  - *Action:* Establish a short position in the overvalued synthetic basket (`source-reported`).
- **Neutral / HOLD State:**
  $$\text{Maintain current position or stay in cash when } Q_{0.10} < \hat{Z}_{t+1}^{\text{ensemble}} < Q_{0.90}$$
  - *Conservative Filter:* Even during extreme single-period negative spikes (e.g., Date 223 score of -4.7369), if dynamic conformal bounds or percentile criteria are not confirmed, the system maintains a HOLD state to suppress false-positive whipsaws (`source-reported`).
- **Exit Logic:**
  - Standard exit occurs when the spread returns to the zero-mean line ($Z_t \approx 0$) or crosses the neutral band (`source-reported`).
  - Stop-loss threshold: Not explicitly parameterized in primary paper; `research-proposed` as a stop-loss when spread diverges beyond 3 standard deviations ($|Z_t| \ge 3.0$) or after 15 calendar days maximum holding period (`research-proposed`).

## Required data

- **Universe / Assets:** Five major liquid digital assets: Tether ($USDT$), Ethereum ($ETH$), Binance Coin ($BNB$), Ripple ($XRP$), and Litecoin ($LTC$) (`source-reported`). Additional major pairs evaluated for pairwise cointegration include $BTC\text{--}ETH, BTC\text{--}LTC, BTC\text{--}XRP, ETH\text{--}LTC, ETH\text{--}XRP, LTC\text{--}XRP$ (`source-reported`).
- **Venue:** Centralized exchange limit order books (Binance Spot & Binance USDⓈ-M Futures) and aggregated data vendors (Yahoo Finance / `yfinance`) (`source-reported`).
- **Timeframe:**
  - Long-term calibration sample: Daily close prices from 02 January 2018 to 31 October 2025 ($N = 2,842$ continuous daily observations) (`source-reported`).
  - Out-of-sample test window: March 2024 to November 2025 (`source-reported`).
  - Real-time streaming evaluation: High-frequency WebSocket price streams from Binance deployed on AWS EC2 and AWS Lambda (`source-reported`).
- **Required Fields:**
  - Close prices ($P_t$) for each asset (`source-reported`).
  - High-frequency order book / trade ticks for real-time WebSocket feeds (`source-reported`).
- **Point-in-Time & Availability:** Strictly rolling window architecture without lookahead bias. All cointegrating vectors, normalization statistics, and deep learning network weights are trained on lagged historical data prior to each forecasting step (`source-reported`).
- **Missing Data Handling:** Cryptocurrency markets trade 24/7/365 without exchange holidays; missing price prints are zero in continuous liquid markets; any temporary API disconnect is handled via forward-fill of the most recent valid print (`research-proposed`).

## Execution assumptions

- **Signal-to-Order Latency:**
  - Daily evaluation: Next-bar market order executed at opening price or VWAP (`research-proposed`).
  - Streaming deployment: Real-time cloud-based inference (AWS EC2 / Lambda) with estimated signal lag of 0.0000 days (`source-reported`).
- **Order Types & Execution:** Market orders assumed in theoretical simulation (`source-reported`). Limit orders with queue estimation required in production to avoid taker fee drag (`research-proposed`).
- **Transaction Costs & Slippage:**
  - *Source Assumption:* Transaction costs and slippage were omitted in the primary paper backtest simulation under the assumption of high asset liquidity (`source-reported provenance gap`).
  - *Research-Proposed Operational Standard:* In live cryptocurrency deployment, maker/taker fees must be explicitly modeled. Binance VIP0 taker fee is $0.0400\%\text{--}0.0750\%$ per leg ($0.08\%\text{--}0.15\%$ round trip across pairs), and maker fee is $0.0200\%$ per leg (`research-proposed`).
- **Position Sizing & Leverage:**
  - Average position size in empirical test: $0.5113$ (51.13% capital utilization), representing moderate exposure and absence of excessive leverage (`source-reported`).
  - Leverage: 1.0x (unleveraged cash/margin) in baseline; maximum leverage constrained to 2.0x (`research-proposed`).
- **Borrow & Shorting:** Requires spot margin borrowing or linear perpetual futures contracts on Binance to execute short legs on tokens ($ETH, BNB, XRP, LTC$) (`research-proposed`).

## Evidence

### Source-reported

All empirical figures below trace directly to Tsoku & Makatjane (2026), *Frontiers in Applied Mathematics and Statistics*, Volume 12, Article 1749337:

#### 1. Dynamic Cointegration Test Results (Table 2)
- **Dynamic Cointegrating Vector (Leading Eigenvector, $\lambda_1 = 0.0773$):**
  - $\text{USDT}$: $-270.904$ (Absolute: $270.904$)
  - $\text{Ethereum}$: $-0.432$ (Absolute: $0.432$)
  - $\text{BNB}$: $+0.124$ (Absolute: $0.124$)
  - $\text{Ripple}$: $+0.067$ (Absolute: $0.067$)
  - $\text{Litecoin}$: $-0.030$ (Absolute: $0.030$)
- **Johansen Trace Statistics vs. Critical Values:**
  - $r \le 0$: Trace Statistic = $276.319$ (Critical Values: 90% = $65.820$, 95% = $69.819$, 99% = $77.820$). Rejection of $r \le 0$ at $p < 0.01$ confirms statistically significant cointegration.
  - $r \le 1$: Trace Statistic = $47.799$ (90% CV = $44.493$, 95% CV = $47.855$, 99% CV = $54.681$).
  - $r \le 2$: Trace Statistic = $19.299$ (95% CV = $29.796$, not rejected).
  - $r \le 3$: Trace Statistic = $4.832$ (95% CV = $15.494$, not rejected).
  - $r \le 4$: Trace Statistic = $0.537$ (95% CV = $3.841$, not rejected).

#### 2. Model Forecasting Performance Comparison on Out-of-Sample Spread (Table 3)
| Metric | Deep Neural Network (DNN) | LSTM Network | Dynamic Weighted Ensemble (DWE) | Winning Architecture |
| :--- | :---: | :---: | :---: | :--- |
| **MSE** | 0.017667 | 0.019226 | **0.012124** | **Dynamic Ensemble** |
| **RMSE** | 0.132917 | 0.138658 | **0.110108** | **Dynamic Ensemble** |
| **MAE** | 0.101259 | 0.104951 | **0.083607** | **Dynamic Ensemble** |
| **MAPE (%)** | 4.098900% | **1.490429%** | 2.033504% | **LSTM** |
| **MFE (Bias)** | -0.052819 | -0.044590 | **-0.043546** | **Dynamic Ensemble** |
| **Theil's U** | **0.371179** | 0.794121 | 0.383306 | **DNN** |

- *Observation:* The Dynamic Ensemble achieves the lowest magnitude-based errors (MSE, RMSE, MAE) and lowest forecast bias. The LSTM achieves the lowest percentage error (MAPE), confirming its superior modeling of proportional changes, while the DNN achieves superior scaled efficiency relative to a naive random walk (Theil's U).

#### 3. Real-Time Pairs Trading Risk & Performance Outcomes (Table 4 & Section 3.2)
- **Total Generated Signals:** 113 trade signals over the out-of-sample evaluation period.
- **Trade Win/Loss Breakdown:** 81 winning trades (71.68%) vs. 32 losing trades (28.32%).
- **Hit Rate (Win/Loss Probability):** **0.5821** (58.21%).
- **Average Profit / Loss per Trade:** **+0.0111** (+1.11% gross return per completed trade cycle).
- **Maximum Drawdown (MDD):** **-0.2875** (-28.75%).
- **Sharpe Ratio:** **1.3662** (statistically robust risk-adjusted return over risk-free rate).
- **Sortino Ratio:** **1.1411** (indicating downside risk control).
- **Average Position Size:** **0.5113** (51.13% exposure).
- **Estimated Signal Lag:** **0.0000 days** (immediate execution response).
- **Market Correlation:** **-0.6517** (demonstrating strong negative beta / market-diversifying characteristics).

#### 4. Prediction Uncertainty & Stability Quantification (Section 3.3 & Figures 7–8)
- **99% Prediction Interval Width (PIW):**
  - Average PIW: **0.0772**
  - Minimum PIW: **0.0232**
  - Maximum PIW: **0.3094**
  - Terminal PIW: **0.0337**
- *Observation:* Narrow intervals indicate high confidence in point forecasts during stable regimes, with rapid adaptive widening during market stress protecting against false breakout entries.

### Independently reproduced

`not independently reproduced`. All quantitative claims, statistical tables, and performance figures are third-party empirical findings published by Tsoku & Makatjane (2026). No independent backtesting run has been conducted in NautilusTrader or PyBroker.

### Negative evidence

1. **Absence of Transaction Cost Modeling in Original Study:**
   - The reported average profit per trade is +1.11% (+0.0111).
   - In a multi-asset basket pairs trade involving 2 to 5 cryptocurrency legs on Binance spot/margin, a retail taker fee of 0.075% per leg results in a two-way round-trip transaction cost of $2 \times 2 \times 0.075\% = 0.30\%$ (for 2 legs) up to $0.75\%$ (for 5 legs).
   - Bid-ask spreads in altcoin pairs ($LTC, XRP$) during volatile periods typically range between 5 and 15 bps.
   - Slippage and taker fees could erode 30% to 70% of the gross 1.11% profit per trade, reducing the net Sharpe ratio from 1.3662 to an estimated range of 0.65–0.95.
2. **Stablecoin Dislocation Tail Risk:**
   - In the leading cointegrating vector (Table 2), $USDT$ carries a dominant weight of $-270.904$. This massive loading reflects the fact that USDT price volatility is tiny ($\sim 0.001$), requiring a huge multiplier to balance the dollar moves of ETH and BNB.
   - If USDT experiences a temporary depegging event (e.g., trading down to $0.985$ or up to $1.015$), the spread $S_t$ suffers an artificial shock of $\pm 270.904 \times \ln(0.985) \approx \mp 4.1$, triggering massive spurious trade signals that reflect stablecoin credit risk rather than cross-token relative-value mispricing.
3. **Severe Maximum Drawdown:**
   - The strategy experienced a maximum drawdown of -28.75% even without leverage. In a leveraged margin account (e.g., 2x–3x), this would represent a catastrophic capital impairment (-57% to -86%).

## Falsification plan

The hypothesis that dynamic Johansen cointegration combined with an adaptive DNN-LSTM ensemble generates exploitable out-of-sample alpha in cryptocurrency pairs can be falsified through the following pre-declared operational tests:

### Test 1: Full Transaction Friction & Exchange Fee Stress Test
- **Methodology:** Reconstruct the dynamic spread on Binance spot and perpetual contracts using tick-level trade and top-of-book L2 quote data. Apply realistic maker/taker fees ($0.050\%$ taker, $0.020\%$ maker) and empirical effective spread slippage ($2.5\text{ bps}$ per leg).
- **Decision Rule / Metric:** Calculate net Sharpe ratio, net profit per trade, and net CAGR across all 113 trades.
- **Research-Defined Falsification Threshold:** If the net Sharpe ratio drops below **0.50** (`research-defined falsification threshold`) or the net average profit per completed trade drops below **0.15% (15 bps)** (`research-defined falsification threshold`), reject the hypothesis that the strategy possesses tradable alpha after real-world execution frictions.

### Test 2: Multi-Regime Walk-Forward Stability Test
- **Methodology:** Partition the 2018–2026 data into 4 distinct structural market regimes: (1) 2018–2019 crypto winter, (2) 2020–2021 liquidity expansion bull market, (3) 2022 deleveraging crash (Terra/FTX), and (4) 2023–2025 institutional ETF expansion.
- **Decision Rule / Metric:** Evaluate dynamic cointegration rank stability and out-of-sample Sharpe ratio in each isolated regime fold.
- **Research-Defined Falsification Threshold:** If the strategy generates a negative Sharpe ratio ($\text{Sharpe} < 0.0$) in **two or more of the four distinct market regimes** (`research-defined falsification threshold`), falsify the claim that dynamic Johansen cointegration successfully adapts to structural breaks.

### Test 3: Stablecoin Numeraire Ablation & Synthetic Depeg Placebo
- **Methodology:** 
  1. Estimate the dynamic cointegration system on crypto-only baskets excluding USDT ($BTC, ETH, BNB, LTC, XRP$) expressed in pure Bitcoin numeraire ($s_t = \ln(P_t / P_{\text{BTC},t})$).
  2. Inject synthetic 1.0% depeg perturbations into USDT price series.
- **Decision Rule / Metric:** Compare cointegration rank and trading performance with and without USDT.
- **Research-Defined Falsification Threshold:** If cointegration rank collapses ($r=0$, trace stat $p > 0.05$) when USDT is removed, or if a 1.0% USDT price shock generates greater than $3.0\sigma$ spread divergence leading to false trade executions (`research-defined falsification threshold`), falsify the relative-value crypto pricing mechanism and classify the original finding as an artifact of stablecoin fiat-peg collinearity.

### Test 4: Model Architecture Ablation (DWE vs. Static Benchmarks)
- **Methodology:** Run parallel walk-forward simulations replacing the Dynamic Weighted Ensemble with: (a) equal-weight voting ($50/50$ DNN/LSTM), (b) pure LSTM, (c) pure DNN, (d) linear ARIMA/GARCH spread model, and (e) static Engle-Granger pairs trading.
- **Decision Rule / Metric:** Measure Out-of-Sample Mean Squared Error (MSE) and trade hit rate.
- **Research-Defined Falsification Threshold:** If the Dynamic Weighted Ensemble fails to demonstrate statistically significant reduction in forecast MSE compared to equal-weight voting or static Engle-Granger ($p > 0.05$ via Diebold-Mariano test) (`research-defined falsification threshold`), reject the necessity and value of the deep dynamic weighting architecture.

## Crypto portability

- **Portability Classification:** `direct` (`source-reported`).
  - Unlike traditional equity models ported into crypto, Tsoku & Makatjane (2026) natively formulated, calibrated, and empirically tested this framework directly on cryptocurrency price data ($BTC, ETH, BNB, LTC, XRP, USDT$) using Yahoo Finance and Binance streaming APIs.
- **Crypto Microstructure Alignment:**
  - *24/7 Continuous Trading:* Cryptocurrencies trade without weekend or overnight session gaps, eliminating the overnight jump risk that plagues traditional equity pairs trading.
  - *Perpetual Futures & Funding Rate Frictions:* While the authors tested spot prices, institutional deployment typically utilizes USDⓈ-M perpetual futures. In perpetual contracts, holding asymmetric long and short positions across multiple coins incurs continuous 8-hour funding rates. If the long leg carries positive funding while the short leg carries negative funding, funding carry could offset spread convergence profits. Funding rate parity must be incorporated into net spread calculations (`research-proposed`).
  - *Exchange Fragmentation & Basis:* Cross-venue discrepancies between Binance, OKX, Bybit, and Coinbase offer potential triangular arbitrage, but also introduce execution basis risk if legs are filled on differing venues. Single-venue execution (Binance) minimizes basis risk.

## Limitations

- **Omission of Transaction Costs (`provenance gap`):** The primary paper does not incorporate exchange trading fees (maker/taker), borrowing costs for short margin positions, or order book bid-ask spread slippage.
- **Stablecoin Collinearity / Numeraire Artifact:** The dominant cointegrating coefficient on USDT ($-270.904$) raises a methodological concern that the cointegrating vector primarily identifies the dollar peg of USDT against volatile altcoins rather than an intrinsic economic cointegration among the tokens themselves.
- **Lack of Hard Stop-Loss / Tail Risk Triggers (`underspecified`):** While the paper details percentile entry thresholds (10th/90th percentiles), it omits explicit stop-loss rules, contributing to the substantial maximum drawdown of -28.75%.
- **Small Universe Basket:** The empirical evaluation is restricted to 5 cryptocurrencies ($USDT, ETH, BNB, XRP, LTC$). Scalability to broader mid-cap or DeFi tokens remains unverified.
- **Computational Overhead:** Online dynamic retraining of deep neural networks (DNN and LSTM) and rolling Johansen trace tests requires dedicated cloud infrastructure (AWS EC2 / Lambda) and GPU compute, introducing operational latency and infrastructure costs.

## Implementation status

- `not-implemented`.
- This research capture records external, peer-reviewed findings from Tsoku & Makatjane (*Frontiers in Applied Mathematics and Statistics*, 2026).
- No implementation has been created in `nautilus-quant-system`, PyBroker, or NautilusTrader.
- No backtest, paper trading, testnet, or live trading has been authorized or conducted.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- A presence in this repository denotes normalized external research capture feeding Loop A (Hermes Research Loop). It does not constitute approval for live capital allocation, paper trading, or production deployment.

## Related Wiki records

- `[[quant/partial-information-regime-filtering-ddpg-ornstein-uhlenbeck-pairs-trading-2026-09-05]]` — Partially observable Markov decision process and DDPG control for Ornstein-Uhlenbeck pairs trading.
- `[[quant/statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05]]` — Deep learning LSTM factor replication and mean-reverting statistical arbitrage under Avellaneda-Lee framework.
- `[[quant/crypto-drl-execution-overlay-multi-pair-trading-2026-09-01]]` — Dynamic multi-pair trading in cryptocurrency markets with deep reinforcement learning execution overlays.
- `[[quant/foreign-exchange-spatiotemporal-graph-statistical-arbitrage-2026-09-02]]` — Spatiotemporal graph neural networks for multi-asset statistical arbitrage and cointegration.
- `[[quant/multiscale-multifractal-cross-correlation-signed-portfolio-2026-09-02]]` — Multifractal detrended cross-correlation analysis for cryptocurrency asset allocation.

## Sources

1. **Primary Peer-Reviewed Paper:**
   - Johannes Tshepiso Tsoku and Katleho Makatjane. *"Deep learning-based pairs trading: real-time forecasting of co-integrated cryptocurrency pairs"*. *Frontiers in Applied Mathematics and Statistics*, Section: Statistics and Probability, Volume 12, Article 1749337 (January 30, 2026).
   - DOI: [10.3389/fams.2026.1749337](https://doi.org/10.3389/fams.2026.1749337)
   - Stable URL: [https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2026.1749337/full](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2026.1749337/full)
   - Canonical XML source: [https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2026.1749337/xml](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2026.1749337/xml)
2. **Cited Foundational Econometric & Methodological Literature:**
   - Franses, P. H. (2005). "On the analysis of seasonally cointegrated time series." *Journal of Econometrics*.
   - Johansen, S. (1991). "Estimation and Hypothesis Testing of Cointegration Vectors in Gaussian Vector Autoregressive Models." *Econometrica*, 59(6), 1551–1580.
   - Gatev, E., Goetzmann, W. N., & Rouwenhorst, K. G. (2006). "Pairs Trading: Performance of a Relative-Value Arbitrage Rule." *The Review of Financial Studies*, 19(3), 797–827.
   - Lo, A. W. (2004). "The Adaptive Markets Hypothesis: Market Efficiency from an Evolutionary Perspective." *Journal of Portfolio Management*, 30(5), 15–29.
   - Romano, Y., Sesia, M., & Candès, E. J. (2019). "Conformalized Quantile Regression." *Advances in Neural Information Processing Systems (NeurIPS)*, 32.
