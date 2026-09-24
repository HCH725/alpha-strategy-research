---
schema: strategy-research-record-v1
title: TradingView Sample Entropy Adaptive-EMA Regime
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
  - https://www.tradingview.com/script/1ZBMuq8g-Sample-Entropy-SampEn-Regime-Detector/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Sample Entropy Adaptive-EMA Regime

## Provenance

Public TradingView open-source script: **Sample Entropy (SampEn) Regime Detector**, author/page identity `GospodarValovaHR`, published 2026-03-21 according to the public TradingView page. Stable source URL: https://www.tradingview.com/script/1ZBMuq8g-Sample-Entropy-SampEn-Regime-Detector/. Source reviewed as of 2026-09-24.

The public description is sufficient to identify the hypothesis and major component roles, but it does not expose enough parameter detail in the reviewed page text to reconstruct the exact estimator and adaptive-EMA mapping. Those gaps are preserved rather than inferred.

## Economic mechanism

### Source-reported

The source describes Sample Entropy (SampEn) as a rolling measure of price-action regularity versus unpredictability. Low SampEn is interpreted as a structured regime in which conventional directional or mean-reversion tools may operate more cleanly; high SampEn is interpreted as noisy/choppy behavior. The source also describes an adaptive EMA whose responsiveness changes with entropy: faster tracking in more predictable conditions and slower tracking in chaotic conditions. It suggests using the entropy state as a regime filter, and reports a SampEn score above 2.0 as a high-noise condition in which risk may be reduced.

### Research interpretation

The falsifiable hypothesis is not that entropy itself predicts direction. It is that **rolling sample entropy contains incremental information about the conditional reliability of simple trading signals**, beyond ordinary volatility, trend-efficiency, and path-complexity controls. A secondary hypothesis is that entropy-conditioned EMA responsiveness improves a simple moving-average baseline after costs without merely reproducing a volatility-adaptive smoother.

This is materially distinct from ordinal/permutation entropy: SampEn measures recurrence/similarity of embedded sequences within a tolerance, whereas permutation entropy operates on ordinal-pattern frequencies. The distinction must survive empirical ablation to justify the extra estimator.

## Signal

Source-supported components:

- Input: rolling price action; exact price field is underspecified in the reviewed public description.
- Regime statistic: Sample Entropy over a rolling window.
- Low SampEn: structured/predictable regime.
- High SampEn: chaotic/choppy regime.
- Source-reported risk reference: SampEn score above `2.0` is described as high noise.
- Adaptive EMA: responsiveness changes with entropy, tightening in predictable regimes and slowing in chaotic regimes.
- Source-reported usage includes regime filtering and interpreting a sharp entropy decline from high to low as possible breakout confirmation.

Underspecified by the reviewed source page:

- rolling window length;
- embedding dimension `m`;
- tolerance `r` and whether it is absolute or scale-normalized;
- distance metric and exact SampEn implementation;
- exact low/neutral/high regime thresholds other than the separately mentioned `2.0` risk reference;
- exact entropy-to-EMA smoothing transformation;
- entry, short-entry, exit, holding period, re-entry, sizing, and complete position-state logic.

Research-proposed operationalization for later testing only: compare a fixed directional baseline under no gate, a low-SampEn gate, and an entropy-adaptive EMA. Parameter grids must be defined ex ante from past-only data; no specific missing source parameter is asserted here.

## Required data

At minimum, timestamped OHLC price bars sufficient to construct the source price series and rolling entropy state. Volume, funding, order book, trades, aggressor side, open interest, and options data are not source-required by the reviewed description.

For crypto testing, bar boundaries, venue, spot/perpetual market type, missing-bar handling, and point-in-time availability must be fixed before evaluation. All rolling statistics must use information available at or before the signal timestamp.

## Execution assumptions

The source page does not specify signal-to-order timing, same-bar versus next-bar fills, market versus limit orders, fees, spread, slippage, impact/capacity, leverage/margin, funding, borrow/short mechanics, latency, partial fills, or failure handling. All are data gaps.

Any later test should use closed-bar signal formation and next-bar execution as a **research-proposed** anti-look-ahead convention unless a more appropriate point-in-time convention is specified before testing. This is not claimed to be the source implementation.

## Evidence

### Source-reported

The TradingView page describes low SampEn as regular/structured, high SampEn as random/choppy, and the adaptive EMA as changing responsiveness with entropy. It also gives `2.0` as a high-noise risk reference and describes a sharp entropy decline as possible breakout confirmation.

No source-reported Sharpe, CAGR, drawdown, win rate, statistically validated alpha, or independently auditable backtest result was identified in the reviewed public page text.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The public description does not establish that low entropy predicts direction; a regular process can represent either trend or orderly mean reversion. The exact SampEn estimator and adaptive-EMA mapping are underspecified in the reviewed page text. The `2.0` risk reference is not accompanied there by a documented cross-market calibration or statistical significance test. No independently verified performance evidence was identified. Absence of additional negative results in the reviewed source is not evidence that none exist.

## Falsification plan

Use liquid crypto spot and perpetual series across multiple assets, timeframes, and volatility regimes with strictly past-only rolling calculations and chronological out-of-sample evaluation.

Primary complexity ladder:

1. directional baseline with no regime gate;
2. baseline + realized-volatility gate;
3. baseline + Kaufman/path-efficiency control;
4. baseline + permutation-entropy regime;
5. baseline + SampEn regime;
6. baseline + SampEn-conditioned adaptive EMA.

Ablate the SampEn regime and adaptive smoothing separately. Test whether SampEn contributes incremental OOS information after controlling for realized volatility, ATR/range compression, absolute returns, Kaufman efficiency ratio, and a simpler entropy estimator. Compare fixed versus past-only calibrated thresholds and require parameter stability across assets/timeframes rather than selecting one favorable cell.

Reject or materially weaken the hypothesis if SampEn does not improve a predeclared OOS metric versus the simpler controls after realistic fees/spread/slippage, if the improvement disappears outside one asset/timeframe, if the adaptive EMA adds no value beyond a volatility-adaptive EMA, or if reasonable changes in `m`, `r`, or lookback reverse the result. Multiple-testing correction should be applied to parameter searches.

## Crypto portability

**unproven**

The source is presented as a general TradingView indicator rather than crypto-specific empirical evidence. The statistic can be computed from crypto bars, but portability must account for 24/7 trading, venue fragmentation, perpetual funding, mark/index versus trade prices, variable liquidity, exchange-specific candle boundaries, and repeated/equal prices in illiquid series. Spot and perpetual results should not be conflated.

## Limitations

- Exact SampEn implementation: **underspecified**.
- Window, embedding dimension, tolerance and most thresholds: **underspecified**.
- Adaptive-EMA transformation: **underspecified**.
- Trading lifecycle and execution model: **underspecified**.
- Crypto evidence: **unproven**.
- Performance: **not independently reproduced**.
- Any later parameterization absent from the source must be labeled **research-proposed**.

## Implementation status

Not implemented in the research stack. No Qlib full backtest, survivor promotion, leaderboard entry, Paper, Testnet, or Live validation is implied.

## Adoption boundary

Research-only. Presence in this repository does not mean the hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor, demonstrated profitability, or received implementation/Paper/Testnet/Live approval.

## Related Wiki records

No Wiki Brain lookup or write was performed because this Scout is GitHub-only. No Wiki relationship is asserted. Repository-level family comparisons for later research include permutation entropy, path-efficiency/Kaufman, fractal-dimension, and other regime classifiers, but those are not adoption evidence.

## Sources

- TradingView — GospodarValovaHR, **Sample Entropy (SampEn) Regime Detector** (public open-source script; published 2026-03-21; reviewed 2026-09-24): https://www.tradingview.com/script/1ZBMuq8g-Sample-Entropy-SampEn-Regime-Detector/
