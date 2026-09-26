---
schema: strategy-research-record-v1
title: "AutoScientist-Quant: budget-conditioned self-evolving coding-agent search over alpha discovery, library filtering and model selection, deployed as a top-50 daily cross-sectional book (arXiv:2608.28632v2)"
created: 2026-09-26
updated: 2026-09-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - llm-agents
  - alpha-factor-mining
  - agentic-search
  - budgeted-search
  - cross-sectional
  - chinese-equities
  - us-equities
  - out-of-sample-protocol
status: research-only
confidence: medium
source_as_of: 2026-09-01
sources:
  - "https://arxiv.org/abs/2608.28632 (arXiv:2608.28632v2 [cs.AI primary; cs.CL, cs.LG cross-lists], submitted v1 Wed 5 Aug 2026 23:34:46 UTC (443 KB), last revised v2 Tue 1 Sep 2026 10:45:43 UTC (460 KB); abs page has NO Comments field (0 occurrences) and NO journal-ref field (0 occurrences); no peer-review statement anywhere; DataCite DOI 10.48550/arXiv.2608.28632 state=findable, resourceTypeGeneral=Preprint, version='2', registered 2026-09-01T03:37:59Z, updated 2026-09-02T03:13:13Z, dateInformation v1 Submitted 2026-08-05T23:34:46Z / v2 Submitted 2026-09-01T10:45:43Z -> no v3; rightsList 'arXiv.org perpetual, non-exclusive license' (http://arxiv.org/licenses/nonexclusive-distrib/1.0/); checked 2026-09-26)"
  - "https://arxiv.org/html/2608.28632v2 (pinned full text, 599812 bytes, SHA-256 bdec9a73b0f0e4dd688eece9f87f3f70e0dab416a81808af58e76cefd286b4ae, LaTeXML 0.7.6, downloaded 2026-09-26, converted to 99343 characters and read end to end: Abstract, Sections 1-5, References, Figure 1-2 captions, plus a cell-level re-extraction of all five result tables (Tables 1-5; the other five <table> elements are Equations 1-4 and one header row)"
  - "https://arxiv.org/pdf/2608.28632v2 (pinned PDF, 717678 bytes, SHA-256 76df8ee72ce287146eeb7a2cf43b185b461080d1f36ea2b2a97976b8a7944ae5, 13 pages, downloaded 2026-09-26, text-extracted to 53849 characters; pypdf metadata /Author 'Zongqian Li; Yaoyiran Li; Yaohui Guo; Ming Zhang; Nigel Collier; Eugene Ie', /Title matches the landing page, /arXivID 'https://arxiv.org/abs/2608.28632v2', /License arXiv non-exclusive; page footer 'arXiv:2608.28632v2 [cs.AI] 1 Sep 2026')"
  - "https://doi.org/10.48550/arXiv.2608.28632 (DataCite DOI record, JSON retrieved 2026-09-26, see source 1 for the fields used)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Source-internal contradiction, our reading of the pinned v2 read 2026-09-26: Section 1.3 (Contributions, fourth bullet) states 'The discovered alphas earn positive excess returns after costs on the held out test window', but Table 4 prints AutoScientist-Quant ARR of -0.1% on CSI 500 under the GLM backbone (the full three-stage method, same held-out test window). The positive-excess-return claim therefore holds for five of the six Table 4 settings and for all four Table 1 settings, not for all of them."
---

# AutoScientist-Quant: budget-conditioned self-evolving coding-agent search over alpha discovery, library filtering and model selection, deployed as a top-50 daily cross-sectional book (arXiv:2608.28632v2)

## Provenance

- **Paper**: Zongqian Li, Yaoyiran Li, Yaohui Guo, Ming Zhang, Nigel Collier, Eugene Ie, *AutoScientist-Quant: Self-Evolving Coding Agents for Automatic Research in Quantitative Investment*, `arXiv:2608.28632v2 [cs.AI]`.
- **Title block printed on the PDF** (author order and markers exactly as rendered): `Zongqian Li^{1,2}*, Yaoyiran Li^{1†}, Yaohui Guo^1, Ming Zhang^1, Nigel Collier^{2†}, Eugene Ie^1`, with `1 Google`, `2 University of Cambridge`. Footnotes on page 1: `*Work done during an internship at Google.` and `†Corresponding authors.` — so **Zongqian Li is the intern-marked first author, and Yaoyiran Li and Nigel Collier are the two corresponding authors** (no equal-contribution statement is printed).
- **E-mails printed on page 1**: `{zqli, yaoyiran, yaohuiguo, mingzhang, eugeneie}@google.com` and `{zl510, nhc30}@cam.ac.uk`. The per-address mapping inside each brace list is not stated beyond the ordering, and no affiliation is given per author beyond the superscript numerals (Google for Li/Li/Guo/Zhang/Ie, University of Cambridge for Collier, Li dual-affiliated).
- **Version / date**: `v1` Wed 5 Aug 2026 23:34:46 UTC (443 KB); `v2` Tue 1 Sep 2026 10:45:43 UTC (460 KB); `v2` is the latest version (arXiv API `id_list=2608.28632` returns `.../2608.28632v2`, `updated 2026-09-01T10:45:43Z`; DataCite `dateInformation` shows only v1 and v2) — **checked 2026-09-26**.
- **Subjects**: `cs.AI` primary; `cs.CL` and `cs.LG` cross-lists. No `q-fin.*` classification.
- **Comments / journal / review**: the abs page carries **no `Comments` field (0 occurrences)**, **no `Journal reference` field (0 occurrences)**, and no peer-review, acknowledgement, funding or conflict statement anywhere in the pinned text → **preprint only, unrefereed as captured**. The only `funding` string in the HTML is the arXiv footer "Major funding support from", and the only `GitHub` strings are arXiv page boilerplate ("Report GitHub Issue", "Submit without GitHub", "Submit in GitHub").
- **Licence**: `arXiv.org perpetual, non-exclusive license` (DataCite `rightsList`; `arxiv.org/licenses/nonexclusive-distrib/1.0/` on the abs page and in the PDF metadata) → this record cites and normalises short claims, printed numbers and short formula fragments only.
- **Code / data availability**: word scan of both pinned renderings for `github.com`, `code availability`, `data availability`, `upon request`, `publicly available`, `supplementary`, `acknowledgement`, `conflict of interest` → **0 relevant hits** → every availability field is `not stated in source`. No prompts, no configuration and no search logs are released either.
- **Source / data as-of**: daily data January 2015 – May 2026; the held-out test window is June 2023 – May 2026; arXiv `v2` dated **2026-09-01** (`source_as_of`); both renderings downloaded **2026-09-26**.
- **Pinned primary sources**: HTML `599812 bytes`, SHA-256 `bdec9a73b0f0e4dd688eece9f87f3f70e0dab416a81808af58e76cefd286b4ae`; PDF `717678 bytes`, SHA-256 `76df8ee72ce287146eeb7a2cf43b185b461080d1f36ea2b2a97976b8a7944ae5`, **13 pages**. Both read end to end on 2026-09-26, with the five result tables re-extracted cell by cell from the HTML and cross-checked against the PDF text (Table 1 and Table 5 rows agree in both renderings).
- **Pre-write source-identity dedup (whole repository, hidden trees included)**: ripgrep over all `*.md` / `*.csv` / `*.json` / `*.txt` including `.mimo-worktrees/`, `.agents/`, `.hermes/` and `coverage_manifest.csv` (1088787 bytes) for `2608.28632`, `10.48550/arXiv.2608.28632`, `AutoScientist`, `Self-Evolving Coding Agents`, `Zongqian`, `Yaoyiran`, `Yaohui Guo`, `Nigel Collier`, `Eugene Ie`, `Improve…Combine…Pivot`, `budgeted search problem` → **0 hits before the write** (case-insensitive), and no filename collision (`*autoscientist*` → 0 files).
- **Four-axis material-distinction statement vs the nearest existing repository records** (source identity differs in every pair):
  1. `alphadiverse-post-training-local-llm-agents-diverse-alpha-factor-mining-2026-09-26.md` — different source (arXiv 2609.29014v1); different mechanism (SFT + joint-GRPO log-det diversity post-training of local Planner/Realizer policies) and different signal construction (fixed 21-factor input bank plus mined factors) vs a **budget-conditioned controller with no post-training** that rewrites a natural-language alpha library at run time; different universe (AlphaDiverse adds a broad A-share universe, this paper uses six index universes only).
  2. `factorminer-self-evolving-experience-memory-formulaic-alpha-2026-09-20.md` — different source; different mechanism (offline experience memory mining formulaic alpha) and different horizon/regime dependency vs an online three-stage budgeted search whose selection stages are scored on a portfolio utility.
  3. `quantaalpha-institutional-price-volume-correlation-intraday-momentum-2026-09-05.md` — QuantaAlpha is a **baseline inside this paper** (Tables 1, 3, 4, 5), a different source identity with a different signal construction (original/mutated/crossover trajectory evolution) vs Improve/Combine/Pivot/Stop controller decisions over a shared parent pool.
  4. `llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04.md` — different source and different contribution class (a deflated/leakage-safe *evaluation* methodology rather than a search framework that reports strategy returns).
  5. `vst-verifiable-structured-transport-agentic-alpha-discovery-2026-09-12.md` — different source, different mechanism (agent-to-agent verifiable transport of alpha specifications) and different data dependency.
  6. `evolvetrade-self-evolving-llm-tool-use-policy-agent-15-us-bluechips-2026-09-26.md` — different source and different horizon/regime: EvolveTrade rewrites a **tool-use system prompt** for a 15-stock daily long-only book with CASH, while this paper never exposes a tool-use policy and operates a top-50 cross-sectional book on index universes with a separate library-filtering and model-selection stage.
  Source identity and mechanism differ in every pair; no reframing of a title was used to create this record.

## Economic mechanism

### Source-reported

Section 1.1 states the premise: alphas rank stocks by expected future return (Fama & French, 1992), and because markets are noisy and nonstationary "individual alphas are not effective once they become crowded, so new alphas need to be discovered at scale and renewed over time"; hand-written libraries (101 formulaic alphas, ALPHA158) "grow slowly", while RL-based symbolic search "optimizes backtest fit alone, producing complex expressions that overfit and do not last".

Section 1.2 names three defects of prior agentic pipelines, which the paper says it fixes:

1. **Static and incomplete automation** — directions, rounds, alpha counts and operations are fixed before the search starts, and automation stops at alpha generation, handing the library to one fixed predictor with no library selection and no model search.
2. **Train/test overlap at the search level** — "every accepted alpha is selected on test performance, so reported results have a selection effect toward the evaluation period" (citing Bailey et al., 2017; Harvey and Liu, 2015).
3. **Two lookahead bugs in the evaluation code reused from prior work** — information metrics were computed over the full sample rather than the declared test segment, and a failed segment filter scored models on their own training span; both were fixed and **all methods were re-evaluated on the corrected pipeline**.

The proposed mechanism (Sections 1.3, 2.1–2.4) is a **single decision core reused over three budgeted tree searches**:

- **Alpha discovery** — a trajectory `τ = ((h_1,F_1,e_1), …, (h_R,F_R,e_R))` whose round `r` proposes a market hypothesis, builds and executes the alpha set implementing it, and records backtest feedback; trajectory reward is the maximum feedback-window utility over its rounds. All trajectories from all directions live in one shared pool `P` ("working memory"). Each round the controller emits `(o_{d,r}, σ_{d,r}, n_{d,r}) = π_LLM(P_r, b_r)` with `o ∈ {Improve, Combine, Pivot, Stop}`; *Improve* rewrites one localized step of a parent by self-reflection, *Combine* recombines complementary parts of stored parents (retrieval strategy itself chosen at run time), *Pivot* opens a fresh direction when existing directions plateau, *Stop* closes a branch "whose expected gain no longer justifies its cost". Budget: `b_{r+1} = b_r − Σ_d n_{d,r}` and `π_LLM(· | b=0) = Stop`.
- **Alpha filtering** — the individually validated but jointly redundant library seeds a subset search over remove/add/swap edits, scored by `Z(S) = Σ_k (m_k(S) − μ_k)/ς_k`, standardising each of the eight metrics of Section 3.2 against its historic distribution across previously evaluated nodes, with all nodes rescored against the current pool at each comparison.
- **Model search** — the same controller over `Ω = ⋃_m {m} × Θ_m` with `M = {Linear, LightGBM, XGBoost, CatBoost, …}`; the winning library/configuration pair "is trained once on the training and validation windows … with early stopping on validation, and evaluated once on the held out window, which no stage of the search ever observes".

Evaluation design (Sections 2.1, 3.1): the feedback window `D_fb` supplies every backtest feedback signal; "the held out window enters exactly once, to produce the numbers in Section 4". Section 4.5 attributes the result to four behaviours: recovering from test dips the search cannot see, redundancy control ("the selected subset keeps 89 of 91 alphas yet single swaps move test ARR by more than a percentage point"), revision accumulating along histories, and evidence-based stopping rather than a fixed schedule.

### Research interpretation

Stated as a falsifiable hypothesis rather than a finding: **under a fixed search budget, a controller that conditions each explore/exploit decision on the remaining budget and jointly searches the alpha library and the predictor produces out-of-sample cross-sectional predictive content and net excess return above (a) agentic alpha-mining baselines and (b) static alpha libraries, when search feedback is provably disjoint from the evaluation window.** The tradable residue is much narrower than the framework claim: a daily cross-sectional score over an index universe, converted into a long-only top-50 book with at most five names replaced per day, measured against the universe's index (CSI) or in absolute terms (US).

Component roles (each role is a claim to be ablated, not a contribution we assume):

- *Regime / universe*: point-in-time index membership over six index universes; no explicit regime filter exists in the source.
- *Primary signal*: the agent-discovered alpha library, combined by the searched predictor into one daily cross-sectional score. **The library itself is never published**, so the signal is a described process, not a reconstructible rule.
- *Selection layer*: alpha filtering and model search, which Section 4.2 shows move portfolio outcomes while barely moving information metrics — i.e. this layer is tuned to portfolio utility on the feedback window, not to IC.
- *Risk / exit*: **absent from the source** — no stop, no sizing rule, no leverage, no cash rule and no exit other than daily re-formation of the top-50 book. F4 below is the ablation that decides whether the selection layer adds anything at all.

## Signal

**Source-reported construction (all from the pinned v2):**

- **Formation timestamp**: `not stated in source`. The paper never prints a timezone, session convention, clock or availability lag for "daily" data, and it never states when an order is placed relative to the score (`data gap` for signal-to-order timing).
- **Prediction target**: Section 2.1 defines a predictor `g` that maps library outputs to "forecasts `ŷ_t = g(F(X_≤t)) ∈ ℝ^N` of the future return", and Section 3.2 computes IC against "realized labels" within each daily cross-section. **The label horizon / return definition (next-day, next-open, n-day, excess or raw) is never printed** → `underspecified`.
- **Universe / data**: daily open, high, low, close and volume for **CSI 300, CSI 500, CSI 800, CSI 1000, S&P 500 and NASDAQ 100**, January 2015 – May 2026, "accessed through Qlib (Yang et al., 2020) with index members taken as of each historical date" (Section 3.1) — i.e. point-in-time membership, which the paper states explicitly. The specific Qlib dataset build, vendor and licence are `not stated in source`.
- **Splits (Section 3.1, contiguous)**: training January 2015 – January 2020; validation January 2020 – June 2021; **feedback window June 2021 – June 2023** (supplies all loop backtest feedback); **test window June 2023 – May 2026** (final evaluation only).
- **Alpha object (Section 2.1)**: an alpha is a function `f: X_≤t → ℝ^N` producing cross-sectional scores from `N × t × W` price/volume history; a library `F = {f_1, …, f_K}` combines scores into inputs; a fixed portfolio rule turns forecasts into daily positions; utility `U(F, g; D)` aggregates the eight metrics of Section 3.2.
- **Search parameters**: controller options `Improve / Combine / Pivot / Stop`; per-round cardinality `n_{d,r} ∈ [n_min, n_max]`; global budget `B` with `|F_B| ≤ B`. **The numeric values of `B`, `n_min`, `n_max`, the number of rounds, the prompts, the decoding settings and every model hyperparameter are `not stated in source`** — Section 4.5 only reveals incidental facts (the CSI 300 selected subset keeps **89 of 91 alphas**; one filtering stage "spends fourteen rounds confirming that no edit outperforms the selected subset").
- **Library filtering (Section 2.3)**: edits are remove / add / swap; score `Z(S) = Σ_k (m_k(S) − μ_k)/ς_k` over the eight metrics (IC, ICIR, RIC, RICIR, ARR, IR, MDD, CR) standardised against their historic distribution over evaluated nodes.
- **Model search (Section 2.4)**: candidates are model × hyperparameter pairs over Linear, LightGBM, XGBoost, CatBoost "and other models"; the winner is trained once on train + validation with early stopping on validation and evaluated once on the test window.
- **Portfolio rule (Section 3.2, verbatim in substance)**: "a cost adjusted daily strategy that holds the **50 stocks with the highest scores**, **replaces at most 5 of them per day**, and is benchmarked against the index of each universe". ARR is the annualised excess return over that index **net of transaction costs**; IR is the information ratio of daily excess returns; MDD is the maximum decrease of the **cumulative excess return**; CR = ARR / |MDD|. On the US universes "these metrics are computed on absolute returns without subtracting the index return" (Table 5 caption).
- **Position weighting**: the word `weight` appears **0 times in both pinned renderings** → equal-weight, value-weight, score-weight and risk-parity are all `data gap`; nothing is inferred. Similarly `short`, `leverage`, `margin` and `borrow` as trading terms are never used (see Execution assumptions).
- **Example discovered alphas (Figure 2 right panel, the only alpha expressions printed anywhere in the paper)** — name, printed ARR, printed expression and the model's printed rationale:
  - *Improve chain*: `Volume_Increase_Delta_ZRank` ARR −1.68%, "an institutional turnover increase predicts 20–30 day alpha", `RANK(ZSCORE(TS_PCTCHANGE($volume,5) − TS_PCTCHANGE($volume,20)))` → `Positive_Surprise_RangeBound_Filter` ARR +0.41%, "a positive surprise on a range-bound stock yields 60–90 day alpha", `RANK((TS_PCTCHANGE($close,5) > 0.05)·(ABS(TS_MEAN($return,20)) < 0.01)·TS_PCTCHANGE($close,5))` → `Volume_Increase_Low_Vol` ARR +2.73%, "continued inflow with low variability earns alpha", `RANK(ZSCORE(TS_PCTCHANGE($volume,12)) − ZSCORE(TS_STD($return,20)))`.
  - *Combine*: `Sentiment_Substitute_Trend` ARR −1.08%, `ZSCORE(TS_SUM($return,5))`; `Range_VolChange_Opposite` ARR −1.68%, `RANK(TS_ZSCORE($high−$low,20)·−TS_ZSCORE(DELTA($volume,1)/($volume+ε),20))`; `Combined_Narrative_Volume_Opposite` ARR +0.41%, `TS_ZSCORE($return,30)·[TS_ZSCORE($volume,30) < −1 && TS_ZSCORE(TS_STD($return,30),30) > 1 ? 1 : 0]`.
  - *Pivot*: `Volume_ZScore_10D` ARR −0.87%, `TS_ZSCORE($volume,10)` → `Volume_ZScore_5D_Rank` ARR −1.48%, `RANK(TS_ZSCORE($volume,5))` → `Volume_Increase_Ratio_Rank` ARR +1.95%, `RANK($volume/(TS_MEAN($volume,30)+ε))`.
  - *Stop*: `Trend_VolumeIncrease_5D` ARR −0.62%, `RANK(TS_SUM($return,5)·TS_ZSCORE($volume,5))` → `QualityESG_12M` ARR −0.83%, `(ZSCORE(−TS_STD($return,252)) + ZSCORE(TS_MEAN($return,252)) + ZSCORE(TS_ZSCORE(DELTA($volume,1),252))) / 3`.
  - The **window these per-alpha ARR numbers refer to is `underspecified`**: the Figure 2 caption prints only "ARR", while Section 2.1/4.5 state that the search observes only the feedback window. They are not test-window results and must not be read as such.
- **Not reconstructible from the source (`data gap`, never invented)**: the full alpha library for any universe (91 alphas on the CSI 300 search at the filtering stage, never enumerated beyond the eight Figure 2 examples), the label definition, the weighting scheme, the execution timing, the cost rate actually applied, and the search budget. **The printed strategy is therefore a description of a research process plus a portfolio construction rule, not a reproducible trading rule.**

**Scout-labelled operationalisation (`research-proposed`, not from the source):** form the score after the close of day `t`, hold the 50 highest-scored names, replace at most five per day, equal-weight the book (weighting is `research-proposed` because the source never states it), hold cash for the remainder, and measure against the point-in-time index. Any threshold, filter or failure rule in the Falsification plan is `research-defined`.

## Required data

- **Instrument / universe**: CSI 300, CSI 500, CSI 800, CSI 1000, S&P 500, NASDAQ 100 constituents; **point-in-time daily index membership** for all six (the source's only explicit survivorship statement).
- **Market type / venue**: cash equities, long-only top-50 book; no derivatives, no futures, no options, no crypto.
- **Timeframe / fields**: daily open, high, low, close, volume; no minute data, no order book, no fundamentals are named as inputs (the Figure 2 expressions use only price/volume fields such as `$volume`, `$close`, `$return`, `$high−$low`).
- **Benchmark series**: daily index return for each universe (CSI tables); **not used** for the US tables, which report absolute returns.
- **Point-in-time**: membership must be evaluated on the signal date only; the feedback window must be provably disjoint from the test window (the source's central design claim — see F6).
- **Timestamp / timezone / session**: `not stated in source` (`data gap`). No calendar, no holiday rule, no close-time convention is printed.
- **Data source / licence**: `not stated in source` — "accessed through Qlib" names the framework, not the vendor or dataset build (`data gap`), and with no code release the empirical pipeline cannot be re-run.
- **Labels**: definition not printed (`underspecified`) — required to recompute IC/ICIR/RIC/RICIR.
- **Missing data / tradability**: no rule for suspended names, price-limit rejections, delistings inside the held book, or partial fills → `data gap` (Chinese large-cap indices and the 5-name replacement cap make these material, but the source is silent).
- **Crypto-specific data**: none; see Crypto portability.

## Execution assumptions

**Cost determination from a Methods-level read** of Sections 2.1–2.4 (Problem Formulation, Alpha Discovery, Alpha Filtering, Model Search), 3.1–3.4 (Datasets, Evaluation Metrics, Baselines, Models), 4.1–4.5, Section 5, Tables 1–5 and Figures 1–2, plus a word-boundary scan of **both** pinned renderings (PDF 53849 chars, HTML 99343 chars):

- `transaction costs` occurs **exactly once in the PDF** (Section 3.2: "ARR is the annualized excess return over the benchmark index net of transaction costs") and **twice in the HTML** (Section 3.2 plus the Table 1 caption: "net of transaction costs"). **No rate, no schedule, no model, no per-side/per-value convention and no worked example is printed anywhere.**
- `fee`, `fees`, `commission`, `spread`, `bid-ask`, `slippage`, `impact`, `participation`, `ADV`, `borrow`, `financing`, `leverage`, `latency`, `fill`, `funding` → **0 hits in both renderings** (the single HTML `funding` hit is the arXiv footer "Major funding support from").
- `capacity` → 2 hits, both meaning *search-budget* capacity ("the controller allocates search capacity", "Capacity follows marginal evidence"), never trading capacity.
- `turnover` → 2 hits: one prose remark that "Information metrics alone do not price turnover, costs, and tail behavior" (no number attached), and one alpha name ("turnover increase substitute"). **Realized portfolio turnover is never reported**, only the structural cap of at most 5 of 50 names replaced per day.
- `margin` → 1 hit, prose ("The margin lies in redundancy control"), not a margin requirement. `Sharpe` → 3 hits in the PDF (4 in the HTML), all bibliographic (Sharpe et al., 1998, cited in the Table 5 caption); **no Sharpe is reported for any strategy in this paper** — the portfolio metrics are IR and CR.
- `execution`, `order`, `next day`, `open price`, `closing price`, `limit-up`, `suspended`, `T+1` → **0 hits**, so order type, execution price, signal-to-order delay, fill model, latency and untradeable-name handling are all `data gap`.

Consequences, stated conservatively:

- **Gross-versus-net status**: the source **claims** its ARR is net of transaction costs, and that claim is recorded as source-reported. The cost rate/model is `underspecified`, so the netting **cannot be reproduced, audited or scaled** from the publication; we do not treat the printed numbers as gross, and we do not treat them as verified net either.
- **`data gap`, never zero**: `commission`, `spread`, `slippage`, `market impact`, `participation`, `ADV`, trading `capacity`, `borrow`, `financing`, `leverage`, `margin`, `latency`, `fill / partial-fill / failure handling`, `funding`, and `turnover` (realized).
- **`underspecified`**: cost model actually applied; label horizon; position weighting; annualisation convention; signal-to-order timing; order type; execution price; cash handling; treatment of suspended/limit names inside the book; the structural claim "long-only" is implied by "holds the 50 stocks with the highest scores" but the words `long-only`, `short` and `no leverage` are never printed.
- **Search-side resource cost is also `data gap`**: no token budget, no dollar cost, no round count, no wall-clock — the "budget" that conditions every decision is never quantified.

## Evidence

### Source-reported

All figures below are read from the pinned v2 HTML (cross-checked cell by cell against the pinned PDF) and are **source-reported only**. Every table covers the **held-out test window June 2023 – May 2026**, and "each result averaged over three independent runs" (Section 3.2). The source states the CSI ARR is **net of transaction costs** at an unstated rate (see Execution assumptions); the US ARR is an **absolute** return. No number below has been independently reproduced.

Metric definitions as printed (Section 3.2): IC = Pearson correlation of scores vs realized labels in each daily cross-section; ICIR = mean daily IC / std of daily IC; RIC / RICIR = Spearman counterparts; ARR = annualised excess return over the universe index (US: absolute); IR = information ratio of daily excess returns; MDD = max decrease of the cumulative excess return; CR = ARR / |MDD|.

**Table 1 — "Main results on CSI 300", GPT-OSS-120B backbone (IC, ICIR, RIC, RICIR | ARR %, IR, MDD %, CR):**

| Method | Alpha | IC | ICIR | RIC | RICIR | ARR | IR | MDD | CR |
|---|---|---|---|---|---|---|---|---|---|
| LightGBM (best ML row) | ALPHA158 | 0.010 | 0.063 | 0.029 | 0.176 | −0.1 | −0.007 | −13.2 | −0.004 |
| Linear | ALPHA158 | 0.005 | 0.025 | 0.020 | 0.102 | −5.1 | −0.562 | −20.1 | −0.252 |
| LSTM (best DL ARR) | ALPHA158 | 0.006 | 0.043 | 0.017 | 0.151 | 0.5 | 0.092 | −7.5 | 0.072 |
| AlphaAgent | CUSTOM | 0.024 | 0.147 | 0.022 | 0.135 | −2.3 | −0.321 | −15.1 | −0.153 |
| AlphaAgent | +ALPHA158 | 0.030 | 0.182 | 0.027 | 0.168 | −1.0 | −0.151 | −12.5 | −0.087 |
| QuantaAlpha | CUSTOM | 0.024 | 0.144 | 0.022 | 0.130 | −1.6 | −0.207 | −14.5 | −0.096 |
| QuantaAlpha | +ALPHA158 | 0.031 | 0.190 | 0.029 | 0.177 | −0.2 | −0.018 | −12.5 | −0.013 |
| **AutoScientist-Quant** | CUSTOM | 0.028 | 0.185 | 0.026 | 0.172 | **1.8** | 0.259 | −12.7 | 0.143 |
| **AutoScientist-Quant** | +ALPHA20 | 0.028 | 0.181 | 0.026 | 0.165 | **2.4** | 0.330 | −12.5 | 0.209 |
| **AutoScientist-Quant** | +ALPHA158 | 0.034 | 0.219 | 0.032 | 0.206 | **3.5** | 0.500 | −9.5 | 0.368 |
| **AutoScientist-Quant** | +ALPHA360 | 0.033 | 0.212 | 0.031 | 0.198 | **3.0** | 0.401 | −12.0 | 0.263 |

(For orientation, the full Table 1 also contains 18 machine/deep-learning rows: the best of them on ARR is LSTM +ALPHA158 at 0.5% and the best on IC is LightGBM +ALPHA158 at 0.010; the worst is LSTM on ALPHA20 at −9.9% ARR with MDD −32.2%.) Source's own reading (Section 4.1): AutoScientist-Quant "attains the best value of all eight metrics in all four alpha settings **among agentic methods**", its excess return is positive in all four settings, and it keeps the smallest MDD among agentic methods in every setting.

**Table 2 — "Ablation of AutoScientist-Quant on CSI 300 under GPT" (ARR %, CUSTOM / +ALPHA20 / +ALPHA158 / +ALPHA360; each cell also prints gain over the best agentic value and gap to the full method):**

| Variant | CUSTOM | +ALPHA20 | +ALPHA158 | +ALPHA360 |
|---|---|---|---|---|
| Full method (Table 1 reference) | 1.8 | 2.4 | 3.5 | 3.0 |
| w/o Model Search (discovery + filtering) | 0.9 | 2.1 | 1.5 | 0.8 |
| w/o Alpha Filtering or Model Search (discovery only) | −0.3 | 1.2 | 0.6 | −0.1 |
| Alpha Discovery w/o Searching Strategy (Improve/Combine/Pivot/Stop) | −2.4 | −0.7 | −0.1 | −0.4 |
| Alpha Discovery w/o Dynamics (alpha count / early stopping / direction creation) | −2.9 | −2.6 | 0.5 | −1.2 |

Source's own reading (Section 4.2): removing model search costs "up to 2.2 percentage points of excess return" with IC nearly unchanged; removing alpha filtering as well moves CUSTOM from 0.9% to −0.3% "while IC stays within 0.003 of the full method"; removing the searching strategy moves CUSTOM from −0.3% to −2.4%; removing the dynamics costs "up to 3.8 percentage points of excess return against the same control, the largest single decrease in the study"; and "No single component explains the advantage".

**Table 3 — "Model robustness on CSI 300 under GLM" (ARR %; cells also print gain over the best baseline and gap to the full method):**

| Method | CUSTOM | +ALPHA20 | +ALPHA158 | +ALPHA360 |
|---|---|---|---|---|
| AlphaAgent | −3.1 | −1.1 | 0.9 | −3.3 |
| QuantaAlpha | −3.6 | −2.0 | −1.2 | −2.2 |
| AutoScientist-Quant, discovery only | −0.4 | 0.1 | 1.4 | 0.3 |
| **AutoScientist-Quant, full** | **0.6** | **1.1** | **2.5** | **1.1** |

Matching information metrics for the full method under GLM: IC 0.033 / 0.033 / **0.036** / 0.035 and ICIR 0.200 / 0.209 / 0.224 / 0.212. Source's own reading (Section 4.3): "seven of the eight baseline settings lose money after costs", and the full method beats the discovery-only variant by 0.8–1.2 pp of excess return with a shallower MDD in every setting.

**Table 4 — "Market robustness on CSI 500, CSI 800, and CSI 1000" (ARR % and IC; alphas re-discovered inside each universe):**

| Universe | Backbone | AlphaAgent ARR | QuantaAlpha ARR | AutoScientist-Quant ARR | AutoScientist-Quant IC |
|---|---|---|---|---|---|
| CSI 500 | GPT | −0.7 | 0.2 | **0.5** | 0.049 |
| CSI 500 | GLM | −0.1 | −1.3 | **−0.1** | 0.048 |
| CSI 800 | GPT | 0.8 | 0.2 | **2.4** | 0.045 |
| CSI 800 | GLM | −0.2 | 0.9 | **1.3** | 0.046 |
| CSI 1000 | GPT | 6.4 | 4.8 | **7.1** | 0.066 |
| CSI 1000 | GLM | 6.5 | 6.4 | **6.9** | 0.068 |

Source's own reading (Section 4.4): "the best or equal best excess return in all six settings and the best value on nearly all other metrics", with the stated exception that QuantaAlpha takes IC on CSI 1000 under GPT (0.067 vs 0.066); and "Gains concentrate where pricing is least efficient", IC rising from 0.043–0.049 on CSI 500/800 to 0.065–0.068 on CSI 1000.

**Table 5 — "Market robustness on S&P 500 and NASDAQ 100 under GLM", absolute returns (ARR %, IR, MDD %, CR):**

| Universe | Method | Alpha | IC | ARR | IR | MDD | CR |
|---|---|---|---|---|---|---|---|
| S&P 500 | AlphaAgent | CUSTOM | 0.006 | 10.4 | 0.687 | −21.1 | 0.476 |
| S&P 500 | QuantaAlpha | CUSTOM | 0.007 | 12.3 | 0.816 | −22.5 | 0.538 |
| S&P 500 | **AutoScientist-Quant** | CUSTOM | 0.009 | **15.4** | 1.021 | −19.8 | 0.795 |
| S&P 500 | **AutoScientist-Quant** | +ALPHA158 | 0.007 | 12.8 | 0.905 | −19.8 | 0.648 |
| NASDAQ 100 | AlphaAgent | CUSTOM | 0.009 | 20.1 | 1.083 | −20.9 | 0.970 |
| NASDAQ 100 | QuantaAlpha | CUSTOM | 0.010 | 22.3 | 1.041 | −25.0 | 0.877 |
| NASDAQ 100 | **AutoScientist-Quant** | CUSTOM | 0.018 | **28.9** | 1.297 | −22.5 | 1.289 |
| NASDAQ 100 | **AutoScientist-Quant** | +ALPHA20 | 0.011 | 24.6 | 1.280 | −18.5 | **1.323** |

Table 5 caption: "Each cell is the absolute metric computed without subtracting the index return, since US equity strategies are commonly evaluated this way (Sharpe et al., 1998)". Merged AutoScientist-Quant settings are **worse** than CUSTOM on both US universes (S&P 500 15.4 → 15.2 / 12.8 / 11.5 for +ALPHA20/+ALPHA158/+ALPHA360; NASDAQ 100 28.9 → 24.6 / 18.3 / 16.3).

**Section 4.5 case study (single search, CSI 300, GPT backbone):** the selected subset keeps **89 of 91 alphas** while "single swaps move test ARR by more than a percentage point"; two same-family volume z-score alphas take the subset to its stage low and two "volume increase" members lift it to its stage best; the Improve line's three generations backtest at **−1.7% / +0.4% / +2.7%**; one filtering stage "spends fourteen rounds confirming that no edit outperforms the selected subset, then rolls back to it"; Figure 2 left plots **test-window** ARR of the +ALPHA20 deployment after each round while "the search itself sees only the feedback window".

**Design claims used as evidence (Sections 1.2, 1.3, 2.1, 3.1):** feedback window (June 2021 – June 2023) disjoint from test window (June 2023 – May 2026); "the held out window enters exactly once"; two lookahead bugs in the inherited evaluation pipeline found and fixed, with **all methods re-evaluated** on the corrected pipeline; point-in-time index membership; two backbones (GPT-OSS-120B, GLM-5) with every conclusion re-checked.

### Independently reproduced

not independently reproduced

We verified only the artefact and the reading: pinned HTML and PDF sizes and SHA-256 hashes recorded above, 13-page PDF count and per-author metadata, the v2-latest check on the arXiv API and the DataCite record (version "2", preprint type, licence, registration dates), DOI resolution, the absence of Comments/journal-ref fields, and every quoted number located in a named table of the pinned v2 with a cell-level re-extraction cross-checked between the two renderings. No alpha was re-implemented, no model was trained, no portfolio was constructed, no search was re-run, and the source ships no code, no data and no prompts.

### Negative evidence

1. **The cost rate is never printed.** The paper asserts ARR is "net of transaction costs" (Section 3.2, Table 1 caption) and nothing else; `fee/commission/spread/slippage/impact/participation/ADV/borrow/financing/leverage/latency/fill` are all 0 hits, so the netting cannot be reproduced, audited or scaled → the cost model is `underspecified`, not verified.
2. **Realized turnover and capacity are never reported.** Only the structural cap (≤5 of 50 names per day) is printed; no turnover series, no ADV, no participation, no capacity, no break-even cost — so even the direction of the cost error is unknown.
3. **The signal itself is unpublished.** The CSI 300 search ends with 91 alphas in the pool (89 retained); only eight expressions appear, in a figure. The headline ARR cannot be attributed to any specific reproducible rule (`not stated in source`).
4. **The search budget is never quantified.** `B`, `n_min`, `n_max`, round counts, prompts, decoding settings and model hyperparameters are all missing, so the "budget-conditioned" mechanism cannot be reconstructed or costed — and neither can a budget-matched comparison.
5. **No dispersion, no inference.** Results are averages over three independent runs with **no standard deviation, no confidence interval, no p-value and no significance test anywhere in the paper** (`significance`, `p-value`, `confidence interval` → 0 hits), across 8 metrics × 4 alpha settings × 6 universes × 2 backbones plus 4 ablation families — no multiplicity control of any kind.
6. **The CSI 500 result is a tie at a negative number.** Table 4, CSI 500 under GLM: AutoScientist-Quant −0.1% ARR, identical to AlphaAgent −0.1%, on the source's own "best or equal best in all six settings" claim; the CSI 500 edge under GPT is 0.5% vs 0.2%.
7. **Source-internal contradiction** (declared in `contradictions`): Section 1.3 claims the discovered alphas "earn positive excess returns after costs on the held out test window", but Table 4 prints −0.1% for the full method on CSI 500 under GLM.
8. **Absolute levels are modest where the claim is strongest.** Table 1's best setting is ARR 3.5%, IR 0.500, CR 0.368 on a ~36-month window; the CUSTOM library alone gives 1.8% with IR 0.259; no Sharpe is reported at all.
9. **The margin over baselines is largely baselines being negative.** On Table 1 the AutoScientist-Quant − QuantaAlpha gap at +ALPHA158 is 3.5% vs −0.2% — the same comparison in raw information terms is 0.034 vs 0.031 IC, a 0.003 difference with no test behind it.
10. **The US tables change the return definition inside one paper.** Table 5 reports absolute returns (caption cites Sharpe et al., 1998) with no index return printed, so the beta component of the 15.4% / 28.9% figures is a `data gap` and those numbers are not comparable with the CSI excess-return tables.
11. **Merging standard libraries hurts on the US universes.** AutoScientist-Quant CUSTOM → +ALPHA158 falls from 15.4% to 12.8% (S&P 500) and 28.9% to 18.3% (NASDAQ 100), the opposite of the Section 4.1 "Generated and predefined alphas are complements" pattern that is true for Table 1's CSI 300 rows.
12. **All baselines are the authors' own re-runs.** Section 3.3: AlphaAgent and QuantaAlpha "share our backbone, search budget, and backtest procedure"; R&D-Agent-Quant is excluded by the authors because "its loop selects alphas on the window it reports". No baseline number is taken from an independent source, and the exclusion criterion is the authors' own.
13. **One shared pipeline for every row.** The paper itself documents that the inherited shared evaluation code carried two lookahead bugs that shifted results across all methods — a fix, but also proof that a single shared harness can move every row at once, with no independent harness to cross-check.
14. **No code, no data, no prompts, no configuration** → nothing is reproducible; availability fields are all `not stated in source`.
15. **Single test window, no subperiods.** One contiguous June 2023 – May 2026 window; no regime split, no subperiod table, no second confirmation window, and the whole search is never re-run forward in time.
16. **Selection is tuned to portfolio outcomes, not to information.** Section 4.2 shows the filtering and model-search stages move ARR by 1–2 pp while IC stays within 0.003 — i.e. the selection layer optimises a standardised score over eight correlated metrics on one feedback window, with no correction for that implicit multiplicity.
17. **The label, the weighting and the execution timing are undefined** (`underspecified`): no label horizon, no position weighting (the word `weight` never appears), no order type, no signal-to-order delay, no fill model, no timezone or session convention.
18. **The Figure 2 per-alpha ARR window is not stated** (caption prints only "ARR"), and Figure 2's left panel plots test-window ARR after every round of a single CSI 300 / GPT search — a post-hoc narrative from one run that the search never saw.
19. **US coverage has no backbone replication.** Table 5 runs GLM only, and alphas are re-discovered inside each universe, so there is no evidence of transfer across markets and no second backbone for the two US results.
20. **Budget can be burned without gain.** The case study's filtering stage spends fourteen rounds confirming no edit helps and then rolls back — the framework's own illustration that marginal search capacity is not always productive, with no aggregate productivity statistic reported.
21. **No independent third-party replication, no venue, no peer review**: preprint only (`v2`, 1 Sep 2026), no Comments field, no journal-ref, and a data source ("accessed through Qlib") with no vendor, build or licence.
22. **Tradability is unaddressed beyond the 5-name cap**: no price-limit rule, no suspension handling, no cash rule, no partial-fill or failed-order handling, no liquidity screen — all `data gap`.

## Falsification plan

Every threshold below is `research-defined` (Scout-chosen), and every operational rule not printed by the source is `research-proposed`. Data for all tests: the same six index universes with point-in-time membership, the source's split (train 2015-01→2020-01, validation 2020-01→2021-06, feedback 2021-06→2023-06, test 2023-06→2026-05) **plus a later frozen window extending beyond 2026-05**. Action on failure: record the hypothesis as disproved for this deployment and drop the candidate — no retuning of thresholds after seeing results.

- **F1 — frozen forward replication.** Re-run the complete three-stage search with a frozen window of ≥ 6 months ending after 2026-05, ≥ 3 independent searches per universe. **Pass** only if median-across-runs ARR excess over the index is > 0 with a moving-block-bootstrap 95% CI excluding zero in at least 3 of the 4 CSI universes. **Fail** otherwise.
- **F2 — cost ladder (decisive for tradability).** Net the identical book at 0/1/5/10/20/30 bp per side plus an explicit A-share commission-and-stamp-duty schedule (and a US schedule for the US tables). **Fail** if net IR < 0.50 at 10 bp one-way, or if a realistic A-share round trip erases > 50% of the printed ARR. This test exists because the source's own cost rate is `underspecified`.
- **F3 — turnover and capacity audit.** Measure realised top-50 membership churn under the ≤ 5-replacements/day cap and volume participation. **Fail** if one-way daily turnover exceeds 10% of the book (the cap's own implication under `0.5·Σ|Δw|`), or if holding 10% of 20-day ADV for the realised top-50 book cannot be funded at a stated capital base; the source prints neither, so this test produces the numbers it lacks.
- **F4 — decisive stage ablation.** Under identical budget, backbone and splits run (a) full method, (b) alpha discovery only, (c) static LightGBM + ALPHA158, ≥ 3 runs each. **Pass** only if (a) beats (b) by ≥ 1.0 pp ARR **and** (b) beats (c) by ≥ 1.0 pp ARR with 95% CIs excluding zero in ≥ 3 of 4 CSI universes. **Fail** if the selection stages or the discovery layer add nothing — the paper's own Table 2 shows both effects are single-digit percentage points with no uncertainty attached.
- **F5 — sham-controller test (decisive for the mechanism).** Replace the budget-conditioned controller with a uniformly random option policy (Improve/Combine/Pivot/Stop with equal probability, random parent, `n` drawn from the same range) at an identical token/round budget, ≥ 5 seeds. **Fail** if the random controller matches the real one within 1.0 pp ARR and 0.002 IC — that would reduce the contribution to "more search beats less search", not "budget conditioning helps".
- **F6 — leakage audit.** Verify from code that no test-window observation reaches any search decision, that the two inherited lookahead bugs are absent, that index membership is point-in-time, and that the feedback window ends before the test window begins. **Fail** on any single instance of test-window access, full-sample metric computation, or membership dated after the signal.
- **F7 — permutation null.** Circularly shift each date's predicted score cross-section by random offsets (1000 draws). **Pass** only if observed IC exceeds the 95th percentile of the null in ≥ 3 of 4 CSI universes.
- **F8 — multiplicity.** Apply Benjamini–Hochberg over the family 6 universes × 8 metrics × 4 alpha settings. **Fail** if no AutoScientist-Quant comparison survives `q < 0.10`.
- **F9 — competing-explanation horse race.** Re-run QuantaAlpha, AlphaAgent and LightGBM+ALPHA158 with matched backbone, matched search budget and ≥ 3 runs each. **Fail** if AutoScientist-Quant is not top-2 on *net* IR in ≥ 3 of 4 CSI universes.
- **F10 — portfolio-definition robustness.** Recompute as value-weighted top-50, top-25, long-short top-50 minus bottom-50, and index-neutral (beta-hedged) residuals; for the US tables, subtract the index return. **Fail** if the long-short spread has Newey-West `t < 1.96`, if the effect exists only in one weighting, or if the US result disappears once index beta is removed.
- **F11 — regime / subperiod stability.** Split the test window into ≥ 3 contiguous subperiods. **Fail** if ≥ 2 of 3 are non-positive in any two CSI universes.
- **F12 — reproducibility gate.** If no code, library or prompts become public within 12 months of 2026-09-01, mark the result permanently `unverifiable` and drop it regardless of printed numbers; if they do become public, a third party must reproduce Table 1 IC and ARR within ±20%.
- **F13 (crypto port, only if adapted)** — port the *pipeline* (daily OHLCV universe → discovered library → model search → top-50 book with ≤ 5 replacements/day) to a BTC/ETH top-50 daily universe under a 10 bp one-way ladder. **Fail** unless Newey-West `t ≥ 1.96` and net IR > 0 survive 10 bp.

## Crypto portability

**`unproven`.**

The source contains **zero crypto evidence**: no crypto universe, no perpetual or futures contract, no funding, no mark/index price, no 24/7 session, no venue fragmentation, no borrow or short-side analysis, and no cost section beyond an unparameterised "net of transaction costs" sentence. Its entire data dependency — point-in-time index membership for six equity indices, daily equity OHLCV, index benchmarks — has **no crypto counterpart** (no index exists for a crypto top-50 book), and none of the crypto-specific frictions (funding rate, mark-price liquidation, 24/7 candle boundaries and timestamp alignment, listing/delisting churn, cross-venue liquidity fragmentation, custody/withdrawal risk) appear anywhere in the paper.

What *could* port is only the research method (budget-conditioned search with a feedback window disjoint from the test window, plus library filtering and model search), which would be a `research-proposed` adaptation and not crypto empirical evidence. A genuine portability claim requires F13 to pass. Crypto portability is not authorisation to trade.

## Limitations

- **`data gap`**: every trading-cost field (commission, spread, slippage, impact, participation, ADV, trading capacity, borrow, financing, leverage, margin, latency, fill/failure handling, funding, realised turnover); label horizon; position weighting; order type, execution price and signal-to-order timing; timezone/session convention; suspended and price-limit handling inside the book; data vendor, dataset build and licence; search budget, round counts, prompts and model hyperparameters; index return for the US tables; code, data and prompt availability.
- **`underspecified`**: the transaction-cost model behind the "net of transaction costs" claim; the window that Figure 2's per-alpha ARR refers to; the annualisation convention; the implied (never stated) long-only/no-leverage framing; the exact meaning of "replaces at most 5 of them per day" (names replaced vs weight traded).
- **`not stated in source`**: the alpha library itself (91 alphas in the CSI 300 pool, eight printed examples), which makes the printed strategy a description of a research process rather than a reproducible trading rule.
- **`not independently reproduced`**: every number in this record; we read and hashed the pinned source, re-extracted its tables and cross-checked two renderings, but re-ran nothing — and the source provides no code, data or prompts to re-run.
- **`unproven`**: crypto portability; any net-of-cost profitability at an unknown cost rate; out-of-window stability beyond a single June 2023 – May 2026 test window; transfer of discovered alphas across universes (alphas are re-discovered per universe by design); any capacity claim.
- **Design limitations**: no dispersion or significance testing behind three-run averages; no multiplicity control over a large metric × setting × universe × backbone grid; baselines are the authors' own re-implementations with one competitor excluded by the authors; one shared evaluation harness for every row (which the paper itself shows can carry lookahead bugs); US results on a single backbone and on a different return definition; a source-internal contradiction between Section 1.3 and Table 4; preprint status with no venue and no peer review.
- **Scope**: this is a record of *research material*. Presence in this repository does not imply the strategy works, was validated, or may be traded.

## Implementation status

`implementation_status: not-implemented`. No implementation exists in our research stack: no alpha was re-implemented, no model was trained, no portfolio was constructed, and no backtest, Paper, Testnet or Live run has occurred. The source itself ships no code, no data and no prompts. Nothing here implies Qlib full-backtest validation or any downstream approval.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record did **not** pass Research Intake Review, did **not** enter Hermes Wiki Brain as an adopted record, did **not** enter the production candidate pool, did **not** complete Qlib validation, and did **not** become a frozen survivor or leaderboard entry. It is not evidence of profitability, not validated alpha, and not approval to implement, paper-trade, testnet-trade or trade.

## Related Wiki records

Mechanism-adjacent pages returned and verified by Wiki Brain `kb_search` for this run (`LLM agent alpha factor discovery agentic`, 10 hits, of which one was an unrelated Hermes release-JSON page and the following six are mechanism-adjacent and are the only pages linked; a second query, `budget search controller alpha library selection model search feedback window held-out test`, returned 0 hits):

- [[quant/alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05]]
- [[quant/alphag-opd-reliability-gated-sibling-counterfactuals-symbolic-alpha-2026-09-05]]
- [[quant/alphalogics-market-logic-multi-agent-factor-generation-2026-09-05]]
- [[quant/vst-verifiable-structured-transport-agentic-alpha-discovery-2026-09-12]]
- [[quant/alphaschema-trading-semantic-plan-space-surrogate-guided-factor-mining-2026-09-05]]
- [[quant/llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04]]

No other Wiki Brain pages were verified for this record; no page is linked beyond the six returned by search, and no page was written.

## Sources

1. Li, Z., Li, Y., Guo, Y., Zhang, M., Collier, N., & Ie, E. (2026). *AutoScientist-Quant: Self-Evolving Coding Agents for Automatic Research in Quantitative Investment*. arXiv:2608.28632v2 [cs.AI; cs.CL, cs.LG], v1 submitted 5 August 2026, v2 submitted 1 September 2026. https://arxiv.org/abs/2608.28632 — DOI https://doi.org/10.48550/arXiv.2608.28632 (DataCite, state=findable, resourceTypeGeneral=Preprint, version "2", registered 2026-09-01, checked 2026-09-26). No Comments field, no journal-ref, no peer-review statement. Licence: arXiv.org perpetual non-exclusive distribution licence. Title block: Zongqian Li (Google and University of Cambridge, "Work done during an internship at Google"), Yaoyiran Li (Google, corresponding), Yaohui Guo (Google), Ming Zhang (Google), Nigel Collier (University of Cambridge, corresponding), Eugene Ie (Google).
2. Pinned full text (HTML): https://arxiv.org/html/2608.28632v2 — 599,812 bytes, SHA-256 `bdec9a73b0f0e4dd688eece9f87f3f70e0dab416a81808af58e76cefd286b4ae`, downloaded and read 2026-09-26.
3. Pinned full text (PDF): https://arxiv.org/pdf/2608.28632v2 — 717,678 bytes, SHA-256 `76df8ee72ce287146eeb7a2cf43b185b461080d1f36ea2b2a97976b8a7944ae5`, 13 pages, downloaded 2026-09-26.
4. DataCite DOI record: https://api.datacite.org/dois/10.48550/arxiv.2608.28632 — retrieved 2026-09-26 (version, rights, registration and version-history dates).

All quantitative claims above are labelled source-reported and trace to Table 1, Table 2, Table 3, Table 4, Table 5, Figure 2, Sections 1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 2.4, 3.1, 3.2, 3.3, 3.4, 4.1, 4.2, 4.3, 4.4, 4.5 and 5 of source 1 as rendered in sources 2 and 3. The source states the CSI figures are net of transaction costs at an unstated rate; none has been independently reproduced.
