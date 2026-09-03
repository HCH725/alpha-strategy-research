---
schema: strategy-research-record-v1
title: "End-to-End Deep Portfolio Optimization with AttentionLSTM and Differentiable Omega-CVaR-Risk-Parity Loss"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - deep-learning
  - lstm
  - attention
  - omega-ratio
  - cvar
  - risk-parity
  - end-to-end
status: research-only
confidence: high
source_as_of: 2026-05-29
sources:
  - "https://doi.org/10.48550/arXiv.2605.28853"
  - "https://arxiv.org/abs/2605.28853"
  - "https://arxiv.org/html/2605.28853v1"
  - "https://github.com/rahulkfernandes/Financially-Guided-Deep-Portfolio-Optimization/tree/ed35155d6fce3bd03232e946994c46de0a57aa5e"
  - "https://github.com/rahulkfernandes/Financially-Guided-Deep-Portfolio-Optimization/releases/tag/v1.0-paper"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# End-to-End Deep Portfolio Optimization with AttentionLSTM and Differentiable Omega-CVaR-Risk-Parity Loss

## Provenance

- **Primary Source:** Rahul Fernandes and Travis Desell (Rochester Institute of Technology), *"Financially Guided Deep Portfolio Optimization"*, arXiv:2605.28853v1 `[q-fin.PM, cs.LG]`, submitted May 2026.
- **Canonical Digital Object Identifier (DOI):** [10.48550/arXiv.2605.28853](https://doi.org/10.48550/arXiv.2605.28853).
- **Full Text Canonical URLs:** [https://arxiv.org/abs/2605.28853](https://arxiv.org/abs/2605.28853) (HTML full text: [https://arxiv.org/html/2605.28853v1](https://arxiv.org/html/2605.28853v1)).
- **Primary Implementation Repository:** Public GitHub repository `https://github.com/rahulkfernandes/Financially-Guided-Deep-Portfolio-Optimization.git`.
  - Immutable Commit SHA: `ed35155d6fce3bd03232e946994c46de0a57aa5e` (HEAD / main branch).
  - Formal Paper Release Tag: `v1.0-paper` (dereferenced commit SHA `f45b48ccefcad549d5d80443d393a7765c5534f1`).
- **Key Audited Implementation Files:**
  - Loss definitions & differentiable surrogates: `src/training/loss_functions.py` (`custom_loss_10`, `custom_loss_11`, `smooth_omega_objective`, `smooth_rockafellar_cvar_regularizer`, `risk_parity_regularizer`, `shrinkage_covariance_torch`).
  - Model architecture: `src/models/lstm.py` (`AttentionLSTM`, combining 4-layer LSTM, layer normalization, multi-head temporal attention `TemporalAttention`, mean pooling, and softmax output).
  - Data preprocessing: `src/data_processing/preprocess_crsp.py` (`clean_inplace`, `_handle_missing_data`, and fixed training-set `RobustScaler`).
  - Evaluation & transaction cost accounting: `src/evaluation/evaluator.py` (`Evaluator._calc_step_ba_costs`).
  - Hyperparameter search & tuning configuration: `config/hparams.json` and `src/training/train_nn.py`.
  - Statistical analysis & test verification: `exploration/test_analysis.ipynb` (contains seed-wise empirical results, paired t-tests, Shapiro-Wilk normality tests, and Bonferroni-corrected p-values).
- **Universe and Historical Sample:** 50 constituent stocks of the S&P 500 index drawn from the Center for Research in Security Prices (CRSP) over a 16-year timeline from December 7, 2007 to November 29, 2023 (4,021 trading days).
- **Chronological Data Partitioning:**
  - Initial Training Period: December 7, 2007 to February 6, 2020.
  - Expanding Validation Period: February 7, 2020 to December 31, 2021 ($K=8$ quarterly expanding walk-forward steps).
  - Out-of-Sample Test Period: January 3, 2022 to November 29, 2023 ($K=8$ quarterly expanding walk-forward steps, 480 trading days covering the 2022–2023 US equity inflation/bear-market cycle).

## Economic mechanism

### Source-reported

Conventional quantitative asset allocation predominantly relies on a two-stage "predict-then-optimize" pipeline:
1. An empirical model (e.g., ARIMA, Random Forest, GARCH, LSTM, or Transformer) is trained to forecast expected asset returns $\hat{R}_{t+1}$ and/or the second-moment asset covariance matrix $\hat{\Sigma}_{t+1}$.
2. A downstream mathematical optimizer (such as Markowitz Mean-Variance Optimization, Quadratic Programming, or Black-Litterman) computes portfolio weights $\mathbf{w}$ to maximize the expected risk-adjusted return.

Fernandes and Desell (2026) demonstrate that this two-stage pipeline suffers from fundamental structural failure in non-stationary, heavy-tailed financial markets:
- **Error Maximization in Matrix Inversion:** Small estimation errors in the expected return vector $\hat{R}$ and noise in high-dimensional empirical covariance matrices $\hat{\Sigma}$ are dramatically compounded during quadratic optimization, driving mean-variance optimizers toward extreme, highly concentrated corner allocations that collapse out of sample ("error maximizers", Michaud 1989).
- **Static Clustering Heuristics:** Advanced clustering-based methods such as Hierarchical Risk Parity (HRP, Lopez de Prado 2016) and Nested Clustered Optimization (NCO, Lopez de Prado 2019) alleviate covariance matrix inversion instability, but they remain heuristic, assume quasi-stationary cluster trees, and fail to capture nonlinear temporal dynamics across shifting macroeconomic regimes.
- **Under-Diversification in Pure Sharpe Surrogates:** Prior end-to-end neural network approaches that maximize differentiable Sharpe ratio surrogates tend to overfit to sample volatility regimes, learning narrow, concentrated asset bets that fail when tail volatility spikes.

To overcome these structural limitations, the authors introduce **Financially Guided Deep Portfolio Optimization**: an integrated end-to-end framework where a neural network directly maps historical price, liquidity, and volume features into normalized portfolio allocation weights $\mathbf{w}_t \in \Delta^{N-1}$. The network is trained via backpropagation on a three-term composite loss function:
1. **Primary Return Objective (Smooth Omega Ratio):** Evaluates the entire return distribution rather than assuming Gaussian normality, rewarding positive return skewness while penalizing downside losses relative to a target threshold $\theta=0$.
2. **Tail-Risk Regularizer (Rockafellar-Uryasev CVaR):** Directly penalizes expected shortfall in the worst 5% tail distribution ($\alpha=0.05$), bounding drawdown risk without compromising average gains.
3. **Structural Diversification Regularizer (Risk Parity with Linear Shrinkage):** Penalizes imbalances in marginal risk contributions across assets, enforcing structural diversification and preventing concentration collapse.

### Research interpretation

The falsifiable alpha hypothesis is that **parameterizing the portfolio allocation policy directly as an attention-augmented recurrent neural network $\mathbf{w}_t = f_\theta(\mathbf{X}_t)$ and training it end-to-end under a composite objective that simultaneously maximizes whole-distribution gain-to-loss asymmetry (Smooth Omega) while penalizing downside tail risk ($\text{CVaR}_{0.05}$) and marginal risk disparity (Risk Parity) eliminates the error-amplifying intermediate forecast step of MVO and the static rigidity of heuristic clustering, delivering positive risk-adjusted returns during severe macro market contractions without expanding downside tail risk.**

The economic inductive bias operates across three complementary channels:
- *Non-Linear Temporal Feature Synthesis:* The `AttentionLSTM` architecture employs an LSTM backbone to filter high-frequency microstructure noise, followed by multi-head temporal self-attention that selectively weights historical stress intervals (such as volatility spikes or liquidity squeezes) over the 180-day lookback window.
- *Gain/Loss Asymmetry Alignment:* Because financial asset returns exhibit negative skewness and excess kurtosis, quadratic variance penalties (as used in MVO and Sharpe optimization) over-penalize large upside gains and under-penalize fat-tailed downside shocks. The smooth Omega ratio aligns network gradients directly with investor utility by maximizing the ratio of expected gains to expected losses.
- *Structural Anti-Concentration Guardrail:* By computing marginal risk contributions against a Ledoit-Wolf-style linear shrinkage covariance matrix and penalizing squared deviations from equal risk contribution, the structural regularizer prevents the neural network from over-allocating to idiosyncratic momentum winners.

## Signal

### Feature Space Representation ($\mathbf{X}_t \in \mathbb{R}^{T_{\text{in}} \times F}$)

The model ingests a 180-day lookback window ($T_{\text{in}} = 180$ trading days) across $N = 50$ S&P 500 constituent stocks and 1 market benchmark, yielding $F = 251$ total features ($50 \times 5 + 1 = 251$):
1. **Asset Daily Returns (50 features):** $r_{i,t} = (P_{i,t} - P_{i,t-1}) / P_{i,t-1}$ (`TICK_RET`).
2. **Amihud Illiquidity Proxy (50 features):** Daily ratio of absolute return to dollar trading volume (`TICK_ILLIQUIDITY`).
3. **Daily Volume Change (50 features):** Percentage change in daily trading volume (`TICK_VOL_CHANGE`).
4. **Share Turnover (50 features):** Daily trading volume divided by total shares outstanding (`TICK_TURNOVER`).
5. **Bid-Ask Spread (50 features):** Daily quoted spread $(P_{\text{ask}} - P_{\text{bid}}) / P_{\text{mid}}$ (`TICK_BA_SPREAD`).
6. **Market Benchmark Return (1 feature):** Daily return of the S&P 500 index (`sprtrn`).

### Feature Preprocessing & Scaling

- Missing data handling: Forward-filling (`ffill(limit=1)`) is applied as a guard for spread features.
- Normalization: Fixed `RobustScaler` (scaling by median centering and Interquartile Range, $\text{IQR} = Q_{75} - Q_{25}$) fitted strictly on the initial training period (2007–2020) and applied out-of-sample without dynamic refitting, eliminating look-ahead bias and handling fat-tailed outliers.

### Neural Network Architecture (`AttentionLSTM`)

- **Input Layer:** Tensor of shape $(B, T_{\text{in}}=180, F=251)$.
- **LSTM Backbone:** PyTorch `nn.LSTM` with `input_size = 251`, `hidden_size = 16`, `num_layers = 4`, `batch_first = True`, `dropout = 0.2`. Outputs hidden tensor $\mathbf{H} \in \mathbb{R}^{B \times 180 \times 16}$.
- **Normalization & Activation:** `nn.LayerNorm(16)` applied to hidden states, followed by `torch.relu` and `nn.Dropout(0.2)`.
- **Temporal Self-Attention (`TemporalAttention`):**
  - Multi-head self-attention operating along the time dimension ($T=180$) with `nheads = 2`, `embed_dim = 16`.
  - Computes queries, keys, and values: $\mathbf{Q} = \mathbf{H} W_Q, \mathbf{K} = \mathbf{H} W_K, \mathbf{V} = \mathbf{H} W_V$.
  - Scaled dot-product attention: $\mathbf{A} = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}}\right) \mathbf{V}$.
  - Residual connection and dropout: $\mathbf{H}_{\text{attn}} = \text{Dropout}(\mathbf{A}) + \mathbf{H}$.
- **Temporal Mean Pooling:** Collapses the time dimension:
  $$\mathbf{c} = \frac{1}{T_{\text{in}}} \sum_{t=1}^{T_{\text{in}}} \mathbf{H}_{\text{attn}, t} \in \mathbb{R}^{B \times 16}$$
- **Linear Output Projection:** Fully connected layer `nn.Linear(16, 50)` mapping pooled representation to asset logits $\mathbf{z} \in \mathbb{R}^{B \times 50}$.
- **Softmax Normalization:**
  $$w_i = \frac{e^{z_i}}{\sum_{j=1}^{50} e^{z_j}}, \quad \forall i \in \{1, \dots, 50\}$$
  Guarantees a fully invested, long-only portfolio satisfying $\sum_{i=1}^{50} w_i = 1$ and $w_i \ge 0$.

### Loss Function Formulation (`CustomLossB` / `custom_loss_11`)

The model is trained to minimize the composite loss over the forward holding window ($T_{\text{out}} = 60$ trading days):
$$\mathcal{L}_{\text{CustomLossB}} = \mathcal{L}_{\text{SmoothOmega}} + \lambda_{\text{CVaR}} \cdot \mathcal{L}_{\text{RockafellarCVaR}} + \lambda_{\text{RP}} \cdot \mathcal{L}_{\text{RiskParity}}$$

Where the component terms are rigorously specified:
1. **Smooth Omega Objective (`smooth_omega_objective`):**
   - Softplus smoothed positive and negative return deviations:
     $$\text{pos}_t = \text{softplus}(r_{p,t} - \theta, \beta=10) = \frac{1}{10} \ln(1 + e^{10(r_{p,t} - \theta)})$$
     $$\text{neg}_t = \text{softplus}(\theta - r_{p,t}, \beta=10) = \frac{1}{10} \ln(1 + e^{10(\theta - r_{p,t})})$$
   - Expected means: $\mu_{\text{pos}} = \frac{1}{T}\sum_{t=1}^T \text{pos}_t$, $\mu_{\text{neg}} = \frac{1}{T}\sum_{t=1}^T \text{neg}_t$.
   - Omega ratio: $\Omega = \frac{\mu_{\text{pos}}}{\mu_{\text{neg}} + \epsilon}$ (with threshold $\theta = 0.0$, $\epsilon = 10^{-8}$).
   - Canonical negative log loss: $\mathcal{L}_{\text{SmoothOmega}} = -\ln(\Omega + \epsilon)$.
2. **Differentiable Rockafellar-Uryasev CVaR Regularizer (`smooth_rockafellar_cvar_regularizer`):**
   - Portfolio losses: $L_t = -r_{p,t}$.
   - Detached Value-at-Risk threshold at confidence $\alpha = 0.05$:
     $$\zeta = \text{Quantile}_{1-\alpha}(L) \quad (\text{evaluated with } \text{torch.no\_grad}())$$
   - Smooth excess loss via softplus with temperature $\tau = 0.01$:
     $$\text{excess}_t = \text{softplus}(L_t - \zeta, \beta = 1/\tau)$$
   - Raw CVaR estimate: $\text{CVaR}_{\text{raw}} = \zeta + \frac{1}{\alpha} \left(\frac{1}{T}\sum_{t=1}^T \text{excess}_t\right)$.
   - Scale-invariant tail ratio normalization:
     $$\mathcal{L}_{\text{RockafellarCVaR}} = \frac{\text{CVaR}_{\text{raw}}}{\max(\sigma(r_p), \text{floor}=10^{-3}) + \epsilon}$$
3. **Risk Parity Regularizer with Linear Shrinkage (`risk_parity_regularizer`):**
   - Sample covariance of returns: $\hat{\Sigma} \in \mathbb{R}^{50 \times 50}$.
   - Linear shrinkage toward scaled identity:
     $$\Sigma_{\text{shrunk}} = (1 - \rho)\hat{\Sigma} + \rho \cdot \frac{\text{Tr}(\hat{\Sigma})}{N} I_N \quad (\rho = 0.1)$$
   - Portfolio variance: $\sigma_p^2 = \mathbf{w}^\top \Sigma_{\text{shrunk}} \mathbf{w}$.
   - Marginal risk contributions: $RC_i = w_i (\Sigma_{\text{shrunk}} \mathbf{w})_i$.
   - Target equal contribution: $\text{Target} = \sigma_p^2 / N$.
   - Scale-invariant squared deviation loss:
     $$\mathcal{L}_{\text{RiskParity}} = \frac{\sum_{i=1}^N (RC_i - \text{Target})^2}{(\sigma_p^2)^2 + \epsilon}$$

### Hyperparameters & Maximin Tuning Procedure

- Tuned Loss Regularization Weights: $\lambda_{\text{CVaR}} = 0.01$, $\lambda_{\text{RP}} = 0.1$.
- Optimizer: AdamW with learning rate $\eta = 1 \times 10^{-4}$, weight decay $1 \times 10^{-2}$.
- Training Batch Size: 64; gradient norm clipping: 0.5; epochs: 200.
- Learning Rate Scheduler: `ReduceLROnPlateau` with decay factor 0.5, patience 10 epochs, minimum learning rate $1 \times 10^{-6}$.
- Maximin Optuna Tuning Objective: Hyperparameters were selected by maximizing the 95% lower confidence bound of the mean Information Ratio across all validation walk-forward steps:
  $$\text{Objective} = \overline{IR} - t_{0.95, K-1} \cdot \frac{\sigma_{IR}}{\sqrt{K}}$$
  where excess return is measured against the equal-weight portfolio benchmark.

### Rebalancing & Execution Cadence

- Cadence: Quarterly rebalancing ($T_{\text{out}} = 60$ trading days, $\approx 3$ calendar months).
- Walk-forward expansion: At each quarter $k$, the training set is expanded to include the preceding quarter's realized data. The model is trained from scratch on all cumulative historical windows.
- Weights $\mathbf{w}^{(k)}$ are inferred using the immediately preceding 180 trading days and held fixed across the entire 60-day holding window.

## Required data

- **Asset Universe:** 50 constituent equities of the S&P 500 index.
- **Market Venue / Data Source:** Center for Research in Security Prices (CRSP) daily stock database accessed through Wharton Research Data Services (WRDS).
- **Market Type:** US equity spot shares.
- **Time Horizon:** Daily closing observations spanning December 7, 2007 to November 29, 2023.
- **Required Fields:**
  - Date (`date`).
  - Asset daily returns (`RET`).
  - Quoted bid-ask spread (`BA_SPREAD`).
  - Amihud illiquidity metric (`ILLIQUIDITY`).
  - Daily trading volume percentage change (`VOL_CHANGE`).
  - Share turnover (`TURNOVER`).
  - S&P 500 market benchmark return (`sprtrn`).
- **Point-in-Time Availability:** Features are formed strictly at the close of trading day $t$. At each quarterly boundary, weights for quarter $k$ are computed using data up to day $T_k$ and deployed at market open of day $T_k + 1$.
- **Missing Data Handling:** CRSP data had zero missing values in the primary dataset; `ffill(limit=1)` is specified as a standard handling protocol for quoted spreads.

## Execution assumptions

- **Portfolio Constraints:** Long-only, fully invested ($\sum_{i=1}^{50} w_i = 1$, $w_i \ge 0$). No short selling, no margin, no leverage.
- **Rebalance Frequency:** Exactly once every 60 trading days (quarterly). No intraday or inter-quarter rebalancing.
- **Transaction Cost Model:**
  - Turnover at walk-forward step $k$:
    $$\text{Turnover}^{(k)} = \sum_{i=1}^N \left|w_i^{(k)} - w_i^{(k-1)}\right| \quad (\text{with } \mathbf{w}^{(0)} = \mathbf{0})$$
  - Realized rebalancing transaction cost (deducted on day 1 of the holding window):
    $$\text{Cost}^{(k)} = \sum_{i=1}^N \left|w_i^{(k)} - w_i^{(k-1)}\right| \cdot \left(\frac{1}{2} \cdot \text{BA-Spread}_{i,1}^{(k)}\right)$$
    where $\text{BA-Spread}_{i,1}^{(k)}$ is the exact observed bid-ask spread of asset $i$ on the first trading day of the quarter.
  - Net return accounting:
    $$r_{1, \text{net}}^{(k)} = r_{1, \text{gross}}^{(k)} - \text{Cost}^{(k)}$$
    $$r_{t, \text{net}}^{(k)} = r_{t, \text{gross}}^{(k)} \quad \text{for } t = 2, \dots, 60$$
- **Fill Assumptions:** Orders execute at the closing price net of half the bid-ask spread. No market impact beyond the quoted spread is modeled. Benchmarks (S&P 500 and Equal-Weight) are evaluated without transaction costs, providing a conservative hurdle for the neural model.

## Evidence

### Source-reported

All performance figures below are directly reported by Fernandes and Desell (arXiv:2605.28853v1, May 2026; Table I, Section V, and audited test notebook `exploration/test_analysis.ipynb`) across 30 random initializations (seeds) over the 480-trading-day out-of-sample test period (January 3, 2022 to November 29, 2023), net of bid-ask spread transaction costs:

| Strategy / Model | Compounded Return | Annualized Sharpe | Annualized Sortino | Max Drawdown | CVaR (5%) | Omega ($\theta=0$) | Calmar Ratio |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **AttentionLSTM-CustomLossB (Mean)** | **+7.86%** (+7.8567%) | **+0.2900** | **+0.4599** | **-20.21%** | **-2.86%** (-2.8573%) | **1.0504** | **+0.2333** |
| AttentionLSTM-CustomLossB (Median) | +8.93% | +0.3160 | +0.5048 | -19.52% | -2.79% | 1.0545 | +0.2336 |
| AttentionLSTM-CustomLossB (Std Dev) | 8.28% | 0.1920 | 0.2995 | 4.17% | 0.23% | 0.0338 | 0.2373 |
| AttentionLSTM-CustomLossB (95% CI) | [5.29%, 10.43%] | [0.2183, 0.3617] | [0.3670, 0.5528] | [-21.49%, -18.92%] | [-2.94%, -2.77%] | [1.040, 1.061] | [0.160, 0.307] |
| **S&P 500 Index Benchmark** | **-4.52%** | **-0.0240** | **-0.0363** | **-25.43%** | **-2.84%** | **0.9960** | **-0.0945** |
| **Nested Clustered Optimization (NCO)** | **-0.64%** | **+0.0536** | **+0.0823** | **-17.20%** | **-2.15%** | **1.0089** | **-0.0196** |
| **Hierarchical Risk Parity (HRP)** | **-7.94%** | **-0.1776** | **-0.2831** | **-19.80%** | **-2.24%** | **0.9714** | **-0.2147** |
| **Equal-Weight Portfolio** | **-9.99%** | **-0.1999** | **-0.3208** | **-21.23%** | **-2.55%** | **0.9678** | **-0.2531** |
| **Global Minimum Variance (GMV)** | **-9.02%** | **-0.2573** | **-0.3928** | **-16.84%** | **-2.10%** | **0.9587** | **-0.2874** |
| **Mean-Variance with Shrinkage** | **-34.21%** | **-0.6922** | **-1.0964** | **-43.62%** | **-3.63%** | **0.8901** | **-0.4525** |
| DeformTime-CustomLossB (Mean) | +2.61% | +0.1674 | +0.2634 | -46.14% | -5.76% | 1.0329 | +0.0733 |
| TemporalTransformer-CustomLossB (Mean) | +2.07% | +0.1500 | +0.2492 | -23.59% | -3.02% | 1.0260 | +0.0911 |
| PatchTST-CustomLossB (Mean) | -5.96% | -0.0459 | -0.0711 | -23.46% | -2.94% | 0.9928 | -0.1314 |
| VSN-LSTM-CustomLossB (Mean) | -8.72% | -0.0755 | -0.1177 | -30.02% | -3.29% | 0.9882 | -0.1472 |
| InvertedAttentionLSTM-CustomLossA (Mean) | -13.23% | -0.2064 | -0.3304 | -27.51% | -3.17% | 0.9672 | -0.2465 |

- **Outperformance Margin:** AttentionLSTM-CustomLossB beat the S&P 500 total compounded return by +12.38 percentage points (+7.86% vs -4.52%, a relative return difference exceeding 270%) and surpassed NCO by +8.50 percentage points (+7.86% vs -0.64%).
- **Tail Risk Stability:** Tail risk (CVaR) was virtually identical between AttentionLSTM (-2.86%) and the S&P 500 (-2.84%), confirming that outperformance was achieved without taking on excessive downside exposure.
- **Statistical Significance (Section V-A & Notebook Cell 38/39):**
  - Against S&P 500: One-sample t-test on Sharpe ratio yields $t_{29} = 8.9587$, raw $p = 3.76 \times 10^{-10}$, Bonferroni-corrected $p < 10^{-8}$. For CVaR, $t_{29} = -0.4164$, $p = 0.6599$ (no significant increase in tail loss).
  - Against NCO: One-sample t-test on Sharpe yields $t_{29} = 6.7449$, raw $p = 1.06 \times 10^{-7}$, Bonferroni-corrected $p = 1.0 \times 10^{-6}$.
  - Paired t-tests against alternative neural architectures: AttentionLSTM significantly outperforms TemporalTransformer ($p = 0.0129$), VSN-LSTM ($p = 5.59 \times 10^{-7}$), PatchTST ($p = 2.84 \times 10^{-9}$), and InvertedAttentionLSTM ($p = 1.06 \times 10^{-10}$). Paired difference against DeformTime in Sharpe was not significant ($p = 0.5334$), but DeformTime exhibited catastrophic tail drawdown (-46.14% vs -20.21%).

### Independently reproduced

`Not independently reproduced.`

All quantitative claims and performance statistics are source-reported from arXiv:2605.28853v1 and its primary GitHub repository (`rahulkfernandes/Financially-Guided-Deep-Portfolio-Optimization` at commit `ed35155d6fce3bd03232e946994c46de0a57aa5e`). No independent training run or backtest execution in NautilusTrader or PyBroker was conducted.

### Negative evidence

- **Lagged Bear Market Adaptation (Initial Underperformance):** During the first two quarters of 2022 (the initial onset of the aggressive Federal Reserve rate-hiking cycle), AttentionLSTM underperformed NCO:
  - Q1 2022 (2022-01-03 to 2022-03-29): AttentionLSTM returned -3.99% vs NCO +1.51% (S&P 500 -2.87%).
  - Q2 2022 (2022-03-30 to 2022-06-24): AttentionLSTM returned -8.85% vs NCO +2.23% (S&P 500 -14.79%).
  The model's cumulative performance only surpassed NCO starting in Q3 2022 (+4.91% vs -0.52%) as the expanding training window incorporated sufficient observations from the new regime.
- **Architectural Fragility Under Financially Guided Loss:** While AttentionLSTM succeeded, several other prominent deep architectures failed under the same loss:
  - PatchTST-CustomLossB produced a negative Sharpe (-0.0459) and negative return (-5.96%).
  - VSN-LSTM-CustomLossB produced a negative Sharpe (-0.0755) and -8.72% return.
  - InvertedAttentionLSTM-CustomLossA delivered a -13.23% return with a Sharpe of -0.2064.
- **Deformable Attention Tail Risk Explosion:** While DeformTime achieved positive Sharpe (0.1674), it suffered severe tail risk failure: CVaR degraded to -5.76% and maximum drawdown reached -46.14% (nearly double the S&P 500's -25.43% drawdown).
- **Survivorship & Universe Bias:** The 50 constituent stocks were fixed based on index presence across the full timeline without simulating point-in-time constituent reconstitution, introducing potential survivorship bias.

## Falsification plan

To falsify the claim that end-to-end AttentionLSTM with Omega-CVaR-RiskParity loss provides structural outperformance:
1. **Survivorship-Free Universe Test:** Replicate the expanding-window walk-forward procedure on a point-in-time survivorship-bias-free universe (e.g., Russell 1000 or full S&P 500 with historical constituent additions/deletions).
   - *Falsification criteria:* If the out-of-sample Information Ratio relative to Equal-Weight drops below 0.0 or if annualized Sharpe fails to exceed NCO at $p \ge 0.05$, the survivorship-free alpha claim is falsified.
2. **Loss Component Ablation:** Train AttentionLSTM under three ablation variants:
   - Variant A: Smooth Omega alone ($\lambda_{\text{CVaR}} = 0, \lambda_{\text{RP}} = 0$).
   - Variant B: Smooth Omega + CVaR ($\lambda_{\text{RP}} = 0$).
   - Variant C: Smooth Omega + Risk Parity ($\lambda_{\text{CVaR}} = 0$).
   - *Falsification criteria:* If Variant B or C matches or outperforms the full three-term loss, the hypothesized tripartite interaction mechanism is refuted.
3. **Rebalancing Frequency & Friction Stress:** Re-evaluate the model at monthly ($T_{\text{out}} = 20$) and bi-weekly ($T_{\text{out}} = 10$) rebalance frequencies under varying transaction cost levels (1x, 2x, 5x quoted spread).
   - *Falsification criteria:* If higher rebalancing turnover generates costs that fully erode excess return over NCO, the mechanism is valid only as a low-frequency allocation policy.
4. **Phase-Randomized Placebo Test:** Train the model on phase-randomized surrogate returns that preserve empirical covariance and marginal variance distributions but destroy temporal sequence predictability.
   - *Falsification criteria:* If the model trained on surrogate data generates positive out-of-sample Sharpe ratios comparable to real data, the model is exploiting cross-sectional distributional artifacts rather than genuine temporal lead-lag patterns.

## Crypto portability

- **Classification:** `adapted` / `unproven`.
- **Porting Rationale:** The primary source investigates US equity spot shares exclusively. Applying this end-to-end architecture to cryptocurrency assets is an adapted research hypothesis, not demonstrated empirical evidence.
- **Critical Crypto Market Frictions:**
  - *24/7 Continuous Session Dynamics:* Equities trade 252 days/year in 6.5-hour daily sessions. Crypto markets trade 365 days/year continuously. A 60-day holding window in crypto represents only ~2 months of continuous trading, while market volatility regimes transition much faster.
  - *Extreme Tail Risk & Asset Delisting:* S&P 500 constituents have mature corporate balance sheets and low acute default probability over 60-day horizons. In crypto, mid-cap tokens frequently experience idiosyncratic drawdowns exceeding 70–90% within days. The Rockafellar-Uryasev CVaR regularizer would require tighter quantile thresholds (e.g., $\alpha = 0.01$) or continuous trailing stop mechanisms.
  - *Perpetual Futures Funding Rate Drag:* In crypto perpetual contracts (`USDT-M Perps`), holding a static long-only basket across 60 days exposes capital to 8-hour funding cash flows. In strong bull regimes (persistent contango), paying 5–15 bps daily funding translates to 3.6%–10.8% quarterly funding drag, which would entirely consume the reported equity gross edge (+7.86% over 2 years).
  - *Liquidity Fragmentation & Execution Spread:* Unlike CRSP large-cap stocks with liquid National Best Bid and Offer (NBBO), crypto tokens exhibit fragmented liquidity across centralized (Binance, Bybit, OKX) and decentralized (Uniswap) venues, requiring venue-specific slippage modeling.

## Limitations

- `not independently reproduced`: All performance figures, t-statistics, and confidence intervals are third-party source-reported.
- `unproven in crypto`: Empirical testing was conducted exclusively on US equities; portability to digital assets is unproven.
- `underspecified universe selection`: The exact selection rule for the 50 S&P 500 constituent tickers out of the 500 possible index members is not specified in the paper text (fixed sample provided in repository).
- `low-frequency lag during market shocks`: The model suffered drawdowns (-12.84% combined over Q1–Q2 2022) at the onset of the bear market before adapting to the new regime.
- `computational overhead`: Hyperparameter tuning using Optuna with expanding walk-forward windows over 100 trials requires substantial GPU cluster resources (A100 / H100 with OpenMPI).
- `omission of market impact`: The transaction cost model deducts half the quoted bid-ask spread but does not account for size-dependent square-root market impact or order-book depth exhaustion.

## Implementation status

- `not-implemented`.
- No implementation exists in NautilusTrader, PyBroker, paper trading, or live execution systems.
- This record serves exclusively as upstream normalized research for subsequent review.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- This record is an analytical capture of academic research. It does not constitute approval for strategy implementation, paper trading, testnet allocation, or live capital deployment.

## Related Wiki records

- `[[quant/cross-asset-futures-vsn-xlstm-sharpe-optimal-portfolio-2026-09-03]]` — Explores end-to-end Sharpe optimization in modern sequence architectures (VSN-xLSTM) across multi-asset futures.
- `[[quant/decision-focused-sparse-tangent-portfolio-dpp-topk-2026-09-03]]` — Investigates decision-focused learning and determinantal point processes for portfolio selection.
- `[[quant/crypto-cross-sectional-return-rank-mlp-decay-portfolio-2026-09-03]]` — Cross-sectional return rank prediction and decay-weighted portfolio construction in cryptocurrency markets.
- `[[quant/lstm-learnable-sector-embeddings-cross-sectional-reversal-2026-09-02]]` — Evaluates LSTM architectures with learnable structural embeddings for cross-sectional momentum and reversal.
- `[[quant/observable-matrix-dynamics-portfolio-optimization-2026-09-02]]` — Studies observable covariance matrix dynamics and shrinkage regularization in continuous portfolio optimization.

## Sources

1. Rahul Fernandes and Travis Desell, *"Financially Guided Deep Portfolio Optimization"*, arXiv preprint `arXiv:2605.28853v1 [q-fin.PM, cs.LG]`, May 2026. DOI: [https://doi.org/10.48550/arXiv.2605.28853](https://doi.org/10.48550/arXiv.2605.28853). Stable URL: [https://arxiv.org/abs/2605.28853](https://arxiv.org/abs/2605.28853). Full text HTML: [https://arxiv.org/html/2605.28853v1](https://arxiv.org/html/2605.28853v1).
2. Primary Source Code Repository: GitHub `https://github.com/rahulkfernandes/Financially-Guided-Deep-Portfolio-Optimization.git`, immutable commit SHA `ed35155d6fce3bd03232e946994c46de0a57aa5e` (Release tag `v1.0-paper`, commit `f45b48ccefcad549d5d80443d393a7765c5534f1`).
3. R. Tyrrell Rockafellar and Stanislav Uryasev, *"Optimization of Conditional Value-at-Risk"*, *Journal of Risk* 2(3), 2000, pp. 21–41. DOI: [10.21314/JOR.2000.038](https://doi.org/10.21314/JOR.2000.038).
4. Marcos Lopez de Prado, *"Building Diversified Portfolios that Outperform Out-of-Sample"*, *Journal of Portfolio Management* 42(4), 2016, pp. 59–69. DOI: [10.3905/jpm.2016.42.4.059](https://doi.org/10.3905/jpm.2016.42.4.059).
5. Marcos Lopez de Prado, *"A Robust Estimator of the Efficient Frontier"*, SSRN Electronic Journal, 2019. DOI: [10.2139/ssrn.3469961](https://doi.org/10.2139/ssrn.3469961).
6. Bryan Lim, Sercan Ö. Arık, Nicolas Loeff, and Tomas Pfister, *"Temporal Fusion Transformers for Interpretable Multi-Horizon Time Series Forecasting"*, *International Journal of Forecasting* 37(4), 2021, pp. 1748–1764. DOI: [10.1016/j.ijforecast.2021.03.012](https://doi.org/10.1016/j.ijforecast.2021.03.012).
7. Harry Markowitz, *"Portfolio Selection"*, *The Journal of Finance* 7(1), 1952, pp. 77–91. DOI: [10.2307/2975974](https://doi.org/10.2307/2975974).
