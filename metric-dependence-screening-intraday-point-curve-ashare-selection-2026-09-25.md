---
schema: strategy-research-record-v1
title: "Metric Dependence Screening (MDS): Intraday Point-Curve Covariates for Large-Universe A-Share Asset Selection (arXiv:2605.02326)"
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional
  - asset-selection
  - portfolio-construction
  - high-frequency-data
  - intraday-volatility
  - china-a-share
  - screening
status: research-only
confidence: medium
source_as_of: "2026-05-10 (arXiv v2 revision date); empirical sample through 2025-12-31"
sources:
  - https://arxiv.org/abs/2605.02326
  - https://arxiv.org/html/2605.02326v2
  - https://arxiv.org/pdf/2605.02326v2
  - https://doi.org/10.48550/arXiv.2605.02326
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Metric Dependence Screening (MDS): Intraday Point-Curve Covariates for Large-Universe A-Share Asset Selection (arXiv:2605.02326)

## Provenance

- **Primary Source:** *Large-Scale Asset Selection via Metric Dependence with Enriched High Frequency Information*, arXiv:2605.02326.
- **Complete author list (exactly as printed):** Yangzhou Chen (Department of Statistics and Data Science, Southern University of Science and Technology, Shenzhen; note "contributed equally"), Shuaida He (School of Computing and Data Science, The University of Hong Kong; note "contributed equally"), Xin Chen (Department of Statistics and Data Science, Southern University of Science and Technology; `chenx8@sustech.edu.cn`, corresponding author).
- **Version / dates:** v1 Monday 4 May 2026 08:26:39 UTC (82 KB source); v2 Sunday 10 May 2026 11:29:59 UTC (83 KB source) is the latest version as of 2026-09-25 (abs submission history, submitted by Yangzhou Chen). Pinned masthead: `arXiv:2605.02326v2 [stat.AP] 10 May 2026`.
- **Categories:** primary `stat.AP` (Applications, Statistics); cross-list `q-fin.PM` (Portfolio Management).
- **Publication status:** `Comments`, `Journal-ref` and publisher-DOI cells are all empty on the abs page, and no peer-review statement appears in the pinned text → **preprint only**, peer-review status a **data gap**. DataCite DOI [10.48550/arXiv.2605.02326](https://doi.org/10.48550/arXiv.2605.02326) followed with redirects returns final HTTP 200 on the arXiv abs page (checked 2026-09-25).
- **License:** Creative Commons Attribution 4.0 International (`CC BY 4.0`), read from the abs-page license cell → text here is normalized and cited, not reproduced wholesale.
- **Pinned primary snapshot (read 2026-09-25):**
  - HTML: `https://arxiv.org/html/2605.02326v2`, **638,067 bytes**, SHA-256 `7e1c924d348e7b83a108b66f05a43c25591e8344fcea3df715042c279ac849c3`, stripped to **96,789 characters / 3,497 lines**. Read line by line: Sections 1–3 and 5–6, Theorems 1–3, Assumptions 1–7, Tables 6–7, Figures 1–2 captions, References. Section 4 (simulation) design text read in full; the numeric cells of simulation Tables 1–5 were sampled, not exhaustively transcribed (**stated as a gap rather than claimed as full coverage**). arXiv site-footer boilerplate was excluded from all keyword scans.
  - PDF: `https://arxiv.org/pdf/2605.02326v2`, **317,562 bytes**, SHA-256 `8c6fb2503754c4ef8bb27f31461ccbfea7c7838ad90e2eb7b8926ea3b378dafd`.
- **Code / replication:** no GitHub/GitLab URL, no code-availability and no data-availability statement anywhere in the pinned text (**data gap**).
- **Data vendor:** the source names the market ("all A shares listed on the Shanghai and Shenzhen exchanges") and the sampling grids (1-minute returns, 5-minute prices) but **no data vendor** (**data gap**).
- **Pre-write source-identity dedup (2026-09-25, repo-wide, hidden-inclusive):** ripgrep across all `*.md` (including `.mimo-worktrees`, `.agents`, `.hermes`) plus `coverage_manifest.csv` for `2605.02326`, `10.48550/arXiv.2605.02326`, `arxiv.org/(abs|html|pdf)/2605.02326`, `Large-Scale Asset Selection`, `Metric Dependence Screening`, `metric dependence`, `\bMDS\b`, `point-curve`, `Yangzhou`, `Shuaida`, `Xin Chen`, `D-SEVIS`, `sure screening`, `screening stage` → **0 hits before this write** (manifest 0 hits too). The only `Fréchet` hit in the repo is `temperature-anomaly-climate-risk-exposure-cev-mopso-portfolio-2026-09-23.md` (1 occurrence, unrelated climate-exposure mechanism) and it was cleared as a family neighbour.

## Economic mechanism

### Source-reported

The paper's first-stage screening problem is portfolio construction, not return prediction: large-universe mean-variance allocation is dominated by estimation error, so the investable universe is reduced before any optimizer runs. Existing screening rules (SIS, SIRS, DC-SIS, and the dependence screening score of Wang et al. 2022, called D-SEVIS in the paper) rank assets from **scalar** daily returns or low-dimensional high-frequency summaries, which discards within-day risk dynamics.

MDS replaces that scalar covariate with an **object-valued** one. For stock *i* on day *t* the covariate is the point-curve object $X_{i,t}=(R_{i,t}, v_{i,t})$: the daily return paired with the latent intraday **spot-volatility curve** $v_{i,t}(u)=\sigma_{i,t}(u)$ over the intraday domain, under the product metric $d_X^2(x,x')=(r-r')^2+\sum_j (v_j-v'_j)^2$ (empirical normalized form, grid weight fixed at 1 across all windows and methods). The conditioning variable is a one-dimensional **risk-adjusted target series** $Y_t$ built, following Wang et al. (2022), by sorting all stocks each day on a market-adjusted high-frequency Sharpe ratio $SR_{i,t}=(R_{i,t}-R_{M,t})/\sqrt{RV_{i,t}}$, taking the $q=\lfloor 0.1p\rfloor$ largest **positive** ratios, and value-weighting their daily returns by market capitalisation (stocks with no intraday trades that day get $SR=-\infty$).

The ranking statistic is a **Fréchet explained-variation coefficient** $\rho = 1 - \mathbb{E}[V(Y)]/V_F \in [0,1]$: how much conditioning on the target (approximated by an $H$-cell partition of $Y$) reduces the metric dispersion of each asset's point-curve object. The estimator $\hat\rho_n^k$ is computed per asset over the estimation window; assets are ranked descending and the top $d$ names form the reduced universe. A second-stage long-only portfolio (equal weight, score-squared weight, or constrained global minimum-variance with sample or shrinkage covariance) is then built on the selected set.

Stated source claims: the point-curve construction "captures risk state information that is not visible from a single daily return"; preserving intraday risk dynamics "delivers clear out of sample portfolio gains relative to benchmark screening methods"; and "its advantage comes mainly from the screening stage rather than from a particular weighting rule" (Section 5).

### Research interpretation

Falsifiable mechanism hypothesis (our reading, not the source's wording): **co-movement with a risk-adjusted cross-sectional leader series is a selection signal**. An asset whose (daily return, intraday volatility-shape) object moves in a stable metric pattern with a value-weighted high-Sharpe basket over the trailing six months is, we hypothesise, an asset whose liquidity/participation and risk state resemble the current "good" cross-section — a *risk-state similarity* channel rather than a return-prediction channel. Component roles:

- **Regime / filter:** none declared by the source; the 6-month rolling estimation window is the only state dependency.
- **Primary signal:** per-asset metric dependence score $\hat\rho^k_n$ over the trailing window (contemporaneous dependence with $Y_t$, not a lagged forecast).
- **Selection rule:** top-$d$ with $d\in\{30,60,90\}$ (source-reported).
- **Allocation layer:** EW / SEVW / constrained GMV with caps $u_{30}=0.15$, $u_{60}=0.10$, $u_{90}=0.05$ (source-reported); the allocation layer is *risk control, not alpha*.
- **Horizon:** monthly re-selection with a one-month hold (source-reported).

Critical interpretive gap: the score is computed on **same-day** $X_{i,t}$ and $Y_t$ pairs, so the mechanism asserts that trailing *contemporaneous* dependence implies *forward* attractiveness. The source reports no predictive IC, no lagged specification, and no decomposition of the forward return link — that arrow is asserted, not measured, and is the single most testable claim in this record.

## Signal

All items below are **source-reported** unless explicitly marked otherwise (Sections 2.1, 2.2, 5, Tables 6–7).

- **Formation timestamp:** "at each rebalancing date" — the source does **not** print a clock time, timezone, or publication convention (**underspecified**). Reconstruction assumption `research-proposed`: features use information through the rebalance date's close and the selection is executed at the next trading day's open.
- **Lookback:** rolling estimation window $M=6$ months of daily/intraday data; features use 1-minute trading-observation returns (midday break treated as adjacent; overnight gaps excluded), a 5-minute grid for the volatility curve with a symmetric window of two 1-minute returns either side (truncated at boundaries), and 5-minute prices for the target's realized variance. Strict point-in-time use of the trailing window is claimed by the source but no leakage audit is printed.
- **Target construction ($Y_t$):** $R_{i,t}=P^{close}_{i,t}/P^{close}_{i,t-1}-1$; $R_{M,t}$ = Shanghai Composite daily return; $RV_{i,t}=\sum_j r_{i,t,j}^2$ over $J$ five-minute intervals; $SR_{i,t}=(R_{i,t}-R_{M,t})/\sqrt{RV_{i,t}}$; $SR=-\infty$ if no intraday trades; select the $q=\lfloor0.1p\rfloor$ largest positive $SR$; $Y_t=\sum_{i\in H_t} MC_{i,t}/\sum_{k\in H_t}MC_{k,t}\cdot R_{i,t}$.
- **Score:** partition $\{Y_t\}$ into $H=8$ empirical-quantile slices per rolling window; per asset compute $\hat\rho^k_n = 1-\sum_m \hat p_m \hat V^k_m / \hat V^k_F$ under $d_X$; rank descending; screen top $d\in\{30,60,90\}$ (a threshold rule $\kappa n^{-\tau}$ is defined but **not** used empirically).
- **Long entry:** buy the top-$d$ screened names, long-only (the source states the long-only constraint reflects the A-share short-sale restriction).
- **Short entry:** none — no short leg exists in the source (**not applicable**).
- **Exit / holding period:** hold exactly one month, then re-form the selection with the window rolled forward one month. No stop, no take-profit, no intra-month re-weighting rule is stated (**underspecified**).
- **Position sizing:** EW; SEVW = score-squared weights; GOC = constrained global minimum variance $\min \omega^\top\hat\Sigma_t\omega$ s.t. $\mathbf{1}^\top\omega=1$, $0\le\omega_j\le u_d$ with sample covariance; GOCS = same with a shrinkage covariance (Schäfer and Strimmer, 2005). Caps $u_{30}=0.15$, $u_{60}=0.10$, $u_{90}=0.05$.
- **Tie-breaking, order type, execution price, partial fills, price-limit and T+1 handling:** **not stated in source** (data gap); any resolution of these is `research-proposed`.
- **Parameters summary:** $M=6$ months, $H=8$ slices, $d\in\{30,60,90\}$, curve grid weight fixed at 1, $q=\lfloor0.1p\rfloor$, caps $0.15/0.10/0.05$, annualization factor 252, annual risk-free rate 0.04. All are source-reported; the source reports **no sensitivity analysis** for any of them.

## Required data

- **Instrument / universe:** all A shares listed on the Shanghai and Shenzhen exchanges, sample window **2023-07-01 to 2025-12-31**, filtered to stocks with **complete observations over the whole sample period** → final $p=2938$ (Section 5). Inclusion/exclusion rule is therefore a *full-sample completeness* filter; no point-in-time listing rule, no delisting treatment, no liquidity floor, no reconstitution schedule (**data gap**; see Negative evidence for the survivorship consequence).
- **Venue / market type:** SSE and SZSE equity cash market (spot), long-only; no futures, options or derivatives in the source.
- **Timeframe / fields:** 1-minute intraday trading-observation returns (used for the spot-volatility grid, $\Delta=1$ minute, midday break joined, overnight gaps excluded); 5-minute last prices (target realized variance $RV_{i,t}$ and the $J$-point volatility grid); daily close-to-close returns; daily market capitalisation (target value weights); Shanghai Composite daily return (market adjustment). Tick/order-book/trades/ aggressor side, open interest, borrow, funding, options surface: **not used and not available in source**.
- **Point-in-time:** the source computes all features on the trailing window up to the rebalance date and holds the selected portfolio for the next month; no explicit availability lag, revision policy, or train/test boundary is printed beyond the rolling $M=6$-month window and the phrase "out of sample" (**partially specified**). The target $Y_t$ itself uses same-day market cap and same-day market return.
- **Timestamp / timezone:** no timezone, clock source, or alignment convention is stated (**data gap**).
- **Missing data:** stocks without intraday trades get $SR_{i,t}=-\infty$ for that day; the universe requires complete observations for the entire 30-month window (ex-post). No imputation policy is described; no stale/suspended/print-cleaning rules (**data gap**).
- **Cost / fee fields:** none. The source explicitly reports results "without transaction costs" and names turnover, transaction costs and liquidity constraints only as **future work** (Section 6). Commission, stamp duty, spread, slippage, market impact, borrow and capacity are all **data gap, never zero**.
- **Data needed to replicate (our normalization):** point-in-time SSE/SZSE daily EOD panel with delisted names retained, 1-minute bars for the full cross-section (≈2,900+ names, 30 months), 5-minute bars, daily market cap, Shanghai Composite returns, and a price series whose corporate-action adjustment convention must be defined by us because the source never states one (**data gap**).

## Execution assumptions

- **Source assumptions (explicit):** long-only (A-share short-sale restriction); monthly holding; constrained GMV caps as above; results reported **without transaction costs**. Nothing else about execution is modelled.
- **Not modelled by the source (all `data gap`, never treated as zero):** order type, market vs limit, fill model, latency, signal-to-order delay, spread, slippage, commission, sell-side stamp duty, market impact, participation/ADV caps, turnover, capacity, borrow, leverage/margin, partial fills, price-limit lock (limit-up/limit-down unfillable days), T+1 same-day-sale restriction, suspension handling, and failure handling.
- **Turnover:** **never reported**. With $d\in\{30,60,90\}$ re-selected monthly from a 2,938-name universe, consecutive-month overlap is unknown, so no break-even cost can be derived from the source (**data gap**).
- **Research-proposed execution layer (clearly not source-reported):** form the score at the rebalance date close, execute the next trading day at the open, one-way cost ladder of 0/5/10/20/30 bp plus A-share sell-side stamp duty and a 10%/20% ADV participation cap, treat a name as unfillable if it is limit-locked at the open. These are **our** operationalization for falsification only; they are not attributed to the source.
- **Net-vs-gross:** every performance figure below is **gross of all trading costs**. Note the source's column header "Accumulated net value" means *cumulative portfolio value*, **not** net-of-cost — it must not be read as a cost-adjusted result.

## Evidence

### Source-reported

Every figure below is **source-reported**, gross of all trading costs, from the pinned v2 HTML. Sample: full data window 2023-07-01 → 2025-12-31; backtest reported as **24 monthly out-of-sample portfolio observations** over **2024–2025** (Section 5 and Table 7 caption). The exact first rebalance date is not printed (**data gap**). Benchmarks: D-SEVIS (Wang et al. 2022 dependence screening), MTM (momentum ranking), and the Shanghai Composite Index (SCI).

- **Table 7, MDS rows (accumulated net value / max drawdown / Sharpe):** EW $d=30$ `1.74 / -0.36 / 0.90`, EW $60$ `1.69 / -0.35 / 0.86`, EW $90$ `1.61 / -0.35 / 0.79`; SEVW $30$ `1.72 / -0.36 / 0.89`, SEVW $60$ `1.69 / -0.35 / 0.86`, SEVW $90$ `1.62 / -0.35 / 0.79`; **GOC $30$ `2.04 / -0.31 / 1.22` (the paper's headline cell, Section 5 text)**, GOC $60$ `1.84 / -0.27 / 1.10`, GOC $90$ `1.68 / -0.27 / 0.96`; GOCS $30$ `1.98 / -0.29 / 1.17`, GOCS $60$ `1.76 / -0.25 / 1.02`, GOCS $90$ `1.65 / -0.27 / 0.92`.
- **Table 7, D-SEVIS rows:** EW `1.46/-0.34/0.65`, `1.45/-0.34/0.64`, `1.48/-0.34/0.67`; SEVW `1.46/-0.34/0.64`, `1.45/-0.34/0.64`, `1.47/-0.34/0.66`; GOC `1.47/-0.31/0.70`, `1.38/-0.28/0.60`, `1.39/-0.28/0.62`; GOCS `1.20/-0.29/0.34`, `1.22/-0.27/0.36`, `1.26/-0.27/0.43`.
- **Table 7, MTM rows:** EW `0.51/-0.55/-0.67`, `0.64/-0.45/-0.50`, `0.76/-0.40/-0.30`; SEVW `0.37/-0.67/-0.95`, `0.43/-0.62/-0.87`, `0.48/-0.57/-0.79`; GOC `0.45/-0.60/-1.08`, `0.70/-0.41/-0.60`, `0.88/-0.29/-0.24`; GOCS `0.45/-0.59/-1.05`, `0.65/-0.42/-0.71`, `0.86/-0.30/-0.28`.
- **Table 7, SCI row:** `1.33 / -0.15 / 0.73`. Drawdowns are printed as decimals; we read them as fractions of portfolio value (**our reading**, the source does not print units).
- **Sharpe convention (source-stated, Section 5):** "annualized with an annualization factor of 252 and an annual risk free rate of 0.04", applied to the **monthly** holding-period return series — the convention is therefore internally underspecified.
- **Our count on printed cells (arithmetic on Table 7, labelled our count, not source claims):** MDS exceeds D-SEVIS on Sharpe in **12 of 12** matched (weighting × size) cells, margins **+0.12 to +0.83**; MDS exceeds D-SEVIS on accumulated value in **12 of 12** cells, margins **+0.13 to +0.78**; MDS's best cell is **+104% over 24 months gross** (2.04) against SCI's **+33%**; MDS drawdowns span **-0.25 to -0.36**, i.e. **12 of 12** MDS cells are deeper than SCI's **-0.15**; the 12 MTM cells are all negative Sharpe (**-0.24 to -1.08**).
- **Simulation evidence (Section 4):** Euclidean setting with $n=200$, $p\in\{2000,5000\}$, cross-sectional correlation $\sigma\in\{0.5,0.8\}$, AR(2) and ARMA(1,1) designs, active set $\{1,2,12,22\}$, $d_1=\lfloor n/\log n\rfloor$ and multiples, **500 replications**, competitors SIS / SIRS / DC-SIS / D-SEVIS; non-Euclidean setting with a Wasserstein ($\mathcal{W}_2$) object-valued response, $\sigma\in\{0,0.5\}$, MDS only (competitors not applicable). Sampled cell, Table 4, $p=2000$, $\sigma=0$, $d_1$, AR(2) and ARMA(1,1) columns: all five $\mathcal{P}_s$ cells and all five $\mathcal{P}_a$ cells print **1.00**. The remaining simulation cells were **sampled, not exhaustively transcribed** (gap in this record).
- **Theory (Section 3):** Theorem 1 gives an exponential tail-deviation bound for $\hat\rho_n$ under $\alpha$-mixing-type dependence and partition approximation; Theorem 2 extends it to $\max_{k\le p}|\hat\rho^k_n-\rho^k|$ and yields **sure screening** $\mathcal{A}^\star\subseteq\hat{\mathcal{A}}_n$ with probability $1-O(s_n n^a e^{-c n^{1-3a-4\tau}})$ under Assumption 6; Theorem 3 gives **rank consistency** of the top-$d$ rule under Assumptions 1–5 and 7. These are asymptotic statements under untested assumptions, not empirical certification.

### Independently reproduced

not independently reproduced.

### Negative evidence

1. **No cost model whatsoever.** Section 5: "We report results without transaction costs"; Section 6 lists turnover, transaction costs and liquidity constraints as future work. Word scan of the pinned v2 text finds "transaction cost" exactly twice, both as above; bid-ask, slippage, commission, fee, stamp duty, impact, capacity, borrow, latency and fill are **absent → data gap, never zero**.
2. **Turnover is never reported**, so no break-even cost, no capacity statement, and no way to tell how much of the gross result survives any friction.
3. **Survivorship / look-ahead in the universe**: "We retain stocks with complete observations over the sample period" (2023-07-01 → 2025-12-31) makes inclusion depend on future survival; delisted, renamed and long-suspended names are removed ex post.
4. **Very thin OOS**: 24 monthly observations, one market, one window (2024–2025) that includes a strong late-2025 A-share rally. No repeated walk-forward, no subperiod or regime split, no hold-out year, no frozen forward window.
5. **No statistical inference at all**: no standard errors, t-statistics, p-values, confidence intervals, block bootstrap, or multiple-testing control across the **36 printed Table 7 cells** (3 selectors × 4 weightings × 3 sizes) plus SCI.
6. **Drawdowns are far deeper than the index**: every MDS cell (-0.25 to -0.36) is materially worse than SCI (-0.15) (our count). The paper's "comparable drawdown" statement is only relative to D-SEVIS, not to the passive benchmark, so part of the gross Sharpe improvement is paid for in tail risk.
7. **Sharpe convention is not reproducible**: an annualization factor of 252 is stated for a monthly holding-period series with an annual risk-free rate of 0.04; the exact return scaling cannot be reconstructed from the text.
8. **Weak baseline set.** Momentum fails outright (12/12 negative cells), and D-SEVIS is a close methodological sibling built on the *same* target series, so the experiment isolates the covariate/metric change but never tests against simple economic screens (value, size, liquidity, index constituents) or against a buy-and-hold-of-the-selected-universe control.
9. **The forward link is untested**: the score is a *contemporaneous* dependence over the trailing window; no predictive IC, rank correlation with next-month returns, or lagged regression is reported, so the causal arrow from dependence to forward return is asserted rather than measured.
10. **No data vendor, no code, no data-availability or code-availability statement, no price-adjustment convention** → independent reproduction currently impossible from the text alone.
11. **Exact OOS window underspecified**: only "24 out of sample portfolio observations" and the Table 7 caption "2024–2025" are printed; the first rebalance date is not.
12. **Execution/feasibility entirely unmodelled for A-shares**: T+1, ±10%/±20% price limits, limit-up/limit-down lock days, suspensions, and stamp duty are never mentioned, and price-limit behaviour is referenced only as a theoretical boundedness argument for the volatility curve.
13. **No parameter sensitivity**: $H=8$, $M=6$, $d$, caps $0.15/0.10/0.05$ and the fixed unit curve weight are researcher-chosen with no robustness grid, so tuning risk is unassessed.
14. **Long-only with no beta decomposition**: no alpha-over-benchmark regression, so a chunk of the gross accumulation may be market beta rather than selection skill.
15. **Theory assumptions untested empirically**: Assumptions 1–7 (strict positivity, modulus of continuity, balancedness, signal separation, $\log p_n=o(n^{1-3a-4\tau})$) are never checked on the A-share data, so the sure-screening/rank-consistency guarantees do not certify the printed ranking.
16. **Preprint status**: no journal, no peer-review statement, single research group, single market; publication-bias and self-evaluation concerns apply.
17. **Wording hazard**: "Accumulated net value" is a cumulative-wealth column, not a net-of-cost column; reading it as cost-adjusted would be a misinterpretation.
18. **Cross-record contrary evidence**: none verified in this run — adjacent A-share records in this repository (listed under Related Wiki records) were **not** re-read for their conclusions here, so no cross-record claim is asserted as evidence.

## Falsification plan

All thresholds below are **research-defined falsification thresholds** (our choices, not the source's) and all operational rules are **research-proposed**. Data assumed: point-in-time SSE/SZSE panel with delisted names retained, 1-minute and 5-minute bars, daily market cap, SCI returns.

- **F1 — Cost ladder (`research-defined`):** re-run the full pipeline with one-way costs 0/5/10/20/30 bp plus A-share sell-side stamp duty, at 10% and 20% ADV participation. **Fail** if the headline cell (MDS, GOC, $d=30$) has net Sharpe $<0.60$ at 10 bp, or if break-even one-way cost $<15$ bp.
- **F2 — Survivorship repair (`research-defined`):** rebuild the universe point-in-time with delisted and suspended names included. **Fail** if the MDS−D-SEVIS Sharpe margin falls below $+0.10$ or MDS net Sharpe $<0.80$.
- **F3 — Repeated walk-forward (`research-defined`):** five non-overlapping ~6-month OOS folds. **Fail** if MDS does not beat D-SEVIS in at least 3 of 5 folds.
- **F4 — Mechanism ablation: does the intraday curve carry the effect? (`research-defined`)** recompute the score with the curve component dropped (return-only covariate, curve weight 0). **Fail the mechanism claim** if the MDS−D-SEVIS Sharpe margin shrinks by less than 20% — i.e. the "intraday risk state" story is then unsupported even if the procedure still works.
- **F5 — Forward-link test (`research-defined`):** rank IC of $\hat\rho$ (trailing) against next-month returns. **Fail** if IC $\le 0$ in at least 3 of 4 quarters, or if the pooled IC t-statistic $<2.0$.
- **F6 — Placebo (`research-defined`):** 1,000 random top-$d$ draws per rebalance date with identical weighting and cost layer. **Fail** if MDS Sharpe is not above the 95th percentile of the placebo distribution.
- **F7 — Turnover and break-even audit (`research-defined`):** report monthly holdings overlap and turnover. **Fail** if break-even one-way cost $<15$ bp or average monthly turnover $>40\%$.
- **F8 — Paired significance (`research-defined`):** moving-block bootstrap over the monthly MDS−D-SEVIS return differential (6-month blocks, 1,000 draws). **Fail** if the 95% interval includes 0.
- **F9 — Multiplicity (`research-defined`):** Benjamini–Hochberg at $q<0.10$ over all 36 printed Table 7 cells plus every ablation. **Fail** if the headline cell does not survive.
- **F10 — Vendor transport (`research-defined`):** rebuild with a second independent intraday data vendor. **Fail** if MDS Sharpe moves by $>0.30$ or the sign of the MDS−D-SEVIS margin flips.
- **F11 — Beta / drawdown control (`research-defined`):** regress the MDS book on SCI. **Fail** if beta-adjusted alpha $\le 0$ or if MDS max drawdown is not brought within $0.9\times$ the SCI drawdown by the risk layer.
- **F12 — Frozen forward window (`research-defined`):** pre-register the rule and evaluate from 2026-01 onward with no retuning. **Fail** if net Sharpe $\le 0$ or if two consecutive months underperform D-SEVIS.
- **F13 — Feasibility / capacity (`research-defined`):** simulate A-share T+1, price-limit locks and suspensions at 10% ADV. **Fail** if more than 20% of selected names are unfillable at the intended execution time.
- **Action on failure:** any failure downgrades the hypothesis to rejected for our purposes and the record stays `research-only`; nothing here authorises implementation. F4 failing while F1/F2 pass would mean "a usable screening rule, but not the claimed mechanism", which is a materially different research object and must be re-recorded rather than relabelled.

## Crypto portability

**unproven.** The source contains no crypto evidence of any kind, and its mechanism originates in a traditional-equity market, so it must not be labelled `direct`.

- **What would port mechanically (`research-proposed` port, not source-verified):** the procedure needs only cross-sectional daily returns plus intraday bars to build the point-curve covariate, a market-adjustment series, and market caps for the target — all available for BTC/ETH and a broad altcoin panel. The screening statistic itself is venue-agnostic.
- **What does not port:** the target's market-adjustment leg is the Shanghai Composite (crypto has no single canonical index → would need a research-proposed BTC or equal-weight market basket); the long-only constraint is imposed by the A-share short-sale restriction, whereas crypto has no such restriction and the meaningful implementation is usually perpetual-based; $q=\lfloor0.1p\rfloor$ positive-HF-Sharpe selection behaves differently on a 24/7 clock with no midday break and no ±10% price limits.
- **Crypto-specific risks absent from the source:** funding and funding-rate carry, mark/index price and liquidation, venue fragmentation and per-exchange candle boundaries, 24/7 session and timezone conventions, borrow and short feasibility, stablecoin/quote-currency effects, listing/survivorship churn (far faster than A-shares), and maker/taker fee schedules.
- **Bottom line:** portability is an untested hypothesis. Any crypto version would be a *ported* hypothesis requiring fresh falsification (F1–F13 re-run on crypto data), not a replication.

## Limitations

- **underspecified:** formation clock time/timezone, execution price and order type, intra-month weight maintenance, tie-breaking, price-adjustment convention, corporate actions, suspension handling, and the exact OOS start date.
- **data gap:** data vendor; code and replication package; data/code-availability statement; turnover; transaction costs, spread, slippage, commission, stamp duty, impact, capacity, borrow; confidence intervals and any statistical inference; parameter sensitivity.
- **not independently reproduced:** no figure in this record has been recomputed by us; every number is transcribed from the pinned v2 tables with row/column provenance stated above.
- **unproven:** the forward link from contemporaneous metric dependence to next-month returns; the claim that the intraday curve (rather than the return coordinate) drives the gain; portability beyond Chinese A-shares; portability to crypto.
- **Survivorship:** the $p=2938$ universe is a full-sample completeness filter, so the printed out-of-sample result is conditioned on future survival.
- **Sample/regime:** 24 monthly observations, one market, one window containing a strong late-2025 rally; no subperiod, regime or hold-out analysis.
- **Model risk:** researcher-set parameters ($H$, $M$, $d$, caps, unit curve weight) with no robustness grid; theory assumptions unchecked on the data; single research group, preprint status.
- **Semantic hazard:** "Accumulated net value" ≠ net-of-cost; drawdown decimals read as fractions is our interpretation of an unlabelled unit.
- **Incremental-write check:** this record was written because the source identity (`2605.02326`) had zero repo hits and the mechanism (metric-space dependence screening on object-valued intraday covariates) is a new family here — not a reframing of an existing record.

## Implementation status

`implementation_status: not-implemented`. Nothing in this record has been implemented in our research stack: no screening pipeline, no A-share data ingestion, no portfolio construction, no backtest, no Qlib run, no Paper/Testnet/Live activity, and no writes to any downstream system. What exists is a source-traceable research capture plus a falsification plan. Implementation would first require a point-in-time universe with delisted names, licensed 1-minute intraday data for the full cross-section, and a reproduction of Table 7 before any extension.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. No record may promote itself by wording, evidence count, confidence, or schedule behaviour.

## Related Wiki records

Verified Wiki Brain pages returned by `kb_search` on 2026-09-25 (only these are linked; no page is fabricated):

- [[quant/china-ashare-l3-eaten-order-age-imbalance-execution-timing-falsification-2026-09-13]] — same universe/venue family (China A-share, intraday microstructure), different mechanism (L2 queue-age imbalance execution timing vs object-valued screening).
- [[quant/alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05]] — cross-sectional alpha-search family; mechanism (grammar-guided formulaic search) differs.
- [[quant/factorengine-program-level-knowledge-infused-factor-mining-2026-09-05]] — factor-mining family; mechanism (program evolution) differs.
- [[quant/llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04]] — evaluation/deflation methodology, relevant to F8/F9 above.

Queries that returned **0 pages** and therefore yield no link: "dependence screening score high frequency Sharpe target two-stage minimum variance" and "A-share factor library overfitting audit illiquidity falsification". A query on "asset selection screening high dimensional portfolio universe reduction" returned only unrelated LLM/RL pages, which were not linked.

**Four-axis distinction vs existing repo records (dedup justification):** `m2-alpha-micro-macro-attention-a-share-deep-learning-ranking-2026-09-13` (same A-share cross-sectional *ranking* purpose, but mechanism = learned micro-macro attention ranking, signal = neural embeddings, no intraday object covariate, no Fréchet screening statistic); `china-ashare-factor-library-overfitting-audit-amihud-illiquidity-falsification-2026-09-13` (same universe, but object = an overfitting *audit* of a 456-factor library, not a selection estimator); `favor-hypothesis-grounded-agentic-factor-validation-topk-portfolio-2026-09-24` (top-k daily portfolio output, but mechanism = LLM hypothesis-grounded factor validation, different universe and horizon); `cross-sectional-realized-skewness-dispersion-market-timing-2026-09-24` (uses intraday realized measures, but as an aggregate *market-timing* signal on S&P 500 allocation, not cross-sectional screening). Source identity, mechanism, signal construction, and material data dependency (1-minute + 5-minute point-curve objects) all differ from every neighbour above.

## Sources

- arXiv abstract page: https://arxiv.org/abs/2605.02326 (v1 4 May 2026 08:26:39 UTC, v2 10 May 2026 11:29:59 UTC; primary `stat.AP`, cross-list `q-fin.PM`; `CC BY 4.0`; no Comments, no Journal-ref, no publisher DOI).
- Pinned full text (primary source read for this record): https://arxiv.org/html/2605.02326v2 — 638,067 bytes, SHA-256 `7e1c924d348e7b83a108b66f05a43c25591e8344fcea3df715042c279ac849c3`, read 2026-09-25.
- Pinned PDF: https://arxiv.org/pdf/2605.02326v2 — 317,562 bytes, SHA-256 `8c6fb2503754c4ef8bb27f31461ccbfea7c7838ad90e2eb7b8926ea3b378dafd`.
- DataCite DOI: https://doi.org/10.48550/arXiv.2605.02326 (final HTTP 200 on the arXiv abs page, checked 2026-09-25).
- Methodological predecessor cited *by* the source (not read directly for this record, so no claim from it is reproduced here): Wang et al. (2022), "Asset selection based on high frequency Sharpe ratio" — the D-SEVIS baseline and the $Y_t$ target construction are attributed to it only as the source describes them.
