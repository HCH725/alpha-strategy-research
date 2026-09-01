---
schema: strategy-research-record-v1
title: "Option Market Making with Hedging-Induced Market Impact: Stochastic Mixed Control, Permanent-Transient Propagator Coupling, and Neural Policy Optimization"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-making
  - options
  - delta-hedging
  - market-impact
  - stochastic-control
  - mixed-control
  - neural-policy
status: research-only
confidence: high
source_as_of: 2025-11-04
sources:
  - "Paulin Aubert, Etienne Chevalier, and Vathana Ly Vath, 'Option market making with hedging-induced market impact', arXiv:2511.02518v1 [q-fin.TR, math.OC], November 4, 2025. Published in Applied Mathematical Finance (2026). DOI: 10.1080/1350486X.2026. https://arxiv.org/abs/2511.02518"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Option Market Making with Hedging-Induced Market Impact: Stochastic Mixed Control, Permanent-Transient Propagator Coupling, and Neural Policy Optimization

## Provenance

- **Primary Source:** Paulin Aubert (Laboratoire de Mathématiques et Modélisation d'Évry, Université d'Évry Paris-Saclay), Etienne Chevalier (ENSIIE, Université Paris-Saclay), and Vathana Ly Vath (ENSIIE, Université Paris-Saclay), *"Option market making with hedging-induced market impact"*, arXiv preprint `arXiv:2511.02518v1 [q-fin.TR, math.OC]`, submitted November 4, 2025; published in *Applied Mathematical Finance* (2026). DOI: [10.1080/1350486X.2026](https://doi.org/10.1080/1350486X.2026). Full text: [https://arxiv.org/abs/2511.02518](https://arxiv.org/abs/2511.02518).
- **Subject Classifications:** Trading and Market Microstructure (`q-fin.TR`), Optimization and Control (`math.OC`).
- **Research Scope:** Classical option market making models (e.g., Avellaneda-Stoikov extensions for derivatives) assume that the market maker is an infinitesimal price-taker whose underlying delta-hedging transactions exert zero feedback on the underlying asset's price. Aubert, Chevalier, and Ly Vath develop a stochastic mixed control framework where the market maker's discrete re-hedging trades exert both permanent (linear price shift) and transient (propagator decay) market impact on the underlying. This induces a non-linear feedback loop: quoted option spreads influence option fill intensities (modeled via Cox processes), accumulated option inventory triggers underlying re-hedging impulses, and re-hedging impact moves the underlying spot price, altering subsequent option moneyness, inventory risk, and adverse selection. The authors prove well-posedness, characterize round-trip manipulation boundaries, and solve the mixed control problem via neural policy optimization.

## Economic mechanism

### Source-reported

1. **Hedging-Induced Endogenous Price Impact:** In liquid and semi-liquid options markets, market makers collectively account for a substantial portion of trading volume in the underlying asset when delta-hedging. Hedging purchases push the underlying price up, increasing call delta and requiring further buying (positive feedback), while hedging sales depress the price. Ignoring this endogenous impact leads to severe underestimation of execution costs and inventory risk.
2. **Coupled State Dynamics & Manipulation Risk:** When delta-hedging shifts underlying prices, naive market makers can be exploited by round-trip trading strategies or fall into destabilizing feedback loops. Incorporating transient impact decay $\rho e^{-\kappa (t - \tau)}$ and permanent impact $\lambda \Delta q$ directly into the Hamilton-Jacobi-Bellman (HJB) formulation eliminates artificial price manipulation opportunities.
3. **Mixed Control Formulation (Continuous Quoting + Discrete Hedging Impulses):** Quoting bid/ask spreads is a continuous action $(\delta_t^b, \delta_t^a)$ that modulates Poisson/Cox arrival rates of option counterparties. Conversely, re-hedging in the underlying market is an impulsive decision $(\tau_k, \xi_k)$ governed by transaction fees and market impact costs. Solving both controls jointly internalizes the cross-asset impact.

### Research interpretation

The falsifiable hypothesis is that **jointly optimizing option quoting skews and discrete underlying re-hedging thresholds under coupled permanent-transient impact dynamics avoids feedback-induced adverse selection and yields higher certainty-equivalent utility than decoupled Avellaneda-Stoikov quoting plus discrete delta-band hedging**:
- Traditional decoupled hedging causes market makers to over-quote and aggressively cross spreads in the underlying precisely when transient impact is at its peak.
- Coordinated mixed control widens option spreads on the side that would exacerbate existing underlying impact and delays re-hedging impulses until transient impact has partially decayed.

## Signal

### 1. Underlying Asset and Impact Dynamics

- **Mid-Price of Underlying Asset $S_t$:**
  $$S_t = S_0 + \int_0^t \sigma dW_s + \lambda \sum_{\tau_k \le t} \xi_k + D_t$$
  where $W_t$ is standard Brownian motion with volatility $\sigma$, $\lambda > 0$ represents the permanent impact parameter, $\xi_k \in \mathbb{R}$ represents the $k$-th impulsive hedging trade in the underlying, and $D_t$ represents the transient price impact state.
- **Transient Impact State $D_t$:**
  $$dD_t = -\kappa D_t dt + \gamma \sum_k \xi_k \delta(t - \tau_k)$$
  where $\kappa > 0$ is the resilience (decay rate) and $\gamma > 0$ is the transient impact coefficient.

### 2. Option Order Flow & Cox Intensity

- **Option Inventory $q_t \in \mathbb{Z}$:** Incremented by $+1$ on ask fills (trader buys from MM) and $-1$ on bid fills (trader sells to MM).
- **Arrival Intensities:** Modeled as state-dependent Cox intensities:
  $$\Lambda_t^a(\delta_t^a, S_t) = A_a \exp\left(-\beta_a \delta_t^a\right) \cdot \psi(S_t), \quad \Lambda_t^b(\delta_t^b, S_t) = A_b \exp\left(-\beta_b \delta_t^b\right) \cdot \psi(S_t)$$
  where $\delta_t^a = p_t^a - \mathcal{C}(S_t)$ and $\delta_t^b = \mathcal{C}(S_t) - p_t^b$ are the quoted half-spreads relative to theoretical option fair value $\mathcal{C}(S_t)$, and $\psi(S_t)$ captures moneyness-dependent arrival rate shifts.

### 3. Mixed Control Objective Function

- **Value Function $V(t, x, q, S, D, \nu)$:** Market maker maximizes expected terminal utility of wealth with risk aversion $\eta > 0$:
  $$V = \sup_{(\delta^a, \delta^b), (\tau_k, \xi_k)} \mathbb{E}\left[ -\exp\left(-\eta \left( X_T + q_T \mathcal{C}(S_T, T) + \nu_T S_T - \frac{\alpha_{\mathrm{liq}}}{2} (q_T^2 + \nu_T^2) \right)\right) \right]$$
  where $\nu_t = \sum_{\tau_k \le t} \xi_k$ is the accumulated underlying hedge inventory, $X_t$ is the cash account, and $\alpha_{\mathrm{liq}}$ is the terminal liquidation penalty.
- **Quasi-Variational Inequality (QVI):**
  $$\min\left( -\partial_t V - \mathcal{L}^{\delta} V, V - \mathcal{M} V \right) = 0$$
  where $\mathcal{L}^{\delta}$ is the continuous quoting differential operator and $\mathcal{M}$ is the impulse intervention operator:
  $$\mathcal{M} V(t, x, q, S, D, \nu) = \sup_{\xi} V(t, x - \xi (S + \lambda \xi + D) - c_{\mathrm{fixed}}, q, S + \lambda \xi, D + \gamma \xi, \nu + \xi)$$
- **Neural Policy Optimization:** Due to high state dimensionality $(t, q, S, D, \nu)$, the optimal feedback controls $\delta^*(t, q, S, D, \nu)$ and the impulse boundary/size $(\tau^*, \xi^*)$ are approximated using deep reinforcement learning / actor-critic policy networks trained via Monte Carlo trajectories.

## Required data

- **Universe:** Liquid option contracts (calls/puts) and their corresponding underlying spot or perpetual market.
- **Timeframe:** High-frequency tick and order-book snapshots (sub-second to 1-minute intervals).
- **Fields:** Option Level-2 book (bid/ask quotes, sizes, trades); underlying Level-2 book (bid/ask quotes, trade prints, aggressor flags); realized volatility $\sigma$; risk-free discount rate.
- **Microstructure Calibration:** Accurate empirical estimates for transient impact decay $\kappa$, transient impact coefficient $\gamma$, permanent impact $\lambda$, and order arrival parameters $(A_a, A_b, \beta_a, \beta_b)$.

## Execution assumptions

- **Option Quoting:** Passive limit orders posted at prices $p_t^b, p_t^a$; fills occur probabilistically according to Cox intensities.
- **Underlying Re-hedging:** Aggressive market orders executed at prevailing spot prices with immediate permanent impact $\lambda \xi$ and transient impact shift $\gamma \xi$.
- **Transaction Costs:** Fixed ticket fee $c_{\mathrm{fixed}}$ plus linear proportional fee $c_{\mathrm{prop}}$ on underlying re-hedging; exchange maker rebates earned on passive option fills.
- **Inventory Bounds:** Hard inventory limits $|q_t| \le Q_{\max}$ and $|\nu_t| \le \mathcal{N}_{\max}$.

## Evidence

### Source-reported

- **Theoretical Guarantees:**
  - The authors establish rigorous mathematical well-posedness of the coupled mixed control QVI.
  - They prove that incorporating transient propagator decay and permanent price impact rules out arbitrage and unbounded round-trip price manipulation strategies.
- **Numerical Policy Optimization Results:**
  - Neural policy optimization converges reliably to optimal state-dependent quoting skews and discrete impulse re-hedging frontiers.
  - In the presence of market impact, the optimal option quoting strategy exhibits an asymmetric spread expansion: when the market maker has a long call inventory ($q > 0$), they aggressively widen the ask spread to suppress further buy arrivals, because additional long inventory would force underlying re-hedging purchases that push the spot price higher, creating an expensive negative feedback loop.
  - Discrete impulse hedging with impact delays re-hedging until net delta imbalance exceeds an endogenous threshold band that widens as transient impact resilience $\kappa$ decreases.
  - Outperforms decoupled Avellaneda-Stoikov + naive delta-hedging baselines by significantly reducing cumulative impact-induced execution slippage.

### Independently reproduced

- Not independently reproduced.

### Negative evidence

- None identified in the reviewed sources; absence is not evidence of no negative result.
- Model performance is sensitive to misspecification of transient resilience rate $\kappa$; if market resilience is slower than estimated, re-hedging trades accumulate excessive transient price pressure, triggering premature liquidation penalties.

## Falsification plan

1. **Zero-Impact Decoupled Baseline Comparison:** Set impact parameters $\lambda = 0, \gamma = 0$ in the neural policy optimizer. If the resulting policy does not converge exactly to classical decoupled Avellaneda-Stoikov quoting plus classical impulse hedging within $1\%$ utility tolerance, the mixed control solver contains implementation artifacts.
2. **Resilience Parameter Perturbation:** Perturb transient decay rate $\kappa$ by $\pm 50\%$ during out-of-sample simulation without retraining the policy. If certainty-equivalent wealth drops below a naive fixed-band delta hedger, the policy network is over-specialized and lacks structural robustness.
3. **Execution Lag Stress Test:** Introduce an execution delay $\tau_{\mathrm{delay}} \in [100\mathrm{ms}, 1\mathrm{s}]$ between the impulse decision $\tau_k$ and the actual spot market fill. If net market making P&L turns negative due to adverse selection during the delay window, the continuous-time impulse assumption is invalid.
4. **Adverse Flow Toxicity Test:** Inject informed institutional order flow into the option arrival process (e.g., 20% of option trades accompanied by permanent spot price jumps). If the policy fails to widen quoting spreads sufficiently to prevent inventory accumulation on the wrong side, the Cox intensity formulation is falsified.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Crypto Adaptation Mechanism:**
  - In crypto markets, option market makers on centralized venues (Deribit) or decentralized protocols (Aevo, Derive, Lyra) actively delta-hedge their exposures on high-liquidity perpetual futures markets (Binance, Bybit, OKX, Hyperliquid).
  - The permanent and transient impact parameters $(\lambda, \gamma, \kappa)$ can be directly calibrated from perpetual order book depth and trade-flow recovery dynamics.
- **Crypto Portability Risks:**
  - Perpetual funding rates introduce an additional continuous carrying cost on the underlying hedge $\nu_t$, which must be integrated into the state space.
  - Crypto perpetual markets experience sudden liquidity gaps and flash crashes during liquidation cascades; transient impact resilience $\kappa$ can collapse to near zero during systemic deleveraging events, invalidating normal-regime impact estimators.

## Limitations

- **High-Dimensional Control Space:** Joint optimization of 2 continuous quoting controls and 2 discrete impulse variables across a 5-dimensional continuous state space $(t, q, S, D, \nu)$ is computationally demanding and requires deep RL training stability.
- **Stationary Impact Assumption:** The model assumes constant impact coefficients $(\lambda, \gamma, \kappa)$, whereas empirical order-book resilience fluctuates strongly with market volatility and time of day.
- **Single-Option Restriction:** The core mathematical framework is formulated for a representative option contract; scaling to full cross-strike/cross-maturity options books requires portfolio-level aggregation approximations.

## Implementation status

- Not implemented in our research stack.
- No PyBroker, NautilusTrader, paper, testnet, or live trading validation has been performed.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- This record represents theoretical and empirical research capture for quantitative intake review. It does not constitute authorization for deployment or capital allocation.

## Related Wiki records

- `[[quant/option-market-making-inventory-risk-quoting-spreads]]`
- `[[quant/market-impact-propagator-transient-resilience-models]]`
- `[[quant/stochastic-mixed-impulse-control-high-frequency-trading]]`

## Sources

- Paulin Aubert, Etienne Chevalier, and Vathana Ly Vath, "Option market making with hedging-induced market impact", arXiv preprint `arXiv:2511.02518v1 [q-fin.TR, math.OC]`, November 4, 2025. Published in *Applied Mathematical Finance* (2026). DOI: [10.1080/1350486X.2026](https://doi.org/10.1080/1350486X.2026). Full text: [https://arxiv.org/abs/2511.02518](https://arxiv.org/abs/2511.02518).
