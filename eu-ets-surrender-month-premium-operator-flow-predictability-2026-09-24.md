---
schema: strategy-research-record-v1
title: "EU ETS Surrender-Month Premium and Operator Flow Imbalance Return Predictability (Cap-and-Trade Trading Frictions)"
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - carbon-markets
  - eu-ets
  - cap-and-trade
  - order-flow
  - informed-trading
  - compliance-deadline-seasonality
  - time-series-predictability
  - falsification
status: research-only
confidence: medium
source_as_of: 2026-06-16
sources:
  - "Nicola Borri, Yukun Liu, Aleh Tsyvinski, Xi Wu, 'Trading Frictions in Dynamic Cap-and-Trade Markets', arXiv:2606.03767v2 [econ.TH; q-fin.GN], v1 submitted Tue 2 Jun 2026 15:21:49 UTC, v2 submitted Tue 16 Jun 2026 07:10:27 UTC, CC BY 4.0, preprint only (no comments, no journal-ref, no publisher DOI). https://arxiv.org/abs/2606.03767"
  - "Pinned full-text HTML of the same paper (v2): https://arxiv.org/html/2606.03767v2"
  - "DataCite DOI for the arXiv record: https://doi.org/10.48550/arXiv.2606.03767 (resolves HTTP 200 to the abs page; this is an arXiv DOI, not a publisher DOI)"
  - "Underlying public data cited by the source: European Union Transaction Log (EUTL), https://ec.europa.eu/clima/ets/ , downloaded via https://www.euets.info (Abrell 2023 database) — data source attribution only, not an independent verification by this Scout"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Two different magnitudes are both labelled 'April premium paid by delayed buyers' and are never reconciled in v2: ~€5 billion (Sections 1 and 5.3, back-of-the-envelope using total net April purchases times ~10% predictable appreciation, stated as 2% of the total traded volume of regulated firms) versus ~€176 million per compliance cycle (Section 1, Section 4.4, Table 2 baseline 175.6, model-implied fixed point). Whether €5bn is a sample aggregate and €176mn a single-cycle model object is our inference, not stated by the source; the labels as printed are inconsistent in scale by roughly 28x per cycle."
---

# EU ETS Surrender-Month Premium and Operator Flow Imbalance Return Predictability (Cap-and-Trade Trading Frictions)

## Provenance

- **Primary source:** Nicola Borri (LUISS University, nborri@luiss.it), Yukun Liu (University of Rochester, yliu229@ur.rochester.edu), Aleh Tsyvinski (Department of Economics, Yale University, a.tsyvinski@yale.edu), Xi Wu (University of California, Berkeley, xiwu@berkeley.edu), *"Trading Frictions in Dynamic Cap-and-Trade Markets"* (`source-reported`, complete author list read from the v2 title block and the arXiv abs page Authors field).
- **Version / date pinned:** `arXiv:2606.03767v2`. Submission history read from the abs page: `[v1] Tue, 2 Jun 2026 15:21:49 UTC (320 KB)`, `[v2] Tue, 16 Jun 2026 07:10:27 UTC (320 KB)` — v2 is current and is the version this record quotes. The v2 HTML header prints `arXiv:2606.03767v2 [econ.TH] 16 Jun 2026`; the in-paper title block is dated **May 2026** (draft date, not a version conflict). Cross-check: every quoted number below was located verbatim in the pinned v2 full-text HTML.
- **Subjects:** primary `econ.TH` (Theoretical Economics), secondary `q-fin.GN` (General Finance) (`source-reported`, abs page).
- **Publication status:** arXiv **preprint only** — `Comments:` empty, `Journal reference:` empty, no publisher DOI on the abs page (`source-reported`). The DataCite DOI `10.48550/arXiv.2606.03767` resolves HTTP 200 to the abs page; it identifies the arXiv record, not a journal. License **CC BY 4.0** (`source-reported`, abs page and HTML footer).
- **Predecessor identity:** the v2 title block states the empirical analysis "subsumes that of *'Inefficiencies of Carbon Trading Markets'* first posted on arXiv on August 12, 2024" (`source-reported`). That predecessor's arXiv identifier was not looked up in this run → `data gap`; repo-wide search for the predecessor title returned 0 hits.
- **Stable URLs:** abstract https://arxiv.org/abs/2606.03767 · pinned full text https://arxiv.org/html/2606.03767v2 · DOI https://doi.org/10.48550/arXiv.2606.03767.
- **Sample period:** transaction and compliance universe from the EUTL, **February 2005 – September 2021** (Phases I–III plus first 9 months of Phase IV) (`source-reported`, §5.1 and §A.2); ~**2.7 million** registry transactions (`source-reported`, abstract). Quantitative headline sample: compliance cycles 2005–2021 (May of year t−1 → April of year t), **109,247 operator-year observations, 10,696 operators** (`source-reported`, §4.2). The month-by-month return panel (Figure 6 Panel B) is annotated **"since 2008"** (`source-reported`, figure note); the exact return-sample window used in Tables 4–5 is **not stated** → `data gap`.
- **Universe:** EU ETS secondary market for European Union Allowances (EUAs); >13,000 installations; three EUTL account types — operator holding accounts (regulated firms), person holding accounts (non-regulated participants / financial intermediaries), administrative accounts (regulators) (`source-reported`, §5.1, §A.1).
- **Primary-source checksum method (2026-09-24):** opened the arXiv landing page (submission history, authors, subjects, comments/jref/DOI fields, license) and read the complete pinned v2 HTML full text (192,017 characters of extracted text; Sections 1–6 plus Online Appendix A.1–A.7) directly, then located every quantitative claim below in its printed Table/Figure/Section.
- **Deduplication audit (this run):** repository-wide search (hidden-inclusive, excluding `.git`) across **2,503 `*.md` files** plus `coverage_manifest.csv` (5,808 lines) for `2606.03767`, `10.48550/arXiv.2606.03767`, the exact title *"Trading Frictions in Dynamic Cap-and-Trade"*, `Inefficiencies of Carbon Trading`, `Operator Flow Imbalance`, `surrender-month`, `April premium`, `EU ETS`, `emission allowance`, `euets.info`, `ec.europa.eu/clima`, `EUA return` → **0 matching records**. Author-name hits (`Nicola Borri`, `Yukun Liu`, `Aleh Tsyvinski`, `Xi Wu`) exist only inside crypto-factor records citing *different* papers (Liu–Tsyvinski–Wu 2022 *JoF* crypto factors; Liu–Tsyvinski 2021 *RFS*; Borri–Shakhnov 2022 *RAPS*; Borri 2019 *JEF*) — different source identities and different mechanisms (crypto cross-sectional factor pricing vs. EU ETS time-series order-flow/compliance-seasonality predictability), so no dedup conflict. Wiki Brain `kb_search "EU ETS cap-and-trade surrender premium operator flow"` returned **0 results** (stated plainly; no link fabricated).
- **As-of date:** source/version as-of **2026-06-16** (v2 submission); data as-of Feb 2005 – Sep 2021.

## Economic mechanism

### Source-reported

The source develops a dynamic stochastic model of a cap-and-trade market with **three interacting trading frictions** — slow (endogenous) participation, limited intermediation, and heterogeneous information — and tests it on EU ETS registry data (`source-reported`, abstract and §1):

1. **Costly market access → persistent non-trading and delayed purchases.** Firms choose a Poisson market-access intensity λ at a convex attention/treasury cost (Lambert-W closed form, Proposition 1). About 40% of operators do not trade in a given year (nearly 60% in Phase I, over 35% in Phases II–III, ~20% in the first nine months of Phase IV) (`source-reported`, §5.2).
2. **Residual compliance demand at the April surrender deadline + limited intermediary capacity → surrender-month price pressure.** Because firms delay, unresolved terminal demand hits a single surrender month; intermediaries absorb it at a quadratic immediacy-provision cost (affine impact `P = P* + ϕM`), producing an equilibrium surrender-month return premium `π_A = φ·D_A(π_A)` with a unique positive solution (Proposition 1) (`source-reported`, §2.1, §3.3–3.4).
3. **A subset of high-access operators trades on private scarcity signals → informative order flow → return predictability.** The model maps this to a monthly **Operator Flow Imbalance** (net flow from person holding accounts into operator holding accounts, scaled by total bilateral volume between the two account types) that predicts future cumulative EUA returns (`source-reported`, §3.5, §5.4).

The source's headline calibrated comparative static: halving intermediary return impact lowers the equilibrium premium by ~38% (not the 50% a static model predicts) because endogenous access raises residual terminal demand by ~23.7%; halving access costs alone lowers it ~20%; halving both lowers it exactly 50% (Corollary 4 scale invariance); doubling access costs raises the premium-to-impact elasticity from 0.69 to 0.72 (`source-reported`, §1, §4.4, Table 2).

### Research interpretation

- **Falsifiable mechanism A (compliance-calendar seasonality):** a regulator-mandated, perfectly predictable annual forcing date (31 March verification → 30 April surrender, €100/t penalty for non-surrender) concentrates reluctant compliance buying into one month; if intermediation capacity is finite and access is slow, that month carries a positive expected return premium — a *structural demand-pressure / friction-capture* hypothesis, not an informational one.
- **Falsifiable mechanism B (informed regulated flow):** a identifiable cohort of high-frequency compliance operators observes scarcity-relevant information (allocation shortfalls, banking plans, policy signals) and their net account-type flow is not instantly impounded, so monthly Operator Flow Imbalance positively forecasts 1–12 month cumulative EUA returns — an *order-flow / informed-trading* hypothesis.
- **Component roles (hybrid):** Regime/calendar: April surrender deadline (mechanism A). Primary signal: monthly Operator Flow Imbalance (mechanism B), with a source-reported frequent-trader variant restricted to operators above the full-sample median trade count. No exit, stop, sizing, or holding rule is specified by the source; any such layer is `research-proposed`.
- The source itself offers competing explanations for mechanism B that are *not* private information: "slower-moving inventory rebalancing or persistent client-order imbalances could also contribute to the predictability pattern" (`source-reported`, §5.4). This record treats the mechanism as contested between informed flow and persistent flow pressure until the falsification tests below decide.

## Signal

**Signal B — Operator Flow Imbalance (source-reported; the only near-operational object in the paper):**

- **Formation timestamp:** computed over calendar month *t* from EUTL registry transfers between person holding accounts and operator holding accounts; regression target is cumulative EUA log return `r(t→t+h)`, h ∈ {1, 2, 3, 4, 6, 8, 12} months (`source-reported`, Table 4). The **publication/availability lag of EUTL data is never stated in the source** → `data gap`; point-in-time tradability of month-*t* flow at month *t* is therefore unverified (look-ahead risk not addressed by the source).
- **Definition:** `OFI_t = (net flow person→operator in month t) / (total bilateral transaction volume between the two account types in month t)` (`source-reported`, §5.4, Table 4 note).
- **Variants:** baseline (all operators) and month-fixed-effects specification (source-reported, Table 4); frequent-trader split `OFI_high` / `OFI_low` computed above/below the **full-sample median number of transactions** — the source explicitly calls this "a descriptive cross-sectional classification rather than as a real-time trading rule" (`source-reported`, §5.5), i.e. it embeds look-ahead by the source's own admission.
- **Direction implied by the source:** positive coefficients at all printed horizons ⇒ long-biased interpretation (higher OFI → higher subsequent cumulative return). The source specifies **no** long/short rule, no entry price, no exit, no holding period beyond the regression horizon, no position sizing, no tie handling, no threshold → the trading rule is entirely absent from the source; any operationalization below is `research-proposed`.
- **`research-proposed` operationalization (for falsification only, not source-reported):** form OFI at month-end *t* using only data publicly available by that date (respecting the EUTL publication lag); go long EUA exposure (listed futures/spot) when OFI > 0 for h months, flat otherwise; scale positions to a 20% ADV participation cap. All thresholds and the sign rule are `research-proposed`.

**Signal A — April surrender-month seasonality (source-reported as a fact, not as a rule):** average monthly EUA log return in April is **about 10%** (raw April sample mean **0.104**, §4.4) and is the highest of all calendar months; April net operator purchases are roughly **ten times** typical non-April months, with December usually second (possibly tax reasons or expiry of the most common EUA futures contract) (`source-reported`, §5.3, Figure 6). A "long into April" timing rule is **not proposed by the source** — it would be `research-proposed`, and the source explicitly warns the premium "does not imply unbounded arbitrage" (finite residual demand, end-of-March verification uncertainty, endogenous banking) (`source-reported`, §5.3).

- **Parameters:** all regression coefficients/horizons as printed in Tables 4–5; frequent-trader split at full-sample median trade count (source-reported). No thresholds, filters, stops, or sizing rules exist in the source → `underspecified`.
- **Signal status:** reconstructable in *definition*; **not reconstructable in timing** (publication lag unknown) and **not specified as a trading rule** at all.

## Required data

- **Instrument / universe:** EU ETS emission allowances (EUAs); regulated operators of EU ETS installations; EU ETS Phases I–partial IV (`source-reported`).
- **Venue / market type:** registry transfers recorded in the **EUTL** (over-the-counter/registry layer), public via `https://ec.europa.eu/clima/ets/`, downloaded with tools at `https://www.euets.info` (`source-reported`, §A.2 footnote 9). The source does **not** map registry flow to any executable venue (ICE futures / spot) → `data gap`.
- **Fields:** per-transaction account identities/types, transfer direction, quantity, timestamps; per-installation allocated and surrendered amounts; company-level aggregation across accounts (`source-reported`, §A.2–A.3). EUA **price** series: the only named vendor is the **daily EUA spot price from Datastream**, used to convert EUA quantities to euros (§A.3 footnote 10); the price series used to compute the monthly returns in Figure 6B/Tables 4–5 is **not re-stated** → `data gap`.
- **Timeframe:** monthly signal and monthly cumulative-return targets; annual May→April compliance cycles for the quantitative section (`source-reported`).
- **Timestamp / timezone:** EUTL record timestamps and their timezone are not described → `data gap`.
- **Point-in-time / availability:** EUTL publication lag and revision policy are not discussed anywhere in v2 → `data gap` (critical for tradability of OFI).
- **Missing data:** no missing-data or exclusion rule for transactions/accounts is stated → `data gap`. Compliance rate is stated as close to 100%, so non-compliance is "unlikely to be an issue" (`source-reported`, §A.2).
- **Funding / fee / spread needs:** not observed, not modeled, not stated → `data gap` (see Execution assumptions).

## Execution assumptions

- **Source-modeled costs:** **none.** Direct full-text keyword scan of the pinned v2: `slippage` 0 hits, `bid-ask`/`bid/ask` 0, `latency` 0, `fill` 0, word-boundary `spread` 0, word-boundary `fees?` 0, `financing` 0, `leverage` 0, `market impact` 0, `participation cap` 0, `commission` 1 hit and it is the institution name "European Commission" (not a trading commission), `transaction cost` 1 hit (bibliography title of Jaraitė et al. 2010), `borrow` 6 hits all on the model's no-borrowing banking constraint, `margin` hits all "marginal"/"on the margin" in model prose, `capacity` hits all "intermediary capacity" (a model primitive, not strategy capacity). There is **no fee, spread, slippage, impact, borrow cost, financing, leverage, or fill model anywhere in v2** → recorded as `data gap`, **not** as zero cost (`source-reported` absence, verified by this Scout's own count).
- **Execution data gap:** "Our transaction data come from registry transfers rather than exchange-level execution records… we observe the direction and quantity of allowance movements… but not a structural decomposition of motives or execution prices for each trade" (`source-reported`, §5.1).
- **Order type / fill model / latency / signal-to-order delay:** not stated by the source → `data gap`. Signal-to-order timing for any strategy is `research-proposed`.
- **Borrow / shorting / leverage / margin:** not stated → `data gap`.
- **Capacity:** the only scale anchor is the source's own "€8 billion ≈ 3.5% of total traded volume under a conservative three-month holding period" ex post arithmetic (`source-reported`, §5.4); no participation-cap or market-impact capacity analysis exists → `data gap`.
- **Compliance penalty** (€100 per ton not surrendered on time, §A.1) is a regulatory penalty for *firms*, not a trading cost of the signal.

## Evidence

### Source-reported

Every figure below is `source-reported`, traced to the pinned v2 (all are gross of any cost because no cost model exists), **not independently reproduced**:

1. **Table 4 — Time-Series Return Predictability (baseline, cumulative-return units, Newey-West t):** Op. Flow Imb. `0.039* (1.958)` at 1m, `0.097*** (2.626)` 2m, `0.137** (2.471)` 3m, `0.213*** (2.806)` 4m, `0.322** (2.513)` 6m, `0.414*** (2.681)` 8m, `0.565*** (2.770)` 12m; R² `0.013 / 0.040 / 0.050 / 0.087 / 0.115 / 0.132 / 0.145`. Month fixed effects: `0.070** (2.350)`, `0.132** (2.505)`, `0.187** (2.527)`, `0.252** (2.599)`, `0.369** (2.417)`, `0.472** (2.585)`, `0.776*** (2.901)`; R² `0.098 → 0.202`. Significance codes: \*/\*\*/\*\*\* = 10/5/1%.
2. **Table 5 — Frequent vs infrequent traders (baseline):** `OFI_high` `0.050 (1.405)`, `0.082* (1.760)`, `0.105* (1.846)`, `0.188*** (2.714)`, `0.253** (2.208)`, `0.326** (2.274)`, `0.556** (2.571)` at 1→12m; `OFI_low` **never significant**: `-0.025 (-0.627)`, `-0.003 (-0.071)`, `0.014 (0.247)`, `0.002 (0.022)`, `0.065 (0.660)`, `0.079 (0.580)`, `-0.045 (-0.283)`. With month FE: `OFI_high` `0.078** (2.105)` … `0.718*** (2.878)`; `OFI_low` still never significant.
3. **Table 3 — No-trade persistence (Panel A full sample, baseline):** `0.404*** (127.120)`, `0.323*** (92.780)`, `0.255*** (66.460)`, `0.215*** (51.820)`, `0.196*** (43.590)` for t+1…t+5 (R² `0.169→0.042`); year-FE row `0.394*** (11.040)` … `0.202*** (16.720)`. Panel B (2013–2021): baseline `0.439*** (96.720)` … `0.217*** (31.180)`; year-FE `0.431*** (9.940)` … `0.233*** (50.600)`.
4. **§5.3 / Figure 6:** April average monthly log return **≈10%** (raw April sample mean **0.104**, §4.4), highest of all months; April net purchases ≈ **10×** typical non-April months; **€5 billion** implied April premium paid by delayed buyers = **2% of total traded volume** of regulated firms (back-of-the-envelope, assumes ~10% predictable April appreciation).
5. **§5.4:** Operator Flow Imbalance implies roughly **€8 billion** cumulative ex post trading performance over the sample, **≈3.5% of total traded volume under a conservative three-month holding period** — the source calls this "an illustrative magnitude… not a direct structural estimate of abnormal returns or informed trading".
6. **Table 1 — Calibration/validation:** pre-surrender no-trade share data **0.560** vs model **0.546**; one-year no-trade persistence **0.658** vs **0.637**; median pre-surrender trade count data **0.000** vs model **1.474**; share of annual volume in April purchases data **0.231** vs model **0.131**; `corr(D_A^model, D_A^data) = 0.949`, slope **1.642**, R² **0.901**; access intensity λ̂ median **0.568** (p10 **0.170**, p90 **1.482**), mean no-access probability **0.548**.
7. **Table 2 — Counterfactuals (equilibrium premium; April premium paid, €mn):** Baseline `0.072 / 175.6`; half φ `0.044 / 135.5` (D_A +23.7%, premium paid −22.9%); half access cost `0.057 / 110.8` (premium −20.3%, paid −36.9%); joint `0.036 / 87.8` (−50.0% / −50.0%); stagger K=2 `0.045 / 135.5`; stagger K=4 `0.029 / 101.5` (premium −59.4% per §1/§4.4, paid −42.2%). Text: doubling access cost → premium `0.089`, then halving φ → `0.054`, elasticity ≈`0.72` vs baseline `0.69`.
8. **§4.3 — Return-impact calibration:** positive-premium-years median φ̂ = `7.83×10⁻¹⁰` (11 years); all-17-year OLS through origin φ̂ = `4.10×10⁻¹⁰`; leave-one-out range `[3.71×10⁻¹⁰, 4.67×10⁻¹⁰]`; all-year OLS R² "small".
9. **§5.2 — Participation:** ~40% annual non-traders overall (nearly 60% Phase I, >35% Phases II–III, ~20% first nine months of Phase IV); among traders mean annual volume ≈**95,000** EUAs, median ≈**3,700**, bottom 10% <**100**, top 10% >**86,000**; **35%** trade less than they surrender, **>10%** trade more than **4×** their surrender obligation (the source's "conservative" frequent-informed-operator definition, §1).
10. **§A.4 — Inference robustness:** Valkanov `t/√T` bootstrap critical values keep coefficients significant at 5% **from the two-month horizon onward**; Stambaugh-type bias "less than 1% of the coefficient estimate".
11. **Abstract / §1:** ~**2.7 million** EUTL transactions, 2005–2021; model-implied terminal demand correlates **0.95** with observed April compliance purchases at the year level.

### Independently reproduced

not independently reproduced

(This run = landing-page checksum + direct full-text read of pinned v2 HTML + locating every quoted number in its printed table/section + full-text cost/keyword counts + repository-wide and Wiki Brain source-identity dedup. No EU ETS data was fetched, no regression was re-run, no backtest was performed.)

### Negative evidence

1. **No cost or execution model at all** — slippage/bid-ask/latency/fill/fees all 0 hits in pinned v2 (Scout's own count); every return number is effectively pre-cost, and the data layer (registry transfers) cannot see execution prices (§5.1).
2. **Not a strategy in the source** — Tables 4–5 are predictive regressions on a single aggregate asset; there is no entry/exit/sizing/holding rule, no portfolio construction, no Sharpe, no drawdown, no turnover figure anywhere in v2 (0 hits).
3. **1-month horizon is only 10%-significant** (`0.039*`, t=1.958) with baseline R² = 0.013; predictability only clears 5% from the 2-month horizon (also the §A.4 Valkanov result).
4. **Frequent-trader split is look-ahead by the source's own admission** — split by *full-sample* median trade count, "descriptive… rather than as a real-time trading rule" (§5.5).
5. **Source-listed competing mechanisms** for Table 4: "slower-moving inventory rebalancing or persistent client-order imbalances could also contribute" (§5.4) — informed-flow interpretation not identified.
6. **April premium explicitly bounded**: finite aggregate residual demand D_A, end-of-March verification uncertainty, endogenous banking ⇒ "does not imply unbounded arbitrage" (§5.3).
7. **Calibration misfits the source itself prints**: April volume share 0.231 (data) vs 0.131 (model); median pre-surrender trade count 0.000 vs 1.474; terminal-demand slope 1.642 (levels understated); fixed-point premium 0.072 vs raw April mean 0.104 (§4.2–4.4, Table 1).
8. **Return-sample window and monthly T for Tables 4–5 are not stated** (Figure 6B only says "since 2008") → `data gap`; φ̂ headline calibration uses only the 11 positive-premium years (selection on sign, §4.3).
9. **Point-in-time tradability unverified** — EUTL publication/availability lag never discussed → `data gap` with look-ahead risk for any real-time OFI signal.
10. **Return-price vendor not re-stated** (only Datastream daily spot is named, for euro valuation) → `data gap`.
11. **Sample ends September 2021**; no post-2021 evidence; single market, single asset, time-series-only design; no cross-market or out-of-sample test anywhere in v2 (0 hits for "out-of-sample", "placebo", "look-ahead").
12. **No code / replication package / data-availability statement** (0 hits for availability/replication/github/osf/dataverse outside arXiv UI chrome); **preprint only, no peer review**; single empirical sample.
13. **Multiplicity (our count):** 7 horizons × 2 specs × 2 split-samples printed with no FDR, deflated-Sharpe, or any selection adjustment.
14. **€8bn / €5bn figures are back-of-the-envelope aggregates**, self-labelled "illustrative… not a direct structural estimate"; and the two "April premium paid by delayed buyers" labels (€5bn vs €176mn/cycle) are unreconciled in v2 (frontmatter `contradictions`).

## Falsification plan

All thresholds below are `research-defined` (Scout-chosen) and all operationalizations are `research-proposed`; none are source-reported.

- **F1 — Point-in-time replication:** rebuild monthly OFI from EUTL using only records publicly available at month-end *t* (respecting publication lag), re-run Table 4. **Pass bar:** 2m–12m coefficients all positive with Newey-West t ≥ 2.0; **fail** if any of 2m/3m/6m/12m is ≤ 0 or t < 2.0 → reject real-time signal claim.
- **F2 — Cost ladder:** charge 0 / 1 / 2 / 5 / 10 bp per side plus listed-venue fees on EUA futures/spot, 20% ADV participation cap, 3-month holding (source's own "conservative" holding). **Fail** if the 12m signal is net-≤-0 at 5 bp or net Sharpe < 0.5 (`research-defined`).
- **F3 — Frozen forward test:** evaluate strictly on post-September-2021 data (2021-10 onward, never used in the paper). **Fail** if the 12m coefficient retains < 50% of the source's 0.565 or NW t < 2.0 (`research-defined`).
- **F4 — No-look-ahead frequent-trader split:** re-form the frequent/infrequent split with rolling *past-only* trade counts. **Fail** if `OFI_high` loses 5% significance at 2m+ **or** `OFI_low` becomes significant (the "informed frequent operator" interpretation dies with it) (`research-defined`).
- **F5 — Placebo:** 1,000 circular-shift/permutation draws of OFI against the return series. **Fail** unless |z| ≥ 2.0 vs the shuffled distribution (`research-defined`).
- **F6 — Competing-mechanism horse race:** include lagged EUA returns, realized volatility, month and phase fixed effects, admin-excluded pure compliance net demand, and energy-benchmark (crude/gas coal) returns as controls. **Fail** if the OFI coefficient shrinks below 50% of baseline or falls below t = 2.0 at 3m — i.e. inventory/client-flow or macro carry, not informed flow, explains it (`research-defined`).
- **F7 — Multiplicity:** apply Benjamini–Hochberg over the full printed grid (7 horizons × 2 specs × 2 splits). **Fail** if no cell survives q < 0.10 (`research-defined`).
- **F8 — Capacity:** scale to the source's own €8bn / 3.5%-of-volume anchor under a 20% ADV cap and F2 costs. **Fail** if implementable net PnL at the cap is < 50% of the gross anchor (`research-defined`).
- **F9 — April seasonality decay:** on post-2021 data, April mean return must exceed the non-April monthly mean in ≥ 4 of 5 years (2022–2026). **Fail** otherwise → treat mechanism A as regime-dead (`research-defined`).
- **Action on failure:** record the failure as negative evidence in this record's family, do **not** implement, do **not** promote to any candidate pool; research-only status is unchanged by passing alone.

## Crypto portability

**unproven.**

The mechanism originates in a regulator-mandated compliance calendar with a penalized surrender deadline and a registry that separates regulated compliance accounts from intermediary accounts. Crypto has no compliance-surrender obligation, no penalty-backed forcing date, no equivalent operator-vs-intermediary account registry, and no comparable identified "regulated operator" cohort. Possible *adapted* analogues (futures expiry, token-unlock cliffs, staking-withdrawal epochs, quarterly options expiry) are hypotheses only — not demonstrated by this source, which never studies crypto. Crypto-specific risks for any port: 24/7 sessions erase the month-end forcing clock; venue fragmentation splits any flow aggregate; on-chain/venue flow is observable in near-real-time (unlike the lagged EUTL), changing the signal's information set; funding, borrow for the short side, and perp liquidation dynamics are unmodeled here; candle/day boundaries and timezone conventions differ entirely. Portability label remains `unproven`, and this is not authorization to trade anything.

## Limitations

- `not independently reproduced`; `data gap` on: EUTL publication lag, return-sample window and monthly T for Tables 4–5, return-price vendor, timestamp/timezone conventions, missing-data rules, executable-venue mapping, and every cost/execution field.
- `underspecified` as a strategy: no entry/exit/sizing/holding/threshold rules exist in the source; the frequent-trader split is explicitly non-point-in-time.
- Identification is contestable: informed flow vs. persistent inventory/client flow is not separated by the source (its own caveat), and the hybrid mechanism A/B are tested as separate facts rather than ablated against each other.
- Sample scope: one market (EU ETS), one asset, 2005–2021, preprint only, no code, no peer review, no out-of-sample or placebo test in the source.
- The two internally inconsistent "April premium paid by delayed buyers" figures (€5bn vs €176mn/cycle) are recorded in frontmatter `contradictions`.
- Absence of negative results elsewhere is not evidence of robustness: `none identified in the reviewed sources beyond those listed; absence is not evidence of no negative result`.

## Implementation status

`implementation_status: not-implemented`. Nothing has been implemented in our research stack: no EUTL ingestion, no OFI signal construction, no backtest, no Qlib run, no prototype. This record is a normalized research capture only. No Paper, Testnet, or Live stage is connected or implied.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; or approved for implementation, paper trading, testnet, or live trading. Any later adoption requires explicit, separate review based on this record plus current sources.

## Related Wiki records

Wiki Brain search `EU ETS cap-and-trade surrender premium operator flow` returned **0 results** (2026-09-24); no related Wiki page is known, so **no Wiki link is fabricated**. Repo-adjacent records were checked and are mechanism-distinct (different assets and channels, kept as neighbors not duplicates): `european-cross-border-day-ahead-power-spread-mean-reversion-2026-09-23.md` (day-ahead power mean reversion), `electricity-spread-thief-forecast-reconciliation-bess-arbitrage-2026-09-22.md` (electricity spread forecasting), `climate-attention-global-warming-search-treasury-excess-return-predictor-2026-09-23.md` (climate-attention treasury timing). None covers EU ETS compliance-seasonality or account-type operator flow.

## Sources

- Borri, Nicola; Liu, Yukun; Tsyvinski, Aleh; Wu, Xi. *"Trading Frictions in Dynamic Cap-and-Trade Markets."* arXiv:2606.03767v2 [econ.TH; q-fin.GN], submitted 16 Jun 2026 (v1: 2 Jun 2026), CC BY 4.0, preprint only. https://arxiv.org/abs/2606.03767 — pinned full text: https://arxiv.org/html/2606.03767v2 — DOI: https://doi.org/10.48550/arXiv.2606.03767 (arXiv/DataCite DOI; no publisher DOI exists).
- Data source named by the paper (attribution only): European Union Transaction Log (EUTL), https://ec.europa.eu/clima/ets/ , retrieved via https://www.euets.info (Abrell 2023); EUA daily spot price from Datastream (§A.3 footnote 10).
- Predecessor title named by the paper: *"Inefficiencies of Carbon Trading Markets"* (first posted on arXiv 12 Aug 2024); its identifier was not verified in this run → `data gap`.
