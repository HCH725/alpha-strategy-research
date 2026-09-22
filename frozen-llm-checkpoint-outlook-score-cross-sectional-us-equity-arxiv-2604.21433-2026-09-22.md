---
schema: strategy-research-record-v1
title: "Frozen LLM Checkpoint Outlook Score and Cross-Sectional US Equity Return Predictability (ChatGPT as a Time Capsule)"
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - large-language-models
  - cross-sectional
  - equity-long-short
  - qualitative-text-signal
  - point-in-time-knowledge
  - information-aggregation
status: research-only
confidence: medium
source_as_of: 2026-04-23
sources:
  - "Sebastian Lehner and Alejandro Lopez-Lira, 'ChatGPT as a Time Capsule: The Limits of Price Discovery', arXiv:2604.21433v1 [q-fin.GN], submitted 23 Apr 2026. DOI: 10.48550/arXiv.2604.21433. https://arxiv.org/abs/2604.21433 (full text read via https://arxiv.org/html/2604.21433v1)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Frozen LLM Checkpoint Outlook Score and Cross-Sectional US Equity Return Predictability (ChatGPT as a Time Capsule)

## Provenance

- **Canonical source**: arXiv:2604.21433v1 [q-fin.GN], *"ChatGPT as a Time Capsule: The Limits of Price Discovery"*, DOI `10.48550/arXiv.2604.21433`, https://arxiv.org/abs/2604.21433
- **Authors (exactly as source)**: Sebastian Lehner (Independent Researcher, Frankfurt, Germany; `seb.lehner1@gmail.com`); Alejandro Lopez-Lira (Warrington College of Business, University of Florida; `alejandro.lopez-lira@warrington.ufl.edu`).
- **Version / date**: submission history shows a **single version `[v1] Thu, 23 Apr 2026 08:49:39 UTC`** (verified on the abs page 2026-09-22). Primary category `q-fin.GN`; license CC BY-NC-ND 4.0.
- **Publication status**: arXiv preprint; the source does not state peer-reviewed/journal acceptance — `not stated in source`.
- **Primary-source checksum performed 2026-09-22**: abs page + full arXiv HTML (`/html/2604.21433v1`) opened and read directly, including §4 Data (4.1–4.5), §5 Empirical Results (5.1–5.7), Tables 1–14 and §6 Conclusion. The arXiv PDF was **not** opened in this run; all numbers below trace to the HTML full text of v1.
- **Source-versioning ambiguity (not silently resolved)**: the HTML rendering carries the date line **"August 24, 2026"**, which conflicts with the abs-page submission date of 23 Apr 2026; recorded as a rendering/date-field ambiguity rather than treated as a second version. No `[v2]` exists in the submission history.
- **Sample / data window as reported**: daily price and share-count data from Refinitiv for **January 2021 – September 2025** (§4.1), yet forward-return windows for the August-2025-cutoff models run "approximately seven months (through March 2026)" (§4.2.1) and Table 13 reports 7-month post-cutoff portfolios for GPT-5.2/GPT-5.4. This **internal inconsistency is marked `data gap`**, not reconciled.
- **Dedup (repo-wide, not git-log-only)**: ripgrep across all `*.md` (plus `coverage_manifest.csv`) for `2604.21433`, exact title `ChatGPT as a Time Capsule`, `Sebastian Lehner`, `outlook score`, `time capsule` → **zero existing records**. `Lopez-Lira` appears only as co-author on three *different* captured papers (`llm-compressed-financial-analysis-information-fidelity-arxiv-2606.29251-2026-09-20.md`, `prediction-market-lead-lag-llm-semantic-risk-filtering-2026-09-03.md`, `small-cap-alpha-beta-separation-uncertainty-aware-llm-portfolio-2026-09-02.md`); `knowledge cutoff` appears only in the small-cap record. No same-source-identity record exists.

## Economic mechanism

### Source-reported

The authors treat each frozen OpenAI checkpoint as a **time-stamped compression of the public textual record available before its knowledge cutoff**. Prompted once per company (temperature 0, `top_p` 1) as an equity analyst restricted to business fundamentals, the model returns an integer outlook score (−10 to +10) that is demeaned/standardised within GICS sector. The source reports this sector-neutral score predicts post-cutoff revenue growth, net-income growth and analyst target-price revisions (Table 3), and predicts 1–12 month cross-sectional returns after controlling size/quality/value/momentum **and** four market-implied cheapness metrics (inverse P/E, ICE-GLS implied cost of equity, ICE-PEG, inverse EV/EBITDA) (Tables 4–6). The stated interpretation is a **limits-of-price-discovery** story: the bottleneck is the cost of aggregating dispersed qualitative information across many documents ("narrative congestion") rather than investor inattention, and this friction may persist or intensify as disclosure volume grows. The source explicitly does **not** claim a formal rejection of market efficiency and flags the joint-hypothesis problem (the score may partly price an unspanned risk dimension).

### Research interpretation

Falsifiable mechanism: **cross-sectional underreaction to dispersed qualitative corporate information**, with a frozen LLM acting as a cheap aggregator over a fixed, auditably pre-cutoff information set. Component roles:

```text
Signal: sector-neutral z-score of frozen-checkpoint 12-month outlook rating (−10..+10)
Timing: score formed at the checkpoint's knowledge cutoff; forward returns start t+1 (non-overlapping 1/3/4/6/12m)
Portfolio layer (source §5.7): regularised mean-variance, long-only, 1.5% position cap, monthly rebalance
Regime filter: none in source
Risk / exit: none stated in source (drawdown control only appears descriptively in Table 13/14)
```

Competing explanations to be tested rather than assumed: (i) the score is a proxy for profitability/quality (source reports L/S correlation with RMW +0.63); (ii) it inherits a cheapness tilt (source says the portfolio's use of the raw score "overstates the signal's independent contribution"); (iii) residual post-cutoff leakage inside a claimed cutoff; (iv) provider-side model drift breaking the "frozen" premise.

## Signal

- **Formation timestamp**: one API query per (company, checkpoint) pair at the checkpoint's **public knowledge cutoff**, treated as the information set; deterministic sampling (`temperature: 0`, `top_p: 1`) so re-querying yields identical output (source §4.2.3). Forward returns begin at `t+1` (last trading day on or before the cutoff — see cutoff-labelling note below). **Timezone convention for cutoff timestamps: `data gap` (not stated in source).**
- **Prompt / extraction**: system prompt casts the model as an equity analyst using only revenue growth, profitability trends and operational risks — explicitly no valuation multiples, market prices or technical indicators; user prompt supplies legal name, ticker, ISIN, country, GICS industry code; response is structured JSON containing outlook score (−10..+10, 12-month forward business assessment vs industry peers), growth/profitability/risk sub-scores, a 0–100 confidence, growth/EPS/margin probability bins, 2–5 driver tags, a ≤30-token rationale, and a 0–100 knowledge-coverage score. Full prompt in source Appendix A.
- **Normalisation (Eq. 10)**: within each GICS sector, `S̃ = (S − mean_sector) / sd_sector`.
- **Lookback**: none in the classical sense — the "lookback" is the model's entire pre-cutoff training corpus. Post-cutoff evaluation windows are non-overlapping ≈20/60/80/120/250 trading days for 1/3/4/6/12 months (§4.1).
- **Checkpoints (Table 1)**: 12 models — GPT-4.1 / mini / nano, o3 (cutoff Jun 2024), GPT-5-mini / nano (May 2024), GPT-5 (Sep 2024), GPT-4o (Oct 2023), GPT-4-Turbo (Dec 2023), GPT-3.5-Turbo (Sep 2021), GPT-5.2 and GPT-5.4 (Aug 2025) — mapping to **six unique analysis dates: Sep 2021, Oct 2023, Dec 2023, May 2024, Sep 2024, Aug 2025** (§5.2.4). *Source-internal labelling tension*: Table 1 prints "Cutoff Jun 24" for the GPT-4.1 family while §5.2.4 says the June-2024 and May-2024 cutoff models both map to the last trading day of May 2024 — recorded as printed, not reconciled (`underspecified`).
- **Entry / long-short construction (evidence, not a specified trade rule)**: quintile sorts on `S̃` with returns winsorised 1st/99th percentile (Table 10); a control-adjusted variant residualises the score on the regression controls (§5.5). **No shorting mechanics, borrow, execution price or exit rule are given → signal `underspecified` for the long-short form.**
- **Portfolio construction actually specified by the source (§5.7, Table 13)**: `μ_i = γ̂ · S̃_i` with `γ̂ = 0.0074` (Driscoll–Kraay pooled 1-month estimate, Table 5); Axioma US4-MH covariance (~80 style/industry factors + idiosyncratic), diagonal shrinkage `α = 0.10`; outlook z-scores winsorised ±2.5; risk aversion `λ = 1`; **long-only with 1.5% position cap (~65–90 active names)**; **monthly rebalance** with the risk model refreshed monthly while **the alpha signal stays fixed from the cutoff date**; signal life 3/6/12 months; GPT-3.5-Turbo excluded from the portfolio sample (two-year gap before the next cutoff). Equal-weight same-universe and the S&P 500 **price** index are the benchmarks.
- **Contamination check (source)**: 100 trivia questions about post-cutoff events → mean accuracy **0%** at every checkpoint (§4.2.3).
- **Multiple testing (source)**: 12 separate checkpoint tests → 7 significant at 5% vs 0.6 expected under the global null; Bonferroni `0.05/12` (`|t| > 2.87`) met by **four** checkpoints (GPT-4.1, GPT-4.1-mini, GPT-4.1-nano, o3); 11 of 12 point estimates positive. The source explicitly declines to claim every checkpoint works.
- **Parameters**: all values above are **source-reported** (fixed, not tuned in this capture). Any threshold introduced later in this record is labelled `research-proposed` / `research-defined`.

## Required data

- **Universe**: securities classified Common Stock, ranked among the ~**7,000 largest US firms by market cap** on the trading day immediately preceding each model cutoff; non-missing shares outstanding and complete factor-exposure/accounting information; **firms delisted after entry are retained** (source states this avoids survivorship bias). Regression-ready sample is far smaller — binding constraint is ICE-GLS coverage (Table 2: GPT-4.1 universe 7,121 → returns 6,517 → **final 1,272**; per-checkpoint finals range 1,059–1,448; Table 10 sort sample N = 6,647).
- **Price data**: Refinitiv Datastream corporate-action-adjusted close (datatype P, excludes dividend reinvestment), stated window **Jan 2021 – Sep 2025** (`data gap` versus the Mar-2026 return windows noted in Provenance). S&P 500 Price Index treated identically for benchmark comparability.
- **Fundamentals / forecasts**: Compustat and Worldscope accounting variables; I/B/E/S consensus `EPS_t+1`, `EPS_t+2`, `EPS_t` **as of one day before each cutoff**.
- **Factors**: Fama–French five factors + momentum from the Kenneth R. French data library; Axioma US4-MH style/industry factor exposures (used as regression controls and as the portfolio covariance engine).
- **LLM API**: OpenAI snapshots with published cutoffs spanning **Sep 2021 – Aug 2025** (releases extend into 2026). API version strings as printed: GPT-4.1 family `2025-04-14`; GPT-5.4 `2026-03-05`; GPT-5.2 `2025-12-11`; GPT-5/mini/nano `2025-08-07`; GPT-4o `2024-08-06`; GPT-4-Turbo `0125-preview`; GPT-3.5-Turbo `0125`; o3 `2025-04-16`.
- **Point-in-time requirements**: information set = checkpoint cutoff; analyst and factor data one day pre-cutoff; forward returns strictly after cutoff. Architecture mix spans autoregressive (GPT-3.5/4-Turbo/4o/4.1) and reasoning (GPT-5 family, o3) models.
- **Missing data**: malformed JSON / refusals coded missing, **<1% of the universe (<50 of ~7,000 per checkpoint)**; observations dropped when the LLM score or any required market-implied metric is missing (§4.4). No imputation.
- **Additional data gaps**: timezone/clock convention for cutoffs, ISIN-level corporate-action edge cases, Axioma/ICE-GLS/I-B-E-S vendor versions and licensing, and the exact per-checkpoint scoring dates behind Table 1 vs §5.2.4 → all `not stated in source` / `data gap`.

## Execution assumptions

- **Source-reported**: monthly rebalance; long-only; 1.5% position cap (~65–90 names); mean-variance with `λ = 1`, covariance shrinkage `α = 0.10`, score winsorisation ±2.5; signal fixed from cutoff while the risk model updates monthly; **all reported portfolio returns are gross of transaction costs**; turnover ≈**15% one-way per month** (excluding formation); at an **assumed 20 bp round-trip**, the aggregate 12-month portfolio's annualised return would fall by **~35 bp/year (Sharpe impact ≈ 0.05)**, per-model portfolios by **50–80 bp/year**; benchmarks are equal-weight same-universe and the S&P 500 price index (dividends excluded by construction of datatype P).
- **Not stated in source**: order type (market/limit), fill model, execution price and signal-to-order timing (same-bar vs next-bar), latency, participation/ADV caps, market impact, capacity, borrow availability and cost for the long-short sorts, shorting mechanics, margin/leverage, partial fills → all `not stated in source`. Fillability and net-of-cost tradability are therefore `underspecified`; the only cost statement in the source is the 20 bp round-trip sensitivity above.

## Evidence

### Source-reported

All figures below are **source-reported** (not reproduced by us) and trace to arXiv:2604.21433v1 as cited in `## Sources`. Sample: US equities, ~7,000-name universe per cutoff, six analysis dates Sep 2021 – Aug 2025, forward windows to ≈Mar 2026 for the newest cutoffs.

- **Table 3 (H1, GPT-4.1)**: outlook score predicts realised 12-month revenue growth `β = 0.168 (t = 10.89)`, N = 6,600; net-income growth `β = 0.038 (t = 2.18)`; analyst target-price revisions `β = 0.347 (t = 4.80)`, N = 5,057.
- **Table 4 (H2 single model, GPT-4.1, τ = 1m)**: `γ = 0.0122 (t = 4.25, p < 0.01)`, N = 1,272; horizon coefficients 3m `0.0038`, 4m `0.0020`, 6m `0.0386***`, 12m `0.0683***` (source text: the 12-month coefficient is "over five times the one-month estimate"). Exact t-statistics for the 6m/12m cells were not transcribed in this capture → `data gap` for those cells.
- **Table 5 Panel A (pooled panel, model fixed effects)**: `γ = 0.0074 (t = 6.02)`, N = 14,918 firm–model observations at 1 month; significant at all horizons up to 6 months; 12-month `γ = 0.0113 (t = 1.07)`.
- **Table 6 / Table 12 (overlap-robust inference)**: Driscoll–Kraay SEs `γ = 0.0074 (t = 5.43)`; twelve-model Fama–MacBeth mean `γ = 0.0078 (t = 5.09)`, Newey–West(1) `t = 4.71`, bootstrap 95% CI `[0.0047, 0.0103]`, bootstrap p = 0.0002; strict one-model-per-cutoff (six cross-sections) `γ = 0.0064 (t = 2.25)` with **p = 0.074** and bootstrap p = 0.019; pooled panel with model + industry FE `γ = 0.0064 (t = 5.74)`.
- **Table 7 (size terciles, GPT-4.1, τ = 1m)**: small `γ = 0.0149 (t = 2.18)`, mid `γ = 0.0077 (t = 1.38)`, large `γ = 0.0087 (t = 2.40)`; score × log-mcap interaction `t = 1.88 (p = 0.06)`.
- **Table 12 (robustness, τ = 1m)**: excl. bottom 20% by size `0.0133 (t = 4.42)`, N = 1,017; large-cap only `0.0110 (t = 3.26)`, N = 636; winsorised 1/99 `0.0125 (t = 4.51)`; winsorised 5/95 `0.0118 (t = 4.53)`.
- **Table 10 (unconditional quintile sorts, GPT-4.1, τ = 1m, returns winsorised 1/99, N = 6,647)**: Q1 −6.56%/mo, Q2 −2.91%, Q3 −2.51%, Q4 −2.20%, Q5 −0.61%; **L/S (Q5−Q1) = +5.95%/mo, t = 7.53**. Control-adjusted L/S spread **2.55%/mo (t = 3.71) ≈ 30.6% annualised** (§5.5) — the source labels this **in-sample**.
- **§5.5.1 (factor character, six calendar-month L/S returns)**: correlations RMW **+0.63**, SMB −0.57, CMA −0.52, market −0.50, momentum +0.16; a time-series alpha regression is **not estimable** (6 observations, 7 parameters); the feasible CAPM intercept is **1.33%/mo (t = 0.78), insignificant**.
- **Table 13 Panel A (aggregate MV portfolio, one model per cutoff, gross of costs)**: 3-month signal life — 13 rebalance months, 21.93% ann. return, 6.21% vol, **SR 3.53**; 6-month — 22 months, 17.71%/7.60%, **SR 2.33**; 12-month — 30 months, **16.83% ann., 7.27% vol, SR 2.31, MDD −3.7%**, versus matched S&P 500 **SR 1.31, MDD −9.7%**; equal-weight 12-month SR 1.55.
- **Table 13 Panel B (per-model, 12-month signal life, gross of costs)**: all 11 model portfolios have positive MV Sharpe; **average MV 12.56% ann. / 7.90% vol / SR 1.66**, equal-weight 15.47%/12.58%/1.37, matched S&P 500 average **SR 1.23**.
- **Costs**: gross of transaction costs throughout; 20 bp round-trip sensitivity ≈ −35 bp/yr (aggregate, SR impact ≈ 0.05) and −50 to −80 bp/yr (per-model) as detailed in `## Execution assumptions`.
- **Mechanism-consistency evidence (§5.4)**: Spearman correlation of cutoff recency with `γ` = **0.617 (p = 0.033)**; within the May/June-2024 cluster larger models score higher (GPT-4.1 `0.0122` vs GPT-4.1-nano `0.0065`; o3 `0.0113` vs GPT-5-nano `0.0059`).

### Independently reproduced

not independently reproduced

### Negative evidence

Drawn **from the source itself** unless noted:

- **No held-out period**: `out-of-sample`/`holdout` appear nowhere in the source; `γ` is estimated and the portfolio applied on the same six cutoff cross-sections, and the source explicitly calls the long-short results **in-sample**.
- **Factor overlap**: the long-short book tracks profitability (RMW ρ = +0.63) and quality-ish characteristics; the only feasible time-series alpha (CAPM) is insignificant (`t = 0.78`), and with six monthly observations a FF5+UMD alpha is **not estimable at all**.
- **Multiple testing**: only **4 of 12** checkpoints survive Bonferroni; the source states it does not claim every checkpoint independently demonstrates predictability.
- **Heterogeneity**: mid-cap tercile insignificant (`t = 1.38`); cross-model significance is concentrated in the GPT-4.1 family and o3.
- **Regime**: the 30-month portfolio window "coincides almost entirely with a rising equity market, and the strategy's behaviour in a downturn remains untested" (source); MDD comparisons are against a benchmark whose own drawdown was minimal in the shortest window.
- **Signal-independence caveat**: the portfolio feeds the **raw** score (not residualised on cheapness) into the optimiser, so returns "overstate the signal's independent contribution relative to a strategy that already trades on valuation metrics" (source).
- **Inference fragility**: the strict six-cutoff Fama–MacBeth test is only marginal (`p = 0.074`); the source flags within-cutoff return overlap as making the 12-model row "less conservative".
- **Costs**: results are gross; only a single 20 bp round-trip sensitivity is given, with no spread/impact/latency model.
- **Reproducibility risk**: scores depend on specific OpenAI API snapshots and published cutoffs that may be deprecated or silently updated; deterministic parameters do not rule out provider-side nondeterminism (`data gap`); score missingness <1%; commercial Axioma/ICE-GLS/I-B-E-S dependencies are not freely reproducible.
- **Source-internal inconsistencies**: Refinitiv window (Jan 2021 – Sep 2025) vs return windows through ≈Mar 2026; Table 1 "Cutoff Jun 24" vs §5.2.4 May-2024 analysis date; HTML date line "August 24, 2026" vs v1 submission 23 Apr 2026 — all recorded, none repaired.
- Absence of any independent replication attempt: **none identified in our own stack; absence is not evidence of no negative result.**

## Falsification plan

Every threshold below is a Scout-authored acceptance rule → **`research-defined`**; every operational choice not specified by the source → **`research-proposed`**. Source-derived items are marked.

1. **Strict out-of-sample checkpoint test** — *data*: a checkpoint/cutoff never used in estimating `γ̂` (e.g., any post-Aug-2025 cutoff) plus its forward 1-month returns; *sample*: ≥1,000 regression-ready names; *metric*: pooled 1-month `γ̂` with Driscoll–Kraay SEs; *threshold*: fail if `|t| < 2.0` or the 95% CI includes 0 (**research-defined**); *action*: reclassify the record as descriptive-only, no candidate-pool entry.
2. **Net-of-cost stress** — *data*: Table 13 turnover (~15% one-way/month); *grid*: 10/20/50 bp round-trip (**research-proposed**, source only tested 20 bp); *metric*: net Sharpe of the 12-month MV portfolio vs matched S&P 500 SR 1.31; *threshold*: fail if net SR ≤ benchmark SR at 20 bp (**research-defined**); *action*: mark mechanism non-tradable at retail costs.
3. **Sector-shuffled placebo** — *data*: same scores and returns; *operation*: permute `S̃` across firms within GICS sector, 1,000 draws (**research-proposed**); *metric*: null distribution of `γ̂`; *threshold*: fail if ≥10% of placebo draws reach `|t| ≥ 2.0` (**research-defined**) → source's headline `t = 4.25` is not extreme; *action*: reject as overfit signal.
4. **Factor-control ablation (competing explanation)** — *data*: Table 4 specification plus explicit RMW/CMA/quality/beta controls; *metric*: change in `γ̂`; *threshold*: fail if `γ̂` falls >50% and becomes insignificant (**research-defined**); *action*: relabel as profitability/quality exposure rather than text alpha.
5. **Checkpoint reproducibility / provider drift** — *data*: re-query the same model+prompt with `temperature 0` on ≥200 firms (**research-proposed**); *metric*: exact-score agreement rate; *threshold*: fail if agreement <95% (**research-defined**) → the "frozen, auditable snapshot" premise is broken; *action*: mark source unreproducible and archive raw responses.
6. **Post-cutoff contamination re-audit** — *data*: extend the source's 100-trivia battery to ≥300 questions per cutoff, oversampling near-boundary events (**research-proposed**); *metric*: mean accuracy; *threshold*: fail if accuracy >5% (**research-defined**); *action*: discard the affected checkpoint as leakage-contaminated.
7. **Regime split** — *data*: same cross-sections split by S&P 500 trailing 12-month sign (**research-proposed**); *metric*: `γ̂` per subperiod; *threshold*: fail if signs flip and both subperiods have `|t| < 2.0` (**research-defined**) → mechanism claim weakened to a bull-market artifact; *action*: downgrade confidence to low.
8. **Capacity / liquidity stress** — *data*: ADV and position-size constraints on the 65–90-name long-only book; *operation*: 10% ADV participation cap (**research-proposed**); *metric*: net SR gap vs benchmark; *threshold*: fail if gap ≤ 0 at 50 bp round-trip (**research-defined**); *action*: mark capacity-limited.
9. **Architecture/family placebo (source-motivated)** — *data*: same prompt run through models whose cutoff post-dates the evaluation start (**research-proposed**); *metric*: predictability of the leaked-checkpoint score; *threshold*: if a post-dated checkpoint performs **no better** than genuinely frozen ones (**research-defined**), the cutoff discipline is not what drives results; *action*: re-audit design.

## Crypto portability

**unproven.** The source demonstrates the mechanism only in US equities (~7,000 Common Stocks, filings regime, I/B/E/S coverage, GICS sector structure, monthly session-based rebalancing). Crypto-relevant risks if one were to port it:

- **Universe depth**: the cross-sectional design needs thousands of names; the set of liquid, disclosure-rich crypto assets is orders of magnitude smaller, so sector-neutral cross-sectional sorts lose power.
- **Disclosure regime**: no 10-K/earnings/analyst corpus — the "dispersed qualitative information" the mechanism aggregates is structurally different (docs, governance forums, on-chain reports), and an LLM's pre-cutoff knowledge of small tokens is thin (the source's own knowledge-coverage score would likely collapse).
- **24/7 session and timestamps**: cutoff-to-first-trade alignment, timezone and candle-boundary conventions are undefined for crypto; no source guidance exists (`data gap`).
- **Venue fragmentation / survivorship**: delistings, stablecoin quoting and cross-exchange price divergence would break the single-vendor price series the source relies on.
- **Costs and structure**: crypto taker fees, funding and impact are absent from the source's gross, 20 bp-equivalent sensitivity.

Any crypto version (e.g., sector-neutral outlook z-scores over the top-N liquid perpetuals, weekly rebalance, long-only top-quintile with explicit fill timing) would be a **new hypothesis, `research-proposed`**, not evidence from this source — and it would still need the falsification tests above before any adoption claim.

## Limitations

- `not independently reproduced` — no replication has been attempted in our stack; all numbers are third-party, source-reported.
- `underspecified` — no order type, execution price, signal-to-order timing, fill model, borrow or exit rule for the long-short construction; portfolio form is long-only with a position cap but no execution convention.
- `data gap` — Refinitiv window (Jan 2021 – Sep 2025) vs Mar-2026 return windows; Table 1 vs §5.2.4 cutoff-labelling tension; HTML date line vs submission date; exact t-statistics for Table 4's 6m/12m cells; timezone conventions; vendor versions/licensing for Axioma, ICE-GLS, I/B/E/S, Refinitiv.
- `data gap` / reproducibility — dependence on specific OpenAI API snapshots and published cutoffs that can be deprecated or altered; provider-side determinism at `temperature 0` is asserted, not demonstrated; prompt Appendix A plus API access are required, and neither the raw score panel nor the code is stated as publicly released by the source.
- Statistical limitations acknowledged by the source: only six unique analysis dates, within-cutoff return overlap, marginal strict Fama–MacBeth result, 4-of-12 Bonferroni survival, no time-series alpha estimable, gross-of-cost reporting, bull-market-concentrated evaluation window, and an explicit joint-hypothesis caveat.
- Publication-bias / source-quality: single preprint by two authors (one independent), no stated peer review, CC BY-NC-ND license (cite and normalise only — no wholesale redistribution of figures).
- Incremental-write check: mechanism (frozen-checkpoint knowledge aggregation → cross-sectional returns) and signal construction (sector-neutral z-score of a prompted outlook rating at a fixed cutoff) are materially distinct from the other LLM records in this repo (news-sentiment, persona consensus, macro-analog nowcasts, KOL distillation), so this capture clears the incremental threshold rather than duplicating a family.
- `confidence: medium` refers to the faithfulness of this research interpretation of the source — **not** to profitability and not to any trading authorisation.

## Implementation status

`implementation_status: not-implemented`. Nothing has been built in our research stack: no score extraction pipeline, no prompt harness, no backtest, no Qlib run, no survivor bundle, no Paper/Testnet/Live activity of any kind. This record is a normalised research capture of an external preprint only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record in the staging repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet or live trading. Any adoption or implementation decision is a separate, explicitly reviewed step.

## Related Wiki records

Two Wiki Brain searches were run this capture: `LLM text signal cross-sectional equity return predictability factor` (7 hits) and `frozen LLM knowledge cutoff point-in-time text aggregation underreaction narrative congestion` (0 hits).

- **No Wiki Brain page exists for this source** (arXiv:2604.21433) — stated plainly rather than linked.
- Nearest family neighbours returned by search, listed only as retrieval hooks for future synthesis/contradiction checks and **not** as the same mechanism or source: [[quant/chronos-foundation-transformer-statistical-arbitrage-factor-residuals-2026-09-12]], [[quant/retail-agent-structured-adverse-timing-contrarian-alpha-2026-09-02]].
- Adjacent records in this staging repo (different sources, different mechanisms): `small-cap-alpha-beta-separation-uncertainty-aware-llm-portfolio-2026-09-02.md` (arXiv:2608.12283), `prediction-market-lead-lag-llm-semantic-risk-filtering-2026-09-03.md`, `llm-compressed-financial-analysis-information-fidelity-arxiv-2606.29251-2026-09-20.md`.

## Sources

- Sebastian Lehner and Alejandro Lopez-Lira, *ChatGPT as a Time Capsule: The Limits of Price Discovery*, **arXiv:2604.21433v1 [q-fin.GN]**, submitted 23 Apr 2026 08:49:39 UTC (single version). DOI: `10.48550/arXiv.2604.21433`.
  - Abstract/landing page: https://arxiv.org/abs/2604.21433
  - Full text read for this record (v1 HTML, sections §1–§6 + Tables 1–14 + Appendix A prompt): https://arxiv.org/html/2604.21433v1
  - Verification performed 2026-09-22: author list, version/date, universe, sample/cutoff windows, cost treatment (gross + 20 bp sensitivity read in §5.7), core performance numbers located to named tables, publication status (preprint).
- No secondary summary was used to fill any field; search-result snippets were discovery aids only.
