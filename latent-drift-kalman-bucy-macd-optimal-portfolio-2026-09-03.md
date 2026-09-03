---
schema: strategy-research-record-v1
title: "Portfolio Optimization under Fast and Slow Latent Mean-Reverting and Momentum Drift: Endogenous Emergence of Continuous-Time MACD Trading Signals"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - stochastic-control
  - partial-information
  - kalman-bucy-filter
  - macd
  - latent-factor
  - mean-reversion
  - momentum
  - hjb-equation
  - utility-maximization
  - exponential-moving-average
status: research-only
confidence: medium
source_as_of: 2026-07-02
sources:
  - "https://arxiv.org/abs/2607.01705"
  - "https://doi.org/10.48550/arXiv.2607.01705"
  - "https://arxiv.org/html/2607.01705v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Portfolio Optimization under Fast and Slow Latent Mean-Reverting and Momentum Drift: Endogenous Emergence of Continuous-Time MACD Trading Signals

## Provenance

- **Primary paper:** Dannin J. Eccles and Roger Lee, *Portfolio Optimization under Fast and Slow Latent Mean-Reverting and Momentum Drift*, arXiv preprint `arXiv:2607.01705v1 [q-fin.MF]`, submitted July 2, 2026. DOI: `10.48550/arXiv.2607.01705`.
- **Author affiliations:**
  - Dannin J. Eccles: Department of Mathematics, University of Chicago, Chicago, IL, USA (`deccles@uchicago.edu`).
  - Roger Lee: Department of Mathematics, University of Chicago, Chicago, IL, USA (`rogerlee@math.uchicago.edu`).
- **Primary source text:** Full-text HTML5 article and mathematical derivations directly retrieved and verified from `https://arxiv.org/html/2607.01705v1` and `https://arxiv.org/abs/2607.01705` (July 2026 snapshot).
- **License:** arXiv.org perpetual non-exclusive license.
- **Source/data as-of:** 2026-07-02.
- **Source-identity deduplication:** Repository-wide inspection confirmed zero existing records for `2607.01705`, `Dannin J. Eccles`, `Roger Lee`, or `latent mean-reverting and momentum drift`. Existing MACD records in this repository are fundamentally distinct:
  - `macd-trend_ohlcv-2026-08-31.md` captures a basic heuristic OHLCV crossover rule without mathematical drift modeling or dynamic control.
  - `volume-price-adjusted-macd-sensitivity-calibration-2026-09-02.md` (Lin et al., arXiv:2604.26063) examines empirical volume-weighted price adjustments and threshold tuning on equity ETFs.
  The Eccles & Lee (2026) paper provides the first continuous-time stochastic control derivation showing that a Moving Average Convergence Divergence (MACD)-type divergence signal emerges endogenously as the optimal filter for unobserved drift driven by fast and slow latent factors under partial information.

## Economic mechanism

### Source-reported

In continuous-time portfolio choice, classical models often assume that the drift (expected return) of an asset is either a known constant (Merton model) or an observable process. In real financial markets, investors observe only realized market prices, while the underlying economic drift is driven by multiple unobservable, time-varying components:
1. **Slow-moving persistent factor ($S_t$):** Reflects long-term macro fundamentals, structural valuation anchors, monetary policy stances, or corporate earnings cycles.
2. **Fast-moving transitory factor ($F_t$):** Captures short-term speculative momentum, order-flow imbalances, institutional repositioning, or sentiment shocks.

Because the investor cannot directly observe either factor, trading decisions must be strictly adapted to the filtration $\mathbb{F}^P$ generated solely by the observed price path $P = (P_t)_{0 \le t \le T}$.

Key theoretical findings established by Eccles & Lee (2026) include:
- **Kalman-Bucy Filtering & Continuous-Time MACD Decomposition (Theorem 3.1):** When asset prices follow a linear-Gaussian diffusion coupled to the fast factor ($dP_t = (\lambda_p F_t - \kappa_p P_t)dt + \sigma_p dW_t^P$), the optimal filtered estimate of the unobserved drift component $\hat{F}_t = \mathbb{E}[F_t \mid \mathscr{F}_t^P]$ decomposes analytically into:
  - A deterministic trend/initial condition component $D_t$;
  - A fast-slow exponential moving average (EMA) divergence signal $\mathfrak{S}_t(\alpha, \beta; \kappa_f, \kappa_s) = \alpha_t \mathcal{E}_t(\kappa_f, \alpha) - \beta_t \mathcal{E}_t(\kappa_s, \beta)$;
  - A deterministic finite-horizon Volterra correction operator $\mathfrak{B}(t; \mathfrak{S})$.
- **Endogenous Emergence without Heuristic Imposition:** Unlike empirical technical analysis—where MACD is postulated ad-hoc as the difference between 12-day and 26-day moving averages—the fast-slow EMA divergence emerges here endogenously as the unique mathematical representation of the Kalman-Bucy filter under two-scale latent drift.
- **Unified Feedback Architecture Across Utility Classes:** Solving the Hamilton-Jacobi-Bellman (HJB) equations for logarithmic ($U(\mathfrak{w}) = \log \mathfrak{w}$), power ($U(\mathfrak{w}) = \frac{\mathfrak{w}^{1-q}}{1-q}$), and exponential ($U(\mathfrak{w}) = -e^{-p\mathfrak{w}}$) utility demonstrates that all three optimal feedback policies depend directly on the net filtered drift $m(\mathfrak{p}, \mathfrak{f}) = \lambda_p \hat{F}_t - \kappa_p P_t$.

### Research interpretation

From an alpha-generation and quantitative strategy perspective, this framework bridges continuous-time stochastic control and technical momentum/mean-reversion indicators:

1. **Rigorous Foundation for MACD Parameters:** Standard technical analysis treats MACD lookback periods (e.g., $(12, 26, 9)$) as arbitrary convention. Under the Eccles-Lee model:
   - The fast EMA decay parameter $\kappa_f$ corresponds to the reversion speed of short-term sentiment/momentum shocks.
   - The slow EMA decay parameter $\kappa_s$ corresponds to the persistence rate of macro/fundamental regimes.
   - The moving-average weights $\alpha_t, \beta_t$ are not fixed constants; they depend dynamically on the instantaneous Kalman filter gain $K_t$ and the posterior estimation error covariance $\boldsymbol{\Sigma}_t$.
2. **Volterra Memory Correction:** Standard discrete MACD ignores the initial-state conditioning and boundary effects of finite holding horizons. The continuous-time Volterra correction term $\mathfrak{B}(t; \mathfrak{S})$ accounts for the non-Markovian accumulation of historical price paths over finite trading periods.
3. **Intertemporal Hedging Demand:** For power-utility investors ($q \neq 1$) and exponential-utility investors ($p > 0$), the optimal policy augments the myopic MACD signal with an intertemporal hedging demand (via the Riccati / linear ODE solutions $\boldsymbol{Q}_t$ and $\boldsymbol{b}_t$) that explicitly hedges fluctuations in the estimation uncertainty of future drift.

## Signal

### 1. Underlying Model Dynamics (Linear-Gaussian Diffusion)

The underlying asset price $P_t$ and latent drift vector $\boldsymbol{\Theta}_t = (F_t, S_t)^\top$ satisfy the continuous-time SDE system:
$$dP_t = (\lambda_p F_t - \kappa_p P_t) dt + \sigma_p dW_t^P$$
$$d\boldsymbol{\Theta}_t = (\mu - \kappa \boldsymbol{\Theta}_t) dt + \sigma d\mathbf{W}_t$$
where:
- $\mu = (\mu_f, \mu_s)^\top \in \mathbb{R}^2$.
- $\kappa = \begin{pmatrix} \kappa_f & -\lambda_f \\ 0 & \kappa_s \end{pmatrix}$, with coupling parameter $\lambda_f > 0$ and mean-reversion rates $\kappa_f > \kappa_s \ge 0$.
- $\sigma = \begin{pmatrix} \sigma_f & 0 \\ 0 & \sigma_s \end{pmatrix}$, with volatilities $\sigma_f > 0, \sigma_s > 0$.
- $\sigma_p > 0$ is the observable price volatility.
- $\kappa_p \ge 0$ is the direct price mean-reversion parameter ($\kappa_p = 0$ corresponds to pure momentum drift).
- $\lambda_p > 0$ transmits the fast latent factor $F_t$ into price drift.
- $\mathbf{W}_t = (W_t^F, W_t^S)^\top$ is a standard 2D Brownian motion, and $W^P$ is a 1D Brownian motion with instantaneous cross-correlation $\rho = (\rho_f, \rho_s)^\top$ satisfying $\|\rho\|_2 = \sqrt{\rho_f^2 + \rho_s^2} < 1$.

### 2. Kalman-Bucy Filtering Equations

Let $\check{P}_t = P_t / \sigma_p$ be the normalized price process. The innovation Brownian motion $\nu_t$ with respect to the price filtration $\mathbb{F}^P$ is:
$$d\nu_t = \frac{1}{\sigma_p} \left[ dP_t - (\lambda_p \hat{F}_t - \kappa_p P_t) dt \right]$$
The conditional mean $\hat{\boldsymbol{\Theta}}_t = (\hat{F}_t, \hat{S}_t)^\top = \mathbb{E}[\boldsymbol{\Theta}_t \mid \mathscr{F}_t^P]$ and conditional covariance $\boldsymbol{\Sigma}_t = \mathbb{E}[(\boldsymbol{\Theta}_t - \hat{\boldsymbol{\Theta}}_t)(\boldsymbol{\Theta}_t - \hat{\boldsymbol{\Theta}}_t)^\top \mid \mathscr{F}_t^P]$ evolve according to:
$$d\hat{\boldsymbol{\Theta}}_t = (\mu - \kappa \hat{\boldsymbol{\Theta}}_t) dt + K_t d\nu_t, \quad \hat{\boldsymbol{\Theta}}_0 \in \mathbb{R}^2$$
$$\dot{\boldsymbol{\Sigma}}_t = -\kappa \boldsymbol{\Sigma}_t - \boldsymbol{\Sigma}_t \kappa^\top + \sigma \sigma^\top - K_t K_t^\top, \quad \boldsymbol{\Sigma}_0 = \hat{\Sigma}_0 > 0$$
where the Kalman gain vector $K_t \in \mathbb{R}^2$ is given by:
$$K_t = \sigma \rho + \frac{\lambda_p}{\sigma_p} \boldsymbol{\Sigma}_t e_1, \quad e_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$

### 3. Continuous-Time MACD Filter Representation (Theorem 3.1)

Let $v_t = K_t / \sigma_p = \frac{\sigma \rho}{\sigma_p} + \frac{\lambda_p}{\sigma_p^2} \boldsymbol{\Sigma}_t e_1$ be the drift volatility state vector. The filtered fast factor $\hat{F}_t$ admits the exact representation:
$$\hat{F}_t = D_t + \mathfrak{S}_t(\alpha, \beta; \kappa_f, \kappa_s) + \mathfrak{B}(t; \mathfrak{S}(\alpha, \beta; \kappa_f, \kappa_s))$$
where:
1. **Deterministic Drift Component:**
   $$D_t = e_1^\top e^{-\kappa t} \hat{\boldsymbol{\Theta}}_0 + \int_0^t e_1^\top e^{-\kappa(t-s)} \mu \, ds$$
2. **Fast-Slow Exponential Divergence (MACD Core Signal):**
   $$\mathfrak{S}_t(\alpha, \beta; \kappa_f, \kappa_s) = \alpha_t \mathcal{E}_t(\kappa_f, \alpha) - \beta_t \mathcal{E}_t(\kappa_s, \beta)$$
   with continuous-time EMA price filter:
   $$\mathcal{E}_t(\gamma, \delta) = \int_0^t e^{-\gamma(t-s)} \delta_s P_s \, ds$$
   and time-varying weights:
   $$\alpha_t = v_t^{(1)} - \frac{\lambda_f}{\kappa_f - \kappa_s} v_t^{(2)}, \qquad \beta_t = \frac{\lambda_f}{\kappa_f - \kappa_s} v_t^{(2)}$$
3. **Deterministic Volterra Memory Operator:**
   $$\mathfrak{B}(t; f, g) = \int_0^t e_1^\top e^{-\kappa(t-s)} \mathbf{M}_s \mathbf{Y}(s; f, g) \, ds$$
   where $\mathbf{Y}(t) = (Y_f(t), Y_s(t))^\top$ is the unique solution to the linear differential equation:
   $$\dot{\mathbf{Y}}_t = (\mathbf{M}_t - \kappa) \mathbf{Y}_t + \mathbf{M}_t \begin{pmatrix} f(t) \\ g(t) \end{pmatrix}, \quad \mathbf{Y}_0 = 0$$
   with matrix $\mathbf{M}_t = \frac{\lambda_p}{\sigma_p} K_t - \kappa_p \mathbf{I}$.

### 4. Optimal Portfolio Policies Across Utilities

Let $\mathfrak{w} > 0$ denote current portfolio wealth, $\mathfrak{p} = P_t$ current asset price, and $x_t = (\mathfrak{p}, \hat{F}_t, \hat{S}_t)^\top \in \mathbb{R}^3$ the augmented price-drift state vector. The effective drift signal entering the first-order condition is:
$$m(\mathfrak{p}, \mathfrak{f}) = \lambda_p \hat{F}_t - \kappa_p P_t$$
where $\mathfrak{f} = \hat{F}_t$. The optimal position $\varphi_U^*(t, \mathfrak{w}, \mathfrak{p}, \boldsymbol{\vartheta})$ (number of shares held in the risky asset) is:

- **Logarithmic Utility ($U(\mathfrak{w}) = \log \mathfrak{w}$):**
  $$\varphi_{\log}^*(t, \mathfrak{w}, \mathfrak{p}, \boldsymbol{\vartheta}) = \frac{\mathfrak{w}}{\sigma_p^2} m(\mathfrak{p}, \mathfrak{f}) = \frac{\mathfrak{w}}{\sigma_p^2} (\lambda_p \hat{F}_t - \kappa_p P_t)$$
  The myopic allocation: position scale is directly proportional to wealth $\mathfrak{w}$, inversely proportional to return variance $\sigma_p^2$, and driven by the net filtered drift containing the continuous-time MACD signal.
- **Power Utility ($U(\mathfrak{w}) = \frac{\mathfrak{w}^{1-q}}{1-q}, \; q > 0, q \neq 1$):**
  $$\varphi_{\mathrm{pow}}^*(t, \mathfrak{w}, \mathfrak{p}, \boldsymbol{\vartheta}) = \frac{\mathfrak{w}}{q \sigma_p^2} \left[ m(\mathfrak{p}, \mathfrak{f}) + \boldsymbol{v}_t^\top (2 \boldsymbol{Q}_t x + \boldsymbol{b}_t) \right]$$
  where $\boldsymbol{v}_t = (\sigma_p, K_t)^\top$, and $(\boldsymbol{Q}_t, \boldsymbol{b}_t, f(t))$ solves the backward matrix Riccati ODE system (Proposition 4.2). The second term represents intertemporal hedging demand against latent factor estimation risk.
- **Exponential Utility ($U(\mathfrak{w}) = -e^{-p\mathfrak{w}}, \; p > 0$):**
  $$\varphi_{\exp}^*(t, \mathfrak{w}, \mathfrak{p}, \boldsymbol{\vartheta}) = \frac{1}{p \sigma_p^2} m(\mathfrak{p}, \mathfrak{f}) - \frac{\boldsymbol{v}_t^\top (2 \boldsymbol{Q}_t x + \boldsymbol{b}_t)}{\sigma_p}$$
  where $(\boldsymbol{Q}_t, \boldsymbol{b}_t, f(t))$ solves a backward linear ODE system (Proposition 4.3). Absolute allocation is independent of wealth, scaled inversely by absolute risk aversion $p$.

## Required data

- **Instrument:** Any liquid continuous-time financial asset (equities, index futures, FX pairs, or crypto perpetual futures).
- **Timeframe:** High-frequency or regularly spaced discrete prices ($P_t$), aggregated at 1-minute, 5-minute, or 1-hour intervals for numerical discretization of the Kalman-Bucy filter.
- **Required inputs:**
  - Mid-price or trade execution price series $P_t$.
  - Calibrated model parameters: $\sigma_p, \sigma_f, \sigma_s, \kappa_p, \kappa_f, \kappa_s, \lambda_p, \lambda_f, \rho_f, \rho_s, \mu_f, \mu_s$.
  - Prior distribution of the unobserved state: initial conditional mean $\hat{\boldsymbol{\Theta}}_0$ and initial covariance $\hat{\Sigma}_0$.
- **Point-in-time constraints:** $\hat{F}_t$ and $\hat{S}_t$ are causal filtered expectations conditioned strictly on $\mathscr{F}_t^P = \sigma(P_s, 0 \le s \le t)$; no forward price information is utilized.
- **Missing-data handling:** Under the continuous Kalman-Bucy formulation, missing observation bars expand the covariance matrix $\boldsymbol{\Sigma}_t$ according to the Lyapunov drift $\dot{\boldsymbol{\Sigma}}_t = -\kappa \boldsymbol{\Sigma}_t - \boldsymbol{\Sigma}_t \kappa^\top + \sigma \sigma^\top$ until the next price observation arrives.

## Execution assumptions

- **Trading friction:** The primary theoretical derivation assumes a frictionless market with zero interest rates, continuous rebalancing, and zero bid-ask spread or transaction costs.
- **Continuous rebalancing:** The portfolio process $\varphi_t$ is assumed to be continuously adjusted. Discrete execution requires time-discretization via Euler-Maruyama or Runge-Kutta stepping.
- **Order type:** Continuous passive or midpoint execution. In real markets, discrete rebalancing intervals ($\Delta t$) incur transaction costs that require band-based regularization (e.g., Soner-Shreve or Whalley-Wilmott no-trade bands).
- **Borrowing / Shorting:** Unconstrained short selling and unconstrained cash borrowing are assumed in the unconstrained self-financing wealth equation $dV_t = \varphi_t dP_t$.

## Evidence

### Source-reported

All analytical claims below are derived and proven by Dannin J. Eccles and Roger Lee (arXiv:2607.01705v1, July 2, 2026):
1. **Mathematical Equivalence to MACD (Theorem 3.1):** The authors analytically prove that the fast-factor filter $\hat{F}_t$ is driven by the fast-slow exponential divergence $\mathfrak{S}_t = \alpha_t \mathcal{E}_t(\kappa_f, \alpha) - \beta_t \mathcal{E}_t(\kappa_s, \beta)$, establishing the first mathematical derivation of MACD as an optimal filter rather than an empirical heuristic.
2. **Explicit Verification of Optimality (Theorem 5.1):**
   - For **logarithmic utility**, the candidate control $\varphi_{\log}^*$ is admissible and achieves the value function $\psi_{\log} = \mathscr{V}_{\log}$ for all finite horizons $T < \infty$.
   - For **exponential utility**, $\varphi_{\exp}^*$ is admissible and achieves $\psi_{\exp} = \mathscr{V}_{\exp}$ for all finite horizons $T < \infty$.
   - For **power utility**, $\varphi_{\mathrm{pow}}^*$ is admissible and optimal on all horizons $T$ for which the matrix Riccati system (Eq. 20) admits a $C^1$ solution on $[0, T]$.
3. **Absence of Empirical Backtest:** The paper is an analytical mathematical finance contribution establishing structural representation, stochastic control, and verification theorems. No historical backtest, Sharpe ratio, or simulated PnL figures are reported by the authors.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Parameter Sensitivity & Calibration Uncertainty:** The Kalman-Bucy filter requires prior knowledge or econometric estimation of 11 continuous parameters ($\sigma_p, \sigma_f, \sigma_s, \kappa_p, \kappa_f, \kappa_s, \lambda_p, \lambda_f, \rho_f, \rho_s, \mu$). In real financial data, latent factor drifts are notoriously difficult to estimate with high precision; misestimation of adjustment speeds $\kappa_f, \kappa_s$ leads to phase misalignment in the MACD divergence signal.
- **Finite Horizon vs. Ergodic Steady State:** In the finite-horizon setting, the Volterra correction $\mathfrak{B}(t; \mathfrak{S})$ and time-dependent Kalman weights $\alpha_t, \beta_t$ do not simplify to static constant weights until the Riccati equation reaches algebraic steady state ($\dot{\boldsymbol{\Sigma}} \to 0$). Applying static textbook MACD weights without accounting for transient covariance dynamics introduces tracking errors.
- **Frictionless Rebalancing Collapse:** In the presence of linear transaction costs (proportional bid-ask spread), continuous rebalancing generates infinite turnover and negative net returns, necessitating a no-trade boundary around the optimal signal.

## Falsification plan

To falsify the hypothesis that the Eccles-Lee two-scale Kalman filter outperforms standard empirical MACD rules:

1. **EM-Algorithm Latent Calibration Test:** Calibrate the continuous-time parameter vector $\boldsymbol{\theta} = (\kappa_f, \kappa_s, \lambda_p, \lambda_f, \sigma_p, \sigma_f, \sigma_s, \rho)$ via expectation-maximization (EM) or Kalman quasi-maximum likelihood on rolling 1-year windows across S&P 500 equity futures and Bitcoin perpetual contracts.
   - *Failure rule:* If the estimated adjustment speed ratio $\kappa_f / \kappa_s \le 1.0$ (no timescale separation between fast and slow factors), the model's structural premise is falsified.
2. **Out-of-Sample Predictive Edge Test (Signal vs. Textbook MACD):** Compare the out-of-sample directional Information Coefficient (IC) of the filtered drift $m(\mathfrak{p}, \mathfrak{f}) = \lambda_p \hat{F}_t - \kappa_p P_t$ against a standard $(12, 26)$ discrete MACD indicator on out-of-sample 1-hour and 1-day bars over 2020–2026.
   - *Failure rule:* If the Eccles-Lee filtered drift signal achieves an out-of-sample IC statistically indistinguishable from or lower than textbook MACD ($p > 0.05$ via Diebold-Mariano test), the theoretical Kalman-Volterra refinement provides no empirical edge.
3. **Transaction Cost Ablation & Turnoff Threshold:** Introduce realistic transaction costs (1 bps maker, 5 bps taker for crypto perps; 1 tick for index futures) and test discrete rebalancing intervals $\Delta t \in \{1\text{m}, 5\text{m}, 15\text{m}, 1\text{h}\}$.
   - *Failure rule:* If net Sharpe ratio after transaction costs drops below zero across all rebalancing cadences $\Delta t$, the unregularized continuous strategy is non-viable without explicit friction modeling.

## Crypto portability

**Portability Classification: Adapted / Unproven.**

The theoretical mechanism is developed for a general diffusion asset and ports conceptually to cryptocurrency markets, but requires specific adaptations:
1. **Perpetual Futures Basis & Funding Rate Integration:** In crypto perpetuals, price drift is heavily influenced by funding rate payments ($r_{\mathrm{fund}}$). If the fast latent factor $F_t$ pushes the perp price above spot index, the resulting funding cost must be subtracted from the effective drift $m(\mathfrak{p}, \mathfrak{f})$ to prevent holding unprofitable momentum into funding payment timestamps (every 8 or 1 hour).
2. **Volatilities and Jumps:** Crypto assets exhibit extreme fat tails and discontinuous price jumps, violating the Gaussian Brownian motion assumption ($W_t^P$). The Kalman-Bucy filter is optimal only under Gaussian noise; in jump-diffusion regimes, an adaptive nonlinear filter (e.g., particle filter or robust Kalman filter) would be required.
3. **24/7 Continuous Trading:** The absence of weekend or overnight exchange closures eliminates the artificial boundary and warm-up discontinuities of equity markets, making continuous Kalman-Bucy filtering more naturally aligned with crypto trading sessions.

## Limitations

- **Purely Analytical Framework:** The primary source contains mathematical proofs and verification theorems, but no empirical backtest or live trading performance data.
- **Gaussian Noise Assumption:** Assumes asset returns and latent factor innovations are purely Brownian, ignoring stochastic volatility, jumps, and leverage effects.
- **Frictionless Market Formulation:** Does not incorporate bid-ask spreads, transaction costs, price impact, or discrete execution latency.
- **Latent Parameter Identifiability:** Continuous-time calibration of coupled latent factor diffusions from price observations alone is susceptible to identification degeneracy and parameter drift.

## Implementation status

- `implementation_status: not-implemented`
- This record captures the upstream mathematical stochastic control derivation only.
- No implementation has been created in PyBroker, NautilusTrader, paper trading, testnet, or live trading workflows.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Research capture does not authorize strategy implementation, paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- `[[quant/volume-price-adjusted-macd-sensitivity-calibration-2026-09-02]]` — Heuristic volume-weighted and sensitivity-calibrated MACD extension (arXiv:2604.26063).
- `[[quant/macd-trend_ohlcv-2026-08-31]]` — Baseline discrete OHLCV MACD crossover rule.
- `[[quant/futures-trend-following-autocorrelation-drift-decomposition-2026-09-02]]` — Multi-horizon continuous-time drift and autocorrelation decomposition for trend-following (arXiv:2607.19497).
- `[[quant/hawkes-driven-otc-market-making-volterra-riccati-2026-09-01]]` — Volterra integral and Riccati ODE stochastic control systems in market microstructure.
- `[[quant/dynamic-portfolio-optimization-cvar-stochastic-control-hjb-2026-09-02]]` — HJB stochastic control framework for dynamic portfolio optimization.

## Sources

- **Primary paper:** Dannin J. Eccles and Roger Lee, *Portfolio Optimization under Fast and Slow Latent Mean-Reverting and Momentum Drift*, arXiv preprint `arXiv:2607.01705v1 [q-fin.MF]`, submitted July 2, 2026. DOI: `10.48550/arXiv.2607.01705`.
  - Abstract & metadata: https://arxiv.org/abs/2607.01705
  - Full-text HTML5: https://arxiv.org/html/2607.01705v1
  - PDF version: https://arxiv.org/pdf/2607.01705v1
- **Foundational literature cited within primary source:**
  - X. Chen and R. Lee (2023), *EMA-type trading strategies maximize utility under partial information*, Frontiers of Mathematical Finance 2 (1), 124–140. DOI: `10.3934/fmf.2023005`.
  - P. Lakner (1995), *Utility maximization with partial information*, Stochastic Processes and their Applications 56 (2), 247–273.
  - P. Lakner (1998), *Optimal trading strategy for an investor: the case of partial information*, Stochastic Processes and their Applications 76 (1), 77–97.
  - T. S. Kim and E. Omberg (1996), *Dynamic nonmyopic portfolio behavior*, The Review of Financial Studies 9 (1), 141–161.
  - I. Karatzas and X. Zhao (2001), *Bayesian adaptive portfolio optimization*, Option Pricing, Interest Rates and Risk Management, Cambridge University Press, 632–669.
  - M. Lorig, Z. Zhou, and B. Zou (2019), *A mathematical analysis of technical analysis*, Applied Mathematical Finance 26 (1), 38–68.
  - J. Xiong (2008), *An Introduction to Stochastic Filtering Theory*, Oxford University Press.
