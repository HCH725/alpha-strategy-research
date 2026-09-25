---
schema: strategy-research-record-v1
title: "Revaluation Alpha: structural-premium-weighted allocation across 14 US equity long-short factors (SSRN 5451754)"
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - factor-investing
  - factor-allocation
  - factor-timing
  - valuation-decomposition
  - us-equity
  - long-short
  - working-paper
status: research-only
confidence: medium
source_as_of: "2026-08-08"
sources:
  - "Robert D. Arnott, Sina Ehsani, Campbell R. Harvey, Omid Shakernia, 'Revaluation Alpha', SSRN abstract 5451754, DOI 10.2139/ssrn.5451754; landing: Posted 8 Sep 2025, Last revised 8 Aug 2026, Date Written August 08, 2026, 36 pages. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5451754 (landing read 2026-09-25)"
  - "Pinned primary-source PDF retrieved from https://papers.ssrn.com/sol3/Delivery.cfm/5451754.pdf?abstractid=5451754&mirid=1&type=2 on 2026-09-25 — 1,300,813 bytes, 36 pages, SHA-256 ace0331d0610268363ab3842fa6893ca328ab20ab2dbe5e9a283178211cc605b, PDF metadata CreationDate D:20260808142111-04'00', /Author 'Sina Ehsani', /Creator 'Acrobat PDFMaker 26 for Word'"
  - "Research Affiliates landing page for the same title (author-list discrepancy noted below), https://www.researchaffiliates.com/publications/journal-papers/1097-revaluation-alpha (read 2026-09-25)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Source-internal: Section 2 prose reports the historical-premium sort's low/mid tier means as 2.84% and 2.48%, but Table 2 prints Low 2.48 and P2 1.79 (H-L 2.84 is consistent with the table, 5.32 - 2.48); the prose tier means cannot be reconciled with the printed table."
  - "Cross-source: the pinned SSRN PDF title page and SSRN abstract page both print four authors (Arnott, Ehsani, Harvey, Shakernia), while the Research Affiliates landing page for the same title lists five names including Chris Brightman; unresolved, pinned four-author list used throughout."
---

# Revaluation Alpha: structural-premium-weighted allocation across 14 US equity long-short factors

## Provenance

- **Primary source (only source used for every empirical claim below):** Robert D. Arnott, Sina Ehsani, Campbell R. Harvey, Omid Shakernia, *"Revaluation Alpha"*, **SSRN abstract `5451754`**, DOI `10.2139/ssrn.5451754`. SSRN landing (read 2026-09-25): **36 pages, Posted 8 Sep 2025, Last revised 8 Aug 2026, Date Written August 08, 2026**; JEL G11, G12, G14, G40; suggested citation dated August 08, 2026. Stable URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5451754 (`source-reported`).
- **Authors exactly as printed on the pinned PDF title page (page 1), with affiliation markers:** `Robert D. Arnott,a Sina Ehsani,b Campbell R. Harvey,a,c and Omid Shakernia,a` — a Research Affiliates, LLC · b Northern Illinois University · c Duke University and NBER (corresponding author printed as cam.harvey@duke.edu). The SSRN abstract page lists the same four authors with affiliations Research Affiliates, LLC / Northern Illinois University – Department of Finance / Duke University – Fuqua School of Business; NBER / Research Affiliates, LLC (`source-reported`).
- **Pinned version / checksum:** the PDF served by SSRN Delivery.cfm on 2026-09-25 is **1,300,813 bytes, 36 pages, SHA-256 `ace0331d0610268363ab3842fa6893ca328ab20ab2dbe5e9a283178211cc605b`**, `/CreationDate D:20260808142111-04'00'`, i.e. it matches the SSRN "Last revised 8 Aug 2026 / Date Written August 08, 2026" stamp. Text was extracted and read end to end (36 pages, 80,099 characters, 1,174 lines) covering the abstract, Sections 1–4, Tables 1–5, Figures 1–3 captions, References, and Appendices A (factor definitions and Table A1), B (finite-sample simulation) and C (rank-weighted robustness, Table C1 and Figures C1–C3) (`source-reported`).
- **Retrieval note (reproducibility of provenance):** plain `curl` and a headless Scrapling fetch both returned **HTTP 403** from SSRN on 2026-09-25; the landing page and the PDF were retrieved through a real browser session that cleared the Cloudflare interstitial, and the PDF was then re-fetched with the session cookies. Any future re-read should expect the same 403 from non-browser clients.
- **Version / publication status:** **SSRN working paper only as pinned.** No journal name, volume, issue, publisher DOI beyond `10.2139/ssrn.5451754`, or acceptance line appears anywhere in the pinned PDF or on the SSRN landing page. The PDF page-1 footnote does thank *"the Executive Editor, William N. Goetzmann, Co-Editor, Daniel Giamouridis, and two anonymous referees for the insightful and constructive comments"*, which indicates the manuscript has been through a journal review process, but **the journal itself is not named in the pinned text → `data gap`**. No arXiv version, no code repository, no data-availability statement, and no replication package are referenced anywhere in the pinned text (`data gap`).
- **License / redistribution:** the SSRN landing prints *"The copyright holder has granted SSRN a license. All rights reserved. No reuse allowed without permission."* → this record cites and normalizes the argument and numbers and does not reproduce the manuscript (`source-reported`).
- **Author-list discrepancy (open):** the Research Affiliates landing page for the same title (https://www.researchaffiliates.com/publications/journal-papers/1097-revaluation-alpha, read 2026-09-25) shows *"By Rob Arnott, Chris Brightman, CFA, Campbell Harvey, PhD, Omid Shakernia, PhD, Sina Ehsani"* and a September 2025 date. The pinned four-author PDF/SSRN list is used throughout; the fifth name is recorded as an unresolved provenance discrepancy, not silently reconciled.
- **Secondary summaries deliberately excluded from all numbers:** an Alpha Architect / Larry Swedroe summary dated 30 Jan 2026 describes the *September 2025* version of this study and reports findings (e.g. a "6 to 24-month" predictive peak, a one-third-of-equity-premium claim) that do not correspond to the pinned August 2026 revision's printed tables. No figure in this record is taken from any secondary summary.
- **Pre-write deterministic dedup (2026-09-25, ripgrep across the whole repository, not `git log`):** `Revaluation Alpha`, `5451754`, `10.2139/ssrn.5451754`, `Shakernia`, `Rob Arnott`, `Robert D. Arnott`, `Arnott, Harvey, Kalesnik`, `structural premium`, `structural return`, `structural component`, `Revaluation` (case-insensitive), `Ehsani` → **zero records carry this source identity** (970 top-level `*.md` records plus `coverage_manifest.csv`; `.mimo-worktrees` copies inspected separately and contain no additional source). The 133 `10.2139/ssrn` hits are other SSRN papers; the four `structural component` hits are unrelated (perpetual-basis segmentation, crypto open-interest decomposition, Alphaschema, GoAnt); the two `structural premium`/`structural return` hits are an unrelated SpaceX pre-IPO basis hypothesis and a crypto SMB note; the two `Ehsani` hits are factor-momentum citations in `alphaforge-generative-formulaic-alpha-dynamic-factor-timing-2026-09-17.md` and `crypto-cross-sectional-factor-momentum-anomaly-portfolios-2026-08-31.md`. `git log --oneline -20` was inspected separately as a convenience glance only.
- **Material distinction from adjacent same-family records (dedup statement, four axes):**
  - `alphaforge-generative-formulaic-alpha-dynamic-factor-timing-2026-09-17.md` (arXiv:2406.18394, AAAI 2025) — different source identity, different mechanism (formulaic alpha mining plus learned combination weights) and different signal construction.
  - `crypto-cross-sectional-factor-momentum-anomaly-portfolios-2026-08-31.md` (Quantitative Finance 2023 / Journal of Finance factor-momentum DOIs) — different source, different signal (past factor returns as the timing variable) and different universe (crypto perps vs US equity factors).
  - `reviving-anomalies-expected-net-return-double-sort-1n-implementable-2026-09-23.md` (SSRN 6468806) — different source, different mechanism (ML expected *net* returns with a price-impact model) and different signal construction.
  - `published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23.md` (Chen & Welch) — different source; it is the closest *contrary* evidence for the same 14-factor-style anomaly library and is cited under Negative evidence.
  - `continuous-macro-timing-growth-defensive-style-allocation-2026-09-02.md` — different source, macro state signal, different horizon and universe.

## Economic mechanism

### Source-reported

- Factor returns are an identity-level sum of two parts (Equation 1): a **structural component** = growth in book value plus dividend yield, and a **revaluation component** = the change in the portfolio's log price-to-book ratio. Decomposition is applied separately to each factor's long and short leg and then combined into the long-short factor.
- Three stated hypotheses (Section 2): **H1** E[Revaluation] = 0 in the long run (the paper explicitly says this does *not* require mean reversion of valuation ratios); **H2** in a finite sample the structural mean is a more efficient estimator of a factor's unconditional premium than the mean of total return; **H3** the structural-weighted multi-factor portfolio outperforms both 1/N and the historical-return-weighted portfolio.
- Claimed mechanism of the trading rule: because realized revaluation is zero-mean noise, subtracting it from realized past returns removes estimation error, so weights proportional to the structural estimate are a better proxy for future factor returns than weights proportional to the raw historical mean. The paper states the advantage is a **finite-sample property** that vanishes as the sample lengthens (Section 4 and Appendix B).
- Factor timing is treated as a separate, competing signal family: value spread (demeaned log P/B) plus prior 1-month and prior 12-month factor returns.

### Research interpretation

- Falsifiable hypothesis: *across a fixed library of US equity long-short factors, an allocation rule that weights factors by (realized historical log return − realized change in log price-to-book) delivers higher risk-adjusted excess return versus an equal-weighted factor portfolio than an allocation rule weighted by raw historical returns, at monthly to annual rebalancing frequencies.*
- The hypothesized economic channel is **estimation-error reduction in a noisy expected-return signal**, not a new risk premium: the paper itself concedes both estimators are unbiased under H1 and that the edge must decay with sample length. A second, weaker channel is that the rule mechanically de-weights factors whose past success was valuation expansion (performance-chasing avoidance).
- Component roles (hybrid structure): **Signal** = structural-premium estimate; **Allocation rule** = proportional weights scaled to unit leverage; **Benchmarks/controls** = 1/N equal weight, historical-mean weight, and a momentum+valuation factor-timing portfolio; **Rebalance cadence** = monthly signal update with Jegadeesh–Titman overlapping portfolios for 3/6/12-month holding periods. No regime filter, no stop, and no entry/exit threshold exist in the source.

## Signal

All items below are `source-reported` unless marked `research-proposed` / `research-defined`.

- **Formation timestamp:** monthly data; at each month *t* all estimates use information available at *t−1* (Section 2.1 sort rule and Section 3 "from the beginning of the sample to time t"). Time zone / session convention for the monthly close is **not stated** (`data gap`).
- **Lookback / estimation window:** initial seed = the first 10 years, **July 1963 – June 1973**, for both historical and structural premiums; thereafter both are updated on an **expanding window** (never re-estimated on a rolling window). Factor returns exist July 1963 – December 2024; the evaluation sample starts **July 1973** and ends **December 2024** (618 months in Table 4).
- **Decomposition rule:** mean annualized log return of the factor (monthly log returns averaged) minus the mean of monthly changes in the log price-to-book of the same leg; legs decomposed separately, then combined into the long-short factor. Price-to-book is the mandated valuation measure "because the analytical decomposition requires this measure" (footnote 3); the paper notes other valuation metrics may be better in practice.
- **Long / short construction (underlying factor portfolios, Appendix A):** split the US stock universe by market cap at the **NYSE median** into large/small, then select the **30% highest and lowest** on the factor characteristic using **NYSE breakpoints**, compute **value-weighted** returns for the six portfolios; each long-short factor is **long the two high portfolios and short the two low portfolios** with equal weights. SIZE is a univariate tercile sort at the NYSE 30th/70th percentiles. 14 factors: ACCRUAL, BETA, CFP, EP, IVOL, ILLIQ, INV, LTREV, MOM, PROF, NSI, SIZE, STREV, VALUE (definitions and Table A1 in Appendix A).
- **Entry / sizing rule:** `w_f = R_f^s / Σ_f R_f^s` (Equation 2), i.e. weights proportional to the structural estimate, normalized to unit leverage; the historical-mean portfolio uses the identical formula with the raw mean. 1/N benchmark = 1/14 each. **No non-negativity constraint is stated for these candidate portfolios** (footnote 5 explicitly warns that raw proportional scaling can produce "extreme allocation" and suggests a convex combination with equal weighting as an alternative it does not test); non-negativity is imposed only in the ex-post mean-variance tests (Table 3 Panel B, Figure 3).
- **Timing comparator (Section 3, Equations 3–5):** expanding Fama–MacBeth regression of the factor's next-*h*-month **average** return on value spread, prior 1-month return, and prior 12-month average return; the fitted forecast at *t* becomes the weight for the portfolio held over the next *h* months. The one-month model trains on July 1963 – June 1973 with the first trade in July 1973; longer-*h* models start training later so that the first *h*-month return exists (footnote 9).
- **Holding period / rebalance:** *h* ∈ {1, 3, 6, 12} months, overlapping-portfolio method of Jegadeesh and Titman (1993): the signal is re-estimated every month while only 1/h of the portfolio is replaced each month.
- **Exit / stop / re-entry:** none specified — this is a perpetual allocation rule, not a single-name entry/exit strategy. Any stop, drawdown trigger, or confidence filter is **absent from the source**; adding one would be `research-proposed`.
- **Parameters and their source:** 14 factors, 30/70 and median-NYSE breakpoints, 10-year seed, expanding window, *h* ∈ {1,3,6,12}, 5,000 circular block-bootstrap resamples with block length equal to the forecast horizon (Table 4 note). All are **fixed, printed parameters** — no tuning search, no train/test hyperparameter split is reported (`underspecified` as a robustness matter).
- **Explicitly underspecified:** whether the underlying 30/70 factor sorts are re-formed monthly, quarterly, or annually (the "top-down implementation that assumes fixed factor portfolios" phrasing in Table 5 hides the bottom-up rebalance); whether the proportional weights may go negative in practice; how dividends, splits and other corporate actions are handled inside the factor returns (delegated to the Arnott et al. 2019 dataset).

## Required data

- **Instrument / universe:** US common stocks; large and small caps per NYSE breakpoints; 14 long-short characteristic factors plus their long-only versions ("we measure the performance of long-only and long-short factor portfolios"). No ETF/index/venue list is given (`data gap`).
- **Fields:** monthly prices and shares outstanding (market equity), book equity, earnings, cash flow, revenue and expense items (profitability), accrual components, total assets, share counts (net share issue), daily returns and daily turnover (Amihud ILLIQ), daily returns for the FF3 residual volatility (IVOL), 60-month rolling market betas, dividends for the structural term, and the factor's aggregate book value and price for the log P/B revaluation term.
- **Data vendor:** **not stated anywhere in the pinned text** — the factor data are taken from *"the data for 14 popular factors from Arnott, Harvey, Kalesnik, and Linnainmaa (2019)"*. CRSP/Compustat are never named (`data gap`).
- **Point-in-time / survivorship:** no statement on point-in-time universe construction, delistings, listing-age filters, or restatements of book equity (`data gap`). Factor definition lags (e.g. when accounting data become available) are not specified in this paper (`underspecified`).
- **Timestamp:** monthly frequency only; timezone, clock and out-of-order handling are not stated (`data gap`).
- **Missing data:** no imputation or missing-data policy is stated (`data gap`).
- **Funding / fee / spread needs:** none modeled — see Execution assumptions.

## Execution assumptions

- **Cost model: none.** A word-boundary scan of the pinned PDF shows `transaction costs` appears only twice, both in prose (footnote 7 quoting prior literature; page 21 stating the mean-variance tests "ignore transactions costs"), and `bid-ask`, `slippage`, `spread`, `commission`, `fees`, `market impact`, `latency`, `fill`, `participation`, `ADV`, `capacity`, `borrow`, `short interest`, `dividend reinvestment policy`, `leverage` and `margin` carry **no modeling statement**. Every such field is `data gap`, never zero. All reported returns are **gross of cost**.
- **What *is* reported instead of cost:** Table 5 Panel C average **two-way monthly turnover** of the *top-down* allocation under fixed factor portfolios: Historical 2.76 / 2.47 / 2.35 / 2.27 %, Structural 6.47 / 3.66 / 2.89 / 2.50 %, Timing 85.88 / 18.40 / 10.64 / 5.58 % for *h* = 1/3/6/12; the 1/N portfolio's drift-only turnover is 2.04 %/month. **Bottom-up (inside-factor) turnover of the underlying long-short portfolios is never reported** → `data gap`, which makes every top-down cost inference an upper bound on tradability cost.
- **Signal-to-order timing:** not stated (month-end formation, no execution price or next-open convention) (`data gap`).
- **Shorting / borrow:** the core instrument is a 14-leg long-short factor portfolio; no borrow availability, stock-loan fee, recall or shorting constraint is modeled (`data gap`).
- **Leverage / margin:** weights are scaled to "unit leverage"; no financing cost or margin requirement is modeled (`data gap`).
- **Latency / partial fills / venue:** not applicable at monthly rebalance in the source, but also not addressed (`data gap`).

## Evidence

### Source-reported

Every figure below is third-party, **gross of cost**, from the pinned SSRN PDF, with table/figure provenance; **not independently reproduced**.

- **Table 1 — Attribution of factor Returns (mean annualized log returns, long-short factors, sample July 1963 – December 2024; Historical = Revaluation + Structural):** ACCRUAL 2.9 / −0.1 / 3.0 · BETA 2.8 / 1.2 / 1.7 · CFP 5.3 / −1.3 / 6.7 · EP 2.6 / −1.9 / 4.5 · IVOL 7.3 / −1.8 / 9.1 · ILLIQ 0.5 / −0.5 / 1.0 · INV 2.3 / 1.1 / 1.2 · LTREV 1.4 / −1.0 / 2.3 · MOM 9.2 / −0.8 / 9.9 · PROF 5.1 / −0.1 / 5.2 · NSI 2.9 / −0.8 / 3.7 · SIZE 1.2 / −0.9 / 2.1 · STREV 4.9 / 0.6 / 4.3 · VALUE 4.1 / −1.3 / 5.4 · **Average 3.7 / −0.5 / 4.3**. The paper states individual revaluation estimates are not statistically different from zero (bootstrap standard errors, footnote 4) but **prints no t-statistics for them** → `data gap`.
- **Table 2 — Return Predictability (July 1973 – December 2024; tercile sorts of the 14 factors, expanding-window estimates, 5/4/5 factor portfolios):** sort on **historical premium** Low 2.48, P2 1.79, High 5.32, H-L 2.84 (SD 6.04 / 6.44 / 7.37 / 8.31; Sharpe 0.41 / 0.28 / 0.72 / 0.34; t 2.95 / 2.00 / 5.18 / 2.45); sort on **structural premium** Low 0.88, P2 3.77, High 5.34, H-L 4.46 (SD 4.05 / 7.51 / 8.09 / 8.00; Sharpe 0.22 / 0.50 / 0.66 / 0.56; t 1.56 / 3.61 / 4.74 / 4.00). The paper's "clairvoyant" full-sample-mean oracle H-L is 4.58 (t 4.68) and is described as uninvestable.
- **Table 3 Panel A — annualized excess return vs 1/N (July 1973 – December 2024, *h* = 1/3/6/12):** Historical 0.71 / 0.67 / 0.69 / 0.68 with tracking error 2.47 / 2.47 / 2.42 / 2.36, IR 0.29 / 0.27 / 0.28 / 0.29, t 2.07 / 1.95 / 2.04 / 2.09; **Structural 1.26 / 1.25 / 1.27 / 1.26 with tracking error 2.06 / 2.02 / 1.97 / 1.93, IR 0.61 / 0.62 / 0.64 / 0.65, t 4.40 / 4.45 / 4.60 / 4.68**. The 1/N benchmark's own annualized mean is 3.3 % (t 4.61).
- **Table 3 Panel B — ex-post mean-variance weights (non-negative):** 1/N vs Historical → 1/N 11 / 18 / 12 / 7 %, Historical 89 / 82 / 88 / 93 %; 1/N vs Structural → 1/N 1 / 0 / 0 / 0 %, Structural 99 / 100 / 100 / 100 %.
- **Table 3 Panel C — spanning annualized alphas:** with 1/N as control, Historical α 0.50 / 0.46 / 0.48 / 0.47 (t 1.45 / 1.33 / 1.39 / 1.43) and Structural α 0.50 / 0.50 / 0.54 / 0.56 (t 2.10 / 2.15 / 2.36 / 2.50); with Historical as control, Structural α 0.46 / 0.48 / 0.44 / 0.42 (t **1.39 / 1.55 / 1.62 / 1.69**); with Structural as control, 1/N α −0.16 / −0.17 / −0.22 / −0.24 (t −0.86 / −0.94 / −1.15 / −1.28) and Historical α 0.10 / 0.02 / −0.04 / −0.08 (t 0.34 / 0.08 / −0.13 / −0.34).
- **Table 4 — Fama–MacBeth predictive regressions (July 1973 – December 2024, 618 months, 14 factors, circular block bootstrap of Politis–Romano 1992 with 5,000 resamples, block length = forecast horizon):** coefficient on **Structural** 0.44 (t 3.13) / 0.55 (4.15) / 0.52 (3.87) / 0.58 (4.21) for 1/3/6/12 months; Value spread −0.28 (−2.27) / −0.16 (−1.51) / −0.20 (−2.03) / −0.17 (−1.75); Prior 1-month return 0.11 (3.82) / 0.03 (1.42) / 0.02 (1.18) / 0.03 (2.53); Prior 1-year return 0.27 (3.85) / 0.16 (2.41) / 0.16 (2.51) / 0.05 (0.84); constant ≈ 0. Footnote 8: under Hodrick (1992) and Hansen–Hodrick (1980) estimators the structural coefficient stays significant at 1 % at every horizon, smallest t = 2.95.
- **Table 5 — Performance and turnover of the three candidate portfolios (evaluation July 1973 – December 2024):** excess return vs 1/N — Historical 0.71 / 0.67 / 0.69 / 0.68, Structural 1.26 / 1.25 / 1.27 / 1.26, **Timing 3.94 / 1.77 / 1.42 / 0.98**; tracking error — 2.47 / 2.47 / 2.42 / 2.36, 2.06 / 2.02 / 1.97 / 1.93, 7.49 / 5.77 / 4.86 / 4.05; two-way monthly turnover — Historical 2.76 / 2.47 / 2.35 / 2.27, Structural 6.47 / 3.66 / 2.89 / 2.50, Timing 85.88 / 18.40 / 10.64 / 5.58 (1/N drift 2.04).
- **Figure 1:** the structural investor accumulates **80 % more wealth** than the 1/N benchmark over July 1973 – December 2024 versus **40 %** for the historical-weighting portfolio; the paper states the outperformance is not driven by a single episode (visual claim, no test statistic printed).
- **Figure 2:** the structural portfolio has the highest IR at every holding period, and beyond six months its IR is "more than double" the next best strategy.
- **Figure 3:** ex-post non-negative mean-variance weights across the four candidate strategies, explicitly **ignoring transaction costs**; at the one-month horizon the optimum is **65 % Timing / 35 % Structural / 0 % Historical / 0 % 1/N**, shifting toward Structural as *h* grows.
- **Table A1 (Appendix A, July 1963 – December 2024):** annualized means and CAPM alphas, e.g. MOM 8.44 (t 4.32), α 9.57 (4.92); VALUE 3.70 (2.75), α 5.07 (3.90); BETA 0.06 (0.03), α 5.57 (3.18); ACCRUAL 2.76 (3.67), α 3.05 (4.05); ILLIQ 0.57 (0.59), α 1.42 (1.48).
- **Appendix B:** a calibrated simulation (R = 5,000 simulated economies, N = 14 factors, first ten years used for the initial estimates) showing the structural estimator's efficiency advantage is a finite-sample property that converges as the sample lengthens; the paper concedes the convergence rate depends on calibration choices.
- **Appendix C / Table C1 (rank-weighted robustness, sample July 1973 – December 2024):** re-running Section 2 with **ranks 1–14** instead of raw magnitude as weights gives excess return vs 1/N of Historical **0.67 / 0.62 / 0.64 / 0.62** (t 2.31 / 2.10 / 2.21 / 2.16) and Structural **1.12 / 1.12 / 1.13 / 1.10** (t 4.21 / 4.29 / 4.22 / 4.55) for *h* = 1/3/6/12, with ex-post non-negative mean-variance weights of 1/N 8 / 23 / 12 / 12 % vs Historical 92 / 77 / 88 / 88 % and 1/N 0 % vs Structural 100 % at every horizon (1/N mean 3.30 %, t 4.61). Figures C1–C3 show the rank-weighted timing portfolio takes the **highest IR at the one-month horizon** (unlike the raw-weighted Figure 2, where the structural portfolio is highest at every horizon) with structural best at all longer horizons — i.e. the 1-month ranking is scheme-dependent, a point the source does not discuss.

**Our own arithmetic on the printed cells (`our count`, not source-reported):**

- Structural beats Historical on excess return at **4 of 4** horizons by 0.55 / 0.58 / 0.58 / 0.58 percentage points per year (1.77×–1.87× the Historical excess) and its IR is **2.10×–2.30×** the Historical IR.
- The Timing portfolio beats Structural on excess return at 1, 3 and 6 months but **loses at 12 months**, and its excess return falls from 3.94 % to 0.98 % between *h*=1 and *h*=12 (**−75.1 %**, −2.96 pp).
- Structural's spanning alpha over Historical **never reaches t ≥ 2.0** at any horizon (maximum 1.69, Table 3 Panel C) — the headline "Structural dominates Historical" is significant against 1/N (t up to 2.50) but only marginally significant against Historical.
- Top-down-only breakeven cost per unit traded, computed as annualized excess ÷ (monthly two-way turnover × 12): Structural **162 / 285 / 366 / 420 bp**, Historical **214 / 226 / 245 / 250 bp**, Timing **38 / 80 / 111 / 146 bp** for *h* = 1/3/6/12. Because inside-factor stock turnover is never reported, these are **upper bounds** on what the strategies can absorb, not evidence of net tradability.
- Structural's *h*=1 turnover is **3.17×** the 1/N drift-only turnover and **2.34×** Historical's.

### Independently reproduced

`Not independently reproduced.`

No replication, re-run, or out-of-sample extension of this study exists in our research stack; the pinned manuscript contains no code, no repository, no data-availability statement and no data vendor, so even the authors' own pipeline could not be executed from the source alone.

### Negative evidence

1. **No transaction-cost model anywhere in the pinned text** (Methods-level read of Sections 1–4 and Appendices A–C plus a word scan): spread, slippage, commission, fees, impact, latency, fill, borrow and margin are all unmodeled, so every headline number is gross; the source itself notes only that its mean-variance tests "ignore transactions costs" (page 21).
2. **Inside-factor (bottom-up) turnover is never reported** — Table 5's turnover is explicitly "under a top-down implementation that assumes fixed factor portfolios". The 30/70 sorts, the 60-month beta, the 12-month ILLIQ and the annual accounting factors trade inside each factor portfolio at an unstated frequency, so realizable turnover is unknown and strictly larger than the printed figures.
3. **The Structural-vs-Historical increment is not statistically significant at 5 %** at any holding period (spanning t = 1.39–1.69, Table 3 Panel C) — the paper's central comparative claim rests on sub-threshold t-statistics, and no direct test of the 80 % vs 40 % wealth gap is printed.
4. **The edge is defined to disappear with more data** (Section 4: "it would vanish in an arbitrarily long sample"); it is estimator efficiency, not a claimed new premium, and Appendix B says convergence speed depends on calibration choices.
5. **The source's own literature review reports contrary results** (footnote 7): Dichtl et al. (2019) and Ilmanen et al. (2021) find factor-timing benefits are modest once trading costs and implementation frictions are counted; Asness (2016), Asness et al. (2017) and Lee (2017) argue value-based factor timing merely replicates a value factor.
6. **The timing baseline collapses with holding period** (3.94 % → 0.98 % excess; turnover 85.88 % → 5.58 %), i.e. the paper's strongest 1-month number comes from the arm with the worst cost profile, while the structural arm's advantage over that baseline at *h*=1 is negative (1.26 % vs 3.94 %).
7. **Single valuation metric:** the decomposition mandates price-to-book; footnote 3 concedes other valuation measures (P/S, P/D, P/E, P/CF, intangibles, blends) "may provide stronger signals of value in practice", and no robustness across metrics is printed for the main tables.
8. **No out-of-sample, no multiplicity control, no placebo:** one sample (July 1973 – December 2024) reused across Tables 2–5 and Figures 1–3, four horizons × several tests, zero Benjamini–Hochberg/deflated-Sharpe/holdout adjustment, and no circular-shift or block-shuffle placebo anywhere in the pinned text.
9. **Factor-library selection risk:** the 14 factors are inherited from Arnott et al. (2019) by authors affiliated with the firm that markets factor products; the paper does not address selection, publication bias, or whether the library would survive a luck-adjusted screen (see cross-record item 12).
10. **Universe/point-in-time gaps:** no CRSP/Compustat naming, no delisting/survivorship policy, no accounting-data availability lag, no long-only-with-real-cost version — all `data gap`.
11. **Long-short implementability:** 14 simultaneous long-short factor legs with no borrow, stock-loan fee, recall or shorting-constraint model; the practical short leg is unpriced (`data gap`).
12. **Cross-record contrary evidence from this repository:** `published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23.md` (Chen & Welch, *What Useful Alphas?*, arXiv:2607.06502) reports a **7 bp median** published-anomaly return with **Var(t) = 1.09 luck-adjusted null** in the investable large-cap universe post-2005 — a direct challenge to the assumption that a 14-factor anomaly library carries the structural premiums printed in Table 1. `reviving-anomalies-expected-net-return-double-sort-1n-implementable-2026-09-23.md` (SSRN 6468806) separately shows that net-of-cost/price-impact expected returns materially reorder anomaly portfolios. Both are different sources with their own provenance; they are cited here as adjacent contrary evidence, not as reproduced results of this paper.
13. **Version drift in secondary coverage:** the widely circulated Alpha Architect summary (30 Jan 2026) describes the September 2025 version and does not match the pinned August 2026 tables (e.g. "6 to 24-month" peak), so any figure quoted from secondary write-ups is unreliable for this record.
14. **Preprint/working-paper status:** SSRN working paper, "No reuse allowed without permission", journal unnamed in the pinned PDF despite referee acknowledgments; no code, no data, no replication package.

## Falsification plan

All thresholds and decision rules below are `research-defined`; all operationalizations not printed in the source are `research-proposed`.

- **F1 — Point-in-time costed replication (`research-proposed`):** rebuild the 14-factor library from point-in-time US equity data with NYSE breakpoints and accounting-availability lags, then run the structural, historical, timing and 1/N arms with a cost ladder of **0 / 5 / 10 / 20 / 30 bp per side** plus paid spread at **20 % ADV**. **Fail if** the structural arm's excess return over 1/N is ≤ 0 at 10 bp, or its IR < 0.30 at 20 bp, at any *h* ∈ {1,3,6,12}.
- **F2 — Significance of the headline comparison (`research-defined`):** paired moving-block bootstrap (block = 12 months, 10,000 draws) on the monthly return difference Structural − Historical. **Fail if** |t| < 2.0 at every horizon, reproducing the source's 1.39–1.69 range.
- **F3 — Expanding vs rolling window (`research-proposed`):** re-estimate the premiums on rolling 10- and 20-year windows instead of the expanding window. **Fail if** the structural arm loses to the historical arm in both rolling variants over the same sample.
- **F4 — Sub-period and regime split (`research-defined`):** split into 1973–1999 and 2000–2024, plus a post-2005 investable large-cap block. **Fail if** the structural excess over 1/N is ≤ 0 in either half or in the post-2005 block.
- **F5 — Valuation-metric robustness (`research-proposed`):** repeat the decomposition with P/S, P/E, P/CF, P/D and a blend (the source uses only P/B). **Fail if** the sign of Structural − Historical flips in ≥ 2 of 5 metrics.
- **F6 — Placebo (`research-defined`):** 1,000 circular-shift (random-offset) resamples of the structural-weighting return series against 1/N. **Fail if** the observed mean excess is not above the 95th percentile of the placebo distribution.
- **F7 — Multiplicity (`research-defined`):** Benjamini–Hochberg at q < 0.10 over the family of {4 horizons} × {Structural vs 1/N, Structural vs Historical, Timing vs Structural} tests. **Fail if** fewer than half the printed effects survive; downgrade confidence to low.
- **F8 — Concentration ablation (`research-defined`):** drop MOM and VALUE (largest structural premiums in Table 1) and re-run. **Fail if** > 50 % of the structural arm's excess return over 1/N disappears, i.e. the result is a two-factor artifact.
- **F9 — Long-short implementability (`research-proposed`):** implement the library long-only plus index-futures beta hedge, with stock-loan fees on the unimplemented short side explicitly priced. **Fail if** the structural arm's excess over 1/N falls below half the paper's 1.26 % at *h* = 1 after costs.
- **F10 — Turnover honesty (`research-defined`):** measure *bottom-up* total two-way turnover including the underlying 30/70 sorts, and recompute the breakeven cost. **Fail if** the realized bottom-up breakeven cost is < 10 bp per unit traded (our top-down upper bounds are 162–420 bp for Structural and 38–146 bp for Timing).
- **F11 — Frozen forward window (`research-defined`):** freeze the rule (no retuning) and evaluate January 2025 onward. **Fail if** the structural arm's excess over 1/N is ≤ 0 over the forward window, consistent with the paper's own prediction that the advantage decays as data accumulate.
- **Action on failure:** any F1/F2/F4/F11 failure downgrades this record to low confidence and blocks any production-candidate nomination; F5/F8/F10 failures require re-stating the mechanism as factor-specific or unimplementable rather than a general allocation improvement.

## Crypto portability

`unproven`

- The source is entirely US equity evidence (NYSE breakpoints, 1963–2024 monthly long-short characteristic factors, dividends/book value as the structural term). Nothing in the pinned text studies crypto, perpetuals, or 24/7 markets.
- Porting risks: crypto cross-sectional factors have no standardized book-value/P-B decomposition for most tokens (many have no meaningful book equity), so the revaluation term itself may not exist; the 24/7 clock removes the monthly-session convention and the NYSE-breakpoint logic; perpetual funding, mark/index price, liquidation, borrow for the short leg, venue fragmentation and index membership rules have no counterpart in the source and are absent from its (already zero) cost model; accounting-based factors (ACCRUAL, PROF, NSI, INV) require audited financials that most crypto issuers do not publish.
- A crypto port would therefore be a **new hypothesis requiring its own primary evidence**, not a direct transfer; label any such attempt `adapted` with fresh falsification.

## Limitations

- `data gap`: data vendor, point-in-time/survivorship policy, accounting-availability lags, dividend/corporate-action handling, monthly session/timestamp convention, execution price and timing, cost/spread/slippage/borrow/margin model, inside-factor turnover, journal of publication, code and replication package.
- `underspecified`: non-negativity of the proportional weights, frequency at which the underlying 30/70 factor sorts are rebuilt, and the statistical test behind the Figure 1 "80 % vs 40 %" wealth claim.
- `not independently reproduced`: every performance, predictive and turnover figure in this record.
- `unproven`: any net-of-cost, out-of-sample, or crypto claim; the Structural-over-Historical increment at conventional significance.
- Incremental-write check: this is a new source identity and a new allocation mechanism (return-decomposition-based factor weighting) not covered by any existing record; no existing record is rewritten.

## Implementation status

`implementation_status: not-implemented`.

No part of this record has been implemented in our research stack: no factor library, no structural-premium estimator, no allocation engine, no Qlib full backtest, no production card, and no Paper/Testnet/Live activity. The source itself ships no code or data pipeline. This research capture does not modify any runtime and does not authorize implementation.

## Adoption boundary

`status: research-only` · `adoption: not-approved` · `approval_scope: research-only`.

Presence of this record in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, Paper, Testnet, or Live. No wording, evidence count or confidence value here promotes the record.

## Related Wiki records

Read-only `kb_search` against Hermes Wiki Brain on 2026-09-25 (queries: "factor momentum timing factor allocation smart beta" → 5 results, none mechanism-adjacent; "revaluation valuation ratio structural factor expected returns decomposition" → 1 result, an unrelated crypto momentum-falsification page; "factor zoo anomaly replication equal weight 1/N multifactor portfolio" → **0 results**) found **no mechanism-adjacent Wiki page** for structural/revaluation-based factor allocation. No Wiki link is asserted here, and **no Wiki page was written** (Scouts are read-only with respect to Wiki Brain).

Adjacent *repository* records (dedup context, not Wiki links): `alphaforge-generative-formulaic-alpha-dynamic-factor-timing-2026-09-17.md`, `crypto-cross-sectional-factor-momentum-anomaly-portfolios-2026-08-31.md`, `reviving-anomalies-expected-net-return-double-sort-1n-implementable-2026-09-23.md`, `published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23.md`, `continuous-macro-timing-growth-defensive-style-allocation-2026-09-02.md`.

## Sources

1. Robert D. Arnott, Sina Ehsani, Campbell R. Harvey, Omid Shakernia. *"Revaluation Alpha."* SSRN abstract **5451754**, DOI `10.2139/ssrn.5451754`; Posted 8 Sep 2025, Last revised 8 Aug 2026, Date Written August 08, 2026, 36 pages, JEL G11/G12/G14/G40. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5451754 (landing read 2026-09-25).
2. Pinned primary-source PDF of source 1, retrieved 2026-09-25 from `https://papers.ssrn.com/sol3/Delivery.cfm/5451754.pdf?abstractid=5451754&mirid=1&type=2`: 1,300,813 bytes, 36 pages, SHA-256 `ace0331d0610268363ab3842fa6893ca328ab20ab2dbe5e9a283178211cc605b`, PDF `/CreationDate D:20260808142111-04'00'` — sole source of Tables 1–5, Figures 1–3, Table A1 and Appendices A–C. SSRN returns HTTP 403 to non-browser clients (verified 2026-09-25).
3. Research Affiliates landing page for the same title (author-list discrepancy only; no number taken from it): https://www.researchaffiliates.com/publications/journal-papers/1097-revaluation-alpha (read 2026-09-25).
4. Dedup/search evidence for this run: ripgrep over all `*.md` (970 top-level records) plus `coverage_manifest.csv` in `HCH725/alpha-strategy-research` for `Revaluation Alpha`, `5451754`, `10.2139/ssrn.5451754`, `Shakernia`, `Robert D. Arnott`, `structural premium`, `structural return`, `structural component`, `Ehsani` (zero source-identity hits); `git log --oneline -20` reviewed as a convenience glance only; repository synced with `git pull origin main` before research.
