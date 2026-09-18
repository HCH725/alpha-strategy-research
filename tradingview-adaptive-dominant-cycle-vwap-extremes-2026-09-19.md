---
schema: strategy-research-record-v1
title: Adaptive Dominant-Cycle VWAP Extreme-Zone Mean Reversion
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
  - https://www.tradingview.com/script/TpfAd8at-Adaptive-VWAP-Stdev-Bands/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Adaptive Dominant-Cycle VWAP Extreme-Zone Mean Reversion

## Provenance

Public TradingView open-source indicator page, **Adaptive VWAP Stdev Bands**, author/page identity `simwai`, originally published 2022-11-10 and shown as updated 2024-02-23. Stable source: https://www.tradingview.com/script/TpfAd8at-Adaptive-VWAP-Stdev-Bands/ . Source reviewed as of 2026-09-19.

The page states that the indicator combines Ehlers dominant-cycle concepts and ZLSMA smoothing with VWAP standard-deviation bands. In adaptive mode, the estimated dominant-cycle length is used as the VWAP reset period; a conventional time-based reset such as daily is also available. The 2024-02-07 release notes state that trading-signal labels were added. The source is public and open-source on TradingView, but this record normalizes the described logic rather than redistributing Pine code.

## Economic mechanism

### Source-reported

The author describes an adaptive VWAP standard-deviation-band indicator in which selectable dominant-cycle algorithms determine the reset period. In adaptive mode, VWAP resets when `bar_index` is divisible by the dominant-cycle length. The author suggests that traders may buy or sell when price reaches extreme zones.

### Research interpretation

The falsifiable hypothesis is that a fixed calendar VWAP anchor can become stale when the market's characteristic oscillation length changes. Re-anchoring VWAP on an estimated dominant cycle may make standardized price-volume deviations more comparable across changing regimes, so excursions into outer VWAP-deviation zones may contain more short-horizon mean-reversion information than excursions defined from a fixed reset schedule.

The proposed alpha mechanism has two separable components:

- **Adaptive anchor:** dominant-cycle estimate controls when VWAP accumulation resets.
- **Extreme-zone signal:** price interaction with VWAP standard-deviation bands identifies an unusually stretched state relative to the adaptive volume-weighted reference.

Whether either component adds predictive value is unverified. In particular, an adaptive reset may merely add parameter instability or timing noise rather than alpha.

## Signal

Source-supported logic:

- Calculate VWAP and standard-deviation bands.
- In an adaptive mode, estimate a dominant-cycle length using one of the selectable algorithms.
- Reset VWAP when `bar_index` is divisible by the dominant-cycle length.
- A time-based reset (for example, daily) is an alternative.
- The source associates outer/extreme zones with potential buy/sell behavior and reports that trading-signal labels were added in the 2024-02-07 release.

The public description does **not** unambiguously specify the exact Boolean rule used by the signal labels, which band level constitutes an actionable extreme, whether an extreme is faded immediately or requires re-entry/cross confirmation, the exact dominant-cycle algorithm/default, smoothing configuration/default, standard-deviation multipliers/defaults, entry timing, exit rule, holding period, re-entry rule, position sizing, or long/short symmetry. These fields are therefore **underspecified** and must not be invented.

A later test may operationalize a simple band-touch/re-entry mean-reversion rule, but any such choice is `research-proposed`, not source-reported.

## Required data

Source-supported minimum:

- OHLC price series sufficient for the selected source input and dominant-cycle estimator;
- volume for VWAP;
- sequential bar index / timestamps;
- timeframe consistent with the chosen reset and cycle estimation.

The source does not specify a particular instrument, venue, market type, crypto universe, or timezone. A causal implementation must compute the dominant-cycle estimate and reset decision only from information available at each signal timestamp. Missing-volume and irregular-bar behavior are not specified.

## Execution assumptions

The source does not specify signal-to-order timing, market versus limit orders, fill model, fees, spread, slippage, impact/capacity, leverage, funding, margin, shorting constraints, latency, partial fills, or failure handling.

For later research, next-bar execution after a fully closed signal bar would be a conservative `research-proposed` baseline. Crypto-perpetual testing would additionally require explicit funding, mark/index, margin and liquidation treatment. Same-bar favorable fills must not be inferred retrospectively.

## Evidence

### Source-reported

The TradingView page describes the indicator construction and intended extreme-zone usage, but the reviewed public description does not provide a traceable Sharpe ratio, CAGR, drawdown, win rate, or other independently auditable performance statistic. No performance claim is promoted to evidence here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-reported negative backtest was identified in the reviewed page. Absence is not evidence of no negative result. The adaptive reset is structurally vulnerable to unstable cycle estimates and to discontinuities caused by changing the reset length.

## Falsification plan

1. **Adaptive-anchor ablation:** hold the extreme-zone rule constant and compare dominant-cycle resets against fixed daily, weekly and fixed-length rolling/anchored VWAP baselines. If adaptive anchoring does not improve out-of-sample risk-adjusted performance or calibration of subsequent mean reversion, reject the adaptive-anchor contribution.
2. **Cycle-estimator stability:** measure turnover and discontinuity in the estimated cycle length. If small price perturbations cause large reset-timing changes and materially unstable results, weaken or reject the mechanism.
3. **Extreme-zone baseline:** compare adaptive VWAP deviations with ordinary rolling z-score / fixed VWAP-deviation signals. If the adaptive construction adds no incremental information, prefer the simpler baseline.
4. **Causality audit:** recompute every cycle estimate, reset event and band value point-in-time. Any use of future bars, repainting, or retrospective cycle selection invalidates the result.
5. **Parameter robustness:** test a bounded grid of cycle-estimator choices, smoothing settings and band multipliers without selecting a single in-sample optimum. A narrow performance island is evidence against robustness.
6. **Regime/OOS test:** evaluate trending, ranging, high-volatility and low-volatility crypto regimes with walk-forward or otherwise strictly held-out periods. The thesis is weakened if gains are confined to one regime or one asset.
7. **Cost sensitivity:** include realistic fees, spread and slippage. Reject tradability if any apparent edge is consumed by plausible execution costs.

## Crypto portability

`unproven`

The mechanism uses generic OHLCV and can technically be computed on crypto, but the cited source does not itself provide crypto-specific empirical validation. Crypto's 24/7 structure makes calendar anchors less economically canonical than in session-based markets, which is precisely why adaptive anchoring is worth testing, but that is a research interpretation rather than evidence.

Venue fragmentation, exchange-specific volume, candle-boundary timezone, spot-versus-perpetual volume, and perpetual funding can materially change results. Cross-venue volume aggregation is not specified by the source.

## Limitations

- `underspecified`: exact signal-label Boolean logic and actionable band level.
- `underspecified`: selected/default dominant-cycle algorithm and its parameters.
- `underspecified`: ZLSMA smoothing configuration and standard-deviation multipliers.
- `underspecified`: entry, exit, holding, re-entry and sizing rules.
- `data gap`: no venue, market type, timeframe or timezone contract in the reviewed description.
- `not independently reproduced`.
- `unproven`: no source-backed crypto performance evidence captured here.
- Adaptive cycle estimation may introduce instability, hidden degrees of freedom and multiple-testing risk.

## Implementation status

Research record only. No implementation or backtest in the research stack has been completed.

## Adoption boundary

This record is research material only. It is not validated alpha and is not approved for implementation, paper trading, testnet, or live trading.

## Related Wiki records

No stable related Hermes Wiki Brain record is asserted from this GitHub-only Scout run.

## Sources

- TradingView — `simwai`, **Adaptive VWAP Stdev Bands** (public open-source script; published 2022-11-10; page shows update 2024-02-23; reviewed 2026-09-19): https://www.tradingview.com/script/TpfAd8at-Adaptive-VWAP-Stdev-Bands/
