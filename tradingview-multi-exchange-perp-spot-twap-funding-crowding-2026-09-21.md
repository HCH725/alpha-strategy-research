---
schema: strategy-research-record-v1
title: Multi-Exchange Perpetual-Spot TWAP Funding Crowding Regime
created: 2026-09-21
updated: 2026-09-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-21
sources:
  - https://www.tradingview.com/script/IHFS6uCQ-Funding-Rate-CryptoSea/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Multi-Exchange Perpetual-Spot TWAP Funding Crowding Regime

## Provenance

Public TradingView open-source script **Funding Rate [CryptoSea]**, author `CryptoSeaTV`, published 2024-05-29. Stable source URL: https://www.tradingview.com/script/IHFS6uCQ-Funding-Rate-CryptoSea/ . Source reviewed 2026-09-21.

The public description states that the indicator covers multiple venues including Binance, BitMEX, Bybit, HTX, Kraken, OKX, Bitstamp, and Coinbase, uses perpetual-futures and spot pricing, computes TWAPs, derives a raw funding-rate measure from the perpetual/spot comparison, and optionally smooths the result with a moving average. The source describes the indicator as useful for identifying funding shifts and potential reversals, but does not specify a complete trading strategy.

## Economic mechanism

### Source-reported

The source presents funding as a measure of derivatives-market positioning and describes shifts in funding as useful context for market trends and possible reversals. It combines perpetual and spot pricing across selectable exchanges and smooths the derived funding measure to expose significant trends.

### Research interpretation

The falsifiable hypothesis is that an extreme or rapidly changing perpetual-versus-spot financing state can proxy leveraged crowding. If positioning becomes sufficiently one-sided, subsequent returns may exhibit either (a) continuation while leveraged demand remains persistent or (b) reversal when carrying cost and crowded positioning become unstable.

The economically relevant component is the derivative/spot dislocation, not the visual candle coloring. Cross-venue agreement may contain more information than a single-venue measure because a broad funding extreme is less likely to be an idiosyncratic venue artifact. That cross-venue aggregation is a **research-proposed** operationalization; the source itself exposes exchange selection but does not establish a tested aggregation rule.

## Signal

Source-supported elements:

- Inputs include perpetual-futures and spot pricing from multiple crypto venues.
- TWAP is calculated for perpetual and spot prices.
- A raw funding-rate measure is derived from their comparison.
- Optional moving-average smoothing is supported; the public description does not expose one canonical smoothing length.
- Exchange selection is configurable.
- The source associates funding shifts/extremes with trend context and potential reversal analysis.

The public page does **not** fully specify a normalized entry, exit, holding period, re-entry rule, position size, universal threshold, or cross-exchange aggregation rule. Those fields are therefore underspecified.

Research-proposed tests, not source rules:

1. Construct each venue's point-in-time perpetual-versus-spot TWAP dislocation using only data available at the decision timestamp.
2. Standardize each venue using an expanding or rolling historical distribution fitted only to prior observations.
3. Test both a median cross-venue crowding score and breadth (fraction of venues with the same funding sign/extreme state).
4. Evaluate two competing hypotheses separately: continuation after broad funding expansion and mean reversion after extreme crowding.
5. Form signals only after the observation window closes; execute no earlier than the next tradable observation.

No source-unsupported numeric threshold is promoted as canonical.

## Required data

- Crypto spot and perpetual-futures prices for the same underlying across supported venues.
- Timestamped data sufficient to reconstruct the source's perpetual and spot TWAP inputs.
- Venue and contract identifiers, including quote currency and contract specification.
- Funding data if available for an external benchmark against the source-derived proxy.
- OHLCV or higher-frequency observations consistent with the selected TWAP horizon.
- Point-in-time symbol availability and venue listing history.
- UTC-normalized timestamps plus venue-specific funding/settlement timing.
- Missing venue observations must remain missing rather than being silently forward-filled across outages or pre-listing periods.

## Execution assumptions

The source does not specify executable order timing, order type, fill model, fees, spread, slippage, impact, leverage, margin, partial fills, or capacity.

For research reproduction, signal formation must use completed observations and any strategy test should execute on the next available bar/observation. Perpetual funding payments, fees, bid/ask spread and slippage must be charged when testing a derivatives implementation. A spot implementation must separately account for shorting/borrow if shorts are allowed. These are research requirements, not source-reported execution rules.

## Evidence

### Source-reported

The source states that the indicator is designed to analyze funding rates across multiple exchanges, uses perpetual and spot TWAPs as the basis of its funding calculation, and can help identify market trends and potential reversals. No stable numeric Sharpe, CAGR, drawdown, hit rate, or return statistic is reported on the reviewed public page, so none is recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The reviewed source provides no independent backtest establishing predictive alpha. A perpetual/spot price difference can also reflect basis, quote-currency effects, venue microstructure, contract specification, liquidity, and timestamp mismatch rather than pure crowding. None identified in the reviewed source as a quantified negative result; absence is not evidence of no negative result.

## Falsification plan

1. **Proxy validation:** compare the source-style perpetual/spot TWAP measure against actual venue funding observations where available. If correlation and extreme-state agreement are weak or unstable, do not label the proxy as funding.
2. **Baseline:** compare against price momentum, realized volatility, single-venue basis/funding, and unconditional returns at identical horizons.
3. **Ablation:** test single venue -> cross-venue median -> cross-venue breadth -> median plus breadth. Retain added complexity only if it improves leakage-safe out-of-sample results.
4. **Competing direction:** test continuation and reversal as separate predeclared hypotheses. Do not select direction retrospectively per regime without an out-of-sample rule.
5. **Venue robustness:** leave one venue out at a time; reject a purported broad-market effect if results are dominated by one venue.
6. **Quote/contract controls:** separate USD, USDT and other quote conventions and linear/inverse contracts where applicable.
7. **Timestamp placebo:** shift funding/proxy observations forward and backward. Predictive performance that improves with unavailable future timestamps indicates leakage or alignment error.
8. **Cost sensitivity:** include fees, spread, slippage and realized funding payments. Reject economically insignificant gross alpha that does not survive realistic costs.
9. **Regime coverage:** include bull, bear, high-volatility, low-volatility and venue-stress periods using point-in-time venue availability.
10. **Failure action:** if the cross-venue score does not add stable out-of-sample information beyond the strongest single-venue or price-only baseline, discard the composite and do not add further filters.

## Crypto portability

direct

The source is explicitly crypto-focused and uses crypto spot/perpetual markets. Portability risks include venue fragmentation, different funding schedules, quote-currency effects, linear versus inverse contract mechanics, symbol-history changes, exchange outages, 24/7 candle boundaries and differences between a price-derived funding proxy and actual funding payments.

## Limitations

- Complete entry/exit/holding/sizing logic: **underspecified**.
- Exact canonical smoothing length and threshold: **underspecified** in the reviewed public description.
- Cross-venue aggregation: **research-proposed**, not source-reported.
- The source-derived measure may mix funding, basis and microstructure effects.
- Historical symbol availability and venue coverage can introduce survivorship bias.
- Not independently reproduced.

## Implementation status

Research-only normalization. No implementation in the research stack and no Qlib full backtest has been completed for this record.

## Adoption boundary

This record is research material only. Repository presence does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, is profitable, or is approved for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

No Wiki lookup was performed because this Scout is GitHub-only. Repository deduplication was performed against current `main`; no record using this canonical TradingView source was found before write.

## Sources

1. CryptoSeaTV. **Funding Rate [CryptoSea]**. TradingView open-source script, published 2024-05-29. https://www.tradingview.com/script/IHFS6uCQ-Funding-Rate-CryptoSea/ . Reviewed 2026-09-21.
