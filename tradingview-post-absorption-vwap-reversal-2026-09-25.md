---
schema: strategy-research-record-v1
title: TradingView Post-Absorption VWAP Reversal
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-25
sources:
  - https://www.tradingview.com/script/j6iKZmCf-Post-Absorption-VWAP-Reversal-Engine-V1-6/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Post-Absorption VWAP Reversal

## Provenance

Public TradingView open-source strategy `Post-Absorption VWAP Reversal Engine V1.6` by `secretmorina`. Stable source URL: https://www.tradingview.com/script/j6iKZmCf-Post-Absorption-VWAP-Reversal-Engine-V1-6/ . The page shows the current version updated May 23 and describes an intraday backtesting/paper-trading model. Source reviewed 2026-09-25.

## Economic mechanism

### Source-reported

The author frames the setup as an effort-versus-result absorption hypothesis: unusually high volume combined with unusually small price displacement may indicate aggressive flow being absorbed by passive liquidity. When that event occurs away from session VWAP, the strategy treats VWAP as a fair-value reference and looks for a reversal toward it.

### Research interpretation

The falsifiable hypothesis is that a high-volume/low-displacement event contains incremental short-horizon mean-reversion information when conditioned on location relative to session VWAP. The volume percentile is the effort proxy, candle displacement normalized by ATR is the result proxy, and VWAP supplies directional context. These components should be tested separately because the composite may add no information beyond ordinary VWAP distance, volume surprise, or volatility-normalized reversal.

## Signal

Source-described formation is intraday and bar based.

- Absorption candidate: volume is high in its recent distribution and candle displacement is small relative to ATR.
- The source gives illustrative examples of volume in the top 90% or 95% of recent bars and candle body / ATR below a threshold such as 0.30; these are examples rather than evidence that one fixed setting is universally optimal.
- Above session VWAP: the event is classified as possible buyer absorption and can form a short fade candidate toward VWAP.
- Below session VWAP: the event is classified as possible seller absorption and can form a long fade candidate toward VWAP.
- Near VWAP: the source describes the event as less directional / ambiguous.
- The strategy supports long-only, short-only, or both-side modes, multiple exit modes, a next-bar entry option, and same-bar exit protection.

The public description does not unambiguously expose the percentile lookback, ATR length, exact VWAP-distance definition for `near`, the complete exit-mode formulas/default, re-entry rules, sizing, or every order-state transition. Those fields are underspecified and must not be inferred.

Research-proposed operationalization for later testing: compare a strictly next-bar implementation with a same-bar-permitted implementation only if the latter can be reproduced without look-ahead; separately test exit-at-VWAP versus fixed-horizon exits. These are research proposals, not source-reported rules.

## Required data

- Intraday OHLCV.
- Session boundaries sufficient to reproduce session VWAP.
- Rolling volume history for percentile/rank estimation.
- OHLC history sufficient for ATR and candle displacement.
- Source focus: liquid futures including ES, YM, MES, and MYM; the author suggests 3-minute, 5-minute, and 15-minute testing and particularly discusses 3-minute behavior.
- Point-in-time requirement: all percentile, ATR, VWAP, and candle features must use only information available by the decision timestamp.
- Missing-data/session-reset handling is not specified by the source.

## Execution assumptions

The source explicitly supports a next-bar entry option and same-bar exit protection, but the public description does not fully specify the default signal-to-order timing, order type, fill model, commissions, bid/ask spread, slippage, market impact, partial fills, leverage, margin, or latency. These must be treated as unspecified rather than silently filled in.

For crypto adaptation, funding and perpetual-contract mechanics would additionally be required if tested on perpetuals.

## Evidence

### Source-reported

The author states that recent ES and YM testing showed promising behavior in some windows/timeframes, while explicitly warning that performance changes with symbol, timeframe, session, risk settings, and regime. No precise performance statistic is retained here because the reviewed public description does not provide a traceable fixed-sample metric suitable for normalization.

The author describes the strategy as intended for liquid intraday futures, especially ES, YM, MES, and MYM, and suggests comparing 3-minute, 5-minute, and 15-minute charts.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source explicitly warns that Strategy Tester fills can differ from live fills, short backtest windows can fail over longer samples, apparently attractive profit factor can coexist with excessive drawdown, and the strategy is not fully live-validated. The author also states that results vary by symbol, timeframe, session, risk settings, and regime.

## Falsification plan

1. Reconstruct the source-described composite without inventing unspecified defaults; treat unresolved parameters as a bounded research grid.
2. Compare against simple controls: VWAP-distance mean reversion alone, volume-surprise alone, candle-body/ATR reversal alone, and a simple signed-return reversal conditioned on VWAP side.
3. Ablate the volume-percentile filter, displacement/ATR filter, and VWAP-location condition one at a time.
4. Test threshold stability rather than selecting a single best percentile/displacement pair; reject the mechanism if performance is concentrated in narrow parameter islands.
5. Use walk-forward/out-of-sample evaluation across multiple liquid instruments and volatility regimes, with long and short sides reported separately.
6. Apply realistic fees, spread/slippage, next-bar execution, and adverse fill sensitivity. Intraday mean reversion should be rejected if the edge disappears under plausible costs.
7. Test whether the composite adds stable OOS information beyond the simplest surviving control. If not, retain the simpler construction and reject the absorption-specific complexity.

## Crypto portability

adapted

The source evidence is from traditional intraday futures, not crypto. The economic hypothesis can be ported to liquid crypto markets, but 24/7 trading makes session VWAP anchoring non-unique; venue fragmentation and heterogeneous volume quality can change the percentile signal; perpetuals add funding, mark/index-price, and liquidation effects. Any UTC/session anchor used for crypto would be research-proposed and must be tested rather than presented as source evidence.

## Limitations

- Several operational parameters and exit-state details are underspecified in the public description.
- The interpretation of high volume plus low displacement as passive-liquidity absorption is a hypothesis, not direct observation of aggressor/passive order flow.
- Session VWAP introduces market-session dependence that does not transfer directly to 24/7 crypto.
- Source-reported favorable behavior is qualitative and sample-dependent.
- Not independently reproduced.

## Implementation status

Research record only. No implementation in the research stack and no Qlib full-backtest validation has been completed for this record.

## Adoption boundary

This artifact is research-only. Repository presence does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No verified related Wiki record is asserted in this GitHub-only Scout run. Conceptually related families include VWAP mean reversion, volume surprise, effort-versus-result/absorption hypotheses, and volatility-normalized reversal.

## Sources

- TradingView, `Post-Absorption VWAP Reversal Engine V1.6`, `secretmorina`: https://www.tradingview.com/script/j6iKZmCf-Post-Absorption-VWAP-Reversal-Engine-V1-6/ (reviewed 2026-09-25).
