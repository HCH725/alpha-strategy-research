---
schema: strategy-research-record-v1
title: TradingView ORB with VWAP, volume, and candle-strength confirmation
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2026-09-25
sources:
  - https://www.tradingview.com/script/wLSGHPUe-ORB-Breakout-Strategy-with-VWAP-and-Volume-Filters/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView ORB with VWAP, volume, and candle-strength confirmation

## Provenance

Public TradingView open-source strategy by `luiscaballero`, "ORB Breakout Strategy with VWAP and Volume Filters." Stable source URL: https://www.tradingview.com/script/wLSGHPUe-ORB-Breakout-Strategy-with-VWAP-and-Volume-Filters/ . Source page was directly reviewed on 2026-09-25. The page shows an initial publication date of Jan 4 and an update/release-note date of Jan 23; the year is not printed in the visible source text, so it is not inferred here.

## Economic mechanism

### Source-reported

The source frames classic Opening Range Breakout (ORB) as vulnerable to false breakouts and assigns three independent confirmation roles: session-anchored VWAP plus VWAP slope filters counter-trend breakouts, breakout-bar volume filters low-participation moves, and candle-strength filters breakouts that pierce the range but close weakly. The stated thesis is that requiring trend, participation, and momentum to align should select stronger opening-range breakouts.

### Research interpretation

This is a hybrid intraday momentum hypothesis. The opening range supplies the primary price-discovery boundary; VWAP direction is a regime/trend filter; volume is a participation confirmation; and close location within the breakout bar is a momentum/acceptance confirmation. The falsifiable incremental claim is not that ORB alone works, but that the three filters jointly or individually improve post-breakout continuation enough to overcome their lower trade frequency and transaction costs.

The source itself reports strongly negative long-horizon default results, so the record should be treated primarily as a component-ablation research hypothesis rather than evidence of profitable alpha.

## Signal

Source-reported rules:

- Opening range: first N bars after the session open; default is 3 bars on a 5-minute chart, i.e. 15 minutes.
- Long setup: breakout above the opening-range high, subject to all enabled filters.
- Short setup: breakout below the opening-range low, subject to all enabled filters.
- VWAP filter: long requires price above session-anchored VWAP with positive slope; short is the inverse. Slope lookback and minimum slope are configurable.
- Volume filter: breakout/setup bar must meet a configurable minimum absolute volume.
- Candle-strength filter: close must be sufficiently near the directional end of the bar. The source gives 0.7 as an example/default interpretation: top 30% for longs, with the symmetric condition for shorts.
- Updated execution description: filters are evaluated on the bar before breakout; when they pass, a stop order is placed at the ORB level, and touching that level executes the entry rather than waiting for a breakout-bar close.
- Pyramiding is disabled and maximum trades per day is configurable.
- Exit/risk modes: fixed-point TP/SL, or breakout-candle stop (low for long, high for short) with take profit as a configurable reward/risk multiple. An optional breakeven rule moves the stop to entry after a configurable fraction of the target is reached.
- All positions are closed at the end of the trading session.

The source page contains an older overview that describes entry as a bar closing beyond the ORB boundary, while the Jan 23 release notes describe stop-order entry at the ORB level after prior-bar filters pass. For research implementation, the later release-note semantics should be treated as the current source-reported rule; the older close-based wording is retained here as a provenance ambiguity rather than silently reconciled.

No additional thresholds are invented. Values for VWAP slope, absolute minimum volume, fixed TP/SL points, reward/risk ratio, breakeven trigger, trading-session hours, and max trades/day are configurable and not fully fixed by the reviewed text.

## Required data

Source-reported / directly implied:

- Intraday OHLCV.
- Session-open and session-close boundaries.
- Session timezone.
- Session-anchored VWAP.
- Sufficient bar history for configurable VWAP-slope lookback.
- Opening-range high and low from the first N bars.
- Volume on the filter/setup bar.
- Tick size for the source's slippage assumption.

The reported backtest is on NQ futures. The source also suggests ES, NQ, MNQ, or other futures for experimentation.

Point-in-time implementation must ensure that opening-range levels are frozen only after the range-formation window completes and that filter values use only information available before the stop order is armed.

## Execution assumptions

Source-reported strategy properties:

- Initial capital: USD 50,000.
- Position size: fixed 1 contract.
- Commission: USD 4 per contract.
- Slippage: 2 ticks.
- Margin: 1%.
- Pyramiding: disabled.
- Updated entry mechanism: stop order at the ORB level after prior-bar filters pass.
- End-of-session flattening.

Spread, market impact, capacity, queue priority, partial fills, rejected orders, and latency are not specified. The source's fixed commission and slippage assumptions must not be treated as universal across instruments or venues.

## Evidence

### Source-reported

For NQ with the source's stated default framework, the page reports:

- Jan 2025 to Jan 2026: 243 trades, 39.09% win rate, profit factor 1.03, net P&L USD 3,581 (+7.16%), and max drawdown USD 25,447 (39.96%).
- 2010 to 2026: 1,699 trades, 37.61% win rate, profit factor 0.756, net P&L -USD 49,632 (-99.26%), and max drawdown USD 50,262 (99.27%).

These are third-party TradingView source-reported results only. The source explicitly states that long-term default results have negative expectancy and presents the script as a research framework rather than a ready-to-trade system.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source's own long-term default backtest is strongly negative, with reported profit factor below 1 and near-total loss of initial capital. The author also explicitly flags parameter sensitivity, regime dependence, transaction-cost impact, and curve-fitting risk. The short recent interval is positive but weak (reported profit factor 1.03) and does not overturn the adverse long-run result.

## Falsification plan

Research-defined falsification thresholds / research-proposed tests:

1. Reproduce the current release-note semantics point-in-time before evaluating alpha.
2. Compare naked ORB against ORB+VWAP, ORB+volume, ORB+candle-strength, every two-filter combination, and all three filters. Reject the "three confirmations add value" thesis if the full model does not improve out-of-sample risk-adjusted net performance versus naked ORB and simpler subsets.
3. Use rolling or anchored out-of-sample windows across multiple years and market regimes; do not optimize and score on the same sample.
4. Stress commissions and slippage above the source's USD 4 / 2-tick assumptions. Reject if modest cost increases erase any out-of-sample advantage.
5. Test several opening-range lengths and session definitions without selecting a single ex-post winner.
6. Measure trade-count reduction and opportunity cost caused by each filter.
7. Test NQ separately from ES/MNQ and any crypto adaptation; do not pool evidence across market structures.
8. Treat the source-reported 2010-2026 negative expectancy as the baseline adverse result that any revised configuration must overcome out of sample.

## Crypto portability

adapted

The mechanism can be adapted to crypto, but the source evidence is from NQ futures and is not crypto evidence. Crypto lacks a single universal cash-session open, so an opening-range anchor must be explicitly defined (for example UTC day boundary or a venue/liquidity session); that choice is research-proposed and must be tested rather than assumed.

For perpetuals, additional requirements include venue-specific volume, 24/7 candle boundaries, funding, mark/index-price conventions, liquidation/margin effects, and fragmented liquidity. Session-anchored VWAP and absolute-volume thresholds are especially venue- and session-definition-sensitive.

## Limitations

- Source-reported long-term default expectancy is negative.
- Entry wording differs between the older overview (close beyond ORB) and later release notes (pre-breakout filters plus stop entry at ORB).
- Several filter thresholds and session settings are configurable rather than uniquely specified.
- No independent reproduction.
- No statistical significance, confidence intervals, turnover/capacity analysis, or out-of-sample protocol is reported on the reviewed page.
- Recent positive results are much shorter than the adverse 2010-2026 sample.
- Crypto portability is unproven.

## Implementation status

Not implemented in the research stack. No Qlib full backtest or independent validation has been performed.

## Adoption boundary

Research-only. Presence in this repository does not mean the strategy passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor/leaderboard entry, is profitable, or is approved for Paper, Testnet, or Live trading.

## Related Wiki records

No stable Hermes Wiki Brain record was resolved in this GitHub-only run; no Wiki link is fabricated.

## Sources

- TradingView, luiscaballero, "ORB Breakout Strategy with VWAP and Volume Filters": https://www.tradingview.com/script/wLSGHPUe-ORB-Breakout-Strategy-with-VWAP-and-Volume-Filters/ (directly reviewed 2026-09-25).
