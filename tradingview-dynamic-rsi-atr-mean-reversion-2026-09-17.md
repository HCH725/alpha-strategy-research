---
schema: strategy-research-record-v1
title: "TradingView Dynamic RSI ATR-Adjusted Mean Reversion with Trend Filter"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - mean-reversion
  - rsi
  - atr
status: research-only
confidence: medium
source_as_of: 2026-09-17
sources:
  - https://www.tradingview.com/script/K9FLcueo-Dynamic-RSI-Mean-Reversion-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Dynamic RSI ATR-Adjusted Mean Reversion with Trend Filter

## Provenance

Public TradingView open-source strategy **Dynamic RSI Mean Reversion Strategy**, published by `nathanfarmer`, stable URL https://www.tradingview.com/script/K9FLcueo-Dynamic-RSI-Mean-Reversion-Strategy/. The page is dated and updated Nov 4, 2024. Source reviewed 2026-09-17.

GitHub dedup against current `main` found no record citing TradingView script identity `K9FLcueo`, the exact title, or author/source identity. Repository keyword search found other RSI, ATR, trend-filter and mean-reversion records, but no materially same construction in which ATR dynamically changes RSI overbought/oversold boundaries and a moving-average trend state suppresses countertrend mean-reversion entries.

## Economic mechanism
### Source-reported

The author describes a mean-reversion strategy that modifies RSI overbought/oversold thresholds using ATR so the extreme zones adapt to volatility. The stated intent is to expand the RSI range in high volatility and tighten it in low volatility, while a moving-average-cross trend filter prevents taking mean-reversion trades against the detected trend. ATR-based stops provide volatility-adjusted protection.

The author explicitly distinguishes signal quality from trade frequency: substantial filtering produces fewer trades, and the trend filter is intended to avoid countertrend entries rather than create the mean-reversion signal itself.

### Research interpretation

The falsifiable alpha hypothesis is that a fixed RSI threshold is poorly calibrated across volatility regimes: the same oscillator reading may represent a meaningful price extreme in one regime but ordinary noise in another. Conditioning the RSI reversal boundary on contemporaneous ATR may therefore improve the precision of exhaustion/reversal signals. The moving-average-cross state is a separate regime gate intended to reduce the known failure mode of mean reversion during persistent trends.

Component roles are therefore:

- **Primary signal:** RSI re-entry/cross relative to volatility-adjusted overbought/oversold thresholds.
- **Volatility adaptation:** ATR changes the effective RSI extreme boundaries.
- **Regime filter:** moving-average cross blocks countertrend trades.
- **Risk logic:** ATR-distance stop loss.

Whether each component adds incremental out-of-sample value is unverified and requires ablation.

## Signal

Source-reported logic recoverable from the public description:

- Calculate RSI.
- Calculate ATR and use it to dynamically adjust RSI overbought and oversold thresholds.
- Long/short entries occur when RSI crosses the corresponding dynamic threshold, subject to the moving-average-cross trend filter so the trade is not countertrend.
- Stops are set at an ATR-derived distance from entry.
- The author states that standard RSI inputs, a relatively slow ATR and a slower MA cross are the default/recommended configuration, but the reviewed prose does not expose the exact numeric defaults.

The exact mathematical mapping from ATR to the RSI threshold, RSI length, ATR length, ATR stop multiplier, moving-average types/lengths, precise long/short comparison operators, exit logic beyond the ATR stop, re-entry behavior, pyramiding, sizing, and order timing are **underspecified** in the reviewed public prose. They must not be invented.

`research-proposed` causal convention for later testing, if the public Pine source has not yet resolved timing: compute all indicator states from completed bars and execute no earlier than the next bar. This is not source-reported.

## Required data

Minimum source-implied data are timestamped OHLC bars sufficient to calculate RSI, ATR and the moving-average trend filter. Volume is not stated as part of the rule. No instrument, venue, market type or timeframe is mandated by the public description; the author recommends testing across assets and timeframes rather than claiming a specific validated universe.

Point-in-time research must form RSI, ATR, dynamic thresholds and moving averages using only information available at the signal timestamp. Warm-up length depends on the exact source parameters and is therefore currently underspecified.

For crypto portability testing, venue, spot/perpetual market type and 24/7 candle boundary must be fixed explicitly.

## Execution assumptions

The reviewed source does not specify same-bar versus next-bar fills, market versus limit orders, spread, fees, slippage, latency, partial fills, leverage, margin, borrow, funding, liquidation treatment or capacity. These must be explicit in later validation.

ATR-based stops are source-reported risk management, not evidence of predictive alpha. Exact stop calculation and fill semantics are underspecified until recovered from the public source.

## Evidence
### Source-reported

The author states that volatility-adjusted RSI thresholds and trend filtering are intended to enhance mean-reversion trade quality, with fewer trades because of the additional filtering. The page recommends experimentation across assets and timeframes and does not present a traceable Sharpe, CAGR, drawdown, win rate or other performance statistic in the reviewed description that should be carried into this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source acknowledges the trade-off that stronger filtering reduces trade count and that trend-filter speed matters: a filter that is too slow can reject desirable trades while allowing poor ones, while a filter that is too fast can fail to filter enough. This implies material parameter sensitivity. No independent negative evidence was reviewed in this Scout cycle; absence of additional negative evidence is not evidence of robustness.

## Falsification plan

1. Recover the exact ATR-to-RSI-threshold mapping and source defaults before claiming exact reproduction; unresolved choices must remain `underspecified` or be labeled `research-proposed`.
2. Compare against a fixed-threshold RSI mean-reversion baseline with identical execution and costs. The volatility-adaptation thesis is weakened if ATR-adjusted thresholds do not improve out-of-sample risk-adjusted performance, drawdown or false-entry rate after accounting for reduced trade count.
3. Ablate the MA trend filter separately to measure whether it improves results or merely suppresses trades.
4. Ablate the ATR stop from entry logic so risk-management effects are not misattributed to signal alpha.
5. Evaluate high/low volatility and trending/ranging regimes separately, with strictly out-of-sample periods.
6. Stress realistic fees, spread and slippage; for perpetuals include funding.
7. Test a small predeclared neighborhood around source parameters rather than optimizing broadly after observing results.

## Crypto portability

`adapted`. The source describes a generic cross-asset strategy and recommends testing on different assets/timeframes; it does not provide crypto-specific empirical evidence in the reviewed description. The OHLC-derived mechanism is portable enough to test on crypto, but that is a ported hypothesis rather than demonstrated crypto alpha.

Crypto validation must account for 24/7 candle boundaries, venue fragmentation, spot-versus-perpetual differences, funding and mark/index conventions for derivatives, and liquidity/slippage differences across assets.

## Limitations

- Exact ATR-to-RSI threshold formula: **underspecified**.
- Exact RSI, ATR and moving-average parameters: **underspecified** in reviewed prose.
- Exact entry confirmation, exits beyond ATR stop, sizing and execution timing: **underspecified**.
- No source-reported quantitative performance claim was adopted.
- Generic-source mechanism; crypto empirical validity is **unproven**.
- Not independently reproduced.

## Implementation status

`not-implemented`.

No implementation or backtest in the user's quantitative research stack was performed in this Scout cycle.

## Adoption boundary

Research material only. Presence in this repository does not imply profitable alpha, successful validation, implementation approval, paper/testnet/live approval, or authorization to trade.

## Related Wiki records

No Hermes Wiki Brain record was consulted or fabricated in this GitHub-only Scout cycle.

## Sources

- TradingView — `nathanfarmer`, **Dynamic RSI Mean Reversion Strategy**: https://www.tradingview.com/script/K9FLcueo-Dynamic-RSI-Mean-Reversion-Strategy/ (published/updated Nov 4, 2024; public open-source strategy; reviewed 2026-09-17).
