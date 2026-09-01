---
schema: strategy-research-record-v1
title: Priority Gas Auctions (PGAs) and Latency-Competitive Arbitrage in Decentralized Exchanges
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - defi
  - dex
  - mev
  - priority-gas-auctions
  - latency-arbitrage
  - order-flow
status: research-only
confidence: high
source_as_of: 2020-05
sources:
  - https://doi.org/10.1109/SP40000.2020.00040
  - https://arxiv.org/abs/1904.05234
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Priority Gas Auctions (PGAs) and Latency-Competitive Arbitrage in Decentralized Exchanges

## Provenance

- **Primary peer-reviewed source:** Philip Daian, Steven Goldfeder, Tyler Kell, Yan Ji, Xingte Zhao, Iddo Bentov, Lorenz Breidenbach, and Ari Juels, "Flash Boys 2.0: Frontrunning, Transaction Reordering, and Consensus Instability in Decentralized Exchanges", *2020 IEEE Symposium on Security and Privacy (SP)*, San Francisco, CA, USA, May 2020, pp. 910–927. DOI: https://doi.org/10.1109/SP40000.2020.00040.
- **Preprint version:** arXiv preprint arXiv:1904.05234 (April 2019 / revised 2020). URL: https://arxiv.org/abs/1904.05234.
- **Empirical scope:** Real-time peer-to-peer network monitoring across 6 global geographic node deployments capturing Ethereum mempool propagation, smart contract state transitions, and high-frequency trading bot activities across decentralized exchanges (EtherDelta, Uniswap, Bancor, Kyber Network, IDEX) from 2018 through 2019.
- **Dataset:** Over 500,000 empirical Priority Gas Auction (PGA) bidding sequences, transaction replacement chains, and cross-DEX cyclic arbitrage executions.

## Economic mechanism

### Source-reported

Daian et al. (2020) empirically identify and formally model the mechanics of **Miner Extractable Value (MEV)** and **Priority Gas Auctions (PGAs)** in blockchain ecosystems:

1. **State-Transition Arbitrage Opportunities:** Decentralized exchanges (DEXes) execute trades asynchronously when transactions are included in blocks. When price discrepancies arise across different DEX liquidity pools (e.g., constant product AMMs vs order-book DEXes) or between off-chain centralized exchanges and on-chain pools, a deterministic profit opportunity $V > 0$ exists for the first transaction that executes the rebalancing trade.
2. **Priority Gas Auctions (PGAs):** Because miners order transactions within a block in descending order of gas price (in Gwei) to maximize fee revenue, multiple competing trading bots detecting the same opportunity engage in dynamic, real-time bidding wars in the public mempool.
3. **Auction Dynamics:** Competing bots continuously monitor rival transactions in the mempool and issue replacement transactions with identical nonces and escalating gas prices ($g_{k+1} > g_k$). Daian et al. model this as a continuous-time/discrete-round game where bots bid a fraction $\alpha \in (0, 1)$ of the expected gross profit $V$ to guarantee prioritized execution.
4. **Latency & Efficiency:** Reaction latencies among top arbitrage bots dropped below 100 milliseconds, and bots routinely bid over 70%–95% of expected gross revenue to miners to win contested arbitrage opportunities.

### Research interpretation

This is an ultra-high-frequency, latency-driven on-chain microstructure alpha strategy:

1. **Mempool Alpha Vector:** The core predictive edge is not statistical price forecasting, but rather sub-second detection and simulation of pending state changes (pending user swaps, oracle updates, and cross-pool price dislocations) before block confirmation.
2. **Game-Theoretic Gas Escalation:** The strategy formulates an optimal dynamic gas pricing rule that maximizes net expected profit:
   $$\max_{g} \mathbb{P}(\text{Win} \mid g, \text{Latency}) \cdot (V - g \cdot \text{GasUsed}) - \mathbb{P}(\text{Lose} \mid g, \text{Latency}) \cdot \text{Cost}_{\text{revert}}$$
3. **Evolution to Modern MEV:** While original PGAs occurred directly in the public peer-to-peer mempool, the economic principles directly underpin modern private builder auctions (e.g., Flashbots MEV-Boost, SUAVE, and L2 sequencing bundles), where the bidding war occurs via direct builder tips rather than public gas replacements.

## Signal

### Mathematical Specification

1. **Arbitrage Payoff Valuation:**
   For a candidate cross-DEX path $\mathcal{P} = (T_1, \dots, T_m)$ involving pools $P_1, \dots, P_k$:
   $$V(\Delta x) = \text{OutputAmount}(\mathcal{P}, \Delta x) - \Delta x$$
   Determine the optimal trade size $\Delta x^*$ by solving:
   $$\Delta x^* = \arg\max_{\Delta x > 0} V(\Delta x)$$
   Let $V^* = V(\Delta x^*)$ denote the gross extractable value in ETH.

2. **PGA Competitive Bidding Rule:**
   Let $g_{\text{rival}}$ denote the highest gas price observed from a competing bot for the same state-transition opportunity.
   Let $\Delta g_{\text{min}}$ denote the minimum replacement increment required by the network (e.g., +10% over existing gas price).
   
   Define the target bid gas price $g_{\text{bid}}$:
   $$g_{\text{bid}} = \min\left(g_{\text{rival}} + \Delta g_{\text{step}}, \; \frac{V^* \cdot (1 - \mu_{\text{margin}})}{\text{GasUsed}}\right)$$
   where $\mu_{\text{margin}}$ is the minimum acceptable profit retention margin (e.g., $\mu_{\text{margin}} = 0.05$ to $0.10$).

3. **Execution Decision:**
   - Submit bid transaction $T_{\text{bid}}$ if:
     $$g_{\text{bid}} \cdot \text{GasUsed} \le V^* - \Pi_{\text{min}}$$
     where $\Pi_{\text{min}}$ is the minimum required absolute net profit threshold.
   - If rival bids exceed the breakeven gas price:
     $$g_{\text{rival}} \ge \frac{V^* - \Pi_{\text{min}}}{\text{GasUsed}}$$
     cancel or drop the bidding war to avoid paying unprofitable execution costs.

### Normalized Pseudocode

```python
import dataclasses
from typing import Optional

@dataclasses.dataclass
class PgaBidDecision:
    should_bid: bool
    target_gas_price_gwei: float
    expected_profit_eth: float
    bid_replacement_count: int

def evaluate_pga_bid(
    gross_extractable_value_eth: float,
    estimated_gas_used: int,
    highest_rival_gas_gwei: float,
    current_bot_gas_gwei: float,
    min_replacement_pct: float = 0.10,    # +10% mempool replacement rule
    min_margin_pct: float = 0.05,          # Retain at least 5% of gross profit
    min_net_profit_eth: float = 0.005,     # Absolute minimum profit hurdle
    max_bidding_rounds: int = 10,
    current_round: int = 0
) -> PgaBidDecision:
    """
    Computes optimal gas price bid in a Priority Gas Auction (PGA)
    for decentralized exchange arbitrage.
    """
    # 1. Compute maximum allowable gas price in Gwei
    max_allowable_cost_eth = gross_extractable_value_eth * (1.0 - min_margin_pct) - min_net_profit_eth
    if max_allowable_cost_eth <= 0:
        return PgaBidDecision(False, 0.0, 0.0, current_round)
        
    max_gas_price_gwei = (max_allowable_cost_eth * 1e9) / estimated_gas_used
    
    # 2. Determine target rival gas price to beat
    if highest_rival_gas_gwei <= 0:
        # First-mover bid: baseline network gas price
        target_bid_gwei = 30.0
    else:
        # Escalation: outbid rival by at least replacement percentage
        target_bid_gwei = highest_rival_gas_gwei * (1.0 + min_replacement_pct)
        
    # 3. Check feasibility against profitability ceiling
    if target_bid_gwei > max_gas_price_gwei or current_round >= max_bidding_rounds:
        return PgaBidDecision(False, current_bot_gas_gwei, 0.0, current_round)
        
    # 4. Compute expected net profit
    total_gas_cost_eth = (target_bid_gwei * 1e-9) * estimated_gas_used
    net_profit_eth = gross_extractable_value_eth - total_gas_cost_eth
    
    return PgaBidDecision(
        should_bid=True,
        target_gas_price_gwei=target_bid_gwei,
        expected_profit_eth=net_profit_eth,
        bid_replacement_count=current_round + 1
    )
```

## Required data

- **P2P Mempool Feed:** Ultra-low latency Ethereum/EVM node connections peering with global mining/validator pools.
- **DEX Pool State:** Real-time synchronized smart contract storage states for Uniswap (v2/v3/v4), Curve, Balancer, and hybrid AMM pools.
- **Pending Transaction Stream:** Full transaction payloads in mempool with decoded function signatures (`swap`, `multicall`, `execute`).
- **Gas Dynamics:** Base fee tracker (EIP-1559), pending transaction gas price histograms, and block builder bundle submission APIs.

## Execution assumptions

- **Transaction Atomicity:** Arbitrage must be executed via custom smart contract with strictly enforced assertion checks (`require(finalBalance >= initialBalance + minProfit)`), ensuring automatic revert if frontrun or if prices move adversely.
- **Replacement Semantics:** High-frequency transaction replacement requires managing identical account nonces with rapid gas price increases to overwrite pending transactions in miners' mempools.
- **Node Infrastructure:** Multi-region geographically distributed nodes to minimize peer-to-peer propagation delay.

## Evidence

### Source-reported

- Daian et al. (2020) empirically analyzed over 500,000 PGA bidding rounds on Ethereum across 2018–2019:
  - Documented that automated bots competed fiercely for deterministic DEX arbitrage, driving gas prices into intense multi-round escalations within seconds.
  - Bots frequently transferred 70% to >90% of total arbitrage revenue to miners in the form of transaction fees.
  - Demonstrated that the median reaction time of top bots dropped from multiple seconds to sub-100 milliseconds, establishing a high-frequency latency arms race in blockchain mempools.
  - Demonstrated the risk of "Time-Bandit attacks" where miners are economically incentivized to rewrite historical blocks if accumulated MEV exceeds block subsidy rewards.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Mempool Frontrunning & Bribe Compression:** Public mempool PGAs create severe negative externalities (failed transaction costs, network congestion). As a result, the ecosystem largely transitioned to private builder order flows (Flashbots / MEV-Boost).
- **Searcher Margin Erosion:** In modern builder auctions, searchers routinely bid 95%–99% of total extracted value to block builders, leaving minimal residual margin for the searcher.
- **Reverted Transaction Fees:** If a competing transaction is mined ahead and the fallback contract lacks proper simulation, the searcher pays full gas costs for a reverted transaction with zero revenue.

## Falsification plan

1. **Mempool Simulation Backtesting:** Replay historical Ethereum/Arbitrum mempool traces (2022–2026) through an EVM state simulator.
2. **Auction Profitability Measurement:** Track net extracted profit after subtracting all winning builder tips and failed transaction gas costs.
3. **Falsification Criteria:** Reject the standalone alpha thesis if:
   - Median residual searcher margin falls below 2% of gross extracted value over a 30-day evaluation window.
   - Total gas expenditure from dropped/reverted transactions exceeds cumulative gross profits.

## Crypto portability

direct

Natively conceived and empirically observed directly within decentralized exchange smart contracts and EVM blockchain mempools. Directly applicable across Ethereum, Arbitrum, Optimism, Base, Binance Smart Chain, and other EVM-compatible ecosystems.

## Limitations

- **Not independently reproduced.**
- **Infrastructure Overhead:** Requires dedicated, high-performance node infrastructure and direct builder connections.
- **Zero-Sum Latency Arms Race:** Performance is highly sensitive to milliseconds of mempool propagation delay.
- **Contract Revert Risk:** Failed execution attempts risk incurring gas costs unless routed through private simulation bundles.

## Implementation status

Research-only. No PyBroker, NautilusTrader, paper, testnet, or live trading implementation has been completed.

## Adoption boundary

This record is staging-layer research material only. It does not constitute an implementation directive or approval for paper, testnet, or live deployment.

## Related Wiki records

- `dex-cyclic-arbitrage-constant-product-amm-2026-09-01`
- `defi-lending-collateral-liquidation-discount-arbitrage-2026-09-01`
- `crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31`
- `crypto-uniswap-v3-just-in-time-jit-liquidity-provision-price-impact-2026-09-01`

## Sources

1. Daian, Philip; Goldfeder, Steven; Kell, Tyler; Ji, Yan; Zhao, Xingte; Bentov, Iddo; Breidenbach, Lorenz; Juels, Ari. "Flash Boys 2.0: Frontrunning, Transaction Reordering, and Consensus Instability in Decentralized Exchanges." *2020 IEEE Symposium on Security and Privacy (SP)*, San Francisco, CA, USA, May 2020, pp. 910–927. DOI: https://doi.org/10.1109/SP40000.2020.00040
2. Daian, Philip; Goldfeder, Steven; Kell, Tyler; Ji, Yan; Zhao, Xingte; Bentov, Iddo; Breidenbach, Lorenz; Juels, Ari. "Flash Boys 2.0: Frontrunning, Transaction Reordering, and Consensus Instability in Decentralized Exchanges." *arXiv preprint arXiv:1904.05234* (2019/2020). URL: https://arxiv.org/abs/1904.05234
