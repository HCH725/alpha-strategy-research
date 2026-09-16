---
schema: strategy-research-record-v1
title: "WaVeFuse: Regime-Adaptive Equity Index Directional Alpha via Wavelet-Denoised Indicators, Channel-Wise Spectral Encoding, and Vertical Attention Fusion (Bohra & Vijay 2026)"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - deep-learning
  - wavelet-transform
  - discrete-wavelet-transform
  - continuous-wavelet-transform
  - technical-indicators
  - vertical-attention-fusion
  - regime-adaptive
  - equity-index
  - directional-trading
status: research-only
confidence: medium
source_as_of: 2026-09-13
sources:
  - "Aashish Bohra and Vivek Vijay, 'WaVeFuse: Regime-Adaptive Equity Index Forecasting via Channel-Wise Wavelet Denoising and Vertical Attention Fusion', arXiv:2609.14733v1 [cs.AI, q-fin.CP, q-fin.ST], submitted September 13, 2026. https://arxiv.org/abs/2609.14733"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# WaVeFuse: Regime-Adaptive Equity Index Directional Alpha via Wavelet-Denoised Indicators, Channel-Wise Spectral Encoding, and Vertical Attention Fusion (Bohra & Vijay 2026)

## Provenance

- **Primary Source:**
  - Authors: Aashish Bohra and Vivek Vijay (Department of Mathematics, Indian Institute of Technology Jodhpur, Rajasthan, India).
  - Title: *WaVeFuse: Regime-Adaptive Equity Index Forecasting via Channel-Wise Wavelet Denoising and Vertical Attention Fusion*
  - Publication: arXiv preprint `arXiv:2609.14733v1 [cs.AI, q-fin.CP, q-fin.ST]`, submitted September 13, 2026 (`source-reported`).
  - Abstract URL: https://arxiv.org/abs/2609.14733
  - Full-Text HTML: https://arxiv.org/html/2609.14733v1
  - Full-Text PDF: https://arxiv.org/pdf/2609.14733v1
  - Canonical DOI: [10.48550/arXiv.2609.14733](https://doi.org/10.48550/arXiv.2609.14733)
  - License: Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Data & Experimental Infrastructure:**
  - Datasets: Daily Open, High, Low, Close, Volume (OHLCV) series for KOSPI (`^KS11`), DAX (`^GDAXI`), NYSE Composite (`^NYA`), and Russell 2000 (`^RUT`) sourced from Yahoo Finance spanning January 1, 2010 through December 31, 2023 (14 years) (`source-reported`).
  - Stress Test Extension: Extended KOSPI evaluation through April 30, 2025 (1,361 test trading days) under frozen 2010–2019 parameters (`source-reported`).
  - Hardware Platform: AMD Ryzen 9 9900X 12-core CPU (4.40 GHz), 32 GB RAM, NVIDIA GeForce RTX 5060 Ti GPU (16 GB VRAM), Python 3.10, TensorFlow 2.10, CUDA 12.9 (`source-reported`).
- **Repository Deduplication Audit:**
  - Audited all existing `.md` strategy records in `alpha-strategy-research` via keyword and regex search.
  - Prior record search: zero existing records cite `arXiv:2609.14733`, Bohra, Vivek Vijay, WaVeFuse, or Vertical Attention Fusion.
  - Related wavelet / frequency decomposition records in the repository:
    - `cwt-wavelet-bandpass-mean-reversion-hmm-stress-overlay-2026-09-12.md`: Uses continuous wavelet transform for frequency bandpass filtering to extract mean-reverting cyclical components with an HMM stress regime gate.
    - `learnable-wavelet-transformer-long-short-equity-wavelsformer-2026-09-03.md`: Uses learnable wavelet filter banks inside a Transformer architecture for cross-sectional stock ranking.
  - Material Differences and Distinctiveness:
    - Unlike prior records that apply wavelets as black-box end-to-end layers or single-channel bandpass filters, WaVeFuse identifies and solves a tripartite failure mode in financial deep learning:
      1. *Indicator Noise Contamination:* Conventional pipelines apply DWT only to raw prices, allowing derived technical indicators (RSI, ATR, CCI, etc.) to inherit and amplify high-frequency microstructure noise. WaVeFuse executes DWT denoising prior to computing technical indicators.
      2. *Heterogeneous Frequency Conflation:* Conventional models flatten or aggregate multi-scale features, destroying the distinction between bounded oscillators (e.g., RSI, Stoch %K) and unbounded accumulation metrics (e.g., OBV). WaVeFuse applies a causal Channel-Wise Continuous Wavelet Transform (CWWT) across 32 integer scales to preserve per-indicator time-frequency fingerprints.
      3. *Static Multi-Branch Fusion:* Conventional hybrid models use static concatenation or fixed summation. WaVeFuse introduces Vertical Attention Fusion (VAF), a differentiable 2-token softmax gating mechanism that dynamically performs minimum-variance Bayes risk allocation, shifting capital and weight between temporal momentum (CNN-BiLSTM) and spectral volatility anomalies (Transformer) as market regimes evolve.

## Economic mechanism

### Source-reported

1. **Microstructure Noise Propagation in Derived Indicators:**
   - Raw equity prices contain two distinct components: fundamental price drift/momentum and high-frequency microstructure noise (bid-ask bounce, order queue imbalances, recording artifacts) (`source-reported`).
   - Non-linear technical indicators (TIs) such as RSI, CCI, and Stochastic %K compute finite differences and ratios of noisy prices, amplifying high-frequency noise and distorting momentum/reversal detection (`source-reported`).
   - Excising microstructure noise via Discrete Wavelet Transform (DWT) using the Symlet-4 wavelet (decomposition level $J=2$, MAD soft-thresholding) prior to indicator calculation preserves the underlying Lipschitz-continuous price trajectory while removing non-informative high-frequency variance (`source-reported`).
2. **Channel-Wise Scale-Space Fingerprinting (CWWT):**
   - Scalar technical indicators collapse rich multi-temporal phenomena into single numbers (e.g., an RSI of 65 cannot distinguish an isolated 2-day spike from a persistent 3-week trend) (`source-reported`).
   - Applying a causal Continuous Wavelet Transform (Morlet mother wavelet, $\omega_0 = 6$) independently across 32 uniformly spaced integer scales ($s \in \{1, \dots, 32\}$) converts each indicator into an instantaneous frequency-domain energy distribution, capturing multi-frequency market dynamics without cross-channel contamination (`source-reported`).
3. **Regime-Adaptive Vertical Attention Fusion (VAF):**
   - The temporal branch (CNN-BiLSTM) captures local sequence dynamics, autocorrelation, and trend persistence in denoised price-volume space (`source-reported`).
   - The spectral branch (Transformer with scale attention pooling) captures global inter-scale energy interactions across indicator frequency bands (`source-reported`).
   - VAF stacks these representations vertically into a 2-token sequence and applies a learned scalar attention gate ($\mathbf{W}_{\text{gate}} \in \mathbb{R}^{32 \times 1}$) followed by softmax, producing convex weights $[\alpha_{\text{temp}}, \alpha_{\text{spec}}]^\top$ with $\alpha_{\text{temp}} + \alpha_{\text{spec}} = 1$ (`source-reported`).
   - Under Theorem 1 and Remark 1, VAF operates as an empirical minimum-variance estimator: when the market exhibits persistent directional trends, the gate allocates higher weight to the temporal branch ($\alpha_{\text{temp}} \approx 1$); during volatility shocks or regime breaks where historical momentum fails, the gate upweights the spectral branch ($\alpha_{\text{spec}} \approx 1$) whose multi-scale energy features exhibit lower conditional error variance (`source-reported`).
4. **Asymmetric Tail Protection:**
   - By minimizing Huber loss ($\delta=0.1$) on bounded normalized targets and dynamically transitioning to spectral representations during dislocations, the strategy circumvents large drawdowns during liquidity panics (e.g., COVID-19 crash) while capturing recovery trends during policy shifts (`source-reported`).

### Research interpretation

- **Orthogonal Subspace Hypothesis:**
  - The model leverages the empirical orthogonality of temporal sequential features (momentum/trend) and instantaneous scale-space features (volatility clustering/energy dispersion).
  - Rather than treating indicators as arbitrary inputs to a large black-box network, the pipeline explicitly decouples low-frequency drift from multi-frequency oscillation, preventing the recurrent layers from over-allocating capacity to high-frequency oscillations.
- **Dynamic Regime-Switching Analogue:**
  - VAF functions as a smooth, continuous, end-to-end differentiable counterpart to discrete Hamilton regime-switching models. Instead of estimating hidden Markov transition probabilities that lag sharp inflection points, the 2-token attention mechanism adjusts branch weights on a per-step basis directly from current scale-space features.

## Signal

### Preprocessing & Signal Construction

1. **Step 1: DWT Denoising on OHLCV (`source-reported`):**
   - Input channel $c \in \{O, H, L, C, V\}$ of length $T$ within the training window is decomposed via Mallat's algorithm using the Symlet-4 (Sym-4) mother wavelet at decomposition level $J=2$:
     $$\mathbf{a}_{j+1} = \downarrow_2 (\mathbf{g} * \mathbf{a}_j), \quad \mathbf{d}_{j+1} = \downarrow_2 (\mathbf{h} * \mathbf{a}_j), \quad \mathbf{a}_0 = \mathbf{x}_c$$
   - Noise standard deviation is estimated via robust Median Absolute Deviation (MAD):
     $$\hat{\sigma}_j = \frac{\text{median}(|\mathbf{d}_j - \text{median}(\mathbf{d}_j)|)}{0.6745}$$
   - Detail coefficients are soft-thresholded using the universal threshold $\lambda_j = \hat{\sigma}_j \sqrt{2 \ln T}$:
     $$\rho_{\text{soft}}(d, \lambda) = \text{sgn}(d) \max(0, |d| - \lambda)$$
   - The denoised channel $\hat{\mathbf{x}}_c$ is reconstructed via inverse DWT (IDWT). Thresholds and normalization parameters are fitted strictly on the in-sample training fold $\mathcal{D}_{\text{train}}^{(k)}$ and applied without refitting to validation and test periods (`source-reported`).
2. **Step 2: Low-Lag Technical Indicators Computation (`source-reported`):**
   - From the denoised price series $\hat{\mathcal{P}}_t$, compute $M=7$ technical indicators:
     1. *Relative Strength Index (RSI-10):* $n=10$ lookback with exponential smoothing to reduce lag (`source-reported`).
     2. *Stochastic %K (SO%K-14):* Lookback $n=14$, $100 \times (C - L_{14}) / (H_{14} - L_{14})$ (`source-reported`).
     3. *Commodity Channel Index (CCI-14):* Lookback $n=14$, $(P - \text{SMA}(P, 14)) / (0.015 \times \text{MAD}(P, 14))$, where $P = (H + L + C)/3$ (`source-reported`).
     4. *On-Balance Volume (OBV):* Cumulative signed volume: $\text{OBV}_t = \text{OBV}_{t-1} + V_t \cdot \text{sgn}(C_t - C_{t-1})$ (`source-reported`).
     5. *Average True Range (ATR-14):* Lookback $n=14$, 14-day EMA of true range $\text{TR}_t = \max(H_t - L_t, |H_t - C_{t-1}|, |L_t - C_{t-1}|)$ (`source-reported`).
     6. *Williams %R (Williams%R-14):* Lookback $n=14$, $-100 \times (H_{14} - C) / (H_{14} - L_{14})$, bounded in $[-100, 0]$ (`source-reported`).
     7. *Rate of Change (ROC-12):* Lookback $n=12$, $100 \times (C_t - C_{t-12}) / C_{t-12}$ (`source-reported`).
3. **Step 3: Channel-Wise Continuous Wavelet Transform (CWWT) (`source-reported`):**
   - For each indicator $m \in \{1, \dots, 7\}$, apply causal Morlet CWT ($\omega_0 = 6$) across $S=32$ uniformly spaced integer scales $s \in \{1, 2, \dots, 32\}$:
     $$W_m(s, t) = \frac{1}{\sqrt{s}} \sum_{\tau = t - 6s}^{t} \text{TI}_m(\tau) \, \psi^*\left(\frac{t - \tau}{s}\right)$$
   - Truncated strictly at current time $t$ to preserve causality; zero-padded for $\tau > t$. A burn-in window of $192$ trading days ($6 \times 32$) is excluded from training folds (`source-reported`).
   - Modulus matrix: $\mathbf{Z}_t = [|W_1(s, t)|, \dots, |W_7(s, t)|] \in \mathbb{R}^{32 \times 7}$ (`source-reported`).
4. **Step 4: Normalization and Lookback Sequencing (`source-reported`):**
   - Denoised OHLCV channels are Min-Max scaled to $[0, 1]$ using training-fold bounds (`source-reported`).
   - Causal sequence window $w=20$ trading days: $\hat{\mathbf{X}}_t \in \mathbb{R}^{20 \times 5}$ (`source-reported`).

### Architecture & Dual-Branch Representation

- **Temporal Branch (CNN-BiLSTM) (`source-reported`):**
  - 1D Convolution: $d_{\text{cnn}} = 64$ filters, kernel size $k=3$, ReLU activation: $\mathbf{H}_{\text{cnn}} = \text{ReLU}(\text{Conv1D}(\hat{\mathbf{X}}_t; \mathbf{W}_{\text{cnn}})) \in \mathbb{R}^{18 \times 64}$ (`source-reported`).
  - BiLSTM Layer 1: $d_{\text{lst1}} = 32$ units, returns sequence $\in \mathbb{R}^{18 \times 64}$ (`source-reported`).
  - BiLSTM Layer 2: $d_{\text{lst2}} = 64$ units, returns concatenated final forward and backward states: $\mathbf{h}_{\text{temp}} = [\vec{\mathbf{h}}_{18}; \overleftarrow{\mathbf{h}}_1] \in \mathbb{R}^{128}$ (`source-reported`).
  - Projection: $\mathbf{u}_{\text{temp}} = \text{ReLU}(\mathbf{W}_{\text{proj}}^{(1)} \mathbf{h}_{\text{temp}} + \mathbf{b}_{\text{proj}}^{(1)}) \in \mathbb{R}^{32}$ ($d_{\text{fus}} = 32$) (`source-reported`).
- **Spectral Branch (Transformer) (`source-reported`):**
  - Input: $\mathbf{Z}_t \in \mathbb{R}^{32 \times 7}$ (treating $S=32$ scales as tokens and $M=7$ indicators as channel features). No positional encoding is added; intrinsic monotonic frequency ordering of Morlet scales is preserved (`source-reported`).
  - Layer 1: 4 attention heads, $d_k = d_v = 16$, dropout $p=0.2$ (`source-reported`).
  - Layer 2: 4 attention heads, $d_k = d_v = 32$, dropout $p=0.2$ (`source-reported`).
  - Scale Attention Pooling: Learned attention score per scale token: $e_s = \mathbf{z}_s^{(\text{penult})} \cdot \mathbf{w}_{\text{pool}} + b_{\text{pool}}$; $w_s = \text{softmax}(e_s)$; pooled representation $\mathbf{h}_{\text{spec}}^{(\text{raw})} = \sum_{s=1}^{32} w_s \mathbf{z}_s^{(\text{penult})} \in \mathbb{R}^7$ (`source-reported`).
  - Projection: $\mathbf{u}_{\text{spec}} = \text{ReLU}(\mathbf{W}_{\text{proj}}^{(2)} \mathbf{h}_{\text{spec}}^{(\text{raw})} + \mathbf{b}_{\text{proj}}^{(2)}) \in \mathbb{R}^{32}$ (`source-reported`).
- **Vertical Attention Fusion (VAF) (`source-reported`):**
  - Meta-sequence: $\mathbf{S} = [\mathbf{u}_{\text{temp}}^\top; \mathbf{u}_{\text{spec}}^\top] \in \mathbb{R}^{2 \times 32}$ (`source-reported`).
  - Attention logits: $\mathbf{e} = \tanh(\mathbf{S} \mathbf{W}_{\text{gate}} + \mathbf{b}_{\text{gate}}) \in \mathbb{R}^{2 \times 1}$ with $d_{\text{gate}} = 1$ (`source-reported`).
  - Softmax weighting: $\boldsymbol{\alpha} = \text{softmax}((\mathbf{e} \mathbf{w}_{\text{att}})^\top) = [\alpha_{\text{temp}}, \alpha_{\text{spec}}]^\top \in \mathbb{R}^2$ (`source-reported`).
  - Fused representation: $\mathbf{h}_{\text{fused}} = \alpha_{\text{temp}} \mathbf{u}_{\text{temp}} + \alpha_{\text{spec}} \mathbf{u}_{\text{spec}} \in \mathbb{R}^{32}$ (`source-reported`).
- **Decoder & Objective (`source-reported`):**
  - Recurrent expansion: `RepeatVector(5)` unrolls $\mathbf{h}_{\text{fused}}$ into a length-5 sequence (`source-reported`).
  - Single-layer BiLSTM decoder: 64 hidden units, dropout $p=0.4 \implies \mathbf{H}_{\text{dec}} \in \mathbb{R}^{64}$ (`source-reported`).
  - Output projection: $\hat{y} = \mathbf{W}_{\text{out}} \cdot \text{Dropout}(\text{ReLU}(\mathbf{W}_{\text{dec}} \mathbf{H}_{\text{dec}} + \mathbf{b}_{\text{dec}})) + b_{\text{out}}$, where $\hat{y} \in [0, 1]$ represents normalized next-step closing price $\tilde{C}_{t+1}$ (`source-reported`).
  - Training Loss: Huber loss with threshold $\delta = 0.1$:
    $$\mathcal{L}_{0.1}(y, \hat{y}) = \begin{cases} \frac{1}{2}(y - \hat{y})^2 & \text{if } |y - \hat{y}| \le 0.1 \\ 0.1(|y - \hat{y}| - 0.05) & \text{otherwise} \end{cases}$$
  - Optimizer: Adam ($\eta = 10^{-3}$, $\beta_1 = 0.9$, $\beta_2 = 0.999$), batch size 32, max 50 epochs, early stopping patience 10 (`source-reported`).

### Trading Signal Logic & Position Sizing

- **Predicted Return:**
  $$\hat{r}_{t+1} = \frac{\hat{p}_{t+1} - p_t}{p_t}$$
  where $\hat{p}_{t+1}$ is the denormalized predicted closing price and $p_t$ is the actual close at time $t$ (`source-reported`).
- **Strategy 1: WaVeFuse Directional ($\text{WaVeFuse}_{\text{directional}}$) (`source-reported`):**
  - *Long Entry:* $\hat{r}_{t+1} > 0$.
  - *Exit (Flat):* $\hat{r}_{t+1} \le 0$.
  - *Position:* Long-only or flat. No shorting in equity benchmark (`source-reported`).
- **Strategy 2: WaVeFuse Risk-Adjusted ($\text{WaVeFuse}_{\text{risk-adjusted}}$) (`source-reported`):**
  - *Volatility-Conditioned Long Entry:* $\hat{r}_{t+1} > 0.5 \times \sigma_t^{(20)}$, where $\sigma_t^{(20)}$ is the 20-day rolling sample standard deviation of realized daily returns (`source-reported`).
  - *Threshold Coefficient:* $0.5$ tuned via grid search on validation fold over $[0.3, 0.7]$ (`source-reported`).
  - *Exit (Flat):* $\hat{r}_{t+1} \le 0.5 \times \sigma_t^{(20)}$ (`source-reported`).
- **Turnover Management (`source-reported`):**
  - Trades execute only on signal state changes (transition from flat to long or long to flat) to minimize turnover (`source-reported`).
- **Position Sizing (`source-reported`):**
  - All-in / all-out single asset exposure: 100% invested capital when long, 0% when flat (`source-reported`). No leverage; uninvested cash earns 0% (`source-reported`).

## Required data

- **Instruments & Universe:**
  - Major global equity indices: KOSPI (`^KS11`), DAX (`^GDAXI`), NYSE Composite (`^NYA`), Russell 2000 (`^RUT`) (`source-reported`).
- **Venue:**
  - National equity exchanges (KRX, Deutsche Börse, NYSE, US Equities); public daily data retrieved from Yahoo Finance (`source-reported`).
- **Timeframe & Session Conventions:**
  - Daily trading-session frequency (`source-reported`).
  - Strict calendar handling: Non-trading days (weekends, national exchange holidays, suspension dates) are excluded entirely rather than forward-filled or interpolated, ensuring continuous trading-time progression without synthetic zero-volatility intervals (`source-reported`).
- **Fields:**
  - Raw Open, High, Low, Close, Volume (OHLCV) (`source-reported`).
- **Point-in-Time & Validation Structure:**
  - Rolling-origin walk-forward validation (WFV): Fixed training window $w_{\text{train}} \approx 5$ years ($\sim 1,250 - 1,300$ trading days), validation window $w_{\text{val}} = 90$ trading days, step size $s = 21$ trading days (`source-reported`).
  - Out-of-sample holdout test partition: Terminal $N_{\text{test}} = 365$ trading days of 2023 (`source-reported`).
  - Normalization parameters (MinMax $[0, 1]$) and DWT universal thresholds are fitted exclusively on each training fold $\mathcal{D}_{\text{train}}^{(k)}$ and frozen across subsequent validation and test sets to prevent look-ahead bias (`source-reported`).

## Execution assumptions

- **Execution Timing & Fill Model:**
  - Trades are assumed to execute at the daily closing price $p_t$ on days when the signal changes state (`source-reported`).
  - *Execution Timing Label:* In real trading, execution at the exact closing print after observing that same close is physically impossible without look-ahead; practical execution requires either executing on the Market-on-Close (MOC) auction using near-close snapshot estimates, or filling at the next-day Open ($t+1$) (`research-proposed`).
- **Transaction Costs:**
  - 10 basis points ($0.10\%$) deducted per trade round-trip or state change (`source-reported`).
- **Slippage, Spread, & Market Impact:**
  - Omitted by primary source: Backtest assumes infinite liquidity at index closing prices without price impact or bid-ask spread friction (`source-reported`).
  - For real-world implementation on liquid index ETFs (e.g., SPY, IWM) or index futures (e.g., E-mini S&P, DAX futures), an additional 2 to 5 bps half-spread plus slippage buffer must be modeled (`research-proposed`).
- **Borrow & Shorting:**
  - Long-only benchmark; no borrow fees or short margin assumptions evaluated in the primary paper (`source-reported`).
- **Capital & Compounding:**
  - Initial capital: 10,000 currency units (`source-reported`).
  - Compounded portfolio equity (`source-reported`).

## Evidence

### Source-reported

All empirical figures below trace directly to Bohra & Vijay (`arXiv:2609.14733v1`, Tables 7, 9, 10, 11, 12, 13, 14, 15):

1. **Baseline Model Forecasting Comparison (Out-of-Sample Test Set 2023, Table 7):**
   - *KOSPI:* WaVeFuse achieves MAE 12.30, RMSE 14.96, MAPE 0.49% (vs. BiLSTM: 15.28 / 18.84 / 0.61%; CNN: 17.62 / 22.15 / 0.71%; Transformer: 13.81 / 16.73 / 0.55%).
   - *DAX:* WaVeFuse achieves MAE 178.34, RMSE 217.93, MAPE 1.14% (vs. BiLSTM: 219.36 / 275.03 / 1.40%; CNN: 255.30 / 330.00 / 1.63%; Transformer: 199.74 / 246.78 / 1.27%).
   - *NYSE Composite:* WaVeFuse achieves MAE 157.51, RMSE 192.21, MAPE 0.90% (vs. BiLSTM: 194.38 / 238.15 / 1.11%; CNN: 225.43 / 281.67 / 1.29%; Transformer: 176.24 / 214.58 / 1.01%).
   - *Russell 2000:* WaVeFuse achieves MAE 30.34, RMSE 37.13, MAPE 0.78% (vs. BiLSTM: 37.28 / 46.14 / 0.96%; CNN: 43.47 / 54.92 / 1.12%; Transformer: 33.94 / 41.28 / 0.87%).
   - *Relative Improvements:* WaVeFuse reduces MAE by 18.6%–19.5% vs. BiLSTM, 30.1%–30.2% vs. CNN, and 10.6%–10.9% vs. Transformer across all four indices.
2. **Statistical Significance & Directional Accuracy (vs. Tuned XGBoost, Table 9):**
   - *KOSPI:* Diebold-Mariano (DM) stat 4.62 ($p < 0.001$), Paired $t$-stat 4.38 ($p < 0.001$), $R^2 = 0.9640$, Directional Accuracy = 78.26%.
   - *DAX:* DM stat 10.38 ($p < 0.001$), Paired $t$-stat 13.97 ($p < 0.001$), $R^2 = 0.8098$, Directional Accuracy = 70.51%.
   - *NYSE Composite:* DM stat 10.24 ($p < 0.001$), Paired $t$-stat 14.33 ($p < 0.001$), $R^2 = 0.8444$, Directional Accuracy = 75.94%.
   - *Russell 2000:* DM stat 10.06 ($p < 0.001$), Paired $t$-stat 14.94 ($p < 0.001$), $R^2 = 0.8276$, Directional Accuracy = 71.23%.
3. **Trading Strategy Performance (365-Day Out-of-Sample Test Set 2023, 10 bps fee, Table 13):**
   - *KOSPI:*
     - $\text{WaVeFuse}_{\text{directional}}$: CAGR 34.4%, Ann Vol 5.9%, Sharpe 4.73 (95% CI: [4.37, 5.09]), Max DD 1.9%, Profit Factor 2.86, Win Rate 63.0%, Final Value 12,760.
     - $\text{WaVeFuse}_{\text{risk-adjusted}}$: CAGR 22.3%, Ann Vol 5.1%, Sharpe 3.63 (95% CI: [3.35, 3.91]), Max DD 1.9%, Profit Factor 2.73, Win Rate 61.2%, Final Value 11,809.
     - XGBoost Baseline: CAGR 10.3%, Ann Vol 5.9%, Sharpe 1.37, Max DD 5.0%, Profit Factor 1.43, Win Rate 46.0%, Final Value 10,847.
     - Buy & Hold: CAGR 4.8%, Ann Vol 14.2%, Sharpe 0.19, Max DD 16.3%, Final Value 10,478.
   - *DAX:*
     - $\text{WaVeFuse}_{\text{directional}}$: CAGR 13.3%, Ann Vol 5.4%, Sharpe 1.96 (95% CI: [1.78, 2.14]), Max DD 4.3%, Profit Factor 1.62, Win Rate 46.6%, Final Value 11,138.
     - $\text{WaVeFuse}_{\text{risk-adjusted}}$: CAGR 9.7%, Ann Vol 4.2%, Sharpe 1.76 (95% CI: [1.60, 1.92]), Max DD 2.3%, Profit Factor 1.90, Win Rate 51.2%, Final Value 10,837.
     - XGBoost Baseline: CAGR -4.4%, Ann Vol 5.1%, Sharpe -1.25, Max DD 8.7%, Profit Factor 0.84, Win Rate 34.0%, Final Value 9,616.
     - Buy & Hold: CAGR 10.2%, Ann Vol 15.8%, Sharpe 0.52, Max DD 12.4%, Final Value 11,015.
   - *NYSE Composite:*
     - $\text{WaVeFuse}_{\text{directional}}$: CAGR 27.8%, Ann Vol 4.3%, Sharpe 5.24 (95% CI: [4.85, 5.63]), Max DD 1.8%, Profit Factor 3.49, Win Rate 63.6%, Final Value 12,305.
     - $\text{WaVeFuse}_{\text{risk-adjusted}}$: CAGR 17.7%, Ann Vol 3.9%, Sharpe 3.68 (95% CI: [3.39, 3.97]), Max DD 2.2%, Profit Factor 2.83, Win Rate 57.9%, Final Value 11,478.
     - XGBoost Baseline: CAGR 10.6%, Ann Vol 4.7%, Sharpe 1.75, Max DD 4.3%, Profit Factor 1.52, Win Rate 49.0%, Final Value 10,886.
     - Buy & Hold: CAGR 5.1%, Ann Vol 13.6%, Sharpe 0.23, Max DD 15.1%, Final Value 10,504.
   - *Russell 2000:*
     - $\text{WaVeFuse}_{\text{directional}}$: CAGR 22.9%, Ann Vol 6.7%, Sharpe 2.83 (95% CI: [2.60, 3.06]), Max DD 6.6%, Profit Factor 2.00, Win Rate 55.3%, Final Value 11,907.
     - $\text{WaVeFuse}_{\text{risk-adjusted}}$: CAGR 26.2%, Ann Vol 6.1%, Sharpe 3.55 (95% CI: [3.27, 3.83]), Max DD 3.5%, Profit Factor 2.75, Win Rate 55.3%, Final Value 12,173.
     - XGBoost Baseline: CAGR 10.5%, Ann Vol 6.9%, Sharpe 1.19, Max DD 6.4%, Profit Factor 1.37, Win Rate 41.4%, Final Value 10,878.
     - Buy & Hold: CAGR 8.4%, Ann Vol 16.9%, Sharpe 0.38, Max DD 15.6%, Final Value 10,814.
   - *Cross-Index Averages (Table 14):*
     - $\text{WaVeFuse}_{\text{directional}}$: Average CAGR 24.6%, Sharpe 3.69, Max DD 3.7%, Win Rate 57.1%, Profit Factor 2.49, Sharpe $> 1.5$ in 4/4 indices.
     - $\text{WaVeFuse}_{\text{risk-adjusted}}$: Average CAGR 19.0%, Sharpe 3.16, Max DD 2.5%, Win Rate 56.4%, Max DD $< 5\%$ in 4/4 indices.
     - XGBoost Baseline: Average CAGR 6.8%, Sharpe 0.77, Max DD 6.1%, Win Rate 42.6%, Sharpe $> 1.5$ in only 1/4 indices.
     - Buy & Hold: Average CAGR 7.1%, Sharpe 0.33, Max DD 14.8%.
4. **Stress Testing Decomposition (KOSPI KS11 Frozen-Model Evaluation, Table 15):**
   - *COVID-19 Crash (Feb–Apr 2020):*
     - $\text{WaVeFuse}_{\text{directional}}$: Return -0.39%, Sharpe -0.12, Max DD 7.50%, Volatility 18.97%.
     - $\text{WaVeFuse}_{\text{risk-adjusted}}$: Return -6.15%, Sharpe -2.85, Max DD 6.54%, Volatility 11.67%.
     - XGBoost: Return -0.61%, Sharpe -0.17, Max DD 7.60%, Volatility 19.39%.
     - Buy & Hold: Return -11.89%, Sharpe -1.09, Max DD 34.05%, Volatility 49.03%.
   - *Trump Tariff War (Jan–Apr 2025):*
     - $\text{WaVeFuse}_{\text{directional}}$: Return +7.73%, Sharpe 2.13, Max DD 3.42%, Volatility 10.32%.
     - $\text{WaVeFuse}_{\text{risk-adjusted}}$: Return +3.09%, Sharpe 1.49, Max DD 1.31%, Volatility 5.17%.
     - XGBoost: Return +7.96%, Sharpe 2.29, Max DD 3.15%, Volatility 9.88%.
     - Buy & Hold: Return +6.57%, Sharpe 0.91, Max DD 14.14%, Volatility 22.50%.
5. **Component Ablation Degradation (Table 11 & Table 12):**
   - *Omit Wavelet Denoising:* Mean MAE increases by $+18.8\%$ (KOSPI $+18.7\%$, DAX $+19.0\%$, NYSE $+19.1\%$, Russell $+18.4\%$).
   - *Omit CWWT (use raw TIs):* Mean MAE increases by $+11.6\%$ (KOSPI $+11.5\%$, DAX $+11.6\%$, NYSE $+11.8\%$, Russell $+11.3\%$).
   - *Omit VAF (use equal $0.5/0.5$ weighting):* Mean MAE increases by $+5.7\%$ (KOSPI $+5.7\%$, DAX $+5.8\%$, NYSE $+6.0\%$, Russell $+5.4\%$).
   - *Replace BiLSTM Decoder with 2-layer MLP:* Mean MAE increases by $+3.6\%$.
6. **Computational Profile (Table 10):**
   - Total model parameters: 152,116. Model size on disk: 0.68 MB.
   - GPU Training time: 99.42 s (DAX) to 109.36 s (NYSE).
   - Inference latency: 0.95 ms/sample (KOSPI) to 1.26 ms/sample (NYSE).

### Independently reproduced

- Not independently reproduced. All figures and claims reflect direct extraction from the primary text of Bohra & Vijay (`arXiv:2609.14733v1`, September 2026).

### Negative evidence

1. **European Low-Amplitude Market Frictional Failure (DAX Win Rate 46.6%):**
   - Despite a high directional accuracy of 70.51% on DAX, the unadjusted directional strategy achieved a win rate of only 46.6% in active trading (`source-reported`).
   - Many correctly predicted daily price moves on DAX were too small to clear the 10 bps transaction fee hurdle, confirming that directional accuracy does not guarantee trading profitability when signal magnitude is low relative to costs (`source-reported`).
2. **Q4 2023 Out-of-Distribution Momentum Shock:**
   - In Q4 2023, the DAX underwent an extraordinary $+15\%$ appreciation, causing prediction residuals to spike and depressing test $R^2$ to 0.8098 (`source-reported`).
   - Rapid, relentless bull trends can lead the spectral branch to misclassify high-momentum moves as transient volatility spikes, temporarily underallocating to the temporal branch.
3. **Macroeconomic News Blindness:**
   - The model is strictly unimodal (OHLCV + derived indicators) and cannot anticipate sudden exogenous macro announcements, central bank surprises, or geopolitical news (`source-reported`).

## Falsification plan

To falsify the hypothesis that WaVeFuse generates genuine, economically persistent alpha that survives market frictions, the following operational tests are defined:

1. **Test 1: Next-Day Open Execution and Spread Sensitivity (`research-proposed`):**
   - *Setup:* Re-run the backtest across KOSPI, DAX, NYSE, and Russell 2000 using next-day Open ($p_{t+1}^{\text{open}}$) fills rather than same-day Close ($p_t^{\text{close}}$), and incorporate realistic half-spreads (5 bps) plus 10 bps taker fees.
   - *Decision Rule:* If the mean annual CAGR drops below the Buy & Hold benchmark or the Sharpe ratio drops below 1.0, the reported alpha is falsified as an artifact of same-day close fill timing and fee underestimation (`research-defined falsification threshold`).
2. **Test 2: Multi-Year Out-of-Sample Walk-Forward Stability (`research-proposed`):**
   - *Setup:* Evaluate WaVeFuse across 5 non-overlapping 1-year test partitions (2018, 2019, 2020, 2021, 2022) rather than the single 2023 window.
   - *Decision Rule:* If the strategy fails to maintain a positive Sharpe ratio in at least 4 of the 5 years, or if maximum drawdown exceeds 15% in any non-crash year, the thesis of regime-adaptive robustness is falsified (`research-defined falsification threshold`).
3. **Test 3: Shuffled Scale-Space Placebo Test (`research-proposed`):**
   - *Setup:* Randomly permute the 32 scale tokens along the sequence dimension of $\mathbf{Z}_t$ before feeding it into the Transformer branch, destroying the monotonic frequency ordering of Morlet wavelets.
   - *Decision Rule:* If the shuffled placebo model achieves forecasting MAE and trading Sharpe ratios within $5\%$ of the canonical WaVeFuse architecture, the claim that inter-scale spectral dependencies provide meaningful economic signal is falsified (`research-defined falsification threshold`).
4. **Test 4: Single-Stock Microstructure Stress Test (`research-proposed`):**
   - *Setup:* Deploy WaVeFuse on individual high-beta single stocks (e.g., TSLA, NVDA) with higher idiosyncratic noise floors than broad market indices.
   - *Decision Rule:* If DWT soft-thresholding attenuates true gap-openings or if the VAF gate collapses to $\alpha_{\text{temp}} \approx 0.5$, the cross-asset portability of the architecture is falsified (`research-defined falsification threshold`).

## Crypto portability

- **Portability Classification:** `adapted / unproven` (`research interpretation`).
- **Primary Source Scope:** The primary paper evaluates developed-market equity indices exclusively (KOSPI, DAX, NYSE Composite, Russell 2000). It does not test or claim applicability to cryptocurrency assets (`source-reported`).
- **Cryptocurrency Adaptation Considerations (`research-proposed`):**
  1. *24/7 Continuous Trading:* Unlike equities with distinct daily session opens, closes, and overnight gaps, crypto trades continuously. Daily candle boundaries (e.g., UTC 00:00) are arbitrary conventions. DWT denoising must be adapted to rolling windows rather than discrete calendar days (`research-proposed`).
  2. *Perpetual Futures Funding Friction:* In crypto perpetual swaps (BTCUSDT, ETHUSDT), holding positions overnight incurs 8-hour funding rates. During strong momentum bull markets, positive funding can exceed 10–30 bps annualized per day, substantially eroding the directional strategy's net returns unless short funding carry is earned (`research-proposed`).
  3. *Fat Tails and Volatility Regime Magnitude:* Crypto volatility regularly spikes by orders of magnitude beyond equity indices. While Huber loss ($\delta=0.1$) handles equity tails, crypto price swings of $10\%-20\%$ in a single day may require dynamic recalibration of the threshold $\delta$ and the volatility filter ($0.5 \times \sigma_t^{(20)}$) (`research-proposed`).
  4. *Microstructure Noise Floor:* Crypto spot and perpetual markets experience substantial tick-level wash trading, fragmented cross-venue liquidity, and exchange latency spikes. DWT decomposition depth $J=2$ may need to be expanded to $J=3$ or $J=4$ to excise crypto-specific microstructural noise (`research-proposed`).

## Limitations

1. **Single Out-of-Sample Window:** Strategy backtesting is evaluated over a single 365-day holdout window (calendar year 2023) (`source-reported`). Sharpe ratios over a single 1-year window carry wide asymptotic confidence intervals ($SE \approx 0.15 - 0.20$) and cannot be extrapolated as asymptotic expected returns (`source-reported`).
2. **Idealized Execution Mechanics:** The backtest assumes fills at exact daily closing prices without bid-ask spreads, market impact, or partial fill friction (`source-reported`).
3. **Fixed Decomposition Parameters:** DWT level $J=2$ and CWT scale count $S=32$ are fixed across all assets and regimes without dynamic tuning (`source-reported`).
4. **Lack of Macro / Order Flow Awareness:** The architecture is restricted to OHLCV price-volume data; it has no access to order flow imbalance, level-2 depth, funding rates, open interest, or macro news catalysts (`source-reported`).
5. **Single-Asset Capital Allocation:** No portfolio-level risk parity, cross-sectional ranking, or multi-asset diversification logic is modeled; each index is traded as an independent single-asset mandate (`source-reported`).

## Implementation status

- `not-implemented`
- This record captures research published in arXiv preprint `arXiv:2609.14733v1`. No implementation exists in the current quantitative research stack, PyBroker, NautilusTrader, paper trading, testnet, or live trading systems.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- The inclusion of this document in `alpha-strategy-research` does not constitute strategy approval, validation, or permission for deployment.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[cwt-wavelet-bandpass-mean-reversion-hmm-stress-overlay-2026-09-12]]`
- `[[learnable-wavelet-transformer-long-short-equity-wavelsformer-2026-09-03]]`
- `[[fifo-queue-partial-identification-l2-execution-sensitivity-2026-09-16]]`

## Sources

1. Aashish Bohra and Vivek Vijay. "WaVeFuse: Regime-Adaptive Equity Index Forecasting via Channel-Wise Wavelet Denoising and Vertical Attention Fusion." arXiv preprint `arXiv:2609.14733v1 [cs.AI, q-fin.CP, q-fin.ST]`, submitted September 13, 2026.
   - Abstract: https://arxiv.org/abs/2609.14733
   - Full-Text HTML: https://arxiv.org/html/2609.14733v1
   - Full-Text PDF: https://arxiv.org/pdf/2609.14733v1
   - Canonical DOI: [10.48550/arXiv.2609.14733](https://doi.org/10.48550/arXiv.2609.14733)
