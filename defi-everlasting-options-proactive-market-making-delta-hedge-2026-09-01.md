---
schema: strategy-research-record-v1
title: Everlasting Options Delta-Hedged Proactive Market Making (PMM) Liquidity Provision
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - options
  - everlasting-options
  - market-making
  - delta-hedging
  - proactive-market-maker
  - pmm
  - funding-rate
status: research-only
confidence: high
source_as_of: 2026-05
sources:
  - https://arxiv.org/abs/2508.07068
  - https://doi.org/10.48550/arXiv.2508.07068
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Everlasting Options Delta-Hedged Proactive Market Making (PMM) Liquidity Provision

## Provenance

- **Primary Academic Source:** Hardhik Mohanty, Giovanni Zaarour, and Bhaskar Krishnamachari, "Proactive Market Making and Liquidity Analysis for Everlasting Options in DeFi Ecosystems," *arXiv preprint arXiv:2508.07068v2* [q-fin.MF / q-fin.TR], August 9, 2025 (revised May 2026). Published in *Proceedings of the 2025 IEEE International Conference on Blockchain and Cryptocurrency (ICBC 2025)*. DOI: [10.48550/arXiv.2508.07068](https://doi.org/10.48550/arXiv.2508.07068).
- **Institution:** Autonomous Networks Research Group (ANRG), Department of Electrical and Computer Engineering, University of Southern California (USC), Los Angeles, USA.
- **Reference Code / Artifacts:** Everlasting Options Market Simulator (USC-ANRG / everlasting-options-simulator).

## Economic mechanism

### Source-reported

Mohanty, Zaarour, and Krishnamachari (2025/2026) investigate liquidity provisioning, funding mechanisms, and risk management for **everlasting options** (non-expiring perpetual options) in decentralized finance (DeFi):
1. **Liquidity Fragmentation in Fixed-Expiry Options:** Traditional European/American crypto options suffer from severe liquidity fragmentation across dozens of discrete expiration dates and strike prices. Traders incur heavy friction and roll slippage when rolling expiring positions into forward contracts.
2. **Unified Liquidity via Perpetual Funding:** Everlasting options eliminate expiration dates by implementing a continuous funding rate mechanism. A constant stream of funding payments $F_t$ is exchanged between long and short positions to peg the mark price $O_t$ to the target equivalent payoff (e.g., Black-Scholes or intrinsic value). Liquidity is concentrated into a single perpetual pool per strike, maintaining near-constant slippage rather than the parabolic slippage growth observed in fragmented AMM pools.
3. **Proactive Market Maker (PMM) vs AMM:** Rather than passive Constant Product Market Makers ($xy = k$), the authors deploy a dynamic Proactive Market Maker (PMM) pricing curve:
   $$P_{\text{AMM}}(Q) = P_{\text{oracle}} \cdot \left( 1 + k \cdot \left( \frac{B_0 - B}{B_0} \right) \right)$$
   which concentrates liquidity near the oracle price $P_{\text{oracle}}$ and minimizes uncompensated loss-versus-rebalancing (LVR).
4. **Dynamic $\Delta$-Hedging for Liquidity Providers (LPs):** The primary risk for option LPs is directional gamma/delta exposure. By coupling PMM quote provision with continuous dynamic $\Delta$-hedging in the liquid underlying spot or perpetual futures market ($\Delta_{\text{net}} = \sum_i Q_i \cdot \frac{\partial O_i}{\partial S}$), LPs capture trading spread fees and net funding payments while neutralizing underlying price drift.

### Research interpretation

This architecture defines a **Delta-Neutral DeFi Volatility & Spread Harvesting Strategy**:
1. **Spread & Carry Capture:** The market maker provides liquidity on bilateral everlasting option pools, collecting:
   - Taker swap/trading fees ($\gamma_{\text{fee}} \approx 10 - 30\text{ bps}$).
   - Asymmetric funding carry when option implied volatility trades at a premium/discount relative to the target funding benchmark.
2. **First-Order Risk Immunization:** By automatically rebalancing spot/perp hedges when the cumulative inventory delta $|\Delta_{\text{portfolio}}| > \Delta_{\text{threshold}}$, the LP transforms an inherently non-linear options underwriting book into a market-neutral yield generator.
3. **Slippage Advantage:** Because everlasting options pool long-term and short-term open interest into a single contract, market depth is significantly higher than fragmented monthly/weekly options, lowering hedging execution friction.

## Signal

The market-making and hedging execution algorithm is formalized as follows:

1. **Option Pricing & Funding Calculation:**
   - For an everlasting option with underlying price $S_t$, strike $K$, risk-free rate $r$, and funding period $T_{\text{fund}}$ (e.g., 1 day):
     $$O_{\text{theoretical}}(S_t, K) = \text{BS}(S_t, K, \sigma_{\text{implied}}, T_{\text{fund}})$$
   - Cumulative funding payment per unit held over interval $\delta t$:
     $$F_t = \frac{O_{\text{mark},t} - \max(S_t - K, 0)}{T_{\text{fund}}} \cdot \delta t$$

2. **PMM Dynamic Bid-Ask Quoting:**
   - Mid-price set by oracle: $P_{\text{mid},t} = O_{\text{theoretical},t}$.
   - Bid quote: $P_{\text{bid},t} = P_{\text{mid},t} \cdot \left( 1 - \frac{\text{spread}}{2} - k_{\text{inv}} \cdot \frac{I_{\text{call},t}}{C_{\text{pool}}} \right)$
   - Ask quote: $P_{\text{ask},t} = P_{\text{mid},t} \cdot \left( 1 + \frac{\text{spread}}{2} - k_{\text{inv}} \cdot \frac{I_{\text{call},t}}{C_{\text{pool}}} \right)$
   where $I_{\text{call},t}$ is current net option inventory, $C_{\text{pool}}$ is pool capital, and $k_{\text{inv}}$ is the inventory skew parameter.

3. **Continuous Delta-Hedging Trigger:**
   - Compute aggregate portfolio Delta:
     $$\Delta_{\text{total},t} = \sum_{j \in \{\text{calls, puts}\}} I_{j,t} \cdot \Delta_{j}(S_t, K_j) + H_{\text{spot/perp},t}$$
     where $\Delta_{\text{call}} = N(d_1)$ and $\Delta_{\text{put}} = N(d_1) - 1$.
   - **Hedging Decision Rule:**
     $$\text{If } |\Delta_{\text{total},t}| > \Delta_{\text{tol}} \quad (\text{e.g., } \Delta_{\text{tol}} = 0.05 \cdot \text{Portfolio Size}):$$
     - Send market/TWAP order to underlying perpetual futures venue:
       $$\text{Order Size } \Delta H = -\Delta_{\text{total},t}$$
     - Reset $\Delta_{\text{total},t} \approx 0$.

4. **Holding Period & Inventory Decay:**
   - Continuous market making with rolling 8-hour / daily funding settlement. Inventory imbalances decay via dynamic PMM skew pricing that incentivizes offsetting taker flow.

## Required data

- **Instruments:** Everlasting call/put options and underlying spot / perpetual futures (e.g., BTC, ETH).
- **Venues:** DeFi Everlasting Options AMM/PMM contracts (e.g., Arbitrum, Optimism, Solana) + CEX/DEX perpetual futures market for hedging (e.g., Binance, Hyperliquid, Bybit).
- **Timeframe:** Continuous block-by-block event updates (sub-second on L2s) aggregated into 1-second and 1-minute delta-monitoring intervals.
- **Fields:** Underlying spot mark price $S_t$, option contract mark price $O_t$, implied volatility surface $\sigma_{\text{implied}}(K)$, cumulative inventory $I_j$, pool reserve levels, gas prices (Gwei), perpetual funding rates.

## Execution assumptions

- **Quoting Model:** Passive liquidity provision via PMM smart contract; taker fills trigger automated rebalance hooks.
- **Hedging Venue:** Liquid perpetual futures with maker rebate or low taker fee ($\le 2 - 5\text{ bps}$).
- **Gas / L2 Friction:** On-chain transactions routed via low-latency L2s (Arbitrum, Solana); gas costs modeled at $\$0.01 - \$0.10$ per hedge transaction.
- **Oracle Latency:** Price updates via low-latency pull oracles (Pyth / Chainlink Low Latency Streams) to prevent front-running arbitrage.

## Evidence

### Source-reported

All empirical and simulation findings below are directly reported by Mohanty, Zaarour, and Krishnamachari (IEEE ICBC 2025 / arXiv:2508.07068v2):
1. **Slippage Invariance:** Slippage for everlasting options under the PMM architecture remains nearly flat across wide inventory variations, unlike fixed-expiration option AMMs where slippage scales parabolically with pool depletion.
2. **Net Positive LP Profitability:** In multi-scenario Monte Carlo simulations incorporating geometric Brownian motion and jump-diffusion price paths with high gas costs and volatile funding, $\Delta$-hedged PMM liquidity providers achieved consistently positive net PnL (fee income + funding capture exceeding hedging costs and residual gamma slippage).
3. **Failure of Unhedged LPing:** Unhedged liquidity providers experienced severe drawdowns and high variance, demonstrating that dynamic delta-neutralization is essential for sustainable options market making.
4. **Funding Equilibrium:** Funding payments successfully anchored the mark price of everlasting contracts to their theoretical equivalent, preventing runaway price divergence.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- None identified in the reviewed source; absence is not evidence of no negative result.
- General DeFi derivatives literature notes that during extreme market-wide tail jumps (e.g., $> 15\%$ intraday flash crashes), high gamma ($\Gamma$) exposure can cause hedging slippage to outpace fee accrual if L2 sequencer congestion delays hedging transactions.

## Falsification plan

1. **Ablation vs Fixed-Expiration AMM Market Making:** Compare the risk-adjusted Sharpe and maximum drawdown of the Everlasting PMM strategy against a standard fixed-expiration option AMM liquidity pool (e.g., Lyra / Dopex style). If everlasting options do not reduce hedging rebalance costs and inventory slippage by at least 25% relative to fixed expiries, the unified liquidity advantage is falsified.
2. **High-Volatility Jump Stress Test:** Simulate jump-diffusion price paths with jumps $\Delta S / S > 10\%$ accompanied by 5-block L2 execution delay. If cumulative LP PnL turns permanently negative due to gamma bleed, the strategy fails without additional exotic variance buffers.
3. **Funding Rate Basis Inversion:** Test whether chronic one-sided market sentiment causes prolonged funding rate divergence where longs refuse to pay funding, forcing the LP to absorb negative carry.

## Crypto portability

- **Direct:** Everlasting options are natively designed for cryptocurrency and DeFi architectures (originally conceptualized for crypto perpetual derivative markets).
- **Crypto-specific factors:** 24/7 continuous trading avoids weekend jump risk; L2 smart contracts enable automated programmatic execution of PMM math and delta-hedging hooks.

## Limitations

- **Simulated Environment:** Empirical results in the primary source are based on simulated market paths and historical backtesting; production live-pool TVL for everlasting options in DeFi remains smaller than standard perpetual futures.
- **Oracle Dependence:** PMM pricing relies on continuous oracle feeds; oracle front-running or stale pricing during network congestion represents a material adverse-selection risk.
- **Execution Latency Risk:** Gas spikes or L2 sequencer downtime can temporarily impair delta-hedging rebalancing.

## Implementation status

No implementation in our research stack has been completed. Not implemented in PyBroker or NautilusTrader.

## Adoption boundary

Research material only. A record being present in this repository does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

## Related Wiki records

- `defi-on-chain-options-mispricing-hegic-arbitrum-2026-09-01.md`
- `crypto-options-volatility-risk-premium-zscore-2026-08-31.md`
- `crypto-deribit-options-volatility-of-volatility-vov-realized-quarticity-2026-09-01.md`
- `funding-aware-market-making-perpetual-dex-2026-08-31.md`

## Sources

1. Hardhik Mohanty, Giovanni Zaarour, and Bhaskar Krishnamachari, "Proactive Market Making and Liquidity Analysis for Everlasting Options in DeFi Ecosystems," *arXiv preprint arXiv:2508.07068v2* [q-fin.MF / q-fin.TR], May 2026; *Proceedings of the 2025 IEEE International Conference on Blockchain and Cryptocurrency (ICBC)*.
   - DOI: https://doi.org/10.48550/arXiv.2508.07068
   - arXiv: https://arxiv.org/abs/2508.07068
   - Simulator Repository: https://github.com/USC-ANRG/everlasting-options-simulator
