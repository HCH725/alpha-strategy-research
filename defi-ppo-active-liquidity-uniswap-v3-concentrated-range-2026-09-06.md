---
schema: strategy-research-record-v1
title: "PPO-Based Active Liquidity Provision in Uniswap v3 Concentrated Liquidity AMM"
created: 2026-09-06
updated: 2026-09-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - uniswap-v3
  - concentrated-liquidity
  - reinforcement-learning
  - PPO
  - active-liquidity-management
  - impermanent-loss-mitigation
  - LVR
status: research-only
confidence: medium
source_as_of: 2025-01-13
sources:
  - "Xu, H. and Brini, A. (2025). Improving DeFi Accessibility through Efficient Liquidity Provisioning with Deep Reinforcement Learning. arXiv:2501.07508v1 [q-fin.CP]. Accepted at AI for Social Impact Workshop, AAAI 2025. https://arxiv.org/abs/2501.07508"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# PPO-Based Active Liquidity Provision in Uniswap v3 Concentrated Liquidity AMM

## Provenance

- **Source:** arXiv:2501.07508v1
- **URL:** https://arxiv.org/abs/2501.07508
- **PDF:** https://arxiv.org/pdf/2501.07508
- **Authors:** Haonan Xu, Alessio Brini (Pratt School of Engineering, Duke University, Durham, NC, USA)
- **Submitted:** 13 January 2025 (v1)
- **Published:** Accepted at AI for Social Impact: Bridging Innovations in Finance, Social Media, and Crime Prevention Workshop, AAAI 2025
- **Sample period:** Hourly data from 5 May 2021 (Uniswap v3 inception) to 29 January 2024
- **Universe:** WETH/USDC Uniswap v3 pool, 0.05% fee tier (Ethereum mainnet, contract 0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640)
- **Market type:** On-chain AMM (Uniswap v3 concentrated liquidity)
- **Data source:** Uniswap Ethereum Subgraph, resampled to hourly series

## Economic mechanism

### Source-reported

Uniswap v3's concentrated liquidity model allows LPs to specify narrow price ranges, improving capital efficiency but intensifying impermanent loss (IL) when prices move outside the range. Passive LP strategies (periodic fixed-interval rebalancing) suffer from unnecessary rebalancing costs during stationary periods and inactive positions during trending periods. The authors propose a PPO-based active LP agent that dynamically adjusts the liquidity price range and rebalancing frequency based on market conditions, balancing fee collection against LVR (Loss-Versus-Rebalancing) and gas costs.

### Research interpretation

The hypothesized alpha mechanism is **adaptive range management under gas-cost friction**: an RL agent that learns to widen ranges during trending periods (reducing rebalancing frequency and gas costs) and narrow ranges during stationary periods (maximizing fee capture per unit of liquidity). The reward function penalizes LVR as an opportunity cost (the cost of not holding a hedged portfolio on a CEX), gas fees for position modifications, and rewards trading fees earned. The agent's edge comes from regime-dependent optimization of the rebalancing frequency and range width, rather than from a directional price forecast. This is a market-making / liquidity provision alpha, not a directional trading alpha.

## Signal

### Formation timestamp
- Formed at each discrete hourly step; decision is whether to maintain current price range or withdraw and redeploy at a new symmetric range centered on the current AMM spot price.

### Lookback
- State space includes: current price, tick index, interval width, liquidity level, exponentially weighted volatility (smoothing factor α = 0.05), 24-hour and 168-hour moving averages, and technical indicators (Bollinger Bands, ADXR, BOP, DX).
- Rolling window training: 7,500 hours (~10 months) training, 1,500 hours (~2 months) out-of-sample testing, shifted by 1,500 hours per iteration.

### Long entry / short entry
- Not applicable in the directional sense. The agent decides between:
  - **Action 0:** Maintain current position (no gas cost, no range change).
  - **Actions 1–4:** Withdraw and redeploy at a new symmetric price range with a specific tick width (hyperparameter-optimized per window).

### Exit
- Position is maintained until the agent chooses a different action at a subsequent hourly step. No explicit time-based exit; the agent learns when to rebalance.

### Holding period
- Variable; the agent may hold a position for hours to months depending on learned policy. No fixed holding period.

### Parameters
- Action space (interval width in ticks): optimized per rolling window via grid search over 50 agents per window. Example values: [0, 20, 50], [0, 10, 20], [0, 40, 50, 60], [0, 50, 100].
- PPO hyperparameters: learning rate (0.00001–0.01), clip range (0.05–0.4), entropy coefficient (0.00001–0.01), discount factor (0.9–0.9999). All optimized per window.
- Neural network: 2–3 hidden layers, sizes 2–10, activation function (sigmoid/relu/tanh) optimized per window.
- Gas fee: fixed at $5 per position modification (based on Etherscan gas tracker).
- Initial liquidity: x₀ = 2 (risky token quantity); also tested at x₀ = 10.
- **All parameters are research-defined (hyperparameter-optimized per window), not source-proven optimal values.**

### Position-sizing logic
- Fixed initial liquidity (x₀ = 2 or x₀ = 10); no dynamic sizing.

## Required data

- **Instrument:** WETH/USDC Uniswap v3 pool (0.05% fee tier)
- **Venue:** Uniswap v3 on Ethereum mainnet
- **Market type:** On-chain AMM (concentrated liquidity)
- **Timeframe:** Hourly OHLCV resampled from transaction data
- **Fields:** Price, tick index, liquidity level, gas fees (from Etherscan), trading fees
- **Point-in-time:** Uniswap Subgraph data; gas fees from Etherscan at time of deployment
- **Missing-data:** Hourly resampling of unevenly spaced transactions may introduce aggregation artifacts; exact methodology for resampling not specified in detail.

## Execution assumptions

- **Signal-to-order timing:** Decision at hourly intervals; position modification assumed to execute at current AMM spot price.
- **Fill model:** Full fill assumed (no partial fills modeled).
- **Fees:** 0.05% fee tier; trading fees accrued per the Uniswap v3 fee formula (Eqns. 5–6 in paper).
- **Slippage:** Not explicitly modeled for LP position entry/exit; implicit in the AMM pricing curve.
- **Gas fees:** Fixed $5 per position modification (withdrawal + redeployment counted as two gas events).
- **LVR:** Modeled as an opportunity cost penalty in the reward function, using the instantaneous LVR formula from Milionis et al. (2023) with exponentially weighted volatility.
- **Funding / leverage:** Not applicable (no perpetual futures or leverage).
- **Latency:** Hourly decision granularity; no sub-hour latency considerations.
- **MEV / sandwich attacks:** Not modeled. This is a significant omission for on-chain strategies.
- **Impact / capacity:** Not assessed; the strategy assumes the LP's position is small relative to pool depth.

## Evidence

### Source-reported

Active LP outperforms passive LP in **7 out of 11 out-of-sample windows** (x₀ = 2):

| Test End Date | Active LP Reward | Passive LP Reward |
|---|---|---|
| 2022-05-14 | 17,893.42 | 1,555.46 |
| 2022-07-16 | 1,546.03 | −1,973.24 |
| 2022-09-16 | 834.13 | −493.90 |
| 2022-11-18 | 3,160.38 | 2,179.77 |
| 2023-01-19 | 3,745.15 | 1,149.32 |
| 2023-03-23 | 4,953.87 | 4,964.50 |
| 2023-05-24 | 3,066.13 | 4,939.25 |
| 2023-07-26 | 6,143.00 | 3,940.10 |
| 2023-09-26 | 4,709.66 | 6,047.50 |
| 2023-11-28 | 1,356.69 | 4,629.40 |
| 2024-01-29 | 6,552.42 | 5,780.83 |

At x₀ = 10, the active LP also outperforms in 7 out of 11 windows. The reward metric is cumulative reward (fees − LVR − gas), denominated in the paper's internal unit (not USD). The passive LP uses a fixed 500-hour (~20 day) rebalancing interval with a 50-tick range width. No Sharpe ratio, win rate, or other standard risk-adjusted metrics are reported.

Source reports that the agent learns to widen ranges during trending periods and narrow during stationary periods, and to maintain inactive positions when anticipating mean reversion. This result has not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Active LP loses in 4 out of 11 windows, including periods where the passive LP significantly outperforms (e.g., 2023-03-23, 2023-05-24, 2023-09-26, 2023-11-28).
- Performance is highly variable across windows: rewards range from 834 to 17,893 for the active LP.
- The passive LP outperforms in windows with strong trending or sustained mean-reverting behavior where the simple rebalancing heuristic happens to align with market dynamics.
- No risk-adjusted metrics (Sharpe, Sortino, max drawdown) are reported, making it impossible to assess whether the active LP's outperformance is risk-adjusted.
- Hyperparameter optimization per window (50 agents per window) introduces potential look-ahead bias in the selection of the best agent, even though each window uses a separate train/test split.

## Falsification plan

1. **Out-of-sample generalization:** Test the trained agent on pools other than WETH/USDC (e.g., WBTC/USDC, ETH/USDT) and on different fee tiers (0.01%, 0.3%, 1%). If the agent's advantage disappears on other pools, the effect may be pool-specific.
2. **Regime robustness:** Evaluate performance across distinct market regimes (e.g., sustained bull, sustained bear, high-volatility chop). The 4 losing windows suggest regime dependency.
3. **Ablation of state components:** Remove technical indicators (BB, ADXR, BOP, DX) from the state space to test whether the agent's edge comes from price dynamics alone or from the indicators.
4. **Transaction cost sensitivity:** Vary gas fees from $1 to $20; if the strategy becomes unprofitable at moderate gas levels, the edge is gas-cost-sensitive.
5. **MEV exposure:** Model sandwich attacks and front-running; if the agent's rebalancing transactions are consistently sandwiched, the edge may be illusory in production.
6. **Compare against simple heuristics:** Test whether a rule-based strategy (e.g., rebalance when price moves N% outside range, or rebalance at fixed intervals with volatility-adaptive width) achieves comparable performance without the complexity of DRL.
7. **Failure threshold:** If the active LP fails to outperform in more than 5 out of 11 windows on a held-out pool, the hypothesis is materially weakened.

## Crypto portability

**Adapted**

The strategy is native to Uniswap v3 on Ethereum mainnet. Portability to other concentrated-liquidity DEXs (e.g., Camelot on Arbitrum, Aerodrome on Base, Raydium on Solana) requires:
- Recalibration of gas fee assumptions (different chains have different gas costs).
- Recalibration of LVR dynamics (different pool depths, fee tiers, and trading volumes).
- Potential changes to tick spacing and price range mechanics (some CLMMs use different tick conventions).
- MEV environment differs significantly across chains (e.g., Solana has different MEV dynamics than Ethereum).
- Funding rate dynamics do not apply (this is a spot AMM strategy, not a perpetual futures strategy).

The strategy does not apply to order-book-based DEXs (e.g., dYdX, Serum).

## Limitations

- **Synthetic simulation only:** No live or paper trading results; all backtests are simulated.
- **Code not released:** "Code will be made available upon acceptance in a GitHub repository" — as of the arXiv publication, code is not available.
- **Single pool tested:** Only WETH/USDC on the 0.05% fee tier.
- **No risk-adjusted metrics:** No Sharpe ratio, Sortino ratio, max drawdown, or Calmar ratio reported.
- **Hyperparameter optimization per window:** 50 agents trained per window, best selected — this is computationally expensive and may introduce selection bias.
- **MEV not modeled:** On-chain transactions are subject to sandwich attacks and front-running, which could erode the active LP's edge.
- **No slippage model for LP entry/exit:** The paper assumes LP position modifications execute at the current spot price without modeling the actual execution slippage.
- **Passive baseline is weak:** The passive LP uses a fixed 500-hour rebalancing interval and fixed 50-tick width, which is a simple heuristic. A more sophisticated passive strategy (e.g., volatility-adaptive fixed-interval) might be a harder baseline.
- **Reward metric is paper-specific:** The cumulative reward metric (fees − LVR − gas) is denominated in internal units, not USD, making cross-study comparison difficult.
- **Data gap:** The paper does not specify the exact methodology for resampling unevenly spaced transaction data into hourly bars, which could introduce aggregation artifacts.

## Implementation status

not-implemented. No implementation in our research stack. The paper's code has not been released as of the arXiv publication date.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

The strategy involves on-chain execution with real gas costs and MEV exposure, which are not captured in the simulation.

## Related Wiki records

- [[quant/crypto-clmm-path-dependent-liquidity-provision-win-score-early-exit-2026-09-02]] — Path-dependent PnL analysis of CLMM LP positions (distinct: analytical framework, not DRL)
- [[quant/defi-amm-amortizing-perpetual-options-lvr-hedge-2026-09-01]] — LVR decomposition and hedging in AMMs (distinct: hedging focus, not active LP management)

## Sources

1. Xu, H. and Brini, A. (2025). Improving DeFi Accessibility through Efficient Liquidity Provisioning with Deep Reinforcement Learning. arXiv:2501.07508v1 [q-fin.CP]. Accepted at AI for Social Impact Workshop, AAAI 2025. https://arxiv.org/abs/2501.07508
