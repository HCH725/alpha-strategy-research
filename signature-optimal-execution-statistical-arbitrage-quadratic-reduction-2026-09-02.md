---
schema: strategy-research-record-v1
title: "Signature-Based Optimal Execution for Statistical Arbitrage: Truncated Path Features, Quadratic Reduction Theorem, and Static Speed Policy Optimization"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - optimal-execution
  - path-signatures
  - rough-paths
  - quadratic-programming
  - pairs-trading
  - temporary-impact
status: research-only
confidence: high
source_as_of: 2026-06-30
sources:
  - "Gianmarco Morbelli, Sven Karbach, Mike Derksen, 'Signature-Based Optimal Execution for Statistical Arbitrage with Path-Dependent Trading Signals', arXiv:2606.31387v1 [q-fin.TR], June 30, 2026. DOI: 10.48550/arXiv.2606.31387. https://arxiv.org/abs/2606.31387"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Signature-Based Optimal Execution for Statistical Arbitrage: Truncated Path Features, Quadratic Reduction Theorem, and Static Speed Policy Optimization

## Provenance

- **Primary Source:** Gianmarco Morbelli, Sven Karbach, and Mike Derksen, *"Signature-Based Optimal Execution for Statistical Arbitrage with Path-Dependent Trading Signals"*, arXiv preprint `arXiv:2606.31387v1 [q-fin.TR]`, submitted June 30, 2026. DOI: [10.48550/arXiv.2606.31387](https://doi.org/10.48550/arXiv.2606.31387). Full text: [https://arxiv.org/abs/2606.31387](https://arxiv.org/abs/2606.31387).
- **Primary Subject Area:** Trading and Market Microstructure (`q-fin.TR`).
- **Context:** Statistical arbitrage and pairs-trading strategies typically decouple signal generation (e.g., $z$-score threshold triggers) from execution (e.g., TWAP/VWAP or heuristic unwind). However, relative-value alpha decays on the same time scale as temporary market impact, inventory risk, and dollar-neutrality constraints. Classical optimal execution models (Almgren-Chriss, Cartea-Jaimungal) solve for execution speed but typically condition only on clock time and remaining inventory or low-dimensional Markov states rather than full path history. Morbelli, Karbach, and Derksen bridge this gap by representing both the predictive alpha process $\alpha_t$ and the trading speed control $v_t$ as linear functionals on the truncated signature of a time-augmented information path $\mathbf{Z}$.

## Economic mechanism

### Source-reported

1. **Coupled Signal-Aware Execution:** Relative-value mispricings are path-dependent; the trajectory by which a spread diverges (e.g., rapid jump vs. slow drift, persistent divergence vs. transient dislocation captured by higher-order signature terms like Lévy area) conveys critical information about expected alpha decay and optimal execution speed.
2. **Integrated Multi-Objective Optimization:** Traders balance instantaneous predictive reward $Q_t^\top \alpha_t$, quadratic temporary market impact $v_t^\top \tilde{\Lambda} v_t$, running mark-to-market inventory risk $\phi Q_t^\top \Sigma Q_t$, net dollar-neutrality penalty $\eta (Q_t^\top P_t)^2$, and soft terminal liquidation penalty $\gamma \|Q_T\|^2$.
3. **Quadratic Reduction via Signature Algebra:** Because both the signal and the control lie on the truncated signature tensor basis $\mathcal{T}^{\le N}(\mathbb{R}^{d_z})$, the entire continuous-time path-dependent stochastic control problem collapses into a static finite-dimensional concave quadratic program in the vectorized policy parameter $\theta = \operatorname{vec}(B)$.

### Research interpretation

The falsifiable thesis is that **jointly optimizing execution speed directly on the path signature basis yields superior return on turnover (ROT) and lower execution friction than separating $z$-score signal generation from exogenous execution schedules**:
- Higher-order signature features (e.g., level-2 antisymmetric Lévy area $\mathbb{A}_t = \frac{1}{2}(\mathbb{Z}_t^{1,2} - \mathbb{Z}_t^{2,1})$ and time-weighted price increments $\mathbb{Z}_t^{0,i} - \mathbb{Z}_t^{i,0}$) enable the speed policy $v_t = B x_t$ to modulate trading aggression based on whether price dislocations are transient or structural, without solving high-dimensional PDEs/HJB equations at runtime.
- The off-line estimation of deterministic moment tensors $A$ and $b$ enables real-time execution via a single static matrix-vector product $v_t = B^* x_t$, eliminating live dynamic programming overhead.

## Signal

### 1. Market Path and Truncated Signature Features

Let $P_t = (P_t^{(1)}, \dots, P_t^{(n)})^\top$ denote unaffected mid-prices of $n$ assets. Construct the time-augmented information stream $Z_t \in \mathbb{R}^{d_z}$:
$$Z_t = (t, P_t^{(1)}, \dots, P_t^{(n)}, z_t)^\top$$
where $z_t$ is an observed exogenous signal (e.g., normalized rolling spread $z$-score $z_t = (S_t - \mu_t)/\sigma_t$).

For a truncation depth $N \in \mathbb{N}$, the coordinate feature vector $x_t \in \mathbb{R}^m$ of the truncated geometric signature $\Phi_t = \mathcal{S}^{\le N}(\mathbf{Z})_{0,t}$ is:
$$x_t = \left( 1, \Delta Z_t^i, \mathbb{Z}_t^{j,k}, \dots \right)^\top \in \mathbb{R}^m, \quad m = \sum_{k=0}^N d_z^k$$
where:
$$\mathbb{Z}_t^{j,k} = \int_{0 < u_1 < u_2 < t} dZ_{u_1}^j dZ_{u_2}^k$$
Define the integrated feature process:
$$y_t = \int_0^t x_u du \in \mathbb{R}^m$$

### 2. Predictive Alpha Signal & Signature-Linear Policy

- **Predictive Signal:**
  $$\alpha_t = K x_t \in \mathbb{R}^n, \quad K \in \mathbb{R}^{n \times m} \text{ (deterministic)}$$
- **Trading Speed Policy:**
  $$v_t = B x_t \in \mathbb{R}^n, \quad B \in \mathbb{R}^{n \times m} \text{ (to be optimized)}$$
- **Inventory Process:**
  $$Q_t = Q_0 + \int_0^t v_u du = Q_0 + B y_t = Q_0 + (y_t^\top \otimes I_n) \theta$$
  where $\theta = \operatorname{vec}(B) \in \mathbb{R}^{nm}$ is the column-major vectorization of $B$.

### 3. Continuous Execution Objective Functional

The agent maximizes:
$$\mathcal{J}(B) = \mathbb{E} \left[ \int_0^T \left( Q_t^\top \alpha_t - v_t^\top \tilde{\Lambda} v_t - \phi Q_t^\top \Sigma Q_t - \eta (Q_t^\top P_t)^2 \right) dt - \gamma \|Q_T\|^2 \right]$$
subject to:
- $\tilde{\Lambda} \succ 0$: symmetric positive definite temporary impact matrix.
- $\Sigma \succeq 0$: symmetric positive semidefinite inventory covariance matrix.
- $\phi \ge 0$: inventory risk penalty parameter (set $\phi = 0$ for pure stat-arb inventory cycling).
- $\eta \ge 0$: dollar-neutrality penalty parameter.
- $\gamma \ge 0$: soft terminal inventory liquidation penalty.

### 4. Quadratic Reduction Theorem (Theorem 2.9)

Under column-major vectorization $\theta = \operatorname{vec}(B)$, the objective reduces exactly to a finite-dimensional quadratic program:
$$J(\theta) = \theta^\top A \theta + b^\top \theta + c$$
where:
$$A = -\mathbb{E} \left[ \int_0^T \left( (x_t x_t^\top) \otimes \tilde{\Lambda} + (y_t y_t^\top) \otimes (\phi \Sigma + \eta P_t P_t^\top) \right) dt + \gamma (y_T y_T^\top) \otimes I_n \right] \in \mathbb{R}^{nm \times nm}$$
$$b = \mathbb{E} \left[ \int_0^T \left( (y_t \otimes I_n) K x_t - 2 (y_t x_t^\top) \otimes \tilde{\Lambda} Q_0 - 2 (y_t \otimes I_n) (\phi \Sigma + \eta P_t P_t^\top) Q_0 \right) dt - 2 \gamma (y_T \otimes I_n) Q_0 \right] \in \mathbb{R}^{nm}$$
$$c = \mathbb{E} \left[ \int_0^T \left( Q_0^\top K x_t - \phi Q_0^\top \Sigma Q_0 - \eta (Q_0^\top P_t)^2 \right) dt - \gamma \|Q_0\|^2 \right] \in \mathbb{R}$$

### 5. Optimal Closed-Form & Regularized Policy

- If $A \prec 0$ (symmetric negative definite), the unique global unconstrained maximizer is:
  $$\theta^* = -\frac{1}{2} A^{-1} b$$
- With Tikhonov / Ridge regularization (Corollary 2.12) to prevent noise amplification from small eigenvalues $\lambda_i \approx 0$ in empirical signature moments:
  $$\theta_{\text{ridge}}^* = -\frac{1}{2} (A - \rho I)^{-1} b, \quad \rho > 0$$
- Live execution trading speed is evaluated without live optimization:
  $$v_t^* = \operatorname{mat}(\theta^*) x_t$$

## Required data

- **Universe:** Cointegrated asset pairs or multi-asset baskets (e.g., equity energy pairs SHEL/BP, crypto spot/perp pairs, futures calendar spreads).
- **Timeframe:** High-frequency ticks, 1-minute, or 5-minute bars aggregated to trading windows (e.g., $T=1$ day or 4-day rolling windows).
- **Price Fields:** Unaffected mid-prices $P_t^{(1)}, P_t^{(2)}$, dollar notionals, and rolling spread $z$-score $z_t = (S_t - \hat{\mu}_t)/\hat{\sigma}_t$.
- **Path Augmentation:** Time channel $t$, asset prices $P_t^{(i)}$, and rolling signal $z_t$, yielding dimension $d_z = 4$ for a 2-asset pair with spread channel.
- **Signature Coordinates:** Truncated signature basis up to degree $N=2$ ($m = 1 + 4 + 16 = 21$ coordinates).
- **Precomputed Moment Tensors:** Empirical Gram matrices $\mathbb{E}[\int_0^T x_t x_t^\top dt]$, $\mathbb{E}[\int_0^T y_t y_t^\top dt]$, $\mathbb{E}[\int_0^T y_t \otimes K x_t dt]$, and mixed price-feature moments $\mathbb{E}[\int_0^T y_t y_t^\top \otimes P_t P_t^\top dt]$ computed off-line across historical training paths.

## Execution assumptions

- **Execution Model:** Continuous trading speed $v_t$ (shares per unit time) with quadratic temporary market impact $v_t^\top \tilde{\Lambda} v_t$.
- **Impact Matrices:** $\tilde{\Lambda} = \operatorname{diag}(10^{-4}, 10^{-5})$ in synthetic experiments; $\tilde{\Lambda} = \operatorname{diag}(10^{-1}, 10^{-2})$ in empirical equity backtests.
- **Proportional Spread Cost:** Ex-post mark-to-market accounting includes half-spread friction $\xi = 0.5 \times 10^{-4}$ (0.5 bps) applied to cumulative traded notional $\mathrm{TN}_T = \int_0^T \sum_{i=1}^n P_t^{(i)} |v_t^{(i)}| dt$.
- **Dollar Neutrality:** Soft penalty $\eta (Q_t^\top P_t)^2$ with $\eta = 10^{-1}$ to $10^{-2}$.
- **Terminal Liquidation:** Soft quadratic penalty $\gamma \|Q_T\|^2$ with $\gamma = 0.1$ to $1.0$.

## Evidence

### Source-reported

All empirical figures below are directly reported by Gianmarco Morbelli, Sven Karbach, and Mike Derksen (arXiv:2606.31387v1, June 2026):

1. **Synthetic Common-Trend Log-Spread Experiment ($N=2$, 10,000 training paths, 5,000 test paths):**
   - Data Generating Process: $dM_t = \mu dt + \sigma_M dW_t^M$, $dX_t = -\kappa X_t dt + \sigma_X dW_t^X$, with $T=1, \mu=0, \sigma_M=0.02, \sigma_X=0.02, \kappa=50, \rho=0.3, c_\alpha=1.5, \beta=1, \lambda_{\text{ridge}}=10^{-8}$.
   - Performance: Signature-based policy achieves Return on Turnover (ROT) of **99 bps** ($\approx 0.99\%$) versus **66 bps** for the standard $z$-score threshold benchmark ($z_e = 2, z_{\text{exit}} = 0$).
   - Terminal Inventory: Gradual reduction toward zero, respecting dollar-neutrality and soft terminal liquidation penalties without abrupt liquidation dumps.

2. **Historical LSE Equity Pairs Trading Backtest (Shell PLC `SHEL` vs BP PLC `BP`):**
   - Training sample: 4-day rolling windows between January 2025 and October 2025.
   - Out-of-sample evaluation: November 2025 to December 2025.
   - Parameters: $N=2$, 8-hour rolling $z$-score window, $\tilde{\Lambda} = \operatorname{diag}(10^{-1}, 10^{-2}), \eta = 10^{-2}, \phi = 0, \gamma = 1, c_\alpha = 1, \beta = 1, \lambda_{\text{ridge}} = 0$.
   - Accounting Performance: Signature execution policy achieves Return on Turnover (ROT) of **99 bps** versus **22 bps** for the classical $z$-score benchmark.
   - Robustness in Regime Shift: In November 2025, where the raw $z$-score strategy recorded negative PnL due to persistent spread divergence, the signature strategy preserved positive accounting PnL by scaling down trading speed in response to higher-order path features.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- None identified in the reviewed paper; absence is not evidence of no negative result.
- Authors note that without Tikhonov regularization ($\rho > 0$), empirical moment matrices for $N \ge 3$ suffer ill-conditioning, where near-null eigenvalues amplify estimation noise and cause out-of-sample speed oscillations.

## Falsification plan

1. **Ablation of Signature Order ($N=0, 1, 2, 3$):** Compare $N=0$ (constant speed), $N=1$ (linear price increments only / Almgren-Chriss class), and $N=2$ (full iterated integrals including Lévy area). If $N=2$ does not deliver statistically significant ROT improvement over $N=1$ net of transaction costs, the higher-order geometric features fail the complexity hurdle.
2. **Permanent Impact & Adverse Selection Stress:** The quadratic reduction relies strictly on temporary impact $\tilde{\Lambda} \succ 0$. Introduce permanent square-root price impact $I_{\text{perm}} \propto \sigma \sqrt{v_t / V_t}$ and cross-asset flow toxicity; if execution slippage erodes $>50\%$ of ROT advantage, the static linear speed approximation breaks down.
3. **Execution Latency Perturbation:** Introduce a discrete lag $\tau_{\text{lag}} \in [100\text{ms}, 5\text{s}]$ between signature computation and child order routing. If ROT degrades below the benchmark, the strategy overfits to zero-latency path updates.
4. **Failure Threshold:** If ROT on out-of-sample test pairs is $\le 25\text{ bps}$ or maximum drawdown exceeds $15\%$ under $1\text{ bps}$ maker/taker fee schedules, reject the execution layer.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Spot vs Perpetual Basis:** Crypto stat-arb pairs (e.g., BTC/ETH, SOL/AVAX, or spot-perp basis) exhibit non-stationary funding rates, asynchronous funding timestamps (8h funding intervals), and fragmented liquidity across Binance, OKX, and Bybit.
- **Mark-Price Dynamics:** In crypto perpetuals, execution occurs at order-book mid-price while liquidations are triggered by index/mark price. The signature information vector $Z_t$ must be augmented with mark-index basis channels and perpetual funding rate imbalances.
- **24/7 Continuous Trading:** Unlike LSE/NYSE equity sessions with discrete trading closes ($T = 1\text{ day}$), crypto execution horizons must be partitioned into rolling finite execution epochs $T \in [1\text{h}, 8\text{h}]$.

## Limitations

- **Linearity in Feature Space:** Admissible policies are restricted to signature-linear functions $v_t = B x_t$. Nonlinear policies (e.g., deep neural networks or Tree ensembles over signature coordinates) cannot be solved via the quadratic reduction theorem and require approximate iterative solvers.
- **Exogenous Path Assumption:** The theorem assumes market paths $Z_t$ are unaffected by the execution policy (temporary impact only). It does not model feedback where trading permanently shifts the mid-price drift.
- **Single Pair Evaluation:** The empirical test uses a single equity pair (`SHEL`/`BP`) over a two-month test window; broad cross-sectional validation across dozens of pairs and varying volatility regimes is omitted.

## Implementation status

`not-implemented` in the quantitative production stack.

## Adoption boundary

Research capture only. A record being present in this repository does not constitute authorization for deployment, implementation in PyBroker/Nautilus, or allocation of capital in paper, testnet, or live trading.

## Related Wiki records

- `[[quant/path-portfolio-optimization-signature-defect-lift-2026-09-02]]`
- `[[quant/options-statistical-arbitrage-graph-learning-synthetic-long-2026-09-02]]`
- `[[quant/microstructure-mean-reversion-optimal-symmetric-band-waiting-option-2026-09-02]]`

## Sources

1. Gianmarco Morbelli, Sven Karbach, Mike Derksen, *"Signature-Based Optimal Execution for Statistical Arbitrage with Path-Dependent Trading Signals"*, arXiv preprint `arXiv:2606.31387v1 [q-fin.TR]`, June 30, 2026. DOI: [10.48550/arXiv.2606.31387](https://doi.org/10.48550/arXiv.2606.31387). Stable URL: [https://arxiv.org/abs/2606.31387](https://arxiv.org/abs/2606.31387).
