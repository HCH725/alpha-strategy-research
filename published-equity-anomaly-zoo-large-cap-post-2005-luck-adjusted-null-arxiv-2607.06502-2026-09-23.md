---
schema: strategy-research-record-v1
title: Published equity anomaly zoo in the investable large-cap universe post-2005 — 7 bp median, Var(t)=1.09 luck-adjusted null (What Useful Alphas?)
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-07-07
sources:
  - "https://arxiv.org/abs/2607.06502 — arXiv:2607.06502v1 [q-fin.GN], 'What Useful Alphas?', Andrew Y. Chen; Ivo Welch, submitted 2026-07-07 (read 2026-09-23)"
  - "https://arxiv.org/pdf/2607.06502v1 — pinned canonical PDF v1, 24 pages, 427,439 bytes, SHA-256 968f0d62fb24aaea41919f036bf958d13364e4d656b23e8480f87c4518309b4b, title page line 'Draft: July 8, 2026' (fully read 2026-09-23)"
  - "https://arxiv.org/html/2607.06502v1 — arXiv HTML rendering of v1, 85,464 bytes, SHA-256 e23f3cb1194f719b2fcc7ac0ec06cbe50f59c976688eb824e5921209d466084d, carries line 'Draft: August 24, 2026' (date line differs from the pinned PDF; read 2026-09-23)"
  - "https://www.openassetpricing.com — Chen & Zimmermann (2022) open-source cross-sectional asset pricing dataset used by the paper (Critical Finance Review 11, pp. 207–264); NOT fetched by the Scout this run, so dataset release/vintage is a data gap"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Published equity anomaly zoo in the investable large-cap universe post-2005 — 7 bp median, Var(t)=1.09 luck-adjusted null (What Useful Alphas?)

## Provenance

- **Primary source (pinned):** Andrew Y. Chen (Federal Reserve Board) and Ivo Welch (UCLA), *"What Useful Alphas?"*, arXiv:2607.06502v1 `[q-fin.GN]`, submitted **2026-07-07 17:02:53 UTC** (submission history on the abstract page shows **v1 only**; `arxiv.org/html/2607.06502v2` and `v3` both returned HTTP 404 on 2026-09-23). License **CC BY 4.0** (stated on the HTML page and in the PDF metadata `/License`). Cite-as: `arXiv:2607.06502 [q-fin.GN]`. The abstract page carries **no journal reference** and **no comment field**; the only DOI present is the arXiv/DataCite DOI `10.48550/arXiv.2607.06502` (PDF metadata `/DOI`), i.e. **not a journal DOI**.
- **Publication status:** preprint. The paper's own title page states **"Target: Financial Analysts Journal."** No acceptance, revision, or peer-review status is stated in-source → **data gap** on review status beyond that target line.
- **Version / date discrepancy inside the source (recorded, not smoothed):** the pinned **PDF v1** title page reads **"Draft: July 8, 2026"**, while the **arXiv HTML rendering of the same v1** (fetched 2026-09-23) reads **"Draft: August 24, 2026"**. Every number cited in this record was verified present in the **PDF** (canonical artifact); the HTML was read in full as a second copy. The two renderings disagree on the draft date line → **underspecified / data gap** on which draft date the authors intend.
- **Primary-source checksum (performed 2026-09-23):** three artifacts fetched and hashed — (a) abstract page `https://arxiv.org/abs/2607.06502`, 39,071 bytes, SHA-256 `9ce20e1cef2b467b025dbb0b574e844903b1cd5620e420ca4c2e8c676287db92`; (b) pinned PDF `https://arxiv.org/pdf/2607.06502v1`, 427,439 bytes, SHA-256 `968f0d62fb24aaea41919f036bf958d13364e4d656b23e8480f87c4518309b4b`, 24 pages, PDF metadata `/Title` = "What Useful Alphas?", `/Author` = "Andrew Y. Chen; Ivo Welch", `/arXivID` = `.../2607.06502v1`; (c) HTML rendering `https://arxiv.org/html/2607.06502v1`, 85,464 bytes, SHA-256 `e23f3cb1194f719b2fcc7ac0ec06cbe50f59c976688eb824e5921209d466084d`.
- **Sections read in full:** Abstract; §I Introduction; §II Data and Universe Filters; §III Post-2005 Returns in the Investable Universe; §IV The Anatomy of Published Alphas; §V Literature; §VI Conclusion; References; **Table 1, Table 2, Table 3** (with their Explanations/Interpretation captions); **Figure 1, Figure 2, Figure 3** captions and axis labels; **Appendix A "A Very Simple Bayes-Stein Shrinkage Formula"** (assumptions, derivation, illustration, sign-orientation discussion). Both the PDF and the HTML rendering were read end-to-end.
- **Data identity:** the study runs entirely on the open-source **Chen and Zimmermann (2022)** dataset at `openassetpricing.com` (*"Open source cross-sectional asset pricing"*, Critical Finance Review 11, pp. 207–264), which "reproduces nearly all published cross-sectional return predictors using standardized code and methodology" (§II). The Scout did **not** fetch the dataset itself this run → **data gap** on dataset release/vintage and on the exact stock-level inputs.
- **Whole-repository source-identity dedup (2026-09-23, ripgrep across all 898 tracked `*.md`, not `git log` alone; `coverage_manifest.csv` also checked):** `2607.06502` = 0 hits; `arxiv.org/abs/2607.06502` = 0; `arxiv.org/pdf/2607.06502` = 0; exact title `What Useful Alphas` = 0; `Andrew Y. Chen` = 0; DOI (none exists beyond the arXiv DataCite DOI, also 0); coverage_manifest = 0 for `2607.06502`, `What Useful Alphas`, `openassetpricing`. **No existing record carries this source identity.**
- **Neighbours checked and kept distinct:** (1) `directional-anomaly-zoo-net-cost-audit-quality-survivor-2026-09-23.md` (Bryan Vine, Alpha Research Paper 4, `bryanvine.github.io/alpha-research/paper4.html`, commit `655e8d4f…`) is the only other record touching `openassetpricing` — **different source, different claims** (see Economic mechanism → Research interpretation and Negative evidence for the explicit material distinctions). (2) `reviving-anomalies-expected-net-return-double-sort-1n-implementable-2026-09-23.md` (SSRN 6468806) rebuilds published anomalies with ML expected-net-return sorts — different source, different mechanism (constructive net-return signal vs. this record's era×universe decomposition plus noise benchmark). (3) `conditioning-sign-on-magnitude-return-decomposition-csm-2026-09-04.md` contains the string `Ivo Welch` as a citation to a *different* work — no source-identity overlap.

## Economic mechanism

### Source-reported

The paper does not propose a new trading rule; it audits the **population of ~200 published long-short anomaly portfolios** and asks why the literature's headline returns are unavailable to a practitioner today. Three source-stated mechanisms explain the collapse (Abstract, §I, §IV):

1. **Post-publication decay plus a trading-technology regime change (time dimension).** "Once an anomaly is published, sophisticated investors trade on it, compressing returns" — with McLean–Pontiff (2016) cited for a roughly 50% post-publication decline and Chen–Zimmermann (2020) confirming it in a larger dataset; alongside decimalization (2001), algorithmic trading and electronic market making, which "reduced trading costs and made it easier for arbitrageurs to act on published signals" (§IV).
2. **Micro-cap concentration and inaccessibility (size dimension).** "Most of the action in anomaly portfolios comes from small and microcap stocks… wider bid–ask spreads, lower institutional ownership, and less analyst coverage, all of which allow mispricings to persist. When we exclude them, the anomaly returns shrink because the large-cap stocks that remain are more efficiently priced" — explicitly *not* a claim that the anomalies were "fake" in small stocks, but that the returns "were concentrated in a segment of the market that most institutional investors cannot practically access at scale" (§IV).
3. **Selection plus statistical noise (the luck benchmark).** Each t-statistic is "true signal plus sampling noise, and the noise has variance 1 by construction… even if every anomaly's true return were zero, the t-statistics of ~200 anomalies would still scatter with a cross-sectional variance of about 1 — the dispersion of 200 dart-throwing monkeys. Only spread beyond 1 is evidence of genuine differences across anomalies" (§III, Appendix A, after Efron 2010). Because the portfolios are each **signed in the direction the original paper documented** (Appendix A, "Sign orientation"), the cross-section is a *selected, positively-signed* set, so its common mean "is mechanically positive rather than a clean average of underlying premia".

The paper's own summary of mechanism is that the anomalies "were real… they were not fake. They were, however, traded away" (§V, footnote 2), and that "statistical significance and economic implementability are different things" (§IV).

### Research interpretation

**Falsifiable hypothesis captured here:** *the standard published equity anomalies, implemented as described in their original papers, deliver approximately zero economically usable alpha in the investable non-micro-cap universe after 2005 — the residual cross-section is statistically consistent with pure selection noise.*

- **Type of record:** a **population-level negative-alpha hypothesis** over ~200/204/170 anomaly portfolios (N varies by universe filter, Table 1), not a single tradable signal. It is a *falsifiable* claim about a menu of strategies that other records in this repository build or test individually.
- **Hypothesized mechanism in our words:** crowding/competition arbitrates published signals (publication decay), the economically meaningful part of the premium lives in an **institutionally inaccessible micro-cap segment** (market-friction/segment mechanism), and what remains in large caps is dominated by **multiple-testing and sign-selection noise** (statistical mechanism) rather than by risk compensation or persistent mispricing.
- **Material distinction from the nearest sibling record** (`directional-anomaly-zoo-net-cost-audit-quality-survivor-2026-09-23.md`, Alpha Research Paper 4 — different source identity): (a) **universe** — Paper 4 uses all-stock equal-weight decile long-shorts (OSAP 212 predictors) with no investability filter, whereas Chen–Welch's central object is the **top-90% / top-3,000 non-micro universe** (Standard filter, N=170); (b) **horizon/regime split** — Paper 4 splits in-sample vs. out-of-sample for decay measurement, Chen–Welch split **through-2005 vs. post-2005** as an era × universe 2×2; (c) **mechanism of disappearance** — Paper 4 attributes the collapse mainly to **turnover cost ladders** (0/30/60 bp per month of turnover → 86%/43%/19% positive) and reports a **low-turnover quality survivor**, whereas Chen–Welch attribute it to **era + universe + selection noise**, apply an **empirical-Bayes shrinkage** (Var(t)=1.09 → factor ≈0.084) and conclude survivors are "almost entirely accounted for by luck"; (d) **cross-check scope** — Paper 4 cross-checks on its own equity **and crypto** data; Chen–Welch use **only** the Chen–Zimmermann equity dataset and no crypto arm. The two sources therefore reach **tension-bearing but independent conclusions** on an overlapping data family (documented under Negative evidence).
- **What each component contributes:** regime = the era split and the universe filter (the paper's two "dimensions"); measurement object = the standardized monthly long-short anomaly portfolios; statistical adjustment = the Bayes-Stein/Efron shrinkage; there is **no entry/exit overlay** — this is a return-distribution study. Do not read the 2×2 cells as a tradable timing rule; they are descriptive decompositions.

## Signal

**Signal object:** one cross-section per month of standardized, **zero-investment long–short anomaly portfolio returns** taken from the Chen–Zimmermann (2022) dataset, re-formed under the paper's universe filters. The record normalizes the construction below; everything marked *source-reported* is stated in the pinned PDF.

- **Formation timestamp / tradability:** portfolios are **monthly**; the sparse-signal rule explicitly sets a **next-month** return ("we use a long-short return of zero for the next month", §II), implying signal-month *t* → return in month *t+1* for that rule. No intraday or daily timing is defined. Timezone/session convention: **not stated in source** (CRSP monthly data) → data gap.
- **Lookback / warm-up:** per-anomaly lookbacks are inherited from each original paper's characteristic construction (dataset-standardized, "typically using quintile or decile sorts", §II). Table 2 requires each signal to have **at least 30 post-2005 months** (Table 2 caption). The pre-2005 sparsity screen uses the **1986–2005** window. Exact per-characteristic windows → **underspecified in this paper** (they live in the dataset's standardized code).
- **Universe filters (monthly, source-reported, §II):**
  - **Standard (N3000, 90%)** — *the paper's main filter* — intersection of the top 3,000 stocks by rank **and** stocks collectively holding the top 90% of total market capitalization;
  - **Rank Only (N3000)**, **Pct Only (90%)**, **Tight (N1000, 80%)** (alternative filters); "Standard and Pct Only give identical results because the 90% market-cap screen is more restrictive than the 3,000-stock rank screen" (Table 1 caption);
  - "No Constraint" = each anomaly's original all-stock portfolio from the dataset, no market-cap filter (Table 1 caption).
- **Era split (source-reported, §II):** **through 2005** (≤ 2005-12) vs. **post-2005** (≥ 2006-01); split chosen after decimalization (2001) and following Chen–Velikov (2023)'s end-2005 split; "the precise split date is unimportant, but it must be after 2001".
- **Sparse-signal / missing-data rules (source-reported, §II):**
  1. *Pre-2005 screen:* for each filter, **drop** the signal if **more than 5%** of its available months in the **1986–2005** sample have **fewer than 20 stocks in either the long or the short leg** (denominator is the signal's own available months, so late-starting signals are not penalized).
  2. *Post-2005:* if either leg holds **fewer than 20 stocks** in a month, the **next-month long–short return is set to zero** — "effectively assuming that the investor declines to trade due to insufficient diversification".
  These two rules are why **N varies by filter**: Table 1 reports **N = 204 (No Constraint), 170 (Standard), 194 (Rank Only), 170 (Pct Only), 161 (Tight)**.
- **Direction / sign convention (source-reported, Appendix A):** "The Chen and Zimmermann (2022) portfolios are signed so that each long–short return was positive in the direction the original paper documented." This orientation does not change Var(t) but **does** change the shrinkage target (see below).
- **Entry / exit / holding / re-entry:** long leg = top sort, short leg = bottom sort, held with **monthly rebalancing** ("Our analysis uses the standard monthly-rebalanced long-short portfolios", §V). No stop, no take-profit, no holding cap, no entry threshold, no sizing rule is defined in-source.
- **Statistical overlay — empirical Bayes shrinkage (source-reported, §III + Appendix A):** `r_adj = [1 − 1/Var(t)] · r`, equivalent to Efron (2010) eq. (1.16) and Chen–Dim (2023) eq. (8), with assumptions "θ ~ Normal with mean zero, and θ and δ independent **within and across predictors**" and Var(t) estimated from the cross-section of post-2005 signal-level t-statistics; the factor is **truncated at zero**. Post-2005 Standard: **Var(t) = 1.09 → factor ≈ 0.084** for long–short returns; for long-minus-market returns **Var(t) = 0.98 < 1 → factor = 0**, so *every* adjusted long-leg mean is zero (Table 2 caption), equal to the common average of about **−4 bp/month** (Appendix A).
- **Shrinkage-target sensitivity, source-reported (Appendix A):** shrinking **toward zero** (what Table 2 reports) puts the best survivor at **≈6 bp/month**; shrinking **toward the cross-sectional mean** (mean t ≈ 0.45, mean long–short return 8 bp) would leave the **median anomaly at ≈8 bp** and the **best survivor at ≈13 bp/month before trading costs**. The paper states "it is not clear what one should shrink toward" and argues the mean "is not a neutral target" because the set is selected and positively signed.
- **Ranking/exclusion rules (source-reported, Table 2 caption):** **IO_ShortInterest is excluded** from the top-10 ranking "due to a suspected data construction issue"; **MomRev is excluded** as "a curated overlap with the momentum survivor family".
- **Parameter provenance:** every threshold above (3,000 / 90% / 1,000 / 80% / 5% / 20 stocks / 1986–2005 / end-2005 / 30 months) is **source-reported**. **Scout-generated operationalization: `research-proposed: none`** — this record contains **zero** Scout-created entry, exit, filter, stop, sizing, or execution rules; all thresholds are quoted from the pinned PDF or explicitly labelled `research-defined` in the Falsification plan.
- **Reconstructability verdict:** **partially reproducible.** The universe filters, era split, sparsity rules, rebalance cadence and shrinkage formula are fully specified; per-anomaly characteristic definitions, the exact post-2005 **sample end date**, the exact N retained per table (beyond Table 1/2/3 values), and the **t-statistic estimation method** are **not stated in source** → signal marked **underspecified** on those points, not presented as fully reproducible.

## Required data

- **Instrument / universe:** US-listed common stocks in CRSP as reproduced by the Chen–Zimmermann (2022) dataset; screens applied monthly by rank and by share of **total market capitalization** (top 90% / top 80%). No crypto, no futures, no options.
- **Market type:** cash equities (long and short legs); zero-investment long–short construction.
- **Venue / vendor:** CRSP via the open-source dataset (`openassetpricing.com`); Fama–French market return used for the long-minus-market panel (Figure 1 Panel B, Table 2 caption: "Mkt – RF plus RF").
- **Timeframe / fields:** monthly long–short returns and CAPM alphas; per-stock characteristics for the screens; market cap for the rank/percentage filters. No order book, no depth, no funding, no open interest, no on-chain fields.
- **Point-in-time / availability:** era split at 2005-12/2006-01 is the paper's only explicit vintage control; the pre-2005 sparsity screen uses only data through 2005 (§II) — a genuine point-in-time guard for *that* screen. Whether the underlying dataset code itself is point-in-time is **not discussed in this paper** → data gap.
- **Sample period:** **through 2005** (≤ 2005-12) and **post-2005** (≥ 2006-01); sparsity window **1986–2005**; Table 2 requires **≥30 post-2005 months**. **The end date of the post-2005 sample is never stated** anywhere in the abstract, §I–§VI, tables, figures, or Appendix A (checked: no `2024`/data-end statement; only a hypothetical "portfolio manager operating in 2025") → **data gap**. The in-document draft dates (PDF "July 8, 2026"; HTML "August 24, 2026") bound the vintage only loosely.
- **Missing-data handling:** the two sparse-signal rules above; **no imputation** is used (zero-returns are an explicit "decline to trade" convention, not an imputed price). Table 2 additionally requires ≥30 post-2005 months and drops two named signals.
- **Cost/fee fields:** none collected in-source (see Execution assumptions); dataset returns are **gross**.

## Execution assumptions

All items below are read from §II (Data and Universe Filters), §III, §IV, §V, §VI and Appendix A — the paper's method sections — not from the abstract alone.

- **Signal-to-order timing / fill model:** **not stated in source.** The only timing statement is the sparse rule's next-month return convention (§II). No same-bar/next-bar execution discussion, no partial-fill or failure handling → **data gap**.
- **Order type:** **not stated in source** → data gap.
- **Fees / spread / slippage / impact:** **no cost model is computed for this paper's own return numbers.** The 48/26/19/7 bp cells, Table 1–3 statistics and the shrinkage results are all **gross** zero-investment long–short returns ("about 1% per year **before trading costs**", §III and §VI finding 1). The cost argument is carried **by citation**: §V quotes **Chen and Velikov (2023)** — anomaly portfolios overweight names at "about four times the median NYSE spread" and "turn over roughly 40% of their two legs each month, so a half-spread of even 25 bps implies a round-trip cost near 20 bps per month"; averaged across **204 anomalies**, mean long–short return **net of costs ≈ −1 bp/month post-2005** under original implementations, rising to **≈ +4 bp** under cost-minimizing execution; combinations fall from **250–380 bp/month gross through 2005 to 0–20 bp net afterward** — with the source's own qualifier that "these figures span the **full stock universe**, where gross returns exceed those in our large-cap universe. The small gross returns of Section III are therefore **upper bounds** on what a large-cap manager could actually net." **Provenance caveat:** those five numbers are **secondary-within-the-primary** (quoted from Chen–Welch §V); the Scout did **not** open Chen–Velikov (2023) directly → treat them as source-quoted, not independently verified. **The precise cost level at which the 7 bp median dies is therefore not computed in-source** → data gap.
- **Borrow / shorting:** the construction **requires a short leg**; §VI finding 3 states the best survivor's return "even this required shorting — the long-only return was at most zero net of selection bias". **Borrow fees, locate availability and hard-to-borrow effects are not modelled anywhere in the paper** → data gap.
- **Leverage / margin:** not applicable to a zero-investment long–short; **no leverage assumption stated** → not stated in source.
- **Capacity / liquidity / participation:** **no capacity or ADV/participation analysis appears in the paper** (the word "capacity" does not appear); the size filter is the only liquidity-aware device (§IV Figure 2: "predictability monotonically decreases in the liquidity of the set of stocks being considered") → capacity **data gap**.
- **Latency:** not stated in source → data gap.
- **Net-vs-gross label:** **gross**. Any net figure in this record is explicitly attributed either to the cited Chen–Velikov numbers or to our `research-defined` cost stress tests.

## Evidence

### Source-reported

Every figure below is traced to the pinned PDF (identical text verified in the HTML rendering unless noted). "bp" = basis points **per month**; Table 1–3 returns and alphas are in **percent per month** (Table 1 caption).

**Headline 2×2 (Abstract, §I, §IV, Figure 3, §VI findings 1–2)** — median zero-investment long–short return per anomaly:

| Cell (Figure 3 panel) | Period | Universe | Median | Mean | % positive |
|---|---|---|---|---|---|
| Panel A (upper-left, "original-paper environment") | through 2005 | all stocks | **0.48% (48 bp)** | 0.57% | **99%** |
| Panel B (upper-right) | through 2005 | top 90% mkt cap (Standard) | **0.26% (26 bp)** | 0.28% | 92% |
| Panel C (lower-left) | post-2005 | all stocks | **0.19% (19 bp)** | 0.25% | 80% |
| Panel D (lower-right, "practitioner reality") | post-2005 | top 90% mkt cap (Standard) | **0.07% (7 bp)** | 0.08% | **67%** |

Decomposition (§I, §IV, §VI finding 2): restricting the **period** to post-2005 cuts the median by **≈60%**; restricting the **universe** to the top 90% cuts it by **≈one-half**; **together ≈85%**; "the two effects are roughly multiplicative… there is no single villain."

**Table 1 — Anomaly Long-Short Returns Post-2005, by Universe Filter** (columns = No Constraint | Standard | Rank Only | Pct Only | Tight):

| Statistic | No Constraint | Standard | Rank Only | Pct Only | Tight |
|---|---|---|---|---|---|
| Mean (%/mo) | 0.25 | 0.08 | 0.13 | 0.08 | 0.09 |
| Median (%/mo) | 0.19 | **0.07** | 0.12 | 0.07 | 0.07 |
| 25th pct | 0.02 | −0.04 | −0.02 | −0.04 | −0.03 |
| 75th pct | 0.39 | 0.18 | 0.25 | 0.18 | 0.21 |
| % pos | 80 | 67 | 71 | 67 | 68 |
| Med. t | 1.11 | **0.45** | 0.60 | 0.45 | 0.46 |
| Med. SR (annualized) | 0.26 | **0.11** | 0.14 | 0.11 | 0.11 |
| Med. α (CAPM, %/mo) | 0.23 | **0.09** | 0.17 | 0.09 | 0.13 |
| Med. t(α) | 1.53 | **0.64** | 1.09 | 0.64 | 0.70 |
| N | 204 | **170** | 194 | 170 | 161 |

Supporting prose (§III): interquartile range under Standard ≈ **−4 to +18 bp**; "the vast majority of anomalies were statistically indistinguishable from zero"; median return of 7 bp ≈ **1% per year before trading costs**.

**Figure 1 — Post-2005 Standard signal-level t-statistics:** Panel A (Long–Short) **mean t = +0.48**; Panel B (Long minus FF market) **mean t = −0.31**; caption interpretation: the long–short right tail "deviates slightly from the standard normal, implying some amount of true non-zero expected returns", but "long-minus-market returns are very close to the standard normal, implying any long leg outperformance is entirely due to luck."

**Luck/noise benchmark (§III, Appendix A):** **Var(t) of post-2005 Standard long–short t-statistics = 1.09** → signal share `1 − 1/1.09 ≈ 0.08`; "the luck-adjusted return of every anomaly collapsed to nearly zero"; **best survivor in Table 2: raw 66 bp → luck-adjusted 6 bp**. For long-minus-market, **Var(t) = 0.98 < 1** → truncation at zero → every adjusted long-leg mean = common average ≈ **−4 bp/month** (Appendix A).

**Table 2 — Top 10 anomalies, post-2005, Standard (N3000, 90%)**, columns = mean monthly long–short | mean long-minus-market | adjusted LS | adjusted long–minus-market (empirical Bayes toward zero), with original-paper citation:

| Anomaly | LS mean | Long–Mkt | Adj. LS | Adj. Long–Mkt | Original paper |
|---|---|---|---|---|---|
| Cash-based operating profitability | **0.66** | 0.40 | **0.06** | 0.00 | Ball et al. (2016) |
| Operating profitability (R&D adj) | 0.60 | 0.26 | 0.05 | 0.00 | Ball et al. (2016) |
| Realized-implied volatility spread | 0.59 | 0.35 | 0.05 | 0.00 | Bali & Hovakimian (2009) |
| Off-season momentum | 0.54 | 0.13 | 0.05 | 0.00 | Heston & Sadka (2008) |
| Net external financing | 0.48 | 0.15 | 0.04 | 0.00 | Bradshaw, Richardson & Sloan (2006) |
| Seasonal momentum (16yr+) | 0.48 | 0.21 | 0.04 | 0.00 | Heston & Sadka (2008) |
| Gross profitability | 0.44 | 0.14 | 0.04 | 0.00 | Novy-Marx (2013) |
| R&D over market cap | 0.41 | 0.33 | 0.03 | 0.00 | Chan, Lakonishok & Sougiannis (2001) |
| Net equity financing | 0.39 | 0.16 | 0.03 | 0.00 | Bradshaw et al. (2006) |
| Operating leverage | 0.38 | −0.01 | 0.03 | 0.00 | Novy-Marx (2011) |
| **Mean, all 170** | 0.08 | −0.04 | 0.01 | 0.00 | — |
| **SD, all 170** | 0.18 | 0.13 | 0.02 | 0.00 | — |

Caption notes: signals need ≥30 post-2005 months; IO_ShortInterest and MomRev excluded from the ranking (reasons above); "the survivors are predominantly profitability and financing signals… their empirical Bayes adjusted means are **at most 6 bps per month**."

**Table 3 — by category, post-2005, Standard** (N | mean | median | 25th | 75th | % pos): Momentum **17 | 0.01 | 0.05 | −0.16 | 0.09 | 53**; Profitability **9 | 0.25 | 0.24 | 0.09 | 0.44 | 78**; Value/Fundamentals **15 | −0.02 | −0.04 | −0.11 | 0.10 | 47**; Investment/Growth **36 | 0.09 | 0.06 | −0.02 | 0.18 | 69**; Trading/Liquidity **13 | 0.09 | 0.11 | 0.03 | 0.13 | 85**; Accruals/Accounting **18 | 0.09 | 0.06 | −0.02 | 0.19 | 72**; Intangibles **12 | 0.04 | 0.00 | −0.02 | 0.07 | 50**; Other **50 | 0.10 | 0.11 | −0.03 | 0.18 | 72**; **All 170 | 0.08 | 0.07 | −0.04 | 0.18 | 67**. Caption: "Category counts and boundaries are approximate. Some anomalies span categories." Interpretation line: "Profitability is the only category with a healthy median return. Momentum, value, and intangibles-based anomalies no longer outperformed in this universe."

**Survivor characterisation (§III, §VI finding 3):** survivors "dominated by profitability and financing signals"; the one volatility signal on the list is the realized-implied volatility spread; only two momentum variants remain (off-season, long-horizon seasonal); **raw returns of the best strategies ≈59–66 bp**, "well below their published in-sample values"; **profitability category averaged ≈25 bp/month**; selection-bias adjustment ⇒ "even the very strongest anomaly earned only 6 bps per month"; surviving momentum variants' **≈50 bp** in the top 90% sits below the **1.0–1.5%/month** reported by Jegadeesh & Titman (1993) on the full universe (source-quoted), and momentum "carries well-known crash risk (Daniel and Moskowitz 2016), which is not reflected in average returns."

**Shrinkage-target sensitivity (Appendix A):** toward-zero ⇒ best survivor **≈6 bp**; toward-the-mean ⇒ median anomaly **≈8 bp**, best survivor **≈13 bp** before trading costs. The paper explicitly declines to pick a target: "It is not clear what one should shrink toward."

**Cost numbers quoted by the source (§V, from Chen & Velikov 2023 — secondary-within-primary):** spreads ≈4× median NYSE spread; ≈40%/month two-leg turnover; half-spread 25 bp ⇒ ≈20 bp/month round trip; mean net ≈ −1 bp (post-2005, original implementations) vs ≈ +4 bp (cost-minimizing execution), across **204 anomalies**; combination gross 250–380 bp/month through 2005 → **0–20 bp net** afterward; and the source's own warning that these span the **full stock universe** so §III's small gross returns are **upper bounds** on what a large-cap manager can net.

**Publication/claim status (Abstract, §VI):** "The evidence strongly suggests that published academic anomalies have been useless to non-micro-cap portfolio managers in the 21st century. Public stock markets were very efficient." Scope limit stated by the authors: "We claim only that the standard published anomalies, implemented as described in their original papers, offered little in the investable universe after 2005."

### Independently reproduced

**Not independently reproduced.** No re-run of the Chen–Zimmermann pipeline, no re-estimation of Var(t), and no retrieval of the dataset were performed in this run; all numbers above are source-reported from the pinned PDF.

### Negative evidence

*Carried by the source itself:*

1. **The record's core content is negative evidence** against the ~200 published anomalies as a tradable menu in the investable universe: median 7 bp gross (≈1%/yr), median t = 0.45, median annualized Sharpe = 0.11, 67% positive, Var(t) = 1.09 ⇒ signal share ≈8%, long-leg performance "entirely due to luck" (Figure 1 Panel B, mean t = −0.31, Var(t) = 0.98).
2. **Source-declared caveats that bound the negative claim (§V, §VI):** "we do not claim that no anomaly-based strategy can ever be profitable"; **dynamic factor timing** (Haddad, Kozak & Santosh 2020), **volatility-managed portfolios** (Moreira & Muir 2017), **machine-learning combinations** (Gu, Kelly & Xiu 2020; Freyberger, Neuhierl & Weber 2020) and proprietary/alternative-data strategies "seem to increase some returns again" and are **outside** their claim; dynamic strategies are "more difficult to assess" (Goetzmann et al. 2007, footnote 3).
3. **Anomalies were "true discoveries"** in the statistical sense (Chen 2021) and "not fake" — the negative result is about *availability after 2005 in large caps*, not about fabrication (§V footnote 2, §IV, §VI).
4. **Momentum's known crash risk** (Daniel & Moskowitz 2016) is not reflected in average returns (§III) — an additional downside the averages hide.
5. **Cost erasure is argued, not measured in-source** (§V): with the quoted ~20 bp/month round trip versus a 7 bp gross median, the sign of net returns in the Standard universe is left to the reader → the paper's own "even minimal trading costs would eliminate" claim is an inference from another paper's full-universe cost estimates.

*Scout-marked (our analysis, labelled):*

6. **Inter-record tension (research interpretation):** the sibling record `directional-anomaly-zoo-net-cost-audit-quality-survivor-2026-09-23.md` (Bryan Vine Paper 4) concludes **"the lone robust survivor is low-turnover quality"** at a 30 bp/month turnover cost (43% of predictors positive), whereas Chen–Welch conclude survivors are **"almost entirely accounted for by luck"** after empirical-Bayes shrinkage (best 6 bp toward zero / 13 bp toward the mean). Different sources, overlapping data family (Chen–Zimmermann / OSAP), **opposite practical readings** — a genuine, testable contradiction inside the staging pool; recorded here rather than resolved (we did not run either study).
7. **Shrinkage-target dependence (source-acknowledged):** the headline "6 bp" survivor figure is the *toward-zero* target; the *toward-mean* target gives **≈13 bp** and moves the median from ≈0 to ≈8 bp (Appendix A). The negative conclusion is therefore **target-conditional**, and the paper says so.
8. **Appendix A assumption to attack (research interpretation):** the derivation assumes θ and δ are independent **within and across predictors** and θ ~ N(0, ·). Anomalies share long legs and common factor shocks, so cross-sectional t-stat noise is unlikely to be independent — if cross-item noise correlation inflates the cross-sectional Var(t) beyond 1 for reasons unrelated to signal, the "signal share ≈ 8%" estimate is **biased upward in the noise direction** (or, if sign-selection compresses dispersion, downward). The paper does not stress-test this → `research-defined` test 4 below.
9. **Sign-selection mechanics (source-acknowledged, Appendix A):** every portfolio is signed in its own published winning direction, so the cross-section mean (8 bp, mean t ≈ 0.45) is mechanically positive; this is precisely why the shrinkage target matters (point 7).
10. **Sparse-rule zeros (research interpretation):** setting post-2005 returns to **zero** whenever either leg has <20 stocks pulls the cross-section toward zero and could **depress medians/means** in exactly the filtered universes the paper emphasises; the paper calls this an "implementation outcome" but reports no sensitivity excluding those months.
11. **Label ambiguity inside the source:** `0.45` is reported as the **median** t (Table 1) and also as the **"mean t-statistic … about 0.45"** (Appendix A), while Figure 1 Panel A states **mean t = +0.48** → mean/median labelling is inconsistent in-source; both values are recorded, neither is reconciled → data gap.
12. **No multiple-testing/deflated-Sharpe/HAC machinery:** the only selection adjustment is the Efron/Chen-Dim shrinkage; **no** deflated Sharpe, no White/Romano-Wolf, no Newey-West or other t-stat adjustment is described anywhere in §II–§VI or Appendix A (the strings "Newey", "heteroskedastic", "deflated", "bootstrap" do not appear) → t-stat estimation is **underspecified**, and serial correlation in monthly long–short returns could make every reported t too large.
13. **No capacity, borrow-cost, or fill analysis** (see Execution assumptions) → the 7 bp gross median is untested for implementability beyond the size filter itself.
14. **Vintage risk (research interpretation):** with no stated sample end date and no pinned dataset release, the post-2005 window could end anywhere in the last few years; a replication on a newer vintage may move every cell.
15. **Renderings disagree on the draft date line** (PDF "July 8, 2026" vs HTML "August 24, 2026") → the artifact identity should always be pinned by PDF SHA-256 `968f0d62…9b4b`, not by draft date.

## Falsification plan

**Source-provided falsification apparatus:** **none pre-registered.** The paper contains no numbered hypotheses, no pre-declared failure thresholds, and no power analysis → **data gap** on author-specified falsification. What the source *does* provide (§V, §VI) is an explicit standing challenge — implementations that use **dynamic factor timing, volatility-managed overlays, ML combinations, or proprietary/alternative data** "seem to increase some returns again" and lie outside its claim — plus an open replication invitation: "The reader can replicate and extend our analysis. We encourage practitioners and researchers to examine their own universe definitions, rebalancing frequencies, and cost assumptions."

**`research-defined` falsification tests (all thresholds chosen by the Scout, none by the source):**

1. **2×2 cell replication** — *Data:* current `openassetpricing.com` release, stock-level with our own Standard (N3000 ∩ 90%) screen. *Sample:* ≤2005-12 and ≥2006-01. *Metric:* median zero-investment long–short return per cell. *Threshold (`research-defined`):* replication is deemed **failed** if the post-2005 Standard median lies outside **[4, 14] bp/month** (i.e. ±7 bp around the reported 7 bp) **or** the through-2005 all-stock median lies outside **[34, 62] bp/month** (±14 around 48). *Action:* if failed, the decomposition magnitudes (60%/50%/85%) are rejected and the record's confidence drops to `low`.
2. **Noise-benchmark stability** — *Data/Sample:* post-2005 Standard signal-level t-stats. *Metric:* Var(t). *Threshold:* if Var(t) ∉ **[1.00, 1.30]**, the "signal share ≈ 8%" claim is treated as **unstable** (below 1.00 → truncation makes the adjustment zero; above 1.30 → factor ≥ 0.23, materially rescuing returns). *Action:* withdraw the luck-adjusted-null conclusion and re-label survivors as untested.
3. **Best-survivor re-test under the source's own targets** — *Metric:* empirical-Bayes adjusted mean of the top-ranked anomaly. *Threshold:* if adjusted mean ≥ **20 bp/month** under *either* shrinkage target (zero or mean), the "survivors ≈ luck" claim fails. *Action:* keep the record but flag the negative claim as rejected.
4. **t-stat construction audit (attacks Scout negative #12)** — *Metric:* recompute each t with Newey-West (lags 6) and with a deflated-Sharpe correction for the ~200 trials. *Threshold:* if the median |t| rises from 0.45 to **> 1.0**, or if ≥25% of anomalies clear |t| ≥ 1.96 HAC, the "statistically indistinguishable from zero" statement fails. *Action:* re-open the anomaly menu as candidates rather than a null.
5. **Cross-item noise-independence stress (attacks Scout negative #8)** — *Metric:* Var(t) computed after (a) de-meaning common factor shocks (regress each anomaly return on FF market/size/value/momentum, take residuals) and (b) block-bootstrap across time. *Threshold:* if adjusted Var(t) ≥ **1.6** (factor ≥ 0.375), the published signal share ≈ 8% is judged **understated by ≥ 4×** and the shrinkage conclusion is rejected. *Action:* record contradiction, drop confidence to `low`.
6. **Cost kill-point (turns the source's inference into a test)** — *Data:* our own cost schedule on the Standard universe (maker vs taker, 5/10/20 bp round trip) plus **borrow fees on the short leg** (absent in-source). *Metric:* net median and net % positive. *Threshold (`research-defined`):* if at a **10 bp/month round-trip + observed borrow** the Standard median net is **≥ 3 bp/month with ≥ 60% of anomalies positive**, the "even minimal costs would eliminate" claim fails at that cost level; at ≥ 20 bp/month round trip the claim should hold (median ≤ 0). *Action:* if the claim fails, the record's practical reading flips from "no menu" to "menu exists under low costs".
7. **Era-split robustness (attacks the time mechanism)** — *Metric:* median post-2005 return with the split moved to **2001-12** and **2010-12**. *Threshold:* if the pre/post gap shrinks to **< 30%** of the reported ~60% reduction under either alternative split, the "trading-tech + publication decay" era mechanism is judged **split-date-driven**. *Action:* reframe mechanism as data-window artefact.
8. **Universe-cut monotonicity (attacks the size mechanism)** — *Metric:* median return across the Figure 2 cutoff path (N500→All). *Threshold:* if the monotonic rise toward small caps is **not monotone** (any adjacent inversion > 2 bp) or the all-stock vs top-90% gap is **< 5 bp** post-2005, the "returns live in micro-caps" mechanism fails. *Action:* retain only the era mechanism.
9. **Out-of-window holdout (the paper's own open challenge)** — *Metric:* post-draft-date data (any months after the paper's sample end once identified) in the Standard universe. *Threshold:* if the holdout median **≥ 15 bp/month gross** and **≥ 5 bp net (10 bp round trip + borrow)**, the "useless in the 21st century" claim is falsified forward. *Action:* promote a successor record with the revived menu; this record is superseded.
10. **Alternative-implementation rescue test (source-declared boundary)** — *Metric:* vol-managed (Moreira–Muir style) or ML-combined versions of the same 170 portfolios in the Standard universe, walk-forward. *Threshold (`research-defined`):* net median **≥ 20 bp/month** after 10 bp round trip on genuinely out-of-sample folds ⇒ **falsifies the paper's practical conclusion** ("not much"), exactly as the source anticipates. *Action:* write a new positive record citing this one as the baseline it beat.

**Common rules (`research-defined`):** every test uses a held-out tail or walk-forward split; **no test may be rescued by unconstrained retuning** — a failed threshold stands; if the required data cannot be obtained (dataset release unpinned, sample end unknown), the affected test is reported as **not run**, never as passed. **On any failure, the record keeps `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`.**

## Crypto portability

**`unproven`.** The source contains **zero** crypto evidence: no crypto universe, no perpetual/spot/funding arm, no cross-market check of any kind (§II data = CRSP equities via Chen–Zimmermann only). This is a **ported question, not crypto empirical evidence** — we do not label it `direct` (source does not demonstrate the mechanism in crypto) and not `adapted` (the source performs no crypto adaptation).

Why a straight port is *not* merely mechanical:

- **Signal construction dependency:** most of the 200+ predictors are **accounting/financial-statement characteristics** (profitability, accruals, financing, investment/growth, operating leverage). Crypto issuers generally have no comparable standardised accounting, so the profitability/financing survivors — the very ones carrying the residual return — **have no direct crypto analogue**; only price/volume-derived members (momentum, seasonal momentum, volatility spread, liquidity/trading) transfer.
- **The mechanism being tested is size/liquidity frictions:** the paper's size story is about **micro-cap equity** (wide spreads, low institutional ownership, low analyst coverage, shorting difficulty). Crypto's "micro-cap" is defined by listing status, venue depth and delisting risk instead; the **same monotonicity claim must be re-established, not assumed**.
- **Venue/market-type differences:** spot vs perpetual, **funding** flows that equities do not have, 24/7 sessions with no close/auction, **exchange fragmentation** (which venue's cap/liquidity screen?), mark/index price conventions, and contract listing/survivorship that can silently rebuild the universe.
- **Shorting mechanics:** equity short-leg conclusions depend on borrow availability/fees; crypto perp shorts instead pay **funding** and face **squeeze/liquidation** risk — the cost structure flips sign unpredictably, so the paper's "even minimal costs would eliminate it" cannot be carried over even in direction.
- **Timestamp/candle boundaries:** monthly CRSP-style returns have no clean equivalent in 24/7 markets; month-boundary effects (weekend/quarterly settlement, index rebalances) need an explicit convention → `research-proposed` if ever operationalised.

**Portability verdict for the pool:** any crypto-analogue record must be built and tested on its own (perpetual cross-sectional factors, funding-inclusive net returns, documented venue screen); this record must not be cited as crypto evidence.

## Limitations

- **data gap** — end date of the post-2005 sample is never stated; the analysis vintage is only bracketed by the two conflicting draft-date lines (PDF "July 8, 2026" vs HTML "August 24, 2026").
- **data gap** — the Chen–Zimmermann dataset release/vintage used by the authors is not pinned, and the Scout did not fetch the dataset; `openassetpricing.com` contents are unverified here.
- **data gap** — no cost, spread, slippage, impact, borrow, fill, latency or capacity model computed for the paper's own gross numbers; net-cost statements are quoted from Chen & Velikov (2023) (secondary-within-primary, not independently opened).
- **underspecified** — t-statistic estimation method (no HAC/Newey-West, no deflated Sharpe, no multiple-testing correction described); per-anomaly characteristic definitions (live in dataset code); order type, execution timing and fill assumptions; timezone/session conventions.
- **underspecified** — Table/Figure cell values are only partially machine-checkable from prose; all numbers recorded here were read out of the **PDF** tables/figures/captions (Table 1–3, Figure 1–3) rather than from prose alone.
- **not independently reproduced** — no re-run, no re-estimation, no dataset retrieval this run.
- **unproven** — crypto portability; forward (post-sample) persistence of the post-2005 collapse; the claim under alternative implementations (timing / vol-managed / ML combinations), which the source explicitly excludes.
- **internal inconsistencies recorded, not repaired** — mean-vs-median labelling of `0.45` (Table 1 median vs Appendix "mean" vs Figure 1 mean `+0.48`); the 6 bp vs 13 bp survivor depending on shrinkage target; N varies 204/170/194/170/161 across filters with "approximate" category counts in Table 3; Momentum category shows median `0.05` while the prose calls momentum "essentially dead" (mean `0.01`, % pos `53`).
- **publication status** — preprint only: "Target: Financial Analysts Journal", no journal reference/DOI; peer-review outcome unknown.
- **scope limit stated by the source** — the conclusion covers "standard published anomalies, implemented as described in their original papers"; it is not a claim about all quant strategies.
- **research interpretation label** — points 6–15 under Negative evidence and all mechanism wording in Research interpretation are the Scout's analysis, not the source's claims.

## Implementation status

`implementation_status: not-implemented`. **Nothing has been implemented in our research stack.** No signal was coded, no dataset was downloaded, no backtest was run, no Wiki Brain page was written, no candidate-pool entry was produced, and no Qlib / Paper / Testnet / Live stage was touched. This artifact is a normalized capture of a public preprint, for Research Intake Review only. The record itself is a *population-level hypothesis*; implementing any individual anomaly from the Chen–Zimmermann menu would be a separate, separately-reviewed decision.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record in the staging repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered `/results/_handoff/candidates.json`; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. No wording, evidence count, confidence value or schedule implies promotion.

## Related Wiki records

Pre-write search of Hermes Wiki Brain on 2026-09-23 found **no related records**: queries `anomaly zoo published factor post-publication decay` and `open source asset pricing Chen Zimmermann quality profitability anomaly` both returned **0 results**. No Wiki-style links are asserted here (fabricating them is prohibited). The retrieval hook for future synthesis is therefore left explicit: this record should be re-checked against any later Wiki page on factor-zoo replication, post-publication decay, empirical-Bayes selection adjustment, or investability/universe screens — and against the staging-pool neighbours named under Provenance.

## Sources

1. Andrew Y. Chen, Ivo Welch — *"What Useful Alphas?"*, **arXiv:2607.06502v1 [q-fin.GN]**, submitted 2026-07-07, CC BY 4.0 — abstract: `https://arxiv.org/abs/2607.06502` (39,071 bytes, SHA-256 `9ce20e1cef2b467b025dbb0b574e844903b1cd5620e420ca4c2e8c676287db92`, read 2026-09-23).
2. **Canonical pinned PDF (primary artifact for every number in this record):** `https://arxiv.org/pdf/2607.06502v1` — 24 pages, 427,439 bytes, SHA-256 `968f0d62fb24aaea41919f036bf958d13364e4d656b23e8480f87c4518309b4b`, title page "Draft: July 8, 2026", PDF metadata `/arXivID` = `https://arxiv.org/abs/2607.06502v1`.
3. **HTML rendering of the same v1 (second copy, read in full):** `https://arxiv.org/html/2607.06502v1` — 85,464 bytes, SHA-256 `e23f3cb1194f719b2fcc7ac0ec06cbe50f59c976688eb824e5921209d466084d`, line "Draft: August 24, 2026" (differs from the PDF — see Provenance).
4. Underlying data source named and required by the paper: Chen, A. Y. and T. Zimmermann (2022), *"Open source cross-sectional asset pricing"*, Critical Finance Review 11, 207–264 — `https://www.openassetpricing.com` (**not fetched this run → data gap**).
5. Cost figures quoted **inside** source §V and attributed there to Chen, A. Y. and M. Velikov (2023), *"Zeroing in on the expected returns of anomalies"*, Journal of Financial and Quantitative Analysis 58(3), 968–1004 — **secondary-within-primary; the Scout did not open this paper**, so those five numbers remain source-quoted, not independently verified.
6. Other works cited **by the source** for context only (not read by the Scout): Efron (2010); Chen & Dim (2023); McLean & Pontiff (2016); Chen & Zimmermann (2020); Chen (2021); Chordia et al. (2014); Jegadeesh & Titman (1993); Daniel & Moskowitz (2016); Novy-Marx (2011, 2013); Ball et al. (2016); Bali & Hovakimian (2009); Heston & Sadka (2008); Bradshaw, Richardson & Sloan (2006); Chan, Lakonishok & Sougiannis (2001); Asquith, Pathak & Ritter (2005); Haddad, Kozak & Santosh (2020); Moreira & Muir (2017); Gu, Kelly & Xiu (2020); Freyberger, Neuhierl & Weber (2020); Goetzmann et al. (2007); Welch (2026), *"Assessing Factors and the CAPM in 2026"*, Working Paper.
