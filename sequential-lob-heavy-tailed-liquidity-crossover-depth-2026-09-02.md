---
schema: strategy-research-record-v1
title: "Heavy-Tailed Liquidity Demand, Crossover Depth, and Power-Law Impact in Sequential Limit Order Books"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - limit-order-book
  - market-microstructure
  - market-impact
  - heavy-tails
  - student-t
  - asymmetric-information
  - crossover-depth
  - bayesian-learning
  - adverse-selection
status: research-only
confidence: high
source_as_of: 2026-07-02
sources:
  - "Umut Çetin, Mingwei Lin, and Giulia Livieri, 'When large trades are not news: Liquidity tail risk and price discovery', arXiv:2607.01198v1 [q-fin.TR], July 2, 2026. DOI: 10.48550/arXiv.2607.01198. https://arxiv.org/abs/2607.01198"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Heavy-Tailed Liquidity Demand, Crossover Depth, and Power-Law Impact in Sequential Limit Order Books

## Provenance

- **Primary Source:** Umut Çetin (London School of Economics), Mingwei Lin (LSE / Peking University), and Giulia Livieri (London School of Economics), *"When large trades are not news: Liquidity tail risk and price discovery"*, arXiv preprint `arXiv:2607.01198v1 [q-fin.TR]`, submitted July 2, 2026. Full text: [https://arxiv.org/html/2607.01198v1](https://arxiv.org/html/2607.01198v1).
- **Primary Categories:** Trading and Market Microstructure (`q-fin.TR`), General Finance (`q-fin.GN`), Statistical Finance (`q-fin.ST`), Optimization and Control (`math.OC`).
- **Theoretical & Empirical Context:** Sequential competitive Limit Order Book (LOB) equilibrium with asymmetric information, generalizing classical Gaussian microstructure models (Biais, Foucault, Salanié, 2023; Kyle, 1985; Glosten, 1994) to heavy-tailed uninformed liquidity regimes ($Z_t \sim \text{Student-}t$).

## Economic mechanism

### Source-reported

In standard microstructure models with Gaussian noise traders, large order imbalances are exponentially unlikely to be liquidity-driven and are therefore immediately interpreted by liquidity providers as toxic private information, producing steep linear or near-linear price impact.

Çetin, Lin, and Livieri (2026) show that when uninformed order flow $Z_t$ possesses heavy tails (modeled via a Student-$t$ distribution with $\nu > 2$ degrees of freedom, representing random latent liquidity variance and rare liquidity shocks), the economics of price discovery and limit order pricing change fundamentally:
1. **Liquidity Tail Ambiguity:** Because extreme uninformed orders occur at polynomial frequency ($\sim |z|^{-(1+\nu)}$), large aggregate order imbalances $Y_t = X_t + Z_t$ remain plausibly non-informational.
2. **Rightward Shift of Crossover Depth:** The "crossover depth"—the threshold order size beyond which an observed trade is more likely information-driven than liquidity-driven—shifts deep into the order book as $\nu$ decreases (heavier tails).
3. **Flatter and More Concave Price Impact:** Liquidity suppliers do not aggressively penalize large trades at moderate depths. Marginal cost schedules $F(x, t, Y^{t-1})$ and price schedules $h(y, t, Y^{t-1})$ become significantly flatter and more concave in the pre-asymptotic large-order region.
4. **Slowed Bayesian Price Discovery:** Liquidity suppliers update posterior beliefs over asset fundamental value $V$ using Student-$t$ likelihoods. Extreme order flow surprises have lower marginal diagnostic weight, slowing Bayesian learning and extending the persistence of bid-ask spreads and adverse selection premia across consecutive trading rounds.
5. **Breakdown of Gaussian Monotonicity & Fixed-Point Existence:** Under polynomial tails, remote liquidity states remain pricing-relevant at polynomial order, causing standard Gaussian monotonicity preservation and compactness arguments to fail (Example 3.1). The authors construct an explicit equilibrium fixed point on a tail-controlled compact class using Schauder's fixed-point theorem (Theorem 3.1) and prove posterior consistency (Theorem 4.1).
6. **Regular Variation Tail Asymptotics (Theorem 5.1):** At extreme depths ($x \to \infty$), the marginal cost schedule satisfies regular variation:
   $$M - F(x) \sim c \cdot x^{\rho^+}$$
   where the tail exponent $\rho^+ \in (-1, 0)$ is explicitly determined by the liquidity tail index $\nu$, the number of competing informed traders $N_t$, and posterior beliefs $\mathbb{P}_t$.

### Research interpretation

This paper provides a rigorous microstructural justification for state-dependent execution algorithms, optimal order slicing, and adverse selection filters:
1. **Tail-Aware Execution Slicing:** When liquidity tail risk is high (low $\nu$, e.g. during market-wide deleveraging, fund rebalancing, or liquidation cascades), large meta-orders experience much lower immediate adverse selection impact than Gaussian models predict, allowing execution algorithms to safely submit larger child orders without triggering aggressive market-maker widening.
2. **Dynamic Adverse Selection Decay:** Alpha signals based on order flow imbalance (OFI) decay significantly more slowly in heavy-tailed markets because market makers take longer to incorporate the private signal into prices.

## Signal

### 1. State Space & Priors
In trading period $t \in \{1, \dots, T\}$:
- $V \in [m, M]$: True fundamental value.
- $\mathbb{P}_t(V \in dv \mid Y^{t-1}) = \mathfrak{p}_{t,V}(v) dv$: Liquidity suppliers' posterior belief after observing past order history $Y^{t-1} = (Y_1, \dots, Y_{t-1})$.
- $N_t \ge 1$: Number of risk-neutral informed traders.
- $Z_t \sim \text{Student-}t(\nu, 0, \sigma)$: Uninformed noise trader flow with tail parameter $\nu > 2$ and scale $\sigma > 0$.

### 2. Bayesian Belief Updating
Upon observing aggregate period trade flow $Y_{t-1} = X_{t-1}^* + Z_{t-1}$:
$$\mathfrak{p}_{t,V}(v \mid Y^{t-1}) \propto \mathfrak{p}_{t-1,V}(v \mid Y^{t-2}) \cdot \mathfrak{q}_\nu\left(Y_{t-1} - F^{-1}(v, t-1, Y^{t-2}); 0, \sigma\right)$$
where $\mathfrak{q}_\nu(z; 0, \sigma) = \frac{\Gamma((\nu+1)/2)}{\sqrt{\pi \nu} \sigma \Gamma(\nu/2)} \left(1 + \frac{z^2}{\nu \sigma^2}\right)^{-\frac{\nu+1}{2}}$.

### 3. Equilibrium Marginal Cost Schedule $F(x)$
The equilibrium marginal cost $F(x, t, Y^{t-1})$ solves the fixed point $\mathcal{T}_{t,\nu} F = F$:
$$F(x) = \mathbb{E}_t\left[ \frac{\int_m^M v \cdot \Pi_t^+(v; x, F) \, \mathfrak{p}_{t,V}(v) dv}{\int_m^M \Pi_t^+(v; x, F) \, \mathfrak{p}_{t,V}(v) dv} \right]$$
where $\Pi_t^+(v; x, F) = \int_0^\infty \mathfrak{q}_\nu(u + x - F^{-1}(v); 0, \sigma) du$.

### 4. Strategic Informed Demand
For informed valuation $v_0$:
$$X_t^*(v_0) = F^{-1}(v_0, t, Y^{t-1})$$
Individual insider order size: $x_{i,t}^* = \frac{1}{N_t} X_t^*(v_0)$.

### 5. Crossover Depth Signal $\Xi_t^*(\nu)$
Define the crossover depth $\Xi_t^*$ as the order size $y > 0$ where the conditional likelihood of informed trading exceeds uninformed liquidity trading:
$$\Xi_t^*(\nu) = \inf \left\{ y > 0 : \mathbb{P}_t(\text{informed} \mid Y_t \ge y) > \frac{1}{2} \right\}$$
- **Alpha Rule:** If $|Y_t| < \Xi_t^*(\nu)$, classify order flow as *liquidity noise* (contrarian / mean-reverting fade). If $|Y_t| \ge \Xi_t^*(\nu)$, classify order flow as *informed directional flow* (momentum / trend follow).

## Required data

- **Universe:** Liquid crypto perpetuals (e.g. BTC-USDT, ETH-USDT) or equity limit order books.
- **Timeframe:** Discrete execution intervals (e.g. 1-minute, 5-minute, or 15-minute aggregated flow windows).
- **Fields:**
  - `timestamp`: Bar timestamp.
  - `net_order_flow` ($Y_t$): Net taker buy volume minus taker sell volume.
  - `L2_bids_asks`: Standing book depth profiles $h(y)$ at multiple lot levels.
  - `spread`: Best bid-ask spread $S_t = h(0^+) - h(0^-)$.
  - `estimated_nu` ($\hat{\nu}_t$): Rolling tail index of order flow volume.
  - `estimated_sigma` ($\hat{\sigma}_t$): Rolling scale parameter.

## Execution assumptions

- **Execution Timing:** Noise traders submit background flow $Z_t$ first; strategic informed traders submit orders $X_t^*$ within the trading window without observing contemporaneous $Z_t$.
- **LOB Pricing:** Liquidity suppliers post competitive schedules $h(y)$ earning zero expected profit conditional on execution.
- **Order Routing:** Passive limit orders execute against aggregate taker flow; market orders incur integrated cost $\int_0^x h(u) du$.

## Evidence

### Source-reported

- **Flatter Price Impact at Depth:** Numerical solutions (Section 6) confirm that lower degrees of freedom $\nu$ (e.g. $\nu = 2.5$ vs $\nu = 10$ vs Gaussian $\nu = \infty$) produce significantly flatter marginal price schedules $h(y)$ across mid-to-high order depths.
- **Crossover Depth Expansion:** As $\nu$ decreases from $\infty$ to $3$, the crossover depth $\Xi^*$ expands by more than $2.5\times$, confirming that large orders in heavy-tailed regimes remain predominantly uninformed.
- **Slowed Posterior Learning:** In multi-period simulations ($T=50$), the posterior variance of fundamental estimates decays at rate $O(1/t)$ under Gaussian noise, but slows markedly under Student-$t$ noise ($\nu=3$), resulting in persistent adverse selection spreads over longer horizons.
- **Informed Competition Attenuation:** Increasing informed trader count $N_t$ from $1$ to $5$ compresses spreads by $\approx 45\%$ and lowers marginal impact, but preserves the power-law tail exponent $\rho^+$.

### Independently reproduced

- Not independently reproduced.

### Negative evidence

- None identified in the reviewed sources; absence is not evidence of no negative result.
- Mathematical limitation: Monotonicity of the marginal cost operator fails in general for arbitrary bounded Lipschitz functions under Student-$t$ noise (Example 3.1); fixed points are proven conditionally on selected monotone branches.

## Falsification plan

1. **Impact Concavity vs Tail Index Test:** Estimate rolling tail index $\hat{\nu}$ of net order flow across 30 crypto perpetuals. Regress empirical price impact slope at depth $y = 5\sigma$ on $\hat{\nu}$.
   - *Falsification Condition:* If price impact at depth becomes steeper (more convex) during heavy-tailed regimes (low $\hat{\nu}$), the core theoretical prediction is falsified.
2. **Crossover Depth Predictive Power:** Classify trades exceeding $\Xi_t^*(\hat{\nu})$ as directional signals and evaluate 1-hour forward return $R_{t+1\text{h}}$.
   - *Falsification Condition:* If fixed-threshold order flow rules outperform tail-adaptive crossover rules $\Xi_t^*(\hat{\nu})$ in out-of-sample risk-adjusted returns (Sharpe ratio difference $t$-stat $< -2.0$), the utility of the tail-adaptive threshold is refuted.
3. **Adverse Selection Half-Life Decay:** Measure the empirical decay rate of bid-ask spread expansion following large order imbalances ($|Y_t| > 3\sigma$) in low-$\nu$ vs high-$\nu$ regimes.
   - *Falsification Condition:* If spreads normalize faster after large shocks in low-$\nu$ regimes than in high-$\nu$ regimes, the Bayesian learning slowdown prediction is falsified.

## Crypto portability

- **Interpretation:** Direct for Crypto Microstructure & Perpetual LOBs.
- **Portability Advantages:**
  - *Empirical Fat Tails:* Crypto order flow volume exhibits pronounced power-law tails ($\nu \approx 2.0 - 2.8$) due to retail herding, algorithmic liquidations, and whale reallocations.
  - *High-Frequency Slicing:* Crypto trading desks executing multi-million dollar perp orders can dynamically adapt their execution slicing based on real-time estimates of $\hat{\nu}_t$.
  - *24/7 Continuous Learning:* Multi-period Bayesian updating can run continuously across 24/7 sessions without market close disruptions.
- **Crypto Microstructure Frictions:** Latency arbitrage and cross-venue MEV taker flow can inject toxic flow that violates the pure Student-$t$ noise assumption during liquidation cascades.

## Limitations

- **Bounded Support Assumption:** Analytical fixed-point existence is proved under bounded support $V \in [m, M]$ (unbounded cases verified numerically).
- **Exogenous Noise Tail Index:** The tail index $\nu$ is treated as an exogenous structural parameter rather than an endogenously determined equilibrium outcome.
- **Myopic Insiders:** Informed traders maximize single-period profit rather than solving a fully dynamic intertemporal control problem with endogenous order splitting.

## Implementation status

- `not-implemented`: Research capture only. No production implementation has been executed in the research repository.

## Adoption boundary

- Research-only. Not approved for implementation, paper trading, testnet, or live deployment.

## Related Wiki records

- `[[quant/crypto-volume-synchronized-probability-of-toxicity-vpin-microstructure-2026-08-31]]`
- `[[quant/passive-market-impact-optimal-execution-mlofi-2026-09-02]]`
- `[[quant/crypto-perpetual-lob-explainable-catboost-gmadl-microstructure-2026-09-01]]`

## Sources

- Umut Çetin, Mingwei Lin, and Giulia Livieri, *"When large trades are not news: Liquidity tail risk and price discovery"*, arXiv preprint `arXiv:2607.01198v1 [q-fin.TR]`, July 2, 2026. DOI: `10.48550/arXiv.2607.01198`. URL: [https://arxiv.org/abs/2607.01198](https://arxiv.org/abs/2607.01198).
- Bruno Biais, Thierry Foucault, and François Salanié, *"Equilibrium in a limit order market with adverse selection"*, Theoretical Economics, 2023.
- Albert S. Kyle, *"Continuous Auctions and Informed Trader"*, Econometrica 53(6), 1315–1335, 1985.
- Lawrence R. Glosten, *"Is the electronic open limit order book inevitable?"*, Journal of Finance 49(4), 1127–1161, 1994.
