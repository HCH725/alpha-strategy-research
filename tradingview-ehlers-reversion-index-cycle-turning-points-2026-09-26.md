---
schema: strategy-research-record-v1
title: Ehlers Reversion Index Cycle Turning-Point Hypothesis
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
  - https://www.tradingview.com/script/V35NeC45-TASC-2026-01-The-Reversion-Index/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Ehlers Reversion Index Cycle Turning-Point Hypothesis

## Provenance

Public TradingView open-source indicator page, **TASC 2026.01 The Reversion Index**, published by `PineCodersTASC` on December 16, 2025. Stable source: https://www.tradingview.com/script/V35NeC45-TASC-2026-01-The-Reversion-Index/ . Source reviewed as of 2026-09-26.

The page states that the script implements John F. Ehlers' Reversion Index as presented in the January 2026 TASC Traders' Tips article, "Identifying Peaks And Valleys In Ranging Markets." This record normalizes the public TradingView description and does not redistribute Pine code.

Current-`main` GitHub dedup found no record citing canonical TradingView script ID `V35NeC45`, the exact PineCodersTASC Reversion Index title, or the normalized Smooth-Reversion-Index/Trigger crossing construction.

## Economic mechanism

### Source-reported

The source presents the Reversion Index as the mean-reversion counterpart to Ehlers' Continuation Index. Its stated purpose is to identify peaks and valleys in cyclical/ranging markets rather than estimate a trend over a large sample. The raw index normalizes net price change by the sum of absolute price changes over the same period. The raw value is then smoothed with Ehlers' SuperSmoother, while a faster Trigger line is constructed using half the smoothing period. Peaks and valleys are interpreted from crossings of the Trigger and Smooth lines.

### Research interpretation

The falsifiable hypothesis is that, when price behavior is dominated by a reasonably stable cycle rather than persistent trend, normalized directional displacement should lose dominance near local cycle extremes. A faster-smoothed version of that normalized displacement crossing a slower-smoothed version may therefore mark turning points with less noise than an unsmoothed reversal measure.

This mechanism depends on cycle structure being present and sufficiently stable. It is not evidence that the indicator predicts profitable reversals in trending, regime-shifting, or crypto markets.

## Signal

Source-reported construction:

- Raw Reversion Index: net change in price over a chosen length, normalized by the sum of absolute price changes over the same period.
- Smooth line: raw Reversion Index smoothed using Ehlers' SuperSmoother.
- Trigger line: a faster smoothed line using half the smoothing period of the Smooth line.
- Source-reported smoothing lengths: Ehlers suggests 8 for the Reversion Index smoothing and 4 for the Trigger; the TradingView implementation hard-codes these values.
- Source-reported cycle guidance: set `Length` to approximately half the expected cycle length. The page gives a 20-bar expected cycle → 10-bar Length example.
- Turning-point event: crossings of Trigger and Smooth are interpreted as peaks and valleys.

The public description does **not** unambiguously state which crossing direction maps to a long entry versus a short entry, nor does it specify a complete position-management rule, holding period, re-entry rule, or exit rule. Those fields are therefore **underspecified**.

A directional strategy mapping such as buying one crossing class and selling/shorting the opposite class would be `research-proposed` and must first be verified against the source implementation or tested as a separate operationalization; it is not asserted here as source-reported.

Signal formation timing and same-bar versus next-bar order timing are also **underspecified** in the reviewed public description.

## Required data

Source-reported construction requires a price series sufficient to compute period-to-period net and absolute price changes. The reviewed page does not specify:

- a required instrument or universe;
- venue;
- spot/futures/perpetual market type;
- canonical timeframe;
- timezone or candle boundary convention;
- missing-data treatment.

For research implementation, OHLCV bars could supply the needed price series, but the exact source price field used by the script should be verified before reproduction rather than assumed.

Point-in-time constraint: only information available through the completed signal bar should be used in any reconstruction; exact execution lag remains `research-proposed`.

## Execution assumptions

The source page is an indicator description, not a complete execution specification. Market versus limit orders, same-bar versus next-bar fills, fees, spread, slippage, market impact, capacity, leverage, margin, borrow/shorting, funding, latency, partial fills, and failure handling are all **data gaps / underspecified**.

No zero-cost assumption should be inferred from their omission.

## Evidence

### Source-reported

The source explains the indicator construction and intended use for identifying peaks and valleys in ranging/cyclical markets. It does not provide a traceable Sharpe ratio, CAGR, drawdown, win rate, profit factor, or other strategy-performance result in the reviewed TradingView description.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No direct empirical failure result is reported on the reviewed TradingView page. However, the source itself limits the intended interpretation: the Reversion Index is meant to identify peaks and valleys within a cycle, and using it over a large sample would tend toward trend estimation rather than its intended purpose.

The reviewed source provides no complete trading rule and no transaction-cost evidence. Absence of a reported negative result is not evidence of robustness or profitability.

## Falsification plan

1. Reconstruct the indicator from the public source semantics and first verify numerical agreement with the TradingView implementation before testing alpha.
2. `research-proposed`: infer/test the two possible directional mappings of Trigger/Smooth crossings separately rather than assuming which crossing is a peak or valley trade.
3. Compare against simple controls: raw normalized net-change reversal, an unsmoothed crossing baseline, and a conventional price/return mean-reversion baseline.
4. Stratify results by ranging versus trending regimes. The mechanism is materially weakened if any apparent edge is not concentrated in cyclical/ranging regimes.
5. Test sensitivity around the source-suggested relationship `Length ≈ expected cycle / 2` and smoothing pair 8/4. A result that exists only at one narrow parameter point should be treated as fragile.
6. Apply walk-forward/out-of-sample validation with all cycle estimates and parameters formed point-in-time.
7. Apply realistic fee, spread, slippage, and turnover assumptions appropriate to the tested venue.
8. `research-defined falsification threshold`: reject the directional-alpha interpretation if out-of-sample net performance does not beat the matched simple mean-reversion control after costs, or if crossing direction fails to produce stable sign-consistent forward returns across independent regimes.

## Crypto portability

**unproven**

The reviewed TradingView source does not demonstrate the Reversion Index on crypto markets. Applying it to crypto is therefore a ported hypothesis, not crypto empirical evidence.

Crypto-specific risks include 24/7 session structure, unstable cycle length, venue fragmentation, spot-versus-perpetual differences, funding, mark/index-price conventions, liquidation-driven trends, and candle-boundary choices. These can invalidate a cycle-turning-point assumption even if the indicator behaves sensibly in other markets.

## Limitations

- `underspecified`: directional long/short mapping from crossing direction is not explicit in the reviewed public description.
- `underspecified`: complete entry/exit/holding/re-entry logic is absent.
- `underspecified`: exact source price field and execution timing are not established from the description.
- `not independently reproduced`.
- `unproven`: no crypto validation is supplied by the source.
- No source-reported strategy performance is available in the reviewed page.
- Expected-cycle estimation itself is not operationally specified on the page; only the relationship between expected cycle and Length is described.

## Implementation status

Research normalization only. No implementation in the research stack, Qlib full backtest, or independent numerical reproduction has been completed.

## Adoption boundary

This artifact is `research-only`, `not-implemented`, and `not-approved`.

Its presence in this repository does **not** mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received Paper, Testnet, or Live approval.

## Related Wiki records

No stable Hermes Wiki Brain record was resolved in this GitHub-only Scout cycle; no Wiki link is fabricated.

## Sources

- https://www.tradingview.com/script/V35NeC45-TASC-2026-01-The-Reversion-Index/
