---
schema: strategy-research-record-v1
title: "Bitcoin Rolling FPCA One-Step-Ahead Hourly Return-Direction Forecast"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - fpca
  - intraday
  - forecasting
status: research-only
confidence: medium
source_as_of: 2026-03-07
sources:
  - "https://doi.org/10.1002/for.70127"
  - "https://arxiv.org/abs/2505.20508"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The final publisher text is internally inconsistent about the 200-forecast rolling-FPCA start date: Section 4.2 states 2019-02-07, while the final-version Table 4 note states 2019-02-27; arXiv v1 states 2019-02-07."
---

# Bitcoin Rolling FPCA One-Step-Ahead Hourly Return-Direction Forecast

## Provenance

Primary source: Joann Jasiak and Cheng Zhong, *Intraday Functional PCA Forecasting of Cryptocurrency Returns*, **Journal of Forecasting** 45(5), 2186-2212, first published 2026-03-07, DOI `10.1002/for.70127`.

Preprint provenance: arXiv `2505.20508v1`, submitted 2025-05-26. The preprint is useful because its HTML preserves several parameter values that are not rendered cleanly in the final publisher HTML. Where the preprint and final article differ, this record attributes the version explicitly rather than merging the values.

The final article studies two related but distinct forecasting exercises. Its daily-function analysis uses Bitstamp BTC prices from 2022-01-01 through 2023-12-30. The strategy hypothesis captured here instead concerns Section 4's **rolling FPCA, one-hour-ahead Bitcoin return forecast**, evaluated on 200 hourly forecasts in a 2019 out-of-sample comparison window. The final article states that this 2019 window matches subsample 5 of Gradojevic et al. (2023), but the reviewed publisher text does not clearly restate the venue/data-vendor identity for that separate 2019 exercise. That venue provenance is therefore a **data gap** and must not be silently inferred from the 2022-2023 Bitstamp sample.

Repository and Wiki Brain source-identity checks found no existing record containing DOI `10.1002/for.70127`, arXiv `2505.20508`, the exact paper title, rolling FPCA, Karhunen-Loève eigenscore regression, or materially equivalent overlapping-24-hour functional-return signal construction. This is therefore a new source/mechanism capture rather than a reframing of an existing record.

## Economic mechanism

### Source-reported

The authors exploit the fact that Bitcoin trades continuously. A UTC "day" is only a conventional partition, so a sequence of 24-hour return functions can be shifted by one hour to create highly overlapping functional observations. Their rolling FPCA method decomposes a set of completed 24-hour return functions and a one-hour-shifted auxiliary set into functional principal components, then learns a mapping from the shifted-function eigenscores to the target-function eigenscores. The mapped eigenscores reconstruct the next one-hour return forecast.

The paper's empirical rationale is therefore statistical rather than a claimed structural risk premium: persistent intraday functional shape and covariance structure in overlapping 24-hour Bitcoin return trajectories may contain information about the next hourly return. At a one-hour horizon, the source notes that the two functional windows overlap in 23 of 24 hourly returns, so their eigenscores are especially closely related; explanatory power deteriorates as the forecast horizon increases and the overlap shrinks.

### Research interpretation

The falsifiable alpha hypothesis is that the **shape of the most recent 24-hour Bitcoin return path**, represented in a rolling functional-principal-component basis, contains short-horizon directional information not captured by an unconditional mean or simple discrete-time baseline.

This should not be interpreted as proof of a durable economic anomaly. Because adjacent 24-hour functions overlap heavily, the signal may partly exploit short-memory return dependence, intraday seasonality, volatility clustering, or mechanical overlap rather than a distinct source of alpha. Those competing explanations require explicit controls.

## Signal

### Source-reported forecasting construction

For one-hour-ahead forecasting (`k = 1`), the source constructs two aligned families of 24-hour hourly-return functions:

1. `X_i(t)`, `t = 1,...,24`: completed target 24-hour functions for historical observations.
2. `X_i^+(s)`, `s = 0,...,23`: auxiliary 24-hour functions shifted one hour behind the target functions. For `k = 1`, the two functions share 23 hourly returns.
3. Demean the auxiliary functions using their point-in-time sample mean and separately demean the target functions using their own sample mean.
4. Perform FPCA separately on the auxiliary and target function sets. Let `alpha_i` denote auxiliary eigenscores and `beta_i` target eigenscores.
5. For each retained target eigenscore, regress historical `beta` scores on the matrix of historical `alpha` scores. The paper evaluates OLS, Ridge, LASSO, SVM, random forest, and neural-network estimators for this mapping.
6. Use the current auxiliary eigenscore vector and the fitted mapping to predict the target eigenscores.
7. Reconstruct the target return function from predicted target eigenscores, target eigenfunctions, and the target mean function. Evaluate the reconstructed function at the next hourly point to obtain the one-hour-ahead BTC return forecast.

The arXiv v1 explicitly reports trying initialization windows of **90 to 110 daily functions** and selecting the number that maximizes in-sample correct-sign rate. The final publisher version likewise states that the number of past functions is selected to maximize in-sample sign accuracy, but its rendered HTML does not preserve the exact tested range. Treat `[90,110]` as **arXiv-v1-specific source-reported detail**, not silently as a guaranteed final-version parameter.

The exact retained FPCA dimension `J` for the rolling 2019 exercise is **underspecified** in the reviewed Section 4 text. The paper gives cumulative-variance rules and dimensions for its separate 2022-2023 daily-function exercise, but this record does not assume those values transfer unchanged to the rolling 2019 experiment.

### Research-proposed trading operationalization

The source is a forecasting paper and does **not** specify an executable trading strategy. The following is **research-proposed**, solely to make the alpha implication testable:

- **Formation timestamp:** immediately after an hourly BTC return becomes fully observable at a UTC hourly boundary, using only observations timestamped at or before that boundary.
- **Model fitting:** recompute the rolling FPCA bases, score mapping, and any window/model selection using training data strictly prior to the forecasted hour. No test-hour label may influence the selection of window length, `J`, regularization, or estimator.
- **Primary variant:** use the LASSO eigenscore mapping because the source reports the highest directional accuracy among the final-version Table 4 estimators; any comparison with Ridge/RF/SVM must be predeclared rather than selected after seeing test PnL.
- **Long entry:** if forecast next-hour return `r_hat > 0`, take +1 unit BTC directional exposure at the first executable price after signal computation.
- **Short entry:** if `r_hat < 0`, take -1 unit BTC directional exposure at the first executable price after signal computation.
- **Tie:** if `r_hat = 0`, remain flat.
- **Exit / holding:** close at the end of the forecasted one-hour interval; no overlapping position is carried beyond its own one-hour forecast horizon.
- **Sizing:** constant unit/notional exposure for the research test. No volatility targeting, leverage rule, stop, take-profit, or confidence threshold is source-reported.

All of the trading rules in this subsection are **research-proposed** and must never be cited as rules from Jasiak and Zhong.

## Required data

- **Instrument:** Bitcoin price series sufficient to calculate consecutive hourly log returns.
- **Source study market/venue:** the final article's 2022-2023 functional-data exercise uses Bitstamp. The exact venue/data-vendor identity of the separate 2019 rolling-FPCA exercise is not clearly restated in the reviewed Section 4 text: **data gap**.
- **Timeframe:** one-hour observations for the captured hypothesis; continuous 24/7 coverage.
- **Fields:** timestamp and tradable/reference price sufficient for hourly return calculation. A later trading reproduction also requires executable bid/ask or equivalent spread/slippage inputs.
- **Functional construction:** rolling 24-hour sequences aligned to UTC hourly boundaries, including shifted auxiliary sequences.
- **Point-in-time requirement:** only returns fully observed by each forecast timestamp may enter the auxiliary function, FPCA estimation, coefficient fitting, tuning, and normalization.
- **Selection-state requirement:** the chosen lookback/window, FPCA dimension, and regression hyperparameters must be learned from training data only and frozen for each out-of-sample prediction until the next predeclared refit.
- **Missing data:** source treatment for missing/stale exchange observations is **underspecified**. Research reproduction should fail the affected window rather than silently impute unless a predeclared imputation method is separately justified.
- **Costs:** fees, bid-ask spread, slippage, latency and market impact are required for any trading interpretation but are not part of the source's forecasting evidence.

## Execution assumptions

The source evaluates statistical return forecasts; it does not report market/limit order type, fill model, latency, leverage, margin, position size, spread, slippage, market impact, funding, borrow cost, or failure handling.

For the **research-proposed** directional translation, use the first executable price after model output is available, not the same price that closes the input bar if the forecast could not have been computed before that price. Record actual signal-computation delay and stress one-bar-boundary latency. For perpetual-futures implementation research, funding and taker/maker fees must be included; for spot-short research, borrow availability and borrow cost must be included. No assumption here authorizes execution.

## Evidence

### Source-reported

The peer-reviewed final article reports 200 one-hour-ahead Bitcoin return forecasts for the rolling-FPCA comparison exercise. Final-version Table 4 reports directional sign accuracy of **59.5% OLS, 60.5% Ridge OLS, 62% LASSO OLS, 57% SVM, 58.5% random forest, and 53.5% neural network**. The paper states that LASSO provides the best forecast-sign rate in that table and that its sign accuracy differs statistically from several alternatives in McNemar comparisons.

The arXiv v1 reports a slightly different earlier Table 4 for 200 hourly forecasts starting 2019-02-07: **59.0% OLS, 62.5% Ridge, 63% LASSO, 57.5% SVM, 60.5% random forest, and 53.5% neural network**. These values are preserved as version-specific evidence, not merged with the final journal values.

The final article also concludes that the rolling FPCA approach compares favorably with the literature benchmark for one-step-ahead hourly Bitcoin forecasting. This is forecast evidence only: neither version reports net trading PnL for the research-proposed long/short rule above.

### Independently reproduced

not independently reproduced

### Negative evidence

- The source selects the number of past daily functions based on in-sample correct-sign rate. Without a nested or strictly rolling selection protocol, this introduces a material model-selection/overfitting risk for a trading interpretation.
- The source's strongest directional result is based on only 200 hourly forecasts, so sampling error and regime dependence are material concerns.
- The final journal and arXiv v1 versions report somewhat different Table 4 values. In addition, the final publisher text is internally inconsistent about the rolling-FPCA start date: Section 4.2 states 2019-02-07, while the Table 4 note states 2019-02-27; arXiv v1 states 2019-02-07.
- The 23-of-24-hour overlap at `k=1` may allow the model to exploit short-memory dependence or time-of-day structure rather than a durable independent alpha mechanism.
- No transaction-cost, spread, latency, funding, borrow, capacity, or executable-PnL evidence is provided for the directional trading translation.

## Falsification

1. **Modern walk-forward directional test.** Use point-in-time BTC hourly data with nested training-only selection of window length, `J`, and regression hyperparameters. **research-defined falsification threshold:** reject the directional-alpha hypothesis if out-of-sample sign accuracy is `<= 50%` over the predeclared test sample. Action: retain the method only as a forecasting/risk research artifact, not as directional alpha.
2. **Benchmark incremental-value test.** Compare against unconditional-sign, AR(1)/random-walk-return, simple last-hour momentum/reversal, and UTC-hour seasonality controls on the identical timestamps. **research-defined falsification threshold:** reject incremental FPCA value if the FPCA forecast does not improve a predeclared directional loss metric over the best simple baseline, or if a paired directional-accuracy test fails to reject equal performance at the 5% level. Action: attribute any apparent edge to the simpler baseline mechanism.
3. **Leakage/model-selection audit.** Reproduce every prediction using only state available before the forecasted hour. **research-defined falsification threshold:** any forecast whose selected window, `J`, normalization, basis, or regression hyperparameter uses future/test labels invalidates that result. Action: discard contaminated results and rerun from a clean temporal split.
4. **Cost-aware trading translation.** Apply the research-proposed one-hour long/short rule with observed/realistic fee, spread, slippage, funding or borrow, and signal-computation delay. **research-defined falsification threshold:** reject the tradable-alpha translation if mean net return per position is `<= 0` or aggregate net PnL is non-positive over the locked out-of-sample test. Action: do not progress the trade mapping.
5. **Overlap / competing-explanation ablation.** Control for last-hour return, 24-hour return, realized volatility, and UTC hour-of-day; compare against models using the same raw lagged returns without FPCA. **research-defined falsification threshold:** if FPCA loses all incremental predictive improvement after these controls, reject the claim that functional decomposition itself adds information.
6. **Horizon perturbation.** Predeclare `k = 1, 2, 4, 8` hour forecasts without retuning to each test result. The source expects explanatory power to weaken as overlap decreases. A flat or erratic profile is not automatically failure, but reversal of the one-hour result together with failure of the `k=1` modern OOS test materially weakens the mechanism.
7. **Venue robustness.** Where data permit, repeat on at least one major crypto venue distinct from the source-data reconstruction. **research-defined falsification threshold:** if the one-hour signal is positive only on a single venue and disappears after common timestamp/cost normalization, classify portability as venue-specific/unproven rather than market-wide.

## Crypto portability

**direct** for the empirical forecasting mechanism because the cited source studies Bitcoin itself and explicitly designs the rolling functional construction for continuously traded 24/7 data.

The **trading** translation remains unproven. Porting the forecast from the source price series to Binance spot or perpetual futures introduces venue fragmentation, mark/index versus trade-price differences, funding, fee tiers, bid-ask spread, latency, contract specification, and possible basis effects. UTC hourly boundaries must be defined identically; a venue's candle-close timestamp must not be treated as executable before the underlying final trade is known.

## Limitations

- **underspecified:** exact FPCA dimension `J` used in the rolling 2019 exercise is not unambiguously stated in the reviewed Section 4 text.
- **data gap:** the final publisher text does not clearly restate the venue/data-vendor identity for the separate 2019 rolling-FPCA exercise, so it must not be inferred from the 2022-2023 Bitstamp sample without further provenance.
- **version sensitivity / source inconsistency:** arXiv v1 and the final journal article report different Table 4 values, and the final publisher text itself gives conflicting 2019-02-07 versus 2019-02-27 start dates. Replication must pin the source version and independently resolve the intended timestamp range.
- **selection bias risk:** source window length is selected by in-sample sign performance; a modern alpha test requires nested/walk-forward selection.
- **small evaluation sample:** 200 hourly forecasts are insufficient to infer durability across market regimes.
- **forecast-versus-trade gap:** sign accuracy is not net profitability; the source does not provide an executable trading rule or costs.
- **not independently reproduced:** no local data/code reproduction was performed in this Scout cycle.

## Implementation status

`not-implemented`. This Scout cycle normalized public research only. No PyBroker family, Nautilus strategy, data pipeline, model training job, backtest, Paper, Testnet, Demo, or Live component was created or modified.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. It is evidence for a falsifiable research hypothesis, not evidence that a profitable tradable strategy exists. Presence in the Alpha Strategy Pool does not authorize implementation, historical validation, paper trading, testnet/demo trading, or live execution.

## Related Wiki records

No materially equivalent rolling-FPCA / functional-eigenscore Bitcoin strategy-research record was found in the pre-write Wiki Brain search.

Relevant validation context already present in Wiki Brain:

- [[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]] — relevant to temporal leakage and overlapping-label validation if the forecast is later tested as a trading hypothesis.

## Sources

1. Jasiak, J., & Zhong, C. (2026). *Intraday Functional PCA Forecasting of Cryptocurrency Returns*. **Journal of Forecasting**, 45(5), 2186-2212. First published 2026-03-07. DOI: https://doi.org/10.1002/for.70127 . Primary final-version sections used: Section 4.1 rolling FPCA algorithm; Section 4.2 application to hourly Bitcoin returns; Tables 4-6; Section 4.3 horizon effect; Data Availability Statement.
2. Jasiak, J., & Zhong, C. (2025). *Intraday Functional PCA Forecasting of Cryptocurrency Returns*. arXiv:2505.20508v1, submitted 2025-05-26: https://arxiv.org/abs/2505.20508 . Used for version-specific reconstruction of the `[90,110]` initialization-window range and the v1 Table 4 values.
