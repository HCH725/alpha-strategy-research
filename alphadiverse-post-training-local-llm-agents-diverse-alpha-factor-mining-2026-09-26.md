---
schema: strategy-research-record-v1
title: "AlphaDiverse: post-trained local LLM research agents for diverse alpha-factor mining on Chinese equity universes (arXiv:2609.29014v1)"
created: 2026-09-26
updated: 2026-09-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - llm-agents
  - alpha-factor-mining
  - post-training
  - grpo
  - chinese-equities
  - cross-sectional
  - out-of-sample-protocol
status: research-only
confidence: medium
source_as_of: 2026-09-24
sources:
  - "https://arxiv.org/abs/2609.29014 (arXiv:2609.29014v1 [cs.AI primary; cs.CE, cs.MA cross-lists], submitted Thu 24 Sep 2026 04:29:37 UTC; Comments field: '33 pages, 7 figures, 26 Tables. Preprint under review'; no journal-ref field; only version — https://arxiv.org/abs/2609.29014v2 returns HTTP 404, checked 2026-09-26)"
  - "https://arxiv.org/html/2609.29014v1 (pinned full text, 721691 bytes, SHA-256 62f9874d1ff300f2a131d84206a2eed8b5f0456e927aec4b25c6fdf786750eb1, downloaded 2026-09-26, converted to 122781 characters / 3461 lines and read end to end: Abstract, Sections 1-5, References, Appendices A-D, Tables 1-26, figure captions, plus a raw-HTML cell-level re-extraction of Tables 9 and 14 whose inline math does not survive text conversion)"
  - "https://arxiv.org/pdf/2609.29014v1 (pinned PDF, 866237 bytes, SHA-256 ce17a92282f8825e019fa0328201ee0707807c957efa652194d45fda37d4ffb0, downloaded 2026-09-26; pdfinfo reports 33 pages and document authors 'Qingzhuo Wang; Zikun Wei; Zhihua Wei; Wen Shen', matching the landing page)"
  - "https://doi.org/10.48550/arXiv.2609.29014 (DataCite DOI, HTTP 302 -> https://arxiv.org/abs/2609.29014, checked 2026-09-26)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Source-internal table cross-reference errors, our count on the pinned v1 HTML read 2026-09-26: the Section 3.3 'Module ablations' paragraph says 'As Table 4 shows, removing complementarity ...' while the module-ablation table is captioned 'Table 3: Results of Module ablations (GPT-5.5)'; the Section 3.3 'Data ablations' paragraph says 'As Table 6 shows, improvement-only selection loses useful mechanisms' while the SFT-data ablation table is captioned 'Table 5: SFT-data ablations' (Table 6 is 'Deployment costs on CSI300'). Every ablation number below is therefore attributed to the captioned table, not to the in-text pointer."
  - "Comparability caveat declared by the source itself rather than resolved: Appendix C.3 states 'we give every ML/DL baselines the same base factors to isolate the prediction architecture' while Section 3 states 'Main comparisons use all available features' for the agentic methods, so the Table 1 ML/DL column and the agentic column do not share an information set. The paper does not print an agentic-vs-ML/DL run under a matched feature set."
---

# AlphaDiverse: post-trained local LLM research agents for diverse alpha-factor mining on Chinese equity universes (arXiv:2609.29014v1)

## Provenance

- **Paper**: Qingzhuo Wang, Zikun Wei, Zhihua Wei, Wen Shen, *AlphaDiverse: Post-Training Local Quantitative Research Agents for Diverse Exploration in Alpha Factor Mining*, `arXiv:2609.29014v1 [cs.AI]`.
- **Affiliations printed on the manuscript title block**: `Tongji University` and `Shanghai Non-convex Intelligent Technology`, with two footnotes — "Work done during an internship at Shanghai Non-convex Intelligent Technology" and "Corresponding Author". The **per-author affiliation mapping and which author is the corresponding author are not stated in source**; the paper prints the two institutions as a single block.
- **Version / date**: only `v1`, submitted **Thu 24 Sep 2026 04:29:37 UTC** (450 KB); `https://arxiv.org/abs/2609.29014v2` returns **HTTP 404** (checked 2026-09-26).
- **Comments field (verbatim)**: "33 pages, 7 figures, 26 Tables. Preprint under review". `pdfinfo` on the pinned PDF reports **33 pages**, matching.
- **Subjects**: `cs.AI` primary; `cs.CE` and `cs.MA` cross-lists. No `q-fin.*` classification.
- **DOI**: DataCite `10.48550/arXiv.2609.29014` → HTTP 302 → `https://arxiv.org/abs/2609.29014` (checked 2026-09-26). **No publisher DOI, no journal-ref (0 occurrences on the landing page), no peer-review statement anywhere in the pinned text** → **preprint only, under review, unrefereed as captured**.
- **Licence**: `arXiv.org perpetual non-exclusive license` (printed on the pinned HTML; `arxiv.org/licenses/nonexclusive-distrib/1.0/` link on the abs page) → this record cites and normalises short claims and printed figures only; no reproduction of the text.
- **Pinned primary sources**: HTML `721691 bytes`, SHA-256 `62f9874d1ff300f2a131d84206a2eed8b5f0456e927aec4b25c6fdf786750eb1`; PDF `866237 bytes`, SHA-256 `ce17a92282f8825e019fa0328201ee0707807c957efa652194d45fda37d4ffb0`. Both downloaded **2026-09-26**; the HTML was converted to `122781` characters / `3461` lines and **read end to end** (Abstract, Sections 1–5, References, Appendices A–D, Tables 1–26, figure captions).
- **Code / data / AI-use**: word-boundary scan of the pinned HTML for `github.com`, `available at`, `data availability`, `upon request`, `publicly available`, `supplementary` → **0 relevant hits** (the only `GitHub` strings are arXiv page boilerplate "Report GitHub Issue / Submit without GitHub"). **No code repository, no dataset link, no data-availability statement, no AI-use disclosure** → every availability field is `not stated in source`.
- **Source / data as-of**: inner research period **May 2022–December 2025**; outer evaluation period **January–August 2026** (Tables 17 and 18 print "January–August 2026" in their captions); arXiv v1 dated **2026-09-24**.
- **Pre-write source-identity dedup (whole repository, hidden trees included)**: `2609.29014`, `AlphaDiverse`, `Qingzhuo`, `Zikun Wei`, `Zhihua Wei`, `Qwen3.8-27B`, `research path collapse`, `useful mechanisms` → **0 hits** across all `*.md` (including `.mimo-worktrees/`, `.agents/`, `.hermes/`) and `coverage_manifest.csv` before the write; `Wen Shen` → 0 hits; the `Non-convex` / `non-convex` pattern returned 31 files, every one cleared as unrelated optimisation-convexity prose (E-Rachev, Wasserstein, fractional-Sharpe QCQP, MPEC), none mentioning AlphaDiverse, Tongji, or this manuscript.
- **Four-axis material-distinction statement vs the nearest existing repository records**: (1) `alphaschema-trading-semantic-plan-space-surrogate-guided-factor-mining-2026-09-05.md` — AlphaSchema is a *baseline inside this paper* (Tables 1, 2, 16–18), different source identity, different mechanism (surrogate-guided semantic plan search vs SFT+GRPO post-training of local Planner/Realizer policies); (2) `quantaalpha-institutional-price-volume-correlation-intraday-momentum-2026-09-05.md` — QuantaAlpha is the method that takes the highest CSI300 ARR here (43.19 vs 42.10), different source, different signal construction (original/mutated/crossover trajectory search vs complementary plan portfolios with a log-det diversity reward); (3) `anytime-valid-referee-llm-factor-mining-certified-csi500-book-2026-09-25.md` — different source, different mechanism (anytime-valid statistical referee gate vs policy post-training), different data dependency; (4) `favor-hypothesis-grounded-agentic-factor-validation-topk-portfolio-2026-09-24.md` — different source and different validation design; (5) `limt-hierarchical-multitask-liquidity-aware-ashare-cross-sectional-apo-2026-09-23.md` — same broad A-share universe but a non-agentic hierarchical multi-task predictor with a different source identity, signal construction and data dependency. Source identity differs in every pair, and mechanism differs in every pair.

## Economic mechanism

### Source-reported

The paper's stated problems are (Section 1) that agentic alpha-mining systems depend on external APIs whose cost, availability, latency and behaviour are outside the operator's control and cannot guarantee confidentiality for proprietary data, and that long research loops "tend to revisit a few successful economic mechanisms that lead to research path collapse".

The proposed remedy is a three-part framework:

1. **Multi-agent research loop (Section 2.1, Tables 7–11)**: a *Planner* proposes research plans, an *Execution* module validates and compiles factor specifications (rejecting invalid features/operators and any specification using information unavailable at prediction time, feeding rejections back as repair notices), a *Validation* screen applies coverage / predictive-quality / redundancy gates (Table 9), and an *Analysis* module writes feedback that becomes the next round's state.
2. **Diverse path collection (Section 2.2, Appendix B.1)**: traces are gathered across varied research environments — four markets × three feature masks × eight archive configurations give **96 fixed task states** (Appendix B.2) — and the Planner demonstrations are split **50/30/20** into model-improvement, productive-switch and new-direction examples so supervision covers direction changes, not only successful endpoints.
3. **Post-training of local agents (Section 2.3, Appendix B.2)**: SFT warm-starts separate LoRA adapters for a **Qwen3.8-27B** Planner and Realizer, then a **joint GRPO** update optimises both with a reward combining factor quality and *incremental useful diversity* — a log-determinant of quality-weighted prediction-change directions minus the archive's existing coverage. The trained nodes replace the API nodes; an unmodified Qwen3.8-27B serves as Analysis.

Anti-test-tuning protocol (Section 1, Appendix C.1): research feedback is confined to the **inner period (May 2022–December 2025)**; after research, factors and the model family are frozen, final training settings are picked on the last 15% of inner observations, the model is refitted on all eligible inner observations and then **evaluated once on the outer period (January–August 2026)**.

Economic-mechanism catalogue (Table 8) that the Planner must draw from, 38 entries in 6 themes: Trend and momentum (5: short horizon momentum, medium horizon momentum, trend strength efficiency, breakout continuation, return acceleration), Reversal (6), Liquidity and volume (6), Intraday structure (6), Volatility and range (7), Relative returns and crowding (8: market relative strength, market beta exposure, idiosyncratic volatility, market residual continuation, market residual reversal, cross-sectional dispersion, co-movement crowding, dependence regime).

### Research interpretation

Stated as a falsifiable hypothesis rather than a finding: **diversity-regularised post-training of research policies yields a retained factor set whose out-of-sample cross-sectional predictive content exceeds what the same research budget produces without that regularisation**. The tradable residue of that claim is deliberately narrower than the framework claim — a retained factor block plus a gradient-boosted predictor, scored cross-sectionally each day and held as an equally weighted top-quintile long-only book. Component roles: *regime/context* = fixed index-membership universe plus feature-masked research environments; *primary signal* = the mined factor block combined by LightGBM; *diversity term* = a training-time reward only, which has no direct effect on a live portfolio except through the factors it causes to be retained; *risk / exit* = **absent from the source** — the paper specifies no stop, no sizing rule and no exit other than daily re-formation of the top quintile. We do not assume any component contributes alpha; F4 and F5 below are the ablations that decide it.

## Signal

**Source-reported construction (all from the pinned v1):**

- **Formation timestamp**: "All features use information available after close" (Appendix C.1). Timezone / session / clock convention for "close" is **not stated in source** (`underspecified`; the market is Chinese equities, but the paper never prints a timezone or an availability lag).
- **Prediction target (Eq. 14)**: `y(i,t) = o(i,t+2) / o(i,t+1) − 1 − b(t)` — the stock's next-open-to-following-open return minus `b(t)`, the benchmark return over the *same* future open-to-open interval. `o(i,t)` is stock `i`'s opening price.
- **Universe / eligibility**: CSI300, CSI500, CSI1000 and the broader Shanghai/Shenzhen A-share universe, "Eligible stocks follow historical daily index membership". Exclusions: Beijing-listed stocks, ST stocks, listings younger than 60 days, suspended/delisted observations, and observations rejected by the shared opening-price-limit filters.
- **Inputs**: daily open/high/low/close, share volume, traded amount, plus minute bars. **21 initial factors** (Table 10): `ret_1, open_close_ret, high_low_range, close_position, vwap, vwap_deviation, log_turnover, log_volume, KMID, KLEN, KMID2, KUP, KUP2, KLOW, KLOW2, KSFT, KSFT2, OPEN0, HIGH0, LOW0, VWAP0`. The wider feature set adds rolling return/volatility statistics, daily Alpha158 formulas, and intraday summaries of opening/closing returns, participation, ranges and VWAP deviations (Table 11 examples: `ret_20, volatility_20, RSV20, last30_ret, first_half_ret, close_vwap_deviation`). Permitted operators: arithmetic (`at_subtract, at_divide, linear_combo`), temporal (`ts_mean, ts_rank`), cross-sectional (`cs_rank, cs_zscore`) and transforms (`at_reverse`).
- **Factor screening (Table 9, re-extracted from raw HTML cells)**: *research acceptance* — factor–target coverage `≥ 0.20`, days with valid IC `≥ 2`, factor score `s_fac ≥ 0.05`, mean absolute correlation against reference factors `≤ 0.90`; *Realizer training-pair selection* (stricter) — coverage `≥ 0.80`, valid-IC days `≥ 120`, `s_fac ≥ 0.25`, absolute RIC `≥ 0.01`, absolute RICIR `≥ 0.05`, within-pair mean absolute correlation `≤ 0.80`. Redundancy rejection is greedy: candidates are processed in decreasing factor score, so a redundant candidate loses to a stronger retained one.
- **Predictor**: LightGBM (Appendix B.2: at most 200 trees with early stopping after 50 rounds for reward evaluation; Appendix C.3: at most 500 trees, early stopping after 50 rounds, for the baseline predictor). Predictions are cross-sectional scores.
- **Portfolio rule (Appendix C.2)**: "Portfolio metrics are annualized excess return (ARR) for the equally weighted top 20% of predicted stocks" — long-only, equal weight, **"Financial tables use this same long-only portfolio definition throughout. Reported returns are gross of trading costs."** Benchmark: the corresponding index return for the index universes; the equal-weight return of eligible A-shares for the A-share universe. IR is the mean/std of daily excess return; MDD is on compounded excess wealth; CR = ARR/MDD; 252 trading days per year.
- **Data splits**: inner period May 2022–December 2025, main comparisons use one research fold with chronological train/validation/search segments in a **7:1:2** ratio, boundary observations purged for the two-opening label lookahead; after research the **last 15% of inner observations** select final training settings, then refit on all eligible inner observations; outer evaluation January–August 2026 once. Standalone ML/DL baselines fit on the earlier 85% of inner data and select on the last 15%.
- **Search budget**: 20 rounds × 4 plans × 2 specifications per plan = **160 candidate slots** per run, identical for every agentic method (Appendix C.3); evaluation inference at temperature 0.1.
- **Reward-window segments (Appendix B.2)**: nominal 252 / 63 / 126 / 63 trading days (train / validation / additional fit / reward) with label-overlap purging.

**Not reconstructible from the source (`data gap`, never invented):** the **retained factor list per market is never printed** — no paper section enumerates the final factors that produced Table 1, so the exact signal behind the headline numbers cannot be rebuilt from the document alone. Also absent: an explicit rebalance cadence (daily re-formation is implied by the daily excess-return series but **not stated in source** → `research-proposed`), order type, execution price, position limits, cash handling, treatment of suspended names inside the held book, and any entry/exit/stop/sizing rule.

**Scout-labelled operationalisation (`research-proposed`, not from the source):** form the score after the close of day `t`, buy the top 20% at the next session open, equal weight, re-form daily, benchmark against the index or the eligible-A-share equal weight. Any threshold, filter or failure rule in the Falsification plan is `research-defined`.

## Required data

- **Instrument / universe**: CSI300, CSI500, CSI1000 and Shanghai/Shenzhen A-share common stocks; **point-in-time daily index membership** for the three index universes; ST-flag history; listing-date history (for the 60-day rule); suspension and delisting flags; opening-price-limit (limit-up/limit-down at the open) flags; Beijing-exchange exclusion flag.
- **Market type / venue**: Chinese on-exchange equities (Shanghai / Shenzhen), cash spot, long-only. No derivatives, no crypto.
- **Timeframe / fields**: daily OHLC, share volume, traded amount; minute bars for the intraday feature group (opening/closing returns, participation, ranges, VWAP deviations).
- **Benchmark series**: index total/price return for the three index universes; a daily equal-weight return of eligible A-shares for the A-share universe (reconstructed by the researcher — the paper states the definition, not a vendor series).
- **Point-in-time**: membership and eligibility must be evaluated on the signal date only; the label deliberately reaches two opens forward, so **purging at segment boundaries is mandatory** (the source purges on the two-opening label lookahead).
- **Timestamp / timezone**: `not stated in source` — the paper never prints a timezone, session calendar or clock convention (`data gap`).
- **Data vendor / licence**: `not stated in source` — no vendor, no dataset name, no access path (`data gap`), and no code or data release, so the empirical pipeline **cannot be re-run from the source alone**.
- **Missing data**: zero denominators give missing values (Table 10 note); coverage gates drop factors below 0.20. Imputation is not specified → `underspecified`.

## Execution assumptions

**Cost determination from a Methods-level read** of Appendix C.1, Appendix C.2 (the sentence "Reported returns are gross of trading costs"), Appendix B.1, Appendix C.3, Section 3 and the full set of Tables 1–26, plus a word scan of the pinned HTML for `fee, commission, spread, slippage, impact, participation, ADV, capacity, borrow, financing, leverage, margin, latency, fill, turnover`:

- The **only** explicit cost statement in the paper is that reported returns are **gross of trading costs**. There is **no cost model, no turnover number, no capacity estimate, no fill model and no net-of-cost result anywhere in the pinned text**.
- Therefore `fees`, `spread`, `slippage`, `impact`, `participation`, `ADV`, `capacity`, `borrow`, `financing`, `leverage`, `margin`, `latency`, `fill / partial-fill / failure handling`, and `turnover` are all **`data gap`, never zero**, and there is no net-of-cost series to quote.
- Two look-alikes that are **not** trading costs and must not be read as such: `log_turnover` is a logged *traded-amount* feature and Table 11 explicitly states "Traded amount is monetary value; it is not the share-turnover rate"; Table 6's `$7.28 / $5.57 / $2.19 / $0.00` are **LLM API inference charges** for one 20-round CSI300 research run (plus 1.436 H200 GPU-hours for the local deployment), not brokerage, spread or market impact.
- `Signal-to-order timing`, `order type`, `fill model`, `latency`, `position limits` and `failure handling` are **`underspecified`**: the source gives a causal boundary (features after close, label from next open to the following open) but never states how orders are placed, at what price, or what happens on a non-fill.
- **Gross-versus-net status is stated** (gross); every other execution field is a gap.

## Evidence

### Source-reported

All figures below are read from the pinned v1 HTML and are **gross of trading costs**, on the outer period **January–August 2026**, long-only equally weighted top-20% excess over the stated benchmark. They have **not** been independently reproduced.

**Table 1 — CSI300 (IC, ICIR, RIC, RICIR | ARR %, IR, MDD %, CR):**

| Method | IC | ICIR | RIC | RICIR | ARR | IR | MDD | CR |
|---|---|---|---|---|---|---|---|---|
| Ridge | 0.0166 | 0.0865 | 0.0210 | 0.1184 | 14.44 | 0.889 | 13.49 | 1.071 |
| MLP | 0.0287 | 0.1320 | 0.0377 | 0.1905 | 27.34 | 1.604 | 13.34 | 2.050 |
| LightGBM | 0.0348 | 0.2043 | 0.0335 | 0.2243 | 24.15 | 1.846 | 6.99 | 3.456 |
| GRU | 0.0303 | 0.1165 | 0.0170 | 0.0720 | 18.46 | 1.024 | 13.81 | 1.316 |
| LSTM | 0.0348 | 0.1460 | 0.0277 | 0.1192 | 24.83 | 1.280 | 16.50 | 1.505 |
| ALSTM | 0.0181 | 0.0964 | 0.0296 | 0.1539 | 25.23 | 1.540 | 8.93 | 2.826 |
| TCN | 0.0131 | 0.0664 | 0.0212 | 0.1229 | 16.70 | 1.140 | 9.32 | 1.793 |
| Transformer | 0.0134 | 0.0607 | 0.0353 | 0.1492 | 7.45 | 0.439 | 13.78 | 0.500 |
| PatchTST | 0.0145 | 0.0600 | −0.0068 | −0.0259 | −3.59 | −0.274 | 21.19 | −0.310 |
| iTransformer | 0.0212 | 0.1473 | 0.0171 | 0.1284 | 15.61 | 0.857 | 6.76 | 1.471 |
| MASTER | 0.0318 | 0.1516 | 0.0325 | 0.1974 | 27.02 | 1.858 | 10.63 | 2.265 |
| StockMixer | −0.0069 | −0.0320 | 0.0236 | 0.1019 | −4.75 | −0.240 | 22.72 | −0.226 |
| RD-Agent(Q) | 0.0244 | 0.1299 | 0.0223 | 0.1342 | 17.57 | 1.355 | 10.03 | 1.751 |
| AlphaAgent | 0.0337 | 0.2075 | 0.0384 | 0.2587 | 33.62 | 2.856 | 6.05 | 5.554 |
| QuantaAlpha | 0.0340 | 0.1804 | 0.0403 | 0.2449 | 43.19 | 2.980 | 6.51 | 6.634 |
| AlphaSchema | 0.0338 | 0.1965 | 0.0367 | 0.2156 | 32.90 | 2.272 | 7.61 | 4.324 |
| **AlphaDiverse** | **0.0378** | **0.2128** | **0.0407** | **0.2790** | **42.10** | **3.210** | **5.51** | **7.641** |

Source's own reading (Section 3.1): AlphaDiverse "leads all four predictive metrics … also achieves the highest IR (3.210) and CR (7.641), the lowest MDD (5.51%), and the **second-highest ARR (42.10%)**".

**Tables 16–18 — the other three universes (AlphaDiverse rows):**

| Universe | IC | ICIR | RIC | RICIR | ARR | IR | MDD | CR |
|---|---|---|---|---|---|---|---|---|
| CSI500 (Table 16) | 0.0308 | 0.2130 | 0.0295 | 0.2296 | 16.19 | 1.245 | 7.30 | 2.216 |
| CSI1000 (Table 17) | 0.0256 | 0.1827 | 0.0364 | 0.2530 | 16.45 | 1.171 | 7.97 | 2.063 |
| A-share (Table 18) | 0.0357 | 0.3280 | 0.0392 | 0.2866 | 19.04 | 2.029 | 4.77 | 3.990 |

Agentic comparators' ARR on the same tables: CSI500 — RD-Agent(Q) 2.50, AlphaAgent 1.53, QuantaAlpha 14.88, AlphaSchema 6.07; the source's own D.1 summary reads: "AlphaDiverse achieves the highest IC, ICIR, RICIR, and IR and the lowest MDD in all three additional markets. **The strongest ARR on CSI500 and CSI1000 and the strongest RIC on CSI500 and A-share are obtained by other methods.**"

**Table 2 — research diversity (mechanisms M / useful mechanisms U / signal clusters C), CSI300 then CSI500:** AlphaDiverse `34/23/129` and `36/25/128`; AlphaDiverse (GPT-5.5) `24/11/108` and `24/11/125`; AlphaDiverse (SFT-only) `27/4/85` and `23/6/83`; Single Synthesis `19/8/122` and `20/10/99`; AlphaSchema `18/2/96` and `19/7/96`; QuantaAlpha `11/3/58` and `22/4/64`; AlphaAgent `5/5/16` and `5/1/34`; RD-Agent(Q) `18/3/67` and `25/14/121`.

**Table 3 — module ablations (GPT-5.5), RIC / ARR % / M / U / pair-corr:** w/o complementarity `0.0352 / 37.73 / 10 / 7 / 0.455`; w/o retrieval `0.0373 / 28.39 / 25 / 9 / 0.371`; w/o memory `0.0383 / 32.26 / 21 / 11 / 0.473`; Single Synthesis `0.0316 / 23.83 / 19 / 8`; full AlphaDiverse (GPT-5.5) `0.0398 / 35.97 / 24 / 11 / 0.322`.

**Table 4 — post-training ablations, RIC / ARR % / M / U / pair-corr:** w/o training `0.0291 / 22.49 / 33 / 11 / 0.413`; w/ SFT `0.0389 / 24.77 / 27 / 4 / 0.511`; Planner only `0.0397 / 32.57 / 30 / 13 / 0.423`; Realizer only `0.0400 / 35.17 / 30 / 15 / 0.394`; w/o diversity reward `0.0403 / 37.77 / 29 / 18 / 0.365`; full AlphaDiverse `0.0407 / 42.10 / 34 / 23 / 0.316`.

**Table 5 — SFT-data ablations, RIC / ARR % / M / U / pair-corr:** w/ improvement only `0.0371 / 22.38 / 21 / 1 / 0.616`; w/o balancing `0.0383 / 23.95 / 25 / 3 / 0.546`; w/o paired supervision `0.0365 / 21.51 / 19 / 1 / 0.651`; full data SFT `0.0389 / 24.77 / 27 / 4 / 0.511`.

**Table 6 — deployment cost of one 20-round CSI300 research run:** GPT-5.5 `$7.28`, Grok-4.6 `$5.57`, GLM-5.3 `$2.19`, AlphaDiverse (local) `$0.00` + `1.436` H200 GPU-hours. **These are LLM inference costs, not trading costs.**

**Training corpus (Table 12):** Planner `589` examples / `9,863,796` input tokens / `341,416` supervised tokens; Realizer `1,006` examples / `2,654,667` input / `402,463` supervised. **Optimisation (Appendix B.2):** 96 task states visited twice = 192 state visits, arranged into 48 updates × 4 states; only the two LoRA adapters receive gradients; reward calibration uses the 75th percentile of historical candidate score gains and the 95th percentile of Gaussian noise-portfolio gains and must be positive or training does not start.

### Independently reproduced

not independently reproduced

We verified only the artefact and the reading: pinned HTML and PDF hashes recorded above, 33-page count and author metadata from `pdfinfo`, DOI 302-resolution, `v2` 404, and every quoted number located in a named table of the pinned v1. No factor was re-implemented, no model was retrained, no portfolio was re-run, and the source ships no code or data.

### Negative evidence

1. **No cost model at all.** Returns are explicitly gross; fees, spread, slippage, impact, participation, ADV, capacity, borrow, financing, leverage, margin, latency, fill, failure handling and turnover are `data gap`, never zero — so no break-even cost, no net Sharpe and no capacity claim can be formed from the source.
2. **The signal itself is unpublished.** The retained factor list per market is never printed, so the headline ARR cannot be attributed to any specific trading rule; only the 21 base factors and the feature/operator sets are documented.
3. **One run per method–market.** Appendix C.3: "we report one complete mining run per agentic method–market configuration, it is the common protocol of agentic alpha factor mining methods because of the high API/GPU cost." No dispersion, no confidence interval, no significance test appears anywhere, while neural baselines are explicitly "metric-wise medians across three seeds" — an asymmetric replication standard inside one table.
4. **AlphaDiverse does not win ARR on CSI300**: 42.10 versus QuantaAlpha 43.19 (source calls it second-highest).
5. **The source's own D.1 sentence** concedes the strongest ARR on CSI500 and CSI1000 and the strongest RIC on CSI500 and A-share go to other methods.
6. **The diversity term barely moves returns.** Table 4: w/o diversity reward already gives RIC 0.0403 and ARR 37.77 against the full model's 0.0407 / 42.10; the paper's claimed gain is coverage (U 18 → 23), not performance.
7. **The complementarity module is not monotone in returns**: Table 3, w/o complementarity yields a *higher* ARR (37.73) than the full GPT-5.5 variant (35.97), which the source itself points out.
8. **Unmatched information sets**: ML/DL baselines receive only the 21 base factors while agentic methods use all available features (Appendix C.3 vs Section 3) — the Table 1 ML/DL and agentic columns are not an apples-to-apples comparison and no matched-feature agentic run is printed.
9. **Teacher-model confound**: training traces come from GPT-5.5, Grok-4.6 and GLM-5.3 API runs; the claim that the distilled local policies generalise beyond those teacher distributions is tested only on 20 shared states (10 familiar, 10 held-out) in Figure 4, with no financial metrics attached to that test.
10. **Outer window is one 8-month Chinese-equity sample** (Jan–Aug 2026), long-only, with no regime split, no subperiod stability table and no second confirmation window; the anti-test-tuning design reduces leakage but does not create independent replications.
11. **No statistical inference or multiplicity control** across 8 metrics × 4 markets × ~16 methods plus 3 ablation families (Tables 3, 4, 5, 22, 23, 24) and 2 diversity budgets.
12. **Benchmarks differ across tables** (index returns for index universes, equal-weight eligible A-shares for the A-share universe), so ARR across Tables 1, 16, 17 and 18 are not mutually comparable.
13. **No code, no data, no data-availability statement** (`not stated in source`) → nothing is independently reproducible from the publication.
14. **Source-internal cross-reference errors**: §3.3 cites "Table 4" for the module ablations (captioned Table 3) and "Table 6" for the SFT-data ablations (captioned Table 5).
15. **Tradeability is only partly handled**: opening-price-limit rejections and <60-day listings remove some untradeable observations, but there is no fill model, no limit-up participation rule and no treatment of suspended names inside the held book.
16. **Budget matching is shallow**: all agentic methods get 160 candidate slots, but slots are not equal in compute or in the number of underlying model calls per method (RD-Agent(Q) and AlphaAgent get 20 batches of eight; QuantaAlpha six original + six mutated + eight crossover tasks; AlphaSchema five batches of 16 plans × 2 realisations).
17. **Source's own Limitations (Section 5)**: the fixed mechanism catalogue and operator library bound what agents can express; joint training evaluates sampled plans on a finite bank of inner states, "which only approximates their delayed contribution during a long research loop."
18. **Status**: preprint "under review", no venue, no peer review, no independent replication, and evidence that rests on a single proprietary Chinese-equity dataset with no vendor disclosed.

## Falsification plan

Every threshold below is `research-defined` (Scout-chosen), and every operational rule not printed by the source is `research-proposed`. Data for all tests: Chinese A-share daily + minute bars with point-in-time index membership, inner period May 2022–December 2025, outer period extended beyond January–August 2026. Action on failure: record the hypothesis as disproved for this deployment and drop the candidate — no retuning of thresholds after seeing results.

- **F1 — frozen forward replication.** Re-run the full pipeline with a *later* frozen window (≥ 6 months ending after 2026-08) and ≥ 3 independent mining runs per market. **Pass** only if median-across-runs ARR excess over the benchmark is > 0 with a moving-block-bootstrap 95% CI excluding zero, in at least 3 of the 4 universes. **Fail** otherwise.
- **F2 — cost ladder (decisive for tradability).** Net the same book at 0/1/5/10/20/30 bp per side plus an explicit A-share commission-and-stamp-duty schedule. **Fail** if net IR < 0.50 at 10 bp one-way, or if a realistic A-share round trip erases > 50% of the gross ARR.
- **F3 — turnover and capacity audit.** Measure daily top-quintile membership churn and volume participation. **Fail** if one-way daily turnover exceeds 40%, or if holding 10% of 20-day ADV for the top quintile cannot be funded within a stated capital base; the source prints neither, so this test produces the number the source lacks.
- **F4 — decisive mining-layer ablation.** Train LightGBM on **only the 21 base factors** under identical splits and budget. **Pass** only if AlphaDiverse beats that control by ≥ 0.005 IC *and* ≥ 5 percentage points ARR on the same outer window in ≥ 3 of 4 universes. **Fail** if the mined factors add nothing beyond the printed baseline.
- **F5 — diversity → performance mechanism.** Across the four markets × the published variants (untrained, SFT-only, w/o diversity reward, w/o complementarity, full), correlate useful-mechanism count `U` with out-of-sample ARR. **Pass** only if Spearman ρ ≥ 0.60 with a positive sign in ≥ 3 of 4 markets. **Fail** if diversity and performance are unrelated — that would reduce the paper to "post-training helps", not "diversity helps".
- **F6 — leakage audit.** Rebuild eligibility point-in-time and re-verify the two-opening label purge at every split boundary. **Fail** on any instance of membership, ST, suspension or price-limit information dated after the signal.
- **F7 — permutation null.** Circularly shift each date's predicted score cross-section by random offsets (1000 draws). **Pass** only if the observed IC exceeds the 95th percentile of the null in ≥ 3 of 4 universes.
- **F8 — multiplicity.** Apply Benjamini–Hochberg across the 4 markets × 8 metrics family. **Fail** if no AlphaDiverse comparison survives `q < 0.10`.
- **F9 — competing-explanation horse race.** Re-run QuantaAlpha, AlphaSchema, AlphaAgent and plain LightGBM under one matched feature set, ≥ 3 runs each. **Fail** if AlphaDiverse is not top-2 on *net* IR in ≥ 3 of 4 universes.
- **F10 — portfolio-definition robustness.** Recompute as value-weighted top quintile, top decile, and long-short top-minus-bottom. **Fail** if the long-short spread has Newey-West `t < 1.96` or if the result exists only in the equal-weighted long-only construction.
- **F11 — regime / subperiod stability.** Split the extended outer window into ≥ 3 contiguous subperiods. **Fail** if ≥ 2 of 3 are non-positive in any two universes.
- **F12 — reproducibility gate.** If no code and no data become public within 12 months of 2026-09-24, mark the result permanently `unverifiable` and drop it from consideration regardless of printed numbers; if they do become public, a third party must reproduce Table 1 IC/ARR within ±20%.
- **F13 (crypto portability, only if adapted)** — port the *pipeline* (feature set + mined-factor block + LightGBM + top-quintile book) to a BTC/ETH top-N daily universe with a 10 bp one-way cost ladder; **fail** unless Newey-West `t ≥ 1.96` and positive net IR survive 10 bp.

## Crypto portability

**`unproven`.**

The source contains **zero crypto evidence**: no crypto universe, no perpetual or futures contract, no funding, no mark/index price, no 24/7 session, no venue fragmentation, no borrow or short-side analysis (the construction is long-only). Its entire data dependency — point-in-time CSI membership, ST flags, opening-price-limit filters, Shanghai/Shenzhen minute bars, index benchmarks — has **no crypto counterpart**, and its cost section is empty, so none of the crypto-specific frictions (funding rate, mark-price liquidation, 24/7 candle boundaries and timestamp alignment, listing/delisting churn, cross-venue liquidity fragmentation, custody/withdrawal risk) are addressed anywhere in the paper.

What *could* port is only the research method (diversity-regularised post-training of research agents plus an inner/outer split), which would be a `research-proposed` adaptation and not crypto empirical evidence. A genuine portability claim requires F13 to pass. Crypto portability is not authorisation to trade.

## Limitations

- **`data gap`**: every trading-cost field (fees, spread, slippage, impact, participation, capacity, borrow, financing, leverage, margin, latency, fill, failure handling, turnover); data vendor; timezone/session convention; AI-use disclosure; code and data availability.
- **`underspecified`**: rebalance cadence (daily formation is implied, never stated), order type, execution price, position limits, cash and suspension handling inside the held book, per-author affiliation mapping and corresponding-author identity, and the entire entry/exit/sizing layer.
- **`not stated in source`**: the retained factor list per market — without it the printed strategy is a *description of a research process*, not a reproducible trading rule.
- **`not independently reproduced`**: every number in this record; we read and hashed the pinned source but re-ran nothing, and the source provides no code or data to re-run.
- **`unproven`**: crypto portability; out-of-sample stability beyond a single 8-month Chinese-equity window; any net-of-cost profitability; any capacity claim; generalisation of distilled policies beyond their teacher API distributions.
- **Design limitations**: single run per agentic method–market, unmatched feature sets between ML/DL and agentic columns, benchmark inconsistency across tables, no inference or multiplicity control, two source-internal table cross-reference errors, preprint status ("Preprint under review") with no venue and no peer review.
- **Scope**: this is a record of *research material*. Presence in this repository does not imply the strategy works, was validated, or may be traded.

## Implementation status

`implementation_status: not-implemented`. No implementation exists in our research stack: no factor was re-implemented, no LightGBM model was trained, no portfolio was constructed, and no backtest, Paper, Testnet or Live run has occurred. The source itself ships no code and no data. Nothing here implies Qlib full-backtest validation or any downstream approval.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record did **not** pass Research Intake Review, did **not** enter Hermes Wiki Brain as an adopted record, did **not** enter the production candidate pool, did **not** complete Qlib validation, and did **not** become a frozen survivor or leaderboard entry. It is not evidence of profitability, not validated alpha, and not approval to implement, paper-trade, testnet-trade or trade.

## Related Wiki records

Mechanism-adjacent pages returned and verified by Wiki Brain `kb_search` for this run (`LLM agentic alpha factor mining Chinese A-share cross-sectional factor discovery`, 4 hits; a second query on post-training / GRPO / inner-outer evaluation returned 0 hits):

- [[quant/alphaschema-trading-semantic-plan-space-surrogate-guided-factor-mining-2026-09-05]]
- [[quant/alphalogics-market-logic-multi-agent-factor-generation-2026-09-05]]
- [[quant/alphag-opd-reliability-gated-sibling-counterfactuals-symbolic-alpha-2026-09-05]]
- [[quant/alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05]]

No other Wiki Brain pages were verified for this record; no page is linked beyond the four returned by search.

## Sources

1. Wang, Q., Wei, Z., Wei, Z., & Shen, W. (2026). *AlphaDiverse: Post-Training Local Quantitative Research Agents for Diverse Exploration in Alpha Factor Mining*. arXiv:2609.29014v1 [cs.AI], submitted 24 September 2026. https://arxiv.org/abs/2609.29014 — DOI https://doi.org/10.48550/arXiv.2609.29014 (DataCite, 302 → abs, checked 2026-09-26). Comments: "33 pages, 7 figures, 26 Tables. Preprint under review". Licence: arXiv perpetual non-exclusive distribution licence.
2. Pinned full text (HTML): https://arxiv.org/html/2609.29014v1 — 721,691 bytes, SHA-256 `62f9874d1ff300f2a131d84206a2eed8b5f0456e927aec4b25c6fdf786750eb1`, downloaded and read 2026-09-26.
3. Pinned full text (PDF): https://arxiv.org/pdf/2609.29014v1 — 866,237 bytes, SHA-256 `ce17a92282f8825e019fa0328201ee0707807c957efa652194d45fda37d4ffb0`, 33 pages, downloaded 2026-09-26.

All quantitative claims above are labelled source-reported and trace to Table 1, Tables 2–6, Tables 16–19, Table 8, Table 9, Table 10, Table 11, Table 12, Sections 1, 3, 3.1–3.3, 5, and Appendices B.1, B.2, C.1, C.2, C.3, D.1–D.7 of source 1 as rendered in sources 2 and 3. All are gross of trading costs and none has been independently reproduced.
