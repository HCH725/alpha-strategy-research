---
schema: strategy-research-record-v1
title: "Leakage-Controlled LLM Macro-Analog Ranking of Seven U.S. Equity Style Factors with Real-Time CPI Nowcast (arXiv:2606.22719)"
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equity-factors
  - factor-timing
  - macro-nowcast
  - llm
  - retrieval-augmented
  - leakage-control
  - walk-forward
status: research-only
confidence: medium
source_as_of: 2026-06-21
sources:
  - "Mao Guan, Qian Chen, 'Leakage-Aware Benchmarking of LLM Forecasting: Real-Time Nowcasts as the Decision-Time Input for Macro Factor Ranking', arXiv:2606.22719v1 [q-fin.ST], submitted 21 Jun 2026. https://arxiv.org/abs/2606.22719"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Leakage-Controlled LLM Macro-Analog Ranking of Seven U.S. Equity Style Factors with Real-Time CPI Nowcast (arXiv:2606.22719)

## Provenance

- **Primary source:** Mao Guan and Qian Chen (both listed in the paper as *Affiliation: Independent Researcher*; corresponding author email shown in the paper header: `guanmao771@gmail.com`), *"Leakage-Aware Benchmarking of LLM Forecasting: Real-Time Nowcasts as the Decision-Time Input for Macro Factor Ranking"*, arXiv preprint `arXiv:2606.22719v1 [q-fin.ST]`, **v1 submitted Sun, 21 Jun 2026 23:36:04 UTC** (single version; submitter shown as Mao Guan). DOI: [10.48550/arXiv.2606.22719](https://doi.org/10.48550/arXiv.2606.22719) (arXiv-issued DOI via DataCite). Stable URL: [https://arxiv.org/abs/2606.22719](https://arxiv.org/abs/2606.22719). Full text HTML read by Scout: [https://arxiv.org/html/2606.22719v1](https://arxiv.org/html/2606.22719v1).
- **Publication status (source-reported, checked on the arXiv abs page 2026-09-22):** Comments field reads *"10 pages, 4 figures. Accepted at the ICML 2026 Workshop on AI Forecasting (Forecasting as a New Frontier of Intelligence). Non-archival. OpenReview: https://openreview.net/forum?id=mi8QiWomm3"*. Subjects: **Statistical Finance (q-fin.ST); Artificial Intelligence (cs.AI)**. **No `journal-ref` and no non-arXiv DOI are listed → peer-review status beyond the non-archival workshop acceptance is `not stated in source`.** License on the HTML rendering: **CC BY 4.0**.
- **Data as-of dates reported by the source:** Kenneth French Data Library accessed 2026-05-13; AQR public factor library (BAB, QMJ) accessed 2026-05-13; Cleveland Fed daily CPI nowcast archive **frozen snapshot 2026-05-13**. Evaluation window ends 2026-03-31.
- **Primary-source checksum performed 2026-09-22:** abs page **and** full v1 HTML were opened directly. Author list, title, version/date, Comments/Subjects/license, sample window, universe, metric definitions, cost treatment (Setup, Method, Results Table 3 caption, Discussion "Deployability", Appendix D.3 / Figure 4) and every number below were read from that v1 text. No secondary summary was used for any strategy rule or empirical claim.
- **Repository deduplication audit (2026-09-22, ripgrep across all `*.md` in this repository plus `coverage_manifest.csv`):** zero hits for `2606.22719`, the exact paper title, `Mao Guan`, `Cleveland Fed`, `nowcast archive`, `macro-analog`, `macro analog`, `investment clock`, `Knotek`. Adjacent records reviewed and **not** duplicates:
  - `continuous-macro-timing-growth-defensive-style-allocation-2026-09-02.md` (arXiv:2605.20636, Xiong) — same broad family (macro-conditioned style rotation) but a **materially different mechanism and construction**: a deterministic continuous `softplus` composite of four observed macro/market signals timing **two** style baskets (growth vs defensive) with 10 bps costs, versus this record's **retrieval of ≥12-month-embargoed historical macro analogs + LLM critic rule + LLM actor scores ranking seven style factors** with a real-time CPI nowcast as the decision-time input. Different source identity, different signal construction, different universe (2 baskets vs 7 factors).
  - `agentic-ai-nowcasting-stock-returns-llm-web-search-2026-09-04.md` — LLM web-search **stock-level** nowcasting; different mechanism (single-name return nowcast vs cross-factor rotation) and different source.
  - `causal-knn-predictive-flow-leakage-falsification-2026-09-13.md` — kNN leakage forensics on a crypto 4H indicator; different source, market and mechanism.
  - `cross-sectional-centering-price-offset-nuisance-rank-ic-2026-09-14.md` — normalization ablation driving **intraday stock-level rank IC** on CSI 300; different task, universe and mechanism.
- This repository has no record that shares this source identity; no second record for this source exists.

## Economic mechanism

### Source-reported

The paper's central claim is methodological first, alpha second:

1. **Leakage channel.** The CPI value labelled as month *t* is typically published by the BLS about **ten days after** the month-end decision date, so a walk-forward backtest that conditions on it consumes roughly ten days of look-ahead (source-reported, §1; Bailey & Lopez de Prado 2014; Harvey et al. 2016). The paper's fix is to substitute the **Cleveland Fed daily inflation nowcast** queried at date *t* for the unreleased current-month inflation value, and to shift FRED CPI and unemployment by one calendar month.
2. **Rotation channel.** A macro-analog retrieval module retrieves historical macro states (investment-clock dimensions, Greetham & Hartnett 2004), a **critic LLM** compresses the retrieved analogs into one tactical rule, and an **actor LLM** maps the current state plus a rolling buffer of recent rules into scores for **seven U.S. equity style factors**. The stated hypothesis is that the *decision-time macro state* (above all, real-time inflation) carries information about the **relative** next-month performance of value/quality/beta/momentum/size factors, and that historically similar macro states foreshadow that relative ordering.
3. **Attribution channel (source-reported and deliberately deflationary).** The paper attributes much of the signal to *real-time inflation information plus macro-similar retrieval*, not to the LLM: "the macro-similar retrieval step does much of the median-IC work, while the LLM pipeline appears to improve the months in which the model commits most strongly to top and bottom factors" (§4).

### Research interpretation

Two separable falsifiable hypotheses, which the source's own ablation already partially adjudicates:

- **H-macro (stronger prior):** a *leakage-clean, decision-time* macro state — lag-shifted FRED series plus a same-day CPI nowcast — produces a **positive cross-factor rank IC** for next-month market-adjusted factor residual returns, and a macro-analog (kNN) retrieval recovers most of it. Source evidence supports direction but not significance (median IC +0.154/+0.161; mean-IC 95% CI includes zero; permutation p = 0.11/0.44).
- **H-LLM (weaker prior):** an LLM critic/actor adds **nonlinear interaction beyond analog averaging**, concentrated in the extreme ranks that drive a top/bottom long-short allocation. Source evidence is suggestive only (mean IC +0.131 vs +0.070; long-short Sharpe 0.71 vs 0.29), and the extreme-overlap diagnostic in Table 6 is **mixed** (kNN slightly higher average extreme overlap).

Economic story for why a channel could exist: inflation surprises reprice discount rates differently across long-duration growth, value, profitability, low-beta and momentum exposures within the same month, and the repricing is visible in *relative* factor returns even after removing market beta. That story is the source's framing, not an established fact; the paper explicitly declines to call the result a discovery.

Component roles (hybrid structure):

```text
Regime / information fix: lag-shifted FRED macro + Cleveland Fed same-day CPI nowcast (leakage control)
Retrieval: top-K=4 macro analogs from [1990-04, t-12m], cosine on 4-D z-scored state vector
Confirmation / rule synthesis: critic LLM writes ONE tactical rule, appended to a rolling 6-rule buffer
Primary signal: actor LLM scores 7 style factors in [0,1]; cross-sectional rank is the signal
Allocation sanity check (not a trading claim): long top-2 / short bottom-2 factors, monthly, 5 bps per unit weight change
```

## Signal

All items below are **source-reported** unless flagged.

- **Formation timestamp:** month-end *t*; 36 monthly decisions from **2023-04-30 through 2026-03-31** (Setup, "Walk-forward"). Decision inputs are defined as observable at *t*. **Timezone / clock convention for "month-end" is `not stated in source`** (the inputs are U.S. FRED / Cleveland Fed / BLS series, but the paper does not declare a timezone; no timezone is inferred here).
- **Label:** cross-sectional rank of the market-adjusted residual factor return `r_resid(f,t) = r(f,t) − β(f,t)·r_MKT(t)`, where `β(f,t)` is a **rolling 60-month OLS beta estimated strictly with data s < t** (Setup, "Label"). `MKT_RF` is **excluded from prediction** (Setup, "Factors").
- **Decision-time inputs:** FRED CPI YoY, CPI level and Unemployment **shifted by one calendar month**; the **daily Cleveland Fed CPI YoY nowcast queried at date t**; all other FRED market variables (e.g. term spread, VIX) "treated as observable at t without publication lag" (Setup). The LLM actor additionally receives **decision-time summaries of FOMC and CPI events from the past 30 days** (Setup / Figure 1); the construction and corpus of those summaries are `underspecified` in the paper body (the corpus is only referenced as an availability constraint on the 2023-04 start).
- **Lookback / retrieval:** candidate analog months satisfy `s ≤ t − 12 months` (≥12-month embargo) inside the pool `[1990-04, t−12m]`; `K = 4` (fixed ex ante to mirror the four investment-clock quadrants); cosine similarity on a **4-D z-scored state vector** = (growth pulse, inflation pulse, term spread, VIX pulse), where pulses are **6-month changes** and `growth pulse = −Δ6(Unemployment, shift 1)` (Method, "Monthly decision protocol"). Standardization is **expanding-window**, `z_u = (x_u − μ_≤u)/σ_≤u`, **no full-sample scaler**, and at least **24 non-null monthly observations** are required before a standardized state is computed (Appendix A).
- **Critic step:** the critic reads the analogs + current macro state and writes **one** tactical rule; the rule is **parsed deterministically into a Δ-vector** applied to the actor's seven scores; rules are appended to a **rolling buffer of the last 6** (Method). Worked source example (2023-04): *"raise HML by 0.15 and lower BAB by 0.15"*.
- **Actor step:** actor scores each of the seven factors in `[0,1]`; the cross-sectional rank of those scores is the monthly signal (Method, Figure 1).
- **Model / decoding:** both LLMs are **Qwen2.5-7B-Instruct**, **4-bit NF4** via bitsandbytes, **greedy decoding T = 0** (deterministic month-by-month) (Method, "Architecture").
- **Entry / exit / holding:** there is **no per-asset entry or exit rule**. The evaluable trade shape is the **allocation sanity check** (Table 3): **long the top-2 ranked factors and short the bottom-2, equal-weighted within each leg, monthly rebalanced, charged 5 bps per unit weight change**; turnover is the average monthly L1 weight change. The source states in the caption and in §5 that this is **"not a deployable trading strategy"** / **"not a trading claim"** — it exists only to test whether rank IC maps to non-trivial allocation value. **Holding period:** one month between rebalances. **The grossing / notional normalization of the two legs (e.g. ±0.5 vs ±1 vs 2/7) is `not stated in source`** — the L1 turnover figures alone do not identify it.
- **Parameters and their source:** `K = 4` (fixed ex ante by the authors to match the LLM retrieval protocol; a K-sweep is reported only as sensitivity, Table 5); embargo `≥12` months; buffer `6`; rule Δ `±0.15` in the two quoted examples; label beta window `60` months; bootstrap `10,000` resamples, `np.random.seed(42)`; permutation `10,000` sign-symmetric draws, seed 42 (Method / Appendix A / Reproducibility). **Prompt templates are `not in the paper` — the source says they "will be included in the public reproducibility package" (Appendix A) → `data gap`.**
- **Baselines (same decision-time constraint):** (i) nowcast-only ridge per factor on `[cf_nowcast_yoy, cf_nowcast_delta_6m]`; (ii) macro+nowcast ridge on the 6-feature decision-time vector with a scaler fit on the training period only; both trained on **≈110 pre-test months ending 2023-03**; (iii) **kNN macro analog** — the same `K = 4` cosine retrieval, but the output is the per-factor mean of the four analogs' realized next-month residual returns (no LLM). The paper states the apples-to-apples contrast is **LLM vs kNN**; the two ridges are a sanity check on a shorter training horizon.
- **Reproducibility status:** the source says it **will release** harness, prompts, per-month score parquets, the frozen Cleveland Fed nowcast archive, retrieved analog indices, the critic-rule log and the inference configuration (Reproducibility / Appendix A). **No package URL is given in the v1 text → `data gap` (release not verified by Scout).**

**Reconstructability verdict:** the ranking pipeline is reconstructable at the level of data sources, windows, embargo, metric and allocation rule; it is **`underspecified`** for byte-exact replication (prompt templates, event-summary corpus, leg normalization, timezone), so it must not be presented as fully reproducible evidence.

## Required data

- **Instrument / universe:** **seven U.S. equity style factor return series** — SMB, HML, RMW, CMA, UMD (Fama-French five-factor library + momentum), **BAB** and **QMJ** — plus `MKT_RF` used only for the label's market adjustment. **This is a factor-return universe, not a stock universe.** Source-reported per-source mapping: **BAB and QMJ from the AQR public factor library, accessed 2026-05-13**; the remaining factor series are attributed to the **Kenneth French Data Library, accessed 2026-05-13** — the exact French-library portfolio construction used for each of SMB/HML/RMW/CMA/UMD is `underspecified` (the paper cites the library, not a specific portfolio file).
- **Venue / market type:** U.S. equity style factors (published research series). Market type: cash equities factor exposures; **no derivatives, no crypto**.
- **Timeframe:** **monthly**, decision at month end, label for the following month.
- **Fields:** FRED CPI YoY, CPI level, unemployment (all lag-shifted one calendar month), term spread, VIX (other FRED market variables treated lag-free), **Cleveland Fed daily CPI YoY nowcast at date t** (archive frozen 2026-05-13), FOMC and CPI event summaries for the past 30 days, the seven factor returns and `MKT_RF`.
- **Point-in-time:** strict — lag-shifted FRED, same-date nowcast, ≥12-month retrieval embargo, expanding-window z-scores, rolling beta with `s < t`, ridge trained only on pre-test months. The source's own headline point is that substituting the nowcast removes a ~10-day look-ahead about realized CPI.
- **Timestamp / timezone:** decision dates are stated (2023-04-30 … 2026-03-31) but **timezone is `not stated in source`**; out-of-order-record handling is `not stated in source`.
- **Missing data:** the macro+nowcast ridge has **n = 34 instead of 36** because of two missing unemployment observations; the paper restricts all methods to the common 34-month subset for the qualitative LLM-vs-kNN comparison (Table 1 caption). A minimum of 24 non-null observations is required before standardizing a state (Appendix A). **No imputation is reported.**
- **Funding / fee / spread needs:** the only cost input is **5 bps per unit weight change** in the allocation sanity check (Table 3). **Commission, borrow for the short factor legs, financing, market impact, spread and slippage models are `not stated in source`** — the Discussion explicitly says deployable claims would require "transaction costs, financing, and capacity", which the paper does not model beyond the 5 bps charge.

## Execution assumptions

- **Signal-to-order timing:** month-end decision, monthly rebalance; **intra-month execution timing, order type, fill model and latency are `not stated in source`** (the sanity check is computed on published factor return series, so no order book is involved).
- **Costs (source-reported):** **5 bps per unit weight change**, charged against subsequent returns in Table 3 and Figure 4 ("Cumulative net return … monthly rebalanced, 5 bps per unit weight change"). Turnover (average monthly L1 weight change): **Full LLM 0.81, kNN 1.10, nowcast-only ridge 0.17, macro+nowcast ridge 0.82** (Table 3).
- **Explicit source disclaimer (§5 "Deployability"):** "The economic sanity check is intentionally simple and should not be interpreted as a deployable trading claim; deployable claims require accounting for transaction costs, financing, and capacity, all of which materially compress paper Sharpe ratios for academic factors."
- **Not stated in source:** leverage / margin, short availability and borrow cost for the shorted factor legs, participation or capacity limits, partial fills, latency, and whether a factor return series is implementable at all. **Implementing this as a trade would require factor-mimicking portfolios or style-instrument proxies; the source does not specify any such instrument mapping → `not stated in source` (Scout-proposed proxies would be `research-proposed`).**
- **Scout assumptions:** none added. No Scout-generated threshold, sizing rule or execution choice is embedded in this record.

## Evidence

### Source-reported

All figures below are third-party claims from Guan & Chen (`arXiv:2606.22719v1`), each tied to its table/section; none has been independently reproduced.

**Table 1 — monthly rank IC, 36-month walk-forward (2023-04 → 2026-03), decision-time inputs only:**

| Method | Mean IC | Median IC | Bootstrap 95% CI (mean) | Permutation p |
|---|---|---|---|---|
| Base: zero-shot CoT | +0.007 | +0.027 | [−0.15, +0.16] | 0.92 |
| + raw analog retrieval | +0.006 | +0.063 | [−0.15, +0.16] | 0.94 |
| + critic rule synthesis | +0.088 | +0.009 | [−0.05, +0.22] | 0.21 |
| **Full LLM: + CF nowcast** | **+0.131** | **+0.154** | **[−0.02, +0.28]** | **0.11** |
| Nowcast-only ridge | +0.045 | +0.125 | [−0.14, +0.23] | 0.63 |
| Macro + nowcast ridge (n=34) | +0.058 | +0.071 | [−0.11, +0.23] | 0.51 |
| kNN macro analog | +0.070 | **+0.161** | [−0.11, +0.24] | 0.44 |

**Table 2 — Full LLM mean Spearman IC by non-overlapping 12-month sub-window:** 2023-04→2024-03 **+0.111**; 2024-04→2025-03 **+0.165**; 2025-04→2026-03 **+0.117** (all three positive).

**Table 3 — long-top-2 / short-bottom-2 sanity check, monthly rebalanced, 5 bps per unit weight change** (source caption: *"Not a trading claim"*):

| Method | Ann. return | Sharpe | Max DD | Turnover (avg monthly L1 Δw) |
|---|---|---|---|---|
| Full LLM pipeline | **+4.2%** | **0.71** | −4.7% | 0.81 |
| kNN macro analog | +1.5% | 0.29 | −5.1% | 1.10 |
| Nowcast-only ridge | −0.9% | −0.12 | −10.6% | 0.17 |
| Macro + nowcast ridge | −0.2% | −0.01 | −10.8% | 0.82 |

**Table 5 (Appendix D.1) — kNN sensitivity to analog count K (LLM pipeline not rerun):** K = 2/4/6/8/12 → mean IC **+0.017 / +0.070 / +0.086 / +0.133 / +0.079**; median IC **+0.089 / +0.161 / +0.089 / +0.179 / +0.089**; long-short Sharpe **+0.02 / +0.29 / +0.51 / +0.77 / +0.17**.

**Table 6 (Appendix D.2) — extreme-rank overlap averaged over the window (Top-2 / Bottom-2 / Extreme):** Full LLM **0.417 / 0.278 / 0.347**; kNN **0.347 / 0.361 / 0.354**; nowcast-only ridge **0.278 / 0.389 / 0.333**; macro+nowcast ridge **0.309 / 0.353 / 0.331**. Source reading: *"an interpretability diagnostic rather than evidence of uniformly better extreme-rank recovery."*

**Appendix D.3 — temporal-dependence robustness:** moving-block bootstrap mean-IC 95% CI **[+0.013, +0.268]** (block L=3) and **[+0.039, +0.228]** (L=6) versus i.i.d. **[−0.023, +0.282]**; monthly IC lag-1 autocorrelation **−0.14**.

**Appendix B, Table 4 — critic-rule audit:** of **30** rules with an extractable (raise, lower) factor pair out of 36, **25 raise HML**, mostly under inverted-yield-curve / low-volatility tags (top rows: raise HML / lower BAB ×7; raise HML / lower UMD ×6; raise HML / lower CMA ×5).

**Appendix C case studies (source: illustrative, not causal):** 2024-12 Full LLM IC **+0.964** vs kNN **−0.321** (gap +1.286); 2024-07 Full LLM IC **+0.607** vs kNN **−0.857** (gap +1.464). Decision-time snapshots in those months include e.g. 2024-12-31: VIX 17.4, term spread +0.33, HY credit spread 2.92, real 10y 2.24, shifted unemployment 4.10, shifted FRED CPI YoY 2.87, Cleveland Fed nowcast 2.86.

- **Nature of the evidence:** an **IC / allocation-level benchmark**, not an executable backtest. Reported performance is **net of the 5 bps-per-weight-change charge only**; equity-asset-class result (U.S. style factors) — **not crypto evidence**.

### Independently reproduced

`not independently reproduced`

No walk-forward re-run, no LLM inference, no factor data download and no allocation replication was performed by this Scout. The source's reproducibility package is promised but carries no URL in v1 → `data gap`.

### Negative evidence

- **Statistical:** the headline mean-IC 95% CI **includes zero** and the sign-symmetric permutation **p = 0.11** — the source explicitly says the evidence is underpowered at n = 36 and declines to frame it as a discovery (§4, §5).
- **kNN matches the LLM on the median:** kNN median IC **+0.161 > LLM +0.154**, with permutation p 0.44 vs 0.11 and mean IC +0.070 vs +0.131 (Table 1) — i.e. the *nowcast + retrieval* input, not the LLM, carries much of the signal (source-reported interpretation).
- **Ablation collapse:** zero-shot CoT (+0.007/+0.027) and zero-shot + raw analog injection (+0.006/+0.063) are indistinguishable from zero; critic-only (+0.088 mean, **+0.009 median**) leaves the median at zero (Table 1). The single largest change occurs when the Cleveland Fed nowcast is added.
- **Non-LLM regressions lose money in the same allocation check:** nowcast-only ridge **−0.9% ann., Sharpe −0.12**; macro+nowcast ridge **−0.2%, Sharpe −0.01** (Table 3).
- **Extreme-rank diagnostic is mixed:** kNN has higher Bottom-2 and average Extreme overlap than the Full LLM (Table 6).
- **Parameter sensitivity:** kNN long-short Sharpe swings **0.02 → 0.77** across K ∈ {2,4,6,8,12}, peaking at K = 8, not the ex-ante K = 4 (Table 5) — an uncorrected researcher-degrees-of-freedom risk for anyone re-tuning K on this window.
- **Regime concentration:** 25 of 30 extractable critic rules "raise HML" in a 2023–2026 inverted-yield-curve / low-vol window; the source states this distribution "should not be interpreted as evidence of general factor-timing skill" (Appendix B).
- **Information matching is imperfect:** the critic anchors its macro narrative at `t−1` while kNN anchors at `t`; both are leakage-clean but the LLM-vs-kNN contrast is "a comparison of logged decision protocols rather than a controlled input ablation" (§5, Appendix A).
- **Cost reality:** only a 5 bps weight-change charge is applied; borrow on shorted factor legs, financing, impact and capacity are unmodeled, and the source itself notes such costs "materially compress paper Sharpe ratios for academic factors" (§5, citing Frazzini, Israel & Moskowitz 2012).
- **Publication-bias / multiple-testing context:** the source cites Harvey, Liu & Zhu (2016) on how fragile single-window evidence is under multiple testing.
- No external replication, failed replication, or credible contrary study **of this specific paper** was identified in this run; absence is not evidence of no negative result.

## Falsification plan

Every threshold below is a **`research-defined falsification threshold`** chosen by this Scout unless explicitly attributed to the source; none is claimed by the paper.

| # | Test | Data / regime | Metric | Pre-declared failure rule | Action on failure |
|---|---|---|---|---|---|
| 1 | **Extended walk-forward** | Rebuild a decision-time archive covering ≥120 month-end decisions (source lists this as its own future work) | mean monthly rank IC + bootstrap CI | mean IC ≤ 0 **or** 95% CI still includes zero at n ≥ 120 | reject H-macro as a stable signal; keep only the leakage-control methodology |
| 2 | **Significance** | Current protocol, extended sample | sign-symmetric permutation p | p ≥ 0.05 | reject H-macro (current v1 already fails this: p = 0.11) |
| 3 | **LLM-vs-kNN matched ablation** | Same inputs, same anchor `t`, same prompts logged | mean-IC and Sharpe difference | LLM − kNN mean IC ≤ 0 over the extended window | reject H-LLM; treat the effect as nowcast+retrieval, drop the LLM layer |
| 4 | **Nowcast channel isolation** | Replace the Cleveland Fed nowcast with lag-shifted published CPI only | median IC | median IC falls to ≈ the no-nowcast ablation level (≤ +0.063, source Table 1 row 2) | attribute the effect to the nowcast input, not to macro-analog reasoning |
| 5 | **Placebo / label shuffle** | Shuffle month labels or analog assignments, 10,000 draws | permutation p of mean IC | p ≥ 0.05 | reject (this is the source's own test type; v1 p = 0.11 already fails) |
| 6 | **Point-in-time nowcast audit** | Re-fetch Cleveland Fed nowcast **vintages as published on date t** (not the 2026-05-13 frozen archive) | any revision after t | any non-trivial vintage revision → leakage | invalidate the leakage-control claim and re-run from scratch |
| 7 | **Cost / implementability stress** | 5 → 10 → 20 → 30 bps per unit weight change **plus** borrow on the shorted factor legs | net ann. Sharpe of top-2/bottom-2 | net Sharpe < 0.20 at 20 bps one-way | reject as an allocation hypothesis; keep as benchmark only |
| 8 | **Instrument mapping** | Replicate with tradable factor/style proxies instead of published factor series | net Sharpe vs Table 3 | net Sharpe < 50% of the factor-series result | reject implementability while retaining the IC claim |
| 9 | **Parameter perturbation** | K ∈ {2,4,6,8,12} (source Table 5), buffer ∈ {1,6,12}, embargo ∈ {6,12,18} | sign and significance of the result | sign flip, or positivity only after post-hoc parameter choice | reject H-macro under the "rescuable by retuning" clause |
| 10 | **Regime / subperiod breakdown** | Split by inverted-curve vs non-inverted-curve months (source's own rule tags, Appendix B) | mean IC per regime | mean IC ≤ 0 outside the 2023–2026 signature | restrict the claim to that regime; reject general factor-timing skill |
| 11 | **Competing explanation** | Directly compare against (a) a purely deterministic investment-clock rule and (b) a 1-feature inflation-nowcast tilt | mean IC / Sharpe vs LLM pipeline | LLM pipeline not better than both simple controls | attribute any remaining edge to the input data, not the model |
| 12 | **Capacity / impact** | Only meaningful after test 8 maps to instruments | participation-scaled net Sharpe | edge erased at realistic ADV participation | reject at target capital scale |

A test is **not** falsifiable if it can be rescued by unconstrained retuning; tests 7, 9 and 11 exist precisely to block that escape.

## Crypto portability

**Verdict: `unproven`.**

- The signal is defined on **seven published U.S. equity style factor return series** with a 33-year macro retrieval pool. Crypto has **no standardized SMB/HML/RMW/CMA/UMD/BAB/QMJ cross-section** with equivalent point-in-time history; any crypto port would first have to *construct* the factor sorts (e.g. size/value-quality-momentum sorts across liquid coins), which the source never does.
- The decision-time anchor is a **U.S. macro release calendar** (BLS CPI, FOMC). Under 24/7 crypto sessions the month-end boundary and the "unreleased inflation" problem differ: there is no BLS-style publication lag to leak, so the paper's central leakage fix has **no direct crypto analogue**, while an adapted version (e.g. nowcast-versus-lagged-official inflation for macro-conditioned crypto rotation) would be a new hypothesis.
- **Shorting the "bottom" factor legs** in crypto requires borrow or perp shorting with **funding**, which is not modeled anywhere in the source; exchange fragmentation, perp/spot basis, index-price versus last-price marking, listing/survivorship in any coin universe, and 24/7 candle boundaries are all unaddressed.
- Any crypto version is an **adapted, unproven ported hypothesis** — it would not be crypto empirical evidence. Crypto portability here is **not** authorization to trade.

## Limitations

- **Sample:** n = **36** monthly decisions, a single window (2023-04 → 2026-03) set by data availability, one nowcast source, one model family (Qwen2.5-7B-Instruct), U.S. equity style factors only.
- **Statistics:** mean-IC CI includes zero, permutation p = 0.11; per-month IC s.d. ≈ 0.45 close to the Spearman null for ranking seven items → single-window power is inherently low (source-reported).
- **`data gap` — reproducibility:** prompt templates, event-summary corpus, per-month score files, retrieved analog indices and the frozen nowcast archive are promised but **not linked in v1**; byte-exact replication is therefore not currently possible.
- **`underspecified`:** month-end timezone; long/short leg normalization in Table 3; exact French-library portfolio file per factor; whether HY credit spread / real 10y yield (shown in case-study snapshots) feed the actor prompt in addition to the 4-D retrieval vector; order/execution mechanics (none are modeled).
- **Costs:** 5 bps per unit weight change only. No commission, borrow, financing, spread, slippage, impact or capacity model → all `not stated in source`.
- **Not an executable strategy:** the source states the sanity check is "not a deployable trading claim"; factor returns are not directly tradable instruments.
- **Methodological:** LLM-vs-kNN is not a controlled input ablation (anchor mismatch); Table 6 extreme-overlap is mixed; K-sweep peak (K = 8) lies away from the ex-ante K = 4; critic rules are heavily HML-concentrated in one regime.
- **Source quality / publication status:** arXiv preprint with a **non-archival workshop acceptance**; no journal-ref. Workshop acceptance is not peer review of the full result.
- **Interpretation scope:** `confidence: medium` describes confidence in the *research interpretation of what the source says* — not confidence that the strategy is profitable.

## Implementation status

`not-implemented`.

Nothing from this record has been implemented in our research stack: no walk-forward harness was reproduced, no factor data was downloaded, no LLM pipeline was run, no allocation was simulated, and no Qlib / backtest validation of any kind occurred. The source's own code and data package was **not** located or verified in this run (`data gap`).

This research capture does not modify any trading engine, does not create a strategy family, and does not authorize Paper, Testnet or Live execution.

## Adoption boundary

`status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record in the repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; or approved for live trading. Research capture is not adoption, and any later adoption decision must be explicit, separately reviewed, and based on this record plus current sources.

## Related Wiki records

- Canonical specification used for this run: `quant/strategy-research-record-spec-v1` (`schema: strategy-research-record-v1`) — the only Wiki Brain record read by this Scout.
- **No strategy record for this source exists in Wiki Brain or in this repository**; this run created only this repository artifact and wrote nothing to Wiki Brain.
- Adjacent **repository** records (different source identities and materially different constructions), read for deduplication:
  - `continuous-macro-timing-growth-defensive-style-allocation-2026-09-02` — deterministic continuous macro score timing two style baskets (arXiv:2605.20636).
  - `agentic-ai-nowcasting-stock-returns-llm-web-search-2026-09-04` — LLM stock-level nowcasting (arXiv:2601.11958).
  - `cross-sectional-centering-price-offset-nuisance-rank-ic-2026-09-14` — normalization ablation for intraday cross-sectional rank IC (arXiv:2609.07122).
  - `causal-knn-predictive-flow-leakage-falsification-2026-09-13` — kNN leakage forensics on a crypto indicator (GitHub commit `21b3a98c4cca73c97508f9b1b907fcda15424a0a`).

## Sources

1. Mao Guan, Qian Chen. *"Leakage-Aware Benchmarking of LLM Forecasting: Real-Time Nowcasts as the Decision-Time Input for Macro Factor Ranking."* arXiv preprint `arXiv:2606.22719v1 [q-fin.ST]`, submitted 21 Jun 2026 23:36:04 UTC. DOI: `10.48550/arXiv.2606.22719`. Stable URL: https://arxiv.org/abs/2606.22719. Full text HTML read by Scout: https://arxiv.org/html/2606.22719v1. Comments: 10 pages, 4 figures; accepted at the ICML 2026 Workshop on AI Forecasting (non-archival); OpenReview: https://openreview.net/forum?id=mi8QiWomm3. License: CC BY 4.0. **Primary source for every rule and number in this record.**
2. Source-reported data dependencies named by the primary source (**not opened by this Scout; listed for provenance only**): Kenneth French Data Library https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html (accessed 2026-05-13); AQR Capital Management factor datasets https://www.aqr.com/Insights/Datasets (BAB, QMJ; accessed 2026-05-13); Federal Reserve Bank of Cleveland, Inflation Nowcasting https://www.clevelandfed.org/indicators-and-data/inflation-nowcasting (daily CPI nowcast archive, frozen snapshot 2026-05-13).
