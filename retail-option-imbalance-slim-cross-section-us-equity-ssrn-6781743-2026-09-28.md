---
schema: strategy-research-record-v1
title: "Retail call-option SLIM imbalance cross-section of U.S. stock returns (daily decile long-short, top-200 SLIM-volume universe, gross of all costs) - SSRN 6781743, November 2019 to June 2021"
created: 2026-09-28
updated: 2026-09-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - us-equity
  - cross-sectional
  - options
  - retail-flow
  - transaction-costs
status: research-only
confidence: medium
source_as_of: 2026-05-17
sources:
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6781743
  - https://doi.org/10.2139/ssrn.6781743
  - "https://github.com/PeterLiu-Quant/Sanity_check/tree/8b2afbbb1e5f6b4fb5d6230253a0955e48b27e1c"
  - https://www.sikorskaya.net/data/
  - https://doi.org/10.1111/jofi.13285
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Reference counts: the SSRN landing read 2026-09-28 shows a heading '0 References' and a heading '0 Citations' while the pinned PDF prints 20 numbered reference entries - unreconciled."
  - "Version/date: the PDF first page prints 'This version: May 17, 2026' and 'First posted: May 17, 2026' and the landing prints 'Date Written: May 17, 2026', but the same landing prints 'Posted: 22 May 2026' - unreconciled."
  - "Test statistic: PDF Table 3 labels the headline long-short statistic 'Newey-West t-statistic (5 lags) +2.26' while the pinned replication code computes that long-short t-statistic as mean / (sd / sqrt(N)) (sanity_check.py, ls_tstat) and 25.75 / (232.75 / sqrt(416)) = 2.2565; HAC appears in the committed script only for the Fama-MacBeth and FF6 regressions, never for the long-short t-statistic - unreconciled."
  - "Robustness claim: the abstract states the signal 'survives the exclusion of meme tickers (post-exclusion t = 1.84)' while t = 1.84 is below the conventional 5% critical value 1.96; the survival criterion actually used is the source's own 50% t-stat-dropoff rule (PDF Table 6 note) - unreconciled."
  - "Pre-registration: PDF Table 6 note states 'The pre-registered threshold for failure was a t-stat dropoff of more than 50%' while the source's own README caveat 6 states the thresholds 'were set after one exploratory run' and 'are not strictly pre-registered in the AEA RCT sense' - unreconciled."
  - "Signal timing: the paper and README describe the signal as 'lagged one trading day' while the committed code applies groupby(ticker).shift(1) to a frame that has already been filtered by slan_vol >= 50 and de-duplicated, so the lag is the previous surviving observation and can span more than one trading day - unreconciled."
  - "Observation counts: PDF Section 3.2 states '583,067 stock-days remain across 5,509 unique tickers' after filtering while PDF Table 1 reports count 582,752 for the same filtered sample (difference 315) - unreconciled."
  - "Reproduction path: the README instructs running 'python cell10_diagnostics.py' for the FF6 / subsample / meme-exclusion diagnostics, but no cell10_diagnostics.py exists in the pinned tree (18 paths at commit 8b2afbbb); those diagnostics live inside sanity_check.py, yet output/diagnostic_summary.csv is committed - unreconciled."
  - "Decision-threshold reporting: README states 'Current results: T1-T3 PASS, T4 WARN ... D2 mechanically FAIL but economically PASS' while the committed CSVs record sanity_summary.csv T4 = False (1d +20.2 -> 5d +51.9) and diagnostic_summary.csv D2 = False (boom t = +1.37); the paper's Section 5.2 presents the same split as supportive of subsample stability - unreconciled."
---

# Retail call-option SLIM imbalance cross-section of U.S. stock returns (daily decile long-short, top-200 SLIM-volume universe, gross of all costs)

## Provenance

Primary source (identity of every claim in this record):

- SSRN landing: `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6781743`, DOI `10.2139/ssrn.6781743`.
- Title exactly as printed on the PDF first page and on the SSRN landing: **"Retail Option Imbalance and the Cross-Section of Stock Returns"** (identical in both places; no title variant).
- Author: **Zijun Liu**, sole author, printed on the PDF first page as `Zijun Liu*` with footnote `Master of Financial Management, Australian National University. Email: Zijun.Liu@anu.edu.au.` The SSRN landing lists a single author with affiliation `Australian National University (ANU), Research School of Finance, Actuarial Studies and Applied Statistics, Students`. No co-authors in either place. No ORCID printed - `data gap`.
- Version/date: PDF first page `This version: May 17, 2026` and `First posted: May 17, 2026`; SSRN landing `Date Written: May 17, 2026` and `Posted: 22 May 2026` (recorded in `contradictions`).
- Publication status: **SSRN working paper, no journal, no peer-review statement.** The PDF footnote states `This is preliminary work in progress; comments are welcome.` and the replication README badge reads `Status: Working Paper`. Landing shows no journal and no peer-review claim, so publication status is **working paper, not stated to be peer reviewed**.
- Landing statistics read in a browser session on **2026-09-28** after the Cloudflare interstitial cleared: `13 Pages`, `Posted: 22 May 2026`, `301` downloads, `618` abstract views, heading `0 References`, heading `0 Citations`, license `The copyright holder has granted SSRN a license. All rights reserved. No reuse allowed without permission.`, JEL `G12, G14, G40`, keywords `retail investors, options, cross-sectional return predictability, asset pricing`, related alert series `Capital Markets: Asset Pricing & Valuation` and `Econometric Modeling: Capital Markets - Asset Pricing`.
- Pinned PDF: retrieved **2026-09-28** from the SSRN delivery pattern `Delivery.cfm/6781743.pdf?abstractid=6781743&mirid=1` using cookies from the cleared browser session; **283,908 bytes**, **13 pages**, **SHA-256 `eaacd2b822e0aedb407b58ad75f3da618b28d98bcdd2c997220c959303244709`**, `%PDF-1.5`; text-extracted page by page with `pypdf 6.11.0` to **28,829 characters** and all 13 pages read (Sections 1-7, Tables 1-6, the equation block, and the 20-entry reference list). No presigned or session-bound URL is stored anywhere in this record.
- Replication hook named by the source (PDF footnote 1): repository **`https://github.com/PeterLiu-Quant/Sanity_check`**, pinned here at full commit SHA **`8b2afbbb1e5f6b4fb5d6230253a0955e48b27e1c`** (HEAD of `refs/heads/main` observed 2026-09-28 via `git ls-remote`; commit author date `2026-05-17T12:21:01Z`, commit message `Rename .gitignore.txt to .gitignore`). Tree at that commit contains exactly 18 paths: `sanity_check.py` (753 lines, 32,606 bytes, SHA-256 `331beb05d5c0916699d014834084e42086e34d7be554ff8b3efdc74d591a1e8b`), `README.md` (10,033 bytes), `requirements.txt`, `LICENSE` (MIT), `output/sanity_summary.csv` (173 bytes), `output/diagnostic_summary.csv` (151 bytes), `output/tables/.gitkeep`, `output/figures/.gitkeep`, `data/raw/.gitkeep`, `data/processed/.gitkeep`. **`data/raw` and `data/processed` hold only `.gitkeep`, so no input data is committed**; `cell10_diagnostics.py`, which the README tells the reader to run, is absent (recorded in `contradictions`).
- Underlying data named by the source: the public **Bryzgalova-Pavlova-Sikorskaya (BPS) SLIM release of September 2023**, file `Retail trading in options sep23.dta`, downloaded from `https://www.sikorskaya.net/data/`; source-reported shape **2,774,260 observations at ticker x option-type x date, 2019-11-04 to 2021-06-30**, with variables `slan imb` (count), `slan vimb` (volume-weighted), `slan dvimb` (dollar-volume-weighted), `slan vol` (total SLIM contract volume) and PERMNO included per PDF Section 3.2. The README states the file is **not redistributed** in the repo in compliance with the BPS replication-package license.
- Prices: **Yahoo Finance** through `yfinance`, `auto_adjust=True`, using the adjusted `Close` column (visible only in the pinned code, not stated in the PDF - the paper says only "Stock returns come from Yahoo Finance"). Factors: **Kenneth French data library** (Fama-French five factors plus the Carhart/Carhart-style momentum factor, PDF Section 5.1).
- Sample periods: headline portfolio **2019-11-05 to 2021-06-30, N = 416 trading days** (PDF Table 3); retail-boom subsample **2020-03-01 to 2021-03-31, 274 days**; surrounding period **142 days** (PDF Table 5); SLIM file itself **2019-11-04 to 2021-06-30** (PDF Section 3.1).
- Universe: **top 200 tickers by total SLIM volume** out of **5,509 unique tickers** in the filtered SLIM file, of which **174** merge with Yahoo prices (26 dropped as delisted, acquired or renamed), giving **66,814 stock-days** (PDF Section 3.2, README).
- Transaction-cost treatment (read at Methods level: PDF Section 3 "Data and Signal Construction", Section 4 "Headline Cross-Sectional Predictability", Section 5 "Robustness", Section 7 "Conclusion"; plus the pinned README caveat list and all 753 lines of the pinned `sanity_check.py`): the paper contains **no** mention of transaction cost, fees, commission, bid-ask spread, slippage, turnover, borrow, latency, fill or participation - a word scan of the full extracted PDF text returns only the unrelated uses of "spread" (long-short spread) and "zero-commission brokerages" (background on retail adoption). The README states explicitly: **"No transaction-cost adjustment. The 232 bps/day standard deviation implies a strategy with high turnover; net-of-cost alpha will be much lower."** and names the Jensen-Kelly-Malamud-Pedersen (2026) implementable-frontier framework as planned v2 work. The committed code contains **no** cost parameter at all (its only "cost" matches are the comments "what factor is absorbing the raw spread" and "raw spread is mostly known factors / meme / boom artifact"). Conclusion: results are **gross, cost treatment explicitly unmodeled by the source**, and every cost/turnover/fill quantity is a `data gap` that must never be read as zero.

Repository-wide source-identity dedup before writing (hidden-inclusive, `rg -uuu` across the whole checkout including `.mimo-worktrees/`, `.agents/`, `.hermes/`, `.git/` and `coverage_manifest.csv`): `6781743`, `Retail Option Imbalance`, `Zijun Liu`, `PeterLiu-Quant`, `Sanity_check`, `sikorskaya`, `single-leg-auction`, `slan imb` / `slan_imb` and `retail option pressure` all returned **zero matches** (exit 1); a positive-control search for `novy-marx` in the same session returned matches (exit 0), so the search was live. A second pattern set (`Bryzgalova`, `retail trading in options`) matched only three existing records that cite *other* Bryzgalova papers (the 2023 SDF/Bayesian model-averaging paper, the 2025 43/45-characteristic reference panel) plus their worktree copies - none uses retail option flow as a signal and none shares this source identity. `git log --oneline -20` was consulted only as a convenience glance and does not by itself satisfy dedup. Wiki Brain `kb_search` (read-only) returned **0 pages** for `Bryzgalova retail trading options wholesalers SLIM` and **0 pages** for `retail investor attention lottery preference options`.

## Economic mechanism

### Source-reported

The author's stated rationale (PDF Sections 1, 2 and 6):

- Structural background: since 2019, retail investors facilitated by zero-commission brokerages and payment for order flow account for **over 60% of options market volume**, citing Bryzgalova, Pavlova and Sikorskaya (2023).
- Two competing literature views are set up: retail option traders as overconfident, attention-driven lottery buyers who lose on average (cited: BPS 2023; Bogousslavsky and Muravyev 2025, who the source says find retail traders lose roughly **4-5% per trade**), versus unsophisticated traders who may concentrate in informed bets and collectively transmit private information (cited: Pan and Poteshman 2006; Johnson and So 2012; Hu 2014). These generate **opposite cross-sectional predictions**: reversal/noise versus continuation.
- Identification: SLIM (single-leg-auction) trades are wholesaler-routed price-improvement auction executions shown by BPS to be dominated by retail orders; the source takes the public SLIM aggregates as inputs and asks whether **cross-sectional differences** in retail option imbalance predict stock returns, regardless of whether the marginal retail trade is profitable.
- Three candidate mechanisms are laid out in Section 6 and the source **does not adjudicate between them**:
  - **(H-A) Dealer gamma hedging.** Retail call buying leaves market makers short gamma, forcing delta-hedging purchases that push the stock up until the hedge unwinds; predicts same-day impact with reversal within days. The source judges the observed decay from h = 2 to h = 10 "slower than a pure gamma-unwind story predicts".
  - **(H-B) Informed retail.** Leverage-motivated private information expressed in calls; predicts multi-day drift with **no** reversion. The source states the monotone decline from h = 2 to h = 10 is "hard to reconcile with H-B as the dominant mechanism".
  - **(H-C) Attention / lottery preference.** Salient stocks bought via short-dated OTM calls push prices above fundamentals and arbitrageurs slowly correct; predicts overshoot then partial reversal. The source calls this "the interpretation most consistent with all four pieces of evidence".
- The source states that **decisive discrimination requires the option maturity dimension** and that the public SLIM sample stops in June 2021, almost a year before the May 2022 0DTE regime shift, so the mechanism question is explicitly **left open** ("a sharp test must await an extension of the SLIM measure", "Work on these extensions is in progress").
- The paper's contribution claim is framed as an empirical cross-sectional fact, not a causal or mechanism result.

### Research interpretation

- Hypothesized mechanism in falsifiable form: **retail-identified call-option buying pressure, measured one day earlier, forecasts the cross-section of U.S. single-stock returns** because retail attention/lottery demand temporarily overpays for the underlying via delta-hedging and demand spillover, and the resulting price overshoot is partially corrected over the following two weeks.
- Component roles, normalized:
  - Signal: call-side SLIM imbalance (`slan imb` in [-1, +1]) of the previous eligible observation.
  - Regime filter: **none** - the source runs a single unconditional sample and only post-hoc subsample splits.
  - Entry layer: daily equal-weight decile sort, long D10 / short D1, rebalanced every trading day.
  - Risk / exit: **none stated** - there is no stop, no volatility targeting, no position limit and no stated holding constraint other than the daily re-sorts; the h-horizon analysis is diagnostic, not an exit rule.
  - Friction layer: absent from the source entirely; the source itself concedes in the README that net-of-cost alpha "will be much lower".
- Live competing explanations this record does not dismiss: **dealer gamma hedging (H-A)**, **informed retail (H-B)**, **generic high-beta/growth-tilt exposure of the top-200 SLIM-volume universe** (Table 2 shows every decile with a large positive raw mean, so the universe itself is a momentum/growth basket in a bull window), **selection on the signal's own activity** (universe chosen by total SLIM volume), and **survivorship from the Yahoo price merge**.
- Research interpretation of the source's own diagnostics: the combination of significant alpha, negative market beta (-0.342) and negative momentum loading (-0.205) is *consistent with* an attention/lottery mispricing channel, but the same combination is equally produced by a small equal-weight book of liquid high-volatility names that happens to lean against the market and against prior winners; the source's own H-A/H-B/H-C discussion leaves all three live and its decisive test needs data it does not have.

## Signal

Everything in this section is source-reported unless explicitly marked `research-proposed` or `data gap`.

- **Signal definition (PDF Section 3.2, Equation 1):** `ROP(i,t) = slan imb(i,t)^(call)`, the count-based single-leg-auction imbalance on **call rows only**, bounded in [-1, +1], positive when retail SLIM call buy volume exceeds sell volume. Call side chosen by the source for (i) cleaner interpretation of bullish retail bets, (ii) much larger call-side SLIM volume, (iii) consistency with BPS's own characterization of retail option preferences.
- **Liquidity filter (code, Cell 2):** keep rows with `slan_vol >= 50` contracts (source comment: "BPS use roughly $1M cum volume; we'll be looser"), then keep `option_type == 'C'`.
- **De-duplication (code):** if a ticker-date appears more than once, keep the row with the largest `slan_vol`.
- **Cross-sectional transforms (code, applied per trade date on the filtered panel):** winsorize at the 1st and 99th percentile (`rop_w`), then standardize to zero mean and unit variance (`rop_z`). The portfolio sort uses the **winsorized** series `rop_w_lag1`; the Fama-MacBeth regression uses the **standardized** series `rop_z_lag1`. The PDF text describes the sort as "on lagged `slan imb`" without stating which transform feeds the deciles - `underspecified`.
- **Formation timestamp / lookback:** the code comment states `ROP measured at end of day t-1 predicts return on day t`, implemented as `groupby(ticker)[...].shift(1)` on the already-filtered frame, then an inner join on ticker and date, then `dropna` on return and lagged signal. Because the shift is taken **after** the `slan_vol >= 50` filter and the de-duplication, the "1-day" lag is the previous **surviving observation**, which can be several trading days earlier for thin names (see `contradictions`). Timezone, session boundary and the availability lag of SLIM trade-date aggregates are **not stated in source** - `data gap`.
- **Universe construction (code, Cell 3):** rank all tickers by total `slan_vol` and take `nlargest(200)`; then merge with Yahoo prices; 174 survive. Selection is therefore **on the signal variable's own volume**, using the full-sample total (an ex-post, in-sample universe choice).
- **Portfolio construction (code, Cell 7):** each trade date, `pd.qcut(rop_w_lag1, 10, labels=False, duplicates='drop') + 1`; equal-weighted mean return per decile; **long-short = D10 - D1**; `ls_mean_bps = ls.mean() * 1e4`; Sharpe = `ls.mean()/ls.std()*sqrt(252)`; the printed t-statistic is `ls.mean()/(ls.std()/sqrt(len(ls)))`.
- **Rebalance / holding period:** **daily**, fully re-sorted each trading day; no position limits, no turnover control, no bid-ask or participation constraint.
- **Horizon diagnostics (PDF Table 3):** cumulative long-short returns at h = 1, 2, 3, 5, 10 trading days built from forward returns `pct_change(h).shift(-h)`; these are diagnostics, not an exit rule.
- **Fama-MacBeth (PDF Section 4.2, Equation 2):** daily cross-sectional regressions of return on lagged standardized ROP; time-series average slope **+21.85 bps per 1 cross-sectional SD**, Newey-West t **+2.14**, mean cross-sectional R2 **1.29%** over 416 days.
- **Parameters:** `slan_vol >= 50`, 1%/99% winsorization, 10 deciles, top-200 universe, 174 merged tickers, lag of one surviving observation, daily rebalance. All are **source-fixed (code-visible)**; none is research-proposed by this record.
- **Reconstructability:** the signal is reconstructable **only if** the BPS September 2023 `.dta` file is obtained from `sikorskaya.net` under its license (not in the repository) and the exact universe/dedup/lag sequence above is copied. Missing or `underspecified`: tie handling when `duplicates='drop'` yields fewer than 10 buckets, the transform fed into the sort, the session/timezone convention, whether Yahoo's `auto_adjust=True` close (code) or an unadjusted close (paper text) is intended, and any sizing or short-leg rule.

## Required data

- **Instrument / universe:** U.S. listed single-stock equities; first pass restricted to the top 200 tickers by SLIM volume (174 with usable prices) out of 5,509 tickers present in the SLIM file. Market type: cash equities for the portfolio, with the signal originating in **listed equity options** (single-stock calls).
- **Signal data:** BPS SLIM retail-identified option trade aggregates, ticker x option-type x date, variables `slan imb`, `slan vimb`, `slan dvimb`, `slan vol`, plus PERMNO (present in the file per PDF Section 3.2 but **not used** in this first pass - the source says a CRSP/PERMNO merge "is the natural next step"). Source: `https://www.sikorskaya.net/data/`, September 2023 release; license forbids redistribution - `data gap` for anyone who cannot obtain it.
- **Prices:** daily OHLCV-equivalent close series from Yahoo Finance via `yfinance` with `auto_adjust=True`; the paper does not state the adjustment convention - `underspecified` (resolved only by reading the pinned code).
- **Factors:** Fama-French MKT-RF, SMB, HML, RMW, CMA plus momentum from Kenneth French's data library (daily or monthly frequency is **not stated in source** - `data gap`; the regression is run on daily portfolio returns, so the factor frequency actually used is `underspecified`).
- **Point-in-time / availability:** SLIM trade-date aggregates are assumed to be usable with a one-day lag; publication timestamp, timezone and any vendor delay are **not stated in source** - `data gap`.
- **Missing data / delisting:** 26 of the top 200 tickers are dropped because they were delisted, acquired or renamed during the window (FB -> META, APHA -> Tilray, FEYE acquired are the source's examples); no delisting return, no trading-halt handling and no stale-price rule is specified. The README calls this survivorship bias from Yahoo and says CRSP via WRDS is v2 work.
- **Not applicable to this signal:** funding, mark/index price, open interest, order book, trade aggressor side in the underlying, options surface/Greeks - the source uses only daily option-flow aggregates and daily equity closes. Option maturity, strike and expiry are **deliberately not used**: the source aggregates over all maturities and flags a maturity-sliced version as future work.

## Execution assumptions

Source-reported:

- **Signal-to-order timing:** the source's only timing statement is that the signal from day t-1 is matched to the return on day t. The execution session, same-bar versus next-bar convention, order type and fill price are **not stated in source** - `data gap`.
- **Order type / fill model / latency / partial fills / participation cap:** **`data gap`** - none of these words appears with operational content anywhere in the pinned PDF or the pinned code.
- **Fees, commission, spread, slippage, market impact:** **`data gap`.** The paper reports no cost of any kind; the README states the results are unadjusted and that "net-of-cost alpha will be much lower"; the code contains no cost term. Reported figures are therefore **gross**.
- **Turnover:** **not reported** - `data gap`. The README asserts only qualitatively that the 232.75 bps/day standard deviation "implies a strategy with high turnover". No one-way or round-trip turnover number exists in the paper, the README or the two committed CSVs.
- **Borrow / shorting:** the strategy **shorts the D1 decile** every day. Borrow availability, borrow fee, recall risk, short-sale restrictions and the treatment of short proceeds and margin are **not stated in source** - `data gap`, never assume free or available borrow.
- **Leverage / margin:** not stated - `data gap`; the construction is written as a unit-notional long-short with equal weights inside each decile.
- **Capacity / liquidity:** not quantified anywhere; the universe (top-200 SLIM-volume names) is liquid by construction but no ADV, participation or AUM constraint is given - `data gap`.
- **Taxes:** not mentioned - `data gap`.
- **Distinction:** every performance number in this record comes from a gross, cost-free simulation on a 416-day window with a 174-ticker universe. Nothing in the source supports the word "tradable"; the source's own README says net-of-cost alpha will be much lower and defers cost work to v2 (naming the Jensen-Kelly-Malamud-Pedersen (2026) implementable-frontier framework, cited by the source and **not read for this record**).

## Evidence

### Source-reported

All figures below are third-party claims from the pinned SSRN PDF (page/table provenance given) and the pinned repository's committed outputs. Nothing here has been independently reproduced.

**Signal descriptives (PDF Table 1, after `slan_vol >= 50`, call rows, 2019-11-04 to 2021-06-30):** `slan imb` count 582,752, mean -0.075, SD 0.331, median -0.066, Q3 +0.091, max +1.000; `slan vimb` count 582,752, mean -0.061, SD 0.460, median -0.056, Q3 +0.204; `slan dvimb` count 582,752, mean -0.042, SD 0.489, median -0.039, Q3 +0.266. Table 1 notes: 5,509 unique tickers on the SLIM side, analysis sample 174 tickers. PDF Section 3.3 additionally reports an average daily cross-sectional SD of `slan imb` of **0.132** and average interquartile range **0.140** in the merged panel. The negative cross-sectional mean is attributed by the source to BPS's finding that retail investors are net sellers of options on average.

**Decile sort (PDF Table 2, equal-weighted daily mean returns, sorted on lagged `slan imb`, bps/day):** D1 +29.59, D2 +23.01, D3 +22.83, D4 +14.28, D5 +24.25, D6 +22.93, D7 +27.50, D8 +19.59, D9 +37.35, D10 +55.34. Table 2 note: "The sort is not strictly monotone but D10 substantially exceeds D1, and the upper deciles (D9-D10) show a clear lift."

**Headline long-short (PDF Table 3, daily-rebalanced D10-D1, equal-weighted within decile):** sample **2019-11-05 to 2021-06-30**, trading days **N = 416**, mean **+25.75 bps/day**, standard deviation **232.75 bps/day**, statistic labelled "Newey-West t-statistic (5 lags)" **+2.26**, annualized Sharpe **1.76**; cumulative long-short at h = 1 **+20.25 bps**, h = 2 **+61.77 bps**, h = 3 **+53.50 bps**, h = 5 **+51.91 bps**, h = 10 **+49.36 bps**. The note states the signal is lagged one trading day and cumulative returns are computed from t to t+h where day t is the day after portfolio formation. PDF Section 4.1 adds t-statistics for the horizons: h = 2 **t = 2.50**, h = 10 **t = 1.19**, and describes the h=10 value as "roughly 80% of the h = 2 peak" that "has lost statistical significance".

**Fama-MacBeth (PDF Section 4.2):** average slope **+21.85 bps** per one cross-sectional-SD move in ROP, Newey-West t **+2.14**, mean cross-sectional **R2 = 1.29%**, N = 416 days. The committed `output/sanity_summary.csv` records `T2,True,"FM beta = +0.002185, t = +2.141"` - 0.002185 in return units is 21.85 bps, identical to the paper.

**Fama-French six-factor regression (PDF Table 4; time-series regression of the daily long-short on FF5 + momentum, HAC standard errors with 5 lags, sample 2019-11-05 to 2021-06-30):** Alpha **+26.82 bps/day (t = 2.52)**, MKT-Rf **-0.342 (t = -2.63)**, SMB **+0.052 (0.23)**, HML **-0.365 (-2.09)**, RMW **+0.409 (1.80)**, CMA **+0.116 (0.30)**, MOM **-0.205 (-1.66)**, **R2 = 0.103**, N = 416. Committed `output/diagnostic_summary.csv` records `D1,True,"FF6 alpha = +26.82 bps, t = +2.524"`.

**Subsample stability (PDF Table 5):** full sample 416 days, +25.75 bps, t +2.26, Sharpe 1.76; retail boom 2020-03 to 2021-03, 274 days, **+21.91 bps, t +1.37, Sharpe 1.31**; surrounding period, 142 days, **+33.16 bps, t +2.61, Sharpe 3.48**. Committed CSV: `D2,False,"Boom t = +1.37, Quiet t = +2.61"`.

**Meme-stock exclusion (PDF Table 6):** full sample +25.75 bps / t 2.26 / Sharpe 1.76; meme tickers excluded **+20.92 bps / t 1.84 / Sharpe 1.44**; t-stat dropoff **-18.2%** against a stated failure threshold of more than 50%. Excluded list (20 named, 14 present in the top-200 sample): AMC, BB, BBBY, CLOV, GME, KOSS, MVIS, NAKD, NOK, OCGN, PLTR, RIDE, RKT, SNDL, SPCE, TLRY, WISH, WKHS, EXPR, GEVO. Committed CSV: `D3,True,"Full t = +2.26, No-meme t = +1.84"`.

**Pre-registered thresholds published by the source (README "Pre-Registered Decision Thresholds", printed by `THRESHOLDS` and `DIAG_THRESHOLDS` in `sanity_check.py`):** T1 cross-sectional IQR of ROP > 0.05; T2 Fama-MacBeth t > 2.0 and beta > 0; T3 long-short mean >= 3 bps/day and Sharpe >= 0.8; T4 signal does not exhibit pure continuation through h = 5; D1 FF6 alpha >= 5 bps and t >= 2.0; D2 signal t >= 1.5 in **both** subsamples; D3 meme-exclusion t-stat dropoff < 50%. Committed `output/sanity_summary.csv`: `T1,True (xs IQR mean = 0.1402)`, `T2,True`, `T3,True (LS mean = +25.75 bps, Sharpe = 1.756)`, `T4,False (1d -> 5d cum: +20.2 -> +51.9)`.

**Source-stated limitations (README "Caveats and Known Limitations"):** (1) Yahoo Finance return source introduces survivorship bias for delisted tickers and dividend-adjustment inaccuracy, with CRSP/WRDS deferred to v2 and the author's preliminary claim that "the headline alpha is unchanged"; (2) the top-200 universe restriction is a "computational convenience", full 5,509-ticker universe deferred to v2 with the author's preliminary claim that the signal "strengthens at the broader universe"; (3) put-side and net (call - put) variants are constructed but not analyzed; (4) the sample stops June 2021 because of the public BPS release; (5) **no transaction-cost adjustment** and "net-of-cost alpha will be much lower"; (6) **the pre-registered thresholds were set after one exploratory run**.

**Comparison claims (PDF Section 4.1):** the source states the +25.75 bps/day magnitude is "roughly four times larger than the equity-side retail order-flow effect documented by Boehmer et al. [2021]"; this is a cross-paper comparison asserted by the source and **not verified** here (Boehmer et al. 2021 was not read for this record).

**Research-computed arithmetic checks of source numbers (inputs are source-reported; the arithmetic is ours, not a reproduction):** 25.75 / (232.75 / sqrt(416)) = **2.2565**; (25.75 / 232.75) * sqrt(252) = **1.7563**; D10 - D1 = 55.34 - 29.59 = **25.75**; 49.36 / 61.77 = **0.799**; 274 + 142 = **416** and (21.91*274 + 33.16*142)/416 = **25.75**; 0.002185 * 10,000 = **21.85 bps**; 583,067 - 582,752 = **315**; mean of D1..D9 = **+24.59 bps/day**. These checks confirm transcription and internal arithmetic consistency only.

### Independently reproduced

`not independently reproduced`

No backtest, no simulation, no data download of the SLIM file or equity prices, and no execution of the authors' code was performed for this record. The only actions taken were: reading the pinned SSRN PDF in full, reading the SSRN landing in a browser session, fetching the pinned repository tree, README, script and two committed CSVs at an immutable commit, reading them, running read-only repository and Wiki Brain dedup searches, and arithmetic cross-checks of printed values. Reading the authors' committed outputs verifies **transcription and internal consistency** of source-reported numbers; it is **not** independent reproduction of the result.

### Negative evidence

1. The headline statistic is marginal: +25.75 bps/day with a t-statistic of +2.26, and the committed code derives that +2,26 from the i.i.d. formula `mean / (sd / sqrt(N))` (25.75 / (232.75 / sqrt(416)) = 2.2565), not from a HAC estimator, despite PDF Table 3 labelling it "Newey-West t-statistic (5 lags)".
2. The window is 416 trading days, about 20 months (2019-11-05 to 2021-06-30), a single COVID-era retail-boom episode; there is no out-of-sample period, no holdout, no walk-forward and no train/test split anywhere in the paper or the code.
3. The universe is selected on the signal's own volume (top 200 by total `slan_vol`, computed over the full sample) and then trimmed to 174 tickers with Yahoo prices, so the investable cross-section is an ex-post, in-sample, 17-name-per-decile book; the 5,509-ticker universe is deferred to v2.
4. Survivorship is explicit: 26 of the top-200 tickers were dropped because they were delisted, acquired or renamed, and no delisting return is used (README caveat 1).
5. The decile sort is not monotone: D1 (+29.59 bps/day) exceeds D2-D8, with D4 the lowest at +14.28; only D9-D10 lift (the source's own Table 2 note).
6. Every decile has a large positive raw mean (D1..D9 average **+24.59 bps/day**, about +123% arithmetic over 416 days), i.e. Table 2 is unadjusted and the universe behaves like a high-growth basket in a bull window; the spread is essentially D10 versus everything else.
7. The retail-boom subsample is not significant: +21.91 bps with t = +1.37 over 274 days, which **fails the source's own D2 threshold** (t >= 1.5 in both subsamples) - `diagnostic_summary.csv` records `D2 = False`.
8. After excluding 14 meme tickers the statistic falls to t = 1.84, below the conventional 1.96, so the abstract's "survives" claim holds only under the source's own 50% dropoff rule.
9. That 50% dropoff rule is called "pre-registered" in PDF Table 6 while the source's README caveat 6 admits the thresholds "were set after one exploratory run" and are "not strictly pre-registered".
10. The horizon test does not meet the source's own T4 criterion: `sanity_summary.csv` records `T4,False` (1d +20.2 -> 5d +51.9, i.e. continuation, not reversal by day 5); the README re-labels this "WARN" and the paper re-labels it "overshooting-correction".
11. The h = 10 cumulative return (+49.36 bps) has t = 1.19 and has lost significance (PDF Section 4.1), so only the first two days carry statistically detectable content.
12. **Zero transaction-cost treatment.** The PDF never mentions cost; the README states results are unadjusted and "net-of-cost alpha will be much lower"; the code has no cost term. A daily full re-sort of two equal-weight deciles in a 174-name universe implies substantial one-way turnover that is never measured - turnover and cost are `data gap`, not zero.
13. The short leg's feasibility is unexamined: no borrow availability, borrow fee, recall, short-sale restriction, margin or short-proceeds treatment is stated - `data gap`; shorting the retail-sell-pressure decile every day for 416 days may be partly or wholly unexecutable.
14. No fill model, order type, execution session, latency, participation cap or market-impact treatment exists anywhere in the source - `data gap`.
15. The paper does not state its return adjustment convention; only the pinned code reveals `auto_adjust=True` on Yahoo's `Close`, so the paper's own text is `underspecified` on a material field.
16. The "one trading day" lag is applied after the liquidity filter and de-duplication, so for thin names the lag spans an unknown number of trading days; the size of this timing distortion is unquantified.
17. No timezone, trading-session or data-availability convention is stated for SLIM trade-date aggregates - `data gap`.
18. The raw data is not in the repository (`data/raw/.gitkeep` only) and cannot be redistributed under the BPS license, so none of the headline numbers can be re-derived without separately obtaining `Retail trading in options sep23.dta` (2,774,260 rows).
19. The documented reproduction path is partly broken: the README instructs `python cell10_diagnostics.py`, which does not exist at the pinned commit, while its output CSV is committed.
20. Specification search is uncontrolled: volume-weighted and dollar-weighted variants, put-side and net variants are computed but not reported, and there is no multiplicity correction anywhere (no Benjamini-Hochberg, no Bonferroni, no model-confidence set).
21. The Fama-MacBeth mean cross-sectional R2 is 1.29% and the FF6 regression R2 is 0.103 - the signal and the risk model explain very little, so the alpha claim rests on 416 daily observations with fragile asymptotics.
22. Factor exposure is not absent as framed: HML -0.365 (t = -2.09) and RMW +0.409 (t = 1.80) are economically meaningful loadings, so the "risk factors absorb essentially none of the spread" claim is stronger than the table supports.
23. Source quality: single-author Master of Financial Management student working paper, self-described as "preliminary work in progress", SSRN landing shows headings `0 References` and `0 Citations`, no journal, no peer-review statement, and the replication README declares "All errors are my own."
24. The mechanism is explicitly undecided by the source: H-A (dealer gamma), H-B (informed retail) and H-C (attention/lottery) all remain live, the decisive maturity-based test needs post-2022 data the source does not have, and the paper's preferred H-C reading is stated as an interpretation rather than a result.

## Falsification plan

All thresholds below are **research-defined falsification thresholds** unless the source itself states the number; every operational rule not present in the source is labeled `research-proposed`.

- **F1 - Frozen forward replication.** `research-proposed` rebuild of the ROP decile long-short with point-in-time data on the frozen forward window starting **2026-10-01** for at least 12 months. **Fail** if forward mean spread <= 0 or forward t < 1.64 (research-defined).
- **F2 - Number reproduction gate.** Independently obtain the BPS SLIM file, re-run the pinned script and reproduce Table 3. **Fail** the headline record if the mean differs from 25.75 bps/day by more than **0.50 bps**, or the Sharpe differs from 1.76 by more than **0.05**, or the FF6 alpha differs from 26.82 bps by more than **0.50 bps** (research-defined tolerances).
- **F3 - Cost ladder.** `research-proposed` first measure one-way daily turnover of the two decile legs, then apply a round-trip cost ladder of 0 / 5 / 10 / 20 / 50 bps. **Fail** H4 (implementability) if net Sharpe falls below 0.5 at 10 bps round trip, or net mean <= 0 at any rung at or below 20 bps (research-defined); report turnover as measured, never as zero.
- **F4 - Turnover and capacity audit.** Compute one-way turnover, days-to-fully-turn, and the ADV participation needed to rotate both legs each session. **Fail** implementability if any leg requires more than **10% of its 20-day ADV** in a single session (research-defined).
- **F5 - Statistic audit (targets `contradictions` 3).** Recompute the long-short t-statistic with Newey-West HAC at 5 lags, and also with a stationary block bootstrap (21-day blocks, 1,000 draws). **Fail** the significance claim if the HAC t falls below **1.96** (research-defined).
- **F6 - Universe robustness.** Re-run on the full 5,509-ticker SLIM universe with a CRSP/PERMNO merge including delisting returns, as the source itself proposes. **Fail** the headline if the spread loses significance at 5% or changes sign (research-defined).
- **F7 - Lag-integrity test (targets `contradictions` 6).** Recompute the signal with a strict calendar-aligned previous-trading-day lag (no gap spanning) instead of `shift(1)` on the filtered frame. **Fail** if the spread changes by more than **30%** or t falls below 1.5 (research-defined), because that would show the headline depends on an undocumented timing artifact.
- **F8 - Signal-variant horse race with multiplicity control.** Run `slan imb`, `slan vimb`, `slan dvimb`, put-side and net variants through the same pipeline and apply Benjamini-Hochberg at **q < 0.10** across the five variants (research-defined). **Fail** if only the count-based variant survives selection.
- **F9 - Concentration / leave-one-out.** Recompute the spread dropping each of the ten largest contributors by |weight| and dropping each of the 14 meme names individually; **fail** if any single removal drops t below **1.5** (research-defined).
- **F10 - Placebo null.** 1,000 draws of date-circularly-shifted (and ticker-shuffled) ROP signals through the identical pipeline. **Fail** if the realized +25.75 bps does not exceed the **95th percentile** of the placebo distribution (research-defined).
- **F11 - Factor and style neutralization.** Re-run D10-D1 residualized against FF5 + momentum, plus industry dummies and a beta- and volatility-matched control portfolio. **Fail** if alpha falls below the source's own D1 gate of **5 bps/day with t >= 2.0** (source-reported threshold reused as the failure rule).
- **F12 - Short-leg feasibility.** Verify borrow availability, fee and locate constraints for the D1 names day by day. **Fail** implementability if more than **20% of D1-days are not borrowable** at a fee under 100 bps/year (research-defined).
- **F13 - Out-of-sample / regime split.** With an extended SLIM measure (if it becomes public), test 2022-01 onward, the post-May-2022 0DTE era the source identifies as decisive. **Fail** the mechanism claim if the sign flips or t < 1.96 out of sample (research-defined); this is also the source's own proposed H-A/H-B/H-C maturity horse race.
- **F14 - Two-subperiod stability with holdout.** Split 2019-11-05 to 2020-08-31 (train) and 2020-09-01 to 2021-06-30 (test), `research-proposed` purely as a hygiene split. **Fail** if the later half does not preserve the sign with t >= 1.64 (research-defined).

Action on failure: the record stays `research-only`, `not-implemented`, `not-approved`; a failed F2, F3, F5, F6, F7, F8 or F11 should be reported back to Research Intake Review as grounds for REJECT rather than for retuning.

## Crypto portability

**Unproven.**

- The source tests **only** U.S. single-stock cash equities with U.S.-listed equity options and makes **no crypto claim**. Nothing in the paper or the repository touches digital assets, so portability is a `research-proposed` hypothesis, not evidence.
- The mechanism - retail-identified derivatives flow propagating into the underlying cross-section - is at least *conceivable* in crypto, but the identifying instrument does not port: there is no wholesaler price-improvement-auction channel, no SLIM-equivalent retail classification, and no comparable public retail-flow aggregate. A port would need a `research-proposed` retail proxy (for example small-lot taker buy/sell imbalance on a single venue, or public end-user versus aggregate account flags), which is a materially different data dependency and is `unproven`.
- Instrument mismatch: the source signal is built from **listed options on the underlying**, while the most liquid crypto derivatives are perpetuals; options open interest and volume are concentrated in a handful of expiries and strikes, and Deribit/Binance/CME option universes differ from perp universes. Funding, mark price and liquidation mechanics that govern perp implementations are **absent from the source** and would have to be modeled from scratch.
- Market-structure differences that break a naive port: 24/7 sessions versus U.S. RTH option auctions, venue fragmentation across many exchanges, candle-boundary and timezone conventions, thin single-name (altcoin) option books with wide quoted spreads, borrow/short mechanics on spot versus perp, custody and withdrawal risk, and severe listing survivorship in the token universe.
- If anyone attempts a port, every operational choice (retail proxy, threshold, sort depth, rebalance cadence, cost model) is `research-proposed` until tested; crypto portability is **not** authorization to trade.

## Limitations

- **Source quality:** sole-author SSRN working paper by a Master of Financial Management student, self-described as "preliminary work in progress", landing shows `0 References` and `0 Citations` headings, no journal and no peer-review statement, MIT-licensed replication code with "All errors are my own." Treat every performance figure as an unrefereed third-party claim.
- **Sample:** 416 trading days, 2019-11-05 to 2021-06-30; no holdout, no out-of-sample, no walk-forward, no multiplicity control.
- **Universe:** top-200-by-SLIM-volume selection computed over the full sample (in-sample, endogenous), then 174 tickers with usable Yahoo prices; the 5,509-ticker universe is deferred to v2. `underspecified` for any point-in-time claim.
- **Survivorship:** 26 dropped tickers and no delisting returns; acknowledged by the source as a Yahoo limitation. `data gap`.
- **Costs:** explicitly unmodeled (README caveat 5); turnover never reported; no spread, slippage, impact, latency, participation or fill model. `data gap` - never treat as zero.
- **Shorting:** borrow availability, fees and recall are not stated. `data gap`.
- **Timing:** `shift(1)` after filtering means the stated "one trading day" lag is really "previous eligible observation"; timezone and session conventions are absent. `underspecified`.
- **Sort input:** the PDF does not say whether deciles are formed on raw, winsorized or standardized imbalance; only the code resolves it. `underspecified`.
- **Return convention:** the PDF does not state its price-adjustment basis; only the code's `auto_adjust=True` resolves it. `data gap` at paper level.
- **Reproducibility:** raw data is license-restricted and absent from the repository; the README's `cell10_diagnostics.py` does not exist at the pinned commit; only two 150-175 byte CSVs are committed as evidence of the run.
- **Mechanism:** unresolved by the source (H-A/H-B/H-C all live), with the decisive maturity test requiring data that is not public.
- **Test statistic:** the headline t-statistic's labelling as Newey-West conflicts with the committed code's i.i.d. formula. `contested`.
- **Contested:** this record carries `contested: true` with nine frontmatter contradictions; none has been reconciled and none should be silently resolved downstream.
- **Not independently reproduced.**
- **Incremental-write check:** no existing record in this repository shares this source identity (hidden-inclusive `rg -uuu` returned zero hits for `6781743`, `Retail Option Imbalance`, `Zijun Liu`, `PeterLiu-Quant`, `Sanity_check`, `sikorskaya`, `single-leg-auction`, `slan imb`, `retail option pressure`; positive control `novy-marx` matched); Wiki Brain `kb_search` returned zero pages for the BPS/SLIM retail-options mechanism.

## Implementation status

`implementation_status: not-implemented`.

Nothing has been implemented in our research stack. No SLIM data has been obtained, no option-flow signal ingested, no portfolio constructed, no backtest run, no Qlib full-backtest executed, and no Paper, Testnet or Live workflow touched. This document is a normalized research capture of a third-party working paper plus a reading of its pinned replication repository. The numbers above are source-reported claims with table-level provenance, not our results.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this record in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. It also does not mean the source's nine contradictions have been reconciled, that its t-statistic labelling is correct, or that any cost, turnover, borrow or fill assumption has been verified. Any later adoption or implementation decision must be explicit, separately reviewed, and based on this record plus current sources.

## Related Wiki records

Verified adjacent pages (found via read-only `kb_search`, none shares this source identity):

- [[quant/retail-agent-structured-adverse-timing-contrarian-alpha-2026-09-02]] - adjacent in that both exploit behavioral order-flow predictability from a specific trader class; differs in market (LLM trading agents versus U.S. equity options retail), in instrument and in source identity.
- [[quant/order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12]] - adjacent in that both study whether order-flow imbalance retains predictive power after frictions; differs in horizon (same-day microstructure versus daily cross-section), universe and source identity.
- [[quant/single-name-equity-earnings-iv-crush-bid-ask-falsification-2026-09-13]] - adjacent in that both are single-name U.S. equity options studies with quoted-spread falsification, which this record lacks entirely; different source and different claim.
- [[quant/nuclear-energy-equity-options-short-put-variance-risk-premium-2026-09-02]] - adjacent in that both use listed U.S. equity options; differs in mechanism (selling variance risk premium versus reading retail flow) and in source identity.
- [[quant/crypto-order-flow-online-sgd-microstructure-horizon-cost-falsification-2026-09-13]] - adjacent in that both separate flow predictability from taker-cost reality; differs in market type (crypto spot versus U.S. equities) and in source identity.

No Wiki Brain page for the SLIM / retail option-imbalance mechanism exists yet; searches for the BPS SLIM mechanism and for retail option-attention pages returned zero pages.

Nearest records in this repository (source identity and mechanism differ on every axis; none is a duplicate):

- `common-firm-level-investor-fears-equity-options-cross-section-premium-2026-09-24.md` - different source (arXiv 2309.03968), different signal (PCA of model-free implied variances) and different claim (a common-fear risk premium rather than retail flow predictability).
- `boehmer-retail-equity-flow` style captures do not exist in this repository; the closest equity-side retail-flow discussion is inside `european-2020-short-selling-ban-liquidity-left-tail-institutional-ownership-did-2026-09-22.md`, which is a different source (2020 European short-selling bans) and a different mechanism.
- `fund-50-5-10-constrained-ownership-share-large-equity-underpricing-2026-09-26.md` - shares no source identity; matches only on unrelated wording during the lexical scan.
- Option-flow records such as `spy-options-svi-surface-rv-falsification-adverse-selection-2026-09-12.md` and `option-implied-surface-cremers-weinbaum-skew-crash-regimes-2026-09-02.md` - different sources, different mechanism (volatility-surface relative value versus retail trade identification), different universe.

## Sources

1. Liu, Z. (2026). *Retail Option Imbalance and the Cross-Section of Stock Returns* (Working paper, Australian National University). SSRN abstract 6781743, DOI `10.2139/ssrn.6781743`. Landing `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6781743`, read in a browser session 2026-09-28: `13 Pages`, `Posted: 22 May 2026`, `Date Written: May 17, 2026`, 301 downloads, 618 abstract views, headings `0 References` and `0 Citations`, license "All rights reserved. No reuse allowed without permission.", JEL `G12, G14, G40`.
2. Same paper, pinned PDF retrieved 2026-09-28 from the SSRN delivery pattern `Delivery.cfm/6781743.pdf?abstractid=6781743&mirid=1`: **283,908 bytes, 13 pages, SHA-256 `eaacd2b822e0aedb407b58ad75f3da618b28d98bcdd2c997220c959303244709`**, text-extracted with `pypdf 6.11.0` to 28,829 characters and read in full (Sections 1-7, Tables 1-6, reference list of 20 entries). All quantitative claims in this record trace to those sections and tables.
3. Replication repository named in the PDF footnote: `https://github.com/PeterLiu-Quant/Sanity_check`, pinned at full commit SHA **`8b2afbbb1e5f6b4fb5d6230253a0955e48b27e1c`** (observed 2026-09-28 via `git ls-remote`; commit date `2026-05-17T12:21:01Z`). Files read at that commit: `README.md` (10,033 bytes), `sanity_check.py` (32,606 bytes, SHA-256 `331beb05d5c0916699d014834084e42086e34d7be554ff8b3efdc74d591a1e8b`, 753 lines), `output/sanity_summary.csv` (173 bytes), `output/diagnostic_summary.csv` (151 bytes), `requirements.txt`, `LICENSE`. Every code-level statement in this record (lag construction, filter order, decile assignment, t-statistic formula, threshold dictionaries) comes from those files at that commit.
4. Underlying signal data named by the source: Bryzgalova, S., Pavlova, A., and Sikorskaya, T. (2023), "Retail Trading in Options and the Rise of the Big Three Wholesalers", *Journal of Finance* 78(6):3465-3514, DOI `10.1111/jofi.13285`; public SLIM release of September 2023 at `https://www.sikorskaya.net/data/`, file `Retail trading in options sep23.dta` (2,774,260 rows, 2019-11-04 to 2021-06-30). Cited here as the source's declared data basis; the BPS paper itself was **not** read for this record - `data gap`.
5. Price and factor vendors named by the source: Yahoo Finance via `yfinance` (equity closes) and Kenneth French's data library (Fama-French five factors and momentum). The implementable-frontier cost framework the README names for v2 (Jensen, Kelly, Malamud and Pedersen, 2026) was **not** read for this record - `data gap`.

No Wiki Brain write, no Kanban task, no backtest, no implementation; hard cap 1 record.
