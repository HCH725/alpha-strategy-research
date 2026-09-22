---
schema: strategy-research-record-v1
title: Bitcoin Halving-Corrected Puell Multiple and Miner-Revenue RSI
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-22
sources:
  - https://www.tradingview.com/script/3wL26GR7-Puell-Multiple-Variants-OperationHeadLessChicken/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Halving-Corrected Puell Multiple and Miner-Revenue RSI

## Provenance

Public TradingView open-source indicator **Puell Multiple Variants [OperationHeadLessChicken]**, author/page identity `OperationHeadLessChicken`, published 2025-10-22 and updated 2025-10-29. Stable source: https://www.tradingview.com/script/3wL26GR7-Puell-Multiple-Variants-OperationHeadLessChicken/ . Source reviewed as of 2026-09-22.

Repository deduplication before capture found the existing classic Puell Multiple/miner-capitulation family, but no record for this canonical TradingView source or its materially distinct halving-normalization / miner-revenue-RSI hypothesis. The distinction is central: this record does not duplicate the classic claim that current miner revenue relative to its trailing 365-day average identifies valuation extremes; it tests whether structural block-subsidy reductions make fixed Puell thresholds nonstationary and whether explicit halving correction or bounded normalization improves cross-cycle comparability.

## Economic mechanism

### Source-reported

The author presents three related Bitcoin miner-revenue views: the classical Puell Multiple; a **Halving-Corrected Puell Multiple** intended to compensate for diminishing block rewards across halvings; and a **Miner Revenue RSI** intended to map miner-revenue conditions into a bounded 0-100 scale. The source states that classical Puell historically signaled cycle tops and bottoms but argues that diminishing rewards make fixed overvalued/undervalued territories difficult to compare across cycles. The author reports experimenting with a post-halving correction factor of approximately **1.63** to align overvalued levels across cycles, while noting that this loses a common horizontal undervaluation region; the Miner Revenue RSI is proposed as another normalization approach.

### Research interpretation

The falsifiable mechanism is **structural nonstationarity in miner-revenue valuation caused by scheduled subsidy halvings**. A raw Puell Multiple may change its distribution as the subsidy component of miner revenue falls relative to fees and Bitcoin's market structure evolves. If this is economically material, a causal halving-aware normalization or a bounded transformation of miner revenue should produce more stable cross-cycle extreme definitions than fixed thresholds on classical Puell.

This does not assume that the source's fitted 1.63 factor is structurally correct. That value may simply align a small number of historical peaks. The useful hypothesis is broader: whether any preregistered, causal halving adjustment adds out-of-sample information beyond classical Puell, raw BTC price momentum, drawdown, and halving-era controls.

## Signal

Source-defined components:

1. **Classical Puell Multiple:** current daily Bitcoin miner issuance/revenue value relative to a long historical baseline; the public page describes the classical Puell family but the complete code-level formula should be reconstructed from a point-in-time miner-revenue series rather than copied from the source.
2. **Halving-Corrected Puell:** post-halving miner revenue is multiplied by a correction factor; the source reports an experimentally selected factor around **1.63** to improve cross-cycle comparability of upper extremes.
3. **Miner Revenue RSI:** applies RSI-style bounded normalization to miner revenue, mapping the state to 0-100 to make high/low territories visually comparable.

The source page does not establish a complete executable entry/exit/holding/sizing lifecycle. Numerical trade thresholds for all variants, exact RSI lookback/default, re-entry, stop logic, and position sizing are therefore `underspecified` here.

`research-proposed` operationalization for falsification only:

- Form every feature from daily miner-revenue observations actually available at the completed daily bar.
- Compare classical Puell, the source-reported 1.63 halving correction, a preregistered family of economically defensible corrections estimated using training history only, and Miner Revenue RSI.
- Evaluate subsequent BTC returns over fixed horizons rather than inventing a source trading lifecycle.
- Treat the 1.63 value as a source-reported fitted parameter, never as a known structural constant.

## Required data

- Bitcoin daily spot/index price for USD valuation and forward-return evaluation.
- Point-in-time Bitcoin block subsidy / issuance schedule and actual daily issuance.
- Point-in-time transaction-fee revenue if miner revenue is reconstructed rather than consumed from a provider.
- Daily miner revenue in USD or sufficient causal components to reconstruct it.
- Exact Bitcoin halving timestamps/heights.
- Historical data-vintage metadata where provider series can be revised or backfilled.
- At least the lookback required by the classical Puell baseline and any RSI calculation before a signal is considered formed.
- Consistent UTC day boundaries for 24/7 Bitcoin data.

## Execution assumptions

The TradingView source is an indicator family, not a fully specified execution strategy. Order type, signal-to-order timing, fees, spread, slippage, market impact, leverage, margin, sizing, stops, exits, and re-entry are not specified.

`research-proposed`: for any later executable falsification, use no earlier than next-bar execution after a completed daily signal and include realistic spot or perpetual costs. If perpetuals are used, funding, mark/index pricing and liquidation mechanics must be modeled separately. Macro-cycle event tests should also report exposure-matched and buy-and-hold controls so apparent performance is not merely long-BTC beta.

## Evidence

### Source-reported

The TradingView page states that classical Puell has historically been useful for Bitcoin cycle tops and bottoms but argues that diminishing block rewards complicate fixed overvalued/undervalued thresholds across halvings. The author reports that experimentation produced a halving correction factor around **1.63**, bringing historical upper extremes closer to a common horizontal level. The source also proposes Miner Revenue RSI as a 0-100 normalization intended to restore interpretable high/low regions.

These are source-reported design claims from the cited TradingView page. The reviewed page does not provide an independently auditable walk-forward protocol, transaction-cost study, confidence intervals, or evidence that 1.63 was selected without full-sample hindsight.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The repository already contains a classic Puell Multiple miner-capitulation record, so a new normalization has value only if it adds stable incremental information. The source itself acknowledges a trade-off: the halving correction that visually aligns upper extremes no longer preserves a common horizontal undervaluation region. The small number of Bitcoin halving cycles also makes any fitted correction factor highly vulnerable to data mining.

## Falsification plan

1. **Mandatory classic baseline:** compare every variant against the existing classical Puell formulation using identical point-in-time miner-revenue data and evaluation horizons.
2. **No full-sample fitting:** estimate any correction factor only on past cycles, freeze it, then test on the next unseen halving era. The source-reported 1.63 factor is evaluated as-is but is not reoptimized on the test period.
3. **Parameter fragility:** test a coarse preregistered neighborhood around the source-reported correction. If apparent performance is a narrow spike around 1.63, treat it as overfit rather than evidence of a structural constant.
4. **RSI ablation:** classical Puell -> halving-corrected Puell -> Miner Revenue RSI. Require each transformation to improve a predefined OOS criterion rather than merely produce cleaner visual bands.
5. **Simple-control test:** compare against raw miner-revenue growth, BTC momentum, drawdown, days-since-halving and halving-era dummy variables. Reject the transformation if these simpler controls explain the same information.
6. **Fee-share regime:** stratify by subsidy-versus-fee composition. A fixed subsidy correction should weaken as transaction fees become a larger fraction of miner revenue; failure to account for this is evidence against a universal factor.
7. **Data-vintage audit:** reconstruct signals only from miner-revenue observations available at the historical timestamp. Reject any edge dependent on revised/backfilled data.
8. **Event-count uncertainty:** report the number of independent upper/lower extreme episodes, confidence intervals and cycle-by-cycle outcomes. Do not infer robustness from a handful of visually aligned peaks.
9. **Forward horizons:** test preregistered medium/long horizons and both upper- and lower-tail states separately; avoid selecting the best horizon after observing outcomes.
10. **Failure action:** if neither halving correction nor Miner Revenue RSI improves leakage-safe OOS discrimination or risk-adjusted returns over classical Puell and simple controls, reject the added normalization rather than adding further filters.

## Crypto portability

**direct** for Bitcoin only. The source and mechanism depend on Bitcoin miner revenue and Bitcoin's programmed subsidy halvings.

Portability to other proof-of-work assets is **unproven** because issuance schedules, fee markets, miner economics, security budgets, liquidity and halving mechanics differ. It is not directly portable to proof-of-stake assets.

## Limitations

- `not independently reproduced`.
- Source-reported correction factor ~1.63 appears experimentally calibrated and is exposed to severe small-sample / hindsight risk.
- Exact RSI lookback/default and complete executable threshold lifecycle are `underspecified` in the reviewed public description.
- Bitcoin has very few independent halving cycles, sharply limiting statistical power.
- Miner revenue increasingly contains transaction fees as well as subsidy; a subsidy-only halving correction may become structurally misspecified.
- Provider miner-revenue series can differ or be revised; point-in-time reconstruction is required.
- Visual alignment of historical cycle extremes is not evidence of predictive alpha.

## Implementation status

Research record only. No implementation in the research stack has been completed. No Qlib full backtest or downstream validation is implied.

## Adoption boundary

`research-only / not-implemented / not-approved`.

Presence in this repository does not mean the record passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received Paper/Testnet/Live approval.

## Related Wiki records

- `bitcoin-onchain-puell-multiple-miner-capitulation-2026-08-31.md` — classical Puell Multiple family and mandatory baseline.
- `tradingview-bitcoin-hash-ribbons-60-120-industrial-miner-recovery-2026-09-21.md` — related but distinct miner-stress/recovery family based on hashrate rather than miner-revenue normalization.
- `tradingview-bitcoin-cost-of-production-difficulty-issuance-regime-2026-09-21.md` — related miner-economics family based on difficulty/issuance proxies.

## Sources

- OperationHeadLessChicken, **Puell Multiple Variants [OperationHeadLessChicken]**, TradingView open-source indicator, published 2025-10-22, updated 2025-10-29, reviewed 2026-09-22: https://www.tradingview.com/script/3wL26GR7-Puell-Multiple-Variants-OperationHeadLessChicken/
