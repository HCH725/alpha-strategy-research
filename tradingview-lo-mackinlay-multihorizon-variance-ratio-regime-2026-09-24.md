---
schema: strategy-research-record-v1
title: TradingView Lo-MacKinlay Multi-Horizon Variance-Ratio Regime Classifier
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
  - https://www.tradingview.com/script/oZYdNeW7-Variance-Ratio-Regime-Classifier-PickMyTrade/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Lo-MacKinlay Multi-Horizon Variance-Ratio Regime Classifier

## Provenance

Public TradingView open-source script: **Variance Ratio Regime Classifier [PickMyTrade]**, author/page identity `PickMyTrade_Official`, published Apr 30 (TradingView page as observed 2026-09-24). Stable source URL: https://www.tradingview.com/script/oZYdNeW7-Variance-Ratio-Regime-Classifier-PickMyTrade/. Source as-of date: 2026-09-24.

Repository deduplication before capture found no record for canonical TradingView source `oZYdNeW7`, no `Lo-MacKinlay` match, and no materially identical rolling four-horizon consensus construction. Existing repository material includes variance-ratio evidence and adjacent Hurst/autocorrelation regime research, but those are distinct source identities and/or signal constructions.

## Economic mechanism

### Source-reported

The source interprets a variance ratio near 1 as random-walk behavior, above 1 as positive-return-autocorrelation / trending behavior, and below 1 as negative-return-autocorrelation / mean-reverting behavior. It combines q = 2, 4, 8, and 16 horizons and requires a minimum number of agreeing votes before assigning a regime. The source proposes the classifier as a diagnostic for choosing trend-following versus mean-reversion approaches and explicitly states that VR values are not buy/sell signals and provide no performance guarantee.

### Research interpretation

The falsifiable hypothesis is that **cross-horizon agreement in rolling variance ratios contains incremental point-in-time information about whether simple continuation or reversal rules are more appropriate than when using a single-lag autocorrelation, single-horizon variance ratio, Hurst/DFA estimate, or unconditional strategy**.

The economically relevant component is not merely `VR > 1` or `VR < 1`; it is the claim that agreement across several aggregation horizons identifies persistent return-dependence structure more reliably than a single noisy estimate. This remains an unverified regime-conditioning hypothesis, not evidence of profitable alpha.

## Signal

Source-reported normalized construction:

- Input return: one-period log return `r(t) = ln(close(t) / close(t-1))`.
- q-period return: `R(t,q) = ln(close(t) / close(t-q))`.
- Variance ratio: `VR(q) = Var[R(t,q)] / (q * Var[r(t)])`.
- Horizons: q = 2, 4, 8, 16.
- Rolling variance-estimation window default: 60 bars.
- Per-horizon EMA smoothing default: 3 bars; 1 disables smoothing.
- Trend vote: smoothed VR(q) > 1.15 by default.
- Mean-reversion vote: smoothed VR(q) < 0.85 by default.
- Otherwise: random-walk vote.
- Minimum votes default: 3 of 4. The source describes 4/4 as stricter and 2/4 as more frequent.
- Composite display: equal-weight mean of active VR values.
- Additional display diagnostics: current-regime streak, z-score versus 50-bar history, and percentile rank versus 100-bar history. These display diagnostics are not treated here as part of the core regime signal.
- Source recommends the 60-bar default for one-hour charts and names BTCUSDT 1H, ETHUSDT 1H, ES1! 1H, NQ1! 1H, EURUSD 1H, and GBPUSD 1H as starting points.

The source does not specify a complete trading lifecycle: there is no source-defined position sizing, order type, stop, take-profit, holding period, or executable entry/exit rule. Mapping the regime to a separately defined continuation/reversal strategy is therefore `research-proposed`, not source-reported.

Signal formation should be treated as bar-close point-in-time for research unless source-code-level verification establishes otherwise; exact intrabar behavior is underspecified from the reviewed public description.

## Required data

Minimum source-implied data:

- timestamped close prices sufficient to compute log returns;
- at least the rolling variance window plus q-horizon history and smoothing warm-up;
- consistent bar boundaries.

For direct crypto evaluation, liquid spot or perpetual OHLCV can supply close prices; volume is not required by the stated core VR construction. Venue, spot/perpetual choice, and consolidated versus venue-specific prices are not fixed by the source. Point-in-time bars must be used without revised future information.

## Execution assumptions

The source is an indicator/regime diagnostic rather than an executable strategy. It does not specify signal-to-order timing, market/limit order choice, fees, spread, slippage, impact, capacity, funding, leverage, margin, borrow, latency, partial fills, or failures.

For any later research implementation, execution must be defined separately and marked `research-proposed`. A conservative first test should form the regime only after the classification bar closes and allow any dependent strategy to act no earlier than the next executable observation, avoiding same-bar look-ahead.

## Evidence

### Source-reported

The source provides the mathematical construction, defaults, and qualitative regime interpretation. It does not report a backtest, Sharpe ratio, CAGR, drawdown, win rate, or independently validated predictive statistic for the regime classifier. It explicitly warns that past regime behavior does not predict future persistence and that VR values are not buy/sell signals.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- No source-reported trading performance is provided.
- Rolling estimation, smoothing, fixed thresholds, and consensus voting introduce several degrees of freedom that can overfit regime labels.
- A variance ratio is closely related to serial dependence already measurable by simpler return-autocorrelation statistics; incremental value is unproven.
- The source labels simultaneous threshold exceedance as statistically meaningful, but the reviewed page does not provide a heteroskedasticity-robust Lo-MacKinlay test statistic, p-value, multiple-horizon correction, or finite-sample calibration for each rolling classification.
- The 60-bar window and 1.15/0.85 thresholds are source defaults, not demonstrated universal boundaries.
- Crypto microstructure, 24/7 trading, venue fragmentation, and changing volatility can alter finite-sample VR behavior.

## Falsification plan

All operational tests and cutoffs below are `research-proposed` unless explicitly identified as source-reported.

1. **Incremental-information test:** compare four-horizon consensus against unconditional continuation/reversal, lag-1 return autocorrelation, a single VR(2), Kaufman efficiency ratio, and the repository's DFA/Hurst regime concept. Fail the complexity layer if consensus does not improve frozen OOS risk-adjusted results after costs.
2. **Component ablation:** test raw unsmoothed VR, each q separately, equal-weight composite, 2/4, 3/4, and 4/4 voting. The multi-horizon claim weakens if a single q performs equivalently or better across OOS regimes.
3. **Threshold robustness:** pre-register a modest grid around the source defaults rather than optimizing per asset. Reject parameter-specific alpha if conclusions reverse under nearby windows, thresholds, or smoothing values.
4. **Statistical-null audit:** use return shuffles or appropriately dependence-preserving null simulations to estimate how often rolling multi-horizon consensus occurs by chance. Separately compare with a heteroskedasticity-robust variance-ratio test where appropriate.
5. **Regime usefulness:** condition the *same* simple momentum and mean-reversion baselines on the classifier. The hypothesis fails if regime gating does not add incremental OOS value versus those baselines without gating.
6. **Market/timeframe portability:** test BTC and ETH across multiple liquid venues and several bar sizes, with point-in-time bar alignment. Reject claims of generality if results are isolated to the source-recommended 1H setting or one venue.
7. **Cost sensitivity:** apply realistic fees, spread, slippage, and perpetual funding where relevant. Reject an executable interpretation if any apparent benefit is consumed by turnover costs.

Failure should simplify or reject the variance-ratio consensus layer rather than trigger additional filters.

## Crypto portability

`direct` for computing the source-defined statistic because the source explicitly lists BTCUSDT 1H and ETHUSDT 1H as recommended starting points; **predictive alpha remains unproven**.

Crypto-specific risks include 24/7 candle-boundary choices, exchange-specific close construction, venue fragmentation, perpetual funding if the classifier is mapped to positions, structural breaks, and changing microstructure. The statistical regime label must not be treated as proof that a continuation or reversal trade will be profitable.

## Limitations

- Not independently reproduced.
- No source-reported executable strategy or performance evidence.
- Exact source-code implementation details beyond the public description were not independently reconstructed during this Scout run.
- Exact intrabar/repainting behavior is underspecified from the reviewed description.
- Statistical significance of the rolling threshold votes is unproven; the page's qualitative use of statistical language should not be upgraded into a formal significance result.
- Incremental value versus simpler autocorrelation, VR, Hurst/DFA, and efficiency-ratio controls is unproven.

## Implementation status

Research record only. No implementation in the research stack, no backtest, no Qlib validation, and no production-candidate promotion was performed in this Scout cycle.

## Adoption boundary

`research-only / not-implemented / not-approved`.

Presence in this repository does not mean the hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitability, or received Paper/Testnet/Live approval.

## Related Wiki records

No GitHub-visible Wiki relationship is asserted. Related repository families include raw return-autocorrelation regimes, DFA/Hurst persistence regimes, variance-ratio evidence, efficiency-ratio/trend-quality research, and momentum/mean-reversion conditioning. This record is distinct because it preserves the canonical TradingView source and its rolling q = 2/4/8/16 minimum-vote consensus construction.

## Sources

1. TradingView, **Variance Ratio Regime Classifier [PickMyTrade]**, `PickMyTrade_Official`, public open-source script, observed 2026-09-24: https://www.tradingview.com/script/oZYdNeW7-Variance-Ratio-Regime-Classifier-PickMyTrade/
