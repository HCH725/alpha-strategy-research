---
schema: strategy-research-record-v1
title: Bitcoin Hash Ribbons 60/120 Industrial-Miner Recovery
created: 2026-09-21
updated: 2026-09-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-21
sources:
  - https://www.tradingview.com/script/ANeKILzG-Hash-Ribbons-2-0/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Hash Ribbons 60/120 Industrial-Miner Recovery

## Provenance

Public TradingView open-source script **Hash Ribbons 2.0**, author/page identity `PrismCharts`, published 2026-08-14. Stable source: https://www.tradingview.com/script/ANeKILzG-Hash-Ribbons-2-0/ . Source reviewed as of 2026-09-21.

This is materially distinct from the repository's existing classic Hash Ribbons record because the source explicitly argues that the classic faster calibration stopped working after 2022 and replaces it with slower 60/120-day hashrate moving averages for the industrial-mining era. The changed horizon/calibration is the core hypothesis under test, not a paraphrase of the classic rule.

## Economic mechanism

### Source-reported

The author describes the indicator as a modernized miner-capitulation signal for the industrial-mining era. The source claims the classic faster Hash Ribbons deteriorated after 2022 and uses 60-day and 120-day hashrate simple moving averages instead. Capitulation begins when the faster hashrate condition weakens relative to the slower baseline; recovery is tracked after that condition improves; a Buy marker is produced only after completed hashrate recovery and a subsequent positive price-momentum condition.

### Research interpretation

The falsifiable hypothesis is that structural changes in Bitcoin mining made the older miner-stress horizon too fast, while a slower 60/120-day hashrate spread better captures economically meaningful miner capitulation and recovery. If miner distress creates delayed forced selling and recovery removes that supply pressure, a confirmed slow-horizon recovery followed by positive price momentum may predict positive medium-horizon BTC returns beyond ordinary price trend and the classic 30/60 Hash Ribbons rule.

The mechanism must not be accepted merely because the slower parameters fit recent history. The central test is whether the 60/120 calibration has stable incremental out-of-sample information after controlling for BTC momentum, drawdown, halving/mining regimes, and the classic Hash Ribbons signal.

## Signal

- **Instrument:** Bitcoin; source is explicitly Bitcoin/miner focused.
- **Primary network inputs:** daily Bitcoin hashrate.
- **Slow-ribbon calibration:** SMA(60 days) and SMA(120 days) of hashrate, explicitly stated by the source.
- **Capitulation / recovery state:** source describes gray as capitulation start, green as recovery in progress, and lime as completed recovery. The exact Boolean transition formulas beyond the stated 60/120 calibration are not fully specified in the public description and are therefore `underspecified` here.
- **Buy confirmation:** source states that the blue Buy marker occurs only when price momentum turns upward after completed recovery. The exact price-momentum formula is not stated in the reviewed public description and is `underspecified`.
- **Optional modules:** breakdown tolerance and a discount filter are source-reported, but their formulas/defaults are not specified in the reviewed description.
- **Formation timing:** `research-proposed` — reconstruct all network and price features only from values actually available by each completed daily bar; do not backfill a recovery marker to an earlier bar.
- **Entry:** `research-proposed` — for falsification only, enter no earlier than the next tradable bar after a causally confirmed recovery-plus-price-momentum event.
- **Exit / holding:** source reports a 90-day evaluation horizon for its walk-forward result but does not state that 90 days is the executable exit rule. Treat 90-day forward return as an evaluation horizon, not an invented source exit rule.
- **Short rule:** not specified by this source.
- **Sizing / leverage / re-entry:** underspecified.

## Required data

- Bitcoin spot price OHLC sufficient for the later price-momentum reconstruction.
- Daily Bitcoin network hashrate with a point-in-time availability timestamp.
- At least 120 prior daily hashrate observations before a fully formed slow ribbon can exist.
- Historical source-vintage handling is material: revised/backfilled network series must not be treated as if their revised values were known at the original signal timestamp.
- For comparative falsification: data sufficient to construct the classic Hash Ribbons calibration and simple BTC momentum/trend controls.
- Timezone/candle boundary should be fixed consistently, preferably UTC for crypto research; the source description does not specify a timezone.

## Execution assumptions

The source is an indicator, not a fully specified execution strategy. It does not establish order type, fill model, fees, spread, slippage, market impact, leverage, margin, position sizing, or re-entry behavior.

`research-proposed`: use next-bar execution after a confirmed daily signal, include realistic BTC trading costs, and prohibit same-bar execution that assumes knowledge unavailable before the signal bar closes. Any later implementation must separately specify spot versus perpetual execution; if perpetuals are used, funding and mark/index conventions become material.

## Evidence

### Source-reported

The TradingView description reports that the 60/120-day hashrate-SMA version maintained a **75% hit rate** and **+31% average 90-day return** in walk-forward testing from **2011 to 2026**. These are author-reported results from the cited TradingView page, not results reproduced by this repository.

The source also states that the classic faster ribbons stopped working after 2022. This is an author claim and must be independently tested rather than treated as established fact.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source's motivation is itself negative evidence against the original faster Hash Ribbons calibration: it claims post-2022 deterioration. However, the reviewed page does not provide enough walk-forward protocol detail, event count, cost treatment, exact hit definition, or uncertainty estimates to establish that the reported 60/120 improvement is statistically robust rather than a recalibration to a small number of cycle events.

## Falsification plan

1. **Exact baseline comparison:** compare 60/120 hashrate recovery against the repository's classic Hash Ribbons rule using identical causal data, signal timing, evaluation horizons, and costs.
2. **Parameter-neighborhood test:** evaluate a preregistered coarse neighborhood around 60/120 (for example slower/faster pairs around those horizons) without selecting the best pair on the full sample. Reject the claim of a uniquely useful 60/120 calibration if performance is a narrow parameter spike.
3. **True walk-forward reconstruction:** fit/select any calibration using only past data, then evaluate the next segment. Never choose 60/120 using 2011-2026 and report that same history as independent validation.
4. **Post-2022 holdout:** specifically test whether the slower rule adds information in the industrial-mining period that motivated the redesign. Compare against 30/60, price momentum alone, and buy-and-hold/exposure-matched controls.
5. **Ablation:** hashrate recovery alone -> + price-momentum confirmation -> + optional discount filter -> + optional breakdown tolerance. Retain extra modules only if they add stable OOS value.
6. **Data-vintage audit:** repeat using only point-in-time available hashrate observations. Reject any apparent edge dependent on revised/backfilled network data.
7. **Regime controls:** stratify by halving era, mining-economics stress, BTC drawdown, realized volatility, and broad trend. Determine whether the signal is merely a delayed price-trend proxy.
8. **Event-count uncertainty:** report number of independent capitulation/recovery events, confidence intervals, and event-level returns. A high hit rate from very few cycle events is insufficient evidence.
9. **Failure action:** if 60/120 does not outperform the classic rule and simple momentum controls in leakage-safe OOS testing, reject the slower recalibration rather than adding further filters.

## Crypto portability

**direct** — the mechanism and source are explicitly Bitcoin-specific and depend on Bitcoin network hashrate.

Portability to other proof-of-work assets is unproven because miner economics, hash-market structure, security budgets, liquidity, issuance schedules, and data quality differ. It is not directly portable to proof-of-stake assets.

## Limitations

- `not independently reproduced`.
- Exact price-momentum confirmation formula is `underspecified` in the reviewed public description.
- Exact state-transition logic for the colored recovery stages is `underspecified` beyond the stated 60/120-day hashrate calibration.
- Optional breakdown-tolerance and discount-filter formulas/defaults are `underspecified`.
- Walk-forward protocol details, event count, costs, uncertainty and hit-rate definition are not provided on the reviewed page.
- Network hashrate data can be revised, smoothed or provider-dependent; point-in-time reconstruction is required.
- The small number of Bitcoin mining cycles creates severe statistical-power and parameter-selection risk.
- The author's statement that classic ribbons stopped working after 2022 is a hypothesis/motivation, not independently verified evidence.

## Implementation status

Research record only. No implementation in the research stack has been completed. No Qlib full backtest or downstream validation is implied.

## Adoption boundary

`research-only / not-implemented / not-approved`.

Presence in this repository does not mean the record passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received Paper/Testnet/Live approval.

## Related Wiki records

- `bitcoin-hash-ribbon-miner-capitulation-2026-08-31.md` — existing classic Hash Ribbons family; mandatory baseline for dedup-aware comparative testing.
- `blockchain-metrics-ribbon-cross-sectional-btc-onchain-indicators-2026-09-03.md` — broader blockchain-metric ribbon family.

## Sources

- PrismCharts, **Hash Ribbons 2.0**, TradingView open-source script, published 2026-08-14, reviewed 2026-09-21: https://www.tradingview.com/script/ANeKILzG-Hash-Ribbons-2-0/
