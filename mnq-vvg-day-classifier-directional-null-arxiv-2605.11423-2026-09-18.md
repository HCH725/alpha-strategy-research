---
schema: strategy-research-record-v1
title: "MNQ Volatility-Volume-Gap Day Classifier: Behavioral Signal with Directional-Strategy Null"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - futures
  - mnq
  - nasdaq-100
  - regime-classification
  - overnight-gap
  - intraday-reversal
  - negative-evidence
  - falsification
  - year-heterogeneity
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - "Mathias Mesfin, 'A Validated Volatility-Volume-Gap Classifier for Regime Identification in MNQ Intraday Data', arXiv:2605.11423 (replacement listing 2026-09-18; original v1 May 2026). Comments note revised year-activation counts, Bailey et al. citation fix, RTH Confluence OOS cross-ref T=3.11, warm-up/threshold detail. https://arxiv.org/abs/2605.11423"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Author replacement (listed with q-fin.TR/new on 2026-09-18) corrected year-activation counts so year totals sum to 40; fixed literature citations; added warm-up/threshold methodological detail. Core null result (no directional configuration passed) is unchanged in the replacement abstract."
---

# MNQ Volatility-Volume-Gap Day Classifier: Behavioral Signal with Directional-Strategy Null

## Provenance

Academic preprint: Mathias Mesfin, **A Validated Volatility-Volume-Gap Classifier for Regime Identification in MNQ Intraday Data**, arXiv:2605.11423 [q-fin.TR, q-fin.CP, q-fin.ST]. Replacement listing observed 2026-09-18 on arXiv q-fin.TR new; original submission May 2026. Canonical URL: https://arxiv.org/abs/2605.11423. Source reviewed as of 2026-09-18 via public arXiv listing abstract and replacement comments (full PDF not independently re-audited this cycle beyond the listing text).

Repository deduplication on current `main` found no record with arXiv id `2605.11423` or the same normalized VVG day-classifier claim. Adjacent record `mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05.md` is a **different** Mesfin paper (arXiv:2605.04004) on structural limits of OHLCV signal families / Gross Edge Ceiling — same author and instrument family, different construct (signal-family falsification vs day-type classifier + directional null). Do not treat this as a duplicate update of that file.

## Economic mechanism

### Source-reported

The paper builds a day-classification system for MNQ (Micro E-Mini Nasdaq 100) futures from three **simultaneously elevated pre-market conditions**:

1. Absolute overnight gap,
2. Absolute first-30-minute return,
3. First-bar volume relative to a 20-day rolling baseline.

Named **Volatility-Volume-Gap (VVG)** classifier. Evaluation: 947 trading days of five-minute data 2021–2025; thresholds computed on an **expanding window** to prevent lookahead bias. Classifier activates on roughly **4.4% of sessions (40 days)**.

Source-reported behavior on classifier days:
- **77.6% reverse from their intraday peak before the close**
- Mean peak-to-close giveback **11.73 points**
- **25.6 basis point next-day return spread** versus non-classifier days
- Year-by-year path heterogeneity: **2024** classifier days closed at mean **+40.74 points** while **2025** crashed to **−42.48** — described as the core obstacle for any directional strategy

Directional test (source-reported):
- **Eight directional configurations tested. None passed.**
- Best result: **T = 1.46**, mean net **+7.80 points**, **127 OOS trades**, reversal entry with OLS regression filter
- **2024 broke year stability**
- Binding constraints: ~40-day sample (~10 per year) and regime-dependent intraday behavior that no fixed rule survives across all test years
- Classifier is preserved as a **research asset**: it identifies a real behavioral phenomenon but **cannot generate a deployable directional signal under current constraints**

Replacement comments (2026-09-18 listing): corrected year-activation counts (year totals now sum to 40); fixed Bailey et al. citation split; updated RTH Confluence cross-reference to walk-forward OOS figures (T=3.11); added warm-up cutoff and threshold-selection methodological detail.

### Research interpretation

The economic hypothesis is that **pre-market stress episodes** (large gap + large opening move + elevated first-bar volume) mark sessions with elevated intraday mean-reversion / path fragility on equity-index futures — a regime label, not a guaranteed edge. The paper’s own negative result is the incremental research content: even when the label co-moves with giveback statistics, **fixed directional rules fail out-of-sample** once year heterogeneity and small activated-sample size are respected.

Scout interpretation: this strengthens the repository’s MNQ/OHLCV negative-evidence family without collapsing into the Gross Edge Ceiling paper — different object of study (day classifier vs signal families).

## Signal

Source-specified classifier (research-normalized from listing abstract):

- Instrument: MNQ five-minute bars; pre-market/opening features for classification.
- Formation: pre-market / early session using overnight gap, first-30-minute return, first-bar volume vs 20-day rolling baseline; expanding-window thresholds (lookahead-controlled per source).
- Entry (directional tests, all null per source): eight configurations including reversal entry with OLS regression filter — exact parameterization of all eight not fully listed in the public abstract; mark underspecified for bit-exact replication from abstract alone.
- Exit / holding: intraday; source discusses peak-to-close giveback and next-day spread — exact trade exit rules for the best OOS config not fully specified in abstract.
- Holding period: intraday to close and/or next-day measurement window.
- Parameters: threshold construction expanding-window; activation ~4.4%; sample 947 days / 40 classifier days.

Underspecified without full PDF: complete list of eight directional configs; exact gap/volume thresholds; OLS filter definition; fee/slippage model behind “mean net +7.80 points.”

## Required data

- Instrument: MNQ Micro E-Mini Nasdaq 100 futures.
- Universe: 947 trading days 2021–2025 per source.
- Timeframe: overnight gap + first 30 minutes + first bar volume; 5-minute intraday path.
- Fields: OHLCV, overnight session reference, volume baseline.
- Point-in-time: expanding-window thresholds claimed to prevent lookahead; Scout did not re-run the audit.
- Crypto portability: not a crypto instrument (see below).

## Execution assumptions

Source-reported OOS trade counts imply a backtest-style evaluation; this Scout cycle does not treat any configuration as implementable. No live/cost ledger claimed in the listing abstract beyond “mean net” for the best failed config.

## Evidence

### Source-reported

arXiv:2605.11423 listing abstract reports classifier definition, 947-day sample, 4.4%/40-day activation, 77.6% peak-reversal rate, 11.73-point giveback, 25.6 bps next-day spread, 2024 vs 2025 sign flip, eight directional configs none passing (best T=1.46, +7.80 pts mean net, 127 OOS trades), and the explicit conclusion that the classifier is a research asset not a deployable directional signal. Replacement comments document count/citation/methodology fixes without reversing the null.

### Independently reproduced

not independently reproduced

### Negative evidence

The paper **is** negative evidence against deployable fixed directional rules on VVG days. Adjacent MNQ Gross Edge Ceiling record (2605.04004) independently documents multi-family OHLCV falsification — complementary prior, not the same study. Year heterogeneity and tiny activated samples are binding constraints per source.

## Falsification

Research-proposed tests for any future VVG-directional claim (not executed):

1. Pre-register one directional rule and evaluate on post-2025 holdout with expanding thresholds; research-defined falsification threshold: fail if OOS T < 2 or year-stability fails in any single year.
2. Sample-size stress: bootstrap/leave-one-year-out on the 40 activated days; fail if edge is driven by 2024 alone.
3. Threshold perturbation ±20% on gap/return/volume cuts; fail if activation set or sign of edge is unstable.
4. Placebo classifier: random days matched on vol only; fail if VVG does not outperform placebo on the behavioral stats (77.6% giveback).
5. Cost stress: add MNQ tick/fees to the best config’s +7.80 mean; fail if net ≤ 0.
6. Leakage audit: recompute expanding thresholds strictly point-in-time; fail if any full-sample quantile enters.
7. Instrument transfer: same three-condition classifier on crypto perps (research-proposed adaptation); fail if no analogous stress-day path statistic appears — do not assume portability.

## Crypto portability

Mark: **not applicable / unproven**.

- Source instrument is MNQ equity-index futures, not crypto.
- Research-proposed adaptation only: analogous “gap + opening move + volume spike” stress labels on crypto perpetuals could be tested; 24/7 crypto lacks a clean overnight session, so the gap feature needs redesign (e.g., funding-window or low-liquidity-hour returns).
- Crypto portability is not authorization to trade.

## Limitations

- Abstract-level capture; full PDF methodology not re-audited this cycle beyond listing/comments.
- `not independently reproduced`.
- Activated sample ~40 days — high variance; year sign flip is fatal for naive directional use.
- Underspecified eight-config menu in public abstract.
- Equity-index specific; weak direct crypto alpha.
- Incremental-write threshold: met as **new negative/falsification evidence** on a day-type classifier construct distinct from 2605.04004 OHLCV family limits.

## Implementation status

`not-implemented`. Research capture only; no runtime change; no Wiki Brain write.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

- `mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05.md` — different paper (2605.04004), same author/instrument family.
- Other intraday/futures falsification records in repo — adjacent negative context.

## Sources

- Mesfin, M., arXiv:2605.11423, https://arxiv.org/abs/2605.11423 (listing abstract + replacement comments; captured 2026-09-18).
