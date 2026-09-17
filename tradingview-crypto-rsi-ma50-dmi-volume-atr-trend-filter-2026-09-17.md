---
schema: strategy-research-record-v1
title: "TradingView Crypto RSI / MA50 / DMI / Volume / ATR Trend Filter"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - crypto
  - trend-following
  - momentum
status: research-only
confidence: medium
source_as_of: 2026-09-17
sources:
  - https://www.tradingview.com/script/i5cYs2nw/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Crypto RSI / MA50 / DMI / Volume / ATR Trend Filter

## Provenance

- **Source:** public TradingView open-source strategy, `MS - Crypto RSI-Based Trading Strategy`.
- **Author/page identity:** `mertk9l7m`.
- **Stable URL:** https://www.tradingview.com/script/i5cYs2nw/
- **Published:** 2025-09-07 according to the public TradingView page.
- **Reviewed / source as-of:** 2026-09-17.
- TradingView labels the page `OPEN-SOURCE SCRIPT`; this record normalizes the public description and does not redistribute the Pine source.
- GitHub dedup on current `main` found no record for canonical TradingView script ID `i5cYs2nw`. The repository contains other trend/momentum composites, but no materially same normalized rule combining the source's MA50 buffer, bounded RSI state, DMI direction, 1.5x volume participation gate, and below-average ATR gate.

## Economic mechanism

### Source-reported

The author describes the system as a cryptocurrency trend-following and momentum strategy that combines trend direction, momentum, directional movement, market participation and volatility filtering. The stated purpose is to filter market noise and require multiple conditions to agree before entry.

### Research interpretation

The falsifiable hypothesis is that trend continuation is more reliable when five roles align rather than when price trend alone is used:

- **Regime:** price relative to MA50 with a stated 5% buffer.
- **Momentum state:** RSI is positive but not at the source's overbought boundary.
- **Directional confirmation:** `+DI > -DI`.
- **Participation:** volume is elevated relative to its moving average.
- **Volatility state:** ATR is below its own average, intended by the source to exclude excessive volatility.

The distinctive research question is whether the low-volatility gate plus participation and directional confirmation improves subsequent continuation conditional on an already-positive price/MA and RSI state. This is not evidence that each filter independently contributes alpha; ablation is required.

## Signal

### Source-reported entry

The public description states that **all** of the following must be true for a buy signal:

1. Current price is above `MA50` with a `5%` buffer.
2. RSI is between `50` and `70`.
3. `+DI > -DI`.
4. Current volume is `1.5x` its moving average.
5. ATR is below its average.

The exact mathematical interpretation of the `5% buffer` and whether `1.5x` means `>= 1.5 × volume_MA` are not restated beyond the source prose; exact operators should be recovered from the public Pine source before exact reproduction.

### Source-reported exit

The public description states that **any one** of the following can produce a sell/exit condition:

1. Price drops below MA50 with the stated 5% buffer.
2. RSI drops below `45`.
3. `-DI` crosses above `+DI`.
4. Volume drops below `50%` of its moving average.
5. ATR rises above its average.

### Specification boundary

- MA length `50`, RSI entry range `50–70`, RSI exit threshold `45`, entry volume multiple `1.5x`, and exit volume multiple `0.5x` are source-reported.
- RSI lookback, DMI/ADX calculation lengths, volume-moving-average type/length, ATR lookback, ATR-average type/length, exact MA type despite the source's generic `MA` wording, timeframe, and exact buffer formula are **underspecified** in the reviewed prose.
- The public description presents buy and sell conditions but does not clearly establish a symmetric short-entry system. This record therefore does not invent a short rule.
- Formation timestamp, same-bar versus next-bar execution, re-entry, pyramiding, sizing and cooldown are **underspecified**.
- `research-proposed` causal convention for later testing: compute all indicators on completed bars and execute no earlier than the next bar unless source-code inspection establishes a different causal sequence. This convention is not source-reported.

## Required data

- **Asset class:** cryptocurrency.
- **Instrument / universe:** no exact symbol or universe is mandated by the reviewed source description.
- **Venue / market type:** `underspecified`; spot versus perpetual/futures is not fixed by the source prose.
- **Timeframe:** `underspecified`.
- **Fields:** timestamped OHLCV sufficient for MA, RSI, DMI and ATR calculations; volume is materially required.
- **Point-in-time requirement:** all indicators and rolling averages must use only data available at the signal timestamp.
- **Missing-data assumption:** `underspecified`; later testing must define treatment of missing candles/volume.
- **Crypto timestamp requirement:** candle boundaries and timezone must be fixed because 24/7 venue aggregation can change indicator states.

## Execution assumptions

The reviewed public description does not specify order type, exact signal-to-fill timing, fill model, fees, spread, slippage, latency, impact, leverage, margin, borrow, partial fills or failures. Those are therefore **underspecified** and must be modeled explicitly in later research.

If tested on perpetual futures, funding and mark/index-price conventions must be added to the execution model; they are not part of the source-reported signal. If tested on spot, no short leg should be inferred from the sell/exit rule without separate source evidence.

## Evidence

### Source-reported

The author characterizes the strategy as designed for cryptocurrency trend-following/momentum and states that the filters are intended to remove noise and generate higher-quality signals. No source-reported Sharpe, CAGR, drawdown, profit factor or win-rate figure is carried into this record because the reviewed public page does not provide a sufficiently traceable empirical statistic needed to state the hypothesis.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source supplies a multi-filter construction but does not establish that each filter contributes incremental predictive value.
- Several indicator calculation lengths and moving-average definitions are not specified in the reviewed prose.
- Requiring high relative volume while simultaneously requiring ATR below its average may substantially reduce trade count; whether that interaction improves continuation is unproven.
- The source does not provide a clear symmetric short-entry rule in the reviewed description.
- No independent cost-adjusted or out-of-sample evidence was produced in this Scout cycle.

## Falsification plan

1. Recover exact indicator lengths, MA definitions, buffer formula, crossover semantics and order timing from the public Pine source before claiming exact reproduction.
2. Compare the full rule with a simple `price > MA50` trend baseline using identical data, execution and costs.
3. Run predeclared ablations for RSI, DMI, volume and ATR gates individually and in sensible groups; the composite thesis is weakened if added filters do not improve out-of-sample risk-adjusted continuation after accounting for lower trade count.
4. Specifically test the interaction `volume >= 1.5x average` with `ATR below average`; reject the claimed filtering benefit if it merely selects rare observations without stable out-of-sample advantage.
5. Test across bull, bear, range, high-volatility and low-volatility crypto regimes, with multiple liquid assets and venues.
6. Stress fees, spread and slippage; add funding for perpetuals.
7. Require strictly point-in-time out-of-sample evaluation. Failure to outperform the simpler trend baseline after realistic costs materially weakens the hypothesis.

## Crypto portability

`direct`. The cited source explicitly presents the strategy as designed for cryptocurrency markets.

Implementation portability still depends on venue and market type. Volume is venue-specific in fragmented crypto markets; perpetuals add funding and mark/index mechanics; spot and derivatives differ in shorting feasibility; and 24/7 candle boundaries can alter MA, RSI, DMI and ATR states.

## Limitations

- RSI, DMI, volume-MA and ATR-average calculation details are partially **underspecified** in the reviewed prose.
- Exact interpretation of the MA50 `5% buffer` is **underspecified**.
- Timeframe, venue and market type are **underspecified**.
- Exact signal-to-order timing, fills, costs and sizing are **underspecified**.
- No symmetric short-entry rule is asserted because it is not clearly supplied by the reviewed description.
- Not independently reproduced.
- Research-only; profitability is unproven.

## Implementation status

`not-implemented`.

No backtest, quantitative-runtime change, paper trade, testnet or live implementation was performed in this Scout cycle.

## Adoption boundary

Research material only. Presence in this repository does not mean validated alpha, implementation approval, paper/testnet/live approval, or authorization to trade.

## Related Wiki records

No stable Hermes Wiki record was consulted or fabricated in this GitHub-only Scout cycle.

## Sources

- TradingView — `mertk9l7m`, **MS - Crypto RSI-Based Trading Strategy**: https://www.tradingview.com/script/i5cYs2nw/ (published 2025-09-07; public open-source strategy; reviewed 2026-09-17).
