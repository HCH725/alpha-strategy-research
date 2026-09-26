---
schema: strategy-research-record-v1
title: "Mosaics of Predictability: P-Tree Endogenous Clustering of Latent Return Predictability into Cluster-Specific Ridge Forecasts, Forecast-Implied Long-Short and Predictability-Differential Long-Short Portfolios (NBER WP 35158)"
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - us-equity
  - cross-sectional
  - machine-learning
  - clustering
  - return-predictability
  - regime-dependence
  - long-short
  - negative-evidence
status: research-only
confidence: medium
source_as_of: 2026-04-30
sources:
  - "Lin William Cong, Guanhao Feng, Jingyu He, Yuanzhi Wang, 'Mosaics of Predictability', NBER Working Paper No. 35158, Issue Date April 2026. https://www.nber.org/papers/w35158"
  - "https://doi.org/10.3386/w35158 (NBER DOI; resolves to the working-paper landing)"
  - "https://www.nber.org/system/files/working_papers/w35158/w35158.pdf (pinned primary PDF read end-to-end for this record: 72 pages, 1,321,976 bytes, SHA-256 9e782aafc28421994216fae6a5dc57bbab5d32d4edf604d15cb9ce8033d416ca, retrieved 2026-09-27)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Source-internal: §4.1 (p.18 of the PDF) states the root-node homogeneous R2 of 1.49% is 'obtained by fitting a Ridge model', but Table 4 Panel A and Table A.9 Panel A print the in-sample Global row as OLS 1.49 / Lasso 0.52 / Ridge 0.54 — the 1.49 figure is labelled OLS in both tables. The estimator behind the tree's split objective is therefore ambiguous."
  - "Source-internal metadata: the pinned PDF cover and the landing <time> element both read April 2026 (landing datetime 2026-04-30T12:00:00Z), while the landing citation_publication_date meta tag reads 2026/05/04."
---

# Mosaics of Predictability: P-Tree Endogenous Clustering of Latent Return Predictability into Cluster-Specific Ridge Forecasts, Forecast-Implied Long-Short and Predictability-Differential Long-Short Portfolios (NBER WP 35158)

## Provenance

- **Primary-source author(s), exactly as source:** **Lin William Cong** (Cornell University and NBER, will.cong@cornell.edu), **Guanhao Feng** (City University of Hong Kong, gavin.feng@cityu.edu.hk), **Jingyu He** (City University of Hong Kong, jingyuhe@cityu.edu.hk), **Yuanzhi Wang** (City University of Hong Kong, yuanzwang5-c@my.cityu.edu.hk) — order and affiliations exactly as printed in the PDF cover block (p.1) and the title block with e-mail addresses (p.2). The landing page `citation_author` meta tags list the same four names in a **different (alphabetical) order** (`Guanhao Feng`, `Jingyu He`, `Lin William Cong`, `Yuanzhi Wang`); the copyright line reads "© 2026 by Lin William Cong, Guanhao Feng, Jingyu He, and Yuanzhi Wang". No fifth author, no discussant-as-author, and no "work done during" annotation appear anywhere in the pinned PDF.
- **Paper title:** *Mosaics of Predictability*. JEL No. **C38, C53, C55, G12**.
- **Version / date (primary-source checksum):** NBER **Working Paper 35158**, DOI `10.3386/w35158`. PDF cover reads **"April 2026"**; landing page `Issue Date: April 2026` (`<time datetime="2026-04-30T12:00:00Z">April 2026</time>`), landing `citation_publication_date` **2026/05/04**, landing `citation_doi` `10.3386/w35158`, `citation_title` `Mosaics of Predictability` (all read directly from the landing HTML on 2026-09-27). **No `Revision Date` and no "Other Versions" block exists on this landing page** → this is the first public NBER version. Pinned PDF metadata: `/CreationDate D:20260428024630Z`, `/ModDate D:20260430111624-04'00'`, `/Producer pdfTeX-1.40.23`, empty `/Title` and `/Author` fields. The April-vs-May metadata mismatch is recorded in `contradictions`, not smoothed.
- **Publication status:** **working paper, not peer reviewed.** Verbatim on the PDF cover: "NBER working papers are circulated for discussion and comment purposes. They have not been peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies official NBER publications." The acknowledgements thank discussants and list ~20 conference venues (2026 Shanghai Forum, 2025 SFS Cavalcade Asia-Pacific, 2025 AFA Annual Meeting, 2024 SoFiE, etc.) — conference presentation is not peer review. No journal reference, no "forthcoming", no `journal-ref` field was found on the landing page or in the PDF.
- **Primary-source inspection for this record:** the NBER PDF was downloaded directly (HTTP 200) and its full text extracted with pypdf; **all 72 pages were read end-to-end**: cover, Abstract/title block (p.2), §1 Introduction, §2.1–§2.4 (predictability measurement, cluster Ridge regression, split criterion Eq. 6, stopping rules), §3.1–§3.2 (data, training/evaluation), §4.1–§4.2 (cross-sectional and regime mosaics), §5.1–§5.2 (OOS validation, forecast-implied strategies Eqs. 8–9), §6 Conclusion, References, Appendix **A.1 predictor lists (Tables A.1–A.2)**, A.2–A.3 (figures/algorithm), A.4.1–A.4.7 (Tables A.3–A.8), **A.5 (Table A.9–A.10)**, plus the **Internet Appendix IA.1–IA.2 (Figure IA.1, Tables IA.1–IA.5)**. Every performance figure below carries its Table/Section provenance. The **transaction-cost treatment was checked specifically in §5.2, Appendix A.4.7 and Internet Appendix IA.2** plus a full-text word scan of the pinned PDF (see *Execution assumptions*).
- **Sample / data as-of:** **monthly U.S. equity panel, 1973–2022** (50 years). Train = first 30 years (**1973–2002**), test = most recent 20 years (**2003–2022**); §3.1 footnote 8 explains the 1973 start (CRSP added NASDAQ coverage for data starting 1972-12-14). Average/median stock counts: train **4,840 / 4,772**, test **3,909 / 3,694**. The **entire 50-year sample** is used for the time-series/regime analyses (§3.1).
- **Universe / filters:** stocks listed on **NYSE, AMEX or NASDAQ for over one year**; **CRSP share codes 10 and 11**; exclusion of stocks with **negative book equity or lagged market equity**; unbalanced panels accepted (§3.1).
- **Repository deduplication audit (2026-09-27, deterministic, before writing):** ripgrep across the **entire repository, hidden-inclusive** — **2,574 `*.md` files** (`.mimo-worktrees/`, `.agents/`, `.hermes/` included; 1,008 of them `git`-tracked) plus all `csv`/`json`/`txt`, and **`coverage_manifest.csv` (5,808 lines / 1,088,787 bytes)** — for each of `w35158`, `10.3386/w35158`, `mosaic` (case-insensitive, also covers "Mosaics of Predictability"), `Guanhao`, `Yuanzhi`, `Jingyu`, `Panel Tree`, `P-Tree`, `predictability differential`, `forecast-implied`, `6705515`, `predictability heterogeneity`, `R2_CMG` → **0 files for every pattern** and **0 hits in `coverage_manifest.csv`**. `git log --oneline -20` was inspected separately as a convenience glance only (HEAD `c15d4d5`) and is not treated as dedup evidence.
- **Material-distinctness statement (independent record):** closest existing records differ in **source identity** and in at least one material axis:
  - `published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23.md` — different source (arXiv anomaly-zoo audit) and different mechanism (luck-adjusted decay of *published* anomaly returns) versus an endogenous partition of the panel by *latent forecastability* plus cluster-conditioned models.
  - `directional-anomaly-zoo-net-cost-audit-quality-survivor-2026-09-23.md` — different source and mechanism (net-cost audit of a fixed anomaly list), no clustering, no forecast-implied portfolio.
  - `smart-predict-then-optimize-spo-plus-robust-portfolio-2026-09-05.md` — different source and mechanism (decision-focused SPO/robust portfolio layer on top of a given forecast), whereas here the *forecast itself* is made heterogeneous by clustering.
  - `cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02.md` — different source; regime gating of a residual MoE model, not a supervised split chosen to maximize cross-cluster R² dispersion.
  - `conditioning-sign-on-magnitude-return-decomposition-csm-2026-09-04.md` and `equity-cross-sectional-homological-neural-network-mfcf-ranking-2026-09-02.md` — hit the same broad literature words (`Gu, Kelly, and Xiu` / cross-sectional return prediction) but are different sources with different mechanisms (sign/magnitude decomposition; topological/MFCF ranking).
  Axes on which this record is materially distinct: **mechanism** (predictability treated as a latent asset-specific/state-specific characteristic partitioned endogenously, plus a *model-misspecification* differential R²_C − R²_G), **signal construction** (greedy P-Tree maximizing |R²_left − R²_right| over 51 characteristics × cut points 0.3/0.7 and 8 smoothed market predictors, then per-leaf inverse-variance-weighted Ridge), **universe/market type** (U.S. listed common stocks, monthly, full cross-section), **horizon/regime** (monthly long-short with an explicit three-regime dividend-yield × liquidity layer), **material data dependency** (51 accounting/price characteristics + Welch–Goyal-style aggregate predictors).
- **Mirror landscape (identification only):** search metadata visible on 2026-09-27 shows an SSRN NBER mirror at `abstract_id=6705515` (72 pages, "Posted: 5 May 2026, Last revised: 18 May 2026") and an earlier author-posted SSRN entry ("Posted 06 Jun 2024, Last Revised 27 Apr 2026"). **Neither SSRN page was opened in this run** (SSRN is Cloudflare-protected for non-browser clients), so **every number in this record is taken solely from the pinned NBER PDF (April 2026)**; cross-mirror numeric equivalence is a `data gap`.

## Economic mechanism

### Source-reported

The authors' chain: return predictability is a **latent, asset-specific, state-dependent characteristic "analogous to beta or volatility"** (§1, §2.1) that governs the signal-to-noise ratio of conditional expected returns. Most designs impose homogeneity (pooled regressions, representative portfolios), which **misspecifies** the forecasting relation when predictability differs across assets and states. Information frictions and limits to arbitrage concentrate predictability where information is costly and trading is thin: the cross-section shows **largest in-sample R² (>10%) for stocks with large earnings surprises (SUE), high earnings–price ratios, high sales-to-price ratios and low trading volume** — the long legs of PEAD (Bernard & Thomas 1989) and earnings-yield effects (Reinganum 1981) — while **low earnings surprises, high bid-ask spreads and strong momentum** predict *nothing or worse-than-zero* R² (§1, §4.1). In the time series, predictability is **countercyclical**, peaking when the market **dividend yield is high and aggregate liquidity is low** (Pastor–Stambaugh liquidity), consistent with Campbell–Shiller present-value mechanics (§4.2, Appendix A.4.4). Translation into money: cluster-specific forecasts beat a single global model, and — in Appendix A.4.6 — the **gap between local and global model fit (R²_C − R²_G) is itself priced**, which the paper interprets as **model-misspecification risk**: investors who trade only on homogeneous benchmarks miss locally relevant signals, so those stocks carry higher expected returns.

### Research interpretation

Falsifiable mechanism: **heterogeneous information-diffusion speed × limits-to-arbitrage** produce a cross-section of conditional-mean signal-to-noise ratios that a single pooled model averages away; if true, (i) a supervised partition chosen for *forecastability* should separate future-return forecastability out of sample, (ii) forecasts built *within* easy-to-predict cells should beat a pooled forecast on the same predictors, (iii) the effect should be strongest in high-dividend-yield / low-liquidity states, and (iv) a spread sorted on *local-vs-global fit* should survive factor spanning. The second, distinct claim is a **mispricing/misspecification channel**, not a risk-premium identification — the paper offers no sharp identification between behavioral and rational channels (§4.2 states this explicitly).

Component roles (as in the source):

```text
Regime layer (optional, "TS+CS" variant): first two splits forced onto market predictors
                            -> 3 regimes: X DY<=0 (377 mo); X DY>0 & X LIQ<=0 (57 mo);
                               X DY>0 & X LIQ>0 (166 mo); 45 terminal clusters
Primary signal:             P-Tree greedy partition maximizing |R2_leaf_left - R2_leaf_right|
                            over 51 firm characteristics (monthly cross-sectional ranks in [0,1],
                            candidate cut points 0.3 / 0.7) and 8 aggregate predictors
                            (cut at 0 after 10-year rolling demeaning + 12-month WMA)
Forecast:                   per-leaf Ridge regression, inverse-variance (1/sigma^2_{i,t-1}) weights,
                            lambda selected by cross-validation within the leaf,
                            predictors z_{i,t-1} and x_{t-1} (one period lagged)
Portfolio A (§5.2):         forecast-implied long-short, three weightings:
                            sign-adjusted equal-weight, sign-adjusted value-weight,
                            forecast-weighted w = r_hat / sum|r_hat| (gross exposure normalised to 1)
Portfolio B (A.4.6):        long-short on the predictability differential R2_CMG = R2_C - R2_G,
                            top-k vs bottom-k clusters (k = 1, 3, 5, 7)
Risk / exit:                none specified by the source — no stop, no vol target, no position
                            limit, no drawdown control, no explicit exit (explicit gap)
```

The paper does not claim every component contributes equally: it reports that the *aggregate* cluster model only beats the global model decisively in the **forecast-weighted** (magnitude) scheme (Table 6 Panel C), while Panels A/B are close, and that the long-short spread is **long-leg driven** (Table A.6) — so an ablation of weighting scheme and of legs is required before attributing alpha to the framework as a whole.

## Signal

All of the following is `source-reported` unless marked.

- **Formation timestamp / tradability:** the panel is **monthly**; the forecast at *t* uses `z_{i,t−1}` (characteristics) and `x_{t−1}` (market predictors), and the cluster assignment, Ridge fit and portfolio weight are functions of information available at **t−1**, earning the return at *t* (Eqs. 2–5, 8–9; Eq. 7 uses `r_{i,t+1}` vs `r̂_{i,t+1}` for OOS scoring). **The exact order time and execution price (month-t close, next month open, or VWAP) are never stated** → `data gap`; any concrete execution convention is `research-proposed`.
- **Rebalancing cadence:** "At each rebalancing date, stock weights are determined in three ways" (§5.2) — **the cadence itself is never printed**. The panel, the trees and the reported Avg/Std are all monthly, so a **monthly** rebalance is the only consistent reading, but that reading is *inferred* → `underspecified`; a replication that pins monthly rebalancing is `research-proposed`.
- **Tree construction (§2.3–§2.4, §3.1):** characteristics are **cross-sectionally standardized to [0,1] each month** with candidate split points **0.3 and 0.7** (mimicking top/middle/bottom sorts); the eight market predictors are **demeaned on a 10-year rolling average and smoothed with a 12-month weighted moving average**, split at 0. Split score `S = |R²_leaf_l − R²_leaf_r|` (Eq. 6) searched over all leaves × all variables × all cut points (P×K per leaf), greedy/global-best, "local-global" principle. Stopping: **minimum leaf size = 30 monthly average stock-return observations**, **maximum depth 6 (≤32 leaves)** for the cross-sectional tree, and no split unless at least one child's R² exceeds its parent's. Result: **23 splits → 24 terminal leaves** (footnote 9, Figure 2).
- **Tree variants:** (a) **CS tree** on 1973–2002 (Figure 2); (b) **TS+CS tree** on 1973–2022 with the **first two splits restricted to market predictors**, depth ≤5 per regime (≤48 leaves), **45 terminal clusters in 3 regimes** (Figure 5, Figure A.3, footnotes 11–12); (c) **structural-break tree** splitting on **calendar month** instead of market predictors (Appendix A.4.5, Figure A.5); (d) **Sharpe-ratio-split tree** replacing R² in Eq. 6 with portfolio Sharpe (Appendix A.5).
- **Cluster-wise forecast model (§2.2):** Ridge regression per leaf, objective Eq. (4), weighted by **inverse of a rolling-window estimate of stock i's conditional return variance** `w_{i,t−1} = 1/σ²_{i,t−1}` (window length not printed → `data gap`); **λ chosen by cross-validation within each cluster** (grid not printed → `data gap`). Cluster predictability score = in-sample R² vs a **zero-return** benchmark (Eq. 5).
- **Estimation/evaluation protocol (§3.2, §5.1):** the P-Tree **and** the leaf models are re-estimated on a **30-year rolling window updated every five years**, repeated **four times** over the 20-year OOS period; hyperparameters are tuned by cross-validation. OOS evaluation additionally uses **five-year rolling clustering with two-fold cross-validation** (footnote 15: train on one contiguous half, validate on the other, retrain on the full in-sample window, then forecast the next 5 years). The source is explicit that **OOS R² is never used to guide splitting** (§2.1) — clustering and leaf estimation are a deliberate in-sample exercise, evaluated afterwards OOS.
- **Predictability groups (§5.1):** leaves are ranked by in-sample R²; **top six clusters = "high"**, **bottom five = "low"**, remainder = "medium"; footnote 16 additionally describes a **cumulative 10%-of-sample-share** rule for grouping clusters. The group labels used in Tables 4–6 are therefore **in-sample-selected**.
- **Portfolio rules (Eq. 8–9):** sign-adjusted `ŵ = +w if r̂ ≥ 0, −w if r̂ < 0` with `w` equal-weighted or value-weighted (market cap); forecast-weighted `ŵ = r̂ / Σᵢ|r̂|` — the source notes (footnote 18, citing Guijarro-Ordonez, Pelger & Zanotti 2025) that normalising absolute weights to sum to one **implicitly imposes a leverage constraint**. Portfolio return `R_{j,t} = Σ_{i∈leaf j} ŵ_{i,t−1} · r_{i,t}` per leaf/group. The books are **explicitly active long–short** (§5.2).
- **Predictability-differential strategy (Appendix A.4.6):** `R²_CMG,j = R²_C,j − R²_G,j` (Eq. 10), clusters ranked by R²_CMG, **long top-k / short bottom-k** clusters, k ∈ {1,3,5,7}, value- and equal-weighted inside clusters; factor-spanning alphas against CAPM, FF3, FF5, FF5+MOM+IVOL, Q5, BS6, DHS3, SY4 (Table A.5).
- **Exit / holding period:** **no exit rule, no maximum holding period, no stop, no deadband** is specified anywhere → `underspecified` (any stop, vol target or drawdown brake in our own tests is `research-proposed`).
- **Ties / simultaneous signals:** not addressed → `underspecified`.
- **Parameters and their source:** cut points 0.3/0.7, min leaf 30, depth 6 (CS) and 5 (regime), 23-split stopping, six/five-cluster high/low grouping, 10% cumulative-share rule, 30-year/5-year re-estimation window, 10 bp cost — **all source-specified**, and **all chosen with the full 1973–2022 panel available**; the paper's only stated protection is the rolling re-estimation plus the Internet Appendix window variations (1978–2007, 1983–2012, 1988–2017). Any re-tuning on this sample is in-sample unless re-derived point-in-time.
- **Position sizing / risk overlay:** **none in the source** beyond the gross-exposure normalisation above.

## Required data

- **Instrument / universe:** U.S. common stocks on NYSE/AMEX/NASDAQ, CRSP share codes 10 and 11, listed >1 year, positive book equity and lagged market equity; monthly, 1973–2022, unbalanced panel; **market type: cash equities, long-short (borrowable) — no futures, no options, no crypto.**
- **Venue / data vendor:** only **CRSP** is named (share codes; NASDAQ coverage footnote 8). The **vendors/sources for the 51 characteristics and the 8 aggregate predictors are not stated in the pinned text** → `data gap` (the predictor list follows Welch & Goyal 2008 and resembles the standard CRSP/Compustat/IBES anomaly library, but no vendor, no database release and no extraction script is printed).
- **Fields:** monthly returns (the model target is described as **"excess return of stock i"** in §2.2 — **the excess-over-benchmark is never defined**, `data gap`); market equity, book equity; the **51 characteristics of Table A.2** in eight categories (size, value, investment, momentum, profitability, liquidity, volatility, intangibles) including `sue`, `ep`, `sp`, `cfp`, `dolvol`, `turn`, `baspread`, `ill`, `zerotrade`, `maxret`, `mom1m…mom60m`, `acc`, `pctacc`, `noa`, `cinvest`, `rna`, `gma`, `bet`, `rvar_capm`, `svar`, `std_dolvol`, `zerotrade`, etc.; the **8 market predictors of Table A.1** (`X_TBL`, `X_INFL`, `X_TMS`, `X_DFY`, `X_DY`, `X_SVAR`, `X_NI`, `X_LIQ` — Pastor–Stambaugh rolling 12-month liquidity).
- **Timeframe / timestamps:** monthly bars; **timezone, clock source and timestamp precision are never stated** → `data gap`; month-boundary convention for characteristic standardization is implied ("for each month") but not specified further.
- **Point-in-time / availability:** all predictors enter **one period lagged** (§2.2); market predictors are additionally smoothed over 12 months and demeaned on a 10-year rolling window (so the first usable months have a warm-up). **No statement anywhere addresses accounting-publication lag** (when SUE, EP, accruals, book equity actually become observable) → `data gap` and the central look-ahead risk, because **SUE and EP are the first two splits of the headline tree**. The source explicitly avoids OOS information in model selection (§2.1) and uses a 1973–2002 / 2003–2022 split with five-year re-estimation, but no purging/embargoing is described.
- **Missing data:** unbalanced panels accepted (§3.1); **no imputation rule is printed** → `underspecified`; the Internet Appendix lists "return winsorization thresholds" as a tunable parameter but **never prints the baseline winsorization level** → `data gap`.
- **Funding / fee / spread needs:** none are consumed by the signal itself (the source models no cost field other than the flat 10 bp charge). A tradable replication still needs, per name and per rebalance: commission/fees, bid-ask spread, **stock-loan/borrow fee for the short leg**, market impact and participation/ADV, financing on margin, dividends/corporate-action treatment, and realised turnover — **all absent from the source → `data gap`, never defaulted to zero** (see *Execution assumptions*).
- **Validation-only inputs (not needed to trade):** NBER recession shading (Figure 6), eight factor models for spanning (Tables A.5–A.7), large-cap subsample (top 30% by market equity).

## Execution assumptions

**Source-reported:**

- Instrument/venue: **cash equities**, full cross-section, **active long–short** portfolios (§5.2), weights refreshed "at each rebalancing date" (cadence not printed).
- **Transaction costs — the complete cost model:** Appendix **A.4.7** states: "While these costs are empirically unobservable and inherently difficult to forecast, we adopt a conservative approach by **imposing a fixed cost of 10 basis points per trade, applied uniformly across all rebalancing periods**." That single parameter produces Tables **A.7** (differential strategy), **A.8** (forecast-implied, CS clusters) and **IA.5** (forecast-implied, TS+CS clusters). §5.2 reports the resulting drift: high-predictability OOS Sharpe moves from 1.66 → 1.59 (Panel B) and 1.86 → 1.80 (Panel C).
- **Word scan of the pinned 72-page PDF (Methods-level, whole document):** `commission` **0**, `fees`/`fee` **0**, `slippage` **0**, `borrow` **0**, `shorting` **0**, `short sale` **0**, `latency` **0**, `fill` **0**, `market impact` **0**, `capacity` **0**, `bid-ask` **3** — and all three `bid-ask` hits are either the `baspread` characteristic (Table A.2) or prose about *which stocks are unpredictable* ("stocks with … high bid-ask spreads … exhibit little or no predictability", §1), **never a cost**. `leverage` **3** hits, all about the weight normalisation (§5.2, footnote 18). `margin` hits are all "marginal" / "profit margin" / prose. `turnover` hits are **only the characteristics** `ato`, `std turn`, `turn` — **portfolio turnover is never reported**. **No order type, fill model, latency, participation cap, position limit, borrow availability, margin rule, financing rate, dividend treatment or failure handling appears anywhere** → every one is a `data gap`, never zero.
- **Gross vs net:** Tables 6, A.5, A.6, IA.4 are **gross**; Tables A.7, A.8, IA.5 are **net of the flat 10 bp/trade assumption only**. No other net-of-cost series exists.
- **Leverage:** forecast-weighted weights are normalised so `Σ|ŵ| = 1` (gross exposure ≈ 1, implicit leverage constraint, footnote 18); sign-adjusted EW/VW books sum `|ŵ| = 1` as well. **No leverage limit, margin requirement or financing cost is discussed** → `data gap`.
- **Short side:** the short legs hold the least predictable clusters, which the source itself characterises as high-bid-ask-spread / low-liquidity names — **no borrow cost, no recall risk, no short-availability screen** → `data gap`.
- Inference: Tables A.5–A.7 print **t-statistics in parentheses** but the paper never states the standard-error convention (no Newey–West, no HAC, no block bootstrap anywhere in the pinned text); Tables 6/A.8 print only star levels → `data gap` on the inference method. SY4 alphas are **2003–2016 only** (footnote 23).

**Research-proposed (our replication choices, not the source's):**

- Signal computed after the month-t close from point-in-time characteristic vintages; order sent at the **next session open**, market orders, full fill at the trade price; explicit 1-month holding.
- Cost ladder of **0 / 10 / 25 / 50 / 100 bp per side** plus an explicit commission schedule, and a **stock-loan fee ladder of 0 / 50 / 100 / 300 bp p.a.** on short notional.
- Participation cap of **10% of 20-day dollar volume** per name and a gross-exposure cap of 1.0 for the capacity test; turnover reported as annual one-way.
- Any stop, volatility target or drawdown brake (`research-proposed`; the source has none).

## Evidence

### Source-reported

All figures below are third-party claims from the pinned NBER WP 35158 PDF (April 2026) and are **not independently reproduced**. In-sample = **1973–2002**, OOS = **2003–2022** unless stated otherwise; returns are monthly averages in %, SR = annualised Sharpe, alpha = Jensen's alpha in % per month against the stated factor model.

**Cross-sectional tree, cluster summary — Table 1 (in-sample, 24 leaves, Figure 2):**

| Leaf | # obs | R²_C | R²_G | R²_C−R²_G | AvgEW | SREW | AvgVW | SRVW |
|---|---|---|---|---|---|---|---|---|
| **N29 (top)** | 10,805 | **10.73** | 6.89 | 3.84 | 4.30 | 2.10 | **3.41** | **1.88** |
| N28 | 11,917 | 8.43 | 6.38 | 2.05 | 3.04 | 1.79 | 2.45 | 1.54 |
| N30 | 17,999 | 7.08 | 6.11 | 0.97 | 2.33 | 1.69 | 1.84 | 1.34 |
| **N23 (bottom)** | 11,089 | **−25.58** | 1.92 | −27.51 | 0.31 | 0.16 | **−0.06** | **−0.02** |

- R²_C spans **10.73% → −25.58%** (a >35 pp spread) and R²_G spans 0.40% → 6.89% (§4.1, Table 1 Panel A). Root/homogeneous R² = **1.49%** (Figure 2 node N1); the pooled model therefore "masks" a 10.73% cell.
- Breadth: the **bottom eight** leaves (R²_C below the 1.49% root) hold **~35%** of observations; the **top three** (R²_C > 5%) hold **~2.3%** (§4.1).
- Tree path to the top cell (Figure 2): first split `SUE ≤ 0.7` (N3 = 2.73 vs N2 = 1.34), second split `EP ≤ 0.7` (N7 = 5.40 vs N6 = 2.14), then `DOLVOL`, `SP` and `TURN` splits; §4.1 states N29 is "high SUE combines with high earnings-to-price (EP > 0.7) and low trading volume". Figure 3 heat maps show the same SUE × EP gradient by year across 1973–2002.

**Out-of-sample predictability — Table 4 (2003–2022, R² in %):**

| Sample | IS OLS / Lasso / Ridge | OOS OLS / Lasso / Ridge |
|---|---|---|
| Panel A Global (no clustering) | 1.49 / 0.52 / 0.54 | 0.27 / 0.40 / 0.35 |
| Panel A Global-High | 4.12 / 2.45 / 2.28 | 3.16 / 2.14 / 2.06 |
| Panel A Global-Low | 0.89 / 0.30 / 0.31 | 0.09 / 0.24 / 0.17 |
| Panel B Aggregate (cluster-wise) | 1.75 / 0.83 / 0.74 | **−0.28** / 0.42 / 0.53 |
| Panel B Cluster-High | 6.03 / 5.07 / 4.69 | 2.97 / 3.79 / **3.84** |
| Panel B Cluster-Low | −2.57 / −1.78 / 0.06 | −1.75 / −0.74 / 0.11 |

- Table 5 (re-fitting homogeneous models on subgroups): removing the top-10% predictability clusters cuts OOS Ridge R² from **0.35 → 0.23**, and the top-20%/top-40% removals give **0.17 / 0.16** — i.e. "a small subset of highly predictable stocks mechanically inflates the apparent predictability of the full sample" (§5.1).
- Table 3 (regimes, Ridge): Regime II global **8.68** (all stocks) vs cluster-wise aggregate **9.28** vs high group **17.35**; large-cap global **12.66** vs high **20.44**. Regime I global Ridge **0.84** and Regime III **2.39** — i.e. most of the action is the 57-month high-DY/low-liquidity state.
- Regime definition (Figure 5): **Regime I 377 months (X DY ≤ 0), Regime II 57 months (X DY > 0 & X LIQ ≤ 0), Regime III 166 months (X DY > 0 & X LIQ > 0)**; **45 terminal clusters**; in-sample global R² 1.44%. Regime dispersion (Table 2): top leaf R² **35.51% (Regime II, N16, #obs 1,946)** vs bottom **−3.97%**; Regime I 11.00% vs −12.79%; Regime III 12.39% vs −0.49%.
- Table A.3/A.4 (calendar-month structural breaks): top-leaf in-sample R² reaches **41.22%** in 1973-01→1978-10; every period's high group exceeds its low group (Table A.4), including in the large-cap subsample.
- Appendix A.5 / Table A.9 (**Sharpe-ratio split** instead of R²): same qualitative ranking, but the OOS cluster-wise high group falls to **0.69 / 0.98 / 1.04** (OLS/Lasso/Ridge) versus **2.97 / 3.79 / 3.84** under the R² split — the OOS forecastability of the "high" group is strongly specification-dependent.
- Internet Appendix robustness (Figure IA.1, Tables IA.1–IA.3, windows **1978–2007, 1983–2012, 1988–2017**): the first two splits remain **SUE plus value (EP / CFP / BM)** in all three; top-leaf in-sample R² **11.11 / 9.68 / 10.40**; bottom leaf **−27.11 / −15.18 / +0.33** (the 1988–2017 variant has **no negative-R² leaf**).

**Forecast-implied portfolios — Table 6 (gross) vs Table A.8 (net of 10 bp/trade), OOS 2003–2022:**

| Panel / group | Gross Avg | Gross SR | Gross α | Net (A.8) Avg | Net SR | Net α |
|---|---|---|---|---|---|---|
| A sign-adjusted VW — Global | 0.72 | 0.60 | −0.03 | 0.62 | 0.52 | **−0.13\*\*\*** |
| A sign-adjusted VW — Aggregate | 0.79 | 0.67 | 0.05\*\* | 0.69 | 0.59 | −0.05\*\* |
| A sign-adjusted VW — High | 1.21 | 0.84 | 0.46\*\* | 1.11 | 0.77 | 0.36\* |
| A sign-adjusted VW — Low | 0.61 | 0.51 | −0.09 | 0.51 | 0.43 | −0.19\* |
| B sign-adjusted EW — High | 2.70 | **1.66** | **1.84\*\*\*** | 2.60 | **1.59** | **1.74\*\*\*** |
| B sign-adjusted EW — Low | 0.67 | 0.46 | −0.15 | 0.57 | 0.39 | −0.25 |
| C forecast-weighted — Global | 1.12 | 0.73 | 0.25\* | 1.02 | 0.67 | 0.15 (n.s.) |
| C forecast-weighted — Aggregate | 1.56 | 1.13 | 0.79\*\*\* | 1.46 | 1.06 | 0.69\*\*\* |
| C forecast-weighted — High | 3.22 | **1.86** | **2.31\*\*\*** | 3.12 | **1.80** | **2.20\*\*\*** |
| C forecast-weighted — Low | 0.88 | 0.54 | −0.03 | 0.78 | 0.48 | −0.13 |

- The abstract's "out-of-sample Sharpe ratios around 2" maps to **1.86** (Table 6 Panel C, High, gross) and **1.89** (Table A.10 Panel C, High, gross, Sharpe-split tree); the larger IA.4 numbers (High SR **2.72**, EW **2.48**) are **full-sample**, not OOS, per the IA.4 caption.
- Large-cap subsample (Table A.8): Aggregate-Large OOS SR **0.58–0.65**, alpha **−0.05\*\* to 0.06\*** — the clustering gain shrinks markedly once small caps are excluded (the source attributes this to lower large-cap predictability).

**Predictability-differential long-short — Table A.5 (gross) vs Table A.7 (net of 10 bp/trade), OOS 2003–2022:**

| Spread | Gross Avg | Gross SR | Gross FF5 α (t) | Net Avg | Net SR | Net FF5 α (t) |
|---|---|---|---|---|---|---|
| T1 − B1 | 2.79 | 1.51 | 3.03\*\*\* (7.17) | 2.59 | 1.40 | 2.83\*\*\* (6.70) |
| T3 − B3 | 1.74 | 1.48 | 2.00\*\*\* (7.52) | 1.54 | 1.31 | 1.80\*\*\* (6.77) |
| T5 − B5 | 1.32 | 1.25 | 1.39\*\*\* (6.05) | 1.12 | 1.06 | 1.19\*\*\* (5.17) |
| T7 − B7 | 1.10 | 1.44 | 1.17\*\*\* (6.89) | 0.90 | 1.18 | 0.97\*\*\* (5.71) |

- All eight factor models (CAPM, FF3, FF5, FF5+MOM+IVOL, Q5, BS6, DHS3, SY4) report significant OOS alphas for every spread, gross and net (Table A.5/A.7 Panel B); SY4 is 2003–2016 only (footnote 23). The source concludes the premium "is not a data-mined result" (§A.4.6) — a claim, not a verification.
- **Leg decomposition (Table A.6), OOS:** long legs T1/T3/T5 average **3.25 / 2.26 / 2.01 %/mo** with SR **1.60 / 1.35 / 1.10** and FF5 alpha **2.51\*\*\* / 1.62\*\*\* / 1.21\*\*\***; short legs B1/B3/B5 average **+0.46 / +0.52 / +0.69 %/mo** with SR **0.22 / 0.32 / 0.46** and CAPM alpha **−0.60\*\* / −0.39\*\* / −0.20\***. The source's own reading: long legs "consistently generate most of the abnormal returns, whereas short-leg portfolios typically exhibit weak or insignificant OOS alphas."

### Independently reproduced

`not independently reproduced`. This run performed only: (a) direct download and full 72-page read of the pinned NBER PDF, (b) landing-page metadata verification (DOI, issue date, `citation_*` meta tags), (c) table/section provenance for every number above, (d) a Methods-level word scan of the cost vocabulary, and (e) repository-wide source-identity dedup. **No regression, tree, portfolio, R², Sharpe or alpha was recomputed; no CRSP/Compustat data was obtained; the strategy was not backtested.**

### Negative evidence

1. **The entire cost model is one flat number.** 10 bp per trade, uniform across rebalancing periods (Appendix A.4.7), with `commission`, `fee/fees`, `slippage`, `borrow`, `latency`, `fill`, `market impact`, `capacity` at **zero occurrences** in the pinned PDF. Every net figure in Tables A.7/A.8/IA.5 inherits an unmeasured-turnover assumption.
2. **Turnover is never reported.** `turnover` appears only as three *characteristics*. A monthly sign-flipping book over the whole cross-section will generate non-trivial two-way turnover by construction (inference, not a source claim), so the 10 bp charge cannot be checked against realised trading.
3. **The short leg is structurally the expensive side.** §1 states the *un*predictable stocks are those with "high bid-ask spreads" and weak liquidity — yet both long-short books short exactly those names, with **no borrow cost, no availability screen, no recall model** (all `data gap`).
4. **The short leg is also a return drag.** Table A.6: OOS short legs return **+0.46 / +0.52 / +0.69 % per month** with near-zero Sharpe — the source's own decomposition attributes the spread to the long leg, so half of the "long-short" story is a documented non-result.
5. **Baseline global predictability is tiny and can be negative.** Table 4: global OOS R² **0.27–0.40%**; the cluster-wise *aggregate* OOS R² under OLS is **−0.28%** (worse than the zero-return benchmark); Table A.9 gives global OOS Ridge 0.35%.
6. **Model selection is in-sample by design.** §2.1: clustering is "a unified in-sample exercise" chosen to maximize R² dispersion; §5.1 then picks the "high" group as the **top six clusters by in-sample R²**. The OOS high-group R² collapses from 6.03 (IS) to 2.97 (OLS OOS), and under the alternative Sharpe-based split to **0.69–1.04** (Table A.9) — i.e. the headline OOS gap is sensitive to a criterion chosen after seeing in-sample fit.
7. **Highest statistical predictability does not deliver returns where it peaks.** §4.2: in **Regime II** (57 months, top leaf R² **35.51%**) the paper reports "a near-zero correlation between R² and average returns" — the state with the most forecastable returns is the state where forecastability does not sort returns. Regime II is also only 57 of 600 months.
8. **No multiple-testing control anywhere.** Three weighting schemes × seven sample groups × three estimators (OLS/Lasso/Ridge) × four tree variants (CS, TS+CS, structural break, Sharpe-split) × nine factor models × two cost states are all starred; no family-wise or FDR statement appears, and the **standard-error convention is never stated** (no Newey–West/HAC/block bootstrap in the pinned text).
9. **Concentration.** The top three clusters hold **~2.3%** of stock-month observations (§4.1) and the headline N29 cell 10,805 obs; capacity, ADV participation and position limits are all `data gap`, so it is unknown whether the cell can absorb capital.
10. **Large-cap-only results are much weaker.** Table A.8: Aggregate-Large OOS SR 0.58–0.65 with alphas of −0.05 to 0.06, versus 0.59–1.06 for the full sample; §5.2 concedes large-cap predictability is lower. The result leans on small/illiquid names — precisely where costs are highest.
11. **The pooled benchmark is weak after costs.** Table A.8 Panel A: the global model's OOS alpha net of 10 bp is **−0.13\*\*\***, i.e. the homogeneous benchmark loses money under the paper's own cost assumption, which mechanically flatters any comparison against it.
12. **Point-in-time fundamentals are unaddressed.** Predictors are only described as "lagged"; there is no accounting-publication-lag treatment, while `sue` and `ep` are the first two splits of the headline tree — the exact setting where look-ahead is most damaging (PEAD requires announcement timing). `data gap`.
13. **Return basis ambiguous.** §2.2 models **excess returns** (benchmark never defined) while Tables 1/6/A.5 report "monthly average return" with no gross/excess/dividend adjustment statement → the 3.41%/mo top-leaf figure cannot be classified as market-adjusted (`underspecified`).
14. **Source-internal estimator contradiction:** §4.1 attributes the root R² 1.49% to a **Ridge** fit, while Table 4 Panel A and Table A.9 Panel A label **1.49 as OLS** and Ridge as 0.54 for the same in-sample global model (recorded in `contradictions`).
15. **Landing metadata mismatch:** `citation_publication_date 2026/05/04` vs Issue Date / PDF cover **April 2026** (recorded in `contradictions`).
16. **The time-series dimension has no OOS protocol.** Footnote 14: "all time-series results are based on the full-sample analysis, the OOS evaluation in this section primarily emphasizes the cross-sectional dimension" — the regime layer that generates the 35.51% cells is therefore in-sample-only.
17. **Sample ends in 2022.** Nothing covers 2023–2026 (a distinct rate/liquidity regime), and there is no walk-forward beyond the 4×5-year re-estimation inside 2003–2022.
18. **Reproducibility is blocked:** **no code, no data-availability statement, no replication package** (`github` 0 hits, `available upon` 0, `replication package` 0 in the pinned text), and the inputs are proprietary CRSP/Compustat-grade data; the paper is a **non-peer-reviewed NBER working paper**.
19. **Cross-record contrary/contextual evidence (different source identities already in this repository):** `published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23.md` (post-2005 investable large-cap anomalies shrink to ~7 bp median under a luck-adjusted null), `directional-anomaly-zoo-net-cost-audit-quality-survivor-2026-09-23.md` (net-cost audit of published anomalies), `llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04.md` (deflated evaluation of searched strategies), `pca-factor-model-error-decomposition-out-of-subspace-arxiv-2609.20550-2026-09-20.md` (factor-model misspecification as a measurable object) — all consistent with "published equity predictability shrinks under honest cost, leakage and multiplicity treatment".
20. **Literature-level fragility acknowledged by the source itself:** IA.1 is written as a response to Cakici et al. (2025) showing that "pockets of predictability" results are sensitive to methodological choices; the paper's answer is more robustness tables, not a pre-registered holdout.
21. **None of the above has been peer reviewed**, and no independent replication is cited by the source.

## Falsification plan

Every threshold below is a `research-defined falsification threshold`; every operational choice not printed in the source is `research-proposed`.

- **F1 — Point-in-time tree replication.** Rebuild the CS tree on 1973–2002 with the source's rules (cut points 0.3/0.7, min leaf 30, depth 6, 23-split stopping, inverse-variance Ridge, within-leaf CV) using characteristic **publication-vintage** data. *Fail if* the top-leaf in-sample R² < 5% or the first two splits are not SUE/value-family (source: 10.73%, SUE then EP).
- **F2 — Frozen forward window.** Hold out **2023-01 → 2026-06**, never used by any tree or grouping in the paper. *Fail if* the OOS high-minus-low forecastability gap is ≤ 0, or the high-group OOS R² ≤ the global model's (source OOS: 3.84 vs 0.35, Ridge, Table 4).
- **F3 — Cost ladder.** Re-run Tables 6/A.5 at 0 / 10 / 25 / 50 / 100 bp per side plus an explicit commission schedule. *Fail if* the high-group OOS alpha (EW, 1.74%) erodes by more than 50% at 25 bp, or if the T−B spread flips sign at 25 bp (source: still positive at 10 bp).
- **F4 — Borrow-cost audit.** Apply 0 / 50 / 100 / 300 bp p.a. stock-loan fees to the short leg and screen for hard-to-borrow names. *Fail if* the T−B OOS Sharpe drops below 0.50 at 100 bp p.a. — the source models **no** borrow cost at all.
- **F5 — Turnover and capacity audit.** Report annual one-way turnover of both books and execute at 10% / 20% of 20-day dollar volume with a square-root impact model. *Fail if* turnover > 300%/yr **and** break-even one-way cost < 10 bp (i.e. the result sits on an unmeasured cost assumption), or if net-of-impact Sharpe falls by more than 0.50.
- **F6 — Sham-clustering placebo (decisive mechanism test).** Grow 1,000 trees using **random split variables** with matched leaf sizes and the same stopping rules; compare the real tree's in-sample and OOS R² dispersion. *Fail if* the real tree's OOS high-minus-low R² dispersion is not above the 95th percentile of the placebo distribution → the mosaic is an artefact of exhaustive search.
- **F7 — Simple-sort horse race (decisive mechanism test).** Compare the tree's high group against a plain **3-characteristic sort (top-SUE × top-EP × bottom-DOLVOL)** and against a standard PEAD portfolio, matched on breadth. *Fail if* the tree's OOS high-minus-low spread ≤ the simple sort's spread (source claim: endogenous clustering adds value beyond fixed sorts, §4.1).
- **F8 — Point-in-time fundamentals / leakage audit.** Rebuild SUE/EP/accrual-based characteristics with 1-month and 2-month publication lags, plus a purged/embargoed walk-forward. *Fail if* the top-leaf R² or the high-group OOS R² drops below the low-group's → the headline split is look-ahead.
- **F9 — Leg ablation.** Long-only version of the high group vs short-only of the low group. *Fail the "long-short" framing* if the short leg's net contribution is ≤ 0 (source Table A.6 already shows OOS short-leg returns +0.46 to +0.69%/mo and weak alphas).
- **F10 — Inference re-run.** Recompute all headline alphas/Newey–West t at lags 6 and 12 and a stationary block bootstrap; apply Benjamini–Hochberg at q < 0.10 across the 3 weightings × 7 groups × 3 estimators × 4 tree variants grid. *Fail if* q ≥ 0.10 for the aggregate and high-group headline cells (source: stars only, s.e. convention unstated).
- **F11 — Subperiod stability.** Split OOS into four 5-year blocks (2003–2007, 2008–2012, 2013–2017, 2018–2022) plus the F2 forward window. *Fail if* ≥ 2 of the 4 blocks show a non-positive high-minus-low alpha or the forward window is negative.
- **F12 — Regime-layer test.** Re-estimate the TS+CS tree with alternative DY/LIQ cut-offs and with the calendar-month variant, strictly out of sample (the source's time-series results are full-sample, footnote 14). *Fail if* Regime-II-only results disappear, or if the regime label (57 months) is not reproducible point-in-time from published DY/LIQ vintages.
- **F13 — Reproducibility gate.** Re-implement from the paper alone (no author code exists). *Fail if* the reconstructed top-leaf R² differs from 10.73% by more than ±2 pp or the 24-leaf structure cannot be recovered → classify as non-reproducible.

**Action on failure:** F1/F2/F3 failing ⇒ keep research-only, do not promote; F6/F7/F8 failing ⇒ treat the mosaic as search artefact or leakage; F4/F5 failing ⇒ non-implementable regardless of statistics; F10 failing ⇒ treat as data-snooped.

## Crypto portability

**unproven.** The mechanism is a *ported hypothesis*, not crypto evidence: the source studies only U.S. cash equities and contains **zero crypto content**.

- **What could port in form:** the algorithm is market-agnostic — a P-Tree maximizing cross-cluster forecastability over lagged features, plus per-leaf regularized forecasts and a forecast-implied long-short book, could be written on a BTC/ETH/perpetual universe with price/volume/liquidity/on-chain features in place of the 51 accounting characteristics; the regime layer could use crypto-native aggregates (funding, OI, stablecoin supply, realized-vol percentile) instead of dividend yield and Pastor–Stambaugh liquidity.
- **What breaks the mechanism:** the headline splits are **`sue`, `ep`, `sp`, `cfp`, `acc`, `noa`** — accounting/earnings variables with **no crypto counterpart**, so the paper's strongest cell cannot be reconstructed; equity **long-short requires borrow** (crypto perp shorts instead carry **funding** and liquidation risk the source never models); **24/7 sessions and fragmented venues** break the monthly, single-calendar panel and the timestamp conventions; there is no closing-auction/market-close alignment, no CRSP-style point-in-time membership (listing/delisting survivorship becomes a first-order issue), dividends are absent but stablecoin/de-peg and custody risks appear instead; and the source's own cost model (flat 10 bp/trade) is irrelevant to taker-fee + funding + spread crypto execution.
- Anything beyond "the algorithm can be re-run on another asset class" — the feature set, thresholds, rebalance cadence, funding treatment and venue policy — is `research-proposed` and untested. This record must never be cited as crypto evidence.

## Limitations

- **`data gap` — cost model:** a single flat 10 bp/trade parameter; commission, spread, slippage, impact, participation, borrow, financing, latency, fill and capacity are all absent (word scan), and realised **turnover is never reported**.
- **`data gap` — execution:** no order type, no fill model, no execution price/time, no rebalancing cadence printed, no partial-failure handling.
- **`data gap` — point-in-time fundamentals:** no accounting-publication-lag treatment for the very characteristics (`sue`, `ep`) that drive the first splits.
- **`data gap` — data provenance:** vendors/releases for the 51 characteristics and 8 market predictors are not stated; the inverse-variance window, the CV grid for λ, and the baseline winsorization level are never printed.
- **`data gap` — inference:** no standard-error convention (Newey–West/HAC/bootstrap) anywhere; no multiplicity control across the reported grid; SY4 alphas limited to 2003–2016.
- **`data gap` — reproducibility:** no code, no data-availability statement, no replication package, proprietary input data; SSRN mirror versions not opened this run, so cross-version numeric equivalence is unknown.
- **`underspecified`:** rebalancing cadence (monthly only by inference), excess-return benchmark, tie handling, the exact Y/N side of the last two splits of the top leaf beyond the prose description, and all exit/risk rules (there are none).
- **`unproven` / `not independently reproduced`:** every R², Sharpe, alpha, return and drawdown in this record; the top-cell in-sample R² of 10.73%; the OOS high-group R² of 3.84%; the 1.86/1.80 OOS Sharpes; the T−B differential spreads.
- **Source quality:** NBER working paper, **explicitly not peer reviewed**; no independent replication cited; the paper itself frames its robustness section as a reply to methodological-sensitivity critiques (Cakici et al. 2025).
- The record's own numbers are **U.S. equity evidence** (monthly, 1973–2022) and must never be presented as crypto, futures or cross-asset evidence.

## Implementation status

`implementation_status: not-implemented`. No P-Tree code, no characteristic pipeline, no portfolio backtest, no Qlib run, no production card and no Paper/Testnet/Live activity exists in our research stack as of 2026-09-27. This document is a normalized research capture only; the falsification plan above has not been executed.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record in the staging repository does **not** mean it passed Research Intake Review, entered Hermes Wiki Brain, entered the production candidate pool, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, or is approved for implementation, paper trading, testnet or live trading. No performance claim here is our own verified result.

## Related Wiki records

Wiki Brain `kb_search` run on 2026-09-27 (read-only; **nothing written**): `return predictability heterogeneity clustering machine learning cross-sectional` → 0 results; `anomaly zoo publication bias decay` → 0 results; `return predictability` → 10 results. Only verified pages are linked:

- [[quant/csi300-regime-augmented-harq-xgboost-low-vol-gated-2026-09-05]] — mechanism-adjacent: regime-gated ML cross-sectional equity forecasting that explicitly separates strong volatility predictability from weak directional predictability.
- [[quant/drift-regime-gated-cross-sectional-value-reversal-2026-09-05]] — adjacent cross-sectional value/reversal with a regime gate, useful for the regime-layer ablation (F12).
- [[quant/forecasted-tangency-minimum-euclidean-distance-portfolio-2026-09-04]] — adjacent: building portfolios directly from return forecasts (the forecast-implied step of §5.2).
- [[quant/sec-form-10-12b-spinoff-drift-decay-falsification-2026-09-13]] — negative-evidence context: drift-type anomalies that weakened after publication (McLean–Pontiff decay).

No other related Wiki page was found; absence is a search result, not a claim that none exists. **Zero repository records and zero Wiki pages share this source identity** (see Provenance dedup).

## Sources

1. Lin William Cong, Guanhao Feng, Jingyu He, Yuanzhi Wang. *"Mosaics of Predictability."* **NBER Working Paper No. 35158**, Issue Date **April 2026**. DOI `10.3386/w35158`. Landing: https://www.nber.org/papers/w35158 (four authors, JEL codes, DOI, issue date and `citation_*` meta tags verified directly from the landing HTML on 2026-09-27).
2. Same paper, **pinned primary PDF**: https://www.nber.org/system/files/working_papers/w35158/w35158.pdf — **72 pages, 1,321,976 bytes, SHA-256 `9e782aafc28421994216fae6a5dc57bbab5d32d4edf604d15cb9ce8033d416ca`**, retrieved and read end-to-end 2026-09-27. Provenance for the Abstract, §1–§6, Appendix A.1–A.5 (Tables A.1–A.10), Internet Appendix IA.1–IA.2 (Figure IA.1, Tables IA.1–IA.5), Figures 1–6, and the cost sentence in Appendix A.4.7.
3. https://doi.org/10.3386/w35158 — DOI resolution for the working paper.
4. Version landscape (identification only, **not opened this run**; SSRN is Cloudflare-protected for non-browser clients): SSRN `abstract_id=6705515` (NBER mirror, search metadata "Posted 5 May 2026 / Last revised 18 May 2026") and an earlier author-posted SSRN entry (search metadata "Posted 06 Jun 2024 / Last Revised 27 Apr 2026") — recorded so a future run can verify cross-version numeric equivalence. No claim in this record comes from either mirror.
5. Works **cited by the source** and used here only as mechanism context (not read for this record): Cong, Feng, He & He (2025), *Growing the Efficient Frontier on Panel Trees*, JFE 167:104024 (the P-Tree framework this paper adapts); Gu, Kelly & Xiu (2020), RFS 33(5) (the homogeneous ML benchmark); Farmer, Schmidt & Timmermann (2023), JF 78(3) *Pockets of Predictability* and Cakici et al. (2025), Critical Finance Review (the methodological-sensitivity critique the Internet Appendix answers); Campbell & Shiller (1988); Pastor & Stambaugh (2003).
