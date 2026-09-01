---
schema: strategy-research-record-v1
title: Dynamic-Weight AMM Continuous Dutch Reverse Auction Rebalancing and Incidental Multi-Hop Routing Arbitrage
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - defi
  - amm
  - tfmm
  - g3m
  - lvr
  - rvr
  - dutch-reverse-auction
  - rebalancing
  - mev
  - base-l2
  - arbitrage
status: research-only
confidence: high
source_as_of: 2026-02
sources:
  - "Willetts, M., & Harrington, C. (2026). Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs. arXiv preprint arXiv:2602.22069v1 [q-fin.TR / q-fin.PM]. https://arxiv.org/abs/2602.22069"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Dynamic-Weight AMM Continuous Dutch Reverse Auction Rebalancing and Incidental Multi-Hop Routing Arbitrage

## Provenance

- **Primary Source:** Matthew Willetts and Christian Harrington, *"Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs"*, arXiv preprint `arXiv:2602.22069v1 [q-fin.TR / q-fin.PM]`, published February 2026. URL: https://arxiv.org/abs/2602.22069, DOI: https://doi.org/10.48550/arXiv.2602.22069.
- **Foundational & Contextual Literature:**
  - Willetts, M., & Harrington, C. (2024a). "Rebalancing-versus-Rebalancing: Improving the fidelity of loss-versus-rebalancing." arXiv preprint `arXiv:2410.23404`.
  - Willetts, M., & Harrington, C. (2024b). "Closed-form solutions for generic N-token AMM arbitrage." arXiv preprint `arXiv:2402.06731`.
  - Willetts, M., & Harrington, C. (2024c). "Optimal rebalancing in dynamic AMMs." arXiv preprint `arXiv:2403.18737`.
  - Milionis, J., Moallemi, C. C., Roughgarden, T., & Zhang, A. L. (2022). "Automated Market Making and Loss-Versus-Rebalancing." arXiv preprint `arXiv:2208.06046`.
  - Milionis, J., Moallemi, C. C., & Roughgarden, T. (2023). "Automated Market Making and Arbitrage Profits in the Presence of Fees." arXiv preprint `arXiv:2305.14604`.
  - Daian, P., Goldfeder, S., Kell, T., Li, Y., Zhao, X., Bentov, I., Breidenbach, L., & Juels, A. (2020). "Flash Boys 2.0: Frontrunning in Decentralized Exchanges, Miner Extractable Value, and Consensus Instability." *IEEE Symposium on Security and Privacy (SP)*, pp. 910–927.
- **Empirical Dataset:** Per-block on-chain execution logs, pool reserves, target weights, token prices, and gas fees from two live QuantAMM protocol pools:
  1. *Safe Haven Pool* (Ethereum mainnet, 3/4-token basket including PAXG, WBTC, WETH, USDC), observed across two 2-hour rebalancing windows in July 2025 (606 blocks) and January 2026 (78 trades);
  2. *Base Macro Pool* (Base Layer-2 network), observed across May 2025 – January 2026, with detailed per-block trade analysis during January 2026 (202 balance changes, 225 transactions).
- **Public-Use Status:** Open-access academic publication / arXiv preprint distributed under the arXiv perpetual non-exclusive license.

## Economic mechanism

### Source-reported

Conventional portfolio management rebalances asset allocations via active taker orders on centralized order books (CEX), incurring direct taker commissions, bid-ask spread crossing costs, and market impact. In decentralized finance, Temporal Function Market Makers (TFMM) operate as Geometric Mean Market Maker (G3M) pools where asset target weights $\mathbf{w}(t) = \{w_i(t)\}_{i=1}^N$ ($\sum w_i = 1$) continuously update over time to track an algorithmic asset allocation strategy (e.g., trend following, momentum, risk parity, or macroeconomic weighting):

$$\prod_{i=1}^N R_i^{w_i(t)} = k(t)$$

When target weights shift while token reserves $\mathbf{R} = \{R_i\}$ remain constant, the pool's internal quoted prices drift away from external market consensus prices $p_i$, creating an allocation drift:

$$\text{Drift}(t) = \sum_{i=1}^N |\theta_i(t) - w_i(t)|, \quad \text{where } \theta_i(t) = \frac{R_i p_i}{\sum_j R_j p_j}$$

This allocation drift manifests as a sequence of implicit, continuous **Dutch reverse auctions**:
1. After each rebalance trade, the pool is near market equilibrium and the available arbitrage extraction is zero.
2. As target weights linearly interpolate block-by-block, the implied price discrepancy grows.
3. The first external arbitrageur whose execution cost (gas, builder tip, swap fees, hedging friction) falls below the accumulated surplus executes a swap against the pool, snapping reserves back toward target weights.
4. Continuous weight interpolation over $N$ discrete block steps reduces the total theoretical arbitrage extraction cost from $\mathcal{O}((\Delta w)^2)$ to $\mathcal{O}((\Delta w)^2 / N)$, asymptotically approaching zero in continuous time ($N \to \infty$).

Furthermore, in mature Layer-2 DEX ecosystems (Base), dynamic-weight pools function as intermediate hops in automated multi-venue routing paths (Uniswap v2/v3/v4, KyberSwap). Rebalancing is executed *incidentally* at zero or negative net cost to the pool, where arbitrageurs pay pool swap fees as part of a wider multi-hop trade.

### Research interpretation

The alpha and operational execution thesis comprises two complementary opportunities:

1. **TFMM Arbitrageur Extraction Strategy (MEV Searcher Alpha):**
   - Monitor on-chain TFMM pool state updates and target weight interpolation trajectories.
   - Size arbitrage trades conservatively to 55–70% of the theoretical unconstrained optimum: because the G3M arbitrage profit curve is strictly concave and flat near its maximum, undersizing captures 85–98% of available extractable surplus while minimizing capital commitment and inventory risk.
   - Execute multi-hop atomic routing bundles that amortize fixed gas/builder tip overhead across multiple venue discrepancies.

2. **Systematic On-Chain Portfolio Rebalancing Strategy (Asset Management Alpha):**
   - Replace active CEX rebalancing with decentralized dynamic-weight G3M pools using continuous spline/linear weight interpolation on high-throughput Layer-2 chains.
   - Harness competitive MEV searcher auctions and incidental multi-hop routing to achieve negative effective execution costs, outperforming both frictionless rebalancing baselines (LVR) and realistic CEX execution models (RVR).

## Signal

The normalized quantitative rules for the dual-sided execution strategy operate as follows:

### 1. External Arbitrageur Trigger & Sizing Rule

1. **State Evaluation:**
   - At block $t$, read token reserves $\mathbf{R}_t = (R_1, \dots, R_N)$, dynamic weights $\mathbf{w}_t = (w_1, \dots, w_N)$, pool swap fee $\gamma = 1 - f$ (e.g., $\gamma = 0.997$ for a 30 bps pool), and external market reference prices $\mathbf{p}_t = (p_1, \dots, p_N)$.
   - Compute pool marginal exchange rate between token $i$ and numeraire $j$:
     $$m_{u, ij}(t) = \frac{w_i(t) R_j(t)}{w_j(t) R_i(t)}$$
   - Identify the no-arbitrage band $[ \gamma \cdot p_i / p_j, \gamma^{-1} \cdot p_i / p_j ]$.

2. **Profitability Threshold Check:**
   - Calculate theoretical gross arbitrage extraction $\Pi^*(t)$ using the closed-form $N$-token G3M solution (Willetts & Harrington, 2024b).
   - Estimate total transaction cost for block $b$:
     $$C_b = G \cdot \text{BaseFee}_b \cdot p_{\text{ETH}} + \text{PriorityFee} + \text{BuilderTip}$$
     where median gas usage $G \approx 450{,}000$ units.
   - Fire entry signal if:
     $$\Pi^*(t) > \mu \cdot C_b, \quad \text{with markup } \mu \in [1.10, 1.50]$$

3. **Trade Sizing & Execution:**
   - Compute optimal input quantity $\Delta R_i^*$.
   - Execute scaled order size:
     $$\Delta R_i^{\text{exec}} = \alpha \cdot \Delta R_i^*, \quad \text{with } \alpha \in [0.55, 0.70]$$
   - Route atomic swap via MEV private builder bundle (e.g., Flashbots / MEV-Boost) back to external liquidity venue.

### 2. TFMM Dynamic Weight Portfolio Interpolation Rule

1. **Strategy Weight Update:**
   - At periodic strategy rebalancing intervals $T_{\text{rebal}}$ (e.g., daily or weekly), evaluate the quantitative factor model to determine new target weight vector $\mathbf{w}^*$.
2. **Discrete Block Interpolation:**
   - For an execution horizon of $K$ blocks ($K = \Delta T / \tau_{\text{block}}$), update the active block weight linearly:
     $$\mathbf{w}(t_k) = \mathbf{w}(t_0) + \frac{k}{K} (\mathbf{w}^* - \mathbf{w}(t_0)), \quad k = 1, \dots, K$$
   - Prevent discrete jumps ($\Delta w > 0.01$ per block) to preserve first-order pool value invariance ($V' = V + \mathcal{O}((\delta w)^2)$).

## Required data

- **Instruments & Venues:** Decentralized dynamic-weight G3M pools (QuantAMM / Balancer v3 vaults) on Ethereum Mainnet and Base Layer-2; reference CEX/DEX spot pools (Uniswap v2/v3/v4, Curve, Binance) for pricing benchmarks.
- **Fields:** Per-block token reserves ($R_i$), dynamic weights ($w_i$), pool swap fee rate ($f$), transaction gas price ($g_b$, base fee, priority fee, builder tip), swap input/output amounts, token reference spot prices ($p_i$).
- **Timeframe & Alignment:** Per-block on-chain execution logs (12-second slots on Ethereum mainnet; 2-second / sub-second blocks on Base L2).
- **Point-in-Time Integrity:** Strict block-by-block chronological reconstruction; zero look-ahead in evaluating target weight interpolation schedules.

## Execution assumptions

- **Order Types & Routing:** Atomic MEV bundle execution (private mempool transactions with direct builder payment) for external arbitrageurs; passive invariant liquidity provision for the TFMM pool.
- **Latency:** Execution latency is bounded by single-block inclusion (1 block delay from weight state change to arbitrage capture).
- **Transaction Costs & Fees:** Pool swap fee $\gamma = 0.997$ (30 bps); Balancer v3 protocol vault fee (50% fee split); gas consumption modeled at median $450{,}000$ gas units per multi-hop arbitrage transaction.
- **Fill Model:** Deterministic on-chain smart contract execution; reverts on negative net profit or slippage breach.

## Evidence

### Source-reported

Willetts & Harrington (2026) report empirical findings across two live QuantAMM pools observed six months apart (July 2025 vs. January 2026):

1. **Ethereum Mainnet (Safe Haven Pool, 3/4-token):**
   - **Auction Compression:** In July 2025 (2-hour window, 606 blocks), 20 arbitrage trades occurred (~1 trade every 6 minutes / 30 blocks); allocation drift reached 0.50–0.65% before resetting. Arbitrageurs extracted $51.55 out of $58.19 theoretical maximum (88.6% efficiency ratio).
   - **Market Maturation (January 2026):** In the same 2-hour window six months later, trade frequency rose to 78 trades (~1 trade every 90 seconds); allocation drift was compressed to $\le 0.40\%$. Mean per-trade extraction fell by 89% from $2.58 to $0.28, and total empirical extraction dropped from $51.55 to $22.00 despite nearly $4\times$ more trades.
   - **Cost Structure Shift:** All-in transaction cost fell from $1.08 to $0.20 per trade (assisted by the Ethereum Fusaka upgrade in Dec 2025); 24% of trades utilized complex MEV bundles with $\ge 4$ legs, and Uniswap v4 represented 37% of swap routing events.
   - **Concave Profit Curve Validation:** Arbitrageurs empirically under-sized trades to 54–71% of optimal size while capturing 81–99% of total available profit.

2. **Base Layer-2 (Base Macro Pool):**
   - **Incidental Routing Regime:** In January 2026 (2-hour window), 202 balance changes occurred across 225 transactions. Mean per-trade extraction was $0.0004 (median $< \$0.001$), with 98% of trades extracting $< \$0.01$. Many trades had negative net extraction, effectively subsidizing the pool.
   - **Multi-Hop Structure:** Transactions averaged 7 swaps across UniV2, UniV3, and UniV4. Arbitrageurs routed through the QuantAMM pool at fair value to complete broader ecosystem loops.
   - **Long-Term Performance vs. Baselines:** From May/August 2025 to January 2026, the Base Macro pool outperformed the frictionless LVR benchmark (perfect zero-cost CEX rebalancing) by **+27 percentage points** and outperformed the realistic CEX rebalancing benchmark (RVR, incorporating spreads and fees) by **+43 percentage points**.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **No Retail Flow at Low TVL:** In both empirical test windows, 0% of transaction volume came from organic retail traders; all swaps originated from MEV searcher bots, meaning the pool earned no non-arbitrage fee subsidies.
- **L1 Gas Threshold Constraint:** On Ethereum Mainnet, high gas costs create a wider no-arbitrage band during network congestion, forcing the pool to accumulate larger allocation drift before triggering an auction clearing.
- **Searcher Consolidation Risk:** On Base, unique active arbitrageurs consolidated from 65 bots in July 2025 to 4 dominant bots in January 2026. While empirical extraction remained near zero, extreme searcher centralization poses cartelization risks if bots collude to widen the strike threshold.

## Falsification plan

The hypothesis that dynamic-weight AMM rebalancing achieves superior execution efficiency and exploitable searcher alpha will be falsified if:
1. **Searcher Alpha Degradation:** Live execution of the 60% undersized G3M arbitrage rule on mainnet yields an annualized net Sharpe ratio $< 1.0$ after deducting gas and builder tips across a 6-month forward evaluation.
2. **LVR Outperformance Reversal:** Over a 12-month rolling evaluation across diverse market regimes (including prolonged bear markets and low-volatility regimes), the net return of the TFMM pool falls below the standard RVR benchmark.
3. **Auction Stalling:** In periods of extreme L1 gas spikes ($> 150\text{ gwei}$), allocation drift exceeds $2.5\%$ for $> 30\text{ consecutive minutes}$ without triggering an arbitrage clearing, causing intolerable portfolio tracking error.
4. **Placebo Invariant Test:** Replacing continuous weight interpolation with discrete step rebalances ($\Delta w$ executed in a single block) produces identical rebalancing costs, disproving the $\mathcal{O}((\Delta w)^2 / N)$ cost-reduction mechanism.

## Crypto portability

**Direct**: The empirical research, mathematical derivations, and protocol mechanics are designed specifically for EVM-based smart contracts, decentralized exchanges (G3M / Balancer v3 / Uniswap), and on-chain MEV searcher ecosystems.

Portability considerations:
- Direct applicability to Layer-2 networks (Base, Arbitrum, Optimism) where sub-cent transaction costs maximize auction compression and incidental routing efficiency.
- Rebalancing execution model directly ports to any on-chain tokenized fund, structured product, or automated ETF vault.

## Limitations

- **not independently reproduced**;
- **TVL scale dependency:** empirical data covers early-stage TVL pools; higher TVL pools may attract different price impact dynamics and noise-trader ratios;
- **chain infrastructure dependency:** performance on Layer-2 (no PBS, sequencer ordering) differs fundamentally from Ethereum Mainnet (MEV-Boost PBS auction);
- **strategy-specific market drift:** outperformance vs. LVR incorporates the directional returns of the underlying asset allocation strategy alongside execution efficiency.

## Implementation status

not-implemented

No implementation in PyBroker, NautilusTrader, or internal live trading pipelines has been completed.

## Adoption boundary

research-only

This record is research material only. It does not constitute investment advice, a validated trading strategy, or authorization for Paper, Testnet, or Live execution.

## Related Wiki records

- [[quant/crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31]] — loss-versus-rebalancing (LVR) theoretical foundation.
- [[quant/crypto-priority-gas-auctions-pga-dex-latency-arbitrage-2026-09-01]] — on-chain DEX arbitrage and MEV searcher mechanics.
- [[quant/crypto-uniswap-v3-just-in-time-jit-liquidity-provision-price-impact-2026-09-01]] — high-frequency liquidity provision and MEV routing.

## Sources

1. Willetts, M., & Harrington, C. (2026). "Pools as Portfolios: Observed arbitrage efficiency & LVR analysis of dynamic weight AMMs." *arXiv preprint arXiv:2602.22069v1 [q-fin.TR / q-fin.PM]*, published February 2026. URL: https://arxiv.org/abs/2602.22069. DOI: https://doi.org/10.48550/arXiv.2602.22069.
2. Willetts, M., & Harrington, C. (2024a). "Rebalancing-versus-Rebalancing: Improving the fidelity of loss-versus-rebalancing." *arXiv preprint arXiv:2410.23404*. URL: https://arxiv.org/abs/2410.23404.
3. Willetts, M., & Harrington, C. (2024b). "Closed-form solutions for generic N-token AMM arbitrage." *arXiv preprint arXiv:2402.06731*. URL: https://arxiv.org/abs/2402.06731.
4. Willetts, M., & Harrington, C. (2024c). "Optimal rebalancing in dynamic AMMs." *arXiv preprint arXiv:2403.18737*. URL: https://arxiv.org/abs/2403.18737.
5. Milionis, J., Moallemi, C. C., Roughgarden, T., & Zhang, A. L. (2022). "Automated Market Making and Loss-Versus-Rebalancing." *arXiv preprint arXiv:2208.06046*. URL: https://arxiv.org/abs/2208.06046.
6. Milionis, J., Moallemi, C. C., & Roughgarden, T. (2023). "Automated Market Making and Arbitrage Profits in the Presence of Fees." *arXiv preprint arXiv:2305.14604*. URL: https://arxiv.org/abs/2305.14604.
7. Daian, P., Goldfeder, S., Kell, T., Li, Y., Zhao, X., Bentov, I., Breidenbach, L., & Juels, A. (2020). "Flash Boys 2.0: Frontrunning in Decentralized Exchanges, Miner Extractable Value, and Consensus Instability." *2020 IEEE Symposium on Security and Privacy (SP)*, pp. 910–927. DOI: https://doi.org/10.1109/SP40000.2020.00040.
