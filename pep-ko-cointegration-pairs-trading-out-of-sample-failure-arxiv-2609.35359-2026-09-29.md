---
schema: strategy-research-record-v1
title: "PEP/KO Cointegration Pairs Trading with Frozen Parameters: COVID-Concentrated In-Sample Edge, Deflated Sharpe 0.423 over 901 Policies, and Out-of-Sample Failure with Hedge-Ratio Sign Flip (arXiv:2609.35359)"
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equities
  - pairs-trading
  - cointegration
  - engle-granger
  - statistical-arbitrage
  - deflated-sharpe
  - regime-dependence
  - transaction-costs
  - falsification
status: research-only
confidence: medium
source_as_of: 2026-09-28
sources:
  - "https://arxiv.org/abs/2609.35359 - arXiv:2609.35359v1 [q-fin.ST], 'From Cointegration to Out-of-Sample Failure: A Pairs-Trading Case Study on PEP-KO', Davide Graziano (single author); submitted Mon, 28 Sep 2026 15:06:47 UTC (2,297 KB); DOI https://doi.org/10.48550/arXiv.2609.35359 (abs page read 2026-09-29)"
  - "https://arxiv.org/html/2609.35359v1 - pinned primary full text, HTTP 200, 168294 bytes, SHA-256 74e3adddbaaf28b3865856c32863eaad5a440678e57bd7071fbe2a5001dcbeee, read end to end on 2026-09-29 (33535 characters / 463 lines: Abstract, Sections 1-6, Equations (1)-(6), Tables 1-5, Figures 1-4 captions, References)"
  - "https://github.com/Dav1deGraziano/PEP-KO-Pairs-Trading-and-Failure-Analysis - companion code and extended report cited as reference [8] by the paper, pinned at commit c335134ad4b0a08e339cfa35c656187eb2a38eb6 (branch main, 2026-09-28T14:41:27Z; repository created 2026-09-25, last push 2026-09-28T14:41:28Z, 0 stars, 0 forks, not archived); README.md (4291 bytes) read 2026-09-29"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Walk-forward labelled out of sample while sitting inside the stated calibration window: Section 4.2 says the concatenated walk-forward aggregate 'provides evidence of positive performance outside the calibration sample' (J^OOS = 0.64), yet Section 1 and Section 3 define that calibration sample as the 2018-2023 training window, and Section 4.2's own fold definition (two-year rolling training windows T_1=[2018,2020) through T_3=[2020,2022), each followed by a one-year test window) puts all three test years (2020, 2021, 2022) inside 2018-2023. Section 4.3 further shows the only profitable fold is the COVID-19 test year. Left unreconciled; not resolved by the Scout."
  - "Abstract asserts a mechanism the body declines to attribute: the abstract states the results 'show that weakening mean-reversion dynamics in the spread undermine the effectiveness of the strategy out-of-sample', while Section 5 states 'the single-trade sample does not allow a definitive attribution' and Section 6 states 'the small number of trades and the limited power of the test prevent a definitive conclusion'. Both statements stand as printed."
  - "Trade-rate statement inconsistent with the printed trade counts: Section 5 states the 2018-2023 window shows 'roughly 2-3 trades per year outside the COVID window', while Section 3.1 reports 9 round trips over that window and Section 4.3 reports the count falling 9 -> 8 when the COVID window (February-April 2020) is excluded; research-computed rates are 1.50-1.80 trades/year including COVID and 1.39-1.68 trades/year excluding it, under both the 5-year and the 6-calendar-year readings of '2018-2023'. The Section 5 expectation of 5-10 out-of-sample trades inherits this claim. Left unreconciled."
  - "Window boundary ambiguity with possible overlap: the in-sample optimisation window is labelled 2018-2023 (abstract, Sections 1 and 3) and the out-of-sample window is labelled 2023-present (abstract, Section 5), so both labels contain 2023 and no start/end dates are printed for either window. Whether the two windows are disjoint or overlap during 2023 is not stated in source."
---

# PEP/KO Cointegration Pairs Trading with Frozen Parameters: COVID-Concentrated In-Sample Edge, Deflated Sharpe 0.423 over 901 Policies, and Out-of-Sample Failure with Hedge-Ratio Sign Flip (arXiv:2609.35359)

## Provenance

- **Primary source (canonical):** arXiv:2609.35359v1 [q-fin.ST], *"From Cointegration to Out-of-Sample Failure: A Pairs-Trading Case Study on PEP-KO"*, **Davide Graziano** (complete author list exactly as printed on the HTML title block and in the arXiv `citation_author` field: one author, no co-authors beyond this). DOI `10.48550/arXiv.2609.35359`.
- **Version/date:** single version. arXiv submission history `[v1] Mon, 28 Sep 2026 15:06:47 UTC (2,297 KB)`; HTML masthead `arXiv:2609.35359v1 [q-fin.ST] 28 Sep 2026`; `citation_date` `2026/09/28`.
- **Subjects / license:** primary subject `Statistical Finance (q-fin.ST)` only, no cross-list printed; HTML header line `License: CC BY 4.0`.
- **Affiliation / contact:** **no affiliation line and no email address are printed** on the HTML title block (the arXiv submission history shows only the internal `From: Davide Graziano [view email]`) -> `not stated in source`.
- **Publication / preprint status:** no `Comments` field, no journal reference, no publisher DOI, no peer-review statement anywhere in the pinned text -> preprint only, **not peer reviewed as far as the source shows**; publication status `not stated in source`.
- **Pinned primary text:** `https://arxiv.org/html/2609.35359v1`, HTTP 200, **168,294 bytes**, SHA-256 `74e3adddbaaf28b3865856c32863eaad5a440678e57bd7071fbe2a5001dcbeee`, retrieved and **read end to end on 2026-09-29** (33,535 characters / 463 extracted lines covering the Abstract, Sections 1-6, Equations (1)-(6), Tables 1-5, Figures 1-4 captions and the reference list). **The PDF was not downloaded -> PDF bytes and checksum are a `data gap`.**
- **Companion artefact (source-reported, cited by the paper as reference [8]):** `https://github.com/Dav1deGraziano/PEP-KO-Pairs-Trading-and-Failure-Analysis`, pinned at commit **`c335134ad4b0a08e339cfa35c656187eb2a38eb6`** (2026-09-28T14:41:27Z, `main`). Contents at that commit: `Code/Notebook.ipynb` (12,896,657 bytes), `Reports/Report.pdf` (2,518,728 bytes), `Reports/Extended_Report.pdf` (9,291,995 bytes), `README.md` (4,291 bytes), split licence `MIT License (code)` + `CC BY 4.0 License (content)`. **The README (not the paper) is the source of the data-vendor statement recorded below; the notebook and both PDFs were not opened by this Scout -> their internal numbers are `data gap`.**
- **Underlying data (source-reported):** daily **adjusted closing prices** for PEP and KO, "corrected for dividends and stock splits" (paper Remark 1), 2013 to the present. **Vendor is `not stated in source` in the paper** (whole-document scan: `yfinance` 0, `Yahoo` 0, `vendor` 0); the companion README states *"Daily adjusted closing prices for PEP and KO, 2013-present, via `yfinance`"* and lists `yfinance` among the Python requirements.
- **Method dependency (not independent sources):** Augmented Dickey-Fuller (Dickey and Fuller, 1979); Engle-Granger two-step cointegration (Engle and Granger, 1987) with adjusted critical values; Deflated Sharpe Ratio (Bailey and Lopez de Prado, 2014); Adjusted Sharpe Ratio via the Pezier-White adjustment (Pezier and White, 2008); Kalman (1960); Gatev, Goetzmann and Rouwenhorst (2006); Do and Faff (2010); Elliott, van der Malde and Malcolm (2005); Vidyamurthy (2004); Zhang (2020, arXiv:2005.09794).
- **Source-quality classification:** single-author academic preprint with Problem Formulation, Methods, Robustness, Out-of-Sample and Conclusion sections read directly from the pinned HTML; no secondary summary, snippet or model-generated abstract was used to fill any field.
- **What this record is not:** it is **not** a record of a profitable strategy. The source's own conclusion is that "the evidence presented in this paper provides limited support for this proposition" (Section 6).

## Economic mechanism

### Source-reported

- The source frames pairs trading as a **market-neutral relative-value strategy that exploits temporary mispricings between economically related securities**, with cointegration as its statistical foundation: two individually `I(1)` log-prices may have a stationary linear combination, so deviations from the estimated long-run relationship are expected to reverse (Section 1).
- For PEP and KO specifically the source notes the pair is "a commonly studied economically related pair" (both in the global beverage industry, similar price dynamics) but that existing evidence finds their cointegrating relationship "may be weak and period-dependent" (Section 1, citing Cui and Cui, 2012), which is exactly the fragility the paper then tests.
- Source-reported statistical basis (Section 2): both log-price series are `I(1)` (ADF fails to reject the unit root at 5% on levels, rejects strongly on returns); the Engle-Granger procedure with adjusted critical values rejects no cointegration at 5% (**p = 0.033**) over **2013-2018**; the fitted spread is an `AR(1)` with `rho_u = 0.9785`, equilibrium level `m = 0.0037` ("effectively zero"), mean-reversion speed `kappa = 1 - rho_u = 0.0215` and an implied **half-life of approximately 31.9 trading days**.
- Source-reported causal story for the failure (abstract and Section 6): **"weakening mean-reversion dynamics in the spread undermine the effectiveness of the strategy out-of-sample"**, i.e. the relationship that justified the rule decays rather than the rule being mis-implemented; Section 6 generalises this to "a statistically significant and economically plausible cointegrating relationship within one estimation regime does not imply that its trading dynamics will remain stable out of sample".
- The source deliberately separates three layers (Section 1): **statistical parameters** (`alpha`, `beta`, `m`, `sigma_u`, estimated on 2013-2018 and frozen), **trading parameters** (`c`, `w`, `N_max`, `L`, fixed ex ante) and the **policy thresholds** `theta = (z_entry, z_exit)` optimised on 2018-2023 and never re-optimised out of sample.

### Research interpretation

- **Hypothesis in falsifiable form (Scout framing):** on a canonical, economically linked US large-cap pair, an Engle-Granger cointegration spread standardised into a z-score carries a **persistent, cost-survivable mean-reversion premium** that is stable across volatility regimes and hedge-ratio drift, so a threshold rule calibrated in one window remains net-positive in a later, untouched window.
- **Component roles (hybrid structure):**
  - Regime / statistical layer: ADF + Engle-Granger + `AR(1)` spread characterisation on 2013-2018, supplying `beta`, `m`, `sigma_u`.
  - Primary signal: z-score threshold crossing on the standardised frozen spread (`z_entry` up, `z_exit` down).
  - Sizing / risk: volatility-scaled dollar notional with a 0.5% risk budget and a 25% exposure cap (risk management, **not** alpha).
  - Execution cost: flat `c = 0.20%` of traded notional charged per leg on entry and on exit, deducted from equity inside the objective.
  - Validation layer: parameter sensitivity, 3-fold walk-forward, COVID-window exclusion, Adjusted and Deflated Sharpe Ratios.
- **Falsifiable reading of the source's own result:** the mechanism **failed** in the source's own out-of-sample window - the hedge ratio flipped sign (`1.6618` -> `-0.2376`), the post-hoc Engle-Granger test no longer rejects no cointegration (`p = 0.12`), and both adaptive-hedge variants still lost money. Any claim that this pair offers a durable premium is therefore **`unproven` and currently contradicted by the source**.
- **Friction assumed by the mechanism (stated, not measured):** the rule requires shorting one leg and going long the other on a daily close signal, with a round-trip cost of four `c` applications (two legs x entry/exit). Borrow availability, dividend leakage on the short leg, bid-ask spread, slippage and fill timing are **not priced anywhere in the source** (see Execution assumptions).
- **Not a new premium:** this is a **representation/validation claim about an established statistical-arbitrage mechanism**, not the discovery of a new risk factor.

## Signal

All items below are **source-reported** unless explicitly marked `research-proposed` or `research-defined`.

- **Formation timestamp:** `z_t` is formed from daily **adjusted closing prices** at `t`, using the frozen equilibrium level `m` and spread standard deviation `sigma_u` estimated on 2013-2018 (Equation 4). Signal-to-order timing, timezone, exchange session convention and whether the position is taken at the close of `t`, at the next open, or at some later reference price are **`not stated in source`** -> `data gap`.
- **Lookback:** statistical layer uses 2013-2018 daily data (ADF with AIC-selected lag order; Engle-Granger; `AR(1)` on the residual spread). Volatility scaling uses a trailing window of `L = 64` trading days of `Delta z_t` "up to `t-1` to avoid look-ahead" (Section 3, Equation 5). The adaptive diagnostics use `M = 504` days (rolling OLS) or a random-walk state (Kalman).
- **Long entry:** `z_t < -z_entry` -> enter the long-spread position (long one unit of PEP, short `beta_hat` units of KO; signs as printed for the opposite case in Section 3).
- **Short entry:** `z_t > z_entry` -> enter the short-spread position (short one unit of PEP, long `beta_hat` units of KO).
- **Exit:** close the position once `|z_t| < z_exit` (Section 3). **No stop-loss, no take-profit and no maximum holding period exist anywhere in the source** (whole-document scan; the out-of-sample trade is in fact "force-liquidate[d] ... at the end, as the exit threshold `z_exit` is never crossed", Section 5).
- **Holding period / re-entry:** maximum holding period `not stated in source`; expected holding is implied by the 31.9-day half-life and `L = 64`. Re-entry after an exit is not discussed explicitly -> `underspecified` (implicitly the same rule re-triggers on the next threshold cross).
- **Parameters (all source-reported):** `w = 0.5%` risk budget; `N_max = 25%` maximum fraction of equity; `c = 0.20%` transaction cost per leg per side; `L = 64` trading days (chosen as "approximately twice the mean-reversion half-life"); `C_0 = $100,000` initial capital; statistical parameters `alpha_hat = -1.409`, `beta_hat = 1.662` (printed as `1.6618` in Section 5), `m_hat = 0.0037`, `sigma_u` frozen from 2013-2018.
- **Position sizing (Equation 5):** `N_t = C_t * min( w / (sigma_u * sigma_Delta_z^L), N_max )`; share counts `S_PEP = N_t / P_PEP` and `S_KO = -beta_hat * N_t / P_KO` with signs reversed for the short-spread position. `sigma_u` and `sigma_Delta_z^L` are **never printed**, so no position size can be reconstructed from the paper -> `data gap`.
- **Optimisation objective (Equation 6):** `theta_star in argmax J(theta)` with `J = mu_Pi / sigma_Pi * sqrt(252)` on the daily return on capital `Pi_t`, over "a predefined grid of candidate policies `Theta`"; the selected policy is `theta_star = (2.15, 0.50)`. **The grid values and ranges are never printed**; only the candidate count `N = 901` appears (Sections 4.4 and 6) -> `underspecified`.
- **Cost handling inside the rule:** `c` is applied "once on entry and once on exit of each leg" and "deducted directly from `C_t`, so that they enter the objective function directly rather than being a post-hoc adjustment" (Section 3), with the stated rationale that narrower bands trigger more round trips.
- **Frozen out-of-sample rule (Section 5):** statistical parameters `beta_hat`, `alpha_hat`, `m_hat`, `sigma_u` and policy parameters `c`, `w`, `N_max`, `L` are all frozen; only `theta_star = (2.15, 0.50)` is carried forward unmodified.
- **Adaptive diagnostics (Section 5.1, explicitly diagnostic):** rolling OLS re-estimating `(alpha_t, beta_t)` over a trailing `M = 504`-day window, and a Kalman filter treating `beta_t` as a random walk; `z_t` is standardised by trailing `M`-day statistics of the adaptive spread, all quantities use only information up to `t-1`, and `(alpha, beta, mu, sigma)` are frozen at their entry values once a position is open. The source states these variants are "interpreted as diagnostic rather than as evidence of a validated strategy" and are not subjected to walk-forward, sensitivity or ASR/DSR analysis.
- **Not present in the source:** universe construction (the pair is hand-picked), liquidity/volume filters, turnover control, a holding-period cap, leverage or margin rules, short-reachability checks, and any re-calibration schedule. Any such rule introduced downstream is **`research-proposed`**.

## Required data

- **Instrument / universe:** two US common stocks - **PepsiCo (PEP)** and **The Coca-Cola Company (KO)** - chosen as a canonical economically related beverage pair (Section 1). **There is no universe rule, no selection protocol and no survivorship discussion** (the pair is presented as already canonical, citing Zhang 2020) -> `data gap` for any generalisation.
- **Market type / venue / market:** US listed equity cash market; venue not stated; **market type is spot equity only** - no options, no futures, no perps.
- **Timeframe:** daily bars. Statistical window **2013-2018**; policy optimisation window labelled **2018-2023**; walk-forward training windows `T_1 = [2018,2020)` through `T_3 = [2020,2022)` each followed by a one-year test window; out-of-sample window labelled **2023-present**, where "present" is the v1 submission date **2026-09-28** (endpoints not printed - frontmatter contradiction 4).
- **Fields:** adjusted daily closing prices (dividend- and split-adjusted) for both names; log-prices and log-returns derived; **no volume, no open interest, no bid/ask, no borrow, no dividend cash flows, no fundamentals, no corporate-action calendar** are used or required by the source.
- **Point-in-time / availability:** the source does not describe an availability lag, a data-vintage rule or how the adjusted-close series was frozen (a `yfinance` auto-adjusted series downloaded in 2026 back-adjusts earlier history for later dividends and splits) -> `data gap`; train/test boundary handling is described explicitly and carefully (Section 1) for model parameters.
- **Timestamp / timezone:** not stated in source -> `data gap`.
- **Missing data:** not discussed; no imputation rule is described -> `data gap`.
- **Cost/fee fields:** only the flat `c = 0.20%` (swept 0.01%-1.00% in Table 2) is required or used; see Execution assumptions.

## Execution assumptions

Determined from a **Methods-level read of Section 3 (Trading Policy), Section 3.1, Section 4.1 (Sensitivity), Section 4.2-4.4, Section 5 and Section 5.1 of the pinned HTML**, plus a whole-document term census of the 33,535-character extracted text.

- **Cost treatment (source-reported, explicit and material):** the **entire** cost model is a single flat proportional charge `c = 0.20%` of traded notional, applied once on entry and once on exit of **each** leg, deducted from equity inside the optimisation objective (Section 3, Section 3.1). Table 2 sweeps `c` from **0.01% to 1.00%**, reporting `J*` in **0.32-0.77** across that sweep with the optimum threshold pair unchanged only for **0.05% <= c <= 0.50%**.
- **Whole-document cost-term census (Scout-recomputed on the pinned HTML text):** `slippage` **0**; `commission` **0**; `bid-ask` **0**; `borrow` **0**; `short sale`/`short-sell` **0**; `margin` **0**; `leverage` **0**; `latency` **0**; `market impact` **0**; `impact` **0**; `capacity` **0**; `turnover` **0**; `execution` **0**; `fill` **0**; `market order`/`limit order` **0**; `next-day`/`next day` **0**; `liquidity` **0**; `risk-free` **0**; `universe` **0**; `stop` **0**; `dividend` **2** - both in Remark 1, describing why adjusted rather than unadjusted closes are used; `yfinance` **0**, `Yahoo` **0**, `vendor` **0** (vendor appears only in the companion README); `252` **1** (the `sqrt(252)` annualisation in Equation 6); `sharpe ratio` **27**; `deflated` **7**; `901` **3**. Zero occurrences are **zero occurrences of the term**, not evidence that the concept was modelled: order type, fill model, signal-to-order delay, spread, slippage, commission, borrow cost, dividend leakage on the short leg, market impact, position limits, margin/financing, latency, participation and capacity are all `data gap` - **never zero**.
- **Order type / fill model / signal-to-order timing:** not stated in source -> `data gap`. The paper never says whether the `z_t` signal formed on the close of `t` is executed at that close, at the next open, or at a later price.
- **Fees / spread / slippage / impact / capacity:** no model beyond `c`; no fee schedule, no bid-ask treatment, no participation cap, no AUM or capacity reference -> `data gap`.
- **Borrow / shorting:** the rule shorts one leg; locate availability, borrow fees and hard-to-borrow risk are not mentioned -> `data gap`.
- **Dividends:** price returns use dividend-adjusted closes (Remark 1), but **dividends payable on the shorted leg are never charged**, and the treatment of dividends received on the long leg beyond the price adjustment is not stated -> `data gap`.
- **Leverage / margin:** not stated. Research-computed from Equation 5 and the printed share counts: gross notional is `N_t * (1 + beta_hat)` = `2.662 * N_t`, so the 25% `N_max` cap corresponds to roughly **66.6% of equity in gross notional** (labelled **research-computed**, not source-reported).
- **Risk-free rate in `J`:** Equation 6 annualises the raw daily return on capital, implying an implicit zero risk-free rate; the convention is **not stated** -> `data gap`.
- **Failure handling:** no partial-fill, no trade-error and no forced-liquidation rule exists; the out-of-sample position ends only because the sample ends (Section 5).
- **Scout-added assumptions:** **none.** No cost, fill, latency, sizing or liquidity assumption has been introduced by this record.

## Evidence

### Source-reported

Every figure below is third-party, **source-reported**, traced to the pinned HTML, and gross of everything except the flat `c` charge.

**Table 1 - ADF tests, 2013-2018:** `X_PEP` statistic **-1.545**, p **0.511**, 5% CV **-2.864**; `X_KO` **-1.663**, p **0.450**, CV **-2.864**; `r_PEP` **-36.50**, p **<0.001**; `r_KO` **-36.62**, p **<0.001**.

**Section 2 descriptive:** annualised log-return volatility PEP **13.09%**, KO **13.80%**; sample correlation **0.66**.

**Section 2.2 cointegration:** OLS `alpha_hat = -1.409`, `beta_hat = 1.662`; Engle-Granger with adjusted critical values rejects no cointegration at 5% with **p = 0.033**; `AR(1)` spread `rho_u = 0.9785`, `m = 0.0037`, `kappa = 0.0215`, half-life **31.9 trading days**.

**Section 3.1 - in-sample policy optimum (2018-2023):** `theta_star = (z_entry, z_exit) = (2.15, 0.50)`, **9 round-trip trades**, annualised **net Sharpe `J = 0.67`**, **net P&L `$16,941`** on `$100,000`; fixed `w = 0.5%`, `N_max = 25%`, `c = 0.20%`, `L = 64` days.

**Table 2 - sensitivity of `theta_star` to auxiliary parameters:** cost `c` over `0.01-1.00%` -> `theta_star` unchanged for `0.05% <= c <= 0.50%`, `J*` range **0.32-0.77**; risk budget `w` over `0.10-1.00%` -> unchanged for `w >= 0.50%`, `J*` **0.55-0.72**; volatility window `L` over `3-478` days -> unchanged for `L >= 6`, `J*` **0.67-0.72**; exposure `N_max` over `5-100%` -> unchanged for `N_max <= 25%`, `J*` **0.55-0.72**.

**Table 3 - 3-fold walk-forward (two-year train, one-year test, no re-adjustment):** fold 1 `theta = (1.30, 0.65)`, `J = 2.14`, net P&L **`$13,794`**, **12 trades**; fold 2 `(2.15, 0.35)`, `J = -0.07`, **`-$391`**, **1 trade**; fold 3 `(2.00, 0.50)`, `J = -0.50`, **`-$2,796`**, **1 trade**; concatenated aggregate **`J^OOS = 0.64`** (Section 4.2).

**Section 4.3 - COVID-19 exclusion (February-April 2020 removed, pre/post segments reset):** optimiser still picks `(2.15, 0.50)`; trades **9 -> 8**; annualised net Sharpe **0.67 -> 0.28**; net P&L **`$16,941 -> $5,759`**.

**Section 4.4 - selection-bias adjustment (computed on the COVID-excluded sample):** Adjusted Sharpe Ratio **0.281** (raw **0.28**); **Deflated Sharpe Ratio `DSR = 0.423`** against **`N = 901`** zero-skill candidate policies; source's reading: the observed Sharpe "is not statistically distinguishable from the maximum Sharpe ratio that could arise by chance when searching over 901 zero-skill policies".

**Table 4 - out-of-sample 2023-present, all parameters frozen:** `J* = -1.19`, net P&L **`-$28,131`**, **`n = 1`** trade, forced liquidation at the end of the sample because `z_exit` is never crossed; equity declines "almost monotonically from a few weeks after entry"; approximately **`-$28,000` before liquidation**. Re-estimated OOS hedge ratio `beta_OOS = -0.2376` versus analysis-window `1.6618`; post-hoc Engle-Granger on the OOS residuals **fails to reject no cointegration at 5% (`p = 0.12`)**. Source explicitly: the single-trade Sharpe "is not a meaningful estimate of OOS performance".

**Table 5 - adaptive hedge-ratio diagnostics, 2023-present, static `theta_star`:** rolling OLS (`M = 504`) `J* = -1.05`, net P&L **`-$27,163`**, **1 trade**; Kalman filter `J* = -0.88`, net P&L **`-$32,752`**, **5 trades**. `beta_t` under rolling OLS falls from about **1** to about **-0.5** before partially recovering; the strategy is flat for the first 18 months, trades once in mid-2024, and is closed only by forced liquidation. Source's reading: "Allowing the hedge ratio to adapt therefore does not improve OOS performance".

**Figure-only claims (no printed statistics):** Figure 1 in-sample equity curve; Figure 2 walk-forward equity curves per fold; Figure 3 aggregate Sharpe surface over the admissible grid with the COVID window excluded; Figure 4 `beta_t` trajectories for rolling OLS versus Kalman. Any claim resting only on these figures is figure-only evidence -> `data gap` for the underlying series.

### Independently reproduced

not independently reproduced

**Scout arithmetic-only checks (no re-execution of the backtest; script exit 0):**

1. `kappa = 1 - 0.9785 = 0.02150` matches the printed `0.0215`; the implied half-life `ln(2)/0.0215 = 32.24` trading days against the printed **31.9** - a **0.34-day (1.06%)** rounding-level difference, also visible in Section 6 where "half-life approximately 32 days" is printed.
2. Walk-forward P&L additivity: `13,794 - 391 - 2,796 = +10,607`.
3. COVID concentration: `(16,941 - 5,759) / 16,941 = 66.0%` of in-sample net P&L sits in February-April 2020; Sharpe reduction `(0.67 - 0.28) / 0.67 = 58.2%`, consistent with the source's "reduces the Sharpe ratio by more than half".
4. Trade-rate reconstruction behind frontmatter contradiction 3: 9 round trips over "2018-2023" = **1.80/year** (5-year reading) or **1.50/year** (6-calendar-year reading); excluding the 0.25-year COVID window with 8 trades = **1.68/year** or **1.39/year** - none reaches the claimed "2-3 trades per year outside the COVID window".
5. Expected out-of-sample trades at the source's claimed rate would be **5.6-11.2** for a 2023-01-01 start (3.74 years), versus **5-10** as printed; at the reconstructed 1.4-1.8/year rate the expectation is **3.9-6.7**, so the printed 5-10 range is only reachable under the source's own (inconsistent) rate.
6. Out-of-sample loss relative to initial capital: `-28,131 / 100,000 = -28.13%`.
7. Hedge-ratio sign flip confirmed: `1.6620 -> -0.2376`, opposite sign `True`; `sqrt(252) = 15.8745`.
8. ASR `0.281` versus raw `0.28` differs by `0.001` ("essentially unchanged"); `DSR 0.423 < 0.5`, so the source's "not distinguishable from chance" reading is arithmetically supported.
9. `p = 0.033 < 0.05` (in-sample reject) and `p = 0.12 >= 0.05` (OOS non-reject) both behave as printed.
10. **Not reconstructable (data gap):** the walk-forward aggregate `J^OOS = 0.64` cannot be derived from the three fold Sharpes (2.14, -0.07, -0.50) without the concatenated daily return series; the in-sample Sharpe `0.67` cannot be tied to a portfolio volatility because `sigma_u`, `sigma_Delta_z^L` and portfolio volatility are never printed (the printed net P&L implies a CAGR of 3.18% (5-year reading) or 2.64% (6-year reading), consistent with `J = 0.67` only if annualised volatility were 4.75% or 3.94% respectively); the Equation 5 position size and therefore the OOS P&L cannot be reconciled from printed inputs.

### Negative evidence

1. **Source's own statistical verdict:** `DSR = 0.423` over `N = 901` searched policies means the in-sample Sharpe is **not distinguishable from the best of 901 zero-skill strategies** (Section 4.4). This is the paper's headline disqualifier, not a Scout inference.
2. **Regime concentration:** removing February-April 2020 cuts in-sample Sharpe **0.67 -> 0.28** and net P&L **`$16,941 -> $5,759`**, i.e. **66.0%** of the in-sample P&L came from one three-month volatility episode (Section 4.3).
3. **Walk-forward asymmetry:** fold 1 (`J = 2.14`, 12 trades) carries the whole aggregate; folds 2 and 3 have **one trade each** and negative returns (Table 3); fold 1's test year is 2020 - the same COVID regime identified in item 2 - and it lies inside the paper's own 2018-2023 calibration label (frontmatter contradiction 1).
4. **Direct out-of-sample failure:** `J = -1.19`, net P&L **`-$28,131`** (**-28.13%** of initial capital), one trade, forced liquidation (Table 4).
5. **Relationship breakdown:** OOS hedge ratio `beta = -0.2376` versus `1.6618` in the estimation window, and post-hoc Engle-Granger **`p = 0.12`** - no rejection of no cointegration in the tradable window (Section 5).
6. **Adaptive hedging does not repair it:** rolling OLS `J = -1.05` (`-$27,163`, 1 trade) and Kalman `J = -0.88` (`-$32,752`, 5 trades) - the Kalman variant is **worse** than the static rule (Table 5), so hedge-ratio drift alone does not explain the failure.
7. **Power is inadequate by the source's own statement:** 1 out-of-sample trade against an expected 5-10; "too few for any resulting Sharpe ratio to be treated as a reliable performance estimate" (Section 5); the source concedes "the single-trade sample does not allow a definitive attribution".
8. **Unbounded holding period:** the policy has no time exit, so the out-of-sample position is held from "early in the window" to the end of the sample - a structural failure mode of threshold-only pairs rules (Section 5).
9. **Threshold instability across folds:** `(1.30, 0.65)`, `(2.15, 0.35)`, `(2.00, 0.50)` - the source states the calibrated policy "is sensitive to the training period" (Section 4.2).
10. **Cost-model thinness:** a single flat `c = 0.20%` is the only friction; no spread, slippage, borrow, dividend-on-short, impact or latency model exists anywhere (census above), and `J*` varies 0.32-0.77 across the printed cost sweep alone (Table 2).
11. **Dividend asymmetry unpriced:** adjusted closes embed dividends in the price series, but dividends **payable on the shorted leg** are never charged, and the paper's only dividend discussion is Remark 1's price-adjustment rationale.
12. **Execution unspecified:** no order type, no fill price, no signal-to-order delay, no next-day convention (census: all zero) - the reported numbers cannot be read as executable returns.
13. **Reproducibility gaps:** data vendor not stated in the paper (only the companion README says `yfinance`); the 901-candidate grid values are never printed; `sigma_u` and `sigma_Delta_z^L` are never printed; portfolio volatility and the daily return series are not printed; the PDF and the notebook were not opened by this Scout.
14. **Selection-bias correction applied to a subset only:** ASR/DSR are computed on the **COVID-excluded** sample (Section 4.4), so the headline `0.67` figure itself is never deflated.
15. **Breadth:** one hand-picked pair of US mega-cap beverage stocks, one sector, one market, daily frequency, roughly 1.4-1.8 trades per year - no cross-sectional breadth and no cross-market evidence.
16. **No peer review / single author / very fresh:** v1 posted 2026-09-28, one author, no Comments, no journal reference, companion repository created 2026-09-25 with 0 stars and 0 forks.
17. **Adjacent contrary evidence already in this repository (different sources, different universes - stated as context, not as tests of this paper):** `us-etf-pairs-trading-cointegration-cost-viability-falsification-2026-09-13.md` (cost viability anti-correlated with cointegration in liquid US ETF pairs); `pairs-trading-adf-stationarity-filter-walk-forward-falsification-2026-09-12.md` (92 ETF pairs, ADF filter walk-forward null); `sp500-pairs-trading-forensic-falsification-unbounded-beta-kalman-phantom-pnl-2026-09-12.md` (unbounded beta, phantom Kalman P&L, deflated Sharpe); `johansen-cointegration-etf-pairs-friction-asymmetry-falsification-2026-09-12.md` (friction asymmetry); `crypto-pairs-trading-cointegration-overfitting-falsification-2026-09-13.md` (data snooping and OOS falsification in crypto pairs).
18. **Absence caveat:** none identified in the reviewed sources beyond the above; absence is not evidence of no negative result.

## Falsification plan

All thresholds, windows and decision rules below are **`research-defined falsification thresholds`** set by this Scout; none are source-reported. The rule is **no retuning to rescue a failed gate**.

- **F1 - Printed-value reproduction (primary gate).** `research-defined`: run the companion notebook pinned at commit `c335134ad4b0a08e339cfa35c656187eb2a38eb6` and require `theta_star = (2.15, 0.50)`, in-sample `J = 0.67`, net P&L `$16,941`, 9 -> 8 trades with/without COVID, `DSR = 0.423`, `ASR = 0.281`, walk-forward fold rows `(1.30,0.65,2.14,13794,12)`, `(2.15,0.35,-0.07,-391,1)`, `(2.00,0.50,-0.50,-2796,1)`, OOS `(-1.19, -28131, 1)`, `beta_OOS = -0.2376`, OOS EG `p = 0.12`, and Table 5 rows `(-1.05,-27163,1)` / `(-0.88,-32752,5)` within **+/-0.01** on Sharpe and **+/-1 dollar** on P&L. **Fail** on any mismatch; also **fail** if the 901-candidate grid cannot be recovered (currently `underspecified` from the paper alone).
- **F2 - Frozen forward test.** `research-defined`: from **2026-09-29** forward, run the frozen rule on PEP/KO with every parameter pinned; **fail** if net Sharpe over the window is `<= 0`, and treat fewer than **5** round trips as **inconclusive-but-still-failed** (no claim may be revived on a small sample).
- **F3 - Point-in-time multi-pair extension.** `research-defined`: pre-register at least **30** economically linked US equity pairs (selection rule fixed before any return is read), run the identical pipeline, and require a **Benjamini-Hochberg `q < 0.10`** family correction plus `DSR > 0.50` on the best pair. **Fail** if `DSR <= 0.50` or if fewer than **3** pairs survive BH.
- **F4 - Cost ladder with full frictions.** `research-defined`: charge **0 / 5 / 10 / 20 / 50 bps per leg per side** on top of an explicit half-spread and a stated commission schedule. **Fail** at the source's own `c = 0.20%` (20 bps) if net Sharpe `<= 0`, since the entire printed edge sits below 0.7.
- **F5 - Statistical-power gate.** `research-defined`: require at least **30** out-of-sample round trips across the multi-pair panel before any Sharpe or DSR claim is treated as evidence. The single-pair design (1 OOS trade) fails this by construction.
- **F6 - Cointegration-stability gate.** `research-defined`: rolling **3-year** Engle-Granger re-tests on each pair; require rejection of no cointegration at 5% in **>= 70%** of rolling windows over the tradable sample, and require the sign of `beta` to be stable (no sign flip). PEP/KO currently **fails** (OOS `p = 0.12`, `beta` sign flip).
- **F7 - Regime ablation.** `research-defined`: re-run excluding 2020-02-01 to 2020-04-30 and, separately, excluding **every** rolling 3-month window; **fail** if the headline Sharpe drops by more than **30%** relative to full-sample (the source already reports a **58.2%** drop).
- **F8 - Placebo pairing.** `research-defined`: run the identical pipeline on **100** randomly drawn mega-cap pairs matched on correlation decile; **fail** the mechanism claim if the PEP/KO in-sample Sharpe (0.67) or DSR (0.423) does not exceed the **90th percentile** of the placebo distribution.
- **F9 - Adaptive-hedge repair test.** `research-defined`: the rolling-OLS and Kalman variants are the **only** permitted alternatives, pre-registered with no further tuning; **fail** if either is net-negative OOS (currently both are: `-1.05` and `-0.88`). No third estimator may be added after seeing results.
- **F10 - Dividend and borrow-inclusive net.** `research-defined`: charge short-leg dividend payments and a stated borrow fee on top of `c`; **fail** if net Sharpe falls by more than **0.15** versus the printed figure.
- **F11 - Executability gate.** `research-defined`: signal on the close of `t`, fill at the **next session open** with a one-way **5 bps** slippage added; **fail** if net Sharpe `<= 0`. (The source specifies no execution convention - this gate exists to close that `data gap`.)
- **F12 - Window-hygiene gate.** `research-defined`: print explicit disjoint endpoints for the in-sample and out-of-sample windows and re-run; **fail** if any 2023 observation enters both windows (currently unresolved - frontmatter contradiction 4).
- **F13 - Liquidity / capacity gate.** `research-defined`: require both legs to trade at **<= 20% of 20-day ADV** across 5 execution days with modelled market impact; **fail** if the intended notional (up to `2.662 x N_max` of equity, research-computed) is not executable.
- **F14 - Action on failure.** `research-defined`: any **F1** failure => record the reproduction attempt as a contradiction and keep `status: research-only`; **F2/F3/F6** failure => retain this record solely as **negative evidence** with no implementation consideration; **F4/F10/F11** failure => the mechanism may not be proposed for Paper/Testnet at all; all failures together => the record stands as a documented falsification of the PEP/KO cointegration premium. No gate may be rescoped, re-parameterised or re-windowed after results are seen.

## Crypto portability

**Verdict: `adapted` (performance `unproven`).**

- The mechanism - cointegration spread, z-score thresholds, volatility-scaled sizing, flat proportional costs - is **instrument-agnostic mathematics**, so it can be *written* for crypto spot or perpetual pairs without modification.
- The evidence base, however, is **two US large-cap equities, 2013-2026, daily, cash market only**; the source performs **no crypto test**, so this is a **ported hypothesis, not crypto empirical evidence**.
- **What does not port as stated:**
  - **Cointegration itself:** crypto price levels are far less likely to maintain a stationary linear combination; delisting and renames break the pair silently, while the source's pair never delists.
  - **Funding, mark/index price, liquidation:** absent from the source entirely; on perpetuals, funding payments and mark-price liquidation would dominate a rule that holds a position for months (the OOS position was held to forced liquidation).
  - **Borrow / short leg:** crypto borrow rates and hard-to-borrow constraints differ completely and are unpriced in the source.
  - **24/7 sessions and candle boundaries:** "daily close" has no single venue-neutral definition; timezone and session cut-offs must be re-specified (`research-proposed`).
  - **Cost structure:** crypto taker/maker fees plus wider spreads on small caps are large relative to a rule that earns one `sigma_u`-sized reversion; the source's flat 20 bps does not transfer.
  - **Universe construction:** there is no crypto analogue of a canonical, never-delisted mega-cap pair; a point-in-time pair list would be required (see F3).
- **Conclusion:** portability is `adapted`, and crypto performance of the hypothesis is `unproven`. A crypto test would be a new study under the F-gates above, not a re-labelling.

## Limitations

- **`data gap` - execution economics:** order type, fill model, signal-to-order timing, latency, spread, slippage, commission, market impact, capacity, turnover, borrow cost, margin/financing and short-leg dividends are **not stated in source** (census above). They must never be read as "zero".
- **`data gap` - reconstruction inputs:** data vendor (in the paper), `sigma_u`, `sigma_Delta_z^L`, the 901 grid values, portfolio volatility, the daily return series and explicit window endpoints are not printed; PDF and notebook not opened by this Scout.
- **`data gap` - timestamps:** timezone, session convention and price-vintage handling of the adjusted-close series are not stated.
- **`underspecified` - the tradable rule:** entry/exit thresholds are printed, but without the grid, the vol inputs and the execution convention the rule cannot be reproduced from the paper alone; the companion notebook is required.
- **`underspecified` - re-entry, holding cap, re-calibration:** none of these is specified; the strategy provably has no maximum holding period.
- **`not independently reproduced`:** no reproduction by this Scout or by any record in this repository; only the arithmetic checks listed above were performed.
- **`unproven` - tradability:** the source's own conclusion is that the evidence gives "limited support" for an exploitable edge, with `DSR = 0.423` and an out-of-sample loss of `-28.13%` of initial capital.
- **Sample and identification limits:** one pair, one sector, one market, one COVID regime driving 66% of in-sample P&L, 1 out-of-sample trade, walk-forward test years inside the paper's own calibration label, and window endpoints unstated (four frontmatter contradictions).
- **Source-quality limits:** single-author, single-version (v1, 2026-09-28) preprint; no peer review, no Comments, no journal reference, no funding or competing-interest statement; companion repository created three days before submission with 0 stars.
- **Reconciliation limits:** the walk-forward aggregate Sharpe, the Equation 5 sizing and the OOS P&L cannot be rebuilt from printed values (arithmetic checks 5 and 10).

## Implementation status

`implementation_status: not-implemented`.

Nothing has been implemented in our research stack. No pair was formed, no spread was estimated, no backtest was run, and no Qlib, Paper, Testnet or Live stage has been touched. This record is a normalised, source-traceable capture of a single preprint's negative result plus a Scout-authored falsification plan.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record in the repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet or live trading. `confidence: medium` refers only to the fidelity of this **research interpretation** to the pinned source - it is not confidence that the strategy makes money, and it is not authorisation to trade.

## Related Wiki records

Read-only `kb_search` on the Wiki Brain vault (2026-09-29) for `pairs trading cointegration mean reversion` returned **8 pages**, of which the following are materially related and verified by path:

- [[quant/pairs-trading-adf-stationarity-filter-walk-forward-falsification-2026-09-12]] - ADF-stationarity-filter walk-forward null over 92 ETF pairs; same validation family, different source, different universe (ETF cross-section instead of one equity pair).
- [[quant/johansen-cointegration-etf-pairs-friction-asymmetry-falsification-2026-09-12]] - Johansen basket falsification under friction asymmetry; multi-pair basket versus a single two-name pair.
- [[quant/us-etf-pairs-trading-cointegration-cost-viability-falsification-2026-09-13]] - cost-viability versus cointegration anti-correlation in liquid US ETF pairs; FDR-controlled panel versus one hand-picked pair.
- [[quant/crypto-pairs-trading-cointegration-overfitting-falsification-2026-09-13]] - cointegration selection data-snooping and OOS falsification in crypto pairs; different market type and data dependency.
- [[quant/sharpe-deflated-multiple-testing-2026-08-27]] - the Deflated Sharpe / multiple-testing framework record; the DSR machinery used by this paper.
- [[quant/llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04]] - search-aware deflated evaluation of discovered strategies; adjacent methodology for the 901-policy search.

A `kb_search` for `deflated Sharpe ratio backtest overfitting selection bias` returned the same cluster plus the pages above; **no Wiki page about PEP/KO, Engle-Granger on single equity pairs, or arXiv:2609.35359 exists**, so no such link was fabricated.

Adjacent records in **this repository** (source identity differs in every pair; four-axis distinction stated):

- `sp500-pairs-trading-forensic-falsification-unbounded-beta-kalman-phantom-pnl-2026-09-12.md` - closest neighbour: also cointegration pairs with a Kalman hedge ratio, deflated Sharpe and a falsification verdict. **Distinct source** (`github.com/Duyanh090205/pairs-trading-engine` commit `30311352...`), **distinct mechanism focus** (look-ahead bias injection, unbounded beta and phantom P&L in a multi-pair live paper engine), **distinct universe** (S&P 500 pairs, not a single beverage pair), **distinct evidence type** (engine forensics rather than a frozen-parameter OOS test with an EG re-test).
- `tether-pairs-trading-fdr-kalman-half-life-net-beta-2026-09-12.md` - relative-value pairs with FDR control and short-borrow handling; different market type (crypto stablecoin), different data dependency (funding/venue data), and it is the only pre-existing record that mentions both PEP and KO names (as generic examples), not this source.
- `ewy-samsung-sk-hynix-three-leg-pairs-stat-arb-stock-perpetual-2026-09-12.md` - three-leg equity/perpetual relative value; different instrument structure (three legs, cross-market), different universe (Korea/US listing pair), different horizon.
- `crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11.md` - Kalman cointegration falsification on perpetuals; different market type, funding and liquidation dependencies absent from this source.
- `commodity-soybean-crush-spread-cointegration-stat-arb-2026-09-12.md` - cointegration on a commodity crush spread; different mechanism (processing-margin spread, not two equities) and different data dependency.

## Sources

1. Graziano, Davide. *"From Cointegration to Out-of-Sample Failure: A Pairs-Trading Case Study on PEP-KO"*. arXiv:2609.35359v1 [q-fin.ST], submitted Mon, 28 Sep 2026 15:06:47 UTC. `https://arxiv.org/abs/2609.35359` | DOI `https://doi.org/10.48550/arXiv.2609.35359`.
2. Pinned primary full text: `https://arxiv.org/html/2609.35359v1` - HTTP 200, **168,294 bytes**, SHA-256 `74e3adddbaaf28b3865856c32863eaad5a440678e57bd7071fbe2a5001dcbeee`, retrieved and read end to end **2026-09-29** (33,535 characters / 463 lines: Abstract, Sections 1-6, Equations (1)-(6), Tables 1-5, Figures 1-4 captions, References). **All normalised numbers in this record were located in this HTML.**
3. Companion artefact (source-reported, cited as reference [8] by the paper): `https://github.com/Dav1deGraziano/PEP-KO-Pairs-Trading-and-Failure-Analysis`, commit **`c335134ad4b0a08e339cfa35c656187eb2a38eb6`** (2026-09-28T14:41:27Z) - `README.md` read 2026-09-29 (source of the `yfinance` data statement and the MIT / CC BY 4.0 split licence); `Code/Notebook.ipynb`, `Reports/Report.pdf` and `Reports/Extended_Report.pdf` **not opened by this Scout** -> `data gap`.
4. Methods referenced **by the source** and not independently read for claims in this record: Dickey and Fuller (1979); Engle and Granger (1987); Bailey and Lopez de Prado (2014, *Journal of Portfolio Management* 40.5, 94-107); Pezier and White (2008); Kalman (1960); Gatev, Goetzmann and Rouwenhorst (2006, *Review of Financial Studies* 19.3); Do and Faff (2010, *Financial Analysts Journal* 66.4); Elliott, van der Malde and Malcolm (2005, *Quantitative Finance* 5.3); Vidyamurthy (2004); Cui and Cui (2012, *Open Journal of Statistics* 2.5); Zhang (2020, arXiv:2005.09794).

**Status literals:** `research-only` | `not-implemented` | `not-approved` | `approval_scope: research-only` | `not independently reproduced`.
