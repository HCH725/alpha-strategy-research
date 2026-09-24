---
schema: strategy-research-record-v1
title: ML Term-Structure Forecast → Active Duration Timing on Government Bond Portfolios (US Treasury & ECB AAA Euro)
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-06-25
sources:
  - https://arxiv.org/abs/2606.26815
  - https://arxiv.org/html/2606.26815v1
  - https://doi.org/10.48550/arXiv.2606.26815
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Source-internal unreconciled start date for the US test/period-1 window: Section 3.3 and Section 4.1 prose print the hold-out/test period and P1 as starting December 2014, while Supplementary Figure 3.1 and Table 4.1 captions print the same windows as starting July 2014 (all checked against pinned arXiv:2606.26815v1 HTML, 2026-09-24). The July-vs-December 2014 gap (~5 months) is printed twice each way and never reconciled; it does not change model ordering but does change window definition."
---

# ML Term-Structure Forecast → Active Duration Timing on Government Bond Portfolios (US Treasury & ECB AAA Euro)

## Provenance

- Primary source: arXiv:2606.26815, "Data-Driven Duration Management -- Term Structure Forecasting Using Machine Learning".
- Authors (exactly three, per arXiv abs-page `citation_author` metadata, checked 2026-09-24): Tobias Lausser; Joao Eduardo Vuolo; Rudi Zagst. Printed affiliations/emails do not appear anywhere in the retrieved v1 HTML → data gap.
- Version/date: single version `[v1] Thu, 25 Jun 2026 09:58:28 UTC (14,119 KB)`, sole submitter Tobias Lausser; HTML header prints `arXiv:2606.26815v1 [q-fin.PM] 25 Jun 2026`; `citation_date` 2026/06/25.
- Primary category q-fin.PM (cross q-fin.CP, stat.ML). No Comments field, no Journal-ref, no publisher DOI beyond arXiv/DataCite → preprint only, peer-review status not stated in source.
- License: arXiv.org perpetual non-exclusive license (abs page). DataCite DOI `10.48550/arXiv.2606.26815` resolves (HTTP 200 → abs page) when checked 2026-09-24.
- Full text read from pinned v1 HTML `https://arxiv.org/html/2606.26815v1` (948,211 bytes fetched 2026-09-24), containing Sections 1–5, Appendix A, References, and the Supplementary Document (hyperparameter tables, whole-period and periodic evaluations). Rendering note: the v1 HTML `<title>`/first section heading prints "Supplementary Document: Data-Driven Duration Management" while the main paper body is rendered later in the same document (title block at body line "Data-Driven Duration Management: Term Structure Forecasting Using Machine Learning"); recorded as a rendering artifact, not a second document.
- Funding: "The authors have nothing to report." Conflicts of Interest: none declared. Data Availability Statement: FRED (https://fred.stlouisfed.org/) and ECB (https://data.ecb.europa.eu/data/datasets) openly available; LSEG/Datastream "Restrictions apply … used under license". No code, repository, or replication-package statement anywhere in v1 (GitHub/code/replication keyword scan: only arXiv chrome text hits) → not independently reproduced.
- Repo-wide source-identity dedup (2026-09-24): ripgrep across all 2,513 `*.md` files (including `.mimo-worktrees`/hidden trees) plus `coverage_manifest.csv` (5,808 lines) for `2606.26815`, the DataCite DOI, `Data-Driven Duration Management`, `Lausser`, `Vuolo`, `Zagst` → **zero hits**. Mechanism-level search for `Nelson-Siegel`/`Nelson Siegel`/`AFNS`/`duration management`/`term structure forecast`/`zero-rate` → only 1 unrelated hit (`dynamic-portfolio-optimization-cvar-stochastic-control-hjb-2026-09-02.md`, a CVaR solvency paper using "zero-rate calibrations", different mechanism, not a yield-curve trading record). Wiki Brain `kb_search` (2026-09-24): "yield curve forecasting duration timing bond portfolio" → 0 results; "neural network interest rate forecast bond trading" → 2 adjacent pages (`quant/foreign-exchange-spatiotemporal-graph-statistical-arbitrage-2026-09-02.md`, `quant/cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02.md`) used only as retrieval hooks; no Wiki page corresponds to this mechanism and none is asserted.
- Four-axis distinction from nearest existing captures: vs the FX graph-StatArb and cross-asset portfolio-transformer Wiki pages (different asset class, different signal family); vs SSRN/carry-gap and equity-premium records (no term-structure duration channel); this is the repository's first yield-curve/term-structure duration-timing family.

## Economic mechanism

### Source-reported

The source frames the strategy as forecast-driven duration management: forecast the zero-rate (yield) curve four weeks ahead, translate the forecast into a target portfolio duration, and mix two assets (a 1-month T-bill as risk-free leg and a 10-year bond index as duration leg) to hit that target. The stated intuition (Section 3.1): duration is first-order price sensitivity to yields, so an investor should lengthen duration when yields are expected to fall and shorten it when yields are expected to rise. NN forecasts are claimed to capture nonlinearities and regime shifts (e.g., the 2022 hiking cycle) that AR/VF-style benchmarks miss: traditional PCA+AR/VAR forecasts "largely resemble a rightward shift of the current curve, suggesting a persistent lag" and "fail to provide actionable investment signals" (Section 4.2). The claimed alpha channel is therefore improved directional timing of interest-rate exposure relative to a constant-duration passive benchmark, not cross-sectional selection.

### Research interpretation

Hypothesized mechanism in falsifiable terms: the level/slope/curvature dynamics of the government yield curve contain short-horizon (1-month) predictability that nonlinear learners (NN on DNS/PCA/AFNS factors, optionally augmented with lagged macro factors) can extract better than linear factor+AR/VAR models; if that directional edge is real, active duration timing should deliver positive active return (and better downside profile) versus a constant 5-year-duration benchmark after paying realistic turnover costs. Roles of components: (a) regime/timing input = predicted 4-week change in the par/zero curve; (b) primary signal = model-specific forecast feeding a progressive duration adjustment; (c) implementation = two-asset mix with duration bounds [2.5, 7.5] and no short selling; (d) evaluation = IR, Omega, relative MDD plus forecast RMSE/MAE/directional accuracy. Alternative/friction explanations the source itself raises or that remain open: the edge may be a duration-bounds/trading-band effect, a sample-specific macro-regime fit, or may vanish net of weekly rebalancing costs (no cost model exists in the source); ablation of each component is not performed by the source.

## Signal

Source-reported elements (all from pinned v1):

- Forecast target: one-month (4-week) ahead changes in the zero-rate curve across 7 maturities (3M, 6M, 1Y, 2Y, 3Y, 5Y, 10Y); signal updated weekly.
- Curve construction: par yields derived from the predicted zero-coupon curve via the printed par-yield formula; linear interpolation between adjacent zero maturities for intermediate points.
- Positioning rule: "proprietary duration management strategy" that "progressively adjusts the portfolio's duration based on the strength of the forecast" (stronger predicted rate decline → larger duration increase, and symmetrically for rises), with "lower and upper limits" — duration bounds [2.5, 7.5] and non-negative weights (no short selling) are printed; the exact forecast→target-duration mapping function, its slope/sensitivity, and its calibration are NOT printed → **underspecified** (proprietary).
- Instruments: US = 1-month US Treasury Bill + "U.S. 10-year total return benchmark" index; Europe = 1-month German Treasury Bill + ICE BofA 10+ Year AAA Euro Government Index. Two assets suffice to hit any target duration within bounds.
- Benchmark for evaluation: passive constant 5-year duration portfolio.
- Rebalance cadence: weekly signal update; forecast horizon 4 weeks (source gives no explicit holding-period or overlap rule beyond this → partially underspecified).
- Models: 43 candidate architectures (Appendix Table A1) spanning DNS/PCA/AFNS/AE compression × AR/VAR/factor-NN/direct-NN × macro settings N/A–F; final picks: US B31 (AFNS factors + AE-compressed macro setting B, direct NN) and Europe N16 (PCA factors, factor-prediction NN, no macro). Training: global re-fit every 104 weeks from scratch, weekly single-epoch local update; BOHB hyperparameter tuning; RMSprop/MSE; inputs normalized to unit variance; no differencing for NN (citing Kim et al. 2004, Bao et al. 2017).
- Data splits (Section 3.3): initial train Apr 1987 (US) / Feb 1992 (EU) → Jan 2005; validation Jan 2005 → Dec 2014 (hyperparameter tuning only); untouched test Dec 2014 → Feb 2025 (US P1/test-start also printed as July 2014 in Supplementary captions → see frontmatter contradiction).
- Not specified by source → research-proposed for any reconstruction: exact duration-mapping formula, execution timestamp/price (open vs close), order type, tie/simultaneous-signal handling, re-entry and overlap rules, position sizing beyond the two-asset duration mix, cost/slippage assumptions, and all acceptance/failure thresholds below.

## Required data

- Weekly zero-coupon rates for maturities 3M/6M/1Y/2Y/3Y/5Y/10Y: US from FRED + Thomson Reuters DataStream, Apr 1987–Feb 2025; Euro-area AAA government curve from ECB, official series Sep 2004–Feb 2025, extended back to Feb 1992 via an OLS mapping on German Bund zero rates (source-reported fit R² 0.9921–0.9987 across maturities, Table 3) with missing German short maturities imputed by per-date DNS curve fits (Table 2: R² 0.9840/0.9213 for 3M in scenarios i/ii, dropping to 0.5781 (3M)/0.7987 (6M) in the 3-missing scenario, <10% of sample).
- US macro (FRED, monthly, 1-month publication lag then forward-filled weekly): USPRIV, INDPRO, PAYEMS, CPIAUCSL, PPIACO, SPREAD (Moody's BAA−AAA, daily → weekly last). German macro for Europe: EMPDE, INDPRODE, PAYEMSDE, CPIDE, PPIDE (corporate spread excluded, no comparable German series).
- Tradable instruments for implementation: 1-month T-bill (US/German), US 10-year total-return index, ICE BofA 10+ Year AAA Euro Government Index — index levels/returns needed point-in-time.
- Point-in-time requirements: macro lags as printed (source does apply 1-month lag for monthly series); zero-rate vintages/revisions not discussed by source → data gap. LSEG/Datastream portion is license-restricted (source's own data-availability statement).

## Execution assumptions

Source-reported: weekly signal update; long-only two-asset mix; duration clamped to [2.5, 7.5]; benchmark constant 5-year duration; evaluation metrics IR, Omega, relative MDD, plus forecast RMSE/MAE/directional accuracy, annualized where applicable.

Not modeled by source (data gap, verified by full-text keyword scan of pinned v1: `slippage` 0, `bid-ask` 0, `latency` 0, `fees` 0, `commission` 0, `transaction cost` 0, `turnover` 0, `fill` 0, `financing` 0, `leverage` 0, `market impact` 0, `borrow` 0, `capacity` 0; the only `cost` hits are figurative prose, the single `Sharpe` hit is a literature citation to Dunis & Morrison 2007, and `margin`/`drawdown` hits are prose/MDD): order type, execution timing (signal-to-order lag, same-bar vs next-bar), fill model, spread, slippage, fees, turnover, impact/capacity, financing on the T-bill leg, leverage, borrow, latency, partial fills. Weekly duration rebalancing between a T-bill and a 10-year index implies material turnover in rising-rate regimes, but the source prints no turnover figure → turnover and net-of-cost performance are **underspecified**, never zero.

## Evidence

### Source-reported

All figures below are source-reported from pinned arXiv:2606.26815v1 (HTML body Section 4 Tables 8–11; Supplementary Tables 4.1–4.4 and 5.1–5.4), gross (no cost model exists), test period Dec 2014–Feb 2025 (US window also captioned from July 2014, see contradiction), annualized where the caption says so; none independently reproduced.

- Whole test period, Table 8 (RMSE / MAE / directional accuracy % / IR / Ω / relative MDD %): US B27 0.2855 / 0.2034 / 56.71 / 0.22 / 1.10 / −12.36; US N28 0.2841 / 0.2031 / 56.58 / 0.39 / 1.18 / −12.10; US B31 (final pick) 0.2527 / 0.1798 / 56.50 / 0.46 / 1.20 / −12.34; EU N16 (final pick) 0.1901 / 0.1288 / 53.28 / 0.59 / 1.29 / −10.02; EU E18 0.1989 / 0.1336 / 53.28 / 0.36 / 1.17 / −9.23; EU E27 0.2013 / 0.1368 / 53.42 / 0.43 / 1.22 / −9.27. All six positive IR; ranking Tables 9–11 select B31 (US, total score 11) and N16 (EU, total score 11).
- US subperiod returns (Suppl. Tables 4.1–4.4, Ret. / MDD %): P1 (Dec or Jul 2014–Feb 2018) B27 0.78/−7.21, N28 0.77/−7.17, B31 1.36/−7.37, Bench 0.98/−4.92; P2 (Feb 2018–Jul 2021) B27 5.24/−6.89, N28 5.03/−7.17, B31 4.98/−6.88, Bench 4.18/−5.02; P3 (Jul 2021–Nov 2022, hiking) B27 −6.48/−9.51, N28 −5.96/−8.73, B31 −6.43/−9.32, Bench −8.02/−11.50; P4 (Nov 2022–Feb 2025) B27 2.19/−3.55, N28 3.50/−2.02, B31 3.22/−5.46, Bench 3.08/−5.93.
- EU subperiod returns (Suppl. Tables 5.1–5.4): P1 (Dec 2014–Sep 2019) N16 2.26/−7.60, E18 1.64/−5.49, E27 1.85/−5.09, Bench 1.79/−5.45; P2 (Sep 2019–Nov 2021) N16 −1.27/−3.55, E18 −0.93/−2.96, E27 −0.91/−4.74, Bench −0.78/−3.73; P3 (Dec 2021–Oct 2023) N16 −3.69/−7.57, E18 −3.14/−7.47, E27 −2.50/−6.53, Bench −6.55/−12.52; P4 (Oct 2023–Feb 2025) N16 5.34/−0.90, E18 3.98/−2.46, E27 3.40/−2.92, Bench 4.67/−2.00.
- Directional-timing hit rate: B31 positioned duration "better than the benchmark … in 52.6% of the observed periods" (Section 4.1, Fig. 13); N16 57.8% (Fig. 14). US test-set σ of zero-rate changes 0.12 vs Europe 0.10 (Section 4.1).
- Model-selection funnel: 43 models; percentile filter applied until exactly 3 per region survived all six metrics — cutoff 54th percentile (US) vs 64th (Europe) (Section 4, Figs. 11–12).
- Our own cell counts from the printed tables (labeled "our count", not a rerun): the active books beat the benchmark on return in 3 of 4 US subperiods for B31 (P1 1.36 vs 0.98, P2 4.98 vs 4.18, P3 −6.43 vs −8.02, P4 3.22 vs 3.08) but lose to it on MDD in P1 and P2 (−7.37 vs −4.92; −6.88 vs −5.02); final pick N16 loses to benchmark on return in EU P2 (−1.27 vs −0.78) and on MDD in P1 (−7.60 vs −5.45) and P4 is its only subperiod win on both axes vs E18/E27. Directional accuracy of the best models never exceeds 56.71% (US) / 53.42% (EU).

### Independently reproduced

not independently reproduced (this run read the landing page + full v1 HTML + supplementary tables, located every quoted figure in its printed table/section, ran the full-text cost-keyword scan and repo-wide/Wiki dedup; no NBBO-style panel rebuild, no model retraining, no backtest rerun, no trading rule implementation; LSEG/Datastream is license-restricted and no code exists in v1).

### Negative evidence

1. Zero transaction-cost, spread, slippage, fee, financing, fill, latency, turnover, impact, or capacity model anywhere in pinned v1 (verified by keyword scan above) — every return/IR/Ω/MDD figure is gross; weekly duration switching between a T-bill and a 10-year index in the 2022 hiking regime is unpriced → net-of-cost performance is a data gap, never zero.
2. Modest gross risk-adjusted edge: best US IR 0.46, best EU IR 0.59 (Table 8); at such IR levels a plausible 1–10 bp-per-rebalance cost ladder can plausibly erase the edge (Scout inference, to be tested).
3. Source's own prints show the active books can lose to the passive benchmark on risk: US B31 MDD worse than benchmark in P1 (−7.37 vs −4.92) and P2 (−6.88 vs −5.02); EU N16 MDD worse in P1 (−7.60 vs −5.45); EU N16 return below benchmark in EU P2 (−1.27 vs −0.78). The "strong performance" claim in Section 4.2 coexists with these printed subperiod losses.
4. Selection-in-sample ambiguity: the final percentile filter uses IR/Ω/MDD/directional accuracy "across the full test period" (Section 4.1 wording), i.e., the recommended models appear to be selected ON the hold-out window the same tables report → look-ahead model-selection bias risk; the source does not state that filtering used validation-only metrics → ambiguity (not escalated to a printed-number contradiction).
5. Weak-oracle foundation: directional accuracy of the selected models is 53.28–56.71%, barely above a coin flip per print; B31's "better duration decision" rate is 52.6% — barely above half of observed periods.
6. Bounds bind: the source states US strategy "frequently hit its upper or lower bounds" due to higher US volatility (Section 4.1) — part of the apparent timing skill may be a trading-band/constraint effect rather than forecast skill (Scout inference; ablation not performed by source).
7. Europe's pre-2004 training inputs are synthesized (German-proxy OLS backcast with R²>0.99 plus DNS-imputed missing German maturities, one scenario as weak as R² 0.5781) — synthetic training rows are model-generated, not observed.
8. Benchmark narrowness: only a constant 5-year-duration passive portfolio is compared; no horse race vs simple yield-trend/momentum rules, DNS-AR forecasts as tradable strategy, or other active duration managers is printed (the AR/VAR models are compared on forecast error and excluded by filter, not net-traded as alternatives).
9. Sample-window internal contradiction (frontmatter): July vs December 2014 test/P1 start printed both ways and never reconciled.
10. Source's own conclusion caveats: "Performance results are also tied to a specific trading strategy and may differ under alternative setups"; BOHB search space/retraining cadence left to future work; AE-for-rates underperformed; no multiplicity adjustment across 43 candidates × 6 metrics × 2 regions.
11. Breadth: two rate universes (US, Euro-AAA), single test window Dec/Jul 2014–Feb 2025 (one hiking cycle, one COVID episode); no walk-forward re-selection, no second hold-out.
12. Reproducibility: no code/replication package; LSEG/Datastream license-restricted; affiliations/emails not printed; preprint-only, single version, peer-review status not stated.
13. Point-in-time risk not fully auditable by the source: macro lag handling is described (1-month lag for monthly series), but zero-rate vintage/revision handling and the German→EU backcast's use of full-sample-fit OLS coefficients (fit statistics reported on the overlap without a stated expanding-window re-estimation) leave potential mild look-ahead in the pre-2004 extension → data gap.
14. No risk layer beyond duration bounds: no stop, no drawdown control, no volatility targeting; Ω<1.10 for US B27 (1.10) and sub-1 Ω prints exist for models in the wider grid (e.g., D43 Ω 0.78), showing many candidates underperform the benchmark on the Omega axis.

## Falsification plan

All thresholds below are `research-defined`; all operational reconstruction choices are `research-proposed`. None are source-reported.

- F1 (second-vendor replication): rebuild US zero rates from an independent vendor (e.g., H.15/FRED-only vs Datastream) and re-run B31/N16-style selection; fail if active-return NW t < 2.0 vs the constant-duration benchmark or if the selected model's IR sign flips.
- F2 (cost ladder): charge 0/1/5/10/20 bp per rebalance plus half-spread on the 10-year leg; fail if net IR < 0.20 (US B31 gross 0.46) or net Sharpe < 0.5 at 10 bp, or if net performance falls below the passive benchmark at any ladder rung ≤10 bp.
- F3 (baseline horse race): compare against (a) DNS-AR/VAR factor forecast used tradably and (b) a 12-month yield-momentum rule; fail if B31/N16 does not add ≥0.15 net IR over the best baseline.
- F4 (honest-selection audit): redo the percentile filter using validation-window (2005–2014) metrics only, freeze, then evaluate once on the untouched test; fail if the validation-selected model's test IR < 0.20 or falls below the passive benchmark (tests the selection-in-sample ambiguity in Negative evidence #4).
- F5 (risk-parity check): fail if active MDD is worse than the passive benchmark by more than 2 percentage points in any of the four US subperiods after cost (B31 already prints −7.37 vs −4.92 in P1 — pre-registered to stress).
- F6 (placebo): 1,000 circular/block-shift draws of the forecast series against realized curve changes; require observed directional-accuracy lift (over 50%) to exceed the 95th percentile of the placebo distribution, z ≥ 2.0.
- F7 (leakage audit): rebuild the EU pre-2004 extension with expanding-window (past-only) OLS and DNS imputation; fail if any model's IR moves by more than ±0.10 versus the source pipeline, or if macro-vintage handling shows any post-date input.
- F8 (subperiod stability): require positive active return vs benchmark in ≥3 of 4 US subperiods AND ≥3 of 4 EU subperiods on frozen models (pre-registered against N16's EU P2 loss).
- F9 (turnover realism): measure weekly one-way turnover implied by duration tracking; fail if median annual turnover >100% notional or 95th-percentile weekly turnover >25% (research-defined capacity screen), or if the F2 ladder at 5 bp erases >50% of gross IR.
- F10 (frozen forward test): freeze B31/N16 equivalents after Feb 2025 and evaluate ≥24 months; fail if forward IR < 50% of the printed 0.46/0.59 or if forward active return ≤ 0.

Failure action: mark the corresponding mechanism claim rejected for our research stack; no unconstrained retuning to revive (any retuning restarts the full pre-registered protocol).

## Crypto portability

unproven. The mechanism is duration timing on government yield curves; crypto has no AAA sovereign zero-coupon curve, no comparable 1-month risk-free/10-year index pair, and no licensed term-structure dataset. Speculative analogues only: perp funding-rate term structure or quarterly-basis duration positioning on a deep perpetual/futures curve. Porting obstacles: 8-hour funding resets, 24/7 candle/session boundaries (the source's RTH-independent weekly cadence at least transfers), venue-fragmented and manipulable mark prices, thin long-end liquidity, no borrow/lending curve equivalent, and unmodeled liquidation on the leveraged leg. The source demonstrates nothing in crypto; `adapted` cannot be claimed either — classification is `unproven`, and this is a ported hypothesis, not crypto empirical evidence.

## Limitations

- Signal underspecified: the proprietary forecast→duration mapping is not printed; an independent researcher cannot reconstruct exact position sizing from v1 alone.
- Transaction costs, turnover, fills, financing, and capacity: entirely unmodeled (data gap, keyword-verified) → all performance figures are gross.
- Selection-in-sample ambiguity (filter appears to use test-window metrics); July-vs-December 2014 window contradiction; 43-model search with no multiplicity/selection adjustment.
- Not independently reproduced; no code; LSEG/Datastream license-restricted; affiliations not printed; preprint-only, single version, peer review not stated.
- Benchmark narrowness (constant 5-year duration only); binds-at-bounds behavior confounds forecast skill with a trading band; synthetic pre-2004 EU training data; one test window, two rate universes.
- Confidence: `medium` refers to research interpretation fidelity (full v1 text and supplementary tables read, every quoted number located in its printed table, cost scan and dedup executed), not to profitability or trading authorization.

## Implementation status

`not-implemented`. Nothing from this record has been implemented in our research stack: no model training, no duration-timing backtest, no production card, no Qlib/Paper/Testnet/Live activity. This record is a research capture only.

## Adoption boundary

`research-only` / `not-approved` / `approval_scope: research-only`. Presence in this repository does not mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. Any adoption decision must be explicit, separately reviewed, and based on this record plus current sources.

## Related Wiki records

Wiki Brain search (2026-09-24) found no page for yield-curve forecasting/duration timing; adjacent retrieval hooks only, asserted as related-topic links, not as the same mechanism:

- [[quant/cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02]] (NN end-to-end portfolio timing, different asset class/signal)
- [[quant/foreign-exchange-spatiotemporal-graph-statistical-arbitrage-2026-09-02]] (ML rate prediction with different mechanism and universe)

## Sources

- arXiv:2606.26815v1 landing page: https://arxiv.org/abs/2606.26815 (authors, version history, categories, license, funding/conflict/data statements; checked 2026-09-24).
- arXiv:2606.26815v1 full text (HTML, 948,211 bytes, fetched 2026-09-24): https://arxiv.org/html/2606.26815v1 — Sections 2.1–3.3 (data, architecture, investment strategy, metrics, tuning), Section 4 Tables 6–11 and Figures 11–14, Section 5, Appendix Table A1, Supplementary Tables 1.1, 2.1–2.2, 3.1–3.2, 4.1–4.4, 5.1–5.4 (all quantitative claims above trace to these tables/sections).
- DataCite DOI: https://doi.org/10.48550/arXiv.2606.26815 (resolves 200 → abs; checked 2026-09-24).
- Underlying data vendors named by the source (not independently re-verified beyond the source's own data-availability statement): FRED https://fred.stlouisfed.org/, ECB https://data.ecb.europa.eu/data/datasets, LSEG/Datastream (license-restricted), ICE BofA 10+ Year AAA Euro Government Index.
