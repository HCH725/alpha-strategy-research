---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Betting Against Beta (BAB)
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - betting-against-beta
  - bab
  - low-beta-anomaly
  - asset-pricing
status: research-only
confidence: high
source_as_of: 2024-12
sources:
  - https://doi.org/10.1016/j.jfineco.2013.10.005
  - https://doi.org/10.1086/295472
  - https://doi.org/10.1111/jofi.13119
  - https://doi.org/10.1016/j.jbankfin.2021.106246
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Betting Against Beta (BAB)

## Provenance

Primary source:

- Andrea Frazzini and Lasse Heje Pedersen. “Betting against beta.” *Journal of Financial Economics* 111, no. 1 (2014): 1–25.
- DOI: https://doi.org/10.1016/j.jfineco.2013.10.005

Foundational and related literature:

- Fischer Black. “Capital market equilibrium with restricted borrowing.” *The Journal of Business* 45, no. 3 (1972): 444–455. DOI: https://doi.org/10.1086/295472.
- Eugene F. Fama and Kenneth R. French. “The Cross-Section of Expected Stock Returns.” *The Journal of Finance* 47, no. 2 (1992): 427–465. DOI: https://doi.org/10.1111/j.1540-6261.1992.tb04398.x.
- Yukun Liu, Aleh Tsyvinski, and Xi Wu. “Common Risk Factors in Cryptocurrency.” *The Journal of Finance* 77, no. 2 (2022): 1133–1177. DOI: https://doi.org/10.1111/jofi.13119.
- Wei Zhang, Yi Li, Xiong Xiong, and Pengfei Wang. “Downside risk and the cross-section of cryptocurrency returns.” *Journal of Banking & Finance* 133 (2021): 106246. DOI: https://doi.org/10.1016/j.jbankfin.2021.106246.

## Economic mechanism

### Source-reported

Frazzini and Pedersen (2014) construct a theoretical model and empirical framework demonstrating that borrowing and margin constraints explain the low-beta anomaly across global asset classes (equities, Treasury bonds, corporate bonds, credit derivatives, commodities, and currencies):

1. **Leverage Constraints & Tilt:** Constrained investors who cannot use leverage to scale their portfolio returns choose to overweight riskier, high-beta assets to achieve their desired expected return targets.
2. **Pricing Distortion (Flatter SML):** This excess demand bids up the prices of high-beta assets, driving down their alphas and Sharpe ratios. Conversely, low-beta assets are left under-demanded, trading at a discount and offering superior risk-adjusted returns (resulting in a flatter Security Market Line than predicted by standard CAPM).
3. **Betting Against Beta (BAB):** Unconstrained investors can exploit this distortion by constructing a zero-beta self-financing factor portfolio: taking a leveraged long position in low-beta assets scaled by $1/\beta_L$ and a deleveraged short position in high-beta assets scaled by $1/\beta_H$.

### Research interpretation

In the cryptocurrency asset class, the low-beta anomaly is reinforced by distinct structural and retail market dynamics:

1. **Retail Speculative Preference for High-Beta Tokens:** Retail participants and undercapitalized traders seek asymmetric upside without access to institutional margin facilities. They systematically concentrate capital in high-beta altcoins and meme tokens, driving their valuations above fundamental risk-neutral equilibrium.
2. **Asymmetric Borrow Rates & Margin Liquidation Risk:** Borrowing rates for altcoins are high and volatile. Leverage-constrained investors cannot borrow cheaply to lever up BTC or ETH, reinforcing their preference for raw high-beta tokens over levered low-beta majors.
3. **Flatter Security Market Line in Crypto:** The empirical relationship between CAPM market beta and realized excess return in cross-sectional crypto portfolios is flatter than predicted by standard equilibrium models, with low-beta assets generating higher risk-adjusted Sharpe ratios.
4. **Market-Neutral Factor Capture:** By leveraging low-beta assets to unit beta and shorting high-beta assets deleveraged to unit beta, the strategy isolates the pure leverage-constraint risk premium while hedging out systematic cryptocurrency market directional risk.

## Signal

### Baseline Source-Normalized Rule

1. **Universe Formation & Eligibility Filter:**
   - At each rebalancing date $t$ (e.g., weekly or monthly at 00:00 UTC), identify all eligible tradeable cryptocurrencies $i \in U_t$.
   - Require minimum continuous daily price history of at least $W = 60$ days (or $W = 90$ days) and daily dollar volume $\ge \$100,000$.
   - Market benchmark $M$: Equal-weighted or market-cap-weighted index of top liquid cryptocurrencies (or Bitcoin daily returns as proxy).

2. **Ex-Ante Beta Estimation & Vasicek Shrinkage:**
   - For each asset $i$, compute sample return standard deviation $\hat{\sigma}_i$ and correlation $\hat{\rho}_{i,m}$ with the market benchmark over rolling window $W$:
     $$\hat{\beta}_i^{\text{raw}} = \hat{\rho}_{i,m} \frac{\hat{\sigma}_i}{\hat{\sigma}_m}$$
   - Apply Bayesian shrinkage (Vasicek adjustment) toward the cross-sectional mean beta ($\bar{\beta} = 1.0$) to suppress estimation error in noisy altcoin time series:
     $$\beta_i = w_s \hat{\beta}_i^{\text{raw}} + (1 - w_s) \bar{\beta}, \quad w_s = 0.6$$

3. **Cross-Sectional Sorting & Bucket Assignment:**
   - Rank the universe $U_t$ in ascending order of shrunk beta $\beta_i$.
   - Compute median beta $\beta_{\text{med}} = \text{median}(\{\beta_i\})$.
   - Allocate assets with $\beta_i \le \beta_{\text{med}}$ to the Low-Beta portfolio ($L$).
   - Allocate assets with $\beta_i > \beta_{\text{med}}$ to the High-Beta portfolio ($H$).

4. **Constituent Weighting:**
   - Rank-based weighting within buckets:
     $$w_{i,L} = k_L (\bar{r} - r_i)^+, \quad w_{i,H} = k_H (r_i - \bar{r})^+$$
     where $r_i = \text{rank}(\beta_i)$, $\bar{r}$ is the average rank, and $k_L, k_H$ normalize weights such that $\sum_{i \in L} w_{i,L} = 1$ and $\sum_{i \in H} w_{i,H} = 1$.
   - Alternatively, equal-weighting across bottom and top terciles/quintiles.

5. **BAB Factor Portfolio Construction:**
   - Calculate portfolio ex-ante betas:
     $$\beta_L = \sum_{i \in L} w_{i,L} \beta_i, \quad \beta_H = \sum_{i \in H} w_{i,H} \beta_i$$
   - Construct the zero-beta BAB factor return:
     $$R_{t+1}^{\text{BAB}} = \frac{1}{\beta_L} (R_{t+1}^L - R_f) - \frac{1}{\beta_H} (R_{t+1}^H - R_f)$$
   - Long leg notional: $+1 / \beta_L$ on Low-Beta basket.
   - Short leg notional: $-1 / \beta_H$ on High-Beta basket.
   - Cash / leverage buffer: $1 - \frac{1}{\beta_L} + \frac{1}{\beta_H}$ placed in risk-free yield / stablecoin collateral.

6. **Rebalancing Cadence & Execution Timing:**
   - Signal formation at timestamp $t$ close (00:00 UTC).
   - Execution at timestamp $t+1$ market open.
   - Rebalance frequency: Monthly or Bi-weekly to control turnover costs.

### Normalized Pseudocode

```python
import numpy as np
import pandas as pd

def compute_crypto_bab_weights(
    close_prices: pd.DataFrame,    # Daily close prices [T, N]
    market_returns: pd.Series,     # Benchmark daily return series [T]
    lookback_window: int = 60,
    shrinkage_factor: float = 0.6,
    min_obs: int = 45
) -> pd.DataFrame:
    """
    Computes Betting Against Beta (BAB) target portfolio weights.
    Returns market-neutral zero-beta long/short weights lagged by 1 period.
    """
    returns = close_prices.pct_change()
    weights = pd.DataFrame(0.0, index=close_prices.index, columns=close_prices.columns)
    
    for t_idx in range(lookback_window, len(close_prices)):
        t = close_prices.index[t_idx]
        window_ret = returns.iloc[t_idx - lookback_window:t_idx]
        window_mkt = market_returns.iloc[t_idx - lookback_window:t_idx]
        
        valid_cols = window_ret.columns[window_ret.count() >= min_obs]
        if len(valid_cols) < 10:
            continue
            
        # 1. Estimate raw beta: cov(r_i, r_m) / var(r_m)
        cov_m = window_ret[valid_cols].apply(lambda s: s.cov(window_mkt))
        var_m = window_mkt.var()
        if var_m <= 1e-8:
            continue
        raw_betas = cov_m / var_m
        
        # 2. Vasicek shrinkage toward cross-sectional mean (1.0)
        shrunk_betas = shrinkage_factor * raw_betas + (1.0 - shrinkage_factor) * 1.0
        
        # 3. Rank assets and assign to Low-Beta vs High-Beta
        ranks = shrunk_betas.rank()
        z_ranks = ranks - ranks.mean()
        
        low_beta_mask = z_ranks < 0
        high_beta_mask = z_ranks > 0
        
        if low_beta_mask.sum() == 0 or high_beta_mask.sum() == 0:
            continue
            
        w_L_raw = -z_ranks[low_beta_mask]
        w_L = w_L_raw / w_L_raw.sum()
        
        w_H_raw = z_ranks[high_beta_mask]
        w_H = w_H_raw / w_H_raw.sum()
        
        # 4. Compute portfolio betas
        beta_L = (w_L * shrunk_betas[low_beta_mask]).sum()
        beta_H = (w_H * shrunk_betas[high_beta_mask]).sum()
        
        if beta_L <= 0 or beta_H <= 0:
            continue
            
        # 5. Scale weights to achieve zero ex-ante market beta
        weights.loc[t, low_beta_mask.index[low_beta_mask]] = w_L / beta_L
        weights.loc[t, high_beta_mask.index[high_beta_mask]] = -w_H / beta_H
        
    return weights.shift(1)  # Signal formed at t, executed at t+1
```

## Required data

- **Universe:** Multi-asset cross-sectional cryptocurrency universe (top 50–200 spot or perpetual tokens).
- **Price Series:** Daily OHLCV series with fixed 00:00 UTC daily close timestamps.
- **Market Benchmark:** Cap-weighted crypto index or BTC/ETH benchmark return series.
- **Volume & Liquidity Metrics:** Daily dollar volume for universe inclusion filtering.
- **Borrow / Collateral Rates:** Margin borrow rates for spot shorts and perpetual funding rates for derivative execution.

## Execution assumptions

- **Execution Timing:** Signal computed at timestamp $t$ close (00:00 UTC); executed at next-bar open $t+1$.
- **Leverage Treatment:** Low-beta leg requires leverage ($1 / \beta_L > 1.0$), which incurs borrowing costs or margin interest. High-beta leg is deleveraged ($1 / \beta_H < 1.0$).
- **Derivative Implementation:** Implementing via perpetual contracts avoids physical spot borrow fees but incurs perpetual funding rate spreads.
- **Transaction Costs:** 5–10 bps round-trip fees; slippage modeled dynamically using ADV.

## Evidence

### Source-reported

- Frazzini and Pedersen (2014) report that the BAB factor produces statistically significant positive alphas and high Sharpe ratios across all major asset classes over multiple decades (e.g., annualized Sharpe ratio of 0.78 in US equities, 0.89 in global equities, and substantial positive alphas in Treasuries, credit, and FX).
- In crypto asset-pricing extensions, empirical studies document that the crypto Security Market Line is significantly flatter than CAPM predictions; high-beta altcoins underperform on a risk-adjusted basis relative to lower-beta assets (e.g., BTC/ETH).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Deleveraging Cascades & Funding Squeezes:** During liquidity crises or rapid macro rallies, leveraged low-beta positions ($1/\beta_L > 1$) can suffer severe margin compression if low-beta assets gap downward while high-beta assets spike.
- **Funding Rate Drag on Altcoin Shorts:** In perpetual futures, shorting high-beta altcoins during severe bear regimes can face negative funding rate drag (shorts paying longs).
- **Turnover Friction:** Beta estimates in crypto are dynamic; frequent re-ranking can induce substantial rebalance turnover if lookback windows are too short ($W < 30$).

## Falsification plan

The BAB hypothesis in cryptocurrencies should be considered falsified if:
1. Cross-sectional Fama-MacBeth regressions show that the risk premium on market beta is strictly positive, steep, and aligned with standard CAPM, leaving no residual alpha for low-beta assets.
2. After accounting for realistic margin borrowing costs and perpetual funding payments, the net annualized Sharpe ratio of the BAB factor is non-positive.
3. Out-of-sample testing across 2022–2026 data indicates that the leveraged Low-Beta leg underperforms the High-Beta leg on a risk-adjusted basis ($t < 1.65$).
4. The BAB alpha is fully explained by existing size (SMB), momentum, and idiosyncratic volatility factors.

## Crypto portability

- **Classification:** Direct.
- **Perpetual Futures Execution:** Perpetual contracts are naturally suited for BAB implementation because leverage is built-in without requiring separate spot margin borrowing, and shorting high-beta tokens is symmetrical to longing low-beta tokens.
- **Funding Rate Interaction:** The funding spread between low-beta majors (BTC/ETH) and high-beta altcoins directly influences the net carry of the BAB portfolio.

## Limitations

- **Not independently reproduced.**
- **Leverage and Liquidation Risks:** The low-beta leg employs leverage ($1/\beta_L$), making the portfolio vulnerable to sudden intraday flash crashes.
- **Beta Instability:** Rolling crypto betas can fluctuate rapidly around market regime shifts, introducing ex-post beta mismatch and residual market delta.
- **Underspecified Optimal Lookback:** The source literature evaluates multiple rolling horizons ($W = 60, 90, 250$); the optimal parameterization for 24/7 crypto markets requires rigorous empirical cross-validation.

## Implementation status

Not implemented in our research stack. No PyBroker or NautilusTrader backtest has been performed.

`implementation_status: not-implemented`

## Adoption boundary

Research-only. This record is quantitative research staging material and does not constitute authorization for deployment in paper, testnet, or live trading.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `[[crypto-cross-sectional-downside-beta-risk-premium-2026-08-31]]`
- `[[crypto-cross-sectional-size-factor-smb-2026-08-31]]`
- `[[crypto-cross-sectional-idiosyncratic-volatility-pricing-2026-08-31]]`
- `[[crypto-dynamic-time-series-momentum-volatility-impulse-2026-08-31]]`

## Sources

1. Andrea Frazzini and Lasse Heje Pedersen, “Betting against beta,” *Journal of Financial Economics* 111(1), 1–25 (2014). DOI: https://doi.org/10.1016/j.jfineco.2013.10.005
2. Fischer Black, “Capital market equilibrium with restricted borrowing,” *The Journal of Business* 45(3), 444–455 (1972). DOI: https://doi.org/10.1086/295472
3. Eugene F. Fama and Kenneth R. French, “The Cross-Section of Expected Stock Returns,” *The Journal of Finance* 47(2), 427–465 (1992). DOI: https://doi.org/10.1111/j.1540-6261.1992.tb04398.x
4. Yukun Liu, Aleh Tsyvinski, and Xi Wu, “Common Risk Factors in Cryptocurrency,” *The Journal of Finance* 77(2), 1133–1177 (2022). DOI: https://doi.org/10.1111/jofi.13119
5. Wei Zhang, Yi Li, Xiong Xiong, and Pengfei Wang, “Downside risk and the cross-section of cryptocurrency returns,” *Journal of Banking & Finance* 133, 106246 (2021). DOI: https://doi.org/10.1016/j.jbankfin.2021.106246
