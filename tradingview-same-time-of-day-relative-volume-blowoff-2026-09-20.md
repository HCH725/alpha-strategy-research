---
schema: strategy-research-record-v1
title: TradingView Same-Time-of-Day Relative Volume and Blow-Off Regime
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-20
sources:
  - https://www.tradingview.com/script/iGvkBAD4-RVOL-by-Bar/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Same-Time-of-Day Relative Volume and Blow-Off Regime

## Provenance

Public TradingView open-source indicator **RVOL by Bar** by `jjdomino23` (page identity also shows James Domino, CMT). Stable public URL: https://www.tradingview.com/script/iGvkBAD4-RVOL-by-Bar/ . The reviewed TradingView page displays publication date `Mar 10` without a visible year, so no publication year is inferred. Source reviewed and preserved as of 2026-09-20.

Canonical TradingView script ID: `iGvkBAD4`.

The source describes a same-bar relative-volume baseline: each intraday bar is compared with the corresponding time-of-day bar across the prior N sessions/days instead of with a generic rolling-volume average. It also classifies price direction together with above/below-average volume and flags statistically unusual `blow-off` volume using a standard-deviation threshold.

## Economic mechanism

### Source-reported

The author states that intraday volume has strong time-of-day seasonality, so comparing a bar with an ordinary rolling volume average can be misleading. The same-time-of-day baseline is intended to normalize that seasonality. The source further describes price-direction/relative-volume coloring as a way to distinguish confirmed versus weak moves and labels unusually high volume as blow-off activity.

### Research interpretation

The falsifiable hypothesis is that **time-of-day-normalized participation contains incremental information beyond raw volume and ordinary rolling relative volume**. Two competing mechanisms should be tested rather than assumed:

1. **Participation-confirmed continuation:** a directional price move accompanied by unusually high same-time-of-day relative volume may continue because participation is unusually strong after controlling for the normal intraday volume curve.
2. **Blow-off exhaustion:** sufficiently extreme same-time-of-day volume may instead mark crowded terminal participation and predict short-horizon reversal or volatility decay.

A third null explanation is that the signal merely identifies high realized-volatility bars and has no incremental directional content after controlling for absolute return and volatility.

## Signal

Source-supported normalized construction:

- Formation: intraday, from the current chart bar and historical bars occupying the same time-of-day slot in prior sessions/days.
- Baseline: average volume for the corresponding bar/time slot over the prior `N` days/sessions. The reviewed page does not expose the default `N`; it is `underspecified`.
- Relative-volume state: current volume relative to its same-slot historical average.
- Directional context: the source colors volume bars by price direction together with whether volume is above or below average, describing this as confirmation versus weakness context.
- Blow-off state: statistically unusual volume above the historical average using a standard-deviation threshold. The exact multiplier/default is not exposed in the reviewed page text and is `underspecified`.
- Extended-hours/session handling: the source states that bars-per-day calculations adjust dynamically for pre/post-market sessions.
- Asset scope: source states multi-asset handling for stocks, futures, and crypto with session-aware time calculations.
- Long entry: not specified by the source.
- Short entry: not specified by the source.
- Exit / holding period: not specified.
- Re-entry: not specified.
- Position sizing: not specified.

`research-proposed`: treat the same-slot RVOL state and blow-off state as explanatory/event variables first, not as completed trading rules. Predeclare forward-return horizons and test continuation versus reversal symmetrically. Any eventual threshold, entry, exit, holding, or sizing rule introduced for research must remain explicitly `research-proposed` rather than source-reported.

## Required data

- Intraday OHLCV bars.
- Exact timestamps sufficient to align the same time-of-day slot across prior sessions/days.
- Session/calendar information where the market has regular and extended sessions.
- Enough prior sessions for the selected `N`-session same-slot baseline.
- For crypto: continuous 24/7 venue-specific OHLCV and a predeclared UTC/session anchor; venue and candle-boundary conventions must remain fixed point-in-time.
- Missing-bar handling is not specified by the source and must be predeclared before testing.

## Execution assumptions

The source is an indicator rather than a complete execution strategy and does not specify signal-to-order timing, market versus limit orders, same-bar versus next-bar fills, fees, spread, slippage, impact/capacity, funding, leverage, borrow/shorting, latency, or partial fills.

`research-proposed`: if directional tests are later converted into trades, form the signal only after the relevant bar volume is finalized and execute no earlier than the next causally available price. For perpetuals, include fees, slippage and funding. These are research controls, not source-reported execution rules.

## Evidence

### Source-reported

The source provides the indicator construction and qualitative interpretation but no traceable Sharpe, CAGR, drawdown, win rate, t-statistic, or other strategy-performance statistic in the reviewed page text. It states that the indicator supports crypto as well as stocks and futures.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source does not establish that same-slot RVOL predicts returns rather than merely contemporaneous activity. It also does not establish whether a blow-off event should imply continuation or reversal. For 24/7 crypto, conventional equity-style open/midday/close seasonality does not transfer mechanically; any intraday periodicity can depend on UTC hour, regional trading overlap, venue, weekday and event calendar. None of these caveats is resolved by the source.

No independent negative empirical result was established during this Scout cycle; absence is not evidence of no negative result.

## Falsification plan

Test on liquid crypto spot and/or perpetual markets with point-in-time OHLCV and predeclared UTC candle boundaries.

1. Compare **raw volume**, ordinary rolling RVOL, and **same-time-of-day RVOL** using identical forward-return horizons.
2. Test same-slot RVOL conditional on price direction for continuation and reversal separately; do not choose the winning sign after seeing results.
3. Test blow-off events as competing outcomes: continuation, reversal, and volatility-only response.
4. Ablate `price direction -> + ordinary RVOL -> + same-slot RVOL -> + blow-off extremeness` to measure incremental information.
5. Control for absolute return, realized volatility, ordinary volume z-score, weekday and UTC hour.
6. `research-proposed` placebo: circularly shift the time-of-day labels or compare each bar with a deliberately wrong time slot while preserving the marginal volume distribution. The same-slot mechanism is weakened if the correctly aligned baseline does not outperform these controls.
7. Repeat across venues and multiple liquid assets. Treat venue-specific volume as venue data, not universal crypto volume.
8. Use out-of-sample periods and realistic transaction costs for any trading operationalization.

The hypothesis is materially weakened if same-time-of-day normalization adds no stable out-of-sample information beyond ordinary rolling RVOL/volatility controls, or if any apparent effect disappears under causal bar-close timing and neighboring parameter choices.

## Crypto portability

direct

The source explicitly states support for crypto. The economic transfer is nevertheless unproven: crypto is 24/7, lacks a universal session open, and has venue-fragmented volume. A crypto test therefore requires a fixed UTC/session convention and should verify that same-time-of-day seasonality actually exists before attributing predictive meaning to the normalized signal.

## Limitations

- Default prior-session lookback `N` is `underspecified` in the reviewed page text.
- Exact standard-deviation blow-off multiplier/default is `underspecified`.
- No source-specified entry, exit, holding, re-entry, or sizing rule.
- Same-slot history and missing-bar implementation details are not fully specified in the reviewed prose.
- Crypto's 24/7 session structure can weaken or alter the source's intraday-seasonality rationale.
- The indicator uses bar volume, not aggressor-side trades, order-book depth, or consolidated cross-venue volume.
- Not independently reproduced.

## Implementation status

Not implemented in the research stack. This Scout did not run a backtest, change quantitative runtime code, create a production/Kanban task, or perform Paper, Testnet, or Live validation.

## Adoption boundary

Research-only. Presence in this repository does not mean the record passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor/leaderboard entry, demonstrated profitable alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted from this GitHub-only Scout run; none is fabricated.

Repository-level conceptual neighbors include existing price/volume breakout and volume-regime records, but this record is differentiated by its material data dependency on **same-time-of-day historical alignment** and its explicit test of time-seasonality normalization versus ordinary rolling relative volume.

## Sources

- TradingView — **RVOL by Bar**, `jjdomino23` / James Domino, CMT, page displays `Mar 10` (year not shown in reviewed text), reviewed 2026-09-20: https://www.tradingview.com/script/iGvkBAD4-RVOL-by-Bar/
