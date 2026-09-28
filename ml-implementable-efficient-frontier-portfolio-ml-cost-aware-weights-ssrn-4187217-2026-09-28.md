---
schema: strategy-research-record-v1
title: "Cost-aware machine learning that learns portfolio weights directly: the implementable efficient frontier on NYSE equities 1981-2020 (Portfolio-ML net Sharpe 1.33, gross-to-net collapse of Markowitz-ML)"
created: 2026-09-28
updated: 2026-09-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - us-equity
  - nyse
  - portfolio-construction
  - machine-learning
  - transaction-costs
  - cost-aware-optimization
  - implementable-efficient-frontier
  - economic-feature-importance
  - published-journal
status: research-only
confidence: medium
source_as_of: "2026-03-15"
sources:
  - "https://academic.oup.com/rfs/article/39/10/3035/8524346 — canonical (DOI https://doi.org/10.1093/rfs/hhag022 → HTTP 302, verified 2026-09-28), The Review of Financial Studies, Volume 39, Issue 10, October 2026, Pages 3035–3078, JOURNAL ARTICLE / EDITOR'S CHOICE, Published: 15 March 2026"
  - "pinned primary text: local accessibility snapshot of that RFS article HTML, 278,571 bytes, 5,323 lines, sha256 0c7bf6cd64606bfa0533fadfe84cf5fdb3eaf9e40f9f472d7b53bd4c2fb207b1, captured 2026-09-28, kept outside the repo in the Hermes cache; equations recovered from inline MathML (e.g. eq. (4) dollar t-costs = ½τ′Λτ, eq. (11) empirical utility, eq. (34) Static-ML solution, eq. (35) Λᵢ,ₜ = 0.2/Vᵢ,ₜ)"
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4187217 — working-paper landing page (read 2026-09-28), doi 10.2139/ssrn.4187217, Swiss Finance Institute Research Paper No. 22-63"
  - "https://github.com/theisij/ml-and-the-implementable-efficient-frontier — code repository, main HEAD 13d836b5187cbfa69730dd256d8eb767e65ca21f (git ls-remote 2026-09-28; GitHub API pushed_at 2025-03-06T00:34:38Z)"
  - "https://github.com/bkelly-lab/ReplicationCrisis/tree/master/GlobalFactors — factor code/documentation cited in RFS footnote 10; data: WRDS Global Factor Data (footnote 10)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Four unreconciled date expressions for the same work: SSRN 'Posted: 18 Aug 2022' and 'Last revised: 19 Aug 2022' vs SSRN 'Date Written: June 19, 2024' and Suggested Citation '(June 19, 2024)' vs RFS 'Published: 15 March 2026' and issue 'October 2026'. Which version produced which numbers is not stated (SSRN PDF retrieval was blocked → data gap)."
  - "The SSRN landing page contradicts itself: article headings read '0 References' and '0 Citations', while the 'Paper statistics' sidebar on the same page reads '13 Citations' and '50 References'."
  - "Version length divergence: SSRN states '88 Pages'; the pinned RFS version prints Pages 3035–3078 (44 printed pages). All numbers in this record are pinned to the RFS HTML; no SSRN-era numbers were carried over."
  - "Code/data homes are inconsistent: RFS 'Code Availability' states the replication code is in the Harvard Dataverse 'at this link' (anchor target not resolvable from the pinned snapshot → data gap), §5 points at theisij/ml-and-the-implementable-efficient-frontier, and footnote 10 points at bkelly-lab/ReplicationCrisis/GlobalFactors plus WRDS. No single canonical artifact hash is published."
  - "§6.4 states 'we use data from Markit covering 2003–2020' while footnote 20 states 'The indicative fee is only available from 2017 to 2020'; the 2003–2016 span is filled by imputation (daily cost-of-borrow-score medians), so the headline 18-year window is partly constructed, not raw."
  - "Table 3 caption calls each cell 'the p-value in the test of whether the average utility of the portfolio choice method in the row is greater than the column method', yet the same cells are framed in prose and in §6.1 as probabilities of superiority (Portfolio-ML row: 99.9%, 99.9%, 100.0%, 100.0%). Probability and p-value readings invert; the source does not reconcile them."
---

# Machine Learning and the Implementable Efficient Frontier (Jensen, Kelly, Malamud, Pedersen)

> Epistemic boundary: everything under **Source-reported** is the primary source's claim, marked `source-reported`, with Table/Figure/Section provenance. Everything under **Research interpretation**, **Research-proposed** and **Research-defined** is Scout-generated. This record is `research-only / not-implemented / not-approved / approval_scope: research-only`; the results below are **not independently reproduced**.

## Provenance

- **Title:** Machine Learning and the Implementable Efficient Frontier.
- **Authors (complete list, exactly as printed on the pinned RFS page):** Theis Ingerslev Jensen; Bryan Kelly; Semyon Malamud; Lasse Heje Pedersen. (The SSRN working-paper landing page prints the same four with middle initials — "Bryan T. Kelly" — and lists affiliations: Yale University; Yale SOM / AQR Capital Management, LLC / NBER; Ecole Polytechnique Federale de Lausanne / CEPR / Swiss Finance Institute; Copenhagen Business School – Department of Finance / AQR Capital Management, LLC / CEPR.)
- **Venue / version read:** *The Review of Financial Studies*, Volume 39, Issue 10, October 2026, Pages 3035–3078; DOI `10.1093/rfs/hhag022`; page badges "JOURNAL ARTICLE" and "EDITOR'S CHOICE"; `Published: 15 March 2026`; editor named on the page: Itay Goldstein. Copyright line: "© The Author(s) 2026. Published by Oxford University Press on behalf of The Society for Financial Studies", with a `https://creativecommons.org/licenses/by-nc-nd/4.0/` licence link.
- **Publication status (step 5b g):** peer-reviewed, published journal article (not a preprint). A working-paper version also exists: SSRN `abstract_id=4187217`, doi `10.2139/ssrn.4187217`, Swiss Finance Institute Research Paper No. 22-63, "88 Pages", `Posted: 18 Aug 2022`, `Last revised: 19 Aug 2022`, `Date Written: June 19, 2024`. Contradictions about dating are listed in the frontmatter.
- **Pinned primary text:** local accessibility snapshot of the canonical RFS article HTML — 278,571 bytes / 5,323 lines / `sha256 0c7bf6cd64606bfa0533fadfe84cf5fdb3eaf9e40f9f472d7b53bd4c2fb207b1` (captured 2026-09-28, cache, not committed). Read end to end: §1–§8, Table 1–4, Figure 1–8 captions/alt text, footnotes 1–20, Author notes, References, Code Availability, Acknowledgement. Equations were recovered from inline MathML, so formula-level claims below cite equation numbers.
- **Direct-PDF status:** the OUP PDF endpoint returned HTTP 400 "Token provided is not valid…" on 2026-09-28 and the SSRN `Delivery.cfm` PDF was bot-blocked → **PDF byte-for-byte checksum `data gap`**; all numbers below are pinned to the RFS HTML snapshot above, never mixed with the SSRN version.
- **Dedup (step 5, full-repo `rg -uuu`, incl. `.git`, `.mimo-worktrees`, `.agents`, `.hermes`, `coverage_manifest.csv`):** `4187217`, `hhag022`, `implementable efficient`, `theisij`, `economic feature importance`, `Multiperiod-ML`, `Portfolio-ML` → no record carries this source identity. Two *existing* records only cite it in passing and explicitly defer to it: `reviving-anomalies-expected-net-return-double-sort-1n-implementable-2026-09-23.md` (F8 names it as a competing benchmark) and `retail-option-imbalance-slim-cross-section-us-equity-ssrn-6781743-2026-09-28.md` (states the Jensen-Kelly-Malamud-Pedersen frontier framework is "not read for this record — data gap"). Positive control `novy-marx` matched 11 files, so the search is alive. **Re-run this run after `git pull origin main` (5845757 → 58a9fde, another Scout's TradingView ATR/ADX record): the seven identity terms still match only this draft plus `reviving-anomalies-…-2026-09-23.md` (on the phrase "implementable efficient"); `retail-option-imbalance-…-2026-09-28.md` matches none of the seven and was re-checked separately on `jensen|frontier framework|not read for this record` (three hits, all citation-only); `novy-marx` positive control now 22 files.** Wiki Brain `kb_search "implementable efficient frontier"` → 0 pages (re-checked this run). **No `*-spec-v2.md` resolution issue this run: `quant/strategy-research-record-spec-v1.md` read as canonical.**
- **source vs research:** every performance/statistical number below carries its Table/Figure/Section anchor. The only Scout-computed values are explicitly tagged `research-computed` (`0.144` from displayed Table 2 cells; `170 bp` from §6.2's 16.3% − 14.6%).

## Economic mechanism

### Source-reported

`source-reported` (Abstract; §1.2, §1.4, §3.1–§3.3, §7)

- Strategies should be judged by **net-of-trading-cost return at each level of risk** — the "implementable efficient frontier" (IEF) — rather than by frictionless, in-sample frontiers (§1.4, §7).
- The failure mode: return-forecast ML is agnostic to trading costs, so it leans on **fleeting small-scale characteristics** (high-turnover signals) whose predictive content cannot pay for its own trading (Abstract, §6.3).
- The fix has two halves: (i) a **trading-cost-aware** portfolio problem with predictable returns, solved approximately in closed form (Gârleanu–Pedersen style amortization term, §3.1–§3.2, eq. (4)/(21)–(24)), then (ii) **learning the portfolio weights directly** with an economic (utility) objective instead of learning returns and plugging them into an optimizer (§3.2, §5.2.3). With wealth scaling `wΛ`, gross return `r′π` and dollar costs `½τ′Λτ` (eq. (4)), the optimizer learns `β_T = (E[Σ̃_t] + λI)⁻¹E[r̃_{t+1}]` for `A(s_t) = f(s_t)β` (Portfolio-ML, §5.2.3).
- Theory claims: the optimal policy is `m g_t π_{t−1} + (I − m) A_t` (Propositions on amortization, §3.2); the IEF **shrinks with wealth** because impact is increasing in trade size (§1.4, §6.2); a new **economic feature importance** measure equals the utility drop when a feature's information is destroyed (§3.3, §6.3, eq. (43)); high-frequency features lose value once costs bind (§3.3, §6.3).

### Research interpretation

`research-proposed`

- Treat this as a *portfolio-construction alpha hypothesis*, not a return-forecast claim: the investable edge is **where a signal's utility survives costs**, i.e. an interaction of (signal persistence × signal strength × capacity), not of signal strength alone.
- Falsifiable core: *on a point-in-time large-cap universe, learning weights under a quadratic impact cost model produces a strictly better net-of-cost frontier than any forecast-then-optimize pipeline at equal information*, and the ranking of signal themes by *gross* importance is not the ranking by *net* importance (§6.3's reversal-vs-quality reversal is the sharpest testable consequence).
- Source itself supplies the attack surface: if the cost model is misspecified (no commission/spread/fill), the "net" frontier is an artifact — hence F1/F2/F7 below.

## Signal

**A. Source-reported inputs and construction** (`source-reported`, §5.1.1, §5.1.3, §5.1.4, §5.2, Table 1)

- **115 stock characteristics** "studied in Jensen et al. (2023)" (§5.1.1); footnote 12: Jensen et al. (2023) study 153 features, "here, we exclude features with poor coverage early in the sample" (153 → 115, `data gap`: per-feature exclusion list lives in Internet Appendix Table D.1, not in the pinned text).
- Each feature is **rank-transformed cross-sectionally each month into [0,1]**; missing values set to **0.5**; a month needs **at least 57 nonmissing features** (§5.1.1).
- `r_{t+1} = μ(s_t) + ε_{t+1}` with `Σ(s_t) = Var_t(ε)`; features feed three consumers (§5.2): Multiperiod-ML, Static-ML, Portfolio-ML.
- **Model class:** random Fourier features + ridge. `RF(s) = (1/√p)[sin(s′w₁), cos(s′w₁), …, sin(s′w_{p/2}), cos(s′w_{p/2})]′`, `w_j ∈ R^115 ~ iid N(0, η²I)`; portfolio form `A_t = diag(1/σ_{i,t}) RF(s_t) β` with `σ_{i,t} = √Σ_{t,ii}` (§5.2.3).
- **Multiperiod-ML:** twelve independent models for excess returns in months `t+1, t+2, …, t+12` (§5.2.1, MathML `t+1,t+2,…,t+12`).
- **Portfolio-ML:** approximates the infinite-horizon sum of past signals using a trailing window of past signals (§5.2.3). **Exact window endpoints are `underspecified` in the pinned text** (rendered only as MathML symbols that do not extract as numerals → `data gap`, not inferred).
- **Hyperparameters (Table 1):** `λ ∈ {0, e⁻¹⁰, e⁻⁹·⁸, …, e¹⁰}` for all three methods; `p = {2⁶, 2⁷, 2⁸, 2⁹}` (Portfolio-ML) vs `{2¹, 2², …, 2⁹}` (Multiperiod-ML, Static-ML); `η ∈ {e⁻³, e⁻²}`. Second layer (`Multiperiod-ML*`, `Static-ML*` only): `u ∈ {0.25, 0.50, 1.00}` scales expected returns, `v ∈ {1, 2, 3}` adds `v·diag(σ_t)` to covariance, `k ∈ {1, 2, 3}` (Multiperiod) / `{11, 13, 15}` (Static) scales `Λ` (§5.3, Table 1).
- **Selection rule (§5.3):** hyperparameter `h*` is re-selected every year `y ≥ 1971` by realized utility of the training run through year `y−1` (validation backtests begin 1971); the second layer `h*` likewise from `u, v, k` grids using only data through `y−1`. Out-of-sample backtest = **1981–2020**.
- **Ranking of themes (§6.3, Figure 5/6):** net-of-cost for Portfolio-ML at `$10B`, importance order ≈ **quality > value > momentum > investment**, then a "substantial drop" for the rest; **short-term reversal** is important only in the frictionless Markowitz-ML benchmark (Figure 5 alt text: "short-term reversal is an important feature for the Markowitz-ML method. However, when taking transaction costs into account … short-term reversal is no longer economically important due to its high turnover. Instead, signals such as quality, value, momentum, and investment are important net of transaction costs."). Figure-only bar heights → exact FI values `data gap` (numbers are in Figure 5, not in printable text).

**B. Scout operationalization** (`research-proposed`, none of this is from the source)

- If a later implementable version is ever built: freeze the theme grouping to the source's 13 themes (Jensen et al. 2023, Internet Appendix Table D.1), rank-transform to [0,1] monthly, missing → 0.5, drop months with <57 nonmissing — all source-specified; anything beyond that (which of the 115 features are kept, universe expansion, rebalance calendar outside monthly) must be re-labelled `research-proposed`.

## Required data

**Source-reported** (`data gap` where the source does not fully specify)

| Item | What the source pins | Status |
|---|---|---|
| Returns / prices | CRSP monthly returns, market equity, dollar volume; common stocks (`shrcd` 10/11/12, `exchcd` 1 = NYSE) | source-reported (§5.1.2) |
| Accounting | Compustat, SIC codes, nonmissing ME/return/dollar volume/SIC | source-reported (§5.1.2) |
| Features | 115 characteristics from Jensen et al. (2023) | source-reported; per-feature list in Internet Appendix Table D.1 → `data gap` in pinned text |
| Risk model | 12 industry dummies (SIC→Kenneth French 12 industries, eq. (36), fn. 14) + 13 theme characteristics (eq. (36); >100 characteristics reduced to 13 themes), factor risk = EWMA of factor returns over the **past 10 years of daily observations** with exponential decay, **half-life 378 days for correlations and 126 days for variances** (fn. 15: BARRA USE4 uses 84d short-term variances / 252d long-term variances / 252d correlations); idiosyncratic variance = EWMA of squared residuals from eq. (36) with **half-life 126 days**, requiring **at least 200 nonmissing observations within the last 252 trading days** (otherwise the median idiosyncratic variance of stocks in the same size group) | source-reported (§5.1.5, eq. (36)–(37), fn. 14, fn. 15); Fama–French-3-factor + momentum style code per fn. 10 |
| Factor data | `bkelly-lab/ReplicationCrisis/GlobalFactors`; WRDS Global Factor Data | source-reported (fn. 10) |
| Cost input | expected daily dollar volume = **average daily dollar volume over the last 6 months**, per stock | source-reported (§5.1.4) |
| Shorting fees | Markit "indicative fee" + daily cost-of-borrow score (DCBS 1–10), 2003–2020, with stated imputation (fn. 20) | source-reported, partly imputed |
| Universe counts | above-median-ME sample: min **184**, median **646**, max **805** stocks; all-NYSE: **401 / 1,270 / 1,579** | source-reported (§5.1.2) |
| Sample | estimation sample Dec **1952**–Dec **2020**; validation backtests from **1971**; OOS backtest **1981–2020** | source-reported (§5.1.2, §5.3, Table 2 caption) |
| Point-in-time rule | stock enters after 12 months satisfying all restrictions, exits after 12 failing; baseline restricted to above-NYSE-median market cap (§6.5 relaxes) | source-reported (§5.1.2, §6.5) |
| Redistribution | CRSP/Compustat/WRDS/Markit are licensed (not redistributable) | source-implied; direct replication requires subscriptions → `data gap` on cost-free replication |

## Execution assumptions

**Source-reported** (`source-reported`; every judgement uses Methods-level reading of §1.1, §5.1.4, §5.2, §6.4, footnotes — not the abstract)

- **Rebalance:** monthly, `w_t = w_{t−1}(1 + g_{t+1}w)` drift between trades; OOS window "rebalanced monthly from 1981 to 2020" (Table 2 caption).
- **Trading cost model (impact only):** dollar t-costs `TC_t = ½ τ_t′ Λ_t τ_t` (eq. (4)), diagonal `Λ` with **`Λ_{i,t} = 0.2 / V_{i,t}`** (eq. (35)), `V_{i,t}` = expected daily dollar volume (6-month average). Stated equivalent, verbatim §5.1.4 prose: "we assume that the market impact … is **0.1% when trading 1% of the daily dollar volume in a stock**"; worked example in §5.1.4 — "$5 million over a day in a stock with a daily volume of $500 million … leading to a transaction cost of $5,000" (= 0.1% of $5M, source-stated). Calibration source: **Frazzini, Israel, and Moskowitz (2018)**. Costs scale with the **square** of wealth (§1.1), which is what makes `wΛ` linear in wealth.
- **Costs are re-estimated monthly but treated as constant inside each optimization** (§5.1.2/§5.1.4 stated approximation).
- **Short selling:** long-short weights are allowed (sum to 1, may be negative); shorting fees are modelled only in §6.4 as an annualized utility deduction (0.5% / 1.2% / 1.1%), with lending revenue **70%** retained (Muravyev et al. 2022 convention, §6.4).
- **Cash / growth:** excess-return formulation; investor's dollars grow at the realized market return `w_t = w_{t−1}(1+R_{m,t})` (§2.2), so AUM is an exogenous wealth path, not a P&L-compounding account.
- **Utility (evaluation metric):** `utility_T = (1/T) Σ_t [r^{gross}_{t+1} − TC_t − (γ/2)(r^{net}_{t+1} − r̄^{net})²]` (eq. (11)), **γ = 10** (Table 2 note); frontier grid uses `γ ∈ {1, 5, 10, 20, 100}` and end-2020 wealth `w ∈ {0, 10⁹, 10¹⁰, 10¹¹}` (§6.2, §7, MathML).
- **Explicitly NOT modelled in the pinned text — word scan of the full snapshot returns 0 occurrences of each:** `commission(s)`, `bid-ask`/`bid`, `spread`, `slippage`, `latency`, `fill`, `participation`, `execution`, `order type`/`market order`/`limit order`, `capacity`, `margin` (financing), `financing`, `funding`, `liquidation`, `tax(es)`, `constraint` (0 occurrences of "constraint" anywhere → position/sector/borrow availability limits are `data gap`, **not** "no limits"). Present instead: `market impact` ×8, `trading cost`/`transaction cost` (dominant), `shorting fee` ×4, `turnover` ×14, `leverage` ×4, `risk-free` ×9. **These are `data gap`/`underspecified`, never "zero cost".**
- **Leverage:** `Lev.` = sum of absolute portfolio weights, averaged (Table 2 note). No margin/financing cost is charged on gross leverage (`Portfolio-ML` 3.00, `Multiperiod-ML*` 5.69, `Static-ML*` 5.27, `Markowitz-ML` 74.61) → financing drag `data gap`.
- **Turnover:** sum of absolute changes in portfolio weights, averaged over time, monthly (Table 2 note) — reported, so no gap here.

## Evidence

### Source-reported

`source-reported` — all rows are the pinned RFS HTML, OOS 1981–2020, monthly rebalance, `γ = 10`, NYSE above-median-ME baseline, `$10B` end-2020 wealth.

**Table 2 "Out-of-sample performance statistics"** (columns: R gross, Vol., SR gross, TC, R-TC, SR net, Utility, Turnover, Lev. — `–`/`+` mean "extremely low/high value" per table note; negative utilities carry a math-rendered minus sign):

| Method | R | Vol. | SR gross | TC | R-TC | SR net | Utility | Turnover | Lev. |
|---|---|---|---|---|---|---|---|---|---|
| Portfolio-ML | 0.15 | 0.11 | 1.38 | 0.006 | 0.15 | **1.33** | **0.086** | **0.25** | 3.00 |
| Multiperiod-ML | 0.38 | 0.33 | 1.15 | 0.293 | 0.09 | 0.26 | −0.453 | 1.70 | 15.75 |
| Static-ML | 0.26 | 0.28 | 0.95 | 0.044 | 0.22 | 0.79 | −0.165 | 0.80 | 12.78 |
| Markowitz-ML | 2.78 | 1.35 | **2.06** | + | – | – | – | 79.36 | 74.61 |
| Factor-ML | 0.11 | 0.13 | 0.84 | 2.509 | −2.40 | −18.09 | −2.487 | 2.79 | 2.00 |
| Rank-ML | 0.08 | 0.07 | 1.16 | 1.266 | −1.18 | −16.73 | −1.210 | 1.81 | 2.00 |
| Minimum variance | 0.11 | 0.11 | 1.03 | 0.824 | −0.71 | −6.41 | −0.771 | 1.35 | 2.57 |
| 1/N | 0.10 | 0.17 | 0.57 | 0.004 | 0.09 | 0.54 | −0.051 | 0.07 | 1.00 |
| Market | 0.08 | 0.15 | 0.52 | 0.000 | 0.08 | 0.51 | −0.033 | 0.01 | 1.00 |
| Multiperiod-ML* (2 layers) | 0.15 | 0.14 | 1.10 | 0.036 | 0.12 | 0.83 | 0.020 | 0.58 | 5.69 |
| Static-ML* (2 layers) | 0.12 | 0.10 | 1.15 | 0.035 | 0.08 | 0.81 | 0.030 | 0.68 | 5.27 |

Provenance: RFS §6.1 + Table 2 caption ("out-of-sample performance … rebalanced monthly from 1981 to 2020"; "Utility … excess return after trading cost minus one-half times the assumed risk aversion of 10 times the realized portfolio variance"). Scout arithmetic check (labeled `research-computed`): `0.15 − 0.006 = 0.144` against the printed `0.15` (rounding-compatible), and each net column satisfies `R − TC = R-TC` to displayed precision.

- **Turnover mechanism (§6.1):** "lower monthly turnover of **25%** relative to **58%** and **68%** for Multiperiod-ML* and Static-ML*" — the stated reason for Portfolio-ML's outperformance.
- **Gross winner is the net loser (§6.1):** "the Markowitz-ML method is the clear winner with an impressive gross Sharpe ratio of **2.06**" while its TC is marked `+` and its net columns `–`.
- **Table 3 "Relative probability of outperformance"** (prob. row > column, uninformative prior + normality): Portfolio-ML vs Multiperiod-ML* **99.9%**, vs Static-ML* **99.9%**, vs Factor-ML **100.0%**, vs Markowitz-ML **100.0%**; Multiperiod-ML* vs Static-ML* **27.1%** (so Static-ML* 72.9%); inverse cells 0.1% / 0.0%. §6.1 prose: "we can reject that Portfolio-ML delivers a lower realized utility than the other methods at conventional levels of significance." (Caption-vs-prose p-value inversion → frontmatter contradiction.)
- **Table 4 "Portfolio correlations"** (caption: "the time-series correlation of the returns **before trading costs** for the various portfolio choice methods, 1981–2020"; lower triangle): Portfolio-ML with Multiperiod-ML* **0.61**, Static-ML* **0.52**, Factor-ML **0.26**, Markowitz-ML **0.26**; Multiperiod-ML* with Static-ML* **0.80**, Factor-ML **0.35**, Markowitz-ML **0.48**; Static-ML* with Factor-ML **0.40**, Markowitz-ML **0.58**; Factor-ML with Markowitz-ML **0.40**; §6.1 comment: "The correlation between Portfolio-ML and Markowitz-ML is only 0.26, indicating that the marginal utility of an investor with $10 billion using Portfolio-ML could be very different from risk adjustments in a frictionless market."
- **Size of the frontier (§6.2, Figure 1(B)):** "an investor with `$10B` and a relative risk aversion of 10 gets a net excess return of **14.6% at 11% volatility**. If the investor had `$1B` instead, the same volatility would provide a net excess return of **16.3%**" → `research-computed` gap = **170 bp** of net return lost to size at fixed 11% vol. **No unique frontier once costs bind** (§6.2, §7).
- **Economic feature importance (§6.3, Figure 5/6):** net-of-cost Portfolio-ML ranks **quality** first, then value, momentum, investment; **short-term reversal drops out** because "the 1-month reversal factor … monthly autocorrelation [is] … not just low but actually negative, giving rise to large portfolio turnover"; comparators: book-to-market autocorrelation **0.94**, median quality feature **0.93**, 12-month momentum **0.87** (§6.3; footnotes 18–19 define the autocorrelation estimator: average across stocks with ≥5 years of monthly obs). Counterfactual frontiers (Figure 6, `γ ∈ {1,5,10,20,100}`): shuffling quality/value moves the net frontier; shuffling reversal "barely changes" it — while all three matter before costs (Panel B).
- **Short-selling costs (§6.4, Figure 7):** annualized deduction **0.5% for Portfolio-ML, 1.2% for Multiperiod-ML*, 1.1% for Static-ML***; "by the end of our sample in December 2020, the median shorting fee is **0.30% per year** and the **99th percentile is 1.1%**"; low because the universe is large and liquid; 70% of lending revenue retained.
- **Size distribution (§6.5, Figure 8):** all-NYSE sample → Portfolio-ML best, then Multiperiod-ML* > Static-ML*, all others negative utility; ranking stable in **the four largest size groups**; **in the smallest (0th–20th percentile) group Multiperiod-ML* and Static-ML* beat Portfolio-ML** ("This finding is surprising…"); Internet Appendix E simulation (stocks never disappear, high data quality, stable DGP) restores the predicted dynamic-over-static advantage, larger for illiquid stocks. Exact per-bucket utilities are figure-only → `data gap`.
- **Implementation difficulty (footnote 3):** "real-time data on many characteristics across more than a thousand stocks … infrastructure for continually updating and trading these models, all of which would be challenging for small investors to implement."
- **Disclosure (Acknowledgement):** "Malamud is a consultant for AQR. AQR Capital Management … may or may not apply similar investment techniques … The views expressed here are those of the authors and not necessarily those of AQR." Funding: Center for Big Data in Finance DNRF167; Swiss Finance Institute / SNSF 100018_192692; INQUIRE Europe.

### Independently reproduced

**Nothing.** `not independently reproduced`. No backtest was run, no data was licensed, no code from `theisij/ml-and-the-implementable-efficient-frontier` was executed. Table 2/3/4 cells were re-read cell-by-cell from the pinned snapshot and cross-checked for internal arithmetic consistency only (net column = R − TC; net Sharpe ≈ (R−TC)/Vol; utility ≈ net − 5·vol² — see `0.144`, `0.086`, `0.030`, `−0.033`), which is a *self-consistency check of the source*, not a reproduction of its results.

### Negative evidence

`source-reported unless marked otherwise` (each item is either the source's own admission or a source-reported result that cuts against usability)

1. **Gross-to-net destruction:** Markowitz-ML gross SR **2.06** → TC `+`, net `–` (Table 2, §6.1); Factor-ML 0.84 → R-TC −2.40 (SR −18.09); Rank-ML 1.16 → −1.18; Minimum variance 1.03 → −0.71. Every frictionless-optimizer benchmark is net-infeasible.
2. **One tuning layer is not enough:** Multiperiod-ML and Static-ML have *positive* net Sharpe (0.26, 0.79) yet **negative realized utility (−0.453, −0.165)** — scaling failure (Table 2; §5.3 explains "out-of-sample returns and risks for optimized portfolios do not match the scale of their ex ante expected versions").
3. **The second tuning layer is partly hand-tuned:** §5.3 admits the `u, v, k` search was chosen "based on some experimentation" — a source-stated risk of benchmark favoritism.
4. **Short-term reversal is worthless to a large investor net of costs** (§6.3, Figure 5/6): important only in the frictionless benchmark; 1-month reversal autocorrelation is *negative* (exact value `data gap` — MathML), i.e. the source's own "fast signal" example fails economically.
5. **The IEF shrinks with size:** 14.6% vs 16.3% at 11% vol (`$10B` vs `$1B`, §6.2) — `research-computed` 170 bp penalty; Proposition-level claim that net Sharpe declines along the frontier as `w` rises (§1.4, §6.2).
6. **Ranking flips in the smallest bucket:** 0–20th percentile → Multiperiod-ML* / Static-ML* first, Portfolio-ML third (§6.5); "surprising … lower data quality may have a larger impact on more sophisticated methods."
7. **Universe was narrowed for tractability and for a database artifact:** baseline = above-NYSE-median market cap (§6.5: "mainly to ease the computational burden"); footnote 11: AMEX/Nasdaq excluded because their 1962/1972 CRSP entries create "large artificial turnover" that poisoned *validation*-period hyperparameters.
8. **Cost model is impact-only** (§5.1.4): commissions, spread, slippage, latency, fill/participation, capacity all have **0 occurrences** in the pinned text → `data gap`, so "net" here is narrower than a real broker P&L.
9. **No financing/short availability friction:** `margin`, `financing`, `funding`, `liquidation`, `constraint` all 0 occurrences → `data gap`; gross leverage up to 74.61 is charged nothing (§Table 2, §5).
10. **Shorting-fee evidence is imputed:** raw indicative fee only 2017–2020 (fn. 20), extended by DCBS medians over 2003–2020 (§6.4).
11. **Sample ends Dec 2020** (§5.1.2) although the article was published 15 March 2026 — **no post-2020 evidence** in the pinned version.
12. **Infrastructure barrier** (fn. 3): explicitly "challenging for small investors to implement".
13. **External contrary finding the source itself cites:** Muravyev et al. (2025) "Anomalies and their short-sale costs" — anomalies' abnormal returns are sensitive to shorting costs (References list; §6.4 uses Muravyev et al. 2022 for the 70% lending-revenue convention).
14. **Real-time caveat (§6.1/§7 wording):** the frontier is an out-of-sample *simulation* over 1981–2020 with pre-chosen `γ` grid and hyperparameters reselected annually from prior-year utility — no live trading, no execution shortfall, no market-close availability guarantee stated.
15. **Table 3's statistics are not multiple-testing adjusted** (5 methods, 10 pairwise cells, one uninformative-prior normality assumption) — `research-computed` observation from the caption's own method description; the source claims "conventional levels of significance" without a family-wise correction.

## Falsification plan

`research-defined` = thresholds below are Scout-proposed falsification gates, **not** source-specified. `research-proposed` items are operational choices the source does not pin. If a test FAILS, the hypothesis is weakened/abandoned — this record is research-only and approves nothing.

- **F1 Reproduction gate (research-defined):** re-run the pinned Table 2 baseline (NYSE above-median ME, 115 features, monthly, 1981–2020, impact model `½τ′Λτ`, `Λ=0.2/V`, 6-month ADV). FAIL if Portfolio-ML net Sharpe is not within `1.33 ± 0.10` or utility not within `0.086 ± 0.02` or monthly turnover not within `0.25 ± 0.05` (tolerances `research-defined`; source reports point estimates only).
- **F2 Cost-model ladder (research-defined):** add explicit per-side commission + half-spread on top of impact (0 / 1 / 5 / 10 bp per side, `research-proposed` ladder). FAIL the "net-of-cost superiority" claim if Portfolio-ML net Sharpe < 0.50 at 5 bp/side or ≤ 0 at 10 bp/side, or if its utility advantage over Static-ML* vanishes (< 0.01) at 5 bp/side.
- **F3 Forward window (research-defined):** extend the frozen protocol over 2021–2025 monthly data (no re-tuning beyond the source's annual rule). FAIL if Portfolio-ML realized utility ≤ 0 in that window or its Table 3-style superiority probability vs Static-ML* falls below 90%.
- **F4 Universe expansion (research-defined):** re-run with AMEX + Nasdaq included using point-in-time listing rules (footnote 11's artifact avoided). FAIL if Portfolio-ML is no longer ranked first by utility among all methods in the all-stock sample.
- **F5 Size-bucket robustness (research-defined):** replicate Figure 8's five buckets. FAIL the "uniformly best" reading if Portfolio-ML does not rank first in ≥ 4 of 5 buckets (source already predicts it loses bucket 0–20, so the pre-registered expectation is exactly one loss; two or more losses = FAIL).
- **F6 Economic-feature-importance replication (research-defined):** permute themes as in eq. (43). FAIL if the utility drop from permuting **quality** is not larger than from permuting **short-term reversal** in the net-of-cost Portfolio-ML run, or if reversal-permutation moves the net frontier as much as quality-permutation (Figure 6 qualitative claim).
- **F7 Capacity / participation audit (research-defined):** compute each stock's monthly trade as a fraction of its 6-month ADV at `$10B`. FAIL if > 10% of stock-months exceed 5% ADV participation (`research-proposed` thresholds) — i.e. if the headline result depends on trades the cost model never prices.
- **F8 Financing drag (research-defined):** charge financing on gross leverage (Portfolio-ML 3.00×, Multiperiod-ML* 5.69×, Static-ML* 5.27×) at `research-proposed` 50 bp/yr on gross exposure. FAIL if Portfolio-ML utility ≤ 0 or its rank vs Market/1/N changes.
- **F9 Short-sale feasibility (research-defined):** redo §6.4 with *raw* (non-imputed) fees only 2017–2020 and with borrow availability capped. FAIL if Portfolio-ML's utility drop exceeds 50% of 0.086, or if short legs become infeasible for > 20% of names-months.
- **F10 Statistical robustness (research-defined):** replace Table 3's uninformative-prior normal probabilities with a stationary block bootstrap of monthly utility differentials (12-month blocks, 10,000 draws, `research-proposed`). FAIL if the 95% CI of `U_PortfolioML − U_StaticML*` includes 0, or if any superiority probability falls below 95%.
- **F11 Placebo (research-defined):** permute feature cross-sections within month, then run the full pipeline. FAIL if placebo net Sharpe ≥ 0.50 or placebo utility ≥ 0.03 (i.e. the pipeline manufactures "net alpha" from noise/cost-model structure).
- **F12 Cost-law sensitivity (research-defined):** vary the impact law implied by `Λ=0.2/V` — re-calibrate to Frazzini et al. (2018) per-stock estimates and to participation exponents `α ∈ {0.5, 1.0}` (`research-proposed`). FAIL if Portfolio-ML's first-place rank flips for any admissible α.
- **F13 Selection-rule audit (research-defined):** replace the source's "highest realized utility through y−1" hyperparameter selection (§5.3, including the admittedly experimental `u, v, k` search) with a pre-registered grid fixed at 1980. FAIL if Portfolio-ML's edge over Multiperiod-ML* drops below p < 0.05 (two-sided, `research-defined`) or its turnover rises above 0.40.
- **F14 Crypto port test (research-defined):** translate the mechanism to a point-in-time perpetual-futures universe (research-proposed translation; no crypto claim exists in the source). FAIL the portability hypothesis if net utility (after funding, taker fees, and the same quadratic-impact form) ≤ 0, or if a point-in-time universe cannot be built without survivorship leakage.

## Crypto portability

**Status: `unproven`.** The pinned source is NYSE-only (§5.1.2 `exchcd = 1`), costs are equity market impact calibrated on Frazzini et al. (2018), and shorting uses Markit equity borrow fees (§6.4). **The word "crypto" does not appear in the pinned text; no crypto result exists — `data gap`, not a negative result.**

What would have to change (`research-proposed`, untested):
- Universe: point-in-time top-N perps by 30-day median dollar volume, with listing/delisting handled like §5.1.2's 12-month in/out rule to avoid the footnote-11 artifact.
- Cost matrix: replace `Λ = 0.2/V` with per-venue maker/taker schedules + funding cost as a separate drag; the quadratic-impact term would need re-derivation for order-book depth (F12/F14).
- Holdings: 24/7 mark-to-market, funding every 8h, isolated vs cross margin — the source's `w_t = w_{t−1}(1+R_m)` wealth path and `γ = 10` utility grid are equity-shaped and would be `research-proposed` re-specifications.
- Signal side: the 115 CRSP/Compustat characteristics have no crypto analogue; only the *mechanism* (learn weights under cost, rank themes by net utility drop) ports.

## Limitations

1. Results are `source-reported` and **not independently reproduced**; CRSP/Compustat/WRDS/Markit access is required for any attempt (`data gap` on free replication).
2. Pinned rendition is the **RFS HTML**, not the PDF (PDF endpoints blocked, 400/bot-wall); some equation symbols and figure bar heights are unrecoverable (`underspecified` where noted: Portfolio-ML lag window endpoints, Figure 5/6/8 numeric values, 1-month-reversal autocorrelation value).
3. Cost coverage is **impact-only + equity borrow fees**; commission/spread/latency/fill/capacity/margin are `data gap` (0 occurrences) — never treat them as modelled at zero.
4. Sample ends 2020; publication is 2026 → 5+ years of unexamined market structure (rates regime, zero-commission retail flow, meme episodes) sit outside the evidence.
5. Baseline universe is deliberately above-median-mecap NYSE only; AMEX/Nasdaq excluded for a database-artifact reason (fn. 11), so results do not transfer to small/illiquid or non-US crosses without F4.
6. Table 3 inference uses an uninformative prior + normality with no multiple-testing correction and an internally inconsistent probability/p-value caption (frontmatter contradiction 6).
7. Hyperparameter selection uses realized utility of prior years and an admittedly experimental second layer (§5.3) — selection-on-outcomes risk.
8. AUM path is exogenous (wealth grows at market return, §2.2) and leverage carries no financing cost — realized compounding, drawdown-driven deleveraging, and margin calls are outside the model.
9. Shorting-fee evidence is 14/18 years imputed (fn. 20); lending revenue fixed at 70% (§6.4 convention).
10. Source declares a conflict-relevant affiliation (Malamud consults for AQR; two authors AQR-affiliated) — disclosed in Acknowledgement, still a limitation for independent reliance.
11. Code provenance is fragmented (three homes, no artifact hash) → reproducibility risk; the Harvard Dataverse link target is `data gap` from the pinned snapshot.
12. This record covers **one** mechanism from a framework paper; the Internet Appendices (A–E) and Figures D.1–D.2 were not read → `data gap` on their contents.
13. Not a validated alpha: no walk-forward, no out-of-source cross-check, no comparison against this repo's other cost-aware records beyond citation-level (`research-proposed`).

## Implementation status

- **status:** `research-only`
- **implementation_status:** `not-implemented`
- **adoption:** `not-approved`
- **approval_scope:** `research-only`
- **reproduction:** `not independently reproduced`
- No code was written, no data was purchased, no backtest was run, no candidate pool / Qlib / Paper / Testnet / Live artifact was touched. Scratch files (word scans, snapshot) live in the Hermes cache and are **not** committed.

## Adoption boundary

Adoption is **not-approved** and out of scope for this record: it is a source-backed hypothesis card only. Any move beyond `research-only` requires (i) F1 reproduction on licensed data, (ii) F2/F7/F8 cost-and-capacity gates passing, (iii) a separate decision record with its own approval scope. `approval_scope: research-only` forbids wiring this into a live or paper trading path from this record alone.

## Related Wiki records

- [[quant/smart-predict-then-optimize-spo-plus-robust-portfolio-2026-09-05]] — adjacent predict-then-optimize lineage; this source's core claim is the opposite ordering (learn weights, not predictions).
- [[quant/crypto-hourly-bitcoin-walk-forward-cost-aware-execution-2026-09-01]] — cost-aware execution, different market/horizon; useful contrast for F14.
- [[quant/attention-factors-statistical-arbitrage-residual-portfolios-2026-09-02]] — net-of-cost policy optimization framing.
- [[quant/chronos-foundation-transformer-statistical-arbitrage-factor-residuals-2026-09-12]] — turnover/cost fragility of learned signals.
- [[quant/size-enhanced-left-side-momentum-resga-expected-shortfall-2026-09-04]] — same JKP feature-family lineage (Jensen et al. 2023 characteristics), different mechanism.

Repo-internal neighbors (not Wiki): `reviving-anomalies-expected-net-return-double-sort-1n-implementable-2026-09-23.md` (F8 cites this source as a competing benchmark — now captured here), `retail-option-imbalance-slim-cross-section-us-equity-ssrn-6781743-2026-09-28.md` (explicitly deferred this framework as a data gap), `us-equity-momentum-rebalance-timing-luck-tranching-cost-aware-ssrn-5747964-2026-09-27.md`.

## Sources

1. Jensen, T. I., Kelly, B., Malamud, S., & Pedersen, L. H. (2026). *Machine Learning and the Implementable Efficient Frontier*. **The Review of Financial Studies, 39(10), 3035–3078.** DOI: https://doi.org/10.1093/rfs/hhag022 (canonical read: https://academic.oup.com/rfs/article/39/10/3035/8524346, Editor's Choice, Published: 15 March 2026). Pinned HTML snapshot: 278,571 bytes, sha256 `0c7bf6cd64606bfa0533fadfe84cf5fdb3eaf9e40f9f472d7b53bd4c2fb207b1`, captured 2026-09-28. Licence: CC BY-NC-ND 4.0 link on page; © The Author(s) 2026, Oxford University Press on behalf of the Society for Financial Studies.
2. Working-paper version: SSRN **4187217** (doi 10.2139/ssrn.4187217), Swiss Finance Institute Research Paper No. 22-63, 88 pages, Posted 18 Aug 2022 / last revised 19 Aug 2022 / Date Written June 19, 2024 (landing page read 2026-09-28).
3. Code: https://github.com/theisij/ml-and-the-implementable-efficient-frontier — `main` = `13d836b5187cbfa69730dd256d8eb767e65ca21f` (`git ls-remote` 2026-09-28; GitHub API `pushed_at` 2025-03-06T00:34:38Z, `created_at` 2024-06-17, license field `null`).
4. Factor code/data cited by the source (footnote 10): https://github.com/bkelly-lab/ReplicationCrisis/tree/master/GlobalFactors and https://wrds-www.wharton.upenn.edu/pages/get-data/contributed-data-forms/global-factor-data/.
5. Calibration inputs named in the source (not re-read this run → `source-reported`, second-hand): Frazzini, Israel & Moskowitz (2018) for impact; Jensen, Kelly & Pedersen et al. (2023) for the 153→115 characteristics; Breiman (2001) for permutation importance; Gârleanu & Pedersen (2013) for the amortization solution; Muravyev et al. (2022, 2025) for lending revenue and short-sale costs; Manchero et al. (2011) BARRA USE4 half-life comparison (footnote 15); Kenneth French 12-industry classification (footnote 14).
