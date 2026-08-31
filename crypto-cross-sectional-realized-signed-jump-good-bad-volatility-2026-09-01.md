---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Realized Signed Jump (Good vs Bad Volatility) Factor
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - high-frequency
  - realized-volatility
  - signed-jumps
  - semivariance
  - anomaly
status: research-only
confidence: medium
source_as_of: 2023-10
sources:
  - "https://doi.org/10.1016/j.irfa.2023.102712"
  - "https://doi.org/10.1162/REST_a_00503"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Realized Signed Jump (Good vs Bad Volatility) Factor

## Provenance

- **Primary Source:** Zehua Zhang and Ran Zhao, "Good Volatility, Bad Volatility, and the Cross Section of Cryptocurrency Returns," *International Review of Financial Analysis*, Volume 89, Article 102712 (October 2023). DOI: [10.1016/j.irfa.2023.102712](https://doi.org/10.1016/j.irfa.2023.102712).
- **Foundational Econometric Framework in Realized Semivariance and Signed Jumps:**
  - Andrew J. Patton and Kevin Sheppard, "Good Volatility, Bad Volatility: Signed Jumps and the Persistence of Volatility," *The Review of Economics and Statistics*, Volume 97, Issue 3, Pages 683–697 (2015). DOI: [10.1162/REST_a_00503](https://doi.org/10.1162/REST_a_00503).
  - Ole E. Barndorff-Nielsen, Silja Kinnebrock, and Neil Shephard, "Measuring Downside Risk: Realised Semivariance," *Volatility and Time Series Econometrics: Essays in Honor of Robert Engle*, Oxford University Press, Pages 117–136 (2010).

Zhang and Zhao (2023) examine high-frequency intraday data across the cryptocurrency market to investigate whether realized variation measures—specifically decomposed into upside "good" volatility and downside "bad" volatility—predict cross-sectional cryptocurrency returns.

## Economic mechanism

### Source-reported

Zhang and Zhao (2023) decompose high-frequency total quadratic variation into positive realized semivariance ($RS^+$) and negative realized semivariance ($RS^-$). They report that signed jump variations account for approximately 18% of total quadratic variation in cryptocurrency returns.

The authors show that Realized Signed Jumps ($RSJ$) possess strong predictive power for future cross-sectional excess returns:
1. Portfolios sorted on $RSJ$ exhibit statistically and economically significant return spreads.
2. The predictive relationship remains robust after controlling for standard cryptocurrency market characteristics, momentum, size, and established factor pricing models.
3. The authors also document distinct persistence and asymmetry dynamics between good and bad volatility components in forecasting future volatility states.

### Research interpretation

The falsifiable hypothesis is that **asymmetric information shocks and directional jump volatility generate cross-sectional mispricing across crypto assets due to behavioral overreaction / underreaction and leverage constraints**:

1. **Information Asymmetry in Volatility Jumps:** Intraday positive jumps ($RS^+$) capture rapid price discovery driven by positive fundamental developments or retail buying stampedes. Negative jumps ($RS^-$) reflect sudden liquidity vacuums, liquidations, and panic unwinds.
2. **Asymmetric Risk Compensation:** When market participants exhibit loss aversion and tail risk sensitivity, assets prone to downside jump risk ($RS^- > RS^+$) require a risk premium, while assets with high upside jump dispersion ($RS^+ > RS^-$) may command speculative lottery premiums that subsequently mean-revert, or vice versa depending on whether momentum or reversal dominates the sorting horizon.
3. **High-Frequency Jump vs Continuous Variation Separation:** Total realized variance ($RV$) aggregates both continuous diffusive noise and jump shocks. Isolating the signed jump ratio ($RSJ$) separates directional jump asymmetry from symmetric ambient volatility.

## Signal

The normalized factor calculation is structured as follows:

1. **Intraday Return Sampling:**
   For each cryptocurrency $i$ on day $t$, sample high-frequency log returns $r_{i,t,j} = \ln(P_{i,t,j}) - \ln(P_{i,t,j-1})$ across $M$ intraday intervals (e.g. 5-minute bars, $M = 288$ for 24/7 crypto markets):
   $$\{r_{i,t,1}, r_{i,t,2}, \dots, r_{i,t,M}\}$$

2. **Realized Positive and Negative Semivariances:**
   - Realized Positive Semivariance ("Good Volatility"):
     $$RS^+_{i,t} = \sum_{j=1}^M r_{i,t,j}^2 \cdot \mathbb{I}_{\{r_{i,t,j} > 0\}}$$
   - Realized Negative Semivariance ("Bad Volatility"):
     $$RS^-_{i,t} = \sum_{j=1}^M r_{i,t,j}^2 \cdot \mathbb{I}_{\{r_{i,t,j} < 0\}}$$
   - Total Realized Variance:
     $$RV_{i,t} = RS^+_{i,t} + RS^-_{i,t} = \sum_{j=1}^M r_{i,t,j}^2$$

3. **Realized Signed Jump ($RSJ$):**
   Normalize the difference between positive and negative semivariances by total realized variance:
   $$RSJ_{i,t} = \frac{RS^+_{i,t} - RS^-_{i,t}}{RV_{i,t}}$$
   The resulting $RSJ_{i,t} \in [-1, +1]$ captures the directional skewness of high-frequency quadratic variation on day $t$.

4. **Cross-Sectional Portfolio Construction:**
   - At each daily rebalancing timestamp (UTC 00:00), rank eligible universe constituents by $RSJ_{i,t}$ (or a rolling $K$-day average, e.g. $K \in \{1, 5, 20\}$).
   - Form quintile or decile portfolios:
     - **Top Quintile (Q5):** Highest $RSJ$ (dominated by positive jump variation).
     - **Bottom Quintile (Q1):** Lowest $RSJ$ (dominated by negative jump variation).
   - Construct equal-weighted or market-cap-weighted Long Q5 / Short Q1 (or Long Q1 / Short Q5 depending on empirical calibration horizon) factor spread portfolios.

## Required data

- High-frequency intraday prices (1-minute or 5-minute OHLCV/tick bars) across liquid spot and perpetual futures markets.
- Point-in-time market capitalization and 24-hour turnover to apply liquid universe filtering.
- Continuous 24/7 timestamp alignment across UTC daily boundaries.
- Survivorship-bias-free historical data spanning delisted tokens.

## Execution assumptions

The source paper focuses on econometric predictability and cross-sectional asset pricing tests; institutional execution mechanics remain **underspecified** in the original text:

- **Rebalancing Frequency & Turnover:** Daily rebalancing of high-frequency volatility sort portfolios implies high annual portfolio turnover.
- **Transaction Costs:** Taker fees (typically 2–5 bps), maker rebates, and bid-ask spreads are not deducted in the raw academic regressions.
- **Short Feasibility:** Short positions in bottom-quintile altcoins require liquid perpetual futures contracts or accessible borrow markets.
- **Execution Timing:** Assumes execution at the next period open/TWAP following the calculation of day $t$ intraday semivariance.

## Evidence

### Source-reported

Zhang and Zhao (2023) report:
- Signed jump variation accounts for approximately **18%** of total quadratic variation in cryptocurrency returns.
- Realized signed jumps ($RSJ$) exhibit statistically significant predictive power for cross-sectional returns.
- Return differentials across $RSJ$-sorted portfolios survive multiple econometric specifications and standard multi-factor asset pricing controls.
- Volatility forecasting models demonstrate significant asymmetry and persistence differences when decomposed into good vs. bad volatility components.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- High-frequency microstructure noise, bid-ask bounce, and discrete tick-size effects can bias realized semivariance calculations if 1-minute or sub-minute data is used without noise filtering.
- Turnover-induced transaction costs in high-frequency cross-sectional rebalancing can erode gross factor alpha.
- Factor overlap: $RSJ$ may share variance with realized skewness ($RSkew$), MAX lottery factors, or jump-diffusion components.

## Falsification plan

1. **Out-of-Sample Empirical Test:** Evaluate $RSJ$ factor returns on an independent out-of-sample dataset from 2021 to 2026 across the top 100 liquid Binance/Bybit perpetual futures.
2. **Microstructure Noise Sensitivity:** Test factor robustness across varying intraday sampling frequencies (1-min, 5-min, 15-min, 30-min). If factor return vanishes at 5-minute sampling, the anomaly may be a microstructure artifact.
3. **Spanning and Ablation Tests:** Run Fama-MacBeth regressions including $RSJ$, total $RV$, realized skewness ($RSkew$), and Amihud illiquidity. If $RSJ$ t-statistic falls below 2.0, reject incremental factor alpha.
4. **Net Fee Hurdle:** If net Sharpe ratio after applying 5 bps round-trip transaction costs falls below 0.5, reject the strategy for automated execution.

## Crypto portability

Direct. The primary source directly investigates cryptocurrency high-frequency market data.

## Limitations

- **Underspecified transaction cost model:** Academic gross factor returns do not account for slippage, funding fees, or exchange maker/taker fee tiers.
- **Data intensity:** Requires continuous, clean, high-frequency tick/bar data across hundreds of digital assets.
- **Unproven live alpha:** Not validated in production execution or historical backtests with realistic order books.

## Implementation status

Not implemented. No PyBroker, NautilusTrader, paper, testnet, or live trading implementation exists for this repository.

## Adoption boundary

Research-only. This record is staging material for review and does not constitute an approved or profitable trading strategy.

## Related Wiki records

- `[[quant/crypto-cross-sectional-jump-diffusion-variance-decomposition-2026-08-31]]`
- `[[quant/crypto-cross-sectional-extreme-downside-risk-var-2026-09-01]]`
- `[[quant/crypto-cross-sectional-idiosyncratic-volatility-pricing-2026-08-31]]`
- `[[quant/crypto-cross-sectional-idiosyncratic-skewness-2026-08-31]]`

## Sources

- Zhang, Z., & Zhao, R. (2023). Good Volatility, Bad Volatility, and the Cross Section of Cryptocurrency Returns. *International Review of Financial Analysis*, 89, 102712. DOI: [https://doi.org/10.1016/j.irfa.2023.102712](https://doi.org/10.1016/j.irfa.2023.102712)
- Patton, A. J., & Sheppard, K. (2015). Good Volatility, Bad Volatility: Signed Jumps and the Persistence of Volatility. *The Review of Economics and Statistics*, 97(3), 683–697. DOI: [https://doi.org/10.1162/REST_a_00503](https://doi.org/10.1162/REST_a_00503)
- Barndorff-Nielsen, O. E., Kinnebrock, S., & Shephard, N. (2010). Measuring Downside Risk: Realised Semivariance. In T. Bollerslev, J. R. Russell, & M. W. Watson (Eds.), *Volatility and Time Series Econometrics: Essays in Honor of Robert Engle* (pp. 117–136). Oxford University Press.
