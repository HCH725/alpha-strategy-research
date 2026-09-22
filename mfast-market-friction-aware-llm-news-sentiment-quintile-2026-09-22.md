---
schema: strategy-research-record-v1
title: "MFAST market-friction-aware decoder-LLM news sentiment → daily value-weighted long-short quintile portfolio (arXiv 2609.23703v1)"
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - financial-news-sentiment
  - large-language-models
  - llama-3
  - decoder-vs-encoder
  - event-time-observability
  - contamination-safe-oos
  - transaction-costs
  - long-short-equity
status: research-only
confidence: medium
source_as_of: 2026-01-30
sources:
  - "Kemal Kirtac. 'Financial Language Models as Applied Artificial Intelligence Systems for News-Based Trading under Market Frictions.' arXiv:2609.23703v1 [cs.CL], submitted 20 September 2026. Stable URL: https://arxiv.org/abs/2609.23703 (full text: https://arxiv.org/html/2609.23703v1). arXiv DataCite DOI: 10.48550/arXiv.2609.23703. Comments on record: '47 pages. Revise and resubmit at Engineering Applications of Artificial Intelligence.' License CC BY 4.0."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MFAST: market-friction-aware decoder-LLM news sentiment into a daily value-weighted long-short quintile portfolio

## Provenance

- **Primary source (single author, exactly as listed on the arXiv abstract page):** Kemal Kirtac. Affiliations as printed in the v1 full text: Department of Computer Science, University College London, 66–72 Gower Street, London WC1E 6EA, United Kingdom; Department of Computer Science, University of Warwick, 6 Lord Bhattacharyya Way, Coventry CV4 7EZ, United Kingdom. Corresponding email as printed: kemal.kirtac.21@ucl.ac.uk.
- **Paper title:** *Financial Language Models as Applied Artificial Intelligence Systems for News-Based Trading under Market Frictions*.
- **Version / date (primary-source checksum, abs page + v1 HTML read 2026-09-22):** `arXiv:2609.23703v1 [cs.CL]`, `[Submitted on 20 Sep 2026]`; running head inside the v1 HTML reads `arXiv:2609.23703v1 [cs.CL] 20 Sep 2026`.
- **Subjects:** primary `Computation and Language (cs.CL)`; cross-lists `Machine Learning (cs.LG)` and `Trading and Market Microstructure (q-fin.TR)`.
- **Publication status:** preprint only. Comments field: `47 pages. Revise and resubmit at Engineering Applications of Artificial Intelligence` → **not peer-reviewed at time of capture**. Abs page carries **no journal-ref and no publisher DOI**; the only DOI present is the arXiv-issued DataCite DOI `10.48550/arXiv.2609.23703`. License: CC BY 4.0.
- **Stable URL:** https://arxiv.org/abs/2609.23703 — full text read for this record: https://arxiv.org/html/2609.23703v1 (Methods-equivalent sections read directly: §3 framework/Algorithm 1, §4 data–labels–temporal controls, §5 implementation, §6 evaluation design incl. §6.3 portfolio construction and market frictions, §7 results incl. §7.3, §8 robustness, §9 explainability, §11 limitations, §13 replication package, Data availability).
- **Source/data as-of:** news sample ends **2026-01-30** (last article date in the primary out-of-sample test window); this is the `source_as_of` value.
- **Pre-write deduplication (2026-09-22):** ripgrep across **all** `*.md` in this repository plus `coverage_manifest.csv` for `2609.23703`, `MFAST`, `market-friction`, and `Kirtac` → **0 hits for `2609.23703` / `MFAST` / `market-friction`** (manifest count 0); `Kirtac` appears only in two adjacent records built from the *earlier, different* source (see Related). `git log --oneline -20` inspected separately (convenience glance only).
- **Material distinction from the adjacent same-author record (required dedup statement):** the repository already holds `llm-news-probing-excess-return-sentiment-timing-2026-09-06.md`, which normalizes **Kirtac & Germano (2024), “Sentiment trading with large language models”, DOI 10.1016/j.frl.2024.105227 / arXiv:2412.19245**. This record is a **different source identity** (arXiv:2609.23703, no DOI,2026 preprint) and is written only because at least one dedup dimension is materially different:
  1. **Material data dependency:** the reported out-of-sample evidence is restricted to **2024-06-01 → 2026-01-30**, i.e. strictly after the LLaMA-3 checkpoint release (2024-04-18) and after the disclosed LLaMA-3 family pretraining data-freshness cutoffs (2023-03 for 8B / 2023-12 for 70B), with Jan–May 2024 used only as a validation/release-date buffer; the earlier source used a random article-level split across the whole sample (the prior record flags that as a temporal-leakage risk).
  2. **Signal construction:** calibrated probabilities → **within-day cross-sectional rank** → **recency-weighted firm-day aggregation** of multiple articles → value-weighted top/bottom **quintile** legs with an explicit **10%-of-ADV participation cap**, threshold-crossing-only rebalancing, and a stated5 bp one-way cost; plus one-sided event-time novelty screening (5-day, cosine > 0.80) and a split-boundary duplicate audit.
  3. **Model family:** decoder-only `meta-llama/Meta-Llama-3-8B` (LoRA) head-to-head against OPT-1.3b / RoBERTa / BERT / FinBERT / Loughran-McDonald dictionary under identical labels and execution rules (Table 5), versus the earlier OPT-2.7B-vs-encoders probing design.
  The core *theme* (firm-news text sentiment → US-equity long-short) is shared with the adjacent record; readers must treat these as one family with two distinct evidence packages, not two independent families.

## Economic mechanism

### Source-reported

The paper's central claim is explicitly an **engineering/deployment** claim, not a new behavioral anomaly: a financial language model's output only has decision value if the whole pipeline — firm matching, timestamp observability, calibration, execution timing, costs, liquidity screens, capacity caps, statistical validation — is respected (§1). The economic motivation it invokes is Grossman–Stilitz-style costly information processing: text is informative (Tetlock2007; Tetlock et al.2008; Da et al.2011; Kelly et al.2021), but information acquisition/interpretation is costly, so prices need not incorporate text instantly — especially where market frictions slow incorporation (§1, §2.4). The source states the mechanism as: decoder-only models capture compositional meaning (negation, contrastive clauses, forward-looking guidance, numeric context, event ambiguity) that lexicon polarity gets wrong, and those are exactly the cases where gradual information diffusion should leave exploitable short-horizon excess returns (§9, Table13). Source also reports a friction-gradient test: predictive coefficients rise from high-liquidity to low-liquidity stocks for all transformer models, steepest for LLaMA-3 and OPT (§7.4, reported in text, no table).

### Research interpretation

- **Primary mechanism (falsifiable form):** slow, friction-impeded diffusion of firm-specific news tone →3-day cross-sectional excess-return drift that a calibrated high-capacity text model ranks better than lexicon polarity.
- **Component roles (hybrid structure, as normalized):**
  - Signal model: calibrated P(positive execution-aligned3-day excess return) from headline+lead+body text.
  - Temporal gate: pre-09:30 ET news may trade same day; at/after09:30, after16:00, weekend, holiday news enters only from the next trading day (§4.4).
  - Eligibility filter: single-firm story → novelty screen → tradability/microstructure screens (§4.1).
  - Portfolio/execution: daily value-weighted quintile long-short, threshold-crossing rebalance,5 bp one-way cost,10% ADV participation cap (§6.3).
  - Risk/overfit controls: White reality check, Hansen SPA, deflated Sharpe, block bootstrap (§6.7, Table12).
- Not every component is alpha: the source's own feature-group ablation (Table6) attributes most predictive power to text (Acc0.787 / AUC0.846) with price-only0.541/0.565, liquidity-only0.528/0.548, metadata-only0.536/0.552, and the full stack0.803/0.866 — i.e. **structure adds at most ~1.6pp accuracy /0.020 AUC over text alone**, so frictions/execution components are hypothesized to *preserve* rather than *create* the edge (research interpretation).

## Signal

All items below are `source-reported` unless marked otherwise.

- **Formation timestamp / availability:** Refinitiv timestamps converted to US Eastern; articles before09:30 on a regular trading day are observable before the open and may enter that day's portfolio; articles at/after09:30, after16:00, on weekends, or on exchange holidays are assigned to the next trading day and enter only from that decision point (§4.4). No same-day return accrues to intraday/after-close news (Table4).
- **Label:** binary sign of the stock's cumulative **three-day execution-aligned** excess return over window `[e, e+2]`, where `e` is the first eligible trading day after the observability rule; excess = stock return − CRSP value-weighted market return (§4.2). Label windows are truncated at split boundaries (§4.3).
- **Model input:** concatenation of headline + lead paragraph + main body up to the model-specific token limit (1024 tokens for LLaMA-3/OPT,512 for RoBERTa/BERT/FinBERT per Table5); no identifiers, timestamps, prices, volumes, spreads, or forward-looking variables are placed in the text input (§4.4). Tokenization diagnostic:93.6% of items fit in512 tokens,98.9% in1024 (§5).
- **Score → signal:** `s = P_m(y=1 | text)` (Eq.1) → validation-set calibration map `g_m` (Eq.2) → within-day rank over the eligible universe `E_t` (Eq.3).
- **Multi-article aggregation:** baseline = **recency-weighted mean** of all eligible article probabilities for the same firm and execution day (later articles larger weight); robustness alternatives = last-story and max-confidence aggregation (§4.4).
- **Novelty screen:** one-sided in event time; new article vs same-firm articles in prior5 trading days; cosine similarity >0.80 ⇒ drop the later duplicate (§4.1, §4.4).
- **Lookback / training window:** supervised training articles2010-01-01→2023-12-31 (701,928 items,3,386 firms); validation + release-date buffer2024-01-01→2024-05-28 (81,317 items,2,742 firms); **primary OOS test2024-06-01→2026-01-30 (190,236 items,3,018 firms)** (Table3). Chronological splits; no random article split for reported test evidence (§4.3).
- **Long entry / short entry:** each trading day, rank eligible stocks by most recent calibrated sentiment probability; **highest quintile → value-weighted long leg, lowest quintile → value-weighted short leg** (§6.3).
- **Exit / rebalancing:** positions adjust **only when stocks cross quintile thresholds** (§6.3); robustness holds positions1/3/5 days (§8).
- **Holding period:** main specification is threshold-driven daily rebalance (implied holding varies);1/3/5-day holding variants reported as robustness (§8). Exact average holding and portfolio turnover: **not stated in source** (data gap).
- **Parameters (source-fixed, chosen on train/validation only, then frozen before the OOS test, §4.3):** quintile cutoffs (robustness: decile, tercile),5 bp one-way cost (robustness:0–50 bp),10% daily dollar-volume participation cap, cosine novelty threshold0.80,5-day novelty window,20-trading-day split-boundary duplicate audit, liquidity screens (below), label window3 trading days.
- **Model checkpoints / training (Table5):** `meta-llama/Meta-Llama-3-8B` (8.0B, decoder, LoRA r=16 alpha=32, lr1.0e-4, batch16,3 epochs, patience2); `facebook/opt-1.3b` (LoRA r=16 alpha=32, lr1.2e-4, batch24,4 epochs); `roberta-base` (125M, full FT, lr2.0e-5, batch64,4 epochs); `bert-base-uncased` (110M, same); `ProsusAI/finbert` (110M, lr1.5e-5, batch64,4 epochs); Loughran-McDonald2022 dictionary (no training). Binary cross-entropy, AdamW, cosine decay,10% warmup, early stop on validation F1. Hardware:4×A10080GB (decoders),1×A10080GB (encoders). Static checkpoints; retrieval, browsing, external tools disabled at inference (§4.3).
- **Fully specified?** The signal is reconstructible in structure but **underspecified** on: exact calibration map family `g_m`, exact quintile tie-breaking, the participation-cap λ value (the cap is stated as “10% of daily dollar volume”; Eq.4 uses λ), borrow/ease-to-borrow rules for the short leg, and cost model beyond a flat bp rate. Those remain `underspecified` / `not stated in source`.

## Required data

All `source-reported` unless noted.

- **Instrument / universe:** US common equities in CRSP (daily returns, prices, bid/ask quotes, share volume, dollar volume, shares outstanding, market cap) linked to Refinitiv News Analytics firm-specific, timestamped news. Survivorship handled via CRSP security identifiers and event-time eligibility: active, inactive, acquired, merged and delisted securities included when they pass screens at the event date; delisting returns combined as `(1+RET)(1+DLRET)−1` (§4.4).
- **Attrition path (Table3):** all Refinitiv US news3,129,924 items /5,218 firms → single-firm stories1,985,135 /4,604 (63.4%) → after5-day novelty screen1,122,475 /4,101 (56.5%) → after tradability+microstructure filters **973,481 /3,452 (86.7%)** → train701,928 (72.1%) / validation buffer81,317 (8.4%) / OOS test190,236 (19.5%).
- **Tradability screens (§4.1):** positive bid **and** ask quotes; daily share volume >1,000 shares; daily dollar volume ≥ $50,000; quoted spread <20%; non-missing Amihud illiquidity and Kyle lambda proxies.
- **Market type / venue:** cash equities (exchange session hours, US); **no derivatives, no crypto**.
- **Timeframe:** daily bars/quotes with millisecond-or-better news timestamps converted to US/Eastern; decision points at the open (09:30) and next-trading-day rolls (§4.4).
- **Fields used:** news text (headline/lead/body), article timestamp, firm identifier; CRSP RET, DLRET, price, bid, ask, share volume, dollar volume, shares outstanding, market cap; derived:3-day execution-aligned excess return vs CRSP VW index, cosine similarity, Amihud illiquidity, Kyle lambda, sector/size/time-bucket metadata (§4, §6.6).
- **Point-in-time:** headline discipline is the paper's own — primary test starts after LLaMA-3 checkpoint release (2024-04-18) and after the disclosed pretraining freshness cutoffs (2023-03 /2023-12); Jan–May2024 excluded from reported test metrics (§4.3, Table4). Static checkpoints, no retrieval.
- **Timestamp / timezone:** all Refinitiv timestamps → US/Eastern, mapped to next feasible decision time; out-of-order handling **not stated in source** (data gap).
- **Missing data:** observations with missing prices/returns, nonpositive quotes, or nontradable status at execution date are excluded **before** label construction and portfolio formation (§4.4); imputation is not used (no imputation method stated ⇒ none claimed).
- **Costs data:** flat one-way transaction-cost parameter (5 bp main) plus10% ADV participation cap; **spread is handled only as a screen (<20% quoted spread) and is not charged in the return accounting**; borrow fees, stock-loan availability, explicit market-impact/slippage models: **not stated in source**.

## Execution assumptions

`source-reported` items:

- **Signal-to-order timing:** execution-aligned observability rule (§4.4) — pre-open news trades same day; all other news trades from the next decision point. A stricter robustness variant delays **every** signal by one full trading day (“timing-conservative specification”, §4.4).
- **Order type / fill model:** not specified beyond daily portfolio formation at ranked quintiles ⇒ **underspecified** (no market-vs-limit choice, no partial-fill model, no queue position).
- **Costs:** **5 bp one-way** transaction cost in the main specification (Eq.5, §6.3, Table9 caption); robustness grid **0–50 bp** with stable model ranking (§8). Impact, slippage beyond the flat bp rate, borrow fees, dividends treatment in the trading P&L: **not stated in source**.
- **Capacity / liquidity:** trades capped at **10% of daily dollar volume** (Eq.4, §6.3); source states this cap binds most often in smaller/less-liquid names and that value weighting keeps results from being driven by infeasible microcap trades (§8). Dollar capacity in absolute terms: **not stated in source**.
- **Spread:** only as a <20% quoted-spread eligibility screen (§4.1) — a deliberately loose screen; charged spread is **not stated in source**.
- **Shorting / borrow:** short leg is formed (lowest quintile) but short availability, locate, borrow cost and recall risk: **not stated in source** ⇒ the net long-short Sharpe cannot be read as borrow-adjusted.
- **Leverage / margin:** not stated in source.
- **Latency:** inference latency reported as an engineering diagnostic (Table11: LLaMA-3112.0 ms/article,8.9 articles/sec,54.2 GB peak GPU memory; OPT43.0 ms/23.3/s/18.6 GB; RoBERTa9.4/106.4/4.8 GB; BERT8.8/113.6/4.6 GB; FinBERT8.5/117.6/4.4 GB; dictionary2.3/434.8/0.5 GB) — no order-routing latency model.
- **Execution realism caveat (source's own limitation, §11.2):** “the execution model is realistic but not a full order-book simulator. Intraday liquidity, queue position, hidden liquidity, and strategic interaction remain outside the current design.”
- Scout assumptions used anywhere below are labeled `research-proposed` / `research-defined`.

## Evidence

### Source-reported

All figures are third-party claims from arXiv:2609.23703v1, **primary OOS test window2024-06-01→2026-01-30 (N=190,236 article-level observations)** unless stated; **not independently reproduced**. Table provenance is given for every number.

- **Classification / calibration (Table7):** accuracy LLaMA-3 **0.787**, OPT **0.763**, RoBERTa **0.748**, BERT **0.728**, FinBERT **0.713**, LM dictionary **0.503**; AUC **0.846 /0.821 /0.807 /0.782 /0.764 /0.512** respectively; Brier **0.151 /0.166 /0.174 /0.190 /0.203 /0.249**; expected calibration error **0.032 /0.041 /0.047 /0.061 /0.068 /0.143**. Paired McNemar tests reject equality of LLaMA-3 vs every other transformer at the1% level (§7.1).
- **Predictive regressions (Table8, firm+date FE, clustered SEs, N=190,236):** LLaMA-3 coef **0.312\*\*\*** (t=**6.44**, within R²=0.052, RMSE3.71); OPT **0.281\*\*\*** (t=5.91, R²0.047); RoBERTa **0.236\*\*\*** (t=5.12, R²0.041); BERT **0.177\*\*\*** (t=4.36, R²0.032); FinBERT **0.158\*\*\*** (t=3.98, R²0.029); LM dictionary **0.049** (t=**1.31**, R²0.006, not significant). Pairwise: with LLaMA-3 in the regression the dictionary coefficient becomes insignificant (§7.2).
- **Net portfolio performance,5 bp cost,10% ADV cap (Table9):** LLaMA-3 long SR **1.72**, short SR **1.48**, **long-short SR2.85**, mean daily **0.34%**, daily vol **1.89%**, MDD **−12.3%**, cumulative L-S **180%**; OPT **2.45** L-S SR, cum **155%**; RoBERTa **2.25**, **120%**; BERT **1.95**, **88%**; FinBERT **1.75**, **64%**; LM dictionary **0.68** L-S SR, cum **−9%**, MDD **−34.2%**. Benchmark rows as printed in Table9: Nasdaq Composite long SR0.88 / L-S SR1.10 / mean daily0.12% / MDD−26.9% / cum35%; Dow Jones Industrial long SR0.78 / L-S SR0.95 / mean0.10% / MDD−28.7% / cum21% (short-leg cells N/A).
- **Statistical validation (Table12):** block-bootstrap Sharpe for LLaMA-3 **2.85**,95% CI **[2.31, 3.34]**; block-bootstrap **daily alpha0.182%**,95% CI **[0.109%,0.252%]**; Diebold–Mariano **DM=−7.12, p<0.001**; White reality check max statistic **2.37, p=0.018**; Hansen SPA **2.21, p=0.026**; deflated Sharpe ratio **DSR=2.19, p=0.014**.
- **Feature-group ablation (Table6):** text only Acc0.787/AUC0.846; price only0.541/0.565; liquidity only0.528/0.548; metadata only0.536/0.552; text+price0.796/0.857; text+liquidity0.792/0.850; full MFAST0.803/0.866.
- **Public-data replication arm (Table10):** Financial PhraseBank sentiment (4,840 sentences,70/15/15) Acc **0.842**, AUC **0.901**; GDELT headline-to-return (2019–2024 construction panel, post-release test from Jun2024) Acc **0.612**, AUC **0.651**; open friction-aware portfolio on post-release tradable public signals: **Sharpe0.92, cumulative41%** (note the magnitude gap vs the proprietary2.85).
- **Robustness (§8, reported in text, no table):** model ranking stable for costs **0→50 bp**, cutoffs **decile/quintile/tercile**, holding **1/3/5 days**, and excluding the largest50 stocks; factor-adjusted alphas remain positive for the strongest transformer models after market, size, value, profitability, investment and momentum controls; the10% participation constraint binds most in smaller/less-liquid stocks.
- **Mechanism gradient (§7.4, text only):** predictive coefficients increase from high- to low-liquidity stocks for all transformers, steepest for LLaMA-3 and OPT.
- **Linguistic attribution (Table13, stratified1,200-article human-coded sample):** LLaMA-3 accuracy vs dictionary gain is smallest for simple polarity (0.812 vs0.641, gain0.171) and largest for contrastive clauses (0.803 vs0.438, gain0.365), forward-looking guidance (0.826 vs0.491, gain0.335), negation (0.781 vs0.462, gain0.319), numeric context (0.774 vs0.519, gain0.255), event ambiguity (0.759 vs0.472, gain0.287); shares of sample22/13/18/17/16/14% (sums to100% as printed).
- **Portfolio turnover, number of names per leg, gross-vs-net decomposition, subperiod Sharpe, capacity in dollars:** **not stated in source** (data gaps; do not infer).
- **Asset-class caveat:** every performance figure above is **US cash equities**, long-short, net of a flat5 bp one-way cost. None of it is crypto evidence.

### Independently reproduced

not independently reproduced

### Negative evidence

- **Weak-signal strategies are destroyed by the same cost model:** the Loughran-McDonald dictionary leg — the classic baseline — is **negative** net (L-S SR0.68, cum −9%, MDD −34.2%) while the indices are positive (Table9). This is the source's own demonstration that at turnover levels implied by quintile threshold rebalancing, a near-chance signal (Acc0.503, t=1.31 in Table8) does not survive costs.
- **Open-data replication is far weaker than the licensed-data headline:** public arm Sharpe **0.92 / cum41%** (Table10) vs proprietary **2.85 /180%** (Table9) — a ~3× gap that the source attributes to noisier entity matching and timestamps (§7.6). An independent reader should treat the headline as the upper end and the open arm as the realistic reproduction target.
- **Contamination cannot be fully excluded (§11, limitation3):** post-cutoff testing, static checkpoints, no retrieval, split-boundary duplicate removal and public replication are called *contamination safeguards, not proof* that no document-level pretraining exposure exists.
- **Execution model is not an order-book simulator (§11, limitation2):** no queue position, hidden liquidity, intraday liquidity or strategic interaction; combined with a loose <20% quoted-spread screen and no charged spread/impact/borrow, the reported net Sharpe is **not a full implementation-cost estimate**.
- **Single-market scope (§11, limitation1):** English-language US equities only; generalization is explicitly not claimed.
- **Source quality / status:** single-author preprint under journal revise-and-resubmit, **not peer-reviewed**, no journal-ref/DOI beyond arXiv; detailed cost grids, factor-loadings, capacity diagnostics and subperiod panels are deferred to an online appendix that is **not in the v1 HTML** (§8) ⇒ those breakdowns are unavailable for audit in this version (data gap).
- **Family-level caution from adjacent literature in this repository:** the same author's earlier random-split design (DOI10.1016/j.frl.2024.105227) carries the temporal-leakage critique documented in `llm-news-probing-excess-return-sentiment-timing-2026-09-06.md`; MFAST is best read as the author's corrective, which cuts both ways — it is more disciplined, but it is also not yet independently checked.
- **None of the above refutes the mechanism**; absence of a failed replication is not evidence of robustness.

## Falsification plan

Items marked `source-defined` come from the paper; `research-proposed` / `research-defined` are Scout operationalization and carry no source authority.

1. **Leakage / observability audit (`source-defined` rule, §4.4 + Table4):** replicate the pre-09:30 vs next-day assignment exactly; then run the source's timing-conservative variant (delay every signal one trading day). **Failure rule (`research-defined`):** if the delayed-signal L-S net Sharpe at5 bp falls below **0.5** or its block-bootstrap95% CI includes0, the event-time alpha claim is rejected — performance that exists only in same-day exposure is not news-interpretation alpha.
2. **Placebo suite (`source-defined`, §6.4):** date-shuffle (same firm), firm-shuffle (same date), sign-permutation of ranks. **Failure rule (`source-defined` intent, `research-defined` cutoff):** a valid signal must collapse to L-S net Sharpe **|SR| <1.0** under each placebo; if any placebo retains SR ≥1.0, the result is mechanical turnover or factor exposure, not information.
3. **Cost stress (`source-defined` grid0–50 bp, §8):** re-run the full model ladder at0/5/10/20/50 bp plus a charged half-spread and a stock-loan fee proxy (`research-proposed` add-ons, since the source charges neither). **Failure rule (`research-defined`):** hypothesis fails if LLaMA-3 net L-S SR **<1.0 at20 bp all-in**, or if the model ordering vs the dictionary inverts (which would show the edge is cost-model artifact).
4. **Contamination stress (`research-proposed`):** re-estimate on a test window that starts **before** the LLaMA-3 freshness cutoff (e.g.2019–2021) using an encoder-only ladder, and compare coefficient magnitudes with the post-cutoff window. **Failure rule (`research-defined`):** if decoder advantage over RoBERTa is ≤0 in the post-cutoff window while being large pre-cutoff, the “language understanding” mechanism is unsupported.
5. **Factor and benchmark adjustment (`source-defined` §8 / `research-defined` cutoff):** Fama–French5 + momentum adjusted alpha must stay positive with t>2 (`research-defined`). Failure ⇒ reclassify as style exposure.
6. **Placebo universe / alternative venue (`research-proposed`):** repeat on (a) a liquidity-trimmed universe excluding the smallest50% by dollar volume, (b) a non-US developed market news feed. Failure ⇒ mechanism is a US-small-cap friction artifact.
7. **Capacity / participation (`source-defined`10% ADV cap, `research-defined` scaling):** scale AUM until the cap binds at5% ADV. **Failure rule (`research-defined`):** net SR <1.0 at that scale ⇒ capacity-fragile.
8. **Ablation of the hybrid (`source-defined` §6.6 design):** remove novelty screen, calibration, timestamp execution, liquidity screens, capacity cap one at a time. If no single removal changes the result materially (|ΔSR| <0.2, `research-defined`), the deployment framing is decorative and the record's mechanism claim must be downgraded to plain text-sentiment drift.
9. **Out-of-sample discipline:** all thresholds above are frozen before touching any new data; any retuning after seeing test results voids the test (`research-defined`). What follows failure: keep the family in research-only, do not promote, and record the failed variant as negative evidence.

## Crypto portability

**adapted** (mechanism ported; **no crypto evidence in the source**).

- The mechanism — friction-slowed diffusion of firm-specific text tone into3-day cross-sectional drift — does not logically require equities, but every empirical number here is US cash equities on US session hours (§11.1).
- Porting changes: (i) **session structure** — crypto trades24/7, so the09:30 observability gate must be redefined (e.g. event-time arrival → next aggregation boundary), and “next trading day” rolls disappear; (ii) **benchmark** — there is no CRSP VW index; excess-return labels would need a BTC/market-basket or equal-weight crypto index, changing label semantics; (iii) **entity mapping** — one news item → one token is far noisier than Refinitiv→CRSP CUSIP linking, and multi-token stories are the norm, which the source's single-firm filter would largely eliminate; (iv) **venue fragmentation and liquidity screens** — Amihud/Kyle/ADV screens must be rebuilt per venue with perp vs spot distinctions, funding and mark/index price; (v) **costs** — taker/maker fees, spread, funding on any hedged perp leg, and liquidation risk replace the flat5 bp + ADV cap; (vi) **token lifecycle** — delisting/delist-return conventions and survivorship differ materially.
- Nothing in the source tests crypto; treat any crypto version as a fresh hypothesis requiring its own contamination-safe OOS and cost study.

## Limitations

- `underspecified`: order type, fill/partial-fill model, tie-breaking, calibration map family `g_m`, participation-cap λ exact value, portfolio turnover, names per leg, average holding, borrow/short costs, leverage/margin, out-of-order timestamp handling, dollar capacity.
- `data gap`: charged spread, market impact, slippage, stock-loan fees are **not stated in source** and must not be assumed zero; subperiod/cost-grid/factor-loading detail is deferred to an unavailable online appendix in v1 (§8).
- `not independently reproduced`: every performance, calibration and statistical figure in this record is a single-author, non-peer-reviewed preprint claim (arXiv:2609.23703v1, R&R at EAAI).
- `unproven`: the decoder-over-encoder advantage is tested on one proprietary panel (Refinitiv–CRSP) with one label definition (3-day execution-aligned excess return); the public arm reproduces only the *ranking*, not the magnitude (Sharpe0.92 vs2.85).
- Contamination risk is reduced, not eliminated (§11.3); the source's own wording is “safeguards … not proof”.
- Family overlap: shares the firm-news-sentiment→equity-long-short theme with `llm-news-probing-excess-return-sentiment-timing-2026-09-06.md` (different source, materially different data dependency/signal construction — see Provenance); if Intake Review judges the distinction immaterial, merge/defer rather than double-count the family.
- Sample-selection: the973,481-item panel is a *tradable* news stream after5 screens, not all media coverage; multi-firm/macro stories (often the market-moving ones) are excluded by construction (§4.4).
- Publication-bias: a single positive paper on LLM trading pipelines is weak evidence; several adjacent records in this repository document LLM-strategy fragility and selection luck.

## Implementation status

`implementation_status: not-implemented`. No part of MFAST — data ingestion, novelty screen, model fine-tuning, calibration, portfolio construction, cost model — has been implemented, run, or validated in our research stack. No Qlib full backtest, no production card, no Paper/Testnet/Live activity exists for this record. The source's replication package (§13: public scripts, configuration templates, model checkpoint identifiers, seeds, ablation/portfolio/statistical-test code, deterministic output tables) is described in the paper; we have **not** fetched or executed it (`data gap`: repository URL for the package is not given as a stable link in the v1 text we read).

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered `/results/_handoff/candidates.json`; completed Qlib validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. No record wording, evidence count, confidence value, or schedule implies promotion.

## Related Wiki records

Adjacent records in this repository (same or neighboring families; listed as file identities, no Wiki links asserted where none is known):

- `llm-news-probing-excess-return-sentiment-timing-2026-09-06.md` — **same first author, earlier, different source** (Kirtac & Germano2024, DOI10.1016/j.frl.2024.105227 / arXiv:2412.19245); random-split leakage critique lives there. Primary dedup counterparty for this record.
- `llm-news-sentiment-direct-rl-crypto-trading-ddqn-grpo-2026-09-06.md` — cites the same author line, different mechanism (RL control, crypto).
- `llm-news-enhanced-cross-sectional-momentum-tilt-2026-09-06.md`, `llm-event-aware-sentiment-factor-contrarian-alpha-2026-09-04.md`, `hybrid-xgboost-finbert-regime-adaptive-equity-2026-09-04.md` — adjacent text-sentiment → equity cross-section family.
- `agentic-ai-nowcasting-stock-returns-llm-web-search-2026-09-04.md`, `tda-persistent-homology-finbert-sentiment-portfolio-optimization-2026-09-02.md`, `foreign-exchange-macro-news-fundamental-momentum-llm-taylor-rule-2026-09-02.md` — adjacent LLM/text → return family, different data dependencies.
- `sok-farsight-llm-trading-agents-robustness-security-negative-evidence-arxiv-2609.19705-2026-09-19.md`, `llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04.md` — family-level negative evidence on LLM trading robustness/selection effects.
- No stable Hermes Wiki Brain page is known for these paths from this run, so no `[[...]]` links are asserted.

## Sources

1. Kemal Kirtac, *Financial Language Models as Applied Artificial Intelligence Systems for News-Based Trading under Market Frictions*, arXiv:2609.23703v1 [cs.CL], submitted2026-09-20,47 pages, R&R at *Engineering Applications of Artificial Intelligence*, CC BY4.0. https://arxiv.org/abs/2609.23703 — primary source for provenance, §3–§13, Tables2–13, Algorithm1, and all quantitative claims above (full text read at https://arxiv.org/html/2609.23703v1 on2026-09-22).
2. Dedup/search evidence for this run: ripgrep over all `*.md` plus `coverage_manifest.csv` in `HCH725/alpha-strategy-research` for `2609.23703`, `MFAST`, `market-friction`, `Kirtac` (0 hits for the new source identity); `git log --oneline -20` reviewed; repository synced with `git pull origin main` before research.
3. Model-card facts quoted from the paper's §4.3 (Llama3 release date2024-04-18; freshness cutoffs2023-038B /2023-1270B, attributed there to Meta Llama2024) — reported second-hand through the primary source, not independently checked against Meta's model card.
