---
schema: strategy-research-record-v1
title: "Dynamic Continuous-Time Portfolio Optimization under Hard Terminal CVaR Constraints: Rockafellar-Uryasev Auxiliary-Threshold Reformulation, Strong Lagrangian Duality, and Nested Bisection-Golden Search HJB Control"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - conditional-value-at-risk
  - expected-shortfall
  - stochastic-control
  - hjb-equation
  - lagrangian-duality
  - incomplete-markets
  - price-impact
status: research-only
confidence: high
source_as_of: 2026-08-24
sources:
  - "Anran Hu, Silvana M. Pesenti, and Xiaofei Shi, 'Dynamic Portfolio Optimization under CVaR Constraints', arXiv preprint arXiv:2608.20179v1 [math.OC], August 24, 2026. DOI: 10.48550/arXiv.2608.20179. Stable URL: https://arxiv.org/abs/2608.20179"
  - "Xiaofei Shi, GitHub repository 'xf-shi/Dynamic-Portfolio-under-CVaR', commit a00c290c93ba900c41ae68952b47bd0a7678616c, August 12, 2026. Stable URL: https://github.com/xf-shi/Dynamic-Portfolio-under-CVaR"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Dynamic Continuous-Time Portfolio Optimization under Hard Terminal CVaR Constraints: Rockafellar-Uryasev Auxiliary-Threshold Reformulation, Strong Lagrangian Duality, and Nested Bisection-Golden Search HJB Control

## Provenance

- **Primary Source:** Anran Hu (University of Oxford), Silvana M. Pesenti (University of Toronto), and Xiaofei Shi (University of Toronto), *"Dynamic Portfolio Optimization under CVaR Constraints"*, arXiv preprint `arXiv:2608.20179v1 [math.OC]`, submitted August 24, 2026. DOI: [10.48550/arXiv.2608.20179](https://doi.org/10.48550/arXiv.2608.20179). Stable URL: [https://arxiv.org/abs/2608.20179](https://arxiv.org/abs/2608.20179).
- **Implementation Source:** Xiaofei Shi, official code repository `xf-shi/Dynamic-Portfolio-under-CVaR`, full commit SHA [`a00c290c93ba900c41ae68952b47bd0a7678616c`](https://github.com/xf-shi/Dynamic-Portfolio-under-CVaR/commit/a00c290c93ba900c41ae68952b47bd0a7678616c), including notebooks `Complete_Market_Plots.ipynb`, `Incomplete_Market_Plots.ipynb`, `Linear_Control_Dynamics_Plots.ipynb`, and `Square_Root_Impact_Plots.ipynb`.
- **Primary Subject Areas:** Optimization and Control (`math.OC`), Portfolio Management (`q-fin.PM`), Risk Management (`q-fin.RM`).
- **Research Funding Context:** Supported in part by the Natural Sciences and Engineering Research Council of Canada (NSERC Grants RGPIN-2025-05847, RGPIN-2024-04569), the Fields Institute for Research in Mathematical Sciences (FOCUS program), and the Laboratory for AI-Powered Financial Technologies under the InnoHK initiative of the Government of the Hong Kong Special Administrative Region.
- **Context & Motivation:** In institutional asset management and quantitative trading desks, regulatory rules (e.g., Basel III/IV internal models approach) and risk mandates impose explicit hard bounds on downside tail risk measured by Conditional Value-at-Risk (CVaR, or Expected Shortfall) rather than quadratic variance penalties. While soft penalties in expected utility functions require ad-hoc tuning and cannot guarantee compliance with a strict risk budget, hard continuous-time dynamic constraints typically destroy time consistency or require market completeness to reduce the problem to terminal payoff replication. In incomplete markets or under execution frictions (where wealth dynamics depend nonlinearly on trading rate and current exposure is a state variable), terminal payoffs cannot be hedged statically. Hu, Pesenti, and Shi resolve this long-standing challenge by exploiting the Rockafellar-Uryasev auxiliary-threshold representation of CVaR to establish joint convexity over the adapted control and a scalar threshold variable, proving strong Lagrangian duality without assuming market completeness, and constructing a provably convergent nested bisection-golden search numerical scheme whose inner loop reduces to standard unconstrained Hamilton-Jacobi-Bellman (HJB) stochastic control.

## Economic mechanism

### Source-reported

1. **Direct Downside Tail Conditioning vs. Uniform De-Risking:** Standard mean-variance or constant relative risk aversion (CRRA) preferences penalize dispersion across the entire distribution, leading to uniform deleveraging (scaling down risky asset holdings uniformly across all future states). In contrast, a hard terminal CVaR constraint averages losses solely within the worst $(1-\alpha)$ tail (e.g., the worst $5\%$ of outcomes). The source proves that a binding CVaR constraint induces an *asymmetric reallocation of risk*: the investor dynamically reduces risky exposure along adverse wealth paths to prevent breaching the catastrophic shortfall limit, while preserving—and near maturity even expanding—risky exposure along favorable paths.
2. **Auxiliary Threshold as an Unconstrained Decomposition:** The Rockafellar-Uryasev representation converts the terminal risk constraint into $\inf_{\eta \in \mathbb{R}} \{ \eta + \frac{1}{1-\alpha} \mathbb{E}[(\ell(W_T) - \eta)_+] \} \le c$. By treating $\eta$ as an auxiliary parameter and introducing the Lagrange multiplier $\lambda \ge 0$, the constrained dynamic problem separates into standard unconstrained control problems with a modified terminal penalty $\Psi_{\lambda, \eta}(w) = g(w) + \frac{\lambda}{1-\alpha} (\ell(w) - \eta)_+$.
3. **Indirect Hedging of Nontraded Endowment Shocks:** In incomplete markets, the investor faces unhedgeable orthogonal Brownian shocks $B^\perp$ (e.g., background revenue, illiquid inventory, staking rewards volatility). Because $B^\perp$ cannot be directly neutralized by traded assets, a binding CVaR constraint forces the investor to reduce traded asset exposure more aggressively in adverse states (a $36.3\%$ drop below Merton exposure) to absorb the background tail uncertainty.
4. **Execution Frictions and Asymmetric Liquidations:** Under quadratic trading rate penalties or square-root price impact, the current dollar exposure $\varphi_t$ becomes an additional state variable and signed trading speed $\dot{\varphi}_t$ becomes the control. The optimal policy front-loads position building during initial periods and exhibits state-dependent partial liquidations (negative trading rates $\dot{\varphi}_t < 0$) exclusively along adverse trajectories to defend the terminal CVaR boundary.

### Research interpretation

The falsifiable thesis is that **incorporating a hard terminal CVaR constraint via dynamic HJB feedback control protects downside capital without sacrificing median compounding efficiency, achieving significant tail compression ($14.5\text{--}36.3\%$ exposure reduction in drawdown regimes) while reducing expected terminal wealth by less than $1\%$ relative to unconstrained Merton growth**:
- Rather than resorting to heuristic trailing stops or static portfolio insurance (CPPI), which suffer from whip-saws and gap risk in continuous-time diffusion markets, the nested bisection-golden search policy produces a continuous Markovian feedback map $\varphi_t^*(W_t)$ that is mathematically certified to satisfy the terminal shortfall bound $\text{CVaR}_{0.95}(-W_T) \le c$.
- The mechanism is especially relevant for crypto perpetual trading desks, where unhedgeable basis volatility, funding rate jumps, and exchange liquidation thresholds impose hard non-negotiable bankruptcy constraints that standard Sharpe-maximizing algorithms fail to respect.

## Signal

### 1. Market and Controlled Wealth Dynamics

Let $(\Omega, \mathcal{F}, \mathbb{F}=\{\mathcal{F}_t\}_{t \in [0,T]}, \mathbb{P})$ be a filtered probability space supporting a standard $d$-dimensional Brownian motion $B_t$ and an independent 1-dimensional Brownian motion $B_t^\perp$. The market contains:
- One risk-free asset with interest rate $r \ge 0$.
- $m \le d$ traded risky assets with excess return vector $\mu(t, S_t) \in \mathbb{R}^m$ and volatility matrix $\sigma(t, S_t) \in \mathbb{R}^{m \times d}$.
- An exogenous cumulative endowment process $\zeta_t$ satisfying $d\zeta_t = b_t dt + \beta_t dB_t + \beta_t^\perp dB_t^\perp$, where $\beta_t^\perp \in \mathbb{R}$ represents nontraded background risk.

Let $\phi_t \in \mathbb{R}^m$ denote shares held, and $\varphi_t = \text{diag}(S_t)\phi_t \in \mathbb{R}^m$ denote dollar risky exposure. The controlled wealth process $W_t^\varphi$ evolves as:
$$dW_t^\varphi = \left( r W_t^\varphi + b_t + \mu_t^\top \varphi_t \right) dt + \left( \sigma_t \varphi_t + \beta_t \right)^\top dB_t + \beta_t^\perp dB_t^\perp, \quad W_0^\varphi = w_0 > 0$$

Admissible strategies $\varphi \in \mathcal{A}$ are predictable processes taking values in a compact, convex action set $A \subset \mathbb{R}^m$ (e.g., $A = [\phi_{\min}, \phi_{\max}]$).

### 2. Primal CVaR-Constrained Problem

The investor minimizes expected running and terminal cost $J(\varphi) = \mathbb{E}\left[ \int_0^T f(t, W_t^\varphi, \varphi_t) dt + g(W_T^\varphi) \right]$ subject to a terminal loss risk constraint:
$$\text{CVaR}_\alpha(\ell(W_T^\varphi)) \le c$$
where $\alpha \in (0, 1)$ (typically $\alpha = 0.95$), $\ell(w) = -w$ is the terminal loss, and $c < 0$ denotes the risk tolerance (e.g., $c = -0.94$, ensuring average terminal wealth in the worst $5\%$ of outcomes is at least $-c = 0.94$).

Using the Rockafellar-Uryasev representation:
$$\text{CVaR}_\alpha(\ell(W_T^\varphi)) = \inf_{\eta \in \mathbb{R}} \left\{ \eta + \frac{1}{1-\alpha} \mathbb{E}\left[ (\ell(W_T^\varphi) - \eta)_+ \right] \right\}$$
Defining the residual mapping $C(\varphi, \eta) = \eta + \frac{1}{1-\alpha} \mathbb{E}[(\ell(W_T^\varphi) - \eta)_+] - c$, the problem becomes:
$$\inf_{\varphi \in \mathcal{A}, \, \eta \in E} J(\varphi) \quad \text{s.t.} \quad C(\varphi, \eta) \le 0$$
where $E = \left[ -\frac{M_X}{\sqrt{\alpha}}, \frac{M_X}{\sqrt{1-\alpha}} \right]$ is a compact interval guaranteeing that the true $\alpha$-quantile of loss lies strictly within $E$ (Proposition 3.2).

### 3. Dual Formulation & Strong Duality

The Lagrangian for $(\varphi, \eta) \in \mathcal{A} \times E$ and multiplier $\lambda \ge 0$ is:
$$\mathcal{L}(\varphi, \eta, \lambda) = J(\varphi) + \lambda C(\varphi, \eta) = \mathbb{E}\left[ \int_0^T f(t, W_t^\varphi, \varphi_t) dt + g(W_T^\varphi) + \frac{\lambda}{1-\alpha} (\ell(W_T^\varphi) - \eta)_+ \right] + \lambda(\eta - c)$$
The dual function is $q(\lambda) = \inf_{\varphi \in \mathcal{A}, \eta \in E} \mathcal{L}(\varphi, \eta, \lambda)$, and the dual problem is $\sup_{\lambda \ge 0} q(\lambda)$.
- **Strong Duality (Theorem 3.13):** Under the Slater condition ($\exists \bar{\varphi} \in \mathcal{A}$ with $\text{CVaR}_\alpha(\ell(W_T^{\bar{\varphi}})) < c$), $p^* = d^*$, and an optimal multiplier $\lambda^* \in [0, \Lambda]$ exists with bounded magnitude $\Lambda = \frac{J(\bar{\varphi}) - J_{\text{low}}}{\delta}$.
- **Primal Recovery (Corollary 3.15):** If $J(\varphi)$ is strictly convex, any Lagrangian minimizer at $\lambda^*$ uniquely recovers the primal optimal control $\varphi^*$.

### 4. Nested Bisection-Golden Search Algorithm

The optimal control is computed via a three-tier nested architecture:
1. **Control Oracle (Fixed $\lambda, \eta$):** Solves an unconstrained stochastic control problem with terminal penalty $\Psi_{\lambda, \eta}(w) = g(w) + \frac{\lambda}{1-\alpha} (-w - \eta)_+$. In the scalar HJB formulation on a discretized wealth grid $w \in [w_{\min}, w_{\max}]$:
   $$V_t + \min_{\phi \in A} \left\{ \frac{1}{2}\gamma(\sigma \phi)^2 - \mu \phi + (rw + b + \mu \phi)V_w + \frac{1}{2}(\sigma \phi + \beta)^2 V_{ww} \right\} = 0$$
   with terminal condition $V(T, w) = \frac{\lambda}{1-\alpha}\max(-w - \eta, 0)$.
   The unconstrained minimizer is calculated analytically at each grid point:
   $$\phi^*(t, w) = \text{clip}\left( \frac{\mu(1 - V_w) - \sigma \beta V_{ww}}{\sigma^2(\gamma + V_{ww})}, \, \phi_{\min}, \, \phi_{\max} \right)$$
2. **Inner Golden-Section Search over $\eta \in [\eta_{\text{low}}, \eta_{\text{high}}]$:** Exploits the convexity of $V_\lambda(\eta) = \inf_{\varphi} \mathcal{L}(\varphi, \eta, \lambda)$ over $E$. At each iteration, reduces the interval by the golden ratio $\rho = \frac{\sqrt{5}-1}{2} \approx 0.618$, requiring only 1 oracle call per step after initialization.
3. **Outer Bisection over $\lambda \in [0, \Lambda]$:** Evaluates the empirical constraint residual $R(\lambda) = \text{CVaR}_\alpha(-W_T^{\varphi_\lambda}) - c$. If $R(\lambda) > 0$, the multiplier is increased ($\lambda_{\text{low}} = \lambda$); if $R(\lambda) < 0$, it is decreased ($\lambda_{\text{high}} = \lambda$).
- **Convergence Rate (Theorem 4.4):** If outer iterations $N_\lambda \to \infty$ and $2^{N_\lambda} \rho^{N_\eta} \to 0$, the residual converges to zero and the computed control $\hat{\varphi}$ converges strongly in $L_{\mathbb{F}}^2$ to the unique optimal control $\varphi^*$.

## Required data

- **Asset Universe:** Continuous-time traded asset price $S_t$ (scalar stock or multi-asset basket) and cash/lending rate $r$.
- **Timeframe & Resolution:** Horizon $T=1.0$ year; finite-difference time discretization $\Delta t = 0.01$ ($100$ steps per year); intraday continuous or high-frequency updates.
- **Drift & Volatility Inputs:** Traded asset excess drift $\mu_t$ (e.g., $\mu = 0.08$) and volatility $\sigma_t$ (e.g., $\sigma = 0.20$); covariance matrix $\Sigma = \sigma \sigma^\top$ for multi-asset settings.
- **Endowment / Non-Traded Shock Data:** Background cash-flow rate $b_t$, traded covariance exposure $\beta_t$, and unhedgeable orthogonal variance parameter $\beta_t^\perp$ (e.g., $\beta^\perp = 0.02$).
- **State Grid Specification:** Wealth coordinate $W_t \in [w_{\min}, w_{\max}]$ discretized into $N_w = 101\text{--}201$ nodes with boundary padding $\pm 25\%$ beyond the $0.2\%$ and $99.8\%$ simulation quantiles.
- **Friction Parameters:** Quadratic trading rate penalty $\Lambda \in [0.001, 0.05]$ or power-law price impact coefficient $\Lambda_{3/2} \approx 0.0045$.

## Execution assumptions

- **Trading Mechanism:** Continuous or discrete-time feedback rebalancing $\varphi_t = f_t(W_t)$ mapped linearly from the HJB policy matrix.
- **Order Timing:** Instantaneous position updates in the frictionless case; finite signed trading rate control $\dot{\varphi}_t = \dot{\phi}_t S_t$ under transaction frictions.
- **Execution Cost Models Evaluated:**
  1. *Frictionless baseline:* Zero slippage, zero transaction fees.
  2. *Quadratic trading-rate regularization:* Objective penalty $\frac{1}{2}\Lambda \dot{\varphi}_t^2$ with $\Lambda = 0.01$.
  3. *Nonlinear square-root price impact:* Execution price $S_t^{\text{exe}} = S_t [ 1 + \Lambda_{3/2} \text{sign}(\dot{\varphi}_t) |\dot{\varphi}_t|^{1/2} ]$, directly reducing cash wealth by $\Lambda_{3/2} |\dot{\varphi}_t|^{3/2} dt$ with $\Lambda_{3/2} = 0.004472135955$.
- **Leverage & Shorting Constraints:** Action space bounded by $[\phi_{\min}, \phi_{\max}] = [-2.0, 2.0]$ times initial wealth.

## Evidence

### Source-reported

All quantitative figures below are directly reported by Hu, Pesenti, and Shi (arXiv:2608.20179v1, August 2026) and verified in the official codebase snapshot (`a00c290c93ba900c41ae68952b47bd0a7678616c`):

1. **Complete-Market Benchmark ($T=1.0, \mu=0.08, \sigma=0.20, \gamma=5.0, w_0=1.0, r=0, \beta^\perp=0$):**
   - *Merton Benchmark (Nonbinding, $c = -0.8600$):*
     - Constant dollar exposure: $\varphi_{\text{Merton}} = \frac{\mu}{\gamma \sigma^2} = \mathbf{0.4000}$.
     - Multiplier: $\hat{\lambda} = \mathbf{0.0000}$.
     - Expected terminal wealth: $\mathbb{E}[W_T] = \mathbf{1.0322}$.
     - Worst-tail mean wealth ($- \text{CVaR}_{0.95}$): $\mathbf{0.8671}$ (slack: $c - \text{CVaR} = +0.0071$).
   - *Binding CVaR Constraint ($c = -0.9400$, requiring worst-tail mean wealth $\ge 0.9400$):*
     - Calibrated multiplier: $\hat{\lambda}^* = \mathbf{0.0720}$; optimal threshold $\eta^* = \mathbf{-0.946330120}$.
     - Mean risky exposure: falls from $0.4000$ to $\mathbf{0.2981}$ (a **$25.5\%$ de-risking**).
     - Expected terminal wealth: $\mathbb{E}[W_T] = \mathbf{1.0242}$ (a minor **$0.78\%$ decline** from $1.0322$).
     - Out-of-Sample (50,000 paths, seed 1900013) worst-tail mean wealth: $\mathbf{0.9406}$ (empirical residual: $\mathbf{-6.133 \times 10^{-4}}$, strictly feasible).
     - State-dependent trajectory bifurcation: along favorable paths ending at $W_T^* \approx 1.311$, exposure rebounds toward the full Merton level $\approx \mathbf{0.400}$; along unfavorable paths ending at $W_T^* \approx 0.947$, exposure declines sharply to $\mathbf{0.068}$ late in the investment horizon.
2. **Incomplete-Market Setting with Nontraded Risk ($\beta^\perp = 0.02$):**
   - *Nonbinding ($c = -0.8600$):* Merton exposure remains $0.4000$; terminal loss CVaR shifts from $-0.8671$ to $-0.8620$ due to unhedgeable background variance.
   - *Binding ($c = -0.9400$):*
     - Calibrated multiplier increases to $\hat{\lambda}^* = \mathbf{0.1400}$ (nearly double the complete-market multiplier).
     - Mean risky exposure falls to $\mathbf{0.2549}$ (**$36.3\%$ below Merton** and **$14.5\%$ below complete market**).
     - Expected terminal wealth: drops by $\approx \mathbf{1.1\%}$ relative to the unconstrained policy.
     - Along unfavorable paths ending at $W_T^* \approx 0.956$, exposure after $t=0.6$ collapses to an average of $\mathbf{0.043}$.
3. **Quadratic Trading-Rate Regularization ($\Lambda = 0.01$):**
   - *Nonbinding ($c = -0.8600$):* Mean exposure $= \mathbf{0.3104}$, terminal loss CVaR $= \mathbf{-0.8839}$, $\hat{\lambda} = 0$.
   - *Binding ($c = -0.9400$):* Multiplier $\hat{\lambda} = \mathbf{0.06001}$, $\hat{\eta} = \mathbf{-0.947499}$.
     - Mean exposure drops from $0.3104$ to $\mathbf{0.2415}$.
     - Expected terminal wealth decreases from $1.0247$ to $\mathbf{1.0192}$.
     - Terminal loss CVaR reaches $\mathbf{-0.9413} \le -0.9400$.
4. **Square-Root Price Impact ($\Lambda_{3/2} = 0.004472135955$, costs deducted from wealth):**
   - *Nonbinding ($c = -0.8600$):* Mean exposure $= \mathbf{0.3500}$, terminal loss CVaR $= \mathbf{-0.8839}$, $\hat{\lambda} = 0$.
   - *Binding ($c = -0.9400$):*
     - Mean exposure falls from $0.3500$ to $\mathbf{0.2422}$.
     - Mean terminal wealth falls from $1.0260$ to $\mathbf{1.0180}$.
     - Out-of-sample terminal loss CVaR: $\mathbf{-0.9409} \le -0.9400$ (feasible).
     - State-dependent liquidations: trading rate $\dot{\varphi}_t$ turns negative across intermediate intervals along unfavorable paths ($W_T \approx 0.947$) to actively dump exposure as downside risk intensifies.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- None identified in the reviewed paper; absence is not evidence of no negative result.
- Authors emphasize that when the CVaR constraint binds aggressively ($c \le -0.96$), optimal exposure in adverse states approaches zero, locking the portfolio into cash and causing severe path-dependent cash drag that permanently eliminates recovery potential if a sharp mean reversion follows.
- In the presence of nonlinear square-root price impact, the controlled state dynamics become non-affine in trading speed ($|\dot{\varphi}|^{3/2}$), which breaches the formal convexity assumptions; while numerical convergence succeeds under the tested calibration, global convergence guarantees do not hold theoretically for arbitrary illiquid asset environments.

## Falsification plan

1. **Downside Tail Preservation under Non-Gaussian Heavy Tails:** Test the calibrated feedback policy against Student-$t$ ($\nu=3$) and Kou double-exponential jump-diffusion innovations. If discrete price gaps bypass the continuous HJB de-risking path and generate an out-of-sample terminal loss CVaR exceeding $c$ by more than $3\%$, the continuous diffusion assumption is falsified and requires jump-adapted PIDE control.
2. **Interim Drawdown vs. Terminal CVaR Decoupling:** While the source reports that interim diagnostic $\text{CVaR}_{0.95}(-W_t)$ remained below $c$ for all $t < T$ in zero-rate calibrations, introduce non-zero interest rates ($r = 5\%$) and volatile cash outflows ($b < 0$). If interim drawdown exceeds the risk budget by $>15\%$ before recovering at $T$, the terminal-only CVaR formulation is insufficient for intra-horizon solvency mandates.
3. **Execution Delay and Stale Policy Stress:** Impose execution latency $\tau \in [1, 5]$ time steps between state observation $W_t$ and order execution $\varphi_{t+\tau}$. If latency-induced tracking errors increase terminal loss CVaR beyond $-0.92$ under the $c=-0.94$ mandate, the policy requires an explicit latency state augmentation.
4. **Rejection Criterion:** Falsify and reject the policy if out-of-sample terminal loss CVaR violates the pre-set limit $c$ by more than $1.0\%$ across $50,000$ Monte Carlo paths, or if expected terminal wealth drops below the risk-free return $w_0 e^{rT}$.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Porting Mechanism to Crypto Perpetual Desks:** In crypto perpetual futures (e.g., BTC/USDT, ETH/USDT on Binance or Hyperliquid), traders face hard liquidation thresholds set by exchange maintenance margin requirements. The terminal CVaR constraint directly maps to an exchange bankruptcy probability constraint.
- **Nontraded Risk Correspondence:** The background risk shock $\beta^\perp dB_t^\perp$ perfectly represents unhedgeable basis risk, cross-venue funding rate divergence, oracle desynchronization, and depeg risk in stablecoin collateral (e.g., USDe, FDUSD).
- **Asymmetric De-risking Utility in Crypto:** Conventional volatility-targeting strategies de-risk symmetrically after volatility spikes, often selling at the exact bottom of liquidation wicks. The state-dependent HJB policy de-risks only along adverse wealth paths ($W_t < w_0$), preserving upside participation during explosive bull runs.
- **Crypto-Specific Frictions:**
  - *Funding Rates:* Continuous 8-hour funding rates act as an asymmetric drift penalty $b_t = -F_t \varphi_t$ that must be integrated directly into the wealth dynamics.
  - *Liquidation Spreads:* Exchange ADL (auto-deleveraging) and liquidation penalties create discontinuous terminal jumps that necessitate replacing the smooth loss function $\ell(w) = -w$ with a barrier penalty $\ell(w) = -w + K \cdot \mathbb{I}_{\{w \le w_{\text{liq}}\}}$."

## Limitations

- **Single Traded Asset Calibration:** The numerical experiments focus on a scalar risky asset ($m=1$) with a one-dimensional wealth coordinate; high-dimensional multi-asset extensions ($m \ge 20$) suffer from the curse of dimensionality under grid-based PDE solvers, requiring deep neural network BSDE or policy gradient solvers.
- **Terminal-Only Constraint Horizon:** Risk is constrained strictly at maturity $T$; intra-horizon pathwise drawdown limits are not explicitly enforced in the optimization objective.
- **Known Stationary Drift & Volatility:** The HJB derivation assumes known constant or deterministic parameters $(\mu, \sigma)$; parameter estimation uncertainty, Bayesian drift filtering, and stochastic volatility (Heston / rough Bergomi) are omitted.

## Implementation status

`not-implemented` in the quantitative production stack.

## Adoption boundary

Research capture only. A record being present in this repository does not constitute authorization for deployment, implementation in PyBroker/Nautilus, or allocation of capital in paper, testnet, or live trading.

## Related Wiki records

- `[[quant/expected-shortfall-and-risk-of-ruin-2026-08-28]]`
- `[[quant/fractional-kelly-2026-08-28]]`
- `[[quant/volatility-targeting-risk-parity-constrained-2026-08-28]]`
- `[[quant/execution-impact-capacity-almgren-square-root-2026-08-28]]`
- `[[quant/crypto-perpetual-optimal-liquidation-funding-rate-hjb-2026-09-02]]`

## Sources

1. Anran Hu, Silvana M. Pesenti, and Xiaofei Shi, *"Dynamic Portfolio Optimization under CVaR Constraints"*, arXiv preprint `arXiv:2608.20179v1 [math.OC]`, August 24, 2026. DOI: [10.48550/arXiv.2608.20179](https://doi.org/10.48550/arXiv.2608.20179). Stable URL: [https://arxiv.org/abs/2608.20179](https://arxiv.org/abs/2608.20179).
2. Xiaofei Shi, official code repository `xf-shi/Dynamic-Portfolio-under-CVaR`, commit [`a00c290c93ba900c41ae68952b47bd0a7678616c`](https://github.com/xf-shi/Dynamic-Portfolio-under-CVaR/commit/a00c290c93ba900c41ae68952b47bd0a7678616c), August 12, 2026. Stable URL: [https://github.com/xf-shi/Dynamic-Portfolio-under-CVaR](https://github.com/xf-shi/Dynamic-Portfolio-under-CVaR).
