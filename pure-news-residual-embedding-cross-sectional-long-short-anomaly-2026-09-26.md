---
schema: strategy-research-record-v1
title: "Pure News (Residual LLM Embedding) Monthly Cross-Sectional Long-Short Anomaly in U.S. Equities (NBER Working Paper 35093, \"The Inefficient Pricing of News\")"
created: 2026-09-26
updated: 2026-09-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: "NBER Working Paper 35093, April 2026, Revised May 2026; pinned PDF retrieved 2026-09-26 CST"
sources:
  - https://www.nber.org/papers/w35093
  - https://doi.org/10.3386/w35093
  - https://www.nber.org/system/files/working_papers/w35093/w35093.pdf
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6540399
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Pure News (Residual LLM Embedding) Monthly Cross-Sectional Long-Short Anomaly in U.S. Equities

## Provenance

### Pinned primary source

- **Paper:** "The Inefficient Pricing of News".
- **Author list (exactly as printed on the pinned PDF cover page):** Antoine Didisheim (University of Melbourne, Faculty of Business and Economics, Department of Finance); Bryan T. Kelly (Yale University and NBER); Mohammad Pourmohammadi (Yale University and Swiss Finance Institute); Hanqing Tian (University of Melbourne). No fifth author and no "et al." construct appears on the cover; the NBER copyright line repeats the same four names.
- **Version / date:** NBER Working Paper No. 35093, "April 2026, Revised May 2026" (cover page). DOI `10.3386/w35093`. JEL codes C45, C58, G02, G1, G11, G12, G14, G17, G40, G41.
- **Publication / preprint status:** NBER working paper only. The PDF carries the standard NBER statement that working papers are circulated for discussion and "have not been peer-reviewed or have been subject to the review by the NBER Board of Directors". No journal reference, no publisher DOI beyond the NBER DOI, and no peer-review claim was found on the pinned PDF or on the NBER landing page (checked 2026-09-26) → **preprint / not peer reviewed**.
- **Licence note (as printed):** © 2026 by the four authors, all rights reserved; short sections not exceeding two paragraphs may be quoted with credit. This record therefore paraphrases and normalizes; it does not reproduce source prose.
- **Author disclosure (as printed):** Bryan Kelly reports consulting income from AQR Capital Management exceeding $10,000 over the past three years, and notes AQR may use similar investment techniques; views are the authors' own. Preserved here as a source-quality caveat (an author is affiliated with a large systematic manager that could trade related signals).
- **Pinned artifact:** `https://www.nber.org/system/files/working_papers/w35093/w35093.pdf` — retrieved **2026-09-26 (CST)** with HTTP 200, `application/pdf`, **8,518,296 bytes**, **SHA-256 `6b1db3f173cbd720e6cf02c5e40befedd147510968485d8b62587c25158626a8`**. Text layer extracted to **158,250 characters / 4,355 lines / 76 page breaks** and read line by line: cover, abstract, Section 1 (Introduction), Section 2 (Data), Section 3 (Predicting News with Stock Characteristics), Sections 4.1–4.7 (MSRR, performance, anomaly universe, size split, persistence/turnover/net-of-cost, mean-variance accounting, time-series innovations), Sections 6.1–6.4 and 6.6–6.7 (lookahead and other robustness, subsamples, training windows), Section 7 (Conclusions), Table 1, Table 2, Table 3, Table 4, Table 7, and the note text of Figures 1–14, 19, 20, 22, 24, 25. The References list, the Internet Appendix and the topic-label appendices were sampled only by heading; no empirical number was taken from them.
- **Companion version:** SSRN `abstract_id=6540399`, same four authors, 75 pages, posted 8 Apr 2026, last revised 20 May 2026 (SSRN landing page checked 2026-09-26). Cross-version wording differs — the pinned NBER version calls the residual signal **"pure news"**, the SSRN abstract calls it **"news shocks"** (wording difference only; **no number in this record comes from SSRN**).
- **Secondary sources:** a third-party blog surfaced the headline figure during discovery. **No performance number in this record is taken from any secondary source**; every figure below is traced to a section, table or figure of the pinned NBER PDF.

### Deduplication (performed before writing, 2026-09-26)

Repo-wide, hidden-inclusive content search across all `*.md` (top level plus `.mimo-worktrees/`, `.agents/`, `.hermes/`) **and** `coverage_manifest.csv`, plus a `git log --oneline -20` glance. Exact source-identity patterns searched: `10.3386/w35093`, `ssrn.6540399` / `abstract_id=6540399`, `Inefficient Pricing of News`, `Didisheim`, `Pourmohammadi`, `Hanqing Tian`, `pure news`, `E5-Mistral`, `ChronoGPT`, `news shock anomaly` → **0 hits for every pattern before this file was written**, with only the new record matching afterwards. The single case-insensitive near hit on the phrase "inefficient pricing" is `kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13.md`, which uses the phrase generically and does not cite this paper; `coverage_manifest.csv` returned 0 hits for all identity patterns.

### Four-axis distinction from the nearest existing records

- `mfast-market-friction-aware-llm-news-sentiment-quintile-2026-09-22.md` — **different source** (Kirtac's MFAST framework), **different signal construction** (sentiment scores → quintile portfolios evaluated under execution frictions) versus 4,096-dimensional residual embeddings aggregated by maximum-Sharpe regression; **different mechanism claim** (deployment feasibility under frictions versus residualizing news against characteristics to isolate unpriced content).
- `supply-chain-network-augmented-llm-text-embeddings-nale-2026-09-04.md` — same broad "LLM text → cross-section" family but **different source**, **different material data dependency** (annual 10-K MD&A text plus a supply-chain graph, yearly horizon) versus licensed real-time Reuters news aggregated to stock-months, and **different signal construction** (network-propagated embedding factor versus within-month characteristic residualization).
- `benzinga-daily-headline-sentiment-cross-sectional-rank-ic-null-2026-09-24.md` — **different source** (Benzinga headlines) and **different signal** (news-sentiment rank-IC null result), used below as related negative evidence rather than as the same claim.
- `published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23.md` — **different source and opposite role**: a post-2005 anomaly-decay audit cited below under Negative evidence.

Source identity, signal construction and material data dependency differ in each case; no reframed duplicate is being created.

## Economic mechanism

### Source-reported

- The authors' stated chain (all anchored to the pinned PDF, Sections 1, 3, 5 and 7): stock-month news text is substantially **predictable from prevailing stock characteristics** (pooled adjusted R² ≈ 7.7% for the 132 JKP characteristics, ≈ 10.2% when 25 GICS industry indicators are added on top of JKP — Section 3 / Figure 2). Because that predictable content is already in prices, the informative part of news is the residual, which the authors name **"pure news"**.
- The residual signal is claimed to be priced with a delay: investors are said to **underreact to negative-tone news and to quantitatively intense news**, and to **overreact to linguistically ambiguous and to high-attention news** (Sections 1, 5.4, 7). A topic-level decomposition attributes the anomaly to 12 interpretable themes ("Earnings & Financial Results", "Corporate Guidance & Outlook", "Analyst Ratings & Sentiment", "Distress, Bankruptcy & Delisting", "Momentum & Trading Activity", "Corporate Actions & Restructuring", "Leadership & Governance", "Growth & Demand Trends", "Biotech, Pharma & Healthcare", "Regulatory & Legal Actions", "Sector-Specific Signals", "Product Launches & Operations"), with **underreaction topics accounting for 62.1% of the news-anomaly portfolio weight** (Section 1 summary of Section 5).
- The authors describe the resulting long-short as an anomaly "of singular magnitude", larger in magnitude and longevity than every anomaly in the Jensen–Kelly–Pedersen (2022) universe (Sections 1, 4.3, 7). This is the source's claim, not our finding.

### Research interpretation

- **Hypothesized mechanism (falsifiable form):** licensed, high-frequency firm-specific news text carries event-driven, idiosyncratic information that is not yet impounded in price; cross-sectionally removing the component of the text embedding that is linearly predictable from prevailing characteristics isolates that information, so a market-neutral long-short portfolio built on the residual earns positive risk-adjusted returns that decay over roughly 12–18 months.
- **Friction / participant behaviour assumed:** limits to attention and limits to arbitrage — slow digestion of dense or negative information (underreaction) and extrapolation of salient/ambiguous information (overreaction), in a cross-section where shorting is feasible and borrow is available.
- **Component roles (this is a two-stage signal, not an indicator stack):**
  - *Data layer:* licensed real-time news → per-article LLM embedding → stock-month average embedding, Z-scored with expanding (recursive) moments.
  - *Purge layer (the actual economic claim):* within-month cross-sectional regression of the embedding on stock characteristics; the residual is the tradable signal.
  - *Portfolio layer:* maximum-Sharpe-ratio regression (MSRR) maps the 4,096 residual coordinates to a single dollar-neutral monthly long-short book.
  - The source itself does not claim every layer contributes alpha; the raw-embedding portfolio (no purge) and the "predictable news" component are reported as materially weaker (Section 4.2), which is exactly the ablation a replication should test.
- **Non-claim:** mechanism is asserted for U.S. equities over 1996–2022 only. The source contains **no crypto evidence of any kind**.

## Signal

All items below are **source-reported unless explicitly marked** `research-proposed` or `data gap`.

- **Formation timestamp / availability:** every article arriving within calendar month *t* is used (conservatively) only at month-end *t* (Section 2). Articles are matched to stocks by exact timestamps; the analysis is monthly. Timezone, exchange-session convention and the exact minute of formation are **not stated in source** → `data gap`.
- **Lookback / embedding construction:**
  - Article embedding = equal-weighted average of token embeddings from **E5-Mistral-7B** (Wang et al., 2024), **D = 4,096** coordinates (Section 2).
  - Stock-month embedding `E_{i,t}` = equal-weighted average of that stock's article embeddings within month *t*; stocks with no article in the month are assigned a missing value (Section 2) — **how missing stock-months enter the MSRR design matrix is not stated** → `underspecified`.
  - Anisotropy correction: per-coordinate Z-score in month *t* using a pooled mean and standard deviation estimated from all stock-months through *t − 1* (expanding, explicitly to avoid lookahead; Section 2 and footnote 6).
- **Purge (the core transformation):** each month run the cross-sectional regression `E_t = S_t β_t + ε_t` (Equation 1), where `S_t` contains a constant plus **132 JKP characteristics** (rank-standardized each month, missing values imputed with the cross-sectional mean rank; Section 2), optionally augmented with 25 GICS industry indicators. The residual `ε_{i,t}` is "pure news". Because the regression is cross-sectional within month *t*, no estimation look-ahead is introduced by this step (source-stated design). Characteristic-purge variants used as robustness: constant only, CAPM (beta), FF3, FF6, full JKP (Figure 4 Panel A).
- **Portfolio rule:** MSRR (Kelly and Xiu, 2023): weights `w_{i,t} = x'_{i,t} b` with `x = ε_{i,t}` (or `E_{i,t}` for the raw variant); `b` is estimated **recursively with an expanding window through *t***, with an **initial 24-month training window**, and the ridge penalty λ selected by leave-one-out cross-validation inside each training sample (Section 4.1). Out-of-sample portfolio return is `F*_{ϵ, t+1} = ε'_t R_{t+1}`.
- **Entry / long / short:** source specifies a **dollar-neutral long-short** (the constant-purged and fully purged embeddings are cross-sectionally de-meaned, so the resulting book is dollar neutral — Section 4.2). No per-name weight cap, no position limit, no rank cutoff and no entry threshold beyond the MSRR weights are stated → `underspecified`.
- **Exit / holding period / re-entry:** holding period is **one month**, rebalanced monthly (the signal is the stock-month embedding; factor return is realized over *t+1*). Delayed-signal variants reuse `ε'_{t−τ} R_{t+1}` for τ = 1…36 months (Section 4.5). No stop, take-profit or time-based exit exists → risk management is not part of this strategy.
- **Smoothing variant (source-reported):** averaging article embeddings over the most recent *j* = 1…24 months; gross Sharpe stays near 3.0 for lookbacks up to 6 months and is 2.4 at 24 months; the source states the **net-of-cost optimum is the 6-month average** (Section 4.5, Figure 12).
- **Alternative, simpler construction (source-reported):** MSE approach — first regress next-month excess returns on the residual embeddings in an expanding window (λ by leave-one-out CV), then sort every month into quintiles on the predicted return and take **long top 20% / short bottom 20%**, either equal-weighted or capped value-weighted (Section 6.4, Table 7).
- **Parameters source-specified:** D = 4,096; 132 JKP characteristics; 25 GICS industry groups; 24-month initial training; expanding estimation; monthly rebalance; τ ∈ {1…36} delay grid; k ∈ {5,10,…,100} purge-size grid with 100 random draws per k; j ∈ {1…24} smoothing grid. All are **source-reported**, not Scout-chosen.
- **Execution price / order timing:** the source states the signal is known at month-end and applies to *t+1* returns, but **never states at which price or session the trade is executed** → `underspecified`. A concrete rule (`research-proposed`, for falsification only): rebalance at the next session's open after month-end, or at month-end close, tested both ways.
- **Overall:** reconstructible in *form*, but not byte-for-byte — the exact handling of missing stock-months, the execution price, and the universe/borrow screen are not specified. Treat as **partially underspecified**.

## Required data

- **Instrument / market type:** U.S. listed common stocks (cash equities). No futures, options, or perpetuals appear anywhere in the source.
- **Universe:** U.S. stocks January 1996 – December 2022; coverage filters follow Didisheim et al. (2024) to keep the 132 JKP characteristics with the highest coverage. Average cross-section **4,198 stocks per month**; on average **52.5%** of stocks have ≥ 1 article in a month; conditional on coverage, **8.7 articles per stock-month** (Section 2 / Table 2). Largest size decile: 81.5% covered, 19.7 articles; smallest decile: 30.0% covered, 4.6 articles. Size-group tests use JKP "mega"/"large" (above the NYSE 50th size percentile) versus "small"/"micro" (1st–50th percentile) (Section 4.4).
- **Venue / data vendor:** Thomson Reuters Real-time News Feed ("Reuters"), filtered to single-stock-tagged articles, 100–100,000 characters, near-duplicates removed, third-party (3PTY) content excluded from the main specification; **6,680,550 articles survive all filters** (Table 1) ≈ "6.7 million" (Section 2). Robustness source: Dow Jones Newswires 1996–2021 (5,378,838 articles) and Reuters 3PTY news (2,265,171 articles, 1996–2022) (Section 6.3).
- **Price/return and characteristics data:** monthly excess returns and the JKP characteristic library (Jensen–Kelly–Pedersen open-source asset pricing), 132 characteristics rank-standardized monthly (Gu et al., 2020 convention), missing values imputed with the cross-sectional mean rank (an explicit imputation choice made by the source), plus 25 GICS industry groups (Section 2).
- **Text/model dependency:** E5-Mistral-7B open-weight model, run privately on the authors' own hardware **because the Reuters feed is licensed** (Section 2 and footnote 5). Chronologically-consistent LLM variant: ChronoGPT (GPT-2, 1.5B) from He et al. (2025); improved-training variant from Kelly et al. (2026) (Section 6.1).
- **Point-in-time requirements:** Z-score moments recursive through *t − 1* (footnote 6); purge regression is within-month cross-sectional; MSRR weights expanding through *t* with a 24-month warm-up; all articles in a month are held back to month-end. These are source-stated anti-lookahead controls.
- **Timestamps / timezone:** article-to-stock linkage uses "precise timestamps"; **timezone, session boundary and out-of-order handling are not stated** → `data gap`.
- **Missing data:** no-news months are coded missing (treatment inside the portfolio estimator unstated → `underspecified`); characteristic missing values are imputed with the cross-sectional mean rank (source-stated).
- **Funding / fee / spread fields:** **none**. The source has no funding, borrow, commission, spread or slippage dataset (see Execution assumptions).
- **Access barrier:** the Reuters Real-time News Feed is a licensed commercial feed (the authors' own footnote explains computations were kept private "per our licensing agreement"). **No public data release, no code repository, and no data-availability or code-availability statement was found in the pinned PDF** → replication requires either an expensive licence or a substitute news corpus (`data gap`).

## Execution assumptions

Cost/execution fields below come from a Methods-level read of Sections 2, 4.1, 4.5 and 6.3–6.4 of the pinned PDF (not from the abstract or any summary), plus a word scan of the full extracted text.

- **Signal-to-order timing:** signal known at month-end *t*; portfolio return defined over *t+1*. **Order price, order type (market/limit), fill model and session are not stated** → `underspecified`; `research-proposed` alternatives are next-open versus month-end-close fills.
- **Fees / spread / slippage / impact / capacity / latency / partial fills:** the only cost object anywhere in the pinned text is a **flat 10 basis points per dollar traded**, applied *ex post* in Figures 11 and 12 Panel B, "following Frazzini et al. (2018)". A full-text word scan returns **zero** occurrences of slippage, bid-ask, commission, market impact, capacity, limit order, market order or fill. Every headline number (Sharpe 3.1, the alphas, the cumulative-return curve) is therefore **gross of cost**; only Figure 11/12 Panel B are net-of-cost, and those panels are figures whose exact net values are **not printed in the text** → `data gap` for precise net Sharpe values.
- **Turnover:** one-sided turnover defined as half the absolute change in drifted positions scaled by lagged gross exposure (Equation 8); the news portfolio's turnover is reported as **75%**, above the highest-turnover JKP factor (short-term reversal, 67%) (Section 4.5 / Figure 11 Panel A). Source-reported.
- **Leverage / margin:** main performance figures are (ex post) standardized to **10% annual volatility** for interpretability (Figure 4 note, Table 4 note); the mean-variance decomposition fixes gross exposure `Σ|w| = 1` (Section 4.6). **No margin, financing or leverage-cost model** → `data gap`.
- **Shorting / borrow:** the strategy is a dollar-neutral long-short including a short leg across thousands of names; **borrow availability, stock-loan fees and recall risk are never discussed** → `data gap`.
- **Funding:** not applicable to cash equities in the source; no funding field exists.
- **Capacity:** not modeled; no ADV, participation or dollar-capacity constraint anywhere → `data gap`.
- **Failures / partial fills:** not addressed → `data gap`.

## Evidence

### Source-reported

All numbers below are **source-reported**, from the pinned NBER Working Paper 35093 PDF (April 2026, Revised May 2026), U.S. equities, monthly, January 1996 – December 2022. **None has been independently reproduced.** Gross unless stated.

- **Headline performance:** long-short on residual ("pure") news embeddings has an **annualized Sharpe ratio of 3.1** over 1996–2022 (Section 1; Section 4.2; Figure 4 Panel A), versus the **largest Sharpe in the JKP anomaly universe of 1.4** over the same period (Section 1; Section 4.3 / Figure 6; footnote 9 identifies it as the cash-based operating profits-to-book-assets factor `cop_at` of Ball et al., 2016).
- **Purge ladder (Section 4.2 / Figure 4 Panel A):** raw-embedding portfolio Sharpe **1.1** (not dollar neutral) → cross-sectionally de-meaned (constant purge) **1.7** → gradually rising with CAPM, FF3, FF6 purges → **3.1** with the full JKP purge. So most of the headline comes from *hedging out* existing-anomaly exposure, not from a higher mean: Section 4.6 / Figure 13 Panel A reports the portfolio mean falling from **5.3% to 4.8%** while volatility is cut by **70%** (the reporting frequency/units of that mean are not labelled in the extracted figure text → `data gap`), and the effective rank of the news-factor covariance matrix rising from **15 to 130** (Figure 13 Panel B).
- **Risk-adjusted level:** with no delay, the strategy earns **about 30% per year on 10% volatility, essentially all of it CAPM alpha** (Section 4.5, discussion of Figure 10).
- **Alpha versus anomaly themes (Table 4; portfolios standardized to 10% annual volatility, annualized alphas with t-statistics in parentheses):** constant purge **0.146 (7.58)**, CAPM **0.157 (8.32)**, FF3 **0.218 (9.88)**, FF6 **0.243 (10.65)**, full JKP **0.294 (12.74)**; R² against the 13 JKP theme portfolios falls to **11%** in the last column (Section 4.3 prose: "about 15% per year" for the weakly purged variants, "29% per year" for the full purge).
- **Size split (Section 4.4 / Figure 7):** full-JKP purge gives **Sharpe 2.7 for small/micro stocks** and **1.4 for large/mega stocks**; in the large-stock universe the best JKP factor reaches **0.9** (Section 1).
- **Conventional sorts (Section 6.4 / Table 7, Panel A, MSE approach):** equal-weighted top-minus-bottom quintile spread returns **12.8% per year** (CAPM alpha also **12.8%**, t = **13.3**, Sharpe **2.68**); capped value-weighted spread returns **6.7% per year** (alpha **6.7%**, t = **6.1**, Sharpe **1.25**). Sorting on MSRR weights instead gives an equal-weighted Sharpe of **2.9** versus **3.1** for the headline MSRR portfolio (Section 6.4).
- **Persistence (Section 4.5 / Figure 10):** predictability **drops by roughly half after one month** and takes **at least about 18 months** to become insignificant.
- **Turnover and cost (Section 4.5 / Figures 11–12):** one-sided turnover **75%** (JKP maximum **67%**); at **10 bp per dollar traded** the gap to JKP factors narrows; smoothing embeddings over the **most recent 6 months** is the stated net-of-cost optimum, and the source's conclusion is that net performance then still exceeds all JKP anomalies. **Exact net Sharpe numbers are figure-only → `data gap` (not printed in text).**
- **Rolling stability (Section 6.6 / Figure 24):** rolling 5-year Sharpe ratios range **2.1 to 4.5**, with a peak near **4.5** early and a drift down to the **2.1–2.5** range by the end of the sample; the source attributes the decline to LLM-era competition for the same signal (author conjecture).
- **Lookahead robustness (Section 6.1 / Figures 19–20):** with chronologically consistent LLMs (ChronoGPT), Sharpe falls from **3.1 to 1.6** (JKP residualization); point-in-time **1.63** versus foresight **1.61** — i.e. essentially no lookahead gap; the improved-training model of Kelly et al. (2026) lifts the point-in-time result to **1.9** over 2014–2022.
- **Other news sources (Section 6.3 / Figure 22):** Dow Jones Newswires gives Sharpe as high as **3.7**; Reuters third-party news **2.3**; both below/above the Reuters baseline of 3.1 as stated.
- **Shorter training windows (Section 6.7 / Figure 25):** rolling windows as short as 6 months still give Sharpe **> 2.1**; performance increases with window length.
- **Mechanism evidence (Sections 1, 5.4):** **62.1%** of anomaly weight sits on underreaction topics; 12 interpretable themes; news predictability from characteristics pooled R² ≈ **7.7%** (132 JKP) and **10.2%** (JKP + industries), with lagged characteristics up to 12 months performing indistinguishably from contemporaneous ones (Section 3 / Figure 3).
- **Sample coverage (Table 2):** 4,198 stocks/month on average; 52.5% monthly news coverage; 8.7 articles per covered stock-month.

### Independently reproduced

`Not independently reproduced.` This run performed only: direct retrieval and full-text reading of the pinned NBER PDF, a word scan of the whole extracted text for cost/execution terms, table/figure/section provenance location for every number above, and a repo-wide source-identity dedup. **No Sharpe, alpha, IC or turnover was recomputed; the Reuters feed, the JKP characteristic panel and the E5-Mistral embeddings were not obtained; the MSRR estimation was not run.**

### Negative evidence

- **Own rolling-window decay:** rolling 5-year Sharpe drifts from a peak near **4.5** down to **2.1–2.5** by the end of sample (Section 6.6 / Figure 24). The source's Section 4.2 statement that the strategy "does not appear to decay late in the sample" (Figure 4 Panel C) sits in tension with that later rolling-window decline; both are source statements and neither is reconciled in the pinned text.
- **Lookahead-hardened replication is half as good:** swapping the industrial-scale embedding model for a chronologically consistent academic model cuts Sharpe from **3.1 to 1.6** (Section 6.1) — the honest point-in-time number is roughly half the headline.
- **Cost sensitivity:** turnover **75%/month one-sided**, above every JKP factor; the only cost model is a flat 10 bp/dollar traded; **net Sharpe values are not printed in the text** (figure-only). With no spread, impact, borrow or capacity model, net-of-cost viability is unproven at the level of stated numbers.
- **Large-cap attenuation:** Sharpe **1.4** on stocks above the NYSE 50th size percentile (Section 4.4), i.e. the tradable, liquid part of the cross-section carries less than half the headline.
- **Conventional implementation is far weaker:** value-weighted quintile spread only **6.7%/yr, Sharpe 1.25** (Table 7 Panel A) — the headline 3.1 comes from a mean-variance-optimized, ex-post-volatility-standardized portfolio over the full cross-section.
- **Overlap with existing anomalies:** for the weakly purged variants, ~40% of news-portfolio variation is explained by 13 well-known anomaly themes (Section 4.3 / Table 4), i.e. part of "raw news" alpha is existing factor exposure.
- **Contrary record in our own repo:** `published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23.md` (arXiv:2607.06502) reports post-2005, large-cap, luck-adjusted decay of published anomalies to single-digit basis points per month; `benzinga-daily-headline-sentiment-cross-sectional-rank-ic-null-2026-09-24.md` reports a null news-sentiment rank-IC result on daily headlines. Both are different sources, but both point the same direction against naive text-signal profitability.
- **Source-quality caveats:** NBER working paper, explicitly not peer reviewed; one author discloses substantial AQR consulting income; the key input (Reuters feed) is licensed, unpublished and unreleased, so no third party can reproduce the baseline as specified.
- **Author-side acknowledgements:** the source concedes the magnitude is model-scale-dependent (Mistral 7B/7T tokens vs a 1.5B/71B-token chronologically consistent model) and that its own competition explanation for recent decay is a conjecture.
- **No capacity, borrow or fill analysis exists anywhere in the pinned text.**
- None of the above was found to be contradicted by an independent replication of this specific paper, because no independent replication was located; absence is not evidence of no negative result.

## Falsification plan

All thresholds and acceptance rules below are **`research-defined falsification thresholds`** and all operational choices not stated by the source are **`research-proposed`**. Action on failure for every test: **do not promote; keep `research-only` and record the failure in this record.**

- **F1 — Point-in-time replication (leakage).** Re-embed a sample of the news corpus with chronologically consistent (point-in-time) models only; recompute Z-scores, the within-month purge and MSRR strictly from data available through *t*. **Fail if** out-of-sample Sharpe < 1.4 (the source's own JKP-benchmark ceiling) or if the point-in-time result is worse than a foresight control by more than 0.3 Sharpe.
- **F2 — Cost ladder.** Re-run the headline and the 6-month-smoothed variants at 0/5/10/20/30 bp per dollar traded, plus a spread-aware model for the large-cap leg. **Fail if** net Sharpe ≤ 0 at 10 bp, or if the net Sharpe at 20 bp is below the best JKP factor's net Sharpe at the same cost.
- **F3 — Turnover discipline.** Measure one-sided monthly turnover on the 6-month-smoothed book. **Fail if** turnover > 100%/month (i.e. more than ~1.7× the source's own reported 75%) — `research-defined`.
- **F4 — Liquidity/capacity screen.** Restrict the universe to names above the NYSE 50th size percentile and cap participation at 10% of 21-day ADV. **Fail if** net Sharpe (at 10 bp) < 0.8 — `research-defined`.
- **F5 — Late-sample stability.** Compute rolling 5-year Sharpe on a frozen post-2018 window. **Fail if** the final rolling window is < 1.5 (the source reports a floor of 2.1) — `research-defined`.
- **F6 — Placebo / permutation.** Shuffle stock identities of the news embeddings within each month (preserving the cross-sectional distribution but destroying the stock–news link) and repeat the full pipeline for ≥ 1,000 draws. **Fail if** the real Sharpe does not exceed the 95th percentile of the placebo distribution.
- **F7 — Frozen forward test.** Freeze parameters (embedding model, purge set, λ grid, 6-month smoothing) at a pre-registered date and run ≥ 24 months of genuinely out-of-sample forward data. **Fail if** forward Sharpe ≤ 0 — `research-defined`.
- **F8 — Mechanism ablation (purge vs no purge).** Compare `ε`-portfolio against the raw-embedding portfolio and against the "predictable news" component under identical costs. **Fail the mechanism claim if** the residual portfolio's Sharpe advantage over the raw portfolio is < 0.5 (source reports 3.1 vs 1.1 gross) — `research-defined`.
- **F9 — Data-dependency transport.** Rebuild the signal from a *different* news corpus (e.g. Dow Jones, or a public/free news feed) with the same pipeline. **Fail if** Sharpe on the substitute corpus < 1.0 — `research-defined`; a failure would indicate the alpha is licensed-data-specific rather than mechanism-specific.
- **F10 — Model-scale audit.** Re-run with the smallest reasonable embedding model and with the chronologically consistent model. **Fail the "not lookahead-driven" claim if** the point-in-time model's Sharpe is below the JKP benchmark of 1.4 — `research-defined`.
- **F11 — Multiplicity control.** Because 4,096 coordinates, several purge sets, several training windows and two portfolio constructions are all explored, apply a Benjamini–Hochberg audit at q < 0.10 across the printed specification grid. **Fail if** the headline result does not survive — `research-defined`.
- **F12 — Anti-lookahead code audit.** Verify in code that Z-score moments, the purge regression, λ selection and MSRR weights use only data through *t*, and that no article timestamped inside month *t* is used before month-end *t*. **Fail on any violation.**

## Crypto portability

**`unproven`** — the pinned source contains zero crypto evidence (no spot, perpetual, futures or on-chain analysis anywhere in the PDF).

- **What could port structurally:** the two-stage recipe (embed text → residualize against prevailing asset characteristics → maximum-Sharpe long-short on the residual) is venue-agnostic in form and could be written down for a top-N crypto spot or perpetual universe with crypto-native characteristics (age, listing vintage, volatility, funding, beta, liquidity, on-chain activity).
- **What does not port:** the purging characteristics are the **JKP equity anomaly library** (book-to-market, accruals, profitability, investment), which has no crypto counterpart; a crypto port would therefore need a different characteristic set, changing the mechanism's residual definition. News arrival in crypto is 24/7 with no month-end boundary; the monthly calendar convention, the "articles held to month-end" rule and the JKP rank-standardization all need re-specification.
- **Crypto-specific risks the source does not address:** perpetual funding (paid every 8h), easy/cheap shorting but liquidation and leverage effects, venue fragmentation of both news and prices, mark/index price conventions, 24/7 candle boundaries and timestamp/timezone conventions, stablecoin quote-currency effects, listing/survivorship churn in small-cap perps, and custody/withdrawal risk.
- **Practical dependency:** the alpha as specified is **licensed-data-dependent** (Thomson Reuters Real-time News Feed). Crypto would require a different news or social-text source, so portability is at best a **ported hypothesis**, not crypto empirical evidence.

## Limitations

- **Not independently reproduced.** Every performance number is source-reported.
- **`data gap` — costs:** no spread, slippage, commission, market-impact, borrow, margin, capacity or fill model exists in the source; the only cost object is a flat 10 bp per dollar traded used in two figures; exact net Sharpe values are figure-only and not printed in the text.
- **`data gap` — execution:** order price, order type, session and timezone are never specified; the tradeable large-cap subset delivers Sharpe 1.4 gross, before any realistic spread.
- **`data gap` — data and code availability:** no public dataset, no repository, no data-availability or code-availability statement in the pinned PDF; the Reuters feed is licensed and was used privately, so the baseline is not reproducible by a third party as specified.
- **`underspecified`:** treatment of stocks with no news in a month inside the MSRR design; position/weight limits; borrow screen; the reporting frequency/units of the Figure 13 mean (5.3% → 4.8%).
- **`unproven` beyond the sample:** U.S. equities, 1996–2022, monthly only; no out-of-sample period after 2022; no live or prospective test; no independent replication located.
- **Source-internal tension (declared, not resolved):** "no major drawdowns / does not appear to decay" (Section 4.2) versus rolling 5-year Sharpe drifting 4.5 → 2.1–2.5 (Section 6.6).
- **Publication-bias / source-quality:** working paper explicitly not peer reviewed; author conflict-of-interest disclosure (AQR consulting income); the headline is an ex-post-volatility-standardized, mean-variance-optimized portfolio over 4,096 coordinates, with model, purge set, training window and smoothing choices all explored in the paper.
- **Multiple-testing exposure:** the specification grid (purge size k, purge set, embedding model, news corpus, training window, smoothing j, two portfolio constructions) is large relative to a single 1996–2022 sample; the source reports no multiplicity adjustment for the headline Sharpe.
- **Mechanism is not isolated from attention/coverage:** news coverage is strongly size-tilted (52.5% overall; 81.5% in the top decile), so the signal partly encodes coverage intensity.

## Implementation status

`implementation_status: not-implemented`. Nothing from this record has been implemented in our research stack: no embedding pipeline, no purge regression, no MSRR estimator, no Qlib backtest, no production card, no Paper, no Testnet and no Live run. This file is a normalized research capture only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this record in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. All third-party results above are source-reported and unreproduced.

## Related Wiki records

Pre-write Wiki Brain searches (`kb_search`) run this cycle: `LLM news text embedding return prediction anomaly` (1 hit), `news sentiment cross-sectional equity long-short return predictability` (0), `text embeddings equity factor anomaly market inefficiency` (0). The single hit — `quant/cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02.md` — was opened, judged **not mechanism-adjacent** (topological shape features on intraday returns, not text/news embeddings), and is therefore **not linked**. **No directly related Wiki strategy record was found for this source or mechanism**; that is a search result, not a claim that none exists. No Wiki link is fabricated.

## Sources

1. Didisheim, Antoine; Kelly, Bryan T.; Pourmohammadi, Mohammad; Tian, Hanqing. *"The Inefficient Pricing of News."* NBER Working Paper No. 35093, April 2026, Revised May 2026. DOI: `10.3386/w35093`. Landing page: https://www.nber.org/papers/w35093 (checked 2026-09-26).
2. Pinned primary PDF (all numbers, tables, figures and section citations in this record come from this artifact): https://www.nber.org/system/files/working_papers/w35093/w35093.pdf — retrieved 2026-09-26 CST, HTTP 200, `application/pdf`, 8,518,296 bytes, SHA-256 `6b1db3f173cbd720e6cf02c5e40befedd147510968485d8b62587c25158626a8`; text layer 158,250 characters / 4,355 lines / 76 page breaks.
3. Companion preprint record (version metadata only, no numbers): SSRN `abstract_id=6540399`, *"The Inefficient Pricing of News"*, 75 pages, posted 8 Apr 2026, last revised 20 May 2026, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6540399 (checked 2026-09-26).
4. Methodological works cited *by* the source and reproduced here only as the source's own references (not used as independent evidence): Kelly, B. T. and Xiu, D. (2023) on maximum-Sharpe-ratio regression; Jensen, T. I., Kelly, B. T., and Pedersen, L. H. (2022) on the JKP anomaly universe; Frazzini, A., Israel, R., and Moskowitz, T. J. (2018) on trading costs (the origin of the 10 bp assumption); Wang et al. (2024) E5-Mistral-7B; He et al. (2025) chronologically consistent LLMs; Ball et al. (2016) for the `cop_at` factor.
