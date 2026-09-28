---
schema: strategy-research-record-v1
title: TradingView ADX + Volume Trend Confirmation
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-29
sources:
  - https://www.tradingview.com/script/whPK8Qlh-ADX-Volume-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView ADX + Volume Trend Confirmation

## Provenance

Public TradingView open-source strategy **ADX + Volume Strategy**, published by **Alex2542** on 2024-09-30. Stable source: https://www.tradingview.com/script/whPK8Qlh-ADX-Volume-Strategy/ . Source reviewed as of 2026-09-29. TradingView canonical script identity: `whPK8Qlh`.

The record normalizes the public strategy description rather than redistributing Pine source.

## Economic mechanism

### Source-reported

The author describes ADX as a trend-strength filter, DI+/DI- as directional confirmation, and abnormal volume as confirmation that market participation supports the move. The stated rationale is to avoid weaker or range-bound signals and participate only when directional trend strength and volume expansion agree.

### Research interpretation

This is a trend-persistence hypothesis with a participation filter. Component roles are:

- Regime/strength: ADX above a threshold.
- Direction: DI+ versus DI-.
- Confirmation: current volume unusually high relative to its recent average.
- Risk/exit: materially underspecified in the public description.

The falsifiable thesis is that directional DMI signals conditioned jointly on high ADX and abnormal volume have better forward risk-adjusted returns than directional DMI alone, after realistic costs. The volume condition may be a useful participation proxy, or may merely select volatile bars after the move has already occurred.

## Signal

Source-reported parameters and entry logic:

- ADX threshold: default 25.
- Volume baseline: 20-period moving average of volume.
- Volume multiplier: default 1.5.
- Long: ADX > 25, DI+ > DI-, and current volume > 1.5 times the 20-period average volume.
- Short: ADX > 25, DI- > DI+, and current volume > 1.5 times the 20-period average volume.
- The author states that ADX and volume parameters are adjustable.

Material gaps:

- ADX/DMI calculation length and smoothing semantics are not specified in the reviewed description.
- Signal-to-order timing is not specified.
- Exit, holding period, re-entry, reversal, pyramiding, and position-sizing semantics are not specified.
- The description does not establish whether the 20-period volume average includes the current bar.

No missing operational rule is silently supplied here.

## Required data

At minimum, OHLCV bars sufficient to calculate DMI/ADX and the 20-period volume average are required.

Instrument/universe, venue, market type, timeframe, timezone/candle boundary, missing-volume handling, and point-in-time venue-volume semantics are data gaps in the reviewed source description.

For crypto testing, venue-specific volume should be treated as venue-local participation rather than market-wide volume unless a separate aggregated-volume dataset is explicitly introduced.

## Execution assumptions

The source description does not specify order type, fill timing, spread, slippage, fees, impact/capacity, funding, leverage/margin, borrow/shorting, latency, partial fills, or failures.

These are data gaps, not zero-cost assumptions. Any later implementation choice for these fields is **research-proposed** unless recovered from the primary source.

## Evidence

### Source-reported

The source explains the intended mechanism, example conditions, strengths, weaknesses, and adjustable parameters. It states that range-bound markets, ADX lag, and low-volume markets can weaken the approach.

No traceable Sharpe, CAGR, maximum drawdown, profit factor, win rate, or other empirical performance statistic was identified in the reviewed source description, so none is recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself identifies three weaknesses: reduced effectiveness in range-bound markets, ADX lag that can cause late entries, and reduced opportunity frequency in low-volume markets. No independent negative study was reviewed in this Scout cycle; absence is not evidence of no negative result.

## Falsification plan

Use completed-bar, point-in-time OHLCV and freeze the source-reported default thresholds before evaluation.

1. Compare the full rule with directional DMI alone.
2. Ablate the ADX gate and volume gate separately to test incremental contribution.
3. Compare the 1.5x abnormal-volume filter with a frequency-matched random gate.
4. Test threshold stability around ADX 25 and volume multiplier 1.5 without selecting the best test-set combination.
5. Evaluate across trend, range, high-volatility, and low-volatility regimes.
6. Use chronological out-of-sample evaluation and report trade count, turnover, drawdown, risk-adjusted return, and cost sensitivity.
7. Apply realistic venue-specific fees, spread/slippage and, for perpetuals, funding.
8. **Research-defined falsification threshold:** reject the normalized hypothesis if the full rule fails to improve out-of-sample risk-adjusted performance over directional DMI alone after costs, or if the apparent benefit disappears when the volume gate is replaced by a frequency-matched control.
9. Because exit logic is source-underspecified, do not interpret any result as a reproduction of the original strategy until exit semantics are resolved. A standardized exit used only to isolate entry predictiveness must be labeled **research-proposed**.

## Crypto portability

**adapted**

The OHLCV/DMI/ADX/volume mechanism is mechanically portable to crypto, but the reviewed source does not provide crypto-specific empirical evidence sufficient to treat portability as validated. Crypto-specific risks include fragmented venue volume, 24/7 candle boundaries, spot versus perpetual differences, funding, leverage/liquidation, and materially different liquidity across venues and symbols.

Any choice of crypto universe, venue, market type, timeframe, session boundary, or aggregated-volume construction is **research-proposed** unless separately source-backed.

## Limitations

- Exit and holding lifecycle: **underspecified**.
- ADX/DMI length and smoothing: **underspecified**.
- Exact volume-average inclusion semantics: **underspecified**.
- Universe, venue, market type, timeframe and timezone: **data gap**.
- Execution and cost model: **data gap**.
- Crypto profitability: **unproven**.
- Not independently reproduced.

## Implementation status

Research normalization only. No implementation in the research stack and no Qlib full backtest were performed by this Scout.

`implementation_status: not-implemented`.

## Adoption boundary

This artifact is **research-only**, **not-implemented**, and **not-approved**. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor/leaderboard entry, demonstrated profitable alpha, or received Paper, Testnet, or Live approval.

## Related Wiki records

No stable related Hermes Wiki record was resolved in this GitHub-only run; no Wiki link is fabricated.

## Sources

- Alex2542, **ADX + Volume Strategy**, TradingView, published 2024-09-30: https://www.tradingview.com/script/whPK8Qlh-ADX-Volume-Strategy/ (reviewed 2026-09-29).
