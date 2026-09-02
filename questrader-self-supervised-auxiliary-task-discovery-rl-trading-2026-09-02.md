---
schema: strategy-research-record-v1
title: "QUESTrader: Self-Supervised Auxiliary Task Discovery via General Value Functions and Non-Myopic Meta-Gradients for Stable Reinforcement Learning in Multi-Stock Trading"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reinforcement-learning
  - ppo
  - auxiliary-tasks
  - general-value-functions
  - meta-gradients
  - multi-stock-trading
  - representation-learning
  - transaction-costs
status: research-only
confidence: high
source_as_of: 2026-08-16
sources:
  - "Arishi Orra, Himanshu Choudhary, and Manoj Thakur, 'Self-Supervised Auxiliary Task Discovery for Stable Reinforcement Learning in Stock Trading', arXiv:2608.15841v1 [q-fin.TR, cs.LG], August 16, 2026. DOI: https://doi.org/10.48550/arXiv.2608.15841. Full text: https://arxiv.org/abs/2608.15841, HTML: https://arxiv.org/html/2608.15841v1, PDF: https://arxiv.org/pdf/2608.15841"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QUESTrader: Self-Supervised Auxiliary Task Discovery via General Value Functions and Non-Myopic Meta-Gradients for Stable Reinforcement Learning in Multi-Stock Trading

## Provenance

- **Canonical Source:** arXiv:2608.15841v1 [q-fin.TR, cs.LG], submitted August 16, 2026.
- **Authors:** Arishi Orra (Corresponding Author, `d21022@students.iitmandi.ac.in`), Himanshu Choudhary (`d21024@students.iitmandi.ac.in`), and Manoj Thakur (`manoj@iitmandi.ac.in`).
- **Affiliation:** School of Mathematical and Statistical Sciences, Indian Institute of Technology Mandi, Mandi 175005, Himachal Pradesh, India.
- **DOI:** [https://doi.org/10.48550/arXiv.2608.15841](https://doi.org/10.48550/arXiv.2608.15841)
- **Stable Source URLs:**
  - Abstract: [https://arxiv.org/abs/2608.15841](https://arxiv.org/abs/2608.15841)
  - Full Text HTML: [https://arxiv.org/html/2608.15841v1](https://arxiv.org/html/2608.15841v1)
  - PDF: [https://arxiv.org/pdf/2608.15841](https://arxiv.org/pdf/2608.15841)
- **Data Source & Universe:** Daily closing prices retrieved from Yahoo Finance covering January 1, 2010 to March 31, 2025 across four major global equity indices:
  1. Dow Jones Industrial Average (DJI, 30 large-cap US equities);
  2. Financial Times Stock Exchange 100 (FTSE 100, top 30 UK blue chips by market capitalization);
  3. Bombay Stock Exchange Sensitive Index (BSE Sensex, 30 leading Indian large-cap equities);
  4. Taiwan Capitalization Weighted Stock Index (TAIEX, top 30 Taiwanese equities by market capitalization).
- **Partitioning & Protocol:**
  - **In-Sample Training & Validation:** January 1, 2010 to December 31, 2023 (14 years);
  - **Out-of-Sample Test Window:** January 1, 2024 to March 31, 2025 (15 months);
  - **Evaluation Harness:** Initial capital of $1,000,000; fixed transaction fee of 0.1% (10 bps) per trade applied to both buy and sell orders. Hyperparameters tuned via Bayesian Optimization (Hyperopt) over the validation split.

## Economic mechanism

### Source-reported

1. **Representation Degradation in Financial Deep Reinforcement Learning:** Financial asset returns exhibit severe non-stationarity, low signal-to-noise ratios, and regime-dependent autocorrelation structures. When Deep Reinforcement Learning (DRL) agents optimize policies directly on scalar portfolio rewards (profit/loss minus transaction fees), the sparse and noisy reward signal frequently leads to brittle representations, gradient saturation, and catastrophic out-of-sample policy collapse.
2. **Fragility of Hand-Crafted Auxiliary Tasks:** While auxiliary prediction tasks (e.g., predicting forward price changes, realized volatility, or technical indicator regimes) can regularize neural networks and improve sample efficiency, conventional designs rely on rigid, heuristic choices of targets and prediction horizons. In non-stationary markets, fixed auxiliary tasks easily misalign with policy optimization as market regimes shift (e.g., predicting momentum during a sharp mean-reverting crisis), introducing negative transfer and degrading trading performance.
3. **Automated Discovery via General Value Functions (GVFs):** General Value Functions formalize predictive questions about the future as expected discounted cumulative returns of arbitrary cumulant signals:
   $$G_t = \mathbb{E}_\pi \left[ \sum_{k=0}^\infty \left( \prod_{m=0}^{k-1} \gamma_{t+m} \right) c_{t+k+1} \,\Bigg|\, s_t \right]$$
   QUESTrader decouples task discovery from policy execution into a two-network architecture:
   - A **Question Network** parameterized by $\eta$ observes future trajectory transitions and dynamically emits cumulants $c_t$ and discount factors $\gamma_t$ defining a bank of $d_q$ auxiliary GVF questions.
   - An **Answer/Main Network** parameterized by $\theta$ receives the current market state $s_t$ and jointly predicts trading policy actions, state values, and the answers to the discovered GVF questions.
4. **Non-Myopic Meta-Gradient Credit Assignment:** The question network has no access to external supervised market labels; instead, it is trained to maximize downstream PPO policy performance. By unrolling the inner PPO parameter updates over $K$ steps, a non-myopic meta-gradient differentiates through the entire optimization trajectory $\theta_{t,0} \to \dots \to \theta_{t,K}$, updating $\eta$ based on how discovered auxiliary questions shape the future learning dynamics of the policy.

### Research interpretation

- **Dynamic Manifold Regularization:** Discovered GVFs function as an adaptive, state-dependent feature regularizer. Rather than constraining the shared encoder with static inductive biases (such as fixed-window momentum forecasting), the meta-gradient guides the question network to discover targets that capture transient market microstructure and latent regime dynamics. When a regime shift occurs, the auxiliary heads adjust their cumulants and discount rates, shielding the policy representation from catastrophic forgetting.
- **Delayed Credit Assignment across Inner Trajectories:** Single-step (myopic, $K=1$) meta-updates fail to recognize the delayed utility of auxiliary representation learning because representation gains materialize only after multiple policy updates. Non-myopic unrolling ($K \in [10, 20]$) acts as a temporal low-pass filter, propagating gradient credit across multiple PPO updates while preventing high-frequency noise from corrupting question definitions.
- **Ported Hypothesis Note:** The empirical validation in arXiv:2608.15841v1 is conducted entirely on global equity indices (DJI, FTSE 100, Sensex, TAIEX). Applying this self-supervised GVF discovery framework to crypto perpetual futures or spot markets is an adapted, unproven research interpretation.

## Signal

### Observation Space

For an $n$-stock trading universe, each state observation $s_t \in \mathcal{S}$ is a continuous vector of dimension $(10n + 1)$ (for $n = 30$, dimension is 301):
1. **Available Cash Balance:** Remaining unallocated capital ($1$ scalar);
2. **Asset Holdings:** Current shares held in each of the $n$ stocks ($n$ scalars);
3. **Close Prices:** Current observed closing price for each of the $n$ stocks ($n$ scalars);
4. **Technical Indicators:** Eight technical indicators computed for each stock ($8n$ scalars):
   - 30-day Simple Moving Average (SMA-30);
   - 60-day Simple Moving Average (SMA-60);
   - Moving Average Convergence Divergence (MACD);
   - Upper Bollinger Band;
   - Lower Bollinger Band;
   - Relative Strength Index (RSI);
   - Commodity Channel Index (CCI);
   - Average Directional Index (ADX).

### Action Space

The action $a_t \in \mathcal{A}$ is an $n$-dimensional discrete integer vector:
$$a_t = [a_{t,1}, \dots, a_{t,n}]^\top, \quad a_{t,i} \in \{-m, \dots, 0, \dots, m\}$$
where $a_{t,i}$ represents the number of shares to buy ($>0$), sell ($<0$), or hold ($0$) for stock $i$ at time $t$, subject to a maximum trading limit $m$ shares per step. The discrete action space contains $(2m + 1)^n$ combinations.

### Reward Function

The immediate reward $r(s_t, a_t)$ quantifies account net value change net of transaction costs:
$$r(s_t, a_t) = (P_{t+1} - P_t) \cdot a_t - \delta P_t \cdot |a_t - a_{t-1}|$$
where $P_t$ is the vector of stock closing prices at time $t$, and $\delta = 0.001$ is the proportional transaction fee (10 bps on both buys and sells).

### Two-Network GVF Architecture & Meta-Gradient Optimization

1. **Question Network ($g_\eta$):**
   - Receives a short future rollout slice $s_{t+1:t+j}$ available during training;
   - Emits cumulants $c_t \in \mathbb{R}^{d_q}$ and discount factors $\gamma_t \in [0, 1]^{d_q}$ for $d_q$ auxiliary questions.
2. **Main/Answer Network ($f_\theta$):**
   - Receives current state $s_t$;
   - Emits policy $\pi_\theta(a_t | s_t)$, value function $V_\theta(s_t)$, and auxiliary predictions $y_\theta(s_t) \in \mathbb{R}^{d_q}$.
   - For question $i \in \{1, \dots, d_q\}$, the predicted answer targets the truncated $W$-step Temporal Difference return:
     $$G_t^{(i)} = \sum_{n=0}^W \left( \prod_{m=0}^{n-1} \gamma_{t+m}^{(i)} \right) c_{t+n+1}^{(i)} + \left( \prod_{m=0}^W \gamma_{t+m}^{(i)} \right) y_{\theta'}^{(i)}(s_{t+W+1})$$
   - Auxiliary Answer Loss:
     $$J_{\text{ans}}(\theta; \eta) = \frac{1}{d_q} \sum_{i=1}^{d_q} \frac{1}{2} \mathbb{E} \left[ \left( G_t^{(i)} - y_\theta^{(i)}(s_t) \right)^2 \right]$$
   - Main Network Joint Loss:
     $$J_{\text{main}}(\theta; \eta) = J_{\text{PPO}}(\theta) + \lambda_{\text{aux}} J_{\text{ans}}(\theta; \eta)$$
     where $J_{\text{PPO}}(\theta)$ is the standard clipped surrogate PPO objective:
     $$J_{\text{PPO}}(\theta) = \mathbb{E}_t \left[ \min\left( \hat{r}_t(\theta) \hat{A}_t, \, \text{clip}(\hat{r}_t(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t \right) \right] - c_1 L_t^{VF}(\theta) + c_2 S[\pi_\theta](s_t)$$
3. **Bi-Level Meta-Optimization:**
   - **Inner Loop:** For $k = 0, \dots, K-1$, update main parameters:
     $$\theta_{t, k+1} = \theta_{t, k} - \alpha \nabla_{\theta_{t, k}} J_{\text{main}}(\theta_{t, k}; \eta_t)$$
   - **Outer Loop:** Evaluate the cumulative meta-objective across the $K$ inner unroll steps:
     $$\mathcal{M}_t(\eta) = \sum_{k=1}^K J_{\text{PPO}}(\theta_{t, k})$$
   - **Non-Myopic Meta-Gradient Update:**
     $$\nabla_\eta \mathcal{M}_t(\eta) = \sum_{k=1}^K \frac{\partial J_{\text{PPO}}(\theta_{t, k})}{\partial \theta_{t, k}} \frac{\partial \theta_{t, k}}{\partial \eta}$$
     $$\eta_{t+1} = \eta_t - \beta \nabla_\eta \mathcal{M}_t(\eta), \quad \theta_{t+1} = \theta_{t, K}$$

### Hyperparameter Search Space & Operating Configuration

From Table 1 and Section 6.3 ablation studies:
- **Hidden Dimensions:** Range $[2, 512]$;
- **Layers:** Range $[1, 8]$;
- **Activation:** [ReLU, Tanh, Sigmoid];
- **Learning Rates:** $\alpha, \beta \in [e^{-8}, e^{-1}]$;
- **Discount Factor $\gamma$:** $[0.9, 0.99]$;
- **PPO Epochs:** $[5, 50]$;
- **Value Loss Coefficient $c_1$:** $[0.01, 0.5]$;
- **Auxiliary Loss Coefficient $\lambda_{\text{aux}}$:** $[0.01, 0.5]$;
- **Entropy Coefficient $c_2$:** $[0.01, 0.1]$;
- **Number of GVF Questions ($d_q$):** Sweet-spot range $d_q \in [16, 64]$ (tested across $\{2, 4, 8, 16, 32, 64, 128\}$; peak Sharpe at $d_q = 16$);
- **Inner Unroll Length ($K$):** Sweet-spot range $K \in [10, 20]$ (tested across $\{1, 2, 4, 10, 20, 50\}$; peak Sharpe at $K = 10$).

## Required data

- **Instruments:** 30 leading equities from DJI, FTSE 100, Sensex, and TAIEX.
- **Venue:** Daily adjusted equity prices sourced from Yahoo Finance.
- **Market Type:** Spot cash equity.
- **Timeframe:** Daily closing bars.
- **Fields:** Open, High, Low, Close, Volume.
- **Point-in-Time Availability:** Indicators computed strictly using closing prices up to date $t$.
- **Missing Data:** Standard forward-fill on non-trading holiday mismatches across international exchanges.

## Execution assumptions

- **Execution Timing:** All stock transactions executed at the day's official closing price.
- **Transaction Costs:** Fixed linear transaction fee of 0.1% (10 bps) charged on both buy and sell turnover:
  $$\text{Cost}_t = \delta P_t \cdot |a_t - a_{t-1}|, \quad \delta = 0.001$$
- **Slippage:** Zero slippage assumed (infinite depth at closing price).
- **Market Impact:** Negligible market impact assumed (trades do not move the closing print).
- **Settlement:** Immediate settlement at the end of each daily period.
- **Initial Capital:** $1,000,000.
- **Shorting / Margin:** Bounded integer positions within holding limits; cash balance constrained non-negative.

## Evidence

### Source-reported

All figures below are directly cited from Arishi Orra, Himanshu Choudhary, and Manoj Thakur (arXiv:2608.15841v1, Tables 2–5 and Section 6), evaluated out-of-sample from January 1, 2024 to March 31, 2025 across five independent runs (mean ± standard deviation):

#### 1. Dow Jones Industrial Average (DJI, Table 2)
| Model | Annual Return (%) | Cumulative Return (%) | Sharpe Ratio | Max Drawdown (%) | Calmar Ratio | Sortino Ratio |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Buy-and-Hold | 12.857 | 16.097 | 0.884 | 10.433 | 1.054 | 1.066 |
| DJI Benchmark Index | 8.234 | 10.258 | 0.724 | 9.331 | 0.882 | 1.040 |
| Mean-Variance Optimization (MVO) | 11.744 | 14.687 | 1.247 | 8.365 | 2.188 | 1.796 |
| Standard PPO | 15.674 ± 1.44 | 19.685 ± 1.81 | 1.076 ± 0.09 | 11.713 ± 0.90 | 1.338 ± 0.12 | 1.575 ± 0.13 |
| DREB Baseline | 17.562 ± 1.59 | 22.101 ± 2.02 | 1.359 ± 0.11 | 9.342 ± 0.74 | 1.879 ± 0.15 | 2.018 ± 0.17 |
| Deep Scalper | 18.176 ± 1.67 | 22.889 ± 2.14 | 1.215 ± 0.10 | 10.469 ± 0.81 | 2.325 ± 0.18 | 1.908 ± 0.15 |
| **QUESTrader (Proposed)** | **21.785 ± 1.42** | **27.536 ± 1.91** | **1.459 ± 0.09** | 10.369 ± 0.68 | **2.394 ± 0.14** | **2.143 ± 0.13** |

#### 2. FTSE 100 (Table 3)
| Model | Annual Return (%) | Cumulative Return (%) | Sharpe Ratio | Max Drawdown (%) | Calmar Ratio | Sortino Ratio |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Buy-and-Hold | 5.651 | 6.984 | 0.774 | 11.081 | 0.816 | 0.906 |
| FTSE Index Benchmark | 9.828 | 12.140 | 0.833 | 10.183 | 0.896 | 1.117 |
| Mean-Variance Optimization (MVO) | 8.429 | 10.609 | 0.938 | 10.062 | 0.972 | 1.071 |
| Standard PPO | 13.018 ± 1.18 | 16.586 ± 1.52 | 0.630 ± 0.06 | 17.814 ± 1.24 | 0.731 ± 0.07 | 1.053 ± 0.10 |
| PPO-AXT (Fixed Aux Tasks) | 12.191 ± 1.10 | 15.553 ± 1.42 | 0.722 ± 0.06 | 17.862 ± 1.25 | 0.684 ± 0.07 | 1.263 ± 0.11 |
| Deep Scalper | 14.336 ± 1.25 | 18.592 ± 1.64 | 0.686 ± 0.06 | 17.995 ± 1.28 | 0.773 ± 0.07 | 1.254 ± 0.11 |
| **QUESTrader (Proposed)** | **19.164 ± 1.36** | **24.596 ± 1.79** | **1.124 ± 0.08** | 12.165 ± 0.92 | **1.575 ± 0.12** | **1.774 ± 0.13** |

#### 3. BSE Sensex (Table 4)
| Model | Annual Return (%) | Cumulative Return (%) | Sharpe Ratio | Max Drawdown (%) | Calmar Ratio | Sortino Ratio |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Buy-and-Hold | 5.461 | 6.768 | 0.482 | 15.721 | 0.411 | 0.614 |
| Sensex Index Benchmark | 6.663 | 8.175 | 0.538 | 15.757 | 0.422 | 0.741 |
| Mean-Variance Optimization (MVO) | 7.830 | 9.652 | 0.703 | 18.076 | 0.433 | 1.034 |
| Standard PPO | 11.948 ± 1.08 | 14.791 ± 1.37 | 0.768 ± 0.06 | 10.653 ± 0.85 | 1.121 ± 0.10 | 1.129 ± 0.10 |
| DREB Baseline | 15.138 ± 1.31 | 18.802 ± 1.63 | 0.916 ± 0.07 | 13.089 ± 0.97 | 1.156 ± 0.10 | 1.341 ± 0.11 |
| Deep Scalper | 13.423 ± 1.18 | 16.642 ± 1.47 | 0.856 ± 0.07 | 17.783 ± 1.27 | 0.754 ± 0.07 | 1.221 ± 0.11 |
| **QUESTrader (Proposed)** | **16.727 ± 1.21** | **20.809 ± 1.54** | **1.003 ± 0.07** | 10.584 ± 0.79 | **1.263 ± 0.10** | **1.488 ± 0.11** |

#### 4. Taiwan Capitalization Weighted Index (TAIEX, Table 5)
| Model | Annual Return (%) | Cumulative Return (%) | Sharpe Ratio | Max Drawdown (%) | Calmar Ratio | Sortino Ratio |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Buy-and-Hold | 15.937 | 19.053 | 0.874 | 15.097 | 0.910 | 1.184 |
| TAIEX (TWII) Benchmark | 17.554 | 20.991 | 0.893 | 18.692 | 0.939 | 1.173 |
| Mean-Variance Optimization (MVO) | 18.007 | 21.468 | 1.738 | 8.065 | 2.173 | 2.171 |
| Standard PPO | 21.513 ± 1.96 | 25.718 ± 2.19 | 1.001 ± 0.08 | 19.525 ± 1.33 | 1.102 ± 0.10 | 1.490 ± 0.12 |
| VS-DRL Baseline | 25.987 ± 2.21 | 31.173 ± 2.64 | 1.038 ± 0.09 | 21.581 ± 1.42 | 1.204 ± 0.11 | 1.519 ± 0.13 |
| Deep Scalper | 26.833 ± 2.25 | 32.740 ± 2.71 | 1.236 ± 0.10 | 16.231 ± 1.14 | 1.653 ± 0.14 | 1.860 ± 0.15 |
| **QUESTrader (Proposed)** | **30.279 ± 2.01** | **38.603 ± 2.58** | **1.803 ± 0.11** | 13.632 ± 0.96 | **2.559 ± 0.16** | **2.310 ± 0.15** |

### Independently reproduced

`not independently reproduced`

### Negative evidence

1. **Failure of Fixed Hand-Crafted Auxiliary Tasks (PA-AXT / PPO-AXT):**
   When auxiliary tasks are fixed a priori to predict technical targets or rolling price returns over rigid horizons (e.g., PPO-AXT or PA-AXT), performance lags behind discovered GVFs and in some regimes falls below standard unassisted PPO. On FTSE 100, PPO-AXT produced a Sharpe ratio of $0.722 \pm 0.06$ and a maximum drawdown of $17.862\%$, whereas QUESTrader achieved a Sharpe of $1.124 \pm 0.08$ and drawdown of $12.165\%$. Fixed auxiliary targets introduce severe gradient interference when volatility or trend regimes deviate from the pre-specified target structure.
2. **Failure of Small Auxiliary Question Banks ($d_q \le 4$):**
   Ablation studies on DJI demonstrate that with only $d_q = 2$ questions, the Sharpe ratio collapses to its lowest value ($\approx 0.9$), and total return remains low ($15\text{–}16\%$). With $d_q = 4$, Sharpe improves only marginally to $\approx 1.0$. Restricting the question bank starves the representation of multi-dimensional market dynamics.
3. **Failure of Oversized Question Banks ($d_q \ge 128$):**
   Increasing $d_q$ beyond 64 to 128 degrades the Sharpe ratio from $\approx 1.4$ down to $\approx 1.15$, and cumulative return drops from $28\%$ to $21\%$. The authors attribute this decay to task redundancy, excessive multi-head parameter contention, and bootstrap variance accumulation in the GVF TD loss.
4. **Failure of Myopic Meta-Updates ($K = 1, 2$):**
   Single-step unrolling ($K = 1$) fails to capture the intertemporal benefit of representation learning, resulting in low Sharpe ($\approx 0.9$) and minimal return ($14\%$).
5. **Degradation under Excessive Unrolling ($K = 50$):**
   Expanding the inner unroll to $K = 50$ steps causes total return to drop from $28\%$ (at $K = 20$) to $23\%$, while Sharpe flattens around $1.2$. Very long inner unrolls inflate meta-gradient variance, accumulate truncation errors, and cause the behavioral policy trajectory to drift outside the valid PPO clipping trust region.
6. **Friction Sensitivity Under Real-World Market Impact:**
   The evaluation assumes zero slippage and zero market impact. For less liquid mid-cap constituents in Sensex or TAIEX, frequent multi-asset rebalancing at the daily close would incur bid-ask spread crossing costs and liquidity concessions that would materially narrow the observed margin of outperformance.

## Falsification plan

1. **Meta-Gradient Disablement Placebo Test:**
   - *Procedure:* Replace the non-myopic meta-gradient update with: (a) a static randomly initialized question network, and (b) a question network updated via pure Gaussian noise perturbations $\eta_{t+1} = \eta_t + \epsilon_t$.
   - *Falsification Rule:* If the random or static GVF network matches or exceeds QUESTrader's Sharpe ratio within $\pm 0.05$ across all four equity datasets, falsify the hypothesis that non-myopic meta-gradients actively discover meaningful auxiliary questions.
2. **Stationary / Shuffled Label Ablation Test:**
   - *Procedure:* Train QUESTrader on cross-sectionally permuted stock returns to break causal cross-asset lead-lag relationships while preserving individual stock return distributions.
   - *Falsification Rule:* If the policy achieves positive excess returns over Buy-and-Hold on cross-sectionally shuffled data, reject the claim of true alpha extraction and attribute performance to backtest overfitting.
3. **Transaction Fee Stress Test:**
   - *Procedure:* Stress-test the execution environment by varying proportional transaction fees from $\delta = 10\text{ bps}$ to $20, 30, 50,$ and $100\text{ bps}$.
   - *Falsification Rule:* If QUESTrader's Sharpe ratio drops below the passive Buy-and-Hold benchmark at fees $\le 30\text{ bps}$, classify the strategy as a high-turnover artifact unsuitable for production deployment.
4. **Out-of-Sample Walk-Forward Holdout Test:**
   - *Procedure:* Freeze the trained model weights and evaluate forward out-of-sample trading performance on daily data from April 1, 2025 through September 2026 without retraining.
   - *Falsification Rule:* If annualized out-of-sample Sharpe drops below $0.5$ or maximum drawdown exceeds $25\%$, reject out-of-sample policy stability.

## Crypto portability

- **Portability Status:** `adapted` / `unproven`
- **Crypto-Specific Structural Divergences & Risks:**
  - *24/7 Session vs. Daily Closing Bells:* Equity trading decisions occur at discrete 16:00 local closing auctions. In crypto, markets trade continuously 24/7. Applying QUESTrader requires establishing arbitrary UTC cutoffs (e.g., 00:00 UTC) or migrating to intraday observation intervals (e.g., 1-hour or 4-hour bars), which alters technical indicator periodicity and serial autocorrelation.
  - *Perpetual Futures Funding Cashflows:* In crypto perpetual contracts, positions incur dynamic 8-hour funding payments. The reward function $r(s_t, a_t) = (P_{t+1} - P_t) \cdot a_t - \delta P_t \cdot |\Delta a_t|$ ignores funding carry. Crowded long exposure during high-funding regimes would severely erode portfolio net equity.
  - *Tail Kurtosis & Flash Crash Dynamics:* Cryptocurrency markets experience sudden, cascading liquidation unwinds (e.g., March 2020 or FTX collapse). In such regimes, gradient updates in PPO can suffer variance spikes. The GVF bank must dynamically downweight discount factors $\gamma_t$ during volatility shocks to avoid propagating corrupted credit.
  - *Liquidation & Margin Constraints:* Unlike unlevered cash equities with simple integer holdings $[-m, m]$, perpetual trading requires dynamic maintenance margin and cross-collateral accounting. A policy without explicit liquidation penalty boundaries risks margin call liquidations.

## Limitations

- **Not Independently Reproduced:** All performance figures, Sharpe ratios, and ablation statistics are sourced from academic preprint arXiv:2608.15841v1.
- **Survivorship & Constituent Selection Bias:** The study selects the top 30 stocks from each index as of the collection date and applies them retroactively across the 2010–2025 period, introducing look-ahead survivorship bias by excluding historical index constituents that were delisted or acquired.
- **Unmodeled Market Impact & Slippage:** Execution is assumed to take place at the exact closing price with zero slippage. In real market execution, executing large rebalances simultaneously across 30 names at the close incurs market impact.
- **High Computational Overhead:** Unrolling inner updates over $K = 10\text{–}20$ steps requires maintaining computation graphs in memory for higher-order gradient differentiation, which severely constrains real-time intraday deployment and extensive multi-asset scaling.

## Implementation status

`not-implemented`. No implementation in PyBroker, NautilusTrader, or any paper/live trading environment has been conducted.

## Adoption boundary

`research-only`, `not-approved`. This document serves strictly as normalized research capture. It does not authorize capital deployment, paper trading, testnet execution, or live operational implementation.

## Related Wiki records

- `[[alphazerobeta-recurrent-ppo-market-neutral-portfolio-2026-09-02]]`
- `[[crypto-drl-execution-overlay-multi-pair-trading-2026-09-01]]`
- `[[finsmart-market-aligned-reinforcement-learning-sentiment-alpha-2026-09-02]]`
- `[[regime-adaptive-continual-learning-portfolio-management-recap-2026-09-02]]`
- `[[sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02]]`

## Sources

1. Arishi Orra, Himanshu Choudhary, and Manoj Thakur, *"Self-Supervised Auxiliary Task Discovery for Stable Reinforcement Learning in Stock Trading"*, arXiv preprint `arXiv:2608.15841v1 [q-fin.TR, cs.LG]`, submitted August 16, 2026. DOI: [https://doi.org/10.48550/arXiv.2608.15841](https://doi.org/10.48550/arXiv.2608.15841). Full text: [https://arxiv.org/abs/2608.15841](https://arxiv.org/abs/2608.15841), HTML: [https://arxiv.org/html/2608.15841v1](https://arxiv.org/html/2608.15841v1), PDF: [https://arxiv.org/pdf/2608.15841](https://arxiv.org/pdf/2608.15841).
