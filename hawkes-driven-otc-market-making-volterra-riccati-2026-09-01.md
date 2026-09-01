---
schema: strategy-research-record-v1
title: Hawkes-Driven OTC Market Making Volterra-Riccati Approximation
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-making
  - otc
  - rfq
  - hawkes-processes
  - stochastic-optimal-control
  - volterra-riccati
  - market-microstructure
  - order-flow
status: research-only
confidence: high
source_as_of: 2026-08
sources:
  - "Alexander Barzykin, 'Hawkes-Driven OTC Market Making: Volterra-Riccati Approximation', arXiv:2608.02002v2 [q-fin.RM, q-fin.MF], August 2026. DOI: 10.48550/arXiv.2608.02002. https://arxiv.org/abs/2608.02002"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Hawkes-Driven OTC Market Making Volterra-Riccati Approximation

## Provenance

- **Primary Source:** Alexander Barzykin (HSBC / Quantitative Research), "Hawkes-Driven OTC Market Making: Volterra-Riccati Approximation", arXiv:2608.02002v2 [q-fin.RM, q-fin.MF], August 2026. DOI: [10.48550/arXiv.2608.02002](https://doi.org/10.48550/arXiv.2608.02002). Full text: [https://arxiv.org/html/2608.02002v2](https://arxiv.org/html/2608.02002v2).
- **Motivation & Dataset:** Anonymized institutional spot-FX Request-for-Quote (RFQ) arrivals for EURUSD, GBPUSD, and USDJPY over a 3-year historical window (>500,000 qualified events per pair after filtering). Data filtered to the London active window [00:00, 20:00], removing weekends, major holidays, daylight-saving transitions, year-end roll periods, and illiquid roll windows. Filtered to RFQs of at least 0.25M notional and client streams with $\ge 1\%$ historical fill conversion.
- **Empirical Order Flow Characteristics:** After transforming calendar time to deterministic seasonality-adjusted RFQ activity time $\tau^c(t) = \int_0^t \bar{\lambda}^c(\theta(s)) ds$, fitted two-way marked Hawkes models exhibit high branching ratios ($\eta \approx 0.86\text{--}0.90$) and multi-scale memory (exponential mixture half-lives $h_1 = 1\text{ min}$, $h_2 = 10\text{ min}$, $h_3 = 60\text{ min}$).

## Economic mechanism

### Source-reported

Barzykin (2026) models an over-the-counter (OTC) market-making problem where request-for-quote (RFQ) arrivals are exogenous information events driven by general Hawkes processes, while dealer fills are controlled thinnings governed by quoted price offsets:
1. **Request/Response Decomposition:** Observing an incoming RFQ updates the dealer's information state regarding future client flow regardless of whether the dealer wins the trade. Winning the trade converts the RFQ into an inventory jump.
2. **Path-Dependency & Curse of Dimensionality:** For general multi-scale or power-law Hawkes kernels, exact dynamic programming requires tracking the entire order-flow history or forward intensity curve. Exact Markovian lifting becomes high-dimensional for sums of exponentials ($2Kd$ variables for $d$ factors, 2 sides, $K$ sizes) and impossible for power-law long memory.
3. **Volterra-Riccati Hierarchy:** Rather than solving a high-dimensional Hamilton-Jacobi-Bellman (HJB) PDE, the dealer computes continuation values via a backward Riccati ODE driven by the conditional Volterra forecast curve of future RFQ intensity, with a second-order noise-aware covariance correction and a state-feedback update from the post-request resolvent response.
4. **Endogenous Quote Impact:** A directional RFQ burst shifts the conditional forecast curve of future flow. When filtered through the Riccati continuation-value shadow price, this forecast update endogenously generates a persistent quote skew that inherits the power-law tail decay of the RFQ memory kernel, reducing inventory displacement and P&L variance compared to a memoryless Poisson policy.

### Research interpretation

The falsifiable thesis is a **predictive flow-forecast market-making mechanism**:
1. **Information Value of Unfilled Quotes:** In quote-driven and RFQ protocols, trade arrivals are not independent Poisson jumps. An incoming quote request signals an elevated probability of subsequent same-direction requests (e.g., from algorithmic slicing, meta-order execution, or shared macro signals).
2. **Separation of Forecasting and Control:** The dealer does not need a full Markovian state lift to quote optimally. Feeding the conditional mean intensity curve and covariance into a linear-quadratic Riccati continuation system delivers near-optimal quoting offsets with minimal computational overhead.
3. **Defensive Skewing vs. Aggressive Picking-Off:** Memoryless Poisson market makers quote symmetrically based only on current inventory, suffering severe adverse selection during directional bursts. A Volterra-Riccati dealer skews quotes defensively ahead of future anticipated flow, minimizing inventory accumulation before the full burst arrives.

## Signal

### 1. Hawkes Intensity & Volterra Forward Curve

The exogenous RFQ arrival intensity for side $s \in \{b, a\}$ and size bucket $k \in \{1, \dots, K\}$ follows:
$$\lambda_t^{s,k} = \mu^{s,k}(t) + \sum_{s'=b,a} \sum_{k'=1}^K \int_{-\infty}^{t-} \phi_{s,k,s',k'}(t-u) dM_u^{s',k'}$$

At decision time $t$, given history $\mathcal{H}_t$, the conditional future intensity curve $m_t(u) = \mathbb{E}[\lambda_u \mid \mathcal{H}_t]$ for $u \ge t$ satisfies the deterministic Volterra integral equation:
$$m_t(u) = \mu(u) + \int_{-\infty}^t \Phi(u-v) dM_v + \int_t^u \Phi(u-v) m_t(v) dv$$

Upon observing a new RFQ of type $i = (s, k)$, the forward forecast curve jumps by the resolvent response $\rho_i(u)$:
$$m_t^{i,+}(u) = m_t(u) + \rho_i(u), \quad \rho_i(u) = \Phi(u-t) e_i + \int_t^u \Phi(u-v) \rho_i(v) dv$$

### 2. Approximation Hierarchy & Shadow Price

The dealer maximizes expected terminal wealth with inventory penalty $\kappa = \frac{1}{2} \gamma \sigma^2$ and quadratic terminal penalty $\ell(q) = \kappa_T q^2$:
- **Level 1 (Mean Volterra-Riccati):** Replaces future intensity with deterministic curve $m_t$. Uses quadratic value ansatz $v_0(\tau, q; m_t) = -\frac{1}{2} A_0(\tau) q^2 + B_0(\tau) q + C_0(\tau)$, where $(A_0, B_0, C_0)$ solve backward Riccati ODEs.
- **Level 2 (Noise-Aware Covariance Correction):** Adds second-order functional derivative correction for intensity variance $\Sigma_t(u_1, u_2) = \operatorname{Cov}_t(\lambda_{u_1}, \lambda_{u_2})$:
  $$\bar{V}(t, q; m_t, \Sigma_t) = \mathcal{V}_0(t, q; m_t) + \frac{1}{2} \iint \mathcal{K}(t, q; u_1, u_2) \Sigma_t(u_1, u_2) du_1 du_2$$
- **Level 3 (State-Feedback Stochastic Volterra-Riccati):** Evaluates continuation value under the post-request forecast $m_t^{i,+} = m_t + \rho_i$. The linearized state-feedback shadow price for an incoming RFQ of type $i = (s, k)$ (with direction $\epsilon_b = +1, \epsilon_a = -1$) is:
  $$p_i^{\mathrm{SF}}(t, q) = \frac{v_0(t, q + \epsilon_i z_i; m_t) - v_0(t, q; m_t)}{z_i} + \int_t^T \left[ \mathcal{D}_i(t, q + \epsilon_i z_i, u; m_t) - \mathcal{D}_i(t, q, u; m_t) \right] \rho_i(u) du$$
  where $\mathcal{D}$ is the functional sensitivity $\frac{\delta \mathcal{V}_0}{\delta m(u)}$.

### 3. Optimal Quote Offset Execution

Given shadow price $p$, the optimal quote offset $\delta_i^*(p)$ is recovered from the exact Hamiltonian optimizer:
$$\delta_i^*(p) = \arg\max_{\delta \in [\underline{\delta}, \bar{\delta}]} f_k(\delta) (\delta + p)$$
where $f_k(\delta) = (1 + \exp(\kappa_0 (\delta - \delta_0)))^{-1}$ is the client win probability function.

## Required data

- **Instruments:** Institutional spot FX currency pairs (EURUSD, GBPUSD, USDJPY) or OTC crypto bilateral dealer quote streams / request-for-stream pairs (BTC/USDT, ETH/USDT).
- **Order Flow Feeds:** Granular RFQ arrival timestamps, size bucket $k$, quote side $s$ (or inferred latent direction), and client execution/rejection outcomes.
- **Mid-Price & Volatility:** Continuous mid-price $S_t$ from reference liquidity pools/exchanges, along with local volatility parameter $\sigma$.
- **Calibration Inputs:** Hawkes baseline intensities $\mu$, branching matrix $\mathcal{B}$, kernel decay rates $\beta_n$, and win probability curve parameters $(\kappa_0, \delta_0)$.

## Execution assumptions

- **Execution Protocol:** Bilateral RFQ / Request-for-Stream where dealer posts a firm quote offset $\delta$ valid for a short duration; client accepts with probability $f(\delta)$.
- **Thinning Model:** Quotes control conversion probability $f(\delta)$ without mechanically generating client request arrivals.
- **Inventory & Risk Model:** Constant inventory variance rate $\sigma^2$, running risk aversion $\gamma$, and terminal liquidation penalty $\kappa_T q^2$.
- **Latency & Grid:** Discretized time steps $\Delta t \approx 10^{-4}$ to $5 \times 10^{-5}$ days ($1\text{--}8\text{ seconds}$), with continuation horizon $T_{\mathrm{cont}}$ to avoid finite-horizon boundary distortions.

## Evidence

### Source-reported

All figures below are directly reported by Alexander Barzykin (arXiv:2608.02002v2, August 2026):
1. **Empirical Hawkes Branching in Spot FX (HSBC Dataset, 3 Years, >500k Events/Pair):**
   - Fitted branching ratios in seasonality-adjusted activity time: $\eta \approx 0.86\text{--}0.90$ across EURUSD, GBPUSD, and USDJPY.
   - Significant multi-scale memory with non-negligible excitation mass persisting past 60 minutes.
2. **Numerical Validation vs. Exact Lifted 2D HJB Benchmark ($T=1\text{ day}$, $\Delta t=10^{-4}$, 20,000 Monte Carlo Paths):**
   - **Benign Common-Mode Burst:** Mean Volterra-Riccati captures the bulk of the value; exact lifted HJB and state-feedback VR policy exhibit virtually zero paired regret.
   - **Near-Critical Common-Mode Burst ($\eta \to 1$):** Covariance correction reduces regret by accounting for large intensity uncertainty.
   - **Directional One-Sided Burst ($\lambda_t^b = \mu^b + X_t, \lambda_t^a = \mu^a$):** State-feedback Volterra-Riccati policy closely tracks the exact lifted HJB, while the memoryless Poisson policy incurs severe paired regret due to inability to condition on the realized memory state $X_t$.
3. **Power-Law Long-Memory Simulation ($N=8$ Exponential Factors, $\beta_n \in [2, 2500]$, 50-RFQ Burst, 100,000 MC Paths):**
   - Post-burst Volterra quote impact inherits the power-law tail decay exponent $\chi$ of the Hawkes resolvent: $\delta_i^{\mathrm{imp}}(t, q) \sim C_{i,i_0}^{\mathrm{imp}}(q) t^{-\chi} L(t)$.
   - State-feedback VR dealer defensively skews quotes immediately upon observing the burst, substantially reducing average inventory displacement, root-mean-square (RMS) inventory, and P&L standard deviation relative to the Poisson baseline.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Memoryless Poisson Failure:** Standard Avellaneda-Stoikov / Guéant Poisson market-making models suffer large economic regret and severe inventory over-accumulation during directional order-flow bursts because they ignore path-dependent excitation.
- **Pure Mean-Forecast Deficiency:** In directional regimes, a static mean forecast that fails to update post-request shadow prices (Levels 1 & 2 without Level 3 state feedback) leaves unhedged inventory risk compared to full state feedback.
- **Unmodelled Latent Drivers:** If exogenous macro events drive order flow, a pure Hawkes model may overestimate endogenous self-excitation branching ratios if baseline intensity is held constant.

## Falsification plan

1. **Ablation Test on State Feedback:** In a backtest simulation with clustered flow, disable the post-request resolvent update $\rho_i(u)$ (reverting to pure Level 1 mean forecast). If inventory RMS does not increase by at least 15% during directional bursts, falsify the necessity of Level 3 state feedback.
2. **Poisson Baseline Regret Test:** Compare the state-feedback Volterra-Riccati quoting policy against an Avellaneda-Stoikov Poisson baseline across simulated Hawkes order flow. If paired P&L variance reduction is statistically indistinguishable from zero ($p > 0.05$), reject the hypothesis of Volterra-Riccati superiority.
3. **Kernel Mis-specification Perturbation:** Perturb the Hawkes branching matrix $\mathcal{B}$ by $\pm 30\%$ and decay rates $\beta_n$ by $\pm 50\%$. If the policy incurs catastrophic inventory drawdowns exceeding the Poisson baseline, reject robustness to parameter uncertainty.
4. **Latency / Queue Degradation Test:** Introduce a quote-amendment delay $\tau_{\mathrm{delay}} \in [100\text{ms}, 2\text{s}]$. If defensive quote skewing is consistently picked off before execution, invalidate high-frequency applicability.

## Crypto portability

**Adapted / Unproven**:
- The mechanism is empirically demonstrated on institutional spot FX (HSBC) and validated in synthetic Hawkes simulations.
- **Crypto Application:** Directly relevant to institutional crypto OTC liquidity providers (e.g., Wintermute, B2C2, Cumberland, Paradigm RFQ) and decentralized intent/RFQ solvers (e.g., CoW Swap, UniswapX, 1inch Fusion, Hashflow).
- **Crypto-Specific Frictions:**
  - **24/7 Continuous Trading:** Eliminates FX weekend/holiday cutoffs but introduces continuous weekend regime shifts and liquidity drains.
  - **Perpetual Funding Drift:** Crypto inventory held in perpetual contracts incurs funding cost drag, which must be incorporated into the running inventory penalty $\kappa$.
  - **Toxic Flow & MEV:** On-chain RFQ requests frequently originate from MEV searchers and toxic routing algorithms, meaning win probability $f(\delta)$ is heavily state-dependent and asymmetric.

## Limitations

- **Not independently reproduced.**
- **Two-Way vs. One-Way Ambiguity:** Empirical FX RFQ data is primarily two-way; signed directionality must be inferred via latent filtering models.
- **Exogenous Request Assumption:** Assumes client RFQ arrivals are independent of dealer quotes (no feedback from quote competitiveness into client order generation).
- **Static Win Probability:** Assumes win probability $f(\delta)$ depends only on quote offset, ignoring time-varying competitive quoting from rival dealers.

## Implementation status

Not implemented. No PyBroker, NautilusTrader, paper, testnet, or live trading implementation.

## Adoption boundary

Research material only. Does not constitute trading advice, production validation, or authorization for live trading.

## Related Wiki records

- `[[quant/funding-aware-market-making-perpetual-dex-2026-08-31]]`
- `[[quant/prediction-market-optimal-market-making-latent-belief-hjb-2026-09-01]]`
- `[[quant/crypto-perpetual-lob-explainable-catboost-gmadl-microstructure-2026-09-01]]`
- `[[quant/crypto-high-frequency-kyles-lambda-price-impact-reversal-2026-08-31]]`

## Sources

1. Alexander Barzykin, "Hawkes-Driven OTC Market Making: Volterra-Riccati Approximation", arXiv:2608.02002v2 [q-fin.RM, q-fin.MF], August 2026. DOI: [10.48550/arXiv.2608.02002](https://doi.org/10.48550/arXiv.2608.02002). https://arxiv.org/abs/2608.02002.
2. Full article text and figures: https://arxiv.org/html/2608.02002v2.
