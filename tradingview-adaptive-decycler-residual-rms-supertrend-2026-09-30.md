---
schema: strategy-research-record-v1
title: TradingView Adaptive Decycler Residual-RMS Supertrend
created: 2026-09-30
updated: 2026-09-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-30
sources:
  - https://www.tradingview.com/script/vEWWRSv8-Adaptive-Decycler-Supertrend-SchizoQuant/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Adaptive Decycler Residual-RMS Supertrend

## Provenance

Public TradingView open-source indicator by SchizoQuant, titled `Adaptive Decycler Supertrend [SchizoQuant]`, canonical script ID `vEWWRSv8`. Source reviewed as of 2026-09-30.

Stable source: https://www.tradingview.com/script/vEWWRSv8-Adaptive-Decycler-Supertrend-SchizoQuant/

The source is an indicator, not a complete trading strategy. This record therefore treats its regime changes as an alpha hypothesis to test rather than as source-validated orders.

## Economic mechanism

### Source-reported

The author combines three functions: directional efficiency adapts the Decycler cutoff; residual RMS measures price displacement around that adaptive baseline; and persistent Supertrend-style trailing converts the asymmetric RMS envelopes into bullish/bearish regimes. Higher directional efficiency makes the baseline more responsive, while lower efficiency makes it smoother. The author distinguishes this construction from conventional ATR-based Supertrend because both the baseline response and reversal distance adapt through separate mechanisms.

### Research interpretation

Hypothesis: directional persistence may be captured more robustly when the trend baseline adapts to path efficiency while the reversal threshold adapts to baseline-relative residual energy. If that separation contains incremental information, regime flips should predict continuation better than a conventional fixed-parameter Supertrend after controlling for turnover and costs.

Component roles:

- Regime adaptation: directional-efficiency measure controls Decycler responsiveness.
- Dynamic baseline: adaptive Decycler.
- Volatility/displacement estimate: RMS of price-minus-Decycler residuals.
- Directional state: persistent trailing envelopes.
- Candidate alpha event: transition of the persistent regime from bearish to bullish or bullish to bearish.

This mechanism is plausible but unvalidated. Complexity itself is not evidence of alpha.

## Signal

Source-reported construction:

1. Over a configurable Efficiency Length, compare net price movement with total distance travelled and normalize efficiency to 0-1.
2. Map efficiency into user-defined Minimum Cutoff / Maximum Cutoff values for the Decycler. Higher efficiency moves toward Minimum Cutoff; lower efficiency moves toward Maximum Cutoff.
3. Convert the adaptive cutoff into the Decycler smoothing coefficient and calculate the adaptive Decycler baseline.
4. Compute residual = price - adaptive Decycler.
5. Over the configurable Residual RMS Length, average squared residuals and take the square root.
6. Form upper and lower envelopes by adding/subtracting independently scaled residual RMS values from the Decycler.
7. In a bullish regime, the lower envelope is the trailing basis and may rise but not fall until reversal. In a bearish regime, the upper envelope may fall but not rise until reversal.
8. Bullish reversal: source moves above the previous bearish trailing level.
9. Bearish reversal: source moves below the previous bullish trailing level.
10. Otherwise preserve the current regime. LONG/SHORT markers appear only on regime changes.

Source-reported parameters are configurable Efficiency Length, Minimum Cutoff, Maximum Cutoff, Residual RMS Length, Upper Multiplier, Lower Multiplier, and source. The reviewed page does not expose numeric defaults for these inputs.

Research-proposed operationalization for later testing only: evaluate a long entry on the next tradable bar after a confirmed bullish regime flip and a short entry on the next tradable bar after a confirmed bearish regime flip; exit/reverse on the opposite confirmed flip. This mapping is not source-reported because the source is an indicator rather than an order-executing strategy.

The exact Decycler cutoff-to-smoothing-coefficient formula is not specified in the reviewed page text and is therefore an implementation data gap for this normalized record rather than something to infer.

## Required data

Source-supported minimum data dependency:

- Price series for the selected TradingView source.
- Bar timestamps sufficient to construct the chosen chart timeframe.
- Historical bars sufficient for the efficiency and residual-RMS windows.

Research implementation would require standard OHLC bar data if testing next-bar execution. The source page does not require volume, funding, order book, trades/aggressor side, open interest, options data, or higher-timeframe requests.

Universe, venue, market type, timeframe, timezone, and crypto instrument are not specified by the reviewed source and remain data gaps.

Point-in-time constraint: use only information available through the completed signal bar. The author states that the script does not use higher-timeframe requests or lookahead logic.

## Execution assumptions

The source is an indicator and does not specify an execution model.

Research-proposed for falsification only:

- Evaluate regime state on completed bars.
- Enter/reverse no earlier than the next tradable bar after a confirmed flip.
- Compare market-order and conservative slippage/fee assumptions appropriate to each tested crypto venue.

Not source-specified: same-bar versus next-bar fill, order type, fees, spread, slippage, market impact, capacity, funding, leverage, margin, borrow/shorting constraints, latency, partial fills, or failure handling. These must not be treated as zero.

## Evidence

### Source-reported

No source-reported return, Sharpe, CAGR, drawdown, win rate, profit factor, or other performance statistic was identified on the reviewed TradingView page.

The author states that the indicator does not use higher-timeframe requests or lookahead logic and explicitly describes it as a trend-regime indicator rather than a complete trading system.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The author notes that directional efficiency depends on historical price movement, recent large residual deviations can widen the envelope, and the persistent trailing mechanism can react late during abrupt reversals. These are direct failure modes for the hypothesis.

No independent negative empirical result was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

Test the hypothesis on liquid crypto spot and perpetual instruments across multiple bar horizons using point-in-time bars and realistic venue costs.

Required controls and ablations:

- Conventional ATR Supertrend baseline.
- Fixed-cutoff Decycler plus residual-RMS trail.
- Adaptive Decycler without residual-RMS adaptation.
- Full adaptive Decycler + residual-RMS construction.

Measure out-of-sample risk-adjusted return, drawdown, turnover, trade count, regime duration, false-flip frequency, and cost sensitivity.

Research-defined falsification threshold: reject the incremental-alpha claim if the full construction does not improve out-of-sample risk-adjusted performance or false-flip behavior versus the simpler controls after realistic costs, or if any apparent benefit is confined to a narrow symbol/timeframe/parameter neighborhood.

Parameter-neighborhood stability around Efficiency Length, cutoff bounds, RMS length, and asymmetric multipliers is required. Failure to reconstruct the exact source formula from a public auditable source before implementation is itself a stop condition.

## Crypto portability

**unproven**

The reviewed source does not provide crypto-specific empirical evidence. The mechanism uses price history only and is mechanically portable, but portability is not validation.

Crypto-specific tests must account for 24/7 candle boundaries, spot-versus-perpetual behavior, venue fragmentation, funding for perpetual positions, mark/index versus traded price, and materially different fee/slippage regimes.

## Limitations

- Indicator, not a complete source-specified trading strategy.
- Numeric input defaults are not exposed in the reviewed page text.
- Exact Decycler cutoff-to-smoothing formula is underspecified in the reviewed page text.
- Universe, venue, timeframe, and holding/execution semantics are unspecified.
- No source-reported empirical performance evidence was identified.
- Crypto portability is unproven.
- Not independently reproduced.

## Implementation status

Not implemented in the research stack. No Qlib full backtest or other internal validation has been performed.

## Adoption boundary

Research-only and not approved.

Presence in this repository does not mean the record passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, demonstrated profitable or validated alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No stable related Hermes Wiki Brain record was identified from the GitHub-only evidence available to this Scout. No Wiki link is fabricated.

## Sources

- SchizoQuant, `Adaptive Decycler Supertrend [SchizoQuant]`, TradingView, public open-source indicator, reviewed 2026-09-30: https://www.tradingview.com/script/vEWWRSv8-Adaptive-Decycler-Supertrend-SchizoQuant/
