---
schema: strategy-research-record-v1
title: "TradingView Dynamic EMA Trend + Daily VWAP Confirmation"
created: 2026-09-28
updated: 2026-09-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-28
sources:
  - https://www.tradingview.com/script/Hjnwl8o2-Dynamic-Trend-Indicator-DTI-VWAP-Filter/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Dynamic EMA Trend + Daily VWAP Confirmation

## Provenance

Public TradingView open-source indicator **Dynamic Trend Indicator (DTI) - VWAP Filter**, author/page identity `CsokosGeza`, published 2025-03-26. Stable source: https://www.tradingview.com/script/Hjnwl8o2-Dynamic-Trend-Indicator-DTI-VWAP-Filter/ . Source reviewed as of 2026-09-28.

The page describes both the indicator construction and a suggested trading interpretation. This record normalizes that public description rather than copying the Pine source.

## Economic mechanism

### Source-reported

The author frames the DTI as a trend-following indicator intended to reduce false signals in choppy markets. Its trend line is a custom EMA whose effective period changes with ATR-scaled volatility and absolute price momentum: stronger trend strength shortens the period for responsiveness, while weaker conditions lengthen it for stability. A daily VWAP filter is used as directional confirmation, and a cooldown prevents rapid signal reversals.

### Research interpretation

The falsifiable hypothesis is that an adaptive trend estimator can preserve responsiveness during directional moves while suppressing noise in weak regimes, and that requiring price to be on the same side of the current-day VWAP removes crossovers that conflict with intraday volume-weighted positioning.

Component roles:

- **Adaptive regime / trend estimator:** dynamic-period EMA driven by ATR and price momentum.
- **Primary trigger:** price crossing the adaptive trend line.
- **Confirmation:** price must be above daily VWAP for long signals and below daily VWAP for short signals.
- **Signal-frequency control:** cooldown bars; this is not assumed to contribute alpha and requires ablation.
- **Optional smoothing:** secondary EMA on the dynamic trend line; also requires ablation.

This is a trend-persistence hypothesis, not evidence that dynamic parameterization, VWAP, smoothing, or cooldown independently adds alpha.

## Signal

Source-described defaults and rules:

- Base length: 14.
- Volatility multiplier: 1.5.
- Trend threshold: 0.5.
- Dynamic EMA period constrained to 5-50.
- Optional smoothing: enabled by default; smoothing EMA length 3.
- Cooldown: 5 bars by default.
- Volatility: ATR over the base length, scaled by the volatility multiplier.
- Trend strength: absolute price momentum over the base length divided by the volatility factor.
- Stronger trend strength shortens the dynamic EMA period; weaker trend strength lengthens it.
- Daily VWAP: cumulative `close * volume / volume`, reset at each new day.
- Long signal: price crosses above the dynamic trend line, price is above daily VWAP, and cooldown has elapsed.
- Short signal: price crosses below the dynamic trend line, price is below daily VWAP, and cooldown has elapsed.
- Suggested use: intraday, especially 1h or 4h; the source gives a 4h SOLUSDT example.
- Suggested trading interpretation: a buy signal can open long; a sell signal can open short or exit long.

The exact algebra mapping trend strength into the integer/dynamic EMA period is **underspecified** in the reviewed public prose. Exact short-position exit semantics, position reversal behavior, re-entry while already positioned, and whether signals are evaluated intrabar or only on confirmed closes are also **underspecified**. They must not be silently invented.

Any later choice of a complete position-state machine, fill timing, stop, take-profit, or holding-period rule is **research-proposed** unless recovered directly from the source.

## Required data

- OHLCV bars for the traded instrument.
- Source examples/support include crypto, forex, and stocks; SOLUSDT 4h is an explicit example.
- Intraday timestamps sufficient to identify daily boundaries.
- ATR inputs from high, low, and prior close.
- Close and volume for the source-described daily VWAP.
- Point-in-time computation only: adaptive EMA, ATR, momentum, VWAP, and cooldown state must use information available at signal formation.
- Venue, crypto market type (spot versus perpetual), timezone used for the daily reset, and session/calendar convention are **underspecified**.

For 24/7 crypto, the daily VWAP reset boundary is material and must be fixed before reproduction rather than inferred after seeing results.

## Execution assumptions

The source recommends entering when a displayed buy/sell signal appears, but does not provide a complete execution model.

**Underspecified / data gap:**

- confirmed-close versus intrabar signal execution;
- same-bar versus next-bar fill;
- market versus limit orders;
- bid-ask spread;
- fees and commissions;
- slippage and market impact;
- latency and partial fills;
- leverage, margin, borrow, and short availability;
- perpetual funding and liquidation treatment;
- position sizing;
- stop-loss and take-profit rules (the source only suggests using trend line/VWAP as possible support/resistance references).

A leakage-safe reproduction should predeclare these choices. Any such choices not present in the source are **research-proposed**.

## Evidence

### Source-reported

The source states that the indicator is intended to reduce whipsaws and is suited to trending markets, and provides a qualitative 4h SOLUSDT example. It does not provide a traceable Sharpe ratio, CAGR, profit factor, drawdown, win rate, or other empirical performance statistic in the reviewed page.

The author explicitly notes lag during sharp reversals, remaining false signals in strongly ranging markets, and dependence on whether the market respects daily VWAP.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself identifies lagging response, ranging-market whipsaws, and VWAP unreliability in low-volume or erratic markets. No independent empirical validation was found in the reviewed source; absence is not evidence of no additional negative result.

## Falsification plan

1. Reconstruct the exact dynamic-period algebra from the public implementation before any performance claim. If it cannot be recovered unambiguously, do not substitute a guessed formula.
2. Test a plain fixed-length EMA crossover baseline against the adaptive EMA using identical execution and costs.
3. Ablate the daily VWAP confirmation: adaptive EMA alone versus adaptive EMA + VWAP.
4. Ablate smoothing and cooldown separately; treat either as useful only if it improves out-of-sample results after controlling for lower trade count.
5. Run the source defaults first, then a predeclared neighborhood around base length, volatility multiplier, trend threshold, smoothing length, and cooldown. Reject a knife-edge parameter optimum.
6. Split trending and ranging regimes using a regime label defined before evaluating strategy outcomes. The hypothesis is materially weakened if adaptation does not improve the trend/chop trade-off versus fixed EMA baselines.
7. For crypto, compare at least two predeclared daily VWAP reset conventions, including UTC midnight. If the sign of the edge depends on an arbitrary reset boundary, treat the VWAP component as unstable.
8. Use chronological out-of-sample evaluation across multiple liquid instruments and timeframes, including the source's 4h SOLUSDT example where data permit.
9. Apply realistic fees, spread, slippage, and one-bar execution delay. Failure under plausible friction weakens the tradability claim.
10. **Research-defined falsification threshold:** reject the composite alpha hypothesis if net out-of-sample risk-adjusted performance does not exceed the fixed-EMA baseline, or if the VWAP/smoothing/cooldown components fail to add stable incremental value across regimes after costs.

## Crypto portability

**direct** as a research hypothesis: the source explicitly presents crypto as a target market and gives SOLUSDT 4h as an example.

Portability risks remain substantial: 24/7 daily-boundary choice, spot versus perpetual differences, funding, mark/index versus last price, venue fragmentation, volume quality, and crypto-specific execution costs are not resolved by the source.

## Limitations

- Dynamic-period mapping is **underspecified** in the reviewed prose.
- Full position/exit state machine is **underspecified**.
- Daily VWAP timezone/reset convention for 24/7 crypto is a **data gap**.
- Execution and cost model is a **data gap**.
- Source evidence is qualitative rather than a traceable performance study.
- Adaptive parameters may overfit regime noise rather than improve trend estimation.
- Cooldown can mechanically improve apparent signal quality by reducing observations without adding predictive information.
- VWAP confirmation and trend-line crossover both depend on price, so apparent confluence may contain redundant information.
- Not independently reproduced.

## Implementation status

Research capture only. No implementation in the research stack, Qlib full backtest, production candidate promotion, paper trading, testnet, or live validation has been performed.

## Adoption boundary

This record is **research-only**, **not-implemented**, and **not-approved**.

Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor/leaderboard strategy, demonstrated profitable alpha, or received Paper/Testnet/Live approval.

## Related Wiki records

No stable Hermes Wiki Brain page was verified in this GitHub-only run; no Wiki link is fabricated.

## Sources

- TradingView — CsokosGeza, **Dynamic Trend Indicator (DTI) - VWAP Filter**, published 2025-03-26, reviewed 2026-09-28: https://www.tradingview.com/script/Hjnwl8o2-Dynamic-Trend-Indicator-DTI-VWAP-Filter/
