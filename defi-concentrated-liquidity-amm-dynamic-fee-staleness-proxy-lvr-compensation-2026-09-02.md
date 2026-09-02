---
schema: strategy-research-record-v1
title: "Dynamic Fee Schedules for Concentrated Liquidity AMMs: Agent-Based LVR Compensation via Staleness-Proxy Pricing"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - amm
  - concentrated-liquidity
  - uniswap-v3
  - adverse-selection
  - lvr
  - dynamic-fees
  - agent-based-model
  - market-design
status: research-only
confidence: medium
source_as_of: 2026-06-23
sources:
  - "Daniele Maria Di Nosse and Fabrizio Lillo, 'Mitigating Adverse Selection in Concentrated Liquidity AMMs with Dynamic Fees: An Agent-Based Model Approach', arXiv preprint arXiv:2606.23070v1 [q-fin.TR], June 23, 2026. DOI: 10.48550/arXiv.2606.23070. https://arxiv.org/abs/2606.23070"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Dynamic Fee Schedules for Concentrated Liquidity AMMs: Agent-Based LVR Compensation via Staleness-Proxy Pricing

## Provenance

- **Primary Source:** Daniele Maria Di Nosse (Scuola Normale Superiore, Pisa, Italy) and Fabrizio Lillo (Scuola Normale Superiore, Pisa, Italy), "Mitigating Adverse Selection in Concentrated Liquidity AMMs with Dynamic Fees: An Agent-Based Model Approach", arXiv preprint `arXiv:2606.23070v1 [q-fin.TR]`, submitted June 23, 2026. DOI: [10.48550/arXiv.2606.23070](https://doi.org/10.48550/arXiv.2606.23070). Stable URL: https://arxiv.org/abs/2606.23070.
- **Sample/Data Period:** Heston model calibrated to Binance ETH/USD data, January 1 2023 to December 31 2023.
- **Venue:** Agent-based simulation of a Uniswap v3-style concentrated liquidity AMM pool interacting with a CEX reference market.
- **Publication Status:** arXiv preprint, June 2026.

## Economic mechanism

### Source-reported

The authors model concentrated liquidity AMMs (Uniswap v3) as automated dealer markets where fees play the role of spreads. LPs in concentrated liquidity pools face adverse selection costs formalized as Loss-Versus-Rebalancing (LVR): because AMMs execute at stale prices, informed arbitrageurs extract value when the external reference price moves. Static fee schedules are shown to be insufficient to compensate standing LPs for this stale-quote adverse selection, particularly when liquidity is concentrated.

The authors propose and evaluate dynamic fee schedules driven by two types of signal:
1. **Volatility-based:** fees that increase when realized or reference-market volatility rises.
2. **Order-flow toxicity / staleness-proxy:** fees that increase when the gap between the AMM price and the external CEX reference price grows, serving as a proxy for stale-quote risk.

The key finding is that dynamic fees improve hedged LP profitability primarily by increasing fee income in states associated with stale-price risk, rather than by reducing LVR itself. Rules that react to the contemporaneous gap between AMM price and CEX reference perform better than rules based only on recent price volatility.

### Research interpretation

The proposed mechanism is **compensation-for-adverse-selection via endogenous spread widening**: when the AMM price is stale relative to the reference market, the dynamic fee increases, making it more expensive for informed traders to extract value from the pool. This is analogous to market makers widening spreads during volatile or informationally asymmetric periods.

The economic thesis is falsifiable: if dynamic fees consistently fail to improve hedged LP profitability across multiple volatility regimes and pool configurations, the mechanism is weakened. The paper identifies an endogenous trade-off: wider fees compensate standing liquidity but reduce smart-router DEX share and, with short-lived liquidity, redirect fee income toward latency-sensitive providers.

**Component roles:**
- Regime signal: volatility or staleness-proxy (AMM-CEX price gap)
- Fee adjustment: monotone mapping from risk signal to fee level, with caps and decay
- LP position: concentrated liquidity with range selection (passive or active)
- PnL metric: hedged PnL = fees − LVR (rebalancing-relative benchmark)

## Signal

### Formation timestamp

Fee adjustment occurs at each block boundary. Agents observe the validated on-chain snapshot St = (P_DEX_t, L_t, m_t) at the beginning of each block, where m_t is the CEX mid-price from the end of the previous block. The fee is updated before swaps execute within the block.

### Lookback

- Volatility-based rules use recent price variance over a configurable window (underspecified exact window in the paper; the paper tests multiple configurations).
- Staleness-proxy rules use the contemporaneous gap between AMM price and CEX reference price at the block boundary.

### Entry (fee trigger)

Two classes of dynamic fee rules tested:
1. **Volatility-based fee:** f_t = base_fee × (1 + α × σ_realized_t), where σ_realized_t is a recent realized volatility estimate and α is a scaling parameter. The paper tests multiple α values and volatility windows.
2. **Staleness-proxy fee:** f_t = base_fee × (1 + β × |P_DEX_t − m_t| / m_t), where β is a scaling parameter. This directly penalizes the AMM-CEX price gap.

### Exit / fee decay

Fee adjustments include explicit caps (maximum fee rate) and decay mechanisms to prevent fee flicker and ensure mean reversion. The paper references deployed protocol patterns (Curve Stableswap-NG, Trader Joe Liquidity Book, Meteora DLMM, Algebra adaptive fee) as design templates.

### Holding period

N/A — this is a fee schedule mechanism, not a directional position strategy. The relevant time horizon is the block-by-block fee update cadence.

### Parameters

- base_fee: static fee rate (tested at Uniswap v3 standard levels, e.g. 0.3%, 0.05%)
- α, β: scaling parameters for volatility and staleness signals (tested across multiple values)
- Cap: maximum fee rate (tested at various levels)
- Decay: fee mean-reversion rate
- All parameters are research-proposed (ABM simulation parameters); no single optimal set is declared by the authors.

### Position sizing / range selection

The paper tests both passive LPs (fixed ranges) and active LPs (periodic range rebalancing). LPs have budgets, review clocks, and risk management. The fee schedule applies uniformly to all takers regardless of LP range choice.

## Required data

- **Instrument:** Two-asset concentrated liquidity AMM pool (token 0 / token 1, e.g. ETH/USDC)
- **Venue:** Uniswap v3-style on-chain AMM (or equivalent tick-based concentrated liquidity)
- **Reference market:** CEX mid-price (e.g. Binance ETH/USD)
- **Timeframe:** Block-by-block execution (Ethereum block time ~12s in the simulation)
- **Fields:** AMM price (P_DEX), active liquidity (L_t), CEX mid-price (m_t), LP inventory (x_t, y_t), fee revenue, swap volumes
- **Data period for calibration:** ETH/USD on Binance, January–December 2023
- **Point-in-time:** CEX mid-price is available at block boundary; AMM state is frozen during block micro-steps
- **Missing-data:** N/A for simulation; real deployment would need reliable CEX price feed and on-chain state

## Execution assumptions

- **Signal-to-order timing:** Fee is set at block boundary; swaps execute within the block using the updated fee.
- **Execution model:** Block-by-block discrete execution with mempool replay; arbitrage intents execute with priority (MEV-style ordering).
- **Fill model:** All swaps execute against live AMM state; partial fills not modeled.
- **Fees:** Taker fee is the dynamic fee f_t; LPs receive pro-rata share of fees proportional to active liquidity.
- **Slippage / spread:** AMM implicit spread is the fee; no additional explicit slippage beyond the AMM pricing curve.
- **Gas / transaction costs:** The paper discusses gas costs qualitatively but does not include gas in the primary hedged PnL metric; gas costs are noted as a practical consideration for LPs.
- **Impact:** CEX price has permanent impact from arbitrageur trades (square-root law with η_imp parameter).
- **Latency:** Mempool latency and block propagation delay are explicitly modeled; agents act on confirmed information from the previous block.
- **Leverage / margin:** Not applicable for LP positions in the simulation.

## Evidence

### Source-reported

- The paper reports simulation results from an ABM with heterogeneous agents (arbitrageurs, noise traders, MEV searchers, active and passive LPs) interacting in a Uniswap v3-style pool.
- **Key finding 1:** Under block-time execution, static fees are insufficient to compensate standing LPs for stale-quote adverse selection, especially when liquidity is concentrated. (Source-reported, simulation-based)
- **Key finding 2:** Dynamic fees can improve hedged LP profitability, but the improvement is primarily due to higher fee income rather than lower cumulative LVR. (Source-reported, simulation-based)
- **Key finding 3:** Rules reacting to the AMM-CEX price gap (staleness-proxy) perform better than volatility-only rules. (Source-reported, simulation-based)
- **Key finding 4:** Fee adaptivity creates an endogenous trade-off: compensates standing liquidity but reduces smart-router DEX share and, with short-lived liquidity, redirects fee income toward latency-sensitive providers. (Source-reported, simulation-based)
- No specific Sharpe, CAGR, or dollar PnL figures are reported for LP positions; results are presented in relative terms (hedged PnL improvement across fee policies).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The paper acknowledges that dynamic fees primarily increase fee income rather than reducing LVR itself, meaning the underlying adverse selection cost remains.
- Very short-lived LP positions may not benefit from dynamic fees if latency-sensitive providers capture the enlarged fee pool.
- The paper does not test dynamic fees against all possible LP strategies or market conditions; results are specific to the calibrated Heston parameters and agent population.

## Falsification plan

1. **Out-of-sample test:** Apply the staleness-proxy dynamic fee rule to a different time period and asset pair (e.g. WBTC/USDC on Uniswap v3) and measure hedged LP profitability relative to static fees. **Failure rule:** If hedged PnL improvement is not statistically significant across ≥3 independent 6-month windows, the mechanism is weakened.
2. **Parameter perturbation:** Vary α, β, cap, and decay parameters; if performance is fragile to parameter choice (e.g. <50% of tested parameter combinations improve hedged PnL), the mechanism is not robust.
3. **Competing explanation:** Test whether the improvement is simply due to higher average fee levels (not the dynamic component). **Ablation:** Compare a static fee set equal to the time-average dynamic fee against the dynamic fee schedule. If the static average fee performs equivalently, the dynamic component adds no value.
4. **Real-world deployment test:** Implement the staleness-proxy fee on a live or testnet Uniswap v3 fork and measure LP outcomes. **Failure rule:** If gas costs of frequent fee updates erase the hedged PnL improvement, the mechanism is not practically viable.
5. **Regime breakdown:** Test across low-volatility, high-volatility, and crash regimes separately. If the mechanism only works in specific regimes, document which and under what conditions.

## Crypto portability

**Direct** — the paper is natively about crypto AMMs (Uniswap v3 on Ethereum).

Crypto-specific considerations:
- **Block time:** The simulation uses Ethereum-like block times; faster chains (e.g. Solana, Base L2) would reduce staleness and potentially reduce the value of dynamic fees (shorter stale-price windows).
- **MEV / priority ordering:** The paper models arbitrageur priority execution; in practice, MEV-Share, Flashbots Protect, or other MEV mitigation mechanisms could alter the adversarial landscape.
- **Gas costs:** Frequent fee updates increase gas costs for the protocol; this is a material practical constraint not fully modeled in the paper.
- **Concentrated liquidity fragmentation:** Dynamic fees interact with LP range selection; LPs who concentrate more narrowly face higher staleness risk and benefit more from dynamic fees, but also face higher impermanent loss.
- **Protocol governance:** Dynamic fee implementation requires protocol-level changes (governance vote, hard fork); it cannot be implemented by individual LPs unilaterally.
- **Cross-venue:** The staleness-proxy fee depends on a reliable CEX price feed; oracle manipulation or CEX downtime could introduce false signals.

## Limitations

- **Simulation-based:** All results are from an agent-based model, not real market data. Agent behaviors are stylized; real market participants may behave differently.
- **Calibration scope:** Heston parameters calibrated to a single asset (ETH/USD) over a single year (2023). Generalization to other assets, volatility regimes, and market structures is unproven.
- **Agent population:** The paper uses a fixed set of agent types and behaviors; real AMM ecosystems have more heterogeneous and adaptive participants.
- **Gas costs:** Not fully modeled in the hedged PnL metric; practical deployment must account for gas overhead of fee updates.
- **Not independently reproduced:** Results are from a single ABM implementation; no independent replication is reported.
- **Data gap:** Exact optimal parameter values for α, β, cap, and decay are not specified; the paper explores a range of configurations without declaring a single recommendation.
- **Endogenous trade-off acknowledged:** The paper explicitly notes that dynamic fees redirect rather than eliminate adverse selection costs, and that short-lived liquidity providers may capture a disproportionate share of fee income.

## Implementation status

Not implemented. The paper provides simulation results from an agent-based model. No on-chain deployment, testnet trial, or paper trading of dynamic fee schedules is reported. The paper references deployed dynamic fee protocols (Curve Stableswap-NG, Trader Joe Liquidity Book, Meteora DLMM, Algebra adaptive fee) as design inspirations, but these are distinct implementations.

## Adoption boundary

This record represents research material only. A record being present in this repository does not mean:
- The dynamic fee mechanism is profitable;
- It has been validated as alpha;
- It is approved for implementation;
- It is approved for paper trading, testnet, or live trading.

The paper's mechanism is a protocol-level design change (fee schedule modification), not an individual LP trading strategy. Adoption would require protocol governance action or a new AMM deployment.

## Related Wiki records

- [[defi-amm-jump-diffusion-lvr-decomposition-optimal-block-time-2026-09-01]] — related LVR analysis via jump-diffusion; complementary analytical framework
- [[defi-concentrated-liquidity-stochastic-impulse-control-tail-risk-2026-09-02]] — RL-based concentrated liquidity provision; different mechanism (range optimization vs. fee optimization)
- [[crypto-dynamic-weight-amm-tfmm-dutch-reverse-auction-rebalancing-2026-09-01]] — dynamic weight AMMs; different mechanism (weight rebalancing vs. fee adjustment)
- [[defi-everlasting-options-proactive-market-making-delta-hedge-2026-09-01]] — proactive market making; related concept of compensating for adverse selection
- [[crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31]] — LVR analysis; foundational concept for this record

## Sources

1. Daniele Maria Di Nosse and Fabrizio Lillo, "Mitigating Adverse Selection in Concentrated Liquidity AMMs with Dynamic Fees: An Agent-Based Model Approach", arXiv preprint `arXiv:2606.23070v1 [q-fin.TR]`, June 23, 2026. DOI: [10.48550/arXiv.2606.23070](https://doi.org/10.48550/arXiv.2606.23070). Stable URL: https://arxiv.org/abs/2606.23070.
