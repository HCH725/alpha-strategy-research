---
schema: strategy-research-record-v1
title: "FinRankGRPO: news-driven listwise LLM ranking of 15 ETFs mapped into entropy-pooling long-only weekly rotation (5 bps per turnover, mean of 5 trials) - arXiv 2609.24175, out-of-sample 2020-2025"
created: 2026-09-28
updated: 2026-09-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - etf
  - cross-sectional
  - large-language-models
  - news-signal
  - portfolio-optimization
  - transaction-costs
status: research-only
confidence: medium
source_as_of: 2026-09-21
sources:
  - https://arxiv.org/abs/2609.24175
  - https://arxiv.org/html/2609.24175v1
  - https://arxiv.org/pdf/2609.24175v1
  - https://doi.org/10.48550/arXiv.2609.24175
  - https://anonymous.4open.science/r/FinRankGRPO-7107/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Translation claim: Section 4.4 states 'These results confirm that improved ranking accuracy directly translates into superior portfolio returns' while the source's own input ablation (Section 5.4, Figure 5) shows Spearman falling 0.023 -> 0.012 while Sharpe rises 0.636 -> 0.677 when the trading-date input is removed, and Spearman falling only to 0.010 while Sharpe collapses to 0.045 when news is removed - ranking accuracy and portfolio return move in opposite directions in the same paper - unreconciled."
  - "Sample unit: Section 4.1 states 'For each weekly sample, we retain the response with the highest Spearman correlation against the ground truth return ranking' while Appendix B repeats the sentence with 'For each day, we retain the response with the highest Spearman correlation against the ground-truth return ranking' before giving the SFT/FinRankGRPO partition rule - weekly versus daily selection unit - unreconciled."
  - "Training-sample count: Section 4.1 calls the 2010-2019 training set '2,516 weekly samples' although that span contains about 522 calendar weeks; Appendix B states training samples use a rolling weekly window while only test samples are non-overlapping calendar weeks, which implies roughly daily-stepped overlapping windows - the frequency label is inconsistent with the count - unreconciled."
  - "Decimal inconsistency: Section 5.3 reports 'Spearman are 0.21 and 0.23 for Base and Instruct' while Table 1 and Figure 3 report 0.021 and 0.023 for the same two rows - unreconciled."
  - "Model inventory: Section 4.2 lists 'the Qwen2.5 model, covering three parameter scales, 0.5B, 1.5B, and 3B, including both the Base and Instruct variants' while Appendix C lists 'Qwen0.5-3B, Qwen0.5-3B-Instruct, Qwen0.5-3B, Qwen1.5-3B-Instruct, Qwen2.5-3B, Qwen2.5-3B-Instruct' - repeated and malformed model names - unreconciled."
  - "Scaling claim: Section 5.1 states larger models 'generally produce better financial rankings and stronger portfolio performance, consistent with scaling law findings' while Figure 3 prints Sharpe 0.521 (0.5B Base) falling to 0.453 (1.5B Base) and 0.505 (0.5B Instruct) falling to 0.500 (1.5B Instruct) - non-monotone in the middle size - unreconciled."
  - "Recession win claim: Section 5.6 states FinRankGRPO 'achieves the highest Spearman correlation and Sharpe ratio (0.4863)' for the 2020 recession while Table 4 prints Claude at the same Sharpe 0.486 - a tie reported as a sole win - unreconciled."
  - "Cost disclosure location: Section 4.3 Evaluation defines the reported metrics and mentions no cost, while the only cost statement in the paper (5 bps per turnover, weekly-close execution, zero slippage, management fees excluded) sits in Appendix F; turnover itself is never reported (the word 'turnover' occurs exactly once in the pinned PDF, inside that cost sentence) - unreconciled."
  - "Undescribed oracle row: Table 1 prints a 'Ground Truth' row with Ann. Ret. 1.049, Sharpe 7.655 and Max DD 0.138 alongside the tradable rows, yet the construction of that row is never described in the text and the words 'oracle' and 'upper bound' occur zero times in the pinned PDF - unreconciled."
  - "Look-ahead framing: Section 4.1 says 'To avoid lookahead bias, we use a chronological split, 2010-2019 for training and 2020-2025 for out-of-sample testing' while the Limitations section states the same 2020-2025 window 'may introduce potential lookahead bias due to the pretraining data of modern LLMs' and no time-controlled checkpoint was used - unreconciled."
---

# FinRankGRPO: news-driven listwise LLM ranking of 15 ETFs mapped into entropy-pooling long-only weekly rotation (5 bps per turnover, mean of 5 trials)

## Provenance

Primary source (identity of every claim in this record):

- arXiv landing: `https://arxiv.org/abs/2609.24175`; version `https://arxiv.org/abs/2609.24175v1`; full text `https://arxiv.org/html/2609.24175v1`; PDF `https://arxiv.org/pdf/2609.24175v1`.
- Title exactly as printed on the landing page, the PDF first page and the HTML header: **"FinRankGRPO: Optimizing LLMs for Listwise Financial Asset Ranking via Group Relative Policy Optimization"** (no title variant).
- Authors exactly as printed on the HTML title block (five authors, with affiliation and e-mail lines): **Ningyuan Deng** (Affiliation: The Hong Kong University of Science and Technology; `ndengad@connect.ust.hk`), **Jinyuan Wang** (The Hong Kong University of Science and Technology; `jwangiy@connect.ust.hk`), **Qi Li** (Ping An Property & Casualty lnsurance Company of China, Ltd, printed with the typo `lnsurance`; `li.qi@graduate.utm.my`), **Jia Zhang** (Ping An Property & Casualty lnsurance Company of China, Ltd; `zhangjia348@pingan.com.cn`), **Yi Yang** (The Hong Kong University of Science and Technology; `imyiyang@ust.hk`). No ORCID is printed - `data gap`.
- Version / date: submission history on the landing page reads **`[v1] Mon, 21 Sep 2026 06:45:38 UTC (743 KB)`**, only one version (`arxiv.org/abs/2609.24175v2` not offered by the submission history). PDF footer stamp `arXiv:2609.24175v1 [cs.CE] 21 Sep 2026`.
- Publication status: **preprint only, not peer reviewed.** The landing page has **no `Comments:` field, no `Journal reference:` field and no publisher `DOI:` field**; the only DOI is the arXiv-issued DataCite identifier `https://doi.org/10.48550/arXiv.2609.24175`, which the landing page annotates `arXiv-issued DOI via DataCite (pending registration)`. Subject class is **`Computational Engineering, Finance, and Science (cs.CE)` only - there is no q-fin cross-list**. License: the landing page license icon resolves to `creativecommons.org/licenses/by/4.0/` and the HTML full text prints `License: CC BY 4.0`.
- Pinned primary HTML: `https://arxiv.org/html/2609.24175v1`, downloaded **2026-09-28**, **276,095 bytes**, **SHA-256 `b094bc1175b62a5e9ad1243267e3506158de3005252ffaead6031bf75030ca2e`**, converted to **64,411 characters / 1,745 lines** and read end to end: Abstract, Sections 1-6, Limitations, Ethical Considerations, References, Appendix A-I, Tables 1-7, Figure 1-9 captions.
- Pinned primary PDF: `https://arxiv.org/pdf/2609.24175v1`, downloaded **2026-09-28**, **932,549 bytes**, **16 pages**, **SHA-256 `f592c2418b9d52d22110ae6f53e191357ae0f960301c011b14a01aa76cff3458`**, text-extracted page by page with `pypdf` to **54,598 characters** and all 16 pages read. Table 1 was re-extracted directly from PDF page 6 and matches the HTML cell for cell; the cost paragraph was located on PDF pages 13-14 (Appendix F).
- Code/data availability statement printed in the abstract: `https://anonymous.4open.science/r/FinRankGRPO-7107/`. Checked **2026-09-28**: the URL returns **HTTP 302** to `https://anonymous.4open.science/api/repo/FinRankGRPO-7107/file/`, which returns **HTTP 401**, i.e. the replication package is **not publicly retrievable** at read time - `data gap`.
- Data named by the source: ETF market prices from **Bloomberg** "under our institution's academic license" (Section 4.1); news headlines from **FNSPID** (Dong et al., 2024, stated `CC BY 4.0`) for 2010-2023 and **The Wall Street Street Journal archive** (`https://www.wsj.com/news/archive/years`) for 2024-2025; weekly news digests produced by **DeepSeek-Chat**; Chain-of-Thought ranking supervision distilled from **GPT-4o-mini, Claude-3.5-Sonnet and DeepSeek-Chat**.
- Sample periods: dataset built for **2010-2025**, chronological split **2010-2019 training (2,516 "weekly samples")** and **2020-2025 out-of-sample testing (314 weekly samples, non-overlapping calendar weeks)** (Section 4.1 and Appendix B); stress window **February-April 2020 (NBER recession)** (Section 5.6).
- Universe: **15 liquid ETFs** (Appendix B, Table 5): size indices `IVV`, `IJH`, `IJR`; sectors `XLB`, `XLE`, `XLF`, `XLI`, `XLK`, `XLP`, `XLU`, `XLV`, `XLY`; alternatives `GLD`, `GSG`, `IYR`.
- Transaction-cost treatment (read at Methods level: Section 4.1 Datasets, Section 4.3 Evaluation, Section 3.3.3 Portfolio Optimization, Section 6 and Limitations, plus Appendix B, Appendix C and Appendix F of the pinned PDF, and a full-text word scan of all 54,598 extracted characters): the paper imposes **"a transaction fee of 5 basis points (0.05%) per turnover to account for commissions and bid-ask spreads"**, assumes **"trades are executed at the weekly closing price"**, assumes **"zero slippage for the execution"** on the grounds that the ETFs are top-tier liquid, and **excludes management fees** "to strictly isolate the alpha generation capability" (Appendix F, PDF pages 13-14). This cost paragraph appears **only** in Appendix F; Section 4.3 defines the evaluation metrics without mentioning any cost. Word scan of the pinned PDF: `turnover` **1** occurrence (the cost sentence itself), `slippage` **1**, `management fees` **1**, `5 basis points` **1**, `buy and hold` **0**, `standard deviation` **0**, `confidence interval` **0**, `significance` **0**, `p-value` **0**, `t-test` **0**, `seed` **0**, `capacity` occurrences are all about neural-network model capacity. Conclusion: results are **net of a single flat 5 bps-per-turnover fee and gross of everything else**; turnover, spread in practice, impact, latency, participation, borrow, margin, taxes and capacity are `data gap`, never zero.

Repository-wide source-identity dedup before writing (hidden-inclusive, `rg -uuu` across the whole checkout including `.mimo-worktrees/`, `.agents/`, `.hermes/`, `.git/` and `coverage_manifest.csv`): `2609.24175`, `10.48550/arXiv.2609.24175`, `FinRankGRPO`, `Ningyuan Deng`, `Jinyuan Wang`, `listwise financial asset ranking`, `Financial Asset Ranking via Group`, `anonymous.4open.science/r/FinRankGRPO` all returned **zero matches** (exit 1); a positive-control search for `novy-marx` in the same session returned matches (exit 0), so the search was live. A second pattern set (`Entropy Pooling`, `entropy pooling`) also returned **zero** existing records, so no entropy-pooling record exists in this repository. `git log --oneline -20` was consulted only as a convenience glance and does not by itself satisfy dedup. Wiki Brain `kb_search` (read-only) returned **0 pages** for `LLM listwise asset ranking portfolio entropy pooling GRPO ETF news` and **0 pages** for `LLM news sentiment ETF rotation long-only weekly portfolio`; a broader `large language model trading signal portfolio` search returned ten real adjacent pages, two of which are linked below.

## Economic mechanism

### Source-reported

The authors' stated rationale (Abstract, Sections 1, 2, 3 and 6):

- Claimed problem 1: standard LLM training objectives are mismatched to portfolio construction, which needs **listwise ordinal structure** rather than next-token prediction; the paper cites evidence that direct numerical forecasting by LLMs suffers "arithmetic hallucination" and that even strong research models reach only "approximately 40% accuracy" on financial numeracy forecasting (cited by the source to Li et al., 2026 - **not read for this record**, `data gap`).
- Claimed problem 2: Black-Litterman / Entropy Pooling frameworks accept structured numerical views but give "limited guidance on deriving such views, or relative asset rankings, from unstructured text such as market news".
- Proposed mechanism: convert a week of aggregated financial news headlines into a **complete ranking of the 15 ETFs**, encode the ranking as **ordinal mean-view constraints** (`P E_q[R] >= 0` for consecutive pairs), update the empirical prior to a posterior by minimizing relative entropy, then solve a **long-only maximum-Sharpe problem** so that capital concentrates on assets the model predicts will relatively outperform.
- Training rationale: Stage 1 supervised fine-tuning on distilled CoT data teaches structured ranking output; Stage 2 (FinRankGRPO) replaces GRPO's exact-match reward, which the source reports gives "zero reward" to all sampled actions and **35.14% zero-loss training steps**, with a **dense Spearman-correlation reward** that yields non-zero loss in **99.68% of steps**.
- Interpretation claim in Section 4.4: "improved ranking accuracy directly translates into superior portfolio returns" and "the model's outputs are ... economically meaningful in real world trading scenarios". The source does **not** claim a causal economic mechanism for why weekly news implies ETF-relative returns; no friction, behavioral or risk-premium channel is named - `underspecified`.
- Stated limitations by the source: English-only news; and the 2020-2025 evaluation window "may introduce potential lookahead bias due to the pretraining data of modern LLMs", with strictly time-controlled checkpoints and earlier out-of-sample periods deferred to future work.

### Research interpretation

- Hypothesized mechanism in falsifiable form: **weekly firm/macro news contains incremental ordinal information about the relative one-week performance of 15 liquid ETFs that a rank-tuned 3B LLM can extract, and mapping that ordering through entropy-pooling mean views into a long-only maximum-Sharpe book converts it into net-of-5-bps risk-adjusted excess return over equal weight.**
- Component roles, normalized:
  - Regime/context input: trading date string plus a DeepSeek-Chat digested weekly headline summary (Section 5.4 shows the date input is *not* needed for returns).
  - Primary signal: complete listwise ranking of the 15 ETFs emitted as JSON by the fine-tuned Qwen2.5-3B-Instruct model.
  - Portfolio layer: entropy pooling with zero-magnitude ordinal views, then long-only max Sharpe with `r = 2.5%`, `1'w = 1`, `w >= 0` (Equation 9).
  - Risk / exit: **none stated** - there is no stop, no volatility target, no drawdown control and no position limit beyond the simplex and long-only constraints; exit is implicit in the weekly re-ranking.
  - Friction layer: one flat 5 bps per turnover fee, weekly-close fills, zero slippage, no management fee.
- Live competing explanations this record does not dismiss: **passive sector/size tilt timing** (the book is long-only over US sector and size ETFs, so returns can be beta/style timing rather than news alpha), **the 2020-2025 single-regime window** (COVID crash, 2022 bear and 2023-2025 bull), **pretraining exposure to the test period** (the source's own admitted risk), **label selection on the realized target during training** (the CoT response retained per sample is the one with the highest Spearman against realized returns), and **the DeepSeek-Chat summarization pipeline being shared with one of the evaluated baselines**.
- Research interpretation of the source's own diagnostics: the decisive pattern is the **decoupling** between ranking quality and portfolio quality - test Spearman never exceeds 0.023 anywhere in Table 1, while removing the news input destroys the Sharpe (0.636 -> 0.045) and removing the date input *improves* it (0.636 -> 0.677). That pattern is more consistent with **news-conditioned defensive/tilt timing inside a long-only book** than with accurate asset ranking, and the source's "ranking accuracy translates into returns" sentence is contradicted by its own Figure 5.

## Signal

Everything in this section is source-reported unless explicitly marked `research-proposed` or `data gap`.

- **Formation timestamp:** for each test week the model receives the trading date and the aggregated news digest of the preceding week and emits a ranking intended for the following week (Equation 1: `y_(t+1) = LLM_theta(T(X_date(t), X_news(t), A))`). The digest aggregates "headlines from the preceding week", de-duplicated with **SimHash at a Hamming distance threshold of 25** and summarized by **DeepSeek-Chat** (Appendix B). Timezone, publication timestamp, news-availability lag and the exact weekly cut are **not stated in source** - `data gap`.
- **Lookback:** news aggregation window = preceding week; no price lookback is used by the model itself (the model sees the date and the news digest, not price series; the source's CoT prompts reason over "historical price trends and recent news headlines" per Section 4.1, so a price-history view inside the prompt is asserted but not specified - `underspecified`).
- **Ranking output:** a complete permutation of the 15 tickers in JSON; structural errors (missing or hallucinated assets) are scored `-1` by the training reward. Tie handling is not addressed because the output is a strict ordering; how duplicate or invalid JSON is handled at inference is `data gap`.
- **View constraints (Section 3.3.1, Equation 7):** every consecutive pair in the ranking gives `E_q[R_i] >= E_q[R_j]` with right-hand side `v = 0` ("qualitative rankings"); the pick matrix `P` therefore has `N-1 = 14` rows for `N = 15` assets (Appendix D prints the 3-asset example).
- **Posterior (Section 3.3.2, Equation 8):** `q* = arg min sum_k q_k ln(q_k / p_k)` subject to the view constraints, `sum q = 1`, `q >= 0`, with `p` the empirical prior over training-history scenarios; scenario count `K`, the prior construction window and the sampling scheme are **not stated in source** - `data gap`.
- **Portfolio rule (Section 3.3.3, Equation 9):** `w* = arg max (w' mu_EP - r) / sqrt(w' Sigma_EP w)` with `r = 2.5%`, subject to `1'w = 1` and `w >= 0`; weights come from the posterior moments `mu_EP = E_q*[R]`, `Sigma_EP = Cov_q*[R]`.
- **Holding period / rebalance:** **weekly**, weights regenerated each week from the new ranking (Appendix F: "we perform weekly portfolio rebalancing based on the generated weights"). No turnover control, no position limits beyond long-only simplex, no cash buffer rule.
- **Parameters:** base models `Qwen2.5-3B` and `Qwen2.5-3B-Instruct` (plus `0.5B` and `1.5B` in Figure 3); SFT 3 epochs, learning rate `1e-4`, cosine schedule with 10% warmup, per-device batch 1, gradient accumulation 4, about 1 hour; FinRankGRPO 1 epoch, about 12 hours, learning rate `3e-6`, cosine decay with 10% linear warmup, group size `G = 4` sampled responses per prompt, `temperature = 1.0`, `top-k = 50`, `top-p = 1.0`, prompt max 1024 tokens; full-parameter training on **3 NVIDIA L20 GPUs** with bfloat16, `torch 2.9.1`, `transformers 4.57.1`, `trl 0.9.6` (Appendix C). Reward: `-1` on structural error, `sigma(rho_s)` when Spearman `rho_s > 0`, `rho_s` when `rho_s <= 0`, with within-group standardized advantage and a clipped importance-ratio objective (KL term "omitted for readability").
- **Training-label construction (Section 4.1, Appendix B):** for each sample, among the CoT responses produced by GPT-4o-mini, Claude-3.5-Sonnet and DeepSeek-Chat, the source retains **the response with the highest Spearman correlation against the realized ground-truth return ranking**; within each calendar year, samples are then sorted by that Spearman with the **top 50% forming the SFT subset and the bottom 50% the FinRankGRPO subset**. Selecting supervision on the realized target is a source-fixed design choice, visible only in Appendix B.
- **Ground truth:** "the ground-truth ranking induced by future realized returns" (Section 4.3) over the 15 ETFs for the target week.
- **Reconstructability:** the *rule* is reconstructable from the paper (ranking -> EP views -> max-Sharpe with `r = 2.5%` -> weekly rebalance -> 5 bps per turnover). The *result* is not reconstructable without Bloomberg prices under an institutional license, the WSJ archive, the DeepSeek-Chat digests, the distilled CoT dataset and the fine-tuned checkpoints; the stated replication URL returns HTTP 401. Missing or `underspecified`: scenario window `K`, prior `p`, prompt texts (given only as figures), tie/JSON-error handling at inference, the risk-free rate used in the *reported* Sharpe, and the number of trials' dispersion.

## Required data

- **Instrument / universe:** 15 US-listed ETFs - 3 size indices (`IVV`, `IJH`, `IJR`), 9 GICS sector SPDRs (`XLB`, `XLE`, `XLF`, `XLI`, `XLK`, `XLP`, `XLU`, `XLV`, `XLY`) and 3 alternatives (`GLD`, `GSG`, `IYR`). Market type: **cash equity ETFs** only - no futures, no options, no crypto.
- **Price data:** Bloomberg daily/weekly ETF prices under the source's institutional academic license; the license forbids redistribution - `data gap` for independent replication.
- **Text data:** FNSPID (2010-2023, stated CC BY 4.0) and WSJ archive headlines (2024-2025), aggregated weekly, SimHash de-duplicated (Hamming 25), summarized by DeepSeek-Chat into an asset-focused market digest.
- **Model artifacts:** Qwen2.5 0.5B/1.5B/3B Base and Instruct checkpoints, SFT and FinRankGRPO stage weights, distilled CoT training set (top-50%/bottom-50% yearly split), and commercial API models GPT-4o-mini, Claude-3.5-Sonnet (20241022), DeepSeek-Chat (V3.2) for baselines and distillation.
- **Point-in-time / availability:** chronological split 2010-2019 train / 2020-2025 test is stated as the look-ahead control; the source concedes in Limitations that LLM pretraining may already contain 2020-2025 financial text and market outcomes, and **no time-controlled checkpoint was used** - `data gap` for any strict point-in-time claim. News publication timestamps, timezone and the availability lag of the weekly digest are `not stated in source`.
- **Missing data / corporate actions:** not discussed anywhere - `data gap`. ETF share creations, dividends and tracking are not mentioned; the price adjustment convention (total return versus price return) is **not stated in source** - `data gap`, which matters because sector-ETF dividends are not negligible over 2020-2025.
- **Not applicable to this signal:** funding, mark/index price, open interest, order book, trade aggressor side, options surface/Greeks - the source uses prices and text only.

## Execution assumptions

Source-reported:

- **Signal-to-order timing:** ranking generated for week `t+1` from week `t` inputs; trades executed **at the weekly closing price** of the rebalance week (Appendix F). Same-bar versus next-bar ambiguity at the weekly boundary is not discussed - `data gap`.
- **Order type / fill model / latency / partial fills / participation cap:** **`data gap`** - none of these is described; fills are assumed to occur at the weekly close with no market-impact or participation constraint.
- **Fees:** **5 bps (0.05%) per turnover**, described as covering "commissions and bid-ask spreads" (Appendix F). Whether turnover is one-way or two-way is **not defined** - `underspecified`; no commission schedule, no exchange fee and no borrow fee is given.
- **Spread / slippage:** slippage assumed **zero** by fiat for the selected ETFs; the spread itself is not modeled separately from the flat 5 bps.
- **Management fees:** explicitly **excluded** (source states this is to isolate alpha) - so reported numbers are gross of ETF expense ratios.
- **Turnover:** **never reported** - `data gap`; a weekly full re-ranking of a 15-name long-only book typically produces material turnover, but no number exists in the source.
- **Leverage / margin / shorting:** long-only, fully invested (`1'w = 1`, `w >= 0`), no leverage, no shorting - shorting constraints are moot; margin and financing are `not applicable` as specified.
- **Capacity / liquidity:** never quantified (`capacity` in the paper always means neural-network capacity) - `data gap`.
- **Taxes:** not mentioned - `data gap`.
- **Distinction:** every performance number in this record is **net of one flat 5 bps per turnover charge and gross of spread in practice, slippage, market impact, management fees, taxes and any capacity limit**, on a 15-ETF universe over 314 out-of-sample weeks. Nothing in the source supports the word "tradable".

## Evidence

### Source-reported

All figures below are third-party claims from the pinned `arXiv:2609.24175v1` (PDF page / table / figure provenance given) and have **not** been independently reproduced. Table 1 values are **"the mean performance averaged over 5 independent trials"** (Table 1 caption, PDF page 6); no dispersion is printed anywhere.

**Main results (PDF Table 1, page 6; test window 2020-2025, 314 weekly samples, 15 ETFs, 5 bps per turnover, weekly close execution):** columns are `Spear. | Kend. | N@3 | N@5 | Ann. Ret. | Sharpe | Max DD | Calmar`.

| Model | Spear. | Kend. | N@3 | N@5 | Ann. Ret. | Sharpe | Max DD | Calmar |
|---|---|---|---|---|---|---|---|---|
| Ground Truth | 1.000 | 1.000 | 1.000 | 1.000 | 1.049 | 7.655 | 0.138 | 7.618 |
| EW | - | - | - | - | 0.085 | 0.302 | 0.356 | 0.239 |
| MVO-SR | -0.007 | -0.006 | 0.569 | 0.596 | 0.080 | 0.339 | 0.268 | 0.299 |
| Momentum | -0.028 | -0.021 | 0.544 | 0.581 | 0.041 | 0.107 | 0.209 | 0.195 |
| Deepseek-Chat | 0.016 | 0.017 | 0.573 | 0.603 | 0.095 | 0.457 | 0.227 | 0.418 |
| GPT-4o-mini | 0.016 | 0.014 | 0.520 | 0.551 | 0.080 | 0.356 | 0.252 | 0.321 |
| Claude | 0.001 | 0.004 | 0.567 | 0.595 | 0.086 | 0.363 | 0.249 | 0.345 |
| Qwen2.5-3B | 0.002 | 0.001 | 0.032 | 0.033 | 0.070 | 0.289 | 0.266 | 0.276 |
| Qwen2.5-3B +SFT | 0.007 | 0.006 | 0.532 | 0.560 | 0.092 | 0.392 | 0.220 | 0.422 |
| Qwen2.5-3B +GRPO | 0.016 | 0.012 | 0.526 | 0.555 | 0.091 | 0.424 | 0.228 | 0.404 |
| Qwen2.5-3B +FinRankGRPO | 0.021 | 0.016 | 0.557 | 0.585 | 0.111 | 0.568 | 0.219 | 0.508 |
| Qwen2.5-3B-Instruct | -0.001 | -0.003 | 0.177 | 0.184 | 0.111 | 0.513 | 0.254 | 0.440 |
| Qwen2.5-3B-Instruct +SFT | 0.019 | 0.015 | 0.522 | 0.552 | 0.092 | 0.444 | 0.249 | 0.375 |
| Qwen2.5-3B-Instruct +GRPO | 0.020 | 0.016 | 0.517 | 0.549 | 0.092 | 0.445 | 0.237 | 0.402 |
| **Qwen2.5-3B-Instruct +FinRankGRPO** | **0.023** | **0.018** | **0.577** | **0.606** | **0.122** | **0.636** | **0.211** | **0.580** |

Source narrative for Table 1 (Section 4.4): annualized return 0.122 "exceeding the equal weight benchmark (0.085) and the leading commercial methods (Deepseek-Chat with 0.095)"; "highest Sharpe(0.636)"; and the claim that "improved ranking accuracy directly translates into superior portfolio returns".

**Reward ablation (PDF Table 2, same SFT-initialized base model):** `NDCG@3` Spear. 0.000 / Kendall 0.000 / Sharpe 0.412 / Max DD 0.223; `Kendall's Tau` 0.000 / 0.002 / 0.441 / 0.220; `FinRankGRPO` 0.023 / 0.018 / 0.636 / 0.211.

**Sentiment-inversion faithfulness (PDF Table 3, Spearman original / inverted / difference):** DeepSeek-Chat 0.016 / -0.021 / **0.037**; Qwen2.5-3B-Instruct -0.001 / 0.006 / -0.008; +SFT 0.019 / -0.010 / 0.029; +FinRankGRPO 0.023 / -0.011 / **0.034**. Source reading: a larger drop means greater sensitivity to semantic direction.

**2020 recession stress test, February-April 2020 (PDF Table 4; columns Spear. / Kendall / Sharpe / Max DD):** DeepSeek-Chat 0.051 / 0.039 / 0.193 / 0.201; GPT-4o-mini 0.042 / 0.050 / 0.386 / 0.211; Claude 0.050 / 0.046 / 0.486 / 0.202; Qwen2.5-3B-Instruct 0.049 / 0.092 / **-0.184** / 0.250; +SFT 0.068 / 0.054 / **-0.266** / 0.211; +FinRankGRPO 0.070 / 0.055 / 0.486 / 0.209. Section 5.6 additionally gives the FinRankGRPO recession Sharpe as **0.4863** and describes a 2020-03-09 case study where the model ranks `GLD` and `XLP` defensively.

**Base-model scaling (PDF Figure 3 labels, read off the figure):** Sharpe for 0.5B / 1.5B / 3B is **0.521 / 0.453 / 0.568 (Base)** and **0.505 / 0.500 / 0.636 (Instruct)**; Spearman is **0.012 / 0.021 / 0.021 (Base)** and **0.014 / 0.020 / 0.023 (Instruct)**. Section 5.1 text quotes the 0.5B Base pair (0.012, 0.521), the 3B Base pair (0.021, 0.568) and the 3B-Instruct pair (0.023, 0.636).

**Two-stage training progression (PDF Figure 4 labels):** Sharpe Original / SFT / FinRankGRPO = **0.289 / 0.392 / 0.568 (Base)** and **0.513 / 0.444 / 0.636 (Instruct)**.

**Input ablation (PDF Figure 5 labels; Section 5.4):** Spearman **0.023 (Ours) / 0.012 (w/o Days) / 0.010 (w/o News)**; Sharpe **0.636 / 0.677 / 0.045**. Source reading: "removing news content sharply reduces the Sharpe ratio from 0.636 to 0.045. In contrast, removing trading date information does not hurt Sharpe ratio and even slightly improves it from 0.636 to 0.677, while reducing the Spearman correlation from 0.023 to 0.012".

**Optimization-signal diagnostics (Section 4.4):** standard GRPO with exact-match reward gives zero reward to all sampled actions and **35.14% zero-loss training steps**; FinRankGRPO produces non-zero rewards for all sampled responses and non-zero loss in **99.68% of steps**.

**Evaluation-metric definitions (Section 4.3, Appendix F):** rank metrics Spearman, Kendall, NDCG@3 and NDCG@5 against the realized next-week ordering; portfolio metrics Annualized Return, Annualized Volatility, Sharpe Ratio, Maximum Drawdown and Calmar Ratio. `Ann. Vol.` is defined in Appendix F but **never printed in any table**; the risk-free rate used *inside the reported Sharpe* is never stated (Equation 9's optimizer uses `r = 2.5%`) - `underspecified`.

**Research-computed arithmetic checks of source numbers (inputs are source-reported; the arithmetic is ours, not a reproduction):** FinRankGRPO Sharpe gap over equal weight = 0.636 - 0.302 = **0.334**; over the best commercial baseline = 0.636 - 0.457 = **0.179**; rank-variance share of the best test Spearman = 0.023^2 = **0.0005** (about 0.05%); number of test weeks implied by 2020-2025 = **314**; announced flat fee = 5 bps = **0.0005** per turnover unit; Calmar cross-check 0.122 / 0.211 = **0.578** against the printed 0.580 (rounding); ratio of oracle to realized Sharpe = 7.655 / 0.636 = **12.0**. These checks confirm transcription and internal arithmetic consistency only.

### Independently reproduced

`not independently reproduced`

No model was trained, no prompt was run, no portfolio was constructed, no backtest was executed, and neither Bloomberg data nor the FNSPID/WSJ text pipeline was obtained for this record. The only actions taken were: reading the pinned HTML and PDF end to end, re-extracting Table 1 and the cost paragraph directly from the pinned PDF, checking the stated replication URL (HTTP 401), running read-only repository and Wiki Brain dedup searches, and arithmetic cross-checks of printed values. Reading source-reported numbers verifies **transcription and internal consistency**; it is **not** independent reproduction of the result.

### Negative evidence

1. Best out-of-sample rank correlation anywhere in Table 1 is **Spearman 0.023** (rho^2 about 0.0005), i.e. the ranking is statistically indistinguishable from noise, while the source claims ranking accuracy "directly translates into superior portfolio returns".
2. The source's own input ablation **contradicts the translation claim**: removing the date input cuts Spearman 0.023 -> 0.012 yet *raises* Sharpe 0.636 -> 0.677, so the metric being optimized and the metric being monetized move in opposite directions.
3. Removing news collapses Sharpe to **0.045** while Spearman only falls to 0.010 - the returns therefore do not track ranking quality even within the same ablation.
4. **Pretraining look-ahead is admitted by the authors**: the 2020-2025 evaluation window "may introduce potential lookahead bias due to the pretraining data of modern LLMs" and no time-controlled checkpoint was used; a chronological train/test split does not fix a model that has already seen the test period's text and market outcomes.
5. **No statistical inference anywhere**: the pinned PDF contains zero occurrences of `standard deviation`, `confidence interval`, `significance`, `p-value`, `t-test` and `seed`; Table 1 reports a mean over 5 trials with no dispersion, so the 0.636 versus 0.457 gap over the best commercial baseline is unquantified.
6. **Cost model is a single flat 5 bps per turnover** with zero slippage assumed, management fees excluded, and no cost sensitivity ladder; whether turnover is one-way or two-way is undefined.
7. **Turnover is never reported** (the word occurs exactly once, inside the cost sentence), so the only cost that is modeled cannot be evaluated - cost drag is `data gap`, not zero.
8. **No passive benchmark**: `buy and hold` occurs zero times in the pinned PDF; equal weight (Sharpe 0.302) is the only passive reference, and neither IVV buy-and-hold nor a dividend-adjusted index return is reported.
9. Universe is **15 ETFs in one asset class mix** (US size, US sectors, gold, broad commodities, US REITs) - no bonds, no non-US equity, no cash sleeve, no crypto; results may be dominated by a single 2020-2025 path.
10. **Single split, single window**: 314 non-overlapping test weeks from one chronological cut, no walk-forward, no rolling origin, no second holdout, and no multiplicity control over the many reported variants (Tables 1-4, Figures 3-5).
11. The **`Ground Truth` row (Ann. Ret. 1.049, Sharpe 7.655, Max DD 0.138)** is a look-ahead construction printed in the same table as tradable rows, and the paper never describes how that row was built (`oracle` / `upper bound` appear zero times).
12. **Label selection on the realized target**: for each training sample the source keeps the CoT response with the *highest Spearman against realized future returns*, and splits each year into top-50% SFT / bottom-50% RL subsets by that same realized Spearman - supervision is chosen using the answer key, which is not available at inference time.
13. **Summarizer confound**: the weekly news digest is produced by DeepSeek-Chat, which is also one of the evaluated baselines (Sharpe 0.457); the choice of summarizer is never ablated, so part of the comparison is between models sharing a representation generator.
14. **Training/test construction differs**: training uses a rolling weekly window (yielding 2,516 samples over 10 years, i.e. roughly daily-stepped overlapping windows) while the test set uses non-overlapping calendar weeks; the label "2,516 weekly samples" is inconsistent with the span, so the effective independence of training observations is unknown.
15. **Weak momentum baseline**: "Short-Term Momentum" ranks on the preceding two weeks of returns and delivers Sharpe 0.107, an implausibly weak reference that flatters every LLM row; equal weight and MVO-SR are the credible passive/naive comparators.
16. **SFT alone damages the Instruct model**: Figure 4 shows Instruct Sharpe falling 0.513 -> 0.444 under SFT before Stage 2 recovers it to 0.636, so the reported gain depends on a two-stage pipeline whose first stage is negative on its own.
17. **Scaling claim is non-monotone**: Figure 3 shows the 1.5B Base Sharpe (0.453) *below* the 0.5B Base (0.521) and the 1.5B Instruct (0.500) below the 0.5B Instruct (0.505), contradicting the "consistent with scaling law" reading in Section 5.1.
18. **Crisis-period instability**: in the February-April 2020 stress window the base model is at Sharpe -0.184 and the SFT stage at -0.266, and the final model's 0.486 only *ties* Claude's 0.486 - the pipeline's crisis behavior is not stable across adjacent variants and the tie is reported as a sole win.
19. **Faithfulness test is tiny in absolute terms**: the sentiment-inversion drop for FinRankGRPO is Delta Spearman 0.034 from a base of 0.023 to -0.011, i.e. both levels are near zero; no portfolio-level faithfulness check (does Sharpe collapse under inverted news?) is reported.
20. **No risk-model control**: no Fama-French/Carhart regression, no beta, size, sector or volatility matching, no style-neutralization - because the book is long-only over sectors, the 0.122 annualized return may be sector or defensive-tilt beta rather than text alpha.
21. **Sharpe definition gap**: Equation 9 uses `r = 2.5%` for optimization, but the risk-free rate used in the *reported* Sharpe is never stated, and `Ann. Vol.` - though defined - is never printed, so the reported Sharpe cannot be re-derived from the table.
22. **Price-adjustment convention absent**: the source never states whether ETF returns are price or total return, which materially affects a 6-year long-only sector comparison - `data gap`.
23. **No capacity, no participation, no order model**: fills are assumed at the weekly close with zero slippage; latency, partial fills, order type and any participation cap are `data gap`.
24. **Replicability**: Bloomberg prices are under an institutional academic license, the WSJ archive is a paid source, and the announced replication package returns HTTP 401 (checked 2026-09-28) - no independent path to re-derive a single number exists.
25. **Source quality**: preprint only, single subject class `cs.CE` with no q-fin cross-list, no Comments field, no journal reference, no peer review, DataCite DOI marked "pending registration", and AI tools used for language polishing (stated by the authors).
26. **Cross-record contrary evidence in this repository (different sources, same broad family):** `benzinga-daily-headline-sentiment-cross-sectional-rank-ic-null-2026-09-24.md` reports an FDR-controlled null for daily headline-sentiment rank IC across seven classifiers, and `retail-equity-anomaly-pit-search-aware-falsification-volatility-positive-control-2026-09-27.md` documents search-aware falsification of equity anomalies; neither shares this source identity, but both weaken the prior that short-horizon text signals survive honest controls.

## Falsification plan

All thresholds below are **research-defined falsification thresholds** unless the source itself states the number; every operational rule not present in the source is labeled `research-proposed`.

- **F1 - Frozen forward replication.** `research-proposed` rebuild of the full pipeline (weekly digest -> ranking -> entropy pooling -> long-only max Sharpe) evaluated on the frozen forward window starting **2026-10-01** for at least 12 months. **Fail** if forward Sharpe <= 0 or forward excess return over equal weight <= 0 (research-defined).
- **F2 - Number reproduction gate.** Re-run the pinned pipeline (or its faithful open reimplementation) on the same 2020-2025 window. **Fail** if the headline Sharpe differs from **0.636 by more than 0.10**, the annualized return differs from **0.122 by more than 0.02**, or the Spearman differs from **0.023 by more than 0.005** (research-defined tolerances).
- **F3 - Cost ladder.** `research-proposed` apply round-trip cost rungs of 0 / 5 / 10 / 20 / 50 bps per turnover on the *measured* turnover. **Fail** implementability if net Sharpe < 0.5 at 10 bps or net excess return over equal weight <= 0 at any rung at or below 20 bps (research-defined).
- **F4 - Turnover and capacity audit.** Compute one-way weekly turnover, days-to-fully-turn, and the ADV participation needed to trade the whole book each week. **Fail** implementability if sustained one-way turnover exceeds **25% of NAV per week** or any single rebalance needs more than **10% of that ETF's 20-day ADV** (research-defined); report turnover as measured, never as zero.
- **F5 - Rank-information test (targets `contradictions` 1).** Over the 314 test weeks, test whether weekly Spearman is positive using a stationary block bootstrap (4-week blocks, 1,000 draws). **Fail** the ranking-information claim if the 95% interval for mean Spearman includes **0** (research-defined).
- **F6 - Placebo null.** 1,000 draws of week-circularly-shifted news digests through the identical pipeline (or shuffled rankings with the same constraint structure). **Fail** if the realized Sharpe 0.636 does not exceed the **95th percentile** of the placebo distribution (research-defined).
- **F7 - Pretraining look-ahead audit (targets `contradictions` 10).** Re-evaluate with a model whose pretraining cutoff precedes the test window, or run the whole test on a pre-cutoff pseudo-out-of-sample window (for example 2015-2019 evaluated with a model released before 2019). **Fail** if the model retains less than **50%** of the reported Sharpe advantage over equal weight (research-defined).
- **F8 - Input-ablation replication (targets `contradictions` 1).** Reproduce Figure 5 exactly: news-removed Sharpe **0.045**, date-removed Sharpe **0.677**, Spearman **0.023 / 0.012 / 0.010**. **Fail** the source's "ranking accuracy translates into returns" claim if Spearman and Sharpe remain decoupled in the reproduction (research-defined: fail if the sign of the Spearman change and the sign of the Sharpe change disagree in at least two of the three ablation cells).
- **F9 - Passive and timing baselines.** Add buy-and-hold IVV, dividend-adjusted equal weight, a 2-week-momentum tilt and a simple 200-day-trend sector rotation, all at the same 5 bps cost. **Fail** if FinRankGRPO net Sharpe <= the best of these baselines (research-defined).
- **F10 - Factor and style control.** Regress the weekly long-only excess return over equal weight on FF5 + momentum plus sector-rotation controls with HAC standard errors. **Fail** if alpha < 0 or t < **1.96** (research-defined).
- **F11 - Subperiod / regime stability.** Split 2020, 2021-2022, 2023-2025 and re-evaluate. **Fail** if the excess return over equal weight changes sign in any subperiod or the 2020-02/04 stress Sharpe is below **0** (research-defined).
- **F12 - Label-selection audit (targets `contradictions` 2 / negative evidence 12).** Re-train Stage 1 with supervision chosen *without* the realized target (random selection among the three CoT responses, or majority vote), keeping everything else fixed. **Fail** if reported Sharpe drops by more than **30%** (research-defined), which would show the pipeline depends on answer-key selection.
- **F13 - Summarizer and prompt robustness.** Swap DeepSeek-Chat for an open summarizer, and separately feed raw de-duplicated headlines without a digest. **Fail** if Sharpe changes by more than **20%** or if DeepSeek-Chat-as-summarizer is what produces the gap over the DeepSeek-Chat baseline (research-defined).
- **F14 - Multiplicity and trial dispersion.** Request per-trial values for all 5 trials of every row in Tables 1-4, apply Benjamini-Hochberg at **q < 0.10** across the ablation grid, and compute a deflated Sharpe that accounts for the reported model/reward/size/search grid. **Fail** if the headline row does not survive at q < 0.10 (research-defined).

Action on failure: the record stays `research-only`, `not-implemented`, `not-approved`; a failed F2, F5, F6, F7, F10 or F12 should be reported back to Research Intake Review as grounds for REJECT rather than for retuning.

## Crypto portability

**Unproven.**

- The source tests **only** 15 US-listed ETFs and makes **no crypto claim**; nothing in the paper or the availability statement touches digital assets, so portability is a `research-proposed` hypothesis, not evidence.
- The mechanism as stated (text -> listwise ranking -> entropy-pooling mean views -> long-only max-Sharpe rotation) is *formally* asset-class-agnostic, which is why an `adapted` reading is tempting; but every material data dependency is asset-specific: Bloomberg ETF prices, FNSPID and WSJ US-headline corpora, and a 15-ETF universe chosen because it is "closer to institutional asset allocation". A crypto port would need a `research-proposed` universe (for example the top-20 liquid USDT pairs by point-in-time volume), a `research-proposed` crypto news corpus with publication timestamps, and a `research-proposed` digest/checkpoint pipeline - a materially different data dependency, hence `unproven`.
- Instrument and market-structure mismatch: 24/7 sessions versus weekly US equity sessions and the weekly-close fill assumption; venue fragmentation across many exchanges; spot versus perpetual differences with funding, mark price and liquidation mechanics that the source never models; candle-boundary and timezone conventions absent from the source; thin and unstable altcoin universes with severe listing survivorship.
- Cost and friction mismatch: the flat 5 bps per turnover "for commissions and bid-ask spreads" does not transfer to crypto taker/maker schedules, funding payments on any perpetual leg, or wide spreads on smaller pairs; no borrow or shorting is contemplated by the source at all.
- If anyone attempts a port, every operational choice (universe, news source, ranking cadence, EP prior, constraint set, cost model, session boundary) is `research-proposed` until tested; crypto portability is **not** authorization to trade.

## Limitations

- **Source quality:** unrefereed arXiv preprint in `cs.CE` only, no Comments field, no journal reference, no peer-review statement, DataCite DOI "pending registration", announced replication URL returning HTTP 401 at read time, and AI-assisted language polishing disclosed. Treat every performance figure as a third-party claim.
- **Sample:** 314 non-overlapping test weeks, 2020-2025, one chronological split, one universe, 5-trial means without dispersion; no out-of-sample beyond 2025, no walk-forward, no multiplicity control.
- **Look-ahead:** admitted pretraining exposure to the evaluation window; no time-controlled checkpoints. `data gap` for a strict point-in-time claim.
- **Signal quality:** best test Spearman 0.023 (rho^2 about 0.0005); ranking quality and portfolio quality are decoupled in the source's own ablations.
- **Costs:** a single flat 5 bps per turnover with zero slippage assumed and management fees excluded; turnover never reported; no spread-in-practice, impact, latency, participation or capacity treatment. `data gap` - never treat as zero.
- **Sharpe definition:** risk-free rate of the *reported* Sharpe not stated (the optimizer uses 2.5%); `Ann. Vol.` defined but never printed, so Sharpe and Calmar cannot be re-derived from the tables. `underspecified`.
- **Returns convention:** price versus total return on the ETFs is never stated. `data gap`.
- **Training pipeline:** supervision selected per sample by realized Spearman against the answer key; SFT/RL subset split also keyed to realized Spearman; summarizer shared with a baseline; prompt templates exist only as figures.
- **Reproducibility:** Bloomberg academic-license data, paid WSJ archive, non-public checkpoints and a 401 replication URL - none of the headline numbers can be re-derived by an independent party today.
- **Described oracle:** the `Ground Truth` row's construction is never explained in the text.
- **Contested:** this record carries `contested: true` with ten frontmatter contradictions; none has been reconciled and none should be silently resolved downstream.
- **Not independently reproduced.**
- **Incremental-write check:** no existing record in this repository shares this source identity (hidden-inclusive `rg -uuu` returned zero hits for `2609.24175`, `10.48550/arXiv.2609.24175`, `FinRankGRPO`, `Ningyuan Deng`, `Jinyuan Wang`, `listwise financial asset ranking`, `Financial Asset Ranking via Group` and the anonymous code URL; a separate `Entropy Pooling` scan also returned zero; positive control `novy-marx` matched); Wiki Brain `kb_search` returned zero pages for the listwise-ranking-plus-entropy-pooling mechanism.

## Implementation status

`implementation_status: not-implemented`.

Nothing has been implemented in our research stack. No news corpus was obtained, no LLM was prompted or fine-tuned, no entropy-pooling problem was solved, no portfolio was constructed, no backtest run, no Qlib full-backtest executed, and no Paper, Testnet or Live workflow touched. This document is a normalized research capture of a third-party preprint plus checks of its pinned HTML/PDF and of the availability of its stated replication package. The numbers above are source-reported claims with page/table/figure provenance, not our results.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this record in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. It also does not mean the source's ten contradictions have been reconciled, that its ranking-accuracy-to-returns claim holds, or that its cost, turnover, fill, price-adjustment or look-ahead assumptions have been verified. Any later adoption or implementation decision must be explicit, separately reviewed, and based on this record plus current sources.

## Related Wiki records

Verified adjacent pages (found via read-only `kb_search`, none shares this source identity):

- [[quant/finsmart-market-aligned-reinforcement-learning-sentiment-alpha-2026-09-02]] - adjacent in that both use GRPO-style reinforcement learning to align an LLM with a financial objective; differs in mechanism (cross-sectional equity sentiment alpha versus listwise ETF ranking into entropy pooling), in market (individual equities versus a 15-ETF allocation book) and in source identity.
- [[quant/trading-r1-curricular-reinforcement-learning-llm-reasoning-2026-09-05]] - adjacent in that both train an LLM with reinforcement learning for trading decisions; differs in signal (reasoning distillation for trading decisions versus Spearman-reward listwise ranking) and in source identity.
- [[quant/small-cap-alpha-beta-separation-uncertainty-aware-llm-portfolio-2026-09-02]] - adjacent in that both turn LLM-derived views into portfolio weights; differs in mechanism (multimodal uncertainty-aware small-cap alpha-beta separation versus EP ordinal views on ETFs) and in source identity.
- [[quant/strategy-research-record-spec-v1]] - the schema specification this record conforms to.

No Wiki Brain page for the listwise-ranking-into-entropy-pooling mechanism exists yet; searches for `LLM listwise asset ranking portfolio entropy pooling GRPO ETF news` and `LLM news sentiment ETF rotation long-only weekly portfolio` returned zero pages.

Nearest records in this repository (source identity and mechanism differ on every axis; none is a duplicate):

- `finatom-head-free-token-generation-etf-allocation-dapo-grpo-2026-09-04.md` - different source (Ouyang and Lee, arXiv 2608.09880), different mechanism (numeric next-period return forecasting emitted as tokens with DAPO/GRPO, then constrained allocation) versus ordinal ranking with a Spearman reward and entropy-pooling views.
- `maple-multi-alpha-position-aware-listwise-ensembling-2026-09-04.md` - different source and different mechanism (listwise ensembling of many formulaic alphas for stock selection versus one LLM ranking 15 ETFs from news).
- `group-aware-policy-optimization-grpo-gspo-lob-directional-trading-2026-09-18.md` - different source (arXiv 2605.25527), different market (limit-order-book directional trading) and different reward, though it shares the GRPO family name.
- `mfast-market-friction-aware-llm-news-sentiment-quintile-2026-09-22.md` and `llm-news-enhanced-cross-sectional-momentum-tilt-2026-09-06.md` - different sources, different mechanisms (news sentiment scores into daily long-short quintiles / momentum tilts versus weekly listwise ETF ranking into a long-only optimizer).
- `benzinga-daily-headline-sentiment-cross-sectional-rank-ic-null-2026-09-24.md` - different source, but the closest contrary result in this repository: an FDR-controlled null for daily headline-sentiment rank IC, relevant as prior evidence that short-horizon headline signals can fail honest controls.

## Sources

1. Deng, N., Wang, J., Li, Q., Zhang, J., and Yang, Y. (2026). *FinRankGRPO: Optimizing LLMs for Listwise Financial Asset Ranking via Group Relative Policy Optimization*. arXiv preprint `arXiv:2609.24175v1 [cs.CE]`, submitted 21 Sep 2026 06:45:38 UTC; single version; no Comments field, no journal reference, no publisher DOI (DataCite identifier `10.48550/arXiv.2609.24175` shown as "pending registration"); license CC BY 4.0. Landing `https://arxiv.org/abs/2609.24175` (read 2026-09-28) for author list, version/date, subject class, license and publication status.
2. Same paper, pinned full text `https://arxiv.org/html/2609.24175v1`, downloaded 2026-09-28: **276,095 bytes, SHA-256 `b094bc1175b62a5e9ad1243267e3506158de3005252ffaead6031bf75030ca2e`**, 64,411 characters, read end to end (Abstract, Sections 1-6, Limitations, Appendix A-I, Tables 1-7, Figures 1-9). Source for affiliations, Equation 9's `r = 2.5%`, dataset construction and the Section 4.4 / 5.x claims.
3. Same paper, pinned PDF `https://arxiv.org/pdf/2609.24175v1`, downloaded 2026-09-28: **932,549 bytes, 16 pages, SHA-256 `f592c2418b9d52d22110ae6f53e191357ae0f960301c011b14a01aa76cff3458`**, text-extracted with `pypdf` to 54,598 characters and read in full. Table 1 re-extracted from page 6; the cost paragraph located on pages 13-14 (Appendix F); word-scan counts for `turnover`, `slippage`, `standard deviation`, `confidence interval`, `p-value`, `oracle`, `buy and hold` taken from this text.
4. Replication package named in the abstract: `https://anonymous.4open.science/r/FinRankGRPO-7107/` - checked 2026-09-28, HTTP 302 to `https://anonymous.4open.science/api/repo/FinRankGRPO-7107/file/` which returns HTTP 401; **not publicly retrievable**, so no code, data or checkpoint provenance could be pinned - `data gap`.
5. Data vendors and models named by the source (cited here as the source's declared basis; none of these was read for this record): Bloomberg prices under an institutional academic license; FNSPID (Dong et al., 2024, stated CC BY 4.0); The Wall Street Journal news archive for 2024-2025; DeepSeek-Chat as digester and baseline; GPT-4o-mini and Claude-3.5-Sonnet as distillers and baselines; Qwen2.5 0.5B/1.5B/3B Base and Instruct as trained models; Entropy Pooling as the view-integration method (Meucci, cited by the source - `data gap`, not read).

No Wiki Brain write, no Kanban task, no backtest, no implementation; hard cap 1 record.
