---
schema: strategy-research-record-v1
title: Bitcoin Spot-Perpetual Multi-Venue Volume-Delta Divergence
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-19
sources:
  - https://www.tradingview.com/script/TyCYjY12-Delta-Vol/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Spot-Perpetual Multi-Venue Volume-Delta Divergence

## Provenance

Public TradingView open-source script `Delta Vol` by `LaDarius_Carter`, originally published 2025-02-24 and updated 2025-02-26. Stable source: https://www.tradingview.com/script/TyCYjY12-Delta-Vol/. Source reviewed as of 2026-09-19.

The source describes Bitcoin volume-delta approximations across Coinbase spot, Binance spot, Binance perpetual, and Bybit perpetual markets, with both individual-venue and aggregate display modes. It explicitly proposes comparing exchanges, spotting divergence, and comparing spot versus futures flow. No source code is reproduced here.

## Economic mechanism

### Source-reported

The author describes volume delta as an approximation of buying versus selling pressure and suggests that disagreement across exchanges, or between spot and futures, can reveal market shifts, accumulation/distribution, trend confirmation, sentiment changes, or potential reversals that ordinary volume may not expose.

### Research interpretation

The falsifiable hypothesis is that **spot-versus-perpetual volume-delta disagreement contains incremental information about short-horizon Bitcoin returns or reversal/continuation regimes beyond price and total volume alone**.

A plausible mechanism is segmentation of informed or less-levered spot demand from leveraged derivatives positioning. For example, persistent spot-positive/perpetual-negative delta could represent spot absorption of leveraged selling; the opposite configuration could represent derivatives-led buying unsupported by spot. These directional interpretations are research hypotheses, not source-verified facts.

A second, distinct question is whether cross-venue aggregation improves signal robustness versus any single venue. If aggregate or spot-perpetual disagreement adds no out-of-sample information beyond price direction, volume, or single-venue delta, the thesis is weakened.

## Signal

Source-supported components:

- Markets: Bitcoin on Coinbase spot, Binance spot, Binance perpetual, and Bybit perpetual are described in the updated source.
- Three delta approximations are described. The original description gives: (1) a candle-range allocation method where buy share is `(close-low)/(high-low)` and sell share is `(high-close)/(high-low)`; (2) a directional typical-price method assigning volume by the sign of current versus previous HLC3; and (3) a simple candle-direction method assigning positive volume to up candles and negative volume to down candles.
- Aggregate mode sums selected venue deltas.
- The source explicitly proposes comparing exchanges and spot versus futures flow for divergences.
- Smoothing options and an adjustable lookback are described, but the updated public description does not provide one canonical parameterization.

Research-proposed operationalization for later testing:

1. Compute contemporaneous spot delta and perpetual delta using one source-described method at a time; do not mix methods inside a primary test.
2. Define a minimal disagreement state from the sign of normalized spot aggregate versus normalized perpetual aggregate (spot positive/perp negative; spot negative/perp positive; agreement-positive; agreement-negative). This sign-state construction is **research-proposed**; it is not presented by the source as a canonical trading rule.
3. Test subsequent returns over pre-registered horizons rather than assuming either reversal or continuation.
4. Separately test a continuous spread between normalized spot and perpetual delta. Scaling, normalization window, thresholds, entry, exit, holding period, re-entry, and position sizing are **underspecified** by the source and must be pre-registered before validation.

Signal formation should use only venue bars available at the decision timestamp. Any later-completed bar or revised/misaligned venue observation must not be backfilled into an earlier signal.

## Required data

- Bitcoin spot OHLCV from Coinbase and Binance.
- Bitcoin perpetual OHLCV from Binance and Bybit.
- Consistent bar interval across venues.
- Exchange and market-type identity retained rather than collapsed at ingestion.
- Point-in-time timestamps with explicit timezone/candle-boundary alignment.
- Venue availability and missing-bar flags.
- If reproducing the source's candle-derived delta, no aggressor-side trade feed is inherently required; this also means the result is an approximation rather than true trade-classified order flow.

The exact TradingView symbol mappings, historical symbol changes, contract denomination normalization, and missing-data policy are underspecified.

## Execution assumptions

The source is an indicator, not a fully specified executable strategy. It does not define canonical signal-to-order timing, market versus limit orders, fees, spread, slippage, impact, funding, leverage, margin, latency, partial fills, or failure handling.

For later research, execution should be evaluated no earlier than the first tradable instant after all venue bars used by the signal are complete. Same-bar fills based on final bar values would require explicit justification. All execution assumptions remain research-proposed until pre-registered.

## Evidence

### Source-reported

The source describes the indicator's construction and intended analytical uses but does not provide a traceable Sharpe ratio, CAGR, drawdown, win rate, or controlled out-of-sample performance result for the spot-perpetual divergence hypothesis. No performance statistic is therefore recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The displayed delta is inferred from OHLCV/candle behavior rather than observed aggressor-side trades, so apparent buying/selling pressure can be a measurement proxy rather than true signed flow. Cross-venue candle boundaries, contract types, volume units, outages, and symbol-history differences can create artificial disagreement. The source provides no independent validation that its divergence interpretation predicts returns.

None of these concerns establishes failure; they are material alternative explanations that must be controlled.

## Falsification plan

1. Use point-in-time aligned BTC spot and perpetual data across the named venues, with explicit missing-bar handling and no forward fill across unavailable venue observations.
2. Pre-register several short horizons appropriate to the tested bar interval and test both continuation and reversal outcomes; do not choose direction after observing results.
3. Compare against simple controls: price momentum/reversal, total volume, spot-only delta, perpetual-only delta, and a single-venue delta.
4. Component ablation: price/volume baseline -> single-venue delta -> same-market multi-venue aggregate -> spot-versus-perpetual disagreement. Require incremental out-of-sample value from the final component.
5. Method ablation: independently test the source-described candle-range, directional-typical-price, and simple candle-direction delta approximations. A result that exists only under one fragile proxy is weaker evidence.
6. Venue ablation: remove each venue in turn and compare Coinbase/Binance spot and Binance/Bybit perpetual contributions. Reject a claimed cross-market mechanism if the result is actually one-venue specific without a defensible reason.
7. Measurement control: where trade-level aggressor-side data is available, compare the OHLCV-derived proxy with true signed-flow measures. Material sign disagreement weakens interpretation of the proxy as order flow.
8. Run chronological out-of-sample and regime splits, including high/low volatility and major venue-stress periods. Apply realistic fees, spread, slippage, and perpetual funding when the tested implementation trades perpetuals.
9. Treat the hypothesis as materially weakened if disagreement has no stable incremental predictive value over the simple controls, reverses sign unpredictably across reasonable specifications, disappears out of sample, or is consumed by realistic costs.

## Crypto portability

direct

The source is explicitly designed around Bitcoin crypto venues. Portability risk remains substantial because spot and perpetual volume units, contract specifications, venue composition, funding, 24/7 candle boundaries, and liquidity differ. Extension to altcoins is unproven.

## Limitations

- Not independently reproduced.
- The source is an indicator, not a complete strategy.
- Entry, exit, holding period, thresholds, sizing, and canonical lookback are underspecified.
- Volume delta is approximated from OHLCV rather than necessarily derived from aggressor-side trades.
- Cross-venue unit normalization and exact symbol history are underspecified.
- The economic direction of spot-perpetual disagreement is unproven; reversal and continuation must both be tested.
- Research-proposed operationalizations must not be confused with source-reported rules.

## Implementation status

Research capture only. No implementation, backtest, reproduction, or validation in the research stack has been completed.

## Adoption boundary

This record is research-only material. It is not evidence of profitable alpha and is not approved for implementation, paper trading, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted from this GitHub-only Scout run.

## Sources

- TradingView, `Delta Vol`, LaDarius_Carter, public open-source script, published 2025-02-24 and updated 2025-02-26: https://www.tradingview.com/script/TyCYjY12-Delta-Vol/ (reviewed 2026-09-19).
