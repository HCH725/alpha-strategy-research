---
schema: strategy-research-record-v1
title: "Crypto World Order Flow Cross-Sectional Quintiles: Weekly High-minus-Low"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cryptocurrency
  - order-flow
  - cross-sectional
  - market-microstructure
status: research-only
confidence: high
source_as_of: 2026-01
sources:
  - "https://doi.org/10.1016/j.finmar.2026.101047"
  - "https://www.efmaefm.org/0EFMAMEETINGS/EFMA%20ANNUAL%20MEETINGS/2025-Greece/papers/OrderFlowpaper.pdf"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto World Order Flow Cross-Sectional Quintiles: Weekly High-minus-Low

## Provenance

Primary source: Alexia Anastasopoulos, Nikola Gradojevic, Fred Liu, Alex Maynard, and Ilias Tsiakas, *Order flow and cryptocurrency returns*, Journal of Financial Markets 79 (2026), article 101047, DOI `10.1016/j.finmar.2026.101047`.

A public November 2024 working-paper version is available from the European Financial Management Association. The published article reports a cross-section of 84 cryptocurrencies over 2018-01-01 to 2022-06-30, with the out-of-sample portfolio-sort period running from 2020-02-18 to 2022-06-30.

Price data are from CoinMarketCap. Signed buyer-initiated and seller-initiated volume used to construct order flow are from CryptoCompare, aggregated from more than 300 exchanges and denominated in 11 fiat currencies: USD, EUR, GBP, JPY, CHF, CAD, AUD, NZD, NOK, SEK, and KRW.

This record normalizes the paper's directly reported **weekly cross-sectional world-order-flow quintile sort**, rather than its more complex machine-learning forecast strategies.

## Economic mechanism
### Source-reported

The authors frame order flow as net demand that can contain both a transitory component associated with short-term price pressure/reversal and a permanent component associated with information and price discovery. They find that lagged world order flow predicts future cryptocurrency returns after controlling for lagged returns, and interpret the positive relation as evidence for a permanent component of order flow.

The paper argues that global rather than purely domestic order flow is especially informative because cryptocurrency trading is fragmented across countries, fiat pairs, and independently operated venues.

### Research interpretation

The falsifiable mechanism is cross-sectional information diffusion through signed global trading demand. Coins receiving stronger net buyer-initiated flow across major fiat trading channels should subsequently outperform coins receiving weaker or negative net flow, provided the signal is not merely contemporaneous price pressure already captured by recent returns.

The orthogonalized version explicitly attempts to isolate the order-flow component not explained by same-period returns. If the effect is genuine price discovery rather than temporary pressure, the residualized flow rank should retain positive next-period predictive power.

## Signal

Source-normalized weekly specification:

1. **Universe construction:** begin with cryptocurrencies having market capitalization above USD 1 million on the first sample date, require continuous trading with non-zero price and volume throughout the source sample, and exclude stablecoins. The paper's resulting balanced panel contains 84 coins. This static historical eligibility rule is source-specific and creates survivorship-selection concerns for modern reuse.
2. **Weekly interval:** source weekly returns run from Saturday 00:00 GMT through Friday 23:59 GMT.
3. **Raw world order flow for coin `i` at week `t`:** aggregate buyer-initiated volume across all 11 fiat denominations into `Buy^W_{i,t}` and seller-initiated volume into `Sell^W_{i,t}`; compute the raw log-difference order flow `of^W_{i,t} = log(Buy^W_{i,t}) - log(Sell^W_{i,t})`.
4. **Standardization:** divide raw world order flow by its trailing 30-observation order-flow volatility, following the source's daily formula `OF_{i,t} = of_{i,t} / sigma(of_{i,t-29:t})`. The reviewed source states that the same standardization is used for world order flow. For a strictly weekly reconstruction, the exact mapping of the 30-observation window to weekly aggregation should be verified against source code/appendix before claiming exact replication; mark this detail as **underspecified**.
5. **Orthogonalization:** at each weekly rebalance date `t`, recursively regress lagged standardized world order flow on lagged returns using an expanding window containing information available only through `t`. Define `ortho-OF^W_{i,t}` as the latest residual. The source explicitly states this expanding-window construction to avoid forward-looking bias.
6. **Cross-sectional rank:** rank all eligible coins by lagged `ortho-OF^W` from lowest to highest.
7. **Portfolio formation:** split the cross-section into five quintiles. `P1` contains the lowest lagged orthogonalized world order flow and `P5` the highest.
8. **Weights:** equal-weight constituents within each quintile.
9. **Long entry:** long `P5` at the weekly rebalance.
10. **Short entry:** short `P1` at the weekly rebalance.
11. **Holding period:** one week.
12. **Exit/rebalance:** close or rebalance at the next weekly formation point and recompute the ranking.
13. **Portfolio return:** `R_LS,t+1 = R_P5,t+1 - R_P1,t+1`.

The paper also reports a raw, non-orthogonalized world-order-flow sort. That variant is not merged into the focal signal because the orthogonalized construction better separates the permanent-flow hypothesis from short-term return reversal.

## Required data

- **Instrument/universe:** source-faithful reproduction requires the historical 84-coin balanced panel or a clearly documented point-in-time modern analogue.
- **Market type:** underlying return series are aggregated cryptocurrency prices; the source does not specify a single executable venue/instrument for each coin.
- **Price source:** CoinMarketCap daily USD prices sampled at 00:00 GMT in the source.
- **Order-flow source:** CryptoCompare signed buy-volume and sell-volume by fiat denomination, aggregated from more than 300 exchanges.
- **Fiat channels:** USD, EUR, GBP, JPY, CHF, CAD, AUD, NZD, NOK, SEK, KRW.
- **Fields:** per-coin buyer-initiated volume and seller-initiated volume by fiat, prices, returns, market capitalization, total volume, stablecoin classification, trading-availability history.
- **Timeframe:** daily source data aggregated to weekly intervals for the focal strategy.
- **Timestamp:** GMT; weekly interval Saturday 00:00 through Friday 23:59.
- **Point-in-time:** expanding-window orthogonalization must use only information available at each rebalance. Modern universe construction should be point-in-time rather than imposing the source's full-sample continuous-trading requirement.
- **Missing data:** the source's balanced-panel construction excludes coins without continuous non-zero observations; it does not provide a general imputation rule.
- **Data gap:** a modern implementation needs signed aggressor-side volume across multiple fiat venues or a defensible substitute. Standard OHLCV alone is insufficient.

## Execution assumptions

The source evaluates equal-weight portfolio returns rather than a single-venue executable basket, so several live execution details remain **underspecified**.

- **Signal-to-order timing:** ranking uses lagged information and evaluates next-period returns, which prevents direct look-ahead in the reported portfolio test. Exact executable timestamp after the Friday period close is not specified.
- **Order type:** underspecified.
- **Fill model:** underspecified.
- **Shorting:** the focal long-short strategy assumes the bottom-quintile coins can be shorted. The paper explicitly notes that this may be difficult or impossible for some cryptocurrencies.
- **Fees/spread/slippage:** no single fixed cost is deducted from the Table 11 weekly world-order-flow portfolio. The broader paper evaluates break-even transaction costs for ML-based portfolios and cites realistic crypto costs around 0.3%-0.5% in prior literature; these are context, not a verified cost model for this exact weekly signal.
- **Impact/capacity:** underspecified.
- **Leverage/margin/borrow:** underspecified and material for the short leg.
- **Venue fragmentation:** source returns and signed flow aggregate across many venues, whereas execution would occur on specific spot, margin, futures, or perpetual venues. This mismatch must be modeled in reproduction.

## Evidence
### Source-reported

For the weekly portfolios sorted on **orthogonalized world order flow**, Table 11 reports a high-minus-low (`P5-P1`) mean return of **1.83% per week**, Newey-West t-statistic **2.82**, three-factor alpha **1.72% per week** with t-statistic **2.71**, and annualized Sharpe ratio **1.93** over the out-of-sample period 2020-02-18 to 2022-06-30.

For the non-orthogonalized weekly world-order-flow sort, the paper reports a `P5-P1` mean return of **1.93% per week**, alpha **1.78%**, and annualized Sharpe ratio **2.05**. The similarity of raw and orthogonalized weekly results is consistent with the paper's finding that recent-return reversal matters more at the daily horizon than at the weekly horizon.

The authors additionally report that order-flow predictive relations remain meaningful in the top-10-coin subset and that order-flow-based machine-learning forecasts outperform models based on economic fundamentals. Those ML results are supporting evidence for the broader mechanism but are not the trading rule normalized in this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The daily raw world-order-flow quintile spread is weak: Table 11 reports only about **0.02% per day** for `P5-P1`, with an annualized Sharpe ratio of **0.11**. Daily performance improves only after orthogonalizing flow against lagged returns, indicating that short-horizon price pressure/reversal can mask or offset the predictive component.

The source's 84-coin universe is a balanced panel requiring continuous trading over the full historical sample. That is not a point-in-time investable universe rule and can introduce survivorship and selection bias if copied mechanically.

The main signed-flow dataset is vendor-specific and aggregated across hundreds of exchanges. Modern reproducibility depends on continued access to equivalent aggressor-side volume by fiat currency; a single-exchange OHLCV substitute does not reproduce the source signal.

The source does not establish live capacity, borrow availability, or exact execution costs for the weekly long-short world-order-flow portfolio.

## Falsification plan

The hypothesis should be materially weakened or rejected if a leakage-safe modern reproduction shows any of the following:

1. Cross-sectional next-week returns are not monotonically increasing with lagged orthogonalized world-order-flow rank.
2. The `P5-P1` spread is not positive out of sample across multiple non-overlapping regimes.
3. The effect disappears when the historical balanced-panel universe is replaced with a genuinely point-in-time investable universe.
4. The effect is driven entirely by a few illiquid coins, fiat regions, or exchanges and vanishes in large/liquid-coin subsets.
5. Removing USD or KRW flow, which the source identifies as dominant contributors to world-flow variation, causes instability inconsistent with a broad global-flow mechanism.
6. The spread does not survive realistic spot/perpetual borrow, funding, maker/taker fees, spread, slippage, and turnover costs using executable venue-specific instruments.
7. Orthogonalization provides no incremental information beyond standard momentum/reversal, volume, liquidity, and volatility controls in modern data.
8. A simple random-rank or lagged-return control portfolio performs similarly after costs.

Ablation should compare raw `OF^W`, orthogonalized `OF^W`, USD-only flow, KRW-only flow, recent return, volume, and momentum ranks.

## Crypto portability

**Direct in mechanism, adapted in implementation.**

The alpha thesis is crypto-native and directly based on cryptocurrency signed order flow. However, the source signal depends on globally aggregated multi-fiat signed volume, while a deployable modern system may have only venue-specific trade/aggressor data or perpetual-market flow.

A Binance-only or perpetual-only implementation would therefore be an adaptation, not a source-faithful replication. Perpetual trade flow may include leverage, liquidation, funding, and market-maker effects absent from aggregate spot-style signed volume. The 24/7 market also makes exact weekly boundaries and causal signal availability important.

## Limitations

- **Not independently reproduced.**
- **Data gap:** requires historical signed buyer/seller volume by multiple fiat currencies; OHLCV alone is insufficient.
- **Underspecified:** exact weekly application of the source's trailing 30-observation order-flow standardization should be verified before exact replication.
- **Underspecified:** executable signal-to-order timestamp, order type, fill model, borrow, and venue mapping.
- **Survivorship/selection risk:** source universe requires continuous trading throughout the full sample.
- **Unproven:** persistence beyond 2022-06-30 under materially different market structure.
- **Unproven:** single-venue and perpetual-futures adaptations.
- Aggregated vendor data may conceal exchange-specific microstructure and timestamp differences.

## Implementation status

No implementation or validation in PyBroker, NautilusTrader, paper trading, testnet, or live trading has been completed for this research record.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material only. It is not proof that the order-flow premium persists, not authorization to acquire vendor data or modify the data pipeline, and not approval for implementation, paper trading, testnet, or live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain links are asserted in this staging record. Concept-level clustering and Wiki promotion belong to the separate downstream Reviewer workflow.

## Sources

1. Alexia Anastasopoulos, Nikola Gradojevic, Fred Liu, Alex Maynard, Ilias Tsiakas, *Order flow and cryptocurrency returns*, Journal of Financial Markets 79 (2026), 101047: https://doi.org/10.1016/j.finmar.2026.101047
2. Public working-paper version, EFMA, November 2024: https://www.efmaefm.org/0EFMAMEETINGS/EFMA%20ANNUAL%20MEETINGS/2025-Greece/papers/OrderFlowpaper.pdf
