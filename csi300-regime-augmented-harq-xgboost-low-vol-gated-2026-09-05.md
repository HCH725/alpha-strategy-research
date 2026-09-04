---
schema: strategy-research-record-v1
title: "CSI 300 Regime-Augmented HARQ and Walk-Forward XGBoost: Low-Volatility Gated Signal-by-Risk Allocation under Implementation Frictions"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equity-index
  - csi300
  - realized-volatility
  - high-frequency-data
  - harq
  - markov-switching
  - gjr-garch
  - msgarch
  - xgboost
  - walk-forward-optimization
  - regime-gating
  - risk-scaling
  - turnover-control
  - transaction-costs
status: research-only
confidence: high
source_as_of: 2026-06-08
sources:
  - "arXiv:2606.09478v1 [q-fin.TR, q-fin.CP, q-fin.MF], June 8, 2026. https://arxiv.org/abs/2606.09478"
  - "https://doi.org/10.48550/arXiv.2606.09478"
  - "https://arxiv.org/html/2606.09478v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# CSI 300 Regime-Augmented HARQ and Walk-Forward XGBoost: Low-Volatility Gated Signal-by-Risk Allocation under Implementation Frictions

## Provenance

- **Primary Source:** Xinyue Fang and Robert Ślepaczuk (Quantitative Finance Research Group, Faculty of Economic Sciences, University of Warsaw), *"Volatility Forecasting and Return Prediction under Market Regimes: Evidence from High-Frequency Chinese Equity Data"*, arXiv preprint `arXiv:2606.09478v1 [q-fin.TR, q-fin.CP, q-fin.MF]`, submitted June 8, 2026.
- **Canonical DOI:** [10.48550/arXiv.2606.09478](https://doi.org/10.48550/arXiv.2606.09478)
- **Stable Abstract URL:** [https://arxiv.org/abs/2606.09478](https://arxiv.org/abs/2606.09478)
- **Full Text HTML:** [https://arxiv.org/html/2606.09478v1](https://arxiv.org/html/2606.09478v1)
- **Data Examined:**
  - High-frequency 5-minute intraday price observations and daily closing prices for the CSI 300 Index (`sh000300`), published by the Shanghai Stock Exchange, sourced from Wind Financial Terminal (Wind Information Co., Ltd.).
  - Total Sample Period: April 8, 2005 to May 31, 2023.
  - Data Filtering Protocol: Retains only continuous trading sessions (09:30–11:30 and 13:00–15:00 CST). Excludes opening auction, overnight return discontinuities, and the 11:30–13:00 midday break. The initial 5-minute bar is computed from continuous session trades.
  - Out-of-Sample Evaluation Windows:
    - Volatility Forecasting Stage: August 21, 2013 to May 29, 2023 ($N = 2,326$ trading days; initial 6-year training window).
    - Return Prediction & Strategy Stage: December 17, 2014 to May 26, 2023 ($N = 2,004$ trading days; initial $N_{\min} = 300$ observations split into 180 training and 120 validation).
    - Cross-Frequency Robustness Common Window: March 30, 2015 to May 26, 2023 ($N = 1,947$ trading days).

## Economic mechanism

### Source-reported

The study investigates whether econometric regime-dependent volatility forecasting and machine-learning return prediction can be sequentially integrated to improve both statistical accuracy and net economic performance in equity markets.

The authors document three fundamental empirical realities:
1. **Strong volatility predictability vs. weak return predictability:** Realized volatility in the Chinese CSI 300 equity market exhibits pronounced persistence, long memory, and state-dependent clustering. In contrast, directional return predictability has a low signal-to-noise ratio, is episodic, and is fragile.
2. **State-dependent predictability concentration:** Return predictability is asymmetric across market regimes. Directional forecasting accuracy is statistically detectable and positive during low-volatility regimes ($p_t \le 0.5$), but completely collapses and turns negative during high-volatility regimes ($p_t > 0.5$), which are dominated by unstable exogenous shocks and noise.
3. **The friction attrition barrier:** Naive machine-learning return-forecasting strategies fail after applying realistic transaction costs (5 basis points). To salvage economic utility, directional predictions must be engineered into a defensive, risk-controlled portfolio allocation framework using:
   - Volatility scaling (weighting expected return inversely by forecasted risk);
   - Low-volatility regime gating (suppressing exposure when high-volatility probability rises);
   - Signal thresholding (filtering out weak, noisy forecasts);
   - Turnover management (weekly rebalancing coupled with a no-trade band).

### Research interpretation

1. **Noise-trader regime decoupling in retail-heavy markets:** The CSI 300 market is characterized by high retail participation and behavioral trading waves. In tranquil, low-volatility states, market liquidity is orderly, allowing tree-based nonlinear models (XGBoost) to extract weak momentum and mean-reversion drift. In turbulent high-volatility states (e.g., the 2015 margin crash, 2018 trade war escalations, or COVID dislocations), panic selling, forced liquidations, and government interventions overwhelm statistical patterns, turning directional forecasts into negative alpha.
2. **Volatility regime probability as an exposure circuit breaker:** The filtered probability $p_t$ from the Markov-switching GJR-GARCH model does not generate standalone directional alpha; rather, it functions as an information-reliability filter. Gating exposure via $(1 - p_t)$ systematically steps aside during periods when the model's forecasting machinery has negative expected value.
3. **Defensive asymmetric payoff profile:** The strategy is explicitly not return-maximizing. Its economic value stems from drawdown suppression and tail-risk defense: during the 2015–2016 crash, it delivered $+10.24\%$ net return while Buy-and-Hold suffered $-39.38\%$ (drawdown $-14.52\%$ vs. $-50.29\%$). However, during strong, sustained bull-market expansions (such as 2017 or the 2020 post-COVID rebound), the strategy underperforms Buy-and-Hold because it remains neutral or throttles exposure.

## Signal

The sequential forecasting and execution pipeline is fully specified in the primary source:

### Stage 1: Volatility Forecasting Framework (`source-reported`)
1. **Intraday Realized Measures:**
   From 5-minute continuous session log-returns $r_{t,i}$ ($i = 1, \dots, M_t$):
   - Realized Variance: $RV_t = \sum_{i=1}^{M_t} r_{t,i}^2$
   - Realized Quarticity: $RQ_t = \frac{M_t}{3} \sum_{i=1}^{M_t} r_{t,i}^4$
   - Bipower Variation: $BPV_t = \mu_1^{-2} \sum_{i=2}^{M_t} |r_{t,i}| |r_{t,i-1}|$, with $\mu_1 = \sqrt{2/\pi}$
   - Signed Jump Measure: $CJ_t = \max(RV_t - BPV_t, 0) \cdot \text{sign}(r_t)$, where $r_t = \ln(P_t/P_{t-1})$ is daily close-to-close return.
2. **Baseline HARQ Model:**
   $$\log(RV_{t+1}) = \beta_0 + \left(\beta_d + \beta_q \frac{\sqrt{RQ_t}}{RV_t}\right) \log(RV_t) + \beta_w \log(RV_{t,w}) + \beta_m \log(RV_{t,m}) + \epsilon_{t+1}$$
   where $RV_{t,w} = \frac{1}{5}\sum_{k=0}^4 RV_{t-k}$ and $RV_{t,m} = \frac{1}{22}\sum_{k=0}^{21} RV_{t-k}$.
3. **Residual-Based Regime Identification (MS-GJR-GARCH):**
   HARQ residuals $e_t$ are modeled via a 2-state Markov-switching GJR-GARCH(1,1) model with Student-$t$ innovations (`MSGARCH`):
   $$\sigma_{t,j}^2 = \omega_j + (\alpha_j + \gamma_j I_{\{e_{t-1} < 0\}}) e_{t-1}^2 + \beta_j \sigma_{t-1,j}^2, \quad j \in \{1, 2\}$$
   Filtered high-volatility regime probability $p_t = P(S_t = \text{High} \mid \mathcal{F}_t)$ is extracted strictly contemporaneously (no smoothed probabilities, no lookahead).
4. **Regime-Augmented HARQ Forecast:**
   $$\widehat{\log RV}_{t+1} = \hat{\beta}_0 + \hat{\beta}_d \log(RV_t) + \hat{\beta}_q \left(\frac{\sqrt{RQ_t}}{RV_t} \log(RV_t)\right) + \hat{\beta}_w \log(RV_{t,w}) + \hat{\beta}_m \log(RV_{t,m}) + \hat{\gamma}_p p_t$$
   Forecasted daily volatility: $\hat{\sigma}_{t+1} = \sqrt{\exp(\widehat{\log RV}_{t+1})}$.

### Stage 2: Walk-Forward XGBoost Return Prediction (`source-reported`)
1. **Predictor Set (12 features observed at time $t$):**
   - *Volatility features:* $\log(RV_t)$, forecasted log-RV $\widehat{\log RV}_{t+1}$ (`logRVhat_t1`), $\log(RQ_t)$, signed jump $CJ_t$, 5-day average volatility $\text{vol\_lag5}_t$, 22-day average volatility $\text{vol\_lag22}_t$.
   - *Regime features:* Filtered high-vol probability $p_t$, lagged probability $p_{t-5}$ (`pt_lag5`), interaction term $\text{vol\_pt}_t = \log(RV_t) \cdot p_t$.
   - *Return dynamics:* Daily return $r_t$, 5-day return $r_{t,w}$, 22-day return $r_{t,m}$.
2. **Estimation & Hyperparameter Tuning Protocol:**
   - Expanding-window walk-forward validation with quarterly (3M) re-estimation.
   - Initial window: $N_{\min} = 300$ observations (180 train, 120 validation).
   - Candidate hyperparameter grid:
     $$\{(\text{n\_estimators}=50, \text{max\_depth}=2, \eta=0.05, \gamma=0.0, \lambda=1.0),$$
     $$(100, 2, 0.03, 0.1, 1.0), (100, 3, 0.03, 0.1, 1.0), (200, 2, 0.01, 0.2, 2.0)\}$$
   - Objective: maximize predictive Pearson correlation on validation set. If all candidates yield correlation $\le 0$, defaults to $(200, 2, 0.01, 0.2, 2.0)$ and treated as zero.
   - Target: next-day return $\hat{r}_{t+1}$.

### Stage 3: Low-Vol Gated Weekly Signal-by-Risk Execution Pipeline (`source-reported`)
1. **Risk-Adjusted Signal:**
   $$s_t^{\text{comb}} = \frac{\hat{r}_{t+1}}{\hat{\sigma}_{t+1}}$$
2. **Low-Volatility Gating:**
   $$s_t^{\text{gated}} = s_t^{\text{comb}} \cdot (1 - p_t)$$
   with gating parameter $\kappa = 1.0$ (complete suppression as $p_t \to 1$).
3. **Threshold Filtering:**
   Let $\theta_t(q)$ be the recursive walk-forward empirical $q$-th quantile of $|s_{1:t-1}^{\text{gated}}|$ using only past data, with baseline $q = 0.60$:
   $$\tilde{s}_t = \begin{cases} s_t^{\text{gated}} & \text{if } |s_t^{\text{gated}}| > \theta_t(q) \\ 0 & \text{otherwise} \end{cases}$$
4. **Walk-Forward Position Scaling & Capping:**
   Scaling coefficient $c_t^{WF}$ targets an average absolute exposure of 0.5:
   $$c_t^{WF} = \frac{0.5}{\frac{1}{t-1}\sum_{\tau=1}^{t-1} |\tilde{s}_\tau|}$$
   Target portfolio weight:
   $$w_t^* = \text{sign}(\tilde{s}_t) \cdot \min\left(c_t^{WF} |\tilde{s}_t|, w_{\max}\right), \quad \text{with } w_{\max} = 0.60$$
5. **Weekly Rebalancing & No-Trade Band:**
   Rebalancing occurs weekly. On rebalancing date $t$, if $|w_t^* - w_{t-1}| > b$ with baseline $b = 0.02$, execute $w_t = w_t^*$; otherwise keep $w_t = w_{t-1}$. On non-rebalancing days, hold $w_t = w_{t-1}$.

## Required data

- **Instrument:** CSI 300 Index (`sh000300`), Chinese A-share equity index.
- **Venue / Source:** Shanghai Stock Exchange / Shenzhen Stock Exchange; 5-minute intraday bars and daily closing prices from Wind Financial Terminal (Wind Information Co., Ltd.).
- **Timeframe & Session Alignment:**
  - 5-minute sampling interval across continuous sessions: 09:30–11:30 and 13:00–15:00 CST ($M_t = 48$ intraday bars per regular session).
  - Explicit exclusion of overnight gap, opening call auction, and 90-minute midday lunch break.
- **Fields Required:** Intraday Open, High, Low, Close, Volume; Daily Close.
- **Point-in-Time Constraint:** All predictors formed at time $t$ use data strictly prior to or at market close on day $t$. Target is return over $(t, t+1]$. No future information or smoothed probabilities permitted.
- **Missing Data Handling:** Non-trading days and market halts follow exchange holiday calendar; zero-trade intraday 5-minute intervals retain previous price.

## Execution assumptions

- **Transaction Costs (`source-reported`):** One-way cost of 5 basis points ($c = 0.0005$, or 0.05%), evaluated across sensitivity levels of 0, 5, 10, and 15 bps. Break-even cost is 19.97 bps on the full out-of-sample sample and 8.96 bps on the common sample.
- **Signal-to-Order Timing (`source-reported`):** Daily close to next-day close return realization ($R_{t+1}^{\text{gross}} = w_t r_{t+1}$).
- **Net Return Accounting (`source-reported`):**
  $$R_{t+1}^{\text{net}} = w_t r_{t+1} - c \cdot |w_t - w_{t-1}|$$
- **Short-Selling Assumption (`source-reported`):**
  - The baseline unrestricted strategy permits short positions. Realized allocation: $20.66\%$ Long, $12.57\%$ Short, $66.77\%$ Neutral.
  - *Source caveat:* Chinese cash equity markets enforce strict short-selling constraints. Under a constrained Long-Only decomposition, net Sharpe drops from $+0.255$ to $-0.046$ at 5 bps.
- **Execution Vehicle (`research-proposed`):**
  - Direct execution of the cash index is non-tradable. Realistic implementation requires CSI 300 index futures (IF contracts traded on the China Financial Futures Exchange [CFFEX]) or liquid CSI 300 ETFs (e.g., 510300.SH / 159919.SZ) with margin financing and securities lending.
- **Fill Model & Impact (`research-proposed`):** Zero price slippage or market impact beyond the 5 bp flat fee; fill assumed at closing price. Cash allocation on neutral days earns 0% yield.

## Evidence

### Source-reported

All figures below are transcribed directly from Xinyue Fang and Robert Ślepaczuk (arXiv:2606.09478v1, June 2026):

#### 1. Volatility Forecasting Out-of-Sample Performance (Table 2 & 3, 2013-08-21 to 2023-05-29, $N = 2,326$)
- **Forecast Loss Metrics:**
  - HARQ + $p_t$: MSE (log) = $0.267345$, QLIKE = $0.162259$, LMAE (log) = $0.402701$.
  - Baseline HARQ: MSE (log) = $0.279911$, QLIKE = $0.171013$, LMAE (log) = $0.410499$.
  - All three loss metrics confirm superior predictive accuracy for the regime-augmented model.
- **Mincer-Zarnowitz Regressions:**
  - HARQ + $p_t$: $R^2 = 0.5398$ (vs. $0.5215$ for Baseline HARQ). Joint calibration null $\alpha = 0, \beta = 1$ is rejected for both ($F = 12.39$, $p = 4 \times 10^{-6}$).
- **Conditional Diebold-Mariano Tests (Table 4, QLIKE loss):**
  - Median RV split (High-vol, $N = 1,163$): Mean loss diff = $+0.015212$, DM stat = $2.5818$ ($p = 0.0049$).
  - Median RV split (Low-vol, $N = 1,163$): Mean loss diff = $+0.002296$, DM stat = $1.3890$ ($p = 0.0824$).
  - Top 25% RV split (Extreme High-vol, $N = 582$): Mean loss diff = $+0.022078$, DM stat = $2.0639$ ($p = 0.0195$).
  - Top 25% RV split (Normal/Low-vol, $N = 1,744$): Mean loss diff = $+0.004308$, DM stat = $3.0933$ ($p = 0.0010$).

#### 2. Return Prediction Out-of-Sample Performance (Table 5, 2014-12-17 to 2023-05-26, $N = 2,004$)
- **Full Sample:** Pearson correlation $r = 0.0449$, Hit Ratio = $53.49\%$, HAC-corrected Newey-West $p = 0.0009$, MAE = $0.0102$.
- **Low-Volatility Subsample ($p_t \le 0.5$, $N = 1,620$):** Pearson correlation $r = 0.0638$, Hit Ratio = $53.77\%$, HAC $p = 0.0013$, MAE = $0.0101$.
- **High-Volatility Subsample ($p_t > 0.5$, $N = 384$):** Pearson correlation $r = -0.0617$, Hit Ratio = $52.34\%$, HAC $p = 0.1928$ (insignificant), MAE = $0.0104$.

#### 3. Main Strategy Net Performance vs. Benchmarks (Table 6, 5 bp fees, 2014-12-17 to 2023-05-26, $N = 2,004$)
| Strategy | ARC (%) | ASD (%) | MaxDD (%) | Sharpe | Sortino | IR** (TE) | IR*** (DTE) | MLD (days) | Trades | %Long | %Short | %Neutral |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Buy & Hold** | -1.11 | 23.38 | -50.60 | -0.047 | -0.062 | – | – | 1,899 | 1 | 100.00 | 0.00 | 0.00 |
| **Momentum Weekly** | 2.13 | 11.68 | -26.71 | 0.182 | 0.258 | 0.042 | 0.065 | 1,798 | 92 | 54.39 | 45.51 | 0.10 |
| **Vol-managed B&H Weekly** | -0.44 | 10.04 | -24.94 | -0.043 | -0.057 | -0.110 | -0.166 | 1,315 | 272 | 96.96 | 0.00 | 3.04 |
| **Regime-only Long-Flat** | -2.25 | 10.69 | -34.55 | -0.210 | -0.272 | -0.235 | -0.342 | 1,899 | 49 | 79.84 | 0.00 | 20.16 |
| **Regime-only Long-Short** | -4.75 | 11.69 | -45.49 | -0.407 | -0.528 | -0.328 | -0.463 | 1,899 | 49 | 79.84 | 20.06 | 0.10 |
| **Low-vol Gated Weekly Signal×Risk** | **1.93** | **7.56** | **-14.52** | **0.255** | **0.394** | **0.021** | **0.034** | **1,384** | **163** | **20.66** | **12.57** | **66.77** |

#### 4. Event-Window Stress Performance (Table 8)
- **2015–2016 Crash:** Strategy cumulative return $+10.24\%$ vs. B&H $-39.38\%$ (difference $+49.62\%$, Sharpe $0.546$ vs. $-0.855$, MaxDD $-14.52\%$ vs. $-50.29\%$).
- **2018–2019 Trade War:** Strategy cumulative return $-0.40\%$ vs. B&H $-2.91\%$ (Sharpe $-0.043$ vs. $-0.071$, MaxDD $-5.74\%$ vs. $-34.26\%$).
- **2020 COVID Rebound:** Strategy cumulative return $+6.32\%$ vs. B&H $+23.71\%$ (Sharpe $1.581$ vs. $1.077$, MaxDD $-2.17\%$ vs. $-16.88\%$).
- **Post-COVID 2021–2023:** Strategy cumulative return $-0.12\%$ vs. B&H $-30.11\%$ (Sharpe $-0.006$ vs. $-0.793$, MaxDD $-12.44\%$ vs. $-41.41\%$).

#### 5. Component Decomposition & Ablation (Tables 17, 19 & 20)
- **Signal Decomposition (at 5 bp fees):**
  - Combined Signal $\times$ Risk: ARC $1.93\%$, ASD $7.56\%$, Sharpe $0.255$, MaxDD $-14.52\%$.
  - Return-only: ARC $0.66\%$, ASD $7.62\%$, Sharpe $0.086$, MaxDD $-18.07\%$.
  - Volatility-only: ARC $-0.45\%$, ASD $6.17\%$, Sharpe $-0.073$, MaxDD $-15.16\%$.
- **Long-Only Constraint Impact (Table 20, 5 bp fees):**
  - Combined Long-only Signal $\times$ Risk: ARC $-0.25\%$, ASD $5.41\%$, Sharpe $-0.046$, MaxDD $-15.06\%$ (virtually identical Sharpe to Buy & Hold $-0.047$).
- **Feature Ablation (Table 17, 5 bp fees):**
  - Main Model: Sharpe $0.2551$, MaxDD $-14.52\%$, break-even fee $19.97$ bps.
  - No Vol Forecast (`logRVhat_t1` excluded): Sharpe $0.0902$, MaxDD $-20.90\%$, break-even fee $10.83$ bps.
  - No Regime ($p_t, p_{t-5}, \text{vol\_pt}$ excluded): Sharpe $0.1800$, MaxDD $-17.60\%$, break-even fee $15.88$ bps.
  - No High-Order Risk ($RQ, CJ$ excluded): Sharpe $0.2604$, MaxDD $-14.39\%$, break-even fee $20.56$ bps.
  - No Forecast/Regime Conditioning: Sharpe $-0.0083$, MaxDD $-19.22\%$, break-even fee $4.59$ bps.
- **Normalized Naive Signal $\times$ Risk Benchmark (Table 21):**
  - Raw unconstrained signal has gross return $5.73\%$ (Sharpe $0.444$, turnover $0.2649$). At 5 bp fees, net return falls to $2.26\%$ (Sharpe $0.176$, MaxDD $-46.85\%$).

### Independently reproduced

Not independently reproduced. All figures and model specifications trace directly to Fang & Ślepaczuk (arXiv:2606.09478v1).

### Negative evidence

The primary authors provide rigorous diagnostic tests that explicitly qualify and limit the strategy's statistical claims:
1. **Insignificant Bootstrap Sharpe Dominance (Table 7):**
   A circular block bootstrap test (5,000 replications, 20-day blocks) testing $H_0: \text{Sharpe} \le 0$ yields an observed Sharpe of $0.255$ with a wide 95% bootstrap confidence interval of $[-0.683, +0.599]$ and a bootstrap $p$-value of $0.182$. Statistical superiority over zero cannot be established at conventional confidence levels.
2. **Multiple Testing & Data Snooping Failures (Table 15 & Section 6.9):**
   - White Reality Check-style test across re-estimation frequencies (1M, 3M, 6M): $p = 0.4636$.
   - Hansen SPA-style test across re-estimation frequencies: $p = 0.3948$.
   - White Reality Check across the $q \times b$ parameter grid ($q \in [0.50, 0.70], b \in [0.00, 0.03]$): $p \approx 0.502$.
   - Hansen SPA across the $q \times b$ parameter grid: $p \approx 0.495$.
   - The authors conclude that the apparent superiority of the baseline parameter set ($q=0.60, b=0.02$) is not statistically significant after correcting for search-space data snooping.
3. **Re-estimation Frequency Brittleness (Table 13 & 14):**
   On the common out-of-sample window ($N = 1,947$), only the quarterly (3M) specification generates positive net return ($1.93\%$, Sharpe $0.226$, break-even cost $8.96$ bps). The 1M re-estimation model suffers from turnover attrition (Sharpe $-0.378$, break-even $0.00$ bps), while the 6M model fails to adapt (Sharpe $-0.634$, break-even $0.00$ bps).
4. **Complete Collapse under Long-Only Restrictions (Table 20):**
   When constrained to long-only positions ($w_t \ge 0$), net return turns negative ($-0.25\%$) and net Sharpe drops to $-0.046$ after 5 bp fees, offering zero return advantage over Buy & Hold ($-0.047$).
5. **High-Volatility Alpha Inversion:**
   During elevated volatility regimes ($p_t > 0.5$), the return prediction correlation turns negative ($-0.0617$), and the hit ratio drops to $52.34\%$ ($p = 0.1928$), demonstrating that ML directional signals are completely unreliable in panic environments.
6. **Bull Market Lag:**
   During the 2020 post-COVID rebound, the strategy generated $+6.32\%$ vs. $+23.71\%$ for Buy & Hold, illustrating significant opportunity cost during sustained upside trends.

## Falsification plan

The strategy's central thesis asserts that high-frequency realized volatility modeling combined with filtered regime gating can rescue weak ML return forecasts to produce defensive, drawdown-controlled portfolio performance net of costs. The following empirical tests define falsification:

1. **Out-of-Sample Expansion Test (2023–2026):**
   - *Test:* Execute the exact frozen 3M walk-forward XGBoost + MS-HARQ pipeline on CSI 300 5-minute data from June 1, 2023 through December 31, 2026.
   - *Failure rule (`research-defined falsification threshold`):* If net Sharpe ratio falls below $0.00$ after 5 bp transaction costs, or if maximum drawdown exceeds $-20.0\%$ over this extended period, the hypothesis of persistent defensive outperformance is falsified.
2. **Transaction Cost & Slippage Stress Test:**
   - *Test:* Re-evaluate strategy performance across realistic institutional execution friction schedules ($c \in [5, 10, 15, 20]$ bps).
   - *Failure rule (`research-defined falsification threshold`):* If the strategy's net Sharpe ratio drops below $0.00$ at a one-way execution friction of $10.0$ bps (matching the common-window break-even threshold of $8.96$ bps), the strategy is classified as an un-executable friction artifact.
3. **Long-Only Vehicle Feasibility Test:**
   - *Test:* Backtest the strategy restricted to $w_t \ge 0$ (long-only ETF / cash equity vehicle).
   - *Failure rule (`research-defined falsification threshold`):* If the net Sharpe ratio is $\le 0.00$ under 5 bp transaction costs, the strategy is declared non-viable for long-only mutual fund and standard retail accounts (already indicated by source Table 20).
4. **Regime Gating Placebo / Permutation Test:**
   - *Test:* Replace the filtered high-volatility probability $p_t$ with a randomized time-series permutation $\tilde{p}_t$ (destroying regime timing while preserving distribution).
   - *Failure rule (`research-defined falsification threshold`):* If the placebo gated strategy achieves a maximum drawdown reduction within $1.0$ percentage point of the genuine model (e.g., MaxDD $\le -15.5\%$), the economic gating hypothesis is refuted (indicating drawdown reduction is merely an artifact of random cash holding rather than regime detection).

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Porting Rationale:** The primary source investigates the Chinese domestic CSI 300 cash equity market. Porting this framework to cryptocurrency represents an unproven research hypothesis.
- **Crypto Microstructure Adaptations (`research-proposed`):**
  1. *Perpetual Futures Vehicle:* Crypto perpetual contracts (e.g., BTC/USDT or ETH/USDT on Binance, Bybit, or Hyperliquid) natively support two-sided execution ($w_t \in [-w_{\max}, +w_{\max}]$), directly solving the domestic equity short-sale friction that crippled the long-only decomposition in Table 20.
  2. *24/7 Session & Interval Normalization:* Unlike the CSI 300 (which trades 4 hours per day with opening and midday exclusions), crypto trades 24/7. Calculating daily realized measures requires fixing a synthetic daily boundary (e.g., 00:00:00 UTC) with $M_t = 288$ five-minute bars per day (`research-proposed`).
  3. *Funding Cost Drag:* Holding perpetual contracts across funding timestamps (typically every 8 hours) incurs positive or negative carry. Because the strategy is neutral for $66.77\%$ of the sample, funding costs are avoided during neutral cash states, but active long/short positions must incorporate funding fee deductions into the net return equation (`research-proposed`).
  4. *Microstructure Noise & Jumps:* Crypto markets exhibit heavy bid-ask bouncing, round-the-clock liquidity shifts, and liquidation cascades. 5-minute sampling may suffer higher microstructure bias than equity index sampling, requiring jump-robust bipower variation or sub-sampled realized variance (`research-proposed`).

## Limitations

1. **Single-Market Specificity:** Evaluated exclusively on the CSI 300 Index; results may reflect idiosyncratic features of the Chinese A-share market (such as price limits, retail trading dominance, and high turnover) that do not generalize to global macro or crypto assets.
2. **Non-Tradability of the Cash Index:** The underlying asset analyzed is the cash spot index ($P_t$). Trading the strategy in practice requires either CSI 300 index futures (IF) or index ETFs, introducing tracking error, roll costs, financing rates, and dividend adjustments.
3. **Generated Regressor Bias:** Forecasted volatility $\widehat{\log RV}_{t+1}$ is an estimated quantity fed into the Stage 2 XGBoost model, propagating first-stage estimation uncertainty and parameter estimation errors into return predictions.
4. **Weak Statistical Alpha Significance:** Circular block bootstrap tests yield $p = 0.182$ for Sharpe $> 0$, and multiple-testing adjustments (White Reality Check $p = 0.4636$, Hansen SPA $p = 0.3948$) indicate that the strategy cannot be claimed as statistically superior to random parameter search.
5. **Re-estimation Brittleness:** Strategy performance is sensitive to model re-estimation cadence: while 3M updating produces positive net Sharpe, 1M and 6M updating yield negative Sharpe ratios ($-0.378$ and $-0.634$).
6. **Asymmetric Bull-Market Underperformance:** The heavy cash allocation ($66.77\%$ neutral) and exposure caps cause severe underperformance during explosive bull regimes.

## Implementation status

- `not-implemented`.
- No prototype or production code has been implemented in PyBroker, NautilusTrader, paper trading, testnet, or live trading.
- This record represents an external research capture and econometric audit only.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- A strategy record being present in this repository does not indicate statistical proof of alpha, operational readiness, or authorization for capital allocation.

## Related Wiki records

- `[[quant/china-ashare-xgboost-treeshap-behavioral-factor-decomposition-2026-09-04]]` (China A-share equity return predictability via XGBoost and TreeSHAP)
- `[[quant/hybrid-xgboost-finbert-regime-adaptive-equity-2026-09-04]]` (Hybrid XGBoost and FinBERT regime-adaptive equity strategy)
- `[[quant/equity-cross-regime-bayesian-optimisation-xgboost-tabnet-hybrid-2026-09-02]]` (Equity cross-regime Bayesian optimization XGBoost-TabNet hybrid)
- `[[quant/crypto-hourly-bitcoin-walk-forward-cost-aware-execution-2026-09-01]]` (Walk-forward cost-aware execution filter for hourly BTC)
- `[[quant/cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02]]` (Cross-sectional volatility regime-gated residual mixture of experts)

## Sources

1. **Primary Paper:** Xinyue Fang and Robert Ślepaczuk (Quantitative Finance Research Group, Faculty of Economic Sciences, University of Warsaw), *"Volatility Forecasting and Return Prediction under Market Regimes: Evidence from High-Frequency Chinese Equity Data"*, arXiv preprint `arXiv:2606.09478v1 [q-fin.TR, q-fin.CP, q-fin.MF]`, submitted June 8, 2026.
   - Stable arXiv URL: [https://arxiv.org/abs/2606.09478](https://arxiv.org/abs/2606.09478)
   - Canonical DOI: [10.48550/arXiv.2606.09478](https://doi.org/10.48550/arXiv.2606.09478)
   - HTML Full Text: [https://arxiv.org/html/2606.09478v1](https://arxiv.org/html/2606.09478v1)
2. **Econometric Methodological Citations:**
   - D. Ardia, K. Bluteau, K. Boudt, L. Catania, and D. Trottier, *"Markov-switching GARCH models in R: The MSGARCH package"*, Journal of Statistical Software 91 (4), pp. 1–38 (2019). [Basis for residual MS-GJR-GARCH model].
   - T. Bollerslev, A. J. Patton, and R. Quaedvlieg, *"Exploiting the errors: A simple approach for improved volatility forecasting"*, Journal of Econometrics 192 (1), pp. 1–18 (2016). [HARQ specification and quarticity formulation].
   - T. Chen and C. Guestrin, *"XGBoost: A scalable tree boosting system"*, In Proceedings of the 22nd ACM SIGKDD Conference, pp. 785–794 (2016). [Stage 2 gradient boosting engine].
   - F. Corsi, *"A simple approximate long-memory model of realized volatility"*, Journal of Financial Econometrics 7 (2), pp. 174–196 (2009). [HAR framework].
   - O. Ledoit and M. Wolf, *"Robust performance hypothesis testing with the Sharpe ratio"*, Journal of Empirical Finance 15 (5), pp. 850–859 (2008). [Circular block bootstrap inference].
