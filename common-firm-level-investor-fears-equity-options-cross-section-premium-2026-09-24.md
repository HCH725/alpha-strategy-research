---
schema: strategy-research-record-v1
title: Common firm-level investor fears cross-sectional premium from equity options (PCA of model-free implied variances)
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-09-07
sources:
  - "https://arxiv.org/abs/2309.03968"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Common firm-level investor fears cross-sectional premium from equity options (PCA of model-free implied variances)

## Provenance

- **Primary source (authors, exactly as the source):** Jozef Baruník (Institute of Economic Studies, Charles University, Prague; Institute of Information Theory and Automation, Czech Academy of Sciences), Mattia Bevilacqua (University of Liverpool Management School), Michael Ellington (University of Liverpool Management School). The arXiv abstract-page authors field and the PDF title page agree; the PDF `/Author` metadata field is **empty**, so consistency was verified only from those two places.
- **Version / date:** **arXiv v1 only** — abstract page shows a single entry `[v1]`, submitted 7 Sep 2023; page/PDF stamp `arXiv:2309.03968v1 [q-fin.GN] 7 Sep 2023`; PDF title page dated September 11, 2023 (CreationDate `D:20230911004254Z`). The abstract page has **no Comments field, no `journal_ref`, and no publisher DOI** (re-checked 2026-09-24) → `preprint only`. arXiv-issued DOI `10.48550/arXiv.2309.03968` verified to resolve (HTTP 302 → `https://arxiv.org/abs/2309.03968`, 2026-09-24).
- **PDF checksum (pinned, read in full):** 50 pages, 1,302,134 bytes, SHA-256 `d13c52a158bdfcfca4d6cdeee86adc5c8a269947035fbd907718bda116c315bc`. `pypdf` extraction yielded 125,962 characters; all 1,927 extracted lines were read directly (Sections 1–6, Appendix A discretization, Appendix Tables A1–A11, references).
- **Sample period (primary source):** firm-level option data **January 03, 2000 – December 31, 2020** (§3.1); rolling-correlation figures cover 2001–2020 (Figure 3 notes). The paper reports **no data after 2020-12-31**.
- **Universe (primary source):** signal panel = **526 firms** with listed equity options after filtering (§3.1; ~90% large-cap, ~10% mid-cap, mostly S&P 500 constituents plus some Russell 1000 names); pricing panel = all CRSP common stocks on NYSE/NASDAQ/AMEX after filters, **average 1,045 stocks (min 883, max 1,385)** (§4). Because the pricing minimum (883) exceeds the optioned panel (526), the sorted universe does **not** require listed options on the stock itself — only the PCA factor (built from the 526 names) and trailing returns are needed; the exact wording of the inclusion rule (“stocks to have this data available”, §4) is `underspecified`.
- **Transaction-cost treatment (must-read sections checked):** Sections 2–5 (Methods / measurement / pricing exercises / robustness) and the Appendix were read, and the full extracted text was keyword-scanned: `cost` / `costs` → **0 occurrences anywhere in the paper**; `transaction cost|turnover|slippage|commission|borrow|short sale|friction|market impact|fees` → **0 occurrences**; `bid-ask` → only 3 occurrences, all in option-data filtering and the CBOE-style discretization (negative-spread option removal; `Q(Ki)` average bid-ask), i.e. **data construction, not trading costs**. Therefore cost/slippage/borrow/turnover treatment is **`not stated in source`** (`data gap`); it is **not** inferred to be zero-cost, and every performance figure below must be read as **gross**.
- **Core performance numbers:** see Evidence → Source-reported; every figure carries its Table/Panel anchor.
- **Pre-write dedup (deterministic, whole repository):** ripgrep across **all tracked files** (all `*.md` records plus `coverage_manifest.csv`) for `2309.03968`, `10.48550/arXiv.2309.03968`, exact title `Common Firm-level Investor Fears`, `Common Firm-level`, `common firm-level`, `firm-level fears`, `common fears`, `bad fears`, `good fears`, `Bevilacqua`, `Ellington`, `model-free implied variance`, `Bakshi` → source-identity terms **0 matches**. The only `Barun` hits are `cross-sectional-realized-skewness-dispersion-market-timing-2026-09-24.md` (different paper, arXiv 2604.07870, different mechanism) and `expected-shortfall-factor-model-common-tail-loss-severity-2026-09-11.md` (different authors, Baruník & Nevrla quantile factors) — neither shares this source identity. `git log --oneline -20` was inspected as a convenience glance only and does not by itself satisfy dedup. Wiki Brain `kb_search`: `"option-implied variance common factor cross-section stock returns risk premium"` → 0 results; `"variance risk premium investor fears options"` → 0 results (recorded as-is; no Wiki link invented).

## Economic mechanism

### Source-reported

The authors argue that option prices embed firm-level uncertainty (“investor fears”) beyond market-level fear (VIX / index options). They extract model-free implied variance from OTM calls and puts on individual stocks, split it into **good fears** (call-implied, upside uncertainty) and **bad fears** (put-implied, downside uncertainty), and take the first principal component of each cross-section as the **common** firm-level fear factor. Their stated rationale is hedging-based: in an ICAPM-style equilibrium (Merton 1993; Campbell et al. 2018; Herskovic et al. 2016; Farago & Tédongap 2018), stocks that hedge shocks to aggregate downside uncertainty (“common bad fears”) are desirable and therefore earn **lower** expected returns; prospect-theory asymmetry (Kahneman & Tversky) makes investors demand a larger compensation for exposure to bad fears than good fears. The paper claims firm-level common fears contain information distinct from index-option market fears (monthly innovations correlate ~74–79% with their market-fear orthogonalized counterparts; rolling daily correlations fall substantially from 2012 onwards).

### Research interpretation

Falsifiable mechanism: **aggregate-uncertainty hedging demand / priced downside-uncertainty risk**, expressed as a cross-sectional beta premium — stocks with high trailing sensitivity to innovations in the PCA factor of put-implied variance deliver lower subsequent returns, so a value-weighted long-low-beta / short-high-beta portfolio earns a positive gross spread. Component roles (hybrid structure):

- **Signal (primary):** trailing 1-year daily beta of each stock’s excess return on innovations to the common bad-fears factor, `β^ΔCF−` (Eq. 6).
- **Controls embedded in the signal:** the beta regression also loads on VIX innovations (`ΔVIX`), or alternatively market-fear innovations (`ΔMF`) — i.e. the signal is defined net of market-level vol/fear co-movement.
- **Cross-sectional risk scale:** monthly value-weighted quintile (main) and decile (Fama–MacBeth) re-sorting.
- **Not a risk-management overlay:** no stop, sizing, or timing rule is proposed by the source.

Note the paper frames this as a *risk premium* (compensation for hedging service), not mispricing. If that framing is right, the spread may be fragile once costs/borrow are introduced, and ablation against variance-risk-premium (VRP), common idiosyncratic volatility (CIV) and liquidity (LIQ) factors is essential. Whether the long leg alone carries the result is an open ablation question (see Negative evidence).

## Signal

All items below are `source-reported` unless marked otherwise.

- **Factor construction timestamp:** daily, using option data from the trading day; PCA extracted with an **expectation-maximization algorithm over a rolling 252-day window** “to eliminate any look ahead bias for our pricing exercise” (§3.2 — source claim).
- **Lookback:** implied variances from options maturing **23–37 days** (proxy for 1-month-ahead variance; nearest expiration to 30 days, single expiration — no CBOE-style interpolation, Appendix A); beta regressions use **1 year (≈252 days) of daily data** rolling to month end.
- **Option filters (signal input):** missing delta, missing IV, zero bid, nil volume, nil open interest, negative bid-ask spread, arbitrage violations removed; then options with **fewer than 4 contracts** on a day removed; stock-level panel requires **>5 years continuous option data** and explicitly excludes **bankruptcy, delisting, and M&A** names (§3.1).
- **Sort formation timestamp:** **end of month t**, on CRSP monthly data after filters; **returns over month t+1**; process repeats monthly (value-weighted quintiles).
- **Universe filters for the sort (month t → applied in t+1):** drop stocks in the **bottom 30% of market cap**; drop stocks priced **< $5**; drop stocks whose month-t returns are in the **top/bottom 5%** (winsorization by exclusion). A relaxed robustness version (bottom 20%, price < $1, average 1,360 stocks) is stated as “available upon request” and is **not verifiable** from v1.
- **Long / short direction:** the paper constructs the spread as **long high-beta (Q5) minus low-beta (Q1)** and reports it as **negative** (Table 3 Panel C `5-1` = −0.53%/month). The implementable reading is therefore **long Q1 (low `β^ΔCF−`), short Q5 (high `β^ΔCF−`)**, held one month, rebalanced monthly.
- **Parameters (all `source-reported`):** 252-day PCA window; 1-year beta window; 23–37 day maturity band; ≥4 contracts; quintile/decile/5×5 double-sort grids; Newey–West t-stats with 12 lags (Shanken 1992 errors-in-variables adjustment) for Fama–MacBeth.
- **`underspecified` / `data gap`:** (i) PCA principal-component **sign orientation and normalization are never stated** — the first PC’s sign is arbitrary, so the paper does not specify how `CF−` is aligned to “bad fears rising”; (ii) the exact trading day, price, and order type used to execute the month-end rebalance are not stated; (iii) the definition/source of the risk-free rate behind “excess return” in the daily beta regressions is not stated; (iv) sort tie-breaking and treatment of stocks entering/leaving the universe mid-month are not stated; (v) delisting-return handling in the CRSP pricing panel is not stated; (vi) timezone/session conventions are not stated (US equity daily data implied, `data gap`). Because of (i)–(vi), the signal is **close to reconstructable but not fully reproducible from the paper alone**.

## Required data

- **Instrument / universe:** US common stocks (NYSE, NASDAQ, AMEX) in the pricing panel; 526 optioned large-/mid-cap firms in the signal panel.
- **Venue / market type:** listed equity options and S&P 500 index options (market-fear control) on US exchanges; spot equities.
- **Vendors (commercial):** **OptionMetrics** daily option quotes; **CRSP** stock prices/returns; **Kenneth French Data Library** (FF5, momentum, anomaly test assets); VIX index; plus VRP (Carr & Wu 2009), CIV (Herskovic et al. 2016), LIQ (Pástor & Stambaugh 2003) series for controls — their exact construction sources for VRP/CIV/LIQ series are not further specified (`data gap`).
- **Fields:** option bid/ask, IV, delta, volume, open interest, strikes, maturities; underlying daily/monthly prices, returns, market cap; index-option quotes for market fears.
- **Point-in-time:** rolling 252-day PCA + trailing 1-year betas are claimed look-ahead-free (§3.2); however the option panel’s exclusion of bankruptcies/delistings/M&A and the >5-year-continuous-data requirement make the **signal’s cross-sectional history survivorship-shaped by construction** (the word “survivorship” never appears in the paper).
- **Missing data:** EM algorithm (Stock & Watson 2002) inside the rolling PCA handles the unbalanced panel; no other imputation is stated.
- **Timestamp / timezone:** not stated (`data gap`).

## Execution assumptions

**The source states essentially none.** No order type, fill model, signal-to-order delay, fees, slippage, spread, impact/capacity model, leverage/margin, borrow/shorting availability or cost, latency, turnover, or failure handling appears anywhere in v1 (full-text keyword scan: bare `cost(s)` 0 hits; turnover/slippage/commission/borrow/friction/market-impact/fees 0 hits). Reported portfolio returns are therefore **gross of all trading frictions**, and short-leg borrow feasibility for the high-beta quintile is untreated. The universe filters (sub-$5 and bottom-30%-cap exclusions) mitigate — but do not resolve — liquidity and borrow concerns.

`research-proposed` operationalization (not from the source): execute the month-end sort at the **next trading day’s close**, market orders; stress borrow/rebate on the short leg at κ ∈ {0, 10, 20, 50} bps per side per rebalance; measure realized monthly two-sided turnover in replication (the paper reports **no turnover figure**, `data gap`) and net CER before any tradability claim.

## Evidence

### Source-reported

All figures are third-party claims from Baruník, Bevilacqua & Ellington, arXiv:2309.03968v1, **US equities, sample Jan 2000 – Dec 2020 (signal options 2000–2020), gross of any cost**, not independently reproduced; each carries its Table/Panel anchor.

- **Factor structure — Table 1 / Table 2:** average cross-sectional implied variance 0.187 (good 0.067, bad 0.120). Rolling-252d first-PC variance explained: mean **87.13% (CF) / 90.51% (CF+) / 83.94% (CF−)**; full-sample: **77.75% / 83.46% / 75.65%** (Table 2 Panel B).
- **Distinct from market fears — §3.3, Figures 2–3:** correlations of monthly innovations with market-fear-orthogonalized innovations **74% (CF), 76% (CF+), 79% (CF−)**; rolling daily correlations range from highs ≈0.8 (CF+ vs good market fears) to lows ≈**−0.05** (CF− vs bad market fears), materially lower from 2012 onward.
- **Single sorts — Table 3 Panel C (common bad fears):** value-weighted quintile monthly excess returns **1.28 / 0.92 / 1.00 / 0.91 / 0.76%**; spread `5-1` = **−0.53%/month (t = −2.82)** = −6.36%/yr; **αFF5 = −0.42%/m (t = −2.32)**; **αFF5+MOM = −0.43%/m (t = −2.46)** → −5.04% / −5.15% per annum (§4 text; intro phrases the risk-adjusted gap as **5.16% per annum**, i.e. 0.43 × 12). Quintile 1 alone: αFF5 = 0.55%/m (t = 3.29); quintile 5 alone: αFF5 = 0.13%/m (t = 1.59, n.s.). Common fears and **common good fears spreads are not significant** (Table 3 Panel A `5-1` t = −1.74; Panel B t = −1.53).
- **With ΔVIX control — Table 4 Panel C:** spread **−0.41%/m (t = −2.66)**; **αFF5 = −0.21%/m (t = −1.78)** → −2.52%/yr; **αFF5+MOM = −0.23%/m (t = −2.24)** → −2.76%/yr (§4 text).
- **With market-fear control — Table 5 Panel C:** spread **−0.41%/m (t = −2.46)**; **αFF5 = −0.16%/m (t = −1.47, not significant)**; **αFF5+MOM = −0.18%/m (t = −2.01)** → −2.16%/yr (§4 text).
- **Fama–MacBeth, decile beta portfolios — Table 6, columns 13–18:** λ_CF− = **−0.41, −0.45, −0.45, −0.47, −0.42, −0.41 per month** with Newey–West/Shanken t = **−3.54, −3.93, −3.76, −4.11, −3.69, −3.29**; §4 text annualizes to **−5.64% to −4.92% per annum** (the abstract, introduction and conclusion state **−5.63% to −4.92%**). Common-fears and common-good-fears λ columns are mostly insignificant (e.g. col. 1 t = −1.07, col. 7 t = −1.05). Adjusted R² 0.756–0.982; intercepts insignificant.
- **Double sorts vs VIX — Table 7, columns 13–18:** λ_CF− = −0.17 to −0.22/month → **−2.64% to −2.04% per annum** (§4 text).
- **Double sorts vs market fears — Table 8, columns 13–18:** significant estimates imply **−2.76% to −2.40% per annum**; col. 15 (−0.15, t = −1.73) only 10%, col. 18 (−0.10, t = −0.99) insignificant (§4 text).
- **Fama–MacBeth with market fears priced jointly — Table 10, columns 13–18:** λ_CF− = −0.21, −0.16, −0.14, −0.22, −0.22, −0.07 (t = −2.67, −1.80, −1.73, −2.74, −2.75, −0.71); significant specs annualize to **−2.64% to −2.52%**, two specs only 10% (§5.1 text). Market-fear premia in the same table are **positive** (good market fears ≈ +1.92% to +2.40%/yr significant).
- **Alternative test assets — §4.1, Figure 4, Tables 9 / A9:** with anomaly portfolios as test assets, significant annualized premia: CF **−3.36% to −1.68%**, CF+ **−3.00% to −1.80%**, CF− **−3.96% to −1.68%** (Figure 4 text); Table 9 (25 ME/INV + ME/BM + ME/MKT + 25 fear portfolios) CF and CF− λ ≈ −0.16 to −0.20/month → **−1.92% to −2.40%/yr**, CF+ negative but insignificant (§4.1 text).
- **Three-pass regressions — Table 11 (Giglio & Xiu 2021):** all Wald tests reject the weak-factor null at p = 0.00; annualized λ ranges **Panel A −2.76% to −1.44%**, **Panel B −3.72% to −1.44%**, **Panel C (equal-weighted IV proxy) −7.68% to −3.96%** (§5.2 text). Caution: Panels A–C report **identical intercept, λMKT, Wald, adjusted R² and factor-count rows**, differing only in λ_CF — the paper does not explain this invariance (`underspecified`).
- **Controls that do not subsume (in-sample, source claim):** FF5, momentum, CIV, LIQ, VRP and a battery of anomaly portfolios; alternative factor definitions; relaxed universe filters (results “available upon request”, not verifiable).

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Zero friction treatment anywhere in v1:** bare `cost(s)`, turnover, slippage, commission, borrow, short-sale, friction, market-impact and fee terms have **0 occurrences** in the full text; the only bid-ask mentions are option-data filters. All headline numbers are gross; short-leg borrow is untreated (`not stated in source`).
2. **No out-of-sample discipline:** `out-of-sample`, `holdout`, `walk-forward` → 0 occurrences; no train/test split, no post-sample holdout; the paper is an in-sample asset-pricing exercise. Also **no Sharpe, no drawdown, no CER** statistics anywhere (0 occurrences).
3. **Economic significance collapses under controls:** the headline −5.16%/yr (Table 3 Panel C, FF5+MOM) falls to **−2.76%/yr with ΔVIX control** and **−2.16%/yr with market-fear control**, where the plain FF5 alpha is **insignificant (t = −1.47)** and even FF5+MOM is only t = −2.01 (5%, not 1%).
4. **Mechanism is narrow:** common-fears and common-good-fears spreads are insignificant in the base spec (Table 3 Panels A/B, t = −1.74 / −1.53) — only **bad** fears price; the premium is not a generic implied-variance effect.
5. **Source-internal inconsistencies:** (a) §4 text says the Table 5 market-fear-controlled FF5+MOM spread is “significant at 1% levels with a t-statistic of −2.24”, but **Table 5 Panel C shows t = −2.01** (−2.24 belongs to Table 4); (b) abstract/intro/conclusion say **−5.63%** while §4 text says **−5.64%** for the same Table 6 range; (c) §4 writes “ranges from −0.41 to 0.47” (missing minus sign; table shows −0.47); (d) Table 11 Panels A–C share identical intercept/market-fit rows without explanation.
6. **Survivorship-shaped signal panel:** §3.1 explicitly excludes **bankruptcy, delisting and M&A** names and requires **>5 years continuous option data** (examples given: GM, Lehman Brothers, Merrill Lynch) — the PCA factor is estimated on a survivor-selected cross-section; the paper never discusses this.
7. **Long leg carries much of the result:** in Table 3 Panel C the short leg (high-beta Q5) has αFF5 = 0.13%/m (t = 1.59, n.s.) while the long leg (Q1) has 0.55%/m (t = 3.29) — the spread depends mostly on low-beta names, raising characteristic-overlap questions that are only partly addressed (characteristic-controlled sorts in Appendix A1/A2; relaxed-filter results “available upon request”).
8. **Unverifiable robustness:** multiple results (relaxed filters, implied-variance-spread measure, alternative specs, “all pricing factors together”) are explicitly “available upon request” and cannot be checked in v1.
9. **No replication materials:** `github`, `replication package`, `code availability` → 0 occurrences; core inputs (OptionMetrics, CRSP) are commercial.
10. **Staleness:** sample ends **2020-12-31** — more than five years before this record (2026-09); no evidence of persistence through the 2021–2026 regime (rate shock, meme-stock era, 0DTE/options-structure changes).

## Falsification plan

Thresholds below are `research-defined falsification threshold`; operational choices are `research-proposed`. None are source-specified.

- **F1 — post-2020 point-in-time persistence (`research-defined`):** rebuild the signal on data from 2021-01-01 to the present (no re-tuning of the 252d/1y windows). Fail if the long-low-β / short-high-β monthly spread’s FF5+MOM alpha is ≥ 0 (sign flip) or its one-sided t does not reach −1.645 in the paper’s λ orientation.
- **F2 — control robustness, the paper’s own weak point (`research-defined`):** re-run the Table 5 spec (market-fear control) jointly with FF5+MOM. Fail if |t| < 1.96 for the controlled spread — the source itself already sits at t = −1.47 (FF5) and −2.01 (FF5+MOM), so this is the primary fragility test.
- **F3 — survivorship ablation (`research-defined`):** rebuild the options panel keeping bankrupt/delisted names (no >5-year-continuous-data requirement). Fail if |λ_CF−| shrinks by ≥ 50% versus the source construction.
- **F4 — placebo (`research-defined`):** 500 time-series shuffles of CF− innovations through the identical pipeline; require the empirical |λ| to sit beyond the 95th percentile of the shuffle distribution (p < 0.05).
- **F5 — specificity ablation (`research-defined`):** CF− must outperform CF+ and CF economically and statistically (source: CF+ insignificant). Fail if CF+ performs equivalently — that would reduce the mechanism to generic implied-volatility exposure, not bad-fear hedging.
- **F6 — cost stress (`research-proposed` grid):** net the spread at κ ∈ {0, 10, 20, 50} bps per side per rebalance (`research-proposed`), using **measured** monthly turnover (source reports none, `data gap`). Fail if net CER at κ = 20 bps ≤ passive long-only over the replication sample.
- **F7 — competing explanations (`research-defined`):** VRP, CIV and LIQ must not subsume the premium out-of-sample (in-sample Table 6 says they do not). Fail if adding any one drives λ_CF− to insignificance (|t| < 1.96) in the post-2020 sample.
- **Action on failure:** keep the record research-only; no implementation, no candidate promotion; log the failed test as negative evidence against this family.

## Crypto portability

**unproven.** The design is inseparable from a **broad cross-section of liquid individual equity options**: it needs ~526 names with 23–37 day OTM puts/calls, ≥4 contracts per strike-day, to run a PCA and then value-weighted quintile sorts on ~1,000 stocks. Crypto has listed options on only a handful of majors (concentrated in BTC/ETH on Deribit and a few venues), so neither the cross-sectional PCA nor the quintile sort is reproducible as designed. Additional porting risks: no month-end/session boundary in 24/7 markets (sort formation timestamp undefined), perp funding and spot/perp basis have no analogue in the paper, venue fragmentation breaks any single options tape, borrow/short mechanics differ entirely, and mark/index-price conventions affect any implied-variance extraction. A BTC/ETH-only two-name version would not constitute the mechanism (no cross-section). This is a **ported hypothesis**, not crypto empirical evidence; crypto portability is not authorization to trade.

## Limitations

- `not independently reproduced`; all performance figures are `source-reported` and **gross**.
- `data gap`: transaction costs, slippage, spread, borrow, turnover, capacity, fill model — none stated in source (verified by full-text scan, not inferred).
- `data gap`: risk-free-rate definition for excess returns, VRP/CIV/LIQ series construction, timezone/session conventions, delisting-return handling in the pricing panel.
- `underspecified`: PCA sign orientation/normalization; exact month-end execution timing/price/order type; the §4 universe-inclusion wording (“this data available”); Table 11’s identical cross-panel fit rows; sort tie-breaking.
- `unproven`: persistence after 2020-12-31; robustness under survivorship-free signal construction; net-of-cost tradability; post-control economic significance (already collapses to ~−2.2%/yr gross at FF5+MOM with market-fear controls).
- Source-quality: preprint only (no journal_ref/DOI on arXiv as of 2026-09-24); several robustness results “available upon request”; no code/data availability statement; commercial data dependency limits replication.
- Sample-selection: signal panel excludes bankruptcies/delistings/M&A and requires >5 years continuous option coverage — survivorship-shaped factor history.
- Publication/selection bias risk is unaddressed by the source.

## Implementation status

`implementation_status: not-implemented`. Nothing in this record has been implemented in our research stack: no signal pipeline, no backtest, no Qlib full-backtest validation, no survivor bundle, no Paper, Testnet, or Live activity. This record is normalized research material only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; or approved for implementation, paper trading, testnet, or live trading.

## Related Wiki records

Two Wiki Brain searches (`"option-implied variance common factor cross-section stock returns risk premium"`, `"variance risk premium investor fears options"`) returned **0 results** — no related Wiki Brain pages were identified, and no Wiki link is invented here. Related records in this repository (different sources, distinct mechanisms):

- `option-implied-surface-cremers-weinbaum-skew-crash-regimes-2026-09-02.md` — options-implied cross-sectional signals (per-stock IV spread / risk-neutral skewness levels) rather than a PCA common factor of implied variances.
- `cross-sectional-realized-skewness-dispersion-market-timing-2026-09-24.md` — shares author Jozef Baruník but is a different paper (arXiv 2604.07870) with a different mechanism (time-series aggregate timing from cross-sectional realized-skewness dispersion vs. cross-sectional beta pricing of option-implied fear factors).
- `crypto-market-volatility-beta-negative-premium-cross-sectional-2026-09-17.md` — analogous “negative premium on volatility-beta exposure” thesis implemented in crypto at market level, not firm-level option-implied common factors.
- `expected-shortfall-factor-model-common-tail-loss-severity-2026-09-11.md` — cites Baruník & Nevrla quantile factors; different mechanism (tail-loss severity factor model).

## Sources

1. Jozef Baruník, Mattia Bevilacqua, Michael Ellington, *"Common Firm-level Investor Fears: Evidence from Equity Options"*, arXiv preprint **arXiv:2309.03968v1 [q-fin.GN]**, submitted 7 September 2023 (PDF dated September 11, 2023; 50 pages; SHA-256 `d13c52a158bdfcfca4d6cdeee86adc5c8a269947035fbd907718bda116c315bc`). https://arxiv.org/abs/2309.03968 ; arXiv-issued DOI `10.48550/arXiv.2309.03968` (resolves to the abstract page, verified 2026-09-24). Preprint only: no Comments, no `journal_ref`, no publisher DOI on the abstract page as of 2026-09-24.
