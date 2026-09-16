---
schema: strategy-research-record-v1
title: "TradingView ATR ZigZag Pivot Breakout"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - breakout
  - zigzag
  - atr
status: research-only
confidence: medium
source_as_of: 2026-09-16
sources:
  - https://www.tradingview.com/script/Hi0gI790-ATR-ZigZag-Breakout/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView ATR ZigZag Pivot Breakout

## Provenance

- Public TradingView open-source strategy: **ATR ZigZag Breakout** by **ReflexSignals**.
- Published: 2025-12-08.
- Stable source URL: https://www.tradingview.com/script/Hi0gI790-ATR-ZigZag-Breakout/
- Source reviewed as of 2026-09-16.
- This record normalizes the publicly described trading logic rather than reproducing the Pine source code.

## Economic mechanism

### Source-reported

The author argues that stop orders and breakout participation tend to cluster around clear swing highs and lows. The strategy uses an ATR-filtered ZigZag to identify pivots intended to be less noisy than fixed-bar or fractal pivots, then places stop-market orders at those pivot levels to participate when price breaks through them. The author describes the approach as especially suited to volatile intraday instruments, including liquid crypto pairs.

### Research interpretation

This is a volatility-normalized structural-breakout hypothesis. ATR-based pivot confirmation attempts to suppress small price oscillations before defining a candidate liquidity/breakout level. The hypothesized alpha is continuation after price crosses a confirmed swing extreme where clustered stop execution and breakout participation may create short-horizon directional order flow. The ATR bracket is risk management rather than the predictive signal.

## Signal

Source-described normalized logic:

1. Use an ATR-threshold ZigZag to identify swing highs and swing lows. A pivot becomes confirmed only after price has moved sufficiently far in the opposite direction according to the ZigZag's ATR threshold.
2. When a new swing direction is detected and the most recent pivot has not already been broken in the current swing leg, arm one candidate stop-market entry:
   - long candidate: most recent confirmed swing high;
   - short candidate: most recent confirmed swing low.
3. Entry occurs if price trades through the armed pivot level and fills the stop order.
4. After entry, the source describes a bracket:
   - stop-loss distance = ATR × configurable stop-loss multiplier;
   - take-profit distance = stop-loss distance × configurable reward/risk multiplier.
5. A pivot level is not reused after it has traded during the same swing leg.
6. If price reverses and the ZigZag establishes a new opposite swing before the pending breakout order fills, cancel the pending order and rotate to the new candidate direction.
7. An optional session filter can restrict eligible trading hours.

Underspecified in the public description: the exact ATR period, ZigZag ATR threshold/multiplier defaults, ATR sampling timestamp for the bracket, stop-loss multiplier default, reward/risk default, and precise intrabar ordering semantics when pivot confirmation/cancellation and a breakout could occur within the same bar. These must be recovered from the open-source implementation or explicitly parameterized before a faithful backtest; they are not invented here.

## Required data

- Instrument: source says volatile instruments and explicitly includes liquid crypto pairs as suitable examples.
- Market type: not fixed by the source; crypto spot or perpetual use would require instrument-specific execution assumptions.
- Timeframe: intraday is source-recommended; no single crypto timeframe is mandated.
- Required fields: timestamp plus OHLC for ZigZag/pivot, breakout and ATR calculation.
- Session/timezone information is additionally required if the optional session filter is enabled.
- Point-in-time requirement: only confirmed pivots available at the decision timestamp may be used. Future ZigZag pivots or subsequently revised swing structure must not leak backward into prior signals.

## Execution assumptions

The source explicitly describes stop-market entry at the confirmed pivot and an ATR-based stop-loss / reward-risk take-profit bracket after fill. It also specifies cancellation of an unfilled candidate when the swing direction reverses.

Fees, spread, slippage, market impact, latency, partial fills, crypto perpetual funding, leverage/margin, venue choice, and gap-through-stop behavior are underspecified. A research implementation must model stop-order slippage and causal pivot confirmation rather than assuming frictionless fills exactly at the plotted pivot.

## Evidence

### Source-reported

The source presents the strategy as an intraday breakout/scalping method and states that ATR-filtered pivots tend to be more meaningful and less noisy than pivots based on fixed bar counts or fractals. It names NQ, GC, and liquid crypto pairs as example volatile instruments. No independently verified performance statistic is adopted in this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independent negative study was identified in the reviewed TradingView source. Important hypothesis risks follow directly from the mechanism: false breakouts can produce adverse stop-market fills, ZigZag confirmation delay can make candidate levels stale, and transaction costs/slippage can dominate a short-horizon breakout edge. Absence of cited negative evidence is not evidence of robustness.

## Falsification plan

- Reconstruct the ATR ZigZag causally and verify that historical pivot labels never use future information.
- Compare against a simpler fixed-lookback high/low breakout baseline to test whether ATR-filtered pivots add incremental value.
- Evaluate long and short legs separately across liquid crypto instruments and multiple intraday horizons.
- Measure performance after realistic taker fees, spread and stop-order slippage; reject the economic hypothesis if apparent edge disappears under plausible costs.
- Stratify results by realized-volatility and trend/chop regimes to test the source claim that volatile conditions are preferable.
- Test sensitivity to ATR period/threshold, stop multiplier and reward/risk multiplier using bounded predeclared ranges rather than retrospective optimization.
- Require out-of-sample persistence and examine whether results are concentrated in a few breakout episodes or instruments.

## Crypto portability

**direct but unproven** — the source explicitly names liquid crypto pairs as suitable instruments, so crypto use is source-contemplated rather than purely ported from another asset class. However, no independent crypto reproduction has been performed here.

Crypto-specific risks include 24/7 candle boundaries, venue fragmentation, spot-versus-perpetual microstructure, taker fees, funding for perpetual positions, liquidation/margin mechanics, and materially different stop-market slippage during fast breakouts.

## Limitations

- Not independently reproduced.
- Several numerical defaults are underspecified in the public prose and must not be guessed.
- ZigZag strategies are particularly vulnerable to look-ahead/repainting mistakes if pivot confirmation is implemented non-causally.
- Source suitability claims are not evidence of profitability.
- Stop-loss and take-profit rules manage realized payoff but do not establish predictive alpha by themselves.

## Implementation status

Research record only. No implementation or validation in the user's quantitative research stack has been completed as part of this Scout cycle.

## Adoption boundary

`research-only`. This record does not establish profitable alpha, implementation approval, backtest validation, paper-trading approval, testnet approval, or live-trading approval.

## Related Wiki records

No stable Hermes Wiki Brain link was verified through the GitHub-only workflow; none is fabricated.

## Sources

- ReflexSignals, **ATR ZigZag Breakout**, TradingView, published 2025-12-08, reviewed 2026-09-16: https://www.tradingview.com/script/Hi0gI790-ATR-ZigZag-Breakout/
