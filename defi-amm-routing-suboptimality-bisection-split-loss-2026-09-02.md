---
schema: strategy-research-record-v1
title: "Quantifying Sub-Optimality in Routing for Automated Market Makers: Multi-Pool Split Loss, Gas-Aware Front-Running Sensitivity, and Empirical Inefficiency Bounds"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - amm
  - dex-routing
  - optimal-execution
  - bisection-optimization
  - mev
  - sandwich-attacks
status: research-only
confidence: high
source_as_of: 2026-07-22
sources:
  - "Weiye Xi and Ciamac C. Moallemi, 'Quantifying Sub-Optimality in Routing for Automated Market Makers', arXiv:2607.20762v1 [q-fin.TR], July 22, 2026. DOI: 10.48550/arXiv.2607.20762. https://arxiv.org/abs/2607.20762"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Quantifying Sub-Optimality in Routing for Automated Market Makers: Multi-Pool Split Loss, Gas-Aware Front-Running Sensitivity, and Empirical Inefficiency Bounds

## Provenance

- **Primary Source:** Weiye Xi (Columbia University) and Ciamac C. Moallemi (Columbia University / Graduate School of Business), *"Quantifying Sub-Optimality in Routing for Automated Market Makers"*, arXiv preprint `arXiv:2607.20762v1 [q-fin.TR]`, published July 22, 2026. DOI: [10.48550/arXiv.2607.20762](https://doi.org/10.48550/arXiv.2607.20762). Stable URL: [https://arxiv.org/abs/2607.20762](https://arxiv.org/abs/2607.20762).
- **Primary Categories:** Trading and Market Microstructure (`q-fin.TR`), Computer Science - Cryptography and Security (`cs.CR`), Mathematical Finance (`q-fin.MF`).
- **Empirical Dataset:** Full historical swap-level audit of 2.98 million WETH-USDC transactions executed across Ethereum mainnet decentralized exchange (DEX) liquidity pools (including Uniswap v2, Uniswap v3, Curve, Sushiswap, and Balancer), capturing approximately $120 billion in cumulative trading volume across leading routing protocols (Uniswap Universal Router, 1inch v4/v5, CoWSwap, and Odos v2).

## Economic mechanism

### Source-reported

In decentralized automated market maker (AMM) architectures, token liquidity for a single trading pair is fragmented across multiple constant function market maker (CFMM) pools with varying fee tiers, bonding curves, and concentrated liquidity tick distributions:
1. **The Optimal Multi-Pool Routing Problem:** For a swap of input size $\Delta_{\mathrm{in}}$, an optimal router seeks to partition volume $\{\Delta_k\}_{k=1}^K$ across available pools to maximize output tokens $\sum_{k=1}^K f_k(\Delta_k) - \text{GasCost}$. Under convex pool reserve curves, optimality requires equalizing the marginal exchange rate (marginal price) across all actively utilized pools:
   $$f_k'(\Delta_k) = \lambda \quad \forall k \in \mathcal{S}_{\mathrm{active}}$$
2. **Decomposition of Routing Sub-Optimality:** Xi and Moallemi (2026) establish three hierarchy benchmarks to isolate the exact structural origins of realized routing losses:
   - **Support-Constrained Optimum (SCO):** Restricts optimization strictly to the subset of pools $\mathcal{S}_{\mathrm{used}}$ selected by the trader's routing contract, isolating execution split misallocation from venue discovery failure.
   - **Full-Venue Optimum (FVO):** Optimizes across the entire universe of available on-chain pools $\mathcal{U}$, establishing the frictionless upper bound of liquidity aggregation.
   - **Gas-Aware Full-Venue Optimum (G-FVO):** Penalizes multi-pool splitting by the marginal transaction gas cost of interacting with additional smart contract calls, capturing the economically rational boundary where split gains exceed EVM invocation fees.
3. **Drivers of Realized Inefficiency:**
   - **Information Staleness:** Off-chain routing engines compute paths based on state observations at block $T$, but transactions execute at block $T+1$ or $T+2$ against an altered reserve state.
   - **Adversarial MEV / Sandwiching:** Priority gas auctions and builder bundle re-ordering allow searchers to manipulate pre-swap reserves, drastically degrading realized execution relative to the pre-trade quote.
   - **Heavy-Tailed Loss Distribution:** While small retail swaps lose higher basis points due to fixed gas constraints, a tiny fraction of whale trades ($<0.5\%$) accounts for the majority of absolute dollar shortfall.

### Research interpretation

The falsifiable hypothesis is that DEX routing inefficiency is not primarily a static convex optimization failure, but rather a **temporal state-staleness and adversarial extraction tax**:
- Static off-chain routers that ignore block latency and mempool competition deliver systematically sub-optimal execution averaging $\approx 2.02\text{ bps}$ per trade.
- An execution router that dynamically calibrates the G-FVO threshold against real-time base fees (EIP-1559) and routes exclusively via private batch auctions (e.g., CoWSwap / MEV-Share) recaptures the majority of the $24 million empirical shortfall without incurring excess marginal gas.

## Signal

### 1. Convex Routing Optimization via Bisection

For a given token pair with $K$ available CFMM pools where each pool has output function $f_k(\Delta_k)$ with monotonically decreasing marginal output $f_k'(\Delta_k)$:
- For a target marginal price $\lambda$, pool $k$ receives input:
  $$\Delta_k(\lambda) = \begin{cases} (f_k')^{-1}(\lambda) & \text{if } \lambda < f_k'(0) \\ 0 & \text{otherwise} \end{cases}$$
- Total allocated input is $\Delta_{\mathrm{tot}}(\lambda) = \sum_{k=1}^K \Delta_k(\lambda)$.
- The optimal multiplier $\lambda^*$ for trade size $\Delta_{\mathrm{in}}$ is solved efficiently via bisection search on the monotonic function $\Delta_{\mathrm{tot}}(\lambda) = \Delta_{\mathrm{in}}$ over the interval $[\min_k f_k'(\Delta_{\mathrm{in}}), \max_k f_k'(0)]$.

### 2. Gas-Aware Pool Pruning (G-FVO)

- Let $g_k$ be the marginal gas cost (in output token terms) of adding pool $k$ to the execution route:
  $$g_k = \text{GasUnits}_k \times \text{BaseFee}_t \times P_{\mathrm{ETH/Output}}$$
- Sort candidate pools by zero-impact marginal rate $f_k'(0)$.
- Sequentially add pool $k+1$ if and only if the incremental routing output under the $(k+1)$-pool bisection exceeds the marginal gas cost:
  $$\max_{\sum \Delta_j = \Delta_{\mathrm{in}}} \sum_{j=1}^{k+1} f_j(\Delta_j) - \max_{\sum \Delta_j = \Delta_{\mathrm{in}}} \sum_{j=1}^k f_j(\Delta_j) > g_{k+1}$$

### 3. Alpha & Execution Decision Rule

- Compute real-time benchmark output $Y_{\mathrm{G-FVO}}(\Delta_{\mathrm{in}})$ at current state $S_t$.
- Evaluate candidate router quote $Y_{\mathrm{router}}(\Delta_{\mathrm{in}})$.
- If $Y_{\mathrm{G-FVO}} - Y_{\mathrm{router}} > \tau_{\mathrm{exec}} = 3.0\text{ bps}$:
  - Reject public mempool routing.
  - Route order through a private bundle / batch auction solver or internalize the flow via an RFQ solver to capture the routing gap $\Delta Y$.

## Required data

- **Venues & Protocols:** Ethereum mainnet (and L2 rollups: Arbitrum, Optimism, Base).
- **Instruments:** Spot DEX trading pairs (WETH-USDC, WETH-USDT, WBTC-WETH, EURC-USDC).
- **Data Feeds:**
  - Full tick-by-tick and event-level CFMM logs: `Swap`, `Mint`, `Burn`, and `Sync` events across Uniswap v2, Uniswap v3, Uniswap v4, Curve v1/v2, Sushiswap, and Balancer.
  - EIP-1559 base fee, priority fee, and builder payment data from Flashbots / MEV-Boost block traces.
  - Mempool pending transaction streams and block inclusion position (transaction index within block).
- **Point-in-Time Requirement:** Strict block-by-block state reconstruction at the exact transaction execution index (pre-swap state vs. post-swap state).

## Execution assumptions

- **Transaction Atomicity:** Smart contract batch executions are atomic within the single transaction payload.
- **Gas Model:** Gas usage per additional CFMM call is approximately 50,000 to 120,000 gas units depending on pool complexity (Uniswap v2 vs. concentrated v3 tick crossings).
- **Slippage Tolerance:** Limit order or maximum slippage tolerance parameter $\epsilon_{\mathrm{slip}} \in [0.05\%, 0.50\%]$ set in router swap parameters.
- **Reversion Risk:** Transactions that exceed user-specified minimum output revert, incurring gas loss with zero token swap.

## Evidence

### Source-reported

All figures below are directly reported by Weiye Xi and Ciamac C. Moallemi (arXiv:2607.20762v1, July 2026):
1. **Sample Scale:**
   - 2.98 million WETH-USDC swaps analyzed across Ethereum mainnet.
   - Total analyzed transaction volume: $\approx \$120\text{ billion}$.
2. **Quantified Routing Shortfall:**
   - Realized routing executions suffered an average shortfall of **2.02 basis points (bps)** per trade relative to the optimal benchmark.
   - Aggregate economic loss: **$24 million** of forgone output value across the sample.
3. **Benchmark Attribution:**
   - Comparing Support-Constrained Optimum (SCO) to realized execution reveals that volume splitting across selected pools is frequently imperfect due to heuristic discretization in off-chain routing algorithms.
   - Comparing Full-Venue Optimum (FVO) and Gas-Aware (G-FVO) reveals that routers frequently omit smaller or newly deployed liquidity pools where marginal prices are superior, even after accounting for marginal gas costs.
4. **Adversarial & Latency Drivers:**
   - A substantial fraction of severe sub-optimality is caused by adversarial sandwiching attacks that alter the state between quote generation and block inclusion.
   - Heavy-tailed distribution: small trades lose higher percentage yield to gas, while large whale trades drive the majority of absolute dollar shortfall.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Gas Spikes Exceeding Split Benefits:** During high gas volatility (e.g., base fee $> 100\text{ gwei}$), the marginal benefit of splitting a $\$50\text{k}$ swap across 3 pools is completely wiped out by EVM execution overhead ($g_k > \Delta f_k$).
- **Concentrated Liquidity Tick Crossing Complexity:** In Uniswap v3 pools with sparse liquidity, high-order tick crossings introduce non-differentiable step functions that degrade the convergence speed of naive bisection algorithms.
- **Off-Chain Routing Latency:** Sub-millisecond price movements on centralized exchanges (Binance) frequently render on-chain marginal rate equilibrium stale before the Ethereum block can be sealed.

## Falsification plan

1. **Marginal Price Equalization Test:** Run real-time bisection on live tick states and compare output against leading aggregator API quotes (1inch, Uniswap, Odos). Falsification threshold: If the bisection G-FVO output fails to beat the best aggregator quote by $> 1.0\text{ bps}$ net of gas on trades $>\$100\text{k}$, reject the routing arbitrage hypothesis.
2. **Sandwich-Free Private Routing vs. Public Mempool Test:** Execute 1,000 paired WETH-USDC swaps ($>\$50\text{k}$ notional) split equally between public mempool routing and private batch auction routing (CoWSwap / Flashbots Protect). Falsification threshold: If public routing does not suffer at least $1.5\text{ bps}$ higher realized slippage on average ($p < 0.01$), reject the hypothesis that adversarial ordering drives the majority of routing sub-optimality.
3. **Gas Sensitivity Boundary Test:** Perturb simulated base fee from 10 gwei to 150 gwei. Falsification threshold: If the optimal pool count does not collapse monotonically to 1 for trade sizes $<\$10\text{k}$, falsify the gas-pruning model.

## Crypto portability

- **Direct:** The model and empirical findings are formulated natively for Ethereum DeFi AMM architectures and EVM-compatible DEX routers.
- **Portability to Alternative Chains:**
  - **L2 Networks (Arbitrum, Base):** Extremely low base fees lower the gas threshold $g_k$, making multi-pool fine splitting optimal even for modest retail trade sizes ($<\$500$).
  - **High-Throughput Chains (Solana):** Micro-slot architectures (400ms) and low gas shift the primary routing bottleneck from gas cost optimization to RPC state latency and transaction landing priority.

## Limitations

- **Not independently reproduced:** Relies on empirical findings from Xi and Moallemi (2026).
- **Single-Pair Focus:** Primary empirical analysis centers on WETH-USDC; multi-hop routing paths (e.g., Token A $\to$ WETH $\to$ Token B) introduce combinatorial graph search complexity not fully captured in single-pair bisection.
- **Static Block Assumption:** Benchmark assumes optimal execution against the instantaneous pre-trade block state, ignoring potential endogenous market impact on subsequent block transactions.

## Implementation status

- `not-implemented`
- Research capture only. No production execution or routing algorithm implemented in PyBroker, Nautilus, or live routing gateways.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Research capture does not authorize paper, testnet, or live trading execution.

## Related Wiki records

- `[[crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31]]`
- `[[defi-cfmm-intrinsic-liquidity-carr-madan-delta-hedge-2026-09-01]]`
- `[[crypto-priority-gas-auctions-pga-dex-latency-arbitrage-2026-09-01]]`
- `[[prediction-market-structural-volatility-wright-fisher-glosten-milgrom-2026-09-02]]`

## Sources

1. Weiye Xi and Ciamac C. Moallemi, *"Quantifying Sub-Optimality in Routing for Automated Market Makers"*, arXiv preprint `arXiv:2607.20762v1 [q-fin.TR]`, published July 22, 2026. DOI: [10.48550/arXiv.2607.20762](https://doi.org/10.48550/arXiv.2607.20762). Stable URL: https://arxiv.org/abs/2607.20762.
