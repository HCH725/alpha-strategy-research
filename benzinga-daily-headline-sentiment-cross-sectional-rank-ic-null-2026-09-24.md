---
schema: strategy-research-record-v1
title: "Benzinga Daily Headline Sentiment Cross-Section: FDR-Controlled Null for Next-Session Rank-IC and Gross Top/Bottom-15% Portfolios across Seven Sentiment Classifiers (S&P 100, 2019)"
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - financial-news-sentiment
  - cross-sectional-equity
  - qlora
  - rank-ic
  - falsification
  - negative-evidence
status: research-only
confidence: low
source_as_of: 2026-08-04
sources:
  - "Fusheng Luo, 'From Financial Sentiment Classification to Return Predictability: A QLoRA Benchmark of Large Language Models', arXiv:2608.04200v1 [q-fin.MF; also cs.LG], submitted 4 Aug 2026 19:57:40 UTC. https://arxiv.org/abs/2608.04200"
  - "https://doi.org/10.48550/arXiv.2608.04200 (arXiv-issued DataCite DOI only; no publisher DOI)"
  - "https://arxiv.org/html/2608.04200v1 (full text, HTTP 200 on 2026-09-24; read directly for this record: §3.2–§3.5 protocol, §4–§5.2 results, §6.1 limitations, Tables 2/3/6/7/8/10/11, Figures 1 and 5)"
  - "https://arxiv.org/pdf/2608.04200v1 (HTTP 200; filename \"2608.04200v1.pdf\"; last-modified 2026-08-06; etag \"CJKWjJ/bipYDEAI=\")"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Benzinga Daily Headline Sentiment Cross-Section: FDR-Controlled Null for Next-Session Rank-IC and Gross Top/Bottom-15% Portfolios across Seven Sentiment Classifiers (S&P 100, 2019)

## Provenance

- **Primary-source author(s), exactly as source:** Fusheng Luo (sole author). Landing page `Authors: Fusheng Luo`; HTML title block shows the same single author with note "This work was conducted while the author was a graduate student at Johns Hopkins University", email `fluo5@alumni.jh.edu`, affiliation Johns Hopkins University, Baltimore, Maryland, USA.
- **Paper title:** *From Financial Sentiment Classification to Return Predictability: A QLoRA Benchmark of Large Language Models*.
- **Version / date:** `arXiv:2608.04200v1 [q-fin.MF] 04 Aug 2026` (PDF dateline and HTML footer, read directly); landing submission history `[v1] Tue, 4 Aug 2026 19:57:40 UTC (132 KB)`. **Only version:** `https://arxiv.org/html/2608.04200v2` tested → HTTP **404**; v1 HTML → HTTP 200.
- **Publication status:** **preprint only.** Landing `Comments: "Waiting to submit to a conference (ICAIF)"`; `Journal-ref:` empty; no publisher DOI (only the arXiv-issued DataCite DOI `10.48550/arXiv.2608.04200`). License on the HTML full text: **CC BY-NC-SA 4.0**.
- **Primary-source inspection for this record:** the arXiv v1 HTML full text was fetched and read directly (not a secondary summary). Verified against the primary source: author list, version/date, downstream sample window and universe (§3.5.1), timing/return alignment (§3.5.2), rank-IC inference (§3.5.3), portfolio construction and the explicit cost exclusion (§3.5.4), every performance number below with its Table/§ anchor, and the seven-item limitations list (§6.1).
- **Repository deduplication audit (2026-09-24):** ripgrep `--hidden` across the **entire repository** — **2,490 `*.md` files** repo-wide including `.mimo-worktrees/`, `.agents/`, `.hermes/`, plus `coverage_manifest.csv` (5,807 data rows) — for `2608.04200`, `10.48550/arXiv.2608.04200`, `arxiv.org/abs/2608.04200`, the exact title fragment `From Financial Sentiment Classification to Return Predictability`, `QLoRA Benchmark`, `Fusheng Luo`, `alumni.jh.edu`, `Benzinga`, `ICAIF` → **0 hits for every source-identity token of this paper** (the only file matching any token is this newly written record itself; the `ICAIF` hits belong to unrelated papers: ISEPT pair trading, FinDPO, analyst networks, FX graph learning, regret-driven portfolios, volatility-drag, factor-augmented volatility, correlation clustering, CVaR Q-learning, ensemble RL trading).
- **Material-distinctness statement (same broad family, independent record):** this repository already holds news/sentiment cross-sectional records with **positive** results from **different source identities**, e.g. `llm-news-probing-excess-return-sentiment-timing-2026-09-06.md` (Kirtac & Germano, *Sentiment trading with large language models*, FRL 2024, DOI `10.1016/j.frl.2024.105227`, arXiv `2412.19245`), `llm-event-aware-sentiment-factor-contrarian-alpha-2026-09-04.md`, `hybrid-xgboost-finbert-regime-adaptive-equity-2026-09-04.md`, `tda-persistent-homology-finbert-sentiment-portfolio-optimization-2026-09-02.md`. This record is independent under the dedup contract because it differs in **source identity** (arXiv `2608.04200`, sole author Luo — no overlap) **and** in material dimensions: (i) **signal construction** — scores are trained on *human sentiment labels* (label-supervised), not probed on realised returns as in Kirtac & Germano; (ii) **timing** — calendar-date aggregation with **next-session open entry**, versus intraday release-synchronised entry; (iii) **evidence class** — a **multiple-testing-controlled multi-classifier null after Newey–West + Benjamini–Hochberg FDR correction**, i.e. new falsification/negative evidence that no existing record documents for this family. It is recorded precisely because it is a rigorous null, not as a third positive sentiment record.
- No code, model-checkpoint, or data repository link appears anywhere in the primary source (only arXiv boilerplate "Report GitHub Issue"); independent reproduction therefore needs the public Benzinga analyst-ratings headlines, a fixed 2019 S&P 100 constituent list, adjusted OHLC, and re-implemented pipelines — **data gap**, not inferred to be available.

## Economic mechanism

### Source-reported

The paper separates two questions that the literature routinely conflates: whether a model reproduces human sentiment labels (Experiment 1) and whether its scores rank subsequent stock returns (Experiment 2). Its stated working mechanism is that news tone carries forward-looking information that context-free classifiers compress away, so a continuous score `s = p_pos − p_neg` aggregated per stock-date should show *some* immediate cross-sectional relation to next-session returns, followed by rapid decay as prices absorb the information. The author's own reading of the results (§5.2.1, §6) is the weaker version: any effect is small, concentrated in the first trading session, and statistically inconclusive; the observed multi-day long-only profitability is attributed to positive market exposure in the 2019 sample rather than sentiment alpha; and a core reason offered for the gap is **objective mismatch** — the classifiers were optimised to reproduce human annotations, not abnormal returns (§6.1, fifth limitation).

### Research interpretation

Falsifiable hypothesis H: *among S&P 100 names with fresh Benzinga headlines, the cross-section of daily mean headline-polarity scores has non-zero predictive content for next-session (open→close) returns at horizons 1/2/3/5 trading days.* Component roles:

```text
Regime: none (unconditional; 2019 only, source-reported)
Signal: label-trained sentiment score, stock-date mean (FinBERT, Financial-RoBERTa,
        TF-IDF Naive Bayes, Qwen2.5-7B + QLoRA, Qwen2.5-7B + QLoRA weighted,
        LLaMA3-8B + QLoRA, Mistral-7B + QLoRA — 7 downstream models, source-reported)
Confirmation: none — no vol, beta, liquidity or news-volume filter in the source
Risk / exit: horizon exit only (close of h-th session); no stop, no sizing rule beyond
             equal weights within legs (source-reported)
```

The paper's Experiment 2 functions as a **falsification attempt on its own hypothesis family**, and the recorded outcome is a null (see Negative evidence). Research interpretation: the result weakens *label-trained daily headline sentiment as a next-session cross-sectional signal in US large caps*, but does **not** generalise to (a) intraday horizons (untested — source lacks intraday timestamps), (b) return-supervised probing (untested head-to-head here), (c) other regimes/years, or (d) crypto. Whether the null reflects a genuinely absent effect or the source's timing/power limitations is an open question, addressed by F1/F5/F6 below.

## Signal

All items below are **source-reported** unless marked `research-proposed` or `underspecified`.

- **Score formation:** for headline `n` and model `m`, `s_{n,m} = p_pos − p_neg ∈ [−1,1]` (Eq. 3, §3.5.1); neutral contributes 0. Inference runs once per unique URL (10,637 unique news_ids), then predictions are mapped back to all 13,115 headline–stock associations.
- **Lookback:** none at signal time — the score uses only same-calendar-day headlines. Historical data enters only via Experiment 1 training (five labelled sentiment corpora, §3.2) and frozen checkpoints.
- **Stock-date aggregation:** `s̄_{i,d,m}` = mean of headline scores for stock `i` on date `d` (Eq. 4, §3.5.2). Stocks without fresh news on date `d` are **excluded from the cross-section** (not given a tied zero signal).
- **Formation timestamp / tradability:** intraday publication times are unavailable for the full sample (source-stated), so every calendar-date signal is conservatively mapped to the **first trading session strictly after `d`**; entry at the **adjusted open of session `t`** (§3.5.2). Timezone of "calendar date" not stated → `data gap`.
- **Return alignment:** `R^(h)_{i,t} = P^close_{i,t+h−1} / P^open_{i,t} − 1` for `h ∈ {1,2,3,5}` (Eq. 5) — 1-day is open→close of the entry session; longer horizons run from the same entry open through the close of the `h`-th session.
- **Cross-sectional test:** daily Spearman rank IC between `s̄` and `R^(h)` (Eq. 6); reported IC = time-series mean of daily ICs; annualised `ICIR = mean/σ × √252` (Eq. 7); Newey–West HAC standard errors with horizon-dependent lags; Benjamini–Hochberg FDR applied jointly to the 28 model×horizon tests (§3.5.3).
- **Portfolio rule:** eligible stocks ranked per model per entry date; most-positive **15%** = long set, most-negative **15%** = short set; equal weights within each leg, unit gross per leg; long–short = +0.5 long / −0.5 short (net 0, gross 1) (Eq. 8, §3.5.4).
- **Holding / overlap:** a new cohort forms every entry session; `h=1` cohorts are held entry-open → same-session close; for `h>1` each cohort is held `h` sessions and receives `1/h` of portfolio capital, so up to `h` cohorts overlap (§3.5.4). No stop, no take-profit, no early exit, no re-entry rule beyond per-session re-formation.
- **Parameters:** tail fraction 15% (fixed, source); horizons {1,2,3,5} (source); equal weights (source). No tuned threshold on the score is specified — **any deployment threshold, minimum score magnitude, minimum news count per stock-day, or position cap is `research-proposed`** and is absent from the source.
- **Reproducibility status:** the *diagnostic* protocol is reconstructable from §3.5 in full; the *trained weights* are not (no checkpoints, prompts, or training scripts released → `data gap`), so exact score reproduction is `underspecified`.

## Required data

- **Universe:** fixed **S&P 100 constituents as of 1 January 2019** (point-in-time snapshot, source-reported §3.5.1); usable Benzinga headlines exist for only **72 of the 100** constituents (§6.1). Intra-year index reconstitution / membership changes during 2019 are not addressed anywhere → `data gap`.
- **News data:** Benzinga analyst-ratings dataset, headline/title text only (separate partner-headlines file excluded), sample 2019-01-01 → 2019-12-31, **253 calendar dates**, 10,637 unique headline URLs, 13,115 headline–stock observations (§3.5.1). Publication timestamps unavailable → `data gap`.
- **Prices:** adjusted open and close per session (Eq. 5). **Data vendor is never stated** anywhere in the primary source (no CRSP/Compustat/Yahoo/Bloomberg/Stooq mention outside a BloombergGPT citation) → `data gap`.
- **Model assets:** TF-IDF + Multinomial Naive Bayes fit on the Experiment 1 training split; off-the-shelf FinBERT and Financial-RoBERTa sentiment checkpoints (no adaptation to the consolidated split, §3.3); QLoRA-adapted Qwen2.5-7B-Instruct / LLaMA3-8B-Instruct / Mistral-7B-Instruct (configuration Tables 4 and 5: unified QLoRA setup, seed 42 for data splits). Exact checkpoint repository identifiers not given → `data gap`.
- **Experiment 1 benchmark (training side):** 33,549 observations harmonised to `y ∈ {−1,0,+1}` from Financial PhraseBank, FOMC corpus, SEntFiN 1.0, Twitter Financial News Sentiment, and NASDAQ financial news; FiQA deliberately excluded because its continuous scores would require researcher-chosen cutoffs (§3.2.1). Stratified split seed 42 → train 25,664 / validation 2,852 / test 5,033 (76.5% / 8.5% / 15.0%, Table 2).
- **Point-in-time / contamination:** models were released **after** the 2019 evaluation window; the paper explicitly flags temporal pretraining contamination as possible and not excludable (§6.1, second limitation) → recorded as source-reported limitation, not resolved.
- **Missing data:** stocks with no fresh news are dropped from that day's cross-section; no imputation (source-reported). Daily cross-sections can be very small on sparse days (§6.1) → power `data gap`.
- **Not required by the source:** order-book, funding, borrow, options, on-chain fields. Short-leg borrow availability/cost is assumed away (see Execution assumptions).

## Execution assumptions

Source-reported:

- **Signal-to-order timing:** calendar-date signal → entry at the adjusted open of the first session strictly after that date (conservative, avoids same-day pre-headline price moves; may miss intraday price discovery — §3.5.2, §6.1 third limitation).
- **Order type / fill model / latency / partial fills:** **not stated in source** → `data gap` (no market-vs-limit assumption, no fill model, no latency or participation-cap discussion anywhere in §3 or §5).
- **Costs:** explicitly and repeatedly **excluded** — "Commissions, bid–ask spreads, market impact, slippage, and stock-borrow fees are excluded, so the portfolios are signal diagnostics rather than estimates of net implementable performance" (§3.5.4); restated as the sixth limitation: results are **gross**, and the paper itself calls this a "high-turnover news-based strategy" for which those frictions matter (§6.1). **Therefore no figure in this record is net-of-cost; no cost is inferred to be zero — the source simply does not model costs.**
- **Turnover:** **not reported anywhere** in the primary source (the word appears only qualitatively in §6.1) → `data gap`; with a fresh cohort every session and 15% tails, turnover is structurally high but unquantified.
- **Neutralisation:** no market-beta, industry, size or momentum neutralisation (§6.1 sixth limitation); long-only legs in particular carry 2019 bull-market exposure.
- **Leverage / margin / shorting:** long–short is net-0 / gross-1 with no leverage stated; the short leg is assumed executable on S&P 100 names with **no borrow cost or availability model** → `data gap`.
- **Capacity / impact:** not addressed → `data gap`.

Research assumptions adopted for this record: **none.** No cost, fill, or sizing assumption has been invented here; any future reproduction must add them and label them `research-proposed`.

## Evidence

### Source-reported

All figures below are third-party claims from `arXiv:2608.04200v1`, read from the primary source, **gross of costs**, on a **single calendar year (2019)** in **US large-cap equity** (not crypto). Table/section anchors are given for every number.

- **Classification side (Experiment 1, Table 6, test N=5,033):** Mistral-7B + QLoRA accuracy **0.8840**, macro-F1 **0.8771**; LLaMA3-8B + QLoRA **0.8814 / 0.8753**; Qwen2.5-7B + QLoRA **0.8683 / 0.8615**; Qwen2.5 + QLoRA weighted CE **0.8667 / 0.8595**; Qwen2.5 zero-shot **0.7280 / 0.7274**; TF-IDF + Naïve Bayes **0.6976 / 0.6334**; FinBERT (off-the-shelf) **0.6930 / 0.6753**; Financial-RoBERTa (off-the-shelf) **0.6622 / 0.6679**. Table 8: QLoRA raises Qwen2.5 macro-F1 **0.7274 → 0.8615**; conclusion §6 states the **+13.41 percentage-point** gain (self-checked: 86.15 − 72.74 = 13.41 ✓). Class-weighted loss does **not** help (0.8615 → 0.8595, §4.3/Table 8).
- **Cross-sectional predictability (Table 10 and §5.2.1):** one-day mean rank IC — Naïve Bayes **0.0141**, FinBERT **0.0143** (largest), Financial-RoBERTa **0.0141**, Qwen2.5 QLoRA **0.0083**, Qwen2.5 QLoRA weighted **0.0083**, LLaMA3 QLoRA **0.0013**, Mistral QLoRA **0.0085**; **every model's two-day IC is negative**, most are near-zero or negative at three days, **all seven are negative at five days**. Largest one-day annualised ICIR: Financial-RoBERTa **1.015**, FinBERT **0.972**, Naïve Bayes **0.951** (§5.2.1). **None of the 28 model×horizon tests is significant after Newey–West + Benjamini–Hochberg FDR: minimum adjusted q = 0.9622**; the smallest unadjusted NW p is **0.0397** (Financial-RoBERTa, two-day) and it does not survive correction (§5.2.1, Figure 5 caption).
- **Gross long–short total return by horizon (Table 10):** 1d — NB **7.47%**, FinBERT **12.96%**, FR **3.17%**, Qwen **−2.35%**, Qwen-w **−0.03%**, LLaMA3 **1.69%**, Mistral **2.69%**; 2d — **−17.01% / −3.07% / −14.76% / −20.34% / −19.87% / −5.09% / −8.66%**; 3d — **−13.31% / 5.32% / −7.36% / −16.07% / −15.70% / −3.61% / −6.57%**; 5d — **−11.96% / 4.34% / −3.20% / −5.43% / −4.76% / 0.98% / −1.51%**.
- **One-day leg-level gross performance (Table 11: long-only return/Sharpe, short-only return/Sharpe, long–short return/Sharpe, long–short MaxDD):** NB **13.38%/0.73, −0.83%/0.13, 7.47%/0.54, −12.13%**; FinBERT **4.05%/0.31, 19.73%/0.96, 12.96%/1.11, −6.37%**; Financial-RoBERTa **15.32%/1.01, −9.05%/−0.37, 3.17%/0.33, −12.52%**; Qwen2.5 QLoRA **−11.24%/−0.59, 5.10%/0.34, −2.35%/−0.14, −12.42%**; Qwen2.5 QLoRA weighted **−8.92%/−0.44, 7.38%/0.45, −0.03%/0.05, −10.94%**; LLaMA3 QLoRA **6.52%/0.45, −5.05%/−0.15, 1.69%/0.20, −11.46%**; Mistral QLoRA **2.74%/0.23, 0.25%/0.11, 2.69%/0.27, −12.79%**. Cross-check performed this run: the seven 1d long–short returns in Table 10 equal the Table 11 long–short column exactly ✓.
- **Return decomposition (§5.2.2):** at 3d/5d the FinBERT **long-only** legs return **39.64% / 33.89%** with Sharpe **2.29 / 2.25**, while the corresponding **short-only** legs lose **22.15% / 20.15%**; the paper attributes this asymmetry to positive market exposure in the 2019 sample rather than cross-sectional sentiment alpha. FinBERT's 1d long–short edge is described as driven mainly by the short leg with a **cohort win rate below 50%** (§5.2.2) and as possibly influenced by a limited number of large observations (§6).
- **Paper's own bottom line (Abstract, §6):** QLoRA is effective for sentiment adaptation, but there is "a clear gap between classification accuracy and tradable cross-sectional signals"; the design does not find statistically robust evidence that daily sentiment signals predict subsequent stock returns.

### Independently reproduced

not independently reproduced

Provenance checks performed this run (these are source-verification steps, **not** a reproduction of the results): landing page + v1 HTML full text read directly; author list, v1 date and single-version status confirmed (v2 → 404); PDF headers fetched (HTTP 200, `2608.04200v1.pdf`, last-modified 2026-08-06); all quoted numbers located in Tables 6/8/10/11 and §5.2.1/§5.2.2 with row/column identity checked; arithmetic self-checks (Table 10 ↔ Table 11 long–short equality; +13.41pp macro-F1 gain); repo-wide source-identity dedup (0 hits). No IC, portfolio, or model was recomputed by us.

### Negative evidence

1. **The headline test is null:** none of 28 model×horizon rank-IC tests survives Newey–West + BH-FDR; minimum adjusted q = 0.9622 (§5.2.1) — i.e. not even marginal after multiple-testing control.
2. **Sign structure is hostile beyond one day:** all seven two-day ICs negative, all seven five-day ICs negative, and gross long–short returns negative for **7 of 7** models at 2d, **6 of 7** at 3d and **5 of 7** at 5d (Table 10).
3. **Classification quality does not transfer to economics:** the QLoRA models top Experiment 1 (macro-F1 0.86–0.88) yet FinBERT (macro-F1 0.6753) has the best 1d IC and long–short return (Table 6 vs Tables 10/11) — a direct dissociation the paper itself emphasises (§6).
4. **Multi-day long-only profits are beta, not alpha:** 3d/5d long-only Sharpe 2.29/2.25 with short legs losing ~20% in a bull year, while ICs at those horizons are zero or negative (§5.2.2).
5. **The one "good" result is fragile:** FinBERT's 1d long–short 12.96% / Sharpe 1.11 is **gross**, statistically unsupported by its IC, concentrated in the short leg with cohort win rate <50%, and flagged by the author as possibly driven by a few large observations (§5.2.2, §6).
6. **Zero cost model on an explicitly "high-turnover" daily strategy:** commissions, spread, impact, slippage and borrow all excluded (§3.5.4, §6.1 sixth limitation); turnover never quantified (`data gap`).
7. **No factor neutralisation:** beta/industry/size/momentum exposures uncontrolled (§6.1) — long-only and long–short legs may both retain systematic exposure.
8. **Power and coverage limits:** only 72/100 universe names have headlines, coverage is heavily uneven, and some daily cross-sections are small (§6.1 first limitation) — a null under low power is weaker evidence than a null at full coverage.
9. **Single regime:** one pre-COVID calendar year (2019) on a fixed large-cap universe; no bear, no high-volatility, no crisis window (§6.1 first limitation).
10. **Temporal contamination risk:** models post-date the 2019 sample; headline text may sit in pretraining corpora (§6.1 second limitation) — this biases *toward* finding signal, yet the result is still null, which arguably strengthens the null.
11. **Timing mismatch:** calendar-date aggregation + next-session open entry likely misses the minutes-to-hours window in which large caps price in news (§6.1 third and sixth limitations) — the true effect, if any, may be intraday and untested.
12. **Objective mismatch (source's own explanation):** models trained on human labels, not returns (§6.1 fifth limitation) — leaves open the return-supervised alternative, which is tested elsewhere with *positive* results (`llm-news-probing-excess-return-sentiment-timing-2026-09-06.md`, Kirtac & Germano 2024 — different source, different supervision and timing). The head-to-head comparison does not exist yet.
13. **No code or checkpoints released:** independent reproduction of the exact scores is blocked today (`data gap`).

Absence of further negative results in the reviewed sources is not evidence that none exist.

## Falsification plan

Every threshold below is `research-defined falsification threshold` (Scout-chosen; the source declares none); every operational choice not present in the source is `research-proposed`.

- **F1 — Replication across regimes (`research-defined`):** re-run the exact §3.5 protocol (same score, same timing, same 15% tails) on ≥5 calendar years including ≥1 bear and ≥1 high-volatility year, universe = point-in-time S&P 100 with full headline coverage. **Failure rule:** the hypothesis "daily label-trained headline sentiment has next-session cross-sectional content" is rejected if no model attains BH-FDR-adjusted q < 0.05 on mean rank IC in at least 2 of the years, **or** the cross-model median annual mean rank IC ≤ 0. Action: keep the family marked unproven and do not promote it into the production candidate pool (Intake decides).
- **F2 — Cost erasure (`research-defined`, cost numbers `research-proposed`):** apply 5 bp commission + 5 bp half-spread per side plus a `research-proposed` 5 bp borrow adder on the short leg (source models zero of these). **Failure rule:** best-model 1d long–short is net ≤ 0, or net annualised Sharpe < 0.30, in ≥4 of 5 years → cost-erased, reject tradability even if F1 passes.
- **F3 — Neutralisation ablation (`research-defined`):** recompute 1d legs on returns residualised for beta, industry, size and momentum (`research-proposed` controls; source uses raw returns). **Failure rule:** long–short Sharpe falls by ≥50% from the source-reported gross 1.11 → the reported edge is exposure, not sentiment.
- **F4 — Supervision ablation (`research-defined`):** train a return-supervised probe (label = next-session market-adjusted excess-return sign, `research-proposed`) on the identical sample and timing, and compare against the label-trained score. **Failure rule:** if the return-supervised probe is *also* FDR-null on this sample/timing, the source's "objective mismatch" rescue explanation is itself rejected → mechanism (not just training target) is falsified at daily-next-session granularity.
- **F5 — Timing ablation (`research-defined`, requires timestamped feed):** re-run with entry at the first trade strictly after each headline's publication timestamp over 5min/30min/1h/4h horizons (`research-proposed`; the source lacks intraday timestamps). **Failure rule:** intraday horizons also FDR-null → the "already priced by next open" explanation is rejected and the diffusion mechanism itself fails for this signal family.
- **F6 — Power/coverage check (`research-defined`):** expand to full-coverage universe (all S&P 100 names, all headlines, multi-year) and confirm daily cross-sections of ≥30 names on ≥90% of sessions. If the null persists at this power, it upgrades from "inconclusive" to "falsified at daily frequency".
- **F7 — Placebo (`research-defined`):** date-shuffle headline scores within model; the placebo |mean IC| must be within ±0.005 of the real signal's mean IC distribution for the test harness to be considered non-spurious (threshold `research-defined`), and any real-signal IC indistinguishable from placebo counts as null.
- **Action on failure:** record stays `research-only`, `not-implemented`, `not-approved`; no candidate-pool promotion, no implementation.

## Crypto portability

**unproven.** The source contains **zero** crypto evidence: universe is US large-cap equity (S&P 100), venue not even named, and all reported results are 2019 equity returns.

Porting considerations (all `research-proposed` if adopted):

- **What could improve:** crypto venues publish timestamped headlines/announcements continuously, so the source's biggest flaw (no intraday timestamps → next-session entry) is fixable; 24/7 trading removes the "wait until next open" delay that likely destroys the signal in equities.
- **What breaks:** crypto news-to-price absorption is far faster and venue-fragmented (Benzinga-style single-feed coverage does not exist; Telegram/X/on-chain feeds dominate); headline→ticker mapping is ambiguous for the ~50 liquid names that a 15%-tail long–short would need; shorting requires perpetuals or borrow with funding/borrow costs the source never models; wash-traded and thin books distort open prices used for entry; stablecoin/quote-currency effects and cross-exchange price dispersion add basis noise the equity protocol ignores.
- **Evidence discipline:** a null in 2019 US equities does not transfer to crypto in either direction; nothing here may be cited as crypto evidence, and the record must not be used to justify crypto implementation.

## Limitations

- `not independently reproduced` — every performance figure is source-reported and unverified by us.
- `confidence: low` refers to **research-interpretation confidence only** (sole-author, not-yet-submitted preprint; single 2019 window; acknowledged pretraining contamination; FDR-null result with low power), **not** to profitability and not to any authorization to trade.
- `data gap`: market-data vendor; intraday publication timestamps; turnover magnitude; order type, fill model, latency, capacity; borrow availability/cost; index reconstitution handling within 2019; exact model checkpoint identifiers; any released code (none exists).
- `underspecified`: deployment threshold/minimum news count/position caps (absent from source); timezone of the "calendar date" convention; tie-handling in the 15% tail ranking; per-day cross-section size distribution.
- `unproven`: the mechanism at intraday horizons, under return-supervised targets, in other regimes, and in crypto.
- **Incremental-write justification:** this record is written for **new falsification / negative evidence** — it is the first repository record documenting an FDR-controlled null for label-trained daily headline sentiment → next-session cross-sectional equity returns, plus the classification-vs-economic-validity dissociation (Table 6 vs Tables 10/11). It is not a paraphrase of any existing positive sentiment record (source identities and supervision targets differ; see Provenance).
- **Scope of the null:** the paper's own caveat stands — absence of next-session predictability under this design is not a general rejection of the economic value of financial sentiment (§6).

## Implementation status

`implementation_status: not-implemented`. Nothing from this record has been implemented in our research stack: no score pipeline, no backtest, no Qlib run, no production card, no Paper/Testnet/Live activity of any kind. This document is a normalized research capture only, and its presence in the repository does not imply any validation stage has begun.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence here does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. No wording, evidence count, or negative-result framing in this record promotes it to any later stage; adoption would require a separate explicit review.

## Related Wiki records

Real pages confirmed present in Hermes Wiki Brain via read-only `kb_search` on 2026-09-24 (queries: "financial news sentiment cross-sectional returns", "Kirtac Germano sentiment trading large language models"; no Wiki write was performed):

- [[quant/finsmart-market-aligned-reinforcement-learning-sentiment-alpha-2026-09-02]] — cross-sectional equity sentiment alpha via GRPO; same input family, positive-result framing, different source and mechanism (RL optimisation of sentiment trading rather than a label-vs-returns validity test).
- [[quant/llm-news-enhanced-cross-sectional-momentum-tilt]] — LLM news sentiment tilting of cross-sectional momentum; useful contrast for whether sentiment adds anything beyond momentum (relevant to F3).
- [[quant/tda-persistent-homology-finbert-sentiment-portfolio-optimization-2026-09-02]] — FinBERT news sentiment as a portfolio input with a topological filter; same raw signal class, different construction.
- [[quant/news-event-tag-drift-rumor-resolution-placebo-adjusted-momentum-2026-09-02]] — placebo-adjusted news-event abnormal-return dynamics; methodological template for F7.
- [[quant/ai-misinformation-risk-factor-pricing-news-lda-2026-09-11]] — cross-sectional equity exposure to news-derived innovations; adjacent news-text factor evidence.
- [[quant/llm-news-sentiment-direct-rl-crypto-trading-ddqn-grpo-2026-09-06]] — news-sentiment trading in crypto (the crypto-side sibling of this signal family; relevant to the portability section).

Adjacent repository records that are **not** Wiki links (dedup context only; different source identities): `llm-news-probing-excess-return-sentiment-timing-2026-09-06.md` (Kirtac & Germano 2024 — closest positive-result counterpart: return-supervised probing, intraday timing), `llm-event-aware-sentiment-factor-contrarian-alpha-2026-09-04.md`, `hybrid-xgboost-finbert-regime-adaptive-equity-2026-09-04.md`, `finsmart-market-aligned-reinforcement-learning-sentiment-alpha-2026-09-02.md`, `earnings-call-speaker-weighted-sentiment-cross-section-2026-09-23.md` (earnings-call sentiment cross-section, different event window), `cross-sectional-realized-skewness-dispersion-market-timing-2026-09-24.md`. No existing record covers arXiv `2608.04200`, Benzinga analyst-ratings headlines, or an FDR-controlled null for label-trained headline sentiment.

## Sources

- Fusheng Luo, *From Financial Sentiment Classification to Return Predictability: A QLoRA Benchmark of Large Language Models*, **arXiv:2608.04200v1 [q-fin.MF]**, submitted 4 August 2026 — https://arxiv.org/abs/2608.04200
- Full text (read directly for this record): https://arxiv.org/html/2608.04200v1 — §§3.2–3.5, 4, 5.2, 6, 6.1; Tables 2, 3, 6, 7, 8, 10, 11; Figures 1 and 5.
- PDF: https://arxiv.org/pdf/2608.04200v1 (HTTP 200; `filename="2608.04200v1.pdf"`; `last-modified: 2026-08-06`; `etag "CJKWjJ/bipYDEAI="`).
- DOI (arXiv-issued, DataCite): https://doi.org/10.48550/arXiv.2608.04200
- Downstream data source named by the paper (not independently re-fetched): Benzinga analyst-ratings headlines, calendar 2019; fixed S&P 100 constituents as of 2019-01-01.
