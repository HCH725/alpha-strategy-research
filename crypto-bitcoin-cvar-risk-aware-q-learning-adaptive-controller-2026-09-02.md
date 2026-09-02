---
schema: strategy-research-record-v1
title: "Bitcoin CVaR Risk-Aware Q-Learning (RaQL) with Adaptive Finite-Budget Training Controller"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reinforcement-learning
  - cvar
  - risk-aware-q-learning
  - bitcoin
  - adaptive-controller
  - finite-budget
  - market-sentiment
status: research-only
confidence: medium
source_as_of: 2026-08-04
sources:
  - "Yifan Wu, Junjie Lei, and Wenjie Huang, 'Adaptive Finite-Budget Training for CVaR Risk-Aware Q-Learning', arXiv preprint arXiv:2608.04305v1 [q-fin.RM, cs.LG], submitted August 4, 2026. Stable URL: https://arxiv.org/abs/2608.04305. Full text HTML: https://arxiv.org/html/2608.04305v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin CVaR Risk-Aware Q-Learning (RaQL) with Adaptive Finite-Budget Training Controller

## Provenance

- **Primary Source:** Yifan Wu (Independent researcher), Junjie Lei (The University of Hong Kong), and Wenjie Huang (The University of Hong Kong), *"Adaptive Finite-Budget Training for CVaR Risk-Aware Q-Learning"*, arXiv preprint `arXiv:2608.04305v1 [q-fin.RM, cs.LG]`, submitted August 4, 2026. Stable URL: [https://arxiv.org/abs/2608.04305](https://arxiv.org/abs/2608.04305). Full text HTML: [https://arxiv.org/html/2608.04305v1](https://arxiv.org/html/2608.04305v1). Submitted to the ACM International Conference on AI in Finance (ICAIF '26), Milan.
- **Empirical Datasets:**
  - **Bitcoin Spot Market Data:** Daily BTCUSDT closing prices retrieved from the Binance public market-data API.
  - **Market Sentiment Data:** Crypto Fear and Greed Index retrieved from the Alternative.me public API (values from 0 to 100 with categorical sentiment classifications: Extreme Fear, Fear, Neutral, Greed, Extreme Greed).
  - **Sample Period:** February 8, 2018 to June 28, 2026 (3,059 daily observations aligned by UTC calendar date).
  - **Dataset Partitioning:** Chronological split; first 70% (2,141 trading days, February 2018 to December 2023) for training, and remaining 30% (918 trading days, December 2023 to June 2026) for out-of-sample test evaluation.
- **Foundational Literature:**
  - Huang, W. and Haskell, W. B. (2021), "Stochastic approximation for risk-aware markov decision processes", *IEEE Transactions on Automatic Control* 66(3), 1314–1320 — foundational asymptotic convergence theory for two-timescale RaQL under dynamic coherent risk measures.
  - Rockafellar, R. T. and Uryasev, S. (2000), "Optimization of conditional value-at-risk", *Journal of Risk* 2(3), 21–41 — variational representation of CVaR as an optimization over a VaR-like threshold.
  - Ben-Tal, A. and Teboulle, M. (2007), "An old-new concept of convex risk measures: the optimized certainty equivalent", *Mathematical Finance* 17(3), 449–476.
  - Gordy, M. B. and Juneja, S. (2010), "Nested simulation in portfolio risk measurement", *Management Science* 56(10), 1833–1848 — cube-root allocation principle for nested budget allocation.
  - Li, X., Yang, W., Liang, J., Zhang, Z., and Jordan, M. I. (2023), "A statistical analysis of Polyak–Ruppert averaged Q-learning", *AISTATS* 2023 — iterate averaging for stochastic variance reduction.

## Economic mechanism

### Source-reported

1. **Failure of Expected-Return Maximization in Asymmetric Crypto Regimes:** Standard risk-neutral reinforcement learning (e.g. classical Q-learning or PPO maximizing expected cumulative return) is heavily vulnerable in cryptocurrency markets due to fat-tailed crashes, volatility clustering, and liquidation-driven drawdown spirals. Dynamic coherent risk objectives, specifically Conditional Value-at-Risk (CVaR), penalize the expected loss in the worst $(1-\alpha)$ tail beyond the Value-at-Risk threshold.
2. **Two-Timescale Coupling and Error Amplification in CVaR RaQL:** In model-free CVaR RaQL, an inner stochastic approximation loop tracks the moving Value-at-Risk threshold $y(s,a)$, while an outer loop updates the action-value table $Q(s,a)$ against the CVaR target $G_\alpha(x, y) = y + \frac{1}{1-\alpha}(x - y)_+$. The authors identify an intrinsic error-amplification mechanism: when $y < x$, the subgradient target expands to:
   $$G_\alpha(x, y) = \frac{x}{1-\alpha} - \frac{\alpha y}{1-\alpha}$$
   For example, at $\alpha = 0.8$, $G_{0.8}(x, y) = 5x - 4y$. If the inner threshold estimate $y$ lags materially below the true conditional VaR optimizer $y^\star$, its estimation error is multiplied by $\frac{\alpha}{1-\alpha}$ (a $4\times$ amplification), propagating massive noise and divergence into the outer Q-update.
3. **Finite-Budget Instability:** Under a finite sampling budget $B$, fixed hyperparameters ($L=80$, $h_y=10$, global decay $j^{-p}$) fail due to:
   - Asymmetric visitation across state-action cells, causing rarely visited cells to suffer premature step-size decay;
   - Uncoupled timescales, where late-stage outer Q-updates shift the minimizer slowly but inner steps remain inappropriately large;
   - Early training instability, where rapid Q-table shifts cause $y$ to diverge.
4. **Adaptive Training Controller without Objective Drift:** The authors propose an adaptive controller that preserves the exact original CVaR Bellman fixed point while dynamically coordinating sample allocation, step sizes, and estimator aggregation via six mechanisms.

### Research interpretation

The alpha thesis operates as a **dynamic downside-risk throttling policy**:
1. **Dynamic Exposure Sizing Conditioned on Joint Sentiment-Momentum Regimes:** Rather than trying to predict unconditional directional drift, the policy learns the optimal portfolio exposure $w \in \{-0.5, -0.2, 0.0, 0.2, 0.5, 1.0\}$ that minimizes the tail risk of multi-period portfolio drawdown given current Bitcoin momentum and market sentiment extremes (Fear & Greed Index).
2. **Variance and Drawdown Suppression at the Expense of Uncompensated Right-Tail Beta:** The strategy accepts lower raw cumulative upside (earning 23.61% vs. 35.43% for Buy-and-Hold over the 2023–2026 test period) in exchange for suppressing annualized volatility from 47.93% down to 9.57%, cutting maximum drawdown from 52.21% down to 6.46%, and lowering daily CVaR tail loss from 0.0210 down to 0.0041.
3. **Subgradient Tracking Stability as an Algorithmic Edge:** The controller ensures that the learned policy converges reliably to the true CVaR optimal policy under modest sample budgets (reducing Bellman residual variance by 85%), preventing the RL agent from overfitting to sample noise or taking erratic levered bets.

## Signal

### Mathematical Specification of CVaR RaQL

Let $\mathcal{S}$ be the finite state space ($S = |\mathcal{S}| = 27$) and $\mathcal{A}$ be the finite action set ($A = |\mathcal{A}| = 6$). Let $Q: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$ denote the cost-valued action-value table.
For upper-tail CVaR at confidence level $\alpha \in (0, 1)$, the sample-level CVaR target and inner subgradient are:
$$G_\alpha(x, y) = y + \frac{1}{1-\alpha} \max\{x - y, 0\}$$
$$g_y(x, y) = 1 - \frac{1}{1-\alpha} \mathbf{1}_{\{x > y\}}$$
where $x_{sa}(s'; Q) = \ell(s, a, s') + \gamma V_Q^-(s')$ is the one-step target loss, with frozen value $V_Q^-(s') = \min_{a'} Q^-(s', a')$.

### The Six Adaptive Controller Mechanisms

The complete adaptive training controller (Algorithm 2 in source) modifies the training execution through three modules:

#### Module 1: Tracking-Stability Module
1. **Per-Cell Inner-Loop Step-Size Decay:**
   Instead of decaying step sizes by a global counter $j$, decay according to the cell-specific inner visit count $k_{sa}$ within the current outer iteration:
   $$\lambda_{sa} = k_{sa}^{-p}$$
2. **Outer-Rate-Matched Decay Synchronization:**
   Couple the inner step size to the outer Q-update learning rate by incorporating the outer visit counter $n_{sa}$:
   $$\lambda_{sa} = k_{sa}^{-p} n_{sa}^{-\eta}$$
   where $\eta$ is matched to the outer Q-learning decay exponent, ensuring that as outer Q-updates settle, inner tracking steps shrink proportionally.
3. **Early $y$ Correction:**
   During the first 5% of the total sampling budget ($T = b/B \le 0.05$), pull the threshold estimate $y(s, a)$ toward the reference target to prevent error amplification and runaway divergence:
   $$y(s, a) \leftarrow y(s, a) + \frac{1}{n_{sa} + 2} 0.5^{k_{sa}-1} \left(\operatorname{clip}(x, y_{\min}, y_{\max}) - y(s, a)\right)$$

#### Module 2: Sampling-Efficiency Module
4. **Two-Phase Action Selection:**
   - **Phase 1 (Broad Coverage, $T = b/B < 0.60$):** Sample the least-visited action in the state to ensure balanced Q-table coverage and avoid premature step-size decay:
     $$a = \arg\min_{a' \in \mathcal{A}} n_{s, a'}$$
   - **Phase 2 (Greedy Concentration, $T \ge 0.60$):** Shift sampling budget toward optimal policy states using $\epsilon$-greedy exploration with greedy probability 0.90 (i.e. $\epsilon = 0.10$).
5. **Progressive Suffix Aggregation:**
   Instead of updating $Q(s, a)$ with only the final inner target $\widehat{q}_{k_{sa}, sa}$, compute an expanding suffix average of the inner target sequence:
   $$\widehat{q}_{\mathrm{agg}, sa} = \frac{1}{m} \sum_{i=k_{sa}-m+1}^{k_{sa}} \widehat{q}_{i, sa}, \quad m = \lceil \omega(T) k_{sa} \rceil$$
   where the suffix fraction expands linearly with training progress:
   $$\omega(T) = 0.1 + 0.1 \min\{9, \lfloor 10T \rfloor\}$$

#### Module 3: Observable-Calibration Module
6. **Data-Driven Parameter Calibration:**
   - **Discount-Aware Outer Exponent:**
     $$\eta = \operatorname{clip}\left(0.5 + k_w(1 - \gamma), 0.5 + \varepsilon, 1.0\right)$$
   - **Loss-Aware Inner Risk Scale:**
     $$h_y = \kappa_h \frac{\ell_{\mathrm{avg}}}{\alpha(1 - \gamma)}$$
     where $\ell_{\mathrm{avg}}$ is the mean absolute loss estimated over a 1-epoch warmup.
   - **Budget-Aware Inner-Loop Depth:**
     $$L = \operatorname{round}\left(k_T \left(\frac{B}{S A}\right)^{1/3}\right)$$

### Operational Trading Policy Execution

At test time, the learned table $Q^\star$ induces the deterministic, parameter-free execution policy:
$$a_t = \arg\min_{a \in \mathcal{A}} Q^\star(s_t, a)$$
The portfolio targets exposure $w(a_t) \in \{-0.5, -0.2, 0.0, 0.2, 0.5, 1.0\}$ in BTCUSDT at daily close (00:00 UTC).

## Required data

- **Underlying Market Price Data:**
  - Asset: BTCUSDT spot (Binance).
  - Timeframe: Daily bars (24-hour UTC calendar day closing prices).
  - Feature: Daily simple return $r_t = P_t / P_{t-1} - 1$.
- **Sentiment Indicator Data:**
  - Alternative.me Crypto Fear & Greed Index (daily values 0 to 100).
  - Sentiment Momentum: 7-day rolling change $\Delta_{7\text{d}}\text{FGI}_t = \text{FGI}_t - \text{FGI}_{t-7}$.
- **State Discretization (27 States):**
  - Feature 1: Current Fear & Greed Index (3 bins: Extreme Fear/Fear, Neutral, Greed/Extreme Greed).
  - Feature 2: 7-day Sentiment Momentum (3 bins: negative momentum, stable, positive momentum).
  - Feature 3: Recent daily return $r_t$ (3 bins: down, flat, up).
  - Combined discrete Markov state $s_t \in \{1, \ldots, 27\}$.
- **Action Space:**
  - Discrete exposure choices $w(a) \in \{-0.5, -0.2, 0.0, 0.2, 0.5, 1.0\}$.
- **Missing Data Handling:** Strict calendar-date alignment; missing dates dropped.

## Execution assumptions

- **Rebalancing Cadence:** Daily at UTC 00:00 close upon observation of state $s_t$.
- **Order Type:** Market order executed at daily close price $P_t$.
- **Transaction Costs:** 5 basis points ($c_{\mathrm{tc}} = 0.0005$) deducted per unit of portfolio turnover:
  $$R_{t}^{\mathrm{net}} = w(a_t) r_{t+1} - c_{\mathrm{tc}} |w(a_t) - w(a_{t-1})|$$
- **Turnover Tracking:** Average daily turnover observed at $\approx 17.40\%$ for the adaptive policy (vs. 0.11% for Buy-and-Hold and 12.78% for baseline).
- **Borrow & Shorting:** Actions $w = -0.5$ and $w = -0.2$ assume inverse short availability with zero borrow fee modeled in the paper (provenance gap: funding rate / borrow cost is omitted).

## Evidence

### Source-reported

All figures, parameter sweeps, and statistics trace directly to Wu, Lei, and Huang (arXiv:2608.04305v1, Section 4, Tables 1–3, Figures 1–3):

1. **Ablation of Bellman Residuals across 20 Seeds ($B = 856,000$ samples, Table 1):**
   - **Scheme 0 (Fixed baseline, $L=80, h_y=10$):** MaxBEQ = 4.6889, MeanBEQ = 1.2202, MaxBEV = 1.9789, MeanBEV = 1.1624.
   - **Scheme 1 (+ Inner-Loop Decay):** MaxBEQ = 6.6569, MeanBEQ = 3.5297, MaxBEV = 4.7099, MeanBEV = 3.3499.
   - **Scheme 2 (+ Outer-Loop Decay):** MaxBEQ = 3.9745, MeanBEQ = 0.6122, MaxBEV = 0.3134, MeanBEV = 0.1211.
   - **Scheme 3 (+ Early $y$ Correction):** MaxBEQ = 3.9438, MeanBEQ = 0.6080, MaxBEV = 0.3133, MeanBEV = 0.1207 (eliminates training divergence when $h_y \le 0.04$).
   - **Scheme 4 (+ Two-Phase Action Selection):** MaxBEQ = 1.4916, MeanBEQ = 0.2369, MaxBEV = 0.2819, MeanBEV = 0.0950.
   - **Scheme 5 (+ Progressive Suffix Aggregation):** MaxBEQ = 1.4361, MeanBEQ = 0.2251, MaxBEV = 0.1667, MeanBEV = 0.0601.
   - **Scheme 6 (+ Observable Calibration Module):** MaxBEQ = 1.3302, MeanBEQ = 0.1854, MaxBEV = 0.1959, MeanBEV = 0.0535.
   - **Overall Residual Reduction:** MeanBEQ reduced by 84.8% ($1.2202 \to 0.1854$), MeanBEV reduced by 95.4% ($1.1624 \to 0.0535$).

2. **Hyperparameter Robustness Sweeps (Table 2):**
   - $\alpha \in [0.50, 0.90]$ sweep ($\gamma = 0.80$): Scheme 6 MeanBEQ ranges from 0.1663 to 0.4005 (vs. 0.1910 to 0.6702 for Scheme 5); MeanBEV ranges from 0.0500 to 0.1108 (vs. 0.0528 to 0.1997 for Scheme 5).
   - $\gamma \in [0.70, 0.90]$ sweep ($\alpha = 0.60$): Scheme 6 MeanBEQ ranges from 0.1856 to 0.1940; MeanBEV ranges from 0.0520 to 0.0576.

3. **Out-of-Sample Trading Performance (918 test days, after 5 bps transaction costs, Table 3):**
   - **Scheme 6 (Adaptive Controller):**
     - Sharpe Ratio: **0.9281** (sample std across 20 seeds: 0.0401)
     - Annualized Return: 8.79% (0.41%)
     - Cumulative Return: 23.61% (1.18%)
     - Annualized Volatility: **9.57%** (0.00%)
     - Maximum Drawdown: **6.46%** (0.38%)
     - Daily Average Turnover: 0.1740 (0.0016)
     - Daily Tail CVaR Loss ($\alpha=0.6$): **0.0041** (0.0000)
   - **Scheme 0 (Fixed-Parameter Baseline):**
     - Sharpe Ratio: 0.5628 (0.2281)
     - Annualized Return: 7.14% (3.89%)
     - Cumulative Return: 19.22% (11.21%)
     - Annualized Volatility: 14.53% (4.82%)
     - Maximum Drawdown: 17.77% (6.48%)
     - Daily Average Turnover: 0.1278 (0.0577)
     - Daily Tail CVaR Loss: 0.0050 (0.0007)
   - **Buy-and-Hold Benchmark:**
     - Sharpe Ratio: 0.4902
     - Annualized Return: 12.82%
     - Cumulative Return: 35.43%
     - Annualized Volatility: 47.93%
     - Maximum Drawdown: 52.21%
     - Daily Average Turnover: 0.0011
     - Daily Tail CVaR Loss: 0.0210
   - **Fixed $w = 0.2$ Benchmark:**
     - Sharpe Ratio: 0.4902
     - Cumulative Return: 11.25%, Annualized Volatility: 9.59%, Max Drawdown: 12.61%, CVaR Loss: 0.0042.

### Independently reproduced

`not independently reproduced`.

### Negative evidence

- **Upside Capture Lag:** The strategy severely underperforms Buy-and-Hold during explosive bull market runs in raw return (23.61% vs. 35.43% cumulative return), because the risk-averse CVaR objective deliberately dampens market exposure.
- **Short-Exposure Borrow Costs Omitted:** The backtest models short allocations ($w \in \{-0.5, -0.2\}$) without deducting perpetual funding rates or borrow fees. In sustained contango / negative funding regimes, short holding drag could degrade net returns.
- **Sensitivity to Discrete State Boundaries:** The 27-state tabular formulation relies on static tercile discretization of returns and sentiment, which may experience regime shift during macro structural breaks.
- **Absence of Proof of Convergence:** As acknowledged by the authors in Section 5, while empirical convergence is verified across 20 random seeds, formal mathematical convergence proofs for coupled adaptive step-size recursions do not yet exist in the RL literature.

## Falsification plan

1. **Transaction Cost Sensitivity Threshold:** Run walk-forward backtests under fees from 5 bps to 50 bps. If the strategy's annualized Sharpe ratio drops below that of Buy-and-Hold (0.4902) at realistic taker fee levels ($c_{\mathrm{tc}} \ge 15\text{ bps}$), reject the operational trading edge.
2. **Perpetual Funding Rate Inclusion:** Retest the policy incorporating actual historical 8-hour Binance BTCUSDT perpetual funding rates on short exposures ($w < 0$). If cumulative net return turns negative, reject the short-position hypothesis.
3. **Sentiment Factor Placebo Test:** Permute the Fear & Greed Index labels across dates while preserving price returns. If the resulting Sharpe ratio is within 1 standard deviation of the true model ($0.9281 \pm 0.0401$), falsify the claim that sentiment momentum provides state informativeness.
4. **Out-of-Universe Transfer Test:** Apply the trained Q-learning policy directly to ETHUSDT and SOLUSDT. If the maximum drawdown exceeds 25% or CVaR loss exceeds 0.015, reject cross-crypto portability.

## Crypto portability

- **Portability:** `direct` (empirical evidence in the paper is established directly on Bitcoin BTCUSDT spot and Crypto Fear & Greed Index from 2018 to 2026).
- **Execution Venue Considerations:**
  - While the paper assumes spot trading, implementing negative weights ($w \in \{-0.5, -0.2\}$) requires perpetual futures (e.g. Binance or Bybit BTCUSDT perps).
  - Perpetual execution introduces 8-hour funding rates, which must be tracked as an explicit cost component.
  - The 24/7 nature of crypto markets aligns with the paper's 365-day annualization convention.

## Limitations

- `not independently reproduced`;
- **Provenance Gap on Calibration Constants:** The preprint paper states that hyperparameters $k_w, \kappa_h, k_T$ and exponents $p, \varepsilon$ are calibrated once and kept fixed across parameter sweeps, but their exact numeric values are omitted from the main text.
- **Tabular State Representation:** Constrained to $3^3 = 27$ discrete states; continuous state features (order-flow imbalance, funding rates, open interest) cannot be represented without neural function approximation.
- **Single-Asset Evaluation:** The study evaluates only Bitcoin (BTCUSDT); portfolio-level cross-sectional diversification across multiple altcoins is unproven.

## Implementation status

- `not-implemented`. Research capture only; no NautilusTrader, PyBroker, paper, testnet, or live trading modules have been constructed or authorized.

## Adoption boundary

- `research-only`, `not-approved`.
- This record captures academic research on risk-sensitive reinforcement learning for Bitcoin. It does not authorize capital allocation, strategy promotion, or deployment to paper, testnet, or live systems.

## Related Wiki records

- `[[quant/alphazerobeta-recurrent-ppo-market-neutral-portfolio-2026-09-02]]` — Reinforcement learning for portfolio optimization.
- `[[quant/dynamic-portfolio-optimization-cvar-stochastic-control-hjb-2026-09-02]]` — Continuous-time CVaR stochastic control.
- `[[quant/crypto-cross-sectional-sentiment-risk-beta-premium-2026-09-01]]` — Sentiment-driven risk premia in crypto.

## Sources

1. Yifan Wu, Junjie Lei, and Wenjie Huang, *"Adaptive Finite-Budget Training for CVaR Risk-Aware Q-Learning"*, arXiv preprint `arXiv:2608.04305v1 [q-fin.RM, cs.LG]`, submitted August 4, 2026. Stable URL: [https://arxiv.org/abs/2608.04305](https://arxiv.org/abs/2608.04305). Full text HTML: [https://arxiv.org/html/2608.04305v1](https://arxiv.org/html/2608.04305v1).
2. Huang, W. and Haskell, W. B. (2021), "Stochastic approximation for risk-aware markov decision processes", *IEEE Transactions on Automatic Control* 66(3), 1314–1320. DOI: [10.1109/TAC.2020.2990145](https://doi.org/10.1109/TAC.2020.2990145).
3. Rockafellar, R. T. and Uryasev, S. (2000), "Optimization of conditional value-at-risk", *Journal of Risk* 2(3), 21–41. DOI: [10.21314/JOR.2000.038](https://doi.org/10.21314/JOR.2000.038).
4. Ben-Tal, A. and Teboulle, M. (2007), "An old-new concept of convex risk measures: the optimized certainty equivalent", *Mathematical Finance* 17(3), 449–476. DOI: [10.1111/j.1467-9965.2007.00311.x](https://doi.org/10.1111/j.1467-9965.2007.00311.x).
5. Gordy, M. B. and Juneja, S. (2010), "Nested simulation in portfolio risk measurement", *Management Science* 56(10), 1833–1848. DOI: [10.1287/mnsc.1100.1213](https://doi.org/10.1287/mnsc.1100.1213).
6. Li, X., Yang, W., Liang, J., Zhang, Z., and Jordan, M. I. (2023), "A statistical analysis of Polyak–Ruppert averaged Q-learning", *Proceedings of the 26th International Conference on Artificial Intelligence and Statistics (AISTATS)*, PMLR 206, 2207–2261.
