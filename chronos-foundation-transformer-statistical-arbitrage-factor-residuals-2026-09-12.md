---
schema: strategy-research-record-v1
title: "Large Language Models for Time Series: Statistical Arbitrage on Factor Residuals with Foundation Transformers and Turnover-Cost Fragility"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - foundation-models
  - time-series-transformers
  - chronos
  - factor-residuals
  - turnover-cost-drag
  - equity-cross-section
  - zero-shot
  - fine-tuning
status: research-only
confidence: high
source_as_of: 2025-11-03
sources:
  - "Sebastien Valeyre and Sofiane Aboura, 'Large Language Models for Time Series: an Application for Single Stocks and Statistical Arbitrage', arXiv:2412.09394v2 [q-fin.PM], submitted December 12, 2024, revised November 3, 2025. Stable URLs: https://arxiv.org/abs/2412.09394, https://arxiv.org/html/2412.09394v2, https://arxiv.org/pdf/2412.09394v2; Primary Data: CRSP US Equity Factor Residuals (1978-2016) by Guijarro-Ordonez et al. (2021) at https://github.com/gregzanotti/dlsa-public/tree/main/residuals; Chronos Pipeline: https://github.com/amazon-science/chronos-forecasting"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Large Language Models for Time Series: Statistical Arbitrage on Factor Residuals with Foundation Transformers and Turnover-Cost Fragility

## Provenance

- **Primary Source:** Working research paper released on arXiv (`arXiv:2412.09394v2 [q-fin.PM]`, version 2 revised November 3, 2025; original submission December 12, 2024).
- **Authors:** Sebastien Valeyre (Machina Capital, Paris, France; Valeyre Research, Cannes, France) and Sofiane Aboura (University of Paris XIII – Sorbonne Paris Nord, Villetaneuse, France).
- **Persistent Identifiers & Public URLs:**
  - arXiv Abstract: `https://arxiv.org/abs/2412.09394` (`arXiv:2412.09394v2 [q-fin.PM]`)
  - Full-Text HTML: `https://arxiv.org/html/2412.09394v2`
  - Full-Text PDF: `https://arxiv.org/pdf/2412.09394v2`
  - License: Creative Commons Public Domain Dedication (CC0 1.0 Universal)
- **Primary Data Source:** Daily residual return series constructed by Guijarro-Ordonez, Pelger, and Zanotti (2021, "Deep Learning Statistical Arbitrage", JFE/arXiv:2106.00312) from the CRSP US equity universe (January 1978 – December 2016), hosted publicly on GitHub at `https://github.com/gregzanotti/dlsa-public/tree/main/residuals`.
- **Pretrained Foundation Model:** Amazon Chronos (`amazon/chronos-t5-tiny`, 11M parameters; Ansari et al., 2024, arXiv:2403.07815), open-sourced at `https://github.com/amazon-science/chronos-forecasting`.
- **Repository Deduplication Audit:** Systematic repository-wide audit of all strategy research records in `alpha-strategy-research` confirmed zero matching records for `arXiv:2412.09394`, Sebastien Valeyre, Sofiane Aboura, Amazon Chronos foundation time-series models, or the `dlsa-public` factor residual datasets. Adjacent repository captures (`ordinal-gates-cardinal-bets-llm-confidence-exposure-coupling-2026-09-05.md`, `statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05.md`, `statistical-arbitrage-rank-space-cnn-transformer-hybrid-atlas-2026-09-02.md`) address fundamentally distinct mechanisms (text-prompt LLM confidence calibration, LSTM factor replication with OU stopping, and specialized ATLAS CNN-Transformers), establishing complete independent provenance.

## Economic mechanism

### Source-reported

1. **Idiosyncratic Mispricing in Factor Residuals:**
   Standard asset pricing models assume that cross-sectional stock returns are driven by a small set of systematic risk factors (e.g., Fama-French 5-factor, PCA, or Instrumented PCA), with the remaining residual component representing idiosyncratic variation. While theoretical asset pricing treats these residuals as white noise, empirical market microstructure and institutional limits to arbitrage create short-lived pricing inefficiencies and localized lead-lag auto-correlations within factor residuals. Statistical arbitrage aims to harvest these temporary deviations by going long underpriced residuals and short overpriced residuals in a dollar-neutral portfolio.

2. **Cross-Domain Time-Series Foundation Models as Alpha Extractors:**
   A common belief in financial econometrics is that large language models and generalist time-series foundation models (such as Chronos, built on the T5 transformer architecture) cannot predict financial market returns because financial series possess low signal-to-noise ratios, non-stationarity, and near-martingale dynamics. The paper challenges this assumption by demonstrating that a 11-million parameter pretrained transformer (`chronos-t5-tiny`), trained exclusively on non-financial synthetic and cross-domain time series, successfully extracts predictive structure from financial factor residuals without overfitting.

3. **Autoregressive Memory vs. Direct Reversal:**
   The paper shows that feeding raw residual returns directly into Chronos ($\alpha=0$) yields minimal zero-shot predictability (gross Sharpe $0.04$ on PCA residuals). However, pre-filtering residuals via an exponential moving average (EMA) autoregressive transform with parameter $\alpha \in [0.2, 0.4]$ enables the foundation transformer to capture multi-scale persistence and reversal, generating out-of-sample gross Sharpe ratios between $2.75$ and $3.25$ on PCA residuals.

4. **Turnover-Cost Drag and Algorithmic Fragility:**
   Crucially, the authors report that despite high gross statistical Sharpe ratios ($3.17$ with a t-statistic of $12.27$ over 15 years for PCA), the strategy exhibits extreme turnover sensitivity: incorporating a realistic 3 basis point (0.03%) trading friction per trade (2–3 bps market impact + 1 bp broker commission) flips the net Sharpe ratio from $+3.17$ to **$-1.49$**. Thus, while foundation models demonstrate genuine mathematical pattern recognition on financial residuals, naive daily portfolio rebalancing on high-dimensional single stocks creates prohibitive turnover drag.

5. **Catastrophic Forgetting in Continual Online Fine-Tuning:**
   When Chronos is fine-tuned daily on rolling 100-day windows, performance is acutely sensitive to the training iteration parameter $\tau$. While moderate updates ($\tau=15$) increase the gross Sharpe ratio from $2.75$ to $3.97$ on PCA, excessive training steps ($\tau=40$) degrade the Sharpe ratio to $3.80$. Over a 15-year simulation, daily continual updates cause the model to gradually lose its pretrained generalist representations, particularly post-2008 where performance flattens.

### Research interpretation

- **Microstructure Basis of Factor-Residual Predictability:**
  Idiosyncratic returns derived from linear factor models (PCA, IPCA, FF5) reflect unmodeled inventory imbalances, liquidity shocks, and institutional block execution. When large institutional investors execute multi-day VWAP/TWAP parent orders, temporary price pressure displaces the stock relative to its factor peer group. The resulting residual mean-reversion is real in gross prices, but its execution is intensely competed over by high-frequency statistical arbitrageurs.
- **Why Foundation Models Mirror Short-Term Reversal (STR):**
  Empirical benchmarking reveals that Chronos forecasts correlate moderately with simple Short-Term Reversal (STR) baselines ($\beta \in [0.2, 0.3]$). The foundation transformer essentially acts as a non-linear, state-dependent filter over recent trailing returns, identifying subtle deviations from pure geometric decay. However, specialized linear and shallow CNN models (such as Guijarro-Ordonez et al.'s 169-parameter CNN-Transformer) outperform the 11M-parameter foundation model ($5.01$ vs. $4.21$ Sharpe), proving that massive parameter capacity offers no structural advantage over compact inductive biases in noisy financial environments.
- **The Execution Drag Barrier:**
  The collapse of net Sharpe from $+3.17$ to $-1.49$ under 3 bps cost illustrates the classic statistical arbitrage fallacy: extracting predictable mean-reversion at daily frequencies across hundreds of liquid equities requires substantial daily portfolio churn (re-ranking the entire cross-section). Unless paired with execution-aware turnover regularization, latency-reducing order types, or liquidity-providing maker execution, daily foundation-model signals remain untradable paper alphas.

## Signal

The strategy signal pipeline consists of four mathematical stages (`source-reported`):

```text
[Stage 1: Factor Residual Extraction (Guijarro-Ordonez et al. 2021)]
  - Raw stock returns r_{d,i} decomposed into K=5 systematic factors and residual return r_{d,i}
  - Specifications: IPCA (240m rolling), PCA (252d rolling), or FF 5-factor (60d rolling)
             ↓
[Stage 2: Autoregressive Smoothing Transform (Equation 1)]
  - hat{r}_{d+1,i} = alpha * hat{r}_{d,i} + r_{d+1,i}, with alpha in {0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.8}
             ↓
[Stage 3: Foundation Model Inference (Equations 2 & 3)]
  - Chronos-T5-tiny context: previous 100 days (tau_ctx = 100)
  - hat{chi}_{d,i} = E[chi(hat{r}_{d+1,i} | hat{r}_{d,i} ... hat{r}_{d-99,i})]
  - Demeaned residual forecast: tilde{chi}_{d,i} = hat{chi}_{d,i} - alpha * hat{r}_{d,i}
             ↓
[Stage 4: Cross-Sectional Ranking & Exposure Construction (Equations 4 - 7)]
  - Centered rank: omega_d^chi = ArgSort(ArgSort(tilde{chi}_d)) - N / 2
  - Resized volatility control: [omega_d^chi]^r = omega_d^chi * Median(sigma) / max(sigma_i, Median(sigma))
  - Normalization: hat{omega}_{d,i} = omega_{d,i} / sum_j |omega_{d,j}| (Gross leverage = 1.0, dollar-neutral)
```

### 1. Mathematical Formulation

- **Residual Return Input:** Let $r_{d,i}$ denote the daily factor residual return of stock $i \in \{1, \dots, N\}$ on day $d$ (`source-reported`).
- **Autoregressive Smoothing Transform (Equation 1):**
  $$\hat{r}_{d+1,i} = \alpha \hat{r}_{d,i} + r_{d+1,i}$$
  where $\alpha \in [0, 0.8]$ is the autoregressive coefficient governing the exponential decay of past residuals (`source-reported`).
- **Chronos Model Prediction (Equation 2):**
  $$\hat{\chi}_{d,i} = \mathbf{E}\left[\chi\left(\hat{r}_{d+1,i} \mid \hat{r}_{d,i}, \dots, \hat{r}_{d-99,i}\right)\right]$$
  where $\chi$ represents the Chronos probabilistic forecasting pipeline conditioning on the trailing 100-day smoothed history (`source-reported`). The expected value is estimated empirically via 20 stochastic samples (`num_samples = 20`) generated with `temperature = 1.0`, `top_k = 50`, `top_p = 1.0` (`source-reported`).
- **Demeaned Residual Forecast (Equation 3):**
  $$\tilde{\chi}_{d,i} = \hat{\chi}_{d,i} - \alpha \hat{r}_{d,i}$$
  isolating the pure incremental forward residual return expectation for day $d+1$ (`source-reported`).
- **Cross-Sectional Rank-Distance Sizing (Equation 4):**
  $$\omega_d^\chi = \Re\left[\Re\left(\tilde{\chi}_d\right)\right] - \frac{N}{2}$$
  where $\Re = \text{ArgSort}$. Applying $\text{ArgSort}$ twice assigns each stock its integer rank position from $1$ to $N$, and subtracting the median rank $\frac{N}{2}$ yields a zero-sum, symmetric long/short rank-distance profile (`source-reported`). Following Valeyre (2019), linear rank-distance weighting achieves optimal mathematical diversification across the entire cross-section compared to extreme quantile sorting (`source-reported`).
- **Volatility-Managed Resizing (Equation 5):**
  $$\left[\omega_d^\chi\right]^r = \left(\Re\left[\Re\left(\tilde{\chi}_d\right)\right] - \frac{N}{2}\right) \frac{\mathbf{M}\left(\sigma_0, \dots, \sigma_N\right)}{\max\left(\sigma_i, \mathbf{M}\left(\sigma_0, \dots, \sigma_N\right)\right)}$$
  where $\sigma_i$ is the trailing 100-day sample standard deviation of daily returns for stock $i$, and $\mathbf{M}(\cdot)$ represents the cross-sectional median standard deviation (`source-reported`). This adjustment down-weights highly volatile stocks to prevent tail-risk concentration (`source-reported`).
- **Gross Leverage Normalization (Equations 6 & 7):**
  $$\hat{\omega}_{d,i}^\chi = \frac{\omega_{d,i}^\chi}{\sum_j \left|\omega_{d,j}^\chi\right|}, \quad \left[\hat{\omega}_{d,i}^\chi\right]^r = \frac{\left[\omega_{d,i}^\chi\right]^r}{\sum_j \left|\left[\omega_{d,i}^\chi\right]^r\right|}$$
  ensuring that the portfolio is strictly dollar-neutral ($\sum_i \hat{\omega}_{d,i} = 0$), $50\%$ long, $50\%$ short, with total gross leverage equal to $1.0$ (`source-reported`).
- **Daily Portfolio Return (Equations 8 & 9):**
  $$\mathcal{P}_{d+1} = \sum_i \hat{\omega}_{d,i}^\chi \times r_{d+1,i}, \quad \left[\mathcal{P}_{d+1}\right] = \sum_i \left[\hat{\omega}_{d,i}^\chi\right]^r \times r_{d+1,i}$$
  evaluated out-of-sample across 2002–2016 (`source-reported`).

### 2. Fine-Tuning Specification

- **Base Architecture:** `amazon/chronos-t5-tiny` (11M parameters, based on `google/t5-efficient-tiny`, vocabulary size 4096, sequence-to-sequence structure) (`source-reported`).
- **Tokenizer:** `MeanScaleUniformBins` with `low_limit = -15.0`, `high_limit = 15.0`, 4096 bins, 2 special tokens (`source-reported`).
- **Optimization:** AdamW Torch Fused optimizer (`source-reported`).
- **Daily Retraining Cadence:** Every day $d$, the model weights from day $d-1$ are updated on 10 random subgroups of the stock universe using the previous 100 days of residual returns, running $\tau \in \{5, 15, 40\}$ gradient steps (`source-reported`).

### 3. Operational Classification Table

| Field | Value / Rule | Status |
| :--- | :--- | :--- |
| Factor Models | IPCA (240m), PCA (252d), FF 5-factor (60d); $K=5$ factors | `source-reported` |
| Autoregressive parameter $\alpha$ | $\alpha \in \{0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.8\}$; optimal $\alpha = 0.3$ | `source-reported` |
| Lookback context window | Trailing 100 days ($\tau_{\text{ctx}} = 100$) | `source-reported` |
| Chronos Model Size | `chronos-t5-tiny` (11M parameters, T5-efficient-tiny) | `source-reported` |
| Chronos Sampling | `num_samples = 20`, `temperature = 1.0`, `top_k = 50`, `top_p = 1.0` | `source-reported` |
| Sizing Rule | Double-ArgSort rank centering ($-\frac{N}{2}$) with median-volatility cap | `source-reported` |
| Leverage & Dollar Neutrality | Gross exposure $= 1.0$; $50\%$ long, $50\%$ short; $\sum \omega_i = 0$ | `source-reported` |
| Rebalancing Frequency | Daily at market close | `source-reported` |
| Rebalance Execution Timing | Filled at day $d+1$ open or close (exact minute unmodeled) | `research-proposed` |
| Borrow / Shorting Rate | Zero borrow fee modeled in paper | `research-proposed` |
| Cost Stress Hurdle | 3 basis points per trade (2-3 bps impact + 1 bp broker fee) | `source-reported` |

## Required data

- **Instrument / Universe:** Largest single US common stocks from CRSP (1978–2016), filtered by liquidity and data completeness by Guijarro-Ordonez et al. (2021) (`source-reported`).
- **Venue:** US Equity Exchanges (NYSE, NASDAQ, AMEX) (`source-reported`).
- **Market Type:** Cash equities (long/short common stock) (`source-reported`).
- **Timeframe:** Daily close-to-close returns (`source-reported`).
- **Required Fields:** Daily close prices, adjusted returns, factor returns, and residual returns across IPCA, PCA, and FF5 models (`source-reported`).
- **Point-in-Time Integrity:**
  - Factors and residuals are extracted using strictly backward-looking rolling windows (240 months for IPCA, 252 days for PCA, 60 days for FF5) (`source-reported`).
  - Chronos models condition exclusively on data available up to day $d$ when generating the forecast for day $d+1$ (`source-reported`).
- **Missing-Data Assumptions:** Handled upstream by Guijarro-Ordonez et al. (2021); stocks with missing or stale quotes within the rolling lookback window are excluded from that day's cross-section (`source-reported`).
- **Cost & Fee Assumptions:** The baseline paper reports gross returns; footnote 3 models a 3 bps total transaction cost per trade (1 bp commission + 2–3 bps market impact) (`source-reported`). Borrow fees for short positions are omitted in the original paper (`research-proposed`).

## Execution assumptions

- **Order Execution:** Market-on-Close (MOC) or Market-on-Open (MOO) next-day fills without intraday execution simulation (`research-proposed`).
- **Fill Model:** Full execution at recorded daily prices without execution delay or order book queues (`research-proposed`).
- **Gross Leverage:** Exactly 1.0x (100% long, 100% short notional normalized to equity) (`source-reported`).
- **Turnover Drag:** High daily turnover resulting from full cross-sectional re-ranking of hundreds of stocks (`source-reported`).
- **Borrow & Shorting:** Perfect short-sale availability with zero hard-to-borrow fees or borrow recalls (`research-proposed`).
- **Capacity & Market Impact:** In small accounts, linear cost models apply; institutional capacity is severely constrained by market impact on high-turnover single-stock rebalancing (`source-reported`).

## Evidence

### Source-reported

1. **Residual Return Summary Statistics (CRSP 1978–2016, Table 1):**

| Factor Model | Rolling Lookback | Daily Residual Mean | Daily Residual SD |
| :--- | :--- | :--- | :--- |
| **IPCA** | 240 months | $4.35 \times 10^{-6}$ | $0.0066$ ($0.66\%$) |
| **PCA** | 252 days | $2.31 \times 10^{-6}$ | $0.0059$ ($0.59\%$) |
| **FF 5-Factor** | 60 days | $2.95 \times 10^{-6}$ | $0.0068$ ($0.68\%$) |

2. **Gross Sharpe Ratios of Zero-Shot Pretrained Chronos (2002–2016 Out-of-Sample, Table 2):**
   Evaluated with volatility-managed resizing across different autoregressive parameter values $\alpha$:

| $\alpha$ Parameter | Fama-French (FF) | PCA | IPCA |
| :--- | :--- | :--- | :--- |
| $\alpha = 0.0$ | $0.07$ | $0.04$ | $-0.47$ |
| $\alpha = 0.1$ | $1.27$ | $2.08$ | $0.68$ |
| $\alpha = 0.2$ | $1.80$ | $2.75$ | $1.19$ |
| **$\alpha = 0.3$** | **$1.84$** | **$3.17$** ($t = 12.27$) | **$1.34$** |
| $\alpha = 0.4$ | $1.39$ | **$3.25$** | **$1.42$** |
| $\alpha = 0.5$ | $1.39$ | $2.71$ | $1.18$ |
| $\alpha = 0.8$ | $-0.24$ | $0.07$ | $-0.81$ |

   *Observation:* Raw residual input ($\alpha=0$) fails completely (Sharpe $0.04$ on PCA, $-0.47$ on IPCA). Pre-smoothing residuals with $\alpha \in [0.2, 0.4]$ is essential to unlock the foundation model's pattern-recognition capability.

3. **Fine-Tuned Chronos vs. Specialized Benchmarks (2002–2016 Out-of-Sample, Table 3):**

| Strategy Configuration | FF Sharpe | PCA Sharpe | IPCA Sharpe | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Pretrained Chronos ($\alpha=0.2$) | $1.80$ | $2.75$ | $1.19$ | Zero-shot foundation model |
| Fine-tuned Chronos ($\alpha=0, \tau=15$) | — | $0.24$ ($t = 0.92$) | — | Daily retrained without EMA |
| Fine-tuned Chronos ($\alpha=0.3, \tau=5$) | $2.12$ | $3.90$ | $2.29$ | Light daily retraining |
| Fine-tuned Chronos ($\alpha=0.3, \tau=15$) | — | $3.97$ | — | Standard daily retraining |
| **Resized Fine-tuned Chronos ($\alpha=0.3, \tau=15$)** | — | **$4.21$** | — | With volatility-managed resizing |
| Fine-tuned Chronos ($\alpha=0.3, \tau=40$) | — | $3.80$ | — | Performance drops from over-updating |
| **CNN-Transformer Benchmark (Guijarro-Ordonez 2021)** | **$3.15$** | **$5.01$** | **$4.29$** | Specialized model (169 parameters) |
| Short-Term Reversal (STR, $\beta=0.2$) | $2.23$ | $4.16$ | $2.31$ | Simple heuristic benchmark |
| Short-Term Reversal (STR, $\beta=0.3$) | $2.16$ | $4.03$ | $2.31$ | Simple heuristic benchmark |
| **Resized STR ($\beta=0.3$)** | **$2.31$** | **$4.27$** | **$2.32$** | Resized simple heuristic |
| STR ($\beta=0.8$) | $1.24$ | $2.42$ | $1.76$ | Slower reversal heuristic |
| STR ($\beta=0.95$) | $0.98$ | $1.38$ | $1.20$ | Slower reversal heuristic |
| AutoARIMA Benchmark | $1.43$ | $2.10$ | $1.22$ | Standard ML baseline |

4. **Transaction Cost Collapse (Footnote 3):**
   - On the PCA dataset with $\alpha=0.3$, gross Sharpe is **$3.17$**.
   - With an applied trading cost of **3 basis points (0.03%)** per trade (typical 2–3 bps market impact for small orders plus 1 bp brokerage fee), the net Sharpe ratio collapses to **$-1.49$**.
   - The authors state explicitly: *"trading costs are prohibitive, as including a 3 basis point slippage cost per trade results in negative net Sharpe ratios... Currently, AI lacks the 'intelligence' to find opportunities that remain profitable when factoring in trading costs."*

5. **WeightWatcher Spectral Analysis (Appendix B.3):**
   Power-law exponents of layer-wise weight eigenvalue distributions were evaluated via WeightWatcher. For fine-tuned Chronos, power-law exponents strictly fell between $2.0$ and $6.0$, confirming that the model did not suffer from overt classical matrix overfitting ($\alpha < 2$) or underfitting ($\alpha > 6$).

### Independently reproduced

`Not independently reproduced.` All quantitative metrics, Sharpe ratios, t-statistics, and transaction-cost collapses cited above represent direct extractions from Valeyre & Aboura (arXiv:2412.09394v2, 2025). No internal replication in PyBroker or NautilusTrader has been conducted.

### Negative evidence

1. **Catastrophic Transaction Cost Sensitivity:**
   A minor transaction friction of 3 bps completely wipes out 15 years of gross alpha, turning a $3.17$ Sharpe into $-1.49$. High-dimensional cross-sectional statistical arbitrage strategies that rebalance daily without turnover penalties cannot survive institutional or retail execution friction.
2. **Structural Inferiority to Specialized Models:**
   An 11-million parameter foundation model (`chronos-t5-tiny`) underperforms a tiny 169-parameter specialized CNN-Transformer ($4.21$ vs. $5.01$ Sharpe on PCA) and barely matches a simple rule-based Short-Term Reversal heuristic ($4.21$ vs. $4.27$ Sharpe). Foundation scale provides no empirical advantage in low signal-to-noise financial time series.
3. **Catastrophic Forgetting & Degradation with Over-Tuning:**
   Increasing the daily training step parameter from $\tau=15$ to $\tau=40$ causes the Sharpe ratio to drop from $3.97$ to $3.80$, demonstrating that continuous online updating causes the model to overwrite its pretrained feature representations with recent financial noise.
4. **Post-2008 Regime Decay:**
   The strategy's cumulative PnL plateaued after 2008 (Figure 1), indicating that modern equity markets exhibit substantially reduced serial auto-correlation in factor residuals, eliminating the gross statistical arbitrage edge in recent market regimes.

## Falsification plan

The empirical hypothesis that foundation time-series transformers possess actionable statistical arbitrage alpha on factor residuals is subject to the following pre-declared falsification tests:

| Test Name | Sample / Regime | Evaluation Metric | Research-Defined Falsification Threshold | Action on Failure |
| :--- | :--- | :--- | :--- | :--- |
| **Transaction Cost & Slippage Stress Test** | 2002–2016 Out-of-sample | Net Annualized Sharpe Ratio | Net Sharpe $\le 0.0$ at realistic fee/slippage $\ge 2\text{ bps}$ per trade | Reject daily rebalanced signal as an unexecutable paper alpha |
| **Modern Regime Out-of-Sample Test** | 2017–2026 CRSP / US Equities | Gross & Net Sharpe Ratio, Max Drawdown | Gross Sharpe $< 1.0$ or Net Sharpe $< 0.0$ over 2017–2026 | Classify the underlying residual auto-correlation as structurally dead |
| **Foundation Pretraining Placebo Test** | 2002–2016 Out-of-sample | Paired Information Coefficient (IC) | $\Delta \text{IC} = \text{IC}_{\text{chronos}} - \text{IC}_{\text{random\_init}} \le 0$ ($p > 0.05$) | Reject claim that pretraining on non-financial time series provides inductive transfer |
| **Turnover-Constrained Optimization Test** | 2002–2016 Out-of-sample | Net Sharpe with L1 Turnover Penalty | Net Sharpe $< 1.0$ when daily portfolio turnover is constrained to $\le 10\%$ | Confirm that the alpha is strictly high-turnover noise capture |
| **STR Collinearity & Incremental Information Test** | 2002–2016 Out-of-sample | Orthogonalized Alpha Residual $t$-stat | $t(\alpha_{\text{orthog}}) < 2.0$ after controlling for linear STR ($\beta=0.3$) | Conclude that Chronos merely approximates linear Short-Term Reversal at $1000\times$ computational cost |

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Traditional-to-Crypto Boundary:** Sourced exclusively from US equity factor residuals (CRSP 1978–2016). The primary paper contains zero cryptocurrency empirical evidence. Application to cryptocurrency markets is purely a research-proposed hypothesis and remains completely unproven.
- **Portability Hazards & Microstructure Differences:**
  1. **Factor Model Definition in Crypto:** In equities, well-established multi-factor models (Fama-French, IPCA, Barra) provide stable residual return series. In cryptocurrency markets, systematic factor models are highly unstable: Bitcoin and Ethereum market beta dominates cross-sectional variance (often $>70\%$), and dynamic cross-sectional factor models (such as rolling PCA or volume/momentum factors) exhibit severe regime breaks during liquidity shifts and protocol blowups.
  2. **Prohibitive Fee Structures:** The strategy fails in equities at 3 bps trading cost. In cryptocurrency spot and perpetual markets, standard retail taker fees range from 4 to 7 bps per side (8–14 bps round-trip), and even institutional VIP taker rates rarely fall below 1.5–2.0 bps. An unconstrained daily rebalancing strategy would suffer fatal fee attrition within weeks.
  3. **Perpetual Funding Rate Drag:** In crypto perpetuals, holding a cross-sectional dollar-neutral long/short book incurs 8-hour funding payments. If the long leg is concentrated in high-funding altcoins and the short leg in discounted coins, funding drag could exceed 15–30% annualized, compounding turnover losses.
  4. **24/7 Continuous Trading & Timestamp Alignment:** Daily equity closing prices represent synchronized auction liquidity (4:00 PM EST). Crypto markets trade 24/7 without opening/closing auctions, meaning cross-sectional residual signals are subject to asynchronous volatility spikes and execution latency risks.
  5. **Inference Latency & Infrastructure Cost:** Running daily or intraday inference with an 11M-parameter transformer across hundreds of tokens introduces significant computational latency, requiring continuous GPU hosting that dwarfs expected net retail alpha.

## Limitations

- **Fatal Turnover Fragility:** The strategy cannot survive realistic transaction costs (net Sharpe drops from $+3.17$ to $-1.49$ under 3 bps cost), rendering the reported gross alpha unexecutable in practice.
- **Lack of Execution Realism:** The original paper assumes costless fills at recorded daily prices, completely ignoring bid-ask spread crossing, order book depth, market impact, borrow fees for short positions, and latency.
- **Survivorship & Factor Pool Bias:** The dataset relies on a static historical universe provided by Guijarro-Ordonez et al. (2021); while point-in-time rolling factor windows are used, any delisting or survivorship treatment in the underlying CRSP cut affects historical residual variance.
- **Computational Overhead vs. Performance:** Chronos required approximately one week of continuous GPU training on dual RTX 4060 Ti hardware to evaluate $\tau=15$ over 15 years, yet failed to beat a 169-parameter CNN-Transformer or a simple 1-line heuristic rule (`STR beta=0.3`).
- **Pre-2008 Regime Dependency:** The strategy's empirical gains were almost entirely generated prior to 2008, with negligible gross alpha generated in the post-financial-crisis era.

## Implementation status

- `not-implemented`.
- No implementation of Chronos-based statistical arbitrage exists in `nautilus-quant-system`, PyBroker, or NautilusTrader.
- No historical backtest, paper trading, demo testnet, or live trading has been authorized or conducted.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption Scope:** `not-approved`.
- **Approval Boundary:** Research capture only. The presence of this record in the repository documents empirical findings and a critical negative result on foundation-model turnover drag. It does not constitute approval for strategy implementation, paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- `[[quant/statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05]]` — Deep learning factor replication and statistical arbitrage on equity residuals.
- `[[quant/statistical-arbitrage-rank-space-cnn-transformer-hybrid-atlas-2026-09-02]]` — Specialized rank-space CNN-Transformer statistical arbitrage.
- `[[quant/ordinal-gates-cardinal-bets-llm-confidence-exposure-coupling-2026-09-05]]` — Decision operator coupling and exposure control under foundation model uncertainty.
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Canonical protocol for preventing lookahead leakage and cross-fold contamination in financial machine learning.

## Sources

1. **Primary Research Paper:**
   - Sebastien Valeyre and Sofiane Aboura, *"Large Language Models for Time Series: an Application for Single Stocks and Statistical Arbitrage"*, arXiv preprint `arXiv:2412.09394v2 [q-fin.PM]`, submitted December 12, 2024, revised November 3, 2025.
   - Stable Abstract URL: `https://arxiv.org/abs/2412.09394`
   - Full-Text HTML: `https://arxiv.org/html/2412.09394v2`
   - Full-Text PDF: `https://arxiv.org/pdf/2412.09394v2`
   - License: Creative Commons Public Domain Dedication (CC0 1.0 Universal)
2. **Primary Factor Residual Data Source:**
   - Guijarro-Ordonez, J., Pelger, M., & Zanotti, G. (2021). *"Deep Learning Statistical Arbitrage"*, arXiv preprint `arXiv:2106.00312 [q-fin.ST]`.
   - GitHub Repository: `https://github.com/gregzanotti/dlsa-public/tree/main/residuals` (CRSP US equity daily residuals for IPCA, PCA, and FF5 models, 1978–2016).
3. **Pretrained Foundation Model Source:**
   - Ansari, A. F., Stella, L., Turkmen, C., Zhang, X., Mercado, P., Shen, H., Shchur, O., Rangapuram, S. S., Pineda Arango, S., Kapoor, S., Zschiegner, J., Maddix, D. C., Wang, H., Mahoney, M. W., Torkkola, K., Wilson, A. G., Bohlke-Schneider, M., & Wang, Y. (2024). *"Chronos: Learning the Language of Time Series"*, arXiv preprint `arXiv:2403.07815 [cs.LG]`.
   - GitHub Repository: `https://github.com/amazon-science/chronos-forecasting` (`amazon/chronos-t5-tiny`).
