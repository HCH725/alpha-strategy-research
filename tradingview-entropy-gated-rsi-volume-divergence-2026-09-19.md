---
schema: strategy-research-record-v1
title: TradingView Entropy-Gated RSI and Volume Divergence
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-19
sources:
  - https://www.tradingview.com/script/xJjDK73N-Entropy-Divergence-No-Repaint-PhenLabs/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Entropy-Gated RSI and Volume Divergence

## Provenance

- Public TradingView open-source Pine Script v6 page: `Entropy Divergence (No Repaint) [PhenLabs]` by PhenLabs.
- Stable source URL: https://www.tradingview.com/script/xJjDK73N-Entropy-Divergence-No-Repaint-PhenLabs/
- TradingView publication label: `Feb 3`; the retrieved page does not expose a year next to that label, so no publication year is inferred.
- Source as-of: 2026-09-19.
- TradingView labels the script open-source. This record normalizes the public description and does not reproduce the Pine source.

## Economic mechanism

### Source-reported

The source argues that ordinary divergence signals are noisy when market behavior is chaotic. It computes Shannon entropy from binned logarithmic price returns and permits divergence signals only when smoothed entropy is below a configurable threshold. Within that low-entropy state, it detects RSI divergence and volume divergence around confirmed pivots. The author characterizes low entropy as a more structured or predictable market state and presents the entropy gate as a way to reduce false divergence signals.

### Research interpretation

The falsifiable hypothesis is not that low entropy is intrinsically bullish or bearish. It is that **conditional predictability matters**: a price-extreme non-confirmation signal may have more directional information when the recent return distribution is relatively ordered than when it is highly disordered.

Component roles:

- **Regime gate:** low Shannon entropy of recent log returns.
- **Primary reversal signal:** price/RSI pivot divergence.
- **Secondary confirmation:** price/volume divergence.
- **Timing constraint:** confirmed pivots and closed-bar signal generation.

The key incremental-alpha question is whether entropy adds information beyond ordinary divergence. A reduction in signal count alone is not evidence of alpha.

## Signal

Source-reported normalized logic:

1. Compute logarithmic price returns over a configurable entropy lookback.
2. Bin those returns into a configurable histogram and calculate Shannon entropy `H(X) = -sum(p * log2(p))`.
3. Smooth entropy with an EMA.
4. Define the source's tradeable regime when smoothed entropy is below the configured threshold.
5. Track confirmed pivots in price, RSI and volume using configurable left/right pivot windows.
6. Bullish RSI divergence: price forms a lower low while RSI forms a higher low; bearish RSI divergence is the converse at highs.
7. The source also detects volume divergence and classifies signals as RSI, VOL, or RSI+VOL.
8. A final signal requires a low-entropy state, a confirmed divergence condition, and a closed bar.

Source-reported defaults/ranges visible on the public page:

- entropy lookback: default 20, range 5-100 bars;
- histogram bins: default 10, range 5-50;
- low-entropy threshold: default 2.5, range 0.5-4.0;
- entropy EMA smoothing: default 3, range 1-10;
- RSI length: default 14, range 5-50;
- pivot left: default 5, range 2-20;
- pivot right: default 2, range 1-10;
- divergence search range: default 60, range 20-200 bars;
- minimum bars between pivots: default 5, range 3-30.

The public description does not fully specify the mathematical rule used for volume divergence, position entry order type, exit, holding period, re-entry, position sizing, stop, target, or portfolio interaction. Those items are `underspecified` and are not invented here.

Any conversion from the indicator's labels into executable positions is `research-proposed` and must be frozen before testing.

## Required data

- Instrument/universe: source is presented as a general chart indicator; PhenLabs describes its work as including crypto systems, but this specific page does not prescribe a fixed universe.
- Market type/venue: underspecified.
- Timeframe: configurable chart timeframe; no single canonical timeframe is prescribed.
- Fields: timestamped OHLCV sufficient for log returns, RSI, volume, and pivot construction.
- Point-in-time constraint: signals must be formed only after the right-side pivot confirmation bars and the current bar are complete.
- Timestamp/candle-boundary convention must be frozen before comparative testing.
- Missing-data handling: underspecified.

## Execution assumptions

The source is an indicator rather than a complete executable strategy. Market/limit order choice, signal-to-order delay, fill price, fees, spread, slippage, impact, leverage, margin, short availability, funding, partial fills, and capacity are not specified.

A causal test must not backdate execution to the visual pivot bar. Earliest eligibility is after the source-required right-side pivot confirmation and closed-bar signal are known; the exact fill convention is `research-proposed` and must be pre-registered.

## Evidence

### Source-reported

The source describes the entropy gate as reducing noisy divergence signals and states that signals are confirmed at bar close without repainting. It also notes that pivot confirmation creates delay, signals may be sparse in strong trends, the entropy threshold may require instrument/timeframe optimization, and divergences can fail during strong trends.

No independently verified profitability, Sharpe, CAGR, drawdown, or win-rate evidence is claimed in this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself identifies pivot-confirmation delay, parameter sensitivity, reduced signal frequency in some regimes, and divergence failure in strong trends. In addition, low entropy can arise from quiet/non-directional compression, so an entropy gate may merely select low-volatility states rather than states in which divergence has directional edge. This is a research concern, not a source-reported result.

## Falsification plan

1. Freeze universe, venue/market type, timeframe, entropy estimator, binning convention, all lookbacks/thresholds, pivot timing, divergence definitions, and execution timing before evaluation.
2. Test **RSI divergence alone** against **RSI divergence + entropy gate**. If the entropy gate does not improve untouched out-of-sample expectancy or risk-adjusted performance after controlling for lower trade count, reject the gate's incremental-alpha thesis.
3. Run component ablations: RSI-only, volume-only, RSI+volume, entropy+RSI, entropy+volume, and entropy+RSI+volume.
4. Compare the entropy gate with simpler controls matched for signal frequency: realized-volatility percentile, ATR percentile, and a random gate. If Shannon entropy adds no incremental information, prefer the simpler control or reject the entropy mechanism.
5. Separate low-entropy compression from low-entropy directional persistence. Condition results on trend strength and realized-volatility regime to test whether entropy is only a proxy for those variables.
6. Enforce strict point-in-time pivot availability. Any result that enters on the historical pivot timestamp before right-side confirmation is invalid.
7. Use walk-forward/untouched OOS testing across multiple liquid crypto instruments and materially different volatility/trend regimes. Parameter tuning must occur only inside training windows.
8. Stress realistic fees, spread and slippage. Reject the executable hypothesis if the conditional edge does not survive costs or is concentrated in a small number of parameter/timeframe choices.

## Crypto portability

`unproven`

The source is compatible with chart data and is associated with crypto-oriented work, but the retrieved page does not provide independently reproduced crypto performance evidence. Crypto-specific risks include 24/7 candle-boundary choices, venue-specific volume, spot-versus-perpetual volume differences, fragmented liquidity, and funding/derivatives effects not represented by OHLCV alone.

## Limitations

- Not independently reproduced.
- The source is an indicator, not a complete trading strategy.
- Volume-divergence construction is not fully specified in the public prose reviewed here.
- Exit, holding, sizing and execution are underspecified.
- Entropy is sensitive to lookback, histogram-bin count and threshold selection.
- Pivot confirmation introduces an explicit causal delay and creates a serious look-ahead risk if implemented incorrectly.
- Low entropy may proxy for simpler volatility or trend-state variables rather than supply independent information.

## Implementation status

No implementation or backtest in our research stack has been completed. `not-implemented`.

## Adoption boundary

Research material only. Presence in this repository does not imply profitable alpha, implementation approval, paper-trading approval, testnet approval, or live-trading approval.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted from this GitHub-only Scout run.

## Sources

- TradingView — PhenLabs, `Entropy Divergence (No Repaint) [PhenLabs]`: https://www.tradingview.com/script/xJjDK73N-Entropy-Divergence-No-Repaint-PhenLabs/ (accessed/as-of 2026-09-19).
