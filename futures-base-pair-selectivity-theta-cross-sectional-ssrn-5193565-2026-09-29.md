---
schema: strategy-research-record-v1
title: "Investment Base Pairs: theta-Scored Pair Selectivity inside Signal-Sorted Multi-Asset Futures Cross-Sections (SSRN 5193565)"
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - futures
  - multi-asset
  - cross-sectional
  - value-momentum-carry
  - pair-selection
  - portfolio-construction
  - ssrn
status: research-only
confidence: medium
source_as_of: 2025-04-01
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5193565"
  - "https://doi.org/10.2139/ssrn.5193565"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "C1: six unreconciled date expressions - PDF footnote 'Current version: March 20, 2025', PDF /CreationDate D:20250320090506-05'00', SSRN 'Date Written: March 25, 2025', SSRN suggested citation '(March 25, 2025)', landing 'Posted: 1 Apr 2025' shown together with 'Last revised: 25 Mar 2025' (a revision date that precedes the posting date), and the PDF footnote's 'a slide presentation of the ideas in this paper was first posted online in October, 2024'"
  - "C2: Appendix Tables D.9, D.10 and D.11 are titled 'Last 15 Years', 'Last 10 Years' and 'Last 5 Years' and their notes do say 'over the last 15/10/5 years of our sample', yet each of the three notes still prints the evaluation window as 'October 2003-September 2023' - the 20-year date range - so the printed window contradicts the stated sub-window length (a 5-year window ending 2023-09 begins 2018-10)"
  - "C3: momentum signal construction is stated two ways - Section 3.1 and the Appendix A table notes define momentum as 'the average trailing 12-month return' (a continuous signal consumed by sign(x_i - x_j) in the pair rule of equation 2), while footnote 12 states that '12-month momentum is defined as long one unit if the signal is positive; otherwise, short one unit' (an absolute-direction convention); the paper never reconciles the relative and absolute readings"
  - "C4: Section 2.1 says 'For general n, the weight on the asset with the highest signal is ...' and every printed weight and scaling expression is then multiplied by the indicator 1{n odd}, which footnote 9 defines as zero when n is even, so equations (1) and (3) evaluate to zero weights for even n; no n-even counterpart appears anywhere in the pinned PDF, and all four tested universes are odd (15 / 13 / 9 / 27), so the case is never exercised"
  - "C5: two entries in the reference list carry the paper's own unverified-identifier annotation while being printed as ordinary citations - Bae (2021) 'ProQuest ID: 2767845 (hypothetical; search ProQuest Dissertations for exact match)' and DeMiguel, Martin-Utrera and Nogales (2023) 'SSRN ID: 4567890 (hypothetical; check SSRN for exact match)'"
---

# Investment Base Pairs: theta-Scored Pair Selectivity inside Signal-Sorted Multi-Asset Futures Cross-Sections (SSRN 5193565)

## Provenance

- **Paper:** Christian L. Goulding and Campbell R. Harvey, *Investment Base Pairs*. Sole two authors printed on the PDF title block as `Christian L. Goulding a , Campbell R. Harvey b,c` with affiliations `a Harbert College of Business, Auburn University, Auburn, AL 36849 USA`, `b Fuqua School of Business, Duke University, Durham, NC 27708 USA`, `c National Bureau of Economic Research, Cambridge, MA 02138 USA`; printed emails `christian.goulding@auburn.edu` and `cam.harvey@duke.edu`. The SSRN landing author lines read `Christian L. Goulding / Auburn University - Harbert College of Business` and `Campbell R. Harvey / Duke University - Fuqua School of Business; National Bureau of Economic Research (NBER)` - the two surfaces agree.
- **Canonical identifiers:** DOI `10.2139/ssrn.5193565`; stable landing `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5193565`; SSRN suggested citation `Goulding, Christian L. and Harvey, Campbell R., Investment Base Pairs (March 25, 2025). Available at SSRN: https://ssrn.com/abstract=5193565 or http://dx.doi.org/10.2139/ssrn.5193565`. JEL `G10, G11, G12, G15`.
- **Landing read in a browser session on 2026-09-29** after the Cloudflare interstitial cleared, showing `62 Pages`, `Posted: 1 Apr 2025`, `Last revised: 25 Mar 2025`, `Date Written: March 25, 2025`, heading `63 References`, heading `0 Citations`, `DOWNLOADS 1,869`, `ABSTRACT VIEWS 6,738`, keywords `cross-signal correlation, signal bias, predictability, pairs trading, futures and forwards, signal sorting, investments, portfolio construction, value, momentum, carry`, and the licence line `The copyright holder has granted SSRN a license. All rights reserved. No reuse allowed without permission.` - so this record normalises only short printed values, table cells and section references.
- **Pinned primary source:** the PDF was retrieved through the landing `Download This Paper` control and the download gate's `Download without registration` step (browser download, 2026-09-29). Only the stable landing URL and DOI are recorded here; **no presigned, expiring or session-bound delivery URL is stored**. Pinned PDF: **1,190,654 bytes, 62 pages, SHA-256 `0ae72e06af64426d4b2654f7d1fd3166ca3cdf0947127ecf3e3d79cda91a7ad4`**. PDF metadata: `/Title "Investment Base Pairs"`, `/Author "Christian L. Goulding; Campbell R. Harvey; "`, `/Creator "LaTeX with hyperref"`, `/Producer "MiKTeX pdfTeX-1.40.26"`, `/CreationDate D:20250320090506-05'00'`. Text extracted with pypdf 6.16.2 to **143,631 characters / 2,402 lines**; all 62 pages read end to end (Sections 1-4, Section 1.1, Sections 2.1-2.5 with Theorems 1-3 and equations (1)-(19), Sections 3.1-3.6.1, body Tables 1-8, Figures 1-5 and their notes, the full reference list, Appendix A with Tables A.1-A.4, Appendix B proofs, Appendix C, Appendix D with Tables D.1-D.13).
- **Publication status:** SSRN working paper (SSRN Electronic Journal / Elsevier). The pinned PDF and the landing carry **no journal, no issue, no DOI other than the SSRN DOI, and no peer-review statement** -> **not stated in source**. Publication/peer-review status therefore remains `not stated in source`.
- **Data source (proprietary):** Appendix A states the monthly returns and signals are *obtained from Research Associates across 64 futures and forwards markets*; no public data artefact, no code, no replication package (`code availability`, `replication`, `github` all return zero occurrences in the pinned text).
- **Companion work named by the source:** footnote 11 refers to *Goulding et al. (2020)* as "an early, unpublished work" for the special case `mi = mj = 0, si = sj = 1`, and the reference list prints *Goulding, C. L., Harvey, C. R., and Pickard, A. (2020). Decoding systematic relative investing: A pairs approach. Available at SSRN 3680314* - **that identity is not present in this repository either (dedup below)**.
- **Pre-write source-identity deduplication (whole checkout, hidden trees included):** `rg -uuu` over every file in the repository working tree - including `.git`, `.mimo-worktrees`, `.agents`, `.hermes`, `coverage_manifest.csv` (1,088,787 bytes) and the **1,064 `*.md` records in the checkout root** (tracked plus untracked) - for `5193565`, `Investment Base Pairs`, `Goulding`, `Research Associates`, `linear-in-rank`, `linear in rank`, `pair selectivity`, `theta score`, `base pair selectivity`, `Selective Base Pairs`, `junk pairs`, `signal-mean bias`, `signal variance imbalance`, `1,710`, `signal-driven pair`, `3680314`, `Decoding systematic relative` -> **0 files each**. `cross-asset predictability` matched 3 files, every hit an unrelated high-frequency cross-impact sentence in `duration-aware-bocpd-lognormal-order-flow-regime-2026-09-11` and its two worktree copies. Positive control `novy-marx` returned **29 files** in the same session. `git pull origin main` was run before researching and `git log --oneline -20` was inspected only as a convenience glance.
- **Canonical schema resolved read-only:** `kb_read quant/strategy-research-record-spec-v2.md` -> file not found, so the run **failed closed onto `quant/strategy-research-record-spec-v1.md`** (canonical, 10,289 bytes, sha256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`).
- **Notation normalisation:** the source's two Greek scores (the barred unconditional score and the unbared conditional score) are written **`theta-bar` and `theta`** throughout this record; every other quoted phrase is reproduced verbatim from the pinned PDF apart from ligature artefacts of the text extraction.

## Economic mechanism

### Source-reported

- **Decomposition (Theorem 1, Section 2.3).** Any dollar-neutral cross-sectional strategy whose weights are linear in signal *ranks* equals a scaled sum of all of its pairwise long-short strategies: `r = 2 / (n^2 - 1{n odd}) * sum_{i<j} r_ij`, where `r_ij = sign(x_i - x_j) * (r_i - r_j)` (equation 2) - long the higher-signal asset, short the lower-signal one, refreshed each period because the ordering flips. The paper calls this collection the **base pairs**. The decomposition preserves unit gross exposure (`sum |w_i| = 1`) and dollar neutrality.
- **Pair model (Section 2.4).** Asset returns are modelled as `r_i = mu_i + b_ii x_i + b_ji x_j + eps_i` (and symmetrically for `r_j`) with jointly normal signals and noise, time-invariant moments. This yields two scores: **theta-bar**, the unconditional steady-state expected pair return, and **theta** (no bar), the conditional expected return given the direction of the current signal gap (Theorem 3, equation 15). Each decomposes exactly into an **unexplained effect UE** (intercepts `mu`), an **own-asset effect OA** and a **cross-asset effect CA** (equations 16-19).
- **Five stated drivers (Figure 1 and Section 1).** D1 own-asset predictability, D2 cross-asset predictability, D3 signal correlation, D4 signal-variance imbalance, D5 signal-mean imbalance - two direct, three modulating.
- **The authors' thesis.** Aggregate signal sorting "either tacitly assumes that there is not any significant performance variation among pair strategies ... or, that if significant variation exists, it cannot be detected and exploited" (Section 1). Their answer: variation exists, it is measurable point-in-time through theta, and **pruning "junk" pairs** raises returns at fixed leverage.
- **Explicit non-identity (Section 1.1).** The technique "differs sharply from a well-known method called 'pairs trading'" - no cointegration, no spread stationarity, no convergence bet; it is a cross-sectional signal-sorted construction whose units happen to be pairs.
- **Stated cost/leverage setting (footnote 6).** "Futures markets offer distinct advantages over traditional assets. Transaction costs below 5 basis points and high liquidity enable global trading efficiency. Embedded leverage amplifies returns uniquely ... Leverage constraints outweigh volatility targets, fixing capital via margins (Moskowitz et al., 2012), and shifting focus from Sharpe ratios - limited by fixed leverage - to average returns per unit of leverage."
- **Stated no-look-ahead claim (Section 3.6 and Section 1).** Pairs are selected "based on their theta score each month at the time of portfolio formation so there is no look-ahead bias"; signals and weights sit at date `t` and returns at `t+1` (Section 2 preamble).

### Research interpretation

- **Falsifiable mechanism:** within a signal-sorted multi-asset futures cross-section, pair-level expected returns are *heterogeneous and predictable* because (i) part of a signal's return relevance spills onto the correlated leg (cross-asset effect) and (ii) signal mean/variance imbalances silently dominate which leg sets the trade direction. A point-in-time screen on the model-implied pair mean can therefore concentrate the book in pairs whose sign-switching is informative and away from pairs whose apparent signal return is really an intercept artefact.
- **Component roles (hybrid structure):**
  - *Premium / primary signal:* value, momentum and carry sortations inside each asset class (equity, bond, currency, commodity) - this is where the return comes from.
  - *Meta-signal / selection layer:* theta ranking of all `N(N-1)/2` pairs inside a category, keeping the top `S%` each month - this is the claimed improvement.
  - *Risk control (not alpha):* fixed leverage multiples per asset class (4.5 equity, 7.5 bond and currency, 1.5 commodity) and unit gross exposure per pair; the paper itself frames leverage as a constraint, not a signal.
  - *Benchmark:* `S = 100%` reproduces the linear-in-signal-rank strategy, so every reported gain is a *selection* effect, not a new premium.
- **What would have to be true:** the theta ranking must survive out of sample, after costs, relative to (a) the all-pairs benchmark, (b) a random-pair placebo of the same concentration, and (c) simple own-asset-only or cross-asset-only scores. None of those comparisons is run by the source beyond the alternative *weighting* baselines (Quantile 30, Fixed 3).
- This is a **ported hypothesis with no crypto evidence**: the source is entirely traditional futures and forwards.

## Signal

**Source-reported normalisation** (Sections 2.2, 2.5, 3.1, 3.6, Appendices A and D):

- **Formation timestamp:** monthly. Signals and weights are formed at date `t`; pair and portfolio returns accrue from `t` to `t+1` (Section 2 preamble). Timezone is never stated - monthly bars only (**data gap**).
- **Universe:** 64 futures and forwards - 15 country equity index futures, 13 bond futures across nine currency zones, 9 one-month currency forwards against USD, 27 commodity futures across six sectors; **within-asset-class pairs only** (cross-asset-class pairs are explicitly excluded). Pair counts: 105 equity, 78 bond, 36 currency, 351 commodity = 570 per signal type, **1,710 base pairs** in total. Front contracts, "rolled to next nearest contract at the beginning of their expiration month" (Appendix A).
- **Signals (monthly, point-in-time at `t`):**
  - Equity: value = earnings/price ratio (3-year z-score); momentum = average trailing 12-month return; carry = futures roll (spot minus first).
  - Bond: value = real yield; momentum = average trailing 12-month return; carry = excess yield plus term-structure roll.
  - Currency: value = 5-year real exchange rate reversal (3-year z-score); momentum = average trailing 12-month return; carry = cash-rate differential.
  - Commodity: value = 5-year price reversal; momentum = average trailing 12-month return; carry = futures roll (first minus second).
- **Pair rule (equation 2):** `r_ij = sign(x_i - x_j) * (r_i - r_j)`; ties (`sign = 0`) are neutral; the long and short legs switch as the signal ordering switches, so pairs are not static.
- **Scores:** theta-bar and theta are estimated on **rolling trailing windows of 120 months (equities), 180 months (bonds) and 240 months (currencies and commodities)**, using all available data inside the window with a **minimum of 24 months** (Section 3.2). The paper states results are robust to +/-5-year window variation and +/-1 year on the minimum-observation rule (footnote 13).
- **Selection rule (Section 3.6):** each month, sort the base pairs of a strategy category by theta and keep only the **top S%**, feeding them into next month's cross-sectional portfolio; `S` takes **11 levels** `5%, 10%, 20%, ..., 100%`, with `S = 100%` equal to the linear-in-rank benchmark. At `S = 10%` the paper's own worked example is the top 10 equity pairs, 7 bond pairs, 3 currency pairs and 35 commodity pairs per month (floor of `S x N(N-1)/2`), i.e. roughly 5 / 4 / 2 / 18 pairs at `S = 5%` (**the 5% counts are research-computed from the same floor rule, not printed**).
- **Leverage:** fixed **within** a strategy category across all selectivity levels for comparability - **4.5x equity, 7.5x bond, 7.5x currency, 1.5x commodity**, the ratio 5:5:3:1 attributed to Ang et al. (2011) margin requirements, average **5.25x**. Footnote 4: returns are "return per unit of leverage".
- **Group aggregation:** asset-class, signal-type and "All" rows are **simple averages of the corresponding strategy-category portfolio series** (table notes in Tables 8, D.8-D.13) - the "All" line is an equal-weight average of the 12 category books at the same `S`.
- **Holding / rebalance cadence:** monthly formation, one-month holding implied by the `t` -> `t+1` return definition. **No explicit rebalance, no holding-period statement, no re-entry rule beyond the monthly re-sort** - underspecified.
- **Position sizing across the selected pairs is not stated.** Each pair carries unit gross exposure, but the paper never says how the selected `k` pairs are combined (equal weight per pair, sum-normalised, or category leverage spread across them). **underspecified - data gap.**
- **Not specified anywhere:** stop / take-profit, drawdown control, turnover control, capacity cap, tie-break rule among equal theta values (the theory assumes strict ordering, footnote 7), minimum-liquidity filter, delisting/roll-cost treatment in returns.

## Required data

- **Instruments:** 64 futures and forwards across four asset classes (15 equity index futures, 13 bond futures, 9 USD-based 1-month currency forwards, 27 commodity futures), front contract only, rolled at the start of the expiration month.
- **Vendor / venue:** monthly returns and signals from **Research Associates** (Appendix A) - proprietary; exchange-level venue list not stated (**data gap**).
- **Market type:** exchange-traded futures and OTC-style forwards (traditional assets only).
- **Timeframe:** monthly bars; no intraday or daily data is used anywhere.
- **Fields:** monthly price/return series per contract; earnings/price ratio, real yield, excess yield, 5-year real exchange rate, cash-rate differential, 5-year price reversal, trailing 12-month return, futures roll (spot-first / first-second / excess-yield-plus-term-structure-roll) as supplied by the vendor. No order book, no trades, no open interest, no bid-ask, no volume, no funding, no borrow (**all zero occurrences in the pinned text**).
- **Point-in-time:** all characteristics are trailing and estimated with data up to `t`; the source claims formation at `t` and returns at `t+1` with "no look-ahead bias". Whether the vendor's earnings/price and real-yield inputs are themselves point-in-time (revision-safe) is **not stated - data gap**.
- **Sample:** "Data are monthly beginning in January 1985 for some of the assets ... and data runs through to September 2023" (Section 3.1); the pair panel's own earliest start date is **1986-01** (Table 1), consistent with the 12-month momentum warm-up (**research-computed reconciliation; the paper prints no note explaining the one-year gap**). Evaluation window for all selectivity results: **October 2003 - September 2023 (240 months)**, with sub-windows described as the last 15, 10 and 5 years of the same sample.
- **Missing data:** not addressed - no statement on stale prices, suspended contracts, or how a pair with a missing leg is handled (**data gap**). Table 1 shows per-category observation counts ranging from 10,740 to 140,014 portfolio-months, i.e. unequal histories are absorbed silently.

## Execution assumptions

Cost determination from a **Methods-level read of Sections 2, 3.1, 3.6, Appendix A and Appendix D** plus a whole-document term scan of the pinned PDF (word-boundary counts): `transaction cost` **2** (Section 1 "Given low transaction costs, high liquidity..." and footnote 6 "Transaction costs below 5 basis points"), while `slippage` **0**, `spread` **0**, `bid-ask` **0**, `commission` **0**, `fee` **0**, `turnover` **0**, `market impact` **0**, `latency` **0**, `fill` **0**, `market order` **0**, `limit order` **0**, `maker` **0**, `taker` **0**, `borrow` **0**, `funding` **0**, `capacity` **0**, `participation` **0**, `execution` **0**, `friction` **0**, `risk-free` **0**, `code availability` **0**, `replication` **0**; `leverage` **39**, `margins` **2**, `liquidity` **2**. Consequences, each a `data gap` and **never treated as zero**:

- **Signal-to-order timing:** signals and weights at `t`, returns at `t+1` (source). Exact trade timestamp, next-bar-open vs month-close execution: **not stated - data gap**.
- **Order type / fill model:** **not stated - data gap** (zero occurrences of order-type vocabulary).
- **Fees, spread, slippage, impact:** no cost model is applied to any reported number. The only quantitative cost statement is footnote 6's `Transaction costs below 5 basis points`, with **no one-way/round-trip qualifier, no per-instrument schedule and no link to any table** - so its scope is **underspecified**.
- **Gross vs net:** the paper **never states whether the reported annualized returns and Sharpes are gross or net** of trading costs, and no cost subtraction appears in any table note - **data gap**.
- **Leverage / margin:** multiples 4.5 / 7.5 / 7.5 / 1.5 (average 5.25) are imposed, "fixing capital via margins"; **no margin requirement schedule, no maintenance-margin or liquidation rule, no leverage-vs-default model - data gap**.
- **Borrow / shorting:** shorting is implicit in dollar-neutral futures pairs; borrow cost, stock-loan or delivery constraints **not stated - data gap** (the word never appears).
- **Roll / expiry:** front contract rolled at the beginning of the expiration month (Appendix A); **roll cost and roll slippage treatment in returns not stated - data gap**.
- **Turnover / capacity:** **zero occurrences** - no turnover figure, no volume share, no AUM scaling, no capacity statement. Concentration at `S = 5%` (roughly 5 / 4 / 2 / 18 pairs) makes this material.
- **Latency / partial fills:** **zero occurrences - data gap**.
- **Risk-free rate:** `risk-free` has zero occurrences; see Independently reproduced for the arithmetic implication for the printed Sharpe ratios.

## Evidence

### Source-reported

All figures below are **third-party claims from the pinned PDF**, none verified by us by re-running the study; each carries its table/section provenance. Evaluation window for every selectivity figure is **October 2003 - September 2023** unless stated otherwise.

**Panel and descriptive statistics (Table 1, Table 2)**
- 1,710 pair portfolios, **518,884 portfolio-months**, **453 distinct months**, earliest pair start **1986-01**, all portfolios end **2023-09**.
- All-portfolios average monthly return **0.19%**, average volatility **7.401%**, average theta-bar **0.16%**. By asset class (avg monthly return / vol): equity 0.09 / 3.881, bond 0.06 / 1.466, currency 0.07 / 2.860, commodity 0.26 / 10.239. By signal type: value 0.14 / 7.403, momentum 0.17 / 7.405, carry 0.25 / 7.396.
- Within-group percentiles of average monthly pair return (Table 2): All min **-1.72**, p25 **-0.07**, median **0.12**, p75 **0.42**, max **2.27**; volatility percentiles **0.33 / 3.27 / 8.55 / 10.68 / 17.71**.
- Category means (Table 1): equity momentum **0.00%** (the weakest cell), commodity carry **0.34%** (the strongest), currency value **0.01%**.

**Descriptive fit of the model (Table 3, Table 4, Table 5)**
- theta-bar contemporaneously explains **63.7%** of trailing-mean pair-return variation with beta **0.984** (SE 0.007), intercept **0.0008**, **N = 126,286** portfolio-months, Newey-West HAC standard errors; best group fit Currency Carry (Adj. R2 **0.852**, beta 1.001), weakest Commodity Carry (Adj. R2 **0.486**, beta 0.785).
- Variance decomposition (Table 4, All): **UE 12.9% / OA 45.6% / CA 41.6%**; extremes Currency Value OA **83.1%** vs **14.0%** CA, Bond Carry CA **54.6%**, Currency Carry UE **30.4%**, All Carry UE **22.0%**.
- Normalised drivers (Table 5, All): `UE 0.101, OA 0.803, CA -0.096`, signal correlation **0.353**, signal-mean bias **0.464**, signal-volatility bias **0.535**; Equity Momentum signal correlation **0.810** (highest), Currency Carry mean bias **1.821**, Commodity Carry volatility bias **0.859**.

**Predictive tests (Table 6, Table 7)**
- Fama-MacBeth of next-month pair return on theta: coefficient **0.158 (t = 3.69)** without fixed effects and **0.150 (t = 3.57)** with asset-class and signal-type fixed effects; Avg. Adj. R2 **0.154 / 0.169**; **429 periods, 477,847 observations**; controls are the FF5 plus Carhart UMD.
- Component regression: **CA 0.161 (t = 4.95)**, **UE 0.121 (t = 2.42, 5% level)**, **OA 0.080 (t = 1.33, not significant)**; CA alone drops to **0.056 (t = 1.81)**.
- Economic magnitudes (Table 7, against a mean annualized pair return of **2.28%**): theta mean effect **0.31% [13.4%]**, +1 SD **1.68% [73.5%]**, +2 SD **3.35% [147.0%]** (model 1); **0.29% [12.7%] / 1.59% [69.8%] / 3.18% [139.6%]** (model 2).

**Headline selectivity results - body Table 8 = Appendix Table D.8, average annualized return, last 20 years**
- **All: 10.4% at S=5%, 8.7% at S=10%, 6.9% at S=30%, against the 3.4% linear-in-rank benchmark** (the abstract's "3.4% to 10.4%"); comparators Quantile 30 **3.7%**, Fixed 3 **4.1%**.
- Full 11-level All row (Table D.8): **10.4, 8.7, 7.4, 6.9, 6.3, 5.9, 5.3, 4.9, 4.7, 4.2, 3.4**.
- Equity value **14.3 vs 3.6** (the abstract's "climbs from 3.6% to 14.3%"); equity momentum **12.4 vs -0.6**; currency momentum **10.3 vs -3.0** (the abstract's "reverses a -3.0% loss to a 10.3% gain"); bond value **15.1 vs 3.6**; bond carry **14.3 vs 2.7**; currency carry **17.3 vs 10.7**; equity carry **13.0 vs 5.7**.
- **Commodity carry is the exception: 2.3 at S=5% vs 5.3 benchmark** (2.3, 4.4, 5.9, 7.2, 6.7, 6.8, 6.9, 6.9, 6.7, 6.3, 5.3 - non-monotone, best at S=30%). The source flags this itself in footnote 15.
- Asset-class rows at S=5% vs benchmark: equity **12.9 vs 2.9**, bond **12.7 vs 3.8**, currency **10.6 vs 3.2**, commodity **5.3 vs 3.9**. Signal-type rows: value **11.0 vs 3.5**, momentum **8.7 vs 0.7**, carry **11.7 vs 6.1**.

**Volatility and Sharpe (Appendix Tables D.12 and D.13, last 20 years)**
- Volatility rises with selectivity: All **11.6% (S=5%) vs 5.2% (S=100%)**; equity all **24.2 vs 8.2**; currency all **27.6 vs 14.5**; currency momentum **46.2 vs 27.7**; equity momentum **34.0 vs 16.5**.
- Sharpe (All): **0.90 at S=5% vs 0.65 at S=100%**; equity all **0.54 vs 0.35**, bond all **0.64 vs 0.46**, currency all **0.38 vs 0.22**, **commodity all 0.33 vs 0.60 (selectivity hurts)**. Category Sharpes at S=5% that stay low: currency value **0.11**, commodity carry **0.11**, commodity momentum **0.19**, currency momentum **0.22**, equity momentum **0.37**.
- Sub-windows (Tables D.9-D.11, All row): last 15y **10.8 vs 3.0**, last 10y **10.0 vs 2.4**, last 5y **13.2 vs 2.3**. Commodity carry at S=5% is negative in all three: **-1.2 / -4.4 / -8.1**. Bond all in the last 5 years is non-monotone and often worse than its benchmark: **10.6 at S=5%, 4.0 at 10%, 1.8 at 20%, -1.3 at 30%, -1.7 at 40%, 0.0 at 50%, 0.1 at 60%** against a **+4.2%** benchmark.
- Baseline scaling claim (Section 3.6): the 4.5/7.5/7.5/1.5 leverage grid "generates approximately 17% volatility across the 12 strategy category benchmark portfolios over the last 20 years".

**Claims in the abstract and Section 1**
- "targeting top pairs can triple average returns at fixed leverage over 20 years"; "Equity Momentum loses -0.6% under the benchmark approach, but gains 12.4% under the base pairs approach"; "Marked selectivity gains ... consistently in sub-samples over the last 20, 15, 10, and 5 years ... for virtually all strategy categories and group levels".
- Statistical protocol: Newey-West (1987) HAC standard errors for the panel and Fama-MacBeth tests, 5% winsorisation of characteristics but not returns (footnote 14), FF5 + UMD controls. **No multiplicity correction anywhere; no deflated Sharpe; no placebo; no out-of-sample split of the 2003-2023 evaluation window.**

### Independently reproduced

**not independently reproduced**

We did not re-run the study: the underlying returns and signals are proprietary (Research Associates), the paper prints no code or replication artefact (`code availability` / `replication` / `github` = 0 occurrences), and Scout scope excludes backtesting. What we did verify is **arithmetic and provenance against the pinned text** (script `ibp_check.py`, pypdf 6.16.2 extraction, **exit 0**, every assertion recomputed from the file rather than from memory):

- **Reproduced (198/198 cells):** Table D.13 (Sharpe) equals Table D.8 (return) divided by Table D.12 (volatility) for every common row and column of the 11-level grid, worst absolute deviation **0.0124** - i.e. the printed Sharpe ratios are raw `mean / volatility` with **no risk-free subtraction**, a fact the paper never states.
- **Reproduced:** Table 1's three partitions (4 asset classes, 3 signal types, 12 categories) each sum exactly to **518,884** portfolio-months.
- **Reproduced:** pair arithmetic 15C2 = **105**, 13C2 = **78**, 9C2 = **36**, 27C2 = **351**, sum 570 x 3 signal types = **1,710**.
- **Reproduced:** leverage ratio 7.5 : 7.5 : 4.5 : 1.5 = **5 : 5 : 3 : 1** as claimed, and (4.5+7.5+7.5+1.5)/4 = **5.25**.
- **Reproduced:** the 12 benchmark category volatilities in Table D.12 average **17.28%**, matching Section 3.6's "approximately 17%".
- **Reproduced:** the abstract's verbal multipliers - 10.4/3.4 = **3.06** ("triple"), 14.3/3.6 = **3.97** ("nearly four-fold").
- **Reproduced:** Table 7's base **0.19% monthly x 12 = 2.28%**, the exact "mean annualized pair portfolio return" it divides by.
- **Reproduced:** the Section 3.6 worked example is the floor of `0.10 x {105, 78, 36, 351}` = **{10, 7, 3, 35}`**, and the selectivity grid has **11** levels as stated.
- **Reproduced:** the reference list contains **63** year-bearing entries, matching the landing heading `63 References`.
- **Reproduced:** `1{n odd}` appears **6** times in equations (1)/(3) and their surrounding text with **no `{n even}` counterpart** (C4), and the word "even" only ever appears in prose such as "an eventual return".
- **Reproduced:** the C2 window mismatch - Tables D.9/D.10/D.11 notes each print `October 2003-September 2023` while titled `Last 15/10/5 Years`.
- **Reproduced:** term census for the cost/execution vocabulary (2 / 0 / 0 / ... exactly as listed under Execution assumptions) and **2** self-flagged `(hypothetical; ...)` references (C5).
- **Context (research-computed, not a source claim):** the pair panel's 1986-01 start versus the stated 1985-01 data start is exactly one 12-month momentum warm-up; equity pairs starting 1989-10 is consistent with Nikkei 225 futures (N = 420 months) gaining a 12-month signal history.

### Negative evidence

1. **No cost model touches any reported number.** The whole paper contains two mentions of "transaction cost" and zero mentions of slippage, spread, bid-ask, commission, fees, turnover, impact, latency, fill, order type, maker/taker, borrow, funding, participation or capacity - so the 10.4% vs 3.4% gap is asserted in an unpriced setting, and gross-versus-net status is never declared.
2. **Concentration doubles volatility before it earns anything.** All-portfolio volatility goes 5.2% -> 11.6% from S=100% to S=5%, so the Sharpe gain is **0.65 -> 0.90**, not the 3x return headline; equity-all volatility goes 8.2% -> 24.2% and currency-momentum 27.7% -> 46.2%.
3. **Commodities lose on risk-adjusted terms.** Commodity-all Sharpe **0.33 (S=5%) vs 0.60 (S=100%)**, and commodity-carry **0.11 vs 0.46** - selectivity degrades the very category that carries the largest share of the pair panel (346,772 of 518,884 portfolio-months).
4. **Commodity carry is the source's own admitted failure:** 2.3% at S=5% vs 5.3% benchmark; footnote 15 attributes it to "unmodeled factors", the lowest Table 3 fit (Adj. R2 0.486), the highest signal-volatility bias (0.859) and second-highest UE dependence.
5. **Extreme selectivity is unstable in sub-samples:** commodity carry at S=5% is **-1.2% (15y), -4.4% (10y), -8.1% (5y)**; bond-all in the last 5 years falls from **+10.6% (S=5%)** through **-1.3% (S=30%)** and **-1.7% (S=40%)** back to **+4.2% at the benchmark**, so the response to selectivity is non-monotone, not a smooth dose-response.
6. **The universe is pre-selected for historical success.** Section 3.2 states that the average pair return is positive "because we study these asset-class-signal-type combinations in part because they are ones that 'worked' historically" - the average pair is positive by construction, so the benchmark level itself is survivor-flavoured.
7. **No out-of-sample test of the selection rule.** The phrases `out-of-sample`, `walk-forward`, `holdout` and `placebo` each return **zero occurrences** in the pinned PDF; everything runs on one 2003-2023 window inside a sample ending 2023-09, with no held-out period and nothing after September 2023 (three years stale as of this capture).
8. **No multiplicity control.** 11 selectivity levels x 12 categories x 4 asset classes x 3 signal types x 4 sub-windows are displayed with no adjustment; `Benjamini`, `family-wise`/`familywise` and `deflated` all return **zero occurrences**, `Holm` matches only inside the word "Stockholm", and the single `multiple testing` hit is the literature review quoting Harvey et al. (2016) rather than a correction applied here. The headline selects the most favourable cell (S=5%).
9. **theta is estimated on windows up to 240 months**, i.e. up to 20 years of overlapping lagged returns; the screen is extremely slow-moving and its early-sample estimates rest on as few as 24 months (Section 3.2), so "conditional" prediction is closer to a slow regime label than a fast signal.
10. **The theta model's own assumptions are conceded** (Section 3.3): "linear return-signal relationships (own and cross-asset); joint normality; time invariance of moments; and unmodeled effects ... not likely to hold in the real world".
11. **Own-asset predictability - the textbook channel - is not a significant cross-sectional predictor** in Table 6 (OA 0.080, t = 1.33), and CA's predictability collapses to t = 1.81 when run alone; the selection score therefore leans on interactions the model itself calls fragile.
12. **No portfolio artefact:** no equity curve, no maximum drawdown, no turnover, no net-of-cost Sharpe, no account-level risk metric anywhere in 62 pages - `drawdown` appears exactly once, inside a literature sentence about momentum's 2009 crash, and `turnover` zero times.
13. **No capacity or liquidity analysis** at all, despite holding only ~5/4/2/18 pairs at S=5% inside 64 futures markets - participation, market impact and borrow are literally absent from the text.
14. **Leverage up to 7.5x is imposed without a margin, liquidation or default model**, while footnote 6 argues leverage "fixing capital via margins" - the risk side of that trade is unexamined.
15. **Proprietary data, no artefact:** Research Associates monthly returns/signals, no code, no replication package, no data-availability statement, no pre-registration - independent reproduction is not currently possible from public sources.
16. **Reference-list integrity:** two citations carry the paper's own `(hypothetical; ...)` annotation with identifiers the paper tells the reader to verify (C5).
17. **Formula scope:** the decomposition and weight formulas are odd-n only (C4); every tested universe happens to be odd (15/13/9/27), so the parity gap is invisible in the results but blocks generalisation to even-n universes.
18. **Momentum construction is ambiguous (C3)** - a reader reimplementing the signal cannot tell whether momentum enters as a continuous rank input or as an absolute +/-1 position, and the two readings give different pairs.
19. **Window labelling in the sub-sample tables is inconsistent (C2)**, so the exact start dates of the 15y/10y/5y results cannot be read off the paper.
20. **Selection and combination weights across kept pairs are unstated**, so the reported category returns are not exactly reconstructable; two reasonable aggregations (equal weight per pair vs re-normalised gross) give different volatilities at S=5%.
21. **Zero external validation:** SSRN landing shows `0 Citations`; this is a working paper with no journal, no issue and no peer-review statement (**not stated in source**), and the licence forbids reuse without permission.
22. **Strategic-benchmark caveat:** the two alternative weighting baselines (Quantile 30, Fixed 3) are the only controls; there is no random-pair or theta-shuffled placebo, so "selection skill" is not separated from "just holding fewer, more volatile pairs".
23. **Adjacent contrary / competing evidence already in this repository** (different sources, different mechanisms): `g10-fx-carry-fx-value-energy-roll-yield-net-cost-audit-2026-09-23` (G10 FX carry/value and energy roll-yield premia shown fragile net of cost), `futures-quad-trend-carry-skew-vov-composite-2026-09-11` (multi-alpha futures composite), `pairs-trading-adf-stationarity-filter-walk-forward-falsification-2026-09-12` (cointegration pair trading fails a walk-forward gate), `future-aligned-soft-contrastive-asset-retrieval-peer-basket-spread-2026-09-25` (peer-basket spread trading), `moving-average-distance-cross-sectional-anchoring-us-equity-ssrn-3111334-2026-09-26` (cross-sectional anchoring long-short), `crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31` (cross-sectional momentum), and the published-anomaly replication records (`published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23`, `nine-anomaly-survivorship-free-agent-replication-oos-null-ssrn-7075658-2026-09-28`) which document post-publication decay of exactly this family of signal-sorted premia.

## Falsification plan

Everything below is **research-defined / research-proposed** by this Scout - none of these thresholds comes from the source, and the source prints **no failure rules of its own**. No-retuning rule: **all parameters stay frozen at the values printed in the pinned PDF (signal definitions, 120/180/240-month windows, 24-month minimum, the 11-level S grid, the 4.5/7.5/7.5/1.5 leverage grid); a failed gate may not be rescued by re-optimising windows, S or leverage on the evaluation sample.**

- **F1 - printed-value reproduction (research-defined).** Re-derive every cell of body Table 8 and Appendix Tables D.8, D.12 and D.13 from a re-implemented pipeline on Research Associates-equivalent futures data. **Tolerance +/-0.2 pp annualized return and +/-0.02 Sharpe.** Fail if any All or asset-class headline cell misses.
- **F2 - point-in-time audit (research-defined).** Assert that theta at month `t` uses only data with timestamps `<= t` for every window, and that vendor inputs (earnings/price, real yield) are vintage-safe. Fail the no-look-ahead claim if any look-ahead edge is found, or if the All S=5% gap shrinks by more than **20%** after PIT correction.
- **F3 - cost ladder (research-defined).** Apply a per-side cost ladder of **0 / 1 / 2.5 / 5 / 10 bp** (the source's own footnote-6 ceiling is 5 bp with an unstated one-way/round-trip scope) and a spread-based alternative. **Fail the tradability claim if, at 5 bp per side, the All gap (10.4 vs 3.4) retains less than 50% of its gross value.**
- **F4 - turnover gate (research-defined).** Measure monthly two-sided turnover of the selected book, including the leg flips implied by `sign(x_i - x_j)`. Fail if the break-even cost implied by turnover (gap / turnover) is **below 1 bp per side**, i.e. the source's own cost claim cannot cover it.
- **F5 - placebo concentration test (research-defined).** For each month, draw **10,000** random `k`-pair subsets matching the S=5% count per category, with the same leverage grid. Fail the theta-specific claim if the observed All S=5% return does not exceed the **95th percentile** of the placebo distribution.
- **F6 - score ablation (research-defined).** Rank pairs with (a) full theta, (b) own-asset effect only, (c) cross-asset effect only, (d) theta-bar (unconditional) only, (e) a random score. Fail the "five-driver" claim if OA-only or CA-only matches full theta within **0.5 pp** of the All S=5% return, or if unconditional theta does as well as conditional theta (which would make the sign-conditioning decorative).
- **F7 - multiplicity gate (research-defined).** Apply Benjamini-Hochberg at **q < 0.10** across the full family (11 S levels x 12 categories x 4 asset classes x 3 signal types x 4 sub-windows) plus a deflated-Sharpe adjustment counting every cell inspected. Fail if the headline cells do not survive.
- **F8 - window-sensitivity gate (research-defined).** Re-estimate with windows of **60 / 120 / 240 months** and minimum-observation rules of **12 / 24 / 36 months**. Fail if the sign of the All S=5% minus benchmark gap flips anywhere in the sweep, or if the Commodity Carry exception silently disappears and reappears.
- **F9 - frozen forward window (research-defined).** Freeze every rule and run **2023-10 onward** as a genuine forward test (the source's sample ends 2023-09). Fail if the All S=5% book fails to beat the all-pairs benchmark in **at least 2 of the first 3 full years**.
- **F10 - parity / generalisation gate (research-defined).** Re-run the decomposition on at least one **even-n** universe (e.g. 14 or 16 contracts) to resolve C4. Fail the "general n" claim if the printed formulas cannot be made to hold without an unpublished even-n expression.
- **F11 - concentration / capacity gate (research-proposed).** Cap each month's position at **20% of 20-day average volume** in each underlying contract and re-scale; fail the capacity claim if net S=5% performance falls below **half** of the reported gross figure, or if more than 10% of scheduled months cannot be filled.
- **F12 - cross-market gate (research-defined).** Replicate the identical selection rule on a second futures data vendor and on **crypto perpetual futures** (research-proposed port: value/momentum/carry analogues must be pre-declared). Fail generalisation if fewer than **2 of 3** asset-class groups reproduce a positive S=5%-minus-benchmark gap.
- **F13 - aggregation-specification gate (research-defined).** Because the source never states how selected pairs are combined, run both equal-weight-per-pair and gross-normalised aggregations at fixed category leverage. Fail the reproducibility claim if the two readings differ by more than **20%** in annualized return or reverse the Commodity Carry verdict.
- **Action on failure:** any failed gate downgrades the corresponding claim to `rejected` in a follow-up record; parameters are not retuned to rescue it.

## Crypto portability

**adapted** - the *mechanism* (decompose a signal-sorted cross-section into pairwise books, then screen those books on a point-in-time expected-return score) is venue-agnostic in principle, but **the source contains zero crypto evidence**, so crypto performance stays **unproven**.

Porting risks:
- **Signal definitions do not transport as stated:** equity "earnings/price", bond "real yield" and the 5-year real exchange rate have no direct crypto analogue; the value legs would have to be re-invented (research-proposed: on-chain yield, realised-vol-adjusted valuation, or exchange-specific metrics). Momentum (12-month average return) and a funding-based carry are the only near-transfers, and a funding-based carry is a *different* signal from a futures roll.
- **Market structure:** the study relies on 64 liquid exchange-traded futures/forwards with a front-contract roll at the start of the expiration month. Crypto perps have no expiry roll; their "carry" is a periodic funding payment on a 8-hour/1-hour calendar, and funding is an explicit cost/receipt that the source never models (0 occurrences of `funding`).
- **Venue fragmentation and survivorship:** the source's universe is a stable vendor list from 1985; crypto perpetual listings are short-lived, delisted and re-based, so a 120/240-month trailing window is often unavailable and point-in-time universe construction becomes the dominant bias.
- **24/7 vs monthly sessions:** the pair rule refreshes monthly at bar boundaries; crypto has no session close, and candle/timestamp boundaries plus stale marks differ across exchanges, which changes `sign(x_i - x_j)` at the margin.
- **Leverage and liquidation:** the 4.5x/7.5x/1.5x futures margin grid assumes exchange futures with a maintenance-margin regime; on perps the same gross exposure interacts with mark-price liquidation and isolated/cross margin, none of which the source models.
- **Cost surface:** "transaction costs below 5 basis points" is a claim about index/commodity/rate futures; crypto perp taker fees, maker rebates, spread and impact have a different shape, and venue fragmentation splits any single-book liquidity assumption.
- **Cross-sectional depth:** 27 commodity and 15 equity legs give 351 and 105 pairs; a crypto universe sized to have 240 months of history is far smaller, so pair counts and the S=5% concentration become statistically thin.

## Limitations

- **underspecified:** aggregation/weighting across the selected pairs; rebalance and holding mechanics beyond the `t` -> `t+1` convention; tie handling; momentum's relative-vs-absolute reading (C3); the exact start dates of the 15/10/5-year sub-windows (C2); the one-way/round-trip scope of the 5 bp cost claim; turnover, position sizing, drawdown control, capacity.
- **data gap (never zero):** order type, fill model, signal-to-order delay, latency, measured spread, slippage, commission, market impact, participation, turnover, capacity, borrow, funding, margin/liquidation model, roll-cost treatment, gross-vs-net status, risk-free rate, missing-data policy, point-in-time vendor vintages, code/replication artefact, pre-registration.
- **not independently reproduced:** all empirical results; only arithmetic identities, term censuses and provenance were checked against the pinned PDF (script `ibp_check.py`, exit 0).
- **contested / internally inconsistent:** 5 recorded contradictions (frontmatter `contradictions`), of which C2, C4 and C5 were each confirmed mechanically against the pinned text.
- **source quality:** SSRN working paper, `0 Citations`, two authors (one academic, one practitioner-affiliated), licence `All rights reserved. No reuse allowed without permission.`, no journal or peer-review statement (**not stated in source**), and two self-flagged hypothetical references.
- **identification:** the improvement is measured against the paper's own all-pairs benchmark and two weighting alternatives only; there is no random-selection placebo, so "theta skill" is not separated from "fewer, more volatile books".
- **sample:** 1985/1986-2023 on a vendor-curated, historically successful asset-class x signal grid; a single evaluation window (2003-2023), no held-out period, no post-2023 evidence.
- **statistical:** no multiplicity adjustment across the 11 x 12 x 4 x 3 x 4 grid, no deflated Sharpe, HAC standard errors only; the headline cell is the extreme of the selectivity grid.
- **incremental-write check:** no existing repository record shares this source identity or this mechanism (pair-level decomposition of rank-linear cross-sectional futures strategies screened on a model-implied pair mean); closest neighbours differ in source, mechanism and market (Negative evidence item 23).

## Implementation status

`implementation_status: not-implemented`.

Nothing in this record has been implemented in our research stack: no futures data was downloaded, no pair decomposition was coded, no backtest, production card, Qlib run, Paper, Testnet or Live workflow exists for this hypothesis. The only artifacts produced by this run are this Markdown record, the pinned PDF text extraction and the arithmetic-only check script in scratch.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record **does not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet or live trading. Those are separate, explicitly gated decisions taken downstream of this repository.

## Related Wiki records

Read-only Wiki Brain searches run this session: `kb_search "cross-sectional signal sorting futures base pairs"` -> 2 hits, `quant/put-call-parity-implied-borrow-dividend-confounding-falsification-2026-09-13.md` and `quant/llm-news-enhanced-cross-sectional-momentum-tilt.md`, both unrelated to pair-level decomposition and therefore **not linked as related**. `kb_read quant/strategy-research-record-spec-v2.md` -> file not found; the run failed closed onto `quant/strategy-research-record-spec-v1.md` (canonical, 10,289 bytes, sha256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`). **No related Wiki page is known, so no Wiki link is written here** (fabricating one is forbidden). No page was written to Wiki Brain by this run.

Neighbouring repository records used only for the dedup statement (each with its own source): `g10-fx-carry-fx-value-energy-roll-yield-net-cost-audit-2026-09-23`, `futures-quad-trend-carry-skew-vov-composite-2026-09-11`, `pairs-trading-adf-stationarity-filter-walk-forward-falsification-2026-09-12`, `future-aligned-soft-contrastive-asset-retrieval-peer-basket-spread-2026-09-25`, `moving-average-distance-cross-sectional-anchoring-us-equity-ssrn-3111334-2026-09-26`, `crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31`, `ewy-samsung-sk-hynix-three-leg-pairs-stat-arb-stock-perpetual-2026-09-12`, `crypto-correlation-clustered-pairs-trading-structural-metadata-stability-2026-09-15`. They differ from this record in **source identity and mechanism in every pair**: signal-sorted futures pair *decomposition and selection* is not cointegration/mean-reversion pairs trading, not a multi-alpha futures composite, not a net-cost premia audit, not an equity cross-sectional anchoring sort, and not a crypto cross-sectional momentum rotation.

## Sources

- Goulding, Christian L. and Harvey, Campbell R. *Investment Base Pairs*. SSRN working paper, DOI `10.2139/ssrn.5193565`, landing `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5193565`, Date Written 2025-03-25, Posted 2025-04-01, 62 pages, 63 references, `All rights reserved. No reuse allowed without permission.` Pinned PDF SHA-256 `0ae72e06af64426d4b2654f7d1fd3166ca3cdf0947127ecf3e3d79cda91a7ad4` (1,190,654 bytes), read in full 2026-09-29. All quantitative claims in this record trace to that PDF by section, equation, body table or Appendix-D table number.
- Secondary surfaces consulted for provenance only (not used for any strategy rule or number): Campbell R. Harvey's public research index `https://people.duke.edu/~charvey/new_research.htm`, which lists the paper as "Investment Base Pairs with Christian Goulding (W169)" and links back to the same SSRN identity.
- Companion identity named by the source but **not** used as evidence here: Goulding, Harvey and Pickard (2020), *Decoding systematic relative investing: A pairs approach*, SSRN 3680314 - absent from this repository (dedup above), so it remains un-captured rather than merged into this record.
- (Neighbouring repository records cited only as dedup/negative-evidence context, each with its own source - listed in Related Wiki records.)
