---
schema: strategy-research-record-v1
title: "Hybrid Neural-Classical Correction for Frozen Time Series Foundation Models: Bilinear-Gated Adaptation and Random Forest Residual Learning for High-Frequency Opening-Hour Return Prediction"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - foundation-models
  - timesfm
  - hybrid-neural-classical
  - high-frequency-trading
  - intraday-opening-hour
  - bilinear-projection
  - random-forest-residual
  - premarket-order-flow
  - parameter-efficiency
status: research-only
confidence: high
source_as_of: 2026-08-09
sources:
  - "Kasun Dewage, Suranadi De Silva, and Shankhadeep Mondal (University of Central Florida), 'Hybrid Neural-Classical Correction for Frozen Time Series Foundation Models: A Comprehensive Ablation Study on High-Frequency Stock Prediction', arXiv:2608.08825v1 [cs.LG], submitted August 9, 2026. Stable URLs: https://arxiv.org/abs/2608.08825, https://arxiv.org/html/2608.08825v1, https://arxiv.org/pdf/2608.08825v1; Code & Data Repository: https://github.com/Kasun-Dewage/Hybrid_Neural2026 (commit fb1541bf408eefdd7708548e8a10a3c7a4cf5ec8, MIT License)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Hybrid Neural-Classical Correction for Frozen Time Series Foundation Models: Bilinear-Gated Adaptation and Random Forest Residual Learning for High-Frequency Opening-Hour Return Prediction

## Provenance

- **Primary Working Paper:** Kasun Dewage, Suranadi De Silva, and Shankhadeep Mondal, *"Hybrid Neural-Classical Correction for Frozen Time Series Foundation Models: A Comprehensive Ablation Study on High-Frequency Stock Prediction"*, arXiv preprint `arXiv:2608.08825v1 [cs.LG]`, submitted August 9, 2026.
  - arXiv Abstract: `https://arxiv.org/abs/2608.08825`
  - Full-Text HTML: `https://arxiv.org/html/2608.08825v1`
  - Full-Text PDF: `https://arxiv.org/pdf/2608.08825v1`
  - Affiliation: Department of Mathematics and Department of Computer Science, University of Central Florida, Orlando, FL.
- **Primary Code & Data Repository:** Open-source implementation and dataset hosted publicly on GitHub:
  - Repository URL: `https://github.com/Kasun-Dewage/Hybrid_Neural2026`
  - Immutable Commit SHA: `fb1541bf408eefdd7708548e8a10a3c7a4cf5ec8`
  - Key Source File: `src/hybrid_neural.py`
  - Dataset Release: `data.csv` (118 MB, 2,011,399 rows across 10 large-cap US technology stocks, December 2024 – January 2026, 1-minute bars)
  - License: MIT License
- **Pretrained Foundation Model:** Google TimesFM (`google/timesfm-1.0-200m`, 200M parameters; Das et al., 2024, ICML), open-sourced at `https://github.com/google-research/timesfm`.
- **Repository Deduplication Audit:** Systematic audit across all strategy research records in `alpha-strategy-research` confirmed zero existing records for `arXiv:2608.08825`, Kasun Dewage, Google TimesFM, or `Hybrid_Neural2026`. Adjacent time-series foundation model records (such as `chronos-foundation-transformer-statistical-arbitrage-factor-residuals-2026-09-12.md` based on Valeyre & Aboura 2025, arXiv:2412.09394v2) investigate an entirely distinct model (Amazon Chronos-T5-tiny 11M parameters), target (daily CRSP cross-sectional factor residuals from 1978 to 2016), horizon (daily rebalancing), and failure mechanism (turnover cost drag under 3 bps friction), whereas the present research addresses intraday high-frequency opening-hour 1-minute multi-step return forecasting, premarket order-flow conditioning, and hybrid bilinear neural-classical residual correction. Complete independent provenance is established.

## Economic mechanism

### Source-reported

1. **Failure of Zero-Shot Time-Series Foundation Models in High-Frequency Finance:**
   General-purpose time-series foundation models (such as Google TimesFM, pretrained on hundreds of billions of non-financial and synthetic time points) fail completely when evaluated zero-shot on high-frequency equity price returns. In the empirical tests reported by Dewage, De Silva, and Mondal, frozen TimesFM produces a mean within-day Pearson return correlation of $\overline{\rho}_{\text{day}} = 0.0586$, a cross-day cumulative return correlation of $\rho_{\text{cross}} = -0.0357$, and a pooled correlation of $\rho_{\text{pool}} = 0.0614$ across 10 major US equities. This performance is statistically indistinguishable from a naive historical mean baseline ($\overline{\rho}_{\text{day}} = 0.0442, \rho_{\text{cross}} = 0.0000, \rho_{\text{pool}} = 0.0610$). Generalist foundation models lack the inductive biases necessary to discern low-signal-to-noise ratio financial microstructure dynamics.

2. **Information Asymmetry and Price Discovery in the Opening Trading Hour:**
   The regular US equity market opening hour (9:30–10:30 AM US/Eastern) exhibits peak intraday volatility, concentrated liquidity shocks, and rapid price discovery as market participants digest overnight information, macroeconomic releases, and earnings announcements. Premarket trading activity (4:30–9:29 AM US/Eastern) contains predictive order-flow and price-pressure signals regarding opening-hour price trajectories. However, extracting this signal requires modeling multi-scale price drift, volume concentration, and intrabar volatility.

3. **Hybrid Neural-Classical Decomposition (The GatedLinear + Random Forest Paradigm):**
   Full fine-tuning of 200M-parameter foundation models is computationally prohibitive and prone to catastrophic overfitting in regime-shifting financial series. The authors propose a frozen-backbone correction framework:
   $$\hat{\mathbf{y}} = \hat{\mathbf{y}}^{(\text{tfm})} + \Delta \mathbf{y}_{\text{neural}}(\mathbf{X}^{(\text{pm})}, \mathbf{m}, \hat{\mathbf{y}}^{(\text{tfm})}) + \Delta \mathbf{y}_{\text{RF}}(f_{\text{summary}})$$
   - A lightweight neural module (`GatedLinear`, $\approx 49\text{K}$ parameters) processes 300 premarket 1-minute bars ($\mathbf{X}^{(\text{pm})} \in \mathbb{R}^{300 \times 7}$) via low-rank bilinear projection $\mathbf{Z} = \mathbf{V}^\top \mathbf{X}^{(\text{pm})} \mathbf{U} \in \mathbb{R}^{8 \times 4}$ (only 2,428 parameters) combined with a learned time-step gating mechanism $\mathbf{g} = \sigma(\mathbf{W}_g \mathbf{h} + \mathbf{b}_g) \in [0, 1]^{60}$.
   - A classical tree ensemble (`RandomForestRegressor`, 250 trees, max depth 12) fits the residual prediction error $\mathbf{y} - (\hat{\mathbf{y}}^{(\text{tfm})} + \Delta \mathbf{y}_{\text{neural}})$ using hand-crafted multiscale summary statistics ($f_{\text{summary}}$).
   - Empirical findings demonstrate that classical residual learning provides the single largest component contribution (+0.158 per-day correlation gain), operating on non-linear tabular interactions and heavy-tailed return distributions where gradient descent on neural embeddings underperforms.

### Research interpretation

- **Microstructure Rationale of Premarket-to-Open Drift:**
  Premarket trading in US equities is characterized by thin order books, wider bid-ask spreads, and participation primarily by institutional desks, algorithms, and informed retail traders. Imbalances formed between 4:30 AM and 9:29 AM create inventory pressure that market makers must absorb at the 9:30 AM opening cross. The opening 60 minutes represent the unwinding and equilibrium re-pricing of this premarket inventory.
- **Complementary Inductive Biases (Trees vs. Transformers vs. Bilinear Projections):**
  Deep sequence models and transformer foundation models excel at learning smooth continuous temporal representations, but struggle with discontinuous threshold effects and extreme outliers common in financial returns. Tree ensembles (Random Forest) partition tabular feature spaces along orthogonal axes, making them robust to non-Gaussian tails and leverage points. By cascading a frozen foundation model $\to$ bilinear-gated neural adapter $\to$ classical residual forest, each model handles the functional scale for which its inductive bias is best suited.
- **The Dimensionality Bottleneck and Information Loss:**
  A key empirical nuance documented by the authors is that compressing $300 \times 7 = 2,100$ premarket features into 32 dimensions via bilinear projection loses localized high-frequency shock details. When Random Forest is excluded, a simpler architecture (`GatedLinear-NoBilinear` using only the last 60 raw premarket bars) outperforms full GatedLinear (0.342 vs. 0.215 correlation). It is only when Random Forest is present to inject tabular summary statistics that the extreme parameter efficiency of the bilinear projection (49K parameters vs. 471K for attention) achieves state-of-the-art accuracy.

## Signal

The signal forecasting pipeline maps premarket data into a 60-step opening-hour return trajectory (`source-reported`):

```text
[Data Window 1: Previous Day Regular Session (9:30-16:00) + Premarket (4:30-9:29)]
                          ↓
[Frozen Foundation Model Inference: TimesFM-1.0-200M]
  - Input: Close price sequence (up to 1,024 1-minute bars)
  - Output: 60-minute raw trajectory forecast y_hat^(tfm) in R^60
                          ↓
[Premarket Feature Extraction: 4:30 to 9:29 AM US/Eastern]
  - Premarket Tensor: X^(pm) in R^(300 x 7) (OHLC normalized by prev_close * vol, log-vol, mom, intrabar vol)
  - Multiscale Summary: m in R^21 (returns, volatility, volume, HL-range over 5, 15, 30, 60, 300m + gap)
                          ↓
[Stage 1: Bilinear-Gated Neural Correction (GatedLinear ~49K params)]
  - Low-rank bilinear projection: Z = V^T * X^(pm) * U in R^(8 x 4) -> flatten to z in R^32 (2,428 params)
  - Concatenation: h_in = [z; m; y_hat^(tfm)] in R^113
  - Encoder MLP: 113 -> 128 -> LayerNorm -> GELU -> Dropout(0.25) -> 128 -> GELU -> h
  - Gated Output: g = sigmoid(W_g * h + b_g) in [0, 1]^60
  - Residual Output: r = W_r * h + b_r in R^60 (W_r, b_r initialized to 0)
  - Neural Correction: Delta_y_neural = g (.) r in R^60
  - Intermediate Composite: y_hat_comb = y_hat^(tfm) + Delta_y_neural
                          ↓
[Stage 2: Classical Tabular Residual Learning (Random Forest)]
  - Features X_rf = [pm_summary(pm); m; y_hat^(tfm); y_hat_comb] in R^(35 + 21 + 60 + 60) = R^176
  - Target: y - y_hat_comb (residual error vector in R^60)
  - Regressor: MultiOutputRegressor(RandomForestRegressor(250 trees, max_depth=12, min_samples_leaf=3))
  - Classical Correction: Delta_y_RF in R^60
                          ↓
[Final Trajectory Prediction]
  - y_hat = y_hat_comb + Delta_y_RF = y_hat^(tfm) + Delta_y_neural + Delta_y_RF in R^60
```

### 1. Mathematical Formulation

#### Premarket Sequence Normalization (`source-reported`)
For each premarket 1-minute bar $\tau \in \{1, \dots, T\}$ ($T = 300$, corresponding to 4:30 AM to 9:29 AM):
- Open, High, Low, Close are normalized by the previous regular session close $C_{\text{prev}}$ and annualized stock volatility $\sigma_i$:
  $$O_{\tau}^{\text{norm}} = \frac{O_\tau - C_{\text{prev}}}{C_{\text{prev}} \cdot \sigma_i}, \quad H_{\tau}^{\text{norm}} = \frac{H_\tau - C_{\text{prev}}}{C_{\text{prev}} \cdot \sigma_i}, \quad L_{\tau}^{\text{norm}} = \frac{L_\tau - C_{\text{prev}}}{C_{\text{prev}} \cdot \sigma_i}, \quad C_{\tau}^{\text{norm}} = \frac{C_\tau - C_{\text{prev}}}{C_{\text{prev}} \cdot \sigma_i}$$
- Volume: $V_\tau^{\text{log}} = \log(1 + V_\tau)$
- Bar momentum: $M_\tau = \frac{C_\tau - C_{\tau-1}}{C_{\tau-1} \cdot \sigma_i}$ (with $M_1 = 0$)
- Intrabar volatility: $S_\tau = \frac{H_\tau - L_\tau}{C_{\text{prev}} \cdot \sigma_i}$
- Resulting tensor: $\mathbf{X}^{(\text{pm})} \in \mathbb{R}^{300 \times 7}$. If fewer than 300 bars exist, the sequence is left-padded with zeros.

#### Multiscale Summary Features $\mathbf{m} \in \mathbb{R}^{21}$ (`source-reported`)
Computed over trailing premarket windows $w \in \{5, 15, 30, 60, T\}$:
1. Window return: $\frac{C_{\text{end}} - C_{\text{start}}}{C_{\text{start}}}$
2. Percentage return standard deviation: $\text{std}(\Delta C / C)$
3. Log cumulative volume: $\log(1 + \sum V)$
4. High-low range: $\frac{\max(H) - \min(L)}{C_{\text{prev}}}$
The 21st feature is the full premarket overnight gap: $\frac{C_{T} - C_{\text{prev}}}{C_{\text{prev}}}$.

#### Low-Rank Bilinear Projection (`source-reported`)
$$\mathbf{Z} = \mathbf{V}^\top \mathbf{X}^{(\text{pm})} \mathbf{U} \in \mathbb{R}^{r_T \times r_F} = \mathbb{R}^{8 \times 4}$$
where $\mathbf{V} \in \mathbb{R}^{300 \times 8}$ projects the temporal dimension (initialized with a linear trend across rows) and $\mathbf{U} \in \mathbb{R}^{7 \times 4}$ projects feature channels. Total projection parameters: $300 \times 8 + 7 \times 4 = 2,428$. The matrix $\mathbf{Z}$ is flattened to $\mathbf{z} \in \mathbb{R}^{32}$.

#### Gated Output & Loss Function (`source-reported`)
Concatenated vector $[\mathbf{z}; \mathbf{m}; \hat{\mathbf{y}}^{(\text{tfm})}] \in \mathbb{R}^{113}$ passes through a 2-layer MLP (hidden dim 128, LayerNorm, GELU, Dropout 0.25). The gating and residual heads compute:
$$\mathbf{g} = \sigma(\mathbf{W}_g \mathbf{h} + \mathbf{b}_g) \in [0, 1]^{60}, \quad \mathbf{r} = \mathbf{W}_r \mathbf{h} + \mathbf{b}_r \in \mathbb{R}^{60}, \quad \Delta \mathbf{y}_{\text{neural}} = \mathbf{g} \odot \mathbf{r}$$
Trained via Directional Loss with $\alpha_{\text{loss}} = 0.7$ and directional penalty weight $\lambda_{\text{dir}} = 1.5$:
$$\mathcal{L}(\hat{\mathbf{y}}, \mathbf{y}) = \alpha_{\text{loss}} \cdot \text{MSE}(\hat{\mathbf{y}}, \mathbf{y}) + (1 - \alpha_{\text{loss}}) \cdot \frac{1}{H} \sum_{t=1}^H \mathbf{1}_{\{\text{sign}(\hat{y}_t) \ne \text{sign}(y_t)\}} \cdot |y_t| \cdot \lambda_{\text{dir}}$$

#### Random Forest Residual Head (`source-reported`)
The target for Random Forest training is the exact residual error: $\mathbf{e}_{\text{train}} = \mathbf{y}_{\text{train}} - \hat{\mathbf{y}}_{\text{comb}}$. Inputs are standardized via `StandardScaler` over 176 features:
- Premarket summary statistics: $p_{-1, :}$, trailing 5-bar mean, 15-bar mean, 30-bar mean, 30-bar std, and short-term momentum ($p_{-1, :} - \text{mean}(p_{-5, :})$) ($6 \times 7 = 42 \to 35$ unique features).
- Multiscale features $\mathbf{m}$ (21 features).
- Raw TimesFM forecast $\hat{\mathbf{y}}^{(\text{tfm})}$ (60 features).
- Intermediate combined forecast $\hat{\mathbf{y}}_{\text{comb}}$ (60 features).
Forest configuration: 250 trees, maximum tree depth 12, minimum samples per leaf 3, `random_state=42`.

### 2. Operational Trading Rule Translation (`research-proposed`)

*The cited primary source formulates and validates multi-step trajectory prediction ($\hat{\mathbf{y}} \in \mathbb{R}^{60}$) but does not define a production execution rule, position sizing, or stop-loss logic. The following trading rule represents a `research-proposed` operational translation:*

- **Signal Timestamp:** Formed at 9:29:55 AM US/Eastern upon receipt of the final premarket bar ($T=300$). Model inference completes within $< 200\text{ ms}$ (`research-proposed`).
- **Predicted Metric:** Cumulative predicted opening-hour return:
  $$\hat{Y}_{\text{cum}} = \sum_{t=1}^{60} \hat{y}_t \quad (\%)$$
- **Long Entry Trigger (`research-proposed`):** At 9:30:00 AM US/Eastern, if $\hat{Y}_{\text{cum}} > +\theta_{\text{long}}$ (with entry threshold $\theta_{\text{long}} = +0.25\%$, `research-proposed`), send market-on-open (MOO) or immediate-or-cancel (IOC) limit order at best ask.
- **Short Entry Trigger (`research-proposed`):** At 9:30:00 AM US/Eastern, if $\hat{Y}_{\text{cum}} < -\theta_{\text{short}}$ (with entry threshold $\theta_{\text{short}} = -0.25\%$, `research-proposed`), send short sell MOO/IOC order at best bid.
- **Neutral / Cash Filter (`research-proposed`):** If $|\hat{Y}_{\text{cum}}| \le 0.25\%$, no position is opened for that trading session.
- **Time-Based Exit (`research-proposed`):** Exactly 60 minutes after market open (10:30:00 AM US/Eastern), execute market-on-close/limit order to flatten the position.
- **Dynamic Trajectory Stop (`research-proposed`):** If realized cumulative loss exceeds $1.5 \times$ the stock's 60-minute historical ATR at any 1-minute bar before 10:30 AM, exit immediately.
- **Position Sizing (`research-proposed`):** Inverse-volatility allocation: $w_i = \frac{1/\sigma_i}{\sum_j 1/\sigma_j}$ with a maximum gross leverage cap of $1.0\times$ portfolio equity.

## Required data

- **Universe:** 10 liquid US equity mega-cap technology stocks: `NVDA`, `MSFT`, `AAPL`, `GOOG`, `GOOGL`, `AMZN`, `META`, `AVGO`, `TSLA`, `NFLX` (`source-reported`).
- **Timeframe:** 1-minute intraday bars (`source-reported`).
  - Premarket session: 4:30 AM – 9:29 AM US/Eastern (300 bars).
  - Target session: 9:30 AM – 10:30 AM US/Eastern (60 bars).
  - Regular trading session: 9:30 AM – 16:00 PM US/Eastern (390 bars).
- **Historical Horizon:** December 2024 to January 2026 (2,011,399 total 1-minute rows, spanning 266 trading days per ticker, 149 days for NFLX) (`source-reported`).
- **Bar Fields Required:** Open, High, Low, Close, Volume, Timestamp (converted to `US/Eastern`) (`source-reported`).
- **Context Sequence:** Trailing regular market close prices from day $d-1$ concatenated with premarket close prices of day $d$ (minimum 100 regular bars and 30 premarket bars required; capped at maximum length of 1,024 bars) (`source-reported`).
- **Point-in-Time Integrity:** Strict chronological splits: 186 train days, 40 validation days, 40 test days (70% train / 15% val / 15% test). Volatility statistics $\sigma_i$ are estimated exclusively on training dates, preventing look-ahead leakage (`source-reported`).

## Execution assumptions

- **Source Execution Modeling:** The primary paper is an econometric and predictive machine learning study; it evaluates trajectory prediction error (MAE, RMSE) and directional correlation metrics. **Transaction fees, bid-ask spread crossing, market impact, borrow fees, and execution slippage are NOT modeled in the primary source** (`source-reported`).
- **Research-Proposed Execution Model:**
  - Order Type: Market-on-Open (MOO) or aggressive limit order with 1-tick tolerance at 9:30:00 AM (`research-proposed`).
  - Commissions: Interactive Brokers Fixed Tier: $0.005 per share or 0.5 bps of trade value (`research-proposed`).
  - Bid-Ask Spread & Slippage: For large-cap US equities (`AAPL`, `NVDA`, `MSFT`), opening spread typically ranges from 1.5 to 3.0 bps. An explicit execution drag of 2.5 bps per one-way leg (5.0 bps round-trip) must be subtracted from realized returns (`research-proposed`).
  - Borrow Availability: Easy-to-borrow status assumed for all 10 liquid mega-cap tech stocks (`research-proposed`).
  - Capacity Limit: Mega-cap tech stocks exhibit daily turnover in billions of dollars; strategy capacity estimated at $10M–$25M portfolio equity before 9:30 AM market impact degrades opening fills (`research-proposed`).

## Evidence

### Source-reported

All performance statistics reported below are directly sourced from the primary paper (Dewage, De Silva, and Mondal 2026, Table II, Table III, Table IV, Table V, Table VI) across the 40-day out-of-sample test period:

#### 1. Aggregate Out-of-Sample Results Across 10 Equities (Table III)

Three distinct correlation metrics are evaluated:
1. **Mean Per-Day Correlation ($\overline{\rho}_{\text{day}}$):** Average within-session Pearson correlation between predicted and actual 60-bar trajectories across test days:
   $$\overline{\rho}_{\text{day}} = \frac{1}{D} \sum_{d=1}^D \text{corr}(\hat{\mathbf{y}}_d, \mathbf{y}_d)$$
2. **Cross-Day Correlation ($\rho_{\text{cross}}$):** Correlation of total 60-minute cumulative returns across test days:
   $$\rho_{\text{cross}} = \text{corr}\left(\sum_{t=1}^{60} \hat{y}_{d,t}, \sum_{t=1}^{60} y_{d,t}\right)$$
3. **Pooled Correlation ($\rho_{\text{pool}}$):** Correlation computed over the flattened $D \times 60$ array:
   $$\rho_{\text{pool}} = \text{corr}(\text{vec}(\hat{\mathbf{Y}}), \text{vec}(\mathbf{Y}))$$

| Model Variant | MAE (%) $\downarrow$ | RMSE (%) $\downarrow$ | Mean Per-Day Corr ($\overline{\rho}_{\text{day}}$) $\uparrow$ | Cross-Day Corr ($\rho_{\text{cross}}$) $\uparrow$ | Pooled Corr ($\rho_{\text{pool}}$) $\uparrow$ |
|:---|:---:|:---:|:---:|:---:|:---:|
| **07_GatedLinear+RF** | **0.1079** | **0.1535** | **0.3730** | 0.5631 | **0.5972** |
| 06_AttnCorrect+RF | 0.1081 | 0.1547 | 0.3678 | **0.5819** | 0.5890 |
| 11_GatedLinear-NoBilinear | 0.1071 | 0.1600 | 0.3422 | 0.5055 | 0.5040 |
| 10_GatedLinear-NoGate | 0.1084 | 0.1666 | 0.2864 | 0.3620 | 0.4317 |
| 02_MLP | 0.1105 | 0.1679 | 0.2407 | 0.4957 | 0.4584 |
| 09_GatedLinear-NoRF | 0.1087 | 0.1710 | 0.2147 | 0.3058 | 0.3219 |
| 08_AttnCorrect-NoRF | 0.1091 | 0.1740 | 0.2335 | 0.3829 | 0.3698 |
| 03_LSTM | 0.1082 | 0.1744 | 0.3519 | 0.4628 | 0.4943 |
| 04_BiLSTM | 0.1090 | 0.1779 | 0.3420 | 0.4653 | 0.4737 |
| 12_AttnCorrect-NoAttn | 0.1109 | 0.1922 | 0.1347 | 0.4179 | 0.1997 |
| 05_TimesFM Base (Frozen) | 0.1113 | 0.1946 | 0.0586 | -0.0357 | 0.0614 |
| 01_HistMean (Baseline) | 0.1115 | 0.1946 | 0.0442 | 0.0000 | 0.0610 |

#### 2. Per-Stock Performance Breakdown (Table IV)

Comparison between Frozen TimesFM Base and the proposed `GatedLinear+RF` hybrid:

| Ticker | Training Volatility $\sigma_i$ | Frozen TFM RMSE (%) | Gated+RF RMSE (%) | Frozen TFM $\overline{\rho}_{\text{day}}$ | Gated+RF $\overline{\rho}_{\text{day}}$ | Frozen TFM $\rho_{\text{pool}}$ | Gated+RF $\rho_{\text{pool}}$ |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **NVDA** | 0.001627 | 0.2466 | 0.1683 (-31.7%) | 0.018 | **0.473** | 0.165 | **0.739** |
| **MSFT** | 0.001000 | 0.1228 | 0.1010 (-17.7%) | 0.099 | **0.424** | 0.075 | **0.624** |
| **AAPL** | 0.001098 | 0.1095 | 0.1068 (-2.5%) | 0.033 | **0.171** | 0.040 | **0.347** |
| **GOOG** | 0.001050 | 0.2140 | 0.1651 (-22.8%) | 0.054 | **0.383** | -0.014 | **0.646** |
| **GOOGL** | 0.001070 | 0.2151 | 0.1616 (-24.9%) | 0.120 | **0.408** | 0.070 | **0.669** |
| **AMZN** | 0.001190 | 0.1463 | 0.1258 (-14.0%) | 0.087 | **0.351** | 0.085 | **0.527** |
| **META** | 0.001298 | 0.1636 | 0.1363 (-16.7%) | 0.083 | **0.399** | 0.158 | **0.659** |
| **AVGO** | 0.001764 | 0.3183 | 0.2320 (-27.1%) | 0.010 | **0.395** | -0.075 | **0.685** |
| **TSLA** | 0.001988 | 0.2541 | 0.1954 (-23.1%) | 0.109 | **0.458** | 0.136 | **0.644** |
| **NFLX** | 0.001150 | 0.1558 | 0.1431 (-8.2%) | -0.027 | **0.268** | -0.025 | **0.434** |

#### 3. Component Ablation Findings (Table V & Table VI)

- **Finding 1 (Random Forest Dominance):** Removing Random Forest from `GatedLinear` drops mean per-day correlation by **-0.1583** (from 0.3730 to 0.2147) and cross-day correlation by **-0.2573** (from 0.5631 to 0.3058). Removing RF from `AttnCorrect` drops per-day correlation by **-0.1343** (from 0.3678 to 0.2335). Classical residual learning provides the single largest performance leap.
- **Finding 2 (Simpler Neural Modules Excel Without RF):** Without RF, `GatedLinear-NoBilinear` (which uses only the last 60 raw premarket bars flattened, 420 dims) achieves 0.3422 per-day correlation, outperforming full `GatedLinear-NoRF` (0.2147 correlation) by +0.128. Bilinear compression loses high-frequency details that require tabular features to recover.
- **Finding 3 (Self-Attention vs. Mean Pooling):** In neural-only adapters, self-attention adds +0.0988 per-day correlation over mean pooling (`AttnCorrect-NoRF` 0.2335 vs. `AttnCorrect-NoAttn` 0.1347).
- **Finding 4 (Parameter Efficiency):** `GatedLinear` requires only **49,000 trainable parameters** ($9.6\times$ fewer than `AttnCorrect`'s 471,000), while achieving superior per-day correlation (0.3730 vs. 0.3678) and pooled correlation (0.5972 vs. 0.5890).

### Independently reproduced

- Not independently reproduced in this research capture. The repository script `src/hybrid_neural.py` and data file `data.csv` are public and structurally verified against the paper's reported values.

### Negative evidence

1. **Complete Inefficacy of Zero-Shot Foundation Models:**
   Frozen TimesFM achieves $\overline{\rho}_{\text{day}} = 0.0586$ and negative cross-day correlation ($\rho_{\text{cross}} = -0.0357$). Without domain adaptation, large-scale generalist time-series foundation models provide no usable alpha signal on intraday equity prices (`source-reported`).
2. **Neural Adaptation Alone Is Subpar:**
   Neural correction without tabular Random Forest (`GatedLinear-NoRF`) produces a per-day correlation of only 0.2147 and cross-day correlation of 0.3058—underperforming a standard LSTM baseline (0.3519 per-day correlation, 0.4628 cross-day correlation) (`source-reported`).
3. **Execution Friction Fragility (`research-proposed`):**
   The mean absolute return per 1-minute bar during the opening hour is approximately $0.10\% - 0.15\%$. If opening hour trading incurs 2.5 to 5.0 bps in round-trip bid-ask crossing and market impact, a significant portion of predicted intraday trajectory profit is vulnerable to execution friction.

## Falsification plan

To falsify the hypothesis that hybrid neural-classical correction extracts genuine, economically viable alpha from premarket order flow, the following tests are defined:

1. **Placebo Shuffled-Premarket Test (`research-defined falsification threshold`):**
   - *Protocol:* Randomly permute the premarket sequence $\mathbf{X}^{(\text{pm})}$ across dates while holding the opening target $\mathbf{y}$ fixed.
   - *Falsification Condition:* If the shuffled-input `GatedLinear+RF` retains $> 30\%$ of its mean per-day correlation (i.e. $\overline{\rho}_{\text{day}} > 0.11$), reject the hypothesis that premarket sequential structure drives the alpha.
2. **Post-Open Latency & Execution Drag Stress (`research-defined falsification threshold`):**
   - *Protocol:* Delay execution from 9:30:00 AM to 9:31:00 AM, 9:32:00 AM, and 9:35:00 AM, and apply synthetic bid-ask spread friction ranging from 1 to 10 bps.
   - *Falsification Condition:* If net simulated PnL becomes negative at an execution delay of $\le 60\text{ seconds}$ or at round-trip transaction costs of $\le 4.0\text{ bps}$, classify the strategy as non-executable paper alpha.
3. **Out-of-Universe Small/Mid-Cap Generalization Test (`research-defined falsification threshold`):**
   - *Protocol:* Evaluate the trained `GatedLinear+RF` pipeline on 50 non-tech Russell 2000 small-cap equities.
   - *Falsification Condition:* If mean per-day correlation drops below 0.10 or cross-day correlation becomes negative across the small-cap panel, conclude that the learned premarket relationship is strictly conditioned on mega-cap tech liquidity regimes.
4. **Isolated Classical Baseline Test (Ablation Control) (`research-defined falsification threshold`):**
   - *Protocol:* Train Random Forest directly on the multiscale summary features $\mathbf{m}$ and premarket summary statistics *without* the frozen TimesFM backbone or bilinear neural module.
   - *Falsification Condition:* If pure Random Forest matches `GatedLinear+RF` within $\pm 0.02$ on per-day correlation ($\overline{\rho}_{\text{day}} \ge 0.353$), the foundation model and neural adapter provide zero incremental economic value.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
  The primary source evaluates exclusively listed US equities during the structured premarket-to-open transition (4:30–10:30 AM US/Eastern). The mechanism is ported to cryptocurrency perpetual markets as an adapted research interpretation.
- **Microstructure Differences:**
  1. *Absence of Fixed Premarket Sessions:* Cryptocurrency centralized and decentralized venues operate 24/7/365 without formal overnight halts or premarket auctions. To adapt the strategy, an artificial "anchor session" must be defined (e.g. 00:00 UTC funding settlement or 08:00 UTC Asian market open) (`research-proposed`).
  2. *Funding Rate and Basis Dispersions:* Perpetual futures prices deviate from spot via funding rate mechanics. A crypto adaptation must incorporate funding rates, open interest changes, and basis as additional input channels alongside OHLCV (`research-proposed`).
  3. *Exchange Fragmentation and Lead-Lag:* US equities trade on consolidated SIP tapes across lit venues. Crypto liquidity is fragmented across Binance, OKX, Bybit, and Hyperliquid. Premarket order flow must be synthesized from multi-venue order books (`research-proposed`).
- **Portability Failure Risk:** High. The primary driver of premarket predictability in US equities is the concentrated overnight news backlog released during the 9:30 AM opening cross. In continuous 24/7 crypto markets, news shocks are priced continuously, likely reducing the predictive power of trailing arbitrary 5-hour lookback windows.

## Limitations

1. **Sample Universe Scope:** Evaluated on only 10 mega-cap US technology stocks over 40 test days. Performance on broader cross-sections or defensive sectors is unproven (`source-reported`).
2. **Absence of Transaction Cost Modeling:** The primary paper reports RMSE, MAE, and correlation metrics; it does not model execution costs, slippage, or market impact (`source-reported`).
3. **Severe Bilinear Information Loss Without RF:** Bilinear projection compresses premarket inputs by $65\times$, discarding high-frequency microstructure dynamics that require tree ensembles to rescue (`source-reported`).
4. **Foundation Model Redundancy Risk:** The frozen TimesFM backbone alone is virtually uninformative ($\rho \approx 0.059$). Further ablation is required to verify whether TimesFM provides any indispensable representation beyond an auto-regressive drift prior (`research-proposed`).
5. **Short Out-of-Sample Window:** 40 test days (approximately 2 calendar months) cannot evaluate stability across bear markets, flash crashes, or prolonged regime transitions (`source-reported`).

## Implementation status

- `not-implemented`.
- No implementation has been completed in `nautilus-quant-system`, PyBroker, or NautilusTrader.
- No backtest, paper trading, testnet, or live trading has been authorized or conducted.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- This record serves as a structured research capture of external empirical findings. Inclusion in this repository does not indicate strategy validity, commercial viability, or authorization for live capital deployment.

## Related Wiki records

- `[[quant/chronos-foundation-transformer-statistical-arbitrage-factor-residuals-2026-09-12]]` — Foundation transformer time-series model (Amazon Chronos-T5) applied to daily factor residuals with turnover-cost fragility.
- `[[quant/statistical-arbitrage-rank-space-cnn-transformer-hybrid-atlas-2026-09-02]]` — Hybrid CNN-Transformer architecture for cross-sectional ranking.
- `[[quant/strata-selective-state-space-intraday-raw-bars-cross-sectional-ranking-2026-09-02]]` — Selective state-space (Mamba) model on raw 5-minute intraday bars with style residualization.
- `[[quant/temporal-kolmogorov-arnold-networks-high-frequency-lob-alpha-decay-2026-09-02]]` — High-frequency intraday microstructure prediction and fast alpha decay.

## Sources

1. **Primary Research Paper:**
   Kasun Dewage, Suranadi De Silva, and Shankhadeep Mondal, *"Hybrid Neural-Classical Correction for Frozen Time Series Foundation Models: A Comprehensive Ablation Study on High-Frequency Stock Prediction"*, arXiv preprint `arXiv:2608.08825v1 [cs.LG]`, August 9, 2026.
   - Abstract: `https://arxiv.org/abs/2608.08825`
   - HTML: `https://arxiv.org/html/2608.08825v1`
   - PDF: `https://arxiv.org/pdf/2608.08825v1`
2. **Primary Code and Data Repository:**
   Kasun Dewage, *"Hybrid_Neural2026"*, GitHub repository:
   - URL: `https://github.com/Kasun-Dewage/Hybrid_Neural2026`
   - Commit SHA: `fb1541bf408eefdd7708548e8a10a3c7a4cf5ec8`
   - File Path: `src/hybrid_neural.py`
   - Dataset: `https://github.com/Kasun-Dewage/Hybrid_Neural2026/releases/latest/download/data.csv`
3. **Pretrained Foundation Model:**
   Abhimanyu Das et al., *"A decoder-only foundation model for time-series forecasting"*, ICML 2024 / arXiv:2310.10688. Google TimesFM repository: `https://github.com/google-research/timesfm`.
