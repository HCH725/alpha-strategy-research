---
schema: strategy-research-record-v1
title: "Active Equal-Weight Tilt Control on a Stochastic Diversity–Dispersion State: S&P 500 Market-vs-Equal-Weight Allocation with Quadratic Friction Surrogate (arXiv:2609.27113)"
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: low
source_as_of: 2026-09-22
sources:
  - https://arxiv.org/abs/2609.27113
  - https://arxiv.org/html/2609.27113v1
  - https://github.com/brianceco/apm-in-cem
  - https://github.com/brianceco/apm-in-cem/tree/ae75eb5803c09b3a2bbd4965cea556831c6cd4aa
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Active Equal-Weight Tilt Control on a Stochastic Diversity–Dispersion State: S&P 500 Market-vs-Equal-Weight Allocation with Quadratic Friction Surrogate

## Provenance

- **Primary source (paper):** Brian Ceco, Xiaofei Shi, Ting-Kam Leonard Wong, *"Active Portfolio Management in Concentrated Equity Markets"*, arXiv preprint `arXiv:2609.27113v1 [q-fin.PM, math.OC, q-fin.MF]`, **v1 submitted Tue, 22 Sep 2026 22:08:37 UTC (841 KB)** — submission history on the landing page shows **only [v1]** (no v2). Comments field: "31 pages, 11 figures". Landing page shows **no journal-ref and no DOI field** → publication status `preprint only`.
- **Author list (exactly as source, HTML v1 front matter):** Brian Ceco — *"Address: Department of Mathematics, University of Toronto"*; Xiaofei Shi — *"Address: Department of Statistical Sciences, University of Toronto"*; Ting-Kam Leonard Wong — *"Address: Department of Statistical Sciences, University of Toronto"*. arXiv `citation_author` meta entries match these three names; no fourth author / no "and N other authors" string observed.
- **License (landing page):** `arxiv.org/licenses/nonexclusive-distrib/1.0/` (arXiv non-exclusive distribution license, **not** a Creative Commons license). This record therefore only normalizes and cites; it does not reproduce paper text or figures.
- **Code (implementation provenance):** repository `https://github.com/brianceco/apm-in-cem`, pinned **full commit SHA `ae75eb5803c09b3a2bbd4965cea556831c6cd4aa`** (default branch `main`; commit message "Added arxiv link to readme … Updated the README to include the correct paper citation", committer date `2026-09-24T00:47:00Z`; repository created `2026-09-18T21:31:37Z`, `pushed_at 2026-09-24T00:47:00Z`, `fork: false`, `stargazers_count: 0`). Recursive tree at that SHA is **`truncated: false`, 24 entries**, including `notebooks/1_diversity_and_dispersion.ipynb`, `notebooks/2_stylized_facts.ipynb`, `notebooks/3_backtest.ipynb`, `src/backtest.py`, `src/config.py`, `src/data.py`, `src/paths.py`, `src/plotting.py`, `src/simulate.py`, `src/utils.py`, `tests/test_backtest.py`, `tests/test_data.py`, `tests/test_utils.py`, `configs/config.json`, `environment.yml`, `requirements.txt`, `README.md`. GitHub API reports `"license": null` → **no license file at the pinned commit** (`data gap` for reuse rights; code is publicly readable, auditable, but unlicensed).
- **Data provenance as stated by source:** constituent-level market capitalization and return data for the **S&P 500, 1977–2024, from the CRSP database** (§4.1 footnote links `https://www.crsp.org/products/research-products/crsp-us-stock-databases`), processed with the publicly available code in **Ruf (2023), `https://github.com/johruf/CRSP_on_WRDS_introduction`, "Notebook 6"** (reference [42] of the paper). Sharpe-ratio risk-free rate comes from **Ken French's data library** (Table 3 caption, reference [17]).
- **Deduplication (performed before writing, 2026-09-24):** repo-wide `rg --hidden` across **all tracked `*.md` (928 files)** plus `coverage_manifest.csv` (5,807 data rows). Exact source-identity patterns all **0 hits**: `2609.27113`, `10.48550/arXiv.2609.27113`, `Active Portfolio Management in Concentrated Equity Markets`, `apm-in-cem`, `brianceco`, `Ting-Kam`, `Taljaard`, `equal weight portfolio underperformed`, `diversity-dispersion`, `diversity dispersion`, `SDD model`, `aiming in front of a moving target`. (`Ceco` produced 9 substring hits that are unrelated words inside two other records — `Kalshi…` and `alphalogics…` — not this author.) Mechanism-word scans found `market diversity` in exactly **1** existing record and `dispersion index` in **1** existing record; both are different sources (see Related Wiki records / neighbour list) with different mechanism, universe and horizon.
- **Source-identity conclusion:** no existing record shares this canonical source identity; no second capture of this paper exists.

## Economic mechanism

### Source-reported

The paper's stated chain is (all quotes/paraphrases anchored to `arXiv:2609.27113v1` sections):

1. **Master-formula decomposition.** Under stochastic portfolio theory the log relative value of the equal-weighted portfolio versus the cap-weighted market portfolio is `d log V^ew = dφ_ew + ½ δ_ew dt` (§2.1, eq. 2.11 region), i.e. relative performance is governed entirely by **market diversity** `φ_ew` and **dispersion** `δ_ew`. Diversity contributes a term that can move relative value in **either** direction; dispersion contributes a non-negative drift. The source's words: *"Over short horizons, a sufficiently sharp decline in diversity can dominate the dispersion effect, causing the equal-weighted portfolio to underperform as market concentration increases."*
2. **Regime statement.** Equal-weight has historically beaten cap-weight, but *"is regime dependent, with the equal-weighted portfolio underperforming during periods of increasing market concentration and high correlations, particularly market bubbles"* (abstract; Figure 1 shows S&P 500 diversity at levels not seen since the late-1990s dot-com bubble, long-run mean about `−6.95`).
3. **Control problem.** Instead of a binary switch, the investor solves a stochastic control problem choosing a **continuous tilt** `λ(t)` between market (`λ≡0`) and equal-weight (`λ≡1`), maximizing expected log relative performance minus active-risk aversion `γ` and a **quadratic surrogate** for implementation friction (`Λ₁` position penalty, `Λ₂` trading-rate penalty). The optimum is a linear forward–backward SDE whose solution trades toward a **weighted conditional forecast of future frictionless tilts** — the paper's phrase is *"aiming in front of a moving target"*, in the spirit of Gârleanu–Pedersen (§3.2, Theorem 3.1).
4. **Predecessor relationship.** The source states that Taljaard & Maré (2021, *Quantitative Finance* 21(11):1855–1868, ref [48]) *"uses a linear-regression signal to select either the equal-weighted portfolio or the market portfolio at each decision date. In this paper, we generalize the framework of [48] to allow continuous adjustments between the equal-weighted and market portfolios."* The 15 bps cost level is also taken *"Following [48]"* (§4.3.3).
5. **Claimed economic result.** Out-of-sample (1995–2024) the resulting strategies *"deliver higher cumulative net returns than both the equal-weighted and market portfolios, and higher information ratios than the equal-weighted portfolio after 15-basis-point proportional transaction costs"* (abstract), with Appendix regressions suggesting *"positive residual alpha"* (§1, reproduction paragraph).

### Research interpretation

- **Hypothesized mechanism (falsifiable form):** market concentration is persistent but mean-reverting (or short-run persistent) in a way that is *observable ex ante* through the joint state of diversity `φ_ew = log` geometric mean of cap weights and realized dispersion `RD_ew`. Because dispersion is a non-negative drift for equal-weight while diversity decline is the loss channel, a **state-dependent tilt** — long equal-weight tilt when expected diversification benefit per unit of active variance is high, market/short tilt when concentration pressure is high — should harvest diversification return while dodging concentration drawdowns, net of a realistic monthly-turnover cost.
- **Component roles (hybrid structure as decoded from the source):**
  - **State / regime input:** monthly market diversity `φ_ew(t_k)` (S&P 500 cap weights) plus monthly realized dispersion of the equal-weight portfolio, scaled to instantaneous dispersion by `δ̂ = c_δ · RD_ew` with `c_δ` estimated in-sample.
  - **Forecast layer (two alternative specifications, both reported):** (i) *mean-reverting* joint SDD model for `(φ, δ)` calibrated by maximum likelihood (Table 2 values, in-sample 1977–1994); (ii) *trending* data-driven model: exponentially smoothed **daily** diversity trend with GARCH(1,1) variance, trend half-life `h_φ = 21` trading days (about one month).
  - **Signal / target:** frictionless tilt `λ₀*(t) = (1/(1+γ))·((2b_φ(t) + δ(t)) / (2σ_φ²(t)) + ½)` (eq. 3.2) — expected relative log return of equal-weight over market, scaled by active variance, shrunk by risk aversion; `λ₀*` may be `<0` or `>1`.
  - **Execution smoothing:** frictional tilt `λ*` aims at `((1+γ)/(1+γ+Λ₁)) ·` a `G`-weighted conditional forecast of `λ₀*` over a rolling horizon `M` (eq. 4.3/4.4), `M = 12` months for the mean-reverting spec, `M = 1` for the trending spec.
  - **Implementable long-only variant:** clipped tilt `λ̄ = (λ* ∨ 0) ∧ 1` (a convex combination of the two portfolios).
- **What is *not* claimed by us:** this record does not assert that the effect survives independent replication, other universes, other cost levels, borrow costs, or that factor alphas are real. The source's own factor section calls its alphas *"descriptive factor attribution rather than conclusive evidence of persistent abnormal returns"* (§ after Table 5).
- **Attribution caution:** the relative-value decomposition is a **theory identity** plus an empirical regime claim; the source itself notes constituent changes, dividends and discrete rebalancing break the exact identity (Remark 2.11 leakage effect), which it does **not** model (listed as future work in §5).

## Signal

All items below are **source-reported unless explicitly tagged** `research-proposed` / `research-defined`.

- **Formation timestamp / tradability:** signals are dated `t_k` and *"use information available through `t_k` and determine the portfolio held over `(t_k, t_{k+1}]`"*; `λ*(t_{k+1})` is *"computed using information available at `t_k` and applied only to returns realized over `(t_k, t_{k+1}]`"* (§4.1, §4.3.1). Discrete grid `Δt = 1/12` → **monthly rebalancing only**, each monthly interval ≈ 21 trading days. Timezone is **not stated** in the source → `data gap` (CRSP daily equity data conventionally uses US exchange sessions; do not treat as verified).
- **Lookback / warm-up:**
  - Diversity: full cap-weight vector at `t_k`; `φ_ew(t_k) = Σᵢ (1/n) log μᵢ(t_k) = log(μ₁⋯μ_n)^{1/n}` (§2.1).
  - Dispersion proxy scale: `c_δ = 0.21` from OLS of `Δlog V^ew − Δφ_ew = (c_δ/2)·RD_ew·Δt + ε` on **monthly observations 1977–1994**, adjusted `R² = 0.95` (§4.1).
  - Mean-reverting SDD parameters: MLE on **1977–1994** for the backtest (Table 2: `κ_φ = 0.43`, `φ̄ = −6.93`, `ν_φ = 0.30`, `κ_δ = 5.52`, `δ̄ = 0.018`, `ν_δ = 0.99`, `ρ = −0.30`, `γ_mr = 19.91`; plus `Λ₁`, `Λ₂` calibrated below). A **separate, longer** calibration for the model-fit section uses **1977–2004** with fit assessed on 2005–2024 (Table 1: `κ_φ = 0.318 (0.089, 0.547)`, `φ̄ = −6.934`, `ν_φ = 0.371`, `κ_δ = 3.179 (1.308, 5.049)`, `δ̄ = 0.011`, `ν_δ = 2.369`, `ρ = −0.20 (−0.304, −0.095)`). The source states that `ν_φ`, `κ_δ`, `ν_δ` **differ materially between the two windows** (§4.3.3).
  - Trending spec (Table 2): `α_φ` set so trend half-life `h_φ = −log2 / log(1−α_φ) = 21` trading days; GARCH `ω = 6.36e−7`, `α_v = 0.14`, `β_v = 0.79` (persistence `0.93`); `γ_trend = 30.11`. Daily returns above **+100%** or below **−50%** are dropped for in-sample calibration only (per Ruf Notebook 6 convention).
  - Frictionless risk scaling: `γ_m` chosen **in-sample** so the frictionless target has **5% annualized active volatility** (eq. 4.6). ⚠ **Internal inconsistency in source (recorded, not repaired):** §4.2.3 simulation text says *"we set `γ = 16.81` so that the frictionless target portfolio has annualized active volatility of 5% in the in-sample period"* while Table 2 (same procedure, same sample) reports `γ_mr = 19.91`. Both numbers appear in v1; the record does not choose between them → `underspecified`.
  - Cost-surrogate calibration (in-sample only, 1977–1994): `Λ̂₁` by matching terminal in-sample quadratic proxy to the **equal-weighted portfolio's** active cost (eq. 4.8); `Λ̂₂` by minimizing terminal absolute discrepancy for the frictional optimal strategy (eq. 4.9); *"All parameters are estimated using 1977–1994 data and then held fixed throughout the out-of-sample period."* Calibrated values shown for the mean-reverting model: **`Λ₁ = 1.17`, `Λ₂ = 0.54`** (Figure 7 caption).
- **Long entry (equal-weight tilt up):** `λ* > 0` — mechanically `λ₀* > 0 ⟺ (2b_φ + δ)/σ_φ² > −1` (eq. region after 3.2): forecast relative log-return of equal-weight net of active variance clears the threshold. Unconstrained solution may exceed 1 (levered equal-weight tilt).
- **Short entry (market/short tilt):** `λ* < 0` when `(2b_φ + δ)/σ_φ² < −1`, i.e. concentration pressure strong enough that expected relative log return is negative — the portfolio then shorts the equal-weight basket relative to market. Table 3 shows the mean-reverting frictional strategy holds **average gross exposure `GE = 1.46`**, i.e. it does take such positions; the source notes *"The mean-reverting strategy tends to take larger short positions … approximately 32% higher [than trending]"*. The clipped variant `λ̄ ∈ [0,1]` is long-only and is reported as an **implementable benchmark**, explicitly *"not the solution of a dynamically constrained version of our stochastic control problem"*.
- **Exit / rebalance:** no stop-loss, no take-profit, no discrete exit. The portfolio is re-targeted **monthly**; between rebalances it is held (stocks held for the whole month *"unless they delist … prior to the end of the month"*).
- **Holding period:** 1 month per target; overlapping positions do not apply (single two-leg portfolio: equal-weight leg + market leg + cash/short balance implied by `‖π‖₁ = GE`).
- **Forecast horizon parameter:** `M = 12` (one-year rolling forecast average) for the mean-reverting spec — *"We find this reasonably balances the tradeoff between reducing transaction costs while minimizing the noise introduced from the forecasting error"*; `M = 1` for the trending spec (no forward forecast). The source states *"Increasing the half-life to several months produces qualitatively similar backtest results"*.
- **Position sizing logic:** governed by the control solution — active-risk budget 5% annualized (in-sample), risk-aversion `γ_m`, penalties `Λ₁`, `Λ₂` (see Table 2). Not a fraction-of-Kelly or fixed-notch rule; reconstructing it requires solving the linear FB-SDE recursion (`src/simulate.py`/`src/backtest.py` in the pinned repo is the executable form).
- **Parameters: fixed vs tuned:** all SDD, `c_δ`, `γ`, `Λ₁`, `Λ₂` are estimated **in-sample 1977–1994 and frozen OOS** (source-reported, good hygiene). The **choice of the two specifications, of the 5% active-vol target, of `M`, and of the 15 bps cost level** are design choices of the authors; the source does not report a search procedure over them → treat any claim of optimality as `underspecified`.
- **Rule fully specified?** Mechanism and equations are fully stated; two items are **not reconstructable from the paper alone**: (i) the exact S&P 500 membership/point-in-time construction (CRSP + Ruf Notebook 6, membership flag not described in the paper) → `data gap`; (ii) the `γ = 16.81` vs `γ_mr = 19.91` discrepancy above → `underspecified`. The pinned repository contains the backtest notebook and `configs/config.json` for (i)-adjacent detail, but this run did **not** execute the notebook.

## Required data

- **Instrument / universe:** time-varying constituents of the **S&P 500** (~largest 500 US listed companies, ~80% of US equity market cap per source), **1977–2024**.
- **Market type:** US **equity spot** (CRSP stocks), with **short selling permitted** in the strategy (short legs on the equal-weight basket relative to market).
- **Venue / data vendor:** CRSP (`crsp.org` US stock databases) via WRDS; processed with `github.com/johruf/CRSP_on_WRDS_introduction` Notebook 6.
- **Timeframe:** **daily** returns used to compute monthly realized dispersion and the daily trend state; **monthly** decision grid (`Δt = 1/12`, ~21 trading days).
- **Fields:** per-stock market capitalization (cap weights `μᵢ`), total returns (dividends enter through the cash/dividend term `D̂` in the cost equation §4.3.3), constituent membership over time, delisting dates; derived series: `φ_ew`, `RD_ew` (equal-weight realized dispersion from daily returns), `δ̂ = c_δ·RD_ew`. Reference-only comparison series: Cboe S&P 500 Dispersion Index (**DSPX**, reference [47]) used in Figure 2, and Ken French library risk-free rate for Sharpe ratios.
- **Point-in-time / availability:** signals use only information through `t_k` and are applied to the *next* month (no same-month look-ahead in the stated design — source-reported). **But:** how S&P 500 membership is identified point-in-time from CRSP is **not described** in the paper → `data gap` (index membership is announced/known at the time in reality; still, replication must pin the exact rule, index-effect handling, and whether membership is lagged).
- **Missing-data / outlier policy:** daily returns `> +100%` or `< −50%` dropped **for in-sample calibration only** (source-reported); stocks assumed held until delisting within the month. No other imputation rules stated → `data gap`.
- **Funding / fee needs:** none for the equity legs other than the **15 bps proportional trade cost** actually modeled. **Not** in the source: **short-borrow fees, dividends-in-lieu, stock-loan availability, market impact, spread**, and index-rebalance transaction costs of the market benchmark beyond what flows through the same 15 bps rule → `data gap`.

## Execution assumptions

- **Signal-to-order timing:** decision at `t_k` using data through `t_k`; portfolio target implemented **at the `t_k` rebalance** and held over `(t_k, t_{k+1}]`. Same-month entry timing within `t_k` (open vs close) is **not specified** → `underspecified`.
- **Order type / fill model:** the source models a **frictionless instantaneous re-target at monthly grid points** charged 15 bps on the **value of all trades**, using the Ruf–Xie (2020) cash-adjustment root-find `F(c) = 0` adapted *"to allow for short-selling"* (§4.3.3). No partial fills, no limit orders, no latency, no participation cap → `data gap` (implicit assumption: full fill at the rebalance).
- **Fees / slippage / spread:** **flat 15 bps proportional cost on trade value, deducted directly from portfolio wealth** for *every* net statistic (§4.3.4: *"Every net-return, Sharpe-ratio, information-ratio, drawdown, and wealth statistic in this subsection is computed after deducting 15-bps proportional transaction costs directly from portfolio wealth."*). **No cost ladder / no sensitivity to the cost *rate*** is reported (the Λ-perturbation in §4.3.5 varies the *policy penalty*, not the backtest cost rate) → `data gap`. Spread, impact, borrow, and financing are **not modeled anywhere in v1** → `data gap` (not to be read as zero).
- **Gross vs net:** both reported (`SR_gross` vs `SR_net` in Table 3); `gross` = before proportional costs, `net` = after (eq. 4.7 defines cumulative active cost `C^π = log V_gross − log V_net`).
- **Leverage / margin / shorting:** unconstrained variants run with `GE` up to **1.65** (frictionless mean-reverting) and **1.46** (frictional mean-reverting) average gross exposure; short legs exist. Margin requirements, rebate income on short proceeds, and borrow fees are **not stated** → `data gap`.
- **Capacity / impact / liquidity:** **not discussed anywhere in v1** → `data gap`.
- **Benchmark turnover:** market benchmark turnover `0.01`, equal-weight `0.07` (Table 3) — i.e. most of the strategy's turnover (`0.15`/`0.34`) is *active* trading generated by the tilt dynamics.
- **What the source assumes vs what we assume:** everything above is the source's model. We add **no** execution assumptions of our own; any replication choice (e.g. rebalance at close of last trading day, borrow fee schedule) must be labeled `research-proposed` — see Falsification plan.

## Evidence

### Source-reported

All figures below are **source-reported** from the pinned primary source `arXiv:2609.27113v1` (no cross-version mixing: only v1 exists). Not independently reproduced.

**Table 3 — out-of-sample performance, monthly rebalancing, 15 bps proportional transaction costs, OOS 1995–2024** (caption: "Tot. Ret. denotes cumulative net return. Ret. is the annualized mean net return … Vol. is the annualized volatility … SRgross and SRnet denote the gross and net Sharpe ratios, respectively, using the risk-free rate from Ken French's data library [17]. IR denotes the information ratio of the net active return … Turnover is the average ℓ₁-distance between the pre- and post-rebalancing portfolio weights … GE denotes average gross exposure … MDD and RT denote maximum drawdown and recovery time, with RT measured in months"):

| Portfolio | Tot. Ret. | Ret. | Vol. | SR_gross | SR_net | IR | Turnover | GE | MDD | RT (mo) |
|---|---|---|---|---|---|---|---|---|---|---|
| `λ₀*,mr` (frictionless, mean-rev) | 32.10 | 0.13 | 0.17 | 0.69 | 0.65 | 0.21 | 0.41 | 1.65 | 0.51 | 52 |
| `λ*,mr` (frictional, mean-rev) | 44.92 | 0.14 | 0.16 | 0.74 | 0.72 | **0.35** | 0.15 | 1.46 | 0.50 | 50 |
| `λ̄*,mr` (clipped long-only) | 32.46 | 0.13 | 0.16 | 0.68 | 0.68 | 0.34 | 0.05 | 1.00 | 0.50 | 39 |
| `λ₀*,trend` (frictionless, trending) | 32.49 | 0.13 | 0.16 | 0.76 | 0.69 | 0.26 | 0.59 | 1.17 | 0.50 | 41 |
| `λ*,trend` (frictional, trending) | 31.41 | 0.13 | 0.15 | 0.73 | 0.69 | 0.29 | 0.34 | 1.11 | 0.51 | 41 |
| `λ̄*,trend` (clipped long-only) | 26.43 | 0.12 | 0.16 | 0.66 | 0.65 | 0.29 | 0.15 | 1.00 | 0.51 | 41 |
| `π^ew` equal-weighted (`λ≡1`) | 24.33 | 0.12 | 0.17 | 0.59 | 0.58 | **0.13** | 0.07 | 1.00 | 0.56 | 44 |
| `μ` market (`λ≡0`) | 21.34 | 0.12 | 0.15 | 0.61 | 0.61 | — | 0.01 | 1.00 | 0.50 | 73 |

Additional source-reported statements tied to the same table/section:

- Headline comparisons (§4.3.4): frictional mean-reverting **net IR 0.35 vs 0.29 for the frictional trending spec vs 0.13 for the equal-weighted portfolio** over 1995–2024; frictional vs frictionless mean-reverting: turnover **0.41 → 0.15**, IR **0.21 → 0.35**; trending: turnover **0.59 → 0.34**, IR **0.26 → 0.29**. The source explicitly notes the mean-reverting IR gain *"cannot be entirely explained by a reduction in transaction costs. Rather, a slower-varying trading signal appears to better predict the mean-reverting dynamics of market diversity."*
- *"On an absolute basis, we see the average rate of return and volatility of all of the portfolios are quite similar, resulting in Sharpe ratios which are not materially different from each other."* (§4.3.4) — net Sharpe range **0.58–0.74** across all eight rows.
- Clipping: *"Clipping the tilt process to the interval [0,1] leaves the information ratio of both strategies effectively unchanged"* (0.34 vs 0.35; 0.29 vs 0.29) → the source's claim that outperformance *"does not require excessive short-selling"*.
- **Unit caveat:** the `Tot. Ret.` column is labeled "cumulative net return" but the caption **does not define the unit** (percent vs terminal-wealth multiple). Values (44.92 / 32.46 / 24.33 / 21.34) are printed exactly as above; treating them as ×wealth multiples is our inference, **not** source-stated → `underspecified`.

**Table 4 — Fama–French 3-factor, monthly OLS (t-statistics in parentheses), OOS portfolio returns:**

| Portfolio | MKT-RF | SMB | HML | 12α (%/yr) | R² (%) |
|---|---|---|---|---|---|
| `π^mr` | 0.981 (40.832) | −0.012 (−0.377) | 0.254 (8.152) | **2.47 (1.943)** | 82.9 |
| `π^trend` | 0.970 (61.784) | 0.051 (2.372) | 0.015 (0.724) | **1.50 (1.811)** | 91.7 |
| `π^ew` | 1.060 (73.682) | 0.225 (11.348) | 0.265 (14.230) | −0.41 (−0.537) | 94.4 |

Source's own reading: *"marginally significant at the 10% level but not at the conventional 5% level."*

**Table 5 — Fama–French 5-factor, monthly OLS:**

| Portfolio | MKT-RF | SMB | HML | RMW | CMA | 12α (%/yr) | R² (%) |
|---|---|---|---|---|---|---|---|
| `π^mr` | 1.007 (38.88) | 0.038 (0.99) | 0.178 (4.00) | 0.123 (2.52) | 0.093 (1.44) | **1.54 (1.18)** | 83.3 |
| `π^trend` | 0.980 (57.60) | 0.054 (2.13) | −0.021 (−0.72) | 0.003 (0.10) | 0.082 (1.94) | **1.26 (1.47)** | 91.8 |
| `π^ew` | 1.077 (69.48) | 0.250 (10.90) | 0.212 (7.99) | 0.058 (1.99) | 0.084 (2.17) | −0.96 (−1.23) | 94.5 |

Source's own reading: *"Neither estimate is statistically significant … We therefore interpret these regressions as descriptive factor attribution rather than conclusive evidence of persistent abnormal returns."*

- **Calibration/simulation evidence (not tradable performance):** Table 1 MLE fit on 1977–2004 with Wald CIs (values listed in Signal), Figure 3–6 stylized-fact comparisons, Figure 8 histograms of terminal performance differences between frictional and frictionless portfolios over **10,000 simulated paths** of the calibrated SDD model. These are model-fit results, **not** market backtests.
- **Sensitivity (§4.3.5, Figure 11):** out-of-sample IR is *"relatively insensitive to moderate changes in `Λ₁`"* for both specs (because `γ` and `Λ₁` enter via `1+γ+Λ₁`), but *"sufficiently large values of `Λ₂` materially reduce the performance of the trending strategy and can eventually produce a negative information ratio"*; the mean-reverting strategy *"remains relatively stable over a broad range of trading-rate penalties."*
- **Publication status:** `preprint only`, v1 22 Sep 2026, no journal-ref, no DOI on landing page, 31 pages / 11 figures, arXiv non-exclusive license.

### Independently reproduced

`Not independently reproduced.` This run performed only: (a) landing-page and full-text (`https://arxiv.org/html/2609.27113v1`) direct reading, (b) table/figure/section provenance location for every number above, (c) GitHub repository metadata + recursive-tree inspection at the pinned SHA, (d) repository-wide source-identity dedup. **No Sharpe, IR, return, alpha or regression was recomputed; the backtest notebook was not executed; CRSP data was not obtained.**

### Negative evidence

Recorded from the primary source itself (no external contrary study was opened for this record):

1. **Factor alpha is not robust in the paper's own tests:** FF5 annualized alphas 1.54%/1.26% with t = **1.18/1.47** → not significant; FF3 alphas significant only at the 10% level (t = 1.943/1.811). Source labels them descriptive.
2. **Absolute risk-adjusted performance does not improve:** net Sharpe 0.72 (strategy) vs 0.61 (market) vs 0.58 (EW); the source states Sharpe ratios are *"not materially different"*. The whole case rests on a **net IR of 0.35** at a 5% in-sample active-vol target.
3. **Effect size is small and concentrated in one mechanism comparison:** net IR gap over equal-weight = 0.35 − 0.13 = 0.22 over 30 years, single universe, single index family.
4. **Recent-period regime doubt flagged by the authors:** *"The recent relative underperformance of the mean-reverting strategy is particularly interesting. It is unclear if, as in the lead up to the dot-com crash, this represents a decline in market diversity which is unsustainable, or else a structural break in the mean-reverting dynamics of diversity."* (§4.3.4) — i.e. the flagship spec may have degraded in exactly the era a live trader would use it.
5. **Estimation-window sensitivity:** `ν_φ`, `κ_δ`, `ν_δ` *"differ materially"* between the 1977–1994 and 1977–2004 calibration windows (§4.3.3) — the state dynamics themselves are window-dependent.
6. **Internal parameter inconsistency:** `γ = 16.81` (§4.2.3, claimed to match the historical-backtest 5% active-vol target) vs `γ_mr = 19.91` (Table 2, same sample/procedure) → unreconciled in v1.
7. **Trending spec is fragile to its own smoothing penalty:** IR can turn **negative** for large `Λ₂` (Figure 11); its frictional turnover (0.34) is >2× the mean-reverting one.
8. **Cost treatment is single-point:** exactly **15 bps**, no ladder, no spread/impact/borrow, while the strategy's turnover (0.15–0.41 monthly ℓ₁) makes it cost-rate sensitive by construction; short legs (GE 1.46) carry **unmodeled borrow fees**.
9. **Open-market effects are acknowledged but unmodeled:** constituent changes produce a *"leakage effect"* (Remark 2.11) that drags relative performance; explicit modeling of constituent turnover is deferred to future work (§5) — so the backtest's universe handling is a material unknown.
10. **Drawdowns are not improved:** MDD 0.50–0.51 for the strategies vs 0.50 market / 0.56 EW, with RT 50 months (mr) vs 44 (EW) and 73 (market) — recovery is *longer* than equal-weight's.
11. **Long-only implementable variant gives up most of the cumulative gap:** `λ̄*,mr` Tot. Ret. 32.46 vs `λ*,mr` 44.92 (as printed) — i.e. part of the headline total-return advantage is delivered by unconstrained leverage/shorting that a constrained account may not run.
12. **Design choices are unreported as a search:** the 5% active-vol target, `M = 12`, two candidate specifications and 15 bps are author choices with no multiple-testing/selection control disclosed → possible specification selection cannot be ruled out from the paper alone.
13. **Absence check:** no independent replication, no out-of-universe test (e.g. Russell/CRSP-wide), no post-publication evidence exists yet (paper is 2 days old at time of writing) — *"absence is not evidence of no negative result."*

## Falsification plan

Thresholds marked `research-defined` are **our** acceptance/failure cutoffs, not the source's. Data requirements marked `research-proposed` are **our** operationalization.

- **F1 — Independent replication (highest priority) `research-defined`.** Rebuild the pipeline on an independent data build (point-in-time index membership, total-return series) and require the **frictional mean-reverting net IR over a fresh ≥10-year OOS window to exceed the equal-weighted benchmark's net IR by ≥ 0.15** (absolute gap, 15 bps) with the **sign of the monthly active-return t-stat ≥ 2.0 (Newey-West, lag 6)**. *Fail →* record as non-replicated and demote to historical curiosity.
- **F2 — Cost ladder `research-defined`.** Re-run at **0 / 5 / 15 / 30 / 50 bps** proportional cost plus a spread model. *Failure rule:* if net IR advantage over equal-weight is `≤ 0` at **30 bps**, or the IR gap at 15 bps falls by **≥ 50%** when moving from 15 → 30 bps, the mechanism is cost-fragile → reject for our stack.
- **F3 — Borrow/short realism `research-defined`.** Add a stock-loan fee (e.g. `research-proposed`: 25 bps/yr general collateral, 100 bps/yr hard-to-borrow on the short basket) and index-rebalance costs. *Failure rule:* IR drops below **0.20** → the leverage/short contribution was the alpha, not the state signal.
- **F4 — Predecessor ablation (does continuous control beat the binary switch?) `research-defined`.** Implement the Taljaard–Maré-style **binary** EW-vs-market selector (the source's own stated predecessor) on the same data. *Failure rule:* if the control's net IR exceeds the binary selector's by **< 0.10**, the stochastic-control layer adds nothing operationally → keep only the simpler binary rule.
- **F5 — Baseline/ablation set `research-defined`.** Compare against always-EW, always-market, trailing-diversity-36M percentile switch, and a random-tilt placebo (shuffled `λ*` paths preserving turnover). *Failure rule:* strategy must beat **≥ 95% of 1,000 shuffled-tilt paths** on net IR and beat always-EW on net IR; otherwise the gain is turnover/leverage artifact.
- **F6 — Subperiod/regime stability `research-defined`.** 1995–2004 / 2005–2014 / 2015–2024 thirds plus the post-2015 subperiod the authors flag as weak. *Failure rule:* if the **2015–2024 net IR vs EW is ≤ 0**, label `regime-limited` and forbid forward claims.
- **F7 — Factor-model audit `research-defined`.** FF5 + momentum + quality with Newey-West, plus a pure equal-weight-vs-market timing regression. *Failure rule:* |t| of alpha **< 2.0** → classify the result as **style/concentration timing with no identified abnormal return**, not alpha.
- **F8 — Parameter stability `research-defined`.** Re-estimate SDD parameters on rolling 20-year windows; perturb `γ`, `Λ₁`, `Λ₂` by ×0.5 / ×2 (mirroring Figure 11) and re-run. *Failure rule:* if the mean-reverting net IR falls **< 0.15** anywhere in that band, or if the `γ = 16.81` vs `19.91` ambiguity changes the sign of the IR gap, treat the policy as knife-edge.
- **F9 — Universe generalization `research-defined`.** Repeat on **Russell 1000 / CRSP all-cap** equal-weight-vs-cap-weight (and, `research-proposed`, on a non-US large index). *Failure rule:* **≥ 2 of 3** universes with IR gap ≤ 0.10 → treat S&P 500 result as single-universe coincidence.
- **F10 — Leakage/point-in-time audit `research-defined`.** Rebuild membership strictly point-in-time with documented lag and index-effect treatment. *Failure rule:* IR gap vs EW changes by **> 0.10** in absolute terms → the published gap was a constituent-handling artifact.
- **F11 — Capacity `research-defined`.** Cap participation (e.g. `research-proposed`: ≤ 10% of ADV, `research-defined` AUM sweep). *Failure rule:* at target AUM the net IR gap falls **< 0.10** → not scalable for our use.
- **Action on failure:** any failed test downgrades the record's interpretation; two or more failed core tests (F1, F2, F6) → mark hypothesis rejected in our research notes. **No implementation, candidate-pool entry, or Paper/Testnet/Live step follows from this record regardless of outcome** — those are separate gated decisions.

## Crypto portability

`unproven`.

- **Mechanism port:** the *form* of the hypothesis (continuous tilt between an equal-weight and a cap-weight basket of a large universe, driven by a diversity–dispersion state) can be written down for crypto (e.g. top-50 spot or perp universes rebalanced monthly/weekly).
- **Why it does not port directly:** (i) the source's evidence is **US large-cap equity 1977–2024** — no crypto evidence anywhere in the paper; (ii) crypto has **no CRSP-like point-in-time index membership**, and market-cap weights are manipulable (supply schedule, exchange-specific float) so `φ_ew` is not a clean concentration state; (iii) **24/7 candles** break the monthly grid and the `Δt = 1/12` / 21-trading-day dispersion convention; (iv) **venue fragmentation** means an "index" of crypto caps is assembled from multiple feeds with different constituent sets; (v) equal-weight portfolios in crypto face **large turnover from listing/delisting churn and token deaths** — the leakage effect the paper already cannot model would be far larger; (vi) shorting the equal-weight basket versus cap-weight requires **perp funding and borrow** on dozens of names, unmodeled here; (vii) concentration dynamics (e.g. BTC dominance cycles) are plausibly faster-moving than S&P 500 diversity, so monthly rebalance and the 21-day half-life may be mis-scaled.
- **Status:** `unproven` = a **ported hypothesis only**, not crypto empirical evidence. Any crypto test would be a new study requiring its own cost/funding/24-7 specification.

## Limitations

- `not independently reproduced` — all performance numbers are source-reported from v1; no recomputation, no code execution, no CRSP access this run.
- `preprint only` — v1 dated 2026-09-22 (2 days before this record), no journal-ref, no peer review, arXiv non-exclusive license; expect revision risk (a v2 could change every number here).
- `underspecified` — unit of the `Tot. Ret.` column; rebalance intraday timing; S&P 500 point-in-time membership construction; `γ = 16.81` vs `γ_mr = 19.91`; whether the market benchmark's own index-rebalance turnover is charged the same 15 bps (the source notes `C^π` is relative and the benchmark *"itself incurs some turnover … when the S&P 500 constituent set changes"*, so increments *"need not be nonnegative in general, although they are positive throughout our monthly backtests"*).
- `data gap` — transaction-cost *rate* sensitivity (single 15 bps point), spread, market impact, latency, borrow fees/rebates, margin, capacity/ADV, dividend detail beyond the `D̂` term, timezone/session convention, and any treatment of corporate actions beyond the referenced Ruf/CRSP pipeline.
- `data gap` — code repository has **no license file** at the pinned SHA (GitHub API `"license": null`); publicly readable but legally unlicensed → do not vendor the code into our stack without clarification.
- Identification: the strategy is a **two-portfolio timing problem**, not a cross-sectional alpha; the only "alpha-like" evidence (factor regressions) is explicitly non-robust in the source. Its economic content may be better described as **concentration-regime risk management** than as return prediction.
- Selection/overfit surface: two forecast specs, a chosen active-vol target, a chosen forecast horizon `M`, a chosen cost rate, and an in-sample-estimated dispersion scaling — all frozen OOS (good), but the *choice set* itself was not exposed to any multiple-testing control (`data gap`).
- Sample: single country, single index, 30-year OOS ending 2024 (no 2025–2026 data); parameters never re-estimated OOS (conservative, but also means a genuine structural break would go undetected — the authors themselves flag this).
- `unproven` — crypto portability (see section above).

## Implementation status

`implementation_status: not-implemented`.

No component of this strategy has been implemented in our research stack. Specifically: no Qlib full backtest, no production card, no candidate-pool entry, no Paper, no Testnet, no Live run, no Wiki Brain ingestion. The only artifacts produced by this capture are (a) this record and (b) the pinned source pointers above. Running the upstream notebook (`notebooks/3_backtest.ipynb`) was **not** done here.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this record in the staging repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. Any adoption decision requires the separate, explicit, gated review process described in the repository README, and — given the negative evidence above — would first require at least F1, F2 and F6 to be executed and passed.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — canonical schema contract (read and verified for this run; `schema: strategy-research-record-v1`).
- Wiki Brain searches run this cycle (`equal-weighted portfolio market concentration active allocation`, `stochastic portfolio theory diversity dispersion functionally generated`, `equal weight portfolio`, `concentration regime equity index rotation`) returned **no directly related strategy record** — i.e. no existing Wiki record on diversity/dispersion-driven equal-weight timing was found. Absence is a search result, not a claim that none exists.
- Adjacent **repository** filenames (explicitly **repo files, not Wiki links**): `functionally-generated-portfolio-diversity-entropy-smallcap-stochastic-cost-2026-09-22.md` (Karimi & Salavati, arXiv:2507.09196 — static functionally generated portfolios under stochastic transaction costs, small-cap universe; materially different: no forecast-driven timing control, different universe, different cost treatment), `cross-asset-reconfiguration-premium-subdominant-eigenspace-vrp-2026-09-02.md` (subdominant-eigenspace dispersion risk-premium on S&P 500 monthly returns — dispersion as a VRP/eigenspace signal, not an equal-weight tilt), `us-equity-vortex-top2-cross-sectional-trend-phase-robustness-2026-09-13.md` (cross-sectional equity trend with liquidity gating — different mechanism and horizon). All three exist as files in this repository; none shares this source identity.

## Sources

1. Brian Ceco, Xiaofei Shi, Ting-Kam Leonard Wong. *"Active Portfolio Management in Concentrated Equity Markets."* arXiv:2609.27113v1 [q-fin.PM, math.OC, q-fin.MF], submitted 22 Sep 2026 22:08:37 UTC; 31 pages, 11 figures; preprint only (no journal-ref, no DOI on landing page); arXiv non-exclusive distribution license. https://arxiv.org/abs/2609.27113 (landing page) and https://arxiv.org/html/2609.27113v1 (full text used for all table/figure/section citations above: Table 1, Table 2, Table 3, Table 4, Table 5, Figure 1, Figure 2, Figure 7, Figure 9, Figure 10, Figure 11, §2.1, §3.1, §3.2, §4.1, §4.2.1, §4.2.3, §4.3.1, §4.3.2, §4.3.3, §4.3.4, §4.3.5, §5, Remark 2.11).
2. Code repository: https://github.com/brianceco/apm-in-cem at commit **`ae75eb5803c09b3a2bbd4965cea556831c6cd4aa`** (2026-09-24); recursive tree inspected (24 entries, non-truncated); `notebooks/3_backtest.ipynb`, `src/backtest.py`, `configs/config.json`; no license file at that commit. GitHub API metadata: created 2026-09-18, pushed 2026-09-24, default branch `main`.
3. *Referenced by the primary source, not opened independently in this run (secondary-provenance markers):* Johannes Ruf & Kangjianan Xie, "The impact of proportional transaction costs on systematically generated portfolios," SIAM J. Financial Math. 11(3):881–896, 2020 (cost root-find methodology, ref [43]); Byran H. Taljaard & Eben Maré, "Why has the equal weight portfolio underperformed and what can we do about it?", *Quantitative Finance* 21(11):1855–1868, 2021 (predecessor binary selector and 15 bps level, ref [48]); Johannes Ruf, "Empirical finance with equity data (Ph.D. course)," https://github.com/johruf/CRSP_on_WRDS_introduction, 2023 (data pipeline, ref [42]); S&P Dow Jones Indices, "FAQ: Cboe S&P 500 Dispersion Index," 2023 (ref [47], DSPX comparison series); Ken French data library (risk-free rate for Table 3 Sharpe ratios, ref [17]); CRSP US Stock Databases (data vendor).
