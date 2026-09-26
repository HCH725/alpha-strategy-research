---
schema: strategy-research-record-v1
title: "50/5/10 Constrained Ownership Share (C): Long-Side Regulatory-Constraint Underpricing Signal for Large U.S. Equities"
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
  - "https://www.nber.org/papers/w35007"
  - "https://doi.org/10.3386/w35007"
  - "https://www.nber.org/system/files/working_papers/w35007/w35007.pdf"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# 50/5/10 Constrained Ownership Share (C): Long-Side Regulatory-Constraint Underpricing Signal for Large U.S. Equities

## Provenance

- **Primary source (pinned, checksummed, text-extracted, and read across the sections listed below):** Pastor, Lubos; Sikorskaya, Taisiya; Wang, Jinrui, *The Hidden Cost of Stock Market Concentration: When Funds Hit Regulatory Limits*, NBER Working Paper **35007**, DOI **10.3386/w35007**. The full 140-page text layer was extracted and the sections enumerated below were read directly; the model/proof appendices (A.1, A.2) and the remaining robustness appendices were **not** opened directly and are cited only via the source's own summaries in §3.4 and §6.4.
- **Version/date as printed on the pinned PDF title block:** "March 2026, Revised September 2026"; NBER landing page `Issue Date = March 2026`, `Revision Date = September 2026`, `citation_publication_date = 2026/03/30`, with "Other Versions" dated March 24, 2026 and June 10, 2026. Landing page fetched **2026-09-26** (HTTP 200).
- **Pinned PDF:** `https://www.nber.org/system/files/working_papers/w35007/w35007.pdf`, **11,971,499 bytes**, **SHA-256 `543b928e2aba2936c3a714cf31180e9c6fc3f2519615e95ef5241915fd19122a`**, **140 pages**, downloaded and text-extracted **2026-09-26**.
- **Sections read line-by-line for this record:** title block and Abstract; §1 Introduction; §2 Institutional background incl. §2.3 Data; §3 (3.1 Fund buffers, 3.2 Index buffers, 3.4 The cost of index capping); §4.1 Stock substitution; §5.1 Realized returns, §5.2 Counterfactual portfolio returns; §6 (6.1–6.4); §7.3; §8.4; §9 Conclusion; **Table 8**, **Table 9**, **Table A.17**, **Table A.27** read as printed tables; Tables 2, 3, 6 and 7 taken from the source's own prose in §3.4, §4.1, §5.1 and §5.2 respectively (the tables themselves were not re-opened cell by cell); Appendix TOC; Appendix A.17 section text.
- **Additional appendix material:** Appendix A.11 read in full (eq. A.54–A.56). Appendix figures/tables A.4, A.5, A.10 and A.11 were **not** opened directly; anything about them in this record is quoted only from the source's own summaries in §4.1 and §6.1 and is labelled as such.
- **Publication/peer-review status (source's own words, PDF p.1):** "NBER working papers are circulated for discussion and comment purposes. They have not been peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies official NBER publications." → **working paper, not peer reviewed**.
- **Author block as printed:** Lubos Pastor (The University of Chicago Booth School of Business and NBER), Taisiya Sikorskaya (The University of Chicago Booth School of Business), Jinrui Wang (The University of Chicago Booth School of Business; jinrui.wang@duke.edu). JEL G12, G14, G23, G28.
- **Disclosures as printed:** "The views expressed here do not necessarily reflect those of Vanguard, its funds, or the National Bureau of Economic Research"; "At least one co-author has disclosed additional relationships of potential relevance for this research"; support acknowledged from the Fama-Miller Center for Research in Finance, University of Chicago Booth School of Business. Per-author mapping of the Vanguard-related disclosure is **data gap** (the PDF does not state which author it belongs to).
- **Code / data / replication:** a full-text scan of the pinned PDF for `github`, `replication`, `data availability`, `available from`, `upon request` returned **no hits** → **no code repository, no replication package and no data-availability statement anywhere in the pinned PDF**; every availability field is `not stated in source`.
- **Publication status of the empirical claim:** all performance figures below are **source-reported** third-party results that have **not** been independently reproduced.
- **Dedup (pre-write, whole repository):** deterministic source-identity search with `rg -uu` over **all 2,561 `.md` files** in the checkout including hidden trees `.mimo-worktrees/`, `.agents/`, `.hermes/`, plus `coverage_manifest.csv`, for `10.3386/w35007`, `w35007`, `35007`, `constrained ownership`, `constrained-ownership`, `constrained fund`, `50/5/10`, `50-5-10`, `50/5/10 rule`, `diversification test`, `NPORT-P`, `The Hidden Cost of Stock Market Concentration`, `Taisiya Sikorskaya`, `Jinrui Wang`, `Lubos Pastor`, `index capping`, `long-position constraint`, `regulated investment compan`, `Russell 1000 Growth`, `Magnificent 7` → **all zero hits** before this write (the only `Pastor` hits are surname collisions inside unrelated records; `Nasdaq-100` hits resolve to unrelated index/derivative records). `git log --oneline -20` was inspected as a convenience glance only and does not by itself satisfy dedup.

## Economic mechanism

### Source-reported

The Internal Revenue Code §851(b)(3) "50/5/10 rule" requires a Regulated Investment Company to hold at least 50% of total assets in issuers for which no single issuer exceeds 5% of total assets and no more than 10% of the issuer's voting securities (§2.2). Because funds track capitalisation-weighted benchmarks, their largest positions sit in the largest-capitalisation stocks, so the rule "effectively constrains funds' long positions in the largest firms" (§1).

The paper hypothesises (§1, §6, §6.4) that in a concentrated market the largest stocks may be **temporarily underpriced** if optimistic investors are unable or unwilling to hold them to the desired extent: an active large-cap growth manager who is optimistic about a mega-cap name will not overweight it further for fear of breaching the limit, and if the benchmark itself is near the limit even passive index funds are constrained, so prices must fall to induce non-index investors to absorb the excess supply.

The authors formalise this in Appendix A.1 ("Model of constrained active demand"): a two-belief (optimist/pessimist) model with a cap on long positions yields two propositions — (i) when the constraint binds, assets favoured by optimists are underpriced because pessimists become the marginal price setters; (ii) four comparative statics: underpricing is **larger** when the constraint is tighter, when the constrained asset is in greater supply, when the asset's payoff is **more volatile**, and when disagreement between optimists and pessimists is **larger**. The source frames this explicitly as the mirror image of Miller (1977) short-sale-constraint overpricing: "constraints on long positions can generate underpricing by suppressing optimists' views" (Abstract).

Supporting behavioural/structural links the source documents: constrained and negative-buffer funds bunch their portfolio weights just below the 5% cutoff (McCrary density test shows a significant discontinuity around 4.9%, Fig. A.4–A.5), reduce rather than increase large positions (59% vs 41% of constrained funds), trim large positions about 12 bps per quarter on average rising to more than 20 bps near the limit (Table 3, §4.1), and cut overall equity exposure by substituting cash (§4.2). Constrained funds then underperform (§5.1), consistent with having sold positions whose subsequent returns they forgo.

Component roles (as declared by the source):

```text
Regime / trigger : rising stock-market concentration pushes fund and index buffers
                   toward the statutory 50/5/10 limit (binding mainly in 2023-2024;
                   large-cap growth category the epicentre)
Primary signal   : constrained ownership share C_s,t — the fraction of a stock's
                   outstanding shares held as a >5% "large position" by funds whose
                   50/5/10 buffer is below 5% (constrained + negative-buffer funds)
Confirmation     : source-reported effect modifiers from the model's comparative
                   statics — above-median return volatility, higher analyst
                   forecast dispersion, active (not passive) constrained funds
Portfolio form   : value-weighted C>0 long-only portfolio versus a C=0 control,
                   monthly formation, one-year holding
Risk / exit      : not specified by the source (no stop, no sizing rule, no exit rule)
```

The source does not claim every component contributes alpha; it reports the volatility and disagreement interactions as incremental (regression (19) and Appendix A.16) and reports that active-fund C predicts better than passive-fund C (§7.3).

### Research interpretation

Falsifiable statement of the mechanism as we normalise it: **aggregate, regulation-forced underweighting of a stock by optimistic institutional holders creates a transitory negative demand shock whose later correction produces positive risk-adjusted returns concentrated in the stocks, periods and risk states where the forced underweight is largest and the price concession required to clear the excess supply is highest.**

In falsifiable terms this predicts: (a) a positive cross-sectional relation between C and subsequent factor-adjusted returns, strongest when the binding constraint is tightest (2023–2024); (b) a positive C × volatility interaction and a positive C × analyst-disagreement interaction; (c) a stronger signal when the constrained holder is an active fund rather than a passive one; (d) no comparable effect from funds whose buffers are wide; (e) if the mechanism is causal rather than a size/AI/liquidity artefact, the relation should survive an AI-sector factor, an ex-Magnificent-7 sample, and a control for a "large position" indicator that is not buffer-conditional. The source reports evidence on (a)–(e). Because the identifying variation is a *regulatory* constraint on *U.S. registered open-end funds*, the mechanism is a **market-structure channel**, not a behavioural-anomaly-per-se claim; its persistence is contingent on the rule remaining binding, which is an empirical state variable rather than a permanent feature.

We treat the strategy layer (long-short implementation, cost ladder, sizing, rebalancing mechanics) as **research-proposed** — the source specifies only long-only value-weighted test portfolios and does not specify an implementable trading rule beyond sorting and holding.

## Signal

All parameters in this section are **source-reported** unless explicitly marked `research-proposed`.

### 1. Fund-level inputs (per fund f, fiscal quarter t)

- `Weight_f,s,t = Value_f,s,t / TotalAssets_f,t × 100` (eq. 1), both variables from **SEC NPORT-P filings**.
- A holding is a **large position** if it exceeds **5% of the fund's total assets** *or* **10% of the issuer's voting securities**; for simplicity the source assumes each common share carries one vote (§2.2, §3.1).
- `Buffer_f,t = 50% − Σ_{s ∈ LargePos} Weight_f,s,t` (eq. 2). Mirror-image calculation (summing large positions rather than non-large positions), justified by footnote 8 as simpler for processing equity holdings.
- Classification: **negative-buffer fund** if `Buffer < 0`; **constrained fund** if `0 ≤ Buffer < 5%` (upper bound set at 5% "to match the regulatory threshold for large positions", §3.1).
- `Shares_f,s,t` = shares held by fund f in stock s in fiscal quarter t, adjusted for splits and dividends using **CRSP CFACSHR** (defined immediately after eq. 7).

### 2. Stock-month signal (eq. 17)

```
C_s,t (%) = [ Σ_f Σ_{τ = t-2..t} Shares_f,s,τ × D^{W>5}_f,s,τ × D^{B<5}_f,t ]
            / SharesOutstanding_s,t × 100
```

- `D^{W>5}` = 1 if the fund's weight in that stock is above 5%; `D^{B<5}` = 1 if the fund's buffer is below 5% (constrained **or** negative-buffer).
- The three-month window (`t`, `t−1`, `t−2`) exists only "to account for differences in fiscal quarter-ends across funds"; for each fund the **latest holdings report available within that three-month window** is used (§6.1).
- Denominator is **all shares outstanding**; the source states C "is essentially a lower bound for constrained ownership" for three stated reasons (float, positions just under 5%, and funds constrained by the 75/5/10 rule) (§6.1).

### 3. Cross-sectional regression sample and covariates

- Formation timestamp: **end of month t**; C is a month-t variable built from quarterly holdings.
- Universe filter: stocks with **price above $5** and, within each month, the **largest 50% by market capitalisation** → **2,806 stocks** (Table 8 / Table 9 notes; 2,799 after excluding the Magnificent 7 in Table A.17).
- `HighC_s,t` = 1 if `C_s,t > 0`; `LowC` (`C_s,t = 0`) is the omitted group (§6.2).
- `Volatility_s,t` = standard deviation of **daily** stock returns over months `t−2, t−1, t`; `HighVol_s,t` = 1 if above the cross-sectional median in month t (§6.2).
- Dependent variable: cumulative return over horizon `h ∈ {1, 3, 6, 9, 12}` months adjusted for **market, size, value and momentum (Carhart 1997)**. Per Appendix A.11 (read for this record) the procedure is **identical for funds and stocks**: factor loadings `β̂_i,t` are estimated from a **daily** Carhart four-factor regression (eq. A.55) over the **252 trading days up to and including the last trading day of month t**, and `Ret(FF4)_i,t+h = (R_i,t+1→t+h − RF_t+1→t+h) − β̂'_i,t · F_t+1→t+h` (eq. A.56) using cumulative monthly factor returns. CAPM-adjusted and FF4+AIQ variants are constructed analogously.
- Estimation: regressions (18) and (19) with **year–month fixed effects**, standard errors **clustered by stock**; robustness to Driscoll–Kraay with `h−1` lags in Appendix A.13.

### 4. Trading strategy as specified by the source (§6.3, Table 9, Table A.27)

- **Formation:** at the **end of each month t**, sort stocks into `High C (C > 0)` and `Low C (C = 0)`.
- **Sizing:** **value-weighted** portfolios for each group.
- **Holding period:** **one year** (so 12 overlapping annual cohorts are formed from monthly sorts; the source reports the High-C portfolio contains **382 stocks on average**).
- **Double sort:** independent monthly sort into above/below-median volatility × the two C groups → 2×2 value-weighted portfolios, each held one year.
- **Evaluation:** annualised **daily** Carhart four-factor alphas using daily factor returns from Ken French's website; **Newey–West t-statistics with a five-day lag** (Table 9 note).
- **Feasible (lagged) variant:** because the NPORT-P regulatory reporting lag is **two months**, the source repeats the whole analysis sorting on the **previous quarter's C** (`C_{s,t−3}`) — Table A.27 / Appendix A.17. Reported alphas are similar (see Evidence).
- **Not specified by the source (therefore `research-proposed`, not source-reported):** any long-short construction, position caps, turnover target, order type, signal-to-order delay beyond the stated filing lag, entry/exit price convention, stop, leverage, borrow arrangement, or rebalancing implementation. A long-short "High-C minus Low-C" book, a volatility-targeted overlay, and any net-of-cost series are **our** operationalisations, not the source's.

### 5. Threshold provenance

The thresholds 50% / 5% / 10%, the buffer cutoff of 5%, the $5 price screen, the above-median-cap screen, the monthly formation cadence, the one-year holding period and the median volatility split are all **source-reported**. The source's own sensitivity note: redefining a large position as weight above 4% and constrained as buffer below 10% raises the market share of `C > 0` stocks to **78%** in 2024Q4 (from about 60%) — i.e. the coverage of the signal is **threshold-sensitive** (§6.1).

## Required data

- **Instrument / universe:** U.S.-listed **common stocks**, identified by CRSP **PERMCO** (security-level PERMNO aggregated to firm level with market-cap weights). Regression universe additionally screened to price > $5 and above-median monthly market cap (2,806 stocks); the underlying holdings sample covers **6,807** U.S.-listed common stocks ever held by the funds during the sample (4,440 present at end-2024).
- **Venue / market type:** U.S. listed equity exchanges (venue is not itemised by the source → venue-level detail is `data gap`); cash, long-only.
- **Fund sample:** **4,745** U.S. domestic equity funds (mutual funds and ETFs, active and passive) with equity holdings between 50% and 150% of total assets; four funds excluded for erroneous pre-September-2021 reported shares (§2.3 footnote 7).
- **Sample period:** NPORT-P data first available **September 2019**, sample ends **December 2024**; predictability reported for **2019–2024** (full) and **2023–2024** (sub-period).
- **Fields:**
  - SEC **NPORT-P** filings: complete portfolio holdings and **total assets** per fiscal quarter (chosen because 50/5/10 is tested on total assets, not CRSP total net assets).
  - **CRSP** mutual fund database (returns, expense ratios, Lipper classifications, total net assets for share-class aggregation) and CRSP stock database (returns, shares outstanding, CFACSHR, industry classifications).
  - **Compustat** accounting data for book-to-market (3×3 style classification).
  - **Fama–French factors** from Ken French's data library (daily Carhart four-factor returns for the strategy alphas).
  - Shares outstanding for the C denominator; daily returns for volatility; analyst forecast dispersion (Diether–Malloy–Scherbina style, Appendix A.16); analyst growth-forecast revisions (Appendix A.15); the **Global X Artificial Intelligence & Technology ETF (AIQ)** daily return as an extra factor (§6.2, Appendix A.14; AIQ identified in Appendix A.11).
  - Index side: **ETF Global** daily ETF holdings to approximate index weights; QQQ holdings for Nasdaq-100 constituents; Nasdaq-100 official total-return series (§3.2, §3.4).
  - 75/5/10 side: annual **N-CEN** filings (§8).
- **Point-in-time / availability:** NPORT-P **reporting lag = two months** (source's own statement, §6.3). The headline Table 8 / Table 9 results use **contemporaneous C**, i.e. holdings information that is not yet publicly available at formation → those results contain a filing-lag look-ahead. The source's feasible counterpart is Table A.27 (`C_{s,t−3}`), which is the point-in-time version.
- **Timestamp / timezone:** monthly equity-market month-ends, U.S. exchange calendar; the source does not state a timezone or an explicit timestamp convention for the formation instant → `underspecified`.
- **Missing-data:** the source excludes four funds with erroneous reported shares; no other imputation rule for missing or stale holdings is stated → `not stated in source`. Note that any reconstruction must not impute missing holdings (spec rule) and should record them as gaps.
- **Survivorship / reconstitution:** the stock universe is "**ever held by these funds during the sample period**" — an ex-post union rather than a point-in-time membership list. This is an ex-post universe filter and is recorded under Negative evidence.
- **Funding / fee / spread / borrow needs:** not addressed anywhere by the source for the stock strategies → `data gap`.

## Execution assumptions

Cost determination for this record was made from a Methods-level read of §2.3 (Data), §3.1, §4.1, §5.1–5.2, §6.1–6.4, §7.3, §8.4, Table 8/9/17/27 notes and Appendix A.17, **plus** a full-text keyword scan of the pinned 140-page PDF.

| Item | What the source actually says |
|---|---|
| Signal-to-order timing | NPORT-P filing lag = **two months**; feasible analysis uses `C_{s,t−3}` (§6.3). Nothing on intraday timing. |
| Order type / fill model | **Not stated in source** → `data gap` |
| Fees / commissions | **Not stated in source** → `data gap` |
| Bid-ask spread | **Not stated in source** → `data gap` |
| Slippage | **Not stated in source** → `data gap` |
| Market impact / participation / ADV / capacity | **Not stated in source** → `data gap` |
| Borrow / shorting | Strategy as reported is **long-only value-weighted test portfolios**; no short leg, no borrow cost → `data gap` for any short implementation |
| Leverage / margin | **Not stated in source** → `data gap` |
| Turnover | **Not reported for the strategies** (the only "turnover" hits in the PDF are fund turnover-ratio *controls*) → `data gap` |
| Gross vs net of cost for Table 9 / A.27 | **Neither stated nor asserted**. The only cost-related sentence in §6.3 is: *"These strategies are unlikely subject to large trading costs because High-C stocks are among the most liquid securities in the market."* → gross/net status is `data gap`; we do **not** infer "gross" or "zero cost". |
| Latency / partial fills / failure handling | **Not stated in source** → `data gap` |
| Rebalance cadence | Monthly formation with **one-year holding**; overlapping cohorts; no explicit trade list → implementation cadence is `underspecified` |
| Costs elsewhere in the paper | Costs appear only for the fund-side discussion: §5.2 notes actual fund returns "reflect also trading costs, intra-quarter rebalancing, and any countermeasures", explicitly saying the counterfactual estimates are not meant to match realized drag; §3.4 reports QQQ returns **net of fees**. Neither is a cost model for the stock signal. |

The single qualitative liquidity assertion is recorded as a **source-reported qualitative claim**, not as a cost model. Every quantitative execution field is a `data gap` and must never be read as zero.

## Evidence

### Source-reported

All figures below are third-party results reported by Pastor, Sikorskaya & Wang, NBER WP 35007 (pinned PDF read 2026-09-26), and have **not** been independently reproduced.

**A. Predictive regressions — Table 8, "Stock return predictability" (annualised-units cumulative Carhart-4 risk-adjusted return, in percent; year–month fixed effects; SEs clustered by stock; *p<0.10, **p<0.05, ***p<0.01):**

*Panel A: 2019–2024, `High C` coefficient from eq. (18)* — 1M **0.112** (t = 1.43); 3M **0.337** (1.53); 6M **0.805\*** (1.85); 9M **1.546\*\*** (2.25); 12M **2.252\*\*** (2.37). Observations 109,335 / 108,672 / 107,767 / 102,129 / 96,552.

*Panel A, eq. (19) with volatility* — `High C` 0.091 (1.28), 0.359\* (1.82), 0.549 (1.49), 1.044\* (1.90), 1.319\* (1.79); `High C × High Vol` 0.030 (0.15), −0.182 (−0.34), 0.578 (0.54), 1.258 (0.75), 2.630 (1.14); `High Vol` −0.056, −0.181, −0.359, −0.511, −0.544 (all insignificant).

*Panel B: 2023–2024, eq. (18)* — 1M **0.309\*\*** (2.57); 3M **1.100\*\*\*** (3.34); 6M **2.301\*\*\*** (3.47); 9M **3.343\*\*\*** (3.17); 12M **4.391\*\*\*** (2.89). Observations 39,846 / 39,627 / 39,350 / 34,301 / 29,294.

*Panel B, eq. (19)* — `High C` 0.067 (0.61), 0.557\* (1.84), 0.835 (1.41), 1.591\* (1.66), 1.931 (1.43); `High C × High Vol` **0.661\*\*** (2.34), **1.473\*\*** (2.00), **3.847\*\*\*** (2.65), **4.416\*\*** (2.01), **6.280\*** (1.95); `High Vol` −0.103, −0.247, −0.898, −1.467, −2.125 (all insignificant).

Prose summary in §6.2: "stocks with C > 0 earn three-month cumulative abnormal returns 1.1% higher than those of stocks with C = 0" in 2023–2024; §1 additionally states the 6-month differential is 2.3% in that sub-period (matching Table 8 Panel B, 6M = 2.301).

**B. Trading strategy — Table 9, "Investment strategy" (annualised daily Carhart four-factor alpha, %; Newey–West t with 5-day lag):**

| | Single sort: High C | Double sort: High C / **High Vol** | Double sort: High C / **Low Vol** | Single sort: Low C | Low C / High Vol | Low C / Low Vol |
|---|---|---|---|---|---|---|
| **Panel A 2019–2024** | **1.68\*** (1.88) | **7.91\*** (1.82) | −0.70 (−0.46) | −2.00 (−1.11) | −0.75 (−0.25) | −2.47 (−1.09) |
| **Panel B 2023–2024** | **2.32\*\*** (2.34) | **11.85\*\*** (2.00) | −1.32 (−0.53) | −2.12 (−0.94) | −2.11 (−0.65) | −2.13 (−0.70) |

§6.3 prose rounds these to 1.7% / 2.3% and 7.9% / 11.8%, and states the High-C portfolio holds **382 stocks on average**.

**C. Feasible, filing-lag-aware version — Table A.27 (sorting on `C_{s,t−3}`), Appendix section A.17 "Implementability of trading strategies":**

| | Single sort: High C | High C / **High Vol** | High C / **Low Vol** | Single sort: Low C | Low C / High Vol | Low C / Low Vol |
|---|---|---|---|---|---|---|
| **Panel A 2019–2024** | **1.65\*** (1.71) | **9.74\*\*** (2.12) | −1.14 (−0.70) | −1.60 (−0.87) | −0.59 (−0.19) | −1.92 (−0.83) |
| **Panel B 2023–2024** | **2.23\*\*** (2.19) | **10.93\*** (1.84) | −1.31 (−0.53) | −1.75 (−0.78) | −1.27 (−0.39) | −1.94 (−0.63) |

§6.3 prose: lagged High-C alphas are 1.7% (2019–2024) and 2.2% (2023–2024); lagged High-C-High-Volatility 9.7% and 10.9%; "all four alphas are significant at the 90% level but only two are significant at the 95% level".

**D. Robustness / mechanism checks (source-reported):**

- **Excluding the Magnificent 7 (Table A.17, sample 2,799 stocks):** Panel A `High C` 0.058 (0.78), 0.166 (0.81), 0.432 (1.09), 0.892 (1.49), 1.308 (1.61) — **all insignificant**; Panel A `High C × High Vol` −0.091, −0.603, −0.510, −0.610, −0.031 — all insignificant. Panel B `High C` 0.265\*\* (2.20), 0.991\*\*\* (3.01), 2.104\*\*\* (3.18), 3.014\*\*\* (2.88), 3.815\*\* (2.57); Panel B interaction 0.564\* (1.96), 1.196 (1.61), 3.187\*\* (2.19), 3.311 (1.53), 4.409 (1.44). §6.2: "slightly weaker than in Table 8 but remain mostly significant in the 2023–2024 period".
- **AI-sector fifth factor:** adding the return of the **Global X Artificial Intelligence & Technology ETF (AIQ)** leaves C coefficients "similar and continue to be economically and statistically significant" (§6.2, Appendix A.14; ETF identified in Appendix A.11 as the FF4+AIQ construction); Table 9 alphas are "very similar" with the extra factor (§6.3).
- **Analyst growth-forecast revisions control:** does not diminish C's predictive power (§6.2, Appendix A.15).
- **Analyst dispersion:** `High C × disagreement` positive and significant, especially 2023–2024; remains significant when the volatility interaction is included (§6.2, Appendix A.16).
- **Large-weight indicator control:** predictive power is not simply funds' propensity to trim large positions (§6.2, Appendix A.13).
- **Active vs passive (§7.3):** active-fund C predicts "a bit more strongly" than all-fund C; passive-fund C estimates are "smaller and weaker statistically".
- **75/5/10 rule (§8.4):** diversified funds with buffers in [20,30)%; directionally similar but weaker statistically; the high-C/high-volatility strategy reports annualised alphas of **10.2% (t = 2.04)** full period and **14.6% (t = 2.07)** in 2023–2024, based on **annual N-CEN filings**.

**E. Contextual / supporting numbers (source-reported):**

- Market concentration: top-10 share of total U.S. market cap rose from **13% to 31%** between 2015 and 2024; within large-cap growth from **30% to 48%** (Figure 1, §1).
- Constrained fund prevalence: negligible in 2019Q3 → **6% of total fund assets** in 2024Q4; peak **2024Q3 with 171 funds (4.5% of funds), 8% of total fund assets, almost $1.4 trillion**; large-cap growth about **one-third of its funds**, **>$1.1 trillion**, about half the category's assets (§1, §3.1, Figure 4).
- `C > 0` stocks: **93 in 2019Q3 → 269 in 2024Q4** (8% of stocks) with **$41 trillion** market cap, **over 60%** of the market; most C values below 1%; `C > 1%` stocks ≈ **30%** of total U.S. market cap at end-sample; **Nvidia C ≈ 5.3%**, **Microsoft C ≈ 4.7%** (§6.1, Figure 7).
- Index capping (Table 2, §3.4): uncapped Nasdaq-100 counterfactual **24.8%/yr** vs actual **23.3%/yr** over 2019–2024 → **+1.5%/yr** (Newey–West significant); gap **3.4%/yr** over 2023–2024; QQQ returned **23.1%/yr net of fees**, **1.7%** below the counterfactual (3.6% gap in 2023–2024).
- Fund performance (Table 6, §5.1): large-cap growth funds' FF4-adjusted return is **57 bps lower** over the three months after becoming constrained (full sample), **1.31%** in 2023–2024; negative-buffer funds **−2.11%** (large-cap growth) and **−1.15%** (all funds) over three months in 2023–2024; across all funds the corresponding three-month effect is **83 bps** (§1). Significant for at least 6 months full sample and at least 12 months in 2023–2024.
- Counterfactual fund portfolios (Table 7, §5.2): constant equity exposure would have added **8.2 bps annualized ($411 million)** in 2023–2024; not rebalancing positions above 5% would have saved **26 bps ($1.51 billion)**.
- Trimming: average reduction of large positions ≈ **12 bps per quarter**, rising to **>20 bps** near the limit (Table 3, §4.1); 59% of constrained funds reduce large positions vs 41% increasing.
- Disposition of `C > 0` stocks across styles: concentrated in large-cap growth, which reached **$30 trillion — more than three quarters of that segment's market cap — by year-end 2024** (Appendix A.6, Figure A.10).

### Independently reproduced

not independently reproduced

### Negative evidence

1. **No cost model of any kind.** The only cost-related statement for the stock strategy is a qualitative assertion that High-C stocks "are unlikely subject to large trading costs because [they] are among the most liquid securities in the market". Fees, spread, slippage, impact, participation, capacity, borrow, financing, turnover and fill are all absent → `data gap`, never zero. Gross/net status of Tables 9 and A.27 is **not stated**.
2. **Full-sample predictability is thin.** In Table 8 Panel A the 1-month and 3-month coefficients are insignificant (t = 1.43, 1.53) and only 6/9/12 months reach 10%/5%/5%. The source itself calls the full-sample strategy alphas "only marginally statistically significant, given the short sample, so they must be interpreted with caution" (§1) and describes the evidence as "only suggestive" / "suggestive evidence … merits further study" (§6.2, §9).
3. **The single-sort High-C alpha is marginal** (t = 1.88 in 2019–2024) and the economically interesting result exists **only in the high-volatility cell**: the High-C / Low-Vol cell alpha is **negative in both periods** (−0.70 and −1.32). The headline "C is priced" claim therefore reduces to a 2×2 interaction on a signal present in only ~269 stocks at end-2024.
4. **The Low-C control leg is itself negative but insignificant** (−2.00 and −2.12, t ≈ −1.1 / −0.9). Part of the apparent spread comes from a control portfolio that is statistically indistinguishable from zero, so a High-minus-Low long-short reading of Table 9 would be double-counting noise.
5. **Headline results use information that is not yet public at formation.** NPORT-P carries a two-month reporting lag, yet Table 8/Table 9 sort on contemporaneous C. Only Table A.27 is point-in-time, and there the single-sort alphas fall to t = 1.71 and 2.19 with only two of four headline alphas significant at 5% — the source's own qualification.
6. **Effectively no out-of-sample test.** The 2023–2024 sub-period is both the estimation window where the constraint binds *and* the window where the effect is strongest; there is no frozen forward window, no walk-forward protocol, and no holdout beyond this split.
7. **Multiplicity is unaddressed.** Five horizons × two panels × two specifications × two C definitions (all-fund / constrained-only / negative-buffer-only / active / passive) × a 2×2 double sort × the 75/5/10 replication, with no multiple-testing correction reported anywhere in the pinned PDF.
8. **Ex-post universe.** The 6,807-stock base is "ever held by these funds during the sample period", not a point-in-time membership list; combined with the above-median-cap and >$5 screens this is an ex-post selection on size and on fund ownership.
9. **The signal is rare and capacity is unknown.** Only 93 → 269 stocks have C > 0; no turnover, no dollar capacity, no participation constraint and no ADV analysis is reported anywhere.
10. **Threshold sensitivity.** Redefining "large position" as >4% and "constrained" as buffer <10% moves the `C > 0` market-cap coverage from ~60% to **78%** (§6.1) — coverage of the signal is a function of choices the regulation does not pin down.
11. **C is explicitly a lower bound** with three stated omissions (float, sub-5% near-threshold positions, 75/5/10-constrained funds) → classical measurement error in the key regressor, whose bias direction under this design is not analysed by the source.
12. **Dependence on the AI/mega-cap episode.** Excluding the Magnificent 7 wipes out **all** full-sample significance in Table A.17 Panel A (all t ≤ 1.61) and leaves only the 2023–2024 main effect; the source presents this as robustness, but it also shows the full-sample result is carried by a handful of names.
13. **The fund-performance evidence is not cleanly identified.** Equation (9) deliberately includes fund but **not** time fixed effects, and the source explains that adding time fixed effects "yields estimates close to zero" — a transparent choice, but it means the underperformance result is time-confounded by construction.
14. **The 75/5/10 extension is weaker** and rests on annual N-CEN filings; the source says the results "must be interpreted cautiously given the short sample" (§8.4).
15. **Causal identification is asserted via a stylised model**, not an instrument or a policy shock; the paper explicitly frames its contribution as "suggestive evidence" (§9).
16. **Label collision hazard in citations:** the PDF contains both a **Table A.17** ("Stock return predictability (excluding the Magnificent 7)", printed on page A-46 inside appendix section A.13) and an **appendix section A.17** ("Implementability of trading strategies", A-59, containing **Table A.27**). §6.2 cites "Table A.17" and §6.3 cites "Appendix A.17"; both are internally correct but the shared `A.17` label is ambiguous and must not be conflated when reusing these numbers.
17. **No independent replication exists**, and the source provides no code, no replication package and no data-availability statement.
18. **Not peer reviewed** (NBER cover statement), with a disclosed co-author relationship of potential relevance whose author-level mapping is `data gap`.

## Falsification plan

Every threshold below is a **research-defined falsification threshold** and every construction choice is **research-proposed**; none of them is specified by the source. The plan is designed so that each test has a pre-declared failure rule that cannot be rescued by retuning.

- **F1 — Independent replication with point-in-time holdings.** Rebuild C from NPORT-P releases using only filings publicly available at formation (respecting the two-month lag, i.e. `C_{s,t−3}` or the exact release date), on a point-in-time stock universe (no "ever held" union), price > $5, above-median cap. **Pass:** the High-C portfolio's annualised Carhart-4 alpha is ≥ 1.5%/yr with Newey–West t ≥ 2.0 in the frozen forward window. **Fail:** t < 1.0 or alpha ≤ 0 → mechanism not replicated.
- **F2 — Cost ladder.** Apply 0 / 5 / 10 / 20 / 30 bp per side plus a 25 bp/yr stock-loan rate on any short leg, at 20% participation cap. **Fail** if net alpha at 10 bp ≤ 0 or if >50% of the gross alpha is erased at 20 bp. (Cost grid is `research-proposed`; the source has no cost model at all.)
- **F3 — Volatility-ablation test (decisive for the mechanism).** Re-estimate the 2×2 double sort with the volatility split replaced by a size split and by a liquidity (ADV) split. **Fail** if the C effect is not specific to compliance-risk (volatility) — i.e. if the High-C alpha is equally large in the low-volatility cell or if the C × volatility interaction loses significance (t < 1.96) in both splits.
- **F4 — Buffer-conditional placebo.** Replace `D^{B<5}` with the same ownership share computed over **unconstrained** funds (buffer ≥ 10%). **Fail** if that placebo predicts returns as well as the constrained share (absolute coefficient within 20% of the constrained estimate).
- **F5 — Threshold grid.** Vary "large position" ∈ {4%, 5%, 6%} and "constrained" buffer ∈ {0–5%, 0–10%, 0–15%}. **Fail** if the sign of the High-C coefficient flips in more than one of the nine cells, or if the result exists only at the 4%/10% setting that maximises coverage.
- **F6 — 1,000-draw circular-shift placebo.** Randomly shift each stock's C series by independent random offsets (preserving autocorrelation), rebuild the portfolios, and form the null distribution of the High-C alpha. **Fail** if the observed alpha does not exceed the 95th percentile of the placebo distribution.
- **F7 — Multiplicity audit.** Benjamini–Hochberg at q < 0.10 across the full reported grid (5 horizons × 2 panels × 2 specs × 2 C definitions × 6 portfolio cells). **Fail** if the headline 3-month 2023–2024 effect does not survive.
- **F8 — Sub-period and regime stability.** Require positive High-C alpha in at least 3 of 4 sub-periods (2019–2020, 2021–2022, 2023–2024, and any frozen forward window ≥ 12 months post-2024-12). **Fail** if all of the effect is confined to 2023–2024 *and* the forward window is flat or negative.
- **F9 — Competing-explanation horse race.** Jointly control for size, book-to-market, momentum, an AI-sector factor, an idiosyncratic-volatility measure, an illiquidity (Amihud) measure, a large-position (non-buffer-conditional) indicator, and analyst forecast dispersion. **Fail** if C's incremental contribution is absorbed (coefficient t < 1.96) once these enter.
- **F10 — Magnificent-7 / concentration audit.** Re-run excluding the top-10 market-cap names each year (rolling, not a fixed 2024 list). **Fail** if full-sample significance disappears entirely, as it already does in the source's own fixed-list Table A.17 Panel A.
- **F11 — Turnover and capacity audit.** Measure realised one-way turnover of the monthly-formation/one-year-hold portfolio and cap positions at 10% and 20% of ADV. **Fail** if turnover exceeds 100%/yr at the single-sort level or if net alpha at the cap is non-positive.
- **F12 — Transport / generalisation.** Apply the same buffer logic to a non-U.S. regime (e.g. UCITS 5/10/40, as the source itself proposes) or to index-cap events (S&P June 2024, Russell March 2025). **Fail** if the direction reverses outside the U.S. 2023–2024 window.

Action on failure: mark the mechanism `falsified-in-our-tests` for the failing axis only, keep the record research-only, and do not promote to the candidate pool.

## Crypto portability

**unproven.**

The mechanism depends on a specific, non-portable institutional fact: U.S. Internal Revenue Code §851(b)(3) diversification tests binding on Regulated Investment Companies, measured from SEC NPORT-P filings. None of this exists in crypto:

- There is no RIC-style 50/5/10 test, no NPORT-P equivalent, and no statutory long-position cap on crypto fund vehicles; on-chain holdings are transparent but no comparable aggregate "buffer" statistic is defined or published.
- The signal's universe (largest U.S. common stocks by market cap, >$5, above-median cap) has no crypto analogue; "mega-cap" crypto assets are a handful of names with 24/7 pricing, no factor-model literature with agreed market/size/value/momentum factors, and no established Carhart-style daily factor library for risk adjustment.
- Long-side constraints in crypto arise from different frictions (index-product mandates on futures ETFs, exchange position limits, custody concentration) that the source never analyses; whether any of them produces the same underpricing channel is an open hypothesis, not evidence.
- Execution differences are material and unaddressed by the source: 24/7 sessions and candle boundaries, funding on perpetuals, mark/index price, venue fragmentation, borrow/short availability and liquidation mechanics are all absent.

Possible future adaptation (explicitly **research-proposed**, untested): construct an analogous "constrained-weight share" for crypto index products (e.g. futures-ETF or index-fund concentration caps) and test whether their forced underweights predict relative returns. Until such a test exists, portability is `unproven`.

## Limitations

Markers used: `underspecified`, `data gap`, `not independently reproduced`, `unproven`, `ex-post selection`.

- **Short, regime-locked sample:** NPORT-P starts September 2019; the constraint only becomes meaningfully binding in 2023–2024. The source itself: "our sample period is short and our findings should be interpreted with caution" (§9).
- **`data gap` — execution layer:** no fees, spread, slippage, impact, participation, capacity, borrow, financing, latency, fill model, or turnover anywhere in the pinned PDF; gross/net status of the strategy alphas is not stated.
- **`data gap` — reproducibility:** no code, no replication package, no data-availability statement; NPORT-P/CRSP/Compustat are proprietary or semi-public inputs.
- **`data gap` — author-level disclosure mapping** for the Vanguard-related views disclaimer.
- **`underspecified` — timestamp/timezone** of the month-end formation instant, and the exact trade-price convention (close vs next open) for the monthly sorts.
- **`underspecified` — rebalance implementation** for one-year holds built from monthly sorts (cohort overlap, partial rebalances, treatment of names whose C drops to zero mid-hold).
- **`ex-post selection` — universe** defined as stocks ever held by sample funds, plus a size/price screen; no point-in-time membership reconstruction.
- **Measurement error:** C is an acknowledged lower bound; sensitivity to the 4%/5%/6% and buffer-cut-off choices is documented but not solved.
- **Multiplicity:** many horizons, panels, specifications and portfolio cells with no correction.
- **Mechanism identification** rests on a stylised model plus pattern correlations, not an exogenous shock.
- **`not independently reproduced`** for every number in the Evidence section.
- **`unproven`** for crypto portability and for any period after 2024-12.
- **Not peer reviewed**; working-paper status with a disclosed co-author relationship.

## Implementation status

`implementation_status: not-implemented`.

No implementation exists in our research stack. Nothing has been built, no NPORT-P pipeline has been constructed, no portfolio has been simulated, and no Paper, Testnet or Live verification of any kind has occurred. This record is a normalised research capture of a third-party working paper only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record in this repository does **not** mean it passed Research Intake Review, entered Hermes Wiki Brain, entered the production candidate pool, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, is profitable, is validated alpha, or is approved for implementation, paper trading, testnet, or live trading. None of those steps has happened.

## Related Wiki records

Pre-write `kb_search` in Hermes Wiki Brain returned **no** page for `fund portfolio concentration limits index concentration stock returns` that is mechanism-adjacent (four results, all unrelated portfolio-construction records), **zero** results for `13F institutional ownership passive index flows return predictability`, **zero** for `constrained ownership share long-side constraint underpricing disagreement`, **zero** for `analyst dispersion disagreement equity return predictability`, and **zero** for `constrained ownership`. Only one verified, mechanism-adjacent page was returned by `index reconstitution rebalancing price impact equity`:

- [[quant/sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13]] (forced-flow / index-related price pressure family)

No other Wiki link is asserted; none was fabricated.

## Sources

- Pastor, L., Sikorskaya, T., & Wang, J. (2026). *The Hidden Cost of Stock Market Concentration: When Funds Hit Regulatory Limits*. NBER Working Paper 35007. DOI: https://doi.org/10.3386/w35007 — landing page https://www.nber.org/papers/w35007 (fetched 2026-09-26, HTTP 200; Issue Date March 2026, Revision Date September 2026).
- Pinned full text: https://www.nber.org/system/files/working_papers/w35007/w35007.pdf — 11,971,499 bytes, SHA-256 `543b928e2aba2936c3a714cf31180e9c6fc3f2519615e95ef5241915fd19122a`, 140 pages, downloaded and read 2026-09-26. All quantitative claims above trace to this file: §1, §2.2–2.3, §3.1, §3.4 (Table 2), §4.1 (Table 3), §5.1 (Table 6), §5.2 (Table 7), §6.1–6.4 (eq. 17, 18, 19; Tables 8, 9), §7.3, §8.4, §9, Appendix TOC, Appendix A.1, A.6, A.13–A.17 (Tables A.17, A.27).
- Cited-by-the-source references used only for mechanism framing (not as independent evidence here): Miller, M. (1977), *Journal of Finance*; Carhart, W. (1997), *Journal of Finance*; Diether, Malloy & Scherbina (2002), *Journal of Finance*; Chen, Hong & Stein (2002); Blume & Keim (2017); Chen (2025); Jiang, Vayanos & Zheng (2025); McCrary (2008); Davis & Haltiwanger (1992).
