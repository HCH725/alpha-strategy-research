---
schema: strategy-research-record-v1
title: Multi-Exchange Open-Interest Anomaly Liquidation Zones
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - open-interest
  - liquidation
status: research-only
confidence: medium
source_as_of: 2026-09-19
sources:
  - https://www.tradingview.com/script/HQgxb0Ul-Open-Interest-liquidation-map-Ox-kali/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Multi-Exchange Open-Interest Anomaly Liquidation Zones

## Provenance

Public TradingView open-source indicator **Open Interest liquidation map [Ox_kali]**, author `Ox_kali`, published 2024-06-05. Stable source URL: https://www.tradingview.com/script/HQgxb0Ul-Open-Interest-liquidation-map-Ox-kali/. Source reviewed as of 2026-09-19. The page states that the work is inspired by LeviathanCapital's aggregated open-interest work.

## Economic mechanism

### Source-reported

The author aggregates open-interest information from multiple crypto derivatives venues, including Binance, BitMEX and Kraken. The script uses an SMA of open-interest candle size and a user-set size factor to flag unusually large OI changes, then attempts to identify liquidation and interest zones. The author explicitly describes the indicator as experimental and does not claim guaranteed predictive performance.

### Research interpretation

The falsifiable hypothesis is that unusually large changes in aggregate derivatives open interest identify episodes of leveraged-position creation or destruction whose associated price zones contain information about subsequent price interaction. Cross-venue aggregation may reduce venue-specific noise relative to a single-exchange OI series.

This does not establish that an OI anomaly is itself a directional signal. A testable operationalization would treat detected anomaly zones as state variables and test whether later approaches to those zones exhibit statistically different continuation, rejection, volatility, or reversal behavior. That operationalization is `research-proposed`.

## Signal

- Formation: evaluate open-interest candle-size anomalies using an SMA baseline and a user-specified anomaly size factor.
- Data aggregation: source reports OI inputs spanning Binance (USDT, USD and BUSD variants), BitMEX (USD and USDT) and Kraken (USD).
- Primary event: an unusually large OI candle relative to its moving-average baseline.
- Zone construction: the source states that detected anomalies are used to define liquidation / interest zones, but the public description does not fully specify the exact zone-price projection and persistence rules; `underspecified`.
- Long entry: not specified by source.
- Short entry: not specified by source.
- Exit: not specified by source.
- Holding period: not specified by source.
- Re-entry: not specified by source.
- Exact SMA length and anomaly-size-factor defaults: not established from the reviewed page; `underspecified`.
- Research-proposed test: condition future returns and price-reaction statistics on first revisit of a previously formed anomaly zone, separately testing rejection and breakout/continuation outcomes rather than presuming direction.

## Required data

- Crypto derivatives open interest from the source-supported venues/contracts.
- Corresponding OHLCV price bars for the traded/reference instrument.
- Consistent timestamps and candle boundaries across venues.
- Contract-unit normalization before aggregation when OI feeds use different quote/base units.
- Point-in-time availability is mandatory: only OI observations available by the signal timestamp may form an anomaly or zone.
- Missing venue observations must not be silently treated as zero.

## Execution assumptions

The source is an indicator rather than a complete execution strategy. Signal-to-order timing, market versus limit orders, fills, fees, spread, slippage, funding, leverage, liquidation risk, latency, partial fills and capacity are not specified.

Any backtest should form the event only after the relevant bar/OI observation is confirmed and execute no earlier than the next feasible timestamp unless the data pipeline can prove contemporaneous availability.

## Evidence

### Source-reported

The TradingView page describes the indicator as experimental and says it attempts to identify liquidation and interest zones from significant multi-platform OI anomalies. No source-reported Sharpe, CAGR, win rate, drawdown, or other validated performance statistic was identified on the reviewed page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself warns that the indicator does not guarantee future market performance and characterizes the implementation as experimental. The reviewed page provides no independent evidence that anomaly zones predict future direction or returns.

## Falsification plan

1. Reconstruct venue-normalized OI point-in-time and verify that anomaly timestamps are invariant to later data revisions.
2. Compare multi-exchange aggregation against Binance-only and each available single-venue baseline.
3. Test first-touch forward returns, rejection probability, breakout probability and realized volatility around anomaly zones over multiple horizons; do not choose direction after observing outcomes.
4. Run placebo tests using randomly shifted event timestamps and size-matched ordinary OI changes.
5. Ablate the anomaly threshold and SMA baseline to determine whether results are robust rather than concentrated at one parameter choice.
6. Segment OI increases versus OI decreases and price-up versus price-down states because position creation and position destruction can have different mechanisms.
7. Require out-of-sample persistence across BTC, ETH and other sufficiently liquid perpetual markets and across high/low-volatility regimes.
8. Include realistic fees, spread, slippage and funding for any executable rule derived from the zones.
9. Reject the alpha interpretation if zone-conditioned outcomes do not outperform matched controls out of sample, or if any apparent effect disappears under point-in-time venue normalization.

## Crypto portability

`direct` — the source is explicitly designed for crypto open-interest data across crypto derivatives venues. Portability across assets remains dependent on contract availability, OI quality, venue coverage and consistent unit normalization.

## Limitations

- `underspecified`: exact zone projection/persistence logic and parameter defaults were not fully recoverable from the reviewed public description.
- `not independently reproduced`.
- OI changes do not uniquely identify long versus short positioning or actual liquidation flow.
- Cross-venue contract specifications and quote units can make naive aggregation misleading.
- Historical availability and survivorship of venue-specific OI symbols may create data gaps.
- The source provides an analytical map, not a complete trading strategy.

## Implementation status

No implementation or backtest in our research stack has been completed. `not-implemented`.

## Adoption boundary

Research material only. Presence in this repository does not imply profitable alpha, validated predictive power, implementation approval, paper-trading approval, testnet approval, or live-trading approval.

## Related Wiki records

No stable Hermes Wiki Brain link asserted from this GitHub-only Scout run.

## Sources

- TradingView — Ox_kali, **Open Interest liquidation map [Ox_kali]**: https://www.tradingview.com/script/HQgxb0Ul-Open-Interest-liquidation-map-Ox-kali/ (published 2024-06-05; reviewed 2026-09-19).
