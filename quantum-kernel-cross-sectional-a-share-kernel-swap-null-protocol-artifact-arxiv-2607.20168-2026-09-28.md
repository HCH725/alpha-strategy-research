---
schema: strategy-research-record-v1
title: "Quantum kernel ridge regression on the China A-share cross-section — kernel-swap null (ΔIC +0.005, p = 0.42) plus an anatomy of how a hindsight-screened universe manufactures a quantum 'advantage' (arXiv:2607.20168)"
created: 2026-09-28
updated: 2026-09-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equities
  - china-ashare
  - cross-sectional
  - machine-learning
  - quantum-kernel
  - negative-evidence
  - point-in-time-universe
  - survivorship-bias
  - multiple-testing
status: research-only
confidence: medium
source_as_of: 2026-07-22
sources:
  - "https://arxiv.org/abs/2607.20168 — arXiv:2607.20168v1 [q-fin.PR primary; quant-ph, stat.ML], 'Quantum Kernels and the Cross-Section of Stock Returns: Anatomy of a Vanishing Advantage', Junchi Shen (sole author, no affiliation printed in the pinned text), submitted Wed, 22 Jul 2026 14:04:12 UTC; landing comments field reads '16 pages, 2 figures, 5 tables. Code and data pipeline available on request'; no journal-ref field and no publisher DOI on the landing; title page line reads 'Manuscript prepared for submission to Quantitative Finance' — read 2026-09-28"
  - "https://arxiv.org/html/2607.20168v1 — pinned v1 full text, 189,687 bytes, SHA-256 7da66a016dab462f2d3ae0fcffc200384714cb113d1b094b3623b6c97e77bafe, converted to 48,926 characters / 1,034 lines and read end to end on 2026-09-28 (Sections 1–10, Tables 1–5, Figures 1–2 captions, Data and code availability block, full reference list)"
  - "https://doi.org/10.48550/arXiv.2607.20168 — DataCite DOI, HTTP 302 → https://arxiv.org/abs/2607.20168, checked 2026-09-28; no journal DOI, no peer-review statement anywhere in the pinned text → preprint only"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Main sample window: Table 3's caption and Section 4.1 both print '170 out-of-sample windows (2012–2025)' while Section 5's subperiod prose reports a '2011–2015' cell (0.027 vs 0.044), Section 3.1 states data cover 'January 2010 through March 2026', and Section 3.2 states the panel holds '1.66 million pool stock-days over 2011–2025' — unreconciled."
  - "Training-window size: the abstract prints '~38,000-observation windows' while Sections 4.4 and 5.1 print '≈37,800' for the same object — unreconciled (rounded vs stated figure)."
  - "Comparator identity for the one nominally significant deficit: Section 5 states '−0.022 versus plain ridge (nominal p = 0.043; Wilcoxon p = 0.027)', which matches the full-set ridge row of Table 3 at printed precision (0.0254 − 0.0477 = −0.0223) and not the top-8 ridge row (0.0494 → −0.0240) that the Section 5.1 budget 2×2 uses — which ridge row was tested is ambiguous."
  - "Multiplicity scope: the abstract claims that 'after family-wise correction no pairwise difference among eleven models is significant' (55 pairs read literally), while Section 5.2 reports Holm adjustment over 'the ten-pair family' with smallest adjusted p = 0.43 — unreconciled."
  - "Section 6.2 states that 'Holm-adjusting the diagnostic study's own eight-pair test family leaves no comparison significant (smallest adjusted p = 0.19)' and, two sentences later, that 'the only quantum win that survives family-wise correction anywhere is the comparison against the MLP' whose nominal p = 0.006 in Section 6.1; if that comparison sits inside the eight-pair family, Holm's smallest adjusted value would be 0.006 × 8 = 0.048, not 0.19 — unreconciled."
---

# Quantum kernel ridge regression on the China A-share cross-section — kernel-swap null plus a hindsight-screened-universe artifact anatomy (arXiv:2607.20168)

## Provenance

- **Primary source:** Junchi Shen (sole author; no affiliation, email or ORCID printed in the pinned text), *«Quantum Kernels and the Cross-Section of Stock Returns: Anatomy of a Vanishing Advantage»*, `arXiv:2607.20168v1 [q-fin.PR]`, cross-listed `quant-ph`, `stat.ML`; **v1 submitted Wed, 22 Jul 2026 14:04:12 UTC (513 KB)**; submission history shows **only [v1]**.
- **Stable URL:** https://arxiv.org/abs/2607.20168 · **DOI:** https://doi.org/10.48550/arXiv.2607.20168 (DataCite, HTTP 302 → landing, checked 2026-09-28).
- **Full text read for this record:** https://arxiv.org/html/2607.20168v1, **189,687 bytes, SHA-256 `7da66a016dab462f2d3ae0fcffc200384714cb113d1b094b3623b6c97e77bafe`**, converted to 48,926 characters / 1,034 lines and **read end to end on 2026-09-28** (Abstract; Sections 1–10; Tables 1–5; Figure 1–2 captions; the Data and code availability block; the full reference list).
- **Title-page status line:** "Manuscript prepared for submission to *Quantitative Finance*"; landing shows **no journal-ref field, no publisher DOI and no peer-review statement** → publication status is **preprint only / not stated in source**.
- **License:** landing shows "License: arXiv.org perpetual non-exclusive license".
- **Code / data:** the landing comments field reads "Code and data pipeline available on request" and the Data and code availability block states the pipeline is "implemented in fourteen Jupyter notebooks with all intermediate artifacts persisted to disk; quantum simulation uses PennyLane … Materials are available from the author on request" → **no public repository, no immutable commit, no frozen data artifact** (a reproducibility `data gap`, not zero).
- **Sample / data as-of:** daily data **January 2010 – March 2026** (Section 3.1); main study **170 walk-forward windows labelled 2012–2025** (Table 3 caption, Section 4.1); diagnostic study **60 windows, 2021–2025** (Section 6.1); point-in-time panel "1.66 million pool stock-days over 2011–2025" (Section 3.2). Sample-window statements are not mutually consistent — see frontmatter contradiction 1.
- **Universe:** China A-shares, two constructions — a **point-in-time** pool (trailing 252-day price coverage > 90%, top 450 by trailing 20-day mean float market capitalisation) and a deliberately retained **static full-sample screen** (the 450 names with the highest price coverage across the whole 2020–2025 sample, i.e. a survival-conditioned, non-implementable screen) used as the treatment arm of a research-design experiment (Section 3.2).
- **Repository deduplication audit (2026-09-28, hidden-inclusive `rg -uuu` across the whole checkout including `.git`, `.mimo-worktrees`, `.agents`, `.hermes`):** exact source-identity patterns `2607.20168`, `Vanishing Advantage`, `Junchi Shen`, `qkrr` / `QKRR`, `kernel-swap` / `kernel swap`, `fidelity kernel` all returned **0 files**; the phrase `quantum kernel` returned exactly **1 file** (`triadic-stress-index-correlation-network-stress-state-risk-overlay-2026-09-25.md`, line 184) whose match is an incidental description of a *different* source (`geometric-observables-qcml-regime-detection-berry-phase-rate` / arXiv 2605.17117); positive control `novy-marx` returned **11 files** in the same session (search is live); `coverage_manifest.csv` returned **0** hits for `2607.20168`. `git log --oneline -20` was used as a convenience glance only. **Dedup passed: hard cap 1, this is a new source identity.**

## Economic mechanism

### Source-reported

- The paper's stated object is not a return-predictive mechanism but a **model-class hypothesis**: encoding the top-8 cross-sectional factor z-scores into an entangling (IQP-style, ring-coupled) quantum feature map on 8 qubits produces a kernel whose `ZZ` phases natively encode pairwise factor interactions, so quantum kernel ridge regression (QKRR) should extract cross-sectional return structure that a classical RBF kernel and penalized linear models cannot (Sections 1 and 4.2).
- The author's own stated diagnosis of the (null) result: the screened, low signal-to-noise, approximately linear equity cross-section is a "hostile arena" for quantum kernels, consistent with the cautious QML theory strand (expressive embeddings concentrate exponentially unless inputs are bandwidth-rescaled; geometric difference is necessary but not sufficient; tuned fidelity kernels rarely beat classical kernels on generic classical data) (Sections 1 and 2).
- The second, methodological claim: a **statistical "quantum advantage" in finance is easy to manufacture unintentionally** when the evaluation uses a hindsight-screened universe, a short window count and data-starved neural baselines; the same pipeline reported "the opposite conclusion" under that design (Sections 1, 6 and 10).
- Proposed protocol standards (Section 10): (i) a kernel-swap / like-for-like control isolating the kernel from the pipeline; (ii) budget-equalized comparisons; (iii) universes and features constructible in real time; (iv) window counts sufficient to resolve the claimed effect size under family-wise correction.

### Research interpretation

- **Hypothesis under test (source's, falsifiable):** at matched training subsamples, solver and tuning budget, `IC(QKRR fidelity) − IC(RBF) > 0` for 20-day-ahead cross-sectional A-share returns, and quantum models should at minimum not be beaten by equal-budget penalized linear models. **The source reports this hypothesis is rejected** on its clean protocol.
- **Mechanism classes involved:** (a) *cross-sectional factor-mixture predictability* — the rotation over up-to-31 firm characteristics with a per-window IC screen is the actual working signal; (b) *interaction/nonlinearity alpha* — whether pairwise characteristic products carry exploitable OOS information (source finds they do not, and that feeding them to the quantum model hurts); (c) *research-design artifact* — survivorship-conditioned universe selection plus under-powered window counts inflates apparent IC, ICIR, hit rate and drawdown stability.
- Our interpretation keeps (a)–(c) separate: **the record's tradable content, if any, is the classical ridge / poly(2)-ridge top-8 ranking, not the quantum kernel.** The quantum component is a negative-evidence control. Any statement that "quantum kernels add cross-sectional alpha in A-shares" is **disconfirmed by the source itself**.
- This is a **ported hypothesis for crypto**, not crypto evidence: the source tests only Chinese A-share cash equities on a 20-day horizon and long-only construction, and names crypto only as a possible future test bed (Section 9).

## Signal

All items below are **source-reported** from the pinned v1 text unless explicitly labeled otherwise. The signal is reconstructable at the level the paper specifies; items the paper does not state are marked `underspecified`.

- **Prediction target:** the 20-trading-day forward return; prices are extended beyond each study's end so no training label is truncated (Section 3.2).
- **Formation timestamp / tradability:** at each rebalance date `t` (every 20 trading days) the training window is the trailing 252 trading days **ending 20 days before `t`**, so every label is realized; cross-sections inside the window are sampled **every third day** (Section 4.1). Timezone, clock and session-close convention: **`data gap`** (not stated in source).
- **Feature construction:** daily characteristics from exchange snapshots (price, valuation ratios, market capitalisation, turnover) and quarterly financial statements; fundamentals merged **as of announcement dates** with the stated aggregation rules (TTM sums only when four consecutive quarters span ≤ 380 days; balance-sheet items at latest disclosed level; YoY growth requires a 330–400-day span; every value forward-filled at most 250 trading days). Each characteristic is **winsorized at ±3σ and standardized cross-sectionally each day over the full market before any universe restriction** (Section 3.1).
- **Lookback / rotation:** for each characteristic the window's average cross-sectional rank IC is computed; the *active set* keeps characteristics with `|mean IC| ≥ 0.015` (minimum six), sign-corrected; the *top-8 set* keeps the eight largest `|mean IC|` and is **shared verbatim by all top-8 models, classical and quantum** (Section 4.1). Main study uses **27** characteristics reconstructible to 2010; the diagnostic study adds four available only from 2020 (RSRS, analyst revisions and variants) for **31**.
- **Quantum feature map:** `x ∈ ℝ^8` = sign-corrected top-8 z-scores **clipped to [−3, 3]**; bandwidth `x̃ = λx`; `R = 2` repetitions of an IQP-style layer on `n = 8` qubits with ring entanglement (indices mod n); fidelity kernel `κ_Q = |⟨ψ(x)|ψ(x′)⟩|²`; projected quantum kernel on the 24-dimensional Bloch-vector features `κ_P = exp(−γ‖φ(x)−φ(x′)‖²)`; **bandwidth tuned per window on the grid {0.05, 0.1, 0.2, 0.4}**; all states by **noiseless exact statevector simulation (PennyLane)**; Gram matrices by one matrix product (Section 4.2).
- **Estimator:** kernel ridge regression `α̂ = (K + αI)^{-1}y` with **`α ∈ {10⁻³, 10⁻², 10⁻¹, 1}`**; because exact KRR is `O(N³)` each window's training set is **stratified-by-date subsampled to `N = 1,536`** observations; within-window temporal 80/20 split; selection criterion for `(λ, α, γ)` is **validation rank IC** (Sections 4.3 and 4.5).
- **Kernel-swap control:** the identical subsample, identical ridge solver and identical per-window hyperparameter budget are applied to three kernels — `qkrr-fid` (fidelity), `qkrr-pqk` (projected) and `krr-rbf` (classical RBF on the same top-8 inputs) — so any performance difference isolates kernel geometry (Section 4.3).
- **Classical benchmarks:** ridge regression (α = 10) on all ≈37,800 window observations; XGBoost (150 trees, depth 3, learning rate 0.05); a 64–32 MLP; `nn3` = the three-hidden-layer 32–16–8 three-seed network of Gu et al. (2020) / Leippold et al. (2022); `poly2ridge` (ridge on all pairwise products of the top-8); `ridge-int` (active set plus catalog interactions passing the same IC screen); `xgb-x`; `qkrr-x` (fidelity QKRR whose rotation pool includes the catalog interactions); and a rank-average hybrid of `qkrr-fid` and ridge (Section 4.4).
- **Budget 2×2 (Section 5.1):** `ridge-sub` trained on exactly the kernel machines' 1,536-observation subsamples; `qkrr-nys` = Nyström extension of the fidelity QKRR to all ≈37,800 observations using the 1,536 subsample as landmarks and the window's already-selected bandwidth.
- **Entry (portfolio mapping):** **long-only top-30% equal-weighted portfolio** by model score, **rebalanced every 20 trading days**, charged **23 bp one-way cost** (Section 4.5). Long-only is attributed by the source to "A-share shorting constraints" (Section 9).
- **Exit / holding period:** exit is implicit in the 20-day rebalance; no stop, no drawdown trigger, no intra-horizon rule is stated → holding period **20 trading days**, `underspecified` beyond that.
- **Short entry:** none (long-only by construction).
- **Position sizing:** equal weight inside the top-30% book; no volatility targeting, no cap per name beyond equal weight → stated as such; any leverage rule is `data gap` (not stated).
- **Interaction catalog:** twelve literature-sourced pairwise interactions (Table 2) built as the daily cross-sectional product of component z-scores, re-winsorized and re-standardized, **signs not imposed** — oriented by the same window-level IC screen (Section 3.3).
- **Rotation-log facts (Section 4.1):** EBITDA/EV's sign flips negative after September 2024; lottery MAX enters the top-8 in **56 of 60** short-study windows.
- **Parameters that are fixed vs tuned:** fixed — 252-day training window, 20-day horizon/rebalance, third-day sampling, `|mean IC| ≥ 0.015`, top-8, ±3σ winsorization, clip [−3,3], `R = 2`, `n = 8`, `N = 1,536`, top-30% book, 23 bp one-way; tuned per window — bandwidth `λ`, ridge `α`, projected-kernel `γ`, all on printed grids.

## Required data

- **Instrument / universe:** China A-share common stocks; point-in-time eligibility = trailing 252-day price coverage > 90%, investable pool = top 450 by trailing 20-day mean **float** market capitalisation (Section 3.2). Delisting / re-listing treatment beyond the coverage screen: **`data gap`** (not stated).
- **Venue / market type:** Chinese exchanges, cash equities, daily bars; no futures, no options, no crypto.
- **Timeframe:** daily data; cross-sections sampled every third day inside training windows; 20-trading-day rebalance.
- **Fields:** OHLCV (price), valuation ratios, market capitalisation / float market capitalisation, turnover; quarterly financial statements for 27 (31) characteristics spanning value, profitability & quality, growth & surprises, risk & leverage and technical categories (Table 1), including book-to-price, sales-to-price, earnings yield, dividend yield, ROA, ROE, gross/net margin, asset turnover, CFO-to-net-income, percent accruals, sales/earnings/asset growth, Δgross margin, standardized earnings surprise, earnings variability, market beta, debt-to-asset, current ratio, 12–1 momentum, 1-month reversal, Bollinger z-score, PPO, lottery MAX; plus RSRS and analyst revisions in the diagnostic study only.
- **Point-in-time requirements:** announcement-date alignment for all fundamentals with the printed aggregation windows; market-based characteristics point-in-time by construction; the static-screen universe is explicitly **not** point-in-time and is retained only as an experimental treatment arm.
- **Timestamp / timezone / session convention:** **`data gap`** — not stated in source.
- **Missing data:** forward-fill capped at 250 trading days; trailing-coverage screen; no other imputation rules stated (imputation beyond the printed forward-fill cap is not specified → `underspecified`).
- **Cost / fee / spread fields:** the only cost input is a **flat 23 bp one-way** charge on the portfolio evaluation. Spread, slippage, market impact, borrow, commission, fee schedule, participation and capacity fields are **not present in the source** → `data gap` (never zero).
- **Not required by this source:** funding, mark/index/basis, order book, open interest, options surface, trades/aggressor side.

## Execution assumptions

Determined from a Methods-level read of Sections 4.1–4.5 (protocol and evaluation) and Section 9 (limitations), plus a whole-document scan of the pinned text (48,926 characters) for cost and execution vocabulary.

- **Signal-to-order timing / fill model / order type:** **`data gap`** — the pinned text contains **zero** occurrences of `market order`, `limit order`, `order type`, `latency`, `participation`, `slippage`, `spread`, `market impact`, `commission`, `fees`, `borrow` and `liquidation`. Nothing about fills can be read as zero.
- **Costs:** exactly one cost statement — the portfolio evaluation is "a long-only top-30% equal-weighted portfolio rebalanced every 20 days at **23 bp one-way cost**" (Section 4.5), and Section 9 adds "Transaction costs are proportional". Whether 23 bp is commission-only or also absorbs spread/impact is **not stated in source** → `data gap`.
- **Turnover:** `turnover` appears in the pinned text **three times, all as an input characteristic** (exchange-snapshot field, "asset turnover", "gm × turnover" interaction). **Portfolio turnover is never reported**, so the 23 bp charge cannot be converted into an annual cost → `data gap`.
- **Shorting / borrow:** no borrow cost model; long-only design is justified by "A-share shorting constraints" (Section 9).
- **Leverage / margin:** not stated → `data gap`.
- **Latency / capacity:** not stated; the only `capacity` occurrence is "qubit capacity is scarce" (Section 7) and the only `funding` occurrence is arXiv page chrome, not the paper.
- **Compute latency:** all kernels are noiseless statevector simulations at `n = 8` qubits; the source states explicitly that at 8 qubits "the kernel is classically computable and no computational speedup was ever at stake" (Section 9) — so no execution-speed claim is made.
- **Scout assumptions:** none added. No Scout-imposed fill model, no Scout-imposed cost beyond quoting the source's 23 bp.

## Evidence

### Source-reported

All figures below are third-party claims from Shen (`arXiv:2607.20168v1`), each with its location in the pinned text; **none has been independently reproduced**. The asset class is **Chinese A-share cash equities** throughout; none of these numbers is crypto evidence.

**Table 3 — main evaluation, point-in-time universe, 170 out-of-sample windows (2012–2025), mean OOS cross-sectional rank IC / ICIR / t-stat / hit rate / net Sharpe (portfolio column, 23 bp one-way):**

| Model | Mean IC | ICIR | t-stat | Hit rate | Sharpe |
|---|---|---|---|---|---|
| Poly(2) ridge (top-8) | 0.0499 | 0.272 | 3.55 | 0.629 | 0.272 |
| Ridge (top-8) | 0.0494 | 0.247 | 3.21 | 0.671 | 0.306 |
| Ridge (full set) | 0.0477 | 0.248 | 3.23 | 0.647 | 0.272 |
| Hybrid (QKRR + ridge) | 0.0453 | 0.250 | 3.26 | 0.635 | 0.283 |
| Ridge + catalog interactions | 0.0451 | 0.243 | 3.17 | 0.653 | 0.242 |
| XGBoost (top-8) | 0.0385 | 0.247 | 3.22 | 0.606 | 0.219 |
| XGBoost (full set) | 0.0299 | 0.197 | 2.57 | 0.594 | 0.203 |
| QKRR fidelity | 0.0254 | 0.171 | 2.23 | 0.582 | 0.134 |
| NN3 (Gu et al. 2020) | 0.0243 | 0.202 | 2.64 | 0.529 | 0.137 |
| KRR-RBF control | 0.0208 | 0.161 | 2.10 | 0.582 | 0.162 |
| QKRR projected | 0.0168 | 0.134 | 1.74 | 0.571 | 0.092 |

- **Headline null (abstract and Section 5):** fidelity QKRR vs its RBF control **ΔIC = +0.005, p = 0.42** (paired t; Wilcoxon p = 0.66) over 170 windows; vs `nn3` **+0.001 (p = 0.90)**; vs top-8 XGBoost **−0.013 (p = 0.16)**; vs "plain ridge" **−0.022 (nominal p = 0.043; Wilcoxon p = 0.027)** — comparator ambiguity recorded as frontmatter contradiction 3; quantum–ridge hybrid vs ridge alone **p = 0.59**.
- **Subperiods (Section 5 prose only, no table):** fidelity QKRR vs ridge — **0.027 vs 0.044 (2011–2015)**, **0.032 vs 0.070 (2016–2020)**, **0.020 vs 0.034 (2021–2025)**.
- **Portfolio prose (Section 5):** "the quantum portfolio's net Sharpe of 0.13 sits below the equal-weight benchmark's 0.15, while top-8 ridge reaches 0.31" — the **0.15 equal-weight figure is prose-only and does not appear in Table 3**.
- **Table 4 — kernel type × training budget (same 170 windows):** Ridge `N=1,536` **0.0355** / `N≈37,800` **0.0494**; QKRR fidelity **0.0254 / 0.0438**; KRR-RBF **0.0208 / —**. Matched small budget: quantum − linear = **−0.010 (p = 0.26)**. Matched full budget: **−0.006 (p = 0.43)**. Data gains: quantum **+0.018 (p = 0.07)**, linear **+0.014 (p = 0.06)** — i.e. the budget-equalized design removes both the "significant quantum loss" and the "sample-efficiency selling point".
- **Multiplicity (Section 5.2):** Holm adjustment over "the ten-pair family" leaves nothing significant; **smallest adjusted p = 0.43** (fidelity QKRR vs ridge); nominal p-values in the 0.03–0.05 range are expected by chance.
- **Table 5 — diagnostic study, static-screen universe, 60 windows (2021–2025), 31 characteristics, "sixteen-model field", selected models printed (Mean IC / ICIR / t / hit rate / Max DD):** Hybrid **0.0606 / 0.469 / 3.63 / 0.783 / −31.3%**; Ridge (full) **0.0567 / 0.389 / 3.02 / 0.717 / −33.7%**; **QKRR fidelity 0.0512 / 0.488 / 3.78 / 0.800 / −27.1% (best ICIR, t, hit rate and drawdown of the field while training on 1,536 observations vs 37,800)**; Ridge (top-8) **0.0507 / 0.344 / 2.66 / 0.633 / −33.2%**; Poly(2) ridge **0.0470 / 0.354 / 2.74 / 0.617 / −29.8%**; XGBoost (full) **0.0366 / 0.320 / 2.48 / 0.700 / −32.5%**; KRR-RBF **0.0365 / 0.429 / 3.32 / 0.717 / −32.8%**; QKRR projected **0.0316 / 0.372 / 2.88 / 0.717 / −31.8%**; NN3 **0.0258 / 0.328 / 2.54 / 0.617 / −32.1%**; MLP **0.0110 / 0.147 / 1.14 / 0.533 / −33.7%**. Quantum wins in that design: vs MLP **+0.040 (p = 0.006)**, vs NN3 **+0.025 (p = 0.053)**, vs XGBoost and RBF **+0.015 each (p = 0.35 and 0.17)**; the hybrid posts the field's best mean IC (0.0606).
- **Decomposition of the illusion (Section 6.2):** matching the 60 static-universe windows to their nearest point-in-time counterparts (±10 days, 60 pairs) moves **QKRR 0.0512 → 0.0184** and **ridge 0.0567 → 0.0330**; the formal difference-in-differences of the quantum kernel's excess universe sensitivity is **+0.009, p = 0.71, bootstrap 95% CI [−0.039, +0.058]** — the attribution to survivorship specifically **cannot be established at window-level power**, which the source flags itself. Sixty windows "cannot resolve IC differentials of ±0.015"; Holm on the diagnostic eight-pair family leaves nothing significant at **smallest adjusted p = 0.19** (see frontmatter contradiction 5).
- **Interactions (Section 7):** short-study ridge with catalog interactions **0.0531 vs 0.0567** without; poly(2) **0.0470 vs 0.0507** linear top-8; on the extended (main) sample the gaps are **−0.003 (p = 0.33)** and **+0.0004 (p = 0.94)**. `qkrr-x` (interactions admitted to the rotation pool, entering the top-8 in **53% of windows**) scores **0.0199 vs 0.0512** for unmodified `qkrr-fid` — **ΔIC = −0.031, nominal p = 0.032** (does not survive Holm).
- **Bandwidth and geometry mechanism (Section 8):** on the production grid {0.05, 0.1, 0.2, 0.4} validation selects the smallest bandwidth in **24 of 60** short-study windows and the quantum edge over RBF concentrates entirely there (**ΔIC = +0.043** in those windows, ≈0 or negative elsewhere). Re-run on a widened eight-point grid **λ ∈ [0.01, 1.6]**: selections move to interior values (**λ = 0.2 in 16, λ = 0.4 in 13 of 60**), mean validation IC is single-peaked at **0.163 (λ=0.2)**, decaying to **0.123 (λ=0.01)** and collapsing in the concentration regime (**0.104 at 0.8, 0.077 at 1.6**). The regularized geometric difference `g` averages **5.4 (median 3.4, never below 2.4)** yet correlates **ρ = −0.20** with the realized quantum-minus-RBF IC differential.
- **Pooled feature diagnostics (Section 3.3):** momentum × surprise pooled IC **+0.022** against **−0.029** and **+0.007** for its components; lottery × reversal **−0.021** against **+0.08** for both components.
- **Arithmetic self-check performed this run (research-computed from the printed table cells, exit 0 apart from one deliberate tolerance note):** all of the printed deltas above reproduce from the table cells — `0.0254−0.0208 = +0.0046 ≈ +0.005`, `0.0254−0.0477 = −0.0223`, `0.0355−0.0254 = +0.0101`, `0.0494−0.0438 = +0.0056`, `0.0438−0.0254 = +0.0184`, `0.0494−0.0355 = +0.0139`, `0.0512−0.0110 = +0.0402`, `0.0512−0.0366 = +0.0146`, `(0.0512−0.0184)−(0.0567−0.0330) = +0.0091 ≈ +0.009`, `0.0199−0.0512 = −0.0313`, `0.006×8 = 0.048` (contradiction 5). This verifies **transcription and internal arithmetic only**, not the result.

### Independently reproduced

`not independently reproduced`

No backtest, no simulation, no data download, no notebook execution and no portfolio reconstruction was performed for this record. The only actions taken were: reading the pinned arXiv v1 full text end to end, reading the landing page metadata, verifying the DataCite DOI redirect, running read-only repository-wide dedup searches, running read-only Wiki Brain searches, and arithmetic self-checks on the paper's own printed table cells. **No A-share or crypto cross-section was rebuilt, no kernel was trained, and no figure was regenerated.**

### Negative evidence

This is a null-result paper, so most of its content is negative evidence against the quantum-kernel alpha hypothesis; items 1–11 bear on that hypothesis, items 12–21 bear on the pipeline's own alpha content and on reproducibility.

1. On the clean point-in-time protocol the fidelity quantum kernel is statistically indistinguishable from its classical RBF control (**ΔIC = +0.005, p = 0.42**, Wilcoxon p = 0.66) across 170 windows (Table 3, Section 5).
2. It also ties the strongest deep benchmark (`nn3`, p = 0.90) and trails top-8 XGBoost (−0.013, p = 0.16) and plain ridge (−0.022, nominal p = 0.043).
3. After the budget 2×2, nothing separates quantum from classical at either scale: **−0.010 (p = 0.26)** at `N = 1,536` and **−0.006 (p = 0.43)** at `N ≈ 37,800` (Table 4) — the paper's own "sample-efficiency" selling point is removed.
4. **No pairwise difference in the main evaluation survives Holm correction** (smallest adjusted p = 0.43).
5. Penalized linear models take the **top five places on mean IC, in every metric, in every five-year subperiod**; poly(2) expansion is indistinguishable from plain linear (ΔIC = +0.0004, p = 0.94).
6. The apparent quantum edge in the 60-window static-screen study **dissolves** when the universe is rebuilt point-in-time (0.0512 → 0.0184), but ridge falls too (0.0567 → 0.0330) and the difference-in-differences is insignificant (+0.009, p = 0.71, CI [−0.039, +0.058]) — the design lacks the power even to diagnose which ingredient produced the artifact.
7. Sixty windows cannot resolve IC differentials of ±0.015; the "stability" superlatives (ICIR, drawdown) reverse when the sample is extended to 170 windows.
8. The only nominally significant quantum wins in either study are **against neural networks, the model class most starved at this data scale** (MLP p = 0.006, NN3 p = 0.053); against properly regularized linear models the quantum kernel never held a significant advantage in any sample at any budget.
9. Documented interaction anomalies **do not help**: ridge with the catalog scores lower than ridge without it (0.0531 vs 0.0567; −0.003, p = 0.33 on the main sample), and feeding interactions to the quantum rotation pool **actively damages it** (0.0199 vs 0.0512, ΔIC = −0.031, nominal p = 0.032) by displacing stronger primitive signals from scarce qubits.
10. The geometric difference — the necessary-condition screen for quantum advantage — is large in every window (`g` mean 5.4, min 2.4) yet **uncorrelated (ρ = −0.20)** with realized OOS gains: distinct geometry is not better-aligned geometry.
11. The tuned bandwidths that generalize are those whose spectrum is dominated by low-order, classically accessible terms; the genuinely quantum high-order interference regime is exactly where generalization dies (validation IC 0.163 at λ = 0.2 vs 0.077 at λ = 1.6).
12. **Even the best classical model is weak as an implementable strategy:** top mean IC 0.0499 with net Sharpe 0.272 and top-8 ridge 0.306 at a flat 23 bp one-way charge, i.e. the pipeline's own best output is a low-Sharpe, long-only, 20-day-horizon book whose turnover is never reported.
13. Costs are a **single flat proportional assumption**; spread, slippage, impact, latency, fills, participation, borrow, leverage and capacity are all absent from the source → cost realism is `data gap`, and any net-of-cost reading of the Sharpe column inherits that gap.
14. **Portfolio turnover is never reported**, so the 23 bp charge cannot be annualized or stress-tested from the paper alone.
15. **No public code or data artifact**: fourteen notebooks and all intermediate artifacts are "available from the author on request"; there is no repository, no commit and no frozen dataset to verify against.
16. **Sole author, preprint only**: no journal-ref, no publisher DOI, no peer-review statement; the title page says the manuscript is *prepared for submission* to *Quantitative Finance*. Treat every figure as an unreferenced third-party claim.
17. Sample-window statements are mutually inconsistent (2010–2026 data, 2011–2025 panel, 2012–2025 windows, a 2011–2015 subperiod cell) — frontmatter contradiction 1.
18. The multiplicity claim's scope is ambiguous (ten-pair family vs "eleven models"), and the diagnostic-study Holm statement conflicts arithmetically with the MLP comparison — frontmatter contradictions 4 and 5.
19. Table 5 prints only 10 of the described **sixteen** diagnostic models ("Selected models"), so six rows of the field that produced the headline artifact are not visible → `underspecified`.
20. **No hardware and no computational claim**: everything is exact statevector simulation at 8 qubits, explicitly classically computable; nothing here says anything about quantum *hardware* economics, and the source says so.
21. Scope limits acknowledged by the source itself: one market, one horizon (20 days), one feature-map family, long-only (no short leg), neural baselines deliberately not re-tuned per window (Section 9).

## Falsification plan

All thresholds below are **research-defined falsification thresholds** unless the source itself states the number; any operational rule not present in the source is labeled `research-proposed`.

- **F1 - Frozen forward replication.** `research-proposed` re-run of the main protocol (point-in-time A-share pool, 20-day horizon, top-8 rotation, kernel-swap triplet) on the frozen forward window starting **2026-10-01**. **Fail** the source's null if fidelity-minus-RBF ΔIC exceeds **+0.010 with p < 0.05** (research-defined) over the first ≥40 forward windows.
- **F2 - Number reproduction gate.** Independently rebuild Tables 3 and 4 from an independent data vendor. **Fail** transcription of the headline if fidelity QKRR mean IC differs from **0.0254** by more than **0.005 IC**, or ridge (top-8) from **0.0494** by more than **0.005 IC** (research-defined tolerance).
- **F3 - Kernel-swap control.** Reproduce the three-kernel triplet on **identical** stratified `N = 1,536` subsamples, identical solver, identical `(λ, α, γ)` budget. **Fail** the null if the fidelity kernel beats the RBF control by more than **+0.010 IC with p < 0.05** (research-defined) — that would reverse the paper's central claim.
- **F4 - Budget-equalized 2×2.** Reproduce `ridge-sub` / `qkrr-nys` at `N = 1,536` and `N ≈ 37,800`. **Fail** the "no difference at matched budget" claim if any matched cell differs by more than **0.010 IC with p < 0.05** (research-defined).
- **F5 - Universe look-ahead ladder (the artifact test).** Run the same 60-window 2021–2025 evaluation under (a) the static full-sample screen, (b) the point-in-time coverage screen, (c) a `research-proposed` conservative screen with delisting-aware coverage. **Fail** the source's "universe alone cannot be attributed" conclusion if the quantum-minus-ridge difference-in-differences is significant at 5% with |DiD| > 0.010 IC (research-defined) across ≥170 windows.
- **F6 - Window-count power ladder.** Evaluate the diagnostic design at **60, 110 and 170** windows (`research-proposed` grid). **Fail** the artifact diagnosis if the quantum kernel retains best-in-field ICIR/hit rate at ≥170 windows under family-wise correction (research-defined).
- **F7 - Multiplicity over the full family.** Apply Holm (and, `research-proposed`, Benjamini-Hochberg at q < 0.10) over **all** pairwise differences: 55 pairs for the 11 printed main-study models and 120 pairs for the sixteen-model diagnostic field. **Fail** the null if any quantum-vs-classical pair survives at adjusted p < 0.05 (research-defined); conversely **fail** any retained "quantum advantage" claim that does not survive this correction.
- **F8 - Bandwidth-grid robustness.** Re-tune on the widened eight-point grid **λ ∈ [0.01, 1.6]** (as the source does in Section 8) and report interior-versus-endpoint selections. **Fail** the mechanism claim if the quantum edge does not concentrate in the low-order (small-λ) regime and the optimum is not interior (research-defined).
- **F9 - Interaction ablation.** Add/remove the twelve catalog interactions for ridge, poly(2) ridge and the quantum rotation pool under the same IC screen. **Fail** the "interactions help nothing" claim if catalog interactions improve ridge OOS IC by more than **+0.005** with p < 0.05 (research-defined); **fail** the quantum design rule if admitting products *improves* `qkrr-fid`.
- **F10 - Cost ladder (requires measuring turnover first).** `research-proposed` ladder of **0 / 23 / 50 / 100 bp per side** applied to the top-30% equal-weight book, with turnover reported per rebalance. **Fail** implementability of the classical ranking if net Sharpe ≤ 0 at **50 bp per side** (research-defined); report the unprinted turnover and the 23 bp composition as a `data gap` in every case.
- **F11 - Turnover / capacity audit.** Report annual turnover of the top-30% book and the ADV participation implied by equal weighting. **Fail** the flat-cost reading if annual turnover exceeds **500%** (research-defined) or any name requires **> 10% of 20-day ADV** in one session (research-defined).
- **F12 - Long-short (non-long-only) translation.** `research-proposed` decile spread / market-neutral variant to test whether rank IC survives without the A-share shorting constraint. **Fail** the cross-sectional-strength claim if the long-short spread is insignificant (|t| < 1.96, research-defined) while long-only IC stays positive — that would indicate the IC is concentrated in beta/size exposure rather than selection.
- **F13 - Shuffled-label placebo.** Circularly shift or permute forward-return labels within window and re-run the full pipeline. **Fail** the whole pipeline if any model's mean |IC| exceeds the **95th percentile** of the placebo distribution (research-defined).
- **F14 - Crypto port test.** `research-proposed` identical protocol on a point-in-time crypto cross-section (per the source's own nomination of "crypto cross-sections" in Section 9). **Fail** the port if quantum-minus-classical ΔIC ≤ 0 with p ≥ 0.05 over ≥170 windows (research-defined); also fail the port if a point-in-time token universe cannot be constructed at all (listing survivorship), since that is a prerequisite, not a result.

Action on failure: the record stays `research-only`, `not-implemented`, `not-approved`. A failure of F2, F3, F7 or F13 should be reported back to Research Intake Review as grounds for REJECT rather than for retuning; F5, F6 and F7 are the tests that decide whether the artifact anatomy generalizes beyond this paper.

## Crypto portability

**unproven.**

- The source tests **only** Chinese A-share cash equities on a 20-day horizon, long-only, with an A-share-specific shorting constraint; it makes **no crypto performance claim**. Section 9 names "crypto cross-sections" (alongside post-structural-break markets and newly listed assets) as a **natural test bed that remains to be tested**, "provided the protocol standards travel along". That is a nomination, not evidence → `unproven`.
- The hypothesis is at least *portable in form*: the mechanism is a cross-sectional ranking over standardized characteristics with a 20-day (or shorter) horizon, which exists in crypto. But every hard requirement gets harder: a **point-in-time token universe with severe listing survivorship** (the source's entire methodological moral is that universe construction is the largest single lever), 24/7 sessions and UTC candle boundaries instead of exchange sessions, no announcement-date fundamentals at all (the 27-characteristic panel is filing-based), wash-traded volume and spoofed turnover, venue fragmentation across CEXs/DEXs, and far deeper market impact in long-tail names.
- If implemented on **perpetuals**, funding and mark-price mechanics, liquidation and leverage constraints enter and are entirely absent from the source; if implemented on **spot**, borrow/short-leg variants (F12) do not exist at all.
- **Crypto portability is not authorization to trade.** Until F14 runs on a point-in-time crypto cross-section with the four protocol standards intact, any "quantum (or ridge) cross-sectional alpha in crypto" statement derived from this record is an unsupported port.

## Limitations

- **Source quality:** sole-author preprint, "prepared for submission to *Quantitative Finance*", no journal-ref, no publisher DOI, no peer-review statement, no public code or data (materials "on request"). Every performance figure is an unrefereed third-party claim. `not independently reproduced`.
- **Cost model is one flat number:** 23 bp one-way, "proportional"; composition (commission vs spread vs impact) never stated; **no** spread, slippage, market impact, latency, order type, fill model, participation, borrow, leverage, margin, commission, fee schedule or capacity anywhere in the pinned text → all `data gap`, never zero.
- **Portfolio turnover never reported**, so cost claims cannot be annualized or ladder-tested from the source. `data gap`.
- **Execution unspecified:** signal-to-order timing, session/close convention, timezone and fill assumptions are `data gap`; the "tradable" reading of the 0.27–0.31 Sharpe column is not supported by this source.
- **Sample-window inconsistency** across Table 3, Sections 3.1, 3.2, 4.1 and 5 (frontmatter contradiction 1) → the exact evaluation window is `underspecified`.
- **Comparator ambiguity** for the only nominally significant deficit (frontmatter contradiction 3) and **multiplicity-scope ambiguity** (contradictions 4 and 5) → the significance narrative is `underspecified`.
- **Table 5 prints 10 of 16** diagnostic models; six rows are not visible. `underspecified`.
- **One market, one horizon, one feature-map family, long-only;** no holdout beyond the walk-forward design; neural baselines not re-tuned per window (deliberate, but stated by the source as a limitation of comparability).
- **No hardware:** 8-qubit noiseless statevector simulation is classically computable; nothing here speaks to quantum-hardware execution economics.
- **Universe is top-450 by float market cap with a coverage screen** — large/mid-cap A-shares only; small-cap and non-Chinese universes out of scope.
- **Contested:** this record carries `contested: true` with five frontmatter contradictions; none has been reconciled and none should be silently resolved downstream.
- **Incremental-write check:** hidden-inclusive `rg -uuu` found zero existing records citing `2607.20168`, `Junchi Shen`, `Vanishing Advantage`, `QKRR`, `kernel-swap` or `fidelity kernel` (positive control `novy-marx` = 11 files; `coverage_manifest.csv` = 0 hits); read-only Wiki Brain `kb_search` for `quantum kernel finance` returned **0 pages**. No duplicate source identity exists in this repository.

## Implementation status

`implementation_status: not-implemented`.

Nothing has been implemented in our research stack. No A-share or crypto data has been ingested, no characteristic panel rebuilt, no kernel trained, no portfolio constructed, no backtest run, no Qlib full-backtest executed, and no Paper, Testnet or Live workflow touched. This document is a normalized research capture of a third-party preprint plus arithmetic self-checks on its printed tables. The numbers above are source-reported claims with table/section provenance, **not our results**.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this record in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. It also does not mean that the source's internal contradictions have been reconciled, that its null result has been independently reproduced, or that any ridge/poly(2) ranking from Table 3 is implementable after real costs. Any later adoption or implementation decision must be explicit, separately reviewed, and based on this record plus current sources.

## Related Wiki records

Verified adjacent pages (found via read-only `kb_search`; none shares this source identity):

- [[quant/lstm-learnable-sector-embeddings-cross-sectional-reversal-2026-09-02]] — adjacent in that both are cross-sectional equity return rankers with a nonlinear/learned component; differs in source identity, market (US-style cross-section vs A-shares) and in that this record's headline is a **null** for the nonlinear component.
- [[quant/equity-cross-sectional-homological-neural-network-mfcf-ranking-2026-09-02]] — adjacent in that both test an exotic dependence/geometric architecture on cross-sectional equity ranking; differs in mechanism (persistent-homology dependence architecture vs quantum feature-map kernel) and in source.
- [[quant/chronos-foundation-transformer-statistical-arbitrage-factor-residuals-2026-09-12]] — adjacent in that both report turn/cost fragility of a cross-sectional ML ranking; differs in model class, market and source identity.
- [[quant/china-ashare-mask-first-upstream-contamination-adjusted-mse-2026-09-04]] — adjacent in that both are China A-share cross-sectional ML studies with an explicit bias/contamination correction angle; differs in source identity and in the specific bias targeted (upstream label contamination vs universe look-ahead).
- [[quant/llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04]] — adjacent in that both are methodological/honest-evaluation records about how protocol choices manufacture apparent alpha; differs in object (LLM strategy search vs quantum-kernel horse race) and source.

Wiki Brain search for `quantum kernel finance` returned **zero pages**; no Wiki link for this mechanism was fabricated.

Nearest records in this repository (source identity and mechanism differ on every axis; none is a duplicate):

- `gaussian-boson-sampling-asset-clustering-statistical-arbitrage-2026-09-02.md` — different source and mechanism (GBS-based clustering for pairs/stat-arb vs quantum kernel for direct cross-sectional ranking); that record's own ablation asks the same "does the quantum step beat classical greedy search" question.
- `photonic-quantum-annealing-constrained-factor-allocation-qubo-2026-09-04.md` — different source, different object (QUBO portfolio allocation vs cross-sectional return prediction) and different claim.
- `quantum-stochastic-walk-smart-1n-long-only-portfolio-optimizer-2026-09-24.md` — different source and mechanism (quantum-walk-inspired optimizer for 1/N blending vs kernel ridge ranking).
- `geometric-observables-qcml-regime-detection-berry-phase-rate-2026-09-20.md` (arXiv 2605.17117) — different source; quantum-machine geometric phase rate used as a **regime feature** rather than as a cross-sectional kernel.
- `published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23.md` — different source (arXiv 2607.06502) and different null (zoo-level luck adjustment vs a model-class horse race).
- `retail-equity-anomaly-pit-search-aware-falsification-volatility-positive-control-2026-09-27.md` — different source; shares the point-in-time-universe and search-aware-inference axes but on US retail anomalies.
- `china-ashare-factor-library-overfitting-audit-amihud-illiquidity-falsification-2026-09-13.md` and `limt-hierarchical-multitask-liquidity-aware-ashare-cross-sectional-apo-2026-09-23.md` — same market (China A-shares), different sources and different mechanisms.

## Sources

1. Junchi Shen. "Quantum Kernels and the Cross-Section of Stock Returns: Anatomy of a Vanishing Advantage." arXiv preprint `arXiv:2607.20168v1 [q-fin.PR]`, submitted 22 July 2026 14:04:12 UTC; 16 pages, 2 figures, 5 tables; title page "Manuscript prepared for submission to Quantitative Finance"; license: arXiv.org perpetual non-exclusive license. Stable URL: https://arxiv.org/abs/2607.20168 · DOI: https://doi.org/10.48550/arXiv.2607.20168 (checked 2026-09-28).
2. Same paper, pinned full text `https://arxiv.org/html/2607.20168v1`, **189,687 bytes, SHA-256 `7da66a016dab462f2d3ae0fcffc200384714cb113d1b094b3623b6c97e77bafe`**, read end to end 2026-09-28 — primary source for every parameter, table cell, p-value, cost statement and contradiction recorded above (Sections 1–10, Tables 1–5, Figures 1–2 captions, Data and code availability).
3. The paper's cited methodological anchors, **not** read as sources for this record and not used to fill any number here: Havlíček et al. (2019), Schuld and Killoran (2019), Huang et al. (2021) *Power of data in quantum machine learning*, Kübler et al. (2021), Slattery et al. (2023), Shaydulin and Wild (2022), Canatar et al. (2023), Thanasilp et al. (2024), Gu, Kelly and Xiu (2020), Leippold, Wang and Zhou (2022), Kozak, Nagel and Santosh (2020), Williams and Seeger (2001), Chen and Guestrin (2016), Bergholm et al. (2018) (PennyLane).
