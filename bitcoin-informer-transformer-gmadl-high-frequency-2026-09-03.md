---
schema: strategy-research-record-v1
title: "Bitcoin Informer ProbSparse Transformer High-Frequency Alpha with Generalized Mean Absolute Directional Loss"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - informer
  - transformer
  - gmadl
  - high-frequency
  - machine-learning
  - loss-function
status: research-only
confidence: high
source_as_of: 2024-07-24
sources:
  - "https://doi.org/10.48550/arXiv.2503.18096"
  - "https://arxiv.org/abs/2503.18096"
  - "https://arxiv.org/html/2503.18096v1"
  - "https://gitlab.com/FilipStefaniuk/wne-msc-thesis/-/tree/0ded87a0fb099ffa669a222ed648fbf81ad2d022"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Informer ProbSparse Transformer High-Frequency Alpha with Generalized Mean Absolute Directional Loss

## Provenance

- **Primary Source:** Filip Stefaniuk and Robert Ślepaczuk (Quantitative Finance Research Group, Faculty of Economic Sciences, University of Warsaw), *"Informer In Algorithmic Investment Strategies on High Frequency Bitcoin Data"*, arXiv:2503.18096v1 [q-fin.CP, cs.LG, q-fin.TR], submitted March 24, 2025.
- **Digital Object Identifier (DOI):** [10.48550/arXiv.2503.18096](https://doi.org/10.48550/arXiv.2503.18096).
- **Full Text Canonical URL:** [https://arxiv.org/abs/2503.18096](https://arxiv.org/abs/2503.18096) (HTML: [https://arxiv.org/html/2503.18096v1](https://arxiv.org/html/2503.18096v1)).
- **Primary Implementation Repository:** Public GitLab repository `https://gitlab.com/FilipStefaniuk/wne-msc-thesis.git` at immutable commit SHA `0ded87a0fb099ffa669a222ed648fbf81ad2d022`. Key audited implementation files:
  - Loss definition: `src/ml/loss.py` (`GMADL` subclassing `MultiHorizonMetric`).
  - Model architecture wrapper: `src/ml/model.py`.
  - Strategy execution logic: `src/strategy/strategy.py` (`ModelGmadlPredictionsStrategy`).
  - Performance accounting: `src/strategy/metrics.py`.
- **Underlying Architectural Foundations:**
  - Informer architecture: Haoyi Zhou, Shanghang Zhang, Jieqi Peng, Shuai Zhang, Jianxin Li, Hui Xiong, Wancai Zhang, *"Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting"*, AAAI 2021, arXiv:2012.07436. Public PyTorch Lightning implementation: `https://github.com/martinwhl/Informer-PyTorch-Lightning`.
  - GMADL loss specification: Jakub Michańków, Paweł Sakowski, Robert Ślepaczuk, *"Mean Absolute Directional Loss as a new loss function for machine learning problems in algorithmic investment strategies"*, *Journal of Computational Science* 81 (2024), 102375, DOI: [10.1016/j.jocs.2024.102375](https://doi.org/10.1016/j.jocs.2024.102375).
- **Universe and Sample Data:** Binance BTC/USDT spot candlestick data from August 21, 2019 to July 24, 2024 (5 full years) evaluated across three distinct high frequencies: 5-minute, 15-minute, and 30-minute intervals.
- **Cross-Market Conditioning Inputs:** Daily CBOE Volatility Index (VIX) closing levels, Federal Reserve monthly Federal Funds effective rate (FRED: FEDFUNDS), and daily Alternative.me Crypto Fear & Greed Index.
- **Validation Design:** 6 rolling evaluation windows. Each window contains 24 months in-sample (split 80% train = 19.2 months, 20% validation = 4.8 months for hyperparameter tuning) and 6 months out-of-sample test. Step size is 6 months, yielding an aggregate out-of-sample evaluation period of 36 months (3 years) covering 311,040 test bars at 5-minute frequency.

## Economic mechanism

### Source-reported

Conventional quantitative deep-learning forecasting models for financial time series almost universally optimize symmetric distance-based loss functions such as Mean Squared Error (MSE) or Root Mean Squared Error (RMSE). Stefaniuk and Ślepaczuk demonstrate that this conventional approach suffers from a fatal economic alignment breakdown in high-frequency trading:

1. **The Conditional Mean Shrinkage Trap:** In high-frequency price series characterized by low signal-to-noise ratios, heavy-tailed leptokurtosis, and non-zero exchange fees (e.g. 10 basis points on Binance spot), quadratic penalty functions (RMSE/MSE) heavily penalize large residual deviations. Consequently, gradient descent drives network parameters toward predicting values close to the unconditional or conditional zero-mean return. Because high-frequency return distributions have massive mass centered near zero, a trivial model predicting $\hat{y} \approx 0$ achieves low RMSE, yet its predictions never clear the transaction fee barrier ($0.1\%$). In empirical testing, an Informer model trained with RMSE generated only 16 trades over a 3-year out-of-sample period at 5-minute frequency, rendering it economically useless.
2. **Directional Sign Asymmetry in Trading Payoffs:** Trading PnL is fundamentally governed by the directional sign of the forward return ($\text{sign}(y_t)$) and its realization magnitude relative to transaction costs, not by small-magnitude precision. Missing or misclassifying the direction of a large volatile price impulse destroys capital, whereas minor distance errors on small noisy bars are economically irrelevant.
3. **GMADL Payoff Alignment:** The Generalized Mean Absolute Directional Loss (GMADL) directly aligns neural network parameter optimization with trading profitability by combining a smooth logistic sign-concordance reward with a power-law magnitude weighting:
   $$GMADL = \frac{1}{N}\sum_{i=1}^{N} (-1) \cdot \left(\frac{1}{1 + e^{-a \cdot y_i \cdot \hat{y}_i}} - \frac{1}{2}\right) \cdot (|y_i|)^b$$
   where $a=100$ and $b=2$. When observed return $y_i$ and forecast $\hat{y}_i$ share the same directional sign ($y_i \cdot \hat{y}_i > 0$), the logistic term exceeds $0.5$, producing a negative loss (a reward) scaled by the squared magnitude $|y_i|^2$. Conversely, when directional signs diverge ($y_i \cdot \hat{y}_i < 0$), the network incurs a steep positive penalty scaled by $|y_i|^2$.
4. **Informer Long-Sequence Scalability:** Standard Transformer multi-head self-attention scales quadratically $\mathcal{O}(L^2)$ in time and memory, limiting lookback sequence length. Informer resolves this via **ProbSparse self-attention**, which calculates an active query score based on Kullback-Leibler divergence relative to a uniform distribution, retaining only the top $u = c \cdot \ln(L_Q)$ dominant query vectors (with sampling factor $c$). It further incorporates **self-attention distilling**, applying 1D convolutions with ELU activation and max-pooling across cascading layers to halve sequence dimensions, enabling the model to learn long-range multi-frequency dependencies without gradient instability.

### Research interpretation

The falsifiable alpha hypothesis is that **intraday 5-minute Bitcoin price returns exhibit directional predictability that can be captured by a sequence-to-sequence attention architecture, provided the loss function selectively rewards directional accuracy on large-magnitude price jumps rather than penalizing variance around zero.**

This mechanism represents an explicit interaction between architecture and objective function:
- The Informer's ProbSparse attention acts as an efficient multi-timeframe feature extractor capable of synthesizing high-frequency micro-movements with multi-day moving average ratios and macro/sentiment covariates without exploding attention maps.
- GMADL provides the necessary non-convex training objective that prevents the attention weights from collapsing into a passive zero-return predictor under high-frequency noise.
- Crucially, the strategy operates as a **directional impulse-capture system**: by trading only when expected return exceeds calibrated positive/negative thresholds, it filters out low-conviction noise and selectively positions for large-magnitude continuation swings.

## Signal

### Input Feature Representation ($\mathbf{X}_t \in \mathbb{R}^{L \times 28}$)

The Informer model ingests an input sequence of length $L = \text{past\_window}$ (for 5-minute GMADL Informer, $L = 28$ bars, equivalent to 140 minutes) composed of 26 continuous real-valued variables and 2 categorical variables (Table 10 of source):

1. **Raw Candlestick Metrics (5 features):** Open, High, Low, Close, Volume.
2. **Log Return (1 feature):** $r_t = (P_t - P_{t-1}) / P_{t-1}$.
3. **Intrabar Price Ratios (4 features):**
   - Open-to-Close: $O_t / C_t$
   - High-to-Close: $H_t / C_t$
   - Low-to-Close: $L_t / C_t$
   - High-to-Low: $H_t / L_t$
4. **Multi-Horizon Realized Volatilities (3 features):** Rolling standard deviation of returns computed over 1 hour, 1 day, and 7 days (`vol_1h`, `vol_1d`, `vol_7d`).
5. **Moving Average Price Ratios (5 features):**
   - Simple Moving Average ratios: $\text{SMA}_{1\text{h}}(C) / C_t$, $\text{SMA}_{1\text{d}}(C) / C_t$, $\text{SMA}_{7\text{d}}(C) / C_t$.
   - Exponential Moving Average ratios: $\text{EMA}_{1\text{h}}(C) / C_t$, $\text{EMA}_{1\text{d}}(C) / C_t$.
6. **Technical Oscillators (5 features):**
   - MACD line: $\text{EMA}_{12}(C) - \text{EMA}_{26}(C)$.
   - MACD signal: $\text{EMA}_9(\text{MACD})$.
   - RSI: 14-period Relative Strength Index.
   - Bollinger Bands ratios: $\text{LowerBand}_{20,2} / C_t$, $\text{UpperBand}_{20,2} / C_t$, $\text{MiddleBand}_{20} / C_t$.
7. **Exogenous Macro / Sentiment Covariates (3 features):**
   - Daily CBOE VIX close (lagged to $t-1$ calendar day).
   - Monthly Federal Funds effective rate (lagged to $t-1$ calendar month).
   - Daily Crypto Fear & Greed Index (lagged to $t-1$ calendar day).
8. **Categorical Temporal Embeddings (2 features):**
   - Hour of the day: $h_t \in \{0, \dots, 23\}$ mapped to learnable continuous embedding.
   - Day of the week: $w_t \in \{0, \dots, 6\}$ mapped to learnable continuous embedding.
   - Fixed sinusoidal positional encodings added to token representations.

All continuous real-valued variables are z-score normalized prior to input ingestion.

### Model Architecture and Hyperparameters (Table 12)

For the primary 5-minute GMADL Informer:
- Lookback window ($L_Q$): 28 bars (140 minutes).
- Forecast horizon: 1 step ahead (5 minutes).
- Model dimensionality ($d$): 256.
- Feed-forward network hidden dimensionality ($f$): 256.
- Multi-head attention heads ($h$): 2.
- Dropout rate: 0.01.
- Number of encoder layers ($L^{enc}$): 1.
- Number of decoder layers ($L^{dec}$): 3.
- Optimization algorithm: Adam, learning rate $\eta = 0.0001$, batch size 256.
- Training duration: 40 epochs with early stopping patience of 15 validation evaluations (evaluated every 300 batches).
- Objective loss: GMADL with $a = 100$ and $b = 2$.

### Strategy Execution and Position Selection (Equation 38)

Let $\hat{y}_t$ denote the Informer model's forward return forecast for interval $t$, formed at the close of interval $t-1$.
The strategy state $p_t \in \{-1, 0, 1\}$ (where $1 = \text{Long}$, $-1 = \text{Short}$, $0 = \text{Flat}$) is governed by four threshold hyperparameters $\theta_{GMADL} = (\text{enter\_long}, \text{exit\_long}, \text{enter\_short}, \text{exit\_short})$:

$$p_t = \begin{cases}
1 & \text{if } \hat{y}_t > \text{enter\_long} \\
0 & \text{if } \hat{y}_t < \text{exit\_long} \text{ and } p_{t-1} = 1 \\
-1 & \text{if } \hat{y}_t < \text{enter\_short} \\
0 & \text{if } \hat{y}_t > \text{exit\_short} \text{ and } p_{t-1} = -1 \\
p_{t-1} & \text{otherwise}
\end{cases}$$

If no condition triggers, the position persists via forward-fill: $p_t = p_{t-1}$. At evaluation end ($t = T$), position is liquidated to flat ($p_T = 0$).

### Selected In-Sample Threshold Values per Out-of-Sample Window (Table 18)

Hyperparameter search explored all 4,096 combinations over $[-0.007, 0.007]$ on the validation partition (maximizing Modified Information Ratio $\text{IR}^{**}$):

- **Window 1 (5min):** $\text{enter\_long} = +0.004$, $\text{exit\_long} = -$, $\text{enter\_short} = -0.005$, $\text{exit\_short} = -$ (direct reversal between long and short).
- **Window 2 (5min):** $\text{enter\_long} = +0.002$, $\text{exit\_long} = -$, $\text{enter\_short} = -0.001$, $\text{exit\_short} = -$.
- **Window 3 (5min):** $\text{enter\_long} = -$, $\text{exit\_long} = -$, $\text{enter\_short} = -0.006$, $\text{exit\_short} = +0.003$ (short-only / defensive cash regime during 2022 crypto winter).
- **Window 4 (5min):** $\text{enter\_long} = +0.002$, $\text{exit\_long} = -$, $\text{enter\_short} = -0.005$, $\text{exit\_short} = -$.
- **Window 5 (5min):** $\text{enter\_long} = +0.002$, $\text{exit\_long} = -$, $\text{enter\_short} = -0.003$, $\text{exit\_short} = -$.
- **Window 6 (5min):** $\text{enter\_long} = +0.001$, $\text{exit\_long} = -$, $\text{enter\_short} = -0.007$, $\text{exit\_short} = -$.

Symbol `"-"` indicates that the specific exit threshold is inactive; positions transition directly from long to short upon opposite entry signal, or hold prior state.

## Required data

- **Primary Instrument:** Bitcoin / Tether spot pair (`BTCUSDT`).
- **Venue:** Binance Spot Exchange (`https://www.binance.com`).
- **Timeframe:** 5-minute regular OHLCV candlestick intervals (comparative evaluations on 15-minute and 30-minute intervals).
- **Candlestick Fields:** `open_time`, `close_time`, `open`, `high`, `low`, `close`, `volume`.
- **Exogenous Datasets:**
  - CBOE VIX Index: Daily closing value (`https://www.cboe.com/tradable_products/vix/vix_historical_data/`).
  - Federal Reserve Effective Federal Funds Rate: Monthly rate (`https://fred.stlouisfed.org/series/FEDFUNDS`).
  - Alternative.me Crypto Fear & Greed Index: Daily index value (`https://alternative.me/crypto/fear-and-greed-index/`).
- **Point-in-Time Availability Alignment:**
  - High-frequency Binance bars: Observations up to interval $t-1$ are closed and fully accessible before forming the forecast for interval $t$.
  - Daily VIX and Fear & Greed values: Shifted by at least 1 full calendar day (e.g. observation on 2022-08-17 04:05 UTC uses index value published on 2022-08-16) to eliminate look-ahead bias regarding unknown intraday publication timestamps.
  - Monthly FEDFUNDS: Shifted to the prior completed calendar month.
- **Missing Data Treatment:** The authors identified 8 exchange maintenance gaps totaling ~101 hours (4.2 days, representing 0.2% of total bars across 5 years). Gaps were forward-filled by propagating the last observed price and volume.

## Execution assumptions

- **Signal-to-Order Timing:** Next-bar execution. When position state changes at interval $t$ (based on forecast generated from data through close of $t-1$), assets are transacted at the closing price of interval $t-1$ (the opening price of interval $t$).
- **Order Type:** Modeled as immediate execution at bar close price (effectively a market order executed at opening price of next candle).
- **Transaction Fees ($e$):** Fixed fee of $0.1\%$ (10 basis points) per trade, corresponding to Binance VIP0 standard spot maker/taker fee.
- **Position Reversal Penalty:** Flipping position directly from $+1$ (Long) to $-1$ (Short) is explicitly accounted as two distinct trades (closing long position and opening short position), incurring $2 \times 0.1\% = 0.2\%$ in transaction costs.
- **Portfolio Sizing:** All-or-nothing full allocation ($100\%$ portfolio equity in active position, or $0\%$ in cash/exit). No leverage or fractional Kelly sizing applied.
- **Shorting Mechanics:** Assumes symmetric short-selling capability on BTC/USDT without borrow fees, margin interest, or short-availability constraints.

## Evidence

### Source-reported

The primary empirical evidence is derived from 6 walk-forward out-of-sample testing windows spanning August 2021 to July 2024 (36 aggregate months, 311,040 test bars at 5-minute resolution). Performance metrics follow the canonical accounting of Michańków et al. (2022) and Kość et al. (2019):
- $\text{ARC} = (E_T / E_0)^{Y/T} - 1$ (Annualized Return Compounded, $Y_{5\text{m}} = 105,120$ intervals/year).
- $\text{ASD} = \text{std}(r) \times \sqrt{Y}$ (Annualized Standard Deviation).
- $\text{IR}^* = \text{ARC} / \text{ASD}$ (Information Ratio / zero-rf Sharpe).
- $\text{MD} = \max_{t} (\max_{\tau \le t} E_\tau - E_t) / \max_{\tau \le t} E_\tau$ (Maximum Drawdown).
- $\text{IR}^{**} = \text{ARC} \times \text{IR}^* / \text{MD}$ (Modified Information Ratio).

#### 1. Performance of Best Strategies Across Entire 3-Year Out-of-Sample Period (Figure 14)

| Strategy | End Value ($E_T$) | ARC (Ann. Return) | ASD (Ann. Vol) | $\text{IR}^*$ (Sharpe) | MD (Max DD) | $\text{IR}^{**}$ | Trades ($N$) | Long % | Short % |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **GMADL Informer (5 min)** | **9.747** | **115.9%** | **54.4%** | **2.129** | **32.7%** | **7.552** | **846** | **44.80%** | **41.51%** |
| RSI Strategy (30 min) | 4.542 | 66.8% | 46.2% | 1.444 | 39.9% | 2.415 | 377 | 30.79% | 28.03% |
| RSI Strategy (5 min) | 3.341 | 50.3% | 50.4% | 0.999 | 30.0% | 1.676 | 846 | 28.29% | 33.47% |
| GMADL Informer (15 min) | 3.296 | 49.6% | 52.7% | 0.942 | 47.4% | 0.987 | 362 | 49.37% | 37.72% |
| RMSE Informer (30 min) | 2.727 | 40.4% | 50.5% | 0.800 | 51.8% | 0.624 | 34 | 64.40% | 24.67% |
| GMADL Informer (30 min) | 2.263 | 31.8% | 36.7% | 0.866 | 53.3% | 0.516 | 811 | 35.51% | 19.59% |
| MACD Strategy (30 min) | 1.952 | 25.4% | 52.4% | 0.485 | 59.2% | 0.207 | 327 | 52.30% | 28.30% |
| RMSE Informer (15 min) | 1.509 | 14.9% | 34.9% | 0.428 | 45.5% | 0.140 | 16 | 15.24% | 27.60% |
| **Buy & Hold Benchmark** | **1.441** | **13.1%** | **57.7%** | **0.228** | **77.3%** | **0.039** | **2** | **100.00%** | **0.00%** |

#### 2. Statistical Significance vs Buy & Hold Benchmark (Table 19)

Probabilistic t-test for $H_0: \text{IR}_{\text{strategy}} \le \text{IR}_{\text{B\&H}}$ with test statistic $t = (\text{IR}_{\text{strat}} - \text{IR}_{\text{B\&H}}) / (\sigma / \sqrt{N})$:
- **GMADL Informer (5 min):** Sample size $N = 311,040$, $\sigma = 2.820834$, $t\text{-stat} = 375.84$, $p\text{-value} = 0.000000^{***}$ (null rejected at $p < 0.001$).
- **RSI Strategy (5 min):** $N = 311,040$, $\sigma = 0.648741$, $t\text{-stat} = 662.77$, $p\text{-value} = 0.000000^{***}$.
- **GMADL Informer (15 min):** $N = 103,680$, $\sigma = 0.558743$, $t\text{-stat} = 408.13$, $p\text{-value} = 0.000000^{***}$.
- **RSI Strategy (30 min):** $N = 51,840$, $\sigma = 1.065079$, $t\text{-stat} = 258.49$, $p\text{-value} = 0.000000^{***}$.

#### 3. Subperiod Window Breakdown for 5-Minute GMADL Informer (Figure 13)

- **Window 1 (late 2021 bull/top):** Outperformed Buy & Hold with steady positive accumulation.
- **Window 2 (first half 2022 bear crash):** Top performance; captured major downward moves via short positioning ($N$ trades highest in this window).
- **Window 3 (second half 2022 post-FTX consolidation):** Achieved highest relative efficiency with only 16 trades; remained in cash/flat for $80\%$ of the period and executed selective short entries.
- **Windows 4 & 5 (2023 recovery and accumulation):** Outperformed Buy & Hold with reduced drawdowns.
- **Window 6 (early-mid 2024 ETF-driven bull run):** Buy & Hold proved superior; GMADL Informer lagged benchmark during uninterrupted vertical rally due to fee friction and inactive long exposure.

#### 4. Frequency Scaling Law

The source documents an empirical divergence between loss functions when moving to higher frequencies:
- **GMADL Informer performance scales monotonically with sampling frequency:**
  - 30-minute: $\text{ARC} = 31.8\%$, $\text{IR}^* = 0.866$, $\text{MD} = 53.3\%$, $\text{IR}^{**} = 0.516$
  - 15-minute: $\text{ARC} = 49.6\%$, $\text{IR}^* = 0.942$, $\text{MD} = 47.4\%$, $\text{IR}^{**} = 0.987$
  - 5-minute: $\text{ARC} = 115.9\%$, $\text{IR}^* = 2.129$, $\text{MD} = 32.7\%$, $\text{IR}^{**} = 7.552$
- **RMSE Informer degrades monotonically with sampling frequency:**
  - 30-minute: $\text{ARC} = 40.4\%$, $\text{IR}^{**} = 0.624$ ($N = 34$)
  - 15-minute: $\text{ARC} = 14.9\%$, $\text{IR}^{**} = 0.140$ ($N = 16$)
  - 5-minute: Complete collapse; predictions cluster near zero ($< 0.1\%$ fee threshold), generating only 16 trades over 3 years.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Quantile Loss Informer Failure:** Across all three frequencies (5m, 15m, 30m), the Informer trained with Quantile Loss failed to outperform Buy & Hold. In 5-minute data, Quantile Informer executed excessive trades, resulting in severe capital erosion from transaction fees. In 15-minute data, it was constrained to holding a position only 40% of the time.
2. **RMSE Incompetence at High Frequencies:** Training deep sequence models with quadratic distance loss (RMSE) on high-frequency cryptocurrency data results in an inability to trigger trades when transaction fees are non-zero.
3. **Regime Vulnerability in Parabolic Bull Trends:** In Window 6 (2024 ETF approval bull market), Buy & Hold achieved higher cumulative return than all tested algorithmic strategies. Active strategies suffer when the asset exhibits persistent unilateral upward drift with low intraday retracement.
4. **Spot Short-Selling Borrow Cost Omission:** The backtest assumes costless short positions ($41.51\%$ of holding intervals in 5-minute GMADL). On Binance Spot Margin, borrowing BTC incurs interest rates ranging from $5\%$ to over $15\%$ APR, which would reduce the reported return.
5. **Sensitivity to Window Partitioning (Section 6.2):** Retraining the 5-minute GMADL Informer on 3 windows or 12 windows instead of 6 windows reduced $\text{IR}^{**}$, indicating that the exact choice of rolling step size influences stability.

## Falsification plan

To falsify the hypothesis that 5-minute GMADL Informer extracts genuine predictive alpha from Bitcoin high-frequency dynamics:

1. **Post-Sample Holdout Test (Out-of-Sample Failure):**
   - *Test:* Run the frozen 5-minute GMADL Informer model on Binance BTC/USDT spot and BTCUSDT perpetual data from August 2024 to September 2026.
   - *Failure Criterion:* Net annualized Sharpe ratio $< 0.5$ or Maximum Drawdown $> 45\%$ after accounting for 10 bps fees.
2. **Transaction Cost and Slippage Degradation Boundary:**
   - *Test:* Increase execution fees and slippage incrementally: $e \in \{0.05\%, 0.10\%, 0.15\%, 0.20\%\}$.
   - *Failure Criterion:* If net returns turn negative at $e \le 0.12\%$, the reported performance is an artifact of the fee assumption rather than a robust statistical edge.
3. **Margin Borrow / Perpetual Funding Drag Audit:**
   - *Test:* For the $41.51\%$ short-holding intervals, apply historical Binance Margin BTC borrow rates (or 8-hour perpetual funding payments).
   - *Failure Criterion:* Net cumulative PnL degradation exceeding $35\%$ of total gain indicates the strategy is not viable as a cash-market system without perpetual margin funding.
4. **Placebo / Label Shuffle Audit:**
   - *Test:* Randomly permute forward return labels within each training window while preserving input feature auto-correlation, train the GMADL Informer, and evaluate out-of-sample.
   - *Failure Criterion:* If the shuffled-label model achieves an out-of-sample Modified Information Ratio within $25\%$ of the unshuffled model, the predictive mechanism is uninformative.
5. **Cross-Asset Portability Failure:**
   - *Test:* Apply the identical Informer GMADL architecture and hyperparameter pipeline to ETH/USDT and SOL/USDT 5-minute spot data.
   - *Failure Criterion:* Negative net Sharpe ratio or failure to beat Buy & Hold across multiple rolling windows.

## Crypto portability

- **Classification:** `direct`. The primary source was empirically developed and evaluated directly on Binance cryptocurrency spot data (`BTCUSDT`).
- **Spot vs Perpetual Implementation:**
  - *Spot Limitations:* On spot exchanges, short exposure requires borrowing asset collateral through margin accounts, introducing borrowing interest, liquidation thresholds, and margin maintenance requirements that were omitted from the paper's spot simulation.
  - *Perpetual Futures Adaptation:* Porting the strategy to USDT-margined perpetual futures (`BTCUSDT PERP`) is direct and economically superior: perpetuals allow symmetric linear shorting without borrow friction, offer lower fee schedules (e.g. 2 to 5 bps taker fees vs 10 bps spot), and deep order-book liquidity.
  - *Perpetual Funding Rate Dynamics:* Holding short positions for $41.51\%$ of the time in perpetuals means the strategy earns funding cash flow during contango regimes (typical in crypto bull phases) and pays funding during backwardation.
- **Latency and Candle Boundaries:** At a 5-minute resolution, computational inference latency for Informer ($< 500\text{ ms}$ on GPU/CPU) easily fits within the bar formation window. However, entering at the exact bar close price assumes negligible slippage; realistic deployment requires limit-order queuing or conservative taker slippage modeling.

## Limitations

1. **Synthetic Gap Imputation:** Forward-filling ~101 hours of exchange outages propagates zero-return bars that artificially lower volatility during maintenance regimes.
2. **Single-Pair Asset Scope:** The study exclusively tests `BTCUSDT`; cross-sectional interaction across digital assets is not examined.
3. **Omission of Bid-Ask Spread and Market Impact:** Trades are executed at the close price of bar $t-1$. In volatile market conditions, aggressive market orders pay half the bid-ask spread and incur market impact that can exceed 2-5 bps.
4. **Heavy Computational Retraining Barrier:** Training an Informer instance across rolling windows requires substantial compute time (~1 hour per run on an Nvidia GTX 1080Ti for 30 sampled combinations out of 1.16M hyperparameter candidates). Full walk-forward re-estimation with hyperparameter refits is computationally burdensome.
5. **Macro Variable Latency:** Daily VIX and Fear & Greed values were lagged by 1 full day; while leakage-safe, this introduces stale macro context during rapid weekend crypto dislocations.

## Implementation status

- **Status:** `not-implemented`.
- No prototype or production pipeline currently exists in NautilusTrader or PyBroker.
- No model weights or automated execution sidecars have been instantiated.

## Adoption boundary

- **Scope:** `research-only`.
- **Adoption:** `not-approved`.
- This document captures normalized research from external literature. It does not constitute approval for live trading, testnet allocation, paper trading, or portfolio inclusion.

## Related Wiki records

- `crypto-perpetual-lob-explainable-catboost-gmadl-microstructure-2026-09-01.md`: Investigates GMADL loss applied to CatBoost gradient boosting over 1-second Binance Futures LOB depth and trade flow features.
- `crypto-hourly-bitcoin-walk-forward-cost-aware-execution-2026-09-01.md`: Studies machine learning models (XGBoost, LSTM, iTransformer) on hourly BTC/USDT with cost-aware magnitude thresholding.
- `cross-asset-futures-vsn-xlstm-sharpe-optimal-portfolio-2026-09-03.md`: Explores end-to-end Sharpe ratio optimization in modern xLSTM sequence architectures.
- `rsi-mean-reversion_ohlcv-2026-08-31.md`: Traditional technical indicator benchmark compared in this source.
- `macd-trend_ohlcv-2026-08-31.md`: Moving Average Convergence Divergence benchmark compared in this source.

## Sources

1. Filip Stefaniuk and Robert Ślepaczuk, *"Informer In Algorithmic Investment Strategies on High Frequency Bitcoin Data"*, arXiv:2503.18096v1 [q-fin.CP, cs.LG, q-fin.TR], March 24, 2025. DOI: [10.48550/arXiv.2503.18096](https://doi.org/10.48550/arXiv.2503.18096).
2. Primary Source Code Repository: GitLab `https://gitlab.com/FilipStefaniuk/wne-msc-thesis.git`, immutable commit SHA `0ded87a0fb099ffa669a222ed648fbf81ad2d022`.
3. Haoyi Zhou, Shanghang Zhang, Jieqi Peng, Shuai Zhang, Jianxin Li, Hui Xiong, Wancai Zhang, *"Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting"*, *Proceedings of the AAAI Conference on Artificial Intelligence* 35(12), 2021, pp. 11106-11115, arXiv:2012.07436.
4. Jakub Michańków, Paweł Sakowski, Robert Ślepaczuk, *"Mean Absolute Directional Loss as a new loss function for machine learning problems in algorithmic investment strategies"*, *Journal of Computational Science* 81, 2024, 102375, DOI: [10.1016/j.jocs.2024.102375](https://doi.org/10.1016/j.jocs.2024.102375).
5. Jakub Michańków, Paweł Sakowski, Robert Ślepaczuk, *"LSTM in Algorithmic Investment Strategies on BTC and S&P500 Index"*, *Sensors* 22(3), 2022, 917, DOI: [10.3390/s22030917](https://doi.org/10.3390/s22030917).
6. Krzysztof Kość, Paweł Sakowski, Robert Ślepaczuk, *"Momentum and contrarian effects on the cryptocurrency market"*, *Physica A: Statistical Mechanics and its Applications* 523, 2019, pp. 691-701, DOI: [10.1016/j.physa.2019.02.057](https://doi.org/10.1016/j.physa.2019.02.057).
