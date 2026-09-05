---
schema: strategy-research-record-v1
title: "Spatio-Temporal Momentum: Joint Time-Series and Cross-Sectional Multi-Task Learning with Shrinkage and Turnover Regularization (Tan, Roberts, & Zohren 2023)"
created: 2026-09-06
updated: 2026-09-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - momentum
  - spatio-temporal
  - multi-task-learning
  - time-series-momentum
  - cross-sectional-momentum
  - shrinkage-regularization
  - turnover-regularization
  - equity-index-futures
  - us-equities
status: research-only
confidence: medium
source_as_of: 2023-02-21
sources:
  - "Wee Ling Tan, Stephen Roberts, and Stefan Zohren. 'Spatio-Temporal Momentum: Jointly Learning Time-Series and Cross-Sectional Strategies'. arXiv preprint arXiv:2302.10175v1 [q-fin.TR, cs.LG], submitted February 20, 2023, revised February 21, 2023. DOI: 10.48550/arXiv.2302.10175. URL: https://arxiv.org/abs/2302.10175."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Spatio-Temporal Momentum: Joint Time-Series and Cross-Sectional Multi-Task Learning with Shrinkage and Turnover Regularization

## Provenance

- **Primary Source Authors:** Wee Ling Tan, Stephen Roberts, and Stefan Zohren (Oxford-Man Institute of Quantitative Finance & Department of Engineering Science, University of Oxford, Oxford, UK).
- **Paper Title:** *"Spatio-Temporal Momentum: Jointly Learning Time-Series and Cross-Sectional Strategies"*
- **Publication Identifier:** arXiv preprint `arXiv:2302.10175v1 [q-fin.TR, cs.LG]`, submitted February 20, 2023, revised February 21, 2023.
- **Canonical DOI:** [10.48550/arXiv.2302.10175](https://doi.org/10.48550/arXiv.2302.10175)
- **Stable URL:** [https://arxiv.org/abs/2302.10175](https://arxiv.org/abs/2302.10175)
- **Primary Source Inspection:** The complete LaTeX source package (`main.tex`, `bibliography.bib`, and figures) from `arXiv:2302.10175v1` was directly unpacked, verified, and audited for all mathematical formulations, loss functions, network architectures, hyperparameter grids, and empirical backtest tables.
- **Repository Deduplication Audit:** A strict full-text audit across `alpha-strategy-research` confirmed zero pre-existing records referencing `arXiv:2302.10175`, "Spatio-Temporal Momentum", or author Wee Ling Tan. Adjacent momentum records in the repository explore time-series momentum with xLSTM/VSN (`cross-asset-futures-vsn-xlstm-sharpe-optimal-portfolio-2026-09-03.md`), macroeconomic regime sieves (`deepm-regime-robust-macro-graph-causal-sieve-evar-2026-09-03.md`), transfer ranking across equities (`crypto-cross-sectional-momentum-fused-encoder-2026-08-31.md`), or analyst coverage networks (`equity-analyst-coverage-network-graph-attention-momentum-spillover-2026-09-02.md`). None formulate a joint spatio-temporal multi-task tensor model unifying cross-asset momentum spillovers with explicit localized turnover regularization and $L_1$ shrinkage.

## Economic mechanism

### Source-reported

Conventional quantitative momentum literature bifurcates into two mutually disjoint paradigms:
1. **Time-Series Momentum (TSMOM):** Constructs trading signals for each asset based strictly on its own historical returns (e.g., sign of past 12-month return in Moskowitz et al. 2012, or MACD filters in Baz et al. 2015). TSMOM constructs signals for individual portfolio assets independently, ignoring concurrent cross-asset feedback, lead-lag spillovers, or the collective market state.
2. **Cross-Sectional Momentum (CSMOM):** Evaluates momentum scores across a universe at time $t$ and takes maximum long positions in the top decile and maximum short positions in the bottom decile (Jegadeesh & Titman 1993). In the initial scoring phase, CSMOM still relies purely on an asset's isolated historical returns. In the allocation phase, heuristic decile binning forces extreme $\pm 1$ allocations while leaving all intermediate assets completely unallocated, failing to capture continuous trend signals.

Tan, Roberts, and Zohren introduce **Spatio-Temporal Momentum (STMOM)** to bridge this divide. The underlying economic hypothesis is that momentum features across peer assets in the cross-section convey vital information about sector-wide lead-lag dynamics, market liquidity states, and risk-premia propagation. By structuring the problem as Multi-Task Learning (MTL) over a shared spatio-temporal tensor $\mathbf{u}_t \in \mathbb{R}^{N^t \times \tau \times d}$, a neural network simultaneously generates continuous trading signals $\mathbf{X}_t \in [-1, 1]^{N^t}$ for all assets in the universe.

Furthermore, empirical SHAP (Shapley Additive exPlanations) analysis reveals that the signal generated for an asset (e.g., Bank of America, BAC) is predominantly driven by cross-sectional peer features (e.g., insurance and brokerage firms' MACD signals such as AJG and JEF) rather than BAC's own isolated history, confirming that cross-sectional momentum spillovers contain significant predictive power.

### Research interpretation

The economic edge of Spatio-Temporal Momentum originates from three interacting mechanisms:
- **Lead-Lag and Information Diffusion in Common Sectors:** In liquid markets, information diffuses unevenly across equities and futures. Industry bellwethers or high-beta index components react to systemic shocks faster than peers. A joint spatio-temporal model extracts these lead-lag dependencies without requiring manual pair or graph specification.
- **Inductive Bias of Multi-Task Learning:** By training a single model to predict $N^t$ asset positions simultaneously under a joint Sharpe loss, the network acts under shared representation regularization. This mitigates individual asset overfitting and aligns weights along common risk factors.
- **Complexity-SNR Trade-Off and Model Parsimony:** Financial returns have notoriously low signal-to-noise ratios (SNR). STMOM architectures exposed to $t$ time samples (as opposed to $t \times N^t$ for single-asset models) suffer severe overfitting when parameterized with high-capacity non-linear networks (CNNs or LSTMs). A simple Single-Layer Perceptron (SLP) equipped with $L_1$ shrinkage behaves as a regularized linear factor model with soft thresholding, extracting sparse, robust cross-asset coefficients that retain positive alpha after high transaction costs.

## Signal

### 1. Mathematical Formulation (`source-reported`)

Let $N^t$ be the number of tradable assets at time $t$, $\tau$ the lookback temporal history window, and $d$ the number of engineered momentum features per asset.
The input is organized as a spatio-temporal tensor $\mathbf{u}_t \in \mathbb{R}^{N^t \times \tau \times d}$, where $\mathbf{u}_t(i, j, k)$ denotes the $k$-th feature of asset $i$ observed at time $t - j$.

The model $f(\mathbf{u}_t; \boldsymbol{\theta})$ simultaneously maps the tensor into a continuous signal vector:
$$\mathbf{X}_t = \begin{bmatrix} X_t^{(1)} \\ X_t^{(2)} \\ \vdots \\ X_t^{(N^t)} \end{bmatrix} \in [-1, 1]^{N^t}$$

The portfolio return at time $t+1$ under volatility-scaled allocation is:
$$r_{t, t+1}^{\text{TSMOM}} = \frac{1}{N^t} \sum_{i=1}^{N^t} X_t^{(i)} \frac{\sigma_{\text{tgt}}}{\sigma_t^{(i)}} r_{t, t+1}^{(i)}$$
where:
- $\sigma_{\text{tgt}} = 0.15$ (15% annualized target volatility) (`source-reported`).
- $\sigma_t^{(i)}$ is the ex-ante volatility of asset $i$, estimated via a 60-day exponentially weighted moving standard deviation of daily returns (`source-reported`).
- $r_{t, t+1}^{(i)}$ is the daily percentage return of asset $i$ from $t$ to $t+1$ (`source-reported`).

### 2. Feature Definitions (`source-reported`)

Each asset $i$ at each historical timestep $t-j$ provides $d = 8$ momentum features:
1. **Volatility-Normalized Returns ($d_1 = 5$):**
   $$F_{1, k}^{(i)}(t) = \frac{r_{t-k, t}^{(i)}}{\sigma_t^{(i)} \sqrt{k}}, \quad k \in \{1, 20, 63, 126, 252\}$$
   capturing daily, monthly, quarterly, semi-annual, and annual normalized momentum.
2. **Volatility-Normalized MACD Signals ($d_2 = 3$):**
   $$\text{MACD}(i, t, S, L) = m(i, t, S) - m(i, t, L)$$
   $$\text{MACD}_{\text{norm}}(i, t, S, L) = \frac{\text{MACD}(i, t, S, L)}{\text{std}(p_{t-63:t}^{(i)})}$$
   $$Y_t^{(i)}(S, L) = \frac{\text{MACD}_{\text{norm}}(i, t, S, L)}{\text{std}\left(\text{MACD}_{\text{norm}}(i, t-252:t, S, L)\right)}$$
   evaluated across three short/long scale pairs $(S_k, L_k) \in \{(8, 24), (16, 48), (32, 96)\}$. Here $m(i, t, j)$ is the exponentially weighted moving average with half-life $HL = \log(0.5) / \log(1 - 1/j)$.

### 3. Model Architectures (`source-reported`)

- **Single-Layer Perceptron (SLP) — Primary Architecture:**
  The input tensor is flattened to $\mathbf{u}_t \in \mathbb{R}^m$, where $m = N^t \cdot \tau \cdot d$. For SLP, temporal history is fixed at $\tau = 5$ (`source-reported`).
  $$\mathbf{X}_t = g(\mathbf{W}^\top \mathbf{u}_t + \mathbf{b})$$
  where $\mathbf{W} \in \mathbb{R}^{m \times N^t}$, $\mathbf{b} \in \mathbb{R}^{N^t}$, and $g = \tanh$.
- **Multilayer Perceptron (MLP):** Two hidden layers with $\tanh$ activations and dropout ($p \in [0.1, 0.5]$). $\tau = 5$.
- **1-D Autoregressive Causal CNN:** Two causal convolutional layers with kernel size downsampling, average pooling $\mathcal{P}$, and an MLP projection head. $\tau = 63$.
- **Long Short-Term Memory (LSTM):** Single-layer LSTM mapping $\mathbf{u}_t \in \mathbb{R}^{\tau \times (N^t \cdot d)}$ across $\tau = 63$ steps into hidden state $\mathbf{h}_t$, followed by a time-distributed dense layer with $\tanh$ activation.

### 4. Loss Formulation, Shrinkage, and Turnover Regularization (`source-reported`)

- **Multi-Task Negative Sharpe Loss:**
  $$\mathcal{L}_{\text{sharpe}}(\boldsymbol{\theta}) = \sum_{i=1}^{N^t} \lambda_i \mathcal{L}_{\text{sharpe}}^{(i)}(\boldsymbol{\theta})$$
  with equal task weights $\lambda_i = \frac{1}{N^t}$.
  $$\mathcal{L}_{\text{sharpe}}^{(i)}(\boldsymbol{\theta}) = - \frac{\sum_{t=1}^T R_i(t) \sqrt{252}}{\sqrt{\sum_{t=1}^T R_i(t)^2 - \left[ \sum_{t=1}^T R_i(t) \right]^2}}$$
  where $R_i(t) = X_t^{(i)} \frac{\sigma_{\text{tgt}}}{\sigma_t^{(i)}} r_{t, t+1}^{(i)}$.
- **$L_1$ Shrinkage Penalty (SLP):**
  Given the high dimensionality of $\mathbf{W} \in \mathbb{R}^{(N^t \cdot \tau \cdot d) \times N^t}$, an $L_1$ regularization penalty induces feature sparsity:
  $$\mathcal{L}(\boldsymbol{\theta}) = \mathcal{L}_{\text{sharpe}}(\boldsymbol{\theta}) + \alpha \sum_{w \in \mathbf{W}} |w|$$
  where $\alpha \in [10^{-5}, 1.0]$ (`source-reported`, Table 4).
- **Localized Minibatch Turnover Regularization (`source-reported`):**
  Daily turnover for asset $i$ is defined as:
  $$\text{TO}_t^{(i)} = \sigma_{\text{tgt}} \left| \frac{X_t^{(i)}}{\sigma_t^{(i)}} - \frac{X_{t-1}^{(i)}}{\sigma_{t-1}^{(i)}} \right|$$
  For non-recurrent models (SLP) trained on shuffled minibatches where consecutive samples $t, t^*$ are non-sequential, localized minibatch turnover is regularized via:
  $$\widetilde{\text{TO}}_t^{(i)} = \sigma_{\text{tgt}} \left| \frac{X_t^{(i)}}{\sigma_t^{(i)}} - \frac{X_{t^*}^{(i)}}{\sigma_{t^*}^{(i)}} \right|$$
  The objective optimizes net-of-cost returns $\tilde{r}_{t, t+1}^{\text{TSMOM}} = \frac{1}{N^t} \sum_{i=1}^{N^t} \left( X_t^{(i)} \frac{\sigma_{\text{tgt}}}{\sigma_t^{(i)}} r_{t, t+1}^{(i)} - c \cdot \widetilde{\text{TO}}_t^{(i)} \right)$ under cost parameter $c$.

## Required data

- **Asset Universes (`source-reported`):**
  1. **US Equities Universe:** 46 common stocks from the Financials sector listed on NYSE, AMEX, and NASDAQ, spanning market capitalizations from Small ($300M–$2B) to Mega (>$200B) sourced from CRSP and screened via Nasdaq Stock Screener. Exact tickers: `AFG`, `AFL`, `AJG`, `BAC`, `C`, `CADE`, `CBSH`, `CFR`, `CHCO`, `CPF`, `CVBF`, `FITB`, `GL`, `IBCP`, `INDB`, `JEF`, `JPM`, `KEY`, `MCO`, `MCY`, `MKL`, `NTRS`, `NWLI`, `PNC`, `SBCF`, `SCHW`, `SEIC`, `SIGI`, `SIVB`, `SNV`, `SRCE`, `STT`, `TFC`, `TMP`, `TRC`, `TROW`, `TRST`, `UBSI`, `UFCS`, `USB`, `VALU`, `VLY`, `WABC`, `WFC`, `WRB`, `ZION`.
  2. **Equity Index Futures Universe:** 12 ratio-adjusted continuous equity index futures contracts sourced from the Pinnacle Data Corp CLC Database: `SP` (S&P 500), `YM` (Mini Dow), `EN` (Nasdaq Mini), `ER` (Russell 2000 Mini), `MD` (S&P 400 Mini), `XU` (Euro Stoxx 50), `XX` (Stoxx 50), `CA` (CAC 40), `LX` (FTSE 100), `AX` (DAX), `HS` (Hang Seng), `NK` (Nikkei 225).
- **Timeframe & Fields:** Daily closing prices and returns (`source-reported`).
- **Data Quality & Preprocessing (`source-reported`):**
  - Missing data threshold: Assets must have less than 10% missing data over the study period.
  - Winsorization: Outliers bounded within 5 times their 252-day exponentially weighted moving standard deviation from their exponentially weighted moving average.
- **Lookback Windows (`source-reported`):**
  - Daily volatility estimation: 60-day exponentially weighted moving standard deviation.
  - Price standard deviation for MACD normalization: 63-day rolling window.
  - MACD historical standard deviation: 252-day rolling window.
  - Temporal tensor depth: $\tau = 5$ days for SLP/MLP; $\tau = 63$ days for CNN/LSTM.
- **Point-in-Time Data Integrity (`research-proposed`):** In live execution, continuous futures roll adjustments must follow open-interest roll schedules, and corporate action splits/dividends in equities must use point-in-time adjusted closing prices to avoid look-ahead bias.

## Execution assumptions

- **Execution Timing (`source-reported`):** Daily rebalancing cadence. Signals generated at close $t$ are allocated for holding over interval $t \to t+1$.
- **Order Types & Execution Model (`research-proposed`):** Source assumes cost-adjusted execution at daily closing prices. In live implementation, execution should occur via market-on-close (MOC) or TWAP orders over the closing auction window to minimize market impact.
- **Transaction Cost Modeling (`source-reported`):** Strategy evaluated across 8 explicit transaction cost tiers: $c \in \{0.0, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 10.0\}$ basis points per dollar of turnover.
- **Leverage and Portfolio Scaling (`source-reported`):** Position sizing scales inversely with asset volatility ($\sigma_{\text{tgt}} / \sigma_t^{(i)}$) targeting a fixed 15% annualized portfolio volatility ($\sigma_{\text{tgt}} = 0.15$). An additional portfolio-level volatility scaling layer adjusts aggregate exposure.
- **Shorting & Borrow Assumptions (`source-reported`):** Equity index futures are inherently symmetric for long/short positions. For US equities, long and short positions are assumed fully symmetrical with unbounded short availability (`source-reported`). Stock borrow fees and short availability constraints are omitted in the source (`research-proposed provenance gap`).

## Evidence

### Source-reported

All quantitative figures below are transcribed directly from Tan, Roberts, & Zohren (arXiv:2302.10175v1, Section 5, Tables 1–4):

#### 1. Out-of-Sample Performance on US Equities (1995–2022, 46 Assets)
Evaluated via expanding walk-forward windows (5-year retraining increments, 90/10 train/val split, 100 random search trials, multiple random seeds; mean across seeds, standard deviation in parentheses):

*Raw Signal Outputs (Table 1):*
- **Long Only:** Return = 6.8%, Vol = 10.2%, Sharpe = 0.667, MDD = 23.5%, Hit Rate = 54.1%, Ave P/L = 0.951.
- **TSMOM (Moskowitz):** Return = 1.2%, Vol = 6.7%, Sharpe = 0.177, MDD = 28.7%, Hit Rate = 52.6%, Ave P/L = 0.932.
- **MACD (Baz et al.):** Return = 0.1%, Vol = 4.5%, Sharpe = 0.021, MDD = 23.7%, Hit Rate = 51.9%, Ave P/L = 0.931.
- **CSMOM (Jegadeesh-Titman):** Return = -3.3%, Vol = 4.8%, Sharpe = -0.702, MDD = 63.1%, Hit Rate = 49.4%, Ave P/L = 0.911.
- **Reference DMN (LSTM):** Return = 5.6% (±0.8%), Vol = 2.8% (±0.8%), Sharpe = **2.043** (±0.263), MDD = **6.7%** (±2.9%), Hit Rate = **59.8%** (±0.5%), Ave P/L = **1.055** (±0.054).
- **STMOM SLP (Ours):** Return = 3.2% (±0.6%), Vol = 2.9% (±0.5%), Sharpe = 1.114 (±0.182), MDD = 7.5% (±1.5%), Hit Rate = 58.1% (±0.7%), Ave P/L = 0.955 (±0.041).
- **STMOM MLP:** Return = 1.3% (±0.5%), Vol = 4.4% (±0.8%), Sharpe = 0.296 (±0.106), MDD = 17.6% (±4.4%), Hit Rate = 54.4%, Ave P/L = 0.902.
- **STMOM CNN:** Return = 1.0% (±0.6%), Vol = 5.1% (±0.6%), Sharpe = 0.195 (±0.106), MDD = 16.7% (±3.7%), Hit Rate = 51.6%, Ave P/L = 0.980.
- **STMOM LSTM:** Return = 1.4% (±0.4%), Vol = 4.4% (±0.8%), Sharpe = 0.320 (±0.108), MDD = 15.9% (±5.3%), Hit Rate = 54.6%, Ave P/L = 0.903.

*Rescaled to 15% Annualized Volatility Target (Table 1):*
- **Long Only:** Return = 13.1%, Vol = 15.5%, Sharpe = 0.841, MDD = 34.4%, Hit Rate = 54.1%.
- **TSMOM:** Return = 5.6%, Vol = 15.7%, Sharpe = 0.358, MDD = 47.0%, Hit Rate = 52.6%.
- **CSMOM:** Return = -10.1%, Vol = 15.4%, Sharpe = -0.655, MDD = 96.4%, Hit Rate = 49.4%.
- **Reference DMN:** Return = **48.7%** (±1.9%), Vol = 16.7% (±0.1%), Sharpe = **2.920** (±0.119), MDD = **26.0%** (±2.9%), Hit Rate = **59.8%**, Sortino = 4.647, Calmar = 1.887.
- **STMOM SLP:** Return = 42.3% (±4.8%), Vol = 16.2% (±0.1%), Sharpe = **2.609** (±0.282), MDD = 30.1% (±3.3%), Hit Rate = 58.1%, Sortino = 4.161, Calmar = 1.428.

#### 2. Out-of-Sample Performance on Equity Index Futures (2003–2020, 12 Contracts)
*Rescaled to 15% Annualized Volatility Target (Table 2):*
- **Long Only:** Return = 7.3%, Vol = 16.3%, Sharpe = 0.450, MDD = 35.5%, Hit Rate = 54.9%.
- **TSMOM:** Return = 3.3%, Vol = 15.9%, Sharpe = 0.209, MDD = 38.0%, Hit Rate = 52.3%.
- **CSMOM:** Return = -9.8%, Vol = 15.4%, Sharpe = -0.638, MDD = 87.1%, Hit Rate = 48.9%.
- **Reference DMN:** Return = 5.5% (±2.6%), Vol = 16.2% (±0.6%), Sharpe = 0.340 (±0.165), MDD = 39.1% (±8.6%), Hit Rate = 52.5%.
- **STMOM SLP (Ours):** Return = **33.3%** (±8.4%), Vol = 16.1% (±0.3%), Sharpe = **2.066** (±0.498), MDD = **24.4%** (±7.6%), Hit Rate = **57.4%** (±1.8%), Sortino = **3.228**, Calmar = **1.619**. (Outperforms DMN by 6.07x on futures).
- **STMOM MLP:** Return = 28.8% (±5.8%), Vol = 16.2%, Sharpe = 1.776 (±0.333), MDD = 23.8% (±5.9%).
- **STMOM LSTM:** Return = 25.1% (±8.5%), Vol = 19.5%, Sharpe = 1.389 (±0.384), MDD = 29.8% (±6.3%).
- **STMOM CNN:** Return = 3.0% (±4.6%), Vol = 16.4%, Sharpe = 0.174 (±0.279), MDD = 44.3% (±12.1%).

#### 3. Impact of Transaction Costs on Net Sharpe Ratio (US Equities, Table 3)
| Strategy | 0.0 bps | 0.5 bps | 1.0 bps | 2.0 bps | 3.0 bps | 4.0 bps | 5.0 bps | 10.0 bps |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Long Only** | 0.841 | 0.839 | 0.838 | 0.835 | 0.832 | 0.829 | 0.826 | 0.812 |
| **TSMOM** | 0.358 | 0.347 | 0.336 | 0.315 | 0.293 | 0.271 | 0.249 | 0.140 |
| **CSMOM** | -0.655 | -0.683 | -0.710 | -0.765 | -0.820 | -0.875 | -0.930 | -1.204 |
| **DMN (Unreg)** | **2.920** | **2.844** | **2.768** | **2.615** | **2.462** | **2.308** | **2.153** | 1.375 |
| **DMN + Reg** | 2.073 | 2.044 | 2.015 | 1.957 | 1.899 | 1.840 | 1.782 | **1.486** |
| **SLP (Unreg)** | 2.609 | 2.518 | 2.427 | 2.243 | 2.060 | 1.876 | 1.691 | 0.762 |
| **SLP + Reg (Ours)** | 2.672 | 2.603 | 2.534 | 2.395 | 2.256 | 2.116 | **1.976** | **1.271** |

Turnover regularization consistently boosts SLP performance across all cost tiers ($c \ge 0$), improving 10 bps Sharpe from 0.762 to 1.271 (+66.8%).

#### 4. Strategy Combinations and Diversification (US Equities, Table 3)
- **TSMOM + CSMOM:** Sharpe = 0.177, Return = 2.8%, MDD = 57.7%.
- **DMN + CSMOM:** Sharpe = 2.115 (±0.153), Return = 34.0%, MDD = 30.7%.
- **Standalone SLP:** Sharpe = 2.609 (±0.282), Return = 42.3%, MDD = 30.1%.
- **DMN + SLP (Joint Portfolio):** Sharpe = **3.304** (±0.151), Return = **55.1%** (±2.7%), MDD = **23.0%** (±1.3%), Hit Rate = **60.3%**, Ave P/L = **1.229**.

### Independently reproduced

`Not independently reproduced.` Findings are transcribed directly from Tan, Roberts, & Zohren (arXiv:2302.10175v1).

### Negative evidence

1. **Failure of Complex Architectures:** High-capacity deep models (MLP, LSTM, and especially CNN) severely underperformed the simple Single-Layer Perceptron across both equities and futures. On Equity Index Futures, CNN delivered negative raw returns (-1.6%, Sharpe -0.215) and rescaled Sharpe of 0.174 vs SLP's 2.066. The authors demonstrate that financial returns have low SNR and that STMOM models are trained on $t$ temporal instances rather than $t \times N^t$ individual samples, leading complex networks to rapidly overfit in-sample noise.
2. **Failure of Cross-Sectional Decile Momentum (CSMOM):** Classical CSMOM was catastrophic across both test periods: Sharpe of -0.702 (MDD 63.1%) in US equities and -0.584 (MDD 55.4%) in futures. Bounding positions to $\pm 1$ on top/bottom deciles while zeroing intermediate assets generated massive drag and negative alpha.
3. **Transaction Cost Degradation without Regularization:** Without turnover regularization, SLP Sharpe plummeted from 2.609 at 0 bps to 0.762 at 10 bps (-70.8%). The localized minibatch turnover penalty was mandatory to preserve edge at institutional fee levels.

## Falsification plan

To falsify the hypothesis that Spatio-Temporal Multi-Task Learning captures genuine cross-asset momentum spillovers beyond isolated time-series momentum:

1. **Cross-Asset Permutation / Placebo Test (`research-proposed`):**
   - *Protocol:* Randomly shuffle the asset feature columns across tickers in $\mathbf{u}_t$ at each timestep while preserving each asset's own historical returns and MACD time series.
   - *Decision Rule (`research-defined falsification threshold`):* If the permuted model's out-of-sample Sharpe ratio is within 10% of the true unpermuted SLP model ($\Delta \text{Sharpe} < 0.10 \times \text{Sharpe}_{\text{true}}$), the hypothesis that cross-asset spatial interaction drives the alpha is falsified.
2. **Sector / Industry Spillover Ablation (`research-proposed`):**
   - *Protocol:* Replace Financials constituents with a cross-industry random sample of equities with low pairwise correlations.
   - *Decision Rule (`research-defined falsification threshold`):* If STMOM fails to outperform standalone DMN on cross-industry panels where lead-lag correlation is negligible, the hypothesis is restricted to intra-sector co-movements rather than universal market momentum.
3. **Subperiod and Regime Stability Breakdown (`research-proposed`):**
   - *Protocol:* Partition out-of-sample periods into high-volatility crash regimes (e.g., 2008 GFC, 2020 Covid crash, 2022 rate hike drawdown) vs low-volatility secular bull markets.
   - *Decision Rule (`research-defined falsification threshold`):* If the strategy suffers an annualized maximum drawdown exceeding 35% at 15% target volatility, or if net Sharpe drops below 0.0 over any rolling 3-year window, reject the model for production allocation.
4. **Transaction Cost and Slippage Stress Test (`research-proposed`):**
   - *Protocol:* Sweep transaction costs beyond 10 bps up to 20 bps with asymmetric maker/taker fees and slippage models.
   - *Decision Rule (`research-defined falsification threshold`):* If regularized SLP Sharpe falls below 0.50 at $c = 12$ bps, the strategy cannot be deployed outside ultra-liquid futures venues.

## Crypto portability

- **Portability Classification:** `adapted` and `unproven`.
- **Primary Source Demonstration:** The primary source investigates only traditional US equities (CRSP) and equity index futures (Pinnacle). The mechanism is entirely unproven in crypto perpetuals or spot markets (`research interpretation`).
- **Cryptocurrency Structural Dynamics:**
  - *Lead-Lag Momentum Spillovers:* In crypto markets, Bitcoin (BTC) and Ethereum (ETH) act as macroeconomic market leaders, while mid-cap and small-cap altcoins exhibit pronounced delayed beta responses. A spatio-temporal tensor architecture could theoretically capture cross-token momentum spillovers from majors to alts more effectively than isolated single-token TSMOM.
  - *24/7 Continuous Trading & Timestamp Boundaries:* Unlike traditional equity sessions with discrete overnight gaps and closing auctions, crypto markets operate 24/7. Daily bar boundaries (00:00 UTC) must be strictly standardized across all exchange feeds (e.g., Binance, OKX, Bybit).
  - *Perpetual Funding Rate Drag:* Holding long/short positions in crypto perpetual futures incurs 8-hour funding rates. Strongly trending altcoins often command extreme annualized funding costs (up to 50–100%), which would rapidly consume momentum alpha if positions are held against funding.
  - *Liquidity Fragmentation and Slippage:* Altcoin perpetuals suffer from thin order-book depth and sudden liquidity vacuums during Bitcoin-led liquidation cascades. The 10 bps cost ceiling established in the paper may be insufficient for mid-cap crypto assets where effective round-trip slippage frequently exceeds 15–25 bps.

## Limitations

- **No Public Codebase Provided (`underspecified`):** While the paper provides detailed mathematical definitions, hyperparameter grids, and layer equations in Appendix A, no official GitHub repository was published alongside the paper. Exact random seeds and implementation scripts must be reconstructed independently.
- **Survivorship Bias in Equities Sample (`data gap`):** The 46 US equities were selected by screening active domestic US companies via Nasdaq Stock Screener as of the study's writing, introducing survivorship bias over the 1990–2022 historical window. The equity index futures backtest (2003–2020) is free from this specific survivorship flaw.
- **Unbounded Shorting Assumption (`execution assumption gap`):** Symmetrical long/short equity execution assumes zero borrow cost and infinite short rebate liquidity, which does not hold for smaller-cap financials during banking crisis periods (e.g., SVB Financial Group, `SIVB`, which is an explicit ticker in the author's universe and collapsed in March 2023).
- **Fixed Static Universe Dimension ($N^t$):** The linear SLP model requires a fixed input vector size $m = N^t \cdot \tau \cdot d$. It cannot handle dynamic universes where tokens or stocks are added or delisted without retraining or zero-padding.
- **Not Independently Reproduced:** All performance statistics are third-party source-reported figures.

## Implementation status

- **Frontmatter Status:** `not-implemented`.
- **Repository Implementation:** No code has been implemented in PyBroker, NautilusTrader, or any internal backtesting engine.
- **Research Scope:** This artifact represents an upstream academic research capture. It does not modify NautilusTrader, create a production strategy family, or authorize Paper, Testnet, or Live execution.

## Adoption boundary

- **Adoption Status:** `not-approved`.
- **Approval Scope:** `research-only`.
- **Boundary Conditions:**
  - Presence in this repository indicates that the research capture has been normalized to canonical Wiki Brain specification; it does not indicate profitable alpha, validated execution edge, or trading readiness.
  - Any future transition to PyBroker exploratory backtesting or NautilusTrader formal verification requires explicit independent review, point-in-time survivorship-bias remediation, and rigorous transaction cost modeling.

## Related Wiki records

- `[[cross-asset-futures-vsn-xlstm-sharpe-optimal-portfolio-2026-09-03]]` — Explores xLSTM and Variable Selection Networks for cross-asset futures time-series momentum under Sharpe loss optimization.
- `[[deepm-regime-robust-macro-graph-causal-sieve-evar-2026-09-03]]` — Investigates deep learning for systematic macro portfolio management with causal sieves and EVaR risk bounds.
- `[[crypto-cross-sectional-momentum-fused-encoder-2026-08-31]]` — Analyzes cross-sectional momentum ranking using neural network encoders across cryptocurrency assets.
- `[[equity-analyst-coverage-network-graph-attention-momentum-spillover-2026-09-02]]` — Examines momentum spillovers across corporate knowledge graphs and financial analyst networks.

## Sources

1. **Primary Academic Source:**
   - Wee Ling Tan, Stephen Roberts, and Stefan Zohren. *"Spatio-Temporal Momentum: Jointly Learning Time-Series and Cross-Sectional Strategies"*. arXiv preprint `arXiv:2302.10175v1 [q-fin.TR, cs.LG]`, submitted February 20, 2023, revised February 21, 2023. DOI: [10.48550/arXiv.2302.10175](https://doi.org/10.48550/arXiv.2302.10175). Stable URL: [https://arxiv.org/abs/2302.10175](https://arxiv.org/abs/2302.10175). Full text PDF: [https://arxiv.org/pdf/2302.10175v1.pdf](https://arxiv.org/pdf/2302.10175v1.pdf).
2. **Underlying Methodological & Benchmark Literature:**
   - Moskowitz, T. J., Ooi, Y. H., and Pedersen, L. H. (2012). *"Time series momentum"*. *Journal of Financial Economics*, 104(2):228–250.
   - Jegadeesh, N. and Titman, S. (1993). *"Returns to buying winners and selling losers: Implications for stock market efficiency"*. *The Journal of Finance*, 48(1):65–91.
   - Baz, J., Granger, N., Harvey, C. R., Le Roux, N., and Rattray, S. (2015). *"Dissecting investment strategies in the cross section and time series"*. Man AHL Research.
   - Lim, B., Zohren, S., and Roberts, S. (2019). *"Enhancing time-series momentum strategies using deep neural networks"*. *The Journal of Financial Data Science*, 1(4):19–38.
   - Baltas, N. and Kosowski, R. (2020). *"Demystifying time-series momentum strategies: Volatility estimators, trading rules and pairwise correlations"*. *Market Momentum: Theory and Practice*, pages 23–49. Wiley.
   - Caruana, R. (1997). *"Multitask learning"*. *Machine Learning*, 28(1):41–75.
   - Lundberg, S. M. and Lee, S.-I. (2017). *"A unified approach to interpreting model predictions"*. *Advances in Neural Information Processing Systems (NeurIPS 2017)*, 30.
