---
schema: strategy-research-record-v1
title: Passive Market Impact and Optimal Limit-Order Liquidation via Multi-Level Order Flow Imbalance
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-07-30
sources:
  - "https://arxiv.org/abs/2607.28323"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Passive Market Impact and Optimal Limit-Order Liquidation via Multi-Level Order Flow Imbalance

## Provenance

This research capture is based on the working paper:
- **Title:** Optimal Execution with Passive Market Impact
- **Authors:** Alexander Barzykin (HSBC), Robert Boyce (Imperial College London), Eyal Neuman (Imperial College London), and Sturmius Tuschmann (Imperial College London)
- **Publication Identifier:** arXiv:2607.28323v1 [math.OC, q-fin.TR]
- **Submission Date:** 30 July 2026
- **Canonical DOI:** [10.48550/arXiv.2607.28323](https://doi.org/10.48550/arXiv.2607.28323)
- **Traceable Source URL:** `https://arxiv.org/abs/2607.28323` / `https://arxiv.org/html/2607.28323v1`

The paper addresses a foundational gap in optimal execution theory: while classical literature (e.g., Almgren–Chriss, Bertsimas–Lo) models price impact almost exclusively as the cost of taking liquidity with aggressive market orders, real-world institutional liquidation often relies on passive limit orders. The authors demonstrate both theoretically and empirically that tactical quote adjustments (submitting, cancelling, and repositioning limit orders) generate multi-level order flow imbalance (MLOFI), transmitting persistent downward price pressure at a mesoscopic rate that decays exponentially with the posted quote distance.

## Economic mechanism

### Source-reported

In electronic limit order book and quote-driven markets, passive execution is achieved not by placing a single static limit order and waiting, but through a tactical chain of quote submissions, cancellations, venue choices, and distance adjustments. 

Empirically:
1. **Fill Intensity Decay:** The arrival rate of limit order executions decays exponentially with the distance $\delta$ from the midprice ($\Lambda(\delta) = \lambda e^{-k\delta}$), consistent with power-law order sizing and logarithmic price responses (Avellaneda & Stoikov, 2008).
2. **MLOFI Price Impact:** Price changes over short horizons respond linearly to order flow imbalance across multiple occupied book levels, with price impact decaying exponentially across book depth ($\beta(\delta) = \xi e^{-\ell \delta}$) (Xu et al., 2023; Cont et al., 2014).

Combining these empirical laws yields a mesoscopic passive price impact rate:
$$\dot{S}_t^{\text{passive}} = -\beta(\delta) \Lambda(\delta) = -\xi \lambda e^{-(k+\ell)\delta} = -\eta e^{-m\delta}$$
where $\eta = \xi \lambda$ and $m = k + \ell$.

Consequently, an executing agent liquidating an inventory of $q_0$ shares faces a fundamental economic trade-off:
- **Aggressive Quoting (small/negative $\delta$):** Maximizes fill intensity but accelerates the accumulation of permanent price degradation across the entire remaining inventory.
- **Conservative Quoting (large $\delta$):** Minimizes price impact and earns higher spread, but increases non-execution risk, prolongs liquidation time, and exposes the position to running and terminal inventory penalties.

### Research interpretation

The model establishes an analytical bridge between microscopic order-book dynamics and mesoscopic continuous-time stochastic control. 

Unlike the classical Almgren–Chriss framework where permanent impact factors out of the optimal execution trajectory (affecting only cash P&L), permanent passive impact directly determines the optimal quoting policy $\delta^*(t, q)$ and governs the convexity of the stochastic liquidation path. When the fill decay rate equals the impact decay rate ($m = k$, verified empirically for equity markets), the Hamilton–Jacobi–Bellman (HJB) PDE is linearized via an exponential logarithmic transformation, yielding an exact closed-form matrix exponential solution. When $m \neq k$ (as observed in FX markets), the first-order condition yields a semi-explicit optimal quote parameterized by the principal real branch of the Lambert W function $W_0$.

## Signal

The execution strategy continuously determines the optimal quote distance $\delta^*(t, q)$ of unit sell limit orders from the prevailing midprice $S_t$ as a function of time $t \in [0, T]$ and remaining inventory $q \in \{1, \dots, q_0\}$.

### Baseline Model Dynamics ($m = k$)

1. **State Dynamics:**
   - Cumulative fill counting process: $N_t$ with stochastic intensity $\Lambda_t = \lambda e^{-k\delta_t} \mathbf{1}_{\{Q_{t-} > 0\}}$.
   - Remaining inventory: $Q_t = q_0 - N_t$.
   - Impacted midprice: $dS_t = -\eta e^{-k\delta_t} \mathbf{1}_{\{Q_{t-} > 0\}} dt + \sigma dW_t$.
   - Cash process: $dX_t = (S_t + \delta_t) dN_t$.

2. **Control Objective:**
   Maximize expected terminal cash net of inventory penalties:
   $$\sup_{\delta \in \mathcal{A}} \mathbb{E}_{t, x, q, s} \left[ X_T + Q_T S_T - \phi \int_t^T Q_u^2 du - \alpha Q_T^2 \right]$$
   where $\phi \ge 0$ is running inventory penalty and $\alpha \ge 0$ is terminal inventory penalty.

3. **Closed-Form Optimal Quote:**
   Using the value function ansatz $u(t, x, q, s) = x + q s - \theta(t, q)$ and linearizing transform $\theta(t, q) = \frac{1}{k} \log \omega(t, q)$, the vector $\omega(t) = (\omega(t, 0), \dots, \omega(t, q_0))^\top$ satisfies the upper bidiagonal linear system $\dot{\omega}(t) + A\omega(t) = 0$ with terminal condition $\omega(T, q) = \exp(k\alpha q^2)$.

   The optimal quote distance is given explicitly by:
   $$\delta^*(t, q) = \frac{1}{k} - \frac{1}{k} \log \left( \frac{\omega(t, q)}{\omega(t, q-1)} \right) + \frac{\eta}{\lambda} q$$
   where $\omega(t) = \exp(A(T-t)) \mathbf{1}$, and the matrix $A \in \mathbb{R}^{(q_0+1) \times (q_0+1)}$ has entries:
   $$A_{q, q} = -k\phi q^2, \quad A_{q, q-1} = \lambda \exp \left( -1 - \frac{k\eta}{\lambda} q \right)$$

### Heterogeneous Decay Extension ($m \neq k$)

When fill decay $k$ and impact decay $m$ differ (e.g., in FX), let $\Delta_q(t) = \theta(t, q) - \theta(t, q-1)$. The optimal quote is given in terms of the principal branch of the Lambert W function $W_0$:
$$\delta^*(t, q) = \frac{1}{k} + \Delta_q(t) + \frac{1}{m - k} W_0 \left( \frac{m - k}{k} \frac{m\eta q}{\lambda} \exp \left( \frac{m - k}{k} (1 - k \Delta_q(t)) \right) \right)$$
where $\theta(t, q)$ solves a nonlinear triangular ODE system.

### Transient Impact Extension

When passive impact exhibits exponential resilience $\dot{I}_t = -\rho I_t + \eta e^{-k\delta_t}$ with $S_t = S_0 - I_t + \sigma W_t$, the optimal quote becomes state-dependent on current impact dislocation $i$:
$$\delta^*(t, q, i) = \frac{1}{k} + \psi(t, q, i) - \psi(t, q-1, i) + \frac{\eta}{\lambda} q - \frac{\eta}{\lambda} \partial_i \psi(t, q, i)$$
incentivizing the trader to quote further from midprice when current dislocation $i$ is elevated to allow liquidity resilience.

## Required data

- **LOB Event Data:** Order-by-order message and order-book snapshots (e.g., NASDAQ LOBSTER L3 or exchange tick data), reconstructing visible limit orders, cancellations, executions, spreads, and midprices.
- **MLOFI Time Series:** Multi-level order flow imbalance aggregated across depth levels $d \in \{1, \dots, 10\}$ at high frequency ($10\text{--}60\,\text{s}$ sampling).
- **Calibration Inputs:**
  - Limit order fill intensity decay: empirical log-linear regression of execution rate $\Lambda(\delta)$ on quote distance $\delta$ in ticks.
  - Multi-level price impact decay: ridge regression of midprice delta $\Delta S$ on MLOFI depth vectors.
  - Volatility $\sigma$, baseline fill rate $\lambda$, tick size, and average half-spread.

## Execution assumptions

- **Order Type:** Passive sell limit orders of unit size ($1$ unit $= 1,000$ shares in calibration).
- **Matching & Fills:** Executions arrive stochastically according to an inhomogeneous Poisson process with intensity $\Lambda(\delta_t) = \lambda e^{-k\delta_t}$.
- **Impact Transmission:** Each fill generates permanent midprice degradation $-\eta e^{-m\delta_t} dt$ until the position is liquidated.
- **Continuous Adjustments:** The trader continuously re-adjusts quote distance $\delta^*(t, q)$ as time elapses and fills occur.
- **Terminal Liquidation:** Unsold inventory at $T$ is evaluated at the impacted midprice $S_T$ minus quadratic penalty $\alpha Q_T^2$.

## Evidence

### Source-reported

1. **Empirical Calibration on NASDAQ Equities (LOBSTER 2016, 252 trading days, Table 4):**
   - Sample of 6 stocks with varying tick sizes (AMZN, TSLA, NFLX, ORCL, CSCO, MU):
     - TSLA: $\hat{k} = 48.0\,\text{ticks}^{-1}$, $\hat{\ell} = 0.08\,\text{ticks}^{-1} \implies \hat{m} = 48.08\,\text{ticks}^{-1}$ ($m \approx k$).
     - Across all 6 NASDAQ equities, $\hat{\ell} \ll \hat{k}$, confirming that the equal-decay model $m = k$ is an accurate empirical approximation for equity limit order books.

2. **Empirical Calibration on FX Markets (LSEG Market Data, Table 5):**
   - Sample of 5 currency pairs spanning major and emerging markets:
     - USDMXN (tick 0.001, spread 4.4 ticks): $\hat{k} = 0.52$, $\hat{\ell} = 0.23$, $\hat{m} = 0.75$.
     - GBPUSD (tick 0.00005, spread 2.7 ticks): $\hat{k} = 0.49$, $\hat{\ell} = 0.27$, $\hat{m} = 0.76$.
     - AUDUSD (tick 0.00005, spread 2.3 ticks): $\hat{k} = 0.54$, $\hat{\ell} = 0.13$, $\hat{m} = 0.67$.
     - USDTHB (tick 0.005, spread 2.1 ticks): $\hat{k} = 0.62$, $\hat{\ell} = 0.33$, $\hat{m} = 0.95$.
     - USDSGD (tick 0.0001, spread 1.5 ticks): $\hat{k} = 0.61$, $\hat{\ell} = 0.26$, $\hat{m} = 0.87$.
   - In FX, $\hat{\ell}$ is substantial relative to $\hat{k}$, confirming that decentralized quote-driven markets require the heterogeneous decay model $m \neq k$.

3. **Monte Carlo Simulation Results ($q_0 = 20\,\text{k-shares}$, $T = 300\,\text{s}$, 1,000 paths, Table 3):**
   - **$\eta = 0.0$ (Zero Passive Impact):**
     - Final inventory: $1.003$ k-shares (95% CI $[0.932, 1.074]$).
     - Net P&L: $+\$0.320\,\text{k}$ ($[0.301, 0.339]$).
     - Implementation shortfall: $-\$0.035\,\text{k}$ ($[-0.037, -0.034]$).
     - Trading time: $284.918\,\text{s}$ ($[283.257, 286.578]$).
   - **$\eta = 0.005$ (Moderate Passive Impact):**
     - Final inventory: $1.928$ k-shares ($[1.816, 2.040]$).
     - Net P&L: $+\$0.071\,\text{k}$ ($[0.049, 0.093]$).
     - Implementation shortfall: $-\$0.019\,\text{k}$ ($[-0.021, -0.017]$).
     - Trading time: $290.153\,\text{s}$ ($[288.674, 291.631]$).
   - **$\eta = 0.010$ (High Passive Impact):**
     - Final inventory: $6.367$ k-shares ($[6.195, 6.538]$).
     - Net P&L: $-\$0.011\,\text{k}$ ($[-0.040, 0.019]$).
     - Implementation shortfall: $-\$0.061\,\text{k}$ ($[-0.063, -0.058]$).
     - Trading time: $298.314\,\text{s}$ ($[297.617, 299.012]$).
   - Higher passive impact $\eta$ forces quotes farther from the midprice to protect mark-to-market inventory, leading to slower execution and lower realized P&L.

4. **Transient Impact & Resilience Dynamics (Table 7):**
   - Increasing resilience $\rho$ from $0.0$ (permanent) to $0.02\,\text{s}^{-1}$ allows the impacted price to recover between fills, increasing realized P&L from $+\$0.717\,\text{k}$ to $+\$1.047\,\text{k}$.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The model was calibrated strictly on traditional US equity (NASDAQ) and foreign exchange (LSEG) feeds; no cryptocurrency data was tested by the authors.
- The theoretical formulation assumes single-unit fills and continuous quote modifications, omitting discrete lot sizes, queue replacement penalties, and exchange cancel/replace API latencies.

## Falsification plan

1. **Crypto MLOFI Calibration:** Reconstruct MLOFI on high-volume crypto perpetual pairs (e.g., Binance BTCUSDT, ETHUSDT) across 10 order book levels. If the ridge regression coefficients $\beta(\delta)$ fail to exhibit statistically significant positive price impact or fail to decay exponentially with quote distance ($\ell \le 0$), the foundational premise of passive impact decay is rejected.
2. **Execution Strategy Benchmark:** Run a controlled simulated execution trial comparing:
   - Baseline Avellaneda–Stoikov (ignoring passive impact, $\eta = 0$).
   - Classical Almgren–Chriss TWAP (market orders only).
   - MLOFI Passive Optimal Execution ($\delta^*(t, q)$ from Theorem 3.1 / 6.1).
   If the MLOFI passive execution policy does not achieve statistically significant lower implementation shortfall (net of maker/taker fees) across metaorders of size $> 1\%$ ADV, the model is falsified.
3. **Resilience Parameter Audit:** Measure price recovery following large passive fills. If empirical resilience $\rho$ is non-stationary or vanishes during volatile regimes, the transient impact closed-form representation is disconfirmed.

## Crypto portability

- **Portability Status:** `adapted`, `unproven`.
- **Porting Rationale:** Institutional liquidation and inventory rebalancing in crypto perpetuals (e.g., OTC desk hedges, basis trades, market-maker unwinds) rely heavily on passive algorithmic execution (maker orders) to capture maker fee rebates and avoid high taker fees. The accumulation of passive sell flow visibly depresses the top of the book and alters funding spreads.
- **Portability Frictions:**
  - *Fee Disparities:* Crypto venues often pay maker rebates ($0\text{--}1\,\text{bp}$) while charging taker fees ($2\text{--}5\,\text{bps}$). The optimal quote boundary must incorporate maker fee offsets.
  - *Market Fragmentation:* Crypto liquidity is split across Binance, OKX, Bybit, Coinbase, and DEX CLOBs (Hyperliquid). Passive execution on one venue generates cross-venue leakage and cross-impact not captured in single-venue formulations.
  - *Funding Rate Accrual:* In crypto perpetual contracts, holding inventory over 8-hour funding intervals incurs continuous funding cash flows that alter the effective running inventory cost $\phi$.

## Limitations

- **Homogeneous Order Sizing:** Assumes unit order fills ($1$ lot), whereas real crypto fills follow fat-tailed size distributions that sweep multiple depth levels.
- **Exogenous Fill Process:** Fills are modeled via Poisson arrivals dependent only on distance $\delta$, ignoring adverse selection correlations with market-wide volatility spikes.
- **Linear Passive Impact Assumption:** Midprice impact is modeled as linear in the passive fill rate $\eta e^{-m\delta}$; large metaorders in illiquid crypto tokens may exhibit non-linear square-root scaling.

## Implementation status

`not-implemented` in our research repository or execution pipelines.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Scope:** Purely theoretical and mathematical finance research capture. Does not authorize deployment to PyBroker, NautilusTrader, Paper, Testnet, or Live execution environments.

## Related Wiki records

- `[[quant/crypto-high-frequency-kyles-lambda-price-impact-reversal-2026-08-31]]`
- `[[quant/crypto-multilevel-order-flow-imbalance-intraday-2026-08-31]]`
- `[[quant/crypto-hourly-bitcoin-walk-forward-cost-aware-execution-2026-09-01]]`
- `[[quant/hawkes-driven-otc-market-making-volterra-riccati-2026-09-01]]`

## Sources

- Barzykin, A., Boyce, R., Neuman, E., & Tuschmann, S. (2026). *Optimal Execution with Passive Market Impact*. arXiv preprint [arXiv:2607.28323v1](https://arxiv.org/abs/2607.28323) [math.OC, q-fin.TR]. Submitted July 30, 2026. DOI: [10.48550/arXiv.2607.28323](https://doi.org/10.48550/arXiv.2607.28323).
- Almgren, R., & Chriss, N. (2001). *Optimal execution of portfolio transactions*. Journal of Risk, 3, 5–40.
- Avellaneda, M., & Stoikov, S. (2008). *High-frequency trading in a limit order book*. Quantitative Finance, 8(3), 217–224.
- Cont, R., Kukanov, I., & Stoikov, S. (2014). *The price impact of order book events*. Journal of Financial Econometrics, 12(1), 47–88.
- Xu, K., Gould, M. D., & Samothrakis, S. (2023). *Multi-level order flow imbalance in limit order books*. arXiv preprint arXiv:1907.06514.
