---
schema: strategy-research-record-v1
title: Just-In-Time Liquidity Provision in Concentrated Liquidity AMMs
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - dex
  - clmm
  - uniswap-v3
  - mev
  - just-in-time-liquidity
  - market-microstructure
status: research-only
confidence: high
source_as_of: 2025-09-15
sources:
  - https://arxiv.org/abs/2509.16157
  - https://doi.org/10.4230/LIPIcs.AFT.2025.16
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4426219
  - https://arxiv.org/abs/2305.15570
  - https://eprint.iacr.org/2023/458
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Just-In-Time Liquidity Provision in Concentrated Liquidity AMMs

## Provenance

Primary source:

- Bruno Llacer Trotti, Weizhao Tang, Rachid El-Azouzi, Giulia Fanti, and Daniel Sadoc Menasché. "Strategic Analysis of Just-In-Time Liquidity Provision in Concentrated Liquidity Market Makers." *7th Conference on Advances in Financial Technologies* (AFT 2025), Schloss Dagstuhl – Leibniz-Zentrum für Informatik. DOI: https://doi.org/10.4230/LIPIcs.AFT.2025.16 / arXiv preprint: https://arxiv.org/abs/2509.16157.

Foundational and related empirical literature:

- Austin Adams and Robin Wan. "Just-in-time Liquidity on the Uniswap Protocol." *SSRN Working Paper Series*, Abstract ID 4426219 (2023). Stable reference: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4426219.
- Agostino Capponi, Ruizhe Jia, and Ye Zhu. "The Paradox of Just-in-Time Liquidity in Decentralized Exchanges: More Providers Can Sometimes Mean Less Liquidity." *Columbia University / arXiv preprint*, arXiv:2305.15570 (2023). Reference: https://arxiv.org/abs/2305.15570.
- Liyi Xiong, Bingsheng Zhang, and Luyao Zhang. "Demystifying Just-in-Time (JIT) Liquidity Attacks on Uniswap V3." *Cryptology ePrint Archive*, Report 2023/458 (2023). Reference: https://eprint.iacr.org/2023/458.

The empirical data in these studies covers transaction-level event logs, mempool broadcasts, and MEV-Boost bundle execution data across Uniswap V3 pools on the Ethereum Layer-1 mainnet from pool inception through late 2024.

## Economic mechanism

### Source-reported

In Concentrated Liquidity Market Makers (CLMMs) such as Uniswap V3, liquidity providers (LPs) specify customized price intervals $[P_a, P_b]$ for their capital. Just-In-Time (JIT) liquidity provision is a strategic Maximal Extractable Value (MEV) strategy where a specialized LP:
1. Detects a large pending swap transaction in the public mempool or private transaction stream;
2. Mints a massive, ultra-concentrated liquidity position in the target pool within the exact narrow price tick range of the pending swap, scheduled immediately before the swap in an atomic bundle;
3. Allows the target swap to execute against the newly injected liquidity, earning swap fees and altering the position's token balance;
4. Burns the liquidity position and collects the accrued fees and returned token balances immediately following the swap within the exact same block.

Trotti et al. (2025) provide a formal transaction-level game-theoretic and optimization model of JIT liquidity. Crucially, the authors discover that **price impact** (the net change in token values resulting from the trade) accounts for approximately **93.7%** of total JIT gross revenue, while swap fee extraction accounts for the remainder (~6.3%). By supplying concentrated liquidity, JIT providers effectively execute an instantaneous asset exchange at favorable execution terms. The authors also establish that real-world JIT bots operate sub-optimally; solving the non-linear optimization problem increases average JIT profits by up to **69%** while reducing passive LP returns by **40% to 44%** per targeted trade.

### Research interpretation

The economic foundation of JIT liquidity is a **zero-holding-period, adverse-selection-free market making strategy**:

1. **Elimination of Holding Risk:** Unlike passive LPs who leave capital exposed across multiple blocks to price drift and toxic arbitrage flow (Loss Versus Rebalancing / LVR), a JIT LP holds exposure for zero blocks ($\Delta t \to 0$), entirely avoiding multi-block directional risk.
2. **Selective Flow Targeting:** The JIT bot selectively targets uninformed or large retail swaps where fee revenue and predictable price impact exceed execution costs, avoiding toxic informed trades that would lead to adverse post-swap price drift.
3. **Non-Linear Fee and Inventory Payoff:** By depositing a large liquidity amount $L_{\text{JIT}} \gg L_{\text{passive}}$, the JIT bot captures the dominant fraction $\frac{L_{\text{JIT}}}{L_{\text{passive}} + L_{\text{JIT}}}$ of the swap fee $\gamma \cdot \Delta x$, while purchasing the sold token at an average execution price bounded by the concentrated tick interval.
4. **Economic Constraint:** The strategy's net profitability depends on whether gross earnings $(\text{Fee Share} + \text{Inventory Value Shift})$ exceed total operational overhead $(\text{L1 Gas Costs} + \text{MEV-Boost Builder Bribe} + \text{Hedging/Disposal Slippage})$.

## Signal

The strategy operates as an ultra-low-latency event-driven MEV execution pipeline:

### 1. Target Swap Detection & Filtering
At time $t$, continuously inspect incoming unconfirmed transactions in the Ethereum mempool / pending bundle stream. Trigger JIT evaluation if:
- Target contract is a verified Uniswap V3 / CLMM pool contract $P$ with fee tier $\gamma \in \{0.01\%, 0.05\%, 0.30\%, 1.00\%\}$.
- Target transaction $T_{\text{target}}$ is a valid swap call (`exactInputSingle`, `exactInput`, `exactOutputSingle`, `swap`) with gross input value:
  $$\text{Value}(T_{\text{target}}) \ge \text{Threshold}_{\text{min}} \quad (\text{e.g., } \ge \$50,000 \text{ USD equivalents})$$
- Target swap slippage tolerance parameter $\sqrt{P}_{\text{limit}}$ allows sufficient price movement.

### 2. State & Price Trajectory Computation
- Extract pool state: current tick $i_0$, square root price $\sqrt{P}_0$, and current active liquidity $L_{\text{passive}}$ in the active tick range.
- Compute the expected post-swap tick $i_1$ given input token amount $\Delta x_{\text{target}}$ and target direction (Token $0 \to$ Token $1$ or Token $1 \to$ Token $0$).
- Define JIT tick boundaries $[i_l, i_u]$ such that $i_l \le \min(i_0, i_1)$ and $i_u \ge \max(i_0, i_1)$. For maximum concentration, $[i_l, i_u]$ is set to the minimal valid tick spacing covering the trade path (e.g., 1 to 2 tick widths).

### 3. Optimal JIT Liquidity Optimization
Solve the constrained non-linear optimization for JIT liquidity amount $L_{\text{JIT}}^*$:
$$\max_{L_{\text{JIT}}} \Pi(L_{\text{JIT}}) = \text{FeeEarned}(L_{\text{JIT}}, \Delta x_{\text{target}}, \gamma) + \Delta V_{\text{inventory}}(L_{\text{JIT}}, i_0, i_1) - \text{Cost}_{\text{gas}} - \text{Bribe}(b)$$
subject to:
- $L_{\text{JIT}} \le L_{\text{capital\_limit}}$ (available capital / flash loan capacity);
- Net expected profit $\Pi(L_{\text{JIT}}) > \text{Threshold}_{\text{profit\_min}}$ (e.g., $> \$25$ net USD).

### 4. Atomic Bundle Assembly & Execution
Construct an atomic bundle containing three sequential transactions:
1. **Tx 1 (Frontrun Mint):** JIT bot calls `NonfungiblePositionManager.mint()` or direct pool `mint()` with liquidity $L_{\text{JIT}}^*$ on tick range $[i_l, i_u]$.
2. **Tx 2 (Target Execution):** Target user swap $T_{\text{target}}$.
3. **Tx 3 (Backrun Burn & Collect):** JIT bot calls `burn()` and `collect()`, converting position back into raw tokens Token 0, Token 1, and collected fee tokens $\Delta fee_0, \Delta fee_1$.
4. **Builder Bribe:** Append direct builder coinbase payment `block.coinbase.transfer(b)` where $b = \alpha \cdot \Pi_{\text{gross}}$ (with bribe share $\alpha \in [0.70, 0.95]$ depending on competitive auction density).

### 5. Inventory Disposal / Hedging
- Any residual unbalanced token acquired during the swap is immediately liquidated via off-chain RFQ, CEX market order, or CowSwap / 1inch solver API to restore neutral inventory.

## Required data

- **High-Frequency Mempool Stream:** Low-latency Ethereum L1 / L2 WebSocket mempool feed (via custom Geth / Nethermind / Reth full nodes) and MEV relay feeds (Flashbots Protect, bloXroute, Eden, BeaverBuild, Titan).
- **On-Chain CLMM State:**
  - Uniswap V3 pool contract storage: `slot0` (current `sqrtPriceX96`, `tick`, `feeProtocol`), active liquidity $L$, tick bitmap words, and initialized `Tick` structs.
  - ERC-20 token balances and allowance states.
- **Gas & MEV Auction Data:**
  - EIP-1559 base fee trajectory, priority gas fees, and historical builder bundle pricing distributions.
- **Off-Chain Reference Price:** Real-time CEX order book feeds (Binance, Coinbase, OKX) for spot index prices to compute inventory hedging cost and fair-value displacement.

## Execution assumptions

- **Atomic Bundle Execution:** Strategy requires private relay submission (e.g., MEV-Boost / Flashbots Builder RPC) where bundles are either included in their entirety or dropped, guaranteeing zero risk of orphan mint positions.
- **Gas Consumption:** A complete JIT bundle (mint + target swap + burn + collect + coinbase bribe) consumes approximately $280,000 - 360,000$ gas units.
- **Builder Bribe Structure:** Competitive searcher auctions force bidding up to $80\% - 95\%$ of gross MEV profit to winning block builders.
- **Zero-Block Duration:** Capital is committed for the duration of a single Ethereum block ($12$ seconds slot duration) with intra-block atomicity.
- **Flash Liquidity Availability:** Capital for $L_{\text{JIT}}$ is supplied from pre-funded searcher vault balances or flash-loan providers (Balancer / Aave / Uniswap Flash Swaps).

## Evidence

### Source-reported

- **Trotti, Tang, El-Azouzi, Fanti, and Menasché (2025):**
  - Transaction-level modeling demonstrates that **93.7%** of JIT liquidity provider profits originate from price impact / token conversion rather than fee extraction alone.
  - Comparing empirical JIT bot transactions against the theoretical optimal non-linear allocation reveals that existing market bots leave significant value uncaptured; optimal sizing increases JIT earnings by up to **69%** on average.
  - Strategic JIT liquidity reduces slippage for target traders but reduces the fee revenues of passive liquidity providers by **40% to 44%** per targeted trade.
- **Adams and Wan (2023):**
  - Empirical analysis of Uniswap V3 demonstrates that JIT liquidity accounts for a meaningful fraction of total swap volume on high-fee pairs (e.g., 0.30% and 1.00% tiers), with JIT providers achieving high capital efficiency due to holding times of exactly one transaction.
- **Capponi, Jia, and Zhu (2023):**
  - Theoretical and empirical analysis indicates that JIT liquidity providers act as predatory market makers, causing passive LPs to experience heightened adverse selection and reducing long-term passive depth on affected pairs.

### Independently reproduced

Not independently reproduced in the user's research stack.

### Negative evidence

- **MEV Bribe Margin Compression:** High competition among MEV searchers using identical mempool scanning algorithms results in bidding wars where builder bribes consume in excess of 90% of gross profits, severely lowering net return on capital.
- **Migration to Private Order Flow (PFOF / Intent-Based DEXs):** The rapid growth of intent-based routing mechanisms (UniswapX, CoW Swap, 1inch Fusion) and private mempools (Flashbots Protect, MEV Blocker) routes large retail orders off the public mempool, reducing the frequency of profitable public JIT targets.
- **L2 Centralized Sequencers:** On Layer-2 rollups (Arbitrum, Optimism, Base), centralized sequencer FIFO (First-In, First-Out) ordering without public mempools eliminates the standard pre-swap/post-swap sandwich bundle mechanism unless searchers collude with or operate sequencers.

## Falsification plan

The JIT liquidity provision hypothesis should be rejected or considered unviable for production research if:

1. **Net Profitability Failure:** Net revenue after paying EIP-1559 base gas fees, builder bribes ($\ge 85\%$), flash loan fees, and off-chain inventory hedging slippage is non-positive ($\Pi_{\text{net}} \le 0$) over a continuous 60-day out-of-sample backtest.
2. **Private Flow Cannibalization:** The share of high-slippage public mempool swaps on Ethereum L1 CLMM pools drops by $> 75\%$ due to intent-based auction routing, reducing strategy trade frequency below statistical viability ($< 1$ opportunity/day).
3. **Protocol-Level Defenses:** Implementation of protocol-level JIT mitigation mechanisms (e.g., minimum LP holding duration, dynamic fee splitting, or multi-block fee vesting) renders intra-block JIT liquidity unexecutable.

## Crypto portability

**Direct**, as Concentrated Liquidity Market Makers, Ethereum transaction bundles, flash liquidity, and MEV-Boost builder architectures are native to decentralized cryptocurrency protocols.

Portability considerations:
- **EVM CLMMs:** Directly applicable to Uniswap V3, PancakeSwap V3, Sushiswap v3, and Camelot on Ethereum, Arbitrum, and Polygon (where bundle relays exist).
- **Non-EVM CLMMs:** Applicable to Solana CLMMs (Raydium CLMM, Orca Whirlpools) via Jito-Solana bundle auctions, though block slot times (400ms) and leader schedules differ materially from Ethereum.

## Limitations

- **Not independently reproduced** in this research stack.
- **Infrastructure & Latency Dependency:** Requires co-located full nodes, low-latency mempool feeds, and optimized solver pipelines; millisecond delays result in missed bundles.
- **Builder Relay Dependence:** Vulnerable to builder-level censorship, bundle unbundling, or validator MEV-stealing.
- **Inventory Basis Risk:** If secondary market CEX/DEX hedging is delayed, the residual token inventory exposes the operator to market gap risk.

## Implementation status

No implementation in PyBroker, NautilusTrader, the strategy registry, any data pipeline, Paper, Testnet, Demo, or Live trading has been created or modified.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material in the Alpha Strategy Pool only. It is not evidence of validated alpha, not an implementation task, and not approval for Paper, Testnet, Demo, or Live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

- `[[crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31]]`
- `[[dex-cyclic-arbitrage-constant-product-amm-2026-09-01]]`
- `[[defi-lending-collateral-liquidation-discount-arbitrage-2026-09-01]]`
- `[[funding-aware-market-making-perpetual-dex-2026-08-31]]`

## Sources

1. Bruno Llacer Trotti, Weizhao Tang, Rachid El-Azouzi, Giulia Fanti, and Daniel Sadoc Menasché, "Strategic Analysis of Just-In-Time Liquidity Provision in Concentrated Liquidity Market Makers," *7th Conference on Advances in Financial Technologies* (AFT 2025), Schloss Dagstuhl – Leibniz-Zentrum für Informatik. DOI: https://doi.org/10.4230/LIPIcs.AFT.2025.16 / arXiv: https://arxiv.org/abs/2509.16157
2. Austin Adams and Robin Wan, "Just-in-time Liquidity on the Uniswap Protocol," *SSRN Working Paper Series*, Abstract ID 4426219, 2023. Reference: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4426219
3. Agostino Capponi, Ruizhe Jia, and Ye Zhu, "The Paradox of Just-in-Time Liquidity in Decentralized Exchanges: More Providers Can Sometimes Mean Less Liquidity," *arXiv preprint*, arXiv:2305.15570, 2023. Reference: https://arxiv.org/abs/2305.15570
4. Liyi Xiong, Bingsheng Zhang, and Luyao Zhang, "Demystifying Just-in-Time (JIT) Liquidity Attacks on Uniswap V3," *Cryptology ePrint Archive*, Report 2023/458, 2023. Reference: https://eprint.iacr.org/2023/458
