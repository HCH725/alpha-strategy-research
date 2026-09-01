---
schema: strategy-research-record-v1
title: "The Science and Practice of Trend-Following Systems: Autocorrelation, Drift Decomposition, and Closed-Form Performance Attribution"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - trend-following
  - managed-futures
  - cta
  - autocorrelation
  - sharpe-ratio
  - skewness
  - fractional-processes
status: research-only
confidence: high
source_as_of: 2026-07-21
sources:
  - "Artur Sepp and Vladimir Lucic, 'The Science and Practice of Trend-Following Systems', arXiv:2607.19497v1 [q-fin.ST, q-fin.MF], July 21, 2026. https://arxiv.org/abs/2607.19497. Code: https://github.com/ArturSepp/TrendFollowingSystems"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# The Science and Practice of Trend-Following Systems: Autocorrelation, Drift Decomposition, and Closed-Form Performance Attribution

## Provenance

- **Primary Paper:** Artur Sepp (LGT Bank Schweiz) and Vladimir Lucic (Quantitative Research), *"The Science and Practice of Trend-Following Systems"*, arXiv preprint `arXiv:2607.19497v1 [q-fin.ST, q-fin.MF]`, published July 21, 2026.
- **Traceable Source URL:** `https://arxiv.org/abs/2607.19497` / `https://arxiv.org/html/2607.19497v1`.
- **Public Code Repository:** Python package `trendfollowing` hosted at `https://github.com/ArturSepp/TrendFollowingSystems`.
- **Empirical Dataset:** 84 liquid futures contracts across global equity indices, government bonds, short-term interest rates, foreign exchange, and commodities, evaluated over 1997 to 2026 with volume-based transaction cost tiers.

## Economic mechanism

### Source-reported

Trend-following (TF) systems across Commodity Trading Advisors (CTAs) and Quantitative Investment Strategies (QIS) monetize serial dependence in asset prices. The paper unifies three major industry implementations:
1. **European TF Systems:** Continuous position sizing proportional to volatility-normalized returns passed through variance-preserving Exponentially Weighted Moving Average (EWMA) or long-short EWMA filters (representative of large European CTAs like Capital Fund Management and Man AHL).
2. **American TF Systems:** Discrete, range-breakout trading with Average True Range (ATR) entry buffers and trailing stop-losses (descended from the original 1980s Richard Dennis "Turtle Traders" methodology).
3. **Time Series Momentum (TSMOM):** Academic momentum implementations using sign-transformed returns across multiple historical windows.

The authors derive three foundational analytical results:
1. **Exact Sample-Path P&L Decomposition:** The cumulative arithmetic return of a European TF system decomposes into an **autocorrelation term** ($\sum_{m=0}^\infty \nu^m \hat{\rho}_T(m) - 1$) and a **squared drift term** ($(\bar{z}_T)^2 / \hat{\gamma}_T(0)$), with an explicit boundary interaction term $R_T$.
2. **Frequency Domain Representation:** Trend-following expected return is a Poisson-kernel integral over the spectrum of volatility-normalized returns: alpha exists at zero drift if and only if there is excess spectral mass at low frequencies.
3. **Structural Positive Skewness:** Aggregated multi-day returns exhibit positive skewness as an intrinsic structural property of the quadratic product filter (lagged signal $\times$ current return), which peaks at horizons near half the filter span ($T \approx \text{span}/2$) even under pure Gaussian white noise where expected return is zero.

### Research interpretation

The continuous European TF rule ($w_t = S_t \frac{\sigma_{\text{target}}}{\sqrt{a}\sigma_t}$) represents dynamic discrete-time fractional Kelly sizing ($w_t^* = \frac{\widehat{SR}_t}{\widehat{\sigma}_t}$), where the EWMA filter acts as a rolling Sharpe ratio estimator. 

A fundamental horizon duality governs trend following:
- **Short filter spans** monetize short-term serial autocorrelation, with Sharpe contributions decaying as $1/\sqrt{\text{span}}$ and turnover scaling as $1/\sqrt{\text{span}}$.
- **Long filter spans** monetize the underlying asset's structural drift, with Sharpe contributions growing as $\sqrt{\text{span}}$ and turnover dropping toward zero.

Under proportional transaction costs $c$, short-memory autoregressive alpha ($\text{AR}(1)$) has a span-invariant break-even cost $c_\infty^* = \phi \sqrt{\pi / (2a)}$. In contrast, long-memory processes ($\text{ARFIMA}(0,d,0)$) yield an interior cost-optimal span scaling as $c^{1/(2d)}$.

## Signal

### 1. Volatility-Normalized Returns

For daily returns $r_t$ of a continuous futures contract:
- Compute rolling EWMA volatility $\sigma_t^2 = \nu_\sigma \sigma_{t-1}^2 + (1-\nu_\sigma) r_t^2$ with span $= 33$ days ($\nu_\sigma = 1 - 2/34$).
- Compute volatility-normalized daily returns:
  $$z_t = \frac{r_t}{\sigma_{t-1}}$$

### 2. European Filter Signal Generation

The strategy evaluates two primary filter types:
- **Variance-Preserving Single EWMA Filter ($\text{span}$):**
  $$S_t = \widetilde{\mathcal{L}}^{(\nu)}(z_t) = \sqrt{\frac{1+\nu}{1-\nu}} \sum_{m=0}^\infty \nu^m z_{t-m}, \quad \nu = 1 - \frac{2}{\text{span} + 1}$$
- **Variance-Preserving Long-Short EWMA Filter ($\text{span}_1, \text{span}_2$):**
  $$S_t = \widetilde{\mathcal{LS}}^{(\nu_1, \nu_2)}(z_t) = \frac{1}{\sqrt{q}} \left( \widetilde{\mathcal{L}}^{(\nu_1)}(z_t) - \widetilde{\mathcal{L}}^{(\nu_2)}(z_t) \right)$$
  where $q = 2 \frac{1 - \sqrt{(1-\nu_1^2)(1-\nu_2^2)} / (1 - \nu_1 \nu_2)}{(1+\nu_1)(1+\nu_2) / (1 - \nu_1 \nu_2)}$. Default industry benchmark: $\text{LS}(250, 20)$ ($\text{span}_1 = 250\text{d}, \text{span}_2 = 20\text{d}$).

### 3. Position Sizing & Rebalancing

- Continuous position weight per instrument:
  $$w_t = S_t \cdot w_t^{\text{vt}}, \quad w_t^{\text{vt}} = \frac{\sigma_{\text{target}}}{\sqrt{a}\sigma_t}$$
  where $\sigma_{\text{target}} = 0.15$ (15% annual vol target), and $a = 260$ (trading days/year).
- Daily strategy return:
  $$f_t = w_{t-1} r_t = \frac{\sigma_{\text{target}}}{\sqrt{a}} S_{t-1} z_t$$

### 4. American Discrete Discretization (Turnover Reduction Overlay)

- Form fast and slow EWMA on raw prices: $E_t^{\text{fast}}, E_t^{\text{slow}}$.
- Compute $\text{ATR}_t$ over 33 days.
- Long Entry: $E_t^{\text{fast}} > E_t^{\text{slow}} + \omega \cdot \text{ATR}_t$ (with buffer $\omega = 5$).
- Trailing Stop-Loss: Exit long if $p_t < \max_{s \le t} p_s - p \cdot \text{ATR}_t$ (with width $p = 5$).
- Binary position weight: $w_t \in \{-1, 0, +1\} \times w_t^{\text{vt}}$.

## Required data

- **Universe:** 84 liquid futures contracts across equity indices (S&P 500, Euro Stoxx 50, Nikkei 225), sovereign bonds (10Y UST, Bund, JGB), short-term interest rates (SOFR, Euribor), currencies (EUR, JPY, GBP, AUD), and commodities (Crude Oil, Gold, Copper, Corn).
- **Timeframe:** Daily settlement prices / close prices (1997–2026).
- **Fields:**
  - Daily continuous stitched prices $s_t$ (adjusted for contract roll wedges).
  - Daily relative return $r_t = (s_t - s_{t-1}) / s_{t-1}$.
  - Daily high, low, close for ATR computation.
  - Foreign exchange rates for non-USD contract conversion.
- **Point-in-Time Alignment:** Daily close signal formation; execution at end-of-day or next-open.

## Execution assumptions

- **Execution Timing:** End-of-day rebalancing (orders sampled shortly before market close).
- **Fractional Trading:** Contracts trade in fractions with net profits reinvested.
- **Turnover Definition:** Volatility-normalized turnover:
  $$U_t = \frac{1}{\sqrt{a}\sigma_t} |w_t - w_{t-1}|$$
- **Transaction Costs:** Volume-based tiered costs (rebalancing + rolling) following Hurst et al. (2017):
  - Equities: 2.0–3.0 bps.
  - Bonds & Rates: 0.5–1.5 bps.
  - FX: 1.0–2.0 bps.
  - Commodities: 3.0–8.0 bps.
  - Portfolio average: $c \approx 20\text{ bps}$ per unit of volatility-normalized turnover ($1.0\% - 1.7\%$ annual drag).

## Evidence

### Source-reported

All metrics below are directly reported by Artur Sepp and Vladimir Lucic (arXiv:2607.19497v1, July 2026):

1. **Closed-Form Sharpe Ratio Accuracy:**
   - Evaluated across 1,000 Monte Carlo paths of 50 years ($13,000$ daily observations per path):
   - Analytical Sharpe ratios match simulation estimates within $0.05$ across Gaussian, Student-t ($\nu=6, \kappa=3$), $\text{AR}(1)$, and $\text{ARFIMA}(1,d,0)$ processes.
   - Excess kurtosis $\kappa = 3$ lowers gross Sharpe ratio by $< 0.009$ (confirming kurtosis is a second-order effect).

2. **Empirical Futures Universe Attribution (84 Contracts, 1997–2026):**
   - **In-Sample Reconstruction:** Analytical formula predicts realized Sharpe ratios across 84 instruments with a pooled correlation $r = 0.99$ and regression slope $\beta = 0.96$.
   - **Decomposition:** Autocorrelation channel generates median Sharpe ratios from $0.55$ (5-day span) to $0.33$ (2-year span); the drift channel adds up to $+0.08$ (growing with span).
   - **Cross-System Correlation:** European and American systems correlate at $95\%$; all three systems correlate at $80\%$ with the SG Trend Index benchmark.

3. **Benchmark Replication & Robustness:**
   - Over December 1999 to June 2026 (net of 2%/20% fee structure and transaction costs):
     - European TF: Annualized Net Sharpe $= 0.47$.
     - American TF: Annualized Net Sharpe $= 0.50$.
     - TSMOM TF: Annualized Net Sharpe $= 0.55$.
     - SG Trend Index: Annualized Net Sharpe $= 0.47$.
   - Ledoit-Wolf bootstrap test confirms no statistically significant difference in Sharpe ratios ($p = 0.96, 0.82, 0.62$).

4. **Turnover & Cost Efficiency:**
   - Volatility-normalized annual turnover: $300\% - 400\%$ for European and TSMOM vs $125\% - 200\%$ for American TF.
   - American discrete buffer/stop-loss logic achieves $\approx 50\%$ lower turnover and execution costs than continuous rebalancing.

5. **Structural Aggregated Skewness:**
   - Cross-sectional median skewness of 100-day European TF on 84 futures contracts attains $2.33$ at a 55-day aggregation horizon, closely matching the closed-form theoretical peak of $2.35$ at $T \approx \text{span}/2$.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Short-Memory AR(1) Non-Viability Under Costs:**
   - For an $\text{AR}(1)$ process with $\phi = 0.05$, the theoretical break-even cost is $c_\infty^* = 37 - 41\text{ bps}$. Realistic implementation costs in fast futures ($40 - 60\text{ bps}$) completely erase the short-memory alpha, forcing the viable trading region to long spans ($\ge 60\text{d}$).
2. **Historical Autocorrelation Decay:**
   - First-lag autocorrelation $\rho(1)$ of volatility-normalized returns across liquid futures has decayed from $\approx 0.04$ (1990s) to $\approx 0.01$ (post-2010), reducing pure short-term trend alpha and increasing reliance on multi-asset cross-sectional carry and drift.
3. **In-Sample Drift Estimation Bias:**
   - Squared sample drift $(\bar{z}_T)^2 / \hat{\gamma}_T(0)$ has an upward bias of $a/T \approx 0.17$ on a 6-year history; naive unconstrained drift projections overstate out-of-sample Sharpe ratios.

## Falsification plan

1. **Shuffled-Time-Order Null Test:** Randomly permute the time ordering of daily returns $r_t$ within each asset (preserving mean, variance, and unconditional distribution while destroying autocorrelation). The European TF expected return must collapse to exactly $\frac{1}{\sqrt{a}} (\mu_{an}^z)^2 / \text{span}$, and at zero drift must equal zero. If simulated P&L remains significantly positive at zero drift, the execution pipeline contains lookahead leakage.
2. **Spectral Flat-Spectrum Test:** Generate synthetic paths with flat power spectra (white noise). Net Sharpe ratios must remain negative at fast spans ($< 30\text{d}$) under $c = 20\text{ bps}$.
3. **Break-Even Cost Horizon Test:** Stress test transaction costs $c \in [10, 100]\text{ bps}$. If the empirical net Sharpe ratio does not transition from fast-span optimality to slow-span optimality at the analytical threshold $c^* = \phi \sqrt{\pi / (2a)}$, the turnover cost model is rejected.
4. **Out-of-Sample Rolling Walk-Forward:** Calibrate optimal spans on 10-year rolling windows and evaluate on 3-year out-of-sample blocks across 2000–2026. If OOS Sharpe ratio drops by $> 50\%$ relative to in-sample attribution, the autocorrelation stability assumption fails.

## Crypto portability

**Portability Status:** `adapted` / `unproven`.

- **Crypto Application Potential:**
  - Trend-following strategies are widely deployed on liquid crypto perpetuals (BTC, ETH, SOL, top 20 altcoins) due to persistent directional momentum driven by retail sentiment, liquidations, and narrative cycles.
  - The long-short filter $\text{LS}(250, 20)$ or faster variants $\text{LS}(60, 10)$ map directly to continuous crypto perpetual rebalancing.
- **Portability Risks & Crypto-Specific Adaptations:**
  - **24/7/365 Trading Calendar:** Crypto markets trade continuously without weekends; annualization factor shifts from $a = 260$ to $a = 365$.
  - **Perpetual Funding Rate Drag:** Holding trend positions (long during bull runs, short during cascades) pays or receives 8-hour perpetual funding rates, which can exceed $10\% - 30\%$ annualized and substantially alter net drift.
  - **Higher Baseline Volatility & Kurtosis:** Daily crypto volatility ($50\% - 100\%$ annualized) and extreme tail kurtosis ($\kappa > 10$) amplify volatility estimator lag and require wider ATR buffers in American implementations.
  - **Execution Slippage & Liquidations:** Crypto perpetual order books suffer from flash slippage during cascade events, making continuous European linear sizing vulnerable to adverse execution compared to discrete stop-loss boundaries.

## Limitations

- **In-Sample Attribution Focus:** The empirical validation validates that the analytical formula reproduces historical performance given the realized autocorrelation and drift; it does not constitute an out-of-sample forecasting model.
- **Linearity vs Discretization Gap:** The exact closed-form solutions hold for European continuous filters; American and TSMOM implementations require empirical calibration slopes ($0.61 - 0.73$) to bridge the non-linear execution discount.
- **Market Impact Exclusion:** The volume-tiered cost model is proportional and excludes non-linear market impact, which becomes the dominant binding constraint for large CTA fund capacities ($> \$1\text{B}$).
- **Drift Non-Stationarity:** Unconditional drift parameters $\mu_{an}^z$ are non-stationary across macro regimes (e.g., secular bond bull market 1980–2020 vs 2021–2024 inflation shock).

## Implementation status

- `not-implemented`: No execution pipeline or backtest has been implemented in PyBroker or NautilusTrader.
- This document is a research-only capture of an external empirical study.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- Research capture does not authorize paper trading, testnet verification, or live capital allocation.

## Related Wiki records

- `[[quant/futures-volatility-normalized-tick-size-trend-following-filter-2026-09-02]]`
- `[[quant/crypto-adaptive-trend-following-asymmetric-portfolio-2026-09-01]]`
- `[[quant/crypto-dynamic-time-series-momentum-volatility-impulse-2026-08-31]]`
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`

## Sources

1. Artur Sepp and Vladimir Lucic. *"The Science and Practice of Trend-Following Systems"*, arXiv preprint `arXiv:2607.19497v1 [q-fin.ST, q-fin.MF]`, submitted July 21, 2026. URL: [https://arxiv.org/abs/2607.19497](https://arxiv.org/abs/2607.19497). Full text: [https://arxiv.org/html/2607.19497v1](https://arxiv.org/html/2607.19497v1).
2. Public replication code repository: [https://github.com/ArturSepp/TrendFollowingSystems](https://github.com/ArturSepp/TrendFollowingSystems) (Python package `trendfollowing`).
