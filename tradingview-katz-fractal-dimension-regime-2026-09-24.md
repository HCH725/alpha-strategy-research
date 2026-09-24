---
schema: strategy-research-record-v1
title: TradingView Katz fractal-dimension path-complexity regime filter
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
  - https://www.tradingview.com/script/ifcOGobE-Fractal-Dimension-Katz-Quant-Lab/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Katz fractal-dimension path-complexity regime filter

## Provenance

- Public TradingView open-source script: **Fractal Dimension (Katz, Quant Lab)**.
- Author/page identity: **akmans**.
- Published: **2025-12-11** according to the public TradingView page.
- Stable TradingView URL: https://www.tradingview.com/script/ifcOGobE-Fractal-Dimension-Katz-Quant-Lab/
- Source reviewed as of **2026-09-24**.
- This record normalizes the public description; it does not redistribute the Pine source.

## Economic mechanism

### Source-reported

The source estimates the Katz Fractal Dimension of price over a rolling window. It interprets lower dimension as a smoother, more directional path and higher dimension as a noisier/choppier or range-like path. The stated bands are approximately 1.0–1.3 for strong directional trend, 1.3–1.5 for mixed/transitional behavior, and 1.5–2.0 for noisy/choppy/mean-reverting or range behavior.

### Research interpretation

The falsifiable hypothesis is that **Katz path geometry contains incremental point-in-time regime information for a fixed directional or mean-reversion baseline beyond simpler path-efficiency, volatility, and trend-strength controls**. The proposed mechanism is not that fractal dimension predicts direction; rather, recent path tortuosity may identify environments in which continuation versus reversal rules have different conditional expectancy.

Because Katz FD is closely related conceptually to path efficiency, its value must be tested directly against simpler controls such as Kaufman Efficiency Ratio rather than assumed from geometric terminology.

Any trading rule derived from the regime is **research-proposed** unless explicitly described as source-reported.

## Signal

### Source-reported construction

For a rolling window, the source states:

- `L` = sum of absolute price changes within the window;
- `d` = maximum distance between any point and the first point in the window;
- `n` = window length;
- `FDI = ln(n) / (ln(n) + ln(d / L))`.

Source-reported interpretation bands:

- FDI about 1.0–1.3: strong directional trend / low randomness;
- FDI about 1.3–1.5: mixed or transitional behavior;
- FDI about 1.5–2.0: noisy, choppy, mean-reverting or range behavior.

### Underspecified by the public description

The reviewed public description does not unambiguously state the default rolling-window length, exact price field, warm-up behavior, zero-range handling, bar-close versus intrabar state semantics, entry/exit rules, holding period, re-entry logic, sizing, or execution timing. These are not inferred.

### Research-proposed operationalization for falsification only

A future test may freeze one simple directional baseline and one simple mean-reversion baseline, calculate Katz FD using only information available through each completed bar, and condition those baselines on predeclared FD bands. This is **research-proposed** and is not attributed to the source author.

## Required data

- Timestamped OHLC bars; exact source price field is **underspecified** by the reviewed description.
- Rolling historical prices sufficient for the selected Katz window.
- No volume, funding, open interest, order book, trade-side, or options data are required by the described core estimator.
- Instrument/universe and venue are not constrained by the public description.
- Point-in-time requirement: all path-length and maximum-distance calculations at time `t` must use only observations available through `t`.
- Crypto tests must define candle boundaries and price source consistently across venues.

## Execution assumptions

The source is an indicator, not a complete executable strategy. It does not specify signal-to-order timing, market versus limit execution, fills, fees, spread, slippage, impact/capacity, funding, leverage/margin, borrow/shorting, latency, or partial-fill/failure handling. Any future backtest must define these independently.

## Evidence

### Source-reported

The public page explains the estimator and qualitative regime interpretation but provides no traceable Sharpe, CAGR, win rate, drawdown, t-statistic, transaction-cost result, sample window, or other profitability evidence.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source provides a regime interpretation, not evidence that Katz FD predicts future returns.
- The indicator is directionless: low FD can describe either an uptrend or a downtrend.
- The public description does not provide empirical validation of the stated regime bands.
- The estimator can be mechanically related to simpler measures of net displacement versus path length; apparent incremental information may disappear against Kaufman Efficiency Ratio or related controls.
- Window length and price-field choices are underspecified and may materially affect classification.
- No source-reported transaction-cost or trading-performance evidence was identified.
- No additional negative empirical result was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

All portfolio mappings and rejection thresholds below are **research-proposed**.

1. **Reconstruct first.** Implement the stated Katz formula point-in-time and explicitly freeze window, price field, warm-up, and degenerate-window handling before return tests.
2. **Complexity baseline.** Compare Katz FD with Kaufman Efficiency Ratio, normalized absolute displacement/path length, realized volatility, ATR-normalized range, ADX, and a simple Choppiness-style measure.
3. **Incremental-information test.** Keep the underlying directional/reversal rules fixed. Katz conditioning survives only if it adds stable OOS information beyond the simpler controls rather than merely relabeling path efficiency.
4. **Band ablation.** Compare the source-reported qualitative bands with continuous FD, a simple 1.5 split, and training-only quantile thresholds. Reject any claim that the three-band construction is necessary if simpler mappings perform equivalently.
5. **Direction separation.** Test trend direction independently from FD so the directional rule's alpha is not misattributed to a directionless regime estimator.
6. **Cross-asset/timeframe robustness.** Freeze parameters before OOS evaluation across liquid crypto assets and multiple bar horizons; report null and negative cohorts.
7. **Costs.** Apply realistic fees, spread/slippage, and perpetual funding where applicable. Reject economic usefulness if conditioning only helps gross results that disappear net of costs.
8. **Failure action.** If Katz FD does not add robust OOS value beyond KER/path-efficiency and simple volatility/trend controls, reject the Katz layer rather than adding further filters.

## Crypto portability

**unproven**

The estimator itself requires only price history and is mechanically portable to crypto, but the reviewed source provides no crypto-specific validation. Crypto evaluation must account for 24/7 candle boundaries, venue fragmentation, spot versus perpetual price construction, mark/index versus traded prices where relevant, thin-token noise, and funding for perpetual positions.

## Limitations

- **underspecified:** rolling-window default, price field, warm-up/degenerate handling, state-transition timing, and complete trading lifecycle.
- **not independently reproduced:** no implementation or backtest was run during this Scout cycle.
- **data gap:** no source-reported performance sample, cost model, or crypto validation.
- **unproven:** incremental information beyond simpler path-efficiency and volatility/trend measures.
- Qualitative labels such as “mean-reverting” should not be upgraded into return forecasts without independent evidence.

## Implementation status

`not-implemented`. This is normalized research material only. No Qlib implementation, full backtest, survivor promotion, Paper, Testnet, or Live validation was performed.

## Adoption boundary

`research-only / not-approved`.

Presence in this repository does not mean this hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, is profitable or validated alpha, or is approved for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — schema reference exposed by the repository README. No Wiki read or write was performed in this GitHub-only cycle.
- Repository-adjacent research includes Kaufman efficiency-ratio percentile gating, DFA/Hurst significance regimes, variance-ratio regimes, and entropy-based regime classifiers. Katz FD is retained only as a materially distinct path-geometry estimator whose incremental value must be tested against those simpler or alternative constructions.

## Sources

- TradingView, akmans, **Fractal Dimension (Katz, Quant Lab)**, public open-source script, published 2025-12-11, reviewed 2026-09-24: https://www.tradingview.com/script/ifcOGobE-Fractal-Dimension-Katz-Quant-Lab/
