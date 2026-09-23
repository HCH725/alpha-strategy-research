---
schema: strategy-research-record-v1
title: "TradingView Reset-CVD Zero-Line Dominance Regime"
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
  - https://www.tradingview.com/script/Scjs0OsS/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Reset-CVD Zero-Line Dominance Regime

## Provenance

Public TradingView open-source indicator **CVD v2 (Cumulative Volume Delta) + Divergences** by `IZO_X`, published 2026-03-11. Stable source URL: https://www.tradingview.com/script/Scjs0OsS/. Source reviewed as of 2026-09-23.

The source describes a bar-by-bar volume-delta histogram, a cumulative CVD line, configurable reset periods (`Never / Weekly / Monthly`), an adjustable CVD EMA, divergence alerts, and zero-line crossovers. The page recommends Weekly reset with EMA 21 for short swing horizons and Monthly reset with EMA 21 for medium swing horizons. These are source-described settings, not independently verified performance parameters.

## Economic mechanism

### Source-reported

The author frames CVD as a measure of the balance between buyer and seller pressure and describes a zero-line crossover as a shift in dominance. Weekly reset is suggested for short swing trading and Monthly reset for longer positions. The source also presents price/CVD divergence as a separate signal family.

### Research interpretation

The materially distinct falsifiable hypothesis retained here is **reset-anchored CVD zero-line state/crossover**, not generic CVD divergence: after a fixed calendar reset, the sign of cumulative directional volume may encode whether net estimated buying or selling pressure has dominated the current weekly/monthly window, and a sign change may contain incremental short-horizon continuation or reversal information beyond price momentum and raw volume imbalance.

The reset itself may be economically arbitrary in 24/7 crypto. Therefore any apparent edge could instead be a calendar-boundary artifact, price-direction proxy, or consequence of the source's approximate delta construction.

## Signal

Source-described components relevant to this record:

- Bar-by-bar volume delta is accumulated into CVD over a configurable reset period.
- Reset choices: Never, Weekly, Monthly.
- CVD can be smoothed with an adjustable EMA; the page recommends EMA 21 for its weekly/monthly swing examples.
- A CVD zero-line crossover is described as a shift in buyer/seller dominance.
- Weekly reset is suggested for short swing trades of roughly 3–14 days; Monthly reset for medium swing positions of roughly 2–4 weeks.

The public description says delta is volume-weighted according to the close position within each candle, but the reviewed page does not expose enough normalized detail to assert the exact formula here without copying/reconstructing Pine code. Exact bar-level delta formula, crossover execution timing, entry/exit lifecycle, stop, target, sizing, and re-entry rules are therefore **underspecified** for this record.

Research-proposed operationalization for falsification, not source-reported trading rules:

1. Construct point-in-time CVD using the source-compatible delta definition once independently reconstructed, with explicit UTC weekly and monthly reset boundaries.
2. Treat positive/negative reset-CVD state and confirmed zero-line crossovers as separate features rather than assuming a complete strategy.
3. Measure forward returns after bar-close crossover confirmation over predeclared horizons; test both continuation and reversal interpretations.
4. Compare raw reset-CVD with EMA-smoothed reset-CVD and with non-reset rolling/cumulative controls.

## Required data

- Liquid crypto instruments with reliable OHLCV.
- Venue-specific volume; spot and perpetual markets should be tested separately.
- Bar timestamps with an explicit timezone/calendar boundary for Weekly and Monthly resets.
- Point-in-time OHLCV only; no future-bar information may enter delta or reset state.
- For cross-venue robustness, venue identity and volume units must remain explicit rather than pooling incompatible feeds.
- Funding, basis and open interest are not required by the source signal but are useful controls for perpetual-market tests.

## Execution assumptions

The source is an indicator, not a complete executable strategy. A leakage-safe test should confirm a crossover only after the relevant bar is complete and execute no earlier than the next tradable observation unless an intrabar model is explicitly supported.

Fees, spread, slippage, market/limit choice, impact/capacity, funding, leverage/margin, borrow/shorting, latency, partial fills and failures are not specified by the source. Any strategy-level test must model them rather than treating an indicator marker as a frictionless fill.

## Evidence

### Source-reported

The TradingView page describes resettable CVD, EMA smoothing, zero-line crossovers as dominance shifts, and Weekly/Monthly swing-oriented settings. It does not provide a traceable independent backtest establishing profitability of the zero-line crossover hypothesis.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The repository already contains research documenting that generic short-horizon CVD/order-flow signals can fail after realistic costs, so CVD provenance alone is not evidence of alpha. The source's volume delta is an estimate derived from bar information rather than exchange-native bid/ask aggressor data. No source-backed profitability evidence for the reset/zero-line rule was identified on the reviewed page; absence of additional negative evidence is not evidence that it works.

## Falsification plan

1. Independently reconstruct the source-compatible delta formula before testing; if it cannot be reproduced unambiguously, classify the record as technically incomplete rather than substituting a convenient CVD definition.
2. Test Weekly and Monthly reset-CVD zero-line crossovers on multiple liquid crypto spot and perpetual instruments using point-in-time bars and explicit UTC boundaries.
3. Baselines: price momentum over matched horizons, signed candle volume, rolling volume imbalance, non-reset CVD, and simple cumulative return since the same reset boundary.
4. Ablation: raw reset-CVD sign, zero-line crossover, EMA-smoothed state/crossover, and reset + smoothing together. The composite should add stable OOS information to justify its complexity.
5. Calendar placebo: shift weekly/monthly reset boundaries and compare rolling fixed-length windows. Reject a claimed structural mechanism if performance exists only at one arbitrary boundary.
6. Direction test: evaluate continuation and reversal hypotheses symmetrically rather than assuming a zero crossing predicts continuation.
7. Venue test: compare spot and perpetual feeds and repeat across major venues; reject if the effect is driven by one volume feed or symbol convention.
8. Use walk-forward/OOS evaluation and realistic fee, spread and slippage scenarios. For perpetuals, include funding where positions span funding events.
9. Reject or materially weaken the hypothesis if reset-CVD state/crossovers do not add directionally stable OOS information beyond price/volume baselines after costs, or if results depend on one reset boundary, asset, venue, or tuned EMA setting.

## Crypto portability

**direct**

The source explicitly presents CVD for crypto-compatible use. However, crypto's 24/7 market makes weekly/monthly reset boundaries convention-dependent, and venue fragmentation means CVD can differ materially across exchanges. Spot volume and perpetual volume also represent different participant mixes; perpetual funding and leverage can confound apparent directional-volume dominance.

## Limitations

- **underspecified:** exact normalized bar-delta formula is not asserted from the public description alone; it must be independently reconstructed before implementation.
- **underspecified:** no complete entry/exit/holding/sizing lifecycle.
- **not independently reproduced:** no Scout-side empirical replication was performed.
- **data gap:** bar-derived directional volume is not exchange-native aggressor-side trade flow.
- Weekly/monthly reset boundaries may create calendar artifacts in a 24/7 market.
- EMA 21 and suggested horizons are source settings, not validated optimal parameters.
- CVD can be highly venue-dependent because crypto volume is fragmented.

## Implementation status

Research record only. No implementation in the research stack, Qlib full backtest, or runtime integration has been completed.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, is profitable or validated alpha, or is approved for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

No Wiki Brain lookup was performed because this Scout is GitHub-only. GitHub deduplication found multiple CVD/divergence and order-flow records, but no existing record for this canonical TradingView source or a materially identical **calendar-reset CVD zero-line dominance/crossover** hypothesis before this write. This record intentionally excludes generic price/CVD divergence as its primary hypothesis to avoid duplicating those families.

## Sources

- IZO_X, “CVD v2 (Cumulative Volume Delta) + Divergences,” TradingView public open-source script, published 2026-03-11, reviewed 2026-09-23: https://www.tradingview.com/script/Scjs0OsS/
