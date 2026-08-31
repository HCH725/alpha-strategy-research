---
schema: strategy-research-record-v1
title: "Crypto Community-Network Inter-Crypto Momentum Spillover: Daily Quartile Long/Short"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cryptocurrency
  - network
  - cross-sectional
  - momentum-spillover
status: research-only
confidence: medium
source_as_of: 2018-12-31
sources:
  - "https://arxiv.org/abs/2108.11921"
  - "https://doi.org/10.1080/07350015.2022.2146695"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Community-Network Inter-Crypto Momentum Spillover: Daily Quartile Long/Short

## Provenance

Primary source: Li Guo, Wolfgang Karl Härdle, and Yubo Tao, *A Time-Varying Network for Cryptocurrencies*. Public arXiv version `2108.11921`, dated 2021-08-27; later published in the *Journal of Business & Economic Statistics*, 42(2), 437-456 (2024), DOI `10.1080/07350015.2022.2146695`.

The source uses historical daily prices, trading volumes, and contract/blockchain attributes from CryptoCompare for the top 400 cryptocurrencies by market capitalization as of 2018-12-31. The empirical sample spans 2016-01-01 through 2018-12-31; after excluding assets younger than one year or with incomplete price/contract information, 182 cryptocurrencies remain.

This record captures the source's inter-crypto momentum-spillover portfolio, not the entire dynamic clustering methodology as an implementation specification. The source's exact CASC tuning and production-grade reconstruction requirements remain complex and partially **underspecified** for direct deployment.

## Economic mechanism
### Source-reported

The authors argue that cryptocurrencies connected by return cross-predictability and technological similarity form latent communities through which information propagates. If information about one asset diffuses gradually to related assets, the contemporaneous returns of other members of the same community can predict the next-day return of a given cryptocurrency.

The source interprets the resulting long-short spread as momentum spillover associated with information propagation across economically/technologically related cryptocurrencies. It reports that the effect persists after splitting the sample by limit-to-arbitrage, investor-attention, and policy-uncertainty proxies.

### Research interpretation

The falsifiable alpha hypothesis is a **network-conditioned cross-sectional lead/lag effect**: a cryptocurrency should have a higher next-day expected return when the other members of its current latent community experienced stronger same-day returns, and a lower next-day expected return when its peers experienced weaker returns.

The alpha object is therefore not ordinary own-price momentum. It depends on a dynamically estimated peer set. A useful ablation is to compare the network-conditioned signal against simple market, sector/category, and own-return momentum baselines.

## Signal

Source-normalized portfolio rule:

1. **Community estimation:** estimate time-varying crypto communities using the paper's dynamic covariate-assisted spectral clustering (CASC) framework. The network combines return cross-predictability with technological covariates.
2. **Return-predictability network:** for each cryptocurrency, the source forms linkages by regressing current returns on other cryptocurrencies' lagged returns over a 360-day rolling window using adaptive Lasso.
3. **Trading signal at day t:** for each cryptocurrency `i`, compute the average same-day return of all *other* cryptocurrencies in its current community:
   `signal_i,t = mean(r_j,t for j in same community as i, j != i)`.
4. **Cross-sectional sort:** rank cryptocurrencies into four quartiles by this peer-return signal.
5. **Long leg:** equal-position long the top quartile ("winner" group).
6. **Short leg:** equal-position short the bottom quartile ("loser" group).
7. **Entry timing:** source states positions are established at the end of day `t` after signal formation.
8. **Holding / rebalance:** rebalance at the end of the next trading day; canonical tested horizon is one day. The source also examines returns up to seven days after signal formation.
9. **Position sizing:** equal positions within the long and short legs.
10. **Re-entry:** daily re-sort and rebalance from the latest community-conditioned peer-return signal.

The quartile and one-day holding rules are source-specified. Exact executable end-of-day price convention, exchange mapping, short instrument selection, and live community-update mechanics are **underspecified** and must not be invented.

## Required data

- Daily cryptocurrency returns and prices.
- Point-in-time cryptocurrency universe and market-cap ranking.
- At least 360 days of lagged return history for the adaptive-Lasso cross-predictability network.
- Blockchain / contract attributes required by the source's community model, including algorithm, proof type, age, total coins, and related technological covariates.
- Point-in-time technology metadata; stale current metadata is not an acceptable substitute for historical characteristics.
- Market-cap and listing history sufficient to avoid survivorship bias.
- For executable validation: venue-specific prices, spreads, fees, shortability/borrow or perpetual-contract availability, funding, and delisting history.
- Consistent daily timestamp / timezone convention.

## Execution assumptions

The academic portfolio is a cross-sectional research construct. The source reports equal-position winner/loser portfolios and end-of-day daily rebalancing but does not provide a production execution model.

Material omitted or unresolved assumptions include:

- same-close versus next-tradable-price execution around the end-of-day signal timestamp;
- taker/maker fees and bid-ask spread;
- slippage and market impact;
- short availability / borrow cost for spot implementations;
- funding and mark/index mechanics for perpetual-futures adaptations;
- partial fills, delistings, venue outages, and liquidity constraints;
- capacity for small historical assets.

Any modern implementation must lag community labels and all features strictly to information available before the trade to prevent look-ahead leakage.

## Evidence
### Source-reported

The source reports that the winner-minus-loser portfolio earns an average **1.08% one-day-ahead return** with a Newey-West t-statistic of **12.24** over 2016-01-01 to 2018-12-31. The reported winner and loser one-day-ahead returns are approximately 1.14% and 0.06%, respectively.

The source also examines days 2 through 7 after signal formation. The large spread is concentrated in the first day; subsequent daily winner-minus-loser spreads are much smaller and mixed in sign, while the authors state the initial effect does not fully reverse over the following week.

The source reports that the momentum-spillover result remains present across high/low subsamples of behavioral proxies such as limit-to-arbitrage, investor attention, and economic-policy uncertainty, which the authors use to argue for an information-propagation interpretation.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independent modern-sample replication was identified in this Scout cycle. Absence of identified negative evidence is not evidence of robustness.

Important internal caution from the source is that the large spread is primarily a one-day effect; days 2-7 show much weaker and statistically insignificant incremental spreads. The sample ends in 2018 and predates the modern perpetual-dominated, highly institutionalized crypto market structure.

## Falsification plan

The hypothesis should be materially downgraded or rejected if:

1. A leakage-safe, point-in-time reconstruction of the network/community labels fails to produce monotonic next-day returns across peer-return quartiles.
2. The winner-minus-loser spread is not economically meaningful after realistic fees, spread, slippage, funding/borrow, and turnover.
3. The signal disappears in a modern untouched out-of-sample period.
4. A simple own-return momentum, market-beta, or static category/sector peer-return signal explains the result equally well or better.
5. Randomized or permuted community assignments produce similar spreads, indicating the dynamic network contributes little information.
6. The effect is driven by stale or illiquid prices, delisting bias, survivorship bias, or assets that were not realistically shortable/tradable.
7. Using only lagged information available before the close eliminates the source-reported one-day effect.

Required ablations should include: own-return momentum, market return, static technology groups, random communities, return-network-only communities, covariate-only communities, and liquidity-matched quartiles.

## Crypto portability

**Direct in concept, adapted in implementation.** The source itself studies cryptocurrencies, so the economic hypothesis is directly crypto-native. However, modern portability is unproven because the 2016-2018 universe, venue structure, asset metadata, and shorting environment differ materially from today's market.

A perpetual-futures implementation could improve shortability for liquid assets but changes the economics through funding, contract-listing selection, mark/index pricing, leverage, and a substantially narrower universe. It must be treated as an adaptation, not a replication.

## Limitations

- **Not independently reproduced.**
- **Data gap:** faithful reconstruction requires historical point-in-time technological metadata and universe membership, not only OHLCV.
- **Underspecified:** exact production mapping of the paper's dynamic CASC procedure, tuning choices, and live update cadence requires careful reconstruction from the full methodology/code.
- **Underspecified:** executable end-of-day fill convention and real shorting costs are not fully modeled in the source portfolio.
- The empirical sample ends in 2018 and may not generalize to current market structure.
- Top-400-by-2018-market-cap sampling can create selection/survivorship concerns for a live point-in-time interpretation.
- High daily turnover makes cost and capacity sensitivity central.
- The source-reported 1.08% is a gross academic portfolio result, not independently verified trading performance.

## Implementation status

No implementation or validation in PyBroker, NautilusTrader, paper trading, testnet, or live trading has been completed for this research record.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material only. Presence in the Alpha Strategy Pool does not mean the hypothesis is profitable, validated, approved for implementation, or approved for paper/testnet/live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain links are asserted. Concept-level clustering, consolidation, promotion, and Wiki Brain ingestion belong to a separate Reviewer workflow.

## Sources

1. Li Guo, Wolfgang Karl Härdle, Yubo Tao, *A Time-Varying Network for Cryptocurrencies*, arXiv:2108.11921, public version dated 2021-08-27: https://arxiv.org/abs/2108.11921
2. Guo, Härdle, Tao, *Journal of Business & Economic Statistics* 42(2), 437-456 (2024), DOI: https://doi.org/10.1080/07350015.2022.2146695
