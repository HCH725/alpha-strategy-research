---
schema: strategy-research-record-v1
title: "MLV Real-Value Numeraire Risk Space for Dividend-Maximizing Stablecoin Collateral Portfolios"
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: low
source_as_of: 2026-08-31
sources:
  - https://arxiv.org/abs/2608.30225
  - https://arxiv.org/pdf/2608.30225v1
  - https://arxiv.org/html/2608.30225v1
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MLV Real-Value Numeraire Risk Space for Dividend-Maximizing Stablecoin Collateral Portfolios

## Provenance

- **Primary source (single, preprint only):** Tomonori Kanno, Kensuke Ito, Yushi Yoshimura, Kyohei Shibano, *Redefining Stablecoins from Nominal to Real Value: A Maximum Likelihood Approach*, **arXiv:2608.30225v1 [cs.CE]**, `[Submitted on 31 Aug 2026]` (landing-page dateline), PDF footer `arXiv:2608.30225v1 [cs.CE] 31 Aug 2026`. Authors and order read from the landing page and the HTML title block: Tomonori Kanno (VLUE Inc., Tokyo, Japan), Kensuke Ito (The University of Tokyo, Endowed Chair for Blockchain Innovation, Tokyo, Japan), Yushi Yoshimura (VLUE Inc., Tokyo, Japan), Kyohei Shibano (The University of Tokyo, Endowed Chair for Blockchain Innovation, Tokyo, Japan). Correspondence contact in the paper: `kanno@vlue.jp`, `k-ito@g.ecc.u-tokyo.ac.jp`, `yoshimura@vlue.jp`, `shibano@tmi.t.u-tokyo.ac.jp`.
- **Stable URLs:** landing `https://arxiv.org/abs/2608.30225`; canonical PDF `https://arxiv.org/pdf/2608.30225v1` (HTTP 200 checked 2026-09-24, `content-disposition: filename="2608.30225v1.pdf"`, `last-modified: Tue, 01 Sep 2026 01:58:09 GMT`, response `etag: "sha256:c6af2dcc5202e9d330d511323132698af2f13453fff98f288c05472ccd78cb3c"`); full text read for this record from `https://arxiv.org/html/2608.30225v1` (HTTP 200, LaTeXML HTML) on 2026-09-24 — Sections 1–5, Appendices A–B, Table 1, Disclosure, Acknowledgment, References all read in full.
- **Version status:** v1 only. `https://arxiv.org/html/2608.30225v2` returned HTTP 404 at verification time (2026-09-24), so no later version exists to reconcile against. Landing-page `Comments`, `Journal reference` and `DOI` fields are all **empty** → **preprint only, no peer review, no DOI**. Primary categories: `cs.CE` (Computational Engineering, Finance, and Science) and `econ.EM` (Econometrics). License in the HTML header: **CC BY-NC-SA 4.0**.
- **Source/data as-of:** submission 2026-08-31; the paper's own experiment sample is stated in §4.2 Data as **June 2019 through January 2026**.
- **Declared interests (Disclosure section, verbatim substance):** "The concept of MLV and its application to portfolio optimization are the subject of patent applications filed by VLUE, Inc. in Japan and internationally." Acknowledgment: Endowed Chair for Blockchain Innovation and the Mohammed bin Salman Center for Future Science and Technology (Saudi-Japan Vision 2030, MbSC2030). Two of four authors are corporate (VLUE Inc.).
- **Code/data availability:** no repository, code, or dataset link appears anywhere in v1 (full-text search for `github`/`code is available`/`available at`/`reproduc` returned no availability statement) → **data gap; reproduction from the paper alone is not possible for several underspecified fields listed below**.
- **Deduplication:** repository-wide deterministic source-identity search on 2026-09-24 (`grep -rIl` across **all** non-binary files in the repository — 2,486 Markdown records plus `coverage_manifest.csv` and every other text file, including the `.mimo-worktrees`, `.agents` and `.hermes` trees) for `2608.30225`, `Redefining Stablecoins`, `Tomonori Kanno`, `Kensuke Ito`, `Kyohei Shibano`, `Maximum Likelihood Value`, `VLUE` → **0 hits**. Repo-wide searches for `unit of account` → 0 hits; `numeraire` → 5 unrelated repo files (quanto/DeFi/AMM/options mechanisms, different sources); `inflation-adjusted`/`real return` → 0 hits. The cited adjacent literature on stablecoin portfolio optimization (Grobys et al. 2025) is not a source identity in this repository either. Independent source identity and a materially distinct mechanism (numeraire/real-return risk-space transformation, not a directional signal) → new record is warranted.

## Economic mechanism

### Source-reported

The authors argue that conventional units of account (fiat currencies, gold, inflation indices) are themselves volatile (Figure 1: USD/JPY and USD/XAU normalized to 1.0 in 1980), so a stablecoin pegged to them inherits that volatility. They propose pegging instead to a new unit, the **Maximum Likelihood Value (MLV)**, defined in §3.1 (Definition 3.1) as the vector of real log-returns `Δv̂` that maximizes the joint density of `Δv` under **Assumption 1 (elliptical distribution)**, with the additional stated assumptions of no arbitrage and the law of one price (footnote 8). The closed form (§3.2, Eq. 5) is `Δv̂_i,t = −(Δp_i,tᵀ Σ_t⁻¹ 1) / (1ᵀ Σ_t⁻¹ 1)`, where `Δp_i,t` is the vector of observable price log-returns in units of `i` and `Σ_t` is a scatter matrix (the derivation adopts Tyler's M-estimator, footnote 10). **Theorem 3.3** states the MLV "is the unit of account that ensures the real return of the minimum-variance portfolio is zero", and §3.3 spells out the equivalence: "estimating unobservable real-value fluctuations via maximum likelihood is equivalent to defining them such that the real return of the minimum-variance portfolio is always zero."

§3.4 claims the MLV "enhances portfolio optimization" because `Σ_t` defined on real returns `Δv` "accurately captures the covariance structure of asset returns and thereby enables a faithful implementation of modern portfolio theory". The proposed rebalance problem (Eq. 11) is `max_w μ̂_i,tᵀ w − C‖w − w_{t−1}‖₁` s.t. `wᵀ1 = 1` and `wᵀ Σ_t w ≤ θ`; the experiment replaces the variance constraint with a downside-risk (CVaR) constraint computed in either the USD or the MLV risk space. §4.2/§5 claim this raises annualized return and Sharpe ratio while "substantially reducing turnover", which the introduction frames as the deposit incentive missing from USDT/USDC-style fiat-backed stablecoins.

### Research interpretation

Normalized, falsifiable hypothesis (our phrasing): **computing the binding risk constraint of a rebalancing portfolio from numeraire-adjusted (real-return) series, instead of from quote-currency series, changes which weight changes the constraint forbids, and thereby preserves or increases realized return per unit of rebalancing churn.** Component roles, separated per the repository contract:

- **Regime / constraint (the only stated treatment):** weekly `CVaR₀.₉₅ ≥ −0.04` computed from either USD-based or MLV-based portfolio returns over the past 100 weeks (§4.2 Methods; footnote 14 defines it as the average of the worst 5% of the past 100 weekly outcomes being no worse than −4%). All other parameters are held constant between the two arms (§4.2 Methods).
- **Return objective:** `μ̂_USD,t`, the equal-weight mean of historical per-asset *dividend* returns over an unstated lookback `L_t` (Appendix B, Eqs. 13–15). This is a dividend-capture objective, not a price-prediction alpha.
- **Universe screen:** at each rebalance the collateral portfolio is built by "selecting high-dividend stocks based on their trailing 12-month dividend yields" from the S&P 500 (§4.2 Data).
- **Turnover penalty inside the objective:** `C = 0.01` times `L¹` weight change (§4.2 Methods) — a soft regularizer chosen by the authors, **not** a transaction-cost model applied to performance.
- **Stability property:** by Theorem 3.3 the MLV's "stability" is *definitional* (the numeraire is constructed so the minimum-variance portfolio's real return is identically zero). It is a mathematical identity, not empirical evidence that the unit is stable in any market.
- **What would count as alpha here:** only the two-row comparison of Table 1 (MLV risk space vs USD risk space, same universe/objective/parameters). There is no directional signal, no forecast, and no factor; if the risk-space effect fails to survive cost and estimator ablations, the record collapses to "a dividend screen plus a covariance-estimator choice".

Open interpretive risks we do not resolve: (i) the risk space and the estimation procedure may change jointly (see Negative evidence 6), and (ii) the MLV used in §4.2 is itself estimated from the same S&P 500 cross-section the portfolio selects from, so the numeraire and the portfolio are not independent.

## Signal

Fully normalized reconstruction attempt; every item not fixed by the source is marked.

- **Formation timestamp:** at each rebalance date `t`, set at **five-week intervals** (§4.2 Data). The MLV sequence `Δv̂` and `Σ_t` are built from observable price log-returns over a rolling window of the past **3N periods** up to `t` (Appendix A, `|W_t| = 3N`, with `N` the number of observed assets; §4.2 states `n ≈ 500`). **The sampling frequency of those input returns (daily/weekly) is never stated** → `data gap`. Timezone, session and calendar conventions → `not stated in source`.
- **Lookback:** Σ window = 3N periods (≈1,500 periods when `n ≈ 500`); CVaR window = past **100 weeks**; dividend-yield screen = trailing **12 months**; dividend-return mean `μ̂` over a "fixed lookback window" `L_t` whose **length is never given** → `underspecified`. Warm-up behaviour of the estimator before the first admissible `3N` window → `underspecified`.
- **MLV/covariance iteration (Appendix A):** Step 1 set `Σ_t^(k=0) = I`; Step 2 compute `Δv̂` from Eq. 5 for every period in `W_t` and form `Δv̂_s = Δp_i,s + Δv̂_i,s·1`; Step 3 re-estimate `Σ_t` from `{Δv̂}` with **Tyler's M-estimator** fixed-point Eq. 12; Step 4 repeat to convergence. **Stopping tolerance and maximum iterations → `not stated in source`.**
- **Long entry / selection:** high-dividend S&P 500 names by trailing 12-month yield. **Number of holdings, yield threshold/rank cutoff, tie handling, and initial weight vector → `underspecified`.**
- **Optimization (Eq. 11 as executed in §4.2):** maximize `μ̂_USD,tᵀ w − 0.01·‖w − w_{t−1}‖₁` subject to `wᵀ1 = 1` and weekly `CVaR₀.₉₅ ≥ −0.04` computed from USD-based or MLV-based returns of the candidate portfolio over the past 100 weeks. **Solver, tolerance, and treatment of infeasible constraints → `not stated in source`.**
- **Sign convention / shorting:** the stated constraint set contains `wᵀ1 = 1` but **no non-negativity constraint is written**, and no shorting, borrow or margin rule appears anywhere in v1 → whether the portfolio is long-only is `underspecified`; this record does **not** assert long-only as source-reported (see Execution assumptions).
- **Exit:** there is no exit rule other than full re-optimization at the next five-week rebalance; no stop-loss, take-profit or time-stop is defined (`stop conditions: not defined in source`).
- **Holding period / overlap:** five-week rebalance cadence; overlapping or partially-traded positions → `not stated in source`.
- **Parameters and their source:** `C = 0.01` (author-fixed, §4.2), `CVaR level 0.95`, `CVaR floor −0.04`, `CVaR lookback 100 weeks`, `rebalance 5 weeks`, `Σ window 3N`, `n ≈ 500` MLV assets, `N = 500` synthetic assets in §4.1 — all **source-reported**; no tuning protocol, no validation split, no hyperparameter search is described → `underspecified`. Any choice of ours in this record is labelled `research-proposed`.
- **Rule completeness:** the normalized rule above is **partially reconstructable**: objective, constraints, cadence, estimator and windows are given; holding count, `L_t`, input frequency, solver, feasibility, sign constraint and execution timing are not. The signal must therefore be treated as **underspecified**, not reproducible as published.

## Required data

- **Instrument / universe:** U.S. common equities; §4.2 Data: "U.S. equities from the S&P 500 universe", with the collateral portfolio selected from high-dividend names and the MLV estimated from "a broader set of equities (`n ≈ 500`) from the same S&P 500". **Point-in-time index membership, listing/delisting handling, reconstitution dates, liquidity or price filters, and survivorship treatment → `not stated in source`** (an S&P 500 screen over 2019–2026 carries an unaddressed survivorship/membership-bias risk).
- **Venue / vendor:** `not stated in source` (no data vendor, feed, or exchange named anywhere in v1) → `data gap`.
- **Timeframe / bar frequency:** rebalance cadence 5 weeks; CVaR sampled weekly; **Σ/MLV input frequency not stated** → `data gap` (see Negative evidence 7).
- **Fields required:** per-asset total price series (log returns), **dividend per share and ex-date timing** (dividends are "treated as nominal cash flows and aggregated at the portfolio level", §4.2 Data), trailing 12-month dividend yield for the screen, index membership flags, and a cross-sectional panel wide enough to run the `3N`-period robust covariance fit. **Funding, borrow, options surface, order-book and open-interest fields are not used.**
- **Point-in-time / availability:** the MLV is explicitly designed to be computable online from past observable prices only (Appendix A: "without requiring MLV-denominated data ex ante"), which is a genuine look-ahead-free construction; however the **publication/availability convention of the dividend and membership data, and any lag applied to the trailing-yield screen → `not stated in source`**.
- **Timestamp / timezone:** `not stated in source`; the conclusion itself lists "price data acquisition and portfolio rebalancing under region-specific trading hours and time zones" as unresolved future work → acknowledged `data gap`.
- **Missing data:** null/stale/suspended/partial-print handling and imputation policy → `not stated in source`; imputation is forbidden in our normalization unless the source specifies it, so any reproduction must declare its own policy as `research-proposed`.
- **§4.1 inputs are synthetic, not market data:** multivariate `t`-distributed log-returns of length `T = 10N` from a random `N × N` correlation matrix with `N = 500`, with ground truth from the generating process. The "real-time computability" claim rests on this simulation, not on market data.

## Execution assumptions

- **Source-stated cost-related modelling (complete list, verified against the full text of §4, Appendices A–B):** exactly one — the `C = 0.01` `L¹` turnover penalty inside objective Eq. 11. It damps weight change; it is **not** a fee, spread or slippage model and is **not applied to the reported return series**.
- **Not stated anywhere in v1 (full-text search of `transaction cost`, `slippage`, `spread`, `commission`, `fee`, `borrow`, `short`, `latency`, `capacity`, `fill`, `bid-ask` found no methods-section treatment):** commissions, bid–ask spread, slippage, market impact, participation/capacity limits, borrow or short-sale availability and cost, leverage/margin, funding, signal-to-order delay, next-bar vs same-bar execution, order type (market/limit), fill model, partial fills and failure handling, latency. → All of the above are **`data gap`**; reported performance must be read as **not stated to be net of trading costs**, and we do **not** infer "cost = zero" — we record that no cost treatment is specified.
- **Fill and timing assumption needed to reproduce (ours, `research-proposed`):** rebalance orders filled at the five-week boundary on the next available price, no partial fills, no borrow needed if the sign constraint is non-negative.
- **Cost stress used only inside our falsification plan (`research-proposed`):** symmetric 5 bp one-way commission plus 5 bp slippage on traded notional, no funding term (equity long-only interpretation). This is Scout-generated and is **not** the source's assumption.
- **Capacity / turnover magnitude:** source-reported turnover is 0.529 (USD risk space) vs 0.133 (MLV risk space) per rebalance in the USD evaluation (Table 1a) — a 0.396 absolute gap (computed from the table) that makes any realistic per-trade cost a first-order, not second-order, term for the baseline arm. Capacity, ADV participation and trade size → `data gap`.
- **Distinction preserved:** the CVaR floor, `C`, screen and cadence are *risk/execution* choices, not alpha. The only candidate for "alpha" in this record is the risk-space (numeraire) treatment itself.

## Evidence

### Source-reported

All figures below are third-party claims from arXiv:2608.30225v1, traced to their exact location; none has been independently reproduced.

- **Table 1 (§4.2), caption "Performance of dividend-maximizing portfolios under CVaR constraints", sample June 2019 – January 2026, S&P 500 high-dividend collateral portfolio, 5-week rebalance, `C = 0.01`, weekly `CVaR₀.₉₅ ≥ −0.04`, returns include price changes plus dividends:**
  - **Panel (a) "Evaluated in the USD space"** — rows are the risk space used to compute the constraint: **USD risk space:** ann. return **0.117**, ann. volatility **0.211**, Sharpe **0.554**, max drawdown **−0.376**, turnover **0.529**. **MLV risk space:** ann. return **0.156**, ann. volatility **0.223**, Sharpe **0.699**, max drawdown **−0.466**, turnover **0.133**.
  - **Panel (b) "Evaluated in the MLV space"** — **USD risk space:** ann. return **0.037**, ann. volatility **0.132**, Sharpe **0.281**, max drawdown **−0.220**, turnover **0.527**. **MLV risk space:** ann. return **0.053**, ann. volatility **0.116**, Sharpe **0.461**, max drawdown **−0.148**, turnover **0.137**.
  - **§4.2 Results prose (independent restatement of panel (a)):** "using the MLV as the risk space increases the annualized return from 11.7% to 15.6% and the Sharpe ratio from 0.554 to 0.699, while substantially reducing portfolio turnover from 0.529 to 0.133."
  - **Derived arithmetic (ours, from the table):** panel (a) deltas +0.039 ann. return, +0.145 Sharpe, −0.396 turnover; panel (b) deltas +0.016 ann. return, +0.180 Sharpe, −0.390 turnover. The reported Sharpe column is reproduced by `ann. return / ann. volatility` to within 0.005 (0.117/0.211 = 0.555 vs 0.554 reported; 0.156/0.223 = 0.700 vs 0.699; 0.037/0.132 = 0.280 vs 0.281; 0.053/0.116 = 0.457 vs 0.461; maximum deviation 0.0041, consistent with the table's 3-decimal rounding), i.e. the ratio is consistent with an **implicit zero risk-free rate; no risk-free rate is stated anywhere in v1** → `data gap`.
- **§4.1 Results (synthetic study):** with `N = 500` and `T = 10N`, correlation-matrix RMSE against ground truth "rapidly decreases as the number of observed assets increases and stabilizes beyond approximately `n = 200`"; "observing on the order of `n ≈ 500` assets is sufficient"; dominant update cost `O(n³)` "allows MLV to be computed in real time on standard computing hardware" — **no hardware, latency benchmark or wall-clock measurement is given** → the real-time claim is analytical, `underspecified`.
- **§3.3 Theorem 3.3:** the MLV is the unit of account for which the minimum-variance portfolio's real return is zero (proved from Eq. 5 and `w* = Σ⁻¹1 / (1ᵀΣ⁻¹1)`), and §3.3 states this is *equivalent to defining* real-value fluctuations that way.
- **Abstract claim:** "MLV can be computed in real time from 500 asset price series and improves annualized returns and Sharpe ratios while substantially reducing turnover in portfolio optimization."
- **Publication status:** single preprint v1, 31 Aug 2026, `cs.CE` + `econ.EM`, empty Comments/Journal-ref/DOI, CC BY-NC-SA 4.0, patent applications declared in the Disclosure section.

### Independently reproduced

not independently reproduced

(Our work on 2026-09-24 was limited to primary-source integrity checks: landing-page metadata, v1-only confirmation (`v2` → HTTP 404), PDF `HTTP 200` with `etag sha256:c6af2dcc5202e9d330d511323132698af2f13453fff98f288c05472ccd78cb3c` and `last-modified 2026-09-01`, full-text reading of Sections 1–5 and Appendices A–B, internal arithmetic checks of Table 1 (Sharpe = return/volatility), and repository-wide source-identity deduplication. No portfolio was reconstructed, no data was obtained, and no backtest was run.)

### Negative evidence

1. **The headline "stability" result is true by construction, not by evidence.** Theorem 3.3 and §3.3 explicitly note that ML estimation here is *equivalent to defining* real-value movements so that the minimum-variance portfolio's real return is zero. The paper's own framing concedes the identity; treating it as empirical validation would be a category error.
2. **Turnover is not invariant across panels for what footnote 15 calls the same portfolio.** Footnote 15 states the two evaluation spaces reflect "whether the same portfolio optimization outcome is evaluated in USD or in MLV", yet Table 1 reports turnover **0.529 vs 0.527** and **0.133 vs 0.137** — differences of 0.002 and 0.004 (computed) in a quantity that is a ratio of traded value to portfolio value and should be unit-invariant apart from rounding. No definition of "turnover" is given anywhere → the reduction claim rests on an undefined statistic with an unreconciled cross-panel discrepancy.
3. **The improvement is not uniformly an improvement.** In the headline USD-evaluated panel the MLV risk space **raises volatility (0.211 → 0.223) and worsens maximum drawdown (−0.376 → −0.466, a 0.090 deterioration, computed)**. The abstract, §4.2 Results and §5 speak only of higher return/Sharpe and lower turnover; the drawdown regression is not acknowledged.
4. **No transaction-cost, spread, slippage, borrow, latency or capacity treatment exists in v1** (full-text verification across §4, Appendices A–B). With source-reported turnover of 0.529 per five-week rebalance in the baseline arm, the absence of a cost model is decision-relevant; returns are not stated to be net of trading costs. (Recorded as `data gap`, not as "cost = 0".)
5. **Zero statistical inference and no out-of-sample design.** There are no t-statistics, p-values, confidence intervals, block bootstraps, repeated splits, alternative universes or holdout periods anywhere in v1 (full-text search: 0 hits for `t-stat`, `p-value`, `significan*`, `bootstrap`, `confidence interval`). A single 6.6-year path on a single index supports point estimates only; no test distinguishes the +0.145 Sharpe gap from estimation noise.
6. **The treatment is confounded with the estimator.** §4.2 says only that CVaR is computed "with covariance structures derived from either USD-based or MLV-based returns, while all other parameters are held constant" — it never states which estimator produces the **USD-space** covariance (plain sample covariance? Tyler's M-estimator?), while the MLV-space path is explicitly Tyler-based and iteratively re-estimated (Appendix A). Because robust-versus-classical covariance estimation alone is known to move portfolio weights, the numeraire effect cannot be isolated from the reported two rows; no 2×2 (numeraire × estimator) ablation is reported.
7. **The stated estimation window cannot be reconciled with the stated sample.** Appendix A fixes `|W_t| = 3N` periods; §4.2 uses `n ≈ 500` → **1,500 periods**, while the sample June 2019 – January 2026 spans ≈1,681 trading days or ≈348 weeks (computed at 252 trading days/year), and **the input frequency is never declared**. Read weekly, the window (≈28.8 years) is infeasible; read daily, the window (~5.95 years) nearly exhausts the sample, leaving roughly 180 trading days of slack and no valid covariance estimate for early rebalance dates. Either reading leaves the reported full-period performance unreproducible as specified → `underspecified`/internally inconsistent.
8. **Scope mismatch between the motivating claim and the experiment.** The introduction says the MLV "infers unobservable real value from **global financial data**" and avoids locality; §4.2 estimates it from **one national equity index (S&P 500, USD-denominated names only)**, and from the same cross-section the portfolio selects from. The unit-of-account claim is therefore never tested against FX, commodities, bonds or non-US data — Figure 1 (USD/JPY, USD/XAU) is illustrative, not part of the experiment.
9. **Selection and evaluation details that a reproduction needs are missing:** number/threshold of "high-dividend" holdings, initial weights, `L_t` length, turnover definition, dividend timing and reinvestment, data vendor, point-in-time membership/survivorship, solver and feasibility handling, estimator for the USD-space covariance, MLV iteration tolerance → all `underspecified` or `data gap` as itemized in Signal/Required data.
10. **Commercial interest and single-preprint status.** Patent applications on MLV and its portfolio optimization are declared (Disclosure), two authors are corporate (VLUE Inc.), the work is unrefereed (no journal ref/DOI), and no code or data is released. Publication-bias and sponsor-direction risk cannot be ruled out.
11. **Most of the reported return level comes from the screen, not the treatment.** The objective maximizes *dividend* returns of a trailing-yield screen; the numeraire only changes the risk constraint. Without a third arm (e.g., screen with no CVaR constraint, or an index control) the absolute 11.7%/15.6% levels cannot be attributed to the MLV mechanism at all — the paper reports no benchmark portfolio, no index return and no equal-weight control for the period.
12. **Unit-dependence of the headline level.** The same portfolios return 11.7%/15.6% in USD space but only 3.7%/5.3% in MLV space (footnote 16 attributes the gap to USD depreciation over the sample). The size of the claimed improvement therefore swings with the evaluation unit (+0.039 vs +0.016 in return; +0.145 vs +0.180 in Sharpe, computed), and no unit is declared canonical.

None of the above is a failed replication by us; they are internal inconsistencies, unmodelled frictions and missing specifications read directly out of the pinned primary source.

## Falsification plan

All thresholds below are `research-defined falsification threshold` (Scout-chosen, not from the source); all cost, estimator and sampling choices are `research-proposed`.

- **F1 — Reproduction of Table 1.** Rebuild both arms (USD risk space, MLV risk space) on the stated S&P 500 high-dividend universe, June 2019 – January 2026, 5-week cadence, `C = 0.01`, weekly `CVaR₀.₉₅ ≥ −0.04`, `3N` window, Tyler M-estimator. **Fail if** either arm's annualized return differs from the table by more than **±0.02** or Sharpe by more than **±0.05** → record the source-reported numbers as not reproducible as specified (expected failure mode: F5 below).
- **F2 — Cost stress.** Apply `research-proposed` symmetric **5 bp one-way commission + 5 bp slippage** on traded notional (plus a variant at 10 bp + 10 bp) to both arms. **Fail the economic claim if** the MLV arm's net Sharpe advantage over the USD arm is **≤ 0**, or if the MLV arm's net Sharpe is **< 0.30**, under either cost setting. Given turnovers of 0.133 vs 0.529, also report which arm's gross result was cost-inflated.
- **F3 — Estimator/numeraire 2×2 ablation.** Cross {USD returns, MLV returns} × {sample covariance, Tyler M-estimator} with everything else fixed. **Fail the stated mechanism if** the MLV main effect is **≤ half** the estimator main effect, or if `MLV + sample covariance` does not beat `USD + Tyler` (both `research-defined`).
- **F4 — Placebo numeraire (removes the "maximum likelihood" content).** Replace MLV with the unit defined by the negative return of a rolling **plain sample-covariance** minimum-variance portfolio (same "zero real return on the MVP" property, no ML/Tyler iteration). **Fail the ML-specific claim if** the placebo matches the MLV arm within **±0.02** annualized return and **±0.03** Sharpe (`research-defined`).
- **F5 — Window-feasibility audit.** Declare the input frequency and run the `3N = 1,500`-period window honestly. **Fail** if no admissible covariance estimate exists before the sample midpoint, i.e. the reported 2019–2021 portion cannot exist as specified → then F1 is void and the record is marked unreproducible-as-specified (`research-defined`).
- **F6 — Subperiod/regime split.** 2019-06–2022-12 vs 2023-01–2026-01. **Fail generality if** the MLV Sharpe advantage is **≤ 0** in either subperiod, or if the entire advantage comes from the 2022–2023 inflation/FX-dislocation window (`research-defined`). Rationale: footnote 16 attributes panel-level differences to USD depreciation, which is regime-concentrated.
- **F7 — Estimator-free and constraint-free controls.** Run (i) the screen with **no** CVaR constraint, (ii) an equal-weight or index control of the same names. **Fail the attribution if** the MLV-vs-USD gap shrinks to **< 0.05 Sharpe** once the constraint and estimator are pinned, or if the screen alone explains the headline levels (`research-defined`).
- **F8 — Turnover reconciliation.** Require a stated turnover definition reproducing both panels' values within **±0.001** (or an explicit explanation of the 0.002/0.004 gaps). **Fail** the turnover-reduction evidence if undefined (`research-defined`).
- **F9 — Crypto port test.** See Crypto portability; run MLV vs quote-currency risk space on a top-50 crypto perpetual/spot universe with `research-proposed` taker costs 5 bp + 5 bp. **Fail portability if** net Sharpe advantage is **≤ 0** or MLV net Sharpe **< 0.30** (`research-defined`).
- **Action on failure:** mark the mechanism not reproducible / cost-erased / estimator-driven / regime-limited as applicable; keep `status: research-only`, `adoption: not-approved`; no implementation, no candidate-pool promotion, no Paper/Testnet/Live. Success in F1–F9 would still only justify an Intake Review, not adoption.

## Crypto portability

**unproven.**

- The mechanism originates in traditional-asset research and is demonstrated **only** on S&P 500 U.S. equities over June 2019 – January 2026; the source itself contains **no crypto experiment**, despite the stablecoin framing. Under the repository rule this cannot be `direct`.
- The framing is crypto-*adjacent* (an MLV-pegged stablecoin issued against a rebalanced collateral portfolio, with USDT/USDC as the contrast), but the collateral portfolio, the risk space, the dividend objective and the CVaR window are all equity constructs. A crypto port would need a `research-proposed` replacement for the **dividend-return objective `μ̂`** (no dividends on crypto assets; staking/yield would be a different signal), which alone changes the strategy.
- Porting risks: (i) **universe and survivorship** — choosing the MLV cross-section from top-N crypto names drags in listing/delisting, wash-trading and concentration effects that an index screen avoids; (ii) **self-referential numeraire** — estimating the unit from the same cross-section that is traded is more easily distorted in thin crypto names; (iii) **24/7 session and candle boundaries** vs the paper's 5-week cadence and unstated input frequency; (iv) **fees/spreads/impact** are structurally larger in crypto, so a turnover-linked effect (0.529 vs 0.133) is *more*, not less, cost-sensitive; (v) **funding and borrow** for any short leg, and perp vs spot mark/index differences, are untreated in the source; (vi) **venue fragmentation and timestamp alignment** for a robust covariance fit.
- Crypto portability is not authorization to trade.

## Limitations

- `underspecified`: input return frequency; `3N` window feasibility vs the stated sample; `L_t` length; number/threshold of high-dividend holdings; initial weights; turnover definition; solver and feasibility handling; sign/short constraint; USD-space covariance estimator; MLV iteration stopping rule; data vendor; point-in-time index membership; timezone/session; missing-data policy.
- `data gap`: no cost/spread/slippage/impact/borrow/latency/capacity/fill model in the performance evaluation (only an in-objective `C = 0.01` turnover penalty); no risk-free rate for the Sharpe ratio; no benchmark/index control; no hardware or latency measurement behind the "real-time" claim.
- `not independently reproduced`: every performance figure in Evidence/Source-reported; our checks were provenance, checksum, internal arithmetic and dedup only.
- `unproven`: generalization beyond one U.S. index, one dividend screen and one 6.6-year path; any crypto applicability; the claim that the ML/maximum-likelihood step adds value over an equivalent-by-construction placebo numeraire (F4).
- Source-quality and incentive limitations: unrefereed single preprint (v1, no DOI/journal ref), declared patent applications on the very method being evaluated, corporate author affiliation, no code/data release. These do not make the numbers wrong, but they raise the bar for any adoption decision.
- Publication-bias/selection: the record is of one positive result with no null alternatives reported; absence of contrary findings in this source is not evidence of absence elsewhere.
- Interpretation boundary: `confidence: low` refers to confidence in **this research reading** (mechanism, gaps, falsification design) — not confidence that the strategy is profitable, and not authorization to trade.

## Implementation status

`implementation_status: not-implemented`. Nothing from this record exists in our research stack: no MLV estimator, no covariance/numeraire pipeline, no portfolio optimizer, no production card, no Qlib full backtest, no survivor bundle, no leaderboard entry, no Wiki Brain ingestion (this record is a repository artifact only), and no Paper, Testnet or Live activity. Reproduction attempts F1–F9 are planned tests, not executed work.

## Adoption boundary

This artifact is research material in a public staging pool. Its presence here does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered `/results/_handoff/candidates.json`; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. `status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. No wording, evidence count, confidence value or schedule implies promotion; any later adoption decision must be explicit, separately reviewed, and based on this record plus current sources.

## Related Wiki records

Real pages confirmed present in Hermes Wiki Brain via read-only `kb_search` on 2026-09-24 (no Wiki write was performed):

- [[quant/hybrid-resnet-rmt-covariance-denoising-crypto-mvp-2026-09-02]] — covariance-quality treatment for minimum-variance portfolios, in crypto; closest methodological neighbour to the `Σ`/MVP core here.
- [[quant/neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02]] — correlation-matrix estimation quality as a portfolio input, same "better Σ → better weights" family without a numeraire change.
- [[quant/forecasted-tangency-minimum-euclidean-distance-portfolio-2026-09-04]] — allocation under estimated moments; useful contrast for the estimator-confound issue (F3).
- [[quant/entropic-value-at-risk-tempered-stable-levy-portfolio-optimization-2026-09-02]] — downside-risk-constrained allocation; same class of "risk constraint, not alpha" component as the CVaR floor here.
- [[quant/eurostoxx-pca-ou-stat-arb-trading-time-friction-falsification-2026-09-12]] — turnover drag and friction falsification; template for F2's cost-erasure test.
- [[quant/crypto-stat-arb-cointegration-fdr-tiering-drifting-hedge-turnover-2026-09-13]] — turnover accounting and cost falsification under multiple testing; template for F8/F9.

Adjacent repository records that are **not** Wiki links (listed for dedup context only, different source identities): `graph-neural-network-volatility-minimum-variance-portfolio-2026-09-03.md`, `crypto-cross-sectional-volatility-managed-momentum-2026-08-31.md`, `cross-sectional-realized-skewness-dispersion-market-timing-2026-09-24.md`, `functionally-generated-portfolio-diversity-entropy-smallcap-stochastic-cost-2026-09-22.md`. No existing record covers a unit-of-account / numeraire risk-space transformation (repo search for `unit of account`: 0 hits).

## Sources

- Kanno, T., Ito, K., Yoshimura, Y., Shibano, K. (2026). *Redefining Stablecoins from Nominal to Real Value: A Maximum Likelihood Approach*. **arXiv:2608.30225v1 [cs.CE]**, submitted 31 Aug 2026. Landing: https://arxiv.org/abs/2608.30225 — author list, submission date, categories, empty Comments/Journal-ref/DOI (read 2026-09-24).
- Same paper, canonical PDF v1: https://arxiv.org/pdf/2608.30225v1 — HTTP 200, `etag "sha256:c6af2dcc5202e9d330d511323132698af2f13453fff98f288c05472ccd78cb3c"`, `last-modified 2026-09-01`, `filename="2608.30225v1.pdf"` (verified 2026-09-24).
- Same paper, full text used for every quoted figure and rule: https://arxiv.org/html/2608.30225v1 — §1 Introduction, §2 Related Work, §3 Model (Definitions 3.1–3.2, Assumption 1, Eqs. 4–11, Theorem 3.3), §4 Experiments (§4.1 synthetic study, §4.2 Data/Methods/Results, **Table 1 panels (a) and (b)**, footnotes 14–16), §5 Conclusion, Appendix A (Σ estimation, Eqs. 12), Appendix B (μ̂ definition, Eqs. 13–15), Disclosure, Acknowledgment (read in full 2026-09-24).
- Canonical specification used to normalize this record: Hermes Wiki Brain `quant/strategy-research-record-spec-v1.md` (`schema: strategy-research-record-v1`, 10,289 bytes, sha256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`, read-only read on 2026-09-24; `kb_search "strategy-research-record-spec-v2"` → 0 results, so v1 remains canonical); repository workflow contract `README.md` in this repository (575 lines, read on 2026-09-24).
