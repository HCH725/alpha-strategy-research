---
schema: strategy-research-record-v1
title: "Post-Screening Portfolio Selection (PS2 / FPS2): Lasso support-recovery screening followed by low-dimensional post-Lasso weight estimation on S&P 500 weekly returns (arXiv:2604.17593v1)"
created: 2026-09-26
updated: 2026-09-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-26
sources:
  - https://arxiv.org/abs/2604.17593
  - https://arxiv.org/html/2604.17593v1
  - https://arxiv.org/pdf/2604.17593v1
  - https://doi.org/10.48550/arXiv.2604.17593
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Source-internal (table/panel mismatch): Table 5 caption prints the full out-of-sample period as '–2025/12', while the Table 5 panel headers print '-2025/11' and Section 6.1 prose prints 'first week of January 2000 to the third week of November 2025' (verified on pinned PDF p.28 and pinned HTML)."
  - "Source-internal (duplicate row): Table E.1 panel (iv) J=500 [Turnover] row [0.826][0.412][0.027][0.108][0.403] (column order FPS2/FM/EW/QIS/FF3) is element-wise identical, by column identity, to the Table 5 panel (iv) J=100 [Turnover] row [0.826][0.412][0.108][0.403][0.027] (column order FPS2/FM/QIS/FF3/EW); the J=500 turnover rows of Table E.1 panels (v) and (vi) are NOT identical to their Table 5 counterparts. The source does not explain the duplication (verified on pinned PDF pp.28 and 57)."
  - "Source-internal (claim vs printed table): Section 5.5 states PS2 'tends to outperform QIS and GL in terms of both MSE and SR', yet Table 3(v) prints QIS SR above PS2 in 24/24 cells and GL SR above PS2 in 23/24 cells (our count on printed cells). The statement is supportable only under an unstated 'closeness to the true SR = 1' reading; the MSE half is mixed (PS2 below QIS in 17/24, below GL in 15/24 cells, our count)."
  - "Source-internal (wording hazard): Section 6.5 says the long-window (J=500) net performance 'deteriorates further', but the printed FPS2 net overall Sharpe at J=500 (0.055, Table E.1 panel (iv)) is higher than the J=100/200/300 net values (0.019/0.042/0.044, Table 5 panel (iv)); what deteriorates is the relative ranking against EW (0.062) and FF3 (0.095) at J=500. Evaluation lengths differ across J (1350-J), so the absolute levels are not strictly comparable — recorded as a wording hazard, not a hard numerical error."
  - "Source-internal (precision): Section 6.5 says FPS2 'uniformly dominates FMAXSER over all reported window lengths' for the overall and pre-pandemic periods, but the overall gross J=100 cell is a tie (FPS2 0.082 vs FM 0.082, Table 5 panel (i))."
---

# Post-Screening Portfolio Selection (PS2 / FPS²): Lasso support-recovery screening then post-Lasso weight estimation

## Provenance

**Primary source (opened and checksum-verified by this Scout on 2026-09-26):**

- Yoshimasa Uematsu and Shinya Tanaka, *Post-Screening Portfolio Selection*, arXiv:2604.17593.
- Sole version `[v1] Sun, 19 Apr 2026 19:53:31 UTC (1,800 KB)`. `https://arxiv.org/abs/2604.17593v2` returned HTTP 404 (7,546 bytes) and `https://arxiv.org/html/2604.17593v2` returned HTTP 404 (7,715 bytes) on 2026-09-26 → v1 is the only version.
- Categories printed on the abs page: `Portfolio Management (q-fin.PM); Methodology (stat.ME)`; `Cite as: arXiv:2604.17593 [q-fin.PM]` → primary q-fin.PM, secondary stat.ME.
- **No Comments field, no journal-ref field, no publisher DOI cell** on the abs page; the only DOI printed is the arXiv-issued DataCite DOI `https://doi.org/10.48550/arXiv.2604.17593` → **preprint only, no peer-review statement in the pinned source**.
- Licence: PDF metadata `/License = http://arxiv.org/licenses/nonexclusive-distrib/1.0/` (arXiv.org perpetual non-exclusive distribution) → the text is cited and normalised here rather than reproduced.
- **Affiliations:** the HTML author block lists two affiliation lines at block level — `Department of Social Data Science, Hitotsubashi University` and `Department of Economics, Otaru University of Commerce` — and Uematsu's correspondence footnote (`Correspondence: Yoshimasa Uematsu, Department of Social Data Science, Hitotsubashi University, 2-1 Naka, Kunitachi, Tokyo 186-8601, Japan`) pins **Uematsu** to Hitotsubashi. Shinya Tanaka carries a `†` superscript whose note content is absent from the pinned HTML and the two affiliation lines are **not bound per author** → **Tanaka's affiliation is `underspecified`**.
- Pinned HTML: `https://arxiv.org/html/2604.17593v1`, 1,690,421 bytes, SHA-256 `da9e60282f0b8b1a3b3efe91886b00ec5606ecfb06a094e29f49e65c350e33b8`, converted to 232,158 characters / 5,220 lines; Sections 1–7, §5.2 (λ-selection steps), §6.1–6.5, Table 3, Table 4, Table 5, Table E.1, the Acknowledgments block and the reference list were read; the 968-ticker appendix and bibliography were sampled.
- Pinned PDF: `https://arxiv.org/pdf/2604.17593v1`, 4,540,418 bytes, SHA-256 `aaa2c91462513159b06a28f46db36d5153523553c226195727c248fa8ca1bee6`, 60 pages, producer `pikepdf 8.15.1`, **no `/CreationDate` in the PDF metadata → `data gap`**. PDF pages 28, 29, 57 and 58 were extracted and cross-checked against the HTML for Table 5, the §6.5 narrative and Table E.1; all quoted cells below were confirmed in **both** renderings.
- Sample period, universe, cost treatment and performance figures below come from §6.1, §6.2, §6.3, §6.4, §6.5, Table 5 (PDF p.28), Table 3/4 and Table E.1 (PDF p.57) of this pinned v1 — never from a secondary summary.
- **Availability:** no code repository, no code-availability section, no data-availability statement and no data vendor for the return panel beyond `Bloomberg` (§6.1); the `Acknowledgments` heading in the pinned HTML is immediately followed by `References`, i.e. the section is **empty** → reproducibility fields are `data gap`.
- Source-reported external dependencies named by the paper (not opened by this Scout, therefore not independently verified): `GitHub/fja05680/sp500` (point-in-time S&P 500 constituent lists, footnote 3) and the Ken French Data Library `https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html` (FF3 factors + 1-month T-bill).

**Repo-wide source-identity dedup (before write, entire repository — not `git log -20`):** ripgrep across **2,552** `*.md` files (988 top-level, hidden-inclusive: `.mimo-worktrees`, `.agents`, `.hermes`) plus `coverage_manifest.csv` (5,808 lines) for `2604\.17593`, `10\.48550/arXiv\.2604\.17593`, `Post-Screening Portfolio`, `post-screening portfolio`, `Uematsu`, `Shinya Tanaka`, `FMAXSER` → **0 hits**; a second sweep for `high-dimensional portfolio|sparse portfolio|portfolio selection with Lasso|sure screening|mean-variance screening` returned 5 files, all different source identities and different mechanisms (see *Related Wiki records*). No existing record was opened or modified.

## Economic mechanism

### Source-reported

- **Support identity (Proposition 1, §3.1).** The paper shows that the support of the population mean–variance optimal weight vector coincides with the support of a low-dimensional regression target, so one-shot high-dimensional portfolio construction decomposes into (i) *support recovery* and (ii) *low-dimensional weight estimation on the recovered support*.
- **Step 1 — screening.** Regress a constant on the excess-return matrix **without an intercept** (pseudo-response `z`), using the Lasso; the active set Ŝ is the screened asset set. The source stresses that this is a *screening* device only: the Lasso coefficients are not the portfolio weights, and the ℓ1 penalty additionally "implicitly controls the portfolio's gross exposure during the screening phase" (§3.1.1, citing Brodie et al. 2009 and Fan et al. 2012).
- **Step 2 — post-screening estimation.** With N replaced by |Ŝ|, estimate weights by a standard low-dimensional method (post-Lasso OLS construction, eq. (3.5)/(6.1)).
- **Why FPS² exists.** Strong pervasive factors make the raw screening target dense and collinear (§1.4, §3.2, §4.3), so FPS² first **defactors** returns with FF3, screens the **residual** matrix, and then **re-includes the investable factors X** in the second-stage problem `[R_Ŝ, X]`. The source's justification: once the augmented problem is considered, the optimal weight of the relevant assets is proportional to the residual component `Σ_u⁻¹ μ_u`, which can be sparse.
- **Economic claim in the abstract and §6.5:** sparse ("small-portfolio") structure "promotes stability and helps reduce turnover and trading frictions"; in the S&P 500 application FPS² "delivers competitive out-of-sample performance relative to benchmark portfolios, particularly in relatively stable market environments, while transaction costs materially weaken the gains from active rebalancing."

### Research interpretation

- **Mechanism class: estimation-error reduction by dimension reduction, not a directional forecasting signal.** The hypothesised channel is that a high-dimensional sample covariance/mean estimate of the mean–variance weights is dominated by noise, while a screened, low-dimensional re-estimate has materially lower estimation variance; any *return* effect must come from the screened set containing assets with persistent risk-adjusted mean, and from the defactoring step removing factor noise before screening. In falsifiable terms: *screening should reduce out-of-sample weight error and raise out-of-sample Sharpe relative to the same estimator on the unscreened universe, at matched cost.*
- **Role of each component (hybrid structure):**
  - Screen: Lasso of a constant on (defactored) returns over a J-week window → selected set Ŝ.
  - Estimation: post-Lasso OLS on `[R_Ŝ, FF3]` over the most recent ℓ < J weeks, target-return scaling with Kan–Zhou (2007) bias correction.
  - Regime claim (source-stated, ours to test): the mechanism works in "relatively stable" regimes and degrades in "highly unstable" ones.
  - Cost/turnover: **not a component of the source's mechanism** — costs enter only as an ex-post proportional charge in the evaluation (§6.3).
- The source itself names the missing link for us: it reports only *point estimates* of Sharpe and turnover, so whether the screening step adds anything **net of its own turnover** is exactly what remains unproven.

## Signal

All items below are source-reported unless explicitly marked `research-proposed` / `research-defined`.

- **Formation timestamp.** At each rebalance date t the method uses the trailing J weekly observations ending at t (Fridays). Screening and weight estimation both run at t; **out-of-sample performance is evaluated on the realized return at t+1** (§6.2) → signal formed at week t close, applied to week t+1 return (next-week execution, no same-bar fill assumption stated).
- **Lookback.** Screening window `J ∈ {100, 200, 300}` weeks (baseline; `J = 500` reported only as a long-window stress test in Table E.1). Post-screening estimation uses only the most recent `ℓ = 50 + |Ŝ|` observations inside the same J-week window (§6.4), with the source asserting ℓ < J in all empirical specifications.
- **Long entry / short entry / exit.** No long-only or no-short-sale constraint is stated anywhere in the pinned body (`long-only`, `short-sale`, `no-shorting`, `borrow` → 0 word hits). The weights come from an unconstrained target-return formula, so **the source-implied position set is unrestricted-sign**; entry/exit are not event rules but a **full weekly re-estimate of the entire weight vector**. Whether negative weights are actually realized is `not stated in source`.
- **Position sizing.** Target return `ρ̄ = (1+0.10)^(1/52) − 1 = 0.001835` (10 % p.a. under 52 weeks), weights scaled by eq. (6.1) `ŵ = ρ̄(1+θ̂)/θ̂ · (R'R)⁻¹R'1` with the Kan–Zhou (2007) bias-corrected `θ̂ = μ̂'Σ̂⁻¹μ̂`. **Gross exposure / leverage / position caps: not stated in source → `data gap`.**
- **Holding period / rebalance cadence.** Weekly re-estimation; no explicit holding-period cap, no deadband, no turnover penalty inside the optimisation.
- **Parameters (all source-reported).** `α = ρ̄` and `τ = 10⁻¹⁰` for the perturbed pseudo-response in the empirical screening step (§6.4); second-stage window `ℓ = 50 + |Ŝ|`; FMAXSER comparator uses sub-pool `N_sub = 50` and **10-fold CV** for its Lasso; **FPS²'s Lasso λ is chosen by the §5.2 k-fold procedure whose loss is the out-of-sample prediction error of the post-screening OLS over a prespecified grid (simulation uses `k = 10`, `M = 100` candidates with the admissibility restriction `|Ŝ| ≤ T(k−2)/k`).** For the empirical application §6.4 refers to "the selection procedure described in Section 5.2" **without restating k or the grid** → **empirical CV fold count and empirical λ grid are `underspecified`.**
- **Not reported anywhere:** the realized cardinality `|Ŝ|` in the empirical application, per-date selected names, weights, turnover decomposition, or any signal-strength statistic → the signal is **underspecified for exact independent reconstruction** (the estimator is reproducible in form, the realized portfolio is not reproducible from the paper).

## Required data

All source-reported.

- **Instrument / universe.** Union of all tickers that appeared in the S&P 500 between Jan 2000 and Nov 2025; master dataset after cleaning = **T = 1,350 weekly observations, 968 distinct tickers** (full list in Supplementary §E.2). The *investable* universe at each date is the point-in-time constituent set intersected with a complete-return-history requirement over the trailing J weeks, so **N varies from 361 to 498**.
- **Venue / market type.** Equities, cash/spot long–short book, US large caps; market type `spot` (no derivatives, no crypto).
- **Timeframe / fields.** Bloomberg **weekly adjusted closing prices sampled on Fridays**, converted to weekly log returns; risk-free (1-month T-bill) subtracted from raw log returns → weekly excess returns. FF3 (Mkt, SMB, HML) from the Ken French Data Library, used both for defactoring and as investable factors.
- **Point-in-time.** Historical constituent lists from `GitHub/fja05680/sp500` (source-reported; the source states this is to avoid survivorship bias); no statement about index-rebalance execution lags, corporate-action handling beyond "adjusted close", or delisting returns → `underspecified`.
- **Missing data (§6.1 cleaning, applied to the full sample).** (i) drop stocks with no valid observations; (ii) treat price spells constant for ≥3 consecutive weeks as missing (stale-price filter); (iii) drop stocks with internal gaps ≥5 weeks (missing or zero-return spells); (iv) drop stocks with >10 % missing/zero observations during their active period **or return history shorter than two years**. No imputation. **Research interpretation:** these are full-sample *ex-post* filters, i.e. a survivorship/availability screen computed with information not available at time t.
- **Not required by the source (therefore absent):** order book, trades/aggressor side, open interest, funding, mark/index/basis, options surface, borrow/locate data.

## Execution assumptions

Cost determination from a Methods-level read of §6.2 (implementation choice), §6.3 (evaluation strategy, including the explicit net-return recursion), §6.4 (parameter setup), §6.5 (results narrative), plus a word-boundary scan of the pinned v1 body.

- **Signal-to-order timing.** Weights estimated at t, performance taken on t+1 (next-week application). Order type, same-bar vs next-bar, partial fills, latency, market vs limit → **`not stated in source`**.
- **Quantified cost model (the only one that exists).** A **single** proportional one-way charge `τ_c = 0.001 (10 bps)` applied to one-way turnover `Σ_i |ŵ_{i,t} − ŵ⁺_{i,t−1}|` inside the excess-return recursion `r̂_{τc,t} = ŵ'_{t−1} r_aug_t − τ_c (1 + ŵ'_{t−1} r_aug_t) Σ_i |ŵ_{i,t} − ŵ⁺_{i,t−1}|` (Callot et al. 2021 form), with `ŵ⁺` the drift-adjusted prior weights. Justification given: "plausible for our large-cap stock universe", following Lee & Seregina (2024) and "broadly consistent with" Novy-Marx & Velikov (2016) and Frazzini et al. (2014). **One cost rung only — no ladder, no per-name cost, no half-spread.**
- **Turnover definition (reported alongside every net panel).** `Turnover = (T−J)⁻¹ Σ_{t=J+1}^{T} Σ_i |ŵ_{i,t} − ŵ⁺_{i,t−1}|` (per-week, summed across names, i.e. two-way-style absolute exposure traded per week).
- **Absent → `data gap`, never zero:** `slippage`, `bid-ask` as a priced term, `commission` as a priced term, `market impact`, `capacity`, `ADV`/`participation`, `borrow`/stock-loan, `latency`, `fill` model, `leverage`/`margin`, `liquidation`, `funding`, `dividend` treatment beyond adjusted close. `commission` and `bid-ask` each appear **once**, in §4.2, solely as the economic rationale for truncating numerically negligible weights — **not as a priced cost**; Monte Carlo experiments carry **no cost term at all**.
- **Shorting / borrow.** No long-only constraint and no borrow cost → short-leg feasibility and stock-loan pricing are `data gap`.
- **Capacity.** Not stated; the source argues qualitatively that sparsity "helps reduce turnover and trading frictions" while its own printed turnover is high (see Negative evidence).

## Evidence

### Source-reported

All figures are third-party claims from arXiv:2604.17593v1, marked source-reported, **not** independently reproduced. Gross = before the 10 bp charge; net = after the 10 bp charge. Table provenance is given for every block.

**Empirical design (§6.1–§6.4).** Bloomberg Friday adjusted close, first week of Jan 2000 → third week of Nov 2025, T = 1,350 weeks, 968 master tickers, N = 361–498 at each date, rolling J-week screening with one-week-ahead evaluation; sample splits: **overall** Jan 2000–Nov 2025 (evaluation length 1350−J), **pre-pandemic** Jan 2000–Dec 2019 (length 1042−J), **post-pandemic** Jan 2020–Nov 2025 (length 308).

**Table 5, PDF p.28 (column order FPS² | FM | QIS | FF3 | EW).**

| Panel | J | FPS² | FM | QIS | FF3 | EW |
|---|---|---|---|---|---|---|
| (i) gross overall | 100 | 0.082 | 0.082 | 0.046 | 0.051 | 0.029 |
| (i) gross overall | 200 | 0.102 | 0.053 | 0.066 | −0.036 | 0.033 |
| (i) gross overall | 300 | 0.100 | 0.082 | 0.073 | 0.042 | 0.030 |
| (iv) net overall | 100 | 0.019 | 0.009 | 0.010 | 0.038 | 0.028 |
| (iv) net overall | 200 | 0.042 | −0.031 | 0.031 | −0.047 | 0.032 |
| (iv) net overall | 300 | 0.044 | −0.010 | 0.040 | 0.035 | 0.029 |
| (ii) gross pre | 100 | 0.119 | 0.100 | 0.040 | 0.043 | 0.032 |
| (ii) gross pre | 200 | 0.122 | 0.056 | 0.063 | −0.051 | 0.038 |
| (ii) gross pre | 300 | 0.117 | 0.082 | 0.055 | 0.032 | 0.034 |
| (v) net pre | 100 | 0.050 | 0.012 | 0.004 | 0.030 | 0.031 |
| (v) net pre | 200 | 0.057 | −0.041 | 0.028 | −0.063 | 0.037 |
| (v) net pre | 300 | 0.052 | −0.015 | 0.020 | 0.023 | 0.033 |
| (iii) gross post | 100 | −0.009 | 0.047 | 0.060 | 0.082 | 0.021 |
| (iii) gross post | 200 | 0.049 | 0.054 | 0.072 | 0.051 | 0.021 |
| (iii) gross post | 300 | 0.068 | 0.087 | 0.109 | 0.096 | 0.021 |
| (vi) net post | 100 | −0.057 | 0.004 | 0.025 | 0.069 | 0.020 |
| (vi) net post | 200 | 0.002 | −0.015 | 0.039 | 0.044 | 0.020 |
| (vi) net post | 300 | 0.030 | −0.003 | 0.077 | 0.092 | 0.020 |

**Turnover rows of Table 5 (bracketed, source-reported):** net overall `[0.826][0.412][0.108][0.403][0.027]` (J=100), `[0.813][0.757][0.126][1.122][0.026]` (J=200), `[0.852][1.042][0.144][0.414][0.026]` (J=300); net pre `[0.844][0.446][0.104][0.426][0.026]`, `[0.868][0.729][0.120][1.449][0.025]`, `[0.932][0.902][0.137][0.520][0.026]`; net post `[0.773][0.307][0.121][0.330][0.028]`, `[0.664][0.833][0.145][0.229][0.028]`, `[0.659][1.378][0.160][0.158][0.028]` (column order FPS² | FM | QIS | FF3 | EW).

**Table E.1, PDF p.57.** Left panel (column order FPS² | FM | EW | QIS | FF3), J=500: gross overall `0.111 / 0.035 / 0.063 / 0.064 / 0.100`; gross pre `0.127 / 0.041 / 0.098 / 0.050 / 0.102`; gross post `0.083 / 0.031 / 0.024 / 0.082 / 0.100`; **net overall `0.055 / 0.017 / 0.062 / 0.024 / 0.095` with `[Turnover] [0.826][0.412][0.027][0.108][0.403]`**; net pre `0.065 / 0.022 / 0.097 / 0.008 / 0.095` with `[1.150][0.168][0.022][0.163][0.264]`; net post `0.037 / 0.015 / 0.023 / 0.043 / 0.097` with `[0.844][0.263][0.028][0.238][0.095]`. Right panel (FPS² | Market): gross overall `0.082/0.073, 0.102/0.080, 0.100/0.079`; gross pre `0.119/0.068, 0.122/0.077, 0.117/0.076`; gross post `−0.009/0.086, 0.049/0.086, 0.068/0.086`; net overall `0.019/0.073, 0.042/0.080, 0.044/0.079`; net pre `0.050/0.068, 0.057/0.077, 0.052/0.076`; net post `−0.057/0.086, 0.002/0.086, 0.030/0.086`.

**Our count on the printed cells (this Scout's arithmetic on the source's own tables):**

- FPS² vs **Market**: gross wins **6/9** (all of overall and pre, none of post); net wins **0/9** (loses in every cell) — consistent with §6.5's own statement that "in net terms, the market benchmark dominates FPS² throughout".
- FPS² **net** vs EW overall **2/3**, vs FF3 overall **2/3**, vs QIS overall **3/3**, vs FM overall **3/3**; pre-pandemic net **3/3 against all four** comparators; post-pandemic net vs EW **1/3**, vs FF3 **0/3**, vs QIS **0/3**, vs FM **2/3**.
- FPS² gross overall vs FM **2 wins + 1 tie** (J=100 is 0.082 vs 0.082); post-pandemic gross vs FM **0/3**, vs QIS **0/3**, vs FF3 **0/3**, vs EW **2/3**.
- **FPS² turnover is 0.659–0.932 per week across the Table 5 panels and 0.826–1.150 in the Table E.1 J=500 rows, versus EW's 0.025–0.028** — one to two orders of magnitude higher, i.e. the "sparsity promotes stability / lower turnover" claim is not what the printed turnover column shows relative to the passive benchmark.

**Simulation evidence (Tables 3 and 4; MSE normalised, true SR = 1).**

- Table 3 (DGP1/DGP2, MSE scaled by MAXSER): SR of PS² spans 0.74–1.38 across the 24 printed cells while QIS spans 1.05–2.55 and GL 1.00–2.13; **QIS SR > PS² SR in 24/24 cells, GL SR > PS² SR in 23/24** (our count); PS² MSE below QIS in 17/24 and below GL in 15/24 cells (our count).
- Table 4 (DGP3/DGP4 with strong factors, MSE scaled to the oracle FPS²-under-perfect-screening): **DGP3, N=500, T=200 → FPS² MSE = 34.44 × oracle (1.00)**; at N=500 the FPS² SR is 1.36 vs oracle 1.17 (T=200) and 1.06 vs 1.07 (T=500) — the source's own reading: large MSE gap but "the two estimators differ little in terms of SR".
- Screening properties (Tables 1–2 narrative, §5.5): PS² power/FDR "reasonably controlled except when T is very small relative to N"; MAXSER "over-selects when T > N and under-selects when T ≤ N"; FPS² screens correctly under strong factors while the original PS² "deteriorates because the screening step is contaminated by the strong common component".

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **No statistical inference anywhere in the pinned body:** `t-statistic`, `p-value`, `confidence interval`, `bootstrap`, `significance`, `Newey`, `information ratio` → **0 word hits**. Every empirical number is a point estimate over a single path; there is no test that FPS² beats any benchmark.
2. **No risk/return report beyond Sharpe:** `drawdown`, `CAGR`, `win rate`, `annualized` → **0 word hits**. §6.3 defines `SR = μ̂/σ̂` on the **weekly** excess-return series; whether the printed 0.019–0.122 values are intended as annualised is **`underspecified`** (conventional annualisation would multiply by √52, so the printed magnitudes look unannualised — our inference, not stated in source).
3. **Cost treatment is a single rung.** Only `τ_c = 0.001` is ever run; no ladder, no half-spread, no per-name cost. `slippage`, `bid-ask` (priced), `commission` (priced), `market impact`, `capacity`, `ADV`, `participation`, `borrow`, `latency`, `fill`, `leverage`, `margin`, `liquidation`, `funding`, `dividend` → **0 priced occurrences → `data gap`, never 0.** Monte Carlo has no cost term at all.
4. **Short leg is free and unverified.** No long-only / no-shorting statement in the body → weights may be negative while stock-loan cost, locate availability and hard-to-borrow names are entirely unmodelled.
5. **Turnover undermines the thesis.** FPS² trades 0.659–0.932 of its book *per week* (up to 1.150 at J=500 pre-pandemic) against EW's 0.025–0.028; at 10 bp one-way the annualised drag on a book that turns over ≈0.8/week is enormous, and the source runs no other cost level. Net of just the 10 bp charge FPS² already loses to the passive Market factor in **9/9** cells and, post-pandemic, to QIS and FF3 in **3/3** cells each.
6. **Single market, single frequency, single cost level, single target return.** US large-cap equities, weekly, 10 bp, ρ̄ = 10 % p.a.; no other asset class, no other rebalance frequency, no other cost.
7. **Ex-post full-sample data cleaning.** The ≥3-week-stale, ≥5-week-gap, >10 %-missing and <2-year-history rules are computed over the whole 2000–2025 sample (research interpretation: an ex-post availability filter that a live point-in-time process could not apply).
8. **The realised portfolio is unreproducible from the paper.** `|Ŝ|`, selected names, weights and per-date turnover decomposition are never printed; the empirical CV fold count and λ grid are not restated (§6.4 only cross-references §5.2).
9. **Four source-internal inconsistencies** are declared in the frontmatter `contradictions` block (Table 5 caption `–2025/12` vs panel `–2025/11`; the Table E.1 panel-(iv) J=500 turnover row duplicating Table 5 panel-(iv) J=100 turnover; the §5.5 "outperforms QIS and GL … SR" claim against Table 3(v); the §6.5 "net deteriorates further" wording against the printed J=500 net value, plus the "uniformly dominates FMAXSER" wording against a 0.082/0.082 tie).
10. **Theory does not cover the empirical process.** Condition 3(a) imposes temporal independence; the source explicitly says extensions "beyond temporally independent settings" and to heavier tails are "left for future work" (§7), while the data are weekly equity returns with serial dependence in the risk-free/turnover terms.
11. **No code, no data statement, empty Acknowledgments, Bloomberg-proprietary input** → independent reproduction is blocked on data access alone.
12. **Preprint only** (no journal-ref, no Comments, no peer-review statement), single cost rung, and no out-of-sample or forward window frozen after 2025-11.
13. **Cross-record contrary evidence (different source identities):** existing records in this repository on spread/mean-reversion and on active rebalancing show that honest cost and feasibility treatment materially erodes gross edges (e.g. the FASCL peer-basket record `arXiv:2602.10711` where 3 of 4 configurations go net-negative at 10 bp with turnover ≈0.32, and the cost-sensitive online window-aggregation record `arXiv:2609.29887` where 25 of 30 printed rows are simultaneously positive-mean and negative-Sharpe). These are **not** the same mechanism; they are recorded here only as cost-sensitivity priors.

## Falsification plan

Every threshold below is chosen by this Scout and is therefore labelled `research-defined` (acceptance/failure cutoff) or `research-proposed` (operational rule not in the source). No test is allowed to be rescued by re-tuning after the fact.

- **F1 — cost ladder (`research-defined`).** Re-run the empirical design with one-way proportional costs at 0/5/10/20/30/50 bp **plus** a paid half-spread modelled at 20 % of ADV per name (`research-proposed`; ADV data not used by the source). **Failure:** FPS² net SR ≤ EW net SR at the 10 bp rung in ≥2 of the 3 sample windows → the claim "screening survives realistic frictions" is rejected.
- **F2 — break-even cost (`research-defined`).** Compute per-name break-even one-way cost = mean weekly excess return ÷ weekly turnover for FPS². **Failure:** break-even ≤ 10 bp → the single reported rung is already past the edge.
- **F3 — point-in-time / survivorship repair (`research-defined`).** Rebuild the universe with point-in-time membership only and drop the ex-post §6.1 rules (iii) and (iv), keeping only information available at t. **Failure:** FPS² net SR at 10 bp falls below 50 % of the printed J=200 overall value (0.042 × 0.5 = 0.021) → the reported edge depends on the ex-post filter.
- **F4 — screening ablation (`research-defined`).** Replace Step-1 screening with (a) the full investable universe and (b) a random subset of the same weekly cardinality |Ŝ| (`research-proposed`), keeping Step 2 identical. **Failure:** FPS² gross SR is not above the 95th percentile of 1,000 random-subset draws, **or** is ≤ the full-universe post-Lasso OLS → the *screening* mechanism (Proposition 1 support recovery) is not doing the work.
- **F5 — defactoring ablation (`research-defined`).** Run PS² (no defactoring) against FPS² on identical windows. **Failure:** PS² ≥ FPS² in ≥2 of 3 windows → the source's claim that defactoring is required under strong factors is unsupported in this data.
- **F6 — parameter perturbation (`research-defined`).** Grid J ∈ {50, 100, 200, 300, 500} × second-stage base ℓ₀ ∈ {30, 50, 100} + |Ŝ| × ρ̄ ∈ {5 %, 10 %, 15 %}. **Failure:** the sign of (FPS² net SR − EW net SR) at 10 bp flips in ≥ half of the grid → result is a tuning artefact.
- **F7 — inference (`research-defined`).** 1,000-draw moving-block bootstrap (52-week blocks) on the weekly SR difference FPS² − EW and FPS² − Market at 10 bp. **Failure:** the 95 % interval includes 0 in the overall window → no evidence of superiority.
- **F8 — multiplicity (`research-defined`).** Benjamini–Hochberg at q < 0.10 across the full printed grid (5 methods × 3 windows × 2 cost states = 30 headline cells). **Failure:** fewer than half of FPS²'s "winning" cells survive → selection narrative.
- **F9 — forward window (`research-defined`).** Freeze parameters and evaluate on a window frozen after the source's sample end (2025-11), ≥12 months, weekly, with the same cost ladder. **Failure:** median net SR ≤ 0 or FPS² < EW in that window → regime-specific result.
- **F10 — borrow / long-only feasibility (`research-proposed`).** Impose a long-only constraint and a 50 bp/yr stock-loan fee on any residual short book. **Failure:** net SR at 10 bp falls below EW's → the unrestricted-sign result was a short-leg artefact.
- **F11 — cardinality / sparsity audit (`research-defined`).** Report the distribution of |Ŝ| over time. **Failure:** median |Ŝ| > N/2 → the "sparse support" premise does not hold in the empirical application (the source never prints |Ŝ|).
- **F12 — turnover decomposition (`research-defined`).** Decompose turnover into screening churn (names entering/leaving Ŝ) vs within-set reweighting. **Failure:** >75 % of turnover is screening churn → the edge, if any, is a name-switching artefact rather than weight estimation, and F4 becomes the binding test.

Action on failure (`research-defined`): mark the hypothesis `rejected` at research stage; no implementation, no Paper/Testnet request.

## Crypto portability

**unproven.**

- The pinned source contains **zero crypto evidence** — the only empirical application is S&P 500 equities on Bloomberg weekly bars.
- *Structurally* the recipe needs only a cross-sectional return panel, a factor/basis for defactoring, and weekly rebalancing, so it is **adaptable in form**: top-N liquid crypto spot or perpetual pairs, weekly Friday (or fixed-calendar) returns, market/basis defactoring with BTC/ETH factors instead of FF3, target-return scaling, and a short leg available via perps.
- *Blocking gaps for a crypto port:* no funding (charged every 8 h on perps), no mark/index-price convention, no liquidation/ bankruptcy mechanics, no venue-fragmented liquidity or borrow/locate model, 24/7 candles vs Friday close boundaries, no point-in-time "index membership" analogue (crypto listing/survivorship is far more aggressive than S&P 500 reconstitution), and the source's own cost model already omits spread and impact in the *easier* market.
- Because the source's only quantified friction (10 bp) is smaller than typical crypto taker fees plus spread on most pairs, a crypto implementation must be re-costed from scratch; **crypto portability is not authorization to trade.**

## Limitations

- `underspecified`: empirical CV fold count and λ grid; realised |Ŝ| and selected names; weights; gross exposure/leverage; long-only vs unrestricted signs; annualisation convention of the printed Sharpe; order type, fill and latency; per-name costs; dividend and corporate-action handling beyond adjusted close; index-rebalance lag; Tanaka's per-author affiliation; PDF creation date.
- `data gap`: all priced spread/slippage/borrow/impact/capacity/ADV/fill/latency/leverage/margin/liquidation/funding/dividend fields; any cost rung other than 10 bp; code and data availability (empty Acknowledgments, no data statement, Bloomberg-proprietary input).
- `not independently reproduced`: all source-reported performance figures.
- `unproven`: the causal claim that support recovery — rather than low-dimensional estimation alone — produces the reported gross edge; the regime claim ("stable vs unstable"); any net-of-honest-cost advantage.
- Identification limits: single path, no inference, ex-post data cleaning, ex-post pre/post-pandemic split, no placebo, no multiplicity control, theory assumes temporal independence, preprint status.
- Incremental-write check: this capture is a **new family for this repository** (Lasso support-recovery screening → post-Lasso mean–variance estimation); no prior record shares its source identity or its screening mechanism.

## Implementation status

`not-implemented`.

No code was written, no backtest was run, no NautilusTrader/Qlib/Paper/Testnet/Live component was touched by this record. Nothing in the research stack has been implemented, and this record does not modify any existing strategy family. The record is a research capture only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this record in the staging repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. Any adoption or implementation decision must be a separate, explicit review based on this record plus current sources.

## Related Wiki records

Wiki Brain read-only pre-write search (no Wiki write performed):

- `sparse portfolio selection Lasso screening mean variance` → **0 results**.
- `high dimensional portfolio selection sparse weights` → 6 broad-family pages (TDA/FinBERT mean–variance optimisation, hybrid ridgelet robust stat-arb, small-cap alpha–beta separation, Alpha-R1 factor screening, LSTM factor-replication stat-arb, Trading-R1) — all different mechanisms and different source identities; **none is a post-screening / support-recovery record, so no Wiki link is asserted and no page is fabricated.**
- `portfolio turnover transaction cost rebalancing mean variance` → 8 pages; the closest by family is `quant/smart-predict-then-optimize-spo-plus-robust-portfolio-2026-09-05.md` (decision-focused optimisation **under turnover costs**) — different mechanism (learned decision layer, not statistical screening), listed only as a retrieval neighbour.

Repo records checked for mechanism proximity (dedup evidence, all distinct source identities): `metric-dependence-screening-intraday-point-curve-ashare-selection-2026-09-25.md` (screening-stage asset selection, but Frechet point-curve dependence on intraday A-share curves), `decision-focused-sparse-tangent-portfolio-dpp-topk-2026-09-03.md` (sparse weights via determinantal top-k), `wasserstein-robust-portfolio-hyperplane-dual-lp-2026-09-02.md`, `moving-band-statistical-arbitrage-convex-concave-markowitz-2026-09-05.md`, `entropic-factor-model-robust-portfolio-replication-circuit-breaker-2026-09-04.md`, `cost-sensitive-online-window-expert-aggregation-hedge-fixed-share-2026-09-25.md` (rolling mean–variance window aggregation), `topological-risk-parity-*` record for `arXiv:2604.16773`. **Four-axis distinction:** source identity (arXiv:2604.17593 vs all of the above), mechanism (Lasso support-recovery screening + post-Lasso OLS under a support identity), signal construction (constant-on-returns Lasso without intercept, FF3 defactoring then factor re-inclusion), and material data dependency (Bloomberg S&P 500 weekly adjusted close with `fja05680` point-in-time membership) all differ.

## Sources

- Yoshimasa Uematsu, Shinya Tanaka, *Post-Screening Portfolio Selection*, arXiv:2604.17593v1 [q-fin.PM], submitted 19 Apr 2026 — https://arxiv.org/abs/2604.17593
- Pinned full text (HTML, 1,690,421 bytes, SHA-256 `da9e60282f0b8b1a3b3efe91886b00ec5606ecfb06a094e29f49e65c350e33b8`) — https://arxiv.org/html/2604.17593v1
- Pinned PDF (4,540,418 bytes, 60 pp., SHA-256 `aaa2c91462513159b06a28f46db36d5153523553c226195727c248fa8ca1bee6`) — https://arxiv.org/pdf/2604.17593v1
- DataCite DOI (arXiv-issued) — https://doi.org/10.48550/arXiv.2604.17593
- Source-reported data dependencies named by the paper, **not opened or verified by this Scout**: `GitHub/fja05680/sp500` (point-in-time S&P 500 constituent lists, paper footnote 3); Ken French Data Library `https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html` (FF3 + 1-month T-bill); Bloomberg (weekly adjusted close, proprietary).
- Cited-by-the-paper methodological anchors (identity only, not used as evidence here): Callot et al. (2021) turnover-cost recursion; Lee and Seregina (2024); Novy-Marx and Velikov (2016); Frazzini et al. (2014); Kan and Zhou (2007) bias correction; Ao, Li and Zheng (2019) MAXSER/FMAXSER; Ledoit and Wolf (2022) QIS; DeMiguel et al. (2009) 1/N; Brodie et al. (2009); Fan et al. (2012); Friedman et al. (2007) graphical lasso.

*Primary source opened, checksum-verified and read directly by this Scout on 2026-09-26; no figure in this record was taken from a secondary summary. Recorded under hard cap 1 (one record this run).*
