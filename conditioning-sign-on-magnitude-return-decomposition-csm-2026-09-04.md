---
schema: strategy-research-record-v1
title: "Conditioning Sign on Magnitude: Non-Copula Return Decomposition for Market Timing"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - return-decomposition
  - market-timing
  - volatility-dynamics
  - sign-predictability
  - multiplicative-error-model
  - probit-regression
  - equity-index
status: research-only
confidence: medium
source_as_of: "2026-06-02"
sources:
  - "Arsène Brou and Richard Luger, 'A new decomposition approach to modeling financial returns: Conditioning sign on magnitude', arXiv:2606.04153v1 [q-fin.ST], June 2, 2026. Accepted for publication in Journal of Banking and Finance. DOI: https://doi.org/10.1016/j.jbankfin.2026.107716. https://arxiv.org/abs/2606.04153"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Conditioning Sign on Magnitude: Non-Copula Return Decomposition for Market Timing

## Provenance

- **Primary Source:** Arsène Brou and Richard Luger (Department of Finance, Insurance and Real Estate, Université Laval, Quebec City, Canada), *"A new decomposition approach to modeling financial returns: Conditioning sign on magnitude"*, arXiv preprint `arXiv:2606.04153v1 [q-fin.ST]`, submitted June 2, 2026.
- **Journal Acceptance:** Author accepted manuscript, accepted for publication in the *Journal of Banking and Finance* (DOI: [10.1016/j.jbankfin.2026.107716](https://doi.org/10.1016/j.jbankfin.2026.107716)).
- **Stable URLs:**
  - Abstract: [https://arxiv.org/abs/2606.04153](https://arxiv.org/abs/2606.04153)
  - Full text HTML: [https://arxiv.org/html/2606.04153v1](https://arxiv.org/html/2606.04153v1)
  - PDF: [https://arxiv.org/pdf/2606.04153v1](https://arxiv.org/pdf/2606.04153v1)
- **Source Data Period:** Monthly data from January 1948 to December 2021 (887 monthly observations). In-sample model estimation and subset selection use the first 400 monthly observations (February 1948 to May 1981); out-of-sample evaluation uses the remaining 487 monthly observations (June 1981 to December 2021) in a rolling-window scheme ($L=400$).
- **Predictor Set:** Eight macro/financial variables derived from the Welch and Goyal (2008) dataset updated through 2021: dividend-price ratio (`dp`), default yield spread (`dfy`), term spread (`tms`), short-term 3-month Treasury bill rate (`tbl`), long-term government bond return (`ltr`), default return spread (`dfr`), net equity expansion (`ntis`), and inflation (`infl`). Two collinear variables (`ep` and `btm`) were excluded due to correlation $> 0.80$.
- **Pre-Write Deduplication Audit:** A comprehensive repository-wide grep for `arXiv:2606.04153`, `Brou`, `Luger`, `Conditioning sign on magnitude`, and `CSM` confirmed zero matching records in the repository. Existing return-prediction and portfolio-allocation records examine multi-model adaptive shrinkage (`two-stage-adaptive-shrinkage-golden-criterion-equity-premium-2026-09-02.md`) and macro style rotation (`continuous-macro-timing-growth-defensive-style-allocation-2026-09-02.md`), but none employ non-copula sign-magnitude return decomposition with probit conditioning on contemporaneous Weibull-MEM magnitude.

## Economic mechanism

### Source-reported

Conventional linear predictive regressions (OLS) model the conditional mean of asset returns directly as a linear function of lagged macro variables. However, out-of-sample empirical evidence consistently shows that linear regressions struggle to outperform a simple historical average benchmark (Welch and Goyal, 2008; Campbell and Thompson, 2008). 

Brou and Luger (2026) build upon the mathematical identity that any raw return $R_t$ can be decomposed without loss of information into the product of its direction and magnitude:
$$R_t = \text{sign}(R_t) \cdot |R_t| = (2 S_t - 1) M_t$$
where $S_t = \mathbf{1}\{R_t > 0\} \in \{0, 1\}$ is a binary directional indicator and $M_t = |R_t| \ge 0$ is the return magnitude (closely tied to volatility). 

Prior decomposition frameworks, such as Anatolyev and Gospodinov (2010, AG), model the marginal distribution of $M_t$ and the marginal distribution of $S_t$ separately, and then link them via a bivariate parametric copula (e.g., Gaussian, Clayton, Frank, or FGM copulas). Brou and Luger propose the **Conditioning Sign on Magnitude (CSM)** framework, which directly factorizes the joint conditional density as:
$$f_{M_t, S_t \mid \bm{X}_{t-1}}(m_t, s_t \mid \bm{x}_{t-1}) = f_{M_t \mid \bm{X}_{t-1}}(m_t \mid \bm{x}_{t-1}) \cdot f_{S_t \mid M_t, \bm{X}_{t-1}}(s_t \mid m_t, \bm{x}_{t-1})$$

The authors provide three economic and statistical justifications for conditioning sign on magnitude rather than the reverse:
1. **Volatility-Induced Sign Predictability:** Due to strong volatility clustering in financial markets, periods of large magnitude $M_t$ exhibit persistent volatility states. As demonstrated by Christoffersen and Diebold (2006), volatility dynamics induce predictable shifts in the conditional probability of observing positive versus negative returns, even when conditional mean predictability is weak.
2. **Behavioral Asymmetries and Feedback Trading:** Structural and behavioral market frictions (Treynor and Ferguson, 1985; Hong and Stein, 1999; Cespa and Vives, 2012) generate state-dependent responses to return magnitude. Large price moves trigger distinct behavioral reactions: extreme negative moves frequently induce liquidity withdrawal and panic selling, skewing the subsequent directional probability downward, whereas positive volatility shocks may prompt momentum chasing or profit taking.
3. **Statistical Conditioning Efficiency:** In econometric modeling, conditioning on a variable that accounts for greater explained variation improves model stability and estimation efficiency. Because return magnitude exhibits substantial persistence and explains large variation, modeling $S_t \mid M_t$ stabilizes directional probability estimates and avoids the parameter estimation overhead and misspecification risks of bivariate copula selection.

### Research interpretation

The hypothesized alpha mechanism is a **volatility-state-modulated directional timing signal**. Rather than forcing macro predictors to forecast dollar returns directly through a static linear hyperplane, the framework disentangles the macro drivers of volatility scale from the drivers of directional sign:
- Macro variables such as credit spreads (`dfy`, `dfr`) exhibit stronger unconditional correlation with return magnitude ($0.166$ and $-0.146$) than with raw returns, acting primarily as scale/risk indicators.
- Interest rate variables such as the short-term T-bill rate (`tbl`) exhibit stronger correlation with directional sign ($-0.143$) than with raw returns ($-0.097$), acting primarily as monetary/liquidity discount rate filters.
- By integrating the conditional sign probability across the full conditional distribution of return magnitude, the expected return forecast $\widehat{\mathbb{E}}(R_{t+1} \mid \bm{x}_t) = 2 \xi_{t+1}^* - \psi_{t+1}$ naturally forms a nonlinear filter: during high-volatility regimes, the directional hurdle is amplified or dampened depending on the estimated sign-magnitude interaction coefficient $\beta$, preventing whipsaws during volatile drawdowns.

## Signal

### Mathematical formulation

The trading signal relies on one-step-ahead conditional mean return forecasts $\hat{r}_{t+1} = \widehat{\mathbb{E}}(R_{t+1} \mid \bm{x}_t)$ generated by the CSM model:

1. **Magnitude Component ($M_t = |R_t|$):**
   Modeled via a Multiplicative Error Model (MEM; Engle, 2002):
   $$M_t = \psi_t \eta_t, \quad \eta_t \sim \text{Weibull}(\kappa, 1), \quad \mathbb{E}(\eta_t \mid \bm{x}_{t-1}) = 1$$
   $$\psi_t = \mathbb{E}(M_t \mid \bm{x}_{t-1}) = \exp(w_v + \bm{\delta}_v' \bm{x}_{t-1})$$
   The conditional CDF is:
   $$F_{M_t \mid \bm{X}_{t-1}}(m \mid \bm{x}_{t-1}) = 1 - \exp\left( - \left[ \frac{m}{\psi_t} \Gamma(1 + \kappa^{-1}) \right]^\kappa \right)$$
   and the conditional quantile function is:
   $$q_t(\upsilon) = F_{M_t \mid \bm{X}_{t-1}}^{-1}(\upsilon \mid \bm{x}_{t-1}) = \psi_t \Gamma(1 + \kappa^{-1})^{-1} (-\log(1 - \upsilon))^{1/\kappa}$$

2. **Sign Component ($S_t = \mathbf{1}\{R_t > 0\}$):**
   Modeled via a probit specification conditioning on both $\bm{x}_{t-1}$ and contemporaneous magnitude $m_t$:
   $$S_t \mid (M_t = m_t, \bm{x}_{t-1}) \sim \text{Bernoulli}(p_t^*), \quad p_t^* = \Phi(\theta_t^*)$$
   - **CSM (Baseline):**
     $$\theta_t^* = w_d + \bm{\delta}_d' \bm{x}_{t-1} + \beta m_t$$
   - **CSM (Poly):**
     $$\theta_t^* = w_d + \bm{\delta}_d' \bm{x}_{t-1} + \beta_1 m_t + \beta_2 m_t^2 + \beta_3 m_t^3$$

3. **Expected Return Integration:**
   Using the decomposition identity $R_t = 2 M_t S_t - M_t$:
   $$\mathbb{E}(R_t \mid \bm{x}_{t-1}) = 2 \xi_t^* - \psi_t$$
   where the cross-product expectation $\xi_t^* = \mathbb{E}(M_t S_t \mid \bm{x}_{t-1})$ is evaluated by 1-D numerical integration over the probability integral transform $\upsilon \in [0, 1]$:
   $$\xi_t^* = \int_0^1 q_t(\upsilon) \Phi(\theta_t^*(q_t(\upsilon))) \, d\upsilon$$

### Formation timestamp
- **Observation timestamp:** End of each calendar month (monthly close, Eastern Time / UTC); source-reported.
- **Signal formation:** Evaluated at month-end using data available up to $t$; source-reported.
- **Tradability:** Position adjustment executed at the start of month $t+1$; source-reported. Exact intra-day fill protocol (e.g., market-on-open at first trading day of the month) is not specified by the source and is `research-proposed`.

### Lookback and Estimation Windows
- **Estimation window ($L$):** Fixed rolling window of 400 monthly observations ($L=400$), re-estimated at each monthly step; source-reported.
- **Initial in-sample calibration:** First 400 months (February 1948 to May 1981); source-reported.
- **Out-of-sample evaluation:** 487 consecutive months (June 1981 to December 2021); source-reported.
- **Predictor subset selection:** Selected once in-sample over the first 400 observations by evaluating all $\binom{8}{k}$ predictor combinations for $k \in \{1, \dots, 8\}$ using the Area Under the (Classification) Curve (AUC; Jordà and Taylor, 2011) criterion; source-reported.
- Selected subsets under AUC criterion:
  - $k=1$: `tbl` (selected by all models); source-reported.
  - $k=2$: `tbl`, `dfr`; source-reported.
  - $k=3$: `tbl`, `dfy`, `dfr`; source-reported.
  - $k=7$: `dp`, `dfy`, `tms`, `tbl`, `ltr`, `dfr`, `infl`; source-reported.
  - $k=8$: all 8 predictors by construction; source-reported.

### Entry and Exit Rules
- **Long Equity Signal:** If predicted excess return $\hat{r}_{t+1} = 2 \xi_{t+1}^* - \psi_{t+1} > 0$, allocate 100% of portfolio equity to the equity index (S&P 500); source-reported.
- **Defensive Cash Signal:** If predicted excess return $\hat{r}_{t+1} \le 0$, switch 100% of portfolio equity to the risk-free asset (3-month Treasury bill rate); source-reported.
- **Rebalance Cadence:** Monthly, evaluated at each month boundary; source-reported.
- **Position Re-entry / Turnover:** When the signal maintains the same regime (positive to positive, or non-positive to non-positive), no portfolio rebalancing occurs and zero transaction costs are incurred; source-reported.

### Parameters
| Parameter | Value | Source Label |
| :--- | :--- | :--- |
| Rolling estimation window $L$ | 400 months | Source-reported |
| Out-of-sample window | 487 months (1981-06 to 2021-12) | Source-reported |
| Number of candidate predictors | 8 macro/financial variables | Source-reported |
| Subset selection criterion | AUC on 1-step-ahead in-sample forecasts | Source-reported |
| Transaction cost $c$ | 10 basis points (0.10%) per allocation switch | Source-reported |
| Probit link function | Standard Normal CDF $\Phi(\cdot)$ | Source-reported |
| Magnitude error distribution | Weibull($\kappa$, 1) with unit mean normalization | Source-reported |
| Polynomial degrees (Poly variant) | Cubic: $m_t, m_t^2, m_t^3$ | Source-reported |
| Monte Carlo integration points | Standard quasi-Monte Carlo / numerical quadrature | `research-proposed` |
| Intraday execution timing | Market-on-Open on Day 1 of month | `research-proposed` |
| Risk-free rate cash proxy | 3-month U.S. Treasury bill | Source-reported |

## Required data

- **Instrument / Asset:** S&P 500 value-weighted index (including dividends); source-reported.
- **Cash / Risk-free proxy:** U.S. 3-month Treasury bill rate (secondary market); source-reported.
- **Predictor Variables:** 8 macroeconomic and financial time series from Welch and Goyal (2008) / Amit Goyal repository:
  1. `dp`: Dividend-price ratio (difference between log of 12-month moving sum of dividends and log of stock prices); source-reported.
  2. `dfy`: Default yield spread (difference between BAA and AAA corporate bond yields); source-reported.
  3. `tms`: Term spread (difference between long-term government bond yield and 3-month T-bill rate); source-reported.
  4. `tbl`: Short-term interest rate (3-month Treasury bill yield); source-reported.
  5. `ltr`: Long-term government bond return; source-reported.
  6. `dfr`: Default return spread (long-term corporate bond return minus long-term government bond return); source-reported.
  7. `ntis`: Net equity expansion (ratio of 12-month net equity issues by NYSE-listed stocks to total end-of-year market cap); source-reported.
  8. `infl`: Consumer Price Index (CPI) inflation rate; source-reported.
- **Timeframe:** Monthly frequency; source-reported.
- **Point-in-Time Availability:** All predictors are lagged by one month ($t-1$) to align with return at month $t$; source-reported. Note: macro series such as CPI (`infl`) may involve publication lags in live trading; source uses standard Goyal-Welch end-of-month release alignment without real-time vintage revision adjustments (`data gap`).
- **Missing Data Handling:** None reported in full historical series (1948–2021). Missing prints or imputation not permitted without explicit declaration.

## Execution assumptions

- **Order Type:** Monthly portfolio rebalancing; source implies rebalancing at monthly close/open. Modeled as immediate fill at published closing index levels without market impact; source-reported.
- **Transaction Costs:** Flat 10 bps (0.10%) deducted from total portfolio wealth whenever an allocation switch occurs between equity and cash ($W_{t+1} = W_t (1 + r_{p,t+1})(1 - c)$); source-reported.
- **Slippage & Spread:** Not modeled by the source beyond the 10 bps flat cost. For large-cap ETF/futures implementation, 10 bps exceeds typical SPY/ES bid-ask spread and commission; source-reported.
- **Leverage / Borrow:** Long-only; zero short positions, zero leverage ($w_t \in \{0, 1\}$); source-reported.
- **Execution Fill Model:** Next-month opening fill assumed; labeled `research-proposed`.
- **Capacity:** Constrained only by S&P 500 index liquidity (hundreds of billions of dollars); source-reported.

## Evidence

### Source-reported

All quantitative figures below are directly reported by Brou and Luger (arXiv:2606.04153v1, Sections 3.1–3.2, Tables 3, 6, 7, 8, and Supplementary Tables B1, B2, B3) over the 487-month out-of-sample period (May/June 1981 to December 2021) with an initial $1 investment:

#### 1. Baseline Benchmark Performance (May 1981 – December 2021)
- **Buy-and-Hold S&P 500:** Terminal Wealth (TW) = $104.63; Annualized Return (AV) = 12.65%; Annualized Volatility (SD) = 15.00%; Sharpe Ratio (SR) = 0.17; Maximum Drawdown (MDD) = not reported in main text summary table.
- **Historical Average (HA):** Identical to Buy-and-Hold because all rolling HA forecasts were positive ($\hat{r}_{t+1} > 0$).
- **12-Month Momentum Switching:** TW = $100.21; SR = 0.20.
- **3-Month & 6-Month Momentum Switching:** Substantially underperformed; TW $< \$50.00$.

#### 2. Strategy Performance across Predictor Dimensions ($k$)
- **At $k=3$ Predictors (`tbl`, `dfy`, `dfr`):**
  - **CSM (Baseline & Poly coincide):** TW = **$181.68** (highest terminal wealth across all tested strategies and models); SR = **0.21** (statistically significant improvement over Buy-and-Hold at the 5% level, Ledoit-Wolf HAC_PW test); annualized CER Gain = **1.878%** (Mean-Variance, $\gamma=5$) and **1.939%** (CRRA, $\gamma=5$).
  - **Copula-based models (Gaussian / Frank / FGM):** TW = $165.23; SR statistically significant at 10% level.
  - **Linear OLS Predictive Regression:** TW = $112.79; SR not statistically significant.
  - **Complete Subset Regression (CSR):** TW = $98.22 (underperforms Buy-and-Hold).
  - **GARCH-in-mean (GARCH-M):** TW = $147.63.
  - **Two-state Markov-Switching (MS):** TW = **$25.65** (severe breakdown due to regime forecasting instability).

- **At $k=2$ Predictors (`tbl`, `dfr`):**
  - **CSM (Baseline):** CER Gain = **1.122%** (Mean-Variance) and **1.108%** (CRRA); statistically significant SR improvement at 10% level.
  - **CSR:** CER Gain = 0.596% (Mean-Variance) and 0.303% (CRRA).
  - **GARCH-M:** TW = $151.01; CER Gain = 1.075% (Mean-Variance) and 1.062% (CRRA).

- **At Intermediate Dimensions ($k=4, 5, 6$):**
  - Linear OLS collapses: TW drops to $71.58 ($k=4$), $62.31 ($k=5$), and $65.92 ($k=6$).
  - CSR partially stabilizes: TW reaches $126.80 at $k=5$.
  - **CSM (Poly variant):** Outperforms Linear and CSR at all intermediate dimensions: TW = **$139.78** ($k=4$), **$148.04** ($k=5$), and **$137.85** ($k=6$); provides significant CER gains over CSM (Baseline) at $k=4$ and $k=6$.

- **At $k=7$ Predictors:**
  - **CSM (Baseline):** TW = $168.05; SR = 0.22; CER Gain = **2.302%** (Mean-Variance) and **2.612%** (CRRA).
  - **Copula-based (Gaussian / Clayton):** TW = $176.00–$178.00; SR = 0.22 (significant at 10% level); CER Gain = 2.442% (Gaussian, Mean-Variance) and 2.748% (Gaussian, CRRA).

- **At $k=8$ Predictors (All Variables):**
  - **CSM (Baseline):** TW = $166.06; CER Gain = 2.267% (Mean-Variance) and 2.579% (CRRA).
  - **CSM (Poly):** TW = $166.86; CER Gain = 2.324% (Mean-Variance) and 2.615% (CRRA).
  - **Clayton Copula:** TW = $173.94.

#### 3. Crisis Period Performance (Sub-sample Analysis, $k=8$, Initial Wealth = $1.00)
- **Global Financial Crisis (August 2007 – March 2009):**
  - Buy-and-Hold: TW = $0.59, MDD = 50.0%.
  - Momentum (3m/6m/12m): TW = $1.04–$1.09.
  - Decomposition models (CSM Baseline & Copulas): TW = **$0.80** (attenuated drawdown by roughly 50% relative to Buy-and-Hold).
  - Linear / CSR / MS: TW = $0.79–$0.82.
- **COVID-19 Shock (December 2019 – December 2021):**
  - 3-Month Momentum: TW = $1.95.
  - CSM (Poly) & Linear/CSR: TW = **$1.79**.
  - Buy-and-Hold & GARCH-M: TW = $1.57–$1.58.

#### 4. Statistical Model Confidence Set (MCS)
- In the 80% Model Confidence Set ($MCS_{80\%}$) across all $k \in \{1, \dots, 8\}$, the CSM models and copula-based decomposition models are **never eliminated** under either squared loss or absolute loss ($p$-values near 1.00).
- Linear OLS is eliminated at $k=3, 4, 5, 6, 8$ under squared loss.
- Markov-switching (MS) is eliminated at all $k$ under squared loss ($p$-values = 0.00).
- GARCH-M is eliminated at $k=4, 5, 6$ under squared loss.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Non-Monotonicity across Predictor Dimensions:** CSM performance is not monotonic in $k$. While achieving superior performance at $k=2, 3$ and $k=7, 8$, the baseline CSM model experiences a performance dip at intermediate dimensions ($k=4, 5, 6$), where terminal wealth drops to ~$120 and CER gains weaken. The polynomial variant (CSM Poly) mitigates but does not fully eliminate this dimensional sensitivity.
- **Sensitivity to In-Sample Subset Selection Criterion:** When best-$k$ subsets are selected using Mean Squared Error (MSE) instead of the Area Under the Curve (AUC) criterion, out-of-sample $R_{OOS}^2$ and portfolio returns deteriorate across all models (Table A2, Supplementary Material). CSM's edge over benchmarks is partially dependent on directional-accuracy-guided feature selection.
- **Crisis Underperformance Relative to Simple Momentum:** During acute panic drawdowns such as the GFC (2007–2009), backward-looking time-series momentum preserved capital significantly better (TW = $1.04–$1.09) than forward-looking decomposition models (TW = $0.80). Monthly macro indicators failed to trigger an instantaneous exit at the very onset of the liquidity crunch.
- **Marginal Utility Edge over Copulas at High Dimensions:** At $k=7$ and $k=8$, copula-based specifications (specifically Clayton and Gaussian) achieve slightly higher terminal wealth ($173–$178 vs $166–$168) and CER gains (by 9 to 14 bps) than CSM Baseline. While CSM avoids copula estimation complexity, it does not strictly dominate copulas in high-dimensional settings.

## Falsification plan

1. **Out-of-Sample Period Extension (2022–2026):**
   - *Test:* Extend the evaluation window from January 2022 to September 2026, encompassing the 2022 Fed rate hiking cycle and the 2023–2024 tech-driven bull market.
   - *Research-defined falsification threshold:* If annualized Sharpe ratio over 2022–2026 falls below the Buy-and-Hold S&P 500 Sharpe ratio by $> 0.15$, or if the CER gain relative to the historical average becomes negative ($< 0.0\%$), the directional timing edge is falsified.
2. **Predictor Shuffling / Placebo Test:**
   - *Test:* Permute the time-series order of lagged predictors $\bm{x}_{t-1}$ while preserving the empirical joint distribution of returns $(M_t, S_t)$.
   - *Research-defined falsification threshold:* If the true CSM model fails to achieve terminal wealth in the top 5th percentile ($p < 0.05$) of 1,000 synthetic scrambled-predictor trials, reject the hypothesis of macroeconomic predictive content.
3. **Transaction Cost Stress Test:**
   - *Test:* Evaluate the strategy under transaction costs scaled from 10 bps to 25 bps, 50 bps, and 100 bps per switch.
   - *Research-defined falsification threshold:* Because the strategy executes a low-turnover monthly switching rule (typically averaging fewer than 4–6 switches per year), if terminal wealth falls below Buy-and-Hold ($104.63) at a transaction cost $\le 30\text{ bps}$, the economic viability of the signal is falsified.
4. **Sign-on-Magnitude Link Ablation:**
   - *Test:* Set $\beta = 0$ in the probit model (CSM Independence specification), disconnecting the contemporaneous magnitude from directional sign probability.
   - *Research-defined falsification threshold:* If the full CSM model ($\beta \ne 0$) fails to generate a statistically significant increase in AUC ($p < 0.05$) or an annualized CER improvement of at least 25 bps over the decoupled independence model ($\beta = 0$), reject the hypothesis that conditioning sign on magnitude provides incremental value over decoupled marginals.

## Crypto portability

**Portability Classification:** Adapted / Unproven.

The economic mechanism was demonstrated solely on monthly U.S. equities (S&P 500) using macroeconomic indicators (`tbl`, `dfy`, `dfr`, etc.). Porting to cryptocurrency represents a `research interpretation` and requires significant adaptations:

- **Predictor Set Substitution:** Macro indicators updated at monthly frequency are ill-suited for crypto's high-volatility, sub-weekly regime cycles. Porting requires substituting macro indicators with crypto-native state variables:
  - *Magnitude predictors:* Trailing realized volatility (e.g., 7-day Garman-Klass or parkinson volatility), options implied volatility (Deribit DVOL), open interest change, and liquidation volume (`research-proposed`).
  - *Sign predictors:* Perpetual funding rate differentials, stablecoin exchange net inflows, cross-sectional basis, and cumulative volume delta (CVD) (`research-proposed`).
- **Timeframe Calibration:** The monthly switching rule must be adapted to daily or 4-hour / 8-hour funding intervals. Because crypto volatility clustering operates across intraday and multi-day horizons, the Weibull MEM can be fitted to daily absolute returns $|R_t|$.
- **Market Structure Frictions:**
  - *Funding & Carry:* Holding perpetual contracts rather than spot introduces funding drag that must be incorporated into the cash-hurdle calculation.
  - *24/7 Continuity:* Crypto markets do not have market open/close boundaries; execution timestamps must be fixed to UTC 00:00 midnight boundaries (`research-proposed`).
  - *Quote Currency Risk:* Cash positions must be held in USD stablecoins (USDT/USDC) rather than risk-free Treasury bills, incurring counterparty/depeg tail risk (`research-proposed`).

## Limitations

- **Equities-Only Empirical Validation:** Primary evidence is restricted to the S&P 500 index over 1948–2021. The source provides zero empirical tests in cryptocurrency, commodities, or foreign exchange.
- **Low-Frequency Focus:** The model operates strictly at a monthly frequency. High-frequency or intraday applicability is unexamined.
- **Macro Data Lag (`data gap`):** While predictors are lagged one month, real-world reporting delays for macroeconomic variables (e.g., inflation releases occur mid-month) introduce potential look-ahead leakage in historical Goyal-Welch datasets unless strictly point-in-time publication calendars are enforced.
- **Parameter Sensitivity:** While the probit log-likelihood is globally concave, Weibull-MEM numerical optimization and 1-D numerical integration for $\xi_t^*$ introduce computational latency during rolling walk-forward re-estimation.
- **Binary Sizing Constraint:** The empirical strategy uses a binary 100% equity / 100% cash rule. Continuous position sizing (e.g., Kelly scaling or volatility targeting) is uninvestigated in the primary paper.

## Implementation status

No implementation in our research stack has been completed. The strategy is `research-only`.

No code has been committed to `nautilus-quant-system`, PyBroker, NautilusTrader, Paper, Testnet, or Live execution pipelines.

## Adoption boundary

This record is research material only. Presence in this repository does not constitute:
- Verified or profitable alpha;
- Authorization for algorithmic implementation;
- Approval for paper trading;
- Approval for testnet deployment;
- Approval for live capital allocation.

Any future progression toward implementation requires formal PyBroker isolated backtesting and subsequent NautilusTrader validation.

## Related Wiki records

- `[[two-stage-adaptive-shrinkage-golden-criterion-equity-premium-2026-09-02]]` — Explores model combination and shrinkage across Goyal-Welch predictors for S&P 500 equity premium forecasting.
- `[[continuous-macro-timing-growth-defensive-style-allocation-2026-09-02]]` — Continuous macro indicator timing on equity style rotation sleeves.
- `[[regime-switching-hmm-reinforcement-learning-etf-allocation-2026-09-04]]` — Regime-dependent macro allocation across equity ETFs.

## Sources

1. **Primary Working Paper & Full Text:**
   Arsène Brou and Richard Luger, *"A new decomposition approach to modeling financial returns: Conditioning sign on magnitude"*, arXiv preprint `arXiv:2606.04153v1 [q-fin.ST]`, submitted June 2, 2026.
   - Stable Abstract URL: [https://arxiv.org/abs/2606.04153](https://arxiv.org/abs/2606.04153)
   - Canonical HTML: [https://arxiv.org/html/2606.04153v1](https://arxiv.org/html/2606.04153v1)
   - PDF: [https://arxiv.org/pdf/2606.04153v1](https://arxiv.org/pdf/2606.04153v1)
2. **Journal Article (In Press):**
   Arsène Brou and Richard Luger, *"A new decomposition approach to modeling financial returns: Conditioning sign on magnitude"*, *Journal of Banking & Finance*, 2026, Article 107716.
   - DOI: [https://doi.org/10.1016/j.jbankfin.2026.107716](https://doi.org/10.1016/j.jbankfin.2026.107716)
3. **Underlying Predictor Dataset:**
   Ivo Welch and Amit Goyal, *"A comprehensive look at the empirical performance of equity premium prediction"*, *Review of Financial Studies*, 21(4), 1455–1508, 2008. Dataset updated through 2021 via Amit Goyal web repository: [http://www.hec.unil.ch/agoyal/](http://www.hec.unil.ch/agoyal/).
4. **Foundation Methodology Reference:**
   Stanislav Anatolyev and Nikolay Gospodinov, *"Modeling financial return dynamics via decomposition"*, *Journal of Business & Economic Statistics*, 28(2), 232–245, 2010. DOI: [10.1198/jbes.2009.07127](https://doi.org/10.1198/jbes.2009.07127).
