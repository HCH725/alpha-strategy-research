---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Active-Address-to-Market-Cap Value Factor
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - value-factor
  - on-chain
  - active-addresses
  - fundamental
  - asset-pricing
status: research-only
confidence: high
source_as_of: 2026-06
sources:
  - https://doi.org/10.1287/mnsc.2024.05875
  - https://pubsonline.informs.org/doi/10.1287/mnsc.2024.05875
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Active-Address-to-Market-Cap Value Factor

## Provenance

Primary source:

- Lin William Cong, G. Andrew Karolyi, Ke Tang, and Weiyi Zhao. "Crypto Value, Factor Pricing, and Market Segmentation." *Management Science* (published online June 5, 2026).
- DOI: https://doi.org/10.1287/mnsc.2024.05875
- Informs URL: https://pubsonline.informs.org/doi/10.1287/mnsc.2024.05875

The study evaluates on-chain network fundamental data from IntoTheBlock combined with market price, trading volume, and market capitalization data from CoinMarketCap covering tokens traded across approximately 300 exchanges. The empirical sample spans 2017 through 2024, expanding from 353 to 1,742 cryptocurrency assets across multiple market cycles.

Related foundational literature:
- Lin William Cong and Yizhou Xiao. "Categories and functions of crypto tokens." *Handbook of Alternative Finance* (2021).
- Yukun Liu and Aleh Tsyvinski. "Risks and returns of cryptocurrency." *The Review of Financial Studies* 34, no. 6 (2021): 2689–2727. DOI: https://doi.org/10.1093/rfs/hhaa113.

## Economic mechanism

### Source-reported

Cong, Karolyi, Tang, and Zhao (2026) identify a significant "crypto value effect" in digital assets using the ratio of active addresses to market capitalization ($AA/MC$) as a proxy for fundamental intrinsic value. Because cryptocurrencies lack traditional corporate cash flows, dividends, or book equity, on-chain network activity (measured by unique active wallet addresses participating in transactions) serves as the primary metric of organic platform adoption and utility.

The authors construct a novel four-factor pricing model:
1. Crypto Market Factor ($MKT_{crypto}$)
2. Crypto Size Factor ($SMB_{crypto}$)
3. Crypto Momentum Factor ($MOM_{crypto}$)
4. Crypto Value Factor ($HML_{crypto}$ or $V_{crypto}$, based on $AA/MC$)

The source reports that this four-factor model explains the cross-section of cryptocurrency return variations significantly better than standard benchmark models. The authors propose that the crypto value premium reflects compensation for bearing "on-chain activity risk" (uncertainty regarding user adoption and network utility persistence) rather than pure behavioral mispricing. Additionally, the paper documents significant market segmentation across token functionality categories (General Payment Tokens, Platform Tokens, Product Tokens, and Security Tokens), where characteristic return sensitivities differ across segments.

### Research interpretation

The falsifiable hypothesis is that **cryptocurrency tokens with high on-chain user activity relative to their market valuation ($AA/MC$) represent fundamentally undervalued networks that systematically outperform low $AA/MC$ "glamour/growth" tokens**:

1. **Fundamental Network Anchoring**: Market prices frequently dislocate from network usage due to speculative hype or retail attention cycles. Tokens exhibiting dense transactional activity relative to market cap experience mean-reverting valuation adjustments as platform utility provides a floor.
2. **On-Chain Risk Compensation**: Holding high $AA/MC$ assets exposes investors to protocol-level adoption dynamics and network operational risk, for which a positive expected return premium is required.
3. **Cross-Sectional Factor Architecture**:
   - Long leg: Top quintile / decile of tokens ranked by $AA/MC$ (high fundamental value).
   - Short leg: Bottom quintile / decile of tokens ranked by $AA/MC$ (speculative glamour / high market cap with low organic network adoption).

## Signal

Normalized source-faithful portfolio signal:

1. **Fundamental Value Ratio ($AA/MC_{i,t}$)**:
   $$AA/MC_{i,t} = \frac{\overline{\text{ActiveAddresses}}_{i, [t-7, t]}}{\text{MarketCap}_{i,t}}$$
   where $\overline{\text{ActiveAddresses}}_{i, [t-7, t]}$ is the trailing 7-day average of unique daily active on-chain sending and receiving addresses for token $i$, and $\text{MarketCap}_{i,t} = P_{i,t} \times \text{CirculatingSupply}_{i,t}$.
2. **Cross-Sectional Ranking**:
   - Filter universe to liquid tokens with valid on-chain active address tracking and minimum trading volume threshold.
   - Sort tokens cross-sectionally at rebalance timestamp $t$ into quintiles ($Q_1$ to $Q_5$) or deciles ($D_1$ to $D_{10}$) based on $AA/MC_{i,t}$.
3. **Portfolio Construction**:
   - **Long Leg ($Q_5$ / High Value)**: Equal-weighted (EW) or value-weighted (VW) basket of top quintile tokens.
   - **Short Leg ($Q_1$ / Low Value)**: Equal-weighted (EW) or value-weighted (VW) basket of bottom quintile tokens.
   - **Spread Portfolio**: High-minus-Low ($HML_{crypto} = Q_5 - Q_1$).
4. **Rebalance Frequency**: Weekly (7-day holding horizon).

Operational parameters regarding specific volume screening cutoffs and multi-chain address aggregation rules not fully articulated in the summary remain **underspecified** and require parameter tuning in backtest simulation.

## Required data

- **On-Chain Fundamental Data**: Daily unique active wallet addresses per asset from IntoTheBlock, Glassnode, Artemis, or Dune Analytics.
- **Market Data**: Daily and weekly OHLCV, circulating token supply, and market capitalization across centralized and decentralized venues from CoinMarketCap, CoinGecko, or Kaiko.
- **Token Classification**: Categorization into functionality segments (General Payment, Platform/L1/L2, DeFi/Product, Security) to control for structural segmentation.
- **Point-in-Time Availability**: Strictly synchronized timestamps ensuring active address data is finalized on-chain prior to portfolio formation.

## Execution assumptions

- Weekly portfolio rebalancing at 00:00 UTC.
- Signal-to-order timing: Execution on the next candle open ($t+1$) following on-chain address confirmation.
- Order types: Limit orders or TWAP market orders over the rebalance window.
- Trading costs: Standard spot/perpetual maker/taker fees (e.g. 5–10 bps) and short-borrow financing rates for low $AA/MC$ short positions.

## Evidence

### Source-reported

- Evaluated across a dataset of 353 to 1,742 crypto assets spanning 2017 to 2024.
- Weekly long-short portfolios sorted on the active-addresses-to-market-cap ratio ($AA/MC$) produce:
  - **Equal-Weighted (EW) Excess Return**: **2.4% per week** with a $t$-statistic of **3.77**.
  - **Value-Weighted (VW) Excess Return**: **1.3% per week** with a $t$-statistic of **2.48**.
- The four-factor asset pricing model ($MKT$, $SMB$, $MOM$, $HML_{crypto}$) significantly outperforms standard CAPM and 3-factor models in pricing cross-sectional crypto assets and reducing GRS test pricing errors.
- The value premium remains statistically significant after controlling for market capitalization, past return momentum, and market segmentation classes.

All quantitative figures above are **source-reported** by Cong et al. (*Management Science*, 2026) and have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the primary reviewed source; absence is not evidence of no negative result.

Potential failure modes and empirical frictions:
- **Sybil / Wash Activity Vulnerability**: On-chain active address counts can be artificially manipulated via bot scripts, micro-transactions, or airdrop farming campaigns, inflating apparent $AA/MC$ ratios for worthless tokens.
- **Multi-Chain & Layer-2 Fragmentation**: Tokens operating across multiple bridges, L2s, and rollups may exhibit fragmented or uncounted address activity if data indexers capture only mainnet contracts.
- **Short Leg Borrow Constraints**: Shorting low $AA/MC$ speculative tokens often incurs high borrow fees or liquidation risk during irrational meme/momentum rallies.

## Falsification plan

The hypothesis should be weakened or rejected if an independent point-in-time backtest demonstrates:

1. The $AA/MC$ long-short spread fails to achieve statistical significance ($t < 2.0$) on out-of-sample data (2024–2026) or when evaluated net of realistic trading fees and borrow costs.
2. Sybil-filtered active address data (e.g., filtering out zero-balance or micro-value transacting addresses) eliminates the cross-sectional return spread.
3. The value factor is entirely subsumed by simple liquidity or size factors ($SMB$) in multi-factor spanning regressions.

## Crypto portability

**Direct**, as the factor is designed specifically for crypto assets using blockchain-native on-chain wallet activity to replace traditional corporate book value.

## Limitations

- **Not independently reproduced.**
- **Data Vendor Dependency**: Relies on standardized on-chain data indexers (e.g., IntoTheBlock); discrepancies in address counting algorithms between vendors can create signal divergence.
- **underspecified:** Exact rules for handling multi-chain token contracts and minimum liquidity exclusion thresholds are not exhaustively specified in the publication text.
- **Execution Cost Drag**: Weekly rebalancing of a broad cross-section across hundreds of altcoins entails significant turnover and transaction cost friction.

## Implementation status

No implementation in our research stack has been completed.

## Adoption boundary

Research material only.

A record being present in this repository does **not** mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

## Related Wiki records

- `[[quant/crypto-cross-sectional-onchain-user-activity-growth-2026-08-31]]`
- `[[quant/crypto-cross-sectional-size-factor-smb-2026-08-31]]`
- `[[quant/crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31]]`
- `[[quant/crypto-cross-sectional-double-sorted-anomaly-interactions-2026-09-01]]`

## Sources

- Lin William Cong, G. Andrew Karolyi, Ke Tang, and Weiyi Zhao, "Crypto Value, Factor Pricing, and Market Segmentation", *Management Science* (published online June 5, 2026). DOI: https://doi.org/10.1287/mnsc.2024.05875. URL: https://pubsonline.informs.org/doi/10.1287/mnsc.2024.05875.
- Lin William Cong and Yizhou Xiao, "Categories and functions of crypto tokens", *Handbook of Alternative Finance* (2021).
- IntoTheBlock On-Chain Fundamental Data Analytics: https://www.intotheblock.com/.
