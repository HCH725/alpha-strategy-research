---
schema: strategy-research-record-v1
title: TradingView Kaufman efficiency-ratio percentile-hysteresis regime filter
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
  - https://www.tradingview.com/script/2Ghnhfqg-Kaufman-Efficiency-Ratio-Gate-NovaLens/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Kaufman efficiency-ratio percentile-hysteresis regime filter

## Provenance

- Public TradingView open-source script: **Kaufman Efficiency Ratio Gate [NovaLens]**.
- Author/page identity: **NovaLens**.
- Stable TradingView URL: https://www.tradingview.com/script/2Ghnhfqg-Kaufman-Efficiency-Ratio-Gate-NovaLens/
- TradingView page displays publication label **Apr 16**; the fetched public page does not display a year next to that label, so no year is inferred here.
- Source reviewed as of **2026-09-24**.
- The public description was normalized rather than copying Pine source code.

## Economic mechanism

### Source-reported

The source treats Kaufman's Efficiency Ratio (KER) as a directionless measure of how efficiently price converts gross path movement into net displacement. It then smooths KER, percentile-ranks it against its own recent history, and applies symmetric hysteresis around the median to classify the current environment as trend-favorable or chop-dominant. The stated rationale is that percentile normalization adapts the threshold to each asset/timeframe, while hysteresis reduces state flicker.

The source explicitly says the gate is backward-looking and directionless: it is a regime filter, not a forward predictor or standalone buy/sell signal.

### Research interpretation

The falsifiable hypothesis is that **trailing percentile normalization plus hysteresis applied to path efficiency provides incremental out-of-sample regime-conditioning value for simple directional strategies beyond raw KER, fixed KER thresholds, realized volatility, ADX, and Choppiness Index-type controls**.

The economic/behavioral mechanism is trend persistence conditional on unusually efficient recent price paths: when net displacement is large relative to cumulative absolute movement, directional rules may face less whipsaw. The percentile and hysteresis layers are engineering transformations whose incremental value must be demonstrated rather than assumed.

Any portfolio allocation, entry, exit, or sizing rule built from this gate is **research-proposed** unless explicitly described below as source-reported.

## Signal

### Source-reported construction

- Raw Efficiency Ratio: `ER = |Close - Close(N)| / sum(|Close(i) - Close(i-1)|)` over the selected KER period.
- Light EMA smoothing is applied to raw KER.
- The smoothed KER is percentile-ranked within a trailing rank window.
- Binary gate uses symmetric hysteresis around the 50th percentile: open above `50 + Stability/2`, close below `50 - Stability/2`.
- Gate open = trend-favorable; gate closed = chop-dominant.
- The source also displays strengthening/weakening/stable momentum of the rank, but does not present that readout as the core binary gate.

Source-reported presets:

- Weekly: KER 10, smoothing 2, rank window 100, stability 2.
- Daily: KER 8, smoothing 2, rank window 50, stability 2.
- 8H: KER 8, smoothing 2, rank window 50, stability 2.
- 4H: KER 14, smoothing 2, rank window 30, stability 2.
- 30m: KER 5, smoothing 5, rank window 30, stability 2.

The source states that bright trend/chop display states correspond to the top/bottom 25% of the recent rank window. These are display/context states and are not treated here as standalone trading entries.

### Source-reported usage, not a complete strategy

The source suggests using gate-open as context for pullbacks, breakouts, moving-average crosses, higher-timeframe confirmation, or regime-aware sizing. It does not prescribe one canonical directional rule. Direction must come from a separate signal.

### Underspecified by the public description

The reviewed public description does not unambiguously specify bar-close versus intrabar state-transition semantics, percentile tie handling, warm-up implementation, exact momentum-readout lookback, canonical entry/exit/holding lifecycle, position sizing, or order timing. These fields must not be invented.

### Research-proposed operationalization for falsification only

A future test may pair the binary gate with one predeclared simple trend baseline such as a Donchian breakout or moving-average direction, execute only from information known at bar close, and compare ungated versus gated performance. This mapping is **research-proposed** and is not attributed to NovaLens.

## Required data

- Timestamped OHLC bars; the core source-reported KER construction requires close prices.
- No volume, funding, open interest, order book, trades, or options data are required by the core gate.
- Instrument/universe: source presents the gate as cross-asset; it notes tuning on gold (`XAUUSD`) and says presets generalize reasonably, while recommending validation on each instrument.
- Timeframes: source provides Weekly, Daily, 8H, 4H, and 30m presets plus Custom.
- Point-in-time requirement: KER, EMA smoothing, percentile rank, and hysteresis state at time `t` must use only observations available through `t`.
- Warm-up/history requirement: the source warns the first roughly 50-100 bars may have unstable percentile ranks depending on preset.

## Execution assumptions

The source is a regime indicator, not a complete trading strategy. It does not specify same-bar versus next-bar execution, market versus limit orders, fill model, fees, spread, slippage, impact/capacity, funding, leverage/margin, borrow/shorting, latency, or partial-fill/failure handling. Any future backtest must define these independently.

## Evidence

### Source-reported

- The source states the indicator was cross-validated against a PyneCore Python reference implementation.
- It states parameters were tuned on gold (`XAUUSD`) through the NovaLens research pipeline and that the presets generalize reasonably to other assets, while recommending instrument-specific testing.
- No traceable Sharpe, CAGR, win rate, drawdown, t-statistic, sample dates, or other profitability statistics are reported on the reviewed public page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source itself states the gate is backward-looking and not a forward predictor.
- The gate is directionless; efficient downtrends and uptrends both produce gate-open states.
- The source warns that regime changes around news can occur faster than the rank window adapts.
- Short KER periods may be noisy on thin instruments.
- The source discloses that parameters were tuned on gold, creating a direct portability/selection concern for crypto and other markets.
- Percentile normalization and hysteresis may add no predictive information beyond raw path efficiency; they may only stabilize presentation.
- No source-reported trading-performance evidence was identified on the reviewed page.
- No additional negative empirical result was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

All portfolio mappings and rejection thresholds below are **research-proposed** unless explicitly source-reported above.

1. **Reconstruct first.** Independently reproduce raw KER, EMA smoothing, trailing percentile rank, hysteresis state, warm-up behavior, and bar-close transitions. Resolve percentile tie semantics before return testing.
2. **Complexity ladder.** Compare the same directional baseline under: no regime gate; raw KER; fixed KER threshold; KER percentile rank without hysteresis; KER percentile rank plus hysteresis. The percentile/hysteresis construction survives only if it adds stable out-of-sample value beyond simpler KER variants.
3. **Alternative regime controls.** Compare against realized volatility, ATR-normalized path measures, ADX, and Choppiness Index-style controls. Reject claims of incremental regime information if KER rank does not improve the predeclared baseline after controlling for these simpler measures.
4. **Preset portability.** Freeze source-reported presets before testing and evaluate across liquid crypto assets and the corresponding timeframes. Do not retune each asset on the full sample. Reject broad portability if gains are concentrated in a narrow asset/timeframe island.
5. **Gold-tuning concern.** Treat the disclosed XAUUSD tuning as source-selection evidence, not crypto validation. Use untouched crypto OOS windows and report null/negative cohorts alongside positive ones.
6. **Direction separation.** Keep the directional rule fixed while changing only the regime layer. This prevents attributing the baseline trend signal's alpha to the directionless KER gate.
7. **Costs and turnover.** Apply realistic fees, spread/slippage, and perpetual funding where applicable. Hysteresis should be tested for whether it actually reduces state turnover enough to matter economically.
8. **Ablate hysteresis.** If hysteresis merely delays exits/entries without improving net OOS performance or state stability, remove it rather than adding further filters.
9. **Failure action.** If percentile normalization and hysteresis do not show incremental OOS value over raw/fixed-threshold KER and simple controls, reject the extra layers and retain the simpler comparator for any future research.

## Crypto portability

**unproven**

The source says the gate can be used across assets and explicitly mentions a volatile altcoin as an example of why raw KER levels differ, but the reviewed page does not provide crypto-specific empirical validation. Crypto tests must account for 24/7 candle boundaries, venue fragmentation, thin-token noise, spot-versus-perpetual construction, mark/index versus traded prices where relevant, and funding for perpetual positions. Source presets should be treated as hypotheses, not crypto-calibrated truths.

## Limitations

- **underspecified:** exact percentile tie handling, warm-up implementation, bar-close/intrabar transition semantics, momentum-readout details, and complete trading lifecycle are not unambiguously specified in the reviewed description.
- **not independently reproduced:** no independent implementation or backtest was run during this Scout cycle.
- **data gap:** no source-reported sample dates, crypto performance statistics, transaction-cost model, or full strategy lifecycle are provided.
- **selection risk:** source parameters were tuned on XAUUSD.
- **unproven:** incremental alpha from percentile normalization and hysteresis beyond raw KER and simpler regime controls has not been established.

## Implementation status

`not-implemented`. This record is normalized research material only. No Qlib implementation, full backtest, survivor promotion, Paper, Testnet, or Live validation was performed.

## Adoption boundary

`research-only / not-approved`.

Presence in this repository does not mean this hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, is profitable or validated alpha, or is approved for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — schema reference exposed by the repository README. No Wiki read or write was performed in this GitHub-only cycle.
- Repository-adjacent research includes permutation-entropy regime ranking, variance-ratio regimes, DFA/Hurst regimes, and composite indicators containing Kaufman-style efficiency. Those are materially different constructions from this source's single-feature KER → smoothing → trailing percentile rank → hysteresis gate.

## Sources

- TradingView, NovaLens, **Kaufman Efficiency Ratio Gate [NovaLens]** (public open-source script page), reviewed 2026-09-24: https://www.tradingview.com/script/2Ghnhfqg-Kaufman-Efficiency-Ratio-Gate-NovaLens/
