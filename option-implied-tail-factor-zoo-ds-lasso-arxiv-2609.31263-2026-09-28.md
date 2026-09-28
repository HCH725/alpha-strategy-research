---
schema: strategy-research-record-v1
title: Option-Implied Tail and Higher-Moment Factor Zoo Tested Against 160 Equity Factors with Double-Selection LASSO (arXiv:2609.31263)
created: 2026-09-28
updated: 2026-09-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equities
  - options
  - option-implied
  - factor-zoo
  - tail-risk
status: research-only
confidence: medium
source_as_of: 2026-09-25
sources:
  - "https://arxiv.org/abs/2609.31263 - arXiv:2609.31263v1 [q-fin.CP], 'Taming the Option Factor Zoo: A High-Dimensional Analysis', Alexander Walter, Lukas Zimmer, Maxim Ulrich; submitted Fri, 25 Sep 2026 13:39:09 UTC; DOI https://doi.org/10.48550/arXiv.2609.31263 (abs page read 2026-09-28)"
  - "https://arxiv.org/pdf/2609.31263v1 - pinned canonical PDF v1, 46 pages, 488461 bytes, SHA-256 70b5561b1b4c0410c1c5f1578c75d04297c502d2d6253e8f1a9cb832098daf32, retrieved 2026-09-28, text extracted page by page with pypdf 6.16.2 to 94210 characters / 1984 lines and all 46 pages read"
  - "https://arxiv.org/html/2609.31263v1 - arXiv HTML rendering of v1, read 2026-09-28, used only to cross-check table values already present in the pinned PDF"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Version date disagreement: the arXiv submission-history line and the PDF footer both read '25 Sep 2026' (v1 submitted Fri, 25 Sep 2026 13:39:09 UTC), while the PDF title page prints 'September 28, 2026'. Left unreconciled; not resolved by the Scout."
  - "Sign disagreement acknowledged by the source itself: for five of the eight significant factors (bakshiKurt, RND_kurt_eps, ivs_convexity, BTX_LJV_7_5, BTX_EQV_relTail_k) the sign of the SDF loading lambda_s is positive while the factor's average return is negative (source Section 4.3); the source explicitly warns that lambda_s is not the premium earned by the long-short portfolio (source Section 3.2 and 4.3)."
  - "Abstract-level claim 'adding the option factors does not significantly raise the maximum Sharpe ratio' sits next to a mechanically higher in-sample maximum Sharpe of 3.74 versus 3.35 (source Section 4.4); the source resolves this by the GRS non-rejection and by noting in-sample Sharpe is upward biased, so both statements stand as printed."
  - "Screen-stability tension: bakshiKurt, RND_kurt_eps and BTX_MRJI_20_annual are among the individually significant factors yet are selected at only 1 of 7 maturities and at most 3 of 70 window-maturity combinations (source Table 3), which the source attributes to the redundancy of the option zoo rather than to stability of those signals."
  - "GRS non-rejection versus maturity-level rejection: the headline GRS at 30 days does not reject (statistic 1.25, p = 0.25) but at the 60-day maturity the GRS rejects at the 5% level (p = 0.043, source Table C.6), one rejection out of seven maturities (source Section 4.5)."
  - "No data or code availability statement, no funding statement and no competing-interest statement were located in the pinned PDF; the source states only that it uses the Feng et al. (2020) DS-LASSO code 'without modification' (source Section 3.2)."
---

# Option-Implied Tail and Higher-Moment Factor Zoo Tested Against 160 Equity Factors with Double-Selection LASSO (arXiv:2609.31263)

## Provenance

- **Primary source (canonical):** arXiv:2609.31263v1 [q-fin.CP], *"Taming the Option Factor Zoo: A High-Dimensional Analysis"*, **Alexander Walter, Lukas Zimmer, Maxim Ulrich** (complete author list exactly as printed on PDF p.1 and in the arXiv listing; three authors, no co-authors beyond these). DOI `10.48550/arXiv.2609.31263`.
- **Version/date:** arXiv submission history `[v1] Fri, 25 Sep 2026 13:39:09 UTC (75 KB)`; PDF footer `arXiv:2609.31263v1 [q-fin.CP] 25 Sep 2026`; PDF title page prints `September 28, 2026`. The two date expressions are **unreconciled** (frontmatter contradiction 1).
- **Contact lines printed on PDF p.1:** `alexander.walter@partner.kit.edu` (Corresponding author), `lukas.zimmer@kit.edu`, `maxim.ulrich@kit.edu`. **An affiliation line is not printed on the title page**, so institutional affiliation is `not stated in source` for this record; only the email domains are source-reported.
- **Publication / preprint status:** arXiv preprint v1 only. No journal, no acceptance comment, no peer-review statement appears in the arXiv listing or the PDF -> publication status `not stated in source`.
- **Keywords / JEL as printed:** keywords "Factor zoo, option-implied information, stochastic discount factor, double-selection LASSO, asset pricing tests"; JEL `G12, G13, C55`.
- **Pinned PDF:** `https://arxiv.org/pdf/2609.31263v1`, **46 pages, 488,461 bytes, SHA-256 `70b5561b1b4c0410c1c5f1578c75d04297c502d2d6253e8f1a9cb832098daf32`**, retrieved 2026-09-28. Text extracted page by page with `pypdf 6.16.2` to **94,210 characters / 1,984 lines**; **all 46 pages read**, including Sections 1-6, Tables 1-7, Appendix A (equity characteristics), Appendix B (option-implied characteristics), Appendix Tables C.1-C.8, and the full reference list. PDF metadata: `/Author "Alexander Walter; Lukas Zimmer; Maxim Ulrich"`, `/Title "Taming the Option Factor Zoo: A High-Dimensional Analysis"`, `/DOI "https://doi.org/10.48550/arXiv.2609.31263"`, `/arXivID ".../2609.31263v1"`, `/License http://arxiv.org/licenses/nonexclusive-distrib/1.0/`, `/Creator "arXiv GenPDF (tex2pdf:0d14211)"`, `/Producer "pikepdf 8.15.1"`, `/Trapped /False`.
- **Secondary cross-check (not a second source of claims):** `https://arxiv.org/html/2609.31263v1` read on 2026-09-28 only to confirm that HTML and PDF render the same table values; every number normalised below was located in the **pinned PDF text**.
- **Underlying data (source-reported, Section 2.1):** equity characteristics from the **Jensen et al. (2023)** dataset built on CRSP and Compustat; **option-implied characteristics constructed from CBOE option data**; risk-free rate from FRED (three-month Treasury bill) with the van Binsbergen et al. (2022/2023) TOPT option-implied rate as robustness; standard benchmark factor series from **Kenneth French's data library**. No dataset or code artefact is released by this paper.
- **Method dependency (not an independent source):** the DS-LASSO implementation of Feng, Giglio and Xiu (2020), used "without modification" (Section 3.2); the implied-volatility kernel smoother of Ulrich et al. (2023) (Section 2.2).
- **Source-quality classification:** primary academic preprint with Methods, Data, Methodology, Results, Robustness and Limitations sections read directly; no secondary summary was used to fill any field.
- **What this record is not:** it is not a record of a profitable strategy. The paper is a **factor-pricing (SDF) study**; its own reported long-short factor returns are mostly negative (Evidence below).

## Economic mechanism

### Source-reported

- The source's question is whether factors sorted on **option-implied characteristics** contribute to the stochastic discount factor (SDF) once a high-dimensional **equity factor zoo** is controlled for (Section 1). Option prices are forward-looking and reveal each stock's **risk-neutral distribution including its tails**, which characteristics built from past prices and accounting data do not directly contain (Section 1).
- The source's stated finding has two parts (Section 1, Section 4):
  1. **Largely spanned:** in-sample the 160 equity factors account for **91.0%** of the variance of the 20 option factors versus a **~69% noise level**, while the 20 option factors account for **35.4%** of the equity factors' variance versus a **~9% noise level** (Table 7). A GRS test does not reject jointly zero option-factor alphas (statistic **1.25**, **p = 0.25**, Section 4.4), and the in-sample maximum Sharpe ratio rises from **3.35** (equity factors) to **3.74** (combined) - an increase of **0.39** that the source states is **not statistically significant** (Section 4.4).
  2. **Not completely spanned:** **8 of the 20** option factors have SDF loadings significantly different from zero at the 5% level after controlling for the equity zoo, and **4** survive a Bonferroni correction for 20 tests: **implied-volatility convexity, the share of risk-neutral variance due to large jumps, left-tail jump variation, and risk-neutral kurtosis** (Section 4.3, Table 6).
- The source's interpretation of the sign pattern (Section 4.3) is that tail size and curvature measures carry **positive** loadings while right-tail jump intensity and option-implied physical variance carry **negative** loadings, "consistent with investors disliking exposure to tail and downside risk (Bollerslev et al., 2015), being willing to pay for right-skewed payoffs (Conrad et al., 2013), and avoiding high-volatility stocks (Ang et al., 2006)". The source immediately qualifies: **"Our design, however, does not identify the economic mechanism."**
- The source explicitly refuses to read the loadings as a tradable premium (Section 3.2, Section 4.3): the scaled loading `lambda_s` **"is not the same as the factor's average return"**; it **"measures only the factor's marginal contribution to the SDF, given the controls"**; and the source states that it reads the sign of `lambda_s` as a statement about which direction of covariance with the factor is priced in the cross-section of test assets, **"not as the premium earned by the long-short portfolio"**.

### Research interpretation

- **Hypothesis in falsifiable form (Scout framing):** the cross-section of optionable US equity returns contains a **tail / higher-moment dimension** - risk-neutral kurtosis, implied-volatility convexity, left-tail jump variation and the share of variance due to large jumps - that is **not reproduced by 152 equity characteristics plus 8 standard French factors**, i.e. option prices carry incremental pricing information beyond price- and accounting-based characteristics.
- **Component roles (this is a measurement study, not a packaged strategy):**
  - Signal source: option-implied tail/higher-moment characteristics (risk-neutral density from CBOE option prices).
  - Construction: monthly value-weighted decile long-short sort per characteristic on S&P 500 constituents.
  - Hypothesis test: DS-LASSO of the option factor against 160 equity controls on a cross-section of test portfolios.
- **Critical boundary:** the source reports **negative average returns** for most of the selected factors (Evidence). A long-short implementation taken literally from Table 4 therefore loses money before costs; any decision to **reverse the sign** of those factors, or to trade only the four Bonferroni-surviving ones, is **`research-proposed`** by this Scout and is **not** proposed, tested or endorsed by the source.
- **Friction assumed by the mechanism (stated, not measured):** the mechanism requires a live, sufficiently deep single-name option surface to recover a risk-neutral density, and a short leg in the underlying decile. Neither friction is priced anywhere in the source (see Execution assumptions).

## Signal

All items below are **source-reported** unless explicitly marked `research-proposed` or `research-defined`.

- **Formation timestamp:** characteristics are computed from option prices at a **constant maturity of tau = 30 days**, chosen because it "matches the monthly rebalancing frequency" (Section 2.3). Sorting happens **"At the end of each month"**; portfolios are **"held for the following month"** (Section 2.3). Timezone, exchange closing convention, option-quote timestamp and any same-day intraday cut-off are **not stated in source** -> `data gap`.
- **Risk-neutral density construction (Section 2.2):** Breeden-Litzenberger (1978) risk-neutral density; a one-dimensional **kernel estimator of Ulrich et al. (2023)** smooths along moneyness `m_i = K_i / F_i` and is chosen because it "reduces cross-validation errors relative to standard approaches"; **implied volativities are extrapolated linearly beyond the observed strikes** "which stabilizes the tails of the density". Kernel bandwidth, strike/maturity filters and the minimum quote count per stock-month are **not stated in source** -> `data gap`.
- **Characteristic families (Section 2.2, Appendix B):** model-free risk-neutral volatility/skewness/kurtosis (Bakshi et al., 2003); jump and tail decomposition of risk-neutral quadratic variation, left- and right-tail jump variation, jump intensities (Bollerslev et al., 2015); the rare-disaster index of Gao et al. (2018); IV surface shape (smirk, convexity, out-of-the-money wing slopes); option-implied betas, option-implied equity premia and the SVIX of Martin (2017); plus **P_implQ** measures that scale risk-neutral moments at longer maturities by the one-day `P/Q` ratio - the source calls carrying a constant `P/Q` ratio to longer maturities **"a strong assumption"** and treats them "as approximations of physical moments". Systematic (`_sys`) and idiosyncratic (`_eps`) decompositions are also built; "The variance decomposition is additive; the decompositions of the higher, normalized moments are not."
- **Screen - how 137 became 20 (Section 3.1):** 91% of the 137 option factors have a variance inflation factor above 10 and 62% above 100. A **histogram-based gradient-boosted regressor** (learning rate `0.01`, at most `100` boosting iterations, maximum tree depth `3`) is fit with target = the **equal-weighted average return of all test-asset portfolios in month t** and features = the returns of the **137 option factors in the same month** (a **contemporaneous fit, not a forecast**). Validation: **five-fold walk-forward time-series split with expanding windows plus five rolling windows**; the **final selection is estimated on the full sample**. SHAP mean-absolute attributions rank the factors; the rule is to **"keep the largest set of top-ranked factors whose cumulative share of total attribution does not exceed 90%"**, yielding **20 factors that account for 89.3%** of total attribution (Section 3.1, Table 2).
- **Factor construction (Section 2.3):** each month, **S&P 500 constituents in the intersected universe** (index membership updated monthly) are sorted into **deciles** on the characteristic; the factor is **long the top decile, short the bottom decile**; portfolios are **value-weighted** and **held for the following month**.
- **Benchmark zoo (Section 2.3):** **160 equity factors =152** built the same way from the characteristics of Jensen et al. (2023) (Appendix A lists 153; price per share `prc` is excluded) **+8** Kenneth French library factors (Fama-French five, momentum, short- and long-term reversal).
- **Individual test (Section 3.2):** each of the 20 option factors is tested **individually** against the 160 equity factors by the Feng-Giglio-Xiu DS-LASSO: Step 1 selects equity factors that price the test assets (pricing relevance); Step 2 selects equity factors whose covariances with the test assets correlate with the option factor's (confounding); `lambda_g` is then OLS-estimated on the union `I = I1 + I2`; the third time-series LASSO residual `z_t` enters the heteroskedasticity-robust variance. Tuning parameters for Steps 1 and 2 use **10-fold cross-validation averaged over multiple random seeds**; the inference step uses K-fold time-series cross-validation with the one-standard-error rule. Reported statistic: **`lambda_s`**, the SDF loading scaled to unit univariate beta exposure, in **basis points per month**.
- **Multiple-testing rule (Section 3.2):**20 tests -> probability of at least one false rejection `1 - 0.95^20 ~ 64%`. **`research-defined` in the source, not by the Scout:** Bonferroni at level `0.05/20` i.e. **`|t| > 3.02`**, plus Benjamini-Hochberg FDR 5%. The source notes the Bonferroni threshold is close to the Harvey et al. (2016) `t > 3.0` hurdle.
- **Test assets (Section 2.3):** for each characteristic, **six portfolios from independent 3x2 sorts on the characteristic and market capitalisation** over all stocks in the intersected universe, plus the French benchmark portfolios. The **total number of test assets `n` entering the DS-LASSO cross-section is never printed as a single number** -> `data gap`. (The "20 test assets" in Section 4.4 refers to the **GRS test**, where the 20 option factors are the test assets and the 160 equity factors are the factors.)
- **Aggregate tests (Section 3.3):** GRS test of jointly zero option-factor alphas; maximum Sharpe ratios for equity-only, option-only and combined sets using tangency weights inverse covariance matrix times mean excess returns with a **Ledoit-Wolf (2004)** shrinkage covariance (because the combined set has 180 factors versus 234 months); shared variation via canonical correlation analysis with the **Stewart-Love (1968)** redundancy index over all `k = 20` canonical pairs, benchmarked against an approximate independent-noise level of `160/233 ~ 0.69` and `20/233 ~ 0.09`.
- **Underspecified for reproduction:** because the screen is fit on the full sample and the tests run on the same sample, the **identity of the 20 factors is conditional on the full-sample screen**; the source states the selected factors should be read **"as representatives of groups of related measures ... rather than as uniquely identified signals"** (Section 4.1) and reports that selection varies across maturities and subsamples (Table 3, Tables C.1/C.3). A point-in-time reproduction cannot recover the same 20 names without re-running the in-sample screen -> **underspecified as an out-of-sample rule**.
- **Not present in the source:** no entry trigger beyond the monthly decile sort, no stop, no take-profit, no holding-period alternative, no position sizing beyond value weights, no leverage rule, no universe liquidity filter, no turnover control. Any such rule is **`research-proposed`** if introduced downstream.

## Required data

- **Instrument / universe:** US common stocks **with listed options** intersected with the Jensen et al. (2023) equity-characteristics panel. Table 1: equity universe **17,586** stocks; stocks with listed options **9,987**; **final universe (sufficient option data) 7,126**; **824,081 firm-month observations**; **42** stocks per month in each leg of a factor portfolio; **369** stocks per month in each leg of a test-asset portfolio. Panel is unbalanced. Factor formation universe = **S&P 500 constituents, updated monthly**; test assets = all stocks in the intersected universe.
- **Market type / venue:** US equity single-name options; option-implied characteristics built from **CBOE option data** (Section 2.1). Option chain fields required: strikes, expiry, bid/ask or settle price used to fit implied volatilities, and the underlying forward `F_i` implied by the moneyness definition - **the exact quote field (bid/ask/mid/settlement) used to fit IV is `not stated in source`** -> `data gap`.
- **Timeframe:** monthly return sample **February 2004 - July 2023, 234 months** (raw data start January 2004; the first month builds lagged variables). A daily-frequency version was attempted and **failed**: "The noise in daily returns led to near-singular covariance matrices, and the DS-LASSO estimation did not converge" (Section 2.1 footnote).
- **Fields:** option-implied characteristics at tau = 30 days (and 1/2/3/5/10/60 days in robustness); equity characteristics from CRSP/Compustat via Jensen et al. (2023); Fama-French five + momentum + short- and long-term reversal from Kenneth French; three-month Treasury bill from FRED converted to a monthly rate and **lagged by one month** (TOPT as robustness).
- **Point-in-time:** index membership updated monthly; **the paper does not describe any option-data availability lag, quote-staleness rule or corporate-action handling for the option panel** -> `data gap`.
- **Timestamp / timezone:** not stated in source -> `data gap`.
- **Missing data:** the source requires "sufficient option data ... to estimate the risk-neutral density" (Table 1 caption) but **does not state the sufficiency criterion** (minimum quotes, moneyness coverage, expiry count) -> `data gap`. Imputation is not described; the linear out-of-the-money IV extrapolation is an explicit tail-stabilisation device, not an imputation of missing strikes.
- **Cost/fee fields:** **none are required or used by the source** - see Execution assumptions.

## Execution assumptions

Determined from a **Methods-level read of Sections 2.1, 2.3, 3.1, 3.2, 3.3, 4.2-4.5 and 5 of the pinned PDF**, plus a whole-document term scan of the extracted 94,210-character text.

- **Cost treatment (source-reported, explicit):** Section 2.3 states verbatim **"We report gross returns and ignore transaction costs throughout."** Every return, alpha, Sharpe, drawdown and loading normalised in this record is therefore **gross of transaction costs**.
- **Whole-document cost-term scan of the pinned PDF (Scout-recomputed):** `transaction cost(s)` **1** occurrence (the Section 2.3 sentence above); `slippage` **0**; `latency` **0**; `market impact` **0**; `capacity` **0**; `commission` **0**; `borrow` **0**; `liquidation` **0**; `execution` **0**; `fill` **0**; `participation` **0**; `short-sell` **0**; `spread` **8** - all inside literature descriptions ("spread between implied and realized volatility", "call-put implied-volatility spread") or the Appendix A/B characteristic name lists (`bidaskhl 21d High-low bid-ask spread Corwin and Schultz (2012)`, `ivs atm spread ATM IV call-put spread Yan (2011)`); `turnover` **7** - all in the Appendix A equity-characteristic name list (`Asset turnover`, `Capital turnover`, `Share turnover`, `turnover 126d`, `turnover var 126d`), never as a modelled cost; `leverage` **2** - Appendix A (`Book leverage`, `Operating leverage`); `funding` **1** - literature citation ("factors motivated by funding constraints (Frazzini and Pedersen, 2014)"); `dividend` **1** - Appendix A (`div12m Dividend yield`); `adv` **1** - inside the bibliography entry "Advances in Neural Information Processing Systems", **not** average daily volume. Zero occurrences are **zero occurrences of the term**, not evidence that the concept was modelled: order type, fill model, latency, spread cost, slippage, commission, borrow cost, short-sale constraint, capacity, market impact and turnover cost are **all `data gap` - never zero**.
- **Order type / fill model / signal-to-order delay:** not stated in source -> `data gap`. The design is a month-end sort held one month; whether the sort is executed at the month-end close, the next open, or an average price is **not stated** -> `data gap`.
- **Fees, spread, slippage, impact, capacity:** explicitly ignored (gross returns). No fee schedule, no bid-ask treatment, no participation cap, no AUM reference -> `data gap`.
- **Funding / leverage / margin:** not stated in source -> `data gap` (the long-short factor implies margin and short availability but neither is specified).
- **Borrow / shorting:** the factor is long top decile and short bottom decile, but **short-reachability, locate availability and borrow cost are not stated** -> `data gap`.
- **Dividends:** the paper does not state whether the equity returns entering the sorts and test assets are total returns including dividends -> `data gap`. (A `div12m Dividend yield` row exists only as an Appendix A *characteristic*, not as a return treatment.)
- **Distributions / rebalancing cadence:** monthly, value-weighted, one-month holding, overlapping positions not applicable (single monthly decision). No turnover reported for any factor -> `data gap` on turnover-driven cost exposure.
- **Scout-added assumptions:** **none.** No cost, fill, latency, sizing or liquidity assumption has been introduced by this record.

## Evidence

### Source-reported

Every figure below is third-party, **source-reported**, gross of costs, in-sample, and traced to the pinned PDF.

**Table 1 - sample selection (Section 2.1):** return sample **Feb 2004 - Jul 2023**, **234** months, monthly; equity universe **17,586**; stocks with listed options **9,987**; final universe **7,126**; firm-month observations **824,081**; average stocks per month per factor-portfolio leg **42**; per test-asset leg **369**.

**Screen diagnostics (Section 3.1):** **91%** of the 137 option factors have VIF > 10, **62%** VIF > 100; GBR hyper-parameters `lr = 0.01`, `<=100` iterations, depth `3`; **20** factors retained covering **89.3%** of total SHAP attribution. Table 2 largest attributions: `P_implQ_var` **14.65%** (mean|SHAP| **0.005653**), `BTX_RJV_k` **13.26%** (**0.005117**), `BTX_EQV_relTail_k` **12.58%** (**0.004854**), `bakshi_X` **6.88%**, `RND_mu` **6.45%**, `P_implQ_var_eps` **6.14%**, `SVIX2_put_annual` **5.43%**.

**Table 3 - screen stability:** `BTX_RJV_k` selected at **7/7** maturities and **28/70** window-maturity combinations; `P_implQ_var` **3/7** and **32/70**; `BTX_MRJI_k_annual` **7/7** and **18/70**; `ivs_convexity` **6/7** and **7/70**; `bakshiKurt` **1/7** and **3/70**; `RND_kurt_eps` **1/7** and **3/70**; `BTX_MRJI_20_annual` **1/7** and **1/70**; `BTX_RJV_10` **1/7** and **1/70**.

**Table 4 - performance of the 20 long-short option factors (Feb 2004 - Jul 2023; annualised mean, vol, MDD, Sharpe, skew; t with Newey-West 6 lags):**
- `bakshiKurt`: **-11.23%**, vol **12.84%**, MDD **-91.07%**, Sharpe **-0.87**, skew **-2.29**, **t = -3.25**.
- `ivs_convexity`: **-14.78%**, vol **17.94%**, MDD **-96.94%**, Sharpe **-0.82**, skew **-3.59**, **t = -2.57**.
- `ivs_smirk`: **-11.17%**, vol **18.93%**, MDD **-93.05%**, Sharpe **-0.59**, skew **-2.52**, **t = -1.96** (described as borderline).
- `RND_mu`: **+8.26%**, vol **31.16%**, MDD **-67.19%**, Sharpe **0.27**, **t = 1.06**.
- `BTX_EQV_relRightTail_10`: **+5.04%**, vol **18.08%**, MDD **-46.76%**, Sharpe **0.28**, **t = 1.23**.
- `BTX_LJV_7_5`: **-4.42%**, vol **24.46%**, MDD **-87.35%**, Sharpe **-0.18**, **t = -0.73**; `BTX_EQV_relTail_k`: **-2.35%**, vol **18.81%**, MDD **-81.12%**, Sharpe **-0.13**, **t = -0.47**.
- Source's own summary (Section 4.2): **"Most have negative average returns over the sample. Only bakshiKurt (t = -3.25) and ivs_convexity (t = -2.57) have average returns that differ significantly from zero at the 5% level"**, and **"Several factors have large negative skewness and drawdowns of more than 90%."**

**Table 5 - FF5 + momentum regressions (annualised alpha, %):** significant negative alphas at the 5% level for `bakshiKurt` **-10.53** (t **-3.14**), `ivs_convexity` **-16.71** (t **-2.79**), `ivs_smirk` **-12.64** (t **-2.47**) and `SVIX2_put_annual` **-9.1** (Section 4.2 prose). The six factors explain up to **59%** of an option factor's variation (`bakshi_X` adj. R^2 **0.59**); most option factors load **positively on the market** and **negatively on RMW and momentum** (e.g. `bakshi_X`: Mkt-RF **0.67**, RMW **-1.53**, CMA **-0.69**, Mom **-0.51**).

**Table 6 - DS-LASSO against 160 equity factors (`lambda_s` in bp/month, heteroskedasticity-robust t):**
- Significant at 5% (**8 of 20**): `bakshiKurt` **78.51**, t **3.15**, avg ret **-93.6 bp/mo**, Bonferroni pass, BH pass; `BTX_alpha_plus` **74.37**, t **2.23**, avg **4.7**; `BTX_EQV_relTail_k` **295.11**, t **3.65**, avg **-19.6**, Bonferroni pass, BH pass; `BTX_LJV_7_5` **445.65**, t **3.59**, avg **-36.8**, Bonferroni pass, BH pass; `BTX_MRJI_20_annual` **-310.38**, t **-2.28**, avg **-19.6**; `ivs_convexity` **420.03**, t **3.92**, avg **-123.2**, Bonferroni pass, BH pass; `P_implQ_var` **-260.97**, t **-2.40**, avg **-42.6**; `RND_kurt_eps` **150.55**, t **2.89**, avg **-40.8**, BH pass only.
- **Survive Bonferroni (|t| > 3.02), the paper's headline four:** `ivs_convexity` **3.92**, `BTX_EQV_relTail_k` **3.65**, `BTX_LJV_7_5` **3.59**, `bakshiKurt` **3.15**; these same four clear the Harvey et al. (2016) `t > 3.0` hurdle, and BH adds `RND_kurt_eps` (Section 4.3).
- Sign pattern (Section 4.3): positive loadings on tail size/curvature (`bakshiKurt`, `RND_kurt_eps`, `ivs_convexity`, `BTX_LJV_7_5`, `BTX_EQV_relTail_k`, `BTX_alpha_plus`) and negative on right-tail jump intensity (`BTX_MRJI_20_annual`) and option-implied physical variance (`P_implQ_var`).

**Table 7 - redundancy indices (Section 4.4):** options explained by equity factors **0.9103** (noise level **0.69**); equity factors explained by options **0.3536** (noise level **0.09**); unique share of options **0.0897**; unique share of equity factors **0.6464**.

**Section 4.4 - aggregate tests:** GRS statistic **1.25**, **p = 0.25** (does not reject; the source notes the test has "few residual degrees of freedom and limited power, so this non-rejection is weak evidence in either direction"); in-sample annualised maximum Sharpe **3.35** (160 equity factors), **1.29** (20 option factors), **3.74** (combined), increase **0.39** not significant; the source calls **3.35 "an upper bound rather than an achievable Sharpe ratio"** because in-sample maximum Sharpe is upward biased in large asset sets (Kan et al., 2024).

**Section 4.5 - robustness:** re-running the whole pipeline at maturities **1, 2, 3, 5, 10, 30 and 60 days** leaves equity factors explaining **91%-94%** of option-factor variance and option factors explaining **29%-35%** of equity-factor variance; GRS does not reject at 5% at **six of seven** maturities, rejecting at **60 days with p = 0.043**; the in-sample Sharpe gain ranges **0.16-0.39** (Table C.7). `BTX_LJV_7_5` is selected at five maturities with a positive significant loading at each; `BTX_EQV_relTail_k` positive and significant at all three maturities where selected; `ivs_convexity` positive and significant at 1,2 and 30 days but **negative at 10 days**; `bakshiKurt`, `RND_kurt_eps` and `BTX_MRJI_20_annual` appear **only at 30 days**; `P_implQ_var`'s loading **changes sign across maturities**. Swapping the FRED T-bill rate for the TOPT option-implied rate leaves the 30-day results unchanged - "no factor changes significance at the 5% level".

### Independently reproduced

not independently reproduced

### Negative evidence

1. **Source's own aggregate null:** GRS does **not** reject jointly zero option-factor alphas (p = **0.25**), and the in-sample maximum-Sharpe improvement (**3.35 -> 3.74**, +**0.39**) is **not statistically significant** (Section 4.4).
2. **Variance spanned:** the equity zoo reproduces **91.0%** of the option factors' in-sample monthly variance versus a **69%** noise benchmark, leaving a **9.0%** unique share (Table 7) - i.e. most option information is already in price/accounting characteristics.
3. **Returns are mostly negative:** most of the 20 long-short factors have negative average annual returns; only `bakshiKurt` (-11.23%) and `ivs_convexity` (-14.78%) are significantly non-zero at 5%, and **both are significantly negative** (Table 4). A literal long-top/short-bottom implementation of those two loses money before costs.
4. **Extreme drawdowns and skew:** MDD up to **-96.94%** (`ivs_convexity`) and **-93.05%** (`ivs_smirk`), with monthly skew **-3.59** and **-2.52** (Table 4); the source notes several factors have drawdowns above 90%.
5. **Alpha signs are negative where significant:** FF5+MOM alphas of **-10.53%**, **-16.71%**, **-12.64%**, **-9.1%** for the four significant factors (Table 5, Section 4.2).
6. **Everything is in-sample:** "All three steps are in-sample" (Section 3); the screen and the tests share observations; **no hold-out period** is used; "we leave out-of-sample validation to future work" (Section 5).
7. **Effective multiple testing exceeds 20:** the 20 factors were selected from 137, so "the effective number of tests exceeds 20, and even the Bonferroni correction understates the multiple-testing problem" (Section 5).
8. **Selection instability:** individual selected factors **vary across maturities and subsamples** (Section 5, Table 3); the three kurtosis/jump-intensity results are **30-day-only** (Section 4.5).
9. **Sign conflict between `lambda_s` and realised average returns** for five of the eight significant factors (Section 4.3) - the pricing statement and the implementable return point in opposite directions.
10. **Gross of costs:** the entire evidence base explicitly **ignores transaction costs** (Section 2.3), on monthly decile re-sorts of S&P 500 names with **no turnover report**.
11. **No economic mechanism identified:** the source states plainly, "Our design, however, does not identify the economic mechanism" (Section 4.3).
12. **GRS has low power:** "With 20 test assets,160 factors, and 234 months, the test has few residual degrees of freedom and limited power, so this non-rejection is weak evidence in either direction" (Section 4.4).
13. **Upward-biased Sharpe benchmark:** the 3.35 reference is explicitly "an upper bound rather than an achievable Sharpe ratio" (Section 4.4).
14. **Contemporaneous screen:** the GBR target is the **same-month** average test-asset return, so the screen "measures fit rather than forecasting ability" (Table C.2 discussion, Section 4.1).
15. **Single universe:** factors are formed only on **S&P 500 constituents**; the source lists extending "beyond S&P 500 constituents" as future work (Section 6).
16. **Failed daily variant:** the daily-frequency DS-LASSO "did not converge" (Section 2.1 footnote) - no higher-frequency evidence exists.
17. **No released artefact:** no code, no data-availability statement (frontmatter contradiction 6); the 137-characteristic dataset is described as a contribution but is not linked from the paper.
18. **Adjacent contrary evidence already in this repository:** `published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23.md` (published large-cap anomalies mostly fail a luck-adjusted null post-2005) and `binance-perpetual-cross-sectional-momentum-taker-cost-falsification-2026-09-13.md` / `binance-perpetual-cross-sectional-momentum-taker-cost-falsification` siblings showing cross-sectional long-short spreads consumed by realistic costs. These are different sources and different universes; they are recorded as adjacent contrary context, not as tests of this paper.
19. **Absence caveat:** none identified in the reviewed sources beyond the above; absence is not evidence of no negative result.

## Falsification plan

All thresholds, windows and decision rules in this section are **`research-defined falsification thresholds`** set by this Scout; none are source-reported.

- **F1 - Frozen out-of-sample replication of the headline four (primary gate).** `research-defined`: rebuild the pipeline with the screen estimated **only on Feb 2004 - Dec 2014** and the DS-LASSO tests run on **Jan 2015 - Jul 2023** without re-screening; require at least **2 of the 4** Bonferroni survivors (`ivs_convexity`, `BTX_EQV_relTail_k`, `BTX_LJV_7_5`, `bakshiKurt`) to keep `|t| > 3.02` in the held-out window. **Fail** if **0 of 4** survive, or if the paper's own screen is unreproducible out of sample.
- **F2 - Post-sample frozen forward test.** `research-defined`: extend the option panel from **2023-08-01 to the next full calendar year** with the 20 factor definitions frozen; **fail** if the four Bonferroni factors jointly show a GRS p-value `>= 0.10` and the combined maximum-Sharpe gain is `<= 0.10`.
- **F3 - Net-of-cost ladder (decisive for tradability).** `research-defined`: charge **0 / 5 / 10 / 20 / 30 bp per side** plus a two-way spread proxy on the monthly decile re-sort of the four surviving factors; **fail** at any cost level `>= 10 bp per side` where the gross-to-net Sharpe of the literal (as-signed) factor falls below **|0.20|**, since Table 4 gross Sharpes are **-0.87** and **-0.82** for the two significant-return factors.
- **F4 - Sign-reversal ablation (`research-proposed` implementation).** `research-defined`: because the source reports **negative** returns and positive `lambda_s`, test both the literal and the **sign-reversed** decile portfolio; **fail** the reversed variant if its net Sharpe `<= 0` after costs or if its advantage is confined to a single subperiod. The reversal itself is `research-proposed`, not source-reported.
- **F5 - Turnover and capacity audit.** `research-defined`: report monthly one-way turnover of each of the four factors and sweep position size from `1x` to `10x` a stated reference ADV; **fail** if net performance drops below `50%` of gross at `5x` size. (The source reports no turnover at all -> this is a pure gap-fill test.)
- **F6 - Point-in-time option-data audit.** `research-defined`: reconstruct characteristics using only quotes observable at the month-end cut-off, with an explicit staleness rule; **fail** if any of the four surviving loadings drops below `|t| = 2.0` or changes sign.
- **F7 - Screen-dependence placebo.** `research-defined`: re-run the full pipeline on **100 randomly permuted characteristic panels** (same dimensions); **fail** if the observed count of Bonferroni survivors (**4**) is not above the **95th percentile** of the placebo distribution.
- **F8 - Multiplicity-corrected family.** `research-defined`: apply Benjamini-Hochberg at **q <= 0.05** across the **full 137** characteristics (not the screened 20); **fail** if fewer than **2** characteristics survive.
- **F9 - Maturity-robustness gate.** `research-defined`: require each of the four to be selected and significant at **>= 4 of 7** maturities (1/2/3/5/10/30/60 days); **fail** for any factor that is 30-day-only (currently `bakshiKurt` and `RND_kurt_eps`).
- **F10 - Benchmark-zoo ablation.** `research-defined`: re-run against a **reduced** control set (FF5 + momentum + volatility + idiosyncratic-vol + turnover) and against the **full 160**; **fail** the incremental claim if the loadings are significant only against the reduced set.
- **F11 - Universe generalisation.** `research-defined`: extend factor formation beyond S&P 500 to the full optionable universe (Russell 3000-equivalent); **fail** if none of the four survives at `|t| > 2.0`.
- **F12 - Short-leg feasibility gate.** `research-defined`: verify borrow availability and locate cost for the short decile names over the sample; **fail** if more than **20%** of short-leg months contain names that are hard-to-borrow, or if modeled borrow cost exceeds **50 bp per year** of the factor's gross return.
- **F13 - Economic-mechanism competing-explanation test.** `research-defined`: control directly for realised volatility, beta, illiquidity and past return; **fail** the tail-risk interpretation if the four loadings collapse below `|t| < 2.0` once those characteristics enter the control set (the source itself does not identify a mechanism).
- **F14 - Action on failure.** `research-defined`: any F1/F3/F6 failure => downgrade this record to `rejected` for implementation consideration and keep it as measurement-only evidence; all failures => retain as a factor-pricing observation with no tradable claim.

## Crypto portability

**Verdict: `unproven`.**

- The evidence is entirely **US listed equity single-name options on CBOE**, monthly, on S&P 500 constituents, over **2004-2023**. The source performs **no crypto test** of any kind, so this is a **ported hypothesis, not crypto empirical evidence**.
- **What could port conceptually:** the risk-neutral-density -> tail/higher-moment characteristic pipeline (Bakshi moments, BTX jump decomposition, IV smirk/convexity) is mathematically venue-agnostic and exists for **BTC/ETH options** (Deribit, CME, IBIT-linked surfaces), which would make an `adapted` test conceivable.
- **What cuts against a direct port:**
  - **Underlying universe:** no "S&P 500 constituents" analogue; crypto cross-sections are a handful of optionable names plus a long illiquid tail, so decile sorts with **42 names per leg** are not reconstructable.
  - **Spot vs perpetual vs dated options:** crypto option surfaces are thin, with wide strikes, unreliable wings and frequent gaps - precisely where the paper's **linear out-of-the-money IV extrapolation** and kernel smoothing (Section 2.2) would dominate the tail measures being sorted on.
  - **24/7 sessions and month boundaries:** the "end of each month" formation timestamp has no closing-auction anchor; UTC month boundaries and funding intervals create artificial cut-offs (`research-proposed` adaptation required).
  - **Funding, mark/index price, liquidation, venue fragmentation:** all absent from the source and all material in crypto perps; the long-short factor would need explicit funding and liquidation handling.
  - **Short leg:** crypto borrow/short constraints and hard-to-borrow alt names differ completely from equity locates (see F12).
  - **Cost structure:** the source models **zero** costs; crypto taker/maker fees and options spread regimes are large relative to a monthly decile factor, so the gross evidence transfers even less well than in equities.
- **Conclusion:** portability is `unproven`; a crypto test would be a new study (F-style design above, on BTC/ETH options only), not a re-labeling.

## Limitations

- **`data gap` - execution economics:** order type, fill model, signal-to-order timing, latency, spread, slippage, commission, market impact, capacity, turnover, borrow cost and short availability are **not stated in source** (whole-document scan above). They must never be read as "zero".
- **`data gap` - dividend/return convention:** whether returns include dividends is not stated.
- **`data gap` - option quote field and sufficiency criterion:** bid/ask/mid/settlement used for IV fitting, minimum quote counts, moneyness coverage and the "sufficient option data" filter are not stated.
- **`data gap` - test-asset panel size:** the number `n` of test assets in the DS-LASSO cross-section is never printed.
- **`data gap` - timestamps:** timezone, quote timestamps and index-membership cut-off conventions are not stated.
- **`underspecified` - the 20-factor list as a rule:** the selected factors are conditional on a **full-sample** screen and are explicitly "representatives of groups of related measures ... rather than as uniquely identified signals" (Section 4.1); they cannot be treated as a frozen point-in-time signal list.
- **`underspecified` - P_implQ physical moments:** the source itself calls the constant `P/Q` ratio carried to longer maturities "a strong assumption".
- **`not independently reproduced`:** no reproduction by this Scout or by any record in this repository; no code or data artefact released by the source.
- **`unproven` - tradability:** the paper never claims a tradable strategy; it reports **gross** factor returns, mostly negative, and explicitly separates SDF loadings from portfolio premia.
- **In-sample by construction, no holdout, effective multiplicity > 20, unstable selection across maturities, upward-biased Sharpe benchmarks, single (S&P 500) universe, monthly-only frequency** - all source-acknowledged (Section 5).
- **Source-quality limits:** single preprint, no peer review, no data/code statement, no funding/competing-interest statement; authors' contact domains are kit-based but **affiliation is not printed on the title page**.
- **Unreconciled contradictions:** see the six items in the frontmatter `contradictions` block - notably the **Sep 25 vs Sep 28, 2026** version date and the **`lambda_s` sign vs realised return sign** conflict.

## Implementation status

`implementation_status: not-implemented`.

Nothing has been implemented in our research stack. No risk-neutral density pipeline has been built, no option panel has been assembled, no factor has been sorted, no backtest has been run, and no Qlib, Paper, Testnet or Live stage has been touched. This record is a normalised, source-traceable capture of a factor-pricing study plus a Scout-authored falsification plan.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record in the repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet or live trading. The record's `confidence: medium` refers only to the fidelity of this **research interpretation** to the pinned source - it is not confidence that the factors make money, and it is not authorisation to trade.

## Related Wiki records

Read-only `kb_search` on the Wiki Brain vault (2026-09-28) for `option-implied factor` returned **5 pages**, of which the following are materially related and verified by path:

- [[quant/option-implied-surface-cremers-weinbaum-skew-crash-regimes-2026-09-02]] - option-implied surface signals, but a crash/regime-predictability hypothesis rather than an SDF spanning test.
- [[quant/crypto-volatility-risk-premium-variance-swap-estimator-fragility-decay-2026-09-12]] - variance-risk-premium harvesting in crypto with estimator fragility; different universe, mechanism and horizon.
- [[quant/expected-shortfall-factor-model-common-tail-loss-severity-2026-09-11]] - tail-loss severity as a cross-sectional priced factor, but built from realised expected shortfall rather than option-implied densities.
- [[quant/spy-options-svi-surface-rv-falsification-adverse-selection-2026-09-12]] - SPY option surface relative value and market-making adverse selection; execution-facing, not cross-sectional pricing.

A `kb_search` for `double-selection LASSO equity characteristics cross-section` returned **0 pages**, and `factor zoo anomaly false discovery` returned **0 pages** - no Wiki link for those concepts was fabricated.

Adjacent records in **this repository** (source identity differs in every pair; four-axis distinction stated):

- `cross-market-alpha191-short-term-trading-factors-double-selection-lasso-2026-09-03.md` - **same two authors** (Alexander Walter, Maxim Ulrich) but a **different source** (arXiv:2601.06499, "Cross-Market Alpha", Du/Walter/Ulrich) and a **materially different mechanism**:168 Chinese short-term trading signals screened against 151 equity characteristics, i.e. price-based formulaic alphas, not option-implied tail densities; different signal construction, different data dependency (no option chain), different universe framing.
- `option-implied-tvs-sdf-equity-premium-forecast-sp500-2026-09-24.md` - arXiv:2607.08500 (Shiraya, Yamakami, Yamazaki): an **aggregate index-premium forecasting** SDF estimate from S&P 500 **index** options, not a cross-sectional decile-factor spanning test on single-name options.
- `option-implied-surface-cremers-weinbaum-skew-crash-regimes-2026-09-02.md` - put-call-parity / skew crash-regime predictability; different signal construction and different horizon.
- `crypto-cross-sectional-realized-kurtosis-tail-risk-premium-2026-08-31.md` - **realised** kurtosis in crypto, not option-implied; different universe, different data dependency (prices only), different market type.
- `published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23.md` (arXiv:2607.06502, Chen & Welch) - a luck-adjusted **null** on published equity anomalies; source identity differs and its mechanism is anomaly-performance decay rather than option-implied spanning.
- `btc-option-implied-vov-predicts-excess-returns-risk-premia-2026-09-19.md` - option-implied VoV predicting **crypto** excess returns; different universe and horizon.

## Sources

1. Walter, Alexander; Zimmer, Lukas; Ulrich, Maxim. *"Taming the Option Factor Zoo: A High-Dimensional Analysis"*. arXiv:2609.31263v1 [q-fin.CP], submitted 25 Sep 2026. `https://arxiv.org/abs/2609.31263` | DOI `https://doi.org/10.48550/arXiv.2609.31263`.
2. Pinned primary PDF: `https://arxiv.org/pdf/2609.31263v1` - 46 pages, 488,461 bytes, SHA-256 `70b5561b1b4c0410c1c5f1578c75d04297c502d2d6253e8f1a9cb832098daf32`, retrieved and fully read 2026-09-28 with pypdf 6.16.2 (94,210 characters / 1,984 lines). **All normalised numbers in this record were located in this PDF.**
3. HTML cross-check: `https://arxiv.org/html/2609.31263v1` (read 2026-09-28; used only to confirm identical table values).
4. Methods referenced **by the source** and not independently read for claims in this record: Feng, Giglio and Xiu (2020) DS-LASSO; Jensen, Kelly and Pedersen (2023) equity characteristics; Bakshi, Kapadia and Madan (2003); Bollerslev, Todorov and Xu (2015); Gao et al. (2018); Martin (2017); Ulrich et al. (2023) IV kernel estimator; Breeden and Litzenberger (1978); Gibbons, Ross and Shanken (1989); Ledoit and Wolf (2004); Stewart and Love (1968); Belloni, Chernozhukov and Hansen (2014); Benjamini and Hochberg (1995); Harvey et al. (2016); van Binsbergen et al. (2022, 2023); Kenneth French data library; FRED; CRSP/Compustat via Jensen et al. (2023); CBOE option data.

**Status literals:** `research-only` | `not-implemented` | `not-approved` | `approval_scope: research-only` | `not independently reproduced`.
