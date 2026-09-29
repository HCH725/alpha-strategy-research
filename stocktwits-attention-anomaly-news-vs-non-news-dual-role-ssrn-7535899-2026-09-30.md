---
schema: strategy-research-record-v1
title: StockTwits Attention Conditioning of the Composite NET Anomaly Long-Short Spread on News vs Non-News Days
created: 2026-09-30
updated: 2026-09-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-29
sources:
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7535899
  - https://doi.org/10.2139/ssrn.7535899
  - https://papers.ssrn.com/sol3/Delivery.cfm/7535899.pdf?abstractid=7535899&mirid=1&download=yes
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# StockTwits Attention Conditioning of the Composite NET Anomaly Long-Short Spread on News vs Non-News Days

## Provenance

- **Primary source (only source used for every number below):** SSRN working paper `10.2139/ssrn.7535899`, Arseny Gorbenko and Hang Wang, *A Tale of Two Days: Social Media Attention and Anomalies on News and Non-News Days*, draft dated September 2026, 58 pages including a 2-page Internet Appendix.
- **Author list exactly as source (title page, footnote 1, and the landing-page `citation_author` meta tags all agree):** exactly two authors - Arseny Gorbenko, Department of Banking and Finance, Monash University, Australia (`arseny.gorbenko@monash.edu`); Hang Wang, Department of Finance, School of Economics, Jinan University (`hangwang@jnu.edu.cn`). No ORCID, no funding statement, no conflict statement, no acknowledgments section, no data-availability statement and no code-availability statement appear in the PDF - those fields stay `data gap`.
- **Version / dates:** title page reads "This draft: September 2026"; the SSRN landing page (read 2026-09-30) prints `citation_online_date 2026/09/29`, `citation_publication_date 2026/09/28` and `citation_doi 10.2139/ssrn.7535899`; the pinned PDF metadata `/CreationDate` and `/ModDate` are both `D:20260928180710+10'00'`. Single undated version on SSRN; no revision history is exposed, so "version" is `not stated in source` beyond the September 2026 draft date.
- **Publication / peer-review status:** SSRN working paper only. No journal reference, no publisher DOI other than the SSRN DOI, and no peer-review claim are printed anywhere in the PDF or on the landing page - publication status is `not stated in source`, and the work is unrefereed as of 2026-09-30.
- **Primary-source checksum (performed 2026-09-30):** PDF fetched from the SSRN delivery endpoint above (Cloudflare clearance obtained in a real browser first, then a single in-page `fetch` with `download=yes` and immediate chunked transfer to disk) - **808,338 bytes, SHA-256 `0b8c61426b0be46d4d5250279bbf3644c2e48ddfd836bcac1ac3ce3c9c902c27`**, 58 pages, extracted with `pypdf` to 116,235 characters over 2,096 text lines and read end to end: title page and abstract (pages 1-2), Section 1 Introduction (pages 3-8), Section 2 Data and 2.1-2.3 (pages 9-13), Section 3 Main Results with 3.1-3.3 (pages 14-21), Section 4 Mechanism 4.1-4.2 (pages 22-29), Section 5 Robustness 5.1-5.4 (pages 30-36), Section 6 Conclusion (page 36), the 38-item reference list (pages 37-40), Appendix A Table A1 variable definitions (pages 41-43), Figure 1 and Figure 2 captions (pages 44-45), Tables 1-10 (pages 46-56) and Internet Appendix Tables IA1-IA2 (pages 57-58). Figures 1 and 2 are images; their values are reported here only through the Section 3.1 / Section 3.2 prose that states them, and that fact is flagged wherever those values are used.
- **Retrieval note:** the SSRN `Delivery.cfm` endpoint returns an SSRN-Alert registration page (HTTP 200, `text/html`, 26,376 bytes) for the default and `&type=2` variants; only the `&download=yes` variant returned `application/pdf` at 808,338 bytes. The previous scout run could not obtain the PDF and therefore correctly wrote no record; this run did obtain it, so all Methods-, table- and figure-level fields below come from the pinned primary source rather than from the abstract.
- **Deterministic source-identity dedup (hidden-inclusive, pre-write, 2026-09-30):** `rg -uuu` over the whole checkout including `.git`, `.mimo-worktrees`, `.agents`, `.hermes` and any manifest files for `7535899`, `A Tale of Two Days`, `Arseny Gorbenko` and `hangwang@jnu` returned **zero files** (rg exit 1). Follow-up searches for `StockTwits` returned 7 files, `Engelberg, McLean|anomalies and news|NET anomaly score|composite anomaly` returned 0 files, and `NUMhigh|non-news days|attention suppresses|news-day effect` returned 0 files. A `novy-marx` positive control returned 35 files in the same session, confirming the pattern machinery was live. The single `Gorbenko` hit is `crypto-prediction-market-layered-informed-trading-skill-score-2026-09-01.md`, which cites Vyacheslav Gorbenko (a different author, SSRN 5227845) - not this source identity. `git log --oneline -20` was used as a convenience glance only, not as dedup.
- **Four-axis distinction against adjacent existing records:** (a) `retail-investor-horizon-pead-stocktwits-long-short-2026-09-23.md` (arXiv 2512.00280) uses StockTwits-adjacent retail data but tests a retail-horizon / earnings-announcement mechanism with a different source and a different signal; (b) `pure-news-residual-embedding-cross-sectional-long-short-anomaly-2026-09-26.md` is a pure-news residual-embedding anomaly with a different source and no attention moderator; (c) `directional-anomaly-zoo-net-cost-audit-quality-survivor-2026-09-23.md` and `published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23.md` audit the anomaly zoo itself rather than conditioning anomaly returns on a same-day attention x news split; (d) `forum-diffusion-speed-excess-comovement-lead-lag-2026-09-24.md` studies forum diffusion and co-movement, not anomaly returns. Source identity and mechanism differ in every pair, so no existing artifact covers this hypothesis.

## Economic mechanism

### Source-reported

The authors argue that financial social media plays a dual role that depends on whether the attention is backed by genuine information:

- On days with no firm-specific information release, user-generated posts are produced to attract attention rather than to convey new material information, so heightened attention amplifies existing biased beliefs and therefore increases mispricing; because short-leg stocks carry investor overoptimism (Stambaugh, Yu, and Yuan 2012) and attract disproportionately bullish social media content (Engelberg, Hwang, Lu, and Mullins 2026), the amplification pushes the anomaly spread in the "wrong" direction.
- On earnings and corporate-news days, the same attention broadens awareness of genuine news and accelerates its incorporation into prices, so anomaly returns are larger than on comparable news days without an attention spike.
- The abstract states the conclusion verbatim: social media attention "suppresses anomaly returns on non-news days but amplifies them on news days", it "decreas[es] mispricing on news days by facilitating information dissemination and increasing mispricing on non-news days by amplifying biased beliefs", and because both the long and the short leg contribute significantly, "attention-driven buying price pressures play a minor role".
- The paper explicitly positions this against a pure attention-induced price-pressure account: the long- and short-leg effects have opposite signs within a day type, and there is no reversal after high-attention news days but a partial reversal after high-attention non-news days.

### Research interpretation

The falsifiable hypothesis captured here is a moderator claim, not a new premium:

- **Regime / moderator:** same-day abnormal retail-attention state (top-quartile abnormal StockTwits message count) crossed with same-day firm information state (earnings announcement or filtered Dow Jones/Wall Street Journal story).
- **Conditional anomaly spread:** the composite NET long-short anomaly spread (quintile 5 minus quintile 1 of the Chen-Zimmermann NET score) is predicted to be lower - potentially negative - on high-attention non-news days and higher on high-attention news days, relative to the same spread on other days.
- **Proposed friction channel (our framing, not the source's):** the non-news-day suppression is a behavioral mispricing effect that is expensive to arbitrage exactly where it is largest (small, illiquid, retail-heavy names), so any implementable version is a net-of-cost question first and a signal question second.
- **Missing links we do not assume:** the paper does not establish that the conditioning variable is knowable before the return is realized (its `Earn` day rule and its same-day message count both use same-day information), and it does not establish that the effect survives shorting costs, spreads or turnover. Those are open, not implied.

## Signal

The source is an explanatory event-conditioning study, not a trading rule. What follows is the source-reported construction, followed by what remains underspecified.

**Source-reported construction**

- **Anomaly score (NET):** monthly characteristics from Chen and Zimmermann (2022) `openassetpricing.com`; only "clearly significant" and "likely significant" anomalies are retained (**209 in total**), then three discrete variables (Governance, NumEarnIncrease, MS) are excluded per footnote 5 - the source does not state whether the 209 count precedes or follows that exclusion, so the exact anomaly count is `underspecified` (the abstract and conclusion both say "more than 200"). Stocks are sorted into quintiles on the signed characteristic at the end of each month; the first (fifth) quintile is the short (long) leg; indicator-type anomalies load on one side only. `NET = Long - Short` counts, i.e. the number of long-side anomaly portfolios minus the number of short-side portfolios a stock belongs to at the end of month t-1 (Appendix Table A1).
- **Portfolio formation:** "At the end of each month, we sort stocks into quintile portfolios by NET and compute the average daily equal-weighted portfolio return over the following month" (Section 3.1). For the regression-level indicators, Appendix Table A1 says `Long NET` / `Short NET` are set by sorting stocks into quintiles on NET **each day** - the source does not reconcile the monthly formation sort with the daily indicator sort, so the exact rebalancing convention for the indicator version is `underspecified`.
- **Attention state (`ANUM`, `NUMhigh`):** StockTwits daily message counts per firm from the Cookson and Niessner (2020) public data release. `ANUM = (messages on day t - mean of messages over the past one year excluding the most recent month) / that mean`. `NUMhigh = 1` for stocks in the top quartile of the daily cross-sectional distribution of `ANUM` (i.e. the indicator covers the unconditional 25% of stock-days). An indicator rather than the continuous measure is used because `ANUM` is extremely right-skewed.
- **Information states:** `Earn = 1` on the trading day with the highest market-share-adjusted volume in the 3-day window around the Compustat announcement date (compensation for after-close releases and for Compustat recording no time); `News = 1` on a 1-day window around a RavenPack Dow Jones Edition story (Dow Jones Newswire + Wall Street Journal) with novelty and relevance scores at or above 100, with after-hours stories assigned to the next trading day; `Inf = Earn or News` (used from Table 4 onward).
- **Baseline regression (Eq. 1):** daily stock return (bps) on `NET`, `NET x NUMhigh`, `NET x Earn`, `NET x News`, `NUMhigh`, `Earn`, `News`, ten daily lags of returns, squared returns and turnover, plus day fixed effects; standard errors double-clustered by firm and day. Columns (2)-(4) of Table 3 add the triple interactions, with the `News` triple printed in columns (2) and (4) and the `Earn` triple printed in columns (3) and (4).
- **Sample screen:** US CRSP stocks with a price of at least $5 at the beginning of the month; final sample 3,906,742 firm-day observations; regression NObs 3,902,416.

**Underspecified / research-proposed (never source-reported)**

- The source specifies **no** entry rule, exit rule, holding period, position sizing, order type, execution timestamp, universe filter for tradability, or signal-to-order delay. Any statement about how one would trade the conditional spread is `research-proposed`.
- The `Earn` day is chosen by same-day volume and `NUMhigh` uses same-day message counts, so both states are only fully known at or after the close; a tradable decision timestamp must therefore be chosen by us and is `research-proposed`.
- Any threshold used in the falsification plan below (cost ladder levels, Sharpe floors, attenuation limits, subsample windows) is `research-defined falsification threshold`.

## Required data

- **Instrument / universe:** US common stocks on CRSP, price >= $5 at the start of the month; no exchange filter stated; no explicit delisting or survivorship treatment stated (`data gap`). Sample period **2010-2021** (stated in the Section 3.2 discussion of Table 3 and again in the Section 6 conclusion).
- **Venue / market type:** US equity cash market only; no futures, options, crypto or non-US instruments appear anywhere in the paper.
- **Timeframe:** daily close-to-close returns; monthly anomaly formation; daily cross-sectional attention state.
- **Fields needed:** StockTwits daily per-firm message counts (public Cookson-Niessner release) and StockTwits bullish/bearish declarations from Cookson, Engelberg, and Mullins (2023); Chen-Zimmermann monthly anomaly characteristics (public, `openassetpricing.com`); CRSP returns, prices, shares outstanding, volume; Compustat quarterly earnings announcement dates; RavenPack Dow Jones Edition story timestamps with novelty/relevance scores; WRDS Intraday Indicators retail-trading measures (Boehmer et al. 2021 algorithm); S&P Global Securities Finance lendable-share balances (Barardehi et al. 2025 method); WRDS Short Volume; I/B/E/S analyst counts; 13F-based institutional ownership; Baker-Wurgler sentiment index; VIX.
- **Point-in-time / availability:** `News` stories are timestamped and after-hours stories roll to the next trading day (usable); `Earn` is defined by the maximum-volume day inside a +/- 1-day window around the announcement date, which is only knowable after that day's volume is observed - a genuine same-day look-ahead in the event definition for any within-day rule. `ANUM` requires a one-year message history with the most recent month skipped, and the robustness variant IA1 column (7) requires at least 30 non-missing daily message observations in the preceding year.
- **Coverage selection:** Appendix Table A1 states that observations with missing message counts are excluded from `ANUM`, and the regression sample fluctuates from 3,358,601 to 3,910,418 NObs across Tables 2, 3 and 9, while Internet Appendix Table IA1 column (6) - which assigns zero to missing `NUMhigh` instead of dropping - reports **8,776,939** NObs. The baseline sample is therefore conditioned on StockTwits coverage, which the paper describes as growing rapidly during the sample, especially in 2020-2021.
- **Missing data:** imputation is forbidden except for the explicitly labelled IA1 column (6) zero-fill and the ADSVI zero-fill described in footnote 19; no other imputation is stated.
- **Cost fields:** none. There is no commission, slippage, spread, borrow-cost, funding, fee or impact data requirement anywhere in the paper (see Execution assumptions).

## Execution assumptions

Cost treatment was determined at Methods level by reading Section 2.1-2.3, Section 3.1-3.3 (including Eq. 1), Section 4.1-4.2, Section 5.1-5.4, Appendix Table A1, Tables 1-10 captions and Internet Appendix Tables IA1-IA2, plus a whole-document term census on the pinned 116,235-character extraction:

- `transaction cost` 0, `transaction costs` 0, `commission` 0, `slippage` 0, `bid-ask`/`bid ask` 0, `market impact` 0, `latency` 0, `execution` 0, `fill` 0, `taker` 0, `limit order` 0, `market order` 0, `funding` 0, `borrow` 0, `short sale` 0, `leverage` 0, `capacity` 0, `participation` 1 (the participation-puzzle literature reference), `friction` 0, `trading cost` 0, `rebalance` 0, `walk-forward`/`walk forward` 0, `holdout` 0, `deflated` 0, `benjamini` 0, `fdr` 0, `multiple test` 0, `p-value` 0, `sharpe` 0, `bootstrap` 0, `newey`/`hac` 0.
- The four `cost` hits are non-trading: "low-cost, user-generated" content (page 3), "higher arbitrage costs" citing Pontiff 2006 (page 19), "higher costs of acquiring firm-specific information" (page 19), plus the reference list. The single `spread` hit is "the spread between the top and bottom NET stocks" (page 15). The five `turnover` hits are all the regression control variable (stock trading volume / shares outstanding). The two `placebo` hits are the long-leg placebo test in Section 4.2. The two `margin` hits are "above-median" sentiment splits. The `liquidity` hits are the Amihud illiquidity sorter. `net return` hits are all `NET returns` (the anomaly spread), never a net-of-cost figure.
- Consequently **every reported return in this paper is gross of all trading costs, spreads, borrow fees and market impact; gross-versus-net status itself is `not stated in source`**. Order type, fill model, signal-to-order delay, execution price convention, shorting and locate availability, borrow fees, dividend treatment on the short leg, position limits, margin, latency, partial fills, participation and capacity all stay `data gap` and must never be read as zero.
- Execution timing that the source does state: daily returns are CRSP close-to-close; portfolio formation is end-of-month with equal-weighted portfolios over the following month; `News` stories released after trading hours are assigned to the following trading day; `Earn` uses the highest-volume day in a 3-day window.
- Institutional/lending measures in Section 4.1 explicitly adjust for the pre/post September 5, 2017 settlement-cycle change (T+3 to T+2) - a settlement adjustment inside a diagnostic measure, not a trading-cost model.

## Evidence

### Source-reported

All third-party claims below are source-reported, all come from the single pinned SSRN PDF, and none has been independently reproduced.

**Sample and descriptive statistics**

- Table 1 (page 46), 3,906,742 firm-day observations: columns are `NUMhigh` No/Yes. `NUMhigh = 1` on 975,246 stock-days (**24.96%**); non-`NUMhigh` 2,931,496 (**75.04%**). `News = 1` on 656,524 stock-days (**16.80%**) of which 253,341 (**6.48%** of the full sample) are also `NUMhigh`; `Earn = 1` on 104,911 stock-days (**2.69%**) of which 62,519 (**1.60%**) are also `NUMhigh`. Cross-checks against the Section 2.3 prose: 253,341/656,524 = 38.6% ("almost 40% of news days"), 62,519/104,911 = 59.6% ("60% of EA days"), 721,905/975,246 = 74.0% ("about 75% of high-attention days occur without any news release"), 912,727/975,246 = 93.6% ("more than 90% occur without an earnings announcement").
- Table 2 (page 47), linear probability model on `NUMhigh`: `Earn` +0.270 (t 57.23), `News` +0.130 (t 74.89), `Ret2` +0.569 (t 2.97), `Dvol` +0.294 (t 78.54), `52HighDum` +0.125 (t 54.94), `52LowDum` +0.139 (t 28.38); Adj. R2 0.029/0.041/0.007/0.062, NObs 3,906,742 / 3,358,601 / 3,577,604 / 3,091,956 for columns (1)-(4). Standard errors clustered by firm and day.

**Headline conditional-spread results**

- Figure 1 (page 44) values, quoted from the Section 3.1 prose because the figure itself is an image: daily High-Low NET equal-weighted return of about **0.10%** on all days, about **0.18%** on news days, about **0.05%** on high-attention days, "almost **0.30%**" on high-attention news days (described as "about 1.5 times" the all-information-day value), and **-0.05%** on high-attention non-news days. The same prose converts 0.10% x 20 trading days into "around 2% per month", consistent with Engelberg et al. (2026).
- Table 3 (page 48), daily return in bps, NObs 3,902,416, Adj. R2 0.156 in all four columns, SEs clustered by time and firm. Column (1): `NET` 0.149 (t 3.47), `NET x NUMhigh` **-0.240** (t -5.01), `NET x Earn` 1.492 (t 6.69), `NET x News` 0.126 (t 2.50), `NUMhigh` 22.870 (t 27.32), `News` 9.417 (t 12.41), `Earn` -11.712 (t -3.63). Column (2) adds `NET x NUMhigh x News` **0.390** (t 3.06) with `NET x NUMhigh` **-0.324** (t -6.92) and `NET x News` -0.005 (t -0.10). Column (3) adds `NET x NUMhigh x Earn` **0.980** (t 2.56) with `NET x NUMhigh` -0.269 (t -5.70), `NET x Earn` 0.887 (t 3.93), `NET x News` 0.123 (t 2.44), `NET` 0.156 (t 3.64). Column (4) carries both triples: `NET x NUMhigh x News` 0.304 (t 2.40), `NET x NUMhigh x Earn` 0.799 (t 2.04), `NET x NUMhigh` -0.327 (t -6.98), `NET` 0.170 (t 3.93).
- Section 3.2 economic illustration (column (3), verbatim logic): for `NET = 10` (stated as about 0.71 standard deviations), 1.6 bps on days with no EA and no high attention; -2.7 bps incremental on high-attention days without EAs, giving a total of -1.1 bps; on high-attention EA days, +9.8 bps on top of the standalone EA effect of 8.9 bps, giving 17.6 bps total. The source states that earnings news with high attention has about twice the positive effect of earnings news alone, and that other corporate news is significantly positive only on high-attention days.
- Figure 2 (page 45) event-time pattern, quoted from Section 3.2 prose (image figure): on high-attention non-news days the anomaly return is lower at t+0, significantly higher at t+1 (a partial reversal), and back to average by t+2 and t+3; on high-attention news days the return is higher at t+0 and back to average from t+1 onward.

**Heterogeneity and mechanism**

- Table 4 (pages 49-50), extreme-tercile splits with `Inf` replacing `Earn`/`News`. Panel A: `NET x NUMhigh x Inf` 0.829 (t 3.58) high RetailOwn vs 0.362 (t 1.78) low RetailOwn; 0.907 (t 3.94) high RetailTrading vs -0.108 (t -0.55) low; `NET x NUMhigh` -0.569 (t -6.78) vs -0.131 (t -2.12), and -0.297 (t -3.59) vs -0.128 (t -2.61) - the prose "more than 4 (2) times stronger" reproduces as 4.34x and 2.32x. Panel B: triple 1.081 (t 3.84) small vs -0.148 (t -1.07) large; 0.777 (t 2.79) high illiquidity vs -0.139 (t -0.90) low; `NET x NUMhigh` -0.683 (t -8.51) small vs -0.026 (t -0.46) large, -0.670 (t -8.29) illiquid vs -0.114 (t -1.60) liquid. Panel C: triple 0.821 (t 3.38) low news coverage vs 0.136 (t 0.74) high; 0.697 (t 2.70) low analyst coverage vs 0.102 (t 0.62) high. **Both effects are reported only in small, illiquid, retail-heavy, thinly-covered names.**
- Table 5 (page 51), leg split, NObs 3,902,416 for returns: `Long NET x NUMhigh` -2.710 (t -2.36), `Short NET x NUMhigh` +7.846 (t 4.65), `Long NET x NUMhigh x Inf` +9.429 (t 2.50), `Short NET x NUMhigh x Inf` -13.872 (t -2.92), `Long NET` 3.552 (t 4.19), `Short NET` -3.058 (t -2.87). Retail order imbalance mirrors the signs (`RetailOIMB`: long -0.287, short +0.275 on non-info high-attention days); institutional imbalance is negative in long-leg stocks (-0.292, t -2.66) and short volume is negative in short-leg stocks (-0.354, t -8.18), which the source reads as sophisticated investors stepping away.
- Table 6 (page 52), one-day lags: `Short NET x Lag(NUMhigh)` **-3.721** (t -2.35) against the +7.846 contemporaneous coefficient in Table 5, which the source interprets as "about half" reversing; `Long NET x Lag(NUMhigh)` 1.851 (t 1.53); the news-day lagged sums are 1.141 (long) and -0.427 (short), i.e. no reversal after high-attention news days.
- Table 7 (page 53): Panel A, Low NET quintile has 3.122 high-attention days per month vs 2.066 in High NET (High-Low -1.055, t -16.03) and 1.242 more bullish days (t -10.34). Panel B, within the Low NET quintile sorted on monthly bullish-day count: monthly raw returns 0.108 / 0.708 / 3.042 percent for Low/Mid/High, High-Low **2.935% (t 5.40)** and High-Low FF6 alpha **2.688% (t 4.79)**. Panel C: `BullRank x NUMhigh` 14.943 (t 3.73) in the Low NET portfolio, -1.028 (t -0.16) in the High NET portfolio (placebo), with `BullRank x NUMhigh x Inf` -21.965 (t -1.61); the prose "3.4 times as large" reproduces as 14.943/4.359 = 3.43.

**Robustness**

- Table 8 (page 54): with contemporaneous `Ret2` interactions, `Dvol` interactions, or `Monday` interactions, `NET x NUMhigh` ranges **-0.151 to -0.308** and `NET x NUMhigh x Inf` ranges **0.308 to 0.612**, all significant at 1%; NObs 3,902,416 / 3,902,415 / 3,902,416.
- Table 9 (page 55), alternative attention definitions (`ANUM > 0`, message volume above its trailing 10-day median, any message that day): `NET x ATThigh` -0.253 (t -6.93), -0.197 (t -5.14), -0.106 (t -3.17); triple 0.370 (t 3.73), 0.266 (t 2.74), 0.153 (t 1.70).
- Table 10 (page 56): adding Seeking Alpha abnormal attention leaves `NET x NUMhigh` at -0.257 (t -5.43) and the triple at 0.353 (t 3.00); `ASEEK` alone is positive (0.158, t 1.95) and insignificant once interacted with `Inf`. Google `ADSVI` gives `NET x ADSVI` -0.324 (t -3.21) with an insignificant triple (-0.028), and `NUMhigh` stays at -0.306 (t -6.62) with triple 0.548 (t 4.34).
- Internet Appendix Table IA1 (page 57), seven robustness columns: `NET x NUMhigh` from -0.263 to -0.350 (all t between -5.78 and -7.28) and triples from 0.327 to 0.549 (t between 2.48 and 4.42), including event-day fixed effects, excluding the bottom size decile or the most illiquid decile, dropping days where fewer than 5% of observations are high-attention, the missing-value zero-fill (NObs 8,776,939), and the >=30-message-history requirement.
- Internet Appendix Table IA2 (page 58): `NET x NUMhigh` -0.278 (t -3.92) high-VIX vs -0.339 (t -6.02) low-VIX; triples 0.849 (t 4.17) vs 0.261 (t 1.55); sentiment split -0.323 / -0.302 with triples 0.627 / 0.409.

### Independently reproduced

not independently reproduced.

Arithmetic-only consistency checks were run against the pinned PDF text (exit 0, no external data, no backtest): the four Table 1 shares and conditional percentages above; the Section 3.2 illustration 0.156 x 10 = 1.56, -0.269 x 10 = -2.69, 0.980 x 10 = 9.80, 0.887 x 10 = 8.87 and -1.1 + 9.8 + 8.9 = 17.6; the Table 6 news-day lagged sums 1.851 + 1.222 - 1.932 = 1.141 and -3.721 - 1.290 + 4.584 = -0.427; the Table 6 / Table 5 reversal ratio 3.721/7.846 = 47.4%; the Table 4 ratios 0.569/0.131 = 4.34 and 0.297/0.128 = 2.32; the Table 7 Panel C ratio 14.943/4.359 = 3.43; the Table 8 printed ranges; and the Table 5 standalone leg difference 3.552 - (-3.058) = 6.61 bps/day against Figure 1's prose "about 0.10%" (different conditioning - indicator legs versus the continuous NET quintile spread - so the two are not required to match and are recorded as such). No coefficient was re-estimated, no data was re-downloaded, and no portfolio was re-run.

### Negative evidence

1. **No cost model of any kind** (census above): every printed number is gross of commissions, spreads, slippage, borrow fees and impact, and gross-versus-net status is not stated.
2. **The effect lives where trading is hardest.** Table 4 reports both the negative non-news effect and the positive news effect as insignificant for large and for liquid stocks (Panel B: -0.026, t -0.46 and -0.114, t -1.60) and for high news/analyst coverage names (Panel C triples 0.136 and 0.102, both t < 1.0), which is exactly where shorting costs, spreads and price impact concentrate.
3. **The short leg carries the load.** Table 5 shows the non-news-day non-information effect is +7.846 bps in short-leg stocks versus -2.710 bps in long-leg stocks, so more than two thirds of the conditional spread comes from shorting retail-favoured small names.
4. **Partial next-day reversal.** Table 6: about half of the short-leg non-news effect reverses the next day (-3.721 versus +7.846), and Figure 2 Panel A shows a positive t+1 reversal - a same-day or one-day holding rule must survive paying for that reversal.
5. **Same-day conditioning, ex-post event labelling.** `Earn` is defined by the highest-volume day in a 3-day window and `NUMhigh` by same-day message counts, so both states are not knowable at the open; a tradable version must re-derive them from information available before the return window, and the source does not test that.
6. **Coverage-selected sample.** Observations with missing StockTwits counts are excluded (Appendix Table A1), yet IA1 column (6) shows the universe roughly doubles to 8,776,939 when those days are added back - the baseline is estimated on a StockTwits-covered subsample whose coverage the paper says grew rapidly, especially in 2020-2021.
7. **No out-of-sample discipline whatsoever**: `walk-forward` 0, `holdout` 0, `placebo` 2 (both meaning the long-leg regression placebo, not a randomization test), no train/test split, no frozen forward window, and no evidence after 2021-12-31.
8. **No multiple-testing control**: `benjamini` 0, `fdr` 0, `deflated` 0, `p-value` 0, `bootstrap` 0 - with at least 40 interaction coefficients reported across Tables 3, 4, 5, 6, 7, 8, 9, 10, IA1 and IA2 at star-based significance only (double-clustered standard errors are the one clear methodological strength).
9. **No risk-adjusted performance at all**: `sharpe` 0; no volatility, drawdown, turnover-implied cost, capacity or alpha-versus-flat-NET improvement statistic is printed, so the incremental value of conditioning over simply holding the NET spread is not quantified in risk-adjusted terms.
10. **Attention correlates with same-day returns positively at the stock level** (`NUMhigh` 22.870 bps, t 27.32 in Table 3 column (1)), a confound the source acknowledges in footnote 9; conditioning the spread requires netting this level effect out.
11. **Control-choice sensitivity**: `NET x NUMhigh` moves from -0.240 to -0.151 when abnormal dollar volume interactions are added (Table 8 column (2)), i.e. the largest single attenuation in the robustness set comes from controlling for abnormal trading volume, an attention proxy.
12. **Attention-define sensitivity**: Table 9 column (3) (any message that day) gives only -0.106 (t -3.17) with a triple of 0.153 (t 1.70), materially weaker than the main quartile measure.
13. **Fresh, unrefereed working paper** posted 2026-09-29 with no citation record, no replication, no code and no data-availability statement.
14. **Concentrated in one regime window**: 2010-2021 US equities only, with the paper itself noting StockTwits usage grew sharply in 2020-2021 and that the news-day attention effect is concentrated in high-VIX periods (Table IA2).

## Falsification plan

Every threshold below is `research-defined falsification threshold`; every operational rule below is `research-proposed`. Action on failure for every gate is: **do not adopt, record the failure in the record, and do not retune the frozen specification.**

- **F1 - Data-access gate (hard prerequisite).** Obtain CRSP, Compustat, RavenPack Dow Jones Edition, WRDS Intraday Indicators and Short Volume, S&P Global Securities Finance, I/B/E/S, plus the public Cookson-Niessner StockTwits release and the public Chen-Zimmermann anomaly files. Fail if any required input cannot be licensed or retrieved for 2010-2021; on failure, stop - no proxy substitution without an explicit, separately labelled proxy record.
- **F2 - Printed-value reproduction.** Re-estimate Eq. (1) and reproduce Table 3 columns (1)-(4) within **0.05 bps** for `NET`, `NET x NUMhigh`, `NET x Earn` and `NET x News`, and within **0.10 bps** for the triples, with the sign of every t-statistic matching; also reproduce Table 1 cell counts exactly. Fail if any tolerance is breached.
- **F3 - Point-in-time reconstruction gate.** Rebuild `NUMhigh` using only message counts observable by a declared decision timestamp (source-reported threshold does not exist; we declare **messages up to the prior close** as the primary and **messages up to 09:30 ET** as a secondary), and rebuild `Earn` from the announcement date only (no same-day volume maximum) and `News` from story timestamps. Fail if the `NET x NUMhigh` coefficient attenuates by more than **50%** relative to the reproduced value or loses its sign.
- **F4 - Cost ladder.** Apply 0 / 1 / 2 / 5 / 10 / 20 bps one-way plus a half-spread term to any conditional long-short implementation. Fail if the conditional- versus unconditional-NET improvement is non-positive at **5 bps one-way**, or if the traded conditional spread itself is non-positive at **10 bps**.
- **F5 - Borrow and shortability gate.** Re-run the short leg restricted to names with an active borrow locator and reported borrow cost; require at least **70%** of short-leg dollar notional locatable and fail if Sharpe of the conditional improvement degrades by more than **0.30** versus the unrestricted version.
- **F6 - Heterogeneity replication gate.** The source's own subsample pattern must reproduce: negative `NET x NUMhigh` significant at 5% in small and in illiquid terciles and insignificant in the large and liquid terciles. Fail if the large/liquid subsample becomes the significant one, because that would mean the effect is not where the mechanism says it is.
- **F7 - Holding-period / reversal gate.** Because Table 6 shows ~47% next-day reversal, evaluate decision horizons of same-day, t+1 exit and t+3 exit. Fail if the t+1-exit version is non-positive after costs at 5 bps, since that is the earliest honest holding period given same-day conditioning.
- **F8 - Placebo gate.** Redraw `NUMhigh` days 1,000 times preserving each stock's 25% high-attention frequency and the day-of-week distribution; fail if the observed `NET x NUMhigh` is not more extreme than the **95th percentile** of the placebo distribution, or if a placebo attention measure built from shuffled message counts reproduces the effect within 20% of its size.
- **F9 - Multiplicity gate.** Apply Benjamini-Hochberg at `q < 0.10` across the full family of interaction coefficients inspected (Tables 3, 4, 5, 6, 7, 8, 9, 10, IA1, IA2 - **>= 40 tests**) plus a deflated Sharpe whose trial count equals the number of attention definitions and subsample splits examined. Fail if the headline non-news interaction does not survive at `q < 0.10`.
- **F10 - Frozen forward window.** Freeze `ANUM` construction, the quartile cut, the 209/200+ anomaly set, the NET score, the `Inf` definition, the quintile scheme and the regression form, then evaluate **2022-01-01 to 2026-06-30** with no retuning. Fail if the `NET x NUMhigh` coefficient is non-negative, or significant at 5% in the wrong direction, or if the conditional-minus-unconditional spread is non-positive after 5 bps costs.
- **F11 - Subperiod split.** Require the non-news interaction to be negative with `|t| >= 2` in **both** 2010-2015 and 2016-2021. Fail if either window is positive.
- **F12 - Execution-realism gate.** Move fills to the next session open with a half-spread charged each way. Fail if the conditional improvement degrades by more than **0.30** Sharpe versus close-to-close accounting.
- **F13 - Capacity gate.** Cap participation at **20% of 20-day median dollar volume** and report degradation. Fail if Sharpe of the conditional improvement falls below 0.50 of the uncapped value at that cap.
- **F14 - Benchmark-completeness gate.** Compare against (a) the flat unconditional NET long-short and (b) a flat NET spread restricted to the small/illiquid tercile where the source says the effect lives. Fail if conditioning adds less than **+0.10** net Sharpe over (b) at 5 bps - i.e. if the attention/news split adds nothing beyond picking the right tercile.
- **F15 - Cross-market replication (crypto portability).** Rebuild the same attention x news conditioning on a crypto cross-section using a public retail-attention feed and timestamped firm/token news. Fail if the sign of the conditional spread difference disagrees with the equity result in at least 2 of 3 tested markets/venues.
- **No-retuning rule:** `ANUM`'s one-year-minus-one-month window, the top-quartile cut, the `Earn` and `News` definitions with the novelty/relevance >= 100 filter, the quintile scheme, the control set, the decision timestamp and the cost ladder are frozen once F2 passes; any later change creates a new pre-registered variant rather than an edit.

## Crypto portability

**adapted (performance unproven).**

- The mechanism - retail attention amplifying biased beliefs when no information arrives, and accelerating information incorporation when information arrives - is instrument-agnostic, so the conditioning idea ports in principle.
- The empirical basis is US equity cash-market data over 2010-2021 only; the pinned text contains **zero** occurrences of `crypto`, `bitcoin`, `perpetual` or `funding`, so there is no crypto evidence in the source.
- Porting obstacles, all `data gap` in the source: no StockTwits equivalent with comparable retail coverage per token; token-level "news" definitions with novelty/relevance filters must be invented (`research-proposed`); 24/7 sessions remove the day-boundary that the whole news/non-news classification depends on; anomaly characteristics themselves (Chen-Zimmermann) do not exist for crypto; funding, mark/index price, liquidation, borrow on the short leg and venue fragmentation are all unaddressed; exchange-level delisting is worse than equity delisting and the paper has no survivorship handling to transport.
- Therefore: hypothesis portable, performance unproven, and crypto is not authorized by this record.

## Limitations

- `underspecified`: the exact anomaly count (209 before or after dropping the three discrete variables); the monthly-versus-daily NET quintile convention (Section 3.1 monthly formation versus Appendix Table A1 daily sorting); the reconciliation of Table 3 column semantics when only one triple is present; whether `NUMhigh`'s 24.96% realized share is exactly the designed top quartile after the sample screen.
- `not stated in source`: publication/peer-review status, gross-versus-net status, all execution and cost fields, delisting/survivorship handling, code or data availability, any risk-adjusted metric.
- `data gap`: transaction costs, slippage, spread, borrow, short availability, capacity, latency, fill model, position limits, multiple-testing control, out-of-sample testing, evidence after 2021-12-31, non-US markets.
- Two minor documentation inconsistencies were found and are recorded rather than repaired: (i) the Table 3 caption attributes the anomaly characteristics to "Chen and Zimmermann (2020)" while Section 2.2, Section 3 and the reference list all cite Chen and Zimmermann (2022), *Critical Finance Review* 27, 207-264; (ii) Section 2.2 states "209 in total" while footnote 5 removes three discrete variables without saying whether 209 is pre- or post-exclusion, and the abstract/conclusion only say "more than 200". Neither changes a reported coefficient, so `contested` stays `false`.
- The conditioning evidence is contemporaneous and therefore is not by itself a tradeable strategy: the source demonstrates a same-day interaction in returns, not a forecast. Any implementable version depends on operational choices the source never makes (decision timestamp, holding period, sizing, cost model), all of which are labelled `research-proposed`.
- The mechanism tests (Tables 5-7) are consistent with the dual-role story but do not uniquely identify it: partial reversal also fits a price-pressure story, and the source concedes biased beliefs and price pressure are not competing explanations in noise-trader models.
- No ablation exists for the "news" versus "earnings" split beyond columns (2)-(4) of Table 3, and no comparison is made against other retail-attention-conditioned anomaly studies on an equal footing beyond the Seeking Alpha and Google columns of Table 10.
- Standard errors are double-clustered by firm and day (a genuine strength) but no HAC/block correction for overlapping monthly formation windows is reported.
- The record is a normalized capture of one fresh SSRN working paper; it is not a replication, not a backtest and not evidence that the conditional spread is tradable.

## Implementation status

`not-implemented`. No implementation exists in our research stack: no data was licensed or downloaded, no coefficient was re-estimated, no portfolio was constructed, no backtest was run, and no signal was wired into any runtime. Nothing in this record implies Qlib full-backtest validation or any Paper, Testnet or Live verification.

## Adoption boundary

`research-only` / `not-approved` / `approval_scope: research-only`. The presence of this record does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; or approved for live trading.

## Related Wiki records

Adjacent pages verified by `kb_search` on 2026-09-30 (only pages actually returned by the search are linked; the queries `social media attention anomalies investor attention` and `retail attention stocktwits news day returns` both returned zero pages, so no page was fabricated):

- [[quant/cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02]]
- [[quant/attention-factors-statistical-arbitrage-residual-portfolios-2026-09-02]]
- [[quant/crypto-24h-displayed-change-rollout-attention-anomaly-2026-09-07]]
- [[quant/put-call-parity-implied-borrow-dividend-confounding-falsification-2026-09-13]]

## Sources

1. Arseny Gorbenko and Hang Wang, *A Tale of Two Days: Social Media Attention and Anomalies on News and Non-News Days*, SSRN working paper, draft September 2026, DOI `10.2139/ssrn.7535899`. Landing page read 2026-09-30: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7535899 (SSRN metadata on that page: `citation_online_date 2026/09/29`, `citation_publication_date 2026/09/28`, authors `Gorbenko, Arseny` and `Wang, Hang`).
2. Same work, pinned full text actually read for this record: https://papers.ssrn.com/sol3/Delivery.cfm/7535899.pdf?abstractid=7535899&mirid=1&download=yes - **58 pages, 808,338 bytes, SHA-256 `0b8c61426b0be46d4d5250279bbf3644c2e48ddfd836bcac1ac3ce3c9c902c27`**, retrieved and parsed 2026-09-30; all sample, cost-treatment, regression and table claims in this record come from this file with the section/table anchors given above.
3. SSRN DOI record: https://doi.org/10.2139/ssrn.7535899
