---
schema: strategy-research-record-v1
title: TradingView Monday VWAP weekly swing
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
  - https://www.tradingview.com/script/rAwb2sPd-Swing-VWAP-Crypto-and-Stocks-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Monday VWAP weekly swing

## Provenance

Public TradingView open-source strategy page, **Swing VWAP Crypto and Stocks Strategy**, author/page identity `exlux`, published 2021-11-15. Stable source: https://www.tradingview.com/script/rAwb2sPd-Swing-VWAP-Crypto-and-Stocks-Strategy/ . Source reviewed as of 2026-09-19.

## Economic mechanism
### Source-reported

The author presents the rule as a swing strategy for crypto and stocks combining VWAP, time management, and risk management. Entry is restricted to Monday when the candle close crosses above VWAP; exit is always on Sunday unless take-profit or stop-loss is reached first.

### Research interpretation

The falsifiable hypothesis is that a bullish Monday close-through-VWAP event identifies favorable weekly directional pressure that persists into the remainder of the week. The calendar restriction may isolate a weekly liquidity/positioning reset, while VWAP acts as the price-location trigger. This mechanism is a research interpretation; the source does not establish that Monday itself contributes independent alpha.

## Signal

- Formation timing: Monday candle close.
- Primary long entry: on Monday, candle close crosses above VWAP.
- Short entry: not specified by the reviewed source description.
- Scheduled exit: Sunday.
- Other exits: take-profit or stop-loss may exit earlier.
- Holding horizon: intrawweek, from qualifying Monday entry until Sunday at the latest, subject to TP/SL.
- Re-entry: underspecified.
- VWAP anchoring/reset convention: underspecified.
- Chart timeframe: underspecified.
- TP/SL values and calculation basis: underspecified.
- Position sizing: underspecified.

The source description is therefore partially reconstructable but not fully specified.

## Required data

- Instrument/universe: source states crypto and stocks; no fixed crypto universe is specified.
- Market type/venue: underspecified.
- OHLCV sufficient to construct the stated candle-close/VWAP condition, subject to resolving the exact VWAP convention.
- Calendar/day-of-week labels.
- Timestamp/timezone and weekly boundary convention are material because crypto trades 24/7 and the Monday/Sunday rule depends on them.
- Point-in-time calculation must use only information available at the qualifying candle close.

## Execution assumptions

The source states the signal condition using candle close but does not specify whether execution occurs at that same close or the next tradable price. Order type, fill model, fees, spread, slippage, impact/capacity, leverage, margin, shorting, latency and partial-fill handling are not specified. TP/SL mechanics are also underspecified.

For later testing, same-bar execution must not be assumed unless reconstructable from the source; a leakage-safe next-bar implementation should be tested separately and labeled as research-proposed if used.

## Evidence
### Source-reported

The reviewed TradingView page describes the rules but does not provide a sufficiently traceable quantitative performance claim that should be preserved here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed source; absence is not evidence of no negative result. The day-of-week restriction creates an obvious data-mining risk, and results may be highly sensitive to timezone/session boundaries and transaction costs.

## Falsification plan

- Reconstruct the exact VWAP/session convention before formal testing; reject any implementation that cannot preserve point-in-time causality.
- Compare the Monday-only trigger against the identical VWAP cross on every other weekday and against an all-days VWAP-cross baseline.
- Test multiple predeclared crypto cohorts and venues rather than selecting only favorable symbols.
- Evaluate UTC and venue-native candle/session boundaries separately; a calendar effect that disappears under reasonable boundary choices is weak evidence.
- Use strict out-of-sample evaluation and transaction-cost sensitivity.
- Ablate the calendar gate and VWAP trigger independently to determine whether either component contributes incremental information.
- Treat TP/SL parameter searches as research-proposed and control the search domain to limit multiple-testing bias.
- Reject or materially weaken the hypothesis if Monday conditioning provides no stable OOS improvement over the all-days baseline after costs.

## Crypto portability

direct

The source explicitly includes crypto. Portability still depends on 24/7 calendar boundaries, VWAP reset semantics, venue fragmentation, spot-versus-perpetual differences, liquidity, fees and, for perpetuals, funding.

## Limitations

- underspecified VWAP anchor/reset convention;
- underspecified timeframe;
- underspecified TP/SL parameters and mechanics;
- underspecified execution timing and market type;
- calendar/timezone sensitivity;
- possible day-of-week data mining;
- not independently reproduced.

## Implementation status

No implementation in the research stack has been completed. This record does not imply Qlib, paper, testnet or live verification.

## Adoption boundary

Research material only. Presence in this repository does not mean profitable, validated alpha, approved implementation, or approval for paper, testnet, or live trading.

## Related Wiki records

No stable related Hermes Wiki Brain record is asserted here.

## Sources

- TradingView, `exlux`, **Swing VWAP Crypto and Stocks Strategy**, published 2021-11-15, reviewed 2026-09-19: https://www.tradingview.com/script/rAwb2sPd-Swing-VWAP-Crypto-and-Stocks-Strategy/
