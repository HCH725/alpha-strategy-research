---
schema: strategy-research-record-v1
title: USDT Exchange Net-Inflow Buy-Side Liquidity Drift at 1-2 Hour Horizons
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - stablecoin
  - usdt
  - on-chain
  - exchange-flow
  - intraday
status: research-only
confidence: medium
source_as_of: 2025-06
sources:
  - https://arxiv.org/abs/2411.06327
  - https://arxiv.org/pdf/2411.06327
  - https://doi.org/10.48550/arXiv.2411.06327
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4630115
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# USDT Exchange Net-Inflow Buy-Side Liquidity Drift at 1-2 Hour Horizons

## Provenance

Primary source: Yeguang Chi, Qionghua (Ruihua) Chu, and Wenyan Hao, *Return and Volatility Forecasting Using On-Chain Flows in Cryptocurrency Markets*, arXiv:2411.06327. The directly reviewed public PDF is dated June 2025. The paper's core on-chain/return sample runs from 2017-12-16 through 2023-01-20 and evaluates 1-, 2-, 3-, 4-, and 6-hour forecast horizons.

Stable source references:

- https://arxiv.org/abs/2411.06327
- https://arxiv.org/pdf/2411.06327
- https://doi.org/10.48550/arXiv.2411.06327
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4630115

Source-identity / pool-level deduplication check:

- The same paper already appears in `ethereum-exchange-net-inflow-bearish-drift-1h-6h-2026-09-01.md`, which captures **ETH-denominated exchange net inflow -> negative future ETH return**.
- The same paper also appears in `ethereum-exchange-net-inflow-conditioned-call-selling-2026-09-03.md`, which captures a **high-ETH-inflow-conditioned Deribit short-call implementation**.
- This record is materially distinct because its predictor, economic mechanism, traded direction, and cross-asset mapping are different: **USDT exchange net inflow is interpreted as deployable buy-side liquidity and predicts positive BTC/ETH returns at the next 1-2 hour horizons**. It does not rely on ETH sell-inventory pressure or option-volatility exposure.
- No repository or Wiki Brain record with the same arXiv/SSRN source and the materially same USDT-net-inflow -> 1-2 hour BTC/ETH positive-return construction was found in the pre-write search.

Source/data as-of date: public paper version June 2025; empirical return sample ends 2023-01-20.

## Economic mechanism

### Source-reported

The authors define net inflow as exchange inflow minus exchange outflow. They interpret USDT net inflow into cryptocurrency exchanges as "dry powder": stablecoin capital transferred from investor wallets onto exchanges is more immediately available to purchase risk assets. In the paper's predictive regressions, larger USDT net inflow is associated with higher subsequent ETH and BTC returns, particularly at 1- and 2-hour horizons.

The source reports that the relation is not statistically significant at 3-, 4-, or 6-hour horizons for either BTC or ETH return forecasting. This horizon decay is part of the source result and should not be removed when normalizing the hypothesis.

### Research interpretation

This is a crypto-native cross-asset liquidity-arrival hypothesis:

- **Predictor:** point-in-time USDT net inflow to centralized exchanges.
- **Target:** subsequent BTC or ETH return.
- **Direction:** positive USDT net inflow -> positive expected BTC/ETH return.
- **Source-supported horizon:** strongest at 1 hour and still statistically significant at 2 hours; no source-supported return effect at 3, 4, or 6 hours.
- **Mechanism:** newly deposited stablecoin balances increase immediately deployable purchasing capacity on exchanges, creating short-lived demand pressure in major crypto assets.

The hypothesis is falsifiable because it predicts a specific sign, a short horizon, and a material decline in predictive content beyond two hours.

Competing explanations include market-wide risk-on news causing both USDT exchange transfers and BTC/ETH appreciation, stablecoin treasury or exchange internal transfers being misclassified as investor dry powder, and delayed provider labeling of exchange flows creating apparent predictability that would not have been tradable in real time.

## Signal

### Source-reported construction

The paper's return-predictive regression is:

`R_(t+h) = beta_0 + beta_1 * USDT_Net_Inflow_t + e_(t+h)`

and a double-variable version adds the current-period return control:

`R_(t+h) = beta_0 + beta_1 * USDT_Net_Inflow_t + beta_2 * R_t + e_(t+h)`

where `h` is 1, 2, 3, 4, or 6 hours. Net inflows are measured in USD millions and returns are decimals.

Source-normalized semantics:

1. At intraday observation time `t`, compute USDT exchange net inflow as inflow from wallets to exchanges minus outflow from exchanges to wallets.
2. Use the observed net inflow to forecast BTC or ETH return over the next `h` hours.
3. The source reports positive `beta_1` coefficients for both BTC and ETH at 1- and 2-hour horizons.
4. The source does not report statistically significant positive return predictability at 3, 4, or 6 hours.

### Source-reported quantitative results

For ETH returns, Table 2 Panel A reports:

- 1-hour single-variable `beta_1 = 1.1e-5`, t-statistic 5.903; double-variable `beta_1 = 1.1e-5`, t-statistic 5.978.
- 2-hour single-variable `beta_1 = 7.5e-6`, t-statistic 2.595; double-variable `beta_1 = 8.4e-6`, t-statistic 2.900.
- 3-, 4-, and 6-hour USDT-net-inflow coefficients are not statistically significant in the reported models.

For BTC returns, Table 3 Panel A reports:

- 1-hour single-variable `beta_1 = 6.3e-6`, t-statistic 4.196; double-variable `beta_1 = 6.5e-6`, t-statistic 4.306.
- 2-hour single-variable `beta_1 = 4.3e-6`, t-statistic 1.872; double-variable `beta_1 = 4.8e-6`, t-statistic 2.105.
- 3-, 4-, and 6-hour USDT-net-inflow coefficients are not statistically significant.

The authors summarize the double-variable model economically as approximately:

- USD 100 million USDT net inflow -> +0.11% ETH return over the next hour.
- USD 100 million USDT net inflow -> +0.065% BTC return over the next hour.

These are source-reported regression interpretations, not independently reproduced trading returns.

### Operational trading rule

**underspecified**.

The source establishes predictive regressions but does not specify one canonical executable threshold such as an absolute USDT amount, percentile rank, rolling z-score, or probability cutoff for entering a long BTC/ETH trade. It also does not prescribe one unique asset-allocation rule between BTC and ETH.

The following testable operationalization is **research-proposed**, not source-reported:

1. Build a point-in-time hourly USDT exchange-net-inflow series using only data actually available after provider finalization.
2. Standardize the observation against a trailing point-in-time window.
3. Primary branch: enter long BTC or ETH only when USDT net inflow is positive and exceeds a predeclared trailing percentile or z-score threshold.
4. Hold for one hour; separately test two hours as the source-supported secondary horizon.
5. Do not extend the canonical signal to 3+ hours unless an independent sample provides new evidence.
6. Evaluate BTC and ETH separately first; any combined portfolio is a separate research choice.

Any threshold, lookback, cross-asset allocation, no-trade band, or confidence scaling is `research-proposed`.

Entry price, re-entry handling, overlapping 1h/2h positions, and position sizing are **underspecified** by the source.

## Required data

- **Signal asset:** USDT transfers into and out of centralized exchanges.
- **Target assets:** BTC and ETH.
- **Market type in source analysis:** cryptocurrency spot/index return series; the paper does not define a canonical perpetual implementation.
- **Source sample:** 2017-12-16 through 2023-01-20.
- **Forecast intervals:** 1h, 2h, 3h, 4h, 6h; only 1h and 2h are source-supported for the focal positive-return hypothesis.
- **Flow fields:** USDT exchange inflow, USDT exchange outflow, derived `net inflow = inflow - outflow`.
- **Price fields:** BTC and ETH prices sufficient to reconstruct non-overlapping or source-consistent forward returns.
- **Control field:** current-period BTC or ETH return for the source's double-variable regression.
- **Exchange coverage:** the paper lists multiple centralized exchanges in its data source set, including Binance, Bitfinex, Bitget, Bitstamp, Bybit, Coinbase, Crypto.com, Deribit, Gate.io, Gemini, Kraken, KuCoin, OKX, Poloniex, and others.
- **Timestamp:** intraday clock aligned between USDT flow aggregation and BTC/ETH returns.
- **Point-in-time requirement:** actual availability/finalization timestamp of the flow observation, not merely the blockchain transaction timestamp or a retrospectively revised hourly series.
- **Address-label vintage:** exchange wallet classifications must be point-in-time or explicitly vintage-controlled; later address knowledge cannot be backfilled into earlier signal timestamps without being labeled as retrospective.
- **Missing-data rule:** data gap; the source does not specify an imputation policy. A replication should skip incomplete intervals rather than silently impute.

For a perpetual implementation, additionally require bid/ask, fees, slippage, depth, mark/index prices, funding, liquidation conditions, and exchange-specific contract metadata.

## Execution assumptions

### Source-reported

The paper reports predictive regressions and case-study/option applications, not a complete underlying BTC/ETH trading implementation driven by USDT flows. No canonical order type, execution venue, signal-to-order latency, position size, leverage, stop, or net-of-cost spot/perpetual trading rule is specified for this USDT-return forecast relation.

### Research interpretation

Any tradable implementation must explicitly model:

- delay from on-chain transaction confirmation to provider exchange-label classification and final net-flow publication;
- signal-to-order latency after the finalized signal becomes available;
- exchange fees and bid-ask spread;
- slippage and market impact;
- perpetual funding and basis if perps are used;
- partial fills, outages, and rejected orders;
- stablecoin depeg or redemption stress;
- exchange treasury/internal-wallet transfers that do not correspond to investor buying intent.

Same-hour execution using a flow figure that becomes final only after that hour closes is prohibited because it would create look-ahead bias.

## Evidence

### Source-reported

The June 2025 paper reports that USDT exchange net inflows positively predict BTC and ETH returns, especially at 1- and 2-hour intervals, in the 2017-12-16 to 2023-01-20 sample.

For ETH, Table 2 Panel A reports positive and statistically significant USDT-net-inflow coefficients at 1 and 2 hours in both single- and double-variable regressions. For BTC, Table 3 Panel A reports the same positive pattern at 1 hour and weaker but still positive evidence at 2 hours. The source explicitly reports no statistically significant USDT-net-inflow return predictability at 3, 4, or 6 hours.

The paper's economic interpretation of the double-variable model states that USD 100 million of USDT net inflow predicts approximately +0.11% ETH return and +0.065% BTC return over the next hour.

The authors also state that they perform in-sample and out-of-sample regression tests, but the public text reviewed in this Scout cycle does not provide a uniquely specified live threshold, a full execution protocol, or a net-of-cost underlying BTC/ETH strategy based solely on USDT flow.

All figures and statistical results above are source-reported and trace to the cited primary paper. They are not our verified results.

### Independently reproduced

not independently reproduced

### Negative evidence

- The source itself shows clear horizon decay: the focal positive-return relation is not statistically significant at 3-, 4-, or 6-hour horizons.
- The source does not supply a single precommitted executable USDT-flow entry threshold for BTC/ETH longs.
- The reported regressions do not by themselves establish net-of-cost trading profitability.
- Historical exchange-address classification may be revised after the fact, introducing point-in-time leakage if modern labels are used retroactively.
- USDT deposits can reflect exchange treasury movements, arbitrage, collateral transfers, redemptions, market-making inventory, or venue migration rather than directional spot buying.
- The core sample ends in January 2023, before the U.S. spot-Bitcoin-ETF era and later changes in stablecoin and institutional market structure.
- The relation may be driven by common risk-on shocks rather than a causal dry-powder channel.
- The source's BTC 2-hour coefficient is weaker than the 1-hour effect, reinforcing that the signal should not be generalized into a persistent multi-hour momentum rule.

## Falsification plan

1. **Point-in-time availability audit.** Rebuild USDT exchange net inflow using actual provider availability timestamps and historical label vintages. **Research-defined falsification threshold:** reject the tradable hypothesis if the 1h/2h coefficient sign or economic value disappears when the signal is delayed to the first verifiable availability time.
2. **Source-sample regression reproduction.** Reproduce the paper's 1h, 2h, 3h, 4h, and 6h regressions for BTC and ETH. **Research-defined falsification threshold:** materially weaken the record if the 1h coefficient is not positive for both BTC and ETH or if the claimed horizon decay cannot be reproduced.
3. **Strict post-source OOS.** Test 2023-01-21 onward, separately including 2024-2026 institutional/ETF-era regimes. **Research-defined falsification threshold:** reject persistence if 1h and 2h OOS coefficients are non-positive or economically negligible after costs across the full post-source sample.
4. **Threshold precommitment.** Compare predeclared positive-flow, percentile, and z-score branches without post-hoc cherry-picking. **Research-defined falsification threshold:** reject a thresholded trading interpretation if positive expectancy appears only at one narrow threshold and disappears at adjacent predeclared thresholds.
5. **Common-shock controls.** Add contemporaneous market return, realized volatility, aggregate volume, funding, basis, macro-news windows, and stablecoin price deviations. **Research-defined falsification threshold:** materially weaken the dry-powder mechanism if USDT flow loses incremental predictive content after these controls.
6. **Internal-transfer filter.** Exclude known exchange treasury reshuffles and internal wallet migrations. **Research-defined falsification threshold:** reject the investor-liquidity interpretation if the effect is concentrated in classified internal/treasury movements.
7. **Venue/vendor robustness.** Compare at least two independently constructed flow datasets or labeling systems when available. **Research-defined falsification threshold:** materially weaken the hypothesis if sign or timing depends on one provider's retrospective classifications.
8. **Cost and latency stress.** Backtest spot and perpetual executions with realistic fees, spread, slippage, funding, and one or more observation delays. **Research-defined falsification threshold:** reject tradability if realistic net PnL is non-positive across both 1h and 2h source-supported horizons.
9. **Placebo timing.** Shift USDT-flow signals by non-overlapping placebo lags while preserving marginal flow distribution. **Research-defined falsification threshold:** materially weaken the information hypothesis if placebo timing performs similarly to true point-in-time timing.
10. **Cross-stablecoin control.** Test USDC and other major stablecoin exchange flows as predeclared controls. If all stablecoins behave identically only through broad market-state exposure, the specific USDT dry-powder interpretation is weakened.

Failure should lead to rejection or reclassification of this hypothesis; it should not be rescued by unconstrained threshold retuning.

## Crypto portability

**direct**.

The predictor and targets are native crypto-market variables and the source directly studies BTC, ETH, and USDT exchange flows. No traditional-market adaptation is required for the core hypothesis.

Porting the regression relation into a perpetual-futures implementation is not automatic. A derivatives implementation must account for:

- 24/7 trading and exact hourly boundary conventions;
- perpetual funding and basis;
- venue fragmentation between spot and derivatives;
- stablecoin quote-currency differences;
- mark/index methodology;
- liquidation and leverage effects;
- exchange-specific USDT availability and wallet labeling;
- stablecoin depeg/redemption events;
- changing share of trading conducted through ETFs, regulated venues, decentralized exchanges, and non-USDT quote assets.

BTC and ETH are source-supported targets. Extension to SOL, BNB, XRP, or smaller assets is **unproven**.

## Limitations

- **not independently reproduced**.
- **underspecified:** no canonical executable USDT-flow threshold, order type, allocation rule, re-entry state machine, or position sizing.
- **data gap:** exact point-in-time provider publication/finalization latency is not fully specified in the reviewed source.
- **data gap:** historical exchange-address label vintage and revision policy are not fully specified.
- **sample-age risk:** core return sample ends 2023-01-20.
- **horizon fragility:** source-supported return effect is concentrated at 1-2 hours and absent at 3-6 hours.
- **execution gap:** no source-reported net-of-cost underlying BTC/ETH strategy is provided.
- **identification risk:** common risk-on shocks may jointly cause stablecoin deposits and asset appreciation.
- **classification risk:** treasury/internal exchange transfers can contaminate net inflow.
- **structural-change risk:** post-ETF, stablecoin regulation, venue migration, and institutional market structure may alter the relation.

## Implementation status

`not-implemented`.

No PyBroker, NautilusTrader, strategy registry, data pipeline, Paper, Testnet, or Live implementation was created or modified in this Scout cycle.

## Adoption boundary

This record is `research-only`, `not-implemented`, `not-approved`, and `approval_scope: research-only`.

Presence in the Alpha Strategy Pool means only that the source-backed hypothesis has been normalized for Research Intake Review. It does not mean the signal is profitable, validated alpha, approved for implementation, approved for paper trading, approved for testnet, or approved for live trading.

No implementation task is created by this record.

## Related Wiki records

- `quant/ethereum-exchange-net-inflow-bearish-drift-1h-6h-2026-09-01.md` — same primary source but a materially different predictor and mechanism: ETH exchange deposits as sell-side pressure rather than USDT deposits as buy-side liquidity.
- `quant/stablecoin-dry-powder-volatility-targeting-copula-2026-09-01.md` — related stablecoin "dry powder" family, but based on stablecoin volatility/volume and copula risk transmission rather than point-in-time USDT exchange net inflow.

The repository also contains `ethereum-exchange-net-inflow-conditioned-call-selling-2026-09-03.md`; that record shares the primary paper but represents a distinct ETH-flow-conditioned options payoff rather than this USDT-flow directional-return hypothesis.

## Sources

1. Yeguang Chi, Qionghua (Ruihua) Chu, and Wenyan Hao, *Return and Volatility Forecasting Using On-Chain Flows in Cryptocurrency Markets*, arXiv:2411.06327, public PDF dated June 2025. https://arxiv.org/abs/2411.06327
2. Full public arXiv PDF, especially Sections 2.2 and 3.2, Table 2 Panel A, Table 3 Panel A, and the conclusion. https://arxiv.org/pdf/2411.06327
3. arXiv DOI resolver. https://doi.org/10.48550/arXiv.2411.06327
4. SSRN record for the June 2025 version, abstract ID 4630115. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4630115
