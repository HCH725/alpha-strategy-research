---
schema: strategy-research-record-v1
title: TradingView Return Autocorrelation Persistence/Reversal Regime
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-24
sources:
  - https://www.tradingview.com/script/NngYOwof-Autocorrelation/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Return Autocorrelation Persistence/Reversal Regime

## Provenance

Public TradingView open-source script **Autocorrelation**, author/page identity `willcheang36`. Stable URL: https://www.tradingview.com/script/NngYOwof-Autocorrelation/ . Reviewed 2026-09-24. The public page shows `Mar 28` and describes an update/release on that date; the reviewed text does not unambiguously expose a publication year, so no year is inferred.

Repository deduplication before capture found no record for canonical TradingView source identity `NngYOwof`. Search for the normalized construction found related uses of autocorrelation and momentum/mean-reversion concepts, but no materially identical record centered on this source's return-autocorrelation regime hypothesis.

## Economic mechanism
### Source-reported

The author describes the indicator as measuring autocorrelation of percentage price changes to identify whether returns persist, reverse, or behave randomly. The stated use is diagnosis of short-term persistence versus randomness rather than a complete trading system.

### Research interpretation

A falsifiable hypothesis is that recent return serial dependence is state-dependent: positive return autocorrelation may identify intervals in which a simple directional continuation rule has higher conditional expectancy, while negative autocorrelation may identify intervals in which a simple reversal rule has higher conditional expectancy. This interpretation is **research-proposed**; the source does not establish that either conditional rule is profitable.

## Signal

Source-supported construction: compute autocorrelation on percentage price changes over recent history and interpret its sign/magnitude as evidence of persistence, reversal, or randomness.

The public description does not expose enough detail to establish the exact lookback, lag, estimator, threshold, warm-up behavior, or missing-value handling. These are `underspecified` and must be reconstructed from the public source before implementation.

**Research-proposed operationalization for falsification only:** after exact source reconstruction, freeze the estimator using information available at bar close `t`; use the sign/state of autocorrelation only as a regime variable applied to separately defined, simple one-bar or multi-bar continuation/reversal baselines, and execute no earlier than the next tradable bar. Entry, exit, holding period, re-entry, sizing, and thresholds are not source-reported and must not be attributed to the author.

## Required data

- Point-in-time OHLC sufficient to compute percentage returns; close is the minimum apparent requirement from the public description.
- Exact instrument, venue, market type, timeframe, lookback, and lag are not specified by the source.
- Crypto testing should use point-in-time tradable symbols and explicit exchange/timeframe boundaries.

## Execution assumptions

The source does not specify orders, fills, fees, spread, slippage, impact, leverage, margin, funding, borrow, latency, or partial fills. Any eventual strategy test must generate the regime at a completed bar and trade only afterward, with venue-appropriate costs. Same-bar fills based on a completed-bar statistic must not be assumed.

## Evidence
### Source-reported

The source explains the interpretation of return autocorrelation as persistence, reversal, or randomness. No traceable Sharpe, CAGR, drawdown, win rate, or other strategy-performance statistic is reported on the reviewed public page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-reported trading-performance validation is present on the reviewed page. Autocorrelation estimates can be noisy and highly sensitive to window, lag, overlapping observations, volatility regime, microstructure effects, and multiple testing. None identified in the reviewed source beyond those research concerns; absence is not evidence of no negative result.

## Falsification plan

1. Reconstruct the exact source estimator first; reject implementation parity if source outputs cannot be reproduced from point-in-time bars.
2. Compare autocorrelation-conditioned continuation/reversal rules against unconditional continuation, unconditional reversal, random-walk/no-signal, and simple return-sign baselines.
3. Test whether autocorrelation adds OOS information beyond volatility, trend strength, and recent-return magnitude using matched baselines and component ablation.
4. Sweep only pre-declared lookbacks/lags and report the full family, not the best cell; use walk-forward or held-out OOS evaluation to control parameter mining.
5. Test liquid crypto spot and perpetual markets separately across bull, bear, high-volatility, low-volatility, and sideways regimes.
6. Apply realistic fees, spread, slippage, and perpetual funding where applicable. If conditional net expectancy/Sharpe does not improve robustly over the corresponding unconditional baseline, reject the autocorrelation regime layer rather than adding filters.
7. Use block/bootstrap or serial-dependence-aware inference where appropriate; reject conclusions that disappear under dependence-aware uncertainty estimates.

## Crypto portability

`unproven`. The statistic can be computed directly from crypto returns, but the source does not provide crypto-specific empirical validation. Risks include 24/7 candle boundaries, venue fragmentation, perpetual funding, exchange-specific microstructure, short-horizon bid/ask bounce, and changing liquidity regimes.

## Limitations

- `underspecified`: exact estimator, lag, lookback, thresholds, and lifecycle are not exposed in the reviewed public description.
- `not independently reproduced`.
- `data gap`: no source-reported execution model or performance sample.
- Autocorrelation is descriptive unless incremental predictive value survives OOS controls; interpreting it as alpha before that test would overstate the source.

## Implementation status

Not implemented in the research stack. No Qlib full backtest or downstream validation was performed by this Scout.

## Adoption boundary

Research material only. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor/leaderboard entry, is profitable, or is approved for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

No GitHub-visible Wiki relationship is asserted. Related repository families include momentum, mean-reversion, Hurst/variance-ratio, and regime-classification research, but this record preserves the distinct canonical TradingView source and raw return-autocorrelation hypothesis.

## Sources

- TradingView — `willcheang36`, **Autocorrelation** (public open-source script), reviewed 2026-09-24: https://www.tradingview.com/script/NngYOwof-Autocorrelation/
