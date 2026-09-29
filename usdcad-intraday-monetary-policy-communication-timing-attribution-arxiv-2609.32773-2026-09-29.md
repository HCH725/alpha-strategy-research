---
schema: strategy-research-record-v1
title: "Intraday USD/CAD Directional Forecasting from Central-Bank Communication Timing and Activity: FDR-Controlled Cumulative-Ablation Attribution"
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - foreign-exchange
  - monetary-policy
  - intraday
  - nlp
  - feature-attribution
status: research-only
confidence: low
source_as_of: "2026-09-26"
sources:
  - "https://arxiv.org/abs/2609.32773v1"
  - "https://arxiv.org/html/2609.32773v1"
  - "https://doi.org/10.48550/arXiv.2609.32773"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Section IV-D states that the evaluated models' out-of-sample R-squared values exceed 0.86 across the forecasting horizons, while Table II prints the best-ML 24-hour R-squared as 0.8442 and Section IV-A states the range as 0.844-0.915; the source does not reconcile which model set the 0.86 floor refers to (research-computed gap 0.0158)."
  - "Table V reports the single feature is_news_hour with mean delta R-squared +0.012 (the largest positive contributor) while Table VI reports the whole News timing only group at +0.0005; the group nests that feature, so the joint removal of the group degrades R-squared about 24x less than removing the one feature, and the source offers no reconciliation beyond its general admission that cumulative ablation is path dependent (research-computed ratio 0.012/0.0005 = 24)."
  - "Section III-A states a continuous hourly grid spanning 2024-06-13 to 2026-06-12 with 17,517 hourly USD/CAD observations, while that inclusive window contains 17,520 hourly slots (730 days x 24) leaving 3 slots unexplained and the endpoint convention unstated (research-computed)."
---

# Intraday USD/CAD Directional Forecasting from Central-Bank Communication Timing and Activity: FDR-Controlled Cumulative-Ablation Attribution

## Provenance

- **Primary source:** Maya Kodeih, Aliaa Alnaggar, Mucahit Cevik, *"Forecasting Intraday USD/CAD Exchange Rate with News-Derived Monetary-Policy Signals"*, `arXiv:2609.32773v1 [cs.AI]`, submitted 26 Sep 2026.
- **Author list (exactly as source):** **Maya Kodeih, Aliaa Alnaggar, Mucahit Cevik** — three authors, order as printed. Verified two ways on the pinned abstract page: `citation_author` meta tags (`Kodeih, Maya` / `Alnaggar, Aliaa` / `Cevik, Mucahit`) and the rendered author block. The HTML front matter prints all three affiliations as **Department of Mechanical and Industrial Engineering, Toronto Metropolitan University, Toronto, ON, Canada** with corresponding-author e-mails `mkodeih@torontomu.ca`, `aliaa.alnaggar@torontomu.ca`, `mcevik@torontomu.ca`. No ORCID is printed → `data gap`.
- **Version pinned:** **v1 only** — submission history `[v1] Sat, 26 Sep 2026 16:50:39 UTC (576 KB)` from Maya Kodeih; dateline `[Submitted on 26 Sep 2026]`. No v2 exists as of 2026-09-29.
- **Subjects:** `Artificial Intelligence (cs.AI)` (primary) `; Machine Learning (cs.LG); Computational Finance (q-fin.CP)`.
- **Publication status:** **not stated in source beyond a venue comment.** The Comments field reads exactly **"IEEE CASCON 2026"**; there is **no journal-ref, no proceedings DOI, no publisher reference and no peer-review statement** on the landing page, and the arXiv-issued DOI `10.48550/arXiv.2609.32773` is annotated **"DOI via DataCite (pending registration)"**. The record therefore treats the paper as a **preprint whose Comments field names a venue**; no independent proceedings listing was verified and none is asserted.
- **License:** abs page license link resolves to `arXiv.org/nonexclusive-distrib/1.0/` and the HTML masthead prints `License: arXiv.org perpetual non-exclusive license` → **not a Creative Commons licence**; only short printed values and section references are normalised here.
- **Primary text pinned:** `https://arxiv.org/html/2609.32773v1`, HTTP 200, **173,808 bytes**, SHA-256 `21821b58c00a26df90b936bf7ccef73d95a102a13e5fb4a8315eec90b560fcc4`, downloaded and **read end to end on 2026-09-29** (56,748 characters / 559 extracted lines: Abstract, Sections I-V, Equations (1)-(5), Tables I-VI, Figure 1-4 captions, References [1]-[20]). Abstract page pinned at **43,200 bytes**, SHA-256 `0c475def1584a3dd19ef759a5c51d41496b7d3b7fc3f6f7cd85b16262f3cdc7a`, used for the author list, dateline, Comments, Subjects, submission history and DOI status. **PDF not downloaded → PDF bytes and checksum are `data gap`.**
- **Code / data:** the paper contains **no code-availability, data-availability, repository or supplementary-material statement** (whole-text scan: the only `GitHub` tokens on the page are arXiv's own "Report GitHub Issue" chrome and one bibliography URL). The sentiment pipeline, feature list beyond Table I, model hyperparameters and rolling-window code are therefore **not reproducible from the primary source** → `data gap`.
- **Sample period (source, §III-A):** **2024-06-13 to 2026-06-12**, i.e. 927 retained monetary-policy articles aligned with **17,517 hourly USD/CAD observations**; data ends 3 months 14 days before submission and the source gives no reason for the end date → `data gap`.
- **Universe / instrument (source):** a **single instrument, the USD/CAD exchange rate at hourly frequency**, aligned to a continuous hourly grid; weekend and other missing observations are **forward-filled using the most recent available exchange rate** while observations supplied by the vendor are retained. There is no cross-sectional universe, no second pair and no crypto instrument.
- **Venue / data vendors (source):** exchange-rate data from **Yahoo Finance**; news from **TheNewsAPI with RSS-feed aggregation**, filtered by a monetary-policy vocabulary (Federal Reserve, Bank of Canada, interest rates, inflation, forward guidance, QE/QT and related macro concepts), de-duplicated, timestamped and aggregated to hourly frequency. Sentiment labelling by **OpenAI GPT-4o-mini**.
- **Transaction-cost treatment (Methods-level):** determined from a read of §III (III-A through III-I), §IV (IV-A through IV-E) and §V plus a word-boundary census of the pinned HTML text: **`transaction cost` appears exactly once, `slippage`, `bid-ask`, `commission`, `fees`, `turnover`, `market impact`, `liquidity`, `order book`, `fill`, `execution`, `borrow`, `margin`, `leverage`, `latency`, `capacity`, `sharpe`, `backtest`, `win rate` and `position` all appear zero times**, and the two `spread` hits are the U.S.-Canada interest-rate spread used as a *predictor*, not a trading spread. The single `transaction cost` hit is the source's own §V admission that the study *"evaluates statistical forecasting performance rather than economic value and therefore does not consider transaction costs, market frictions, or trading profitability."* So **no friction is modelled at all: this is an explicit by-design absence stated by the source, not an unmodelled-by-oversight claim**, and every execution field (order type, fill, signal-to-order delay, latency, spread, slippage, impact, participation, borrow, funding, leverage, capacity) stays `data gap` and is **never read as zero**.
- **Repository-wide source-identity dedup (performed 2026-09-29 before writing):** `rg -uuu -F` over **all `*.md` files including `.mimo-worktrees`, `.agents`, `.hermes`** for `2609.32773`, `Forecasting Intraday USD/CAD`, `Kodeih`, `Alnaggar`, `Mucahit Cevik`, `is_news_hour`, `TheNewsAPI`, `torontomu`, `monetary-policy communication` → **0 hits each**; the same nine tokens plus `USD/CAD` scanned against **`coverage_manifest.csv` (5,807 data rows, 1,088,787 bytes)** → **0 hits each**; positive control `novy-marx` returned **30 files** in the same session; `git log --oneline -20` used as a convenience glance only. **This source identity is not in the repository.**
- **Family distinction vs adjacent in-repo captures (stated on mechanism, not title):**
  - `foreign-exchange-macro-news-fundamental-momentum-llm-taylor-rule-2026-09-02.md` (arXiv:2608.00761) — G-10 **cross-sectional monthly** fundamental-momentum book from economic-calendar surprises with a Taylor-rule anchor and a printed Sharpe claim. Distinct on **source identity**, on **signal construction** (calendar-surprise fundamental momentum vs central-bank communication timing/activity features), on **horizon** (monthly vs 1-24 hours) and on **market type** (cross-sectional G-10 vs a single USD/CAD book with no portfolio at all).
  - `gdelt-finbert-xgboost-macro-news-sentiment-fx-treasury-directional-2026-09-24.md` (arXiv:2505.16136) — **next-day** directional trading on EUR/USD, USD/JPY and ZN from GDELT FinBERT polarity with a printed cost deduction. Distinct on **source identity**, on **signal construction** (polarity/impact features vs communication-channel ablation with FDR control), on **horizon** (daily next-day vs intraday hours), on **universe** (three instruments with a costed backtest vs one pair with no economic-value evaluation) and on **material data dependency** (GDELT Events API vs TheNewsAPI + RSS + GPT-4o-mini stance labels).
  - `bitcoin-fomc-announcement-event-drift-contraction-2026-09-01.md` — FOMC **event-day drift in BTC equities/crypto**, i.e. an event-study return claim rather than a forecasting/attribution design; different source, different market, different horizon.
  - **No existing repository record uses the USD/CAD pair, an hourly FX grid, or a central-bank-communication attribution design as its primary object.**
- **Wiki Brain was read only:** `kb_read quant/strategy-research-record-spec-v2.md` → **file not found, so the run failed closed onto `quant/strategy-research-record-spec-v1.md` (canonical, 10,289 bytes, SHA-256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`)**; `kb_search "FX news sentiment monetary policy communication forecasting"` → 0 pages, `kb_search "foreign exchange FX direction prediction"` → 4 low-scoring adjacent pages (Fourier-residue equity reversal, cross-asset hybrid drawdown ensemble, NautilusTrader adapter notes, cross-asset futures timing transformer), none sharing this source identity or mechanism. **No Wiki page was written, no Wiki link was fabricated.**
- **Boundaries:** no Wiki Brain write, no Kanban, no backtest, no market-data download, no dependency install, no code execution of any kind.

## Economic mechanism

### Source-reported

The authors' stated rationale (§I, §III, §IV, §V): monetary-policy announcements, policy guidance and central-bank communication move exchange rates by reshaping expectations about future rates and inflation, but prior FX work mostly tests *whether* text helps and not *which dimension* of the communication helps. The paper's claimed channels are (i) **communication timing** — the hours in which policy-relevant news arrives (`is_news_hour`), (ii) **communication activity** — counts of recent Federal Reserve / Bank of Canada articles and non-neutral-communication events in trailing 6h / 24h / 168h windows, (iii) **LLM-derived stance sentiment** — GPT-4o-mini hawkish/dovish/neutral/mixed labels for Fed and BoC separately, aggregated into a sentiment differential `SD_t = S_t^Fed - S_t^BoC`, an impulse `I_t = SD_t` on arrival hours else 0, an exponential decay `D_t = SD_t · exp(-λ·Δt)` and rolling means `RS_t^(k)`, (iv) **policy stance** and (v) **information persistence**, benchmarked against conventional market variables (USD/CAD lags, intraday volatility, the U.S.-Canada rate spread, macro momentum, WTI). The source's headline conclusion is that predictive value **concentrates in a small subset of engineered features**, with timing strongest individually, targeted activity measures positive, LLM sentiment complementary at group level, and broad aggregate news volume largely redundant; the methodological claim is that **attribution (cumulative ablation under Benjamini-Hochberg FDR control), not aggregate accuracy, is the right evaluation object**.

### Research interpretation

Stated falsifiably: **attention-arrival timing in a slow-diffusing public-information stream predicts the sign of the next few hours of a single FX pair, while the *level* remains a random walk.** The testable content is not the tree ensemble — it is the claim that (a) conditioning on *when* policy information arrives (and on how intensely the two central banks are speaking) shifts the conditional sign probability of `y_{t+h} - y_t` at 1-24 hour horizons beyond what price persistence alone gives, and (b) that shift survives multiple-testing control. Roles of the components in a tradable reading (all **research-proposed**, none of it in the source): **regime/context** = macro and rate-spread covariates; **primary signal** = modelled `P(y_{t+h} > y_t)` built from communication timing/activity features; **confirmation** = the FDR-supported feature subset only (drop `news_articles_*` and `hours_since_*_168h`, which the source itself finds net negative); **risk/exit** = research-proposed time stop and a cost ladder, since the source supplies no exit, sizing, holding period or cost rule at all. A less flattering reading the same evidence supports: `is_news_hour` is an **information-arrival indicator**, so the model may be forecasting short-horizon *volatility/dispersion around news* rather than direction, and the level-forecast benchmark result (the random walk wins at every horizon) says the information set adds nothing to price-level dynamics.

## Signal

Everything below is **source-reported unless explicitly tagged `research-proposed` or `underspecified`**.

- **Formation timestamp:** hourly grid; news articles are timestamped and aggregated to hourly frequency, and §III-I states every prediction is generated *"using only information available at the forecasting time, avoiding look-ahead bias"*. Timezone of the article timestamps and of the hourly grid is **not stated** → `underspecified`.
- **Lookback:** rolling sentiment means `RS_t^(k)` over *"multiple lookback windows"* with **k values not enumerated** → `underspecified`; named trailing windows that do appear: `fed_articles_24h`, `fed_non_neutral_last_24h`, `boc_articles_24h`, `boc_news_last_24h`, `fed_news_last_6h`, `news_articles_6h`, `news_articles_24h`, `hours_since_news_168h`, `hours_since_boc_news_168h`. Decay rate **λ not stated** → `underspecified`. Warm-up: rolling windows make the first observations shorter; §III-A says windows are *"slightly smaller windows at the beginning of the sample"*.
- **Target / "entry" in the source's own terms (Eq. 5):** `d_{t+h} = 1` if `y_{t+h} - y_t > 0`, else `0` — a **strict inequality, so a flat (forward-filled) move is labelled 0**. Horizons **h ∈ {1, 3, 8, 24} hours**, trained as separate direct models per horizon (no recursive error propagation).
- **Decision rule:** the classifier probability is *"converted into a binary prediction using a decision threshold"* — **the threshold value is never printed** → `underspecified`. Classification metrics: directional accuracy (DA), balanced accuracy, macro-F1, AUC; benchmarks are a majority-class predictor and a persistence predictor.
- **Level task:** direct multi-horizon regression of the USD/CAD level with **Extra Trees, XGBoost and LightGBM**; probabilistic extension via native quantile objectives (LightGBM, XGBoost) or ensemble-member quantiles (Extra Trees), with conformal calibration evaluated only as a separate post-processing step. **Hyperparameter values and the random-seed value are not printed in the pinned text** (the source only says hyperparameters stayed constant across windows and a fixed seed was used) → `underspecified`.
- **Rolling evaluation:** each window is split **85/15 train-test** ≈ **4,324 training and 764 out-of-sample observations** (window ≈ 5,088 observations ≈ 212 days; research-computed 15% × 5,088 = 763.2 ≈ 764). How metrics are pooled across windows — mean of window scores or pooling of overlapping OOS predictions — is **not stated**, and the printed 1-hour test-set class counts (939 up / 1,602 down = 2,541) exceed a single window's 764 OOS slots by 3.3× → `underspecified`.
- **Benchmarks:** level → 3-observation moving average and the **no-change random walk** `ŷ_{t+h} = y_t`; direction → majority-class and persistence.
- **Long entry / short entry / exit / holding period / re-entry / position sizing:** **the source specifies none of these** — there is no trading rule, no portfolio, no holding period and no sizing rule anywhere in the paper. `research-proposed` operationalization for any future test: sign rule `long USD/CAD` when `P(up) > 0.5 + τ` and `short` when `P(up) < 0.5 - τ` with **τ = 0.05 (research-defined)**, entered at the next hourly bar open, flat otherwise, **time exit after h hours (research-proposed)**, one position at a time, **no re-entry within the same h-hour block (research-proposed)**. None of that is source-reported.
- **Fully specified?** **No — underspecified.** The feature set (Table I categories + named examples), the targets and the evaluation protocol are reconstructable; the threshold, lookback grid, λ, hyperparameters, seed, prompt template and pooling rule are not.

## Required data

- **Instrument / universe:** USD/CAD spot, hourly; single-instrument universe, no cross-section, no survivorship logic, no reconstitution.
- **Venue / market type:** FX spot via a data vendor (Yahoo Finance named); OTC market structure, session calendar not stated → `data gap`.
- **Timeframe:** hourly bars on a **continuous grid including weekend hours filled by forward-fill of the last price**; the source explicitly notes weekend market closures produce missing observations.
- **Fields:** USD/CAD hourly rate (level only — **no OHLCV is named**), article publication timestamps, article text, Fed/BoC stance labels, engineered counts/recency/impulse/decay features, USD/CAD lags, intraday volatility, U.S.-Canada rate spread, macro momentum series, WTI crude oil price.
- **Point-in-time:** article timestamps are asserted to be aligned before aggregation and predictions use only information available at forecast time, but **publication-vs-arrival semantics, RSS delay, and any revision handling are not described** → `data gap`.
- **Timestamp / timezone:** not stated → `data gap`.
- **Missing data:** missing observations including weekend closures are **forward-filled** (source); no other missing-data rule, no bad-print handling, no imputation policy for features → partially specified.
- **Funding / fee / spread needs:** **not observed, not modelled, explicitly out of scope** (§V). For any tradable version: FX spot spread, cross-check on the USD/CAD hourly bid-ask, and the two-day rollover/swap on overnight positions would all have to be added — **all `research-proposed`, none in the source.**

## Execution assumptions

- **From the source:** none. §V states outright that the study *"does not consider transaction costs, market frictions, or trading profitability"* and proposes *"realistic trading evaluations"* as future work together with Diebold-Mariano and Clark-West tests.
- **Signal-to-order timing / next-bar vs same-bar / order type / fill model / fees / spread / slippage / impact / capacity / funding / leverage / margin / borrow / latency / partial fills:** **all `data gap` in the source**, never zero.
- **`research-proposed` assumptions for a future test (not source-reported):** signal formed at the close of hour `t`, order submitted at the open of hour `t+1` (one-hour delay), market order, full fill, round-trip cost ladder **0/1/2/3/5 bps (research-defined)**, no leverage, long/short both permitted, single position at a time, no borrow constraint assumed for spot FX.
- Because the source reports **no portfolio construction at all**, every reported number below is a **forecasting** statistic and must not be read as a return, Sharpe, or hit rate of a strategy.

## Evidence

### Source-reported

All figures are third-party, source-reported, none independently reproduced; provenance is the pinned v1 HTML.

**Table II (§IV-A) — level forecasting vs random walk, OOS inside rolling windows:**

| Horizon | Best-ML R² | Best-ML NRMSE | RW R² | RW NRMSE |
|---|---|---|---|---|
| 1h | 0.9150 | 0.00549 | 0.9988 | 0.00065 |
| 3h | 0.9039 | 0.00584 | 0.9967 | 0.00109 |
| 8h | 0.8886 | 0.00628 | 0.9916 | 0.00173 |
| 24h | 0.8442 | 0.00742 | 0.9764 | 0.00289 |

Best model names printed only for two cells: 1h **LightGBM Direct**, 24h **Extra Trees Direct** (§IV-A prose); 3h/8h model identity `data gap`. The source's own reading: *"none of the evaluated machine-learning models outperforms the no-change random walk on level-based forecasting metrics"*, with the gap narrowing as persistence weakens. Research-computed ratios of ML NRMSE to RW NRMSE: **8.4x / 5.4x / 3.6x / 2.6x**.

**Table IV (§IV-C) — directional classification, best results per horizon:**

| Horizon | DA (%) | Majority (%) | Persistence (%) | Balanced acc. | Macro F1 | AUC |
|---|---|---|---|---|---|---|
| 1h | 66.08 | 63.05 | 62.61 | 0.721 | 0.660 | 0.744 |
| 3h | 65.12 | 61.54 | 61.57 | 0.698 | 0.651 | 0.729 |
| 8h | 66.55 | 57.80 | 61.51 | 0.705 | 0.658 | 0.707 |
| 24h | 63.22 | 51.14 | 57.70 | 0.626 | 0.604 | 0.634 |

Source-stated margins over the majority baseline ≈ **+3.0 / +3.6 / +8.7 / +12.1 pp**; research-computed exact margins **+3.03 / +3.58 / +8.75 / +12.08 pp** and over persistence **+3.47 / +3.55 / +5.04 / +5.52 pp**. Class shares printed: 1h test set **939 up / 1,602 down** (majority 63.05%), 3h **38.46/61.54**, 8h **42.20/57.80**, 24h **51.14/48.86**. §IV-C concludes the communication features *"may be more useful for predicting market direction than for improving precise exchange-rate level forecasts in this setting."*

**Table III (§IV-B) — uncalibrated probabilistic forecasts, Full vs Step 7 (reduced) feature set:**

| H | Pinball Full | Pinball Step 7 | WIS Full | WIS Step 7 | Cov90 Full | Cov90 Step 7 |
|---|---|---|---|---|---|---|
| 1h | 0.003329 | 0.001479 | 0.002394 | 0.001062 | 53.72 | 68.92 |
| 3h | 0.003731 | 0.001989 | 0.002682 | 0.001429 | 63.23 | 58.47 |
| 8h | 0.004001 | 0.002829 | 0.002877 | 0.002032 | 61.85 | 50.88 |
| 24h | 0.004600 | 0.004102 | 0.003308 | 0.002946 | 57.85 | 46.29 |

Source-stated pinball reductions **55.6% / 46.7% / 29.3% / 10.8%** (research-recomputed 55.57 / 46.69 / 29.29 / 10.83 ✓). Nominal-50% coverage across the grid **30.85%-44.01%**, nominal-90% coverage **53.72%-63.23%** — systematically too narrow. Step 7 improves scoring but **worsens coverage at 3h/8h/24h**.

**Table V (§IV-D) — FDR-supported feature-level attribution (mean ΔR² on removal, 95% bootstrap CI, global BH q):**

| Feature | Mean ΔR² | Mean ΔDA | 95% CI | q |
|---|---|---|---|---|
| `is_news_hour` | +0.012 | +0.04 pp | [+0.006, +0.018] | 0.003 |
| `fed_non_neutral_last_24h` | +0.005 | -0.01 pp | [+0.003, +0.008] | 0.003 |
| `fed_articles_24h` | +0.005 | -0.10 pp | [+0.002, +0.008] | 0.008 |
| `boc_news_last_24h` | +0.005 | -0.09 pp | [+0.001, +0.009] | 0.041 |
| `boc_articles_24h` | +0.003 | +0.08 pp | [+0.001, +0.004] | 0.026 |
| `news_articles_24h` | -0.010 | -0.07 pp | [-0.014, -0.006] | 0.001 |
| `intraday_volatility` | -0.010 | +0.03 pp | [-0.016, -0.004] | 0.008 |
| `hours_since_boc_news_168h` | -0.009 | +0.02 pp | [-0.015, -0.004] | 0.008 |
| `fed_news_last_6h` | -0.007 | +0.08 pp | [-0.012, -0.004] | 0.008 |
| `news_articles_6h` | -0.005 | -0.01 pp | [-0.007, -0.002] | 0.008 |
| `hours_since_news_168h` | -0.005 | +0.03 pp | [-0.007, -0.002] | 0.007 |

**Table VI (§IV-E) — group-level attribution (mean ΔR² / mean ΔDA):** News timing only **+0.0005 / -0.01 pp**; News volume only **-0.0018 / -0.01 pp**; LLM-derived sentiment only **+0.0020 / +0.02 pp**; Combined **+0.0001 / -0.00 pp**. Representative sentiment features: `sent_diff_impulse` +0.001/-0.05 pp, `sent_diff_decay_24h` +0.002/-0.00 pp, `usd_cad_confidence` +0.003/+0.06 pp, `usd_cad_direction` -0.000/+0.02 pp, `sent_diff_decay_6h` -0.001/+0.07 pp. §IV-E also states that oil price (`DCOILWTICO`), the rate spread (`_Spread_pct`) and sentiment-decay features **rank highest by model importance yet add little under ablation**, whereas `is_news_hour` has low importance and the largest ablation effect.

**Validation and design facts (source):** GPT-4o-mini stance labelling checked against a **random sample of 100 articles**, reported only as *"generally consistent"* with **no agreement statistic**; a non-neutral-communication event study described qualitatively as *"often directionally consistent"* with **no numbers**; a **fixed random seed** (value not printed) and **constant hyperparameters** across windows; **Benjamini-Hochberg FDR** applied to ablation p-values, with a feature counted only if the CI excludes zero **and** q passes the threshold (threshold value not printed → `underspecified`).

### Independently reproduced

not independently reproduced

Arithmetic-only checks performed on 2026-09-29 against the pinned text (**research-computed; no data, no model, no code was run**): the four DA-minus-majority and four DA-minus-persistence margins reproduce exactly; `939 + 1602 = 2,541` and `1602/2541 = 63.05%` reproduce the printed majority; the four pinball reductions reproduce to two decimals; `4,324 + 764 = 5,088` with `0.15 × 5,088 = 763.2 ≈ 764` reproduces the 85/15 split; the inclusive 2024-06-13 → 2026-06-12 window gives **17,520** hourly slots against the printed **17,517** (Δ 3, unreconciled); Table II's 24h best-ML R² of 0.8442 sits **0.0158 below** the §IV-D statement that R² exceeds 0.86 across horizons; Table V `is_news_hour` ÷ Table VI timing group = **24×**.

### Negative evidence

1. **No economic value is claimed or measured.** §V: the study *"evaluates statistical forecasting performance rather than economic value and therefore does not consider transaction costs, market frictions, or trading profitability."* There is **no strategy in the source** — no entry, exit, sizing, holding period, turnover, return, Sharpe or drawdown (word census: `sharpe`, `backtest`, `turnover`, `position`, `win rate` all zero occurrences).
2. **The level task loses to the random walk at every horizon** (Table II): ML R² 0.9150/0.9039/0.8886/0.8442 vs RW 0.9988/0.9967/0.9916/0.9764, and ML NRMSE **8.4×/5.4×/3.6×/2.6×** the RW error (research-computed). The source states this plainly.
3. **The attributed predictive value therefore lives inside a model that does not beat the trivial benchmark on the metric used for attribution (ΔR²).** The headline attribution is a statement about relative model fit, not about an edge over a naive forecaster.
4. **Directional edges over the trivial baselines are small at the short horizons:** +3.03 pp over majority and +3.47 pp over persistence at 1h, +3.58/+3.55 pp at 3h (research-computed), with a 63.05% majority class at 1h.
5. **Discrimination decays with horizon:** AUC 0.744 → 0.634 and balanced accuracy 0.721 → 0.626 from 1h to 24h; at 24h the raw DA edge is the largest (+12.08 pp) but against the weakest baseline (51.14%).
6. **The LLM sentiment layer contributes little incrementally:** group sentiment ΔR² **+0.0020**, representative sentiment features between **-0.001 and +0.003**, while the single biggest contributor is a **binary news-arrival indicator** (`is_news_hour`, +0.012). The commercial LLM pipeline is not where the value sits by the source's own numbers.
7. **Most engineered features are net negative once FDR is applied:** six of eleven supported features have negative ΔR² (-0.005 to -0.010), including `intraday_volatility` and every aggregate news-volume variable → *"Improving communication-based forecasting is thus as much about selecting informative features as about adding new ones."*
8. **Attribution is method-dependent:** §IV-E reports that model importance ranks oil, the rate spread and sentiment decay at the top while ablation ranks them as useless or harmful; and §V concedes *"cumulative ablation is inherently path dependent"*. The Table V vs Table VI inconsistency (contested, contradiction 2) is a concrete instance.
9. **Interval calibration is bad and gets worse at long horizons:** nominal-90% coverage 53.72%-63.23% for the full set; Step 7 pushes 3h/8h/24h coverage down to 58.47/50.88/46.29%.
10. **The 90% interval under-covers by 26-46 pp at 24h** (57.85% and 46.29% vs 90%) → any probabilistic-sizing overlay built on these intervals would be under-capitalised (research interpretation).
11. **Stale-price labelling risk from the forward-filled grid (research-computed concern):** weekend hours are forward-filled, and Eq. 5 labels any non-positive move as 0, so **flat hours are counted as "not up"**. The source never reports a flat/stale share by horizon, so part of the 63.05% 1h majority class may be stale quotes rather than genuine down moves. The nearly balanced 24h class shares (51.14/48.86) versus the strongly skewed 1h shares (36.95/63.05) are not explained anywhere in the paper.
12. **Thin and opaque news input:** **927 articles over 730 days (≈1.27/day, research-computed)** after a monetary-policy vocabulary filter whose term list is not printed; near-duplicate rule not printed; TheNewsAPI is a commercial feed with no archive guarantee → point-in-time reconstruction is `data gap`.
13. **Unquantified label quality:** a 100-article manual check reported as *"generally consistent"* with **no kappa, no confusion matrix, no inter-rater agreement**, plus an admitted sensitivity to *"prompt design, model selection, and classification uncertainty"* (§V) with no prompt published.
14. **No significance test on the headline gaps:** bootstrap + BH FDR is applied to **ablation** effects only; the DA-vs-benchmark gaps carry **no confidence interval, no DM/Clark-West test** (explicitly deferred to future work, §V).
15. **Single pair, single 730-day window, single policy regime:** USD/CAD with Fed and BoC only; §V itself says this *"limit[s] direct generalization to other currencies and monetary-policy regimes"*. No regime split, no pre-2024 extension, no second data vendor.
16. **Reproducibility is zero from the source:** no code, no data-availability statement, no hyperparameters, no seed value, no threshold, no feature ordering (the ablation sequence is *"predefined"* but not printed) — the entire pipeline is `underspecified` for an independent re-run.
17. **Design detail that can leak overlap:** printed 1h class counts (2,541) are 3.3× a single window's 764 OOS slots, so metrics are almost certainly aggregated across windows, but pooling/overlap handling is unstated → possible double counting of OOS observations is unresolved.
18. **Preprint status with only a Comments-field venue claim** ("IEEE CASCON 2026"), no journal-ref, no proceedings DOI, no peer-review statement, and a DataCite-pending arXiv DOI.
19. **Post-sample gap:** data end 2026-06-12, submission 2026-09-26 — nothing after June 2026 is evaluated, and no frozen forward window exists.

## Falsification plan

Every threshold below is **research-defined** (none comes from the source), and each gate has a pre-declared action on failure that **forbids retuning to rescue it**.

- **F1 — printed-value reproduction.** Re-run the published pipeline (requires author code/data; if unreleased, record `data gap` and treat F1 as failed-by-unavailability, not passed) and require Table IV DA within **±0.5 pp** and Table V `is_news_hour` ΔR² within **±0.003** at every horizon. *Action on failure:* drop all printed numbers as non-reproducible; no parameter search.
- **F2 — benchmark gate (the gate the source skipped).** Test the communication-feature model against the no-change random walk **and** against a price-features-only model with a Diebold-Mariano test on levels and a paired test on DA; require **two-sided p < 0.05 (research-defined)** and DA edge ≥ **+2.0 pp (research-defined)** over both baselines at ≥3 of 4 horizons. *Action on failure:* the hypothesis is rejected as a forecasting claim; attribution numbers become irrelevant.
- **F3 — stale-hour exclusion.** Recompute all direction metrics **excluding every forward-filled/non-trading hour**; require the DA edge over the majority class to remain **≥ +2.0 pp (research-defined)** at ≥3 of 4 horizons and the majority class to stay within **5 pp (research-defined)** of the full-sample value. *Action on failure:* the effect is a stale-quote artefact; reject.
- **F4 — economic-value gate (`research-defined`).** Implement the research-proposed sign rule (threshold τ = 0.05, next-hour entry, h-hour time exit, one position) under a **0/1/2/3/5 bps round-trip ladder**; require **net Sharpe ≥ 0.50 (research-defined)** and positive net mean return at **2 bps (research-defined)** over the frozen sample, plus net performance reported at the **same horizons** used for the DA claim. *Action on failure:* report as "forecasting-only, no tradeable edge"; do not re-tune τ.
- **F5 — attribution path-stability.** Repeat cumulative ablation under **≥5 randomly permuted removal orders (research-defined)**; require `is_news_hour` to remain a **top-3 positive contributor in ≥4 of 5 orders (research-defined)** and the sign of every Table V row to be preserved in ≥4 of 5. *Action on failure:* treat the attribution headline as path artefact.
- **F6 — group/feature consistency reconciliation.** Require the joint removal of the timing group to degrade R² **at least as much as** removing `is_news_hour` alone (monotonicity of nested removals, up to a **±0.002 tolerance, research-defined**). *Action on failure:* mark contradiction 2 unresolved and downgrade confidence.
- **F7 — cross-pair generalisation.** Replicate on **≥5 additional G10 pairs (EUR/USD, GBP/USD, USD/JPY, AUD/USD, USD/CHF) (research-defined)** with the same features; require a **sign-consistent DA edge over the majority baseline in ≥4 of 6 pairs (research-defined)** and a pooled paired p < 0.05. *Action on failure:* reject as a single-pair/specific-regime effect.
- **F8 — frozen forward window.** Freeze the pipeline on 2026-06-12 data and evaluate **≥6 untouched months from 2026-10-01 (research-defined)**; require a positive DA edge in **≥4 of 6 months (research-defined)** with no feature re-selection. *Action on failure:* reject; no re-fit.
- **F9 — labeller robustness.** Re-label with **≥3 independent labelers (GPT-4o-mini, one different frontier LLM, one non-LLM baseline) (research-defined)** and require the timing/activity/sentiment group ordering to be preserved in **≥2 of 3 (research-defined)**, with a reported kappa ≥ **0.60 (research-defined)**. *Action on failure:* attribute the effect to labeller idiosyncrasy; reject.
- **F10 — point-in-time / leakage audit.** Verify article **arrival** timestamps (RSS/API receipt time) rather than publish time, and re-run; require the `is_news_hour` ΔR² to stay within **±0.003 (research-defined)** of the printed value. *Action on failure:* reject for look-ahead.
- **F11 — timestamp placebo.** Circularly shift article timestamps by **±7 days (research-defined)**, 1,000 draws; require the observed `is_news_hour` ΔR² to exceed the **95th percentile (research-defined)** of the placebo distribution. *Action on failure:* the timing feature is capturing generic intraday structure, not news.
- **F12 — news-supply sensitivity.** Subsample the 927 articles to **50% (research-defined)** across 10 draws; require the sign of the top-5 Table V effects to be preserved in **≥8 of 10 draws (research-defined)**. *Action on failure:* reject as supply-thin.
- **F13 — competing-explanation control.** Add a pure-volatility/news-arrival baseline (trailing realised vol + generic news count, no central-bank-specific features); require the central-bank-specific feature block to add **≥ +0.002 ΔR² with q < 0.05 (research-defined)** beyond it. *Action on failure:* the effect is generic event volatility, not monetary-policy information.

## Crypto portability

**`adapted` (performance `unproven`).** The mechanism — information-arrival timing in a slow-diffusing public stream shifting short-horizon direction probabilities — is instrument-agnostic and the paper's modelling stack (hourly grid, tree ensembles, cumulative ablation under FDR) needs only timestamps and a price series. But **nothing in the source is crypto evidence**: USD/CAD is an OTC FX pair with a weekday session, Fed/BoC communication has no direct crypto analogue, and the source evaluates no market other than USD/CAD.

Porting risks: (a) **24/7 sessions** remove the weekend-forward-fill block that this record flags as a labelling risk, but replace it with thin-liquidity session hours and no official close; (b) **news supply** — crypto-relevant drivers (ETF flows, exchange outages, large-transfer alerts, protocol exploits) are not central-bank text, so the 927-article vocabulary filter does not port and a new feed with trustworthy arrival timestamps is required; (c) **funding, mark/index price, liquidation and leverage** are entirely outside the source and matter for any perpetual-based version; (d) **venue fragmentation** makes a single vendor's hourly series an unreliable entry reference; (e) **spread and slippage** for BTC/USDT and ETH/USDT perps at hourly rebalance are unmodelled here, and the source's own by-design absence of cost modelling means there is no cost anchor to inherit; (f) **timestamp semantics** (exchange event time vs vendor bar time) become the decisive leakage question in 24/7 markets.

## Limitations

- `not independently reproduced`; every performance figure is `source-reported`.
- **No strategy exists in the source** — no entry, exit, sizing, holding period, cost, turnover, return, Sharpe or drawdown. Any operational rule in this record is explicitly `research-proposed`.
- `underspecified`: decision threshold, rolling-window lookback grid, decay λ, feature-removal order, hyperparameters, seed value, FDR threshold, metric pooling across windows, article timestamp timezone, filter vocabulary, prompt template.
- `data gap`: PDF bytes/checksum, code and data availability, inter-rater agreement for labels, flat/stale-hour share by horizon, 3-hour and 8-hour best-model identities, reason the sample ends 2026-06-12, venue/session definition for the hourly grid.
- **Three unreconciled source-internal contradictions recorded with `contested: true`** (R² floor 0.86 vs printed 0.8442; feature vs group attribution magnitude; 17,517 vs 17,520 hourly slots).
- Single pair, single 730-day window, single central-bank pair, one policy regime; no regime split, no second vendor, no cross-country replication, no frozen forward test.
- The commercial news dependency (TheNewsAPI) plus unpublished filtering makes point-in-time reconstruction unverifiable from the public record.
- Preprint status: Comments field "IEEE CASCON 2026", no journal-ref, no proceedings DOI, no peer-review statement; arXiv DOI pending DataCite registration.
- Commercial API dependency (OpenAI GPT-4o-mini) inside the signal path introduces cost, version-drift and reproducibility risk that the source does not quantify.

## Implementation status

`implementation_status: not-implemented`. **Nothing has been implemented in our research stack.** No feature pipeline, no model, no rolling-window harness, no signal generation, no backtest, no market-data download and no dependency installation was performed for this record. The only work done was reading the pinned primary source and arithmetic-only checking of printed values. No Qlib, Paper, Testnet or Live stage is connected, implied or attempted.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record in the staging repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. Research capture is not adoption, and no wording, number of evidence items, confidence value or schedule behaviour may promote it.

## Related Wiki records

Read-only retrieval hooks, no page written and no link fabricated. `kb_search "FX news sentiment monetary policy communication forecasting"` → **0 results**. `kb_search "foreign exchange FX direction prediction"` → 4 low-scoring adjacent pages, none sharing this source identity, mechanism or horizon: `quant/fourier-residue-sign-magnitude-equity-reversal-decomposition-2026-09-04`, `quant/cross-asset-hybrid-ensemble-short-horizon-drawdown-alpha-2026-09-06`, `quant/nautilustrader-adapters-developer-deep-notes-2026-08-10`, `quant/cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02`. `kb_read quant/strategy-research-record-spec-v2.md` returned file-not-found, so this record was built against the canonical `quant/strategy-research-record-spec-v1.md`. No materially related Wiki page for intraday FX or central-bank-communication attribution was found.

## Sources

- Primary: `https://arxiv.org/abs/2609.32773v1` (abstract page, 43,200 bytes, SHA-256 `0c475def1584a3dd19ef759a5c51d41496b7d3b7fc3f6f7cd85b16262f3cdc7a`) — authors, dateline, Comments "IEEE CASCON 2026", Subjects, submission history, DOI status.
- Primary full text: `https://arxiv.org/html/2609.32773v1` (HTTP 200, 173,808 bytes, SHA-256 `21821b58c00a26df90b936bf7ccef73d95a102a13e5fb4a8315eec90b560fcc4`), read end to end 2026-09-29 — Abstract, §I-§V, Eq. (1)-(5), Tables I-VI, Figure captions, References [1]-[20].
- DOI: `https://doi.org/10.48550/arXiv.2609.32773` (DataCite, pending registration as printed on the landing page).
- PDF: `https://arxiv.org/pdf/2609.32773` — **not downloaded**, so no PDF-level figure was used anywhere in this record.
- No code, data, repository or companion source is cited by the primary source; none was substituted from secondary summaries. Search-result material was used only to locate the paper, never to fill rules or numbers.
