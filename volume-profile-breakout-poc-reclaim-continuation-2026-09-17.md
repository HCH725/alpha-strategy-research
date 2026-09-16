---
schema: strategy-research-record-v1
title: Volume-Profile Breakout POC-Reclaim Continuation
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-17
sources:
  - https://www.tradingview.com/script/JoK0u4ld-Volume-Profile-Breakout-Continuation/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Volume-Profile Breakout POC-Reclaim Continuation

## Provenance

Public TradingView open-source script/research page by **CodaPro**, titled **Volume Profile Breakout Continuation**:

https://www.tradingview.com/script/JoK0u4ld-Volume-Profile-Breakout-Continuation/

TradingView displayed the publication age as `7 days ago` when reviewed on 2026-09-17; the exact publication timestamp was not exposed in the reviewed page text. Source as-of date: 2026-09-17.

This record normalizes the publicly described mechanism and rules; it does not reproduce or redistribute the Pine source code.

## Economic mechanism

### Source-reported

The author describes a chained state machine rather than independent indicators: ATR-normalized range compression identifies an accumulation region; a volume-at-price profile is built only from bars inside that region; a confirmed breakout fixes the profile levels; price must then pull back into the frozen POC zone and subsequently close back through POC in the breakout direction before an entry is marked. An optional prior-completed higher-timeframe EMA bias filters breakout direction.

### Research interpretation

The falsifiable hypothesis is that a compressed range followed by directional escape and then a successful reclaim of the range's highest-volume acceptance level identifies continuation more selectively than an unconditional breakout. The frozen POC acts as an event-specific acceptance/retest level: a successful reclaim may indicate that the breakout survived a liquidity test, while a close through the opposite value-area edge invalidates that interpretation.

Component roles should remain separate in later testing:

- Regime/event formation: ATR-normalized range compression.
- Structural context: volume profile constructed only over the detected accumulation range.
- Direction formation: confirmed close outside the range.
- Optional filter: prior completed higher-timeframe close versus EMA.
- Primary entry confirmation: pullback into frozen POC tolerance zone followed by confirmed close back through POC in breakout direction.
- Invalidation/risk: opposite value-area edge, wait timeout, TP/SL, maximum holding period and cooldowns.

The incremental research value is the **event-anchored, frozen POC reclaim state machine**, not generic volume profile or generic breakout logic.

## Signal

Signal formation is bar-close based according to the source.

1. Examine the last `N` bars. If their price range is at or below `k × ATR`, open an accumulation box.
2. Grow the box while price remains within the allowed accumulation state. Abandon it if expansion exceeds an author-defined abandon threshold or the setup exceeds its maximum duration.
3. During accumulation, construct a volume-at-price histogram using only accumulation bars. The source spreads each bar's volume evenly across the profile rows intersected by that bar's high-low range. The highest-volume row is POC; the value area expands outward from POC to the selected percentage.
4. A confirmed close above/below the accumulation box forms a long/short breakout. If the optional HTF filter is active, long requires the previous completed HTF close above its EMA and short requires it below its EMA.
5. At breakout, freeze POC, VAH and VAL.
6. Wait for price to revisit a POC zone whose tolerance is parameterized as a percentage of accumulation-range height.
7. Long trigger: after the qualifying pullback, a confirmed close back through frozen POC in the breakout direction. Short trigger is symmetric.
8. Invalidate a waiting setup if price closes through the far edge of the frozen value area or the maximum pullback wait expires.
9. Source trade-management options include fixed-percentage or ATR-multiple TP/SL, maximum bars in trade, entry cooldown, optional post-exit cooldown by exit type, and New-York-time end-of-day flattening.

Parameters exposed by the source include range lookback, compression multiple, minimum/maximum accumulation bars, abandon multiple, ATR length, profile rows, value-area percentage, HTF timeframe/EMA length, POC-zone half-width, maximum pullback wait, TP/SL mode and values, maximum bars in trade, cooldowns, and end-of-day flatten time.

Exact default numeric values are **underspecified** in the reviewed public description and are not inferred here. The source states that defaults are only a starting point for one instrument, not an optimized recommendation.

## Required data

- OHLCV bars for the traded instrument.
- ATR inputs derived from OHLC.
- Chart-timeframe volume for the accumulation profile.
- Higher-timeframe OHLC when the optional HTF EMA filter is enabled.
- Correct bar-close timestamps and higher-timeframe completion state.
- New York clock/calendar only if the optional end-of-day flatten rule is retained.

Point-in-time requirement: HTF filtering must use the previous completed HTF bar. The source explicitly states lookahead is off. Profile levels used after breakout must be frozen at breakout rather than recomputed with future bars.

The profile is an approximation: the source allocates chart-bar volume across price rows rather than using tick-level volume-at-price. Instruments without volume reportedly fall back to time-at-price; that fallback should not be assumed equivalent to actual volume in research.

## Execution assumptions

The source states that state transitions, entry and time-based exits are evaluated on confirmed bars. TP and SL are checked against bar high/low.

Material execution details remain **underspecified**, including:

- whether a confirmed-close entry is filled at that close or next executable price;
- market versus limit order behavior;
- intrabar ordering when TP and SL are both touched;
- spread and slippage;
- commissions/fees;
- market impact and capacity;
- partial fills and order failures;
- crypto perpetual funding and leverage/margin treatment.

These must be specified before any credible backtest.

## Evidence

### Source-reported

The reviewed page describes the mechanical state machine and labels it non-repainting: confirmed bars are used for transitions, prior completed HTF values are requested with lookahead off, and completed profile levels are not redrawn. The author explicitly says the defaults are not optimized or intended to imply a particular outcome.

No source-reported Sharpe, CAGR, drawdown, win rate, or other performance statistic is relied upon in this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself identifies an important measurement limitation: the profile uses chart-timeframe bar volume rather than tick-level volume-at-price and distributes bar volume across traversed price rows. That approximation can materially alter POC/VAH/VAL location.

No independent negative empirical study was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

A future test should compare the full state machine against simpler controls using identical universe, timing and costs:

1. unconditional range breakout;
2. compression + breakout without volume-profile pullback;
3. breakout + generic midpoint/retest instead of POC;
4. full frozen-POC pullback/reclaim rule;
5. full rule with and without the HTF EMA filter.

Test liquid crypto spot and perpetual markets separately across multiple volatility/trend regimes and multiple bar sizes. Freeze all event levels point-in-time and execute no earlier than the information-available timestamp.

The hypothesis is materially weakened if the POC pullback/reclaim stage fails to improve out-of-sample risk-adjusted return, adverse excursion, false-breakout rate, or cost-adjusted expectancy relative to simpler breakout/retest controls; if results disappear when realistic fees/slippage/funding are applied; or if performance is unstable to reasonable profile-row, value-area and compression parameters.

Ablate the volume-profile approximation itself by comparing available higher-resolution volume-at-price construction with the source-style bar-volume allocation. Failure should lead to rejection or reformulation, not parameter mining.

## Crypto portability

`adapted`

The public page mentions Alpaca stocks/crypto connectivity but does not provide crypto-specific empirical validation. This record therefore treats crypto use as a ported hypothesis rather than crypto evidence.

Crypto-specific risks include 24/7 session boundaries, venue fragmentation, differing exchange volume, spot-versus-perpetual microstructure, perpetual funding, mark/index versus trade price, and the arbitrary nature of New-York end-of-day flattening for continuously traded markets. For crypto research, session-flatten logic should be separately ablated rather than assumed necessary.

## Limitations

- Not independently reproduced.
- Exact default numeric parameters are underspecified in the reviewed description.
- Fill timing and transaction-cost model are underspecified.
- Volume-at-price is approximated from chart-bar volume rather than true tick-level price-volume allocation.
- Crypto portability is adapted and empirically unproven.
- Publication page exposed relative age rather than an exact publication timestamp at review time.
- The multi-stage rule has enough degrees of freedom to create overfitting risk; component ablations are required.

## Implementation status

No implementation in our research stack has been completed. No PyBroker, Nautilus, paper, testnet or live verification is claimed.

## Adoption boundary

Research material only. Presence in this repository does not imply profitability, validated alpha, implementation approval, paper/testnet approval, or live-trading approval.

## Related Wiki records

None linked; no stable related Hermes Wiki Brain page was verified from the permitted GitHub-only workflow.

## Sources

- CodaPro, **Volume Profile Breakout Continuation**, TradingView public open-source script/research page, reviewed 2026-09-17: https://www.tradingview.com/script/JoK0u4ld-Volume-Profile-Breakout-Continuation/
