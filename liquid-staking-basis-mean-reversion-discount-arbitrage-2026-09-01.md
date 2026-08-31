---
schema: strategy-research-record-v1
title: Liquid Staking Derivative Basis Mean Reversion and Discount Arbitrage
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - liquid-staking
  - basis-arbitrage
  - relative-value
  - ethereum
  - defi
  - curve
status: research-only
confidence: high
source_as_of: 2023-05-31
sources:
  - https://doi.org/10.1002/fut.22556
  - https://ideas.repec.org/a/wly/jfutmk/v45y2025i2p91-117.html
  - https://www.econstor.eu/handle/10419/281487
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3984897
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Liquid Staking Derivative Basis Mean Reversion and Discount Arbitrage

## Provenance

Primary source:

- Stefan Scharnowski and Hossein Jahanshahloo. "The Economics of Liquid Staking Derivatives: Basis Determinants and Price Discovery." *Journal of Futures Markets*, Volume 45, Issue 2 (February 2025), pages 91–117. First published online November 2024.
- DOI: https://doi.org/10.1002/fut.22556
- RePEc/IDEAS bibliographic entry: `RePEc:wly:jfutmk:v:45:y:2025:i:2:p:91-117` (https://ideas.repec.org/a/wly/jfutmk/v45y2025i2p91-117.html)
- Working paper repository: EconStor research report 281487 (https://www.econstor.eu/handle/10419/281487) / SSRN Abstract ID: 3984897 (https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3984897)

The empirical core of the study examines transaction-level and liquidity data from the Curve Finance stETH/ETH liquidity pool (the primary secondary liquidity venue for Lido Staked Ether) between November 1, 2021, and May 31, 2023, augmented with Lido smart contract variable trackers, Ethereum Beacon Chain on-chain data, and centralized exchange spot markets.

The sample spans critical structural shifts in Ethereum's monetary and consensus architecture: the pre-Merge Beacon Chain phase, the collapse of Terra/Luna and subsequent Celsius/3AC insolvencies (May–June 2022), the Ethereum Proof-of-Stake Merge (September 2022), and the Shapella upgrade (April 2023) which activated on-chain validator withdrawal queues.

## Economic mechanism

### Source-reported

Liquid staking tokens (LSTs), such as Lido stETH, are synthetic derivatives representing claims on underlying staked crypto assets (ETH) plus accrued Proof-of-Stake consensus and execution rewards. By transforming illiquid staked assets into freely transferable ERC-20 tokens, liquid staking allows market participants to earn staking yields while maintaining collateral utility across decentralized finance (DeFi).

Scharnowski and Jahanshahloo (2025) provide an empirical and theoretical analysis of the "liquid staking basis"—defined as the relative price difference between the liquid staking token and its underlying asset ($P_{\text{stETH}} - P_{\text{ETH}}$ or $\ln(P_{\text{stETH}}) - \ln(P_{\text{ETH}})$). The source identifies four primary economic determinants driving time-variation in the basis:

1. **Staking Rewards:** The basis reflects the expected yield differential between liquid staking protocols and direct validator staking. When protocol yields drop relative to direct staking or benchmark rates, the basis discount widens.
2. **Concentration and Protocol Risks:** Node operator concentration, smart contract vulnerability exposure, and protocol governance dominance introduce credit/operational risk premia. As Lido's share of total staked ETH grew, market participants priced in concentration and tail-slashing risks.
3. **Limits to Arbitrage and Secondary Liquidity:** Arbitrage between secondary market prices and primary redemption value is constrained by unbonding delays, withdrawal queue throughput, and secondary liquidity depth. In periods of heavy one-way selling (e.g., institutional liquidations), automated market maker (AMM) reserves become severely imbalanced, forcing the basis into substantial discount.
4. **Behavioral and Market Stress Factors:** Market-wide volatility (realized ETH volatility) and risk-off sentiment significantly widen the basis discount, whereas positive investor attention and sentiment narrow the spread.

Furthermore, the study finds that LST secondary markets (such as Curve pools) actively contribute to price discovery of the underlying cryptocurrency rather than merely functioning as passive price followers.

### Research interpretation

The liquid staking basis represents a structural relative-value and discount-arbitrage opportunity with asymmetric convergence characteristics:

- **Structural Upper Bound:** In the absence of protocol fee rebates, the spot LST price rarely trades at a sustained premium above par ($P_{\text{LST}} / P_{\text{ETH}} \le 1.0$) because any market participant can deposit 1 ETH to mint 1 stETH instantly via the protocol smart contract.
- **Dynamic Lower Bound:** The lower bound (discount) is governed by liquidity constraints and limits to arbitrage. During liquidity shocks or forced deleveraging, secondary AMM pools absorb massive sell orders, driving the price of stETH down relative to ETH.
- **Convergence Pathways:**
  1. *Secondary Rebalancing:* As market distress subsides, natural demand for staking yield and arbitrage capital absorb the discount in AMM/CEX pools, driving the price back toward parity.
  2. *Primary Redemption (Post-Shapella):* Arbitrageurs can buy discounted stETH in the secondary market and submit it to the protocol's withdrawal queue (`WithdrawalQueueERC721.sol`) to redeem 1:1 for native ETH, locking in an annualized return equal to the discount divided by the unbonding latency ($T_{\text{queue}}$), plus staking yield accrued during the queue.

A disciplined relative-value strategy captures this basis discount through either delta-hedged arbitrage (buying discounted LST, shorting ETH perpetual futures / borrowing ETH) or yield-enhanced spot accumulation (substituting native ETH holding with discounted LST).

## Signal

The strategy operates as a multi-condition relative-value and discount-arbitrage engine:

### 1. State Variables & Metrics
- **Spot Liquid Staking Basis:**
  $$\text{Basis}_t = \frac{P^{\text{stETH}}_t}{P^{\text{ETH}}_t} - 1$$
- **Rolling Basis Z-Score:**
  $$Z_{\text{Basis}, t} = \frac{\text{Basis}_t - \mu_{\text{Basis}}(w)}{\sigma_{\text{Basis}}(w)}$$
  where $w$ is a rolling lookback window (e.g., 30 days).
- **AMM Pool Reserve Imbalance:**
  $$\text{Imbalance}_t = \frac{\text{Reserve}^{\text{stETH}}_t}{\text{Reserve}^{\text{stETH}}_t + \text{Reserve}^{\text{ETH}}_t}$$
  (In a balanced Curve pool, $\text{Imbalance} \approx 0.50$; during stress events, stETH reserve share expands toward $0.70 - 0.85$).
- **Withdrawal Queue Latency Proxy ($T_{\text{queue}}$):** Total ETH awaiting exit on the Beacon Chain divided by the daily validator churn limit.

### 2. Entry Logic
- **Discount Arbitrage Entry:** Triggered when:
  1. $\text{Basis}_t \le \text{Threshold}_{\text{entry}}$ (e.g., $\text{Basis}_t \le -1.50\%$ or $Z_{\text{Basis}, t} \le -2.0$);
  2. AMM pool imbalance $\text{Imbalance}_t \ge 0.65$;
  3. No unmitigated smart-contract exploit or consensus-level slashing event ($\ge 1\%$ validator slashing) detected via on-chain event monitors.
- **Portfolio Execution:**
  - *Delta-Neutral Arbitrage:* Buy stETH on DEX/CEX at market price $P^{\text{stETH}}_t$; open an equal notional short position in ETH perpetual futures (or borrow spot ETH to sell).
  - *Yield-Enhanced Spot:* Swap benchmark ETH spot holdings into stETH at discounted rate.

### 3. Exit Logic
- **Market Convergence Exit:** Close positions when $\text{Basis}_t \ge -0.15\%$ (spread returns to normal band).
- **Primary Redemption Exit (Alternative Route):** If secondary market discount persists past $T_{\text{queue}} + \text{buffer}$, submit stETH to Lido Withdrawal Queue, burn stETH, receive native ETH 1:1, and close the perpetual short hedge upon receipt of ETH.
- **Emergency Stop-Loss:** If catastrophic protocol-level vulnerability, regulatory blacklisting, or smart contract freeze occurs, immediately exit all long LST exposure at prevailing market liquidity.

## Required data

- **High-Frequency DEX Pool State:**
  - Curve stETH/ETH pool (`0xDC24316b9AE028F1497c275EB9192a3Ea0f67022`): reserves, virtual price, swap events, and A-parameter.
  - Uniswap v3 stETH/ETH and wstETH/ETH pools: tick liquidity distributions and fee tier volumes.
- **Spot & Derivative Market Data:**
  - ETH/USD, ETH/USDT spot trade and order book tick data across major CEXs (Binance, Coinbase, OKX, Bybit).
  - ETH perpetual futures: mark price, index price, funding rate (8h settlement), and open interest.
  - Spot margin ETH borrow rates (Aave v3, Compound v3, Binance margin).
- **On-Chain Protocol & Consensus Data:**
  - Lido smart contract state: `Lido.sol`, `StETH.sol`, `WithdrawalQueueERC721.sol`.
  - Consensus layer metrics: Beacon Chain validator count, total staked ETH, exit queue depth, entry queue depth, effective balance, slashing logs.
  - Node operator distribution and validator concentration indices.
- **Macro / Market Factors:**
  - Realized ETH return volatility (trailing 7-day and 30-day).
  - Market sentiment / liquidity proxies.

## Execution assumptions

- **DEX Slippage & Price Impact:** Non-linear execution cost modeled against the Curve StableSwap invariant ($A = 50$). Large orders during severe pool imbalance incur significant marginal slippage.
- **On-Chain Gas Costs:** Ethereum Layer-1 transaction fees for token approvals, Curve swap executions, withdrawal queue requests (`requestWithdrawals`), and withdrawal claim executions (`claimWithdrawals`).
- **Perpetual Funding Rate Drag:** Delta-hedged short positions pay continuous funding if funding rates are positive ($\text{Funding} > 0$), which offsets basis discount gains; in negative funding regimes, short positions earn carry.
- **Withdrawal Queue Latency:** Post-Shapella unbonding is not instantaneous; queue duration depends on the rate of validator exits (governed by the churn limit: 8–12 validators per epoch). Typical redemption delay ranges from 1 to 5 days under normal conditions, but can extend to multiple weeks during mass validator exit waves.
- **Borrowing / Margin Constraints:** Spot margin borrowing requires over-collateralization and carries variable borrow rate spikes during high-volatility events.

## Evidence

### Source-reported

Stefan Scharnowski and Hossein Jahanshahloo (2025) report the following empirical findings based on their analysis of the Curve stETH/ETH liquidity pool from November 1, 2021, to May 31, 2023:

- **Time-Varying Basis Dynamics:** The liquid staking basis deviates significantly from zero over time, exhibiting pronounced discount spikes during market-wide liquidity crunches. During the May–June 2022 crisis (Terra/Luna collapse, Celsius and Three Arrows Capital liquidations), the stETH discount widened to multi-percentage-point levels (reaching discounts in excess of 5–7% on secondary venues).
- **Regression Analysis on Determinants:**
  - Staking rewards: Low protocol staking rewards relative to direct staking significantly widen the basis discount.
  - Risk awareness: Higher protocol concentration risk and elevated underlying ETH return volatility are statistically significantly associated with a wider basis discount.
  - Limits to arbitrage: Reductions in secondary market liquidity depth (Curve pool reserves) strongly increase the magnitude of the discount.
  - Sentiment: Positive sentiment and heightened investor attention significantly reduce the basis discount.
- **Price Discovery Contribution:** Vector Error Correction Models (VECM) and Hasbrouck Information Share / Gonzalo-Granger Component Share analyses demonstrate that LST prices in decentralized pools make a statistically meaningful contribution to the price discovery process of underlying ETH.

### Independently reproduced

Not independently reproduced in the user's research stack.

### Negative evidence

- **Structural Illiquidity Pre-Shapella:** Prior to the Shapella upgrade (April 2023), stETH could not be redeemed for native ETH on-chain. During the June 2022 liquidity crisis, the discount persisted for months without an arbitrage-driven primary redemption mechanism, demonstrating that secondary AMM liquidity alone is insufficient to prevent severe de-pegging under structural limits to arbitrage.
- **Perpetual Funding Cost Drag:** In strong bull markets with persistent positive perpetual funding rates ($> 20-30\%\text{ APR}$), holding a short perpetual hedge over a 15–30 day basis convergence horizon can exceed the gross basis discount captured.
- **Leverage Cascade Risks:** Recursive leveraged staking on lending protocols (e.g., depositing stETH as collateral to borrow ETH and buy more stETH) creates endogenous liquidation spirals where automated liquidations dump stETH into AMMs, drastically widening the discount beyond theoretical equilibrium.

## Falsification plan

The liquid staking basis discount arbitrage hypothesis should be rejected or materially modified if an independent historical and out-of-sample backtest (spanning June 2023 through 2026) demonstrates any of the following:

1. **Net Profitability Failure:** Net returns from basis discount arbitrage are non-positive after subtracting on-chain L1 gas fees, Curve/DEX slippage, CEX maker/taker fees, and perpetual funding costs.
2. **Post-Shapella Basis Compression:** Following the implementation of on-chain withdrawals (Shapella), the secondary basis discount remains permanently compressed within transaction cost bounds (e.g., $|\text{Basis}| < 0.20\%$), eliminating harvestable mispricing opportunities.
3. **Queue Congestion Risk:** During severe stress events, withdrawal queue duration expands faster than the basis discount compensates, yielding an annualized return inferior to cash/risk-free benchmarks.
4. **Funding Asymmetry:** The cost of carrying delta-hedges via perpetual futures systematically dominates the basis convergence profit.
5. **Tail Slashing & Smart Contract Exposure:** The residual smart contract and slashing tail risks cannot be compensated by the realized basis spread over a multi-year sample.

## Crypto portability

**Direct**, as the strategy mechanism and source empirical data are entirely native to the Ethereum Proof-of-Stake blockchain, liquid staking smart contracts, and decentralized exchange liquidity pools.

Portability considerations across LST ecosystems:
- **Wrapped vs. Rebalancing Tokens:** Rebalancing tokens (stETH) adjust balances daily via rebasing, requiring specific accounting handlers in backtesting engines; wrapped non-rebasing tokens (wstETH) accrue value through an increasing exchange rate ($P^{\text{wstETH}} = P^{\text{stETH}} \times \text{ShareRatio}$).
- **Cross-Chain LSTs:** The same economic mechanism applies to other PoS chains with liquid staking (e.g., JitoSOL / mSOL on Solana, bETH / stATOM on Cosmos), though withdrawal queue mechanics, unbonding periods (e.g., Solana's 2–3 day epoch cycle vs Cosmos 21-day unbonding), and AMM invariants differ materially.

## Limitations

- **Not independently reproduced** in this research stack.
- **Protocol & Smart Contract Risk:** Delta-neutral hedging protects against ETH market price movement but does not protect against smart contract hacks, governance attacks, or slashing penalties within the liquid staking protocol.
- **Regime Shift Post-Shapella:** The primary empirical sample (Nov 2021–May 2023) encompasses both pre-Merge and pre-Shapella regimes. The activation of on-chain withdrawals altered the duration and amplitude of basis discounts by providing a hard redemption ceiling.
- **Capital Intensity:** Delta-neutral arbitrage requires capital allocation across both on-chain DeFi (long LST) and centralized/decentralized derivatives exchanges (short hedge margin), creating potential liquidation risks on the short leg during sharp upward price spikes.

## Implementation status

No implementation in PyBroker, NautilusTrader, the strategy registry, any data pipeline, Paper, Testnet, Demo, or Live trading has been created or modified.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material in the Alpha Strategy Pool only. It is not evidence of validated alpha, not an implementation task, and not approval for Paper, Testnet, Demo, or Live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

- `[[crypto-cross-sectional-locked-supply-staking-conviction-2026-09-01]]`
- `[[crypto-cex-dex-cross-venue-funding-spread-carry-2026-08-31]]`
- `[[crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31]]`
- `[[funding-aware-market-making-perpetual-dex-2026-08-31]]`
- `[[crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31]]`

## Sources

1. Stefan Scharnowski and Hossein Jahanshahloo, "The Economics of Liquid Staking Derivatives: Basis Determinants and Price Discovery," *Journal of Futures Markets*, Volume 45, Issue 2, February 2025, pages 91–117. DOI: https://doi.org/10.1002/fut.22556
2. RePEc/IDEAS bibliographic entry for Scharnowski and Jahanshahloo (2025): https://ideas.repec.org/a/wly/jfutmk/v45y2025i2p91-117.html
3. EconStor Open Access Repository, Working Paper No. 281487: https://www.econstor.eu/handle/10419/281487
4. SSRN Scholarly Paper Record (Abstract ID 3984897): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3984897
