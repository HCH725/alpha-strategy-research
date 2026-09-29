---
schema: strategy-research-record-v1
title: "RICE-Alpha: Point-in-Time Issuer-Local Typed-Event Graph with Reliability-Calibrated Residual Correction on a Multi-View LLM Stock Score (Nasdaq-100 / HSI, weekly top-10% long-only)"
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - llm-reasoning
  - event-driven
  - point-in-time
  - cross-sectional
  - equity
status: research-only
confidence: medium
source_as_of: 2026-09-27
sources:
  - "https://arxiv.org/abs/2609.34004 (arXiv:2609.34004v1 [cs.LG], submitted 27 Sep 2026; landing read 2026-09-29)"
  - "https://arxiv.org/pdf/2609.34004v1 (pinned v1 PDF, 15 pages, 1103328 bytes, SHA-256 2de1d5766a752441bb71917789f43825efd33ce631f641aa89a6b477e106d26c, fetched 2026-09-29)"
  - "https://arxiv.org/html/2609.34004v1 (arXiv full-text HTML for the same v1, 303357 bytes, fetched 2026-09-29 as a cross-check)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Section 4.2 parenthetical '(at most 6% of their U.S. values)' does not hold as a magnitude claim for all three methods it attaches to: from Table 1 Panel A the Hong Kong / U.S. IC ratios are 0.0013/0.0216 = 6.02% (MEME), 0.0011/0.0188 = 5.85% (R&D-Agent-Quant) and -0.0018/0.0077 = -23.4% (AI Hedge Fund), i.e. a magnitude of about 234% of its U.S. value; unreconciled in the pinned v1 text."
---

# RICE-Alpha: Point-in-Time Issuer-Local Typed-Event Graph with Reliability-Calibrated Residual Correction on a Multi-View LLM Stock Score (Nasdaq-100 / HSI, weekly top-10% long-only)

## Provenance

**Primary source identity.** arXiv preprint `arXiv:2609.34004v1 [cs.LG]`, title *RICE-Alpha: Reliability-Informed Correction with Event Graphs for LLM-Agent Stock Forecasting*, landing page `https://arxiv.org/abs/2609.34004`, pinned PDF `https://arxiv.org/pdf/2609.34004v1`, full-text HTML `https://arxiv.org/html/2609.34004v1`. The landing submission history prints exactly one version: `[v1] Sun, 27 Sep 2026 23:03:31 UTC (786 KB)`; the `Comments` field reads `15 pages, 4 figures, 4 tables`; `Subjects: Machine Learning (cs.LG)` only (no q-fin primary category); the Journal-reference field and the external DOI field are empty; the only DOI is the arXiv-issued DataCite DOI `https://doi.org/10.48550/arXiv.2609.34004`; `citation_date 2026/09/27`. The HTML full-text page prints `License: CC BY 4.0`, and the pinned PDF carries a `/License` field naming `creativecommons.org/licenses/by/4.0` (scheme elided here, see the pinned PDF metadata) → **preprint only, no peer-reviewed venue, no v2 as of 2026-09-29** (`source_as_of: 2026-09-27` = v1 submission date). The landing prints v1 as `(786 KB)` while the artefact served by the `/pdf/` endpoint is 1,103,328 bytes — two different artefacts, recorded as printed and **not reconciled**.

**Author list (three-way match).** Exactly three authors, identical ordering in (a) the landing `Authors:` block and `citation_author` meta (`Liu, Tong` / `Liu, Lanmiao` / `Hu, Xiang`), (b) the PDF title block (`Tong Liu1,*  Lanmiao Liu2,3,*,†  Xiang Hu4,*`) and (c) the PDF `/Author` metadata (`Tong Liu; Lanmiao Liu; Xiang Hu`): **Tong Liu\*, Lanmiao Liu\*, Xiang Hu\*** (\* equal contribution; † corresponding author `lanmiao.liu@mpi.nl`; Xiang Hu contact printed as `huxiang2022@e-chinalife.com`). Affiliations printed on page 1: `1 Zircon Security`, `2 Utrecht University`, `3 The Max Planck Institute for Psycholinguistics`, `4 China Life R&D Center`. No ORCID, no funding statement, no conflict/competing-interest statement, no acknowledgments section and **no code/data availability statement** anywhere in the pinned PDF → all of those fields `data gap`.

**Pinned PDF read-back (primary-source checksum, performed 2026-09-29).** 15 pages, 1,103,328 bytes, SHA-256 `2de1d5766a752441bb71917789f43825efd33ce631f641aa89a6b477e106d26c`; pypdf 6.11.0 extraction yields 54,984 characters over 15 pages; the Abstract, §1–§6, all four tables (Tables 1–4 with captions and notes), all four figure captions, the full References list and Appendix A (*Notation and Fixed Scales*) were read end to end. The same v1 was independently fetched as arXiv full-text HTML (303,357 bytes) and used only to cross-check section headings and the license line. PDF metadata `/Title` matches the landing title and `/arXivID` is `https://arxiv.org/abs/2609.34004v1`; `/Producer pikepdf 8.15.1`, `/Creator arXiv GenPDF (tex2pdf:0d14211)`, `/Trapped /False`.

**No implementation artefact.** The paper releases no repository, no prompts file and no point-in-time data archive; the only GitHub URL in the PDF is the third-party baseline `https://github.com/virattt/ai-hedge-fund` (cited as Singh 2024, `Accessed September 26, 2026`), which was **not fetched for this record**. Data vendors named by the source are Alpha Vantage (`https://www.alphavantage.co/documentation/`, `Accessed September 26, 2026`) and Tushare Pro (`https://tushare.pro/document/2`, `Accessed September 26, 2026`), also not fetched.

**Repository-wide dedup audit (2026-09-29, hidden-inclusive).** `rg -uuu` across the entire checkout — including `.git`, `.mimo-worktrees`, `.agents`, `.hermes`, `coverage_manifest.csv` (1,088,787 bytes) — for each of `2609\.34004`, `RICE-Alpha`, `RICE Alpha`, `Reliability-Informed Correction`, `Lanmiao Liu`, `Zircon Security`, `RICE Delta`, `Typed Event Agent` → **0 matching files for every pattern**, and `grep -c` of `coverage_manifest.csv` for `2609.34004` / `RICE-Alpha` / `Reliability-Informed` / `Lanmiao` → **0**. Mechanism-level scan for `issuer-local`, `event graph`, `event-graph`, `successor transition`, `reliability-weighted`, `point-in-time event`, `event continuation` returned only unrelated prose in `tradingview-atr-filtered-liquidity-void-repair-2026-09-24.md`, `favor-hypothesis-grounded-agentic-factor-validation-topk-portfolio-2026-09-24.md`, `alphaschema-trading-semantic-plan-space-surrogate-guided-factor-mining-2026-09-05.md`, `autoscientist-quant-budgeted-self-evolving-search-cross-sectional-top50-2026-09-26.md`, `tradingview-oi-footprint-liquidation-cluster-density-2026-09-20.md`, `quantaalpha-institutional-price-volume-correlation-intraday-momentum-2026-09-05.md` — none of which records a typed-event successor graph or this source. Positive control `novy-marx` → **31 files before writing**. `git log --oneline -20` was inspected only as a convenience glance (head `c15b4df`, the Boundaries-of-TSMOM record), not as dedup evidence.

**Four-axis distinction against the closest existing records.** `llm-augmented-semantic-network-cross-stock-reversal-2026-09-04.md` (arXiv 2604.19476, Huang et al., a paper this source *cites* in §2 but explicitly does **not** benchmark) builds cross-stock embedding-similarity links and trades a Gatev-distance quintile **reversal**; RICE-Alpha builds **within-issuer** typed-event successor edges, pools them only after local pairing, and adds a reliability-weighted **residual** to a long-only top-decile momentum-style book — different source, different signal construction, different direction convention. `news-event-tag-drift-rumor-resolution-placebo-adjusted-momentum-2026-09-02.md` (arXiv 2608.14014) times disclosure/rumor abnormal-return drift with a placebo adjustment; RICE-Alpha never times an event window, it calibrates graph continuation into a daily cross-sectional score. `llm-event-aware-sentiment-factor-contrarian-alpha-2026-09-04.md` (arXiv 2508.07408) turns social-media event labels into a **contrarian** factor with no graph and no point-in-time memory layer. `favor-hypothesis-grounded-agentic-factor-validation-topk-portfolio-2026-09-24.md` (arXiv 2608.30192) mines formulas with distributional construct-validation gates on CSI 500 / S&P 500 via Qlib `TopkDropout`; RICE-Alpha does not mine formulas at all — its claim is that an issuer-local, reliability-calibrated event correction adds incremental IC on top of an already-built multi-view score. `evolvetrade-self-evolving-llm-tool-use-policy-agent-15-us-bluechips-2026-09-26.md` learns an LLM tool-use trading policy; different mechanism and universe. Baseline overlap (AI Hedge Fund, R&D-Agent-Quant, 12–1 momentum) appears in other records but shared baselines are not shared source identity. Every pair differs in source identity **and** in at least one of mechanism, signal construction, universe/market type, horizon/regime or material data dependency → independent record under the dedup contract.

## Economic mechanism

### Source-reported

The authors' thesis (§1, §2) is a **point-in-time information-structure claim**, not a new premium: equity-relevant news unfolds as temporally dependent corporate events, so historical material is usable only if (i) event continuity, (ii) cutoff availability and (iii) transition reliability are modelled explicitly. They diagnose three coupled failure modes in existing LLM financial agents — *limited historical contextualization*, *weak temporal grounding of event relations*, and *uncalibrated use of historical transitions* (§1) — and answer each with one module:

- **Regime / context:** none in the trading rule. Regime enters twice, differently: a date-level macro signal `µ_t` with a clipped historical market beta `χ_i,t` adjusts the Base Alpha (Appendix A, Eq. 5 surroundings), and a three-state market regime `ζ_t` (risk-on / neutral / risk-off, from three historical index-volatility levels) gates which event statistics may be queried (Appendix A).
- **Primary signal — History-Aware Multi-View Base Alpha (§3.2).** Dedicated Sentiment, Technical, Fundamental and Macro agents each return a standardized view with a confidence score; the Sentiment Agent is additionally conditioned by a Multi-Tier Memory Layer (MML) that retrieves only temporally eligible issuer-specific context (local graph context, matured historical cases, current event narrative, regime-matched calibration evidence, successor-event memories), with outcome-dependent memory admitted "only after the corresponding returns have matured". Views with confidence `c ≥ 0.30` are reconciled into `ev_i,t`, then `b_i,t = clip(m_i,t · ev_i,t, bmin, bmax)` with `(bmin, bmax) = (−1, 1)` (Eq. 1; Appendix A: `ev = clip(s_fb · clip(v̄/3, −1, 1), −1, 1)`, `v̄ = 0` when no view is eligible, `m = clip(1 + 0.25 µ_t χ_i,t, 0.75, 1.25)`).
- **Confirmation / correction layer — the RICE Event Engine (§3.3), the actual research claim.** *Stage 1:* a Typed Event Agent resolves cutoff-available news against the previously validated active-record set; each accepted record `z = (g_z, f_z, π_z, κ_z)` carries a grounded description, event type, event sentiment and a lifecycle state `κ ∈ {NEW, UPDATED, CARRIED}`, and **only validated NEW and UPDATED records create dated graph occurrences**, so repeated coverage cannot inflate transition support. Successor relations `A → B` are formed **strictly within one issuer**, requiring `B` inside a successor window `W_succ` and the same market regime; an anchor becomes eligible only after its full successor window has elapsed. Comparable pairs are then pooled **across** issuers "only after issuer-local formation and within the same market and regime", producing a graph `G(ζ)_t` that is **frozen at cutoff t, so current records may query but cannot update the statistics used for their own prediction** (§3.3.1). *Stage 2:* the current query set is matched to the frozen graph; one-hop outgoing edges get a smoothed conditional transition rate `p_e`, a regime baseline `q_e`, a relative lift `L_e = p_e / max(q_e, ε)`, and an observational reliability weight `ρ_obs` built from matured support, distinct-successor-date coverage and standardized matured successor-return association; each retained edge contributes a bounded score `C_i,e,t` whose **sign follows the matured successor-return association** (Eq. 2, Appendix A Eq. 8), aggregated to `r_graph` clipped at `±τ_Δ = 0.20`.
- **The residual step (§3.3.2, Eq. 3).** Because MML and the technical view may already encode the same events, the graph signal is **not** added directly: it is residualized against the Base Alpha and the technical view by average-rank regression (≥ 20 common stocks) and standardization, gated by `g_edge ∈ {0,1}` (at least one retained non-self transition), yielding the RICE Delta `Δ_i,t`.
- **Final synthesis (§3.4, Eq. 4).** `a_i,t = clip(b_i,t + λ_Δ · s_Δ · Δ_i,t, a_min, a_max)` with `λ_Δ = 0.30`, `s_Δ = 1/3`, `(a_min, a_max) = (−1, 1)` (Appendix A).

Reported economic reading (§4.2, §4.4): the correction "turn[s] sparse historical episodes into a steadier daily ranking" (the U.S. daily IC dispersion is about half of momentum's), and the resulting book loses less in falling markets than in rising ones.

### Research interpretation

Falsifiable form of the hypothesis: **within-issuer temporal succession of typed corporate events carries incremental cross-sectional return information that (a) a point-in-time frozen graph can extract without look-ahead, and (b) is not already contained in a sentiment/technical/fundamental/macro composite score — so a reliability-weighted, rank-residualized graph term raises daily IC and ICIR out of sample.** Component roles, kept separate so ablation can be attempted later:

```text
Regime:        three-state index-volatility regime ζ_t gating graph statistics (plus a bounded macro multiplier on Base Alpha)
Primary signal: multi-view LLM Base Alpha (sentiment + technical + fundamental + macro, MML-grounded)
Confirmation:  issuer-local typed-event successor graph -> reliability weight -> rank residual (the paper's actual claim)
Risk/exit:     none in the source — weekly reset to equal-weight top 10%, T+1 at next open (portfolio rule, not alpha)
```

Two boundaries I mark rather than resolve. First, the source disclaims causal identification: each pooled edge "represents temporal order rather than causation" (§3.3.1), so the mechanism is a **predictive-continuation** claim, not an event-causality claim. Second, the architecture is the only thing the authors say differs from prior event-graph work — §2 states those methods "are not directly benchmarked under the empirical protocol used in this study … our distinction is architectural rather than an empirical claim of superiority over prior event-graph methods". Any statement stronger than "adds IC over the three evaluated LLM agents and 12–1 momentum under one shared portfolio rule" would therefore be `research-proposed`, not source-reported.

## Signal

**Formation timestamp.** One score per stock per signal date `t` from cutoff-available news, price–volume history, fundamentals and dated macro/market indicators; evaluation follows a **`T+1` execution convention**, and the prediction target is the **five-session return from the next open** (§3.1, §4.1). Timezone, session/candle-boundary convention, the news publication-to-cutoff lag and the treatment of articles arriving after the cutoff are **not stated in source** → `data gap`.

**Lookback.** MML retrieves temporally eligible issuer history with no printed horizon; the event graph uses a successor window `W_succ = 1–20 exchange sessions` (Appendix A); graph estimates read records **at least 25 sessions old**, and an anchor is eligible only after its full successor window, making eligible anchors **at least 45 sessions old** (Appendix A); return-association horizons `H = {1, 5, 20}` sessions with the five-session value entering the correction; Technical/Fundamental view windows, the `12–1` momentum baseline construction and any warm-up length beyond "a 2023 warm-up that initializes memory and event statistics" (§4.1) are **not stated in source** → `underspecified`.

**Long entry (source-reported, §4.1).** At each **weekly rebalance** the portfolio is **reset to equal weights on the top-scoring 10% of constituents**, trades at the **next open**, and is held until the next rebalance. Scores are cross-sectional ranks clipped to `[−1, 1]`.

**Short entry.** **None.** The rule is explicitly long-only for every strategy in Table 1; no short leg, borrow, hedge or index-short is stated anywhere in the PDF (0 occurrences of `short-sell`, `shorting`, `borrow`) → no short-side signal exists in the source.

**Exit / holding period.** Exit is implicit: full reset at the next weekly rebalance; maximum and expected holding period are not printed; no stop-loss, take-profit or time stop is stated → `data gap` on exit precedence.

**Parameters actually published (Appendix A — the "fixed scales", frozen before evaluation).** Confidence floor `c ≥ 0.30`; Base Alpha clip `(−1, 1)`; macro multiplier `clip(1 + 0.25 µ χ, 0.75, 1.25)`; successor window 1–20 sessions; 25-session record maturity; 45-session anchor eligibility; three-state regime; Beta priors `α_p = β_p = α_q = β_q = 1`, `ε = 1e-12`; edge filters `n_e ≥ 5`, `p_e ≥ 0.30`, `L_e ≥ 1.5`, non-self transitions only, **at most 8 outgoing edges per query state**; association horizons `{1, 5, 20}` with `σ_ret = max(σ̂, 0.02)` and association forced to zero unless `J > 1` and `σ̂ > 1e-12`; support factor `R_e = min(1, n_e/20)·min(1, D_e/8)·min(1, n_e/10)·min(1, (N_ζ − n_A)/30)`; stored reliability `ρ_stored = clip(R_e · min(1, max_h |s_assoc|/2), 0, 1)` and fallback `ψ(x) = min(1, |x|/2)` else `0.5`; lag-alignment weight `w_lag = exp[−½((ℓ_e − h)/max(σ_ℓ,e, 1.5))²]` with `ω(e) = w_lag,5 / Σ_h w_lag`; edge contribution `η_e = sclip^0.25(ρ_obs · tanh(log clip(L_e, 1e-6, 20)) · tanh(θ_e/σ_ret))` and `C_i,e,t = sclip^0.25[x_i,A,t · 0.6 · p_e · η_e · ω(e)]`; graph bound `τ_Δ = 0.20`; residualizer clips the raw graph signal to `[−3, 3]`, uses average ranks versus Base Alpha and technical view, fits an intercept rank regression on at least 20 common stocks, and assigns zero correction to degenerate residuals or stocks without a retained edge; final `λ_Δ = 0.30`, `s_Δ = 1/3`, score clip `(−1, 1)`.

**Not printed (blocking exact reconstruction):** the actual three index-volatility level cutoffs for `ζ_t`; the bounds of `µ_t` and `χ_i,t`; the matured-feedback scale `s_fb` when feedback *is* eligible; the matched-state importance `x_i,A,t` normalization detail beyond "normalized to mean one"; the exact prompt texts, model decoding parameters and update rules for view weights ("frozen update rules", §4.1, never printed); and every model/API configuration → `underspecified`. **No code is released, so the signal is partially specified: fully reconstructable in structure, not in numbers.**

**Position sizing / rebalance cadence.** Equal weight across the top 10% of a ~100-name (NDX) or ~80-name (HSI) universe, weekly reset, ~10 names per book; participation caps, position limits and partial-fill handling → `not stated in source`.

## Required data

- **Instrument / universe:** Nasdaq-100 constituents (U.S.) and Hang Seng Index constituents (Hong Kong) with **date-specific membership** (§4.1). No futures, no perpetuals, no options, no crypto.
- **Venue / data vendor:** Alpha Vantage (prices, financials, market indicators, U.S. news) and Tushare Pro (Hong Kong data; `https://tushare.pro/document/2`), both `Accessed September 26, 2026` per the source's References. Whether any vendor supplies a true point-in-time news archive with publication timestamps is `data gap`.
- **Timeframe / fields:** daily signal dates; adjusted prices; financials; news (English for the U.S., English **and** Chinese for Hong Kong); market indicators; dated macro/market indicators `M_t`; a 2023 warm-up year used to initialize memory and event statistics; weekly rebalance; five-session forward target from the next open.
- **Sample period (§4.1):** evaluation **2024-01-02 → 2026-03-30**, i.e. **562 U.S. signal dates** and **551 Hong Kong signal dates** (Table 3 Panel A repeats 562 / 551; pooled comparisons use **534 shared valid dates**).
- **Point-in-time:** the source asserts cutoff-available inputs, a frozen graph, matured-only outcome memory and date-specific membership, and states that prompts/hyperparameters/update rules/portfolio rule/trading costs were **frozen at the end of the 2023 warm-up with identical hyperparameters in the two markets and "No setting was tuned, selected, or revised using 2024–2026 data"** (§4.1). Publication-lag modelling, revisions, delistings and corporate-action handling → `data gap`.
- **Benchmark fields:** NDX and HSI index levels (Table 1 Panel B, Figure 4), **stated to exclude costs**.
- **Not used:** order book, trades/aggressor side, open interest, funding, mark/index/basis, borrow, options surface, on-chain fields — none appear in the source.

## Execution assumptions

**Source-reported (§4.1 "Portfolio and frozen configuration", §4.3 robustness sentence, Figure 4 caption).**

- Signal at date `t` → **trades at the next open** (T+1), weekly full reset to equal-weight top-10% of constituents, held to the next rebalance.
- **Costs: `4+4 bp` per side in the U.S. and `10+4 bp` in Hong Kong, explicitly "commission plus slippage"**, frozen before evaluation and identical across the two markets' rules.
- **Cost stress:** §4.3 reports "per-side costs of 20 and 28 bp leave Sharpe ratios of 1.551 and 1.659" — text only, **no table**, and the mapping of 20/28 bp to the two markets' default 8/14 bp per-side schedules is not explained → `data gap`.
- **Robustness variants reported in text only:** dropping the ten largest caps keeps IC and RankIC significant in both markets (Newey–West `t ≥ 2.69`); Qwen3-Max in every LLM role gives U.S. IC 0.0281 / ICIR 0.1958 — but **Qwen3-Max is never run through the portfolio backtest** (§6).
- **Statistical machinery:** Newey–West `t` with 5 lags for the overlapping five-session target (20-lag IC values 4.72 and 2.28 printed in the Table 3 note); one-sided paired **20-session block bootstrap, 5,000 replications**, with **Holm adjustment by market and metric** (6-row U.S. families, single-row Hong Kong family); unadjusted Panel C comparison explicitly declared outside the Holm family.
- **Backbone:** DeepSeek-V4-Flash (DeepSeek-AI 2026) **without fine-tuning** for every reported portfolio result.

**Not modelled anywhere in the PDF (word census of the pinned text, Methods-level: §3, §4.1, §4.3, Appendix A).** `bid-ask`/`spread` **0**, `market impact` **0**, `latency` **0**, `fill`/`filled` **0**, `maker` **0**, `taker` **0**, `order type`/`market order`/`limit order` **0**, `participation` **0**, `turnover` **0**, `capacity` **0**, `leverage` **0**, `margin` **0**, `funding` **0**, `borrow` **0**, `short-sell`/`shorting` **0**, `walk-forward` **0**, `placebo` **0**, `benjamini`/`fdr`/`multiple testing`/`deflated` **0**, `cagr` **0**, `crypto`/`bitcoin`/`perpetual` **0**, `risk-free` **0**; `transaction cost(s)` 2 + 1, `slippage` 1, `commission` 1 (all inside the single §4.1 cost sentence), `backtest(ing)` 1 + 1, `drawdown` 3, `holm` 9, `point-in-time` 20. So: **order type, fill model, signal-to-order delay beyond T+1, latency, participation, turnover, capacity, leverage/margin, borrow, spread and impact all stay `data gap` — never zero.** LLM inference/API cost is likewise `data gap` (no compute, token or API-cost accounting appears).

**Research-proposed (not from the source) if this record is ever executed:** a symmetric per-side cost ladder of 0 / 1 / 2.5 / 5 / 10 bp, an explicit quoted-spread-crossing fill test, a 20% ADV participation cap, explicit turnover reporting from the weekly top-10% reset, and an LLM inference-cost ledger per signal date — each a `research-proposed` operationalization, not a source claim.

## Evidence

### Source-reported

All figures below are third-party claims from the pinned v1 PDF; portfolio metrics are **net of the §4.1 cost schedule** (`4+4 bp` per side U.S., `10+4 bp` per side Hong Kong) while **NDX/HSI index rows exclude costs** (Table 1 caption, Figure 4 caption); ICIR/RankICIR are **not annualized**; ARR and MDD are in % with MDD printed as a positive loss; `†`/`‡` mark lag-5 Newey–West `t > 1.96` / `2.58`. **None of these numbers has been independently reproduced.**

**Table 1 Panel A — prediction quality, daily cross-sectional correlation against the five-session next-open return:**

| Method | U.S. IC | U.S. ICIR | U.S. RankIC | U.S. RankICIR | HK IC | HK ICIR | HK RankIC | HK RankICIR |
|---|---|---|---|---|---|---|---|---|
| MEME | 0.0216 | 0.1135 | 0.0254 | 0.1228 | 0.0013 | 0.0067 | 0.0156 | 0.0794 |
| R&D-Agent-Quant | 0.0188 | 0.0796 | 0.0177 | 0.0706 | 0.0011 | 0.0048 | 0.0125 | 0.0630 |
| AI Hedge Fund | 0.0077 | 0.0595 | 0.0094 | 0.0845 | −0.0018 | −0.0121 | 0.0033 | 0.0264 |
| Momentum (12–1) | 0.0316 | 0.1274 | 0.0322 | 0.1324 | 0.0160 | 0.0645 | 0.0327 | 0.1312 |
| **RICE-Alpha** | **0.0350‡** | **0.2928** | **0.0360‡** | **0.2927** | **0.0283†** | **0.1986** | **0.0395‡** | **0.2514** |

**Table 1 Panel B — strategy performance (net of costs; index rows exclude costs):**

| Method | U.S. ARR | U.S. Sharpe | U.S. MDD | U.S. CR | HK ARR | HK Sharpe | HK MDD | HK CR |
|---|---|---|---|---|---|---|---|---|
| Index (NDX / HSI) | 20.66 | 0.986 | 24.37 | 0.848 | 22.24 | 0.952 | 21.24 | 1.047 |
| MEME | 10.60 | 0.591 | 22.38 | 0.474 | 11.07 | 0.638 | 15.72 | 0.704 |
| R&D-Agent-Quant | 11.62 | 0.567 | 27.24 | 0.427 | 17.43 | 0.929 | 16.32 | 1.068 |
| AI Hedge Fund | 10.97 | 0.700 | 17.52 | 0.626 | 27.84 | 1.130 | 20.13 | 1.383 |
| Momentum (12–1) | 18.94 | 0.889 | 21.46 | 0.883 | 23.10 | 1.098 | 13.23 | 1.746 |
| **RICE-Alpha** | **30.86** | **1.656** | **12.09** | **2.552** | **36.64** | **1.725** | **11.83** | **3.097** |

**Table 2 — U.S. cumulative ablation (IC / ICIR / RankIC / RankICIR):** complete `0.0350 / 0.2928 / 0.0360 / 0.2927`; `w/o C3 (direct)` `0.0260 / 0.2203 / 0.0290 / 0.2437`; `Reliability only` `0.0326 / 0.2706 / 0.0330 / 0.2665`; `Residualization only` `0.0208 / 0.1777 / 0.0242 / 0.2040`; `w/o C2–C3 (memory)` `0.0191 / 0.1469 / 0.0205 / 0.1531`; `w/o C1–C2–C3` `0.0064 / 0.0472 / 0.0090 / 0.0641`; `Single-agent run` `0.0148 / 0.0925 / 0.0142 / 0.0828`; `Qwen3-Max backbone` `0.0281 / 0.1958 / 0.0291 / 0.2012`.

**Table 3 Panel A — RICE-Alpha means with Newey–West `t` (lag 5):** U.S. 562 dates, IC `0.0350 (4.31)`, RankIC `0.0360 (4.24)`; Hong Kong 551 dates, IC `0.0283 (2.48)`, RankIC `0.0395 (3.10)`; pooled 534 shared dates, IC `0.0317 (4.17)`, RankIC `0.0377 (4.41)`. Table note also prints 20-lag IC values `4.72` and `2.28`.

**Table 3 Panel B — paired increments of RICE-Alpha over each comparator (increment, t_diff, p_boot, p_Holm):** U.S. vs `w/o C1–C2–C3` IC `0.0286, 3.80, 0.0002 (0.0012)` and RankIC `0.0270, 3.40, 0.0004 (0.0024)`; vs `w/o C2–C3` IC `0.0159, 3.70, 0.0002 (0.0012)` and RankIC `0.0155, 3.34, 0.0004 (0.0024)`; vs `w/o C3` IC `0.0090, 2.44, 0.0096 (0.0192)` and RankIC `0.0070, 1.82, 0.0444 (0.0480)`; vs `AI Hedge Fund` IC `0.0252, 2.58, 0.0024 (0.0072)` and RankIC `0.0246, 2.64, 0.0024 (0.0096)`; vs `Residualization only` IC `0.0142, 2.86, 0.0008 (0.0032)` and RankIC `0.0118, 2.27, 0.0120 (0.0360)`; vs `Reliability weighting only` IC `0.0023, 1.66, 0.0378 (0.0378)` and RankIC `0.0030, 2.02, 0.0240 (0.0480)`; Hong Kong vs `AI Hedge Fund` IC `0.0305, 2.52, 0.0020 (0.0020)` and RankIC `0.0370, 3.06, 0.0004 (0.0004)`. **Table 3 Panel C (declared outside the Holm family):** reliability-only minus residualization-only, U.S. IC `0.0119, 2.35, 0.0050`, RankIC `0.0087, 1.67, 0.0406`.

**Table 4 — behaviour in falling and rising markets (Capture down/up; Crash = return in the index's largest drawdown; Down mo. = mean return in the 7 U.S. / 13 HK down months):** Index `1.00/1.00, −24.4, −4.5 | 1.00/1.00, −21.2, −3.3`; MEME `0.28/0.33, −20.8, −4.1 | 0.02/0.11, +3.5, +0.2`; R&D-Agent-Quant `0.29/0.35, −24.9, −4.9 | 0.25/0.33, −11.8, −1.8`; AI Hedge Fund `0.73/0.71, −17.0, −3.2 | 0.93/0.97, −20.1, −2.8`; Momentum (12–1) `0.83/0.85, −16.8, −4.1 | 0.58/0.64, −9.3, −1.4`; **RICE-Alpha `0.51/0.65, −10.9, −0.4 | 0.34/0.51, −9.2, +1.3`**.

**Text-only claims (no table anchoring them):** U.S. daily IC dispersion SD `0.120` (RICE-Alpha) vs `0.248` (momentum); Hong Kong retains `81%` of U.S. IC; best agent baselines "at most `0.0216` and `0.0013`"; Holm-adjusted paired `p ≤ 0.0096` vs AI Hedge Fund; net ARR beats the indices by `10.20` and `14.40` points; U.S. baselines' beta `0.20` (MEME) and `0.18` (R&D-Agent-Quant); RICE-Alpha outperformed the index in `6 of 7` U.S. down months and `all 13` Hong Kong down months; single-agent two-sided block-bootstrap `p = 0.020` (IC) and `0.042` (RankIC); drop-ten-largest-caps `t ≥ 2.69`; 20/28 bp per-side stress → Sharpe `1.551` / `1.659`; Qwen3-Max U.S. IC `0.0281`, ICIR `0.1958`.

### Independently reproduced

not independently reproduced. No scoring pipeline was run, no Alpha Vantage or Tushare data was pulled, no baseline was re-run and no metric was recomputed from returns for this record. The only quantities computed here are (a) file/page/byte/SHA-256 checksums of the pinned v1 artefacts, (b) a word census of the pinned text, and (c) arithmetic-only consistency checks of printed cells: Calmar `= ARR / MDD` reproduces **all 12** Table 1 Panel B cells to ±0.001 (e.g. `30.86/12.09 = 2.553` vs printed `2.552`; `22.24/21.24 = 1.047`); `ICIR = IC / SD` reproduces momentum U.S. `0.0316/0.248 = 0.1274` and implies SD `0.1195 ≈ 0.120` for RICE-Alpha, matching the §4.2 text; ARR gaps `30.86 − 20.66 = 10.20` and `36.64 − 22.24 = 14.40` match §4.2; HK/US IC retention `0.0283/0.0350 = 80.9% ≈ 81%` matches §4.2; single-agent increments `0.0350 − 0.0148 = 0.0202` and `0.0360 − 0.0142 = 0.0218` match §4.3; the Table 2 ablation ladder is monotone as claimed; and the Table 3 Holm family **reproduces exactly** for both U.S. metrics (IC raw `{0.0002, 0.0002, 0.0008, 0.0024, 0.0096, 0.0378}` → adjusted `{0.0012, 0.0012, 0.0032, 0.0072, 0.0192, 0.0378}`; RankIC raw `{0.0004, 0.0004, 0.0024, 0.0120, 0.0240, 0.0444}` → adjusted `{0.0024, 0.0024, 0.0096, 0.0360, 0.0480, 0.0480}`), confirming the reported `p_Holm` column. The pooled mean `0.0377` vs the simple average of the two market RankICs `(0.0360 + 0.0395)/2 = 0.03775` differs only by rounding on a different date set (534 vs 562/551) and is **not** independently checkable from printed values.

### Negative evidence

1. **Author-acknowledged LLM look-ahead.** §6: "Both models may contain information that postdates individual forecasts." The entire point-in-time design sits on top of a pretrained backbone whose knowledge may include 2024–2026 news and prices; the paper does not test a cutoff-safe backbone → the PIT claim is unverifiable at the model layer.
2. **Author-acknowledged evaluation-period selection, uncorrected.** §6: "Evaluation-period selection can make estimates optimistic; tests of the selected series do not adjust for this selection."
3. **No out-of-sample period at all.** The frozen-2023-warm-up design is strong, but the claim rests on a **single** 2024-01-02 → 2026-03-30 window; `holdout`, `validation set`, `test set`, `walk-forward` each appear **0** times in the pinned text. There is no second window, no rolling origin and no pre-declared future test.
4. **Almost no multiple-testing control.** `benjamini`, `fdr`, `multiple testing`, `deflated`, `placebo` each appear **0** times. Holm (9 occurrences) applies only inside the paired ablation family (6 rows per market per metric); nothing corrects for 8 reported metrics × 2 markets × 8 configurations × 3 robustness analyses, nor for choosing this evaluation period.
5. **No run-to-run stability for a stochastic LLM system.** `seed` appears **0** times; no repeated decoding runs, no temperature disclosure, no variance of IC/Sharpe across runs. (For contrast, `favor-hypothesis-grounded-agentic-factor-validation-topk-portfolio-2026-09-24.md` reports 10-run dispersion with AR std equal to its headline.)
6. **Turnover never reported.** `turnover` appears **0** times, yet the rule fully resets an equal-weight top-10% book every week; without a turnover figure the stated 8/14 bp per-side costs cannot be checked and the net-Sharpe claim cannot be stress-tested.
7. **Flat, unmeasured cost model.** Slippage is asserted as a constant (4 bp U.S., 4 bp HK) inside a single sentence; `spread`, `bid-ask`, `market impact`, `latency`, `fill`, `maker`, `taker`, `order type`, `participation` all appear **0** times. The 20/28 bp stress is text-only, unexplained relative to the 8/14 bp defaults, and still a flat schedule.
8. **No capacity, leverage or borrow treatment.** `capacity`, `participation`, `leverage`, `margin`, `funding`, `borrow`, `shorting` = **0** occurrences; there is no short leg, so the reported Sharpe contains whatever market beta the top-decile book carries — and **RICE-Alpha's own beta is never printed** (only baselines' U.S. betas 0.20/0.18 are, §4.4).
9. **Benchmark asymmetry.** Index rows exclude costs while strategy rows are net of costs (Table 1 caption), yet §4.2 compares "net ARR exceeds the indices by 10.20 and 14.40 points" — a disclosed but real apples-to-oranges gap.
10. **Narrow baseline set.** Three LLM agents (MEME, R&D-Agent-Quant, AI Hedge Fund), one 12–1 momentum and the index. No value, quality, low-volatility, short-term reversal or news-count factor baseline; prior event-graph methods are explicitly **not** benchmarked (§2), so "strongest results among the evaluated methods" is scoped to a thin field.
11. **Two robustness claims have no printed numbers.** The drop-ten-largest-caps test (`t ≥ 2.69`) and the 20/28 bp cost stress (Sharpe 1.551 / 1.659) exist only in one sentence of §4.3 — no table, no sample detail, no Market split → `data gap`.
12. **Backbone robustness is prediction-only.** Qwen3-Max is evaluated for IC/ICIR (Table 2) but §6 states "Portfolio evaluation uses DeepSeek-V4-Flash; Qwen3-Max is evaluated only for prediction quality" — so the 1.656 / 1.725 Sharpe numbers are single-backbone.
13. **Claims without printed statistics.** §4.2 asserts momentum and AI Hedge Fund IC/RankIC are "not significant in either market", but Table 3 contains no rows for them → their `t` values are `data gap`.
14. **Reproducibility gap.** No code, no prompts, no point-in-time news archive, no data-availability statement, no acknowledgments/funding/COI; vendors are commercial APIs accessed the day before submission; every baseline row is the authors' own re-run inside their own harness.
15. **Defensive reading is beta-confounded.** Down-market capture 0.51 (U.S.) / 0.34 (HK) and up-capture 0.65 / 0.51 mean the book is materially less exposed than the index; the MDD advantage (12.09 vs 24.37) partly follows from that exposure, and no beta-adjusted return or information ratio versus the index is reported (CR is ARR/MDD of the raw series).
16. **Hong Kong edge is thinner than the headline.** HK RankIC 0.0395 vs momentum 0.0327 (a 0.0068 gap) and HK IC carries only `†` (`t = 2.48 < 2.58`); LLM baselines collapse to near zero in HK, so the HK "win" is largely against failing systems.
17. **The reported parenthetical that does not hold** (see `contradictions`): §4.2's "(at most 6% of their U.S. values)" fails for AI Hedge Fund by an order of magnitude and is exceeded by MEME's 6.02%.
18. **Cost of the signal itself is invisible.** No inference/API/compute accounting appears anywhere; a daily multi-agent LLM run over ~100 names × 562 + 551 dates is a material unpriced cost.
19. **Status and maturity.** Single-authorship-order preprint, v1 only, cs.LG only, no journal reference, no peer review, 15 pages / 4 tables; submitted 2026-09-27 with data vendor access stamps of 2026-09-26.
20. **Metric definitions are partial.** `risk-free` appears **0** times and the Sharpe construction (annualization, risk-free series) is never stated; ARR is described only by the caption note "ICIR and RankICIR are not annualized", implying ARR is annualized without defining it → `data gap`.
21. **Zero crypto content.** `crypto`, `bitcoin`, `perpetual` each appear **0** times in the pinned text.

## Falsification plan

Every threshold below is a `research-defined falsification threshold` (Scout-chosen, not the source's) with an explicit action on failure. **Global rule: no retuning.** Windows, thresholds, the top-10% rule, the cost schedule, the regime states, `λ_Δ`, the edge filters and the benchmark set are frozen as printed; a gate that fails may not be rescued by re-optimizing any of them — failure changes the record's status, not the configuration.

- **F1 — Printed-value reproduction.** Re-run the frozen pipeline on the same panels. Fail if reproduced U.S. IC misses `0.0350 ± 0.0025`, HK IC misses `0.0283 ± 0.0025`, or U.S./HK Sharpe miss `1.656 ± 0.15` / `1.725 ± 0.15`. Action: mark every headline `unverified`.
- **F2 — Stochastic-stability gate.** Five independent re-decodings (plus temperature 0). Fail if `std(IC)` across runs ≥ `0.0035` (10% of headline IC) or if any run's U.S. IC ≤ 0. Action: treat the headline as a single lucky draw; downgrade to `falsified-robustness`.
- **F3 — Backbone look-ahead gate.** Re-run with a backbone whose knowledge cutoff precedes 2024-01-02 (or a locally served, cutoff-bounded model) with prompts unchanged. Fail if U.S. IC falls below `0.0175` (half the headline). Action: reattribute the result to post-hoc knowledge; the PIT claim fails.
- **F4 — News-availability lag gate.** Enforce strict publication-timestamp admission (only articles published before the prior close). Fail if U.S. IC falls below `0.0175`. Action: reclassify the signal as latency-contaminated.
- **F5 — Cost ladder and turnover gate (`research-proposed`).** Report turnover, then reprice at 0 / 1 / 2.5 / 5 / 10 / 20 bp per side. Fail if U.S. Sharpe ≤ `0.50` at 5 bp per side, or if reported weekly turnover exceeds `60%` of book value. Action: reject the net-alpha reading; keep only the IC claim.
- **F6 — Capacity gate (`research-proposed`).** Cap participation at 20% of 20-day ADV for the ~10-name book. Fail if Sharpe degrades by more than `0.10` versus the unconstrained run. Action: mark capacity `unproven` and bound position size explicitly.
- **F7 — Family-wide multiplicity gate.** Apply Benjamini–Hochberg at `q < 0.10` across the full reported family (4 predictive + 4 portfolio metrics × 2 markets × 8 configurations), plus a deflated-Sharpe check with trial count equal to the number of configurations actually inspected. Fail if the headline IC/Spearman family does not survive at `q < 0.10`. Action: reclassify significance as selection artifact.
- **F8 — Mechanism placebo (`research-proposed`).** 1,000 circular-shift / issuer-label-shuffled event-graph draws that preserve marginal event frequencies but destroy issuer-local succession. Fail if the real U.S. IC is not above the 95th percentile of the placebo distribution. Action: the event-continuation mechanism is unsupported even if returns survive.
- **F9 — Ablation-ladder gate.** Reproduce Table 2. Fail if `w/o C1–C2–C3` IC ≥ `0.0191`, or if the full-system increment over memory-only is `< 0.010` IC. Action: restrict the claim to "memory alone" (which the source says still beats every baseline at ICIR 0.1469).
- **F10 — Cross-universe replication gate.** Frozen hyperparameters on (a) a U.S. mid/small-cap panel and (b) one third market not in the paper. Fail if U.S. mid/small-cap IC ≤ 0 **or** the third-market IC ≤ 0. Action: restrict the claim to large-cap index constituents.
- **F11 — Frozen forward window.** Score 2026-04-01 onward with everything frozen (the paper's sample ends 2026-03-30). Fail if forward U.S. IC ≤ 0 or forward Sharpe ≤ 0 over ≥ 12 months. Action: reject persistence; record as sample-bound.
- **F12 — Baseline-breadth gate.** Add value, quality, low-volatility, 1-month reversal, a naive news-count factor and the index as comparators under the same top-10% rule. Fail if the best non-LLM baseline reaches IC ≥ `0.0300` (i.e. within `0.005` of the headline). Action: attribute the edge to the portfolio rule or generic cross-section, not to the event graph.
- **F13 — Data-access gate.** Attempt to rebuild the point-in-time news stream and date-specific membership from a reproducible source. Fail if publication-timestamped news or as-of membership cannot be obtained independently. Action: keep the record `research-only` permanently; no implementation attempt.
- **F14 — Crypto replication gate (`research-proposed`).** Port the issuer-local successor graph (event types redefined for token/exchange events) to a liquid-token cross-section with the same frozen scales. Fail if IC ≤ 0. Action: `crypto portability: unproven` stands permanently; no crypto candidate-pool entry.

## Crypto portability

**unproven.** The pinned text contains **0** occurrences of `crypto`, `bitcoin` or `perpetual`; every empirical claim is on Nasdaq-100 and HSI constituents. Porting risks:

- **Event ontology:** the mechanism needs a high-volume stream of *typed, issuer-local, temporally ordered* corporate events with a news wire that supports point-in-time replay. Crypto has token/exchange/governance events with different typing, far noisier duplicates and heavy bot-generated coverage; the NEW/UPDATED/CARRIED lifecycle that prevents double-counting would have to be redesigned → `research-proposed`.
- **Universe breadth:** a top-10% long-only book over ~100 names needs a liquid investable cross-section; most tradable token universes are far narrower and dominated by BTC/ETH beta, so cross-sectional IC is not comparable.
- **Session structure:** 24/7 candles, venue-specific day boundaries and timezone conventions differ from exchange sessions; the source states **no** timestamp convention at all (`data gap`), which matters more in 24/7 markets.
- **Perpetuals/funding/shorting:** no funding, basis, borrow, margin or liquidation model exists in the source, and the rule is long-only — a crypto perp port would add mechanics the paper never addresses (mark/index price, funding P&L, ADL/liquidation).
- **Execution:** crypto taker fees plus real spreads make the flat 4 bp slippage assumption unportable; the paper has no spread, impact, latency or fill model at all.
- **Pretraining look-ahead:** amplified in crypto, where LLM training corpora are dense with post-2024 price and event discussion.
- **Venue survivorship/delistings:** far more severe than in index constituents, where the source already leaves delisting handling unstated.

This is a ported hypothesis, not crypto empirical evidence; `crypto portability: unproven` — and a port is not a trading authorization.

## Limitations

- `underspecified`: regime level cutoffs, macro/beta bounds, `s_fb` when feedback exists, `x_i,A,t` detail, prompt texts, decoding parameters, view-weight update rules, Technical/Fundamental lookbacks, momentum-baseline construction, exit precedence, turnover level, Sharpe/ARR definitions, timezone/session and news-lag convention, and the mapping from 20/28 bp stress to the 8/14 bp defaults.
- `data gap`: code, prompts, point-in-time news archive, as-of membership file, delisting/corporate-action handling, order type, fill model, latency, participation, capacity, leverage/margin, borrow, spread, impact, LLM inference cost, RICE-Alpha's own beta, t-statistics for the "not significant" baselines, ORCID/funding/COI/acknowledgments, and peer-review status.
- `not independently reproduced`: every performance and significance number in this record.
- `unproven`: that event-continuation (rather than the backbone's latent knowledge or the portfolio rule) produces the edge — the source's own §6 concedes possible post-dated model information, and there is no placebo, no cutoff-safe backbone test and no out-of-sample window.
- Disclosed asymmetries: strategy rows net of costs vs index rows gross (Table 1 caption); defensive capture partly explains the drawdown advantage; Hong Kong comparison is largely against LLM baselines that collapse there.
- One unreconciled printed statement (`contested: true`, see `contradictions`): the "(at most 6% of their U.S. values)" parenthetical.
- Single preprint, v1, 15 pages / 4 tables, no peer review, single evaluation window, single portfolio backbone, single run per configuration, text-only robustness claims, and zero crypto evidence.

## Implementation status

`implementation_status: not-implemented`. Nothing from this record has been implemented in our research stack: no RICE-Alpha pipeline, no Alpha Vantage or Tushare pull, no LLM scoring run, no Qlib backtest, no candidate-pool entry, no Paper / Testnet / Live activity, and no write to any downstream system. This artifact is a normalized research capture only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this file in the staging repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered `/results/_handoff/candidates.json`; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. Those stages remain separate and gated.

## Related Wiki records

Verified by `kb_search` on 2026-09-29 (no page was fabricated; queries for `event-driven news sentiment graph stock return predictability`, `LLM financial agent memory retrieval layered memory trading equity` and `cross-stock semantic network reversal predictability` returned **0** pages, so no mechanism-matching page exists yet):

- `[[quant/news-event-tag-drift-rumor-resolution-placebo-adjusted-momentum-2026-09-02]]` — news-event drift/rumor resolution with placebo-adjusted abnormal returns; adjacent event-driven news alpha, different source and different mechanism (event-window timing vs graph-continuation residual).
- `[[quant/llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04]]` — leakage-safe, search-aware deflated evaluation; this is precisely the multiple-testing discipline this record's Negative evidence items 3–4 show the source does not apply.
- `[[quant/sentiment-augmented-drl-alpha-reward-ddpg-active-trading-2026-09-05]]` — sentiment-augmented alpha reward for active trading; adjacent LLM/sentiment signal family, different mechanism.

Adjacent repository records (file paths, **not** verified Wiki pages): `llm-augmented-semantic-network-cross-stock-reversal-2026-09-04.md` (arXiv 2604.19476 — cited by this source but not benchmarked by it), `llm-event-aware-sentiment-factor-contrarian-alpha-2026-09-04.md`, `favor-hypothesis-grounded-agentic-factor-validation-topk-portfolio-2026-09-24.md`, `evolvetrade-self-evolving-llm-tool-use-policy-agent-15-us-bluechips-2026-09-26.md`, `frozen-llm-checkpoint-outlook-score-cross-sectional-us-equity-arxiv-2604.21433-2026-09-22.md`.

## Sources

1. Tong Liu, Lanmiao Liu, Xiang Hu. *"RICE-Alpha: Reliability-Informed Correction with Event Graphs for LLM-Agent Stock Forecasting."* arXiv:2609.34004v1 [cs.LG], submitted 27 Sep 2026 23:03:31 UTC (landing prints `(786 KB)` for v1). Landing page: https://arxiv.org/abs/2609.34004 (retrieved 2026-09-29; Comments `15 pages, 4 figures, 4 tables`; Journal-ref and external DOI fields empty; Subjects `Machine Learning (cs.LG)`; one version only).
2. Pinned full text: https://arxiv.org/pdf/2609.34004v1 — 15 pages, 1,103,328 bytes, SHA-256 `2de1d5766a752441bb71917789f43825efd33ce631f641aa89a6b477e106d26c`; every table, figure caption and Appendix A constant cited above was read directly from this PDF on 2026-09-29 (pypdf 6.11.0, 54,984 characters).
3. Cross-check text: https://arxiv.org/html/2609.34004v1 — 303,357 bytes, fetched 2026-09-29; used to confirm section structure and the `License: CC BY 4.0` line.
4. arXiv DOI: https://doi.org/10.48550/arXiv.2609.34004 (the only DOI in the pinned metadata).
5. Data/software cited by the source (**not fetched** for this record): Alpha Vantage API documentation `https://www.alphavantage.co/documentation/` (`Accessed September 26, 2026`), Tushare Pro `https://tushare.pro/document/2` (`Accessed September 26, 2026`), and the baseline repository `https://github.com/virattt/ai-hedge-fund` (Singh 2024, `Accessed September 26, 2026`). Baselines named in §4.1: MEME (Guo et al., arXiv:2602.11918), R&D-Agent-Quant (Li et al., NeurIPS 2025), AI Hedge Fund (Singh 2024), plus a price-only 12–1 momentum baseline.
