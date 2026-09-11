---
schema: strategy-research-record-v1
title: "Expected Shortfall Factor Models: Common Tail Loss Severity and Cross-Sectional Expected Returns"
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - downside-risk
  - expected-shortfall
  - tail-risk
  - factor-models
  - cross-sectional-equity
  - latent-factors
status: research-only
confidence: medium
source_as_of: 2026-09-10
sources:
  - "https://arxiv.org/abs/2609.10587"
  - "https://arxiv.org/pdf/2609.10587"
  - "https://arxiv.org/html/2609.10587v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Expected Shortfall Factor Models: Common Tail Loss Severity and Cross-Sectional Expected Returns

## Provenance

- **Primary Source:** Yujie Hou, Xinbing Kong, Yalin Wang, and Bin Wu. *Expected Shortfall Factor Models: Common Tail Losses and Expected Returns*.
- **Identifiers:** arXiv preprint `arXiv:2609.10587v1 [econ.EM, q-fin.ST, stat.ME]`, submitted 10 September 2026, listed 11 September 2026. Under review at *Operations Research*.
- **Stable URLs:**
  - Abstract: [https://arxiv.org/abs/2609.10587](https://arxiv.org/abs/2609.10587)
  - PDF: [https://arxiv.org/pdf/2609.10587](https://arxiv.org/pdf/2609.10587)
  - Full HTML: [https://arxiv.org/html/2609.10587v1](https://arxiv.org/html/2609.10587v1)
- **Primary Data Analyzed in Source:**
  - Large cross-section of Chinese equities drawn from the CSI 300 index constituents (~250 liquid equities with stable time-series coverage).
  - Sample timeframe: January 2000 through December 2023 (24 years, 262 monthly rebalance periods).
  - Daily closing prices obtained from the Wind database.
  - Observable benchmark factors: Fama–French five factors (MKT, SMB, HML, RMW, CMA), Momentum (MOM), and the risk-free rate, in both value-weighted (VW) and equal-weighted (EW) configurations.
- **Source Quality:** Rigorous econometrics and asset pricing preprint establishing nonasymptotic finite-sample error bounds, Neyman-orthogonalized two-stage estimation, consistent factor-number selection criteria, extensive Monte Carlo simulations (7 scenarios), and exhaustive empirical asset pricing tests (univariate sorts, bivariate dependent sorts, Fama–MacBeth cross-sectional regressions, and factor-spanning regressions).

## Economic mechanism

### Source-reported

Conventional panel factor models decompose asset returns into common movements in conditional means (e.g., Connor & Korajczyk 1986; Bai 2009) or conditional quantile thresholds (Quantile Factor Models / QFM, e.g., Ando & Bai 2020; Chen et al. 2021; Baruník & Nevrla 2026). However, a conditional mean ignores the lower tail, and a conditional quantile provides only the boundary cutoff ($Q_\tau$), revealing nothing about the average return conditional on breaching that boundary. 

Two assets may exhibit identical 10% Value-at-Risk (quantile) thresholds but suffer drastically different expected losses conditional on being in that worst 10% of states. If the severity of these tail losses co-moves across assets, it represents a distinct source of systematic downside risk that cannot be recovered from conditional means or quantiles alone.

The Expected Shortfall Factor Model (ESFM) models conditional Expected Shortfall at tail level $\tau \in (0, 1)$:
$$\mathrm{ES}_\tau(Y_{it} \mid X_{it}, f_{t,\tau}) = X_{it}^\top \beta_{i,\tau}^0 + \lambda_{i,\tau}^{0\top} f_{t,\tau}^0$$
where $Y_{it}$ is the asset return, $X_{it}$ are observed systematic risk factors (e.g., Fama–French five factors), $f_{t,\tau}^0$ is an $r_\tau^0$-dimensional vector of unobservable latent tail-severity factors, and $\lambda_{i,\tau}^0$ is the asset-specific factor loading. The authors demonstrate that latent ES factors react sharply during severe market stress (such as the 2015 Chinese stock market crash and the March 2020 COVID-19 shock) and that cross-sectional exposure to these latent tail-loss severity factors commands a substantial, economically distinct risk premium.

### Research interpretation

This research identifies **common loss severity as an independent, priced dimension of downside risk**. 

1. **Beyond Mean and Quantile Risk:** Traditional beta measures sensitivity to overall market variance, while downside beta (Ang, Chen, and Xing 2006) and quantile factors (Baruník & Nevrla 2026) measure sensitivity to whether an asset enters its lower tail. ESFM isolates how severely an asset crashes *conditional on already entering the tail*.
2. **Catastrophe Loss Vulnerability:** Risk-averse investors with convex disutility over extreme losses demand an ex-ante return premium for holding assets that experience deeper drawdowns during systemic tail liquidation events.
3. **Neyman Orthogonality in Signal Extraction:** Because Expected Shortfall is not elicitable alone (Fissler & Ziegel 2016), estimation requires first-stage quantile threshold estimation. The two-stage orthogonalized score ensures that first-stage quantile estimation errors do not enter the second-stage ES coefficient or factor estimation to first order, protecting empirical factor loadings from threshold estimation noise.
4. **Asymmetric Long-Short Driver:** In empirical portfolios, the high-minus-low spread is heavily driven by the underperformance of low-exposure assets (P1 earns ~ -8% annualized, while P5 earns +1% to +3% annualized). This indicates that low ESFM exposure identifies assets that decouple from common catastrophic losses, commanding a substantial "safe-haven / crash-resilience" price premium (yielding depressed future average returns).

## Signal

- **Signal Formation & Rebalancing Cadence:** Rebalanced at the end of each calendar month $t$. Factor exposures are estimated using a rolling lookback window of 60 months (5 years) of daily returns ($T \approx 1{,}260$ trading days) across the universe of $N \approx 250$ stocks.
- **Tail Probability Level:** Evaluated across $\tau \in \{0.10, 0.20, 0.30\}$, centered on $\tau = 0.20$ to balance economic relevance of tail stress against finite-sample tail sparsity.
- **Two-Stage Estimation Procedure:**
  - **Stage 1 (Unit-by-Unit Quantile Regression):** For each stock $i \in [N]$, estimate conditional quantile coefficients $\widehat{\alpha}_{i,\tau} \in \mathbb{R}^{p+1}$ via Koenker-Bassett check loss:
    $$\widehat{\alpha}_{i,\tau} = \arg\min_{\alpha_{i,\tau} \in \mathbb{R}^{p+1}} \frac{1}{T} \sum_{t=1}^T \rho_\tau(Y_{it} - X_{it}^\top \alpha_{i,\tau}), \quad \rho_\tau(u) = (\tau - \mathbb{I}(u < 0)) u$$
    where $X_{it} = (1, \text{MKT}_t, \text{SMB}_t, \text{HML}_t, \text{RMW}_t, \text{CMA}_t)^\top$.
  - **Stage 2 (Orthogonalized ES Factor Extraction):**
    Construct the Neyman-orthogonalized response variable:
    $$Z_{it}(\widehat{\alpha}_{i,\tau}) = (Y_{it} - X_{it}^\top \widehat{\alpha}_{i,\tau}) \mathbb{I}(Y_{it} \le X_{it}^\top \widehat{\alpha}_{i,\tau}) + \tau X_{it}^\top \widehat{\alpha}_{i,\tau}$$
    Define standardized response $Z_{it}^*(\widehat{\alpha}_{i,\tau}) = \tau^{-1} Z_{it}(\widehat{\alpha}_{i,\tau})$.
    Extract $r=2$ latent factors $\widehat{F}_\tau \in \mathbb{R}^{T \times r}$ and loadings $\widehat{\Lambda}_\tau \in \mathbb{R}^{N \times r}$ via alternating least squares and PCA:
    1. Given factor matrix $F_\tau$ normalized such that $F_\tau^\top F_\tau / T = I_r$, estimate covariate coefficients:
       $$\widehat{\beta}_{i,\tau} = (X_i^\top M_{F_\tau} X_i)^{-1} (X_i^\top M_{F_\tau} Z_i^*(\widehat{\alpha}_{i,\tau}))$$
       where $M_{F_\tau} = I_T - F_\tau (F_\tau^\top F_\tau)^{-1} F_\tau^\top$.
    2. Form residual matrix $\widehat{W}_\tau \in \mathbb{R}^{N \times T}$ with elements $\widehat{W}_{it,\tau} = Z_{it}^*(\widehat{\alpha}_{i,\tau}) - X_{it}^\top \widehat{\beta}_{i,\tau}$.
    3. Update $\widehat{F}_\tau$ as $\sqrt{T}$ times the eigenvectors corresponding to the largest $r=2$ eigenvalues of $\frac{1}{NT} \widehat{W}_\tau^\top \widehat{W}_\tau$.
    4. Update loading matrix $\widehat{\Lambda}_\tau = \frac{1}{T} \widehat{W}_\tau \widehat{F}_\tau$.
    5. Iterate until convergence.
  - **Factor-Number Selection:** Number of latent factors $r=2$ is confirmed by the modified Information Criterion:
    $$\text{IC}_\tau(r) = \log \widehat{V}_\tau(r) + r \cdot \log\left(\frac{NT}{N+T}\right) \left(\frac{N+T}{NT}\right)$$
- **Cross-Sectional Ranking & Portfolio Weights:**
  - Rank all $N$ stocks by their estimated factor exposure (factor-mimicking portfolio loading) into 5 quintiles ($P_1$ to $P_5$) or 10 deciles ($D_1$ to $D_{10}$).
  - Long portfolio: $P_5$ (highest exposure to ESFM risk), equal-weighted across constituent stocks.
  - Short portfolio: $P_1$ (lowest exposure to ESFM risk), equal-weighted across constituent stocks.
  - High-minus-Low (H–L) spread: $R_{t+1}^{\text{H-L}} = R_{t+1}^{P_5} - R_{t+1}^{P_1}$.
- **Holding Period:** 1 calendar month ($t \dots t+1$).

## Required data

- **Universe:** Large-cap liquid equities (constituents of the CSI 300 index, approximately 250 continuously traded Chinese equities).
- **Venue:** Shanghai Stock Exchange (SSE) and Shenzhen Stock Exchange (SZSE); primary data vendor in source: Wind Financial Database.
- **Market Type:** Spot cash equity.
- **Timeframe:** Daily closing prices for factor estimation; monthly rebalanced portfolio returns for cross-sectional pricing.
- **Sample Range:** January 2000 through December 2023 (24 continuous years).
- **Fields:** Daily closing prices, split/dividend adjustments, total market capitalization, Fama–French five factors (Market, SMB, HML, RMW, CMA), Momentum factor (MOM), risk-free rate ($R_f$).
- **Missing Data Handling:** Equities with substantial missing records or IPO seasoning shorter than the 60-month lookback window are excluded from the rolling estimation panel until sufficient continuous daily history exists.

## Execution assumptions

- **Rebalance Cadence:** Monthly at calendar month-end.
- **Signal-to-Order Timing / Fill Model:** Evaluated on monthly close-to-close returns (`research-proposed fill model`: orders executed at the closing auction of the last trading day of the month or market open on the first trading day of the subsequent month).
- **Transaction Costs & Fees:** Third-party paper backtests report gross returns with zero explicit transaction costs deducted (`research-proposed execution caveat`: in China A-shares, institutional trading costs include 0.05% stamp tax on selling, 0.01%–0.03% broker commissions, and 0.02%–0.05% execution slippage).
- **Shorting / Borrow Availability:** The paper assumes an unconstrained dollar-neutral long/short spread ($+1.0$ on $P_5$, $-1.0$ on $P_1$). In physical Chinese equity markets, securities lending for shorting is heavily restricted, illiquid, or subject to prohibitive borrowing fees (6%–12% APR) (`research-proposed operational requirement`: physical long-short execution requires synthetic implementation via CSI 300 index futures hedging or equity swap margin financing).
- **Weighting Scheme:** Equal-weighted (EW) across stocks within each quintile/decile; observable benchmark factors evaluated in both value-weighted (VW) and equal-weighted (EW) specifications.

## Evidence

### Source-reported

All empirical figures below are extracted directly from the published tables and text of Hou, Kong, Wang, and Wu (arXiv:2609.10587v1):

#### 1. Annualized Portfolio Returns and Factor Alphas (Table 5.3.1, CSI 300 Panel 2000–2023, 262 Months)

Stocks sorted into 5 quintile portfolios or 10 decile portfolios based on estimated factor exposures (preceding 60-month window). Benchmark factors constructed using value-weighted (VW) returns; Newey–West $t$-statistics with 6 lags shown in parentheses:

| Sorting Scheme | Model | Tail Level $\tau$ | Annualized Mean H–L Return | CAPM Alpha | FF3 Alpha | FF5 Alpha |
|:---|:---|:---:|:---:|:---:|:---:|:---:|
| **5 Portfolios** | **ESFM** | **$\tau = 0.10$** | **8.04%** ($t=2.62$) | **9.01%** ($t=3.09$) | **9.40%** ($t=3.38$) | **10.31%** ($t=3.33$) |
| 5 Portfolios | Mean-IFE | Any $\tau$ | 5.29% ($t=2.19$) | 5.20% ($t=2.14$) | 5.33% ($t=2.19$) | 5.18% ($t=2.18$) |
| 5 Portfolios | QFM | $\tau = 0.10$ | 5.05% ($t=1.80$) | 5.92% ($t=2.13$) | 5.71% ($t=1.97$) | 5.73% ($t=1.87$) |
| **5 Portfolios** | **ESFM** | **$\tau = 0.20$** | **10.27%** ($t=3.08$) | **11.26%** ($t=3.49$) | **11.75%** ($t=3.84$) | **12.25%** ($t=3.61$) |
| 5 Portfolios | Mean-IFE | Any $\tau$ | 5.29% ($t=2.19$) | 5.20% ($t=2.14$) | 5.33% ($t=2.19$) | 5.18% ($t=2.18$) |
| 5 Portfolios | QFM | $\tau = 0.20$ | 5.29% ($t=1.87$) | 5.98% ($t=2.07$) | 6.13% ($t=2.13$) | 8.38% ($t=2.51$) |
| **5 Portfolios** | **ESFM** | **$\tau = 0.30$** | **10.20%** ($t=2.96$) | **11.28%** ($t=3.41$) | **11.81%** ($t=3.78$) | **12.34%** ($t=3.48$) |
| 5 Portfolios | Mean-IFE | Any $\tau$ | 5.29% ($t=2.19$) | 5.20% ($t=2.14$) | 5.33% ($t=2.19$) | 5.18% ($t=2.18$) |
| 5 Portfolios | QFM | $\tau = 0.30$ | 3.77% ($t=1.22$) | 3.87% ($t=1.24$) | 4.43% ($t=1.58$) | 5.25% ($t=1.48$) |
| **10 Portfolios** | **ESFM** | **$\tau = 0.10$** | **9.34%** ($t=2.48$) | **10.55%** ($t=2.99$) | **11.02%** ($t=3.28$) | **13.09%** ($t=3.33$) |
| 10 Portfolios | Mean-IFE | Any $\tau$ | 8.27% ($t=2.54$) | 8.23% ($t=2.52$) | 8.52% ($t=2.60$) | 8.14% ($t=2.59$) |
| 10 Portfolios | QFM | $\tau = 0.10$ | 7.76% ($t=2.23$) | 8.74% ($t=2.53$) | 8.42% ($t=2.33$) | 8.26% ($t=2.11$) |
| **10 Portfolios** | **ESFM** | **$\tau = 0.20$** | **10.78%** ($t=2.73$) | **11.97%** ($t=3.13$) | **12.54%** ($t=3.46$) | **14.04%** ($t=3.28$) |
| 10 Portfolios | Mean-IFE | Any $\tau$ | 8.27% ($t=2.54$) | 8.23% ($t=2.52$) | 8.52% ($t=2.60$) | 8.14% ($t=2.59$) |
| 10 Portfolios | QFM | $\tau = 0.20$ | 6.88% ($t=1.90$) | 7.79% ($t=2.09$) | 8.01% ($t=2.18$) | 10.56% ($t=2.47$) |
| **10 Portfolios** | **ESFM** | **$\tau = 0.30$** | **11.68%** ($t=2.84$) | **13.01%** ($t=3.27$) | **13.69%** ($t=3.69$) | **14.96%** ($t=3.39$) |
| 10 Portfolios | Mean-IFE | Any $\tau$ | 8.27% ($t=2.54$) | 8.23% ($t=2.52$) | 8.52% ($t=2.60$) | 8.14% ($t=2.59$) |
| 10 Portfolios | QFM | $\tau = 0.30$ | 4.28% ($t=1.19$) | 4.49% ($t=1.24$) | 5.10% ($t=1.54$) | 7.28% ($t=1.92$) |

#### 2. Monotonic Return Gradient Across Exposure Quintiles (Figure 5.3.1)

Average annualized returns display a strict monotonic upward progression from lowest exposure ($P_1$) to highest exposure ($P_5$) across all six combinations of tail level ($\tau \in \{0.10, 0.20, 0.30\}$) and factor weighting (VW and EW):
- $P_1$ (Lowest ESFM Exposure): ~ $-8.0\%$ p.a.
- $P_2$: ~ $-5.0\%$ p.a.
- $P_3$: ~ $-2.0\%$ p.a.
- $P_4$: ~ $0.0\%$ p.a.
- $P_5$ (Highest ESFM Exposure): $+1.0\%$ to $+3.0\%$ p.a.

#### 3. Two-Pass Fama–MacBeth Cross-Sectional Pricing Regressions (Table 5.3.2)

Estimated prices of risk ($\times 100$) in monthly cross-sections:
- **Univariate ESFM risk price:** $+1.3647$ ($\tau=0.10$), $+1.5763$ ($\tau=0.20$), $+1.6291$ ($\tau=0.30$).
- **Joint specification with Mean and QFM:** ESFM risk price remains positive and statistically dominant at $+0.9168$ ($\tau=0.10$), $+1.5114$ ($\tau=0.20$), $+1.4751$ ($\tau=0.30$).
- **Controlling for Fama–French Five Factors:** ESFM risk price remains $+0.9540$ ($\tau=0.10$, $R^2=7.58\%$), $+1.1411$ ($\tau=0.20$, $R^2=7.64\%$), $+1.0543$ ($\tau=0.30$, $R^2=7.73\%$).

#### 4. Factor Spanning Regressions & Mean–Variance Efficiency (Table 5.3.3)

Regressing the traded ESFM H–L factor on MKT, SMB, HML, RMW, CMA, MOM, and the corresponding Mean and QFM factors:
- **Value-Weighted Observable Factor Specification:**
  - $\tau = 0.10$: Spanning alpha $\alpha = 6.60\%$ p.a. ($t = 2.80$), Mean loading $0.336$ ($t=2.94$), QFM loading $0.361$ ($t=3.94$), $R^2 = 48.85\%$. Maximum Sharpe ratio expands from $1.56$ (benchmarks) to **$1.78$** (with ESFM), $\Delta \text{SR}^2 = 0.723$.
  - $\tau = 0.20$: Spanning alpha $\alpha = 8.65\%$ p.a. ($t = 2.48$), Mean loading $0.467$ ($t=4.09$), QFM loading $0.161$ ($t=1.70$), $R^2 = 42.59\%$. Maximum Sharpe ratio expands from $1.64$ to **$1.90$**, $\Delta \text{SR}^2 = 0.921$.
  - $\tau = 0.30$: Spanning alpha $\alpha = 9.37\%$ p.a. ($t = 2.70$), Mean loading $0.546$ ($t=4.60$), QFM loading $0.085$ ($t=0.90$), $R^2 = 45.52\%$. Maximum Sharpe ratio expands from $1.52$ to **$1.82$**, $\Delta \text{SR}^2 = 1.010$.
- **Equal-Weighted Observable Factor Specification:**
  - $\tau = 0.10$: $\alpha = 7.35\%$ p.a. ($t = 3.39$), Max SR expands from $1.78$ to **$2.02$**, $\Delta \text{SR}^2 = 0.892$.
  - $\tau = 0.20$: $\alpha = 7.91\%$ p.a. ($t = 3.09$), Max SR expands from $1.81$ to **$2.05$**, $\Delta \text{SR}^2 = 0.898$.
  - $\tau = 0.30$: $\alpha = 8.66\%$ p.a. ($t = 3.14$), Max SR expands from $1.78$ to **$2.04$**, $\Delta \text{SR}^2 = 0.990$.

#### 5. Dependent Bivariate Conditional Sorts (Figure 5.3.3)

Conditioning on QFM exposure, Mean exposure, or idiosyncratic volatility in $5 \times 5$ sorts, or on joint QFM–Mean in $3 \times 3 \times 5$ sorts:
- Annualized conditional H–L return spreads remain between **$5.6\%$ and $9.9\%$** p.a. across all conditioning specifications.
- In every case, the 95% Newey–West confidence intervals remain strictly bounded above zero.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Joint Wald Test Failure Across Tail Levels:** While tail-by-tail spanning alphas are statistically significant individually ($t > 2.48$), the joint Wald test that all three ESFM alphas ($\tau \in \{0.10, 0.20, 0.30\}$) are simultaneously zero under value-weighted benchmark factors fails to reject the null ($\chi^2(3) = 4.50$, $p = 0.213$). Under equal-weighted factors, joint significance is marginal ($p = 0.058$). Joint multi-tail claims are therefore unproven.
- **Short-Leg Skewness & Implementation Barrier:** As shown in Figure 5.3.1, the spread is asymmetric: the long leg ($P_5$) produces modest absolute annualized gains ($+1\%$ to $+3\%$), while the short leg ($P_1$) drives the bulk of the spread through deep negative absolute returns ($-8\%$). In markets where shorting is constrained or expensive (e.g., China A-shares with 6%–12% borrow fees), capturing this spread via cash equity is economically eroded.
- **Frictionless Backtest Bias:** The paper evaluates gross returns. Factoring in China A-share turnover friction (0.05% stamp tax on selling plus commissions and slippage) would reduce net performance, though monthly rebalancing keeps turnover relatively modest compared to daily strategies.
- **Factor Loading Instability in Deep Tails:** In Table 5.3.3, the ESFM factor loading on the QFM factor drops from $0.361$ ($t=3.94$) at $\tau=0.10$ down to $0.085$ ($t=0.90$, statistically insignificant) at $\tau=0.30$, indicating structural shift in factor spanning across tail depths.

## Falsification plan

1. **Transaction Cost and Short-Borrow Stress Test:**
   - Subtract realistic institutional execution frictions: 10 bps one-way trading costs, 0.05% selling stamp tax, and an annual short-borrow fee of 6.0%–10.0% APR on the short leg ($P_1$).
   - `research-defined falsification threshold`: If net annualized H–L return drops below 3.0% or net Sharpe ratio drops below 0.35, reject the operational tradeability of the physical cash-equity long/short strategy.
2. **Lookback Estimation Window Compression:**
   - Compress the rolling estimation window from 60 months down to 24 months and 36 months to test whether the latent factor structure requires decades of data or adapts to local regime shifts.
   - `research-defined falsification threshold`: If the out-of-sample Fama–French five-factor alpha drops below 4.0% p.a. or loses statistical significance ($t < 1.96$) under a 36-month lookback, reject the structural stability of the estimated ES loadings.
3. **Cross-Asset / Crypto Portability Validation:**
   - Implement the two-stage ESFM algorithm on a panel of the top 40 liquid cryptocurrency perpetual contracts (e.g., on Binance or Hyperliquid), using a 180-day lookback of 8-hour funding-inclusive returns and $\tau = 0.15$.
   - `research-defined falsification threshold`: If the high-minus-low ESFM crypto spread yields a negative net Sharpe ratio or fails to produce a positive alpha over the market-cap-weighted crypto index ($t < 1.65$), reject cross-asset portability of the loss-severity mechanism.
4. **Placebo Shuffled Tail Residual Test:**
   - On days where more than 10% of stocks cross their first-stage $\tau$-quantile threshold, randomly permute the residual loss magnitudes $Z_{it}^* - X_{it}^\top \beta_{i,\tau}$ across assets while preserving marginal distributions.
   - `research-defined falsification threshold`: If the placebo ESFM factors produce an H–L spread whose alpha exceeds 50% of the empirical ESFM alpha, reject the claim that cross-sectional tail comovement (rather than individual asset variance) drives the return premium.
5. **Multi-Horizon Holding Period Decay:**
   - Evaluate holding periods of 1 week, 2 weeks, 1 month, 3 months, and 6 months without rebalancing.
   - `research-defined falsification threshold`: If the H–L return alpha collapses to zero within 2 weeks ($t < 1.0$), classify the signal as high-frequency microstructure rebound rather than a persistent systematic risk premium.

## Crypto portability

- **Portability Status:** `adapted / unproven`.
- **Primary Source Asset Class:** Tested exclusively on Chinese cash equities (CSI 300 constituents); no cryptocurrency assets evaluated in the source.
- **Economic Thesis in Crypto (`research-proposed`):**
  - Crypto markets exhibit extreme kurtosis, heavy negative tail skewness, and frequent cascading liquidations where cross-asset correlations spike toward unity.
  - While mean factor models and simple VaR cutoffs fail during market crashes, ESFM's explicit modeling of *within-tail loss severity* makes it theoretically well-suited to identifying altcoins that suffer catastrophic drawdown amplification during Bitcoin crash cascades.
  - Crucially, unlike Chinese equities where shorting is constrained, cryptocurrency perpetual contracts provide frictionless two-sided shorting. Because the equity spread was primarily driven by the underperformance of crash-resilient stocks ($P_1$), shorting high-tail-loss tokens ($P_5$) or longing low-tail-loss tokens ($P_1$) can be executed directly in perpetual markets without securities lending friction.
- **Crypto-Specific Implementation Hurdles:**
  1. *Funding Rate Carry Risk:* During severe market liquidations, perpetual swap funding rates can turn intensely negative (shorts pay longs up to -100% APR annualized). A long/short book held across monthly intervals could suffer severe funding rate drag. Returns $Y_{it}$ must be total economic returns including 8-hour funding payments.
  2. *Lookback Compression:* A 60-month lookback in crypto spans an entire market epoch; crypto implementation requires compressing lookback windows to 90–180 days (or using hourly bars over 30–60 days).
  3. *Continuous 24/7 Trading:* Daily bars must be synchronized to a uniform UTC boundary (e.g., 00:00:00 UTC) to prevent asynchronous tail estimation error.
  4. *Survivorship & Liquidity Attrition:* The crypto altcoin universe suffers frequent delistings and catastrophic collapses (e.g., LUNA, FTT). A dynamic rolling universe filter (e.g., 30-day ADV $> \$20\text{M}$) is mandatory to prevent survivor bias.

## Limitations

- **Short-Leg Asymmetry:** Empirical profits in equities stem primarily from the short leg ($P_1$ at $-8\%$ p.a.), making real-world cash equity extraction subject to borrow availability and margin interest.
- **Joint Significance Ambiguity:** Joint Wald tests for spanning alphas across multiple tail levels failed the 5% significance barrier ($p = 0.213$ under VW factors), indicating that statistical strength is localized to individual tail choices rather than uniform across the entire tail spectrum.
- **Unmodeled Execution Costs:** Baseline paper backtests do not incorporate broker fees, stamp taxes, or market impact.
- **High Data History Requirement:** The 60-month rolling window restricts the eligible universe to assets with extensive, continuous history, introducing survivorship and listing age biases.
- **Non-Elicitable First Stage:** Expected Shortfall requires a first-stage quantile regression. While Neyman orthogonality removes first-order bias, small sample sizes or extreme tail thresholds ($\tau < 0.01$) can destabilize the pseudo-response $Z_{it}^*$.
- **Not Independently Reproduced:** All performance metrics and alphas are third-party source-reported figures.

## Implementation status

`not-implemented`. This record is a research capture and specification only. No algorithm has been integrated into NautilusTrader, PyBroker, or our production pipelines, and no live, paper, or testnet trading is authorized.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- A strategy record being present here indicates only that the research has been normalized into canonical specification format. It does not imply that the strategy is profitable, approved for implementation, or authorized for paper, testnet, or live trading.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` (canonical strategy research specification)
- `[[quant/entropic-value-at-risk-parity-tempered-stable-returns-2026-09-11]]` (EVaR tail risk budgeting and tempered stable returns)
- `[[quant/crypto-cross-sectional-extreme-downside-risk-var-2026-09-01]]` (extreme downside risk and VaR premia in crypto cross-sections)
- `[[quant/size-enhanced-left-side-momentum-resga-expected-shortfall-2026-09-04]]` (expected shortfall conditioning in momentum portfolios)
- `[[quant/crypto-bitcoin-cvar-risk-aware-q-learning-adaptive-controller-2026-09-02]]` (CVaR downside risk control in automated execution)

## Sources

1. Hou, Yujie, Xinbing Kong, Yalin Wang, and Bin Wu. "Expected Shortfall Factor Models: Common Tail Losses and Expected Returns." arXiv preprint `arXiv:2609.10587v1 [econ.EM, q-fin.ST, stat.ME]`, submitted 10 September 2026, listed 11 September 2026. Stable URL: [https://arxiv.org/abs/2609.10587](https://arxiv.org/abs/2609.10587). Full HTML: [https://arxiv.org/html/2609.10587v1](https://arxiv.org/html/2609.10587v1). PDF: [https://arxiv.org/pdf/2609.10587](https://arxiv.org/pdf/2609.10587).
2. Portfolio Returns & Alphas: Table 5.3.1 (same source). CSI 300 equity panel (2000–2023, 262 months). Annualized H–L returns: 8.04% ($\tau=0.10$, $t=2.62$), 10.27% ($\tau=0.20$, $t=3.08$), 10.20% ($\tau=0.30$, $t=2.96$); FF5 Alphas: 10.31% ($\tau=0.10$, $t=3.33$), 12.25% ($\tau=0.20$, $t=3.61$), 12.34% ($\tau=0.30$, $t=3.48$). Decile H–L FF5 Alphas: 13.09% ($\tau=0.10$), 14.04% ($\tau=0.20$), 14.96% ($\tau=0.30$).
3. Two-Pass Cross-Sectional Regressions: Table 5.3.2 (same source). Fama–MacBeth risk prices controlling for FF5: 0.9540 ($\tau=0.10$), 1.1411 ($\tau=0.20$), 1.0543 ($\tau=0.30$).
4. Factor Spanning Regressions: Table 5.3.3 (same source). Spanning alphas controlling for MKT, SMB, HML, RMW, CMA, MOM, Mean factor, and QFM factor: 6.60% ($\tau=0.10$, $t=2.80$, Max SR 1.78 vs 1.56), 8.65% ($\tau=0.20$, $t=2.48$, Max SR 1.90 vs 1.64), 9.37% ($\tau=0.30$, $t=2.70$, Max SR 1.82 vs 1.52). Joint Wald test: $\chi^2(3) = 4.50$, $p = 0.213$ (VW); $\chi^2(3) = 7.49$, $p = 0.058$ (EW).
5. Quintile Return Monotonicity: Figure 5.3.1 (same source). Strict monotonic upward gradient from $P_1$ (~ -8% p.a.) to $P_5$ (+1% to +3% p.a.).
6. Dependent Bivariate Conditional Sorts: Figure 5.3.3 (same source). Conditional H–L return spreads of 5.6%–9.9% p.a. controlling for QFM, Mean, and idiosyncratic volatility.
7. Methodology & Econometric Foundations: Section 2 & Section 3 (same source). Check-loss quantile regression (Koenker & Bassett 1978), Neyman-orthogonalized ES regression (Barendse 2020; He et al. 2023b), and PCA factor extraction (Bai & Ng 2002, 2013).
