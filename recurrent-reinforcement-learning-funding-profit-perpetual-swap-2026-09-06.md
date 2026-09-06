---
schema: strategy-research-record-v1
title: "Recurrent Reinforcement Learning Funding-Profit Capture on Crypto Perpetual Swaps"
created: 2026-09-06
updated: 2026-09-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - reinforcement-learning
  - funding-rate
  - echo-state-network
  - online-learning
  - market-microstructure
status: research-only
confidence: medium
source_as_of: 2022-05-21
sources:
  - "Borrageiro, G., Firoozye, N., & Barucca, P. (2022). 'The Recurrent Reinforcement Learning Crypto Agent.' IEEE Access, vol. 10, pp. 38590–38599. arXiv:2201.04699v4 [cs.LG]. https://arxiv.org/abs/2201.04699"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Recurrent Reinforcement Learning Funding-Profit Capture on Crypto Perpetual Swaps

## Provenance

- **Authors**: Gabriel Borrageiro (University College London / BlueCrest Capital), Nick Firoozye (University College London / Exos Bank), Paolo Barucca (University College London)
- **Publication**: IEEE Access, vol. 10, pp. 38590–38599, 2022
- **arXiv**: 2201.04699v4 [cs.LG]
- **DOI**: 10.1109/ACCESS.2022.3166599
- **Source type**: Peer-reviewed journal article
- **Sample period**: Approximately 2017–2021 (~5 years, 1684 daily observations)
- **Universe**: Single instrument: XBTUSD (Bitcoin vs US Dollar) perpetual swap on BitMEX
- **Data frequency**: 5-minute sampled intraday data (525,600 observations)

## Economic mechanism

### Source-reported

The authors propose a meta-model combining an Echo State Network (ESN) as a dynamic reservoir feature space with a Direct Recurrent Reinforcement Learning (DRRL) agent. The ESN processes order book, trade, and funding information into a high-dimensional feature representation. The DRRL agent then learns to target a position that maximizes a quadratic utility function of expected return minus risk. Critically, the net return decomposition explicitly includes funding cost/profit as a component (equation 8: rt = Δpt·ft−1 − δt|Δft| − κt·ft), meaning the agent learns to capture funding profit as a source of return. The authors report that 71% of the cumulative 350% total return comes from funding profit.

### Research interpretation

The core alpha hypothesis is that funding rate dynamics on perpetual swaps represent a learnable, systematic return component. In crypto perpetual markets, longs pay shorts when the funding rate is positive (contango/backwardation regime), and shorts pay longs when negative. The agent learns to dynamically size positions based on the interaction between funding rates, price movements, and transaction costs. This is distinct from simple funding-rate carry strategies because:

1. The agent uses a continuous position function (tanh output) rather than binary long/short signals
2. It learns from multiple sources of impact on PnL simultaneously (price moves, execution costs, funding)
3. It uses online learning to adapt to non-stationary funding dynamics

The mechanism could be decomposed as:
- **Regime detection**: implicit — the agent learns when funding dynamics favor long vs short positioning
- **Position sizing**: dynamic, learned via quadratic utility optimization
- **Funding capture**: systematic extraction of the funding rate as a return component
- **Risk management**: quadratic utility naturally penalizes volatility; the agent abstains when expected net reward is negative

## Signal

- **Formation timestamp**: Continuous — the agent processes 5-minute bar data and updates positions sequentially
- **Lookback**: The ESN uses a dynamic reservoir of 100 hidden units with 10 back-connections, processing the full history of inputs via recurrent dynamics
- **Long entry**: Agent outputs ft > 0 via tanh[wout·zt], learning to go long when expected utility is maximized
- **Short entry**: Agent outputs ft < 0, learning to go short when utility is maximized
- **Exit**: Position is driven toward zero when the expected net reward µt < 0 (equation 7, exponentially weighted mean of returns)
- **Position sizing**: Continuous [-1, +1] via tanh activation; average position ~0.41 (long bias)
- **Parameters**:
  - Risk appetite λ = 0.00001 (set via information ratio)
  - ESN: nhidden = 100, nback = 10, sparsity α = 0.75
  - Extended Kalman filter: ridge penalty β = 1, decay τ = 0.999
  - Spectral radius ρ(Whidden) < 1 (echo state property)
- **Fully specified**: Yes — the model architecture, hyperparameters, and training procedure are fully described in the paper

## Required data

- **Instrument**: XBTUSD perpetual swap (or equivalent crypto perpetual)
- **Venue**: BitMEX (historical); applicable to any perpetual swap venue
- **Market type**: Perpetual futures/swaps
- **Timeframe**: 5-minute bars
- **Fields**: Bid/ask prices (for mid-price and spread), trade data, funding rate (κt), order book depth
- **Funding data**: The funding rate formula (equation 4) requires: interest rate differential (et), basis premium, and basis cap (ζ = 5 bps)
- **Timestamp**: Intraday, 5-minute sampling
- **Missing data**: The paper uses vendor-supplied 5-minute sampled data; tick-level data would be preferable but was constrained by vendor throttle

## Execution assumptions

- **Signal-to-order timing**: Next-bar execution on 5-minute bars
- **Order type**: Market orders (price taker)
- **Fill model**: Immediate fill assumed (price taker crosses spread)
- **Fees**: Exchange fees set at 5 basis points (0.05%) of notional
- **Spread**: Half bid-ask spread at execution time (variable, not fixed)
- **Slippage**: Not explicitly modeled beyond the spread; the authors emphasize this as a key advantage over prior work that assumes fixed costs
- **Funding**: Fully modeled — funding rate κt applied to position at each funding interval
- **Leverage**: Implicit via the perpetual swap contract (BitMEX XBTUSD offered up to 100x)
- **Capacity**: Not discussed; single-instrument strategy on a single venue
- **Latency**: Not discussed; 5-minute sampling implies low latency sensitivity

## Evidence

### Source-reported

- Total return: ~350% net of transaction costs over ~5 years
- Annualised information ratio: 1.46
- Funding contribution: 71% of cumulative return (0.713 out of 3.498 total cumulative PnL components)
- Execution cost: -54% cumulative (-0.542)
- Average position: 0.41 (long bias)
- Monte Carlo (250 trials): Mean information ratio 1.160 (std 0.299), mean total return 297.7% (std 74.0%)
- 95% of mean information ratios: [1.123, 1.197]
- 95% of mean total returns: [288.6%, 306.9%]
- Results are gross of the authors' acknowledge of limitations (see Negative evidence)

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The paper acknowledges that ESN parameters are initialized at random, introducing variability (information ratios range from 0.219 to 1.763 across 250 Monte Carlo trials)
- The sample is a single instrument on a single venue (BitMEX XBTUSD) — no cross-asset or cross-venue validation
- The test period (2017–2021) includes both a major bull market and the 2018 bear market, but the agent shows long bias (average position 0.41), suggesting potential regime dependence
- BitMEX's market structure and fee model have changed since the test period; the exchange has lost significant market share
- The 71% funding contribution raises questions about whether the strategy is primarily a funding carry play rather than a directional alpha — if funding dynamics change structurally, the majority of returns could disappear
- The authors note that the funding rate formula (equation 4) includes a basis cap (ζ = 5 bps), which may not hold on all venues or in all market conditions
- No out-of-sample or walk-forward validation beyond the single backtest

## Falsification plan

- **Required sample**: Replicate on at least 3 additional perpetual swap venues (e.g., Binance, Bybit, OKX) and at least 2 additional instruments (e.g., ETH perpetual)
- **Regime breakdown**: Test separately in bull (2020–2021), bear (2018), and sideways (2019) regimes; if funding capture degrades significantly in one regime, the thesis is weakened
- **Funding sensitivity**: Ablation test — remove funding from the utility function; if performance collapses, the strategy is primarily a funding carry play, not a directional alpha
- **Fee sensitivity**: Test at 3 bps, 5 bps, 10 bps exchange fees; if profitability disappears below 5 bps, the edge is fee-dependent
- **Walk-forward validation**: Split the 5-year sample into rolling 1-year train / 3-month test windows; if out-of-sample Sharpe drops below 0.5, the in-sample results may be overfit
- **Baseline comparison**: Compare against a simple funding carry strategy (long when funding negative, short when funding positive, flat otherwise) to isolate the RL agent's marginal contribution
- **Failure metric**: If the annualised information ratio drops below 0.5 on any cross-venue replication, the thesis is materially weakened

## Crypto portability

**adapted**

The strategy originates from crypto perpetual swaps and is therefore directly applicable to that market structure. However, several portability risks exist:

- **Venue risk**: BitMEX was the primary venue in the test period; modern perpetual swap markets are dominated by Binance, Bybit, and OKX with different fee structures, funding mechanisms, and liquidity profiles
- **Funding mechanism differences**: Different exchanges use different funding rate formulas, intervals (8h vs 1h vs other), and caps; the specific formula (equation 4) may not transfer
- **Liquidity**: BitMEX XBTUSD was one of the most liquid perpetual swaps in 2017–2021; replicate only on instruments with comparable or better liquidity
- **24/7 session structure**: The strategy operates on 5-minute bars with continuous online learning — applicable to 24/7 crypto markets
- **Leverage**: The strategy implicitly uses leverage via the perpetual swap; position sizing is learned, not fixed

## Limitations

- Single instrument, single venue, single backtest — no cross-validation or replication
- Sample period (2017–2021) may not be representative of current market structure
- BitMEX has lost significant market share since the test period
- 71% of returns from funding — the strategy may be primarily a funding carry play rather than a directional alpha
- No explicit capacity analysis
- The ESN architecture is relatively simple (100 hidden units) — unclear if it scales to more complex signal environments
- Online learning approach requires continuous data feed and computation — operational complexity not discussed
- The paper does not address cryptocurrency-specific risks such as exchange insolvency, withdrawal freezes, or smart contract risk
- Not independently reproduced

## Implementation status

not-implemented

No implementation in our research stack. This is a research-only capture.

## Adoption boundary

This record represents external research material only. Presence in this repository does not imply:

- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

## Related Wiki records

- `[[quant/4h-context-funding-alignment-regime-crypto-perpetual-2026-09-06]]` — different mechanism: 4H context-funding alignment regime indicator (Badawi et al. 2025)
- `[[quant/extreme-negative-funding-contrarian-btc-return-2026-09-06]]` — different mechanism: extreme negative funding as contrarian signal for BTC spot returns (Memon et al. 2026)
- `[[quant/strategy-research-record-spec-v1]]`

## Sources

1. Borrageiro, G., Firoozye, N., & Barucca, P. (2022). "The Recurrent Reinforcement Learning Crypto Agent." *IEEE Access*, vol. 10, pp. 38590–38599. arXiv:2201.04699v4 [cs.LG]. DOI: 10.1109/ACCESS.2022.3166599. https://arxiv.org/abs/2201.04699
