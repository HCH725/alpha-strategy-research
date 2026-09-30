---
schema: strategy-research-record-v1
title: "TradingView NQ Overnight-to-Morning Amplitude Regime"
created: 2026-10-01
updated: 2026-10-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-11
sources:
  - https://www.tradingview.com/script/lVGDWz4p-NQ-OVN-AM-Amplitude/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView NQ Overnight-to-Morning Amplitude Regime

## Provenance

Public TradingView open-source indicator **NQ OVN AM Amplitude** by **integrale42**. Stable source: https://www.tradingview.com/script/lVGDWz4p-NQ-OVN-AM-Amplitude/ . The page was published 2026-09-09 and updated 2026-09-11. TradingView canonical script identity: `lVGDWz4p`. Source as-of date: 2026-09-11.

The source explicitly describes itself as a range map, not an entry signal.

## Economic mechanism

### Source-reported

The source partitions Nasdaq futures overnight sessions by whether the 18:00-06:00 New York high-low range is at or above, or below, its trailing 60-session median. It reports that the subsequent 09:30-12:00 morning range scales differently with overnight amplitude: 0.95 times overnight range after a LARGE overnight and 1.93 times overnight range after a SMALL overnight. The author states these multipliers come from an NQ hourly study covering 577 sessions from April 2024 through September 2026.

### Research interpretation

This suggests a falsifiable **conditional volatility-amplitude** hypothesis rather than directional alpha: unusually compressed overnight sessions may leave more unresolved price discovery for the cash morning, producing a larger morning-to-overnight range ratio than already-expanded overnight sessions.

A downstream trading rule is not supplied by the source. Any use of the projected amplitude for entries, targets, option structures, breakout filters, or position sizing would be **research-proposed** and must be tested separately.

## Signal

Source-reported normalization:

- Instrument: NQ1! / MNQ1!.
- Overnight formation window: 18:00-06:00 New York.
- Overnight amplitude: high minus low over that full window, also displayed as a percentage.
- Regime lookback: trailing 60 sessions; classification uses 15-minute history in the background.
- LARGE: overnight range at or above the 60-session median.
- SMALL: overnight range below the 60-session median.
- At 06:00 New York, overnight size and projected morning amplitude lock until the next overnight session.
- Projected 09:30-12:00 morning range: LARGE uses 0.95 x overnight range; SMALL uses 1.93 x overnight range.
- Current morning range updates through 12:00.
- The indicator is intended to run on a 1-minute chart.
- A separate ATR(14) x 2 distance is displayed for risk reference; its timeframe is configurable. It is not evidence for the amplitude hypothesis.

No long/short entry, exit, holding period, re-entry rule, or directional forecast is source-specified. Those fields are **underspecified**. Any conversion from the range forecast into an executable strategy is **research-proposed**.

## Required data

Source-reported requirements:

- Nasdaq futures with overnight-session data, specifically NQ1! / MNQ1!.
- Intraday OHLC sufficient to construct the 18:00-06:00 and 09:30-12:00 New York ranges.
- 15-minute history for the 60-session overnight-range classification.
- 1-minute chart context for the published indicator.
- New York session timestamps with daylight-saving-time-safe timezone handling.

For independent research, contract-roll handling, continuous-futures adjustment policy, missing bars, holiday/half-session handling, and point-in-time session completeness must be specified. These are source gaps.

## Execution assumptions

The source does not define an executable trade. Signal-to-order timing, order type, fill model, spread, commissions, slippage, market impact, leverage, margin, partial fills, latency, and position sizing are therefore **not source-specified**.

For hypothesis testing only, using the 06:00 locked classification to forecast the later 09:30-12:00 realized range is a **research-proposed** causal-timing interpretation. No order should be assumed at 06:00 or 09:30 merely because the forecast exists.

## Evidence

### Source-reported

The author reports an NQ hourly study of 577 sessions from April 2024 through September 2026 and publishes conditional morning-range multipliers of 0.95 for LARGE overnight sessions and 1.93 for SMALL overnight sessions. The TradingView page does not provide, in the reviewed description, dispersion, confidence intervals, statistical significance, out-of-sample results, transaction-cost-adjusted trading returns, or a directional strategy result.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independent negative evidence was identified in the reviewed source. The source itself warns that these are historical medians, not guarantees, and explicitly says the tool is a range map rather than an entry signal. Absence of identified negative evidence is not evidence that none exists.

## Falsification plan

1. Reconstruct NQ/MNQ sessions with New York daylight-saving-safe boundaries and freeze every input at the stated 06:00 information set.
2. Reproduce the 60-session median regime and test whether SMALL sessions have a materially higher subsequent 09:30-12:00 range / overnight-range ratio than LARGE sessions.
3. Primary baseline: unconditional morning-range forecast. Secondary baselines: prior-day realized range, ATR-only forecast, and a continuous regression of morning amplitude on overnight amplitude without a median split.
4. **Research-defined falsification threshold:** reject the discrete-regime hypothesis if the SMALL-versus-LARGE difference is not directionally stable across rolling out-of-sample folds or if its out-of-sample forecast error does not improve over the unconditional baseline.
5. Ablate the 60-session median threshold by testing nearby frozen lookbacks and continuous percentile rank; reject a claimed regime effect if performance depends narrowly on the exact threshold.
6. Segment major volatility regimes, weekdays, contract rolls, holidays, and pre/post macro-announcement mornings to test whether the relation is merely calendar/event exposure.
7. If an executable strategy is later proposed, evaluate it separately with realistic futures fees, spread, slippage, roll mechanics, and latency. Forecast accuracy alone is not trading alpha.
8. Do not retune the published 0.95 and 1.93 multipliers on the test window.

## Crypto portability

**adapted / unproven.**

The source is explicitly NQ/MNQ futures and depends on a U.S. overnight-versus-cash-session partition. Crypto trades 24/7 and has no equivalent Nasdaq cash open, so direct portability is unsupported. A crypto adaptation would require a **research-proposed** session anchor, such as a fixed UTC window or a major regional liquidity transition, and must independently establish that the conditioning mechanism survives venue fragmentation, perpetual funding, and continuous trading.

## Limitations

- The published object is a range forecast/map, not a trading strategy.
- Directional entry and exit semantics are underspecified.
- The 577-session study is source-reported and not independently reproduced.
- The reviewed source does not expose uncertainty estimates or out-of-sample validation for the reported multipliers.
- Continuous-futures construction and roll treatment are a data gap.
- Holiday and shortened-session treatment are a data gap.
- The median split may discretize a relation that is actually continuous.
- Crypto portability is unproven.
- Forecasting realized range does not by itself establish monetizable alpha.

## Implementation status

Research record only. No implementation in the research stack, no Qlib full backtest, and no independent reproduction has been completed.

## Adoption boundary

This record is research-only, not implemented, and not approved. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received Paper, Testnet, or Live approval.

## Related Wiki records

No stable related Hermes Wiki Brain record was identified from the GitHub-only scope; no Wiki link is fabricated.

## Sources

- TradingView, integrale42, **NQ OVN AM Amplitude**: https://www.tradingview.com/script/lVGDWz4p-NQ-OVN-AM-Amplitude/ (published 2026-09-09; updated/source as-of 2026-09-11).
