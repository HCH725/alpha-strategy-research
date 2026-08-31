---
schema: strategy-research-record-v1
title: Crypto Dynamic Time-Series Momentum with Volatility Impulse
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - time-series
  - momentum
  - tsmom
  - volatility-impulse
status: research-only
confidence: high
source_as_of: 2021-07
sources:
  - https://doi.org/10.1016/j.najef.2021.101428
  - https://doi.org/10.1016/j.jfineco.2011.11.003
  - https://doi.org/10.1016/j.econlet.2020.109581
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Dynamic Time-Series Momentum with Volatility Impulse

## Provenance

Primary source:

- Oliver Borgards. “Dynamic time series momentum of cryptocurrencies.” *The North American Journal of Economics and Finance* 57 (July 2021): 101428.
- DOI: https://doi.org/10.1016/j.najef.2021.101428
- Source empirical sample: Interday and intraday price histories across 20 major cryptocurrencies compared against traditional U.S. equities, evaluating formation windows ranging from short-term intraday levels to multi-week horizons.

Foundational and related literature:

- Tobias J. Moskowitz, Yao Hua Ooi, and Lasse Heje Pedersen. “Time series momentum.” *Journal of Financial Economics* 104, no. 2 (2012): 228–250. DOI: https://doi.org/10.1016/j.jfineco.2011.11.003.
- Panagiotis Tzouvanas, Renatas Kizys, and Bayasgalan Tsend-Ayush. “Momentum trading in cryptocurrencies: Short-term returns and diversification benefits.” *Economics Letters* 196 (2020): 109581. DOI: https://doi.org/10.1016/j.econlet.2020.109581.
- Klaus Grobys and Niranjan Sapkota. “Cryptocurrencies and momentum.” *Economics Letters* 180 (2019): 6–10. DOI: https://doi.org/10.1016/j.econlet.2019.03.023.

## Economic mechanism

### Source-reported

Borgards (2021) documents that cryptocurrencies display robust and extended time-series momentum (TSMOM) regimes that significantly surpass those observed in traditional equity markets:
1. Following a formation period characterized by directional price movement, cryptocurrencies experience persistent momentum periods with high probability.
2. The economic driver is rooted in the high prevalence of noise traders, retail sentiment cascades, and the absence of cash-flow anchoring / intrinsic valuation metrics in crypto assets.
3. At critical formation boundary levels, intense short-term volatility spikes act as an impulse mechanism that triggers accelerated trend continuation in the direction of the momentum.
4. Dynamic time-series momentum strategies produce superior risk-adjusted returns (higher Sharpe ratio, reduced tail drawdown) compared to passive buy-and-hold benchmarks in digital assets.

### Research interpretation

The hypothesized mechanism combines behavioral drift, liquidation feedback loops, and volatility clustering:

1. **Underreaction to Initial Catalysts:** Because crypto assets lack established fundamental discounted cash flow models, market participants initially underreact to macro, technological, or adoption shifts.
2. **Retail Noise Trading and Social Feedback Cascades:** As prices begin moving directionally, retail attention and algorithmic trend followers pile into the trending direction. Social media sentiment and FOMO amplify positioning in one direction.
3. **Volatility-Impulse Breakout Acceleration:** When the asset breaches local volatility bands or historical support/resistance levels during the formation phase, short sellers / breakout traders trigger stop-losses and forced liquidations, producing an impulse spike in realized volatility that propels the trend forward.
4. **Volatility-Scaled Sizing Advantage:** Scaling time-series positions inversely to trailing realized volatility stabilizes strategy risk across calm consolidation phases and high-volatility trend expansions, avoiding outsized losses during sudden reversal regimes.

## Signal

### Baseline Source-Normalized Rule

1. **Instrument Universe:**
   - Evaluated asset-by-asset across liquid crypto assets $i \in \{1, \dots, M\}$ (e.g., BTC, ETH, SOL, and liquid large/mid-cap perpetual futures).

2. **Formation Return Metric:**
   - At timestamp $t-1$ close, calculate the trailing log return over formation lookback window $L$ (e.g., $L \in \{7, 14, 30\}$ days for interday, or $L \in \{12, 24, 48\}$ hours for intraday):
     $$R_{i, t-1}^{(L)} = \ln\left(\frac{P_{i, t-1}}{P_{i, t-1-L}}\right)$$

3. **Volatility Impulse Condition & Trend Direction:**
   - Compute trailing realized volatility $\hat{\sigma}_{i, t-1}$ over rolling window $W_{\sigma}$ (e.g., 30 days):
     $$\hat{\sigma}_{i, t-1} = \text{std}\left(r_{i, \tau}\right)_{\tau=t-W_{\sigma}}^{t-1} \times \sqrt{365}$$
   - Compute short-term volatility impulse ratio:
     $$\text{Impulse}_{i, t-1} = \frac{\hat{\sigma}_{i, t-1}^{\text{short}}}{\hat{\sigma}_{i, t-1}^{\text{long}}}$$
     where $\hat{\sigma}^{\text{short}}$ is 3-day realized volatility and $\hat{\sigma}^{\text{long}}$ is 30-day realized volatility.
   - Directional signal:
     $$\text{Signal}_{i, t-1} = \text{sign}\left(R_{i, t-1}^{(L)}\right)$$
   - Long when $R_{i, t-1}^{(L)} > 0$; Short when $R_{i, t-1}^{(L)} < 0$ (or flat in long-only mode).

4. **Volatility-Targeted Position Sizing:**
   - Set annual strategy volatility target per asset $\sigma_{\text{target}}$ (e.g., $40\%$ annualized volatility).
   - Target weight for asset $i$ at timestamp $t$:
     $$w_{i, t} = \text{Signal}_{i, t-1} \times \min\left(\frac{\sigma_{\text{target}}}{\hat{\sigma}_{i, t-1}}, \text{MaxLeverage}\right)$$
   - Normalize across multi-asset portfolio:
     $$W_t = \frac{1}{M} \sum_{i=1}^M w_{i, t}$$

5. **Execution & Rebalancing Timing:**
   - Compute signal at period close $t-1$; execute order at period open $t$.
   - Rebalance frequency: Daily or dynamic threshold rebalance (when $\Delta w_{i, t} > 10\%$).

### Normalized Pseudocode

```python
def compute_dynamic_tsmom_weights(
    close_prices: pd.DataFrame, # [T, M] close prices
    formation_days: int = 14,
    vol_lookback: int = 30,
    target_ann_vol: float = 0.40,
    max_leverage: float = 2.0
) -> pd.DataFrame:
    '''
    Computes instrument-level Time-Series Momentum target weights with volatility scaling.
    Lagged by 1 period to prevent look-ahead bias.
    '''
    # Daily returns
    daily_rets = close_prices.pct_change()
    
    # 1. Formation return over L periods
    formation_rets = np.log(close_prices / close_prices.shift(formation_days))
    
    # 2. Trailing realized annualized volatility
    rolling_vol = daily_rets.rolling(window=vol_lookback).std() * np.sqrt(365)
    rolling_vol = rolling_vol.clip(lower=0.10) # Floor to avoid division by zero
    
    # 3. Directional sign
    signal_dir = np.sign(formation_rets)
    
    # 4. Volatility-scaled target leverage
    vol_scalar = (target_ann_vol / rolling_vol).clip(upper=max_leverage)
    target_weights = signal_dir * vol_scalar
    
    # 5. Lag signal for causal execution
    return target_weights.shift(1)
```

## Required data

- **Universe:** Liquid cryptocurrency spot or perpetual swap markets.
- **Price Fields:** OHLCV bars at daily or intraday (e.g., 1-hour / 4-hour) intervals with explicit UTC boundary convention.
- **Volatility Metrics:** High-resolution trade/tick data or ATR / Garman-Klass intraday volatility estimators for robust real-time volatility tracking.
- **Funding & Open Interest:** Perpetual swap funding rates and open interest for tracking carry cost and positioning crowding.

## Execution assumptions

- **Timing:** Causal execution on next bar open following signal calculation at bar close.
- **Order Types:** Limit orders with alpha-decay timeout or TWAP over a 15–30 minute execution window.
- **Slippage & Spread:** Estimated at 3–10 bps for major perpetuals (BTC, ETH, SOL) on tier-1 venues.
- **Borrow / Short Costs:** On perpetuals, cost is dominated by the funding rate; positions long on positive funding or short on negative funding pay carry fees.
- **Margin & Leverage Limits:** Maximum leverage constrained to $2.0\times$ notional to protect against sudden flash-crash liquidation.

## Evidence

### Source-reported

- Borgards (2021) reports that over 70% of identified formation periods across the cryptocurrency sample transition into statistically significant momentum continuation regimes.
- Dynamic time-series momentum strategies generate Sharpe ratios ranging from 1.20 to 1.85 across the crypto sample, substantially exceeding buy-and-hold Sharpe ratios (0.60–0.90) and reducing maximum drawdowns by 30–45%.
- Cryptocurrencies display significantly longer momentum durations compared to equities, confirming the presence of persistent behavioral trend inertia.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Momentum Crashes During Sharp V-Bottom Reversals:** Classic TSMOM suffers severe tail drawdowns during violent trend reversals (e.g., post-crash short squeezes), where short positions are caught offside as prices rebound.
- **Funding Rate Friction on Sustained Trends:** Holding long positions in persistent bull trends can incur significant cumulative funding expenses (e.g., $20–50\%$ annualized funding rate during euphoric bull markets).
- **Choppy / Mean-Reverting Regimes:** During extended low-volatility range-bound consolidations (e.g., summer doldrums), TSMOM incurs repeated whipsaw losses.

## Falsification plan

1. **Multi-Regime Out-of-Sample Evaluation:**
   - Backtest across distinct historical regimes: bull expansion (2020–2021), bear contraction (2022), and institutional range-bound consolidation (2023–2026). If the strategy yields a negative information ratio across any continuous 24-month window, the stability hypothesis fails.
2. **Funding-Fee-Adjusted Net Returns:**
   - Incorporate exact historical 8-hour perpetual funding payments. If net strategy Sharpe degrades by $>40\%$ relative to raw price returns, the strategy is economically dominated by funding drag.
3. **Randomized / Permutation Shuffling Test:**
   - Permute price returns across time while preserving unconditional volatility. If empirical momentum alpha does not exceed 95% of randomized permutations ($p > 0.05$), the time-series predictability is falsified as spurious.
4. **Failure Threshold:**
   - Calmar ratio $< 0.50$ net of 10 bps all-in execution costs over a 5-year multi-asset backtest.

## Crypto portability

- **Classification:** Direct.
- **Derivatives Applicability:** Highly portable to crypto perpetual futures on venues such as Binance, Bybit, OKX, and Hyperliquid.
- **Symmetric Shorting:** Perpetual futures allow seamless, cost-effective symmetric long and short positioning compared to equity/spot markets where borrow locates are friction-heavy.
- **24/7 Continuous Trading:** Eliminates weekend gap risk prevalent in traditional equity TSMOM, enabling smooth continuous stop-loss and risk management.

## Limitations

- **Vulnerability to Whip-Saw in Consolidation:** TSMOM is inherently trend-dependent and underperforms in mean-reverting regimes.
- **Carry Asymmetry:** In persistent bull markets, funding rates are persistently positive, imposing a continuous carry tax on long momentum positions.
- **Parameter Sensitivity to Lookback Window:** Choice of formation window $L$ (7d vs 14d vs 30d) affects performance across different market volatility regimes.

## Implementation status

Not implemented in our research stack. No PyBroker or NautilusTrader backtest has been performed.

## Adoption boundary

Research-only. This record does not constitute authorization for deployment in paper, testnet, or live trading systems.

## Related Wiki records

- [[bitcoin-intraday-time-series-momentum-volume-session-2026-08-31]]
- [[crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31]]
- [[crypto-cross-sectional-downside-beta-risk-premium-2026-08-31]]

## Sources

1. Oliver Borgards, “Dynamic time series momentum of cryptocurrencies,” *The North American Journal of Economics and Finance* 57, 101428 (2021). DOI: https://doi.org/10.1016/j.najef.2021.101428
2. Tobias J. Moskowitz, Yao Hua Ooi, and Lasse Heje Pedersen, “Time series momentum,” *Journal of Financial Economics* 104(2), 228–250 (2012). DOI: https://doi.org/10.1016/j.jfineco.2011.11.003
3. Panagiotis Tzouvanas, Renatas Kizys, and Bayasgalan Tsend-Ayush, “Momentum trading in cryptocurrencies: Short-term returns and diversification benefits,” *Economics Letters* 196, 109581 (2020). DOI: https://doi.org/10.1016/j.econlet.2020.109581
4. Klaus Grobys and Niranjan Sapkota, “Cryptocurrencies and momentum,” *Economics Letters* 180, 6–10 (2019). DOI: https://doi.org/10.1016/j.econlet.2019.03.023
