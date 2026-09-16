---
schema: strategy-research-record-v1
title: "TradingView Keltner / EMA200 / ADX / Volume Volatility Breakout"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-16
sources:
  - https://www.tradingview.com/script/36zwwSMa-Volatility-Breakout-System-Fixed-Risk/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Keltner / EMA200 / ADX / Volume Volatility Breakout

## Provenance

Public TradingView open-source strategy **Volatility Breakout System [Fixed Risk]**, published by `debdaspt85`. Stable source URL: https://www.tradingview.com/script/36zwwSMa-Volatility-Breakout-System-Fixed-Risk/. Source reviewed 2026-09-16; the TradingView page showed the script updated Jan 31.

## Economic mechanism
### Source-reported

The author describes a trend-following volatility-breakout system intended to capture volatility expansion while filtering low-momentum chop. A close outside the Keltner Channel is treated as the breakout; direction relative to the 200 EMA supplies trend bias; ADX supplies trend-strength confirmation; and volume above its moving average supplies participation confirmation.

### Research interpretation

The falsifiable hypothesis is that a volatility-band breakout has more continuation value when three conditions agree: prevailing trend direction (EMA200), non-trivial trend strength (ADX), and above-normal participation (volume). The components therefore have distinct roles rather than being an arbitrary indicator stack: Keltner = primary breakout trigger; EMA200 = directional regime filter; ADX = strength filter; volume = participation confirmation.

## Signal

Source-reported core logic:

- Primary trigger: a candle closes outside the Keltner Channel.
- Direction filter: trades are taken only in the direction of the 200 EMA. The exact comparison/operator for long versus short is not stated in the reviewed prose and is therefore **underspecified** here.
- Strength filter: ADX must exceed a threshold; the source states default `20`.
- Volume filter: current volume must be above a volume moving average; the moving-average type and length are **underspecified** in the reviewed prose.
- Risk/exit layer: ATR-based stop loss, a trailing stop after favorable movement, and a breakeven move after price advances by a configurable percentage.
- Cooldown: the source includes a post-signal cooldown, but its duration/trigger details are **underspecified** in the reviewed prose.
- The source exposes separate long-entry, long-exit, short-entry and short-exit alerts, confirming bidirectional trade states.

Exact Keltner basis/length/multiplier, ATR length/multiplier, trailing activation/distance, breakeven percentage, volume-MA parameters, order timing, and cooldown values were not recoverable from the reviewed public description. They must not be silently invented. The source recommends higher timeframes such as 1H or 4H for more accurate backtest handling with bar magnifier, but this is not evidence that those horizons are optimal.

## Required data

Minimum source-implied inputs are timestamped OHLCV bars sufficient to calculate Keltner Channels, EMA200, ADX, ATR and a volume moving average. Venue and instrument are not restricted by the reviewed source. Point-in-time research must form every indicator from information available no later than the signal bar close and must not use future bars.

## Execution assumptions

The public description specifies a candle **closing** outside the Keltner Channel as the trigger, so a leakage-safe implementation should not assume an intrabar breakout was known before that close. Exact order placement/fill timing after confirmation is **underspecified**. The source notes `use_bar_magnifier=true` and recommends 1H/4H or suitable intrabar inspection for backtesting. Fees, spread, slippage, market impact, funding, leverage/margin, partial fills and crypto-specific perpetual funding are not specified in the reviewed description and must be modeled explicitly in later testing.

## Evidence
### Source-reported

The TradingView author presents the system as a volatility-expansion trend-following strategy and states the filters are intended to avoid weak/choppy signals. No source-reported performance statistic is carried into this record because none was required to state the hypothesis faithfully.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself identifies low-momentum/choppy conditions as the failure environment the ADX filter is intended to reduce. No independent evidence was reviewed in this Scout cycle; absence of additional negative evidence is not evidence of robustness.

## Falsification plan

Test the full rule against a plain Keltner close-breakout baseline using the same universe, execution model and costs. Predeclare ablations for EMA200, ADX and volume filters so incremental contribution is measurable rather than assumed. Require strictly out-of-sample evaluation across trend, range, high-volatility and low-volatility regimes. Stress fees/slippage and, for perpetuals, funding. The hypothesis is materially weakened if the combined filters do not improve out-of-sample risk-adjusted results or drawdown/false-breakout behavior relative to the simpler breakout after accounting for reduced trade count, or if gains disappear under realistic costs.

## Crypto portability

`adapted`. The rule uses generic OHLCV-derived indicators and can be evaluated on crypto spot or perpetual bars, but the reviewed source does not establish crypto-specific empirical validity. Crypto testing must account for 24/7 candle boundaries, venue-specific volume, fragmented liquidity, and perpetual funding/mark-price conventions where applicable.

## Limitations

Several implementation parameters are **underspecified** in the public prose even though the source is labeled open-source on TradingView. This record intentionally does not reconstruct or redistribute the Pine source code. The economic rationale and high-level signal path are sufficiently explicit for a research hypothesis, but an implementation must resolve missing parameters from the public source or label any chosen values `research-proposed` before testing. Not independently reproduced.

## Implementation status

No implementation or backtest in the user's quantitative research stack has been performed for this record.

## Adoption boundary

Research material only. Presence in this repository does not imply profitable alpha, successful validation, implementation approval, paper/testnet/live approval, or authorization to trade.

## Related Wiki records

No stable Hermes Wiki record was consulted or fabricated in this GitHub-only Scout cycle.

## Sources

- TradingView — `debdaspt85`, **Volatility Breakout System [Fixed Risk]**: https://www.tradingview.com/script/36zwwSMa-Volatility-Breakout-System-Fixed-Risk/ (reviewed 2026-09-16; public open-source strategy page; page showed update Jan 31).
