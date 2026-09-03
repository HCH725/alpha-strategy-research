---
schema: strategy-research-record-v1
title: "WaveLSFormer: Learnable Wavelet Transformer for Intraday Long-Short Equity Trading and Risk-Adjusted Return Optimization"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - wavelet-transform
  - transformer
  - long-short
  - equity
  - risk-adjusted-return
  - end-to-end-trading
  - lead-lag
status: research-only
confidence: high
source_as_of: 2026-03-12
sources:
  - "https://doi.org/10.48550/arXiv.2601.13435"
  - "https://arxiv.org/abs/2601.13435"
  - "https://arxiv.org/html/2601.13435v4"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# WaveLSFormer: Learnable Wavelet Transformer for Intraday Long-Short Equity Trading and Risk-Adjusted Return Optimization

## Provenance

- **Primary Source:** Shuozhe Li (University of Texas at Austin), Du Cheng (Northeastern University, Shenyang), Amy Zhang (University of Texas at Austin), and Leqi Liu (University of Texas at Austin, Department of Computer Science & Information, Risk and Operations Management [IROM]), *"A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization"*, arXiv preprint `arXiv:2601.13435v4 [cs.LG, cs.AI, q-fin.CP]`.
- **Submission History:**
  - Version 1 (`v1`): January 19, 2026 (22:41:31 UTC).
  - Version 2 (`v2`): January 30, 2026 (20:14:14 UTC).
  - Version 3 (`v3`): March 2, 2026 (18:01:11 UTC).
  - Version 4 (`v4`): March 12, 2026 (00:44:46 UTC).
- **Canonical Digital Object Identifier (DOI):** [10.48550/arXiv.2601.13435](https://doi.org/10.48550/arXiv.2601.13435).
- **Traceable Full Text URLs:**
  - Abstract: [https://arxiv.org/abs/2601.13435](https://arxiv.org/abs/2601.13435)
  - Full HTML: [https://arxiv.org/html/2601.13435v4](https://arxiv.org/html/2601.13435v4)
  - Canonical PDF: [https://arxiv.org/pdf/2601.13435](https://arxiv.org/pdf/2601.13435)
  - TeX Source Package: [https://arxiv.org/src/2601.13435](https://arxiv.org/src/2601.13435)
- **Academic Context:** Peer-reviewed presentation associated with ICLR 2026 workshop tracks (OpenReview: *"WaveLSFormer: A Learnable Wavelet Transformer for Long-Short Equity Trading"*).
- **Source-Identity Deduplication:** Repository audit confirmed zero matching records for `2601.13435`, `WaveLSFormer`, `Shuozhe Li`, or `Leqi Liu`. Previous transformer/wavelet records in this repository (e.g., `bitcoin-informer-transformer-gmadl-high-frequency-2026-09-03.md`, `cross-asset-futures-vsn-xlstm-sharpe-optimal-portfolio-2026-09-03.md`, `lstm-learnable-sector-embeddings-cross-sectional-reversal-2026-09-02.md`) address completely separate architectures, data universes, and problem formulations.
- **Historical Data Pool & Provider:**
  - Price & Volume Data: Commercial market data API `polygon.io` providing 1-hour OHLCV bars over roughly 10 years.
  - Sector/Industry Classifications: Curated stock lists published by `StockAnalysis.com`.
  - Timeline Sample: 5 years of hourly U.S. equity data spanning October 29, 2020 to October 29, 2025.
  - Temporal Partitioning: Chronological 70% / 10% / 20% split:
    - Training period: 5,292 hourly steps.
    - Validation period: 756 hourly steps.
    - Test period (out-of-sample): 1,512 hourly steps.

## Economic mechanism

### Source-reported

Conventional deep learning models applied to financial markets predominantly frame trading as a sequential point-wise price or return forecasting task optimized via standard regression loss functions (such as Mean Squared Error $\text{MSE}$ or Mean Absolute Error $\text{MAE}$). Li et al. (2026) demonstrate that this conventional paradigm suffers from three critical structural deficiencies:

1. **Objective Mismatch:** Minimizing point-wise return forecast errors does not optimize trading profits. Trading performance is determined by sequential position allocations $\tilde{w}_t \in [-1, 1]$ and their cumulative realized P&L $R_{t+1} = 1 + \tilde{w}_t \cdot r_{t+1}$, rather than the numeric precision of $\hat{r}_{t+1}$. Regression loss functions penalize positive and negative prediction errors symmetrically, whereas in real trading, taking an aggressive position with the incorrect sign is catastrophic, while small deviations around zero are negligible. Furthermore, minimizing regression losses under non-stationary noise merely approximates unconditional expectations $\mathbb{E}[\ell_t \mid \mathbf{X}_{t-1}]$ rather than extracting profitable decision signals.
2. **High-Frequency Noise Gradient Corruption:** Financial time series possess an exceptionally low signal-to-noise ratio (SNR). Direct end-to-end backpropagation exposes deep network backbones (LSTMs or Transformers) to high-frequency microstructure noise gradients, which mislead parameter updates and cause rapid overfitting. While classical Discrete Wavelet Transforms (DWT, such as Haar or Daubechies) decompose signals into frequency sub-bands, they rely on rigid, hand-crafted, non-trainable filter kernels that fail to adapt to task-specific market regimes. Moreover, naive concatenation of multi-frequency representations allows volatile high-frequency components to destabilize representation learning.
3. **Optimizer Deadlock in Direct Position Losses:** Formulating position learning directly via tanh-activated continuous allocations $\tanh(p_t)$ creates severe gradient saturation: as logits approach exposure bounds, $\tanh'(\cdot) \to 0$, causing backpropagated parameter gradient norms to collapse toward zero and deadlocking the optimizer in sub-optimal local minima.

To overcome these structural bottlenecks, the authors introduce **WaveLSFormer**, an end-to-end framework integrating:
- An **end-to-end learnable finite impulse response (FIR) wavelet filter bank** governed by differentiable real fast Fourier transform (rFFT) spectral regularizers that enforce tight-frame Parseval energy conservation and sharp low/high frequency band separation;
- A **Low-Guided High-Frequency Injection (LGHI)** cross-attention module that computes self-attention maps strictly from the stable low-frequency trend branch and injects high-frequency details through a gated residual connection initialized with a conservative gate ($\beta_0 \approx 0.0067$);
- A **soft-label trading objective** $y_t = \sigma(k \ell_t)$ ($k=45$) that scales directional confidence by future return magnitude, coupled with an overfitting penalty (capping batch annualized ROI at 100%) and an exponentially decaying capped Sharpe ratio regularizer;
- A **validation-calibrated risk-budget normalization** rule that scales position size to target unit leverage and enforces an active trading dead zone ($\tau = 0.01$).

### Research interpretation

The falsifiable alpha hypothesis is that **decoupling trend representation from transient microstructure noise via an end-to-end learnable FIR wavelet filter bank and asymmetric low-guided attention injection—combined with direct soft-label directional confidence training and batch Sharpe regularization under a fixed validation risk budget—extracts genuine lead-lag and momentum/reversal co-movements across intra-industry equity constituents, outperforming standard point-wise regression forecasters and fixed wavelet hybrids without expanding tail drawdown.**

The strategy captures two distinct structural market phenomena:
1. **Intra-Industry Information Diffusion (Lead-Lag Spillover):** By screening sector peers using Dynamic Time Warping (DTW) and non-parametric Granger causality, the model conditions the target asset's trading decisions on informative lead-lag signals from economically related firms, capturing delayed price adjustments across large-cap and mid-cap sector constituents.
2. **Frequency-Decomposed Signal Synthesis:** Macroeconomic trends and sector momentum reside primarily in low-frequency bands, whereas idiosyncratic microstructure shocks and temporary liquidity imbalances reside in high-frequency residuals. By forcing cross-attention queries and keys to originate exclusively from the low-frequency trend path, the model prevents transient microstructure fluctuations from dominating positional bias while preserving high-frequency timing refinements.

## Signal

### Multi-Asset Input Space & Lookback Window

The model operates on a rolling lookback window of $L = 96$ hourly bars (representing approximately 14.8 trading days at 6.5 market hours per day):
$$\mathbf{X}_{t-1} = \big[\boldsymbol{\ell}_{t-L}, \dots, \boldsymbol{\ell}_{t-1}\big] \in \mathbb{R}^{d \times L}$$
where each vector $\boldsymbol{\ell}_t = (\ell_{1,t}, \dots, \ell_{d,t})^\top$ comprises log price returns across $d$ retained industry constituents:
$$\ell_{j,t} = \log\left(\frac{\text{Close}_{j,t}}{\text{Open}_{j,t}}\right) = \log(1 + r_{j,t})$$

### Pre-Execution Asset Selection Pipeline

To isolate informative contextual peers without data snooping, all asset screening is conducted strictly on in-sample training data:
1. **Sector Proxy DTW Filtering:** For each industry, constituent candidates are compared against the liquid sector ETF proxy. Historical log-return series over a fixed lookback window are evaluated via Dynamic Time Warping (DTW). Candidates whose DTW distance exceeds the empirical median (50th percentile) are discarded to eliminate idiosyncratic outliers.
2. **Directional Non-Parametric Granger Causality:** Pairwise tests are executed using the Diks & Panchenko (2006) non-parametric test on candidate log-return series. P-values are adjusted via the Benjamini-Hochberg False Discovery Rate (BH-FDR) procedure. Only assets exhibiting statistically significant directed causality with the target asset $j^\star$ ($p_{\text{adj}} < 0.05$ in at least one direction) are retained in the multi-asset tensor $\mathbf{X}$. (For example, in Renewable Energy, 8 assets—AEP, AWK, CMS, CNP, NEE, PEG, WEC, XEL—were retained as contextual peers for target asset CWEN out of 16 candidates).

### Neural Wavelet Front-End & Differentiable Spectral Regularization

The input series is decomposed into low-pass ($s_t$) and high-pass ($n_t$) components using 1D finite impulse response (FIR) convolution filters:
$$y[n] = \sum_{k=0}^{L_{\text{kernel}}-1} \theta_k \, x[n-k]$$
Filter weights $\boldsymbol{\theta} \in \mathbb{R}^{L_{\text{kernel}}}$ act as the time-domain impulse response $h[k] = \theta_k$. Its frequency response is obtained via real Fast Fourier Transform (rFFT) on an $n_{\text{fft}} = 81$ grid:
$$H(e^{\mathrm{j}\omega}) = \sum_{k=0}^{L_{\text{kernel}}-1} \theta_k \, e^{-\mathrm{j}\omega k}$$

To prevent degenerate solutions and enforce tight-frame wavelet behavior, the filter bank is trained under a four-component differentiable spectral loss:
$$\mathcal{L}_{\text{wavelet}} = \lambda_{\text{spec}} \big(\mathcal{L}_{\text{low}} + \mathcal{L}_{\text{high}}\big) + \mathcal{L}_{\text{overlap}} + \mathcal{L}_{\text{parseval}} + \mathcal{L}_{\text{ratio}}$$
where:
- Out-of-band energy suppression ($p=2$):
  $$\mathcal{L}_{\text{low}} = \sum_\omega (\omega / \pi)^2 |G_{\text{low}}(\omega)|^2, \qquad \mathcal{L}_{\text{high}} = \sum_\omega (1 - \omega / \pi)^2 |G_{\text{high}}(\omega)|^2$$
- Spectral overlap penalty: $\mathcal{L}_{\text{overlap}} = |G_{\text{low}}|^2 \cdot |G_{\text{high}}|^2$
- Tight-frame Parseval conservation: $\mathcal{L}_{\text{parseval}} = \big(|G_{\text{low}}|^2 + |G_{\text{high}}|^2 - 2\big)^2$
- Energy ratio hinge penalty: $\rho = \frac{|G_{\text{high}}|^2}{|G_{\text{low}}|^2 + \varepsilon}$, with $\mathcal{L}_{\text{ratio}} = \max(\rho - \rho_{\max}, 0) + \max(\rho_{\min} - \rho, 0)$
- Default spectral weight: $\lambda_{\text{spec}} = 10$.

### Low-Guided High-Frequency Injection (LGHI)

Let $L \in \mathbb{R}^{T \times d}$ and $H \in \mathbb{R}^{T \times d}$ denote the low-frequency and high-frequency latent representations. Attention weights are computed exclusively from the low-frequency branch to shield queries and keys from high-frequency noise:
$$A(L) = \mathrm{softmax}\left(\frac{(L W_Q)(L W_K)^\top}{\sqrt{d_k}}\right)$$
$$Z(L, H) = A(L) (H W_V) W_O$$
The fused representation is injected through a gated residual connection:
$$Y = L + \beta \, Z(L, H), \qquad \beta = \sigma(\gamma)$$
where $\gamma$ is a learnable scalar initialized conservatively to $\gamma = -5$, yielding $\beta_0 = \sigma(-5) \approx 0.0067$. This small-gate initialization prevents gradient explosion in deep Transformer stacks and vanishing gradients in recurrent networks.

### Transformer Backbone & Trading Objective

The fused representation $Y$ is processed by a 6-layer Transformer encoder ($d_{\text{model}} = 512$, $d_{\text{ff}} = 1024$, $n_{\text{heads}} = 128$, input length 96, 128-dimensional Time2Vec temporal embedding, ProbSparse attention with distillation).

The network outputs a scalar logit $p_t = f_\theta(\mathbf{X}_{t-1}) \in \mathbb{R}$, yielding probability $P_t = \sigma(p_t)$. Training optimizes:
$$\mathcal{L}_{\text{train}} = \mathcal{L}_{\text{trade}} + \mathcal{L}_{\text{penalty}} + \mathcal{L}_{\text{sharpe}} + \mathcal{L}_{\text{wavelet}}$$

1. **Soft-Label Cross-Entropy Loss:** Future return $\ell_t$ is mapped to a calibrated probabilistic soft target:
   $$y_t = \sigma(k \, \ell_t), \qquad k = 45 \text{ (calibrated so that } \sigma(k \cdot 5\%) \approx 0.90\text{)}$$
   $$\mathcal{L}_{\text{trade}}(t) = -y_t \log P_t - (1 - y_t) \log(1 - P_t)$$
2. **Batch Overfitting Penalty:** Annualized strategy ROI is capped at $R_{\text{ann}}^{\max} = 1.0$ (100% ARR). With $H_{\text{year}} = 252 \times 6.5 = 1638$ hours and batch span $H_{\mathcal{B}}$, the implied batch ROI threshold is $T_{\mathcal{B}} = (1 + R_{\text{ann}}^{\max})^{H_{\mathcal{B}} / H_{\text{year}}} - 1$:
   $$\mathcal{L}_{\text{penalty}} = \lambda_{\text{roi}} \big[\max(R_{\mathcal{B}} - T_{\mathcal{B}}, 0)\big]^2, \qquad \lambda_{\text{roi}} = 0.5$$
3. **Capped Sharpe Ratio Regularizer:**
   $$\mathcal{L}_{\text{sharpe}} = \exp\left(-\alpha \cdot \min\left(\frac{3}{\sqrt{K}}, \; \frac{\mathbb{E}[R_p]}{\sigma(R_p) + \varepsilon}\right)\right)$$
   where $K = 1638$, $\alpha > 0$ controls penalty intensity, and the cap $3/\sqrt{K}$ prevents gradient dominance.

### Position Mapping & Fixed Risk Budget

At inference time, raw logit $p_t$ is mapped to continuous position $w_t$:
$$w_t = 2\sigma(p_t) - 1 = \tanh(p_t / 2) \in [-1, 1]$$
To prevent aggressive bet sizing from confounding signal alpha, the position is rescaled by the validation-period mean absolute exposure:
$$s_{\text{val}} = \frac{1}{T_{\text{val}}} \sum_{t \in \mathcal{D}_{\text{val}}} |w_t|, \qquad \hat{w}_t = \frac{w_t}{s_{\text{val}}}$$
The executable position $\tilde{w}_t$ enforces a dead zone $\tau = 0.01$ and clips at target leverage $L = 1.0$:
$$\tilde{w}_t = \begin{cases} 0, & |\hat{w}_t| < \tau = 0.01 \\ \max(-L, \min(L, \hat{w}_t)), & \text{otherwise} \end{cases}$$

## Required data

- **Asset Universe:** U.S. equities categorized into liquid industry sectors via `StockAnalysis.com`. Candidate sectors are screened by an annualized return threshold (ARR $\ge 10\%$) on the training period:
  - Retained Sectors (6): Biotechnology (ARR 33.99%), Medical Devices (ARR 12.49%), Semiconductors (ARR 14.11%), Renewable Energy (ARR 10.15%), Life Insurance (ARR 12.77%), Retail Consumer Goods (ARR 11.83%).
  - Excluded Sectors (8): Regional Banks (5.71%), Engineering Construction (8.21%), Electronic Components (8.90%), IT Services (8.72%), Software Application (7.64%), Specialty Industrial Machinery (4.41%), Utilities Electric (4.13%), Real Estate REITs (2.45%).
- **Reference Instruments:** Sector-specific ETFs used as benchmarks for Dynamic Time Warping (DTW) distance screening.
- **Timeframe:** 1-hour OHLCV bars.
- **Data Vendor / Source:** Commercial API provider `polygon.io` (5-year evaluation window: October 29, 2020 to October 29, 2025).
- **Features Required:** Within-bar log returns $\ell_{j,t} = \log(\text{Close}_{j,t} / \text{Open}_{j,t})$ for target stock and all FDR-Granger retained sector peers.
- **Point-in-Time Discipline:** All DTW clustering, Granger causality matrices, validation scaling factors $s_{\text{val}}$, and hyperparameter checkpoints are fitted strictly on past training/validation splits; zero test-set leakage.

## Execution assumptions

- **Execution Timing:** At the beginning of hour $t$, the model ingests historical bars through hour $t-1$, computes signal $p_t$, and enters position $\tilde{w}_t$ held over hour $t+1$.
- **Fill Price:** Idealized execution at open price of hour $t+1$ (single-period return $R_{t+1} = 1 + \tilde{w}_t \cdot r_{j^\star, t+1}$).
- **Friction & Cost Assumptions:** The authors explicitly note in Section VIII-A that their empirical evaluation employs idealized trading assumptions:
  - Maker/taker transaction fees: 0.0 bps (omitted).
  - Bid-ask spread: 0.0 bps (omitted).
  - Market impact / slippage: 0.0 bps (omitted).
  - Short-borrow fee / borrow availability constraints: Omitted (frictionless shorting).
- **Provenance Gap:** The complete omission of transaction costs in an hourly rebalancing strategy constitutes a critical limitation and provenance gap.

## Evidence

### Source-reported

All figures below are transcribed directly from Li et al. (arXiv:2601.13435v4, Sections VI–VII, Tables II–IX), evaluated across 10 random seeds on the held-out test period (1,512 hourly steps):

#### Overall Performance Across Backbones (Table VIII & IX, 6-Industry Average, 10 Seeds)

| Model Architecture | Parameters (M) | FLOPs (G) | Out-of-Sample Test ROI | Out-of-Sample Test Sharpe |
| :--- | :---: | :---: | :---: | :---: |
| Plain MLP | 8.146M | 3.468G | $0.075 \pm 0.023$ | $0.813 \pm 0.311$ |
| Wavelet + MLP | 8.151M | 10.412G | $0.165 \pm 0.045$ | $1.079 \pm 0.139$ |
| Plain LSTM | 12.538M | 492.614G | $0.191 \pm 0.029$ | $1.656 \pm 0.495$ |
| Wavelet + LSTM | 13.298M | 530.862G | $0.317 \pm 0.049$ | $1.879 \pm 0.221$ |
| Plain Transformer | 15.928M | 665.921G | $0.225 \pm 0.056$ | $1.024 \pm 0.122$ |
| **WaveLSFormer (Ours)** | **15.943M** | **659.742G** | **$0.607 \pm 0.045$** | **$2.157 \pm 0.166$** |

#### Industry-by-Industry Breakdown (Table VIII, Mean $\pm$ Std over 10 Seeds)

- **Biotechnology:**
  - WaveLSFormer: ROI **$0.601 \pm 0.034$**, Sharpe **$1.695 \pm 0.050$**
  - Plain Transformer: ROI $0.124 \pm 0.066$, Sharpe $0.511 \pm 0.189$
  - Wavelet + LSTM: ROI $0.173 \pm 0.026$, Sharpe $0.934 \pm 0.102$
- **Semiconductors:**
  - WaveLSFormer: ROI **$1.104 \pm 0.053$**, Sharpe **$2.555 \pm 0.081$**
  - Plain Transformer: ROI $0.333 \pm 0.021$, Sharpe $1.134 \pm 0.035$
  - Wavelet + LSTM: ROI $0.465 \pm 0.069$, Sharpe $2.072 \pm 0.227$
- **Renewable Energy:**
  - WaveLSFormer: ROI **$0.423 \pm 0.074$**, Sharpe **$2.775 \pm 0.365$**
  - Plain Transformer: ROI $0.169 \pm 0.018$, Sharpe $1.173 \pm 0.113$
  - Wavelet + LSTM: ROI $0.221 \pm 0.022$, Sharpe $1.656 \pm 0.061$
- **Life Insurance:**
  - WaveLSFormer: ROI **$0.185 \pm 0.004$**, Sharpe $1.472 \pm 0.039$
  - Plain Transformer: ROI $0.120 \pm 0.010$, Sharpe $0.976 \pm 0.086$
  - Wavelet + LSTM: ROI $0.168 \pm 0.025$, Sharpe **$1.783 \pm 0.195$**
- **Medical Devices:**
  - WaveLSFormer: ROI **$0.669 \pm 0.049$**, Sharpe **$1.979 \pm 0.167$**
  - Plain Transformer: ROI $0.289 \pm 0.036$, Sharpe $1.060 \pm 0.125$
  - Wavelet + LSTM: ROI $0.404 \pm 0.060$, Sharpe $1.937 \pm 0.212$
- **Retail Consumer Goods:**
  - WaveLSFormer: ROI **$0.659 \pm 0.055$**, Sharpe $2.465 \pm 0.293$
  - Plain Transformer: ROI $0.317 \pm 0.187$, Sharpe $1.291 \pm 0.185$
  - Wavelet + LSTM: ROI $0.471 \pm 0.093$, Sharpe **$2.895 \pm 0.528$**

#### Component Ablations (Tables II, IV, V, VI, VII)

1. **Wavelet Front-End (Table IV):** Neural Wavelet (ROI **$0.607 \pm 0.045$**, Sharpe **$2.157 \pm 0.166$**) outperforms Classic Fixed Wavelet (ROI $0.346 \pm 0.048$, Sharpe $1.439 \pm 0.103$) and Plain Transformer (ROI $0.225 \pm 0.056$, Sharpe $1.024 \pm 0.122$).
2. **Frequency Sub-Bands (Table V):** Dual-branch Low+High (ROI **$0.607 \pm 0.045$**, Sharpe **$2.157 \pm 0.166$**) outperforms Low-Freq Only (ROI $0.310 \pm 0.051$, Sharpe $1.148 \pm 0.147$) and High-Freq Only (ROI $0.135 \pm 0.089$, Sharpe $0.546 \pm 0.246$).
3. **Fusion Architecture (Table VI):** Low-Guided Injection (LGHI) (ROI **$0.607 \pm 0.045$**, Sharpe **$2.157 \pm 0.166$**) substantially outperforms naive channel Concatenation (ROI $0.207 \pm 0.048$, Sharpe $0.814 \pm 0.083$).
4. **Sharpe Regularizer & Drawdown (Table VII):**
   - Soft-Label + Sharpe Regularizer: ROI **$0.553 \pm 0.035$**, Sharpe **$2.000 \pm 0.122$**, Maximum Drawdown (MDD) **$9.580\% \pm 1.736\%$**.
   - Soft-Label Only (no Sharpe loss): ROI $0.470 \pm 0.056$, Sharpe $1.400 \pm 0.224$, MDD $15.463\% \pm 2.662\%$.
5. **Supervised Loss Formulation (Table II, Renewable Energy):** Soft-Label Cross-Entropy (ROI **$0.377 \pm 0.045$**, Sharpe **$1.943 \pm 0.311$**) dominates MAE regression (ROI $0.125 \pm 0.061$, Sharpe $0.899 \pm 0.355$) and MSE regression (ROI $0.078 \pm 0.039$, Sharpe $0.586 \pm 0.275$).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Complete Omission of Trading Frictions:** In high-turnover hourly rebalancing with a small position dead zone ($\tau = 0.01$), portfolio turnover is substantial. Under realistic equity commissions and bid-ask spreads (typically 2–5 bps for large caps, 10–20 bps for mid caps), a significant portion or entirety of the gross return ($0.607$ cumulative over 1,512 hours $\approx 4.0 \times 10^{-4}$ per bar $\approx 4.0$ bps per hour) will be consumed by transaction friction.
- **Numerical Instability under Large Gate Values:** The paper proves and empirically demonstrates that setting the LGHI gate parameter $\beta \ge 0.5$ triggers gradient explosions in deep Transformer stacks (spectral radius of layer Jacobians exceeding 1.0) and vanishing gradients in LSTM backbones, causing optimization failure unless initialized at $\gamma = -5$ ($\beta_0 \approx 0.0067$).
- **Deadlock under Direct Tanh Loss:** Direct continuous position training via $-\exp(\sum \tanh(p_t) \ell_t)$ suffers severe gradient saturation, causing parameter gradient norms to collapse toward zero and deadlocking training.
- **Severe Degradation under High-Frequency Signals Alone:** Removing the low-frequency trend path causes average Sharpe to collapse from $2.157$ to $0.546$, proving that high-frequency signals cannot generate standalone alpha without trend gating.

## Falsification plan

To disconfirm or establish strict operational bounds for the WaveLSFormer strategy:

1. **Transaction Cost & Slippage Hurdle Test:** Re-run backtest simulation incorporating 2 bps, 5 bps, and 10 bps proportional round-trip transaction costs and bid-ask spread penalties. If the net Sharpe ratio drops below $0.50$ or annualized net ROI falls below zero at a 5 bps fee level, the strategy's alpha is classified as an artifact of friction-free accounting.
2. **Purged Combinatorial Cross-Validation (CPCV):** Subject the 5-year dataset to 10-fold CPCV with a 24-hour embargo to eliminate temporal autocorrelation leakage. If out-of-sample Sharpe decays by more than $50\%$ relative to sequential walk-forward splits, the model suffers from look-ahead overfitting.
3. **Cross-Sectional Peer Shuffling (Placebo Test):** Replace the FDR-Granger-selected sector peer returns in $\mathbf{X}_{t-1}$ with randomly permuted stock returns drawn from unrelated industries while leaving the target asset's returns intact. If the resulting model achieves performance comparable to the original WaveLSFormer, the claimed intra-industry lead-lag mechanism is falsified.
4. **Classical Fixed Wavelet Benchmark Stress:** Train identical Transformer encoders using standard non-learnable discrete wavelets (Haar, Daubechies db4, Symlet, Coiflet). If a tuned db4 wavelet matches the learnable FIR filter bank, the complexity overhead of end-to-end differentiable rFFT regularization is unjustified.
5. **Dead-Zone & Leverage Sensitivity:** Sweep threshold $\tau \in [0.005, 0.05]$ and leverage target $L \in [0.5, 2.0]$. If the strategy's Sharpe is unstable under modest variations in $\tau$, the signal lacks robustness to execution thresholds.

## Crypto portability

- **Portability Status:** `adapted` / `unproven`.
- **Research Interpretation:**
  - The mechanism is evaluated exclusively on U.S. cash equities (hourly bars). Porting to cryptocurrency represents a research adaptation rather than verified empirical evidence.
  - **24/7/365 Continuous Trading:** Unlike equity markets with 6.5-hour trading days, crypto perpetuals operate without session breaks. The hourly annualization factor must be adjusted from $K = 1638$ to $K = 8760$.
  - **Perpetual Funding Rate Dynamics:** Hourly position holding in crypto perpetuals incurs 8-hour (or 1-hour on certain DEXs) funding payments. Holding net directional exposure in crowded sectors can result in significant negative funding drag.
  - **Exchange Microstructure & Fee Tiers:** Crypto exchanges feature maker/taker fee tiers (e.g., 2–5 bps taker, 0 to -1 bps maker). To survive, WaveLSFormer's continuous position changes must be routed via passive limit orders or adapted to higher-timeframe bars (e.g., 4-hour or daily).
  - **Sector Peer Cointegration:** Crypto tokens within sectors (e.g., DeFi, Layer-1s, AI memecoins) exhibit strong beta co-movements, making DTW and Granger causality highly applicable. However, high survivorship bias and short coin lifespans require dynamic universe reconstitution.

## Limitations

- **Friction-Free Accounting:** Backtests omit transaction fees, bid-ask spread crossing costs, slippage, and borrow costs (`data gap` / `unproven`).
- **Limited Universe Scope:** Empirical evaluation is restricted to 6 specific U.S. equity industries selected via training ARR, creating potential sector-selection bias (`sample limitation`).
- **Fixed Hourly Bar Resolution:** The model was tested exclusively on 1-hour bars; sensitivity to lower (4h, daily) or higher (15m, 5m) frequencies is unknown.
- **Computational Complexity:** With 15.943M parameters and 659.742 GFLOPs per forward pass, retraining the model in an online streaming production pipeline imposes non-trivial hardware requirements.
- **Underspecified Order Routing:** The paper does not model intraday price execution between bar open and close or latency between signal generation and order fill (`underspecified`).

## Implementation status

`not-implemented`. This document constitutes an upstream research evaluation. No implementation in PyBroker, NautilusTrader, paper trading, testnet, or live environments exists or is authorized by this record.

## Adoption boundary

`research-only`.
- Adoption status: `not-approved`.
- Approval scope: `research-only`.
- Presence of this record does not constitute verification of alpha, profitability, or authorization for live or automated deployment.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Methodological standards for temporal purging, embargoing, and cross-validation integrity.
- `[[quant/sharpe-deflated-multiple-testing-2026-08-27]]` — Framework for deflating reported Sharpe ratios under multiple testing and seed selection.
- `[[quant/signal-to-executable-pnl-costs-2026-08-28]]` — Bridge analysis from gross alpha signals to net executable P&L under fees, spreads, and market impact.
- `[[quant/phase8-financial-ml-sample-leakage-contract-2026-08-28]]` — Rules governing leakage prevention and strict in-sample preprocessing.
- `[[quant/phase8-temporal-validation-calibration-uncertainty-2026-08-28]]` — Standards for walk-forward validation and calibration stability.
- `[[quant/equity-cross-sectional-homological-neural-network-mfcf-ranking-2026-09-02]]` — Complementary cross-sectional equity ranking using topological representations.
- `[[quant/lstm-learnable-sector-embeddings-cross-sectional-reversal-2026-09-02]]` — Cross-sectional equity reversal using sector embeddings.
- `[[quant/strata-selective-state-space-intraday-raw-bars-cross-sectional-ranking-2026-09-02]]` — High-frequency state-space cross-sectional ranking across intraday raw bars.

## Sources

1. Shuozhe Li, Du Cheng, Amy Zhang, and Leqi Liu, *"A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization"*, arXiv preprint `arXiv:2601.13435v4 [cs.LG, cs.AI, q-fin.CP]`, submitted January 19, 2026, revised March 12, 2026. DOI: [10.48550/arXiv.2601.13435](https://doi.org/10.48550/arXiv.2601.13435). Stable abstract: [https://arxiv.org/abs/2601.13435](https://arxiv.org/abs/2601.13435). Full text HTML: [https://arxiv.org/html/2601.13435v4](https://arxiv.org/html/2601.13435v4).
2. OpenReview / ICLR 2026 Workshop presentation: *"WaveLSFormer: A Learnable Wavelet Transformer for Long-Short Equity Trading"*, OpenReview forum paper ID for WaveLSFormer.
3. C. Diks and V. Panchenko, *"A new statistic and practical guidelines for nonparametric Granger causality testing"*, *Journal of Economic Dynamics and Control*, vol. 30, no. 9–10, pp. 1647–1669, 2006.
