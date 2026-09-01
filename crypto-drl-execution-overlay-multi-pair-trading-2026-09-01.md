---
schema: strategy-research-record-v1
title: "Deep Reinforcement Learning Execution Overlay for Multi-Pair Statistical Arbitrage in Cryptocurrency Markets"
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - pairs-trading
  - statistical-arbitrage
  - deep-reinforcement-learning
  - safe-rl
  - deterministic-shielding
status: research-only
confidence: medium
source_as_of: 2026-06-25
sources:
  - https://arxiv.org/abs/2606.04574 (arXiv:2606.04574v2, submitted 3 Jun 2026, revised 25 Jun 2026)
  - https://github.com/damianlebiedz/pair-trading-with-rl (commit 2caba40a838dbc8f7cba02348b483913b7b32821)
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Deep Reinforcement Learning Execution Overlay for Multi-Pair Statistical Arbitrage in Cryptocurrency Markets

## Provenance

- **Source:** arXiv:2606.04574v2, "Dynamic Multi-Pair Trading Strategy in Cryptocurrency Markets with Deep Reinforcement Learning"
- **Authors:** Damian Lebiedź, Robert Ślepaczuk (University of Warsaw, Faculty of Economic Sciences)
- **Submitted:** 3 June 2026; revised 25 June 2026
- **URL:** https://arxiv.org/abs/2606.04574
- **Code:** https://github.com/damianlebiedz/pair-trading-with-rl (commit SHA: 2caba40a838dbc8f7cba02348b483913b7b32821)
- **Data:** Binance USD-M Futures, 1-hour interval data
- **In-sample:** 2024; Out-of-sample: 2025
- **License:** CC BY-NC-ND 4.0

## Economic mechanism

### Source-reported

The authors propose a hybrid architecture combining classical statistical arbitrage (pair trading) with a Deep Reinforcement Learning (DRL) execution overlay. The system has two layers:

**Layer 1 — Statistical Baseline (Filter-then-Rank pair selection):**
- Hierarchical pair selection: cointegration testing → Hurst exponent filter (H < 0.5 for mean reversion) → beta coefficient constraints → performance-based ranking.
- Execution model: "Fixed Risk, Adaptive Mean" — trades a snapshot equilibrium rather than static or continuous rolling mean-reversion. Positions are entered when the spread diverges beyond a threshold and held until mean reversion or risk limit breach.

**Layer 2 — DRL Execution Overlay (PPO + LSTM):**
- A Proximal Policy Optimization (PPO) agent with Long Short-Term Memory (LSTM) architecture operates exclusively as an execution layer on top of the statistical baseline.
- The agent does NOT generate trading signals — it governs execution decisions (entry timing, exit timing, position sizing) within strict deterministic risk management boundaries ("deterministic shielding").
- This decoupling prevents the instability and overfitting common in end-to-end RL trading systems.

### Research interpretation

This is a **safe reinforcement learning approach to statistical arbitrage execution** with the following falsifiable hypotheses:

- **Execution alpha via RL:** A DRL agent can optimize trade execution timing and sizing beyond heuristic rules, adapting to changing microstructural conditions (volatility, spread dynamics, liquidity).
- **Deterministic shielding prevents divergence:** Anchoring the neural policy to statistically robust boundaries (hard stop-losses, maximum position limits) mitigates the severe divergence risks that plague traditional pair trading in volatile crypto markets.
- **Hierarchical pair selection improves robustness:** Multi-stage filtering (cointegration + Hurst + beta + performance ranking) isolates higher-conviction mean-reverting pairs than any single metric alone.
- **Regime-adaptive mean reversion:** The "Fixed Risk, Adaptive Mean" execution model absorbs structural drift and regime shifts better than static or continuous-rolling approaches.

The key innovation is the **decoupling of signal generation from execution optimization** — the statistical model identifies *what* to trade, while the RL agent optimizes *how* to trade it, within safety constraints.

## Signal

- **Pair selection:** Hierarchical Filter-then-Rank:
  1. Cointegration test (Engle-Granger two-step).
  2. Hurst exponent filter: H < 0.5 (anti-persistent / mean-reverting).
  3. Beta coefficient constraints.
  4. Performance-based ranking of surviving pairs.
- **Entry signal:** Spread divergence beyond threshold (from statistical baseline).
- **Execution decisions (RL overlay):** PPO agent with LSTM observes market state and outputs execution actions (entry/exit/hold, position size) within deterministic bounds.
- **Exit:** Mean reversion to equilibrium, or risk limit breach (hard stop).
- **Position sizing:** Deterministic risk management boundaries constrain RL agent output.
- **Lookback / observation space:** RL agent observes recent spread history, market microstructure features; exact observation space dimensions specified in the paper.
- **Reward function:** Tested multiple configurations; risk-sensitive reward functions outperform naive PnL-based rewards.
- **Holding period:** Variable — depends on spread mean reversion speed and risk limits.
- **Fully specified:** Yes — methodology is detailed with code available; however, exact RL hyperparameters and observation space dimensions require referencing the paper/code.

## Required data

- **Instruments:** Multiple cryptocurrency perpetual swap pairs on Binance USD-M Futures.
- **Venue:** Binance USD-M Futures.
- **Market type:** Perpetual swaps.
- **Timeframe:** 1-hour OHLCV candles.
- **OHLCV fields:** Open, High, Low, Close, Volume.
- **Spread data:** Derived from paired asset prices (spread = price_A − β · price_B).
- **Funding rate:** Not explicitly modeled in the paper; a gap for real-world deployment.
- **Order book / depth:** Not explicitly required by the baseline; the RL agent may benefit from microstructure features.
- **Timestamp:** Hourly candle boundaries.

## Execution assumptions

- **Signal-to-order:** Hourly execution.
- **Order type:** Market order assumed.
- **Fill model:** Assumes full fill at signal price; slippage not explicitly modeled.
- **Fees:** Not explicitly stated in the abstract; assumed included in backtesting.
- **Slippage:** Not explicitly modeled — a significant gap for high-frequency pair trading.
- **Funding rate:** Not modeled — potential source of alpha erosion for held positions.
- **Leverage:** Not explicitly stated.
- **Capacity:** Not analyzed.
- **Latency:** Not modeled.
- **Look-ahead bias:** Authors claim comprehensive elimination of look-ahead and survivorship biases.
- **Statistical significance:** OOS outperformance significant at 10% level (stationary circular block bootstrap); marginally misses the 5% threshold.

## Evidence

### Source-reported

- **Out-of-sample (2025):** The optimized RL policy achieved out-of-sample performance that "substantially outperformed the heuristic baseline."
- **Statistical significance:** Stationary circular block bootstrap confirms risk-adjusted outperformance significant at 10% level, but falls marginally short of the 5% threshold.
- **Robustness:** The authors attribute the marginal miss of the 5% threshold to "extreme idiosyncratic variance characteristic of digital assets."
- **Key finding:** The DRL overlay improves execution over the heuristic baseline, but the baseline itself (Filter-then-Rank + Fixed Risk, Adaptive Mean) is the primary driver of profitability. The RL overlay provides incremental execution optimization.

This result has not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The 10% significance level (rather than 5%) weakens the statistical case for the RL overlay's incremental value.
- The authors acknowledge that "end-to-end RL architectures frequently suffer from extreme policy instability and out-of-sample overfitting," motivating their decoupled approach — but this also means the RL agent's contribution may be modest.
- No explicit modeling of funding rate costs, slippage, or transaction costs in the reported results — these could materially erode performance in live trading.
- Single-venue study (Binance USD-M only); generalization to other venues or higher-frequency data is untested.

## Falsification plan

- **Required sample:** Replicate on independent time periods (e.g., 2024 as OOS, or cross-venue data from OKX/Bybit).
- **Relevant regimes:** Test during extreme volatility events (e.g., FTX collapse, COVID crash analogues) where pair divergence risks are highest.
- **Baseline / control:** Compare the DRL overlay against the heuristic baseline alone, simple Bollinger-band-based execution, and OU s-score-based execution.
- **Ablation tests:** Remove the RL overlay entirely to quantify its marginal contribution; test different reward functions and observation spaces.
- **Cost sensitivity:** Add realistic slippage (1–5 bps), funding rate costs (rolling 8-hour), and transaction fees to determine if the edge survives.
- **Out-of-sample requirement:** Must survive walk-forward validation, not just a single OOS window.
- **Failure metric:** RL overlay fails to outperform the heuristic baseline by >5% in Sharpe ratio over any 6-month rolling window.
- **What action follows failure:** The heuristic baseline (Filter-then-Rank + Fixed Risk, Adaptive Mean) may still be viable as a standalone strategy without the RL complexity.

## Crypto portability

direct

This strategy is natively designed for Binance USD-M perpetual futures. Crypto-specific considerations:
- Pair selection via cointegration is well-suited to crypto's high cross-asset correlation and frequent regime shifts.
- The Hurst exponent filter (H < 0.5) selects anti-persistent spreads, which is appropriate for crypto's mean-reverting microstructure.
- Funding rate costs are NOT modeled — this is a critical gap for perpetual swap strategies where funding can be 0.01%+ per 8 hours.
- The 1-hour timeframe captures intraday mean reversion but may miss higher-frequency spread dynamics.
- Deterministic shielding (hard risk limits) is particularly valuable in crypto's fat-tailed return distribution.

## Limitations

- **Not independently reproduced** — all results are source-reported.
- **Single-venue study** — Binance USD-M only.
- **No slippage or funding rate modeling** — critical gaps for real-world deployment of pair trading strategies.
- **10% significance level** — the RL overlay's incremental value is not statistically significant at the conventional 5% level.
- **61-page thesis** — the full methodology is detailed but requires significant implementation effort; the code is public but may have dependencies or configuration complexity.
- **Pair selection may be overfit** — the hierarchical Filter-then-Rank methodology involves multiple filtering stages, each of which could introduce selection bias if not carefully validated.
- **RL agent stability** — despite deterministic shielding, PPO+LSTM agents can still exhibit policy drift in non-stationary environments; long-horizon stability is not tested.
- **Data gap:** Exact RL hyperparameters, observation space composition, and reward function details require referencing the full paper and code.

## Implementation status

Not implemented in our research stack. No PyBroker, Nautilus, paper trading, testnet, or live trading has occurred.

## Adoption boundary

This record is research material only. Presence in this repository does not imply:
- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

## Related Wiki records

- [[crypto-factor-augmented-volatility-pairs-trading-2026-09-01]] (related pairs trading approach)
- [[crypto-cross-cryptocurrency-lead-lag-adaptive-lasso-10m-2026-09-01]] (related cross-asset signal)
- [[contrarian-market-making-fill-probability-order-flow-2026-09-01]] (related execution optimization)

## Sources

1. Lebiedź, D., Ślepaczuk, R. (2026). "Dynamic Multi-Pair Trading Strategy in Cryptocurrency Markets with Deep Reinforcement Learning." arXiv:2606.04574v2. https://arxiv.org/abs/2606.04574
2. GitHub repository: https://github.com/damianlebiedz/pair-trading-with-rl (commit SHA: 2caba40a838dbc8f7cba02348b483913b7b32821)
