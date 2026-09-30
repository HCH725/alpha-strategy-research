---
schema: strategy-research-record-v1
title: "CZAR Zero-Agnostic Asymmetric Loss for Intraday BTC Log-Return Direction: Sign Long-Short Under a Cost-Excluded Naive Sharpe (arXiv:2609.36061)"
created: 2026-09-30
updated: 2026-09-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - btc
  - loss-function
  - objective-function
  - directional-accuracy
  - intraday
  - lightgbm
status: research-only
confidence: medium
source_as_of: "2026-09-28 (arXiv v1 submission date and ADI publication date); Tiingo BTC/USD 1-minute candles retrieved 2026-04-30"
sources:
  - https://arxiv.org/abs/2609.36061
  - https://arxiv.org/pdf/2609.36061v1
  - https://arxiv.org/html/2609.36061v1
  - https://doi.org/10.48550/arXiv.2609.36061
  - https://doi.org/10.70235/allora.0x30033
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Table 2 caption states that every CZAR variant lifts R_P and IC 'several-fold over the symmetric baselines', but the same table contradicts that generalisation in 45 of the 56 comparable (2 horizons x 2 baselines x 7 CZAR rows x 2 metrics) cells: 45 cells sit below 3x the baseline value -- 41 of them in the 1x-to-3x range and 4 below 1x, i.e. CZAR is worse than the symmetric baseline there: 15-minute CZAR(alpha=0.01) R_P 0.017 vs L1 0.019 (0.89x), 1-hour CZAR(alpha=0.005) IC 0.046 vs L1 0.053 (0.87x), 1-hour CZAR(alpha=1) IC 0.044 vs L1 0.053 (0.83x), 1-hour CZAR(tuned) IC 0.052 vs L1 0.053 (0.98x); recorded as printed, not reconciled."
  - "Section 4.2 prose states that CZAR 'keeps the aspect ratio within a factor of a few of unity across the whole alpha sweep', but Table 2 prints log10(AR) = -0.82 for 15-minute CZAR(alpha=1), i.e. a predicted spread 0.151x the true spread, which is 6.61x below unity, and -0.71 for CZAR(alpha=0.5) at both horizons, 5.13x below unity; recorded as printed, not reconciled."
---

# CZAR Zero-Agnostic Asymmetric Loss for Intraday BTC Log-Return Direction: Sign Long-Short Under a Cost-Excluded Naive Sharpe (arXiv:2609.36061)

## Provenance

- **Primary source (sole source for every number below):** arXiv `2609.36061v1`, Joel Pfeffer, J. M. Diederik Kruijssen, Florian Stecker and Steven N. Longmore, *"Introducing the CZAR Loss: A Tailored Objective Function for Financial Log-Return Predictions"*.
- **Author list exactly as source (three places agree):** exactly four authors in this order -- **Joel Pfeffer**, **J. M. Diederik Kruijssen**, **Florian Stecker**, **Steven N. Longmore**. Agreement between the PDF title page, the PDF `/Author` metadata (`Joel Pfeffer; J. M. Diederik Kruijssen; Florian Stecker; Steven N. Longmore`) and the four `citation_author` metas on the arXiv abs page (`Pfeffer, Joel`, `Kruijssen, J. M. Diederik`, `Stecker, Florian`, `Longmore, Steven N.`). Title-page affiliation footnotes: superscript 1 on Pfeffer, Kruijssen and Stecker, superscript 1,2 on Longmore, printed as `1Allora Foundation, 2Liverpool John Moores University`. No ORCID, no funding statement, no conflict-of-interest statement and no data- or code-availability statement appear anywhere in the pinned text (whole-document scan: `github.com` 0, `data availability` 0, `code availability` 0, `replication package` 0) -> those fields stay `data gap`.
- **Version / identifiers (arXiv abs page read 2026-09-30):** submission history has **one version** -- `[v1] Mon, 28 Sep 2026 18:18:06 UTC (764 KB)`, submitted by Diederik Kruijssen. PDF stamp `arXiv:2609.36061v1 [cs.LG] 28 Sep 2026`. `citation_date` = `2026/09/28`. Subjects: `Machine Learning (cs.LG)` primary, cross-listed `Computational Engineering, Finance, and Science (cs.CE)`, `Computational Finance (q-fin.CP)`, `Mathematical Finance (q-fin.MF)`. Comments field: `22 pages, 12 figures, 2 tables; appeared in ADI (September 2026)`. Journal reference field: `ADI 3, 33-54 (2026)`. DataCite DOI `10.48550/arXiv.2609.36061` plus publisher DOI `10.70235/allora.0x30033` (present in both the abs `citation_doi` meta and the PDF first-page line `Allora Decentralized Intelligence 3, 33-54; 2026 September 28 doi:10.70235/allora.0x30033`).
- **Publication status (recorded as printed):** published in *Allora Decentralized Intelligence* (ADI), volume 3, pages 33-54, dated 2026-09-28. The source makes **no peer-review statement** of any kind, and the journal name matches the authors' own affiliation (`Allora Foundation`); reference [Kruijssen et al. 2024] in the same reference list cites `Allora Decentralized Intelligence, 1, 1`, i.e. the venue itself. Peer-review status beyond "appeared in ADI" is therefore `not stated in source`.
- **License:** Creative Commons Attribution-ShareAlike 4.0 (`CC BY-SA 4.0`) -- arXiv license icon `licenses/by-sa/4.0` on the abs page and `/License` in the PDF metadata pointing at the `creativecommons.org/licenses/by-sa/4.0/` path (the metadata spells that path with an `http` scheme; the scheme is elided here to keep the record free of plain-http URLs). Text below is normalized, quoted sparingly, and analytically structured; no source text is copied wholesale.
- **Pinned primary snapshots (all fetched 2026-09-30):**
  - PDF: `https://arxiv.org/pdf/2609.36061` -> **1,159,819 bytes, SHA-256 `8b1d28878faadb6745befb7f1c10548fe4cfc18fdd640cddaac282b798c3daff`**; embedded metadata `/Title = Introducing the CZAR Loss: A Tailored Objective Function for Financial Log-Return Predictions`, `/Author = Joel Pfeffer; J. M. Diederik Kruijssen; Florian Stecker; Steven N. Longmore`, `/DOI = https://doi.org/10.70235/allora.0x30033`, `/arXivID = https://arxiv.org/abs/2609.36061v1`, `/Creator = arXiv GenPDF (tex2pdf:0d14211)`, `/Producer = pikepdf 8.15.1`. Extracted with `pypdf` 6.16.2 -> **22 pages, 86,183 characters, 1,721 lines, read end to end** (title page and affiliation footnotes, Abstract, Sections 1-5, Equations (1)-(11) and (B1)-(B8) and (C1)-(C7), Table 1 and Table 2, Figures 1-9 and D1-D3 captions, footnote 4 (strategy definition) and footnote 5 (Tiingo), the 34-item reference list, Appendix A reference implementation, Appendix B breakeven proof with Proposition 1, Appendix C pseudo-Huber smoothing, Appendix D parameter optimization). `pypdf` emitted `Exceeded 5000 form XObject invocations while extracting text; further form content is skipped` -- figure internals were therefore **not** machine-extracted, so every figure-level value below is marked as such.
  - abs page: `https://arxiv.org/abs/2609.36061` -> **46,977 bytes, SHA-256 `4817cfdf2171528f749dd331622234fda0e690bd69c691d5c7581bb48b03df51`**, read in full for authors, dateline, Comments, journal reference, DOI, subjects, license and submission history.
  - HTML full text: `https://arxiv.org/html/2609.36061v1` -> HTTP 200, **638,030 bytes, SHA-256 `6ae11aeddedfaecb808c8937c135758ba9d77f06684356e919dbb0ed7f0ef814`**, read for cross-surface verification; it contains exactly 12 article figures plus 2 `<figure class="ltx_table">` blocks (Table 1 and Table 2), matching the Comments field. Table 2 cells were parsed from the `alttext` of each `<math>` node so that the LaTeX-rendered copy and the `<annotation>` copy cannot double-count.
  - The served PDF is **1,159,819 bytes** while the submission history reports **764 KB** (arXiv GenPDF re-render) -- both figures recorded, **not reconciled**.
- **Sample period (as printed):** no calendar dates are given for the train or test windows. Section 4.2: a single most-recent split per horizon of **20,000 candles for training** (last **2,000** held out as Optuna inner validation), **one-candle gap**, then a **2,000-candle test window**. Table 2 caption: test windows of **approximately 21 days (15-minute)** and **approximately 83 days (1-hour)**. Data provenance sentence (Section 4.2; the footnote-5 marker that follows the vendor name in the source is omitted here): `one-minute BTC/USD OHLCV candles sourced from Tiingo` and `(retrieved on 2026-04-30), aggregated to the prediction horizon` -> **data as-of = 2026-04-30; calendar start/end of each window = `data gap`** (arithmetic only: 2,000 x 15 min = 20.83 days, 2,000 h = 83.33 days, consistent with the printed 21 days and 83 days, where the source prints an approximation glyph before each number).
- **Universe / instrument:** **BTC/USD, single asset, one-minute OHLCV candles from Tiingo**, aggregated to 15-minute and 1-hour. The strings `spot`, `perpetual`, `futures`, `exchange`, `venue` and `Binance` each occur **0 times** in the pinned PDF, so the market type (spot vs perpetual) and the venue are `not stated in source`. `BTC/USD` occurs exactly once (the provenance sentence above).
- **Code / replication package:** no repository, no code-availability or data-availability statement. Appendix A of the paper itself prints a NumPy reference implementation of `czar_loss`, `czar_gradient` and `czar_hessian` (with `_correlated_beta` and `_correlated_C` defaults), and the paper states the Hessian clip `1e-6` used in the LightGBM experiments lives in the training wrapper rather than in that listing. **No third-party code was executed in this run.**
- **Pre-write deduplication (2026-09-30, whole checkout, not `git log -20`):** hidden-inclusive `rg -uuu` over the entire working tree (tracked records, `.git/`, `.mimo-worktrees/`, `.agents/`, `.hermes/`) for `2609.36061`, `allora.0x30033`, `Kruijssen`, `Zero-Agnostic`, `zero-returns bias`, `Introducing the CZAR`, `Joel Pfeffer`, `allora.0x10001` -> **0 files for every token** (rg exit 1). The bare tokens `CZAR` -> **0 files** and `Pfeffer` -> **0 files**. `coverage_manifest.csv` (1,088,787 bytes) -> **0 hits** for `2609.36061`. Vendor token `Tiingo` -> 6 files resolving to only two distinct records (`llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04.md`, `us-etf-pairs-trading-cointegration-cost-viability-falsification-2026-09-13.md`, each plus two `.mimo-worktrees` copies) -- vendor vocabulary, not source identity. **Positive control in the same session:** `novy-marx` -> **42 files**, proving the scan is live. `git log --oneline -20` was inspected separately as a convenience glance only.
- **Material distinction from adjacent mechanism neighbors (dedup statement):** (a) `classification-cross-entropy-vs-mse-decile-long-short-arxiv-2108.02283-2026-09-30.md` (Bai & Pukthuanthong, arXiv `2108.02283`) -- also a loss-function record, but different source identity, different loss family (strictly proper *classification* scoring rule aligned with decile membership vs an *asymmetric magnitude* loss aimed at the zero-return attractor), different signal construction (cross-sectional top/bottom decile probability ranking vs sign of a single-asset time-series forecast), different universe (US common stocks, monthly, 1962-2024 vs BTC/USD intraday), different horizon and different data dependency (CRSP/Compustat 102 characteristics vs Tiingo 1-minute OHLCV). (b) `finance-grounded-loss-functions-band-turnover-crypto-2026-09-05.md` (arXiv `2509.04541`) -- differentiable portfolio-objective surrogates (Sharpe / drawdown / band turnover) for a crypto market-neutral network; different source, and portfolio-objective surrogates are not per-sample return losses. (c) `crypto-volatility-forecast-loss-level-alignment-risk-overlay-2026-09-25.md` (arXiv `2609.27024`) -- loss choice for *volatility-level* forecasting plus a multiplicative level-alignment factor; different source, different prediction target (variance level vs signed log return), different horizon (daily vs 15-minute/1-hour). (d) `gt-score-anti-overfitting-objective-multi-metric-gate-2026-09-05.md` -- a multi-metric anti-overfitting *strategy* objective, not a per-sample training loss. (e) `bitcoin-regime-aware-meta-learning-selective-directional-trading-2026-09-13.md` and `btc-usdt-l2-queue-imbalance-short-horizon-ic-economics-gap-2026-09-19.md` -- BTC directional/short-horizon signals, but regime-gating and queue-imbalance mechanisms with different sources. This record therefore differs from every neighbor on **source identity** and, independently, on at least two of **mechanism** (removal of the zero-returns attractor by direction-oriented asymmetric loss), **signal construction** (sign of `y_hat`, unit long/short, rebalanced every candle), **universe/market type** (single-asset intraday BTC/USD), **horizon/regime** (15-minute and 1-hour candles) and **material data dependency** (Tiingo 1-minute BTC/USD). It is a new source identity (`arXiv:2609.36061`).

## Economic mechanism

### Source-reported

The authors' stated story (Abstract, Sections 1, 2, 5): financial log-returns have a conditional mean close to zero, so symmetric regression losses (MSE, MAE, and every Bregman loss whose optimal predictor is the conditional mean) are minimized in expectation by a near-zero forecast. A constant zero prediction therefore becomes a near-optimal solution -- the **"zero-returns bias"** / zero-returns attractor -- both during training (predictions shrink toward zero, destroying the forecast as a directional signal) and during evaluation (trivial forecasters lead loss-based rankings). Section 2 shows that under the Gaussian linear prediction model `y_hat = rho*y + sigma_N*xi` with `y ~ N(0,1)`, **all symmetric monotonic losses share one universal breakeven directional accuracy** (Appendix B, Proposition 1): the breakeven condition reduces to `(1-rho)^2 * sigma^2 + sigma_N^2 = sigma^2`, i.e. `rho_min = 1 - sqrt(1 - (sigma_N/sigma)^2)`, and substituting into `DA = 1/2 + (1/pi) * arctan(rho*sigma/sigma_N)` gives `DA = 0.5 + arctan(rho_min*sigma/sigma_N)/pi`, valid for `0 <= sigma_N <= sigma` and identical for mean (linear) and mean-log averaging. At `sigma_N > sigma` no Gaussian linear model can beat the zero predictor under any directional accuracy.

CZAR (Composite Zero-Agnostic Return) is the source's answer: a piecewise-quadratic loss, convex in the prediction at fixed true value, whose asymmetry is oriented by the **sign of the true return** rather than by the sign of the error. Standardized variables `z = (y - mu)/sigma`, `z_hat = (y_hat - mu)/sigma`, asymmetry factor `beta_eff(|z|) = 1/(1 + beta*|z|)`, then Region A (wrong direction, or correct direction but undershooting): `(1 - beta_eff)*|z_hat - z| + (alpha/2)*(z_hat - z)^2`; Region B (correct direction and overshooting): `beta_eff*(alpha/2)*(z_hat - z)^2`; plus an evaluation-only floor `L_floor(z)` that raises the zero-prediction loss to a target `C`. The floor contributes **no gradient** (it depends only on `z`), so training-time pressure away from zero comes entirely from the Region A asymmetry, while the floor acts only on sample-averaged validation and ranking losses. The stated economic rationale for the direction-orientation is that overshooting a correctly-signed prediction is nearly harmless while undershooting or predicting the wrong direction is not, and the asymmetry vanishes as the true return approaches zero.

The source also positions the loss for decentralized inference networks: Section 5 states that in "decentralized inference networks such as Allora (Kruijssen et al., 2024), where topic-level losses determine the relative rewards of competing workers ... a symmetric criterion would actively subsidize zero-like inference strategies." This is an **author-adjacent interest** (the authors are Allora Foundation staff, the venue is ADI, and reference [Kruijssen et al. 2024] is a self-citation to the same venue) -- recorded as printed, and carried as a source-independence limitation below.

### Research interpretation

Falsifiable restatement: **the training/evaluation loss is a first-order design choice for a signed intraday crypto return signal, because an asymmetric direction-oriented loss stops the model class from collapsing onto the zero forecast, and only forecasts whose spread is not collapsed carry usable sign information -- but the source demonstrates this only as a cost-excluded, single-window, single-asset, single-seed comparison whose gains disappear if model selection uses a symmetric criterion.** Component roles (`research interpretation`):

```text
Regime / conditioning:  none - the claim is unconditional; no regime filter exists in the source
Primary signal:         sign(y_hat) of a LightGBM forecast of the next 15-minute or 1-hour
                        BTC/USD log return, where y_hat is trained with CZAR (alpha grid)
                        and standardized by a 100-candle rolling return sigma (min 50)
Baseline / control:     identical LightGBM pipeline trained with L1 (MAE) and L2 (MSE)
                        on the same features, split, seed and tuning budget
Confirmation:           the ablation in Section 4.2 that re-selects every model (including
                        CZAR-trained ones) on the symmetric log-L1 validation loss
Position:               unit long when y_hat > 0, unit short when y_hat < 0, fully invested,
                        rebalanced every candle (source's own footnote 4 definition)
Risk / exit:            none - no stop, no sizing, no drawdown control exists in the source
                        (drawdown 0 occurrences); risk management is not part of the hypothesis
```

Competing explanations that must be tested rather than assumed away: (i) the reported CZAR naive-Sharpe gains are **annualized from 21-day and 83-day windows with an IID scaling factor**, which the source itself calls a reporting convention citing Lo (2002), so they may be sampling noise rather than signal; (ii) each Table 2 row is **independently tuned with 300 Optuna trials on its own loss**, so the cross-row comparison is not on a common selection criterion and no multiple-testing correction exists (`Benjamini`, `deflated`, `bootstrap`, `multiple test` all 0 occurrences); (iii) the sign rule is **fully invested and rebalances every candle** with all frictions excluded, so any positive naive Sharpe is gross of a very large turnover; (iv) the improvement is concentrated in the tails (DA_1sigma, DA_IQR) while full-sample DA is within one binomial standard error of the baselines, which the source explicitly concedes.

## Signal

All items below are `source-reported` unless explicitly marked `research-proposed`, `research-defined` or `underspecified`. Notation normalized to ASCII: the source prints the Greek letters alpha, beta, sigma, mu, tau, rho; `DA_1sigma` below is the source's `DA_1s` column with a Greek sigma, `log10AR` is `log10(sigma_pred / sigma_true)`.

- **Target (Section 4.2):** next aggregated-candle log return `log(c_{t+1} / c_t)`, at a 15-minute or 1-hour horizon, from one-minute BTC/USD candles aggregated to the horizon.
- **Features (Section 4.2, computed exclusively from past candles):** single-candle log returns and within-candle realized volatilities at the **six most recent lags**; candle-geometry features (log high-low range, open-to-close return, upper and lower wick lengths, position of the close within the candle range); the log gap between the close and the OHLC4 typical price together with its **5- and 15-candle rolling means**; volume features (log volume and two log volume-change ratios over horizon-relative windows); and **sin/cos encodings of time-of-day and day-of-week** from UTC timestamps. Exact definitions of the two volume-change ratio windows are `underspecified` (the source says only "over horizon-relative windows").
- **Standardization (Section 3.1 footnote 2 and Section 4.2):** `mu = 0` (natural for short-horizon log returns); `sigma` is a **100-candle rolling standard deviation of single-candle realized returns, minimum 50 candles**; the same values are used during training and evaluation.
- **Split:** single most-recent split per horizon -- **20,000 candles training**, last **2,000 as Optuna inner validation**, **one-candle gap**, **2,000-candle test window**. No walk-forward, no expanding window, no embargo beyond the single gap (`walk-forward` 0, `expanding` 0, `holdout` 0 occurrences).
- **Training objective (Section 3, Appendix A):** CZAR via its analytical gradient and Hessian passed to LightGBM through the `objective` hook; **Hessian clipped from below at 1e-6**. Hyperparameters (Table 1): `alpha` (quadratic strength, `alpha > 0`, default **1**), `beta` (asymmetry decay, default `beta*(alpha)`, Eq. 10: `beta*(alpha) = 4.2*alpha^0.56 + 27.0*alpha^2.17`, calibrated on `1e-4 <= alpha <= 0.7`, giving `beta*(1) = 31.2`), `C` (floor target, default `C*(alpha)`, Eq. 11: asymmetric Hill-bell with linear correction, coefficients `(A,t,p,k,R,m) = (7.90, 4.59e-3, 0.657, 0.684, 2.25, -0.218)`, range `1e-5 <= alpha <= 1`, giving `C*(1) = 2.19`), `tau` (hinge smoothing, default **0.5**, the smallest value monotonic across `alpha <= 1`).
- **Alpha sweep:** `alpha` in `{0.005, 0.01, 0.05, 0.1, 0.5, 1}` plus one **CZAR-tuned** row in which `alpha` is an Optuna parameter on a log grid `[1e-3, 1]` while evaluation uses a fixed `alpha = 1` to keep the loss scale constant. The tuned rows print `alpha ~ 0.054` (15-minute) and `alpha ~ 0.0045` (1-hour).
- **Tuning (Section 4.2):** every Table 2 row is **independently tuned** with Optuna (TPE, **300 trials per model**), minimizing the sample mean of the logarithm of the per-sample values of that row's **own** training loss, `<log|L|>`. Joint search space: `num_leaves in [15,127]`, `min_child_samples in [20,300]`, `subsample` and `colsample_bytree` in `[0.6,1]`, L1 and L2 leaf regularization strengths in `[1e-8,10]` (log-scaled); **fixed random seed 42** so each per-row study is deterministic. Early stopping after **100 rounds** without inner-validation gain, capped at 5,000 trees (typically under 200). Learning rate calibrated per loss as `0.05 / s_loss` where `s_loss` comes from a one-tree LightGBM fit at learning rate 1, anchored to a base L2 rate of **0.05**.
- **Portfolio rule (footnote 4, verbatim substance):** each period the strategy takes a **unit long position when `y_hat > 0` and a unit short position when `y_hat < 0`**, earning the realized return `sign(y_hat)*y`; it **stays fully invested and rebalances every candle**; the reported Sharpe **excludes transaction costs, slippage, and position sizing**.
- **Metrics (Section 4.2 and Table 2 caption):** directional accuracy (DA) over the full sample; DA restricted to truths outside the interquartile range (`DA_IQR`); DA restricted to `|z| > 1 sigma` (`DA_1sigma`); `log10AR = log10(sigma_pred/sigma_true)`; Pearson correlation `R_P`; rank correlation `IC`; and a **naive annualized Sharpe** defined as `mean(sign(y_hat)*y) / std(sign(y_hat)*y)` annualized by `sqrt(525960/ell)` with `ell` the horizon in minutes and 525,960 the number of one-minute intervals per year -- factors of **approximately 187** (15-minute) and **approximately 94** (1-hour).
- **Holding period / exit / re-entry:** holding period equals one candle (rebalance every candle). No stop, no take-profit, no signal-strength threshold, no cash rule -> `underspecified`.
- **Position sizing:** unit long/short, fully invested; **no leverage, gross-exposure cap, per-name cap or risk budget** -> `data gap`.
- `research-proposed` operationalisations (none appear in the source): next-candle entry at the aggregate candle close with market orders; a per-side cost ladder of 0/1/2/5/10 bps; a minimum-conviction deadband `|z_hat| < delta` that stays flat; a 100-candle warm-up discarded from the test window; a second-vendor replication of the 1-minute series.

## Required data

- **Instrument:** BTC/USD (single asset). Contract type (spot vs perpetual), quote/settlement currency and settlement convention are `not stated in source` (0 occurrences of `spot`, `perpetual`, `futures`, `exchange`, `venue`).
- **Universe:** single instrument; no inclusion/exclusion rule, no liquidity filter, no survivorship handling, no reconstitution schedule (not applicable to a single-asset study, but also not discussed).
- **Venue / data vendor:** Tiingo, one-minute BTC/USD OHLCV candles; the paper states no venue aggregation rule and no license terms -> `data gap`.
- **Market type:** `not stated in source`. Tiingo's `BTC/USD` feed is a spot composite by vendor convention, but the paper never says so; treat market type as `data gap` until independently resolved.
- **Timeframe:** one-minute source candles aggregated to **15-minute** and **1-hour** prediction horizons; `525,960` one-minute intervals per year inferred from the median candle interval.
- **Fields:** OHLCV (open, high, low, close, volume); derived log returns, within-candle realized volatility, high-low range, wick lengths, close position in range, OHLC4 typical price, log volume and two log volume-change ratios, plus UTC time-of-day/day-of-week sin/cos encodings.
- **Point-in-time:** features are stated to be "computed exclusively from past candles"; the target is the *next* aggregated candle; the one-candle gap separates validation from test. Publication/availability lags and any stale-candle handling are `not stated in source`.
- **Timestamp / timezone:** UTC explicitly (time encodings "from UTC timestamps"); clock source, precision, alignment and out-of-order handling `not stated in source`.
- **Missing data:** `not stated in source` -> `data gap`.
- **Standardization input:** a 100-candle rolling standard deviation of single-candle realized returns, minimum 50 candles, computed identically for training and evaluation.
- **Funding / fee / spread needs:** **none are modelled** -- `fee`/`fees` 0, `commission` 0, `bid-ask` 0, `turnover` 0, `market impact` 0, `latency` 0, `funding` 0, `financing` 0, `leverage` 0, `dividend` 0, `liquidity` 0, `capacity` 0 occurrences. Any costed replication must supply these itself.

## Execution assumptions

Cost treatment was determined at Methods level from Section 4.2 (including footnote 4), the Table 2 caption, Section 5 and Appendix A, plus a word-boundary census of the pinned 86,183-character PDF text:

- `transaction cost` / `transaction costs` = **1** -- the footnote 4 sentence defining the naive Sharpe as excluding "transaction costs, slippage, and position sizing".
- `slippage` = **1** -- the same sentence.
- `fee` / `fees` = **0**, `commission` = **0**, `bid-ask` = **0**, `turnover` = **0**, `market impact` = **0**, `impact` = **0**, `latency` = **0**, `limit order` = **0**, `market order` = **0**, `participation` = **0**, `borrow` = **0**, `funding` = **0**, `financing` = **0**, `leverage` = **0**, `dividend` = **0**, `liquidity` = **0**, `capacity` = **0**, `backtest` = **0**, `drawdown` = **0**, `risk-free` = **0**, `buy-and-hold` = **0**.
- `fill` = **1**, and the single hit is the non-friction prose "designed to fill this gap".
- `position sizing` = **1** and `rebalance(s)` = **1**, both inside footnote 4; `portfolio` = **1** (the phrase "tied to a particular portfolio construction"); `Sharpe` = **10**.

So the source models **no friction at all, by explicit design**: the Table 2 caption states the naive Sharpe ratios "exclude costs (i.e. are not comparable to live trading)". Order type, fill model, signal-to-order delay, latency, spread, slippage, impact, participation, borrow, funding, financing, leverage, dividend treatment and capacity all stay **`data gap` and are never read as zero** -- the two friction-word hits are the source's own statement that those items are excluded.

Remaining material assumptions, as printed: **next-candle, candle-close decision with rebalance every candle** (the position is marked on the realized return of the *next* aggregated candle); **unit position, fully invested, both directions**; **no fees, no spread, no slippage, no impact, no borrow cost, no funding**; **no leverage and no margin rule**; **no partial-fill or failure handling**; annualization by `sqrt(525960/ell)` which the source itself says "assumes serially uncorrelated returns and should be read as a reporting convention rather than an estimate of attainable annual performance (Lo, 2002)".

## Evidence

### Source-reported

Every figure below is `source-reported`, transcribed from the pinned primary source with Table/Section provenance, and **none has been independently reproduced**.

**Idealized tests (Section 4.1, Figures 7-9 -- figure-level, not machine-verifiable this run because pypdf skipped form XObject content):**

- Under mean log loss, CZAR's breakeven directional accuracy tracks the 50% chance line to within **approximately 5 percentage points or better across `sigma_N` in [0, 1.5]**, versus the universal symmetric envelope which rises sharply as `sigma_N -> 1`. Under mean linear loss CZAR's breakeven is intermediate but improves on the asymmetric-MAE envelope at every noise scale.
- Monte Carlo: **5 x 10^4 samples per `(rho, sigma_N)` pair** for the Section 4.1 sweeps; **N = 50,000** for the beta optimization at `sigma_N = 1` (Appendix D, Figure D1); **N = 10^6** for the 95% binomial CI band in Figure D3.
- Heavy tails: the same sweeps with unit-variance Student-t truths at `nu = 5` and `nu = 3`; under log loss heavier tails raise the breakeven for both losses while CZAR retains its margin over MSE at every `sigma_N` and tail index, with mild degradation attributed by the source to Gaussian-calibrated defaults.
- Figure D3 legend prints optimal floor levels `C* = 3.6, 3.2, 2.8, 2.5, 2.4, 2.3, 2.2` at `alpha = 0.01, 0.03, 0.1, 0.3, 0.5, 0.7, 1` -- independently recomputed from Eq. (11) this run as **3.55, (not checked), 2.80, (not checked), (not checked), (not checked), 2.19**, consistent at the printed precision for the three values checked.

**Table 1 (CZAR hyperparameters):** `alpha` default 1 (`alpha > 0`); `beta` default `beta*(alpha)`, Eq. (10); `C` default `C*(alpha)`, Eq. (11); `tau` default 0.5.

**Table 2 (held-out metrics, 18 rows x 7 metrics) -- column order exactly as printed: `DA`, `DA_IQR`, `DA_1sigma`, `log10AR`, `R_P`, `IC`, `Sharpe_naive`:**

| Training loss | DA | DA_IQR | DA_1sigma | log10AR | R_P | IC | Sharpe_naive |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **BTC 15-minute** | | | | | | | |
| L1 | 0.510 | 0.487 | 0.473 | -0.93 | 0.019 | 0.018 | -4.97 |
| L2 | 0.514 | 0.508 | 0.499 | -1.18 | 0.016 | 0.019 | 0.96 |
| CZAR (alpha=0.005) | 0.531 | 0.523 | 0.537 | -0.46 | 0.046 | 0.034 | 5.62 |
| CZAR (alpha=0.01) | 0.522 | 0.504 | 0.501 | -0.44 | 0.017 | 0.033 | -0.95 |
| CZAR (alpha=0.05) | 0.523 | 0.525 | 0.534 | -0.59 | 0.033 | 0.050 | 3.95 |
| CZAR (alpha=0.1) | 0.513 | 0.514 | 0.511 | -0.58 | 0.025 | 0.019 | 1.15 |
| CZAR (alpha=0.5) | 0.521 | 0.523 | 0.532 | -0.71 | 0.033 | 0.029 | 4.76 |
| CZAR (alpha=1) | 0.514 | 0.514 | 0.527 | -0.82 | 0.055 | 0.032 | 5.08 |
| CZAR (tuned, alpha~0.054) | 0.524 | 0.519 | 0.561 | -0.60 | 0.039 | 0.056 | 7.09 |
| **BTC 1-hour** | | | | | | | |
| L1 | 0.518 | 0.505 | 0.473 | -0.96 | 0.019 | 0.053 | -1.09 |
| L2 | 0.517 | 0.513 | 0.485 | -1.02 | 0.001 | 0.021 | 1.29 |
| CZAR (alpha=0.005) | 0.521 | 0.526 | 0.538 | -0.41 | 0.038 | 0.046 | 2.67 |
| CZAR (alpha=0.01) | 0.526 | 0.528 | 0.524 | -0.54 | 0.034 | 0.065 | 2.38 |
| CZAR (alpha=0.05) | 0.516 | 0.522 | 0.531 | -0.49 | 0.034 | 0.058 | 2.86 |
| CZAR (alpha=0.1) | 0.526 | 0.546 | 0.550 | -0.55 | 0.047 | 0.072 | 5.96 |
| CZAR (alpha=0.5) | 0.515 | 0.521 | 0.520 | -0.71 | 0.044 | 0.059 | 3.89 |
| CZAR (alpha=1) | 0.512 | 0.523 | 0.529 | -0.62 | 0.041 | 0.044 | 3.21 |
| CZAR (tuned, alpha~0.0045) | 0.519 | 0.525 | 0.520 | -0.45 | 0.031 | 0.052 | 3.00 |

Table 2 caption claims (each checked against the cells this run): L1 and L2 "shrink their predictions well below the truth" with `log10AR` the caption prints as approx. -0.9 to -1.2 (cells: -0.93, -1.18, -0.96, -1.02) and their large-move DA "sits at or below the 50% chance line"; every CZAR variant keeps `log10AR` closer to zero, "often raise DA on large moves above chance" (cells **0.501 to 0.561**), "lift RP and IC several-fold over the symmetric baselines" (**contradicted -- see contradiction 1**) and "generally improve the naive Sharpe". Section 4.2 prose, stated separately: the symmetric large-move DA "falls at or below 50%" with the printed range `0.47-0.50` (cells: 0.473, 0.499, 0.473, 0.485) while CZAR "lifts DA 1sigma above chance for every setting" with the printed range `0.50-0.56` (the source prints an approximation glyph and an en dash in both ranges) -- cells **0.501 to 0.561**.

**Section 4.2 prose claims (each verified against Table 2 this run):**

- Binomial standard errors on the 2,000-candle test window: **approximately 1.1 percentage points** on full-sample DA, **approximately 2 points** on `DA_1sigma` (about one third of the sample) and **approximately 1.6 points** on `DA_IQR` (about one half). Recomputed independently: `sqrt(0.25/2000) = 1.12pp`, `sqrt(0.25/667) = 1.94pp`, `sqrt(0.25/1000) = 1.58pp` -- all three match.
- "Given a binomial standard error of approximately 1.1 percentage points ... full-sample DA is **generally statistically indistinguishable** from L1 and L2."
- "Every fixed CZAR setting clears both symmetric losses (L1 and L2) on the naive Sharpe at the 1-hour horizon, and all but one (alpha = 0.01) do so at the 15-minute horizon." **Verified cell-by-cell**: 6/6 at 1-hour; at 15-minute the sole failure is `CZAR (alpha=0.01)` at **-0.95** versus L2 **0.96** (and L1 **-4.97**).
- The tuned variant "delivers the best 15-minute `DA_1sigma` (**0.561**)" -- **verified** as the maximum `DA_1sigma` among all 15-minute CZAR rows.
- Symmetric predictions shrink "roughly an order of magnitude" (`log10AR` about **-0.9 to -1.2**) while CZAR's aspect ratio grows from about **-0.82 at alpha=1** to about **-0.46 at alpha=0.005** at the 15-minute horizon -- **verified** against the printed cells.
- Annualization factors **approximately 187** and **approximately 94** -- recomputed `sqrt(525960/15) = 187.25` and `sqrt(525960/60) = 93.63`. Test windows **approximately 21 and 83 days** -- recomputed 20.83 and 83.33 days.

**Section 4.2 selection ablation (the source's own robustness warning):** repeating the 15-minute experiment while selecting **every** model, including the CZAR-trained ones, on the **symmetric log-L1** validation loss pulls CZAR back onto the aspect-ratio degeneracy: `log10AR` collapses from the **-0.4 to -0.8** range into the **-1.0 to -1.4** range of the symmetric losses, and `DA_1sigma` and `DA_IQR` are reduced to **approximately 50%**. The source's own conclusion: "Training with CZAR is thus necessary but not sufficient ... so the gains reported above rely on using CZAR as both the training objective and the model-selection loss."

### Independently reproduced

Not independently reproduced.

The only verification performed this run was **arithmetic and fidelity checking of the pinned primary artefacts** (not a reproduction of the experiment): a standalone script exit 0 with **78 checks / 0 failures** covering (a) the word-boundary friction census above including the exact footnote-4 and Table-2-caption sentences, (b) re-parsing all 18 Table 2 rows from the pinned HTML `alttext` and confirming every prose claim listed above cell-by-cell, (c) the two contradiction enumerations (45 of 56 sub-3x cells with 4 below 1x; aspect ratio 6.61x and 5.13x below unity), (d) derived arithmetic -- annualization factors, test-window days, the three binomial standard errors, `beta*(1) = 31.2`, `C*(1) = 2.19`, `C*(0.01) = 3.55` vs the printed 3.6, `C*(0.1) = 2.80` vs the printed 2.8, the `C*` peak near `alpha = 1e-2`, the `C*` sign change between `alpha = 10` and `alpha = 11`, the universal breakeven limit `0.75` at `sigma_N = sigma`, `DA(rho=0.1, sigma_N=0.5) = 0.563` from Eq. (B5), and `E|N(0,1)| = 0.7979` against the Figure 1 annotation 0.795, and (e) source-surface facts -- 4 `citation_author` metas, single v1 dated 28 Sep 2026, both DOIs, the Comments string, the journal reference, the CC BY-SA 4.0 license, cs.LG primary, 14 HTML `<figure>` blocks = 12 figures + 2 tables, 22 PDF page markers, the ADI page footer, a 34-URL reference block, and the absence of any `github.com` or data/code-availability statement. No market data was downloaded, no model was trained, no third-party code was executed, and no figure-level value was machine-verified.

### Negative evidence

Numbered items 1-24; items 1-2 are the recorded contradictions and are restated here for completeness.

1. **Caption claim contradicted by its own table (contradiction 1):** "several-fold" lift in `R_P`/`IC` fails in **45 of 56** comparable cells -- 41 of those in the 1x-to-3x range and **4 below 1x**, i.e. CZAR is *worse* than the symmetric baseline: 15-minute `CZAR(alpha=0.01)` `R_P` 0.017 vs L1 0.019 (0.89x); 1-hour `CZAR(alpha=0.005)` `IC` 0.046 vs L1 0.053 (0.87x); 1-hour `CZAR(alpha=1)` `IC` 0.044 vs L1 0.053 (0.83x); 1-hour `CZAR(tuned)` `IC` 0.052 vs L1 0.053 (0.98x).
2. **Prose claim contradicted by its own table (contradiction 2):** "within a factor of a few of unity" versus `log10AR = -0.82` (0.151x, **6.61x** below unity) at 15-minute `alpha=1`, and `-0.71` (0.195x, **5.13x** below unity) at both horizons for `alpha=0.5`.
3. **All frictions are excluded by design.** Footnote 4 and the Table 2 caption both state costs, slippage and position sizing are excluded and the numbers are "not comparable to live trading". The word census shows zero occurrences of fee, commission, bid-ask, turnover, market impact, latency, order type, participation, borrow, funding, financing, leverage, dividend, liquidity and capacity.
4. **Turnover is maximal by construction.** The rule is fully invested and "rebalances every candle" -- at the 15-minute horizon that is up to 2,000 decision points inside a ~21-day test window, all cost-free.
5. **Full-sample directional-accuracy gains are within sampling error**, by the source's own statement: binomial SE about 1.1pp versus CZAR-minus-baseline DA gaps that are mostly 0.2-2.0pp; the source concedes full-sample DA is "generally statistically indistinguishable" from L1 and L2.
6. **The gains live in the tails, which carry the larger standard errors** (about 2pp on `DA_1sigma`, about 1.6pp on `DA_IQR`), i.e. the headline improvement is measured on roughly one-third to one-half of a 2,000-candle sample.
7. **Not every CZAR variant improves the naive Sharpe.** 15-minute `CZAR(alpha=0.01)` prints **-0.95** versus L2 **0.96**; 15-minute `CZAR(alpha=0.1)` prints 1.15, barely above L2. The abstract's general "improve long-short performance" wording does not carry this exception; the body does.
8. **Single asset, single split, single seed.** BTC/USD only; one most-recent 20,000/2,000/2,000 split per horizon; `seed` occurs once in the document (42). No walk-forward, no expanding window, no second window, no second asset, no second vendor.
9. **Test windows of about 21 and 83 days.** Every Sharpe in Table 2 is annualized from those windows by an IID `sqrt(T)` factor that the source explicitly labels a reporting convention citing Lo (2002).
10. **No multiple-testing control.** Each of the 18 rows gets 300 Optuna trials on its own loss; `Benjamini`, `deflated`, `bootstrap` and `multiple test` each occur **0** times; the alpha grid (6 fixed + 1 tuned) x 2 horizons is itself a selection space with no correction.
11. **Cross-row comparison is not on a common selection criterion** -- each row is tuned and early-stopped on its own loss, so a row's advantage can be partly a selection-objective advantage.
12. **The source's own ablation shows the gain is selection-dependent:** re-selecting on the symmetric log-L1 loss collapses CZAR `log10AR` from -0.4/-0.8 to -1.0/-1.4 and pushes `DA_1sigma`/`DA_IQR` back to about 50%. The source states training with CZAR is "necessary but not sufficient".
13. **No benchmark at all.** `buy-and-hold` occurs 0 times; there is no comparison against holding BTC, against an always-long rule, or against any trivial baseline, and no risk metric whatsoever (`drawdown` 0, `risk-free` 0).
14. **No statistical significance test is reported** for any Table 2 difference -- no t-statistic, no p-value, no confidence interval on the CZAR-minus-baseline gaps (the binomial SEs are reported but no test is run on them).
15. **Venue and instrument type are unstated** (`spot`/`perpetual`/`exchange`/`venue`/`Binance` all 0), so the trading object cannot be pinned down from the source alone.
16. **Single-vendor data with no availability/quality statement**, retrieval date 2026-04-30 only; missing-data, stale-candle and out-of-order handling all `not stated in source`.
17. **Feature definitions partially underspecified** -- the two log volume-change ratios are described only as "over horizon-relative windows".
18. **Heavy-tail degradation is admitted:** the `beta*` and `C*` defaults were calibrated on the Gaussian linear testbed, and the source states the log-loss breakeven degrades under Student-t truths, expecting recalibration to recover "much of the gap".
19. **The loss floor never touches training gradients** -- by construction `L_floor` depends only on the true value, so any training-time benefit rests entirely on the Region A asymmetry; the floor only changes rankings.
20. **The loss introduces a stated forecast bias** -- the Discussion concedes CZAR removes the zero-returns attractor "at the cost of a characterizable forecast bias"; magnitude is not quantified in the source.
21. **No code, no data, no replication package** -- `github.com`, `data availability`, `code availability` and `replication package` all 0 occurrences; only a NumPy listing in Appendix A (and the Hessian clip used in the experiments is explicitly *not* in that listing).
22. **Source-independence gap:** all four authors are affiliated with the Allora Foundation, the venue (ADI, *Allora Decentralized Intelligence*) carries the same name, reference [Kruijssen et al. 2024] cites that same venue at volume 1 page 1, and the Discussion names Allora as a direct beneficiary of a non-symmetric criterion. No peer-review statement appears anywhere.
23. **Figure-level claims are unverified here** -- `pypdf` skipped form XObject content, so the approximately-5pp breakeven statement (Figure 7), the Figure 1 panel annotations and the Figure D1-D3 surfaces were read only as captions and surrounding prose; panel-to-annotation mapping in the extracted text could not be established unambiguously and is recorded as `data gap`.
24. **Served-artefact mismatch:** submission history says 764 KB while the served PDF is 1,159,819 bytes (recorded, not reconciled), and no contrary external study or replication of CZAR was identified in this run -- absence of contrary evidence is not evidence of absence.

## Falsification plan

Each gate has a `research-defined falsification threshold` and an explicit action; none of these thresholds appears in the source.

- **F1 -- printed-value reproduction.** Re-run the pinned split and reproduce all 18 Table 2 rows. *Threshold:* every `DA`/`DA_IQR`/`DA_1sigma`/`log10AR`/`R_P`/`IC` cell within 0.0005 and every `Sharpe_naive` cell within 0.01 of the printed value. *Action on failure:* the transcription or the source's pipeline is wrong -- stop and re-audit before any further use of this record.
- **F2 -- common-selection-criterion ablation.** Re-run all rows selecting (and early-stopping) every model, including CZAR-trained ones, on **one shared** validation loss, and separately on CZAR as the shared loss. *Threshold:* CZAR must still beat L2 on `DA_1sigma` by at least **1.0pp** at both horizons under *both* shared-selection choices. *Action on failure:* relabel the finding as selection-loss-dependent and withdraw any claim of loss-driven improvement (no retuning allowed to rescue it).
- **F3 -- cost ladder.** Apply 0/1/2/5/10 bps per side round-turn to the sign rule at both horizons, plus a half-spread variant. *Threshold:* the CZAR-greater-than-L2 ordering must survive at **2 bps per side** and net `Sharpe_naive` must remain **> 0**. *Action on failure:* the record becomes evidence-against -- a cost-excluded intraday sign claim cannot be operationalised at its own turnover.
- **F4 -- turnover and capacity bound.** Measure two-way turnover per day for each row. *Threshold:* if round-turn turnover exceeds **20x notional per day**, mark capacity-infeasible regardless of Sharpe. *Action on failure:* cap the claim to research-only and forbid any capacity inference.
- **F5 -- multiple-testing control.** Apply Benjamini-Hochberg across the full grid (18 rows x 5 seeds x 2 horizons). *Threshold:* the CZAR-minus-L2 `DA_1sigma` gap must survive at **q <= 0.10**. *Action on failure:* downgrade to "not established".
- **F6 -- multi-window walk-forward.** At least **5 non-overlapping test windows totalling >= 12 months**, with a one-candle gap between train/validation/test and identical frozen hyperparameters. *Threshold:* CZAR beats L2 on `DA_1sigma` in **>= 4 of 5** windows at the 1-hour horizon. *Action on failure:* classify the effect as regime-dependent.
- **F7 -- seed stability.** Repeat with seeds {42, 7, 123, 2024, 31337}. *Threshold:* the sign of the CZAR-minus-L2 `DA_1sigma` gap must be consistent in **>= 4 of 5** seeds. *Action on failure:* treat the effect as noise.
- **F8 -- benchmark gate.** Compare the sign rule against always-long BTC over the same windows and against the L1/L2 pipelines with a paired test. *Threshold:* `Sharpe_naive` must exceed the always-long Sharpe with a paired **p < 0.05** (research-defined). *Action on failure:* the long-short sign rule adds nothing over holding.
- **F9 -- placebo.** Circularly shift the target by +/- 1 day (research-proposed shift length), 1,000 draws, keeping the pipeline fixed. *Threshold:* the real `DA_1sigma` must exceed the **95th percentile** of the placebo distribution. *Action on failure:* artefact of calendar/seasonality structure rather than signal.
- **F10 -- heavy-tail / distribution-shift recalibration.** Re-derive `beta*(alpha)` and `C*(alpha)` on the empirical return distribution (or Student-t with `nu` in {3, 5}) instead of the Gaussian testbed. *Threshold:* the log-loss breakeven must stay **>= 50%** across `sigma_N` in [0, 1.5]. *Action on failure:* the defaults are Gaussian-specific and the breakeven claim does not transport.
- **F11 -- second-vendor replication.** Rebuild the 1-minute BTC/USD series from an independent vendor. *Threshold:* `|Delta DA_1sigma| <= 1.0pp` **and** the sign of the CZAR-minus-L2 gap unchanged. *Action on failure:* data-construction artefact.
- **F12 -- point-in-time / leakage audit.** Verify every feature, including the 100-candle rolling `sigma` (min 50), is computable at the decision candle's close with no future information, and that the one-candle gap really separates validation from test. *Threshold:* zero future-derived features. *Action on failure:* reject the record outright.
- **F13 -- no-retuning rule.** Freeze the alpha grid, `beta*(alpha)` from Eq. (10), `C*(alpha)` from Eq. (11), `tau = 0.5`, the feature list, the split protocol and the seed set for the entire battery. *Threshold:* a failed gate may not be rescued by changing any frozen element. *Action on failure:* any change restarts the whole battery as a new, separately registered hypothesis.

## Crypto portability

**direct** (mechanism demonstrated in crypto by the source itself) -- with economic viability **unproven**.

- The source is native crypto: the only empirical experiment is **BTC/USD intraday (15-minute and 1-hour)**, so unlike a traditional-asset strategy this one does not need to be ported at all. The mechanism (a direction-oriented asymmetric loss) is instrument-agnostic, and nothing in it depends on equity market structure.
- What is *not* demonstrated: the source shows **no perpetual-futures evidence** (`perpetual`, `futures`, `funding` all 0 occurrences), so funding-rate drag, mark/index-price liquidation mechanics and basis are entirely unmodelled for a perpetual implementation; `spot` and `exchange`/`venue` are also 0 occurrences, so even the spot/perpetual identity of the tested instrument is `data gap`.
- 24/7 session structure: the source's only session-aware inputs are sin/cos time-of-day and day-of-week encodings, which on a 24/7 market encode thin-liquidity hours rather than an open/close cycle; no session rule, no forced flat, no settlement boundary exists in the rule.
- Venue fragmentation, custody, stablecoin/quote-currency effects, liquidity and market-impact differences, and timestamp/candle-boundary conventions across venues are all `data gap` -- none appears in the source and none was modelled.
- Cost anchor: there is **no cost anchor to inherit** (all friction words 0 except the two exclusion statements), so any crypto port must bring its own fee, spread, slippage and funding model from scratch (F3).
- Crypto portability is not authorization to trade; it says only that the mechanism requires no market-structure translation.

## Limitations

- `underspecified`: calendar windows; venue; spot vs perpetual; missing-data handling; the two volume-change ratio windows; order type, fill model, latency and signal-to-order delay; any sizing or risk rule.
- `data gap`: no code, no data, no replication package; figure-level values not machine-verifiable this run (pypdf form-XObject skip); served PDF size vs submission-history size unreconciled.
- `not independently reproduced`: every Table 2 number and every Section 4.1/4.2 claim. Only arithmetic and fidelity checks on the pinned artefacts were performed (78 checks, 0 failures, script exit 0).
- `unproven`: that CZAR-trained signals survive costs, survive multiple-testing correction, survive a second window or a second seed, or beat a buy-and-hold baseline -- none of these is tested by the source, and none was tested here.
- Source-quality caveat: single-group paper in a same-named venue with no peer-review statement and an explicit institutional interest in the loss's adoption (Section 5 names Allora as a beneficiary).
- Two unreconciled internal inconsistencies are carried in `contradictions` (`contested: true`): the "several-fold" `R_P`/`IC` caption claim (45 of 56 cells below 3x, 4 below 1x) and the "factor of a few of unity" aspect-ratio claim (6.61x and 5.13x below unity).
- This record is a capture of a **training-objective / signal-construction hypothesis**, not of a fully specified trading strategy: the predictive-signal half is specified, the execution half is absent by design.
- No contrary external study of CZAR was found in this run; absence of contrary evidence is not evidence of no negative result.

## Implementation status

`not-implemented`. This is a research capture only. Nothing in this record has been implemented in our research stack: no LightGBM or CZAR objective has been trained, no backtest has been run, no market data has been downloaded, no third-party code has been executed, and no Qlib, Paper, Testnet or Live verification of any kind has occurred. The source's own numbers are cost-excluded and were produced by the authors, not by us.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. Those are separate, gated decisions that have not been taken. No wording, confidence level, evidence count or schedule in this record promotes it.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` -- canonical strategy-research specification (resolved read-only this run; `quant/strategy-research-record-spec-v2.md` returned file-not-found, so the run failed closed onto v1 at 10,289 bytes, sha256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`).
- `[[quant/crypto-short-horizon-predictability-purged-walk-forward-audit-2026-09-11]]` -- the closest methodological neighbor: it audits short-horizon **crypto return predictability** against the zero-return null with purged walk-forward validation, Pesaran-Timmermann directional tests, 17 bps per-side costs and Deflated Sharpe, and finds net directional edges collapse under costs. Read and verified this run (29,160 bytes, sha256 `332112a8fc2c2a1def9eb6a0c1d11c423204b76a49db58d6a0c1b17078de4a1c`). It is the falsification template this record's F3/F5/F6/F8 mirror; different source, different horizon (daily vs intraday), different mechanism (predictability audit vs loss-function design).
- `[[quant/sharpe-deflated-multiple-testing-2026-08-27]]` -- Lo (2002) Sharpe statistics, `sqrt(q)` annualization caveats and Deflated Sharpe Ratio. Read and verified this run (14,435 bytes, sha256 `5faef5088806d7c0c4be5464b8deec0ebf57dd405c91235af6f170f4fc0588fb`). Directly relevant because the source's `sqrt(525960/ell)` annualization of 21-day and 83-day windows is exactly the IID assumption that page cautions against.

No other Wiki page was verified as related this run; no link was asserted from an unverified `kb_search` result (two searches -- `CZAR zero-returns asymmetric loss objective` and `cross-entropy classification mean squared error decile long-short` -- each returned 0 pages).

## Sources

1. Pfeffer, Joel; Kruijssen, J. M. Diederik; Stecker, Florian; Longmore, Steven N. "Introducing the CZAR Loss: A Tailored Objective Function for Financial Log-Return Predictions." *Allora Decentralized Intelligence* 3, 33-54 (2026 September 28). DOI `10.70235/allora.0x30033`. Allora Foundation and Liverpool John Moores University.
2. Same work, arXiv preprint: `arXiv:2609.36061v1 [cs.LG]`, submitted Mon, 28 Sep 2026 18:18:06 UTC. Abstract page https://arxiv.org/abs/2609.36061; pinned PDF https://arxiv.org/pdf/2609.36061v1 (1,159,819 bytes, SHA-256 `8b1d28878faadb6745befb7f1c10548fe4cfc18fdd640cddaac282b798c3daff`); pinned HTML https://arxiv.org/html/2609.36061v1 (638,030 bytes, SHA-256 `6ae11aeddedfaecb808c8937c135758ba9d77f06684356e919dbb0ed7f0ef814`); DataCite DOI https://doi.org/10.48550/arXiv.2609.36061. All fetched 2026-09-30.
3. Data vendor named by the source (not consulted directly): Tiingo, one-minute BTC/USD OHLCV candles, retrieval date as printed: 2026-04-30, https://www.tiingo.com/.
4. Cited by the source and used only as the source's own justification, not consulted here: Lo, A. W. (2002), "The Statistics of Sharpe Ratios", *Financial Analysts Journal* 58(4), 36-52 (annualization caveat); Kruijssen et al. (2024), *Allora Decentralized Intelligence* 1, 1 (the Allora network reference).
