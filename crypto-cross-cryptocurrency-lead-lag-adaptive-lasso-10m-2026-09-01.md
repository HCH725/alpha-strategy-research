---
schema: strategy-research-record-v1
title: Crypto Cross-Cryptocurrency Lead-Lag Predictability with Adaptive LASSO (Up to 10 Minutes)
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - lead-lag
  - information-diffusion
  - adaptive-lasso
status: research-only
confidence: medium
source_as_of: 2024-06
sources:
  - https://doi.org/10.1016/j.jedc.2024.104863
  - https://ink.library.smu.edu.sg/lkcsb_research/6901
  - https://doi.org/10.2139/ssrn.3974583
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - A recent simplified public replication reports statistically positive BTC-to-altcoin lead coefficients but negative net performance after costs; it is not a replication of the full published adaptive-LASSO specification and therefore is only weak negative evidence.
---

# Crypto Cross-Cryptocurrency Lead-Lag Predictability with Adaptive LASSO (Up to 10 Minutes)

## Provenance

Primary published source: Li Guo, Bo Sang, Jun Tu, and Yu Wang, "Cross-cryptocurrency return predictability," *Journal of Economic Dynamics and Control*, Volume 163, Article 104863 (2024), DOI: https://doi.org/10.1016/j.jedc.2024.104863.

Public author-institution record / published working-paper version: Singapore Management University InK, https://ink.library.smu.edu.sg/lkcsb_research/6901, identifier DOI https://doi.org/10.2139/ssrn.3974583. The public record states minute-frequency Binance data, predictive horizons up to ten minutes, adaptive LASSO / PCA robustness, and an out-of-sample long-short portfolio after transaction costs.

The 2024 journal article is the canonical citation. Earlier SSRN/EconBiz records exist with materially different author lists and performance summaries; those version differences are preserved as a provenance caution rather than merged into the published-paper evidence.

## Economic mechanism

### Source-reported

The authors attribute cross-cryptocurrency return predictability to information spillovers and slow information diffusion. Common shocks are incorporated into some cryptocurrencies faster than others because investor attention is limited, so lagged returns of other coins retain information about the focal coin's next few minutes of return.

### Research interpretation

This is a short-horizon lead-lag hypothesis rather than generic momentum. The predictive object is the cross-coin return vector: recent returns of faster-moving or more informative cryptocurrencies may forecast delayed adjustment in other coins. Adaptive LASSO is used to select which lagged cross-coin returns contain incremental information for each focal asset.

The falsifiable mechanism is: after controlling for the focal asset's own recent return history, a sparse subset of other coins' lagged minute returns should improve strictly out-of-sample next-period forecasts, and a portfolio formed from those forecasts should retain positive net performance after realistic fees, spread, slippage, and latency.

## Signal

Normalized source-backed rule:

- Universe: liquid cryptocurrencies traded on Binance; the public working-paper summary describes minute-frequency data and earlier versions describe a top-coin universe.
- Predictors: lagged minute returns of other cryptocurrencies, with the focal coin's own history treated separately as needed by the forecasting specification.
- Model: adaptive LASSO to select informative cross-cryptocurrency lagged-return predictors; principal-component analysis is reported as a robustness alternative.
- Forecast horizon: predictive relationships are reported up to ten minutes.
- Portfolio use: rank or otherwise map out-of-sample return forecasts into long and short positions, with frequent rebalancing.

Underspecified from the public canonical materials reviewed in this Scout cycle:

- exact final published universe membership and point-in-time eligibility rule;
- exact lag set for every model specification;
- adaptive-LASSO penalty-selection procedure used in the final published version;
- exact portfolio breakpoints / number of long and short assets;
- exact position weights;
- exact rebalance convention in the final journal version;
- exact signal-to-order delay and fill rule;
- handling of overlapping ten-minute forecasts;
- whether spot, futures, or both are used for each published economic-value table.

Do not silently infer these missing rules from older working-paper versions.

## Required data

- Point-in-time Binance instrument universe.
- Minute-level tradeable prices or OHLCV for each included cryptocurrency.
- Reliable synchronized timestamps across all coins.
- Delisting / listing history to avoid survivorship bias.
- Bid-ask spread and fee schedule for realistic cost modeling.
- If derivatives are tested: contract type, mark/index price, funding, and contract availability at each timestamp.
- Data-quality handling for stale candles, missing minutes, venue outages, and newly listed coins.

## Execution assumptions

The published research reports economic value after transaction costs, but the public sources reviewed here do not fully specify all execution details needed for independent implementation.

Research implementation should therefore assume no same-bar clairvoyance. Forecasts must be formed only after all predictor returns used by the model are observable, and orders should execute no earlier than the next feasible tradeable timestamp. Fees, spread, slippage, latency, partial fills, and turnover must be modeled explicitly.

Because this is a minute-frequency strategy, small changes in latency and cost assumptions can dominate the gross edge. Any implementation that ignores these frictions should be treated as non-decision-grade.

## Evidence

### Source-reported

The 2024 peer-reviewed article reports strong evidence of cross-cryptocurrency return predictability using Binance data: lagged returns of other cryptocurrencies significantly predict focal-cryptocurrency returns, with robustness across adaptive LASSO and principal-component methods. It also reports that a long-short portfolio formed from the predictive information generates sizable out-of-sample returns after transaction costs.

The SMU public working-paper record states that predictability extends up to ten minutes and reports an out-of-sample long-short portfolio with positive economic value after transaction costs. Because versioned public records report different performance figures, this record deliberately does not promote one exact return statistic as the canonical journal result without table-level verification from the final article.

### Independently reproduced

Not independently reproduced.

### Negative evidence

A recent public simplified replication inspired by this paper reports positive BTC-to-altcoin lead coefficients across a fixed altcoin universe but failure to remain profitable after costs. This is not a replication of the full published adaptive-LASSO cross-coin model and should not be treated as a direct contradiction; it nevertheless reinforces that transaction costs and model specification are central to the hypothesis.

More generally, the source's mechanism is expected to weaken as market-making competition, co-location, exchange infrastructure, and cross-venue arbitrage improve. The historical finding therefore requires fresh post-publication OOS testing.

## Falsification plan

1. Reconstruct a point-in-time liquid Binance universe with minute bars and no survivorship leakage.
2. Use walk-forward estimation only; fit adaptive LASSO using training data available strictly before each forecast timestamp.
3. Compare against:
   - focal-coin own-lag model;
   - simple BTC-leads-altcoins baseline;
   - equal-weight cross-coin momentum baseline;
   - zero-return forecast.
4. Test horizons from 1 through 10 minutes without selecting the best horizon on the final test set.
5. Measure both forecast IC / directional accuracy and a fully costed long-short portfolio.
6. Stress test fees, spread, slippage, latency, stale bars, missing assets, and reduced liquidity.
7. Require a genuinely post-publication holdout, ideally including 2024-2026 market regimes.
8. Reject or materially downgrade the hypothesis if cross-coin predictors fail to improve OOS performance over own-lag baselines, or if net returns are non-positive under realistic execution costs.

## Crypto portability

direct

The source directly studies cryptocurrency markets and Binance data. Portability risk remains high across venues because lead-lag structure depends on fragmentation, quote currency, participant mix, matching-engine latency, and liquidity. A Binance result should not be assumed to transfer unchanged to other CEXs, DEXs, spot markets, or perpetual futures.

## Limitations

- Not independently reproduced.
- Exact final-journal portfolio construction is underspecified in the public materials reviewed here.
- Earlier public working-paper versions contain differing author lists and reported performance figures; do not merge them as though they were one immutable specification.
- Minute-level costs and latency can erase apparent statistical predictability.
- The result may decay structurally as information diffusion accelerates.
- Cross-coin synchronization and stale-price handling can create false lead-lag relationships.
- Data gap: no fresh 2024-2026 independent replication of the full final specification was identified in this cycle.

## Implementation status

Research-only. No PyBroker, NautilusTrader, paper, testnet, or live implementation has been completed as part of this Scout cycle.

## Adoption boundary

This record is staging-layer research material only. It is not evidence that the strategy is currently profitable, not an implementation directive, and not approval for PyBroker, NautilusTrader, paper trading, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted here.

Related Alpha Strategy Pool families include cross-crypto information-diffusion / network-spillover research, but this record is preserved separately because the source, minute-level adaptive-LASSO specification, horizon, and execution assumptions are materially distinct.

## Sources

1. Guo, Li; Sang, Bo; Tu, Jun; Wang, Yu. "Cross-cryptocurrency return predictability." *Journal of Economic Dynamics and Control* 163 (2024), 104863. DOI: https://doi.org/10.1016/j.jedc.2024.104863
2. Singapore Management University InK public record / published working-paper version: https://ink.library.smu.edu.sg/lkcsb_research/6901
3. SSRN identifier associated with the SMU public record: https://doi.org/10.2139/ssrn.3974583
4. Weak negative evidence only, simplified public replication inspired by the paper: https://www.rlxbt.com/articles/sharpe-1073-still-untradeable-the-cross-crypto-experiment-gets-16-more-chances
