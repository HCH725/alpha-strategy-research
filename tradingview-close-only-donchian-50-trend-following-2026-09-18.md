---
schema: strategy-research-record-v1
title: "TradingView Close-Only Donchian 50 Trend Following"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - trend-following
  - breakout
  - donchian
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - https://www.tradingview.com/script/YPQwKNF8-Donchian-Quest-Research/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Close-Only Donchian 50 Trend Following

## Provenance

Public TradingView open-source strategy **Donchian Quest Research**, author `sergeyen`. Stable source URL: https://www.tradingview.com/script/YPQwKNF8-Donchian-Quest-Research/. The page shows initial publication Dec 6, 2023 and update Jul 14, 2024. Source reviewed 2026-09-18.

GitHub dedup on current `main` found no record containing TradingView script identity `YPQwKNF8` or the normalized close-only 50-bar channel rule. This record normalizes the public description and does not reproduce the Pine source.

## Economic mechanism

### Source-reported

The author presents a trend-following breakout strategy derived from the Donchian concept but intentionally calculates channel extremes from **Close** prices rather than High/Low. The stated rationale is to reduce reactions to volatile candle wicks or alleged "stop hunting" and require a closing-price breakout before recognizing a trend. The source also states that two channels are conceptually used, one for opening and one for closing trades.

### Research interpretation

The falsifiable hypothesis is that closing-price extremes contain a cleaner persistence signal than intrabar High/Low extremes in markets with frequent transient wicks. Replacing conventional high/low Donchian boundaries with rolling close extrema may reduce false breakout transitions at the cost of discarding genuine intrabar information and potentially changing entry timing.

The relevant alpha question is therefore not generic Donchian trend following alone, but whether the **close-only formation rule** improves out-of-sample trend capture after costs relative to an otherwise matched High/Low Donchian baseline.

## Signal

Source-reported default rule:

- Default opening-channel length: `50` candles.
- Default closing-channel length: `50` candles.
- Channel inputs use **Close prices**, not High/Low.
- **Open long:** the latest Close equals the maximum Close across the 50-close channel.
- **Close long:** the latest Close equals the minimum Close across the 50-close channel.
- **Open short:** the latest Close equals the minimum Close across the 50-close channel.
- **Close short:** the latest Close equals the maximum Close across the 50-close channel.

The public description says the opening and closing channels are separate and gives 50 as the default length for both, implying their lengths may be configurable; exact allowable parameter ranges are not stated.

The description does not resolve whether the rolling extremum includes the current bar before comparison or references a prior completed channel, nor the exact order-placement/fill timing after a qualifying close. Those details are **underspecified** and must not be invented.

`research-proposed` causal convention for later testing, if source-code inspection has not first resolved the ambiguity: compare the completed signal-bar close with the channel formed strictly from prior completed bars and execute no earlier than the next bar. This convention is not source-reported.

Position sizing, pyramiding, cooldown/re-entry behavior beyond the opposite channel transition, leverage, and separate protective stops are **underspecified** in the reviewed prose.

## Required data

Minimum signal data are timestamped closing prices at the chosen bar frequency. Full OHLC data are required for a fair matched comparison with conventional High/Low Donchian channels and for realistic execution simulation.

The source does not mandate a particular instrument, venue, market type, or timeframe. The TradingView page categorizes the strategy as general trend following. Point-in-time testing must form each rolling channel only from data available at the signal timestamp and must fix candle boundaries before reproduction.

## Execution assumptions

The source defines signal states using the latest Close, so the breakout cannot be known as a completed-bar event before that close. Exact post-close order timing, market/limit order type, fill price, fees, spread, slippage, impact, leverage/margin, short borrow/funding, partial fills and latency are not specified.

A leakage-safe implementation must not use the completed signal close as a guaranteed executable fill unless source semantics and the execution model justify it. Crypto-perpetual testing would additionally require funding and mark/index conventions even though these are not part of the source signal.

## Evidence

### Source-reported

The author states that using Close rather than High/Low is intended to avoid reacting to volatile wicks and that openings often occur earlier than with a conventional Donchian channel while closes require a "real breakout." These are source claims, not independently verified findings. No traceable Sharpe, CAGR, drawdown, profit factor, win rate, or other performance statistic is carried into this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source provides no independent comparison establishing that close-only channels outperform conventional Donchian channels. Close-only construction can also ignore economically meaningful intrabar extremes, so any claimed reduction in false breaks may be offset by delayed or altered trend recognition. No independent negative study was reviewed in this Scout cycle; absence is not evidence of no negative result.

## Falsification plan

1. Recover exact channel indexing and order semantics from the public source before claiming exact reproduction; otherwise preserve the causal convention as `research-proposed`.
2. Compare close-only Donchian against a matched High/Low Donchian baseline using identical opening/closing lengths, universe, execution and costs.
3. Predeclare separate measurements for false-break frequency, trade count, average holding period, turnover, drawdown and risk-adjusted return so lower activity is not automatically mistaken for better alpha.
4. Test multiple channel lengths around the source default without broad post-hoc optimization and evaluate long and short legs separately.
5. Require out-of-sample coverage across persistent trends, high-wick/high-volatility periods and sideways regimes.
6. Stress spread/slippage and, for perpetuals, funding. The close-only thesis is materially weakened if its apparent advantage disappears after matched costs or if it does not outperform the conventional channel on the specific false-break/continuation outcomes it is intended to improve.

## Crypto portability

`adapted`.

The source presents a generic trend-following construction rather than crypto-specific empirical evidence. The mechanism is straightforward to port to liquid crypto spot or perpetual OHLC bars, but crypto's 24/7 candle boundaries, venue fragmentation, frequent wicks, liquidation-driven extremes, perpetual funding and mark/index conventions can materially change both the hypothesized benefit of ignoring wicks and the execution result. Those effects require direct crypto testing.

## Limitations

- Exact channel indexing/current-bar inclusion is **underspecified** in the reviewed public description.
- Exact signal-to-order/fill timing is **underspecified**.
- Instrument, venue, market type and timeframe are **underspecified**.
- Position sizing, pyramiding, protective stop and leverage rules are **underspecified**.
- The source rationale concerning wick filtering has not been independently validated.
- Not independently reproduced.

## Implementation status

`not-implemented`.

No implementation or backtest in the user's quantitative research stack was performed in this Scout cycle.

## Adoption boundary

Research material only. Presence in this repository does not imply profitable alpha, successful validation, implementation approval, paper/testnet/live approval, or authorization to trade.

## Related Wiki records

No Hermes Wiki Brain record was consulted or fabricated in this GitHub-only Scout cycle.

## Sources

- TradingView — `sergeyen`, **Donchian Quest Research**: https://www.tradingview.com/script/YPQwKNF8-Donchian-Quest-Research/ (public open-source strategy; published Dec 6, 2023; updated Jul 14, 2024; reviewed 2026-09-18).
