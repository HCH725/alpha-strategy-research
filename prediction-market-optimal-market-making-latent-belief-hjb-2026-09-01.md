---
schema: strategy-research-record-v1
title: Prediction Market Optimal Market Making via Latent Belief Diffusion and HJB Stochastic Control
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - prediction-markets
  - polymarket
  - kalshi
  - market-making
  - stochastic-optimal-control
  - hamilton-jacobi-bellman
  - latent-belief-diffusion
  - inventory-risk
  - settlement-risk
  - binary-contracts
status: research-only
confidence: high
source_as_of: 2026-07-20
sources:
  - "Feil, D., & Nendel, M. (2026). Optimal Market Making in Prediction Markets. arXiv preprint arXiv:2607.17991v1 [q-fin.TR / math.OC / q-fin.MF]. https://arxiv.org/abs/2607.17991"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Prediction Market Optimal Market Making via Latent Belief Diffusion and HJB Stochastic Control

## Provenance

- **Primary Source:** Dominik Feil (University of Konstanz) and Max Nendel (University of Waterloo), *"Optimal Market Making in Prediction Markets"*, arXiv preprint `arXiv:2607.17991v1 [q-fin.TR / math.OC / q-fin.MF]`, published July 20, 2026. URL: https://arxiv.org/abs/2607.17991, DOI: https://doi.org/10.48550/arXiv.2607.17991.
- **Related Foundational Literature:**
  - Avellaneda, M., & Stoikov, S. (2008). "High-Frequency Trading in a Limit Order Book." *Quantitative Finance*, 8(3), 217–224.
  - Guéant, O., Tapia, C. A., & Manziadi, Z. (2013). "Dealing with the inventory risk: a solution to the market making problem." *Mathematics and Financial Economics*, 6(4), 259–277.
  - Guéant, O. (2017). "Optimal market making." In *The Financial Mathematics of Market Liquidity* (pp. 107–152). CRC Press.
  - Hanson, R. (2003). "Combinatorial Information Market Design." *Information Systems Frontiers*, 5(1), 107–119.
  - Dalen, A. (2026). "Belief Aggregation in Prediction Markets." Working Paper.
  - Krylov, N. V. (1996). *Lectures on Elliptic and Parabolic Equations in Hölder Spaces*. American Mathematical Society, Graduate Studies in Mathematics, Vol. 12.
- **Context:** Unlike equity or commodity limit order books where prices evolve over an unbounded range $[0, \infty)$, prediction market contracts (e.g. Polymarket, Kalshi) trade binary contingent claims with payoffs $Y \in \{0, 1\}$ at a terminal resolution time $T$. Feil & Nendel (2026) develop the first rigorous continuous-time stochastic control framework tailored specifically to prediction market order books, resolving the dual-risk trade-off between running mark-to-market inventory risk and terminal binary settlement risk.
- **Public-Use Status:** Open-access preprint under arXiv perpetual non-exclusive license.

## Economic mechanism

### Source-reported

In modern prediction markets operating via Central Limit Order Books (CLOBs, such as Polymarket and Kalshi), market prices $p_t \in (0,1)$ represent the market-implied conditional probability of an outcome $Y \in \{0, 1\}$. 

A market maker quoting bid $\pi_t^b$ and ask $\pi_t^a$ faces two distinct, structurally coupled risk components:
1. **Running Mark-to-Market Inventory Risk:** Prior to event resolution $T$, changes in market belief induce fluctuations in the mark-to-market value of accumulated inventory $q_t$. This instantaneous risk is proportional to the price volatility $\varsigma(t, p_t)^2$.
2. **Terminal Settlement Risk:** At contract expiry $T$, remaining inventory $q_T$ settles against the binary realization $Y \sim \text{Bernoulli}(p_T)$. The conditional variance of this terminal payout is $\operatorname{Var}[q_T Y \mid \mathcal{F}_T] = q_T^2 p_T (1 - p_T)$, representing catastrophic liquidation risk if holding unhedged positions into resolution.

The authors model the price dynamics through a non-linear logistic transformation of a latent information belief process $(L_t)_{t \in [0,T]}$:
- Latent belief SDE: $dL_t = \mu(t, L_t) dt + \sigma(t, L_t) dW_t$
- Market price: $p_t = f(L_t) = \frac{1}{1 + e^{-L_t}}$, where $f \in C^2(\mathbb{R}; (0,1))$ and $L_t = \ln\left(\frac{p_t}{1 - p_t}\right)$ (log-odds).
- Martingale condition: For $p_t$ to remain an $\mathbb{F}$-martingale (satisfying no-arbitrage), the drift of the latent belief must strictly satisfy:
  $$\mu(t, x) = -\frac{1}{2} \sigma^2(t, x) \frac{f''(x)}{f'(x)} = -\frac{1}{2} \sigma^2(t, x) (1 - 2 f(x))$$
- Price diffusion coefficient: $\varsigma(t, p) = f'(f^{-1}(p)) \sigma(t, f^{-1}(p)) = p(1-p) \tilde{\sigma}(t, p)$.

The market maker maximizes expected terminal wealth with running and terminal variance penalties:
$$\sup_{\pi \in \mathcal{A}} \mathbb{E}\left[ X_T + q_T Y - \frac{1}{2} \gamma \int_0^T q_t^2 \varsigma(t, p_t)^2 dt - \frac{1}{2} \gamma_T q_T^2 p_T (1 - p_T) \right]$$
where $\gamma > 0$ is running risk aversion and $\gamma_T > 0$ is terminal settlement risk aversion.

### Research interpretation

The alpha hypothesis is **Optimal Inventory- and Settlement-Risk Controlled Liquidity Provision in Binary Limit Order Books**:

1. **Probability-Dependent Structural Quote Skew:**
   In classical models (Avellaneda-Stoikov), quote skew is driven solely by inventory imbalance ($q \neq 0$). In prediction markets, order arrival intensities naturally vanish as prices approach boundaries ($p \to 0$ or $p \to 1$). Consequently, even at flat inventory ($q = 0$), profit-maximizing quotes exhibit an intrinsic structural skew:
   - For $p < 0.5$, bids are placed closer to the mid-price than asks (positive skew).
   - For $p > 0.5$, asks are placed closer to the mid-price than bids (negative skew).
2. **Dual-Horizon Inventory Control Dynamics:**
   - Running risk parameter $\gamma$ governs inventory limits during early trading ($t \ll T$).
   - Terminal parameter $\gamma_T$ dominates as $t \to T$, forcing aggressive quote adjustments to drive terminal inventory $q_T \to 0$ before binary resolution.
3. **Downside Risk Immunization:**
   By solving the reduced 3D Hamilton–Jacobi–Bellman (HJB) equation, a prediction market maker captures bid-ask spreads while drastically cutting tail drawdown / Expected Shortfall compared to myopic (instantaneous profit) market making.

## Signal

The optimal quoting strategy operates as follows:

1. **State Space and Reduced HJB Formulation:**
   - State vector: $(t, p, q) \in [0, T] \times (0, 1) \times \mathcal{Q}$, where inventory $\mathcal{Q} = \{-Q, -Q+\Delta, \dots, Q\}$.
   - Reduced value function $V(t, p, q)$ satisfies the non-linear parabolic partial differential equation:
     $$\partial_t V(t, p, q) + \frac{1}{2} \varsigma(t, p)^2 \partial_{pp}^2 V(t, p, q) - \frac{1}{2} \gamma q^2 \varsigma(t, p)^2 + \mathcal{H}^b(t, p; \Delta_q^+ V) + \mathcal{H}^a(t, p; \Delta_q^- V) = 0$$
     subject to terminal condition:
     $$V(T, p, q) = q p - \frac{1}{2} \gamma_T q^2 p(1 - p)$$
     where $\Delta_q^+ V = \frac{V(t, p, q) - V(t, p, q+\Delta)}{\Delta}$ and $\Delta_q^- V = \frac{V(t, p, q-\Delta) - V(t, p, q)}{\Delta}$.

2. **Hamiltonian Functions and Optimal Quotes:**
   - For bid side ($q < Q$):
     $$\mathcal{H}^b(t, p; z) = \sup_{\pi \in [0, 1]} \Delta \Lambda^b(t, p, \pi) \left( p - \pi - z \right)$$
     Optimal bid quote:
     $$\pi^{b,*}(t, p, q) = (u_{t,p}^b)^{-1}\left( \frac{V(t, p, q) - V(t, p, q+\Delta)}{\Delta} \right)$$
     where $u_{t,p}^b(\pi) = p - \pi - \frac{\Lambda^b(t, p, \pi)}{\partial_\pi \Lambda^b(t, p, \pi)}$.
   - For ask side ($q > -Q$):
     $$\mathcal{H}^a(t, p; z) = \sup_{\pi \in [0, 1]} \Delta \Lambda^a(t, p, \pi) \left( \pi - p - z \right)$$
     Optimal ask quote:
     $$\pi^{a,*}(t, p, q) = (u_{t,p}^a)^{-1}\left( \frac{V(t, p, q-\Delta) - V(t, p, q)}{\Delta} \right)$$
     where $u_{t,p}^a(\pi) = \pi - p + \frac{\Lambda^a(t, p, \pi)}{\partial_\pi \Lambda^a(t, p, \pi)}$.

3. **Parametric Execution Specification:**
   - Volatility process: $\tilde{\sigma}(t, p) = \sigma_0 + \sigma_1 (t/T)^\eta + \frac{\sigma_2}{1 + (\ln(p/(1-p)))^2}$.
   - Order arrival intensities:
     $$\Lambda^b(t, p, \pi) = A(t, p) \left(\frac{\pi}{p}\right)^\nu \exp\left(-k(t)(p - \pi)\right)$$
     $$\Lambda^a(t, p, \pi) = A(t, p) \left(\frac{1 - \pi}{1 - p}\right)^\nu \exp\left(-k(t)(\pi - p)\right)$$
     with overall market activity $A(t, p) = (A_0 + A_1 (t/T)^\xi) 4 p(1-p)$ and liquidity parameter $k(t) = k_0 + (k_1 - k_0)(t/T)^\kappa$.

4. **Quoting Execution Rules:**
   - If $q_t < Q$: Post limit buy order at $\pi^{b,*}(t, p_t, q_t)$ of size $\Delta$.
   - If $q_t > -Q$: Post limit sell order at $\pi^{a,*}(t, p_t, q_t)$ of size $\Delta$.
   - If $q_t = Q$: Cancel bid quote (quote only ask).
   - If $q_t = -Q$: Cancel ask quote (quote only bid).

## Required data

- **Venue & Markets:** Prediction market CLOBs:
  - Polymarket (Polygon on-chain settlement, CTF exchange contracts);
  - Kalshi (CFTC-regulated binary event contracts).
- **Timeframe & Granularity:** Real-time L2 order book quotes and market order trade prints; discrete time step $h \approx 1\text{ s}$ to $1\text{ min}$ for HJB lookup.
- **Fields:** Mid-price / implied probability $p_t$, best bid $\pi_t^b$, best ask $\pi_t^a$, time-to-settlement $T - t$, contract inventory $q_t$, cash balance $X_t$.
- **Model Parameters:** Calibrated baseline volatility $\sigma_0$, time acceleration $\sigma_1, \eta$, activity constants $A_0, A_1$, liquidity decay $k_0, k_1$, risk aversion $(\gamma, \gamma_T)$.

## Execution assumptions

- **Order Model:** Passive limit orders posted at optimal quotes $\pi^{b,*}, \pi^{a,*}$; fills arrive as non-homogeneous Poisson processes with intensity $\Lambda^b, \Lambda^a$.
- **Inventory Bound:** Discrete grid $\mathcal{Q}$ with hard boundary $[-Q, Q]$ (e.g. $Q = 100\text{ contracts}, \Delta = 1$).
- **Exchange Fees:** Polymarket maker fee = $0\text{ bps}$; taker fee = $0\text{ bps}$ (fee-free market making). Kalshi maker rebate / fee schedule applied where applicable.
- **Settlement:** Cash settlement at $T$ to either $\$1.00$ (event occurred) or $\$0.00$ (event did not occur).

## Evidence

### Source-reported

Feil & Nendel (2026) evaluate the optimal quoting strategy against a myopic benchmark (which maximizes instantaneous expected mark-to-market profit and ignores inventory risk) across **10,000 Monte Carlo simulation paths** ($T = 1.0, p_0 = 0.50$):

| Performance & Risk Metric | Baseline Myopic Strategy | Optimal Quoting Strategy | Performance Improvement |
| :--- | :--- | :--- | :--- |
| **Mean Terminal PnL** | Baseline | Nearly identical (~98% retained) | Minimal profit sacrifice |
| **Standard Deviation of PnL** | **28.11** | **10.34** | **63.2% reduction in volatility** |
| **Average Absolute Terminal Inventory ($E[\|q_T\|]$)** | **49.37** | **15.23** | **69.1% reduction in inventory overhang** |
| **5% Value-at-Risk ($\text{VaR}_{0.05}$)** | **32.41** | **4.20** | **87.0% reduction in tail loss** |
| **5% Expected Shortfall ($\text{ES}_{0.05}$ / CVaR)** | **40.50** | **9.68** | **76.1% reduction in tail severity** |

Key structural insights reported by the authors:
- **Spread Compression over Time:** The optimal spread narrows as $t \to T$ due to rising market activity and spread sensitivity $k(t)$, but widens near $T$ specifically when $p \approx 0.50$ due to peak settlement uncertainty.
- **Intrinsic Boundary Skew:** Even with zero inventory ($q=0$), quotes are positively skewed for $p < 0.50$ and negatively skewed for $p > 0.50$, matching the empirical reality that buying at low prices carries asymmetric fill intensity compared to selling.
- **Inventory Sensitivity:** Increasing terminal risk aversion $\gamma_T$ aggressively forces inventory toward zero in the final $10\%$ of contract life ($t \in [0.9 T, T]$).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Toxic Informed Flow at Event Resolution:** In prediction markets with rapid breaking news (e.g. election call, breaking court ruling), informed takers submit large aggressive orders before the market maker can cancel standing limit orders, leading to adverse selection.
- **Illiquid / Stale Markets:** In contracts with low baseline activity ($A_0 \approx 0$), execution rates are insufficient to unwind inventory before $T$, forcing reliance on wider spreads that reduce fill rates further.
- **Model Intensity Mis-specification:** If actual taker flow deviates significantly from the assumed exponential intensity $\Lambda(t, p, \pi)$, quote optimization can misprice execution probabilities.

## Falsification plan

The optimal prediction market making strategy will be deemed falsified if:
1. **Downside Protection Failure:** In an empirical walk-forward backtest on historical Polymarket order books (2024–2026), the strategy's 5% Value-at-Risk exceeds $50\%$ of the myopic baseline's VaR.
2. **Profit Deficit:** The strategy captures $< 70\%$ of the gross bid-ask spread profit earned by a simple symmetric fixed-spread market maker across liquid election/macro markets.
3. **Toxic Jump Loss:** During sudden news events (implied probability shifts $> 20\%$ in $< 5\text{ minutes}$), adverse selection losses exceed total cumulative spread earnings over the preceding 30 days.
4. **Finite Difference Instability:** Numerical solution of the 3D reduced HJB equation fails to converge within 50 iterations or violates maximum principle monotonicity on fine grids ($N_p > 500, N_t > 1000$).

## Crypto portability

**Direct**: Polymarket is a decentralized cryptocurrency prediction market protocol deployed on Polygon, utilizing USDC as the settlement currency and conditional token frameworks (CTF).

Portability considerations:
- Direct execution via Polymarket CLOB API / WebSockets.
- Applicable to on-chain decentralized prediction platforms (Polymarket, Azuro, Limitless) and regulated centralized venues (Kalshi, PredictIt).
- Native handling of 24/7 continuous trading and discrete resolution timestamps.

## Limitations

- **not independently reproduced**;
- **order arrival intensity parametrization:** relies on specific functional forms for $\Lambda^b, \Lambda^a$ that require empirical calibration per market category;
- **latency & cancel-replace speed:** on-chain or API latency during news shocks exposes standing quotes to informed arbitrage;
- **discrete inventory grid:** assumes trade increments $\Delta$ on a finite bounded grid $\mathcal{Q}$.

## Implementation status

not-implemented

No implementation in PyBroker, NautilusTrader, or internal live trading systems has been performed.

## Adoption boundary

research-only

This record is research material only. It does not constitute investment advice, a validated trading system, or authorization for Paper, Testnet, or Live trading execution.

## Related Wiki records

- [[quant/crypto-cross-platform-binary-threshold-mispricing-polymarket-binance-2026-09-01]] — Polymarket vs Binance binary threshold pricing.
- [[quant/crypto-kalshi-prediction-market-macro-repricing-volatility-forecasting-2026-09-01]] — Prediction market implied volatility forecasting.
- [[quant/crypto-short-horizon-prediction-market-settlement-push-reversal-2026-09-01]] — Short-horizon settlement dynamics in prediction markets.

## Sources

1. Feil, D., & Nendel, M. (2026). "Optimal Market Making in Prediction Markets." *arXiv preprint arXiv:2607.17991v1 [q-fin.TR / math.OC / q-fin.MF]*, published 20 July 2026. URL: https://arxiv.org/abs/2607.17991. DOI: https://doi.org/10.48550/arXiv.2607.17991.
2. Avellaneda, M., & Stoikov, S. (2008). "High-Frequency Trading in a Limit Order Book." *Quantitative Finance*, 8(3), 217–224. DOI: https://doi.org/10.1080/14697680701381228.
3. Guéant, O., Tapia, C. A., & Manziadi, Z. (2013). "Dealing with the inventory risk: a solution to the market making problem." *Mathematics and Financial Economics*, 6(4), 259–277. DOI: https://doi.org/10.1007/s11579-012-0087-0.
4. Guéant, O. (2017). "Optimal market making." In *The Financial Mathematics of Market Liquidity: Mechanics, Modelling and Trading* (pp. 107–152). Chapman and Hall/CRC.
5. Hanson, R. (2003). "Combinatorial Information Market Design." *Information Systems Frontiers*, 5(1), 107–119. DOI: https://doi.org/10.1023/A:1022658200490.
6. Krylov, N. V. (1996). *Lectures on Elliptic and Parabolic Equations in Hölder Spaces*. Graduate Studies in Mathematics, Vol. 12. American Mathematical Society, Providence, RI.
