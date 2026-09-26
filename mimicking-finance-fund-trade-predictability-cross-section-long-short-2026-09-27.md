---
schema: strategy-research-record-v1
title: "Mimicking Finance: Fund-Manager Trade-Predictability Cross-Section, Long Least-Predictable / Short Most-Predictable US Stocks (NBER Working Paper 34849)"
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - mutual-fund-holdings
  - behavior-predictability
  - cross-sectional
  - us-equity
  - institutional-signal
  - machine-learning
status: research-only
confidence: medium
source_as_of: 2026-02-16
sources:
  - "Lauren Cohen, Yiwen Lu, and Quoc H. Nguyen, 'Mimicking Finance', NBER Working Paper 34849, DOI 10.3386/w34849, Issue Date February 2026 (landing citation_publication_date 2026/02/16). https://www.nber.org/papers/w34849"
  - "https://doi.org/10.3386/w34849"
  - "Pinned primary-source PDF: https://www.nber.org/system/files/working_papers/w34849/w34849.pdf - HTTP 200, 6,616,358 bytes, 79 pages, SHA-256 cec210777463d593fd49c4d469814f7545f25d302d800745df04024b3f661b27, downloaded 2026-09-27 and text-extracted with pypdf 6.16.2 to 122,274 characters, read end to end (cover, Abstract, Sections 1-8, References, Figures 1-11, Tables I-XIV, Appendix A-B)."
  - "Discovery-only, not pinned and not used for any number in this record: earlier public author draft dated November 24, 2025 at https://www.rotman.utoronto.ca/media/rotman/Mimicking-Finance---Nov-2025.pdf and a mirror at https://chelseayao.com/static/file/Cohen_Lu_Nguyen_WP25_Mimicking%20Finance.pdf (found via web search 2026-09-27; not opened for quantitative content, so all figures here come from the NBER February 2026 PDF only)."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Source-internal (Section 7.1 vs Table XII): the prose says 'the Correct Predictions Portfolio outperforms the Incorrect Predictions Portfolio during nearly the entire sample period', while Table XII reports the opposite ordering (Incorrect/Harder-to-Predict 7.981% vs Correct/Easier-to-Predict 7.069% annualized) and the very next clause of the same sentence describes a cumulative Incorrect-minus-Correct gap that is rising. Most consistent with a swapped-label typo in the prose, but it is unresolved inside the source and is not silently repaired here."
  - "Source-internal (Introduction vs Section 7.2 vs Table XIII note): the 424 bp Q1-Q5 spread is described as an annualized return 'in the next quarter' (Introduction, p.3), as 'annualized over the next year' (Section 7.2, p.30), and as a 'quarterly performance differential ... annualized by multiplying by four' (Table XIII note). The record adopts the Table XIII note as the authoritative reading (1-quarter holding, annualized by x4) and flags the other two wordings as inconsistent."
---

# Mimicking Finance: Fund-Manager Trade-Predictability Cross-Section, Long Least-Predictable / Short Most-Predictable US Stocks (NBER Working Paper 34849)

## Provenance

- **Primary source (authors, exactly as the source):** Lauren Cohen (Harvard University, Harvard Business School, and NBER; lcohen@hbs.edu), Yiwen Lu (University of Pennsylvania, The Wharton School; yiwelu@wharton.upenn.edu), and Quoc H. Nguyen (DePaul University; qnguye14@depaul.edu). Three authors only. The order "Lauren Cohen / Yiwen Lu / Quoc H. Nguyen" is identical across (a) the PDF cover page, (b) the PDF title page and abstract block, and (c) the NBER landing `citation_author` fields. The cover prints surname-only forms, the title page prints full names, and the paper's own reference list cites the first author as "Cohen, L." — all consistent.
- **Identifier / version / date:** NBER Working Paper **34849**, **DOI 10.3386/w34849**, PDF cover and title page both print **"February 2026"**, NBER landing **Issue Date February 2026**, landing `citation_publication_date` and `dcterms.date` both **2026/02/16**, JEL **C45, C53, C55, C82, G11, G23**. The landing page (fetched 2026-09-27, HTTP 200) shows **no Revision Date and no "Other Versions" block**, so the February 2026 PDF is the single NBER version. NBER working-paper cover text: papers "have not been peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies official NBER publications" ⇒ **not peer reviewed**.
- **Pinned primary source:** `https://www.nber.org/system/files/working_papers/w34849/w34849.pdf`, **6,616,358 bytes, 79 pages, SHA-256 `cec210777463d593fd49c4d469814f7545f25d302d800745df04024b3f661b27`**, downloaded and read end to end on **2026-09-27** (122,274 extracted characters; every table below was re-read cell by cell from the extracted text of pages 51-67, and every figure caption from pages 40-50).
- **PDF metadata:** `/CreationDate D:20260127145905Z`, `/ModDate D:20260211101003-05'00'`, `/Creator LaTeX with hyperref`, `/Producer` empty, `/Creator` banner `pdfTeX 3.141592653-2.6-1.40.26 (TeX Live 2024)`; `/Title`, `/Author`, `/Subject`, `/Keywords` are **empty**, so identity rests on the cover/title page plus the landing metadata, which agree.
- **Acknowledgements / disclosures (PDF cover, verbatim scope):** a long thank-you list (Suman Banerjee, Stefano Bonini, Brigham Brau, William Cong, Patricia Dechow, Winston Wei Dou, Cameron Ellis, Paul Gao, Jon Garfinkel, Itay Goldstein, David Hirshleifer, Gerard Hoberg, John Hund, Byoung-Hyoun Hwang, Zoran Ivkovich, Ron Kaniel, Scott Kominers, Seokwoo J. Lee, Bradford Levy, Erik Lie, Claudia Moise, Sean Myers, Anna Pavlova, Carmen Payne-Mann, Lin Peng, Tarun Ramadorai, Jonathan Reuter, Alberto Rossi, Denis Schweizer, Devin Shanthikumar, Richard Sloan, Jonathan Sokobin, Chester S. Spatt, Jess Stauth, Lorien Stice-Lawrence, Siew Hong Teoh, Jose Tribo, Wei Xiong, Jiajie Xu, Mao Ye, Yao Zeng, and Miao Ben Zhang, as printed) plus a seminar list (University of Iowa, Harvard, NBS at NTU, UGA Fall Finance Conference, CETAFE, CFEA, Society of Quantitative Analysts Boston, BFWG, NBER Big Data/AI/Financial Economics, RCF-ECGI, CUHK-RAPS-RCFS, SQA, AI in Finance), followed by "All remaining errors are our own" and the standard NBER non-endorsement disclaimer. A whole-text scan returns **zero hits for `conflict`, `disclos`, `funding`, `grant`, `sponsor`, `data availability`, `upon request`, `github`, and `replicat*`** ⇒ funding source, conflict statement, code availability, data availability and replication-package status are all **`not stated in source`**.
- **Canonical schema resolution:** `kb_read quant/strategy-research-record-spec-v1.md` → **10,289 bytes**, sha256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7` (identical to the previous run); `kb_read quant/strategy-research-record-spec-v2.md` → **file not found**, so **v1 remains canonical** (schema `strategy-research-record-v1`, 15 frontmatter keys, 13 body sections, 5 subsections).
- **Repo sync:** `git pull origin main` → already up to date before research; `git log --oneline -20` inspected; `git status --porcelain --untracked-files=no` clean.
- **Repo-wide source-identity dedup (2026-09-27, deterministic, `rg -uu` across the whole repository including hidden trees `.mimo-worktrees/`, `.agents/`, `.hermes/`, `.git` history, every `*.md`/`*.csv`/`*.json`/`*.txt` and `coverage_manifest.csv`)** for the patterns `10.3386/w34849`, `w34849`, `34849`, `Mimicking Finance`, `Yiwen Lu`, `Quoc H\. Nguyen`, `Quoc Nguyen`, `prediction precision`, `percent of correct prediction` → **every pattern returned zero hits except a single `Quoc Nguyen` occurrence**, and that occurrence was inspected line-by-line: it is a bibliography entry for a *different* paper (Cohen & Nguyen, "Moving Targets," SSRN 4736129, cited as a baseline inside `llm-moving-targets-metric-shift-earnings-call-cross-section-2026-09-24.md`). A separate `mimick*` scan returned only incidental verb uses ("mimic/mimicking") in unrelated records. ⇒ **no existing record shares this canonical source identity**, so a new record is legitimate.
- **Four-axis distinction (mechanism / signal construction / universe / horizon / data dependency) against the nearest existing records** — every pair differs on at least one axis, and most differ on all five:
  - `sec-form-13f-institutional-cloning-staleness-falsification-2026-09-13.md` (13F cloning of institutional positions): **source** differs (SEC 13F filings vs NBER WP 34849); **mechanism** differs (copy the informed trade vs avoid the mechanically replicable trade); **signal construction** differs (raw position changes with staleness decay vs LSTM trade-direction accuracy aggregated per stock).
  - `mutual-fund-redemption-forced-sale-residual-supply-absorption-premium-2026-09-24.md` (arXiv 2605.30672): source differs; mechanism differs (forced-sale liquidity absorption vs behavioural non-compensation for replicable behaviour); universe differs (fund-flow-driven names vs top-100 active-equity holdings).
  - `fund-50-5-10-constrained-ownership-share-large-equity-underpricing-2026-09-26.md` (NBER WP 35007): source differs; mechanism differs (regulatory long-position cap → temporary discount vs manager-behaviour predictability → crowd-priced trades); signal construction differs (constrained-ownership share C vs prediction-precision quintile).
  - `sec-form-144-aborted-insider-intent-expiration-drift-2026-09-24.md` and `anomaly-pre-release-drift-predicted-signal-decile-portfolios-2026-09-23.md`: different sources, event-driven horizons (days), different data dependencies (Form 144 / pre-release drift).
  - `two-stage-adaptive-shrinkage-golden-criterion-equity-premium-2026-09-02.md`, `gq-lasso-quantile-equity-premium-timing-2026-09-02`-family and `cross-sectional-realized-skewness-dispersion-market-timing-2026-09-24.md`: aggregate market-timing / forecast-combination mechanisms with different sources, horizons (monthly/quarterly aggregate) and data dependencies; this record is a **cross-sectional stock** signal built from **holdings-derived behavioural accuracy**.
  - `retail-agent-structured-adverse-timing-2026-09-02`-family and the LLM-agent records: different sources entirely (LLM agent behaviour vs mutual-fund holdings).

## Economic mechanism

### Source-reported

The paper's stated thesis (Abstract, Sections 1 and 2, Section 8) is an **equilibrium-compensation argument about replicable behaviour**, not a trading rule:

- "Agents should not be compensated for aspects of their behavior and human capital that can be replicated in a low-cost way" (Section 1, p.1). A single-layer LSTM trained only on a fund's own past behaviour plus observable fund/firm/market conditions predicts **71% of its quarterly buy/hold/sell decisions**, versus **52%** for a max-frequency (majority-class / zero-rule) baseline, a **36.5% relative increase, p < 0.0001** (Section 5.1, Figure 3, Table II).
- The Section 2 model separates **routine** (scalable, cheap to imitate) from **non-routine** (costly-effort) tasks and derives pooling/separation equilibria before and after AI; the empirical content offered is that routine, mechanically reproducible behaviour should command a **lower equilibrium price**.
- **Performance claim (source-reported):** predictability of trading is monotonically related to subsequent performance. At the **fund** level, least-predictable managers (Q1) earn category-relative cumulative excess returns of **0.14% (t=2.05)** at one quarter rising to **0.36% (t=2.88)** at four quarters, while the most-predictable (Q5) earn **−0.42% (t=2.36)** at four quarters, giving a Q1−Q5 spread of **0.23% (t=2.13)** → **0.79% (t=3.05)** (Table X). At the **stock** level, aggregating accuracy across all funds holding each stock, the least-predictable quintile (Q1) beats the most-predictable quintile (Q5) by **424 bp annualized (t=5.74)** with monotone quintile returns (Table XIII).
- The source's own casual mechanism story for *why* the stock-level spread exists is one sentence in Section 7: predictable funds "could be those that follow more mechanical strategies, that may be relatively easier for models to learn, but also potentially for markets to anticipate, learn, and quickly price, reducing their ability to generate alpha," whereas unpredictable funds "may reflect managers who adapt dynamically or exploit informational advantages." The source presents this as a possibility ("could", "may"), **not as an identified causal channel**, and runs no test that separates it from the alternative explanations its own Tables VII-IX imply.

### Research interpretation

- **Hypothesized mechanism (falsifiable form, `research interpretation`):** *crowding / mechanical-trade anticipation.* Stocks whose aggregate holder trades are easiest to mimic are the stocks most likely to be held through templated, style-driven, easily front-run rules; those trades are anticipated and priced, so the "easy to mimic" cohort underperforms and the "hard to mimic" cohort outperforms. The tradable statement is the cross-sectional spread, not the fund-level spread.
- **Competing mechanism that the source's own tables make live (`research interpretation`, not source-reported):** the accuracy score is *deterministically* related to observable characteristics, so the spread may be a **characteristics tilt in disguise**. From Tables VII-IX (all source-reported, but their implication is ours): low-precision stocks are **larger** (Market Equity −0.0000***, Table VII col 2), **younger**, **more widely held** (−0.0002***, col 3), **lower book-to-market** (+0.0365*** on BE/ME, Table VIII col 7), **higher R&D/Sales** (−0.0092***, col 4), **more earnings-surprised** (−0.0002**, col 9), **lower free cash flow and lower net equity payout** (+0.0235*** / +0.2564***, cols 6 and 8), and **higher past-1-month return** (−0.0239***, Table IX col 1). That is a *growth / recent-winner* tilt, i.e. long-growth-short-value plus short-term **continuation** exposure (the opposite of the classical one-month reversal), not obviously a behavioural "unpredictability" premium.
- **Role of each component if one tried to trade it** (all `research-proposed`, none source-specified as a rule): *Signal layer:* quarterly stock-level average trade-direction accuracy. *Portfolio layer:* equal-weighted Q1 long / Q5 short. *Holding/rebalance layer:* one quarter. *Risk layer:* none exists in the source — no stop, no vol target, no exposure neutralisation beyond whatever the FF alphas implicitly measure.
- The record does **not** assume the behavioural channel is the operating one; the falsification plan below is built mainly around killing the characteristics explanation.

## Signal

Two layers must be separated: the **model layer** (source-reported in detail) and the **tradable cross-section** (source-reported as a portfolio sort, but with material operational gaps).

**Model layer (source-reported, Section 3.1-3.3, Figure 2, Appendix A)**

- **Panel construction:** fund-security holdings from Morningstar Direct (SEC **N-30D, N-CSR, N-Q, N-PORT** filings and fund prospectuses), reported quarterly or semiannually. Universe: **actively managed U.S. equity mutual funds**, excluding **index, sector-specific, balanced, and international** funds. Sample period **1990-2023**. Monthly calendar with **forward carry-forward of missing fund-security months** ("If a month is missing ... we carry forward its last known values"), a **"recent non-zero" fill for up to six months** if a security disappears and reappears, then restricted to **quarter-ends (Mar/Jun/Sep/Dec)**. Funds must span **≥ 7 calendar years** and hold **≥ 10 securities per quarter**. Holdings are rank-ordered by market value into fixed slots `id = 1..N` with **padding** for empty slots. Final dataset: **1,706 unique mutual funds, 5,434,702 fund-security-quarter observations**. Section 4 states the analysis covers **the top 100 positions** held by these funds (average position ≈ $6 million; average held-firm ME ≈ $30 billion, median $6 billion).
- **Target:** `Δsh_{i,t} = (sh_{i,t+1} − sh_{i,t}) / (sh_{i,t} + 1)`, three classes: **−1 if Δsh ≤ −0.01**, **0 if |Δsh| < 0.01**, **+1 if Δsh ≥ 0.01** (a ±1% band is "no change"). Prediction task is at the **fund-security-quarter** level.
- **Features (all lagged so they are observable when predictions are made):** fund-level lagged prior-quarter and multi-quarter returns, net quarterly flows, lagged fund size and holdings-based value/momentum; security-level log market equity, book-to-market, past-return momentum and factor exposures (market, size, value, profitability, investment, short-term reversal) drawn from the **JKP Global Factor Database** and merged at permno-month; **peer activity rates** (share-increase / share-decrease / no-change frequencies) within the fund's Morningstar style category plus lags; macro from **FRED** (real and nominal short rates, 10-year yield, yield-curve slope, BAA-Treasury spread, term spreads 5y−1y and 10y−3m, default spread, related yields) lagged to the quarter; within-fund context (current position market value, lagged share counts up to six quarters, portfolio-weight dynamics, size rank within the fund, and a padding indicator).
- **Model:** **single-layer LSTM**. Input is a tensor `X ∈ R^{T×N×F}` with **T = 8 consecutive quarters**, securities ordered descending by market value, cross-section vectorised to an `N·F`-dimensional sequence. Rolling design: **28-quarter windows** split chronologically into **20 quarters training + 8 quarters testing**, **no shuffling**; windows advance **one quarter at a time** (Figure 2: Observation 1 trains 2000Q1-2004Q4 / tests 2005Q1-2006Q4; Observation 3 trains 2000Q3-2005Q2 / tests 2005Q3-2007Q2). **Dropout and recurrent dropout 0.25 each**; softmax over an `N×3` probability grid; **time-step mask** when a whole cross-section is synthetic padding; **output feasibility mask** zeroing `p_{−1}` and renormalising over `{0,+1}` when the security lacks continuous presence over the 8-quarter input horizon (a looser variant only requires presence in the final input quarter). Loss: **weighted categorical cross-entropy**, class weights default 1, optional **focal variant with γ = 1**; optimiser **Adam** with early stopping on validation loss, **max 50 epochs**.
- **Evaluation metric:** *Prediction Precision* = weighted average fraction of correct direction predictions, restricted to test outputs where the feasibility mask permits a sell decision; baseline = the max-frequency class from the training window. Results: **0.71 mean (sd 0.14, min 0.14, median 0.73, max 1.00)** vs naive **0.52 (sd 0.21, min 0.00, median 0.53, max 1.00)** over **N = 53,489** fund-quarters (Table II); **44.38%** of managers fall below 50% accuracy under the naive method vs **11.11%** under the model; the highest single Morningstar style is **mid-cap blend at 75%** (Section 5.1-5.2, Figures 3-5). The prediction-precision time series is printed for **1995Q1 to 2023Q1** (Figure 4, Panel A).

**Tradable cross-section (source-reported as a sort; `underspecified` as a rule)**

- **Formation:** "Each quarter, stocks are ranked by the average prediction accuracy of all funds holding that stock and sorted into five **equal-weighted** portfolios." **Quintile 1 (Q1)** = stocks where managers' trades are **least** predictable (lowest average accuracy); **Quintile 5 (Q5)** = most predictable (Table XIII note; Figure 10 caption). Only stocks held by at least one of the 1,706 sample funds can enter the sort ⇒ the tradable universe is a **fund-held subset of US listed equities**, not the CRSP/total market.
- **Holding period / cadence:** the Table XIII note states the Q1−Q5 column is a **quarterly** differential and that "the estimates of the returns and alphas are annualized by multiplying by four" ⇒ **one-quarter holding, quarterly rebalance** is the reading adopted here. The Introduction instead says "in the next quarter" and Section 7.2 says "annualized over the next year" — both are inconsistent with the table note and are recorded as source-internal contradictions in the frontmatter.
- **Direction:** the source reports the **Q1−Q5 difference** (long least-predictable, short most-predictable). It never writes an instruction to trade it; the long-short framing is how the source itself labels the row, but converting it into an executable trade is **`research-proposed`**.
- **Not specified by the source ⇒ `underspecified` (never guessed here):** the timestamp/timezone of formation; **when the aggregated accuracy value becomes available** (a prediction made at quarter `t` is scored against the `t+1` share change, so the score for `t` is not knowable at `t`; the source never states the availability lag); the SEC **filing lag** of N-Q/N-CSR/N-PORT holdings, which is likewise never addressed; the exact evaluation window used to score accuracy in a given formation quarter; breakpoints (no NYSE breakpoint rule is printed — the sort is described only as "five equal-weighted portfolios"); minimum breadth per quintile; tie handling; delisting and corporate-action treatment; the return series and the factor library used for Tables X-XIII; whether Q1−Q5 is dollar-neutral or beta-neutral; and every execution detail (order type, price, latency, partial fills).
- **Parameters summary:** target band ±1%; T = 8 quarters input; 28-quarter window with 20/8 train/test split; dropout 0.25/0.25; focal γ = 1 (optional); 50 epochs; class weights 1 (default); funds ≥ 7 years and ≥ 10 holdings; top-100 positions; **all of these are source-reported**, none is Scout-tuned. Anything the source does not print — quintile count is source-reported as 5, but leg weighting, neutralisation, cost ladder and entry/exit price — is **`research-proposed`**.

## Required data

- **Instrument / universe:** US-listed common stocks held by actively managed US equity mutual funds; **1,706 funds**, **5,434,702 fund-security-quarter** observations, top-100 positions per fund, quarter-end snapshots, 1990-2023 (fund panel), 1995Q1-2023Q1 (printed prediction-precision panel).
- **Holdings data:** Morningstar Direct fund-security holdings (shares and market value) sourced from **SEC N-30D, N-CSR, N-Q, N-PORT** filings and prospectuses, quarterly or semiannual; forward fill to monthly, "recent non-zero" fill up to six months, then keep Mar/Jun/Sep/Dec.
- **Fund characteristics:** Morningstar (inception, category, manager metadata) **and** CRSP Mutual Fund Database (monthly TNA, fund returns, expense ratio, turnover, income yield), merged first on ticker then on CUSIP; **all funds retained regardless of survivorship status**.
- **Security characteristics:** JKP Global Factor Database (Jensen, Kelly and Pedersen 2023), monthly, merged at permno-month.
- **Macro:** FRED (real/nominal short rates, 10-year yield, curve slope, BAA-Treasury spread, term and default spreads).
- **Return series for Tables X-XIII and the FF3/FF4/FF5 alphas:** **`not stated in source`**. The paper names no stock-return database, no risk-free series, no factor library and no delisting convention; "risk-free" appears only inside the printed factor definitions `Mkt–RF`. This is a hard `data gap`, not an inference.
- **Point-in-time / availability:** the source states all features are lagged "so that they are observable at the time predictions are made" and that the rolling design "ensures that predictions are always generated out-of-sample, preventing look-ahead bias" (Section 3.3, Figure 2 caption). **No statement exists about the availability lag of holdings filings or of the accuracy score itself** ⇒ `underspecified`.
- **Missing data:** forward-carry of missing fund-security months and a six-month "recent non-zero" fill are explicitly specified by the source (imputation is source-reported, not Scout-introduced). Delisting, suspension and bad-print handling for the *return* series: `not stated in source`.
- **Funding / fee / spread needs:** none are specified anywhere; see Execution assumptions.

## Execution assumptions

- **Method-level cost determination (Section 3, Section 7, Sections 4-6, Tables I-XIV, Figures 1-11, Appendices A-B, plus a whole-text word scan of the pinned 79-page PDF):**

| Term | Hits in pinned PDF | Meaning of the hits |
|---|---|---|
| `transaction cost` | **0** | — |
| `trading cost` | **0** | — |
| `commission` | **0** | — |
| `slippage` | **0** | — |
| `bid-ask` / `bid ask` | **0** | — |
| `market impact` | **0** | — |
| `capacity` | **0** | — |
| `funding` (financing) | **0** | — |
| `borrow` | **0** | — |
| `net of cost` / `gross return` | **0** | — |
| `fee` | 24 | fund **management fees**, 12b-1 fees, expense ratios, **redemption/sales-restriction fees** — never a trading-cost model |
| `cost` | 12 | theory costs (`C_t(e)`, "costly non-routine effort"), "low-cost" replication, literature remarks about active managers net of costs — never a trading-cost model |
| `turnover` | 20 | **fund turnover ratio** as a fund characteristic and as an explanatory variable for predictability — never portfolio turnover of the Q1−Q5 spread |
| `margin` | 7 | marginal-cost/marginal-benefit theory and "marginally significant" — never margin/leverage financing |
| `liquidity` | 2 | cited literature (Kacperzyk et al. 2008) and a remark about style rebalancing/liquidity needs — no liquidity model |
| `fill` | 1 | the six-month "recent non-zero" holdings **data fill** — not an order fill |

  ⇒ **The source contains no transaction-cost, spread, slippage, impact, borrow, financing, leverage, margin, participation, capacity or fill model of any kind.** Every one of those fields is recorded as **`data gap`, never zero**, and the gross/net status of Tables X-XIII is **`not stated in source`**. No result in this record may be read as net-of-cost evidence.
- **Signal-to-order timing:** `not stated in source`. Order type, market vs limit, same-bar vs next-bar, latency, partial fills, failure handling, and price basis (close vs next open) are all `underspecified`.
- **Shorting / borrow:** the headline spread is a **short leg in Q5**. Borrow availability, stock-loan fee and rebate are **`not stated in source`**; nothing in the paper establishes that Q5 names are borrowable.
- **Leverage / margin:** `not stated in source`.
- **Turnover and capacity:** `not stated in source`; the sort is quarterly and equal-weighted, so turnover exists but is never printed or bounded.
- **`research-proposed` execution layer (Scout's, not the source's):** form at the quarter-end close using only accuracy values that are computable at that date once filing lags are respected; enter on the next trading day's close; equal-weight the long and short legs; rebalance quarterly; mark-to-market continuously; and evaluate a 0/1/5/10/20/30 bp one-way cost ladder plus a commission schedule. **None of this is source-reported.**

## Evidence

### Source-reported

Every figure below is **source-reported**, traced to the pinned NBER WP 34849 PDF (SHA-256 `cec21077…`), read on 2026-09-27. **None has been independently reproduced.** All results are **US mutual-fund / US equity evidence**; **there is no crypto evidence in this source.**

**Model accuracy (Table II, Section 5.1, Figures 3-5):**

| Quantity | Model | Naive (max-frequency) |
|---|---|---|
| Prediction Precision, mean | **0.71** | **0.52** |
| sd / min / median / max | 0.14 / 0.14 / 0.73 / 1.00 | 0.21 / 0.00 / 0.53 / 1.00 |
| Observations | 53,489 fund-quarters (Table II) | 53,489 |
| Share of managers below 50% accuracy | **11.11%** | **44.38%** |

Relative improvement **+36.5%, p < 0.0001** (Section 5.1). Highest style: **mid-cap blend 75%** (Section 5.2).

**Headline cross-section — Table XIII, quintile stock portfolios on average fund prediction accuracy, five equal-weighted portfolios, estimates annualized ×4:**

| Return specification | Q1 (least predictable) | Q2 | Q3 | Q4 | Q5 (most predictable) | Q1−Q5 |
|---|---|---|---|---|---|---|
| Return | **8.707*** (3.85)** | 7.884*** (3.79) | 6.745*** (3.17) | 5.765*** (2.61) | 4.467* (1.73) | **4.240*** (5.74)** |
| Excess Return | 6.476*** (2.85) | 5.653*** (2.70) | 4.513** (2.11) | 3.533 (1.59) | 2.236 (0.86) | **4.240*** (5.74)** |
| FF3 alpha | 2.689 (1.53) | 1.803 (1.12) | 0.526 (0.33) | −0.543 (0.33) | −1.736 (0.85) | **4.425*** (6.08)** |
| FF4 alpha | 3.254* (1.78) | 2.524 (1.52) | 1.686 (1.03) | 0.392 (0.23) | −0.303 (0.15) | **3.557*** (5.12)** |
| FF5 alpha | 1.753 (0.92) | 0.706 (0.41) | −0.446 (0.26) | −1.842 (1.03) | −2.109 (0.95) | **3.862*** (4.96)** |

(FF3 = Mkt–RF, SMB, HML; FF4 adds MOM; FF5 adds RMW, CMA. Stars: *** p<0.01, ** p<0.05, * p<0.10.) Note that **no single quintile leg is significant at 5% in the FF3/FF4/FF5 rows** while the spread t-stats are 4.96-6.08; the table prints **no observation count and no sample period** ⇒ `data gap`.

**Fund-level performance — Table X (cumulative excess fund returns versus the *average fund in the same Morningstar category*, horizons 1-4 quarters ahead):**

| Horizon | Q1 | Q2 | Q3 | Q4 | Q5 | Q1−Q5 |
|---|---|---|---|---|---|---|
| CRET[0,1] | 0.14** (2.05) | 0.06 (0.82) | 0.06 (1.12) | −0.04 (0.64) | −0.09 (1.52) | **0.23** (2.13)** |
| CRET[0,2] | 0.25*** (2.58) | 0.13 (1.31) | 0.12 (1.22) | −0.05 (0.56) | −0.22** (2.07) | 0.47*** (2.87) |
| CRET[0,3] | 0.33*** (3.18) | 0.21* (1.76) | 0.17 (1.39) | −0.02 (0.21) | −0.31** (2.47) | 0.64*** (3.34) |
| CRET[0,4] | 0.36*** (2.88) | 0.34** (2.31) | 0.18* (1.66) | 0.06 (0.44) | −0.42** (2.36) | **0.79*** (3.05)** |

**Table XI (4-quarter cumulative excess return and factor alphas for fund quintiles):** Excess Return 0.365***(2.86) / 0.319**(2.15) / 0.156(1.43) / 0.035(0.26) / −0.449**(2.49), spread **0.815***(3.05)**; FF3 alpha 0.374***(2.80) / 0.285*(1.85) / 0.185(1.62) / 0.091(0.64) / −0.439**(2.33), spread **0.812***(2.85)**; FF4 alpha 0.308**(2.24) / 0.313*(1.95) / 0.281**(2.45) / 0.119(0.80) / −0.475**(2.43), spread **0.783***(2.66)**; FF5 alpha 0.370***(2.58) / 0.105(0.66) / 0.249**(2.04) / 0.079(0.51) / −0.409**(2.03), spread **0.779**(2.53)**. The Section 7.2 prose summarises these as alphas "ranging from 0.78% to 0.82%" for the spread.

**Table XII (fund-quarter split into Harder-to-Predict / Easier-to-Predict holdings, annualized ×4):** Return **7.981***(61.59)** vs **7.069***(54.62)**, difference **0.912***(12.41)**; Excess Return 6.490 vs 5.579, difference 0.912***(12.41); FF3 alpha 1.897 vs 0.800, difference 1.097***(14.37); FF4 alpha 2.177 vs 1.276, difference 0.902***(11.60); **FF5 alpha 0.624***(5.21) vs −0.459***(3.95)**, difference 1.083***(13.03).

**Table XIV (Fama-MacBeth, dependent variable cumulative abnormal return quarters 0→4, Newey-West standard errors, N = 40,585; t-statistics printed as magnitudes):** Prediction Precision **−0.8554** (2.06)**, **−1.0074** (2.38)** with Active Share, **−1.0261*** (2.70)** additionally controlling for RET[−1,0] and CRET[−4,0]; Active Share **0.0041***(5.13)** and 0.0032***(4.57); RET[−1,0] 0.1311**(2.09); CRET[−4,0] 0.0628**(2.12); constants 0.6736/0.5527/0.5648; R² 0.00533 / 0.00854 / 0.106.

**Determinants of the accuracy score (Tables VII-IX; two-way clustered SEs at firm and quarter):**

- Table VII: Portfolio Position **0.0020*** (52.407)** (smaller relative positions are *more* predictable); Market Equity **−0.0000*** (3.375)**; #Funds Position Held In **−0.0002*** (4.659)**; Firm Age **0.0000*** (5.114)**; N = 5,316,273-5,958,755; R² ≈ 0.244-0.253.
- Table VIII: Total Debt/ME **0.0083*** (4.739)**; Asset Turnover **−0.0000*** (66.758)**; Sales/BE 0.0002 (0.581); R&D/Sales **−0.0092*** (2.668)**; Gross Profit/ME 0.0005 (0.110); Free Cash Flow/ME **0.0235*** (3.373)**; Book Equity/ME **0.0365*** (16.053)**; Net Equity Payout/ME **0.2564*** (16.216)**; Earnings Surprise **−0.0002** (1.992)**; N ≈ 2,995,288-5,323,840 per column; R² ≈ 0.223.
- Table IX: Past 1 Month Return **−0.0239*** (printed 3.089)**; Momentum 1-6 Months −0.0000 (0.928); Momentum 1-12 Months −0.0019 (1.341); CAPM Idiosyncratic Vol **0.1857* (1.722)**; N = 5,213,302-5,286,960; R² ≈ 0.223-0.224; quarter-year fixed effects throughout.

**Fund/manager determinants (Sections 6.1, Tables IV-VI, source-reported in prose):** longer manager tenure and managing more funds/more styles ⇒ **higher** precision; manager ownership in the fund ⇒ **lower** precision (ownership indicator 0.0578, t = 4.874); older funds ⇒ higher precision; more within-category and within-family competition ⇒ lower precision; larger teams, larger funds, higher turnover (−0.0149, t = −9.712), heavier flows and higher management fees (−0.0078, significant at 5%) ⇒ lower precision.

**Figures:** Figure 8 (fund-quintile cumulative abnormal returns by horizon), Figure 9 (cumulative Correct vs Incorrect portfolios plus their cumulative gap), Figures 10-11 (stock-quintile cumulative returns, the Q1−Q5 cumulative line, per-quintile mean quarterly returns with t-stats, and four risk-adjusted cumulative panels). **None of these figures prints numeric axis values in the text layer** ⇒ exact curve values are `data gap`; only the caption-level statements above are usable.

### Independently reproduced

not independently reproduced.

(No LSTM was trained, no quintile portfolio was rebuilt, and no factor regression was run in this repository. The inputs — Morningstar Direct, CRSP Mutual Fund Database, JKP Global Factor Database, FRED, and an unnamed return/factor source — include licensed commercial databases that are not available to this Scout, and the source publishes no code, no seeds, no hyperparameter file and no replication package.)

### Negative evidence

1. **No transaction-cost model exists anywhere in the source** (Methods-level read of Sections 3, 4-7 plus a full-text word scan of the 79-page pinned PDF; see the table in Execution assumptions). Commission, fees (as trading costs), spread, slippage, impact, participation, capacity, borrow, financing, leverage, margin, latency, fill and turnover are all `data gap` — **never zero** — so no Table X-XIII number may be read as net of cost, and the gross/net label is itself `not stated in source`.
2. **The strategy's turnover is never reported and never defined**, despite a full quarterly re-sort of an equal-weighted long/short pair of quintiles. Cost sensitivity is unmeasured.
3. **Hard look-ahead risk in the tradable signal is never addressed.** Two separate availability lags are unmodelled: (a) SEC **N-Q / N-CSR / N-PORT** holdings are published weeks to months *after* the quarter-end they describe, yet the sort uses quarter-end holdings directly; (b) the *prediction accuracy* of a fund's trade at quarter `t` is scored against the **`t+1`** share change, so an accuracy value labelled `t` cannot be known at `t` without waiting a quarter, and the paper never states which lag (if any) it applies. **This is a `research interpretation` by this Scout, not a source claim** — the source asserts only that *features* are lagged and that the rolling window makes *predictions* out-of-sample (Section 3.3).
4. **The return and factor data behind Tables X-XIII are unnamed.** No stock-return database, no risk-free series, no factor library, no delisting rule. Table XIII's "Excess Return" row is undefined (excess over what), and its Q1−Q5 value is **identical** to the raw "Return" spread (4.240), which the source does not explain.
5. **The spread looks substantially like a characteristics tilt.** From the source's own Tables VII-IX, the least-predictable (winning) quintile is larger, younger, growth-oriented, high-R&D, earnings-surprised, lower-payout — and **higher past-1-month return**, i.e. a *recent-winner* cohort. Long Q1 / short Q5 therefore carries growth-vs-value and short-term-continuation exposure; adding MOM (FF4) already cuts the spread from **4.425 to 3.557**. The source runs **no horse race** against size, value, profitability, investment, momentum, one-month reversal, idiosyncratic volatility, MAX, turnover, illiquidity or attention controls.
6. **Source-internal contradiction, Table XII vs Section 7.1 prose** (frontmatter `contradictions`): the prose says the Correct Predictions portfolio outperforms the Incorrect Predictions portfolio over nearly the whole sample, while Table XII reports 7.981 vs 7.069 the other way round; the same sentence then describes a rising Incorrect-minus-Correct gap, which agrees with the table and contradicts its own first clause.
7. **Source-internal contradiction on the horizon of the headline 424 bp** (frontmatter `contradictions`): "next quarter" (Introduction) vs "annualized over the next year" (Section 7.2) vs "quarterly differential, annualized ×4" (Table XIII note). The economic magnitude depends on which is right by a factor of four in per-period terms.
8. **Source-internal wording error that changes the signal's meaning:** Figure 10's caption describes Q1 as stocks where "funds are least accurate in predicting **these stocks' return directions**." The model never predicts returns — it predicts **share-change directions of a fund's holdings**. Reading the caption literally would produce a different (and much stronger) claim than the method supports.
9. **Table XIII prints no sample period, no observation count, no number of stocks per quintile, and no breakpoint rule.** Every statistic in the headline table is therefore un-auditable with respect to sample scope ⇒ `data gap`.
10. **Leg-level insignificance:** in the FF3/FF4/FF5 rows, no individual quintile is significant at 5% (Q1 t = 1.53 / 1.78 / 0.92), and in the Excess Return row Q4 and Q5 are insignificant (t = 1.59 / 0.86). Only the *spread* is strongly significant, which is possible but makes the result sensitive to the correlation structure between legs — a structure the source never reports.
11. **Fund-level effect is small in absolute terms:** the fund-level Q1−Q5 cumulative spread is **0.79% over four quarters** (Table X), i.e. roughly 20 bp per quarter of *category-relative* performance — a fund-selection signal, not a tradeable stock signal, and one that is measured against peer funds rather than a market or cash benchmark.
12. **Table X "excess" is category-relative, not risk-adjusted:** `CRET` is the fund return minus the average of all funds in the same Morningstar category, so Table X cannot be read as alpha or as excess over cash; the risk-adjusted version (Table XI) exists but the definition of its "Excess Return" row is not restated.
13. **No out-of-sample protocol beyond the model's rolling window.** There is no frozen forward holdout, no post-2023 evaluation, no walk-forward of the *portfolio* rule, and no subperiod table for Table XIII — stability is asserted from Figures 10-11 alone, whose numeric values are not printed.
14. **No multiplicity control anywhere:** Tables IV-XIV (dozens of coefficients across manager, fund, security and return specifications) plus Figures 3-11 are reported with no Bonferroni/FDR procedure, and several results are marginal (Table IX CAPM idio vol t = 1.722; Table VIII Earnings Surprise t = 1.992; Table IX Momentum 1-12 t = 1.341).
15. **Standard-error conventions are heterogeneous and mostly un-HAC'd for the portfolio rows:** two-way clustered at firm and quarter (Tables VII-IX), quarter-year and fund fixed effects (Tables IV-VI), Newey-West only in the Fama-MacBeth table (Table XIV), and **no stated standard-error method for Tables X-XIII** (the tables print t-statistics in parentheses with no method note). Quarterly overlapping cumulative-return horizons in Table X (CRET[0,4] spans four overlapping quarters) are a natural place where uncorrected serial correlation would inflate t-stats.
16. **Precision itself is drifting upward by the source's own account** (Section 5.2, Figure 4): accuracy improves "toward present-day" and "post-2016", which the source attributes partly to factor-investing diffusion. If the score's cross-section is regime-dependent, the trading spread built on it may be too; no regime breakdown of Table XIII is reported.
17. **No code, no data, no replication package, no hyperparameters.** Learning rate, batch size, hidden dimension rule ("scales with the size of the realized cross-section"), sequence sampling, class weighting choice and random seeds are all `not stated in source`; the focal-loss variant is described as "optional" with no statement of which results use it.
18. **Not peer reviewed** (NBER working-paper cover) and the landing page shows no journal publication, no revision and no other versions.
19. **Sample ends in 2023** (fund panel 1990-2023; printed precision panel 1995Q1-2023Q1) while the paper is dated February 2026 ⇒ **no evidence for 2024-2026**.
20. **Publication-bias / researcher-degree-of-freedom concerns:** many specifications, at least three plausible readings of the headline horizon, a swapped-label prose sentence, an undefined "excess" row, and a caption that mis-describes the target variable — collectively a warning sign about the polish of the quantitative reporting, independent of whether the effect is real.
21. **Identifiability of the mechanism is absent:** the paper never tests whether predictable trades are "anticipated and priced"; it documents correlation between a predictability score and returns. No causal design, no instrument, no placebo sort (e.g. sorting on a *shuffled* accuracy score), no random-accuracy null.
22. **No capacity or liquidity analysis:** no participation rate, no ADV constraint, no AUM sensitivity, no market-impact estimate, and no statement that the short leg is borrowable.

## Falsification plan

All thresholds and cutoffs below are **`research-defined falsification threshold`** (chosen by this Scout, not by the source). All operational rules not printed in the source are **`research-proposed`**.

- **F1 — Frozen forward replication (primary test).** Data: quarterly US equity cross-sections covering 2024Q1-2026Q4, never used by the source, with holdings made available only **after** their SEC filing dates. Rule: rebuild the accuracy score with the source's exact target band, window structure and sort, no re-tuning. Metric: annualized Q1−Q5 return and its Newey-West t. **Fail if** the annualized spread ≤ 0, or |t| < 1.96. **Action:** report the hypothesis as not generalising and stop treating it as a candidate.
- **F2 — Filing-lag and accuracy-lag point-in-time audit (decisive for validity).** Re-run F1 twice: (i) lag all holdings by their actual filing dates, (ii) additionally lag the aggregated accuracy score by one full quarter so that only already-scored predictions are used. **Fail if** the spread drops by more than 50%, loses significance (|t| < 1.96), or changes sign under either lag. This is the single most dangerous unaddressed issue in the source.
- **F3 — Cost ladder (decisive for tradability).** Measure one-way quarterly turnover of the equal-weighted Q1/Q5 pair from absolute weight changes (`research-proposed`), then apply 0/1/5/10/20/30 bp one-way plus a commission schedule and a separate stock-loan fee on the short leg. **Fail if** the spread's Sharpe falls by more than 50% at 10 bp one-way, or the mean spread turns negative at or below 10 bp.
- **F4 — Characteristics horse race (decisive for mechanism).** Add controls for size, book-to-market, profitability, investment, one-month reversal, 12-1 momentum, idiosyncratic volatility, MAX, turnover, Amihud illiquidity, earnings surprise, R&D/sales and a headline attention proxy to the cross-sectional regression behind Table XIII. **Fail if** the Q1−Q5 coefficient shrinks by more than 50% and becomes insignificant (|t| < 1.96), i.e. the spread is a characteristics tilt in disguise.
- **F5 — Decisive mechanism ablation.** Compare three rankings on the same data: (i) true model accuracy, (ii) the **naive max-frequency** accuracy (which the source computes but never sorts on), (iii) a **permuted/shuffled accuracy** score preserving the cross-sectional distribution. **Fail if** (i) does not beat (ii) by a statistically significant margin, or if (iii) produces a spread whose |t| is within the 95% band of (i)'s — the latter would show the score's *content* is irrelevant and only its correlation with characteristics matters.
- **F6 — Turnover and capacity audit.** Report average and median one-way quarterly turnover, then cap positions at 10% (and 20%) of average daily dollar volume. **Fail if** the target weights cannot be reached inside the 10% participation cap, or required annual turnover exceeds 500% of the cohort's traded volume.
- **F7 — Placebo / circular shift.** Circularly shift the quarterly accuracy-score panel by k ∈ {1..11} quarters relative to returns, 1000 draws, preserving cross-sectional structure. **Fail if** the genuine alignment's |spread| is not above the 95th percentile of the null.
- **F8 — Subperiod stability.** Require the Q1−Q5 spread to be positive and significant (|t| ≥ 1.96) in at least 3 of 4 subperiods: 1995-2004, 2005-2013, 2014-2019, 2020-2023, **and** separately in 2024-2026. **Fail otherwise.**
- **F9 — Factor-model robustness.** Require the spread to survive at least FF5 **plus** a q-factor and an unconventional-factors specification, and to stay positive after adding the one-month-reversal and MAX factors (neither is in FF3/FF4/FF5). **Fail if** the alpha falls below 100 bp annualized or |t| < 1.96.
- **F10 — Multiplicity control.** Apply Benjamini-Hochberg at q < 0.10 across the paper's headline battery (Tables VII, VIII, IX, X, XI, XII, XIII, XIV). **Fail if** the Table XIII spread and the Table X four-quarter spread do not survive.
- **F11 — Reproducibility gate.** Either obtain the authors' code/seeds or rebuild the LSTM from Section 3.3. **Fail (as "not reproducible") if** Prediction Precision cannot be reproduced within ±0.03 of 0.71 and the naive baseline within ±0.03 of 0.52, or if the Table XIII Q1−Q5 spread cannot be reproduced within ±100 bp annualized on the source's own sample.
- **F12 — Borrow and short-leg gate (`research-proposed`).** Verify that a randomly sampled 500-stock panel of Q5 names is borrowable at a stock-loan fee ≤ 100 bp/yr with ≥ 90% availability. **Fail if** fewer than 80% of Q5 names are borrowable, since the headline spread requires the short leg.
- **F13 — Benchmark-orthogonality audit.** Recompute the fund-level Table X spread against cash and against a market index in addition to the category mean, and state whether the 0.79% four-quarter gap survives. **Fail if** the spread is indistinguishable from zero once category demeaning is replaced by a market benchmark (it would then be a style-timing artifact).
- **F14 — Crypto port gate (`research-proposed`, only if a port is ever attempted).** Require Newey-West |t| ≥ 1.96 on the ported spread **and** a positive net-of-10 bp Sharpe ≥ 0.30 over ≥ 3 years of crypto data, with an explicit point-in-time substitute for fund holdings. **Fail otherwise** and keep portability at `unproven`.

## Crypto portability

**unproven.**

- The source contains **zero crypto evidence**: no crypto instrument, no exchange, no spot/perpetual/futures contract, no funding, no 24/7 session, no on-chain data.
- The signal's entire data dependency is **mutual-fund regulatory holdings filings** (N-30D/N-CSR/N-Q/N-PORT) plus Morningstar/CRSP fund metadata. **Crypto has no equivalent disclosure regime.** Any port would need a substitute cohort whose positions are publicly observable at a known lag (e.g. on-chain fund-like vehicles, DAO treasuries, or exchange-reported aggregate positioning) — that substitution is a **new hypothesis (`research-proposed`)**, not a port of this one.
- Mechanism-level obstacles: the paper's mechanism is about *regulated, quarterly-reporting, benchmark-constrained asset managers* whose trades are templated by style mandates. Crypto market structure has no comparable mandate/reporting cycle, so the "predictable manager" population is undefined; and the accuracy score's determinants (value, payout, book-to-market, earnings surprise, R&D) have no direct crypto counterpart.
- Market-structure differences that would have to be re-derived: 24/7 sessions and exchange-specific candle boundaries; funding and mark/index price; leverage, liquidation and margin; venue fragmentation and per-venue survivorship; borrow availability for the short leg (perp shorts substitute differently from cash equities); custody/withdrawal and stablecoin/quote-currency effects; and the quarterly horizon itself.
- Because neither the mechanism nor the signal has been demonstrated in crypto by the source, portability is **`unproven`**; this is not authorization to trade anything.

## Limitations

- `not independently reproduced` — no number in this record has been reproduced by us.
- `data gap` — transaction costs, commissions, spread, slippage, impact, participation, capacity, borrow, stock-loan fee, financing, leverage, margin, latency, fill model, failure handling, turnover and gross-vs-net labelling: the source models **none** of them (verified by a Methods-level read plus full-text scan of the pinned 79-page PDF), and none may be read as zero.
- `data gap` — the stock/fund **return series, risk-free series and factor library** behind Tables X-XIII are never named; Table XIII's "Excess Return" definition is never given.
- `data gap` — Table XIII prints **no sample period, no observation count, no quintile breadth and no breakpoint rule**; Figures 8-11 print no numeric values in the text layer.
- `underspecified` — the availability timing of the aggregated accuracy score (scoring requires the *next* quarter's share change) and the SEC holdings **filing lag** are never addressed; this is the largest threat to the tradable interpretation and is a `research interpretation`, not a source claim.
- `underspecified` — formation timestamp/timezone, execution price, order type, latency, leg weighting and neutrality convention, tie handling, delisting and corporate-action treatment.
- `underspecified` — the horizon of the headline 424 bp is stated three different ways across the Introduction, Section 7.2 and the Table XIII note (recorded in frontmatter `contradictions`); this record adopts the Table XIII note.
- `underspecified` — LSTM hyperparameters beyond those printed (learning rate, batch size, hidden-dimension rule, seed, and which runs use the optional focal loss).
- `not stated in source` — code availability, data availability, replication package, conflict/funding disclosures, and any journal publication status beyond the NBER working-paper cover.
- Identification is correlational: the source documents that a predictability score co-moves with subsequent returns; it does not identify the "anticipated-and-priced" channel, and its own Tables VII-IX show the score is strongly determined by size, value, payout, R&D, earnings surprise and past returns.
- Sample scope: **top-100 holdings of 1,706 actively managed US equity mutual funds, 1990-2023**, printed precision panel 1995Q1-2023Q1; index, sector, balanced and international funds are excluded, and only fund-held stocks can enter the sort.
- Publication-bias and multiplicity concerns apply: a large battery of tables with no multiplicity correction, inconsistent standard-error conventions (with none stated for the two headline portfolio tables), a swapped-label sentence, and an undefined excess-return row.
- Capacity, borrowability and turnover of the long-short spread are entirely unaddressed.
- This is a research capture of a public working paper. It is not evidence that the spread survives after costs, survives a filing-lag point-in-time rebuild, survives 2024-2026, or exists outside US mutual-fund-held equities.

## Implementation status

`implementation_status: not-implemented`.

Nothing has been implemented in our research stack: no strategy module, no data pipeline, no LSTM training run, no backtest, no paper-trading configuration. No Qlib full-backtest validation, no Paper, no Testnet and no Live verification has occurred, and none is implied by this record. This research capture does not modify any trading engine, does not create a strategy family, and does not authorize execution.

## Adoption boundary

`status: research-only` · `adoption: not-approved` · `approval_scope: research-only`.

The presence of this record in the repository means only that normalized, source-traceable research material has been staged. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. Any later adoption or implementation decision must be explicit, separately reviewed, and based on this record plus current sources. No wording, evidence count, confidence value, or schedule behavior in this record promotes itself.

## Related Wiki records

Pre-write search of Wiki Brain (`kb_search`) for `mutual fund holdings institutional ownership cross-sectional stock returns predictability`, `13F institutional cloning crowding`, `fund manager skill crowding crowded trades underperformance`, and `institutional herding holdings-based signal stock selection` returned **0 hits each**; only the query `machine learning cross-sectional return prediction equity` returned pages. The verified, method-adjacent pages from that query (returned from the vault, so they exist) are:

- [[quant/lstm-learnable-sector-embeddings-cross-sectional-reversal-2026-09-02]] — LSTM cross-sectional equity model; adjacent method family, **different source, different signal, different mechanism**.
- [[quant/statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05]] — deep-learning cross-sectional equity; adjacent method family, **different source and mechanism**.

No Wiki Brain page for a mutual-fund-holdings predictability signal was found, and **no page is fabricated here**. The nearest *repository* records (13F cloning, mutual-fund redemption flow, constrained-ownership share) are named in Provenance's four-axis distinction but have **no verified Wiki Brain page**, so they are not linked as Wiki links.

## Sources

- Lauren Cohen, Yiwen Lu, and Quoc H. Nguyen, **"Mimicking Finance," NBER Working Paper 34849**, DOI **10.3386/w34849**, Issue Date **February 2026** (landing `citation_publication_date` 2026/02/16), JEL C45, C53, C55, C82, G11, G23. Landing: https://www.nber.org/papers/w34849 (fetched 2026-09-27, HTTP 200).
- DOI: https://doi.org/10.3386/w34849
- **Pinned primary-source PDF:** https://www.nber.org/system/files/working_papers/w34849/w34849.pdf — HTTP 200, **6,616,358 bytes, 79 pages, SHA-256 `cec210777463d593fd49c4d469814f7545f25d302d800745df04024b3f661b27`**, downloaded 2026-09-27 and read end to end (cover, Abstract, Sections 1-8, References, Figures 1-11, Tables I-XIV, Appendices A-B). Every quantitative claim in this record is traced to a specific Table/Section/Figure of this PDF.
- NBER landing metadata used for identity only: `citation_title`, three `citation_author` entries in paper order, `citation_doi`, `citation_publication_date`, `citation_technical_report_number`.
- References **cited by the source only** (not opened by this Scout; no numbers imported): Hochreiter and Schmidhuber (1997), *Neural Computation*; Jensen, Kelly and Pedersen (2023), *Journal of Finance* 78(5), 2465-2518 (JKP Global Factor Database); Cremers and Petajisto (2009), *RFS* 22(9), 3329-3365 (Active Share); Gu, Kelly and Xiu (2020, 2021); Chen, Pelger and Zhu (2024), *Management Science* 70(2), 714-750; Kaniel, Lin, Pelger and Van Nieuwerburgh (2023), *JFE* 150(1), 94-138; DeMiguel, Gil-Bazo, Nogales and Santos (2023), *JFE* 150(3), 103737; Freyberger, Neuhierl and Weber (2020), *RFS*; Cohen, Malloy and Nguyen (2020), *JF* 75(3), 1371-1415; Carhart (1997); Wermer (1997); Berk and Van Binsbergen (2015), *JFE*; Autor, Levy and Murname (2003); Acemoglu and Restrepo (2020); Brynjolfsson, Li and Raymond (2025); Office of Financial Research Annual Report 2024 (the "54 trillion-dollar" figure).
- Discovery-only, **not verified and not used for any number**: earlier public author draft dated 2025-11-24 at https://www.rotman.utoronto.ca/media/rotman/Mimicking-Finance---Nov-2025.pdf and mirror https://chelseayao.com/static/file/Cohen_Lu_Nguyen_WP25_Mimicking%20Finance.pdf; IDEAS/RePEc record https://ideas.repec.org/p/nbr/nberwo/34849.html. These were located during discovery and are listed only to show that a pre-NBER draft exists; the NBER February 2026 PDF is the pinned version for this record.
