---
schema: strategy-research-record-v1
title: "VertiFuseX: Generalizable Equity Directional Forecasting via Penultimate-Layer Multi-Stream Temporal Fusion, Triple-Barrier Gating, and Post-Loss Cool-Down (Bohra & Vijay 2026)"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - deep-learning
  - lstm
  - bi-lstm
  - stacked-lstm
  - penultimate-fusion
  - triple-barrier
  - cool-down
  - equity-index
  - directional-alpha
status: research-only
confidence: medium
source_as_of: 2026-09-14
sources:
  - "Aashish Bohra and Vivek Vijay, 'VertiFuseX: Generalizable Financial Forecasting via Multi-Stream Temporal Fusion', arXiv:2609.12793v1 [cs.LG, cs.AI, q-fin.ST], submitted September 14, 2026. https://arxiv.org/abs/2609.12793"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# VertiFuseX: Generalizable Equity Directional Forecasting via Penultimate-Layer Multi-Stream Temporal Fusion, Triple-Barrier Gating, and Post-Loss Cool-Down (Bohra & Vijay 2026)

## Provenance

- **Primary Source:**
  - Authors: Aashish Bohra and Vivek Vijay (Department of Mathematics, Indian Institute of Technology Jodhpur, Karwar, Rajasthan, India; contact: `bohra.1@iitj.ac.in`, `vivek@iitj.ac.in`).
  - Title: *VertiFuseX: Generalizable Financial Forecasting via Multi-Stream Temporal Fusion*
  - Publication: arXiv preprint `arXiv:2609.12793v1 [cs.LG, cs.AI, q-fin.ST]`, submitted Monday, September 14, 2026 (`source-reported`).
  - Abstract URL: https://arxiv.org/abs/2609.12793
  - Full-Text HTML: https://arxiv.org/html/2609.12793v1
  - Full-Text PDF: https://arxiv.org/pdf/2609.12793v1
  - Canonical DOI: [10.48550/arXiv.2609.12793](https://doi.org/10.48550/arXiv.2609.12793)
  - License: Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Experimental Infrastructure & Datasets:**
  - Historical Price Data: 15 years (January 1, 2010 through December 31, 2024) of daily Open, High, Low, Close (OHLC) data retrieved from Yahoo Finance for 10 global equity indices across North America, Europe, and Asia (`source-reported`):
    - United States: S&P 500 (`^GSPC`), Dow Jones Industrial Average (`^DJI`), New York Stock Exchange Composite (`^NYA`), NASDAQ Composite (`^IXIC`).
    - Europe: FTSE 100 (`^FTSE`), DAX (`^GDAXI`).
    - Asia: Hang Seng Index (`^HSI`), KOSPI (`^KS11`), Nikkei 225 (`^N225`), NIFTY 50 (`^NSEI`).
  - Hardware Environment: Tesla P100-PCIE-16GB GPU, Intel Xeon 2.20 GHz CPU, 12 GB RAM, Python 3.10, TensorFlow 2.14, CUDA 11.8 on Google Colab (`source-reported`).
- **Repository Deduplication Audit:**
  - Audited all existing `.md` records in `alpha-strategy-research` via keyword and regex search.
  - Prior record search: zero existing records cite `arXiv:2609.12793`, VertiFuse, or VertiFuseX.
  - Related deep-learning fusion and multi-scale temporal records in the repository:
    - `wavefuse-wavelet-denoised-cwwt-vertical-attention-fusion-2026-09-16.md` (Bohra & Vijay 2026, arXiv:2609.14733): Combines Discrete Wavelet Transform (DWT Sym-4) price denoising, 7 derived technical indicators, Channel-Wise Continuous Wavelet Transform (CWWT across 32 Morlet scales), and Vertical Attention Fusion (VAF) between a CNN-BiLSTM temporal branch and a Transformer spectral branch.
    - `learnable-wavelet-transformer-long-short-equity-wavelsformer-2026-09-03.md`: Employs learnable wavelet filter banks for cross-sectional ranking.
  - Distinctiveness & Material Differences:
    - *Input Modality & Preprocessing:* Unlike WaVeFuse, which requires multi-scale continuous wavelet decomposition of seven derived technical indicators, VertiFuseX is strictly univariate ($f=1$, raw closing prices only) and executes zero hand-crafted feature engineering or wavelet transforms, completely eliminating lookahead or indicator parameter dependencies.
    - *Architectural Mechanism:* While WaVeFuse uses attention-gated fusion between temporal sequences and spectral frequency tokens, VertiFuseX directly addresses the representational bottleneck of recurrent models by executing penultimate-layer vertical fusion across three heterogeneous recurrent inductive biases (sequential memory in LSTM, bidirectional context in Bi-LSTM, and hierarchical multi-scale abstraction in St-LSTM) alongside a parallel feedforward DNN stream.
    - *Risk Management & Execution Overlay:* VertiFuseX formulates an institutional trading model incorporating an empirical forecast quantile threshold ($\tau_{25}$), next-day opening price execution ($P_t^{\text{open}}$) with overnight gap risk, Triple-Barrier Method exits (Take-Profit $+6\%$, Stop-Loss $-3\%$, minimum 3-day hold), and a novel post-stop-loss cool-down mechanism that explicitly halts trading for 3 days to break error autocorrelation clusters during regime shifts.

## Economic mechanism

### Source-reported

1. **Information-Theoretic Advantage of Penultimate-Layer Representations:**
   - Final-layer outputs in standard deep learning architectures undergo severe task-specific compression into scalar predictions to minimize empirical loss, discarding rich intermediate temporal state dynamics (`source-reported`).
   - Under the Data Processing Inequality, intermediate hidden representations satisfy $I(\mathbf{X}; \mathbf{F}_i) \ge I(\mathbf{X}; \hat{y}_i)$, meaning that penultimate representations $\mathbf{F}_i = \phi_{i(-1)}(\mathbf{X})$ retain strictly greater or equal mutual information with the input price sequence than scalar final predictions $\hat{y}_i$ (`source-reported`).
   - Operating at the penultimate layer preserves the distinct inductive biases of heterogeneous recurrent structures—sequential memory (LSTM), bidirectional context (Bi-LSTM), and multi-scale hierarchy (St-LSTM)—before they are collapsed into scalar outputs (`source-reported`).
2. **Mitigation of Error Autocorrelation via Learned Vertical Affine Fusion:**
   - Decision-level ensembling (e.g., simple or weighted averaging of scalar predictions) reduces variance under independent errors, but suffers diversification collapse during market regime shifts when individual branch errors become highly correlated (`source-reported`).
   - VertiFuseX concatenates penultimate representations along the feature axis into a vertical stack ($\mathbf{F}_{\text{vert}} \in \mathbb{R}^{192}$) and projects them through a learned affine operator $\mathbf{W}_{\text{fuse}} \in \mathbb{R}^{64 \times 192}$ optimized end-to-end via backpropagation (`source-reported`).
   - This joint gradient flow enables complementary specialization: the St-LSTM captures persistent macro trends, the Bi-LSTM contextualizes local volatility within the lookback window, and the learned weight matrix dynamically shifts sensitivity between branches across market regimes without requiring manual parameter re-tuning (`source-reported`).
3. **Mid-Range Temporal Dominance (Lags 9–15 Days):**
   - Gradient-based saliency analysis ($|\partial \hat{y} / \partial x_t|$) reveals that VertiFuseX attenuates both noisy immediate-step price fluctuations (lags 17–20) and stale distant history (lags 1–3), consistently concentrating its predictive attribution on mid-range lags 9 to 15 (`source-reported`).
   - This 9–15 day window aligns with empirical 2-to-3 week swing trading horizons, but emerges organically from learned penultimate feature filtering rather than prescribed indicator lookbacks (`source-reported`).
4. **Behavioral De-Biasing via Post-Loss Cool-Down Gating:**
   - Empirical analysis of forecasting failures indicates that model prediction errors cluster temporally during structural market breaks; when the model misinterprets a regime shift, directional failures persist for 2 to 3 consecutive trading days (`source-reported`).
   - Implementing a mandatory 3-day post-stop-loss cool-down pause ($\delta_t = 0$) directly suppresses "error autocorrelation" and prevents algorithmic "revenge trading" into persistent adverse market regimes, reducing cluster length rather than individual loss magnitude (`source-reported`).

### Research interpretation

- **Orthogonal Recurrent Priors as Implicit State-Space Filtering:**
  - By combining forward-only recursion (LSTM), non-causal within-window contextualization (Bi-LSTM), and progressive vertical depth (St-LSTM), VertiFuseX creates an implicit multi-frequency decomposition of raw closing prices without requiring wavelet transforms or Fourier filters.
  - The parallel feedforward DNN acts as a static non-linear baseline, ensuring that persistent price levels or step changes do not induce runaway recurrent drifts.
- **Drawdown-Centric Risk Truncation vs. Unconstrained Momentum:**
  - The strategy's edge stems primarily from asymmetry in downside protection rather than superior upside capture. During strong bull markets, the strategy sacrifices modest upside (e.g., trailing buy-and-hold on NASDAQ 26.59% vs 36.25%) in exchange for eliminating left-tail compound drawdowns via triple-barrier stops and mandatory cool-down pauses.

## Signal

### Preprocessing & Architecture

1. **DATAETL Preprocessing Pipeline (`source-reported`):**
   - Input: Daily closing price series $P_t$ for index $k$ (`source-reported`).
   - Time indexing: Strictly trading-time progression; non-trading calendar days (weekends, exchange holidays, market suspensions) are excised completely without interpolation, forward-filling, or backward-filling (`source-reported`).
   - Windowing: Chronological sliding window of length $w = 20$ trading days, strictly univariate ($f = 1$): $\mathbf{X}_t = [P_{t-19}, P_{t-18}, \dots, P_t]^\top \in \mathbb{R}^{20 \times 1}$ (`source-reported`).
   - Normalization: Min-Max scaling to $[0, 1]$:
     $$\tilde{P} = \frac{P - P_{\min}^{(\text{train})}}{P_{\max}^{(\text{train})} - P_{\min}^{(\text{train})}}$$
     Fitted strictly on the in-sample training split $\mathcal{D}_{\text{train}}$ and frozen for validation and test evaluations (`source-reported`).
2. **Feature Extraction (FeatExt) Layer (`source-reported`):**
   - *LSTM Branch:*
     - Layer 1: 128 units, `return_sequences=True`, batch normalization, dropout $p=0.3 \implies \mathbf{H}_{\text{LSTM}}^{(1)} \in \mathbb{R}^{20 \times 128}$ (`source-reported`).
     - Layer 2: 64 units, `return_sequences=False`, batch normalization, dropout $p=0.3 \implies \mathbf{F}_{\text{LSTM}}^{(-1)} \in \mathbb{R}^{64}$ (`source-reported`).
   - *Bi-LSTM Branch:*
     - Layer 1: 128 units per direction (256 concatenated), `return_sequences=True`, batch normalization, dropout $p=0.3 \implies \mathbf{H}_{\text{Bi-LSTM}}^{(1)} \in \mathbb{R}^{20 \times 256}$ (`source-reported`).
     - Layer 2: 32 units per direction (64 concatenated), `return_sequences=False`, batch normalization, dropout $p=0.3 \implies \mathbf{F}_{\text{Bi-LSTM}}^{(-1)} \in \mathbb{R}^{64}$ (`source-reported`).
     - *Causal Guarantee:* The backward pass operates strictly over historical observations within the window $[t-19, \dots, t]$ and never accesses future timestamps $\tau > t$ (`source-reported`).
   - *Stacked LSTM (St-LSTM) Branch:*
     - Layer 1: 128 units, `return_sequences=True`, batch normalization, dropout $p=0.3 \implies \mathbf{H}_{\text{St-LSTM}}^{(1)} \in \mathbb{R}^{20 \times 128}$ (`source-reported`).
     - Layer 2: 128 units, `return_sequences=True`, batch normalization, dropout $p=0.3 \implies \mathbf{H}_{\text{St-LSTM}}^{(2)} \in \mathbb{R}^{20 \times 128}$ (`source-reported`).
     - Layer 3: 64 units, `return_sequences=False`, batch normalization, dropout $p=0.3 \implies \mathbf{F}_{\text{St-LSTM}}^{(-1)} \in \mathbb{R}^{64}$ (`source-reported`).
   - *Parallel DNN Stream:*
     - Input: Flattened 20-day vector $\mathbf{x}_{\text{flat}} \in \mathbb{R}^{20}$ (`source-reported`).
     - Dense Layer 1: 128 units, ReLU activation, dropout $p=0.3$ (`source-reported`).
     - Dense Layer 2: 64 units, ReLU activation, dropout $p=0.3 \implies \mathbf{F}_{\text{DNN}}^{(-2)} \in \mathbb{R}^{64}$ (`source-reported`).
     - Dimension Alignment: Mapping layer $\hat{\mathbf{F}}_{\text{DNN}} = \text{ReLU}(\mathbf{W}_{\text{align}} \mathbf{F}_{\text{DNN}}^{(-2)} + \mathbf{b}_{\text{align}}) \in \mathbb{R}^{64}$ (`source-reported`).
3. **VertiFuse Layer (Two-Stage Vertical Fusion) (`source-reported`):**
   - *Stage 1 (Temporal VertiFuse):* Vertical concatenation of the three recurrent penultimate representations:
     $$\mathbf{F}_{\text{vert}} = \left[\mathbf{F}_{\text{LSTM}}^{(-1)}; \mathbf{F}_{\text{Bi-LSTM}}^{(-1)}; \mathbf{F}_{\text{St-LSTM}}^{(-1)}\right] \in \mathbb{R}^{192}$$
     $$\mathbf{F}_{\text{fused}} = \text{ReLU}(\mathbf{W}_{\text{fuse}} \mathbf{F}_{\text{vert}} + \mathbf{b}_{\text{fuse}}) \in \mathbb{R}^{64}$$
     where $\mathbf{W}_{\text{fuse}} \in \mathbb{R}^{64 \times 192}$ and $\mathbf{b}_{\text{fuse}} \in \mathbb{R}^{64}$ (`source-reported`).
   - *Stage 2 (Joint Temporal-DNN Fusion):* Vertical concatenation of fused temporal vector with aligned DNN vector:
     $$\mathbf{F}_{\text{combined}} = \text{ReLU}\left(\mathbf{W}_{\text{comb}} \left[\mathbf{F}_{\text{fused}}; \hat{\mathbf{F}}_{\text{DNN}}\right] + \mathbf{b}_{\text{comb}}\right) \in \mathbb{R}^{64}$$
     where $\mathbf{W}_{\text{comb}} \in \mathbb{R}^{64 \times 128}$ and $\mathbf{b}_{\text{comb}} \in \mathbb{R}^{64}$ (`source-reported`).
   - *Regression Output:* Scalar next-day normalized price prediction:
     $$\hat{y}_{t+1} = \mathbf{w}_{\text{out}}^\top \mathbf{F}_{\text{combined}} + b_{\text{out}} \in \mathbb{R}$$
     Denormalized closing price forecast: $\hat{P}_{t+1} = \hat{y}_{t+1}(P_{\max} - P_{\min}) + P_{\min}$ (`source-reported`).
4. **Training Optimization Protocol (`source-reported`):**
   - Loss function: Mean Squared Error (MSE) (`source-reported`).
   - Optimizer: Adam with initial learning rate $\eta = 10^{-4}$ (`source-reported`).
   - Learning Rate Scheduler: `ReduceLROnPlateau` (patience = 5 epochs, decay factor = 0.5) (`source-reported`).
   - Regularization: Early stopping with patience = 10 epochs on validation loss, $\ell_2$ weight decay ($10^{-4}$), and dropout rate 0.3 across all modules (`source-reported`).
   - Batch size: 64; Maximum epochs: 50 (`source-reported`).

### Trading Signal Logic & Position Management

- **Forecast Return Calculation (`source-reported`):**
  $$\hat{r}_{t} = \frac{\hat{P}_{t} - P_{t-1}}{P_{t-1}}$$
- **Directional Long Entry Trigger (`source-reported`):**
  - A long position is initiated at the close of day $t-1$ if:
    1. The predicted return $\hat{r}_t$ exceeds the 25th percentile ($\tau_{25}$) of the out-of-sample forecast distribution, capturing the top 75% of positive predicted price moves: $S_t = \mathbb{I}(\hat{r}_t > \tau_{25})$ (`source-reported`).
    2. The risk-gating state variable $\delta_t = 1$ (the system is not in an active cool-down pause) (`source-reported`).
  - *Stress-Testing Variant:* For extreme crisis regimes (COVID crash, 2022 bear market), the entry threshold is tightened to the 75th percentile ($\tau_{75}$) of the training distribution, capturing only the top 25% highest-conviction signals (`source-reported`).
- **Position Sizing (`source-reported`):**
  - Binary allocation: 100% portfolio equity invested in the single index when long; 0% (100% cash) when flat (`source-reported`).
  - No leverage, no shorting (`source-reported`). Uninvested cash earns zero return (`source-reported`).
- **Exit Logic (Triple-Barrier Method) (`source-reported`):**
  For an open position entered at price $P_{\text{entry}}$, the position is closed if any of three barriers is hit:
  1. *Take-Profit (TP):* Cumulative trade return $r_{\text{trade}} = (P_t - P_{\text{entry}}) / P_{\text{entry}} \ge +6.0\%$ (`source-reported`).
  2. *Stop-Loss (SL):* Cumulative trade return $r_{\text{trade}} \le -3.0\%$ (`source-reported`).
  3. *Time Horizon / Signal Cessation:* The directional forecast drops below the entry threshold ($\hat{r}_{t+1} \le \tau_{25}$), subject to a mandatory minimum holding period of 3 trading days ($t - t_{\text{entry}} \ge 3$) (`source-reported`).
- **Post-Stop-Loss Cool-Down Mechanism (`source-reported`):**
  - If a position exits via the Stop-Loss barrier ($r_{\text{trade}} \le -3\%$), the risk gate immediately sets $\delta_t = 0$ for a mandatory cooling-off period of 3 trading days:
    $$\delta_t = 0 \quad \forall \, t \in [t_{\text{exit}} + 1, t_{\text{exit}} + 3]$$
  - No new long positions may be opened during these 3 days, regardless of the magnitude of $\hat{r}_t$ (`source-reported`).
  - Trading resumes ($\delta_t = 1$) on trading day $t_{\text{exit}} + 4$ (`source-reported`).

## Required data

- **Instruments & Universes:**
  - 10 global equity market indices: S&P 500 (`^GSPC`), DJIA (`^DJI`), NYSE Composite (`^NYA`), NASDAQ Composite (`^IXIC`), FTSE 100 (`^FTSE`), DAX (`^GDAXI`), Hang Seng Index (`^HSI`), KOSPI (`^KS11`), Nikkei 225 (`^N225`), and NIFTY 50 (`^NSEI`) (`source-reported`).
- **Venue & Sourcing:**
  - National exchanges (NYSE, NASDAQ, London Stock Exchange, Deutsche Börse, HKEX, KRX, Tokyo Stock Exchange, NSE India); sourced publicly via Yahoo Finance API (`source-reported`).
- **Timeframe & Session Conventions:**
  - Daily trading-session frequency (`source-reported`).
  - Calendar alignment: All non-trading days (weekends, exchange holidays, emergency trading halts) are dropped from the series, ensuring continuous trading-time indices without synthetic zero-volatility data points (`source-reported`).
  - Note on U.S. alignment: The four U.S. indices (S&P 500, DJIA, NYSE, NASDAQ) share an identical trading calendar, producing exactly 3,388 training days and 365 test days across the 15-year sample (`source-reported`).
- **Data Fields:**
  - Strictly univariate: Daily Closing Price ($P_t$) only (`source-reported`).
  - Raw Open prices ($P_t^{\text{open}}$) are used exclusively to determine trade fill prices on execution days (`source-reported`).
  - High and Low prices ($P_t^{\text{high}}, P_t^{\text{low}}$) are used to evaluate intraday Triple-Barrier barrier touches (`source-reported`).
- **Point-in-Time & Validation Structure:**
  - Chronological non-overlapping split: First 3,388 trading days (January 1, 2010 – December 2023) for model training, with the terminal 10% reserved for internal validation (`source-reported`).
  - Out-of-sample holdout test partition: Terminal 365 trading days (calendar year 2024 for primary U.S. baseline evaluation) held locked and uninspected (`source-reported`).
  - Extreme regime stress evaluation: Trained on January 1, 2010 – December 27, 2019; tested over 1,260 trading days (December 27, 2019 – December 31, 2024) under frozen weights (`source-reported`).

## Execution assumptions

- **Order Timing & Execution Fill Model:**
  - *Order Generation:* Signals are computed at the daily market close of day $t-1$ using closing prices up to $P_{t-1}$ (`source-reported`).
  - *Fill Execution:* Orders are submitted for execution at the market open of day $t$ and filled at the opening price $P_t^{\text{open}}$ (`source-reported`).
  - *Overnight Gap Risk:* The simulation explicitly models overnight price gap risk between close $t-1$ and open $t$, preventing look-ahead execution at $P_{t-1}^{\text{close}}$ (`source-reported`).
- **Transaction Costs & Slippage:**
  - A proportional fee of $\psi = 10$ basis points ($0.10\%$) is deducted on every executed trade round-trip or state change (`source-reported`).
  - *Bid-Ask Spread & Market Impact:* Omitted from paper backtest (`source-reported`).
  - *Implementation Buffer:* For actual index ETF (e.g., SPY, QQQ) or liquid futures (e.g., E-mini S&P 500) trading, an additional 2 to 4 bps half-spread plus slippage buffer must be modeled (`research-proposed`).
- **Shorting, Borrow, & Financing:**
  - Long-only strategy; no shorting or borrow fees required (`source-reported`).
  - Unallocated capital sits in cash earning 0% nominal interest (`source-reported`).
- **Capital Allocation & Compounding:**
  - Initial capital: 10,000 currency units (`source-reported`).
  - Portfolio returns compound geometrically over time (`source-reported`).

## Evidence

### Source-reported

All quantitative figures below trace directly to Bohra & Vijay (`arXiv:2609.12793v1`, Tables 6, 8, 9, 10, 11, 12, 13):

1. **Forecasting Error Comparison vs. Baselines (2024 Out-of-Sample Test Set, 365 Days, Table 6):**
   - *S&P 500:* VertiFuseX achieves MAE 30.22, RMSE 40.57, MAPE 0.59%.
     - vs. LSTM (51.57 / 64.52 / 1.25%): -41.4% MAE, -37.1% RMSE, -52.8% MAPE.
     - vs. Bi-LSTM (53.42 / 66.48 / 1.29%): -43.4% MAE, -39.0% RMSE, -54.3% MAPE.
     - vs. St-LSTM (46.49 / 59.31 / 1.12%): -35.0% MAE, -31.6% RMSE, -47.3% MAPE.
     - vs. Standalone ARIMA (59.12 / 74.85 / 1.45%): -48.9% MAE, -45.8% RMSE, -59.3% MAPE.
   - *DJIA:* VertiFuseX achieves MAE 201.93, RMSE 270.60, MAPE 0.52%.
     - vs. LSTM (333.28 / 424.64 / 1.01%): -39.4% MAE, -36.3% RMSE, -48.5% MAPE.
     - vs. Bi-LSTM (297.50 / 389.82 / 0.90%): -32.1% MAE, -30.6% RMSE, -42.2% MAPE.
     - vs. St-LSTM (303.97 / 396.18 / 0.91%): -33.6% MAE, -31.7% RMSE, -42.9% MAPE.
     - vs. Standalone ARIMA (378.45 / 482.67 / 1.15%): -46.6% MAE, -43.9% RMSE, -54.8% MAPE.
   - *NYSE Composite:* VertiFuseX achieves MAE 93.34, RMSE 120.43, MAPE 0.53%.
     - vs. LSTM (170.07 / 213.70 / 1.09%): -45.1% MAE, -43.6% RMSE, -51.4% MAPE.
     - vs. Bi-LSTM (165.28 / 208.55 / 1.06%): -43.5% MAE, -42.3% RMSE, -50.0% MAPE.
     - vs. St-LSTM (150.18 / 192.65 / 0.96%): -37.8% MAE, -37.5% RMSE, -44.8% MAPE.
     - vs. Standalone ARIMA (198.76 / 249.34 / 1.27%): -53.0% MAE, -51.7% RMSE, -58.3% MAPE.
   - *NASDAQ Composite:* VertiFuseX achieves MAE 134.54, RMSE 180.87, MAPE 0.83%.
     - vs. LSTM (206.81 / 256.85 / 1.65%): -34.9% MAE, -29.5% RMSE, -49.7% MAPE.
     - vs. Bi-LSTM (212.46 / 263.70 / 1.69%): -36.7% MAE, -31.4% RMSE, -50.9% MAPE.
     - vs. St-LSTM (195.82 / 243.98 / 1.56%): -31.3% MAE, -25.8% RMSE, -46.8% MAPE.
     - vs. Standalone ARIMA (245.89 / 304.56 / 1.89%): -45.3% MAE, -40.6% RMSE, -56.1% MAPE.
2. **State-of-the-Art Model Benchmark Comparisons (Table 9):**
   - *DAX (2000–2021):* VertiFuseX MAE 133.94 vs. BiCuDNNLSTM-1dCNN 188.27 (-28.86%); RMSE 190.87 vs. 258.65 (-26.21%).
   - *HSI (2000–2021):* VertiFuseX MAE 268.84 vs. BiCuDNNLSTM-1dCNN 411.27 (-34.63%); RMSE 359.48 vs. 526.21 (-31.69%).
   - *S&P 500 (2000–2017):* VertiFuseX MAE 9.28 vs. ModAugNet 12.05 (-23.0%); MAPE 0.79% vs. 1.07% (-26.1%).
   - *S&P 500 (2010–2018):* VertiFuseX MAE 13.85 vs. Reservoir Computing 15.80 (-12.34%); RMSE 21.64 vs. 23.25 (-6.92%); MAPE 0.52% vs. 0.60% (-13.33%).
   - *DJIA (1991–2010):* VertiFuseX RMSE 100.84 vs. DE-ABC-Bi-LSTM-ARIMA 158.66 (-36.4%); MAPE 0.70% vs. 0.81% (-13.6%).
   - *KOSPI (2014–2022):* VertiFuseX MAE 22.59 vs. GA-CNN-LSTM 31.47 (-28.2%); RMSE 28.29 vs. 40.05 (-29.36%); MAPE 0.80% vs. 1.10% (-27.2%).
   - *NSE (1996–2020):* VertiFuseX MAE 62.99 vs. StockNet 69.93 (-9.92%); MAPE 0.65% vs. 0.82% (-20.73%).
3. **Economic Trading Performance (2024 Out-of-Sample, 10 bps fee, Table 11):**
   - *S&P 500:*
     - VertiFuseX: Total Return 29.41%, Sharpe 1.43, Sortino 1.85, Max DD -9.75%, Win Rate 67.7%, Exposure 74.8%, 31 Trades.
     - Buy-and-Hold: Total Return 29.44%, Sharpe 1.37, Sortino 1.89, Max DD -10.28%, Win Rate 100.0%, Exposure 100.0%, 1 Trade.
     - Naive Momentum: Total Return -5.08%, Sharpe -0.44, Sortino -0.52, Max DD -11.28%, Win Rate 46.7%, Exposure 56.7%, 92 Trades.
   - *DJIA:*
     - VertiFuseX: Total Return 21.44%, Sharpe 1.15, Sortino 1.75, Max DD -8.94%, Win Rate 57.7%, Exposure 74.8%, 26 Trades.
     - Buy-and-Hold: Total Return 21.08%, Sharpe 1.06, Sortino 1.63, Max DD -9.02%, Win Rate 100.0%, Exposure 100.0%, 1 Trade.
     - Naive Momentum: Total Return 0.18%, Sharpe -0.19, Sortino -0.26, Max DD -9.92%, Win Rate 52.9%, Exposure 56.7%, 85 Trades.
   - *NASDAQ:*
     - VertiFuseX: Total Return 26.59%, Sharpe 1.04, Sortino 1.27, Max DD -11.97%, Win Rate 64.9%, Exposure 74.8%, 37 Trades.
     - Buy-and-Hold: Total Return 36.25%, Sharpe 1.27, Sortino 1.74, Max DD -13.15%, Win Rate 100.0%, Exposure 100.0%, 1 Trade.
     - Naive Momentum: Total Return -0.39%, Sharpe 0.00, Sortino 0.00, Max DD -14.89%, Win Rate 50.6%, Exposure 58.4%, 85 Trades.
   - *NYSE Composite:*
     - VertiFuseX: Total Return 7.68%, Sharpe 0.35, Sortino 0.51, Max DD -13.14%, Win Rate 48.6%, Exposure 74.8%, 37 Trades.
     - Buy-and-Hold: Total Return 17.31%, Sharpe 0.88, Sortino 1.32, Max DD -10.66%, Win Rate 100.0%, Exposure 100.0%, 1 Trade.
     - Naive Momentum: Total Return 4.92%, Sharpe 0.18, Sortino 0.26, Max DD -9.04%, Win Rate 56.5%, Exposure 53.7%, 85 Trades.
4. **Controlled Ablation Hierarchy (Table 12):**
   - *S&P 500:* St-LSTM (46.49 MAE / 59.31 RMSE / 1.12% MAPE) $\rightarrow$ Average Ensemble (43.18 / 55.21 / 1.04%) $\rightarrow$ Final-Layer Fusion (39.87 / 51.96 / 0.93%) $\rightarrow$ VertiFuseX Penultimate Fusion (30.22 / 40.57 / 0.59%).
     - Penultimate fusion reduces MAE by an additional 24.2% and MAPE by 36.6% relative to Final-Layer Fusion under identical parameter capacity at the combination stage.
   - *NASDAQ:* St-LSTM (195.82 / 243.98 / 1.56%) $\rightarrow$ Average Ensemble (184.35 / 229.67 / 1.45%) $\rightarrow$ Final-Layer Fusion (170.42 / 214.86 / 1.32%) $\rightarrow$ VertiFuseX Penultimate Fusion (134.54 / 180.87 / 0.83%).
     - Penultimate fusion reduces MAE by an additional 21.1% and MAPE by 37.1% relative to Final-Layer Fusion.
5. **Extreme Market Regime Stress Testing (Frozen 2010–2019 Model, S&P 500, Table 13):**
   - *COVID-19 Crash (19 Feb – 30 Apr 2020):*
     - VertiFuseX: Total Return -9.63%, Sharpe -0.56, Max DD -26.45%, Annualized Volatility 61.33%.
     - Buy & Hold: Total Return -16.08%, Sharpe -0.98, Max DD -33.67%, Annualized Volatility 68.13%.
     - Naive Momentum: Total Return -19.78%, Sharpe -2.21, Max DD -23.61%, Annualized Volatility 46.18%.
     - Result: VertiFuseX outperformed Buy & Hold by +6.45 percentage points in return and limited drawdown by 7.22 percentage points via signal shrinkage and cool-down gating.
   - *2022 Bear Market (1 Jan – 31 Oct 2022):*
     - VertiFuseX: Total Return -10.04%, Sharpe -0.51, Max DD -17.67%, Annualized Volatility 23.45%.
     - Buy & Hold: Total Return -19.56%, Sharpe -1.04, Max DD -25.38%, Annualized Volatility 24.33%.
     - Naive Momentum: Total Return -30.31%, Sharpe -2.41, Max DD -30.50%, Annualized Volatility 18.26%.
     - Result: VertiFuseX outperformed Buy & Hold by +9.52 percentage points in return and limited drawdown by 7.71 percentage points.
6. **Computational Latency & Footprint (Table 10):**
   - Total model parameters: ~675,000. Memory footprint: 2.6 MB.
   - GPU training time per index: 100.23 s (S&P 500), 107.16 s (DJIA), 107.55 s (NYSE), 101.11 s (NASDAQ).
   - Deterministic inference latency: 1.47 ms/sample (S&P 500, NYSE) to 1.56 ms/sample (DJIA).

### Independently reproduced

- `not independently reproduced`
- All empirical claims and performance statistics are third-party results reported directly in the primary paper by Bohra & Vijay (`arXiv:2609.12793v1`, September 2026). No internal backtesting has been executed in `nautilus-quant-system` or PyBroker.

### Negative evidence

1. **Failure to Outperform Buy-and-Hold on Heterogeneous Composite Index (NYSE Composite):**
   - On the NYSE Composite, VertiFuseX achieved a 2024 total return of only 7.68% compared to 17.31% for Buy-and-Hold, with a lower Sharpe ratio (0.35 vs. 0.88), lower Sortino ratio (0.51 vs. 1.32), and deeper maximum drawdown (-13.14% vs. -10.66%) (`source-reported`).
   - The authors identify the structural reason: the NYSE Composite contains higher cross-sectional sectoral heterogeneity and smaller-cap constituents with lower trend persistence and stronger mean-reverting dynamics. The 20-day lookback and triple-barrier trend logic were frequently whipsawed by constituent rotation (`source-reported`).
2. **Lagging Bull-Market Participation on High-Beta Index (NASDAQ):**
   - On NASDAQ, VertiFuseX generated 26.59% total return versus 36.25% for Buy-and-Hold (a 9.66 percentage point lag in upside capture) (`source-reported`).
   - The strategy's 74.8% market exposure and risk barriers truncated upside participation during persistent vertical tech rallies in exchange for an 8.97% relative reduction in max drawdown (-11.97% vs -13.15%) (`source-reported`).
3. **Macro / News Catalyst Blindness:**
   - Because VertiFuseX relies strictly on univariate closing price series without order book, interest rate, macroeconomic calendar, or sentiment feeds, it is completely blind to unexpected policy rate decisions, geopolitical shocks, or corporate earnings releases (`source-reported`).

## Falsification plan

To test the falsifiability of the hypothesis that penultimate-layer multi-stream temporal fusion generates reproducible, execution-robust economic alpha, the following operational tests are defined:

1. **Test 1: Bid-Ask Spread & Next-Day Open Execution Stress Test (`research-proposed`):**
   - *Design:* Simulate the exact 2024 out-of-sample trading model on S&P 500, DJIA, and NASDAQ using next-day Open fills ($P_t^{\text{open}}$), but expand the friction model from the baseline 10 bps flat fee to include realistic exchange maker/taker fees (5 bps) plus a 5 bps half-spread and 3 bps market impact buffer (total 13 bps per trade).
   - *Decision Rule:* If the net Sharpe ratio drops below 0.80 across S&P 500 and DJIA, or if the net total return falls below zero on any index, the claim of economic tradability under realistic microstructure frictions is falsified (`research-defined falsification threshold`).
2. **Test 2: Post-Loss Cool-Down Ablation Test (`research-proposed`):**
   - *Design:* Re-run the backtest across all four U.S. indices and the two stress regimes with the 3-day post-stop-loss cool-down disabled ($\delta_t \equiv 1$), allowing immediate re-entry upon signal trigger.
   - *Decision Rule:* If the maximum drawdown during the COVID-19 crash worsens by less than 2.0 percentage points or if the Sortino ratio improves without cool-down, the hypothesis that error autocorrelation clustering justifies an exogenous trading halt is falsified (`research-defined falsification threshold`).
3. **Test 3: Temporal Shuffling & Branch Permutation Placebo Test (`research-proposed`):**
   - *Design:* Randomly permute the temporal order of closing prices within each 20-day sliding window before feature extraction, destroying the chronological causality while preserving the empirical marginal return distribution.
   - *Decision Rule:* If the VertiFuseX architecture trained on shuffled windows achieves an out-of-sample forecasting MAPE within 10% of the canonical model (MAPE $\le 0.65\%$ on S&P 500), the claim that the model exploits genuine sequential memory and multi-scale temporal dependencies is falsified (`research-defined falsification threshold`).
4. **Test 4: Cross-Asset Equities vs. Commodity/Crypto Regime Transfer (`research-proposed`):**
   - *Design:* Deploy the frozen VertiFuseX architecture on non-equity liquid futures (Crude Oil CL, Gold GC, Bitcoin BTC perpetual) across the 2020–2024 window without parameter retuning.
   - *Decision Rule:* If the strategy generates negative total returns across more than 2 of the 3 alternative assets, the hypothesis of domain-general multi-stream temporal abstraction is falsified as an equity-specific overfit (`research-defined falsification threshold`).

## Crypto portability

- **Portability Classification:** `adapted / unproven` (`research interpretation`).
- **Primary Source Scope:** The primary paper evaluates developed-market equity indices exclusively (S&P 500, DJIA, NYSE, NASDAQ, FTSE, DAX, HSI, KOSPI, Nikkei 225, NIFTY 50). It does not test or evaluate cryptocurrency assets (`source-reported`).
- **Cryptocurrency Adaptation Considerations (`research-proposed`):**
  1. *24/7 Continuous Trading & Session Boundaries:* Unlike equity markets with distinct 09:30–16:00 trading hours and overnight gap risk between close and open, crypto trades 24/7. Applying next-day Open fills ($P_t^{\text{open}}$) is an artificial construct in crypto. The model must be adapted to fixed rolling UTC timestamps (e.g., UTC 00:00 boundary) or discrete intraday bar resolutions (e.g., 4-hour or 1-hour bars) (`research-proposed`).
  2. *Perpetual Futures Funding Rates:* In crypto perpetual swaps (BTCUSDT, ETHUSDT), holding long positions incurs periodic 8-hour funding payments. During extended bull markets, annualized funding rates frequently exceed 15% to 40%, which would materially erode the strategy's 21%–29% annual return unless active funding carry hedging is integrated (`research-proposed`).
  3. *Volatility Scaling of Triple-Barrier Thresholds:* The fixed Take-Profit ($+6\%$) and Stop-Loss ($-3\%$) thresholds were calibrated to equity index daily volatility ($\sigma \approx 12\% - 18\%$ annualized). In crypto, where single-day price moves of $5\% - 10\%$ are common, static $-3\%$ stops would trigger premature cool-down halts during normal intraday noise. The barrier thresholds must be dynamically scaled by a rolling ATR or realized volatility metric (e.g., $1.5 \times \text{ATR}_{14}$ stop, $3.0 \times \text{ATR}_{14}$ take-profit) (`research-proposed`).
  4. *Liquidity Fragmentation & Extreme Fat Tails:* Crypto liquidity is fragmented across Binance, Bybit, OKX, and Coinbase. Slippage and liquidation cascade wicks can breach the $-3\%$ stop-loss barrier at prices far worse than the barrier level, causing severe slippage expansion beyond the assumed 10 bps (`research-proposed`).

## Limitations

1. **Univariate Price-Only Scope:** VertiFuseX relies exclusively on closing prices ($f=1$). It ignores trading volume, open interest, order flow imbalances, and macroeconomic announcements (`source-reported`).
2. **Single-Year Out-of-Sample Holdout Window:** Primary trading results are evaluated over a single 365-day test window (calendar year 2024), which represents an exceptional large-cap U.S. bull market dominated by mega-cap technology momentum (`source-reported`).
3. **Underperformance on Sectorally Diverse Markets:** Demonstrates clear weakness on the NYSE Composite (Sharpe 0.35 vs. 0.88 Buy-and-Hold), proving that the strategy fails on assets characterized by strong constituent mean reversion and sector rotation (`source-reported`).
4. **Deterministic Point Predictions Without Calibrated Uncertainty:** The model outputs a single point forecast $\hat{y}_t$ without conformal prediction intervals or Bayesian uncertainty bounds, preventing position sizing based on model confidence (`source-reported`).
5. **Fixed Exogenous Risk Parameters:** The Triple-Barrier thresholds ($+6\%, -3\%$, 3-day hold) and the 3-day post-loss cool-down duration are fixed heuristics rather than dynamically optimized controls (`source-reported`).

## Implementation status

- `not-implemented`
- This record captures external research published in arXiv preprint `arXiv:2609.12793v1` (September 14, 2026). No implementation exists in the current quantitative research stack, `nautilus-quant-system`, PyBroker, NautilusTrader, paper trading, testnet, or live trading execution systems.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- The inclusion of this research record in `alpha-strategy-research` does not constitute strategy approval, operational authorization, or validation for live deployment.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]`
- `[[wavefuse-wavelet-denoised-cwwt-vertical-attention-fusion-2026-09-16]]`
- `[[fifo-queue-partial-identification-l2-execution-sensitivity-2026-09-16]]`
- `[[binance-perpetual-dollar-bar-monotonic-lightgbm-queue-fill-falsification-2026-09-13]]`
- `[[cross-sectional-equity-ridge-percentile-rank-alpha-2026-09-03]]`

## Sources

1. Aashish Bohra and Vivek Vijay. "VertiFuseX: Generalizable Financial Forecasting via Multi-Stream Temporal Fusion." arXiv preprint `arXiv:2609.12793v1 [cs.LG, cs.AI, q-fin.ST]`, submitted September 14, 2026.
   - Abstract: https://arxiv.org/abs/2609.12793
   - Full-Text HTML: https://arxiv.org/html/2609.12793v1
   - Full-Text PDF: https://arxiv.org/pdf/2609.12793v1
   - Canonical DOI: [10.48550/arXiv.2609.12793](https://doi.org/10.48550/arXiv.2609.12793)
