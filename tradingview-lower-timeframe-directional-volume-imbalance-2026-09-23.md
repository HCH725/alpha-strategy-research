---
schema: strategy-research-record-v1
title: TradingView Lower-Timeframe Directional-Volume Imbalance as Parent-Bar Continuation Signal
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-23
sources:
  - https://www.tradingview.com/script/yyPTcwdo-delta-imbalance-candle/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Lower-Timeframe Directional-Volume Imbalance as Parent-Bar Continuation Signal

## Provenance

- Public TradingView open-source indicator: **delta imbalance candle** by `sudhakar_kb`.
- Stable source URL: https://www.tradingview.com/script/yyPTcwdo-delta-imbalance-candle/
- Source reviewed as of 2026-09-23.
- The public page displays `Apr 7` but does not unambiguously expose the publication year in the reviewed description, so no year is asserted here.
- The source uses `request.security_lower_tf` to inspect 1-minute bars inside a higher-timeframe chart bar, classifies each 1-minute bar's volume by the sign of its close-versus-open move, and flags a parent bar when one side's accumulated volume is at least a configurable multiple of the other side. The description gives 3x as the example/default imbalance relationship.
- GitHub deduplication on current `main` found no record for this canonical TradingView source. Related repository records use true/proxy order-flow, OI, CVD, or volume imbalance in different constructions; none found in the dedup search used this source's specific 1-minute directional-volume aggregation plus parent-bar imbalance-ratio rule.

## Economic mechanism

### Source-reported

The author describes the indicator as a high-frequency order-flow tool intended to identify an intrabar buyer/seller imbalance. One-minute sub-bars are assigned to buying volume when close > open and otherwise to selling volume; a parent bar is highlighted only when accumulated volume on one side is at least the selected imbalance ratio versus the other side. The source also allows a separate source ticker, for example using a futures instrument as the flow source while viewing another instrument.

The source characterizes the resulting state as aggressive or institutional buying/selling pressure. That characterization is preserved as an author claim, not treated here as verified trade-aggressor measurement.

### Research interpretation

**Research-proposed hypothesis:** a large imbalance in lower-timeframe directionally classified volume may contain short-horizon continuation information beyond the parent bar's own return and total volume. The possible mechanism is persistence after unusually one-sided intrabar participation.

However, the construction does **not** identify true buyer-initiated versus seller-initiated trades. It classifies an entire 1-minute bar's volume from the sign of that bar's price change. Therefore the primary falsification question is whether the lower-timeframe aggregation adds information beyond ordinary lower-timeframe momentum, signed candle volume, and parent-bar price movement. If it does not, the order-flow interpretation and incremental-alpha thesis fail.

A second research-proposed hypothesis is that using a liquid derivatives source ticker to condition a related spot instrument may provide lead/lag information. This is not demonstrated by the source and must be tested separately from same-instrument use.

## Signal

Source-supported construction:

1. For each higher-timeframe chart bar, obtain the constituent 1-minute bars from a selected source ticker.
2. For each 1-minute bar, classify its full volume as **buy volume** when `close > open`; otherwise classify it as **sell volume**.
3. Sum classified buy volume and sell volume over the parent bar.
4. Flag bullish imbalance when buy volume is at least `imb_ratio` times sell volume; flag bearish imbalance when sell volume is at least `imb_ratio` times buy volume.
5. The public description gives 3x as an example/default imbalance relationship and states that the ratio is configurable.
6. The indicator colors the parent candle when a qualifying imbalance occurs. The source does not specify an executable entry/exit strategy.

- Formation timing: the historical signal should be treated as known only after all constituent 1-minute bars of the parent bar are complete. Any research execution based on the completed imbalance must occur no earlier than the next feasible timestamp.
- Lookback: constituent 1-minute bars inside the current parent bar; no additional historical lookback is stated for the imbalance calculation.
- Long entry: not specified by source.
- Short entry: not specified by source.
- Exit / holding period: not specified by source.
- Re-entry: not specified by source.
- Position sizing: not specified by source.
- Multi-timeframe dependency: 1-minute source data aggregated inside the parent chart timeframe.
- Cross-instrument dependency: optional source ticker distinct from the chart ticker.
- Parameter: configurable `imb_ratio`; 3x is explicitly described as the imbalance example/default relationship.

**Research-proposed operationalization for falsification only:** measure forward returns after confirmed bullish and bearish imbalance events over pre-registered horizons, then compare the event signal against simpler controls. This is not source-reported trading logic.

## Required data

- One-minute OHLCV for the selected source ticker.
- Parent-timeframe OHLCV for event alignment and forward-return measurement.
- Exact, point-in-time parent/sub-bar timestamp mapping with no future 1-minute bar included in a parent-bar signal.
- For cross-instrument testing, synchronized source and target instruments and explicit handling of venue/timezone/candle-boundary differences.
- Source example mentions a futures source ticker; market type is otherwise not constrained by the public description.
- Crypto testing is research-proposed. For perpetual-futures implementation, funding, mark/index conventions and contract metadata are required for realistic net returns even though they are not inputs to the indicator.
- Missing 1-minute sub-bars must not be silently treated as zero volume without an explicit rule.

## Execution assumptions

The source is an indicator and does not specify signal-to-order timing, order type, fills, fees, spread, slippage, impact, leverage, margin, funding, borrow, latency, partial fills, or failures.

Any later executable test must use a causally valid timestamp. A parent-bar imbalance that requires all constituent 1-minute bars cannot be assumed executable at the same parent-bar close at an advantageous historical price without a justified fill model. Cross-instrument source/target tests must additionally model timestamp synchronization and any venue latency.

## Evidence

### Source-reported

The source reports the indicator construction and its intended use for detecting intrabar directional-volume imbalance. It does not report a traceable Sharpe ratio, CAGR, drawdown, win rate, or independently validated predictive statistic on the reviewed public page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The public construction uses candle-direction volume classification rather than true bid/ask aggressor data. A 1-minute bar with `close > open` assigns all of its volume to buying even though actual trades during that minute can occur on both sides. This creates a direct alternative explanation: the indicator may be a nonlinear repackaging of lower-timeframe price direction and volume rather than order-flow information.

No source-reported evidence was found showing that the 3x imbalance threshold predicts subsequent returns, survives costs, generalizes across timeframes/instruments, or adds information beyond price momentum and volume controls. Absence of such evidence is a material gap, not evidence of no effect.

## Falsification plan

1. **Causal reconstruction:** reproduce the 1-minute classification and parent-bar aggregation exactly, using only sub-bars available by parent-bar completion.
2. **Core event study:** pre-register parent timeframes and forward horizons, then measure forward returns after bullish and bearish imbalance events without tuning the horizon to the result.
3. **Parent-bar control:** compare against parent-bar return sign, return magnitude, range, and total-volume percentile. Reject the incremental-alpha thesis if the imbalance event does not add stable OOS information.
4. **Lower-timeframe momentum control:** compare against simple counts of up/down 1-minute bars, summed 1-minute returns, and volume-weighted signed 1-minute returns. This is the key test of whether the ratio construction adds anything beyond intrabar momentum.
5. **Classification ablation:** compare the source's whole-bar volume assignment with alternative research controls such as proportional candle-body signed volume. Do not call either construction true aggressor flow without trade-side data.
6. **Threshold robustness:** test the source-described 3x relationship and a small pre-registered neighborhood of imbalance ratios. Reject an effect that exists only at a narrowly optimized threshold.
7. **Continuation versus reversal:** test both hypotheses rather than assuming that extreme imbalance must continue. Pre-register direction before final OOS evaluation.
8. **Same-instrument versus cross-instrument:** test source=target separately from derivatives-source/spot-target configurations. Cross-instrument improvement must beat target-only price/volume controls to support a lead/lag thesis.
9. **Crypto venue robustness:** if ported to crypto, replicate across liquid BTC/ETH instruments and more than one venue where synchronized 1-minute history is adequate.
10. **Timeframe robustness:** test multiple parent bar sizes while keeping the 1-minute source resolution fixed; report event counts and clustering.
11. **Cost sensitivity:** apply realistic fees, spread, slippage and, for perpetuals, funding. A gross effect that disappears under plausible costs is not tradable alpha.
12. **Frozen OOS:** freeze signal construction, threshold set, horizons and controls before final out-of-sample testing. If the imbalance rule fails to improve the strongest simple price/volume baseline OOS, reject it rather than adding filters.

## Crypto portability

**adapted**.

The source construction is mechanically portable to crypto instruments with reliable 1-minute OHLCV, but the reviewed source does not demonstrate crypto alpha. Crypto-specific risks include 24/7 candle boundaries, fragmented spot/perpetual venues, different source/target liquidity, perpetual funding, mark/index versus traded price, and timestamp alignment. The optional futures-source/spot-target concept is especially sensitive to venue and instrument synchronization.

## Limitations

- `not independently reproduced`: neither the indicator nor the research-proposed forward-return tests were reproduced in this Scout cycle.
- `unproven`: no source-backed evidence that the imbalance predicts forward returns or provides incremental alpha.
- The source's buyer/seller labels are proxy classifications from 1-minute candle direction, not verified aggressor-side trade data.
- Entry, exit, holding period, re-entry and sizing are `underspecified` because the source is an indicator rather than a complete strategy.
- Publication year is a provenance gap on the reviewed public page; only `Apr 7` is displayed.
- Cross-instrument lead/lag use is research-proposed and must not be inferred from the indicator's source-ticker feature alone.

## Implementation status

No implementation in the research stack has been completed. No backtest was run in this Scout cycle.

`implementation_status: not-implemented`

## Adoption boundary

Research-only. This record has not passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, become a frozen survivor or leaderboard entry, or received Paper, Testnet, or Live approval. It must not be represented as profitable, validated alpha, or approved trading logic.

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]] — schema reference only; no Wiki access or write was performed in this GitHub-only Scout cycle.
- No additional Wiki relationship was asserted because this Scout is GitHub-only.

## Sources

- TradingView — **delta imbalance candle**, `sudhakar_kb`: https://www.tradingview.com/script/yyPTcwdo-delta-imbalance-candle/ (reviewed 2026-09-23).
