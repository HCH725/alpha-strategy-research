---
schema: strategy-research-record-v1
title: "R&D intensity long-only top-20 S&P 500 portfolio (RD20) and the HML_RD characteristic premium - SSRN 6002295, July-June formation, Novy-Marx-Velikov calibrated costs"
created: 2026-09-28
updated: 2026-09-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - us-equity
  - cross-sectional
  - factor
  - intangible-investment
  - transaction-costs
status: research-only
confidence: medium
source_as_of: 2026-01-01
sources:
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6002295
  - https://doi.org/10.2139/ssrn.6002295
  - https://github.com/vastdreams/fse-rnd-alpha/tree/2ce1514f418bb314e201e751c4a06279b34e6288/paper_latex/data/publication_snapshot.json
  - https://research.finsoeasy.com/rnd-alpha-paper.pdf
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "JEL codes: SSRN landing prints G11, G12, G14, O32 while the PDF first page prints JEL: G11; G12; M41 - unreconciled."
  - "Reference/citation counts: the SSRN landing shows a heading '0 References' and a heading '0 Citations' while the same landing's paper-statistics block links '1 Citations' and the PDF body prints 31 numbered reference entries - unreconciled."
  - "Sharpe ratio: PDF Section 9.2 states an annualized Sharpe ratio of approximately 1.00 (mean return 17.5%, volatility 17.6%) while the pinned publication snapshot reports investable_backtest.portfolio_performance.sharpe_ratio = 0.821 and portfolio_performance_net.sharpe_ratio = 0.820; the PDF's own 17.48/17.55 = 0.996 is a mean-over-volatility ratio, not the excess-return Sharpe the PDF defines in Appendix A.5 - unreconciled."
  - "Factor-model coverage: the PDF conclusion claims positive alphas 'across CAPM, FF3, FF5, and FF5+Momentum models' while Table 11 prints only FF3, FF3_MOM, FF5 and FF5_MOM, the pinned snapshot contains zero occurrences of the string 'CAPM', and the FF3 alpha is insignificant (p = 0.2314) - unreconciled."
  - "Fama-MacBeth: the PDF Section 8.1 and Section 12 state that monthly Fama-MacBeth regressions 'confirm' or 'corroborate' the relationship while the pinned snapshot sets fama_macbeth_monthly.rd_predicts_returns = false and its own interpretation string reads 'not significantly associated with next-month returns' (p = 0.0737) - unreconciled."
  - "Size scope: the PDF Section 7.4 and Section 12 state the premium exists within size categories including large caps while the pinned snapshot sets double_sort_analysis.key_findings.rd_works_in_large_caps = false (Large spread 2.61%, p = 0.0684) - unreconciled, and RD20 is a large-cap-only strategy."
  - "Delisting treatment: the PDF Section 3.2 and Section 7.5 state Tier-1 has no CRSP-grade delisting returns and uses cash-after-exit plus a simulated sensitivity, while the pinned snapshot's double_sort_analysis.methodology_notes.survivorship_correction reads 'Delisting returns integrated' - unreconciled."
  - "Mechanism claim: the PDF Section 8.4 states 'We do not claim to distinguish these mechanisms definitively' while the pinned snapshot sets mispricing_tests.interpretation.likely_explanation = 'MISPRICING' with confidence 'High' - unreconciled."
  - "Sector neutrality: the PDF Section 12 lists 'survives sector-neutral construction' as a primary finding while Section 6 of the same PDF states the sector-neutral HML_RD is substantially smaller and not statistically significant (1.04%, t = 0.92, p = 0.3636) - unreconciled."
  - "Version/date expressions: the PDF title block prints 'January 1, 2026 - Version 1.0', the PDF citation block prints 'Sehgal, A. (2026)', the SSRN landing prints 'Date Written: January 01, 2026' and 'Posted: 23 Jan 2026' - all preserved, unreconciled."
---

# R&D intensity long-only top-20 S&P 500 portfolio (RD20) and the HML_RD characteristic premium

## Provenance

Primary source (identity of every claim in this record):

- SSRN landing: `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6002295`, DOI `10.2139/ssrn.6002295`.
- Title exactly as printed on the SSRN landing and on the PDF title block: **"R&D Alpha: Investment Intensity and Long-Term Stock Returns"** (identical in both places; no title variant).
- Author: **Abhishek Sehgal**, sole author, ORCID `0009-0000-9424-4695`, affiliation printed on the PDF as `FSE Research & Investments Pty Ltd`, web `research.finsoeasy.com`; PDF footnote gives ABN 35 688 556 747, 50 Murray St, Pyrmont, Sydney, NSW 2009, Australia, and states the research is supported by Eye Dream Pty Ltd trading as Finsoeasy (ABN 95 650 714 060). The SSRN landing lists the single affiliation `FSE Research & Investments Pty Ltd`. No co-authors in either place.
- Version/date: PDF title block `January 1, 2026 - Version 1.0`; SSRN landing `Date Written: January 01, 2026` and `Posted: 23 Jan 2026`.
- Publication status: **working paper on SSRN, not stated to be peer reviewed.** The landing shows no journal and no peer-review statement; the PDF BibTeX block declares `type = {Working Paper}`.
- Landing statistics read in a browser session on **2026-09-28** after the Cloudflare interstitial cleared: `36 Pages`, `Posted: 23 Jan 2026`, `449` downloads, `1,903` abstract views, heading `0 References`, heading `0 Citations` with a separate paper-statistics link reading `1 Citations`, license `The copyright holder has granted SSRN a license. All rights reserved. No reuse allowed without permission.`, JEL `G11, G12, G14, O32`. Disclosure printed on the landing: the author is the founder of FSE Research & Investments Pty Ltd, which funded the research; the author does not actively manage investments for third parties.
- Pinned PDF: retrieved **2026-09-28** through the landing's `Open PDF in Browser` delivery link; **540,997 bytes**, **36 pages**, **SHA-256 `7ec0754a352969f5ac560d7916944caca9bb057cb410f8bdf6c5b3cd57017150`**; text-extracted page by page with `pypdf 6.16.2` to **86,645 characters** and all 36 pages read (Sections 1-12, Appendices A-D, References [1]-[31], Tables 1-18, Figures 1-5 captions). The presigned delivery URL is short-lived and deliberately not stored anywhere in this record.
- PDF first page prints `JEL: G11; G12; M41`, which differs from the landing (recorded in `contradictions`).
- Reproducibility hook named by the source (PDF Section 11 and Data Availability Statement): repository **`https://github.com/vastdreams/fse-rnd-alpha`**, pinned here at full commit SHA **`2ce1514f418bb314e201e751c4a06279b34e6288`** (HEAD as observed on 2026-09-28 via `git ls-remote`; commit author date `2026-07-15T13:01:12Z`), file path **`paper_latex/data/publication_snapshot.json`** (260,373 bytes at that commit).
- The snapshot at that commit carries `meta.id = 037ee52e-70f5-4bd5-9a27-ae1843740e4b`, `meta.built_at = 2026-01-01T22:58:38.210229`, `meta.data_tier = tier1`, `meta.return_convention = july_june`, `meta.git_commit = null`. This **matches the Snapshot ID printed on PDF page 2 and in Appendix B.3**, so the JSON at the pinned commit is the frozen artifact behind the PDF's numbers even though the repository HEAD commit postdates Version 1.0.
- The PDF also cites the author's own copy at `https://research.finsoeasy.com/rnd-alpha-paper.pdf`.
- Sample periods: HML_RD annual premium series **Jul1995-Jun1996 to Jul2024-Jun2025 (30 observations)**; investable RD20 backtest **Jul2001-Jun2025 (24 July-June periods, `N=24`)**; monthly Fama-MacBeth **1995-07-01 to 2025-06-01 (360 months)**; snapshot `investable_backtest.period = "2001-2024"`.
- Universe: **current S&P 500 constituents**, gated at each July 1 formation date by each ticker's reported S&P 500 "Date added" from the Wikipedia S&P 500 constituents list; historical removals are **not** tracked (removal spans tracked = 0 in Table 2).
- Data tier: Tier-1 fundamentals and prices from **Financial Modeling Prep (FMP)**; factors (MKT, SMB, HML, RMW, CMA, MOM) monthly from **Kenneth French's data library**; benchmark is an **SPY total-return proxy built from split-adjusted close plus separately ingested dividend cashflows**.
- Transaction-cost treatment (read at Methods level, PDF Section 9.2 Tables 17-18 and snapshot `transaction_costs` + `net_of_cost_returns`): costs are **modeled, not observed**. The PDF states a literature-calibrated turnover model citing **Novy-Marx and Velikov (2016), doi 10.1093/rfs/hhv063**, giving an annual trading cost of **0.027%** against realized turnover. Market impact is set to exactly `0.0` in the snapshot's cost model; bid-ask and commission appear only in the snapshot's separate 100-holdings cost block. There is **no** fill model, no latency, no participation cap, no borrow cost, and no slippage term anywhere in the paper or the snapshot. Taxes are explicitly not modeled.

Repository-wide source-identity dedup before writing (hidden-inclusive, `rg -uuu` across the whole checkout including `.mimo-worktrees/`, `.agents/`, `.hermes/`, `coverage_manifest.csv`, `_*.json`): `6002295`, `Sehgal`, `fse-rnd-alpha`, `finsoeasy`, `HML_RD`, `RD20`, `037ee52e`, `R&D intensity` and `R&amp;D intensity` all returned **zero matches** (a positive-control search for `novy-marx` in the same command returned matches, so the search was live). `git log --oneline -20` was consulted only as a convenience glance and does not by itself satisfy dedup.

## Economic mechanism

### Source-reported

The author's stated rationale (PDF Sections 1 and 2):

- Under U.S. GAAP, **SFAS 2 (1974), now ASC 730**, requires R&D expenditure to be expensed as incurred. Innovation-intensive firms therefore report lower contemporaneous earnings even when R&D creates economically valuable intangible assets.
- **Mispricing interpretation:** investors anchor on near-term earnings and underweight intangible investment, so prices adjust gradually as innovation outcomes arrive and patient high-R&D holders earn abnormal returns. Supporting citations named by the source include Lev and Sougiannis (1996), Chan, Lakonishok and Sougiannis (2001), Eberhart, Maxwell and Siddique (2004), Barth, Kasznik and McNichols (2001), Gu (2005), Cai, Cooper and He (2023).
- **Risk interpretation:** high-R&D firms carry uncertain payoffs, operating leverage and funding sensitivity, so a premium can be equilibrium compensation for innovation risk rather than mispricing; cited supports include Kothari, Laguerre and Leone (2002), Li (2011), Hirshleifer, Hsu and Li (2013).
- The source is explicit: **"The analysis is associational rather than causal"** and **"We do not claim to distinguish these mechanisms definitively"** (PDF Abstract and Section 8.4). The source does not assert that RD20 generates alpha independent of sector, size or beta.
- Source-reported hypotheses (PDF Section 2.5): H1 characteristic premium, H2 stability/regimes, H3 not just sector or standard factors, H4 implementability net of frictions.

### Research interpretation

- Hypothesized mechanism in falsifiable form: a **slow-moving accounting characteristic (R&D expense / revenue) forecasts the cross-section of large-cap equity returns** because the accounting treatment makes reported earnings a biased proxy for intangible capital formation, and the bias is only slowly corrected.
- Component roles, normalized:
  - Signal: prior-fiscal-year R&D expense divided by revenue.
  - Timing: Fama-French July-June formation to avoid filing-lag look-ahead.
  - Implementation layer: either (a) a within-universe Q5-minus-Q1 spread, or (b) a concentrated long-only top-20 equal-weight portfolio.
  - Friction layer: an annual, low-turnover rebalance, which the source treats as the binding implementation constraint rather than the signal.
- Competing explanations that the source does not eliminate, and that this record treats as live: **sector tilt** (Healthcare 22.23% and Technology 13.06% average intensity versus below 2% for most other sectors), **size tilt**, **zero-versus-nonzero R&D reporting** (see Negative evidence), and **beta/exposure to an equal-weight growth-tilted cohort**.
- Research interpretation of the source's own diagnostics: the pattern in Table 15 (premium 1.62% in large, 6.72% in medium, 8.59% in small; 1.02% low volatility versus 12.89% high volatility) is *consistent with* mispricing under costly arbitrage, but the same pattern is equally consistent with a lottery/vol loading, and the source's own liquidity proxies disagree with each other (Table 16).

## Signal

Everything in this section is source-reported unless explicitly marked `research-proposed` or `data gap`.

Two distinct objects are defined by the source, which must not be conflated (PDF Section 1.1):

- **HML_RD**: within-universe high-minus-low premium, Q5 minus Q1, from annual equal-count quintile sorts on R&D intensity.
- **RD20 strategy spread**: benchmark-relative excess return of an implementable long-only top-20 portfolio versus SPY, reported gross and net.

Formation and ranking (PDF Section 4.1, Section 9.1, Table 3, and snapshot `methodology_parameters`):

- **Signal definition:** `R&D intensity(i,t) = 100 * R&D expense(i,t) / Revenue(i,t)` using the **prior** fiscal year's value.
- **Formation timestamp:** portfolios formed **at the end of June / on July 1** each year; the source's own example timeline is fiscal year end Dec 2022, 10-K filings Feb-Mar 2023, formation July 2023, measurement July 2023 - June 2024. Exact clock time, order type and same-day versus next-day execution: **data gap** (not stated in source).
- **Universe gate:** current S&P 500 constituents, included only after their reported "Date added". Table 2: eligible count rises from 189 (Jul 2001) to 487 (Jul 2024); average 268.0 per formation year; min/max 120/487; union 487; addition spans tracked 375; **removal spans tracked 0**.
- **Filters (Table 3 and snapshot `methodology_parameters.filters`):** minimum revenue threshold **$100M**; R&D expense required non-negative; R&D intensity capped at **100%** by default and **200%** for high-R&D sectors; annual returns winsorized at the **1st and 99th percentile**; snapshot sanity constants `max_annual_return_decimal = 10.0`, `min_annual_return_decimal = -0.99`. Firms reporting **zero R&D are retained** and typically fall in Q1.
- **Quintiles:** 5 equal-count groups, equal-weight within each quintile (`weighting = equal_weight_within_quintile`), rebalance frequency annual.
- **RD20 selection:** sort the eligible universe at end of June by prior fiscal-year R&D intensity, **select the top 20**, weight **equal at 5% each**, hold **July through June (12 months)**, rebalance annually, sell names leaving the top 20 and buy names entering. Snapshot `investable_backtest.meta` confirms `n_holdings = 20`, `reconstitution = annual`, `selection_method = rd_alpha`, `return_convention = july_june`, `use_point_in_time = true`.
- **Exit handling (baseline A):** if a stock's price history ends mid-window, compute the holding-period return to the last observed trading day and treat cash as earning **0%** thereafter ("cash-after-exit"). Sensitivity B applies conservative delisting penalties of -0.3%, -0.6% and -1.0% per year (Table 14). This is explicitly **not** a CRSP `dlret` substitution.
- **Return construction (Tier-1):** split-adjusted closes plus separately ingested ex-dividend cashflows; daily return `(P(t) + D(t)) / P(t-1) - 1` on ex-dividend dates and `P(t)/P(t-1) - 1` otherwise, compounded within each July-June window. Tier-2 (CRSP-style total returns with authoritative delisting treatment) is described as "when available" and is **not used** in this snapshot.
- **Holding period / re-entry:** 12 months, annual, one reconstitution event per year.
- **Parameters:** all thresholds above are **fixed by the source** (snapshot parameters). Nothing in this section is research-proposed.
- **Reconstructability:** the signal is reconstructable **except** for (a) the tie-breaking rule among stocks with identical R&D intensity - **data gap**, and material, because the pinned snapshot shows average R&D intensity of exactly **0.0** for Q1, Q2 and Q3 in its 5-year quintile aggregates, so membership inside the bottom three quintiles is decided among ties by an unstated rule; (b) the minimum-revenue filter's interaction with ties; (c) the exact intra-day execution convention. Because of (a), the record marks the signal as **partially underspecified**, not fully reproducible.

## Required data

- **Instrument / universe:** U.S. listed common stocks currently in the S&P 500; point-in-time eligibility via reported index addition dates. Market type: cash equities (NYSE, AMEX, Nasdaq implied by the index).
- **Fundamentals:** annual income-statement **R&D expense** and **revenue**, with fiscal-year alignment and a public availability date that postdates the fiscal year end by at least the 10-K filing lag. Source vendor: Financial Modeling Prep (Tier-1).
- **Prices:** split-adjusted daily closes; separate **dividend event** series (cash amounts and ex-dates), because Tier-1 provides no vendor dividend-adjusted close.
- **Index membership:** S&P 500 "Date added" per ticker (source: Wikipedia list compiled from S&P Dow Jones Indices announcements); **historical removal dates are unavailable in this tier** and must be sourced elsewhere for an honest point-in-time rebuild.
- **Sector labels:** `sp500_companies.sector` **current GICS labels**; the snapshot explicitly notes "point-in-time sectors unavailable in Tier-1".
- **Factors:** Kenneth French monthly MKT-RF, SMB, HML, RMW, CMA, MOM, aligned to July-June windows; snapshot `ff_factors_status` reports annual 61 / monthly 748 rows, status `ok`.
- **Benchmark:** SPY total-return proxy from split-adjusted close plus dividend cashflows.
- **Point-in-time requirements:** filing-date-aware fundamentals, index addition dates, and - for a defensible rebuild - index removal dates and CRSP delisting returns, neither of which the source has.
- **Missing-data assumptions (source-reported):** zero R&D is treated as a legitimate value, not missing; cash-after-exit at 0% replaces missing terminal returns; a `data quality score (0-100)` averaging 49.2 is reported in Table 1 but its definition is **data gap** (not stated in source).
- **Not applicable to this signal:** funding, mark/index price, open interest, order book, trades/aggressor side, options surface - this is a cash-equity annual-rebalance signal.

## Execution assumptions

Source-reported:

- **Signal-to-order timing:** formation at end of June / July 1; the source does not state the execution session, order type, or whether trades occur at the June 30 close, the July 1 open, or spread over days. **data gap.**
- **Order type / fill model / latency / partial fills:** **data gap** - the words do not appear with any operational content in the PDF or the snapshot.
- **Fees and spread (snapshot `net_of_cost_returns.5yr.cost_methodology`, cost model `sp500_moderate`, source `Novy-Marx & Velikov (2016)`):** `bid_ask_cost_pct = 0.08`, `commission_cost_pct = 0.01`, `one_way_total_pct = 0.09`, `round_trip_total_pct = 0.181`, `market_impact_cost_pct = 0.0`, `annual_turnover_pct = 40.0`, `annual_trading_cost_pct = 0.072`, `n_holdings = 100`. This block describes the **100-holding quintile portfolios**, not RD20.
- **RD20 cost headline (PDF Table 17):** annual trading cost estimate **0.027%**, gross premium **7.55%**, net premium **7.52%**, premium capture **99.6%**, backtest Jul2001-Jun2025 (N=24).
- **RD20 realized turnover (snapshot `transaction_costs.turnover`, computed as `0.5 * sum |w_t - w_{t-1}|`, first year excluded):** average **14.6%**, maximum **25.0%**, per-year values 0.0% (2001) to 25.0% (2006, 2016). The PDF does not print this number; it is read from the pinned snapshot.
- **Cost sensitivity ladder (PDF Table 18, bp per 100% turnover -> annual cost / net premium / capture):** 5 -> 0.007% / 7.54% / 99.9%; 10 -> 0.015% / 7.54% / 99.8%; 25 -> 0.036% / 7.51% / 99.5%; 50 -> 0.073% / 7.48% / 99.0%.
- **Baseline cost rate:** the bp-per-100%-turnover rate that produces the headline **0.027%** is **never printed** in the PDF or the snapshot. **data gap.** (Research arithmetic, clearly labeled as such: 0.027% divided by the snapshot's 14.6% average turnover implies roughly 18.5 bp per 100% turnover, and the four Table 18 rows back-solve to roughly 14-15% turnover, consistent with the snapshot. This back-solve is **research-computed**, not source-reported.)
- **Slippage / impact / capacity:** market impact is **explicitly zero** in the cost model that is used; no spread, no latency, no participation cap, no ADV constraint anywhere. The PDF states only qualitatively that "Equal-weighted S&P 500 strategies have high capacity, but very large portfolios may face liquidity constraints." Capacity is **not quantified** - **data gap**, never treat as unconstrained or as zero.
- **Leverage / margin / borrow / shorting:** RD20 is long-only with no leverage stated. The HML_RD object is a long-short spread; its borrow cost and short feasibility are **not stated** - **data gap**.
- **Taxes:** explicitly not modeled (PDF Backtest Limitations).
- **Distinction:** every cost figure above is a **modeled** parameter from a published taxonomy, not an observed execution record. The result must not be described as tradable without further work.

## Evidence

### Source-reported

All figures below are third-party claims from the pinned SSRN PDF (page/table provenance given) and its pinned publication snapshot. Nothing here has been independently reproduced.

**Annual characteristic premium (PDF Table 5, descriptive, N = 30 July-June years):** mean **3.73%**, std. dev. **20.09%**, min **-45.80%**, max **76.21%**, positive years **17**, win rate **57%**, Newey-West t (lag = 1) **1.10**, Newey-West p **0.2793**. Cohen's d reported as **0.32** (PDF Section 4.2.3).

**Newey-West lag robustness (PDF Table 4):** lag 0 SE 3.6056, t 1.03, p 0.3098; lag 1 SE 3.3809, t 1.10, p 0.2793; lag 2 SE 2.7254, t 1.37, p 0.1819; lag 3 SE 2.5288, t 1.47, p 0.1512.

**Year-by-year extremes (PDF Table 6):** best **+76.21%** (Jul1999-Jun2000), worst **-45.80%** (Jul2000-Jun2001), then **-27.96%** (Jul2001-Jun2002); most recent year **-1.28%** (Jul2024-Jun2025).

**Monthly factor spanning (PDF Table 11; snapshot `spanning_tests_full`; monthly frequency, 360 months, Newey-West HAC lags 12, alpha annualized from monthly intercept x12):**

| Model | Alpha (%/yr) | SE | 95% CI | t | R2 | snapshot alpha_p | snapshot is_spanned |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FF3 | 2.07 | 1.72 | [-1.31, 5.45] | 1.20 | 0.493 | 0.2314 | true |
| FF3_MOM | 2.16 | 1.54 | [-0.87, 5.18] | 1.40 | 0.493 | 0.1626 | true |
| FF5 | 4.37 | 1.45 | [1.53, 7.21] | 3.01 | 0.564 | 0.00279 | false |
| FF5_MOM | 4.40 | 1.43 | [1.61, 7.19] | 3.09 | 0.564 | 0.00219 | false |

The PDF abstract and Section 8.1 summarize the same result as an **FF5 alpha of 4.37% per year, p < 0.01**, and the conclusion repeats it.

**Monthly Fama-MacBeth (PDF Table 12; snapshot `fama_macbeth_monthly`; 360 months 1995-07 to 2025-06, 100,644 firm-months, 279 firms/month, avg R2 0.0612):** R&D Intensity coefficient **0.01935**, t(FM) **1.57**, t(NW, lag 12) **1.794**, p(HAC) **0.0737**, p(FM) **0.1172**; Intercept 4.85405 (4.619 / 4.312); Log(Market Cap) **-0.15668** (-3.815 / -3.304); Book-to-Market -0.03085 (-0.163 / -0.174).

**Rolling-window descriptive spread (PDF Table 7 and snapshot `publication_stats`):** 5YR Q5 18.74% / Q1 13.37% / spread **5.37%**; 10YR 13.78% / 10.31% / **3.47%**; 20YR 11.79% / 10.13% / **1.66%**. ANOVA: 5yr F = 3.46, p = 0.010, eta-squared 0.093; 10yr F = 2.74, p = 0.032, eta-squared 0.084; 20yr F = 1.72, p = 0.15 (not significant). 5yr quintile means Q1 13.37, Q2 11.68, Q3 13.70, Q4 14.08, Q5 18.74.

**Regimes (PDF Table 8, Jul 2001 onward):** post-dot-com 2001-2002 Q1 7.2 / Q5 -1.3 / HML **-8.5** / win 50%; pre-GFC 2003-2007 15.1 / 11.9 / **-3.3** / 40%; financial crisis 2008-2009 -5.6 / -2.2 / **+3.4** / 100%; post-GFC 2010-2016 16.3 / 22.7 / **+6.4** / 71%; recent era 2017-2024 13.0 / 18.5 / **+5.5** / 50%.

**Sector structure (PDF Table 9):** Healthcare 60 firms / 22.23% average intensity / $1619.9B R&D; Technology 83 / 13.06% / $2516.2B; Communication Services 21 / 3.87%; Consumer Cyclical 53 / 2.39%; Basic Materials 19 / 1.88%; Financial Services 70 / 1.77%; Industrials 74 / 1.72%; Real Estate 31 / 0.99%.

**Sector-neutral robustness (PDF Table 10):** N = 30, mean **1.04%**, std 6.93%, positive years 19, win rate 63%, NW t (lag 1) **0.92**, p **0.3636**.

**Size x R&D double sort (PDF Table 13; snapshot `double_sort_analysis`, 29 years, 8,259 observations):** Large 12.06 / 13.64 / 14.67, spread **2.61**, t **1.82**, p **0.0684**; Medium 11.67 / 13.69 / 15.27, spread **3.60**, t **2.44**, p **0.0148**; Small 12.71 / 14.81 / 18.56, spread **5.85**, t **3.51**, p **<0.001**.

**Delisting sensitivity (PDF Table 14):** baseline 3.73 / t 1.10 / p 0.2793; conservative -0.3%/yr 3.43 / 1.01 / 0.3191; moderate -0.6%/yr 3.13 / 0.93 / 0.3626; aggressive -1.0%/yr 2.73 / 0.81 / 0.4264.

**Arbitrage-cost proxies (PDF Table 15; snapshot `mispricing_tests`, 29 years):** Size Large 1.62 (n 2760), Medium 6.72 (2745), Small 8.59 (2754); Volatility Low 1.02 (2754), Medium 1.21 (2745), High 12.89 (2760). The snapshot additionally carries Coverage Low 10.65 / Medium 4.97 / High 0.95, which is **not printed in the PDF**, and notes that "Coverage is proxied by years_tracked (count of historical income statement years), not analyst coverage."

**Illiquidity moderation (PDF Table 16, premium in % per year, Jul2001-Jun2025, N = 24 years, NW lags 1):** Amihud Liquid 5.93% (t 2.49), Medium 1.06% (0.45), Illiquid 7.53% (2.69), Illiquid - Liquid 1.60% (0.45); dollar volume Liquid 6.03% (2.51), Medium 2.70% (1.19), Illiquid 5.47% (2.43), Illiquid - Liquid -0.56% (-0.17).

**Sample construction (PDF Tables 1-2):** 503 unique tickers in cohort; eligible with 5-year window coverage 202, 10-year 171, 20-year 123; average R&D intensity 5.92%; average data quality score 49.2; average constituents per formation year 268.0 (min 120 / max 487); union 487; addition spans tracked 375; removal spans tracked 0; membership source `wikipedia_sp500_list: 9112`.

**Investable RD20 (PDF Section 9.2-9.3):** gross premium **7.55%**, net **7.52%**, capture **99.6%**, annual trading cost **0.027%**; annualized Sharpe stated as **approximately 1.00 (mean return 17.5%, volatility 17.6%)**; maximum drawdown **23.3%**, occurring in 2008, stated as less severe than the S&P 500 drawdown in the same period. Snapshot `investable_backtest` performance blocks: `portfolio_performance.sharpe_ratio = 0.821`, `max_drawdown = -23.26`; `portfolio_performance_net.sharpe_ratio = 0.820`, `max_drawdown = -23.30`; `benchmark_performance.sharpe_ratio = 0.841` (equal-weight research cohort), `max_drawdown = -27.52`; `sp500_performance.sharpe_ratio = 0.432`, `max_drawdown = -36.74`.

**Snapshot yearly_data aggregates (24 July-June periods, research-computed arithmetic over the source-reported yearly series - label: research-computed, inputs source-reported):** portfolio return mean **17.478%**, sd **17.554%**, 4 negative years; portfolio return net mean **17.454%**, sd **17.551%**; SPY mean **9.705%**, sd **15.535%**; equal-weight cohort benchmark mean **16.919%**, sd **16.671%**; `excess_vs_sp500` mean **7.774%**, sd 8.300%, negative in **4 of 24** years; `excess_return` versus the equal-weight cohort mean **0.562%**, sd 11.051%, negative in **11 of 24** years. Terminal wealth over the 24 periods: gross portfolio **36.08**, net portfolio **35.90**, SPY proxy **7.19**; drawdown from the same annual series: portfolio **-23.3%**, SPY **-36.7%**.

### Independently reproduced

`not independently reproduced`

No backtest, no simulation, no data download of fundamentals or prices, and no code execution from the authors' repository was performed for this record. The only actions taken were: reading the primary source PDF in full, reading the SSRN landing in a browser session, fetching the repository's published snapshot JSON at an immutable commit and reading values out of it, running read-only repository dedup searches, and running read-only Wiki Brain searches. Reading values out of the authors' own frozen snapshot verifies **transcription** of source-reported numbers; it is **not** independent reproduction of the result.

### Negative evidence

1. The headline annual premium is not statistically significant at conventional levels: mean 3.73%, Newey-West t = 1.10, p = 0.2793 over 30 years (PDF Table 5).
2. No Newey-West lag choice in 0-3 rescues significance; the best is t = 1.47, p = 0.1512 (PDF Table 4).
3. The win rate is 57% (17 of 30 years), i.e. close to a coin flip, and the standard deviation (20.09%) is more than five times the mean.
4. Sector-neutral construction collapses the premium to 1.04% with t = 0.92, p = 0.3636 (PDF Table 10), so most of the headline premium is between-sector (tech/health tilt) rather than within-sector stock selection.
5. The Fama-MacBeth R&D coefficient is significant only at the 10% level (p = 0.0737 HAC, p = 0.1172 FM), and the pinned snapshot sets `rd_predicts_returns = false`.
6. Factor spanning is model-dependent: FF3 alpha 2.07% (p = 0.2314) and FF3_MOM alpha 2.16% (p = 0.1626) are both insignificant; only FF5 and FF5_MOM clear 5%. The "distinct from standard factors" conclusion rests on a single model family.
7. The conclusion claims a CAPM spanning result, but Table 11 has no CAPM row and the pinned snapshot contains zero occurrences of `CAPM`.
8. The investable strategy is large-cap only, yet the source's own double sort finds the large-cap spread insignificant (2.61%, t = 1.82, p = 0.0684) and the snapshot hard-codes `rd_works_in_large_caps = false`.
9. The PDF's Sharpe claim of approximately 1.00 conflicts with the snapshot's 0.821 (0.820 net); the PDF's own inputs (17.48 / 17.55 = 0.996) are a mean-over-volatility ratio, not the excess-return Sharpe defined in its Appendix A.5.
10. RD20's Sharpe (0.821) is **lower** than its own equal-weight research-cohort benchmark's Sharpe (0.841) in the same snapshot.
11. Against the equal-weight cohort, RD20's mean annual excess is only **+0.56%** with sd 11.05% and is negative in **11 of 24** years (research-computed from snapshot `yearly_data`), so most of the 7.52% versus SPY is benchmark composition, not top-20 selection.
12. The 20-year rolling spread is 1.66% and its ANOVA is insignificant (F = 1.72, p = 0.15).
13. Regime dependence is severe: HML is -8.5% in 2001-2002 and -3.3% in 2003-2007, and the 2017-2024 win rate is only 50% (PDF Table 8).
14. The two worst years (-45.80% and -27.96%) both precede or coincide with the start of the investable backtest, so the 2001 start date truncates the premium's worst observed stretch while the 1995-2001 evidence remains in the descriptive series.
15. Delisting sensitivity never yields significance: the most adverse scenario gives 2.73%, t = 0.81, p = 0.4264 (PDF Table 14).
16. The universe is not point-in-time: only **current** S&P 500 constituents are in the panel, removal spans tracked = 0, and historical constituents that left the index are absent (PDF Table 2 footnote). This is survivorship by construction.
17. Exit handling is cash-after-exit at 0%, not CRSP delisting returns; the PDF states Tier-1 cannot substitute for `dlret`.
18. Sector labels are current GICS, not point-in-time (snapshot note on `annual_hml_premium_sector_neutral.methodology`), so the sector-neutral test itself inherits look-ahead on sector membership.
19. The quintile sort is dominated by zero-R&D firms: the snapshot's 5-year quintile aggregates show average R&D intensity of exactly **0.0** for Q1, Q2 and Q3, and `cohort_summary.by_rd_profile` shows Low 346 versus High 86 versus Medium 71 of 503 companies - so the sort is largely a zero-versus-nonzero split with an unstated tie-break inside the bottom three quintiles.
20. Quintile means are non-monotonic (5-year: Q1 13.37% **above** Q2 11.68%), so the monotonicity that H1 implies is not observed.
21. The pinned snapshot contains an **undocumented second premium series** (`factor_premiums` / `publication_stats.rd_factor_premium`: 31 annual observations labelled 1995-2025, mean **5.40%**, sd 12.41, t **2.424**, p **0.021589**, significant, 24 positive / 7 negative, min -24.15, max 33.33) whose quintile returns do not match PDF Table 6 and which the PDF never reports or defines. Significance of the R&D premium therefore flips depending on which of the two series in the same frozen artifact one reads.
22. Internal text conflicts inside the source artifact itself: the snapshot's `fama_macbeth_monthly.interpretation` says "not significantly associated with next-month returns" while the PDF conclusion says Fama-MacBeth "confirms"; `double_sort_analysis.methodology_notes.survivorship_correction` says "Delisting returns integrated" while the PDF says Tier-1 has no CRSP delisting; `mispricing_tests.interpretation.likely_explanation` asserts "MISPRICING" with confidence "High" while the PDF disclaims distinguishing mechanisms; `methodology_parameters.notes` says "primary inference uses annual non-overlapping HML series where available" while the PDF repeatedly states the annual series is descriptive and primary inference is monthly.
23. The frozen publication artifact contains an unhandled error value: `payload.backtest_window` is the string `{"error": "cannot access local variable 'JulyJuneReturn' where it is not associated with a value"}`, i.e. the deterministic build published a Python exception in place of a table.
24. Process and scope weaknesses that bear on all of the above: all costs are modeled with market impact set to exactly 0.0 and with no spread, latency, participation or fill model; taxes are unmodeled; there is **no holdout, no out-of-sample period and no train/test split** (the backtest window equals the analysis window); there is **no multiplicity control** across the many reported tests (4 NW lags, 4 spanning models, 3 size buckets, 3 volatility buckets, 5 regimes, 2 liquidity proxies, 3 delisting scenarios); it is a **sole-author working paper funded by the author's own firm**, the SSRN landing shows `0 References` and no peer-review statement, and the baseline cost rate behind the headline 0.027% is never printed.

## Falsification plan

All thresholds below are **research-defined falsification thresholds** unless the source itself states the number; all operational rules not present in the source are labeled `research-proposed`.

- **F1 - Frozen forward replication.** `research-proposed` rebuild of RD20 with point-in-time S&P 500 membership including removal dates, evaluated on the frozen forward window starting **2026-10-01** through the next full July-June cycle. **Fail** if forward net excess versus SPY is <= 0 (research-defined).
- **F2 - Number reproduction gate.** Independently rebuild Table 5 and Table 17 from an independent vendor. **Fail** the record's headline numbers if mean HML_RD differs from 3.73% by more than 0.50 percentage points, or the net premium differs from 7.52% by more than 0.50 pp (research-defined tolerance).
- **F3 - Point-in-time universe test.** Rebuild with the full historical S&P 500 membership ledger (additions **and** removals) plus CRSP delisting returns. **Fail** H3 if the premium falls by more than 50% of the reported value or loses significance at 5% (research-defined).
- **F4 - Sector-neutral gate.** Reproduce the within-sector equal-weight HML. **Fail** the "distinct signal" claim if the sector-neutral premium stays near 1.04% and remains insignificant at 5% (research-defined).
- **F5 - Within-large-cap gate.** Re-run the size x R&D double sort restricted to the actual RD20 eligibility set. **Fail** the investable premise if the large-cap spread remains insignificant at p >= 0.05 (research-defined).
- **F6 - Zero-R&D tie-break ablation (`research-proposed`).** Restrict the universe to firms with strictly positive R&D and pre-declare a deterministic tie-break (descending intensity, then ascending ticker). **Fail** if the premium vanishes, which would show the effect is a zero-versus-nonzero reporting artifact rather than an intensity gradient.
- **F7 - Timing-convention test.** Recompute the premium under (a) July-June, (b) calendar-year and (c) fiscal-year-aligned formation, pre-registered. **Fail** if significance appears under only one convention, since that indicates specification search rather than a robust signal (research-defined). This directly probes the undocumented second series found in the snapshot (Negative evidence 21).
- **F8 - Sharpe-definition audit.** Recompute RD20's Sharpe from the published yearly returns with a stated risk-free series. **Fail** if the reported approximately 1.00 cannot be reproduced under the definition printed in the source's own Appendix A.5 (research-defined).
- **F9 - Benchmark decomposition.** Test RD20 against the equal-weight eligible-universe cohort. **Fail** the alpha claim if mean annual excess <= 0 or |t| < 1.96 (research-defined), because the headline 7.52% is versus SPY.
- **F10 - Cost ladder.** `research-proposed` ladder of 0 / 25 / 50 / 75 / 100 bp per 100% turnover applied to the 14.6% realized turnover. **Fail** H4 if net excess versus SPY goes <= 0 at any rung at or below 50 bp (research-defined), and in all cases report the unprinted baseline rate as a gap.
- **F11 - Capacity / liquidity audit.** Compute the ADV participation required to rotate the 20-name book at each historical rebalance. **Fail** if any name requires more than 10% of its 20-day ADV in a single session (research-defined).
- **F12 - Multiplicity control.** Apply Benjamini-Hochberg at q < 0.10 across the full reported test family (4 NW lags, 4 spanning models, 3 size buckets, 3 volatility buckets, 5 regimes, 2 liquidity proxies, 3 delisting scenarios). **Fail** H3 if the FF5 spanning alpha does not survive (research-defined).
- **F13 - Subperiod stability.** Split Jul2001-Jun2013 and Jul2013-Jun2025. **Fail** if the sign of the RD20 excess differs between halves (research-defined).
- **F14 - Placebo.** Draw 1,000 random 20-stock portfolios from the same eligible universe, matched on sector counts and size decile, and compute their equal-weight excess versus the cohort. **Fail** if RD20's mean excess does not exceed the 95th percentile of the placebo distribution (research-defined).

Action on failure: the record stays `research-only`, `not-implemented`, `not-approved`; a failed F2, F4, F5, F6, F9 or F12 should be reported back to Research Intake Review as grounds for REJECT rather than for retuning.

## Crypto portability

**Not applicable** for the literal signal.

- The signal variable - R&D expense divided by revenue under U.S. GAAP / ASC 730 - does not exist in crypto markets. There is no filing regime, no R&D expense line, no revenue denominator comparable across protocols, and no S&P 500-like survivorship-curated large-cap universe. The source itself tests **only** U.S. large-cap cash equities and makes no crypto claim.
- A crypto analogue would have to be `research-proposed` and would be **unproven**: for example core-developer or treasury "R&D" burn per unit of protocol revenue or per unit of float, ranked across a point-in-time token universe. Every hard problem is worse in crypto than in the source setting: 24/7 sessions versus a July-June annual cycle, point-in-time token universes with severe listing survivorship, no audited standardized expense accounting, wash-traded "revenue", venue fragmentation, and no equivalent of index membership gating.
- Other crypto-specific risks if anyone attempted a port: funding and mark-price mechanics do not apply to spot-style annual holds but do apply to any perpetual-based implementation; token unlocks and vesting create forced supply flows with no equity analogue; custody and withdrawal risk is absent from the source; liquidity and market impact for a concentrated 20-name book are far worse in long-tail tokens than in S&P 500 names.
- Crypto portability is **not** authorization to trade.

## Limitations

- **Source quality:** sole-author SSRN working paper, funded by the author's own firm, no journal and no peer-review statement on the landing, `0 References` shown on the landing while the PDF prints 31 references. Treat every performance figure as an unrefereed third-party claim.
- **Primary inference is mixed:** the paper's own annual premium is insignificant (p = 0.2793) and it anchors significance instead on monthly spanning and Fama-MacBeth; the Fama-MacBeth result clears only 10%, and the snapshot flags it as non-predictive.
- **Not point-in-time:** current-constituents-only membership with zero removal spans tracked; current GICS labels; Wikipedia-sourced addition dates. `data gap`.
- **Delisting and exit modeling:** cash-after-exit at 0% with a simulated penalty ladder, not CRSP `dlret`. `data gap`.
- **Tie-breaking inside the quintiles is unspecified and material** given that Q1-Q3 average intensity is exactly 0.0. `underspecified`.
- **Execution is unspecified:** no order type, session, latency, fill model, participation cap or slippage. `data gap`. The word "tradable" is not supported by this source.
- **Costs are modeled, not observed;** market impact is set to exactly 0.0; the baseline cost rate behind 0.027% is never printed. `data gap`.
- **Benchmark choice does a lot of work:** the headline 7.52% is versus SPY; versus the equal-weight eligible cohort the same snapshot shows +0.56% mean annual excess and a lower Sharpe than the cohort.
- **Undocumented second premium series** in the frozen snapshot (mean 5.40%, t = 2.424, p = 0.0216) that the PDF never reports or defines. `underspecified`.
- **A published error value** sits in `payload.backtest_window` of the frozen snapshot, which weakens the "every numeric claim can be verified against the source data" reproducibility claim. `data gap`.
- **No holdout, no out-of-sample period, no multiplicity control, no capacity quantification.**
- **Scope:** U.S. large-cap only; small-cap and international explicitly out of scope per the source's own limitations.
- **Contested:** this record carries `contested: true` with ten frontmatter contradictions; none has been reconciled and none should be silently resolved downstream.
- **Not independently reproduced.**
- **Incremental-write check:** no existing record in this repository shares this source identity (hidden-inclusive `rg -uuu` returned zero hits for `6002295`, `Sehgal`, `fse-rnd-alpha`, `HML_RD`, `RD20`, `037ee52e`); Wiki Brain `kb_search` returned zero pages for R&D intensity / intangible premium.

## Implementation status

`implementation_status: not-implemented`.

Nothing has been implemented in our research stack. No R&D-intensity data has been ingested, no portfolio constructed, no backtest run, no Qlib full-backtest executed, and no Paper, Testnet or Live workflow touched. This document is a normalized research capture of a third-party working paper plus a reading of its frozen publication snapshot. The specific numbers above are source-reported claims with table-level provenance, not our results.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this record in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. It also does not mean the source's internal contradictions have been reconciled, or that the source's Sharpe, significance or cost claims survive independent replication. Any later adoption or implementation decision must be explicit, separately reviewed, and based on this record plus current sources.

## Related Wiki records

Verified adjacent pages (found via read-only `kb_search`, none shares this source identity):

- [[quant/sec-form4-microcap-insider-purchases-gradient-boosting-momentum-2026-09-05]] - adjacent in that both are point-in-time fundamental/event signals in U.S. equities; differs in universe (microcap versus S&P 500), mechanism (disclosure-driven momentum versus accounting-expensing characteristic) and horizon.
- [[quant/sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13]] - adjacent in that both depend on S&P 500 membership mechanics; differs in mechanism (scheduled index-flow event study versus annual characteristic sort) and in the point-in-time membership requirement that this record lacks.
- [[quant/crypto-cross-sectional-factor-zoo-iterative-alpha-compression-2026-09-01]] - adjacent in that both are cross-sectional factor claims; differs in market type and in source identity.

No Wiki Brain page for this mechanism exists yet; a search for R&D intensity / intangible premium returned zero pages.

Nearest records in this repository (source identity and mechanism differ on every axis; none is a duplicate):

- `published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23.md` - cites Chan, Lakonishok and Sougiannis (2001) as one row of an anomaly zoo; different source (arXiv 2607.06502), different mechanism (zoo-level luck adjustment), different claim.
- `wealth-creation-profitability-investment-interaction-double-sort-factor-2026-09-26.md` - different source (Financial Analysts Journal, DOI 10.1080/0015198X.2026.2683330), different signal (profitability x investment interaction term), different construction (3x3 value-weighted long-short).
- `moving-average-distance-cross-sectional-anchoring-us-equity-ssrn-3111334-2026-09-26.md` - different source (SSRN 3111334), different mechanism (technical anchoring / momentum versus accounting characteristic).
- `directional-anomaly-zoo-net-cost-audit-quality-survivor-2026-09-23.md` - different source and different question (net-cost audit of a zoo rather than a single characteristic's implementability).

## Sources

1. Sehgal, A. (2026). *R&D Alpha: Investment Intensity and Long-Term Stock Returns* (Working Paper). FSE Research & Investments Pty Ltd. SSRN abstract 6002295, DOI `10.2139/ssrn.6002295`. Landing `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6002295`, read 2026-09-28; `Posted: 23 Jan 2026`, `Date Written: January 01, 2026`, `36 Pages`, 449 downloads, 1,903 abstract views, license "All rights reserved. No reuse allowed without permission."
2. Same paper, pinned PDF retrieved 2026-09-28 from the landing's delivery link: 540,997 bytes, 36 pages, SHA-256 `7ec0754a352969f5ac560d7916944caca9bb057cb410f8bdf6c5b3cd57017150`, text-extracted to 86,645 characters and read in full. Author's own copy cited in the PDF: `https://research.finsoeasy.com/rnd-alpha-paper.pdf`. The presigned delivery URL was not stored.
3. Reproducibility repository named by the source: `https://github.com/vastdreams/fse-rnd-alpha`, pinned at full commit SHA `2ce1514f418bb314e201e751c4a06279b34e6288` (observed 2026-09-28 via `git ls-remote`, commit author date 2026-07-15T13:01:12Z), path `paper_latex/data/publication_snapshot.json` (260,373 bytes), snapshot ID `037ee52e-70f5-4bd5-9a27-ae1843740e4b`, built 2026-01-01T22:58:38.210229. All snapshot-derived values in this record were read from that file at that commit.
4. Cost model cited by the source for its transaction-cost calibration: Novy-Marx, R. and Velikov, M. (2016), "A Taxonomy of Anomalies and Their Trading Costs", *The Review of Financial Studies* 29(1):104-147, DOI `10.1093/rfs/hhv063` (cited as reference [4] in the source; cited here only as the source's declared cost basis, not as an independent read).
5. Underlying data vendors named by the source: Financial Modeling Prep (Tier-1 fundamentals and prices), Kenneth French data library (monthly factors), Wikipedia S&P 500 constituents list for "Date added" membership gating.

No Wiki Brain write, no Kanban task, no backtest, no implementation; hard cap 1 record.
