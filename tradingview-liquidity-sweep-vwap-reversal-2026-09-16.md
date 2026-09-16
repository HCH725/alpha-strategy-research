---
schema: strategy-research-record-v1
title: "TradingView Previous-Day Liquidity Sweep + VWAP Reversal"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - liquidity-sweep
  - vwap
status: research-only
confidence: medium
source_as_of: 2026-09-16
sources:
  - https://www.tradingview.com/script/raeV41qI/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Previous-Day Liquidity Sweep + VWAP Reversal

## Provenance

Public TradingView open-source strategy `_mr_beach Liquidity Sweep + VWAP Reversal` by ReneHerkert, published 2026-01-25. Stable source URL: https://www.tradingview.com/script/raeV41qI/ . Source reviewed 2026-09-16.

## Economic mechanism

### Source-reported

The source models a reversal after price takes liquidity beyond the previous day's high or low, then returns inside that prior-day boundary and crosses back to the appropriate side of VWAP. A long-term EMA is used as a directional filter. The author frames VWAP as a fair-value reference and the previous-day extremes as liquidity levels.

### Research interpretation

The falsifiable hypothesis is that failed excursions beyond prior-day extremes contain short-horizon reversal information when price subsequently reclaims both the swept level and intraday VWAP, conditional on the prevailing EMA trend. Component roles are distinct: previous-day high/low defines the potential liquidity event; reclaim supplies failure-of-breakout confirmation; VWAP requires return through an intraday volume-weighted reference; EMA filters direction. Whether any component adds incremental alpha must be tested by ablation rather than assumed.

## Signal

Source-reported core rules:

- Reference levels: previous day's high (PDH) and previous day's low (PDL).
- Trend filter: EMA, default length 200.
- Bullish sweep candidate: current low trades below PDL.
- Bearish sweep candidate: current high trades above PDH.
- Long confirmation: after a sweep below PDL, price closes back above PDL and above VWAP, with the close above the EMA trend filter.
- Short confirmation: after a sweep above PDH, price closes back below PDH and below VWAP, with the close below the EMA trend filter.
- The source describes a session filter and one-trade-per-day constraint.
- Risk management is ATR-based.

Underspecified from the reviewed public description: exact session default, ATR period/multiplier, precise stop/target formula, whether the sweep and reclaim must occur on the same bar, order type/fill timing, and any expiry rule between sweep and confirmation. These must not be silently inferred.

## Required data

- Instrument/universe: source does not restrict the core logic to a single instrument; portability is unproven.
- Market type: not fixed by the source description.
- Intraday OHLCV sufficient to compute VWAP and EMA.
- Prior completed daily high/low, available point-in-time before the current session.
- Session/calendar definition consistent with the venue used to form PDH/PDL and VWAP.
- ATR requires OHLC history.
- For perpetual crypto testing, funding/mark/index data would be needed only for realistic accounting, not signal formation.

Point-in-time requirement: PDH/PDL must come only from the completed prior daily session; current-day information must not leak into those levels.

## Execution assumptions

The public description does not establish exact signal-to-order timing or fill semantics. A later test must predeclare whether a confirmed bar-close signal executes at that close or the next tradable price. Fees, spread, slippage, market impact, leverage, margin, funding, partial fills, and latency are not specified by the source and must be modeled explicitly during validation rather than treated as zero by implication.

## Evidence

### Source-reported

The TradingView page describes the rule set and presents it as a Strategy Tester implementation. No source-reported Sharpe, CAGR, drawdown, win rate, or other performance statistic is used in this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The reviewed source does not establish that a liquidity sweep is itself predictive, nor that VWAP or EMA confirmation contributes incremental alpha. The mechanism is vulnerable to genuine breakout days, ambiguous session boundaries, repeated sweeps, and execution costs. No independent negative-result study was identified in this Scout cycle; absence is not evidence of no negative result.

## Falsification plan

Research-proposed tests:

1. Compare the full rule against a prior-day-level failed-breakout baseline without VWAP or EMA confirmation.
2. Ablate VWAP and EMA separately to measure incremental contribution.
3. Test genuine trend/breakout regimes versus range/reversal regimes.
4. Use point-in-time prior-day levels and fixed venue-specific session boundaries.
5. Evaluate bar-close versus next-bar execution and realistic fee/slippage sensitivity.
6. For crypto, test multiple UTC/session definitions because 24/7 markets lack a natural exchange close.
7. Require out-of-sample persistence across assets and regimes; reject the hypothesis if the full confirmation stack does not improve risk-adjusted or tail-aware results over the simpler failed-breakout baseline after costs. The exact quantitative rejection threshold is research-proposed and must be predeclared before formal testing.

## Crypto portability

unproven

The mechanism can be translated to liquid crypto spot or perpetual markets using a chosen daily boundary, but that is a ported research hypothesis rather than source-demonstrated crypto evidence. The largest portability risk is session definition: PDH/PDL and VWAP reset semantics can materially change when a 24/7 venue is partitioned at UTC, exchange-local, or another boundary. Perpetual tests also require funding and mark/index accounting downstream.

## Limitations

- Not independently reproduced.
- Exact session configuration is underspecified in the reviewed public description.
- ATR exit parameters and exact execution semantics are underspecified.
- The causal interpretation of stop-taking/liquidity sweeps is unproven; the observable rule is a failed excursion and reclaim around prior-day extremes.
- VWAP and EMA may add delay without incremental predictive value; ablation is required.
- 24/7 crypto session boundaries create a material data-definition dependency.

## Implementation status

No implementation in the user's research/backtest stack has been completed. This record normalizes external research only.

## Adoption boundary

Research material only. Presence in this repository does not mean profitable, validated alpha, approved for implementation, or approved for Paper/Testnet/Live trading.

## Related Wiki records

No stable Hermes Wiki record is asserted from this GitHub-only Scout cycle.

## Sources

- ReneHerkert, `_mr_beach Liquidity Sweep + VWAP Reversal`, TradingView, published 2026-01-25: https://www.tradingview.com/script/raeV41qI/
