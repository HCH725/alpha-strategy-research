---
schema: strategy-research-record-v1
title: DEX Cyclic Arbitrage in Constant-Product Automated Market Makers
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - amm
  - arbitrage
  - cyclic-arbitrage
  - triangular-arbitrage
  - mev
  - constant-product
status: research-only
confidence: high
source_as_of: 2022-04
sources:
  - https://doi.org/10.1145/3487553.3524204
  - https://arxiv.org/abs/2105.02784
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# DEX Cyclic Arbitrage in Constant-Product Automated Market Makers

## Provenance

- **Primary peer-reviewed source:** Ye Wang, Yan Chen, Haotian Wu, Liyi Zhou, Shuiguang Deng, and Roger Wattenhofer, "Cyclic Arbitrage in Decentralized Exchanges", *Companion Proceedings of the Web Conference 2022 (WWW '22 Companion)*, April 2022, Pages 12–19. DOI: https://doi.org/10.1145/3487553.3524204.
- **Preprint / working version:** arXiv preprint arXiv:2105.02784 (May 2021). URL: https://arxiv.org/abs/2105.02784.
- **Sample period:** May 4, 2020 to April 10, 2021 (approx. 11 months on Ethereum mainnet).
- **Underlying AMM protocols studied:** Uniswap V2 and SushiSwap constant-product liquidity pools ($x \cdot y = k$).
- **Core dataset:** On-chain transaction logs and state transitions from Ethereum mainnet, analyzing 292,606 cyclic arbitrage transactions.

## Economic mechanism

### Source-reported

Wang et al. (2022) formulate cyclic arbitrage (also termed triangular or multi-hop closed-loop arbitrage) across decentralized exchanges running constant-product automated market makers (CFMMs/CPMMs).

In an ecosystem with multiple trading pairs and decentralized liquidity pools, trading activity in one pool can create transient relative price disparities across indirect cross-pair exchange routes. When a closed sequence of liquidity pools $P_1, P_2, \dots, P_n$ connects a cycle of tokens $T_0 \to T_1 \to T_2 \to \dots \to T_n = T_0$, an arbitrage opportunity exists if trading a positive input amount $a$ through the sequence of pools yields an output amount $R(a) > a + \text{GasCost}$.

The authors establish:
1. The mathematical condition for the existence of profitable cyclic arbitrage in constant-product pools with transaction fee factor $\gamma_i = 1 - f_i$ (where $f_i = 0.003$ for standard 0.3% pools). An arbitrage opportunity exists if and only if the product of marginal exchange rates around the cycle exceeds 1:
   $$\prod_{i=1}^n \left( \gamma_i \cdot \frac{y_i}{x_i} \right) > 1$$
   where $x_i$ and $y_i$ denote the input and output reserves of pool $i$ at the moment of trade.
2. The closed-form analytical solution for the optimal input amount $a^*$ that maximizes net arbitrage profit:
   $$\pi(a) = R(a) - a - \text{GasCost}$$
   Because $R(a)$ is strictly concave with diminishing marginal returns due to slippage/price impact, there exists a unique optimal input $a^*$ where marginal revenue equals marginal cost: $R'(a^*) = 1$.
3. Over 99.97% of real-world cyclic arbitrageurs implement their strategies via custom smart contracts, executing all swap legs atomically within a single transaction to eliminate directional inventory risk and partial-fill risk.

### Research interpretation

This is an atomic, pure cross-venue/cross-pair microstructure arbitrage strategy. Unlike directional momentum, statistical mean-reversion, or CEX-DEX arbitrage, cyclic DEX arbitrage entails zero structural holding period and zero unhedged delta exposure if executed atomically on-chain.

The economic rent arises from asynchronous liquidity demand across decentralized pools: large uninformed retail trades or single-pair liquidations push the marginal price of a token pool away from the implicit cross-rate defined by other pools. Arbitrageurs act as decentralized market stabilizers, restoring consistency across cross-pair AMM state vectors.

The key operational bottleneck is priority gas auction (PGA) / MEV bundle competition: when multiple searchers identify the same cyclic price discrepancy, miner/validator tips determine execution precedence.

## Signal

Normalized source-backed formulation:

1. **Cycle Discovery**:
   - Construct a directed token exchange graph $G = (V, E)$, where vertices $V$ represent tokens and directed edges $e = (u, v) \in E$ represent active AMM liquidity pools allowing swaps from token $u$ to token $v$.
   - Assign edge weights $w(u, v) = -\ln\left(\gamma \cdot \frac{y_{uv}}{x_{uv}}\right)$.
   - Identify candidate cycles $C = (T_0, T_1, \dots, T_n = T_0)$ using negative-cycle detection algorithms (e.g., modified Bellman-Ford or exhaustive $k$-hop search for $k \in \{2, 3\}$).

2. **Profitability Condition**:
   - Verify that the cycle product condition holds:
     $$\prod_{i=1}^n \gamma_i \frac{y_i}{x_i} > 1$$

3. **Optimal Input Size ($a^*$ Calculation)**:
   - For a 2-hop cycle between two pools trading tokens $A$ and $B$ (Pool 1 with reserves $x_1, y_1$ and Pool 2 with reserves $x_2, y_2$):
     The output of the first swap is $b_1 = \frac{\gamma_1 y_1 a}{x_1 + \gamma_1 a}$.
     The output of the second swap is $R(a) = \frac{\gamma_2 y_2 b_1}{x_2 + \gamma_2 b_1}$.
   - Maximize net revenue $R(a) - a$ with respect to $a$. The optimal input amount $a^*$ is obtained in closed form by solving $\frac{d R(a)}{d a} = 1$:
     $$a^* = \frac{\sqrt{\gamma_1 \gamma_2 x_1 y_1 x_2 y_2} - x_1 x_2}{\gamma_1 (x_2 + \gamma_2 y_1)}$$
     (valid whenever $\sqrt{\gamma_1 \gamma_2 x_1 y_1 x_2 y_2} > x_1 x_2$).
   - For general $n$-hop cycles ($n \ge 3$), solve the unconstrained one-dimensional convex optimization $\max_{a > 0} [R(a) - a]$ via Brent's method or Newton-Raphson before submitting the transaction.

4. **Execution Decision**:
   - Estimate the total transaction gas cost $G_{\text{total}} = \text{GasUsed} \times \text{BaseFee} + \text{MinerPriorityFee}$.
   - Execute only if projected net profit $\pi(a^*) = R(a^*) - a^* - G_{\text{total}} > \text{MinProfitThreshold} > 0$.

Underspecified / implementation gaps from source:
- Dynamic sizing of miner tips / MEV bundle bribe percentages across different network congestion states.
- Exact routing heuristics when multi-pool tokens have more than 3 intermediary hops.

## Required data

- Real-time Ethereum (or EVM/L2) pending transaction mempool and state trie.
- On-chain reserve states ($x_i, y_i$) and fee structures ($\gamma_i$) for all whitelisted Uniswap V2, SushiSwap, and clone CPMM pools.
- Real-time gas base fee ($EIP-1559$ `baseFeePerGas`) and priority gas fee estimations.
- Flashbots / MEV-Boost block builder RPC endpoints for private bundle inclusion (to avoid public mempool front-running).

## Execution assumptions

- Atomic on-chain execution: all hops must be executed inside a single smart contract invocation. If $R(a^*) - a^* < \text{SlippageTolerance}$, the contract must revert the transaction to prevent capital loss.
- Zero inventory holding period: input capital is borrowed (e.g. via flash loan or held in smart contract) and repaid within the same block.
- Builder / Validator bundle inclusion: transactions are submitted as MEV bundles directly to block builders, paying a fraction of gross profit as a builder tip to ensure top-of-block execution without sandwiching risk.

## Evidence

### Source-reported

- Over the 11-month observation period (May 2020 – April 2021) on Ethereum mainnet, Wang et al. (2022) identified 292,606 executed cyclic arbitrage transactions across Uniswap V2 and SushiSwap.
- Total gross revenue extracted by cyclic arbitrageurs exceeded **138 million USD**.
- Over 99.97% of all cyclic arbitrage transactions were executed via specialized smart contracts.
- The authors observed that unexploited arbitrage opportunities with potential revenue $> 1\text{ ETH}$ (~$4,000 USD at market peak) persistently remained in the market across multiple blocks, reflecting network latency, gas auction friction, and capital constraints among active searchers during the sample period.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- High competition among searchers has commoditized cyclic AMM arbitrage. In modern EVM environments (2024–2026), MEV searchers bid up to 90%–99% of gross arbitrage profits to block builders via Flashbots MEV-Boost auctions, leaving minimal net alpha to the searcher.
- Reverted transactions due to race conditions or state changes between mempool simulation and block execution still incur base gas costs if not submitted through private builder bundles with revert protection.

## Falsification plan

1. Historical simulation on archived EVM node state: Replay historical blocks (2022–2026) across Uniswap V2/V3, SushiSwap, and Curve pools to detect theoretical cyclic opportunities.
2. Net profit measurement: Compute gross profit minus simulated priority gas fees / builder bribes under competitive MEV-Boost auction conditions.
3. Latency / Head-of-line testing: Test whether non-validator searchers can capture cyclic opportunities against co-located builder infrastructure.
4. Falsification criteria: Reject the standalone alpha thesis if net searcher margin after builder tips falls below zero across a 30-day continuous test period on mainnet.

## Crypto portability

direct

The strategy is natively formulated on decentralized exchange liquidity pools and constant-product AMM smart contracts on Ethereum. It directly ports to EVM-compatible layer-1 and layer-2 networks (Arbitrum, Optimism, Base, BSC, Polygon) and non-EVM AMMs (Solana Raydium/Orca) with parameter adjustments for local fee models, block times, and transaction ordering mechanisms.

## Limitations

- High competitive saturation: MEV searcher competition transfers the majority of gross yield to validators/builders.
- State invalidation risk: A competing transaction executing earlier in the same block shifts pool reserves and eliminates the expected price discrepancy.
- Contract risk and execution overhead: Requires custom smart contracts with optimized assembly/Yul execution to minimize gas overhead.
- Not a traditional directional or statistical time-series strategy; cannot be evaluated using conventional backtesting libraries (e.g., PyBroker) without full EVM state replay engines.

## Implementation status

Research-only. No PyBroker, NautilusTrader, paper, testnet, or live trading implementation has been completed.

## Adoption boundary

This record is staging-layer research material only. It does not constitute an operational recommendation, implementation directive, or approval for paper, testnet, or live deployment.

## Related Wiki records

- `crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31`
- `cross-exchange-crypto-spatial-arbitrage-2026-08-31`

## Sources

1. Wang, Ye; Chen, Yan; Wu, Haotian; Zhou, Liyi; Deng, Shuiguang; Wattenhofer, Roger. "Cyclic Arbitrage in Decentralized Exchanges." *Companion Proceedings of the Web Conference 2022 (WWW '22 Companion)*, April 2022, pp. 12–19. DOI: https://doi.org/10.1145/3487553.3524204
2. Wang, Ye; Chen, Yan; Wu, Haotian; Zhou, Liyi; Deng, Shuiguang; Wattenhofer, Roger. "Cyclic Arbitrage in Decentralized Exchanges." *arXiv preprint arXiv:2105.02784* (2021). URL: https://arxiv.org/abs/2105.02784
