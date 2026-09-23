---
schema: strategy-research-record-v1
title: "US-equity cyber-risk disclosure premium: doc2vec cosine similarity of 10-K text to MITRE ATT&CK attack descriptions, quarterly value-weighted quintiles, long top-quintile P5 (arXiv 2409.08728)"
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-09-13
sources:
  - "Loïc Maréchal, Nathan Monnet, 'Disentangling the sources of cyber risk premia', arXiv:2409.08728v1 [q-fin.PM, cs.LG], 13 September 2024. https://arxiv.org/abs/2409.08728 (DOI 10.48550/arXiv.2409.08728, resolves 2026-09-23); full-text PDF https://arxiv.org/pdf/2409.08728v1"
  - "MITRE ATT&CK knowledge base (attack matrix used to build the cyber scores) — https://attack.mitre.org"
  - "SEC EDGAR full-text 10-K index archives (firm filing source used by the paper) — https://www.sec.gov/Archives/edgar/full-index/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# US-equity cyber-risk disclosure premium: 10-K text similarity to MITRE ATT&CK attack descriptions → quarterly value-weighted quintile portfolios, long P5

## Provenance

- **Primary source (complete author list, exactly as printed on the PDF title page):** Loïc Maréchal (HEC Lausanne, University of Lausanne, `loic.marechal@unil.ch`); Nathan Monnet (Swiss Finance Institute, École Polytechnique Fédérale de Lausanne — Cyber-Defence Campus, armasuisse S+T, `nathan.monnet@armasuisse.ch`). Title: *"Disentangling the sources of cyber risk premia."*
- **Version / date (primary-source checksum, performed 2026-09-23):** `arXiv:2409.08728v1 [q-fin.PM, cs.LG]`, submitted **2024-09-13 11:30:42 UTC**, v1 = only version (`updated` identical to `published` on the arXiv API record). Stable URL https://arxiv.org/abs/2409.08728 · arXiv-minted DOI `10.48550/arXiv.2409.08728` (verified resolving to the abs page, 2026-09-23) · full-text PDF https://arxiv.org/pdf/2409.08728v1 downloaded for this record: **2,782,600 bytes, 88 pages, SHA-256 `0ef90542c4e2a86620984987e813b5e42ea36c62c732e9740b6e4ebd51ff4dc5`**; the whole PDF text was extracted and read for this record (Methods §3, Results §4, Conclusion §5, all 32 tables + Figures captions).
- **Publication / preprint status:** arXiv preprint only. The arXiv API record carries **no `journal_ref`, no publisher `doi`, no `comment` field** (read 2026-09-23) → peer-review/publication status **not stated in source**. PDF cover footnote: the document "results from a research project funded by the Cyber-Defence Campus, armasuisse Science and Technology, and was initially written as Nathan Monnet's Master thesis" (`source-reported`, recorded as provenance quirk, not repaired).
- **Sample period:** market data and 10-K collection cover **January 2007 – December 2023** for **7,079 US-listed firms** that filed 10-K forms (§3.1), with **64,988 10-K statements** identified (avg. 2.73 per firm, §3.2). **Every reported asset-pricing result covers January 2009 – December 2023** (table captions of Tables 10, 12–15 and Table 17; Table 1 characteristics and Table 3 score statistics are labelled 2009–2023). Both windows are recorded as printed; the paper does not reconcile the 2007 data start with the 2009 estimation start → `underspecified`.
- **Universe:** US common stocks with CRSP/Compustat data downloaded through the Wharton Research Data Services API that have filed 10-K statements with the SEC (§3.1–3.2); industry context given with the 12 Fama–French industries from SIC codes (Fig. 1). Reported portfolios hold **628.48 – 629.67 firms per quintile on average** (Table 10, Panel B). No explicit size/liquidity/exchange filter and no explicit delisting rule is stated → `data gap`.
- **Transaction-cost treatment:** the Methods that govern portfolio construction (§3.1 market data, §3.5.1 univariate sorts, §3.5.2 double sorts, §3.5.3 Fama–MacBeth, §3.6 GRS/Bayesian tests) and all 32 result tables were read for this record; a full-text keyword scan of the 88-page PDF returns **zero occurrences of "transaction cost(s)", "bid-ask", "slippage", "borrow", "short sale", "Amihud/illiquidity", "net of cost"**, and no fee/spread/impact parameter appears anywhere. Recorded as **`not stated in source` (`data gap`)** — the reported returns are not labelled net of cost by the source, and they are **not** assumed to be cost-free by this record.
- **Repository deduplication (2026-09-23, ripgrep across ALL `*.md` records plus `coverage_manifest.csv`, not `git log -20`):** `2409.08728`, `Disentangling the sources of cyber risk premia`, `Celeny`, `MITRE`, `cyber score`, `cyber risk premia`, `Maréchal`, `Monnet` → **zero hits carrying this source identity**. The only incidental matches are a different author's surname (Aloïs Maréchal, Politecnico student author of an unrelated record), the unrelated GitHub user `cybereow`, and an unrelated cyber-loss-citation inside `defi-lending-operational-tail-risk-premium-mispricing-2026-09-02.md`. Wiki Brain `kb_search "cyber risk premia cross-sectional"` → **0 results**, so only the verified specification page is linked below. `git log --oneline -20` reviewed as a convenience glance only; `git pull origin main` run before researching (fast-forward `2a94731 → 5c7cbb4`); tracked files were clean at write time (`git status --porcelain --untracked-files=no`).
- **Material distinction from neighbours (dedup statement):** the pool already holds text/NLP-based equity and crypto factor records (`ai-misinformation-risk-factor-pricing-news-lda-2026-09-11.md` news-LDA risk factor, `supply-chain-network-augmented-llm-text-embeddings-nale-2026-09-04.md` text embeddings, `llm-event-aware-sentiment-factor-contrarian-alpha-2026-09-04.md` sentiment) — those price **text content/sentiment** as behavioural information. This source's mechanism is different: **semantic similarity of statutory disclosure text to a cyber-attack technique taxonomy**, argued to price a **physical/operational risk exposure** (a compensation-for-risk hypothesis), with an in-paper **sentiment-filtered control score that shows no premium** (Table 11). The companion paper the source builds on (Celeny & Maréchal, arXiv:2402.04775, *Cyber risk and the cross-section of stock returns*) is a **different source identity** and is **not captured in this repository**; no number from it is used in this record except where this primary source itself quotes it.

## Economic mechanism

### Source-reported

The authors' claim is a risk-premium claim, not a behavioural-timing claim: a 10-K whose language is semantically close to MITRE ATT&CK's descriptions of cyber-attack tactics/techniques indicates that the firm faces more cyber risk, and "taking additional cyber risk grants additional returns" (§4.4). Their three stated readings are (a) cyber scores load on a priced cyber-risk exposure that standard factor models do not span (Tables 10, 12–15, 17, 23–28); (b) the scores are largely independent of standard financial and non-semantic firm characteristics (§4.3, Tables 4–9, R²-within up to 0.43, and they report the risk-length-table t-statistics improving on Florackis et al. 2023's 40.80/20.59); and (c) the market prices **one aggregate cyber risk** rather than the four sub-types, because portfolio returns built from different cyber scores are statistically indistinguishable (Table 29) and the SolarWinds event study is inconclusive (Tables 30–32, §4.9).

### Research interpretation

Falsifiable restatement: **cross-sectionally, US firms in the top quintile of 10-K→MITRE ATT&CK semantic similarity earn higher subsequent value-weighted returns than bottom-quintile firms, and the spread is not fully explained by market, size, value, investment, profitability and momentum exposures.** Component roles:

```text
Signal: quarterly cross-sectional score = doc2vec cosine similarity of 10-K text to MITRE ATT&CK sub-technique paragraphs (overall score; four clustered sub-scores)
Portfolio: value-weighted quintiles, previous-quarter score, quarterly refresh → long P5 (top 20%) and research-analysed P5−P1 spread
Controls/placebo: cyber sentiment score (risk/uncertainty vocabulary only) — source-reported null premium (Table 11, Table 18)
```

Competing explanations the source does not fully shut down, and which this record keeps alive: (i) the score proxies for intangible-heavy/human-capital-light tech business models (humans-per-capital and risk-length load with |t| ≈ 7–11 in Tables 4–9; FF12 industry composition is not neutralised in the sorts); (ii) ambiguity/lottery preference for hard-to-price operational risk rather than equilibrium compensation; (iii) under-reaction to slowly-moving disclosure text. **Do not assume the spread is an equilibrium premium or that every component is alpha** — the sentiment control null supports score specificity, not tradability.

## Signal

- **Formation timestamp:** firms are classified **each quarter using the most recent cyber score known from the previous quarter** (§3.5.1) — a one-quarter publication lag on the 10-K filing date (the paper does not state whether the score becomes available at filing date, acceptance date, or quarter boundary → `underspecified`).
- **Score construction (`source-reported`):** 10-K HTML from SEC EDGAR archives → BeautifulSoup text extraction → punctuation/number removal, lowercasing, stop-word and stop-word-frequency removal (Celeny & Maréchal 2023 preprocessing code) → sentences merged into paragraphs averaging **≈40 words after preprocessing (640 paragraphs/10-K, 46 words mean, s.d. 2.8, 309 paragraphs s.d.)** → Paragraph Vector doc2vec (Le & Mikolov 2014; **the source reuses the saved doc2vec model of Celeny & Maréchal 2023**, hyperparameters "extensively covered" there → `underspecified` here) → cosine similarity of each 10-K paragraph to each of the **785 MITRE ATT&CK sub-technique descriptions** (mean length 39.7 words) → aggregated per filing. Four **super-tactic** sub-scores come from Louvain clustering of the 785×785 similarity matrix (lower threshold 0.25 → 0, upper 0.85 → 0.5; K-means and spectral clustering checked as alternatives, Fig. 5–8): **Preparation and Reconnaissance; Persistence and Evasion; Credential Movement; Command and Data Manipulation**; plus the **overall score** (all 14 tactics) and a **cyber sentiment score** that keeps only paragraphs whose vocabulary contains "risk"/"uncertainty" terms.
- **Score scale:** cosine similarity, empirically narrow: overall score mean 0.53, s.d. 0.03, min 0.33, max 0.65 (Table 3, 2009–2023); sentiment score mean 0.51, s.d. 0.05, min 0.00, max 0.72.
- **Portfolio rule (`source-reported`):** five quintiles of the score each quarter; **value-weighted using end-of-previous-quarter market capitalisation**; **rebalanced quarterly**; P5 = top 20% by score. Double sorts (Table 16) first form quintiles of market beta / book-to-market / size, then cyber-score quintiles inside each (25 portfolios). Fama–MacBeth (Table 17) uses **20 cyber-score portfolios**, time-series betas on **24-month rolling windows**, monthly cross-sections, Jan 2009–Dec 2023. GRS tests run on 20 portfolios sorted by cyber score, size, book-to-market and market beta (§3.6, Tables 23–28); Bayesian BGRS factor-selection follows Barillas & Shanken (2018) (Figs. 16–21).
- **Entry / exit / holding (`source-reported` for the published sorts, `research-proposed` for anything tradable):** the source reports portfolio average returns with quarterly refresh; it specifies **no order type, no signal-to-order delay, no same-bar/next-bar convention, no stop, no position cap and no explicit long-only vs long-short mandate** — in fact its conclusion states: "a long-short portfolio P5−P1 destroys performance… We recommend that future studies using a similar work frame focus solely on P5 instead of P5−P1, as has been done until now" (§5), which sits in tension with Table 10 reporting a significant positive P5−P1 spread (recorded verbatim as a source-internal inconsistency, not repaired). Operational implementation choices (monthly check instead of quarterly, next-day-at-close entry after score refresh, cash fallback when fewer than N names qualify, industry-neutral breakpoints) are **`research-proposed`**, not from the source.
- **Parameters:** quintile count 5 (fixed, `source-reported`), 20 portfolios for FM/GRS (`source-reported`), 24-month beta window (`source-reported`), score thresholds 0.25/0.85 in the Louvain similarity matrix (`source-reported`). No tuned threshold, stop or sizing parameter is stated by the source; anything Scout-supplied appears only in the falsification plan and is labelled `research-defined`/`research-proposed`.
- **Reproducibility status:** signal is **partially** reconstructable from the paper alone; the frozen doc2vec model, exact cleaning script and clustering implementation live in the companion paper/code → overall signal marked **`underspecified`** for independent reimplementation.

## Required data

- **Instrument / universe:** US-listed operating companies filing SEC 10-K forms; CRSP monthly returns + Compustat fundamentals via WRDS (`source-reported`, §3.1); no crypto, no futures, no ETFs.
- **Venue / market type:** US equity exchanges (CRSP/Compustat consolidated view); spot equity only.
- **Timeframe:** monthly return observations; **quarterly score refresh and portfolio formation**; annual 10-K filing cadence.
- **Fields:** monthly returns, market capitalisation (end of previous quarter for weighting), book-to-market, size, market beta, plus the characteristic set of Tables 1/A1 (ROA, Tobin's Q, intangibles/assets, debt/assets, ROE, price-earnings, profit margin, asset turnover, cash ratio, sales/invested capital, capital ratio, R&D/sales, ROCE, readability, "secret" dummy, risk-length table, volume per capital, humans per capital — winsorised at the 1st/99th percentile by year, Table 1); factor returns Mkt, SMB, HML, UMD/MOM, CMA, RMW and the 1-month T-bill from Kenneth French's data library (`source-reported`, §3.1).
- **Text/data pipeline:** SEC EDGAR 10-K HTML full-index files (CIK-keyed, §3.2), MITRE ATT&CK knowledge base (14 tactics, 785 sub-techniques, §3.3), doc2vec model (DM variant, re-used from the companion paper, §3.4.2).
- **Point-in-time / availability:** score for quarter *t* is built from the most recent 10-K known at quarter *t−1* (§3.5.1) — filing-date availability is **not** explicitly modelled → `data gap`; no revision/vintage handling for restated filings is described → `underspecified`.
- **Missing data:** the pipeline filters out firms without a 10-K and "cleans" the sample (§3.1, Table 1 "after cleaning") but the cleaning rules, suspension/staleness handling and delisting treatment are **not stated** → `data gap`; imputation is not described.
- **Funding / fee / spread needs:** not addressed by the source → `not stated in source` (see Execution assumptions).

## Execution assumptions

- **What the source assumes (`source-reported`):** value-weighting inside each quintile using **end-of-previous-quarter** market cap; quarterly portfolio update with a one-quarter-stale score; monthly return measurement; factor-model controls (CAPM, Carhart/FFC, FF5) for alphas. Reported figures are **average monthly excess returns and model alphas in percent** — the source never labels them gross or net → `not stated in source`.
- **What the source omits (`not stated in source`, read directly in §3.1/§3.5 and all tables):** order type (market/limit), fill model and same-bar/next-bar timing, signal-to-order latency, bid-ask spread, slippage, market impact/participation caps, commissions, **short-sale borrow availability and stock-loan fees for the P1 leg**, margin/leverage, partial fills, capacity/ADV limits, turnover and holding-period statistics, and any delisting/liquidation convention. None may be treated as zero; every one is a `data gap` or `underspecified`.
- **Anything this record adds (all `research-proposed`):** enter at the next session close after the quarterly score refresh; cap participation at a fraction of 20-day ADV; apply a linear cost κ ∈ {10, 20, 30, 50} bps of traded notional; test a long-only P5 tilt versus a cap-weighted benchmark because the source's conclusion itself steers away from the short leg. None of these is source-reported.

## Evidence

### Source-reported

All figures below are third-party claims of Maréchal & Monnet (`arXiv:2409.08728v1`), **value-weighted portfolios, average monthly percent, January 2009 – December 2023**, each traced to its table. None has been independently reproduced.

- **Table 10 (overall cyber score, univariate quintiles):** average excess returns **P1 0.82 / P2 0.93 / P3 1.04 / P4 1.22 / P5 1.44**, all significant at 1%; **P5−P1 0.62 (t 2.05)**. Alphas: CAPM **P5 0.36 (t 2.14, 5%)**, CAPM **P5−P1 0.54 (t 1.49, not significant)**; FFC (Carhart) **P5 0.27 (t 3.04, 1%)**, **P5−P1 0.36 (t 2.20, 5%)**; FF5 **P5 0.29 (t 3.16, 1%)**, **P5−P1 0.44 (t 2.88, 1%)**. Panel B: average firms per portfolio 628.48–629.67; average scores P1 0.49 → P5 0.57; source-printed "Sharp Ratio" P1 0.61, P2 0.69, P3 0.72, P4 0.88, **P5 1.02**, **P5−P1 0.68**.
- **Tables 12–15 (sub-scores, same layout):** Command & data manipulation spread **0.65 (t 1.94)**, FF5 alpha spread **0.49 (t 2.61)**; Credential movement spread **0.61 (t 2.06)**, FF5 alpha spread **0.43 (t 2.74)**; Persistence & evasion spread **0.64 (t 2.01)**, FF5 alpha spread **0.48 (t 2.97)**; Preparation & reconnaissance spread **0.57 (t 1.97)**, FF5 alpha spread **0.38 (t 2.42)** — and its within-quintile sequence 0.86 / 0.85 / 1.15 / 1.11 / 1.43 is **not monotonic** (§4.5 states this explicitly for preparation & reconnaissance).
- **Table 16 (double sorts with beta / book-to-market / size):** increasing average returns across cyber quintiles in nearly every conditioning block; only the **BM Q1** block fails to increase consistently and β-Q3 / Size-Q5 rows differ by 0.01% (source calls the marginal case "possibly spurious"); the `*` marker means non-monotonic with a −0.03% tolerance (Table 16 caption).
- **Table 17 (Fama–MacBeth, 20 VW portfolios, 24-month rolling betas):** cyber coefficient **0.054 (t 1.925, 10%)** in M.1 (cyber only), **0.051 (t 1.807, 10%)** M.2 (+market), **0.051 (t 2.097, 5%)** M.3 (FF3 controls), **0.040 (t 1.547, n.s.)** M.4 (FF5 controls, where the source reports collinearity with CMA). Source's own translation: one standard deviation of the overall score (0.03) ⇒ **0.03 × 0.04 = 0.12% per month** additional return, "compared to Celeny and Maréchal (2023) with 0.18%" (that 0.18% is this paper's quotation of its companion, not an independently read number).
- **Tables 23–28 (GRS) and Figs. 16–21 (Barillas–Shanken BGRS):** reported qualitatively — the probability of jointly-zero alphas and average R² improve when the P5−P1 factor is added to FF5 (except size-sorted portfolios where the base probability is already high), and the top-five factor subsets at the end of the sample include the cyber factor in every case except the sentiment score; the source states cyber-factor importance is **rising over time**. Exact GRS F-stats/posterior probabilities are shown only in figures/tables whose numeric values were not machine-readable in the PDF text layer → `data gap` for precise values; the direction is `source-reported`.
- **Tables 4–9 (score determinants):** within-R² of regressing cyber scores on characteristics ranges roughly **0.16–0.43** (highest: preparation & reconnaissance, Model 1 = 0.4331), with humans-per-capital |t| ≈ 7–11 and risk-length-table |t| ≈ 3–11 → scores are *partially* spanned by characteristics even though the abstract calls them "unrelated to other firms' characteristics" (internal tension, recorded as printed).
- **Table 11 / Table 18 (sentiment control):** sentiment-score spread **0.14 (t 1.21)**, FF5 alpha spread **0.12 (t 1.15)**, non-monotonic 0.99 / 1.08 / 1.24 / 1.15 / 1.14; FM sentiment coefficients 0.003/0.000/0.003/−0.008, all n.s. → the source's own negative control shows **no premium** (§4.4, §4.6, §5).
- **Table 29 (Welch tests across score-built portfolios):** no significant difference between returns of P5/P20 portfolios built from each sub-score and the overall-score portfolio (examples: sentiment p = 0.5405 / 0.2446; persistence-and-evasion p = 0.9058 / 0.9293) → "market perceives a single aggregated risk".
- **Tables 30–32 (SolarWinds, 14 Dec 2020, market-model CAR, betas from prior year):** all insignificant — overall-score P5 CAR[−1,1] **0.206 (t 0.616)**, CAR[−1,3] **0.194 (t 0.748)**; P1 CAR[−1,1] −0.146 (t −0.311); P20 overall CAR[−1,1] 0.078 (t 0.151).

### Independently reproduced

not independently reproduced.

### Negative evidence

Source-supplied, inside `arXiv:2409.08728v1`:

1. **Long-short is thin and model-dependent.** P5−P1 average excess spread is only 0.62%/month (t 2.05) and its **CAPM alpha is insignificant (t 1.49)**; significance appears only after Carhart/FF5 controls (Tables 10).
2. **The conclusion contradicts its own table.** §5 states "a long-short portfolio P5−P1 destroys performance" and recommends studying **P5 alone**, while Table 10 reports a significant positive spread and positive significant spread alphas — recorded verbatim as a source-internal inconsistency.
3. **Fama–MacBeth significance collapses under FF5 controls** (0.040, t 1.547) because of collinearity with CMA (§4.6) — the premium's independence from the investment factor is not established.
4. **The sentiment-filtered score shows no premium at all** (Table 11, Table 18, §4.4/§4.6/§5), and the **preparation-and-reconnaissance** sub-score is non-monotonic (Table 15, §4.5) — only 4 of the 6 score variants behave as claimed.
5. **Event-study null:** SolarWinds CARs are all insignificant (Tables 30–32), and the source explicitly notes this **contrasts with Florackis et al. (2023)**, who find a statistically significant drop in their top cyber portfolio around the same event (§4.9, cited by the source; no number from Florackis is used here).
6. **Scores are partially spanned by characteristics:** within-R² up to 0.433 with strong humans-per-capital / risk-length / "secret" loadings (Tables 4–9) versus the abstract's "unrelated" claim — a proxy-for-composition risk that the univariate sorts (which are not industry-neutral) does not eliminate.
7. **Companion-paper comparison is weaker:** the source itself says its overall-score double-sort trend is stronger than "the trend was less pronounced" in Celeny & Maréchal (2023) (§4.5), i.e. the finding is construction-sensitive.
8. **No cost, turnover or capacity treatment exists in the primary source** (full-text scan, §3.1/§3.5 read): at quarterly rebalance of ~3,145 names per refresh with a one-quarter-stale signal, gross spreads of 0.44–0.62%/month have unknown survival after spreads, borrow fees on the P1 short leg, and small/illiquid-name impact → economics `unproven`.
9. **Publication status unverified:** preprint only, no `journal_ref`/publisher DOI on the arXiv record, Master-thesis origin, two-author working paper with no registered journal version (§Provenance).

External / adjacent (context only, attribution kept separate): the anomaly-decay and text-factor literature cited by this source (Hassan et al. 2019; Antweiler & Frank 2004; Calomiris & Mamaysky 2019; Florackis et al. 2023) is used by the authors as motivation; **no external replication of this specific score was found** in the reviewed sources — absence is not evidence of no negative result.

## Falsification plan

Every threshold below is chosen by this Scout: **`research-defined falsification threshold`** unless marked `source-reported`.

1. **Exact reproduction gate (`research-defined`):** rebuild scores point-in-time from EDGAR (filing-date availability), re-use the frozen doc2vec model, and re-form Jan 2009–Dec 2023 VW quintiles. Failure: P5−P1 average monthly spread differs from **0.62%** by more than ±0.15 pp, or FF5 spread alpha differs from **0.44%** by more than ±0.15 pp → stop, treat the published numbers as non-reproducible, do not proceed.
2. **Frozen out-of-sample extension (`research-defined`):** hold the quintile rule, weighting and quarterly refresh fixed and evaluate **2024-01 → 2026-12** (incomplete windows reported as-is). Failure: FF5 alpha of P5−P1 with |t| **< 2.0** (HAC/Newey–West on monthly returns) or long-only P5 excess over the cap-weighted universe ≤ 0 → reject the premium claim.
3. **Cost stress (`research-defined`):** apply κ ∈ {10, 20, 30, 50} bps of traded notional plus a participation cap of 10% of 20-day ADV, and a +1-session execution delay. Failure: net-of-cost P5−P1 or long-only excess alpha ≤ 0 at κ = 20 bps → reject implementability (the source specifies no costs, so this test is ours).
4. **Characteristic-residualised re-sort (`research-defined`):** orthogonalise the overall score on humans-per-capital, risk-length, "secret", intangibles/assets, size, B/M, beta and FF12 industry dummies (the determinants of Tables 4–9), then re-form quintiles. Failure: monotonicity across quintiles disappears (Spearman ρ of quintile index vs mean return **< 0.9**, i.e. any inversion beyond the source's own −0.03% tolerance) → conclude the raw score was a characteristic/industry proxy, not a cyber premium.
5. **Industry-neutral control (`research-defined`):** re-run Table 10 with FF12-industry-neutral breakpoints. Failure: within-industry P5−P1 |t| **< 2.0** → reject cross-sectional robustness.
6. **Placebo / label shuffle (`research-defined`):** randomly reassign 10-K texts across firms within size decile and year, rebuild scores, re-run 500 times. Failure of the placebo (i.e. the real spread is not in the top 5% of the shuffled distribution, p ≥ 0.05) → reject score-specificity.
7. **Sentiment-control replication (`source-reported` criterion, tested by us):** the sentiment score must remain premium-free (Table 11 spread 0.14, t 1.21). If the sentiment score produces a spread comparable to the overall score, the semantic-specificity channel is falsified.
8. **Sub-period / regime split (`research-defined`):** pre-2015 vs post-2015 and a 2020–2023 stress slice (the source claims rising factor importance in Figs. 16–21 but gives no split statistics). Failure: spread |t| < 2.0 in the post-2015 half → downgrade to historical-sample artefact.
9. **Short-leg feasibility (`research-defined`):** audit stock-loan availability and fees for P1 names by market-cap decile. If the short leg is not locatable/affordable for > 30% of P1 weight, restrict conclusions to the long-only P5 tilt (consistent with the source's own §5 recommendation) and discard long-short claims.
10. **No rescue by retuning (`research-defined`):** quintile count, windows and breakpoints may not be re-chosen after seeing any test above; a failure is recorded as a failure.

## Crypto portability

**`unproven`.** The primary source contains **zero crypto evidence**; its mechanism depends on a statutory annual filing (10-K) that crypto projects do not produce. Nothing in arXiv:2409.08728 supports porting the premium.

Porting would require rebuilding the whole measurement layer, all `research-proposed`: a disclosure corpus (whitepaper, audit reports, post-mortems, team docs, GitHub READMEs/security advisories), a point-in-time filing analogue (publication timestamps on-chain/off-chain), and a crypto-relevant attack taxonomy (the MITRE ATT&CK enterprise/ICS matrices are enterprise-IT, not protocol-exploit, ontologies). Crypto-specific risks that do not exist in the source's sample: 24/7 sessions with no filing calendar, venue fragmentation and cross-exchange price gaps, perp funding on the long leg, stablecoin/quote-currency effects, far smaller free floats and single-name impact, no SEC-style disclosure enforcement (so disclosure quality itself is endogenous), and token-level survivorship/delistions. Under the repository rule, a traditional-asset mechanism may not be labelled `direct` without crypto evidence in the cited source.

## Limitations

- `underspecified`: doc2vec model artefact and hyperparameters (deferred to the companion paper), text-cleaning script, score availability lag convention, sample "cleaning" rules, delisting/suspension handling, whether quintile membership requires any minimum size/liquidity.
- `data gap`: exact GRS F-statistics and BGRS posterior probabilities (figure-only in the PDF text layer), turnover and holding-period statistics, capacity, industry-neutral sorts, sub-period stability statistics, cost/borrow/spread treatment (absent from the source entirely).
- `not stated in source`: publication/peer-review status (arXiv record has no `journal_ref`), execution mechanics of any tradable version, net-of-cost returns.
- `not independently reproduced`: every performance number in this record.
- `unproven`: the equilibrium-risk-premium interpretation; behavioural and characteristic-proxy explanations remain live (see Economic mechanism).
- Identification limits: one sample (US equities, 2009–2023), no out-of-sample country/venue replication, single dominant event study (SolarWinds) that is null, multiple score variants tried (6 reported) with only 4 behaving as claimed → multiplicity is not corrected for in the source.
- Source-quality limits: preprint, Master-thesis origin, funder affiliation (armasuisse Cyber-Defence Campus) tied to the cybersecurity domain under study; no code or data availability statement was found in the PDF (`data gap`).

## Implementation status

`implementation_status: not-implemented`. No score pipeline, portfolio construction, backtest, or execution logic has been built in our research stack: nothing was written to Qlib, the production candidate pool, NautilusTrader, Paper, Testnet, or Live for this record. Wiki Brain was not written by this Scout. All numbers above are third-party, source-reported, and `not independently reproduced`.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record in the staging repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered `/results/_handoff/candidates.json`; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. No stage beyond research capture is implied or connected.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — authoritative strategy-research record specification (read directly for this run; SHA-256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`).
- Wiki Brain search for `cyber risk premia cross-sectional` returned **0 records** (2026-09-23) → no stable Wiki page is known for this mechanism; no further Wiki link is asserted.
- Repository neighbours by mechanism (linked by path, not Wiki pages): `ai-misinformation-risk-factor-pricing-news-lda-2026-09-11.md`, `supply-chain-network-augmented-llm-text-embeddings-nale-2026-09-04.md`, `llm-event-aware-sentiment-factor-contrarian-alpha-2026-09-04.md` (text-derived equity factors — different mechanism: information/sentiment content vs attack-taxonomy semantic similarity); `defi-lending-operational-tail-risk-premium-mispricing-2026-09-02.md` (operational/cyber-loss tail analogy in DeFi — different market and claim).
- **Distinct source identity not captured in this repository** (context only, no numbers used): Celeny & Maréchal, *Cyber risk and the cross-section of stock returns*, arXiv:2402.04775 — the companion whose overall score and doc2vec model this paper reuses.
- Future retrieval routes: search `cyber score`, `MITRE ATT&CK`, `2409.08728`, `Maréchal`, `Monnet`, `Celeny`, `SolarWinds event study`, `10-K textual risk factor`.

## Sources

1. Loïc Maréchal, Nathan Monnet. *"Disentangling the sources of cyber risk premia."* arXiv preprint `arXiv:2409.08728v1 [q-fin.PM, cs.LG]`, submitted 13 September 2024. Stable URL: https://arxiv.org/abs/2409.08728 · arXiv DOI: `10.48550/arXiv.2409.08728` (verified resolving 2026-09-23) · Full-text PDF read for this record: https://arxiv.org/pdf/2409.08728v1 (88 pages, 2,782,600 bytes, SHA-256 `0ef90542c4e2a86620984987e813b5e42ea36c62c732e9740b6e4ebd51ff4dc5`, downloaded 2026-09-23). Publication status: arXiv record carries no `journal_ref` and no publisher DOI (arXiv API read 2026-09-23).
2. Primary-source data/method references used by the paper and required to rebuild the signal (identified from §3, no numbers taken): MITRE ATT&CK knowledge base, https://attack.mitre.org (14 tactics, 785 sub-techniques); SEC EDGAR 10-K full-index archives, https://www.sec.gov/Archives/edgar/full-index/; CRSP / S&P Global Market Intelligence Compustat via WRDS; Kenneth French data library (Mkt, SMB, HML, UMD, CMA, RMW, 1-month T-bill), http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html.
3. Companion/comparison paper named by the primary source (identity only — no independently read number is used): Celeny & Maréchal, *Cyber risk and the cross-section of stock returns*, arXiv:2402.04775; and Florackis et al. (2023) cyber-portfolio event study, cited only as reported inside §4.3/§4.9 of the primary source.
4. Deduplication evidence for this run: ripgrep across all `*.md` records plus `coverage_manifest.csv` in `alpha-strategy-research` for `2409.08728`, `Disentangling the sources of cyber risk premia`, `cyber score`, `cyber risk premia`, `MITRE`, `Celeny`, `Maréchal`, `Monnet` → 0 hits carrying this source identity; `git log --oneline -20` reviewed as a convenience glance only; repository synced with `git pull origin main` before researching (fast-forward `2a94731 → 5c7cbb4`).
