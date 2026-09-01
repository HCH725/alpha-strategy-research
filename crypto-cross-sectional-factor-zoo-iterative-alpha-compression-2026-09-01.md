---
schema: strategy-research-record-v1
title: "Crypto Factor Zoo Compression: Alpha-Based Iterative Factor Selection and Dominance of Liquidity Risk"
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - factor-zoo
  - spanning-tests
  - iterative-factor-selection
  - liquidity-risk
  - turnover-volatility
status: research-only
confidence: high
source_as_of: 2026-01
sources:
  - https://doi.org/10.1016/j.irfa.2026.105137
  - https://ideas.repec.org/a/eee/finana/v113y2026ics1057521926001258.html
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Factor Zoo Compression: Alpha-Based Iterative Factor Selection and Dominance of Liquidity Risk

## Provenance

- **Primary Academic Source:** Aleksander Mercik, Adam Zaremba, and Ender Demir, "Crypto factor zoo (.Zip)," *International Review of Financial Analysis*, Volume 113, 2026, Article 105137. DOI: [10.1016/j.irfa.2026.105137](https://doi.org/10.1016/j.irfa.2026.105137).
- **Bibliographic Record:** RePEc/IDEAS stable handle: https://ideas.repec.org/a/eee/finana/v113y2026ics1057521926001258.html.
- **Empirical Dataset:** 36 distinct return-predictive anomaly factors in cryptocurrency cross-sections evaluated across weekly rebalanced portfolios spanning 2018 through 2024.
- **Methodological Framework:** Adaptation of the alpha-based iterative factor selection algorithm developed by Swade, Nolte, Shackleton, and Zaremba (2024) to the cryptocurrency market.

## Economic mechanism

### Source-reported

Mercik, Zaremba, and Demir (2026) address the proliferation of cross-sectional return anomalies (the "factor zoo") in cryptocurrency markets:
1. **Factor Redundancy & Spanning:** Out of 36 candidate asset pricing and technical factors documented in prior literature, the vast majority are statistically spanned and economically redundant when tested against a core subset of benchmark factors.
2. **Parsimonious 2-to-3 Factor Core:** Applying the Swade et al. (2024) iterative alpha-minimization selection algorithm, the authors establish that just **two to three factors** are sufficient to eliminate all statistically significant pricing alphas across the remaining 33+ anomaly portfolios.
3. **Dominance of Liquidity Risk:** Liquidity-related variables heavily dominate the selection hierarchy. In particular:
   - **Turnover Volatility** (volatility of trading turnover);
   - **Bid-Ask Spread** (effective quoted spread / illiquidity);
   - **New-Address-to-Price Ratio** (blockchain-native network adoption metric);
   completely absorb and subsume classical price-only signals such as univariate momentum, short-term reversal, and size.
4. **Robustness Across Weighting Schemes:** The finding that 2–3 liquidity-centric factors span the cryptocurrency cross-section holds robustly across value-weighted, equal-weighted, and cap-trimmed portfolio construction methods.

### Research interpretation

This provides a quantitative rationale for a **Compressed 3-Factor Multi-Factor Alpha Strategy**:
1. **Factor Overfitting Protection:** Stacking dozens of correlated price indicators creates high turnover, high execution friction, and illusory backtest alpha. Compressing the universe to the 3 dominant orthogonal dimensions (turnover volatility, bid-ask spread, and on-chain user growth) avoids factor multicollinearity.
2. **Liquidity Friction Compensation:** The primary source of sustained cross-sectional alpha in crypto is compensation for liquidity instability and transaction friction. High turnover volatility tokens command a structural risk premium because quantitative market makers and liquidity providers require higher returns to hold inventory during turbulent volume regimes.
3. **On-Chain Network Growth Anchor:** The new-address-to-price ratio provides a genuine fundamental anchor: tokens whose on-chain active user base expands relative to market price generate positive risk-adjusted excess returns that cannot be explained by trading volume or volatility alone.

## Signal

The compressed multi-factor strategy builds an orthogonalized 3-factor composite score:

1. **Constituent Factor Computation (Weekly Formation Date $t$):**
   - **Factor 1: Turnover Volatility ($\text{TurnoverVol}_{i,t}$):**
     Standard deviation of daily turnover over the trailing 30 days:
     $$\text{Turnover}_{i,\tau} = \frac{\text{Volume}_{i,\tau}}{\text{MarketCap}_{i,\tau}}, \quad \text{TurnoverVol}_{i,t} = \text{std}(\text{Turnover}_{i, \tau})_{\tau=t-29}^t$$
   - **Factor 2: Effective Bid-Ask Spread ($\text{Spread}_{i,t}$):**
     Average relative bid-ask spread (or Corwin-Schultz high-low spread estimator) over trailing 7 days:
     $$\text{Spread}_{i,t} = \frac{1}{7} \sum_{\tau=t-6}^t \frac{\text{Ask}_{i,\tau} - \text{Bid}_{i,\tau}}{\text{Mid}_{i,\tau}}$$
   - **Factor 3: New Address to Price Ratio ($\text{NAP}_{i,t}$):**
     Ratio of 7-day average new on-chain addresses to circulating coin price:
     $$\text{NAP}_{i,t} = \frac{\overline{\text{NewAddresses}}_{i,[t-6,t]}}{P_{i,t}}$$

2. **Cross-Sectional Normalization & Composite Score:**
   - At each weekly rebalance date $t$, convert each raw factor into a uniform cross-sectional z-score (winsorized at $\pm 3\sigma$):
     $$z_{f,i,t} = \frac{X_{f,i,t} - \mu_{f,t}}{\sigma_{f,t}}, \quad f \in \{\text{TurnoverVol}, \text{Spread}, \text{NAP}\}$$
   - Form the equal-weighted composite alpha score:
     $$S_{i,t} = z_{\text{TurnoverVol},i,t} + z_{\text{Spread},i,t} + z_{\text{NAP},i,t}$$

3. **Portfolio Allocation:**
   - Sort eligible tokens into quintiles based on $S_{i,t}$.
   - Go long the top quintile ($Q_5$, high liquidity risk premium + high on-chain user growth) and short (or underweight) the bottom quintile ($Q_1$, low turnover volatility + high relative overpricing).
   - Rebalance weekly ($K = 7\text{d}$).

## Required data

- **Universe:** Liquid cryptocurrencies and Layer-1/Layer-2 tokens with accessible on-chain and order book data (200+ tokens).
- **Market Data:** Daily OHLCV, circulating market cap, bid-ask quotes / order book depth.
- **On-Chain Data:** Daily new wallet addresses created per blockchain network / token contract.
- **Timeframe:** Daily observations aggregated to weekly rebalancing timestamps (UTC Sunday 23:59:59).

## Execution assumptions

- **Rebalancing Frequency:** Weekly ($K = 1\text{w}$).
- **Execution Mechanism:** VWAP execution across 2-hour window post-rebalance timestamp.
- **Frictions & Fees:** 
  - Centralized exchange taker fees: 5 to 8 bps.
  - Bid-ask spread cost: 10 to 30 bps (specifically accounted for as Factor 2 selects tokens with wider spreads).
- **Borrow / Shorting:** For tokens without liquid perpetual futures, long-only high-minus-benchmark implementation.

## Evidence

### Source-reported

All empirical results below are directly reported by Mercik, Zaremba, and Demir (*International Review of Financial Analysis*, 2026, Article 105137):
1. **Factor Spanning:** Across 36 candidate cryptocurrency anomalies, an iterative alpha-based selection process identifies that 2 to 3 factors span all remaining 33+ anomaly portfolios, leaving zero statistically significant residual alphas.
2. **Dominant Variables:** The iterative selection algorithm consistently selects turnover volatility, bid-ask spread, and new-address-to-price ratio as the most influential spanning dimensions.
3. **Redundancy of Technical Price Factors:** Price-only momentum and short-term reversal factors are economically subsumed once liquidity risk factors are included in the asset pricing kernel.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- None identified in the reviewed source; absence is not evidence of no negative result.
- General empirical asset pricing literature emphasizes that illiquidity-based factor premiums are vulnerable to high execution costs in practical implementation, as high-spread assets inherently incur larger trading drag during rebalancing.

## Falsification plan

1. **Ablation Test against 36-Factor Equal-Weighted Benchmark:** Test whether the parsimonious 3-factor composite outperforms an uncompressed 36-factor ensemble on a net-of-cost basis out-of-sample. If the 36-factor uncompressed ensemble yields higher net Sharpe after realistic trading costs, the parsimony hypothesis is falsified.
2. **Sub-Period Stability:** If the 3-factor model fails to explain cross-sectional returns in post-2024 bear or rangebound regimes ($t\text{-stat} < 1.96$), reject model invariance.
3. **Net Alpha Hurdle:** If net excess returns after 15 bps round-trip transaction costs fall below 3.0% annualized, the strategy fails live deployment criteria.

## Crypto portability

- **Direct:** The underlying empirical study was executed exclusively on cryptocurrency market data (36 factors across multi-year weekly panels from 2018 to 2024).
- **Crypto-specific factors:** New address generation is a blockchain-native fundamental metric with no direct counterpart in traditional equity markets.

## Limitations

- **On-Chain Metric Availability:** New address counts are available for native Layer-1 coins and major smart contract tokens, but long-tail ERC-20 / SPL tokens may suffer from bot address spam or lack of clean explorer data.
- **Capacity & Rebalancing Drag:** High-spread constituent tokens in Quintile 5 will suffer greater slippage during portfolio rebalancing.

## Implementation status

No implementation in our research stack has been completed. Not implemented in PyBroker or NautilusTrader.

## Adoption boundary

Research material only. A record being present in this repository does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

## Related Wiki records

- `crypto-cross-sectional-double-sorted-anomaly-interactions-2026-09-01.md`
- `crypto-cross-sectional-systematic-liquidity-risk-beta-2026-08-31.md`
- `crypto-cross-sectional-amihud-illiquidity-premium-2026-08-31.md`

## Sources

1. Aleksander Mercik, Adam Zaremba, and Ender Demir, "Crypto factor zoo (.Zip)," *International Review of Financial Analysis*, Volume 113, 2026, Article 105137.
   - DOI: https://doi.org/10.1016/j.irfa.2026.105137
   - RePEc Handle: https://ideas.repec.org/a/eee/finana/v113y2026ics1057521926001258.html
2. Alexander Swade, Stefan Nolte, Mark Shackleton, and Adam Zaremba, "An alpha-based approach to factor selection," *Journal of Financial and Quantitative Analysis* (2024).
