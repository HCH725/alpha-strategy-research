---
schema: strategy-research-record-v1
title: AMM Loss-Versus-Rebalancing (LVR) and Toxic Arbitrage
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - amm
  - lvr
  - adverse-selection
  - mev
  - cex-dex-arbitrage
  - market-microstructure
status: research-only
confidence: high
source_as_of: 2024-06
sources:
  - https://arxiv.org/abs/2208.06046
  - https://doi.org/10.1145/3658644.3670387
  - https://doi.org/10.1137/23M1577789
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AMM Loss-Versus-Rebalancing (LVR) and Toxic Arbitrage

## Provenance

Primary source: Jason Milionis, Ciamac C. Moallemi, Tim Roughgarden, and Anthony Lee Zhang, “Automated Market Making and Loss-Versus-Rebalancing,” *arXiv preprint arXiv:2208.06046* (2022 / revised 2024), ACM Conference on Computer and Communications Security (CCS) / *SIAM Journal on Financial Mathematics*. DOI: https://doi.org/10.1145/3658644.3670387.

Foundational and related literature:
- Hayden Adams, Noah Zinsmeister, and Dan Robinson, “Uniswap v2 Core,” Whitepaper (2020). URL: https://uniswap.org/whitepaper.pdf.
- Hayden Adams, Noah Zinsmeister, Moody Salem, River Keefer, and Dan Robinson, “Uniswap v3 Core,” Whitepaper (2021). URL: https://uniswap.org/whitepaper-v3.pdf.
- Guillermo Angeris and Tarun Chitra, “Improved Price Oracles: Constant Function Market Makers,” *ACM Conference on Advances in Financial Technologies (AFT)* (2020). DOI: https://doi.org/10.1145/3419614.3423251.

The study establishes a theoretical framework for isolating and measuring the adverse selection cost incurred by liquidity providers in constant function automated market makers (CFMMs) due to stale price quoting relative to centralized exchanges.

## Economic mechanism

### Source-reported

Milionis et al. (2022) establish that automated market makers (like Uniswap, Curve, and Balancer) do not actively update prices as external fundamental valuations change; price updates on CFMMs occur solely when external traders execute swaps against the pool.

When the market price of an asset changes on an external, liquid reference market (such as Binance or Coinbase), the AMM pool's quote is momentarily stale. Arbitrageurs exploit this latency by submitting swaps that buy undervalued tokens or sell overvalued tokens before the AMM quote reflects the true market price. 

The authors define **Loss-Versus-Rebalancing (LVR)** as the difference between the return of an AMM liquidity provider position and a hypothetical rebalancing portfolio that dynamically matches the LP's asset weights without incurring adverse selection. They prove that:
1. LVR is a non-negative, monotonically increasing running cost driven by the asset's continuous volatility $\sigma$ and pool liquidity.
2. In the absence of transaction fees, LVR represents the exact economic rent extracted by latency arbitrageurs from passive LPs.
3. For an LP position to be profitable, fee revenue generated from uninformed retail order flow must exceed the cumulative LVR drag.

### Research interpretation

The hypothesized mechanism operates along two complementary alpha vectors:

1. **CEX-DEX Latency Arbitrage (Extracting LVR Alpha)**:
   - High-frequency arbitrageurs continuously compare the external liquid CEX price $P_t^{\text{CEX}}$ against the on-chain DEX pool price $P_t^{\text{DEX}}$.
   - Whenever $|P_t^{\text{CEX}} - P_t^{\text{DEX}}| / P_t^{\text{DEX}} > \gamma_{\text{fee}} + \text{GasCostRatio}$, the arbitrageur routes a targeted atomic swap (via private MEV builder bundles) to rebalance the AMM pool to the CEX price, instantaneously offloading the acquired inventory on the CEX to lock in a riskless spread.

2. **Volatility-Adaptive LP Quoting / Dynamic Fee Alpha (Mitigating LVR)**:
   - For market makers or dynamic-fee AMM protocols, expected instantaneous LVR drain scales quadratically with asset volatility:
     $$d\text{LVR}_t = \frac{1}{8} \sigma_t^2 S_t L_t dt$$
   - An LP or automated vault can maximize net returns by dynamically adjusting the pool fee $\gamma_t^*(\sigma_t)$ proportional to realized volatility $\sigma_t \sqrt{\Delta t}$, or by hedging the directional inventory delta on CEX perpetuals whenever realized volatility spikes.

## Signal

### Signal A: CEX-DEX Toxic Arbitrage Engine

1. **Mispricing Metric**:
   - Let $S_t$ be the real-time CEX mid-price.
   - Let $P_t(R_x, R_y)$ be the AMM marginal pool price with reserves $R_x, R_y$ and fee rate $\gamma$.
   - Effective swap price boundary for buying asset $X$: $P_t^{\text{buy}} = P_t / (1 - \gamma)$.
   - Effective swap price boundary for selling asset $X$: $P_t^{\text{sell}} = P_t \cdot (1 - \gamma)$.

2. **Arbitrage Execution Trigger**:
   - **Buy on DEX / Sell on CEX**: If $S_t > P_t / (1 - \gamma) \cdot (1 + \text{GasCostBuffer})$, submit flash swap to purchase $\Delta x$ from DEX pool until pool price reaches $S_t (1 - \gamma)$, simultaneous short fill on CEX.
   - **Sell on DEX / Buy on CEX**: If $S_t < P_t (1 - \gamma) \cdot (1 - \text{GasCostBuffer})$, submit flash swap to sell $\Delta x$ into DEX pool until pool price reaches $S_t / (1 - \gamma)$, simultaneous long fill on CEX.

3. **Optimal Arbitrage Swap Size ($\Delta x^*$ for Uniswap $x \cdot y = k$)**:
   $$\Delta x^* = \sqrt{\frac{k \cdot (1 - \gamma)}{S_t}} - \frac{x}{1 - \gamma}$$

### Signal B: Volatility-Conditioned Dynamic LP Fee Adaptation

1. Compute rolling realized volatility $\hat{\sigma}_t$ over high-frequency returns (e.g. 5-minute EWMA).
2. Set dynamic fee tier:
   $$\gamma_t^* = \max\left(\gamma_{\min}, c_{\text{opt}} \cdot \hat{\sigma}_t \sqrt{\Delta t_{\text{block}}}\right)$$
   where $c_{\text{opt}}$ balances retail volume elasticity against expected LVR losses.

3. **Specification status**: **fully specified** for closed-form LVR calculation and CEX-DEX mispricing threshold; **underspecified** regarding Ethereum block builder priority auctions / bribe bidding optimization.

## Required data

- High-frequency WebSocket order book stream from primary CEX venues (e.g. Binance BTC/USDT, ETH/USDT Level 2).
- On-chain DEX pool state (liquidity depth $L$, tick arrays for Uniswap v3, pool balances for Uniswap v2/Curve).
- Real-time mempool pending transactions and base fee / priority gas price oracles (EIP-1559).
- Block creation / slot timestamp synchronization metadata.

## Execution assumptions

- Atomic transaction execution: DEX leg submitted via private MEV relay (e.g. Flashbots Protect / Titan Builder / BeaverBuild) to prevent frontrunning and sandwiching.
- CEX leg executed via low-latency API taker order (IOC) with sub-10ms execution loop.
- Gas cost estimation: Includes base fee plus competitive builder bribe (often 80–90% of gross arbitrage margin in competitive block spaces).

## Evidence

### Source-reported

Milionis et al. (2022, 2024) document:
- Closed-form proof that cumulative LVR over $[0, T]$ equals $\int_0^T \frac{\sigma^2}{8} S_t L_t dt$ for constant-product AMMs.
- Empirical analysis across Uniswap v3 pools indicates that for major pairs (ETH/USDC, WBTC/USDC), cumulative LVR exceeds trading fee income during sustained high-volatility regimes.
- Arbitrageurs systematically extract predictable dollar flows from AMMs that match the theoretical LVR prediction with high statistical alignment ($R^2 > 0.85$ on daily aggregated flow data).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- MEV builder capture: In competitive public blockchains (Ethereum L1, Arbitrum, Solana), searcher competition pushes priority bribes to 85–95% of gross arbitrage profit, severely compressing net searcher margins.
- Reorg and block latency risk: If a block inclusion is delayed or uncle-banded, CEX inventory remains unhedged, exposing the arbitrageur to adverse price drift.

## Falsification plan

The strategy hypothesis should be considered falsified if:
1. In empirical CEX-DEX backtesting, total transaction costs (gas, priority bribes, CEX taker fees) exceed the gross extracted price divergence in $> 60\%$ of blocks.
2. For dynamic LP fee strategies, increasing fee $\gamma_t^*$ during high-volatility regimes causes total retail swap volume to drop to zero, reducing net fee collection below baseline static-fee pools.
3. Oracle-integrated DEX architectures (e.g. RFQ AMMs or pull-oracle pools) eliminate the CEX-DEX price gap, driving available LVR arbitrage flow to zero.

## Crypto portability

**Direct**: Exclusively native to decentralized cryptocurrency Automated Market Makers and cross-venue CEX-DEX trading infrastructure.

Portability adaptations:
- Applicable to Uniswap v2/v3/v4 on Ethereum, Arbitrum, Optimism, Base.
- Applicable to Solana AMMs (Raydium, Orca) using Jito MEV bundles.
- Applicable to cross-DEX arbitrage between concentrated liquidity pools.

## Limitations

- **not independently reproduced**: requires full blockchain mempool and tick-level CEX backtesting engine.
- **builder bribe compression**: searcher net alpha is heavily degraded by MEV auction dynamics.
- **infrastructure dependency**: requires co-located CEX infrastructure and private RPC node access.

## Implementation status

No implementation in PyBroker, NautilusTrader, or any internal research/backtesting pipeline has been performed.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material only. It does not represent a validated production strategy, an execution authorization, or approval for Paper, Testnet, or Live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

- `[[crypto-cex-dex-cross-venue-funding-spread-carry-2026-08-31]]`
- `[[crypto-multilevel-order-flow-imbalance-intraday-2026-08-31]]`
- `[[crypto-perpetual-no-arbitrage-deviation-2026-08-31]]`

## Sources

1. Jason Milionis, Ciamac C. Moallemi, Tim Roughgarden, and Anthony Lee Zhang, “Automated Market Making and Loss-Versus-Rebalancing,” *arXiv preprint arXiv:2208.06046* (2022). URL: https://arxiv.org/abs/2208.06046
2. Jason Milionis, Ciamac C. Moallemi, Tim Roughgarden, and Anthony Lee Zhang, “An Automated Market Maker with Loss-Versus-Rebalancing Minimization,” *ACM CCS* (2024). DOI: https://doi.org/10.1145/3658644.3670387
3. Hayden Adams, Noah Zinsmeister, Moody Salem, River Keefer, and Dan Robinson, “Uniswap v3 Core,” Whitepaper (2021). URL: https://uniswap.org/whitepaper-v3.pdf
