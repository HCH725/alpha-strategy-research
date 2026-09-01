---
schema: strategy-research-record-v1
title: "Online Market Making with Action-Dependent Limit Order Book Feedback: Informative Silence, Elimination Learning, and Regret-Bounded Spread Adaptation"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-making
  - limit-order-book
  - online-learning
  - action-dependent-feedback
  - regret-bounds
  - mean-reversion
  - adverse-selection
status: research-only
confidence: high
source_as_of: 2026-05-27
sources:
  - "Davide Maran and Marcello Restelli, 'Online Market Making and the Value of Observing the Order Book', arXiv:2605.19584v1 [cs.LG, q-fin.TR], May 27, 2026; 39th Annual Conference on Learning Theory (COLT 2026). DOI: 10.48550/arXiv.2605.19584. https://arxiv.org/abs/2605.19584"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Online Market Making with Action-Dependent Limit Order Book Feedback: Informative Silence, Elimination Learning, and Regret-Bounded Spread Adaptation

## Provenance

- **Primary Source:** Davide Maran (Politecnico di Milano) and Marcello Restelli (Politecnico di Milano), *"Online Market Making and the Value of Observing the Order Book"*, arXiv preprint `arXiv:2605.19584v1 [cs.LG, q-fin.TR]`, submitted May 27, 2026; accepted at the 39th Annual Conference on Learning Theory (COLT 2026). DOI: [10.48550/arXiv.2605.19584](https://doi.org/10.48550/arXiv.2605.19584). Full text: [https://arxiv.org/abs/2605.19584](https://arxiv.org/abs/2605.19584).
- **Primary Categories:** Machine Learning (`cs.LG`), Trading and Market Microstructure (`q-fin.TR`).
- **Context:** Mathematical resolution of the online learning market-making problem under action-dependent feedback. In classical multi-armed bandit / partial monitoring formulations, market makers face "censored feedback" (learning client valuations only when a trade occurs). Maran and Restelli formalize the structural information contained in resting Limit Order Book (LOB) quotes when *no* trade occurs ("informative silence").

## Economic mechanism

### Source-reported

In electronic limit order markets, a market maker sequentially posts bid prices $p_{b,t}$ and ask prices $p_{a,t}$ around an underlying fair price $S_t$:
1. **The Censoring Fallacy in Standard Bandits:** Traditional online learning models treat unexecuted quotes as uninformative bandit arms (zero feedback). However, in a real LOB, if an ask quote $p_{a,t}$ is not lifted by an incoming buyer with private valuation $v_t$, the market maker directly observes that $v_t < p_{a,t}$. If other resting orders in the book execute or remain untouched, the LOB provides explicit upper and lower bounds on market demand.
2. **Action-Dependent Information Structure:**
   - **Trade Occurs ($Y_t = 1$):** Transaction is executed at quoted price $p_t$. The maker earns the spread but client surplus $v_t - p_t$ remains latent.
   - **No Trade Occurs ($Y_t = 0$):** Transaction is not executed, but the unexecuted order book state confirms $v_t < p_t$, revealing a clean one-sided inequality constraint on the cumulative distribution function $F(v)$.
3. **Fundamental Learnability Transformation:** This asymmetric observation feedback converts an intractable partial monitoring problem with $O(T^{2/3})$ lower bounds into an active elimination problem achieving optimal $O(\sqrt{T})$ regret under stochastic i.i.d. valuations and autoregressive mean-reverting price dynamics.
4. **Adversarial Robustness:** Under non-stationary / adversarial oblivious price paths, an explore-then-perturb randomized quoting policy achieves $O(T^{2/3})$ expected regret, guaranteeing finite-sample safety against predatory quote sniping.

### Research interpretation

The falsifiable thesis is that **unfilled quote observations contain non-linear filtering value** that accelerates spread convergence:
- Market-making algorithms that update valuation beliefs only upon trade executions over-estimate adverse selection during low-volume regimes and widen spreads excessively.
- Conditioning spread updates on the duration and depth of unfilled resting quotes allows the market maker to narrow spreads faster toward optimal half-spread $\delta^* = \arg\max_\delta \delta (1 - F(\delta))$ without suffering elevated inventory toxicity.

## Signal

### 1. State Space and Action-Dependent Observation

- At each round $t = 1, \dots, T$:
  - Mid-price follows state $S_t$ (either i.i.d. noise or mean-reverting AR(1) process $S_{t+1} = \rho S_t + \epsilon_t$ with $|\rho| < 1$).
  - Market maker selects half-spread $\delta_t \in \mathcal{K} \subset [0, \bar{\delta}]$, quoting bid $p_{b,t} = S_t - \delta_t$ and ask $p_{a,t} = S_t + \delta_t$.
  - Incoming buyer valuation is $V_t = S_t + \xi_t$, where $\xi_t \sim F_\xi$ is zero-mean buyer excess valuation.
- **Feedback Protocol:**
  - If $\xi_t \ge \delta_t$: Trade occurs ($Y_t = 1$). Reward $R_t = \delta_t - \text{AdverseSelection}_t$.
  - If $\xi_t < \delta_t$: No trade occurs ($Y_t = 0$). Feedback reveals upper bound $\xi_t \in [-\infty, \delta_t)$.

### 2. Elimination-Based Spread Optimization (Stochastic Setting)

- Maintain active candidate spread set $\mathcal{A}_k \subseteq \mathcal{K}$ in epoch $k$.
- Compute empirical survival estimate $\hat{S}_k(\delta) = \frac{1}{N_k} \sum_{\tau \in \mathcal{E}_k} \mathbf{1}_{\{\xi_\tau \ge \delta\}}$ using both trade events and order-book bounding feedback.
- For each candidate $\delta \in \mathcal{A}_k$, compute empirical expected revenue $\hat{\mu}_k(\delta) = \delta \cdot \hat{S}_k(\delta)$ and confidence radius $\beta_k(\delta) = \sqrt{\frac{2 \ln(2 |\mathcal{K}| / \alpha)}{N_k}}$.
- **Elimination Step:** Discard any sub-optimal spread candidate satisfying:
  $$\max_{\delta' \in \mathcal{A}_k} (\hat{\mu}_k(\delta') - \beta_k(\delta')) > \hat{\mu}_k(\delta) + \beta_k(\delta)$$
- Update active set $\mathcal{A}_{k+1} \leftarrow \mathcal{A}_k \setminus \{\text{discarded candidates}\}$ and advance to epoch $k+1$.

### 3. Explore-Then-Perturb Quoting Policy (Adversarial Setting)

- Partition time horizon $T$ into exploration phase of length $T_0 = \lceil T^{2/3} \rceil$ and exploitation phase $T - T_0$.
- In exploration phase, sample spreads uniformly across discrete grid $\mathcal{K}_\epsilon$ of mesh size $\epsilon = T^{-1/3}$.
- In exploitation phase, select empirical best spread with Laplace perturbation noise $\eta_t \sim \text{Lap}(0, \gamma_t)$ where $\gamma_t = O(t^{-1/3})$ to prevent adversarial quote manipulation.

## Required data

- **Instruments:** Spot and perpetual limit order book markets (BTC-USDT, ETH-USDT, high-volume equities / FX).
- **Feeds:**
  - L2/L3 tick-by-tick order book updates (new orders, amendments, cancellations, executions).
  - High-resolution timestamped fill reports with matched trade IDs.
  - Inter-trade arrival duration $\Delta \tau_t$ and book queue position tracking.
- **Sampling Frequency:** Event-driven tick-by-tick state transition updates (microsecond to millisecond precision).

## Execution assumptions

- **Passive Order Posting:** Market maker acts exclusively as a passive liquidity provider (maker-only post orders).
- **Latency Model:** Order submission and cancellation latency $\tau_{\mathrm{lat}} \le 5\text{ms}$; orders are placed at discrete tick price levels.
- **Inventory Penalty:** Running quadratic inventory holding cost $\frac{1}{2} \gamma \sigma^2 q_t^2$ applied to net accumulated position $q_t = \sum_{\tau=1}^t (Y_{\tau}^{\mathrm{buy}} - Y_{\tau}^{\mathrm{sell}})$.

## Evidence

### Source-reported

All theoretical bounds and asymptotic guarantees below are proved by Davide Maran and Marcello Restelli (arXiv:2605.19584v1 / COLT 2026):
1. **Stochastic i.i.d. Valuation Regret:**
   - Under action-dependent LOB feedback, the elimination algorithm achieves high-probability cumulative regret bounded by $O(\sqrt{T \ln(|\mathcal{K}| / \alpha)})$.
   - Eliminates the necessity of Hölder-continuity or smoothness assumptions on the valuation density $f(\xi)$, outperforming standard multi-armed bandit lower bounds ($O(T^{2/3})$).
2. **Mean-Reverting Price Dynamics:**
   - For Ornstein-Uhlenbeck / AR(1) price dynamics with autoregressive coefficient $|\rho| < 1$, the regret bound remains $O(\sqrt{T})$, establishing that price mean-reversion preserves optimal learnability.
3. **Adversarial / Oblivious Price Paths:**
   - In non-stochastic environments with arbitrary bounded price trajectories, the explore-then-perturb algorithm achieves expected regret $O(T^{2/3})$.
4. **Information Value of Silence:**
   - Theoretical proof that observing order book state upon trade absence reduces the minimax regret rate from non-learnable / hard partial monitoring to canonical statistical estimation rates.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Toxic Queue Depletion:** In regimes dominated by low-latency informed flow (e.g., CEX-DEX latency arbitrage or news shocks), non-execution may indicate quote mispricing rather than uninformative valuation bounds, introducing bias into the naive empirical survival estimator $\hat{S}(\delta)$.
- **Zero-Intelligence Order Flow Assumption:** If client arrivals are endogenously correlated with maker spread adjustments (strategic feedback), regret bounds degrade if opponent strategies adapt dynamically.
- **Discrete Tick Constraints:** In large-tick instruments where spread is constrained to 1 tick, the continuous optimization gain collapses to zero.

## Falsification plan

1. **Elimination Speed vs. Bandit Benchmark Test:** In an LOB market simulator with synthetic trader valuations, compare the sample efficiency and regret of the action-dependent elimination algorithm against a standard upper confidence bound (UCB) bandit that updates only on fills. Falsification threshold: If the elimination algorithm does not achieve at least 35% faster parameter convergence and lower cumulative regret ($p < 0.01$), reject the informative silence hypothesis.
2. **Mean-Reverting Stress Test:** Test the algorithm across asset price processes with varying mean-reversion speeds $\rho \in [0.1, 0.99]$. Falsification threshold: If cumulative regret scales faster than $T^{0.55}$ as $\rho \to 0.95$, falsify the mean-reversion invariance theorem.
3. **Latency-Induced Adverse Selection Test:** Inject simulated quote-posting latency $\tau \in [10\text{ms}, 200\text{ms}]$. Falsification threshold: If realized Sharpe ratio drops below 0 when latency exceeds 50ms, confirm that the algorithm requires low-latency execution infrastructure.

## Crypto portability

- **Adapted / Unproven**:
- The mathematical proofs are derived in generic online learning frameworks and calibrated to continuous double auction limit order books.
- **Crypto Application:** Directly applicable to crypto CLOB venues (Binance, OKX, Bybit, Coinbase) and decentralized CLOBs (Hyperliquid, dYdX v4, Drift).
- **Crypto Portability Challenges:**
  - **Asymmetric Toxicity:** Crypto LOBs exhibit extreme adverse selection during liquidation cascades; valuation distribution $F_\xi$ undergoes sudden heavy-tailed regime shifts.
  - **Perpetual Funding Rate Drift:** Quoting must incorporate perpetual funding payments into the effective mid-price drift $\rho$.

## Limitations

- **Not independently reproduced:** Theoretical proofs from Maran and Restelli (2026).
- **Stationary Valuation Distribution within Epochs:** Assumes buyer/seller valuation distribution $F_\xi$ remains stationary across elimination epochs.
- **Independent Bid/Ask Decomposition:** Assumes bid and ask learning dynamics can be decoupled into two independent one-sided online learning problems.

## Implementation status

- `not-implemented`
- Research capture only. No production quoting algorithm implemented in PyBroker, Nautilus, or live market-making engines.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Research capture does not authorize paper, testnet, or live market making.

## Related Wiki records

- `[[quant/funding-aware-market-making-perpetual-dex-2026-08-31]]`
- `[[quant/hawkes-driven-otc-market-making-volterra-riccati-2026-09-01]]`
- `[[quant/crypto-high-frequency-kyles-lambda-price-impact-reversal-2026-08-31]]`
- `[[crypto-noise-perturbed-order-flow-privacy-subsidy-kyle-market-making-2026-09-01]]`

## Sources

1. Davide Maran and Marcello Restelli, *"Online Market Making and the Value of Observing the Order Book"*, arXiv preprint `arXiv:2605.19584v1 [cs.LG, q-fin.TR]`, submitted May 27, 2026; 39th Annual Conference on Learning Theory (COLT 2026). DOI: [10.48550/arXiv.2605.19584](https://doi.org/10.48550/arXiv.2605.19584). Stable URL: https://arxiv.org/abs/2605.19584.
