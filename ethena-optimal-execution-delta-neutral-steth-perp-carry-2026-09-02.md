---
schema: strategy-research-record-v1
title: "Optimal Execution of Delta-Neutral stETH/Perp Carry: Ethena Yield-Bearing Stablecoin Stochastic Control"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - stablecoin
  - ethena
  - carry-trade
  - delta-neutral
  - staking
  - perpetual-futures
  - stochastic-control
  - optimal-execution
  - price-impact
status: research-only
confidence: medium
source_as_of: 2026-05-11
sources:
  - "https://arxiv.org/abs/2605.11263"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Optimal Execution of Delta-Neutral stETH/Perp Carry: Ethena Yield-Bearing Stablecoin Stochastic Control

## Provenance

- Lorig, M. (2026). "Optimal Control of the Ethena Yield-Bearing Stablecoin." arXiv preprint arXiv:2605.11263.
- Published: 2026-05-11. Category: q-fin.MF.
- URL: https://arxiv.org/abs/2605.11263

## Economic mechanism

### Source-reported

The Ethena protocol earns yield by simultaneously holding a long staked Ethereum (stETH) position and an equal-sized short position in ETH perpetual futures. This combined position is delta-neutral with respect to ETH spot price, yet earns carry from two sources: (1) staking rewards on the stETH leg, and (2) funding-rate payments received from long perpetual holders when the perpetual trades at a premium to spot. The paper formulates and solves stochastic control problems that model the optimal rate at which the protocol should simultaneously buy stETH and short the perpetual. The key modeling feature is that the control (the rate of position building/unwinding) exerts two distinct types of price impact: permanent impact that shifts mid-market prices of both legs and compresses the basis (permanently eroding future funding income), and temporary impact that reflects execution slippage on each leg. Both infinite-horizon discounted and finite-horizon (maximize wealth up to date T with terminal liquidation cost) problems are solved with explicit optimal controls.

### Research interpretation

The alpha hypothesis is that the execution timing of a delta-neutral carry trade is itself a source of alpha, independent of the carry signal. The mechanism is:

1. **Permanent price impact creates a feedback loop**: Aggressively building the carry position compresses the stETH/ETH basis and reduces the perpetual premium, permanently eroding the very yield the position is designed to capture. This creates a non-trivial optimal sizing/speed problem.
2. **Temporary impact adds execution cost**: Each rebalancing trade incurs slippage on both the stETH leg (DEX/CEX) and the perpetual leg (CEX), creating a convex cost that penalizes frequent or large trades.
3. **Optimal control resolves the tradeoff**: The explicit solution balances the marginal yield gain from a larger position against the marginal basis compression and execution cost, yielding an optimal trajectory for position building.

The alpha source is the operational efficiency — protocols or traders who optimize their entry/exit timing around this price impact structure capture more of the available carry than naive constant-rate execution.

## Signal

- **Formation timestamp**: Continuous; the optimal control prescribes a time-dependent trajectory for position building/unwinding.
- **Lookback**: The model requires estimation of permanent impact parameters (how basis compression responds to position changes) and temporary impact parameters (execution slippage per unit traded). These are estimated from market data (exact methodology in the source paper).
- **Entry (position building)**: The optimal control specifies the rate du/dt at which to simultaneously buy stETH and short ETH perpetuals at each point in time. The trajectory depends on:
  - Current position size
  - Current basis spread (stETH discount/premium + perpetual funding rate)
  - Permanent impact parameters
  - Temporary impact parameters
  - Discount rate (infinite horizon) or time-to-horizon (finite horizon)
- **Exit (position unwinding)**: In the finite-horizon formulation, the protocol maximizes total wealth up to date T, subject to a terminal cost for liquidating the remaining position. The optimal unwinding trajectory is the time-reverse of the building trajectory (under symmetric impact assumptions).
- **Holding period**: Determined by the optimization horizon T; the infinite-horizon formulation yields a steady-state optimal position size.
- **Parameters**:
  - Permanent impact coefficient (how much basis compresses per unit of position change)
  - Temporary impact coefficient (slippage per unit of trade size)
  - Staking rate (annualized stETH yield)
  - Funding rate (perpetual funding rate)
  - Discount rate
  - Terminal liquidation cost (finite horizon)
- **Underspecified items**: Exact numerical values for impact coefficients are not provided in the abstract; the source paper contains the derivations. The model assumes continuous-time dynamics which may not match discrete on-chain execution. Research-proposed: the assumption that permanent and temporary impact are linear/quadratic (standard in market microstructure but unverified for these specific instruments).

## Required data

- **Instrument**: stETH (staked Ethereum) and ETH perpetual futures (e.g., on Binance, Bybit, or other major CEX).
- **Venue**: stETH available on DEXs (Curve, Uniswap) and some CEXs; perpetual futures on major CEXs.
- **Market type**: Spot (stETH) + perpetual futures.
- **Timeframe**: High-frequency data for impact estimation; daily or hourly for carry monitoring.
- **Fields**: stETH/ETH spot price, ETH perpetual mark/index price, perpetual funding rate, staking rate, order book depth on both legs, trade execution data.
- **Point-in-time**: Funding rate and staking rate must be observed in real-time; basis data must be current.
- **Timestamp**: UTC, sub-second precision for impact estimation.
- **Missing-data**: stETH liquidity on DEXs can be thin; perpetual funding rates are observed only at discrete intervals (every 8h on most CEXs).

## Execution assumptions

- **Order type**: Market orders on both legs (stETH purchase on DEX/CEX, perpetual short on CEX).
- **Fill model**: Continuous-time model; actual execution is discrete (block-level for stETH, order-book for perpetuals).
- **Latency**: DEX execution subject to block time (12s Ethereum); CEX execution near-instantaneous.
- **Signal-to-order delay**: The optimal control is a trajectory, not a discrete signal; execution follows the prescribed rate.
- **Fees**: DEX swap fees for stETH acquisition; maker/taker fees for perpetual shorting; funding rate payments.
- **Slippage**: Explicitly modeled as temporary impact; the optimal control accounts for this.
- **Impact / capacity**: Permanent impact is the core constraint — larger positions compress the basis and reduce yield. This is the paper's central contribution.
- **Leverage / margin**: The perpetual short requires margin; the stETH position may be used as collateral.
- **Failure handling**: Not explicitly modeled; in practice, liquidation of the perpetual short is a risk if ETH price moves sharply against the position (though the position is delta-neutral, basis moves can cause PnL volatility).

## Evidence

### Source-reported

- The paper derives explicit optimal controls for both infinite-horizon and finite-horizon formulations.
- The key result is that permanent price impact creates a fundamental tradeoff: larger positions earn more carry but compress the basis, reducing per-unit yield. The optimal trajectory balances these effects.
- Source reports analytical solutions; no empirical backtest or live trading results are provided in the abstract.
- Source quality: single-author working paper from an academic researcher; not peer-reviewed at time of publication.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The model assumes continuous-time dynamics; actual on-chain and CEX execution is discrete and may deviate from the optimal trajectory.
- Permanent impact parameters are estimated from historical data; if market microstructure changes (e.g., new entrants, liquidity shifts), the estimated parameters may become stale.
- The model does not account for smart contract risk, staking withdrawal delays, or exchange counterparty risk.
- Ethena's actual protocol may not follow the optimal trajectory due to governance constraints, deposit/withdrawal queues, or other operational factors.

## Falsification plan

1. **Parameter sensitivity**: Vary permanent and temporary impact coefficients across plausible ranges; if the optimal trajectory changes qualitatively (e.g., from gradual building to immediate full position), the model's practical value is questionable.
2. **Backtest against naive execution**: Implement the optimal trajectory and compare against a constant-rate (dollar-cost averaging) approach on historical stETH/ETH basis and funding rate data. If the optimal trajectory does not materially outperform after fees, the alpha from optimal execution is falsified.
3. **Regime test**: Evaluate during periods of extreme basis compression (e.g., negative funding rates) and extreme basis expansion (e.g., bull market premium) to verify the model handles both regimes.
4. **Capacity test**: Determine at what position size the permanent impact becomes dominant (yield approaches zero); this defines the practical capacity of the strategy.
5. **Failure threshold**: If the optimal trajectory net carry (after all impact and fees) is within 10% of naive DCA, the execution alpha is negligible.

## Crypto portability

- **Direct**: The strategy is native to crypto markets (stETH + ETH perpetual carry).
- **Protocol-specific**: Tuned for Ethena's specific structure; other staking+perp carry strategies (e.g., different LSTs, different perp venues) require re-estimation of impact parameters.
- **Funding rate dependency**: The strategy's viability depends on the perpetual trading at a premium to spot (positive funding rate); during prolonged negative funding periods, the carry reverses.
- **Staking rate risk**: stETH staking rate can change with network conditions; the model treats it as a known parameter.
- **24/7**: Perpetual futures trade 24/7; stETH staking is continuous; DEX execution is always available.

## Limitations

- Analytical solutions only; no empirical backtest or live trading evidence in the paper.
- Continuous-time model may not match discrete on-chain execution.
- Permanent impact parameters are model-dependent estimates, not directly observable.
- Does not account for smart contract risk, staking withdrawal queues, or exchange counterparty risk.
- Funding rate regime risk: the strategy loses when perpetuals trade at a discount (negative funding).
- Not independently reproduced.
- Source quality: single-author working paper; not peer-reviewed at time of publication.

## Implementation status

Not implemented. The paper provides analytical solutions only; no backtest, paper trading, or live deployment evidence exists.

## Adoption boundary

This record is research material only. It does not indicate profitability, validated alpha, or authorization for implementation, paper trading, testnet, or live deployment.

## Related Wiki records

No related records found in Wiki Brain.

## Sources

- Lorig, M. (2026). "Optimal Control of the Ethena Yield-Bearing Stablecoin." arXiv:2605.11263. URL: https://arxiv.org/abs/2605.11263. Published 2026-05-11.
