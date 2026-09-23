---
schema: strategy-research-record-v1
title: Yang-Zhang Volatility Percentile Compression-Release Regime
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
  - https://www.tradingview.com/script/Wf2FzLLq/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Yang-Zhang Volatility Percentile Compression-Release Regime

## Provenance

Public TradingView open-source script **Compression / Release - Yang-Zhang percentile**, author/page identity `z411392`. Stable source: https://www.tradingview.com/script/Wf2FzLLq/ . Reviewed as of 2026-09-24; the public page shows publication on Jun 30. The source states that it works on stocks, futures, FX, and crypto and is a realized-volatility state indicator rather than a directional trading signal.

Repository deduplication against current `main` found no record for this canonical TradingView source and no materially identical Yang-Zhang percentile compression/release construction. Related repository records use other volatility-compression constructions or broader volatility regimes, so this record isolates the estimator-and-state construction rather than treating generic compression as novel.

## Economic mechanism

### Source-reported

The source describes a market as compressed when current Yang-Zhang realized volatility ranks low relative to its own history and as releasing when that percentile rises. It explicitly warns that release measures volatility expansion as it happens, does not predict direction, and is not a buy/sell signal.

### Research interpretation

The falsifiable hypothesis is not that low volatility alone predicts positive returns. It is that a low Yang-Zhang volatility percentile followed by a confirmed percentile release may identify a transition into a higher-volatility state. A directional alpha, if any, must come from an independently specified direction rule and must show incremental out-of-sample value relative to simpler realized-volatility and range-compression baselines. This operationalization is `research-proposed`.

## Signal

Source-specified state construction:

- Realized-volatility estimator: Yang-Zhang volatility using OHLC information.
- Yang-Zhang window: default 20 bars.
- Compression percentile: `ta.percentrank` of current Yang-Zhang volatility against a default 252-bar history, scaled 0–100.
- Release: change in compression percentile over a default 10-bar release window.
- Compression / expansion reference levels: default 20 / 80.
- Release-start marker: compression percentile crosses back above the compression level.
- Source says the indicator is best read on a daily chart.

The source does not specify long entry, short entry, exit, holding period, re-entry, sizing, leverage, or a complete directional lifecycle. Those elements are `underspecified` and must not be inferred from the release marker.

Research-proposed tests may condition a separately defined momentum/breakout or mean-reversion baseline on the compression/release state, but such rules are not source-reported.

## Required data

- OHLC bars for the target instrument.
- Sufficient point-in-time history for the 20-bar Yang-Zhang calculation and 252-bar percentile lookback, plus warm-up.
- Default research timeframe implied by the source: daily; other timeframes require separate validation.
- Crypto can be tested directly at the indicator-construction level, but 24/7 markets have no conventional overnight session gap, which can alter the behavior of Yang-Zhang components relative to sessioned assets.
- All rolling calculations must use only information available through the confirmed signal bar.

## Execution assumptions

The source is an indicator and does not define execution. For any research-proposed directional test, signal formation must occur on a confirmed bar and execution must not assume access to that bar's final OHLC before the close. Fees, spread, slippage, market/limit order choice, impact, capacity, leverage, margin, funding, borrow, latency, and partial fills are unspecified and must be modeled by the downstream experiment appropriate to the chosen instrument.

## Evidence

### Source-reported

The source provides the construction and interpretation of the volatility-state indicator but does not report a traceable Sharpe ratio, CAGR, win rate, drawdown, predictive regression, or independently validated directional-alpha result. It explicitly states that the release is not predictive of direction and is not a buy signal.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself states that the percentile can remain near an extreme during sustained regimes and that release is a contemporaneous measurement of expansion rather than a forecast. No source-backed profitability evidence was identified on the reviewed TradingView page; absence is not evidence of no negative result.

## Falsification plan

1. Reconstruct the source-specified Yang-Zhang 20-bar volatility, 252-bar percentile rank, 10-bar release change, and 20/80 state levels using point-in-time OHLC only.
2. Test whether low-percentile states and release-start events predict subsequent realized volatility at multiple fixed horizons. Compare against close-to-close realized volatility percentile, ATR/range percentile, Bollinger/Keltner compression, and a simple rolling high-low range baseline.
3. For any directional use, keep direction orthogonal: compare the same momentum/breakout or mean-reversion rule with and without the Yang-Zhang state. The state layer survives only if it adds stable out-of-sample information beyond the underlying directional rule.
4. Ablate the estimator and state logic separately: Yang-Zhang versus simpler volatility estimators; raw low percentile versus low-percentile-plus-release; percentile rank versus raw volatility threshold.
5. Stress the 20/252/10 and 20/80 defaults across nearby parameter neighborhoods rather than selecting a single favorable setting.
6. Test BTC and multiple liquid crypto instruments across trend, range, crash, and low-volatility regimes. Explicitly test whether the sessionless crypto setting weakens the Yang-Zhang advantage over simpler estimators.
7. Apply realistic costs only after a directional lifecycle is specified. Reject the alpha layer if any apparent benefit disappears out of sample, is parameter-fragile, or is indistinguishable from generic volatility compression/release.

## Crypto portability

`direct` for the indicator construction because the source explicitly states that it works on crypto; `unproven` for directional alpha because the source does not demonstrate a profitable crypto trading strategy. The 24/7 crypto session structure is a material portability issue because Yang-Zhang was designed to incorporate overnight/open-to-close information that behaves differently when there is no exchange close.

## Limitations

- Not independently reproduced.
- No source-reported directional strategy or profitability evidence.
- Entry, exit, holding, sizing, and execution are underspecified.
- The source's default daily interpretation may not transfer to intraday crypto bars.
- The economic value of Yang-Zhang versus simpler volatility estimators in 24/7 markets is unproven.
- A release event measures current expansion and must not be mislabeled as a forecast.

## Implementation status

Research-only normalization of a public TradingView source. No implementation or Qlib full-backtest validation has been completed.

## Adoption boundary

This record is research material only. It has not passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, become a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received Paper/Testnet/Live approval.

## Related Wiki records

No specific Wiki record is asserted from this GitHub-only Scout run. Related repository families include volatility-compression breakout and realized-volatility regime research, but no equivalence is implied.

## Sources

- TradingView — `z411392`, **Compression / Release - Yang-Zhang percentile**: https://www.tradingview.com/script/Wf2FzLLq/ (public open-source script; reviewed 2026-09-24).
