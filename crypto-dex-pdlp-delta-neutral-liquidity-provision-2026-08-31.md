---
schema: strategy-research-record-v1
title: Crypto DEX Perpetual Demand Lending Pools (PDLP) Delta-Neutral Liquidity Provision
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - dex
  - pdlp
  - delta-neutral
  - yield-harvesting
  - liquidity-provision
  - derivatives
status: research-only
confidence: medium
source_as_of: 2026-04
sources:
  - "Tarun Chitra, Theo Diamandis, Nathan Sheng, Luke Sterle, and Kamil Yusubov, 'Perpetual Demand Lending Pools', arXiv:2502.06028 (February 2025). https://arxiv.org/abs/2502.06028"
  - "Ruichao Jiang and Long Wen, 'Target Weight Mechanism doesn't make delta hedge easier', arXiv:2604.16467 (April 2026). https://arxiv.org/abs/2604.16467"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Jiang and Wen (2026, arXiv:2604.16467) contest Chitra et al. (2025), demonstrating that during high pool utilization, sudden trader liquidations, and rebalancing execution latency, the Target Weight Mechanism does not fully eliminate hedging drag, leading to non-trivial tracking variance and convexity risk."
---

# Crypto DEX Perpetual Demand Lending Pools (PDLP) Delta-Neutral Liquidity Provision

## Provenance

- **Foundational Protocol & Mechanism Theory:** Tarun Chitra, Theo Diamandis, Nathan Sheng, Luke Sterle, Kamil Yusubov, "Perpetual Demand Lending Pools", *arXiv preprint arXiv:2502.06028* (February 2025). [arXiv:2502.06028](https://arxiv.org/abs/2502.06028).
- **Critical Re-Evaluation & Contestation:** Ruichao Jiang and Long Wen, "Target Weight Mechanism doesn't make delta hedge easier", *arXiv preprint arXiv:2604.16467* (April 2026). [arXiv:2604.16467](https://arxiv.org/abs/2604.16467).
- **Target Protocols & Real-World Precedents:** Multi-asset liquidity pools underwriting decentralized perpetual futures, including Jupiter (JLP on Solana), GMX (GLP / GM pools on Arbitrum/Avalanche), and Hyperliquid (HLP on Hyperliquid L1).

## Economic mechanism

### Source-reported

Chitra et al. (2025) formalize the mechanics of Perpetual Demand Lending Pools (PDLPs). Unlike Constant Function Market Makers (CFMMs) that suffer from continuous Loss-Versus-Rebalancing (LVR) due to arbitrageurs exploiting stale pricing, PDLPs act as shared lending vaults where liquidity providers (LPs) deposit multi-asset baskets (e.g., SOL, ETH, BTC, USDC, USDT) to facilitate leveraged trader positions. LPs earn continuous borrow fees, trading fees, and net liquidation payouts.

To manage inventory imbalances, PDLP protocols enforce a "Target Weight Mechanism" (TWM) that dynamically adjusts deposit/withdrawal and swap fee schedules to incentivize arbitrageurs to restore asset proportions toward predefined target weights. Chitra et al. theoretically prove that LPs can maintain a delta-hedged portfolio by taking short positions in the underlying volatile assets on external venues, yielding an optimal risk-adjusted return stream dominated by fee capture rather than market beta.

### Research interpretation

This is a synthetic delta-neutral yield harvesting strategy operating across decentralized and centralized derivative venues:
1. **Asset Exposure Decomposition:** An LP token representing a share of a PDLP basket has a net dollar value and time-varying vector of asset deltas:
   $$\mathbf{\Delta}_t = [\delta_{1,t}, \delta_{2,t}, \dots, \delta_{N,t}]^T$$
   where $\delta_{i,t}$ reflects the physical quantity of asset $i$ held in the pool plus the net open interest of traders (unrealized PnL liability) in asset $i$.
2. **Dynamic Delta Hedging:** The researcher holds $Q_{\text{LP}}$ units of LP tokens on-chain and continuously opens short positions $\mathbf{H}_t = [h_{1,t}, h_{2,t}, \dots, h_{N,t}]^T$ on liquid external derivative venues (e.g. Binance/Bybit perps or Hyperliquid perps) such that:
   $$h_{i,t} = - Q_{\text{LP}} \cdot \delta_{i,t}$$
3. **Alpha / Net Yield Thesis:** The net excess return $\alpha_t$ earned by the LP-hedger is the cumulative pool fee revenue minus the sum of external funding rates, hedging transaction fees, slippage, and basis tracking variance:
   $$\alpha_t = \text{Yield}_{\text{PDLP}}(t) - \sum_{i=1}^N \left( \text{FundingCost}_i(t) + \text{RebalanceFee}_i(t) + \text{Slippage}_i(t) \right) - \epsilon_{\text{tracking}}(t)$$
4. **Contested Fragility:** As highlighted by Jiang & Wen (2026), when pool utilization approaches $100\%$ or during sharp multi-standard-deviation market crashes, trader skewness and on-chain oracle update latency can cause rapid shifts in pool deltas $\mathbf{\Delta}_t$, creating non-linear tracking slippage before external hedges can be readjusted.

## Signal

- **State Identification & Delta Extraction:**
  - Continuously query on-chain pool state at periodic time interval $\Delta \tau = 1\text{ hour}$ (or upon delta drift exceeding threshold $\theta_{\text{drift}} = 2.0\%$):
    - Physical reserve quantities $R_{i,t}$ of volatile assets $i \in \{1, \dots, N\}$.
    - Open trader short/long positions $OI_{i,t}^{\text{long}}, OI_{i,t}^{\text{short}}$.
    - Net delta per LP token:
      $$\delta_{i,t} = \frac{R_{i,t} - \left(OI_{i,t}^{\text{long}} - OI_{i,t}^{\text{short}}\right)}{\text{TotalSupply}_{\text{LP},t}}$$
- **Hedging Target Calculation:**
  - Desired external short hedge size for asset $i$:
    $$H_{i,t}^* = - Q_{\text{LP}} \cdot \delta_{i,t}$$
- **Rebalancing Trigger Condition:**
  - Calculate exposure deviation for each asset:
    $$\Delta H_{i,t} = |H_{i,t}^{\text{current}} - H_{i,t}^*|$$
  - Execute rebalance trade on external perpetual venue if:
    $$\frac{\Delta H_{i,t} \cdot P_{i,t}}{Q_{\text{LP}} \cdot \text{NAV}_{\text{LP},t}} > \theta_{\text{rebalance}} \quad (\text{default } \theta_{\text{rebalance}} = 1.5\%)$$
- **Yield / Spread Entry Filter:**
  - Only deploy capital when 7-day moving average PDLP fee yield exceeds external perpetual funding drag:
    $$\text{EMA}_{7\text{d}}(\text{APR}_{\text{PDLP}}) - \sum_{i=1}^N w_{i,t} \cdot \text{EMA}_{7\text{d}}(\text{FundingRate}_i) > \text{HurdleRate} \quad (\text{default } 8.0\% \text{ net APR})$$
- **Exit / De-risking Trigger:**
  - Exit LP position and unwind hedges if net spread turns negative for 72 consecutive hours or if pool utilization exceeds $95\%$ (heightened tail risk / illiquidity).
- **Specification Status:** Fully specified for baseline static and threshold-based rebalancing; underspecified for continuous HJB-optimal stochastic control hedging paths.

## Required data

- **On-Chain DEX Data:**
  - Smart contract state for target PDLP (e.g. JLP on Solana, HLP on Hyperliquid): token reserves, total pool supply, trader open interest per asset, accumulated borrow and trade fees.
  - Oracles: Pyth / Chainlink price feed timestamps and latency distributions.
- **External CEX/DEX Perpetual Data:**
  - Spot and perpetual futures OHLCV (1m/1h), order book depth (L2/L3), 8h funding rates, and historical borrow rates for hedged assets (BTC, ETH, SOL).
- **Timestamp Synchronization:**
  - On-chain block timestamps mapped precisely to UTC exchange millisecond timestamps.

## Execution assumptions

- **Execution Venue for Hedge:** Deep centralized liquidity (Binance, Bybit, OKX) or low-latency decentralized CLOB (Hyperliquid).
- **Order Types:** Maker post-only limit orders for rebalancing when drift is within $[1.5\%, 3.0\%]$; taker IOC orders if delta drift exceeds $3.0\%$ to avoid severe unhedged beta exposure.
- **Trading Fees:** Maker $-0.005\%$ to $+0.02\%$; Taker $0.04\%$ to $0.05\%$.
- **On-chain Gas & Swap Costs:** Solana gas negligible ($<\$0.01$); Arbitrum gas $\$0.20-\$1.50$ per transaction.
- **Liquidation Margin:** Maintain at least $3\times$ collateral cushion on external short perpetual accounts to eliminate margin liquidation risk during sharp upward market rallies.

## Evidence

### Source-reported

- Chitra et al. (2025) derive theoretical bounds proving that the Sharpe ratio of an optimal delta-hedged PDLP strategy is strictly greater than or equal to the unhedged LP Sharpe ratio under standard Brownian asset price dynamics.
- Source claims empirical performance of delta-hedged JLP/GLP strategies in 2024 generated annualized net yields of approximately $25\%–40\%$ with near-zero equity beta.
- Jiang and Wen (2026) show in simulation that under jump-diffusion processes with jump intensity $\lambda = 0.1$, the Target Weight Mechanism induces rebalancing lag, generating up to $4.8\%$ annualized tracking loss and occasional delta leakage.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Prolonged Negative Funding Regimes:** During intense bear markets or localized altcoin short squeezes, external perpetual funding rates can turn severely negative, forcing short hedgers to pay substantial funding fees that overwhelm PDLP fee yields.
- **Smart Contract & Depeg Vulnerabilities:** Pool holdings can be contaminated if an underlying collateral asset suffers a depeg or exploit (e.g. wrapped token depeg, oracle front-running), causing structural losses not compensable by external hedging.

## Falsification plan

1. **Net Spread Decay Test:** Compute the rolling 30-day realized net spread (LP yield minus funding and rebalancing costs) across historical 2022–2026 data. If the net spread after realistic fees and slippage is below the risk-free rate ($<\text{SOFR} + 2\%$) for $>40\%$ of rolling windows, the strategy fails.
2. **Stress-Period Delta Leakage:** Evaluate tracking PnL during major market drawdowns ($>20\%$ daily drops). If unhedged delta variance causes drawdowns exceeding $5.0\%$, the delta-neutrality assumption is falsified.
3. **Ablation on Rebalancing Frequency:** Vary rebalancing intervals from 10 minutes to 24 hours. If performance collapses due to fee friction at high frequency or delta drift at low frequency without a stable profitable sweet spot, reject operational feasibility.

## Crypto portability

**Direct**: PDLPs are native decentralized crypto primitives (GMX GLP/GM, Jupiter JLP, Hyperliquid HLP). The strategy is specifically designed for crypto spot-perp and DEX-CEX microstructure.

## Limitations

- **contested**: Divergent academic findings regarding delta-hedge tractability under high utilization (Chitra et al. vs. Jiang & Wen).
- **not independently reproduced**: Empirical backtest with synchronized tick-level on-chain state and CEX order book execution has not been executed internally.
- **underspecified**: Dynamic stochastic control rebalancing parameters require venue-specific tuning.
- **tail risk**: Smart contract risk, oracle delay, and DEX protocol insolvency risks cannot be hedged via vanilla derivatives.

## Implementation status

No internal implementation in PyBroker, NautilusTrader, or live execution engines has been performed.

`implementation_status: not-implemented`

## Adoption boundary

Research material only. Does not constitute trading advice, production validation, or authorization for Paper, Testnet, or Live deployment.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `[[crypto-cex-dex-cross-venue-funding-spread-carry-2026-08-31]]`
- `[[crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31]]`
- `[[crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31]]`

## Sources

1. Tarun Chitra, Theo Diamandis, Nathan Sheng, Luke Sterle, and Kamil Yusubov, "Perpetual Demand Lending Pools", *arXiv preprint arXiv:2502.06028* (February 2025). [https://arxiv.org/abs/2502.06028](https://arxiv.org/abs/2502.06028)
2. Ruichao Jiang and Long Wen, "Target Weight Mechanism doesn't make delta hedge easier", *arXiv preprint arXiv:2604.16467* (April 2026). [https://arxiv.org/abs/2604.16467](https://arxiv.org/abs/2604.16467)
