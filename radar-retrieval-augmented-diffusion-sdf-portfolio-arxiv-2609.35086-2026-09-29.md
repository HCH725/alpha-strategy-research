---
schema: strategy-research-record-v1
title: "RADAR retrieval-augmented diffusion market representations for SDF portfolio weights (arXiv:2609.35086v1)"
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - arxiv
  - portfolio-construction
  - stochastic-discount-factor
  - diffusion-model
  - retrieval-augmented
  - multimodal-news
  - us-equities
  - representation-learning
status: research-only
confidence: medium
source_as_of: "arXiv v1 submitted Mon, 28 Sep 2026 13:03:58 UTC; pinned HTML and abstract page read 2026-09-29"
sources:
  - "https://arxiv.org/abs/2609.35086 (abstract page, HTTP 200, 42547 bytes, SHA-256 4fd5682051eb290274a564f0f31f37bb5fd4b063fcae75b4d595c4a04d92480c, retrieved 2026-09-29)"
  - "https://arxiv.org/html/2609.35086v1 (pinned v1 HTML, HTTP 200, 348275 bytes, SHA-256 3a79399ec97e604aeb84cf1ddf69ed90ae1033a63bc263db204b1e70575bbf60, retrieved 2026-09-29, read end to end)"
  - "https://doi.org/10.48550/arXiv.2609.35086 (arXiv-issued DataCite DOI, printed as pending registration on the abstract page)"
  - "https://github.com/xinyangli5579-star/RADAR (code URL printed in the abstract; HTTP 404 on 2026-09-29, see contradictions)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Source-internal (abstract vs artifact, checked 2026-09-29): the abstract states verbatim 'Our code is available at: https://github.com/xinyangli5579-star/RADAR', but that URL returns HTTP 404, the GitHub REST repository lookup for xinyangli5579-star/RADAR returns 404, the owner account exists with public_repos = 0, its /repos listing returns an empty array with HTTP 200, and a repository search for 'RADAR stochastic discount factor' returns total_count 0. The availability claim and the retrievable artifact cannot both be true at read time; unreconciled."
  - "Source-internal (Section 5 prose vs Table 3): the text states radar 'is largely generalizable across multiple domains' on Time-MMD, while research-counting the nine printed domain rows of Table 3 shows radar has the strictly highest of the three printed values in 0 of 9 domains (No Diffusion or Gaussian is highest in every row, including the two rows the prose calls out, Security and Traffic). The prose claim and the printed table are not reconciled in the pinned text."
  - "Source-internal (Appendix D Tables 6-7 inference convention): the printed p-values reproduce as one-sided normal tail probabilities (research-computed: radar CAPM t = 2.159 gives one-sided 0.0154 vs printed 0.016 and two-sided 0.0309; radar FF3 t = 1.814 gives one-sided 0.0348 vs printed 0.035 and two-sided 0.0697; MLP FF3 t = 0.870 gives one-sided 0.1922 vs printed 0.192), yet Appendix D never states the sidedness (Appendix B does state one-sided for its own difference tests) and the prose calls the 15.47 percent FF3 alpha 'statistically significant at the 5 percent level'. Under the conventional two-sided reading that alpha is not significant at 5 percent (two-sided p about 0.070)."
  - "Source-internal (Table 1 CumRet vs AnnRet aggregation): research-computing T = ln(1 + CumRet) / ln(1 + AnnRet) for all thirteen Table 1 rows gives 4.96 to 5.50 years, hitting 5.00 to 5.04 for nine rows but 5.50 for HAN, StockNet, iTransformer and NGAT, while the experimental design implies five consecutive one-year out-of-sample windows (Section 4 rolling protocol, Figure 5 caption 'aggregated over 5 rolling windows'). No annualization or aggregation convention is printed that reconciles the two columns at the stated precision for all rows."
---

# RADAR: retrieval-augmented diffusion market representations for SDF portfolio weights (arXiv:2609.35086v1)

## Provenance

- **Primary source:** Kelvin J.L. Koa, Xinyang Li and Ke-Wei Huang, *"Retrieval-Augmented Diffusion Modeling for Stochastic Discount Factor Portfolios"*, arXiv preprint **arXiv:2609.35086v1 [cs.LG]**, masthead stamp `arXiv:2609.35086v1 [cs.LG] 28 Sep 2026`.
- **Authors (exactly as printed in the pinned HTML title block):** Kelvin J.L. Koa; Xinyang Li (marked `* Equal contribution`); Ke-Wei Huang (printed with a dagger symbol next to `Corresponding author`). Affiliations printed on the title block: **National University of Singapore** and **Asian Institute of Digital Finance**. Emails printed: `kelvin.koa@u.nus.edu`, `xinyangli5579@gmail.com`, `dishkw@nus.edu.sg`. No ORCID is printed.
- **Version / date:** single version **v1**, submission history `Mon, 28 Sep 2026 13:03:58 UTC (2,223 KB)`, submitted by Kelvin Koa. Read from the abstract page 2026-09-29.
- **Subjects:** Machine Learning (cs.LG); Computational Finance (q-fin.CP); Portfolio Management (q-fin.PM). Primary category cs.LG.
- **Comments field:** `NeurIPS 2026`. This is a self-reported conference acceptance in the arXiv Comments field; **no journal reference, no proceedings reference and no publisher DOI are printed**, so publication status is recorded as `conference acceptance claimed in source, not independently verified`. Peer-review status otherwise `not stated in source`.
- **DOI:** `https://doi.org/10.48550/arXiv.2609.35086`, printed on the abstract page as `DOI via DataCite (pending registration)`.
- **License:** `CC BY 4.0` (printed in the HTML masthead).
- **Pinned primary text:** `https://arxiv.org/html/2609.35086v1` -- HTTP 200, **348,275 bytes**, SHA-256 `3a79399ec97e604aeb84cf1ddf69ed90ae1033a63bc263db204b1e70575bbf60`, retrieved 2026-09-29 and read end to end: abstract, Sections 1-6, Equations (1)-(16), Tables 1-7, Figure 1-10 captions, References, Appendix A (diffusion formulation), Appendix B (significance and robustness), Appendix C (cross-sectional analysis), Appendix D (CAPM and Fama-French).
- **Abstract page:** `https://arxiv.org/abs/2609.35086` -- HTTP 200, **42,547 bytes**, SHA-256 `4fd5682051eb290274a564f0f31f37bb5fd4b063fcae75b4d595c4a04d92480c`, read 2026-09-29 for submission history, Comments, Subjects and DOI status.
- **PDF:** not downloaded; PDF byte count and PDF checksum = `data gap`.
- **Stated code artifact:** `https://github.com/xinyangli5579-star/RADAR` (printed at the end of the abstract). Checked 2026-09-29: HTTP 404; GitHub REST `repos/xinyangli5579-star/RADAR` returns 404; owner account `xinyangli5579-star` exists (user id 246965837) with `"public_repos": 0` and an empty `/repos` array at HTTP 200; repository search for `RADAR stochastic discount factor` returns `total_count 0`. **No commit SHA can be preserved because no repository is retrievable** - recorded as contradiction 1 and as a reproducibility `data gap`, not silently dropped.
- **Repository dedup (hidden-inclusive, before writing):** `rg -uuu -l -F` across the entire checkout including `.git`, `.mimo-worktrees`, `.agents`, `.hermes` and `coverage_manifest.csv` returned **zero files** for each of `2609.35086`, `xinyangli5579`, `Retrieval-Augmented Diffusion`, `Stochastic Discount Factor Portfolios`, `Kelvin J.L. Koa` and `context-aware denoising`; `coverage_manifest.csv` (1,088,787 bytes) returned 0 matches for `2609.35086` / `xinyangli5579` / `Retrieval-Augmented Diffusion`; positive control `novy-marx` returned **23 files** in the same session. Phrase-only neighbours found by content search are listed under Related Wiki records with their four-axis distinction. `git log --oneline -20` was used as a convenience glance only and does not substitute for the identity search above.

## Economic mechanism

### Source-reported

- The source frames portfolio construction as **stochastic discount factor (SDF) estimation** rather than return forecasting: given weights `w_hat_t` and next-period returns `r_{t+1}`, the SDF is defined as `1 - w_hat_t' r_{t+1}` and training minimises `L_SDF = E_t[(1 - w_hat_t' r_{t+1})^2] + lambda * ||w_hat_t||_2^2` (Equation 3), because minimising the second moment prices every asset with zero error. The stated intuition is that systematic pricing error means the learned market representation failed to capture structure that the inputs contain.
- Two stated failure modes motivate the proposal: (i) **non-stationarity** - regime shifts bias models toward whichever regimes dominate the sample; (ii) **noisy text** - news embeddings carry irrelevant content. Standard diffusion is said to fail because isotropic Gaussian noise is independent of the input and does not reflect the state-dependent, heteroskedastic nature of financial uncertainty.
- The proposed remedy, **radar (Retrieval-Augmented Diffusion-based Assets Representation)**, has three claimed roles: retrieval of historically similar event segments supplies a **regime-conditioned noise distribution**; conditional diffusion **denoises** the price and news embeddings; and the diffusion process is **initialised with the empirical mean and variance of the retrieved contexts** so the denoising trajectory is grounded in conditional rather than unconditional statistics.
- Claimed economic payoff (abstract and Section 1): state-of-the-art Sharpe, Sortino and Calmar, plus representations whose cosine similarity ordering tracks realised return correlation (Figure 5) and whose MLP-scored quintiles produce a monotonic NAV ordering (Figure 6), i.e. "economically meaningful signals on asset returns and correlations".

### Research interpretation

- Hypothesised mechanism in falsifiable form: **regime-conditional denoising of a multimodal market state reduces estimation noise in an under-determined SDF objective, so the resulting long/short cross-sectional weights carry more per-unit-risk signal than (a) the same model without retrieval, (b) the same model without denoising, and (c) naive equal weighting.** The channel is variance reduction in the weight-estimation step, not a newly identified risk premium: nothing in the pinned text claims a structural premium, and the factor regressions in Appendix D are explicitly framed as separating signal extraction from common risk premia.
- Component roles (ablation evidence is source-reported, Table 2): regime retrieval = the differentiator (full model 1.062 vs +Embeddings 0.859 vs +Diffusion 0.411); denoising = helpful only when retrieval supplies the noise (the +Diffusion-only row is *below* the plain SDF baseline of 0.505); news modality = contributory (w/o News 0.650, below the Equal Weight benchmark of 0.795); price modality = dominant (w/o Price 0.797). Under this reading the economically interesting claim is narrow: **retrieval-conditioned noise, not diffusion per se.**
- Alternative competing explanations that the source does not exclude: beta and factor exposure (radar beta 0.977, i.e. essentially market-level), higher realised volatility than the benchmarks (0.271 vs 0.200 Equal Weight and 0.191 S&P 500), gross-of-cost reporting with no turnover figure, ex-post intersection of index membership with news coverage, and test-set selection of the retrieval size K.
- This is a **ported hypothesis**: the empirical basis is US large-cap equities only. See Crypto portability.

## Signal

Everything below is `source-reported` unless explicitly labelled `research-proposed` or `data gap`.

- **Formation timestamp:** at each time step `t` the model observes the price window `x_t^(p)` and the news observed at `t`. Event segments are cut at news arrival times `tau_i` (Section 3.3, Equation 7); retrieval is restricted to `tau_i < t` (Equations 8-9), so the retrieved context is strictly causal in the printed formulation. Publication-lag handling of FNSPID articles (article timestamp vs market timestamp) is `data gap` - not stated in source.
- **Lookback:** input sequence length **60 trading days** (Implementation Details); encoders are GRUs with additive attention pooling, hidden dimension **64**; price and text representations are fused by a bilinear layer with ReLU (Equation 6). Event segments span from a news event to just before the next news event.
- **Retrieval:** top-**K = 10** neighbours per modality by cosine similarity, context bank refreshed **every 5 epochs** (Implementation Details). K was chosen from a reported sweep (Figure 4) whose selection split is `data gap` - the paper does not state whether K was chosen on validation or on the reported test windows.
- **Denoising:** dual-path forward diffusion with **T = 100** timesteps, linear noise schedule, noise drawn from the retrieved per-modality mean and variance (Equations 11-12); x0-prediction denoisers conditioned on the joint market representation and the diffusion step (Equation 13); reconstruction objective is an **unweighted** squared error (Equation 14), with Appendix A stating explicitly that the timestep- and covariance-dependent weighting is dropped.
- **Final representation:** `z_hat_t = (1 - gamma) * (q_hat_t + c_hat_t) + gamma * q_t` (Equation 15). **The value of `gamma` is never printed** - `data gap`. Likewise `rho` (diffusion/SDF loss balance, Equation 16) and `lambda` (L2 weight penalty, Equation 3) are never printed - `data gap`.
- **Weight map:** `w_hat_t = g(z_hat_t)` (Equation 2). The architecture of `g` is not specified for the main model - `data gap`. **No sign, gross-exposure, leverage, margin or position constraint is printed** (the words `gross`, `long-only` and portfolio-use `constraint` have zero occurrences) - whether the strategy shorts is `not stated in source`.
- **Entry / exit:** the model outputs portfolio weights that are held until the next rebalance; **rebalancing horizon H = 7 trading days** at default (robustness sweep H in {1, 7, 20}, input length L in {60, 120}, Figure 7). Signal-to-order timing, whether rebalance prices are the same close or the next session, and tie handling are `data gap`.
- **Baselines' portfolio rule (needed to read Table 1):** forecasting baselines (StockNet, HAN, NGAT, iTransformer, RATD) are converted to portfolios by **ranking predicted returns and equally weighting the top 50 stocks at each rebalancing date** (Section 4); portfolio-optimisation baselines (BSV, DKKM, MLP, LinAttn, SDF) learn weights directly. Benchmarks are the S&P 500 index and an Equal Weight portfolio.
- **Training:** AdamW with cosine annealing, 50 epochs, early stopping patience 10, gradient clipping at 1.0, single NVIDIA GeForce RTX 4090 (Implementation Details). Optimiser hyper-parameters, batch size and the train/validation boundary rule (only "90:10 train/validation split" inside each 4-year window) are otherwise `data gap`.
- **Overall reconstruction status:** the mechanism and the hyper-parameters that are printed are reproducible in outline, but `gamma`, `rho`, `lambda`, the weight head `g`, all weight constraints, all cost and fill rules and the seed aggregation behind Table 1 are missing, so the signal is **underspecified** and must not be presented as reproducible evidence.

## Required data

- **Instrument / universe:** 377 US equities that appear **both** in the S&P 500 index and in the FNSPID news corpus (Section 4). Whether index membership is point-in-time or as-of-now is `not stated in source`; the words `point-in-time` and `survivorship` have zero occurrences in the pinned text, so survivorship and news-coverage selection are open.
- **Sample period:** **June 2011 to June 2020**, about **2,270 trading days** (Section 4).
- **Venue / market type:** US equity cash market; daily adjusted close prices from **Yahoo Finance**; no derivatives, no perpetuals, no funding.
- **Text data:** **FNSPID** (Dong et al., 2024, reference [10]) news articles, daily granularity; the source's own Limitations note calls FNSPID "relatively sparse in coverage" and names Bloomberg/Reuters as the more comprehensive but proprietary alternative.
- **Timeframe / fields:** daily OHLCV adjusted closes (Table 1 sample shows AAPL, ADBE, AMZN, BAC, BRK-B from 2000-01-03 for the raw Yahoo extract; the radar experiment window starts June 2011); news timestamps at day granularity; the raw extract in Section 3 covers 105,680 rows (20 stocks x 5,284 trading days) for the earlier dataset description, which does **not** equal the 377-stock radar panel - the exact ticker list is `data gap`.
- **Point-in-time / availability:** rolling-window protocol is stated to avoid look-ahead (Section 4: each window uses 4 years for training with a 90:10 train/validation split, the subsequent 1 year for out-of-sample testing, rolling forward by 1 year). Reconstitution schedule, constituent timing and news availability lag: `data gap`.
- **Benchmark and factor data:** S&P 500 index for benchmarking; risk-free rate `R_f` and the SMB/HML factors for Appendix D are used in the printed equations but **their source and level are never stated** - `data gap`.
- **Missing-data handling:** the source only says it checks for missing data in Section 3; imputation, suspension and stale-print rules: `data gap`.
- **Cost / fee / spread needs:** **not stated in source** - see Execution assumptions.

## Execution assumptions

Cost treatment was determined from a Methods-level read of Sections 3.1-3.5 (problem formulation, encoders, retrieval, diffusion, joint objective), Section 4 (Experiments: dataset, baselines, Implementation Details), Section 5 (Results), Appendices B-D, plus a whole-document term census of the pinned HTML text:

- **Zero modelled occurrences** of: `transaction cost`, `transaction`, `cost`, `commission`, `slippage`, `bid-ask`, `bid ask`, `spread`, `turnover`, `market impact`, `latency`, `execution`, `friction`, `liquidity`, `capacity`, `participation`, `fee` (the single `fee` hit is the word "feedback" in the HTML footer), `funding` (single hit is the arXiv "Major funding support" footer), `margin` (single hit is "marginal distribution" in Appendix A), `leverage` (four hits are the verb "leverages"), `bid`, `long-only`, `point-in-time`, `survivorship`.
- Consequently **every performance figure in this record is gross of cost**, and order type, fill model, signal-to-order delay, execution price convention, fees, spread, slippage, impact, participation, position limits, margin, financing, borrow and capacity are **`data gap`, never zero.**
- **Rebalance cadence:** H = 7 trading days at default (Figure 7 sweeps H in {1, 7, 20}); a full 377-stock weight vector is re-solved at each rebalance, but **turnover is never reported** (0 occurrences) and no weight-constraint block is printed.
- **Benchmark construction:** Equal Weight and S&P 500 are printed as reference rows; no cost-matched or turnover-matched baseline exists in the pinned text.
- **What the source assumes vs what we assume:** the source assumes nothing about costs; any executable-price, fee or spread treatment used later is `research-proposed` and lives in the Falsification plan, not in this section.

## Evidence

### Source-reported

All figures below are third-party claims from arXiv:2609.35086v1 and have **not** been independently reproduced. Asset class: **US large-cap equities (S&P 500 names), June 2011-June 2020**; they are not crypto evidence.

- **Table 1 (out-of-sample, pooled over the rolling protocol, gross of cost), columns Sharpe / Sortino / Calmar / CumRet / AnnRet / MaxDD / Vol:**
  - **radar** `1.062 / 1.352 / 0.924 / 2.502 / 0.285 / 0.308 / 0.271` (best in five of the seven columns; not best on MaxDD or Vol)
  - Equal Weight `0.795 / 0.873 / 0.393 / 1.005 / 0.149 / 0.380 / 0.200`; S&P 500 `0.513 / 0.576 / 0.244 / 0.487 / 0.083 / 0.339 / 0.191`
  - Forecasting baselines: HAN `0.705 / 0.816 / 0.355 / 0.892 / 0.123 / 0.347 / 0.191`; StockNet `0.780 / 0.899 / 0.387 / 1.218 / 0.156 / 0.404 / 0.216`; iTransformer `0.758 / 0.877 / 0.393 / 0.997 / 0.134 / 0.342 / 0.190`; NGAT `0.710 / 0.817 / 0.334 / 0.893 / 0.123 / 0.369 / 0.189`; RATD `0.680 / 0.754 / 0.302 / 0.844 / 0.130 / 0.431 / 0.214`
  - Portfolio-optimisation baselines: BSV `0.361 / 0.481 / 0.164 / 0.252 / 0.046 / 0.281 / 0.160`; DKKM `0.367 / 0.489 / 0.177 / 0.229 / 0.042 / 0.238 / 0.139`; LinAttn `0.407 / 0.558 / 0.326 / 0.195 / 0.036 / 0.111 / 0.100`; MLP `0.502 / 0.710 / 0.406 / 0.203 / 0.038 / 0.093 / 0.080`; SDF `0.505 / 0.690 / 0.313 / 0.211 / 0.039 / 0.125 / 0.083`
- **Table 2 (ablation, same columns):** w/o News `0.650 / 0.821 / 0.304 / 1.229 / 0.174 / 0.573 / 0.332`; w/o Price `0.797 / 0.878 / 0.395 / 1.003 / 0.149 / 0.377 / 0.200`; SDF baseline `0.505 / 0.690 / 0.313 / 0.211 / 0.039 / 0.125 / 0.083`; +Embeddings `0.859 / 0.959 / 0.429 / 1.138 / 0.164 / 0.383 / 0.201`; **+Diffusion `0.411 / 0.466 / 0.108 / 0.501 / 0.085 / 0.784 / 0.525`** (below the plain SDF baseline; the source calls this "unexpectedly"); full radar `1.062 / ...` as above.
- **Table 3 (Time-MMD generalisation, Sharpe, columns No Diffusion / Gaussian / radar):** Agriculture `2.328 / 2.375 / 2.240`; Climate `0.484 / 0.464 / 0.464`; Energy `1.753 / 0.540 / 0.517`; Environment `0.931 / 0.946 / 0.928`; Health (AFR) `2.413 / 4.203 / 1.635`; Health (US) `1.007 / 0.956 / 0.821`; Security `1.526 / 1.584 / 1.557`; SocialGood `0.953 / 0.547 / 0.512`; Traffic `1.154 / 1.350 / 1.290`.
- **Table 4 (pooled significance, radar minus each baseline, "taken from observations across five random seeds"), columns Monthly p / HAC p / DM p / LW p:** Equal Weight `0.0016 / 0.0015 / 0.0015 / 0.0079`; HAN `0.0015 / 0.0016 / 0.0016 / 0.0105`; StockNet `0.0021 / 0.0030 / 0.0030 / 0.0137`; iTransformer `0.0041 / 0.0042 / 0.0041 / 0.0402`; NGAT `0.0011 / 0.0013 / 0.0012 / 0.0081`; RATD `0.0003 / 0.0005 / 0.0005 / 0.0018`; BSV `0.0026 / 0.0050 / 0.0050 / 0.0086`; DKKM `0.0017 / 0.0014 / 0.0014 / 0.0071`; MLP `0.0029 / 0.0024 / 0.0024 / 0.0140`; LinAttn `0.0045 / 0.0052 / 0.0052 / 0.0253`; SDF `0.0046 / 0.0036 / 0.0035 / 0.0189`. Tests are declared **one-sided** in Appendix B (monthly t, Newey-West HAC, Diebold-Mariano, Ledoit-Wolf).
- **Table 5 (robustness), columns Bootstrap p / Boot-delta-Sharpe p / Fisher HAC p / Fisher Monthly p:** Equal Weight `0.0023 / 0.0153 / 0.0012 / 0.0020`; RATD `0.0012 / 0.0044 / 0.0005 / 0.0010`; SDF `0.0032 / 0.0437 / 0.0013 / 0.0021`; the remaining eight baselines lie between these, with the largest printed value 0.0437.
- **Table 6 (CAPM on daily returns):** radar `alpha 18.71%, t 2.159, p 0.016, beta 0.977, R2 0.476`; Equal Weight `4.78%, 2.712, 0.003, 1.030, 0.957`; BSV `6.60%, 1.614, 0.053, 1.248, 0.849`; DKKM `4.10%, 2.403, 0.008, 1.019, 0.960`; MLP `4.86%, 1.864, 0.031, 0.893, 0.897`; LinAttn `7.13%, 2.208, 0.014, 1.051, 0.859`; SDF `5.34%, 1.352, 0.088, 0.983, 0.816`.
- **Table 7 (Fama-French three-factor):** radar `alpha 15.47%, t 1.814, p 0.035, beta_m 0.988, beta_SMB 0.064, beta_HML -0.173, R2 0.488`; Equal Weight `4.63%, 3.233, 0.001, 0.999, 0.079, 0.159, 0.975`; BSV `8.73%, 2.833, 0.002, 1.192, 0.402, 0.327, 0.918`; DKKM `3.88%, 2.735, 0.003, 0.988, 0.042, 0.156, 0.974`; MLP `2.30%, 0.870, 0.192, 0.892, -0.079, -0.064, 0.896`; LinAttn `8.05%, 2.448, 0.007, 1.007, 0.134, 0.245, 0.889`; SDF `7.42%, 2.002, 0.023, 0.927, 0.108, 0.347, 0.863`.
- **Figure-only claims (values not printed in the text layer, therefore `data gap` for reproduction):** Figure 4 top-K sweep with cross-seed coefficient of variation; Figure 5 embedding-similarity vs realised-correlation deciles "aggregated over 5 rolling windows"; Figure 6 Q1-Q5 NAV separation; Figure 7 radar "consistently highest across all six (L, H) configurations"; Figures 8-10 volatility-group and sector breakdowns (prose says gains are largest in Information Technology and Financials and limited in Energy and Real Estate).
- **Research-computed cross-checks of printed values (arithmetic only, no model run):**
  1. `Calmar = AnnRet / MaxDD` reproduces for **13 of 13** Table 1 rows to within 0.003 (e.g. radar 0.285/0.308 = 0.925 vs printed 0.924; S&P 500 0.083/0.339 = 0.245 vs 0.244).
  2. Implied horizon `T = ln(1 + CumRet) / ln(1 + AnnRet)` is 4.96-5.50 across Table 1 (five rows near 5.00, four rows at 5.50) - basis for contradiction 4.
  3. Reported Sharpe exceeds `AnnRet / Vol` in **13 of 13** rows by 0.010 to 0.078 (radar 1.052 vs 1.062; Equal Weight 0.745 vs 0.795), consistent with an arithmetic-mean annualisation and/or an unstated risk-free convention - recorded as `data gap`, not as an error.
  4. radar is best in **5 of 7** Table 1 columns; Equal Weight is second on Sharpe (0.795 > StockNet 0.780), matching the source's prose claim.
  5. radar is strictly best in **0 of 9** Table 3 domain rows - basis for contradiction 2.
  6. Tables 6-7 p-values match a **one-sided** normal tail to 0.0001 in 6 of 6 spot checks - basis for contradiction 3.

### Independently reproduced

not independently reproduced

Only the arithmetic cross-checks listed above were executed (they verify internal consistency of printed cells, not the strategy). No model was trained, no data was downloaded, no portfolio was constructed, no backtest was run, and the stated code repository is not retrievable.

### Negative evidence

1. **No cost model of any kind.** `transaction cost`, `transaction`, `cost`, `commission`, `slippage`, `spread`, `bid-ask`, `turnover`, `market impact`, `latency`, `execution`, `friction`, `liquidity` and `capacity` all return zero occurrences in the pinned text, so the entire headline is gross of cost while a 377-stock book is re-solved every 7 trading days with unreported turnover.
2. **The naive Equal Weight benchmark is the second-best row in the whole table** (Sharpe 0.795), and the source's own text states that the forecasting baselines "remain relatively consistent with each other and similar to equal-weighting" and that "forecasting ability might not matter much in a real-life multi-asset portfolio setting."
3. **The diffusion component alone is negative-value:** Table 2 `+Diffusion` Sharpe 0.411 is below the plain SDF baseline 0.505, with MaxDD 0.784 and Vol 0.525 the worst in the table; the source acknowledges this and attributes it to arbitrary Gaussian noise.
4. **Cross-domain generalisation does not hold in the printed table:** radar is strictly best in 0 of 9 Time-MMD domains (research-counted).
5. **One-sided inference behind the alpha claim** (research-computed): the 15.47 percent FF3 alpha is significant only one-sided; two-sided p is about 0.070, and the paper does not state the sidedness in Appendix D.
6. **No multiple-comparison control:** Table 4 contributes 11 baselines x 4 tests and Table 5 another 11 x 4, i.e. 88 printed p-values; `Benjamini`, `FDR` and `multiple test` all return zero occurrences, so family-wise or false-discovery control is absent.
7. **Seed dispersion of the headline table is unknown:** five random seeds are mentioned only for Table 4 and Figure 4; Table 1 carries no seed aggregation statement, so 1.062 has no printed dispersion.
8. **Hyper-parameters required to rebuild the model are missing:** `gamma` (Equation 15), `rho` (Equation 16), `lambda` (Equation 3), the weight head `g`, and every weight constraint (sign / gross exposure / leverage / margin) are unstated.
9. **Selection of K = 10 is not shown to be validation-only:** Figure 4 reports the sweep whose numbers are also the reported performance view; the split used for choosing K is not stated, so test-set selection cannot be excluded.
10. **Universe construction is ex post and unexamined:** the panel is the intersection of S&P 500 membership with FNSPID news coverage; `point-in-time` and `survivorship` have zero occurrences, so both index survivorship and news-coverage selection are open.
11. **News coverage sparsity is a source-declared limitation:** FNSPID is described as "relatively sparse in coverage", and the w/o News ablation (0.650) already falls below Equal Weight (0.795), so the news arm's marginal contribution is bounded by corpus quality.
12. **No retrievable artifact:** the abstract's code URL returns 404 and the owner account has zero public repositories (checked 2026-09-29), so no independent replication path exists today.
13. **No statistical statement for the figure-based claims:** Figures 4-10 carry the representation, robustness, sector and volatility-regime arguments, but their numeric values are not in the text layer and no printed statistic accompanies Figures 5 and 6 - `data gap`.
14. **Beta is essentially one:** radar beta 0.977 (Table 6) and 0.988 (Table 7) with R2 0.476/0.488; the source itself says this is "moderate market exposure rather than a market-neutral strategy".
15. **Higher benchmark volatility:** radar Vol 0.271 exceeds Equal Weight 0.200 and S&P 500 0.191, and radar MaxDD 0.308 is worse than every portfolio-optimisation baseline (0.093-0.238), so the Sharpe gain comes with a materially deeper peak-to-trough.
16. **Risk-free rate unspecified:** Sharpe and Sortino are printed without the Rf source or level, and Appendix D uses `R_f` without defining it - `data gap`.
17. **Execution price convention unstated:** adjusted closes are used for signals; whether rebalances trade at the same close, the next open, or are simply marked, is not stated - `data gap`.
18. **No capacity, participation or liquidity analysis** anywhere in the pinned text (all four terms zero).
19. **Evidence window ends June 2020:** no out-of-sample evidence after 2020-06, no temporal subperiod table, and no frozen forward window; the only breakdowns are cross-sectional (volatility groups, sectors).
20. **Single asset class, single market, single corpus:** US large-cap equity cash market plus one news corpus; nothing about futures, options, perps, funding or 24/7 sessions.
21. **Baseline conversion rule may understate the forecasting models:** they are forced through a top-50 equal-weight portfolio, a construction the source argues neutralises forecast differences, so the comparison does not isolate forecasting skill; no turnover-matched or cost-aware baseline exists.
22. **Publication status is self-reported:** the `NeurIPS 2026` comment has no proceedings or journal reference to verify, so venue-based quality priors must not be applied.
23. **None identified in the reviewed external literature for this specific source** beyond the above; absence of a contrary study is not evidence of no negative result.

## Falsification plan

All thresholds, windows and decision rules below are **research-defined falsification thresholds** (none is source-reported) and apply to a `research-proposed` operationalisation. Each gate has an action on failure, and **retuning is not permitted to rescue a failed gate**.

- **F1 - Printed-value reproduction.** Rebuild Table 1, Table 2, Table 6 and Table 7 from the released artifact and data. Pass = every printed ratio reproduced within +/- 0.001 and every printed return within +/- 0.1 percentage points. Fail = mark the source's evidence non-reproducible and return the candidate to Research Intake Review as REMEDIATE.
- **F2 - Artifact availability.** Pass = a code URL named by the source resolves to a public repository with a full commit SHA that builds. Fail = the record stays `research-only` and no downstream candidate-pool entry may cite reproduction. **Currently failing (404, public_repos 0, checked 2026-09-29).**
- **F3 - Cost ladder.** Apply research-proposed costs of 0 / 1 / 2 / 5 / 10 / 20 bps per side plus a half-spread term on every weight change, at H = 7. Pass = radar's gross Sharpe advantage over Equal Weight (1.062 - 0.795 = +0.267) remains >= +0.10 net at 5 bps. Fail = the claim is a cost artefact; reject.
- **F4 - Turnover gate.** Report annualised one-way turnover of the radar book. Pass = turnover <= 100 percent per year, or, if higher, net Sharpe at 10 bps still exceeds net Equal Weight. Fail = reject as non-investable at the reported capacity.
- **F5 - Executable-price gate.** Re-run with signals formed on the close and orders sent at the next session open, crossing the quoted spread both ways. Pass = net Sharpe advantage over Equal Weight stays positive. Fail = reject.
- **F6 - Inference gate.** Re-estimate Tables 4-7 with two-sided tests plus Benjamini-Hochberg at q < 0.10 over the full 88-comparison family. Pass = radar still beats every baseline family representative at q < 0.10 and the FF3 alpha is two-sided p < 0.05. Fail = withdraw the "statistically significant alpha" wording and cap the record at descriptive status.
- **F7 - Retrieval placebo.** Replace retrieved contexts with (a) temporally shuffled event segments of identical count and (b) a global-moment Gaussian matched on the retrieved mean/variance. Pass = full radar beats both placebos by >= +0.10 Sharpe (research-defined). Fail = the retrieval mechanism, not the model, carries no information; reject the mechanism claim.
- **F8 - Component ablation gate.** Confirm the printed ordering `SDF 0.505 < +Embeddings 0.859 < radar 1.062` and `+Diffusion 0.411 < SDF 0.505`. Pass = radar must beat `+Embeddings` by >= +0.10, otherwise the diffusion machinery is unnecessary and the hypothesis is reduced to representation learning. Fail = reject the diffusion-specific claim, keep at most a representation-learning hypothesis.
- **F9 - Seed stability.** Ten seeds with all hyper-parameters frozen. Pass = at least 8 of 10 seeds beat Equal Weight 0.795 and the mean is >= 1.00. Fail = label the headline unstable.
- **F10 - Point-in-time universe.** Rebuild with point-in-time S&P 500 membership and news coverage known at each formation date, plus an all-constituents (no news-coverage intersection) control. Pass = radar's Sharpe advantage over Equal Weight is >= +0.10 in both variants. Fail = survivorship/coverage selection explains the result; reject.
- **F11 - News-timestamp placebo / competing explanation.** Destroy the news timing by circularly shifting article timestamps within each year while keeping the price panel fixed. Pass = the shifted variant's advantage falls to <= +0.05 while the true-timing variant stays >= +0.10; additionally the beta must stay <= 1.10. Fail = the gain is beta or market structure, not news-conditioned retrieval; reject.
- **F12 - Subperiod and factor robustness.** Split the five test windows into 2015-2017 and 2018-2020. Pass = both subperiods show a positive Sharpe advantage over Equal Weight and CAPM/FF3 alpha stays positive two-sided. Fail = regime-limited result; label as regime-dependent and block adoption.
- **F13 - Frozen forward window.** Freeze every hyper-parameter (`gamma`, `rho`, `lambda`, K = 10, H = 7, L = 60) and evaluate 2020-07-01 through 2026-06-30 on the same universe rule. Pass = strictly positive Sharpe advantage over Equal Weight net of the F3 5-bps ladder. Fail = hypothesis rejected; no retuning, new record required for any revised rule.
- **F14 - Cross-market replication.** Repeat on two of three independent panels: (a) a second equity market (e.g. STOXX 600 with an equivalent news corpus), (b) a US small/mid-cap panel, (c) crypto top-30 liquid spot with a crypto-native news corpus. Pass = >= +0.10 net Sharpe advantage over Equal Weight in at least 2 of 3. Fail = label market-specific and restrict any future hypothesis to the original market.

Action-on-failure map: F1/F2 fail -> REMEDIATE (no candidate-pool entry); F3/F4/F5 fail -> REJECT as non-investable; F6 fail -> downgrade to descriptive evidence only; F7/F8 fail -> REJECT the mechanism claim (representation-learning variant may be re-registered as a new source-backed hypothesis); F9/F10/F11/F12/F13 fail -> REJECT with the recorded failure as negative evidence; F14 fail -> portability marked `unproven` and any crypto hypothesis requires a fresh record.

## Crypto portability

**adapted** (performance in crypto: `unproven`).

- **Why not `direct`:** every empirical result in the pinned source is US large-cap equity options-free cash-market evidence over June 2011-June 2020 with an FNSPID news corpus; the words `crypto`, `Bitcoin` and `Ethereum` do not appear as an experimental domain in the pinned text (Time-MMD domains in Table 3 are agriculture, climate, energy, environment, health, security, social good, traffic - none is a traded crypto market).
- **What plausibly ports:** the mechanism is instrument-agnostic in form - a market-state representation, an SDF-style second-moment objective `E[(1 - w'r)^2]`, context retrieval over event segments and a diffusion denoiser need no equity-specific primitive. Cross-sectional daily rebalancing of a multi-asset book is directly available on crypto spot and perpetual panels.
- **What does not port as stated:** (i) the news arm depends on FNSPID, which has no crypto coverage - a crypto corpus with reliable timestamps would be a new material data dependency; (ii) equity daily closes and the third-way session clock are replaced by 24/7 candles and exchange-specific daily boundaries, which changes what an "event segment" is; (iii) crypto adds funding, mark/index price, liquidation and venue-fragmentation effects that the source never models (`funding`, `margin`, `leverage` have zero modelled occurrences); (iv) S&P 500 index membership has no analogue, so the universe rule must be re-specified (listing age, liquidity floors, survivorship handling) - research-proposed; (v) crypto spreads and impact are typically wider, which interacts directly with the missing cost model (F3/F5 gates).
- **Crypto-specific risks to state explicitly:** spot vs perpetual basis and funding carry; index/mark price vs last price at rebalance; 24/7 sessions and candle-boundary alignment; listing and delisting survivorship; single-venue vs multi-venue liquidity fragmentation; stablecoin quote-currency effects; custody and withdrawal constraints.
- Crypto portability is **not** authorisation to trade, and no crypto result exists for this source.

## Limitations

- `underspecified`: `gamma`, `rho`, `lambda`, the weight head `g`, all portfolio constraints, the risk-free rate, execution price convention, seed aggregation for Table 1, the K-selection split, and the CumRet/AnnRet aggregation convention.
- `data gap`: PDF bytes and checksum (PDF not downloaded); FNSPID article availability lag; ticker list for the 377-stock panel; numeric values behind Figures 4-10; any cost, fill, turnover, capacity or margin field (never printed, never inferred as zero).
- `not independently reproduced`: no training, no backtest, no data download, no artifact (repository 404).
- `unproven`: profitability net of any cost; portability to crypto; stability after 2020-06; robustness to point-in-time universe construction.
- Source quality: arXiv v1 preprint with a self-reported `NeurIPS 2026` comment and no journal reference - peer-review status `not stated in source`.
- Incremental-write threshold was respected: this is a new family (retrieval-conditioned diffusion for SDF weight learning) with a distinct source identity; no existing repository record shares its mechanism or source.
- Publication-bias and selection concerns: a single research group produced all rows (radar plus all baselines re-run in-house), there is no external replication, and the headline is the best row of a 13-row table chosen under an unstated seed and hyper-parameter protocol.

## Implementation status

`implementation_status: not-implemented`.

Nothing from this record has been implemented in our research stack: no strategy family, no prototype, no historical backtest run in our systems, no Paper, Testnet or Live verification, no Qlib full-backtest validation, no dependency installation, no market-data download. The only executed work for this record was reading the pinned primary text end to end, arithmetic cross-checks of printed cells, read-only dedup searches and a read-only code-URL availability check.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record means only that normalised, source-traceable research material exists in the public staging pool. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. Research capture is not strategy adoption and not permission to run Paper/Testnet/Live.

## Related Wiki records

Read-only `kb_search` queries were run against Hermes Wiki Brain; nothing was written.

- Query `stochastic discount factor portfolio deep learning` returned 4 verified adjacent pages: `quant/chronos-foundation-transformer-statistical-arbitrage-factor-residuals-2026-09-12.md`, `quant/model-free-statistical-arbitrage-empirical-mean-reversion-time-reinforcement-learning-2026-09-05.md`, `quant/exploratory-reinforcement-learning-sequential-optimal-stopping-pairs-trading-2026-09-05.md`, `quant/continuous-macro-timing-growth-defensive-style-allocation-2026-09-02.md`.
- Query `retrieval augmented diffusion news embedding portfolio weights` returned **0** pages, so no closer Wiki page exists to link and none was fabricated.

Four-axis distinction against the nearest repository neighbours (source identity differs in every pair):

1. `retrieval-augmented-llm-expert-switching-portfolio-management-2026-09-03.md` (source arXiv:2608.28252, retrieval-augmented **LLM-guided expert switching** among trading experts) - mechanism differs (expert selection by LLM reasoning vs diffusion-denoised market representation feeding an SDF weight map) and source identity differs.
2. `cross-predictive-sdf-cross-asset-spillover-max-sharpe-2026-09-23.md` (source arXiv:2602.20856, econometric **cross-asset spillover SDF** with max-Sharpe construction) - shares the SDF framing only; signal construction (closed-form/econometric spillover SDF vs learned multimodal representation), method class and source differ.
3. `co-pricing-bma-sdf-tradable-portfolio-joint-bond-stock-factor-zoo-2026-09-26.md` (source arXiv:2604.04430, **Bayesian model averaging over a 54-factor zoo** for bond/stock co-pricing) - different asset classes, different mechanism (factor-zoo model averaging vs representation denoising), different source.
4. `pure-news-residual-embedding-cross-sectional-long-short-anomaly-2026-09-26.md` (source NBER w35093, **residual LLM-embedding news anomaly**, monthly cross-section) - different signal construction (statistically extracted residual news factor vs end-to-end weight learning), different horizon (monthly vs 7-day), different source.

## Sources

- Kelvin J.L. Koa, Xinyang Li, Ke-Wei Huang, *"Retrieval-Augmented Diffusion Modeling for Stochastic Discount Factor Portfolios"*, arXiv:2609.35086v1 [cs.LG], submitted 28 Sep 2026 13:03:58 UTC. `https://arxiv.org/abs/2609.35086`
- Pinned full text (read end to end for this record): `https://arxiv.org/html/2609.35086v1` - 348,275 bytes, SHA-256 `3a79399ec97e604aeb84cf1ddf69ed90ae1033a63bc263db204b1e70575bbf60`, retrieved 2026-09-29.
- Canonical DOI: `https://doi.org/10.48550/arXiv.2609.35086` (printed as DataCite pending registration).
- Code URL printed in the abstract, checked 2026-09-29: `https://github.com/xinyangli5579-star/RADAR` - HTTP 404, not retrievable.
- Supporting dataset reference named by the source (not fetched): FNSPID, Dong et al., 2024 (reference [10] of the pinned text).
