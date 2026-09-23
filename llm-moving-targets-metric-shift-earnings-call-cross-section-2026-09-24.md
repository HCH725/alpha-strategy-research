---
schema: strategy-research-record-v1
title: "LLM Moving-Targets Metric Shift: Embedding-Ruler Tracking of Year-over-Year Performance-Metric Attrition in Earnings Calls (Long Low-Shift / Short High-Shift, S&P 100)"
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-03-15
sources:
  - https://arxiv.org/abs/2510.03195
  - https://arxiv.org/pdf/2510.03195v5
  - https://doi.org/10.48550/arXiv.2510.03195
  - https://anonymous.4open.science/r/Evolving-Signals-in-Corporate-Disclosures-8775/README.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# LLM Moving-Targets Metric Shift: Embedding-Ruler Tracking of Year-over-Year Performance-Metric Attrition in Earnings Calls (Long Low-Shift / Short High-Shift, S&P 100)

## Provenance

- **Primary source (only source used for every number below):** arXiv `2510.03195`, Chanyeol Choi, Yoon Kim, Yu Yu, Young Cha, V. Zach Golkhou, Igor Halperin, Georgios Papaioannou, Minkyu Kim, Zhangyang Wang, Jihoon Kwon, Minjae Kim, Alejandro Lopez-Lira, and Yongjae Lee, *"From Text to Alpha: Can LLMs Track Evolving Signals in Corporate Disclosures?"* (affiliations on the paper: 1 LinqAlpha, 2 MIT, 3 BlackRock, 4 Blackstone, 5 J.P. Morgan, 6 Fidelity Investments, 7 Qube Research & Technologies, 8 State Street Investment Management, 9 University of Texas at Austin, 10 University of Florida, 11 UNIST; Chanyeol Choi is the corresponding author).
- **Author list exactly as source:** exactly the 13 authors above, in that order — verified identical across (i) the arXiv abs page `<div class="authors">`, (ii) the PDF `/Author` metadata, and (iii) the paper's own byline; no author appears in one place and not the others.
- **Landing / version:** `https://arxiv.org/abs/2510.03195`, **arXiv v5, last revised 15 Mar 2026** (submission history: `[v1] Fri, 3 Oct 2025 17:30:56 UTC`, `[v2] Mon, 6 Oct 2025 02:45:48 UTC`, `[v3] Thu, 4 Dec 2025 21:31:03 UTC`, `[v4] Wed, 11 Mar 2026 06:11:26 UTC`, `[v5] Sun, 15 Mar 2026 03:57:17 UTC`, submitter of record Jihoon Kwon); arXiv comment field = `9 pages`; PDF stamp = `arXiv:2510.03195v5 [cs.CE] 15 Mar 2026`. **No `journal_ref` and no publisher DOI on the abs page** → publication status is **preprint only / not stated in source**; `10.48550/arXiv.2510.03195` is the arXiv auto-DOI and resolves HTTP 200 to the abs page (checked 2026-09-24).
- **Primary-source checksum (performed 2026-09-24):** PDF `https://arxiv.org/pdf/2510.03195v5`, **9 pages, 882,291 bytes, SHA-256 `e19ffc5902bd0a21eee6e68eec920c10a79e360c8636163f5bdfae3f7b5fe355`**; the file was **re-downloaded from the pinned `v5` URL on 2026-09-24 and produced the identical SHA-256** (byte-identical to the copy parsed). Extracted with `pypdf` and **read in full end-to-end** (abstract → §1–§6 Conclusion + Limitations → Tables 1–4 → Figures 1–3 → references → Appendix Table 5 full extraction prompt). Every field below is either quoted from that text with a table/section anchor or explicitly marked as a gap.
- **Sample period:** **January 2010 – December 2024** (§5.1 Data; Table 1 `Sample period Jan. 2010 – Dec. 2024`, `Number of quarters 64`) — consistent in abstract-adjacent setup text and Table 1; no conflicting date appears in v5.
- **Universe:** firms **listed in the S&P 100 index** over that window (§5.1), `Number of firms 100`, `Firm-quarter observations 5,615`, `Returns observations 16,675` (Table 1). The authors state the restriction is theirs, not the baseline's: *"While the original study uses a broader universe, we focus on S&P 100 firms due to computational cost constraints associated with LLM-based extraction"* (§5.1). **No point-in-time index-membership rule, no liquidity/size/exclusion filter, no delisting/survivorship treatment is stated anywhere in the paper** → `data gap` / `underspecified`.
- **Data vendors:** the paper names **no transcript vendor, no returns vendor and no index-constituent source** (`CRSP`/`Compustat`/`I/B/E/S`/`Refinitiv`/`Bloomberg` all absent except the *BloombergGPT* citation) → `not stated in source`. The **linked code snapshot's README** (same primary source's artifact, see below) specifies: HTML earnings-call transcripts keyed by ISIN (`{ISIN}={Quarter}_{Year}_{Company_Name}={Date}.html`, example `US0378331005=Q1_2010_Apple_Inc.=2010-04-20.html`), a pipe-delimited monthly returns file `TRAIN_DATA_FMP_SNP100.csv` (`FMP` = Financial Modeling Prep, optional `FMP_API_KEY` for `src/fmp.py`), and included Kenneth French `F-F_Research_Data_Factors` / `F-F_Research_Data_5_Factors_2x3` TSVs — recorded as **code-repo-specified**, not paper-stated.
- **Transaction-cost treatment (Methods §4, Experiments §5 incl. §5.1 setup, Limitations, and the full extracted text keyword-scanned):** `transaction cost`, `bid-ask`, `slippage`, `commission`, `borrow`, `short sale`, `liquidity`, `capacity`, `participation`, `market impact`, `turnover`, `fees` → **all 0 hits** (the only `cost` strings are "computational cost constraints", "cost savings" in the mechanism narrative, and the words "Sales Fee Cost" inside the Figure 2 illustration; the only `fee` hit is that same figure label) → recorded as **`not stated in source` (`data gap`)**, **not** inferred as zero. The paper's Results are therefore **gross, uncosted portfolio spreads and factor alphas**.
- **Code/provenance caveat:** the paper states *"Codes are available at this GitHub repository"* (§5), but the pinned hyperlink target extracted from the PDF's link annotations is **`https://anonymous.4open.science/r/Evolving-Signals-in-Corporate-Disclosures-8775/README.md`** — an anonymized review snapshot, reachable HTTP 200 when fetched 2026-09-24, **not a github.com URL**. No immutable commit SHA exists for this snapshot → **`data gap` (immutable code provenance unavailable)**; the snapshot README confirms it is an *"Implementation of the Moving Targets methodology from Cohen & Nguyen (2024)"* and documents the pipeline (`MT Score Calculation → Fama-MacBeth regression (4 specifications) → Quintile portfolio backtest with 3-month overlapping holding periods, FF3/FF5 alphas plus Sharpe ratios (Lo 2002)`, `compare` mode running a *Ledoit-Wolf (2008) Sharpe ratio test*).
- **Source-internal model variance (recorded, not reconciled):** §5.1 Implementation Details names the extractor as **Gemini-2.5-Pro** with **text-embedding-3-large** as the ruler; the code README's credential table instead lists `OPENAI_API_KEY` → *"OpenAI API key for GPT-5 extraction + text-embedding-3-large"* with Gemini (`GOOGLE_APPLICATION_CREDENTIALS`) as *optional*. Paper and code therefore describe **different extractor variants (Gemini-2.5-Pro vs GPT-5)** over the same ruler → recorded as printed.
- **Dedup (performed before writing, repository-wide, not just `git log -20`):** identity index over **all 911 tracked `*.md` (plus tracked `coverage_manifest.csv`)** searched with `git grep` for `2510.03195`, `10.48550/arXiv.2510.03195`, `From Text to Alpha`, `moving targets` / `metric shifting`, `Cohen and Nguyen` / `4736129` (the baseline's SSRN id), `LinqAlpha`+title, `Chanyeol`+title, `embedding as ruler`, `text-embedding-3-large`, `Gemini-2.5-Pro`, `Evolving-Signals-in-Corporate-Disclosures`, `llm-moving-targets`, and the filename itself → **0 source-identity hits** (the arXiv ID and title are absent from every tracked file, including the manifest). Author-overlap records exist but cite **different arXiv IDs with materially different mechanisms**: `prediction-market-lead-lag-llm-semantic-risk-filtering-2026-09-03.md` (`arXiv:2602.07048`, prediction-market lead–lag risk filtering) and `llm-compressed-financial-analysis-information-fidelity-arxiv-2606.29251-2026-09-20.md` (`arXiv:2606.29251`, LLM-compression fidelity negative evidence). Nearest domain neighbor `earnings-call-speaker-weighted-sentiment-cross-section-2026-09-23.md` (`arXiv:2604.13260`) shares the earnings-call→cross-section setting but its mechanism (speaker-role-weighted sentiment) and source identity are both different from this record's (year-over-year metric attrition via embedding similarity). ⇒ new source identity **and** materially distinct signal construction → not a duplicate.
- **Source/data as-of:** source-as-of = arXiv v5, 2026-03-15; data-as-of = sample end December 2024 (Table 1).

## Economic mechanism

### Source-reported

The authors' claimed channel (Abstract, §1, §3, §6): managers choose which performance metrics to emphasize each quarter, and when a previously emphasized metric becomes hard to sustain (e.g., stalling sales growth) they *"pivot to emphasizing different metrics, such as cost savings or strategic investments"* — the **moving targets** phenomenon from Cohen and Nguyen (2024, SSRN 4736129), formally the fraction of previously discussed metrics absent in the current period. High metric shifting is interpreted as managers steering attention away from deteriorating goals; the paper argues that traditional spaCy NER + rule-based string matching misses semantically equivalent rewordings and extracts junk tokens (`the %`, `a % increase`), so an **LLM as extractor, embedding as ruler** pipeline (metric extraction by Gemini-2.5-Pro preserving contextual qualifiers such as `"North America cloud revenue"`, cross-quarter cosine-similarity matching by text-embedding-3-large with a piecewise threshold) measures the same construct more faithfully, and this better measurement *"captures return-relevant information that the NER-based approach does not"* (§5.2). The reported result: firms with high target shifting subsequently underperform; the paper's portfolio instruction is to **buy low-metric-shifting firms and sell high-metric-shifting firms** (§5.1, Introduction).

### Research interpretation

Falsifiable mechanism statement: **year-over-year attrition of emphasized performance metrics in quarterly earnings calls is a managed-disclosure behavioral signal — a cross-sectional proxy for deterioration of the narrative being sustained — and its LLM/embedding measurement carries information about next-period abnormal returns beyond size, book-to-market and momentum.** Component roles: *primary signal* = embedding-similarity moving-targets (MT) score comparing quarter `i` vs `i−4`; *measurement layer* = LLM extraction + embedding matching (this paper's contribution vs the NER baseline); *portfolio expression* = long lowest-MT quintile / short highest-MT quintile. The economic link (why metric attrition predicts returns — undisclosed deterioration, guidance-quality decay, or simply narrative instability priced by investors) is **explicitly not investigated by the source** (Limitations: *"we demonstrate predictive gains but do not investigate why"*), so the mechanism remains a hypothesis, not a demonstrated causal channel. The competing measurement explanation — that any gain over NER is an extraction-quality artifact rather than a new economic factor — is live and testable (see Falsification F4/F6).

## Signal

All items below are `source-reported` unless marked otherwise; every operational choice not in the source is labeled `research-proposed`.

- **Formation timestamp:** the MT score is defined per fiscal quarter `i` against the same fiscal quarter one year prior `i−4` (§3, Eq. 1/4). The exact tradability convention — call date/time (BMO vs AMC), transcript publication lag, and the first moment the score is computable — is **not stated** → `data gap` / `underspecified` (the code snapshot's filenames embed a call `Date`, but no lag rule is specified). `research-proposed`: form the score once the transcript is publicly available and enter at the **next trading day's close**.
- **Lookback:** YoY quarter pairing `i` vs `i−4` (inclusive of both endpoints as printed); requires at least four quarters of history (implied by `i−4`); sampled **quarterly** (64 quarters, 2010-01→2024-12, Table 1). Warm-up handling for the first four quarters of the sample is not stated → `data gap`.
- **Signal construction (ruler):** encode each extracted metric with text-embedding-3-large; for each prior-quarter metric take the **maximum** cosine similarity to any current-quarter metric (Eq. 2); apply piecewise-linear `h(·)` mapping (`0` if similarity ≤ α, linear between, `1` if ≥ β, Eq. 3); `MT = 1 − mean(S)` over prior-quarter metrics (Eq. 4), i.e. the fraction of last year's metrics no longer present (higher = more shifting). Baseline (NER) variant: spaCy NER + rule-based string matching with the same `i`/`i−4` definition (§3).
- **Long entry:** quintile sort of firms on their **most recent MT score**; **Q1 = lowest MT** (least shifting) is bought (§5.1: *"we construct a portfolio strategy … buy shares with low metric shifting"*).
- **Short entry:** **Q5 = highest MT** (most shifting) is sold short; headline statistic is the **Q5−Q1 spread** (reported negative ⇒ the implemented direction long-Q1/short-Q5 is profitable when the spread is negative).
- **Portfolio construction:** **5 quintiles, equal-weighted, calendar-time portfolios** (§5.1, Table 3 caption).
- **Holding period / rebalance cadence:** the **paper never states the portfolio frequency or holding period** (Table 3 caption says only "Calendar-time portfolio"; the word `rebalance` does not appear) → `underspecified` in the paper. The **code snapshot's README** specifies *"Quintile portfolios with 3-month overlapping holding periods"* over month-end monthly return data (`TRAIN_DATA_FMP_SNP100.csv`) → recorded as **code-repo-specified (monthly re-sort, 3-month overlapping holdings)**; the Fama–MacBeth test is explicitly monthly (next-month returns, coefficients averaged monthly, §5.1).
- **Exit:** no stop, take-profit or explicit exit rule is given; positions roll with the periodic re-sort → `not stated in source` beyond the holding-period description above. `research-proposed`: time-based exit only (roll at each re-sort), no stop.
- **Parameters (all source-fixed):** similarity thresholds **α = 0.4, β = 0.6**, *"selected from a sweep at 0.2 intervals based on both predictive performance and interpretability"* (§5.1 Implementation Details) — i.e. **tuned on the evaluation sample**; quintile count 5; equal weight; extractor **Gemini-2.5-Pro**; ruler **text-embedding-3-large**; full extraction prompt (section classification into `presentation` vs `analyst_qa`, normalized short noun-phrase targets, dedup rule) in **Appendix Table 5**. The authors state they *"use a single strong model for each component and leave model comparisons to future work."*
- **Reconstruction status:** score definition, thresholds, sort and direction are exact-enough; **tradability timing, rebalance frequency (paper), transcript vendor, membership rule and all cost/execution parameters are not** → the record is **partially underspecified** and must not be presented as a fully reproducible backtest recipe.

## Required data

- **Instrument/universe:** U.S. large-cap equities, **S&P 100 constituents, 100 firms, Jan 2010 – Dec 2024** (§5.1, Table 1). Point-in-time membership, reconstitution and delisting rules **not stated** → `data gap`.
- **Text data:** quarterly earnings-call transcripts with speaker/section structure sufficient to split prepared presentation vs analyst Q&A (Appendix Table 5 prompt assumes an indexed-JSON dialog with speaker labels; code snapshot assumes HTML transcripts keyed by ISIN + call date). **Vendor not stated in the paper** → `not stated in source`; code snapshot implies a self-assembled ISIN-keyed HTML collection.
- **Price/fundamental data:** monthly returns plus `SIZE` (log market cap), `LOG_BM`, `RET_1`, `RET_12`, ISIN mapping (code README `TRAIN_DATA_FMP_SNP100.csv`, FMP implied); Fama–French 3- and 5-factor monthly series (code snapshot includes Kenneth French TSVs). Paper names no vendor → `not stated in source` for the paper itself.
- **Model APIs:** a proprietary LLM extractor (Gemini-2.5-Pro per paper; GPT-5 listed in code README) and an embedding API (text-embedding-3-large) — a **material reproducibility dependency**: model versions are not pinned and are silently mutable by the provider → `underspecified`.
- **Timestamp/timezone:** month-end `DATE` convention in the code file; call timestamps/timezone and transcript availability lag not stated → `data gap`.
- **Missing data:** treatment of quarters with no call, missing transcripts, or missing metrics is not stated → `data gap`; `research-proposed`: drop (no imputation) and report coverage.

## Execution assumptions

- **Source:** the paper specifies **no order type, no signal-to-order delay, no fill model, no fees/spread/slippage, no borrow or short-sale constraint, no participation cap, no capacity, no leverage and no failure handling** — full keyword scan of the Methods/Experiments/Limitations text returned zero hits for every one of these terms → **`not stated in source` (`data gap`)**. Results are gross spreads/alphas. Code snapshot adds evaluation machinery (calendar-time backtest, FF3/FF5 alphas, Sharpe (Lo 2002), Ledoit-Wolf 2008 comparison test) but **no transaction-cost model** either.
- **`research-proposed` execution for any future test (none of this is in the source):** enter at next trading day's close after the score is computable; market orders; monthly re-sort with 3-month overlapping holdings (code-implied); one-way cost stress κ ∈ {10, 20, 30, 50} bps plus an optional 50% ADV participation cap; borrow assumed available on S&P 100 names at a flat fee (**not modeled by the source**); report both gross and net.
- Distinguish clearly: any net-of-cost number produced later would be **our** result, not the source's.

## Evidence

### Source-reported

All figures below are `source-reported`, from arXiv `2510.03195v5`, and **have not been independently reproduced**. Period units for Table 3 are **not stated by the paper** (see gap note after the table).

- **Table 3 (calendar-time quintile portfolios sorted on most recent MT score, equal-weighted; t-statistics in parentheses; `∗ p<0.10, ∗∗ p<0.05, ∗∗∗ p<0.01`):**
  - **(A) NER-based method** — Excess Return: Q1 `0.0156*** (4.38)`, Q2 `0.0131*** (3.85)`, Q3 `0.0111*** (3.19)`, Q4 `0.0132*** (3.99)`, Q5 `0.0135*** (3.94)`, **Q5−Q1 `−0.0031 (−1.48)`**; 3-Factor Alpha: `0.0047*** (3.43)`, `0.0027** (2.12)`, `0.0017 (1.15)`, `0.0040*** (2.88)`, `0.0039** (2.47)`, **spread `−0.0018 (−0.89)`**; 5-Factor Alpha: `0.0045*** (3.26)`, `0.0028** (2.19)`, `0.0016 (1.07)`, `0.0040*** (2.79)`, `0.0041** (2.54)`, **spread `−0.0014 (−0.70)`** → baseline spreads **insignificant**.
  - **(B) LLM-based method** — Excess Return: Q1 `0.0148*** (4.75)`, Q2 `0.0131*** (3.84)`, Q3 `0.0128*** (3.60)`, Q4 `0.0132*** (3.65)`, Q5 `0.0117*** (3.50)`, **Q5−Q1 `−0.0041** (−2.08)`**; 3-Factor Alpha: `0.0056*** (3.89)`, `0.0036*** (2.63)`, `0.0024* (1.89)`, `0.0029* (1.91)`, `0.0018 (1.22)`, **spread `−0.0048** (−2.40)`**; 5-Factor Alpha: `0.0055*** (3.71)`, `0.0038*** (2.78)`, `0.0026** (2.02)`, `0.0032** (2.02)`, `0.0013 (0.87)`, **spread `−0.0052** (−2.55)`**.
  - **§5.2 prose restatement:** *"excess return of −0.41% (t=−2.08), 3-factor alpha of −0.48% (t=−2.40), and 5-factor alpha of −0.52% (t=−2.55), all significant at the 5% level"* — consistent with Table 3(B) (0.0041/0.0048/0.0052 as percentages). **Period-unit gap:** Table 3's caption and the paper never state whether these calendar-time returns are monthly; the word `monthly` appears in the paper only for the Fama–MacBeth coefficient averaging. Monthly cadence is only implied (16,675 return observations ≈ 5,615 firm-quarters × 3 months; code README's month-end data + 3-month overlapping holdings) → **`underspecified`; do not assert a per-period unit the source does not print.**
  - **Table 4 (Fama–MacBeth, next-month returns, controls Log(Size)/Log(BM)/Ret(−1,0)/Ret(−12,−1), N = 5,615):** MT-score coefficient **(A) NER `0.0107 (1.10)`** (positive, insignificant), **(B) LLM `−0.0370 (−0.95)`** (negative, **insignificant at every conventional level**); LLM-column controls: Log(Size) `−0.0072 (−1.37)`, Log(BM) `−0.0037 (−0.71)`, Ret(−1,0) `−0.0501 (−0.81)`, Ret(−12,−1) `0.0006 (0.06)`, Constant `0.1200 (1.53)`; R² `0.3897 / 0.3915`.
  - **Abstract claim:** the method *"achieves more than twice the risk-adjusted alpha"* of the NER baseline — true for the factor-alpha spreads in-sample (`0.0052/0.0014 ≈ 3.7×`, `0.0048/0.0018 ≈ 2.7×`) but **not** for the raw excess-return spread (`0.0041/0.0031 ≈ 1.3×`).
  - **Sample statistics:** Table 1 as quoted in Provenance (64 quarters, 100 firms, 5,615 firm-quarters, 16,675 return observations).
  - **Code-snapshot-reported extras (not in the paper's tables):** the README documents `4 specifications` of Fama–MacBeth, Sharpe ratios (Lo 2002), and a Ledoit-Wolf (2008) two-Sharpe comparison mode; **no numeric results are printed in the README** → no performance figure can be attributed to the code.

### Independently reproduced

not independently reproduced

### Negative evidence

1. **Source-internal contradiction on the cross-sectional test:** the Conclusion claims *"Fama–MacBeth regressions confirm significant predictive power at the 10% level"*, but Table 4(B) shows the LLM MT coefficient at **t = −0.95** — insignificant at 10%, 5% and 1%; the abstract's *"significantly stronger predictive power"* is likewise unsupported by Table 4. The **only** significant evidence in the paper is the Table 3(B) portfolio spread (|t| = 2.08–2.55).
2. **Sign instability of the cross-sectional coefficient:** NER gives `+0.0107`, LLM gives `−0.0370` — the two measurement methods disagree in sign, and neither is significant, so the regression evidence is compatible with no effect (Table 4).
3. **The baseline's economic thesis fails its own test:** the NER-based moving-targets spread is insignificant in all three rows (t = −1.48 / −0.89 / −0.70, Table 3A), so the underlying "metric shifting predicts returns" claim is only detected after this paper re-measures it, in-sample, with tuned thresholds.
4. **In-sample parameter tuning:** α = 0.4 / β = 0.6 were *"selected from a sweep at 0.2 intervals based on … predictive performance"* (§5.1) on the evaluation sample — no holdout or walk-forward selection is reported.
5. **No cost treatment whatsoever:** zero hits for transaction-cost/bid-ask/spread/slippage/commission/borrow/capacity/turnover terms in Methods, Experiments and Limitations → results are gross; a 3-month-overlap long–short quintile strategy on 100 large caps has real (unmodeled) borrow, spread and turnover drag.
6. **Thin statistical object:** 3 spread t-statistics, no multiple-testing correction reported, 136-ish periods at best, single universe, single sample window ending December 2024.
7. **Narrow universe by construction:** S&P 100 only, chosen for computational cost (§5.1, Limitations) — the baseline (Cohen & Nguyen 2024, SSRN 4736129) uses a broader universe; whether the effect exists in mid/small caps (where disclosure-driven mispricing is typically stronger) is untested.
8. **Model dependency and mutation risk:** single proprietary extractor (Gemini-2.5-Pro per paper / GPT-5 per code README — the source itself is inconsistent) plus one embedding model; the authors list model robustness as future work (Limitations). Proprietary model versions are not pinned → today's replication may silently use a different model.
9. **Mechanism untested:** the paper explicitly does not investigate *why* LLM tracking captures return-relevant information (Limitations) — measurement gain vs economic channel remains unresolved.
10. **Data/lineage gaps:** no transcript/returns vendor in the paper, no point-in-time membership, no delisting/survivorship handling, no missing-data rule → `data gap` on several required fields.
11. **Reproducibility gap:** code lives only behind an anonymized `anonymous.4open.science` snapshot with **no immutable commit SHA**, despite the text saying "GitHub repository"; no results are printed in the snapshot README.
12. **Preprint status:** 9-page unrefereed v5 preprint; no journal reference or publisher DOI → claims not peer-reviewed.
13. **External replication status of this specific LLM-embedding construction:** none identified in the reviewed sources; absence is not evidence of no negative result. (The baseline NER construct's wider literature was not re-audited in this run and is not claimed here.)

## Falsification plan

Each threshold below is a `research-defined falsification threshold`; each operational rule not quoted from the source is `research-proposed`.

- **F1 — Cross-sectional significance (repairs the paper's own contradiction):** re-run the Fama–MacBeth test on the reconstruction; **fail** if the MT coefficient is not negative with |t| ≥ 2 (Newey–West, lags ≥ holding period). Source's own Table 4 (t = −0.95) already fails this bar — the record proceeds only on portfolio-spread evidence.
- **F2 — Out-of-sample / walk-forward:** freeze α = 0.4, β = 0.6, models and sort rules, then evaluate on periods/universes never used for tuning (post-2024 data and/or a broader point-in-time universe such as S&P 500). **Fail** if Q5−Q1 (long Q1/short Q5) 5-factor alpha is not negative with |t| ≥ 2 out-of-sample.
- **F3 — Cost stress:** apply κ ∈ {10, 20, 30, 50} bps one-way (`research-proposed`) plus modeled borrow on the short leg to the gross spread with 3-month-overlap turnover. **Fail** if the net 5-factor spread at κ = 20 bps is < 10 bps per reporting period (threshold `research-defined`).
- **F4 — Measurement ablation / placebo:** (a) swap extractor (Gemini-2.5-Pro vs GPT-5 vs an open-weights model) and embedding model; **fail** if the spread sign flips or alpha retention < 50% (`research-defined`); (b) shuffled-label placebo: permute MT scores across firms 500 times; require empirical p < 0.05 (`research-defined`); (c) threshold-perturbation: α, β ∈ {0.3, 0.4, 0.5} × {0.5, 0.6, 0.7}; **fail** if the effect exists only at the published cell (sign of spread unstable across ≥ 1/3 of cells, `research-defined`).
- **F5 — Baseline parity:** out-of-sample, the LLM ruler must beat the NER baseline's spread (|t| difference or paired test, `research-proposed`; Ledoit-Wolf 2008 test is already wired into the code snapshot). **Fail ⇒ drop the LLM layer** (or the mechanism) rather than keep paying for it.
- **F6 — Channel ablation:** compute MT separately on the prepared-presentation section and the analyst-Q&A section (the source's prompt already emits both labels). **Fail** if only one section carries the entire effect and that section's signal does not survive F1–F3 (`research-defined`) — this decides whether the thesis is management steering or a Q&A artifact.
- **F7 — Membership/survivorship audit:** rebuild with point-in-time index membership and delisting returns. **Fail** if the alpha vanishes (`research-defined`: |t| < 2).
- **F8 — Mechanism probe:** test whether high MT scores co-occur with subsequent guidance cuts / analyst forecast revisions in the next two quarters. **Fail ⇒ record stays a pure measurement artifact** with no economic channel (still tradable in principle, but the mechanism claim is withdrawn).
- **Action on failure:** any failed test keeps/strengthens `status: research-only`; no implementation, candidate-pool promotion, or Paper/Testnet/Live step may follow from a failed falsification.

## Crypto portability

**unproven.** The mechanism is rooted in a **mandatory quarterly corporate-disclosure regime** (10-Q/10-K cycle, scheduled earnings calls with prepared remarks + analyst Q&A). Crypto tokens have no equivalent standardized disclosure stream: L1/L2 foundations and issuers publish irregular blog updates and AMAs, with no guaranteed cadence, no `i−4` YoY pairing structure, and no audited metric taxonomy — so the signal's core data dependency (paired quarterly transcripts) does not exist for most crypto assets. Additional porting risks: 24/7 sessions and exchange-specific candle boundaries vs month-end equity data; venue-fragmented and manipulable "disclosure" channels (social posts, governance forums) with no point-in-time integrity; perpetual funding/borrow asymmetries for the short leg; listing survivorship on thin alt markets. The closest testable analog — applying the same pipeline to crypto-exposed U.S. equities (e.g., Coinbase, MicroStrategy-type issuers) or to a hand-built corpus of foundation updates — is a **ported hypothesis, not crypto empirical evidence**, and is not demonstrated by this source (the source contains zero crypto evidence). Crypto portability is not authorization to trade.

## Limitations

- `underspecified`: portfolio reporting frequency/period units (Table 3), tradability timing, transcript vendor, index-membership point-in-time rule, delisting/survivorship, missing-data handling, warm-up.
- `not stated in source`: all transaction-cost, borrow, capacity and execution assumptions; paper's returns-data vendor.
- `data gap`: immutable code provenance (anonymized snapshot, no commit SHA); no results in the code README; model versions not pinned (extractor inconsistent between paper and code).
- `not independently reproduced`: every performance figure in this record is the author's own in-sample result on a 100-firm universe with tuned thresholds and no cost model.
- Sample ends December 2024; preprint only (v5, no journal reference); 9 pages with no appendix robustness tables (appendix = extraction prompt only).
- Incremental-write check: new family (LLM/embedding measurement of moving-targets), new signal construction (embedding ruler vs NER string matching), no adjacent record in this repository or Wiki Brain (see Provenance dedup).

## Implementation status

`implementation_status: not-implemented`. Nothing in this record has been implemented in our research stack: no signal has been computed, no portfolio constructed, no Qlib full backtest, no Paper, Testnet or Live run. The record is a normalized research capture of a third-party preprint plus its anonymized code snapshot (neither executed nor verified by us).

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. No record may promote itself by wording, evidence count, confidence, or schedule behavior.

## Related Wiki records

Queried in Hermes Wiki Brain on 2026-09-24 before writing (only actually-returned pages are linked):

- [[quant/strategy-research-record-spec-v1]] — canonical schema contract this record conforms to (read in full).
- [[quant/earnings-announcement-premium-jump-risk-decay-falsification-2026-09-13]] — adjacent earnings-event risk/decay evidence in equities.
- [[quant/news-event-tag-drift-rumor-resolution-placebo-adjusted-momentum-2026-09-02]] — disclosure/narrative-drift abnormal-return family.
- [[quant/single-name-equity-earnings-iv-crush-bid-ask-falsification-2026-09-13]] — single-name earnings microstructure/cost falsification context.

Wiki Brain searches for `moving targets earnings call metric` and `speaker identity which voices move markets earnings call sentiment` returned **no** record of this paper or of the Cohen–Nguyen baseline → no closer Wiki neighbor exists. In this repository, the nearest domain neighbor is `earnings-call-speaker-weighted-sentiment-cross-section-2026-09-23.md` (different mechanism and source; not a duplicate).

## Sources

- Chanyeol Choi, Yoon Kim, Yu Yu, Young Cha, V. Zach Golkhou, Igor Halperin, Georgios Papaioannou, Minkyu Kim, Zhangyang Wang, Jihoon Kwon, Minjae Kim, Alejandro Lopez-Lira, Yongjae Lee, *"From Text to Alpha: Can LLMs Track Evolving Signals in Corporate Disclosures?"*, arXiv:2510.03195v5 [cs.CE], last revised 15 Mar 2026 (v1 3 Oct 2025) — https://arxiv.org/abs/2510.03195 ; PDF https://arxiv.org/pdf/2510.03195v5 (9 pp., SHA-256 `e19ffc5902bd0a21eee6e68eec920c10a79e360c8636163f5bdfae3f7b5fe355`, verified byte-identical on re-fetch 2026-09-24); auto-DOI https://doi.org/10.48550/arXiv.2510.03195 (HTTP 200, 2026-09-24). Preprint only: no journal reference or publisher DOI stated.
- Code snapshot linked from the paper's §5 PDF hyperlink: https://anonymous.4open.science/r/Evolving-Signals-in-Corporate-Disclosures-8775/README.md (anonymized snapshot "Evolving Signals in Corporate Disclosures", HTTP 200, fetched 2026-09-24; no immutable commit SHA available — `data gap`). Cited in this record only for execution/data-specification details explicitly printed in its README.
- Baseline cited **by** the primary source (not consulted for any number in this record): Lauren Cohen, Quoc Nguyen, *"Moving Targets"*, SSRN 4736129 (2024) — referenced as the NER-based baseline and broader-universe origin (§3, §5.1 of the primary source).
