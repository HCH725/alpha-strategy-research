---
schema: strategy-research-record-v1
title: "Boundaries of Time-Series Momentum: conditioning equity time-series momentum on a term-spread-plus-valuation extreme (Financial Management, DOI 10.1111/fima.70055)"
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - time-series-momentum
  - regime-filter
  - equity-market-timing
  - valuation-extremes
  - journal-article
status: research-only
confidence: medium
source_as_of: 2026-07-06
sources:
  - "PRIMARY SOURCE (pinned 2026-09-29): https://onlinelibrary.wiley.com/doi/full/10.1111/fima.70055 — Wiley Online Library Version of Record, opened in a browser session and read end to end. Page title 'Boundaries of Time‐Series Momentum - Suominen - Financial Management - Wiley Online Library'. Printed masthead: journal 'Financial Management'; labels 'ORIGINAL ARTICLE' and 'Open Access'; authors line 'Matti Suominen, Erik Hjalmarsson'; 'First published: 06 July 2026 https://doi.org/10.1111/fima.70055'; footer label 'Early View — Online Version of Record before inclusion in an issue'. Pinned text = document.body.innerText, 105,970 characters / 108,097 bytes over 757 lines, SHA-256 94abc96ea27c2b7d3aa7ff79078ba5be50794a2d7ea54a9ac9ec3ea59a340c1f; document.documentElement.innerHTML length 1,712,580 characters. Covers Abstract, Sections 1-8, body Tables 1-12 (all notes), Figures 1-2, Endnotes 1-17, Acknowledgments, Appendix A1-A4 with Tables A1-A6 and Figures A1-A2. The reference-list container is present but empty in the DOM, so the bibliography entry count is a data gap."
  - "https://doi.org/10.1111/fima.70055 — DOI printed in the masthead and in citation_doi / dc.identifier / publication_doi meta tags. citation_issn 1755-053X; citation_journal_title 'Financial Management'; citation_publisher 'John Wiley & Sons, Ltd'; citation_online_date 2026/07/06; citation_keywords 'business cycle', 'equity market returns', 'time-series momentum'; citation_author order ['Matti Suominen','Erik Hjalmarsson']; citation_author_institution ['School of Business Aalto University Aalto Finland','University of Gothenburg Gothenburg Sweden']."
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6867878 (SSRN-issued DOI 10.2139/ssrn.6867878) — earlier working-paper version of the same study, identified but NOT opened in this run, so its posted/revised dates, page count, citation counts and licence are all `data gap`. The pinned primary for every number below is the Wiley Version of Record, never the SSRN version."
  - "https://onlinelibrary.wiley.com/doi/pdf/10.1111/fima.70055 (PDF) — attempted, not obtained: direct curl returned HTTP 403 behind a Cloudflare interstitial and an in-session fetch returned HTML rather than PDF bytes, so PDF size, page count, PDF checksum and PDF metadata are `data gap`."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Table 8 note vs Section 5 text: the note reads 'Ninety percent of the observations with the lowest Average of the Boundaries variable are said to lie within the Boundaries, and the observations above the 10th percentile of the Average of the Boundaries variable are said to lie at the Boundaries', while Section 5 defines at-the-Boundaries states as 'when the average measure for Boundaries is above its 90th percentile'. Above the 10th percentile would place 90% of observations at the Boundaries; above the 90th percentile places 10%. Both sentences are printed in the pinned text and are mutually exclusive as written. Unreconciled."
  - "Section 1 states 'In our sample of US returns from 1927 to 2021, the findings are qualitatively similar', while Section 2, every table note and the abstract-era sample description use 'June 1927 to December 2024'. The 2021 endpoint appears nowhere else. Unreconciled."
  - "Table 3, columns (1)-(4): the 'Term spread' row prints strictly positive OLS estimates 0.07, 0.06, 0.09*, 0.07 with strictly negative Newey-West t-statistics (−1.91), (−1.33), (−2.25), (−1.65), while columns (5)-(8) print positive estimates 0.04, 0.03, 0.04, 0.06 with positive t-statistics (0.96), (0.86), (1.16), (1.51). The same row in Table 9 (identical specification, Hodrick standard errors, Section 7) prints estimates 0.08, 0.05, 0.10*, 0.07 with positive t-statistics 1.74, 1.09, 2.03, 1.37. A positive estimate cannot carry a negative t-statistic; verified against the raw DOM HTML, not an extraction artefact. Unreconciled."
  - "Table 11, 'Past 12m stock market absolute excess return' row: all ten OLS estimates are positive (0.13*, 0.12*, 0.08, 0.19, 0.07, 0.25, 0.16*, 0.35*, 0.16*, 0.41*) and all ten Hodrick t-statistics are negative ((−2.14), (−2.02), (−1.25), (−0.90), (−1.11), (−1.75), (−2.42), (−2.36), (−2.41), (−2.66)). The corresponding Table 5 row prints the same signs as its estimates. Verified against the raw DOM HTML. Unreconciled."
  - "Appendix A4 prose reads 'In Tables A4 and A5, we present examples of how our results might be used to improve investment strategies for time-series momentum ... in the last column of Tables A4 and A5 ... either in the 12,1 time-series momentum strategy (A4) or in our diversified index of time-series momentum strategies (A5)', but the printed table captions are 'TABLE A4. Kitchen sink model for time-series momentum', 'TABLE A5. Trading strategies for equity premium (Rm − Rf) 1968-2023' and 'TABLE A6. Trading strategy for a diversified portfolio of time-series momentum strategies (TSMOM) 1968-2023', and Section 7 separately assigns 'Tables A3 and A4' to the robustness tests. The prose numbering and the caption numbering cannot both be right. Unreconciled."
  - "Section 6 reads 'we include all 10 explanatory variables from Table 4 in the predictive regression (10-factor model)'. Table 4 is the five-column international forward-market-return regression and its note lists seven right-hand-side terms; the ten-specification table for TSMOM is Table 5. The cross-reference does not resolve in the published numbering. Unreconciled."
---

# Boundaries of Time-Series Momentum: conditioning equity time-series momentum on a term-spread-plus-valuation extreme (Financial Management, DOI 10.1111/fima.70055)

## Provenance

**Primary-source author(s), exactly as source.** Two authors, printed on the masthead as `Matti Suominen, Erik Hjalmarsson` and reproduced in that order by the page's `citation_author` meta tags. `citation_author_institution` gives **School of Business, Aalto University, Aalto, Finland** for Suominen and **University of Gothenburg, Gothenburg, Sweden** for Hjalmarsson. No ORCID, no author email, no corresponding-author marker, no author-affiliation block and no funding or conflict-of-interest statement appear anywhere in the pinned text or meta tags → all of those fields are `data gap`, never inferred. The Acknowledgments section contains exactly one sentence: `Open access publishing facilitated by Aalto-yliopisto, as part of the Wiley - FinELib agreement.`

**Paper title:** *Boundaries of Time-Series Momentum* (masthead and `citation_title`; the browser tab title uses the typographic form `Boundaries of Time‐Series Momentum`). Printed keywords: `business cycle`, `equity market returns`, `time-series momentum`.

**Version / date.** `First published: 06 July 2026`; `citation_online_date 2026/07/06`; journal footer `Early View — Online Version of Record before inclusion in an issue`. Received, accepted and revised dates are not printed → `data gap`. Volume, issue and page numbers are not printed because the article is still in Early View → `data gap`.

**Publication / preprint status:** peer-reviewed journal article published by John Wiley & Sons, Ltd in *Financial Management* (ISSN 1755-053X), labelled `ORIGINAL ARTICLE` and `Open Access`, available as an online Version of Record before issue assignment. The SSRN working-paper version (abstract id 6867878, DOI 10.2139/ssrn.6867878) is identified in `## Sources` but was **not opened this run**; its dates and page counts are `data gap`. Caution: a third-party newsletter summarising the SSRN version attributes the paper to `Matti Suominen` and `Sebastian Müller`, which contradicts the primary source's author list (the SSRN version was not opened, so whether its own author list differed is `data gap`); secondary summaries of this item were therefore not used for any fact recorded here.

**Retrieval path (2026-09-29).** A browser session opened the Wiley full-text URL and read it directly; `document.body.innerText` and `document.documentElement.innerHTML` were both captured. Direct `curl` to the PDF URL returned HTTP 403 (Cloudflare), and an in-session `fetch` of the same PDF URL returned HTML (43,551 bytes, SHA-256 `d4e6ae4daf1691c5a5d071cbda04e06615c25edcbc539c496fa5f3aae68baa81`) instead of PDF bytes, so the PDF is a `data gap`. The only stable identifiers stored here are the full-text URL and the DOI; no session-bound or expiring URL is recorded.

**Pinned primary-text integrity.** 108,097 bytes, 105,970 characters, 757 lines, SHA-256 `94abc96ea27c2b7d3aa7ff79078ba5be50794a2d7ea54a9ac9ec3ea59a340c1f`; 1,258 non-ASCII characters (typographic minus signs, en dashes, accented names). Read end to end for this record: Abstract; Sections 1-8 (Introduction; Data and the Definition of Boundaries; Equity Market Return Reversals Near Boundaries; Time-Series Momentum Returns and Boundaries; Valuation Ratios and the Business Cycle; Out-of-Sample Return Predictability; Robustness Tests; Conclusions); Tables 1-12 with every table note; Figures 1-2 captions; Endnotes 1-17; Acknowledgments; Appendix A1-A4 with Tables A1-A6 and Figures A1-A2. The reference-list container is empty in the DOM → reference count `data gap`.

**Sample period (source).** US: **June 1927 – December 2024** (Section 2; repeated in the notes to Tables 1, 2, 3, 5, 7, 9, 11, A1, A3, A4). Sub-samples: Table A3/A4 kitchen-sink columns run June 1937 – December 2024 and June 1949 – December 2024; Table 5 regressions use N = 1,135 / 1,040 / 920 months because of the 10- and 20-year normalisation windows. International: **January 1989 – December 2024**, unbalanced panel, **20 countries** with individual start dates printed in Endnote 7 (Australia Dec 1989, Austria Jul 1991, Belgium Nov 1989, Canada Feb 1992, Denmark Jan 1989, Finland May 1991, France Jan 1989, Germany Dec 1990, Ireland Jan 1989, Japan May 1993, Italy Dec 1995, Netherlands Jan 1989, New Zealand Dec 1989, Norway Jan 1989, Portugal Feb 1999, Spain Jan 1992, Sweden Apr 1991, Switzerland Jan 1989, UK Jan 1989, USA Jan 1989). Trading-strategy tables A5 and A6 run **June 1968 – December 2023** (the first 20 years train the expanding regression and one-year-ahead returns are needed).

**Universe (source).** US: the broad equity market index, the risk-free Treasury rate (Kenneth French's website), long-term government bond yields and bond excess returns (Ibbotson, computed as Ibbotson US long-term government bond total return minus Ibbotson US Treasury bill total return), macro series from FRED (industrial production, unemployment), Shiller's CAPE and dividend yield from Robert Shiller's website, and term spread defined as the long-term bond yield minus the annualized risk-free rate on Kenneth French's website. International: equity index returns and dividend yields per country from Datastream; bond data from Datastream Benchmark Government Bond indices at the **5-year maturity** (chosen over longer maturities for data availability); all national risk-free rates from Datastream. Point-in-time revision policy, publication lags and vendor-vintage handling are never discussed → `data gap`.

**Transaction-cost / execution treatment (source): `data gap`, never zero.** Determination was made at Methods level from Section 2 (Data and the Definition of Boundaries), Section 4 (strategy construction), Section 6 (out-of-sample), Section 7 (robustness) and Appendix A4 (Out-of-Sample Investment Strategies) — the sections that define the traded object — plus a word-boundary census of the pinned 105,970-character text:

| term | occurrences | what the single hit, if any, actually is |
|---|---|---|
| `transaction cost` / `transaction costs` | **0** / **0** | — |
| `slippage` | **0** | — |
| `commission` | **0** | — |
| `fee` / `fees` | **0** / **0** | — |
| `bid-ask` / `bid ask` | **0** / **0** | — |
| `market impact` | **0** | — |
| `impact` | **1** | Section 7, 'This change in return definition has only a very small impact on the resulting OLS estimates' — not an execution model |
| `spread` | **147** | every occurrence is inside `term spread` / `Term Spread`, i.e. the yield-curve slope; **zero** occurrences of a price or quoted spread |
| `latency` / `fill` / `maker` / `taker` / `order type` / `market order` / `limit order` / `execution` / `participation` / `turnover` / `capacity` / `leverage` / `margin` / `funding` | **0** in every case | — |
| `borrow` (exact word) | **0** | the phrase `borrowing at the risk-free rate` appears in the Table 1/5/6 notes as the financing convention for the long leg; no borrow cost, rebate or short-availability model |
| `walk-forward` / `placebo` / `Benjamini` / `FDR` / `multiple testing` / `deflated` | **0** in every case | — |
| `backtest` / `drawdown` / `CAGR` / `win rate` | **0** in every case | — |
| `out-of-sample` | **16** | Sections 6, 7, 8, Endnotes and Appendix A4 |
| `Sharpe ratio` / `sharpe` | **4** / **6** | Appendix A4 prose and Tables A5/A6 only |
| `crypto` / `bitcoin` / `perpetual` | **0** / **0** / **0** | — |

Consequence: **the paper states no cost, execution, financing or capacity model anywhere.** Whether the returns in Tables A5/A6 are gross or net is not stated → `data gap`, never assumed to be net and never asserted to be gross. Order type, fill model, signal-to-order delay, latency, index-short borrow or rebate, margin, liquidation, turnover, participation and capacity all remain `data gap`, never zero.

## Economic mechanism

### Source-reported

The authors state that Shiller's CAPE, the dividend yield and the government bond yield-curve slope are value measures in equity and bond markets, and that equity market time-series momentum "performs well in mid-valuation regimes, but breaks down near historical valuation extremes, where the direction of the equity market commonly turns" (Abstract). They show that historical extremes of these ratios form "boundaries" near which 12-month equity returns revert and near which time-series momentum stops working, and that the breakdown is symmetric — it holds whether valuations are extremely low or extremely high and whether equity momentum is positive or negative (Section 1). Their stated interpretation is macro: extreme valuation states are states in which both the economy and monetary policy are highly sensitive to past equity returns, so large equity moves trigger policy responses that induce reversals (Section 1; Section 5; Table 8); they offer this explicitly as "one interpretation", not an identified causal result. They state the practical use directly: knowing the boundaries "is important for investors in time-series momentum strategies, as it can improve their portfolio returns through better time-varying allocation to time-series momentum strategies and equity" (Section 1), and the Conclusions say the information is "relevant for investors who can use the information to better time their equity market exposure and exposure to time-series momentum strategies."

### Research interpretation

The hypothesis is a **regime-filtered trend-following claim**, not a new premium:

```text
Regime:          Boundaries = (scaled term spread)^2 + (scaled CAPE or scaled dividend yield)^2,
                 each component a 12-month moving average min-max normalised over the trailing
                 10-year (or 20-year) range into [-1, +1]; Boundaries in [0, 2], higher = nearer
                 a joint equity/bond valuation extreme.
Primary signal:  sign of the past 12-month equity-market excess return (Moskowitz-Ooi-Pedersen
                 style time-series momentum), evaluated over 25 lookback x holding combinations.
Confirmation:    (Appendix A4 only) an expanding-window predictive regression on Boundaries,
                 past 12-month excess return and their interaction, plus a normalised-CAPE gate.
Risk / exit:     rotate between the diversified TSMOM index and the market risk premium, or
                 between the equity risk premium and cash-like zero exposure, on the regime.
```

Falsifiable form: the mean 12-month return of the diversified TSMOM portfolio and the probability that a 12-month sign persists should both decline as Boundaries rises, and the coefficient on `past-12-month return x Boundaries` (or `past-12-month absolute return x Boundaries`) should be significantly negative. The mechanism claimed for the decline is policy/valuation-state sensitivity; that channel is a separate, weaker claim than the reduced-form conditioning result and must be tested separately (see F12). Do not assume every component contributes: the regime filter, the sign signal, the expanding-regression overlay and the CAPE gate are four distinct roles and require ablation (see F11).

## Signal

Everything in this section is **source-reported** unless explicitly tagged.

**Boundaries construction (Section 2, Equation 1).**
- Inputs: 12-month moving averages of the term spread, of Shiller's CAPE and of the dividend yield (Endnote 1 notes the CAPE moving average is a moving average of an inverse of a moving average and that using 12-month price / 10-year average earnings gives a correlation of 1.00 with it).
- Scaling: subtract the past 10-year (or 20-year) **minimum** of the series from the 12-month average, divide by the past 10-year (or 20-year) **range** (max − min) to obtain a value in [0, 1], then multiply by 2 and subtract 1 to obtain [−1, +1].
- Combination: `Boundaries = (scaled term spread)^2 + (scaled CAPE)^2` when CAPE is used, or `(scaled term spread)^2 + (scaled dividend yield)^2` when dividend yield is used. Maximum 2 (both components at opposite extremes), minimum 0 (both at mid-levels).
- `Average of the Boundaries` = the average of the four Boundaries measures used in Tables 3 and 5 (10-year CAPE, 10-year dividend yield, 20-year CAPE, 20-year dividend yield) — this is the quantity used in Section 6, Table 8 and Appendix A4.
- Endnote 2: an alternative boundary defined as the **sum of the absolute values** of the normalised components gives qualitatively similar results.
- **Signal formation / tradability timing is not stated**: no month-end versus month-average convention, no publication lag for CAPE or dividend yield, no statement of when the 12-month average becomes tradable → `data gap`.

**Time-series momentum construction (Section 4, Table 1 note).**
- Following Moskowitz, Ooi and Pedersen (2012): invest in the equity market index (borrowing at the risk-free rate) if the sign of the market excess return over the lookback period is positive; otherwise short the equity market and invest at the risk-free rate.
- The source uses **equivalent positions in the cash market** rather than futures, explicitly "to obtain longer data series".
- Lookback periods 1, 3, 6, 9, 12 months; holding periods 1, 3, 6, 9, 12 months; 25 portfolios opened each month; the monthly TSMOM return is the equally weighted average of all open positions.
- **No volatility scaling**, deliberately (Section 4, Endnote 11), because the authors have no volatility-predictability hypothesis.
- Positions are held for the duration of a fixed holding period; re-entry follows automatically from the next month's portfolio opening. Overlapping-position treatment beyond "equally weighted average of all open positions" is not further specified → underspecified on weights, sizing and ties.

**Appendix A4 strategy variants (Table A5 and Table A6 notes; all thresholds are source-reported, none is Scout-invented).**
- `Mkt-RF`: passive 1-month investment in the equity risk premium.
- `TSMOM (12,1)`: 1-month investment whose exposure equals the sign of the past 12-month equity market excess return.
- `Estimate-based strategy` (Table A5): an expanding regression estimated up to t−12 forecasts the forward 12-month excess equity return from the Average of the Boundaries, past 12-month equity excess returns and their interaction; invest 1 month in the equity risk premium if the estimate is **above 6%** (described as roughly the long-run historical average of the equity premium) and short the equity premium if the estimate is **below −2%**; otherwise zero. "It is therefore often out of the equity market."
- `TSMOM (12,1) when signals match`: invest in TSMOM(12,1) if and only if the estimate-based signal and the TSMOM(12,1) signal agree.
- `Estimate-based strategy 2` (Table A5): run the estimate-based strategy only if the **normalised CAPE is below 0.5**; returns are zero otherwise. The source's own commentary: it "performs extremely well, but this is more expected as the strategy conditions on several variables."
- `Estimate-based strategy` (Table A6, diversified TSMOM version): invest in the TSMOM index if the model estimate is **above −1%** (the note explains the cutoff as a one-third weight on TSMOM's long-run mean and two-thirds on the regression estimate) and short the TSMOM index otherwise.
- `TSMOM when signals match` (Table A6): long if the TSMOM regression estimate is **above −1%** and the TSMOM(12,1) estimate is **above −3%**.
- `Estimate-based strategy 2` (Table A6): run the estimate-based strategy except when **normalised CAPE is above 0.5 and past 12-month returns have been positive**.
- `Alternate between market and TSMOM`: hold the diversified TSMOM index whenever the Average of the Boundaries is **below 33% of its theoretical maximum of 2** (i.e. below 2/3) and the market risk premium otherwise; Appendix A4 prose adds that this low-Boundaries state "occurs roughly 20% of the time".
- In all of these, "returns equal zero when the conditions for investing are not satisfied."

**What remains underspecified:** which of CAPE versus dividend yield a real implementer should use (the paper runs both as alternatives and never selects one); how the 25 open TSMOM portfolios are weighted beyond equal weighting; the price and timestamp at which each monthly switch is executed; how a cash-market index short is actually obtained and financed; whether the expanding regression uses the same dependent-variable definition as Tables 3-5 (compounded) or as Tables 9-11 (summed); and any position sizing, leverage, margin or risk target. The record therefore does **not** present the Appendix A4 variants as reproducible.

## Required data

- **Instruments:** national/regional equity market index total returns; a long-term government bond total-return and yield series; a short-term risk-free rate; Shiller's CAPE; market-level dividend yield; term spread (long yield minus annualised short rate); NBER business-cycle peak dates; industrial production and unemployment (for the macro side-claims).
- **Universe:** one broad equity index per country; US sample plus a 20-country international panel (country list in Endnote 7). No single-name stocks, no sector, no options, no crypto.
- **Venue / market type:** cash equity index and cash bond market, monthly frequency. The source explicitly does not use futures.
- **Timeframe:** monthly. All main regressions use forward 12-month returns (compounded in Tables 3-6, sum of 1-month returns in Tables 9-12); Appendix A1 also reports forward 1-month regressions.
- **Fields:** index return, risk-free rate, long-bond yield and total return, CAPE, dividend yield, industrial production, unemployment, NBER peak flags.
- **Point-in-time:** CAPE from Robert Shiller's website and dividend yield from the same source carry revision and publication lag; the paper states no availability convention → `data gap`. Datastream index and bond vintages likewise → `data gap`.
- **Timestamp / timezone:** not stated for a monthly design → not applicable beyond month alignment, which is itself unspecified → `data gap`.
- **Missing data:** Table 1 Panel A contains **7 blank cells out of 100** and Panel B **14 blank cells out of 100** (Panel C has none); Table 2 contains cells printed as 0.0% and 100.0%, which implies cell counts of only a few observations; **no per-cell observation counts are printed anywhere** → `data gap`. The international panel is explicitly "unbalanced to maximize the sample size"; countries enter at different dates; imputation rules are never stated.

## Execution assumptions

**Source assumptions (as printed):** monthly rebalancing implied by "25 portfolios that are opened each month"; long leg financed by borrowing at the risk-free rate; short leg described as shorting the equity market index in the cash market; returns measured on index levels with **no stated cost of any kind**; the alternating strategy holds either the TSMOM index or the market risk premium and is flat only in the estimate-based variants.

**Not stated by the source → `data gap`, never treated as zero:** signal-to-order timing; next-bar/next-month-open versus same-month execution; order type; fill model; latency; bid-ask spread; commissions; slippage; market impact; index-short borrow availability and rebate; leverage and margin; liquidation; turnover of the switching rule; participation; capacity; partial fills and failure handling; and whether Tables A5/A6 returns are gross or net. **No cost, execution, financing or capacity model appears anywhere in the pinned text** (census in Provenance).

## Evidence

### Source-reported

All figures below are third-party claims from the pinned Version of Record, with their table provenance. Nothing here has been re-estimated by us.

**Table 1** (12-month forward returns of the diversified TSMOM index, double-sorted deciles of 12-month-average term spread against 12-month-average valuation, each normalised on a trailing 10-year window; US June 1927–December 2024, international January 1989–December 2024):
- Panel A (US, term spread x Shiller's CAPE): mid cells up to **45.5%** (term-spread decile 4, CAPE decile 3), 37.8%, 34.5%, 33.6%; corner and near-corner cells negative, e.g. **−15.6%** (decile 10, decile 5), **−12.3%** (decile 9, decile 7), **−11.1%** (decile 9, decile 6), **−7.7%** (decile 10, decile 4). 93 of 100 cells populated.
- Panel B (US, term spread x dividend yield): mid cells up to **35.0%** and **33.6%**; low cells to **−9.3%** (decile 9, decile 2) and **−4.5%** (decile 10, decile 5). 86 of 100 cells populated; one cell prints `9.12%` where every other cell prints one decimal.
- Panel C (international, term spread x dividend yield): mid cells up to **14.9%**; decile-10 row runs −2.2%, −5.6%, −5.1%, −2.4%, 0.5%, 2.3%, 4.6%, 1.1%, 0.9%, −1.8%. All 100 cells populated.
- Source's own summary (Section 1): "time-series momentum works best in the mid-valuation regimes, but it fails near historical extremes (the 10th and 90th percentiles of the past valuation ratios)".

**Table 2** (relative frequency with which future 12-month market excess returns share the sign of past 12-month excess returns, same double sort): cells span **0.0% to 100.0%**; the source reads it as showing "the probability that momentum continues is low near extreme valuation regimes". The presence of 0.0% and 100.0% cells with no printed denominators means the cell-level frequencies are thin → see Negative evidence.

**Table 3** (US, forward 12-month market excess returns, Newey-West with 12 lags, N = 1,159 / 1,040 / 920):
- `Past 12m stock market excess return × Boundaries`: **−0.45\*\*** (t = −3.05), **−0.33\*** (−2.20), **−0.43\*\*** (−2.82), **−0.26\*** (−1.98) in specifications (5)-(8).
- Adjusted R²: **0.07 / 0.10 / 0.08 / 0.10** without Boundaries, versus **0.12 / 0.15 / 0.13 / 0.16** with Boundaries and interactions; 10-year scaling gives 0.12 and 0.15, 20-year scaling gives 0.13 and 0.16.
- `Shiller's CAPE` **−0.11\*\*** (t = −3.13 / −3.16); `Dividend Yield` **0.14\*\*** (t = −2.82 / −2.89).

**Table 4** (international panel, same design, Newey-West, N = 7,717 / 5,337 / 2,937):
- `Past 12m stock market excess return × Boundaries`: **−0.33\*\*** (t = −6.37, 10-year scaling) and **−0.30\*\*** (t = −4.66, 20-year scaling).
- Adjusted R² rises from **0.05** (no Boundaries) to **0.15** and **0.17**; `past 12m stock market excess return` is +0.27\*\* (t = 4.10) in specification (4).

**Table 5** (US, forward 12-month returns to the diversified TSMOM index, Newey-West, N = 1,135 / 1,040 / 920):
- `Boundaries` alone: **−0.06\*\*** (t = −3.24), **−0.07\*\*** (−3.73), **−0.05\*\*** (−2.69), **−0.05\*\*** (−2.98) in the four specifications without interactions — significant at the 1% level in all four, exactly as the text states.
- With interactions, `Past 12m stock market absolute excess return × Boundaries` = **−0.13** (−0.74), **−0.25** (−1.83), **−0.21\*** (−2.00), **−0.34\*\*** (−2.58).
- Adjusted R²: **0.02 / 0.02** without Boundaries, rising to **0.08-0.12** with Boundaries and to **0.12** when interactions are included; the source's text says 2% → "up to 10%" with Boundaries and "up to 12%" with interactions.

**Table 6** (international TSMOM, Newey-West, N = 7,281 / 5,337 / 2,937): `Boundaries` = **−0.04\*\*** (t = −4.33) under 10-year scaling but **−0.01** (t = −0.65) and **−0.02** (t = −1.16) under 20-year scaling — i.e. not significant in the wider window; the `absolute equity return × Boundaries` interaction is **−0.26\*\*** (−5.31) and **−0.18\*\*** (−3.11).

**Table 7** (macro side-claims): moving averages of the valuation ratios raise predictive power for industrial production and unemployment; Section 5 prose states the R² "rises between 10% and 70% when moving averages are used instead of the unadjusted valuation ratios".

**Table 8** (US, averages by sign of past 12-month equity excess return and Boundaries state, sample June 1927 – December 2024 with the first 20 years used to form the Boundaries average): at-the-Boundaries versus within-Boundaries differences for positive minus negative past equity returns are **1.86 vs 4.21** percentage points of industrial-production growth, **0.68 vs 1.76** percentage points of risk-free-rate change, **0.16 vs 0.79** percentage points of 10-year yield change, **4.48 vs −4.24** percentage points of recession probability, and **−0.95 vs −1.05** percentage points of unemployment-rate change. (The note's percentile definition is internally inconsistent — see contradictions.)

**Section 6, Figure 2 (out-of-sample).** CUMSUM tests with an out-of-sample period starting in **2000**: `CUMSUMOOS` is positive for the diversified-TSMOM predictive regressions in Panels A-C (one-factor, three-factor and ten-factor), which the source reads as evidence of out-of-sample usefulness; for the **equity risk premium** (Panels D-F) only the one-factor model is positive and "the CUMSUM tests with more explanatory variables fail ... to show out-of-sample predictability". Endnote 15 adds: "the Boundaries-based predictability is driven mostly by the years 2012-2017."

**Section 7 (robustness).** Hodrick (1992) standard errors and the IVX procedure of Kostakis et al. (2015) replace Newey-West: the source states Hodrick t-statistics "generally tend to be smaller in absolute value" and that the key results are "still mostly present, albeit slightly weaker". Table 9's interaction is −0.43\* and −0.45\*\* in two columns but −0.27 and −0.23 (unstarred) in the other two; Table 11's interaction row is unstarred in all four columns with IVX p-values 0.50, 0.28, 0.31, 0.16.

**Table A5 — trading strategies for the equity premium, June 1968 – December 2023** (returns are 1-month returns per the note; units printed as percentages):

| | Mkt-RF | TSMOM (12,1) | Estimate-based | TSMOM (12,1) when signals match | Estimate-based 2 | Alternate between market and TSMOM (12,1) |
|---|---|---|---|---|---|---|
| Return since June 1968 | 0.56% | 0.35% | 0.54% | 0.41% | 0.56% | **0.65%** |
| Return since 2000 | 0.55% | 0.36% | 0.78% | 0.52% | 0.95% | **0.82%** |
| Sharpe since June 1968 | 0.42 | 0.26 | 0.47 | 0.55 | 0.53 | **0.49** |
| Sharpe since 2000 | 0.41 | 0.27 | 0.68 | 0.64 | **0.96** | 0.62 |
| Correlation with market since June 1968 | 1.00 | 0.11 | 0.73 | 0.53 | 0.66 | 0.81 |
| Correlation with market since 2000 | 1.00 | 0.04 | 0.82 | 0.60 | 0.71 | 0.65 |

**Table A6 — trading strategies for the diversified TSMOM index, June 1968 – December 2023:**

| | Mkt-RF | TSMOM | Estimate-based | TSMOM when signals match | Estimate-based 2 | Alternate between market and TSMOM |
|---|---|---|---|---|---|---|
| Return since June 1968 | 0.54% | 0.29% | 0.30% | 0.30% | 0.31% | **0.69%** |
| Return since 2000 | 0.52% | 0.38% | 0.46% | 0.44% | 0.51% | **0.88%** |
| Sharpe since June 1968 | 0.42 | 0.37 | 0.38 | 0.39 | 0.43 | **0.54** |
| Sharpe since 2000 | 0.41 | 0.46 | 0.56 | 0.54 | 0.65 | **0.70** |
| Correlation with market since June 1968 | 1.00 | 0.16 | 0.10 | 0.09 | 0.03 | 0.88 |
| Correlation with market since 2000 | 1.00 | 0.12 | 0.07 | 0.06 | −0.01 | 0.76 |

**Abstract.** Controlling for reversals near 10- or 20-year valuation extremes "increases the R2 of a predictive regression of equity market returns by up to 110% and the R2 of a predictive regression of time-series momentum returns by up to 550%."

**Table A3 / A4 (kitchen sink).** With unadjusted valuation ratios, risk-free-rate change, unemployment and its change added: `Past 12m stock market excess return × Boundaries` stays significant at the 1% or 5% level in all six Table A3 columns (−0.46\*\*, −0.30\*, −0.37\*\*, −0.28\*), and in Table A4 `Boundaries` is −0.07\*\* (−3.68), −0.07\*\* (−3.84), −0.06\* (−2.13), −0.05\* (−2.07), −0.06\*\* (−3.29), −0.05\*\* (−2.62), −0.06\* (−2.25), −0.05 (−1.19), −0.06\* (−2.25), −0.03 (−1.10) with adjusted R² up to **0.21**.

### Independently reproduced

`not independently reproduced`

Arithmetic-only cross-checks of printed cells (no data, no backtest, no dependency installed, no market data downloaded — these are consistency checks on the source's own numbers, not a reproduction of its empirical claims):

1. Table 3 paired adjusted-R² gains from adding Boundaries: 0.07→0.12 = **+71.4%**, 0.10→0.15 = **+50.0%**, 0.08→0.13 = **+62.5%**, 0.10→0.16 = **+60.0%**; the cross-pairing of the smallest baseline (0.07) with the largest Boundaries specification (0.15) gives **+114.3%**. The abstract's "up to 110%" is therefore arithmetically reachable only under 2-decimal rounding (a true baseline of ≈0.0714 rounds to 0.07); unadjusted R² is never printed → `data gap`.
2. Table 5 baseline 0.02 → maximum 0.12 = **+500.0%**; the abstract's "up to 550%" would require a baseline of ≈0.0185, which also rounds to the printed 0.02 → rounding-compatible but **not reproducible from printed values**; unadjusted R² not printed → `data gap`.
3. Table 4 international gains: 0.05→0.15 = **+200%**, 0.04→0.17 = **+325%**, both far above the abstract's 110% figure, so the abstract's number must come from a US specification only.
4. Table A5 Sharpe ranking since June 1968: market **0.42** > Estimate-based 2 **0.53** is the exception, but plain TSMOM(12,1) **0.26** and diversified TSMOM **0.37** (Table A6) both **trail** the market's 0.42 unconditionally.
5. Table A6 "Alternate" is not a fixed blend: a fixed 20/80 mixture of the printed TSMOM (0.29%) and market (0.54%) monthly returns is **0.49%**, whereas the printed Alternate column is **0.69%** — consistent with a switching series, and it confirms the column reflects state-dependent timing rather than an average holding.
6. Table 1 blank-cell counts: Panel A **7/100**, Panel B **14/100**, Panel C **0/100** (parsed cell-by-cell from the pinned text).
7. Table 8 note is internally exclusive: "Ninety percent … lowest … within" implies at-the-Boundaries = the top 10%, but "above the 10th percentile" would put **90%** of observations at the Boundaries.
8. Table 3 columns (1)-(4) t-statistics carry signs opposite to their own estimates; Table 9 prints the same specification with consistent positive signs — sign mismatch confirmed against raw DOM HTML.
9. Table 11: **10 of 10** estimates positive with **10 of 10** t-statistics negative — sign mismatch confirmed against raw DOM HTML.
10. Cost-term census reproduced independently: `transaction cost` 0, `slippage` 0, `commission` 0, `fee(s)` 0, `bid-ask` 0, `market impact` 0, `latency` 0, `turnover` 0, `leverage` 0, `margin` 0, `funding` 0, `capacity` 0, `execution` 0, `walk-forward` 0, `Benjamini` 0, `FDR` 0, `multiple testing` 0, `backtest` 0, `crypto` 0; `spread` 147 all inside `term spread`; `impact` 1 (a prose remark about OLS estimates).

### Negative evidence

1. **No cost model of any kind** is present; whether the reported strategy returns are gross or net is unstated → `data gap`, and the printed Sharpes cannot be read as implementable.
2. **Index shorting in the cash market** is assumed with no borrow cost, rebate, availability or locate model; the long leg's "borrowing at the risk-free rate" is a modelling convention only.
3. **Unconditional TSMOM loses to the market on Sharpe**: Table A5 TSMOM(12,1) 0.26 vs Mkt-RF 0.42 (since 1968); Table A6 diversified TSMOM 0.37 vs 0.42 (since 1968). The regime overlay, not momentum itself, is doing the work the source claims.
4. **Out-of-sample evidence is narrow**: CUMSUM for the equity risk premium fails for every multi-factor specification, and Endnote 15 states the Boundaries-based predictability "is driven mostly by the years 2012-2017".
5. **The headline interaction weakens under the source's own robustness methods**: in Table 11 (Hodrick/IVX) the `absolute equity return × Boundaries` interaction is unstarred in all four columns with IVX p-values 0.16-0.50, and in Table 9 two of four market-return interaction cells are also unstarred.
6. **Window sensitivity**: the international `Boundaries` coefficient is significant under 10-year scaling but not under 20-year scaling (Table 6 columns 4-7).
7. **Thin cells**: Table 1 has 7 (Panel A) and 14 (Panel B) empty decile cells and Table 2 contains 0.0% and 100.0% frequencies, with no printed observation counts per cell → the cell-level evidence base cannot be sized → `data gap`.
8. **No multiple-testing control anywhere**: `Benjamini`, `FDR` and `multiple testing` all have zero occurrences across 12 body tables, 6 appendix tables and 4 figures, all starred.
9. **No placebo, no walk-forward, no deflated Sharpe, no pre-registration.** "Out-of-sample" means CUMSUM on rolling regressions plus Appendix A4 strategies whose thresholds (6%, −2%, −1%, −3%, normalised CAPE 0.5, Boundaries 2/3) are never stated to have been fixed before the evaluation sample.
10. **Same-window performance concentration**: the strategies' gains are larger since 2000 than since 1968 (Table A5 estimate-based 0.78% vs 0.54%, estimate-based 2 0.95% vs 0.56%; Table A6 alternate 0.88% vs 0.69%) — the same window in which the CUMSUM out-of-sample test succeeds and the same window Endnote 15 identifies as driving the result (2012-2017).
11. **Self-declared research gaps by the authors**: Endnote 11 leaves Boundaries-based risk prediction "to future research"; Endnote 13 states "we do not analyze the portfolio effects of an international time-series momentum strategy"; the source itself cites McLean and Pontiff (2016) in Section 1 for the expectation that published return-predictive signals decay.
12. **The low-Boundaries state is rare as printed**: Appendix A4 says the `Average of the Boundaries < 2/3` condition "occurs roughly 20% of the time", so the headline `Alternate` column is a market-risk-premium book most of the time; no decomposition of that column into in-TSMOM versus in-market months is printed → `data gap`.
13. **Six unreconciled printed inconsistencies** (frontmatter `contradictions`), including two rows whose t-statistics contradict the sign of their own estimates. Table-level transcription from this source is not fully trustworthy.
14. **Formatting anomaly**: Table 1 Panel B prints a `9.12%` cell among one-decimal cells, suggesting a cell-level typesetting inconsistency.
15. **Sample ends December 2024** (December 2023 for the trading tables). No evidence after that date; no 2025-2026 regime; no crisis-2020 or 2022 sub-period decomposition is reported for the trading tables.
16. **Single asset class and single mechanism family**: broad equity indices and government bonds only; zero occurrences of crypto, perpetuals or single names.
17. **Point-in-time data risk**: CAPE and dividend yield come from a researcher-maintained website and bond/equity series from Datastream and Ibbotson; no vintage, revision or availability handling is stated → `data gap`.
18. **Publication-decay risk acknowledged but not measured** (Section 1, citing McLean and Pontiff 2016), and the article is itself newly published (July 2026).

None identified in the reviewed sources that contradicts the core reduced-form claim itself; **absence of a contrary published result is not evidence that no negative result exists**, and this run performed no literature search beyond the source's own reference trail (the bibliography itself was not retrievable → `data gap`).

## Falsification plan

Every threshold below that is not printed in the source is labelled **research-defined** (a falsification cutoff chosen by us) or **research-proposed** (an operational rule chosen by us). None is source-reported. **No-retuning rule:** once this plan is executed, every window, threshold, scaling choice and benchmark definition is frozen; a failure may not be rescued by re-selecting 10-year versus 20-year windows, CAPE versus dividend yield, or a different percentile cut.

| # | Gate | Test | Failure rule | Action on failure |
|---|---|---|---|---|
| F1 | Printed-value reproduction | Re-extract every number cited in this record from the pinned text and re-run the arithmetic checks above | Any cited number absent or different | Correct the record; if the source value cannot be located, delete the claim |
| F2 | Sign-consistency (**research-defined**) | Reconcile Table 3 cols (1)-(4) and Table 11 t-statistic signs against estimates and any published standard errors | Signs remain unreconcilable | Mark those two rows unusable; exclude them from all downstream summaries; if reconciliation requires errata, request them |
| F3 | Boundaries monotonicity (**research-defined**) | On an independent index-level monthly sample, regress forward 12-month TSMOM returns on Boundaries decile with HAC standard errors | Slope ≥ 0 or p ≥ 0.05 | Reject the regime-conditioning hypothesis for that universe |
| F4 | Interaction gate (**research-defined**) | Coefficient on `past-12-month return × Boundaries` negative with p < 0.05 under **both** Newey-West (12 lags) and IVX | Significant under only one method | Downgrade to `unproven`; the source's own Table 11 already fails this in 4/4 columns |
| F5 | Window robustness (**research-defined**) | Repeat F3/F4 for 10-year **and** 20-year normalisation and for CAPE **and** dividend yield (2x2) | Any cell of the 2x2 insignificant at 5% | Record regime-window dependence; do not average the cells |
| F6 | Frozen forward window (**research-defined**) | Extend the sample from 2025-01-01 forward for ≥ 24 months; TSMOM high-minus-low-Boundaries differential | Differential ≤ 0, or CUMSUMOOS turns negative over the new window | Falsify the out-of-sample claim for the modern period |
| F7 | Cost ladder (**research-proposed**) | Implement the switching rule via a broad index ETF or index futures at 0 / 1 / 2.5 / 5 / 10 bp round trip including financing of the short leg | `Alternate` Sharpe advantage over Mkt-RF (printed 0.54 vs 0.42 since 1968) falls below zero at ≤ 5 bp | Reject any implementable-alpha claim; keep only the reduced-form predictability claim |
| F8 | Turnover and capacity (**research-proposed**) | Measure annual turnover of the `Alternate` and `Estimate-based` rules; cap participation at 20% of index-ETF ADV | Sharpe degradation > 0.10 versus the costless printed value | Mark capacity as binding; downgrade implementability |
| F9 | Placebo (**research-defined**) | 1,000 circular-shift (phase-randomised) draws of the Boundaries series against TSMOM returns | Empirical rejection rate > 10% at a nominal 5% level | Treat the relationship as artefactual |
| F10 | Multiplicity (**research-defined**) | Benjamini-Hochberg at q < 0.10 over the full family of Boundaries and interaction coefficients across the equivalent of Tables 3-6, 9-12, A3, A4 | Headline interaction has q ≥ 0.10 | Downgrade the headline to non-significant; report only the family result |
| F11 | Ablation of the composite (**research-defined**) | Compare predictive power of: full Boundaries, CAPE term alone, term-spread term alone, the absolute-value alternative of Endnote 2, and a random orthogonal control | Full Boundaries does not beat every single-term and the control by ΔAIC ≥ 2 (or Δout-of-sample R² > 0) | Narrow the claim to whichever single term survives; drop the "joint boundary" language |
| F12 | Macro-mechanism gate (**research-defined**) | Reproduce Table 8: sensitivity of 12-month risk-free-rate and 10-year-yield change to past equity return in at-Boundaries versus within-Boundaries states | Difference not significant at 5%, or sign flips | Drop the monetary-policy interpretation; retain only the reduced-form timing result |
| F13 | Data-access gate | Point-in-time access to CAPE, dividend yield, term spread and index returns with vintage control | Not obtainable | Record stays `research-only` permanently; no implementation attempt |
| F14 | Crypto replication (**research-proposed**) | Build crypto analogues of the two components (e.g. funding-rate term structure or open-interest/valuation z-range as the "valuation" leg; a range-position measure as the "term-spread" leg) and test F3/F4 on BTC/ETH perpetual time series | No significant negative Boundaries slope at 5% with ≥ 36 months of data | Crypto portability stays `unproven`; no crypto implementation |

## Crypto portability

**`unproven`.**

The pinned source contains **zero** occurrences of `crypto`, `bitcoin` or `perpetual`, and no digital-asset instrument, no derivatives funding, no 24/7 session and no exchange-fragmentation analysis. This is a ported hypothesis, not crypto empirical evidence.

What would have to be re-derived rather than copied:
- **The "valuation" leg has no direct crypto analogue.** CAPE and dividend yield are aggregate earnings/payout ratios of an equity corpus; a crypto equivalent (e.g. realised-yield, fee-to-market-cap, or on-chain valuation ratios) is `research-proposed` and unvalidated.
- **The 10- and 20-year min-max windows do not fit.** BTC has roughly 15 years of continuous price history and most perpetuals far less; a 20-year normalisation window is impossible for the universe, and a shortened window changes the meaning of "historical extreme" (selection bias toward short-window extremes).
- **The bond leg disappears.** The term spread is a government yield-curve slope; crypto has no risk-free curve, so the second squared term must be replaced or dropped, changing Boundaries from a two-term to a one-term statistic (F11 must then be re-run).
- **Session and cadence.** The design is monthly with 12-month forward returns and 12-month moving averages; 24/7 candles, exchange-specific month boundaries, and per-venue timestamps all change the alignment of "month".
- **Execution.** Shorting a broad crypto index in cash does not exist; the implementable forms would be index-like baskets, perpetual shorts with funding, or inverse products — each with funding, mark/index price, liquidation, leverage and margin mechanics that the source does not model at all (all `data gap` here).
- **Venue and survivorship.** Delistings, index-construction rules, stablecoin/quote-currency effects and liquidity concentration are unaddressed.

Marking portability `direct` is forbidden: the source demonstrates the mechanism only in traditional equity and bond markets.

## Limitations

- `not independently reproduced`: **every empirical claim in this record.** Only internal arithmetic of printed cells was checked (14 checks listed under Evidence → Independently reproduced).
- `data gap`: PDF bytes, page count and PDF metadata; volume/issue/pages; received/accepted dates; ORCID; author emails; affiliations beyond the meta tags; funding and conflict-of-interest statements; bibliography size; per-cell observation counts in Tables 1-2; unadjusted R² behind the abstract's 110%/550%; all cost, execution, financing, leverage, turnover and capacity fields; point-in-time/vintage handling of CAPE, dividend yield, Datastream and Ibbotson inputs; and the SSRN version's own dates and page counts (not opened).
- `underspecified`: signal formation timestamp and tradability convention; execution price and timing of the monthly switch; weighting across the 25 open TSMOM portfolios beyond "equally weighted"; choice between CAPE and dividend yield for a real implementation; whether Appendix A4 regressions use compounded or summed dependent variables; the identity of "Table 4" in Section 6's ten-factor cross-reference.
- `unreconciled`: the six items in the frontmatter `contradictions`, two of which are sign contradictions between printed estimates and printed t-statistics. Table-level numbers from this source should be re-verified against an erratum or the PDF before downstream use.
- `unproven`: any claim that the regime overlay improves live returns; the monetary-policy mechanism (Section 5 is descriptive and the source does not identify it causally); out-of-sample performance after 2024; and crypto portability.
- The source's own framing is predictive-regression evidence, not a backtest: only Tables A5/A6 are strategy returns, they are costless by omission, and their switching thresholds are not stated to be pre-registered.
- **Incremental-write threshold / dedup context.** This record was written because the source identity and the mechanism are both absent from the repository (see the dedup evidence in the report below). It is a new family — *valuation-extreme regime conditioning of equity time-series momentum* — not a duplicate.

## Implementation status

`implementation_status: not-implemented`. Nothing in our stack has been built for this record: no strategy module, no data pipeline, no backtest, no indicator, no configuration. No Qlib full backtest, no Paper, no Testnet and no Live verification has occurred or is implied. This research capture does not modify NautilusTrader, create a strategy family, or authorise any execution stage.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. The presence of this record in the repository means only that normalised research material entered the public staging pool. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; or approved for live trading. No wording, evidence count, confidence value or schedule behaviour in this record promotes itself.

## Related Wiki records

Read-only `kb_search` on Hermes Wiki Brain (2026-09-29; queries: `time series momentum equity market timing valuation` → 10 results, none covering valuation-extreme regime conditioning of equity TSMOM; `equity market timing regime filter trend following valuation premium` → 10 results, none covering this mechanism or this source). **No Wiki Brain page exists for the Boundaries variable, valuation-extreme regime conditioning of time-series momentum, or this paper, so no Wiki link is fabricated for the core mechanism.** `kb_read` was used twice to resolve the canonical specification; **no Wiki write was performed by this run.**

Adjacent **repository** records (dedup context only — different source identities and different mechanisms, therefore **not** Wiki links):

- `crypto-risk-managed-tsmom-crash-state-de-risking-drawdown-control-2026-09-14.md` — same strategy family (time-series momentum) but a crypto universe with a crash-state/de-risking risk overlay instead of a valuation regime; source SSRN 7115459.
- `long-only-us-equity-ath-trend-following-vol-sizing-atr-ratchet-turnover-control-ssrn-5084316-2026-09-27.md` — US equity trend with volatility sizing and ATR ratchet stops (risk/exit mechanism), source SSRN 5084316; no valuation regime.
- `us-equity-long-only-trend-above-own-sma-cash-retreat-nvidia-concentration-attribution-ssrn-7073258-2026-09-28.md` — long-only single-name moving-average trend with cash retreat and an attribution audit; different universe, different signal, source SSRN 7073258.
- `us-equity-pretom-month-end-liquidity-demand-dispensability-factor-zoo-ssrn-6909918-2026-09-29.md` — shares senior author Matti Suominen but is a different paper (SSRN 6909918), a cross-sectional anomaly/calendar-window claim at a six-day horizon, not an index-level regime-conditioned TSMOM claim.
- `gq-lasso-quantile-equity-premium-timing-2026-09-25.md` — equity-premium forecasting and monthly timing, but a penalised-quantile forecasting method (arXiv:2505.16019) rather than a valuation-extreme regime filter on momentum.
- `two-stage-adaptive-shrinkage-golden-criterion-equity-premium-2026-09-02.md` — equity-premium predictability/aggregation method (arXiv:2607.11054), different source and different mechanism.
- `fractional-momentum-fractional-difference-filter-crash-mitigation-2026-09-23.md` — momentum crash mitigation via a fractional-difference filter; a signal-construction mechanism, not a valuation regime.

## Sources

1. Suominen, Matti, and Erik Hjalmarsson. *Boundaries of Time-Series Momentum.* **Financial Management**, first published 06 July 2026, Early View (online Version of Record before issue assignment). DOI `10.1111/fima.70055`. ISSN 1755-053X. Publisher John Wiley & Sons, Ltd. Open Access (Wiley – FinELib agreement funded by Aalto-yliopisto). Full text: https://onlinelibrary.wiley.com/doi/full/10.1111/fima.70055 — **pinned and read end to end on 2026-09-29**, 108,097 bytes / 105,970 characters, SHA-256 `94abc96ea27c2b7d3aa7ff79078ba5be50794a2d7ea54a9ac9ec3ea59a340c1f`.
2. DOI resolver: https://doi.org/10.1111/fima.70055
3. SSRN working-paper version of the same study (identified, **not opened this run**): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6867878 ; DOI https://doi.org/10.2139/ssrn.6867878 — all version-specific fields `data gap`.
4. PDF endpoint of the primary source (attempted, **not obtained**, HTTP 403 behind a Cloudflare interstitial and HTML instead of PDF bytes in-session): https://onlinelibrary.wiley.com/doi/pdf/10.1111/fima.70055
5. Third-party secondary summary, cited **only** to document an author misattribution and **not** used as a source for any fact about the paper: https://etfps.substack.com/p/the-etf-portfolio-strategist-01-jul (attributes the study to `Matti Suominen` and `Sebastian Müller` and dates it `01 June 2026`, neither of which matches the primary source).

**Dedup and safety notes for this run.** Hidden-inclusive source-identity search with `rg -uuu -i -F` across the entire checkout (including `.git`, `.mimo-worktrees`, `.agents`, `.hermes` and `coverage_manifest.csv`, 1,088,787 bytes) for `fima.70055`, `10.1111/fima`, `Boundaries of Time`, `Boundaries variable`, `Suominen`, `Hjalmarsson`, `valuation extremes`, `mid-valuation`, `term spread`, `1755-053X` and `6867878` returned **no pre-existing record for this source**: zero hits for `fima.70055`, `Boundaries of Time`, `Boundaries variable`, `Hjalmarsson`, `mid-valuation`, `1755-053X` and `6867878`; `coverage_manifest.csv` returns zero for all of `6867878`, `fima.70055`, `Suominen`, `Hjalmarsson`, `Boundaries of Time`; `Suominen` matched only the unrelated SSRN 6909918 record (same author, different paper); `10.1111/fima` matched three unrelated records whose DOIs merely share the Wiley `10.1111` prefix; `valuation extremes` matched two unrelated Bitcoin TradingView records; `term spread` matched unrelated macro/predictability records. Positive control `novy-marx` (`.git` excluded) was 36 files before writing. `git log --oneline -20` was used as a convenience glance only and does not substitute for the search above.
