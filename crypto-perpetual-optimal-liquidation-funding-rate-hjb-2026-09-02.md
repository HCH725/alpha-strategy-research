---
schema: strategy-research-record-v1
title: "Optimal Liquidation of Perpetual Contracts under Continuous Funding Rate Payments and Price Impact: HJB Dimensional Reduction and Linear Feedback Speed"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto-perpetuals
  - optimal-liquidation
  - funding-rate
  - market-impact
  - stochastic-control
  - hjb-equation
status: research-only
confidence: high
source_as_of: 2026-01-15
sources:
  - "Ryan Donnelly, Junhan Lin, Matthew Lorig, 'Optimal Liquidation of Perpetual Contracts', arXiv:2601.10812v1 [q-fin.TR, q-fin.CP], January 15, 2026. DOI: 10.48550/arXiv.2601.10812. https://arxiv.org/abs/2601.10812"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Optimal Liquidation of Perpetual Contracts under Continuous Funding Rate Payments and Price Impact: HJB Dimensional Reduction and Linear Feedback Speed

## Provenance

- **Primary Source:** Ryan Donnelly (King's College London), Junhan Lin (University of Washington), Matthew Lorig (University of Washington), *"Optimal Liquidation of Perpetual Contracts"*, arXiv preprint `arXiv:2601.10812v1 [q-fin.TR, q-fin.CP]`, published January 15, 2026. DOI: [10.48550/arXiv.2601.10812](https://doi.org/10.48550/arXiv.2601.10812). Full text: [https://arxiv.org/abs/2601.10812](https://arxiv.org/abs/2601.10812).
- **Primary Subject Areas:** Trading and Market Microstructure (`q-fin.TR`), Computational Finance (`q-fin.CP`).
- **Context:** Classical execution frameworks (e.g., Almgren-Chriss, 2000; Guéant, 2016) optimize the trade-off between temporary/permanent price impact and inventory price risk over a finite horizon $[0, T]$, but assume zero cash-flow carrying cost. In cryptocurrency perpetual futures (swaps), holding an inventory position incurs or receives a continuous funding rate payment proportional to the basis between the perpetual contract price $P_t$ and the underlying spot/index price $S_t$. Donnelly, Lin, and Lorig solve the stochastic control problem of liquidating a perpetual contract position before time $T$ while explicitly incorporating continuous funding cash flows alongside temporary and permanent price impact.

## Economic mechanism

### Source-reported

1. **Perpetual Basis and Funding Dynamics:** Perpetual futures lack a fixed expiration date. To anchor the perpetual market price $P_t$ to the underlying spot/index price $S_t$, exchanges enforce continuous funding payments where long position holders pay short holders (or vice versa) a rate proportional to $P_t - \psi(S_t)$ (typically linear, $\psi(S_t) = S_t$).
2. **Tripartite Trade-Off in Perpetual Execution:** An executing trader liquidating an inventory position $q_0 	o q_T = 0$ faces three simultaneous costs:
   - **Market Impact Costs:** Immediate slippage and price depression from trading speed $
u_t = \dot{q}_t$.
   - **Inventory Price Variance Risk:** Unhedged market volatility $\phi \int_0^T q_t^2 dt$ over the liquidation horizon.
   - **Carrying Cost / Benefit via Funding:** If the trader holds a long position ($q_t > 0$) while the basis is positive ($P_t > S_t$), they continuously bleed funding payments, creating an incentive to accelerate liquidation. Conversely, if $P_t < S_t$, the trader receives funding payments, providing an economic incentive to decelerate liquidation and capture yield while managing price risk.
3. **Dimensional Reduction in Stochastic Control:** Because funding depends strictly on the spread $Z_t = P_t - S_t$, the value function in the Hamilton-Jacobi-Bellman (HJB) formulation reduces dimensionality from $(P_t, S_t)$ to the single basis state variable $Z_t$, allowing an exact closed-form solution for linear payoff structures.

### Research interpretation

The falsifiable thesis is that **incorporating real-time funding rate basis $Z_t = P_t - S_t$ into stochastic optimal execution schedules yields strictly lower implementation shortfall (total execution cost + risk penalty) than traditional Almgren-Chriss TWAP/VWAP execution schedules in cryptocurrency perpetual markets**:
- When basis and inventory have the same sign ($q_t \cdot Z_t > 0$), holding the perpetual position incurs net negative carry; optimal liquidation speed is strictly higher than Almgren-Chriss baseline.
- When basis and inventory have opposite signs ($q_t \cdot Z_t < 0$), holding the perpetual position collects positive carry; optimal liquidation speed dynamically slows down, monetizing funding yield until basis mean-reverts or terminal time $T$ approaches.

## Signal

### 1. State Variables & Market Dynamics

Let:
- $q_t \in \mathbb{R}$: Inventory position of the agent at time $t \in [0, T]$, with initial inventory $q_0$ and required terminal liquidation $q_T = 0$.
- $
u_t = \dot{q}_t$: Trading velocity (control variable), where $
u_t < 0$ denotes selling / liquidating a long position.
- $S_t$: Spot / index price following arithmetic Brownian motion:
  $$dS_t = \sigma_S dW_t^S$$
- $P_t$: Perpetual contract price affected by spot drift, basis mean reversion $\kappa$, and permanent market impact parameter $\gamma$:
  $$dP_t = dS_t - \kappa (P_t - S_t) dt + \gamma 
u_t dt + \sigma_P dW_t^P$$
  with $\operatorname{Corr}(dW_t^S, dW_t^P) = ho_{SP}$.
- $Z_t \equiv P_t - S_t$: Basis / premium process following an Ornstein-Uhlenbeck process modified by permanent impact:
  $$dZ_t = -\kappa Z_t dt + \gamma 
u_t dt + \sigma_Z dW_t^Z$$
  where $\sigma_Z^2 = \sigma_P^2 + \sigma_S^2 - 2 ho_{SP} \sigma_P \sigma_S$.

### 2. Wealth & Cash-Flow Evolution

The agent's cash / wealth process $X_t$ evolves according to:
$$dX_t = -
u_t (P_t + \eta 
u_t) dt - ho_{\mathrm{fund}} q_t (P_t - \psi(S_t)) dt$$
where:
- $\eta > 0$ is the temporary price impact parameter (execution price $P_t + \eta 
u_t$).
- $ho_{\mathrm{fund}} > 0$ is the funding payment frequency parameter (e.g., annualized 8-hour rate frequency).
- $\psi(S_t) = S_t$ for standard linear funding contracts.

### 3. Stochastic Control Objective & HJB Solution

The agent maximizes expected utility over terminal wealth minus quadratic inventory risk penalty $\phi > 0$:
$$V(t, x, q, p, s) = \sup_{
u \in \mathcal{A}} \mathbb{E} \left[ X_T + q_T P_T - \phi \int_t^T q_u^2 du \;\Big|\; X_t=x, q_t=q, P_t=p, S_t=s ight]$$
with boundary condition $q_T = 0$.

Exploiting the ansatz $V(t, x, q, p, s) = x + q p + h(t, q, z)$ where $z = p - s$:
The excess value function $h(t, q, z)$ satisfies the parabolic PDE:
$$\partial_t h - \phi q^2 - ho_{\mathrm{fund}} q z - \kappa z \partial_z h + rac{1}{2} \sigma_Z^2 \partial_{zz} h + \sup_{
u} \left\{ 
u \left( -(\eta - rac{1}{2}\gamma) 
u + \partial_q h + \gamma \partial_z h ight) ight\} = 0$$

Using the quadratic ansatz:
$$h(t, q, z) = A(t) q^2 + B(t) q z + C(t) z^2 + D(t)$$
the optimal feedback trading speed $
u_t^*(q_t, z_t)$ is given in closed form by:
$$
u_t^*(q_t, Z_t) = rac{2 A(t) + \gamma B(t)}{2 \eta - \gamma} q_t + rac{B(t) + 2 \gamma C(t)}{2 \eta - \gamma} Z_t \equiv lpha(t) q_t + eta(t) Z_t$$
where $A(t), B(t), C(t)$ solve a coupled system of deterministic Riccati ordinary differential equations:
$$\dot{A}(t) = \phi - rac{(2 A(t) + \gamma B(t))^2}{4 (\eta - rac{1}{2}\gamma)}$$
$$\dot{B}(t) = ho_{\mathrm{fund}} + \kappa B(t) - rac{(2 A(t) + \gamma B(t))(B(t) + 2 \gamma C(t))}{2 (\eta - rac{1}{2}\gamma)}$$
$$\dot{C}(t) = 2 \kappa C(t) - rac{(B(t) + 2 \gamma C(t))^2}{4 (\eta - rac{1}{2}\gamma)}$$
with terminal boundary conditions $A(T) 	o -\infty$ (enforcing $q_T = 0$), $B(T) = 0$, $C(T) = 0$.

### 4. Non-Linear Payoffs & Short-Time Asymptotics

For non-linear funding payoff functions $\psi(S)$ (e.g., capped funding brackets or inverse contracts):
- The value function is expanded via a perturbation series in powers of $ho_{\mathrm{fund}}$ or trading horizon $	au = T - t$.
- At leading order, the optimal strategy recovers the linear feedback formula with an effective basis correction $	ilde{Z}_t = P_t - \mathbb{E}[\psi(S_t) \mid S_t]$.

## Required data

- **Universe:** Cryptocurrency Perpetual Swaps (e.g., BTC-USDT-PERP, ETH-USDT-PERP, SOL-USDT-PERP on Binance, Bybit, OKX, Hyperliquid).
- **Timeframe:** High-frequency tick-by-tick and 1-second sampled quotes and trades.
- **Fields:**
  - $P_t$: Perpetual top-of-book mid-price and micro-price.
  - $S_t$: Spot index / oracle price published by the exchange.
  - $Z_t = P_t - S_t$: Real-time basis.
  - Continuous / 8-hour funding rate schedules ($ho_{\mathrm{fund}}$).
  - Taker trade volume for calibrated impact parameters ($\eta, \gamma$).
- **Point-in-Time Integrity:** All oracle index prices and perpetual prices must be synchronized without timestamp lag.

## Execution assumptions

- **Order Type:** Algorithmic continuous limit / aggressive taker orders modulated by trading velocity $
u_t^*$.
- **Impact Model:** Linear temporary impact $\eta 
u_t$ and permanent price impact $\gamma 
u_t$.
- **Trading Horizon:** Finite execution window $T \in [5	ext{ min}, 4	ext{ hours}]$.
- **Terminal Liquidation:** Hard terminal boundary $q_T = 0$ enforced by terminal penalty.

## Evidence

### Source-reported

All analytical and structural claims trace directly to Donnelly, Lin, & Lorig (arXiv:2601.10812v1, Sections 2–4, Propositions 1–3, and Figures 1–4):
1. **Analytical Closed-Form Solvability:** For linear payoff contracts ($\psi(s) = s$), the multi-dimensional HJB equation reduces exactly to a 1-dimensional system of Riccati ODEs.
2. **Monotonicity of Control Coefficients:** The inventory coefficient $lpha(t)$ and basis coefficient $eta(t)$ in the optimal trading speed $
u_t^*(q_t, Z_t) = lpha(t) q_t + eta(t) Z_t$ are proven to be strictly negative for all $t \in [0, T)$.
3. **Carry-Induced Execution Asymmetry:**
   - When liquidating a long position ($q_t > 0$), a positive basis ($Z_t > 0$) strictly accelerates liquidation speed ($
u_t^*$ becomes more negative) to truncate funding drain.
   - A negative basis ($Z_t < 0$) decelerates liquidation speed, retaining inventory to collect the funding rate rebate.
4. **Asymptotic Convergence:** For non-linear payoffs, the first-order short-time asymptotic expansion matches the linear closed-form policy within $O(T^2)$ error bounds.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- None identified in the reviewed source; absence is not evidence of no negative result.
- However, if the basis $Z_t$ exhibits severe jump-diffusion or regimes of unpegging (e.g., stablecoin de-peg or extreme short squeezes where $\kappa 	o 0$), the linear mean-reverting Ornstein-Uhlenbeck assumption breaks down, leading to sub-optimal execution schedules.

## Falsification plan

1. **Almgren-Chriss Benchmark Comparison:** Run parallel simulated and paper-trade liquidations of 1,000 randomized inventory blocks ($10	ext{--}100$ BTC) comparing the Donnelly-Lin-Lorig funding-aware policy against a standard Almgren-Chriss TWAP/AC policy under historical Binance/Hyperliquid tick data. If the funding-aware policy fails to achieve a lower Implementation Shortfall (IS) by at least 1.5 bps in high funding regimes ($|ho_{\mathrm{fund}}| > 30\%$ APR), reject the execution advantage.
2. **Basis Directional Stress Test:** Artificially invert the basis signal ($Z_t 	o -Z_t$). If the inverted execution schedule does not experience statistically significant higher implementation costs ($p < 0.01$), the policy's theoretical carry optimization is non-functional.
3. **Mean-Reversion Sensitivity ($\kappa 	o 0$):** Perturb the calibrated basis mean-reversion parameter $\kappa$ across $[0.1 	imes \hat{\kappa}, 10 	imes \hat{\kappa}]$. If execution slippage degrades by $> 25\%$ under parameter perturbation, the model lacks operational robustness.

## Crypto portability

**Portability Status:** `direct`.

- **Mechanism Portability:** This framework is natively designed for cryptocurrency perpetual futures markets (Binance Futures, Hyperliquid, Bybit, dYdX).
- **Crypto-Specific Dynamics:**
  - Standard perpetuals charge funding continuously or in discrete 8-hour / 1-hour epochs based on TWAP $(P_t - S_t)$. The continuous approximation $ho_{\mathrm{fund}} q_t (P_t - S_t) dt$ maps directly onto continuous-funding DEXs (Hyperliquid, Drift) and serves as an accurate proxy for centralized exchange epochs.
  - Multi-collateral margin and inverse contract variants map to the non-linear payoff approximation $\psi(S_t) 
eq S_t$.

## Limitations

- **Stationary Parameter Assumption:** Assumes constant impact coefficients $(\eta, \gamma)$ and mean-reversion speed $\kappa$, whereas empirical order book depth and basis volatility fluctuate dynamically during market volatility spikes.
- **Continuous Trading Approximation:** Assumes continuous execution rates $
u_t$; discrete order sizing and exchange rate limits (API rate limits, minimum lot sizes) require quantization.
- **Oracle / Spot Index Latency:** Discrepancies between the exchange index feed $S_t$ and composite spot prices can introduce basis estimation noise.

## Implementation status

`not-implemented`

No implementation has been conducted in the local research repository, PyBroker, NautilusTrader, paper, testnet, or live trading systems.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

This record is an upstream research capture. It does not authorize strategy implementation, backtesting promotion, or production deployment.

## Related Wiki records

- `[[funding-aware-market-making-perpetual-dex-2026-08-31]]`
- `[[perpetual-inverse-linear-margin-currency-funding-spread-2026-09-01]]`
- `[[passive-market-impact-optimal-execution-mlofi-2026-09-02]]`

## Sources

- Ryan Donnelly, Junhan Lin, Matthew Lorig, *"Optimal Liquidation of Perpetual Contracts"*, arXiv preprint `arXiv:2601.10812v1 [q-fin.TR, q-fin.CP]`, submitted January 15, 2026. DOI: `10.48550/arXiv.2601.10812`. URL: [https://arxiv.org/abs/2601.10812](https://arxiv.org/abs/2601.10812).
