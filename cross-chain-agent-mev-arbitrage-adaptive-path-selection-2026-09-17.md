---
schema: strategy-research-record-v1
title: Cross-Chain Agent MEV Arbitrage — Adaptive Path Selection with Dual Searcher-Target Vulnerability
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-chain
  - mev
  - defi
  - ai-agents
status: research-only
confidence: medium
source_as_of: 2026-09-15
sources:
  - https://arxiv.org/abs/2609.17897
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Chain Agent MEV Arbitrage — Adaptive Path Selection with Dual Searcher-Target Vulnerability

## Provenance

- **Paper:** Wei Ye, Jingyan Xu, Yuanhong Wu. "When AI Agents Meet MEV: Cross-Chain Arbitrage in the Agentic Economy."
- **arXiv ID:** `arXiv:2609.17897v1 [cs.CR]`
- **Submitted:** 15 Sep 2026 (v1)
- **Published at:** 7th International Conference on Mathematical Research for Blockchain Economy (MARBLE 2026)
- **Authors:** Wei Ye (Department of Economics, Fordham University, New York, NY, USA); Jingyan Xu, Yuanhong Wu (Department of Computer and Information Science, Fordham University, New York, NY, USA)
- **Primary source:** https://arxiv.org/pdf/2609.17897 (17 pages, 4 figures, 4 tables)
- **Data period:** 23,000 tick-level Uniswap V3 swap events (WETH/USDC) across Ethereum, Arbitrum, and Base; five trading days (Feb 22–25 and Mar 23, 2026); DeFiLlama aggregate data Sep 2025–Mar 2026 for calibration.

## Economic mechanism

### Source-reported

The paper studies cross-chain arbitrage when autonomous AI agents, rather than humans or bots, are the searchers. The authors argue that agents operate simultaneously as MEV extractors and MEV targets — a duality that existing cross-chain MEV models obscure. The mechanism has two components:

1. **Cross-chain price gap exploitation:** Price discrepancies between DEX pools on different chains (e.g., WETH/USDC on Ethereum vs. Arbitrum) create arbitrage opportunities. The gap-to-cost ratio determines viability, not the absolute gap size.
2. **Dual agent exposure:** Because agents follow deterministic or near-deterministic policies, they become predictable MEV targets. An adversary can observe the agent's on-chain transaction history and predict timing, trade size, and path, enabling sandwich attacks and predictive front-running across chains.

### Research interpretation

The hypothesized alpha mechanism is structural: cross-chain DEX liquidity fragmentation creates persistent (structural) price gaps driven by execution timing and information latency rather than fundamental market segmentation. The paper finds that cross-chain price gaps (ETH–ARB mean 0.044%) are comparable in magnitude to intra-chain fee-tier gaps (ETH .01%–.05% mean 0.049%), supporting the interpretation that the gap is a microstructure artifact, not an informational inefficiency.

The economic thesis for an AI-agent arbitrageur is: identify the optimal trade size and path selection strategy under transaction cost constraints (gas + bridge fees) and price uncertainty during bridge delay, while calibrating MEV protection (timing/size randomization) against profit loss.

**Key signal components (research-proposed operationalization):**
- **Primary signal:** Cross-chain price gap between DEX execution prices (e.g., WETH/USDC on ETH vs. ARB)
- **Optimal sizing:** Mean-variance utility: x* = p_i(t)(μ_j − p_i(t)) / (λσ²_j) — gap-dependent, volatility-penalized, risk-aversion-scaled
- **Path selection:** Belief-weighted online learning (ε-greedy with exponential moving average belief updates; converges under Robbins–Monro)
- **MEV protection:** Transaction timing randomization, trade size perturbation, MEV-aware bridge selection (research-proposed ϕ ≈ 0.4–0.6 optimal protection level)

## Signal

- **Formation timestamp:** Continuous monitoring of on-chain DEX execution prices; arbitrage decision at each observation interval. 10-second binning used for empirical gap measurement.
- **Lookback:** Belief updates use exponential moving average (η = 0.1 in experiments); no fixed lookback window — beliefs are stateless updates of success probability.
- **Long entry (buy on source, sell on destination):** Execute when the cross-chain price gap exceeds the cost threshold: E[p_j(t + τ_ij)] > p_i(t)(1 + c(t)/x). Arbitrage involves buying token A on chain B_i at p_i(t) and selling on chain B_j after bridging.
- **Short entry (sell on source, buy on destination):** Not explicitly modeled — paper focuses on single-direction price gap exploitation.
- **Exit:** Immediate — single-period arbitrage profit captured upon sale on destination chain. No holding period.
- **Holding period:** Duration of bridge delay τ_ij (seconds to minutes). Inventory-based arbitrage averages ~9s; bridge-based averages ~242s (source-reported from Öz et al. 2025).
- **Parameters:** Risk aversion λ (configurable by agent designer); exploration rate ε = 0.1; learning rate η = 0.1; discount factor δ. All are research-proposed choices for the simulation, not source-optimized.
- **Position-sizing logic:** x* = p_i(t)(μ_j − p_i(t)) / (λσ²_j) — risk-aversion-scaled optimal size under mean-variance utility. (research-proposed operationalization; source derives the formula but does not field-test specific parameter values)
- **Falsification thresholds (research-defined):** Adaptive strategy mean profit > Greedy baseline over 100 independent 180-day trials; MEV exposure reduction > 50% at ϕ ≈ 0.4–0.6.

## Required data

- **Instrument:** WETH/USDC (primary); WBTC/USDC, ARB/USDC, OP/USDC (calibration).
- **Universe:** Uniswap V3 pools across Ethereum (0.01%, 0.05%, 0.30% fee tiers), Arbitrum (0.01%, 0.05%), and Base (0.01%, 0.05%).
- **Venue:** Uniswap V3 on Ethereum, Arbitrum, Base; DeFiLlama for aggregate gas/bridge/DEX volume data.
- **Market type:** DEX spot (WETH/USDC pair); cross-chain bridge transfers (Across, Stargate, Hop, CCTP).
- **Timeframe:** Tick-level swap events (second resolution); 10-second aggregation bins.
- **Fields:** Execution price per swap; daily OHLCV; daily gas fees per chain; daily bridge volume per protocol; daily DEX volume per chain.
- **Timestamp:** Second-level resolution for L2 swap events; daily for calibration data.
- **Point-in-time:** L2 data spans Feb 22–25 and Mar 23, 2026; calibration data Sep 2025–Mar 2026.
- **Missing-data:** L1–L2 overlap window limited to 28 minutes on Mar 23 (only 112 simultaneous ETH–ARB observations vs. 954 ARB–Base). Cross-chain daily discrepancies negligible at daily frequency (closed by bots within milliseconds). (data gap — limited L1–L2 simultaneous observation window)
- **Transaction costs (source-reported):** Gas fees: Ethereum mean $668K/day aggregate, Base $201K/day, Arbitrum $45K/day, Optimism $4.8K/day. Per-trade costs: ETH–ARB estimated $5.25 (gas + bridge); ARB–Base via CCTP estimated $0.70–$1.20. These are calibrated from DeFiLlama aggregate data, not observed per-trade.

## Execution assumptions

- **Signal-to-order timing:** Continuous monitoring; decision at each observation interval (10-second bins in experiments).
- **Next-bar vs same-bar:** Not applicable — tick-level execution assumed.
- **Market order:** DEX swap (market order on AMM).
- **Fill model:** Full fill assumed for all simulated trades. No partial fill modeling.
- **Fees:** Gas fees per chain (calibrated from DeFiLlama daily aggregate); DEX swap fees (Uniswap V3 fee tiers: 0.01%–0.30%). Fees are included in the cost threshold but not modeled at per-trade granularity.
- **Spread:** Not explicitly modeled; execution price observed from Uniswap V3 swap data.
- **Slippage:** Not explicitly modeled as a separate component. The execution price from Uniswap V3 already incorporates price impact.
- **Impact / capacity:** Not modeled. The paper assumes the agent's trades do not move the market.
- **Funding:** Not applicable for spot DEX arbitrage.
- **Leverage / margin:** Not used in the arbitrage model. Leverage is irrelevant for single-period DEX spot arbitrage.
- **Latency:** Bridge delay τ_ij is the primary latency component: inventory-based ~9s, bridge-based ~242s (source-reported from Öz et al. 2025).
- **Partial fills / failures:** Arbitrage failure included in the model (negative profit or execution failure triggers belief update).
- **Key gap:** The paper calibrates per-trade costs from aggregate daily chain-level data, not from actual per-trade observations. This introduces estimation uncertainty into the cost threshold. (underspecified)

## Evidence

### Source-reported

- **Cross-chain price gap statistics (Table 2, Section 5.2):** ETH–ARB: N=112, mean 0.044%, median 0.031%, P90 0.086%, max 0.479%. ARB–Base: N=954, mean 0.013%, median 0.010%, P90 0.027%, max 0.077%. Intra-chain ETH .01%–.05%: N=267, mean 0.049%. All WETH/USDC, 10-second bins.
- **Arbitrage viability (Section 5.3):** At $50K trade size with $5.25 total cost, 80% of ETH–ARB 10-second windows are profitable. At $10K via CCTP with $0.70 cost, 63% of ARB–Base windows are viable. On Ethereum, trades below $25K rarely viable.
- **Adaptive path selection performance (Table 3, Section 5.4):** 100 runs, 180 days, 4 chains, 12 paths. Random: mean profit −$135 (Std 345). Greedy: $2,367 (Std 697). ε-Greedy: $2,242 (Std 586). Adaptive (ours): $2,627 (Std 560). Adaptive outperforms Greedy in 57/100 runs, ε-Greedy in 69/100 runs. Adaptive advantage strongest when path success probabilities are heterogeneous.
- **MEV protection-profitability tradeoff (Table 4, Section 5.5):** 30 independent trials per protection level ϕ. At ϕ=0: attacker achieves 100% joint prediction accuracy. At ϕ=0.4: 54.2% joint accuracy, MEV exposure cut >50%. At ϕ=0.8: 16.0% joint accuracy. Optimal protection near ϕ≈0.4–0.6.
- **Convergence proof (Proposition 1, Section 3.3):** Belief estimates converge to true success probability under Robbins–Monro conditions (decaying η_t with Ση_t = ∞ and Ση²_t < ∞).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The Random strategy loses money on average (−$135), confirming that naive path selection is insufficient when gaps are small relative to costs.
- L2–L2 gaps (ARB–Base mean 0.013%) are small; viability depends critically on trade size and cost assumptions. At $1K trade size, viability drops substantially.
- The paper's future work acknowledges that L1–L2 data collection needs scaling to weeks for formal distributional estimation, and the framework has not been tested in multi-agent strategic settings.

## Falsification plan

1. **Out-of-sample cross-chain gap persistence:** Replicate the 10-second gap measurement on additional token pairs (WBTC/USDC, ARB/USDC) and additional L2 chains (Optimism) over longer time windows (weeks, not days). Failure if gap-to-cost ratio is insufficient for consistent profitability after realistic execution costs.
2. **Adaptive path selection vs. simpler baselines:** Run the belief-weighted algorithm against Greedy and ε-Greedy on out-of-sample data. Failure if the 11% average improvement does not hold outside the calibrated simulation environment.
3. **Transaction cost sensitivity:** Vary per-trade costs (gas fees, bridge fees, slippage) by ±50% from calibrated values. Failure if profitability is eliminated at realistic cost levels.
4. **MEV exposure under adversarial conditions:** Test the protection-profitability tradeoff in a live or testnet setting with realistic sandwich attackers. Failure if the ϕ≈0.4–0.6 optimal protection level does not generalize beyond the simulation's simplified attacker model.
5. **Capacity and market impact:** Increase simulated trade sizes to detect when the agent's own trades begin to move DEX prices. Failure if the framework breaks down at realistic capital levels.
6. **Failure metric (research-defined):** If the adaptive strategy's mean profit over 100 independent 180-day simulations falls below the Greedy baseline mean minus one standard deviation, the hypothesis is materially weakened. Action: reconsider the belief-update mechanism or path-selection rule.

## Crypto portability

direct

The paper is natively about crypto (DeFi cross-chain DEX arbitrage). Key crypto-specific considerations:

- **Spot vs perpetual:** The arbitrage model applies to DEX spot pools (Uniswap V3). Perpetual futures arbitrage is not modeled; funding rate dynamics are not part of the framework.
- **Funding:** Not applicable for spot DEX arbitrage.
- **24/7 session structure:** The framework assumes continuous monitoring, which aligns with 24/7 crypto markets.
- **Venue fragmentation:** This is the core of the paper — multi-chain DEX fragmentation creates the arbitrage opportunity.
- **Liquidity:** The paper uses Uniswap V3 concentrated liquidity pools; liquidity depth varies by fee tier and chain.
- **Bridge delay and risk:** Bridge delays (9s–242s) are the primary source of execution risk and MEV exposure.
- **Contract specification:** Standard ERC-20 token swaps; no exotic derivatives.
- **Timestamp / candle boundaries:** Second-level resolution for L2 data; 10-second bins for gap measurement.

## Limitations

- **Short observation window:** Primary cross-chain gap data limited to 5 trading days (Feb 22–25 and Mar 23, 2026); ETH–ARB pair limited to 28-minute overlap on Mar 23 (N=112). Gap distributions may not be representative of all market regimes. (underspecified, data gap)
- **Simulation-based strategy evaluation:** Adaptive path selection results are from calibrated simulations, not live or historical replay. Simulation assumes log-normal gap distribution calibrated from observed data but does not verify this assumption. (underspecified)
- **Calibrated cost estimates:** Per-trade costs are derived from aggregate daily chain-level data (DeFiLlama), not from actual per-trade observations. This may over- or underestimate real costs. (data gap)
- **No market impact modeling:** The agent's trades are assumed to be small enough not to move DEX prices. At realistic capital levels, this assumption may break down. (underspecified)
- **Simplified MEV attacker model:** The MEV vulnerability analysis assumes the attacker uses median-based and majority-vote heuristics. Real attackers may use more sophisticated prediction methods. (underspecified)
- **Single token pair:** Empirical analysis limited to WETH/USDC. Generalizability to other pairs is unverified. (data gap)
- **Multi-agent dynamics not modeled:** The paper acknowledges that multi-agent strategic settings with AMM-specific price impact are future work. (not independently reproduced)
- **No transaction cost stress test under extreme gas periods:** Gas fee variability (e.g., during network congestion) is not stress-tested. (data gap)

## Implementation status

No implementation in our research stack has been completed. The paper provides Algorithm 1 (adaptive cross-chain path selection) as pseudocode; no open-source implementation was identified.

## Adoption boundary

This record is research material only. It does not mean:
- The cross-chain arbitrage strategy is profitable after realistic execution costs
- The adaptive path selection algorithm outperforms in live trading
- The MEV protection tradeoff generalizes beyond the simulated environment
- Any trading, paper trading, testnet, or live deployment is authorized

## Related Wiki records

- `[[quant/defi-cross-chain-oracle-latency-speculative-liquidation-mev-2026-09-07]]` — Related DeFi MEV research but focuses on oracle latency and liquidation, not agent-driven cross-chain arbitrage.
- `[[quant/dex-cyclic-arbitrage-constant-product-amm-2026-09-01]]` — Intra-chain cyclic arbitrage in AMMs; different mechanism (within-chain vs. cross-chain).
- `[[quant/amm-lvr-jump-floor-optimal-block-time-2026-09-08]]` — AMM LVR research; related to DEX liquidity but different economic mechanism.
- `[[quant/strategy-research-record-spec-v1]]` — Schema specification.

## Sources

1. Wei Ye, Jingyan Xu, Yuanhong Wu. "When AI Agents Meet MEV: Cross-Chain Arbitrage in the Agentic Economy." arXiv preprint `arXiv:2609.17897v1 [cs.CR]`, submitted 15 Sep 2026. Published at MARBLE 2026 (7th International Conference on Mathematical Research for Blockchain Economy). https://arxiv.org/abs/2609.17897

**Author list verified against primary source:** Wei Ye (Fordham University, Dept. of Economics), Jingyan Xu (Fordham University, Dept. of Computer and Information Science), Yuanhong Wu (Fordham University, Dept. of Computer and Information Science). Exact match with arXiv landing page.

**Version/date:** v1, submitted 15 Sep 2026. Confirmed from arXiv submission history.

**Sample period:** 23,000 Uniswap V3 swap events across Ethereum, Arbitrum, and Base (Feb 22–25 and Mar 23, 2026); DeFiLlama aggregate data Sep 2025–Mar 2026. Confirmed from Section 5.1.

**Universe:** WETH/USDC pair on Uniswap V3 pools (Ethereum, Arbitrum, Base). Confirmed from Section 5.1.

**Transaction cost/slippage treatment:** Gas fees calibrated from DeFiLlama daily aggregate per-chain data; bridge fees estimated from protocol-level data; DEX swap fees included in Uniswap V3 fee tiers. Slippage not explicitly modeled as separate component. Confirmed from Sections 3.1, 5.1, and Table 1.

**Core performance numbers:** ETH–ARB mean gap 0.044% (Table 2, Section 5.2); ARB–Base mean gap 0.013% (Table 2, Section 5.2); Adaptive strategy mean profit $2,627 vs. Greedy $2,367 (Table 3, Section 5.4); MEV exposure cut >50% at ϕ≈0.4–0.6 (Table 4, Section 5.5). All cross-referenced to specific tables/sections in the primary source.

**Publication status:** Published at MARBLE 2026 conference. Peer-reviewed conference paper.
