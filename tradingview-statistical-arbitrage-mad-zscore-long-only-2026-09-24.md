---
schema: strategy-research-record-v1
title: TradingView robust MAD Z-score pairs mean reversion, long-side only
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
  - https://www.tradingview.com/script/Kt6XkQIM-Statistical-Arbitrage-Pairs-Trading-Long-Side-Only/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView robust MAD Z-score pairs mean reversion, long-side only

## Provenance

Public TradingView open-source strategy `Statistical Arbitrage Pairs Trading - Long-Side Only` by `piirsalu`, published 2025-01-30. Stable canonical source URL: https://www.tradingview.com/script/Kt6XkQIM-Statistical-Arbitrage-Pairs-Trading-Long-Side-Only/ . Source reviewed 2026-09-24.

The source page identifies the artifact as a TradingView Strategy with source code available publicly. This record normalizes the public description rather than redistributing the Pine source.

Repository deduplication on current `main` before creation found no record citing canonical TradingView script id `Kt6XkQIM`. Repository search does contain adjacent pairs/statistical-arbitrage research, including ADF-filtered pairs trading and other spread/z-score constructions, but not this source's specific combination of per-instrument normalization, spread construction, median/MAD robust standardization, and long-side-only execution.

## Economic mechanism

### Source-reported

The author describes a simplified statistical-arbitrage approach between two correlated instruments. Each instrument is normalized with a Z-score; the difference between the normalized series forms a spread. A modified Z-score based on the median and Median Absolute Deviation (MAD) is then used to identify unusually negative spread deviations. The stated thesis is that an extreme relative undervaluation of the main instrument versus its pair may mean-revert.

### Research interpretation

The falsifiable hypothesis is that a robustly standardized relative-price dislocation contains short-horizon mean-reversion information that survives outliers better than a conventional mean/standard-deviation spread Z-score.

The potentially distinctive component is not generic pairs trading itself, but the use of median/MAD robust scaling after forming a spread from two normalized price series. If that robust transformation adds no out-of-sample value relative to simpler spread constructions, it should be removed.

The source calls the approach statistical arbitrage, but the published TradingView implementation is long-side only. It therefore does not establish a market-neutral paired portfolio by itself. Treat the relative-value interpretation as a hypothesis, not as evidence of beta neutrality.

## Signal

Source-supported normalized logic:

1. Select the chart/main instrument and a second correlated instrument.
2. Normalize both price series using Z-scores.
3. Form a spread between the two normalized series.
4. Compute a modified Z-score of that spread using its median and Median Absolute Deviation to reduce sensitivity to outliers.
5. Enter a long position in the main instrument when the modified spread Z-score falls below a user-defined negative threshold. The source gives `-1.0` as an example threshold, not a universally validated value.
6. Close the long position when the spread Z-score returns to or above `0`.
7. Source-reported position sizing defaults to 10% of equity.

The public description does not unambiguously expose the normalization lookback, MAD lookback, exact modified-Z scaling constant, selected default pair, bar timeframe, signal-to-fill timing, re-entry behavior, or whether every displayed parameter is unchanged from the underlying Pine implementation. Those fields are `underspecified` and are not invented here.

`research-proposed`: evaluate the published long-only rule first without adding a short leg. A separately hedged two-leg implementation may be tested only as a distinct experimental variant because the source page does not establish its execution semantics.

## Required data

Source-supported requirements:

- synchronized price history for two instruments;
- chart/main instrument plus a user-selected pair instrument;
- enough trailing observations to compute each price Z-score, the resulting spread, its median, and MAD.

Underspecified by the public description:

- exact venue(s);
- exact asset universe and default pair;
- spot/futures/perpetual market type;
- timeframe;
- price field used for normalization;
- session alignment and timezone;
- stale/missing-bar handling across the two instruments;
- point-in-time treatment when one venue or instrument is unavailable.

For crypto portability, synchronized timestamps and venue-consistent prices are mandatory to avoid creating artificial spread moves from asynchronous candles.

## Execution assumptions

The source reports percentage-of-equity sizing with a default of 10%, and states that commissions and slippage are included in its backtesting setup. The public description does not expose enough detail here to reproduce the exact commission rate, slippage amount/model, order type, signal-to-order timing, fill convention, spread/impact assumptions, borrow, leverage, margin, partial fills, or failures.

The strategy is described as long-side only, so the source page does not establish executable hedge-leg mechanics. Do not infer a simultaneous short in the paired instrument from the statistical-arbitrage label.

`research-proposed`: any independent test should use next-eligible-bar execution unless inspection of a reproducible source implementation establishes a different causal timing rule, and should stress realistic fees/slippage for the tested venue. This is a proposed research convention, not source-reported behavior.

## Evidence

### Source-reported

The source states that the strategy uses median/MAD modified Z-score normalization to reduce outlier sensitivity, enters long below a user-defined negative threshold such as `-1.0`, exits at spread Z-score `>= 0`, sizes trades at a default 10% of equity, and includes commissions and slippage in backtesting.

No Sharpe ratio, CAGR, drawdown, win rate, sample interval, instrument pair, or other reproducible performance statistic is asserted in the public description reviewed here, so none is recorded as evidence.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source describes two correlated instruments but does not establish cointegration or spread stationarity. Correlation alone is insufficient to guarantee mean reversion.
- The TradingView strategy is long-side only; therefore a profitable result could contain directional beta rather than pure relative-value alpha.
- Normalizing each price series before differencing is not equivalent to estimating a hedge ratio or cointegrating residual. The economic meaning of the resulting spread must be tested rather than assumed.
- The public page does not expose enough execution and lookback detail to reproduce the source backtest exactly from the description alone.
- No independently verified performance evidence is available in this Scout cycle.

## Falsification plan

1. Reconstruct only parameters that can be traced to the source; treat unresolved defaults as an explicit implementation gap rather than optimizing them silently.
2. Test on economically related pairs and reject pairs whose relationship is selected using future information.
3. Compare the source construction against simpler controls: raw price ratio/log-price spread, OLS hedge-ratio residual, conventional mean/standard-deviation Z-score, and the same normalized-series spread without MAD scaling.
4. Ablate the robust layer: if median/MAD does not improve walk-forward net Sharpe, drawdown, or tail behavior consistently relative to standard scaling, reject the added robust-transformation complexity.
5. Test stationarity/relationship stability only with information available at formation time. Compare ungated and causally gated variants; do not retroactively retain only pairs that later mean-revert.
6. Separate long-only directional exposure from relative-value information by comparing against buy-and-hold/main-instrument and beta-matched controls.
7. Stress lookbacks and entry thresholds over broad neighborhoods rather than selecting a single best setting. Reject results that depend on a narrow threshold such as exactly `-1.0`.
8. Apply walk-forward/out-of-sample evaluation across multiple market regimes and include realistic fees, spread/slippage, and—if adapted to perpetuals—funding.
9. For any proposed two-leg version, account for both legs' costs, synchronized execution, hedge ratio, margin, funding/borrow, and legging risk. Do not attribute its results to the source's long-only implementation.
10. Materially weaken the hypothesis if the robust construction fails to outperform the simpler controls net of costs across OOS windows, if spread stationarity is unstable, or if apparent performance disappears after controlling for main-instrument directional beta.

## Crypto portability

`adapted`

The source page does not demonstrate this strategy specifically on crypto, so it is not direct crypto empirical evidence. The relative-value mechanism can be adapted to crypto pairs, but requires additional controls for 24/7 trading, venue fragmentation, synchronized candle boundaries, changing pair relationships, stablecoin quote effects, and—when using perpetuals—funding, mark/index conventions, leverage, liquidation and cross-venue basis differences.

A crypto test should prefer economically defensible pair relationships and must not select pairs retrospectively from realized correlation or profitability.

## Limitations

- `underspecified`: normalization and MAD lookbacks, exact robust-scaling formula/constant, timeframe, default pair, price field, and detailed execution semantics are not fully exposed in the reviewed public description.
- `not independently reproduced`: no source backtest or signal path was reproduced during this Scout cycle.
- `unproven`: the source's robust transformation has not been shown here to add incremental OOS alpha over conventional pairs controls.
- The label `statistical arbitrage` should not be read as proof of market neutrality or cointegration.
- Long-only execution can confound relative-value signal quality with directional market exposure.

## Implementation status

Research record only. No implementation in the research stack and no Qlib full backtest was performed by this Scout.

## Adoption boundary

This artifact is `research-only`, `not-implemented`, and `not-approved`. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor/leaderboard entry, or received Paper, Testnet, or Live approval.

## Related Wiki records

No stable Hermes Wiki Brain link was established during this GitHub-only Scout cycle. No Wiki link is fabricated.

## Sources

- TradingView, `Statistical Arbitrage Pairs Trading - Long-Side Only`, author `piirsalu`, published 2025-01-30, reviewed 2026-09-24: https://www.tradingview.com/script/Kt6XkQIM-Statistical-Arbitrage-Pairs-Trading-Long-Side-Only/
