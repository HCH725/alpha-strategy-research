---
schema: strategy-research-record-v1
title: "Reviving Anomalies: Dependent Double Sort of 153 JKP Characteristics on ML Expected Net Returns (NN forecast − scale-dependent price impact) with 1/N Investment across Fund Sizes"
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional
  - anomaly-selection
  - machine-learning
  - expected-returns
  - transaction-costs
  - us-equity
  - mutual-funds
status: research-only
confidence: medium
source_as_of: "2026-03-25"
sources:
  - "Heiner Beckmeyer, Florian Berg, Timo Wiedemann, Jonas Wortmann, 'Reviving Anomalies', MIT Sloan Research Paper No. 7378-26, SSRN abstract 6468806, DOI 10.2139/ssrn.6468806; date written 25 Mar 2026, posted 26 Mar 2026, landing shows last revised 23 Jun 2026; retrieved PDF version dated March 25, 2026. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6468806"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Reviving Anomalies: Dependent Double Sort of 153 JKP Characteristics on ML Expected Net Returns (NN forecast − scale-dependent price impact) with 1/N Investment across Fund Sizes

## Provenance

- **Primary source (landing + full 30-page PDF read this run):** Heiner Beckmeyer, Florian Berg, Timo Wiedemann, Jonas Wortmann, *"Reviving Anomalies."* SSRN abstract ID **6468806**, DOI **10.2139/ssrn.6468806**, **MIT Sloan Research Paper No. 7378-26**. Landing: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6468806 (30 pages; posted 26 Mar 2026; last revised 23 Jun 2026; date written 25 Mar 2026). PDF delivery URL: https://papers.ssrn.com/sol3/Delivery.cfm/6468806.pdf?abstractid=6468806&mirid=1&type=2
- **Author list exactly as the primary PDF title page:** *Heiner Beckmeyer, Florian Berg, Timo Wiedemann, Jonas Wortmann*. Title-page affiliations: University of Münster (Beckmeyer); Massachusetts Institute of Technology (Berg); University of Münster – Finance Center Münster / University of Potsdam (Wiedemann); University of Münster (Wortmann). The SSRN landing lists the same four names in the same order.
- **Pinned version / checksum (measured 2026-09-23):** the PDF was fetched inside a real browser session after clearing SSRN's Cloudflare interstitial, **539,504 bytes**, **SHA-256 `35abeaa5710f97fcb3bcf7e68eae48a7f32e75b84fbe414e053c5c3b170525f4`**. Embedded metadata: `/CreationDate D:20260325145439Z`, `/Producer pdfTeX-1.40.26`, `/Creator LaTeX with hyperref`. Title page states **"This version: March 25, 2026"**, matching the landing's date-written field. **Version caveat:** the landing page says "Last revised: 23 Jun 2026", but the currently downloadable PDF is byte-identical to a 25 Mar 2026 build → any June revision is **`data gap`** (not verified); this record pins the March 25, 2026 PDF. All 30 pages were text-extracted and read (Abstract, §1–§6, Tables 1–8, Figures 1–5 captions, References, Appendix A–B).
- **Sample period verified from the primary PDF (§3, Table 1/2/3 captions):** **testing/out-of-sample sample = January 2004 – December 2023 (20 years)**; the first neural-network model is trained on the preceding **23 years starting January 1980** (§2, Expected Returns). The overall start of the underlying characteristic panel before 1980 is `not stated in source`.
- **Universe verified from the primary PDF:** U.S. equities; the 153 characteristic-based anomalies and their sort directions come from **Jensen, Kelly & Pedersen (2023)**, constructed from **CRSP and Compustat** (§2 and footnote 2; §4). Fund-level analysis uses the **CRSP Mutual Fund Database**: after filters (equity share ≥ 50% of holdings matched to the JKP sample, ≥ 10 matched stocks) **4,597 funds remain in 2023** (Appendix A). Stock-level inclusion rules beyond the JKP dataset (price/size/listing/delisting filters, breakpoint exchange) are **`not stated in source`** → `data gap`.
- **Transaction-cost treatment verified from the primary PDF Methods (§2, "Transaction Costs", Eq. 5–6):** costs **are modeled** — a quadratic dollar price-impact term `TC_{t,i} = ½ τ'_t Λ_{i,t} τ_t` with `Λ_{i,t} = 0.2 / V_{i,t}`, `V` = expected daily dollar volume proxied by the **trailing six-month average daily dollar volume**, calibrated to **Frazzini, Israel & Moskowitz (2018)** (trading 1% of daily dollar volume moves price ≈0.1%). Everything reported as "net" is gross return **minus price impact only**: full-text scan finds **no commission, no bid-ask-spread term, no borrow/short fee, no slippage model beyond impact, no fill model** applied to returns (bid-ask spreads and effective spreads appear only when citing Edelen et al. 2007 and Chen & Velikov 2023) → each of those is `not stated in source`. How the trade-size vector `τ_t` is derived from the portfolios' actual rebalancing trades is **not specified** → `data gap`.
- **Core performance numbers:** every quantitative claim below is traced to a named table/section of the pinned PDF (Table 1, Table 2, Table 3, Table 4, Table 5, Table 6, Table 7, Table 8, Figure 1, Figure 2, Figure 3, Figure 4, Figure 5, §1–§6, Appendix A/B). No figure comes from a secondary summary. Table 1 cells were cross-validated against the §1/§3 prose (micro 18% / small 14% / large 9% and Sharpe 0.75 / 0.71 / 0.62 for the E[r]-&-TC block; the E[r]-adjusted 1600m cell is empty because N = 0).
- **Publication status:** SSRN working paper / MIT Sloan Research Paper Series. **No journal acceptance, forthcoming notice, peer-review statement, or non-SSRN DOI appears in the PDF or on the landing page** → `not stated in source`. No code/replication-package statement appears in the PDF → `not stated in source`. SSRN license on the landing page: "No reuse allowed without permission" → this record normalizes and cites rather than reproduces the work.
- **Pre-write deterministic dedup (2026-09-23, ripgrep across ALL `*.md` in this repository, not `git log`):** `6468806`, `Reviving Anomal`, `Beckmeyer`, `Wiedemann`, `Wortmann`, `anomaly alignment`, `implementable anomal`, `153 characteristic`, `implementable efficient frontier`, `scale-dependent price impact` → **zero records carry this source identity**. The single hit for `6468806` is the dedup note inside `daily-return-information-factor-drif-elastic-net-cross-sectional-2026-09-23.md`, which records this candidate as *deferred under the hard cap* — a mention, not a capture. Adjacent records checked and kept distinct: `daily-return-information-factor-drif-elastic-net-cross-sectional-2026-09-23.md` (Cakici et al. single-signal elastic-net DRIF over 21 daily returns — different paper, different signal), `anomaly-pre-release-drift-predicted-signal-decile-portfolios-2026-09-23.md` (pre-release drift timing of predicted anomalies), `china-ashare-factor-library-overfitting-audit-amihud-illiquidity-falsification-2026-09-13.md` / `us-equity-microstructure-ensemble-lightgbm-fdr-falsification-2026-09-13.md` (multiple-testing audits of different sources), `cross-sectional-equity-ridge-percentile-rank-alpha-2026-09-03.md` and `alphaforge-generative-formulaic-alpha-dynamic-factor-timing-2026-09-17.md` (other ML factor constructions, different sources). **Genuinely new source identity and new mechanism family: ML-expected-return-and-cost-conditioned selection of classic anomaly portfolios, validated on mutual-fund behavior.**

## Economic mechanism

### Source-reported

The authors start from the literature's negative finding — most classic anomalies (size, value, momentum, …) stopped delivering significant returns after ~2003 and, more damningly, fail to survive implementation costs (Green, Hand & Zhang 2017; Chen & Velikov 2023; DeMiguel et al. 2020) — and argue the fix is not to abandon anomalies but to **select within them** (§1, §6):

- **Expected-return conditioning:** each anomaly's extreme quintile contains stocks that are extreme on the characteristic but heterogeneous on forward returns; conditioning the long leg on the highest machine-learning expected return (and the short leg on the lowest) concentrates capital where signal and forecast agree (§2).
- **Scale-dependent price impact:** implementability is a property of **fund size**, not of the signal alone — cost is convex in trade size and inversely proportional to dollar volume (Eq. 5–6, following Jensen et al. 2025 and Frazzini et al. 2018), so the same anomaly is tradable for a 40m USD fund and dead for a 1.6bn USD fund (§1, §3).
- **Joint condition:** sorting on **expected net return** = NN gross forecast − modeled impact identifies *implementable anomalies* (ex ante positive expected net return), and a plain **1/N** allocation across those implements the idea (§3, Table 3).
- **Behavioral confirmation:** mutual funds are claimed to tilt holdings toward implementable anomalies and away from non-implementable ones, and the tilt predicts higher subsequent net fund returns (§4, Tables 4–6) — i.e. the mechanism is asserted to be economically used by real institutions.

### Research interpretation

Falsifiable form: **the cross-section of next-month U.S. equity returns contains enough independent information in a 153-characteristic ML forecast that, when used as the second stage of a dependent quintile sort on a classic anomaly, it raises the number of cost-surviving anomalies and the 1/N out-of-sample Sharpe — and the improvement must come from the forecast layer, not from extra portfolio concentration or from post-hoc selection.** Component roles (per README hybrid structure): **no regime filter and no exit/stop logic exist in the source** — Signal = (i) first-stage anomaly quintile sort, (ii) second-stage sort on `E[r] − E[TC]`; Portfolio = value-weighted long top-top cell / short bottom-bottom cell, or 1/N across anomalies whose expected net return > 0. The price-impact term is a **cost model, not an alpha signal** (README rule 8): it changes *which* anomalies are selected, not the direction of the return forecast. Do not assume each layer contributes: the source supplies the E[r]-only ablation (Table 1) but **not** a TC-only ablation, and supplies a concentration control (Figure 5) but not a shuffled-forecast placebo.

## Signal

All items below are source-reported unless explicitly labeled `research-proposed` / `underspecified` / `data gap`.

- **Formation timestamp:** portfolios are formed **each month at time t** and earn `t+1` returns (Eq. 1–2); the expected-return model is **re-estimated once per year, at end-December, using information through that December, and held fixed for the next year** (§2). The exact calendar day and timezone of formation/execution are `not stated in source`.
- **Lookback / training window:** first model trained on **January 1980 → December 2003** (23 years, first OOS month = January 2004); expanding training thereafter; **70%/30% train/validation split by months**, **50 trials**, final prediction = **equal-weighted ensemble of the five best models** (§2).
- **First stage (§2):** value-weighted quintile sort on characteristic `c`, for each of the **153 JKP (Jensen–Kelly–Pedersen 2023) characteristics**, keeping each original study's sort direction (footnote 2).
- **Second stage (§2, Eq. 3–4):** within **each** first-stage quintile, re-sort stocks by `E_t[r_net,i,t+1] = f(c_i,t) − E_t[TC]` into quintiles (dependent double sort → 25 portfolios). `f(·)` = feed-forward neural network, **three hidden layers, pyramidal layering, Gu–Kelly–Xiu (2020)** specification; `E_t[TC]` = quadratic impact from Eq. 5–6 **evaluated at the fund size under consideration** (40 / 200 / 500 / 1600 m USD, measured Dec 2023 and discounted back in time at the market return, §3).
- **Long entry:** value-weighted portfolio of the **highest-characteristic ∩ highest-expected-net-return** cell. **Short entry:** value-weighted portfolio of the **lowest-characteristic ∩ lowest-expected-net-return** cell (Eq. 2). Sort ties, breakpoint exchange, and minimum cell size are `not stated in source` → `underspecified`.
- **Ex ante selection (Figure 3, §3):** an anomaly is *implementable* in month t if its expected **net** (post-impact) return over the next month is positive; no significance test is applied in this ex ante step (the source says so explicitly).
- **Portfolio across anomalies (Table 3):** **1/N equally weighted across all implementable anomalies** in that month for the fund size considered; the 1/N baseline is chosen because beating it is hard (DeMiguel et al. 2009) and **optimization across the achievable set is explicitly left to future research** (§3, §6).
- **Holding period / rebalance:** **one month**, overlapping positions do not apply; within-month adjustment `not stated in source`.
- **Reported portfolio statistics basis:** value-weighted; "net" = gross return minus **modeled price impact only** (Table 1/3 captions); significance = **positive net return at the 5% level over 2004–2023** (Table 1/2 captions).
- **Mutual-fund layer (§4, not part of the tradable signal):** *anomaly alignment* = Σ fund weight × (+1 long leg / −1 short leg / 0) on each target portfolio, computed over a **grid of 100 fund sizes** with each fund assigned the nearest grid point; funds restricted to equity share ≥ 50% matched and ≥ 10 matched stocks.
- `research-proposed` (not in source): any entry threshold, stop, take-profit, volatility target, liquidity/participation cap, position limit, venue, rebalance clock other than month-end, long-only/long-short variant selection, and any crypto universe.
- `data gap`: **strategy turnover is never reported**; **how the trade-size vector τ_t is computed from the rebalance is not specified**; the source reports no fill model, no execution timing, and no short-borrow feasibility for the short leg.

## Required data

- **Instrument / universe:** U.S. common stocks in the JKP 153-characteristic panel (CRSP/Compustat); **not crypto**. Stock-level filters `not stated in source` → `data gap`.
- **Venue / data vendor:** CRSP + Compustat (characteristics per Jensen, Kelly & Pedersen 2023); **CRSP Mutual Fund Database** (fund sizes, quarterly holdings); all proprietary → reproduction requires WRDS-class access (`data gap`: no data vintage or code version pinned).
- **Market type / timeframe:** equity cash market; **monthly** portfolio formation; daily dollar volume series for the cost model.
- **Fields used:** 153 firm characteristics (value, momentum, quality, investment, profitability, leverage, accruals, debt issuance, size, low risk, skewness, seasonality, profit growth — the 13 JKP themes, Table 2); monthly returns; **trailing 6-month average daily dollar volume** (cost model); market returns (to discount fund sizes back in time); fund-level: MTNA, management fee, expense ratio, turnover ratio, equity share, monthly fund returns (Appendix B, Tables 5–8).
- **Point-in-time / availability:** expected-return model re-fit each December on data through that December and applied to the next year (§2) — the source labels 2004–2023 out-of-sample; fund holdings enter with their own reporting lag (`underspecified`: lag/staleness of CRSP holdings is not discussed).
- **Timestamp / timezone:** `not stated in source`.
- **Missing data:** `not stated in source` — no explicit imputation or stale-value rule beyond the source datasets' own construction (`data gap`).
- **Funding/fee/spread needs:** no funding (equity); the signal itself needs no data on fees, but tradability assessment needs commissions, spread, borrow fee and slippage — **none are provided by the source** (`not stated in source`; see Execution assumptions).

## Execution assumptions

- **Signal-to-order timing:** month-t formation → month t+1 return; **no execution lag, order type, or fill model is specified** → `not stated in source`.
- **Fees, spread, slippage, impact:** the only modeled cost is **quadratic price impact** (Eq. 5–6, Frazzini et al. 2018 calibration, cost split equally between buyer and seller). **Commissions, bid-ask spread, explicit slippage, market-impact beyond the quadratic term, and any fill/partial-fill model are absent** → `not stated in source`. Reported "net" returns must therefore be read as **net of modeled price impact only** (Scout reading, consistent with every Table 1/3 caption).
- **Turnover / capacity:** **turnover is not reported anywhere in the pinned PDF** → `data gap`; consequently the implied dollar trading volume, participation rate and capacity of the 1/N strategy cannot be checked against the impact calibration.
- **Borrow / shorting:** the short leg of every anomaly is assumed available; **no borrow fee, availability, recall or shorting-constraint model** → `not stated in source`.
- **Leverage / margin:** `not stated in source`; the strategy is presented as a self-financed long–short overlay, with fund-size-dependent costs, and negative market beta is reported (Table 3, β from −0.255 to −0.480).
- **Fund-size assumption:** the four AUM levels are **2023 CRSP percentiles (≈20th/40th/60th/80th)** discounted back at the market return — a modeling convention for cost scaling, not an observed historical AUM path (§3).
- **Distinguish source vs Scout:** everything Scout adds (extra cost rungs, liquidity caps, lag tests) appears only in the Falsification plan and is labeled `research-proposed` / `research-defined`.

## Evidence

### Source-reported

All figures below are **source-reported, not independently verified**, from the pinned March 25, 2026 PDF; sample 2004–2023; value-weighted; "net" = minus modeled price impact only; significance at the 5% level unless noted. Fund sizes in million USD (40 / 200 / 500 / 1600).

- **Table 1 (ex post counts and averages of anomalies with significant positive net returns):** Unadjusted **N = 17 / 10 / 3 / 1**, net return **0.08 / 0.08 / 0.07 / 0.06**, Sharpe **0.57 / 0.60 / 0.62 / 0.59**, MaxDD **−0.32 / −0.34 / −0.26 / −0.31**. E[r]-adjusted **N = 126 / 73 / 9 / (1600: empty, N = 0)**, net return **0.21 / 0.18 / 0.16**, Sharpe **0.82 / 0.70 / 0.57**, MaxDD **−0.55 / −0.58 / −0.60**. E[r]-&-TC-adjusted **N = 126 / 101 / 81 / 41**, net return **0.18 / 0.14 / 0.11 / 0.09**, Sharpe **0.75 / 0.71 / 0.68 / 0.62**, MaxDD **−0.51 / −0.44 / −0.39 / −0.34** (values cross-checked against §1 and §3 prose: "101 significant anomalies with net returns of 14% and a Sharpe ratio of 0.71"; "18% per year for a micro fund, decreasing to 9% per year for a large fund"; "0.75 and 0.68").
- **Figure 1 (gross improvement of E[r]-adjusted over plain HML, by JKP theme):** average annualized gross improvement **+12.5% (seasonality) to +22% (size, low risk)**; mean t-statistics of the improvement **2.3 (seasonality) to > 6 (size)** — the source notes many exceed Harvey–Liu–Zhu's (2015) threshold of 3.
- **Table 2 (theme × fund-size counts):** quality is the most revived theme (**15 / 15 / 16 / 13** of 17 for E[r]-&-TC across 40/200/500/1600), followed by investment, momentum (**8 / 8 / 4 / 1** of 8), accruals (**5 / 4 / 4 / 4** of 5); **size: 1 / 0 / 0 / 0** of 5 and **value: 12 / 5 / 1 / 0** of 13 for large funds — size and value are effectively not revived for small-to-large funds.
- **Figure 2:** number of significant anomalies rises steeply with fund size adjustment; **above ≈200m USD the TC adjustment becomes as important as the expected-return adjustment** (§3).
- **Figure 3 (ex ante implementable anomalies per month):** **> 140** for micro-to-medium funds with minor fluctuations; for 1600m USD funds **120–140 until 2016, declining thereafter, with a further drop in 2023**.
- **Table 3 (20-year out-of-sample 1/N in implementable anomalies, net):** fund 40 → net return **0.160**, σ 0.158, **Sharpe 1.010**, MaxDD **−0.344**, CAPM **α 0.203\*\*\***, **β −0.480**; fund 200 → **0.120**, 0.133, **0.904**, −0.303, **α 0.155\*\*\***, β −0.388; fund 500 → **0.092**, 0.108, **0.851**, −0.278, **α 0.120\*\*\***, β −0.314; fund 1600 → **0.054**, 0.085, **0.639**, −0.247, **α 0.077\*\*\***, β −0.255. (Abstract: "Sharpe ratios between 0.64 and 1.01".)
- **Table 4 (anomaly-alignment panel):** implementable-minus-non-implementable alignment **0.053 (no FE) / 0.109 (time FE) / 0.120 (time+fund FE)**, all \*\*\*; standard errors clustered by time and entity.
- **Table 5 (cross-sectional fund returns on alignment):** implementable **0.054\*\*\* (no controls) / 0.062\*\*\* (with controls)**; non-implementable **0.001 / −0.011 (insignificant)**. With IQR = 0.114: **+0.62 / +0.71 pp per month → +7.39 / +8.48 pp per year** (§4, footnote 5).
- **Table 6 (predictive panel, lagged alignment):** implementable **0.037\*\*\* / 0.044\*\*\*** → **+0.42 / +0.50 pp per month → +5.06 / +6.02 pp per year**; non-implementable **0.006 / 0.014 (insignificant)**.
- **Tables 7–8 (management fees):** implementable alignment has **no significant effect** on fees; non-implementable alignment is associated with **lower** fees — cross-sectional **−0.12 pp (no controls) / −0.08 pp (controls)** per IQR and panel **−0.10 pp / −0.05 pp** per IQR, against a full-sample mean annualized fee of **0.44%** (§4, Tables 7–8, Appendix B).
- **Robustness (§5):** PCA of anomaly returns — first component's explained variance rises **≈40% → ≈50%** after E[r] adjustment while the first two components are unchanged and higher-order components diverge → the adjusted anomalies span **more heterogeneous** opportunities (Figure 4). Concentration control — the ML-augmented portfolio outperforms a plain characteristic sort split into **5 / 10 / 15 / 20 / 25** portfolios by a substantial margin, including the most concentrated single sorts (Figure 5).
- **Fund-sample description (Appendix A/B):** 4,597 funds in 2023 after filters; alignment mean 0.006, σ 0.097, IQR 0.114; monthly fund return mean 0.008; mean management fee 0.442%.
- **`data gap`:** no turnover, no gross-vs-impact decomposition of realized costs, no deflated/multiple-testing-corrected Sharpe, no IC, no code or replication package, and no confidence interval for the 1/N results beyond CAPM α stars.

### Independently reproduced

not independently reproduced.

### Negative evidence

- **From the source itself:**
  - **Scale kills anomalies:** without augmentation only **1** anomaly survives net of impact for a 1.6bn fund (Table 1), and with expected-return conditioning **0** survive for that size until the TC layer is added (Table 1, E[r]-adjusted column) — i.e. the headline "revival" is fund-size conditional.
  - **Drawdown risk rises with the ML layer:** E[r]-adjusted MaxDD **−55% to −60%** vs −26% to −34% unadjusted; the source attributes this to "being wrong" in high-expected-return stocks (§3). Even after TC adjustment MaxDD stays **−34% to −51%**.
  - **Theme boundary:** **size and value anomalies are not revived** for small-to-large funds; for 1600m funds only **one** momentum, one profit-growth and one leverage anomaly survive (Table 2, §3, §6) — the mechanism relies on liquid, information-rich names, not the classic small-cap anomalies.
  - **Profitability decays with scale:** 1/N net return falls **16.0% → 5.4%** and Sharpe **1.01 → 0.64** from 40m to 1600m funds (Table 3); the source leaves optimal allocation between implementable anomalies and a market overlay to **future research** (§6).
  - **Deteriorating opportunity set:** for the largest funds the ex ante count of implementable anomalies declines after **2016** with a further drop in **2023** (Figure 3), consistent with the post-2003 anomaly decay the paper starts from (Green et al. 2017; Chen & Velikov 2023 — anomalies "fail to survive transaction costs in the form of effective spreads", §1).
  - **Literature the paper concedes:** post-publication decay (McLean & Pontiff 2016), cost-driven loss of significance (DeMiguel et al. 2020), all-in trading costs inferred from fund exposures (Patton & Weller 2020), ETF/fund replications returning less than paper results (Johansson, Sabbatucci & Tamoni 2025) — all cited by the authors themselves (§1, Related Literature).
  - **Causal modesty:** the source explicitly does **not** identify why anomalies decayed (§1), so the mechanism claim rests on selection, not on a causal repair of mispricing.
- **From Scout reading (clearly separated):**
  - **Cost model is partial by construction:** price impact only — no commission, spread, or borrow on a long–short portfolio of 153 monthly-rebalanced anomalies; turnover is unreported, so the completeness of the impact deduction cannot be audited.
  - **Selection-on-significance risk:** Table 1/2 count anomalies that are *ex post* significant at 5% over 2004–2023 among 153 candidates (×3 construction variants ×4 fund sizes); no deflated-Sharpe / multiple-testing correction is reported for the counts, and the 1/N strategy then selects on top of the same forecasts — the source's Harvey–Liu–Zhu remark (§3, Figure 1) is not carried into the count tables.
  - **Elapsed test window:** OOS = 2004–2023, already in the past; there is no post-2023 holdout in the pinned version, and the June 2026 revision on the landing page was not verified (`data gap`).
  - **Reproduction barrier:** proprietary CRSP/Compustat/CRSP-MF data, an unpublished 153-feature pipeline, 50-trial NN ensembles annually, no code statement → independent reproduction cost is high and unverified.
  - **Version mismatch** between landing ("last revised 23 Jun 2026") and the downloadable March 25, 2026 PDF (`data gap`).
  - Absence of peer review: SSRN/MIT Sloan working paper with no acceptance statement (`not stated in source`).

## Falsification plan

Source-defined tests (already in the paper's design): expanding-window annual re-fit with a 23-year initial training window; ex ante vs ex post comparison (Figure 3 vs Table 1); concentration control against 5–25-way single sorts (Figure 5); PCA heterogeneity check (Figure 4); fund-behavior validation with fixed effects and clustered errors (Tables 4–8); E[r]-only ablation of the TC layer (Table 1).

Scout-added operational tests — everything here is `research-proposed` except thresholds explicitly marked `research-defined`:

1. **Full-cost ladder (`research-proposed`).** Re-run Table 3 after adding, on top of the modeled impact, one-way commissions + half-spread + annualized borrow fee at 5 / 10 / 20 / 40 bps per side. **Failure rule (`research-defined`):** if the net CAPM α is ≤ 0 for **all four fund sizes**, the *tradability* claim fails (the selection relation may still hold); action = keep `research-only`, block any implementation candidate.
2. **Turnover / impact audit (`research-proposed`).** Compute realized monthly turnover and the dollar participation of the 1/N strategy; compare implied impact with the Frazzini-calibrated `0.2/V` term. **Failure rule (`research-defined`):** if realized cost exceeds **2×** the modeled `E[TC]`, the cost layer is mis-specified and every "net" number in Table 1/3 must be treated as overstated.
3. **Multiple-testing deflation (`research-proposed`).** Apply a deflated-Sharpe / false-discovery control to the 153 × 3 × 4 family behind Table 1. **Failure rule (`research-defined`):** if fewer than **50%** of the source's flagged anomalies (baseline 126 / 101 / 81 / 41) survive the correction, the "revival" is a selection artifact; action = reject the count claim, retain only the 1/N evidence.
4. **Post-2023 blind holdout (`research-proposed`).** Freeze the March 2026 specification and evaluate 2024–2026 (and each new year) with no re-tuning of quintiles, ensemble rules, or fund sizes. **Failure rule (`research-defined`):** 1/N net Sharpe < **0.5** for micro/small funds, or net α ≤ 0 for any fund size in two consecutive years, fails the current-regime hypothesis.
5. **Layer ablation (`research-proposed`).** Add the missing **TC-only** cell (characteristic sort + cost filter, no NN forecast) and an **NN-only** cell (no characteristic first stage). **Failure rule (`research-defined`):** if the TC-only count matches the E[r]-&-TC count (within 10 anomalies) the ML layer adds nothing; if the NN-only cell matches Table 3's Sharpe within 0.10, the anomaly first stage adds nothing.
6. **Forecast-shuffle placebo (`research-proposed`).** Within each month, permute the cross-section of NN expected net returns before the second sort (keeps the distribution, destroys the stock-level mapping). **Failure rule (`research-defined`):** if the shuffled forecast preserves Table 1's E[r]-adjusted counts within 20%, the improvement is a sort-mechanics/concentration artifact rather than return predictability.
7. **Concentration replication (`research-proposed`).** Reproduce Figure 5 with the shuffled forecast; the ML overlay must beat the 25-portfolio single sort **after** full costs. **Failure rule (`research-defined`):** a tie or deficit after costs fails the "interpretability-preserving overlay" claim.
8. **Competing explanation (`research-proposed`).** Benchmark the double sort against the closest published alternative — Jensen, Kelly, Malamud & Pedersen (2025) implementable efficient frontier and Chen & Velikov (2023) expected-return sorts — on identical data and cost terms. **Failure rule (`research-defined`):** if the 1/N Sharpe advantage over the best alternative is < 0.10, this paper's incremental contribution is not established (both are checked by their own primary sources before any number is quoted).
9. **Point-in-time / leakage audit (`research-proposed`).** Rebuild features from raw CRSP/Compustat with delisting returns and vintage-correct JKP code; confirm the January 2004 first-OOS boundary never sees post-2003 data. **Failure rule (`research-defined`):** any 20%+ change in Table 1 counts is a pipeline failure, not a hypothesis test — rebuild before proceeding.
10. **Action on failure:** every failure path leaves the record at `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`; no re-tuning of frozen parameters may be used to rescue a failed test.

## Crypto portability

**unproven.** The source demonstrates the mechanism only in U.S. equities and never mentions crypto, stablecoins, funding, or 24/7 markets anywhere in the pinned PDF — there is **no crypto evidence**, so this cannot be `direct`; nothing has been ported yet, so it is not `adapted`.

Porting risks if a crypto variant is ever attempted (all `research-proposed`, none from the source):

- **Universe / survivorship:** quintile double sorts need a broad, point-in-time cross-section with delisted names; crypto listing histories are survivor-biased, and the 153 JKP characteristics (accruals, debt issuance, book equity) have **no direct equivalent** for tokens — the whole characteristic first stage must be re-specified, which is a different signal.
- **Calendar semantics:** month-t formation with a next-month holding period collides with crypto's 24/7 clock; candle/timezone conventions and "month end" are free parameters the source never defines for crypto.
- **Cost layer:** the impact model is calibrated on equity daily dollar volume; perp venues need funding payments, maker/taker fees, mark/index basis and liquidation-chain effects that the quadratic `0.2/V` term does not capture — cross-venue fragmentation also breaks the single-`V` assumption.
- **Short leg:** crypto perps make shorting cheap but funding and liquidation cascades interact with a monthly long–short overlay in ways the source never models (spot vs perpetual, borrow/availability differ by venue).
- **Fund-size scaling:** the four AUM anchors are CRSP mutual-fund percentiles; "fund size" has no counterpart for a crypto mandate, so the TC-conditioned selection would need a `research-proposed` capacity anchor of its own.
- Any claim of the form "implementable-anomaly selection works on crypto" would be a **different mechanism record requiring its own primary source**.

## Limitations

- `data gap`: **turnover never reported**; the trade-size vector `τ_t` used in the impact model is not defined; no gross-vs-cost decomposition of the "net" figures.
- `data gap`: cost model = price impact only; no commission, spread, borrow, slippage, fill or latency model anywhere in the pinned PDF.
- `data gap`: no deflated/multiple-testing correction for the Table 1/2 counts, no IC, no capacity analysis, no replication package or code statement.
- `data gap`: the June 23, 2026 revision advertised on the landing page was not retrievable; the pinned PDF is the March 25, 2026 build.
- `underspecified`: stock-level universe filters, sort breakpoints/ties, formation date/timezone, missing-data handling, holdings-report staleness, short-loan feasibility.
- `underspecified`: publication status — SSRN / MIT Sloan working paper, no journal or peer-review statement in source.
- Sample risk: test window 2004–2023 is entirely in the past; the source itself documents a shrinking implementable set after 2016 for large funds (Figure 3) and general post-2003 anomaly decay.
- Scale risk: results are strictly conditional on fund size (40m → 1600m USD); net return falls 16.0% → 5.4% and the unadjusted/unexpected-return layers collapse to 0–1 anomalies for large funds.
- Model risk: 50-trial, top-5-ensemble NN re-fit annually on 153 features — re-fit variance, seed sensitivity and hyperparameter provenance are `not stated in source`.
- Dependency risk: proprietary CRSP/Compustat/CRSP-MF data and the JKP feature pipeline make independent reproduction expensive; `not independently reproduced`.
- Single-study evidence for this exact construction; adjacent literature (Chen & Velikov 2023; Johansson et al. 2025; Patton & Weller 2020) points the other direction on cost survival, but their primary sources were **not** opened this run — no numbers from them are asserted here.

## Implementation status

`implementation_status: not-implemented`. Nothing in this record has been implemented in our research stack: no characteristic pipeline, no neural-network expected-return model, no double-sort engine, no backtest, no Qlib run, no Paper/Testnet/Live activity of any kind. The record is a normalized research capture of a public working paper only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. No Sharpe ratio, anomaly count, alpha star, or fund-alignment regression in this record promotes it.

## Related Wiki records

No stable Hermes Wiki Brain page is verified for any related record this run, so only the schema page is linked as a Wiki link:

- `[[quant/strategy-research-record-spec-v1]]` — authoritative schema specification (read this run).

Adjacent records already in this repository (checked for dedup; **different source identities and different mechanisms** — plain filenames, not Wiki links):

- `daily-return-information-factor-drif-elastic-net-cross-sectional-2026-09-23.md` — Cakici et al. (SSRN 6005614) elastic-net DRIF; single signal spanning the short-horizon anomaly class, gross-of-cost with breakeven analysis (different paper, different signal, different cost treatment).
- `anomaly-pre-release-drift-predicted-signal-decile-portfolios-2026-09-23.md` — timing of predicted-anomaly deciles around information release (different mechanism: event-window drift).
- `china-ashare-factor-library-overfitting-audit-amihud-illiquidity-falsification-2026-09-13.md`, `us-equity-microstructure-ensemble-lightgbm-fdr-falsification-2026-09-13.md` — multiple-testing / overfitting audits that frame the same skepticism this record's falsification plan must survive.
- `cross-sectional-equity-ridge-percentile-rank-alpha-2026-09-03.md`, `alphaforge-generative-formulaic-alpha-dynamic-factor-timing-2026-09-17.md`, `adaptive-alpha-weighting-ppo-llm-generated-alphas-2026-09-05.md` — other ML factor-construction sources (different papers, different signals).
- `crypto-cross-sectional-elastic-net-ctrend-2026-08-31.md` and the broad `crypto-cross-sectional-*` anomaly family — the equity anomaly families this paper selects over; any crypto analogue would be a separate record.

## Sources

1. Heiner Beckmeyer, Florian Berg, Timo Wiedemann, Jonas Wortmann. *"Reviving Anomalies."* **MIT Sloan Research Paper No. 7378-26**, SSRN abstract **6468806**, DOI **10.2139/ssrn.6468806**; date written 25 March 2026, posted 26 March 2026, landing shows "last revised 23 Jun 2026"; retrieved document version "March 25, 2026"; 30 pages. Landing: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6468806 — **landing page and all 30 pages read on 2026-09-23**; retrieved PDF SHA-256 `35abeaa5710f97fcb3bcf7e68eae48a7f32e75b84fbe414e053c5c3b170525f4`, 539,504 bytes, `/CreationDate D:20260325145439Z`. PDF: https://papers.ssrn.com/sol3/Delivery.cfm/6468806.pdf?abstractid=6468806&mirid=1&type=2
2. Every quantitative claim in this record traces to that pinned PDF at a named location: **Table 1** (ex post significant-anomaly counts, net returns, Sharpe, MaxDD by fund size and construction), **Table 2** (counts per JKP theme), **Table 3** (20-year OOS 1/N net return, σ, Sharpe, MaxDD, CAPM α/β), **Table 4** (anomaly-alignment panel), **Tables 5–6** (fund-return regressions and IQR effects), **Tables 7–8** (management-fee regressions), **Figures 1–5** (theme improvements, fund-size curve, ex ante counts, PCA, concentration control), **§2 Methodology / Eq. 1–6** (double sort, NN expected returns, quadratic price impact), **§3–§4** (ex post/ex ante results, fund behavior), **§5 Robustness**, **§6 Conclusion**, **Appendix A–B** (fund-size distribution, summary statistics).
3. Methods/cost verification (required by the run contract) was performed against **§2 "Transaction Costs" (Eq. 5–6)** and every table caption's "net … accounting for price impact costs" wording, not against the abstract or any summary.
4. Discovery aids only (no figure or rule in this record is taken from them): the SSRN landing-page metadata/abstract, and the prior run's dedup note in `daily-return-information-factor-drif-elastic-net-cross-sectional-2026-09-23.md` which deferred this candidate under the hard cap.
