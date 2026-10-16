---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Alorse DMI Winner Three-Bar DI Persistence and EMA55 Filter"
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/momentum/DMI%20Winner.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alorse DMI Winner Three-Bar DI Persistence and EMA55 Filter

## Provenance

- Source repository: https://github.com/Alorse/pinescript-strategies
- Immutable source commit: 8fb3837ddcd137f1450c3e82d654ff3df24d54d5
- Exact source path: strategies/momentum/DMI Winner.pine
- Primary source file: https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/momentum/DMI%20Winner.pine
- The source signal is preserved. Research execution derivatives are clearly disclosed below; no change is silently represented as lossless.

## Economic mechanism

Momentum continuation requires directional movement dominance on three consecutive closed candles, persistent trend intensity and a 55-period moving average regime filter. Unlike a simple DI cross or the existing DMI Swings contrarian record, the code uses three consecutive DI-level comparisons plus ADX and candle color.

## Signal — exact source rules

Pine v5 strategy, pyramiding=0, percent_of_equity default sizing 20%, source commission 0.01% per side. DMI: len=14, ADX smoothing lensig=13, keyLevel=23, [DIplus, DIminus, ADX] = ta.dmi(14,13).

- hasMa=true; maType=EMA; maLen=55; MA=EMA(close,55). Source supports optional SMA or disabled filter, but this record pins default EMA.
- longCond = DIplus > DIminus on current AND previous AND two-bars-back candles.
- shortCond = DIplus < DIminus on current AND previous AND two-bars-back candles.
- longEntry = longCond AND ADX > 23 AND close > MA AND close > open.
- shortEntry = shortCond AND ADX > 23 AND close < MA AND close < open.
- showLong=true and showShort=false: enter Long when longEntry is true, close Long when shortEntry is true; no short orders in default mode.
- Both direction flags enabled: Pine submits corresponding Long/Short entries on their signals, with opposite-direction reversal according to pyramiding=0. Short-only mode is another explicit input variant.
- Source entry/exit blocks are gated by time between startTime=2021-02-01 23:59:59 and endTime=2099-02-01 23:59:59. These are backtest settings, NOT an optimal chart interval.
- useSL=false default; no price stop is submitted. If the user enables useSL, the code submits only a Long stop at avg-entry-price * (1 - 0.10), with no corresponding Short stop. There is no source take-profit, trailing, cooldown or safety-order rule.
- Persistent true predicates can persist across bars, but pyramiding=0 prevents same-side accumulation. The first qualifying long after becoming flat is a possible re-entry.

## Required data and causality

One symbol's completed OHLC. DMI requires high/low/close, EMA requires close, bullish/bearish candle requires open. All indexes are current or previous candles, with no request.security, repaint, lookahead or future extrema. Research-declared conservative warmup: 100 completed bars to stabilize EMA55 and Wilder's DMI/ADX; 100 is not an author-specified indicator length.

## Execution assumptions — disclosed research derivative

Original Pine omits process_orders_on_close, therefore source decisions from closed bars normally enter/close on NEXT bar open. Our proposed HB lane derives same-bar-close fills for the identical closed-bar predicates. This modifies execution timing/prices (NOT indicator logic); it is not claimed as a source-native execution reproduction. Before PASS the independent reviewer must check the actual Hummingbot controller/executor, bar-availability and isolated Binance USDT-M fill/cost path under pinned package 20260920, VERSION dev-2.17.0.

Author's 2021–2099 optional date window must be treated as declared source configuration, not cherry-picked for performance. Downstream 7-pair, 1h/4h/1d and 3x/5x experiments choose their own evaluation windows explicitly. House BO/SO DCA sizing is a separate declared derivative that may alter order events, not part of this original signal record.

## Deduplication

The main pool has DMI Swings contrarian ADX and ADX/DI cross families. Neither is the same as three consecutive DI dominance bars plus ADX>23, EMA55 and bullish candle with *mirrored full condition* exit. Direct Alorse source URL absent from searched main. Reviewer must re-check open PRs before merge.

## Evidence

Primary source was read end-to-end at this pinned commit. No independent empirical reproduction or success claim.

## Falsification plan

Recompute DMI14/ADX13 and EMA55 on closed bars and verify exact three-bar DI persistence, ADX strict >23 and candle-side gate. For default long-only compare closes against *shortEntry*, not mere DI sign crossover. Assert no Short executions, no SL when useSL=false and no pyramiding. Separately audit when an optional short or SL configuration is explicitly selected.

## Crypto portability and limitations

No symbol binding; uses only single-timeframe OHLC. Default no hard stop may leave open downside exposure. Use default long-only rule for source identification, not inferred chart-timeframe preference.

## Implementation status

not-implemented. This is an admission record only; no actual Hummingbot or Qlib execution is claimed.

## Adoption boundary

Research-only, not approved for Testnet/Mainnet. Proposed PASS is subject to independent reviewer validation of all existing six HB_READY gates and exact-head merge; it is not self-certified.

## Sources

- Primary source: https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/momentum/DMI%20Winner.pine
- Independent review contract: https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
