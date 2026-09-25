---
schema: strategy-research-record-v1
title: "Triadic Stress Index (TSI) correlation-network stress-state risk overlay"
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-08-11
sources:
  - "https://arxiv.org/abs/2608.10788 (arXiv:2608.10788v1 [physics.soc-ph, cross-list q-fin.RM + q-fin.ST], submitted 11 Aug 2026 10:47:57 UTC; pinned v1 HTML 246627 bytes, SHA-256 82beb8205757769e08e42bc4287e2c0c23ad999864f848d4eacb547eb9b5f9b2, read end to end 2026-09-25)"
  - "https://doi.org/10.48550/arXiv.2608.10788 (DataCite DOI, 302 -> https://arxiv.org/abs/2608.10788 checked 2026-09-25; no publisher DOI and no journal-ref in the arXiv API record)"
  - "https://github.com/BiomeMakers/TSI-OmegaS @ commit 01948247d129cd2860203e44d6ea5df61751bb30 (main HEAD verified live 2026-09-25, author Alberto Acedo, 2026-09-23T09:09:11Z)"
  - "https://github.com/BiomeMakers/TSI-OmegaS/blob/01948247d129cd2860203e44d6ea5df61751bb30/explorations/README.md (source's own closed-experiment inventory used for negative evidence)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Sections 6.6 and 9 define the Holm-Bonferroni family as 4x2x3 = 24 tests (16 significant before correction, 9 after), while the Section 8 Limitations bullet calls it a 'family of eighteen tests' while pointing at Section 6.6 (pinned v1 text, read 2026-09-25)."
  - "Section 6.2 presents the unexplained-alarm comparison as 'Computed for every metric' (TSI 4.0% / effective rank 14.7% / effective rank on returns 58.5% / Absorption Ratio 59.4%), while the Section 6.3 caveat states the same quantity was 'not computed ... for the Absorption Ratio or for the spectral baselines'. The same pinned version contradicts itself on whether that comparison exists (read 2026-09-25)."
---

# Triadic Stress Index (TSI) correlation-network stress-state risk overlay

## Provenance

- **Paper**: Alberto Acedo (sole author; affiliation printed on the paper as Biome Makers Inc., acedo@biomemakers.com), *The Triadic Stress Index in Financial Markets*, `arXiv:2608.10788v1 [physics.soc-ph]`, cross-listed to `q-fin.RM` and `q-fin.ST`.
- **Version/date**: only `v1`, submitted 11 Aug 2026 10:47:57 UTC (arXiv API `published` field); `v2` returns **HTTP 404** (checked 2026-09-25). arXiv Comments field reads `21 pages, 3 figures. Cross-list to q-fin.RM and q-fin.ST. Code and data: https://github.com/BiomeMakers/TSI-OmegaS`. **No `journal_ref`, no journal DOI in the arXiv API record, no peer-review statement → preprint only.**
- **DOI**: DataCite `10.48550/arXiv.2608.10788` → HTTP 302 → `https://arxiv.org/abs/2608.10788` (checked 2026-09-25).
- **Licence**: paper licensed **CC BY-NC-ND 4.0** (licence link on the abs page) → this record cites and normalises short claims only; no reproduction of the text.
- **Pinned primary source**: v1 HTML, **246,627 bytes, SHA-256 `82beb8205757769e08e42bc4287e2c0c23ad999864f848d4eacb547eb9b5f9b2`**, converted to 78,592 bytes / 1,491 lines and **read end to end on 2026-09-25** (Abstract, Sections 1–10, Tables 1–2, figure captions, References, licence footer).
- **Code/data**: `https://github.com/BiomeMakers/TSI-OmegaS` at **commit `01948247d129cd2860203e44d6ea5df61751bb30`** (main HEAD, verified live 2026-09-25; author Alberto Acedo, 2026-09-23T09:09:11Z, message "Add off-balance-sheet guarantees note, data and extractor"). Validation scripts exist at `code/validation/samefilter_benchmarks.py`, `code/validation/block_bootstrap_significance.py`, `code/validation/multiple_comparisons.py`, `code/validation/leadlag_analysis.py`, `code/validation/balance_saturation_sp500.py`. **The repo HEAD postdates paper v1 by about six weeks and the paper pins no commit → moving target; any replication must pin its own SHA.**
- **Repo licence**: dual **AGPL-3.0 OR commercial** (Copyright 2026 Biome Makers Inc., `LICENSE` in repo).
- **Companion theory**: reference [1] of the paper points to `https://github.com/BiomeMakers/OmegaS-fsri` (FSRI framework preprint), which fixes the original composition with `Coex` in the denominator.
- **Declared interest**: "The author declares no competing financial interests beyond patent applications filed by Biome Makers Inc. relating to the index described here" (References footer); patent cited as US 2022/0268756 A1.
- **Source's own negative-evidence folder**: `explorations/README.md` opens with "Nothing in this folder is claimed by the preprint" and inventories seven pre-registered tests that were closed.

## Economic mechanism

### Source-reported

The index is transplanted without alteration from soil-microbiome co-occurrence network analysis: four factors (clustering, density, modularity, degree variance) that separate managed from undisturbed soil communities are computed on the **correlation network of financial assets** and read as **structural concentration** — a few nodes accumulating the interactions the rest lose. The author links this to Minsky-style fragility built up in plain sight, and deliberately **reverses the ecological orientation**: in a market, correlations rise together under stress, so the network becomes denser, more weakly modular and more degree-dispersed, therefore `Coex` (degree-sequence variance) moves from the denominator (framework Definition 1) to the numerator in `TSI = (C·D/M)·Coex` (paper §3.1, eq. 1). The orientation choice is not just argued: §3.1 reports F1 0.275 for eq. (1) against 0.157 for the Definition-1 composition (chance 0.152) on the 2006–2011 bank portfolio, with a paired block-bootstrap difference of +0.054 and CI [−0.229, +0.315] (directional, not conclusive). The register is explicit and repeatedly restated: TSI is a **coincident state index, not a forecast** (§6.7), and §9 states "Everything in this paper is a backtest of a state reading", with allocation explicitly left as a different exercise.

### Research interpretation

Hypothesis (falsifiable form): **systemic stress episodes are accompanied by a measurable rise in correlation-network concentration** (triadic closure `Tr(A³)`, density and degree variance up; inverse spectral gap down), so a frozen composite of those four quantities can serve as a *regime/state overlay* that identifies windows in which cross-sectional co-movement is unusually concentrated, plus a per-node read of which asset carries the concentration. Component roles if ever operationalised: **Regime/state = filtered TSI level (source-reported state reading); Primary predictive signal = none — the source demonstrates no leading power (source-reported null); Attribution = per-node `diag(A³)` (source-reported, but §8 shows it degenerates to node degree on real matrices); Trade trigger / sizing / exit = absent from the source and therefore entirely `research-proposed`.** Competing explanation to be tested rather than assumed: the source's own Gini-normalised variant scores 0.098, below chance (§3.1), which the author reads as "a substantial part of what TSI detects in this setting is the level of correlation rather than the shape of its distribution" — i.e. the composite may be an expensive proxy for mean absolute correlation.

## Signal

All items below are `source-reported` unless marked otherwise.

- **Formation timestamp**: rolling window of **20 trading days of daily log-returns**, recomputed **every 3 days** (Table 1 caption: "All windows: 20 trading days, recomputed every 3 days."). Windows are exchange trading days from yfinance/OFR daily series; timezone/session convention beyond "trading days" is `not stated in source`.
- **Index construction**: `A = |ρ|` with zero diagonal from the window correlation matrix `ρ`; `TSI = (C·D/M)·Coex` where C = weighted clustering (normalised `Tr(A³)`), D = connection density, M = inverse spectral gap of the graph Laplacian (modularity proxy), Coex = variance of the degree sequence (§3.1 eq. 1). No free parameter in the index itself.
- **Persistence memory filter** (eqs. 2–3): asymmetric exponential filter, **α↑ = 0.6** when TSI rises, **α↓ = 0.08** when it falls; "chosen by inspection and later validated by grid search" (§5.2). Grid: α↑∈[0.3, 0.8], α↓∈[0.02, 0.20], train 2000–2015 / test 2016–2026 on the OFR Financial Stress Index series; in-sample vs out-of-sample F1 correlation across the 36 combinations = **0.96**, optimum α↓ = 0.08 robust for α↑∈[0.5, 0.7] (§5.3, §6.3).
- **Alarm threshold**: **90th percentile of each series = a fixed 10% alarm budget**; `code/validation/samefilter_benchmarks.py` verifies every compared series flags exactly 10.0% of windows at that percentile (§6.13 methodological note).
- **Per-node attribution**: `diag(A³)` — the alarm read per node instead of summed, with **no k to select** (§6.1). On real data §8 shows it reduces to the node degree (rank correlation 0.996, cubic in degree explains R² = 0.992 of the triangle count across 245 windows of 464 S&P 500 constituents).
- **Raw-magnitude caveat**: because C, D, M and Coex scale differently with `n`, raw TSI levels are **not comparable across networks of different size**; only within-series z-scores/percentiles are (§3.1).
- **Tradeable rule**: **none exists in the source.** Entry, exit, direction, holding period, re-entry, sizing, stop and instrument are `not stated in source`; the paper explicitly declines to supply an allocation rule (§9). Any de-risk/derisk gate built on the 90th-percentile alarm is **`research-proposed`**.

## Required data

Source-reported (Table 1, plus §6.13):

| Scenario | Universe | Period | Source |
|---|---|---|---|
| Banking crises (Bear Stearns, Lehman, European debt) | 10 banks | 2006–2011 | yfinance |
| AI sector | 11 stocks | 2021–2026 | yfinance |
| Out-of-sample calibration | 8 OFR components | 2000–2026 | OFR |
| Large-network robustness | 42 stocks, 7 sectors | 2006–2026 | yfinance |
| Cross-market (crypto, FX, commodities, sovereign debt) | 10 + 7 + 10 + 10 assets | 2021–2024 | yfinance |
| Balance-index head-to-head / attribution limitation | 447 then 464 S&P 500 constituents (245 windows) | ten-year panel | S&P 500 panels (repo scripts) |

- **Fields needed**: daily adjusted/unadjusted closes for the panel (log returns), the OFR Financial Stress Index components for calibration and lead–lag, and a documented crisis-episode label list. No order book, trades, funding, open interest, options or on-chain field is used.
- **Ground truth**: **three manually curated crisis lists** that are not identical (§6.3): a 16-episode narrow list (hyperparameter calibration), a 23-window wide list (every F1 figure in §§6.2/6.4), and a 25-episode list (unexplained-alarm accounting). The paper itself warns that precision/recall/unexplained-alarm figures do not come from the same list as the F1 figures (§8).
- **Point-in-time**: `data gap` — no publication-lag or vintage treatment is described for yfinance/OFR inputs; labels are retrospective episode definitions.
- **Missing-data handling**: `not stated in source`.
- **Timeframe/session**: daily bars on exchange trading days; the crypto panel in §6.10 is likewise read on that convention (`data gap` for 24/7 session boundaries).

## Execution assumptions

Cost/fill determination was made from Methods-level reading of §3 (construction), §5 (Data and Protocol), §6 (Results), §7 (Discussion), §8 (Limitations), §9 (Where This Stands) plus a word-boundary scan of the pinned v1 text (78,592 bytes): `transaction cost` 0, `trading cost` 0, `slippage` 0, `bid-ask` 0, `sharpe` 0, `turnover` 0, `commission` 0, `fee/fees` 0, `rebalance` 0, `drawdown` 0, `borrow` 0, `capacity` 0, `latency` 0, `hedge` 0, `market impact` 0, `position size` 0, `risk-free` 0; the single `spread` hit is "the spread between those three [selection rules]", the single `trading` hit is "20 trading days", the `backtest`/`allocation` hits are the §9 sentence declining to build a rule, `portfolio` appears 3 times in descriptive context, and `alpha` never appears as an excess-return term.

Consequently **every execution field is `data gap`, never zero**: order type, fill model, signal-to-order delay, next-bar vs same-bar convention, fees, spread, slippage, impact, participation/capacity, leverage/margin, borrow/short availability, funding and failure handling are all `not stated in source`, and **no number anywhere in the source is net of cost**. Signal-to-order timing, if this state reading were ever wired to a risk overlay, is **`research-proposed`** (e.g. act at the next session open after the 3-day recompute); nothing in the source specifies it.

## Evidence

### Source-reported

All figures below are third-party claims from the pinned v1 (2026-08-11) or from the pinned repo commit; none is net of transaction costs (the source models no costs).

- **Like-for-like spectral benchmark, §6.2 table, out of sample 2016–2026 (897 windows), F1@p90, filtered column**: TSI **0.447** (raw 0.367); effective rank (correlation) **0.377**, Δ +0.038, 95% CI [−0.010, +0.111] → **tie**; Vendi score **0.377**, Δ +0.037 [−0.009, +0.104] → **tie**; Absorption Ratio **0.134**, Δ +0.219 [+0.070, +0.410], p<0.0005 → **TSI wins**; effective rank on returns **0.174**, Δ +0.227 [+0.097, +0.393], p<0.0005 → TSI wins. Raw reading: TSI leads effective rank by only 0.020 with an interval containing zero.
- **Significance, §6.4**: F1 gap **0.273** (0.447 vs 0.174), block bootstrap B = 2,000, block ≈ 1 quarter, **95% CI [0.095, 0.392]**, one-sided **p < 0.0005**. Author's own caveat: the metric rewards sustained plateaus, which is exactly what the memory filter was built to produce — the test confirms the filter meets its design goal, not independent superiority.
- **Full history 2000–2026 (2,232 windows), §6.2**: filtered TSI **0.389** vs effective rank **0.342** (tie, p = 0.07) vs Absorption Ratio **0.175** (p < 0.0005).
- **Label sensitivity, §6.2 second table**: the tie with effective rank holds in **all six** sample×label cells (TSI ahead in five; the sixth favours effective rank by 0.023, p = 0.59); the win over the Absorption Ratio **disappears under the narrowest (16-episode) list** where gaps +0.170 / +0.121 have intervals touching zero.
- **Alarm quality, §6.2 (25-episode list, full history, all series filtered, top-decile budget)**: TSI **4.0% (9 of 224)** unexplained, effective rank and Vendi **14.7% (33)**, effective rank on returns **58.5% (131)**, Absorption Ratio **59.4% (133)**; out of sample **3.3% / 17.8% / 61.1% / 71.1%**. Author's qualification: at a fixed alarm budget this is `1 − precision`, i.e. the same comparison re-expressed, so it is not independent evidence.
- **Precision/recall, §6.3**: 16-episode list out of sample **69% precision / 32% recall**; 23-window list out of sample **precision 1.00, recall 0.29 (90 alarms, none outside a labelled window)**; 25-episode full history **9 of 224 alarms unexplained = 4.0%** (explicitly not out of sample).
- **Multiplicity, §6.6**: family = 4 baselines × 2 samples × 3 labellings = **24 tests**, Holm–Bonferroni FWER 0.05; **16 significant before correction, 9 after**; the six effective-rank comparisons are ties before and after; three lost results all sit on the narrow 16-episode labelling.
- **Ollivier–Ricci head-to-head, §6.5**: TSI ahead in all six cells — OOS ΔF1 +0.126 / +0.087 / +0.101 (p 0.011 / 0.007 / 0.003), full history +0.023 / +0.074 / +0.073 (p 0.388 / 0.018 / 0.023) — but **only one of the five nominally significant cells survives the §6.6 correction**.
- **Lead–lag, §6.7** (OFR Financial Stress Index, lags k ∈ [−15, +30], each step ≈ 3 business days, n = 2,232): TSI raw peaks at **k = 0, ρ = +0.203**; TSI with memory at **k = −2, ρ = +0.195**; Absorption Ratio at **k = −15, ρ = +0.063**. In first differences ΔTSI raw peaks at **k = 0, ρ = +0.094**, and at k = +1 the correlation is −0.009 / +0.008 against a ±0.041 threshold → **coincident, not leading**.
- **Synthetic attribution, §6.1** (120 simulations per regime, 16 nodes, 40-observation windows; top-|epicentres| hit rate): `diag(A³)` **0.994 / 0.978 / 0.980 / 0.975** for 1–4 epicentres; node degree **0.933 / 0.940 / 0.952 / 0.961**; fixed k = 2 **0.756 / 0.999 / 0.946 / 0.948**; Marchenko–Pastur rule **0.997 / 0.978 / 0.962 / 0.959 (ties the triangle rule)**; Kaiser rule **0.000 / 0.071 / 0.457 / 0.808**; oracle **0.989 / 0.999 / 0.981 / 0.989**. Local balance index **0.329 / 0.552 / 0.724 / 0.841** vs triangle rule **0.992 / 0.996 / 0.972 / 0.966** (chance 0.188–0.750).
- **Large-network behaviour, §6.9 Table 2 (42-asset, 7-sector, ending z-scores)**: Bear Stearns −0.28 / −0.42 / −0.26 / −0.12, Lehman 0.10 / 1.20 / 1.27 / **2.61**, European debt −1.09 / 2.18 / **5.35** / 2.13 across Financials / Tech / Diverse / Full baskets; COVID z = 1.35 (Feb–Apr 2020); 2022 rate-hike selloff z = 1.41 (Jan–Oct 2022). A basket concentrated on the crisis epicentre **forgets** (z below its own mean mid-crisis); diversified baskets do not.
- **Cross-market, §6.10**: crypto all-time peak **z = 3.9 in May–June 2022 (Terra/Luna collapse)** with MATIC-USD flagged as most-connected; sovereign debt peak **z = 3.6 (Aug–Dec 2023)** with MBB flagged. Negative scope cases: September 2022 GBP/gilt crisis (memory-TSI negative throughout) and the 2022 Ukraine invasion (~3-month lag).
- **Composition ablation, §3.1**: eq. (1) composition F1 **0.275** vs Definition-1 composition **0.157** vs chance **0.152** (CI on the paired difference [−0.229, +0.315]); the framework's shape-normalised **Gini variant scores 0.098, below chance**.
- **Signed channel null, §6.13**: replacing `Tr(A³)` with `Tr(ρ³)` gives correlation **1.000** across all 2,232 windows and ΔF1 **0.000** (95% CI [−0.005, +0.005]) → signing the correlation does not rescue the single-asset blind spot. Balance index on 8-node networks saturates at κ = 1 on **26% (weighted) / 70% (binary)** of 20-day windows; on 464 S&P 500 constituents saturation disappears (≤2.0% of windows) and the head-to-head is a **tie** (TSI F1 0.160–0.161 vs balance index 0.184–0.187, chance ≈ 0.14), and the Absorption Ratio cannot be scored there at all (60-day window, 464 assets → covariance rank 59, top n/5 = 93 components capture the whole trace → ratio identically 1).
- **Persistent homology, §6.12**: correlation-network H1 is a **negative result** (mean 0.03–0.07, crisis vs calm indistinguishable); Takens-embedding H1 peaks 30 Mar 2020 at ~12σ above the historical mean (0.104 ± 0.110), with 15 of the 20 highest readings inside documented crises.
- **Real-matrix attribution collapse, §8**: `diag(A³)` vs degree rank correlation **0.996**, cubic R² **0.992**; the residual has rank correlation **+0.002** with forward 5-day returns (bootstrap interval spanning zero) and its forward-volatility association **+0.187 → +0.016 [−0.003, +0.035]** once current volatility is partialled out → "a practitioner should use the degree, which costs one matrix row-sum".

### Independently reproduced

not independently reproduced.

### Negative evidence

Led by the source's own closed-experiment folder (`explorations/README.md` at the pinned commit; seven pre-registered tests, "the answer ... is no"):

1. **No investment rule survives**: `investment_rule_headtohead.py` — neither index beats 1/N over 5 days; `esx_*` — balance rule works in sample, fails out of sample, and honest calibration removes it; `sp500_headtohead.py` reports +1.6% out-of-sample excess with p = 0.005 (2012–2017, 447 assets) but **`sp500_10y.py` on 10 years / 464 assets changes sign between halves — the README forbids quoting the first without the second**; `crypto_headtohead.py` (18 crypto assets) — the balance rule is undefined there and "ours adds nothing"; `exposure_rule.py` — exposure sizing **ties volatility targeting and correlates 0.85 with it**; `euro_backtest.py` — apparent edge vanishes with more independent windows.
2. **Forecasting/scenario line also closed**: `structure_forecast.py` — no next-month correlation-structure prediction beyond persistence; `scenario_generality.py` — fails on dollar-neutral books where the EWMA Gaussian default passes; `corr_forecast_rival.py` — DCC beats persistence by 9–13%; `shrinkage_target.py` — triadic covariance target OOS GMV realised vol **13.68% vs 12.27% constant-correlation, 11.66% Ledoit–Wolf nonlinear, 11.33% scaled identity** (464 assets, p/T = 0.93, comparison tilted toward the triadic target, and it still lost).
3. **The shape claim fails its own ablation**: Gini-normalised variant scores 0.098, below chance (§3.1) — a substantial part of what TSI detects may be the *level* of correlation, not its distribution shape.
4. **No detection advantage over a sharpened spectral baseline**: six-cell tie with the effective rank survives all three labellings and the Holm correction; the author states the Absorption Ratio win is "largely explained by the AR being a weak baseline (F1 ≈ 0.17–0.19, roughly half of every other measure tested), not by TSI accessing information the spectrum lacks".
5. **The headline win is labelling-dependent and correction-dependent**: the AR victory disappears under the narrowest list, and 16/24 → 9/24 survive Holm (§6.6); §8 simultaneously mis-states the family as eighteen tests (frontmatter `contradictions`).
6. **Coincident, not leading** (§6.7): any de-risk overlay inherits the stress only when it is already present; at k = +1 the differenced correlation is inside the noise band.
7. **Forgetting behaviour**: raw TSI collapses to negative z inside its own crisis when the basket is concentrated on the epicentre (§6.8/§6.9, Table 2), repaired only by the fitted memory filter.
8. **Scope boundaries**: GBP/gilt crisis undetected (memory-TSI negative throughout), Ukraine invasion lagged ~3 months (§6.10); TSI reads correlation-structure breaks, not directional price events.
9. **Short-series recalibration failed** (§6.11): with 5-year / 2–3-episode series the ground-truth list definition dominates the hyperparameters.
10. **Attribution advantage does not survive real data** (§8): it is exactly equal to a well-chosen adaptive-k rule in synthetic tests and reduces to node degree on real matrices, with the residual carrying no forward-return content.
11. **Significance test is aimed at its own design target** (§8): the bootstrap evaluates the memory filter against the exact objective it was built for.
12. **Ground-truth hygiene**: three inconsistent manual label lists, every headline number attached to a different one (§6.3, §8).
13. **Design-level limits**: single 42-asset large-network test, single Takens embedding parameter set, no formal pre-registration (the paper says only "criteria fixed before the corresponding experiments were run").
14. **Source quality**: preprint only, sole author, yfinance data, manual episode labels, declared patent interest, repo HEAD not pinned by the paper, repo code dual-licensed AGPL-3.0/commercial.
15. **No trading layer of any kind** (word-boundary scan above): zero cost, fill, borrow, capacity, turnover or P&L model, therefore nothing in the record is net of cost and no profitability claim exists to evaluate.

## Falsification plan

Every threshold below is **`research-defined` (falsification cutoff) or `research-proposed` (operationalisation)** — none is source-reported. Failure action for any test: the hypothesis is downgraded in our research notes and the record is not eligible to advance beyond research-only.

- **F1 — Point-in-time detection replication (`research-defined`)**: rebuild the 20-trading-day / 3-day-recompute pipeline with α↑ = 0.6, α↓ = 0.08 and the 90th-percentile budget frozen before evaluation, on a point-in-time universe and label set. Out-of-sample F1@p90 must be **≥ 0.40** and the paired block-bootstrap CI of the gap vs effective rank must not be strictly negative. Failing either → detection claim not reproduced.
- **F2 — "Not just correlation level" ablation (`research-defined`)**: compete TSI against mean-|ρ| and a Gini-normalised variant on the same windows. If mean-|ρ| matches TSI (F1 gap CI contains 0) the composite is redundant as a *shape* measure; expected outcome is high risk because the source's own Gini variant scored 0.098 (§3.1).
- **F3 — Equal-budget baseline horse race (`research-defined`)**: same windows, same filter, same alarm budget, baselines = effective rank, Marchenko–Pastur spectral rule, Ollivier–Ricci curvature. If effective rank leads by **≥ 0.05 F1 with a CI excluding 0**, H1 fails as stated.
- **F4 — Costed risk-off overlay (`research-defined`, `research-proposed` gate)**: gate = reduce exposure when filtered TSI ≥ its 90th percentile (research-proposed; the source supplies no rule), tested at **0 / 5 / 10 / 20 / 30 bp per side, 20% ADV participation, plus 50 bp/yr stock-loan**. Failure if at 10 bp/side net excess return ≤ 0 or net Sharpe improvement ≤ 0. The source's own `exposure_rule.py` ties volatility targeting with ρ = 0.85, so prior risk of failure is high.
- **F5 — Placebo (`research-defined`)**: 1,000 circular-shift (and 1,000 block-shuffle) realisations of the label series; the observed F1@p90 must exceed the **95th percentile** of the placebo distribution.
- **F6 — Label robustness (`research-defined`)**: rebuild all three crisis lists point-in-time with a written inclusion rule; if F1@p90 falls below **0.35** or the ranking vs baselines flips under any single list, the result is declared label-driven.
- **F7 — Regime/venue transport (`research-defined`)**: rerun frozen parameters on (a) a non-US equity panel, (b) a crypto perp panel, (c) a multi-asset panel. Failing **two of three** → no transport claim.
- **F8 — Multiplicity (`research-defined`)**: pre-register the full comparison family and require **Benjamini–Hochberg q < 0.10** for every claimed win; a win that vanishes after correction is recorded as a tie.
- **F9 — Epicentre-forgetting failure rule (`research-defined`)**: on a basket concentrated in the crisis epicentre, filtered z must stay **> 0** through the labelled episode; a negative z inside the episode (the §6.9 pattern) counts as a failure of the raw index and bounds any overlay built on it.

## Crypto portability

**`adapted`** — the source itself measures TSI on a 10-year cross-market crypto panel (§6.10: historical peak z = 3.9 in May–June 2022 during the Terra/Luna collapse with MATIC-USD flagged; §6.10 crypto row of Table 1, 10 crypto assets, 2021–2024), so **the state reading is source-demonstrated in crypto**. What is *not* demonstrated anywhere, in any market, is turning that reading into a gate, a position or a return stream (§9). Crypto-specific porting risks: the 20-day/3-day window and the 10% alarm budget were derived on exchange-traded daily equity/OFR series and are not re-derived for crypto; 24/7 sessions make "trading day" candle boundaries and the 3-day recompute cadence ambiguous (`data gap`); funding, mark/index price, liquidation cascades and liquidation-driven co-movement are absent from a source that models no trading costs at all; venue fragmentation (spot vs perp across exchanges) changes the correlation matrix itself; the 10-asset crypto cross-section is far narrower than real top-coin breadth, and top-coin returns are beta-dominated, which mechanically raises mean |ρ| and can saturate the concentration read. `direct` is not warranted for any *trading* use; `adapted` covers only the index-as-state-reading.

## Limitations

- `not independently reproduced` — no replication by us; no Qlib, Paper, Testnet or Live evidence exists.
- `data gap` — transaction costs, slippage, spread, fees, borrow, funding, leverage, capacity, fill model, order timing, position sizing and P&L are entirely absent from the source; nothing is net of cost.
- `data gap` — point-in-time/vintage handling of yfinance and OFR inputs, missing-data rules and timezone/session conventions are not stated.
- `underspecified` — no tradeable rule exists in the source; any entry/exit/sizing rule built on this record is `research-proposed`.
- Preprint only (arXiv v1, sole author, no peer review), with a declared patent interest and a repo whose HEAD is six weeks newer than the pinned paper and unpinned by it.
- Ground truth is three inconsistent hand-curated label lists; every headline number is attached to a different one, and the paper warns against quoting precision/recall together with F1.
- Detection advantage over the sharpest spectral baseline is a **tie**, not a win; the advantage over the Absorption Ratio is labelling-dependent and its own explanation is baseline weakness.
- Attribution is a tie against a well-chosen adaptive-k spectral rule in synthetic tests and collapses to node degree on real matrices; the residual carries no forward-return information.
- Coincident register (§6.7) means no leading power has been shown; the single tradable claim class (a de-risk gate) is untested anywhere.
- Two internal source contradictions are recorded in frontmatter `contradictions` (family size 24 vs 18; alarm-quality computed vs not computed).
- `unproven` — any profitability, Sharpe, drawdown, turnover or capacity figure, because the source reports none.

## Implementation status

`not-implemented`. No implementation exists in our research stack: no signal pipeline, no backtest, no production card, no Qlib full-backtest validation, and no Paper, Testnet or Live run. The source's code exists in its own repository (pinned above) but has not been executed by us; the source's own `explorations/` folder reports that its investment and forecasting lines were tested and closed.

## Adoption boundary

Presence of this record means only a normalised research capture in a public staging pool. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

- `[[quant/spectral-graph-topological-crash-rally-detection-correlation-network-2026-09-04]]` — the only Wiki Brain page returned (score 76) by the read-only query "absorption ratio correlation network crisis detection regime" on 2026-09-25; read-only search for "Triadic Stress Index correlation network systemic stress" and "systemic stress network concentration correlation regime risk overlay crypto" both returned 0 results. No Wiki page was written by this Scout.

Adjacent records already in this repository, with the four-axis distinction (mechanism / signal construction / universe / horizon) that keeps them independent:

- `spectral-graph-topological-crash-rally-detection-correlation-network-2026-09-04.md` ("ORCA") — mechanism: supervised crash/rally detection from spectral + graph features; ours: an unsupervised fixed composite state index with no training step. Signal construction differs (learned classifier thresholds vs a closed-form four-factor trace); horizon differs (event/rally detection vs a coincident 20-day state read).
- `geometric-observables-qcml-regime-detection-berry-phase-rate-2026-09-20.md` (QCML Berry Phase Rate) — mechanism: quantum-machine geometric phase rate as a regime feature; ours: triangle-count/density/modularity/degree-variance topology. Signal construction and data dependency differ entirely (learned quantum kernel observables vs correlation-matrix graph invariants).
- `cross-asset-reconfiguration-premium-subdominant-eigenspace-vrp-2026-09-02.md` (Reconfiguration Premium) — mechanism: priced risk premium from subdominant-eigenspace rotation, i.e. a cross-sectional return claim; ours: a systemic-stress *state* read with an explicit no-return claim (§9). Horizon/regime differs (persistent premium vs episodic stress alarm).
- `cryptocurrency-correlation-network-consensus-clustering-mpt-2026-09-17.md` (crypto consensus clustering) — mechanism: portfolio construction via stable correlation clustering with return forecasting; ours: no clustering, no forecast, no weights — a scalar stress index plus per-node attribution. Universe overlaps (crypto panel) but signal construction and purpose differ.

## Sources

- Acedo, A. (2026). *The Triadic Stress Index in Financial Markets*. arXiv:2608.10788v1 [physics.soc-ph]; cross-list q-fin.RM, q-fin.ST. https://arxiv.org/abs/2608.10788 — pinned v1 HTML 246,627 bytes, SHA-256 `82beb8205757769e08e42bc4287e2c0c23ad999864f848d4eacb547eb9b5f9b2`, read end to end 2026-09-25 (§§1–10, Tables 1–2, References, CC BY-NC-ND 4.0 licence footer).
- DataCite DOI record: https://doi.org/10.48550/arXiv.2608.10788 (302 → abs page, checked 2026-09-25; no publisher DOI, no journal-ref).
- Code and data: https://github.com/BiomeMakers/TSI-OmegaS at commit `01948247d129cd2860203e44d6ea5df61751bb30` (main HEAD verified live 2026-09-25; dual AGPL-3.0/commercial licence).
- Source's closed-experiment inventory: https://github.com/BiomeMakers/TSI-OmegaS/blob/01948247d129cd2860203e44d6ea5df61751bb30/explorations/README.md (read 2026-09-25).
- Companion framework cited by the paper (not read as a primary source for this record): https://github.com/BiomeMakers/OmegaS-fsri (paper reference [1]).
