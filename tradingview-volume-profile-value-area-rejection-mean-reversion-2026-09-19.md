---
schema: strategy-research-record-v1
title: TradingView Volume-Profile Value-Area Rejection Mean Reversion
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-19
sources:
  - https://www.tradingview.com/script/89On6rru-Volume-Profile/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Volume-Profile Value-Area Rejection Mean Reversion

## Provenance

Public TradingView open-source script/research page by **alphachart_tv**, titled **Volume Profile**:

https://www.tradingview.com/script/89On6rru-Volume-Profile/

TradingView displays the publication label `Apr 4`; the reviewed page text does not expose a publication year, so no year is inferred. Source as-of date: 2026-09-19.

The source is a public indicator rather than a complete trading strategy. This record normalizes the publicly described value-area rejection hypothesis without reproducing Pine source code.

Repository deduplication found an existing volume-profile breakout/POC-reclaim continuation record from a different TradingView source. This record is materially distinct: its primary hypothesis is **rejection at VAH/VAL and reversion toward accepted value**, rather than post-breakout continuation after a frozen POC reclaim.

## Economic mechanism

### Source-reported

The author describes a volume-at-price profile in which POC is the highest-volume price row and a 70% value area defines VAH and VAL. The page characterizes POC as a price magnet/support-resistance reference, VAL as support, VAH as resistance, and prices outside the value area as potentially overextended or breaking out. It provides automatic POC bounce, VAL bullish-rejection and VAH bearish-rejection conditions.

The profile can be rolling, session-anchored, or week-anchored. Each bar's volume is distributed proportionally across the price rows spanned by that bar. The source states calculations use confirmed bar data and do not use future data.

### Research interpretation

The falsifiable hypothesis is that a failed excursion into or through a completed/point-in-time value-area boundary contains information about short-horizon reversion toward locally accepted price, beyond ordinary price reversal or distance-from-moving-average effects.

Component roles:

- Structural context: volume-at-price distribution.
- Acceptance reference: POC and the 70% value area.
- Primary event: interaction with VAH or VAL followed by rejection back toward value.
- Competing mechanism: an excursion beyond VAH/VAL may instead represent genuine price discovery and continuation.

The alpha claim therefore cannot be assumed from the label `rejection`; reversal and continuation must be tested as competing outcomes.

## Signal

The public page specifies the following source-level logic qualitatively:

- POC Bounce Up: price touches POC and reverses upward.
- POC Bounce Down: price touches POC and reverses downward.
- VAL Rejection: price tests VAL and bounces upward.
- VAH Rejection: price tests VAH and bounces downward.

Profile construction:

- Value area: 70% of profile volume.
- Configurable rows: 10-50.
- Rolling anchor: recalculated over the last `N` bars.
- Session anchor: resets each trading day.
- Week anchor: resets each trading week.
- Auto-timeframe settings reported by the source: 1-5m uses lookback 30 / 18 rows; 15-30m uses 40 / 20; 1h uses 50 / 24; 4h uses 70 / 28; daily uses 100 / 32; weekly+ uses 150 / 40.

The reviewed description does **not** fully specify the exact Boolean definition of `touches`, `tests`, `reverses`, or `bounces`, nor a canonical entry price, exit, holding period, stop, re-entry rule, or position sizing. Those items are **underspecified** and are not invented here.

A future operationalization may define bar-close-confirmed rejection and a fixed forward horizon, but any such choice is **research-proposed**, not source-reported.

## Required data

- OHLCV bars for the traded instrument.
- Chart-timeframe volume.
- Bar-close timestamps.
- Session/day and week boundary definitions for anchored modes.
- Point-in-time profile state at each decision timestamp.

The source states that bar volume is allocated proportionally across price rows spanned by the bar. This is an approximation to true traded volume-at-price and should not be treated as tick-level footprint data.

For crypto, venue identity matters because exchange-specific volume distributions can differ. Session boundaries also require an explicit timezone convention in a 24/7 market.

## Execution assumptions

The source describes an indicator and alert conditions, not an execution model. It states the profile uses confirmed bar data and that rolling profiles use historical high/low/volume without future data.

Material execution assumptions are **underspecified**, including:

- exact signal-to-order timestamp;
- same-close versus next-bar execution;
- market versus limit orders;
- fees, spread and slippage;
- market impact/capacity;
- partial fills and failures;
- perpetual funding, leverage and margin;
- exit and stop mechanics.

A leakage-safe test should act no earlier than the first timestamp at which the rejection is actually confirmed.

## Evidence

### Source-reported

The source describes POC/VAH/VAL construction and labels POC bounce, VAL rejection and VAH rejection as actionable alert conditions. It states that the indicator works on crypto, forex, stocks, futures and indices from 1-minute to monthly timeframes, and describes its calculations as non-repainting.

No Sharpe, CAGR, drawdown, win rate, t-statistic, or other source-reported performance statistic is relied upon here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself presents prices outside the value area as potentially either **overextended or breaking out**. That ambiguity is directly contrary to treating every VAH/VAL excursion as a mean-reversion event.

The profile is also constructed from bar OHLCV by distributing each bar's volume across price rows, rather than from actual transaction-level volume-at-price. This measurement approximation can move POC/VAH/VAL and alter apparent rejection events.

No independent negative empirical result was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

Test the hypothesis on liquid crypto spot and perpetual instruments, with point-in-time profile construction and realistic costs. Pre-register simple rejection definitions and forward horizons rather than selecting them after observing results.

Required controls and ablations:

1. VAH/VAL rejection versus unconditional short-horizon reversal after an equal-sized price move.
2. VAH/VAL rejection versus distance-from-rolling-mean or z-score mean reversion.
3. Volume-profile boundary versus price-only rolling high/low or quantile boundary.
4. VAH/VAL rejection versus POC bounce.
5. Rolling versus session versus weekly profile anchoring.
6. Source-style bar-volume allocation versus higher-resolution volume-at-price when available.
7. Reversal versus continuation following excursions outside the value area.
8. Venue-specific profiles versus a consistent reference venue for crypto.

Evaluate out-of-sample expectancy, risk-adjusted return, hit rate conditional on symmetric payoff definitions, adverse/favorable excursion, turnover and cost sensitivity. Split results by volatility/trend regime and by spot/perpetual market type.

The hypothesis is materially weakened if VAH/VAL rejection does not add stable out-of-sample information beyond simple price-only reversal controls; if the sign flips across reasonable anchors/row counts; if higher-resolution volume-at-price removes the effect; or if realistic fees/slippage/funding consume the expectancy. Failure should lead to rejection or reformulation, not threshold mining.

## Crypto portability

`direct`

The source explicitly states that the indicator works on crypto, so the mechanism is directly applicable as a crypto research hypothesis. This is **not** evidence that it is profitable in crypto.

Crypto-specific risks include 24/7 session definitions, fragmented venue volume, spot/perpetual differences, funding, mark/index versus traded price, exchange-specific liquidity, and unstable volume profiles during thin-liquidity periods.

## Limitations

- Not independently reproduced.
- The source is an indicator, not a complete strategy.
- Exact bounce/rejection Boolean logic is underspecified in the reviewed description.
- Entry, exit, holding, sizing and execution are underspecified.
- Volume-at-price is approximated from chart-bar volume rather than transaction-level footprint data.
- The source publication label exposes `Apr 4` but not the year in the reviewed page text.
- Reversal and breakout/continuation are competing interpretations at value-area boundaries.
- Cross-venue crypto portability remains empirically unverified.

## Implementation status

No implementation in our research stack has been completed. No backtest, paper, testnet or live verification is claimed.

## Adoption boundary

Research material only. Presence in this repository does not imply profitability, validated alpha, implementation approval, paper/testnet approval, or live-trading approval.

## Related Wiki records

None linked; no stable Hermes Wiki Brain page was verified or accessed under this GitHub-only workflow.

## Sources

- alphachart_tv, **Volume Profile**, TradingView public open-source script/research page, reviewed 2026-09-19: https://www.tradingview.com/script/89On6rru-Volume-Profile/
