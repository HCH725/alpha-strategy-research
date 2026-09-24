---
schema: strategy-research-record-v1
title: TradingView two-scale Higuchi fractal-dimension gated SMA-cross trend strategy
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
  - https://www.tradingview.com/script/iJGW4b97-Higuchi-Fractal-Dimension-forexobroker/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView two-scale Higuchi fractal-dimension gated SMA-cross trend strategy

## Provenance

- Public TradingView open-source script: **Higuchi Fractal Dimension [forexobroker]**.
- Author/page identity: **forexobroker**.
- Published: **2026-05-12** according to the public TradingView page.
- Stable TradingView URL: https://www.tradingview.com/script/iJGW4b97-Higuchi-Fractal-Dimension-forexobroker/
- Source reviewed as of **2026-09-24**.
- This record normalizes the public description and does not redistribute the Pine source.

## Economic mechanism

### Source-reported

The source uses a simplified two-scale Higuchi-style fractal-dimension estimator to distinguish smoother price paths from jagged/random paths. It interprets fractal dimension closer to 1 as smoother/trending and closer to 2 as more jagged/random. A smooth-regime gate is then combined with an SMA directional/crossover rule. The source states that buy signals require the smooth regime, price above the trend SMA, an upward SMA cross, no existing long state, a completed cooldown, and a confirmed bar; sell logic is the corresponding smooth-regime condition with price below the SMA and a downward cross.

### Research interpretation

The falsifiable hypothesis is that **a two-scale path-roughness gate improves a simple SMA-cross continuation rule by excluding choppy states, after controlling for simpler path-efficiency and volatility/trend filters**. The proposed economic/behavioral mechanism is conditional trend persistence: when recent price geometry is relatively smooth, a directional crossover may contain more continuation information than the same crossover during a jagged path.

This is materially distinct from the repository's Katz fractal-dimension capture because the estimator construction differs and this source supplies an explicit directional SMA-cross state machine. That distinction does not establish incremental alpha; it creates a testable ablation target.

## Signal

### Source-reported construction

The public source describes the simplified estimator as:

1. Over the Higuchi window, compute `L(1)` as the average absolute single-bar move.
2. Compute `L(4)` as the average absolute four-bar move, normalized by step count.
3. Compute `D = log(L(1) / L(4)) / log(4) + 1`, clipped to `[1, 2]`.
4. Define a smooth regime when `D <= threshold`.
5. Obtain direction from price relative to the trend SMA and its crossover.

Source-reported defaults:

- Higuchi Window: `60`;
- Trend SMA Length: `20`;
- Smooth Threshold: `1.65`;
- Cooldown Bars: `4`.

Source-reported long trigger:

- smooth regime;
- close above SMA;
- close crosses SMA upward;
- not already long;
- cooldown elapsed;
- `barstate.isconfirmed`.

Source-reported sell trigger:

- smooth regime;
- close below SMA;
- close crosses SMA downward.

The source also describes a position-lock state machine and alerts for buy/sell, smooth-regime transitions, stronger trend/chop states, and SMA crosses.

### Underspecified by the reviewed public description

The public description does not unambiguously specify whether a sell signal closes a long, opens a short, or both; the exact short-side state-machine symmetry; precise re-entry/state reset details; position sizing; stop/target logic; order type; or fill timing beyond confirmed-bar signal formation. The exact implementation details of the four-bar normalization are described conceptually but the Pine source was not independently reproduced in this Scout cycle. These gaps are not silently filled.

### Research-proposed operationalization for falsification only

For a future controlled test, use the source-reported confirmed-bar signal and execute at the next tradable bar under a predeclared fill model. Compare the same SMA-cross rule with and without the HFD gate. Any such order timing, long/short mapping, exit mapping, or fill convention not explicitly stated above is **research-proposed**.

## Required data

- Timestamped OHLC bars; the described core calculations use close prices.
- At least the 60-bar source-reported HFD window plus the 20-bar SMA warm-up under defaults.
- No volume, funding, open interest, order-book, aggressor-side, or options data are required by the described signal construction.
- Source says the estimator is suitable across live charts and discusses crypto/forex parameter guidance, but it does not define a fixed instrument universe or venue.
- Point-in-time requirement: HFD, SMA, crossover, cooldown, and state must use only information available through the confirmed signal bar.

## Execution assumptions

The source specifies confirmed-bar signal formation but does not provide a complete execution model. Market versus limit orders, same-close versus next-bar fills, fees, spread, slippage, impact/capacity, funding, leverage/margin, borrow/shorting, latency, and partial-fill/failure handling are **underspecified**. Any future backtest must declare them independently rather than infer zero costs.

## Evidence

### Source-reported

The source explains the estimator, signal rules, defaults, and qualitative regime interpretation. It does not provide a traceable backtest sample, Sharpe ratio, CAGR, drawdown, win rate, transaction-cost result, or other profitability statistic in the reviewed public description.

The source explicitly notes that the two-scale `k=1`/`k=4` approximation is faster but less accurate than a full Higuchi calculation over `k=1..k_max`, that the estimate can saturate on extremely thin instruments, and that the `1.65` threshold was calibrated to liquid majors/indices and may need adjustment on faster instruments.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- No source-reported profitability or transaction-cost evidence was identified.
- The HFD gate is directionless; direction comes from the SMA component.
- The source itself states the two-scale approximation is less accurate than full Higuchi estimation.
- The `1.65` threshold is source-reported as calibrated to liquid majors/indices, creating selection and crypto-portability risk.
- The source notes estimator saturation risk on extremely thin instruments.
- The HFD gate may simply proxy path efficiency, volatility, or trend strength rather than add independent information.
- The source notes theoretical random-walk `D=1.5` while real charts can show roughly `1.4-1.7` even during visibly trending sessions, weakening any naive universal threshold interpretation.

## Falsification plan

Any acceptance/rejection thresholds and portfolio mappings below are **research-defined falsification thresholds** or **research-proposed** where stated.

1. **Component ablation:** compare identical SMA-cross logic under (A) no regime gate, (B) source two-scale HFD gate, and (C) full Higuchi estimator implemented from a separately validated specification. Reject the two-scale layer if it does not improve OOS behavior over the ungated baseline.
2. **Simpler-control horse race:** compare HFD gating with Kaufman Efficiency Ratio, normalized displacement/path length, Katz FD, realized volatility, ATR-normalized range, ADX, and a Choppiness-style control. Require incremental OOS information rather than a renamed complexity measure.
3. **Threshold robustness:** test the source `1.65` threshold against training-only quantiles and nearby fixed thresholds without selecting on test performance. Reject claims of threshold specificity if results are fragile.
4. **Estimator ablation:** compare `k=1/4` against a full Higuchi construction. If the approximation's apparent edge disappears under the fuller estimator or small implementation changes, treat it as unstable.
5. **Direction attribution:** hold the HFD state fixed while varying only the directional baseline; ensure any return predictability is not simply SMA-cross alpha misattributed to HFD.
6. **Cooldown ablation:** compare source-reported 4-bar cooldown with no cooldown and predeclared alternatives. Treat cooldown as execution/state logic, not alpha, unless it adds robust net value.
7. **Point-in-time/OOS:** freeze all parameters before evaluation across liquid crypto instruments and multiple bar horizons, with confirmed-bar formation and no intrabar hindsight.
8. **Cost sensitivity:** include realistic fees, spread/slippage, and perpetual funding where applicable. Reject economic usefulness if any improvement is gross-only and disappears under realistic costs.
9. **Failure action:** if HFD does not add robust OOS value beyond the ungated SMA cross and simpler controls, reject the HFD gate rather than adding more indicators.

## Crypto portability

**unproven**

The estimator and SMA require only price bars, so mechanical portability is straightforward. The source explicitly discusses crypto in parameter guidance for embedding-style market speed only indirectly through its HFD framing, but it provides no crypto-specific validation or profitability evidence. The source-reported `1.65` threshold was calibrated to liquid majors/indices, not established as a crypto threshold.

Crypto evaluation must account for 24/7 candle boundaries, venue fragmentation, spot versus perpetual price construction, mark/index versus traded prices where relevant, thin-token noise, and perpetual funding if positions are carried.

## Limitations

- **underspecified:** exact sell/short state semantics, reset/re-entry details, position sizing, exits beyond opposing signal semantics, and execution/fill model.
- **not independently reproduced:** no Pine-code reproduction or backtest was run during this Scout cycle.
- **data gap:** no source-reported performance sample or cost model.
- **unproven:** incremental information beyond ungated SMA cross, KER/path efficiency, Katz FD, and simple volatility/trend controls.
- Source terminology linking lower fractal dimension with trend should not be upgraded into a claim of future-return predictability without independent evidence.

## Implementation status

`not-implemented`. This is normalized research material only. No Qlib implementation, full backtest, survivor promotion, Paper, Testnet, or Live validation was performed.

## Adoption boundary

`research-only / not-approved`.

Presence in this repository does not mean this hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, is profitable or validated alpha, or is approved for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

No stable related Hermes Wiki Brain page was verified in this GitHub-only cycle, so no Wiki link is fabricated.

Repository-adjacent research includes the Katz fractal-dimension regime record, Kaufman efficiency-ratio gating, DFA/Hurst regimes, and variance-ratio regimes. The present record is retained as a distinct two-scale HFD estimator plus explicit SMA-cross/cooldown signal construction.

## Sources

- TradingView, forexobroker, **Higuchi Fractal Dimension [forexobroker]**, public open-source script, published 2026-05-12, reviewed 2026-09-24: https://www.tradingview.com/script/iJGW4b97-Higuchi-Fractal-Dimension-forexobroker/
