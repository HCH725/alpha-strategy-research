---
schema: strategy-research-record-v1
title: "TradingView SuperTrend Regime Confluence"
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-13
sources:
  - "https://in.tradingview.com/script/mpjNqADq-SuperTrend-Regime-Confluence/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView SuperTrend Regime Confluence

## Provenance

- Public TradingView open-source strategy: **SuperTrend Regime Confluence**, author **DefinedEdge**.
- Stable source: https://in.tradingview.com/script/mpjNqADq-SuperTrend-Regime-Confluence/
- TradingView canonical script identity: `mpjNqADq`.
- Publication shown by TradingView: **Sep 13, 2026**; source reviewed as of 2026-09-27.
- The source page exposes a normalized description and identifies the script as open source. This record summarizes the public description rather than redistributing Pine source code.
- Repository dedup before write found no `mpjNqADq`, exact title, or author match on current `main`. A broader SuperTrend/regime/confluence search produced one unrelated record; no materially identical normalized signal was identified.

## Economic mechanism

### Source-reported

The author describes a trend-following system intended to address two weaknesses of a fixed-parameter SuperTrend: ATR bands can be too tight in volatile conditions and too wide in quiet conditions, while unconditional flips can whipsaw in ranges.

Three components are combined:

1. an ADX plus ATR-ratio regime classifier labels bars Trending, Volatile, or Ranging and changes the SuperTrend multiplier by regime;
2. the strategy can suppress entries in the Ranging regime;
3. each SuperTrend flip receives a deterministic 0–100 confluence score based on volume surge, displacement beyond the band, trend alignment, regime quality, and prior distance from the band.

Only flips above the configured minimum score are eligible.

### Research interpretation

Falsifiable hypothesis: **SuperTrend directional flips contain more persistent trend information when the volatility band adapts to observable market regime and when the flip is accompanied by displacement, participation, trend alignment, and favorable pre-flip structure.**

Component roles:

- Regime: ADX + ATR-ratio classifier.
- Primary signal: volatility-adaptive SuperTrend direction flip.
- Confirmation: deterministic five-factor confluence score.
- Optional filters: EMA alignment, volume filter, ranging-regime exclusion, cooldown.
- Risk / exit: selectable stop and take-profit logic; these are risk/execution components rather than evidence that the entry signal itself has alpha.

Ablation is essential because the source does not establish that every component contributes incremental predictive value.

## Signal

Source-described default configuration:

- Instrument / timeframe shown: BTCUSDT, 4H.
- ATR length: 10.
- Base SuperTrend multiplier: 3.
- Regime lookback: 40.
- ADX length: 14.
- ADX threshold: 20.
- Trend EMA: 50.
- Minimum confluence score: 65.
- Entry cooldown: 5 bars.
- Risk per trade: 6% of equity.
- ATR stop: 6x.
- Risk:reward target: 2.5.

Formation logic:

1. Classify the current bar as Trending, Volatile, or Ranging using ADX and ATR-ratio logic.
2. Adapt the SuperTrend multiplier to the classified regime; the public description states that Volatile widens the multiplier and Ranging tightens it.
3. Detect a SuperTrend direction flip.
4. Score the candidate from 0 to 100:
   - volume surge: 0–20;
   - displacement beyond the band in ATR units: 0–25;
   - direction versus longer EMA: 0–20;
   - regime quality: 0–15;
   - prior distance from the band: 0–20.
5. Require the score to clear the configured threshold; optional ranging-regime, EMA, volume, cooldown, and long/short gates may further restrict entry.
6. Exits are configurable: ATR, percent, or SuperTrend-flip stop; Risk:Reward, percent, or no take-profit.

**Underspecified from the reviewed public description:** exact ATR-ratio regime formula and thresholds, regime-specific multiplier mapping, exact sub-score formulas/thresholds, exact SuperTrend band update algebra, whether score comparison is strictly greater-than or greater-than-or-equal, signal-to-order timing, same-bar versus next-bar fills, re-entry/pyramiding semantics, and the exact optional-filter defaults beyond those explicitly listed above. These must not be inferred.

## Required data

- BTCUSDT for the source-shown configuration.
- 4H OHLCV.
- High, low, close for ATR/SuperTrend construction.
- Volume for the volume-surge score/filter.
- Sufficient history for ATR(10), regime lookback 40, ADX(14), EMA(50), plus any internal score lookbacks not disclosed in the public description.
- Timestamped bars with a stable candle-boundary convention.

Venue, spot-versus-perpetual market type, quote-source details, timezone/candle boundary, missing-bar policy, and point-in-time venue availability are **data gaps** in the reviewed description.

## Execution assumptions

Source-reported defaults include commission **0.06%** and slippage **2 ticks**. Risk-based sizing targets 6% equity risk per trade in the shown setup, and the author states position size is capped at 90% of equity with no leverage.

The public description does not specify order type, exact signal-to-fill timing, spread model beyond the stated commission/slippage assumptions, market impact, capacity, partial fills, failed orders, latency, funding, borrow, margin treatment, tick-size source, or whether the shown BTCUSDT is spot or perpetual. These are **underspecified/data gap**, not zero.

## Evidence

### Source-reported

For BTCUSDT 4H, Jan 2020 through Sep 2026, with the displayed defaults, the TradingView page reports:

- return: +824%;
- maximum drawdown: 24.55%;
- profit factor: 1.80;
- win rate: 46.4%;
- trades: 168;
- commission: 0.06%;
- slippage: 2 ticks.

These are source-reported TradingView backtest claims on one instrument/configuration and are not independently verified here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source itself warns that trend-following can suffer drawdowns and losing streaks in extended sideways conditions.
- The displayed result is a single-instrument historical backtest.
- No independent out-of-sample or walk-forward evidence is presented in the reviewed description.
- The adaptive regime mapping and confluence sub-score formulas are not fully reconstructable from the public prose alone.
- The number of interacting filters and parameters creates material selection/overfitting risk.
- None identified beyond the above in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

All thresholds below are **research-proposed**, not source claims.

1. **Frozen reconstruction gate:** reconstruct only after exact Pine semantics are available; reject implementation if regime mapping or score components cannot be reproduced without guessing.
2. **Baseline ablation:** compare the complete rule against a fixed-multiplier SuperTrend using the same ATR length and execution model. The adaptive thesis weakens materially if the full model fails to improve out-of-sample Sharpe by at least 0.20 or reduce whipsaw/trade-cost drag.
3. **Component ablation:** remove, one at a time, regime adaptation, ranging-regime exclusion, volume score, displacement score, EMA alignment, regime-quality score, and prior-distance score. Require evidence that complexity adds incremental value rather than merely reducing trade count.
4. **Frozen out-of-sample test:** freeze parameters before a later sample; reject the claimed edge if net performance is non-positive or materially worse than the simple SuperTrend baseline.
5. **Cost sensitivity:** test at the source's 0.06% commission / 2-tick slippage and at harsher fee/slippage assumptions; reject practical portability if modest cost increases erase the incremental edge.
6. **Regime stability:** separately evaluate trending, volatile, and ranging periods; falsify the regime-classification thesis if the adaptive mapping does not improve the environment it is intended to address.
7. **Parameter fragility:** perturb ATR length, base multiplier, regime lookback, ADX threshold, EMA length, and score threshold around defaults. A narrow isolated optimum is evidence against robustness.
8. **No-lookahead audit:** verify all regime, score, ATR, EMA, and flip inputs are available at the actual signal timestamp and that TradingView execution semantics are reproduced causally.

Failure should retain this record as research-only and prevent promotion of the failed hypothesis.

## Crypto portability

**direct** for the source-shown BTCUSDT hypothesis, but venue/contract implementation remains underspecified.

The source explicitly demonstrates the strategy on BTCUSDT 4H, so the hypothesis is directly crypto-oriented rather than ported from another asset class. However, the reviewed page does not state whether the symbol is spot or perpetual, which venue supplies it, or how funding, mark/index price, liquidation, 24/7 candle boundaries, venue fragmentation, and contract specification should be handled. Those are material implementation gaps.

## Limitations

- `underspecified`: exact regime classifier and regime-to-multiplier mapping.
- `underspecified`: exact five sub-score formulas and thresholds.
- `underspecified`: fill timing, order type, re-entry and pyramiding semantics.
- `data gap`: venue and spot/perpetual identity.
- `data gap`: funding, spread, impact, capacity, latency, partial fills and failures.
- `not independently reproduced`: all reported performance.
- Single instrument and one displayed configuration.
- Multi-component parameterization creates overfitting and multiple-testing risk.
- Source publication is recent relative to the reported historical test, so forward evidence is limited.

## Implementation status

`implementation_status: not-implemented`.

No implementation or Qlib full backtest was performed in this Scout cycle. No runtime code was changed.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence in this repository does not mean this strategy passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, is profitable or validated alpha, or is approved for Paper, Testnet, or Live trading.

## Related Wiki records

No stable related Hermes Wiki Brain record was resolved from the GitHub-only contract. No Wiki link is fabricated.

## Sources

- TradingView, DefinedEdge, **SuperTrend Regime Confluence**, public open-source strategy, published Sep 13, 2026: https://in.tradingview.com/script/mpjNqADq-SuperTrend-Regime-Confluence/ — reviewed 2026-09-27. The source supplies the mechanism description, component weights, displayed defaults, execution-cost defaults, and source-reported backtest figures summarized above.
