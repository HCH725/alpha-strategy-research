---
schema: strategy-research-record-v1
title: "Cross-Market Alpha: Testing Short-Term Trading Factors in the U.S. Market via Double-Selection LASSO"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-market-alpha
  - alpha191
  - double-selection-lasso
  - factor-investing
  - short-term-reversal
  - volume-price-interaction
  - high-dimensional-econometrics
status: research-only
confidence: medium
source_as_of: 2026-05-21
sources:
  - "https://arxiv.org/abs/2601.06499"
  - "https://doi.org/10.48550/arXiv.2601.06499"
  - "https://arxiv.org/html/2601.06499v2"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Market Alpha: Testing Short-Term Trading Factors in the U.S. Market via Double-Selection LASSO

## Provenance

- **Primary paper:** Jin Du, Alexander Walter, and Maxim Ulrich, *Cross-Market Alpha: Testing Short-Term Trading Factors in the U.S. Market via Double-Selection LASSO*, arXiv preprint `arXiv:2601.06499v2 [q-fin.ST]`, first submitted January 10, 2026, revised May 21, 2026. DOI: `10.48550/arXiv.2601.06499`.
- **Authors & Affiliations:**
  - Jin Du (Equal contribution, `jin.du@partner.kit.edu`), Karlsruhe Institute of Technology (KIT).
  - Alexander Walter (Equal contribution, Corresponding author, `alexander.walter@partner.kit.edu`), Karlsruhe Institute of Technology (KIT).
  - Maxim Ulrich (`maxim.ulrich@kit.edu`), Karlsruhe Institute of Technology (KIT).
- **Primary source text:** Full unabridged LaTeX source files (`main.tex`, `references.bib`, and figures) retrieved directly from the official arXiv source bundle (`https://arxiv.org/src/2601.06499` and `https://arxiv.org/html/2601.06499v2`, release May 2026).
- **License:** arXiv.org perpetual non-exclusive license.
- **Source/data as-of:** 2026-05-21 (revised preprint release). Empirical panel covers 2002-01-01 to 2022-12-31 (21 years).
- **Source-identity deduplication:** Repository-wide inspection confirmed zero existing records citing `2601.06499`, `Jin Du`, `Alexander Walter`, `Maxim Ulrich`, `Alpha191`, or `Double-Selection LASSO`. While adjacent records examine high-dimensional asset pricing (e.g. Aldridge 2026 on Kyle's lambda or Le Grice 2026 on TabNet), this paper provides an independent high-dimensional econometric evaluation of 168 short-term trading signals from the Chinese Alpha191 library (Guotai Junan Securities, 2017) evaluated against 151 fundamental factors from the Jensen, Kelly, and Pedersen (2023) equity factor zoo on the U.S. S&P 500 panel.

## Economic mechanism

### Source-reported

1. **Dual-Horizon Pricing and the Factor Zoo Gap:** Classical empirical asset pricing (Fama and French, 1992, 1993, 2015; Hou, Xue, and Zhang, 2015) relies predominantly on slow-moving fundamental accounting metrics (book-to-market, profitability, investment growth). While meta-studies document a massive "factor zoo" of hundreds of anomalies (Harvey et al., 2016; Jensen et al., 2023), these slow factors suffer from institutional crowding, diminished post-publication returns (McLean and Pontiff, 2016), and fail to reflect real-time, sentiment-driven market dislocations. Conversely, high-frequency trading signals capture fast participant dynamics but are often dismissed as fleeting noise. Du, Walter, and Ulrich propose bridging this gap via a dual-horizon framework: integrating fast trading footprints with slow fundamental anchors.
2. **Behavioral Universality across Heterogeneous Market Structures:** The Chinese A-share market is structurally retail-dominated (~60% of trading volume per CSDC reports), generating pronounced speculative overreaction, herding, and liquidity-seeking behavior (Li et al., 2014; Liu et al., 2019). The Alpha191 factor library (Guotai Junan Securities, 2017) was engineered to systematically catalog these price-volume, momentum, and order-flow patterns. The authors hypothesize *Behavioral Universality*: psychological biases (overreaction, herding, attention constraints, limits to arbitrage; Daniel et al., 1998; Hirshleifer, 2001; Shleifer and Vishny, 1997) represent innate human cognitive traits rather than market-specific quirks. Testing whether retail-derived A-share signals survive in the highly institutionalized, informationally efficient U.S. S&P 500 large-cap universe provides a stringent cross-market hurdle.
3. **Omitted Variable Bias (OVB) and Multicollinearity in High Dimensions:** Standard single-step LASSO (SS) or OLS applied to high-dimensional factor libraries ($p > n$) suffers from severe coefficient instability and sign flips because standard $L_1$ shrinkage penalizes all variables simultaneously, discarding weak but critical confounding controls. To establish valid post-selection inference, the study adopts the Double-Selection (DS) LASSO framework (Belloni, Chernozhukov, and Hansen, 2014; Feng, Giglio, and Xiu, 2020), which separately screens outcome drivers and factor confounders before executing unpenalized joint inference with heteroskedasticity-robust standard errors.
4. **Thematic Clustering of Surviving Alphas:** 17 of 168 tested Alpha191 factors survive the DS-LASSO hurdle against 151 fundamental controls with $|t| > 2.0$ ($p < 0.05$). They cluster into three primary behavioral mechanisms:
   - *Short-Term Mean Reversion:* Extreme price extensions relative to moving averages or intraday ranges (e.g. Multi-Period Mean Reversion Ratio [046], 24-Day Percentage Deviation from Mean [071]) generate predictable corrections not spanned by Book-to-Market (HML) or Size (SMB).
   - *Volume-Price Interactions & Order Flow Conviction:* Volume conveys information orthogonal to price changes (Blume, Easley, and O'Hara, 1994). Cumulative On-Balance Volume (084), Price-Volume vs. Low-Volume Correlation Ranks (123), and Volume MACD Histograms (155) capture footprints of strategic institutional order splitting (Kyle, 1985; De Long et al., 1990).
   - *Volatility & Non-Linear Risk Pricing:* Higher-order moments and asymmetric range volatility (Benchmark-Relative Excess Return Skewness [181], 12-Day Average True Range [161], Inverse Rank of Intraday Volatility and Correlation [054]) reflect compensation for non-linear crash risk and intraday uncertainty.

### Research interpretation

From a quantitative strategy research perspective, Du, Walter, and Ulrich establish that:
- High-velocity trading signals originating from retail-heavy order flow do not wash out when aggregated over a monthly rebalancing horizon. Instead, 110 of 168 factors show monotonic increases in Newey-West $t$-statistics as the horizon expands from 1 day to 21 days, proving that they capture slow-decaying information diffusion and structural liquidity demand rather than fleeting microsecond noise.
- The severe instability and sign flipping of single-stage LASSO (where 14 of 17 factors flip sign or lose significance) demonstrates that empirical factor evaluation without confounder protection is fundamentally unreliable.
- An institutional investor can harvest a dual-horizon risk premium by pairing slow fundamental style factors (low turnover, high capacity) with orthogonal fast price-volume and mean-reversion signals, providing significant diversification during regime shifts when fundamental models suffer synchronized drawdowns.

## Signal

### 1. Data Cleaning & Variable Exclusion
- **Universe:** S&P 500 constituents (historical point-in-time membership from CRSP and OptionMetrics IvyDB, 2002–2022).
- **Filters:** Common equity (CRSP share codes 10/11) on NYSE, AMEX, or NASDAQ. Penny stocks priced below $5 are excluded.
- **Factor Screen:** Of the 191 original Alpha factors, 23 discontinuous or numerically unstable factors are dropped prior to analysis (due to zero-division risks, high missingness, or unstable time series in rolling windows), leaving 168 candidate factors.
- **Rolling Window:** 252 trading days per stock for computing time-series indicators and rolling ranks.

### 2. Signal Construction & Monthly Horizon Aggregation
- **Daily Signal Calculation:** Daily factor values are computed across all eligible constituents.
- **Decile Long-Short Portfolios:** Each day, stocks are sorted into value-weighted high-minus-low decile portfolios based on market capitalization.
- **Scaled Monthly Aggregation:** Daily high-minus-low return series are aggregated to a monthly rebalancing frequency by scaling the 21-day mean return:
  $$r_{m,t} = 21 \times \left( \frac{1}{21} \sum_{\tau=1}^{21} r_{d,\tau} \right)$$
  (Validated via paired $t$-test: for 134 of 168 factors, scaled-average returns are statistically indistinguishable from compounded monthly returns with $p > 0.05$).

### 3. Test Asset Portfolios
- **Bivariate $3 \times 2$ Sorts:** Independent sorts on Size (3 bins) and Factor (2 bins), generating 1,008 Alpha portfolios and 918 Jensen control portfolios ($N = 1,926$ test assets).
- **Bivariate $5 \times 5$ Sorts:** Independent sorts on Size (5 quintiles) and Factor (5 quintiles), generating 4,200 Alpha portfolios and 3,825 Jensen control portfolios ($N = 8,025$ test assets) for tail-granularity testing.

### 4. The Three-Stage Double-Selection LASSO Econometric Engine

Let $\bar{r} \in \mathbb{R}^N$ denote the time-series mean vector of test asset portfolio returns, and $\widehat{\text{Cov}}(\boldsymbol{r}_t, \boldsymbol{h}_t) \in \mathbb{R}^{N \times p}$ denote sample covariances with $p = 151$ fundamental control factors. Let $\widehat{\text{Cov}}(\boldsymbol{r}_t, \boldsymbol{g}_{t,j}) \in \mathbb{R}^N$ denote sample covariances with candidate Alpha factor $j \in \{1,\dots,d\}$ ($d = 168$).

- **Stage 1 (Outcome Driver Selection):** Penalized cross-sectional LASSO of mean portfolio returns on control factor covariances:
  $$\min_{\gamma, \lambda} \left\{ \frac{1}{N} \left\| \bar{r} - \iota_N \gamma - \widehat{\text{Cov}}(\boldsymbol{r}_t, \boldsymbol{h}_t)\lambda \right\|_2^2 + \tau_0 \frac{1}{N} \|\lambda\|_1 \right\}$$
  where $\iota_N$ is a vector of ones and $\gamma$ is an unpenalized zero-beta intercept. Non-zero coefficients define the active control set $I_1$.
- **Stage 2 (Confounder Selection):** For each candidate Alpha factor $j$, regress its portfolio covariance on the full set of control covariances:
  $$\min_{\xi_j, \chi_j} \left\{ \frac{1}{N} \left\| \widehat{\text{Cov}}(\boldsymbol{r}_t, \boldsymbol{g}_{t,j}) - \iota_N \xi_j - \widehat{\text{Cov}}(\boldsymbol{r}_t, \boldsymbol{h}_t)\chi_j \right\|_2^2 + \tau_{1j} \frac{1}{N} \|\chi_j\|_1 \right\}$$
  Non-zero coefficients identify controls correlated with candidate alpha exposures, forming $I_{2,j}$. The union across all test alphas forms $I_2 = \bigcup_j I_{2,j}$.
- **Stage 3 (Post-Selection Joint Inference):** Perform unpenalized cross-sectional OLS of portfolio mean returns on the union $I_1 \cup I_2$ plus the full test alpha vector $\boldsymbol{g}_t$:
  $$\bar{r} = \iota_N \gamma_0 + \widehat{\text{Cov}}(\boldsymbol{r}_t, \boldsymbol{h}_{t, I_1 \cup I_2}) \lambda_h + \widehat{\text{Cov}}(\boldsymbol{r}_t, \boldsymbol{g}_t) \lambda_g + \epsilon$$
  Estimated with HC3 heteroskedasticity-robust covariance matrix. A factor is certified as carrying statistically significant incremental risk premium if $|t(\hat{\lambda}_{g,j})| > 2.0$ ($p < 0.05$).
- **Regularization Tuning:** LassoCV with 200 candidate penalty values, 10-fold cross-validation, and $\epsilon = 0.05$. Final penalty selected via the **1-SE rule** (choosing the most restrictive penalty within one standard error of minimum MSE to enforce parsimony and avoid overfitting in $p > n$).

### 5. Mathematical Formulations of the 17 Certified Alpha Signals

1. **Alpha 046 (Multi-Period Mean Reversion Ratio, $\lambda_s = 79$ bp, $t = 3.68^{**}$):**
   $$\text{Alpha}_{046} = \frac{\text{Mean}(\text{Close}, 3) + \text{Mean}(\text{Close}, 6) + \text{Mean}(\text{Close}, 12) + \text{Mean}(\text{Close}, 24)}{4 \times \text{Close}}$$
2. **Alpha 084 (20-Day Cumulative On-Balance Volume, $\lambda_s = 51$ bp, $t = 3.68^{**}$):**
   $$\text{Alpha}_{084} = \sum_{\tau=1}^{20} \left( \text{Close}_\tau > \text{Close}_{\tau-1} ? \text{Volume}_\tau : (\text{Close}_\tau < \text{Close}_{\tau-1} ? -\text{Volume}_\tau : 0) \right)$$
3. **Alpha 073 (Inverse Rank of Nested Decayed Price-Volume Correlations, $\lambda_s = 40$ bp, $t = 3.41^{**}$):**
   $$\text{Alpha}_{073} = -\left( \text{TSRank}(\text{DecayLinear}(\text{DecayLinear}(\text{Corr}(\text{Close}, \text{Volume}, 10), 16), 4), 5) - \text{Rank}(\text{DecayLinear}(\text{Corr}(\text{VWAP}, \text{Mean}(\text{Volume}, 30), 4), 3)) \right)$$
4. **Alpha 123 (Price-Volume vs. Low-Volume Correlation Rank, $\lambda_s = 42$ bp, $t = 3.39^{**}$):**
   $$\text{Alpha}_{123} = -\mathbb{I}\left( \text{Rank}\left(\text{Corr}\left(\sum_{t=1}^{20} \frac{\text{High}_t + \text{Low}_t}{2}, \sum_{t=1}^{20} \text{Mean}(\text{Volume}, 60)_t, 9\right)\right) < \text{Rank}(\text{Corr}(\text{Low}, \text{Volume}, 6)) \right)$$
5. **Alpha 049 (Downward Directional Pressure Ratio, $\lambda_s = 25$ bp, $t = 3.12^{**}$):**
   $$\text{Alpha}_{049} = \frac{\sum_{t=1}^{12} \text{DDP}_t}{\sum_{t=1}^{12} \text{DDP}_t + \sum_{t=1}^{12} \text{UDP}_t}$$
   where $\text{DDP}_t = (\text{High}_t + \text{Low}_t \ge \text{High}_{t-1} + \text{Low}_{t-1} ? 0 : \max(|\text{High}_t - \text{High}_{t-1}|, |\text{Low}_t - \text{Low}_{t-1}|))$, and $\text{UDP}_t = (\text{High}_t + \text{Low}_t \le \text{High}_{t-1} + \text{Low}_{t-1} ? 0 : \max(|\text{High}_t - \text{High}_{t-1}|, |\text{Low}_t - \text{Low}_{t-1}|))$.
6. **Alpha 071 (24-Day Percentage Deviation from Mean, $\lambda_s = 58$ bp, $t = 3.06^{**}$):**
   $$\text{Alpha}_{071} = \frac{\text{Close} - \text{Mean}(\text{Close}, 24)}{\text{Mean}(\text{Close}, 24)} \times 100$$
7. **Alpha 184 (Rank of Delayed Price-Gap Correlation, $\lambda_s = 41$ bp, $t = 2.86^{**}$):**
   $$\text{Alpha}_{184} = \text{Rank}(\text{Corr}(\text{Delay}(\text{Open} - \text{Close}, 1), \text{Close}, 200)) + \text{Rank}(\text{Open} - \text{Close})$$
8. **Alpha 155 (Volume MACD Histogram, $\lambda_s = 40$ bp, $t = 2.82^{**}$):**
   $$\text{Alpha}_{155} = \text{SMA}(\text{Volume}, 13, 2) - \text{SMA}(\text{Volume}, 27, 2) - \text{SMA}(\text{SMA}(\text{Volume}, 13, 2) - \text{SMA}(\text{Volume}, 27, 2), 10, 2)$$
9. **Alpha 054 (Inverse Rank of Intraday Volatility and Correlation, $\lambda_s = 44$ bp, $t = 2.67^{**}$):**
   $$\text{Alpha}_{054} = -\text{Rank}\left( \text{Std}(|\text{Close} - \text{Open}|) + (\text{Close} - \text{Open}) + \text{Corr}(\text{Close}, \text{Open}, 10) \right)$$
10. **Alpha 181 (Benchmark-Relative Excess Return Skewness, $\lambda_s = 38$ bp, $t = 2.57^{**}$):**
    $$\text{Alpha}_{181} = \frac{\sum_{t=1}^{20} \left( (R_t - \bar{R}_{20}) - (R_{m,t} - \bar{R}_{m,20})^2 \right)}{\sum_{t=1}^{20} (R_{m,t} - \bar{R}_{m,20})^3}$$
11. **Alpha 161 (12-Day Average True Range, $\lambda_s = 34$ bp, $t = 2.57^{*}$):**
    $$\text{Alpha}_{161} = \text{Mean}(\text{TR}, 12), \quad \text{TR} = \max(\text{High} - \text{Low}, |\text{Delay}(\text{Close}, 1) - \text{High}|, |\text{Delay}(\text{Close}, 1) - \text{Low}|)$$
12. **Alpha 190 (Log Gain-to-Loss Variability Ratio, $\lambda_s = 36$ bp, $t = 2.49^{*}$):**
    Log-ratio comparing the count and sum of squared return deviations above the 20-day compounding benchmark to those below it.
13. **Alpha 039 (Rank of Decay-Adjusted Momentum-VWAP Divergence, $\lambda_s = 39$ bp, $t = 2.49^{*}$):**
    $$-\left( \text{Rank}(\text{DecayLinear}(\text{Delta}(\text{Close}, 2), 8)) - \text{Rank}\left(\text{DecayLinear}\left(\text{Corr}\left(0.3 \times \text{VWAP} + 0.7 \times \text{Open}, \sum_{t=1}^{37} \text{Mean}(\text{Volume}, 180), 14\right), 12\right)\right) \right)$$
14. **Alpha 015 (Overnight Gap Return, $\lambda_s = 41$ bp, $t = 2.46^{*}$):**
    $$\text{Alpha}_{015} = \frac{\text{Open}}{\text{Delay}(\text{Close}, 1)} - 1$$
15. **Alpha 063 (6-Day Relative Strength Index, $\lambda_s = 45$ bp, $t = 2.38^{*}$):**
    $$\text{Alpha}_{063} = \frac{\text{SMA}(\max(\text{Close} - \text{Delay}(\text{Close}, 1), 0), 6, 1)}{\text{SMA}(|\text{Close} - \text{Delay}(\text{Close}, 1)|, 6, 1)} \times 100$$
16. **Alpha 001 (6-Day Negative Correlation of Volume Growth and Return, $\lambda_s = 37$ bp, $t = 2.31^{*}$):**
    $$\text{Alpha}_{001} = -\text{Corr}\left( \text{Rank}(\text{Delta}(\log(\text{Volume}), 1)), \text{Rank}\left(\frac{\text{Close} - \text{Open}}{\text{Open}}\right), 6 \right)$$
17. **Alpha 086 (10-Day Price Acceleration vs. Directional Change, $\lambda_s = 32$ bp, $t = 2.30^{*}$):**
    Conditional piecewise function tracking the second-difference of closing prices over 10-day vs 20-day windows.

## Required data

- **Universe:** S&P 500 constituents (CRSP common stocks, share codes 10/11) from 2002-01-01 to 2022-12-31.
- **Vendors:** CRSP (daily stock prices, shares outstanding, returns) and OptionMetrics IvyDB (implied volatility and VWAP).
- **Timeframe:** Daily OHLCV bars and intraday Volume-Weighted Average Price (VWAP).
- **Volume & Price Fields:** Open, High, Low, Close, Volume, VWAP.
- **Control Factor Panel:** 151 fundamental firm characteristics from the Jensen, Kelly, and Pedersen (2023) equity factor zoo covering 4,135,225 firm-months.
- **Missing Data Rules:** Stocks require at least 252 continuous trading days in rolling estimation windows; stocks priced below $5 are dropped to prevent penny-stock microstructure distortion.

## Execution assumptions

- **Rebalancing Cadence:** Monthly rebalancing at calendar month close.
- **Portfolio Weighting:** Value-weighted decile portfolios using lagged market capitalization.
- **Signal Aggregation:** Scaled mean daily return ($21 \times \bar{r}_d$) across the monthly holding horizon.
- **Transaction Costs & Capacity:** Empirical tests report cross-sectional asset pricing risk premiums gross of trading frictions; capacity feasibility is established by restricting the testing ground to S&P 500 large-cap equities (the world's most liquid equity capital pool).

## Evidence

### Source-reported

All figures, risk premiums, $t$-statistics, and comparison metrics below trace directly to Du, Walter, and Ulrich (*arXiv:2601.06499v2*, Sections 2 & 3, Tables 1, 2, and 3, and Appendix Table 4):

#### 1. Primary Empirical Results: $3 \times 2$ DS vs. SS LASSO (Table 1)
Evaluated across $N = 1,926$ test assets (1,008 Alpha + 918 Jensen portfolios) over 2002–2022:
- **Multi-Period Mean Reversion Ratio (046):** DS $\lambda_s = 79$ bp ($t = 3.68^{**}$) vs. SS $\lambda_s = -19$ bp ($t = -0.12$, sign flip).
- **20-Day Cumulative OBV (084):** DS $\lambda_s = 51$ bp ($t = 3.68^{**}$) vs. SS $\lambda_s = -1,052$ bp ($t = -3.14^{**}$, sign flip).
- **Nested Decayed Price-Volume Corr (073):** DS $\lambda_s = 40$ bp ($t = 3.41^{**}$) vs. SS $\lambda_s = -50$ bp ($t = -1.02$).
- **Price-Volume vs. Low-Volume Rank (123):** DS $\lambda_s = 42$ bp ($t = 3.39^{**}$) vs. SS $\lambda_s = 217$ bp ($t = 3.66^{**}$).
- **Downward Directional Pressure Ratio (049):** DS $\lambda_s = 25$ bp ($t = 3.12^{**}$) vs. SS $\lambda_s = -90$ bp ($t = -2.42^{*}$, sign flip).
- **24-Day Deviation from Mean (071):** DS $\lambda_s = 58$ bp ($t = 3.06^{**}$) vs. SS $\lambda_s = -300$ bp ($t = -1.36$).
- **Rank of Delayed Price-Gap Corr (184):** DS $\lambda_s = 41$ bp ($t = 2.86^{**}$) vs. SS $\lambda_s = 18$ bp ($t = 0.22$).
- **Volume MACD Histogram (155):** DS $\lambda_s = 40$ bp ($t = 2.82^{**}$) vs. SS $\lambda_s = -150$ bp ($t = -3.38^{**}$, sign flip).
- **Inverse Rank Intraday Vol & Corr (054):** DS $\lambda_s = 44$ bp ($t = 2.67^{**}$) vs. SS $\lambda_s = 800$ bp ($t = 2.99^{**}$).
- **Benchmark-Relative Excess Skewness (181):** DS $\lambda_s = 38$ bp ($t = 2.57^{**}$) vs. SS $\lambda_s = 243$ bp ($t = 4.51^{**}$).
- **12-Day Average True Range (161):** DS $\lambda_s = 34$ bp ($t = 2.57^{*}$) vs. SS $\lambda_s = 4,286$ bp ($t = 3.89^{**}$).
- **Log Gain-to-Loss Variability Ratio (190):** DS $\lambda_s = 36$ bp ($t = 2.49^{*}$) vs. SS $\lambda_s = -593$ bp ($t = -3.64^{**}$, sign flip).
- **Rank Decay Momentum-VWAP Divergence (039):** DS $\lambda_s = 39$ bp ($t = 2.49^{*}$) vs. SS $\lambda_s = 478$ bp ($t = 3.38^{**}$).
- **Overnight Gap Return (015):** DS $\lambda_s = 41$ bp ($t = 2.46^{*}$) vs. SS $\lambda_s = -270$ bp ($t = -0.75$).
- **6-Day Relative Strength Index (063):** DS $\lambda_s = 45$ bp ($t = 2.38^{*}$) vs. SS $\lambda_s = -212$ bp ($t = -2.07^{*}$, sign flip).
- **6-Day Negative Corr Vol Growth & Return (001):** DS $\lambda_s = 37$ bp ($t = 2.31^{*}$) vs. SS $\lambda_s = 558$ bp ($t = 4.69^{**}$).
- **10-Day Price Acceleration vs. Direction (086):** DS $\lambda_s = 32$ bp ($t = 2.30^{*}$) vs. SS $\lambda_s = 158$ bp ($t = 3.11^{**}$).

#### 2. Portfolio Granularity Ablation: $5 \times 5$ vs. $3 \times 2$ (Table 2)
Evaluated across $N = 8,025$ test assets (4,200 Alpha + 3,825 Jensen portfolios):
- Partitioning into $5 \times 5$ sorts isolates extreme tail deviations, expanding the certified factor pool from 17 to 30 significant factors ($p < 0.05$).
- Prominent tail-sensitivity factors include:
  - Alpha 184 (Delayed Price-Gap Corr): $\lambda_s = 40$ bp ($t = 6.78^{**}$ vs $3 \times 2$ $t = 2.86^{**}$).
  - Alpha 141 (Inverse High-Volume Corr): $\lambda_s = 25$ bp ($t = 5.54^{**}$ vs $3 \times 2$ $t = 1.69$, emerging from insignificance).
  - Alpha 123 (Price-Volume vs Low-Volume Rank): $\lambda_s = 26$ bp ($t = 5.43^{**}$ vs $3 \times 2$ $t = 3.39^{**}$).
  - Alpha 015 (Overnight Gap Return): $\lambda_s = 31$ bp ($t = 5.17^{**}$ vs $3 \times 2$ $t = 2.46^{*}$).
  - Alpha 099 (Close-Volume Covariance Rank): $\lambda_s = 22$ bp ($t = 5.04^{**}$ vs $3 \times 2$ $t = 1.96$).
  - Alpha 046 (Multi-Period Mean Reversion): $\lambda_s = 33$ bp ($t = 4.33^{**}$).
  - Alpha 073 (Nested Decayed PV Corr): $\lambda_s = 21$ bp ($t = 4.29^{**}$).

#### 3. Alternative Estimator Benchmarks (Table 3: DS-LASSO vs. Elastic Net vs. PCA)
- **Multi-Period Mean Reversion (046):** DS $\lambda_s = 79$ bp ($t = 3.68^{**}$), ENet $\lambda_s = 678$ bp ($t = 4.34^{**}$), PCA $\lambda_s = 171$ bp ($t = 5.29^{**}$).
- **24-Day Deviation from Mean (071):** DS $\lambda_s = 58$ bp ($t = 3.06^{**}$), ENet $\lambda_s = 685$ bp ($t = 4.00^{**}$), PCA $\lambda_s = 109$ bp ($t = 2.76^{**}$).
- **Delayed Price-Gap Corr (184):** DS $\lambda_s = 41$ bp ($t = 2.86^{**}$), ENet $\lambda_s = 197$ bp ($t = 3.46^{**}$), PCA $\lambda_s = 72$ bp ($t = 5.06^{**}$).
- **Benchmark-Relative Skewness (181):** DS $\lambda_s = 38$ bp ($t = 2.57^{**}$), ENet $\lambda_s = -67$ bp ($t = -1.38$), PCA $\lambda_s = 59$ bp ($t = 4.94^{**}$).
- Core factors remain robust and statistically significant across shrinkage, dimension-reduction, and sequential selection paradigms.

#### 4. Signal Persistence across Return Horizons (Appendix Table 4)
- Out of 168 tested signals, **110 exhibit strict monotonicity** in their Newey-West adjusted $t$-statistics from 1-day to 21-day holding horizons.
- **130 factors** display a Spearman rank correlation above $0.50$ across horizons, confirming that information aggregates rather than dissipates over monthly horizons.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Single-Selection LASSO Breakdown:** 14 of the 17 surviving Alpha191 factors experience severe coefficient instability, sign flips, or collapse of statistical significance under standard single-stage LASSO (SS), demonstrating that naive penalized regression without confounder control generates false negatives and unstable factor loadings.
- **Discontinuous / Unstable Factors:** 23 of the original 191 factors had to be dropped entirely due to numerical singularities, excessive missing values, or unstable time series in rolling windows.
- **Signal Dilution under Coarse Partitioning:** $3 \times 2$ sorting dilutes tail-sensitive alphas through central-tendency averaging; 13 factors (including Alpha 141 and Alpha 099) only achieve significance when partitioned into $5 \times 5$ quintiles.
- **Frictionless Reporting:** All risk premiums are estimated gross of transaction costs, slippage, and short-borrow fees. In high-turnover implementations, turnover drag could substantially erode reported premiums unless rebalanced at lower monthly frequencies.

## Falsification plan

To falsify the Cross-Market Alpha191 Double-Selection hypothesis:

1. **Walk-Forward Out-of-Sample Validation (2023–2026):**
   - *Protocol:* Re-estimate the Stage-1 and Stage-2 DS-LASSO models using the pre-2023 historical data, then evaluate the 17 certified alpha signals strictly out-of-sample on the post-2022 panel (2023-01-01 to 2026-08-31).
   - *Falsification threshold:* If fewer than 5 of the 17 certified alphas retain positive cross-sectional risk premiums ($\lambda_s > 0$) with $t > 1.65$ ($p < 0.10$), the reported predictability is falsified as sample-specific overfitting or regime-dependent artifact.
2. **Transaction Cost & Market Impact Drag Stress Test:**
   - *Protocol:* Backtest an actionable multi-factor long-short composite of the top 5 DS-certified alphas (046, 084, 073, 123, 071) applying realistic institutional execution costs: 5 bps one-way transaction cost for liquid large caps, plus size-dependent square-root market impact and borrow fees.
   - *Falsification threshold:* If the net-of-cost annualized Sharpe ratio drops below $SR < 0.50$ or maximum drawdown exceeds $25\%$, the strategy fails the economic exploitability test.
3. **Daily Rebalancing vs. Monthly Aggregation Parity Test:**
   - *Protocol:* Execute the decile portfolio sort on a daily rebalance schedule (next-day open execution) versus the paper's scaled monthly rebalance schedule.
   - *Falsification threshold:* If daily turnover costs erase more than 100% of the annualized alpha compared to the monthly rebalanced variant, the claim of monthly information horizon efficiency is falsified.
4. **Placebo / Scrambled Price-Volume Correlation Test:**
   - *Protocol:* Randomly permute the daily volume vectors across stocks while preserving price series, and recompute the volume-dependent alphas (084, 073, 123, 155).
   - *Falsification threshold:* If the synthetic scrambled volume signals produce comparable cross-sectional $t$-statistics to the true signals, the volume-conviction mechanism is an artifact of price trend correlation rather than genuine volume information.

## Crypto portability

**Portability Classification: Adapted / Unproven.**

The empirical findings of Du, Walter, and Ulrich were established on U.S. large-cap equities (S&P 500, 2002–2022). Porting this framework to cryptocurrency markets involves key structural adaptations:

1. **Native Trade Aggressor Flags (No Heuristic Volume Signs):** In equities, on-balance volume (Alpha 084) and volume-return correlations (Alpha 001) rely on daily sign heuristics ($\text{Close} > \text{Delay}(\text{Close}, 1)$). In crypto centralized exchanges (Binance, Bybit, OKX), trade feeds provide explicit taker side flags (`is_buyer_maker`). This allows direct, high-fidelity measurement of net aggressor volume flow without sign approximation errors.
2. **Perpetual Funding Rate Confounding:** Crypto perpetual futures incur funding fee cash flows every 1 to 8 hours. Holding long positions in short-term mean-reversion alphas (Alpha 046, Alpha 071) when funding rates are heavily positive introduces an unmodeled cash drag. Effective alpha signals in crypto perpetuals must be residualized against prevailing funding rate carry.
3. **24/7 Continuous Trading & Absence of Overnight Gaps:** Alpha 015 (Overnight Gap Return: $\text{Open} / \text{Delay}(\text{Close}, 1) - 1$) and Alpha 184 rely on equity session open/close boundaries. In crypto's 24/7 continuous market, "gaps" must be redefined around discrete UTC liquidity resets (e.g. 00:00 UTC or 08:00 UTC funding timestamps).
4. **Heavy-Tailed Volatility & Tail Dispersions:** Cryptocurrency cross-sectional returns exhibit extreme kurtosis and frequent crash cascades. The paper's finding that $5 \times 5$ fine sorting captures "tail-sensitivity" factors (such as Alpha 184 and Alpha 141) indicates that tail-sensitive signals may be exceptionally potent in crypto, but require strict volatility parity sizing and stop-loss gating to prevent catastrophic liquidation.

## Limitations

- **S&P 500 Large-Cap Specificity:** Empirical testing is confined to the liquid constituents of the S&P 500; while intentional to demonstrate institutional capacity, behavioral alpha premiums in small-cap equities or crypto remain unproven.
- **Gross-of-Cost Evaluation:** Factor risk premiums are estimated from cross-sectional regressions on portfolio covariances without explicit transaction cost, spread, or borrow fee subtractions.
- **Monthly Return Aggregation:** Aggregating daily high-frequency signals via scaled 21-day mean returns smooths intraday microstructural dynamics, potentially dampening fast-decaying signals.
- **Linear Factor Framework:** The DS-LASSO model assumes linear factor-return relationships; non-linear interactions between fundamental controls and fast alphas require further machine learning exploration.

## Implementation status

- `implementation_status: not-implemented`
- This record captures upstream academic research only.
- No implementation has been created in PyBroker, NautilusTrader, paper trading, testnet, or live trading workflows.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Research capture does not authorize strategy implementation, backtesting promotion, paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- `[[quant/equity-order-flow-kyle-lambda-cross-sectional-liquidity-premium-2026-09-03]]` — Cross-sectional Kyle's lambda price impact and signed order flow return predictability on CRSP equities (Aldridge, 2026).
- `[[quant/equity-cross-regime-bayesian-optimisation-xgboost-tabnet-hybrid-2026-09-02]]` — Cross-regime Bayesian optimization of tree and deep learning tabular models on US equities (Le Grice, 2026).
- `[[quant/cross-sectional-crypto-momentum-2026-08-31]]` — Cross-sectional momentum and reversal dynamics in digital asset markets.
- `[[quant/crypto-cross-sectional-amihud-illiquidity-premium-2026-08-31]]` — Microstructure liquidity premiums and adverse selection across crypto tokens.
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Combinatorial purged cross-validation and leakage prevention in high-dimensional strategy evaluation.

## Sources

- **Primary paper:** Jin Du, Alexander Walter, and Maxim Ulrich, *Cross-Market Alpha: Testing Short-Term Trading Factors in the U.S. Market via Double-Selection LASSO*, arXiv preprint `arXiv:2601.06499v2 [q-fin.ST]`, submitted January 10, 2026, revised May 21, 2026. DOI: `10.48550/arXiv.2601.06499`.
  - Abstract & metadata: https://arxiv.org/abs/2601.06499
  - Full-text HTML5: https://arxiv.org/html/2601.06499v2
  - PDF version: https://arxiv.org/pdf/2601.06499
  - Primary TeX source bundle: https://arxiv.org/src/2601.06499
- **Foundational literature cited within primary source:**
  - A. Belloni, V. Chernozhukov, and C. Hansen (2014), *Inference on treatment effects after selection among high-dimensional controls*, The Review of Economic Studies 81(2), 608–650. DOI: `10.1093/restud/rdt044`.
  - G. Feng, S. Giglio, and D. Xiu (2020), *Taming the factor zoo: A test of new factors*, The Journal of Finance 75(3), 1327–1370. DOI: `10.1111/jofi.12883`.
  - T. I. Jensen, B. T. Kelly, and L. H. Pedersen (2023), *Is there a replication crisis in finance?*, The Journal of Finance 78(5), 2465–2518. DOI: `10.1111/jofi.13249`.
  - Guotai Junan Securities (2017), *The Alpha191 Factor Library: Technical Analysis Signals and Formula Specifications*, Quantitative Research Report, Guotai Junan Securities Co., Ltd.
  - L. Blume, D. Easley, and M. O'Hara (1994), *Market statistics and technical analysis: the role of volume*, The Journal of Finance 49(1), 153–181. DOI: `10.1111/j.1540-6261.1994.tb04424.x`.
  - A. S. Kyle (1985), *Continuous auctions and insider trading*, Econometrica 53(6), 1315–1335. DOI: `10.2307/1913210`.
  - J. B. De Long, A. Shleifer, L. H. Summers, and R. J. Waldmann (1990), *Noise trader risk in financial markets*, Journal of Political Economy 98(4), 703–738. DOI: `10.1086/261703`.
  - A. Shleifer and R. W. Vishny (1997), *The limits of arbitrage*, The Journal of Finance 52(1), 35–55. DOI: `10.1111/j.1540-6261.1997.tb03807.x`.
  - E. F. Fama and K. R. French (1993), *Common risk factors in the returns on stocks and bonds*, Journal of Financial Economics 33(1), 3–56. DOI: `10.1016/0304-405X(93)90023-5`.
  - E. F. Fama and K. R. French (2015), *A five-factor asset pricing model*, Journal of Financial Economics 116(1), 1–22. DOI: `10.1016/j.jfineco.2014.10.010`.
  - C. R. Harvey, Y. Liu, and H. Zhu (2016), *... and the cross-section of expected stock returns*, The Review of Financial Studies 29(1), 5–68. DOI: `10.1093/rfs/hhv059`.
  - R. D. McLean and J. Pontiff (2016), *Does academic research destroy stock return predictability?*, The Journal of Finance 71(1), 5–32. DOI: `10.1111/jofi.12365`.
