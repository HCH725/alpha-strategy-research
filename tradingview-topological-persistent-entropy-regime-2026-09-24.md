---
schema: strategy-research-record-v1
title: TradingView Topological Persistent-Entropy Regime
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: low
source_as_of: 2026-09-24
sources:
  - https://www.tradingview.com/script/sCRu5xEB-Prometheus-Topological-Persistent-Entropy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Topological Persistent-Entropy Regime

## Provenance

Public TradingView open-source script: **Prometheus Topological Persistent Entropy**, author/page identity `ScorsoneEnterprises`. The public page shows original publication `Sep 30, 2024` and an update `May 2, 2025`. Stable source URL: https://www.tradingview.com/script/sCRu5xEB-Prometheus-Topological-Persistent-Entropy/. Source reviewed as of 2026-09-24.

The reviewed public description is sufficient to identify a topological/persistence-entropy regime hypothesis, but not sufficient to reconstruct the exact persistence-diagram algorithm or a complete trading rule. Those gaps are preserved rather than inferred.

## Economic mechanism

### Source-reported

The source describes a topology-inspired procedure applied to log-return segments. It says a persistence diagram tracks the birth and death of price features, with feature lifetime representing persistence. It then computes entropy from those lifetimes. The source interprets more persistent features as associated with stable trends and shorter-lived features as associated with volatility, and states that smoothed persistence entropy above its SMA signals bearishness.

### Research interpretation

The falsifiable hypothesis is that **the distribution of persistence lifetimes contains incremental information about future return or regime behavior beyond ordinary volatility, trend efficiency, fractal dimension, and conventional entropy measures**. A second, weaker hypothesis is that the source's persistence-entropy-versus-SMA state has directional information rather than merely repackaging recent volatility or path geometry.

This record does not assume that the source's topological terminology establishes a valid persistent-homology implementation. The exact construction must be independently reconstructed and audited before treating it as such.

## Signal

Source-supported components:

- Input described as segments of log returns.
- Construct price features with birth/death states and associated lifetimes.
- Compute entropy from feature lifetimes.
- Smooth the persistence-entropy series and compare it with an SMA.
- Source-reported directional interpretation: smoothed persistence entropy above its SMA signals bearishness.
- The source reports that a 2025-05-02 update improved the entropy function and added binning.

Underspecified in the reviewed public page text:

- segment/window length;
- exact filtration, complex, distance construction, homology dimension, and birth/death algorithm;
- exact lifetime normalization and entropy formula;
- binning method introduced in the update;
- smoothing method and lengths;
- SMA length;
- exact crossing/state logic and whether equality has special handling;
- long-entry rule, short-entry rule beyond the qualitative bearish interpretation, exit, holding period, re-entry, sizing, and complete position state machine.

Research-proposed operationalization for later testing only: first reproduce a point-in-time persistence-entropy state from completed bars, then compare a simple directional baseline conditioned on entropy above/below its trailing smoother. No missing source parameter is asserted here.

## Required data

Timestamped OHLC price bars sufficient to derive the source's log-return series. The reviewed source does not require volume, funding, order book, aggressor-side trades, open interest, or options data.

For crypto evaluation, venue, spot/perpetual market type, bar boundaries, missing bars, and price field must be fixed in advance. All feature birth/death and entropy calculations must use only information available at the signal timestamp.

## Execution assumptions

The source page does not specify signal-to-order timing, same-bar versus next-bar execution, market versus limit orders, fill model, fees, spread, slippage, impact/capacity, leverage/margin, funding, borrow/short mechanics, latency, partial fills, or failure handling. All are data gaps.

Closed-bar formation and next-bar execution would be a **research-proposed** anti-look-ahead convention for later testing, not a source-reported implementation.

## Evidence

### Source-reported

The source qualitatively associates persistent features with stable trends and shorter-lived features with volatility, and states that smoothed persistence entropy above its SMA signals bearishness. It also says the indicator tends to look better on higher timeframes while functioning the same way on lower timeframes.

No source-reported Sharpe, CAGR, drawdown, win rate, statistical significance, or independently auditable backtest result was identified in the reviewed public page text.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The public description does not establish that the stated birth/death construction is mathematically equivalent to a standard persistent-homology pipeline. The exact filtration and entropy construction are underspecified. The bearish interpretation is asserted without a performance table or significance test in the reviewed page. The source itself notes that the lower-timeframe display looks unusual. A release note says red/green coloring had previously been backwards, showing at least one historical presentation defect. None of these points independently disproves the hypothesis, but they materially lower confidence until reproduced.

## Falsification plan

1. Reconstruct the estimator point-in-time and validate it on synthetic series with known structure before any return test. Fail the construction if reasonable implementations consistent with the public description produce materially incompatible states.
2. Compare persistence entropy against simpler controls: realized volatility, absolute-return dispersion, ATR/range measures, Kaufman/path efficiency, fractal dimension, Shannon entropy, permutation entropy, and sample entropy.
3. Test the source-reported entropy-versus-SMA bearish state against an ungated directional baseline using chronological out-of-sample splits and realistic costs.
4. Ablate the topological layer: replace persistence lifetimes with simpler return/run-length or excursion-duration distributions. If performance is unchanged, the topological construction lacks incremental evidence.
5. Test multiple assets and timeframes with parameters frozen from past-only data and correct for multiple testing.
6. Reject or materially weaken the hypothesis if persistence entropy provides no stable OOS incremental information over the simpler controls, if directionality reverses across reasonable parameterizations, or if any apparent edge disappears after fees/spread/slippage.

## Crypto portability

**unproven**

The statistic is price-derived and therefore mechanically portable to crypto bars, but the reviewed source does not provide crypto-specific empirical validation. Crypto testing must account for 24/7 sessions, exchange-specific candle boundaries, venue fragmentation, perpetual funding, mark/index versus trade prices, variable liquidity, and spot/perpetual differences. Higher- versus lower-timeframe behavior should be tested rather than inferred from the source's qualitative display comment.

## Limitations

- Exact persistent-homology / birth-death construction: **underspecified**.
- Window, filtration, entropy normalization, smoothing and SMA parameters: **underspecified**.
- Complete trading lifecycle: **underspecified**.
- Directional interpretation: **unproven**.
- Crypto evidence: **unproven**.
- Performance: **not independently reproduced**.
- Any later reconstruction choices absent from the source must be labeled **research-proposed**.

## Implementation status

Not implemented in the research stack. No Qlib full backtest, survivor promotion, leaderboard entry, Paper, Testnet, or Live validation is implied.

## Adoption boundary

Research-only. Presence in this repository does not mean the hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor, demonstrated profitability, or received implementation/Paper/Testnet/Live approval.

## Related Wiki records

No Wiki Brain lookup or write was performed because this Scout is GitHub-only. No Wiki relationship is asserted. Repository-level comparisons for later research include entropy-regime, fractal-dimension, and topological-data-analysis families; similarity alone is not adoption evidence.

## Sources

- TradingView — ScorsoneEnterprises, **Prometheus Topological Persistent Entropy** (public open-source script; published 2024-09-30; updated 2025-05-02; reviewed 2026-09-24): https://www.tradingview.com/script/sCRu5xEB-Prometheus-Topological-Persistent-Entropy/
