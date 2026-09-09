---
schema: strategy-research-record-v1
title: "Edgeflow Composite LOB Microstructure Alpha for Binance Spot"
created: 2026-09-09
updated: 2026-09-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - spot
  - microstructure
  - limit-order-book
  - order-book-imbalance
  - trade-flow-imbalance
  - microprice
  - spread-regime
  - high-frequency
  - binance
status: research-only
confidence: medium
source_as_of: 2026-01-01
sources:
  - "Chrisler Nunes, 'Edgeflow: A Real-Time, Low-Latency Market Microstructure Engine for Cryptocurrency Spot Markets — Composite Alpha Signal Construction, Multi-Horizon Predictive Validation, and Realistic Execution Simulation in C++20', SSRN Electronic Journal, 2026. DOI: 10.2139/ssrn.6416798. https://doi.org/10.2139/ssrn.6416798"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Edgeflow Composite LOB Microstructure Alpha for Binance Spot

## Provenance

- **Primary source**: Chrisler Nunes, "Edgeflow: A Real-Time, Low-Latency Market Microstructure Engine for Cryptocurrency Spot Markets — Composite Alpha Signal Construction, Multi-Horizon Predictive Validation, and Realistic Execution Simulation in C++20", SSRN Electronic Journal, published 2026-01-01 (preprint).
- **DOI**: 10.2139/ssrn.6416798
- **Author**: Chrisler Nunes (single author; h-index 0, 0 citations at time of capture).
- **Publication status**: SSRN preprint; no peer review confirmed. 0 citations at time of capture.
- **Universe**: Binance spot markets; specific results reported for BTCUSDT.
- **Sample period**: Not explicitly stated in the abstract or landing page. The paper uses live L2 WebSocket data and reports "preliminary live-data results." Data period is unspecified (data gap).
- **Replication code**: Not found in public repositories at time of capture (data gap).

## Economic mechanism

### Source-reported

The author proposes that short-horizon return predictability in crypto spot markets can be captured by a composite signal combining four order-book microstructure features: (1) order book imbalance at the top of book (L1), (2) order book imbalance at five levels deep (L5), (3) microprice offset from mid price, and (4) trade flow imbalance over a rolling window. The signal is further conditioned on spread regime classification (TIGHT, NORMAL, WIDE), with the hypothesis that microstructure signals carry statistically significant alpha only under specific spread conditions. The economic channel is aggressive liquidity-taking pressure creating temporary price pressure that is partially predictable at sub-second horizons.

### Research interpretation

The hypothesized mechanism is that imbalances in the limit order book at multiple depth levels, combined with the microprice (volume-weighted mid reflecting true supply/demand pressure) and contemporaneous trade flow, capture transient informed or directional pressure that has short-lived but exploitable predictive power for next-tick or next-few-ticks price direction. The spread regime conditioning is motivated by the observation that microstructure signals are more informative when the market is tight (low spread, high informational content of small price changes) versus wide (noise-dominated). This is a compensated-liquidity-provision / adverse-selection hypothesis operationalized as a weighted linear composite.

**Component roles (research-proposed weighting)**:
- OBI L1 (weight 0.30): Top-of-book supply/demand pressure
- OBI L5 (weight 0.20): Deeper book pressure, less sensitive to single-level noise
- Microprice offset from mid (0.20): Volume-weighted fair value deviation
- Trade flow imbalance over rolling window (0.30): Aggressor-side directional pressure

## Signal

- **Formation timestamp**: Signal formed on each L2 depth update (diff update from Binance WebSocket). Becomes tradable immediately upon book update. Timezone: UTC (Binance server timestamps).
- **Lookback**: Rolling window for trade flow imbalance (exact window length not stated in abstract — data gap). OBI L1 and L5 are instantaneous (current book state). Microprice offset is instantaneous.
- **Long entry**: Composite signal exceeds a positive threshold (exact threshold not specified — research-proposed). Direction: buy when composite signal is positive and exceeds threshold.
- **Short entry**: Composite signal falls below a negative threshold (exact threshold not specified — research-proposed). Direction: sell when composite signal is negative and below threshold.
- **Exit**: Time-based exit at target horizon (50ms, 100ms, 250ms, or 500ms). The paper evaluates predictive power at these four horizons.
- **Holding period**: 50ms to 500ms (evaluated at four discrete horizons).
- **Parameters**: Four feature weights (0.30, 0.20, 0.20, 0.30) — source-reported. Spread regime thresholds (TIGHT/NORMAL/WIDE boundaries) — not specified in abstract (data gap). Entry thresholds — not specified (research-proposed).
- **Position sizing**: Inventory constraints with maximum limits (exact limits not specified — data gap). Not position-sized in the abstract beyond inventory caps.
- **Underspecified items**: Exact entry/exit thresholds, trade flow rolling window length, spread regime boundaries, position size limits, and signal normalization method are all unspecified in the available source material.

## Required data

- **Instrument**: Binance spot; BTCUSDT specifically; potentially other spot pairs (not confirmed).
- **Universe**: Binance spot markets.
- **Venue**: Binance (specific venue required for L2 diff-depth synchronization protocol).
- **Market type**: Spot.
- **Timeframe**: Real-time tick-by-tick (L2 depth updates and aggregated trade flow via WebSocket).
- **Fields**: Level-2 order book (multiple depth levels), aggregated trade flow, bid/ask prices and sizes, trade aggressor side (implied by trade flow), spread.
- **Point-in-time**: Real-time streaming data; no look-ahead in the validation framework (source-reported).
- **Timestamp**: Binance server timestamps; UTC.
- **Missing-data**: Binance diff-depth synchronization with sequence-ID validation and gap detection (source-reported). Stale or missed updates handled by the system's consistency checks.
- **Funding/fee/spread**: Per-trade fee deduction in simulation (taker fees modeled). Spread classified into regimes. Exact fee rates not specified (data gap — likely Binance standard maker/taker schedule).

## Execution assumptions

- **Signal-to-order timing**: Immediate upon signal generation (sub-second).
- **Next-bar vs same-bar execution**: Same-tick (real-time); no bar aggregation.
- **Order type**: Both aggressive (taker) and passive (maker) entry modes supported (source-reported).
- **Fill model**: Taker fills assumed immediate; maker fills subject to passive fill timeouts (source-reported). Exact fill probability model not specified (data gap).
- **Fees**: Per-trade fee deduction included in simulation (source-reported). Exact rates unspecified (data gap — likely Binance standard 0.1% taker / 0.1% maker or VIP tiers).
- **Spread**: Classified into TIGHT/NORMAL/WIDE regimes. Exact boundaries unspecified (data gap).
- **Slippage**: Not explicitly modeled in the abstract (data gap — may be included in the execution simulator but not detailed).
- **Impact / capacity**: Not discussed in abstract (data gap). Given 50ms horizons and Binance spot, capacity is likely very limited.
- **Leverage / margin**: Spot market; no leverage (1x).
- **Latency**: System is described as "real-time, low-latency" implemented in C++20. Exact latency not specified (data gap).
- **Partial fills / failures**: Maker fill timeouts supported. Partial fills not discussed (data gap).

## Evidence

### Source-reported

- Composite signal achieves hit rates above 60% at the 50ms horizon in the TIGHT spread regime for BTCUSDT.
- Raw Sharpe ratio exceeding 2.0 in simulation.
- These are simulation results using live L2 data with realistic fee modelling and inventory constraints.
- The paper reports hit rate, average price move in basis points, and Sharpe ratio by signal bucket and horizon, plus an alpha decay curve.
- **These are source-reported simulation results and have not been independently reproduced.**

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result.

**Known concerns**:
- The Pindza (2026) paper on microstructure alpha in crypto (DOI: 10.3389/fbloc.2026.1811716) found that no microstructure strategy survives realistic exchange fees after proper leakage controls on minute-level data. While edgeflow operates at a much shorter horizon (50ms-500ms), this result suggests caution about claiming microstructure alpha is robust to execution costs in crypto.
- The 60% hit rate at 50ms in TIGHT regime may not generalize to other regimes (NORMAL, WIDE), other assets, or other time periods. The regime-conditional reporting suggests the signal is not uniformly predictive.
- Single-author SSRN preprint with 0 citations; no peer review.

## Falsification plan

- **Out-of-sample**: Replicate the signal construction on an independent sample period not used in the original validation. Require Sharpe > 1.0 after fees on the held-out period.
- **Regime breakdown**: Test performance across all three spread regimes (TIGHT, NORMAL, WIDE). If the signal only works in TIGHT regime, assess how often TIGHT regime occurs and whether total alpha is positive after accounting for regime frequency.
- **Fee sensitivity**: Stress-test with Binance fee tiers (0.1% taker, 0.075% with BNB discount, VIP tiers). At 50ms horizons, taker fees of 0.1% per round trip may erode the signal.
- **Asset generalization**: Test on other Binance spot pairs (ETHUSDT, etc.) to assess whether the signal is BTC-specific or generalizable.
- **Parameter perturbation**: Vary the four feature weights away from the reported (0.30, 0.20, 0.20, 0.30). If performance is highly sensitive to exact weights, the signal may be overfit.
- **Latency sensitivity**: Assess how performance degrades with realistic execution latency (10ms, 50ms, 100ms, 500ms added delay).
- **Failure threshold**: If post-fee Sharpe < 0.5 on any independent sample, the strategy is not viable for live deployment.
- **Action on failure**: Mark as rejected for implementation; retain as research reference for microstructure signal construction methodology.

## Crypto portability

**direct**

The strategy is native to crypto spot markets (Binance). It does not require porting. However:
- The signal is venue-specific (Binance L2 WebSocket protocol, diff-depth synchronization). Other venues may have different book structures, update frequencies, or APIs.
- Spot-only; does not address perpetual futures, funding, or leverage.
- 24/7 market structure is naturally accommodated.
- Liquidity fragmentation across venues is not addressed.

## Limitations

- **Source quality**: Single-author SSRN preprint with 0 citations. No peer review confirmed. h-index 0.
- **Simulation-only**: All reported results are from simulation, not live trading. The "preliminary live-data results" language suggests data was collected live but not traded live.
- **Data period unspecified**: The sample period is not stated in the abstract or landing page (data gap).
- **Replication code unavailable**: No public GitHub repository found at time of capture (data gap).
- **Underspecified signal**: Exact entry/exit thresholds, trade flow window, spread regime boundaries, and normalization method are not specified in available source material.
- **Regime-limited results**: Strongest results (60% hit rate, Sharpe >2.0) are reported only for TIGHT regime at 50ms horizon. Performance in NORMAL and WIDE regimes, and at longer horizons, is not detailed in the abstract.
- **Single-asset**: Results reported only for BTCUSDT. Generalizability unknown.
- **Capacity**: At 50ms horizons on a single pair, capacity is likely very small. Not discussed in available material (data gap).
- **No negative evidence search conducted**: Limited source availability prevented a thorough search for contrary findings.

## Implementation status

Not implemented. No implementation exists in our research stack. The paper describes a C++20 system but no public code is available.

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:
- The strategy is profitable
- The alpha signal is validated
- The strategy is approved for implementation
- The strategy is approved for paper trading, testnet, or live trading

The composite LOB signal construction is a research-proposed design. All weights, thresholds, and regime boundaries are either source-reported (weights) or research-proposed (thresholds, boundaries). No independent validation has been performed.

## Related Wiki records

- [[crypto-perpetual-lob-explainable-catboost-gmadl-microstructure-2026-09-01]] — Related ML-based LOB feature analysis on Binance perpetuals (different mechanism: CatBoost/LOF vs. weighted linear composite; perpetuals vs. spot).
- [[crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01]] — Microstructure alpha testing on Binance spot/perp with negative result (no strategy survives realistic fees after leakage controls).
- [[clusterlob-order-flow-imbalance-trader-behavior-clustering-2026-09-03]] — Order flow imbalance clustering for intraday forecasting (equities, not crypto; different mechanism).

## Sources

- Chrisler Nunes, "Edgeflow: A Real-Time, Low-Latency Market Microstructure Engine for Cryptocurrency Spot Markets — Composite Alpha Signal Construction, Multi-Horizon Predictive Validation, and Realistic Execution Simulation in C++20", SSRN Electronic Journal, 2026. DOI: 10.2139/ssrn.6416798. https://doi.org/10.2139/ssrn.6416798
