---
schema: strategy-research-record-v1
title: "Smart Predict-then-Optimize (SPO+) Portfolio Allocation: Decision-Focused Learning under Turnover Costs, Weight Regularization, and Multiplicative Perturbation Uncertainty"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - decision-focused-learning
  - smart-predict-then-optimize
  - spo-plus
  - robust-optimization
  - transaction-costs
  - turnover-control
  - etf-allocation
  - walk-forward-optimization
  - pyepo
status: research-only
confidence: high
source_as_of: 2026-01-12
sources:
  - "arXiv:2601.04062v3 [q-fin.PM], 12 January 2026. https://arxiv.org/abs/2601.04062"
  - "https://doi.org/10.48550/arXiv.2601.04062"
  - "https://arxiv.org/html/2601.04062v3"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Smart Predict-then-Optimize (SPO+) Portfolio Allocation: Decision-Focused Learning under Turnover Costs, Weight Regularization, and Multiplicative Perturbation Uncertainty

## Provenance

- **Primary Source:** Wang Yi and Takashi Hasuike (Department of Industrial and Management Systems Engineering, School of Creative Science and Engineering, Waseda University, Tokyo, Japan), *"Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets"*, arXiv preprint `arXiv:2601.04062v3 [q-fin.PM]`, submitted 7 January 2026, revised 12 January 2026.
- **Canonical DOI:** [10.48550/arXiv.2601.04062](https://doi.org/10.48550/arXiv.2601.04062)
- **Canonical Web Abstract:** [https://arxiv.org/abs/2601.04062](https://arxiv.org/abs/2601.04062)
- **Canonical HTML Full Text:** [https://arxiv.org/html/2601.04062v3](https://arxiv.org/html/2601.04062v3)
- **Implementation Framework:** The authors implement the SPO+ surrogate loss via PyEPO (Tang & Khalil 2024, *Mathematical Programming Computation* 16:297–335) with PyTorch and Optuna for walk-forward time-series hyperparameter validation.
- **Source-Identity Deduplication:** Repository-wide grep audit confirms zero matching records for `2601.04062`, `Wang Yi`, `Takashi Hasuike`, `Smart Predict-then-Optimize`, or `SPO+`. Distinct from existing portfolio optimization records in this repository:
  - `decision-focused-sparse-tangent-portfolio-dpp-topk-2026-09-03.md` (Jeon et al. 2026, arXiv:2607.00581) evaluates cardinality-constrained $k$-sparse Sharpe tangency portfolios via Disciplined Parametrized Programming (DPP) QCQP layers and smooth top-$k$ selection on S&P 500 equities.
  - In contrast, Wang & Hasuike (2026) investigate the Smart Predict-then-Optimize (SPO+) surrogate loss bounding decision regret (Elmachtoub & Grigas 2022) with linear predictors on U.S. ETFs (2015–2025), incorporating proportional turnover transaction penalties ($\gamma = 0.005$), $\ell_2$ portfolio weight regularization ($\lambda = 0.42$), and worst-case regret over multiplicative uncertainty box sets ($\rho \in \{0.01, 0.1\}$).

## Economic mechanism

### Source-reported

In classical quantitative portfolio management, machine learning models and optimization algorithms are traditionally decoupled into a two-stage "Predict-then-Optimize" (PtO) pipeline:
1. A statistical forecaster (e.g., linear regression, tree, or neural network) is trained to minimize pointwise prediction error (such as Mean Squared Error, MSE: $\min_\theta \|\hat{\bm{r}} - \bm{r}\|_2^2$).
2. The point estimates $\hat{\bm{r}}$ are passed as fixed parameters into an external optimizer (e.g., Markowitz mean-variance or Sharpe ratio maximization) subject to budget and trading constraints.

The authors demonstrate that this decoupled approach suffers from a fundamental structural misalignment between the statistical training loss and downstream portfolio decision quality:
- Financial asset returns are characterized by extremely low signal-to-noise ratios, weak periodicity, and frequent non-stationary regime shifts.
- Under realistic constraints (e.g., long-only budget simplex $\mathcal{W}$) and trading frictions (proportional turnover costs $\gamma \|\bm{w} - \bm{w}_{t-1}\|_1$), small prediction errors on borderline assets can induce large, abrupt shifts in optimal portfolio weights $\hat{\bm{w}}$.
- Consequently, minimizing MSE across all assets equally penalizes errors on assets that are irrelevant to the allocation decision while failing to penalize errors that trigger catastrophic rebalancing into losing positions.

To resolve this objective mismatch, the authors adopt the Smart Predict-then-Optimize (SPO) paradigm (Elmachtoub & Grigas 2022). SPO embeds the downstream portfolio optimization problem directly into the training loss function via the SPO+ surrogate loss:
$$\mathcal{L}_{\mathrm{SPO+}}(\hat{\bm{r}}, \bm{r}) = \max_{\bm{w} \in \mathcal{W}} (2\hat{\bm{r}} - \bm{r})^\top \bm{w} - \bm{r}^\top \bm{w}^\star$$
where $\bm{w}^\star = \arg\max_{\bm{w} \in \mathcal{W}} \bm{r}^\top \bm{w}$ denotes the full-information oracle allocation under realized returns $\bm{r}$. The SPO+ loss provides a tractable, convex upper bound on true decision regret:
$$\mathrm{Regret}(\hat{\bm{w}}, \bm{r}) = \bm{r}^\top \bm{w}^\star - \bm{r}^\top \hat{\bm{w}}$$

The authors extend this framework along three realistic market dimensions:
1. **Transaction Cost Penalty:** Incorporating turnover friction directly into the portfolio value function:
   $$\hat{\bm{w}} = \arg\max_{\bm{w} \in \mathcal{W}} \left( \hat{\bm{r}}^\top \bm{w} - \gamma \|\bm{w} - \bm{w}_{t-1}\|_1 \right)$$
   where $\gamma > 0$ controls fee intensity. By Danskin's theorem, subgradients with respect to predicted returns are evaluated at the active portfolio decision.
2. **$\ell_2$ Weight Regularization:** Adding an $\ell_2$ shrinkage penalty $-\lambda \|\bm{w}\|_2^2$ ($\lambda > 0$) to discourage extreme single-asset concentration and promote diversification, while maintaining affine parameter dependence for SPO+ gradient propagation.
3. **RobustSPO under Multiplicative Perturbations:** Acknowledging that point return estimates remain uncertain, the authors define an uncertainty set:
   $$\mathcal{U} = \left\{ \bm{\zeta} \in \mathbb{R}^n : \|\bm{\zeta}\|_\infty \le \rho \right\}$$
   where perturbed predictions $\tilde{\bm{r}} = \hat{\bm{r}} \circ (1 + \bm{\zeta})$ yield worst-case regret:
   $$\min_\theta \max_{\bm{\zeta} \in \mathcal{U}} \left( \bm{r}^\top \bm{w}^\star - \bm{r}^\top \tilde{\bm{w}} \right)$$
   solved during mini-batch training via Monte Carlo scenario sampling of worst-case perturbation bounds.

### Research interpretation

The core economic mechanism is the geometric alignment of model parameter updates with the active faces of the portfolio decision simplex. When an asset's expected return places it far from the portfolio boundary, prediction errors on that asset have zero marginal economic cost. Decoupled PtO models waste model capacity fitting irrelevant assets, whereas SPO+ concentrates gradient descent exclusively on assets that cross allocation thresholds.

Furthermore, integrating turnover penalties ($\gamma \|\bm{w} - \bm{w}_{t-1}\|_1$) directly into the training loop teaches the predictor to output return differentials that exceed the round-trip transaction hurdle before triggering rebalancing. During severe market stress (such as the March 2020 COVID-19 crash), unconstrained Markowitz models chase transient return signals into falling knives, incurring devastating turnover drag and capital erosion. SPO+ with fees and RobustSPO establish an endogenous inertia band, preserving capital and limiting maximum drawdowns below 10% when standard baselines experience >30% drawdowns.

Component structure of the strategy:
- **Predictor component:** Transparent linear mapping $f_\theta(\bm{x}) = \hat{\bm{r}}$ ensuring Occam's razor and avoiding deep overfitting.
- **Optimization layer:** Parameterized linear/quadratic programming solver determining portfolio weights $\hat{\bm{w}} \in \mathcal{W}$.
- **Decision loss:** SPO+ convex surrogate regret bound propagating decision-aware gradients back into predictor weights $\theta$.
- **Friction filter:** $\ell_1$ turnover penalty $\gamma \|\bm{w} - \bm{w}_{t-1}\|_1$ ($\gamma = 0.005$, source-reported).
- **Diversification filter:** $\ell_2$ weight regularization $\lambda \|\bm{w}\|_2^2$ ($\lambda = 0.42$, source-reported).
- **Adversarial robustness filter:** Multiplicative perturbation radius $\rho \in \{0.01, 0.1\}$ hedging against non-stationary regime shocks.

## Signal

- **Formation timestamp:** Month-end close $t$. Tradable at the opening of month $t+1$ (`research-proposed execution timestamp convention`; source specifies monthly rebalancing and holding over out-of-sample period $[t, t+1]$).
- **Lookback and rolling structure (source-reported):**
  - Training window: Past 12 months $[t-12, t-3]$ (9 months of effective training data).
  - Validation window: Time-ordered 3 months $[t-3, t]$ for hyperparameter tuning via Optuna.
  - Out-of-sample evaluation: 1 month $[t, t+1]$ until next monthly rebalancing date.
  - Rolling cadence: Window rolls forward by 1 month at each rebalancing step; model retrained from scratch each month.
- **Feature construction (source-reported):**
  Derived from daily historical price and volume data for each ETF:
  1. *Log returns:* Short-term price momentum and return rate.
  2. *Simple Moving Averages (SMA) and Price Bias:* $(P_t - \mathrm{SMA}_k) / \mathrm{SMA}_k$ capturing trend persistence and mean reversion.
  3. *Relative Strength Index (RSI) and MACD differences:* Oscillator momentum and trend divergence.
  4. *Bollinger Band Width:* $(U_t - L_t) / \mathrm{SMA}_t$ measuring volatility expansion/contraction.
  5. *Volume-based indicators:* Volume moving average ratios reflecting market participation.
  *(Exact window lengths for SMA, RSI, and MACD are not published in paper text; marked as source-underspecified; standard default parameters $k \in \{20, 50, 200\}$, RSI 14-day, MACD 12/26/9 are `research-proposed`).*
- **Predictor model (source-reported):**
  Linear model $f_\theta(\bm{x}) = \bm{W} \bm{x} + \bm{b}$, generating estimated return vector $\hat{\bm{r}} \in \mathbb{R}^n$.
- **Portfolio optimization formulations (source-reported):**
  1. *SPO+ MaxReturn:*
     $$\hat{\bm{w}} = \arg\max_{\bm{w} \in \mathcal{W}} \hat{\bm{r}}^\top \bm{w}$$
     Trained via PyEPO minimizing $\mathcal{L}_{\mathrm{SPO+}}(\hat{\bm{r}}, \bm{r})$.
  2. *SPO+ with Transaction Costs:*
     $$\hat{\bm{w}} = \arg\max_{\bm{w} \in \mathcal{W}} \left( \hat{\bm{r}}^\top \bm{w} - \gamma \|\bm{w} - \bm{w}_{t-1}\|_1 \right), \quad \gamma = 0.005$$
  3. *SPO+ with Transaction Costs and $\ell_2$ Regularization:*
     $$\hat{\bm{w}} = \arg\max_{\bm{w} \in \mathcal{W}} \left( \hat{\bm{r}}^\top \bm{w} - \gamma \|\bm{w} - \bm{w}_{t-1}\|_1 - \lambda \|\bm{w}\|_2^2 \right), \quad \gamma = 0.005, \lambda = 0.42$$
  4. *RobustSPO:*
     Worst-case regret over $\mathcal{U} = \{\bm{\zeta} : \|\bm{\zeta}\|_\infty \le \rho\}$ ($\rho \in \{0.01, 0.1\}$), trained via Monte Carlo mini-batch sampling of worst-case perturbation scenarios.
- **Feasible portfolio set (source-reported):**
  Long-only standard simplex:
  $$\mathcal{W} = \left\{ \bm{w} \in \mathbb{R}^n : \sum_{i=1}^n w_i = 1, \quad w_i \ge 0 \right\}$$
- **Hyperparameter search space (source-reported Table 1):**
  - Optimizer: Adam.
  - Batch size: 63.
  - Training epochs: Selected from range $[20, 40]$ via Optuna time-series validation.
  - Learning rate: Selected from range $[10^{-4}, 5 \times 10^{-2}]$ (log-uniform distribution) via Optuna.
  - Transaction cost parameter: Fixed $\gamma = 0.005$.
  - Regularization parameter: Fixed $\lambda = 0.42$.
  - Robustness radius: Evaluated at $\rho \in \{0.01, 0.1\}$.
- **Holding period:** Exactly 1 month between monthly rebalance dates (source-reported).
- **Position-sizing logic:** Continuous weights $w_i \in [0, 1]$ directly output by the convex/linear programming solver (source-reported).

## Required data

- **Instrument:** Tradable U.S. Exchange-Traded Funds (ETFs) (source-reported).
- **Universe definition:** Daily historical data of U.S. ETFs from 2015-01-01 to 2025-01-01 (source-reported).
  *(Provenance gap: The primary source does not enumerate the exact constituent ETF tickers in the paper text. A representative 10-to-15 liquid U.S. ETF multi-asset universe—e.g., SPY, QQQ, IWM, EEM, EFA, XLF, XLK, XLE, XLV, TLT, IEF, GLD, DBC—is `research-proposed` for replication).*
- **Venue:** U.S. equity exchanges (NYSE / NASDAQ) (source-reported).
- **Market type:** Spot cash equity ETFs (source-reported).
- **Timeframe:** Daily OHLCV bars (source-reported).
- **Required fields:** Open, High, Low, Close, Volume (source-reported).
- **Point-in-time rules:** Strictly rolling window walk-forward. At month $t$, training uses only $[t-12, t-3]$ and validation uses $[t-3, t]$; zero look-ahead into $[t, t+1]$ (source-reported).
- **Missing data handling:** `research-proposed`: Forward-fill suspended or holiday bars; assets with missing data over the 12-month lookback window excluded from that month's optimization universe.

## Execution assumptions

- **Execution timing:** Portfolio rebalanced monthly. Orders assumed placed at Month-Open on the first trading day following month-end signal generation (`research-proposed execution convention`).
- **Order type:** Market / Market-On-Open (MOO) order (`research-proposed`).
- **Fill model:** Complete fill at official open price (`research-proposed`).
- **Transaction costs:** Proportional turnover fee of $\gamma = 0.005$ (50 basis points) deducted from portfolio wealth on each rebalancing trade: $\mathrm{Cost}_t = 0.005 \times \|\bm{w}_t - \bm{w}_{t-1}\|_1$ (source-reported).
- **Slippage and market impact:** Omitted in primary source beyond the 50 bps linear turnover fee; linear impact assumption is a source limitation.
- **Shorting / Borrow:** No short positions permitted; $w_i \ge 0$ strictly enforced (source-reported).
- **Leverage:** Exactly 1.0x gross leverage ($\sum w_i = 1$) (source-reported).
- **Execution failure handling:** `research-proposed`: In case of unexecutable ETF halts, reallocate target weights proportionally among remaining active constituents.

## Evidence

### Source-reported

All empirical results below are directly extracted from Section 5 and Tables 3, 4, and 5 of Wang & Hasuike (2026), arXiv:2601.04062v3. Sample period covers 10 years of rolling monthly backtests from 2015-01-01 to 2025-01-01 under 50 bps proportional transaction costs.

#### 1. Overall Backtest Performance (2015–2025, Table 3)
| Strategy | Annualized Return (%) | Annualized Volatility (%) | Sharpe Ratio | Sortino Ratio | Maximum Drawdown (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **SPO+ (Unconstrained MaxReturn)** | **14.05** | 19.09 | **0.785** | **0.728** | -28.71 |
| **SPO+ with Fee ($\gamma = 0.005$)** | 10.54 | 15.75 | 0.715 | 0.699 | -28.51 |
| **RobustSPO ($\rho = 0.01$)** | 9.67 | 15.09 | 0.688 | 0.660 | **-27.79** |
| **PtO Markowitz Baseline** | 9.00 | 14.76 | 0.659 | 0.624 | -30.22 |
| **RobustSPO ($\rho = 0.1$)** | 8.09 | 14.96 | 0.595 | 0.582 | -29.64 |
| **SPO+ with Fee & $\ell_2$ ($\gamma = 0.005, \lambda = 0.42$)** | 7.69 | 15.74 | 0.550 | 0.512 | -30.18 |
| **MaxSharpe Baseline** | 7.13 | 13.63 | 0.574 | 0.514 | -26.33 |
| **Softmax-MaxReturn** | 4.11 | 13.75 | 0.362 | 0.331 | -32.20 |
| **Softmax-MaxSharpe** | 1.32 | 13.02 | 0.166 | 0.152 | -38.37 |

*Findings:* Decision-focused SPO+ achieves the highest annualized return (14.05%) and highest Sharpe (0.785), outperforming the standard decoupled PtO Markowitz model (9.00% return, 0.659 Sharpe).

#### 2. Performance during COVID-19 Market Crisis (Jan 2020 – Dec 2020, Table 4)
| Strategy | Annualized Return (%) | Annualized Volatility (%) | Sharpe Ratio | Sortino Ratio | Maximum Drawdown (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **RobustSPO ($\rho = 0.1$)** | **46.92** | 18.61 | **2.170** | **2.322** | **-9.58** |
| **SPO+ with Fee ($\gamma = 0.005$)** | **46.92** | 18.61 | **2.170** | **2.322** | **-9.58** |
| **SPO+ (Unconstrained)** | 35.48 | 31.49 | 1.128 | 0.956 | -27.80 |
| **PtO Markowitz Baseline** | 20.63 | 28.98 | 0.796 | 0.693 | -30.22 |
| **RobustSPO ($\rho = 0.01$)** | 17.81 | 14.87 | 1.182 | 0.999 | -10.71 |
| **MaxSharpe Baseline** | 12.42 | 10.44 | 1.179 | 0.965 | -10.00 |
| **SPO+ with Fee & $\ell_2$** | -3.51 | 22.50 | -0.046 | -0.037 | -28.93 |
| **Softmax-MaxSharpe** | -4.72 | 16.51 | -0.210 | -0.161 | -26.65 |
| **Softmax-MaxReturn** | -6.73 | 18.21 | -0.292 | -0.222 | -30.37 |

*Findings:* During the March 2020 liquidity shock, RobustSPO ($\rho = 0.1$) and SPO+ with Fee restricted maximum drawdowns to -9.58% while capturing 46.92% annualized return (Sharpe 2.170), compared to a -30.22% drawdown for PtO Markowitz.

#### 3. Performance during 2024 Bull Market (Jan 2024 – Dec 2024, Table 5)
| Strategy | Annualized Return (%) | Annualized Volatility (%) | Sharpe Ratio | Sortino Ratio | Maximum Drawdown (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **SPO+ (Unconstrained)** | **35.96** | 15.09 | **2.120** | **2.167** | -6.31 |
| **MaxSharpe Baseline** | 22.26 | 11.64 | 1.793 | 1.870 | -7.18 |
| **PtO Markowitz Baseline** | 15.07 | 8.51 | 1.699 | 1.716 | **-5.47** |
| **SPO+ with Fee & $\ell_2$** | 14.89 | 12.72 | 1.160 | 1.092 | -8.83 |
| **Softmax-MaxReturn** | 10.66 | 11.91 | 0.914 | 0.845 | -7.19 |
| **RobustSPO ($\rho = 0.01$)** | 9.99 | 9.90 | 1.015 | 0.969 | -5.94 |
| **RobustSPO ($\rho = 0.1$)** | 9.38 | 10.59 | 0.903 | 0.856 | -5.99 |
| **Softmax-MaxSharpe** | 8.79 | 12.09 | 0.760 | 0.713 | -7.02 |
| **SPO+ with Fee ($\gamma = 0.005$)** | 7.71 | 10.79 | 0.745 | 0.719 | -5.94 |

*Findings:* In strong bull markets, unconstrained SPO+ captures momentum rapidly (35.96% return, 2.120 Sharpe), whereas models with strict turnover fees (7.71%) or robustness sets (9.38%) exhibit drag due to conservative rebalancing inertia.

### Independently reproduced

Not independently reproduced. (Scout research capture; empirical results reflect third-party author claims in arXiv:2601.04062v3).

### Negative evidence

1. **Catastrophic Failure of Softmax Direct Differentiable Allocators:** SoftmaxDFL models mapping features directly to portfolio weights via softmax layers failed across all metrics, producing overall Sharpe ratios of 0.362 (MaxReturn) and 0.166 (MaxSharpe), and posting negative returns during COVID-19 (-6.73% and -4.72%). Without the structural regularizing geometry of convex optimization, unconstrained neural allocators severely overfit noise.
2. **$\ell_2$ Weight Regularization Degradation:** Enforcing $\ell_2$ shrinkage ($\lambda = 0.42$) consistently degraded performance: overall Sharpe dropped from 0.785 to 0.550, and during the 2020 crisis, returns fell to -3.51% (Sharpe -0.046) with a -28.93% drawdown. The authors acknowledge that artificial dispersion forces allocation into structurally declining assets, destroying performance during market bifurcations.
3. **Turnover Penalty Drag in Upward Regimes:** During sustained bull markets (2024), SPO+ with Fee underperformed PtO Markowitz by -7.36% in return and -0.95 in Sharpe (7.71% vs. 15.07%), demonstrating that turnover penalties create costly inertia when underlying market leadership trends persistently.

## Falsification plan

To disconfirm the validity of the Smart Predict-then-Optimize portfolio allocation framework:

- **Test 1: Standardized ETF Universe Robustness and Benchmark Parity.**
  - *Data & Universe:* Replicate across two distinct, standardized public ETF universes over 2010–2026: (a) 11 Select Sector SPDR ETFs (XLE, XLF, XLK, XLV, XLI, XLP, XLY, XLU, XLB, XLRE, XLC); (b) 10 Multi-Asset Global ETFs (SPY, QQQ, IWM, EFA, EEM, TLT, IEF, LQD, GLD, DBC).
  - *Metric:* Net out-of-sample Sharpe ratio after 50 bps turnover cost.
  - *Decision Rule:* `research-defined falsification threshold`: If SPO+ fails to outperform the PtO Markowitz baseline by at least +0.08 Sharpe ratio on both universes across the full sample, reject the claim that decision-focused surrogate loss provides generalizable superiority over decoupled prediction.
- **Test 2: Friction Stress Testing and Rebalancing Hurdle.**
  - *Setup:* Step turnover transaction cost parameter $\gamma$ from 10 bps to 100 bps in 10 bps increments.
  - *Metric:* Annualized turnover rate and net Sharpe ratio.
  - *Decision Rule:* `research-defined falsification threshold`: If the net Sharpe ratio of SPO+ with fee falls below 0.30 at $\gamma \ge 25\text{ bps}$, or if average monthly turnover exceeds 60%, classify the edge as an artifact of unrealistic liquidity and execution assumptions.
- **Test 3: Synthetic Feature Permutation (Placebo Test).**
  - *Setup:* Replace the historical technical features (SMA, RSI, MACD, Bollinger Band Width, Volume) with phase-randomized surrogate time series while preserving marginal distributions and cross-sectional correlations.
  - *Metric:* In-sample training loss convergence and out-of-sample decision regret.
  - *Decision Rule:* `research-defined falsification threshold`: If the placebo-trained model achieves an out-of-sample Sharpe ratio within 85% of the real-feature model, reject the hypothesis that the technical indicator feature set contains predictive economic content.
- **Test 4: Crisis Regime Replicability Audit.**
  - *Setup:* Evaluate RobustSPO ($\rho = 0.1$) on isolated out-of-sample crisis regimes (e.g., 2008 Global Financial Crisis if data permits, or 2022 Fed rate hiking drawdown).
  - *Metric:* Maximum Drawdown during market correction.
  - *Decision Rule:* `research-defined falsification threshold`: If RobustSPO suffers a drawdown exceeding -20% during a recognized equity bear market (e.g., 2022 drawdown where SPY fell >20%), reject the claim of guaranteed crisis downside containment below 10%.

## Crypto portability

- **Portability Classification:** `adapted` and `unproven`. (The primary source evaluates only U.S. cash equity ETFs; applicability to cryptocurrency markets is an unproven research interpretation).
- **Crypto-Specific Frictions and Risks:**
  - *24/7 Continuous Trading & Candle Boundaries:* Unlike U.S. ETFs with daily closing auctions at 16:00 EST, crypto markets trade continuously. Monthly rebalancing based on UTC midnight boundaries may introduce severe path dependency and execution slippage during illiquid weekend hours.
  - *Perpetual Funding Rate Drag:* Applying SPO+ to crypto perpetual futures requires incorporating continuous 8-hour funding rates into the objective function. Long-only allocations in high-funding regimes will suffer structural cash drag not present in ETF cash equities.
  - *Perturbation Uncertainty Scaling:* The author-tested uncertainty radii ($\rho = 0.01$ and $\rho = 0.10$, representing 1% to 10% relative error) are calibrated for low-volatility equity ETFs. In crypto markets where monthly asset volatility routinely reaches 40%–100%, a 1%–10% perturbation set is economically negligible. A crypto adaptation would require `research-proposed` volatility-scaled uncertainty sets ($\rho_i = c \cdot \sigma_i$).
  - *Symmetric Long/Short Capacity:* In crypto perpetuals, shorting is frictionless and symmetric ($w_i \in [-1, 1]$). Expanding the feasible set $\mathcal{W}$ from the standard simplex to a net-zero or gross-leverage bounded set changes the subgradient geometry of the SPO+ loss layer, requiring customized solver constraints.

## Limitations

- **Source Underspecification of ETF Universe:** The primary source does not report the exact constituent list of ETF tickers used in the 2015–2025 backtest, limiting exact byte-for-byte empirical reproducibility.
- **Model Family Restriction:** Only linear predictors $f_\theta(\bm{x}) = \bm{W}\bm{x} + \bm{b}$ are evaluated within the SPO framework; non-linear feature interactions and deep temporal architectures (e.g., TCN, Transformers) were not combined with SPO+ due to optimization tractability constraints.
- **Simplified Friction Model:** Transaction costs are modeled as a constant linear proportion ($\gamma = 0.005$); non-linear price impact, bid-ask spread variations, and borrow fees are omitted.
- **Low-Frequency Monthly Horizon:** The strategy rebalances only once per month. It cannot exploit high-frequency microstructure mispricings or intraday volatility bursts.
- **No Independent Reproduction:** Findings are based entirely on preprint data from Wang & Hasuike (2026); no independent live or backtested replication has been completed in our research environment.

## Implementation status

- `not-implemented`.
- This research record represents an external knowledge capture only. No code has been implemented in PyBroker, NautilusTrader, or our execution infrastructure.

## Adoption boundary

- `research-only`.
- `adoption: not-approved`.
- `approval_scope: research-only`.
- Capture of this research record does not imply strategy adoption, validation, or permission for paper trading, testnet execution, or live deployment. Any future progression requires formal pipeline review and independent empirical testing within `nautilus-quant-system`.

## Related Wiki records

- [[decision-focused-sparse-tangent-portfolio-dpp-topk-2026-09-03]] — Decision-focused learning for cardinality-constrained Sharpe ratio optimization using DPP QCQP layers.
- [[forecasted-tangency-minimum-euclidean-distance-portfolio-2026-09-04]] — Forecasted tangency portfolio geometry with distance shrinkage.
- [[two-stage-adaptive-shrinkage-golden-criterion-equity-premium-2026-09-02]] — Two-stage adaptive shrinkage for equity risk premium forecasting.
- [[observable-matrix-dynamics-portfolio-optimization-2026-09-02]] — Covariance-free portfolio optimization based on observable transition dynamics.
- [[dynamic-portfolio-optimization-cvar-stochastic-control-hjb-2026-09-02]] — Continuous-time dynamic portfolio optimization under CVaR constraints.

## Sources

- **Primary Source:** Wang Yi and Takashi Hasuike, *"Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets"*, arXiv preprint `arXiv:2601.04062v3 [q-fin.PM]`, 12 January 2026.
  - Abstract: [https://arxiv.org/abs/2601.04062](https://arxiv.org/abs/2601.04062)
  - DOI: [https://doi.org/10.48550/arXiv.2601.04062](https://doi.org/10.48550/arXiv.2601.04062)
  - Full Text HTML: [https://arxiv.org/html/2601.04062v3](https://arxiv.org/html/2601.04062v3)
- **Methodological Foundations:**
  - Elmachtoub, A. N., and Grigas, P. (2022). *"Smart 'Predict, then Optimize'"*. *Management Science*, 68(1), 9–26. DOI: [10.1287/mnsc.2020.3922](https://doi.org/10.1287/mnsc.2020.3922).
  - Tang, B., and Khalil, E. B. (2024). *"PyEPO: A PyTorch-based end-to-end predict-then-optimize library for linear and integer programming"*. *Mathematical Programming Computation*, 16, 297–335. DOI: [10.1007/s12532-024-00255-x](https://doi.org/10.1007/s12532-024-00255-x).
  - Schutte, N., Postek, K., and Yorke-Smith, N. (2024). *"Robust losses for decision-focused learning"*. In *Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence (IJCAI-24)*, pp. 4868–4875. DOI: [10.24963/ijcai.2024/538](https://doi.org/10.24963/ijcai.2024/538).
