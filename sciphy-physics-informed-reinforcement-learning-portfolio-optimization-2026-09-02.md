---
schema: strategy-research-record-v1
title: "SciPhy Reinforcement Learning for Dynamic Institutional Portfolio Allocation with Microstructure Price Impact"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - reinforcement-learning
  - physics-informed-neural-networks
  - pinn
  - hamilton-jacobi-bellman
  - price-impact
  - multi-asset-etf
status: research-only
confidence: medium
source_as_of: 2026-07-14
sources:
  - "Igor Halperin and Andrey Itkin, 'SciPhy Reinforcement Learning for Portfolio Optimization', arXiv preprint arXiv:2607.15195v1 [q-fin.PM, q-fin.CP, cs.LG], submitted July 14, 2026. Stable URL: https://arxiv.org/abs/2607.15195. Full text HTML: https://arxiv.org/html/2607.15195v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SciPhy Reinforcement Learning for Dynamic Institutional Portfolio Allocation with Microstructure Price Impact

## Provenance

- **Primary Source:** Igor Halperin and Andrey Itkin, *"SciPhy Reinforcement Learning for Portfolio Optimization"*, arXiv preprint `arXiv:2607.15195v1 [q-fin.PM, q-fin.CP, cs.LG]`, submitted July 14, 2026. Stable URL: [https://arxiv.org/abs/2607.15195](https://arxiv.org/abs/2607.15195). Full text HTML: [https://arxiv.org/html/2607.15195v1](https://arxiv.org/html/2607.15195v1).
- **Asset Universe & Historical Dataset:**
  - 14 liquid US Exchange-Traded Funds (ETFs) spanning multiple asset classes:
    - US Equity Trackers: SPY (S&P 500), IWM (Russell 2000), QQQ (Nasdaq 100), DIA (Dow Jones Industrial Average);
    - International Equities: EFA (Developed Markets ex-US), EEM (Emerging Markets), FXI (China Large-Cap);
    - Fixed Income: TLT (20+ Year US Treasury Bond), HYG (High Yield Corporate Bond);
    - Commodities: GLD (Gold), SLV (Silver), USO (Crude Oil);
    - Currencies: FXE (Euro);
    - Real Estate: VNQ (MSCI US REIT Index).
  - Historical sample period: January 1, 2019 to December 31, 2025 (7 full calendar years, approximately 1,762 trading days per asset).
  - Data attributes: Daily Open, High, Low, Close, Volume, Average Daily Volume (ADV), and Market Capitalization obtained from Yahoo Finance.
  - Microstructure spreads: High-Low daily spread estimator of Corwin & Schultz (2012) utilized to calibrate five-parameter Kyle/Almgren-Chriss quadratic execution impact tensors.
  - Chronological Partitioning:
    - Training block: Windows 0 to 1007 (covering 2019 through 2022);
    - Purge gap: 63 trading days;
    - Out-of-sample evaluation: Windows 1071 to 1190 (April 2023 to December 2023).
- **Foundational Literature:**
  - Almgren, R. and Chriss, N. (2001), "Optimal execution of portfolio transactions", *Journal of Risk* 3(2), 5–39 — quadratic price impact modeling.
  - Halperin, I. (2023), offline reinforcement learning via pathwise Hamilton-Jacobi PDEs and Girsanov likelihood ratios.
  - Raissi, M., Perdikaris, P., and Karniadakis, G. E. (2019), "Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations", *Journal of Computational Physics* 378, 686–707.
  - Corwin, S. A. and Schultz, P. (2012), "A simple way to estimate bid-ask spreads from daily high and low prices", *Journal of Finance* 67(2), 719–760.
  - Dang, D. M. and Forsyth, P. A. (2014), "Better than Merton: continuous-time portfolio allocation under impulse control", *SIAM Journal on Control and Optimization* 52(6), 3412–3441.

## Economic mechanism

### Source-reported

1. **Failure of Linear-Quadratic and Myopic Models Under Price Impact:** When institutional portfolios rebalance across multiple assets, large transactions exert permanent and temporary market impact. In continuous time, both running execution costs and induced price drift scale quadratically with trading action, moving the portfolio problem outside the classical linear-quadratic-regulator (LQR) framework. Myopic mean-variance rebalancing or unconstrained signal-tilted rules incur excessive trading friction and turnover that rapidly destroys gross information gains.
2. **Extrapolation Collapse in Offline Deep Reinforcement Learning:** Applying conventional model-free deep reinforcement learning (e.g. DDPG, PPO, SAC) to historical financial data fails due to severe distribution shift: out-of-distribution state queries cause value networks to produce wildly inaccurate overestimations.
3. **Physics-Informed Regularization via Pathwise Hamilton-Jacobi Projection:** The authors formulate entropy-regularized dynamic portfolio optimization over an extended state space $\mathbf{y}_t = (\mathbf{x}_t, \mathbf{S}_t, C_t)$ (holdings, stochastic prices, and cumulative costs). Applying Itô's lemma along observed empirical trajectories cancels second-order diffusion terms against martingale increments. This projects the continuous-time semilinear Hamilton-Jacobi-Bellman (HJB) PDE onto a pathwise first-order Hamilton-Jacobi (HJ) relation along realized historical paths.
4. **Single-Sweep Offline Optimization Without Policy Iteration:** By parameterizing the value function $J_\theta$ with a Physics-Informed Neural Network (PINN) and weighting historical behavioral demonstrations by their exact Girsanov Radon-Nikodym likelihood ratio, the offline RL problem reduces to a single-pass supervised regression objective. The mathematical PDE structure enforces spatial smoothness across the value gradients ($\partial J/\partial \mathbf{x}, \partial J/\partial \mathbf{S}, \partial J/\partial C$), eliminating extrapolation error.
5. **Elimination of Rate-Accumulation Transient via Target-Holding Reformulation:** In continuous-time rate formulations ($d\mathbf{x}_t = \mathbf{a}_t dt$), position holdings $\mathbf{x}_t$ represent slow integrals of trading rates. Over short institutional horizons (e.g., 20–60 business days), this induces a structural lag where signal-implied holdings are never reached before the episode terminates. Reformulating the control variable from a continuous trading rate $\mathbf{a}_t$ to an instantaneous target holding jump $\mathbf{h}_t = \mathbf{x}_{t+\Delta t}$ allows the portfolio to immediately realize signal-implied weights while charging full quadratic price impact on the induced rate $\mathbf{a}_t = (\mathbf{h}_t - \mathbf{x}_t)/\Delta t$.

### Research interpretation

The alpha thesis operates as a **dynamic multi-period execution and risk-budgeting controller**:
1. **Transfer Coefficient Maximization Under Severe Market Frictions:** The framework addresses the fundamental gap between raw signal predictive power (information coefficient $\mathrm{IC} \approx 0.27$) and tradable Sharpe ratio. Rather than generating an alpha signal from scratch, SciPhyRL acts as an optimal dynamic execution and sizing transformer, dampening trades where marginal transaction costs exceed marginal signal drift.
2. **Turnover Suppression via Convex Regularization:** By enforcing Kullback-Leibler (KL) divergence shrinkage toward a low-turnover equal-weighted prior and embedding saturating time envelopes $g(\tau) = \tau_{\mathrm{sat}} \tanh(\tau / \tau_{\mathrm{sat}})$, the controller prevents runaway rebalancing as the time horizon grows.
3. **Horizon-Stable Risk-Adjusted Edge:** While absolute portfolio returns fluctuate across market regimes, the policy maintains a stable risk-adjusted advantage (+0.40 to +0.415 Sharpe ratio gain over passive equal-weight benchmarks) across both 1-month and 3-month evaluation windows.

## Signal

### Extended State Space and Control Reformulation

Let $N = 14$ denote the number of portfolio assets. The state vector at time $t$ is:
$$\mathbf{y}_t = (\mathbf{x}_t, \mathbf{S}_t, C_t) \in \mathbb{R}^N \times \mathbb{R}^N \times \mathbb{R}$$
where $\mathbf{x}_t \in \mathbb{R}^N$ represents holdings in share units, $\mathbf{S}_t \in \mathbb{R}^N$ represents asset price levels, and $C_t \in \mathbb{R}$ tracks cumulative execution costs.

The control action is parameterized as the target holding $\mathbf{h}_t \in \mathbb{R}^N$, executed instantaneously at the beginning of each daily interval $[t, t+\Delta t]$ ($\Delta t = 1$ trading day):
$$\mathbf{x}_{t+\Delta t} = \mathbf{h}_t$$
The induced trade size is $\delta \mathbf{h}_t = \mathbf{h}_t - \mathbf{x}_t$, and the induced trading rate is:
$$\mathbf{a}_t = \frac{\mathbf{h}_t - \mathbf{x}_t}{\Delta t}$$

### Cumulative Cost and Objective Function

The continuous-time value function $J(\tau, \mathbf{x}, \mathbf{S}, C)$ with time-to-go $\tau = T - t$ minimizes the running execution and risk cost plus relative entropy toward behavioral prior policy $\pi_0$:
$$J(\tau, \mathbf{x}, \mathbf{S}, C) = \inf_{\pi} \mathbb{E} \left[ \int_0^\tau \left( \mathcal{C}(\mathbf{x}_t, \mathbf{a}_t, \mathbf{S}_t) + \beta^{-1} D_{\mathrm{KL}}(\pi(\cdot|\mathbf{y}_t) \,||\, \pi_0(\cdot|\mathbf{y}_t)) \right) dt + U(C_T) \right]$$
where $\beta > 0$ is the inverse temperature parameter, and the terminal utility enforces quadratic tracking of a target Capital Market Line (CML) cost level $z_{\mathrm{tg}}$:
$$U(C_T) = \frac{1}{2} (C_T - z_{\mathrm{tg}})^2$$

### Value Function Neural Ansatz

To satisfy terminal conditions analytically, the PINN parameterizes $J_\theta$ via the hard-terminal ansatz:
$$J_\theta(\tau, \mathbf{x}, \mathbf{S}, C) = U(C) + g(\tau) h_\theta(\mathbf{x}, \mathbf{S}, C)$$
where $g(\tau) = \tau_{\mathrm{sat}} \tanh(\tau / \tau_{\mathrm{sat}})$ is a saturating time envelope that bounds spatial value gradients at large $\tau$, preventing unconstrained turnover accumulation.

### Analytic Gibbs Optimal Policy

Under a two-component Gaussian mixture prior $\pi_0(\mathbf{a}) = \sum_{k=1}^2 \omega_k \mathcal{N}(\mathbf{u}_k^{(0)}, \mathbf{\Omega}_k^{(0)})$, the optimal policy $\pi^\star(\mathbf{h}|J)$ is an updated Gaussian mixture whose component means $\mathbf{u}_k(J)$ and precisions $\mathbf{\Omega}_k(J)^{-1}$ are derived in closed form from the gradient vectors:
$$\nabla_{\mathbf{x}} J_\theta, \quad \nabla_{\mathbf{S}} J_\theta, \quad \nabla_C J_\theta$$

### Predictive Signal Construction

In the empirical validation, the underlying cross-sectional signal $\zeta_t$ is constructed to match the empirical lag-1 autocorrelation $\rho_{\mathrm{asset}}$ of asset returns:
$$\zeta_{t, i} = \alpha_1 \tilde{r}_{t+1, i} + \beta_1 \mathrm{EWMA}_t(\tilde{r}_i) + u_{t, i} + \eta_{t, i}$$
where:
- $\tilde{r}_{t, i} = \dot{S}_{t, i} / (\sigma_i S_{t, i})$ is the normalized log-return;
- $\mathrm{EWMA}_t(\tilde{r}_i)$ is an exponential moving average with span $= 3$;
- $u_{t, i} \sim \mathcal{N}(0, 1)$ is independent Gaussian noise;
- $\eta_{t, i}$ is a stationary unit-variance $\mathrm{AR}(1)$ process with persistence parameter $\varphi \in (-1, 1)$;
- Parameters $(\alpha_1, \beta_1, \varphi)$ are determined sequentially by:
  1. Memory share $m \in [0, 1)$ fixing the fraction of informative variance from historical returns ($m = 0.3$);
  2. Total informative variance pinned to $q$ ($q \in \{0.1, 0.2\}$);
  3. Signal lag-1 autocorrelation matched to asset return lag-1 autocorrelation $\rho_{\mathrm{asset}} = -0.0229$.
  For $T=63, q=0.1, m=0.3$: $\alpha_1 = 0.2672, \beta_1 = 0.2943, \varphi = -0.0831$.

## Required data

- **Universe:** 14 liquid US ETFs (SPY, IWM, QQQ, DIA, EFA, EEM, FXE, FXI, TLT, HYG, SLV, GLD, USO, VNQ).
- **Timeframe:** Daily bars (1 trading day $\Delta t = 1.0$).
- **Fields Required:**
  - Daily Open, High, Low, Close (OHLC);
  - Daily Trading Volume and Average Daily Volume (ADV);
  - Daily Market Capitalization;
  - Daily Bid-Ask Spread proxy estimated via Corwin-Schultz (2012) high-low spread estimator:
    $$\gamma = \left[\log\left(\frac{H_t}{L_t}\right)\right]^2 + \left[\log\left(\frac{H_{t+1}}{L_{t+1}}\right)\right]^2, \quad \beta = \log\left(\frac{\max(H_t, H_{t+1})}{\min(L_t, L_{t+1})}\right)^2$$
- **Sample Length:** January 1, 2019 to December 31, 2025 (7 years; 1,762 trading days).
- **Execution Windows:** Rolling episodes of length $T = 31$ trading days (1 calendar month) and $T = 63$ trading days (1 quarter).
- **Missing Data Handling:** Calendar alignment with standard US market holidays; missing prints forward-filled or dropped.

## Execution assumptions

- **Execution Cadence:** Daily rebalancing at market open based on state $\mathbf{y}_t$ formed at prior close.
- **Price Impact Model:** Microstructure-grounded quadratic model (Almgren-Chriss / Kyle framework) with 5 calibrated effective parameters:
  - Permanent price impact scaling with trading volume relative to ADV;
  - Temporary price impact scaling quadratically with trade size;
  - Cross-asset impact tensor capturing spillover liquidity shocks;
  - Proportional transaction costs set to approximately 10 basis points (0.0010) per trade turnover unit.
- **Turnover Definition:** Cumulative one-way turnover:
  $$\mathrm{Turnover} = \sum_{t=1}^T \frac{\sum_{i=1}^N P_{t, i} |\delta h_{t, i}|}{\Pi_t}$$
  where a value of 1.0 indicates the entire portfolio book is traded once per episode.
- **Self-Financing Enforcement:** Softly enforced via a quadratic penalty on notional deviations $|\sum_i P_{t, i} h_{t, i} - \Pi_t|^2$ in the Gibbs step, with residual cash imbalances accumulated and tracked explicitly in the state variable $C_t$.

## Evidence

### Source-reported

All figures, metrics, and parameters trace directly to Halperin & Itkin (arXiv:2607.15195v1, Section 6, Tables 3–7, Figures 1–8):

1. **Performance Metrics for Horizon $T = 31$ Days ($q = 0.1, R^2 = 0.0501$, Table 3):**
   - **In-Sample (1,008 episodes, 2019–2022):**
     - Gibbs Policy (SciPhyRL): Sharpe **0.611**, Annualized Return 7.4%, Annualized Volatility 12.0%, Turnover 0.5475.
     - Equal-Weight Baseline: Sharpe 0.502, Annualized Return 7.8%, Annualized Volatility 15.5%, Turnover 0.2349.
     - Behavioral Prior Policy: Sharpe 0.441, Annualized Return 6.7%, Annualized Volatility 15.3%, Turnover 1.2428.
   - **Out-of-Sample (120 episodes, April–December 2023):**
     - Gibbs Policy (SciPhyRL): Sharpe **1.120**, Annualized Return 9.0%, Annualized Volatility **8.0%**, Turnover 0.5414.
     - Equal-Weight Baseline: Sharpe 1.074, Annualized Return 10.9%, Annualized Volatility 10.2%, Turnover 0.1971.
     - Behavioral Prior Policy: Sharpe 0.937, Annualized Return 9.6%, Annualized Volatility 10.2%, Turnover 1.2421.

2. **Performance Metrics for Horizon $T = 31$ Days ($q = 0.2, R^2 = 0.1147$, Table 4):**
   - **In-Sample (1,008 episodes):**
     - Gibbs Policy (SciPhyRL): Sharpe **1.180**, Annualized Return 14.0%, Annualized Volatility 11.8%, Turnover 1.1987.
     - Equal-Weight Baseline: Sharpe 0.502, Annualized Return 7.8%, Annualized Volatility 15.5%, Turnover 0.2349.
     - Behavioral Prior Policy: Sharpe 0.441, Annualized Return 6.7%, Annualized Volatility 15.3%, Turnover 1.2428.
   - **Out-of-Sample (120 episodes):**
     - Gibbs Policy (SciPhyRL): Sharpe **1.489**, Annualized Return 12.3%, Annualized Volatility **8.2%**, Turnover 1.1485.
     - Equal-Weight Baseline: Sharpe 1.074, Annualized Return 10.9%, Annualized Volatility 10.2%, Turnover 0.1971.
     - Behavioral Prior Policy: Sharpe 0.937, Annualized Return 9.6%, Annualized Volatility 10.2%, Turnover 1.2421.

3. **Performance Metrics for Horizon $T = 63$ Days ($q = 0.2, R^2 = 0.1166, \beta = 15$, Table 5):**
   - **In-Sample (1,008 episodes):**
     - Gibbs Policy (SciPhyRL): Sharpe **1.139**, Annualized Return 12.7%, Annualized Volatility 11.2%, Turnover 2.4322.
     - Equal-Weight Baseline: Sharpe 0.447, Annualized Return 6.9%, Annualized Volatility 15.4%, Turnover 0.4878.
     - Behavioral Prior Policy: Sharpe 0.390, Annualized Return 5.9%, Annualized Volatility 15.1%, Turnover 2.5388.
   - **Out-of-Sample (120 episodes, spanning Autumn 2023 multi-asset drawdown):**
     - Gibbs Policy (SciPhyRL): Sharpe **0.526**, Annualized Return 4.3%, Annualized Volatility **8.1%**, Turnover 2.2698.
     - Equal-Weight Baseline: Sharpe 0.126, Annualized Return 1.3%, Annualized Volatility 10.4%, Turnover 0.3837.
     - Behavioral Prior Policy: Sharpe 0.025, Annualized Return 0.3%, Annualized Volatility 10.5%, Turnover 2.5090.

4. **Sensitivity to Control Parameters ($\beta = 25$, Panel 5, Figures 7–8):**
   - For $T = 63, q = 0.2, \beta = 25, z_{\mathrm{tg}} = N_{\mathrm{not}}(1.0 - e^{0.2T})$:
     - In-Sample: Sharpe **1.618**, Annualized Return 13.7%, Annualized Volatility 8.5%, Turnover 4.1490.
     - Out-of-Sample: Sharpe **0.706**, Annualized Return 4.4%, Annualized Volatility **6.2%**, Turnover 3.8942.

5. **Stability of the Sharpe Edge Across Horizons:**
   - Out-of-sample Sharpe advantage of SciPhyRL over the Equal-Weight benchmark:
     - At $T = 31$ days: $+0.415$ (1.489 vs 1.074).
     - At $T = 63$ days: $+0.400$ (0.526 vs 0.126).
   - Bootstrap 95% confidence intervals across 10 random seeds (Table 6) confirm narrow variance around reported IQM levels, demonstrating robustness to network weight initialization.

### Independently reproduced

`not independently reproduced`.

### Negative evidence

- **Regime Vulnerability in Macro Drawdowns:** At $T = 63$ days, absolute out-of-sample Sharpe ratio collapses from 1.49 down to 0.526 (and annual return from 12.3% down to 4.3%). The authors explain that the 120 rolling 63-day test windows overlap across August–October 2023, when equities, Treasuries, credit, and commodities experienced a simultaneous multi-asset sell-off as the US 10-year yield approached 5%. Because all 14 assets declined jointly, multi-asset diversification could not avoid drawdowns.
- **Symmetric Tracking Utility Caps Right-Tail Upside:** The quadratic terminal loss $U(C) = \frac{1}{2}(C - z_{\mathrm{tg}})^2$ penalizes surplus gains beyond target $z_{\mathrm{tg}}$ identically to shortfalls, artificially constraining right-tail profit accumulation.
- **Failure of Continuous Rate Formulation (Ablation Null Result):** In the rate-coordinate ablation (Section D.2), without the target-holding reformulation ($d\mathbf{x}_t = \mathbf{a}_t dt$), the learned policy collapses entirely onto the passive equal-weighted benchmark, failing to express signal information within realistic trading horizons.
- **Off-Diagonal Covariance Truncation:** To keep the analytic Gibbs step tractable, the quadratic curvature in the precision matrix is truncated to the diagonal of $P^\top \Sigma P$, discarding cross-asset risk couplings in the second-order term.

## Falsification plan

1. **Ablation of Hamilton-Jacobi Regularization (Behavioral Cloning Test):** Train the neural network without the pathwise Hamilton-Jacobi residual loss in Eq. (73). If the resulting policy produces Sharpe ratios within 1 standard error of full SciPhyRL, falsify the claim that PDE-informed physics regularization is necessary for offline control.
2. **Signal Decay Stress Test:** Replace the engineered oracle signal with real decay-prone signals (e.g. cross-sectional short-term reversal or analyst revisions with half-life $\tau_{1/2} < 3$ days). If the net-of-cost Sharpe ratio falls below the passive equal-weight baseline (Sharpe $\le 0.126$), reject the multi-period execution edge for fast-decay alphas.
3. **Transaction Cost and Slippage Sensitivity:** Increase modeled transaction costs from 10 bps to 35 bps. If the out-of-sample Sharpe gain over equal-weight disappears ($\Delta \mathrm{Sharpe} \le 0.05$), falsify the claim of cost-resilient multi-period optimization.
4. **Window-Overlap Significance Test:** Recompute statistical significance using block-bootstrap or Diebold-Mariano tests with non-overlapping 63-day windows. If the $p$-value for the Sharpe advantage over equal weight exceeds 0.05, invalidate the horizon-stability hypothesis.

## Crypto portability

- **Portability:** `adapted` / `unproven`.
- **Porting Rationale:** The primary source establishes empirical results exclusively on a 14-asset US ETF universe using daily closing bars. It has never been tested on cryptocurrency spot or perpetual markets.
- **Crypto-Specific Frictions:**
  - **24/7 Continuous Trading:** Crypto markets operate without overnight session closures, requiring redefinition of discrete rebalancing cadence $\Delta t$ and continuous tracking of funding cycles.
  - **Perpetual Funding Rate Drift:** In crypto perpetuals, holding costs include 8-hour funding rates $f_t$, which introduce an additional state variable into the cost function $C_t$.
  - **Fat-Tailed Price Impact:** Crypto liquidity on centralized (e.g. Binance) and decentralized (e.g. Uniswap v3) venues exhibits extreme order-book depth asymmetry and liquidity cascades, violating Kyle's symmetric quadratic impact assumption.
  - **High Idiosyncratic Volatility:** Annualized volatilities in crypto (60%–120%) require substantially wider prior distributions $\mathbf{\Omega}_k^{(0)}$ and lower inverse temperature $\beta$ to avoid severe KL divergence explosions.

## Limitations

- `not independently reproduced`;
- `unproven` in crypto markets (adapted research interpretation only);
- **Engineered Oracle Signal Dependency:** The empirical experiments utilize a synthetic oracle signal with controlled out-of-sample $R^2 \in [0.05, 0.12]$ rather than real, uncurated predictive factors;
- **Overlapping Rolling Windows:** The 120 test episodes at $T = 63$ share 62 of 63 days, inducing strong serial correlation across out-of-sample performance observations;
- **Heuristic Parameter Settings:** Price impact and control hyperparameters ($\beta, \Lambda, z_{\mathrm{tg}}, \tau_{\mathrm{sat}}$) are set to illustrative values rather than formally calibrated via maximum likelihood or cross-validation;
- **Diagonal Precision Approximation:** The analytical Gibbs partition function truncates cross-asset off-diagonal covariance terms in the quadratic exponent.

## Implementation status

- `not-implemented`.
- Pure research capture. No NautilusTrader, PyBroker, backtest engine, paper trading, testnet, or live execution scripts have been implemented or authorized.

## Adoption boundary

- `research-only`, `not-approved`.
- This record serves solely as a structured research capture of academic literature on physics-informed reinforcement learning for dynamic portfolio optimization. It does not authorize capital deployment, model promotion, or live execution.

## Related Wiki records

- `[[quant/dynamic-portfolio-optimization-cvar-stochastic-control-hjb-2026-09-02]]` — Continuous-time HJB stochastic control for portfolio optimization.
- `[[quant/self-consistent-adjoint-policy-iteration-constrained-portfolio-2026-09-02]]` — Simulation-based policy iteration for constrained dynamic portfolio choice.
- `[[quant/path-portfolio-optimization-signature-defect-lift-2026-09-02]]` — Path portfolio optimization and signature defect regularization.
- `[[quant/observable-matrix-dynamics-portfolio-optimization-2026-09-02]]` — Multi-asset dynamic allocation with market-neutral constraints.

## Sources

1. Igor Halperin and Andrey Itkin, *"SciPhy Reinforcement Learning for Portfolio Optimization"*, arXiv preprint `arXiv:2607.15195v1 [q-fin.PM, q-fin.CP, cs.LG]`, submitted July 14, 2026. Stable URL: [https://arxiv.org/abs/2607.15195](https://arxiv.org/abs/2607.15195). Full text HTML: [https://arxiv.org/html/2607.15195v1](https://arxiv.org/html/2607.15195v1).
2. Almgren, R. and Chriss, N. (2001), "Optimal execution of portfolio transactions", *Journal of Risk* 3(2), 5–39. DOI: [10.21314/JOR.2001.038](https://doi.org/10.21314/JOR.2001.038).
3. Corwin, S. A. and Schultz, P. (2012), "A simple way to estimate bid-ask spreads from daily high and low prices", *Journal of Finance* 67(2), 719–760. DOI: [10.1111/j.1540-6261.2012.01729.x](https://doi.org/10.1111/j.1540-6261.2012.01729.x).
4. Dang, D. M. and Forsyth, P. A. (2014), "Better than Merton: continuous-time portfolio allocation under impulse control", *SIAM Journal on Control and Optimization* 52(6), 3412–3441. DOI: [10.1137/130948956](https://doi.org/10.1137/130948956).
5. Raissi, M., Perdikaris, P., and Karniadakis, G. E. (2019), "Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations", *Journal of Computational Physics* 378, 686–707. DOI: [10.1016/j.jcp.2018.10.045](https://doi.org/10.1016/j.jcp.2018.10.045).
