---
schema: strategy-research-record-v1
title: "The Cost of Direction: Net-of-Cost Out-of-Sample Audit of the 212-Predictor Directional Anomaly Zoo with Low-Turnover Quality as the Lone Survivor (Alpha Research Paper 4)"
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-06-17
sources:
  - "https://bryanvine.github.io/alpha-research/paper4.html — Bryan Vine, 'The Cost of Direction: A Net-of-Cost Audit of the Directional Anomaly Zoo', Alpha Research Paper 4, byline June 17, 2026"
  - "https://github.com/bryanvine/alpha-research — file docs/paper4.html at full commit SHA 655e8d4f1ff4b41006e05931d078a722af1e732e (2026-06-17T00:34:13Z, commit message 'Paper 4: The Cost of Direction — a net-of-cost audit of the directional anomaly zoo') and at head 17b8b5e1c79af194f733544517d82e3cf12c2259; both byte-identical to the published page (SHA-256 06ddabcfb50247fad9bb1c5a8049ff7bbf83afaa50a2659d9d6bb7e399dfcef6, 19718 bytes, verified 2026-09-23)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# The Cost of Direction: Net-of-Cost Out-of-Sample Audit of the 212-Predictor Directional Anomaly Zoo with Low-Turnover Quality as the Lone Survivor (Alpha Research Paper 4)

## Provenance

- **Primary source:** Bryan Vine, *"The Cost of Direction: A Net-of-Cost Audit of the Directional Anomaly Zoo"* — Alpha Research, Paper 4 (byline **June 17, 2026**). Stable published URL: `https://bryanvine.github.io/alpha-research/paper4.html`.
- **Repository URL:** `https://github.com/bryanvine/alpha-research`.
- **Immutable provenance:** file path `docs/paper4.html` at **full commit SHA `655e8d4f1ff4b41006e05931d078a722af1e732e`** (2026-06-17T00:34:13Z, commit message *"Paper 4: The Cost of Direction — a net-of-cost audit of the directional anomaly zoo / A replication-crisis r…"*, GitHub commits API `path=docs/paper4.html`, single history entry) — the commit that introduced the paper.
- **Primary-source checksum (performed 2026-09-23):** three copies were fetched and hashed — (a) the live GitHub Pages file, (b) `docs/paper4.html` at creation commit `655e8d4f…`, (c) `docs/paper4.html` at repository head `17b8b5e1c79af194f733544517d82e3cf12c2259` (head as of 2026-09-23, last repository commit 2026-08-23). All three are **byte-identical**: SHA-256 `06ddabcfb50247fad9bb1c5a8049ff7bbf83afaa50a2659d9d6bb7e399dfcef6`, **19,718 bytes**; Git blob SHA `a2cedd3f4089143f48f7722b65f4f95b76e83523`. The published page equals the pinned artifact.
- **Full text read in this run (2026-09-23):** Abstract, §1 Introduction (pre-registered H1–H4), §2 Data & leakage control, §3 Method, §4.1–4.4 Results, §5 Discussion, §6 Limitations & future work, References.
- **Supporting code/data documentation directly inspected at head `17b8b5e1…`:** `scripts/16_fetch_factor_zoo.py`, `scripts/17_equity_zoo_core.py`, `scripts/18_factor_zoo_audit.py`, `scripts/43_paper4_figures.py`, `alpha_research/factors/equity_zoo.py`, `alpha_research/factors/carry.py`, `research/paper4_data_profile.md`, `configs/data_sources.yaml`. Every operational parameter marked *source-reported (code)* below was read from those files, not inferred.
- **Not present in the repository:** `data/` and `experiments/` contain only `.gitkeep` — the raw panels (`oap_ls_returns.parquet`, `famafrench_monthly.parquet`, FnSpID/Binance-derived panels) and the result JSONs (`experiments/paper4_zoo_audit.json`, `experiments/paper4_ourdata.json`) are **absent** → exact recomputation is impossible from the repository alone → `data gap`.
- **Publication status:** personal research-series blog post with public code and dated research log; **not peer-reviewed, no journal/conference acceptance, no external replication claimed** → `data gap` on independent vetting.
- **Repository-wide deduplication audit (2026-09-23, whole repository of 896 `*.md` records, not `git log`):** ripgrep across **all `*.md`** for `paper4.html`, `Cost of Direction`, `directional anomaly`, `anomaly zoo`, `655e8d4f`, `06ddabcf`, `equity_zoo`, `factor_zoo`, `43_paper4_figures`, `paper4_data_profile`, `16_fetch_factor_zoo`, `17_equity_zoo_core` → **zero records carry this source identity** (no `coverage_manifest` file exists in this repository). `alpha_research/factors/equity_zoo.py` appears only inside the sibling Paper-5 record (`vol-conditional-liquidity-provision-reversal-micro-price-execution-overlay-2026-09-23.md`), which captures a *different paper with a different mechanism* (volatility-conditional liquidity-provision reversal with Stoikov micro-price execution vs. this paper's zoo-wide cost/survival audit). `alpha_research/factors/carry.py` / `load_spot_returns` are cited by no record. Same-author records already in the pool cover Papers **1, 2, 3, 5, 6, 8, 9** (VRP, funding carry, crypto stat-arb, microstructure liquidity provision, FX carry/roll yield, on-chain premia decay, LLM valuation bots) — non-overlapping mechanisms; **only Paper 7 (a series synthesis) remains uncaptured and is a wrapper over papers 1–6, not an independent candidate.**
- **Distinction from the two nearest neighbours in the pool (material, not reframing):** (1) `reviving-anomalies-expected-net-return-double-sort-1n-implementable-2026-09-23.md` (SSRN 6468806) proposes an ML *expected-net-return* signal plus double sort and a 1/N implementable allocation — a **constructive alpha strategy**; this record's source builds **no new signal**: it is a *meta-audit* whose tested object is the 212 published predictors themselves, and whose deliverable is a survival cascade (decay → multiple testing → costs → recent decade) and a survivor ranking. (2) `anomaly-pre-release-drift-predicted-signal-decile-portfolios-2026-09-23.md` (SSRN 4939779) tests **pre-release drift inside a fixed window before accounting disclosures** — a different horizon, different signal construction and different mechanism from a post-publication decay/cost audit. McLean–Pontiff appears in ~10 pool records only as a *literature citation*, never as a source identity for a zoo-wide audit record.

## Economic mechanism

### Source-reported

The author argues three forces jointly destroy the published cross-sectional directional zoo for a participant who pays costs (§1): (i) **post-publication crowding decay** — disclosure attracts arbitrage capital and halves the premium (cited: McLean & Pontiff 2016); (ii) **multiple-testing inflation** — with hundreds of attempts many predictors clear the journal `|t|>2` bar by chance (cited: Harvey, Liu & Zhu 2016, whose `|t|>3` hurdle the paper adopts); (iii) **transaction costs on high-turnover portfolios** — equal-weight decile long-shorts rebalance monthly and are the most expensive academic portfolios to trade (cited: Novy-Marx & Velikov 2016). The paper pre-registers four hypotheses in §1 and reports all four *Confirmed*: H1 most published anomalies do not survive out-of-sample net of costs, survivor = low-turnover quality/profitability; H2 the `|t|>2` bar fails multiple testing and the premium decays post-publication (53% decay); H3 turnover and costs, not signal, decide survival (30 bp/month halves the survivors); H4 on the author's own recent data classic directional factors are dead net of cost — only reversal (liquidity provision) and crypto short-horizon trend pay.

### Research interpretation

The falsifiable mechanism is **cost-and-crowding filtration, not directional forecasting**: the hypothesis is that most of the cross-sectional directional premium is a selection/publication artifact whose *survival* is determined by turnover × cost rather than by predictive strength, so that a survivor set should be tiny, stable, and concentrated in the **cheapest-to-hold** premium (quality/profitability). Component roles as normalized:

```text
Audit universe (tested object): 212 published predictors, monthly EW-decile long-short returns (OSAP) + Ken French canonical factors
Regime/decay filter:            in-sample (original study window) vs out-of-sample (strictly post-sample-end) mean return and t-stat
Significance filter:            full-sample |t|>3 (multiple-testing hurdle) instead of the publication |t|>2 bar
Cost filter:                    flat monthly cost subtracted from OOS mean, swept 0 / 30 / 60 bp per month
Recency filter:                 recent decade (year >= 2015) Sharpe vs the author's +0.3 floor
Endorsed survivors:             (a) low-turnover quality/RMW (published factor returns), (b) short-term reversal on own data
                                (mechanism delegated to sibling Paper 5 record), (c) crypto 30-day momentum on own data
```

Do not assume every component contributes alpha; the audit itself is the claim, and each endorsed survivor remains `unproven` until independently tested (see Falsification plan).

## Signal

The source specifies an **audit procedure plus three endorsed survivor constructions**; it is not a single entry/exit strategy. Normalized as follows.

**Part A — the audit (authoritative, OSAP + Ken French), source-reported unless marked:**

- **Formation timestamp:** OSAP returns are monthly, month-end `DatetimeIndex` (source-reported, `research/paper4_data_profile.md`); French factors monthly. Timezone not stated for the equity files → `data gap` (US equity month-end convention implied, not asserted).
- **Windows:** for each predictor, in-sample = original study window years taken from `oap_signaldoc.csv` (`samplestart`/`sampleend`); out-of-sample = `year > sample_end`; recent decade = `year >= 2015` (source-reported (code), `scripts/18_factor_zoo_audit.py` L54–57).
- **Inclusion filters (source-reported (code)):** predictor series must have ≥36 total monthly observations, ≥24 in-sample months, and ≥24 out-of-sample months (same script, L48, L57). The dataset holds **212 predictor columns** (`1188 months × 212 predictors, 1926-01..2024-12`); **the exact per-test `n` actually used lives in `experiments/paper4_zoo_audit.json`, which is not in the repository** → the paper's phrase "across the 212 predictors" is dataset size; per-test `n ≤ 212` is `data gap`.
- **Statistics:** monthly t-stat = `mean / std * sqrt(n)` — **no HAC/Newey–West or autocorrelation correction** (source-reported (code), L28–30). Annualized Sharpe = `mean/std*sqrt(12)` (L23–25). McLean–Pontiff decay = `1 − mean(OOS)/mean(IS)` (L70).
- **Cost rule:** for `c ∈ {0.0, 0.003, 0.006}` (i.e. 0 / 30 / 60 bp per month), a predictor "survives" when `mean(OOS) − c > 0` — a **flat monthly cost on the return, not a turnover-measured cost** (source-reported (code), L71–73; explicitly acknowledged as illustrative in §6).
- **Floor/hurdles (author's chosen bars, source-reported as author choices):** `|t|>3` full-sample and OOS; "+0.3-Sharpe mean-reversion floor" applied to recent-decade Sharpe (§3; `FLOOR = 0.3`, `scripts/17_equity_zoo_core.py` L23).

**Part B — the author's own-data factors (walk-forward cross-sectional long-short), source-reported unless marked:**

- **Signal lag / no look-ahead:** every signal is shifted one trading day before being applied to the next day's return (§2; `alpha_research/factors/equity_zoo.py` module docstring and `ls_backtest` `S = sig.shift(1)`).
- **Equity signals (FnSpID daily panel):** momentum 12-1 = rolling 231-day sum of log returns shifted 21 days (`sig_momentum(lb=252, skip=21)`); short-term reversal = negative rolling 21-day sum of log returns (`sig_st_reversal`); low-vol = negative rolling 60-day standard deviation (`sig_low_vol`); news sentiment follow/contrarian = ± rolling 5-day mean of the FnSpID daily sentiment field (`sig_sentiment`, `sign=+1/−1`).
- **Crypto signals (daily, UTC):** momentum 30d = rolling 30-day sum of log returns; reversal 7d = negative rolling 7-day sum of log returns (source-reported (code), `scripts/17_equity_zoo_core.py` L64–65).
- **Portfolio construction:** cross-sectional **dollar-neutral long-short**, gross exposure 1.0 (0.5 long / 0.5 short, equal-weighted within leg); longs = signal ≥ quantile `1−q`, shorts = signal ≤ quantile `q`, with `q = 0.30` (equity) and `q = 0.33` (crypto) — the paper describes this as "top vs bottom tercile" (§3); equity uses 0.30 (source-reported (code), `ls_backtest`).
- **Rebalance cadence / parameters:** weights recomputed every `rebal` trading days — **5 trading days for equity, 7 days for crypto** — and held (forward-filled) in between; a rebalance is skipped when fewer than 20 ranked names exist (equity code) (source-reported (code)); the paper does not state cadence → the cadence above is from the pinned code.
- **Holding period / exit / re-entry:** no explicit exit, stop or holding-period rule — positions are re-struck at each rebalance and persist until the next one; maximum holding ≈ rebalance interval. There is no discretionary entry/exit logic to reconstruct.
- **Look-ahead hygiene in the audit:** "OOS" begins strictly after the published sample-end year so it is genuinely post-discovery; own-data factors are walk-forward with a one-day lag (§2).
- **Underspecified:** exact rebalance calendar/roll convention, tie-handling for equal quantile values, universe reconstitution rule for the crypto "top-30" (by what metric, how often), and the news-sentiment field's vendor definition are **not stated in source** → `underspecified`.
- **Labeling statement:** every operational parameter above is **source-reported** (from `docs/paper4.html` or the pinned code files named inline). **No Scout-proposed entry/exit, filter, stop or sizing rule was introduced anywhere in this record** (`research-proposed: none`); the only Scout-authored operational choices are the pre-declared falsification thresholds, each labeled `research-defined` in the Falsification plan.

## Required data

- **Part A universe/data (source-reported, `research/paper4_data_profile.md` + `configs/data_sources.yaml`):** Chen–Zimmermann **Open-Source Asset Pricing** release **202510 (v2.00, Oct-2025)**, files `PredictorLSretWide.csv` + `SignalDoc.csv` — monthly **gross** equal-weight-decile long-short returns for **212 predictors, 1926-01..2024-12**, decimal units, ~31% NaN by design (staggered predictor start dates; 27 predictors reach back to 1926); signaldoc classifies `Predictor = 212 / Placebo = 114 / Drop = 5`. WRDS/CRSP credentials were **not** used (returns-only route). **Ken French** monthly factor library, **1203 months × 9 factors, 1926-02..2026-04** (5-factor file starts 1963-07; momentum 1927-01; ST reversal 1926-02; LT reversal 1931-01), decimal, built from the 202604 data vintage per file preambles.
- **Part B equity data:** proprietary **FnSpID** daily adjusted-price + sentiment panels, path `/apps/jepa-trader/data/raw_fnspid/` (`prices_panel.parquet`, `sentiment_panel.parquet`, ~9.0 GB, ~7,697 files per `configs/data_sources.yaml`); universe = names with ≥60% daily coverage since 2016-01-01, daily returns clipped to ±50% (winsorization) — **coverage-based survivorship filter applied by construction** (source-reported (code)); **the vendor, listing rules and constituent history of FnSpID are `not stated in source`** → `data gap`.
- **Part B crypto data:** `*_spot1d.parquet` daily spot closes loaded by `alpha_research/factors/carry.py::load_spot_returns()` from `/apps/alpha-research/data/funding/` — the **Binance USD-M perpetual funding backfill + matched spot** build documented in `configs/data_sources.yaml` (built by `scripts/11_backfill_funding.py`, "228 perpetuals", used for Paper 2, 2023→2026). Paper §2 reports the panel as "**top-30 crypto daily panel (2023–2026)**"; the top-30 selection/reconstitution rule and whether every symbol is Binance spot are **not stated in source** → `data gap`.
- **Sample windows as reported:** OSAP 1926–2024 (audit OOS tail ends 2024-12), recent decade 2015–2024 for anomalies, French factors "through 2026" (§2) but reported as "2015–2025" in §4.3 (window-label ambiguity, see Limitations); own-data equity results labeled **2016–20** in the §4.4 table, own-data crypto **2023–26**.
- **Point-in-time / availability:** per-predictor sample start/end taken from the signaldoc (original study windows); OOS strictly after sample-end; one-day signal lag for Part B (§2). Revision policy for the sentiment field and for French factor vintages → `not stated in source`.
- **Missing data:** OSAP NaNs are dropped per predictor (`dropna`) with minimum-length filters (source-reported (code)); no imputation asserted; no explicit stale/suspension/halt handling → `not stated in source`.
- **Funding/fee/spread needs:** none used in Part A; Part B crypto is **spot** returns only — no funding, borrow, or options data requested by the signal → see Execution assumptions for what that leaves unmodeled.

## Execution assumptions

- **Signal-to-order timing:** signal formed on day *t*−1 close, applied to day *t* return (Part B, one-day shift); Part A is a return-series audit with no order timing at all (source-reported).
- **Order type / fill model / latency / partial fills:** **not stated in source** — no market-vs-limit choice, no fill model, no latency model, no partial-fill or failed-trade handling anywhere in the paper or the inspected scripts → `not stated in source`.
- **Costs — Part A:** flat monthly cost of **0 / 30 / 60 bp** subtracted from each predictor's OOS monthly mean; the paper explicitly states OSAP returns are **gross**, that per-predictor turnover was **not measured**, and that the flat cost is "illustrative (though conservative — these are the most expensive portfolios to trade)" (§6). **No spread, slippage, market impact, borrow fee, or short-availability model is applied** → net figures are a **lower-bound-style sensitivity, not an executable net**.
- **Costs — Part B:** one-way turnover cost of **10 bp** charged on `Σ|Δweights|` at each rebalance (equity and crypto alike; "net of 10 bp/side", §3; `cost_bps=10.0` in `ls_backtest`). A momentum cost sweep at 0/5/10/20 bp exists in code for the equity momentum factor only; its reported values are in `experiments/paper4_ourdata.json` → **absent from the repository** → `data gap`.
- **The author's own cost caveat:** the equity short-term reversal survivor is "Equal-weight, small-cap-tilted, high-turnover; 10 bp/side is optimistic for small-caps — properly the subject of Paper 5" (§4.4 footnote).
- **Borrow / shorting:** dollar-neutral shorts are constructed at will with **no borrow availability, borrow fee, recall risk or hard-to-borrow filter modeled** (equity or crypto) → `not stated in source`; on crypto the short leg is **spot** (no perp funding, no borrow) per the loader.
- **Leverage / margin:** gross exposure normalized to 1.0; no leverage, margin or financing constraints modeled → `not stated in source`.
- **Impact / capacity:** **no volume, ADV, participation-rate or capacity analysis anywhere in the paper** → `data gap`; equal-weight decile construction tilts to smaller names, which the author concedes are the most expensive to trade (§2).
- **Funding:** not applicable to Part A; not modeled for the Part B crypto short book (spot-only returns) → funding drag on a real perp-implemented version is `not stated in source`.

## Evidence

### Source-reported

All figures below trace to the pinned `docs/paper4.html` (SHA-256 `06ddabcf…cef6`) section noted in brackets, or to the pinned supporting files where marked; **none has been independently reproduced**. Asset class is US listed equities (Part A + Part B equity) and spot crypto (Part B crypto) — this record is **not** crypto evidence except where explicitly labeled crypto.

1. **Post-publication decay (§Abstract, §4.1, Figure 1):** mean long-short return across the predictor set falls **0.69%/month in-sample → 0.32%/month out-of-sample, a 53% decline**; **86%** stay positive OOS; only **34%** keep `|t|>2` OOS and **18%** keep `|t|>3` OOS. Author labels this "almost exactly McLean–Pontiff".
2. **Multiple-testing hurdle (§Abstract, §4.2, Figure 2):** only **61%** of predictors clear `|t|>3` full-sample, **median |t| = 3.4**; **18%** keep `|t|>3` out-of-sample; **42%** beat the +0.3 Sharpe floor over the recent decade; **3%** are statistically strong (`|t|>3`) in the most recent decade; **median recent-decade Sharpe = 0.22**.
3. **Cost cascade (§4.2, Figure 3; sweep definition §3):** fraction with positive OOS returns **86% (0 bp) → 43% (30 bp/month) → 19% (60 bp/month)**; "43% survive a 30 bp/month cost" — i.e. a realistic flat monthly cost removes more than half the sign-positive set.
4. **Canonical Fama–French factors, 2015–2025 (§4.3, Figure 4), Sharpe:** **market 0.77**, **RMW/profitability 0.39**, momentum 0.25, **HML/value −0.05**, **SMB/size −0.20**, **CMA/investment −0.13**, "reversal −0.04" (the paper does not say which French reversal series; data file carries both ST_Rev and LT_Rev → exact series identity `data gap`). Only market and quality clear the +0.3 floor.
5. **Own-data cross-section, net of 10 bp/side (§4.4 table), net / gross Sharpe:** equity momentum 12-1 (2016–20) **−0.01 / 0.03** (dead, not even positive gross); equity low-vol (2016–20) **−0.92 / −0.91**; equity news-sentiment contrarian (2016–20) **−0.46 / −0.43**; equity short-term reversal (2016–20) **+0.86 / 1.15** ("liquidity provision; cost-fragile\*" per the table's own footnote); **crypto momentum 30d (2023–26) +0.53 / 0.61**; crypto reversal 7d (2023–26) **−0.47 / −0.26**.
6. **Pre-registration (§1):** H1–H4 stated before results and reported *Confirmed* (verbatim claims quoted in Economic mechanism). This is author-asserted pre-registration within the document; there is no timestamped registry → pre-registration strength `unproven`.
7. **Dataset/vintage facts (source-reported, `research/paper4_data_profile.md`):** OSAP `1188 months × 212 predictors, 1926-01..2024-12`, gross; signaldoc `331 rows × 28 cols` (`Predictor 212 / Placebo 114 / Drop 5`); full-sample mean annualized predictor long-short return **6.0% (median 5.2%)**, mean annualized Sharpe **0.51 (median 0.45)**; French library `1926-02..2026-04`; OpenAP release pinned **202510 (v2.00, Oct-2025)**; Google-Drive quota incident forced the `PredictorLSretWide.csv` route; the net-of-cost half "must impose a cost model" because the file itself carries no cost adjustment.
8. **Code-verified parameters (source-reported (code), pinned head):** monthly t with no HAC (`18_factor_zoo_audit.py` L28–30); decay `1 − OOS/IS` (L70); cost test on flat monthly cost `{0, 0.003, 0.006}` (L71–73); recent decade `year >= 2015` (L56); `FLOOR = 0.3`; equity `q=0.3, rebal=5, cost_bps=10`; crypto `q=0.33, rebal=7, cost_bps=10`; equity momentum `lb=252, skip=21`; reversal window 21 days; low-vol window 60 days; sentiment window 5 days; crypto momentum/reversal windows 30/7 days; crypto Sharpe annualized with `ppy=365`; annualized Sharpe helpers drop exact-zero return days (`equity_zoo.py` `ann_sharpe`).

### Independently reproduced

`Not independently reproduced.` In this run the Scout verified only artifact integrity (three copies of `docs/paper4.html` byte-identical, SHA-256 `06ddabcf…cef6`, 19,718 bytes) and read the full text plus the pinned audit/core/factor/data-profile files. No OSAP or French data were downloaded, no script was executed, and no result JSON exists in the repository to compare against — the published figures remain **third-party reported results**.

### Negative evidence

- **The source's own headline is negative evidence against directional alpha:** ~53% post-publication decay; only 61% clear `|t|>3` full-sample; 18% keep `|t|>3` OOS; median recent-decade Sharpe 0.22 (below the author's own 0.3 floor); only 3% statistically strong in the recent decade; costs cut the positive-OOS fraction 86% → 43% → 19% (0/30/60 bp) (§4.1–4.2).
- **Canonical premia are dead or marginal 2015–2025** in the source's own numbers: value −0.05, size −0.20, investment −0.13, reversal −0.04, momentum 0.25 (all below the 0.3 floor) (§4.3).
- **Own-data failures:** momentum 12-1 net −0.01 (fails even gross), low-vol −0.92, sentiment contrarian −0.46, crypto 7d reversal −0.47 (§4.4 table).
- **Internal construction tension to keep open:** FF "reversal" is reported at **−0.04** (§4.3) while the author's own short-term reversal is **+0.86 net** (§4.4) — same label, different construction, frequency and universe; the source reconciles them by re-classifying its own reversal as a *liquidity-provision* premium delegated to Paper 5, but the FF number and the in-house number are **not interchangeable evidence**.
- **Cost realism is explicitly weak in the direction that matters:** the only equity survivor is flagged cost-fragile by the author ("10 bp/side is optimistic for small-caps", §4.4 footnote); Part A's flat monthly cost ignores per-predictor turnover (§6).
- **No multiple-testing-adjusted survivor count, no deflated Sharpe, no capacity/ADV test, no borrow-cost test, no significance test on any of the §4.4 Sharpe differences** → the survivor ranking is descriptive, not statistically arbitrated → `data gap`.
- **Reproducibility wall:** proprietary FnSpID panel, raw OSAP/French files and both result JSONs are absent from the repository (§Provenance) → no external party can re-derive the numbers as published.
- **None of this is a failed replication of the source:** no independent replication was attempted, so no replication failure exists; the negative evidence above is the source's own reported content plus the Scout-identified gaps.

## Falsification plan

**Source-reported thresholds (author's, not ours):** pre-registered H1–H4 (§1); survival bars = `|t|>3` full-sample and OOS, `+0.3` recent-decade Sharpe floor, flat cost ladder 0/30/60 bp/month (§3).

**Research-defined tests (Scout-proposed; thresholds chosen by us, not by the source — each specifies data, sample, metric, threshold, action):**

1. **Decay-magnitude replication (research-defined).** Data: frozen OSAP 202510 `PredictorLSretWide.csv`. Recompute in-sample vs OOS mean per the §3 windows. **Threshold:** `|decay − 53%| > 15pp` ⇒ reject the *magnitude* claim (retain direction only); `< 10pp` ⇒ support. Action on failure: record the decay as direction-only evidence; no re-tuning of windows.
2. **Quality-survivor net test (research-defined).** Data: Ken French RMW and the cost ladder. **Threshold:** RMW Sharpe over 2015–2025 **≤ 0.30 after a flat 30 bp/month cost**, or ≤ 0 ⇒ reject "lone robust survivor is low-turnover quality". Action: the endorsed survivor is downgraded to unproven and cannot be used as a candidate anchor.
3. **Flat-cost vs measured-turnover audit (research-defined).** Data: rebuild EW-decile LS with per-predictor monthly turnover (Novy-Marx–Velikov style). **Threshold:** difference between the flat-cost and turnover-based "fraction positive OOS" at the same nominal cost **> 10pp** ⇒ the paper's cost model is miscalibrated and its 43%/19% figures are withdrawn (either direction). Action: re-derive all cost-cascade percentages before any use.
4. **Multiple-testing robustness (research-defined).** Data: the 212 full-sample t-stats. Apply Benjamini–Hochberg at `q = 0.10` (and a deflated-Sharpe check). **Threshold:** fewer than **50%** of the 61 `|t|>3` survivors remain ⇒ the `|t|>3` bar itself is too lax and the paper's survivor set is overstated. Action: report survivors only under the stricter correction.
5. **Post-2020 own-data window (research-defined).** Data: an equity panel with daily prices + sentiment for **2021-01-01→2026-08-31** (FnSpID or an open substitute, flagged as a substitution). Same 10 bp/side, same rebalance. **Threshold:** short-term reversal net Sharpe **< 0.30** or **≤ 0** ⇒ the equity survivor does not survive its own out-of-window test. Action: kill the equity survivor claim.
6. **Crypto trend cost ladder (research-defined).** Data: the top-30 spot panel 2023–2026, cost ladder **5/10/20 bp per side**, plus a perp-implemented variant adding real funding and borrow. **Threshold:** 30d-momentum net Sharpe **≤ 0 at 20 bp/side**, or the perp variant dropping **> 40%** below the spot variant ⇒ reject the crypto survivor / portability claim. Action: crypto trend recorded as cost-fragile, not portable.
7. **Regime split (research-defined).** Split the recent decade into **2015–2019 / 2020–2024 / 2025–2026**. **Threshold:** quality (RMW) positive Sharpe in **fewer than 2 of 3** subperiods ⇒ regime-fragile survivor, downgrade confidence. Action: no deployment-facing use of the survivor ranking.
8. **Placebo / control (research-defined).** Shuffle each predictor's monthly series against calendar time (circular shift ≥ 60 months), re-run the full survival cascade 500×. **Threshold:** placebo median "recent-decade Sharpe > 0.3" share **within 5pp of the real 42%** ⇒ the audit's thresholds do not discriminate signal from noise. Action: thresholds must be tightened before any conclusion.
9. **Competing-explanation control (research-defined).** For the two endorsed survivors (RMW, short-term reversal), regress long-short returns on size, investment, turnover and illiquidity factors plus the market. **Threshold:** residual alpha **t < 3** or magnitude **halves** ⇒ the "survivor" is a beta/style artifact, not idiosyncratic alpha. Action: reclassify as exposure, not alpha.

**On any failure:** results are reported as-is; parameters and windows are **not** retuned to rescue the hypothesis. The record stays `research-only / not-implemented / not-approved` regardless of outcome.

## Crypto portability

**`adapted`** — component-level, not global:

- **Crypto 30-day momentum (the one component the source itself demonstrates on crypto):** tested on the author's own **top-30 spot** daily panel, 2023–2026, net **+0.53** Sharpe at 10 bp/side (§4.4) — source-reported, spot only, **not** perpetual. Because the source runs the mechanism in crypto markets, this component may not be called `direct`: venue coverage, the top-30 selection rule, cost calibration and the short-leg implementation are `not stated in source`/`data gap`, and 2023–2026 is a single post-2022 regime window.
- **Equity directional factors and the quality survivor:** **`unproven`** in crypto. Value/quality/size/momentum audits rest on *published equity factor returns* (OSAP/French); nothing in the source tests them on crypto assets. Any "quality survives net-of-cost in crypto" statement would be a **different mechanism requiring a new record**.
- **Crypto-specific risks for a port:** (i) the source's leg is **spot** — a perp-implemented dollar-neutral book adds **funding flows on both legs** and borrow/availability on the short side, none modeled; (ii) `rebal=7` with a UTC day-floor works on 24/7 data but the equity-derived 5-trading-day cadence and month-end audit windows do **not** translate to 24/7 candle boundaries; (iii) venue fragmentation — the panel derives from a single Binance-matched build, so cross-venue price dispersion, index/mark price and withdrawal/custody risk are untested; (iv) crypto cross-sections are ~30 names, so decile/tercile breakpoints are coarse and single-name shocks dominate; (v) listing/survivorship — a "top-30 today" universe applied historically leaks which coins survived; the source gives no reconstitution rule → `data gap`; (vi) crypto removes short-selling frictions that plague the equity zoo, which could move the audit's cost conclusion in **either** direction — untested.

## Limitations

Markers used: `underspecified`, `data gap`, `not independently reproduced`, `unproven`.

1. `not independently reproduced` — every performance figure is third-party reported; the repository ships code and documentation but **no raw data and no result JSONs** (`data/`, `experiments/` = `.gitkeep` only).
2. `data gap` — **flat** monthly cost in Part A instead of measured per-predictor turnover (author's own §6 concession); no spread/slippage/impact/borrow/latency/fill model anywhere.
3. `data gap` — no capacity, ADV or participation analysis; equal-weight decile tilt toward small/illiquid names makes the reported net an upper bound for size-constrained capital.
4. `data gap` — exact per-test `n` after the ≥36/≥24/≥24 filters is in an absent JSON; "212" is the dataset size, not a verified per-test count.
5. `data gap` — window-label ambiguity: §2 says French factors "through 2026", §4.3/Figure 4 label the window "2015–2025", while `18_factor_zoo_audit.py` filters `year >= 2015` over data spanning to **2026-04**; the precise end month behind the 0.77/0.39/etc. Sharpes is therefore not unambiguously resolvable from the source.
6. `data gap` — §4.3's "reversal −0.04" does not identify the French series (ST_Rev vs LT_Rev both present in the data file).
7. `underspecified` — statistical machinery: monthly t with **no HAC correction** (code), no multiple-testing-adjusted survivor set, no deflated Sharpe, no confidence intervals or significance tests on any reported Sharpe difference (including the survivor ranking).
8. `underspecified` — Part B execution: no order type, fill model, latency, borrow/short availability, or reconstitution rule; equity survivor explicitly cost-fragile per the author's own footnote.
9. `data gap` — own-data **equity window ends 2020** (§6); the code's docstring says "2016-2025" and its subperiod table includes a 2023–2025 bucket, while the paper's results table labels equity rows "(2016–20)" — the two disagree; we take the paper's reported window and flag the conflict. There is **no post-2020 own-data evidence** for the equity survivors.
10. `data gap` — source quality: single-author, non-peer-reviewed blog post; pre-registration is asserted inside the document with no external timestamp; proprietary FnSpID data blocks third-party reproduction.
11. `unproven` — the endorsed survivors (quality, short-term reversal, crypto 30d momentum) are **rankings from a descriptive audit**, not validated tradable strategies; the author himself writes that quality "deserves a dedicated, cost-and-capacity-aware follow-up" (§6).
12. `data gap` — coverage-based survivorship filter (≥60% daily coverage since 2016) and ±50% return winsorization applied to the equity panel by construction (code); effect on the reversal/momentum results is not quantified.

## Implementation status

`implementation_status: not-implemented`. Nothing from this record has been implemented in our research stack: no strategy was coded, no Qlib (or any) backtest was run, no signal was computed on our data, and no Paper/Testnet/Live workflow was touched. The Scout's only actions this run were repository sync, primary-source retrieval and checksum verification, full-text/code reading, deduplication search, and this record's commit. This record does not imply Qlib full-backtest validation, survivor status, or any trading approval.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record in the staging repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. Any later adoption must be an explicit, separately reviewed decision based on this record plus current sources.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — canonical strategy-research record specification used to normalize this capture.

Nearest records in this repository (linked by path, not Wiki pages; no other Wiki page identities were verified for this topic): `reviving-anomalies-expected-net-return-double-sort-1n-implementable-2026-09-23.md` (constructive ML net-return anomaly allocation — different mechanism), `anomaly-pre-release-drift-predicted-signal-decile-portfolios-2026-09-23.md` (pre-release drift — different horizon/mechanism), `vol-conditional-liquidity-provision-reversal-micro-price-execution-overlay-2026-09-23.md` (same author's Paper 5, to which this paper delegates its reversal survivor), `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11.md` (Paper 2), `crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12.md` (Paper 3), `g10-fx-carry-fx-value-energy-roll-yield-net-cost-audit-2026-09-23.md` (Paper 6), `autonomous-llm-research-stablecoin-flow-carry-trend-death-2026-09-19.md` (Paper 8), `two-engine-llm-intrinsic-valuation-consensus-margin-of-safety-forward-ic-2026-09-23.md` (Paper 9), `crypto-volatility-risk-premium-variance-swap-estimator-fragility-decay-2026-09-12.md` (Paper 1).

## Sources

1. Bryan Vine. *"The Cost of Direction: A Net-of-Cost Audit of the Directional Anomaly Zoo."* Alpha Research, Paper 4, byline **June 17, 2026**. https://bryanvine.github.io/alpha-research/paper4.html — primary source, read in full (Abstract, §1–§6, References) on **2026-09-23**. Every quantitative claim in this record traces to §2, §3, §4.1, §4.2, §4.3, §4.4 (table + footnote), §6, or the supporting files listed in entry 2.
2. Bryan Vine. `alpha-research` repository. https://github.com/bryanvine/alpha-research — file `docs/paper4.html` at full commit `655e8d4f1ff4b41006e05931d078a722af1e732e` (2026-06-17T00:34:13Z, *"Paper 4: The Cost of Direction — a net-of-cost audit of the directional anomaly zoo"*) and at head `17b8b5e1c79af194f733544517d82e3cf12c2259` (2026-08-23); both byte-identical to the published page (SHA-256 `06ddabcfb50247fad9bb1c5a8049ff7bbf83afaa50a2659d9d6bb7e399dfcef6`, 19,718 bytes, verified 2026-09-23). Supporting paths directly inspected at this head: `scripts/18_factor_zoo_audit.py`, `scripts/17_equity_zoo_core.py`, `scripts/16_fetch_factor_zoo.py`, `scripts/43_paper4_figures.py`, `alpha_research/factors/equity_zoo.py`, `alpha_research/factors/carry.py`, `research/paper4_data_profile.md`, `configs/data_sources.yaml`.
3. Underlying data sources **as declared by the source** (not accessed or verified by the Scout): A. Y. Chen & T. Zimmermann, *Open Source Cross-Sectional Asset Pricing* (Critical Finance Review; openassetpricing.com), release `202510`; K. French data library factor files (5-factor, momentum, ST/LT reversal, through 2026-04 in the author's copy); proprietary FnSpID daily price/sentiment panels; author-local Binance USD-M funding + matched spot backfill (`scripts/11_backfill_funding.py`).
4. Literature the source itself cites for its mechanism (listed for provenance only — claims are the source's): McLean & Pontiff (2016, *JF* 71(1)); Harvey, Liu & Zhu (2016, *RFS* 29(1)); Hou, Xue & Zhang (2020, *RFS* 33(5)); Novy-Marx & Velikov (2016, *RFS* 29(1)); Fama & French (2015, *JDE* 116(1)); Chen & Zimmermann (2022, *CFR*).
