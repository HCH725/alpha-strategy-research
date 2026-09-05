---
schema: strategy-research-record-v1
title: "Finance-Grounded Optimization: Differentiable Sharpe, Drawdown, and Band Turnover Losses for Crypto Market-Neutral Alpha Generation"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - deep-learning
  - loss-functions
  - sharpe-loss
  - maximum-drawdown
  - turnover-regularization
  - portfolio-optimization
  - cryptocurrency
  - binance
status: research-only
confidence: high
source_as_of: 2026-01-31
sources:
  - "arXiv:2509.04541v2 [cs.LG, q-fin.ST], 31 January 2026. https://arxiv.org/abs/2509.04541"
  - "https://doi.org/10.48550/arXiv.2509.04541"
  - "https://arxiv.org/html/2509.04541v2"
  - "https://www.kaggle.com/datasets/kkhubiev/cryptotrading"
  - "https://www.kaggle.com/code/kkhubiev/finance-grounded-loss-functions"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Finance-Grounded Optimization: Differentiable Sharpe, Drawdown, and Band Turnover Losses for Crypto Market-Neutral Alpha Generation

## Provenance

- **Primary Source:** Kasymkhan Khubiyev (Sirius University of Science and Technology, Sirius, Russia), Mikhail Semenov (Sirius University of Science and Technology), Irina Podlipnova (Sirius University of Science and Technology & Moscow Institute of Physics and Technology), and Dinara Khubieva (Kazan Federal University), *"Finance-Grounded Optimization For Algorithmic Trading"*, arXiv preprint `arXiv:2509.04541v2 [cs.LG, q-fin.ST]`, submitted September 4, 2025, revised [v2] January 31, 2026. Prepared for *ICOMP 2025: International Conference on Computational Optimization*.
- **Canonical DOI:** [10.48550/arXiv.2509.04541](https://doi.org/10.48550/arXiv.2509.04541)
- **Canonical Web Abstract:** [https://arxiv.org/abs/2509.04541](https://arxiv.org/abs/2509.04541)
- **Canonical HTML Full Text:** [https://arxiv.org/html/2509.04541v2](https://arxiv.org/html/2509.04541v2)
- **Official Open Code & Dataset Repository:**
  - Kaggle Public Dataset: [https://www.kaggle.com/datasets/kkhubiev/cryptotrading](https://www.kaggle.com/datasets/kkhubiev/cryptotrading)
  - Kaggle Implementation Notebook: [https://www.kaggle.com/code/kkhubiev/finance-grounded-loss-functions](https://www.kaggle.com/code/kkhubiev/finance-grounded-loss-functions)
- **Deduplication Audit:** A comprehensive repository-wide search confirms zero prior records matching `2509.04541`, `Khubiyev`, `Finance-Grounded`, `ModSharpe`, `LogMDD`, `BandTurnover`, or `TvrReg`. This capture is distinct from existing portfolio optimization records:
  - `smart-predict-then-optimize-spo-plus-robust-portfolio-2026-09-05.md` (Wang & Hasuike 2026, arXiv:2601.04062) investigates the Smart Predict-then-Optimize (SPO+) upper bound on decision regret with linear predictors and multiplicative box uncertainty sets on U.S. ETFs.
  - `decision-focused-sparse-tangent-portfolio-dpp-topk-2026-09-03.md` (Jeon et al. 2026, arXiv:2607.00581) evaluates cardinality-constrained $k$-sparse tangency portfolios via Disciplined Parametrized Programming (DPP) quadratic-constrained quadratic programs (QCQP) on S&P 500 equities.
  - `alphazerobeta-recurrent-ppo-market-neutral-portfolio-2026-09-02.md` evaluates reinforcement learning policy networks via Recurrent PPO on crypto perpetuals.
  - In contrast, Khubiyev et al. (2025/2026) investigate end-to-end differentiable surrogate objective functions (`LogMDDLoss`, `ModSharpeLoss`, `SharpeLoss`) coupled with piecewise-linear band turnover regularization (`TvrReg`) for multi-frequency (15m, 1h, 1d) deep neural networks (LSTM and MLP) and multi-alpha weighting across 61 Binance crypto assets.

## Economic mechanism

### Source-reported

In quantitative asset management, deep learning architectures are typically trained using standard regression loss functions, primarily Mean Squared Error (MSE):
$$\mathcal{L}_{\mathrm{MSE}} = \frac{1}{N}\sum_{i=1}^{N} \left( \hat{y}_{i,t} - f_i(\boldsymbol{\theta}, \vec{x}_t) \right)^2$$
Minimizing MSE is theoretically optimal under the Gauss–Markov theorem for linear models with homoskedastic, uncorrelated Gaussian errors. However, the authors demonstrate that financial time series, especially cryptocurrency asset returns, severely violate these assumptions:
- Return distributions exhibit pronounced heavy tails, positive/negative excess kurtosis, and time-varying volatility clustering. Shapiro–Wilk ($W$) and Pearson ($\chi^2$) normality tests on daily returns of BTCUSDT ($W = 0.95, \chi^2 = 146.19, p < 10^{-22}$), ETHUSDT ($W = 0.94, \chi^2 = 208.26, p < 10^{-25}$), and SOLUSDT ($W = 0.91, \chi^2 = 335.49, p < 10^{-73}$) decisively reject Gaussianity.
- Symmetric MSE penalizes prediction errors uniformly across all assets and regimes, treating a minor prediction variance on an unallocated asset identically to a catastrophic directional miss on an actively held asset.
- Consequently, models optimized for statistical MSE consistently fail when evaluated on financial utility metrics, producing negative test-set Sharpe ratios (e.g., LSTM MSE Sharpe $-0.4564$, MLP MSE Sharpe $-0.5924$).

To resolve this objective-metric mismatch, the authors formulate a family of "finance-grounded" loss functions directly derived from core portfolio performance metrics:
1. **Differentiable Variance-Normalized Sharpe Loss (`SharpeLoss`):**
   $$\text{SharpeLoss} = \frac{\mathbb{E}(pnl)}{\mathrm{Var}(pnl) + \varepsilon}$$
   Omits the horizon constant $\sqrt{H}$ (which does not affect gradients) and replaces standard deviation $\sigma(pnl)$ with variance $\mathrm{Var}(pnl)$ in the denominator, avoiding square-root gradient singularities when variance is small. Gradient descent minimizes $-\text{SharpeLoss}$.
2. **Scale-Invariance Pathology and Modified Sharpe Loss (`ModSharpeLoss` / `MS`):**
   Standard Sharpe loss is scale-invariant with respect to position sizing ($\alpha_i \approx 10^{-2}$ vs $\alpha_i \approx 10^2$ yield identical loss values), allowing models to converge to degenerate, unconstrained position magnitudes. The authors introduce a prediction-quality penalty:
   $$\text{ModSharpeLoss} = \mathbb{E}[\alpha - r] \frac{\mathbb{E}(pnl)}{\mathrm{Var}(pnl) + \varepsilon} = \mathbb{E}[f(x, \boldsymbol{\theta}) - y] S(\boldsymbol{\theta})$$
   To resolve sign instability when $\mathbb{E}[\alpha - r] < 0$, the authors propose norm-stabilized variants:
   $$\text{ModSharpeAbsLoss} = \mathbb{E}[|\alpha - r|] \frac{\mathbb{E}(pnl)}{\mathrm{Var}(pnl) + \varepsilon}$$
   $$\text{ModSharpeSquaredLoss} = \mathbb{E}[(\alpha - r)^2] \frac{\mathbb{E}(pnl)}{\mathrm{Var}(pnl) + \varepsilon}$$
3. **Maximum Drawdown Losses (`MDDLoss`, `LogMDDLoss`, `SoftMDDLoss`):**
   Directly penalizes peak-to-trough equity loss:
   $$\text{MDDLoss} = -\min_t DD_t, \quad DD_t = C_t - \max_{u \le t} C_u, \quad C_t = \sum_{u \le t} pnl_u$$
   Smooth variants include logarithmic scaling (`LogMDDLoss`) and soft-min approximation (`SoftMDDLoss` with temperature $\tau > 0$):
   $$\min_t z_t \approx -\tau \log \sum_t \exp(-z_t / \tau)$$
4. **Band Turnover Regularization (`TvrReg`):**
   Classical linear turnover penalties ($\lambda \cdot \text{tvr}$) monotonically penalize trading activity, driving neural network policies toward conservative, near-static allocations resembling passive buy-and-hold. The authors propose a piecewise-linear band penalty:
   $$\text{TvrReg} = \lambda \cdot \left( \max(0, \text{tvr} - tb) + \max(0, bb - \text{tvr}) \right)$$
   where $\text{tvr} = \sum_{i=1}^M |\alpha_i(d) - \alpha_i(d-1)|$, $tb$ is the upper turnover bound (set to $1.0$, preventing churn beyond 100% notional per day), $bb$ is the lower turnover bound (set to $0.3$, ensuring at least 30% reallocation to prevent buy-and-hold stagnation), and $\lambda = 1.0$.

### Research interpretation

The core economic mechanism is the geometric and path-dependent alignment of loss gradients with portfolio utility. In volatile, heavy-tailed crypto markets, prediction error is dominated by idiosyncratic noise. Decoupled two-stage pipelines (predict returns via MSE, then construct a portfolio) waste model capacity trying to fit noise in non-tradable or unallocated assets.

By embedding downside risk metrics (`LogMDDLoss`) or risk-adjusted return ratios (`ModSharpeAbsLoss`) directly into the computational graph, backpropagation assigns larger gradients to errors that cause drawdown or expand portfolio variance. 

Furthermore, the band turnover regularizer acts as a soft inertia corridor:
- Inside $[bb, tb] = [0.3, 1.0]$, the marginal penalty gradient is zero. The network has total freedom to rebalance capital when predictive signals are strong.
- Above $tb = 1.0$, linear penalties actively penalize excessive churn and transaction friction drag.
- Below $bb = 0.3$, the network is penalized for passive decay into buy-and-hold complacency, forcing the model to continuously rotate capital into higher-conviction alpha signals.

Component structure of the strategy family:
- **Predictor component:** Multi-frequency LSTM or 3-layer MLP processing 20-day multi-resolution windows (daily, hourly, 15-minute).
- **Portfolio constraint mapping $g(\cdot)$:** Demeaning and $L_2$ norm scaling enforcing market-neutrality ($\mathbf{1}^\top \vec{w} = 0$) and unit leverage ($\|\vec{w}\|_2 \le 1$).
- **Objective function:** Differentiable finance-grounded loss (`LogMDDLoss`, `ModSharpeAbsLoss`, or `SharpeLoss`).
- **Turnover control:** Piecewise-linear band penalty $\text{TvrReg}$ with bounds $[0.3, 1.0]$.
- **Multi-alpha aggregator (portfolio variant):** LSTM model weighting 20 low-correlated multimodal alphas via single-weight or point-wise weight generation.

## Signal

- **Signal formation timestamp:** Daily close prior to portfolio rebalancing. Tradable at the daily rebalance boundary (`research-proposed execution timestamp convention`; source specifies daily portfolio rebalancing and medium-frequency daily holding periods).
- **Lookback and multi-frequency input feature window (source-reported):**
  - Sliding window length: 20 calendar days prior to execution.
  - Multi-frequency structure:
    1. Days $t-20$ to $t-7$ (first 14 days): Daily returns ($14$ steps).
    2. Days $t-6$ to $t-4$ (subsequent 3 days): Hourly returns ($3 \times 24 = 72$ steps).
    3. Days $t-3$ to $t$ (final 3 days closest to execution): 15-minute returns ($3 \times 96 = 288$ steps).
  - Target variable: Next-day realized return $r_i(d) = \frac{p_i(d)}{p_i(d-1)} - 1$.
- **Extracted market variables (source-reported):**
  - Open, High, Low, Close prices.
  - Base and Quote asset trading volumes.
  - Taker buy volumes (base and quote assets).
  - Total count of executed trades.
- **Predictor architectures & training details (source-reported):**
  - **LSTM:** Recurrent neural network with a linear output projection layer. Optimizer: AdamW. Constant learning rate: $\eta = 10^{-3}$.
  - **MLP:** 3 fully connected dense layers with ReLU activations. Optimizer: AdamW. Constant learning rate: $\eta = 10^{-5}$.
  - No learning rate scheduling or post-hoc smoothing applied.
- **Portfolio transformation mapping $g(\cdot)$ (source-reported):**
  - Given raw model output score vector $\vec{s}_t = f(\vec{x}_t; \boldsymbol{\theta}) \in \mathbb{R}^N$:
  - Enforce dollar market-neutrality: $\mathbf{1}^\top \vec{w}_t = 0$.
  - Enforce leverage bound: $\|\vec{w}_t\|_2 \le Q$ with $Q = 1$.
  - Operational normalization: $\tilde{s}_{i,t} = s_{i,t} - \frac{1}{N}\sum_{j=1}^N s_{j,t}$, with portfolio weights $w_{i,t} = \frac{\tilde{s}_{i,t}}{\max(\|\tilde{\mathbf{s}}_t\|_2, 1)}$ (`research-proposed normalization mapping details adhering to source constraints`).
- **Loss function formulations (source-reported):**
  - `LogMDDLoss`: $-\log(1 - \min_t DD_t)$ where $DD_t$ is running cumulative drawdown.
  - `ModSharpeAbsLoss`: $\mathbb{E}[|\alpha - r|] \frac{\mathbb{E}(pnl)}{\mathrm{Var}(pnl) + \varepsilon}$ with $\varepsilon = 10^{-8}$ (`research-proposed small epsilon constant for numerical stability`).
  - `RiskAdjLoss`: $-\mathbb{E}(pnl) + \lambda \times \text{DrawDown} + \gamma \times (\alpha - r)^2$ with $\lambda = 0.3, \gamma = 0.01$ (source-reported).
  - `BandTurnover`: $\text{TvrReg} = \lambda \cdot (\max(0, \text{tvr} - 1.0) + \max(0, 0.3 - \text{tvr}))$ with $\lambda = 1.0$ (source-reported).
- **Portfolio multi-alpha combination (source-reported):**
  - Input: 20 low-correlated multimodal alphas (capturing order book imbalance, trade-flow ratios, VWAP spreads, and reversal).
  - Architecture: LSTM generating combination weights $\vec{w}_{\mathrm{alpha}} \in \mathbb{R}^{20}$ (single-weight mode) or $W_{\mathrm{alpha}} \in \mathbb{R}^{20 \times M}$ (point-wise mode).

## Required data

- **Instruments:** 61 actively traded cryptocurrency pairs quoted against USDT on Binance (e.g., BTCUSDT, ETHUSDT, SOLUSDT).
- **Venue:** Binance centralized exchange (API historical spot data).
- **Market type:** Spot market (`source-reported evaluation universe`; requires porting rules for perpetual futures).
- **Timeframe:** Multi-frequency candle bars: 15-minute, 1-hour, and 1-day resolutions.
- **Fields:**
  - `open`, `high`, `low`, `close` prices.
  - `volume` (base asset volume).
  - `quote_volume` (quote asset volume in USDT).
  - `taker_buy_volume` (base asset taker buy volume).
  - `taker_buy_quote_volume` (quote asset taker buy volume).
  - `number_of_trades` (trade count).
- **Point-in-time requirements:** Features generated strictly on retrospective rolling windows without lookahead bias.
- **Universe selection & survivorship filter (source-reported):**
  - Assets listed on Binance no later than 2021 and continuously active through July 1, 2025 without delisting ($N = 61$).
  - Year 2021 intentionally excluded from training/testing due to extreme non-stationary volatility (median absolute annual price change transition of 432.42%).

## Execution assumptions

- **Rebalancing interval:** Daily frequency (medium-frequency strategy).
- **Order type:** Assumed execution within the sampling interval at daily candle boundary (`research-proposed execution model: market on open/close`).
- **Transaction fees & slippage:** NOT MODELED in the source backtests (`source-reported execution limitation`).
  - Authors explicitly state: *"In the current experimental setup, transaction costs and market impact are not explicitly modeled; consequently, strategies with aggressive trading activity benefit from amplified short-term gains without incurring execution penalties. In realistic market conditions, the inclusion of transaction costs would reduce the effective profitability of high-turnover strategies and lead to substantially lower Sharpe ratios."*
  - Binance VIP0 spot baseline fee: 10 bps (0.10%) taker, or 2–4 bps maker (`research-proposed fee benchmark`).
- **Shorting & borrow mechanics:** The model assumes frictionless short exposure in the market-neutral basket ($\mathbf{1}^\top \vec{w} = 0$). In spot crypto, shorting requires margin borrowing with daily borrow interest; in perpetual futures, shorting is native but incurs funding payments (`research-proposed operational caveat`).
- **Capital allocation & leverage:** Total gross exposure bounded by $Q = 1.0$ ($L_2$ norm).

## Evidence

### Source-reported

All metrics reported below are directly sourced from Kasymkhan Khubiyev, Mikhail Semenov, Irina Podlipnova, and Dinara Khubieva (arXiv:2509.04541v2, January 2026), evaluated over the out-of-sample test interval (historical data period January 1, 2022 to July 1, 2025 on $N = 61$ Binance spot pairs).

#### 1. Single-Alpha Performance Across Loss Objectives (Table 3 & Appendix Table B)

| Model & Strategy Objective | Portfolio Turnover | Max Drawdown | PnL (%) | Test Sharpe $\uparrow$ |
| :--- | :---: | :---: | :---: | :---: |
| **LinReg** (Linear Regression baseline)* | 1.43 | -0.0870 | +29.64% | 2.0963 |
| **LSTM LogMDDLoss** | 0.17 | **-0.0637** | +16.17% | **1.7573** |
| **LSTM MDDLoss** | 0.18 | -0.0671 | +15.87% | 1.6914 |
| **LSTM ModSharpeAbsLoss + ClassicalTvr** | **0.03** | -0.1453 | +18.72% | 1.5551 |
| **LSTM ModSharpeLoss** | 0.12 | -0.0670 | +15.28% | 1.5283 |
| **LSTM TurnoverLoss + ClassicalTvr** | 0.04 | -0.0405 | +13.42% | 1.4989 |
| **LSTM ModSharpeAbsLoss + BandTvr** | 0.04 | -0.1529 | +17.15% | 1.4711 |
| **LSTM SharpeLoss** | 0.10 | -0.1198 | +12.80% | 1.3628 |
| **MLP LogMDDLoss** | 0.24 | -0.0919 | +13.78% | 1.2882 |
| **LSTM ModSharpeAbsLoss** (no reg) | 0.05 | -0.0978 | +11.02% | 1.2745 |
| **LSTM MeanCVaRLoss + BandTurnover** | 0.24 | -0.0904 | +15.24% | 1.2579 |
| **Reversion** (Heuristic benchmark) | 0.12 | -0.1083 | +24.45% | 1.2418 |
| **LSTM SoftMDDLoss** | 0.17 | -0.0639 | +11.99% | 1.2158 |
| **XGBoost** (ML baseline) | 1.42 | -0.0985 | +25.93% | 0.7181 |
| **Mean Reversion** (Heuristic benchmark) | 0.76 | -0.2407 | +14.92% | 0.6480 |
| **Buy&Hold** (Passive market benchmark) | 0.04 | -0.9226 | +24.90% | 0.3072 |
| **LSTM MSELoss** (Standard regression) | 0.22 | -0.2004 | -6.03% | **-0.4564** |
| **MLP MSELoss** (Standard regression) | 0.59 | -0.1131 | -6.32% | **-0.5924** |
| **Random Forest** (ML baseline) | 0.94 | -0.1074 | -7.30% | **-0.7808** |

*\*Note on LinReg:* Authors explicitly note that while LinReg achieved a high Sharpe on the test subset, it exhibited extreme turnover (1.43) and severe drawdowns across the full historical horizon, indicating regime instability.

#### 2. Deep Learning Multi-Alpha Portfolio Optimization (Table 5)

Evaluated combining 20 low-correlated multimodal alphas (order-book imbalance, trade volume ratios, VWAP divergence):

| Portfolio Weighting Objective | Portfolio Turnover | Max Drawdown | PnL | Test Sharpe $\uparrow$ |
| :--- | :---: | :---: | :---: | :---: |
| **LogMaxDrawDownLoss + BandTurnover** | 1.0994 | **-0.0225** | 0.0666 | **7.6881** |
| **RiskAdjLoss** | 0.8362 | **-0.0190** | 0.0797 | 7.0307 |
| **ModSharpeAbsLoss** | 0.7929 | -0.0273 | 0.0938 | 6.3984 |
| **ModSharpeSquaredLoss** | 0.7638 | -0.0202 | 0.0781 | 6.3968 |
| **SharpeLoss + ClassicalTurnover** | 0.8272 | -0.0363 | 0.0970 | 6.3156 |
| **MSELoss + BandTurnover** | 0.8996 | -0.0231 | 0.0822 | 6.1370 |
| **SharpeLoss + BandTurnover** | 0.7614 | -0.0342 | 0.1227 | 6.0656 |
| **SoftMaxDrawDownLoss** | 0.8616 | -0.0276 | 0.0610 | 5.8556 |
| **SharpeLoss** | 0.7378 | -0.0460 | 0.1173 | 5.7360 |
| **MeanVarianceLoss** | 0.7372 | -0.0501 | 0.1116 | 5.3585 |
| **EntropicRiskLoss** | 0.7373 | -0.0501 | 0.1116 | 5.3564 |
| **PnLLoss** | 0.7373 | -0.0502 | 0.1115 | 5.3536 |
| **Equal Weighted Portfolio** (Baseline) | 1.2925 | -0.0797 | 0.0788 | 2.5947 |
| **MSELoss** (Decoupled regression weighting) | 0.9685 | -0.0921 | 0.0311 | 1.0249 |
| **ModSharpeLoss** (Sign-unstable version) | 0.6862 | -0.3403 | 0.0108 | -0.8621 |

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Failure of Classical Regression Losses:** Models trained with standard MSE loss (LSTM, MLP, Random Forest) systematically failed across economic dimensions, posting negative Sharpe ratios ($-0.45$ to $-0.78$) and negative net PnL ($-6.0\%$ to $-7.3\%$) despite achieving lower pointwise MSE.
2. **Sign Instability in Raw ModSharpeLoss:** In multi-alpha portfolio weighting, the unconstrained `ModSharpeLoss` without absolute-value or squared regularizers experienced sign reversal when $\mathbb{E}[\alpha - r] < 0$, collapsing to a Sharpe of $-0.8621$ and a $-34.03\%$ maximum drawdown.
3. **Turnover Collapse under Classical Regularization:** Classical linear turnover penalties ($\lambda \cdot \text{tvr}$) monotonically discouraged trading, driving turnover down to $0.03$ and suppressing responsiveness to transient market opportunities.
4. **Friction Sensitivity:** High Sharpe ratios (>7.0) reported in multi-alpha portfolio weighting reflect zero-fee, zero-slippage assumptions. At daily turnovers near 1.0–1.1, round-trip fees of 10 bps per day would erode ~25–35% annual performance, significantly degrading the unhedged edge.

## Falsification plan

1. **Transaction Cost & Slippage Stress Test:**
   - *Test:* Inject explicit taker fee schedules (5 bps, 10 bps, 15 bps per trade) and linear market impact ($0.5 \times \text{spread}$).
   - *Failure condition (`research-defined falsification threshold`):* If net annualized Sharpe ratio drops below $0.50$ or annualized return turns negative under a 10 bps fee schedule, the strategy edge is falsified as transaction-friction drag.
2. **Out-of-Sample Walk-Forward Stability:**
   - *Test:* Retrain on January 2022 – December 2024 and evaluate out-of-sample on January 2025 – September 2026.
   - *Failure condition (`research-defined falsification threshold`):* If out-of-sample Sharpe ratio drops below $0.30$ or maximum drawdown exceeds $20\%$, reject the hypothesis of stationary risk-adjusted learning.
3. **Placebo / Label Permutation Test:**
   - *Test:* Train identical LSTM models with `LogMDDLoss` on cross-sectionally shuffled return targets $\tilde{r}_i(t) = \pi(r_i(t))$.
   - *Failure condition (`research-defined falsification threshold`):* If the shuffled model produces an in-sample Sharpe ratio $> 0.50$, the loss function is falsified as capturing spurious statistical artifacts rather than true cross-sectional predictability.
4. **Survivorship Bias Audit:**
   - *Test:* Re-evaluate the strategy on a point-in-time Binance universe that includes tokens that were delisted, liquidated, or collapsed (e.g., LUNA, FTT) between 2022 and 2025.
   - *Failure condition (`research-defined falsification threshold`):* If inclusion of historical delistings increases maximum drawdown beyond $30\%$ or renders cumulative PnL negative, the reported results are falsified as survivorship selection bias.

## Crypto portability

- **Portability status:** `adapted` (source demonstrates empirical testing on Binance crypto spot pairs, but deployment to crypto perpetual contracts requires unproven adaptation).
- **Spot to Perpetual Futures Dynamics:**
  - The primary study evaluated spot pairs without funding rate payments. In perpetual futures, maintaining short positions in an $L_2$ market-neutral basket entails receiving or paying 8-hour funding rates. In bull regimes, negative basis and high positive funding rates can substantially alter long/short net carry.
  - Perpetual execution requires collateral margin management, liquidation buffer monitoring, and funding rate arbitrage hedging.
- **Session Continuity (24/7 Market):**
  - Unlike equity markets with discrete overnight closes, crypto operates continuously. The choice of daily cutoff (e.g., 00:00 UTC) introduces arbitrary candle boundary effects. Multi-frequency features (15m, 1h) partially mitigate this, but execution latency around 00:00 UTC funding events requires careful timestamp synchronization.
- **Liquidity & Microstructure Fragmentation:**
  - Liquidating 61 assets simultaneously at a daily rebalancing point requires adequate depth across lower-cap constituents. In illiquid tokens, market-order execution could induce severe slippage exceeding the model's gross margin.

## Limitations

- **Omission of Transaction Costs:** Third-party backtests report gross returns without fees, borrow interest, or market impact. This is the single largest caveat in the cited paper.
- **Survivorship Bias:** Asset universe was filtered to tokens listed before 2022 that remained continuously traded through July 2025, filtering out failed or delisted projects.
- **Underspecified Train/Validation/Test Split Dates in Text:** While the overall period is specified as Jan 1, 2022 – Jul 1, 2025 and code is available on Kaggle, the exact calendar dates for the test interval are not explicitly declared in the paper text (`provenance gap`).
- **Scale-Invariance Sensitivity:** Requires careful implementation of `ModSharpeAbsLoss` or `LogMDDLoss`; unregularized Sharpe objectives risk pathological position scaling.

## Implementation status

- `not-implemented`: No implementation or execution has been conducted in our research stack (`nautilus-quant-system` or PyBroker).
- Source authors have published reference PyTorch code and Jupyter notebooks on Kaggle ([https://www.kaggle.com/code/kkhubiev/finance-grounded-loss-functions](https://www.kaggle.com/code/kkhubiev/finance-grounded-loss-functions)).

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Research capture does not constitute approval for paper trading, testnet deployment, or live trading. Any future implementation requires independent backtesting with realistic fee modeling, liquidity filters, and walk-forward verification.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/strategy-research-record-spec-v1]]`
- `smart-predict-then-optimize-spo-plus-robust-portfolio-2026-09-05.md`
- `alphazerobeta-recurrent-ppo-market-neutral-portfolio-2026-09-02.md`
- `decision-focused-sparse-tangent-portfolio-dpp-topk-2026-09-03.md`

## Sources

1. Kasymkhan Khubiyev, Mikhail Semenov, Irina Podlipnova, and Dinara Khubieva. *"Finance-Grounded Optimization For Algorithmic Trading"*. arXiv preprint `arXiv:2509.04541v2 [cs.LG, q-fin.ST]`, submitted September 4, 2025, revised January 31, 2026. DOI: [10.48550/arXiv.2509.04541](https://doi.org/10.48550/arXiv.2509.04541). Stable URL: [https://arxiv.org/abs/2509.04541](https://arxiv.org/abs/2509.04541). Full text: [https://arxiv.org/html/2509.04541v2](https://arxiv.org/html/2509.04541v2).
2. Kasymkhan Khubiyev. *"Cryptotrading Dataset"*. Kaggle Datasets (2025/2026). Stable URL: [https://www.kaggle.com/datasets/kkhubiev/cryptotrading](https://www.kaggle.com/datasets/kkhubiev/cryptotrading).
3. Kasymkhan Khubiyev. *"Finance-Grounded Loss Functions"*. Kaggle Code Notebook (2025/2026). Stable URL: [https://www.kaggle.com/code/kkhubiev/finance-grounded-loss-functions](https://www.kaggle.com/code/kkhubiev/finance-grounded-loss-functions).
