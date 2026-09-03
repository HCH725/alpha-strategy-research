---
schema: strategy-research-record-v1
title: Crypto Regime-Dependent Distress Microstructure Next-Quarter Risk
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - distress
  - regime
  - volatility
  - liquidity
  - momentum
  - cross-sectional
status: research-only
confidence: medium
source_as_of: 2026-08-07
sources:
  - https://doi.org/10.3390/jrfm19080599
  - https://www.mdpi.com/1911-8074/19/8/599
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Regime-Dependent Distress Microstructure Next-Quarter Risk

## Provenance

Primary source: Huda Aldhahi and Abdulrahman Alsamaani, “Regime-Dependent Predictability of Cryptocurrency Distress: Cross-Sectional Evidence from Two Exchanges,” *Journal of Risk and Financial Management* 19(8), 599, published 2026-08-07, DOI `10.3390/jrfm19080599`.

Primary Kraken sample: daily market data for 609 USD-quoted cryptocurrencies, with a survivorship-inclusive coin-quarter panel spanning the usable 2017–2025 estimation period from exchange history beginning in 2013. Cross-exchange robustness: 79 currently listed Binance USDT pairs, 2017–2026, explicitly survivorship-biased by construction.

Source-identity deduplication was performed across this repository before writing. No record matched the DOI, exact paper title, the 609-coin Kraken distress-onset design, or the distinctive mechanism of coin-level microstructure distress scores whose predictive mapping weakens or can invert under high market-wide volatility. This record is therefore source-distinct and mechanism-distinct at the pool level.

The source is a predictive empirical study, not a trading-strategy backtest. This record preserves that boundary. Any portfolio construction below that is not explicitly in the paper is labeled `research-proposed`.

## Economic mechanism

### Source-reported

The authors report that next-quarter onset of severe, sustained cryptocurrency distress is predictable on average from lagged coin-level market characteristics: higher realized volatility, lower liquidity, weaker momentum, and younger asset age are associated with greater distress risk. The central finding is not that this mapping is stable. Its predictive reliability depends on the contemporaneous market-wide volatility regime.

In turbulent market regimes, the cross-sectional relationship between coin-level signals and subsequent distress weakens materially. The paper reports that some signal channels can become locally inverted in weak out-of-sample years. The authors test a natural explanation—higher cross-coin co-movement compressing useful cross-sectional dispersion in turbulent periods—but do not find support for that mechanism.

### Research interpretation

The falsifiable alpha/risk hypothesis is a **regime-conditioned cross-sectional distress-risk effect**: a composite of lagged realized volatility, liquidity, momentum, volume trend, and age may help rank coins by next-quarter severe-distress risk in calmer regimes, but a static mapping should not be trusted when market-wide volatility is elevated.

For alpha research, the useful implication is asymmetric. A static “short the highest predicted distress-risk coins” rule is not supported by the source because prediction can deteriorate to chance or worse in stressed regimes. A more defensible test is whether **regime-gated avoidance, underweighting, or short-bias** against high predicted distress risk adds value only when the model’s contemporaneous regime is within a historically reliable zone. Any such portfolio rule is `research-proposed`, not source-reported.

The economic channel remains partially unresolved. Liquidity deterioration, weak momentum, high idiosyncratic/realized risk, and asset youth plausibly proxy fragility or limited investor support, but the paper establishes predictive association rather than causality.

## Signal

### Source-reported predictive construction

**Unit and formation timestamp**

- Observation unit: coin-quarter `(i, q)`.
- Predictors are formed from daily market data available through the end of calendar quarter `q`.
- Outcome: distress onset in quarter `q+1`.
- This lag structure is intended to avoid contemporaneous feedback and look-ahead.
- Exact exchange timezone / quarter-close timestamp convention is `underspecified` in the reviewed source text and must be fixed before replication.

**Universe / at-risk set**

A coin-quarter is eligible when the coin is currently non-distressed, has at least 30 genuinely traded days in the quarter, and the coin has at least 90 days of observed history. Returns are computed only on days with positive volume and at least one trade. Heavy-tailed predictors are winsorized at the 1st and 99th percentiles.

**Predictors**

1. `RVol(i,q)`: annualized standard deviation of daily log returns in quarter `q`, annualized with `sqrt(365)`.
2. `LDVol(i,q)`: log of average daily dollar trading volume in quarter `q`.
3. `Ret(i,q)`: compounded quarterly return.
4. `VTrend(i,q)`: quarter-over-quarter first difference in log average daily dollar volume.
5. `Age(i,q)`: days since first observed trade as of quarter-end.

The baseline pooled panel logit standardizes the coin-level predictors and estimates next-quarter distress-onset probability with year fixed effects in the in-sample specification.

**Distress definition**

- Trailing peak: maximum closing price over the prior 365 calendar days including the current day as specified by the paper’s trailing window notation.
- Drawdown: current close divided by trailing peak minus one.
- Primary distress threshold: `theta = 0.70`.
- A quarter is distressed when drawdown reaches at least `-70%` at some point during the quarter **and** remains at or below `-70%` at quarter-end.
- Distress onset occurs when the current quarter becomes distressed and the immediately prior quarter was not distressed.
- Robustness thresholds reported by the source: `theta in {0.60, 0.80}`.

**Market-wide volatility regime**

The paper defines quarterly market-wide volatility as the cross-sectional mean of qualifying coins’ realized volatility and standardizes it across quarters. The interaction model augments the baseline with market-wide volatility and interactions between the coin-level predictors and the regime variable.

**Source model output**

The output is a next-quarter distress probability / risk score, not an explicit executable long-short order.

### Research-proposed operationalization for falsifiable trading research

The following is **not source-reported**:

- `research-proposed`: at each quarter-end, estimate the model strictly using only data available before that formation timestamp, score the current at-risk universe, and rank coins by predicted next-quarter distress probability.
- `research-proposed`: test high-risk-minus-low-risk cross-sectional return spreads and an investable long-low-risk / short-high-risk portfolio, but only where historical shortability and borrow/funding are point-in-time available.
- `research-proposed`: add a regime gate that suppresses or neutralizes the distress trade when current market-wide volatility is in a high-volatility state.
- `research-proposed`: do not hard-code the paper’s descriptive suggestion of a 75th–80th percentile caution zone as a source-validated trading threshold; any percentile gate must be selected in training data only and treated as a tunable research parameter.
- `research-proposed`: rebalance quarterly at the first executable timestamp after all quarter-end inputs are complete; same-quarter-close fills are forbidden unless independently proven feasible without look-ahead.
- `research-proposed`: maximum holding period one quarter, with no overlapping re-entry for a coin already held from the immediately prior rebalance unless the portfolio specification explicitly permits it.

Signal status: **partially specified for predictive replication; underspecified as an executable trading strategy**.

## Required data

- **Instrument:** cryptocurrency spot markets for the source replication. Kraken primary sample uses USD-quoted coins; Binance robustness uses USDT-quoted spot pairs.
- **Universe:** point-in-time exchange listing history, including inactive/delisted coins for a survivorship-inclusive primary replication. A currently listed-only universe is not equivalent.
- **Venue:** Kraken for primary replication; Binance for cross-exchange robustness.
- **Timeframe:** daily OHLCV and trade-count data aggregated to calendar quarters.
- **Fields:** daily close, traded volume, trade count, first observed trade timestamp, point-in-time listing/inactivity status, and quote-currency conversion sufficient to construct dollar volume.
- **Derived fields:** daily log return, quarterly realized volatility, log average daily dollar volume, quarterly compounded return, quarter-over-quarter volume trend, age, 365-day trailing peak, drawdown, distress state, distress onset, and cross-sectional market-wide volatility.
- **Point-in-time:** delisted/inactive histories must remain visible; current-listing reconstruction alone creates survivorship bias. Predictor winsorization, standardization, model fitting, and regime normalization must use training information only in prospective tests.
- **Timestamp:** exact Kraken/Binance daily-bar timezone and quarter-end clock convention are a `data gap` in the reviewed source text; replication must explicitly pin them before testing.
- **Missing data:** retain only genuinely traded days; require at least 30 traded days per coin-quarter and at least 90 days of coin history as source-reported. No additional imputation is authorized.
- **Funding/fee/spread needs:** not required to reproduce predictive AUC, but mandatory for any `research-proposed` long-short implementation. Historical maker/taker fees, bid-ask spreads, borrow/short availability, funding if perpetuals are substituted, slippage, impact, and delisting-exit assumptions are required.

## Execution assumptions

The source does not report an investable portfolio execution protocol. Order type, signal-to-order delay, fill price, spread, slippage, market impact, participation cap, position limits, short borrow, leverage, liquidation treatment, and portfolio transaction costs are therefore `underspecified` for trading use.

For any future test:

- `research-proposed`: signal formation completes only after the final daily data for quarter `q` are known and validated.
- `research-proposed`: earliest eligible fill is the first liquid observation after signal completion.
- `research-proposed`: delisting or trading suspension must be handled with point-in-time executable exit logic, not a convenient final database price.
- `research-proposed`: spot short tests require actual historical borrow availability; perpetual substitution changes the instrument and introduces funding, mark/index, basis, and liquidation dependencies.
- `research-proposed`: capacity must be capped by contemporaneous depth/volume rather than by present-day liquidity.

No source-reported trading return should be inferred from the predictive statistics.

## Evidence

### Source-reported

Primary sample and model evidence from Aldhahi and Alsamaani (2026), DOI `10.3390/jrfm19080599`:

- The final Kraken at-risk sample contains about 2,579–2,580 coin-quarters from 609 cryptocurrencies, with 529 next-quarter distress-onset events, approximately 20.5% of observations.
- Coin-stratified five-fold out-of-sample ROC AUC is about `0.678` on Kraken.
- The baseline model reports a one-standard-deviation increase in realized volatility associated with distress odds about `2.48x` as large (`p < 0.001`). Stronger quarterly momentum is associated with lower distress odds (odds ratio about `0.75`, `p = 0.001`), and older age is protective (per-year odds ratio about `0.83`, `p < 0.001`). The reported volume-trend odds ratio is about `1.17` (`p = 0.029`).
- Rolling-origin prospective ROC AUC is highly unstable: approximately `0.79` in 2022 and `0.71` in 2023, versus `0.45` in 2021 and `0.43` in 2024; the source reports a mean around `0.605` across five test years.
- In the regime-interaction model, the aggregate regime dependence is strongly significant. The source reports a robust negative volume interaction (about `-0.21`, bootstrap `p = 0.002`) and a robust positive momentum interaction (about `+0.18`, bootstrap `p < 0.001`) in the Kraken analysis; individual channels are specification-sensitive.
- The proposed co-movement explanation is not supported: across 34 qualifying quarters, the source reports Pearson `r = 0.08` (`p = 0.64`) and Spearman `rho = -0.02` (`p = 0.93`) between average cross-coin correlation and the volatility regime.
- Cross-exchange replication on 79 Binance USDT coins reports cross-validated AUC around `0.652` versus `0.678` on Kraken, with aggregate regime dependence again significant (`likelihood-ratio p = 3.4e-6` on Binance versus `9.1e-5` on Kraken). The source explicitly notes that the significant individual interaction channels differ by exchange.
- Robustness checks cover alternative distress thresholds, alternative regime proxies, alternative frequencies, inference methods, and a second exchange. The paper reports cross-validated AUC broadly in the `0.665–0.719` range across specifications.

These are source-reported empirical results. They are not independently verified in this Scout cycle and are not evidence of net trading profitability.

### Independently reproduced

not independently reproduced

### Negative evidence

The source provides unusually important negative evidence:

- Prospective performance can be worse than chance in specific years (`AUC 0.43–0.45`), so a static distress model is not reliably portable across regimes.
- In 2024, precision–recall performance reportedly falls below the event-rate baseline and Brier score is worse than the null forecast, reinforcing that the failure is not only a ROC-AUC artifact.
- Individual interaction channels are not stable across Kraken and Binance even though the aggregate regime-dependence result persists.
- The tested co-movement mechanism is rejected; the economic cause of the regime instability remains unresolved.
- Binance replication is based on currently listed pairs and is survivorship-biased by design.
- Exchange-level distress is not global asset extinction; a coin can be impaired or inactive on one venue while trading elsewhere.
- The study establishes predictive association, not causality. Project failure, security incidents, regulation, token design, or omitted fundamentals may jointly drive predictors and distress.
- Quarterly aggregation coarsens event timing and may be too slow for some practical risk applications.

## Falsification plan

1. **Strict post-source out-of-sample test**
   - Data: point-in-time Kraken and at least one independent liquid venue after the source’s effective sample end.
   - Sample: no overlap with model-selection or threshold-selection data; use a forward period of at least 8 completed quarters where available.
   - Metric: rolling-origin ROC AUC, PR AUC, Brier score, calibration slope, and realized high-minus-low risk return spread.
   - `research-defined falsification threshold`: reject the portable predictive hypothesis if pooled forward ROC AUC is `<= 0.52` **or** PR AUC fails to exceed the contemporaneous event-rate baseline in at least 75% of completed forward quarters.
   - Action: no strategy promotion; retain only as historical/negative evidence.

2. **Regime-dependence replication**
   - Data: same point-in-time universe and source-equivalent predictors.
   - Regimes: rolling market-wide realized-volatility percentile computed from training history only.
   - Metric: interaction likelihood-ratio test plus calm-vs-turbulent OOS AUC difference.
   - `research-defined falsification threshold`: weaken/reject the regime-conditioning thesis if interaction terms are jointly insignificant at `p >= 0.10` **and** turbulent-regime AUC is not at least `0.05` lower than calm-regime AUC across two independent venues.

3. **Leakage and survivorship audit**
   - Data: full listing/delisting history, point-in-time availability timestamps, historical symbol mappings.
   - Metric: compare survivorship-inclusive versus current-listing-only estimates.
   - `research-defined falsification threshold`: reject investable interpretation if the high-vs-low distress ranking changes sign or more than half of the apparent spread disappears after point-in-time universe reconstruction.

4. **Parameter perturbation**
   - Vary distress threshold across at least `60%`, `70%`, and `80%`; trailing-peak lookback around the source’s 365-day choice; winsorization boundaries; minimum trading-day filter; and quarterly versus monthly aggregation.
   - `research-defined falsification threshold`: reject robustness if the predictive rank ordering or regime direction changes sign in more than one-third of reasonable neighboring specifications.

5. **Placebo / shuffled-label test**
   - Shuffle next-quarter onset labels within time blocks while preserving cross-sectional event rates.
   - Metric: OOS AUC distribution and interaction test statistic.
   - `research-defined falsification threshold`: fail if real-model OOS AUC or regime-interaction statistic does not exceed the 95th percentile of the placebo distribution.

6. **Competing-explanation controls**
   - Add point-in-time security incidents, delisting notices, token unlocks, market-cap/size, broad-market return, and available project-fundamental controls where public history exists.
   - `research-defined falsification threshold`: materially weaken the mechanism if the source-style microstructure composite loses incremental OOS ranking value after these controls.

7. **Trading-cost and fillability stress for any portfolio adaptation**
   - Include historical shortability/borrow or perpetual funding, fees, spread, slippage, impact, suspension/delisting exits, and at least one-bar signal delay.
   - `research-defined falsification threshold`: reject the trading adaptation if net high-risk-minus-low-risk performance is non-positive after conservative executable costs, even if predictive AUC remains above chance.

8. **Regime-gate ablation**
   - Compare static distress ranking with a training-only volatility-regime gate.
   - `research-defined falsification threshold`: reject the gate as value-adding if it does not improve at least two of OOS drawdown, calibration, PR AUC, or net return without materially reducing usable sample coverage.

## Crypto portability

**Portability: direct for the predictive hypothesis; unproven for an executable alpha strategy.**

The evidence is natively cryptocurrency-based and is replicated across Kraken USD and Binance USDT spot markets, so the distress-predictability mechanism itself is directly crypto-relevant. However, an investable long-short translation is not source-validated.

Crypto-specific risks include:

- 24/7 quarter-boundary and daily-bar timestamp definitions can change predictor values.
- Exchange fragmentation means venue-specific distress need not equal global distress.
- Delisting, suspension, stale quotes, and thin books make short-side backtests especially vulnerable to non-executable prices.
- Spot shorting can be impossible or expensive exactly for the highest-risk coins.
- Perpetual substitution introduces funding, basis, mark/index, liquidation, and contract-availability biases.
- USDT versus USD quote regimes may change measured dollar volume and liquidity relationships.
- Listing/survivorship reconstruction is critical because failed coins are economically central to the hypothesis.
- Token redenominations, migrations, forks, and symbol reuse require point-in-time identity mapping.

## Limitations

- The paper is a predictive distress study, not a source-validated trading strategy.
- Exact exchange timezone and bar-boundary convention are `underspecified` in the reviewed text.
- The mechanism generating regime instability remains `unproven`; the paper rejects the most obvious co-movement channel.
- Individual predictor interactions differ across exchanges and specifications.
- Primary results are quarterly; timing within the next quarter is not identified precisely.
- Kraken distress is venue-specific, not equivalent to global token failure.
- Binance robustness uses a survivorship-biased currently listed universe.
- No independent reproduction was performed in this Scout cycle.
- Historical trading costs, borrow, fills, forced exits, and capacity are absent from the source’s predictive AUC evidence.
- The source’s practitioner discussion of high-volatility caution zones is descriptive; it should not be treated as a pre-validated hard trading cutoff.

## Implementation status

`not-implemented`

No PyBroker, Nautilus, strategy-registry, data-pipeline, Paper, Testnet, Demo, or Live implementation was created or modified in this Scout cycle. No implementation task was created.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. It records a source-backed hypothesis and negative/regime evidence only.

Presence in the Alpha Strategy Pool does not authorize trading, strategy registration, Wiki Brain promotion, paper trading, testnet, demo, or live deployment. Any later implementation or adoption decision requires separate Research Intake Review and downstream validation.

## Related Wiki records

No stable related Hermes Wiki Brain record path was resolved or linked in this Scout cycle. Wiki Brain access in this run was used only to resolve and read the canonical `strategy-research-record-v1` contract; no Wiki Brain content was modified.

## Sources

- Aldhahi, H., and Alsamaani, A. (2026). “Regime-Dependent Predictability of Cryptocurrency Distress: Cross-Sectional Evidence from Two Exchanges.” *Journal of Risk and Financial Management*, 19(8), 599. Published 2026-08-07. DOI: https://doi.org/10.3390/jrfm19080599
- Public full-text article page: https://www.mdpi.com/1911-8074/19/8/599
