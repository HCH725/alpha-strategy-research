---
schema: strategy-research-record-v1
title: Cross-Exchange Liquidation Asymmetry Reversal
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
  - https://www.tradingview.com/script/cwefCALw-Liquidations-Aggregated-Lite/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Exchange Liquidation Asymmetry Reversal

## Provenance

- **Source:** TradingView open-source script, `Liquidations Aggregated (Lite)`.
- **Author / page identity:** `mxdvt07`, TradingView.
- **Stable public URL:** https://www.tradingview.com/script/cwefCALw-Liquidations-Aggregated-Lite/
- **Published:** 2025-10-17.
- **Latest source-page update reviewed:** 2025-12-20.
- **Source as of:** 2026-09-19.
- The source is public and traceable. No Pine source code is reproduced here; this record normalizes the public methodology and research hypothesis only.

## Economic mechanism

### Source-reported

The source aggregates liquidation data across Binance, Bybit, and OKX to represent derivative-market stress across venues. It distinguishes forced short closures as liquidation buy volume and forced long closures as liquidation sell volume. The author states that large liquidation events can coincide with localized volatility spikes and price pivots; the usage notes specifically associate strong short-liquidation spikes during downtrends with possible short-term bounces and strong long-liquidation spikes during uptrends with possible retracements.

### Research interpretation

Forced liquidation is mechanically aggressive order flow rather than discretionary information. A sufficiently extreme, cross-venue liquidation imbalance may temporarily exhaust the forced side and create a short-horizon reversal after the cascade decays. The cross-exchange aggregation is potentially useful because a liquidation event visible simultaneously across major venues should better represent system-wide leverage stress than a single-venue print.

This is a falsifiable interpretation, not a verified fact. A competing hypothesis is continuation: liquidation cascades may reveal genuine information or trigger further margin calls, so extreme liquidation flow could predict continued movement rather than reversal. A third possibility is that liquidation asymmetry predicts only future volatility and contains no directional alpha.

## Signal

The source constructs two aggregate series:

- short liquidations / forced buy volume, aggregated across supported exchange feeds;
- long liquidations / forced sell volume, aggregated across supported exchange feeds.

The public description states that liquidation feeds are requested separately for USD- and USDT-margined pairs, exchange-specific magnitude adjustments normalize denomination differences, and normalized values are summed across venues. Bybit directional handling and OKX normalization were explicitly corrected in later releases; the latest reviewed release uses `barmerge.gaps_on` for requested liquidation series.

**Source-supported directional interpretation:**

- unusually strong short-liquidation buy volume can mark a short squeeze;
- unusually strong long-liquidation sell volume can mark a long wipe;
- sustained directional asymmetry can indicate leveraged-positioning imbalance.

**Research-proposed operationalization for later testing:** define point-in-time liquidation shock intensity from each aggregate relative to its own trailing distribution, then test forward returns after extreme short- versus long-liquidation shocks. Evaluate reversal and continuation directions separately rather than hard-coding the source narrative.

The source does not specify a canonical statistical threshold, formation lookback, entry rule, exit rule, holding period, re-entry rule, position size, or complete trading strategy. Those elements are **underspecified** and must not be inferred as source-reported.

## Required data

- Crypto perpetual-futures instruments; the source gives BTCUSDT and ETHUSDT as examples.
- Liquidation feeds for supported Binance, Bybit, and OKX perpetual contracts.
- Direction-separated long- and short-liquidation volume.
- USD- and USDT-margined contract identity where applicable.
- Exchange-specific denomination / scale metadata sufficient to reproduce normalization.
- OHLCV price bars for forward-return measurement and regime conditioning.
- Timestamp-aligned point-in-time data with no future-filled liquidation observations.
- Missing liquidation observations must remain distinguishable from zero liquidation volume.

The source notes historical lower-timeframe data-gap / forward-fill issues and later changed `request.security()` handling to `barmerge.gaps_on`; this is a material point-in-time data constraint.

## Execution assumptions

The source is an indicator, not a complete executable strategy. Signal-to-order timing, same-bar versus next-bar execution, order type, fill model, fees, spread, slippage, market impact, capacity, funding, leverage, margin, latency, partial fills, and failure handling are not specified.

For later research, any trading rule derived from liquidation shocks must use only liquidation data available by the signal timestamp and should execute no earlier than a causally available bar boundary. This is **research-proposed**, not source-reported.

## Evidence

### Source-reported

The source describes the aggregation and qualitative interpretation of liquidation spikes but does not provide a traceable Sharpe ratio, CAGR, drawdown, win rate, or other strategy-level performance statistic in the reviewed public description. No quantitative profitability claim is imported into this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source's own release history documents data-quality and normalization problems: Bybit liquidation direction was corrected, OKX USDT perpetual normalization was fixed, and lower-timeframe forward-filled data gaps were addressed in later versions. These changes demonstrate that apparent liquidation signals can be sensitive to venue-specific data semantics and missing-data handling.

No independent negative-performance study was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

1. Test forward returns after point-in-time extreme short-liquidation and long-liquidation shocks across multiple liquid crypto perpetuals and several horizons.
2. Compete three hypotheses directly: reversal, continuation, and volatility-only response. Reject directional alpha if shocks predict magnitude but not stable return sign out of sample.
3. Compare cross-exchange aggregation against Binance-only, Bybit-only, OKX-only, and equalized single-venue baselines. The multi-venue thesis is weakened if aggregation adds no stable out-of-sample information.
4. Ablate directional asymmetry against total liquidation magnitude. Test whether `long liquidation - short liquidation` or a normalized ratio contributes beyond total forced-flow intensity.
5. Use rolling / expanding thresholds fitted strictly on prior observations; no full-sample percentile thresholds.
6. Repeat across trend, range, high-volatility, and low-volatility regimes. The source's reversal examples should not be assumed universal.
7. Explicitly test missing-data policy and venue normalization. Zero-fill, forward-fill, and gaps-on treatments must not silently create the signal.
8. Include realistic fees, spread, slippage, funding, and latency. Reject any short-horizon edge that disappears under conservative executable costs.
9. Require chronological out-of-sample survival across assets and venues. Failure should lead to rejection or simplification, not additional indicator stacking.

## Crypto portability

direct

The source itself targets crypto perpetual futures and uses crypto-exchange liquidation feeds. Portability nevertheless depends on venue-specific liquidation symbol semantics, inverse versus linear contract denomination, exchange coverage, feed continuity, 24/7 candle boundaries, and whether historical liquidation data available to research matches what was available in real time.

## Limitations

- Indicator rather than a fully specified strategy.
- Entry, exit, holding period, sizing, and threshold are **underspecified**.
- Exchange-specific normalization is a material dependency.
- Historical feed gaps and prior direction/normalization corrections create data-quality risk.
- Liquidation events may predict volatility rather than direction.
- Cross-venue events are correlated and must not be treated as independent observations.
- No independently verified performance evidence.
- Not independently reproduced.

## Implementation status

Research-only external material. No implementation or backtest in our research stack has been completed for this record.

## Adoption boundary

`research-only / not-implemented / not-approved`.

Presence in this repository does not imply profitable alpha, formal validation, approval for implementation, paper trading, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted in this GitHub-only Scout record.

## Sources

- TradingView — `Liquidations Aggregated (Lite)` by `mxdvt07`: https://www.tradingview.com/script/cwefCALw-Liquidations-Aggregated-Lite/ (published 2025-10-17; reviewed source update 2025-12-20; accessed/as-of 2026-09-19).
