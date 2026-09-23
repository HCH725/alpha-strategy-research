---
schema: strategy-research-record-v1
title: "Earnings-Call Speaker-Identity Weighted Sentiment: FinBERT Section-Weighted Long-Short on S&P 500 Post-Earnings Returns"
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-04-14
sources:
  - https://arxiv.org/abs/2604.13260
  - https://arxiv.org/pdf/2604.13260v1
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Earnings-Call Speaker-Identity Weighted Sentiment: FinBERT Section-Weighted Long-Short on S&P 500 Post-Earnings Returns

## Provenance

- **Primary source (only source used for every number below):** arXiv `2604.13260`, Karmanpartap Singh Sidhu, Junyi Fan, Maryam Pishgar, *Which Voices Move Markets? Speaker Identity and the Cross-Section of Post-Earnings Returns*, Viterbi School of Engineering, University of Southern California (emails on title page: kssidhu@usc.edu, junyifan@usc.edu, pishgar@usc.edu).
- **Landing / version:** `https://arxiv.org/abs/2604.13260`, **arXiv v1, submitted 14 Apr 2026** (API `published = updated = 2026-04-14T19:48:48Z`, i.e. **single version, no v2**), primary category `q-fin.TR`; arXiv comment field = `22 tables, 2 figures, 16 references`; arXiv API returns **no `journal_ref` and no publisher DOI** → publication status is **preprint only / `not stated in source`**. DOI `10.48550/arXiv.2604.13260` resolves HTTP 200 to the arXiv abs page (checked 2026-09-23); it is the arXiv auto-DOI, not a journal DOI.
- **Primary-source checksum (performed 2026-09-23):** PDF `https://arxiv.org/pdf/2604.13260v1`, **11 pages, 972,017 bytes, SHA-256 `e8b5e5f6bc6132ec7a113f0fba0436f40a6c120151db9598d2f1623b85812960`**, extracted with `pypdf 6.16.2` and **read in full end-to-end** (Introduction → Conclusion + all 22 tables + 2 figures + 16 references). Every field below is either quoted from that text with a table/section anchor or explicitly marked as a gap.
- **Author list exactly as source:** exactly the three authors above; no fourth author appears on the title page or in the arXiv API metadata.
- **Sample period — the source is internally inconsistent; recorded verbatim, not reconciled:** Abstract says `16,428 ... transcripts (2015–2025)`; §I says `April 2015 to December 2025`; §III.A says `April 2015 to December 2025 ... 16,428 earnings call events ... 447 unique firms`; **Table I Panel A says `Sample period April 2015 – January 2025`, `Total transcripts 16,537`, with footnote `The sample ends with earnings calls reported through Q4 2024`**; Table III caption says `16,109 earnings call–return observations ... April 2015 to December 2024`; §IV.E.5 says training `April 2015 to December 2022 (11,138 call observations)` and test `January 2023 onward (4,971 observations)`; Table V caption says training `11,179 earnings call observations prior to January 1, 2023`; **Table VII says train `N = 11,297`, test `N = 5,131 (January 2023 – December 2024)`**; §VII limitation says test period `2023–2025`. Counts and end-date therefore disagree across abstract, tables and text → **`data gap` / internal inconsistency, recorded as printed**.
- **Universe:** S&P 500 constituents with available transcripts, **447 unique tickers, ≈400 firms per quarter, large-cap U.S. equities** (§III.A; Table II annual coverage 387–445 tickers per year, `variation across years is due to index reconstitution and data availability`). **No explicit point-in-time index-membership rule, no liquidity/size/exclusion filter, no delisting/survivorship treatment stated** → `data gap` / `underspecified`.
- **Data vendors named by the source:** earnings-call transcripts (with speaker name + title) from the **Alpha Vantage API**; call timestamps (BMO/AMC) from **Yahoo Finance**; daily prices/returns from **Yahoo Finance**; Fama–French five factors + risk-free rate from **Kenneth French's data library** (daily factor returns compounded to monthly); quarterly actual/estimate EPS for SUE from **Alpha Vantage**; Loughran–McDonald dictionary from the **University of Notre Dame** repository (§III.A–D).
- **Transaction-cost treatment (Methods, §IV statistical framework, §V–§VI read in full; keyword scan of the extracted full text):** **no bid-ask, spread, commission, slippage, borrow, short-sale, market-impact, turnover, participation or capacity parameter appears anywhere in the paper** → recorded as **`not stated in source` (`data gap`)**, **not** inferred as zero. The source itself states the limitation in §VII: `implementation of the long–short strategy would face transaction costs and capacity constraints that we do not model.`
- **Source/data as-of:** source as-of = arXiv v1, 2026-04-14; data as-of = the source's own (inconsistent) sample end, latest internally consistent reading being **December 2024** per Tables III and VII; no data beyond 2025 is verifiable.
- **Dedup (performed before writing):** repository-wide search across all 908 tracked `*.md` (516 distinct arXiv IDs, 1,485 DOIs, 216 GitHub repos, 174 TradingView URLs indexed) for `2604.13260`, `Which Voices Move Markets`, `speaker identity`, `Sidhu`, `Pishgar`, `section-weighted`, `analyst sentiment`, `Q&A sentiment`, `speaker-role` → **0 hits**; filename absent; Wiki Brain `kb_search "earnings call sentiment post-earnings announcement drift"` returned only unrelated records (linked below). New source identity and materially distinct mechanism (speaker-role weighting of call sentiment) ⇒ not a duplicate.

## Economic mechanism

### Source-reported

The authors claim that post-earnings returns are not equally affected by all voices in a call: analyst questions in Q&A are `spontaneous, based on knowledgeable judgment, and difficult for management to anticipate`, while `planned management remarks are scripted and strategically constructed` (§II.D, Hypothesis 1); therefore an aggregation weighted by each speaker category's empirical predictive power beats an equal-weighted transcript sentiment (Hypothesis 1), the weighted signal earns FF5 abnormal returns (Hypothesis 2), it is orthogonal to standardized unexpected earnings (Hypothesis 3), and FinBERT subsumes the Loughran–McDonald dictionary (Hypothesis 4). The economic story the authors advance is **mispricing from sluggish assimilation of soft information** (managerial confidence, hedging, evasion, analyst skepticism), supported by their claim that both legs of the long–short contribute (§V.E, Table XV) and by CAR fan-divergence over 30 days (§VI.B).

### Research interpretation

Falsifiable mechanism: **speaker-role is an information-quality dimension of disclosure text**; sell-side analyst tone is a less managed, more forward-looking proxy for the informed part of the call, so a cross-section of stocks sorted on analyst-heavy FinBERT sentiment underreacts for roughly one to two weeks (source's own IC-decay half-life, §VI.A) and can be harvested as a long–short, i.e. a text-based variant of post-earnings-announcement drift (PEAD) with differential weighting by speaker credibility.

Component roles (structure preserved; ablation required before assuming each contributes):

```text
Measurement: sentence-level FinBERT net sentiment, operator sentences and <10-char sentences removed (§IV.A)
Weighting / primary signal: IC-derived speaker-category weights from the training window, frozen for OOS (Method M4, Eq. 8–10)
Simpler rival signal inside the same source: analyst-only sentiment (Method M5, Eq. 11) — source-reported as the strongest variant
Control: SUE (expanding-window standardized EPS surprise, winsorized 1/99, Eq. 1–2)
Portfolio: monthly equal-weighted sentiment quintiles, long Q5 / short Q1 (§IV.E.3)
Risk / exit: none specified by the source (no stop, no sizing rule, no cost model)
```

**Scout observation, not source-reported (our critique):** the source's AMC event window is `close day t−1 → close day t+1` (§III.C), which starts **before** the after-market call takes place, so one trading day of the measured "post-earnings" return accrues **before the signal exists**; the BMO window (`close t−1 → close t`) has the same look-back start but the call precedes that session. This is our reading of the stated formula, flagged for falsification below (Test F1), not a claim the source makes about itself.

## Signal

**Source-reported (reconstruction-relevant):**

- **Formation timestamp:** sentence scoring on the transcript of the call; call timed as BMO or AMC via Yahoo Finance timestamps (§III.A). **Publication/availability lag of the Alpha Vantage transcript itself is never stated** → `underspecified` (can the scored signal be produced before the return window opens? not verifiable from the source).
- **Lookback:** one call (quarterly event); sentence-level scoring with NLTK sentence tokenizer, sentences `<10 characters` dropped, operator sentences dropped (§IV.A); no multi-call lookback window is specified.
- **Sentiment transforms:** `S_i = P(positive)_i − P(negative)_i ∈ [−1,1]` (Eq. 3); confidence `c_i = 1 − P(neutral)_i` (Eq. 4).
- **Speaker classes (§III.B):** Analyst (title/affiliation contains a sell-side firm name), CFO (`CFO`, `Chief Financial Officer`, `Treasurer`), Executive (`CEO`, `Chief Executive`, `President`, `Chairman`, `COO`, `CTO`, `Managing Director`), Other.
- **Five aggregations (§IV.B):** M1 simple mean (Eq. 5); M2 confidence-weighted mean (Eq. 6); M3 extreme fractions with `τ > 0.5` minus `τ < −0.5` (Eq. 7); **M4 section-weighted** = per-category mean (Eq. 8) then `w_g = IC_g / Σ_{g′: IC_g′>0} IC_g′` if `IC_g > 0` else `0` (Eq. 9), renormalized over categories present in that call (Eq. 10); M5 analyst-only mean (Eq. 11).
- **Frozen weights (Table V, training sample pre-2023):** Analyst train IC `0.128*** (p 3.03e−42, N 11,179) → 48.8%`; CFO `0.078*** (5.44e−16, N 10,835) → 29.5%`; Executive `0.042*** (1.13e−05, N 10,963) → 15.9%`; Other `0.015 (p 3.35e−01, N 4,029) → 5.8%`. Abstract/conclusion round these to `49% / 30% / 16% / 5%`.
- **Return windows (§III.C):** 1-day = `close t−1 → close t+1` (AMC) or `close t−1 → close t` (BMO); 5-day = to `t+5` (AMC) / `t+4` (BMO).
- **IC (§IV.E.1):** monthly Spearman rank correlation between call sentiment and 1-day return, months with `≥20` call observations only; Newey–West HAC `L = min{3, ⌊0.75·M^{1/3}⌋}`.
- **Portfolio (§IV.E.3):** `sort stocks each month into quintiles by sentiment`, **equal-weighted**; long Q5 (most positive), short Q1 (most negative); monthly portfolio excess returns regressed on the five FF factors (Eq. 15).
- **Fama–MacBeth (§IV.E.2):** monthly cross-sectional regressions, all regressors cross-sectionally standardized within month, Newey–West t (Eq. 13–14).
- **Out-of-sample design (§IV.E.5):** train **Apr 2015 – Dec 2022**, test **Jan 2023 onward**, M4 weights derived only from training ICs and applied unmodified.
- **Stated horizon behaviour (§VI.A):** IC `0.119` at 1 day → `0.099` at 5d → `0.065` at 10d → `0.032` at 21d; source states a half-life of `about 6–7 trading days`.

**Not specified by the source → `underspecified`:** entry/exit order type and exact fill session; what happens to a stock with **no call in a given rebalance month** (signal refreshed, carried forward, or dropped); treatment of overlapping event windows within a month; tie handling; position sizing beyond equal weight; borrow availability and cost on the Q1 short leg; call-level staleness; transcript-availability lag; point-in-time S&P 500 membership; handling of calls with a missing speaker category (only Eq. 10's renormalization is given).

**`research-proposed` (our operationalization, not in the source):** act at the next session **close** after the scored transcript is available (BMO → same-day close if scoring finishes before the bell, otherwise next session close); **maximum holding period 21 trading days** (anchored to the source's §VI.A IC decay, which reports near-zero IC at 21d), monthly quintile re-sort with a **trailing-92-day freshness filter** (drop signals from calls older than one quarter); **ADV-participation cap 10%** per name per day; insufficient depth → park that leg in cash for the month; cost grid **κ ∈ {10, 20, 30, 50} bps** per side applied to both legs.

## Required data

- Instrument/universe: **U.S. S&P 500 large-cap equities** (spot, listed); no crypto, no derivatives.
- Venue/data: Alpha Vantage earnings-call transcripts incl. speaker name/title and call date; Yahoo Finance call timestamps (BMO/AMC) and daily OHLC/close returns; Kenneth French FF5 + risk-free daily factor series (compounded monthly); Alpha Vantage quarterly EPS actual + estimate for SUE; Loughran–McDonald positive/negative word lists.
- Fields: per-sentence FinBERT `P(positive)/P(negative)/P(neutral)` (model checkpoint and version **not stated by the source** → `data gap`), speaker category, call timestamp, daily returns, SUE, FF5 factors.
- Point-in-time: requires transcript availability no later than the start of the measured return window; the source never documents transcript publication delay or backfill → `underspecified`. SUE uses an **expanding-window** firm-level standard deviation requiring `≥4` prior observations and 1/99 winsorization (Eq. 1–2) — this part is explicitly point-in-time.
- Timestamp/timezone: U.S. exchange sessions; BMO/AMC classification from Yahoo Finance; **timezone/precision of the call timestamp not stated** → `data gap`.
- Missing data: source excludes calls with missing price data and unmatched timestamps (§III.A) but gives no imputation rule for missing sentences/speakers; **no imputation should be added by us** (spec forbids silent imputation).

## Execution assumptions

- **Source-reported:** **none material.** The source models portfolio formation and factor regressions only. No order type, no fill model, no signal-to-order delay, no fees, no spread, no slippage, no borrow/shorting availability, no leverage, no latency, no partial-fill handling, no capacity limit — and §VII explicitly concedes `transaction costs and capacity constraints that we do not model`. Recorded as **`not stated in source` / `data gap`, not as zero cost.**
- **`research-proposed` (ours, must be re-declared in any test):** market orders at the next available close; equal weight within each quintile; next-close and +1-session-delay variants both reported; κ ∈ {10,20,30,50} bps/side plus a separate borrow-basis sensitivity of {25, 50, 100} bps/yr on the short leg; 10% ADV participation cap; no leverage; partial fills truncated to the cap; failure → that name skipped, leg weight redistributed among remaining names that month (if fewer than 20 names remain tradable on either side, the month is declared non-tradable).

## Evidence

### Source-reported

All figures below are third-party claims from arXiv `2604.13260v1`, **gross of any transaction cost** (no cost model exists in the source), and have **not** been independently reproduced.

- **Full-sample ICs (Table VI, N = 16,428, IC vs 1-day return):** M1 `0.0813 (tNW 5.49, p 4.10e−08)`; M2 `0.0986 (6.36)`; M3 `0.0749 (5.36)`; **M4 `0.1188 (9.11, p 8.05e−20)`**; **M5 analyst-only `0.1405 (11.71, p 1.16e−31)`**; 5-day IC column: `0.0673 / 0.0804 / 0.0620 / 0.0988 / 0.1171`. Abstract claims M4 is a `46% improvement` over M1.
- **Out-of-sample ICs (Table VII; train Apr 2015–Dec 2022 `N=11,297`, test Jan 2023–Dec 2024 `N=5,131`, weights frozen):** M4 train `0.1141` → test `0.1442`; M5 `0.1273` → `0.1707`; M1 `0.0806` → `0.0966`; source's `Decay` column: M4 `−26.4%`, M5 `−34.1%`, M1 `−19.9%` (source defines decay as (Train−Test)/|Train|, negative = strengthening out-of-sample). **Fig. 1:** in-sample mean monthly IC `0.099`, OOS mean `0.115`, positive in `85% of months`.
- **Quintile spreads, event-window 1-day returns, full sample (Table VIII):** M4 `Q1 −0.96 / Q2 −0.18 / Q3 0.46 / Q4 0.60 / Q5 1.30`, **`Q5−Q1 = 2.26% (t 13.33)`**; M5 `Q1 −1.22 … Q5 1.63`, **`2.85% (t 16.35)`**; M1 `1.60% (t 9.89)`. **OOS (Table IX, N = 5,131):** M4 `Q1 −1.77 / Q5 1.38`, **`3.14% (t 9.07)`**; M5 `3.76% (t 10.58)`; M1 `2.13% (t 6.28)`. **M4 detail (Table X):** Q1 mean ret `−0.962%` (t −8.21, std 6.716), Q3 `0.458` (3.79), Q5 `1.301` (10.59, std 7.042), spread `2.263 (t 13.33)`.
- **Hard-numbers control (Table XI):** SUE IC `0.2458 (tNW 17.58, N 16,109)` vs M4 `0.1184 (8.95)` and M5 `0.1409 (11.94)`.
- **Fama–MacBeth with SUE (Table XII, 110 months):** M4 univariate `0.00679 (t 7.16)`; **M4 + SUE `0.00505 (t 5.57)`**; SUE `0.01425 (14.17)` → `0.01342 (13.43)`; M5-only model `0.00809 (6.94)`.
- **Double sort inside SUE terciles (Table XIII):** Low SUE `Q5−Q1 = 2.227% (t 7.27)`, Mid `1.613 (5.67)`, High `1.145 (4.06)`, all `***`; N = 5,370/5,369/5,370.
- **FF5 alpha, monthly long–short (Table XIV Panel A):** **M4 `α = 2.026%/mo (tNW 6.49)`, annualized `24.31%`**; M5 `2.542% (8.69)`, annualized `30.51%`; M4 factor loadings `Mkt–RF 0.1223*, SMB −0.1816*, HML 0.2002*, RMW −0.1077, CMA −0.1953`; `R² = 0.079` (M4) / `0.034` (M5); `N months = 100 / 99`.
- **Alpha by quintile (Table XV):** Q1 `−0.939% (t −3.34)`, Q2 `0.040 (0.21)`, Q3 `0.106 (0.49)`, Q4 `0.479 (3.36)`, Q5 `1.086 (7.76)`, **Q5−Q1 `2.026% (t 6.49, p 8.36e−11)`**.
- **Sub-periods (Table XVI):** pre-COVID 2015–19 `2.227%/mo (t 11.70, 39 mo)`; **COVID 2020–21 `−0.505% (t −0.68, p 0.499, 21 mo)`**; post-COVID 2022+ `2.865% (t 10.35, 40 mo)`; train pre-2023 `1.560% (t 4.48, 71 mo)`; **test 2023+ `2.770% (t 8.56, 29 mo)`**.
- **FinBERT vs LM (Tables XVII–XIX):** full-sample IC M4 `0.1188 (FB t 15.33)` vs LM `0.0745 (t 9.58)`; M5 `0.1405 (18.10)` vs LM `0.0619 (7.91)`; OOS train→test M4 FB `0.1141 → 0.1442`, LM `0.0586 → 0.1077`; quintile spreads M4 `2.263%` (FB) vs `1.355%` (LM), M5 `2.847%` vs `1.029%`.
- **Fama–MacBeth horse race (Table XX, 112 months):** section-weighted joint spec FB `0.00660 (t 5.90)` vs LM `0.00073 (t 0.86)`; analyst-only joint FB `0.00986 (t 7.65)` vs LM `−0.00109 (t −1.37)` → source claims FinBERT subsumes LM.
- **XGBoost/SHAP validation (Table XXI):** SHAP share Analyst `59.6%`, CFO `29.1%`, Executive `8.5%`, Other `2.8%`; model IC in-sample `0.1723 (std 0.0613)` vs OOS `0.1711 (std 0.0686)` — source reports this as corroboration of the speaker hierarchy.
- **Horizon decay (§VI.A):** IC `0.119 → 0.099 (5d) → 0.065 (10d) → 0.032 (21d)`, stated half-life `6–7 trading days`. **CAR (§VI.B, approximate as printed, no table):** over 30 trading days Q5 ≈ `+1.5%`, Q1 ≈ `−1.5%`, total ≈ `3.0%`, divergence starting on day 0. **Industry controls (§VI.C):** M4 coefficient `remains significant` with GICS sector fixed effects — **exact coefficient/t not reported → `data gap`**.

### Independently reproduced

not independently reproduced

### Negative evidence

**In-source (verified in the same primary source, recorded as printed):**

1. **The headline weighting machinery is dominated by its own simpler rival.** Analyst-only M5 beats section-weighted M4 on every reported metric: IC `0.1405` vs `0.1188` (Table VI), OOS IC `0.1707` vs `0.1442` (Table VII), event spread `2.85%` vs `2.26%` (Table VIII), OOS spread `3.76%` vs `3.14%` (Table IX), FF5 alpha `2.542%` vs `2.026%` (Table XIV). The source acknowledges M5 has `the highest IC` (§V.A) but still leads with M4's alpha — i.e. **speaker weighting itself is not shown to add anything over analyst-only sentiment**.
2. **COVID sub-period failure:** 2020–2021 alpha is `−0.505%/mo (t −0.68, p 0.499)` (Table XVI) — a two-year regime with no effect, source-reported.
3. **Only the tails carry alpha:** Q2 `0.040 (p 0.831)` and Q3 `0.106 (p 0.625)` are indistinguishable from zero (Table XV); the monotonicity claim holds for the extreme quintiles, not the middle.
4. **Hard numbers dominate soft text:** SUE's IC `0.2458` is roughly double M4's `0.1184` (Table XI); the sentiment signal is incremental, not primary.
5. **Internal sample/period/count inconsistencies** (see Provenance): 16,428 vs 16,537 vs 16,109 observations; 11,138 vs 11,179 vs 11,297 training N; 4,971 vs 5,131 test N; end date April-window `January 2025` vs `Q4 2024` vs `December 2025`.
6. **Statistic mismatch for identical numbers:** Table VI gives M4 `IC 0.1188, tNW 9.11` and M5 `0.1405, tNW 11.71`, while Table XVII reports the **same** ICs with `t = 15.33` and `t = 18.10`; the abstract's OOS `0.142 / 0.115` also does not equal Table VII's `0.1442 / 0.1141`. Two different t-statistic conventions/objects are reported without reconciliation → recorded verbatim.
7. **Costs and capacity explicitly unmodeled** (§VII quote in Provenance); no turnover figure is given anywhere, so the net-of-cost viability of a monthly-rebalanced large-cap long–short cannot be assessed from the source → `data gap`.
8. **A weight is derived from an insignificant IC:** `Other` gets `5.8%` weight from `IC 0.015, p = 0.335` (Table V), contrary to the stated `if IC_g > 0` positivity rule being the only filter.
9. **Stated test window is short** (source's own §VII limitation): OOS alpha rests on `29 months` (Table XVI) / `5,131` events through Dec 2024.
10. **Scout observation (not source-reported):** the AMC event window `close t−1 → close t+1` (§III.C) includes one pre-signal trading day inside the "post-earnings" return (see Economic mechanism → Research interpretation).

**External:**

- `none identified in the reviewed sources; absence is not evidence of no negative result`. This run opened and verified only the primary source above; no external replication or failure study of *this specific speaker-weighted claim* was located.
- Adjacent leads found by search this run and **recorded as leads only, not as evidence** (not opened/verified beyond the abstract noted): (a) Molinaro, *Do earnings call transcripts predict post-announcement returns?*, SSRN `6695758` (written 2026-04-30, Russell 1000, walk-forward ML — direction of result not verified); (b) Meursault, Liang, Routledge & Scanlon, *PEAD.txt*, Philadelphia Fed WP 21-07/R rev. 2022 (snippet claims text-based PEAD exceeds classic PEAD and classic PEAD is near zero in recent years — **snippet-level only, not read**); (c) arXiv `2609.11144` (abstract read 2026-09-23): across five sentiment instruments on securities-class-action X messages (2002–2025), `benchmark agreement therefore establishes semantic validity but does not by itself determine predictive rankings` — a methodological caution on a **different corpus**, not a replication of this paper.

## Falsification plan

Every threshold below is `research-defined` (Scout-chosen), every operational rule not quoted from the source is `research-proposed`. Data: the source's own inputs (Alpha Vantage transcripts, Yahoo prices, French factors), Apr 2015 – Dec 2024, S&P 500, train/test split frozen at Jan 2023 exactly as §IV.E.5.

- **F1 — event-window contamination (`research-defined`):** recompute all 1-day/5-day returns with AMC = `close t → close t+1` and BMO = `close t → close` on t (no pre-signal day). **Failure rule:** if the M4 1-day IC falls below `0.06` (half the source's full-sample `0.1188`) or the FF5 alpha loses significance (`|t| < 2`), the original headline is treated as window-contaminated and the hypothesis is weakened. Action: record as refuted-in-original-form.
- **F2 — speaker-weighting ablation (`research-defined`):** M4 vs M5 head-to-head on identical samples (IC, FF5 alpha, net spread). **Failure rule:** M4 fails to beat M5 by `≥0.01` IC or `≥0.25pp/month` alpha in both train and test ⇒ the *speaker-weighting* mechanism (H1 as stated) is falsified even if analyst sentiment survives; record M5 as the surviving, simpler signal.
- **F3 — speaker-label placebo (`research-defined`):** 500 shuffles of speaker-category labels within each call, rebuilding M4 each time. **Failure rule:** observed M4 IC must exceed the 95th percentile of the shuffled distribution (empirical `p < 0.05`); otherwise speaker identity is not the operative channel.
- **F4 — cost / turnover stress (`research-defined` thresholds on a `research-proposed` cost grid):** apply κ ∈ {10, 20, 30, 50} bps/side + short-leg borrow {25, 50, 100} bps/yr, with 10% ADV participation caps and +1-session delay. **Failure rule:** net FF5 alpha at **κ = 20 bps** must remain `> 0` with `|t| ≥ 2` in the test period, else the effect is classified **gross-only / economically untradable**.
- **F5 — regime split (`research-defined`):** report 2015–19 / 2020–21 / 2022+ and train/test separately. **Failure rule:** any sub-period with `α < 0` or `|t| < 2` (the source already fails 2020–2021) ⇒ the record is downgraded to `regime-limited`; two consecutive failed sub-periods in a re-run ⇒ reject for adoption review.
- **F6 — staleness / tradability audit (`research-defined`):** verify transcript availability timestamps exist **before** the first tradable session of the return window for ≥ `95%` of calls. **Failure rule:** below 95% ⇒ signal declared non-point-in-time and rejected regardless of alpha.
- **F7 — hard-numbers baseline (`research-defined`):** SUE-only and SUE+M4 double sorts must keep a positive, significant sentiment spread in **all three** SUE terciles (`|t| ≥ 2`, Table XIII analogue). **Failure rule:** spread insignificant in ≥1 tercile ⇒ sentiment is not orthogonal to earnings surprise as claimed.
- **F8 — dictionary horse race (`research-defined`):** joint FM regression FB + LM must reproduce the source's direction (FB significant at `p < 0.01`, LM insignificant). **Failure rule:** LM significant (`|t| ≥ 2`) in the joint spec ⇒ the subsumption claim (H4) fails.
- **F9 — no retuning rescue (`research-defined`):** weights frozen at the training window; **no parameter may be re-estimated on the test period**; if F1–F8 fail, the correct action is `record negative result`, not re-optimize weights, horizons or quintile counts.

## Crypto portability

**unproven.**

- The source contains **zero crypto evidence** (S&P 500 equities only) and its mechanism depends on a U.S. corporate disclosure institution: scheduled quarterly calls, sell-side analysts with coverage incentives, SEC-reporting cadence, and an Alpha Vantage-style transcript feed with speaker titles.
- Crypto has no equivalent recurring multi-speaker disclosure event with a standardized speaker taxonomy: closest analogues are project AMAs, core-dev calls, and founder threads — unstructured, unmoderated, and without a sell-side analyst role, so the `Analyst 48.8% / CFO 29.5% / Executive 15.9%` hierarchy has no direct mapping.
- Even the adapted version would need: 24/7 session and candle boundaries (no BMO/AMC split), venue fragmentation of the underlying spot/perps, transcript availability timing on-chain/off-chain, liquidity far below S&P 500 large caps (the 10% ADV cap and 20–50 bps grid would bind harder), and exchange/venue delisting survivorship.
- `research-proposed` porting direction only: score project-update calls/AMAs with a role taxonomy (core dev / foundation exec / outside contributor / community) on a single large-cap perpetual (e.g. BTC/ETH) and re-run F1–F4; nothing beyond hypothesis generation is implied.

## Limitations

- `not independently reproduced` — every performance figure is source-reported and gross of costs.
- `data gap`: transaction costs, spread, slippage, borrow, turnover, capacity, fill model — absent from the source (its own §VII concession).
- `data gap`: transcript publication/availability lag; FinBERT model checkpoint/version; timezone of call timestamps; exact GICS-fixed-effect coefficient (§VI.C has no number); no table anchors for the §VI.B CAR figures (printed as approximations).
- `underspecified`: staleness handling for stocks without a call in a rebalance month, overlapping-event handling, index reconstitution / point-in-time S&P 500 membership, sizing, tie rules, missing-category behavior beyond Eq. 10.
- `underspecified` / internal inconsistency: sample end date and N counts disagree across abstract, Table I, Table III, §IV.E.5, Table V and Table VII (see Provenance); two different t-statistic conventions appear for identical ICs (Table VI vs Table XVII); abstract OOS IC `0.142` ≠ Table VII `0.1442`.
- Source-reported regime failure 2020–2021 (Table XVI) and source-reported limitation of a `29-month` test window and large-cap-only universe (§VII).
- Publication-bias / source-quality: single-version arXiv preprint, **no peer review evidenced** (no journal_ref, no publisher DOI), three authors from one engineering school (not an asset-pricing department); confidence is therefore `medium` for the *research interpretation* only, and says nothing about profitability.
- Scout-side risk: our `research-proposed` execution rules (entry session, 21-day hold, freshness filter, cost grid) are not the source's and must be re-declared in any test; F1's event-window critique is our reading of §III.C, not the source's admission.

## Implementation status

`implementation_status: not-implemented`. No scoring pipeline, transcript ingestion, portfolio construction, backtest, Qlib run, paper, testnet or live component has been built from this record. Nothing in our research stack has been executed against this hypothesis. This record is a normalized research capture only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this file does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered `/results/_handoff/candidates.json`; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. Those are separate, gated, downstream decisions made outside the Scout workflow.

## Related Wiki records

Verified by `kb_search` this run (no link is fabricated):

- [[quant/strategy-research-record-spec-v1]] — canonical record contract read for this run.
- [[quant/earnings-announcement-premium-jump-risk-decay-falsification-2026-09-13]] — adjacent event-window / PEAD-falsification record; different source and mechanism (jump-risk compensation vs speaker-weighted text).
- [[quant/news-event-tag-drift-rumor-resolution-placebo-adjusted-momentum-2026-09-02]] — adjacent disclosure-text drift record with placebo methodology worth reusing for F3.
- [[quant/finsmart-market-aligned-reinforcement-learning-sentiment-alpha-2026-09-02]] — adjacent sentiment-alpha record; different model and construction.

## Sources

- Sidhu, K. S., Fan, J., & Pishgar, M. (2026). *Which Voices Move Markets? Speaker Identity and the Cross-Section of Post-Earnings Returns*. arXiv:2604.13260v1 [q-fin.TR], submitted 14 Apr 2026. https://arxiv.org/abs/2604.13260 (preprint; arXiv API reports no journal reference and no publisher DOI).
- Direct PDF used for all quoted figures: https://arxiv.org/pdf/2604.13260v1 (11 pages, SHA-256 `e8b5e5f6bc6132ec7a113f0fba0436f40a6c120151db9598d2f1623b85812960`, read in full 2026-09-23).
- Auto-DOI (resolves to the arXiv abs page, HTTP 200 on 2026-09-23): https://doi.org/10.48550/arXiv.2604.13260
- Named data dependencies cited by the source (not separate evidence for the results): Alpha Vantage API (transcripts, EPS), Yahoo Finance (call timestamps, prices), Kenneth French data library (FF5 + risk-free), Loughran–McDonald dictionary (Notre Dame repository).
- External search leads recorded in Negative evidence but **not** used for any number: SSRN 6695758; Philadelphia Fed WP 21-07/R; arXiv 2609.11144 (abstract only).
