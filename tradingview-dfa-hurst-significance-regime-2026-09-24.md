---
schema: strategy-research-record-v1
title: TradingView DFA Hurst Significance Regime
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
  - https://www.tradingview.com/script/cA7HdsdX-Hurst-Exponent-Detrended-Fluctuation-Analysis/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView DFA Hurst Significance Regime

## Provenance

Public TradingView open-source indicator **Hurst Exponent - Detrended Fluctuation Analysis**, author/page identity `Motgench`, published 2025-11-30 and updated 2025-12-18. Stable public URL: https://www.tradingview.com/script/cA7HdsdX-Hurst-Exponent-Detrended-Fluctuation-Analysis/ . Source reviewed as of 2026-09-24.

## Economic mechanism

### Source-reported

The source uses detrended fluctuation analysis (DFA) on log returns to estimate a Hurst-like scaling exponent. It interprets values above 0.5 as persistent/trending, below 0.5 as anti-persistent/mean-reverting, and near 0.5 as random-walk-like. Rather than treating every deviation from 0.5 as meaningful, it also describes sample-size-adjusted 95% confidence bounds obtained by Monte Carlo simulation. The author explicitly warns that the indicator describes past/current market state and does not forecast that the state will continue.

The source further proposes a behavioral interpretation: statistically significant inefficiency may eventually be competed away, so prolonged excursions outside the confidence interval may be closer to regime exhaustion than regime continuation. This is a source-reported hypothesis, not verified alpha evidence.

### Research interpretation

The falsifiable research hypothesis is that a **DFA-estimated persistence state, especially its distance from a sample-size-adjusted null confidence band, contains incremental information about whether simple continuation or reversal rules should be favored** beyond information already available from raw return autocorrelation, trend strength, realized volatility, and recent return magnitude.

A second, distinct `research-proposed` hypothesis is that **duration outside the null confidence band** may contain regime-exhaustion information: newly significant persistence may behave differently from a long-lived significant excursion. This must be tested rather than assumed.

The potential mechanism is time-varying serial dependence / long-memory structure. The DFA estimator is materially different from a single-lag return-autocorrelation statistic because it estimates scaling behavior across multiple box sizes after local detrending.

## Signal

Source-supported construction:

1. Form log returns over a rolling sample.
2. Subtract the sample mean from those log returns.
3. Cumulatively sum the demeaned returns to form an integrated profile.
4. Divide that profile into non-overlapping boxes at multiple, approximately log-spaced scales.
5. Fit a linear trend within each box and compute detrended RMS fluctuation.
6. Regress log average RMS fluctuation on log box size; the regression slope is the DFA/Hurst exponent.
7. Interpret slope above 0.5 as persistence, below 0.5 as anti-persistence, and compare the estimate with sample-size-adjusted 95% Monte Carlo confidence bounds before calling the state statistically significant.

Source-reported parameter guidance includes a sample size greater than 50 for measurement accuracy, optional smoothing, and the statement that larger samples permit larger Base Scale / Max Scale choices. The page gives examples such as sample size 1024 with scale `(16,4)` for long-memory inspection and discusses `(8,2)` as a stable example in its scale comparison. These are source examples/guidance, not validated optimal parameters.

The public page does not specify a complete trading lifecycle: no canonical entry, exit, holding period, re-entry rule, sizing rule, order type, or stop logic is defined. It also does not expose enough detail in the reviewed page text to reconstruct the exact Monte Carlo simulation, confidence-band lookup, optional smoothing length, or all implementation defaults. These elements are `underspecified`.

`research-proposed` operationalization for later testing only: compare a simple continuation rule when DFA is significantly above the upper null band, a simple reversal rule when DFA is significantly below the lower band, and no DFA conditioning inside the band. Separately test excursion age/duration as a conditioning variable. Do not treat this operationalization as source-reported.

Signal formation must use only a completed bar and only data available through that bar. No future classification of an excursion may be backfilled onto its start.

## Required data

- Instrument/universe: source is generic; the page explicitly illustrates Bitcoin on daily bars but does not establish a validated crypto universe.
- Market type/venue: not specified.
- Fields: timestamp and close are sufficient for the described log-return DFA construction; OHLCV is not otherwise required by the stated calculation.
- Timeframe: generic; Bitcoin daily is a source example.
- Rolling history: enough completed bars for the selected sample size and box scales.
- Point-in-time requirement: all rolling samples, detrending, confidence classification, and excursion duration must be computed only from information available at signal time.
- Missing-data treatment, venue consolidation, and session/candle-boundary handling: not specified.

## Execution assumptions

The source is an indicator/regime study, not a complete executable strategy. Signal-to-order timing, next-bar versus same-bar execution, market/limit orders, fill model, fees, spread, slippage, impact/capacity, funding, leverage/margin, borrow/shorting, latency, and partial fills are not specified.

Any later backtest should form the DFA state at a completed bar and, for a tradable interpretation, execute no earlier than the next available bar unless a stricter point-in-time execution model is justified. This is `research-proposed`, not source-reported.

## Evidence

### Source-reported

The source explains the DFA construction, argues that it has advantages over rescaled-range estimation for non-stationary series and smaller samples, and presents Bitcoin daily as an illustrative long-memory example. It does not provide a traceable Sharpe ratio, CAGR, drawdown, win rate, predictive IC, or controlled trading backtest demonstrating profitable alpha from the indicator.

The source explicitly states that the Hurst value measures past/current market state and does not imply that the state will persist into the future.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source itself warns that the estimate is descriptive rather than a forecast of future regime.
- A deviation from 0.5 can occur by chance; the source therefore uses Monte Carlo confidence bounds rather than the 0.5 threshold alone.
- Estimate behavior depends on sample size and scale selection; the source notes that some larger scale settings can become messy or overshoot.
- No source-reported trading-performance evidence demonstrates that DFA conditioning adds alpha after costs.
- The reviewed public page does not fully specify the confidence-band simulation or all defaults, creating a reconstruction gap.
- DFA persistence can overlap economically with simpler serial-dependence measures; incremental value over raw autocorrelation is unproven.

## Falsification plan

1. Reconstruct DFA point-in-time from completed bars only and validate the estimator on synthetic white-noise, persistent, and anti-persistent processes before any return test.
2. Compare DFA state against simpler baselines: lag-1 and multi-lag return autocorrelation, variance ratio, Kaufman efficiency ratio, ADX/trend strength, realized volatility, and recent-return magnitude.
3. Test unconditional continuation/reversal rules versus the same rules conditioned on DFA significance. Require held-out or walk-forward OOS improvement rather than selecting the best in-sample cell.
4. Ablate the confidence-band layer: raw `H-0.5`, binary `H>0.5`, and significance-band state. If confidence filtering does not add stable OOS information, reject that layer.
5. Test multiple pre-declared sample sizes and box-scale configurations; report the family rather than only the best setting. Large sensitivity or sign reversal across nearby settings weakens the hypothesis.
6. For the `research-proposed` exhaustion hypothesis, compare newly significant excursions with long-duration excursions using only contemporaneously known excursion age. Reject it if duration adds no OOS information after controlling for return trend and volatility.
7. Run cost sensitivity appropriate to the tested horizon. If any apparent edge is consumed by plausible fees/spread/slippage, reject the tradable interpretation.
8. Test across assets, timeframes, bull/bear/high-vol/low-vol regimes, and crypto spot versus perpetuals where data permit. A result confined to one asset or narrow parameter cell is insufficient.
9. Explicitly compare against the repository's simpler raw return-autocorrelation regime hypothesis. If DFA does not provide stable incremental OOS information, prefer the simpler estimator and reject the added complexity.

Failure action: do not promote the DFA layer as an alpha component; retain only as rejected/negative research evidence if later Intake/validation reaches that conclusion.

## Crypto portability

`direct` for research measurement because the source itself demonstrates the indicator on Bitcoin daily data, but **predictive/trading alpha remains unproven**.

Crypto-specific risks include 24/7 candle-boundary choices, venue fragmentation, spot/perpetual divergence, rapidly changing market microstructure, and the possibility that long lookbacks mix structurally different crypto regimes. Perpetual implementations additionally require funding and mark/index-price treatment in any trading test.

## Limitations

- `underspecified`: exact Monte Carlo confidence-band construction and all implementation defaults are not fully recoverable from the reviewed public page text.
- `underspecified`: no complete entry/exit/holding/sizing lifecycle.
- `not independently reproduced`.
- `unproven`: predictive and economic value after costs.
- `data gap`: missing-data, venue, session-boundary, and execution conventions.
- The source's statements about DFA estimator advantages and market inefficiency are source claims and should not be upgraded into verified predictive evidence.

## Implementation status

Research normalization only. No implementation in the research stack and no backtest was run by this Scout.

## Adoption boundary

Research-only. This record has not passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib full-backtest validation, become a frozen survivor/leaderboard entry, demonstrated profitability, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No GitHub-visible Wiki relationship is asserted. Related repository families include raw return-autocorrelation regimes, Hurst/cycle studies, variance-ratio research, trend/mean-reversion conditioning, and entropy/regime classification. This record preserves the distinct canonical TradingView source and DFA multi-scale detrending construction.

## Sources

- TradingView — **Hurst Exponent - Detrended Fluctuation Analysis**, `Motgench`, published 2025-11-30, updated 2025-12-18, reviewed 2026-09-24: https://www.tradingview.com/script/cA7HdsdX-Hurst-Exponent-Detrended-Fluctuation-Analysis/
