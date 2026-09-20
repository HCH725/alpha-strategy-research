---
schema: strategy-research-record-v1
title: HTF Delta-Flux Liquidation Exhaustion
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-20
sources:
  - https://www.tradingview.com/script/QB2tCO1N-HTF-Delta-Flux-Liquidations-BigBeluga/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# HTF Delta-Flux Liquidation Exhaustion

## Provenance

- Primary source: BigBeluga, “HTF Delta Flux + Liquidations [BigBeluga],” public TradingView open-source script.
- Stable public URL: https://www.tradingview.com/script/QB2tCO1N-HTF-Delta-Flux-Liquidations-BigBeluga/
- TradingView page date displayed at review: May 29; the page does not expose a year unambiguously in the reviewed text.
- Source reviewed as of 2026-09-20.
- The source explicitly describes its liquidation markers as a volume-based proxy rather than exchange liquidation-feed observations.

## Economic mechanism

### Source-reported

The source decomposes higher-timeframe candles using lower-timeframe cumulative volume-delta dynamics (“Delta Flux”). It states that a bullish higher-timeframe candle accompanied by declining Delta Flux can indicate aggressive selling being absorbed, while price rising with flat Delta Flux can indicate weak conviction. It also identifies unusually large changes in volume delta relative to recent activity as synthetic “Liquidity Flush” events and states that such events after rapid price extensions can mark temporary exhaustion or local turning points.

### Research interpretation

The falsifiable hypothesis is that the *path* of lower-timeframe directional volume inside a higher-timeframe candle contains incremental information beyond the higher-timeframe OHLCV endpoint. In particular, a price extension whose higher-timeframe direction conflicts with its intrabar cumulative-delta path, especially when accompanied by an extreme delta-velocity event, may identify exhaustion/absorption and increase subsequent mean-reversion probability.

A competing hypothesis is continuation: extreme directional delta may simply identify genuine information arrival and predict further movement rather than exhaustion. The research design must test both rather than assuming reversal.

Component roles:

- Regime/context: higher-timeframe candle structure and recent price extension.
- Primary state variable: intrabar cumulative-volume-delta path relative to higher-timeframe price direction.
- Event confirmation: extreme rate-of-change in volume delta relative to its recent distribution.
- Outcome hypothesis: subsequent reversal/exhaustion versus continuation.

## Signal

Source-supported logic:

- Construct a higher-timeframe candle while observing lower-timeframe directional volume within that candle.
- Track the cumulative volume-delta path through the higher-timeframe candle rather than only its final value.
- Identify unusually high-velocity volume-delta events using a standard-deviation threshold relative to recent activity.
- Source examples treat bullish higher-timeframe price with declining Delta Flux as possible absorption and price rising with flat Delta Flux as low-conviction.
- The source states that synthetic liquidation/flush labels after fast price extensions frequently mark temporary exhaustion.

Underspecified by the reviewed source:

- exact lower-timeframe delta construction and aggressor classification;
- default higher/lower timeframe mapping;
- exact delta-rate-of-change formula and lookback;
- standard-deviation estimator and default threshold;
- quantitative definition of a fast price extension;
- exact divergence/flatness threshold;
- canonical long/short entry;
- exit, holding period, re-entry, sizing, and stop logic.

Research-proposed operationalization for later testing only: measure the slope/path displacement of intrabar cumulative delta against contemporaneous higher-timeframe price displacement; separately flag tail delta-velocity observations using leakage-safe rolling standardization. Evaluate future returns after aligned, divergent, and divergent-plus-flush states over fixed forward horizons. These are research proposals, not source-reported trading rules.

## Required data

- Crypto spot or perpetual OHLCV at the target higher timeframe.
- Lower-timeframe or trade-level volume data sufficient to construct a point-in-time directional-volume proxy.
- Intrabar timestamps aligned strictly inside each higher-timeframe candle.
- For a higher-fidelity reproduction, aggressor-side trades are preferable to candle-direction volume approximations.
- No real liquidation feed is required for the source construction; the source explicitly uses a synthetic volume-based proxy.
- If tested on perpetuals, funding, mark/index and open interest are useful controls but are not required by the source signal itself.
- Point-in-time constraint: only lower-timeframe observations available by each decision timestamp may enter the feature. A completed higher-timeframe candle must not leak future intrabar observations into earlier decisions.

## Execution assumptions

The source is an indicator/diagnostic and does not specify an executable strategy contract. Order type, signal-to-order timing, same-bar versus next-bar execution, fees, spread, slippage, impact, funding, leverage, margin, partial fills and latency are underspecified.

Any later backtest should use next-observation execution after a fully observable signal unless a stricter point-in-time intrabar design is explicitly implemented. This is research-proposed, not source-reported.

## Evidence

### Source-reported

The author states that declining Delta Flux inside a bullish higher-timeframe candle can indicate absorption, flat Delta Flux during rising price can indicate low conviction, and synthetic liquidation/flush markers after fast extensions frequently indicate temporary exhaustion. The source does not provide a traceable backtest, Sharpe ratio, CAGR, drawdown, win rate, or statistical significance for these claims.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source explicitly states that its liquidation engine does not use real-time exchange liquidation API data and instead treats extreme volume-delta changes as a proxy for liquidation-like events. Therefore the “liquidation” interpretation can be wrong even when the volume anomaly itself is measured correctly.

The source provides qualitative use cases rather than a statistical validation, and several implementation details required for exact reconstruction are underspecified. Volume-delta approximations may also differ materially from true aggressor-side trade classification.

## Falsification plan

1. Build a leakage-safe dataset with lower-timeframe observations nested inside completed higher-timeframe candles; test 1h/4h/1d higher-timeframe variants separately rather than pooling them.
2. Baselines: higher-timeframe price momentum alone, terminal cumulative delta alone, total volume shock alone, realized-volatility shock alone, and a simple price/volume divergence baseline.
3. Test whether intrabar Delta-Flux path features add incremental out-of-sample information over those baselines.
4. Ablate: price extension only → delta-path divergence only → delta-velocity shock only → divergence + shock interaction.
5. Competing outcomes: measure both reversal and continuation at multiple fixed forward horizons; reject an exhaustion-only story if continuation dominates robustly.
6. Replace the TradingView-style directional-volume proxy with true aggressor-side trade delta where available. If the effect disappears, classify the proxy-specific result as non-portable.
7. Run timestamp/event-label placebos and randomized within-regime controls to determine whether generic high-volatility episodes explain the result.
8. Condition on volatility, volume, open-interest and funding regimes where available to test whether Delta Flux has incremental information rather than merely relabeling stress.
9. Require out-of-sample persistence across multiple liquid crypto instruments and cost sensitivity before any implementation consideration.
10. Failure action: if incremental predictive information does not survive baselines, point-in-time controls, proxy replacement and costs, reject the hypothesis rather than tune thresholds to rescue it.

## Crypto portability

direct

The source is directly framed as an order-flow/volume diagnostic usable on market charts and discusses synthetic liquidation-like events without requiring traditional-market session assumptions. Crypto-specific risks remain material: 24/7 candle boundaries, venue fragmentation, spot/perpetual volume differences, exchange-specific trade classification, funding, and the gap between synthetic volume anomalies and actual forced liquidations.

## Limitations

- Not independently reproduced.
- Exact delta construction is underspecified in the reviewed description.
- Exact standard-deviation lookback/threshold and price-extension definition are underspecified.
- Liquidation markers are proxies, not exchange liquidation observations.
- Qualitative chart interpretation may introduce hindsight and discretionary labeling.
- Multi-timeframe construction creates substantial look-ahead risk if intrabar data are not aligned point-in-time.
- No source-reported transaction-cost or execution study was identified.

## Implementation status

Research record only. No implementation, backtest, quantitative-runtime integration, paper trading, testnet validation, or live validation has been performed as part of this Scout cycle.

## Adoption boundary

This record is research-only and not approved for implementation or trading. Presence in this repository does not establish profitability, validated alpha, execution feasibility, or approval for paper, testnet, or live deployment.

## Related Wiki records

No stable Hermes Wiki Brain link was established during this GitHub-only Scout cycle; none is fabricated.

## Sources

- BigBeluga, “HTF Delta Flux + Liquidations [BigBeluga],” TradingView public open-source script, reviewed 2026-09-20: https://www.tradingview.com/script/QB2tCO1N-HTF-Delta-Flux-Liquidations-BigBeluga/
