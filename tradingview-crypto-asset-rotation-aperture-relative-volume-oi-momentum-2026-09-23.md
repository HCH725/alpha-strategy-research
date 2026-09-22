---
schema: strategy-research-record-v1
title: TradingView Crypto Asset Rotation Aperture — Relative Volume/OI Accumulation Momentum
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
  - https://www.tradingview.com/script/I9yPY5x6-Asset-Rotation-Aperture/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Crypto Asset Rotation Aperture — Relative Volume/OI Accumulation Momentum

## Provenance

Public TradingView open-source indicator **Asset Rotation Aperture**, published by ColeGarner on 2024-01-29 and updated 2025-01-08. Stable source URL: https://www.tradingview.com/script/I9yPY5x6-Asset-Rotation-Aperture/. Source reviewed as of 2026-09-23.

The source describes a multi-asset indicator that compares rolling cumulative volume, or alternatively open interest, after relative normalization. It characterizes the construction as a fork of Money Flow Index, similar to centered On-Balance Volume, modified to lead price, smoothed, and recursively plotted. The reviewed public description does not expose enough numerical detail to reconstruct every transformation exactly; those elements remain explicitly underspecified here.

## Economic mechanism

### Source-reported

The author states that relative volume accumulation momentum across multiple assets can visualize capital rotation and changing market narratives, and recommends using symbols from exchanges that dominate volume for the assets being compared.

### Research interpretation

The falsifiable hypothesis is that **cross-asset changes in normalized accumulation pressure contain incremental information about subsequent relative returns**. If capital reallocates gradually rather than instantaneously, an asset whose volume- or OI-based accumulation measure strengthens relative to peers may subsequently outperform peers whose normalized accumulation weakens.

This is materially different from a single-asset raw-volume trend: the proposed alpha channel is *relative capital-rotation pressure across assets*. The OI variant may capture derivatives-position expansion rather than spot turnover and therefore requires separate treatment rather than pooling the two data types.

## Signal

### Source-supported construction

- Universe: multiple user-selected assets, indices, narratives, or symbol equations.
- Input: rolling cumulative **volume or open interest** for each selected series.
- Transformation: source describes a Money Flow Index fork, similar to centered OBV, modified, smoothed, recursively plotted, and normalized so differently sized assets can be compared side by side.
- Signal interpretation: relative strengthening/weakening of the normalized lines is intended to reveal accumulation momentum and asset/narrative rotation.
- Venue guidance: source recommends selecting exchanges that dominate volume for the chosen assets.

The reviewed source description does **not** fully specify the exact accumulation formula, smoothing coefficients, recursive transformation, normalization window, formation timestamp, entry/exit thresholds, holding period, rebalance interval, re-entry rule, or position sizing. These are `underspecified` and must not be inferred as source-reported rules.

### Research-proposed operationalization

Only for falsification after a source-compatible reconstruction is available:

1. At each leakage-safe formation timestamp, rank eligible assets by the reconstructed Aperture value and/or its recent change.
2. Test whether high-ranked assets outperform low-ranked assets over predeclared forward horizons.
3. Run **volume** and **OI** variants independently; do not mix them until each survives its own ablation.
4. Compare level, first difference, and rank-change variants to determine whether any information comes from accumulation state or rotation acceleration.

These portfolio/ranking rules are research-proposed and are not claimed by the TradingView author.

## Required data

- Crypto asset universe defined point-in-time.
- Venue-specific spot or derivatives volume, depending on tested variant.
- Open interest for the OI variant, with contract/unit normalization documented.
- OHLC price data for returns and any source-compatible MFI-style price component required by reconstruction.
- Consistent timestamps and candle boundaries across assets/venues.
- Point-in-time symbol availability and delisting history.
- Venue dominance/liquidity information if implementing the author's recommendation to select representative exchanges.

Data must avoid survivorship bias. OI series must not be silently substituted across inverse, linear, coin-margined, and stablecoin-margined contracts without normalization.

## Execution assumptions

The source does not provide a complete executable strategy. Signal-to-order timing, next-bar versus same-bar execution, market/limit orders, fees, spread, slippage, impact, funding, leverage, margin, shorting constraints, partial fills, and capacity are unspecified.

Research testing should form signals only from information available by the decision timestamp and execute no earlier than the next tradable observation. Any long-short implementation must include venue-specific fees, funding where applicable, and conservative slippage/capacity assumptions.

## Evidence

### Source-reported

The TradingView author describes the indicator as a leading visualization of price, narratives, and capital rotation. The reviewed page does not report a traceable backtest, Sharpe ratio, CAGR, drawdown, hit rate, or other independently auditable performance statistic; none is imported here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-reported formal negative backtest was identified on the reviewed page. Important prior risks are nevertheless clear: volume can reflect churn rather than directional accumulation; OI can rise with both long and short positioning; exchange-specific activity can migrate; recursive smoothing can introduce lag; and cross-sectional normalization can mechanically change when the universe changes. Absence of source-reported negative evidence is not evidence that these risks are benign.

## Falsification plan

1. **Reconstruction gate:** first reproduce the source-compatible transform from publicly available source logic. If the exact transform cannot be reconstructed without guessing material parameters, stop rather than backtest an invented strategy.
2. **Incremental-information baseline:** compare against simple price momentum, raw volume momentum, turnover change, OBV/MFI, and raw OI change. Reject the Aperture transformation if it adds no stable out-of-sample information.
3. **Cross-sectional test:** use a point-in-time liquid crypto universe and test rank IC plus high-minus-low forward returns at predeclared horizons. Require the sign to remain stable across non-overlapping OOS periods.
4. **Rotation ablation:** compare absolute level, first difference, and cross-sectional rank change. If only one finely tuned representation works, treat that as overfitting risk.
5. **Volume vs OI ablation:** test spot-volume and derivatives-OI variants separately. A result in one does not validate the other.
6. **Venue robustness:** repeat with representative high-liquidity venues and reject a thesis that depends on one idiosyncratic venue feed without an economic explanation.
7. **Universe robustness:** use point-in-time membership, delistings, minimum liquidity screens, and leave-one-asset-out checks. Test whether results survive removal of BTC/ETH and major outliers.
8. **Timing placebo:** lag inputs by additional bars and test timestamp perturbations to detect look-ahead or synchronization artifacts.
9. **Cost hurdle:** apply fees, spread, slippage, funding, and turnover costs. Reject any trading interpretation whose net OOS edge is not economically positive and stable.
10. **Complexity test:** if simple volume/OI momentum performs equivalently, reject the additional recursive/normalized layer.

Failure of the incremental-information, OOS, timing, or cost tests should remove this hypothesis from further promotion rather than trigger parameter expansion.

## Crypto portability

`direct`

The source itself is presented for multi-asset use and explicitly discusses exchange volume selection; crypto assets are a direct intended use case. Portability across crypto venues remains nontrivial because volume fragmentation, wash activity, differing contract units, funding, OI definitions, and 24/7 candle boundaries can change the measured signal.

## Limitations

- `underspecified`: exact transformation and default numerical parameters are not fully recoverable from the reviewed page description alone.
- `not independently reproduced`.
- `data gap`: point-in-time venue dominance and historically consistent OI definitions may be difficult to maintain.
- Cross-sectional normalization can create composition effects when assets enter or leave the comparison set.
- Volume is not signed order flow; accumulation is an interpretation, not an observed fact.
- OI direction is ambiguous without complementary positioning/order-flow information.
- The author's qualitative claim that the indicator can lead price is source-reported, not validated alpha evidence.

## Implementation status

No implementation or Qlib full backtest has been completed in this research system. This record only preserves a source-backed, falsifiable research hypothesis.

## Adoption boundary

Research material only. Presence in this repository does not mean the record passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor/leaderboard entry, demonstrated profitability, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

- `[[crypto-cross-sectional-abnormal-volume-disagreement-2026-08-31]]` — related cross-sectional volume-family hypothesis, but based on abnormal turnover/disagreement rather than recursively normalized multi-asset accumulation momentum.
- `[[quantaalpha-institutional-price-volume-correlation-intraday-momentum-2026-09-05]]` — related price-volume interaction research with a different signal construction and horizon.

## Sources

- TradingView, ColeGarner, **Asset Rotation Aperture**, published 2024-01-29, updated 2025-01-08; reviewed 2026-09-23: https://www.tradingview.com/script/I9yPY5x6-Asset-Rotation-Aperture/
