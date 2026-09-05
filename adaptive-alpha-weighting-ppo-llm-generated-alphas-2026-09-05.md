---
schema: strategy-research-record-v1
title: "Adaptive Alpha Weighting with PPO: Dynamic Integration of Prompt-Based LLM-Generated Formulaic Alphas"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reinforcement-learning
  - proximal-policy-optimization
  - formulaic-alpha
  - llm-agent
  - deepseek
  - portfolio-optimization
  - equities
  - cross-asset
status: research-only
confidence: medium
source_as_of: 2026-03-04
sources:
  - "arXiv:2509.01393v2 — https://arxiv.org/abs/2509.01393"
  - "https://doi.org/10.48550/arXiv.2509.01393"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Adaptive Alpha Weighting with PPO: Dynamic Integration of Prompt-Based LLM-Generated Formulaic Alphas

## Provenance

- **Paper Title:** Adaptive Alpha Weighting with PPO: Enhancing Prompt-Based LLM-Generated Alphas in Quant Trading
- **Authors:** Qizhao Chen and Hiroaki Kawashima (Graduate School of Information Science, University of Hyogo, Kobe, Japan)
- **arXiv Identifier:** `arXiv:2509.01393v2 [q-fin.PM]` (v1 submitted September 2, 2025; revised March 4, 2026)
- **Digital Object Identifier (DOI):** [10.48550/arXiv.2509.01393](https://doi.org/10.48550/arXiv.2509.01393)
- **Primary URLs:**
  - Abstract: [https://arxiv.org/abs/2509.01393](https://arxiv.org/abs/2509.01393)
  - Full Text HTML: [https://arxiv.org/html/2509.01393v2](https://arxiv.org/html/2509.01393v2)
  - Primary Source Package: arXiv LaTeX source tarball (`arXiv:2509.01393v2`) directly inspected for algorithmic specifications, mathematical formulations, and tabular data.
- **Repository Pre-Write Deduplication Audit:**
  - A full search across `alpha-strategy-research` confirmed zero prior records referencing `arXiv:2509.01393`, "Adaptive Alpha Weighting with PPO", or "Prompt-Based LLM-Generated Alphas".
  - Related record `sentiment-vader-technical-indicator-mean-variance-crypto-portfolio-2026-09-04.md` cites a different paper by author Qizhao Chen (`arXiv:2508.16378`), which investigates static Ridge-regression-based Mean-Variance optimization in cryptocurrency markets. The present paper is materially distinct in mechanism (reinforcement learning via PPO vs. convex QP Markowitz), signal construction (50 prompt-distilled DeepSeek formulaic alphas vs. linear technical indicators), state space (POMDP with moving-average regime gates and rolling volatility scaling vs. static covariance matrix), and asset class (international equities vs. cryptocurrencies).

---

## Economic mechanism

### Source-reported

The authors argue that while large language models (LLMs)—specifically reasoned prompt models like `deepseek-r1-distill-llama-70b`—can generate diverse formulaic alphas capturing momentum, mean reversion, sentiment, and volume dynamics, individual alphas suffer from severe non-stationarity and alpha decay. In static or equal-weighted combinations, decaying alphas dilute portfolio returns and elevate drawdowns. 

To address this, the authors propose framing alpha combination as a sequential decision-making problem governed by a Partially Observable Markov Decision Process (POMDP). By employing Proximal Policy Optimization (PPO), an on-policy actor-critic algorithm with a clipped surrogate objective, the system dynamically reallocates weights across 50 formulaic alphas in response to observed market feedback. To control downside risk during adverse regimes, the trading environment embeds two structural constraints:
1. **Regime-Aware Risk Penalty:** Penalizes positions that conflict with the prevailing trend regime (determined by a 20-day vs. 100-day moving average crossover).
2. **Dynamic Volatility Targeting & Adaptive Quintile Filtering:** Dynamically scales exposure inversely to 63-day realized volatility and filters trade entries using rolling 126-day price quantiles (75th and 25th percentiles).

The authors report that this framework stabilizes policy updates, enforces capital preservation during drawdowns, and achieves significantly higher Sharpe ratios and lower maximum drawdowns than static equal-weighted, buy-and-hold, or simple momentum strategies.

### Research interpretation

The candidate alpha mechanism operates on three distinct economic channels:
1. **Dynamic Factor Timing / Multi-Signal Regime Switching:** Individual formulaic alphas capture distinct behavioral inefficiencies (e.g., short-term overreaction to earnings sentiment, medium-term trend continuation, volume-confirmed price breakouts). Because market regimes shift between trending and mean-reverting states, static weights inevitably hold decaying or inverted signals. The PPO policy network functions as a non-linear factor-timing allocator, learning to dynamically up-weight robust signals and down-weight or invert deteriorating signals based on market regime and volatility context.
2. **Asymmetric Capital Preservation via Policy-Level Risk Shaping:** Standard quantitative strategies optimize raw returns, often suffering severe drawdowns when underlying factor premises fail. Embedding explicit soft penalties for trend-regime contradiction ($\mathcal{P}^{\text{regime}}_t$) directly into the reinforcement learning reward function conditions the agent to adopt a conservative, selective participation profile. This results in low trade frequency during chop and prolonged market-neutral stances during adverse conditions, driving drawdown reduction.
3. **Volatility Budgeting:** Volatility scaling ensures that position risk remains homoskedastic across market cycles, preventing high-volatility regimes from dominating portfolio variance.

This is a **hybrid alpha framework**: a library of diverse LLM-generated predictive formulaic signals coupled with an adaptive reinforcement-learning gating and capital allocation policy.

---

## Signal

The signal and execution pipeline is fully specified by the primary source:

### 1. Alpha Signal Generation & Normalization
- **LLM Generator:** Prompt-based `deepseek-r1-distill-llama-70b` (deployed via Groq) prompted with training-period OHLCV, 11 technical indicators (`pandas-ta`), daily NLTK VADER sentiment polarity scores $S_t \in [-1, 1]$ from Yahoo News (via EODHD API), and global indices (S&P 500, Nikkei 225, Hang Seng Index).
- **Alpha Library:** 50 formulaic mathematical expressions ($\alpha_{1,t}$ to $\alpha_{50,t}$) shared across all assets [source-reported].
  - *Momentum:* e.g., $\alpha_{1,t} = (C_t - O_t)/O_t + 0.5 \cdot \text{Mom}_3$; $\alpha_{2,t} = \text{Mom}_{10} \cdot (C_t - \text{SMA}_5)$; $\alpha_{3,t} = (\text{Mom}_3 + \text{Mom}_{10})/2$.
  - *Sentiment:* e.g., $\alpha_{6,t} = S_t \cdot (C_t - O_t)/O_t$; $\alpha_{7,t} = \text{Polarity}_{\text{Apple}} \cdot (C_t - \text{SMA}_5)$.
  - *Volume:* e.g., $\alpha_{11,t} = V_t / \text{SMA}_{20}$; $\alpha_{12,t} = \text{OBV} \cdot (C_t - O_t)/O_t$.
  - *Global Index:* e.g., $\alpha_{16,t} = (C_t / C_{\text{Nikkei}}) \cdot S_t$; $\alpha_{17,t} = (C_t / C_{\text{SP500}}) \cdot \text{Mom}_3$.
  - *Technical Oscillators:* e.g., $\alpha_{21,t} = \text{MACD} \cdot \text{Signal}$; $\alpha_{25,t} = \text{BB}_{\text{Upper}} - \text{BB}_{\text{Lower}}$.
  - *Combinations:* e.g., $\alpha_{31,t} = (C_t - \text{SMA}_5)/\text{SMA}_5 + 0.5 \cdot S_t$; $\alpha_{50,t} = (C_t - \text{SMA}_5)/\text{SMA}_5 + (C_t - \text{SMA}_{20})/\text{SMA}_{20} + S_t + \text{Mom}_3 + \text{Mom}_{10}$.
- **Standardization:** Each raw alpha $\alpha_{i,t}$ is standardized via `StandardScaler` ($\mu=0, \sigma=1$) across the historical window prior to composite aggregation [source-reported].

### 2. State Observation Space ($s_t \in \mathcal{S}$)
At daily decision bar $t$, the state vector integrates four components [source-reported]:
1. $\text{OHLCV}_t$: Raw daily price and volume.
2. $p_{t-1} \in [-1, 1]$: Preceding target position exposure.
3. $\text{regime}_t \in \{0, 1\}$: Trend regime indicator based on moving average crossover:
   $$\text{regime}_t = \mathbb{I}(\text{MA}_{20,t} > \text{MA}_{100,t})$$
   where $1 = \text{bullish}, 0 = \text{bearish}$.
4. $\sigma^{\text{daily}}_t$: 63-day rolling daily volatility of forward returns:
   $$\sigma^{\text{daily}}_t = \text{Std}(R^{\text{future}}_{t-62:t}), \quad \sigma^{\text{annual}}_t = \sigma^{\text{daily}}_t \sqrt{252}$$

### 3. Action Space & Alpha Weight Normalization
The policy network outputs a 50-dimensional raw weight action vector $\mathbf{w}_t = \pi_\theta(s_t) \in \mathbb{R}^{50}$ [source-reported]:
1. **Clipping:** $\tilde{\mathbf{w}}_t = \operatorname{clip}(\mathbf{w}_t, -1, 1)$
2. **$L_1$-Norm Normalization:**
   $$\mathbf{w}^{\text{norm}}_t = \frac{\tilde{\mathbf{w}}_t}{\|\tilde{\mathbf{w}}_t\|_1 + \epsilon}, \quad \text{with } \epsilon = 10^{-8}$$
   This ensures $\sum_{i=1}^{50} |w^{\text{norm}}_t[i]| \approx 1$, bounding gross leverage.

### 4. Composite Alpha Formation & Adaptive Signal Filtering
- **Composite Alpha Signal:**
  $$\alpha^{\text{composite}}_t = \sum_{i=1}^{50} w^{\text{norm}}_t[i] \cdot \alpha_{i,t}$$
- **Rolling Quantile Bounds:** Computed from a 126-day rolling close price window [source-reported]:
  $$\tau^{\text{upper}}_t = Q_{0.75}(\text{Close}_{t-126:t}), \quad \tau^{\text{lower}}_t = Q_{0.25}(\text{Close}_{t-126:t})$$
- **Signal-Based Directional Position:**
  $$p_t^{\text{raw}} = \begin{cases} \min\left(1, 2(\alpha^{\text{composite}}_t - \tau^{\text{upper}}_t)\right), & \alpha^{\text{composite}}_t > \tau^{\text{upper}}_t \\ \max\left(-1, 2(\alpha^{\text{composite}}_t - \tau^{\text{lower}}_t)\right), & \alpha^{\text{composite}}_t < \tau^{\text{lower}}_t \\ 0, & \text{otherwise} \end{cases}$$
  When composite alpha lies within $[\tau^{\text{lower}}_t, \tau^{\text{upper}}_t]$, the position is set strictly to 0 (cash / neutral filter).

### 5. Volatility Scaling & Position Sizing
- **Target Volatility:** $\sigma_{\text{target}} = 0.15$ (15% annualized) [source-reported].
- **Scaling Factor:**
  $$v_t = \min\left(2.0, \frac{\sigma_{\text{target}}}{\sigma^{\text{annual}}_t}\right)$$
- **Final Position:**
  $$p_t = p_t^{\text{raw}} \cdot v_t \in [-2, 2]$$

### 6. Reward Formulation with Regime Risk Penalty
The step reward $r_t$ driving PPO training incorporates transaction friction and trend contradiction penalty [source-reported]:
$$\text{TC}_t = \lambda \cdot |p_t - p_{t-1}| \quad (\lambda = 0.001 = 10\text{ bps})$$
$$\mathcal{P}^{\text{regime}}_t = \lambda_{\text{reg}} \cdot |p_t| \cdot \mathbb{I}(\operatorname{sign}(p_t) \neq \text{regime}_t) \quad (\lambda_{\text{reg}} = 0.05)$$
$$r_t = p_t \cdot R^{\text{future}}_t - \text{TC}_t - \mathcal{P}^{\text{regime}}_t$$
where $R^{\text{future}}_t = (C_{t+1} - C_t)/C_t$.

---

## Required data

- **Universe:** 10 international public equities [source-reported]:
  - Apple Inc. (AAPL, US Tech)
  - HSBC Holdings plc (HSBC, UK/Global Banking)
  - PepsiCo, Inc. (PEP, US Consumer Staples)
  - Tencent Holdings Ltd. (0700.HK, China Tech/Gaming)
  - Toyota Motor Corp. (TM, Japan Automotive)
  - Airbus SE (AIR.PA, Europe Aerospace)
  - Exxon Mobil Corp. (XOM, US Energy)
  - Petróleo Brasileiro S.A. - Petrobras (PBR, Brazil Energy)
  - Netflix, Inc. (NFLX, US Communication/Media)
  - InfuSystem Holdings, Inc. (INFU, US Healthcare Micro/Small Cap)
- **Timeframe & Sampling:** Daily bars (OHLCV) spanning February 16, 2016 to May 8, 2024 (~2,070 trading sessions) [source-reported].
- **Market Data Fields:**
  - Asset daily Open, High, Low, Close, Volume (`yfinance`) [source-reported].
  - Benchmark index daily Close: S&P 500 (`^GSPC`), Nikkei 225 (`^N225`), Hang Seng Index (`^HSI`) [source-reported].
- **Sentiment Feeds:**
  - Daily company-specific financial news articles retrieved via EODHD Financial News API and Yahoo News [source-reported].
  - Polarity scores $S_t \in [-1, 1]$ generated using NLTK VADER sentiment analyzer [source-reported].
- **Point-in-Time & Leakage Constraints:**
  - Feature normalization and technical indicator lookback windows use strictly backward-looking data [source-reported].
  - Training/Test partition: First 80% chronological sessions for in-sample training; final 20% held out for strictly out-of-sample evaluation [source-reported].
  - Walk-forward rolling windows: 2-year rolling training ($252 \times 2 = 504$ trading days) followed by a 1-year test ($252$ trading days), stepped forward by 6 months ($126$ trading days) [source-reported].

---

## Execution assumptions

- **Execution Timing:** Decision formed at close of day $t$; execution assumed at close price of day $t$ or immediate open of day $t+1$ [source-reported / `research-proposed` next-open execution].
- **Order Type:** Market orders assumed [source-reported / `research-proposed`].
- **Transaction Costs:** Fixed linear transaction fee of $\lambda = 0.001$ ($10\text{ bps}$ per unit turnover) explicitly subtracted in backtest and reward calculation [source-reported].
- **Slippage & Bid-Ask Spread:** Explicit bid-ask spread and non-linear market impact are **not modeled** in the primary paper [provenance gap / `research-proposed` 3–5 bps slippage stress].
- **Borrow / Short Availability:** Assumes frictionless shorting on all 10 equities with zero borrow fee [source-reported assumption; `research-proposed` realistic borrow costs of 25–150 bps p.a. for equities].
- **Holding Period:** Dynamic, determined by policy rebalance. Mean holding duration ranges from $1.00$ days (Airbus) to $14.05$ days (Netflix) [source-reported].
- **Turnover:** Average daily turnover ranges from $0.0090$ ($0.9\%$ daily for Netflix) to $0.2007$ ($20.1\%$ daily for Airbus) [source-reported].
- **Capacity / ADV Constraints:** Not modeled by authors [provenance gap; `research-proposed` maximum participation cap of $1.0\%$ 20-day ADV].

---

## Evidence

### Source-reported

All quantitative figures below are transcribed directly from Tables 7, 8, 9, 10, 12, 13, and 14 of `arXiv:2509.01393v2`:

#### 1. Out-of-Sample Performance on Fixed 80/20 Split (Table 7)
Evaluated across 10 independent non-deterministic inference runs (reported as Mean $\pm$ Std):

| Stock | Cumulative Return (PPO) | Cum. Return (B&H) | Sharpe Ratio (PPO) | Sharpe Ratio (B&H) | Max Drawdown (PPO) | Max Drawdown (B&H) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Apple** | $\mathbf{1.6817 \pm 0.0619}$ | $0.3082$ | $\mathbf{1.9998 \pm 0.0169}$ | $0.8194$ | $\mathbf{-0.0101 \pm 0.0007}$ | $-0.1732$ |
| **HSBC** | $0.5685 \pm 0.0259$ | $\mathbf{0.6161}$ | $\mathbf{2.4113 \pm 0.0558}$ | $1.6087$ | $\mathbf{-0.0220 \pm 0.0099}$ | $-0.1425$ |
| **Pepsi** | $\mathbf{0.6272 \pm 0.0331}$ | $0.1170$ | $\mathbf{1.4319 \pm 0.0434}$ | $0.5220$ | $\mathbf{-0.0067 \pm 0.0001}$ | $-0.1694$ |
| **Tencent** | $\mathbf{0.6245 \pm 0.0632}$ | $0.1752$ | $\mathbf{1.1440 \pm 0.1052}$ | $0.4680$ | $\mathbf{-0.0810 \pm 0.0208}$ | $-0.3362$ |
| **Toyota** | $0.0638 \pm 0.0267$ | $\mathbf{0.8742}$ | $1.2786 \pm 0.3810$ | $\mathbf{1.6646}$ | $\mathbf{-0.0223 \pm 0.0062}$ | $-0.1420$ |
| **Airbus** | $0.0148 \pm 0.0079$ | $\mathbf{0.6646}$ | $1.3899 \pm 0.5449$ | $\mathbf{2.4272}$ | $\mathbf{-0.0061 \pm 0.0042}$ | $-0.0757$ |
| **Exxon Mobil** | $0.0307 \pm 0.0175$ | $\mathbf{0.4597}$ | $\mathbf{1.5525 \pm 0.2590}$ | $1.5336$ | $\mathbf{-0.0030 \pm 0.0027}$ | $-0.1567$ |
| **Petrobras** | $0.0945 \pm 0.0356$ | $\mathbf{0.4659}$ | $\mathbf{1.5357 \pm 0.2272}$ | $1.1112$ | $\mathbf{-0.0102 \pm 0.0042}$ | $-0.3154$ |
| **Netflix** | $0.3085 \pm 0.0009$ | $\mathbf{0.6215}$ | $\mathbf{1.9010 \pm 0.0050}$ | $1.3044$ | $\mathbf{-0.0490 \pm 0.0004}$ | $-0.2010$ |
| **InfuSystem** | $0.0202 \pm 0.0182$ | $\mathbf{0.0912}$ | $\mathbf{0.8970 \pm 0.6531}$ | $0.4121$ | $\mathbf{-0.0101 \pm 0.0045}$ | $-0.3405$ |

*Baseline Comparisons:*
- **Equal-Weighted (EW):** Suffered negative cumulative returns in 9 of 10 assets (e.g., Apple $-32.0\%$, HSBC $-90.6\%$, Tencent $-70.7\%$) and large drawdowns (Apple $-36.6\%$, Tencent $-87.4\%$).
- **Momentum (MOM):** Suffered negative cumulative returns in 7 of 10 assets (e.g., Apple $-48.0\%$, HSBC $-56.8\%$, Tencent $-47.6\%$) and drawdowns exceeding $50\%$.
- **Random Entry/Exit (RB):** Achieved positive but substantially lower Sharpe ratios (mean $0.28$ to $1.65$) and drawdowns between $-8.3\%$ and $-29.3\%$.

#### 2. Statistical Significance Tests (Tables 8 & 9)
- **Diebold-Mariano (DM) Test vs. Baselines (Table 8):**
  - vs. Equal-Weighted: Statistically significant outperformance ($p < 0.05$ or $p < 0.01$) for 7 of 10 stocks (Apple $p=0.000$, Airbus $p=0.001$, InfuSystem $p=0.000$, etc.).
  - vs. Random Baseline: Statistically significant outperformance ($p < 0.05$ or $p < 0.01$) for 6 of 10 stocks (Apple $p=0.001$, Tencent $p=0.000$, Toyota $p=0.000$).
  - vs. Momentum: Statistically significant outperformance for 5 of 10 stocks.
  - vs. Buy-and-Hold: DM statistic was negative for 8 of 10 stocks but statistically significant at the $5\%$ level only for Tencent (DM stat $-2.25, p=0.024$) due to high cash/neutral dilution.
- **Relative Sharpe Ratio Bootstrap Test (Table 9):**
  - Block-bootstrapped $\Delta \text{SR} = \text{SR}_{\text{PPO}} - \text{SR}_{\text{B\&H}}$ (95% CI):
    - Apple: $\Delta \text{SR} = +1.7695^*$ (CI $[0.1787, 3.4424], p=0.0296$)
    - HSBC: $\Delta \text{SR} = +0.7928^*$ (CI $[0.4321, 2.2641], p=0.0006$)
    - Pepsi: $\Delta \text{SR} = +0.3365^*$ (CI $[0.0010, 1.9168], p=0.0494$)
    - Tencent: $\Delta \text{SR} = +1.3282$ (CI $[-0.6347, 3.1084], p=0.1820$)
    - Toyota: $\Delta \text{SR} = +0.4890^*$ (CI $[0.2533, 1.2456], p=0.0010$)
    - Airbus: $\Delta \text{SR} = -0.1380$ (CI $[-2.9630, 2.2057], p=0.7814$)
    - Exxon Mobil: $\Delta \text{SR} = +0.1628^*$ (CI $[0.0857, 1.1749], p=0.0370$)
    - Petrobras: $\Delta \text{SR} = +0.0903$ (CI $[-1.3394, 0.6880], p=0.8062$)
    - Netflix: $\Delta \text{SR} = +0.6016^*$ (CI $[0.1274, 1.3747], p=0.0174$)
    - InfuSystem: $\Delta \text{SR} = +1.0333^*$ (CI $[0.5141, 2.4829], p<0.0001$)
  - 7 out of 10 stocks rejected the null hypothesis of equal Sharpe ratios at the $5\%$ level.

#### 3. Execution Dynamics (Table 10)
- **Win Rate:** Across all 10 equities, average win rate was relatively low ($14.16\%$ for Pepsi, $25.82\%$ for Apple, $44.19\%$ for Netflix), demonstrating that alpha is generated through asymmetric payoff (cutting losers via regime filter and running winners) rather than high hit rate.
- **Holding Period:** Ranged from $1.00$ days (Airbus), $1.06$ days (Exxon Mobil), $1.34$ days (Toyota) to $8.04$ days (HSBC) and $14.05$ days (Netflix).
- **Daily Turnover:** Ranged from $0.0090$ (Netflix) to $0.2007$ (Airbus).

#### 4. Ablation: LLM-Generated vs. Kakushadze 101 Human-Crafted Alphas (Table 12)
Under identical PPO environment across 10 runs (controlled for 50-feature dimensionality):
- **Apple:** Human CR $-0.85\%$, SR $-0.59$ vs. LLM CR $\mathbf{+168.17\%}$, SR $\mathbf{+2.00}$.
- **HSBC:** Human CR $+0.40\%$, SR $+0.34$ vs. LLM CR $\mathbf{+56.85\%}$, SR $\mathbf{+2.41}$.
- **Pepsi:** Human CR $-0.27\%$, SR $-0.08$ vs. LLM CR $\mathbf{+62.72\%}$, SR $\mathbf{+1.43}$.
- **Toyota:** Human CR $-1.87\%$, SR $-0.52$ vs. LLM CR $\mathbf{+6.38\%}$, SR $\mathbf{+1.28}$.
- **Tencent:** Human CR $+4.95\%$, SR $\mathbf{+2.01}$ vs. LLM CR $\mathbf{+62.45\%}$, SR $+1.14$.

#### 5. RL Algorithm Comparison (Table 13)
Comparing PPO against SAC, TD3, and A2C under identical states and rewards:
- **Apple:** PPO CR $\mathbf{1.6817}$ (SR $2.00$), SAC CR $0.5621$ (SR $\mathbf{2.61}$), TD3 CR $0.5845$ (SR $\mathbf{2.62}$), A2C CR $0.5619$ (SR $2.59$).
- **Pepsi:** PPO CR $\mathbf{0.6272}$ (SR $\mathbf{1.43}$), SAC CR $0.0568$ (SR $0.86$), TD3 CR $0.0567$ (SR $0.86$), A2C CR $0.0569$ (SR $0.86$).
- Max drawdowns across all RL algorithms remained bounded below $-1\%$ to $-8\%$.

#### 6. Walk-Forward Out-of-Sample Performance (Table 14)
Averaged across rolling windows (2-year train / 1-year test / 6-month step):
- **Apple:** PPO Ann. Vol $\mathbf{4.74\%}$, Sharpe $\mathbf{1.55 \pm 0.86}$, Max DD $\mathbf{-0.40\%}$ vs. B&H Sharpe $0.96$, Max DD $-25.0\%$.
- **HSBC:** PPO Total Return $\mathbf{+3.79\%}$, Sharpe $\mathbf{1.19 \pm 2.10}$, Max DD $\mathbf{-2.56\%}$ vs. B&H Total Return $-18.55\%$, Sharpe $-0.74$, Max DD $-70.82\%$.
- **Pepsi:** PPO Sharpe $\mathbf{0.85 \pm 1.51}$, Max DD $\mathbf{-1.09\%}$ vs. B&H Sharpe $0.85$, Max DD $-15.06\%$.
- **Tencent:** PPO Ann. Vol $\mathbf{4.38\%}$, Max DD $\mathbf{-2.48\%}$ vs. B&H Max DD $-60.62\%$.
- **Toyota:** PPO Sharpe $\mathbf{0.89 \pm 1.04}$, Max DD $\mathbf{-0.70\%}$ vs. B&H Sharpe $0.73$, Max DD $-19.11\%$.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Underperformance in Strong Bull Markets:** On stocks with massive secular bull runs (e.g., Toyota B&H CR $+87.4\%$ vs. PPO $+6.4\%$; Airbus B&H CR $+66.5\%$ vs. PPO $+1.5\%$; Exxon Mobil B&H CR $+46.0\%$ vs. PPO $+3.1\%$), the strategy significantly underperformed passive buy-and-hold in total return. This occurs because the policy is risk-constrained (volatility targeting capped at 15% and quantile thresholds requiring neutral/cash holding during non-extreme signals).
2. **Low Win Rates:** The policy displays hit rates between $14\%$ and $44\%$, meaning the majority of daily bars exit flat or with small friction losses. If executed in high-spread or high-slippage environments, transaction drag could eliminate the edge.
3. **Equal-Weighted Alpha Failure:** Equal-weighted combination of all 50 LLM alphas generated severe negative returns ($-32\%$ on Apple, $-90.6\%$ on HSBC, $-70.7\%$ on Tencent), proving that LLM alpha generation alone does NOT provide unconditional positive expected return. The entire positive performance is contingent on the PPO weighting, regime penalty, and risk-filtering layers.
4. **Sentiment Sensitivity Indifference:** The authors' ablation in Section 5.6 (Table 18) revealed that removing sentiment features entirely yielded virtually indistinguishable performance, proving that textual news sentiment provided zero incremental economic alpha beyond price and technical volume signals.

---

## Falsification plan

The core hypotheses of the PPO adaptive alpha weighting strategy can be operationalized and tested for falsification through the following experimental protocols:

1. **Transaction Cost and Slippage Stress Test:**
   - *Protocol:* Simulate the strategy under progressive transaction costs: $\lambda \in \{5, 10, 20, 30, 50\}\text{ bps}$ per unit turnover.
   - *Decision Rule (`research-defined falsification threshold`):* If the net Sharpe ratio drops below $0.50$ or annualized net return becomes non-positive at $\lambda \le 20\text{ bps}$ across $> 50\%$ of the evaluated assets, reject the tradable alpha hypothesis; the reported edge is an artifact of frictionless rebalancing assumptions.
2. **Execution Timing & Look-Ahead Audit:**
   - *Protocol:* Replace the same-bar close execution assumption with next-bar market-on-open execution ($p_t$ decided using data up to close of day $t$, order filled at Open of day $t+1$).
   - *Decision Rule (`research-defined falsification threshold`):* If shifting execution to next-day open degrades the mean Sharpe ratio across the 10 assets by more than $35\%$ relative to the close-price baseline, the strategy suffers from look-ahead execution bias.
3. **Regime Filter & Risk Control Ablation:**
   - *Protocol:* Retrain PPO after setting $\lambda_{\text{reg}} = 0$ (no moving-average trend penalty) and removing the rolling quintile filters ($\tau^{\text{upper}}_t, \tau^{\text{lower}}_t$).
   - *Decision Rule (`research-defined falsification threshold`):* If maximum drawdown increases by more than $300\%$ (e.g., from $-2\%$ to $>-8\%$) or Sharpe ratio degrades below the Buy-and-Hold benchmark, the hypothesis that PPO dynamically discovers regime timing endogenously is rejected; risk reduction is purely mechanical from the heuristic filters.
4. **Permutation & Placebo Alpha Test:**
   - *Protocol:* Replace the 50 LLM formulaic alphas with 50 synthetic Gaussian white-noise series with identical marginal variance, keeping the PPO architecture identical.
   - *Decision Rule (`research-defined falsification threshold`):* If the PPO agent trained on noise alphas achieves an out-of-sample Sharpe ratio within $15\%$ of the LLM-alpha model, reject the hypothesis that LLM alphas carry true informational content; the performance is an artifact of the volatility-targeting overlay and moving-average filter.
5. **Universe Expansion to Unseen Assets:**
   - *Protocol:* Apply the identical 50 formulaic alphas and PPO architecture to a clean, unseen universe of 50 liquid US equities (e.g., S&P 500 constituents) over the 2024–2026 horizon without retraining the prompt.
   - *Decision Rule (`research-defined falsification threshold`):* If the out-of-sample cross-sectional median Sharpe ratio is $\le 0.30$ or fails to exceed an equal-weighted sector benchmark, the candidate is classified as overfit to the 10 exploratory stocks.

---

## Crypto portability

**Portability Classification: Adapted / Unproven**

The primary source evaluated the strategy exclusively on 10 single-stock equities across international jurisdictions. Porting this framework to cryptocurrency markets represents a research interpretation and faces significant market-microstructure differences:

1. **Continuous 24/7/365 Trading Horizon:** Equities feature standardized daily opens and closes with weekend halts. Crypto perpetuals trade continuously. Daily bar boundaries must be fixed to a synthetic convention (e.g., 00:00 UTC) [`research-proposed`].
2. **Perpetual Futures Funding Rate Carry:** In crypto perpetual contracts, holding long or short positions entails 8-hour funding rate payments. In persistent bull markets, funding rates can exceed $20\%-50\%$ APR, severely penalizing short-term trend filters or long positions held across high-funding intervals [`research-proposed`].
3. **Volatility Scaling Calibration:** Crypto assets exhibit annualized volatilities of $50\%-120\%$, compared to $15\%-30\%$ in large-cap equities. The fixed $\sigma_{\text{target}} = 0.15$ (15%) would force the leverage scaler $v_t = \min(2, 0.15/\sigma)$ to allocate negligible capital ($10\%-20\%$ position exposure), turning the strategy into a predominantly cash-holding system unless recalibrated to a crypto-specific target (e.g., $\sigma_{\text{target}} = 0.50$) [`research-proposed`].
4. **Moving Average Regime Drift:** High crypto volatility leads to frequent whipsaws across 20-day and 100-day moving averages, which could trigger excessive regime violation penalties ($\mathcal{P}^{\text{regime}}_t$) during range-bound chop [`research-proposed`].
5. **Cross-Sectional Rank Dispersion:** The 50 formulaic alphas use single-asset indicators and equity index closes (S&P 500, Nikkei). A crypto adaptation must replace these indices with crypto proxies (e.g., BTC, ETH, TOTAL market cap) and incorporate crypto-native features such as aggregate Open Interest, liquidation volumes, and exchange net inflows [`research-proposed`].

---

## Limitations

- **Small Asset Universe:** Empirical testing is restricted to only 10 stocks, selected manually across sectors, which introduces sample selection risk.
- **Underspecified Real-World Friction:** No bid-ask spread, borrow fee, or price impact is included in backtests. Only a flat $10\text{ bps}$ transaction fee is modeled.
- **Cash Drag in Strong Up-Trends:** Strong capital preservation rules produce substantial underperformance in secular bull regimes (e.g., Toyota $+6.4\%$ vs. $+87.4\%$ B&H).
- **Reliance on LLM Prompt Repeatability:** LLM prompt distillation outputs are stochastic and subject to prompt drift or model deprecation over time.
- **Low Hit Ratio:** Win rates below $30\%$ for several stocks indicate that profitability hinges entirely on managing the payoff ratio rather than predicting directional probability.
- **Daily Rebalance Latency:** Daily frequency limits ability to react to intraday liquidity shocks or crash regimes.

---

## Implementation status

Not implemented. No implementation currently exists in the `nautilus-quant-system` repository, PyBroker pipelines, or NautilusTrader backtesting harness.

---

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

The strategy must undergo rigorous out-of-sample validation, realistic spread/slippage modeling, and benchmark contrast tests in PyBroker and NautilusTrader before any implementation decision can be considered.

---

## Related Wiki records

- `[[quant/sac-two-sided-lending-perpetual-portfolio-2026-09-05]]` — Reinforcement learning (SAC) applied to multi-asset crypto perpetual futures with interest-rate lending.
- `[[quant/alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05]]` — Formulaic alpha mining via tree-LSTM grammar search.
- `[[quant/alphalogics-market-logic-multi-agent-factor-generation-2026-09-05]]` — Multi-agent LLM reasoning for formulaic alpha factor generation.
- `[[quant/deep-portfolio-optimization-attention-lstm-omega-cvar-risk-parity-2026-09-03]]` — Deep neural network optimizing differentiable risk surrogates.
- `[[quant/regime-switching-hmm-reinforcement-learning-etf-allocation-2026-09-04]]` — Regime-aware reinforcement learning for multi-asset allocation.
- `[[quant/sentiment-vader-technical-indicator-mean-variance-crypto-portfolio-2026-09-04]]` — Sentiment and technical indicator integration in crypto mean-variance portfolios.

---

## Sources

1. **Primary Academic Source:** Qizhao Chen and Hiroaki Kawashima, *"Adaptive Alpha Weighting with PPO: Enhancing Prompt-Based LLM-Generated Alphas in Quant Trading"*, arXiv preprint `arXiv:2509.01393v2 [q-fin.PM]`, submitted September 2, 2025; revised March 4, 2026. DOI: [10.48550/arXiv.2509.01393](https://doi.org/10.48550/arXiv.2509.01393). URL: [https://arxiv.org/abs/2509.01393](https://arxiv.org/abs/2509.01393). Full text HTML: [https://arxiv.org/html/2509.01393v2](https://arxiv.org/html/2509.01393v2).
2. **Foundational Citations Cited in Primary Source:**
   - John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov, *"Proximal Policy Optimization Algorithms"*, arXiv preprint `arXiv:1707.06347`, 2017.
   - Zura Kakushadze, *"101 Formulaic Alphas"*, Wilmott Magazine, 2016(84):72–80, 2016. arXiv: `arXiv:1601.00991`.
