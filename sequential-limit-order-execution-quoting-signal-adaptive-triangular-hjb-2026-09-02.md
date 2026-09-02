---
schema: strategy-research-record-v1
title: "Explicit Signal-Adaptive Sequential Optimal Execution Quotes: Triangular HJB Solvability, Point-Process Fill Dynamics, and Certainty-Equivalent Inventory Risk"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - optimal-execution
  - limit-order-book
  - optimal-quoting
  - stochastic-control
  - point-processes
  - hjb-equations
  - alpha-signals
  - inventory-risk
status: research-only
confidence: high
source_as_of: 2026-06-11
sources:
  - "Fenghui Yu, 'Explicit Signal-Adaptive Sequential Optimal Execution Quotes', arXiv:2605.24242v2 [q-fin.TR], June 11, 2026. DOI: 10.48550/arXiv.2605.24242. https://arxiv.org/abs/2605.24242"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Explicit Signal-Adaptive Sequential Optimal Execution Quotes: Triangular HJB Solvability, Point-Process Fill Dynamics, and Certainty-Equivalent Inventory Risk

## Provenance

- **Primary Source:** Fenghui Yu (Delft Institute of Applied Mathematics, Delft University of Technology), *"Explicit Signal-Adaptive Sequential Optimal Execution Quotes"*, arXiv preprint `arXiv:2605.24242v2 [q-fin.TR]`, first submitted May 22, 2026, revised June 11, 2026. DOI: [10.48550/arXiv.2605.24242](https://doi.org/10.48550/arXiv.2605.24242). Full text: [https://arxiv.org/abs/2605.24242](https://arxiv.org/abs/2605.24242).
- **Primary Subject Area:** Trading and Market Microstructure (`q-fin.TR`), Optimization and Control (`math.OC`).
- **Context:** Classical optimal execution models (Almgren-Chriss, Cartea-Jaimungal) typically operate at the macro level by controlling the aggregate continuous trading rate of a metaorder, ignoring micro-level limit order book (LOB) child quote placement and fill risk. Conversely, optimal quoting models (Ho-Stoll, Avellaneda-Stoikov, Guéant) often assume a zero-drift (martingale) mid-price for analytical tractability, precluding the integration of predictive alpha signals. Yu develops a unified, fully explicit solution theory for sequential limit-order optimal quoting under signal-dependent mid-price drift $g(s_t)$, price impact, execution fill risk, inventory risk, and four distinct optimization criteria.

## Economic mechanism

### Source-reported

1. **Integrated Scheduling and Micro-Quoting:** A liquidating agent controls the quote depth $\delta_t$ (distance from reference mid-price $M_t$) for individual limit orders. Executions occur via a point process with quote-dependent intensity $\lambda_t^\delta = \lambda e^{-\kappa \delta_t}$. Posting further away increases price improvement but raises execution fill risk and inventory holding duration.
2. **Signal-Driven Continuation Value:** Reference mid-price dynamics follow $dM_t = g(s_t) dt + \sigma_t dW_t$, where $g(s_t)$ represents short-term drift predicted by LOB order flow imbalance or machine learning alpha signals. A positive expected drift increases the continuation value of holding inventory, causing the optimal quote depth $\delta_t^*$ to widen (more patient quoting), whereas an adverse drift causes quotes to tighten or cross the spread (aggressive immediate execution).
3. **Triangular Reduction of Jump-Diffusion HJB Equations:** For all four standard execution objectives (risk-neutral, running inventory penalty, CARA utility, CARA + running penalty), an exponential-affine transformation decouples the Hamilton-Jacobi-Bellman (HJB) system into a finite-dimensional lower-triangular linear system of ordinary differential equations (ODEs), solvable in exact closed form via divided differences.

### Research interpretation

The falsifiable thesis is that **incorporating real-time predictive drift signals $g(s_t)$ into sequential limit-order placement via exact triangular HJB quotes yields strictly higher execution proceeds and lower implementation shortfall than martingale-assumption quoting (e.g., standard Avellaneda-Stoikov or zero-drift Guéant models)**:
- The exact analytical solution reveals that a quadratic running inventory penalty $J(q) = \frac{1}{2}\sigma^2 \gamma q^2$ exactly matches the certainty-equivalent drift correction induced by exponential CARA utility, providing a rigorous structural bridge between penalty-based execution heuristics and formal expected utility theory.
- In long horizons ($\tau = T - t \to \infty$), optimal quote depth exhibits a phase transition: it grows linearly $\delta^{\text{unc}}(t,q) \sim \frac{g(s)}{b}(T-t)$ when favorable drift creates a new maximum in effective continuation value $\Psi(q)$, but grows only logarithmically $\delta^{\text{unc}}(t,q) \sim \frac{1}{\kappa}\log(T-t)$ in the fully degenerate zero-drift case ($A_q = 0$).

## Signal

### 1. Controlled Execution Dynamics & Point-Process Fills

- **Reference Price Dynamics:**
  $$dM_t = g(s_t) dt + \sigma_t dW_t$$
  where $s_t$ is a bounded predictive alpha signal, $g(s_t)$ is the predicted instantaneous drift, and $\sigma_t \ge 0$ is volatility.
- **Controlled Quote Depth $\delta_t \in \mathcal{A}$:**
  Predictable quote offset from reference price, constrained to $\delta_t \in [\delta_{\min}, \delta_{\max}]$.
- **Fill Point Process $N_t^\delta$:**
  $$d N_t^\delta \sim \operatorname{Poisson}\left(\lambda_t^\delta dt\right), \quad \lambda_t^\delta = \lambda e^{-\kappa \delta_t} \mathbf{1}_{\{Q_{t-}^\delta > 0\}}$$
  with arrival intensity parameter $\lambda > 0$ and price-sensitivity parameter $\kappa > 0$.
- **Inventory & Cash Evolution:**
  $$d Q_t^\delta = - d N_t^\delta, \quad Q_0 \in \mathbb{N}$$
  $$d X_t^\delta = \left( M_t - a + b \delta_t \right) d N_t^\delta$$
  where $a \ge 0$ is fixed adverse price impact and $b > 0$ is the quote improvement sensitivity factor ($a=0, b=1$ for standard spread quoting).

### 2. Four Execution Optimization Criteria

1. **Case I (Risk-Neutral Wealth):**
   $$\sup_{\delta \in \mathcal{A}} \mathbb{E} \left[ X_\tau^\delta + Q_\tau^\delta M_\tau - I(Q_\tau^\delta) \right]$$
2. **Case II (Running Inventory Penalty $J(q)$):**
   $$\sup_{\delta \in \mathcal{A}} \mathbb{E} \left[ X_\tau^\delta + Q_\tau^\delta M_\tau - I(Q_\tau^\delta) - \int_0^\tau J(Q_t^\delta) dt \right]$$
3. **Case III (CARA Utility with Absolute Risk Aversion $\gamma > 0$):**
   $$\sup_{\delta \in \mathcal{A}} \mathbb{E} \left[ -\exp\left\{ -\gamma \left( X_\tau^\delta + Q_\tau^\delta M_\tau - I(Q_\tau^\delta) \right) \right\} \right]$$
4. **Case IV (CARA Utility + Running Inventory Penalty $J(q)$):**
   $$\sup_{\delta \in \mathcal{A}} \mathbb{E} \left[ -\exp\left\{ -\gamma \left( X_\tau^\delta + Q_\tau^\delta M_\tau - I(Q_\tau^\delta) - \int_0^\tau J(Q_t^\delta) dt \right) \right\} \right]$$

### 3. Unified Triangular ODE System & Explicit Quotes

For all four cases, the value function transforms into $V(t,x,M,q)$ via an exponential/affine ansatz governed by $w(t,q)$:
$$\partial_t w(t,q) + A_q w(t,q) + C w(t, q-1) = 0, \quad w(T,q) = G_q, \quad w(t,0) = 1$$
where the case-specific parameters are:
- **Case I:** $A_q = \frac{\kappa}{b} g(s) q$, $C = \lambda \exp\left\{-\frac{\kappa a}{b} - 1\right\}$, $G_q = \exp\left\{-\frac{\kappa}{b} I(q)\right\}$.
- **Case II:** $A_q = \frac{\kappa}{b} \left( g(s) q - J(q) \right)$, $C = \lambda \exp\left\{-\frac{\kappa a}{b} - 1\right\}$, $G_q = \exp\left\{-\frac{\kappa}{b} I(q)\right\}$.
- **Case III:** $A_q = \frac{\kappa}{b} g(s) q - \frac{1}{2} \sigma^2 \gamma q^2 \left(1 + \frac{\kappa}{b\gamma}\right)$, $C = \frac{\lambda \kappa}{\kappa + b\gamma} \exp\left\{ -\frac{\kappa a}{b} - \frac{\kappa}{b\gamma} \log\left(1 + \frac{b\gamma}{\kappa}\right) \right\}$, $G_q = \exp\left\{-\left(\gamma + \frac{\kappa}{b}\right) I(q)\right\}$.
- **Case IV:** $A_q = \frac{\kappa}{b} \left( g(s) q - J(q) \right) - \gamma J(q) - \frac{1}{2} \sigma^2 \gamma q^2 \left(1 + \frac{\kappa}{b\gamma}\right)$, with $C, G_q$ as in Case III.

- **Explicit Optimal Feedback Quotes:**
  - Cases I & II:
    $$\delta_t^{*(I,II)}(q) = \Pi_{[\delta_{\min}, \delta_{\max}]} \left( \frac{1}{\kappa} + \frac{a}{b} + \frac{1}{\kappa} \log \left( \frac{w(t,q)}{w(t, q-1)} \right) \right)$$
  - Cases III & IV:
    $$\delta_t^{*(III,IV)}(q) = \Pi_{[\delta_{\min}, \delta_{\max}]} \left( \frac{a}{b} + \frac{1}{b\gamma} \log \left( 1 + \frac{b\gamma}{\kappa} \right) + \frac{1}{\kappa + b\gamma} \log \left( \frac{w(t,q)}{w(t, q-1)} \right) \right)$$

- **Closed-Form Solution for $w(t,q)$ (Divided Differences):**
  When $A_0, \dots, A_q$ are distinct:
  $$w(t,q) = \sum_{i=0}^q \left( \sum_{j=i}^q G_j C^{q-j} \prod_{k=i, k \neq l}^j \frac{1}{A_k - A_l} \right) e^{A_i (T-t)}$$

## Required data

- **Universe:** Limit Order Book assets with observable order queue depths (equities, crypto perpetuals, futures).
- **LOB Microstructure Data:** Top-of-book best bid/ask, mid-price $M_t$, and order-flow imbalance (OFI) to estimate short-term predictive drift $g(s_t)$.
- **Point-Process Calibration:** Trade tick execution stream to calibrate fill intensity baseline $\lambda > 0$ and quote-depth decay parameter $\kappa > 0$.
- **Impact & Risk Parameters:** Fixed adverse impact $a \ge 0$, quote price scaling factor $b > 0$, asset return volatility $\sigma_t$, and terminal penalty schedule $I(q) = \alpha q$.

## Execution assumptions

- **Execution Mode:** Sequential limit order posting at distance $\delta_t^*$ from mid-price.
- **Unit Order Size:** Each fill executes exactly 1 unit (lot size) of inventory and decrements $Q_t$ by 1.
- **Execution Price:** $P_{\text{exec}} = M_t - a + b \delta_t^*$.
- **Admissibility:** Predictable bounded feedback quotes $\delta_t^* \in [\delta_{\min}, \delta_{\max}]$.
- **Terminal Horizon:** Horizon $T \in (0, \infty)$; any remaining inventory at $T$ is liquidated at penalized price $M_T - I(Q_T)$.

## Evidence

### Source-reported

All analytical theorems, proofs, and numerical figures below are directly reported by Fenghui Yu (arXiv:2605.24242v2, June 2026):

1. **Rigorous Verification & Well-Posedness (Theorem 4.6):**
   - Proves pathwise uniqueness, non-explosiveness, and boundedness of the controlled jump process $(X_t^\delta, M_t, Q_t^\delta)$.
   - Establishes that the explicit candidate value functions $V(t,x,M,q)$ satisfy the dynamic programming verification theorem on $[0,T] \times \mathbb{R} \times \mathbb{R} \times \{0, \dots, Q_0\}$.

2. **Numerical Sensitivity Across Alpha Signals (Section 7, Figures 1–11):**
   - **Constant Signals ($g(s) \in \{-0.05, 0.0, +0.05\}$):** Positive drift ($g(s) = +0.05$) shifts optimal quote depth upward by $\approx 0.15$–$0.30$ units away from mid-price, enforcing patient liquidity provision; negative drift ($g(s) = -0.05$) lowers quotes, inducing rapid aggressive execution to avoid adverse selection.
   - **Time-Decaying Signals ($g(s,t) = g(s) e^{-0.01 t}$):** The quote depth spread widens early in the execution window when predictive signal strength is maximal, converging smoothly to the terminal penalty slope as $t \to T$.
   - **Certainty-Equivalent Equivalence:** Numerically confirms that setting running inventory penalty $J(q) = \frac{1}{2}\sigma^2 \gamma q^2$ in Case II replicates the principal curvature of CARA utility in Case III, with quotes differing only by the risk-aversion constant shift $\frac{1}{b\gamma}\log(1 + b\gamma/\kappa) - \frac{1}{\kappa}$.

3. **Long-Horizon Asymptotic Phase Transition (Propositions 6.1 & 6.2):**
   - In non-degenerate drift regimes ($A_q > A_{q-1}$), the unconstrained quote depth scales linearly: $\lim_{\tau \to \infty} \delta^{\text{unc}}(t,q)/\tau = g(s)/b$.
   - In the fully degenerate zero-signal zero-risk regime ($A_q = 0$), optimal quote depth scales logarithmically: $\lim_{\tau \to \infty} \delta^{\text{unc}}(t,q)/\log(\tau) = 1/\kappa$.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- None identified in the reviewed paper; absence is not evidence of no negative result.
- The author notes that unconstrained quotes can diverge to $+\infty$ if favorable drift $g(s) > 0$ is assumed permanent without mean-reversion, necessitating practical compact bounds $[\delta_{\min}, \delta_{\max}]$ to prevent total fill starvation.

## Falsification plan

1. **Alpha Signal Decay & Reversal Stress:** Introduce an Ornstein-Uhlenbeck or sign-flipping mean-reverting drift $g(s_t) = -\theta s_t + \sigma_s dW_t^s$. If the frozen-signal approximation leads to severe inventory overrun and terminal penalty blowout compared to an adaptive benchmark, the quasi-static signal assumption is falsified.
2. **Adverse Fill Probability Perturbation:** Replace the homogeneous Poisson intensity $\lambda e^{-\kappa \delta}$ with a toxicity-skewed jump process where adverse mid-price jumps correlate with fill arrivals (adverse selection). If fill toxicity erodes $>40\%$ of price improvement, the independent point-process assumption fails.
3. **Execution Horizon Sensitivity:** Test execution efficiency across varying horizons $T \in [10\text{s}, 1\text{h}]$. If child order quote adjustments exceed the exchange rate-limit constraints or incur excessive cancel/replace fees, the continuous quoting schedule is unviable.
4. **Failure Threshold:** If implementation shortfall exceeds a naive TWAP baseline by $>5\text{ bps}$ across a 1,000-metaorder simulation under historical LOB tick data, reject the quoting policy.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Crypto LOB Microstructure:** Crypto perpetuals (Binance, Bybit, Hyperliquid) feature sub-second order book updates, discrete tick/lot sizes, and VIP fee tiers (negative maker fees / rebates). The parameter $a$ can be negative to reflect maker rebates.
- **Perpetual Funding Rate Drift:** In perpetual futures, funding payments accrued during inventory liquidation act as an explicit running inventory cost $J(q) = q \cdot r_{\text{fund}}$, modifying the effective drift $g(s) - r_{\text{fund}}$.
- **Queue Priority Dynamics:** The theoretical model assumes continuous quote depth $\delta_t$; in fixed-tick crypto books, quote depth must be discretized onto price ticks with queue priority tracking.

## Limitations

- **Unit Lot Size Restriction:** The analytical derivation assumes each execution reduces inventory by exactly 1 unit; multi-unit block executions require compound Poisson extensions.
- **Frozen Signal Approximation:** Time-dependent and stochastic drift signals $g(s_t)$ are handled via instantaneous frozen-signal evaluation rather than solving coupled multi-dimensional jump-diffusion PDEs.
- **Absence of Permanent Market Impact:** The model incorporates fixed execution adjustment $a$ and depth sensitivity $b$, but does not model path-dependent permanent impact on subsequent mid-price trajectories.

## Implementation status

`not-implemented` in the quantitative production stack.

## Adoption boundary

Research capture only. A record being present in this repository does not constitute authorization for deployment, implementation in PyBroker/Nautilus, or allocation of capital in paper, testnet, or live trading.

## Related Wiki records

- `[[quant/market-making-axiomatic-unified-inventory-quoting-spread-decomposition-2026-09-02]]`
- `[[quant/deep-rl-market-making-closing-auction-anticipation-2026-09-02]]`
- `[[quant/passive-market-impact-optimal-execution-mlofi-2026-09-02]]`

## Sources

1. Fenghui Yu, *"Explicit Signal-Adaptive Sequential Optimal Execution Quotes"*, arXiv preprint `arXiv:2605.24242v2 [q-fin.TR]`, first submitted May 22, 2026, revised June 11, 2026. DOI: [10.48550/arXiv.2605.24242](https://doi.org/10.48550/arXiv.2605.24242). Stable URL: [https://arxiv.org/abs/2605.24242](https://arxiv.org/abs/2605.24242).
