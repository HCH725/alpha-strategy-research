---
schema: strategy-research-record-v1
title: AR-HMM regime-switching cointegration-spread statistical arbitrage on Brent, Shanghai and WTI crude oil futures (three-contract hedge when pairwise cointegration fails)
created: 2026-09-30
updated: 2026-09-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-30
sources:
  - "arXiv:2309.00875v3 landing page https://arxiv.org/abs/2309.00875v3 (captured 2026-09-30, 41722 bytes, SHA-256 ee863cf79f83666e4ee535a8ac29f7a66ad896247dc366f140c9575173343f3c)"
  - "arXiv:2309.00875v3 PDF https://arxiv.org/pdf/2309.00875v3 (captured 2026-09-30, 768717 bytes, SHA-256 749f3deacd54dede22e08dc0a31e5814853afe7930f2a9bd4667fe53a3b589e4)"
  - "arXiv API record https://arxiv.org/abs/2309.00875v3 via https://export.arxiv.org/api/query?id_list=2309.00875 (captured 2026-09-30, 2699 bytes, SHA-256 67aa6a3874f7acbffcb43724d7b65f4c0a1a826f1299a7fb5b20bd1b6cd66f51)"
  - "arXiv:2309.00875v1 PDF https://arxiv.org/pdf/2309.00875v1 (captured 2026-09-30, 1076209 bytes), read only to establish that the landing/API abstract is the v1 abstract"
  - "arXiv:2309.00875v2 PDF https://arxiv.org/pdf/2309.00875v2 (captured 2026-09-30, 734075 bytes), read only to establish that the v2 abstract is a third, intermediate variant"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "arXiv landing-page and arXiv API abstract (identical to the v1 PDF abstract) state that statistical arbitrage strategies involving the three traditional crude oil futures Brent, WTI and Dubai 'do not yield profitable investment opportunities', while the pinned v3 PDF Table 8 reports statistically significant positive performance for exactly those traditional instruments: Brent-Dubai plain-vanilla Sharpe 1.8001 with three stars and Brent-WTI-Dubai PredI Sharpe 1.5607 with three stars, both at the 1% level, and the v3 abstract itself claims the opposite finding as point (iii). The landing/API abstract is therefore stale v1 metadata for a v3 pin; this record treats the v3 PDF abstract and v3 tables as authoritative and records the landing/API abstract as stale."
---

# AR-HMM regime-switching cointegration-spread statistical arbitrage on Brent, Shanghai and WTI crude oil futures (three-contract hedge when pairwise cointegration fails)

## Provenance

**Primary source identity.** arXiv:2309.00875v3, exact title `A hidden Markov model for statistical arbitrage in international crude oil futures markets`, landing `https://arxiv.org/abs/2309.00875v3`, PDF `https://arxiv.org/pdf/2309.00875v3`.

**Complete author list, exactly as the source, in source order.** `Viviana Fanelli`, `Claudio Fontana`, `Francesco Rotondi`. The same three names in the same order appear (a) as three `citation_author` meta tags on the landing page (`Fanelli, Viviana` / `Fontana, Claudio` / `Rotondi, Francesco`), (b) as three `<author><name>` entries in the arXiv API feed (`Viviana Fanelli`, `Claudio Fontana`, `Francesco Rotondi`), and (c) as the submitting author in the landing submission history (`From: Francesco Rotondi`). No fourth author, no trailing `et al.`, no consortium line.

**Version and date.** Landing `citation_date` is `2023/09/02`. Landing dateline reads verbatim `[Submitted on 2 Sep 2023 (v1), last revised 13 Feb 2026 (this version, v3)]`. Submission history gives `[v1] Sat, 2 Sep 2023 09:35:00 UTC (929 KB)`, `[v2] Fri, 20 Sep 2024 13:50:03 UTC (626 KB)`, `[v3] Fri, 13 Feb 2026 10:06:35 UTC (273 KB)`; the parenthesised kilobyte figures are arXiv's submission-package sizes, not PDF byte counts. The API returns one entry with `published` `2023-09-02T09:35:00Z` and entry `updated` `2026-02-13T10:06:35Z`, consistent with v3. The pinned PDF is therefore the 2026-02-13 v3, not the 2023 v1.

**Publication / preprint status.** The landing page has no `Comments` row (0 occurrences of `Comments`), no `Journal-reference` row (0 occurrences), and no publisher DOI cell; the API feed carries no `arxiv:comment`, no `arxiv:journal_ref` and no `arxiv:doi`. `peer` occurs 0 times on the landing page. Publication status is therefore **preprint only, peer-review status not stated in source**. The landing sidebar does carry `arXiv-issued DOI via DataCite` with `10.48550/arXiv.2309.00875`; this is an arXiv/DataCite identifier, not a journal DOI. Licence is **CC BY 4.0** (`creativecommons.org/licenses/by/4.0/`). Subjects are **`General Finance (q-fin.GN)` only** (primary category `q-fin.GN`); there is no `q-fin.ST`, `q-fin.TR` or `math.PR` cross-list.

**Pinned artefact digests (all computed this run on the captured bytes).**

- v3 PDF: **768,717 bytes**, SHA-256 `749f3deacd54dede22e08dc0a31e5814853afe7930f2a9bd4667fe53a3b589e4`, extracted with pypdf 6.16.2 into **31 pages**, a raw text layer of **96,272 characters** containing 4 embedded NUL bytes, **96,268 characters** after removing them, over **1,853 newline-separated lines** (1,854 counting the trailing empty line), read end to end: Abstract, Sections 1 to 5, Equations (2.1), (2.2), (2.3), (2.8), (3.1) to (3.4), (4.1), (4.2), Remark 2.1, Remark 2.2 parts (1) to (6), Remark 3.1, Remark 3.2, Remark 4.1, Remark 4.3, Tables 1 to 8 with every printed cell, Figures 1 to 10 captions, the Acknowledgment block and the full reference list.
- landing HTML: **41,722 bytes**, SHA-256 `ee863cf79f83666e4ee535a8ac29f7a66ad896247dc366f140c9575173343f3c`.
- API XML: **2,699 bytes**, SHA-256 `67aa6a3874f7acbffcb43724d7b65f4c0a1a826f1299a7fb5b20bd1b6cd66f51`.
- canonical spec read this run: `quant/strategy-research-record-spec-v1.md`, **10,289 bytes**, SHA-256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`; `quant/strategy-research-record-spec-v2.md` returned file-not-found, so this run failed closed onto v1.

**Text-layer caveats recorded and not reconciled.** The PDF is a LaTeX text layer; Greek letters and math alphabets are extracted as visual-lookalike Unicode code points, so the bandwidth level, the cointegration vector, the bold transition matrix and the three parameter vectors all come back as lookalike glyphs rather than as ASCII names, hyphenation is hard-wrapped across lines (`pa-` / `rameters`), and the VAR/VECM coefficient matrices are emitted as vertical column fragments rather than as aligned rows. Every numeric cell quoted in this record was located verbatim in that text layer after whitespace and Unicode normalisation, and row/column identity was re-checked against the surrounding table caption rather than inferred from position alone.

**Stale-metadata finding (this run's main provenance discovery, and the basis for `contested: true`).** The arXiv landing `citation_abstract`-equivalent block and the arXiv API `<summary>` are byte-for-byte the same text, and that text is the **v1** PDF abstract: it ends with `On the contrary, statistical arbitrage strategies involving the three traditional crude oil futures (Brent, WTI, Dubai) do not yield profitable investment opportunities.` The **v2** PDF abstract is a third, softened variant (`... deliver a lower investment performance.`). The **v3** PDF abstract is a fourth text with three numbered findings: `(i) Shanghai futures can be profitable even under conservative levels of transaction costs; (ii) strategies based on our model outperform those relying solely on observed spread values; (iii) incorporating three futures contracts enables the implementation of arbitrage strategies even in cases where pairwise cointegration is not detected.` Only `v1`/`v2`/`v3` PDFs differ; the landing and API never advanced past v1. **This record cites the v3 PDF abstract and v3 tables as authoritative and treats the landing/API abstract as stale metadata for the pinned version.**

**Deduplication (hidden-inclusive, deterministic source-identity search).** `rg -uuu` across the entire checkout including `.git`, `.mimo-worktrees`, `.agents`, `.hermes` and `coverage_manifest.csv` returned **0 files** for every one of `2309.00875`, `Fanelli`, `Rotondi`, `Claudio Fontana`, `OLDUB1M`, `SICC.01`, `NCLC.01`, `LLCC.01`, and the exact title substring `hidden Markov model for statistical arbitrage`. `coverage_manifest.csv` (5,808 lines) returned 0 hits for `2309.00875` and `Fanelli`. A broader mechanism scan for `PredI`, `ProbI`, `predicted increments`, `Shanghai crude oil` and `INE crude` returned only `options-physical-crash-frontier-socp-finite-quotes-2026-09-02.md` (plus two `.mimo-worktrees` copies of the same file), whose only match is the unrelated phrase `crash probability interval` inside an options-pricing record; no strategy token collides. Positive control `novy-marx` matched **56 files** case-insensitively before this write, confirming the scan is not silently failing. `git log --oneline -20` was used as a convenience glance only. The candidate was re-checked against the whole checkout immediately before writing, not against recent commits alone.

## Economic mechanism

### Source-reported

The authors' stated chain is: (1) Brent, Shanghai and WTI nearest-maturity futures prices are **cointegrated**, so a linear combination `S_t = lambda_0 + sum_i lambda_i F^i_t` (Equation 2.1) is stationary and mean-reverting; (2) because the cointegration vector is documented elsewhere to suffer structural breaks (Caporin et al. 2019, Lee and Papanicolaou 2016), the spread is modelled as a **regime-switching autoregressive process of order one modulated by an unobservable Markov chain** (Equation 2.2, `S_{t+1} = gamma(X_t) + alpha(X_t) S_t + eta(X_t) z_t`), which the authors note is the discrete-time observation-frequency representation of an OU-HMM (Remark 2.1, Equation 2.3); (3) parameters are re-estimated **online** with a filter-based EM algorithm, batched every `m = 10` steps, so the model tracks the market; (4) the model's one-step-ahead conditional mean and variance define forecast bands that time entries, and a spread sign change times exits; (5) the source states three empirical findings in the v3 abstract - Shanghai-inclusive strategies stay profitable at conservative transaction costs, model-based strategies beat purely observation-based ones, and **three contracts allow execution where pairwise cointegration is absent**. Section 4.3 reports that `WTI-Dubai`, `Shanghai-WTI` and `Brent-WTI` show no pairwise cointegration under Johansen and, when that fails, under Engle-Granger with either choice of dependent variable (footnote 9), which is the stated justification for the three-contract construction.

The VECM evidence the authors give for the direction of adjustment is that in Equation (4.1) the adjustment coefficient on the spread is `0.419` with standard error `0.121` and three-star 1% significance **only in the `Delta F^S` equation**, while the corresponding coefficients `0.059 (0.151)` and `0.063 (0.149)` in the Brent and WTI equations are not significant; they read this as unidirectional long-run causality running from Brent and WTI into Shanghai, and as evidence that Shanghai is the stabilising, reversion-catching leg.

### Research interpretation

Falsifiable restatement, with component roles separated:

```text
Cointegration structure: Johansen rank-1 hedge among three same-underlying
  futures, weights from a weekly-frequency VECM estimated on the training
  window only -> portfolio construction (not the alpha).
Regime / forecast engine: 2-state Gaussian AR-HMM on the daily spread,
  online filter-based EM -> conditional mean and variance used to place the
  bands (the actual predictive object).
Entry trigger (research label: source-reported): observed spread outside the
  alpha-bandwidth interval around the model or sample centre.
Exit (research label: source-reported): spread sign change, first discrete
  crossing of zero.
Sizing / normalisation (research label: source-reported): cointegration
  vector scaled by gross notional exposure G_t = |lambda_0| + sum_k |lambda_k| F^k_t.
Cash (research label: source-reported): uninvested balance earns zero
  interest; reported returns are treated as excess returns.
```

The hypothesised economic channel is **deviation-and-reversion in a shared-underlying futures basis**, amplified by a latent-regime conditioning variable: if the spread's conditional variance and conditional mean genuinely switch between two persistent states (baseline `pi_11 = 0.8588`, `pi_22 = 0.9732`), then a band placed on the *filtered* distribution admits fewer false entries than a band placed on unconditional sample moments, and the residual edge survives the Shanghai contract's 53.71 bp cost because entries are infrequent enough. A competing non-alpha explanation is that the reported edge is beta to a single one-year oil path plus a favourable choice of `alpha` in a 5-by-5 grid with no multiplicity control; the falsification plan below is built to separate these.

## Signal

**Formation timestamp.** Daily. The spread `S_t`, the bands and the position decision are all dated `t` in the source's own indexing; the source does not state an exchange session, a timezone, a closing-price convention, or a settlement-versus-settlement alignment for `t`. Timezone and publication/availability convention: **data gap**.

**Lookback / estimation windows.**

- Cointegration weights: **weekly** prices, Johansen trace test with a constant in the cointegrating relationship, `VAR(p)` lag order chosen by Schwarz IC, `p = 2`, all estimated on the training sample only (`t_0 = 03/26/2018` to `t_B = 07/01/2022`); daily-frequency cointegration results are pushed to Supplementary Materials that are **not present in the pinned PDF** (data gap).
- AR-HMM: **daily** spread series built from the weekly-estimated weights; `N` chosen from `{1,2,3}` by minimising a mean forecast error over "the trading sample", yielding `N = 2` "in the training sample" (the phrasing does not identify whether the scoring window is the training window or the full test window - **underspecified**, see negative evidence 8).
- Model-parameter batch: `m = 10` (parameters updated every two weeks); denominator truncation at 10x the previous estimate; initial state `X_hat_0 = e_1`; `pi_hat_11(0) = 0.6`, `pi_hat_22(0) = 0.5`; OLS initialisation for `gamma, alpha, eta` on the **first 20 datapoints** of the spread (twice `m`), with `N = 2` seeds at `1.3x` and `0.7x` of those OLS estimates (Remark 2.2 parts (1), (2), (5), (6)).
- ProbI rolling moments: sample mean and standard deviation over `t-1-n : t-1`, with **`n` never printed anywhere in the source** - **underspecified**.
- RI / PI empirical quantile `q_{alpha/2,x}` of the spread increment `x_t = S_t / S_{t-1} - 1`: **the estimation window for the empirical quantile is never printed** - **underspecified**.

**Entry (source-reported).** Assume no open position at `t-1`. Let `q_{alpha/2}` be the `alpha/2` quantile of the standard normal and `alpha` the bandwidth level.

- PV: open at `t` if `S_t != 0` (Burgess 1999 benchmark).
- ProbI: open at `t` if `S_t` is outside `(mu_hat_{t-1-n:t-1} +/- |q_{alpha/2}| * sigma_hat_{t-1-n:t-1})`; equivalently the rolling z-score `z_t` is outside `(-q_{alpha/2}, +q_{alpha/2})` (Bollinger-band / Avellaneda-Lee form).
- PredI: open at `t` if `S_t` is outside `(E[S_t | F_{t-1}] +/- |q_{alpha/2}| * sqrt(Var[S_t | F_{t-1}]))`, where `E[S_t | F_{t-1}] = gamma_hat(X_hat_{t-1}) + alpha_hat(X_hat_{t-1}) * S_{t-1}` and `Var[S_t | F_{t-1}] = (eta_hat(X_hat_{t-1}))^2` (Elliott et al. 2005 inspired).
- RI: open at `t` if `x_t` is outside `(-|q_{alpha/2,x}|, +|q_{alpha/2,x}|)` with `x_t = S_t / S_{t-1} - 1` (Dunis et al. 2006 inspired).
- PI: open at `t` if the predicted increment `x_hat_t = E[S_{t+1} | F_t] / S_{t-1}` is outside `(-|q_{alpha/2,x}|, +|q_{alpha/2,x}|)`.

**Direction (source-reported).** `S_t > 0` -> short the portfolio `lambda`; `S_t < 0` -> long `lambda`. An opening at `t` generates an immediate cash inflow of `|S_t|`.

**Exit (source-reported).** A position opened at `t-1` is closed at `t` if `S_t` changes sign, i.e. the first discrete crossing of zero. No stop-loss, no take-profit, no time stop, no partial exit; when no signal is active the strategy holds no futures and returns exactly zero.

**Holding period (source-reported).** Unbounded above; in the test sample the completed-trade counts `N_TW` are 37 / 24 / 12 / 30 / 35 for PV / ProbI / PredI / RI / PI at `alpha = 0.20`, i.e. PredI completes only 12 trading windows across a 261-day test year (average about 21.75 test days per PredI trade). Non-overlapping trading windows are defined explicitly by `(sigma_j, tau_j)` in Section 3.2.

**Parameters.** `alpha` grid is source-reported as `0.30`, `0.25`, `0.20` (baseline for every downstream experiment), `0.15`, `0.05`, described as bands from about one standard deviation down to about two. Everything else in this section is either source-reported as quoted or explicitly marked `underspecified`. No entry threshold, exit rule, stop, sizing rule or filter in this section is Scout-invented; where the source is silent the field is marked `data gap` rather than filled.

**Overall signal status: partially specified.** Portfolio construction, direction, exit, normalisation and the `alpha` grid are fully reconstructable; ProbI's rolling window `n`, RI/PI's empirical-quantile window, the trading timestamp convention, and the execution price/lag are **underspecified** and must not be presented as reproducible evidence.

## Required data

- **Instrument / universe:** four continuous near-month futures series built from the nearest monthly maturity - Datastream mnemonics `LLCC.01` (Brent), `NCLC.01` (WTI), `SICC.01` (Shanghai crude oil, converted from CNY to USD), `OLDUB1M` (Dubai, used only in Section 4.3 / Table 8). Universe inclusion rule is "these four named series", not a filtered cross-section; there is **no liquidity, volume, open-interest or minimum-tick filter**, no survivorship handling and no reconstitution schedule (the universe is static and defined by vendor mnemonics).
- **Venue / market type:** exchange-traded crude oil futures across ICE (Brent), CME/NYMEX (WTI), INE (Shanghai) and ICE/Dubai; the source names **Datastream** as the vendor and does not name the exchanges (exchange attribution is Scout interpretation).
- **Timeframe:** daily prices and weekly prices; cointegration on weekly, filtering, parameter estimation and trading on daily.
- **Fields used:** settlement/last futures prices only. No volume, no open interest, no order book, no funding, no borrow, no on-chain, no sentiment fields. Bid-ask enters only as an ex-post cost parameter (Table 1), not as a tradable field.
- **Point-in-time / train-test boundary:** `t_0 = 03/26/2018` to `T = 06/30/2023`, `1,373` daily and `273` weekly observations; break `t_B = 07/01/2022`; **test sample is 261 daily and 52 weekly observations (one year)**; training is therefore 1,112 daily observations (1,373 minus 261, arithmetic only). Cointegration weights and all initialisation are estimated on the training side; the source states the cointegration vector is estimated in-sample and evaluated out-of-sample. Point-in-time audit of the Datastream continuous-series roll rule: **data gap** (roll rule, roll date and roll cost are never printed; the source only argues verbally that roll yield largely cancels because the cointegrating coefficients sum near zero).
- **Timestamp:** no timezone, no clock source, no precision, no out-of-order treatment is stated - **data gap**.
- **Missing data:** no null / stale / suspended / bad-print handling rule is stated - **data gap**. The source does note that cointegration is re-tested across windows and that some `(t_0)` windows yield *no* cointegration at all (Figure 9 missing data points), which is a form of implicit sample failure rather than a fill rule.
- **Funding / fee / spread needs:** observed = average daily half bid-ask spread by contract (Table 1). Modelled = a per-contract scalar `c_i` charged on trades. Omitted = slippage, commission, exchange and clearing fees, financing, margin interest, borrow, market impact, latency, partial fills, and any dependence of cost on order size or participation.

## Execution assumptions

Cost treatment was determined at Methods level from Section 3.1, Section 3.2, Section 4.1.1, Section 4.2, Section 4.3, Section 4.4.1 and Table 1, plus a whole-document census of the pinned 96,268-character text layer: `transaction cost(s)` 32/25, `bid-ask` 1, `margin call` 1, `impact` 5 (all five occurrences of `impact` are prose about model/data impact, none is a market-impact model), while `slippage` 0, `commission` 0, `fee`/`fees` 0, `funding` 0, `borrow` 0, `turnover` 0, `capacity` 0, `market impact` 0, `latency` 0, `order type` 0, `maker`/`taker` 0, `participation` 0, `fill` 0, `liquidity` 0, `leverage` 1 (a reference title only) - **every one of these is a data gap and must not be read as a zero.**

- **Cost model (source-reported).** Following Hain et al. (2018), each contract's `c_i` is the **average effective daily half bid-ask spread over the full sample period**, reported in Table 1 in basis points: **Brent 5.80, Shanghai 53.71, WTI 20.24, Dubai 1.52**. Table 8 states these per-contract costs are included again for every contract combination. Figure 8 rescales the whole cost vector by 80% to 120%.
- **Signal-to-order timing:** not stated. Opening and closing conditions are written on the same `t` at which the position is said to be opened/closed, with no next-bar, next-session or same-session rule - **underspecified**.
- **Order type / fill model:** not stated anywhere (0 occurrences) - **data gap**. No limit/market distinction, no partial fills, no queue position, no slippage.
- **Leverage / margin / financing:** futures margin is never quantified; `margin call` appears once, in risk prose only. Idle cash earns **zero interest** "for simplicity of presentation"; returns are declared **excess returns**, and the Sharpe numerator does not subtract a risk-free rate. No financing cost on the futures leg is modelled - **data gap**.
- **Position limits / capacity / participation:** not stated (0 occurrences) - **data gap**.
- **Borrow / shorting:** the short leg is a futures short; no borrow fee, no locate, no short-sale constraint - **data gap**.
- **Failure handling:** none stated - **data gap**.
- **Annualisation.** Returns are annualised by the source's printed rule `R * 250 / n` (Section 3.2, the string `250` occurs exactly once in this sense). The Sharpe ratio is declared to be expressed "in annual terms" but **no annualisation factor for SR is printed anywhere** (`sqrt` occurs 0 times) - **underspecified / data gap**.

All printed performance figures below are therefore **net of the Table 1 scalar half-spread cost only, and gross of everything else**; the source does not label them gross or net, so this record does not upgrade them to "net of costs".

## Evidence

### Source-reported

Every figure below is source-reported, traced to the pinned v3 PDF, and **has not been independently reproduced**. Asset class is **traditional commodity futures plus one equity-index and one commodity-ETF passive benchmark**; none of it is crypto evidence.

**Sample and split.** `t_0 = 03/26/2018`, `T = 06/30/2023`, 1,373 daily / 273 weekly; `t_B = 07/01/2022`; test 261 daily / 52 weekly (Section 4.1.1, Section 4.2).

**Table 1 - transaction cost parameters `c_i` (bps, full-sample average daily half bid-ask spread, following Hain et al. 2018).** Brent 5.80, Shanghai 53.71, WTI 20.24, Dubai 1.52. Prose benchmark: the source says these sit between the roughly 20 bps of Alizadeh and Nomikos (2008) and roughly 60 bps of Do and Faff (2012).

**Table 2 - unit-root p-values on weekly prices.** ADF: Brent 0.9434, Shanghai 0.8535, WTI 0.9423. PP: 0.8788, 0.8413, 0.8714. Breakpoint Perron: 0.9548, 0.9471, 0.9425 (lag length by Schwarz IC) - all consistent with a unit root.

**Table 3 - Johansen trace test (constant in the cointegrating relation).** `r = 0`: statistic 35.5106 vs critical 29.7976, p = 0.0099; `r <= 1`: 10.0981 vs 15.4948, p = 0.3074; `r <= 2`: 0.8131 vs 3.8415, p = 0.5153. Exactly **one** cointegrating relationship. VAR order `p = 2` by Schwarz IC, described as stable (roots of the characteristic equation) and "quite stable" across different `t_0`/`t_B`.

**Equation (4.1) VECM, adjustment column.** Spread-adjustment coefficients `0.059 (s.e. 0.151)` for `Delta F^B`, `0.419*** (0.121)` for `Delta F^S`, `0.063 (0.149)` for `Delta F^W`; lagged-difference terms generally insignificant, which the source reads as short-run causality being weak and long-run causality running Brent/WTI -> Shanghai.

**Equation (4.2) - the tradable spread on the test sample.** `S_t = F^B_t - 0.6982 F^S_t - 0.3402 F^W_t + 0.4322`. The source states ADF and PP reject a unit root on `S` while KPSS does not reject stationarity (exact test statistics for these three are **not printed** - data gap).

**Table 4 - AR-HMM parameter point estimates at the end of the training sample.** `baseline` row: `pi_11 0.8588`, `pi_22 0.9732`, `gamma_1 0.4705`, `alpha_1 0.6214`, `eta_1 1.8343`, `gamma_2 0.0855`, `alpha_2 0.8164`, `eta_2 1.2187`. Across 100 random initialisations: `mean` 0.9255 / 0.9627 / 0.4504 / 0.6426 / 1.5606 / 0.0600 / 0.8049 / 1.2777; `std. dev.` 0.0583 / 0.0559 / 0.0948 / 0.1319 / 0.4821 / 0.0587 / 0.0405 / 0.0951; `t-ratio` 15.87 / 17.21 / 4.75 / 4.87 / 3.24 / **1.02** / 19.85 / 13.44. The source explicitly flags `gamma_2` as close to zero and weakly determined, and states this has negligible impact because strategies are driven by opening signals.

**Table 5 - full performance grid, Brent-Shanghai-WTI test sample, `alpha = 0.20` block (baseline).** Columns are `PV, ProbI, PredI, RI, PI, Ex. S&P, Ex. ETF`.

| row | PV | ProbI | PredI | RI | PI | Ex. S&P | Ex. ETF |
|---|---|---|---|---|---|---|---|
| R | -0.0091 | 0.1043 | 0.1518 | -0.0244 | 0.0230 | 0.1174 | -0.2847 |
| SR | -0.0025 | 0.8335* | 1.1792* | -0.1508 | 0.2359 | 0.6729 | -0.7436 |
| p-val. SR test | 0.5125 | 0.0765 | 0.0615 | 0.635 | 0.3790 | 0.2360 | 0.8710 |
| N_TW | 37 | 24 | 12 | 30 | 35 | - | - |
| mean R_TW | -0.0002 | 0.0042** | 0.0120** | -0.0008 | 0.0007 | - | - |
| p-val. R_TW | 0.9053 | 0.0251 | 0.0467 | 0.6547 | 0.7013 | - | - |
| % R_TW > 0 | 0.5135 | 0.6667 | 0.8333 | 0.4000 | 0.5714 | - | - |
| p-val. WRC | 0.0650, best from WRC: PredI* | | | | | | |

Significance stars are 10% / 5% / 1%. Under the baseline specification **PredI's Sharpe of 1.1792 is significant only at 10% (p = 0.0615)**, ProbI's 0.8335 only at 10% (p = 0.0765), the White Reality Check p-value is 0.0650 with best strategy PredI at 10%, and PV and RI are negative. Other `alpha` blocks in Table 5, read cell by cell: `alpha = 0.30` ProbI R 0.1055 / SR 0.8151* / p 0.0795, PredI R 0.1394 / SR 1.1010* / p 0.0605, RI R -0.0471 / SR -0.3137, PI R 0.0174 / SR 0.1955, WRC p 0.0745 best PredI*; `alpha = 0.25` ProbI R 0.1043 / SR 0.8335* / p 0.0765, PredI R 0.1668 / SR 1.2562** / p 0.0360, RI R -0.0432 / SR -0.2909, PI R 0.0243 / SR 0.2458, WRC p 0.0360 best PredI**; `alpha = 0.15` ProbI R 0.0572 / SR 0.5171, PredI R 0.1632 / SR 1.3032** / p 0.0180, RI R 0.0206 / SR 0.2373, PI R 0.0416 / SR 0.3685, WRC p 0.0335 best PredI**; `alpha = 0.05` ProbI R 0.0559 / SR 0.7556, PredI R 0.0729 / SR 0.7244, RI R -0.0020 / SR -0.0319, PI R 0.1994 / SR 1.3136** / p 0.0135, WRC p 0.0110 best PI**. Note the non-monotone pattern: PredI is best at `alpha` 0.15-0.25 and *loses* to PI at `alpha = 0.05`.

**Table 6 - initialisation robustness, 100 randomised runs.** PredI `baseline` R 0.1518 / SR 1.1792 / mean R_TW 0.012; `mean` 0.1679 / 1.2718 / 0.0125; `std. dev.` 0.0349 / 0.254 / 0.0033; `t-ratio` 4.808 / 5.008 / 3.8159. PI `baseline` 0.023 / 0.2359 / 0.0007; `mean` 0.0374 / 0.3406 / 0.0012; `std. dev.` 0.0094 / 0.0706 / 0.0005; `t-ratio` 4.0001 / 4.8235 / 2.484.

**Table 7 - risk, stationary bootstrap (Politis-Romano, 2,000 replications, expected block length 20), Brent-Shanghai-WTI, `alpha = 0.20`.**

| row | PV | ProbI | PredI | RI | PI | Ex. S&P | Ex. ETF |
|---|---|---|---|---|---|---|---|
| VaR99% | -2.5078% | -2.5078% | -2.5078% | -2.6663% | -2.5078% | -2.8106% | -5.3009% |
| VaR95% | -1.5197% | -1.3472% | -1.3178% | -1.4422% | -1.5197% | -1.7337% | -3.8152% |
| VaR90% | -1.1033% | -1.0294% | -0.8052% | -1.0294% | -1.1033% | -1.3019% | -3.1380% |
| ES99% | -2.7297% | -2.7297% | -2.7297% | -2.8093% | -2.7297% | -3.5073% | -6.9106% |
| ES95% | -1.8981% | -1.8324% | -1.8155% | -1.896% | -1.8981% | -2.435% | -5.0296% |
| ES90% | -1.5848% | -1.5259% | -1.4400% | -1.5728% | -1.5848% | -1.9961% | -4.2791% |
| MDD | -10.1668% | -6.3788% | -5.7282% | -10.7311% | -9.3580% | -15.5447% | -39.4747% |

The source itself notes that at the 99% level the scarcity of extreme observations limits empirical discrimination.

**Table 8 - contract-combination robustness, `alpha = 0.20`, Ledoit-Wolf and t-test p-values replaced by star notation.** Benchmark passive rows are omitted by the source but printed in the prose: S&P `R 11.74%, SR 0.6729`; ETF `R -28.47%, SR -0.7436`.

| combination | PV SR | ProbI SR | PredI SR | RI SR | PI SR | WRC p / best |
|---|---|---|---|---|---|---|
| Brent-Shanghai-WTI | -0.0025 | 0.8335* | 1.1792* | -0.1508 | 0.2359 | 0.065 / PredI* |
| Brent-Shanghai | 0.7561* | 0.6382 | 1.7738*** | 0.2856 | 0.9302* | 0.011 / PredI** |
| Brent-Dubai | 1.8001*** | 1.3823** | 1.5267*** | 1.1975* | 1.8156*** | 0.0035 / PI*** |
| Brent-Shanghai-Dubai | 1.229** | 0.5189 | 0.915** | 0.053 | 1.3569** | 0.0135 / PI** |
| Brent-WTI-Dubai | 1.4469** | 1.007* | 1.5607*** | 0.8929 | 1.4864** | 0.009 / PredI*** |
| Brent-Shanghai-WTI-Dubai | 1.4311*** | 0.7912* | 0.8691* | 0.1657 | 1.5781*** | 0.004 / PI*** |

Corresponding returns R, read from the same table: Brent-Shanghai-WTI `-0.0091 / 0.1043 / 0.1518 / -0.0244 / 0.023`; Brent-Shanghai `0.1316 / 0.104 / 0.3621 / 0.0359 / 0.1711`; Brent-Dubai `0.1478 / 0.099 / 0.1214 / 0.0692 / 0.1479`; Brent-Shanghai-Dubai `0.1014 / 0.0329 / 0.0692 / 0.0014 / 0.1129`; Brent-WTI-Dubai `0.113 / 0.069 / 0.122 / 0.0511 / 0.1163`; four-contract `0.1206 / 0.0554 / 0.0636 / 0.0085 / 0.1343`. Mean trading-window returns for the highest cells: Brent-Shanghai PredI `0.0225***`, Brent-WTI-Dubai PredI `0.007***`, four-contract PI `0.0045***`. The source's own reading: **one of PredI or PI is always the WRC best-performing strategy**, and pairwise cointegration is absent for `WTI-Dubai`, `Shanghai-WTI` and `Brent-WTI`.

**Statistical machinery.** Ledoit and Wolf (2008) Sharpe-ratio test against `H_0: SR = 0` implemented with a **fixed-size circular block bootstrap, 2,000 replications, 20 blocks**; standard t-test on trading-window returns; **White Reality Check** (White 2000, implemented following Sullivan et al. 1999) with the **stationary bootstrap of Politis and Romano (1994), 2,000 replications, average block length 20**, benchmarked against a zero-return investment; stationary bootstrap for VaR/ES/MDD with 2,000 replications and expected block length 20; 100 randomised-EM runs for initialisation robustness. Census of the pinned text: `p-value` 9, `significan` 22, `bootstrap` 12, `White Reality` 3, `t-ratio` 4, while `benjamini` 0, `bonferroni` 0, `holm` 0, `fdr` 0, `multiple test` 0, `seed` 0, `walk-forward` 0, `holdout` 0, `point-in-time` 0, `survivorship` 0, `source code` 0, `github` 0, `data availability` 0, `software` 0, `matlab` 0, `python` 0.

**Source's own framing of magnitude.** Section 4.2 states the reported returns are consistent with Hain et al. (2018), who document roughly 6%-8% annual excess returns for this class of commodity-futures statistical arbitrage.

### Independently reproduced

`not independently reproduced`

Arithmetic-only consistency checks run this session (explicitly **not** a reproduction, no market data downloaded, no strategy executed): 1,373 minus 261 equals 1,112 training days; 261 daily observations equal 250 trading days plus 11 calendar-day residual, i.e. the source's "a year of observations"; the Table 5 `alpha = 0.20` block and the first block of Table 8 are cell-for-cell identical as the Table 8 caption claims (R `-0.0091 / 0.1043 / 0.1518 / -0.0244 / 0.023`, SR `-0.0025 / 0.8335* / 1.1792* / -0.1508 / 0.2359`, WRC `0.065`), confirming no cross-table transcription drift; 12 PredI trading windows over 261 test days implies about 21.75 days per trade; the three non-cointegrating pairs named in Section 4.3 match the six Table 8 blocks (three two-contract blocks minus the Brent-Shanghai one that *is* cointegrated, plus Brent-WTI which is not offered as a Table 8 block); and the whole-document census counts quoted above were recomputed against the extracted text layer and matched the counts claimed in this record.

### Negative evidence

1. At the baseline specification the headline strategy's Sharpe is significant only at the 10% level (`p = 0.0615`), the runner-up only at 10% (`p = 0.0765`), and the White Reality Check p-value is `0.0650` - none clears a conventional 5% bar.
2. The test sample is 261 daily observations, one year, spanning `07/01/2022` to `06/30/2023` - a window that contains the 2022 oil-price peak and the subsequent decline. No second out-of-sample window, no walk-forward, no holdout beyond this single split, and no post-2023 data despite a 2026 posting.
3. `N_TW = 12` for the baseline PredI strategy means 12 completed trades support the headline Sharpe; the trading-window t-test on those 12 observations has `p = 0.0467`.
4. Two of the five strategies are unprofitable at baseline: PV `R = -0.0091, SR = -0.0025` and RI `R = -0.0244, SR = -0.1508`; RI is negative at `alpha` 0.30, 0.25 and 0.05 as well, and the source states RI "fails to deliver consistent profitability and is never statistically significant".
5. The `alpha` grid (5 values) x strategy (5) x contract-set (6) comparison family has **zero multiplicity control**: `benjamini`, `bonferroni`, `holm`, `fdr`, `multiple test` all occur 0 times, so the star notation is unadjusted across at least 150 reported cells.
6. No seed, no code, no software package, no repository, no data-availability statement (`seed` 0, `source code` 0, `github` 0, `software` 0, `matlab` 0, `python` 0, `data availability` 0) - the "100 randomised runs" cannot be re-executed and the randomisation distribution is unrecoverable.
7. Cost coverage is one scalar half-spread per contract: `slippage` 0, `commission` 0, `fee`/`fees` 0, `funding` 0, `borrow` 0, `market impact` 0, `latency` 0, `turnover` 0, `capacity` 0, `liquidity` 0, `participation` 0. The Table 1 cost is itself the **full-sample average**, i.e. it uses the test period's own bid-ask behaviour - a point-in-time cost leak for a claimed out-of-sample result.
8. The state-count `N` is selected by minimising a mean forecast error "over the trading sample" while the result is reported as "the preferred specification in the training sample" - the selection window is not unambiguously identified as pre-test, so test-set leakage in the choice of `N = 2` cannot be ruled out from the text (**underspecified**).
9. Two strategy parameters are not printed at all: ProbI's rolling window `n` (Section 3.1 says only "a rolling window of n days") and RI/PI's empirical-quantile estimation window - neither strategy is independently reconstructable.
10. Execution timing, order type, fill model, signal-to-order delay, latency, partial-fill and failure handling are absent from the source (0 occurrences for `order type`, `latency`, `fill`, `maker`, `taker`), so the printed results cannot be attributed to a specified execution convention.
11. The Sharpe annualisation factor is never printed (`sqrt` occurs 0 times; only the return rule `R * 250/n` appears), so the SR scale cannot be verified from the text.
12. Point-in-time and survivorship treatment of the Datastream continuous near-month series is unstated: the roll rule, roll dates and roll costs are never printed; the source only argues verbally that roll yield cancels because coefficients sum near zero.
13. `alpha` is described as an "intermediate choice within the range commonly adopted" and is then fixed for every downstream experiment; because Table 5 shows PredI winning only in the middle of that grid and PI winning at `alpha = 0.05`, the headline is sensitive to a researcher-chosen bandwidth with no selection rule stated in advance.
14. The cointegration relationship is itself fragile by the source's own account: Figure 9 reports that shrinking the training window *rejects* cointegration outright (missing data points in the figure), and Section 4.4.2 states performance falls as `t_0` moves forward and that the dataset is significantly affected by COVID-19; Section 4.4.3 reports a small performance decline for `t_B` after January 2022 and a small increase after July 2022, i.e. the split date moves the answer.
15. The Sharpe ratio denominator includes the long idle stretches of zero returns, which the source itself says "may attenuate the Sharpe ratio ... potentially reducing the power of statistical Sharpe ratio tests based on daily returns" (Remark 4.2) - an author-stated reason the reported significance is conservative *and* an author-stated reason the trading-window statistics (which are higher) should not be substituted for it.
16. The benchmark set is thin: a passive S&P 500 excess return and one crude-oil ETF excess return, both with no transaction costs, versus five variants of the authors' own rule; there is no naive z-score pairs-trading baseline re-run on the same split, no buy-and-hold-spread baseline, and no "hold the cointegration vector without timing" control.
17. Publication status is preprint-only with no Comments, no journal reference and no publisher DOI; a three-version revision history (2023 -> 2024 -> 2026) in which the abstract was rewritten twice is a publication-bias and selectivity concern in its own right.
18. **Stale abstract contradicting the pinned tables** (see `contradictions` in the frontmatter): the abstract that arXiv actually serves for this record claims the traditional Brent/WTI/Dubai instruments are unprofitable, while v3 Table 8 reports Brent-Dubai PV SR `1.8001***` and Brent-WTI-Dubai PredI SR `1.5607***`. Anyone consuming the landing page or the API summary without opening the PDF would draw the opposite conclusion on the exact instruments this record is about.
19. Zero crypto content: `crypto` occurs once (a footnote citing Crepelliere et al. 2023 on cryptocurrency arbitrage), `bitcoin` 0, `perpetual` 0 - no crypto evidence exists in this source.
20. The daily-frequency cointegration analysis the source relies on to justify the daily trading loop is deferred to Supplementary Materials that are **not contained in the pinned PDF** (`supplementary` occurs twice, both as forward references), so that analysis cannot be checked from the primary artefact.
21. The Acknowledgment block (funding from the University of Padova STARS StG PRISMA and project P20224TM7Z) is present, but there is no conflict-of-interest statement, no data-availability statement and no author-contribution statement; the single occurrence of `conflict` in the text is the Russia-Ukraine conflict, not a disclosure.
22. No independent replication, third-party re-run or critical commentary on this specific source was found in this run; absence is not evidence of no negative result.

## Falsification plan

All thresholds below are **research-defined falsification thresholds** (or **research-proposed** for any operational choice the source does not print); none is source-reported. Data for every gate is the four Datastream near-month series (or a second vendor's equivalent) at daily and weekly resolution, plus per-contract bid-ask or spread data.

- **F1 - Printed-value reproduction.** Rebuild `S_t` from Equation (4.2) and re-derive Table 5 `alpha = 0.20`, Table 7 and Table 8 first rows. **Fail if** any of the Table 5 baseline cells (R, SR, p-val. SR test, N_TW, mean R_TW, p-val. R_TW, %R_TW>0), the Table 7 MDD row, or the Table 8 first-block row differs by more than 0.0005 in absolute value after matching the source's own annualisation rule. **Action:** stop; treat all other source numbers as unverified and do not proceed to F2-F14. *Currently not executable: no code, no seed, ProbI `n` and RI/PI quantile window missing - so this gate is open and blocking by construction.*
- **F2 - Stale-abstract / instrument-claim gate.** Explicitly test the landing/API claim: run Brent-Dubai and Brent-WTI-Dubai as the source's own Table 8 does, with the source's own costs. **Fail if** either traditional-instrument configuration produces a positive Sharpe significant at 5% or better in a re-run - that would confirm the v1 abstract is wrong for the current sample rather than the tables being wrong. **Action:** record which artefact (v1 abstract, v3 tables) is contradicted; never cite the landing abstract as the finding of this source.
- **F3 - Cost ladder.** Re-run the frozen signal with per-side costs of 0, 5, 10, 20, 50 bps applied uniformly and with the Table 1 vector scaled 80% to 120% as in Figure 8. **Fail if** baseline PredI net Sharpe falls below 0.50 at the source's own Table 1 vector, or below 0.00 at twice that vector. **Action:** reject the claim that the effect survives conservative costs; report only gross results thereafter.
- **F4 - Execution-timing gate (research-proposed).** Re-run assuming the signal dated `t` is executed at the next session's open, then with a 1-day and a 2-day signal-to-fill delay. **Fail if** baseline PredI Sharpe degrades by more than 0.30 absolute versus the same-day assumption. **Action:** mark the source's execution convention as outcome-determining; the result is not implementable as printed.
- **F5 - Out-of-sample extension.** Freeze every parameter at its training-sample value and run `07/01/2023` to the latest available date (minimum 24 additional months). **Fail if** the frozen rule's out-of-sample Sharpe is below 0.00 or if the cointegration rank test rejects rank 0 (no cointegration) at 5% inside the extension window. **Action:** reject the mechanism as regime-bound; reclassify as a 2018-2023 sample artefact.
- **F6 - Walk-forward stability.** Repeat the full `t_0`/`t_B` sweep with an expanding training window and a rolling 12-month test window, recording every window. **Fail if** fewer than 60% of windows produce a positive PredI Sharpe. **Action:** report the strategy as split-date sensitive; cite Figure 9 and Figure 10 as the source's own prior warning.
- **F7 - Baseline and ablation gate.** Compare against (a) the plain PV rule, (b) a static Bollinger/z-score rule with the rolling window `n` explicitly set (research-proposed: `n = 252`), (c) an untimed hold of the cointegration vector, (d) an always-flat book. **Fail if** the AR-HMM PredI rule does not beat every one of (a), (b), (c) on Sharpe after F3 costs. **Action:** the alpha is attributable to the hedge, not to the HMM; downgrade the mechanism claim.
- **F8 - Model-vs-observation ablation.** The source's own claim (ii) is that model-based beats observed-based. Test PredI versus ProbI and PI versus RI at every `alpha` on identical windows. **Fail if** PredI does not beat ProbI in a majority of `alpha x contract-set` cells, or if the sign of the difference flips in more than one third of cells. **Action:** withdraw claim (ii) and treat the HMM as optional decoration.
- **F9 - Parameter-perturbation gate.** Perturb `alpha` by +/- 0.05, the batch `m` over {5, 10, 20}, and the state count `N` over {1, 2, 3}, all without re-tuning anything else. **Fail if** baseline PredI changes sign in return or loses more than 0.50 Sharpe under any single perturbation. **Action:** mark the result as a tuned point, not a robust region.
- **F10 - Placebo / shuffled-label test.** Circularly shift the spread series (block lengths 5, 21, 63) and re-run the whole pipeline 500 times. **Fail if** the real sample's PredI Sharpe sits below the 95th percentile of the placebo distribution. **Action:** declare the reported Sharpe indistinguishable from a resampling artefact.
- **F11 - Multiplicity gate.** Apply Benjamini-Hochberg at `q < 0.10` plus a deflated-Sharpe correction over the full reported family (5 alphas x 5 strategies x 6 contract sets plus the risk table). **Fail if** no cell survives at `q < 0.10`. **Action:** report the star notation as unadjusted and withdraw significance language.
- **F12 - Point-in-time and roll gate.** Rebuild the continuous series from raw contract-by-contract data with a published, point-in-time roll rule, and re-estimate costs from a training-only bid-ask window rather than the full sample. **Fail if** the baseline PredI Sharpe moves by more than 0.30 absolute or the hedge coefficients change sign. **Action:** declare the result dependent on vendor continuous-series construction and on a look-ahead cost estimate.
- **F13 - Capacity and liquidity gate (research-proposed).** Cap each leg at 10% of the contract's average daily volume and re-run. **Fail if** Sharpe degrades by more than 0.50 absolute or if the Shanghai leg is unfillable in more than 20% of intended sessions. **Action:** mark as non-scalable research material only.
- **F14 - Frozen forward window.** From the date this record is written, run the frozen rule with no re-estimation choices for at least 12 months and score it once. **Fail if** forward Sharpe is below 0.00. **Action:** reject; no further re-tuning is permitted under the rule below.

**No-retuning rule (applies to every gate).** The following are frozen once F1 is attempted: the four Datastream near-month series; the weekly-frequency Johansen rank-1 hedge with a constant and VAR order 2; the exact spread `S_t = F^B - 0.6982 F^S - 0.3402 F^W + 0.4322`; the 2-state AR-HMM with `m = 10`, `X_hat_0 = e_1`, `pi_11(0) = 0.6`, `pi_22(0) = 0.5` and first-20-point OLS seeding at 1.3x/0.7x; the five strategies exactly as written in Section 3.1; the `alpha` grid {0.30, 0.25, 0.20, 0.15, 0.05} with `alpha = 0.20` as the single declared baseline; the exit-on-sign-change rule; the gross-notional normalisation `G_t`; zero-interest idle cash; and the Table 1 cost vector as the source baseline. A failed gate cannot be rescued by re-selecting `alpha`, `N`, `n`, the quantile window, `t_0`, `t_B`, the contract set, or the cost vector; any such re-selection is a new experiment requiring a new record.

## Crypto portability

**Portability: adapted (mechanism ports mechanically; performance unproven; no crypto evidence in the source).**

The source contains `crypto` exactly once, in footnote 2 citing Crepelliere, Pelster and Zeisberger (2023) on cryptocurrency arbitrage as an example of a different literature; `bitcoin` 0 and `perpetual` 0 occurrences. Nothing in this record is crypto empirical evidence.

What ports mechanically: the statistical object (a stationary spread from a rank-1 cointegrating relationship), the two-state AR-HMM with online filter-based EM, the band-and-sign-change trading logic, the gross-notional normalisation, and the falsification plan F1-F14.

What fails to port and must be re-derived rather than copied:

- **Instrument.** There is no single underlying behind a BTC/ETH "cointegration" of this form: perpetuals, quarterly futures and spot on different venues are not three claims on one asset with one delivery, so the three-contract construction (the source's headline contribution) has no direct crypto analogue; the closest analogue would be cross-venue or spot-perpetual-quarterly on the *same* asset, which changes the mechanism from cross-contract basis to funding/basis carry.
- **Sessions and timestamps.** 24/7 sessions, no daily settlement boundary, no exchange-official daily close for all venues - the `t` indexing and the `250/n` annualisation both break.
- **Funding and margin.** Perpetual funding (8-hour or 1-hour), mark-price margining, ADL and liquidation price are absent from the source's cost model entirely (`funding` 0 occurrences); the source's single scalar half-spread is not a substitute.
- **Venue fragmentation and survivorship.** Datastream's single continuous series has no crypto counterpart; delistings, index rebaskets, quote-currency choice (USDT vs USD vs BTC) and stablecoin depeg all become new point-in-time requirements.
- **Liquidity and impact.** Crypto perp depth and taker-fill behaviour differ by orders of magnitude across venues; F13 must be re-run from scratch, and the source's `liquidity` 0 / `capacity` 0 baseline offers no prior.

Crypto portability is not authorization to trade; it is a hypothesis that the filter-and-band machinery is worth testing on crypto only after F1-F14 are re-derived for crypto instruments.

## Limitations

- `underspecified`: ProbI rolling window `n`; RI/PI empirical-quantile estimation window; signal-to-order timing and execution price; Sharpe annualisation factor; timezone/session/price-field convention; Datastream roll rule; `N` selection window (training vs trading sample).
- `data gap`: slippage, commission, fees, funding, borrow, market impact, latency, order type, fill model, maker/taker, participation, turnover, capacity, liquidity, position limits, leverage/margin quantification, missing-data handling, point-in-time audit, out-of-order timestamps, code/seed/software, data availability, conflict-of-interest statement, Supplementary Materials.
- `not independently reproduced`: every source-reported number above.
- `unproven`: that the effect survives anything beyond the Table 1 scalar half-spread; that it survives a second one-year window; that it survives multiplicity correction; that the two-regime structure is identifiable from 1,112 training observations; that it ports to crypto.
- Sample limitation: a single static four-name universe defined by vendor mnemonics, one market (crude oil futures), one geography set, one horizon (daily), a start date forced by the March-2018 Shanghai listing, and a test year chosen by a single break date that the source itself shows moves results.
- Identification limitation: the cointegration vector, the regime model and the bandwidth are all estimated or chosen on the same training sample, and the rank-1 test that gates the whole strategy is itself fragile under window perturbation (Figure 9).
- Source-quality limitation: preprint only, three versions, abstract rewritten twice, no peer-review claim, no journal reference; the arXiv-served abstract is stale relative to the pinned version and contradicts the pinned tables on the traditional-instrument claim.
- Publication-bias limitation: a positive-result grid with 150+ reported cells and no multiplicity control; the two negative strategies are reported, but the family-wise false-discovery rate is unknown.
- Reproducibility limitation: no code, no seed, two missing strategy parameters, no Supplementary Materials in the artefact, and a "100 randomised runs" robustness claim whose draws cannot be regenerated.
- Incremental-value check: this capture is written because the repo holds no record for this source identity (dedup 0 files) and because its mechanism is materially distinct from the existing records - see the section below.

## Implementation status

`implementation_status: not-implemented`.

Nothing in this record has been implemented in our research stack. No NautilusTrader strategy, no strategy family, no Qlib configuration, no backtest, no market-data download, no dependency installation and no third-party code execution occurred for this record. The only artefacts produced this run are: this Markdown file in the staging repository, and read-only capture/extraction scripts plus cached primary-source bytes under a scratch directory. The `not independently reproduced` statement above is literal: no number in this record has been reproduced by us.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record in the repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. Research capture is not strategy adoption, implementation authorization, or permission to run Paper/Testnet/Live. No record may promote itself by wording, evidence count, confidence, or schedule behaviour; any later adoption or implementation decision must be explicit, separately reviewed, and based on this record plus current live sources.

## Related Wiki records

Read-only Wiki Brain searches this run returned verified existing pages; four were linked, all mechanically adjacent and all materially distinct from this capture. No page was fabricated and **no page was written to Wiki Brain**.

- [[quant/crude-oil-crack-spread-seasonally-adjusted-mean-reversion-stop-lockout-2026-09-12]] - same asset class (crude oil) but a **processing 3:2:1 crack-spread** mean-reversion rule with stop/re-entry lockout; mechanism (refinery margin, not futures cointegration), signal construction and horizon all differ.
- [[quant/sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12]] - shares the Johansen-cointegration-plus-OU statistical-arbitrage *family*, but on an equity index basket with an explicit 4-way ablation and family-wise multiple-testing deflation; universe (equities vs commodity futures), mechanism emphasis (OU vs AR-HMM) and the material data dependency (factor/basket data vs four futures series) all differ, and it is the closest existing contrast for gate F11.
- [[quant/pairs-trading-adf-stationarity-filter-walk-forward-falsification-2026-09-12]] - shares the cointegration-gated pairs-trading thesis, but makes the **stationarity-filter rejection** the object of study under walk-forward validation; mechanism (filter falsification vs regime-conditional forecasting) and horizon differ.
- [[quant/us-etf-pairs-trading-cointegration-cost-viability-falsification-2026-09-13]] - shares the cost-viability question, but on ETF/fixed-income pairs with an abstention-gate artefact and fractional nonstationarity; universe and material data dependency differ.

Additional repo records read as contrast only, none linked as the same mechanism: `commodity-soybean-crush-spread-cointegration-stat-arb-2026-09-12.md`, `pep-ko-cointegration-pairs-trading-out-of-sample-failure-arxiv-2609.35359-2026-09-29.md`, `sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12.md`, and the FMZ/wiki Kalman-OU and Johansen-OU records.

**Four-axis distinction versus the nearest existing records** (source identity / mechanism / signal construction / universe-market-type / horizon-regime / material data dependency): every linked pair differs in source identity and in at least three of the five axes. This source is the only record built on an **online filter-based AR-HMM forecast band** applied to a **three-contract crude-oil hedge including the INE Shanghai contract**, evaluated on a **single one-year daily test window**.

## Sources

- arXiv landing page, `https://arxiv.org/abs/2309.00875v3`, captured 2026-09-30, 41,722 bytes, SHA-256 `ee863cf79f83666e4ee535a8ac29f7a66ad896247dc366f140c9575173343f3c` - for the exact title, the three `citation_author` tags, `citation_date 2023/09/02`, the dateline, the single `General Finance (q-fin.GN)` subject, the absent Comments and Journal-reference rows, the arXiv-issued DataCite DOI `10.48550/arXiv.2309.00875`, the CC BY 4.0 licence, the three-line submission history with submitter `Francesco Rotondi`, `peer` count 0, and the stale v1-identical abstract.
- arXiv PDF (v3), `https://arxiv.org/pdf/2309.00875v3`, captured 2026-09-30, 768,717 bytes, SHA-256 `749f3deacd54dede22e08dc0a31e5814853afe7930f2a9bd4667fe53a3b589e4`, 31 pages, 96,268 extracted characters read end to end - for the v3 abstract, Sections 1-5, Equations (2.1)-(4.2), Remarks 2.1/2.2/3.1/3.2/4.1/4.3, Tables 1-8 and Figures 1-10.
- arXiv API record, `https://export.arxiv.org/api/query?id_list=2309.00875`, captured 2026-09-30, 2,699 bytes, SHA-256 `67aa6a3874f7acbffcb43724d7b65f4c0a1a826f1299a7fb5b20bd1b6cd66f51` - one entry, `published 2023-09-02T09:35:00Z`, entry `updated 2026-02-13T10:06:35Z`, primary category `q-fin.GN`, three authors in source order, no `arxiv:comment`, no `arxiv:journal_ref`, no `arxiv:doi`, `<summary>` identical to the stale v1 abstract.
- arXiv PDF (v1), `https://arxiv.org/pdf/2309.00875v1`, captured 2026-09-30, 1,076,209 bytes - read only to establish that the landing/API abstract is the v1 abstract.
- arXiv PDF (v2), `https://arxiv.org/pdf/2309.00875v2`, captured 2026-09-30, 734,075 bytes - read only to establish that the v2 abstract is a third, intermediate variant.

Third-party works cited **by the source** and quoted here only as the source's own attributions, not as independently consulted evidence: Hain et al. (2018) for the cost estimator and the 6%-8% magnitude reference; Ledoit and Wolf (2008) for the Sharpe test; White (2000) and Sullivan et al. (1999) for the reality check; Politis and Romano (1994) for the stationary bootstrap; Johansen (1988); Engle and Granger (1987); Gatev et al. (2006); Burgess (1999); Vidyamurthy (2004); Elliott et al. (2005); Dunis et al. (2006); Avellaneda and Lee (2010); Bock and Mestel (2009); Alizadeh and Nomikos (2008); Do and Faff (2012); Caporin et al. (2019); Lee and Papanicolaou (2016).
