---
schema: strategy-research-record-v1
title: Bitcoin Option-Implied Risk-Neutral Density Low-Volatility / High-VRP Regime
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - options
  - variance-risk-premium
  - regime
status: research-only
confidence: medium
source_as_of: 2026-06-26
sources:
  - https://arxiv.org/abs/2410.15195
  - https://arxiv.org/html/2410.15195v2
  - https://ssrn.com/abstract=5374295
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - The source identifies regimes ex post using hierarchical clustering over the option-implied risk-neutral-density panel; a leakage-safe online regime classifier is not source-reported.
  - A higher variance risk premium in the low-volatility cluster does not by itself establish that a live short-volatility strategy earns superior net returns after tails, hedging costs, and execution frictions.
---

# Bitcoin Option-Implied Risk-Neutral Density Low-Volatility / High-VRP Regime

## Provenance

Primary public source:

- Caio Almeida, Maria Grith, Ratmir Miftachov, and Zijin Wang, **“Risk Premia in the Bitcoin Market,”** arXiv:2410.15195v2, last revised 2025-08-01.
- arXiv ID: `2410.15195`.
- arXiv DOI: `10.48550/arXiv.2410.15195`.
- Stable URLs: https://arxiv.org/abs/2410.15195 and https://arxiv.org/html/2410.15195v2.
- The later SSRN record uses the title **“Option-Implied Risk Premia and Cryptocurrency Market Regimes,”** dated 2026-06-26, SSRN abstract `5374295`, DOI `10.2139/ssrn.5374295`: https://ssrn.com/abstract=5374295.
- Source data: daily Bitcoin prices from 2014-01 through 2022-12 and transaction-level Deribit BTC options from 2017-07 through 2022-12. The source focuses on a 27-day investment horizon and constructs option-implied risk-neutral densities from Deribit options.

### Source-identity / duplication check

Repository-wide checks were performed for:

- arXiv ID `2410.15195`;
- SSRN ID `5374295`;
- exact source titles;
- authors Almeida / Grith / Miftachov / Wang;
- the distinctive mechanism: clustering full Bitcoin option-implied risk-neutral densities into high- and low-volatility regimes and comparing regime-conditional Bitcoin variance risk premia.

No existing repository record captured this source identity or this specific risk-neutral-density-cluster mechanism.

A related existing record, `crypto-options-volatility-risk-premium-zscore-2026-08-31.md`, uses a different public GitHub source and a trailing VRP z-score harvesting rule. This record is distinct because its source and central hypothesis are **option-implied risk-neutral-density regime classification and the counterintuitive finding that BVRP is higher in the low-volatility regime**, not a generic IV-minus-RV z-score rule.

## Economic mechanism

### Source-reported

The authors estimate daily Bitcoin option-implied risk-neutral densities and use functional-data hierarchical clustering to separate the sample into two dominant market regimes. The clusters are economically interpretable as high-volatility (HV) and low-volatility (LV) states; risk-neutral variance explains most of the cluster variation.

The source reports that Bitcoin variance risk premium (BVRP), defined from risk-neutral variance relative to physical realized variance, is **higher in the low-volatility cluster** than in the high-volatility cluster. The authors interpret the low-volatility state as one in which investors are relatively more concerned with variance and upside risk despite calmer observed volatility.

### Research interpretation

A falsifiable alpha hypothesis is that **option-implied distribution shape contains state information not captured by realized volatility alone**, and that calm-looking Bitcoin regimes can carry a richer variance-risk premium than turbulent regimes.

If this state dependence survives leakage-safe, rolling out-of-sample classification, it could inform when variance-selling exposure is more or less economically attractive. This does **not** imply that “low realized volatility = sell options.” The useful state variable is the option-implied risk-neutral distribution / regime, not realized volatility in isolation.

## Signal

### Source-reported

The paper does **not** provide a live trading entry/exit rule.

Its empirical regime construction is:

- estimate daily Bitcoin option-implied risk-neutral densities;
- use functional-data hierarchical clustering with an `L2`-based distance after mapping densities into a suitable function space;
- select two main clusters corresponding to HV and LV states;
- compare conditional Bitcoin premium and BVRP across those clusters.

Source-reported empirical classification evidence indicates that higher risk-neutral variance increases the probability of the HV cluster, while higher mean, skewness, and kurtosis are associated with the LV cluster. Variance alone explains most of the observed cluster variation.

### Research-proposed operationalization

Because the source clustering is not presented as a leakage-safe online trading classifier, any live rule below is **research-proposed**, not source-reported:

1. Build a daily fixed-maturity BTC risk-neutral density from contemporaneously available Deribit option data using only information available before the decision timestamp.
2. Fit regime classification on a rolling historical window only; never refit using future dates.
3. Classify the current observation into an LV-like or HV-like state from the option-implied density or a reduced-form approximation using risk-neutral moments.
4. Test whether a delta-hedged short-variance / short-vega basket entered in LV-like states has higher forward net risk-adjusted returns than the same exposure entered in HV-like states.
5. Treat this as a **state-conditioning hypothesis**, not a standalone directional BTC-return signal.

No source-reported threshold, option structure, strike selection, hedge frequency, sizing rule, stop, or holding rule is available. Any such choice is `research-proposed`.

## Required data

- Bitcoin spot/index history.
- Deribit BTC option transaction or quote data with timestamp, call/put type, strike, maturity, implied volatility / option price, and underlying price.
- Risk-free rate proxy for the relevant horizon.
- Fixed-maturity interpolation sufficient to reconstruct the option-implied risk-neutral density; the source emphasizes 27-day maturity and also uses 9-, 27-, and 45-day implied-volatility curves for clustering.
- Realized Bitcoin variance aligned to the same horizon.
- Point-in-time option availability and timestamps are mandatory for any live or OOS replication.
- 24/7 calendar and UTC settlement conventions must be handled explicitly.

## Execution assumptions

The paper is an asset-pricing / risk-premium study, not an execution study. Therefore the following are `underspecified`:

- exact tradable option basket;
- market vs limit execution;
- bid/ask spread and slippage model;
- delta-hedge instrument;
- delta-hedge frequency;
- vega / gamma exposure limits;
- margin and liquidation handling;
- funding / futures basis when futures are used for hedging;
- capacity and market impact.

For testing, all of these must be imposed explicitly and labeled `research-proposed`.

## Evidence

### Source-reported

The source uses Deribit BTC options from July 2017 through December 2022 and focuses on a 27-day horizon.

For the regime-conditional analysis, the source reports annualized values approximately as follows:

- overall BVRP: `0.14`;
- HV-cluster BVRP: `0.12`;
- LV-cluster BVRP: `0.17`;
- HV risk-neutral variance: `0.86`;
- HV physical variance: `0.74`;
- LV risk-neutral variance: `0.46`;
- LV physical variance: `0.29`.

The source reports 649 HV days and 368 LV days in the conditional sample and states that variance is the dominant variable separating the two clusters. It also reports that the low-volatility regime attributes a larger share of the Bitcoin premium to positive-return states.

These are source-reported estimates, not independently reproduced trading results.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Ex-post clustering risk:** the paper’s cluster construction is an empirical classification exercise over the sample. The source does not demonstrate that the same regime labels can be generated online without future information.
2. **Risk premium is not strategy PnL:** a larger BVRP does not guarantee superior realizable short-option returns after discrete hedging, convexity, jumps, spread, fees, liquidation risk, and margin constraints.
3. **Sample ends in 2022:** the evidence predates major later structural changes in crypto derivatives, including the growth of institutional BTC products and post-2024 spot ETF market structure.
4. **Single underlying / venue concentration:** the core options evidence is Bitcoin / Deribit-specific.
5. **Tail dependence:** an LV state may contain latent jump risk that is precisely why investors pay a larger variance premium; harvesting that premium can still produce rare severe losses.

## Falsification plan

1. Reconstruct the source-style 27-day risk-neutral-density panel using point-in-time Deribit data.
2. Split chronologically and fit regime classification only on the training history.
3. Compare a leakage-safe online density classifier against simpler baselines:
   - realized-volatility-only state;
   - BVIX / implied-variance-only state;
   - generic IV-minus-RV VRP z-score.
4. Measure forward delta-hedged option returns or variance-swap-equivalent PnL under identical execution assumptions in LV-like and HV-like states.
5. Include realistic fees, bid/ask, discrete hedging, futures funding/basis, margin, and crash scenarios.
6. Repeat on post-2022 data as a true structural OOS test.
7. Test whether the full density classifier adds incremental information beyond risk-neutral variance alone.

**Research-defined falsification threshold:** reject the useful-regime-alpha interpretation if, in post-2022 OOS testing, the LV-like state fails to deliver a statistically and economically higher net variance-selling premium than the HV-like state, or if the full-density classifier adds no robust incremental value over an implied-variance-only baseline after costs and multiple-testing controls.

## Crypto portability

`direct`

The source is already Bitcoin-options research using Deribit data. Portability beyond BTC is `unproven`.

Material crypto-specific risks:

- 24/7 trading and settlement boundaries;
- venue-specific option liquidity;
- Deribit concentration;
- inverse / linear hedge instrument choice;
- rapid changes in implied-volatility surface microstructure;
- funding and basis costs for perpetual/futures hedges;
- extreme jumps and liquidation risk.

## Limitations

- `underspecified`: no source-reported live signal threshold, option basket, sizing, holding, or hedge rule.
- `data gap`: the source sample ends in 2022.
- `unproven`: leakage-safe online clustering and post-2022 regime persistence are not established by the source.
- `unproven`: superior net PnL from selling variance specifically in the LV state is a research interpretation, not a source-reported backtest result.
- `not independently reproduced`.

## Implementation status

No implementation in PyBroker, Nautilus, or any other internal research/trading stack has been completed.

## Adoption boundary

This record is research material only.

Presence in this repository does **not** mean the hypothesis is profitable, independently validated, approved for implementation, approved for paper trading, approved for testnet, or approved for live trading.

## Related Wiki records

None identified. Do not fabricate Wiki links.

## Sources

1. Caio Almeida, Maria Grith, Ratmir Miftachov, Zijin Wang, **“Risk Premia in the Bitcoin Market,”** arXiv:2410.15195v2, revised 2025-08-01. https://arxiv.org/abs/2410.15195
2. Full public arXiv HTML used for data, methodology, and empirical-result verification: https://arxiv.org/html/2410.15195v2
3. Maria Grith, Caio Almeida, Ratmir Miftachov, Zijin Wang, **“Option-Implied Risk Premia and Cryptocurrency Market Regimes,”** SSRN abstract 5374295, version dated 2026-06-26. DOI `10.2139/ssrn.5374295`. https://ssrn.com/abstract=5374295
