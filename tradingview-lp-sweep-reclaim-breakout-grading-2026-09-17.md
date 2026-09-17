---
schema: strategy-research-record-v1
title: "TradingView LP Sweep/Reclaim and Breakout Quality Grading"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - liquidity-sweep
  - breakout
status: research-only
confidence: medium
source_as_of: 2026-09-17
sources:
  - https://www.tradingview.com/script/ptNxWRuu-LP-Sweep-Reclaim-Breakout-Grading-Long-only/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView LP Sweep/Reclaim and Breakout Quality Grading

## Provenance

Public TradingView open-source strategy **LP Sweep / Reclaim & Breakout Grading: Long-only**, author `Shihyuuu`, stable URL https://www.tradingview.com/script/ptNxWRuu-LP-Sweep-Reclaim-Breakout-Grading-Long-only/. The page is dated and updated 2025-09-08. Source reviewed 2026-09-17. TradingView identifies it as an open-source script. This record normalizes the public description rather than redistributing Pine source.

GitHub dedup against current `main` found no record for canonical TradingView script identity `ptNxWRuu`, the title/author pair, or the normalized combination of prior-window liquidity sweep/reclaim plus separately graded Donchian breakout.

## Economic mechanism

### Source-reported

The source exposes two distinct long-entry families. The first treats a downside excursion through a prior-window low followed by a close back above that level as a liquidity-pool sweep and reclaim. The second treats a close above a prior Donchian high plus an ATR buffer as a momentum breakout. Both can be filtered by real-time quality grading intended to distinguish stronger setups from weaker ones.

For sweep setups, the source grades trend/slope, break of structure, candle body relative to ATR, location relative to a long EMA, headroom to a swing high, and repeated-sweep behavior. For breakout setups, it grades trend direction, candle body/ATR, distance beyond the breakout level, volume relative to its moving average, upper-wick behavior, headroom to the last swing high, and EMA slope.

### Research interpretation

The falsifiable hypothesis has two behavioral mechanisms rather than one arbitrary indicator stack:

1. **Sweep/reclaim mean reversion:** a transient trade below a prior-window extreme followed by a close back inside the range may represent stop/liquidity consumption without successful downside continuation. Reclaim is the primary signal; grading attempts to identify contexts where reversal/continuation upward is more plausible.
2. **Breakout continuation:** a close beyond a prior Donchian high with an ATR-scaled buffer may contain more continuation information when trend, participation, candle quality, and structural headroom agree.

The A/B/C score is therefore a conditional-selection layer. Later research should test whether the grading adds information beyond each raw trigger; complexity itself is not evidence of alpha.

## Signal

### Sweep/reclaim family — source-reported

- Compute liquidity-pool bounds from prior-bar window extremes: prior lowest low and prior highest high over an `N`-bar window, offset by one bar.
- Long sweep trigger: current low trades below the prior-window low and the current bar closes back above that prior-window low.
- Quality features include EMA(88) trend/slope, close above the last confirmed swing high as a BOS bonus, body size relative to ATR, location above a long EMA, headroom to swing high, and a multiple-sweep-count bonus.
- Feature scores are summed into A/B/C grades; A or B is required for sweep entry according to the reviewed description.

### Trend-breakout family — source-reported

- Core long trigger: close above the previous Donchian high of configurable `boLen`, plus an ATR buffer.
- Optional trend filter: close above the default EMA.
- Breakout grading includes price/EMA trend alignment and rising EMA, candle body relative to ATR, gap above the breakout level in ATR units, volume relative to a moving average, an upper-wick penalty, headroom to the last swing high, and an EMA-slope bonus.
- The feature sum maps to A/B/C; when grading is enabled, A or B is required.

### Specification gaps

The public description does not expose enough detail to reproduce the exact numeric scoring weights, grade cutoffs, default `N`, `boLen`, ATR-buffer magnitude, long-EMA length where distinct from EMA(88), swing-confirmation algorithm, volume-MA parameters, or multi-sweep counting rule. These are **underspecified** and are not invented here.

The reviewed description also does not specify the full exit, stop, holding-period, sizing, re-entry, pyramiding, or order-fill rules. No `research-proposed` values are introduced for those gaps in this Scout cycle.

## Required data

At minimum: timestamped OHLCV bars. OHLC is required for prior-window extremes, sweep/reclaim tests, Donchian highs, candle-body/wick measurements, EMA, ATR, and swing structure; volume is required for breakout participation grading. Instrument, venue, market type, and preferred timeframe are **underspecified** in the reviewed description. Point-in-time construction must use only prior confirmed information for offset window extremes and any confirmed swing feature; later validation must verify that swing/BOS logic cannot leak future confirmation into the signal timestamp.

## Execution assumptions

The source defines conditions using current-bar low/close and close-based breakout logic, but exact TradingView order timing and fill semantics are not stated in the reviewed description. A later causal implementation must distinguish signal formation at bar close from fill timing. Market/limit order choice, spread, fees, slippage, impact, latency, partial fills, leverage, margin, borrow/shorting, and funding are not specified. The strategy is explicitly long-only, so this source does not support inventing a mirrored short rule.

## Evidence

### Source-reported

The source provides explicit signal construction and grading features but the reviewed public description does not provide a traceable Sharpe ratio, CAGR, drawdown, win rate, or other performance statistic suitable for preservation here. No profitability claim is upgraded into evidence.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The scoring layer has many interacting features and therefore creates substantial overfitting risk unless its incremental contribution is tested out of sample. Confirmed-swing/BOS features can also create look-ahead risk if historical confirmation timing is implemented incorrectly. Sweep/reclaim setups may fail during genuine downside trend continuation, while breakout setups may fail on exhaustion/false breaks. None of these risks was independently quantified in this Scout cycle.

## Falsification plan

Test the two entry families separately before testing their union. For sweep/reclaim, compare the raw prior-low sweep-and-close-reclaim trigger against the same trigger plus grading. For breakout, compare a plain prior-Donchian-high + ATR-buffer trigger against the graded version. Use walk-forward/out-of-sample evaluation across trending and ranging regimes, and explicitly audit swing/BOS timestamps for look-ahead leakage. Ablate each grading component or coherent feature group to determine whether EMA trend, candle quality, volume, headroom, and structural bonuses add incremental information. Stress realistic fees/slippage and reject the grading thesis if it does not improve out-of-sample risk-adjusted behavior or false-signal quality relative to the simpler triggers after accounting for reduced trade count.

## Crypto portability

`unproven`. The source page does not establish crypto-specific evidence. The OHLCV-based mechanisms can be researched on crypto, but that would be a ported hypothesis. Crypto testing must account for 24/7 candle boundaries, venue-specific volume, fragmented liquidity, and — for perpetual futures — funding, mark/index conventions, leverage and liquidation mechanics.

## Limitations

- Exact grading weights and A/B/C thresholds are **underspecified** in the reviewed public description.
- Several lookbacks and structural algorithms are **underspecified**.
- Exit, sizing, re-entry and fill rules are **underspecified**.
- Confirmed-swing features require explicit point-in-time leakage auditing.
- The source is long-only; no short-side hypothesis is inferred.
- Not independently reproduced.

## Implementation status

`not-implemented`. No implementation, backtest, paper, testnet or live validation was performed in this Scout cycle.

## Adoption boundary

Research material only. Repository presence does not mean profitable, validated, approved for implementation, or approved for paper/testnet/live trading.

## Related Wiki records

No stable Hermes Wiki Brain record was consulted or fabricated in this GitHub-only Scout cycle.

## Sources

- TradingView — `Shihyuuu`, **LP Sweep / Reclaim & Breakout Grading: Long-only**: https://www.tradingview.com/script/ptNxWRuu-LP-Sweep-Reclaim-Breakout-Grading-Long-only/ (published/updated 2025-09-08; public open-source strategy page; reviewed 2026-09-17).
