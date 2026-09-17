---
schema: strategy-research-record-v1
title: "TradingView BTC VWAP Mean-Magnet Range Reversion"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-17
sources:
  - https://www.tradingview.com/script/RAOFpp0y-Strat%C3%A9gia-VWAP-Mean-Magnet-v9-Simple-Alert/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView BTC VWAP Mean-Magnet Range Reversion

## Provenance

Public TradingView open-source strategy **[Stratégia] VWAP Mean Magnet v9 (Simple Alert)** by `GaborNemeth`, published 2025-08-07. Stable source URL: https://www.tradingview.com/script/RAOFpp0y-Strat%C3%A9gia-VWAP-Mean-Magnet-v9-Simple-Alert/. Source reviewed 2026-09-17. The page explicitly describes the strategy as intended for a ranging Bitcoin market. GitHub dedup against current `main` found no record for TradingView script identity `RAOFpp0y`, the source title, or a materially same normalized BTC range/VWAP-zone + RSI-extreme + anti-volume-spike entry rule.

## Economic mechanism

### Source-reported

The author frames VWAP as a mean magnet during sideways Bitcoin conditions. Entries require price to enter a directional signal zone, an RSI extreme consistent with temporary overextension, and a volume safety filter intended to avoid trading against unusually high-momentum breakouts.

### Research interpretation

The falsifiable hypothesis is conditional liquidity-provision / mean reversion: when Bitcoin is in a range, displacement away from a volume-weighted reference may revert, but only when momentum is locally stretched and volume does not indicate a genuine high-participation breakout. The three components have distinct roles: VWAP-derived zone = displacement trigger; RSI = overextension confirmation; volume = breakout-risk veto. The source description does not establish that any component independently contributes alpha, so later ablation is required.

## Signal

Source-reported entry logic is evaluated simultaneously at candle close:

- Long: price crosses into the source's green signal zone, RSI is below `25`, and entry-candle volume is not excessively high.
- Short: price crosses into the source's red signal zone, RSI is above `65`, and entry-candle volume is not excessively high.
- Intended regime: ranging / sideways Bitcoin market.

The reviewed public description does not expose the exact mathematical construction or width of the red/green VWAP signal zones, the RSI lookback, the quantitative definition/lookback of `excessively high` volume, the timeframe, or the exact range-regime classifier. These are **underspecified** and are not invented here.

Exit logic, holding period, re-entry/cooldown, position sizing, stop loss, take profit, pyramiding, and reversal behavior are not specified in the reviewed public description and remain **underspecified**.

Any later operational definition for the signal-zone width, volume threshold, RSI length, or range classifier that is not recovered from the public source must be labeled `research-proposed` rather than source-reported.

## Required data

Minimum source-implied data are timestamped Bitcoin OHLCV bars sufficient to calculate VWAP, RSI, the source's signal zones, and the volume filter. Exact venue, spot versus perpetual market type, timeframe, VWAP reset/session convention, timezone/candle boundary, and missing-data treatment are **underspecified**. Point-in-time research must use only data available by the confirmed signal-bar close and must not use future bars in zone, RSI, volume, or regime formation.

## Execution assumptions

The source explicitly states that all three entry conditions must coincide **at the close of a candle**, so a leakage-safe implementation cannot assume the confirmed signal was known earlier in that candle. Exact order submission and fill timing after confirmation are **underspecified**; a later next-bar execution convention would be `research-proposed` unless recovered from the public source.

Order type, fees, spread, slippage, market impact, latency, leverage/margin, shorting implementation, partial fills, and perpetual funding are not specified in the reviewed description. These must be modeled explicitly in later testing, particularly because mean-reversion edges can be cost-sensitive.

## Evidence

### Source-reported

The source describes the strategy as specifically designed for sideways Bitcoin and explains the volume condition as a safety filter against risky high-momentum breakouts. No traceable Sharpe, CAGR, drawdown, profit factor, win rate, or other performance statistic is carried into this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself implies a key failure regime: high-momentum breakout conditions, which the volume veto attempts to avoid. The strategy is also explicitly regime-dependent on a ranging Bitcoin market. Exact zone and volume formulas are missing from the reviewed prose, preventing exact reproduction from the description alone. No independent negative evidence was reviewed in this Scout cycle; absence is not evidence of robustness.

## Falsification plan

Recover the exact public-source zone construction, RSI length, volume rule, VWAP/session convention, range classifier, and exits before claiming exact reproduction. Then compare the complete rule with: (1) zone-only mean reversion, (2) zone + RSI without volume veto, and (3) a simple VWAP-distance baseline under identical execution and costs. Evaluate range and trend regimes separately, with strictly out-of-sample periods. Stress fees/slippage and perpetual funding where applicable. The hypothesis is materially weakened if the RSI and volume conditions do not improve out-of-sample risk-adjusted performance or false-breakout behavior after accounting for reduced trade count, or if the edge persists only under an ex-post range classifier unavailable at signal time.

## Crypto portability

`direct`. The cited source explicitly targets Bitcoin. Portability to other crypto assets is unproven. Crypto testing must fix 24/7 VWAP reset/session conventions, venue-specific volume, candle boundaries, spot-versus-perpetual mechanics, funding where relevant, and fragmented-liquidity effects.

## Limitations

The exact VWAP signal-zone formula, RSI length, volume threshold/lookback, range-regime definition, timeframe, exit rules, and fill mechanics are **underspecified** in the reviewed public description. The source is open-source on TradingView, but this record intentionally normalizes the publicly described logic rather than redistributing Pine code. Not independently reproduced. Inclusion here does not imply profitable or validated alpha.

## Implementation status

`not-implemented`.

No implementation or backtest in the user's quantitative research stack was performed in this Scout cycle.

## Adoption boundary

Research material only. This record is not evidence of profitability or validated alpha and is not approval for implementation, paper trading, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain record was consulted or asserted in this GitHub-only Scout cycle.

## Sources

- TradingView — `GaborNemeth`, **[Stratégia] VWAP Mean Magnet v9 (Simple Alert)**: https://www.tradingview.com/script/RAOFpp0y-Strat%C3%A9gia-VWAP-Mean-Magnet-v9-Simple-Alert/ (public open-source strategy; published 2025-08-07; reviewed 2026-09-17).
