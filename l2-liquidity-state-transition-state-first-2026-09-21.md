---
schema: strategy-research-record-v1
title: "L2 Liquidity-State Transition as Primary Predictor of Post-Event Microstructure Regime (State-First Design Principle)"
created: "2026-09-21"
updated: "2026-09-21"
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - microstructure
  - L2
  - order-book
  - regime-detection
  - crypto
  - perpetual-futures
status: research-only
confidence: medium
source_as_of: "2026-07-10"
sources:
  - "https://arxiv.org/abs/2607.09230"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# L2 Liquidity-State Transition as Primary Predictor of Post-Event Microstructure Regime (State-First Design Principle)

## Provenance

- **Source**: arXiv:2607.09230v1 — "When Does Order Flow Matter? State-Dependent L2 Liquidity-State Transitions in Crypto Futures"
- **Author**: Joohyoung Jeon
- **Submitted**: July 10, 2026
- **Subjects**: Trading and Market Microstructure (q-fin.TR); Machine Learning (cs.LG)
- **URL**: https://arxiv.org/abs/2607.09230
- **Sample period**: January 2023 through May 2026 (40 monthly out-of-sample folds)
- **Universe**: Binance BTCUSDT and ETHUSDT perpetual futures, top-20 L2 order book, sampled per minute
- **Data sources**: Top-20 limit-order-book record (per-level bid/ask prices and sizes), aggregate trade-flow (signed taker volume, imbalances, trade counts, VWAP, returns), and a commercial macroeconomic announcement calendar
- **Total windows**: 47,513 (18,631 event windows: BTC 9,330, ETH 9,301; 28,882 matched non-event windows) from 9,773 unique scheduled events

## Economic mechanism

### Source-reported

The paper proposes that within macro-event windows, the **persistent pre-event L2 liquidity state** (calm, mixed, or stressed) is the first-order predictor of the post-event liquidity regime. Order flow adds incremental predictive value only when layered on top of the L2 state, not as a replacement. The macro-event calendar enters only by locating windows and supplying matched non-event controls; event label content (type, region, importance) is not used as a model input.

### Research interpretation

The hypothesized mechanism is that L2 order book state captures persistent microstructure conditions — liquidity depth, spread tightness, and imbalance — that are more informative about near-term liquidity transitions than contemporaneous order flow. This suggests:

1. **Regime persistence**: L2 liquidity states exhibit serial persistence; the book state at time t is a strong predictor of the book state at t+1 to t+5 minutes, even around macro events.
2. **Order flow is conditional**: Trade flow is informative about liquidity transitions only when the L2 state context is already known. As a standalone predictor, order flow is dominated by the state.
3. **Asset asymmetry**: The order-flow increment is robust for ETH (clears null at both 1m and 5m horizons, strongest under stressed pre-event liquidity) but not robustly established for BTC (only isolated 5-minute passes, no regime clears at both horizons).

This has direct implications for **regime-filtered order flow strategies**: L2 state should be used as a regime gate before applying order flow signals, particularly on ETH. The "state-first" design principle means any RL, execution, or LLM-based microstructure model should exceed the L2 state baseline before its added complexity is credited.

## Signal

**Note**: This paper is a prediction study, not a trading study. It does not define entry/exit rules, position sizing, or portfolio construction. The "signal" below is the research-proposed operationalization of the paper's findings for a trading context.

- **Formation timestamp**: L2 state observed at minute t; liquidity regime target defined at minute t+1 or t+5 (research-proposed horizons from the paper's evaluation)
- **Lookback**: Pre-event L2 state computed from the 20-level order book: relative bid-ask spread, total depth across top-20 levels, order-book imbalance across those levels. State discretized into calm/mixed/stressed using train-fold-only tercile thresholds.
- **Entry (research-proposed)**: When pre-event L2 state is "stressed" (or "mixed"), activate order flow signals for ETH (and conditionally for BTC). When L2 state is "calm," suppress or reduce order flow signal weight.
- **Exit**: Not specified by source. Research-proposed: exit when L2 state transitions to "calm" or at a fixed time horizon matching the liquidity-state prediction window (1–5 minutes).
- **Holding period**: 1–5 minutes (matching the prediction horizons studied). Research-proposed for intraday microstructure strategies.
- **Parameters**: State discretization via train-fold-only tercile thresholds of spread, depth-20, and imbalance-20. Logit/ordered-logit models over continuous L2 features fail to improve on the coarse state baseline. A shallow nonlinear L2 model adds robust further gain. Order flow overlay adds +0.010 pooled NLL improvement at both horizons.
- **Position sizing**: Not specified by source.
- **Full specification**: Underspecified — the paper defines a prediction task and evaluation protocol, not a trading strategy. The operationalization above is research-proposed.

## Required data

- **Instrument**: Binance BTCUSDT and ETHUSDT perpetual futures (the paper studies these two specifically)
- **Venue**: Binance Futures
- **Market type**: Perpetual futures (USDT-margined)
- **Timeframe**: 1-minute L2 order book snapshots; 1-minute and 5-minute prediction horizons
- **Fields**: Top-20 bid/ask prices and sizes per side (L2 order book); aggregate trade-flow (signed taker volume, imbalances, trade counts, VWAP, returns); macroeconomic announcement timestamps
- **Point-in-time**: Order-book and trade-flow series are continuous over the full sample; macro calendar used only to locate event windows
- **Timestamp**: Per-minute sampling; timezone not explicitly stated (Binance data typically UTC)
- **Missing-data**: Not explicitly addressed in the source. The paper uses continuous series rather than event-restricted windows.
- **Funding/fee/spread**: Not modeled. The paper reports no cost assumptions. Data gap.

## Execution assumptions

- **Signal-to-order timing**: Not specified. The paper is a prediction study, not an execution study.
- **Order type**: Not specified.
- **Fill model**: Not specified.
- **Fees**: Not modeled. The paper explicitly states it "reports no policy, profit, or simulator result."
- **Spread**: The relative bid-ask spread is a model input feature, not an execution cost assumption.
- **Slippage**: Not modeled.
- **Impact / capacity**: Not addressed.
- **Funding**: Not modeled.
- **Leverage / margin**: Not addressed.
- **Latency**: Not addressed (1-minute sampling resolution is stated).

## Evidence

### Source-reported

Source reports the following key results from the staged nested model comparison (Table 1, Section 5):

- **Coarse pre-event state baseline** (vs. marginal): NLL improvement +0.034 at 1m, +0.045 at 5m. This is the strongest single predictor.
- **Multinomial logit** over continuous L2 features: NLL improvement −0.048 at 1m, −0.034 at 5m (below zero — fails to improve on the coarse state).
- **Ordered logit**: NLL improvement −0.052 at 1m, −0.047 at 5m (below zero — fails to improve).
- **Nonlinear L2-shape model**: NLL improvement +0.044 at 1m, +0.060 at 5m (passes permutation null; bootstrap intervals [.041, .046] and [.057, .062]).
- **Order-flow overlay** (pooled): NLL improvement +0.010 at both 1m and 5m; flow-shuffle null threshold +0.004/+0.003 (passes).
- **Order-flow on BTC**: +0.001 at 1m, +0.003 at 5m; null threshold +0.002/+0.002 (not established at 1m).
- **Order-flow on ETH**: +0.020 at 1m, +0.016 at 5m; null threshold +0.006/+0.003 (clearly passes both horizons).
- **Regime decomposition**: ETH order flow is largest under stressed pre-event liquidity; BTC shows only isolated5-minute passes and no regime clears at both horizons.

All results use proper scoring rules (negative log-likelihood and Brier score, which agree in sign in every cell). Evaluation uses rolling monthly out-of-sample folds with event-clustered validation and blocked permutation tests. Each feature layer is admitted only if it improves on the layer below on the same panel.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The paper is explicitly a prediction study, not a trading study. No profit, Sharpe, or execution result is reported.
- The two-asset scope (BTC, ETH only) is a genuine limit; the ETH-vs-BTC asymmetry is a two-point observation, not a population statement.
- Order flow on BTC is not robustly established — isolated 5-minute passes, no regime clears at both horizons.
- The volatility-tercile, hour-blocked, and multiple-testing checks tighten findings without widening scope.
- The paper does not use event label content (type, region, importance) as a predictor; whether pre-event state dominates a model given the event label is future work.
- Whether pre-event state is similarly first-order for a price-direction target is untested.

## Falsification plan

1. **Out-of-sample replication**: Replicate the staged nested model comparison on additional crypto perpetual futures (SOL, DOGE, etc.) and on additional venues (OKX, Bybit). If the coarse state baseline advantage disappears or reverses on >2 additional pairs, the state-first principle is weakened.
2. **Sub-minute data**: Test at 10-second or tick-level resolution. If the state persistence advantage degrades sharply at higher frequency, the finding may be an artifact of the 1-minute sampling.
3. **Directional target**: Test whether pre-event L2 state is similarly first-order for price-direction prediction (not just liquidity-state transition). If price-direction models gain more from order flow than from L2 state, the state-first principle is liquidity-specific, not universal.
4. **Event-label inclusion**: Add event type, region, and importance as competing predictors. If event labels dominate L2 state, the state-first claim is bounded to the no-label baseline.
5. **Trading backtest**: Operationalize the research-proposed regime filter and test whether L2-state-conditioned order flow signals produce higher risk-adjusted returns than unconditional order flow signals. Research-defined falsification threshold: Sharpe ratio of L2-conditioned strategy must exceed unconditional by ≥0.3 on a 6-month out-of-sample window (research-defined threshold).
6. **Capacity / impact stress**: Test whether the L2 state signal survives realistic fill assumptions (spread, slippage, partial fills) on a 1-minute horizon. If costs erase the signal, the prediction result has no trading value.

## Crypto portability

**Direct** — the paper is already conducted on crypto perpetual futures (Binance BTCUSDT and ETHUSDT).

Crypto-specific considerations:
- **Perpetual-specific**: The funding mechanism and mark/index price dynamics are not modeled. The paper studies L2 book transitions, which are market-structure-level and venue-specific.
- **Venue fragmentation**: Results are Binance-specific. Other venues (OKX, Bybit, DEX perpetuals) may have different L2 dynamics.
- **24/7 session structure**: The paper uses macro-economic event windows, which are more relevant during traditional market hours. Crypto-specific events (exchange outages, protocol hacks, large liquidation cascades) may produce different L2 state dynamics.
- **Liquidity**: Top-20 L2 depth is sufficient for BTC and ETH on Binance; thinner perpetuals may not have reliable L2 state signals.
- **Timestamp / candle boundaries**: The1-minute sampling resolution is coarse relative to actual L2 dynamics; sub-minute effects are not captured.

## Limitations

- **Prediction study, not trading study**: No profit, Sharpe, or execution result is reported. The paper establishes a baseline and evaluation protocol, not a strategy.
- **Two-asset scope**: BTC and ETH only; the ETH-vs-BTC asymmetry is a two-point observation.
- **1-minute resolution**: Sub-minute dynamics are not captured.
- **No event label content**: Event type, region, and importance are excluded from the model.
- **No price-direction target**: Whether L2 state is similarly first-order for price prediction is untested.
- **Order-flow features are summaries**: Local trade-flow summaries, not full order-flow reconstruction.
- **Not independently reproduced**: Results are from a single paper with a single author.
- **Data source**: Licensed raw inputs (L2 order book, macro calendar) cannot be redistributed; derived artifacts will be released upon acceptance.
- **No cross-venue validation**: Binance-only.

## Implementation status

Not implemented. This is a research-only capture of a prediction study's findings. No trading strategy, backtest, or execution system has been built from this record.

## Adoption boundary

This record represents research material only. A record being present in this repository does not mean:
- Passed Research Intake Review
- Entered Hermes Wiki Brain
- Entered the production candidate pool
- Completed Qlib full-backtest validation
- Became a frozen survivor or leaderboard entry
- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading, testnet, or live trading

## Related Wiki records

- No directly related records identified in the repository at time of capture. The paper's state-first design principle is a microstructure baseline concept that may relate to future order-flow or regime-detection strategies.

## Sources

1. Jeon, Joohyoung. "When Does Order Flow Matter? State-Dependent L2 Liquidity-State Transitions in Crypto Futures." arXiv:2607.09230v1, submitted July 10, 2026. https://arxiv.org/abs/2607.09230
