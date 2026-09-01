---
schema: strategy-research-record-v1
title: "Axiomatic Unified Inventory Market Making: Forced Equivalence of Avellaneda-Stoikov and Cartea-Jaimungal, Additive Spread Decomposition, and Phase Transitions"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-making
  - limit-order-book
  - avellaneda-stoikov
  - cartea-jaimungal
  - inventory-control
  - axiomatic-foundations
  - spread-decomposition
status: research-only
confidence: high
source_as_of: 2026-06-08
sources:
  - "Frank M. V. Feys, 'Avellaneda-Stoikov and Cartea-Jaimungal as One Framework: A Forced Uniqueness Theorem for Inventory Market Making', arXiv:2606.01477v3 [q-fin.MF], revised June 2026. DOI: 10.48550/arXiv.2606.01477. https://arxiv.org/abs/2606.01477"
  - "Frank M. V. Feys, 'Axiomatic Market Making', arXiv:2606.09454v1 [q-fin.TR], June 8, 2026. DOI: 10.48550/arXiv.2606.09454. https://arxiv.org/abs/2606.09454"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Axiomatic Unified Inventory Market Making: Forced Equivalence of Avellaneda-Stoikov and Cartea-Jaimungal, Additive Spread Decomposition, and Phase Transitions

## Provenance

- **Primary Sources:**
  1. Frank M. V. Feys (University of Oxford / Oxford-Man Institute of Quantitative Finance), *"Avellaneda-Stoikov and Cartea-Jaimungal as One Framework: A Forced Uniqueness Theorem for Inventory Market Making"*, arXiv preprint `arXiv:2606.01477v3 [q-fin.MF]`, first submitted May 2026, revised June 2026. DOI: [10.48550/arXiv.2606.01477](https://doi.org/10.48550/arXiv.2606.01477). Full text: [https://arxiv.org/abs/2606.01477](https://arxiv.org/abs/2606.01477).
  2. Frank M. V. Feys, *"Axiomatic Market Making"*, arXiv preprint `arXiv:2606.09454v1 [q-fin.TR]`, submitted June 8, 2026. DOI: [10.48550/arXiv.2606.09454](https://doi.org/10.48550/arXiv.2606.09454). Full text: [https://arxiv.org/abs/2606.09454](https://arxiv.org/abs/2606.09454).
- **Primary Categories:** Mathematical Finance (`q-fin.MF`), Trading and Market Microstructure (`q-fin.TR`).
- **Context:** Theoretical breakthrough in mathematical market making. For two decades, quantitative market makers have treated the expected-utility framework of Avellaneda & Stoikov (2008) and the running-inventory-penalty framework of Cartea & Jaimungal (2014) as two distinct, competing optimization formulations. Feys establishes an axiomatic forced-uniqueness theorem proving that both frameworks are exact mathematical manifestations of a single underlying preference functional, derives a unique 3-parameter quoting rule, and uncovers a sharp phase transition between active quoting and book freeze.

## Economic mechanism

### Source-reported

In continuous double auction limit order book markets:
1. **The Axiomatic Foundation:** Rather than postulating an ad-hoc utility function or penalty integral, Feys establishes eight foundational behavioral axioms (Cash-Additivity, Normalization, Concavity, Monotonicity, Scale-Invariance, Strong Dynamic Consistency, Law-Invariance, and Information Neutrality).
2. **Forced Uniqueness and Equivalence Theorem:** Under these axioms, the objective functional over inventory trajectories $q_{[0, T]}$ is uniquely forced to a canonical form. The Cartea-Jaimungal (CJ) running penalty $\phi \int_0^T q_t^2 dt$ is proven to be the exact second-order Taylor expansion of the Avellaneda-Stoikov (AS) CARA utility formulation $-\mathbb{E}[e^{-\gamma (X_T + q_T S_T)}]$, establishing the strict parameter equivalence:
   $$\phi = \frac{1}{2} \gamma \sigma^2$$
   and terminal penalty parameter $\alpha = \frac{1}{2} L''(0)$ where $L(\cdot)$ is the terminal liquidation loss function.
3. **Additive Spread Decomposition:** The unique quoting rule maps market state $(q, \mu, \sigma^2, \lambda, \alpha)$ to bid and ask quotes with exact separation:
   - Mid-quote shift is strictly linear in inventory: $\delta_{\mathrm{mid}}(q) = -\frac{1}{2} \gamma \sigma^2 (2q \pm 1) \Delta t$.
   - Quoted spread decomposes additively into an inventory risk premium and an adverse selection premium:
     $$S(q) = \delta^a(q) + \delta^b(q) = S_{\mathrm{inventory}}(q) + S_{\mathrm{adverse}}$$
     where $S_{\mathrm{inventory}}(q) = \gamma \sigma^2 (2T - 2t)$ and $S_{\mathrm{adverse}} = \frac{2}{\kappa} \ln\left(1 + \frac{\kappa}{\gamma}\right)$.
4. **Sharp Phase Transition to Market Freeze:** When inventory exceeds a critical structural threshold $q_{\mathrm{crit}} = \frac{\kappa \Delta S_{\mathrm{tick}}}{2 \gamma \sigma^2 \Delta t}$, the optimal bid or ask quote jumps discontinuously outside the active queue depth, inducing a localized liquidity freeze.

### Research interpretation

The falsifiable thesis is that **unifying AS and CJ quoting dynamics under the structural identity $\phi = \frac{1}{2}\gamma\sigma^2$ eliminates parameter calibration misalignment and prevents inventory-skew over-widening**:
- Market makers calibrating $\phi$ and $\gamma$ independently in live trading introduce unhedgeable basis risk between terminal risk and intraday inventory control.
- Enforcing the axiomatic parameter coupling and additive spread decomposition stabilizes fill probability estimation and reduces inventory drawdown variance across volatility spikes.

## Signal

### 1. Canonical 3-Parameter Quoting State

At time $t \in [0, T]$ with inventory $q_t \in [-Q_{\max}, Q_{\max}]$:
- **Observed Market Variables:** Mid-price $S_t$, instantaneous volatility $\sigma_t$, order book arrival intensity $\lambda_t(\delta) = A e^{-\kappa \delta}$, and informed order flow fraction $\alpha_{\mathrm{inf}} \in [0, 1)$.
- **Coupled Risk Parameter:** Risk aversion coefficient $\gamma > 0$, defining running penalty rate $\phi_t = \frac{1}{2} \gamma \sigma_t^2$.

### 2. Quoting Formulas

The optimal bid distance $\delta_t^b$ and ask distance $\delta_t^a$ relative to mid-price $S_t$ ($p_t^b = S_t - \delta_t^b$, $p_t^a = S_t + \delta_t^a$) are computed as:
$$\delta_t^a(q_t) = \frac{1}{\kappa} \ln\left(1 + \frac{\kappa}{\gamma}\right) + \frac{1}{2} \gamma \sigma_t^2 (T - t) (2 q_t + 1)$$
$$\delta_t^b(q_t) = \frac{1}{\kappa} \ln\left(1 + \frac{\kappa}{\gamma}\right) - \frac{1}{2} \gamma \sigma_t^2 (T - t) (2 q_t - 1)$$

### 3. Inventory Asymmetry and Reservation Price

- **Reservation Price:**
  $$R_t(q_t) = S_t - q_t \gamma \sigma_t^2 (T - t)$$
- **Effective Half-Spread:**
  $$\bar{\delta}_t = \frac{1}{2} (\delta_t^a + \delta_t^b) = \frac{1}{\kappa} \ln\left(1 + \frac{\kappa}{\gamma}\right) + \frac{1}{2} \gamma \sigma_t^2 (T - t)$$
- **Phase Transition Threshold Check:** If $|q_t| \ge q_{\mathrm{crit}} = \frac{1}{\gamma \sigma_t^2 (T - t) \kappa}$, deactivate passive quoting on the loaded side and execute an active hedge via market order / taker liquidity.

## Required data

- **Instruments:** Spot and perpetual crypto markets (BTC/USDT, ETH/USDT, SOL/USDT) and traditional index futures (ES, NQ).
- **L2 Order Book Data:**
  - Top-of-book and depth snapshots at $\le 10\text{ms}$ resolution.
  - Fill events and trade tape to calibrate arrival intensity parameters $(A, \kappa)$ via maximum likelihood estimation:
    $$\hat{\kappa} = \arg\max_\kappa \sum_{i=1}^N \left( \ln(A) - \kappa \delta_i - \int_0^T A e^{-\kappa \delta_t} dt \right)$$
- **High-Frequency Realized Volatility:** 5-minute rolling realized variance $\sigma_t^2 = \sum_{k} r_k^2$ sampled from tick returns.

## Execution assumptions

- **Passive Maker Quoting:** Post-only limit orders submitted at price ticks $p^b, p^a$.
- **Cancellation & Amend Latency:** Order replacement latency $\tau_{\mathrm{lat}} \in [1\text{ms}, 10\text{ms}]$.
- **Queue Priority:** Price-time priority in Central Limit Order Book (CLOB).
- **Maker Fees / Rebates:** Incorporates exchange tier maker fee/rebate $c_{\mathrm{maker}}$ into effective spread bounds.

## Evidence

### Source-reported

All mathematical proofs, uniqueness theorems, and structural corollaries reported below are from Frank M. V. Feys (arXiv:2606.01477v3 and arXiv:2606.09454v1, June 2026):
1. **Forced Uniqueness Theorem:**
   - Under the eight axiomatic postulates, the objective functional is uniquely determined up to positive affine transformation, proving that the AS exponential utility optimization and CJ running penalty minimization produce identical optimal controls to second order in $\Delta t$.
   - Confirms that independent tuning of $\phi$ and $\gamma$ in historical implementations created artificial parameter redundancy.
2. **Decoupled Three-Parameter Identification:**
   - Proves that the three structural parameters $(\gamma, \sigma^2, \kappa)$ are uniquely identified from three distinct observable moments of the limit order book quotes:
     1. Inventory slope $\partial \delta_{\mathrm{mid}} / \partial q \to \gamma \sigma^2$;
     2. Baseline spread at zero inventory $S(0) \to \frac{2}{\kappa} \ln(1 + \kappa/\gamma)$;
     3. Fill probability decay rate $\partial \ln \lambda / \partial \delta \to \kappa$.
3. **Analytical Phase Transition:**
   - Demonstrates the existence of a sharp phase transition boundary where optimal quoting breaks down into pure one-sided liquidation, explaining empirical "quote disappearing" phenomena during volatility bursts.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Non-Exponential Arrival Intensity:** If empirical order arrivals follow a power law $\lambda(\delta) \propto \delta^{-\alpha}$ rather than exponential decay $A e^{-\kappa \delta}$, the closed-form additive spread separation requires numerical approximation.
- **Latency Arbitrage / Adverse Toxic Fills:** In fragmented markets where informed toxic flow snipes stale maker quotes across venues within $< 2\text{ms}$, the static intensity parameter $\kappa$ underestimates toxic fill probability, causing inventory accumulation beyond $q_{\mathrm{crit}}$.

## Falsification plan

1. **Parameter Coupling Equivalence Test:** In an LOB simulation backtest with calibrated BTC-USDT order flow, compare quoting performance of (a) axiomatic coupled policy ($\phi = \frac{1}{2}\gamma\sigma^2$), versus (b) uncoupled two-parameter grid search $(\phi, \gamma)$. Falsification threshold: If the coupled policy exhibits higher inventory variance or lower Sharpe ratio ($p < 0.05$) than the uncoupled model across 10,000 simulated paths, reject the axiomatic sufficiency theorem.
2. **Spread Decomposition Linearity Test:** Regress empirical quoted half-spread differences against inventory $q_t$. Falsification threshold: If the quadratic term in $\delta_t^a(q) - \delta_t^b(q) = \beta_1 q + \beta_2 q^2$ is statistically significant ($p < 0.01$ with $|\beta_2 / \beta_1| > 0.05$), reject the linear inventory mid-quote shift hypothesis.
3. **Phase-Transition Boundary Validation:** Test inventory drawdown behavior as $|q_t| \to q_{\mathrm{crit}}$. Falsification threshold: If fill rates do not exhibit a discontinuous drop $> 70\%$ within $\pm 5\%$ of $q_{\mathrm{crit}}$, falsify the sharp phase transition prediction.

## Crypto portability

- **Adapted / Direct for CLOBs**:
- The framework applies directly to crypto central limit order book exchanges (Binance Futures, OKX, Bybit, Coinbase, Hyperliquid L1).
- **Crypto-Specific Dynamics:**
  - **Perpetual Funding Rate Drift:** For perpetual swaps, the fair price drift $\mu_t$ must be augmented by the funding rate cost: $\tilde{\mu}_t = \mu_t - r_{\mathrm{funding}} / 8\text{h}$.
  - **Extreme Volatility Spikes:** High kurtosis in crypto returns requires continuous dynamic updating of $\sigma_t^2$ using intraday tick-level realized quarticity to avoid inventory breach of $q_{\mathrm{crit}}$.

## Limitations

- **Not independently reproduced:** Theoretical proofs from Feys (arXiv:2606.01477v3 / arXiv:2606.09454v1, 2026).
- **Assumes Continuous State Space:** Real exchange quotes are quantized to discrete tick sizes ($\Delta p_{\mathrm{tick}}$), requiring integer price rounding.
- **Zero Cross-Asset Spillover:** Models single-asset inventory without multi-asset cross-impact correlation matrix.

## Implementation status

- `not-implemented`
- Research capture only. No market-making quoting engine implemented in PyBroker, Nautilus, or live trading systems.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Research capture does not authorize live quoting or capital allocation on order book venues.

## Related Wiki records

- `[[quant/hawkes-driven-otc-market-making-volterra-riccati-2026-09-01]]`
- `[[quant/funding-aware-market-making-perpetual-dex-2026-08-31]]`
- `[[quant/market-making-latent-fad-stochastic-control-hjb-2026-09-02]]`
- `[[quant/market-making-online-lob-action-dependent-feedback-2026-09-02]]`

## Sources

1. Frank M. V. Feys, *"Avellaneda-Stoikov and Cartea-Jaimungal as One Framework: A Forced Uniqueness Theorem for Inventory Market Making"*, arXiv preprint `arXiv:2606.01477v3 [q-fin.MF]`, first submitted May 2026, revised June 2026. DOI: [10.48550/arXiv.2606.01477](https://doi.org/10.48550/arXiv.2606.01477). Stable URL: https://arxiv.org/abs/2606.01477.
2. Frank M. V. Feys, *"Axiomatic Market Making"*, arXiv preprint `arXiv:2606.09454v1 [q-fin.TR]`, submitted June 8, 2026. DOI: [10.48550/arXiv.2606.09454](https://doi.org/10.48550/arXiv.2606.09454). Stable URL: https://arxiv.org/abs/2606.09454.
