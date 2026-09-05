---
schema: strategy-research-record-v1
title: "KASPER: Kolmogorov-Arnold Networks for Stock Prediction and Explainable Regimes via Gumbel-Softmax and Temporal Shapley Attribution"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - machine-learning
  - kolmogorov-arnold-networks
  - kan
  - regime-detection
  - gumbel-softmax
  - spline-activation
  - shapley-values
  - stock-prediction
  - equities
status: research-only
confidence: medium
source_as_of: 2025-07-28
sources:
  - "arXiv:2507.18983v1 [cs.LG, q-fin.ST], 28 July 2025. https://arxiv.org/abs/2507.18983"
  - "https://doi.org/10.48550/arXiv.2507.18983"
  - "https://arxiv.org/html/2507.18983v1"
  - "Suruchi Arora, 'Yahoo Finance Dataset (2018-2023)', Kaggle Datasets (2023). https://www.kaggle.com/datasets/suruchiarora/yahoo-finance-dataset-2018-2023"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# KASPER: Kolmogorov-Arnold Networks for Stock Prediction and Explainable Regimes via Gumbel-Softmax and Temporal Shapley Attribution

## Provenance

- **Primary Source:** Vidhi Oad, Param Pathak, Nouhaila Innan, Shalini Devendrababu, and Muhammad Shafique, *"KASPER: Kolmogorov Arnold Networks for Stock Prediction and Explainable Regimes"*, arXiv preprint `arXiv:2507.18983v1 [cs.LG, q-fin.ST]`, submitted July 28, 2025; accepted and published in *Transactions on Machine Learning Research (TMLR)* (2026).
- **Canonical DOI:** [10.48550/arXiv.2507.18983](https://doi.org/10.48550/arXiv.2507.18983)
- **Canonical Web Abstract:** [https://arxiv.org/abs/2507.18983](https://arxiv.org/abs/2507.18983)
- **Canonical HTML Full Text:** [https://arxiv.org/html/2507.18983v1](https://arxiv.org/html/2507.18983v1)
- **External Public Dataset Reference:**
  - Suruchi Arora, *"Yahoo Finance Dataset (2018-2023)"*, Kaggle Datasets (2023). Public URL: [https://www.kaggle.com/datasets/suruchiarora/yahoo-finance-dataset-2018-2023](https://www.kaggle.com/datasets/suruchiarora/yahoo-finance-dataset-2018-2023).
- **Deduplication Audit:** A full audit of the repository confirms zero prior captures referencing `2507.18983`, `KASPER`, `Oad`, `Pathak`, `Innan`, `Devendrababu`, `Shafique`, or `suruchiarora`.
  - The repository contains one other KAN-related record: `temporal-kolmogorov-arnold-networks-high-frequency-lob-alpha-decay-2026-09-02.md` (T-KAN), which investigates high-frequency limit order book (LOB) microstructural alpha decay in equity tick data without regime detection.
  - In contrast, KASPER couples a Gumbel-Softmax differentiable regime classifier with contrastive and orthogonality penalties in Layer 1, and routes predictions to regime-specific sparse B-spline KAN predictors with temporal Monte Carlo Shapley rule extraction in Layer 2 for daily equity return forecasting.

## Economic mechanism

### Source-reported

In financial markets, asset return dynamics, volatility, and cross-feature interactions shift across latent macroeconomic and behavioral market regimes (e.g., bull trends, bear sell-offs, and stagnant consolidation). Standard deep learning models (MLPs, LSTMs, Transformers) employ fixed activation functions on neurons (such as ReLU, GELU, or Sigmoid) and dense weight matrices, which suffer from two key limitations:
1. **Regime Over-Smoothing and Black-Box Inflexibility:** Fixed-activation models learn an average mapping across conflicting regimes, leading to severe underfitting or parameter overfitting during volatile regime transitions.
2. **Lack of Explainability:** Black-box neural representations fail to reveal which price-action drivers govern specific market phases, impeding human auditability and risk control.

To address this, the authors propose KASPER, based on the Kolmogorov-Arnold representation theorem (which states that any multivariate continuous function can be decomposed into a finite sum of univariate continuous functions). KASPER introduces learnable 1D B-spline activation functions placed directly on network edges rather than fixed node activations.

The architecture operates in two stages:
1. **KAN Layer 1 (Regime Detection):** Uncovers latent market states ($k=3$ regimes) from rolling historical windows of price and volatility features. It combines:
   - Learnable hybrid linear and cubic B-spline activation functions initialized on empirical quantile knot grids.
   - Differentiable Gumbel-Softmax categorical sampling:
     $$p_i = \frac{\exp((f_i + g_i)/\tau)}{\sum_{j=1}^k \exp((f_j + g_j)/\tau)}$$
     with Gumbel noise $g_i \sim \text{Gumbel}(0, 1)$ and annealing temperature $\tau$.
   - Contrastive representation separation:
     $$\mathcal{L}_{\text{contrastive}} = \sum_{i,j} y_{ij} \|z_i - z_j\|_2^2 + (1 - y_{ij}) \max(0, m - \|z_i - z_j\|_2)^2$$
   - Orthogonality regularization on regime weight matrices $W_r$:
     $$\mathcal{L}_{\text{ortho}} = \sum_r \|W_r W_r^T - I\|_F^2$$
     preventing feature collapse and forcing distinct, decorrelated regime representations.
2. **KAN Layer 2 (Regime-Adaptive Forecasting):** Generates regime-conditioned next-day return forecasts $\hat{y}_t^{(i)}$ using regime-specific B-splines:
   $$\hat{y}_t^{(i)} = \sum_j w_j^{(i)} \phi_j^{(i)}(x_{j,t}), \quad \phi_j^{(i)}(x) = \sum_k \beta_{j,k}^{(i)} B_k(x; \xi^{(i)})$$
   subject to dynamic $\ell_1$ sparsity pruning on coefficients $w_j^{(i)}$ to eliminate noisy weights.
3. **Temporal Monte Carlo Shapley Attribution:** Quantifies the marginal contribution of each feature per regime, weighting historical Shapley estimates with an exponential time-decay factor $\gamma^{T-t}$ to extract human-interpretable trading rules.

### Research interpretation

The economic thesis rests on conditional non-linearity: the predictive relationship between intraday price action (such as open-to-close spread, high-to-low range, and price velocity) and subsequent-day return is non-stationary and non-linear. In consolidating (neutral) regimes, intraday price range and reversal dynamics dominate; in strong trending regimes, directional persistence (open-to-close velocity) dominates while volatility range metrics lose predictive power.

By partitioning the latent state space using an orthogonalized Gumbel-Softmax gate and fitting univariate cubic splines per regime, KASPER approximates arbitrary non-linear response curves with localized parameter support, preventing catastrophic interference between regime-specific alphas.

Component decomposition:
- **Regime Gate:** KAN Layer 1 with hybrid linear/cubic splines + Gumbel-Softmax ($k=3$).
- **Disentanglement Regularizer:** Contrastive loss ($\lambda_c = 0.01$) + weight orthogonality ($\lambda_o = 0.01$).
- **Predictive Engine:** KAN Layer 2 with regime-specific B-splines and adaptive $\ell_1$ pruning ($\lambda_s = 0.001$).
- **Rule Extractor:** Temporally discounted Monte Carlo Shapley value ranking.

## Signal

- **Signal formation timestamp:** Daily close ($t$) after market settlement (`research-proposed execution convention`; source states daily feature engineering and next-day return target).
- **Target definition (source-reported):**
  $$y_t = \frac{\text{future\_close} - \text{close}_t}{\text{close}_t} = \frac{p_{t+1} - p_t}{p_t}$$
  where $\text{future\_close} = p_{t+1}$ is the closing price of the next trading day shifted by $-1$.
- **Input state matrix $S_t \in \mathbb{R}^{n \times f}$ (source-reported):**
  - Rolling historical lookback window: $n$ days (`research-proposed window length: n = 20 days` based on rolling window convention).
  - 15 raw engineered features generated on historical data with closed-left windows:
    1. `OC_spread`: $\frac{\text{Close}_t - \text{Open}_t}{\text{Open}_t}$
    2. `HL_spread`: $\frac{\text{High}_t - \text{Low}_t}{\text{Low}_t}$
    3. `price_velocity`: $\frac{\text{Close}_t - \text{Close}_{t-1}}{\Delta t}$
    4. `price_acceleration`: $\frac{\text{velocity}_t - \text{velocity}_{t-1}}{\Delta t}$
    5. `volatility_ratio`: rolling standard deviation of returns
    6. `momentum_state`: trend momentum indicator
    7. `ATR`: Average True Range
    8. Additional price lags and rolling volume/price statistics.
  - Feature selection: Top 8 features selected via `SelectKBest(score_func=f_regression)`.
  - Feature normalization: `StandardScaler` fitted on training split for both inputs and target.
- **Model hyperparameters & architectures (source-reported):**
  - Number of regimes $k = 3$ (Regime 0: Neutral/Consolidation, Regime 1: Transitional/Breakout, Regime 2: Directional/Trending).
  - Hidden dimension: 64.
  - Spline configuration: Hybrid linear (3 knots) and cubic (2 knots) splines initialized with empirical quantile knot grids.
  - Activations: `SplineActivation` and `GELU`.
  - Optimizer: AdamW ($lr = 0.001$, $weight\_decay = 10^{-5}$).
  - Batch size: 32.
  - Epochs: 100 with early stopping (patience = 15).
  - Scheduler: `ReduceLROnPlateau` (decay factor = 0.7, patience = 7).
  - Gradient clipping: 0.5.
- **Loss function (source-reported):**
  $$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{Huber}}(y_t, \hat{y}_t) + 0.01 \mathcal{L}_{\text{contrastive}} + 0.001 \mathcal{L}_{\text{sparse}} + 0.01 \mathcal{L}_{\text{ortho}} + 0.05 \mathcal{L}_{\text{balance}}$$
- **Directional trading trigger (`research-proposed trading rule`):**
  - Long entry: Enter Long if $\hat{y}_t > +\epsilon_{\text{threshold}}$.
  - Short entry: Enter Short if $\hat{y}_t < -\epsilon_{\text{threshold}}$ (or flat in long-only equity implementation).
  - In source evaluations: Directional trade evaluation uses $\text{sign}(\hat{y}_t) == \text{sign}(y_t)$ with $\epsilon_{\text{threshold}} = 0.0$.
  - Holding period: Exactly 1 trading day (close-to-close rebalancing).

## Required data

- **Instrument / Universe:** U.S. equities time series from Yahoo Finance (source references Suruchi Arora Kaggle dataset 2018–2023; exact single ticker vs multi-asset constituent list is underspecified in paper text; `provenance gap`).
- **Venue:** U.S. National Market System (NYSE/NASDAQ via Yahoo Finance API).
- **Market type:** Cash Equities (Spot).
- **Timeframe:** Daily bars (1D resolution, OHLCV).
- **Fields:**
  - `open`: opening price.
  - `high`: highest intraday price.
  - `low`: lowest intraday price.
  - `close`: regular session closing price.
  - `volume`: trading volume.
- **Point-in-time conventions (source-reported):**
  - Forward-filling for missing observations.
  - Closed-left windows for rolling statistics to prevent lookahead bias.
  - Strict 70% train / 15% validation / 15% test temporal split (January 2018 to December 2023).

## Execution assumptions

- **Execution timing:** Signal computed at daily close $t$; order executed at Close $t$ or Open $t+1$ (`research-proposed execution model: Market-on-Close / Market-on-Open`).
- **Transaction fees & slippage:** NOT MODELED in the source paper (`source-reported execution limitation`).
  - Reported performance figures reflect zero commissions, zero exchange fees, zero borrow costs, and zero bid-ask spread slippage.
  - Baseline retail equity fee benchmark: 0 to 1 bps per share, but bid-ask spread friction in small/mid-cap equities typically imposes 5–15 bps round-trip drag (`research-proposed fee benchmark`).
- **Shorting availability:** Assumes frictionless symmetric short execution for directional accuracy and Sharpe ratio calculations (`research-proposed operational caveat`).
- **Holding period & turnover:** Daily rebalance (holding period = 1 day), implying high annualized portfolio turnover (~200–252x notional per year).

## Evidence

### Source-reported

All quantitative figures below are directly extracted from Vidhi Oad, Param Pathak, Nouhaila Innan, Shalini Devendrababu, and Muhammad Shafique (*KASPER: Kolmogorov Arnold Networks for Stock Prediction and Explainable Regimes*, arXiv:2507.18983 / TMLR 2026), evaluated over the 15% out-of-sample test split of the Yahoo Finance dataset (2018–2023).

#### 1. Core Model Performance Metrics (Table I, Section IV-C, Section IV-D)

| Metric | Source-Reported Value | Measurement Methodology / Context |
| :--- | :---: | :--- |
| **Coefficient of Determination ($R^2$)** | **0.8953 ± 0.0030** (0.89) | 5-run walk-forward mean ± std over out-of-sample test split |
| **Mean Squared Error (MSE)** | **0.0001** | Test split prediction loss |
| **Root Mean Squared Error (RMSE)** | **0.0046** | Test split normalized scale |
| **Mean Absolute Error (MAE)** | **0.0033** | Test split mean absolute error |
| **Annualized Sharpe Ratio** | **12.02** | Calculated as $\frac{\mu_r - r_f}{\sigma_r} \times \sqrt{252}$ on strategy daily returns |
| **Peak Walk-Forward Sharpe Ratio** | **~15.0** | Peak observed during walk-forward window Period 2.0 |
| **Final Walk-Forward Sharpe Ratio** | **~6.5** | Moderated Sharpe at Period 4.0 as trend-following risk expands |
| **Maximum Drawdown (MDD)** | **-0.09%** | $\min_t (V_t / \max_{s \le t} V_s - 1)$ across the entire test horizon |
| **Win Rate** | **83.17%** | Share of profitable trades ($N_+ / N \times 100$) |
| **Peak Walk-Forward Win Rate** | **~87%** | Observed during walk-forward Period 2.0–2.5 |
| **Profit Factor** | **1.53** | Gross profits divided by gross losses ($1.53 per $1 risked) |
| **Cumulative Test Return** | **+2.76%** | Baseline test interval cumulative return |
| **Extended Walk-Forward Return** | **~+5.0%** | Cumulative return by final walk-forward period |

#### 2. Comparative Benchmark Analysis (Table III)

All baselines reported in Table III on the Yahoo Finance test dataset:

| Model / Framework | $R^2 \uparrow$ | MAE $\downarrow$ | Sharpe $\uparrow$ | Max Drawdown $\downarrow$ | MSE $\downarrow$ | RMSE $\downarrow$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **RF + Monte Carlo** (Zhao 2025 [[26]]) | 0.78 | — | 0.93 | -28.11% | 0.015 | — |
| **Single Layer LSTM** (Bhandari et al. 2022 [[10]]) | 0.79 | — | — | — | — | 40.4 |
| **LSTM + KAN** (Yao 2024 [[24]]) | — | 0.0057 | — | — | — | 0.0082 |
| **AE-LSTM + DRL** (Sagiraju & Mogalla 2022 [[27]]) | — | — | 1.85 | — | — | — |
| **VLSTAR** (Bucci & Ciciretti 2021 [[21]]) | — | — | 0.93 | — | — | — |
| **AGNES** (Bucci & Ciciretti 2021 [[21]]) | — | — | 0.82 | — | — | — |
| **DQS** (Li & Ming 2023 [[28]]) | — | — | 3.65 | — | — | — |
| **KASPER (Ours)** | **0.89** | **0.0033** | **12.02** | **-0.09%** | **0.0001** | **0.0046** |

#### 3. Empirical Regime Distribution & Shapley Feature Attribution (Section IV-B, IV-D)

- **Regime Frequency Distribution:**
  - Neutral High-Confidence Regime 0: 18.7% of samples.
  - Neutral High-Confidence Regime 2: 16.6% of samples.
  - Neutral High-Confidence Regime 1: 13.9% of samples.
  - Bearish High-Confidence Regime 2: 9.2% of samples.
  - Bullish High-Confidence Regimes: 6.3% to 7.3% across regimes.
  - Low-Confidence Classifications: < 1.5% across all states.
- **Regime Feature Importance Breakdown:**
  - *Regime 0 (Consolidation):* `OC_spread` = 88.9% (Shapley $0.016 \pm 0.014$), `price_velocity` = 3.9%, `momentum_state` = 3.1%, `HL_spread` = 4.9% (Shapley $0.011 \pm 0.006$).
  - *Regime 1 (Transitional):* `OC_spread` = 83.6% (Shapley $0.039 \pm 0.017$), `momentum_state` = 7.0%, `HL_spread` = 4.9%, `price_velocity` = 3.2%, `volatility_ratio` = 0.002.
  - *Regime 2 (Directional Trend):* `OC_spread` = 89.4% (Shapley $0.083 \pm 0.021$), `price_velocity` = 5.4%, `ATR` = 0.003, `HL_spread` = 1.0%.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Extreme Sensitivity to Frictionless Assumptions:** The reported Sharpe ratio of 12.02 and maximum drawdown of -0.09% over a 2018–2023 stock dataset are extraordinary and strongly indicative of an unpenalized theoretical execution model. With a 1-day holding period (~252 rebalances per year), a round-trip fee of just 5 bps (0.05%) would deduct $252 \times 0.05\% = 12.6\%$ annually, completely consuming the strategy's reported cumulative test return (+2.76% to +5.0%).
2. **Feature Dominance & Leakage Hazard:** The `OC_spread` ($\frac{\text{Close}_t - \text{Open}_t}{\text{Open}_t}$) accounts for 83.6% to 89.4% of total feature attribution across all regimes. If execution occurs at Close $t$ to capture $y_t = \frac{p_{t+1} - p_t}{p_t}$, the trade is valid; however, if order placement occurs at Open $t+1$ or if day $t$ Open/Close prints are misaligned with execution timestamps, substantial predictive power may evaporate.
3. **Walk-Forward Sharpe Decay:** During walk-forward testing across Periods 1.0 to 4.0, the Sharpe ratio decayed from an initial peak of ~15.0 down to ~6.5 (a >55% contraction), reflecting vulnerability to structural volatility shifts as the model rotated into trend-following regimes.
4. **Underspecified Asset Universe:** The paper references a Kaggle dataset (Suruchi Arora 2023) but omits the exact ticker identity, market capitalization filter, or index constituent definition in the text, creating a reproducibility obstacle.

## Falsification plan

1. **Transaction Cost & Slippage Friction Stress Test:**
   - *Test:* Inject realistic execution costs: 1 bps, 3 bps, 5 bps, and 10 bps per trade with 1-bar execution delay (signal formed at Close $t$, order filled at Open $t+1$ VWAP).
   - *Failure condition (`research-defined falsification threshold`):* If net annualized Sharpe ratio falls below 1.0 or cumulative return becomes negative under a 5 bps round-trip cost model, reject the strategy as an artifact of frictionless execution.
2. **Asset Universe Cross-Validation:**
   - *Test:* Evaluate KASPER across standardized liquid benchmarks: S&P 500 constituents, NASDAQ-100 constituents, and Russell 2000 constituents over 2018–2025.
   - *Failure condition (`research-defined falsification threshold`):* If the out-of-sample $R^2$ drops below 0.05 or directional accuracy drops below 52.0% across large-cap liquid equities, reject the claim of generalizable regime forecasting.
3. **Ablation of KAN vs Standard MLP/LSTM:**
   - *Test:* Replace the spline-activated KAN Layer 2 with an identical-parameter MLP with GELU/ReLU activations and an LSTM, keeping the Gumbel-Softmax regime gate fixed.
   - *Failure condition (`research-defined falsification threshold`):* If the standard MLP baseline matches KASPER's test $R^2$ within 0.02 and Sharpe ratio within 10%, the hypothesized superiority of Kolmogorov-Arnold spline representations is falsified.
4. **Label Permutation / Placebo Test:**
   - *Test:* Train KASPER on randomly permuted return targets $\tilde{y}_t = \pi(y_t)$ while keeping the feature matrix $S_t$ intact.
   - *Failure condition (`research-defined falsification threshold`):* If the permuted model achieves an $R^2 > 0.10$ or Sharpe ratio $> 1.0$, the multi-loss optimization pipeline is falsified as prone to severe spurious overfitting.

## Crypto portability

- **Portability status:** `adapted` (source demonstrates empirical testing exclusively on U.S. equities via Yahoo Finance daily data; deployment to crypto spot or perpetuals is adapted and unproven).
- **Crypto-Specific Adaptation Requirements (`research-proposed`):**
  - *24/7 Continuous Session Boundaries:* Equities possess distinct 09:30–16:00 EST cash market boundaries, making `OC_spread` ($\frac{\text{Close} - \text{Open}}{\text{Open}}$) a distinct intraday measurement. In 24/7 crypto markets, open and close are arbitrary 00:00 UTC boundaries. A crypto adaptation must test fixed-interval rolling windows (e.g., 24-hour VWAP vs 8-hour session intervals) rather than calendar Open/Close.
  - *Perpetual Funding Rate Regimes:* Crypto market regimes are heavily influenced by perpetual futures basis and 8-hour funding rates. Incorporating funding rate imbalances and open interest velocity into Layer 1 regime detection is a necessary crypto domain extension.
  - *High Volatility & Tail Fatness:* Crypto asset returns exhibit kurtosis significantly higher than equity indices; spline knot boundaries initialized via Gaussian percentiles would saturate rapidly, requiring robust Cauchy or empirical quantile knot placements.

## Limitations

- **Frictionless Backtest:** Third-party performance numbers do not include transaction fees, exchange taker fees, or market impact, which are critical at daily turnover frequencies.
- **Single-Source Universe Underspecification:** The paper does not specify the individual equity ticker symbols analyzed from the Kaggle Yahoo Finance dataset (`provenance gap`).
- **Unrealistic Absolute Sharpe Ratio:** An empirical Sharpe ratio of 12.02 over a multi-year daily stock trading horizon is extraordinarily elevated for a directional model and must be treated with skepticism pending independent friction-inclusive reproduction.
- **Computational Overhead of KAN Splines:** Evaluating and updating B-spline basis functions across multiple regimes and knots is computationally more demanding than standard matrix multiplications, increasing training time and inference latency.

## Implementation status

- `not-implemented`: No implementation or execution has been conducted in our research stack (`nautilus-quant-system` or PyBroker).
- Source authors have described the algorithmic flow and parameter specifications in the text; independent PyTorch reimplementation is feasible using standard `pykan` or `torch-kan` libraries.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Research capture does not constitute approval for paper trading, testnet deployment, or live trading. Any consideration for implementation requires independent walk-forward reproduction with realistic transaction fee modeling, execution latency audits, and liquid universe testing.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]`
- `temporal-kolmogorov-arnold-networks-high-frequency-lob-alpha-decay-2026-09-02.md`
- `regime-switching-hmm-reinforcement-learning-etf-allocation-2026-09-04.md`
- `partial-information-regime-filtering-ddpg-ornstein-uhlenbeck-pairs-trading-2026-09-05.md`
- `finance-grounded-loss-functions-band-turnover-crypto-2026-09-05.md`

## Sources

1. Vidhi Oad, Param Pathak, Nouhaila Innan, Shalini Devendrababu, and Muhammad Shafique. *"KASPER: Kolmogorov Arnold Networks for Stock Prediction and Explainable Regimes"*. arXiv preprint `arXiv:2507.18983v1 [cs.LG, q-fin.ST]`, submitted July 28, 2025; published in *Transactions on Machine Learning Research (TMLR)* (2026). DOI: [10.48550/arXiv.2507.18983](https://doi.org/10.48550/arXiv.2507.18983). Stable URL: [https://arxiv.org/abs/2507.18983](https://arxiv.org/abs/2507.18983). Full text: [https://arxiv.org/html/2507.18983v1](https://arxiv.org/html/2507.18983v1).
2. Suruchi Arora. *"Yahoo Finance Dataset (2018-2023)"*. Kaggle Datasets (2023). Stable URL: [https://www.kaggle.com/datasets/suruchiarora/yahoo-finance-dataset-2018-2023](https://www.kaggle.com/datasets/suruchiarora/yahoo-finance-dataset-2018-2023).
