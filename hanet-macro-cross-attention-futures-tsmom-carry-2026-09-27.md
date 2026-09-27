---
schema: strategy-research-record-v1
title: "HANET Hierarchical Cross-Attention Macro Conditioning of Futures Time-Series Momentum and Carry"
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - futures
  - time-series-momentum
  - carry
  - macro-conditioning
  - mixed-frequency-attention
  - deep-learning
  - regime-retrieval
  - transaction-cost-sensitivity
status: research-only
confidence: medium
source_as_of: 2026-05-30
sources:
  - "arXiv:2606.00624v1 [q-fin.ST, q-fin.CP], 'Macro-aware time series forecasting via hierarchical mixed-frequency attention models', Daniel Cunha Oliveira, Kieran Wood, Stefan Zohren, Mihai Cucuringu, André Fujita, submitted Sat 30 May 2026 08:56:32 UTC. https://arxiv.org/abs/2606.00624 (DOI in PDF metadata: https://doi.org/10.48550/arXiv.2606.00624)"
  - "Pinned primary PDF: https://arxiv.org/pdf/2606.00624v1 — 3,163,583 bytes, 30 pages, SHA-256 396d2fcb5cf5772698562a4d7bfdba4595b2019af1ebded3cf37e0d6d80d9f5d, downloaded 2026-09-27"
  - "Pinned primary HTML: https://arxiv.org/html/2606.00624v1 — 385,338 bytes, SHA-256 c8ddf0cf0fe2bc37b76e2f5f0e58b9e7b8290675acce59ac2a7444236c11819d, downloaded 2026-09-27"
  - "Author publication page classifying the work as 'arXiv preprint': https://kieranjwood.github.io/publication/hanet (checked 2026-09-27)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# HANET Hierarchical Cross-Attention Macro Conditioning of Futures Time-Series Momentum and Carry

## Provenance

- **Primary source:** arXiv preprint **arXiv:2606.00624v1**, *"Macro-aware time series forecasting via hierarchical mixed-frequency attention models"*, categories `q-fin.ST` (primary) and `q-fin.CP`.
- **Authors (exactly as printed on the PDF title page and in the arXiv API author list):** Daniel Cunha Oliveira (IME-USP, doliveira@ime.usp.br); Kieran Wood (University of Oxford, kieran.wood@eng.ox.ac.uk); Stefan Zohren (University of Oxford, stefan.zohren@eng.ox.ac.uk); Mihai Cucuringu (UCLA; University of Oxford, mihai@math.ucla.edu); André Fujita (IME-USP; Kyushu University, andre.fujita@ime.usp.br). No author is marked with an equal-contribution or corresponding-author footnote in the source → per-author role/correspondence = **data gap**.
- **Version / date:** arXiv submission history shows a single version `[v1] Sat, 30 May 2026 08:56:32 UTC (10,774 KB)`; the `abs` page carries no Comments field, no journal-ref field and no arXiv DOI field, and the arXiv API returns `updated == published == 2026-05-30T08:56:32Z` with `doi` absent → **preprint only, no peer-review or journal publication stated in source** (further corroborated by the first author's publication page, which lists "Publication: arXiv preprint"). The PDF metadata `/DOI` is `https://doi.org/10.48550/arXiv.2606.00624` and `/License` is `http://creativecommons.org/licenses/by/4.0/` (CC BY 4.0, also printed as `License: CC BY 4.0` on the HTML).
- **Pinned artefacts (both downloaded and read end to end on 2026-09-27):**
  - PDF: `https://arxiv.org/pdf/2606.00624v1`, 3,163,583 bytes, 30 pages, SHA-256 `396d2fcb5cf5772698562a4d7bfdba4595b2019af1ebded3cf37e0d6d80d9f5d`, pypdf 6.16.2 metadata authors matching the title block, `/arXivID` = `https://arxiv.org/abs/2606.00624v1`.
  - HTML: `https://arxiv.org/html/2606.00624v1`, 385,338 bytes, SHA-256 `c8ddf0cf0fe2bc37b76e2f5f0e58b9e7b8290675acce59ac2a7444236c11819d`.
  - Both renderings were cross-checked cell by cell for Tables 1–6 and Tables 7–11; all numbers quoted below appear in **both** renderings.
  - Note: the `abs` page lists the v1 submission size as 10,774 KB while the bytes currently served are 3,163,583 → arXiv-side file normalisation/re-generation, **not reconciled** in source; the recorded SHA-256 is of the bytes served on 2026-09-27.
  - Date-line quirk: the PDF title page prints `June 2, 2026` while the HTML body prints `August 24, 2026`, both after an arXiv stamp of `30 May 2026`. These look like render-time `\today` artefacts of the two renderings; the authoritative version date is the arXiv v1 timestamp. Recorded, not reconciled.
- **Primary-source checksum coverage (all read directly from the pinned PDF/HTML, section level):** abstract; §1 Introduction; §2 Related Literature; §3 (incl. §3.1 momentum, §3.2 carry); §4 (incl. §4.1 benchmark LSTM, §4.2 Matching-Network/X-Trend retrieval, §4.3 Hierarchical Attention Network); §5.1 Financial Data; §5.2 Economic Data; §6 Performance Evaluation; §7.1–§7.3; §8 Conclusions; Appendix A (Tables 7–10), Appendix B (Table 11), Appendix C; Tables 1–11; Figures 1–7.
- **Repository deduplication audit (hidden-inclusive, pre-write, 2026-09-27):** ripgrep over the whole checkout with `--hidden -g '!.git'` scanned **2,605 files** (all `*.md`, `coverage_manifest.csv`, `*.json`, `*.txt`, plus `.mimo-worktrees/`, `.agents/`, `.hermes/`) for each of: `2606.00624`, `10.48550/arXiv.2606.00624`, `HANET`, `Daniel Cunha Oliveira`, `hierarchical mixed-frequency`, `macro-aware time series forecasting` → **every pattern returned zero matches before this write**. Secondary identity/adjacency scans: `Kieran Wood` → 2 files (both different arXiv sources, see Related); `FRED-MD` → 1 file (unrelated factor-pricing record); mechanism-level scans `mixed-frequency|macro conditioning|regime-aware attention` → 2 files (both unrelated), `macroeconomic regime|attention over macro|macro context` → 17 files (loose prose mentions; the only mechanism-adjacent records are DeePM and the GPT/sector macro record).
- **Four-axis distinction (why this is not a duplicate):**
  1. *Source identity* — `arXiv:2606.00624` appears nowhere in the repository; adjacent records are `arXiv:2601.05975` (DeePM) and `arXiv:2603.01820` (VSN-LSTM/xLSTM benchmark), different papers by partially overlapping authors.
  2. *Mechanism* — monthly→daily **hierarchical cross-attention retrieval over macro history** conditioning a forecaster, versus DeePM's macro **graph prior + directed-delay causal sieve + SoftMin EVaR portfolio regularisation**, versus a pure cross-asset neural trend benchmark with no macro input.
  3. *Signal construction* — daily network positions for two **time-series** tasks (TSMOM and carry) on futures, versus cross-sectional/graph portfolio construction elsewhere.
  4. *Material data dependency* — **point-in-time FRED-MD macro vintages** (Dec 1959–Jan 2023 panel) as the retrieval key, plus **Pinnacle** futures panel; no other record depends on that combination.

## Economic mechanism

### Source-reported

The authors' stated rationale (§1, §5.2, §8): the binding limit in macro-financial prediction is not the number of daily observations but the **scarcity of distinct macroeconomic regimes**. Conditioning information in existing deep forecasting work is drawn almost exclusively from past prices/returns, with macro data either ignored or appended as a flat feature concatenation to the daily vector — a design the authors argue is restrictive because expected returns vary with the state of the economy. HANET (Hierarchical Attention Network) therefore frames *regime selection as attention over macroeconomic contexts*: queries and keys live on a **monthly macro grid** (PCA of FRED-MD), values keep the **daily** market information, and the resulting monthly attention weights are projected onto the daily grid so day-level signal structure is not discarded. The source reports that this yields better risk-adjusted performance than price-only neural forecasters "particularly during turbulent periods", and that two ablations show the gain comes from *structured* macro conditioning rather than from adding macro features: an LSTM given the same macro PCs by concatenation performs poorly, and shuffling the temporal ordering of the macro PCs substantially degrades performance. Attention weights are additionally presented as an interpretability channel (sparse "Regime Detector" heads vs dense "Global Context" heads; COVID-2020 queries retrieving 2008 contexts, 2022 inflation queries retrieving early-1980s Volcker contexts — §7.3, Figure 7).

### Research interpretation

Stated as a falsifiable hypothesis, not as an established fact:

- **Regime/conditioning component:** historically similar *macro* states (monthly FRED-MD PCAs, retrieved by learned attention over the full macro history) carry transferable information about the *next-day* position in each futures contract. If the macro axis is pure noise, the shuffled-macro control should match the full model; the source reports it does not.
- **Primary signal:** the network's daily score `Ŝ_{t,i} = β′h_{t,i} + b` mapped through a sizing function `φ` (Eq. 24–25), then volatility-scaled. The tradable hypothesis is therefore *"macro-regime-conditioned neural timing of time-series momentum and carry on a multi-asset futures panel beats both classical sign rules and a price-only LSTM out of sample, gross, and survives modest per-trade costs."*
- **Risk/sizing component (not alpha):** 60-day exponentially weighted ex-ante volatility scaling to a fixed annualised target; there is **no stop-loss, no take-profit, no explicit risk layer and no capacity constraint** in the source. The component roles are (Regime: hierarchical cross-attention over monthly macro PCs) + (Signal: daily LSTM/attention forecaster outputs) + (Sizing: volatility scaling). Ablation is the source's own tool for asking whether the regime component contributes; the source does **not** claim every component contributes alpha.
- Everything not printed by the source (thresholds, filters, execution timing, cost ladder acceptance cutoffs below) is labelled **research-proposed** or **research-defined**.

## Signal

- **Formation timestamp:** daily, at the futures exchange settle. §5.1: Pinnacle's `close` is the exchange settle price and is "the end-of-day reference for return construction", and "all features used at time `t` can be formed from information available up to the end of day `t`". Timezone/session convention beyond "exchange settle" is **not stated in source**. Macro inputs are monthly; §5.2 claims each monthly vintage reflects only information observable at that month (point-in-time, publication lags and revisions accounted for) — **source-reported, not independently verified**.
- **Lookback:** sequence length **84 days** (Table 11), "Days per Context 21 days", "Context Months **all available**" (Table 11); macro context in §7.3 runs from January 1980 to the end of the sample (44-year macro matrix). Warm-up/endpoint inclusivity conventions: **not stated in source** (data gap).
- **Inputs (features):** §4.1 defines `x_{t,i}` only generically — "may include both asset-specific signals and macro features replicated across assets". Section 3 defines the candidate signals that are used *both* as network inputs and as benchmarks: MACD (Eq. 3–5), lagged cumulative returns `R^(k) = P_t/P_{t-k} − 1` (Eq. 6–8), carry (Eq. 9–13), and carry/vol (Eq. 14). **The exact final feature vector, its window set `𝒦`, and the number of retained macro PCs `K` used by HANET are not printed** → signal is **partially underspecified**. (Table 2's caption states the *LSTM concatenation ablation* uses "the first five principal components"; it does not state that HANET uses five.)
- **Entry / exit / direction:** the forecaster emits a continuous score per asset per day; `w_{t,i} = φ(Ŝ_{t,i})` with `φ: ℝ → [−1,1]` (Eq. 25), then `w̃_{t,i} = w_{t,i} · σ_tgt / σ̂_{t,i}` (Eq. 38). Table 11 documents two possible output activations — `tanh (LS)` and `sigmoid (LO)` — and Appendix B says the long-only-vs-long-short mode was logged per run, **but the mode used for the reported results is never printed** → **data gap**; the record therefore does not assert a short book. There is no stop, no take-profit and no time-based exit; positions are simply replaced when the model re-emits (position reversal is what "Hold (Days)" measures).
- **Holding period (source-reported):** mean holding **3 days** for the momentum task and **22 days** for the carry task (Tables 1 and 4), against 5 (LSTM), 34–36 (Lag/MACD rules) and 217 days (passive buy-and-hold).
- **Portfolio aggregation:** §6 Eq. (39) gives `R^{port}_{t+1,j} = w̃′_{t,j} r_{t+1,j}` for the network portfolio, whereas Eq. (2) defines the benchmark time-series strategy return as `(1/m) Σ_i R_{t+1,i}`. The scaling/normalisation convention that reconciles the two is **not printed** → **underspecified**.
- **Parameters (all source-reported, Table 11, p.25):** LSTM hidden `{30, 60}`; HANET output-LSTM hidden `{30, 60}`; FFNN hidden `{25, 50, 100}`; hierarchical cross-attention heads `{2, 5}`; self-attention heads `{2, 5}`; layers `1`; ticker embedding `{25, 50, 100}`; dropout `0.3` (variational or regular); layer norm and residuals on for HANET; initial attention temperature `0.1`; output activation `tanh (LS) / sigmoid (LO)`; Adam, LR `1e-3`, **seq-to-seq Sharpe loss**, batch 32 with 4 gradient-accumulation steps (effective 128), max grad norm 1.0, mixed precision (CUDA only); sequence length 84 days, days per context 21, context months all available, epochs 200, early-stopping patience 20, validation split 20%, **initial in-sample window 252×15 days**, **walk-forward step 252×5 days**, **seed trials 100**, **top-10%-of-seeds ensemble** for both HANET and the LSTM benchmark. No hyperparameter is described as tuned on the test set, but the seed-selection rule and its evaluation basis are not explained beyond Table 11 → selection-bias **data gap**.
- **Benchmarks compared (source-reported):** passive buy-and-hold; `Lag(264)` sign rule; `MACD(8, 96)` sign rule; a shared-parameter LSTM benchmark; carry sign rule (carry task only); plus ablations `LSTM Macro PCA Augmented` and `HANET Shuffled Macro PCA`. The construction/rebalancing of the "Passive Buy-and-Hold (Bench.)" row is **not described anywhere in the paper** → data gap. No comparison to published Momentum Transformer / Deep Momentum Network / X-Trend numbers on this data.

## Required data

- **Instrument / universe (source-reported):** "We select **55 contracts** spanning commodities, bonds, currencies, and equity indices from the larger universe covered by Pinnacle" (§5.1). Appendix A actually prints **51 rows / 50 unique Pinnacle tickers** — Table 7 commodities 23 rows, Table 8 bonds/rates 9, Table 9 FX 7, Table 10 equity/index 12 — with `ZA` (Palladium) listed in **both** Table 7 and Table 10. The claimed 55 vs the printed 50 unique tickers is **not reconciled** in source (see Negative evidence).
- **Venue / market type:** exchange-traded futures (and for FX, Pinnacle spot + interest-rate series used to proxy a 3-month forward). Market type = futures/forwards; **no crypto, no equities cash, no options**.
- **Timeframe / fields:** daily open, high, low, close/settle, volume, open interest (§5.1); ratio-adjusted continuously linked series (`.RAD`, built with Pinnacle's `DMAKERW`) for momentum and carry; futures curve (near + deferred) for equity carry (front vs second) and commodity carry (front vs same-calendar-month contract one year later); FX spot + 3-month forward proxy.
- **Exclusions (source-reported):** bond futures are **excluded from the carry experiments** because only the futures curve is observable in the data environment (§3.2, §5.1) — carry results are therefore on a smaller panel than momentum results; the panel composition per task is not printed (data gap).
- **Macro data:** FRED-MD (McCracken & Ng 2016), monthly, **point-in-time vintages** (source-reported), "our version of the dataset contains **127 variables**" across Output/Income, Consumption-Orders-Inventories, Labor, Housing, Money-and-Credit, Prices; **interest-rate and exchange-rate variables excluded**; "sample spans **December 1959 to January 2023**". Whether 127 is the count before or after the exclusions is not stated (data gap). PCA loadings `U_K` are fit **on training data only and held fixed**, with validation/test months projected onto them (§5.2) — a leakage control the source states explicitly.
- **Point-in-time / availability:** macro vintages claimed aligned to information available at each forecast date; `K` (number of PCs HANET attends over) not stated; futures index/point-in-time membership rules not applicable (non-index panel); **the macro panel is stated to end January 2023 while the reported out-of-sample window ends 2024**, and §7.3 describes a 44-year macro matrix starting January 1980 — the three statements are mutually inconsistent and are **not reconciled** in source.
- **Missing data:** null/stale/suspended/bad-print handling, roll calendar, contract-expiry rules and imputation policy → **not stated in source** (data gap; imputation is forbidden by default in our own reading of the spec).

## Execution assumptions

- **Signal-to-order:** daily EOD settle formation; **execution price, order type, fill model and latency are not stated in source** → data gap. Whether positions are struck at the same settle or the next session's open is **not stated** → same-bar vs next-bar = **data gap**.
- **Fees / spread / slippage / impact:** §6 states verbatim that "Transaction costs can be included as a penalty term, though **in the baseline analysis we set them to zero**." All headline Tables 1, 2, 4, 5 are labelled **Gross**. The source's only cost model is the post-hoc symmetric per-trade ladder in Tables 3 and 6.
- **Cost ladder (source-reported, Table 3 p.15 for momentum, Table 6 p.18 for carry):** per-round-trip cost of 0 / 0.1 / 0.5 / 1 / 2 / 5 / 10 bps applied to **4,622** (momentum) and **4,645** (carry) round-trip trades over the 2005–2024 out-of-sample period.
- **Turnover / capacity / ADV / participation:** no turnover ratio, no participation or ADV cap, no capacity statement, no borrow/financing/leverage/margin assumptions, no partial-fill or failure handling → **every one of these is a data gap, never zero**.
- **Funding / liquidation:** not applicable to the source's futures panel and not modelled; not applicable to crypto in this record (see Crypto portability).
- Any execution choice made by us rather than the source (e.g. next-open execution, a specific fee schedule) is **research-proposed**.

## Evidence

### Source-reported

All figures below are third-party claims from `arXiv:2606.00624v1`, **gross of transaction costs** unless the row says otherwise, over the **2005–2024 out-of-sample period**, all portfolios **volatility-targeted to 10% annualised** (table captions), and **not independently reproduced**.

**Table 1 (p.13), time-series momentum, gross:**

| Strategy | Mean % | Std % | SR | Sortino | MDD % | Hold (d) | t-stat₁ | ρ | IR | t-stat₂ |
|---|---|---|---|---|---|---|---|---|---|---|
| Passive Buy-and-Hold (bench.) | 2.88 | 10.47 | 0.28 | 0.37 | −34.73 | 217 | 1.28 | 1.00 | – | – |
| Lag(264) | 3.52 | 10.47 | 0.34 | 0.48 | −28.85 | 34 | 1.44 | 0.12 | 0.05 | 0.19 |
| MACD(8, 96) | 2.26 | 10.77 | 0.21 | 0.30 | −28.39 | 36 | 0.75 | −0.09 | −0.04 | −0.16 |
| LSTM Benchmark | 13.73 | 11.52 | 1.19 | 1.61 | −14.16 | 5 | 5.37 | 0.22 | 0.83 | 3.44 |
| **HANET** | **22.45** | 11.31 | **1.99** | 2.50 | −15.87 | 3 | 8.78 | 0.35 | 1.72 | 7.04 |

`t-stat₁` = mean-return t-statistic; `t-stat₂` = Newey–West HAC t-statistic of active returns vs the passive benchmark; `IR` = annualised information ratio (Table 1 caption).

**Table 2 (p.15), momentum ablation, gross:** LSTM Benchmark 13.73 / 11.52 / **1.19** / 1.61 / −14.16; LSTM Macro PCA Augmented 0.64 / 11.46 / **0.06** / 0.07 / −25.82; HANET 22.45 / 11.31 / **1.99** / 2.50 / −15.87; HANET Shuffled Macro PCA 9.41 / 11.59 / **0.81** / 0.98 / −16.90.

**Table 3 (p.15), momentum cost sensitivity (HANET):** cost bps → net SR: 0.00 → **1.958** (gross), 0.10 → 1.923, 0.50 → 1.780, 1.00 → 1.601, 2.00 → 1.244, 5.00 → **0.171**, 10.00 → **−1.608**; 4,622 round-trip trades. (The ladder's gross SR is printed as 1.958 while Table 1 prints 1.99 — rounding/denominator difference, **not reconciled** in source.)

**Table 4 (p.17), time-series carry, gross:**

| Strategy | Mean % | Std % | SR | Sortino | MDD % | Hold (d) | t-stat₁ | ρ | IR | t-stat₂ |
|---|---|---|---|---|---|---|---|---|---|---|
| Passive Buy-and-Hold (bench.) | 2.48 | 10.49 | 0.24 | 0.32 | −34.86 | 217 | 1.22 | 1.00 | – | – |
| Carry (classical) | 6.49 | 10.40 | 0.62 | 0.93 | −27.16 | 30 | 2.38 | −0.25 | 0.24 | 1.00 |
| LSTM Benchmark | 7.80 | 10.27 | 0.76 | 1.08 | −21.78 | 27 | 3.31 | 0.52 | 0.73 | 2.99 |
| **HANET** | **9.49** | 10.43 | **0.91** | 1.28 | **−17.71** | 22 | 3.68 | 0.65 | 0.89 | 3.68 |

**Table 5 (p.18), carry ablation, gross:** LSTM Benchmark **0.76** SR; LSTM Macro PCA Augmented **−0.17** SR (MDD −52.18); HANET **0.91** SR; HANET Shuffled Macro PCA **0.12** SR (MDD −34.59).

**Table 6 (p.18), carry cost sensitivity (HANET):** 0.00 → **0.913** (gross), 0.10 → 0.910, 0.50 → 0.897, 1.00 → 0.881, 2.00 → 0.850, 5.00 → 0.756, 10.00 → **0.599**; 4,645 round-trip trades.

**Tables 7–11 (pp.23–25):** universe ticker lists and full experimental configuration (quoted in Signal / Required data above). **Figures 3 and 5** show the cumulative-return/drawdown paths; §7.1 prose states HANET pulls away from the LSTM "especially after 2014". **Figure 7 / Appendix C** are the attention-heat-map interpretability exhibits.

Provenance for every number above: `arXiv:2606.00624v1` PDF pages 13, 15, 17, 18, 23–25 (identical values re-extracted cell by cell from the pinned HTML rendering).

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Every headline number is gross.** §6 sets the transaction-cost penalty to zero in the baseline; only Tables 3 and 6 model costs at all, and they are post-hoc.
2. **Momentum collapses under realistic costs.** Table 3: net SR 1.244 at 2 bps, **0.171 at 5 bps**, **−1.608 at 10 bps** on 4,622 round trips — the momentum claim survives only a very tight cost assumption.
3. **Very high turnover.** Mean holding of **3 days** (momentum) means the strategy is close to a daily re-strike book; the source reports trade counts but **no turnover ratio and no capacity/ADV analysis**.
4. **Macro can hurt badly when wired in naively.** Table 2: LSTM + concatenated macro PCs → SR **0.06** (worse than the 1.19 macro-free LSTM); Table 5: SR **−0.17**, MDD **−52.18%**. The same information is claimed to be the source of HANET's edge, so the result is architecture-conditional, not information-conditional.
5. **Shuffled-macro control is still far above the naive model but below the plain LSTM on momentum.** Table 2: shuffled SR **0.81** vs full **1.99** vs macro-free LSTM **1.19** → macro ordering accounts for much of the gain, and the architecture effect is not cleanly isolated; §7.1 itself says the shuffled variant "still outperforms the naive LSTM+PCA augmentation".
6. **Drawdown trade-off on momentum.** HANET MDD **−15.87%** is *worse* than the LSTM benchmark's **−14.16%** (Table 1); the source concedes the ~1.7pp give-up.
7. **No significance test for the HANET-vs-LSTM difference.** Reported t-stats are for own means and active returns vs the passive benchmark; there is no test of the *difference* between models, no confidence interval on any Sharpe, no seed dispersion, and no multiplicity control over 2 tasks × 5–6 strategies × 6 metrics.
8. **Seed-selection layer.** Table 11: **100 seed trials** with a **top-10%-of-seeds ensemble** for both models. Which set the top decile was selected on (validation vs test) is not stated → selection-bias **data gap**; the reported point estimates may be conditional on favourable seeds.
9. **Universe count mismatch.** §5.1 claims **55 contracts**; Appendix A prints **51 rows / 50 unique tickers** with `ZA` duplicated across Tables 7 and 10 → the traded panel is not reproducible from the paper.
10. **Volatility-target inconsistency.** §3 states "we take `σ_tgt = 15%` in our experiments" while Tables 1–6 and Figures 3–6 are labelled "volatility-targeted (10% annualized)" → the risk target actually used is ambiguous.
11. **Macro sample / out-of-sample window conflict.** §5.2 says the macro panel spans Dec 1959–Jan 2023, §7.3 says the macro matrix covers 44 years from January 1980, and the results window is 2005–2024. Macro inputs for 2023–2024 are therefore **undefined in source** (data gap), and the vintages actually used cannot be reconstructed.
12. **Direction of the book is not printed.** Table 11 documents both `tanh (LS)` and `sigmoid (LO)` output modes and Appendix B says the mode was logged, but no table states which mode produced Tables 1–6.
13. **Portfolio-aggregation convention differs between Eq. (2) (`1/m` average) and Eq. (39) (`w̃′r`)** with no reconciliation → gross returns are not independently recomputable.
14. **Benchmarks partially unspecified.** The passive buy-and-hold construction (weights, rebalance, contract set) is never described; `Lag(264)` and `MACD(8,96)` are the only rule-based comparators, and there is **no head-to-head against published Momentum Transformer / DMN / X-Trend results** on any comparable data.
15. **No code, no data, no availability statement.** `github`, `code availability`, `data availability`, `reproduc` all return **zero hits** in the pinned PDF; the underlying Pinnacle panel is a **commercial** database. Independent reproduction is currently blocked (data gap).
16. **Carry panel silently differs from momentum panel** (bonds excluded, §3.2/§5.1) while Tables 1 and 4 are presented side by side; per-task panel composition is not printed.
17. **Single reported out-of-sample window (2005–2024), no subperiod or regime table.** Prose only ("pulling away especially after 2014"); no decade/regime breakdown, no walk-forward dispersion, no crisis-window stress numbers.
18. **The source's own conclusion lists the missing robustness work** (§8): "future work should stress test HANET under alternative evaluation protocols, including walk-forward re-estimation, stricter non-overlapping regime splits, and transaction-cost aware objectives".
19. **Point-in-time macro claim is unverified.** FRED-MD vintages are real (ALFRED), but the paper gives no vintage identifier, retrieval date or reconstruction recipe; the claim is source-reported only.
20. **Statistical/benchmark composition concerns:** the passive benchmark itself has SR 0.28–0.24 with ρ=0.35 (momentum) to 0.65 (carry), so a material share of HANET's return is directional market exposure rather than timing; the source reports IR (1.72 / 0.89) but no beta-hedged variant.
21. **Publication/selection status:** preprint only, not peer reviewed, no journal-ref, no independent replication, and render-time date artefacts (PDF `June 2, 2026` vs HTML `August 24, 2026` vs submission `30 May 2026`) that are not explained.
22. **None identified in the reviewed external sources** for direct refutations of this paper: it is May 2026 work and no citing replication, comment or failure report was found in the searches run on 2026-09-27; absence is not evidence of no negative result.

## Falsification plan

Every threshold in F1–F13 is a **research-defined falsification threshold** (not from the source); every construction choice is **research-proposed**. Failure action for all tests: mark the hypothesis falsified for this record and do not advance it to a production candidate.

- **F1 — Frozen forward replication (decisive).** Rebuild the pipeline with point-in-time FRED-MD vintages and an independent futures panel (e.g. a different vendor or public data with rolled contracts), freeze all hyperparameters from Table 11, and run 2005–2024 plus a 2025–2026 holdback. **Pass** requires HANET's gross SR to exceed the price-only LSTM by **≥0.30** on the momentum task and **≥0.10** on the carry task in the holdback, with a **Newey-West t ≥ 1.96** on the difference of daily returns. **Fail** if the gap is ≤ 0 or insignificant.
- **F2 — Cost ladder (decisive for tradability).** Apply 0/1/2/5/10/20 bps per round trip plus a commission model. **Fail** if momentum net SR < **0.80** at 2 bps or < **0.50** at 5 bps (the source's own Table 3 gives 1.244 and 0.171, so 5 bps is expected to fail — pre-registering it makes the failure informative rather than rescuable).
- **F3 — Turnover / capacity audit.** Compute one-way turnover and 10%-ADV participation for each of the 55/50 contracts. **Fail** if required turnover exceeds **500% per year** or any contract needs >10% of ADV at the reported position scale.
- **F4 — Decisive mechanism ablation (three-way).** Full HANET vs macro-free LSTM vs shuffled-macro HANET vs naive-concat LSTM, all at identical seeds/ensembles. **Pass** requires full − shuffled SR gap ≥ **0.50** (momentum) and ≥ **0.30** (carry), *and* full − macro-free ≥ **0.30**. Otherwise the macro-retrieval mechanism is not carrying the result.
- **F5 — Seed-selection audit.** Report the full distribution across all **100** seeds (median, IQR, worst decile), not just the top-10% ensemble, with the selection set explicitly identified. **Fail** if the all-seed median SR is < **60%** of the reported ensemble SR, or if selection was performed on the test window.
- **F6 — Point-in-time / leakage audit.** Verify (a) macro vintages match ALFRED publication dates, (b) PCA loadings fit on training data only, (c) no feature uses information after the settle timestamp, (d) the 2023–2024 macro gap is resolved with real vintages. **Fail** on any leak, or if macro inputs for 2023–2024 cannot be reproduced.
- **F7 — Universe and specification reproducibility gate.** Reconcile 55 vs 50 unique tickers, `σ_tgt` 15% vs 10%, LS vs LO mode, and the Eq. (2)/Eq. (39) aggregation. **Fail** if the panel and gross return series cannot be reconstructed from the paper plus its appendices.
- **F8 — Permutation null.** Circular-shift the macro PC series by 1,000 random offsets (preserving autocorrelation) and re-run the headline metric. **Fail** if the real full-model SR is not above the **95th percentile** of the null distribution.
- **F9 — Multiplicity control.** Benjamini–Hochberg `q < 0.10` across 2 tasks × 6 strategies × 6 metrics. **Fail** if no HANET contrast survives.
- **F10 — Baseline horse race.** Compare against published-family baselines (Deep Momentum Network, Momentum Transformer/X-Trend) implemented on the same panel and window. **Fail** if HANET is not in the **top-2** by gross SR on either task.
- **F11 — Subperiod / regime stability.** 2005–2012, 2013–2016, 2017–2024 (plus the 2008, 2020, 2022 episodes). **Fail** if HANET underperforms the macro-free LSTM in **any** subperiod, or if the full-sample gain is driven by a single window.
- **F12 — 12-month reproducibility gate.** With code and a licensed/independent data panel, results must land within **±20%** of the reported gross SR (1.99 momentum / 0.91 carry). **Fail** otherwise.
- **F13 — Crypto port gate.** Only if F1–F4 pass: port the macro-retrieval conditioning to a crypto perp/spot panel, with Newey-West `t ≥ 1.96` and net SR ≥ **0.30** after 10 bps plus funding. **Fail** = crypto portability stays `unproven`.

## Crypto portability

**unproven.**

The source contains **zero crypto evidence**: the panel is exchange-traded commodity, bond, FX and equity-index futures (Pinnacle), the conditioning key is US FRED-MD macro vintages, and the trading model is daily-settle futures with no funding, no mark/index price, no liquidation, no leverage/margin mechanics and no 24/7 session. Porting would require at minimum: a crypto-specific low-frequency conditioning panel (FRED-MD is a US-real-economy vintage set with no crypto counterpart), a decision on whether macro regimes transfer at all to a 24/7 asset, venue-fragmented candles with UTC boundary conventions, funding/liquidation economics for any perpetual leg, and an execution model for a book with 3-day average holding. This record therefore treats the mechanism as a **ported hypothesis**, not as crypto empirical evidence; `direct` or `adapted` is explicitly **not** claimed. Crypto portability is not authorization to trade.

## Limitations

- `underspecified`: final feature vector and macro PC count `K`; long-only vs long-short output mode; portfolio aggregation convention; passive-benchmark construction; execution price/order type/fill model; missing-data policy; per-task panel composition; seed-selection evaluation set; turnover, capacity and participation.
- `data gap`: 55-vs-50 universe count; `σ_tgt` 15%-vs-10%; macro panel end (Jan 2023) vs results window (to 2024) vs the 44-year/1980 matrix description; whether "127 variables" is pre- or post-exclusion; arXiv v1 listed size vs served bytes; render-time date lines; code and data availability (no statement exists in source).
- `not independently reproduced`: all reported performance, ablations and cost ladders.
- `unproven`: crypto portability; the causal reading of the attention-heat-map narratives (§7.3 is explicitly interpretive: "suggest", "appear").
- Source-quality: preprint, not peer reviewed, single test window, no multiplicity control, commercial data dependency, authors' own stated future work includes the missing robustness checks.
- Incremental-write / dedup: the economic mechanism and signal construction are recorded here for the first time in this repository (pre-write scans above); if a later run finds the same source already captured, this record should be updated rather than duplicated.

## Implementation status

`implementation_status: not-implemented`. Nothing in this record has been implemented in our research stack: no code was written, no data was acquired (the Pinnacle panel is commercial), no backtest, walk-forward, paper, testnet or live run was performed, and no Wiki Brain record, candidate-pool entry, Qlib run, Kanban task or strategy family was created by this capture. The strategy exists only as source-reported research material.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. The presence of this record does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, Paper, Testnet or Live. All third-party results above are `source-reported` and were **not independently reproduced**. Any operational rule not printed by the source (execution timing, cost acceptance cutoffs, falsification thresholds) is `research-proposed` / `research-defined` and carries no authority.

## Related Wiki records

Pre-write `kb_read` resolution of the canonical specification: `quant/strategy-research-record-spec-v1.md` → 10,289 bytes, SHA-256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`; `quant/strategy-research-record-spec-v2.md` → file not found, so **v1 remains canonical**. Read-only; no Wiki Brain write was performed.

`kb_search("macro regime attention deep learning futures momentum carry")` returned 2 verified pages, both linked here; `kb_search("DeePM macro graph prior portfolio regime robust")` returned 0 pages, so no DeePM page is linked:

- [[quant/cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02]] — mechanism-adjacent: cross-asset futures timing under end-to-end Sharpe optimisation, but with **no macro conditioning** (different mechanism and data dependency).
- [[quant/equity-cross-regime-bayesian-optimisation-xgboost-tabnet-hybrid-2026-09-02]] — mechanism-adjacent: cross-regime model selection, equity universe, **no attention retrieval and no macro-vintage key**.

Repository-adjacent records (same repository, **not** Wiki links, different source identities and mechanisms): `deepm-regime-robust-macro-graph-causal-sieve-evar-2026-09-03` (arXiv:2601.05975, DeePM — macro *graph prior* + causal sieve + EVaR, portfolio regularisation rather than forecast conditioning) and `cross-asset-futures-vsn-xlstm-sharpe-optimal-portfolio-2026-09-03` (arXiv:2603.01820 — futures neural trend benchmark with no macro input). Both are by partially overlapping authors (Wood/Zohren), which is exactly why the four-axis distinction in Provenance is stated explicitly.

## Sources

1. Daniel Cunha Oliveira, Kieran Wood, Stefan Zohren, Mihai Cucuringu, André Fujita, *"Macro-aware time series forecasting via hierarchical mixed-frequency attention models"*, **arXiv:2606.00624v1 [q-fin.ST, q-fin.CP]**, submitted 30 May 2026 08:56:32 UTC, CC BY 4.0. Landing page: https://arxiv.org/abs/2606.00624 — DOI (from PDF metadata): https://doi.org/10.48550/arXiv.2606.00624.
2. Pinned full text (primary source for every field in this record), PDF: https://arxiv.org/pdf/2606.00624v1 — 3,163,583 bytes, 30 pages, SHA-256 `396d2fcb5cf5772698562a4d7bfdba4595b2019af1ebded3cf37e0d6d80d9f5d`, downloaded 2026-09-27; sections §1–§8, Appendices A–C, Tables 1–11, Figures 1–7 read directly.
3. Pinned full text (HTML rendering used for cell-level cross-checking): https://arxiv.org/html/2606.00624v1 — 385,338 bytes, SHA-256 `c8ddf0cf0fe2bc37b76e2f5f0e58b9e7b8290675acce59ac2a7444236c11819d`, downloaded 2026-09-27.
4. Author publication page (used only to corroborate preprint-only status): https://kieranjwood.github.io/publication/hanet — checked 2026-09-27.
5. References *cited by the source* for the benchmark signal definitions (not read independently for this record): Baz, Granger, Harvey, Le Roux & Rattray (2015) *"Dissecting investment strategies in the cross section and time series"*; Moskowitz, Ooi & Pedersen (2012) *"Time series momentum"*, JFE 104(2); Vinyals et al. (2016) *Matching Networks*; Wood et al. (2021) *Momentum Transformer*; Wood et al. (2024) *X-Trend*; Lim & Zohren (2019) *Deep Momentum Network*; McCracken & Ng (2016) *FRED-MD*; Wood, Roberts & Zohren (2026) *DeePM* (arXiv:2601.05975).
