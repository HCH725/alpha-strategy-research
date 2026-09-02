---
schema: strategy-research-record-v1
title: "Cross-Asset Futures Multi-Horizon Trend Following with Hybrid VSN-LSTM and xLSTM Architectures Under End-to-End Sharpe Ratio Optimization"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-asset
  - futures
  - deep-learning
  - trend-following
  - vlstm
  - xlstm
  - sharpe-optimization
  - risk-adjusted-alpha
status: research-only
confidence: high
source_as_of: 2026-03-02
sources:
  - "Adir Saly-Kaufmann, Kieran Wood, Jan-Peter Calliess, Stefan Zohren, 'Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance', arXiv:2603.01820v1 [q-fin.TR, cs.LG], March 2, 2026. DOI: 10.48550/arXiv.2603.01820. Stable URL: https://arxiv.org/abs/2603.01820. Full-text HTML: https://arxiv.org/html/2603.01820."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Asset Futures Multi-Horizon Trend Following with Hybrid VSN-LSTM and xLSTM Architectures Under End-to-End Sharpe Ratio Optimization

## Provenance

- **Primary Source:** Adir Saly-Kaufmann, Kieran Wood, Jan-Peter Calliess, and Stefan Zohren (Department of Engineering Science & Oxford-Man Institute of Quantitative Finance, University of Oxford), *"Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance"*, arXiv preprint `arXiv:2603.01820v1 [q-fin.TR, cs.LG]`, submitted March 2, 2026.
- **Canonical DOI:** [10.48550/arXiv.2603.01820](https://doi.org/10.48550/arXiv.2603.01820)
- **Traceable Source URLs:** [https://arxiv.org/abs/2603.01820](https://arxiv.org/abs/2603.01820) | Full text HTML: [https://arxiv.org/html/2603.01820](https://arxiv.org/html/2603.01820)
- **Primary Subject Classifications:** Trading and Market Microstructure (`q-fin.TR`), Machine Learning (`cs.LG`).
- **Data & Universe:** Pinnacle Data Continuous Linked Contracts (CLC), comprising 65 continuous futures contracts across 5 asset classes (Bonds, Commodities, Energies, Foreign Exchange, and Equity Indices) spanning 2010 to 2025 (15 years). Continuous contracts are back-adjusted using a ratio-adjusted backwards methodology to remove roll-induced price discontinuities.
- **Evaluation Splits:** Rolling-window retrain scheme every 5 years; validation set uses the last 10% of each training window; evaluation conducted across out-of-sample periods from 2010 to 2025 (including subperiods 2010–2015, 2015–2020, 2020–2025, and 2015–2025).

## Economic mechanism

### Source-reported

Financial return series are characterized by heavy-tailed distributions, low signal-to-noise ratios, pronounced non-stationarity, and time-varying regime shifts. While generic deep learning and linear time-series baselines (such as DLinear, NLinear, and PatchTST) dominate standard physical benchmarks (e.g., weather, electricity, traffic), they struggle in financial applications because those domains feature high signal-to-noise ratios and strong seasonal regularity.

The authors propose that effective financial forecasting requires three specific architectural properties:
1. **Denoising and Feature Conditioning:** Dynamically filtering out transient high-frequency noise and weighting relevant predictors at each time step via Variable Selection Networks (VSN);
2. **Asset-Specific and Regime-Aware Representation Learning:** Capturing cross-asset heterogeneity through learned ticker embeddings without prematurely forcing cross-sectional feature mixing;
3. **Adaptive Memory and Persistent State Evolution:** Retaining rare, economically meaningful directional signals across non-stationary regimes without premature forgetting or sigmoid gate saturation.

The empirical benchmark demonstrates that:
- Linear models (AR1x, ARnnx, DLinear, NLinear) fail to maintain consistent out-of-sample Sharpe ratios across regimes, collapsing in low-volatility and transitional periods.
- Non-recurrent Transformer architectures (e.g., iTransformer) suffer from severe under-reactivity, resulting in minimal turnover but poor risk-adjusted returns (Sharpe 0.35).
- Recurrent sequence models with structural inductive biases excel:
  - **VLSTM (VSN + LSTM):** Combines feature-level nonlinear gating with recurrent memory, achieving the highest overall out-of-sample Sharpe ratio (2.39, 2010–2025) and highest information ratio relative to passive buy-and-hold (0.85).
  - **xLSTM (Extended LSTM):** Introduces exponential gating and matrix-valued associative memory ($C_t \in \mathbb{R}^{d \times d}$), achieving a 50% reduction in turnover (482 vs. 966 for VLSTM) and delivering the largest portfolio-level breakeven transaction cost buffer.
  - **LPatchTST (LSTM + PatchTST):** Employs an LSTM as a temporal channel-wise denoiser prior to patch self-attention, achieving the lowest maximum drawdown (-17.4%) and maintaining strictly positive Sharpe ratios in every single calendar year from 2010 to 2024 (minimum annual Sharpe +0.51).

### Research interpretation

The core falsifiable hypothesis is: **In cross-asset multi-horizon futures trend following, direct end-to-end maximization of a differentiable Sharpe ratio over pooled return batches produces superior risk-adjusted alpha only when paired with architectural inductive biases that enforce soft input feature selection (VSN) and persistent, non-saturating recurrent state memory (LSTM / xLSTM). Without these inductive biases, linear models underfit regime shifts, while unconstrained attention mechanisms overfit to transient noise.**

The system operates as an end-to-end multi-component quantitative strategy:
```text
Raw Daily Prices (65 continuous futures contracts)
  ↓
Feature Engineering: 6 multi-horizon normalized returns + 3 normalized MACD signals (9 features)
  ↓
Dynamic Feature Gating: Variable Selection Network (VSN) with Gated Linear Units (GLU)
  ↓
Temporal Memory Encoder: Recurrent State Backbone (LSTM, xLSTM, or LPatchTST) + Ticker Embedding
  ↓
Projection Head: Linear layer + Hyperbolic Tangent (tanh) -> Conviction Signal ŷ_{t,k} ∈ [-1, 1]
  ↓
Risk Equalizer: Ex-ante EWMA Volatility Targeting -> Leverage Factor vs_factor_{t,k} = 1 / σ_{t,k}
  ↓
Portfolio Construction: Target weight w_{t,k} = (σ_tgt / √K) · ŷ_{t,k} · (1 / σ_{t,k})
  ↓
Ensemble Layer: Average positions of top S validation seeds to suppress turnover churn
```

Economic drivers:
- **Trend Persistence Across Multiple Horizons:** Captures momentum at short (1-day, 1-week), intermediate (1-month, 3-month), and long (6-month, 1-year) horizons simultaneously.
- **Dynamic Feature Selection (VSN):** Financial features fluctuate in predictive value; VSN suppresses uninformative or noisy inputs on a time-step-by-time-step basis.
- **Volatility Targeting and Risk Parity:** Equalizes risk contributions across volatile commodities (e.g., Natural Gas) and low-volatility fixed income (e.g., Euro Schatz), preventing high-volatility assets from dominating portfolio variance.
- **End-to-End Objective Alignment:** Optimizing directly for portfolio Sharpe ratio circumvents the misalignment between statistical loss functions (MSE/MAE) and risk-adjusted economic profit.

## Signal

### 1. Input Features ($d = 9$ continuous features per asset $k$ at time $t$)

All features are constructed strictly from historical closing prices $P_{t, k}$:

1. **Normalized Returns over 6 Horizons:**
   $$r^{\text{norm}}_{t, h} = \frac{r_{t, h}}{\sigma_t \sqrt{h}}, \quad h \in \{1, 5, 21, 63, 126, 252\} \text{ trading days}$$
   where $r_{t, h} = \frac{P_t - P_{t-h}}{P_{t-h}}$ and $\sigma_t$ is the ex-ante EWMA volatility.

2. **Volatility-Normalized MACD Momentum Signals across 3 Timescale Pairs:**
   For $(T_s, T_l) \in \{(8, 24), (16, 48), (32, 96)\}$:
   $$\text{MACD}_t = \text{EWMA}_{h(T_s)}(P)_t - \text{EWMA}_{h(T_l)}(P)_t$$
   $$q_t = \frac{\text{MACD}_t}{\text{Std}_{63}(P)_t}$$
   $$\text{Signal}_t = \frac{q_t}{\text{Std}_{252}(q)_t}$$
   where $\text{Std}_W(x)_t$ denotes the rolling sample standard deviation over window $W$.

3. **Asset Identification:**
   A learned categorical ticker embedding vector $e_k \in \mathbb{R}^H$ is provided for each asset to capture instrument-specific dynamics.

### 2. Ex-Ante Volatility Estimation & Scaling

Daily conditional mean $\mu_t$ and conditional variance $\sigma_t^2$ are updated via an Exponentially Weighted Moving Average (EWMA):
$$\mu_t = \lambda r_t + (1 - \lambda) \mu_{t-1}$$
$$\sigma_t^2 = \lambda (r_t - \mu_t)^2 + (1 - \lambda) \sigma_{t-1}^2, \quad \lambda = \frac{2}{\text{span} + 1}$$
*(Note: The exact numerical integer for `span` is omitted in the primary source text, representing a provenance gap; standard quantitative literature uses 60 days).*

The time-varying leverage factor is:
$$\text{vs\_factor}_{t, k} = \frac{1}{\sigma_{t, k}}$$

### 3. Architecture Specification

- **Lookback Window:** Sequence length $L = 84$ trading days (approx. 4 calendar months) for recurrent and VSN models; $L = 512$ for patch models.
- **Variable Selection Network (VSN):**
  Given input vector $x_t \in \mathbb{R}^d$:
  $$\tilde{v}_t^{(i)} = \text{GLU}(W_v x_t^{(i)} + b_v), \quad i \in \{1, \dots, d\}$$
  $$v_t = \text{Softmax}(W_g x_t + b_g) \in \mathbb{R}^d$$
  $$\tilde{x}_t = \sum_{i=1}^d v_t^{(i)} \tilde{v}_t^{(i)}$$
- **Recurrent Temporal Encoder:**
  Processes $\{\tilde{x}_t\}_{t=1}^L$ to extract terminal hidden state $h_t \in \mathbb{R}^H$:
  - *VLSTM:* Classical LSTM recurrence with additive memory cells and sigmoid forget/input gates.
  - *xLSTM:* Extended LSTM with exponential gating, running-max log-domain stabilization, and matrix-valued associative memory ($C_t \in \mathbb{R}^{H \times H}$) updated via key-value outer products $v_t k_t^\top$.
- **Unified Projection Head:**
  $$\hat{y}_{t, k} = \tanh(w_{\text{lin}}^\top h_t + b_{\text{lin}}) \in [-1, 1]$$
  where $\hat{y}_{t, k}$ represents directional conviction (bounded between -1.0 full short and +1.0 full long).

### 4. Portfolio Allocation & Position Sizing

For a universe of $K$ active assets, target portfolio volatility $\sigma_{\text{tgt}} = 10\%$ (0.10 annualized):
$$w_{t, k} = \frac{\sigma_{\text{tgt}}}{\sqrt{K}} \cdot \hat{y}_{t, k} \cdot \frac{1}{\sigma_{t, k}}$$

Daily gross portfolio return at $t+1$:
$$R_{t+1}^{\text{port}} = \frac{1}{K} \sum_{k=1}^K w_{t, k} \cdot r_{t+1, k}$$

### 5. Training Objective (Differentiable Sharpe Ratio Loss)

Parameters $\theta$ are optimized end-to-end by minimizing the negative annualized Sharpe ratio computed over pooled batch return sequences $\mathbf{R}^{\text{port}} = \{R_1^{\text{port}}, \dots, R_T^{\text{port}}\}$:
$$\mathcal{L}(\theta) = - \frac{\hat{\mathbb{E}}[R]}{\sqrt{\widehat{\text{Var}}[R] + \epsilon}} \cdot \sqrt{252}$$
where $\epsilon = 10^{-6}$ for numerical stability.

### 6. Top-Seed Ensembling

To suppress high-frequency weight oscillations and reduce transaction costs, predictions are ensembled over the top $S$ seeds based on validation loss (top 10 of 50 runs in primary benchmark; top 5 of 25 in reduced budget):
$$\bar{w}_{t, k} = \frac{1}{S} \sum_{s=1}^S w_{t, k}^{(s)}$$

## Required data

- **Instruments:** 65 continuous futures contracts covering 5 major sectors:
  - *Fixed Income (Bonds):* US 2Y Note, US 5Y Note, US 10Y Note, US T-Bond, Euro Bund, Euro Bobl, Euro Schatz, UK Gilt Long, Canada 10Y Bond.
  - *Equity Indices:* S&P 500 mini, Nasdaq mini, Russell 2000 mini, Mini Dow, S&P 400 mini, Euro Stoxx 50, STOXX 50, FTSE 100, CAC 40, Nikkei 225, Hang Seng.
  - *Currencies (FX):* US Dollar Index, EUR, GBP, JPY, AUD, CAD, CHF, MXN, CAD/JPY, NOK/USD, USD/NZD, USD/SEK, USD/SGD.
  - *Commodities:* Gold, Silver, Copper, Platinum, Palladium, Corn, Soybeans, Soybean Oil, Soybean Meal, Wheat (KC, Minneapolis, Chicago), Rough Rice, Oats, Cotton No. 2, Sugar No. 11, Cocoa, Coffee, Orange Juice, Feeder Cattle, Live Cattle, Lean Hogs, Milk III, Lumber, Goldman Sachs Commodity Index, CRB Index.
  - *Energies:* Light Crude Oil, Brent Crude Oil, Brent Gasoil, RBOB Gasoline, Natural Gas.
- **Roll Schedule & Stitching:** Continuous contracts ratio-adjusted backwards from expiration dates to eliminate roll jumps.
- **Timeframe:** Daily bars (1-day resolution).
- **Price Fields:** Daily Close ($P_t$).
- **Lookback Requirements:** Minimum burn-in of 252 days for 1-year momentum normalization and MACD standard deviation calculations; sequence window length $L = 84$ days.
- **Missing Data Handling:** If an instrument is not actively trading or halted, its active weight allocation is set to zero ($K$ adjusted to active tradable count).

## Execution assumptions

- **Execution Cadence:** Daily rebalancing at the close of day $t$; position held over $(t, t+1)$ to earn return $r_{t+1}$.
- **Order Type:** Market-on-Close (MOC) or Next-Day Market Open.
- **Optimization Frictions:** Primary models trained with zero explicit friction ($c_k = 0$) to measure raw predictive edge, with friction resilience evaluated post-hoc via breakeven cost analysis ($c_k^*$).
- **Leverage & Margining:** Dynamic leverage induced by $1 / \sigma_t$; portfolio total gross market value (GMV) floats to achieve the constant $10\%$ annualized portfolio volatility target.
- **Shorting:** Fully symmetric long and short positions allowed ($w_{t, k} \in [-\infty, +\infty]$, with conviction bounded by $\tanh \in [-1, 1]$).
- **Ensemble Filtering:** Top-10 seed ensembling acts as a natural turnover low-pass filter, cutting execution churn substantially without sacrificing signal fidelity.

## Evidence

### Source-reported

All figures below are transcribed directly from the primary source (Saly-Kaufmann, Wood, Calliess, Zohren, arXiv:2603.01820v1, Tables 1, 2, 3, 4, 9, 10, and 11) over the 15-year out-of-sample test window (2010–2025), evaluated under a 10% annualized volatility target ($\sigma_{\text{tgt}} = 0.10$):

#### 1. Full-Sample Gross Performance & Statistical Diagnostics (2010–2025, Table 2)

| Model | CAGR | Ann. Return | Sharpe Ratio | $t$-stat (HAC) | Hit Rate | Turnover | xGMV | Info. Ratio | $t$ (HAC) vs Passive | Corr. vs Passive |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Passive Buy & Hold** | 0.0435 | 0.0476 | 0.48 | 1.65 | 0.531 | – | – | – | – | – |
| **AR1x** | 0.0813 | 0.0831 | 0.83 | 3.12 | 0.539 | 353.64 | 90.421 | -0.0086 | -0.0305 | 0.3533 |
| **ARnnx** | 0.0646 | 0.0677 | 0.68 | 2.52 | 0.538 | 280.66 | 69.525 | -0.0829 | -0.3011 | 0.4325 |
| **DLinear** | 0.0750 | 0.0773 | 0.77 | 2.87 | 0.539 | 278.41 | 75.282 | 0.0141 | 0.0501 | 0.2612 |
| **NLinear** | 0.066 | 0.068 | 0.66 | – | – | – | – | – | – | – |
| **LSTM** | 0.1351 | 0.1318 | 1.32 | 4.56 | 0.554 | 948.08 | 225.769 | -0.0637 | -0.2303 | 0.2816 |
| **VLSTM (VSN+LSTM)** | **0.2632** | **0.2388** | **2.39** | **8.81** | **0.588** | 966.86 | 218.369 | **0.8539** | **3.3071** | 0.4042 |
| **Mamba2** | 0.0587 | 0.0620 | 0.62 | 2.31 | 0.546 | 233.00 | 58.164 | -0.0901 | -0.3246 | 0.2220 |
| **VSN+Mamba2** | 0.0967 | 0.0973 | 0.97 | 3.65 | 0.555 | 329.11 | 78.842 | 0.1091 | 0.3936 | 0.2821 |
| **PatchTST** | 0.0847 | 0.0864 | 0.86 | 3.29 | 0.541 | 623.88 | 198.021 | -0.2149 | -0.7848 | 0.5530 |
| **LPatchTST** | 0.2550 | 0.2323 | 2.32 | 8.81 | 0.577 | 959.89 | 211.514 | 0.7070 | 2.7470 | 0.3471 |
| **PsLSTM** | 0.1868 | 0.1763 | 1.76 | 6.83 | 0.563 | 823.07 | 185.496 | 0.3981 | 1.5410 | 0.4862 |
| **TFT** | 0.2398 | 0.2201 | 2.20 | 8.13 | 0.584 | 912.81 | 223.231 | 0.6665 | 2.5487 | 0.3888 |
| **VxLSTM** | 0.1937 | 0.1821 | 1.82 | 6.89 | 0.574 | 775.88 | 159.438 | 0.4666 | 1.6727 | 0.5069 |
| **xLSTM** | 0.1937 | 0.1796 | 1.80 | 6.85 | 0.568 | **482.62** | **91.924** | 0.7984 | 2.9042 | 0.6274 |
| **iTransformer** | 0.0308 | 0.0353 | 0.35 | 1.26 | 0.529 | 36.32 | 9.203 | -0.1539 | -0.5563 | 0.4855 |

#### 2. Downside Risk & Tail Behavior (Table 3)

| Model | Max Drawdown | Calmar Ratio | Worst 3m Sharpe | Min Annual Sharpe | CVaR 5% |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **AR1x** | -0.167 | 0.49 | -3.92 | -0.59 | 0.0147 |
| **ARnnx** | -0.206 | 0.31 | -4.52 | -0.90 | 0.0148 |
| **DLinear** | -0.180 | 0.42 | -4.93 | -0.94 | 0.0149 |
| **LSTM** | -0.342 | 0.40 | -5.15 | -1.51 | 0.0143 |
| **VLSTM** | -0.229 | 1.15 | -3.68 | -0.10 | 0.0137 |
| **Mamba2** | -0.263 | 0.22 | -4.06 | -0.71 | 0.0149 |
| **VSN+Mamba2** | -0.163 | 0.59 | -4.00 | -0.63 | 0.0148 |
| **PatchTST** | -0.176 | 0.48 | -5.58 | -1.21 | 0.0151 |
| **LPatchTST** | -0.174 | 1.47 | -3.91 | **+0.51** | **0.0136** |
| **PsLSTM** | -0.131 | 1.43 | -3.80 | -0.40 | 0.0143 |
| **TFT** | -0.232 | 1.03 | -3.87 | -0.14 | 0.0141 |
| **VxLSTM** | **-0.118** | **1.64** | -3.70 | -1.31 | 0.0139 |
| **xLSTM** | -0.141 | 1.35 | **-3.57** | -0.28 | 0.0141 |
| **Passive** | -0.308 | 0.14 | -6.11 | -1.53 | 0.0144 |
| **iTransformer** | -0.264 | 0.12 | -3.93 | -1.16 | 0.0154 |

#### 3. Subperiod Out-of-Sample Sharpe Ratios (Table 1)

| Strategy | 2010–2025 | 2015–2025 | 2010–2015 | 2015–2020 | 2020–2025 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **AR1x** | 0.77 | 0.70 | 0.74 | 0.06 | 1.35 |
| **DLinear** | 0.64 | 0.64 | 0.60 | 0.00 | 1.28 |
| **LSTM** | 1.48 | 1.33 | 1.83 | 1.60 | 1.07 |
| **VLSTM** | **2.40** | **2.25** | **2.57** | **2.61** | **1.88** |
| **LPatchTST** | 2.31 | 2.22 | 2.33 | 2.11 | 2.34 |
| **TFT** | 2.27 | 2.08 | 2.47 | 2.08 | 2.08 |
| **xLSTM** | 1.79 | 1.84 | 1.46 | 1.68 | 1.99 |
| **Mamba2** | 0.78 | 0.86 | 0.54 | 0.18 | 1.54 |

#### 4. Breakeven Cost & Turnover Efficiency (Tables 9 & 10)

- **xLSTM Implementation Efficiency:** xLSTM generates a turnover of 482.62, representing a 50.1% reduction relative to VLSTM (966.86) and classical LSTM (948.08). On high-liquidity instruments such as the S&P 500 mini (ES), xLSTM produces an annual turnover of only 26.01 and a breakeven cost of $19.25\text{ bps}$, compared to VLSTM's $8.1\text{ bps}$.
- **VLSTM Breadth:** VLSTM delivers broader positive alpha across the universe, with top agricultural contracts (Lumber LB: $30.84\text{ bps}$; Oats ZO: $24.13\text{ bps}$; Milk III DA: $22.04\text{ bps}$) exhibiting high gross profitability.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Failure of Linear and Non-Recurrent Attention Models:** Neither linear autoregression (AR1x, ARnnx, DLinear) nor pure attention (iTransformer) generated statistically significant positive information ratios relative to a passive benchmark. In fact, AR1x (IR -0.0086), ARnnx (IR -0.0829), and iTransformer (IR -0.1539) lagged buy-and-hold on an excess risk-adjusted basis.
- **Drawdown Vulnerability of Standard LSTM:** Without VSN feature selection or exponential gating, standard LSTM suffered a severe maximum drawdown of -34.2% and a minimum annual Sharpe of -1.51, confirming that vanilla recurrent units easily overfit during non-trending, choppy regimes.
- **Selective State-Space Model Instability:** Mamba2 failed to outperform basic recurrent models (aggregate Sharpe 0.62), underperforming even DLinear (0.77) over the full 2010–2025 window unless supplemented by explicit VSN feature selection (VSN+Mamba2 Sharpe 0.97).
- **Liquid Bond Squeeze:** Liquid interest-rate futures (e.g., US 2Y Note TU, Euro Schatz UZ) showed very low breakeven thresholds ($c^* < 2\text{ bps}$), indicating that standard retail commissions and execution slippage would erode alpha on short-term rates.

## Falsification plan

1. **Out-of-Sample Rolling Stress Test (2025–2027 data):**
   - *Test:* Run frozen VLSTM and xLSTM architectures on forward out-of-sample futures data.
   - *Threshold / Decision Rule:* Annualized Sharpe ratio must remain $\ge 1.20$, and maximum drawdown must not exceed $-25\%$. If Sharpe falls below 0.80 across any 24-month rolling period, the alpha persistence hypothesis is falsified.
2. **VSN Feature Selection Ablation Test:**
   - *Test:* Strip the Variable Selection Network from VLSTM and feed raw concatenated 9-feature vectors directly into the LSTM backbone.
   - *Threshold / Decision Rule:* If full-sample Sharpe ratio does not degrade by at least $\Delta \text{SR} \ge 0.50$ (moving from 2.39 toward vanilla LSTM's 1.32), the hypothesis that dynamic feature gating provides the critical denoising edge is rejected.
3. **Temporal Placebo / Shuffled-Sequence Test:**
   - *Test:* Shuffle temporal bar sequences within each lookback window while preserving cross-sectional correlation.
   - *Threshold / Decision Rule:* Sharpe ratio must collapse to $|\text{SR}| < 0.25$. Any non-trivial profitability under shuffled temporal order indicates look-ahead bias or data leakage.
4. **Transaction Cost Haircut Sensitivity:**
   - *Test:* Impose realistic tiered transaction costs (1.0 bps for liquid FX/indices, 3.0 bps for energies/metals, 8.0 bps for agricultural futures).
   - *Threshold / Decision Rule:* If portfolio net Sharpe drops below 1.20 for VLSTM or below 1.30 for xLSTM, the strategy is deemed unviable for production deployment.

## Crypto portability

**Portability Status:** `adapted` / `unproven`.

The primary research paper was conducted exclusively on traditional cross-asset continuous futures (commodities, FX, fixed income, equity indices). The authors provide no empirical evidence on cryptocurrency markets.

Key portability challenges and adaptation requirements:
1. **24/7 Session Boundaries & Volatility Scaling:** Traditional futures trade in discrete weekday sessions with defined closes. Crypto perpetuals trade continuously (24/7/365). Volatility targeting ($\sigma_{t, k}$) and MACD indicators must be adapted to rolling 24-hour UTC windows rather than standard 252-day annualization constants ($\sqrt{365}$ scaling required).
2. **Perpetual Funding Rate Drag:** Traditional futures contain embedded term structure / basis roll costs. Crypto perpetuals incur 8-hourly funding payments between longs and shorts. Prolonged one-sided momentum positioning during bull/bear runs can incur substantial funding drag that erodes gross trend alpha.
3. **Liquidation Wicks & Extreme Tail Risk:** Crypto assets display significantly higher kurtosis and frequent flash crashes / liquidation cascades compared to traditional futures. While the paper's target clipping ($\pm 20 \sigma$) stabilizes training, real execution in crypto requires hard stop-loss circuit breakers to prevent liquidation under volatility-targeted leverage.
4. **Universe Liquidity Gate:** Porting requires filtering down to top 20–30 liquid perpetual contracts (e.g., Binance / Bybit / Hyperliquid perpetuals) with strict minimum 24-hour turnover thresholds ($\ge \$20\text{M}$ volume) to ensure capacity.

## Limitations

- **Not Independently Reproduced:** All performance statistics are third-party source-reported from arXiv:2603.01820v1.
- **Unproven in Crypto:** Ported hypothesis without validated crypto execution.
- **Provenance Gap on Volatility Span:** The exact integer value for the EWMA volatility estimation span parameter $\lambda = \frac{2}{\text{span} + 1}$ is omitted from Appendix A.2 of the source text.
- **Gross-Return Training Assumption:** Models were optimized end-to-end on gross returns ($c_k = 0$) and relied on seed ensembling to control turnover, rather than embedding an explicit turnover penalty directly into the differentiable loss function.
- **Survivorship & Roll Bias:** The dataset uses continuous linked contracts from Pinnacle Data, which inherently embeds roll and contract selection rules.

## Implementation status

`not-implemented`.

This record represents external research ingestion only. No code has been written to PyBroker, NautilusTrader, paper, testnet, or live trading workflows.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.

This capture serves as theoretical and empirical reference material for deep learning sequence modeling and multi-horizon trend following. It does not constitute authorization for deployment or capital allocation.

## Related Wiki records

- `[[quant/cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02]]`
- `[[quant/portfolio-bayesian-parametric-policies-policy-risk-regularization-2026-09-02]]`
- `[[quant/regime-adaptive-continual-learning-portfolio-management-recap-2026-09-02]]`
- `[[quant/futures-trend-following-autocorrelation-drift-decomposition-2026-09-02]]`
- `[[quant/compact-rienet-volatility-drag-mitigation-leveraged-gmv-2026-09-02]]`
- `[[quant/clusterlob-order-flow-imbalance-trader-behavior-clustering-2026-09-03]]`

## Sources

1. **Primary Academic Source:** Adir Saly-Kaufmann, Kieran Wood, Jan-Peter Calliess, and Stefan Zohren (Department of Engineering Science & Oxford-Man Institute of Quantitative Finance, University of Oxford), *"Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance"*, arXiv preprint `arXiv:2603.01820v1 [q-fin.TR, cs.LG]`, March 2, 2026. DOI: [https://doi.org/10.48550/arXiv.2603.01820](https://doi.org/10.48550/arXiv.2603.01820). Stable URL: [https://arxiv.org/abs/2603.01820](https://arxiv.org/abs/2603.01820). Full-text HTML: [https://arxiv.org/html/2603.01820](https://arxiv.org/html/2603.01820).
2. **Benchmark Framework & Volatility Targeting Foundation:** Bryan Lim, Stefan Zohren, and Stephen Roberts, *"Enhancing time series momentum strategies using deep neural networks"*, Journal of Financial Data Science, 2019 / arXiv:1904.04912; and *"Trading with the Momentum Transformer: An Intelligent and Interpretable Architecture"*, arXiv:2112.08534, 2021.
3. **xLSTM Architectural Reference:** Maximilian Beck, Konstantin Pöppel, Markus Spanring, Andreas Auer, Olga Prudnikova, Michael Kopp, Günter Klambauer, Johannes Brandstetter, and Sepp Hochreiter, *"xLSTM: Extended Long Short-Term Memory"*, Advances in Neural Information Processing Systems (NeurIPS), 37, 2024. arXiv:2405.04517.
4. **Data Provider:** Pinnacle Data CLC (Continuous Linked Contract) dataset documentation, [https://pinnacledata2.com/clc.html](https://pinnacledata2.com/clc.html).
