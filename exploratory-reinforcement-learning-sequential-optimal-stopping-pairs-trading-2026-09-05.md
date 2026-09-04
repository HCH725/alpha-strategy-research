---
schema: strategy-research-record-v1
title: "Exploratory Reinforcement Learning for Speculative Trading: Continuous-Time Sequential Optimal Stopping, Intensity-Relaxed Cox Processes, and Closed-Form Gibbs Execution Policies"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - pairs-trading
  - reinforcement-learning
  - optimal-stopping
  - cox-process
  - entropy-regularization
  - exploratory-rl
  - prospect-theory
  - hamilton-jacobi-bellman
status: research-only
confidence: high
source_as_of: 2026-04-02
sources:
  - "Yun Zhao, Alex S.L. Tse, and Harry Zheng, 'Reinforcement Learning for Speculative Trading under Exploratory Framework', arXiv:2604.02035v1 [q-fin.TR], April 2, 2026. https://arxiv.org/abs/2604.02035"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Exploratory Reinforcement Learning for Speculative Trading: Continuous-Time Sequential Optimal Stopping, Intensity-Relaxed Cox Processes, and Closed-Form Gibbs Execution Policies

## Provenance

- **Primary Academic Source:** Yun Zhao (Department of Mathematics, Imperial College London, London SW7 2AZ, UK; `yun.zhao23@imperial.ac.uk`, supported by Roth Scholarship), Alex S.L. Tse (Department of Mathematics, University College London, London WC1H 0AY, UK; `alex.tse@ucl.ac.uk`), and Harry Zheng (Department of Mathematics, Imperial College London, London SW7 2AZ, UK; `h.zheng@imperial.ac.uk`), *"Reinforcement Learning for Speculative Trading under Exploratory Framework"*, arXiv preprint `arXiv:2604.02035v1 [q-fin.TR]`, submitted April 2, 2026.
  - Canonical arXiv Abstract: [https://arxiv.org/abs/2604.02035](https://arxiv.org/abs/2604.02035)
  - Canonical DOI: [https://doi.org/10.48550/arXiv.2604.02035](https://doi.org/10.48550/arXiv.2604.02035)
  - Full-Text HTML: [https://arxiv.org/html/2604.02035v1](https://arxiv.org/html/2604.02035v1)
  - Primary LaTeX Source Package: `https://arxiv.org/src/2604.02035` (audited directly from unpacked source files `Reinforcement_Learning_for_Speculative_Trading_under_Exploratory_Framework.tex`, figures, and bibliography).
- **Associated Code / Implementation Verification:** The paper establishes theoretical foundations and numerical implementations using finite difference HJB solvers and deep policy iteration. Data and algorithms are presented self-contained in the text and Appendix B (`Algorithm 1: Offline Policy Iteration`). All mathematical derivations, state dynamics, error bounds, and simulation equations were directly audited from the primary LaTeX source.
- **Pre-Write Deduplication & Identity Verification:** An exhaustive scan across all 379 markdown strategy records in `alpha-strategy-research` confirmed zero existing records matching `2604.02035`, `Yun Zhao`, `Alex S.L. Tse`, `Harry Zheng`, or `sequential optimal stopping exploratory framework`. Existing statistical arbitrage and pairs-trading records in the repository focus on:
  - Non-parametric empirical mean-reversion time minimization (`model-free-statistical-arbitrage-empirical-mean-reversion-time-reinforcement-learning-2026-09-05.md`);
  - End-to-end autoencoder policy learning (`end-to-end-statistical-arbitrage-autoencoder-policy-2026-09-05.md`);
  - Graph clustering with SPONGE (`graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05.md`);
  - Convex-concave programming with moving bands (`moving-band-statistical-arbitrage-convex-concave-markowitz-2026-09-05.md`);
  - Maximum weight matching pairs selection (`graphical-matching-pairs-trading-maximum-weight-matching-2026-09-05.md`);
  - LSTM factor replication (`statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05.md`);
  - Signature-based optimal execution (`signature-optimal-execution-statistical-arbitrage-quadratic-reduction-2026-09-02.md`).
  None of the existing records address sequential two-stage (entry and exit) optimal stopping in continuous time, nor do they employ intensity-relaxed Cox jump processes regularized by uniform-measure Shannon differential entropy with closed-form Gibbs policy distributions. The theoretical and algorithmic formulation in `arXiv:2604.02035v1` is completely distinct.

## Economic mechanism

### Source-reported

1. **Failure of One-Off Stopping and Fixed-Threshold Executions:** Classical pairs trading and speculative trading literature traditionally assumes either heuristic fixed-deviation entry/exit rules (e.g., standard deviation bands $\pm 2\sigma$, which fail out-of-sample due to parameter instability) or one-off optimal stopping formulations (which solve either entry or exit independently, ignoring the causal feedback between entry level and subsequent exit profitability).
2. **Sequential Dynamic Optimization under Prospect Theory Preferences:** Speculative round-trip trading fundamentally requires a sequential optimal stopping formulation: an agent must first time the initiation $\tau$, pay purchase costs, and subsequently time the liquidation $\nu \geq \tau$ to maximize discounted expected utility over the round-trip profit net of transaction costs. Under S-shaped Prospect Theory preferences (with risk aversion over gains, risk seeking over losses, and loss aversion parameter $k > 1$), an investor's willingness to liquidate is strongly conditioned on the pathwise reference entry price $B_{\nu} = P_{\tau}$.
3. **Intensity Relaxation via Cox Processes:** In continuous-time stochastic control, solving sequential stopping directly leads to coupled variational inequalities with moving free boundaries that suffer from the curse of dimensionality. By relaxing discrete stopping times into the jump times of two Cox processes whose hazard rates $\alpha_t, \beta_t \in [0, M]$ are controlled, the sequential stopping problem is converted into an equivalent continuous-time Markovian stochastic control problem. The intensity cap $M < \infty$ prevents instantaneous greedy over-exploitation and enforces exploratory duration.
4. **Entropy Regularization and Exploratory Policies:** Deterministic policies in continuous-time reinforcement learning often converge prematurely to suboptimal local extrema. By regularizing the agent's objective with Shannon's differential entropy (relative to the uniform distribution on $[0, M]^2$) scaled by temperature $\eta > 0$, the agent optimizes over continuous probability distributions of execution intensities. This yields closed-form Gibbs distributions whose parameters are driven directly by the economic marginal advantages of entry and exit ($\Delta_1(p)$ and $\Delta_2(p, b)$).
5. **Decoupled Log-Exponential HJB System:** Unlike prior exploratory stopping models (e.g., Dong 2024) which produce explosive exponential source terms, the bounded intensity formulation yields a numerically stable log-exponential source term $\eta \ln\left(\frac{e^y - 1}{y}\right)$, enabling efficient finite-difference solution and model-free offline policy iteration.

### Research interpretation

1. **Path-Conditioned Liquidation Boundary:** The state augmentation $(P_t, J_t, B_t)$ directly embeds path memory into an otherwise Markovian spread. By explicitly tracking the reference entry level $B_t = P_{\tau}$, the model captures the disposition effect and asymmetric loss aversion: when a pair diverges adversely after entry, the required exit threshold $p^*(b)$ dynamically shifts upward to recover transaction costs, preventing premature exit while enforcing mathematically rigorous stopping criteria.
2. **Exploration as Execution Desynchronization:** In real-world limit order books and OTC liquidity pools, executing immediately when a theoretical boundary is crossed often suffers from market impact, adverse selection, and toxic front-running. The Gibbs-distributed intensity policy can be interpreted economically as randomized execution timing (Poisson arrival of orders) that optimizes the trade-off between price slippage risk and execution certainty.
3. **Model-Free Generalization:** Although the analytical benchmark is derived under an Ornstein-Uhlenbeck spread, the offline policy iteration algorithm requires only discrete historical or simulated spread trajectories $\{P_{t_l}\}$. This enables the strategy to adapt to non-Gaussian, fat-tailed, or structurally shifting spreads where analytical PDE solutions do not exist.

## Signal

The strategy operates sequentially through three discrete trading regimes $J_t \in \{0, 1, 2\}$ over an augmented state vector $X_t = (P_t, J_t, B_t) \in \mathbb{R} \times \{0, 1, 2\} \times \mathbb{R}$ (`source-reported`):
- $J_t = 0$: Pre-entry regime (flat position, scanning for optimal spread entry; `source-reported`).
- $J_t = 1$: In-market regime (position open at recorded spread entry price $B_t = P_{\tau}$, scanning for optimal liquidation; `source-reported`).
- $J_t = 2$: Post-exit regime (round-trip transaction completed, terminal absorbing state; `source-reported`).

### 1. State Augmentation and Continuous-Time Dynamics (`source-reported`)

- **Spread Signal Process:** The underlying spread $P_t = S^A_t - S^B_t$ follows a general one-dimensional diffusion:
  $$dP_t = \mu(P_t) dt + \sigma(P_t) dW_t, \quad P_0 = p \quad (\text{source-reported})$$
  In the benchmark pairs-trading implementation, $P_t$ is parameterized as an Ornstein-Uhlenbeck process:
  $$dP_t = \theta (\bar{p} - P_t) dt + \sigma dW_t \quad (\text{source-reported})$$
  where $\theta > 0$ is mean-reversion speed, $\bar{p}$ is long-run equilibrium spread, and $\sigma > 0$ is spread volatility (`source-reported`).
- **State Augmentation Dynamics:**
  $$\begin{aligned}
    dP_t &= \mu(P_t) dt + \sigma(P_t) dW_t, & P_0 &= p \\
    dJ_t^{\bm{u}} &= \mathds{1}_{\{J_{t-}^{\bm{u}} = 0\}} dN_t^{\bm{\alpha}} + \mathds{1}_{\{J_{t-}^{\bm{u}} = 1\}} dN_t^{\bm{\beta}}, & J_0^{\bm{u}} &= 0 \\
    dB_t^{\bm{u}} &= P_t \mathds{1}_{\{J_{t-}^{\bm{u}} = 0\}} dN_t^{\bm{\alpha}}, & B_0^{\bm{u}} &= 0
  \end{aligned} \quad (\text{source-reported})$$
  where $N_t^{\bm{\alpha}}$ and $N_t^{\bm{\beta}}$ are Cox counting processes driven by effective intensity rates $\lambda_t^{\bm{\alpha}} = \alpha_t \mathds{1}_{\{J_{t-}^{\bm{u}} = 0\}}$ and $\lambda_t^{\bm{\beta}} = \beta_t \mathds{1}_{\{J_{t-}^{\bm{u}} = 1\}}$, bounded above by $M < \infty$ (`source-reported`).

### 2. Preference Specification and Economic Advantages (`source-reported`)

- **Realized Utility Payoff:** At liquidation $t = \nu$, given current spread $p$ and entry spread $b$, the terminal reward is:
  $$G(p, b) = U(\gamma p - \iota b - \Psi - R) \quad (\text{source-reported})$$
  For pairs trading with $\gamma = \iota = 1$ and S-shaped power utility:
  $$G(p, b) = \begin{cases}
    (p - b - \Psi - R)^{\varpi}, & p - b - \Psi - R \geq 0 \\
    -k |p - b - \Psi - R|^{\varpi}, & p - b - \Psi - R < 0
  \end{cases} \quad (\text{source-reported})$$
  where $\varpi \in (0, 1]$ represents risk aversion/seeking curvature, $k > 0$ denotes loss aversion, $\Psi \geq 0$ is fixed transaction cost, and $R \in \mathbb{R}$ is the reference benchmark return (`source-reported`).
- **Marginal Entry and Exit Advantages:**
  $$\Delta_1(p) := \mathcal{V}_1(p, p) - \mathcal{V}_0(p) \quad (\text{source-reported})$$
  representing the certainty-equivalent net advantage of entering the trade at spread $p$ relative to remaining flat (`source-reported`).
  $$\Delta_2(p, b) := G(p, b) - \mathcal{V}_1(p, b) \quad (\text{source-reported})$$
  representing the certainty-equivalent net advantage of closing the trade at spread $p$ given reference entry $b$ relative to continuing to hold (`source-reported`).

### 3. Optimal Exploratory Policy and Execution Intensities (`source-reported`)

- **Closed-Form Gibbs Exploration Densities:** Over intensity domain $\mathbb{M} = [0, M]$ with entropy temperature $\eta > 0$:
  $$\pi^{\bm{\alpha},*}(\lambda; p) = \frac{\Delta_1(p)}{\eta} \frac{\exp\left(\lambda \Delta_1(p)/\eta\right)}{\exp\left(M \Delta_1(p)/\eta\right) - 1}, \quad \lambda \in [0, M] \quad (\text{source-reported})$$
  $$\pi^{\bm{\beta},*}(\lambda; p, b) = \frac{\Delta_2(p, b)}{\eta} \frac{\exp\left(\lambda \Delta_2(p, b)/\eta\right)}{\exp\left(M \Delta_2(p, b)/\eta\right) - 1}, \quad \lambda \in [0, M] \quad (\text{source-reported})$$
  When $\Delta_1(p) = 0$ or $\Delta_2(p, b) = 0$, the optimal density reduces to the uniform distribution $\frac{1}{M}$ on $[0, M]$ (`source-reported`).
- **Closed-Form Optimal Execution Intensities (Mean Arrival Rates):**
  $$\bar{\lambda}^{\bm{\alpha},*}(p) = \begin{cases}
    \frac{M}{1 - \exp\left(-M \Delta_1(p)/\eta\right)} - \frac{\eta}{\Delta_1(p)}, & \Delta_1(p) \neq 0 \\
    \frac{M}{2}, & \Delta_1(p) = 0
  \end{cases} \quad (\text{source-reported})$$
  $$\bar{\lambda}^{\bm{\beta},*}(p, b) = \begin{cases}
    \frac{M}{1 - \exp\left(-M \Delta_2(p, b)/\eta\right)} - \frac{\eta}{\Delta_2(p, b)}, & \Delta_2(p, b) \neq 0 \\
    \frac{M}{2}, & \Delta_2(p, b) = 0
  \end{cases} \quad (\text{source-reported})$$
- **Greedy Limit ($\eta \downarrow 0$):** As exploration is quenched, policies collapse to threshold indicators:
  $$\bar{\lambda}^{\bm{\alpha},*}(p) \to M \mathds{1}_{\{\Delta_1(p) > 0\}} + \frac{M}{2} \mathds{1}_{\{\Delta_1(p) = 0\}} \quad (\text{source-reported})$$
  $$\bar{\lambda}^{\bm{\beta},*}(p, b) \to M \mathds{1}_{\{\Delta_2(p, b) > 0\}} + \frac{M}{2} \mathds{1}_{\{\Delta_2(p, b) = 0\}} \quad (\text{source-reported})$$
  defining the optimal free boundaries $p^*(b)$ as the unique roots where $\Delta_1(p) = 0$ and $\Delta_2(p, b) = 0$ (`source-reported`).

### 4. Offline Policy Iteration Algorithm (`source-reported`, Appendix B)

Given offline signal trajectories $\{P_{t_l}^n\}_{l=0, \dots, L}^{n=1, \dots, N}$ discretized at $\Delta t$:
1. **State Simulation:** At each step $l$, compute entry/exit probabilities:
   $$q_{t_l}^{\bm{\alpha}} = 1 - \exp\left(-\bar{\lambda}_{t_l}^{\bm{\alpha}} \Delta t\right), \quad q_{t_l}^{\bm{\beta}} = 1 - \exp\left(-\bar{\lambda}_{t_l}^{\bm{\beta}} \Delta t\right) \quad (\text{source-reported})$$
   Draw Bernoulli variables $Y_l^{\bm{\alpha}} \sim \text{Bernoulli}(q_{t_l}^{\bm{\alpha}})$ and $Y_l^{\bm{\beta}} \sim \text{Bernoulli}(q_{t_l}^{\bm{\beta}})$ to transition $J_{t_{l+1}}$ and latch $B_{t_{l+1}} = P_{t_{l+1}}$ upon entry (`source-reported`).
2. **Temporal Difference Errors:**
   $$\begin{aligned}
     \delta_{0, l} &= \mathds{1}_{\{j_l = 0\}} \left( -c_{t_l}^{\bm{\alpha}} \Delta t + e^{-\rho \Delta t} \left( \mathds{1}_{\{j_{l+1}=0\}} \mathcal{V}_0(p_{l+1}) + \mathds{1}_{\{j_{l+1}=1\}} \mathcal{V}_1(p_{l+1}, b_{l+1}) \right) - \mathcal{V}_0(p_l) \right) \\
     \delta_{1, l} &= \mathds{1}_{\{j_l = 1\}} \left( -c_{t_l}^{\bm{\beta}} \Delta t + e^{-\rho \Delta t} \left( \mathds{1}_{\{j_{l+1}=1\}} \mathcal{V}_1(p_{l+1}, b_{l+1}) + \mathds{1}_{\{j_{l+1}=2\}} G(p_{l+1}, b_{l+1}) \right) - \mathcal{V}_1(p_l, b_l) \right)
   \end{aligned} \quad (\text{source-reported})$$
   where entropy penalties are:
   $$c_{t_l}^{\bm{\alpha}} = \eta \int_0^M \pi_{t_l}^{\bm{\alpha}}(\lambda) \ln(M \pi_{t_l}^{\bm{\alpha}}(\lambda)) d\lambda, \quad c_{t_l}^{\bm{\beta}} = \eta \int_0^M \pi_{t_l}^{\bm{\beta}}(\lambda) \ln(M \pi_{t_l}^{\bm{\beta}}(\lambda)) d\lambda \quad (\text{source-reported})$$
3. **Loss Function and Network Update:**
   $$\text{loss}^{(k)} = \frac{1}{\sum_{n=1}^N \sum_{i=1}^I \sum_{l=0}^{L-1} \mathds{1}_{\{J_{t_l}^{n, i, k} \in \{0, 1\}\}}} \sum_{n=1}^N \sum_{i=1}^I \sum_{l=0}^{L-1} \left( (\delta_{0, l}^{n, i, k})^2 + (\delta_{1, l}^{n, i, k})^2 \right) \quad (\text{source-reported})$$
   Update value function parameters $\Theta_0, \Theta_1$ via gradient descent (`source-reported`).

### 5. Research-Proposed Operational Trading Rules (`research-proposed`)

The paper demonstrates theoretical convergence and offline policy iteration under continuous diffusion; the following rules are research interpretations required to translate the continuous policy into discrete execution (`research-proposed`):
- **Bar Timeframe & Sampling:** 5-minute or 15-minute consolidated bars for crypto perpetual pairs (`research-proposed`).
- **Discrete Entry Trigger:** Enter long spread ($+1$ asset A, $-1$ asset B) when estimated entry intensity $\bar{\lambda}^{\bm{\alpha},*}(P_t) \geq 0.5 \cdot M$ (`research-proposed`).
- **Discrete Exit Trigger:** Liquidate spread position when estimated exit intensity $\bar{\lambda}^{\bm{\beta},*}(P_t, B_t) \geq 0.5 \cdot M$ (`research-proposed`).
- **Hard Stop-Loss Override:** If $P_t - B_t \leq -3.0 \cdot \frac{\sigma}{\sqrt{2\theta}}$, exit immediately regardless of policy to cap structural divergence tail risk (`research-proposed`).
- **Maximum Holding Period:** Force exit after $T_{\max} = 3.0 \cdot \frac{\ln 2}{\theta}$ (three half-lives of the OU process) to prevent capital stagnation (`research-proposed`).

## Required data

- **Instruments:** Two highly correlated or cointegrated assets forming a mean-reverting spread $P_t = S^A_t - S^B_t$ (`source-reported`). In crypto adaptation, high-liquidity perpetual futures contracts (e.g., ETHUSDT vs. BTCUSDT, or intra-sector pairs like ARBUSDT vs. OPUSDT; `research-proposed`).
- **Timeframe:** Continuous-time theoretical formulation; discretized at $\Delta t = 0.1$ in simulation (`source-reported`). In market backtesting: 1-minute to 15-minute OHLCV bars (`research-proposed`).
- **Price Fields:** Mid-quote or last traded prices for $S^A_t$ and $S^B_t$; synthetic spread series $P_t = S^A_t - S^B_t$ (`source-reported`).
- **Funding & Borrow Rates:** For perpetual futures adaptation: 8-hour funding rates for both legs to account for net funding carry ($F^A_t - F^B_t$; `research-proposed`).
- **Point-in-Time Hygiene:** Cointegration parameters and OU calibration parameters ($\theta, \bar{p}, \sigma$) must be estimated strictly rolling out-of-sample over a formation lookback window (e.g., 60 days; `research-proposed`) without lookahead leakage.

## Execution assumptions

- **Order Types & Timing:** Continuous intensity control implies execution via Poisson arrival of orders (`source-reported`). In discrete trading implementation: limit orders placed at the inside bid/ask when arrival probability exceeds threshold, or passive maker orders with 50 ms execution latency (`research-proposed`).
- **Fill Model:** Immediate fill assumed in theoretical paper (`source-reported`). In research backtesting: conservative maker-taker fill model with half-spread crossing penalty (`research-proposed`).
- **Trading Fees:** Zero in baseline theoretical setup ($\Psi = 0$; `source-reported`). In crypto perpetual backtesting: maker fee $0.02\%$, taker fee $0.05\%$ per leg (`research-proposed`).
- **Slippage & Market Impact:** Neglected in primary paper (`source-reported`). For realistic simulation: fixed 2 bps slippage per trade (`research-proposed`).
- **Capital & Leverage:** 1x nominal leverage, dollar-neutral notional allocation across both pair legs (`research-proposed`).

## Evidence

### Source-reported

1. **Theoretical Convergence Proofs (Theorems 2.9 & 3.6):**
   - The authors prove that the error between the original sequential optimal stopping value function $V_{\text{orig}}$ and the entropy-regularized exploratory RL objective $\mathcal{V}_{\text{ent}}^{\eta}$ satisfies:
     $$|V_{\text{orig}}(p) - \mathcal{V}_{\text{ent}}^{\eta}(p, 0, 0)| \leq C M^{-\kappa/2} + C M^2 |\eta \ln \eta| \quad (\text{source-reported})$$
     where $\kappa \in (0, 1]$ is the H\"older exponent of the utility function, $M$ is the intensity cap, and $\eta$ is entropy temperature (`source-reported`).
   - Monotone convergence $\mathcal{V}_{\text{ent}}^{\eta_1} \leq \mathcal{V}_{\text{ent}}^{\eta_2}$ holds for $\eta_1 \geq \eta_2$ because relative Shannon entropy is strictly non-positive ($\mathcal{H}(\pi) \leq 0$; `source-reported`).
   - Exact convergence to the true value function is established when $M \to \infty$ and $\eta \downarrow 0$ such that $M^2 |\eta \ln \eta| \to 0$ (`source-reported`).
2. **Benchmark Numerical Implementation Parameters:**
   - Model parameters: subjective discount rate $\rho = 0.05$, OU mean reversion speed $\theta = 0.1$, long-run mean $\bar{p} = 0$, volatility $\sigma = 0.2$, Prospect Theory risk parameter $\varpi = 0.5$, loss aversion $k = 2$, transaction cost $\Psi = 0$, reference point $R = 1$ (`source-reported`).
   - Grid domain: $p \in [-4.0, 4.0], b \in [-4.0, 4.0]$, grid spacing $0.05$, stopping tolerance $10^{-6}$ for iterative tridiagonal finite-difference solver (`source-reported`).
   - Operating parameters: $M = 50$, $\eta = 10^{-5}$ (`source-reported`).
3. **Comparative Statics and Free Boundaries:**
   - Value function $\mathcal{V}_0(p)$ is strictly monotonically decreasing in spread $p$ (`source-reported`).
   - Value function $\mathcal{V}_1(p, b)$ is strictly monotonically increasing in $p$ and decreasing in $b$ (`source-reported`).
   - Exit free boundary $p^*(b)$ (the root of $\Delta_2(p, b) = 0$) increases monotonically with entry price $b$, verifying that loss-averse traders dynamically demand higher exit prices when entering at higher levels (`source-reported`).
   - Increasing $\sigma$ raises $\mathcal{V}_0(p)$ across all $p$ because higher spread volatility accelerates entry and exit stopping times, increasing discounted present value (`source-reported`).
   - Increasing $\theta$ raises $\mathcal{V}_0(p)$ for low $p$ (strong mean-reversion pulls spread up faster) but depresses $\mathcal{V}_0(p)$ near equilibrium $\bar{p}$ (spread is confined to a narrow band, limiting round-trip excursion profit; `source-reported`).
4. **Offline Policy Iteration Accuracy:**
   - Parameterized via two-layer MLPs with 32 hidden units and ReLU activation; time step $\Delta t = 0.1$, horizon $L = 100$ steps (`source-reported`).
   - Policy iteration closely tracks the ground-truth finite-difference HJB solution, with small approximation errors localized strictly around the free boundary $p^*(b)$ (`source-reported`).
5. **Provenance Gap on Empirical Backtests:** The paper is a theoretical and methodological contribution; it presents comprehensive stochastic proofs, finite-difference solutions, and offline policy iteration simulations, but does not report empirical PnL or Sharpe ratios on historical equity or crypto tick datasets (`source-reported provenance gap`).

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **High Temperature Failure Mode:** When entropy temperature $\eta$ is set too high (e.g., $\eta = 0.1$), the exploration penalty flattens the policy distribution across $[0, M]$, causing the agent to trade randomly with low intensity even when the spread is deeply mispriced, severely degrading realized profit (`source-reported`).
2. **Low Intensity Cap Throttling:** When $M$ is too low (e.g., $M = 1$), the agent cannot execute trades rapidly enough when favorable opportunities occur, causing long execution lags that miss transient mean-reversion peaks (`source-reported`).
3. **Boundary Sensitivity in Neural Approximation:** As documented in Figure 8 of the paper, neural network TD error approximation shows noticeable errors near the free boundary $p^*(b)$, which can lead to premature or delayed triggering if the network is under-parameterized (`source-reported`).

## Falsification plan

1. **Placebo Test on Geometric Brownian Motion:** Run the policy iteration agent on pure geometric Brownian motion (zero mean reversion, $\theta = 0$). If the agent initiates trades and generates positive annualized alpha net of transaction costs, the strategy is overfitted to noise. `Research-defined falsification threshold`: annualized Sharpe $> 0.2$ on pure GBM indicates spurious fit.
2. **Transaction Cost Sensitivity Test:** Inject realistic round-trip crypto perpetual fees ($0.08\%$ combined taker fees) plus 5 bps slippage. `Research-defined falsification threshold`: net Sharpe must remain $> 1.0$; if transaction friction reduces cumulative return below zero, the strategy is falsified for active trading.
3. **Out-of-Sample Parameter Stability (Walk-Forward):** Calibrate the neural value approximators on historical rolling 6-month windows and evaluate out-of-sample on the subsequent 3 months across 10 cryptocurrency pairs. `Research-defined falsification threshold`: OOS Sharpe $< 0.5$ or maximum drawdown exceeding $20\%$ falsifies the model-free adaptation.
4. **Regime Shift / Trend Decoupling Stress Test:** Apply the policy during structural divergence regimes (e.g., token hack, tokenomics change, or delisting events where the spread exhibits a permanent structural break). `Research-defined falsification threshold`: maximum loss per pair must be strictly bounded by the hard stop-loss override ($< 5\%$ total portfolio equity loss).

## Crypto portability

**Portability Classification:** `adapted` / `unproven`.

### Specific Portability Risks and Structural Differences
1. **Perpetual Funding Rate Asymmetry:** In traditional cash-settled pairs trading, holding costs are dominated by borrow rates. In crypto perpetuals, 8-hour funding rates can be highly asymmetric and persistent during bull/bear regimes. A spread position holding long asset A and short asset B can bleed substantial capital if asset A trades at a large funding premium while asset B is at a discount (`research-proposed`).
2. **24/7 Continuous Trading and Sudden Liquidation Cascades:** Unlike equity markets with daily closes and circuit breakers, crypto markets operate 24/7 with frequent flash crashes and cascade liquidations. A sharp basis shock can trigger exchange liquidations before the mean-reverting drift manifests (`research-proposed`).
3. **Cross-Exchange Basis & Fragmentation:** Pairs trading across different centralized exchanges (e.g., Binance vs. Bybit) introduces transfer latency and counterparty risk. The strategy is best deployed within a single high-liquidity venue (`research-proposed`).
4. **Contract Specifications and Non-Linear PnL:** Using USDT-margined perpetuals ensures linear payoff matching the paper's $P_t = S^A_t - S^B_t$ assumption. Coin-margined (inverse) contracts violate linearity and require non-linear hedging models (`research-proposed`).

## Limitations

- `underspecified`: The paper evaluates the model on simulated Ornstein-Uhlenbeck processes and does not provide an explicit cointegration screening pipeline or portfolio allocation heuristic for multi-pair universes.
- `not independently reproduced`: No live or historical market backtest has been performed in this repository.
- `unproven`: Crypto perpetual application is an adapted research hypothesis; funding costs and order book liquidity constraints were not modeled in the paper.
- `data gap`: Order book level-2 microstructure depth, queue position, and latency slippage were omitted in the continuous diffusion formulation.

## Implementation status

`not-implemented`

No implementation currently exists in `nautilus-quant-system`, PyBroker, or live trading workflows. This capture is strictly for theoretical normalization and research evaluation.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

This document represents exploratory quantitative research. It does not constitute authorization for deployment, paper trading, testnet, or live capital allocation.

## Related Wiki records

- `model-free-statistical-arbitrage-empirical-mean-reversion-time-reinforcement-learning-2026-09-05.md`
- `end-to-end-statistical-arbitrage-autoencoder-policy-2026-09-05.md`
- `graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05.md`
- `moving-band-statistical-arbitrage-convex-concave-markowitz-2026-09-05.md`
- `graphical-matching-pairs-trading-maximum-weight-matching-2026-09-05.md`
- `statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05.md`
- `signature-optimal-execution-statistical-arbitrage-quadratic-reduction-2026-09-02.md`

## Sources

1. Yun Zhao, Alex S.L. Tse, and Harry Zheng, *"Reinforcement Learning for Speculative Trading under Exploratory Framework"*, arXiv preprint `arXiv:2604.02035v1 [q-fin.TR]`, April 2, 2026.
   - Canonical URL: [https://arxiv.org/abs/2604.02035](https://arxiv.org/abs/2604.02035)
   - DOI: [https://doi.org/10.48550/arXiv.2604.02035](https://doi.org/10.48550/arXiv.2604.02035)
   - Full HTML: [https://arxiv.org/html/2604.02035v1](https://arxiv.org/html/2604.02035v1)
   - Unpacked Primary LaTeX Source Package: `https://arxiv.org/src/2604.02035` (`Reinforcement_Learning_for_Speculative_Trading_under_Exploratory_Framework.tex`, figures, and bibliography).
