---
schema: strategy-research-record-v1
title: Crypto Intraday Seasonality with Open-Interest and Volatility Regimes
created: 2026-09-21
updated: 2026-09-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-21
sources:
  - https://www.tradingview.com/script/SQSYcyfK/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Intraday Seasonality with Open-Interest and Volatility Regimes

## Provenance

- Public TradingView open-source script: **Session Heatmap** by `ketan_kee`.
- Stable source URL: https://www.tradingview.com/script/SQSYcyfK/
- TradingView page shows publication/update date **2025-12-15**; reviewed as of **2026-09-21**.
- The source describes an intraday-seasonality heatmap for true range, volume, and open-interest changes, grouped by weekday or month, with 30-minute or 1-hour slots and optional percentile scaling.
- The source states that open-interest metrics require Binance perpetual symbols and that daylight-saving time is not automatically adjusted.

## Economic mechanism

### Source-reported

The source presents recurring time-of-day patterns in volatility, volume, and open-interest changes as a way to identify periods when market activity tends to be relatively high or low. It distinguishes OI increases, OI decreases, and net OI change, and permits weekday/month grouping.

### Research interpretation

**Research-proposed hypothesis:** crypto derivatives activity is not temporally homogeneous even though trading is 24/7. Recurrent clock-time/weekday participation patterns may reflect overlapping regional trading hours, derivatives funding/position-management routines, macro-market openings, and liquidity-provider inventory cycles. Conditional deviations from a point-in-time seasonal baseline may therefore contain information about subsequent volatility or directional continuation/reversal.

The economically relevant test is not whether a heatmap looks seasonal. It is whether **time-slot-conditioned OI and volatility surprises** add predictive information beyond unconditional time-of-day, realized-volatility, volume, and price-trend controls.

Two competing hypotheses should be tested rather than assumed:

1. **Participation-confirmed continuation (research-proposed):** unusually large positive OI change and elevated true range relative to the same historical clock slot may identify fresh leveraged positioning and increase short-horizon continuation probability.
2. **Crowding/exhaustion reversal (research-proposed):** extreme OI expansion during historically active slots may instead identify crowded positioning that is vulnerable to reversal or liquidation after the activity burst.

## Signal

### Source-supported construction

- Partition observations into clock-time slots; the source offers **30-minute / 1-hour** slot sizes.
- Metric choices include true range (TR), volume, OI increase, OI decrease, and OI net change.
- Group historical observations by weekday or month.
- The source offers percentile-mode visualization using the 5th-95th percentile range to reduce outlier impact.
- Chart timeframe should be equal to or smaller than the selected slot size.

### Research-proposed operationalization

No source trading rule is claimed. For falsifiable research only:

1. At each completed bar, assign the observation to a UTC clock slot and weekday.
2. Using only observations available before that bar, estimate the trailing distribution for the same slot/weekday of TR, volume, and OI change.
3. Convert current values to expanding/rolling percentile ranks or robust standardized surprises.
4. Test subsequent returns and realized volatility conditional on OI-surprise sign/magnitude and TR surprise.
5. Separately test continuation and reversal branches; do not select direction ex post.

Signal formation must occur only after the current bar closes. Lookback length, minimum history, threshold, holding horizon, entry/exit, re-entry, and sizing are **underspecified by the source** and any tested choices are `research-proposed`.

## Required data

- **Primary market:** crypto perpetual futures; source specifically requires Binance perpetual symbols for OI metrics.
- Point-in-time OHLCV with true-range inputs.
- Point-in-time open-interest observations aligned to each bar.
- Exchange/contract identity and contract-history metadata.
- UTC timestamps plus explicit exchange/chart timezone mapping.
- Calendar fields for weekday and month.
- For portability tests: equivalent OI series from other perpetual venues where historically available.
- Missing OI observations must remain missing; they must not be forward-filled across outages or contract changes without an explicit test.
- Historical data availability must reflect what was observable at each signal timestamp.

## Execution assumptions

The source is an analytical indicator, not a fully specified execution strategy. It does not define order type, entry price, exit, holding period, fees, spread, slippage, market impact, leverage, margin, funding treatment, or partial-fill behavior.

For later research, all signal decisions should be formed on completed bars and executed no earlier than the next executable observation unless a stricter event-time simulation is available. All execution choices are `research-proposed`.

## Evidence

### Source-reported

The source reports that the tool analyzes historical time-of-day patterns in TR, volume, and OI changes and supports weekday/month grouping. It does **not** report a verified trading return, Sharpe ratio, CAGR, drawdown, win rate, or causal alpha estimate.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source explicitly notes that DST is not automatically adjusted, which can shift London/New York session relationships relative to UTC.
- The source states that OI metrics require Binance perpetual symbols, creating venue-specific portability risk.
- A visually stable seasonal heatmap does not establish return predictability or tradable alpha.
- No source-reported cost-adjusted backtest was identified.

## Falsification plan

1. **Strict point-in-time baseline:** construct each seasonal expectation from prior observations only; never use a full-sample heatmap to score earlier history.
2. **Ablation:** compare `clock slot only` → `+ weekday` → `+ volume` → `+ TR` → `+ OI change`. Reject added layers that do not improve leakage-safe OOS results.
3. **Controls:** compare against unconditional momentum/reversal, realized volatility, raw OI change, raw volume, and simple UTC-hour/day-of-week dummies.
4. **Same-slot placebo:** randomly permute historical slot labels within comparable volatility regimes. A genuine seasonality-conditioned effect should materially weaken.
5. **Timestamp placebo:** shift OI observations forward/backward by one slot to detect alignment artifacts.
6. **DST robustness:** test pure UTC slots separately from research-proposed region/session mappings with historical DST calendars. Do not infer DST-adjusted sessions from the source.
7. **Venue robustness:** test Binance-only first, then independently test other venues where point-in-time OI exists; do not assume cross-venue equivalence.
8. **Regime robustness:** evaluate bull/bear, high/low volatility, weekday/weekend, and major market-stress periods separately.
9. **Competing direction:** predeclare continuation and reversal branches. Reject the directional thesis if neither survives OOS after multiple-testing control and costs.
10. **Failure action:** if OI/TR seasonal surprises add no stable OOS information beyond simple clock-time and volatility controls, reject the composite and retain no extra complexity.

## Crypto portability

**direct** for the source's Binance-perpetual OI use case; **unproven** for other venues.

Crypto-specific risks include 24/7 trading, exchange-specific OI definitions, venue fragmentation, contract migrations, funding intervals, changing regional participation, DST shifts in external markets, and candle-boundary differences. These can create apparent seasonality without a stable economic premium.

## Limitations

- Trading rule: **underspecified**.
- Historical lookback/minimum sample: **underspecified**.
- Entry, exit, holding period, re-entry, sizing: **underspecified**.
- OI field construction and historical revision policy: **data gap** from the public description.
- Cross-venue portability: **unproven**.
- Predictive alpha: **not independently reproduced**.
- Multiple-testing risk is material because many slot × weekday × metric combinations can be inspected.

## Implementation status

Research record only. No implementation in the research stack and no Qlib full backtest has been completed for this record.

## Adoption boundary

This artifact is research material only. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, is profitable, or is approved for Paper, Testnet, or Live trading.

## Related Wiki records

- [[tradingview-same-time-of-day-relative-volume-blowoff-2026-09-20]] — related intraday seasonality concept focused on same-time-of-day relative volume; the present hypothesis is materially distinct because OI-change and volatility seasonality are primary data dependencies.
- [[tradingview-aggregated-oi-volume-delta-liquidation-absorption-2026-09-21]] — related derivatives positioning research using OI shocks and volume delta rather than recurring clock-time baselines.

## Sources

1. TradingView, `ketan_kee`, **Session Heatmap**, public open-source script, updated 2025-12-15, reviewed 2026-09-21: https://www.tradingview.com/script/SQSYcyfK/
