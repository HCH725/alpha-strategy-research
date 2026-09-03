---
schema: strategy-research-record-v1
title: "Crypto Nonlinear Multi-Fiat Order-Flow ML Forecast: Daily Cross-Sectional Quintiles"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cryptocurrency
  - order-flow
  - machine-learning
  - cross-sectional
  - market-microstructure
status: research-only
confidence: high
source_as_of: 2026-01-15
sources:
  - "https://doi.org/10.1016/j.finmar.2026.101047"
  - "https://www.researchgate.net/publication/399878992_Order_flow_and_cryptocurrency_returns"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Nonlinear Multi-Fiat Order-Flow ML Forecast: Daily Cross-Sectional Quintiles

## Provenance

Primary source: Alexia Anastasopoulos, Nikola Gradojevic, Fred Liu, Alex Maynard, and Ilias Tsiakas, *Order flow and cryptocurrency returns*, *Journal of Financial Markets* 79 (2026), article 101047, DOI `10.1016/j.finmar.2026.101047`, available online 2026-01-15. The reviewed author-uploaded full text is the published article under CC BY 4.0.

The source uses daily data for 84 cryptocurrencies from 2018-01-01 through 2022-06-30. Its machine-learning out-of-sample test period runs from 2020-02-18 through 2022-06-30. CoinMarketCap supplies prices and CryptoCompare supplies signed buyer-initiated and seller-initiated volumes across 11 fiat denominations.

Pool-level source-identity check found an existing record from the same paper: `crypto-world-order-flow-cross-sectional-quintile-weekly-2026-08-31.md`. This record is intentionally distinct rather than a reframing of that record. The existing record normalizes a **weekly direct sort on aggregate world order flow**. This record normalizes the paper's materially different **daily nonlinear machine-learning forecast combination (`NL-Mean`) using all 11 international order-flow predictors, followed by a next-day cross-sectional quintile sort**. The signal construction, model layer, forecast horizon, rebalancing frequency, and out-of-sample estimation procedure are therefore different.

## Economic mechanism

### Source-reported

The authors distinguish a transitory order-flow component associated with temporary price pressure and reversal from a permanent component associated with asymmetric information and price discovery. Lagged order flow remains positively related to future cryptocurrency returns after controlling for lagged returns, which the authors interpret as evidence that trades convey information that is incorporated into prices with persistence.

The source further reports that the predictive relation is nonlinear and involves interactions across international order-flow channels. Nonlinear ML models conditioning on all international order flows outperform linear models and models based on economic fundamentals in one-day-ahead out-of-sample forecasting.

### Research interpretation

The testable mechanism is delayed cross-market information aggregation. Signed demand arriving through different fiat trading channels may reveal heterogeneous regional information or informed trading before that information is fully reflected in the cross-section of coin prices. A nonlinear ensemble may capture threshold effects and interactions among those flows that a single aggregate world-order-flow rank cannot.

This interpretation does not establish causality. The model may instead be exploiting persistent liquidity demand, exchange composition, stale aggregation, or cross-sectional exposures correlated with the order-flow inputs. Those competing explanations must survive explicit controls and modern out-of-sample tests.

## Signal

Source-normalized focal specification: **`NL-Mean` with the `OF` information set, daily quintile sort**.

1. **Historical universe:** use the source's balanced panel of 84 cryptocurrencies. Initial inclusion requires market capitalization above USD 1 million on 2018-01-01, continuous non-zero price and volume through the source sample, and exclusion of stablecoins. This is source-reported but is not a point-in-time modern eligibility rule.
2. **Daily price clock:** source daily USD prices are CoinMarketCap observations at `00:00 GMT`. The paper excludes weekends and U.S. holidays from its daily sample.
3. **Per-fiat raw order flow:** for each coin and each of 11 fiat denominations (USD, EUR, GBP, JPY, CHF, CAD, AUD, NZD, NOK, SEK, KRW), construct net demand as the log difference between buyer-initiated and seller-initiated transaction volume over the daily observation period.
4. **Order-flow standardization:** divide each raw order-flow series by its trailing 30-day order-flow volatility using the source formula `OF_{i,t} = of_{i,t} / sigma(of_{i,t-29:t})`. The same normalization is applied to the international flow inputs.
5. **Predictors:** the focal `OF` information set uses the 11 lagged standardized international order flows. All ML models also condition on lagged returns to capture short-term reversal.
6. **Pre-model standardization:** within each rolling estimation iteration, standardize variables using the mean and variance estimated from the training set only.
7. **Nonlinear model set:** estimate random forest (`RF`), stochastic gradient boosted regression trees (`SGB`), and feed-forward neural networks with one through four hidden layers (`NN1`-`NN4`). Except for RF, the source uses a Huber objective with its threshold set at the 99.9th percentile of returns in the combined training and validation samples; RF uses the default squared-error loss.
8. **Forecast combination:** at each forecast date, compute `NL-Mean` as the equally weighted arithmetic mean of the forecasts from the nonlinear model set. This is source-reported; it is not a Scout-selected ensemble weighting.
9. **Walk-forward estimation:** initial training sample `T1` is 2018-02-14 through 2019-02-14. Initial validation sample `T2` is 2019-02-15 through 2020-02-14. Initial test month begins 2020-02-18 and ends 2020-03-13. Hyperparameters are optimized on the validation sample. Model parameters are held fixed for one month, after which validation and test windows roll forward by one month and the training sample expands by one month. Repeat through 2022-06-30.
10. **Forecast target:** generate one-day-ahead return forecasts for every eligible coin.
11. **Cross-sectional rank:** on each source trading day `t`, rank all 84 coins from lowest to highest by the `NL-Mean OF` forecast for return at `t+1`.
12. **Portfolio formation:** divide the ranked cross-section into five quintiles. `P1` contains the lowest forecasts and `P5` the highest forecasts. Equal-weight constituents within each quintile.
13. **Long-short rule:** long `P5` and short `P1`; portfolio return is `R_{P5,t+1} - R_{P1,t+1}`. The source also evaluates long-only `P5` because shorting some coins may be infeasible.
14. **Holding/rebalance:** hold for one source-defined daily period and recompute the forecast/rank each day; portfolios are rebalanced daily.
15. **Executable formation timestamp:** **underspecified**. The paper's statistical rule uses information at `t` to evaluate `t+1`, but it does not specify the vendor publication latency, exact time at which all 11 signed-flow fields are simultaneously available, or an executable venue/order price after the `00:00 GMT` data cut. No same-timestamp fill assumption should be treated as source-reported.
16. **Stops, take-profit, leverage and discretionary filters:** none are specified by the source for this portfolio sort. Do not add them to a source-faithful reproduction.

## Required data

- **Instrument/universe:** historical reproduction requires the paper's 84-coin balanced panel; a modern test requires a point-in-time investable universe with documented listings/delistings rather than full-sample survival filtering.
- **Price source:** CoinMarketCap daily USD price at 00:00 GMT for the source reproduction.
- **Order-flow source:** CryptoCompare signed buyer-initiated and seller-initiated volume aggregated from more than 300 exchanges.
- **Fiat channels:** USD, EUR, GBP, JPY, CHF, CAD, AUD, NZD, NOK, SEK, and KRW.
- **Fields:** per-coin buy volume and sell volume for each fiat channel, price, lagged return, market capitalization, total volume, stablecoin classification, and trading-availability history.
- **Timeframe:** daily for the focal ML strategy.
- **Timestamp/alignment:** GMT/UTC convention; exact vendor availability time and cross-venue synchronization are **underspecified** and must be audited before causal reproduction.
- **Point-in-time ML state:** preserve training, validation, test boundaries; use only training-set moments for feature standardization; preserve monthly walk-forward hyperparameter/model refresh logic.
- **Missing data:** source universe construction avoids missing observations through a balanced-panel requirement; no general source imputation rule is provided. Imputation should not be silently introduced.
- **Data gap:** historical signed aggressor-side volumes by coin and by 11 fiat denominations may require vendor access and may not be reconstructible from ordinary OHLCV.
- **Model details:** the main paper identifies the model classes and walk-forward design, while detailed hyperparameter search spaces are delegated to its Online Appendix. Exact independent reproduction requires that appendix or equivalent author code/configuration.
- **Cost fields for tradability tests:** venue-specific maker/taker fees, bid-ask spread, slippage, borrow availability/cost or perpetual funding, market impact, and executable instrument mapping.

## Execution assumptions

The source tests predictive portfolio returns, not a fully specified venue-level execution engine. The following boundaries therefore apply:

- **Order type:** underspecified.
- **Signal-to-order delay:** underspecified because the exact availability timestamp of all vendor flow inputs is not reported.
- **Fill/reference price:** source return measurement is based on CoinMarketCap daily prices rather than guaranteed executable venue quotes.
- **Latency:** underspecified.
- **Liquidity/participation cap:** underspecified.
- **Position limits:** source portfolios are equal-weight; hard venue position limits are underspecified.
- **Shorting:** the paper explicitly notes that some coins may be difficult or impossible to short and therefore separately studies long-only `P5`.
- **Borrow/funding:** not directly modeled as a realized historical borrow/funding series in the normalized signal.
- **Transaction costs:** the source reports turnover and a **break-even transaction cost**, not a deduction of observed venue-specific realized costs from every trade. Break-even cost must not be restated as actual net-of-cost performance.
- **Modern executable mapping:** using spot margin or perpetual futures instead of the source's aggregated price series is **research-proposed** and constitutes an adaptation, not source-faithful reproduction.

## Evidence

### Source-reported

The published article reports that out-of-sample ML forecasting is conducted only at the daily horizon. The test sample is 2020-02-18 through 2022-06-30, using an expanding training sample, a rolling validation/test procedure, and monthly model refreshes.

For statistical forecast accuracy, the paper reports that nonlinear models using order flow outperform the zero-return benchmark and models using economic fundamentals. The best reported model is SGB with the `OF` information set, with out-of-sample `R^2` of approximately `0.39%` under the paper's squared-error metric.

For the focal `NL-Mean OF` portfolio in Table 12, the source reports a daily `P5-P1` mean return of **0.78%**, daily three-factor alpha of **0.81%** with Newey-West t-statistic **5.83**, and annualized Sharpe ratio **3.61**. Table 12 states that portfolios are equal-weight and rebalanced daily.

Table 13 reports for the same `NL-Mean OF` construction a long-only `P5` mean return of **0.84%**, alpha **0.87%**, annualized Sharpe ratio **1.98**, daily turnover **0.78**, and break-even transaction cost **1.07%**. For the long-short `P5-P1` version it reports mean **0.78%**, alpha **0.81%**, annualized Sharpe **3.61**, daily turnover **1.56**, and break-even transaction cost **0.50%**. These are source-reported portfolio statistics, not independently verified or realized live returns.

The paper also reports that the best single nonlinear model, SGB using the same OF information set, has a long-short annualized Sharpe of **3.68**, and that nonlinear OF models continue to show economic value in lower-arbitrage-cost and top-10-market-cap subsets.

### Independently reproduced

not independently reproduced

### Negative evidence

- The source sample ends on 2022-06-30, so persistence under the post-2022 market structure is **unproven**.
- The historical universe is a full-sample balanced panel requiring continuous trading, which creates a survivorship/selection concern for direct replication as an investable strategy.
- Statistical portfolio returns use aggregated CoinMarketCap prices and vendor-aggregated order flow rather than a single executable venue, producing a material signal/execution mapping gap.
- The source reports break-even transaction-cost capacity rather than a point-in-time reconstruction using observed maker/taker fees, spreads, slippage, borrow, funding and impact for each constituent.
- Daily rebalancing produces high turnover, especially for the long-short portfolio (`1.56` in Table 13), so cost and capacity estimates are first-order rather than cosmetic.
- Detailed ML hyperparameter grids are in the Online Appendix; exact reproduction without those settings is incomplete.
- The source excludes weekends and U.S. holidays from its daily ML sample even though cryptocurrency markets trade continuously. Whether the learned relation transfers to true 24/7 daily operation is **unproven**.
- No contrary replication was identified in the reviewed sources; absence is not evidence of no negative result.

## Falsification

The hypothesis should be materially weakened or rejected under the following pre-declared tests. Thresholds introduced by this Scout are explicitly labeled **research-defined falsification threshold**.

1. **Strict post-source OOS:** rebuild the signal with point-in-time data and freeze all design choices before testing dates after 2022-06-30. **Research-defined falsification threshold:** reject the modern continuation claim if the net `P5-P1` mean return is `<= 0` over the locked OOS sample.
2. **Leakage audit:** independently verify vendor timestamps, feature standardization, train/validation/test membership, monthly hyperparameter refresh, and that no future return enters feature creation. Any confirmed look-ahead or test-set contamination that is necessary to reproduce the reported effect is an immediate failure.
3. **Rank monotonicity:** test whether realized next-day returns increase across forecast quintiles. **Research-defined falsification threshold:** fail the cross-sectional ranking mechanism if the locked OOS `P5-P1 <= 0` and there is no positive rank-return monotonicity.
4. **Incremental ML value:** compare `NL-Mean OF` against the paper's simpler direct world-order-flow sort and against lagged-return-only models using identical samples and costs. **Research-defined falsification threshold:** reject the claim that nonlinear multi-fiat interactions add alpha if `NL-Mean OF` does not improve OOS net performance over both controls.
5. **Shuffled-label placebo:** rerun the complete training pipeline on at least 1,000 return-label permutations while preserving the feature/time structure. **Research-defined falsification threshold:** fail if the observed locked-OOS Sharpe does not exceed the 95th percentile of placebo Sharpes.
6. **Model perturbation:** vary random seeds, reasonable tree depth/boosting parameters, neural-network width/depth, Huber threshold and monthly refresh choices within predeclared neighborhoods. Fail if performance depends on a narrow isolated parameter setting and sign stability does not survive the perturbation set.
7. **Point-in-time universe:** replace the source balanced panel with a listing-aware, delisting-aware investable universe. **Research-defined falsification threshold:** reject portability if `P5-P1` net return becomes non-positive and the original effect is attributable to full-sample survivor selection.
8. **24/7 clock robustness:** compare the source weekday/holiday calendar with genuine 24/7 UTC daily formation and alternative non-overlapping UTC cuts. Fail portability if the result exists only under the historical weekday calendar and disappears under plausible causal crypto clocks.
9. **Cost and capacity stress:** map constituents to executable spot-margin or perpetual instruments and apply contemporaneous fees, spread, slippage, borrow/funding and impact. **Research-defined falsification threshold:** reject tradability if expected net return after measured costs is `<= 0` at the intended capacity.
10. **Venue/data ablation:** compare all-11-fiat order flow with USD-only, KRW-only, single-venue aggressor flow, and aggregated world order flow. If the alpha cannot survive removal of one vendor-specific channel or is entirely explained by a single region/venue, downgrade the proposed global-information mechanism.
11. **Competing explanations:** control for momentum/reversal, volume, liquidity, volatility, size, exchange composition and contemporaneous return pressure. Reject the informational-price-discovery interpretation if the forecast rank has no incremental predictive content after those controls.

## Crypto portability

**Direct in source domain; adapted for modern execution.**

The evidence is already cryptocurrency-specific, so no traditional-market translation is required. The research signal, however, is based on globally aggregated signed volume across many exchanges and fiat currencies, while a deployable system may trade spot, margin or perpetual instruments on a smaller set of venues.

A modern perpetual implementation must therefore be labeled **research-proposed**. It would need explicit treatment of funding, liquidation-driven flow, contract availability, quote currency/stablecoin effects, leverage, venue fragmentation, exchange outages and delistings. A Binance-only or USDT-perpetual-only model is not equivalent to the source's multi-fiat global order-flow information set.

The source's weekday/U.S.-holiday daily calendar is also not native to a 24/7 market. Any continuously rebalanced UTC implementation is an adaptation requiring fresh falsification rather than a silent calendar change.

## Limitations

- **Not independently reproduced.**
- **Data gap:** exact historical multi-fiat signed aggressor volume requires CryptoCompare-equivalent data and may not be available from ordinary exchange OHLCV archives.
- **Underspecified:** exact real-time publication/availability timestamp for each vendor field, executable signal-to-order delay, fill model, and venue mapping.
- **Partial reproducibility gap:** main-paper model classes and walk-forward splits are explicit, but detailed hyperparameter grids/configurations reside in the Online Appendix.
- **Selection risk:** balanced-panel construction requires continuous trading through the historical sample.
- **Execution risk:** high daily turnover, short availability and fragmented venue costs may materially reduce source-reported gross performance.
- **Calendar mismatch:** source daily ML tests exclude weekends and U.S. holidays despite 24/7 crypto trading.
- **Regime risk:** all reported OOS evidence ends 2022-06-30; later persistence is unproven.
- **Model risk:** ensemble performance may be sensitive to model complexity, hyperparameter tuning and nonstationary flow/return interactions.
- **Vendor dependence:** the information content may partly reflect CryptoCompare aggregation methodology rather than a venue-invariant economic signal.

## Implementation status

No implementation or validation in PyBroker, NautilusTrader, the strategy registry, data pipeline, paper trading, testnet or live trading has been performed for this record.

`implementation_status: not-implemented`

## Adoption boundary

This record is Alpha Strategy Pool research material only. It does not approve the strategy, authorize vendor-data acquisition, create an implementation task, or authorize Paper, Testnet or Live execution.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain strategy links are asserted in this staging record. Concept-level clustering, consolidation and Wiki promotion belong to the separate Research Intake Review workflow.

Pool-level materially related record:

- `crypto-world-order-flow-cross-sectional-quintile-weekly-2026-08-31.md` — same primary paper, but materially distinct weekly direct aggregate-world-order-flow sort; it explicitly excludes the paper's ML forecast strategies from its focal rule.

## Sources

1. Alexia Anastasopoulos, Nikola Gradojevic, Fred Liu, Alex Maynard, Ilias Tsiakas, *Order flow and cryptocurrency returns*, *Journal of Financial Markets* 79 (2026), article 101047, DOI `10.1016/j.finmar.2026.101047`, available online 2026-01-15: https://doi.org/10.1016/j.finmar.2026.101047
2. Author-uploaded published full text, ResearchGate, uploaded 2026-02-26: https://www.researchgate.net/publication/399878992_Order_flow_and_cryptocurrency_returns
