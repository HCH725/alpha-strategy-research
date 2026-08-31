---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Amihud Illiquidity Premium (CIHML)
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - illiquidity
  - amihud
  - asset-pricing
  - cihml
status: research-only
confidence: high
source_as_of: 2025-08
sources:
  - https://doi.org/10.1108/CAFR-06-2024-0077
  - https://doi.org/10.1016/S1386-4181(01)00024-6
  - https://doi.org/10.1016/j.jbankfin.2020.106022
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Amihud Illiquidity Premium (CIHML)

## Provenance

Primary source:

- Asgar Ali, Sanshao Peng, and Syed Shams. “Unravelling cross-sectional patterns in cryptocurrencies: a four-factor asset pricing model.” *China Accounting and Finance Review* 27, no. 4 (2025): 493–519.
- DOI: https://doi.org/10.1108/CAFR-06-2024-0077
- Source empirical sample: Weekly and daily data covering 1,160 cryptocurrencies across 468 weeks (January 2014 through December 2022) sourced via the CoinMarketCap API.

Foundational and related literature:

- Yakov Amihud. “Illiquidity and stock returns: cross-section and time-series effects.” *Journal of Financial Markets* 5, no. 1 (2002): 31–56. DOI: https://doi.org/10.1016/S1386-4181(01)00024-6.
- Alexander Brauneis, Roland Mestel, Ryan Riordan, and Erik Theissen. “How to measure the liquidity of cryptocurrency markets?” *Journal of Banking & Finance* 124 (2021): 106022. DOI: https://doi.org/10.1016/j.jbankfin.2020.106022.
- Yukun Liu, Aleh Tsyvinski, and Xi Wu. “Common Risk Factors in Cryptocurrency.” *The Journal of Finance* 77, no. 2 (2022): 1133–1177. DOI: https://doi.org/10.1111/jofi.13119.

## Economic mechanism

### Source-reported

Ali, Peng, and Shams (2025) investigate the cross-sectional determinants of cryptocurrency returns and propose a four-factor asset pricing model comprising:
1. Cryptocurrency Market Factor ($CR_m - R_f$);
2. Crypto Size Factor (CSMB: Small-Minus-Big);
3. Crypto Reversal Factor (CLMW: Losers-Minus-Winners);
4. Crypto Illiquidity Factor (CIHML: Illiquid-High-Minus-Low).

The authors document that:
- Amihud illiquidity—measured as the absolute price change per dollar of daily trading volume—exhibits a strong, positive, and statistically significant cross-sectional relation with subsequent cryptocurrency returns.
- Tokens with high price impact (illiquid assets) systematically outperform tokens with low price impact (liquid assets) to compensate investors for bearing liquidity risk and holding-period liquidation hurdles.
- The CIHML factor generates a significant risk premium that cannot be subsumed by standard market beta, market capitalization (size), or momentum factors.
- Incorporating CIHML alongside size and short-term reversal dramatically improves the pricing of cross-sectional cryptocurrency portfolios and reduces Gibbons-Ross-Shanken (GRS) test pricing errors compared to traditional models.

### Research interpretation

The hypothesized economic mechanism is structural compensation for price impact and transaction frictions:

1. **Liquidity Friction Compensation:** Investors holding thinly traded tokens face steep bid-ask spreads, shallow order book depth, and adverse price impact when rebalancing or liquidating positions. To hold such inventory over finite horizons, investors require an ex-ante expected return premium.
2. **Flight-to-Liquidity Risk:** During market downturns, liquidity rapidly dries up in less liquid tokens, creating severe execution penalties. High-Amihud assets thus carry unhedgeable liquidity beta risk.
3. **Limits to Arbitrage:** Arbitrageurs cannot easily eliminate pricing inefficiencies in high-illiquidity tokens due to high transaction costs and borrow constraints, allowing the illiquidity spread to persist in cross-sectional equilibrium.
4. **Factor Sorting:** Sorting the cross-section by the rolling Amihud illiquidity ratio and taking a long position in high-illiquidity tokens against a short position in low-illiquidity tokens (or holding an illiquidity-tilted long basket) harvests this structural liquidity risk premium.

## Signal

### Baseline Source-Normalized Rule

1. **Universe Formation & Minimum Liquidity Filter:**
   - At each rebalancing date $t$ (e.g., weekly on Sunday 00:00 UTC or daily at 00:00 UTC), identify all active, tradeable cryptocurrencies $i \in U_t$.
   - Exclude stablecoins, wrapped/pegged tokens, and tokens with zero trading volume.
   - Require minimum continuous trading history over the lookback window $W$ (e.g., $W = 30$ days) and a minimal base volume threshold (e.g., daily dollar volume $\ge \$10,000$) to prevent division-by-zero artifacts.

2. **Amihud Illiquidity Ratio Calculation:**
   - For each asset $i$ on day $d$, compute the daily Amihud illiquidity metric:
     $$\text{ILLIQ}_{i,d} = \frac{|R_{i,d}|}{\text{DollarVolume}_{i,d}} \times 10^6$$
     where $R_{i,d} = \frac{P_{i,d} - P_{i,d-1}}{P_{i,d-1}}$ is the daily return and $\text{DollarVolume}_{i,d} = P_{i,d} \times \text{Volume}_{i,d}$.
   - Compute the rolling average Amihud score over lookback window $W$:
     $$\overline{\text{ILLIQ}}_{i,t} = \frac{1}{W} \sum_{d=t-W+1}^t \text{ILLIQ}_{i,d}$$

3. **Cross-Sectional Ranking & Bucket Assignment:**
   - Rank the universe $U_t$ in ascending order of $\overline{\text{ILLIQ}}_{i,t}$.
   - Partition into $N$ quantile buckets (e.g., quintiles: Q1 [Most Liquid / Lowest ILLIQ] to Q5 [Most Illiquid / Highest ILLIQ]).
   - **Long Bucket (Illiquid / Q5):** Top 20% highest Amihud illiquidity ratio.
   - **Short / Benchmark Bucket (Liquid / Q1):** Bottom 20% lowest Amihud illiquidity ratio (predominantly mega-cap liquid tokens like BTC, ETH, SOL).

4. **Portfolio Weighting & Construction:**
   - Equal-weighted (or inverse-volatility weighted) within each quantile bucket.
   - Target CIHML factor portfolio: $+1.0$ weight on Q5 (Illiquid), $-1.0$ weight on Q1 (Liquid) for dollar-neutral implementation, or long Q5 beta-hedged against market index.

5. **Rebalancing Frequency & Execution Timing:**
   - Signal formation at timestamp $t$ close (00:00 UTC).
   - Execution at timestamp $t+1$ market open (next-bar execution).
   - Rebalance cadence: Weekly (baseline in Ali et al. 2025) or monthly.

### Normalized Pseudocode

```python
import numpy as np
import pandas as pd

def compute_crypto_cihml_weights(
    close_prices: pd.DataFrame,    # Daily close prices [T, N]
    dollar_volumes: pd.DataFrame,  # Daily dollar trading volumes [T, N]
    lookback_window: int = 30,
    n_buckets: int = 5,
    min_dollar_vol: float = 10_000.0,
    min_obs: int = 20
) -> pd.DataFrame:
    """
    Computes cross-sectional Crypto Illiquid-High-Minus-Low (CIHML) target weights.
    Lagged by 1 period to prevent look-ahead bias.
    """
    # 1. Daily return calculation
    daily_returns = close_prices.pct_change()
    
    # 2. Daily Amihud illiquidity measure
    # Set zero or negative volume to NaN to avoid division by zero
    valid_vol = dollar_volumes.where(dollar_volumes >= min_dollar_vol, np.nan)
    daily_amihud = (daily_returns.abs() / valid_vol) * 1e6
    
    # 3. Rolling average illiquidity over formation window
    rolling_amihud = daily_amihud.rolling(window=lookback_window, min_periods=min_obs).mean()
    
    weights = pd.DataFrame(0.0, index=close_prices.index, columns=close_prices.columns)
    
    for t in close_prices.index:
        amihud_t = rolling_amihud.loc[t].dropna()
        if len(amihud_t) < 15:
            continue
            
        # Cross-sectional quantile sort
        ranks = amihud_t.rank(method="first", ascending=True)
        q = pd.qcut(ranks, q=n_buckets, labels=False)
        
        liquid_tokens = amihud_t.index[q == 0]              # Q1: Lowest illiquidity (most liquid)
        illiquid_tokens = amihud_t.index[q == (n_buckets - 1)] # Q5: Highest illiquidity (most illiquid)
        
        # Equal-weighted within bucket
        weights.loc[t, illiquid_tokens] = 1.0 / len(illiquid_tokens)
        weights.loc[t, liquid_tokens] = -1.0 / len(liquid_tokens)
        
    return weights.shift(1)  # Signal formed at t, executed at t+1
```

## Required data

- **Universe:** Broad multi-asset spot and perpetual cryptocurrency universe.
- **Price & Volume Fields:** Daily close prices and daily dollar trading volume (or close price $\times$ token volume).
- **Timestamp Standardization:** Consistent daily candle boundary (e.g., 00:00:00 UTC).
- **Point-in-Time Universe Records:** Survivorship-free historical data including delisted tokens, dead projects, and historical exchange listings.
- **Microstructure / Spread Reference:** Historical bid-ask spreads or high-frequency order book depth to evaluate realistic transaction frictions.

## Execution assumptions

- **Execution Timing:** Signal calculated using closing data up to day $t$; orders dispatched at market open of day $t+1$ (next-bar execution).
- **Order Handling:** Execution via TWAP or passive limit orders with execution slippage penalty due to shallow depth in Q5 tokens.
- **Transaction Costs:** 5–15 bps taker fees or 2–5 bps maker fees; illiquidity premium must be evaluated against high execution costs in Q5 illiquid tokens.
- **Short Feasibility:** Shorting illiquid spot tokens is heavily constrained or impossible; on derivatives, Q1 (liquid) can be shorted via perpetual futures while Q5 is held long in spot or liquid perpetual subsets.

## Evidence

### Source-reported

- Ali, Peng, and Shams (2025) report that the CIHML factor generates a statistically significant positive weekly excess return with a $t$-statistic exceeding $3.2$ over the 2014–2022 sample across 1,160 cryptocurrencies.
- The four-factor model (CRm-Rf, CSMB, CLMW, CIHML) substantially outperforms the single-factor CAPM, Fama-French 3-factor, and Carhart 4-factor models in pricing cross-sectional crypto portfolios.
- GRS test statistics for model pricing errors drop significantly when CIHML is added, demonstrating that liquidity risk is priced separately from size and short-term reversal.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Turnover & Execution Drag:** In live execution, holding illiquid tokens (Q5) incurs severe real-world slippage and wide bid-ask spreads (often 50–200+ bps), which can consume the gross statistical premium unless turnover is strictly minimized.
- **Survivorship / Delisting Risk:** Illiquid tokens have high baseline failure rates (rug pulls, protocol abandonment, exchange delisting). If delisted tokens with total loss (-100%) are excluded from empirical datasets, reported returns are heavily biased upward.
- **Liquidity Black Holes:** During broad crypto market crashes, illiquid tokens suffer severe price collapses with zero bid depth, preventing orderly liquidation.

## Falsification plan

The CIHML illiquidity hypothesis should be considered falsified if:
1. Re-estimating the strategy on a survivorship-bias-free database including all delisted/dead tokens reduces the net return spread below zero.
2. Incorporating realistic liquidity-adjusted transaction costs (bid-ask spread + price impact) erodes the annualized Sharpe ratio below 0.2.
3. Out-of-sample testing on 2023–2026 data shows that the Q5 minus Q1 return spread is non-positive or statistically indistinguishable from zero ($t < 1.96$).
4. The alpha of CIHML is fully absorbed when regressed against a composite model of size, idiosyncratic volatility, and downside beta.

## Crypto portability

- **Classification:** Adapted.
- **Spot vs Perpetual Implementation:** On spot exchanges, the universe of illiquid tokens is vast, but shorting is restricted. On perpetual futures exchanges, only liquid and moderately liquid tokens are listed (top 100–300 perps), which truncates the illiquidity distribution but allows symmetric long-short execution.
- **Perpetual Adaptation:** Within the perpetual universe, sorting relative Amihud illiquidity produces an executable long-short factor with lower structural default risk.
- **Funding Rate Impact:** High-illiquidity perpetuals often trade at erratic funding rates; carrying long positions requires monitoring funding fee accrual.

## Limitations

- **Not independently reproduced.**
- **Underspecified Live Execution:** The academic source provides factor-sort evidence rather than an optimized algorithmic trading execution framework.
- **High Sensitivity to Microstructure Noise:** Small denominator values (low volume) can create extreme outlier spikes in the Amihud ratio, requiring winsorization or volume floors.
- **Capacity Constraints:** The strategy cannot scale to large institutional AUM due to the intrinsic illiquidity of the long bucket.

## Implementation status

Not implemented in our research stack. No PyBroker or NautilusTrader backtest has been performed.

`implementation_status: not-implemented`

## Adoption boundary

Research-only. This record is quantitative research staging material and does not constitute authorization for deployment in paper, testnet, or live trading.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `[[crypto-cross-sectional-size-factor-smb-2026-08-31]]`
- `[[crypto-cross-sectional-last-day-return-reversal-liquidity-conditioned-2026-08-31]]`
- `[[crypto-cross-sectional-downside-beta-risk-premium-2026-08-31]]`
- `[[crypto-cross-sectional-idiosyncratic-volatility-pricing-2026-08-31]]`

## Sources

1. Asgar Ali, Sanshao Peng, and Syed Shams, “Unravelling cross-sectional patterns in cryptocurrencies: a four-factor asset pricing model,” *China Accounting and Finance Review* 27(4), 493–519 (2025). DOI: https://doi.org/10.1108/CAFR-06-2024-0077
2. Yakov Amihud, “Illiquidity and stock returns: cross-section and time-series effects,” *Journal of Financial Markets* 5(1), 31–56 (2002). DOI: https://doi.org/10.1016/S1386-4181(01)00024-6
3. Alexander Brauneis, Roland Mestel, Ryan Riordan, and Erik Theissen, “How to measure the liquidity of cryptocurrency markets?” *Journal of Banking & Finance* 124, 106022 (2021). DOI: https://doi.org/10.1016/j.jbankfin.2020.106022
4. Yukun Liu, Aleh Tsyvinski, and Xi Wu, “Common Risk Factors in Cryptocurrency,” *The Journal of Finance* 77(2), 1133–1177 (2022). DOI: https://doi.org/10.1111/jofi.13119
