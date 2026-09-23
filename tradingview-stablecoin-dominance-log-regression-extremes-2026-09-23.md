---
schema: strategy-research-record-v1
title: TradingView Stablecoin Dominance Log-Regression Extremes
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-23
sources:
  - https://www.tradingview.com/script/J92vFESl-Stablecoin-Dominance/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Stablecoin Dominance Log-Regression Extremes

## Provenance

Public TradingView open-source indicator **Stablecoin Dominance** by `VanHe1sing`, published and updated 2023-10-31, reviewed 2026-09-23. Stable URL: https://www.tradingview.com/script/J92vFESl-Stablecoin-Dominance/

Repository deduplication was performed against current `main` before capture by canonical TradingView source identity and normalized signal. No record for this canonical source was found. Existing stablecoin-dominance research in the repository includes materially different constructions, including volatility-adjusted normalization and price/dominance composite signals; this record isolates **dominance deviation from a regression trend using ±2-standard-deviation bands**.

## Economic mechanism

### Source-reported

The source treats stablecoin dominance as a crypto-market sentiment / capital-allocation proxy. It uses a regression line as the central tendency of stablecoin dominance and bands two standard deviations above and below that line. The author describes dominance near/above the upper band as an oversold-crypto / potential-bottom condition and dominance near/below the lower band as an overbought-crypto / potential-top condition.

The source credits `rumpypumpydumpy` for the log-regression code.

### Research interpretation

Falsifiable hypothesis: **extreme deviations of stablecoin dominance from its time-varying regression trend contain incremental medium-horizon mean-reversion information for broad crypto returns beyond raw stablecoin-dominance level/change, crypto price momentum, and simple rolling z-scores.**

Possible mechanism: a high positive dominance residual may represent unusually defensive allocation / sidelined stablecoin capital relative to the prevailing structural trend, while a large negative residual may represent unusually aggressive deployment into non-stable crypto assets. If positioning pressure mean-reverts, subsequent broad-crypto returns may be asymmetric after such extremes.

This interpretation is a hypothesis, not a verified causal statement. Dominance is a ratio and can move because stablecoin capitalization changes, non-stable crypto capitalization changes, or both.

## Signal

Source-supported construction:

- Input: stablecoin dominance.
- Central line: a regression line of stablecoin dominance; the page states that log-regression code is used but does not expose enough textual detail here to reconstruct the exact regression specification.
- Upper extreme: regression line + 2 standard deviations.
- Lower extreme: regression line - 2 standard deviations.
- Source interpretation: dominance approaching/exceeding the upper band corresponds to potential broad-crypto oversold / bottom conditions; dominance approaching/falling below the lower band corresponds to potential overbought / top conditions.

Underspecified by the reviewed source page:

- exact stablecoin constituents and weighting;
- regression functional form beyond the log-regression attribution;
- regression lookback / anchor and standard-deviation window;
- signal formation timestamp;
- precise entry trigger (touch, close beyond, cross, or re-entry);
- exit / holding period / re-entry;
- position sizing;
- tradable instrument or portfolio.

Research-proposed operationalization for falsification only, conditional on source-compatible reconstruction: evaluate separately (a) first close beyond each band and (b) first re-entry inside the band after an excursion; measure forward broad-crypto returns over predeclared horizons. Do not treat this operationalization as source-reported.

## Required data

- Point-in-time stablecoin-dominance series compatible with the TradingView source construction.
- Component stablecoin market-cap series if needed to reconstruct the dominance numerator.
- Total / non-stable crypto market capitalization needed to understand denominator effects.
- BTC and/or broad-crypto benchmark prices for forward-return tests.
- Daily timestamps are a research-proposed starting frequency; source page does not specify a mandatory timeframe.
- Historical constituent availability and stablecoin launches / depegs must be handled point-in-time; do not backfill future constituents into earlier history.

## Execution assumptions

The source does not specify executable order mechanics, fees, spread, slippage, impact, leverage, borrow, funding, or same-bar/next-bar execution.

For any later falsification, signal values must be formed only from information available at the decision timestamp. A research-proposed trading test should use next-observation execution after confirmed band events and include realistic costs for the chosen instrument. Same-bar hindsight execution is not allowed.

## Evidence

### Source-reported

The source qualitatively describes upper-band stablecoin-dominance extremes as potential crypto-market bottoms and lower-band extremes as potential tops. It provides no traceable Sharpe, CAGR, win rate, drawdown, sample statistic, or independently audited backtest result on the reviewed page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independent negative study was identified in the reviewed source. Important structural objections remain: dominance is mechanically denominator-dependent; regression/band choices may be fit to a small number of crypto cycles; stablecoin composition changes over time; and a ±2σ rule assumes a degree of residual stability that may not hold through regime shifts, depegs, regulatory events, or rapid market-cap expansion.

## Falsification plan

1. **Reconstruction gate:** first reproduce the source-compatible dominance, regression centerline, and ±2σ bands without guessing missing parameters. If this cannot be done from traceable public information, classify the hypothesis as technically underspecified rather than optimizing a substitute into existence.
2. **Point-in-time test:** use only stablecoin constituents and market-cap observations actually available at each timestamp; explicitly model data publication latency where applicable.
3. **Baselines:** compare against raw stablecoin-dominance level, dominance change, a simple rolling z-score, BTC/broad-market momentum, and broad-market drawdown/volatility.
4. **Denominator ablation:** separately control changes in stablecoin market cap and non-stable crypto market cap. Reject the liquidity interpretation if apparent alpha is explained by denominator-driven price moves already embedded in dominance.
5. **Transformation ablation:** compare the regression residual/bands with simpler rolling mean/standard-deviation bands. If log-regression adds no robust out-of-sample information, discard the added transformation.
6. **Event definition:** test band touch/cross and post-extreme re-entry separately; do not choose the better definition retrospectively without multiple-testing correction.
7. **Regime robustness:** test bull, bear, sideways, high/low-volatility, major stablecoin depeg, and changing-stablecoin-composition periods separately.
8. **Out-of-sample:** use walk-forward estimation and leave-one-cycle-out checks. Regression parameters and thresholds must be estimated without future observations.
9. **Failure criterion:** reject or materially weaken the hypothesis if the regression-extreme feature has no stable incremental predictive information over simpler dominance and price controls after costs, or if results depend on one cycle, one band-event definition, or hindsight constituent selection.

## Crypto portability

`direct`

The source itself is crypto-specific and uses stablecoin dominance. Portability across crypto instruments is nevertheless unproven: BTC, ETH, altcoin baskets, spot, and perpetuals can react differently, and perpetual implementations introduce funding and venue-fragmentation effects absent from the source description.

## Limitations

- `underspecified`: exact regression and standard-deviation estimation details are not fully recoverable from the reviewed page text.
- `data gap`: exact stablecoin constituent set / weighting is not stated in the reviewed description.
- `not independently reproduced`.
- `unproven`: no source-reported quantitative performance statistics are available on the reviewed page.
- Stablecoin dominance is a ratio, so a falling value does not by itself prove stablecoins were redeemed or deployed into risky crypto assets.
- Structural breaks from stablecoin launches, failures, depegs, regulation, and changing market share can invalidate a stationary-band interpretation.

## Implementation status

Research record only. No implementation in the research stack and no Qlib full backtest has been completed for this record.

## Adoption boundary

`research-only / not-implemented / not-approved`

Presence in this repository does not mean the hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitability, or received Paper/Testnet/Live approval.

## Related Wiki records

- `[[tradingview-stablecoin-dominance-volatility-adjusted-risk-regime-2026-09-21]]` — related stablecoin-dominance family using a materially different volatility-adjusted normalized oscillator.
- `[[tradingview-bitcoin-usdt-dominance-liquidity-adjusted-price-2026-09-23]]` — related dominance family combining BTC price with USDT dominance; distinct from regression-residual extremes.

## Sources

- TradingView — `VanHe1sing`, **Stablecoin Dominance**, published/updated 2023-10-31, reviewed 2026-09-23: https://www.tradingview.com/script/J92vFESl-Stablecoin-Dominance/
