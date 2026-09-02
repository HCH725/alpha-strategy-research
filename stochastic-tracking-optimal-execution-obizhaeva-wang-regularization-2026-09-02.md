---
schema: strategy-research-record-v1
title: "Stochastic Tracking for Optimal Execution under Transient Price Impact: Hilbert-Space Projection, Quadratic Rate Regularization, and Sharp Square-Root Convergence in Generalized Obizhaeva-Wang Models"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - optimal-execution
  - transient-price-impact
  - obizhaeva-wang
  - stochastic-tracking
  - central-risk-book
  - quadratic-regularization
  - besov-modulus
status: research-only
confidence: high
source_as_of: 2026-08-29
sources:
  - "Marcel Nutz and Moritz Voss, 'The Convergence Rate of Stochastic Tracking with Application to Optimal Execution', arXiv preprint arXiv:2608.29468v1 [q-fin.TR, q-fin.MF], August 29, 2026. DOI: 10.48550/arXiv.2608.29468. Stable URL: https://arxiv.org/abs/2608.29468"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Stochastic Tracking for Optimal Execution under Transient Price Impact: Hilbert-Space Projection, Quadratic Rate Regularization, and Sharp Square-Root Convergence in Generalized Obizhaeva-Wang Models

## Provenance

- **Primary Source:** Marcel Nutz (Columbia University, Departments of Statistics and Mathematics) and Moritz Voss (University of California, Los Angeles, Department of Mathematics), *"The Convergence Rate of Stochastic Tracking with Application to Optimal Execution"*, arXiv preprint `arXiv:2608.29468v1 [q-fin.TR, q-fin.MF]`, submitted August 29, 2026. DOI: [10.48550/arXiv.2608.29468](https://doi.org/10.48550/arXiv.2608.29468). Stable URL: [https://arxiv.org/abs/2608.29468](https://arxiv.org/abs/2608.29468).
- **Primary Subject Areas:** Trading and Market Microstructure (`q-fin.TR`), Mathematical Finance (`q-fin.MF`), Systems and Control (`math.OC`).
- **Research Scope:** In electronic trading and institutional central risk book (CRB) execution, traders unwind large positions while receiving stochastic client order flows over time. When market liquidity exhibits transient price impact—where trades push the limit order book away from the fundamental price and resilience gradually recovers depth—the canonical continuous-time framework is the Obizhaeva–Wang (2013) model. However, the theoretical optimal strategy in unregularized transient impact models is singular: it requires discrete block trades at inception and maturity, as well as continuous trading with infinite variation driven by updates to the random terminal order flow. In live market microstructure, such trading spikes leak massive information, incur severe non-linear slippage, and violate exchange order rate constraints. While practitioners regularize the problem by adding an instantaneous quadratic trading rate penalty ($\varepsilon u_t^2$), the regularized optimal policy lacks a closed-form solution and requires solving complex coupled backward stochastic differential equations (BSDEs). Nutz and Voss resolve this fundamental execution problem by mapping the regularized execution problem to a constrained stochastic quadratic tracking problem on a Hilbert space, deriving explicit non-asymptotic bounds via a Besov-type modulus, proving that regularized execution cost converges at the sharp rate $O(\sqrt{\varepsilon})$, and constructing an explicit, implementable feedback tracking strategy $Q^\varepsilon$ that achieves this optimal rate without solving the regularized BSDE.

## Economic mechanism

### Source-reported

1. **Transient Price Impact and Resilience Dynamics:** In contrast to permanent impact (Almgren–Chriss) where market impact accumulates linearly without decay, the Obizhaeva–Wang framework models transient price impact where execution pushes the order book by a displacement factor $\lambda_t$ (inverse market depth), which then decays exponentially at resilience rate $\beta_t$. The controlled price displacement process $Y_t^Q$ evolves as $dY_t^Q = -\beta_t Y_t^Q dt + \lambda_t dQ_t$.
2. **Singular Strategy Block Trades & Infinite Variation:** In the unregularized model, the optimal execution strategy $Q^*$ contains discrete block trades at $t=0$ and $t=T$ to exploit the initial and terminal resilience windows, while keeping the scaled price impact process $Y_t^* / \eta_t$ a martingale over the interior $(0, T)$. When the terminal inventory $\Xi_T$ is stochastic (learned dynamically from arriving order flow $\Xi_t = \mathbb{E}[\Xi_T \mid \mathcal{F}_t]$), $Q^*$ inherits the continuous martingale fluctuations of $\Xi_t$ and consequently exhibits infinite variation.
3. **Suppression of Trading Spikes via Quadratic Velocity Regularization:** To prevent instantaneous spikes that signal intent and invite front-running, the execution desk penalizes velocity by $\varepsilon \int_0^T u_t^2 dt$, forcing the strategy $Q \in \mathcal{Q}_{\text{ac}}$ to be absolutely continuous ($dQ_t = u_t dt$).
4. **Hilbert Space Distance Equivalence:** The excess execution cost of any strategy $Q$ relative to the singular optimizer $Q^0$ is mathematically identical to the squared norm $\|Y^Q - Y^0\|_\mathcal{H}^2$ in an impact Hilbert space $\mathcal{H}$, which in turn is bounded by a constant multiple of the squared inventory tracking error $\mathbb{E}\int_0^T |Q_t - Q_t^0|^2 dt$. Thus, optimal regularized execution reduces to stochastic quadratic tracking of $Q^0$ under the terminal constraint $Q_T = \Xi_T$.
5. **Two-Phase Feedback Strategy Construction:** Rather than solving an intractable BSDE, the trader operates an explicit two-phase strategy $Q^\varepsilon$: an exponential smoothing filter targeting $Q^0$ with relaxation scale $\sqrt{\varepsilon}$ on $[0, T-\sqrt{\varepsilon}]$, followed by an asymptotically singular terminal bridge on $[T-\sqrt{\varepsilon}, T)$ that forces $Q_T^\varepsilon \to \Xi_T$ almost surely.

### Research interpretation

The falsifiable thesis is that **in electronic limit order books with transient price impact and stochastic order flow, smoothing singular execution via quadratic velocity regularization incurs an excess execution cost that scales strictly as $O(\sqrt{\varepsilon})$, and this theoretical lower bound is fully saturated by a two-phase explicit feedback tracker without solving the regularized BSDE**:
- The square-root rate $O(\sqrt{\varepsilon})$ is governed by the $L^2$ time-translation modulus (roughness) of the underlying semimartingale inventory target; because semimartingales have a finite time-translation seminorm, smoothing cannot converge faster than $\sqrt{\varepsilon}$.
- Attempting to track the singular inventory $Q^0$ with sub-optimal heuristics (such as TWAP or unconstrained exponential smoothing) incurs severe terminal mismatch penalties $\Theta(\sqrt{\varepsilon})$ or fails terminal delivery; concatenating an exponential filter with an explicit terminal bridge achieves minimal price impact drag.

## Signal

### 1. Market Dynamics and Unregularized Problem

Let $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \in [0,T]}, \mathbb{P})$ be a filtered probability space. Let $\beta, \lambda: [0, T] \to (0, \infty)$ be deterministic, bounded functions with $\beta$ càdlàg of finite variation, $\lambda$ absolutely continuous with derivative $\dot{\lambda}$ of finite variation, $\gamma_t = \log(\lambda_t)$, and $2\beta_t + \dot{\gamma}_t > c > 0$ (precluding price manipulation).
Define auxiliary deterministic functions:
$$\eta_t = \lambda_t \exp\left( \int_0^t (\beta_s + \dot{\gamma}_s) ds \right), \quad \theta_t = \int_0^t \frac{\beta_s + \dot{\gamma}_s}{\eta_s} ds$$
Let $S \in \mathcal{S}^2$ be the unaffected martingale price, and $Q \in \mathcal{Q}$ be a càdlàg semimartingale inventory strategy satisfying $Q_{0-} = 0$ and terminal constraint $Q_T = \Xi_T \in L^2(\mathcal{F}_T)$. The price impact process $Y = Y^Q$ satisfies:
$$Y_t^Q = e^{-\int_0^t \beta_s ds} y + \int_{[0, t]} e^{-\int_s^t \beta_r dr} \lambda_s dQ_s$$
The execution cost functional is:
$$J_0(Q) = \mathbb{E}\left[ \int_{[0, T]} (S_{t-} + Y_{t-}^Q) dQ_t + \frac{1}{2} \sum_{0 \le t \le T} \lambda_t (\Delta Q_t)^2 \right] = \mathbb{E}\left[ \int_{[0, T]} Y_{t-}^Q dQ_t + \frac{1}{2} \sum_{0 \le t \le T} \lambda_t (\Delta Q_t)^2 \right]$$

### 2. Hilbert Space Formulation & Singular Solution

Define the Hilbert space $\mathcal{H}$ of progressively measurable processes equipped with inner product:
$$\langle X, Y \rangle_\mathcal{H} = \mathbb{E}\left[ \int_0^T X_t Y_t (2\beta_t + \dot{\gamma}_t)\lambda_t^{-1} dt + X_T Y_T \lambda_T^{-1} + X_0 Y_0 \lambda_0^{-1} \right]$$
Then the terminal constraint $Q_T = \Xi_T$ defines a closed affine subspace $\mathcal{Y} \subset \mathcal{H}$. By Theorem 4.2, the unique optimal unregularized strategy $Q^0 \in \mathcal{Q}$ is:
$$Q_t^0 = \Xi_t - \frac{1}{\eta_t} M_t + \frac{1}{\lambda_0 \eta_t (\theta_T - \theta_t + \eta_0^{-1} + \eta_T^{-1})} \left[ y + \lambda_0 \Xi_{0-} + \lambda_0 \int_0^T (\theta_T - \theta_s + \eta_T^{-1}) d\Xi_s \right]$$
where $M_t = \mathbb{E}[M_T \mid \mathcal{F}_t]$ is a square-integrable martingale.
$Q^0$ incurs discrete block trades at the boundaries:
$$\Delta Q_0^0 = \frac{1}{\lambda_0}(Y_0^0 - y), \quad \Delta Q_T^0 = \Xi_T - Q_{T-}^0$$

### 3. Regularized Execution & The Explicit Feedback Tracker

For regularization parameter $\varepsilon > 0$, the admissible class is absolutely continuous strategies $\mathcal{Q}_{\text{ac}} = \{Q : dQ_t = u_t dt, \mathbb{E}\int_0^T u_t^2 dt < \infty, Q_T = \Xi_T\}$, minimizing:
$$J_\varepsilon(Q) = J_0(Q) + \frac{\varepsilon}{2} \mathbb{E}\left[ \int_0^T u_t^2 dt \right]$$
Instead of solving the intractable regularized BSDE, the trader implements the explicit two-phase strategy $Q^\varepsilon \in \mathcal{Q}_{\text{ac}}$ (Lemma 5.5):
Set $s = T - \sqrt{\varepsilon}$. The trading rate $u_t^\varepsilon = \dot{Q}_t^\varepsilon$ is defined by the Markovian feedback rule:
$$u_t^\varepsilon = \begin{cases} \frac{1}{\sqrt{\varepsilon}} \left( Q_t^0 - Q_t^\varepsilon \right), & 0 \le t \le T - \sqrt{\varepsilon} \\ \frac{\Xi_t - Q_t^\varepsilon}{T - t} + N_t, & T - \sqrt{\varepsilon} \le t < T \end{cases}$$
where the terminal bridge correction $N_t$ is:
$$N_t = \frac{1}{T - t} \int_t^T \frac{T - r}{T - t} d\Xi_r$$
- **Phase 1 ($t \in [0, T-\sqrt{\varepsilon}]$):** Exponential tracking of the unregularized inventory $Q^0$ with time constant $\sqrt{\varepsilon}$.
- **Phase 2 ($t \in [T-\sqrt{\varepsilon}, T)$):** Stochastic bridge pulling the inventory to the terminal order flow $\Xi_T$, satisfying $\lim_{t \uparrow T} Q_t^\varepsilon = \Xi_T$ $\mathbb{P}$-almost surely.

## Required data

- **Asset Universe:** Liquid equities, equity index futures, FX forwards, or crypto perpetuals/spot order books.
- **Microstructure Inputs:**
  - Order book resilience parameter $\beta_t > 0$ (speed of limit order book replenishment, estimated from high-frequency tick book recovery).
  - Market depth parameter $\lambda_t > 0$ (price impact per share traded, estimated from Kyle's lambda or order flow imbalance regression).
  - Initial price displacement $y = Y_{0-} \in \mathbb{R}$ (prevailing imbalance in the order book prior to execution).
- **Stochastic Target Process:** Cumulative incoming order flow / execution mandate $\Xi_t = \mathbb{E}[\Xi_T \mid \mathcal{F}_t]$, where $\Xi_T \in L^2(\mathcal{F}_T)$ satisfies the reachability condition:
  $$\int_0^T \frac{1}{T-t} d\mathbb{E}[\Xi_t^2] < \infty$$
- **Timeframe & Resolution:** High-frequency intraday execution horizon $T \in [5 \text{ minutes}, 1 \text{ day}]$; discrete simulation / order slicing at sub-second to second resolution ($\Delta t \ll \sqrt{\varepsilon}$).

## Execution assumptions

- **Execution Model:** Continuous limit/market order placement under transient price impact; marginal fill price given by $S_{t-} + Y_{t-}^Q$.
- **Trading Velocity Bounds:** Absolutely continuous controls $u_t \in L^2(\Omega \times [0, T])$; quadratic regularization penalty parameter $\varepsilon \in (0, T^2/4]$.
- **Terminal Fulfillment:** Exact terminal delivery $Q_T^\varepsilon = \Xi_T$ enforced almost surely via the terminal bridge.
- **No-Arbitrage Constraint:** $2\beta_t + \dot{\gamma}_t > c > 0$ strictly enforced to guarantee absence of price manipulation and transaction cycle arbitrage.

## Evidence

### Source-reported

All mathematical bounds and quantitative convergence rates below are directly cited from Nutz and Voss (arXiv:2608.29468v1, August 29, 2026):

1. **Non-Asymptotic Bound on Excess Price Impact Cost (Theorem 5.7):**
   For every $0 < \varepsilon \le T^2/4$, the explicit feedback strategy $Q^\varepsilon$ satisfies:
   $$J_0(Q^\varepsilon) - J_0(Q^0) \le C_1 \sqrt{\varepsilon}$$
   where $C_1 = 4 C_Y^2 (m_2 A_\alpha^2 + 3 T C_0 + 6 T K_0 + 6 \Lambda(\sqrt{\varepsilon}))$, with $C_Y$ being the Lipschitz constant of the impact map ($C_Y \le 2(1 + T\bar{\beta})\bar{\lambda} + 2\bar{\lambda}V_\lambda$).
2. **Sharp Value Function Convergence (Theorem 5.7 & Corollary 5.8):**
   The total regularized execution cost $J_\varepsilon(Q^\varepsilon)$ above the unregularized value $V(0) = J_0(Q^0)$ satisfies:
   $$J_\varepsilon(Q^\varepsilon) - V(0) \le (C_1 + C_2) \sqrt{\varepsilon}$$
   Consequently, the regularized value function $V(\varepsilon) = \inf_{Q \in \mathcal{Q}_{\text{ac}}} J_\varepsilon(Q)$ satisfies:
   $$0 \le V(\varepsilon) - V(0) \le (C_1 + C_2) \sqrt{\varepsilon}$$
   establishing that the regularized execution value converges to the unregularized singular value at rate **$O(\sqrt{\varepsilon})$**.
3. **Inventory Tracking Convergence:**
   The $L^2$ distance between the explicit tracker $Q^\varepsilon$ and the singular optimizer $Q^0$ vanishes at rate $O(\varepsilon^{1/4})$:
   $$\mathbb{E}\left[ \int_0^T |Q_t^\varepsilon - Q_t^0|^2 dt \right] \le 2(C_0 + 2K_0) T \sqrt{\varepsilon} + 2 \Lambda(\sqrt{\varepsilon}) \sqrt{\varepsilon} = O(\sqrt{\varepsilon})$$
   and the true regularized optimizer $Q^{*,\varepsilon}$ satisfies the identical bound:
   $$\mathbb{E}\left[ \int_0^T |Q_t^{*,\varepsilon} - Q_t^0|^2 dt \right] \le \frac{C_1 + C_2}{C_\beta} \sqrt{\varepsilon}$$
4. **Sharpness in the Benchmark Obizhaeva–Wang Case (Proposition 5.9):**
   In the classical setting with constant $\beta > 0, \lambda > 0$, deterministic terminal target $\Xi_T \neq 0$, and zero initial impact $y=0$:
   $$V(\varepsilon) - V(0) = \frac{\sqrt{\lambda}}{2(\beta T + 2)^2} \Xi_T^2 \sqrt{\varepsilon} + o(\sqrt{\varepsilon})$$
   proving that the convergence rate $O(\sqrt{\varepsilon})$ is exact and cannot be improved by any absolutely continuous execution policy.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Singular Control Failure in Discrete Execution:** Attempting to execute the unregularized singular strategy $Q^0$ directly in electronic markets fails due to the infinite variation term: discretizing a continuous martingale with non-zero quadratic variation leads to discrete trading steps that blow up transaction costs as $\Delta t \to 0$.
- **Terminal Bridge Instability near Horizon:** As $t \to T$, the denominator $(T-t)$ in the terminal bridge feedback rule $u_t^\varepsilon = \frac{\Xi_t - Q_t^\varepsilon}{T-t} + N_t$ approaches zero. If the reachability condition $\int_0^T \frac{1}{T-t} d\mathbb{E}[\Xi_t^2] < \infty$ is violated (e.g., if order flow surprises arrive with discrete jumps near maturity), the required trading velocity diverges, leading to severe execution penalties.
- **Absence of Rate Acceleration:** Unlike smooth deterministic targets where tracking error can decay as $O(\varepsilon)$, stochastic targets driven by Brownian order flow cannot achieve an approximation rate faster than $O(\sqrt{\varepsilon})$.

## Falsification plan

1. **Empirical Slippage vs. $\sqrt{\varepsilon}$ Scaling Test:** In a tick-level limit order book simulator (or market replay), calibrate resilience $\beta$ and depth $\lambda$. Execute a random terminal order $\Xi_T$ across grid values of the penalty $\varepsilon \in [10^{-5}, 10^{-1}]$. Fit the log-log regression $\log(J_\varepsilon - J_0) = a + b \log(\varepsilon)$. If the empirical slope $b$ deviates significantly from $0.50$ ($b < 0.40$ or $b > 0.60$), the theoretical square-root tracking rate is falsified.
2. **Terminal Bridge vs. TWAP Benchmark:** Compare $Q^\varepsilon$ against a naive execution baseline that executes via exponential tracking until $T-\sqrt{\varepsilon}$ and dumps remaining inventory via constant TWAP. If the explicit terminal bridge does not reduce total execution cost by at least $15\%$ relative to the naive TWAP completion across 1,000 Monte Carlo order flow paths, the terminal bridge formulation is falsified as ineffective.
3. **Transient vs. Permanent Impact Breakdown:** Test the strategy in an asset whose price impact is predominantly permanent ($\beta \approx 0$). If the resilience decay fails to materialize, the strategy overtrades in Phase 1, generating excess slippage relative to standard Almgren–Chriss.
4. **Rejection Threshold:** Reject the execution strategy if realized implementation shortfall exceeds the theoretical bound $(C_1 + C_2)\sqrt{\varepsilon}$ by more than $20\%$, or if order velocity at $T - \Delta t$ breaches venue rate limits.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Application to Crypto Perpetual Central Risk Books:** Applicable to market makers and institutional execution desks unwinding inventory on high-throughput venues (Binance, OKX, Hyperliquid, Bybit).
- **Resilience Dynamics in Crypto:** Crypto limit order books display rapid resilience ($\beta$ on the order of seconds) driven by algorithmic quoting bots, but suffer severe depth fragility ($\lambda$ spikes) during liquidation cascades.
- **Funding Rate Interaction:** For positions held across 8-hour funding intervals, the execution horizon $T$ must consider the funding fee drift; holding inventory across funding timestamps introduces an asymmetric holding cost not captured in pure Obizhaeva–Wang models.
- **Venue Latency & Discrete Block Execution:** Sub-second latency jitter and batch auctions (or Solana slot boundaries) prevent continuous velocity execution; the continuous rate $u_t^\varepsilon$ must be discretized into discrete child slices (e.g., via TWAP/VWAP sub-intervals of length $\Delta t \le \sqrt{\varepsilon}/10$).

## Limitations

- **Linear Price Impact Restriction:** The model assumes price displacement is linear in trade size ($\lambda dQ_t$); square-root price impact laws (Barra / Almgren square-root) are not covered by the quadratic Hilbert-space duality.
- **Deterministic Liquidity Parameters:** Resilience $\beta_t$ and depth $\lambda_t$ are assumed deterministic and known upfront; stochastic liquidity regimes (e.g., sudden order book vacuum during macro news) are omitted.
- **Unconstrained Inventory Space:** The tracking strategy $Q^\varepsilon$ does not enforce strict interim inventory caps $|Q_t| \le Q_{\max}$, which could lead to margin violations during extreme order flow surges.

## Implementation status

`not-implemented` in the quantitative production stack.

## Adoption boundary

Research capture only. A record being present in this repository does not constitute authorization for deployment, implementation in PyBroker/Nautilus, or allocation of capital in paper, testnet, or live trading.

## Related Wiki records

- `[[quant/execution-impact-capacity-almgren-square-root-2026-08-28]]`
- `[[quant/crypto-perpetual-optimal-liquidation-funding-rate-hjb-2026-09-02]]`
- `[[quant/sequential-limit-order-execution-quoting-signal-adaptive-triangular-hjb-2026-09-02]]`
- `[[quant/signature-optimal-execution-statistical-arbitrage-quadratic-reduction-2026-09-02]]`
- `[[quant/passive-market-impact-optimal-execution-mlofi-2026-09-02]]`

## Sources

1. Marcel Nutz and Moritz Voss, *"The Convergence Rate of Stochastic Tracking with Application to Optimal Execution"*, arXiv preprint `arXiv:2608.29468v1 [q-fin.TR, q-fin.MF]`, August 29, 2026. DOI: [10.48550/arXiv.2608.29468](https://doi.org/10.48550/arXiv.2608.29468). Stable URL: [https://arxiv.org/abs/2608.29468](https://arxiv.org/abs/2608.29468).
2. Anna Obizhaeva and Jiang Wang, *"Optimal Consumption and Portfolio Selection with Lognormal Prices"*, *Journal of Financial Markets*, 16(1):1–32, 2013.
3. Peter Bank, H. Mete Soner, and Moritz Voß, *"Hedging with Temporary Price Impact"*, *Mathematics and Financial Economics*, 11(2):223–239, 2017.
4. Marcel Nutz, Stephen Webster, and Long Zhao, *"Optimal Liquidation in a Central Risk Book"*, *Mathematical Finance*, 34(3):885–918, 2024.
