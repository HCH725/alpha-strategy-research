---
schema: strategy-research-record-v1
title: "TradingView Livermore-Seykota Pivot Breakout with EMA and Volume Confirmation"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - breakout
  - trend-following
status: research-only
confidence: medium
source_as_of: 2026-09-16
sources:
  - https://www.tradingview.com/script/RwdDiWV5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Livermore-Seykota Pivot Breakout with EMA and Volume Confirmation

## Provenance

Public TradingView open-source strategy by `longtien`, titled **Livermore-Seykota Breakout Strategy**, published 2025-05-19. Stable source URL: https://www.tradingview.com/script/RwdDiWV5/. Source reviewed as of 2026-09-16. This record normalizes the public strategy description; it does not reproduce or redistribute the Pine source code.

## Economic mechanism

### Source-reported

The author describes a breakout system inspired by Livermore-style pivot breakouts, Seykota-style trend confirmation, and ATR-based risk management. Entries require a break of a recent pivot, directional moving-average alignment, and above-average volume. The stated intent is to align breakout trades with the prevailing trend and require participation confirmation.

### Research interpretation

The falsifiable alpha hypothesis is **conditional trend continuation after a structurally meaningful price breakout**. The components have distinct roles:

- Primary signal: breakout of a recent pivot high or pivot low.
- Directional regime: price relative to EMA50 plus EMA20/EMA200 ordering.
- Participation confirmation: current volume above its 20-period simple moving average.
- Risk/exit logic: ATR-scaled stop and trailing stop; these are risk controls rather than independent alpha evidence.

The hypothesis is that pivot breaks accompanied by trend alignment and elevated participation have better continuation properties than unfiltered pivot breaks. Each filter should later be ablated rather than assumed to add alpha.

## Signal

Source-described normalized logic:

- Long entry condition: close breaks above the recent pivot high; close is above EMA50; EMA20 is above EMA200; current volume exceeds the 20-period SMA of volume.
- Short entry condition: close breaks below the recent pivot low; close is below EMA50; EMA20 is below EMA200; current volume exceeds the 20-period SMA of volume.
- Initial stop-loss: 3 ATR from entry price.
- Trailing stop: ATR-based with a 2 ATR offset.

Material underspecification preserved from the public description:

- Pivot-left/right confirmation lengths and exact pivot function semantics are not stated in the reviewed description.
- ATR lookback and smoothing convention are not stated in the reviewed description.
- The exact order-placement timing after a qualifying close is not stated.
- Re-entry, simultaneous stop/trailing-stop precedence, pyramiding, and position sizing are not established by the reviewed description.

No missing value above is silently supplied as source-reported fact.

## Required data

Minimum data for the described hypothesis:

- OHLCV bars for the traded instrument.
- Sufficient history for EMA20, EMA50, EMA200, 20-period volume SMA, pivot confirmation, and ATR.
- Causal timestamps and a consistent candle boundary.

The source description is not venue-specific and does not establish spot versus perpetual semantics. For crypto adaptation, venue, market type, fee schedule, funding treatment, and bar timezone must therefore be fixed before testing.

## Execution assumptions

The public description states close-based breakout conditions and ATR-scaled exits but does not establish a complete fill model. A later implementation must explicitly decide whether a signal formed on bar close is executed at that close or no earlier than the next executable price. Same-bar fills must not be assumed without causal evidence.

Fees, spread, slippage, market impact, funding, leverage/margin, partial fills, and latency are underspecified in the reviewed source description and must be modeled explicitly in validation.

## Evidence

### Source-reported

The TradingView page states that the strategy is intended to combine trend-aligned pivot breakouts, volume confirmation, and dynamic ATR-based risk management. No independently verified performance statistic is carried into this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independent negative study was identified in this Scout cycle. Mechanistically, pivot strategies are sensitive to confirmation lag and pivot-definition choices; those are research risks, not source-verified failure evidence. Absence of identified negative evidence is not evidence of robustness.

## Falsification plan

Test the complete rule against a plain pivot-breakout baseline under identical universe, timestamps, costs, and execution assumptions. Required ablations should include:

1. pivot breakout only;
2. + EMA50 price-direction filter;
3. + EMA20/EMA200 ordering;
4. + volume > SMA20 confirmation;
5. full rule with ATR exit logic.

Require strictly causal pivot confirmation: a pivot cannot become tradable before the bars needed to confirm it are available. Evaluate long and short legs separately, multiple market regimes, out-of-sample periods, and realistic fee/slippage sensitivity. The hypothesis is materially weakened if the full filter stack fails to improve robust out-of-sample risk-adjusted results versus the simpler breakout baseline after costs, or if apparent performance disappears when pivot confirmation is shifted to its true availability timestamp.

Any numerical acceptance threshold used later is research-defined and must be declared before the corresponding test rather than inferred after observing results.

## Crypto portability

`adapted`

The breakout/trend/volume mechanism is portable to liquid crypto markets in principle, but the reviewed source does not establish crypto-specific empirical validity. Crypto testing must account for 24/7 candle boundaries, fragmented venue volume, spot-versus-perpetual differences, funding, fee tiers, and the possibility that pivot behavior differs materially across timeframes and venues.

## Limitations

- Pivot construction is underspecified in the reviewed public description.
- ATR lookback/smoothing is underspecified.
- Execution and sizing semantics are incomplete.
- Not independently reproduced.
- The named association with well-known traders is descriptive branding from the source, not evidence that the exact composite rule is historically attributable to them.
- Multiple filters may be redundant; ablation is required.

## Implementation status

Research record only. No implementation or quantitative-runtime validation was performed by this Scout.

## Adoption boundary

`research-only`. This record is not evidence of profitability, validated alpha, implementation approval, paper/testnet approval, or live-trading authorization.

## Related Wiki records

No stable Hermes Wiki record was consulted or fabricated in this GitHub-only Scout cycle.

## Sources

- TradingView — longtien, **Livermore-Seykota Breakout Strategy**, published 2025-05-19: https://www.tradingview.com/script/RwdDiWV5/
