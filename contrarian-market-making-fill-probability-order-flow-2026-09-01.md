---
schema: strategy-research-record-v1
title: Contrarian Market Making via Order-Flow-Feature Fill Probability on Crypto Perpetuals
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - microstructure
  - market-making
  - adverse-selection
  - order-flow
  - high-frequency
  - contrarian
  - perpetual
status: research-only
confidence: medium
source_as_of: 2025-11-25
sources:
  - "Jakob Albers, Mihai Cucuringu, Sam Howison, Alexander Y. Shestopaloff, 'The Market Maker's Dilemma: Navigating the Fill Probability vs. Post-Fill Returns Trade-Off', arXiv:2502.18625v2 [q-fin.TR], November 25, 2025. https://arxiv.org/abs/2502.18625"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Contrarian Market Making via Order-Flow-Feature Fill Probability on Crypto Perpetuals

## Provenance

- Paper: arXiv:2502.18625v2 (q-fin.TR), submitted January 2025, revised November 2025.
- Authors: Jakob Albers (Oxford), Mihai Cucuringu (Oxford/UCLA), Sam Howison (Oxford), Alexander Y. Shestopaloff (Queen Mary/Memorial).
- Data: 232,897 minimum-sized maker orders on Binance USDT-margined BTC perpetual (XBTUSDT), collected over a one-week live trading experiment, agnostic to any trading signal.
- Venue: Binance Futures (BTCUSDT perpetual).
- Source URL: https://arxiv.org/abs/2502.18625

## Economic mechanism

### Source-reported

The authors document a fundamental trade-off for maker (passive) orders at the top of the book: fill probability is negatively correlated with post-fill returns. When the next price move is against a maker order, that order fills automatically (probability 1) but yields a negative return — this is adverse selection against stale quotes. When the next price move is favorable, the order may no longer be at the top of the book, so it misses the favorable move entirely. This mechanical fact renders naive maker strategies (e.g., always posting at the touch in the direction of order flow imbalance) unprofitable.

The authors propose a "Reversals" framework: a logistic regression model trained on 46 order-flow features (amplitude, VWAP returns, standard deviation of price changes, and trade volume patterns across 100ms, 1s, 5s, 30s, and 300s windows) to classify whether a contrarian maker order (posted against the prevailing order flow imbalance) will fill profitably. The model is trained with a direction-aware GMADL objective and evaluated via time-series cross-validation.

Key findings from the live experiment:
- A negative correlation between fill likelihood and post-fill returns confirms the adverse selection problem.
- Contrarian maker strategies (posting buy orders when sell-side pressure dominates, and vice versa) can achieve positive expected returns when conditioned on the model's fill probability prediction.
- The "Reversals" model identifies situations where a contrarian maker strategy at the touch is effective.
- Commonly cited strategies (e.g., trading in the direction of OBI) are shown to be highly unprofitable for maker orders.

### Research interpretation

The alpha hypothesis is: on crypto perpetual futures, the fill probability vs post-fill returns trade-off creates a structural opportunity for contrarian limit order placement. Specifically, when recent order flow is skewed toward one side (e.g., aggressive selling), posting a buy limit order at the top bid is contrarian — it profits from the mean reversion of the temporary price pressure. The key is that the contrarian order fills precisely when the selling pressure exhausts, yielding a positive post-fill return.

This is a microstructure-based alpha: the mechanism is adverse selection reversal. Informed/toxic flow pushes prices temporarily; the contrarian maker captures the reversion. The model's 46 features across multiple timescales capture the state of this pressure.

The strategy is not pure alpha — it is a combination of alpha (contrarian positioning) and risk management (model-based filtering of when contrarian orders are profitable). The alpha component is the order-flow feature set's ability to predict profitable fill outcomes.

## Signal

- **Signal formation**: Every time the order book top-of-book state and recent trade flow are observed (sub-second frequency on Binance Futures).
- **Feature set**: 46 engineered features from order flow across 5 timescales (100ms, 1s, 5s, 30s, 300s):
  - Amplitude of price changes
  - VWAP returns
  - Standard deviation of returns
  - Trade volume patterns (max size, average size, buy count, sell count, total buy volume, total sell volume) per timescale
- **Model**: Logistic regression (direction-aware GMADL objective) trained on historical order data with time-series cross-validation.
- **Long entry (buy maker order)**: Post a buy limit order at the top bid when the model predicts high fill probability with positive expected post-fill return (i.e., contrarian to prevailing sell pressure).
- **Short entry (sell maker order)**: Post a sell limit order at the top ask when the model predicts high fill probability with positive expected post-fill return (i.e., contrarian to prevailing buy pressure).
- **Exit**: Order is filled (becomes a position) or canceled if price moves away from the top of the book. For balanced-inventory trading, positions are unwound when inventory reaches a target threshold.
- **Holding period**: Short-horizon (seconds to minutes); orders are either filled or canceled quickly.
- **Parameters**: Fill probability threshold for order submission; inventory limits; cancellation rules.
- **Position sizing**: Minimum-sized orders (experimental setup); scaling to larger sizes is not validated.
- **Underspecified**: The exact fill probability threshold, inventory management rules, and risk limits are not fully specified in the paper. The logistic regression coefficients are provided but the threshold for action is not.

## Required data

- **Instrument**: BTCUSDT perpetual (Binance Futures).
- **Venue**: Binance Futures (or comparable high-liquidity crypto perp venue).
- **Market type**: Perpetual futures.
- **Timeframe**: Sub-second to 5-minute (for feature construction); sub-second for execution.
- **Data fields**:
  - Order book top-of-book (best bid/ask price and quantity) at sub-second frequency.
  - Trade data (aggressor side, size, timestamp) at sub-second frequency.
  - Recent trade flow aggregates over 100ms, 1s, 5s, 30s, 300s windows.
- **Missing-data assumptions**: Assumes continuous, tick-level data feed from Binance. Data gaps or delayed feeds degrade feature quality.

## Execution assumptions

- **Signal-to-order timing**: Near-instantaneous; features are computed from recent trade flow and order book state, and orders are submitted immediately.
- **Fill model**: Maker limit orders at the top of the book. Fill depends on incoming taker flow.
- **Fees**: Binance Futures maker fee (typically 0.02% or negative for VIP tiers). The paper notes that maker fees are significantly lower than taker fees.
- **Spread**: Virtually always one tick wide on Binance BTC perpetual, except fleetingly after price changes.
- **Slippage**: Not applicable for maker orders (fixed price), but cancellation risk if price moves away.
- **Latency**: Critical for sub-second feature computation and order submission. The paper uses a live trading setup but does not specify exact latency requirements.
- **Capacity**: Minimum-sized orders only. Scaling to larger sizes introduces queue position effects and potential market impact.
- **Leverage**: Not specified; the experimental setup uses minimum-sized orders without leverage.

## Evidence

### Source-reported

- 232,897 minimum-sized maker orders over one-week live experiment on Binance BTC perpetual.
- Negative correlation between fill probability and post-fill returns documented empirically.
- Logistic regression model with 46 features achieves classification of profitable vs unprofitable fills.
- Contrarian maker strategy at the touch shows positive expected returns when conditioned on model prediction.
- Flash crash robustness analysis: taker strategy profits during adverse selection events while maker strategy suffers — validates adverse selection theory.
- Source-reported Sharpe: Not reported (the paper is about mechanism characterization, not strategy performance).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The paper's flash crash analysis shows that maker strategies are vulnerable during sudden adverse selection events (e.g., large price moves from external shocks).
- The authors note that commonly cited OBI-directional strategies are "highly unprofitable" for maker orders — contrarian positioning is necessary.
- The logistic regression model's performance is evaluated on a one-week sample; longer-horizon stability is unknown.
- Scaling beyond minimum-sized orders is not validated and may degrade fill probability and return profiles.

## Falsification plan

- **Required sample**: Replicate the live trading experiment over multiple weeks/months across different market regimes (trending, range-bound, volatile).
- **Baseline**: Compare contrarian maker strategy to: (a) naive OBI-directional maker, (b) random maker placement, (c) passive taker strategy.
- **Out-of-sample**: Test the logistic regression model on out-of-sample periods not used in training.
- **Regime sensitivity**: Evaluate performance during high-volatility regimes, flash crashes, and low-liquidity periods.
- **Cost sensitivity**: Include Binance maker fees and potential adverse execution costs.
- **Failure metric**: If the contrarian strategy's expected post-fill return (net of fees) is not significantly positive after transaction costs, the hypothesis is weakened.
- **Scaling test**: Evaluate whether the model's predictive power degrades when order sizes increase beyond minimum.

## Crypto portability

direct

The paper is already conducted on a crypto perpetual futures venue (Binance BTC perpetual). The mechanism — adverse selection at the top of the book, order flow imbalance dynamics, and fill probability vs return trade-off — is specific to crypto perpetual futures markets.

Portability risks:
- Different venues have different order book dynamics, spread behavior, and fee structures.
- The 46-feature logistic regression model is trained on Binance BTC perpetual data; generalization to other crypto perps (ETH, SOL) or other venues requires retraining.
- Sub-second data feed and execution infrastructure requirements are non-trivial.
- The model's performance may degrade during extreme volatility or regime changes.

## Limitations

- Underspecified: Exact fill probability threshold, inventory management rules, and risk limits are not fully specified.
- Data gap: One-week live experiment only; longer-horizon performance unknown.
- Not independently reproduced.
- Scaling beyond minimum-sized orders is unvalidated.
- Flash crash vulnerability acknowledged by authors.
- The paper is more of a mechanism characterization study than a full strategy backtest; Sharpe/CAGR/drawdown metrics are not provided.

## Implementation status

not-implemented

## Adoption boundary

This record is research material only. A record being present in this repository does NOT mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[crypto-high-frequency-kyles-lambda-price-impact-reversal-2026-08-31]]
- [[crypto-volume-synchronized-probability-of-toxicity-vpin-microstructure-2026-08-31]]
- [[crypto-multilevel-order-flow-imbalance-intraday-2026-08-31]]
- [[crypto-liquidity-provision-reversal-premium-cross-market-2026-09-01]]
- [[funding-aware-market-making-perpetual-dex-2026-08-31]]

## Sources

1. Jakob Albers, Mihai Cucuringu, Sam Howison, Alexander Y. Shestopaloff. "The Market Maker's Dilemma: Navigating the Fill Probability vs. Post-Fill Returns Trade-Off." arXiv:2502.18625v2 [q-fin.TR], November 25, 2025. https://arxiv.org/abs/2502.18625
