---
schema: strategy-research-record-v1
title: "Fear Moves Markets: Sentiment-Augmented POMP Latent-Volatility Filter for Bitcoin (Delta Fear-and-Greed Regressor + Student-t Measurement)"
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - volatility
  - sentiment
  - fear-and-greed-index
  - state-space-model
  - pomp
  - latent-volatility
  - filter-diagnostics
  - risk-modeling
status: research-only
confidence: medium
source_as_of: "2026-09-22"
sources:
  - "Abeyankar Giridharan, Chang Li, Suvrorup Mukherjee, Xinhe Wu, 'Fear Moves Markets: Sentiment-Augmented POMP for Volatility Modeling of Bitcoin Returns', arXiv:2609.23250 [stat.AP]. Landing page https://arxiv.org/abs/2609.23250 read 2026-09-25: submitted 19 Sep 2026 23:21:57 UTC (v1, 2,284 KB), last revised 22 Sep 2026 23:27:26 UTC (v2, current, 2,284 KB); no Comments field, no journal-ref, no publisher DOI, no peer-review statement; license link resolves to creativecommons.org/licenses/by/4.0/ (CC BY 4.0)."
  - "Pinned primary source read end to end 2026-09-25: https://arxiv.org/html/2609.23250v2 — fetched 127,791 bytes, stripped to 29,039 characters (body 27,690 characters before the arXiv HTML chrome), covering Sections I-VI, Table I-Table II, Figure 1-4 captions, References [1]-[8] and the per-author affiliation block."
  - "Pinned primary PDF cross-check: https://arxiv.org/pdf/2609.23250v2 — 2,513,803 bytes, SHA-256 47e595c8a966a958595ecf0d94521653e1203fdc07391bc4139a5d55d1e86e6b, retrieved 2026-09-25 (page count not asserted: no PDF page/text utility was available in this run environment, so the body was read through the pinned HTML cross-check above)."
  - "Version-contrast source (not used for any number in this record): https://arxiv.org/pdf/2609.23250v1 — 2,513,876 bytes, SHA-256 a7152003c7192e970b37bd8b279d751404f5e82b1fd8ca6944ca88f78da26ed6."
  - "arXiv API metadata https://export.arxiv.org/api/query?id_list=2609.23250 and DataCite DOI https://doi.org/10.48550/arXiv.2609.23250 — DOI checked 2026-09-25 with HTTP 302 to https://arxiv.org/abs/2609.23250."
  - "Code release cited by the source itself as 'Code and reproducibility resources' in the LaTeXML thanks note under the v2 title: https://github.com/abeyankargiridharan/Novel_Approach_to_Volatility_Analysis_on_Bitcoin_Returns — default branch main, HEAD commit 4905198c12a6fdcf48689a313fef398130015179 dated 2025-06-14T06:57:54Z ('Merge pull request #1 ... restructuring and presentation'). Files read at that commit: README.md, breto/final.R (327 lines), bitcoin-preprocessing-HSV.Rmd, fng-analysis.Rmd, bitcoin-garch-analysis.R, requirements.txt (R 4.4.1, pomp 6.1, knitr 1.50, lubridate 1.9.4, doParallel 1.0.17, doRNG 1.8.6.1, ggplot2 3.5.1), runf.sbat, breto/final-r-3.sbat, datasets/bitcoin_2020-01-01_2025-04-06.csv, datasets/bitcoin_2024-04-06_2025-04-06.csv, datasets/bitcoin_fg.csv, volatility-project.html (4,903,307 bytes)."
  - "Sentiment-input endpoint actually used by the released code (paper never names it): https://api.alternative.me/fng/ called with limit=1000 (bitcoin-preprocessing-HSV.Rmd) and limit=2000 (fng-analysis.Rmd); the same notebook titles its plot 'CNN Fear & Greed Index Over Time' (naming disagreement recorded under contradictions)."
  - "Method provenance cited by the source but NOT read as primary evidence in this record: C. Breto, 'On idiosyncratic stochasticity of financial leverage effects', Statistics & Probability Letters 91 (2014) 20-26 (ref [2]); E. L. Ionides, D. Nguyen, Y. Atchade, A. A. King, 'Inference for dynamic and latent variable models via iterated, perturbed bayes maps', PNAS 112 (2015) 719-724 (ref [8]); King, Nguyen & Ionides, JSS 69(12) (2016) for the R package pomp (cited in the code README)."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Method label disagreement inside the source: the abstract says the model is fit 'via simulation-based inference', while Section V says 'Parameter estimation is performed via the iterated filtering (IF) algorithm [8], which applies stochastic optimization to latent-variable models by combining parameter perturbation with particle filtering' — IF is a likelihood/optimization procedure, not likelihood-free simulation-based inference, and no likelihood-free (ABC / neural posterior) method appears anywhere in the paper or the released code."
  - "Internal numeric disagreement: Section V-1 prose says 'Mode 1 peaks at around 4100, about 100 log-likelihood units above Mode 2 at roughly 4000', while Table II prints the maximum log-likelihood of the enhanced Breto model as 4093.85; the prose mode location and the tabulated maximum are not reconciled."
  - "The paper never names the FGI provider or the Bitcoin price source, while its own released code fetches api.alternative.me and simultaneously labels the same series 'CNN Fear & Greed Index' (fng-analysis.Rmd, bitcoin-preprocessing-HSV.Rmd), so the source's artifacts disagree about what the sentiment input is and where it came from."
  - "Two different Bitcoin close series exist in the released datasets for identical dates with no vendor identified: 2020-01-01 = 7200.17 (bitcoin_2020-01-01_2025-04-06.csv, column 'Close') versus 7213.918462217 (bitcoin_fg.csv, column 'close'); 2025-04-05 = 83504.8 versus 83582.03; 2025-04-06 = 78214.48 versus 78310.34. The paper does not state which series its returns were built from."
  - "Paper-versus-code disagreement on what is implemented: the paper presents the enhanced Breto model (gamma * Delta FGI in the state equation, Student-t measurement) as fitted and as the source of Table II, but the pinned HEAD of the released repository implements only the original Breto model (parameter names sigma_nu, mu_h, phi, sigma_eta, G_0, H_0; dmeasure = dnorm; no gamma term anywhere in breto/final.R) and the released volatility-project.html (4.9 MB) contains zero occurrences of 'gamma', 'Student', 'sentiment' and zero occurrences of every Table II value (4093 / 4074 / 3959 / 3902)."
---

# Fear Moves Markets: Sentiment-Augmented POMP Latent-Volatility Filter for Bitcoin (Delta Fear-and-Greed Regressor + Student-t Measurement)

## Provenance

- **Primary source:** Abeyankar Giridharan, Chang Li, Suvrorup Mukherjee, Xinhe Wu — four authors, all University of Michigan (Dept. of Statistics: Giridharan `abeygiri@umich.edu`, Mukherjee `suvrom@umich.edu`, Wu `xinhwu@umich.edu`; Dept. of IOE: Li `liichang@umich.edu`), arXiv preprint `arXiv:2609.23250v2 [stat.AP]`, submitted 19 Sep 2026, last revised 22 Sep 2026. Preprint only: no Comments field, no journal reference, no publisher DOI beyond the arXiv DataCite DOI `10.48550/arXiv.2609.23250`, no peer-review statement; license CC BY 4.0.
- **Pinned checksums:** v2 PDF `2,513,803` bytes, SHA-256 `47e595c8a966a958595ecf0d94521653e1203fdc07391bc4139a5d55d1e86e6b`; v2 HTML `127,791` bytes fetched and stripped to `29,039` characters (body `27,690` characters), read end to end on 2026-09-25; v1 PDF `2,513,876` bytes, SHA-256 `a7152003c7192e970b37bd8b279d751404f5e82b1fd8ca6944ca88f78da26ed6` (used only for version contrast). Every number below comes from the pinned v2 body (Section V, Table II, Figure 1-4 captions) unless labelled otherwise.
- **Structure read:** Sections I-VI, Table I (model feature matrix), Table II (model performance), Figure 1 (data/preprocessing), Figure 2 (filter diagnostics, last iteration), Figure 3 (convergence of 100 iterated-filtering trajectories), Figure 4 (simulated vs observed path, days 200-300), References [1]-[8].
- **Universe / asset class:** single asset, **Bitcoin daily closing prices**, crypto, plus a daily sentiment series (Fear & Greed Index, FGI). Sample as stated by the source: **January 2020 - April 2025** (abstract, Section III, Figure 1 caption). The observation count `N` is **not stated anywhere in the paper** (`data gap`); our count of the released datasets is 1,923 data rows in `bitcoin_2020-01-01_2025-04-06.csv` and 1,922 data rows in `bitcoin_fg.csv`, both spanning 2020-01-01 to 2025-04-06 (`our count`, not source-reported).
- **Data provenance:** the paper names neither the Bitcoin price source nor the FGI provider (`data gap`); both are recoverable only from the released code (see Sources). The code pulls FGI from `https://api.alternative.me/fng/` at analysis time with `limit=1000`/`limit=2000`, i.e. an unpinned live snapshot rather than a versioned vintage (`data gap` on revisions/point-in-time availability).
- **Implementation artifact:** the source links a GitHub repository from the title thanks-note ("Code and reproducibility resources"). Pinned HEAD `4905198c12a6fdcf48689a313fef398130015179` (2025-06-14) contains R/pomp scripts for the **original** Breto model, a GARCH grid-search script, FGI/preprocessing notebooks and three CSVs — but **no implementation of the enhanced (sentiment + Student-t) model and none of the paper's reported numbers** (verified by file-level reads and a 0-hit scan of `volatility-project.html`). Reproducing Table II therefore requires rebuilding the enhanced model from the equations alone.
- **Repository deduplication audit (run 2026-09-25 before writing):** ripgrep across **all** `*.md` in the checkout including `--hidden --no-ignore` (`.mimo-worktrees`, `.agents`, `.hermes`; 2,540 files at run time) plus `coverage_manifest.csv` (5,808 rows) for `2609.23250`, `10.48550/arXiv.2609.23250`, `Fear Moves Markets`, `Giridharan`, `Suvrorup`, `Xinhe Wu`, `Sentiment-Augmented POMP`, `Novel_Approach_to_Volatility`, `Breto`, `Bretó`, `partially observed Markov`, `api.alternative.me` → **0 hits in every `.md` and 0 hits in the manifest**. Near-strings were opened and cleared as different sources with different mechanisms: `Fear and Greed` matched 36 times across 7 files (`crypto-macro-sentiment-contrarian-fear-greed-ema-2026-09-03.md` — arXiv:2512.02029 contrarian EMA timing; `regret-driven-portfolio-ftl-llm-hedging-sentiment-gated-2026-09-05.md` — arXiv:2601.17021 F&G-gated allocation; `crypto-cross-sectional-sentiment-risk-beta-premium-2026-09-01.md` — J. Behavioral & Experimental Finance 46 (2025) cross-sectional sentiment beta; `crypto-bitcoin-cvar-risk-aware-q-learning-adaptive-controller-2026-09-02.md` — arXiv:2608.04305 F&G as a state input to CVaR Q-learning; `crypto-security-shock-cross-sectional-factor-hacks-mktcap-2026-09-01.md` — arXiv:2601.07664; `market-regime-routed-specialist-gbt-asymmetric-hysteresis-2026-09-12.md` — github/davidxu277/alpha-timing; `crypto-brown-esg-uncertainty-next-day-downside-liquidity-amplified-2026-09-03.md` — FRL DOI 10.1016/j.frl.2026.109770); `alternative.me` matched 102 times across those and adjacent crypto records; `Sentiment-Augmented` matched 5 files, all sentiment-reward DRL / FinBERT-portfolio records from unrelated sources.
- **Four-axis distinction against the closest existing records:** (1) *source identity* — `arXiv:2609.23250` appears nowhere in the repository, while the neighbours rest on arXiv:2512.02029, arXiv:2601.17021, arXiv:2608.04305, arXiv:2601.07664, DOI 10.1016/j.jbef.2025.101043, DOI 10.1016/j.frl.2026.109770 and `github/davidxu277/alpha-timing`; (2) *mechanism* — sentiment enters as an **exogenous regressor inside a latent log-volatility state equation of a partially observed Markov process**, whereas the neighbours use FGI as a contrarian timing signal, an allocation gate, a cross-sectional control/factor, or an RL state input; (3) *signal construction* — `H_n = mu_h(1-phi) + phi H_{n-1} + beta_{n-1} R_n exp(-H_{n-1}/2) + gamma * Delta FGI_scaled,n-1 + omega_n` with Student-t(`nu=5`) measurement noise and an iterated-filtering fit, none of which appears in any existing record; (4) *material data dependency* — the joint requirement of daily BTC log returns **and** a point-in-time sentiment history aligned to the state equation at `n-1`, fitted by particle filtering. Universe (single-asset BTC daily), mechanism, signal construction and data dependency therefore all differ; this is not a reframing of an existing capture.

## Economic mechanism

### Source-reported

The source's chain of reasoning, in its own terms:

1. **Premise:** "Cryptocurrency markets exhibit extreme price swings and sentiment-driven regime shifts, which traditional volatility models often fail to capture" (abstract). GARCH, Heston-type stochastic volatility and HMMs are described as adequate for equities/fixed income but weak on crypto's tails and regime breaks (Section I).
2. **Base model (Breto POMP, Section IV-A):** latent log-volatility `H_n` follows an AR(1) with a random-walk leverage channel driven by a second latent state `G_n`:

   - `H_n = mu_h(1-phi) + phi H_{n-1} + beta_{n-1} R_n exp(-H_{n-1}/2) + omega_n` (Eq. 3)
   - `beta_n = Y_n sigma_eta sqrt(1-phi^2)`, `R_n = tanh(G_n) in (-1,1)`, `omega_n ~ N(0, sigma_eta^2 (1-phi^2) (1-R_n^2))`
   - `G_n = G_{n-1} + nu_n`, `nu_n ~ N(0, sigma_nu^2)` (Eq. 4)
   - observation `Y_n = exp(H_n/2) eps_n`, `eps_n ~ N(0,1)` (Eq. 2)

   A negative return together with a negative `R_n` raises `H_n`, so bad news raises conditional variance while good news has a muted, `tanh`-compressed effect — the model's leverage asymmetry (Section IV-A).
3. **Enhancement 1 — sentiment regressor (Eq. 5):** add `gamma * Delta FGI_scaled,n-1` to the `H_n` equation. FGI is centered on its range midpoint 50 and first-differenced to make it stationary (Section III-2) so that the state equation stays stable and identifiable; `gamma` is interpreted as the directional effect of sentiment changes on volatility, with the source arguing that both falling FGI (fear) and rising FGI (greed) amplify volatility, and Section V-3 reporting `gamma` in `(-1, 0)` — i.e. **fear shifts move volatility more than greed shifts**.
4. **Enhancement 2 — heavy tails:** replace Gaussian measurement noise with Student's t, and "after empirical testing, we find that a t-distribution with `nu = 5` degrees of freedom offers the best fit" (Section IV-B).
5. **Estimation and evaluation (Section V):** iterated filtering (IF, ref [8]) with `N_p = 2000` particles; a local search from an informed start, then multiple global IF searches from randomly sampled initial values inside a "plausible parameter box", keeping the parameter set with maximum estimated likelihood; Figure 3 overlays **100 independent IF trajectories**; diagnostics are effective sample size (ESS) and the conditional one-step log-likelihood `log p(Y_n | Y_{1:n-1}, theta_hat)`.
6. **Claimed result:** the enhanced model has the highest maximum log-likelihood and the most stable filter (Table II, Figure 2), with interpretable parameters (`gamma in (-1,0)`, `mu_h` near -7.5 to -8 in the enhanced model versus no convergence in the original), and a simulated path that visually tracks the observed path over days 200-300 (Figure 4).

### Research interpretation

The falsifiable hypotheses this record normalizes (every operationalization below is **`research-proposed`**, none is printed by the source):

- **H1 — sentiment has incremental content for BTC latent volatility (`research-proposed`).** Conditioning the latent log-volatility dynamics on the change in a public sentiment index improves *out-of-sample* one-step volatility density forecasts and filter stability relative to a price-only stochastic-volatility model with leverage. Roles: *state variable* = filtered `H_t` (or `exp(H_t)`); *exogenous driver* = `Delta FGI` at `t-1`; *evidence available today* = in-sample maximum likelihood only (Table II). F1/F2/F4 below are the tests that would support or kill it.
- **H2 — fear-dominant asymmetry (`research-proposed`).** The sign and magnitude of `gamma` are stable out of sample and across sub-periods, so that sentiment *deterioration* carries more volatility information than sentiment improvement. Source-reported support is the single point estimate range `(-1,0)` from Figure 3 with no confidence interval.
- **H3 — from fit to money is a separate, untested link.** A better-filtered volatility state can only become alpha through a downstream use (volatility targeting, risk gating, variance-risk-premium timing, position sizing, options/perpetual hedging). The source contains **no** such layer, so H1 improving does not imply H3 improves; components must be ablated independently (F3, F9). This record must not be read as evidence that a sentiment-conditioned vol filter is tradable.

## Signal

**Source-reported (a filtered state, not a trading rule):**

- **Formation timestamp / tradability:** daily, at the close of day `n`: returns `Y_n` and the lagged regressor `Delta FGI_scaled,n-1` enter the state equation, so the filtered `H_n` is available once day `n` and the sentiment value for `n-1` are observed. Timezone, trading-day boundary (UTC vs exchange close) and the availability lag of FGI are **not stated** (`underspecified`).
- **Input series construction:** `A_{n+1} = log Z_{n+1} - log Z_n`, then `Y_n = A_n - Abar` where `Abar` is the **full-sample** mean (Eq. 1) — a centering that uses future data (`data gap` / look-ahead, see Negative evidence 5). FGI is centered at 50 then first-differenced; the additional "scaling" referenced by `FGI_scaled` in Eq. 5 is never defined numerically (`underspecified`).
- **Model parameters:** seven free parameters `sigma_eta, sigma_nu, gamma, mu_h, G_0, H_0, phi` (Section V, Figure 3); `nu = 5` is fixed after "empirical testing" (search space and selection rule not disclosed); particle count `N_p = 2000`.
- **Output used as signal:** the filtered latent log-volatility `H_t` (equivalently conditional standard deviation `exp(H_t/2)`) and the fitted `gamma`/`mu_h`.
- **Entry, exit, holding period, re-entry, position sizing, thresholds, rebalance cadence:** **not specified by the source — `underspecified`.** The paper states no trading rule of any kind; nothing about entry thresholds, stops, holding, sizing or execution exists to be quoted.
- **Scout operationalization, all `research-proposed` (explicitly not source-reported):** *signal timestamp* = end of UTC day `t`, tradable at the next session's open/close (one-day delay); *risk gate* — reduce a BTC/perpetual exposure when `exp(H_t/2)` exceeds a trailing 30-day median by a `research-defined` factor 1.5, restore below 1.2; *volatility targeting* — scale exposure to hit a `research-defined` 40% annualized target volatility using the filtered state, with a `research-defined` 20% cap on gross exposure; *VRP timing (higher bar)* — short realized-vol exposure only when a filtered-vol estimate is high relative to a quoted/implied benchmark, which requires an options venue the source never names; *re-entry* — after 5 trading days below the gate. All thresholds (1.5 / 1.2 / 40% / 20% / 5 days) are scout-chosen `research-defined` values selected only to make H1/H3 falsifiable; the source supports none of them.

## Required data

- **Instrument / universe:** Bitcoin daily closing prices, single asset. Source sample: 2020-01 to 2025-04. Extension universe (`research-proposed`): BTC-USD across at least two additional venues, plus ETH for cross-asset transport.
- **Venue / market type:** source does not state venue or whether the close is spot, futures or an index (`data gap`); the released CSVs are a bare `Start,Close` pair with no vendor field. Market type for any trading use would be spot or perpetual (`research-proposed`), which adds funding, mark/index price and liquidation requirements the source never models.
- **Timeframe:** daily bars; 24/7 crypto sessions make the "daily" boundary a convention that the source leaves unstated (`underspecified`) — candle boundaries, timezone and out-of-order records are undefined.
- **Fields:** close price and derived demeaned log return; FGI daily level (0-100) and its first difference at `n-1`. For the falsification tests additionally: intraday prices for realized volatility, an implied/vol-benchmark series (e.g. an exchange-published BTC implied-vol index — `research-proposed`), perpetual funding rates and mark/index basis if the downstream use is a perpetual (`research-proposed`).
- **Point-in-time:** FGI must be stored as a dated vintage because the API is queried live at analysis time (`limit=1000`/`2000`), and the paper declares no vintage, no availability lag and no revision policy (`data gap`). The full-sample mean `Abar` used in Eq. 1 is itself a look-ahead input that must be replaced by a recursive/expanding mean in any point-in-time replication.
- **Missing data:** not addressed by the source (`data gap`): no statement on missing days, halts, stale FGI values, or mismatched calendars between price and sentiment series; imputation is not permitted by this record.
- **Funding / fee / spread needs:** entirely unmodeled in the source (`data gap`): no maker/taker fees, no funding, no borrow, no spread, no slippage, no market impact, no capacity.

## Execution assumptions

**Source-reported:**

- There is **no order, no fill, no portfolio and no execution layer** in the source — it is a model-fit study. Nothing in it can be executed as written.
- Word-boundary scan of the pinned v2 body (29,039-character HTML text; counts exclude the arXiv HTML chrome where noted): `transaction` 0, `transaction cost` 0, `cost` 0, `slippage` 0, `bid-ask` 0, `commission` 0, `fee`/`fees` 0, `turnover` 0, `Sharpe` 0, `backtest` 0, `VaR`/`value-at-risk` 0, `RMSE` 0, `QLIKE` 0, `MSE` 0, `BIC` 0, `bootstrap` 0, `seed` 0, `p-value` 0, `t-stat` 0, `significan*` 2 (both rhetorical: abstract "significantly outperforms" and conclusion "significantly stronger effect"), `confidence interval` 0, `error bar` 0, `walk-forward` 0, `rolling` 0, `train` 0, `split` 0, `holdout` 0, `penalty` 0, `exchange` 1 (the Kuala Lumpur Stock Exchange inside a related-work sentence), `Binance` 0, `Coinbase` 0, `vendor` 0, `point-in-time` 0, `forecast*` 3 (all inside related-work/reference sentences), `AIC` 1 (generic GARCH specification remark), `capacity` 1 (abstract phrase "improved capacity to capture"), `leverage` 15 (all the model's *leverage effect*, never margin leverage), `portfolio` 1 (motivation sentence), `funding` 1 and `GitHub` 3 (arXiv page chrome only: "Report GitHub Issue" / "Submit with GitHub" / "Submit in GitHub"), plus the source's own single `github.com` code link in the title thanks-note. Absent items are `data gap`, never "zero cost".
- The only quantitative comparisons in the source are in-sample maximum likelihood and filter/parameter diagnostics (Table II, Figures 2-4).

**Scout additions, all `research-proposed`:** one-day signal-to-order delay; daily close-to-close execution; if the downstream use is a perpetual, an explicit funding charge every 8 hours plus mark-price basis and liquidation risk; if the downstream use is options, spread and borrow on the short-vol leg; a cost ladder of 0/5/10/20 bps per side for any turnover-bearing test; no capacity claim of any kind.

## Evidence

### Source-reported

All figures below are third-party, source-reported from the pinned `arXiv:2609.23250v2` body, asset class **crypto (Bitcoin daily)**, sample **January 2020 - April 2025**, **in-sample maximum-likelihood fit with no cost model and no out-of-sample evaluation**, single asset, single specification. Not independently reproduced.

- **Table II ("Model Performance", Section V-1), maximum log-likelihood:** Enhanced Breto **4093.85**; Original Breto **4074.67**; HSV model **3959.11**; GARCH(3,1) **3902.41**. Our count on the printed cells: the enhanced model leads the original Breto by **19.18** likelihood units, HSV by **134.74** and GARCH(3,1) by **191.44** (`our count`, arithmetic on source-reported Table II values only).
- **Section V-1 likelihood geometry:** bimodal IF trajectories — "Mode 1 peaks at around 4100, about 100 log-likelihood units above Mode 2 at roughly 4000"; the original Breto shows a similar bifurcation while HSV is unimodal (plots for the latter two "omitted for brevity").
- **Filter stability (Figure 2):** with `N_p = 2000`, the enhanced model keeps ESS "close to the theoretical maximum (2000) across most time points", with "occasional drops below 50"; both state-space benchmarks show "consistently lower ESS"; **GARCH(3,1) ESS cannot be assessed "since IF is not applicable to GARCH"** (source's own statement).
- **Conditional one-step log-likelihood:** the enhanced model's lower panel of Figure 2 is reported as higher than the benchmarks over time (figure-only, no table of values — `data gap` on the series).
- **Parameter results (Figure 3, 100 IF trajectories):** `gamma` converges to `(-1, 0)`; `mu_h` converges to approximately `(-7.5, -8)` in the enhanced model while showing "no convergence pattern" in the original; `sigma_eta`/`phi` are bimodal with Mode 1 at `phi` near 1 (so `sqrt(1-phi^2) ~ 0`) and "Box 2" spanning `phi` roughly 0 to 0.6.
- **Simulation check (Figure 4):** a path simulated at the maximum-likelihood parameters over a randomly chosen window days 200-300 "exhibits close correspondence with the ground truth" (visual comparison only).
- **Table I feature matrix:** GARCH = no state-space/no SV/no leverage/no sentiment; HSV = state-space + SV, no leverage, no sentiment; Original Breto = state-space + SV + leverage, no sentiment; Enhanced Breto = all four.
- **Data/scale claims:** "daily Bitcoin returns and FGI data from January 2020 to April 2025"; GARCH(3,1) "selected through grid search"; `nu = 5` chosen "after empirical testing"; estimation via IF with `N_p = 2000`, local search plus global searches from random starts inside a plausible box, best-likelihood parameter set retained.
- **Publication status:** preprint only, `stat.AP` sole category, CC BY 4.0, no peer review, no journal, DataCite DOI only.

### Independently reproduced

Not independently reproduced. No re-estimation of the POMP models, no recomputation of Table II, no verification of the Figure 2-4 diagnostics, and no backtest of any downstream rule has been performed in our research stack. The released code does not even contain the enhanced model (Provenance), so reproduction would start from the equations.

### Negative evidence

1. **Everything is in-sample.** The evaluation compares *maximum* log-likelihoods on the same sample used for estimation: no train/test split, no walk-forward, no hold-out, no rolling window (word scan: `split` 0, `train` 0, `walk-forward` 0, `rolling` 0, `holdout` 0). In-sample likelihood comparisons with different parameter counts and different observation distributions are not evidence of predictive content.
2. **No statistical inference anywhere.** Zero `p-value`, `t-stat`, `confidence interval`, `error bar`, `bootstrap` or `seed` occurrences; no likelihood-ratio test, no AIC/BIC penalty (the single `AIC` occurrence is a generic GARCH remark), no standard errors on `gamma`. The abstract's "significantly outperforms" and the conclusion's "significantly stronger effect" are therefore unsupported by any test in the paper.
3. **Non-identifiability is admitted by the source.** The likelihood surface is bimodal with modes ~100 units apart, `sigma_eta` and `phi` trade off against each other, `phi`'s second mode spans 0-0.6, and `mu_h` only converges *because* the sentiment regressor was added ("one plausible explanation... removes a key confound"). Parameter-level claims (`gamma`, `mu_h`) therefore rest on one selected mode of a multi-modal fit.
4. **Hidden in-sample tuning.** `nu = 5` was chosen "after empirical testing" with no search space, no selection metric and no sample split; the plausible parameter box and informed starting point for IF are likewise chosen in-sample. `underspecified`.
5. **Look-ahead in the observation series.** Returns are demeaned by the **full-sample** mean (Eq. 1; code: `bitcoin_ret - mean(bitcoin_ret)`), so every `Y_n` contains information from the end of the sample. Any replication must replace this with a recursive centering; the size of the resulting change in `gamma` and in the Table II gaps is unknown.
6. **No forecasting or risk metric.** The paper never computes RMSE/QLIKE/MSE on held-out data, never runs a VaR/exception backtest, never reports drawdown, turnover, Sharpe or any economic use — despite the abstract's framing about regime shifts. `forecast*` appears 3 times, all in related work/reference titles.
7. **Benchmark mismatch.** GARCH(3,1) is fitted by grid search (code: `tseries::garch` over (p,q) ordered by AIC) while the state-space models are fitted by IF; ESS diagnostics are explicitly not comparable ("IF is not applicable to GARCH"); raw likelihoods are compared across Gaussian and Student-t observation models without a parameter-count or density-class adjustment. The benchmark set also contains no HAR/GJR/EGARCH-t, no realized-volatility model and no sentiment-free Student-t control.
8. **The ablation that would isolate the contribution does not exist.** The paper reports one combined enhancement (sentiment **plus** Student-t) versus a Gaussian original, so the likelihood gain of 19.18 units cannot be attributed to sentiment rather than to the fat-tailed measurement distribution.
9. **Reproducibility gap between paper and code.** Pinned HEAD implements only the original Breto model (Gaussian `dmeasure`, no `gamma`); `volatility-project.html` (4.9 MB) contains no `gamma`, no `Student`, no `sentiment` and none of the Table II values; the code snapshots date from April-June 2025 while the paper is dated September 2026. The enhanced model as reported cannot be re-run from the release, and no environment, seed or run manifest for the reported fit is provided.
10. **Data provenance is unrecoverable from the paper.** No Bitcoin price vendor, no exchange, no FGI provider, no timezone, no calendar rule; the code simultaneously labels the FGI series "CNN Fear & Greed Index" while calling `api.alternative.me`, and the two released close series disagree by 13.7 USD on 2020-01-01 and by 77 USD on 2025-04-05 (`our count` on released files). A point-in-time replication cannot know which price path the reported fit used.
11. **Sentiment input is not pinned.** FGI is pulled live with `limit=1000`/`2000` at analysis time; no vintage, no publication timestamp, no availability lag and no revision policy is documented, and the paper does not state whether `Delta FGI` at `n-1` was contemporaneously available on day `n-1` (`data gap` on look-ahead in the covariate).
12. **Scaling of the regressor is undefined.** Equation 5 writes `FGI_scaled` and the text says the series is differenced *and scaled*, but no scale factor, standardization window or units are given — `gamma in (-1,0)` is therefore not interpretable in economic units and not directly reproducible.
13. **Single asset, single window, no sub-period robustness.** One asset (BTC), one 5-year window, no regime breakdown, no second cryptocurrency, no cross-market check, no multiplicity control across the two reported model comparisons and the parameter interpretations.
14. **Terminology inconsistency.** The abstract's "simulation-based inference" does not match Section V's iterated-filtering description (see frontmatter `contradictions`); readers expecting likelihood-free inference will not find it in the paper or the code.
15. **Cross-record adjacency, not corroboration.** In this repository the seven FGI-using records use FGI as a tradable or gating signal (contrarian EMA timing, FTL gating, cross-sectional risk beta, RL state input) or as a control variable; none of them tests sentiment-augmented latent-volatility filtering, so none supports or refutes H1. The nearest methodological caution in-repo — `crypto-macro-sentiment-contrarian-fear-greed-ema-2026-09-03.md` — records that its own signal was not significant for some baskets and that its analysis was "an impulse-response analysis, not a strategy backtest; transaction costs, slippage, and implementation frictions are not incorporated". Beyond the reviewed sources, no contrary study specific to this model was found; **absence is not evidence of no negative result**.

## Falsification plan

Every threshold below is a `research-defined` acceptance/failure cutoff and every rule is `research-proposed`; none is printed by the source. Failure action in every case: mark the hypothesis rejected-for-now and record the failed cell as negative evidence (no unconstrained retuning).

- **F1 — Point-in-time out-of-sample density forecast (`research-defined`).** Rebuild the enhanced model with recursive (expanding) demeaning and vintage-pinned FGI; evaluate one-step-ahead density forecasts on a held-out last 20% of the sample plus at least one rolling-origin fold, against a price-only Breto control and an AR-GJR-t(5) control. **Fail** H1 if the enhanced model's mean log score is not strictly higher than the price-only control, or if the QLIKE improvement over the best control is <= 0 at both the 1-day and 5-day horizon.
- **F2 — Isolating the sentiment channel (`research-defined`).** 2x2 ablation: {with, without `Delta FGI`} x {Gaussian, Student-t(5)} on identical samples and identical IF budgets. **Fail** H1 if the sentiment arm adds less than 2.0 log-likelihood units per 100 observations out of sample, or if the Student-t arm alone accounts for >= 90% of the total gain over the original model.
- **F3 — Sign stability of `gamma` (`research-defined`).** Rolling 18-month estimation windows (step 3 months) with particle-filter standard errors or a moving-block bootstrap over days. **Fail** H2 if `gamma >= 0` in more than 20% of windows, or if the 95% interval of the full-sample `gamma` includes 0, or if the sign flips between the 2020-2022 and 2023-2025 halves.
- **F4 — Benchmark horse race (`research-defined`).** Add HAR-RV, EGARCH-t and a GJR-GJR-t(5) benchmark, all fit on the identical training window and scored on the identical test window with the same density metric. **Fail** H1 if the enhanced POMP is not the top-ranked model in at least 2 of 3 evaluation regimes (calm / high-vol / trend).
- **F5 — Identifiability audit (`research-defined`).** Profile likelihood for `(sigma_eta, phi)` and `mu_h` across >= 20 random IF starts with fixed seeds and reported seed list. **Fail** if the retained mode is not recovered in >= 80% of starts, or if the across-start coefficient of variation of `mu_h` exceeds 20%, or if the two modes remain within 20 likelihood units of each other (i.e. the reported "winner" is arbitrary).
- **F6 — Look-ahead repair (`research-defined`).** Re-run with recursive demeaning and with no demeaning (zero-mean state). **Fail** if the Table II gap between the enhanced and original model shrinks by more than 50% relative to the reported 19.18 units, or if `gamma` changes sign.
- **F7 — Sentiment vintage audit (`research-defined`).** Reconstruct `Delta FGI` from dated API snapshots taken at (or before) each `n-1`. **Fail** if vintage drift changes the sign of `gamma`, or if the out-of-sample log-score advantage in F1 changes sign between vintages — that would show the effect depends on data that were not available at the time.
- **F8 — Circular-shift placebo (`research-defined`).** 1,000 random circular shifts of the `Delta FGI` series (shifts >= 30 days) through the same pipeline. **Fail** H1 if the observed log-likelihood gain lies inside the placebo 95% band.
- **F9 — Downstream economic test (`research-proposed`).** Drive a `research-proposed` volatility-targeted BTC exposure (40% target, 20% gross cap, one-day delay) with the filtered state, and charge 0/5/10/20 bps per side (plus 8-hour funding if a perpetual is used). **Fail** H3 if net Sharpe at 10 bps does not exceed the price-only-model version by >= 0.20, or if net Sharpe <= 0 at 10 bps, or if the gated version fails to reduce max drawdown by >= 20% versus an ungated book.
- **F10 — Risk-utility check (`research-defined`).** 1% and 2.5% VaR/ES exception tests on filtered-variance forecasts: Kupiec test p >= 0.05 required at both levels. **Fail** H1's risk reading if either level rejects.
- **F11 — Sub-period concentration (`research-defined`).** Decompose the likelihood/log-score gain by calendar year (2020 COVID shock, 2021 bull, 2022 drawdown, 2023 consolidation, 2024-2025). **Fail** if more than 70% of the total gain comes from a single year or a single regime — the effect would be a crisis-fitting artefact rather than a stable channel.
- **F12 — Multiplicity and forward freeze (`research-defined`).** Report Benjamini-Hochberg q-values across every printed comparison (F1-F11) with q < 0.10 required for any "supported" label, and freeze the full specification (window, `nu`, regressor, thresholds in F9) before 2026-10-01, evaluating only later data for >= 6 months. **Fail** if no cell survives BH or if the frozen forward window shows a non-positive gain.

## Crypto portability

**direct.** The source is already crypto-native: Bitcoin daily returns, a crypto-specific sentiment index, 24/7 sessions and a crypto drawdown/bull-run sample. Nothing has to be ported from traditional assets for H1/H2.

Crypto-specific risks that still must be handled explicitly:

- **Clock and session conventions:** daily bars on a 24/7 market need a declared boundary (UTC 00:00 vs venue close), and the source states none (`underspecified`). Timestamp precision, out-of-order data and the alignment of `Delta FGI` at `n-1` with the return at `n` are undefined.
- **Venue fragmentation:** the close-price series is not identified and the released files disagree; a replication must pin a venue (or a composite) and document the choice, and cross-venue closes change demeaned returns.
- **Sentiment data availability:** FGI is a crypto aggregate with its own publication process; pinning vintages is required (F7), and extending it to other assets or to intraday horizons is unproven.
- **Perpetual/options layer (if H3 is pursued):** funding charged every 8 hours, mark/index basis, liquidation thresholds, borrow on any short-vol leg, and exchange-specific fee tiers all become required fields that the source never models; none may be silently treated as zero.
- **Liquidity/impact:** daily BTC is liquid, but any gated strategy's turnover, capacity and participation are `data gap`.
- **Point-in-time and survivorship:** single-asset, single-window selection with no alternative universe; transport to a broader crypto basket is `unproven`.
- Crypto portability being `direct` is not authorization to trade; it only means the source's own evidence is crypto evidence.

## Limitations

- `underspecified` — no entry, exit, holding, sizing, threshold or execution rule exists in the source; all such content in this record is `research-proposed` / `research-defined`.
- `underspecified` — `FGI_scaled` has no stated scale factor; `N` is never stated; timezone/calendar/venue are never stated; the IF "plausible parameter box", starting point and random-start seeds are not disclosed.
- `data gap` — no out-of-sample evaluation, no forecast metric, no VaR/exception test, no economic or trading layer, no cost model of any kind, no confidence intervals or significance tests, no multiplicity control.
- `data gap` — Bitcoin price vendor, FGI provider and data vintages are absent from the paper and only partially inferable from code that itself disagrees ("CNN" label vs `api.alternative.me`).
- `not independently reproduced` — every number is third-party, in-sample, point-estimate evidence from a single preprint.
- `unproven` — H1 (incremental forecast content), H2 (stable fear asymmetry) and H3 (any economic value) are hypotheses; the source demonstrates in-sample fit only.
- Source-quality limitation: preprint only, no peer review, student-course-provenance code (README thanks a course instructor), paper dated 2026 while the released code predates it by ~15 months, and the released artifacts do not contain the reported model.
- Publication-bias / selection concern: benchmarks and hyper-parameters appear selected in-sample; the bimodal likelihood and the "best fit" choice of `nu = 5` are degrees of freedom for post-hoc selection.
- Identification limitation: `gamma`, `mu_h`, `sigma_eta` and `phi` are only partially identified (multi-modal, mutually compensating), so economic interpretation of the sentiment coefficient is fragile.
- Reproducibility limitation: without the enhanced-model code, seeds, parameter box and data vintages, Table II cannot be checked as published; the two released close series make even the input data ambiguous.

## Implementation status

`implementation_status: not-implemented`.

No POMP/iterated-filtering pipeline, no sentiment data store, no volatility filter, no downstream rule, no backtest and no paper/testnet/live run exists in our research stack. Nothing has been wired into Qlib, NautilusTrader or any production candidate path, and this record does not modify any of them. What exists today is a normalized research capture of a third-party in-sample model comparison plus its code-release caveats.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this record in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, Paper, Testnet or Live. Research capture is not adoption, and no wording, evidence count or confidence value in this record promotes it.

## Related Wiki records

Verified by read-only `kb_search` on 2026-09-25 (pages returned by the vault itself; none was invented):

- [[quant/crypto-kalshi-prediction-market-macro-repricing-volatility-forecasting-2026-09-01]] — crypto realized-volatility forecasting conditioned on an external (prediction-market) signal; the closest structural neighbour (external driver -> crypto vol state), but with a different signal source and no latent state-space filter.
- [[quant/regret-driven-portfolio-ftl-llm-hedging-sentiment-gated-2026-09-05]] — Fear-and-Greed used as an allocation gate rather than as a volatility-model regressor.
- [[quant/crypto-bitcoin-cvar-risk-aware-q-learning-adaptive-controller-2026-09-02]] — Bitcoin risk-control policy that takes the Fear & Greed Index as an environment input (risk/RL layer, not a volatility filter).
- `kb_search` for "sentiment augmented POMP bitcoin latent volatility fear greed regressor" returned **0 pages**, confirming there is no existing sentiment-augmented latent-volatility record in Wiki Brain.

Repository-adjacent records (repo files, not Wiki links, listed for the dedup trail): `crypto-macro-sentiment-contrarian-fear-greed-ema-2026-09-03.md`, `crypto-cross-sectional-sentiment-risk-beta-premium-2026-09-01.md`, `crypto-security-shock-cross-sectional-factor-hacks-mktcap-2026-09-01.md`, `market-regime-routed-specialist-gbt-asymmetric-hysteresis-2026-09-12.md`, `crypto-brown-esg-uncertainty-next-day-downside-liquidity-amplified-2026-09-03.md`, `sentiment-vader-technical-indicator-mean-variance-crypto-portfolio-2026-09-04.md`, `adaptive-tft-pattern-conditioned-crypto-volatility-forecasting-2026-09-05.md`, `crypto-volatility-risk-premium-variance-swap-estimator-fragility-decay-2026-09-12.md`.

## Sources

1. Abeyankar Giridharan, Chang Li, Suvrorup Mukherjee, Xinhe Wu, *Fear Moves Markets: Sentiment-Augmented POMP for Volatility Modeling of Bitcoin Returns*, `arXiv:2609.23250v2 [stat.AP]`, submitted 19 Sep 2026 23:21:57 UTC, last revised 22 Sep 2026 23:27:26 UTC; authors affiliated to the University of Michigan (Dept. of Statistics and Dept. of IOE). Abstract/landing: https://arxiv.org/abs/2609.23250 (read 2026-09-25; no Comments, no journal-ref, no peer-review statement; license CC BY 4.0).
2. Pinned primary HTML (source of the body read end to end): https://arxiv.org/html/2609.23250v2 — 127,791 bytes fetched, 29,039 characters of extracted text, retrieved 2026-09-25.
3. Pinned primary PDF cross-check: https://arxiv.org/pdf/2609.23250v2 — 2,513,803 bytes, SHA-256 `47e595c8a966a958595ecf0d94521653e1203fdc07391bc4139a5d55d1e86e6b`, retrieved 2026-09-25.
4. Version-contrast PDF v1 (not used for any number): https://arxiv.org/pdf/2609.23250v1 — 2,513,876 bytes, SHA-256 `a7152003c7192e970b37bd8b279d751404f5e82b1fd8ca6944ca88f78da26ed6`.
5. arXiv API metadata record: `https://export.arxiv.org/api/query?id_list=2609.23250`; DataCite DOI: https://doi.org/10.48550/arXiv.2609.23250 (HTTP 302 -> arXiv abs, checked 2026-09-25).
6. Code release named by the source: https://github.com/abeyankargiridharan/Novel_Approach_to_Volatility_Analysis_on_Bitcoin_Returns at pinned commit `4905198c12a6fdcf48689a313fef398130015179` (2025-06-14) — files read: `README.md`, `breto/final.R`, `bitcoin-preprocessing-HSV.Rmd`, `fng-analysis.Rmd`, `bitcoin-garch-analysis.R`, `requirements.txt`, `datasets/bitcoin_2020-01-01_2025-04-06.csv`, `datasets/bitcoin_fg.csv`, `volatility-project.html`.
7. Sentiment data endpoint used by the released code (not named in the paper): https://api.alternative.me/fng/ (`limit=1000` / `limit=2000`), read from the released R Markdown notebooks.
8. Works cited *by the source* for method provenance only (not used as empirical evidence here): C. Breto, *On idiosyncratic stochasticity of financial leverage effects*, Statistics & Probability Letters 91 (2014) 20-26; E. L. Ionides, D. Nguyen, Y. Atchade, A. A. King, *Inference for dynamic and latent variable models via iterated, perturbed bayes maps*, PNAS 112 (2015) 719-724; A. A. King, D. T. Nguyen, E. L. Ionides, *Statistical Inference for Partially Observed Markov Processes via the R Package pomp*, JSS 69(12) (2016) 1-43.
