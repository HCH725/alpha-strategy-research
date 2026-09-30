---
schema: strategy-research-record-v1
title: "Day-Ahead Battery-Profit Evaluation of Probabilistic Electricity Forecasts: QBTS Gaming by Overdispersion and Low Discriminatory Power of Battery Trading Strategies"
created: 2026-09-30
updated: 2026-09-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-04-21
sources:
  - https://arxiv.org/abs/2604.19580
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Section 4.4 defines VaR at level alpha as the '(1-alpha)-quantile of the return distribution' but the printed formula VaR_alpha = inf{x in R : P(r <= x) >= alpha} is the alpha-quantile, and the same subsection then states the exceedance ratio 'should be close to 1-alpha'; prose, formula and calibration target cannot all hold."
  - "Table 5's caption states 'Negative values imply that the losses exceed the VaR more frequently than the nominal level', while Section 6.2 states 'The climatology model has VaR exceedance rates below the nominal level' about a climatology row that is entirely negative (-0.25 to -0.03); the sign convention in the caption and the sign reading in the prose are opposites."
  - "Section 6.2 reports the LEAR-BS model has 'exceedance rates of 11% to 23% above the nominal level', but Table 5's LEAR-BS row is 0.05 0.05 0.05 0.05 0.04 0.04 0.18 0.18 0.18 0.18 0.18 0.17 0.22 0.23 0.22 0.22 0.22 0.22, contains no 0.11 cell, and under the above/below-nominal reading the same sentence applies to climatology corresponds to 4 to 23 percentage points, not 11 to 23."
  - "Section 3.1 says 'A somewhat counterintuitive property of QBTS is described in Result 1' and Section 4.3 says 'We discuss the results in light of Result 2', but no statement labelled Result 1 or Result 2 exists anywhere in the pinned text; only Definition 1, Propositions 1-3 and Remarks 1-3 are labelled."
  - "Section 4.2 prints the emission factors eta_Gas = 0.2, eta_Coal = 0.35 and eta_Oil = 0.3 while the Appendix A table prints CO2 Factor (eta) of 0.2 for gas, 0.3 for coal and 0.27 for oil; the coal and oil values cannot both be correct."
  - "Section 6.3 states 'the profits are exactly the same for the simplified BESS and the MILP approach', but Figure 13's Expected Value block prints DP-1 below MILP-1 by 0.4 to 0.5 (thousand EUR) in all seven model rows (824.5 vs 825.0, 1009.6 vs 1010.1, 1151.7 vs 1152.1, 1151.7 vs 1152.1, and 1188.3 vs 1188.8 three times)."
---

# Day-Ahead Battery-Profit Evaluation of Probabilistic Electricity Forecasts: QBTS Gaming by Overdispersion and Low Discriminatory Power of Battery Trading Strategies

## Provenance

**Primary source (pinned this run, 2026-09-30):** arXiv:2604.19580v1 `[q-fin.ST]`.

- Abstract page: `https://arxiv.org/abs/2604.19580` -- HTTP 200, **43,338 bytes**, SHA-256 `49fc7530e0ab613fde9ff837a114eba5e997a274ef799fac6abea868598e1f44`.
- PDF: `https://arxiv.org/pdf/2604.19580` -- HTTP 200, **3,907,780 bytes**, SHA-256 `0b45efef4c8d1b7de2ee258adb504bf53819b8480fd8183c196a67e2ad0fd4b1`, extracted with pypdf 6.16.2 into **36 pages, 139,305 characters of page text, written out as a 141,767-byte / 140,051-character / 3,515-line file with page separators and read end to end**: title page and Abstract, Sections 1 through 7, Equations (1) through (49), Tables 1 through 5 (every cell), Figure 1 through Figure 15 captions (main text), Acknowledgments, the generative-AI declaration, the CRediT statement, the complete main reference list, Appendix A, and the Supplementary Material on pages 31 to 36 (its own figures renumbered 1 to 6 inside the supplement, the six-step scenario-generation recipe, Algorithms 1 to 3, and the supplementary references). The PDF metadata `/Title` is byte-identical to the title above.
- arXiv API: `https://export.arxiv.org/api/query?id_list=2604.19580` -- **3,314 bytes**, SHA-256 `f5bae62416cd817a01177c929134d65cc7a94f82c4807f6132421ce41474ceca`.

**Title (exactly as printed on page 1 and in the abstract page):** *Probabilistic Forecasting for Day-ahead Electricity Prices, Battery Trading Strategies and the Economic Evaluation of Predictive Accuracy*.

**Authors (exactly as printed):** `Simon Hirsch` and `Florian Ziel`. Affiliations printed on page 1: `(1) Data Science in Energy and Environment, University of Duisburg-Essen, Germany`; `(2) Statkraft Trading GmbH, Germany`. Manuscript date line: `April 21, 2026`.

**Version / date:** abstract dateline `[Submitted on 21 Apr 2026]`; submission history `[v1] Tue, 21 Apr 2026 15:35:32 UTC (5,047 KB)`; arXiv API `<published>2026-04-21T15:35:32Z</published>` and `<updated>2026-04-21T15:35:32Z</updated>` (single version, no v2; feed-level `<updated>2026-09-30T05:21:46Z</updated>`); PDF first-page footer `arXiv:2604.19580v1 [q-fin.ST] 21 Apr 2026`. The `5,047 KB` submission-history figure is the arXiv source-package size and is not the size of the served 3,907,780-byte PDF; the two are different objects and are not reconciled in the source (**data gap**, not treated as a contradiction).

**Subjects:** `Statistical Finance (q-fin.ST); Econometrics (econ.EM); Portfolio Management (q-fin.PM); Applications (stat.AP)` -- q-fin.ST primary.

**Comments field:** `30 pages, 15 figures, 5 pages supplementary materials`.

**Publication / licence status:** `journal-ref` cell empty; `DOI` cell empty on the abstract page; the only DOI is the arXiv-issued DataCite value carried in the PDF metadata (`https://doi.org/10.48550/arXiv.2604.19580`); no publisher DOI and no peer-review statement anywhere in the pinned text -- **preprint only**. Licence cell: `view license` linking to `http://arxiv.org/licenses/nonexclusive-distrib/1.0/` (arXiv.org perpetual non-exclusive distribution licence; this plain-HTTP URL is preserved literally as printed and is the only non-HTTPS URL in this record); the PDF metadata `/License` carries the same URL.

**Code / data availability:** `repository` = 0, `code availab` = 0, `data availab` = 0, `reproduc` = 0 occurrences in the pinned 139,305-character text. No repository URL, no immutable commit, no run manifest -- all **data gap**. The named third-party input is the dataset of Lipiecki, Uniejewski & Weron (2024) built from ENTSO-E and investing.com, which was **not fetched this run**.

**Source-identity deduplication (whole repository, before writing, 2026-09-30):** `rg -uuu -F` across the entire checkout including `.git`, `.mimo-worktrees`, `.agents`, `.hermes` for `2604.19580`, `Simon Hirsch`, `Florian Ziel`, `Hirsch & Ziel`, `Hirsch and Ziel`, `quantile-based trading`, `QBTS`, `DLENAR`, `Probabilistic Forecasting for Day-ahead Electricity Prices`, `Economic Evaluation of Predictive Accuracy` and `Uniejewski`.

- `2604.19580` returns **4 files**: `.git/COMMIT_EDITMSG`, `.git/logs/refs/heads/main`, `.git/logs/HEAD` (git internals) and `bess-day-ahead-ms-ave-probabilistic-profit-ensemble-stopping-rule-2026-09-30.md`, where it appears only as line 329 of that record's in-paper-citation list (`Hirsch & Ziel (2026), arXiv:2604.19580`), i.e. as a work cited *inside* Weron & Maciejowska's reference apparatus and explicitly marked "not independently read" -- **not** that record's own source identity.
- `Hirsch & Ziel` returns **2 files**: the same BESS record, plus `orderfusion-plus-intraday-electricity-buy-sell-price-trajectory-orderbook-dynamic-mask-2026-09-22.md`, whose only hit is `Hirsch & Ziel 2024` (a different paper) at line 53.
- `Simon Hirsch`, `Florian Ziel`, `Hirsch and Ziel`, `quantile-based trading`, `QBTS`, `DLENAR`, both title fragments and `Uniejewski` return **0 files** (`Uniejewski` returns exactly 1 file, the BESS record, as another in-paper citation).
- `coverage_manifest.csv` (5,808 lines) returns **0** for `2604.19580`, `Simon Hirsch`, `Florian Ziel`, `QBTS`, `DLENAR`.
- Loose token `Hirsch` returns **12 files before this write and 13 after**: ten are `Herfindahl-Hirschman` (HHI) mentions (`crypto-cross-sectional-blockchain-network-distribution-factor-2026-09-01.md`, `crypto-perpetual-slippage-at-risk-sar-liquidity-early-warning-2026-09-02.md`, `polymarket-favorite-longshot-bias-crypto-politics-2026-09-14.md`, each with two `.mimo-worktrees` copies, plus the coordinator `_payload_20260928.json`), and two are **in-paper citations inside other electricity records** (`Hirsch & Ziel (2026), arXiv:2604.19580` in the BESS record's literature list, `Hirsch & Ziel 2024` at line 53 of the OrderFusion-plus record). The 13th file is this record itself, so **no pre-existing record carries `2604.19580` as its own source identity**.
- Positive control `novy-marx` returns **54 files before this write and 55 after**, the sole increment being this record's own dedup sentence. Post-write re-scan: `Simon Hirsch`, `Florian Ziel`, `quantile-based trading`, `QBTS`, `DLENAR`, `Probabilistic Forecasting for Day-ahead Electricity Prices` and `Economic Evaluation of Predictive Accuracy` each return **exactly this record and nothing else**, `2604.19580` goes from 4 files to 5 with the increment being this record, `Hirsch & Ziel` from 2 to 3 and `Uniejewski` from 1 to 2 (both increments this record), and `coverage_manifest.csv` (5,808 lines) still returns 0 for `2604.19580`, `Simon Hirsch`, `Florian Ziel`, `QBTS` and `DLENAR`. `git log --oneline -20` was inspected as a convenience glance only and does **not** by itself satisfy dedup. `git pull origin main` at run start fast-forwarded `6ff1571` to `36a3b84` (another scout's TradingView record), and `HEAD == origin/main == 36a3b84` was re-confirmed immediately before commit.

**Conclusion:** no existing record has this source identity, so a new record is admissible under the dedup contract.

## Economic mechanism

### Source-reported

The source is an **evaluation-methodology paper**, not a profitability claim. Its stated mechanism has three linked parts.

1. **Quantile-based trading strategies (QBTS) are gameable.** QBTS (attributed to Uniejewski 2025, first circulated 2023; extended by O'Connor et al. 2024, 2025a, 2025b as TS-1/2/3) picks hour `b` as the arg-min and hour `s` as the arg-max of the *median* forecast (with `b != s`), then places a coupled limit buy at the `(1-alpha)`-quantile for `b` and a limit sell at the `alpha`-quantile for `s`. Proposition 1 decomposes expected profit into an acceptance-probability term times an expected-profit-if-accepted term and states the expression "is not uniquely maximized for the true forecast, but is potentially maximized by an overdispersed respectively underdispersed forecast": widening the forecast raises the acceptance region (Figure 2) while lowering the conditional margin, and the net sign depends on `alpha` and on the buy/sell price spread. The Gaussian simulation of Figure 3 shows cells where a dispersion-multiplied forecast earns **more** expected profit than the perfect forecast: in the `Profit, mu_b = 50, mu_s = 100, sigma = 10` panel the top row (risk level `alpha = 0.05`, verified because the matching acceptance-probability cell at dispersion `1.0` prints `0.90 = (1-0.05)^2`) prints `26.5 36.0 47.0 49.9 49.9` across scale-inflation factors `0.25 0.5 1.0 2.0 4.0`, so the perfect forecast earns `47.0` while the over-dispersed forecasts earn `49.9`; the same panel's bottom row (`alpha = 0.5`) is flat at `16.4`, and the narrower-spread `mu_b = 90, mu_s = 100, sigma = 10` panel moves the other way (`9.2 10.9 11.0 10.0 10.0` on its top row), which the source describes as profits decreasing under over-dispersed, low-`alpha` forecasts "since we start to accept more unprofitable trades". Remark 1 expresses acceptance probability through the copula, `AP = (1-alpha) - C_{b,s}(1-alpha, alpha)`, and the paper states that positive cross-hour correlation reduces AP and that QBTS therefore "does not capture this effect and hence can lead to suboptimal bids".

2. **Battery trading strategies are not strictly proper scoring rules.** Proposition 2 states that battery optimization "compress[es] the distributional information", so distinct forecasts `F_1 != F_2` can produce the same objective value `rho` and the same ranking of `(b,s)` pairs. Example 1 constructs forecasts that differ arbitrarily far from the truth outside the two hours that matter; Example 2 constructs distinct covariance structures with identical profit-distribution variance (Equation 28). The source's own summary: "economic backtest performance can be decision-relevant, but it is generally unsuitable as a stand-alone strictly proper scoring rule for model selection over full predictive distributions."

3. **The alternative is a stochastic program on the full joint distribution.** Draw `M` multivariate scenarios, compute the revenue distribution for every admissible schedule, optimize a risk measure `rho` (expected profit, or CVaR), and submit unrestricted day-ahead bids -- either by dynamic programming over single `(b,s)` pairs (Section 3.1, Algorithm 3) or by the mixed-integer linear formulation of Equations (12) to (20) solved with `pyomo` and the HiGHS solver. Because risk-neutral optimization only ever reads the point forecast, the source confines its economic discussion to the risk-averse case ("Given the fact that risk-neutral optimization approaches do not profit from probabilistic forecasting, we focus our discussion on the risk-averse case"). Decision quality is then assessed by cross-scoring every model's optimal bids against every model's forecast and by a Diebold-Mariano test of Equation (30); a Kendall's-tau kernel score (Equation 41, Proposition 3) is proposed as a proper score for the dependence structure.

**Closing recommendation of the source:** "the economic evaluation of probabilistic forecasts should be treated as an additional layer, not only as forecast evaluation, but as decision quality evaluation. A robust procedure therefore combines (a) forecast evaluation using (strictly) proper scoring rules, and (b) objective-aligned decision diagnostics, and (c) the evaluation of economic performance measures."

### Research interpretation

This record captures an **evaluation-artifact hypothesis**, not a directional premium. Two falsifiable claims are separated because they can fail independently.

- **H1 (gaming / incentive hypothesis).** A forecaster who inflates the dispersion of an otherwise unbiased day-ahead price distribution can raise *realized* QBTS battery profit without improving, and while worsening, calibration. If true, any "economic value of better forecasts" number produced by a QBTS-style backtest is partly a measurement artifact of the forecaster's own dispersion choice rather than skill. Mechanism class: **strategic misreporting against a non-proper scoring rule**, not a market friction and not a return premium.
- **H2 (information-bottleneck hypothesis).** Battery P&L compresses the predictive distribution onto the handful of hours the optimizer actually touches, so profit-based model rankings are unstable to battery configuration (duration, cycles) while proper-score rankings are stable. Mechanism class: **measurement bottleneck / low discriminatory power**.

Component roles, with source-vs-research labels:

```text
Regime:            none proposed -- the source is a measurement claim, not a conditional strategy
Primary signal:    multivariate scenario forecast -> risk-measure optimization over admissible
                   charge/discharge schedules -> unrestricted day-ahead bids (source-reported,
                   Sections 3.1, 3.2, Algorithms 1-3, Equations 12-20)
Risk / state:      battery physics only -- capacity kappa, round-trip efficiency eta, charge
                   limits (18), storage empty at h = H (19), cycle limit (20), no simultaneous
                   buy and sell in one hour (15) (source-reported)
Evaluation layer:  proper scoring rule + objective-aligned decision diagnostics + economic
                   performance, three layers jointly (source-reported, Section 7)
Cost layer:        none modelled by the source; any fee/spread/impact ladder below is
                   research-proposed
```

**Alpha translation.** As an executable rule, the only strategy in the source is "optimize a risk measure of the scenario-implied revenue distribution over admissible schedules and submit unrestricted day-ahead bids on the day-ahead auction." The source explicitly disclaims the profitability question ("We do not focus on the absolute profitability of BESS investments in energy markets"). Any use of this record as a *trading* candidate therefore rests on a research-proposed step -- attaching a cost and impact model -- that the source never performs, and every threshold used below to test H1/H2 is `research-defined`.

## Signal

Everything in this section is `source-reported` unless explicitly prefixed `research-proposed`.

**Formation timestamp and tradability**

- Delivery day `d` prices are set by a uniform-price auction "cleared at 12:00 CET for the delivery of electricity on the next day" (Section 4.1). The forecast and the bid decision therefore have to be complete before the 12:00 CET gate of the day before delivery; the source does not print an explicit issue timestamp for the forecast itself (**data gap**).
- Regressors are lagged so that they are available at decision time: prices of the previous day, time-series lags `l = 2..14` of the same delivery hour, weekday and holiday dummies, residual load for delivery day `d`, and fuel/EUA prices at `d-2` (Equation 31).

**Lookback and estimation window**

- Training window `2015-01-15` to `2018-12-26`; test window `2018-12-27` to `2023-12-31`; the supplementary states `T = 1831 out-of-sample days`, and the inclusive day count of that test window is independently recomputed as **1831**, matching.
- Parameters are estimated "in a expanding window fashion using the online learning algorithm developed in Hirsch et al. (2024)", **separate models per delivery hour**. Endpoints inclusive; no rolling re-estimation schedule beyond the expanding window is stated.

**Forecast models (seven, all sampled for the stochastic program)**

| Label | Marginal | Dependence | Source |
|---|---|---|---|
| Climatology | bootstrap draw from in-sample observations of the same hour | -- | Gneiting & Raftery (2007) benchmark |
| Naive-BS | `P_{d,h} = P_{d-7,h} + eps_d`, weekday-matched bootstrap | full error trajectories | Ziel & Weron (2018) |
| LEAR-N(0, Sigma) | LEAR mean (Lago et al. 2021), multivariate normal on residuals | empirical `Sigma` | Lago et al. (2021) |
| LEAR-BS | LEAR mean, k-means day clustering + k-nearest-neighbour cluster pick | sampled residual paths | Section 4.2, Appendix A |
| DLENAR-IND | GAMLSS Student-t (`mu`, `sigma`, `nu`), Equation (31) + Equations (49) | `Omega = I` | this paper |
| DLENAR-DEP | same marginal | empirical correlation `dcorr(g)` on the Gaussian copula scale | this paper |
| DLENAR-DWD | same marginal | per-weekday correlation matrices | this paper |

- The DLENAR mean (Equation 31) = previous-day 24 prices + lags `l = 2..14` of the same hour + weekday/holiday dummies + a b-spline of degree 2 with 4 knots on residual load + residual-load x marginal-cost interactions for gas, coal and oil, with fuel and EUA prices at `d-2`. Scale (Equation 49) uses the same regressors with linear residual-load and fuel terms; degrees of freedom are intercept-only with inverse-softplus links.
- Dependence is fitted by inference-for-margins: in-sample PIT to `U(0,1)`, inverse-quantile transform to `N(0,1)`, correlation fitted on that scale, then rank-reordering so that **marginals are exactly identical across the three dependence variants** (Section 4.2 and the supplementary six-step recipe). This is why Table 3's MAE, RMSE, CRPS, MPD and MHD columns are identical for all three DLENAR rows.

**Scenario generation**

- `M = 2500` scenarios per day for `H = 24` hours over `T = 1831` out-of-sample days. The supplementary states this "gives close to 109 Mio random numbers"; the product `2500 * 24 * 1831 = 109,860,000` reproduces that statement. The same paragraph gives `2500 * 0.1 = 250` worst samples for a CVaR level it calls `alpha = 0.1`.

**Battery and objective (Table 2, verbatim)**

- Storage `kappa = 10 MWh`.
- Duration `d = kappa / xi` in `{1, 2, 4}` hours, "translates to `xi in 10, 5, 2.5 MW`".
- Number of cycles `c` in `{1, 2}` cycles per day.
- Round-trip efficiency printed as `eta 2 = 0.952` in Section 4.3. The extracted rendering does not disambiguate whether the trailing digit belongs to the value (`eta^2 = 0.952`) or is a footnote marker after `eta^2 = 0.95`; **the exact round-trip efficiency is therefore a data gap** and no profit figure below is reproducible without it.
- Objectives: `Expected Profit (Risk-neutral)` and `Conditional Value-at-Risk (CVAR, risk-averse, alpha in 0.5, 0.75, 0.9)`. The symbol `alpha` is used for the confidence level in Table 2 but for the tail fraction in the supplementary ("a CVAR optimization at the `alpha = 0.1` level"); the convention is not reconciled in the source (see Limitations).
- Optimization methods: `Dynamic Programming (DP)` and `Mixed-Integer Linear Programming (MILP)`; solver `pyomo` + `HIGHS` (Section 3.2).

**MILP constraints (Equations 12-20, verbatim structure)**

- Objective `max rho(R_m)` over scenario revenues `R_m` (Equation 13).
- Bid volume bounded by charge/discharge capacity (14); no simultaneous buy and sell in one hour (15); buy-bid count `<= N_b` (16) and sell-bid count `<= N_s` (17); running charge limits (18); **storage empty at `h = H`** (19); cycle limit (20). `N_b` and `N_s` are never given numeric values; Section 6.3 names `MILP-24` as "the MILP optimization allowing for up to 24 bids per day", so `N_b + N_s <= 24` is the only bound implied -- **the split between `N_b` and `N_s` is a data gap**.

**Decision rule**

- One decision per day. `DP` picks the single `(b, s)` pair maximizing the discretized risk measure over scenarios (Algorithm 3); `MILP` returns a set of hourly bid volumes. There is **no stop, no take-profit, no re-entry rule, no holding-period logic beyond the intraday charge/discharge cycle, and no position-sizing rule other than the capacity constraints**. Abstention on a given hour is possible only through the MILP's count limits and the risk measure, not through an explicit no-trade threshold -- unlike the stopping rule used by the sibling BESS record.

**Baselines the source attacks (printed algorithms, supplementary)**

- `Algorithm 1 (QBTS)`: `b = argmin Q^0.5_h`, `s = argmax Q^0.5_h` with `b < s`; limit buy at `Q^(1-alpha)_b`, limit sell at `Q^alpha_s`; accept iff `P_b <= Q^(1-alpha)_b` and `P_s >= Q^alpha_s`; pay off battery profits adjusted for efficiency if accepted, else 0.
- `Algorithm 2 (TS-1)`: choose hours from the `alpha` and `1-alpha` quantiles with `b < s`, then place **unlimited** orders, so bids are always accepted.

**Underspecified in the source:** the b-spline knot locations (printed only as "a b-Spline basis of degree 2 and 4 knots"), the exact exogenous availability timestamps, `N_b`/`N_s`, the CVaR `alpha` convention, the round-trip efficiency, and any parameter-tuning protocol (the source states it "ha[s] not undertaken extensive feature engineering or hyperparameter optimization").

## Required data

- **Instrument:** German day-ahead electricity, hourly delivery products (`H = 24` delivery hours per day), quoted in EUR/MWh. No futures, no options, no intraday or balancing product is traded in the reported experiments.
- **Universe:** a single bidding zone (Germany) and a single market stage (day-ahead). No inclusion/exclusion, liquidity, listing or survivorship rule is stated because the universe is a fixed 24-hour product grid; **reconstitution and survivorship rules: not applicable / not stated**.
- **Venue / market type:** the integrated day-ahead auction of the single day-ahead coupling (SDAC) as organised on EPEX SPOT; the source refers to "the day-ahead market ... organized as a uniform price auction" and cites the EPEX trading brochure. No order-book, no matching-engine data.
- **Timeframe:** hourly bars per delivery hour, one decision per delivery day; the source notes the "recent market change to quarter-hourly trading in the single day-ahead coupling (SDAC)" as a computational motivation but does **not** run quarter-hourly experiments (**data gap**).
- **Fields actually used** (Section 4.2, Appendix A, all `source-reported`):
  - day-ahead price vector of the previous day (24 values) and same-hour lags `l = 2..14`;
  - residual load for the delivery day;
  - weekday dummies plus a separately encoded public-holiday dummy (Ziel 2018);
  - gas price `EUR/MWht`, coal price `EUR/t`, oil price `EUR/bbl` at `d-2`, and EUA price `EUR/tCO2` at `d-2`;
  - conversion factors `nu` (fuel unit to MWht) printed in Appendix A as gas `-`, coal `1/8.144 t/MWht`, oil `1/1.17 bbl/MWht`, and `CO2 Factor (eta)` printed as `0.2`, `0.3`, `0.27` (which conflicts with Section 4.2's `0.2 / 0.35 / 0.3` -- see contradictions);
  - round-trip efficiency `eta` and capacity `kappa`, `xi` from Table 2.
- **Fields NOT used:** no order book, no depth, no trades or aggressor side, no open interest, no funding, no mark/index/basis, no options surface, no borrow, no on-chain or sentiment data.
- **Point-in-time:** the auction gate is 12:00 CET; fuel and EUA regressors are lagged to `d-2`; the source prints no publication-vintage, revision or availability-lag handling for ENTSO-E/investing.com series -- **point-in-time correctness is a data gap**.
- **Timestamp / timezone:** the source states the 12:00 CET clearing time once and otherwise does not specify timestamp granularity, clock source, alignment or out-of-order handling -- **data gap**.
- **Missing data:** no null, stale, suspended, partial or bad-print rule is stated anywhere in the pinned text -- **data gap**; imputation policy not specified.
- **Cost/fee/spread fields:** none requested. The only friction-like quantity is the physical round-trip efficiency `eta`. There is **no fee, commission, spread, slippage, funding, borrow or impact input** in the data requirements.
- **Third-party dataset:** Lipiecki, Uniejewski & Weron (2024) compilation of ENTSO-E and investing.com, covering 2015-2023; **not fetched this run**, so its exact contents, revisions and access path are **data gap**.

## Execution assumptions

Determined at Methods level from Sections 2.1, 3.1, 3.2, 4.1, 4.3, 4.4, Equations (4), (5), (12)-(20), Algorithms 1-3 and Table 2, plus a word-boundary and substring census of the pinned 140,051-character text layer.

- **Signal-to-order timing:** one bid decision per delivery day, in the uniform-price auction closing at 12:00 CET on the day before delivery. Same-day decision and same-day clearing; no latency model.
- **Order type:** `QBTS` and `TS-1` place **limit** orders (QBTS) or **unlimited** orders (TS-1); the paper's own DP/MILP variants place **unrestricted bids**, i.e. the source's headline profits assume unconditional acceptance in the day-ahead auction.
- **Fill model:** for QBTS, coupled acceptance of the buy and sell leg ("either both are executed or neither is executed"), which the source relates to the EPEX loop-bid product but explicitly declines to model as a loop bid because loop bids are conditional on total cash flow. For the DP/MILP variants there is **no fill model at all** -- bids are assumed to clear at the auction price.
- **Fees / commissions / spread / slippage / impact / latency / borrow / leverage / margin / liquidation / turnover / maker / taker / queue:** substring counts over the pinned text are `transaction cost` = **1** and `transaction costs` = **1**, both produced by the **same single occurrence** (one hit in total) inside the reference title *"Trading large volumes of power with market impact and transaction costs"* (Narajewski & Ziel 2022); `market impact` = **2**, the second being the Section 4.3 sentence *"For larger battery capacities, we would need to take market impact into account (see Narajewski and Ziel, 2022), which is beyond the scope of this paper."*; `fee` = 0, `fees` = 0, `commission` = 0, `slippage` = 0, `bid-ask` = 0, `funding` = 3 (two acknowledgments plus the CRediT phrase "Funding acquisition"), `maker` = 1 (inside "decision-maker"), `taker` = 0, `fill` = 0, `latency` = 0, `borrow` = 0, `leverage` = 0, `liquidation` = 0, `turnover` = 0, `queue` = 0, `participation` = 0, `market order` = 0, `walk-forward` = 0, `CAGR` = 0, `drawdown` = 0, `win rate` = 0, `confidence interval` = 0. `spread` = **8** as a substring (**3** singular `spread`, **5** plural `spreads`), and every one of the eight means the buy/sell **price spread between delivery hours** (or a reference-title spread), never a bid-ask spread. **Conclusion: the only modelled friction is physical round-trip efficiency; every monetary friction is a `data gap` and must not be read as zero-cost evidence.**
- **Capacity / impact:** the source conditions its own scope on capacity -- *"For larger battery capacities, we would need to take market impact into account ... which is beyond the scope of this paper"* -- so all reported profits are for a 10 MWh asset with no market-impact term.
- **Leverage / margin / shorting / borrow:** not applicable to a physical battery in the source's framing; no financial leverage modelled; **not stated**.
- **Partial fills / failures / re-bidding:** not modelled; the auction either clears the submitted bid matrix or it does not, and no rejection or amendment rule is printed -- **data gap**.
- **What the source assumes vs what a researcher must assume:** acceptance of unrestricted bids, a fixed 10 MWh asset, and zero monetary costs are **source-assumed**; any fee schedule, spread, slippage, participation cap or impact model used later is **research-proposed** and is introduced only in the falsification plan below.

## Evidence

### Source-reported

All figures below are read from the pinned 3,907,780-byte PDF and are **third-party claims**. Test window for every table and figure is `2018-12-27` to `2023-12-31` (T = 1831 days); training window `2015-01-15` to `2018-12-26`; universe German day-ahead hourly; asset a 10 MWh battery; **all monetary results are gross of every trading cost** (see Execution assumptions).

**Table 3 -- statistical scoring rules (7 models x 12 columns, every cell).** Columns as printed: `MAE`, `RMSE` (header glyph rendered `sqrt(RMSE)`, defined in Equation 35 as `sqrt(MSE)`), `CRPS`, `VS 0.5`, `VS1.0`, `DSS`, `ES`, `Brier`, `RPS`, `KS`, `MPD`, `MHD`; lower is better throughout.

| Model | MAE | RMSE | CRPS | VS 0.5 | VS1.0 | DSS | ES | Brier | RPS | KS | MPD | MHD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Climatology | 69.766 | 112.770 | 56.318 | 9.072 | 1694.479 | 176.766 | 291.149 | 0.931 | 2.907 | 0.831 | 29.641 | 11.117 |
| Naive-BS | 34.487 | 61.676 | 29.235 | 5.416 | 1119.829 | 204.941 | 160.579 | 0.986 | 2.690 | 0.807 | 21.772 | 10.484 |
| LEAR-BS | 16.222 | 30.211 | 13.530 | 3.020 | 602.827 | 180.588 | 79.210 | 0.934 | 1.745 | 0.693 | 10.441 | 6.304 |
| LEAR-N(0, Sigma) | 16.339 | 30.357 | 13.220 | 3.049 | 611.727 | 182.419 | 77.292 | 0.893 | 1.721 | 0.690 | 10.537 | 6.322 |
| DLENAR-IND | 14.740 | 27.713 | 10.769 | 3.273 | 666.584 | 150.644 | 65.028 | 0.872 | 1.594 | 0.681 | 7.420 | 5.312 |
| DLENAR-DEP | 14.740 | 27.713 | 10.769 | 2.595 | 527.446 | 116.299 | 62.730 | 0.848 | 1.465 | 0.662 | 7.420 | 5.312 |
| DLENAR-DWD | 14.740 | 27.713 | 10.769 | 2.587 | 525.592 | 116.599 | 62.721 | 0.847 | 1.466 | 0.662 | 7.420 | 5.312 |

Internal consistency checks that reproduce: the three DLENAR rows share identical `MAE / RMSE / CRPS / MPD / MHD` (marginals are rank-reordered to be identical by construction) and differ only in `VS, DSS, ES, Brier, RPS, KS` (dependence-sensitive); `Brier` ranks Naive-BS (`0.986`) **worse** than Climatology (`0.931`), which the source explains explicitly.

**Table 4 -- top-k Brier scores (7 models x 16 columns: Low-k / High-k / Low-High-k / BESS-k, each at `k = 1, 2, 4, 8`).** Full rows as printed -- Climatology `0.88 0.89 0.90 0.92 | 0.86 0.87 0.89 0.92 | 0.87 0.88 0.90 0.92 | 0.88 0.89 0.91 0.93`; Naive-BS `1.01 0.99 0.99 0.99 | 0.86 0.91 0.94 0.97 | 0.94 0.95 0.97 0.98 | 0.98 0.98 0.98 0.99`; LEAR-BS `0.84 0.86 0.89 0.91 | 0.72 0.79 0.86 0.91 | 0.78 0.82 0.87 0.91 | 0.85 0.87 0.90 0.93`; LEAR-N(0, Sigma) `0.80 0.82 0.85 0.87 | 0.70 0.76 0.82 0.87 | 0.75 0.79 0.84 0.87 | 0.81 0.83 0.86 0.89`; DLENAR-IND `0.76 0.79 0.82 0.85 | 0.69 0.74 0.80 0.85 | 0.73 0.77 0.81 0.85 | 0.78 0.80 0.84 0.87`; DLENAR-DEP `0.73 0.76 0.79 0.82 | 0.64 0.70 0.77 0.82 | 0.68 0.73 0.78 0.82 | 0.74 0.77 0.81 0.84`; DLENAR-DWD `0.73 0.76 0.79 0.82 | 0.64 0.70 0.77 0.82 | 0.68 0.73 0.78 0.82 | 0.74 0.77 0.81 0.84`. Cell-by-cell comparison confirms the `BESS-k` block is **never better** than the `Low-k` and `High-k` blocks for any model and is strictly worse in most cells (Climatology ties at `k = 1, 2` and is worse at `k = 4, 8`), which the source attributes to the intuition "that the middle ranks are harder to predict than the lowest and highest ranks".

**Table 5 -- VaR exceedance rates (7 models x 18 cells: alpha in {0.5, 0.75, 0.9} x duration in {1, 2, 4} x cycles in {1, 2}).** Every cell, in printed column order:

| Model | alpha=0.5 (6 cells) | alpha=0.75 (6 cells) | alpha=0.9 (6 cells) |
|---|---|---|---|
| Climatology | -0.20 -0.25 -0.20 -0.25 -0.21 -0.24 | -0.11 -0.12 -0.10 -0.12 -0.10 -0.11 | -0.03 -0.04 -0.03 -0.04 -0.03 -0.03 |
| Naive-BS | 0.18 0.16 0.17 0.16 0.15 0.13 | 0.32 0.31 0.32 0.30 0.29 0.26 | 0.33 0.33 0.33 0.31 0.31 0.30 |
| LEAR-BS | 0.05 0.05 0.05 0.05 0.04 0.04 | 0.18 0.18 0.18 0.18 0.18 0.17 | 0.22 0.23 0.22 0.22 0.22 0.22 |
| LEAR-N(0, Sigma) | 0.06 0.07 0.06 0.06 0.07 0.06 | 0.13 0.14 0.12 0.12 0.12 0.12 | 0.12 0.13 0.11 0.12 0.12 0.12 |
| DLENAR-IND | 0.09 0.07 0.08 0.07 0.08 0.07 | 0.14 0.11 0.14 0.11 0.15 0.14 | 0.14 0.10 0.14 0.10 0.15 0.12 |
| DLENAR-DEP | 0.09 0.09 0.08 0.08 0.08 0.07 | 0.12 0.11 0.12 0.10 0.11 0.11 | 0.09 0.08 0.08 0.07 0.07 0.06 |
| DLENAR-DWD | 0.09 0.09 0.08 0.08 0.08 0.07 | 0.12 0.11 0.12 0.10 0.12 0.11 | 0.09 0.08 0.09 0.07 0.07 0.06 |

Caption verbatim: *"Value-at-Risk (VaR) exceedance rates. Negative values imply that the losses exceed the VaR more frequently than the nominal level."* Row extrema recomputed: Climatology `-0.25 .. -0.03` (entirely negative), Naive-BS `0.13 .. 0.33`, LEAR-BS `0.04 .. 0.23`, LEAR-N `0.06 .. 0.14`, DLENAR-IND `0.07 .. 0.15`, DLENAR-DEP `0.06 .. 0.12`, DLENAR-DWD `0.06 .. 0.12`. **No cell in the LEAR-BS row equals `0.11`.**

**Figure 9 -- total profit `[1000 EUR]`, MILP, 1 cycle, 21 cells per objective block (7 models x durations 1, 2, 4).** The PDF text layer emits each block as a flat list; the **model-major grouping below is `research-inferred`** (7 groups of 3 = durations 1, 2, 4), validated by seven exact matches between Figure 9's `alpha = 0.9, d = 1` cells and Figure 13's MILP-24 column (`611.4 / 827.9 / 1136.3 / 1127.8 / 1023.7 / 1075.6 / 1071.6`), and by the three DLENAR rows being identical only under this grouping.

| Model | Expected Value (1,2,4) | CVaR alpha=0.5 (1,2,4) | CVaR alpha=0.75 (1,2,4) | CVaR alpha=0.9 (1,2,4) |
|---|---|---|---|---|
| Climatology | 825.0 / 756.0 / 662.1 | 771.0 / 727.0 / 648.3 | 718.6 / 706.7 / 603.1 | 611.4 / 607.9 / *[gap]* |
| Naive-BS | 1010.1 / 962.8 / 854.2 | 974.9 / 930.7 / 828.9 | 933.7 / 894.2 / 791.4 | 827.9 / 789.9 / 697.3 |
| LEAR-BS | 1152.1 / 1098.7 / 976.4 | 1150.7 / 1096.7 / 974.6 | 1147.1 / 1093.6 / 969.9 | 1136.3 / 1083.5 / 961.9 |
| LEAR-N(0, Sigma) | 1152.1 / 1097.4 / 975.6 | 1146.8 / 1093.3 / 971.4 | 1140.7 / 1086.7 / 965.5 | 1127.8 / 1075.7 / 955.1 |
| DLENAR-IND | 1188.8 / 1132.4 / 1008.8 | 1132.4 / 1111.4 / 1002.9 | 1083.6 / 1077.4 / 991.8 | 1023.7 / 1022.2 / 962.9 |
| DLENAR-DEP | 1188.8 / 1132.4 / 1008.8 | 1172.5 / 1123.1 / 1001.1 | 1140.9 / 1097.6 / 984.8 | 1075.6 / 1039.1 / 938.1 |
| DLENAR-DWD | 1188.8 / 1132.4 / 1008.8 | 1170.9 / 1121.7 / 1000.4 | 1139.4 / 1096.0 / 982.9 | 1071.6 / 1032.6 / 931.4 |

The `CVaR alpha = 0.9, 1 cycle` block emits only **20 of 21** cells in the PDF text layer; the missing cell is the Climatology `d = 4` value (its `d = 1` and `d = 2` cells, `611.4` and `607.9`, are present). This is recorded as a **data gap**, not inferred.

**Figure 10 -- Sharpe ratio, 1 cycle, 21 cells per block (same grouping rule, `research-inferred`).** Expected Value `Climatology 0.82/0.82/0.81, Naive-BS 0.88/0.88/0.87, LEAR-BS 0.95/0.97/0.96, LEAR-N 0.96/0.97/0.96, DLENAR-IND 0.96/0.97/0.96, DLENAR-DEP 0.96/0.97/0.96, DLENAR-DWD 0.96/0.97/0.96` -- the three DLENAR rows are **identical** here, consistent with risk-neutral optimization reading only the point forecast, which all three variants share; CVaR `alpha = 0.9` `Climatology 0.92/0.92/0.93, Naive-BS 0.74/0.75/0.73, LEAR-BS 0.95/0.96/0.95, LEAR-N 0.94/0.95/0.94, DLENAR-IND 0.94/0.94/0.94, DLENAR-DEP 0.94/0.94/0.94, DLENAR-DWD 0.94/0.95/0.94`. The Sharpe ratio is defined by the source in Equation (32) as `E[r] / SD[r]` over daily battery returns, **without a risk-free rate and without any cost deduction**.

**Figure 13 -- DP versus MILP for the 1-hour, 1-cycle battery (21 cells per block; legend order `MILP 1, MILP 24, DP 1`, `research-inferred` grouping validated by the Figure 9 anchor).** Expected Value, model-major `(MILP-1, MILP-24, DP-1)` per model: Climatology `825.0 / 825.0 / 824.5`, Naive-BS `1010.1 / 1010.1 / 1009.6`, LEAR-BS `1152.1 / 1152.1 / 1151.7`, LEAR-N `1152.1 / 1152.1 / 1151.7`, DLENAR-IND `1188.8 / 1188.8 / 1188.3`, DLENAR-DEP `1188.8 / 1188.8 / 1188.3`, DLENAR-DWD `1188.8 / 1188.8 / 1188.3` -- recomputed MILP-1 minus DP-1 = `0.5, 0.5, 0.4, 0.4, 0.5, 0.5, 0.5` (thousand EUR). Number-of-no-bid-days block for CVaR `alpha = 0.9` in the same order: Climatology `692 / 0 / 689`, Naive-BS `508 / 296 / 498`, LEAR-BS `23 / 9 / 23`, LEAR-N `42 / 17 / 42`, DLENAR-IND `351 / 47 / 351`, DLENAR-DEP `149 / 66 / 149`, DLENAR-DWD `148 / 70 / 148` -- MILP-24 has fewer no-bid days than the two single-pair variants for every model, reproducing the source's sentence "the simplified approach has more no-bid days than the MILP-24 approach".

**Figure 6 -- constructed counterexample (the paper's own demonstration of H2).** Forecast legends `F0: MAE=30.40, F1: MAE=32.47, F2: MAE=245.41, F3: MAE=142.16, F4: MAE=50.02`; optimal-bid P&L legends for the 1-hour battery `F0..F5: P&L=974.2` (all six identical), for the 2-hour battery `F0 495.6, F1 827.4, F2 485.9, F3 962.0, F4 962.0, F5 962.0`, and for the 4-hour battery `F0 247.8, F1 413.7, F2 247.8, F3 481.0, F4 481.0, F5 481.0`. The text layer prints **five** MAE entries but **six** P&L entries per panel, so the per-forecast correspondence for `F5` is a **data gap**; the source's own caption states that the forecast whose MAE is `245.41` still earns the same expected revenue as the near-perfect ones for the 1-hour battery, and that "a relatively small change in the asset portfolio can make a previously optimal forecast perform very poorly".

**Cross-scoring (Figures 11 and 12 in the main text, plus figures 3 to 6 of the Supplementary Material).** Verbatim claims that reproduce from the printed matrices: for VaR `alpha = 0.9, d = 1, c = 1`, the Naive-BS row (`59.4 159.8 104.1 100.8 78.9 81.3 80.2`) is the column-wise maximum for **all seven** columns, reproducing "the Naive-BS model has the worst scores for the optimal bids derived from itself, but also for all other models' optimal bids"; a DLENAR row attains the column-wise minimum in **every** column of the VaR `alpha = 0.5, d = 1, c = 1` panel; and the hatched cells mark non-rejection of `H0` in Equation (30), i.e. Diebold-Mariano comparisons at an unstated level (**data gap**).

**Prose claims quoted with their printed anchors.**

- "For the optimization with respect to the expected profits, the DLENAR models yield the highest profits." -- reproduced from Figure 9's Expected Value block, where all three DLENAR rows are `1188.8 / 1132.4 / 1008.8` and no other model reaches those cells.
- "the LEAR-BS model ... also has exceedance rates of 11% to 23% above the nominal level" and "The LEAR-N(0, Sigma) model ... has exceedance rates of 5% to 15% above the nominal level." -- **not reproducible from Table 5**; recorded as contradiction 3.
- "the climatology model has VaR exceedance rates below the nominal level and, for alpha = 0.9, also very close to the nominal level" -- the climatology row is indeed entirely negative, but the Table 5 caption assigns the opposite sign to negatives; recorded as contradiction 2.
- "total achieved profits are no suitable measure to compare model performance in a risk-averse setting" and "measures of decision quality and scoring rules disagree also in the probabilistic setting" -- the source's headline interpretation.
- "the profits are exactly the same for the simplified BESS and the MILP approach" -- contradicted by Figure 13's Expected Value block; recorded as contradiction 6.

**Supplementary quantitative identities that reproduce independently:** `T = 2500 x 24 x 1831` random numbers = `109,860,000` against the printed "close to 109 Mio random numbers"; `2500 x 0.1 = 250` worst samples as printed; the inclusive day count of `2018-12-27 .. 2023-12-31` = `1831` as printed.

### Independently reproduced

not independently reproduced

The only checks performed this run are checksum and arithmetic checks of the pinned artefact itself (both pinned file digests recomputed, printed literal tracing, and the three supplementary identities above). No forecast, optimization, backtest or trading simulation was run, no market data was downloaded, and no third-party code was executed.

### Negative evidence

1. **No monetary friction anywhere.** `transaction cost(s)` occurs exactly once and only inside the reference title of Narajewski & Ziel (2022); `market impact` occurs twice, once in that same reference title and once in the sentence placing impact "beyond the scope of this paper"; `fee`, `fees`, `commission`, `slippage`, `bid-ask`, `taker`, `fill`, `latency`, `borrow`, `leverage`, `liquidation`, `turnover`, `queue`, `participation`, `market order`, `walk-forward`, `CAGR`, `drawdown`, `win rate`, `confidence interval` are all 0. Every profit and Sharpe number in this record is therefore **gross of trading cost**.
2. **The source explicitly disclaims the profitability question:** "We do not focus on the absolute profitability of BESS investments in energy markets ... or on sophisticated, multi-market optimization."
3. **The headline over-dispersion result is derived under an assumption the source itself rejects.** Section 2.2 states "For simplificity, we assume that delivery periods are independent" when showing that an over-dispersed forecast can beat the perfect one; Remark 1 and Figure 4 then show real delivery hours are positively correlated and that this "further weakens the validity of QTBS for forecast evaluation". The demonstration regime and the empirical regime are not the same regime.
4. **Proposition 2 is constructive, not general.** It is exhibited through Examples 1 and 2 for specific `rho` values (expected revenue and a normal profit distribution); the source never proves non-properness for every risk measure or every battery configuration.
5. **One market, one vendor compilation, one split.** German day-ahead only; ENTSO-E/investing.com data as compiled by Lipiecki et al. (2024); a single train/test cut (`2015-01-15..2018-12-26` / `2018-12-27..2023-12-31`); `walk-forward` = 0, `hold-out` = 0, `holdout` = 0 occurrences. No rolling origin, no second market, no second split.
6. **No multiple-comparison control.** The supplementary Figure 2 prints pairwise Diebold-Mariano grids for eight scores over a 7x7 model set, and the hatched cells of Figures 11-12 encode non-rejection, yet `Benjamini` = 0, `FDR` = 0, `multiple testing` = 0, `multiplicity` = 0, `Bonferroni` = 0 occurrences, and the significance level of the DM tests is never stated (**data gap**).
7. **The QBTS results themselves are not numerically printed.** Figures 14 and 15 (total profit, profit per MWh traded, realized and expected acceptance probability versus nominal prediction-interval coverage) are line plots whose text layer carries only axis ticks -- **all exact QBTS performance numbers are a data gap**, so the very strategy the paper criticises cannot be quantified from the pinned artefact.
8. **The best-Sharpe model is the worst forecaster.** Climatology ranks last on every statistical score in Table 3 (MAE `69.766`, CRPS `56.318`) yet posts Sharpe `0.92/0.92/0.93` at CVaR `alpha = 0.9`, 1 cycle; the source attributes this to conservative bids with low profit and low volatility, i.e. a risk-management artefact, not forecast skill.
9. **Risk-neutral optimization ignores the predictive distribution entirely** (the source's own statement), so the "economic value of probabilistic forecasts" survives only in the risk-averse branch -- and there the LEAR-BS model, which Table 3 shows is *worse* than LEAR-N on CRPS (`13.530` vs `13.220`) and worse than all three DLENAR variants, earns the highest Figure 9 profit at CVaR `alpha = 0.9` and `0.75` for the 1-hour battery.
10. **Calibration evidence is unreadable as printed.** The VaR definition, the exceedance-ratio target, the Table 5 caption and the Section 6.2 prose disagree (contradictions 1, 2, 3), so no independent reader can recover the sign or the level of the reported exceedance deviations without guessing.
11. **The exact round-trip efficiency is not decidable from the pinned text** (`eta 2 = 0.952`), and `N_b`/`N_s` and the CVaR `alpha` convention are unstated, so profit levels are **not reproducible** from the artefact alone.
12. **The symbol `alpha` is used for two different quantities:** a confidence level in Table 2 (`0.5, 0.75, 0.9`) and a tail fraction in the supplementary ("a CVAR optimization at the `alpha = 0.1` level ... worst `2500 x 0.1 = 250` samples").
13. **Model specification was not tuned or hardened:** "we have not undertaken extensive feature engineering or hyperparameter optimization, but chose a configuration that has been shown to work well in previous work."
14. **No artefact for reproduction:** `repository` = 0, `code availab` = 0, `data availab` = 0, `reproduc` = 0 occurrences; no GitHub URL, no immutable commit, no environment or seed (`seed` = 0, `random seed` = 0 occurrences).
15. **Preprint and disclosed interest.** No journal reference, no publisher DOI, no peer-review statement; Simon Hirsch is declared as "employed as industrial Ph.D. student with Statkraft Trading GmbH", funding is declared from Statkraft and from DFG TRR 391, and Github Copilot use is declared. `competing` = 4 occurrences, all ordinary prose ("competing forecasts/models"), so there is **no competing-interests declaration**.
16. **The source admits its own metric hides skill:** "the decision not to trade (in a certain hour) can also be a valuable decision, but is not as prominently captured in the evaluation. This hides part of the forecaster's skill."
17. **The 10 MWh asset is not scaled:** impact is declared out of scope, so nothing in the record supports a capacity claim above 10 MWh.
18. **Zero digital-asset content:** `crypto` = 0, `bitcoin` = 0, `ethereum` = 0, `perpetual` = 0, `binance` = 0, `usdt` = 0 occurrences. There is no evidence of any kind for crypto portability, and no negative result from crypto either -- absence of evidence only.

## Falsification plan

Two hypotheses are tested separately. Every threshold, grid, metric and action below is **`research-defined falsification threshold` / `research-proposed`** -- none of it is in the source. **No-retuning rule:** once a gate is run, the model set (7), the battery grid (`d in {1,2,4}`, `c in {1,2}`), the objective set (expected value, CVaR at `0.5/0.75/0.9`), the dispersion grid, the windows and every threshold in this section are frozen; a failed gate may not be re-run with a loosened cut, and any change requires a new record version.

**H1 -- QBTS profit is not monotone in forecast quality (gaming).**

- **F1 (`research-defined`, printed-value reproduction).** Every source-reported number quoted in this record must appear verbatim in the pinned 3,907,780-byte PDF text layer. *Action on failure:* delete the number from the record; if a headline claim loses its anchor, set `confidence: low`.
- **F2 (`research-defined`, provenance integrity).** arXiv `2604.19580` must still resolve to a single version `v1` with the pinned digests. *Action on failure:* re-pin the new version, re-read end to end, and re-run F1.
- **F3 (`research-defined`, parameter completeness -- **currently failing**).** Exact round-trip efficiency, `N_b`/`N_s` and the CVaR `alpha` convention must be stated by the source before any numeric reproduction of profit. *Action on failure:* the record stays `research-only` and no profit figure may be reproduced or cited as reproducible.
- **F4 (`research-defined`, gaming reproduction -- the core test).** On the source's own test window, hold the marginal centre fixed and multiply forecast dispersion by `b in {0.25, 0.5, 1.0, 2.0, 4.0}` (the source's own Figure 3 grid), then run Algorithm 1 at `alpha in {0.05, 0.10, ..., 0.50}`. **H1 is supported** if at least one `b > 1` cell yields higher realized QBTS profit than `b = 1.0` **while** CRPS is strictly worse than at `b = 1.0`. **H1 is falsified** if no `b != 1` cell beats `b = 1.0` at any `alpha`, or if every profitable distortion also improves CRPS. *Action on failure:* mark H1 `rejected-in-research` and stop treating QBTS profit as a gameable metric.
- **F5 (`research-defined`, dependence placebo).** Repeat F4 after replacing the joint forecast with independent hourly marginals and, separately, after permuting the within-day hour labels 1,000 times (`research-proposed`). **H1 is weakened** if the over-dispersion gain appears in both placebo arms at the same rate as in the true arm; *action:* attribute the gain to the acceptance-region geometry rather than to any exploitable structure.

**H2 -- battery-profit evaluation has low discriminatory power (ranking instability).**

- **F6 (`research-defined`, ranking-stability gate).** Compute the 7-model Spearman rank correlation of *battery profit* and of *CRPS* across all six configurations `(d, c)`. **H2 is falsified** if the profit ranking is stable at `rho >= 0.90` for every configuration pair while the CRPS ranking is unchanged; **H2 is supported** if any configuration pair gives profit `rho <= 0.50`, or if the profit winner changes between `d = 1` and `d = 4`. *Action on failure:* drop the "low discriminatory power" language and re-describe the metric as configuration-robust.
- **F7 (`research-defined`, counterexample search).** Draw 10,000 forecast pairs `(F1, F2)` with `F1` equal to the reference DLENAR-DEP ensemble and `F2` perturbed outside the optimizer's selected hours; **H2 is falsified** if no pair achieves an absolute CRPS gap of at least `20%` of `CRPS(F1)` while producing the identical optimal bid set for all six configurations. *Action on failure:* Proposition 2's practical relevance is marked unproven for this asset.
- **F8 (`research-defined`, three-layer agreement gate).** Rank the seven models by (a) proper score, (b) cross-scored decision quality and (c) profit. **The source's own recommendation is falsified** if layer (a) never adds information beyond (c): specifically, if `Kendall tau` between (a) and (c) is `>= 0.90` in all six configurations, then the three-layer procedure collapses to a single layer. *Action on failure:* record the three-layer procedure as redundant for this sample.

**Economic robustness gates (all cost and capacity inputs are `research-proposed`).**

- **F9 (`research-defined`, cost ladder).** Re-run the profit ranking with round-trip efficiency held at the source's value and an added monetary ladder of `0 / 0.5 / 1 / 2 / 5 EUR per MWh` **`research-proposed`**, applied symmetrically to the buy and sell legs. **The profit-based ranking is not cost-robust** if the model ordering changes at three or more of the five levels. *Action on failure:* any downstream candidate must be re-derived from gross numbers only, and no net-of-cost claim may be inherited from this record.
- **F10 (`research-defined`, capacity / impact gate).** Repeat the experiment at `100 MW` and `1000 MW` **`research-proposed`** sizes with a linear impact term of `0 / 0.01 / 0.05 EUR per MWh per MW traded` **`research-proposed`** (the impact model itself is the source's cited Narajewski & Ziel (2022), not read this run). **Scaling claim falsified** if the model ordering at 10 MWh does not survive either size. *Action on failure:* the record remains pinned to the 10 MWh asset with no capacity extrapolation.
- **F11 (`research-defined`, second-window and second-market gate).** Freeze the entire specification and evaluate on `2024-01-01` onward **`research-proposed`** (the source's data ends `2023-12-31`), and replicate on one non-German bidding zone **`research-proposed`, e.g. France or Spain day-ahead**. **Robustness falsified** if the Expected-Value ordering `DLENAR > LEAR > climatology` reverses for two of three durations in either arm, or if the climatology Sharpe observation (`>= 0.90` at CVaR `alpha = 0.9`, 1 cycle) flips below `0.80`. *Action on failure:* mark both the ordering and the Sharpe observation as single-window artefacts.
- **F12 (`research-defined`, multiplicity gate).** Apply Benjamini-Hochberg at `q < 0.10` **`research-proposed`** across the full family of pairwise DM tests implied by the 7x7 grid over all eight scores in supplementary Figure 2. **Falsified as evidence** if any cell the source marks significant loses significance after correction. *Action on failure:* remove every significance claim inherited from the hatched-cell figures and keep only point estimates.

**Boundary gate.** No crypto statement of any kind may be added to this record until the QBTS gaming experiment is re-derived with funding, mark/index price, liquidation and 24/7 session structure; until then crypto portability stays `unproven` regardless of any electricity-side result.

## Crypto portability

`unproven`

The pinned text contains **zero** occurrences of `crypto`, `bitcoin`, `ethereum`, `perpetual`, `binance` or `usdt`, so nothing in the source demonstrates this mechanism on digital assets. The record therefore treats it as a **ported hypothesis, not crypto empirical evidence**.

What fails to port as printed:

- **Physical asset:** the object being optimized is a 10 MWh battery with round-trip efficiency, charge limits, a cycle limit and an end-of-day empty-state constraint (Equations 18-20). A crypto position has no such state constraints, so the whole MILP collapses into ordinary portfolio selection and the "battery" framing loses content.
- **Market structure:** a single uniform-price auction gated at 12:00 CET, versus 24/7 continuous trading with maker/taker fees, order books and queue priority. There is no analogue of the coupled buy/sell acceptance rule or the EPEX loop bid.
- **Data dependencies:** ENTSO-E residual load, gas/coal/oil marginal costs and EUA prices have no crypto counterpart.
- **Missing crypto mechanics entirely:** funding rate, mark/index versus last-price, liquidation and leverage, venue fragmentation and survivorship, stablecoin and quote-currency effects, custody and withdrawal risk, and candle-boundary/timezone conventions are all unaddressed (`funding` appears only in the acknowledgments, `liquidation` = 0, `leverage` = 0).

What *might* port in adapted form, and only as a research question: the **evaluation** claim (H1/H2) is about scoring rules rather than about electricity. If a crypto evaluation pipeline ranks models by realized strategy P&L on a compressed action set, the same information-bottleneck argument applies in principle -- but that is a `research-proposed` analogy, not evidence, and it must not be recorded as `direct`.

## Limitations

- `underspecified`: round-trip efficiency (`eta 2 = 0.952`), `N_b`/`N_s`, the CVaR `alpha` convention, b-spline knot locations, forecast issue timestamp, timestamp/timezone policy, missing-data policy, DM significance level, `F5`-to-`F6` per-forecast mapping in Figure 6.
- `data gap`: one of 21 cells in Figure 9's CVaR `alpha = 0.9` block; every numeric value of Figures 14 and 15 (the QBTS results); all point-in-time/vintage handling; the Lipiecki et al. (2024) dataset itself.
- `not independently reproduced`: all forecast, optimization, profit and Sharpe results.
- `unproven`: any statement about profitability, capacity above 10 MWh, other markets, other periods, or crypto.
- **Single-artefact dependence.** Everything here is read from one preprint PDF; no HTML endpoint was used (the arXiv LaTeXML rendering was not attempted this run) and no second copy was cross-checked beyond the abs page and the API record.
- **Interpretive layers.** The model-major grouping of Figures 9, 10 and 13 is `research-inferred` from a flat text-layer order; it is anchored by seven exact matches against Figure 13's MILP-24 column and by the identity of the three DLENAR rows, but it remains an inference and is labelled as such wherever used.
- **The critique is partly self-referential.** The source argues that profit-based evaluation is unreliable and then reports profits; the record therefore treats the *qualitative* ranking statements as source-reported interpretation, not as validated fact.
- **Publication bias / source quality:** preprint with no peer review, an author employed by an energy trading firm, declared funding, and declared LLM-assisted writing.
- **Incremental-write check:** this capture adds a new family (evaluation-methodology / scoring-rule integrity) that no existing record in this repository covers; it is not an ordinary duplicate of any `day-ahead` or `BESS` record.

## Implementation status

`implementation_status: not-implemented`

Nothing has been implemented in our research stack. No forecast model was fitted, no stochastic program was solved, no `pyomo`/HiGHS run was executed, no market data was downloaded, no dependency was installed, and no third-party code was executed. The checks performed this run are limited to file digests, printed-literal tracing and arithmetic identities on the pinned artefact. This record does **not** imply Qlib full-backtest validation, Paper, Testnet or Live verification of anything.

## Adoption boundary

`status: research-only` | `adoption: not-approved` | `approval_scope: research-only`

The presence of this record in the staging repository means only that normalized research material was pushed. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading.

## Related Wiki records

Three read-only `kb_search` queries were run against Hermes Wiki Brain this run (`day-ahead electricity price forecasting battery arbitrage evaluation` -> 0 pages; `proper scoring rule forecast evaluation` -> 2 pages; `electricity power market trading` -> 1 page). Exactly one result is materially adjacent and is linked with an explicit mechanism distinction:

- `[[quant/prediction-market-proper-betting-accuracy-profit-conversion-2026-09-02]]` -- also asks whether forecast accuracy converts into realised profit, but in CLOB prediction markets with a binary settlement and a fixed tick, i.e. **a different market type, a different signal construction (value-bet sizing rather than battery scheduling) and a different horizon**; it is a retrieval hook, not the same hypothesis. The other two search results (a Polymarket favourite-longshot record and a crude-oil crack-spread record) share only topical words and are deliberately **not** linked. No Wiki page was written this run.

Repository-adjacent records distinguished here (four axes each -- source identity, mechanism, signal construction, universe/stage -- differ in every pair):

1. `bess-day-ahead-ms-ave-probabilistic-profit-ensemble-stopping-rule-2026-09-30.md` (arXiv:2608.26122, Weron & Maciejowska) -- **closest neighbour.** Different source identity; that record captures an ARX + Multiple-Split *profit ensemble with a loss-probability stopping rule* as a tradable decision rule over 2021-2024 German and Spanish products, whereas this record captures a **critique of the evaluation methodology itself** (properness and discriminatory power) over 2015-2023 German products, and it cites `2604.19580` only inside its own literature list.
2. `orderfusion-plus-intraday-electricity-buy-sell-price-trajectory-orderbook-dynamic-mask-2026-09-22.md` -- different source, **intraday order-book trajectory** signal and market stage versus day-ahead auction scheduling; its Hirsch & Ziel citation is the 2024 paper, not this one.
3. `electricity-spread-thief-forecast-reconciliation-bess-arbitrage-2026-09-22.md` -- different source, a reconciliation/steal-of-spread mechanism rather than a scoring-rule integrity claim.
4. `eex-peak-baseload-forward-spread-risk-premium-matrix-har-rcv-2026-09-24.md` and `european-cross-border-day-ahead-power-spread-mean-reversion-2026-09-23.md` -- different source identities, forward/cross-border spread premia rather than evaluation methodology; different horizon, different market stage, different material data dependency.

## Sources

- Simon Hirsch and Florian Ziel, *Probabilistic Forecasting for Day-ahead Electricity Prices, Battery Trading Strategies and the Economic Evaluation of Predictive Accuracy*, arXiv:2604.19580v1 `[q-fin.ST]`, submitted 21 Apr 2026 15:35:32 UTC -- abstract page `https://arxiv.org/abs/2604.19580` (43,338 bytes, SHA-256 `49fc7530e0ab613fde9ff837a114eba5e997a274ef799fac6abea868598e1f44`) and PDF `https://arxiv.org/pdf/2604.19580` (3,907,780 bytes, SHA-256 `0b45efef4c8d1b7de2ee258adb504bf53819b8480fd8183c196a67e2ad0fd4b1`), both fetched 2026-09-30.
- arXiv API record `https://export.arxiv.org/api/query?id_list=2604.19580` (3,314 bytes, SHA-256 `f5bae62416cd817a01177c929134d65cc7a94f82c4807f6132421ce41474ceca`), giving `published` and `updated` both `2026-04-21T15:35:32Z`.
- arXiv licence cell as printed: `http://arxiv.org/licenses/nonexclusive-distrib/1.0/` (the only plain-HTTP URL in this record, preserved literally from the source).
- Works cited *inside* the source (attributed to its own reference list, **not independently read** this run): Uniejewski (2025) *J. Commodity Markets* 39; Uniejewski & Weron (2021) *Energy Economics* 95; O'Connor, Prestwich & Visentin (2024); O'Connor, Bahloul, Rossi, Prestwich & Visentin (2025a) *Energy and AI* 21; O'Connor, Collins, Prestwich & Visentin (2025b) *Energy and AI* 20; Maciejowska, Lipiecki & Uniejewski (2025) arXiv:2511.13616; Lago, Marcjasz, De Schutter & Weron (2021) *Applied Energy* 293; Lipiecki, Uniejewski & Weron (2024) *Energy Economics* 139; Narajewski & Ziel (2022) *Energy Economics* 110; Hirsch, Berrisch & Ziel (2024) arXiv:2407.08750; Hirsch (2025) arXiv:2504.02518; Gneiting & Raftery (2007) *JASA* 102; Diebold & Mariano (2002) *JBES* 20; Fissler, Ziegel & Gneiting (2015) arXiv:1507.00244; Jiao & Vert (2015) ICML; Ziel & Weron (2018) *Energy Economics* 70; Ziel (2018) *JMPSCE* 6; EPEX Spot (2025) trading brochure.
