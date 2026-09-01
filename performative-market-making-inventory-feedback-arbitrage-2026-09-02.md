---
schema: strategy-research-record-v1
title: "Performative Market Making: Strategic Exploitation of Inventory-Control Feedback Loops and Performative Equilibrium"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-making
  - microstructure
  - performativity
  - avellaneda-stoikov
  - inventory-control
  - game-theory
  - nash-equilibrium
status: research-only
confidence: high
source_as_of: 2026-02-15
sources:
  - "Charalampos Kleitsikas, Stefanos Leonardos, Carmine Ventre, 'Performative Market Making', arXiv:2508.04344v2 [q-fin.TR, cs.GT], February 2026. DOI: 10.48550/arXiv.2508.04344. https://arxiv.org/abs/2508.04344"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Performative Market Making: Strategic Exploitation of Inventory-Control Feedback Loops and Performative Equilibrium

## Provenance

- **Primary Source:** Charalampos Kleitsikas, Stefanos Leonardos, and Carmine Ventre (King's College London, Department of Informatics), *"Performative Market Making"*, arXiv preprint `arXiv:2508.04344v2 [q-fin.TR, cs.GT]`, submitted August 6, 2025, revised February 15, 2026. DOI: [10.48550/arXiv.2508.04344](https://doi.org/10.48550/arXiv.2508.04344). Full text: [https://arxiv.org/abs/2508.04344](https://arxiv.org/abs/2508.04344).
- **Primary Categories:** Quantitative Finance - Trading and Market Microstructure (`q-fin.TR`), Computer Science - Computer Science and Game Theory (`cs.GT`).
- **Context:** Mathematical formalization of performativity in financial market microstructure. Bridges classical inventory-based market making (Avellaneda and Stoikov, 2008) with performative prediction, proving how a strategic market maker can reverse-engineer and exploit the deterministic price drift induced by peer market makers' inventory-control rules.

## Economic mechanism

### Source-reported

Classical market-making frameworks (e.g., Avellaneda and Stoikov 2008, Guéant et al. 2012) assume an exogenous, uncoupled price process (typically an arithmetic or geometric Brownian motion). In reality, financial models are **performative**: when multiple algorithmic market makers adopt similar inventory-skew models, their quoting behavior actively shapes and alters the price dynamics they seek to predict.

Kleitsikas, Leonardos, and Ventre (2026) establish:
1. **The Performative Feedback Loop:** Standard Avellaneda-Stoikov (A&S) market makers continuously adjust their reservation prices $r(s, q, t) = s - q \gamma \sigma^2 (T-t)$ and quote asymmetric bid/ask spreads $(\delta^b(q), \delta^a(q))$ to offload accumulated inventory $q$. When market makers represent a significant fraction of liquidity, their synchronized inventory-skewing behavior injects a deterministic drift into the mid-price:
   $$dS_t = \mu(Q_t^{\text{agg}}) dt + \sigma dW_t$$
   where $Q_t^{\text{agg}}$ is the aggregate inventory of the prevailing market makers.
2. **Alpha Decay and Exploitation:** The deterministic drift $\mu(Q_t^{\text{agg}})$ induces alpha decay on conventional A&S strategies. A strategic "performative market maker" (PMM) that embeds knowledge of the market participants' decision rules into its own optimization can:
   - Accurately predict the future price trajectory resulting from peer inventory dumping;
   - Post strategic quotes that capture the predictable inventory-unwinding drift;
   - Extract superior expected profit and loss ($\text{P\&L}$) and Sharpe ratios without taking uncompensated directional bets.
3. **Performative Stability:** The paper proves the existence of a *performative stable state* (a game-theoretic fixed point / Nash equilibrium) where other market participants cannot profitably deviate to alternative naive pricing strategies.

### Research interpretation

The actionable alpha thesis is **strategic liquidity provision through peer inventory inference**:
- In electronic and crypto markets where automated market makers share standard risk aversion parameters $\gamma$ and inventory-control horizons $T$, large liquidity-taking shocks push peer MMs into synchronized inventory states (e.g., heavily long after a retail selling wave).
- Naive MMs lower their ask quotes and widen their bid quotes to liquidate inventory, causing predictable short-term downward price pressure.
- The performative market maker exploits this by shading its quotes in the opposite direction: tightening its bid when peer MMs are dumping at discounted prices, and posting opportunistic asks once peer inventory is exhausted, harvesting both the bid-ask spread and the performative inventory-reversion drift.

## Signal

### Aggregate Peer Inventory Estimator
1. **LOB Quote Asymmetry Tracking:** Observe top-of-book bid and ask depths $(v_t^b, v_t^a)$ and spreads $(\delta_t^b, \delta_t^a)$ from reference mid-price $S_t$.
2. **Inferred Peer Inventory ($\hat{q}_t^{\text{peer}}$):**
   Invert the standard Avellaneda-Stoikov reservation formula:
   $$\hat{q}_t^{\text{peer}} = \frac{\delta_t^a - \delta_t^b}{2 \gamma_{\text{est}} \sigma_t^2 (T - t)}$$
   where $\gamma_{\text{est}}$ is the estimated risk aversion of the dominant liquidity providers.

### Performative Quoting Policy
For a performative market maker with inventory $q_t$ and inferred aggregate peer inventory $\hat{Q}_t^{\text{agg}}$:
1. **Performative Reservation Price ($r^{\text{perf}}$):**
   $$r_t^{\text{perf}} = S_t - q_t \gamma \sigma^2 (T-t) + \beta \cdot \mu(\hat{Q}_t^{\text{agg}})(T-t)$$
   where $\mu(\hat{Q}_t^{\text{agg}}) = -\kappa \hat{Q}_t^{\text{agg}}$ represents the expected drift generated by peer inventory liquidation, and $\beta$ is the performative response parameter.
2. **Optimal Quoting Spreads:**
   $$\delta_t^{a, \text{perf}} = r_t^{\text{perf}} - S_t + \frac{1}{\gamma}\ln\left(1 + \frac{\gamma}{\kappa_{\text{order}}}\right)$$
   $$\delta_t^{b, \text{perf}} = S_t - r_t^{\text{perf}} + \frac{1}{\gamma}\ln\left(1 + \frac{\gamma}{\kappa_{\text{order}}}\right)$$
3. **Order Placement Trigger:**
   - Post limit buy order at $P_t^b = S_t - \delta_t^{b, \text{perf}}$ (post-only).
   - Post limit sell order at $P_t^a = S_t + \delta_t^{a, \text{perf}}$ (post-only).
   - Continuously update quotes when $|\hat{Q}_t^{\text{agg}}|$ shifts by more than threshold $\Delta Q_{\text{thresh}}$.

## Required data

- **Instruments:** Liquid centralized exchange perpetuals/spot pairs (Binance, OKX, Bybit) or high-volume decentralized CLOBs (Hyperliquid).
- **Data Granularity:** Top 5-10 LOB price levels and continuous trade flow at $\le 100 \text{ ms}$ snapshot frequency.
- **Fields:** Best Bid Price, Best Ask Price, Best Bid Size, Best Ask Size, Microsecond Timestamps, Signed Trade Executions.
- **Point-in-time:** Online causal state estimation of $\hat{Q}_t^{\text{agg}}$ with zero look-ahead bias.

## Execution assumptions

- **Order Type:** Passive Post-Only Limit Orders (Maker execution to capture maker fee rebates).
- **Latency Requirement:** Quote update and cancellation latency $\le 10 \text{ ms}$.
- **Fee Model:** Maker fee rebate ($-0.2 \text{ bps}$ to $0.0 \text{ bps}$) / Taker fee ($2.0 \text{ bps}$ to $5.0 \text{ bps}$).
- **Inventory Bounds:** Hard inventory constraint $|q_t| \le Q_{\max}$; emergency market-order liquidation triggered if $|q_t| > Q_{\max}$.

## Evidence

### Source-reported

- Kleitsikas, Leonardos, and Ventre (2026, arXiv:2508.04344) provide analytical proofs and multi-agent reinforcement learning simulations:
  1. Closed-form derivation proving that embedding the performative feedback loop transforms the asset price from a martingale into a mean-reverting process driven by aggregate inventory $Q_t^{\text{agg}}$.
  2. In multi-agent environments against standard Avellaneda-Stoikov market makers, the performative market maker achieves strictly higher cumulative P&L and superior risk-adjusted Sharpe ratio across all tested parameter configurations.
  3. Proof of the existence of a performative stable state (Nash equilibrium) where participants cannot profitably deviate by adopting naive pricing.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- If the dominant volume in the market is driven by exogenous toxic informed traders (e.g. news events, large directional takers) rather than inventory-balancing market makers, the estimated drift $\mu(\hat{Q}_t^{\text{agg}})$ will misidentify the true price trajectory, causing adverse selection losses.
- If competing market makers also adopt performative strategies, the predictable drift flattens, compressing the performative premium to zero (competitive equilibrium).
- High latency relative to top HFT firms: if peer MMs update quotes faster than the performative MM can adjust, the strategy risks getting adversely selected on stale limit orders.

## Falsification plan

1. **Synthetic Multi-Agent Simulation Benchmark:** Deploy an agent-based market simulation with $N=10$ standard Avellaneda-Stoikov market makers and evaluate the performative market maker. Falsification threshold: If the performative market maker fails to achieve a statistically significant higher Sharpe ratio ($p < 0.01$) than the baseline A&S agent after 100,000 simulated trading rounds, reject the theoretical advantage.
2. **Empirical Peer Inventory Drift Test:** Regress future 1-minute to 15-minute mid-price returns on inferred aggregate inventory $\hat{Q}_t^{\text{agg}}$ derived from top-of-book skew on Binance/Hyperliquid BTC/ETH perps. Falsification threshold: If the regression slope $\beta_{\text{inventory}}$ is not statistically negative ($t\text{-stat} > -2.0$), the performative feedback assumption is invalid in that market.
3. **Execution Latency Degradation Test:** Introduce simulated quote-update latencies from 5 ms to 200 ms. Falsification threshold: If positive excess PnL vanishes at latency $> 25 \text{ ms}$, mark the strategy as unviable for non-colocated execution.

## Crypto portability

- **Adapted / Unproven:**
  - The theoretical model is formulated for continuous limit order book markets.
  - Crypto perpetual markets (e.g. Binance, Hyperliquid) feature highly automated, programmatic market makers that frequently rely on standard A&S/Guéant inventory frameworks, making performative feedback highly plausible.
  - However, the prevalence of high-leverage retail taker flows, funding rate payments, and cross-exchange lead-lag dynamics can contaminate the pure inventory-drift relationship, requiring empirical validation in crypto.

## Limitations

- **Not independently reproduced:** Results depend on theoretical proofs and simulated agent environments in Kleitsikas et al. (2026).
- **Latent Parameter Identification:** Accurately estimating $\gamma_{\text{est}}$ and the aggregate inventory share of naive vs. sophisticated MMs in real-time is noisy.
- **Toxic Flow Contamination:** Fails to distinguish between inventory-induced quote skews and quote skews caused by private information about impending macro news.

## Implementation status

- `not-implemented`
- Research capture only. No implementation in NautilusTrader, PyBroker, or live market making sidecars.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Not approved for paper, testnet, or live trading.

## Related Wiki records

- `[[market-making-latent-fad-stochastic-control-hjb-2026-09-02]]`
- `[[multi-level-market-making-logistic-normal-deep-sets-2026-09-02]]`
- `[[contrarian-market-making-fill-probability-order-flow-2026-09-01]]`
- `[[funding-aware-market-making-perpetual-dex-2026-08-31]]`
- `[[hyperliquid-sunshine-trading-adverse-selection-liquidity-extraction-2026-09-01]]`

## Sources

1. Charalampos Kleitsikas, Stefanos Leonardos, Carmine Ventre, *"Performative Market Making"*, arXiv preprint `arXiv:2508.04344v2 [q-fin.TR, cs.GT]`, submitted August 6, 2025, revised February 15, 2026. DOI: [10.48550/arXiv.2508.04344](https://doi.org/10.48550/arXiv.2508.04344). Stable URL: https://arxiv.org/abs/2508.04344.
