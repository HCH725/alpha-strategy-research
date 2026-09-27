---
schema: strategy-research-record-v1
title: "Joint Return and Risk Modeling with Deep Neural Networks for Portfolio Construction"
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-03-09
sources:
  - https://arxiv.org/abs/2603.19288
  - https://arxiv.org/html/2603.19288v1
  - https://arxiv.org/pdf/2603.19288v1
  - https://doi.org/10.48550/arXiv.2603.19288
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Joint Return and Risk Modeling with Deep Neural Networks for Portfolio Construction

## Provenance

- **Primary Source:** Keonvin Park (Interdisciplinary Program in Artificial Intelligence, Seoul National University, Seoul, 08829, South Korea; email: `kbpark16@snu.ac.kr`), *"Joint Return and Risk Modeling with Deep Neural Networks for Portfolio Construction"*, arXiv preprint `arXiv:2603.19288v1 [q-fin.PM]`, cross-listed in `cs.AI` and `cs.LG`, submitted March 9, 2026 (2026-03-09T01:49:51Z).
- **Canonical DOI:** [10.48550/arXiv.2603.19288](https://doi.org/10.48550/arXiv.2603.19288) (arXiv-issued DOI via DataCite).
- **Stable Abstract URL:** https://arxiv.org/abs/2603.19288
- **Full Text HTML:** https://arxiv.org/html/2603.19288v1
- **Full Text PDF:** https://arxiv.org/pdf/2603.19288v1 (9 pages, 1,678,806 bytes, SHA-256 `f1f7f3c0ec3365083d421ffcbec7f21f8335f2d35a5e734f2b4ee9c549a4e14c`, downloaded and directly inspected 2026-09-27).
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Publication Status:** Preprint only; no journal reference or publisher DOI appears on arXiv as of 2026-09-27.
- **Code and Data Availability:** No public repository link or open-source implementation is provided in the paper. The data availability statement notes: "The datasets analysed during the current study are available from the corresponding author upon reasonable request."
- **Pre-write Deduplication Audit (2026-09-27):** Repository-wide search across 1,024 Markdown records in this workspace, Git history, and `coverage_manifest.csv` confirmed zero existing records matching `arXiv:2603.19288`, author `Keonvin Park`, email `kbpark16@snu.ac.kr`, or the exact title phrase "Joint Return and Risk Modeling with Deep Neural Networks for Portfolio Construction".

## Economic mechanism

### Source-reported

The author argues that classical portfolio optimization is grounded in the mean-variance framework of Markowitz (1952), but practical implementation suffers from estimation instability. Small estimation errors in expected return vectors lead to volatile weights, while sample covariance matrices suffer from noise amplification.

Financial time series exhibit well-documented empirical phenomena: volatility clustering, conditional heteroskedasticity, nonlinear cross-asset dependencies, and structural regime shifts. While traditional econometric models (e.g., GARCH) account for time-varying volatility, they rely on rigid parametric assumptions. Most deep learning applications in finance focus exclusively on forecasting expected returns, decoupling return forecasting from risk estimation, which is then delegated to static historical covariance matrices.

The author posits that decoupling return and risk modeling produces suboptimal and fragile portfolio allocations during volatile market regimes. The paper proposes an end-to-end framework where a multivariate Long Short-Term Memory (LSTM) network extracts latent temporal and cross-asset representations from sequential financial data, enabling simultaneous generation of forward-looking expected returns and dynamic covariance structures for Sharpe-ratio-based portfolio optimization.

### Research interpretation

The falsifiable alpha hypothesis is: **a multivariate neural network that jointly extracts forward-looking return forecasts and time-varying risk structures from sequential price data can produce higher risk-adjusted returns (Sharpe ratio) than decoupling return prediction from historical sample covariance matrices, because the latent representation encodes volatility clustering and cross-asset regime transitions**.

Component roles:
- **Latent Representation Extractor:** Multivariate LSTM processing rolling historical return windows across assets to capture nonlinear temporal dependencies and cross-sectional interactions.
- **Return Prediction Head:** Linear projection layer from LSTM latent state to asset expected returns, trained via mean squared error.
- **Dynamic Risk Estimator:** Model-implied dynamic volatility and cross-asset covariance matrix estimated from the learned representation and predicted returns.
- **Portfolio Construction / Allocation Module:** Numerical solver (Sequential Quadratic Programming) finding long-only portfolio weights that maximize the portfolio Sharpe ratio subject to full investment constraints.

## Signal

The normalized mathematical specification from Sections 3.1–3.5 of arXiv:2603.19288v1 is:

1. **Input Definition:**
   Let $r_t \in \mathbb{R}^N$ denote the vector of daily log returns for $N$ assets at time $t$:
   $$r_t = \log\left(\frac{P_t}{P_{t-1}}\right)$$
   For each trading day $t$, an observation window of length $L$ is constructed:
   $$X_t = \{r_{t-L}, \dots, r_{t-1}\} \in \mathbb{R}^{L \times N}$$
   *(Note: The exact integer value of $L$ is `underspecified` in the paper text; Figure 6 illustrates a 30-day window, so $L=30$ is `research-proposed` for baseline replication).*

2. **Multivariate Temporal Representation:**
   The input window $X_t$ is passed through a multivariate LSTM network:
   $$h_t = \text{LSTM}(X_t)$$
   where $h_t \in \mathbb{R}^d$ is the latent representation summarizing cross-asset and temporal information within the window. *(The hidden dimension $d$, number of layers, dropout rate, and training optimizer parameters are omitted in source and are `underspecified`; $d=64$, 1 layer, Adam optimizer are `research-proposed`).*

3. **Expected Return Forecast:**
   Expected return vector $\hat{\mu}_t \in \mathbb{R}^N$ is obtained via a linear projection layer:
   $$\hat{\mu}_t = W_\mu h_t + b_\mu$$
   Parameters are trained by minimizing the mean squared error over the training period:
   $$L_{\text{return}} = \frac{1}{N} \|r_t - \hat{\mu}_t\|^2$$

4. **Dynamic Risk Estimation:**
   In Section 3.3, asset-level volatility is computed over the rolling observation window:
   $$\hat{\sigma}_{t,i} = \sqrt{\frac{1}{L} \sum_{k=t-L}^{t-1} (r_{k,i} - \bar{r}_i)^2}$$
   Cross-asset covariance is derived from predicted returns:
   $$\hat{\Sigma}_t = \text{Cov}(\hat{\mu}_t)$$
   *(In Algorithm 1 lines 5–6, these are generalized as $\hat{\sigma}_t = f_\sigma(h_t)$ and $\hat{\Sigma}_t = f_\Sigma(h_t)$. The exact function form of $f_\Sigma$ versus rolling sample covariance of $\hat{\mu}_t$ is `underspecified`).*

5. **Sharpe Ratio-Based Portfolio Optimization:**
   Given $\hat{\mu}_t$ and $\hat{\Sigma}_t$, portfolio weights $w_t \in \mathbb{R}^N$ are determined by solving:
   $$\max_{w_t} \frac{w_t^\top \hat{\mu}_t}{\sqrt{w_t^\top \hat{\Sigma}_t w_t}}$$
   subject to:
   $$\sum_{i=1}^N w_{t,i} = 1, \quad w_{t,i} \ge 0 \quad \forall i \in \{1, \dots, N\}$$
   The optimization problem is solved using Sequential Quadratic Programming (SQP).

6. **Operational Execution Rules:**
   - **Direction:** Long-only ($w_{t,i} \ge 0$). No short sales or leverage allowed ($\sum w_{t,i} = 1$).
   - **Rebalance Frequency:** Daily (each time step $t$ in test set).
   - **Execution Timestamp:** `underspecified` by source; same-close execution is implicit in the paper's backtest, but next-bar open fill (MOO) is `research-proposed` for implementability.

## Required data

- **Universe:** 10 large-cap US equities spanning multiple sectors: AAPL, MSFT, GOOGL, AMZN, TSLA, NVDA, META, JPM, V, UNH (`source-reported`).
- **Data Vendor / Source:** Yahoo Finance (`source-reported`).
- **Fields:** Daily adjusted closing prices ($P_t$), used to compute daily log returns $r_t = \log(P_t / P_{t-1})$.
- **Timeframe:** Daily bars (`source-reported`).
- **Sample Period:** January 2010 to January 2024 (14 calendar years):
  - **Training Period:** 2010 to 2019 (10 years) (`source-reported`).
  - **Test Period (Out-of-Sample):** 2020 to 2024 (4 years) (`source-reported`).
- **Data Hygiene and Quality Gaps:**
  - **Survivorship Bias:** The 10 assets were selected as mega-cap winners of the 2010–2024 period with full history. No point-in-time constituent reconstitution is performed (`data gap`).
  - **Lookahead / Publication Timing:** Use of adjusted closing prices introduces retroactive dividend and split adjustments (`data gap`).

## Execution assumptions

- **Fill Model:** Immediate execution at daily closing prices with zero latency (`source-reported` implicit simulation). Next-day open fill is `research-proposed` for causal live testing.
- **Transaction Costs:** 0.0 basis points (`source-reported`). Section 5 explicitly notes that transaction costs are omitted and deferred to future work.
- **Slippage / Bid-Ask Spread:** 0.0 basis points (`omitted by source`, `data gap`).
- **Borrow / Shorting Fees:** 0.0 bps (not applicable due to long-only constraint $w_{t,i} \ge 0$).
- **Market Impact / Participation Cap:** Not modeled (`data gap`).
- **Leverage:** 1.0x (unlevered, fully invested).
- **Execution Frictions Status:** The source empirical performance is strictly gross of all trading frictions.

## Evidence

### Source-reported

All figures below are transcribed directly from Keonvin Park (arXiv:2603.19288v1, Sections 2.1–2.3, Tables 1–3, Figures 1–2):

1. **Table 1: Return Prediction Performance (Out-of-Sample Test Period 2020–2024):**
   - Model: Deep Forecasting Model (Multivariate LSTM)
   - RMSE: 0.0264
   - MAE: 0.0177
   - Directional Accuracy: 0.5192 (51.92%)

2. **Table 2: Portfolio Performance Comparison (Out-of-Sample Test Period 2020–2024, Gross):**
   - **Equal Weight (EW):**
     - Annual Return: 0.2332 (23.32%)
     - Sharpe Ratio: 0.7756
   - **Historical Mean-Variance (Historical MV):**
     - Annual Return: 0.2062 (20.62%)
     - Sharpe Ratio: 0.7474
   - **Neural Portfolio (Proposed):**
     - Annual Return: 0.3641 (36.41%)
     - Sharpe Ratio: 0.9125

3. **Table 3: Summary Statistics of Daily Log Returns (Full Sample 2010–2024):**
   - AAPL: Mean = 0.000850, Std = 0.017921
   - AMZN: Mean = 0.000908, Std = 0.020331
   - GOOGL: Mean = 0.000763, Std = 0.017033
   - JPM: Mean = 0.000667, Std = 0.016563
   - META: Mean = 0.000762, Std = 0.025337
   - MSFT: Mean = 0.000948, Std = 0.016752
   - NVDA: Mean = 0.001775, Std = 0.027607
   - TSLA: Mean = 0.001679, Std = 0.035440
   - UNH: Mean = 0.000841, Std = 0.015653
   - V: Mean = 0.000789, Std = 0.015266

4. **Visual Findings:**
   - Figure 1: Compares predicted volatility against realized rolling volatility, reporting that the model captures volatility clustering and major regime transitions during the 2020–2024 test period.
   - Figure 2: Displays cumulative portfolio returns during 2020–2024, showing consistent wealth trajectory outperformance of the Neural Portfolio over Equal Weight and Historical MV.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Zero Transaction Cost Vulnerability:** The entire empirical evaluation assumes 0 bps fees and 0 bps slippage. Daily rebalancing across 10 volatile growth stocks (especially NVDA, TSLA, and META) incurs substantial turnover. If daily one-way turnover averages 15%–30%, a realistic round-trip fee and slippage hurdle of 5–10 bps represents an annual drag of 3.8%–7.5%, which would compress the Neural Portfolio's Sharpe ratio from 0.9125 down toward or below the passive Equal Weight benchmark (0.7756).
2. **Severe Survivorship and Selection Bias:** The asset universe is restricted to 10 mega-cap US technology and financial winners of the 2010–2024 decade. High performers like NVDA (daily mean +0.001775, ~45% annual) and TSLA (daily mean +0.001679, ~42% annual) dominate portfolio returns. Backtesting on an ex-post curated universe of secular winners inflates returns and does not test whether the model can avoid losers or navigate broad market constituents.
3. **Marginal Directional Accuracy Edge:** The reported directional accuracy of 51.92% (Table 1) is only 1.92 percentage points above an uninformative 50% coin flip. No statistical significance test (e.g., Diebold-Mariano test, t-statistic, or p-value) is provided to establish whether this forecast edge is statistically distinguishable from noise.
4. **Underspecified Model Hyperparameters:** The author omits the exact lookback window length $L$, LSTM hidden layer size $d$, number of LSTM layers, dropout, batch size, learning rate, and training epochs. The results cannot be deterministically replicated without guessing hyperparameters.
5. **Ambiguity in Covariance Estimation:** In Section 3.3, covariance is written as $\hat{\Sigma}_t = \text{Cov}(\hat{\mu}_t)$, while in Algorithm 1 it is written as $\hat{\Sigma}_t = f_\Sigma(h_t)$. How sample covariance of a single daily forecast vector is estimated without an explicit rolling sample of predictions or a parameterised neural covariance head is unspecified.
6. **Absence of Risk and Turnover Metrics:** Table 2 omits maximum drawdown, Sortino ratio, Calmar ratio, portfolio turnover, Value-at-Risk (VaR), and factor attribution (beta, size, momentum exposure).
7. **No Code Availability:** Neither code nor training checkpoints are publicly released.

## Falsification plan

All quantitative cutoffs below are **research-defined falsification thresholds**; operational rules required to resolve source ambiguities are labeled **research-proposed**:

1. **Transaction Cost Ladder Test:**
   - *Test:* Re-run the daily rebalanced SQP portfolio under a realistic execution cost ladder: 0 bps, 2.5 bps, 5 bps, 10 bps, and 15 bps per trade (one-way fee + slippage).
   - *Research-defined falsification threshold:* If net Sharpe ratio drops below the passive Equal Weight Sharpe (0.7756) at or before 5 bps per trade, or if annualized turnover exceeds 250% without corresponding risk-adjusted compensation, reject the strategy as an artifact of frictionless execution.
2. **Point-in-Time S&P 500 Broad Universe Test:**
   - *Test:* Expand the asset universe from the 10 curated mega-cap winners to a survivorship-bias-free, point-in-time universe (e.g., S&P 100 or S&P 500 constituents rebalanced annually).
   - *Research-defined falsification threshold:* If the Neural Portfolio Sharpe fails to exceed the broad market cap-weighted benchmark (SPY) or Equal Weight benchmark by at least 0.15 Sharpe out-of-sample, reject the claim of generalizable joint return-risk modeling.
3. **Execution Timing / Next-Open Fill Audit:**
   - *Test:* Compare same-day close execution (assumed by the paper) against a causal next-bar open fill (MOO) using prices $P_{t+1}^{\text{open}}$.
   - *Research-proposed operational rule:* Generate signals using data available up to time $t$ close; submit MOO orders for execution at $t+1$ market open.
   - *Research-defined falsification threshold:* If Sharpe drops by > 0.20 or annualized return decreases by > 8 percentage points under next-open execution, reject the reported performance as lookahead-dependent.
4. **Temporal Order Placebo Test:**
   - *Test:* Randomly permute the chronological order of daily returns in $X_t$ while preserving the cross-sectional correlation structure.
   - *Research-defined falsification threshold:* If the trained LSTM on time-shuffled data achieves comparable return forecasting accuracy (RMSE within 5% of 0.0264) and portfolio Sharpe (> 0.85), falsify the claim that the model learns sequential temporal dynamics rather than unconditional asset covariance.
5. **Linear / Econometric Baseline Ablation:**
   - *Test:* Replace the multivariate LSTM with classical baselines: (a) rolling Vector Autoregression (VAR(1)), (b) rolling ridge regression with DCC-GARCH covariance, and (c) static 60-day rolling mean-variance.
   - *Research-defined falsification threshold:* If the Neural Portfolio does not produce a statistically significant improvement in out-of-sample Sharpe ratio (Diebold-Mariano test p-value < 0.05) over the regularized linear/GARCH baseline, reject the deep neural network architecture as unnecessary parameter complexity.
6. **Subperiod and Regime Stability Audit:**
   - *Test:* Segment the 2020–2024 test period into distinct regimes: (a) Covid crash/rebound (2020), (b) Tech bull market (2021), (c) Rate hike selloff (2022), and (d) AI expansion (2023–2024).
   - *Research-defined falsification threshold:* If the strategy exhibits negative excess return or Sharpe < 0 in more than one distinct sub-regime (specifically 2022 bear market), reject the claim of robust regime adaptability.

## Crypto portability

- **Portability Classification:** **adapted / unproven**
- **Porting Rationale:** The primary source investigates only 10 large-cap US equities on daily closing data. The mechanism is not evaluated or demonstrated in cryptocurrency markets by the author.
- **Crypto-Specific Market Microstructure Adaptations:**
  - *24/7 Session Boundaries:* Crypto markets trade continuously without an official closing auction. A daily bar convention must be declared (`research-proposed: 00:00:00 UTC cutoff`).
  - *Perpetual Futures and Funding Rates:* In crypto perpetual contracts, 8-hour funding rates represent a primary cost/carry component. Holding long positions in high-beta altcoins during bullish regimes can incur annualized funding costs of 10%–50%, which would materially degrade gross portfolio Sharpe.
  - *Extreme Volatility and Tail Spikes:* Crypto cross-asset correlations frequently spike to > 0.85 during liquidation cascades. An unconstrained Sharpe maximization model trained on equity data could concentrate capital in high-volatility tokens right before cascade events.
  - *Universe Selection:* A crypto adaptation would require evaluating a liquid basket (e.g., top 10 market cap perpetual contracts on Binance or Bybit, such as BTC, ETH, SOL, BNB, XRP, ADA, DOGE, AVAX, LINK, LTC), incorporating taker execution fees (4–5 bps) and funding payments.

## Limitations

- **underspecified:** Lookback window length $L$, LSTM hidden dimension $d$, number of layers, training learning rate, batch size, epoch budget, early stopping criterion, and the exact algebra of the covariance estimator $\hat{\Sigma}_t$ are not specified in the text.
- **data gap:** 0.0 bps transaction fees, 0.0 bps slippage, 0.0 bps borrow/financing costs, and zero market impact assumptions. No maximum drawdown, turnover, or tail risk metrics are reported. No code or data files are made publicly available.
- **selection bias:** Test universe is limited to 10 ex-post mega-cap technology and finance winners over 2010–2024.
- **not independently reproduced:** The empirical figures are strictly source-reported and have not been replicated in our research environment.
- **unproven:** Deployable alpha after realistic transaction costs, execution lag, and out-of-sample forward walk is unproven.

## Implementation status

- `not-implemented`: This artifact is a research capture only.
- No algorithmic implementation has been added to the production stack or execution engines.
- No Qlib full backtest, candidate pool entry, paper trading, testnet, or live trading execution has occurred or been authorized.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`
- Presence of this record in the repository indicates solely that the external paper has been cataloged and normalized according to the canonical strategy-research specification. It does not indicate profitability, passing Research Intake Review, entry into Hermes Wiki Brain, promotion to the production candidate pool, or authorization for live or testnet capital allocation.

## Related Wiki records

- `[[quant/spatio-temporal-momentum-multitask-shrinkage-turnover-regularization-2026-09-06]]` — Related multi-asset neural prediction with turnover and shrinkage constraints.
- `[[quant/china-ashare-mask-first-upstream-contamination-adjusted-mse-2026-09-04]]` — Cross-sectional portfolio optimization using machine learning with bias-adjusted loss functions.
- `[[quant/functionally-generated-portfolio-diversity-entropy-smallcap-stochastic-cost-2026-09-22]]` — Non-parametric equity portfolio construction with explicit stochastic transaction cost bounds.
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Methodological standard for evaluating walk-forward validation and avoiding leakage in sequential neural network backtests.

## Sources

- **Primary Paper:** Keonvin Park, *"Joint Return and Risk Modeling with Deep Neural Networks for Portfolio Construction"*, arXiv preprint `arXiv:2603.19288v1 [q-fin.PM, cs.AI, cs.LG]`, submitted March 9, 2026 (2026-03-09T01:49:51Z).
  - arXiv Abstract: https://arxiv.org/abs/2603.19288
  - Full Text HTML: https://arxiv.org/html/2603.19288v1
  - Full Text PDF: https://arxiv.org/pdf/2603.19288v1 (SHA-256 `f1f7f3c0ec3365083d421ffcbec7f21f8335f2d35a5e734f2b4ee9c549a4e14c`)
  - DOI: https://doi.org/10.48550/arXiv.2603.19288
