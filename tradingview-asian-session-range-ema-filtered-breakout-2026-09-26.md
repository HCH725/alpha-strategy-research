---
schema: strategy-research-record-v1
title: Asian Session Range Breakout with Daily EMA and Box-Width Filters
created: 2026-09-26
updated: 2026-09-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-26
sources:
  - https://www.tradingview.com/script/igxoVSvV-Asian-Box-Breakout-EDA-Tuned/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Asian Session Range Breakout with Daily EMA and Box-Width Filters

## Provenance

Public TradingView open-source strategy page, **Asian Box Breakout - EDA Tuned**, by **waranyutrkm**, published May 25 (TradingView page as read 2026-09-26). Stable source: https://www.tradingview.com/script/igxoVSvV-Asian-Box-Breakout-EDA-Tuned/

The public page states that the strategy is intended for indices and crypto, including US100 and BTC. This record normalizes only claims visible on that primary-source page; it does not reproduce or redistribute the Pine source.

## Economic mechanism

### Source-reported

The author describes an Asian-session high/low breakout strategy intended to reduce low-quality false breakouts through a daily EMA trend filter and a minimum box-width filter. Daily ATR is used for stop sizing, while position sizing is risk based.

### Research interpretation

The falsifiable alpha hypothesis is that the Asian-session range concentrates a time-bounded reference range and that subsequent breaks contain continuation information when aligned with the daily trend and when the range is not abnormally narrow. The daily EMA is a regime filter; the minimum box width is a range-quality filter. ATR stop sizing, risk-based position sizing, trailing stops, and end-of-day closing are risk/execution components and should not be assumed to create alpha.

Ablation is required to distinguish the contribution of the session breakout itself from the EMA and minimum-width filters.

## Signal

Source-reported components:

- Formation: build the high and low of an Asian-session range.
- Entry: trade breakouts of the Asian-session high/low.
- Regime filter: daily EMA trend filter.
- Range-quality filter: minimum box width.
- Direction modes: long only, short only, or both.
- Risk: daily ATR-based stop-loss sizing.
- Position sizing: percentage-of-equity risk based.
- Exit/risk management: trailing stop activated after an R-multiple move; optional end-of-day close.

The primary-source page does **not** state the exact Asian-session start/end timestamps or timezone, EMA length/direction test, minimum-width formula or threshold, ATR length/multiple, exact breakout confirmation rule, order type, R-multiple trigger, trailing-stop formula, end-of-day timestamp, re-entry rule, or default direction mode. These fields are **underspecified** and are not inferred here.

No Scout-chosen operationalization is introduced in this record. Any future concrete values for those gaps must be explicitly labeled `research-proposed`.

## Required data

Source-supported minimum:

- OHLC price data sufficient to construct the Asian-session high/low.
- Daily data or a causally available daily EMA value for the trend filter.
- Daily OHLC-derived true range/ATR inputs for stop sizing.
- Intraday timestamps sufficient to identify the Asian session and any end-of-day exit.
- Instrument support includes the author's stated examples US100 and BTC.

Data gaps:

- Exact venue and BTC market type (spot, perpetual, futures) are not stated.
- Exact intraday timeframe is not stated.
- Session timezone and candle-boundary convention are not stated.
- Point-in-time handling of the daily EMA/ATR while an intraday session is active is not stated.

A leakage-safe implementation must use only daily information available at the signal timestamp; the source page does not specify that convention.

## Execution assumptions

The source page does not specify signal-to-order timing, same-bar versus next-bar fills, market versus stop orders, fill model, commissions, spread, slippage, impact/capacity, funding, leverage/margin, borrow/short constraints, latency, partial fills, or failure handling. These are **data gaps**, not zero-cost assumptions.

The source reports risk-based sizing, ATR stop sizing, an R-multiple-activated trailing stop, and an optional end-of-day close, but their exact formulas/timing are underspecified.

## Evidence

### Source-reported

The source says the strategy is designed for indices and crypto such as US100 and BTC and that performance depends heavily on market regime, timeframe, and parameter settings. It does not provide traceable Sharpe, CAGR, drawdown, win rate, trade count, or other numerical performance statistics on the reviewed page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself warns that backtest performance depends heavily on regime, timeframe, and parameter settings. No independent negative study was identified in the reviewed primary source; absence is not evidence of no negative result.

## Falsification plan

All thresholds below are **research-defined falsification thresholds**, not source claims.

1. Reconstruct the source-supported rule only after the missing session, EMA, box-width, ATR, trailing-stop, and timing semantics are fixed and documented without look-ahead.
2. Compare raw Asian-session breakout against +daily-EMA, +minimum-box-width, and combined variants; reject the claim that the filters add value if their out-of-sample net risk-adjusted performance does not improve on the raw breakout.
3. Use chronological out-of-sample testing across multiple BTC volatility regimes and at least one distinct crypto instrument.
4. Run realistic fee/spread/slippage sensitivity; reject practical viability if the net edge is non-positive under a defensible liquid-venue cost model.
5. Test nearby session boundaries and parameter neighborhoods; materially discontinuous performance around a single setting weakens the hypothesis.
6. Verify all daily filters are causally available at each intraday decision point.
7. Separate long and short results; a result driven by only one side should be reported as such rather than generalized.

## Crypto portability

**direct**, but narrowly: the source explicitly states that the strategy is designed for crypto markets such as BTC. That is source scope, not evidence of profitability.

Portability risks include crypto's 24/7 session structure, the arbitrary nature of an "Asian session" boundary across venues, spot-versus-perpetual differences, funding, venue fragmentation, mark/index pricing, and timezone/candle-boundary choices. The source does not resolve these issues.

## Limitations

- Exact session definition: **underspecified**.
- Exact EMA rule and length: **underspecified**.
- Exact minimum box-width rule: **underspecified**.
- ATR and trailing-stop parameters/formulas: **underspecified**.
- Entry confirmation and fill timing: **underspecified**.
- Venue, market type, timeframe, costs, and funding: **data gap**.
- Claimed "EDA Tuned" process, tuning sample, and anti-overfitting procedure are not described on the reviewed page: **data gap**.
- **Not independently reproduced.**
- No source-reported numerical performance evidence was used.

## Implementation status

Research normalization only. No implementation in the research stack and no Qlib full backtest have been completed.

## Adoption boundary

This record is research-only, not implemented, and not approved. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, proved profitable, or received Paper, Testnet, or Live approval.

## Related Wiki records

No stable related Hermes Wiki Brain record is asserted here.

## Sources

- TradingView, waranyutrkm, **Asian Box Breakout - EDA Tuned**: https://www.tradingview.com/script/igxoVSvV-Asian-Box-Breakout-EDA-Tuned/ — public open-source strategy page, read 2026-09-26.
