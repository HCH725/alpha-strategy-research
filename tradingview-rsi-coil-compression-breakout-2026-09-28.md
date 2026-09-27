---
schema: strategy-research-record-v1
title: TradingView RSI Coil Compression Breakout
created: 2026-09-28
updated: 2026-09-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-28
sources:
  - https://www.tradingview.com/script/dwgn7hrE-Coil-Breaker-RSI-Range-Compression/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView RSI Coil Compression Breakout

## Provenance

Public TradingView open-source strategy **Coil Breaker | RSI Range Compression**, author **blitz_locked**, canonical TradingView script ID `dwgn7hrE`.

Stable source: https://www.tradingview.com/script/dwgn7hrE-Coil-Breaker-RSI-Range-Compression/

Source reviewed as of 2026-09-28. The public description and strategy logic were normalized rather than copying the Pine script.

## Economic mechanism

### Source-reported

The author treats RSI itself as a volatility process. The stated premise is that when the recent high-low range of RSI compresses to an unusually low percentile of its own history, momentum is dormant and may subsequently release in a directional breakout. An EMA-slope filter supplies direction; an optional ADX filter can exclude very weak directional conditions.

The author explicitly characterizes the system as breakout/momentum rather than mean reversion, and states that many coil breakouts fail or chop. The claimed payoff thesis is asymmetric: relatively frequent small losses are intended to be offset by less frequent larger winners.

### Research interpretation

Hypothesis: **unusually low realized dispersion in an oscillator can encode latent price-momentum compression; a subsequent break of the pre-existing oscillator range may identify volatility/momentum expansion earlier than a conventional price breakout.**

Component roles:

- Regime / setup: RSI range compression ranked against its own history.
- Primary signal: RSI breaks the established pre-breakout coil band after a recent squeeze.
- Directional confirmation: EMA slope.
- Optional confirmation: ADX trend-strength gate.
- Risk / exit: ATR stop plus fixed R-multiple target.
- Sizing: equity-percent risk sizing.

The central alpha question is the compression-to-expansion transition. ATR exits and risk sizing are risk-management components, not evidence of predictive alpha.

## Signal

Source-specified logic:

1. Calculate RSI.
2. Over a configurable `coilLen`, measure RSI range as recent RSI high minus recent RSI low.
3. Rank that range against its own longer history using a percentile calculation over configurable `pctLen`.
4. Flag a coil when the RSI range falls into the low tail of that history; the stated default percentile threshold is 20%.
5. Maintain a Bollinger-style dynamic channel around RSI.
6. After a squeeze has been active recently, use a breakout of the **established coil band, not the still-forming current band**, as the primary trigger.
7. Use EMA slope to determine directional eligibility.
8. Optionally require ADX confirmation.
9. Manage an accepted trade with an ATR-based stop and fixed R-multiple target; position size is based on a fixed percentage of equity risk.

Underspecified in the reviewed public description:

- RSI length and source;
- exact `coilLen` default;
- exact `pctLen` default;
- exact percentile/ranking implementation;
- Bollinger-style RSI-channel lookback and deviation multiplier;
- how long a prior squeeze remains eligible for a later breakout;
- precise EMA length and slope definition;
- ADX length and threshold defaults;
- exact ATR length/multiple;
- exact R target and equity-risk default;
- exact bar-close versus intrabar order-submission semantics;
- re-entry and simultaneous/reversal handling.

No missing parameter above is inferred.

## Required data

Minimum source-implied data:

- OHLC data sufficient to calculate RSI, EMA, ATR and ADX;
- instrument and venue: not specified;
- market type: not specified;
- timeframe: not specified;
- volume: not required by the described core signal;
- timestamp/candle-boundary convention: not specified.

Point-in-time requirement: compression percentile and established coil bands must be calculated only from information available at the signal timestamp. The source explicitly distinguishes the established coil band from the still-forming band, which should be preserved in any later implementation to avoid look-ahead contamination.

## Execution assumptions

Source states ATR-based stop, fixed R-multiple target, and equity-percent risk sizing.

The following are underspecified / data gaps:

- market versus limit entry;
- same-bar versus next-bar fill;
- spread;
- fees;
- slippage;
- impact / capacity;
- partial fills;
- funding for perpetual markets;
- leverage / margin;
- borrow / shorting;
- liquidation handling;
- latency.

Any future choices for these fields are **research-proposed** unless independently traced to the source.

## Evidence

### Source-reported

The author states that this style of breakout/momentum system often has a low win rate, approximately 30–40%, and describes the intended payoff profile as 2R+ winners versus 1R losers. These are source-reported characterization/expectation claims from the TradingView page, not independently verified performance statistics for a fixed instrument, sample, or parameter set.

The source does not provide a sufficiently traceable fixed-sample return, Sharpe, CAGR, maximum drawdown, profit factor, or trade-count result in the reviewed public description.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The author explicitly states that most coil breakouts fail or chop and warns that results may be dominated by one or two outlier trades. The author also states that coil dynamics vary substantially by instrument and timeframe.

These admissions materially weaken any assumption that the setup is universally portable or robust without instrument/timeframe-specific validation.

## Falsification plan

Research-defined tests:

1. Compare the full strategy against a baseline price/RSI momentum breakout without the compression prerequisite.
2. Ablate the EMA-slope filter and optional ADX filter separately; do not assume either adds alpha.
3. Test the compression threshold across broad, predeclared ranges rather than optimizing only around the stated 20% default.
4. Use walk-forward or otherwise strict out-of-sample evaluation across multiple crypto instruments and materially different volatility regimes.
5. Measure expectancy, profit factor, tail concentration, and the share of total PnL contributed by the largest 1–5 trades; reject an apparent edge that is economically dependent on a tiny number of sample-specific outliers.
6. Stress fees, spread, slippage and, for perpetuals, funding.
7. Verify that all percentile calculations and coil-band references are point-in-time and that no still-forming band leaks future/current-bar information into the trigger.

**Research-defined falsification threshold:** the hypothesis is materially weakened if compression-conditioned breakouts do not improve out-of-sample expectancy or risk-adjusted payoff versus the simpler breakout baseline after realistic costs, or if any improvement is unstable across reasonable parameter neighborhoods and regimes.

Failure should result in rejection or simplification rather than adding further filters.

## Crypto portability

**unproven**

The public source is instrument-agnostic and does not demonstrate a fixed crypto sample. The mechanism is plausibly portable to liquid crypto because volatility clustering and compression/expansion are not asset-class-specific, but that is a research hypothesis rather than crypto empirical evidence.

Crypto-specific risks include 24/7 candle boundaries, venue fragmentation, spot-versus-perpetual differences, funding, liquidation mechanics, and potentially large differences in oscillator behavior across liquidity tiers.

## Limitations

- Not independently reproduced.
- Instrument, venue, market type and timeframe are unspecified.
- Several material indicator defaults and exact formula details are underspecified in the reviewed public description.
- No traceable fixed-sample performance table was found in the reviewed source.
- Source-reported 30–40% win-rate and 2R+ payoff language is not a verified result for a specified sample.
- Parameter tuning across assets/timeframes creates substantial overfitting risk.
- Tail concentration may dominate apparent profitability.
- Execution and cost model is a data gap.

## Implementation status

Research-only external material. No implementation in the research stack has been completed.

`implementation_status: not-implemented`

No Qlib full-backtest validation or Paper/Testnet/Live verification is implied.

## Adoption boundary

This record is normalized research material only.

Its presence in this repository does **not** mean it:

- passed Research Intake Review;
- entered Hermes Wiki Brain;
- entered the production candidate pool;
- completed Qlib full-backtest validation;
- became a frozen survivor or leaderboard entry;
- is profitable or validated alpha;
- is approved for implementation;
- is approved for paper trading;
- is approved for testnet;
- is approved for live trading.

## Related Wiki records

No stable related Hermes Wiki Brain record is asserted from this GitHub-only Scout run.

## Sources

- TradingView, **Coil Breaker | RSI Range Compression**, blitz_locked, canonical script ID `dwgn7hrE`, public open-source strategy, reviewed 2026-09-28: https://www.tradingview.com/script/dwgn7hrE-Coil-Breaker-RSI-Range-Compression/
