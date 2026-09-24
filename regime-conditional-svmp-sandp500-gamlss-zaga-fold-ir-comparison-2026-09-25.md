---
schema: strategy-research-record-v1
title: "Regime-Conditional SVMP Technical-Signal Timing on the S&P 500 Index with GAMLSS/ZAGA Fold-Level Performance Distribution Comparison"
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equity-timing
  - single-index
  - walk-forward
  - support-vector-machine
  - technical-indicators
  - regime-conditional-evaluation
  - distributional-regression
status: research-only
confidence: medium
source_as_of: 2026-06-30
sources:
  - "Krzysztof Ozimek, 'Regime-Conditional Distributional Comparison of Trading Strategies: A GAMLSS/ZAGA Framework Applied to the S&P 500', arXiv preprint arXiv:2606.31251v1 [q-fin.ST], submitted June 30, 2026. DOI: 10.48550/arXiv.2606.31251. Stable URL: https://arxiv.org/abs/2606.31251"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Cross-reference mismatch: Section 3.1 states that estimated coefficients and model comparison statistics are reported in Table 1, while Section 3.3 states that Table 2 reports the estimated coefficients; the coefficients are in fact printed in Table 2 (Table 1 is the descriptive six-number summary). Unreconciled in the source."
  - "Framing tension: Section 3.1 reports that the standalone ZAGA fit for the SVMP series retained the null model under BIC, 'indicating that the IR* distribution of the active strategy is invariant to the market regime as characterised by MOM and RV', while the abstract, Section 3.4 and the Conclusions describe the dominance relationship as strictly regime-dependent. The two statements can be reconciled only through the pooled model's strategy-by-regime interaction terms (Table 2 Panels A and C), which the source does not spell out as a reconciliation."
---

# Regime-Conditional SVMP Technical-Signal Timing on the S&P 500 Index with GAMLSS/ZAGA Fold-Level Performance Distribution Comparison

## Provenance

- **Primary source:** Krzysztof Ozimek, *Regime-Conditional Distributional Comparison of Trading Strategies: A GAMLSS/ZAGA Framework Applied to the S&P 500*, `arXiv:2606.31251v1 [q-fin.ST]`, sole author, submitted **Tue, 30 Jun 2026 07:26:07 UTC (901 KB)**.
- **Author block exactly as source (PDF title page):** "Krzysztof Ozimek" with footnote *a* = "Independent Researcher, Warsaw (Poland). ORCID: https://orcid.org/0009-0005-5210-9205. E-mail: contact@drkrzysztofozimek.com". Single author; no co-authors, no affiliation beyond the independent-researcher footnote (`source-reported`).
- **Stable URL:** https://arxiv.org/abs/2606.31251 — version history shows **only [v1]**; `https://arxiv.org/abs/2606.31251v2` returns HTTP 404 (checked 2026-09-25).
- **Canonical DOI:** 10.48550/arXiv.2606.31251 resolves (HTTP 200 after redirect, checked 2026-09-25).
- **Full text actually read:** the arXiv HTML endpoint `https://arxiv.org/html/2606.31251v1` returns **HTTP 404**, so the **v1 PDF was pinned**: 922,289 bytes, 20 pages, SHA-256 `dee394a7911bfb3aa475867bf3e828471d3432ba64d064698b6fb0d1d644008c`, downloaded and read end-to-end 2026-09-25 covering the bilingual abstract, Sections 1–4, equations (1)–(20), Tables 1–4, Figure 1, and the full References list.
- **Publication / review status (`source-reported`):** arXiv abstract page shows **no Comments field, no Journal-ref, no publisher DOI beyond the DataCite arXiv DOI, and no peer-review statement** → **preprint / working paper only**. The PDF carries **no funding statement, no competing-interest declaration, no data-availability or code-availability statement, and no generative-AI statement** (word scan of the pinned PDF: `data availab` 0, `supplement` 0, `declarat` 0, `conflict` 0, `fund` 0, `GitHub` 0) → **no replication package is offered by the source (`data gap`)**.
- **Sample / data as-of:** daily S&P 500 index closes, **2 January 2002 – 31 December 2025** (`source-reported`, Section 2.1 and Table 1 note).
- **Repo-wide source-identity dedup (2026-09-25):** ripgrep over **all `.md` records in the repository (hidden-inclusive: `.mimo-worktrees`, `.agents`, `.hermes`)** plus `coverage_manifest.csv` for `2606.31251`, `10.48550/arXiv.2606.31251`, the exact title string `Regime-Conditional Distributional Comparison`, `GAMLSS`, `ZAGA`, `Grudniewicz`, `Ślepaczuk`/`Slepaczuk`, and `Adjusted Information Ratio` → **every exact-identity pattern returns zero hits** (manifest likewise zero). The only author-name hits are three lines of the distinct record `cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02.md` (same author, **different source identity** `arXiv:2606.08586`, BallMapper / decoder-conditional VAE / Function-on-Function regression on intraday cross-sectional anomaly scores).
- **Four-axis distinction (mechanism / signal / universe / horizon-regime / data dependency) against adjacent captures:** (1) `cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02` (Ozimek `2606.08586`) — intraday cross-sectional topological anomaly scores vs. this record's single-index time-series 7-indicator SVMP with long/flat/short thresholding; (2) `bitcoin-perpetual-information-bars-tick-minute-directional-failure-2026-09-02` — same SVM-family classifier label but crypto information-bar failure study, different market type, different features, different conclusion; (3) `statistical-arbitrage-rank-space-cnn-transformer-hybrid-atlas-2026-09-02` — cross-sectional rank-space CNN/Transformer portfolios vs. a single-index directional timing rule; (4) `us-etf-pairs-trading-cointegration-cost-viability-falsification-2026-09-13` — relative-value cointegration with explicit cost falsification vs. gross-of-cost index timing; (5) `equity-cross-regime-bayesian-optimisation-xgboost-tabnet-hybrid-2026-09-02` — cross-sectional regime-switched stat-arb models vs. a fold-level *evaluation* framework. None of them use a polynomial-kernel SVM on seven lagged price-only indicators with per-fold 40/60-percentile three-class thresholds, nor do they model fold-level `IR*` with a ZAGA distributional regression.

## Economic mechanism

### Source-reported

1. **Regime-conditional dominance instead of a single scalar verdict.** The source argues that collapsing an entire backtest to one number discards *when* a strategy works. Its claim is economic as well as statistical: an active ML signal and a passive buy-and-hold benchmark should respond differently to the same market state, so the sign of the performance gap should be a function of realised volatility (`RV`) and momentum (`MOM`).
2. **Where the active signal is supposed to add value.** The stated reading of the fitted model is a momentum-conditioned crossover: under low/negative momentum the active SVMP strategy keeps producing positive expected fold performance while buy-and-hold degrades (Section 3.4, Table 3), whereas in strongly positive momentum the passive benchmark dominates ("a trending market rewards a passive strategy over an ML-based signal", Section 3.4).
3. **Why a distributional model is needed.** `IR*` is floored at zero (folds with non-positive mean return get exactly 0), so the fold-level series is a point mass at zero plus a continuous positive tail — motivating a zero-adjusted Gamma (ZAGA) response inside GAMLSS with location/scale/zero-inflation parameters conditioned on regime covariates (Sections 2.2.5, 2.3).
4. **Signal generator (the tradable component).** A polynomial-kernel SVM regression (`SVMP`) on seven lagged technical indicators predicts the daily index return; three-class thresholds taken from the 40th/60th percentiles of the *in-sample fitted* values map the forecast to long (+1) / cash (0) / short (−1) (Sections 2.2.1–2.2.4).

### Research interpretation

- **Hypothesized mechanism (falsifiable form):** price-only technical composites carry weak conditional drift information whose usefulness is *state-dependent* — specifically, mean-reversion/short-horizon signal quality is higher when trailing 40-day momentum is low or negative, and is swamped by trend in strong positive momentum. Under this reading the SVMP rule is a **conditional market-timing hypothesis**, not a cross-sectional alpha.
- **Role of each component (ablation needed before crediting any of them):**
  - *Regime layer:* `RV` (within-fold standard deviation of daily returns) and `MOM` (compounded 40-day return) — **evaluation conditioning only**, not part of the trading rule.
  - *Primary signal:* 7 lagged indicators → SVMP regression forecast → 40th/60th percentile three-class signal.
  - *Risk/exit layer:* none beyond the 0 state (flat/cash). There is **no stop, no volatility target, no drawdown control, no position sizing rule**.
  - *Benchmark:* pure buy-and-hold of the index.
- **Critical interpretive point (`research interpretation`, supported by source structure):** the regime covariates are computed **inside the same out-of-sample window whose performance they condition on** (Eq. 10–11, Section 2.3.4). The regime label is therefore *not available in real time*; the whole regime-conditional result is a **descriptive, ex-post stratification**, and any prospective "trade the regime" reading of this record is a ported hypothesis, not something the source demonstrates. The source itself lists real-time regime classification as future work (Section 4).

## Signal

All rules below are `source-reported` from the pinned v1 PDF unless explicitly marked.

- **Instrument / price series:** S&P 500 index daily closes, ticker `^GSPC`, Yahoo Finance via `quantmod` (Section 2.1). Sample 2002-01-02 → 2025-12-31.
- **Feature set (7 inputs, Section 2.2.1):**
  1. SMA deviation: `P_t − SMA15_t` (15-day simple moving average);
  2. MACD signal: `MACD_t − signal_t` with 12-day EMA − 26-day EMA and a 9-day EMA of the MACD line;
  3. Stochastic Oscillator fast-%K window 14;
  4. Stochastic fast-%D smoothing 3;
  5. Stochastic slow-%D smoothing 3 (three stochastic series in total, so `p = 7`);
  6. RSI window 14;
  7. Williams %R window 14.
  Computed with the R package `TTR`; **all indicators are lagged by one period before use as model inputs to avoid look-ahead bias**.
- **Preprocessing:** min–max rescaling to `[−1, 1]`, with `min(x)`/`max(x)` **estimated on the in-sample window only** and applied unchanged to the out-of-sample window (Eq. 2, Section 2.2.3).
- **Model:** SVM in regression mode with polynomial kernel `k(x_i,x_j) = (c + (1/p)·x_i'x_j)^d`, **`p = 7`, `c = 2`, `d = 2`**, fitted with `e1071` in R; target = daily return (Sections 2.2.2–2.2.3).
- **Walk-forward protocol (Section 2.2):** fixed in-sample window `T_IS = 160` trading days → out-of-sample window `T_OOS = 40` trading days → step `Δ = 40` (non-overlapping OOS windows) → **`B = 146` complete folds** covering 2002–2025.
- **Entry / position rule (Eq. 3):** thresholds `q40`, `q60` are the empirical 40th and 60th percentiles of the SVMP **fitted values on the in-sample window of that fold**; for out-of-sample day `t`:
  `s_t = +1` if `r̂_t > q60`; `s_t = 0` if `q40 ≤ r̂_t ≤ q60`; `s_t = −1` if `r̂_t < q40`.
  `+1` = long, `−1` = short, `0` = no exposure (cash).
- **Returns:** `r_t^SIG = s_t · r_t`, benchmark `r_t^BH = r_t` (Section 2.2.4). Position is re-evaluated daily; **no holding-period cap, no re-entry rule, no stop, no sizing rule** are stated — full ±1× notional is implied by the return equation, and cash is assumed to earn zero (no risk-free rate appears anywhere: word scan `risk-free` 0).
- **Performance metric (Eq. 4):** fold-level Adjusted Information Ratio `IR*_b = (max{r̄_b; 0})² / (σ̂_b · MDD_b)` over the 40-day OOS window, where `MDD_b` is the in-fold maximum drawdown (Eq. 5). Strictly non-negative; **not annualised, not a Sharpe ratio**, and taken from Grudniewicz & Ślepaczuk (2025).
- **Evaluation layer (`source-reported`):** pooled dummy-variable GAMLSS/ZAGA model over `n = 2B = 292` fold observations with strategy indicator `D`, regime covariates `RV` (Eq. 10, within-OOS-window standard deviation of daily returns) and `MOM` (Eq. 11, compounded 40-day OOS return), plus `D×MOM` and `D×RV` interactions; `gamlss::stepGAICAll.A` stepwise selection with BIC penalty `k = log 292`; comparison via regime-specific `ΔE`, `ΔVar` (Eqs. 14–15) at six quantile-matched `(MOM, RV)` points, and a parametric bootstrap with `N_b = 9,999` replications of `n = 146` draws from the fitted ZAGA for three null hypotheses (Eqs. 16–19).
- **Underspecified / reconstructible-gap markers (`underspecified`):** (a) exact target alignment — inputs are lagged one period and the target is described as "daily returns", but the source never states explicitly whether the fitted target for row `t` is `r_t` or `r_{t+1}`, so the signal-to-order timing is *implied* rather than specified; (b) no execution price, order type, fill or latency convention anywhere; (c) no statement of how indicator warm-up days before the first 160-day IS window are handled; (d) Section 2.1 states only **closing prices** are retrieved, yet the Stochastic Oscillator conventionally needs high/low inputs — whether `TTR::stoch` was fed an HLC or a close-only series is not stated; (e) whether the 40/60 thresholds are recomputed per fold is stated (per fold), but no sensitivity to those two numbers is reported.

## Required data

- **Instrument / universe:** single instrument — S&P 500 index (`^GSPC`) daily closes. **No cross-section, no constituents, no corporate actions, no survivorship dimension** (index-level series).
- **Venue / data vendor:** Yahoo Finance via `quantmod` (`source-reported`). Point-in-time quality of that vendor feed over 2002–2025 is not discussed by the source (`data gap`).
- **Market type:** cash equity index (spot index level). No derivatives, no funding, no options surface.
- **Timeframe / fields:** daily bars; **closes are sufficient for SMA/MACD/RSI/Williams %R and for the log-return target**; high/low requirement for the stochastic oscillator is `underspecified` (see Signal).
- **Point-in-time / availability:** indicators lagged one period; min/max scaling fit on IS only (both `source-reported`). The regime covariates are **not** point-in-time — they use the full OOS window being evaluated (see Evidence → Negative evidence).
- **Timestamp / timezone:** not stated by the source; equity-session daily bars imply exchange-local session closes (`data gap` for explicit timezone convention).
- **Missing data / halts / dividends:** not addressed anywhere in the PDF (`data gap`). The index series is not adjusted for anything the source would need to declare, but no missing-print or holiday handling is described.
- **Cost data needed for any net test (all `research-proposed`, none supplied by the source):** commission, bid-ask/quoted spread, slippage, borrow fee and index-short availability, financing on cash, turnover measured from `s_t` changes, market impact, capacity.

## Execution assumptions

- **Source-stated model:** the strategy return is `s_t · r_t` with `s_t ∈ {−1, 0, +1}` recomputed every OOS day; performance is measured **gross of transaction costs** — the Conclusions list "a performance measure gross of transaction costs" as an explicit limitation (Section 4).
- **Pinned-PDF cost word scan (2026-09-25):** `transaction cost` 2 and `cost` 2 (both inside the Section 4 limitations/future-work sentence about adding transaction costs and bid-ask spreads as GAMLSS covariates), `bid-ask` 1 (same sentence), `spread` 3 (two are "dispersion/spread between strategies", one is the bid-ask future-work clause), `slippage` 0, `commission` 0, `fee`/`fees` 0, `borrow` 0, `turnover` 0, `capacity` 0, `latency` 0, `fill` 0, `leverage` 0, `market impact` 0, `rebalanc` 0, `holding` 0 (as a rule), `Sharpe` 4 (two are reference titles, one is prose about Chen & Lee 1981, one is the remark that `IR*` penalises what Sharpe leaves unaddressed — **no strategy Sharpe is printed anywhere**). → **No fee, spread, slippage, borrow, fill, latency, turnover, capacity or P&L-cost model exists in the source; every one of those fields is `data gap`, never "zero cost".**
- **Shorting:** the `−1` state implies a short position in an index with **no borrow availability, no stock-loan fee, and no index-proxy/instrument specification** (`data gap`); shorting a cash index level is not directly executable, so any real implementation needs a futures/ETF/swap proxy — a porting decision the source never makes (`research-proposed` if adopted).
- **Cash:** the `0` state is assumed to earn nothing (no risk-free rate, `risk-free` 0 hits) → any carry-aware test is `research-proposed`.
- **Signal-to-order timing:** not specified (see Signal underspecified item (a)); no next-bar rule, no same-bar rule, no order type, no partial-fill or failure handling.
- **Leverage / margin:** not mentioned; ±1× notional is implied by the return equation only.
- **Distinguish source vs. Scout:** everything in this record's Falsification plan that involves costs, proxies, thresholds for pass/fail, or live windows is `research-proposed` / `research-defined`; none of it comes from the source.

## Evidence

### Source-reported

All figures below are third-party claims read directly out of the pinned `arXiv:2606.31251v1` PDF (922,289 bytes, 20 pages, SHA-256 `dee394a7…4008c`), with the printed table/section given for traceability. **Nothing here has been independently reproduced, and nothing here is crypto evidence** (the sample is a US equity index).

- **Design:** 146 non-overlapping 40-day OOS folds, `T_IS = 160`, `T_OOS = 40`, `Δ = 40`, `^GSPC` daily 2002-01-02 → 2025-12-31 (Sections 2.1–2.2); pooled `n = 292` fold-strategy observations (Section 3.2).
- **Table 1 (descriptive statistics per fold):**
  - Zero-`IR*` folds: **39 / 146 (26.7%) for buy-and-hold vs 70 / 146 (47.9%) for SVMP**.
  - `IR*_BH`: min 0, 1st Qu. 0, median 0.0008801, **mean 0.0076762**, 3rd Qu. 0.0092805, max 0.0773044, skew 2.5080, excess kurtosis 6.7995.
  - `IR*_SIG`: min 0, 1st Qu. 0, median 0.0000036, **mean 0.0030820**, 3rd Qu. 0.0021380, max 0.0551700, skew 3.9623, excess kurtosis 21.0504.
  - `RV`: min 0.002636, mean 0.010092, max 0.044738, skew 3.1133, excess kurtosis 12.8257. `MOM`: min −0.250817, mean 0.016989, max 0.232265, skew −0.9685, excess kurtosis 4.1087.
- **Table 2 (pooled GAMLSS/ZAGA coefficients; RS algorithm converged in 2 cycles, residual df 280, global deviance −1498.43, GAIC(BIC) = −1430.30 with df 12 vs −1421.08 with df 18 for Strategy B, against a null dummy baseline of −1137.74 with df 6):**
  - log μ: intercept −6.0478 (t = −26.704), `D_SIG` +1.7435 (t = 3.364, p = 0.0009), `MOM` +53.7625 (p < 2e-16), `RV` −229.0470 (p < 2e-16), `D×MOM` −57.4065 (p < 2e-16), `D×RV` +141.2516 (p = 0.0035).
  - log σ: intercept −0.1106 (p = 0.0724), `D_SIG` +0.5802 (p = 4.5e-4) → **SVMP fold dispersion is unconditionally higher**.
  - logit ν: all four coefficients insignificant with **numerically inflated standard errors because of near-complete separation** (the source flags this in the Table 2 note).
- **Table 3 (regime-specific expected `IR*` and variance, six quantile-matched `(MOM, RV)` points):** `ΔE = E(IR*_SIG) − E(IR*_BH)` = **+0.011411 (Min.), +0.003915 (1st Qu.), +0.001986 (Median), +0.002142 (Mean), −0.000571 (3rd Qu.), −0.022130 (Max.)**; `ΔVar` positive at every regime except Max. (`+9.551e-4, +9.516e-5, +5.687e-5, +4.306e-5, +2.002e-5, −3.949e-4`), with `Var(IR*_BH)` at Min. reported as ≈ 0 (< 1e-8).
- **Table 4 (parametric bootstrap, `N_b = 9,999`, `n = 146` draws per replication):** `p̂1` (H0: `E(IR*_BH) ≤ E(IR*_SIG)`) = **1.0000 / 1.0000 / 1.0000 / 1.0000 / 0.1143 / 0.0000** across Min. → Max.; `p̂2` (H0: `Var(IR*_BH) ≤ Var(IR*_SIG)`) = 1.0000 / 1.0000 / 1.0000 / 1.0000 / 0.9979 / 0.0000; `p̂3` (signal-to-noise ratio, H0: `E/√Var` of BH ≤ that of SIG) = **NA / 0.8768 / 0.0000 / 0.0000 / 0.0000 / 0.0000**. `p̂3` is `NA` at Min. because `ν̂_BH → 1` drives all BH draws to zero (**T3 valid 0.0% of replications**; 100.0% at all other regimes).
- **Headline reading (`source-reported`, Sections 3.4 and 4):** SVMP has higher expected `IR*` under low-to-moderate momentum with "decisive bootstrap support from Median through Min.", buy-and-hold dominates at Max. momentum, and **buy-and-hold achieves the superior risk-adjusted ratio from Median onward** because "SVMP's variance penalty swamps its return advantage".
- **Computing environment / seeds / reproducibility:** R with `e1071` 1.7-16, `TTR`, `quantmod` 0.4.28, `gamlss`; no random seeds are relevant to the SVM fit, but **no code, notebook, or data-availability statement is provided** (`data gap`).

**Our own arithmetic on the printed cells (`our count`, consistency audit only — not a rerun):**
1. `ΔE` recomputed as `E(IR*_SIG) − E(IR*_BH)` from Table 3 columns reproduces all six printed values to the printed precision (e.g. Min. `0.011411 − 0.000000 = +0.011411`; Max. `0.000068 − 0.022197 = −0.022129` vs printed `−0.022130`); `ΔVar` likewise reproduces all six.
2. Zero-fold shares: `39/146 = 26.71%` (printed 26.7%), `70/146 = 47.95%` (printed 47.9%) — consistent; equivalently **SIG finished a fold with non-positive mean return in 70 cases against 39 for BH (76 vs 107 positive-mean folds)**.
3. Pooled `n = 2 × 146 = 292` matches the printed `2B = 292`.
4. Aggregate mean `IR*` ratio: `0.0076762 / 0.0030820 = 2.49` → **buy-and-hold's average fold `IR*` is about 2.5× the active strategy's**, an unconditional result that sits alongside (not against) the conditional Table 3 pattern.
5. Sample-length check: `160 + 146 × 40 = 6,000` days of history consumed; a 2002-01-02 → 2025-12-31 daily index sample contains on the order of ~6,000–6,050 trading sessions, and **the source never states how the residual tail days are handled** → recorded as `underspecified`, not as an error.
6. The six evaluation points are described in the Table 1 note as "quantile-matched `(MOM, RV)` pairs" taken from the **separate marginal** six-number summaries of `RV` and `MOM`, i.e. they are **marginal-quantile combinations, not observed joint regime states** (e.g. the "Min." point pairs minimum momentum with *minimum* realised volatility); the source does not state otherwise → flagged in Limitations.

### Independently reproduced

not independently reproduced

### Negative evidence

- **No cost model at all** — the performance measure is explicitly gross of transaction costs (Section 4), and the pinned-PDF word scan finds no fee/spread/slippage/borrow/turnover/latency/fill/capacity/impact model. Any claim about tradability from this record is unsupported by the source.
- **The active strategy loses on its own aggregate metric:** mean fold `IR*` 0.0030820 (SIG) vs 0.0076762 (BH), and **47.9% of SVMP folds score exactly zero vs 26.7% for buy-and-hold** (Table 1). The conditional advantage in Table 3 is therefore a *reweighting* claim, not a level claim.
- **Risk-adjusted comparison is rejected in favour of the passive benchmark from Median momentum upward** (`p̂3 = 0.0000` at Median, Mean, 3rd Qu. and Max., Table 4) — the source's own text: "BH achieves a superior risk-adjusted ratio — SVMP's variance penalty swamps its return advantage".
- **Structurally higher dispersion for the active strategy:** `ΔVar > 0` in 5 of 6 regimes and `D_SIG = +0.5802` (p = 4.5e-4) in the log σ equation (Tables 2–3).
- **Regime conditioning is ex-post by construction:** `RV` and `MOM` are computed *within* the OOS window being scored (Eqs. 10–11), so the regime label cannot be known at decision time; the source only proposes real-time regime classification as future work (Section 4). Any "switch strategies by regime" reading is `research interpretation`, not source evidence.
- **Model-based, not resampled, inference:** all bootstrap p-values are draws from the *fitted* ZAGA (Section 2.4.2), so "decisive" support is conditional on the ZAGA assumption; the source concedes "bootstrap inference depends on the ZAGA distributional assumption" (Section 4).
- **Numerical failure at the most adverse regime:** near-complete separation makes the ν-equation standard errors "numerically inflated" (Table 2 note) and renders `p̂3` undefined at Min. with **0.0% valid replications** (Table 4) — the headline SVMP-favouring regime is exactly where the inference breaks.
- **No standard performance reporting:** no Sharpe, no CAGR, no full-path maximum drawdown, no turnover, no trade count, no exposure statistics are printed anywhere for either strategy; the bespoke `IR*` (which squares the mean and floors at zero) is the only performance number in the paper.
- **Very heavy tails in the response:** excess kurtosis 6.80 (BH) and 21.05 (SIG) on 146 observations (Table 1) — fold-level means from 40-day windows are extremely noisy, and the 18-test grid (6 regimes × 3 hypotheses) carries **no multiple-testing correction** (no `BH`/`q-value`/`Bonferroni` language in the pinned PDF).
- **Data-availability red flags:** sole independent-researcher authorship, no peer review, no code, no replication package, no declarations, no funding statement, and a vendor (`Yahoo Finance`) whose index history is not validated for point-in-time integrity in the source.
- **Single instrument, single period, single model class** — the source's own limitation list (Section 4).
- **No short-side realism:** a `−1` state on a cash index with no borrow/proxy/cost modelling at all.

## Falsification plan

Every test below is `research-proposed`, and every numeric cut-off is a `research-defined falsification threshold`; none is stated by the source.

1. **F1 — Ex-post regime repair (the core validity test).** Re-derive `RV` and `MOM` using **only information available at the start of each OOS window** (trailing 40-day window ending at `t−1`), then recompute `ΔE` and the three bootstrap p-values at the same six quantile points.
   *Fail rule:* if the sign pattern "ΔE > 0 at low-to-moderate momentum, ΔE < 0 at Max." disappears, or `p̂1` at Min./1st Qu./Median/Mean falls below 0.50, the regime-conditional claim is **falsified as an artifact of in-window conditioning**.
2. **F2 — Cost ladder on the trading rule.** Rebuild `r_t^SIG` with 0/1/2/5/10 bp charged per position change (`|s_t − s_{t−1}|`), plus a stock-loan fee of 25 bp and 50 bp per year on the average short fraction, with an index-futures or ETF proxy for the `−1` state.
   *Fail rule:* if the sign of `ΔE` at Min./1st Qu./Median/Mean flips to ≤ 0 at **5 bp per side**, the strategy is **falsified as a frictionless artifact**.
3. **F3 — Turnover and holding audit.** Report one-way turnover, average holding length, and the distribution of `|Δs_t|`.
   *Fail rule:* if mean one-way turnover exceeds **10% of notional per trading day**, the gross-of-cost result is deemed **non-actionable regardless of `ΔE`** (a threshold chosen because daily three-class flipping on a 40/60 percentile band is the expected failure mode).
4. **F4 — Standard-metric horse race on the concatenated OOS path.** Compute full-path CAGR, annualised Sharpe, max drawdown, hit rate and exposure for SIG and BH (metrics the source never prints).
   *Fail rule:* if SIG Sharpe ≤ BH Sharpe **and** SIG max drawdown ≥ BH max drawdown, the active rule is **rejected on conventional metrics** even if conditional `ΔE` stays positive.
5. **F5 — Threshold perturbation.** Replace the (40th, 60th) percentile band with (30th, 70th) and (45th, 55th), re-running the full walk-forward.
   *Fail rule:* if the six-regime sign pattern of `ΔE` flips in **≥ 2 of 6 regimes** between neighbouring thresholds, the pattern is **parameter-fitting noise**, not a mechanism.
6. **F6 — Placebo signal.** 1,000 draws of a null signal that preserves the empirical long/flat/short state frequencies but randomly permutes the timing (circular block shifts of `s_t`).
   *Fail rule:* if the observed `ΔE` at Min. does not exceed the **95th percentile** of the placebo distribution, the low-momentum advantage is **not distinguishable from exposure allocation**.
7. **F7 — Multiple-testing control.** Apply Benjamini–Hochberg at `q = 0.10` across the 18 reported tests (6 regimes × 3 hypotheses), and re-run the bootstrap with a block-bootstrap resampling of realised fold returns instead of ZAGA draws.
   *Fail rule:* if **fewer than half** of the reported rejections/retentions survive, the inferential layer is **falsified as distributionally fragile**.
8. **F8 — Cross-instrument transport.** Freeze every parameter and rerun the identical pipeline on SPY, the STOXX 600, Nikkei 225 and CSI 300 (or BTC-USD as the crypto leg) over the same 2002/2014–2025 span.
   *Fail rule:* if low-momentum `ΔE ≤ 0` in **≥ 2 of 4** additional instruments, the regime-conditional mechanism is **not transportable** and should be dropped rather than retuned.
9. **F9 — Mechanism attribution ablation.** Swap SVMP for (a) logistic regression and (b) a shallow gradient-boosted tree on the identical seven features and thresholds, and separately (c) keep SVMP but randomise feature labels.
   *Fail rule:* if the regime pattern is identical across model classes and disappears only under feature randomisation, the source of the pattern is the **thresholded technical composite, not the SVM** — the record must then be re-scoped accordingly.
10. **F10 — Frozen forward window.** Lock the entire specification as of 2025-12-31 and evaluate 2026-01 onward without retuning.
    *Fail rule:* if, after **two consecutive full years**, cumulative `ΔE ≤ 0` or SIG underperforms BH on calendar-year return in both years, the hypothesis is **rejected prospectively**.

## Crypto portability

`unproven`

- The mechanism and all evidence come from a **US cash equity index** with a 16:00 US/Eastern session close; nothing in the source touches crypto, perpetuals, funding, or 24/7 timestamps.
- **Porting obstacles (`research interpretation`):** (a) `^GSPC` is an index level — a crypto port needs a defined instrument (spot basket, perpetual, or futures) with its own funding/basis, none of which the source models; (b) the `−1` short state needs a borrow/funding assumption that is `data gap` even in equities; (c) daily candle boundaries, weekend gaps and the 252-vs-365 calendar change every indicator window and the `MOM`/`RV` regime covariates; (d) crypto's 24/7 session changes what "one period lagged" and "daily return" mean, and the 40/60 percentile thresholds would need re-estimation; (e) venue fragmentation, index construction and rebalancing have no analogue in a single-vendor index feed.
- **What would still be testable:** the *evaluation* contribution (fold-level zero-inflated performance distribution conditioned on trailing regime covariates) is method-agnostic and could be applied to crypto fold returns — but that is a `research-proposed` reuse of the framework, not evidence that the SVMP timing rule works in crypto.

## Limitations

- `not independently reproduced` — every number is a third-party claim from an unrefereed single-author preprint with no code or data release.
- `underspecified`: signal-to-order timing (target alignment with the lagged features), execution price/order type/fill, indicator warm-up before the first IS window, close-only vs HLC input for the stochastic oscillator, handling of residual tail days after `160 + 146×40 = 6,000` consumed sessions, and the treatment of index holidays/missing prints.
- `data gap`: all cost, borrow, financing, capacity, latency and turnover fields; no risk-free rate on the cash state; no Sharpe/CAGR/MDD/turnover of the full path; no multiple-testing control; no point-in-time validation of the Yahoo Finance index history.
- **Ex-post regime labelling** — the central claim conditions performance on covariates computed from the very window being evaluated; this is the single largest identification gap in the record (see F1).
- **Marginal-quantile regime points** — the six `(MOM, RV)` evaluation points pair separate marginal quantiles (Table 1 note) and are therefore synthetic combinations rather than observed joint states; the source does not discuss joint-regime coverage.
- **Degenerate inference at the headline regime** — near-complete separation makes `p̂3` undefined at Min. (0.0% valid replications) and inflates the ν-equation standard errors; the regime most favourable to SVMP is the least statistically tractable.
- **Bespoke, non-standard metric** — `IR*` squares the mean daily return and floors at zero, so it is not comparable to Sharpe/Sortino values reported elsewhere, and its zero mass (26.7%/47.9%) drives the ZAGA specification in the first place.
- **Same-author adjacency** — the repository already holds a record from this author on a different paper (`arXiv:2606.08586`); the two must not be merged, and neither should be treated as independent corroboration of the other.
- **Source-quality:** preprint only (no Comments, no Journal-ref, no publisher DOI, no peer-review statement), independent researcher, no declarations of any kind.

## Implementation status

`not-implemented`. This is an upstream research capture only. No SVMP walk-forward pipeline, GAMLSS/ZAGA evaluation layer, or index-timing rule has been implemented in our research stack; no Qlib full backtest, no production card, no paper, testnet or live run exists for this record. The source itself ships no code, so nothing could be "implemented from the source" without re-deriving it from the PDF.

## Adoption boundary

- `status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.
- Presence in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet or live trading.
- All operational rules not stated by the source (costs, proxies, thresholds, fail cuts, live windows) are labelled `research-proposed` / `research-defined` and must not be quoted as source-reported.

## Related Wiki records

- [[quant/market-regime-routed-specialist-gbt-asymmetric-hysteresis-2026-09-12]] — adjacent regime-conditional equity timing (regime nowcaster + specialist GBTs + hysteresis, long-only, 5 bp costed); materially different mechanism: *trading* on a trailing regime label versus this record's *ex-post* conditioning of a fixed SVMP rule.
- [[quant/crypto-short-horizon-predictability-purged-walk-forward-audit-2026-09-11]] — adjacent walk-forward/short-horizon predictability audit with leakage controls; different market type and a purged protocol this source does not implement.
- [[quant/equity-cross-regime-bayesian-optimisation-xgboost-tabnet-hybrid-2026-09-02]] — adjacent cross-regime equity ML capture; cross-sectional stat-arb design rather than single-index directional timing.

(These three pages were located with `kb_search` and one was read in full; no other Wiki link is asserted for this mechanism.)

## Sources

1. Krzysztof Ozimek. *"Regime-Conditional Distributional Comparison of Trading Strategies: A GAMLSS/ZAGA Framework Applied to the S&P 500."* arXiv preprint `arXiv:2606.31251v1 [q-fin.ST]`, submitted 30 June 2026 (v1, 901 KB, sole version as of 2026-09-25).
   - Abstract / stable URL: https://arxiv.org/abs/2606.31251
   - Pinned full text (HTML endpoint returns 404): https://arxiv.org/pdf/2606.31251v1 — 922,289 bytes, 20 pages, SHA-256 `dee394a7911bfb3aa475867bf3e828471d3432ba64d064698b6fb0d1d644008c`, read end-to-end 2026-09-25.
   - Canonical DOI: https://doi.org/10.48550/arXiv.2606.31251 (resolves, checked 2026-09-25).
   - Author identifiers: ORCID 0009-0005-5210-9205; contact@drkrzysztofozimek.com; Independent Researcher, Warsaw (Poland).
2. Upstream references **cited inside** the primary source and used only to attribute the strategy's construction (not used as evidence in this record): Grudniewicz, J., & Ślepaczuk, R. (2025). *Application of machine learning in algorithmic investment strategies on global stock markets.* Research in International Business and Finance, 73, 102566. https://doi.org/10.1016/j.ribaf.2024.102566 (origin of the `IR*` measure and the SVMP choice); Dash, R., & Dash, P. K. (2016). *A hybrid stock trading framework integrating technical analysis with machine learning techniques.* Journal of Finance and Data Science, 1(2), 42–57 (origin of the seven-indicator feature set).
3. Repository dedup evidence: ripgrep scans of all `*.md` records plus `coverage_manifest.csv` on 2026-09-25 for `2606.31251`, the DataCite DOI, the exact title, `GAMLSS`, `ZAGA`, `Grudniewicz`, `Slepaczuk`, `Adjusted Information Ratio` → zero hits (author-name hits belong only to the distinct `arXiv:2606.08586` record).
