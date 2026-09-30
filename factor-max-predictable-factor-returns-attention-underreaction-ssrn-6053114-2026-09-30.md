---
schema: strategy-research-record-v1
title: Factor MAX Cross-Sectional Timing of Equity Factor Portfolios by Prior-Month Maximum Daily Factor Return
created: 2026-09-30
updated: 2026-09-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional
  - factor-timing
  - meta-strategy
  - extreme-returns
  - investor-attention
  - us-equities
status: research-only
confidence: medium
source_as_of: 2025-12
sources:
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6053114
  - https://doi.org/10.2139/ssrn.6053114
  - https://papers.ssrn.com/sol3/Delivery.cfm/6053114.pdf?abstractid=6053114&mirid=1
  - https://api.crossref.org/works/10.2139/ssrn.6053114
  - https://scholars.hkbu.edu.hk/en/publications/factor-max-and-predictable-factor-returns/
  - https://sites.google.com/view/ming-zeng/working-papers
  - https://sbfc.sydney.edu.au/2025/papers/SBFC2025_1E2_P216.pdf
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Introduction reports the low-attention factor MAX spread as 0.42% per month with t-statistics = 2.93, while Section 4.1 reports the same statistic as 0.43% per month with t-statistics = 3.03 and Table 5 Panel A prints 0.43 (3.03); recorded as printed, not reconciled."
  - "The conditioning attention index is defined three incompatible ways: Section 4.1 says 'average z-score of five attention proxies' but then enumerates six items including firm advertisement expenditure; the Table 5 caption says 'five attention proxies' and enumerates five items with firm advertisement expenditure omitted; the Introduction enumerates six with the word 'including'; the exact composition of the conditioning variable is therefore ambiguous."
  - "The principal-component exercise signal is defined four ways: the Introduction says PC factors are sorted on 'the prior month's maximal daily return (MAX)'; Section 4.2 says 'the average of their five largest daily returns in month t'; Section 4.2 later says 'their largest daily returns in the prior month'; the Table 7 caption says 'the average of their largest PC factor returns'; MAX, MAX5 and an unspecified average are different statistics, so Table 7 cannot be attributed to the baseline signal."
  - "The Table 7 significance legend reads '***, **, and * denote significance at the 10%, 5%, and 1% levels, respectively', which is inverted from standard convention and false against the printed t-statistics: PC21-PC40 Returns is marked * with t = 1.91, which is not significant at 1%, while PC1-PC20 Returns is marked *** with t = 3.02, which is significant at 1% rather than only at 10%."
---

# Factor MAX Cross-Sectional Timing of Equity Factor Portfolios by Prior-Month Maximum Daily Factor Return

## Provenance

- **Primary source (every number in this record comes from it):** Liyao Wang and Ming Zeng, *Factor MAX and Predictable Factor Returns*, SSRN working paper, DOI `10.2139/ssrn.6053114`, available at `https://ssrn.com/abstract=6053114`.
- **Author list exactly as source:** exactly two authors, in this order - Liyao Wang (footnote dagger: Department of Accountancy, Economics and Finance, School of Business, Hong Kong Baptist University, 34 Renfrew Road, Kowloon Tong, Hong Kong; `lywang@hkbu.edu.hk`) and Ming Zeng (footnote double-dagger: Department of Economics and the Centre for Finance, University of Gothenburg, P.O. Box 640, SE 40530 Gothenburg; `ming.zeng@cff.gu.se`). The SSRN landing page `citation_author` meta tags repeat the same two names in the same order (`Wang, Liyao`, `Zeng, Ming`). The SSRN landing page shows a different department label for the first author (`HKBU - Department of Finance and Decision Sciences`) than the PDF footnote; both are recorded as printed, not reconciled.
- **Version / date:** the pinned PDF carries the dateline `December 2025` and a PDF `CreationDate` of `D:20260105050923Z`; the SSRN landing page shows `Date Written: December 01, 2025`, `37 Pages Posted: 19 Jan 2026`, `citation_online_date 2026/01/19` and `citation_publication_date 2025/12/01`; the Crossref record for the DOI was created `2026-01-26` and indexed `2026-01-27`. There is no arXiv identifier and no journal version.
- **Pinned primary PDF:** `https://papers.ssrn.com/sol3/Delivery.cfm/6053114.pdf?abstractid=6053114&mirid=1`, fetched 2026-09-30, **359,440 bytes**, SHA-256 `6d170dd9709bab69e4a0e06b4dca701fdb9371f8835581a6cbe8dc038685fc46`, **37 pages**, **63,894 extracted characters**, **1,038 newline-separated lines**, read end to end covering the Abstract, Sections 1, 2.1, 2.2, 3, 3.1, 3.2, 3.3, 3.4, 4, 4.1, 4.2, 4.3, 5, the full reference list, Figures 1-4 with captions, Tables 1-7 with every printed cell, and the funding footnote block. Text was extracted with `pypdf` 6.16.2; the extraction contains no NUL characters.
- **Retrieval caveat recorded, not hidden:** in this run the SSRN landing page first returned a Cloudflare bot-verification interstitial in the headless browser and `curl` returned HTTP 403 for the landing page and for all three `Delivery.cfm` forms; the landing page and the PDF became retrievable only after the challenge cleared inside a real browser session, and the PDF was then fetched with that session's clearance through a 302 redirect to `download.ssrn.com`. Any SSRN-side byte change after 2026-09-30 would invalidate the digest above.
- **Cross-check version (used only to detect version drift, never as a source of numbers below):** the November 2025 conference author PDF hosted by the Sydney Banking and Financial Stability Conference, `https://sbfc.sydney.edu.au/2025/papers/SBFC2025_1E2_P216.pdf`, fetched 2026-09-30, 290,324 bytes, SHA-256 `f9bf91edbaadc2cc49cc155ce85db2fc50a74e7a5a5022da82245752231230cd`, 36 pages, 62,531 characters. Diffing the two versions is what exposed the stale Introduction figures recorded in the contradictions above, and it confirms that the November draft's Introduction t-statistic of 4.49 for the headline spread was corrected to 5.89 in the December draft.
- **Landing-page metadata used for status only:** `citation_title = Factor MAX and Predictable Factor Returns`, `citation_doi = 10.2139/ssrn.6053114`, `citation_abstract_html_url = https://papers.ssrn.com/abstract=6053114`, `citation_keywords = Factor Investing, Extreme Returns, Return Predictability, Underreaction, Investor Attention`, `tdm-reservation = 1`. The landing page states `License Information: The copyright holder has granted SSRN a license. All rights reserved. No reuse allowed without permission.` This record therefore cites and normalizes the work and does not reproduce its text. Crossref returns `type: posted-content`, `subtype: preprint`, `publisher: Elsevier BV`, `group-title: SSRN`, `container-title` empty, `reference-count: 0`.
- **Publication / peer-review status:** preprint / working paper only. The pinned PDF contains zero occurrences of `accepted`, `forthcoming` or `under review`; the string `Review of Asset Pricing Studies` occurs exactly once and only as the journal of the cited Kagkadis et al. (2024) reference, so no journal acceptance is claimed in the primary source. The statement "R&R at Review of Asset Pricing Studies" appears only on the second author's public working-papers page (`https://sites.google.com/view/ming-zeng/working-papers`) and is recorded here as an **unverified author-page claim**, not as source-verified status. The HKBU institutional repository record (`https://scholars.hkbu.edu.hk/en/publications/factor-max-and-predictable-factor-returns/`) lists DOI `10.2139/ssrn.6053114`, 37 pages and `Publication status: Published - 19 Jan 2026`, which is the SSRN posting date rather than a journal publication.
- **Funding and disclosures:** the PDF footnote block thanks discussants Chuck Fang and Robert Webb and participants at the 38th Australasian Finance and Banking Conference, the Sydney Banking and Financial Stability Conference and the New Zealand Finance Meeting 2025; Liyao Wang acknowledges National Natural Science Foundation of China Grant No. 72402193 and Research Grant Council of Hong Kong Project No. 12501425; Ming Zeng acknowledges Jan Wallanders och Tom Hedelius stiftelse and Tore Browaldhs stiftelse grant BFh21-0007. There is no conflict-of-interest statement, no data-availability statement and no code-availability statement in the PDF (`data availability` occurs once and only in the sentence about PC-factor data before 1970).
- **Sample period (primary source):** 1963:01 - 2023:12 (732 monthly observations, printed as `N = 732` in Table 2 Panel B).
- **Universe (primary source):** 172 factors with continuous coverage from January 1963 through December 2023, drawn from "Open Source Asset Pricing" (Chen and Zimmermann, 2022), restricted to factors built from continuous signals and formed as value-weighted quintiles, after excluding seven lottery-related anomalies; the underlying equity sample is all U.S. common stocks on NYSE, Amex and Nasdaq with CRSP share codes 10 or 11.
- **Typographic normalization:** typographic en dashes, minus signs, multiplication signs, curly quotation marks and superscripts in the pinned PDF (for example `H-L`, `1963:01 - 2023:12`, `5 x 5`, `R2`, `*`) are rendered as plain ASCII in this record. No value was altered.
- **Schema resolution (read-only):** this run attempted `quant/strategy-research-record-spec-v2.md` in Hermes Wiki Brain and received `file not found`, so it failed closed onto the canonical `quant/strategy-research-record-spec-v1.md`, 10,289 bytes, SHA-256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`, read in full before writing. No schema was invented and no older record was migrated.
- **Pre-write dedup (hidden-inclusive, whole checkout):** `rg -uuu` across `alpha-strategy-research` including `.git`, `.mimo-worktrees`, `.agents` and `.hermes` returned **0 files** for `6053114`, `10.2139/ssrn.6053114`, `ssrn.com/abstract=6053114`, `Factor MAX`, `factor MAX`, `factor-level MAX`, `Predictable Factor Returns`, `Extreme factor returns contain valuable`, `maximum daily return of a factor`, `Liyao Wang`, `lywang@hkbu`, `Ming Zeng`. `coverage_manifest.csv` (5,808 lines) returned 0 hits for `factor max`, `6053114` and `liyao`. A `novy-marx` positive control returned 55 `.md` files, proving the scan was live. `git log --oneline -20` was read only as a convenience glance and was not treated as dedup. Nearest existing records are `crypto-cross-sectional-max-daily-return-lottery-momentum-2026-08-31.md` (stock/coin-level MAX, different aggregation level, different sign of predictability, crypto universe), `crypto-cross-sectional-factor-momentum-anomaly-portfolios-2026-08-31.md` (cumulative-return factor momentum, not extreme-return conditioning, crypto universe), `us-equity-pretom-month-end-liquidity-demand-dispensability-factor-zoo-ssrn-6909918-2026-09-29.md` (month-end liquidity-demand calendar conditioning of the factor zoo, a different signal construction), and `published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23.md` (luck-adjusted anomaly-zoo null results). In every pair the source identity, mechanism, signal construction and material data dependency differ.

## Economic mechanism

### Source-reported

The authors define **factor MAX** as the maximum daily return of a factor within a given month, and propose it as a cross-sectional predictor of factor returns that is distinct from factor momentum, which conditions on cumulative performance over recent horizons. Each month they sort the 172 factors into five quintiles on prior-month MAX, buy quintile 5 and sell quintile 1, and rebalance monthly. Their stated mechanism is **limited-attention underreaction to factor-level news**: a large daily factor return can encode salient, factor-level information (clustered earnings surprises, an FOMC-driven repricing of duration), and attention-constrained investors process that news slowly, so factor prices drift upward after the extreme realization. Supporting claims made by the source: (i) the spread survives five risk models and survives spanning controls for time-series and cross-sectional factor momentum; (ii) it survives spanning controls for stock-level lottery and momentum anomalies; (iii) the spread is concentrated in low-attention factors, in non-extreme macro-news months, and in factor-months without constituent earnings announcements; (iv) it is concentrated in high-eigenvalue principal components of factor returns; (v) an event study shows factor returns drift upward for at least 30 days after a factor's MAX day, while stock returns reverse after a stock's MAX day, which the authors use to reconcile positive factor-level MAX predictability with the negative stock-level MAX effect of Bali, Cakici and Whitelaw (2011). These are the authors' claims, not our findings.

### Research interpretation

- **Regime / conditioning role:** none is required for the baseline; the source's own evidence makes investor attention and the salience of same-day news a *moderator* rather than a separate alpha source.
- **Primary signal:** cross-sectional continuation of factor-portfolio returns after an extreme positive daily realization, hypothesized as **slow incorporation of aggregate news into portfolios-of-portfolios** rather than as compensation for a priced risk factor, because the spread retains positive alphas under CAPM, FF5, FF5+MOM, HXZ and DHS.
- **Falsifiable form:** across a fixed, pre-declared universe of value-weighted equity factor portfolios, the cross-sectional rank of prior-month maximum daily factor return positively predicts next-month equal-weighted factor return, and this relation is not spanned by prior-month factor return, prior-year factor return, or stock-level lottery/momentum characteristics.
- **Candidate economic channel to test:** underreaction is strongest where the *aggregate* news is hardest to arbitrage because it must be processed across many names at once; the alternative explanation the source cannot exclude is that factor MAX proxies for a slowly mean-reverting risk factor that the five risk models omit.
- **Explicit caution:** the strategy is a meta-strategy over factor portfolios. Its tradability is a property of the underlying stock portfolios, not of an abstract index, so any "alpha" claim inherits every cost, borrow and capacity property of ~34 long plus ~34 short value-weighted stock portfolios.

## Signal

All items below are **source-reported** unless marked `research-proposed` or `underspecified`.

- **Formation timestamp:** at the beginning of each month from January 1963 to December 2023, factors are sorted into five groups on the maximum daily factor return realized in the preceding calendar month (Section 3.1). The exact clock, timezone and whether formation uses the last trading day's close or the next month's first print are **underspecified** - the source says only "at the beginning of each month".
- **Lookback:** one calendar month of daily factor returns; MAX = `max` over the daily return series inside month `t`. The number of trading days in the window, the warm-up requirement and endpoint inclusivity are **underspecified**. No minimum-history rule is stated for a factor entering the panel mid-sample.
- **Long entry:** buy the factors in quintile 5 (highest prior-month MAX).
- **Short entry:** sell the factors in quintile 1 (lowest prior-month MAX). The spread is called `H-L` in every table.
- **Portfolio return:** "We calculate the returns of the MAX portfolios in month t + 1 as the equal-weighted average of the factor returns" (Section 3.1). So the meta-portfolio is equal-weighted across factors; each factor itself is a value-weighted stock portfolio.
- **Exit / holding period:** one month; "all portfolios are rebalanced monthly" (Section 3.1 and every table caption). No stop, no take-profit, no partial exit, no overlapping-position rule. Re-entry is automatic at each monthly rebalance.
- **Parameters:** quintile count = 5 (baseline); factor universe = 172; weighting across factors = equal; rebalance = monthly; risk models = CAPM, FF5, FF5+MOM, HXZ, DHS; Newey-West t-statistics. No lag structure, no threshold parameter, no rank cutoff beyond the quintile boundary.
- **Alternate signal definitions the source also reports:** `MAX5` = sum of the five largest daily factor returns in the month (Section 3.4, Table 4 Panel A); decile rather than quintile formation (Table 4 Panel C); factor sets built from the original source papers (Table 4 Panel B), capped value-weighted terciles of Jensen, Kelly and Pedersen (2023) (Table 4 Panel D), and the large common factors of Arnott, Kalesnik and Linnainmaa (2023) (Table 4 Panel E); randomly drawn subsets of 50 and 100 factors repeated 1,000 times (Section 3.4, Figure 3).
- **Moderator used by the source (not part of the baseline):** factor-level attention = the cross-sectional average, over the stocks in the factor's long and short legs, of a firm-level composite attention index built as an average z-score of attention proxies (composition ambiguous, see contradiction 2); and a same-day coincidence flag for extreme macro-news days (aggregate market return, EPU index, VIX) and for constituent earnings announcements in the month.
- **Position sizing:** **underspecified**. The source never states the notional of the long leg versus the short leg, whether the spread is 100/100 or 50/50, whether the portfolio is dollar-neutral, or any leverage. `leverage` occurs once in the whole document and only as variance-scaling of principal components.
- **Order timing, price, order type, fill:** **underspecified** - not stated anywhere in the source.
- **Research-proposed operationalization (clearly not source-reported):** signal computed at the last close of month `t`; orders submitted at the next session's open of month `t+1`; one-month holding; legs sized 100/100 gross. This is a Scout proposal for falsification only and must not be read as the source's rule.

## Required data

- **Instrument:** portfolios of U.S. common stocks; the traded object in the source is a *factor portfolio*, not a single security.
- **Universe:** CRSP share codes 10 or 11 on NYSE, Amex and Nasdaq; 172 factors with continuous coverage 1963:01-2023:12 from Chen and Zimmermann (2022) "Open Source Asset Pricing", restricted to continuous signals and value-weighted quintiles, after removing seven lottery-related anomalies (MaxRet, IdioVol3F, IdioVolAHT, ReturnSkew, ReturnSkew3F, CoskewACX, Coskewness).
- **Venue / market type:** U.S. equity exchanges; secondary listing of the factor series from a public research dataset. Market type: **cash equities**, no derivatives.
- **Timeframe:** daily factor returns to build MAX; monthly factor returns to compute performance; monthly rebalance.
- **Fields:** daily and monthly factor return series (172 series); daily and monthly stock returns including delisting returns when available (CRSP); quarterly and annual accounting variables (Compustat); Compustat RDQ quarterly earnings announcement dates; the Economic Policy Uncertainty index of Baker, Bloom and Davis (2016); the CBOE VIX. For the attention moderator the source additionally names abnormal trading volume, past 12-month returns, analyst coverage, firm advertisement expenditure, absolute value of earnings surprise and 52-week high - which require point-in-time analyst-coverage, advertising-expenditure and earnings-surprise (SUE) series.
- **Point-in-time / availability:** **data gap**. `point-in-time` occurs 0 times, `look-ahead` 0, `survivorship` 0. The only availability caveat printed is "including delisting returns when available".
- **Timestamp:** **data gap** - no timezone, no session convention, no alignment rule is stated.
- **Missing data:** "continuous coverage" is required for universe membership, but no stale/suspended/partial-print rule and no imputation policy is stated; imputation therefore stays **not stated in source**.
- **Funding / fee / spread needs:** **data gap**. No fee, spread, borrow, funding or turnover field is used or discussed anywhere in the pinned text.

## Execution assumptions

The cost treatment was determined at Methods level, by reading Sections 2.1, 2.2, 3, 3.1, 3.2, 3.3, 3.4, 4, 4.1, 4.2, 4.3, the conclusion, the Figure 1-4 captions and all seven table captions, plus a whole-document census of the pinned 63,894-character text layer.

**Census of the pinned primary PDF (count of case-insensitive substring occurrences):**

| term | count | term | count |
|---|---|---|---|
| `transaction cost` / `transaction costs` | 0 / 0 | `bid-ask` / `bid ask` | 0 / 0 |
| `cost` / `costs` | 0 / 0 | `slippage` | 0 |
| `fee` / `fees` | 0 / 0 | `commission` | 0 |
| `funding` | 0 | `borrow` | 0 |
| `short sale` / `shorting` | 0 / 0 | `turnover` | 0 |
| `capacity` | 0 | `market impact` / `latency` | 0 / 0 |
| `order type` / `limit order` / `market order` | 0 / 0 / 0 | `maker` / `taker` / `participation` | 0 / 0 / 0 |
| `liquidity` | 0 | `leverage` (PC variance scaling) | 1 |
| `margin` (the word "marginal") | 1 | `spread` (portfolio high-minus-low spread only) | 25 |

`spread` occurs 25 times and in every instance means the long-short portfolio spread, never a quoted or transacted spread; `leverage` occurs once and means rescaling principal-component factors to the variance of the average factor; `margin` occurs once inside the word "marginal". **Every friction field is therefore a `data gap` and must never be read as a modeled zero.** The source reports only gross returns.

- **Order type / fill model:** not stated in source.
- **Signal-to-order delay / latency:** not stated in source.
- **Fees / commissions:** not stated in source (0 occurrences).
- **Spread / slippage / impact:** not stated in source (0 occurrences).
- **Turnover:** not stated in source (0 occurrences), even though the strategy re-forms two legs of roughly 34 factor portfolios every month.
- **Funding:** not applicable to cash equities in the source and not discussed.
- **Leverage / margin:** not stated in source.
- **Borrow / shorting:** not stated in source; shorting the constituents of ~34 factor portfolios is assumed implicitly and never costed or availability-checked.
- **Capacity / partial fills / failures:** not stated in source.
- **Research-proposed execution for falsification only:** next-session-open fills, full fill at the opening price, and a research-proposed cost ladder of 0 / 5 / 10 / 20 / 50 basis points per side applied to an estimated monthly one-way turnover of the underlying stock legs. None of this is source-reported.

## Evidence

### Source-reported

Every figure below is third-party, source-reported, taken from the pinned 37-page SSRN PDF of Wang and Zeng, and has **not** been independently reproduced. Newey-West t-statistics are in parentheses. All results are U.S. equity factor results over 1963:01-2023:12 - they are **not** crypto evidence.

**Table 1 - Performance of factor MAX portfolios (monthly average returns, Sharpe ratio and alphas, in %):**

| row | P1 | P2 | P3 | P4 | P5 | H-L |
|---|---|---|---|---|---|---|
| Return | 0.09 (3.04) | 0.23 (5.52) | 0.29 (5.73) | 0.37 (6.66) | 0.41 (7.80) | **0.32 (5.89)** |
| SR | 0.17 | 0.12 | 0.26 | 0.28 | 0.27 | 0.25 |
| CAPM alpha | 0.11 (3.62) | 0.26 (5.84) | 0.33 (6.57) | 0.43 (7.47) | 0.46 (8.13) | 0.36 (4.99) |
| FF5 alpha | 0.04 (1.69) | 0.16 (5.69) | 0.20 (5.68) | 0.28 (5.87) | 0.37 (6.84) | 0.33 (5.17) |
| FF5+MOM alpha | 0.03 (1.26) | 0.13 (4.96) | 0.16 (5.35) | 0.21 (5.53) | 0.30 (5.06) | 0.27 (3.52) |
| HXZ alpha | -0.02 (-0.61) | 0.04 (1.13) | 0.09 (2.47) | 0.14 (2.74) | 0.35 (4.88) | 0.37 (4.18) |
| DHS alpha | 0.05 (1.66) | 0.13 (3.51) | 0.17 (3.79) | 0.15 (2.95) | 0.29 (4.49) | 0.24 (3.76) |

Headline claims in prose: Section 1 and Section 3.1 both report the H-L spread as 0.32% per month with t = 5.89; Section 3.1 reports alphas ranging from 0.24% (DHS) to 0.37% (HXZ); Section 3.1 and Figure 1 report a cumulative FF5 alpha of **$9.58 per dollar invested** over 1963:01-2023:12 and state that the strategy "displays limited drawdowns" with no drawdown number printed. Section 3.1 and Figure 2 report the number of factors per leg rising from **22 at the start of 1963** to approximately **34 in 1990** and staying above 34 thereafter.

**Table 2 Panel A - factor momentum comparators:** CSMOM P1 -0.15 (-1.87), P5 0.72 (8.47), H-L 0.87 (5.78), SR 0.18 / 0.31 / 0.27, FF5 -0.17 (-2.22) / 0.81 (9.78) / 0.98 (5.83); TSMOM Short 0.09 (1.56), Long 0.41 (7.58), Long-Short 0.32 (3.34), SR 0.12 / 0.28 / 0.06, FF5 0.03 (0.58) / 0.38 (5.40) / 0.35 (2.85). TSMOM is defined as long factors with positive prior one-year returns skipping one month and short factors with negative returns.

**Table 2 Panel B - spanning tests (N = 732 in every column):** column (1) MAX on CSMOM: alpha 0.14 (2.93), CSMOM loading 0.20 (7.47), adj. R2 0.26; column (2) MAX on TSMOM: alpha 0.26 (4.34), TSMOM loading 0.17 (3.38), adj. R2 0.05; column (3) MAX on both: alpha 0.11 (2.34), CSMOM 0.20 (7.48), TSMOM 0.12 (2.10), adj. R2 0.29; column (4) CSMOM on MAX: alpha 0.46 (3.35), MAX loading 1.28 (9.75), adj. R2 0.26; column (5) TSMOM on MAX: alpha 0.22 (2.51), MAX loading 0.32 (3.22), adj. R2 0.05. Section 3.2 describes the R2 as "approximately 5% to 26%".

**Table 3 - spanning controls for stock-level anomalies (alpha of the factor MAX spread, then the control's loading, then adj. R2):** Panel A lottery: IdioVol3F 0.32 (5.73), -0.01 (-0.16), 0.01; IdioVolAHT 0.32 (6.01), -0.01 (-0.62), 0.01; MaxRet 0.32 (5.92), -0.01 (-0.50), 0.01; ReturnSkew 0.31 (4.84), -0.20 (-3.28), 0.04; ReturnSkew3F 0.29 (4.51), -0.16 (-2.86), 0.02; CoskewACX 0.31 (5.14), 0.04 (1.02), 0.01; Coskewness 0.31 (6.04), 0.02 (0.28), 0.01. Panel B momentum: Mom6m 0.29 (4.84), 0.05 (2.35), 0.02; Mom12m 0.27 (4.35), 0.05 (2.55), 0.03; IndMom 0.31 (5.37), 0.05 (1.97), 0.01; LRreversal 0.30 (5.09), 0.07 (2.89), 0.04; STreversal 0.35 (6.45), -0.15 (-6.85), 0.17.

**Table 4 - robustness:** Panel A (MAX5 = sum of the five largest daily returns) Return 0.02 (0.67) / 0.49 (7.36) / H-L 0.47 (6.72), SR 0.21 / 0.28 / 0.26, FF5 -0.04 (-1.47) / 0.46 (6.32) / 0.50 (5.88). Panel B (factors built per the original papers) Return 0.19 (6.70) / 0.85 (11.81) / 0.65 (9.51), SR 0.31 / 0.55 / 0.42, FF5 0.17 (7.95) / 0.78 (10.22) / 0.61 (8.06). Panel C (decile factors, decile portfolios, H-L = P10 - P1) Return 0.11 (2.60) / 0.71 (7.07) / 0.61 (5.33), SR 0.20 / 0.28 / 0.23, FF5 0.05 (1.29) / 0.73 (6.99) / 0.68 (5.72). Panel D (JKP capped value-weighted terciles) Return 0.10 (4.14) / 0.27 (3.97) / H-L 0.17 (2.58), SR 0.09 / 0.30 / 0.16, FF5 0.08 (3.71) / 0.17 (4.67) / 0.10 (2.05). Panel E (large common factors of Arnott, Kalesnik and Linnainmaa 2023, H-L = P3 - P1) Return 0.12 (2.43) / 0.47 (4.15) / 0.34 (3.21), SR 0.13 / 0.19 / 0.18, FF5 0.02 (0.34) / 0.17 (2.68) / 0.15 (1.95).

**Section 3.4 and Figure 3 - resampling:** drawing 50 factors at random 1,000 times gives 93% of excess-return t-statistics and 98% of FF5-alpha t-statistics above 3; drawing 100 factors 1,000 times gives 99% and 100%. The Introduction summarizes only the 100-factor panel as "99% of excess-return spreads and 100% of risk-adjusted alphas remain statistically significant at the 1% level".

**Table 5 - attention double sort (monthly average returns, 5 x 5):** Panel A (MAX), attention rows P1..P5 then H-L column: Low 0.24 / 0.31 / 0.29 / 0.41 / 0.67 / **0.43 (3.03)**; P2 0.11 / 0.25 / 0.21 / 0.21 / 0.47 / 0.36 (2.86); P3 0.09 / 0.23 / 0.27 / 0.38 / 0.40 / 0.31 (2.14); P4 0.13 / 0.15 / 0.30 / 0.36 / 0.21 / 0.08 (0.49); High 0.06 / 0.19 / 0.33 / 0.21 / -0.03 / **-0.08 (-0.55)**; bottom cross-attention row -0.17 (-1.53) / -0.11 (-1.18) / 0.04 (0.38) / -0.20 (-1.85) / -0.68 (-3.72) / **-0.55 (-2.88)**. Panel B (factor MOM): Low ... 0.96 (4.79); High ... 0.71 (3.12); bottom row -0.16 (-1.18) / -0.02 (-0.16) / -0.13 (-1.22) / -0.32 (-2.90) / -0.42 (-3.01) / -0.26 (-1.18). Section 4.1 states the low-attention spread as 0.43% per month (t = 3.03); the Introduction states 0.42% (t = 2.93) for the same statistic - see contradiction 1.

**Table 6 - macro-news and earnings conditioning (P1 / P5 / H-L, return and FF5 alpha):** Panel A market-return extreme: 0.04 (0.66) / 0.13 (1.04) / 0.13 (0.96), FF5 0.01 (0.13) / 0.10 (0.70) / 0.12 (0.78); non-extreme: 0.11 (3.47) / 0.54 (8.88) / 0.44 (6.75), FF5 0.06 (0.20) / 0.45 (5.80) / 0.40 (4.58). Panel B EPU extreme: -0.05 (-0.45) / 0.35 (1.38) / 0.21 (0.80), FF5 -0.11 (-0.94) / 0.32 (1.26) / 0.15 (0.66); non-extreme: 0.10 (3.23) / 0.46 (6.94) / 0.36 (6.11), FF5 0.05 (1.96) / 0.40 (6.58) / 0.35 (5.11). Panel C VIX extreme: -0.12 (-1.03) / 0.14 (0.31) / 0.27 (0.61), FF5 -0.22 (-1.41) / 0.52 (1.22) / 0.78 (1.91); non-extreme: 0.12 (2.99) / 0.37 (5.01) / 0.24 (2.81), FF5 0.09 (2.60) / 0.36 (4.34) / 0.27 (2.77). Panel D earnings announcements present: 0.34 (5.58) / 0.16 (2.03) / **-0.19 (-1.98)**, FF5 0.29 (4.79) / 0.17 (2.13) / -0.12 (-1.12); no earnings announcements: 0.08 (2.12) / 0.28 (3.69) / 0.20 (2.50), FF5 0.03 (0.97) / 0.25 (3.46) / 0.21 (2.38).

**Table 7 - factor MAX across eigenvalue-ordered principal components (returns and FF5 alpha):** PC1-PC20 0.39 (3.02) marked `***` and FF5 0.48 (2.95) marked `***`, adj. R2 0.01 / 0.01; PC21-PC40 0.22 (1.91) marked `*` and FF5 0.18 (1.48), adj. R2 0.01 / 0.03; PC41-PC60 0.21 (1.55) and FF5 0.33 (1.98) marked `**`, adj. R2 0.01 / 0.01; PC61-PC80 0.02 (0.10) and FF5 0.02 (0.12); PC81-PC100 -0.04 (-0.24) and FF5 -0.14 (-0.98); PC101-PC122 -0.05 (-0.30) and FF5 0.05 (0.32). Section 4.2 and Table 7 use 122 factors with data before 1970 and a rolling 10-year daily-return window for eigenvectors.

**Figures 1-4:** Figure 1 cumulative log returns and FF5 alpha of the H-L spread; Figure 2 count of factors per leg (22 in 1963 rising to about 34 by 1990); Figure 3 t-statistic distributions of the 1,000-draw resampling; Figure 4 event study around day-zero (the day a stock or factor earns its monthly MAX) from 10 days before to 50 days after, with a shaded 95% confidence interval, showing stock cumulative abnormal returns declining after day zero while factor cumulative raw returns "continue to drift upward for at least for the following 30 days". No numeric series is printed for Figures 1-4 beyond the axis labels, so the event-study magnitudes are **data gap**.

**Arithmetic-only consistency checks run by the Scout (no external data, no backtest):** 0.41 - 0.09 = 0.32 matches Table 1 H-L; 732 months / 12 = 61 years, matching 1963:01-2023:12 and the printed `N = 732`; 172 / 5 = 34.4, matching the "approximately 34" factors per leg; 20 x 5 + 22 = 122 matches the PC subsets; 0.24 / 0.32 = 0.75, so the smallest alpha is 75% of the raw spread, consistent with the prose claim that "a significant share" remains unexplained; Table 4 H-L cells reproduce as 0.47 = 0.49 - 0.02, 0.66 vs printed 0.65, 0.60 vs printed 0.61, 0.17 = 0.27 - 0.10, 0.35 vs printed 0.34 (all within one rounding unit); Table 5 Panel A Low H-L reproduces as 0.67 - 0.24 = 0.43. One check does **not** close: the Table 5 Panel A bottom-row H-L cell of -0.55 implies a cross-attention difference of about -0.52 with a rounding band of roughly [-0.54, -0.50] from the printed cells, leaving a gap of up to 0.03 percentage points - recorded as an unreconciled presentation gap rather than a contradiction. A second check is diagnostic rather than confirmatory: reading the Table 1 SR row as a *monthly* ratio (0.32 / 0.25 implies a monthly standard deviation of 1.28%) gives a plain t of about 6.76 against the printed Newey-West 5.89, whereas reading it as an *annualised* ratio implies a plain t of about 1.95; the monthly reading is the only arithmetically coherent one, and the source never states the annualisation (`annualiz` occurs 0 times).

### Independently reproduced

not independently reproduced

### Negative evidence

1. **There is no cost model of any kind.** In the pinned 63,894-character text, `cost`, `costs`, `slippage`, `commission`, `bid-ask`, `fee`, `fees`, `funding`, `borrow`, `short sale`, `turnover`, `capacity`, `market impact`, `latency`, `order type`, `limit order`, `market order`, `maker`, `taker`, `participation` and `liquidity` all occur **0** times. Every printed return and alpha is gross; net-of-cost performance is a `data gap`, never a zero.
2. **Turnover is never reported**, even though the strategy re-forms two legs of roughly 34 value-weighted stock portfolios every month for 732 months. Cost drag cannot be bounded from the source.
3. **The short leg is assumed, not demonstrated.** Shorting the constituents of ~34 factor portfolios simultaneously is required; borrow availability, locate rules and borrow fees are absent (`borrow` 0, `short sale` 0).
4. **Sizing and gross notional are absent.** The meta-portfolio return is "the equal-weighted average of the factor returns", but the long-versus-short notional split, dollar-neutrality and any leverage are never stated.
5. **The Sharpe-ratio row is not interpretable from the source.** `annualiz` occurs 0 times and the Table 1 caption only says "Sharpe ratio (SR)". The research-computed diagnostic in the Evidence section favours a monthly reading but the source prints no factor.
6. **A printed cross-group difference cannot be reproduced.** Table 5 Panel A's bottom-row H-L cell of -0.55 sits about 0.03 pp outside the band implied by the printed cells (research-computed, see Evidence).
7. **The effect disappears in every extreme-macro-news partition.** Table 6 reports H-L of 0.13 (t 0.96) for market-return extremes, 0.21 (0.80) for EPU extremes and 0.27 (0.61) for VIX extremes - all statistically insignificant - while the corresponding non-extreme subsamples carry the entire effect (0.44/6.75, 0.36/6.11, 0.24/2.81).
8. **The effect is negative in earnings months.** Table 6 Panel D reports H-L of -0.19 with t = -1.98 when any leg constituent reports earnings that month, i.e. negative and, under a conventional two-sided 5% cutoff, statistically significant - yet both the Introduction and Section 4.1 call this subsample "insignificant". The source never states its significance threshold (see contradiction 4), so the characterization cannot be adjudicated from the source.
9. **The conditioning variables carry lookahead risk.** To exploit the profitable subsamples an implementer must know, at formation, a factor's MAX day, whether that day coincides with an extreme macro-news day, and whether leg constituents report earnings *that month* - the third of which uses information dated inside the return month. `point-in-time`, `look-ahead` and `survivorship` all occur 0 times.
10. **Universe breadth drifts sharply.** Each leg holds about 22 factors at the start of 1963 against roughly 34 from 1990 (Section 3.1, Figure 2), so early-period quintiles are built on a much thinner factor zoo. No sub-period or decade breakdown of the headline spread is printed.
11. **The universe is pre-purged.** Seven lottery-related anomalies (MaxRet, IdioVol3F, IdioVolAHT, ReturnSkew, ReturnSkew3F, CoskewACX, Coskewness) are excluded before the sort, so the headline spread is measured on a filtered zoo and no full-zoo implementation is reported.
12. **Factor momentum is the larger raw trade and absorbs most of the spread.** Table 2 Panel A: CSMOM H-L is 0.87%/month (t 5.78) against factor MAX's 0.32%; Table 2 Panel B column (3) shows factor MAX's alpha falls to 0.11%/month (t 2.34) once CSMOM and TSMOM are both controlled, i.e. roughly two thirds of the raw spread is shared with factor momentum.
13. **Risk-adjusted monotonicity fails.** Table 1 DHS alphas across P1..P5 run 0.05, 0.13, 0.17, 0.15, 0.29 (P4 below P3), and the SR row is non-monotone (0.17, 0.12, 0.26, 0.28, 0.27), so only raw returns are monotone in MAX.
14. **One robustness universe does not clear a conventional threshold.** Table 4 Panel E (large common factors) reports a raw spread of 0.34 (t 3.21) but an FF5 alpha of 0.15 with t = 1.95.
15. **The principal-component result is a single-subset result.** Table 7 is significant only for PC1-PC20; PC21-PC40 returns give t = 1.91, PC41-PC60 returns t = 1.55, and from PC61 onward every estimate is near zero or negative with adj. R2 between 0.01 and 0.03.
16. **No multiplicity control anywhere.** `benjamini`, `bonferroni`, `holm`, `fdr`, `multiple test`, `multiplicity`, `deflated` and `p-hacking` all occur 0 times, across a family that includes 5 quintile buckets x 5 risk models, 4 alternative universes plus a decile and a MAX5 variant, 12 spanning controls, 2 momentum benchmarks, a 5 x 5 double sort, 4 news partitions, 6 PC subsets and a 1,000-draw resampling experiment.
17. **No seed.** `seed` and `random seed` occur 0 times, so the exact Figure 3 resampling distribution is not reproducible.
18. **No code and no replication package.** `source code`, `github`, `software`, `code availability`, `python`, `matlab` and `replication package` all occur 0 times. The underlying factor data (Chen and Zimmermann, 2022) is public, so a from-scratch reconstruction is possible, but nothing is published by the authors.
19. **No temporal validation.** `walk-forward`, `holdout`, `point-in-time` and `look-ahead` all occur 0 times; `out-of-sample` occurs exactly once and refers only to the PC eigenvector estimation window. Every headline number is a full-sample in-place estimate over 1963-2023.
20. **Survivorship handling is conditional.** Section 2.2 includes delisting returns only "when available".
21. **Risk reporting is thin.** `drawdown` occurs once, in prose ("displays limited drawdowns"), with no number; `cagr`, win rate and capacity are absent entirely. The only risk figures are the SR row and Newey-West t-statistics.
22. **Publication status is unverified preprint.** No acceptance, forthcoming or under-review statement exists in the primary source; the "R&R at Review of Asset Pricing Studies" claim comes only from an author page. Four versions of the same statistic already drift between the November 2025 and December 2025 drafts (see contradictions), so revision risk is demonstrated rather than hypothetical.
23. **The moderator's inputs are untested for data lags.** Analyst coverage, absolute earnings surprise, firm advertisement expenditure and 52-week high all require point-in-time fundamental and analyst series; the source states no availability lag, revision policy or vendor for any of them.

## Falsification plan

Every threshold below is a **research-defined falsification threshold**; every rule marked *research-proposed* is a Scout operationalization, not a source-reported choice. All gates are pre-registered before any data is touched.

- **F1 - Printed-value reproduction.** Rebuild the 172-factor panel from Chen and Zimmermann (2022) exactly as Section 2.2 describes and re-run the baseline quintile sort. *Fail:* the reproduced H-L monthly return is outside 0.32 +/- 0.05 pp, or its Newey-West t falls outside [4.49, 5.89] - the interval deliberately spans both the December (5.89) and November (4.49) printed values so the version drift is forced into the open. *Action:* stop; reconcile the two drafts before any further work.
- **F2 - Net-of-cost gate.** Apply a *research-proposed* per-side cost ladder of 0 / 5 / 10 / 20 / 50 bp to the underlying stock legs with a *research-proposed* turnover estimate derived from the actual monthly re-forming of both legs. *Fail:* at 10 bp per side the net H-L monthly return is <= 0, or the net Sharpe falls below 0.50 times the gross Sharpe. *Action:* record the strategy as cost-infeasible and stop.
- **F3 - Borrow and short-leg gate.** Attempt the short leg over the constituents of the bottom quintile. *Fail:* more than 10% of required short notional is unavailable at a borrow fee above 50 bp annualised, *research-defined*. *Action:* re-run as a long-only underweight implementation and treat any surviving spread as a different hypothesis.
- **F4 - Capacity gate.** Scale the meta-portfolio to a *research-proposed* 10% of median daily dollar volume of the underlying names. *Fail:* realised implementation shortfall removes more than 50% of the gross monthly spread, *research-defined*. *Action:* mark capacity-bounded and stop.
- **F5 - Signal-definition gate (targets contradiction 3).** Pre-declare one PC-section signal (MAX, MAX5, or mean-of-top-k) before running Table 7's replication. *Fail:* the sign of the PC21-PC40 spread changes across the three candidate definitions, or PC1-PC20 significance depends on which definition is chosen. *Action:* declare Table 7 non-interpretable and drop the systematicity claim.
- **F6 - Attention-composition gate (targets contradiction 2).** Rebuild the attention index in both published compositions (five proxies, and six proxies including firm advertisement expenditure). *Fail:* the low-minus-high attention spread difference (printed -0.55, t -2.88) changes sign or loses significance under either composition. *Action:* treat the moderator as underspecified and unusable.
- **F7 - Conditioning-variable point-in-time gate.** Rebuild the extreme-macro-news flag and the earnings flag using only data published by the formation date. *Fail:* any part of the classification requires information dated on or after the first day of the return month, or the earnings flag cannot be formed point-in-time at all. *Action:* discard all Table 6 conditioning results and evaluate only the unconditional baseline.
- **F8 - Conditional-versus-unconditional gate.** The source's own evidence puts the entire effect in non-extreme, low-attention, no-earnings months. *Fail:* a *research-proposed* pre-declared portfolio restricted to those source-defined subsamples does not retain Newey-West t >= 1.96 on data after 2023-12. *Action:* reject the conditional thesis rather than the unconditional one, and say which was rejected.
- **F9 - Factor-momentum span gate.** *Fail:* on out-of-sample data the factor-MAX alpha after jointly controlling CSMOM and TSMOM falls to <= 0 or t < 1.96 (baseline in-sample value 0.11, t 2.34). *Action:* conclude factor MAX is a repackaged factor-momentum signal.
- **F10 - Lottery-exclusion robustness gate.** Re-run the baseline with the seven excluded lottery anomalies restored to the universe. *Fail:* the H-L spread changes by more than 20% in magnitude or loses significance, *research-defined*. *Action:* conclude the headline depends on the pre-filter.
- **F11 - Universe-breadth gate.** Split the sample at 1990 (the point where the source says breadth stabilises above 34). *Fail:* the pre-1990 sub-sample H-L t < 1.96 while the post-1990 sub-sample is significant, or vice versa, *research-defined*. *Action:* restrict the claim to the sub-sample that survives and state the regime dependence.
- **F12 - Multiplicity gate.** Apply Benjamini-Hochberg at q < 0.10 across the full family enumerated in negative-evidence item 16, plus a deflated-Sharpe adjustment for the number of variants tried. *Fail:* the baseline H-L is no longer significant after correction. *Action:* reclassify the result as selection-contaminated.
- **F13 - Frozen forward window.** Freeze the baseline (MAX = single maximum daily factor return, 5 quintiles, 172-factor universe, equal weighting, monthly rebalance, no moderator) and evaluate 2024-01 forward for at least 24 months, *research-defined*. *Fail:* forward monthly H-L <= 0, or Newey-West t < 1.96. *Action:* report as temporally unstable and stop.
- **F14 - Risk-model robustness gate.** *Fail:* on the frozen forward window the spread is absorbed by any two of CAPM, FF5, FF5+MOM, HXZ and DHS simultaneously (alpha <= 0 with t < 1.96). *Action:* reclassify as an omitted-risk-factor story rather than underreaction.

**Global no-retuning rule:** the 172-factor universe, the seven-anomaly exclusion, MAX as the single maximum daily return, 5 quintiles, equal weighting across factors, monthly rebalance, the five risk models, the 1963:01-2023:12 sample, the sign convention (long high-MAX, short low-MAX) and the absence of any cost model in the source are frozen. A failed gate may not be rescued by switching to MAX5, by changing the quintile count, by re-selecting the universe, by re-tuning the attention or news partitions, by extending the sample, or by introducing a cost assumption that was not pre-declared.

## Crypto portability

**adapted - performance unproven.**

The pinned source contains zero occurrences of `crypto`, `bitcoin`, `ethereum`, `perpetual`, `futures`, `options` and `etf`. There is no crypto evidence of any kind in this record.

- **What ports mechanically:** the *statistic* - the maximum daily return of a portfolio over a month, cross-sectionally ranked and sorted into quintiles - is asset-class agnostic, provided one can construct a panel of daily-return "factor" series. A crypto analogue would need a pre-declared zoo of crypto anomaly portfolios with continuous daily histories, which the repository already studies from other angles.
- **What does not port:** the underlying object. In the source each factor is a value-weighted portfolio of U.S. equities with a borrowable short leg; crypto portfolios differ on shorting (perpetual-futures synthetic shorts versus hard-to-borrow spot), on funding payments, on 24/7 sessions so that "a month" of daily returns has no natural boundary, on candle boundaries and timezone alignment, on venue fragmentation and index/price-source differences, on listing and delisting survivorship in the factor inputs, and on the fact that many crypto "factors" are single-asset or thin cross-sections rather than diversified value-weighted books.
- **Concentration risk:** the source's own mechanism (limited attention to aggregate news) is calibrated to a market with scheduled macro and earnings announcements; crypto has a different salience calendar, so the moderator would have to be re-derived rather than copied.
- **Boundary:** portability is a hypothesis about mechanism only. Nothing here is crypto empirical evidence, and nothing here authorizes crypto trading.

## Limitations

- `underspecified`: formation clock and timezone; warm-up and endpoint conventions; long/short notional split, dollar-neutrality and leverage; order type, fill model, signal-to-order delay; turnover; Sharpe annualisation; missing-data policy; timestamp conventions; point-in-time availability of every moderator input.
- `data gap`: all transaction-cost, spread, slippage, commission, fee, borrow, funding, capacity, latency and participation fields (0 occurrences each); no drawdown number, no CAGR, no win rate, no capacity analysis; no numeric series behind Figures 1-4.
- `not independently reproduced`: every performance figure in this record is source-reported; only arithmetic identities internal to the printed tables were checked.
- `unproven`: the limited-attention mechanism is consistent with the subsample evidence but is not identified - an omitted slowly-varying risk factor remains an open alternative explanation, and the source itself cannot exclude it.
- Publication-bias and revision risk are live: this is an unrefereed working paper whose own two most recent drafts disagree on at least four printed statistics.
- Version caveat: only the December 2025 / 37-page SSRN PDF pinned above was used for numbers; the SSRN landing page and the Crossref record were used only for identity and status.
- Related but distinct source not used for any figure here: the first author's earlier *Factor MAX in the Chinese Market* meeting paper (`https://www.efmaefm.org/0EFMAMEETINGS/EFMA%20ANNUAL%20MEETINGS/2025-Greece/papers/MAX.pdf`) reports a risk-adjusted factor MAX premium of 0.82% per month in China A-shares. It is a different study, a different market and a different source identity, and it is recorded here only so a future run treats it as a separate candidate rather than a duplicate.
- No market data was downloaded, no backtest was run, no third-party code was executed, and no dependencies were installed during this run.

## Implementation status

`implementation_status: not-implemented`. Nothing in this record has been implemented in our research stack. No Qlib backtest, no NautilusTrader change, no Paper, Testnet or Live run has occurred, and no candidate pool, Wiki Brain record or leaderboard entry has been produced by this capture.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record in the repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. Research capture is not adoption, and crypto portability is not authorization to trade.

## Related Wiki records

- [[quant/crypto-cross-sectional-factor-zoo-iterative-alpha-compression-2026-09-01]] - factor-zoo redundancy and spanning; adjacent in subject (the factor zoo as an object) but a different mechanism (alpha-based factor selection versus extreme-return conditioning), a different universe (crypto versus U.S. equities) and a different source.
- [[quant/crypto-perp-vol-scaled-cross-sectional-momentum-factor-2026-09-12]] - cross-sectional momentum over perpetual futures; adjacent in subject (cross-sectional ranking of return-based signals) but a different mechanism (cumulative return rather than within-month maximum), a different universe and a different material data dependency (perpetual-futures funding and venue data).

Two read-only Wiki Brain searches returned zero pages for factor-MAX / attention-underreaction / month-end-liquidity queries; no page was fabricated, and no Wiki Brain page was written by this run.

## Sources

1. Liyao Wang and Ming Zeng, *Factor MAX and Predictable Factor Returns*, SSRN working paper, Date Written December 01, 2025, posted 19 Jan 2026, 37 pages. Landing: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6053114 - DOI: https://doi.org/10.2139/ssrn.6053114 - Pinned PDF: https://papers.ssrn.com/sol3/Delivery.cfm/6053114.pdf?abstractid=6053114&mirid=1 (359,440 bytes, SHA-256 `6d170dd9709bab69e4a0e06b4dca701fdb9371f8835581a6cbe8dc038685fc46`, fetched 2026-09-30). **Sole source of every empirical figure in this record.**
2. Crossref metadata for the DOI: https://api.crossref.org/works/10.2139/ssrn.6053114 - used only for author order, title, DOI, `posted-content` / `preprint` type and deposit dates.
3. Hong Kong Baptist University institutional repository record: https://scholars.hkbu.edu.hk/en/publications/factor-max-and-predictable-factor-returns/ - used only for the 37-page count, the DOI and the `Published - 19 Jan 2026` status label.
4. Ming Zeng, working papers page: https://sites.google.com/view/ming-zeng/working-papers - used only for the unverified "R&R at Review of Asset Pricing Studies" claim.
5. Version-drift cross-check (no figure taken from it): https://sbfc.sydney.edu.au/2025/papers/SBFC2025_1E2_P216.pdf - November 2025 conference author PDF, 290,324 bytes, SHA-256 `f9bf91edbaadc2cc49cc155ce85db2fc50a74e7a5a5022da82245752231230cd`.
6. Works cited *by* the primary source and named above only as the origin of a dataset or a comparator, not as evidence for this strategy: Andrew Y. Chen and Tobias Zimmermann, "Open source cross-sectional asset pricing", *Critical Finance Review* 27, 207-264 (2022); Turan G. Bali, Nicolas Cakici and Robert F. Whitelaw, "Maxing out: stocks as lotteries and the cross-section of expected returns", *Journal of Financial Economics* 99, 427-446 (2011); Sina Ehsani and Juhani T. Linnainmaa, "Factor momentum and the momentum factor", *Journal of Finance* 77, 1877-1919 (2022); Ralph D. Arnott, Viktor Kalesnik and Juhani T. Linnainmaa, "Factor Momentum", *Review of Financial Studies* 36, 3034-3070 (2023).
