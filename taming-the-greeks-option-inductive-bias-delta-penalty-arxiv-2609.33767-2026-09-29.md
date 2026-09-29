---
schema: strategy-research-record-v1
title: "Taming the Greeks: end-to-end LSTM option straddles with a differentiable Delta risk-sensitivity penalty (Nasdaq 100 equity options)"
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - options
  - straddle
  - delta-hedging
  - deep-learning
  - regularization
  - equity-options
status: research-only
confidence: medium
source_as_of: 2026-09-27
sources:
  - "https://arxiv.org/abs/2609.33767v1"
  - "https://arxiv.org/html/2609.33767v1"
  - "https://doi.org/10.48550/arXiv.2609.33767"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "C1: Section 7 Conclusion claims 'the best variant retaining a Sharpe ratio of 1.053 at 100 bps', but every cell of the Table 5 100.0 bps column is at most 0.871 (Baseline LSTM + TC Reg.), and Section 6.4 itself prints 0.871 as the highest 100 bps Sharpe; 1.053 appears in Table 1 as the Baseline row's Ave. P/L value."
  - "C2: Section 6.4 states 'The L1-based penalties consistently outperform their L2 counterparts across both the ENP and DP variants, particularly at higher cost levels' (Table 5 at 100 bps: ENP (L1) 0.718 vs ENP (L2) 0.634, DP (L1) 0.860 vs DP (L2) 0.763), while Section 7 states 'Among all variants, the L2 variants offer the most favorable trade-off'."
  - "C3: Section 7 states 'Incorporating turnover regularization during training further improved robustness at high cost levels', but in Table 5 the + TC Reg. rows at 100 bps are below their plain counterparts for both drift-penalty families (DP (L1) 0.777 vs 0.860; DP (L2) 0.690 vs 0.763); only Baseline, ENP (L1) and ENP (L2) improve (0.871 vs 0.816; 0.770 vs 0.718; 0.839 vs 0.634)."
  - "C4: Section 6.1 states signals are rescaled 'to target an annualized volatility of 15%' and Table 1 is captioned 'Rescaled to Target Volatility', but the printed Vol. column spans 0.156 to 0.199 with no value equal to 0.150 and no ex-ante versus ex-post reconciliation in the text."
  - "C5: Section 6.3 states 'the highest Sharpe variants reduce mean gross Delta by only approximately 5%-10%', but research-computed reductions of the Table 3 gross mean against the Baseline 0.256 using the Table 1 best rows are ENP (L1) 5.1 percent, ENP (L2) 1.6 percent, DP (L1) 9.8 percent and DP (L2) 3.5 percent, so the stated band covers only the two L1 variants."
---

# Taming the Greeks: end-to-end LSTM option straddles with a differentiable Delta risk-sensitivity penalty (Nasdaq 100 equity options)

## Provenance

- **Primary source (pinned version):** Wee Ling Tan, Stephen Roberts, Stefan Zohren, "Taming the Greeks: Option Portfolios with Inductive Biases", `arXiv:2609.33767v1 [q-fin.PM]`.
- **Authors exactly as printed:** Wee Ling Tan (corresponding author, `weeling@robots.ox.ac.uk`), Stephen Roberts (`sjrob@robots.ox.ac.uk`), Stefan Zohren (`stefan.zohren@eng.ox.ac.uk`); printed affiliations: Department of Engineering Science and Oxford-Man Institute of Quantitative Finance, University of Oxford. The abstract page lists the same three authors in the same order; no ORCID is printed.
- **Version / date:** single version `v1`, submitted Sun 27 Sep 2026 17:05:50 UTC (7,930 KB), submission history "From: Wee Ling Tan". The HTML masthead prints `arXiv:2609.33767v1 [q-fin.PM] 27 Sep 2026`. There is no v2 and no replacement.
- **Subjects:** Portfolio Management (q-fin.PM); Machine Learning (cs.LG); Computational Finance (q-fin.CP); Trading and Market Microstructure (q-fin.TR).
- **DOI:** `10.48550/arXiv.2609.33767`, labelled by arXiv as "arXiv-issued DOI via DataCite (pending registration)".
- **Publication status:** no `Comments` field, no `Journal reference`, no publisher DOI and no peer-review statement anywhere on the abstract page, so publication status is **not stated in source**; this is a preprint only. The HTML license line reads "arXiv.org perpetual non-exclusive license".
- **Primary-source checksum (read end to end):** `https://arxiv.org/html/2609.33767v1`, HTTP 200, 323,493 bytes downloaded, converted to 80,649 characters over 1,425 lines and read completely on 2026-09-29, covering the Abstract, Sections 1-8, equations (1)-(17), Tables 1-6, Figures 1-9 captions, the 34-item reference list, Appendix A (hyperparameter grid) and Appendix B; plus the abstract page `https://arxiv.org/abs/2609.33767` at 41,934 bytes for submission history, subjects and license. The PDF was not downloaded, so the PDF byte count and PDF checksum are **data gap**.
- **Data provenance:** the empirical work uses OptionMetrics Ivy DB (proprietary, licensed) for end-of-day option bid/ask quotes, implied volatilities and Greeks; no dataset, code repository or code-availability statement appears in the pinned text (the only "GitHub" strings are arXiv page chrome).
- **Deduplication (hidden-inclusive, pre-write):** `rg -uuu` across the whole checkout including `.git`, `.mimo-worktrees/`, `.agents/`, `.hermes/` and `coverage_manifest.csv` for `2609.33767`, `Taming the Greeks`, `Greek-ratio`, `exposure-normalized` and `Wee Ling Tan` returned only the same-author, different-paper record `spatio-temporal-momentum-multitask-shrinkage-turnover-regularization-2026-09-06.md` (matched on the author name only, source `arXiv:2302.10175`); `2609.33767` and `Taming the Greeks` returned zero files anywhere in the checkout, and `coverage_manifest.csv` returned zero matches for `33767` and `Taming`. A broader `drift penalty` scan matched only `dynamic-portfolio-optimization-cvar-stochastic-control-hjb-2026-09-02.md` (an HJB portfolio-control phrase, unrelated source). Positive control `novy-marx` matched 22 files in the same session. `git log --oneline -20` was used only as a convenience glance. Re-run after the final `git pull` returns only this record.

## Economic mechanism

### Source-reported

The authors' claim is a *training-objective* claim, not a new risk premium. End-to-end neural trading objectives that maximise risk-adjusted return are "agnostic to the sensitivities of the resulting portfolios with respect to specific underlying risk factors" and therefore "implicitly load on specific undesirable risks"; adding a differentiable risk-sensitivity penalty to the loss "natively embeds hedging behavior into the network's learning process". They instantiate the penalty on first-order directional exposure (Delta) of a static delta-neutral straddle portfolio, arguing that although an at-the-money straddle starts at Delta approximately 0, "as the underlying asset price drifts away from the initial strike ... net Delta accumulates towards an absolute value of 1.0 as one leg moves deep in-the-money", so "unhedged Delta dominates the variance of the strategy's payoff". A naive absolute-Delta penalty is rejected because it "admits a degenerate solution" the authors call **signal shrinkage** (the model can zero every position to buy the reward), motivating two scale-free variants: an exposure-normalized penalty (Delta per unit gross allocation) and a Greek-ratio drift penalty (Delta per unit Gamma, acting as a structural weight on contracts that have drifted out of the convex ATM region). The stated economic benefit is that moderate regularization "acts as a beneficial inductive bias", improving out-of-sample risk-adjusted return while reducing directional exposure; the stated cost is that "hedging is not costless" once the penalty dominates.

### Research interpretation

Hypothesized mechanism in falsifiable form: **the unconstrained end-to-end Sharpe objective harvests a persistent long-Delta tilt (an unintended market-timing/long-beta load) inside a nominally delta-neutral option portfolio, and a scale-free Delta penalty removes that tilt, so the residual return should be closer to a pure non-directional straddle return; if the residual Sharpe does not fall when the tilt is removed, the "hedging benefit" story is wrong and the reported gain is generic regularization or selection.** Component roles:

```text
Regime / universe: monthly standard (third-Friday) options on Nasdaq 100 constituents,
                   near-ATM straddles formed at each monthly expiry
Primary signal:    LSTM f_theta mapping point-in-time option features to X in [-1, 1]
Confirmation / risk: differentiable Delta penalty added to the negative-Sharpe loss
                     (exposure-normalized ENP or Greek-ratio drift DP, L1 or L2, alpha = 1e0..1e7)
Risk / exit:       no exit rule; position weights fixed from formation to expiry with a
                   one-time delta hedge at inception, signal re-scaled daily to 15% target vol
```

Ablation required by this interpretation: a generic-regularization control (weight decay or a shuffled-Delta penalty at matched magnitude) is absent from the source, so the source cannot distinguish "Delta-specific hedging inductive bias" from "any extra loss term helps". This is recorded as a data gap, not as evidence for either side.

## Signal

All items below are `source-reported` unless marked otherwise.

- **Formation timestamp / tradability:** portfolio formation occurs on each monthly option expiry date; features are end-of-day OptionMetrics observables of that formation date, and daily strategy returns are computed from closing bid-ask midpoints, so the signal is an end-of-day signal evaluated on next-day midpoint values. Timezone, clock and same-bar versus next-bar execution convention are **not stated in source** (data gap).
- **Universe screen (formation date):** keep only standard monthly options expiring on the third Friday of the following month; exclude weeklies and contracts affected by special settlements or other corporate actions; drop observations violating American-style arbitrage bounds, with zero bid, or with ask <= bid; keep only contracts with strictly positive open interest at formation.
- **Instrument construction:** per stock, pair the call and put with the same strike expiring the following month whose moneyness (`S/K` for calls, `K/S` for puts) is closest to 1.0, restricted to `[0.95, 1.05]`; "equivalently, this selection criterion targets a straddle Delta of close to zero at initiation".
- **Weights:** `w_call = -Delta_put / (Delta_call - Delta_put)`, `w_put = Delta_call / (Delta_call - Delta_put)` from initial deltas; "After normalization, these weight allocations remain fixed until expiration", i.e. a single hedge at initiation and no re-hedging (explicitly aligned with Goyal-Saretto 2009, Heston et al. 2023 and Tan et al. 2024).
- **Position signal:** `X_{i,t} in [-1,1]` produced by an LSTM `f_theta(u_{i,t})` (architecture referred to Tan, Roberts & Zohren 2024, "Deep learning for options trading: an end-to-end approach"); long positive, short negative, flat near zero.
- **Portfolio return:** `R^Pi_{t+1} = (1/N_t) * sum_i X_{i,t} * (sigma*/sigma_{i,t}) * R_{i,t+1}` with `R_{i,t+1} = (V_{i,t+1}-V_{i,t})/V_{i,t}`, `V = w_call*C + w_put*P` on closing midpoints, `sigma*` an annualized target volatility, and `sigma_{i,t}` a 20-day exponentially weighted moving standard deviation of straddle returns. Reporting rescales all signals to a 15 percent annualized target (see C4 for the printed realized vols).
- **Input features (five groups):** (1) volatility-normalized returns `R_{t-k,t}/(sigma_{i,t}*sqrt(k))` for `k in {1,5,10,15,20}` trading days; (2) volatility-adjusted MACD signals for `S in {2,4,8}` and `L in {8,16,32}`; (3) Heston option-momentum averages of trailing straddle returns over `n in {1,3,6,12}` months; (4) log-moneyness of the individual put and call plus annualized days-to-expiry; (5) OptionMetrics Greeks of the static straddle: Delta, Gamma, Theta, Vega, Rho.
- **Training objective:** `L(theta) = J(theta) + alpha * ||grad_x V||` with `J = -sqrt(252) * E[R_tilde]/sqrt(Var[R_tilde])`, `R_tilde = X*(sigma*/sigma)*R`. Penalties, all printed as equations:
  - naive `sum |X*Delta|` (equation 9) - evaluated and rejected for signal shrinkage;
  - exposure-normalized `ENP = sum|X*Delta| / (sum|X| + eps)` (equation 10) and `ENP-quad = sum(X*Delta)^2 / (sum X^2 + eps)` (equation 11);
  - drift penalty `DP = sum|X*Delta| / (sum|X*Gamma| + eps)` (equation 12) and `DP-quad = sum(X*Delta)^2 / (sum(X*Gamma)^2 + eps)` (equation 13).
- **Training procedure:** minibatch SGD with Adam; each in-sample window split chronologically 90/10 train/validation, validation used only for early stopping with patience 25 epochs; hyperparameters by random search over 100 candidate configurations; Appendix A grid: minibatch `{32,64,128,256}`, dropout `{0.1..0.5}`, hidden layer `{5,10,20,40,80,160}`, learning rate `1e-5..1e0`, max gradient norm `1e-4..1e1`, risk-aversion `alpha in {1e0,1e1,...,1e7}`; hardware AMD EPYC 7713 plus multiple NVIDIA L40 GPUs.
- **Out-of-sample protocol:** expanding window in five-year increments - each successive training window extends by five years, then "the calibrated model, with all parameters and hyperparameters held fixed, is evaluated on the subsequent five-year period", repeated across "several independently seeded trials" whose OOS results are aggregated. The exact calendar boundaries of every train and test window, the number of seeds and the number of independent models are **not stated in source** (data gap); the words `walk-forward`, `holdout`, `placebo`, `purge`, `embargo` and `deflated` have zero occurrences in the pinned text.
- **Benchmarks:** Long Only (`X=1`); TSMOM in sign form with a 20-day lookback (`X = sign(R_{t-20,t})`, reported as the inverse TSMR); volatility-normalized multi-horizon MACD (reported as MACDMR); Heston option momentum over `n in {1,3,6,12}` months in time-series form (TSHestonMR) and cross-sectional decile form (CSHestonMR). Section 6.1 states "momentum-based strategies were generally unprofitable over the out-of-sample period, we report only the inverse allocation (MR) strategies" and that for the Heston portfolios "we report results for the best performing lookback period for brevity".
- **Rules that are underspecified:** no entry/exit price convention beyond midpoint marking, no order type, no position limit, no capital base, no re-balance cadence other than daily signal change, no tie handling for simultaneous signals, no membership-timing rule for the Nasdaq 100 constituent set, and no rule for the cost level `c` used to train the `TC Reg.` variants (Section 6.4 says only "at a prescribed cost level c"). Any threshold introduced for our own testing is labeled research-proposed / research-defined in the Falsification plan.

## Required data

- **Instrument:** equity options (calls and puts) on Nasdaq 100 Index constituents; standard monthly contracts expiring the third Friday of the following month; near-ATM moneyness `[0.95, 1.05]`.
- **Universe:** "constituents of the Nasdaq 100 Index over the period from January 2010 to December 2023". Whether membership is point-in-time or a single current-constituent list is **not stated in source** - this is a survivorship / look-ahead data gap that must be resolved before any reproduction.
- **Venue / market type:** US listed equity options (exchange and market type are not named beyond OptionMetrics as the vendor); single-market, single-asset-class study.
- **Vendor / fields:** OptionMetrics Ivy DB end-of-day bid and ask quotes, implied volatilities and Greeks. Greeks and IVs are "calculated with a binomial tree model using Cox, Ross, and Rubinstein".
- **Timeframe:** daily marks; monthly portfolio formation; sample window January 2010 - December 2023 (14 years).
- **Additional fields needed but not supplied:** underlying price for moneyness, open interest at formation, corporate-action / special-settlement flags, expiry calendar, point-in-time index membership, dividend and interest-rate inputs for American-style bounds.
- **Timestamp / point-in-time:** no timezone, no clock source, no publication-lag or revision handling is stated; the phrase "point-in-time option features" appears only while describing the earlier Tan et al. 2024 work, not as an assertion about this study's own data assembly.
- **Missing data:** no explicit stale, suspended or partial-print handling; imputation policy not stated.
- **Cost / funding data needs:** not supplied - quoted spread series, commissions, exchange fees and borrow/locate costs are absent from the study design (see Execution assumptions).

## Execution assumptions

Cost and fill treatment was determined from a Methods-level read of Section 4.1 (portfolio formation and returns), Section 5.4 (optimization), Section 5.5 (backtest details) and Section 6.4 (transaction costs and turnover regularization), plus a whole-document term census of the pinned 80,649-character text.

- **Marking and fill model:** daily returns track "the combined value of the constituent options using their closing bid-ask midpoints", an approach the paper states "inherently assumes European-style execution". No crossing of the quoted spread is modelled: `bid-ask` occurs once in the whole document and `spread` occurs zero times.
- **Turnover definition (the only cost model):** `tau_{i,t} = sigma_tgt * |X_{i,t}/sigma_{i,t} - X_{i,t-1}/sigma_{i,t-1}|`; net return `R_tilde = (1/N_t) * sum (X*(sigma*/sigma)*R - c * tau)` with `c` a proportional cost per unit of turnover in basis points, evaluated at `c = 0, 0.5, 1, 2, 3, 4, 5, 10, 20, 50, 100` bps (Table 5). Turnover therefore mixes signal changes with changes in the volatility estimate.
- **Turnover-regularized training:** `TC Reg.` models replace portfolio returns in the training loss with the turnover-adjusted return, so the cost of rebalancing is inside the loss; the prescribed `c` used for training is **not stated in source** (data gap).
- **Modelled cost terms:** `transaction cost` appears 15 times and `turnover` 15 times, all in the Section 6.4 sense of a flat proportional charge. Zero modelled occurrences of: `commission`, `slippage`, `latency`, `borrow`, `assignment`, `leverage`, `participation`. `margin` occurs once and is the word "marginal"; `capacity` occurs once and means model capacity ("the model's capacity to generate meaningful trading signals"); `funding` occurs once and is the arXiv funding footer. All of these are **data gap, never zero**: order type, signal-to-order delay, partial fills, early assignment / exercise handling on American-style contracts, option short locate and borrow, exchange and clearing fees, market impact, position limits, margin and financing costs, and any capacity or participation cap.
- **Hedging:** one delta hedge at formation, no subsequent re-hedging, weights fixed to expiry; no re-hedging cost, no rebalancing of the hedge, no gamma-scalping.
- **Latency / sequencing:** none stated (data gap).
- **Sizing:** equal-weight `1/N_t` across the day's eligible straddles, then volatility-scaled to the target; no capital base, gross exposure cap, Kelly fraction or leverage is stated (data gap).

## Evidence

### Source-reported

All figures below are transcribed from the pinned `arXiv:2609.33767v1` HTML and are **source-reported, not independently reproduced**. Universe and market for all of them: near-ATM monthly straddles on Nasdaq 100 constituent options, January 2010 - December 2023, aggregated out-of-sample results across seeds, equal-weighted and rescaled toward a 15 percent annualized target volatility.

- **Table 1 (out-of-sample performance, no transaction costs), columns E[Return] / Vol / Downside Dev / MDD / Sharpe / Sortino / Calmar / Hit Rate / Ave. P/L:**
  - Long Only `0.100 / 0.161 / 0.088 / 0.340 / 0.621 / 1.129 / 0.294 / 0.447 / 1.390`
  - TSMR `0.132 / 0.161 / 0.086 / 0.311 / 0.822 / 1.537 / 0.426 / 0.449 / 1.431`
  - MACDMR `0.128 / 0.163 / 0.086 / 0.276 / 0.785 / 1.487 / 0.465 / 0.447 / 1.440`
  - TSHestonMR `0.117 / 0.156 / 0.100 / 0.268 / 0.747 / 1.166 / 0.435 / 0.494 / 1.168`
  - CSHestonMR `0.118 / 0.158 / 0.104 / 0.292 / 0.742 / 1.135 / 0.403 / 0.511 / 1.098`
  - Baseline (Sharpe objective only) `0.399 / 0.187 / 0.131 / 0.222 / 2.131 / 3.043 / 1.797 / 0.656 / 1.053`
  - ENP (L1) `0.422 / 0.187 / 0.130 / 0.225 / 2.255 / 3.259 / 1.878 / 0.662 / 1.090`
  - ENP (L2) `0.409 / 0.181 / 0.129 / 0.236 / 2.260 / 3.167 / 1.735 / 0.638 / 1.182`
  - DP (L1) `0.436 / 0.186 / 0.122 / 0.210 / 2.339 / 3.583 / 2.078 / 0.675 / 1.101`
  - DP (L2) `0.425 / 0.188 / 0.131 / 0.246 / 2.255 / 3.236 / 1.724 / 0.681 / 1.012`
  - Section 6.1 prose: benchmarks "deliver annualized Sharpe ratios in the range of 0.621 to 0.822"; Baseline "2.131"; ENP models "2.260"; DP models "the highest Sharpe ratio of 2.339 with the lowest maximum drawdown across all models".
- **Table 2 (net position-normalized Delta, mean / std / min / Q1 / median / Q3 / max):** Long Only `0.023/0.142/-0.465/-0.054/0.024/0.117/0.432`; TSMR `0.011/0.076/-0.234/-0.033/0.002/0.053/0.452`; MACDMR `0.015/0.084/-0.243/-0.033/0.009/0.062/0.464`; TSHestonMR `0.004/0.061/-0.398/-0.023/0.003/0.035/0.206`; CSHestonMR `0.001/0.067/-0.276/-0.038/-0.000/0.037/0.276`; Baseline `0.127/0.107/-0.164/0.035/0.121/0.210/0.421`; ENP (L1) `0.083/0.099/-0.190/0.007/0.062/0.146/0.423`; ENP (L2) `0.089/0.098/-0.169/0.010/0.072/0.153/0.427`; DP (L1) `0.056/0.081/-0.254/-0.000/0.047/0.108/0.397`; DP (L2) `0.101/0.099/-0.188/0.021/0.088/0.167/0.427`. Section 6.2.1: Baseline mean net Delta `0.127` and median `0.121`, "even the first quartile is positive"; regularized means between `0.056` and `0.101`.
- **Table 3 (gross position-normalized Delta, mean / std / min / Q1 / median / Q3 / max):** Long Only `0.218/0.110/0.000/0.133/0.221/0.306/0.484`; TSMR `0.218/0.110/0.000/0.132/0.221/0.306/0.484`; MACDMR `0.201/0.101/0.000/0.128/0.198/0.273/0.486`; TSHestonMR `0.218/0.110/0.000/0.133/0.221/0.306/0.484`; CSHestonMR `0.219/0.113/0.000/0.134/0.221/0.311/0.525`; Baseline `0.256/0.123/0.000/0.159/0.272/0.363/0.479`; ENP (L1) `0.243/0.120/0.000/0.148/0.255/0.343/0.479`; ENP (L2) `0.252/0.123/0.000/0.156/0.267/0.358/0.490`; DP (L1) `0.231/0.116/0.000/0.140/0.238/0.328/0.482`; DP (L2) `0.247/0.121/0.000/0.152/0.262/0.351/0.492`. Section 6.2.2: penalties "act primarily by reducing the baseline model's persistent positive bias ... while only moderately reducing the gross Delta exposure".
- **Table 4 (alpha sweep, `alpha = 1e0 ... 1e7`, Sharpe):** ENP (L1) `1.833, 2.113, 2.231, 2.255, 1.865, 1.070, 0.667, 0.567`; ENP (L2) `2.024, 2.260, 2.107, 2.088, 2.007, 1.794, 1.179, 0.397`; DP (L1) `2.139, 2.161, 2.339, 1.753, 0.935, 0.402, -0.106, 0.129`; DP (L2) `2.255, 1.954, 1.977, 1.865, 0.759, 0.414, -0.294, 0.009`. Section 6.3: the alpha-performance relation is "non-monotonic"; DP (L1) falls from `2.339` at `alpha=1e2` to `0.935` at `alpha=1e4`; DP (L2) falls from `2.255` at `alpha=1e0` to `0.759` at `alpha=1e4`; DP (L1) at `alpha=1e4` "deliver[s] the largest reduction in gross Delta, lowering the mean gross position-normalized Delta by approximately 61 percent, but its Sharpe ratio falls below 1.0"; DP (L1) at `alpha=1e3` gives "approximately 41 percent" gross reduction with Sharpe `1.753`, "below that of the baseline model".
- **Table 5 (Sharpe vs proportional cost, columns 0 / 0.5 / 1 / 2 / 3 / 4 / 5 / 10 / 20 / 50 / 100 bps):** Long Only `0.621 ... 0.496 / 0.372`; TSMR `0.822 ... 0.574 / 0.326`; MACDMR `0.785 ... 0.343 / -0.100`; TSHestonMR `0.747 ... 0.497 / 0.247`; CSHestonMR `0.742 ... 0.587 / 0.431`; Baseline LSTM `2.131, 2.124, 2.117, 2.104, 2.090, 2.076, 2.062, 1.994, 1.859, 1.458, 0.816`; Baseline LSTM + TC Reg. `1.840, 1.835, 1.830, 1.820, 1.810, 1.800, 1.791, 1.742, 1.644, 1.352, 0.871`; ENP (L1) `2.255 ... 1.467 / 0.718`; ENP (L1) + TC Reg. `1.932 ... 1.348 / 0.770`; ENP (L2) `2.260 ... 1.405 / 0.634`; ENP (L2) + TC Reg. `1.788 ... 1.310 / 0.839`; DP (L1) `2.339, 2.331, 2.324, 2.308, 2.292, 2.276, 2.261, 2.182, 2.027, 1.574, 0.860`; DP (L1) + TC Reg. `1.803 ... 1.286 / 0.777`; DP (L2) `2.255 ... 1.491 / 0.763`; DP (L2) + TC Reg. `1.594 ... 1.142 / 0.690`. Section 6.4 prose: "all baseline and regularized models outperform the benchmark models across the entire range of transaction costs"; "DP (L1) remains the best-performing model up to 50 bps, achieving a Sharpe ratio of 1.574"; "At the highest cost level of 100 bps, Baseline LSTM + TC Reg achieves the highest Sharpe ratio of 0.871".
- **Research-computed checks (arithmetic only, from the printed tables, this run):** every row of Table 5 is non-increasing in `c` (15 rows checked); the 100 bps column maximum is `0.871`; Table 1 Baseline `Ave. P/L = 1.053` (the value reused in the Conclusion); best-row gross-Delta reductions versus the Baseline `0.256` are ENP (L1) `(0.256-0.243)/0.256 = 5.08%`, ENP (L2) `1.56%`, DP (L1) `9.77%`, DP (L2) `3.52%`; `+TC Reg` minus plain at 100 bps is `+0.055 / +0.052 / +0.205 / -0.083 / -0.073` for Baseline / ENP (L1) / ENP (L2) / DP (L1) / DP (L2); grid arithmetic `4 penalty families x 8 alpha values = 32 alpha rows` in Table 4 and `11 cost levels` in Table 5 hold. These checks are arithmetic consistency checks of printed values, not a reproduction of the backtest.
- **Reconciliation status:** five internal inconsistencies are recorded as `contradictions` in the frontmatter with `contested: true`.

### Independently reproduced

not independently reproduced

The backtest itself was not rerun: the data are proprietary (OptionMetrics Ivy DB), no code or artefact is published in the pinned source, and no dataset or seed list is disclosed. Only the arithmetic consistency checks listed above were executed.

### Negative evidence

1. No statistical inference accompanies any headline number: zero occurrences of `t-stat`, `p-value`, `confidence interval` or a Diebold-Mariano style comparison; a Baseline-to-DP (L1) Sharpe gain of `2.339 - 2.131 = 0.208` is reported without any dispersion, standard error or significance test.
2. The `+0.208` gain is measured against a Baseline whose own Sharpe of `2.131` is already far outside anything in the rules-based benchmark set (`0.621` to `0.822`), with no decomposition of where that gap comes from.
3. Multiple testing is uncontrolled: 100 random-search hyperparameter configurations, 4 penalty families, 8 alpha values, several seeds, several benchmarks, and a reporting rule that picks "only the best performing model for each regularized variant" - the words `deflated`, `placebo`, `walk-forward`, `holdout` and `multiplicity` do not occur.
4. Benchmark reporting is selected: "momentum-based strategies were generally unprofitable ... we report only the inverse allocation (MR) strategies", and Heston results are "the best performing lookback period ... for brevity". The omitted rows are precisely the rows that would show how weak the benchmark set is.
5. Cost realism: returns are marked at closing midpoints (`bid-ask` appears once, `spread` zero times), so no quoted spread is ever crossed; there are zero occurrences of commission, slippage, latency, borrow, assignment or participation; the only friction is a flat proportional charge in bps on a signal-based turnover definition.
6. The cost ladder is a scalar sweep, not a microstructure model: `c` in `{0..100}` bps per unit turnover, with no per-contract fee schedule, no spread term, no size dependence and no market-impact term, and no stated mapping from `c` to any real option broker's costs.
7. Early assignment and early exercise are unmodelled: the universe screen explicitly drops American-style arbitrage-bound violations, yet returns are computed "inherently assum[ing] European-style execution"; assignment risk, borrow/locate and early-exercise optimality are absent (zero occurrences).
8. Margin, financing and leverage are entirely absent (the single `margin` hit is the word "marginal"), yet short straddles and delta-hedged option books require portfolio margin; returns are therefore not margin-adjusted and no capital base is given, so return-on-capital, Calmar and MDD are not tied to any investable denominator.
9. Nasdaq 100 membership timing is not stated ("constituents of the Nasdaq 100 Index over the period from January 2010 to December 2023"), leaving survivorship and look-ahead risk open on a universe known for heavy index turnover.
10. Exact train/test boundaries are not printed; "expanding window ... with five-year increments" over a 14-year sample cannot be reconstructed unambiguously, so the degree of train/test separation is unverifiable.
11. Seed handling is opaque: "several independently seeded trials" with results "aggregated" - the count of trials, the aggregation rule and any seed dispersion are not reported, so seed selection or averaging cannot be audited.
12. Overlapping daily observations inside a held-open monthly straddle book are serially correlated by construction, and no block bootstrap, HAC correction or effective-sample-size adjustment is reported.
13. The paper's own Table 4 shows the alpha-performance surface is sharply non-monotonic and includes negative Sharpe regions (DP (L1) `-0.106` at `1e6`, DP (L2) `-0.294` at `1e6`), i.e. the mechanism fails under a plausible nearby hyperparameter.
14. The paper's own gross-Delta tables show the hedging claim is mostly a netting effect: best-variant gross reductions are 1.6 to 9.8 percent (research-computed) versus a net-mean reduction of 0.127 to 0.056, and Section 6.2.2 concedes the penalties act "primarily by reducing the baseline model's persistent positive bias".
15. The Conclusion's cross-checkable claims fail against its own tables (contradictions C1, C3), so the narrative layer of the source is not a reliable summary of the numeric layer.
16. No placebo or generic-regularization control: the design never tests the Delta penalty against weight decay or a shuffled-Greek penalty at matched magnitude, so the "hedging inductive bias" interpretation is unidentified.
17. No capacity, liquidity or open-interest-based sizing analysis beyond an `open interest > 0` screen; no participation cap, no book-size or volume-based ceiling.
18. Reproducibility: proprietary OptionMetrics Ivy DB, no code availability statement, no repository, no seeds, no dataset snapshot - the printed Sharpe values cannot be regenerated from public artefacts.
19. Evidence window ends at the December 2023 sample end; nothing after 2023-12-31, no regime breakdown by volatility episode (2020 crash, 2022 rates) and no crisis stress table.
20. Single asset class, single market, single option structure (monthly near-ATM straddles) - no cross-market, cross-expiry or cross-structure replication is reported.
21. Sharpe values above 2 are asserted on a rescaled (vol-targeted) return series while Table 1's realized vols sit between 0.156 and 0.199 against a stated 0.15 target (contradiction C4), and the rescaling rule's ex-ante/ex-post status is unstated.

## Falsification plan

All thresholds below are **research-defined falsification thresholds** (the source states no failure rule for its own claims) and all operational choices introduced here are **research-proposed**. Each gate is evaluated once against frozen parameters; a failed gate cannot be rescued by retuning (`no-retuning rule`).

- **F1 - printed-value reproduction.** Re-derive the Table 1, Table 4 and Table 5 cells for Baseline, ENP (L1/L2), DP (L1/L2) from a pinned rebuild. Threshold: absolute difference <= 0.01 in Sharpe and <= 0.001 in the Delta summary means for every printed cell. Action on failure: mark the corresponding printed value unreproducible and drop it from any downstream claim.
- **F2 - window-disclosure gate.** Obtain exact calendar train/test boundaries and seed count for every reported fold. Action on failure (boundaries not recoverable within one run): treat the out-of-sample label as unverified and stop, i.e. the source's OOS claim is not usable as evidence.
- **F3 - point-in-time universe gate.** Rebuild the universe with point-in-time Nasdaq 100 membership. Threshold: DP (L1) at `alpha=1e2` must still exceed the Baseline Sharpe by at least `+0.10`. Action on failure: conclude the reported penalty gain is partly or wholly a constituent-survivorship artifact.
- **F4 - executable-price gate.** Recompute returns by crossing the quoted spread on both legs at entry and exit (buy the ask, sell the bid) instead of marking at midpoints, plus a per-contract commission schedule. Threshold: net Sharpe at that realistic friction must remain above the Long Only benchmark net Sharpe at the same friction, and the degradation from the mid-based Sharpe must be <= 0.30. Action on failure: reject the tradability of the claim (research-only becomes "not tradable as stated").
- **F5 - cost-ladder realism.** Extend the ladder to `c = 0, 1, 2.5, 5, 10, 20, 50, 100` bps *plus* a fixed per-contract fee term and a spread term. Threshold: the sign of the DP-versus-Baseline ordering must be preserved at every rung <= 20 bps. Action on failure: the "robust to transaction costs" claim fails.
- **F6 - generic-regularization placebo (mechanism-critical).** Train three matched controls with the same alpha grid: (a) L2 weight decay on the output layer, (b) a Delta penalty computed on time-shuffled Delta values, (c) a penalty on a randomly signed Greek. Threshold: DP (L1) must beat the best control by >= `+0.10` out-of-sample Sharpe. Action on failure: conclude the effect is generic regularization or selection, not a Delta-specific hedging inductive bias.
- **F7 - gross-Delta mechanism gate.** Threshold: the chosen penalty must reduce mean gross position-normalized Delta by >= 20 percent versus Baseline while giving up <= 0.20 Sharpe. Action on failure: the "embedded hedging" mechanism reduces to portfolio-level netting, which is what the source's own gross table suggests.
- **F8 - inference gate.** Compute a HAC (Newey-West, automatic lag) t-statistic on the daily out-of-sample return spread of the best regularized model minus Baseline, and a 1000-draw circular-shift placebo on the same spread. Threshold: t >= 2.0 and placebo p < 0.05. Action on failure: treat the incremental gain as statistically indistinguishable from zero.
- **F9 - seed-stability gate.** Rerun with >= 10 fixed seeds and report mean and standard deviation. Threshold: the DP-versus-Baseline gap must exceed one full seed standard deviation and be positive in >= 8 of 10 seeds. Action on failure: treat the headline as initialization luck.
- **F10 - selection/multiplicity gate.** Compute a deflated Sharpe ratio with trial count `N = 100 configs x 4 families x 8 alpha x seeds x reported benchmarks`. Threshold: DSR >= 0.95, and Benjamini-Hochberg `q < 0.10` across the reported family. Action on failure: treat the reported best row as selection-biased and compare only against pre-registered rows.
- **F11 - subperiod and frozen-forward gate.** Split the sample into 2010-2016 and 2017-2023 (research-proposed split at the printed sample window), then run a frozen forward window from 2024-01-01 for 24 months. Threshold: non-negative Sharpe in both subperiods and non-positive forward result = failure of the forward claim. Action on failure: regime-limited conclusion; no extension of the claim past 2023-12-31.
- **F12 - benchmark-completeness gate.** Add an unconditional short-straddle (variance-risk-premium) benchmark, a 20-day TSMOM sign benchmark as printed (including the profitable side, not just the inverse), and the best Heston lookback chosen on training data only. Threshold: the learned model must exceed the best simple benchmark by >= `+0.20` net Sharpe at `c = 5` bps. Action on failure: conclude the alpha is short-vol or simple-timing exposure rather than model skill.
- **F13 - capacity gate (research-proposed).** Cap daily position changes at 20 percent of the contract's daily volume or 10 percent of open interest (whichever binds). Threshold: net Sharpe degradation <= 0.30. Action on failure: classify as capacity-limited and stop.
- **F14 - 2-of-3 cross-market replication.** Rebuild the identical objective on (a) S&P 500 index options, (b) Deribit BTC/ETH monthly options (crypto port), (c) a second equity index option panel. Threshold: at least 2 of 3 must show a positive regularized-minus-baseline gap net of F4 frictions. Action on failure: mark the mechanism asset-class-specific; combined with a negative F6, withdraw the general claim.

## Crypto portability

**adapted** - not `direct`, because the pinned source contains no crypto evidence at all: the entire empirical design is OptionMetrics data on Nasdaq 100 equity options, and the paper never mentions crypto, perpetuals or digital assets.

What transports: the objective `L = negative Sharpe + alpha * scale-free Delta penalty` is instrument-agnostic, and the ENP/DP forms depend only on portfolio Delta and Gamma, which exist on any listed option. Crypto venues (Deribit BTC/ETH options, USDT-perpetual options venues) offer Delta/Gamma directly from the exchange mark model.

What does not port as stated:

- **Contract structure:** the source depends on a dense cross-section of *single-name* near-ATM monthly straddles formed at third-Friday expiries; crypto has at most two liquid underlyings with Friday-dated and daily expiries, so `N_t` collapses and the equal-weight cross-section that drives the Sharpe aggregation disappears.
- **Underlying session:** the source's daily EOD midpoint marks assume a US equity session close; crypto is 24/7, so "closing midpoint", daily return boundaries and the 20-day EWMA volatility estimator need an explicit clock convention.
- **Greeks source:** OptionMetrics CRR-binomial IV/Greeks versus exchange-supplied mark-price Greeks - a model substitution the paper says is allowed in principle but never tests.
- **Frictions:** crypto option bid-ask spreads are far wider than Nasdaq 100 constituent options and there is no listed-guaranteed central counterparty margin grid equivalent; funding, liquidation and mark-price mechanics of the perp leg (if used to hedge instead of the underlying) are unmodeled here.
- **Membership:** no index-constituent universe exists, so the survivorship question in F3 transforms into an instrument-listing/derivability question (which underlyings have listed options at all).
- **Leverage / liquidation:** absent from the source, but first-order in crypto because perp hedging carries liquidation risk.

Crypto performance of the mechanism is **unproven**. This section is a porting hypothesis, not crypto empirical evidence, and crypto portability is not authorization to trade.

## Limitations

- `underspecified`: exact out-of-sample windows, seed count, seed aggregation rule, the cost level used to train `TC Reg.` models, Nasdaq 100 membership timing, timezone and execution convention, capital base, margin model, and the number `N_t` of straddles per formation date.
- `data gap`: PDF checksum (PDF not downloaded), quoted-spread series, commissions and fees, order type, fill model, latency, signal-to-order delay, assignment/early-exercise handling, borrow/locate, market impact, participation, capacity, leverage/margin/financing, code and data availability.
- `not independently reproduced`: every performance number in this record. Only arithmetic consistency checks on printed table values were performed.
- `unproven`: the causal reading that the Delta penalty - rather than generic regularization, hyperparameter selection or seed aggregation - produces the reported `+0.208` Sharpe increment; the source contains no control for that.
- `contested`: five internal contradictions (frontmatter C1-C5) mean the Conclusion cannot be quoted as a summary of the tables.
- Single vendor (OptionMetrics), single index (Nasdaq 100), single structure (monthly near-ATM straddle), single window (2010-2023), no crisis or regime breakdown, no evidence after 2023-12-31.
- The source is a preprint with no stated journal, volume, issue or peer review, so publication status is `not stated in source`.
- Incremental-write note: this record captures a new mechanism family (loss-level risk-sensitivity regularization of an end-to-end option strategy) that no existing record in this repository covers; it is not a reframing of an existing capture.

## Implementation status

`implementation_status: not-implemented`.

Nothing from this record has been implemented in our research stack: no LSTM, no penalty loss, no OptionMetrics ingestion, no option-straddle portfolio construction, no backtest, no Qlib run, no Paper, Testnet or Live activity, and no dependency installation. The only work performed for this capture was reading the pinned primary source, running arithmetic consistency checks on its printed tables, and repository deduplication. No claim of Qlib full-backtest validation, Paper, Testnet or Live verification exists or may be inferred.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

This record being present in the repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. Research capture is not strategy adoption and not permission to run Paper, Testnet or Live. Any later adoption decision must be explicit, separately reviewed, and based on this record plus current sources.

## Related Wiki records

Read-only Wiki Brain search on 2026-09-29 (`option straddle delta hedging deep learning options trading`, 4 hits; `spatio-temporal momentum Zohren Roberts end-to-end neural network strategy`, 0 hits) returned these verified adjacent pages, which are linked without any page being written:

- [[quant/transformer-ddqn-straddle-option-volatility-trading-2026-09-05]] - straddle volatility trading, but source `arXiv:2509.07987` and a Transformer-DDQN reinforcement-learning signal, not a loss-level Delta penalty; different source identity and different mechanism.
- [[quant/spy-options-svi-surface-rv-falsification-adverse-selection-2026-09-12]] - option relative value with an explicit adverse-selection boundary; different mechanism (surface fitting) and different evidence class.
- [[quant/single-name-equity-earnings-iv-crush-bid-ask-falsification-2026-09-13]] - short-straddle event selling that fails after quoted-spread and commission friction; useful contrast on the cost realism gate F4.

No stable Wiki Brain page was found for the same-author earlier paper (`spatio-temporal-momentum-multitask-shrinkage-turnover-regularization-2026-09-06`, source `arXiv:2302.10175`), so it is referenced by filename only and not linked as a Wiki page. `kb_search` was used read-only; no Wiki Brain page was created, updated or deleted by this run.

## Sources

1. Wee Ling Tan, Stephen Roberts, Stefan Zohren. "Taming the Greeks: Option Portfolios with Inductive Biases." arXiv preprint `arXiv:2609.33767v1 [q-fin.PM]`, submitted 27 Sep 2026 17:05:50 UTC. Abstract page: https://arxiv.org/abs/2609.33767
2. Full text (HTML v1), read end to end 2026-09-29: https://arxiv.org/html/2609.33767v1 - provenance for Sections 1-8, equations (1)-(17), Tables 1-6, Figures 1-9, Appendices A-B and the 34-item reference list.
3. DOI: https://doi.org/10.48550/arXiv.2609.33767 (arXiv-issued via DataCite, pending registration).
4. Data dependency cited by the source: OptionMetrics Ivy DB (proprietary end-of-day option quotes, implied volatilities and Greeks) - not redistributable, no public artefact.
