---
schema: strategy-research-record-v1
title: "Optimal Market Making with Latent Price Fads and Informed Order Flow Filtering"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-making
  - stochastic-control
  - hamilton-jacobi-bellman
  - price-fads
  - adverse-selection
  - nonlinear-filtering
status: research-only
confidence: medium
source_as_of: 2026-06-15
sources:
  - "Emilio Barucci, Adrien Mathieu, and Leandro Sánchez-Betancourt, 'Market Making with Fads, Informed, and Uninformed Traders', arXiv:2501.03658v2 [q-fin.TR], revised June 2026 (forthcoming in Mathematical Finance). https://arxiv.org/abs/2501.03658"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Optimal Market Making with Latent Price Fads and Informed Order Flow Filtering

## Provenance

- **Primary Source:** Emilio Barucci (Politecnico di Milano), Adrien Mathieu (University of Oxford), and Leandro Sánchez-Betancourt (King's College London), *"Market Making with Fads, Informed, and Uninformed Traders"*, arXiv preprint `arXiv:2501.03658v2 [q-fin.TR]`, first submitted January 7, 2025, revised June 2026 (forthcoming in *Mathematical Finance*). URL: https://arxiv.org/abs/2501.03658.
- **Primary Category:** Trading and Market Microstructure (`q-fin.TR`).
- **Mathematical Framework:** Continuous-time stochastic optimal control, Hamilton-Jacobi-Bellman (HJB) system of coupled ODEs/PDEs, and nonlinear filtering for unobserved state estimation.

## Economic mechanism

### Source-reported

Classical market-making frameworks (e.g., Avellaneda-Stoikov, Ho-Stoll) assume the underlying asset price follows a pure martingale (arithmetic Brownian motion) where price changes are permanent, and market makers manage only inventory risk and adverse selection against static arrival intensities.

Barucci, Mathieu, and Sánchez-Betancourt introduce a structural market microstructure model where the observed market midprice $S_t$ consists of two distinct components:
$$S_t = V_t + Y_t$$
where:
1. $V_t$ is the **unobservable fundamental value**, modeled as a continuous martingale:
   $$dV_t = \sigma dW_t^V$$
2. $Y_t$ is a **transitory price "fad"** (short-term deviation/mispricing), modeled as an Ornstein-Uhlenbeck mean-reverting process:
   $$dY_t = -\kappa Y_t dt + \eta dW_t^Y$$

The market is populated by two distinct classes of market participants:
- **Informed Traders:** Understand that $Y_t$ is transitory. When the fad is positive ($Y_t > 0$, asset overvalued), informed traders arrive predominantly on the ask side (selling to capture overvaluation). When $Y_t < 0$, informed traders buy.
- **Uninformed / Noise Traders:** Insensitive to the fad; arrive symmetrically on both sides of the book according to standard price-sensitivity intensity functions.

The market maker posts bid and ask quotes around midprice:
$$S_t^a = S_t + \delta_t^a, \quad S_t^b = S_t - \delta_t^b$$
Crucially, the market maker does not directly observe whether incoming orders originate from informed or uninformed traders, nor do they directly observe the true decomposition $(V_t, Y_t)$. Under this information asymmetry, the optimal liquidity provision strategy requires:
1. **Asymmetric Spread Skewing:** As the fad $Y_t$ increases, the optimal market maker widens the bid spread $\delta_t^{b*}$ to protect against adverse selection from informed sellers, while tightening the ask spread $\delta_t^{a*}$ (decreasing the price of liquidity) to sell inventory aggressively to uninformed buyers at inflated prices prior to mean reversion.
2. **Nonlinear Latent Fad Filtering:** In the realistic partial information regime, the market maker constructs a real-time filter $\hat{Y}_t = \mathbb{E}[Y_t \mid \mathcal{F}_t^{\text{orders}}]$ from the observed point-process order arrival history $(\Delta N_t^a, \Delta N_t^b)$.

### Research interpretation

This mechanism provides a rigorous blueprint for high-frequency algorithmic market making in markets with strong mean-reverting microstructure:
1. **Dynamic Skew beyond Pure Inventory:** Traditional Avellaneda-Stoikov skewing shifts spreads solely based on current inventory $q_t$. This model proves that optimal quoting requires a two-dimensional state space: inventory $q_t$ and the estimated fad state $\hat{Y}_t$.
2. **Exploiting Informed vs. Noise Asymmetry:** When an asset is temporarily pumped by retail enthusiasm ($Y_t > 0$), naive market makers get run over on the bid. The fad-aware market maker widens bids and dumps long inventory into uninformed ask orders, maximizing PnL while minimizing toxic flow.

## Signal

### 1. Market Dynamics & Order Arrival Intensity

- **Midprice:** $S_t = V_t + Y_t$, with mean reversion speed $\kappa > 0$ and volatility parameters $\sigma, \eta$.
- **Informed Proportion:** Let $\alpha \in [0, 1]$ be the proportion of informed traders in the market.
- **Order Arrival Rates:**
  - **Ask Side (Trader Buys from MM):**
    $$\lambda_t^a(\delta_t^a, Y_t) = (1 - \alpha) \Lambda^u e^{-k \delta_t^a} + \alpha \Lambda^i e^{-k (\delta_t^a + Y_t)}$$
  - **Bid Side (Trader Sells to MM):**
    $$\lambda_t^b(\delta_t^b, Y_t) = (1 - \alpha) \Lambda^u e^{-k \delta_t^b} + \alpha \Lambda^i e^{-k (\delta_t^b - Y_t)}$$

### 2. Market Maker Objective & HJB Formulation

The market maker maximizes expected terminal utility of wealth and inventory over horizon $[0, T]$ with absolute risk aversion $\gamma$:
$$\max_{(\delta^a, \delta^b)} \mathbb{E}\left[-\exp\left(-\gamma \left(X_T + q_T S_T - \frac{\alpha_c}{2} q_T^2\right)\right)\right]$$

Applying the ansatz $v(t, x, q, y) = -\exp(-\gamma x) \exp(-\gamma q S) \exp\left(-\gamma \theta(t, q, y)\right)$, the value function satisfies the Hamilton-Jacobi-Bellman (HJB) system:
$$\partial_t \theta + \frac{1}{2}\sigma^2 q^2 \gamma - q \kappa y + \frac{1}{2}\eta^2 \partial_{yy}\theta - \frac{1}{2}\gamma \eta^2 (\partial_y \theta)^2 - \kappa y \partial_y \theta + \max_{\delta^a} \mathcal{H}^a(\delta^a) + \max_{\delta^b} \mathcal{H}^b(\delta^b) = 0$$

### 3. Optimal Quoting Policy ($\delta^{a*}, \delta^{b*}$)

The first-order conditions yield the optimal half-spreads:
$$\delta_t^{a*}(q, \hat{Y}_t) = \frac{1}{k} + \theta(t, q, \hat{Y}_t) - \theta(t, q-1, \hat{Y}_t) - \frac{1}{k} \ln \left(\frac{(1-\alpha)\Lambda^u + \alpha \Lambda^i e^{-k \hat{Y}_t}}{(1-\alpha)\Lambda^u + \alpha \Lambda^i}\right)$$
$$\delta_t^{b*}(q, \hat{Y}_t) = \frac{1}{k} + \theta(t, q, \hat{Y}_t) - \theta(t, q+1, \hat{Y}_t) - \frac{1}{k} \ln \left(\frac{(1-\alpha)\Lambda^u + \alpha \Lambda^i e^{k \hat{Y}_t}}{(1-\alpha)\Lambda^u + \alpha \Lambda^i}\right)$$

### 4. Latent Fad State Estimation ($\hat{Y}_t$)

Under partial information (where $Y_t$ is latent), $\hat{Y}_t$ is updated continuously via point-process stochastic filtering:
$$d\hat{Y}_t = -\kappa \hat{Y}_t dt + K_t^a \left(dN_t^a - \hat{\lambda}_t^a dt\right) + K_t^b \left(dN_t^b - \hat{\lambda}_t^b dt\right)$$
where $K_t^a, K_t^b$ are the filter Kalman-like gain matrices derived from the conditional likelihood ratio of trade arrivals.

## Required data

- **Instrument Universe:** High-frequency liquid instruments (Equities, Crypto Perpetuals, FX pairs).
- **Venues:** CME, Binance Futures, Bybit, Hyperliquid, Coinbase.
- **Timeframe:** Subsecond tick event streams (Level-2 LOB snapshots and trade prints).
- **Fields:**
  - Individual trade prints (price, size, aggressor side: buy/sell).
  - L2 order book top-of-book quotes ($S_t^a, S_t^b$) and spread.
  - Real-time midprice series ($S_t$).
  - Estimated parameters ($\kappa, \eta, \sigma, \alpha, \Lambda^u, \Lambda^i, k$) calibrated via rolling Maximum Likelihood Estimation (MLE) or GMM on intraday order flow.

## Execution assumptions

- **Quoting Mechanics:** Resting passive limit orders placed simultaneously at $S_t + \delta_t^{a*}$ and $S_t - \delta_t^{b*}$.
- **Inventory Bounds:** Hard inventory limits $q \in [-Q_{\max}, Q_{\max}]$ enforced by penalty parameter $\alpha_c$ or quote cancellation at boundaries.
- **Latency & Cancellation:** Tick-to-trade latency < 10ms for updating quotes upon trade execution or midprice drift.
- **Fee Model:** Maker rebate structure (e.g., -0.5 bps to 0.0 bps) or standard VIP maker tier.

## Evidence

### Source-reported

- **Price of Liquidity Characterization:** The paper formally proves that the price of liquidity (optimal bid-ask spread) is a strictly increasing convex function of the proportion of informed traders $\alpha$.
- **Asymmetric Spread Dynamics:**
  - In numerical simulations and calibrated test beds, when $\hat{Y}_t > 0$, the market maker widens the bid spread ($\delta_t^{b*} \uparrow$) and tightens the ask spread ($\delta_t^{a*} \downarrow$).
  - As $\alpha$ increases from $0.0$ to $0.4$, the magnitude of the optimal spread widening during fad extremities increases by more than **$2.5\times$**, demonstrating that failure to account for informed adverse selection during fads leads to severe adverse selection losses.
- **Outperformance over Standard Avellaneda-Stoikov:**
  - Across Monte Carlo simulations incorporating mean-reverting fads, the fad-aware HJB market maker achieves higher expected terminal PnL and a significantly higher Sharpe ratio than a standard inventory-only Avellaneda-Stoikov benchmark (which suffers systematic inventory losses during large fad excursions).
  - The nonlinear filtering method effectively tracks latent fad dynamics $\hat{Y}_t$ from anonymous trade arrival counts alone.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Parameter Mis-specification Risk:** If the true mean-reversion parameter $\kappa$ is overestimated (i.e., the price movement is actually a permanent fundamental shock $dV_t$ rather than a transitory fad $Y_t$), the market maker will aggressively lean against a persistent trend, accumulating toxic adverse inventory.
- **Numerical Complexity:** Solving the coupled HJB system in real time for large inventory grids ($Q_{\max} > 50$) requires pre-computed offline lookup tables or neural network approximations.

## Falsification plan

1. **HJB Policy vs. Benchmark Ablation Test:** Deploy two parallel market-making simulators on historical tick data: Model 1 (Fad-Aware HJB with $\hat{Y}_t$ filtering) vs. Model 2 (Standard Avellaneda-Stoikov with symmetric intensity).
   - **Failure Rule:** If Model 1 does not achieve at least a $15\%$ improvement in Sharpe ratio or a $20\%$ reduction in inventory drawdown during high-volatility mean-reverting regimes, the theoretical advantage of fad modeling is falsified.
2. **Latent Filter Information Content Test:** Compute the correlation between the filtered state $\hat{Y}_t$ and future realized 5-minute price returns $(S_{t+5\text{m}} - S_t)$.
   - **Failure Rule:** If the Spearman rank correlation is not significantly negative ($\rho \ge -0.05$, indicating failure to forecast mean reversion), the order-flow filter carries no actionable predictive content.
3. **Regime Shift Stress Test:** Subject the quoting algorithm to synthetic data where $100\%$ of price jumps are permanent Brownian jumps ($\eta = 0, \kappa = 0$).
   - **Failure Rule:** Measure maximum drawdown under regime breakdown; establish strict circuit-breaker thresholds where the algorithm defaults to wide symmetric quoting if filtering residual errors exceed $3\sigma$.

## Crypto portability

**adapted**

The theoretical model is asset-agnostic and particularly relevant to cryptocurrency perpetual markets:
- **Frequent Transitory Price Dislocations ("Fads"):** Crypto markets frequently experience violent transitory price distortions driven by retail liquidations, social sentiment cascades, and leveraged funding spikes that exhibit rapid mean reversion ($\kappa \gg 1$).
- **Anonymous Microstructure:** Crypto order books are fully anonymous, matching the partial information assumption where market makers observe only execution timestamps and sizes.
- **Perpetual Funding Drift:** The funding rate mechanism provides an observable proxy/anchor for the direction and magnitude of the price fad $(S_t - \text{Index}_t)$, simplifying the estimation of $Y_t$.

## Limitations

- **Continuous Model vs. Discrete Queue Priority:** The theoretical HJB model assumes continuous quoting and execution intensities, abstracting away discrete price ticks and queue priority mechanics in real limit order books.
- **Latency Sensitivity:** Market makers face adverse selection if latency is too high to cancel quotes before informed traders hit them.
- **Assumption of Constant Informed Fraction $\alpha$:** In live markets, the proportion of informed order flow $\alpha$ fluctuates dynamically across market regimes.

## Implementation status

No implementation in our research stack. The record documents published mathematical and computational results from Barucci, Mathieu, and Sánchez-Betancourt (arXiv:2501.03658v2, 2026); no PyBroker, Nautilus, or live trading components have been created.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[quant/multi-level-market-making-logistic-normal-deep-sets-2026-09-02]] — Multi-level market making and inventory control
- [[quant/funding-aware-market-making-perpetual-dex-2026-08-31]] — Funding-aware market making in perpetual DEXs
- [[quant/prediction-market-optimal-market-making-latent-belief-hjb-2026-09-01]] — Latent belief HJB market making in prediction markets
- [[quant/crypto-noise-perturbed-order-flow-privacy-subsidy-kyle-market-making-2026-09-01]] — Order flow privacy and Kyle market making

## Sources

1. Emilio Barucci, Adrien Mathieu, and Leandro Sánchez-Betancourt, "Market Making with Fads, Informed, and Uninformed Traders", arXiv preprint arXiv:2501.03658v2 [q-fin.TR], first submitted January 7, 2025, revised June 2026 (forthcoming in Mathematical Finance). URL: https://arxiv.org/abs/2501.03658.
