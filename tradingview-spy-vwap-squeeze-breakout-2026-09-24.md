---
schema: strategy-research-record-v1
title: TradingView SPY VWAP Squeeze-Release Breakout
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
  - https://www.tradingview.com/script/HNql4p3J-SPY-VWAP-Squeeze-Breakout/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView SPY VWAP Squeeze-Release Breakout

## Provenance

- Public TradingView open-source strategy: `SPY VWAP + Squeeze Breakout` by `busapete`.
- Stable source: https://www.tradingview.com/script/HNql4p3J-SPY-VWAP-Squeeze-Breakout/
- TradingView page displays publication date `Mar 12`; source reviewed as of 2026-09-24. The reviewed page does not expose a publication year in its visible description, so no year is inferred here.
- The source identifies SPY as the intended instrument and describes the strategy as intraday.

## Economic mechanism

### Source-reported

The author combines a Bollinger-Band/Keltner-Channel squeeze with VWAP location and candle direction. A squeeze is present while the Bollinger Bands are inside the Keltner Channels. The source describes a directional trade when that compression releases: long above VWAP on a bullish candle and short below VWAP on a bearish candle. Positions are closed when price crosses back over VWAP in the adverse direction.

### Research interpretation

The falsifiable hypothesis is that volatility compression followed by release contains directional continuation information, but only when contemporaneous price location relative to session VWAP and candle direction agree with the breakout direction. In this interpretation, the squeeze is a regime/trigger component, VWAP is an intraday directional-location filter, and candle sign is a minimal momentum confirmation.

The three components may simply repackage recent price direction and volatility state rather than contribute independent alpha. They therefore require explicit ablation against simpler controls.

## Signal

Source-supported normalization:

1. Squeeze state: Bollinger Bands are inside Keltner Channels.
2. Trigger: the squeeze releases / `fires`.
3. Long entry: squeeze release while price is above VWAP and the current bar closes above its open.
4. Short entry: squeeze release while price is below VWAP and the current bar closes below its open.
5. Long exit: price crosses back below VWAP.
6. Short exit: price crosses back above VWAP.
7. The source states that Bollinger length/standard-deviation and Keltner length/multiplier are configurable inputs and that Keltner range calculation uses `ta.tr(true)`.

Underspecified in the reviewed public description: exact default parameter values, precise definition/timing of the transition from squeeze-on to squeeze-release, VWAP anchoring/reset semantics, chart timeframe, signal-to-order timing, re-entry/pyramiding behavior, position sizing, and whether an exit can reverse immediately.

No missing detail is filled by assumption. Any later operationalization of those gaps must be labeled `research-proposed`.

## Required data

- Intended source instrument: SPY ETF.
- Intraday OHLCV bars.
- Session-aware VWAP inputs and session/calendar timestamps.
- Bollinger Bands require the configured price series, lookback and standard-deviation calculation.
- Keltner Channels require the configured price series, lookback/multiplier and true range; the source explicitly mentions `ta.tr(true)`.
- Point-in-time calculations must use only information available at signal formation. Exact warm-up and session-reset rules are underspecified.

## Execution assumptions

The source does not specify same-bar versus next-bar fills, market/limit order type, commissions, bid-ask spread, slippage, market impact, capacity, partial fills, latency, or position sizing. Those assumptions must not be inferred from TradingView's strategy display.

For SPY intraday testing, VWAP/session boundaries must be aligned to the source's intended trading session without future information. If adapted to a 24/7 market, a session anchor must be explicitly defined rather than silently borrowing an equity-session reset.

## Evidence

### Source-reported

The source describes the construction as a framework for backtesting SPY intraday volatility strategies and states that the combination is intended to filter noise and focus on squeeze breakouts confirmed by price location and momentum. No Sharpe, CAGR, drawdown, win rate, profit factor, or other numerical performance claim is adopted from the reviewed page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independent negative empirical result was identified in the reviewed source; absence is not evidence of no negative result. The public description itself leaves material parameter, timing, VWAP-anchor, and execution details unspecified. The construction also stacks three highly price-dependent filters, creating a material risk that apparent selectivity is redundant rather than incremental.

## Falsification plan

Research-proposed tests:

1. Reconstruct only source-supported squeeze, VWAP and candle-direction rules; do not optimize missing defaults into existence.
2. Baseline ladder: compare unconditional directional breakout/momentum, squeeze release alone, squeeze + VWAP, squeeze + candle sign, and the full squeeze + VWAP + candle-sign construction.
3. Compression control: compare Bollinger-inside-Keltner squeeze with simpler realized-volatility percentile and ATR/range-compression states using matched entry timing.
4. VWAP placebo/control: compare session VWAP with session open, rolling mean/EMA, and a no-location-filter variant. Reject a special VWAP interpretation if it adds no stable OOS value.
5. Candle-sign control: replace bullish/bearish candle confirmation with signed one-bar return and remove it entirely. Treat equivalent results as evidence that the component is merely repackaged price direction.
6. Require chronological out-of-sample SPY testing across multiple volatility regimes and realistic spread, fees and slippage. Keep parameter selection strictly in-sample or walk-forward.
7. Test session-boundary sensitivity because VWAP reset semantics can materially alter the signal.
8. Reject or materially weaken the hypothesis if the full construction fails to improve risk-adjusted OOS performance and drawdown versus simpler controls after costs, or if its apparent edge depends on narrow parameter choices.

## Crypto portability

`adapted`

The cited source is SPY-specific and does not provide crypto evidence. A crypto adaptation would need an explicit VWAP/session anchor in a 24/7 market, venue-specific volume treatment, candle-boundary convention, and separate spot/perpetual handling. Perpetual testing must additionally model funding, mark/index prices, leverage and liquidation. This is a ported hypothesis, not crypto empirical validation.

## Limitations

- Exact default Bollinger/Keltner parameters: underspecified in the reviewed page.
- Exact squeeze-release transition semantics: underspecified.
- VWAP anchoring/reset rule: underspecified.
- Intended intraday timeframe: underspecified.
- Order timing, costs and sizing: underspecified.
- Source is SPY-specific; crypto portability is unproven.
- Not independently reproduced.

## Implementation status

Research-only external material. No implementation or Qlib full-backtest validation has been completed by this Scout.

## Adoption boundary

This record is research material only. Its presence does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor/leaderboard entry, demonstrated profitable alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No GitHub-visible Wiki-record relationship is asserted. Conceptually related families include volatility-compression breakouts, session VWAP trend filters, and intraday momentum confirmation.

## Sources

- TradingView, `busapete`, `SPY VWAP + Squeeze Breakout`: https://www.tradingview.com/script/HNql4p3J-SPY-VWAP-Squeeze-Breakout/ (page displays `Mar 12`; reviewed 2026-09-24).
