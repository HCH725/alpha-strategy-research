---
schema: strategy-research-record-v1
title: "TradingView CUSUM Volatility Breakout"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - cusum
  - volatility-breakout
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - https://www.tradingview.com/script/s8f1jeTo-CUSUM-Volatility-Breakout/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView CUSUM Volatility Breakout

## Provenance

- Public TradingView open-source script: **CUSUM Volatility Breakout** by **CoinOperator**.
- Published: 2025-12-27.
- Stable source URL: https://www.tradingview.com/script/s8f1jeTo-CUSUM-Volatility-Breakout/
- Source reviewed as of 2026-09-18.
- This record normalizes the public description; it does not redistribute the Pine source code.

## Economic mechanism

### Source-reported

The author presents CUSUM as a statistical change-detection mechanism intended to identify small cumulative shifts in a differenced price process before a trend becomes obvious. The script adapts its control limit using the ratio of short- and long-term ATR, can weight price CUSUM by volume intensity, and can require ATR expansion and/or Bollinger Band breakout confirmation.

### Research interpretation

The falsifiable hypothesis is that persistent small directional price deviations contain information about an emerging regime shift before conventional breakout confirmation. CUSUM accumulation is the primary signal; volatility-adaptive control limits attempt to normalize detection across regimes. Optional volume weighting tests whether participation strengthens the signal, while ATR expansion and Bollinger release are confirmation filters rather than independent alpha assumptions.

## Signal

Source-described normalized logic:

1. Construct a differenced price series using configurable length/order/lag settings.
2. Feed either the transformed differenced series directly or residuals around a short-term EMA baseline into directional CUSUM accumulators.
3. Compare positive and negative cumulative deviations with dynamic control limits. The control threshold H adapts with the short-versus-long ATR ratio; K controls accumulation sensitivity.
4. Optional volume weighting amplifies or suppresses price-CUSUM response using log-normalized volume intensity.
5. Optional ATR confirmation requires current ATR to show expansion relative to smoothed ATR.
6. Optional Bollinger confirmation synchronizes a volatility-contraction/release event with the CUSUM signal using configurable lookback windows.
7. Long signal: confirmed positive CUSUM control-limit breach that clears enabled filters; the source describes price/volume confirmation plus BB breakout when those filters are active.
8. Short signal: symmetric negative CUSUM breach that clears enabled filters.
9. Source states that conditions are detected on the signal bar and chart arrows mark actual fills on the following fill bar.
10. Exit is triggered automatically by an opposite-side signal.
11. Reset behavior is configurable: immediate, opposite-side, decay, threshold, or continuous/no reset. Conflict handling is also configurable, including ignore-both, latest, stronger-side, average-resolve, and sequential-confirm modes.

The public prose exposes parameter roles and some guidance but not one uniquely mandated configuration. Exact default price-difference length/order/lag, K, H bounds, ATR lengths, Bollinger lengths, volume amplification and reset/conflict mode are therefore **underspecified** for a canonical backtest and must not be guessed.

## Required data

- Instruments: source states the method is intended across futures, forex, crypto, stocks, ETFs and CFDs.
- Crypto portability therefore uses the source's own contemplated universe rather than a cross-asset inference.
- Required fields: timestamp and OHLC; volume is additionally required when volume confirmation/weighting is enabled.
- Timeframe: configurable; no single crypto timeframe is mandated by the source.
- Derived inputs: differenced price, ATR at short/long or smoothed horizons, optional log-normalized volume, optional Bollinger Bands, and optional EMA residual baseline.
- Point-in-time requirement: every control limit, residual, volatility statistic, BB condition and confirmation must be computed only from information available at the signal timestamp.
- Venue/candle-boundary conventions are not specified.

## Execution assumptions

The source explicitly distinguishes a prior signal bar from the bar on which the plotted trade fill occurs and states that opposite-side signals trigger exits. This implies a causal signal-to-fill separation that must be preserved.

Market-versus-limit order type, exact next-bar fill price, fees, spread, slippage, market impact, latency, partial fills, leverage/margin, perpetual funding and liquidation mechanics are underspecified. A research implementation must not assume frictionless same-bar execution.

## Evidence

### Source-reported

The source describes the indicator as a configurable statistical trend-detection and volatility-breakout method. It states that higher K reduces sensitivity, that H controls false-alarm versus detection delay, and gives an illustrative target ARL framework rather than a verified profitability claim. It also explicitly cautions that volume weighting may be unsuitable for low-liquidity or irregular-volume crypto pairs. No source-reported performance statistic is adopted here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The reviewed source itself identifies a crypto-specific caveat: volume weighting can be problematic when volume patterns are irregular or liquidity is low. More broadly, adaptive thresholds and numerous optional modes create substantial specification and multiple-testing risk. No independent negative empirical study was identified in the reviewed source; absence is not evidence of robustness.

## Falsification plan

- Freeze one causal baseline configuration before testing; do not optimize all optional modes simultaneously.
- Compare CUSUM alone against simple price-momentum and fixed-lookback breakout baselines to test incremental information content.
- Ablate ATR adaptation, volume weighting, ATR confirmation and Bollinger confirmation one at a time.
- Test transformed-data versus residual input modes separately rather than selecting retrospectively.
- Verify signal-bar versus fill-bar timing explicitly and reject any implementation that leaks future bars into control limits or confirmations.
- Evaluate liquid crypto instruments across multiple volatility/trend regimes and report long/short legs separately.
- Apply realistic fees, spread and slippage; reject the trading hypothesis if gross signal quality does not survive plausible costs.
- Require out-of-sample persistence and parameter-neighborhood stability for K, H and differencing choices.
- For volume-enabled variants, test venue dependence because crypto volume is fragmented and venue-specific.

## Crypto portability

**direct but unproven** — the source explicitly lists crypto among intended markets. The author nevertheless recommends disabling volume weighting for instruments with low-liquidity or irregular volume, explicitly including some crypto pairs.

Crypto-specific risks include 24/7 candle boundaries, fragmented venue volume, spot-versus-perpetual differences, funding, mark/index-price conventions, taker costs and regime-dependent liquidity.

## Limitations

- Not independently reproduced.
- Exact default configuration is underspecified in the public prose.
- The large configuration surface creates material overfitting and multiple-testing risk.
- CUSUM's statistical false-alarm framing does not by itself establish profitable trading alpha.
- Source statements about faster detection and reduced false alarms are hypotheses/author claims, not independent evidence.
- Volume normalization may not transfer consistently across crypto venues.

## Implementation status

Research record only. No implementation, backtest or validation in the user's quantitative research stack was performed in this Scout cycle.

## Adoption boundary

`research-only`. Presence in this repository does not establish profitable alpha, implementation approval, backtest validation, paper-trading approval, testnet approval or live-trading approval.

## Related Wiki records

No stable Hermes Wiki Brain link was verified through this GitHub-only workflow; none is fabricated.

## Sources

- CoinOperator, **CUSUM Volatility Breakout**, TradingView, published 2025-12-27, reviewed 2026-09-18: https://www.tradingview.com/script/s8f1jeTo-CUSUM-Volatility-Breakout/
