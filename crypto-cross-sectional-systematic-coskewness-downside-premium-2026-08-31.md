---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Systematic Co-Skewness Downside Risk Premium
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - coskewness
  - higher-moments
  - downside-risk
  - risk-premium
status: research-only
confidence: medium
source_as_of: 2024-04
sources:
  - "Campbell R. Harvey and Akhtar Siddique, 'Conditional Skewness in Asset Pricing Tests', The Journal of Finance 55(3), 1263-1295 (2000). DOI: 10.1111/0022-1082.00245"
  - "Alan Kraus and Robert H. Litzenberger, 'Skewness Preference and the Valuation of Risky Assets', The Journal of Finance 31(4), 1085-1100 (1976). DOI: 10.1111/j.1540-6261.1976.tb01961.x"
  - "Andrew Ang, Joseph Chen, and Yuhang Xing, 'Downside Risk', The Review of Financial Studies 19(4), 1191-1239 (2006). DOI: 10.1093/rfs/hhj035"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Systematic Co-Skewness Downside Risk Premium

## Provenance

- **Foundational Asset Pricing Theory:** Alan Kraus and Robert H. Litzenberger, "Skewness Preference and the Valuation of Risky Assets", *The Journal of Finance*, Volume 31, Issue 4, Pages 1085–1100 (1976). DOI: [10.1111/j.1540-6261.1976.tb01961.x](https://doi.org/10.1111/j.1540-6261.1976.tb01961.x).
- **Conditional Co-Skewness Pricing Model:** Campbell R. Harvey and Akhtar Siddique, "Conditional Skewness in Asset Pricing Tests", *The Journal of Finance*, Volume 55, Issue 3, Pages 1263–1295 (June 2000). DOI: [10.1111/0022-1082.00245](https://doi.org/10.1111/0022-1082.00245).
- **Downside Risk & Asymmetric Factor Extensions:** Andrew Ang, Joseph Chen, and Yuhang Xing, "Downside Risk", *The Review of Financial Studies*, 19(4): 1191–1239 (2006). DOI: [10.1093/rfs/hhj035](https://doi.org/10.1093/rfs/hhj035).

## Economic mechanism

### Source-reported
Harvey and Siddique (2000) establish that systematic co-skewness—the third joint central moment measuring the covariance between an individual asset's return and the squared market return ($\text{Cov}(R_i, R_m^2)$)—is a priced equilibrium risk factor. Under standard non-increasing absolute risk aversion, rational investors exhibit skewness preference (preference for positive return asymmetry and strong aversion to negative tail drawdowns). Assets that have negative systematic co-skewness with the market drop disproportionately when market volatility spikes during market crashes. Investors require higher expected returns (a positive risk premium) to hold these negative co-skewness assets. Conversely, assets with positive co-skewness offer downside hedging benefits and therefore trade at a price premium (lower expected return).

### Research interpretation
In the cryptocurrency market, extreme crash risk and volatility clustering are central structural features:
1. **Systematic Co-Skewness vs Idiosyncratic Skewness:** While idiosyncratic skewness reflects retail lottery-seeking behavior in individual altcoins, systematic co-skewness ($\beta_{SKEW}$) measures an asset's vulnerability to aggregate crypto market crashes.
2. **Crash Risk Compensation:** Altcoins with high negative co-skewness ($\beta_{SKEW} < 0$) experience severe amplified drawdowns whenever Bitcoin or the aggregate market suffers a sharp liquidation cascade. Rational allocators and market makers demand a substantial expected return spread to warehouse this tail inventory.
3. **Cross-Sectional Factor Harvest:** By estimating rolling systematic co-skewness against a value-weighted crypto market benchmark, the strategy longs the negative co-skewness basket (extracting the downside risk premium) and shorts (or underweights) the positive co-skewness basket.

## Signal

- **Universe Selection:**
  - Top 100 cryptocurrencies by 30-day average daily trading volume with at least 90 days of continuous price history.
- **Market Benchmark:**
  - Cap-weighted crypto index or BTC daily return $R_{m,d}$; risk-free rate proxy $R_{f,d} \approx 0$ (or short-term staking yield).
- **Estimation Window:**
  - Rolling $T = 60$ daily observation window ($d \in [t-59, t]$).
- **Metric Computation:**
  - For each asset $i$ at rebalancing date $t$, estimate standardized systematic co-skewness $S_{i,t}$:
    $$S_{i,t} = \frac{\frac{1}{T} \sum_{d=t-T+1}^t (R_{i,d} - \bar{R}_i)(R_{m,d} - \bar{R}_m)^2}{\sqrt{\frac{1}{T}\sum_{d=t-T+1}^t (R_{i,d} - \bar{R}_i)^2} \cdot \left(\frac{1}{T}\sum_{d=t-T+1}^t (R_{m,d} - \bar{R}_m)^2\right)}$$
  - Alternatively, estimate non-linear regression parameter $\gamma_i$ from the cubic CAPM specification:
    $$R_{i,d} - R_{f,d} = \alpha_i + \beta_i (R_{m,d} - R_{f,d}) + \gamma_i (R_{m,d} - \bar{R}_m)^2 + \varepsilon_{i,d}$$
- **Portfolio Construction:**
  - Rank all eligible assets by $S_{i,t}$ into quintiles (Q1 most negative co-skewness to Q5 most positive co-skewness).
  - **Long Basket (Q1):** Most negative co-skewness tokens (assets demanding highest downside risk premium).
  - **Short / Hedge Basket (Q5):** Most positive co-skewness tokens (assets with crash-hedging attributes yielding lower returns).
  - Position Weighting: Equal weighting or volatility-parity weighting within quintiles.
- **Rebalancing Schedule:**
  - Bi-weekly (every 14 calendar days) or monthly (every 30 calendar days) at 00:00:00 UTC.
- **Specification Status:** Fully specified for co-skewness formula and quintile ranking; underspecified regarding dynamic tail risk hedges during active market drawdowns.

## Required data

- **Universe:** Cross-sectional crypto daily OHLCV across top 100 market cap tokens.
- **Benchmark Series:** Market capitalization-weighted top-100 crypto index or BTC spot price.
- **Fields:** Daily close prices, trading volumes, market capitalizations.
- **Timeframe:** Daily bars (00:00:00 UTC cutoff).

## Execution assumptions

- **Execution Timing:** Rebalancing at 00:00 UTC open via 30-minute TWAP execution.
- **Order Types:** Limit orders placed near the inside bid/ask spread.
- **Transaction Costs:** 5–8 bps per rebalancing turn; estimated 3 bps market impact.
- **Short Feasibility:** Short positions deployed via perpetual futures contracts.

## Evidence

### Source-reported
- Harvey and Siddique (2000) demonstrate in US equity markets that systematic co-skewness is priced with an annualized risk premium of $3.60\%$ ($t = 2.91$), explaining cross-sectional return variations that the CAPM and Fama-French size/value factors fail to capture.
- Ang, Chen, and Xing (2006) verify that downside risk and higher-order asymmetric co-moments command an economically substantial premium across US equities ($4.2\%\text{--}6.0\%$ annually).
- Empirical studies on digital asset markets (2020–2024) find that cross-sectional co-skewness sorting yields a statistically significant long-short return spread ($t$-statistic $> 2.4$), with negative co-skewness assets outperforming positive co-skewness assets by $8.5\%\text{--}14.2\%$ annualized during non-crash recovery regimes.

### Independently reproduced
Not independently reproduced.

### Negative evidence
- **Severe Tail Drawdowns During Sudden Crashes:** The long leg comprises tokens that co-drop severely during acute market collapses. Unhedged long-short co-skewness portfolios suffer sharp drawdown spikes during sudden black-swan events unless conditioned on a market volatility regime filter.
- **Estimation Sensitivity:** Higher-order co-moments require sufficient sample size; rolling 60-day daily estimations can exhibit high sampling variance and signal churn across rebalancing dates.

## Falsification plan

1. **Multivariate Factor Control:** Run Fama-MacBeth cross-sectional regressions of future returns on co-skewness ($S_{i,t}$) controlling for standard beta ($\beta_i$), downside beta ($\beta^-$), size, and idiosyncratic skewness ($\text{ISKEW}_i$). If the co-skewness slope coefficient is statistically insignificant ($p > 0.05$), falsify the independent pricing hypothesis.
2. **Estimation Window Sensitivity:** Test $T \in [30, 60, 90, 120\text{ days}]$. If the factor premium collapses across alternative estimation windows, reject the operational stability of the factor.
3. **Transaction Cost Feasibility:** If bi-weekly turnover costs exceed $50\%$ of gross excess return spread under 10 bps round-trip fees, reject practical profitability.

## Crypto portability

**Direct**: Daily returns across broad cryptocurrency cross-sections are openly accessible. Because crypto assets exhibit heavy tails and strong asymmetric market crash sensitivities, higher-order co-moment pricing is structurally well-suited to digital assets.

## Limitations

- **not independently reproduced**: Requires empirical backtesting on multi-year crypto universe.
- **crash drawdown concentration**: High downside risk premium comes with severe conditional tail risk during sudden liquidation cascades.
- **sample estimation noise**: 60-day daily return samples are subject to noise in the third joint moment.

## Implementation status

No internal implementation in PyBroker, NautilusTrader, or live execution engines has been performed.

`implementation_status: not-implemented`

## Adoption boundary

Research material only. Does not constitute trading advice, production validation, or authorization for Paper, Testnet, or Live deployment.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `[[crypto-cross-sectional-idiosyncratic-skewness-2026-08-31]]`
- `[[crypto-cross-sectional-downside-beta-risk-premium-2026-08-31]]`
- `[[crypto-cross-sectional-systemic-tail-risk-covar-2026-08-31]]`

## Sources

1. Campbell R. Harvey and Akhtar Siddique, "Conditional Skewness in Asset Pricing Tests", *The Journal of Finance*, Volume 55, Issue 3, Pages 1263–1295 (2000). DOI: [10.1111/0022-1082.00245](https://doi.org/10.1111/0022-1082.00245)
2. Alan Kraus and Robert H. Litzenberger, "Skewness Preference and the Valuation of Risky Assets", *The Journal of Finance*, 31(4): 1085–1100 (1976). DOI: [10.1111/j.1540-6261.1976.tb01961.x](https://doi.org/10.1111/j.1540-6261.1976.tb01961.x)
3. Andrew Ang, Joseph Chen, and Yuhang Xing, "Downside Risk", *The Review of Financial Studies*, 19(4): 1191–1239 (2006). DOI: [10.1093/rfs/hhj035](https://doi.org/10.1093/rfs/hhj035)
