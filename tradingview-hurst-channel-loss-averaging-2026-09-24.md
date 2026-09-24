---
schema: strategy-research-record-v1
title: TradingView Hurst Channel Re-entry with Loss Averaging
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-24
sources:
  - https://www.tradingview.com/script/llpM5Ehy-HURST-Channel-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Hurst Channel Re-entry with Loss Averaging

## Provenance

- Public TradingView open-source strategy: `HURST Channel Strategy` by `darbat`.
- Stable source: https://www.tradingview.com/script/llpM5Ehy-HURST-Channel-Strategy/
- TradingView page states publication on 2022-03-24 and update on 2022-03-29; source reviewed as of 2026-09-24.
- The update notes that a short strategy was added, but the public page text does not specify the short-side state machine sufficiently to normalize it without inference.

## Economic mechanism

### Source-reported

The author describes a Hurst-channel strategy intended for volatile, continuous instruments, particularly futures, on timeframes above 15 minutes. The long-side rule buys a recovery through the lower channel, increases exposure when an open position is underwater relative to the channel midpoint, and exits on a downward crossing of the upper channel. The author states that it works best in uptrends or consolidations and warns that downtrends require more capital because additional positions are doubled.

### Research interpretation

The falsifiable hypothesis is not that the Hurst label itself creates alpha. The economically relevant construction is a channel mean-reversion/recovery entry combined with state-dependent loss averaging: an adverse excursion toward/below the channel midpoint is treated as an opportunity to increase exposure, while recovery to the opposite channel boundary realizes the reversion.

The doubling rule creates convex exposure to adverse persistence and may dominate both returns and tail risk. A useful test therefore has to separate any channel timing edge from the capital-allocation effect of averaging down.

## Signal

Source-supported long-side normalization:

1. Formation is evaluated from close-price/channel relationships on chart bars.
2. Long entry: open a long position when close crosses above the lower Hurst-channel band from below.
3. Additional long: when an open position's average price is below the channel's `0.5` / midpoint value, add another position at double size, according to the author's description.
4. Long exit: close when close crosses below the higher/upper channel band from above.
5. Source guidance: volatile continuous instruments, futures, and timeframes above 15 minutes.
6. The 2022-03-29 release note says a short strategy was added, but its exact entry, averaging, exit, and sizing semantics are underspecified in the reviewed public page and are therefore not reconstructed here.

Underspecified by the public description: exact Hurst-channel formula and channel parameters, source-price choice beyond the stated close-cross rules, maximum number of additions, whether doubling is recursive or only one additional order, pyramiding constraints, order timing/fill semantics, and re-entry behavior after exit.

No missing rule is filled by assumption.

## Required data

- OHLC data sufficient to reproduce the Hurst channel once its exact construction is established.
- Bar close for the documented crossing rules.
- Position state and average entry price for the loss-averaging condition.
- Source targets volatile continuous instruments/futures and timeframes above 15 minutes; portability outside that setting is unproven.
- Point-in-time channel values must use only information available at the signal timestamp; exact warm-up requirements are underspecified.

## Execution assumptions

The public page does not specify next-bar versus same-bar fills, market versus limit execution, commissions, spread, slippage, impact, margin/leverage, liquidation treatment, partial fills, or capacity. These omissions are material because doubling exposure during adverse movement can make execution and margin assumptions dominate results.

Any backtest must prevent look-ahead in channel construction and explicitly model capital/margin constraints before evaluating the averaging rule.

## Evidence

### Source-reported

The author states that the strategy works best on volatile and continuous instruments (futures), on timeframes above 15 minutes, and in uptrends or consolidations. The author also states that downtrends require more capital to open doubled positions. No independently verified Sharpe, CAGR, drawdown, win rate, or other performance statistic is taken from the page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself flags a structural weakness: downtrends require more capital because the strategy doubles additional exposure. This is directly adverse to the mean-reversion thesis when price persistence continues against the position. The reviewed page does not establish that the Hurst-channel timing component adds value independently of averaging-down exposure, and it does not provide sufficient execution/margin detail to validate tail risk.

## Falsification plan

Research-proposed tests:

1. Reconstruct the exact Hurst-channel definition from the traceable source before implementation; reject implementation if it cannot be reproduced without guessing.
2. Compare the documented channel entry/exit with fixed unit sizing against the same rule with the loss-averaging layer. This isolates timing alpha from sizing/path dependence.
3. Compare against simpler channel controls using the same entry/exit topology (for example rolling price envelopes) to test whether the Hurst construction contributes incremental out-of-sample information.
4. Ablate the doubling rule into fixed-size add, no add, and capped-add variants. If apparent performance depends primarily on recursive or concentrated averaging, treat the result as sizing leverage rather than signal alpha.
5. Evaluate persistent downtrend, gap, high-volatility and liquidation/margin-stress regimes explicitly, with realistic fees, spread and slippage.
6. Require chronological out-of-sample testing across multiple instruments and bar sizes above and around the source's stated 15-minute guidance.
7. Reject or materially weaken the hypothesis if the fixed-size signal lacks OOS edge, if simple channel controls match it, or if realistic capital constraints make the averaging variant non-robust.

## Crypto portability

`adapted`

The source discusses futures/continuous instruments rather than demonstrating crypto evidence. A crypto port would need to distinguish spot from perpetual futures and model 24/7 candle boundaries, venue fragmentation, funding, mark/index price, leverage and liquidation. The loss-averaging rule is especially sensitive to crypto's discontinuous volatility and persistent directional episodes. This is a ported hypothesis, not crypto empirical validation.

## Limitations

- Exact Hurst-channel construction and parameters: underspecified in the reviewed public description.
- Short-side rule added in the update: underspecified.
- Maximum additions and precise doubling semantics: underspecified.
- Execution, costs, margin and liquidation: underspecified.
- Not independently reproduced.
- Crypto portability: unproven.
- Source-reported qualitative suitability is not evidence of profitability.

## Implementation status

Research-only external material. No implementation or Qlib full-backtest validation has been completed by this Scout.

## Adoption boundary

This record is research material only. Its presence does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor/leaderboard entry, demonstrated profitable alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No GitHub-visible Wiki-record relationship is asserted. Potential conceptual families for later review are channel mean reversion, adverse-excursion scaling, pyramiding, and Hurst/cycle methods.

## Sources

- TradingView, darbat, `HURST Channel Strategy`, published 2022-03-24 and updated 2022-03-29: https://www.tradingview.com/script/llpM5Ehy-HURST-Channel-Strategy/ (reviewed 2026-09-24).
