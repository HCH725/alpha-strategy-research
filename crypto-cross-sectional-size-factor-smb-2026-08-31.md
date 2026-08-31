---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Size Factor (Small-Minus-Big / SMB)
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - size
  - smb
  - asset-pricing
status: research-only
confidence: high
source_as_of: 2022-04
sources:
  - https://doi.org/10.1111/jofi.13119
  - https://doi.org/10.1093/rfs/hhaa113
  - https://doi.org/10.1016/0304-405X(93)90023-5
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Size Factor (Small-Minus-Big / SMB)

## Provenance

Primary source:

- Yukun Liu, Aleh Tsyvinski, and Xi Wu. “Common Risk Factors in Cryptocurrency.” *The Journal of Finance* 77, no. 2 (April 2022): 1133–1177.
- DOI: https://doi.org/10.1111/jofi.13119
- Working paper lineage: NBER Working Paper No. 25779 (April 2019, revised 2021).
- Source empirical sample: Weekly and daily cross-sectional cryptocurrency data from 2014 through 2019/2020 spanning over 1,800 cryptocurrencies sourced from CoinMarketCap and underlying spot exchanges.

Foundational and related literature:

- Eugene F. Fama and Kenneth R. French. “Common risk factors in the returns on stocks and bonds.” *Journal of Financial Economics* 33, no. 1 (1993): 3–56. DOI: https://doi.org/10.1016/0304-405X(93)90023-5.
- Yukun Liu and Aleh Tsyvinski. “Risks and Returns of Cryptocurrency.” *The Review of Financial Studies* 34, no. 6 (2021): 2689–2727. DOI: https://doi.org/10.1093/rfs/hhaa113.
- Alexander Brauneis, Roland Mestel, Ryan Riordan, and Erik Theissen. “How to measure the liquidity of cryptocurrency markets?” *Journal of Banking & Finance* 124 (2021): 106022. DOI: https://doi.org/10.1016/j.jbankfin.2020.106022.

## Economic mechanism

### Source-reported

Liu, Tsyvinski, and Wu (2022) establish that cross-sectional cryptocurrency returns are systematically captured by a three-factor asset-pricing model consisting of:
1. A cryptocurrency market factor (CMKT);
2. A cryptocurrency size factor (Small-Minus-Big / SMB);
3. A cryptocurrency momentum factor (MOM).

The authors systematically construct and test cryptocurrency counterparts of classic equity characteristics (including size, momentum, reversal, value, volatility, volume, and illiquidity). They find that:
- The size factor (SMB) generates a large, statistically significant positive return spread across coins sorted by circulating market capitalization.
- Small market capitalization cryptocurrencies significantly outperform large market capitalization cryptocurrencies on average.
- The three-factor model (CMKT, SMB, MOM) accounts for the returns of ten distinct long-short characteristic strategies that appear to generate alpha under a single-market-factor model.
- The size premium is economically linked to investor attention, user adoption rates, limits to arbitrage in small tokens, and compensation for protocol distress/failure risk.

### Research interpretation

The hypothesized mechanism combines several structural characteristics of the crypto asset class:

1. **Retail Speculative Attention & Growth Option Value:** Small-cap tokens exhibit lottery-like payoffs and high convexity. When crypto market risk appetite expands, speculative capital disproportionately rotates down the market cap spectrum into small-cap and micro-cap tokens, generating outsized returns relative to large-cap anchors like BTC and ETH.
2. **Limits to Arbitrage and Asymmetric Borrow Costs:** Shorting small-cap altcoins is heavily constrained by illiquidity, lack of margin borrow, exchange fragmentation, or high borrowing rates. Positive demand shocks are thus absorbed primarily through price appreciation without immediate short arbitrage correction.
3. **Fundamental Protocol Distress / Abandonment Risk Compensation:** Small tokens carry substantially higher baseline hazard rates of project abandonment, code exploits, liquidity death, and delisting. Investors demanding exposure to non-anchor crypto tokens require a structural risk premium to compensate for severe tail failure probabilities.
4. **Cross-Sectional Rotation Dynamics:** Sorting the universe by market capitalization and holding a long-small / short-large (or beta-hedged small-cap) portfolio harvests this structural return differential.

## Signal

### Baseline Source-Normalized Rule

1. **Universe Formation & Eligibility:**
   - At each rebalancing date $t$ (e.g., weekly on Sunday 00:00 UTC, or daily at 00:00 UTC), identify all active, tradeable cryptocurrencies $i \in U_t$.
   - Filter out stablecoins, wrapped tokens, tokens with zero trading volume, and tokens below minimum price or liquidity thresholds (e.g., price $< \$0.001$ or daily dollar volume $< \$50,000$).
   - Require minimum continuous historical existence of $K$ days (e.g., $K = 30$ days) to avoid newly listed single-day listing pumps.

2. **Size Metric Calculation:**
   - Compute circulating market capitalization for each eligible coin $i$ as of observation cutoff $t-1$:
     $$\text{MCAP}_{i,t-1} = \text{Price}_{i,t-1} \times \text{CirculatingSupply}_{i,t-1}$$
   - If reliable circulating supply is unavailable point-in-time, total coin supply or trailing 30-day average dollar volume can serve as a proxy.

3. **Cross-Sectional Sorting & Bucket Assignment:**
   - Rank the eligible universe $U_t$ in ascending order of $\text{MCAP}_{i,t-1}$.
   - Sort assets into $N$ quantile buckets (e.g., terciles: Small, Medium, Big, or quintiles: Q1 [Smallest] to Q5 [Largest]).
   - Baseline SMB portfolio:
     - **Long Bucket (Small / Q1):** The bottom 20% (or bottom tercile) of market capitalization.
     - **Short Bucket (Big / Q5):** The top 20% (or top tercile) of market capitalization (predominantly mega-cap assets like BTC, ETH, BNB, SOL).

4. **Portfolio Weighting:**
   - Within each bucket, weights can be equal-weighted (EW) or value-weighted (VW).
   - In value-weighted SMB (standard in Liu et al. 2022 to mitigate micro-cap microstructure distortions):
     $$w_{i,t}^{\text{Small}} = \frac{\text{MCAP}_{i,t-1}}{\sum_{j \in \text{Small}} \text{MCAP}_{j,t-1}}$$
     $$w_{i,t}^{\text{Big}} = \frac{\text{MCAP}_{i,t-1}}{\sum_{k \in \text{Big}} \text{MCAP}_{k,t-1}}$$
   - Target position: $+1.0$ notional on Small bucket, $-1.0$ notional on Big bucket (dollar-neutral long-short).

5. **Rebalancing Frequency & Execution Timing:**
   - Signal computed at bar close $t-1$.
   - Orders submitted at open of period $t$ (e.g., next bar open).
   - Rebalance frequency: Weekly (baseline in Liu et al. 2022) or Daily.

### Normalized Pseudocode

```python
def compute_crypto_smb_weights(
    prices_df: pd.DataFrame, # Daily close prices [T, N]
    mcap_df: pd.DataFrame,   # Point-in-time market cap [T, N]
    volume_df: pd.DataFrame, # Daily dollar volume [T, N]
    n_buckets: int = 5,
    min_volume_usd: float = 50_000.0,
    min_history_days: int = 30
) -> pd.DataFrame:
    '''
    Computes cross-sectional Small-Minus-Big (SMB) portfolio target weights.
    Lagged by 1 period to eliminate look-ahead bias.
    '''
    # 1. Align point-in-time universe as of t-1
    valid_mask = (
        (prices_df > 0) & 
        (mcap_df > 0) & 
        (volume_df >= min_volume_usd) &
        (prices_df.rolling(min_history_days).count() >= min_history_days)
    )
    
    weights = pd.DataFrame(0.0, index=prices_df.index, columns=prices_df.columns)
    
    for t in prices_df.index:
        eligible_coins = prices_df.columns[valid_mask.loc[t]]
        if len(eligible_coins) < 10:
            continue
            
        mcap_t = mcap_df.loc[t, eligible_coins]
        ranks = mcap_t.rank(method='first', ascending=True)
        q = pd.qcut(ranks, q=n_buckets, labels=False)
        
        small_coins = eligible_coins[q == 0]
        big_coins = eligible_coins[q == (n_buckets - 1)]
        
        # Equal-weighted within bucket (or value-weighted)
        weights.loc[t, small_coins] = 1.0 / len(small_coins)
        weights.loc[t, big_coins] = -1.0 / len(big_coins)
        
    return weights.shift(1) # Ensure signal known before trading day
```

## Required data

- **Universe:** Broad multi-asset cryptocurrency universe (spot or perpetual contracts).
- **Price Fields:** Daily OHLCV with explicit candle-close timestamp conventions (00:00 UTC recommended).
- **Market Capitalization / Circulating Supply:** Point-in-time circulating supply and market capitalization records. Survivor-bias-free historical data is essential (incorporating delisted and dead coins).
- **Volume & Liquidity:** Daily dollar trading volume across primary exchanges for liquidity filtering.
- **Borrow / Short Availability:** Point-in-time borrow availability and interest rates if implementing direct spot shorting, or perpetual swap open interest and contract specifications for derivative implementations.

## Execution assumptions

- **Execution Timing:** Signal computed at timestamp $t-1$ close; executed on timestamp $t$ market open (next-bar execution).
- **Order Types:** Limit orders with passive execution or TWAP over the rebalance window to reduce market impact in less liquid small-cap tokens.
- **Slippage & Market Impact:** Small-cap tokens exhibit substantial price impact and wider bid-ask spreads (often 20–100+ bps). Net profitability depends critically on turnover management.
- **Fee Model:** Standard exchange maker/taker fee tiers (e.g., 2–5 bps maker, 5–10 bps taker on VIP tiers).
- **Shorting Mechanics:** In practice, shorting micro-cap tokens is cost-prohibitive or impossible on spot; the short leg of SMB is typically implemented using liquid perpetual futures (e.g., short BTC/ETH perpetuals) or synthesized via cross-sectional rank-weighted baskets.

## Evidence

### Source-reported

- Liu, Tsyvinski, and Wu (2022) report that the SMB portfolio generates a statistically significant weekly return spread of 1.52% to 2.85% per week (annualized > 80%, t-statistic > 3.5) over their 2014–2019 sample.
- The three-factor model achieves an average R^2 of > 75% in explaining cross-sectional crypto portfolio returns.
- Alphas of ten previously identified crypto anomalies become statistically indistinguishable from zero when regressed against the three-factor model (CMKT, SMB, MOM).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Survivorship & Delisting Bias:** Studies examining dead coins (e.g., CoinMarketCap unadjusted historical snapshots) note that small-cap returns are severely upward-biased if delisted tokens that went to zero are omitted from historical backtests.
- **Execution / Capacity Constraints:** Realized returns of small-cap long portfolios degrade rapidly when accounting for realistic bid-ask spreads, shallow order book depth, and liquidity exhaustion during market downturns.
- **Bear Market Crashes:** In crypto winter regimes (e.g., 2018, 2022), small-cap tokens suffer severe drawdown cascades relative to Bitcoin, leading to massive drawdowns for long-only small-cap exposure unless market-beta-hedged.

## Falsification plan

1. **Survivorship-Bias-Free In-Sample Replication:**
   - Re-estimate the SMB factor using a point-in-time reconstructed universe including all dead, bankrupt, and delisted tokens. If the return spread collapses to zero after incorporating actual terminal delisting losses (e.g., -100% on defunct tokens), the anomaly is falsified as survivorship bias.
2. **Transaction Cost & Market Impact Sensitivity:**
   - Apply realistic liquidity-adjusted slippage models (Almgren-Chriss or square-root law based on 24h volume). If net Sharpe ratio drops below zero at a moderate trading capital size (> $500k AUM), the strategy lacks executable capacity.
3. **Out-of-Sample Regime Verification:**
   - Test the factor across post-2022 market data (2023–2026). Verify whether SMB maintains positive alpha after controlling for BTC beta and whether small-cap outperformance persists in institutionalized market conditions.
4. **Failure Threshold:**
   - A 3-year rolling out-of-sample annualized net information ratio < 0.0 or a maximum drawdown exceeding 50% in a beta-neutral formulation falsifies the live tradeability of the size factor.

## Crypto portability

- **Classification:** Adapted.
- **Spot vs Perpetual Differences:** While spot allows access to long-tail small caps, shorting is severely limited. Implementing SMB on perpetual futures restricts the universe to the top 100–250 listed perps on tier-1 venues (e.g., Binance, Bybit, OKX), which compresses the size dispersion between the Small and Big buckets.
- **Perpetual Implementation Adaptation:** On perpetuals, the SMB factor can be structured as: Long bottom-tercile perpetuals (small altcoins) vs Short top-tercile perpetuals (BTC/ETH), dynamically beta-weighted to maintain net market delta neutrality.
- **Funding Rate Drag:** Small-cap perpetuals frequently trade at positive funding rates during bull runs and negative funding rates during bear runs. Carrying long positions in small-cap perps requires monitoring cumulative funding fee drag.

## Limitations

- **Underspecified Live Execution:** The source paper presents an asset-pricing factor sort rather than an executable order execution algorithm.
- **Liquidity & Capacity Bottlenecks:** Small-cap assets have limited capacity; institutional scaling is constrained.
- **Data Gap on Historical Point-in-Time Delistings:** Accurate historical market cap and supply data for obsolete tokens requires specialized point-in-time databases.
- **Contaminated by Lottery / Skewness Effects:** Small-cap tokens often overlap with high-MAX-return lottery tokens, meaning SMB may partially proxy for unpriced skewness preferences.

## Implementation status

Not implemented in our research stack. No PyBroker or NautilusTrader backtest has been performed.

## Adoption boundary

Research-only. This record does not constitute authorization for deployment in paper, testnet, or live trading systems.

## Related Wiki records

- [[crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31]]
- [[crypto-cross-sectional-downside-beta-risk-premium-2026-08-31]]
- [[crypto-cross-sectional-last-day-return-reversal-liquidity-conditioned-2026-08-31]]
- [[crypto-cross-sectional-max-daily-return-lottery-momentum-2026-08-31]]

## Sources

1. Yukun Liu, Aleh Tsyvinski, and Xi Wu, “Common Risk Factors in Cryptocurrency,” *The Journal of Finance* 77(2), 1133–1177 (2022). DOI: https://doi.org/10.1111/jofi.13119
2. Eugene F. Fama and Kenneth R. French, “Common risk factors in the returns on stocks and bonds,” *Journal of Financial Economics* 33(1), 3–56 (1993). DOI: https://doi.org/10.1016/0304-405X(93)90023-5
3. Yukun Liu and Aleh Tsyvinski, “Risks and Returns of Cryptocurrency,” *The Review of Financial Studies* 34(6), 2689–2727 (2021). DOI: https://doi.org/10.1093/rfs/hhaa113
4. Alexander Brauneis, Roland Mestel, Ryan Riordan, and Erik Theissen, “How to measure the liquidity of cryptocurrency markets?” *Journal of Banking & Finance* 124, 106022 (2021). DOI: https://doi.org/10.1016/j.jbankfin.2020.106022
