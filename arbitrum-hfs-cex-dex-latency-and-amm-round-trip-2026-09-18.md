---
schema: strategy-research-record-v1
title: "Observable High-Frequency Swapping on Arbitrum: Deterministic Sequencer CEX-DEX Latency Edge and Short-Horizon AMM Round-Trips"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - arbitrum
  - layer-2
  - cex-dex
  - latency-arbitrage
  - automated-market-maker
  - uniswap-v3
  - high-frequency-trading
  - microstructure
status: research-only
confidence: high
source_as_of: 2026-09-13
sources:
  - "https://arxiv.org/abs/2609.14481"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Observable High-Frequency Swapping on Arbitrum: Deterministic Sequencer CEX-DEX Latency Edge and Short-Horizon AMM Round-Trips

## Provenance

- **Primary Source:** Shijian Chen (The Hong Kong Polytechnic University), Ya Chen (Hefei University of Technology), Jing Cai (The Hong Kong Polytechnic University), Catherine Liu (The Hong Kong Polytechnic University), *"Quantifying Observable High-Frequency Swapping on Arbitrum"*, arXiv preprint `arXiv:2609.14481v1 [cs.CR, q-fin.TR]`, submitted September 13, 2026 (`source-reported`).
- **Canonical URLs:**
  - Abstract: https://arxiv.org/abs/2609.14481
  - Full-text PDF: https://arxiv.org/pdf/2609.14481v1
  - Primary source archive examined: Complete author-provided LaTeX package (`samplepaper.tex`, `tex/S1_introduction.tex`, `tex/S2_background.tex`, `tex/s3_motivation_example_0x2d512b.tex`, `tex/s4_methodology.tex`, `tex/s5_result.tex`, `tex/s6_discussion.tex`, `tex/s7_conclusion.tex`, `refs.bib`) unpacked from `2609.14481.tar.gz`.
- **Pre-write Deduplication Audit:**
  - Canonical identifier check: `arXiv:2609.14481` does not appear in any existing file in `alpha-strategy-research`.
  - Author search: Zero prior records cite Shijian Chen, Ya Chen, Jing Cai, or Catherine Liu.
  - Market architecture distinction: Existing CEX-DEX research in this repository (`crypto-cex-dex-arbitrage-subsecond-latency-risk-compression-2026-09-01.md`, `mev-origin-cex-dex-arbitrage-jump-diffusion-saturation-2026-09-15.md`) investigates Ethereum Layer-1 mempool environments characterized by Proposer-Builder Separation (PBS), 12-second block intervals, and priority fee bidding. This record captures empirical microstructure on Arbitrum Layer-2, which operates under a centralized first-come, first-served (FCFS) deterministic sequencer with sub-second (~250ms) block times, negligible gas (<$0.05), and no public mempool competition.

## Economic mechanism

### Source-reported

On Ethereum Layer-1, Miner/Maximal Extractable Value (MEV) is primarily structural: searchers compete in public mempools or private builder auctions (MEV-Boost/PBS) via priority gas auctions (PGAs) or builder bribes, executing sandwich attacks, liquidations, and multi-hop cyclic arbitrage. Layer-2 rollups such as Arbitrum transform this execution environment by replacing the auction-based mempool with a centralized sequencer executing transactions under deterministic first-come, first-served (FCFS) ordering at sub-second block intervals (~250ms) with negligible transaction fees (<$0.05). Under this design, classical sandwiching and mempool frontrunning are suppressed, but latency becomes the scarce economic commodity.

Chen et al. (2026) identify and quantify a distinct regime termed **High-Frequency Swapping (HFS)**—continuous single-hop swaps executed at machine cadence by algorithmic actors:
1. **CEX-DEX Latency Edge:** Continuous price discovery primarily occurs on deep centralized exchanges (Binance spot). Because decentralized AMM pools update only when an on-chain transaction executes, price dislocations emerge whenever CEX prices adjust faster than L2 pool reserves. Latency-optimized swappers monitor CEX order books and immediately submit single-swap transactions to L2 pools to extract this pricing lag before AMMs re-equilibrate.
2. **Short-Horizon Pool Round-Trips:** Algorithmic swappers provide liquidity-like behavior by taking directional inventory during transient volume bursts and news shocks (e.g., regulatory announcements), then unwinding positions within a 24-hour window when local pool prices retrace or inventory rebalances.
3. **Same-Peg Stablecoin Micro-Arbitrage:** In low-fee AMM pools (e.g., Uniswap v3 1 bp or 5 bp tiers), subtle deviations from parity between same-peg stablecoins (USDC vs. bridged USDC.e) create risk-free micro-spreads ($>1.0$ exchange rate) that can be systematically captured with near-zero gas costs.

### Research interpretation

The primary economic mechanism is **cross-venue latency arbitrage under deterministic single-sequencer execution**:
- In contrast to L1 where the auction winner captures the entire block arbitrage, L2 FCFS sequencing turns latency into a continuous race to the sequencer's network interface.
- Algorithmic actors do not need to construct complex multi-hop flashloan bundles; instead, they stream lightweight, atomic single-hop swaps directly targeting pool mispricings.
- The high temporal clustering (Fano factor $\gg 1$) and directional persistence (runs of 3–5 consecutive unidirectional swaps) demonstrate that HFS actors operate event-driven execution algorithms triggered by external CEX price drift, consuming AMM liquidity until local pool prices match the CEX benchmark.

## Signal

The primary source documents empirical trading behavior and per-second execution edges (`source-reported`). An operational trading strategy capturing these mechanics within an event-driven framework is specified below (`research-proposed`):

### 1. CEX-DEX Latency Arbitrage Signal (`source-reported` mechanism; `research-proposed` execution parameterization)
- **Observation Grid:** 1-second rolling evaluation window (`source-reported`).
- **DEX Effective Price:** Compute Volume-Weighted Average Price across all pool trades within second $t$:
  $$\mathrm{DEX}_t = \frac{\sum_{i} p_i q_i}{\sum_{i} q_i}$$
  where $p_i$ and $q_i$ are the marginal price and quantity of the $i$-th swap (`source-reported`).
- **CEX Benchmark Price:** Simultaneous Binance spot mid/VWAP price $\mathrm{CEX}_t$ (`source-reported`).
- **Signed Execution Edge (basis points):**
  $$\mathrm{Edge}_t = \begin{cases} \dfrac{\mathrm{CEX}_t - \mathrm{DEX}_t}{\mathrm{CEX}_t} \times 10^4, & \text{if buying base token on DEX} \\[8pt] \dfrac{\mathrm{DEX}_t - \mathrm{CEX}_t}{\mathrm{CEX}_t} \times 10^4, & \text{if selling base token on DEX} \end{cases}$$
- **Trade Trigger (`research-proposed`):**
  - Trigger a DEX buy swap if $\mathrm{Edge}_t \ge \theta_{\text{long}}$, with default $\theta_{\text{long}} = 5.0\text{ bps}$ (`research-proposed`, calibrated to match the source-reported mean edge of +5.4 bps).
  - Trigger a DEX sell swap if $\mathrm{Edge}_t \le -\theta_{\text{short}}$, with default $\theta_{\text{short}} = 5.0\text{ bps}$ (`research-proposed`).
  - Hedging leg: Concurrently submit an offsetting limit/market order on Binance spot to lock the spread and maintain delta-neutral inventory (`research-proposed`).

### 2. AMM Short-Horizon Round-Trip Signal (`source-reported` matching logic; `research-proposed` entry/exit rules)
- **Regime Identification:** High-volatility news shocks or volume acceleration (e.g., hourly swap count $> 3 \times$ rolling 24-hour mean) (`research-proposed`).
- **Entry Execution:** Execute directional burst orders in the direction of order flow momentum (median run length 3 to 4 swaps) (`source-reported`).
- **Exit Logic:**
  - Primary exit: Reversal swap in the same pool when price returns to pool VWAP or reaches a profit target of $+8.0\text{ bps}$ (matching source-reported median round-trip return) (`research-proposed`).
  - Time stop: Mandatory position closeout at $t + 24\text{ hours}$ (`source-reported` maximum round-trip horizon).

### 3. Same-Peg Stablecoin Parity Signal (`source-reported`)
- **Condition:** For same-peg pairs (e.g., USDC $\to$ USDC.e, USDT $\to$ USDC):
  $$R_{\text{exec}} = \frac{Q_{\text{out}}}{Q_{\text{in}}} > 1.0000$$
- **Trigger:** Submit single-hop swap whenever $R_{\text{exec}} \ge 1.00005$ (+0.5 bps gross edge) on Uniswap v3 1 bp or 5 bp pools (`research-proposed`).

## Required data

- **Venues & Markets (`source-reported`):**
  - Decentralized: Arbitrum Layer-2 DEXs (Uniswap v3, Uniswap v2, Camelot, PancakeSwap, SushiSwap, Ramses, Trader Joe).
  - Centralized: Binance Spot (WETH/USDT, WETH/USDC, ARB/USDT, ARB/USDC).
- **Instruments (`source-reported`):**
  - Primary pairs: USDC/WETH, USDT/WETH, ARB/USDC, ARB/WETH.
  - Secondary pairs: Pendle, Magic, GMX, WBTC.
- **On-Chain Data Requirements (`source-reported`):**
  - Full-chain transaction traces parsing `Swap()` events.
  - Output recipient addresses (filtering out router and aggregator smart contracts).
  - Inter-arrival block timestamps and transaction sequence numbers.
- **Off-Chain Market Data (`source-reported`):**
  - High-frequency order book snapshots and top-of-book trades for Binance spot.
- **Data Filtering Protocol (`source-reported`):**
  - Only single-swap transactions retained (excludes multi-hop and cyclic bundles).
  - Liquidation events excluded.
  - Only tokens listed on Binance spot or futures on or before July 2024.

## Execution assumptions

- **Block Interval & Sequencing (`source-reported`):** Arbitrum centralized sequencer with ~250ms block times and deterministic FCFS queue ordering.
- **Transaction Costs (`source-reported`):** L2 execution gas fee typically $< \$0.05$ per swap.
- **Latency Budget (`research-proposed`):** End-to-end signal-to-sequencer network latency must be $< 50\text{ms}$ (co-located or proximity node to Arbitrum sequencer endpoint in AWS/US-East or relevant region) to win the FCFS race against competing HFS searchers.
- **CEX Hedging Costs (`research-proposed`):** VIP fee tier on Binance assumed at 1.0–2.0 bps maker or 2.0–4.0 bps taker.
- **Fill Model (`research-proposed`):** On-chain DEX fill is deterministic based on Uniswap v3 pool liquidity ticks at the moment of execution; zero execution slippage relative to pool state, but subject to queue arrival race conditions.

## Evidence

### Source-reported

All quantitative figures trace directly to Chen, Chen, Cai, and Liu (arXiv:2609.14481v1, September 2026):
1. **Dataset & Scale:**
   - 18-month panel: January 2023 to June 2024.
   - Identified 477 distinct HFS swappers executing 29.9 million single swaps (~22% of all observed Arbitrum swaps).
   - Aggregate notional turnover: $> \$1.02 \times 10^{11}$ USD ($102B).
   - Daily active HFS swappers: average ~42 unique addresses (range 17 to 70).
   - Peak single day: May 23, 2024 (spot Ethereum ETF approval expectations), with 314,842 transactions and $> \$1.08\text{B}$ notional across 57 active swappers.
2. **CEX-DEX Execution Advantage:**
   - Evaluated across 124 swapper-pool combinations with $\ge 1,000$ observed seconds on WETH-stablecoin pools (USDC/WETH, USDT/WETH, DAI/WETH) between June 2023 and June 2024.
   - **Average mean execution edge:** **+5.4 bps**, with an average of **69.6% of seconds** exhibiting positive DEX advantage over Binance spot.
   - Distribution is right-skewed, peaking near +5 bps and extending up to +30 bps (standard deviation $\approx 28\text{ bps}$).
   - Top-performing outlier: address `0x98f989` achieved an average edge of **+26.9 bps** across 2,011 observed seconds, with **97.7% of seconds** showing DEX-favorable execution.
3. **Short-Horizon Round-Trip Profitability:**
   - Evaluated across 161 swapper-pair samples (109 distinct swappers) on USDC/WETH and USDT/WETH between June 2023 and June 2024.
   - **Mean round-trip return:** **+5.7 bps** (median **+8.0 bps**; volume-weighted mean **+9.6 bps**).
   - Profitability share: approximately **75% of swapper-pair combinations** exhibited positive average returns.
   - Return volatility: average 63 bps (weighted 42 bps).
   - Specific pool breakdown: USDC/WETH average +5.5 bps; USDT/WETH average +5.9 bps.
   - Top addresses (`0x6f15ee`, `0x6117e2`, `0x98f989`) achieved average round-trip returns exceeding **+50 bps**.
4. **Stablecoin Micro-Arbitrage:**
   - Identified 16,321 transactions where execution rate strictly exceeded 1.0.
   - Generated estimated gross profit of **$122.7K** across **$168.1M** volume.
   - Highlighted transaction: single swap of $750K USDC $\to$ USDC.e at rate 1.000065 yielded $48.70 profit.
5. **Microstructure & Behavioral Metrics:**
   - Trade size distribution: median $1.75k, 90th percentile $7.95k, 99th percentile $22.5k, maximum $> \$1.0\text{M}$.
   - Inter-arrival times: median 4 seconds, 90th percentile 101 seconds, 99th percentile 881 seconds (~15 minutes).
   - Directional dynamics: median alternation rate 0.25 (1 switch per 4 trades); median run length 3 trades (p90 = 8 trades).
   - Temporal dispersion: median Fano factor 150.93 (p90 = 885.50), reflecting extreme burstiness.
   - Institutional concentration: 8 addresses mapped via Arkham Intelligence to professional firms (Wintermute, Flow Traders, Selini Capital, Manifold Trading).

### Independently reproduced

Not independently reproduced. This record captures empirical findings from the primary source only.

### Negative evidence

- **Unobserved Off-Chain Costs:** On-chain traces capture only executed outcomes; they do not reveal off-chain CEX taker fees, inventory hedging slippage, or funding costs incurred when managing delta on centralized books (`source-reported`).
- **Reversion and Race Losses:** Under FCFS sequencing, multiple searchers detecting the same CEX dislocation submit simultaneous transactions; losing transactions can revert or execute at worse prices, consuming gas without capturing the spread (`research-proposed`).
- **One-Sided Inventory Accumulation:** Address `0x51c728` (Wintermute) executed 303,082 swaps on ARB/USDC that were 100% buys with zero sells, demonstrating that some high-frequency swappers serve as one-way execution conduits for broader off-chain mandates rather than self-contained round-trip strategies (`source-reported`).

## Falsification plan

Operational tests to disconfirm the viability of L2 HFS latency arbitrage:
1. **Net CEX-DEX Margin Stress Test:**
   - Procedure: Simulate simultaneous Binance spot hedging for all DEX executions using real historical tick data.
   - Decision Rule: If net return after deducting 2.0 bps CEX taker fee and $0.05 L2 gas fee drops below **+1.0 bps** across a 30-day walk-forward window, the standalone latency arbitrage thesis is falsified (`research-defined falsification threshold`).
2. **Sequencer Congestion & Reversion Stress Test:**
   - Procedure: Model competing searcher arrival times using an empirical Poisson/Pareto race against top swapper arrival curves.
   - Decision Rule: If the simulated transaction win rate drops below **40%** or transaction reversion costs exceed **30% of gross captured edge**, the strategy is deemed unviable without proprietary sequencer infrastructure (`research-defined falsification threshold`).
3. **Stand-Alone AMM Round-Trip Win-Rate Test:**
   - Procedure: Evaluate 24-hour matched buy-sell cycles on Uniswap v3 without external CEX rebalancing.
   - Decision Rule: If the out-of-sample win rate drops below **55%** or the annualized Sharpe ratio drops below **0.50**, the hypothesis that AMM round-trip profitability is self-contained rather than an artifact of off-chain inventory transfers is falsified (`research-defined falsification threshold`).

## Crypto portability

- **Classification:** `direct`.
- **Reason:** The empirical research, institutional entities, smart contracts, and market dynamics documented in the primary source are natively situated within cryptocurrency Layer-2 decentralized exchanges (Arbitrum Uniswap v3) and centralized crypto exchanges (Binance).
- **Cross-L2 Considerations:**
  - Optimism / Base: Use OP Stack sequencers with different block intervals (e.g., 2 seconds or sub-second flashblocks); FCFS dynamics apply similarly, but fee structures and builder models may vary.
  - Future Protocol Changes: The potential introduction of Arbitrum Timeboost (a priority auction mechanism giving a 200ms express lane to the highest bidder) would fundamentally alter the pure network latency race, converting FCFS HFS into an auction-based MEV regime.

## Limitations

- **Observational Traces Only:** The dataset lacks visibility into off-chain private book state, proprietary inventory levels, CEX order placement, and internal firm risk-transfer protocols.
- **Single-Chain Focus:** Empirical evidence is restricted to Arbitrum from January 2023 to June 2024 and may not directly translate to alternate L2 architectures with distinct sequencer policies.
- **Threshold Sensitivity:** Classification of HFS relies on empirically chosen inter-arrival thresholds ($N \ge 150$, $\tilde{g} \le 120\text{s}$, $g_{0.9} \le 900\text{s}$).

## Implementation status

`not-implemented`. This strategy has not been implemented or backtested within `nautilus-quant-system` or PyBroker.

## Adoption boundary

- Status: `research-only`.
- Adoption: `not-approved`.
- Approval Scope: `research-only`.
- This research record is captured for quantitative intelligence and theoretical understanding of Layer-2 market microstructure. It does not constitute approval for paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- `[[quant/crypto-cex-dex-arbitrage-subsecond-latency-risk-compression-2026-09-01]]`
- `[[quant/mev-origin-cex-dex-arbitrage-jump-diffusion-saturation-2026-09-15]]`
- `[[quant/crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31]]`
- `[[quant/cross-exchange-crypto-spatial-arbitrage-2026-08-31]]`

## Sources

- **Primary Paper:** Shijian Chen, Ya Chen, Jing Cai, Catherine Liu, "Quantifying Observable High-Frequency Swapping on Arbitrum", *arXiv preprint arXiv:2609.14481v1 [cs.CR, q-fin.TR]*, submitted September 13, 2026. URL: [https://arxiv.org/abs/2609.14481](https://arxiv.org/abs/2609.14481).
- **Primary Source Code & Archive:** LaTeX source archive `2609.14481.tar.gz` unpacked and examined on local filesystem (`tex/S1_introduction.tex`, `tex/S2_background.tex`, `tex/s3_motivation_example_0x2d512b.tex`, `tex/s4_methodology.tex`, `tex/s5_result.tex`, `tex/s6_discussion.tex`, `tex/s7_conclusion.tex`, `refs.bib`).
