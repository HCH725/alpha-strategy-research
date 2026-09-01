---
schema: strategy-research-record-v1
title: "Bitcoin CME COT Trader-Position Sentiment Futures Risk Premium"
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - futures
  - cme
  - cot
  - positioning
  - sentiment
status: research-only
confidence: medium
source_as_of: 2021-06-29
sources:
  - https://doi.org/10.1002/fut.22373
  - https://onlinelibrary.wiley.com/doi/10.1002/fut.22373
  - https://www.researchgate.net/figure/Level-of-net-positions-TFF-data-The-dynamics-of-weekly-net-position-levels-without_fig2_362843237
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin CME COT Trader-Position Sentiment Futures Risk Premium

## Provenance

- **Primary source:** Shimeng Shi (2022), "Bitcoin futures risk premia," *Journal of Futures Markets*, 42(12), 2190-2217.
- **DOI:** `10.1002/fut.22373`.
- **Version of record:** first published online 2022-08-22; accepted 2022-07-22.
- **Primary market:** regulated CME Bitcoin futures.
- **Primary public positioning data:** U.S. Commodity Futures Trading Commission Commitments of Traders (COT) / Traders in Financial Futures (TFF) reports.
- **Source/data as-of:** a publicly exposed figure from the paper shows weekly TFF net-position data through 2021-06-29 and a displayed period beginning 2018-04-10. The article also states that CFTC data from 2018-2021 were used. Treat the exact full-sample boundaries for every regression as `underspecified` unless verified from the full article tables.
- **Source-identity check:** repository search on 2026-09-01 found no existing record containing DOI `10.1002/fut.22373`, the exact paper title, COT/TFF terminology, or the same trader-position/sentiment mechanism. This is not a reframing of an already captured source.

## Economic mechanism

### Source-reported

Shi studies Bitcoin futures risk premia using position-based measures, market-microstructure variables, and macroeconomic predictors. The paper reports that trading activity and **extreme sentiment of speculators and retailers** have significant predictive power for subsequent Bitcoin futures price changes over multiple horizons. It further reports that speculators behave like **negative-feedback traders**, while retailers behave like **positive-feedback traders**. The return effect of changes in hedger net positions may depend on extreme macroeconomic states.

The public TFF figure associated with the paper defines weekly normalized net position for trader type `j` as:

`NP_t^j = (Long_t^j - Short_t^j) / OI_t`

and displays dealer/intermediary, asset manager/institutional, leveraged-fund, and other-reportable categories.

### Research interpretation

The falsifiable hypothesis is that **who is carrying the directional futures position matters for the subsequent CME Bitcoin futures risk premium**. Extreme positioning by trader groups may proxy for heterogeneous information, inventory pressure, trend chasing, or contrarian liquidity provision.

A plausible interpretation of the source-reported feedback behavior is:

- trader groups exhibiting positive-feedback behavior may amplify recent price moves and create crowded continuation/exhaustion states;
- trader groups exhibiting negative-feedback behavior may absorb price pressure and encode contrarian positioning;
- the predictive relation may be state-dependent rather than monotonic, because the source specifically emphasizes **extreme sentiment** rather than merely the sign of net positioning.

This interpretation is a research hypothesis, not a verified trading rule.

## Signal

### Source-reported specification

- **Frequency:** weekly CFTC positioning data.
- **Position variable:** normalized trader-group net positions, with the publicly displayed TFF formula `NP_t^j = (Long_t^j - Short_t^j) / OI_t`.
- **Predictive target:** subsequent Bitcoin futures price changes / futures risk premia over multiple horizons.
- **Key conditioning variables:** trading activity; extreme sentiment of speculators and retailers; hedger net-position changes; macroeconomic variables.
- **Exact sentiment construction:** `underspecified` in the public abstract/figure material reviewed in this Scout cycle.
- **Exact threshold defining "extreme":** `underspecified`.
- **Exact mapping from the article's labels "speculators" and "retailers" to every COT/TFF reporting category:** `underspecified` in the public material reviewed here.
- **Exact forecast horizons, coefficient signs by horizon, and portfolio implementation:** `underspecified` unless verified from the article tables.

### Research-proposed operationalization

For testability only, and **not source-reported**, a future reproduction should:

1. ingest point-in-time weekly CME Bitcoin futures COT/TFF reports using their publication timestamps;
2. compute each reported trader group's normalized net position exactly as above;
3. reproduce the source's original trader-group mapping and extreme-sentiment definition from the full paper before any trading interpretation;
4. test subsequent CME Bitcoin futures returns at the exact source horizons;
5. only after reproduction, evaluate whether extreme positioning can be transformed into a directional or regime signal.

No 1-sigma, percentile, z-score, holding-period, stop, leverage, or sizing threshold is introduced here because the source specification has not yet been fully recovered.

## Required data

- CME Bitcoin futures continuous-contract or contract-level prices.
- CFTC COT and/or TFF weekly reports with:
  - long contracts by trader category;
  - short contracts by trader category;
  - total open interest;
  - report date;
  - **actual publication timestamp** for leakage-safe use.
- Contract roll information for CME Bitcoin futures.
- Trading activity / liquidity variables used by the source; exact definitions are `underspecified` in the reviewed public extract.
- If reproducing macro-state interactions: the source names NFCI, TED spread, U.S. M2, funding costs of financial institutions, and other macro variables.
- Bloomberg-sourced fields used in the original study may be license-restricted; a public reproduction must document substitutions rather than copying restricted data.

## Execution assumptions

- COT/TFF observations must not be treated as known on the report date before their actual public release. A leakage-safe test enters only after the corresponding CFTC release is observable.
- Futures rolls, bid-ask spread, commissions, slippage, and margin usage must be modeled explicitly.
- Same-close execution on data that became public after that close is prohibited.
- The source is an empirical predictor study, not a fully specified executable strategy; order type, position sizing, leverage, exits, and roll procedure are `underspecified`.
- A crypto-perpetual translation would require a separate portability test because CME trader classifications do not exist directly on Binance/Bybit/OKX perpetual markets.

## Evidence

### Source-reported

The peer-reviewed article reports that:

- trading activity and extreme sentiment of speculators and retailers predict subsequent Bitcoin futures price changes over different horizons;
- lower transaction costs are associated with higher Bitcoin futures risk premia;
- financial conditions, TED spread, U.S. M2, and institutional funding-cost variables can predict Bitcoin futures returns;
- the return impact of hedger net-position changes may depend on extreme macroeconomic conditions;
- speculators behave like negative-feedback traders, while retailers behave like positive-feedback traders.

The publicly exposed TFF figure shows normalized net positions for dealer/intermediary, asset manager/institutional, leveraged-fund, and other-reportable groups over 2018-04-10 to 2021-06-29 and states the normalization formula used above.

No precise coefficient, t-statistic, Sharpe ratio, or trading return is recorded here because those figures were not traceable from the public material reviewed in this run.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- No independent replication was identified in the sources reviewed during this cycle.
- The sample largely reflects the early institutionalization period of CME Bitcoin futures; trader composition, ETF adoption, basis structure, and market microstructure changed materially after 2021.
- Weekly COT/TFF data are delayed public reports, so any apparent predictability is vulnerable to look-ahead bias if report dates are confused with publication timestamps.
- The public abstract does not expose the exact extreme-sentiment thresholds or full horizon-by-horizon coefficient structure, so an executable signal cannot be faithfully reconstructed from the abstract alone.
- CFTC trader classifications are specific to regulated futures reporting and may not map cleanly to crypto-native perpetual venues.

## Falsification plan

1. Reproduce the paper's exact trader-category mapping, sentiment construction, transformations, and forecast horizons from the full article.
2. Build a point-in-time CFTC release calendar and reject any result that relies on data before public availability.
3. Replicate the original 2018-2021 sample first, then conduct a strict post-2021 out-of-sample test through the latest available period.
4. Compare trader-position predictors against baselines using only lagged BTC return, open interest, volume, basis, and realized volatility.
5. Test whether predictive content survives futures roll costs, commissions, spread, and conservative slippage.
6. Test structural stability before and after major regime changes including U.S. spot Bitcoin ETF launch and the expansion of institutional derivatives participation.
7. **Research-defined falsification threshold:** reject the operational alpha hypothesis if the source-direction predictive relation fails to remain statistically and economically distinguishable from the baseline in leakage-safe post-2021 OOS data after costs. No numeric Sharpe/t-stat cutoff is imposed at Scout stage.

## Crypto portability

direct for CME Bitcoin futures; adapted/unproven for crypto-native perpetuals.

The empirical source is already Bitcoin-futures-specific, so no cross-asset portability assumption is needed for CME reproduction. Translation to perpetual futures is not direct because:

- trader identities/categories are not disclosed through CFTC-style reports;
- perpetual funding creates an additional carry channel;
- venues trade 24/7 while CFTC data are weekly;
- leverage, liquidation, and offshore venue composition differ materially from CME.

## Limitations

- not independently reproduced
- exact sentiment threshold: `underspecified`
- exact trader-label mapping for "speculator" and "retailer": `underspecified` in the public extract reviewed
- exact horizon-by-horizon coefficients: `data gap`
- executable entry/exit and sizing rules: `underspecified`
- post-2021 structural stability: `unproven`
- some original market data were Bloomberg-licensed, so public reproduction may require documented substitutes

## Implementation status

not-implemented

No PyBroker, NautilusTrader, paper, testnet, or live implementation has been created or requested by this Scout record.

## Adoption boundary

This record is research material only. Presence in the Alpha Strategy Pool does not mean the hypothesis is profitable, independently validated, approved for implementation, approved for paper/testnet/live trading, or approved for Wiki Brain ingestion.

## Related Wiki records

No stable Hermes Wiki Brain links were identified or created in this Scout cycle.

## Sources

1. Shi, S. (2022). "Bitcoin futures risk premia." *Journal of Futures Markets*, 42(12), 2190-2217. DOI: https://doi.org/10.1002/fut.22373
2. Wiley Online Library article page / version-of-record metadata and abstract: https://onlinelibrary.wiley.com/doi/10.1002/fut.22373
3. Publicly exposed figure from the source article showing TFF net-position categories, normalization formula, and 2018-04-10 to 2021-06-29 period: https://www.researchgate.net/figure/Level-of-net-positions-TFF-data-The-dynamics-of-weekly-net-position-levels-without_fig2_362843237
4. CFTC Commitments of Traders landing page referenced by the article: https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm
