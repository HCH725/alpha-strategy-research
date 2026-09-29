---
schema: strategy-research-record-v1
title: "AlphaPareto: LLM-Encoded Alpha-Pool State plus Pareto-Regularized Multi-Objective RL for Formulaic Alpha Discovery (CSI300 / CSI800 / full A-share market, S&P 500, monthly top-50 long-only)"
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - llm-reasoning
  - reinforcement-learning
  - formulaic-alpha
  - cross-sectional
  - equity
status: research-only
confidence: medium
source_as_of: 2026-09-28
sources:
  - "https://arxiv.org/abs/2609.34188 (arXiv:2609.34188v1 [stat.ML], submitted 28 Sep 2026 03:03:41 UTC; landing read 2026-09-29)"
  - "https://arxiv.org/pdf/2609.34188v1 (pinned v1 PDF, 19 pages, 2981862 bytes, SHA-256 fb160d025d64f3f2b2fe36effeb3ef6303cb9aa91468b6bb45ec1aa2475d98cd, fetched 2026-09-29)"
  - "https://github.com/BiQiBaoWinner/AlphaPareto (code repository named in §5 of the paper; HEAD commit bdc92dfa9aa8a3849459c9a3568bd38a15af56d8 of branch main, metadata read via the GitHub REST API on 2026-09-29, contents not inspected)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Section 5.2 states 'We use the DeepSeek-R1 model family to provide LLMs of different parameter scales', but Table 3 in the same subsection prints a Qwen-Embedding-4B row (not a DeepSeek-R1 model), Table 6 lists Qwen-Embedding-4B among the 'LLM candidates', and §5 plus Appendix E.1 name Qwen-Embedding-4B as the encoder used for every headline result; the paper never reconciles which model set the scaling study actually covers. Unreconciled in the pinned v1 text."
---

# AlphaPareto: LLM-Encoded Alpha-Pool State plus Pareto-Regularized Multi-Objective RL for Formulaic Alpha Discovery (CSI300 / CSI800 / full A-share market, S&P 500, monthly top-50 long-only)

## Provenance

**Primary source identity.** arXiv preprint `arXiv:2609.34188v1 [stat.ML]`, title *AlphaPareto: Formulaic Alpha Discovery with LLM-Guided Multi-Objective Reinforcement Learning*, landing page `https://arxiv.org/abs/2609.34188`, pinned PDF `https://arxiv.org/pdf/2609.34188v1`. The landing submission history prints exactly one version: `[v1] Mon, 28 Sep 2026 03:03:41 UTC (2,914 KB)`; submitter shown as `Zhoufan Zhu [view email]`; `citation_date` / `citation_online_date` = `2026/09/28`. The `Comments` field reads `Accepted by Neurips 2026 main track` and the PDF page-1 footer prints `40th Conference on Neural Information Processing Systems (NeurIPS 2026).` The `Subjects` line reads `Machine Learning (stat.ML) ; Artificial Intelligence (cs.AI) ; Machine Learning (cs.LG)` with stat.ML primary; the Journal-reference field carries **no printed value**, and the only DOI anywhere in the metadata is the arXiv-issued DataCite DOI `https://doi.org/10.48550/arXiv.2609.34188` (also the PDF `/DOI` field). Landing license link and PDF `/License` both name `creativecommons.org/licenses/by-sa/4.0` → **CC BY-SA 4.0**. Publication status therefore is: **accepted at a peer-reviewed venue (NeurIPS 2026 main track) but the version of record is not yet published as of 2026-09-29; arXiv v1 preprint only, no v2** (`source_as_of: 2026-09-28` = v1 submission date). The landing prints v1 as `(2,914 KB)` while the served artefact is 2,981,862 bytes (≈ 2,912 KiB) — two representations of the same document, recorded as printed.

**Author list (three-way match).** Exactly three authors, identical ordering in (a) the landing `citation_author` meta (`Zhao, Yingbo` / `Yang, Zeyu` / `Zhu, Zhoufan`), (b) the PDF title block and (c) the PDF `/Author` metadata (`Yingbo Zhao; Zeyu Yang; Zhoufan Zhu`): **Yingbo Zhao**, **Zeyu Yang**, **Zhoufan Zhu\*** (\* corresponding: `Corresponding author to: Zhoufan Zhu <tylerzzf@xmu.edu.cn>`). Affiliations and addresses as printed on page 1: Yingbo Zhao — School of Economics, Xiamen University, Fujian, China (`15620241152783@stu.xmu.edu.cn`); Zeyu Yang — Paula and Gregory Chow Institute for Studies in Economics, Xiamen University, Fujian, China (`yangzeyu@stu.xmu.edu.cn`); Zhoufan Zhu — School of Economics & Wang Yanan Institute for Studies in Economics, Xiamen University, Fujian, China (`tylerzzf@xmu.edu.cn`). **No ORCID, no funding statement, no conflict/competing-interest statement and no acknowledgments section** appear anywhere in the pinned PDF → all of those fields `data gap`.

**Pinned PDF read-back (primary-source checksum, performed 2026-09-29).** 19 pages, 2,981,862 bytes, SHA-256 `fb160d025d64f3f2b2fe36effeb3ef6303cb9aa91468b6bb45ec1aa2475d98cd`; pypdf 6.16.2 extraction yields 59,357 characters over 19 pages, read end to end: Abstract, §1–§6, Tables 1–11 (including Table 5 token grammar, Table 7 hyperparameters, Table 8 paired tests, Tables 9–10 appendices), Figure 1–Figure 4 captions, Algorithm 1, the full Appendix B prompt template, Appendices C–K and the reference list. PDF metadata `/Title` matches the landing title, `/arXivID` is `https://arxiv.org/abs/2609.34188v1`, `/Producer pikepdf 8.15.1`, `/Creator arXiv GenPDF (tex2pdf:0d14211)`. **Text-layer caveat:** the LaTeX-rendered rows of Tables 1, 2, 3, 4 and 10 overprint some cells (e.g. `3.92%3.92%3.92%`, `-13.29%-13.29%`); the de-duplicated single value of each cell was used below, and every figure quoted here was re-read against its column header. The arXiv full-text HTML for the same v1 (`https://arxiv.org/html/2609.34188v1`, 392,787 bytes) was fetched this run but **not** used as the reading copy.

**Implementation artefact.** §5 prints `https://github.com/BiQiBaoWinner/AlphaPareto` as "the source code for reproducing the experiments". GitHub REST API read on 2026-09-29: repository `BiQiBaoWinner/AlphaPareto`, default branch `main`, created `2026-09-28T02:25:28Z`, last push `2026-09-28T02:25:38Z`, HEAD commit **`bdc92dfa9aa8a3849459c9a3568bd38a15af56d8`** (`Initial commit`, committer date `2026-09-28T02:24:46Z`, author Yingbo Zhao), repository size 1,691 KB, 0 stars / 0 forks / 0 open issues, `license` field `null` → **no detected license file**, description: `Official code for "AlphaPareto: ..." — LLM-guided Pareto multi-objective RL for formulaic alpha mining, evaluated on Chinese A-share markets (CSI 300/800/All) with Qlib`. The **repository contents, README, data pipeline and result artefacts were not inspected this run** → code completeness, data-availability and reproducibility claims stay `data gap`, and public-use rights are `data gap` because the repository carries no license.

**Repository-wide dedup audit (2026-09-29, hidden-inclusive).** `search_files` over the entire checkout — including `.mimo-worktrees`, `.agents`, `.hermes` and `coverage_manifest.csv` (1,088,787 bytes) — for each of `2609.34188`, `AlphaPareto`, `BiQiBaoWinner`, `Yingbo Zhao`, `Zeyu Yang`, `Zhoufan Zhu`, `Pareto-regularized`, `Multi-Human-Value Alignment` → **0 records for this source**; the only `Zhoufan Zhu` hits are two *other* papers (the ReSGA tail-risk record for arXiv:2606.04576 and the AlphaRJM record's reference list citing AlphaQCM, ICML 2025), i.e. same author, different source identity. `coverage_manifest.csv` → **0** hits for `34188` / `alphapareto` / `pareto`. Mechanism-level scan for `alpha pool semantic`, `value palette`, `Relative Rank Entropy`, `perturbation fidelity`, `mega-alpha`, `MaskPPO`, `MAP-based` returned only the AlphaForge record (and its two worktree copies) — the AlphaGen/AlphaForge family vocabulary this source uses as *baselines* — and case-insensitive scans for `Qwen-Embedding`, `non-stationary MDP`, `multi-objective reward`, `Pareto efficient frontier` returned only `meta-rl-crypto-self-improving-meta-reward-trading-agent-2026-09-05.md`, `ml-conditional-asymmetric-beta-market-neutral-minvar-hedging-2026-09-25.md`, `goant-quality-diversity-multi-agent-microstructure-alpha-discovery-2026-09-12.md`, `alphazerobeta-recurrent-ppo-market-neutral-portfolio-2026-09-02.md` — unrelated prose, none of them recording this source. Positive control `novy-marx` → **33 matches across 30 `.md` records after writing, of which exactly one is this record's own dedup sentence** (i.e. 32 matches across 29 records before writing), plus `.git` internals (`COMMIT_EDITMSG` 1, `logs/HEAD` 31, `logs/refs/heads/main` 31, all pre-existing); a post-write identity re-scan for `2609.34188`, `AlphaPareto` and `BiQiBaoWinner` returns **exactly this one record**. `git log --oneline -20` was inspected only as a convenience glance (head `b227777`, the RICE-Alpha record), not as dedup evidence.

**Four-axis distinction against the closest existing records.** `alphaforge-generative-formulaic-alpha-dynamic-factor-timing-2026-09-17.md` (source: AlphaForge, AAAI 2025) improves the *combination* model with time-varying alpha weights and is one of AlphaPareto's own baselines; AlphaPareto's claim lives in the *search* objective — a vector reward `(IC, RRE, PFS, DH)` scalarized by a MAP dual — and in putting the LLM-encoded pool into the MDP state. `alphag-opd-reliability-gated-sibling-counterfactuals-symbolic-alpha-2026-09-05.md` uses on-policy distillation with reliability gates on sibling counterfactuals (distillation mechanism, no multi-objective reward, no pool-as-state). `alpharjm-reward-jump-memory-sde-critic-symbolic-alpha-2026-09-11.md` changes the *critic/reward memory* (reward-jump memory, SDE critic) under a scalar objective — AlphaPareto explicitly rejects scalarization-by-hand. `alpha-foundry-gp-gflownet-formulaic-alpha-mining-crypto-perps-2026-09-19.md` searches on **crypto perpetual** universes with GP + GFlowNets — different universe/market type and different search machine; `goant-quality-diversity-multi-agent-microstructure-alpha-discovery-2026-09-12.md` searches **market-microstructure** text/data with a quality-diversity multi-agent scheme — different input data dependency. `mufasa-self-evolving-multi-agent-symbolic-valuation-discovery-arxiv-2609.32746-2026-09-29.md` mines *valuation* reasoning rather than price-volume formulas. Shared vocabulary (formulaic alpha, RPN grammar, mega-alpha, MaskPPO) reflects a common research lineage, not a shared source. Every pair differs in source identity **and** in at least one of mechanism, signal construction, universe/market type, horizon/regime or material data dependency → independent record under the dedup contract.

## Economic mechanism

### Source-reported

The authors' thesis (§1, §2) is a **claim about the search procedure**, not a market premium. They argue that RL-based formulaic alpha discovery suffers two structural defects: (i) **non-stationarity** — the reward `R(f_t, F_t)` depends on the evolving alpha pool `F_t` while the state encodes only the token sequence `z_t`, so "the same state-action trajectory may receive different rewards at different stages of training"; (ii) **single-objective reward design** — every prior method optimises the scalar in-sample IC of the combined signal, even though pool quality "is inherently multi-dimensional". Their answer, with component roles kept explicit:

- **Regime:** none. No regime filter, no volatility gate, no conditioning variable exists anywhere in the pipeline.
- **Primary signal — the mega-alpha (§3).** Each formulaic alpha `f_p` maps history `H_{s−1}` to a cross-sectional signal `α_p_s ∈ R^N`; signals are cross-sectionally z-scored and combined by a **linear model** `α̂_s(F) = Σ_p α̃_p_s β̂_p`, with `β̂` fit by least squares on the training window with an ℓ1 penalty `α = 5×10⁻³` (Table 7).
- **Search state (§4.1) — the paper's first novelty.** The MDP state is augmented to `x_t = (z_t, F_t)`; because `F_t` is a set of mathematical expressions, a **frozen LLM (Qwen-Embedding-4B)** encodes a structured prompt `d(F_t)` (full template in Appendix B) into a last-layer hidden vector `e_t ∈ R^{d_e}` (`d_e = 2560`, Table 6); the token sequence goes through a 2-layer LSTM (`hidden 128`, `dropout 0.1`), both are projected by FFNs (`hidden 256`), combined by element-wise product, then a further FFN maps to a 128-d embedding fed to the MaskPPO policy and value heads. The LLM is frozen — no gradient passes through it — so it functions as a **semantic encoder of what the pool already covers and what blind spots remain**, not as a factor generator.
- **Search objective (§4.2) — the second novelty.** The scalar reward is replaced by `r_t = (IC_t, RRE_t, PFS_t, DH_t)^T`: `IC` = mean daily cross-sectional Pearson correlation of the updated mega-alpha with future returns over `D_train`; `RRE` (Relative Rank Entropy) = `(1/|D_train|)(1 + Σ_{s≥2} 1/(1 + D_KL(p_s ‖ p_{s−1})))` on normalised cross-sectional rank vectors — higher means more stable rankings over time; `PFS` (perturbation fidelity score) = mean Spearman correlation between the mega-alpha and a perturbed copy `(1+ε_s) ⊙ α̂_s`, with `ε_s` drawn half from Gaussian and half from Student-t3 noise **rescaled to the empirical cross-sectional variance of stock returns**; `DH` (diversity entropy) = normalised Shannon entropy of the eigenvalues of the pool's signal covariance matrix. The four objectives are scalarised by the **MAP (Multi-Human-Value Alignment Palette)** dual: `r*_t = λ(c)^T r_t`, with `λ(c)` the maximiser of `−log E_π[exp(λ^T r_t)] + λ^T c`, re-solved online on replay-buffer reward vectors (solver lr 0.01, 500 steps, 1 retry) from a **value palette** `c = (c_IC, 0.95, 0.93, 0.80)` where `c_IC = 0.090 / 0.085 / 0.250` for CSI300 / CSI800 / Market (Table 7).
- **Portfolio layer (Appendix G) — risk/exit in the source's own terms.** Long-only top-50 by mega-alpha at each monthly rebalance, rotating **at most 5** eligible names, skipping stocks under price-limit constraints, executing **at the close**, with a flat 15 bp-per-side cost and a 5 CNY minimum fee.

Reported reading (§5.1, §6): conditioning on the pool "may be especially useful in complex markets", and the multi-objective reward "discovers alpha pools that are not only more predictive, but also more stable, robust, and diverse"; the LLM "serves only as a frozen semantic encoder … rather than a generator".

### Research interpretation

Falsifiable form: **an RL alpha-search agent that is told what the current pool already contains (via a frozen LLM embedding) and that is rewarded on four pool-quality axes rather than IC alone will produce a formulaic alpha pool with higher out-of-sample cross-sectional IC and higher net portfolio Sharpe than single-objective, pool-unaware search on the same grammar, universe and split.** Component roles, stated so ablation can be attempted:

```text
Regime:        none (source has no regime layer)
Primary signal: linear mega-alpha over an RL-discovered pool of price-volume formulaic alphas
Search/design:  frozen-LLM pool-as-state (stationarises the MDP) + 4-objective MAP scalarisation
Risk/exit:      none beyond the portfolio rule — monthly top-50 long-only, rotate <=5 names, close execution
```

Two boundaries I mark rather than resolve. First, **the source identifies no economic premium**: the alpha content is inherited from whatever cross-sectional price-volume anomalies the grammar can express, and the paper's contribution is the discovery machine — so the mechanism to falsify is *search quality*, not a behavioural or structural market effect. Second, the paper never reports which formulas were finally selected, so "the strategy" is a procedure plus a data window, not a printed rule set; any claim that the discovered pool encodes a specific premium (momentum, reversal, liquidity) would be `research-proposed`.

## Signal

**Formation timestamp.** Each alpha maps `H_{s−1}` (historical market data) to a signal for day `s`, with a **20-day forward return** target ("leading days 20", Table 7) and an in-sample IC evaluated over `D_train` = 2013/07/01–2023/06/30. The portfolio is formed "at each rebalance date" and **trades at the close** (Appendix G). Whether the mega-alpha used for a close-of-day-`s` trade is computed from data through `s−1`, through `s`'s own close, or from an earlier snapshot, and the timezone/session convention, are **not stated in source** → `data gap` (this is the classic close-signal/close-fill ambiguity).

**Lookback.** Time-series operators use `d ∈ {10, 20, 30, 40, 50}` days (Table 5); maximum expression length `L_max = 15` tokens; the linear combiner is fitted on the 10-year training window; the RL training horizon is `250,000` steps (`P = 10`) or `300,000` steps (`P = 20`) with `max steps / tolerance 10,000 / 500`, `metrics window 252 / step 5` (Table 7). Warm-up length for indicators and the treatment of the first 15-token expressions → `underspecified`.

**Grammar / parameters actually published (Table 5, Table 7, Appendix E).** Features: `Open, High, Low, Close, Vwap, Volume`; constants `{-30, -10, -5, -2, -1, -0.5, -0.01, 0.01, 0.5, 1, 2, 5, 10, 30}`; time deltas `{10,20,30,40,50}`. Time-series operators: `Ref, TsRank, Mean, Med, Sum, Std, Var, Max, Min, WMA, EMA, Cov, Corr`. Cross-sectional operators: `Sign, Abs, Log, Rank, Add, Sub, Mul, Div, Greater, Less`. Special tokens `BEG`/`SEP`, invalid-action masking, deterministic transitions, `γ = 1`, incomplete formula reward `0`, invalid formula reward `−1`, pool size `P ∈ {10, 20}` **tuned on the validation set**, "keep at most `P` alphas according to their fitted contributions" (the pruning statistic is not defined → `underspecified`). Networks: 2-layer LSTM hidden 128 dropout 0.1; `FFN_e`/`FFN_h` hidden 256; `FFN_u` → 128-d; `d_e = 1536 / 2560 / 3584 / 5120 / 5120` for DeepSeek-1.5B / Qwen-Embedding-4B / DeepSeek-7B / DeepSeek-14B / DeepSeek-32B (Table 6); optimiser Adam, lr `5×10⁻⁴`, batch 128. Palette: `c_IC = 0.090 / 0.085 / 0.250` (CSI300 / CSI800 / Market), `c_RRE = 0.95`, `c_PFS = 0.93`, `c_DH = 0.80`; PFS noise is Gaussian or Student-t3 with equal probability, rescaled to empirical cross-sectional return variance.

**Long entry (source-reported, Appendix G).** At each monthly rebalance, **long-only top 50** names ranked by the mega-alpha; **partial rotation: trade up to 5 eligible stocks**; exclude stocks "subject to price-limit constraints"; execute at the close; initial capital **100 million CNY**; benchmark **Shanghai Composite Index (SH.000001)**; backtest run on the **full market universe** with monthly rebalancing consistent with the 20-day target.

**Short entry.** **None.** No short leg, no hedge, no borrow anywhere in the pinned text (`shorting`, `borrow`, `short sale` = 0 occurrences; the single `short` hit is the phrase "short-term sentiment" inside the Appendix B prompt).

**Exit / holding period.** Exit is implicit in the monthly reset; no stop-loss, take-profit or time stop is stated; actual holdings duration and turnover are never printed → `data gap`.

**Not printed (blocking exact reconstruction):** the discovered alpha expressions themselves (Figure 3 shows one illustrative alpha and its RPN; Appendix B's ten expressions are labelled a *typical structure* example, not the fitted pool), the fitted weights `β̂`, the value-palette selection rule, how `c_IC` was chosen per universe, the LLM pooling/layer used to obtain `e_t`, any decoding/inference settings of the encoder, and the pool-pruning statistic. **The search procedure is specified in detail; the tradable output is not published in the paper.**

## Required data

- **Instrument / universe:** Chinese A-shares in three nested universes — **CSI300** (largest 300), **CSI800** (largest 800), **Market** (full market universe) — plus an **S&P 500** replication (Appendix J) that "change[s] only the stock universe and retain[s] the other experimental settings". Cash equities only; no futures, perpetuals, options or crypto.
- **Sample split (§5):** training **2013/07/01–2023/06/30**, validation **2023/07/01–2024/06/30**, test **2024/07/01–2025/06/30**; target = **20-day future stock return**.
- **Fields:** daily `Open, High, Low, Close, Vwap, Volume` per stock; price-limit flags (used to exclude names at rebalance); cross-sectional future returns; benchmark index `SH.000001` levels; index membership for the three A-share universes and for S&P 500.
- **Point-in-time:** **no** statement of vendor, membership timing, reconstitution, survivorship, delisting, corporate-action or price-adjustment handling — `vendor`, `tushare`, `joinquant`, `survivorship`, `point-in-time`, `delist`, `suspension` all return **0** occurrences in the pinned text → `data gap`. The paper says only "Chinese A-share stock market data" (§5); the word `Qlib` appears as the source of the Alpha158 baseline and in the GitHub repository description, **not** as a declared data provider for the experiment.
- **Model dependency:** frozen **Qwen-Embedding-4B** weights (encoder); baselines AlphaAgent and R&D-Agent-Quant use **DeepSeek-V3.2 (671B)** as generator (§5); scaling study uses DeepSeek-1.5B/7B/14B/32B plus Qwen-Embedding-4B (Table 3, see `contradictions`).
- **Not used:** order book, trades/aggressor side, open interest, funding, mark/index/basis, borrow, options surface, news, fundamentals, on-chain fields — none appear in the source (all alphas are price/volume formulas).

## Execution assumptions

**Source-reported (Appendix G, §5).**

- Signal at rebalance date → **execute at the close**, monthly rebalance, long-only top 50, rotate **up to 5** names, skip price-limit-constrained names.
- **Costs: `15 basis points per side`, minimum fee `5 CNY`** — the single cost statement in the paper.
- Capital 100 million CNY; benchmark `SH.000001`; IC-level results are **gross of costs** (costs are only introduced in Appendix G's portfolio).
- Statistical machinery: 5 random seeds per stochastic experiment; **paired t-tests across 5 matched seeds** (Appendix F, Table 8) reported at a **10% significance level**, p-values as percentages; no HAC/block correction, no bootstrap, no multiplicity adjustment.

**Word census of the pinned text (Methods-level read of §3, §4, §5 and Appendices D–K).** `transaction cost` **1** occurrence and the only fee statement is the same Appendix G sentence (`minimum fee of 5 CNY`; other leading-anchor `fee` hits are the verb `feed`), `backtest` **6**, `sharpe` **3**, `information ratio` **3**, `drawdown` **3**, `rebalance` **2** + `rebalancing` **1**, `price-limit` **1**; while `slippage`, `commission`, `bid-ask`, `spread`, `latency`, `maker`, `taker`, `order type`, `participation`, `turnover`, `capacity`, `leverage`, `margin`, `funding`, `borrow`, `walk-forward`, `holdout`, `placebo`, `benjamini`, `fdr`, `multiple test`, `deflated`, `risk-free`, `cagr`, `beta`, `survivorship`, `point-in-time`, `look-ahead`, `adv` (as average daily volume), `crypto`, `bitcoin`, `perpetual` all return **0** modelled occurrences. `impact` occurs 3 times, all as prose ("the impact of non-stationarity", "the impact of MAP", Appendix H title) — **no market-impact model exists**; `fill` occurs once as the verb "filling" (prompt text); `liquidity` (2) and `data source` (3) occur only inside the Appendix B prompt template; `wind` (2) and `adv` (3) are the words *window* and *advantage*. So **order type, fill model, signal-to-order delay, latency, participation, turnover, capacity, leverage/margin, borrow, spread and market impact all stay `data gap` — never zero.**

**Research-proposed (not from the source) if this record is ever executed:** a per-side cost ladder of 0 / 2.5 / 5 / 10 / 15 / 20 / 50 bp, explicit turnover reporting, a 20%-of-20-day-ADV participation cap, a quoted-spread/fill test, and a next-session-open execution variant — each a `research-proposed` operationalization.

## Evidence

### Source-reported

All figures below are third-party claims from the pinned v1 PDF. ICs are **gross of costs**; the Table 2 portfolio is **net of the 15 bp-per-side schedule with the 5 CNY minimum fee** (Appendix G); ICs and their standard deviations are printed in percent; the portfolio test window is 2024/07/01–2025/06/30 unless stated otherwise. **None of these numbers has been independently reproduced.**

**Table 1 — out-of-sample IC (Mean, Std in parentheses; Alpha158 has no repeated runs so Std is blank):**

| Method | CSI300 | CSI800 | Market |
|---|---|---|---|
| Alpha158 | 2.99% (–) | 4.77% (–) | 4.04% (–) |
| MLP | 1.51% (2.33%) | 4.63% (0.90%) | 7.00% (0.18%) |
| GP | 1.09% (0.82%) | 2.74% (1.40%) | 7.52% (1.53%) |
| AlphaAgent | 0.51% (0.34%) | 0.48% (0.46%) | 1.10% (0.59%) |
| R&D-Agent-Quant | 2.39% (0.96%) | 2.45% (0.73%) | 1.48% (0.91%) |
| AlphaGen | 3.69% (0.66%) | 5.07% (0.63%) | 8.44% (1.09%) |
| AlphaQCM | 0.50% (0.95%) | 4.79% (0.34%) | 9.16% (4.22%) |
| AlphaForge | 2.03% (0.65%) | 4.17% (1.96%) | 5.37% (1.81%) |
| **AlphaPareto** | **3.92% (0.46%)** | **5.70% (0.87%)** | **10.10% (1.01%)** |

§5.1 text: highest IC on all three datasets; second-best values `3.69% / 5.07% / 9.16%`; gains over the strongest RL baseline `0.23% / 0.63% / 0.94%` (percentage points).

**Table 2 — out-of-sample monthly portfolio (AV annualised return, MDD maximum drawdown, IR information ratio, SR Sharpe ratio):**

| Model | AV | MDD | IR | SR |
|---|---|---|---|---|
| Alpha158 | 33.17% | −18.71% | 1.08 | 1.34 |
| MLP | 47.09% | −25.21% | 1.57 | 1.58 |
| GP | 24.49% | −13.29% | 0.77 | 1.18 |
| AlphaGen | 40.03% | −15.91% | 1.65 | 1.61 |
| AlphaAgent | 35.07% | −29.94% | 0.71 | 0.89 |
| R&D-Agent-Quant | 37.30% | −30.18% | 0.76 | 0.96 |
| AlphaQCM | 19.45% | −19.74% | 0.20 | 1.21 |
| **AlphaPareto** | **58.92%** | **−18.12%** | **2.62** | **2.59** |

§5.1 text: AlphaPareto has the highest AV/IR/SR; MDD "slightly worse than those of GP and AlphaGen but better than remaining methods". Figure 4 shows cumulative returns visually only — **no benchmark row is printed for SH.000001**.

**Table 3 — out-of-sample IC across encoder sizes (CSI300 / CSI800 / Market):** DeepSeek-1.5B `2.65% (0.99) / 5.39% (0.44) / 9.33% (0.92)`; **Qwen-Embedding-4B `3.92% (0.46) / 5.70% (0.87) / 10.10% (1.01)`**; DeepSeek-7B `3.38% (0.56) / 5.50% (1.23) / 9.50% (0.56)`; DeepSeek-14B `3.71% (1.73) / 5.59% (0.46) / 9.74% (0.64)`; DeepSeek-32B `3.26% (1.43) / 4.76% (0.52) / 9.88% (1.13)` — pattern described as "clearly non-monotonic".

**Table 4 — ablation (LLM pool-state / MAP-MORL):** none (≡ AlphaGen) `3.69% (0.66) / 5.07% (0.63) / 8.44% (1.09)`; LLM only `2.37% (0.68) / 5.04% (0.42) / 9.68% (0.83)`; MORL only `3.99% (1.27) / 5.54% (1.03) / 9.63% (0.80)`; both `3.92% (0.46) / 5.70% (0.87) / 10.10% (1.01)`. §5.3 text: full model is best on CSI800 and Market; on CSI300 it loses `0.07`pp of mean but cuts std by `0.81`pp versus MORL-only.

**Table 8 — paired t-tests across 5 matched seeds (t, one-sided p in parentheses):** Alpha158 `4.55 (0.52%) / 2.40 (3.73%) / 13.39 (0.01%)`; MLP `2.73 (2.62%) / 7.05 (0.11%) / 8.00 (0.07%)`; GP `16.11 (0.00%) / 9.58 (0.03%) / 10.87 (0.02%)`; AlphaAgent `55.88 (0.00%) / 25.41 (0.00%) / 44.84 (0.00%)`; R&D-Agent-Quant `6.59 (0.14%) / 34.67 (0.00%) / 116.93 (0.00%)`; AlphaGen `1.69 (8.34%) / 5.08 (0.35%) / 14.96 (0.01%)`; AlphaQCM `14.58 (0.01%) / 3.67 (1.07%) / 0.65 (27.60%)`; AlphaForge `20.95 (0.00%) / 2.74 (2.59%) / 9.81 (0.03%)`. §5.1/F text: significant at the 10% level against every baseline on CSI300 and CSI800, and against every baseline on Market **except AlphaQCM** (`p = 27.60%`).

**Appendix H (equal-weight scalarisation control, CSI800):** fixed ¼-weight sum of the four rewards `4.92% (0.52%)` versus MAP `5.70% (0.87%)`.
**Appendix I (random-noise control, CSI800):** matched pool-independent noise `4.22% (1.62%)`; no pool representation `5.54% (1.03%)`; LLM embedding `5.70% (0.87%)`.
**Table 10 — S&P 500 out-of-sample IC:** Alpha158 `3.92% (–)`; MLP `5.43% (0.31%)`; AlphaAgent `−0.01% (0.56%)`; R&D-Agent-Quant `1.29% (0.49%)`; AlphaGen `7.03% (0.30%)`; AlphaQCM `7.18% (0.84%)`; AlphaForge `1.33% (2.97%)`; **AlphaPareto `7.65% (0.13%)`**; §J text: `+0.47`pp over AlphaQCM with std falling `0.84% → 0.13%`.
**Table 11 — compute:** 66 Intel Xeon Platinum 8470Q vCPUs, 330 GB RAM, one RTX PRO 6000 (96 GB), 1 GPU + 64 CPU workers per run; main comparison `195 runs × 8h = 1560h`, scaling study `150 × 8h = 1200h`, ablation `360 × 7h = 2520h`, plus "approximately 4 additional GPU-hours" of exploratory runs.
**Figure 2 (text description):** highest perturbation robustness (PFS) on all three universes, second-highest diversity (DH) on CSI300/CSI800, third-or-fourth temporal stability (RRE) on CSI300/CSI800, "relatively moderate" DH and RRE on Market.

### Independently reproduced

not independently reproduced. No search pipeline was run, no A-share or S&P data was pulled, no baseline was re-run and no metric was recomputed from returns for this record. The only quantities computed here are (a) file/page/byte/SHA-256 checksums of the pinned artefacts and the GitHub API metadata, (b) a word census of the pinned text, and (c) arithmetic-only consistency checks of printed cells, executed by `check_alphapareto.py` (exit 0, **0 FAIL**): the Appendix F p-value column **reproduces exactly for all 24 comparisons** when recomputed as a *one-sided Student-t right tail with df = 4* (five matched seeds) inside the interval implied by each t rounded to two decimals — e.g. `t = 4.55 → 0.521%` vs printed `0.52%`, `t = 1.69 → 8.315%` vs printed `8.34%`, `t = 0.65 → 27.557%` vs printed `27.60%`, `t = 2.73 → 2.622%` vs printed `2.62%`, `t = 3.67 → 1.070%` vs printed `1.07%`; §5.1 IC increments `3.92−3.69 = 0.23`, `5.70−5.07 = 0.63`, `10.10−9.16 = 0.94`; §5.3 ablation deltas `3.99−3.92 = 0.07` and `1.27−0.46 = 0.81`; §J `7.65−7.18 = 0.47`; Table 11 `195×8 = 1560`, `150×8 = 1200`, `360×7 = 2520`; Table 1 column winners (AlphaPareto first, AlphaGen/AlphaQCM second in every column); Table 2 ranking (AlphaPareto max AV/IR/SR, with GP and AlphaGen showing smaller drawdowns); and Table 7 palette targets versus achieved out-of-sample IC (`0.090 / 0.085 / 0.250` versus `0.0392 / 0.0570 / 0.1010` — every target sits **above** the achieved value). Two research-computed diagnostics follow from the same script: the paired design implies a cross-seed correlation of **+0.91 (AlphaGen, CSI300), +0.99 (AlphaAgent, CSI300), +0.98 (R&D, CSI300), +0.98 (AlphaAgent, Market), +0.98 (AlphaQCM, Market)** between matched seed pairs, i.e. the very small p-values are produced by near-perfect pairing on only four degrees of freedom; and the exploratory compute line ("approximately 4 additional GPU-hours") is smaller than a single reported run (7–8 GPU-hours) against a reported total of 5,280 GPU-hours.

### Negative evidence

1. **One out-of-sample window for everything.** All Table 1/2/3/4/8 numbers come from 2024/07/01–2025/06/30; `walk-forward` and `holdout` each appear **0** times; Appendix J changes the *universe* but "retain[s] the other experimental settings", so it shares the same window. No rolling origin, no second period, no pre-declared forward test.
2. **No multiplicity control whatsoever.** `benjamini`, `fdr`, `multiple test`, `deflated`, `placebo` each appear **0** times, yet Table 8 alone prints 24 paired tests (8 baselines × 3 universes), alongside 15 scaling cells, 12 ablation cells, one equal-weight control, one noise control and a separate S&P 500 table — and significance is claimed at a permissive **10% level**.
3. **Five seeds, four degrees of freedom.** Every headline comparison rests on `n = 5`; the implied cross-seed correlation of 0.91–0.99 (research-computed) shows the p-values are driven by pairing, not by sample size — one rerun seed can flip the marginal CSI300 result.
4. **The Market win is not significant against the strongest non-LLM competitor.** Table 8: AlphaPareto vs AlphaQCM on Market `t = 0.65, p = 27.60%`, explicitly reported as not significant by the source.
5. **The CSI300 win over the best prior RL method is marginal.** AlphaPareto vs AlphaGen on CSI300 `t = 1.69, p = 8.34%` (one-sided) for a `0.23`pp gap.
6. **The full model is not uniformly best.** Table 4: LLM-only *hurts* on CSI300 (`2.37%` versus the `3.69%` no-component baseline, −1.32pp) and the full model (`3.92%`) is **below** MORL-only (`3.99%`) on CSI300; §5.3 attributes this to "domain noise from the LLM".
7. **Palette targets are unreachable as printed.** Value-palette `c_IC` minimum levels (0.090/0.085/0.250) exceed the achieved out-of-sample ICs (0.0392/0.0570/0.1010) and **in-sample ICs are never printed**, so the stated "desired minimum level for each objective" cannot be checked; how `c_IC` was set per universe is unstated.
8. **Encoder selection may be test-informed.** §5.2 and Table 3 compare five encoders *by out-of-sample IC* and name Qwen-Embedding-4B the best; the paper never says the encoder was chosen on the validation set → possible test-set model selection, `data gap`.
9. **Unreconciled scaling-study description** (see `contradictions`): DeepSeek-R1 family stated in §5.2 versus a table that includes Qwen-Embedding-4B, which is also the main configuration.
10. **Underspecified encoder plumbing.** "Last-layer hidden representation of the LLM" (Eq. 3) is not defined for the DeepSeek-R1 reasoning family or for an embedding-specialised model (no pooling rule, no layer index) → results are not reconstructible from the text alone.
11. **Flat single-line cost model.** 15 bp/side + 5 CNY minimum fee is the entire cost treatment; `slippage`, `commission`, `bid-ask`, `spread`, `market impact`, `latency`, `order type`, `participation` = **0**; no fill model, no delay model, and close-signal/close-fill is not reconciled.
12. **Turnover never printed.** `turnover` = **0** occurrences although the rule rotates up to 5 of 50 names monthly; without turnover the net AV/SR cannot be stressed and the flat 15 bp assumption cannot be checked.
13. **No capacity or liquidity analysis.** `capacity`, `participation` = 0, no ADV reference, no position limits, 100 million CNY over 50 names with no market-impact model.
14. **No exposure decomposition.** `beta` = 0 occurrences; Table 2 has no benchmark row (Figure 4 is visual), no factor attribution, and neither the Sharpe nor the information ratio definitions (risk-free series, annualisation, benchmark for IR) are stated → `data gap`.
15. **Data provenance entirely absent.** No vendor, no membership timing, no survivorship/delisting/adjustment disclosure (`vendor`, `survivorship`, `point-in-time`, `delist`, `suspension` = 0), so the CSI300/CSI800/Market/S&P panels cannot be rebuilt as of any date from the paper.
16. **The tradable output is not published.** Discovered expressions, weights and the final pool are never printed; the illustrative Figure 3 and the Appendix B example are labelled examples, so independent reconstruction requires the repository — which has a **single initial commit** and **no detected license** (`license: null`), leaving usage and redistribution rights `data gap`.
17. **Baselines were re-run and modified by the authors.** Appendix D: AlphaAgent's prompt was changed to 10 candidates × 5 iterations; R&D-Agent-Quant's factor count was fixed to 10, outer loops raised 5 → 10 and its LaTeX output replaced; all other settings follow "original repository defaults" — no third-party or published baseline numbers are used, and AlphaAgent/R&D are reported as very weak (CSI300 `0.51%` / `2.39%`).
18. **Search multiplicity is unaccounted for.** Up to 300,000 grammar-level steps over 15-token expressions plus pool-size tuning on validation, with no selection-adjusted (deflated) evaluation of the resulting pool.
19. **Compute and cost accounting do not reconcile.** 5,280 reported GPU-hours (Table 11, arithmetic verified) plus "approximately 4 additional GPU-hours" of exploratory runs — smaller than one reported run; LLM inference/token cost for the encoder (and for the DeepSeek-V3.2 baselines) is never reported.
20. **Two different objects are compared.** IC (gross, 20-day horizon, daily cross-section) and portfolio SR/AV (net, monthly, top-50) are reported side by side with no bridge — no rank-stability of the top-50, no turnover, no decay analysis between them.
21. **Status and maturity.** arXiv v1 only, 19 pages, accepted but not yet in proceedings, single test window, single portfolio universe (full A-share market), zero crypto content (`crypto`, `bitcoin`, `perpetual` = 0).
22. **Author-acknowledged limitations (§6):** "performance may depend on the prompt template, which has not been systematically studied" and "we use a linear mega-alpha combiner, which may exclude useful nonlinear structures".

## Falsification plan

Every threshold below is a `research-defined falsification threshold` (Scout-chosen, not the source's) with an explicit action on failure. **Global rule: no retuning.** The grammar, `L_max = 15`, `P ∈ {10, 20}`, the palette `c`, the splits, the top-50/rotate-5 rule, the 15 bp schedule, the encoder and the benchmark are frozen as printed; a failed gate may not be rescued by re-optimising any of them — failure changes the record's status, not the configuration.

- **F1 — Printed-value reproduction.** Re-run the released code at commit `bdc92dfa9aa8a3849459c9a3568bd38a15af56d8` on the same splits. Fail if CSI300/CSI800/Market IC miss `3.92 / 5.70 / 10.10 %` by more than `±0.25`pp each, if the S&P 500 IC misses `7.65%` by more than `±0.25`pp, or if portfolio `AV` misses `58.92%` by more than `±3.0`pp / `SR` misses `2.59` by more than `±0.15`. Action: mark every headline `unverified`; record stays `research-only` permanently.
- **F2 — Data and point-in-time gate.** Rebuild all four universes from a named vendor with as-of membership, adjustment and delisting rules. Fail if membership is ex-post, if delisted names are dropped, or if no vendor can be identified. Action: no implementation attempt; permanent `research-only`.
- **F3 — Signal-timing gate.** Recompute the mega-alpha strictly from information available before the execution timestamp (signal from data through `t−1`, trade at close `t`, or signal at close `t`, trade at next open). Fail if out-of-sample IC falls below **half** the printed value (CSI300 `< 1.96%`, Market `< 5.05%`). Action: reject the tradable reading; retain only the search-method claim.
- **F4 — Cost ladder and turnover gate (`research-proposed`).** Report monthly turnover, then reprice at 0 / 2.5 / 5 / 10 / 15 / 20 / 50 bp per side plus the 5 CNY minimum fee. Fail if net Sharpe at the source's own 15 bp falls below `1.00`, or if reported monthly turnover exceeds `40%` of book value. Action: reclassify the 58.92%/2.59 pair as cost-fragile.
- **F5 — Capacity gate (`research-proposed`).** Cap participation at 20% of 20-day ADV per name. Fail if Sharpe degrades by more than `0.30` versus the unconstrained run. Action: mark capacity `unproven` and bound position size explicitly.
- **F6 — Family-wide multiplicity gate.** Apply Benjamini–Hochberg at `q < 0.10` over the full reported family (9 methods × 3 universes + 5 encoders + 4 ablations + 1 cross-market table = 47 IC comparisons), plus a deflated-Sharpe check whose trial count equals the number of configurations actually inspected (including the 300,000-step search). Fail if the AlphaPareto-over-AlphaGen and AlphaPareto-over-AlphaQCM comparisons do not survive at `q < 0.10`. Action: significance reclassified as selection artefact.
- **F7 — Seed-stability gate.** Ten matched seeds per configuration. Fail if AlphaPareto fails to beat AlphaGen on CSI300 in at least `8 of 10` seeds, or if `std(IC) > 25%` of the mean on any universe. Action: downgrade to `falsified-robustness`.
- **F8 — Component gate.** The full model must beat both ablations on **all three** universes. **Currently failing as printed** (CSI300 full `3.92%` < MORL-only `3.99%`). Action: until a frozen rerun reverses it, restrict the claim to CSI800 and Market and record the LLM-component benefit as universe-dependent.
- **F9 — Prompt/palette robustness gate (`research-proposed`).** Three alternative pool-encoding prompts and palette entries perturbed by ±20%. Fail if any universe's IC moves more than `20%` in relative terms. Action: attribute the result to prompt/palette tuning rather than to the mechanism (the source itself flags this limitation).
- **F10 — Encoder-selection gate.** Select the encoder on the validation window only, then evaluate once on the test window. Fail if the validation-chosen encoder's test IC is below half the printed value (`CSI300 < 1.96%`) or if Qwen-Embedding-4B stops being best in a validation-only selection. Action: reclassify Table 3 as test-informed selection.
- **F11 — Execution-realism gate.** Keep the price-limit exclusion, add fill confirmation and a one-session delay for rotated names. Fail if net Sharpe drops by more than `0.30` versus the printed `2.59`. Action: reject the close-execution assumption.
- **F12 — Exposure/benchmark gate.** Report beta and factor-adjusted alpha versus `SH.000001` (and CSI300 for the CSI panels). Fail if benchmark-relative IR is `< 0.50` or if beta `> 0.90` explains the return. Action: attribute the AV to beta, not to the discovered pool.
- **F13 — Cross-market replication gate (`research-proposed`).** Frozen settings on (a) a non-Chinese developed-equity panel (e.g. STOXX 600) and (b) a liquid crypto cross-section. Fail if either panel's OOS IC `≤ 0`. Action: restrict the claim to large-cap A-shares; crypto portability stays `unproven`.
- **F14 — Frozen forward window.** Evaluate 2025/07/01 onward (the paper's test ends 2025/06/30) with everything frozen. Fail if forward IC `≤ 0` or forward Sharpe `≤ 0` over ≥ 12 months. Action: reject persistence; record as sample-bound.

## Crypto portability

**adapted.** The pinned text contains **0** occurrences of `crypto`, `bitcoin` or `perpetual`; every empirical claim is on Chinese A-shares and S&P 500 constituents. The *machinery* (RPN grammar over OHLCV/volume, RL search, four-objective pool reward, linear mega-alpha, top-N long-only portfolio) is instrument-agnostic, so this is a **ported hypothesis, not crypto empirical evidence**, and `adapted` does not mean demonstrated:

- **Universe and breadth:** a top-50 long-only book over a full national equity market has thousands of candidates; liquid token universes are far narrower and dominated by BTC/ETH beta, so a 20-day cross-sectional IC on 50 names is not comparable → `research-proposed` re-derivation needed.
- **Session structure:** time deltas `{10,20,30,40,50}` and the 20-day target assume exchange sessions; 24/7 candles, venue-specific day boundaries and timezone conventions are undefined in the source and matter more in crypto.
- **Rules that do not exist in crypto:** the A-share **price-limit exclusion** has no direct analogue (circuit-breakers/limit-up-down differ by venue), and ST/suspension handling — itself unstated — becomes token delisting and exchange listing churn, which is far more severe.
- **Costs/execution:** 15 bp/side plus a 5 CNY minimum fee is an A-share schedule; crypto taker/maker fees, real spreads, and per-venue impact are unmodelled, and the source has no spread, fill, latency or impact model at all.
- **Perpetuals/funding/shorting:** no funding, basis, borrow, margin or liquidation mechanics exist in the source, and the rule is long-only.
- **Point-in-time data:** the source's complete silence on vendor/membership/adjustment would be even more damaging in crypto, where survivorship and re-listing effects are larger.

A port would be a new experiment; `crypto portability: adapted` is not authorization to trade.

## Limitations

- `underspecified`: pool-pruning statistic, value-palette selection rule, encoder pooling/layer, prompt sensitivity (author-acknowledged), signal-to-order timing and session convention, Sharpe/IR/AV definitions and risk-free series, indicator warm-up, exit precedence, actual turnover, benchmark row for Table 2, in-sample IC levels, and the DeepSeek-R1-versus-Qwen scaling-study scope.
- `data gap`: data vendor, as-of membership, survivorship, delisting and adjustment rules, order type, fill model, latency, participation, capacity, leverage/margin, borrow, spread, market impact, LLM inference/token cost, ORCID/funding/COI/acknowledgments, repository contents, and repository license (public-use rights).
- `not independently reproduced`: every performance, IC and significance number in this record.
- `unproven`: that the *multi-objective + pool-state design* (rather than the single test window, the linear combiner, the top-50 rule or search multiplicity) produces the reported edge — there is no second window, no multiplicity control, no encoder-selection protocol and no prompt robustness test.
- Disclosed asymmetries: IC is gross while the portfolio is net at 15 bp; the full model is best only on CSI800/Market; the Market advantage over AlphaQCM is not significant; Alpha158 and GP show smaller drawdowns than AlphaPareto.
- One unreconciled printed statement (`contested: true`, see `contradictions`): the §5.2 DeepSeek-R1 scaling description against Table 3/Table 6/§5.
- Peer-review status: NeurIPS 2026 main-track acceptance stated on the landing, version of record not yet published at capture; arXiv v1 only, single test window, zero crypto evidence.

## Implementation status

`implementation_status: not-implemented`. Nothing from this record has been implemented in our research stack: no AlphaPareto search run, no A-share or S&P data pull, no Qlib backtest, no candidate-pool entry, no Paper / Testnet / Live activity, and no write to any downstream system. The linked GitHub repository was **not** cloned or executed. This artifact is a normalized research capture only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this file in the staging repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered `/results/_handoff/candidates.json`; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. Those stages remain separate and gated.

## Related Wiki records

Verified by `kb_search` on 2026-09-29 (no page was fabricated; each linked path appeared in a returned result set, and queries were kept to what actually exists):

- `[[quant/alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05]]` — grammar-guided MCTS/Tree-LSTM formulaic alpha discovery; adjacent search-procedure family, different search machine and different objective (no multi-objective pool reward).
- `[[quant/alpharjm-reward-jump-memory-sde-critic-symbolic-alpha-2026-09-11]]` — reward-jump memory with an SDE critic for symbolic alpha; same scalar-reward lineage that AlphaPareto argues against, different source.
- `[[quant/alphag-opd-reliability-gated-sibling-counterfactuals-symbolic-alpha-2026-09-05]]` — reliability-gated on-policy distillation for symbolic alpha factors; distillation mechanism, no pool-as-state.
- `[[quant/goant-quality-diversity-multi-agent-microstructure-alpha-discovery-2026-09-12]]` — quality-diversity multi-agent search over microstructure data; different input data dependency and different search paradigm.

Adjacent repository records (file paths, **not** verified Wiki pages): `alphaforge-generative-formulaic-alpha-dynamic-factor-timing-2026-09-17.md` (AlphaForge, a baseline in Table 1), `alpha-foundry-gp-gflownet-formulaic-alpha-mining-crypto-perps-2026-09-19.md` (crypto-perp GP + GFlowNet search), `mufasa-self-evolving-multi-agent-symbolic-valuation-discovery-arxiv-2609.32746-2026-09-29.md`, `adaptive-alpha-weighting-ppo-llm-generated-alphas-2026-09-05.md`, `favor-hypothesis-grounded-agentic-factor-validation-topk-portfolio-2026-09-24.md`, `autoscientist-quant-budgeted-self-evolving-search-cross-sectional-top50-2026-09-26.md`.

## Sources

1. Yingbo Zhao, Zeyu Yang, Zhoufan Zhu. *"AlphaPareto: Formulaic Alpha Discovery with LLM-Guided Multi-Objective Reinforcement Learning."* arXiv:2609.34188v1 [stat.ML], submitted Mon, 28 Sep 2026 03:03:41 UTC (landing prints `(2,914 KB)`). Landing page: https://arxiv.org/abs/2609.34188 (retrieved 2026-09-29; Comments `Accepted by Neurips 2026 main track`; Journal-reference field empty; Subjects `Machine Learning (stat.ML) ; Artificial Intelligence (cs.AI) ; Machine Learning (cs.LG)`; one version only).
2. Pinned full text: https://arxiv.org/pdf/2609.34188v1 — 19 pages, 2,981,862 bytes, SHA-256 `fb160d025d64f3f2b2fe36effeb3ef6303cb9aa91468b6bb45ec1aa2475d98cd`; every table, figure caption, hyperparameter and Appendix B/G/K statement cited above was read directly from this PDF on 2026-09-29 (pypdf 6.16.2, 59,357 characters).
3. arXiv full-text HTML for the same v1: https://arxiv.org/html/2609.34188v1 — 392,787 bytes, fetched 2026-09-29, **not** used as the reading copy.
4. arXiv DOI: https://doi.org/10.48550/arXiv.2609.34188 (the only DOI in the pinned metadata); licence `creativecommons.org/licenses/by-sa/4.0`.
5. Code repository named in §5: https://github.com/BiQiBaoWinner/AlphaPareto — HEAD commit `bdc92dfa9aa8a3849459c9a3568bd38a15af56d8` (branch `main`, `Initial commit`, 2026-09-28T02:24:46Z), repository metadata read via `https://api.github.com/repos/BiQiBaoWinner/AlphaPareto` and `.../commits?per_page=1` on 2026-09-29; **contents not inspected, no license detected**.
6. Baselines and methods as cited by the source (not fetched for this record): AlphaGen (Yu et al., KDD 2023), AlphaForge (Shi et al., AAAI 2025), AlphaQCM (Zhu & Zhu, ICML 2025), AlphaAgent (Tang et al., KDD 2025), R&D-Agent-Quant (Li et al., NeurIPS 2025 D&B), Alpha158/Qlib (Yang et al. 2020), Kakushadze *101 Formulaic Alphas* (arXiv:1601.00991), MAP (Wang et al., ICLR 2025), AlphaEval (arXiv:2508.13174), AlphaSAGE (ICLR 2026), AlphaBench (ICLR 2026).
