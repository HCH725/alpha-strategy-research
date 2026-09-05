---
schema: strategy-research-record-v1
title: "Sentiment-Augmented Deep Reinforcement Learning for Active Trading with Excess Alpha-Reward Formulation and Discretized DDPG Policy"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - deep-reinforcement-learning
  - ddpg
  - dql
  - alpha-reward
  - sentiment-analysis
  - llama-3.2
  - btc
  - tsla
  - market-regime-shift
status: research-only
confidence: medium
source_as_of: "2026-07-20"
sources:
  - "Andrei Neagu, Eeham Khan, Leila Kosseim, 'CLaC@FinMMEval 2026 Task 3: Sentiment-Augmented Deep Reinforcement Learning for Active Trading -- An Alpha-Reward Approach', arXiv:2607.16028v1 [cs.LG, q-fin.TR], submitted 17 July 2026. CLEF 2026 FinMMEval Lab Task 3 Merit Award. https://arxiv.org/abs/2607.16028"
  - "TheFinAI / CLEF Task 3 Trading Dataset, Hugging Face: https://huggingface.co/datasets/TheFinAI/CLEF_Task3_Trading"
  - "Brian Ferrell, Financial-News-Multisource Dataset, Hugging Face: https://huggingface.co/datasets/Brianferrell787/financial-news-multisource (revision b509ef6, DOI: 10.57967/hf/6432)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Sentiment-Augmented Deep Reinforcement Learning for Active Trading with Excess Alpha-Reward Formulation and Discretized DDPG Policy

## Provenance

- **Title:** CLaC@FinMMEval 2026 Task 3: Sentiment-Augmented Deep Reinforcement Learning for Active Trading -- An Alpha-Reward Approach
- **Authors:** Andrei Neagu, Eeham Khan, and Leila Kosseim (CLaC Laboratory, Department of Computer Science and Software Engineering, Concordia University, Montreal, Canada)
- **Publication Identifier:** arXiv:2607.16028v1 [cs.LG, q-fin.TR]
- **Submission Date:** 17 July 2026
- **Conference / Workshop:** CLEF 2026 FinMMEval Lab Task 3 (Financial Decision Making), awarded Merit Award
- **Canonical arXiv URL:** `https://arxiv.org/abs/2607.16028` / `https://arxiv.org/html/2607.16028`
- **External Data Sources:**
  - Daily equity & crypto OHLCV from Yahoo Finance (`yfinance` Python library)
  - Financial news text from Brian Ferrell's `financial-news-multisource` Hugging Face dataset (DOI: 10.57967/hf/6432, revision b509ef6)
  - Official evaluation benchmark from CLEF Task 3 Hugging Face dataset (`TheFinAI/CLEF_Task3_Trading`)
- **Code Release:** All code, trained model checkpoints, hyperparameter configurations, and data preprocessing scripts are designated for open-source release upon paper acceptance (`source-reported`).

## Economic mechanism

### Source-reported

Financial markets present non-stationary, noisy sequential decision environments with heterogeneous multi-modal information (price action, volume dynamics, cyclical calendar seasonality, and textual news flow). Traditional rule-based strategies and standard supervised forecasting models often fail to optimize multi-period cumulative wealth under transaction costs.

The authors formulate active daily trading as a discrete-action Markov Decision Process (MDP) for single assets (evaluating Bitcoin [BTC] and Tesla [TSLA]). The central theoretical and economic mechanism is the **alpha reward**:
- Rather than optimizing raw portfolio log-returns $\log(V_t / V_{t-1})$, the reward function explicitly measures excess return relative to the buy-and-hold market benchmark:
  $$r_t = \log\left(\frac{V_t}{V_{t-1}}\right) - \log\left(\frac{c_t}{c_{t-1}}\right) = \log\left(\frac{V_t}{V_{t-1}}\right) - m_t$$
  where $m_t = \log(c_t / c_{t-1})$ represents the market log-return.
- **Telescoping Cumulative Alpha Identity:** Over an undiscounted episode of length $T$, the per-step rewards sum exactly to the terminal log-outperformance:
  $$\sum_{t=1}^T r_t = \log\left(\frac{V_T}{V_0}\right) - \log\left(\frac{c_T}{c_0}\right) = \log(\alpha_T)$$
  where $\alpha_T = (V_T / V_0) / (c_T / c_0)$ is the terminal outperformance ratio over buy-and-hold.
- **Optimal Policy Equivalence:** Under the exogenous price-taker assumption, the market return sequence $\{m_t\}$ is independent of the agent's policy $\pi_\theta$. The alpha-reward objective differs from the raw log-return objective only by a policy-independent expectation term $\mathbb{E}[\sum_t \gamma^{t-1} m_t]$, proving that the two objectives share identical optimal policies $\pi^*$.
- **Control Variate & Variance Reduction:** For long positions with zero trade turnover, $\log(V_t / V_{t-1}) = m_t$, meaning the alpha reward has variance zero, whereas the raw return reward has variance $\mathrm{Var}(m_t)$. Subtracting the market return $m_t$ acts as a zero-bias control variate, drastically reducing the gradient estimator variance on highly volatile assets (e.g., BTC and TSLA annualized volatilities exceeding 60%).
- **Multi-Modal Information Fusion:** Technical trend (EMA10, EMA50), momentum (RSI14, MACD), dynamic volatility (BollingerB), volume flow ($\log(V_t / V_{t-1})$), cyclical calendar harmonics, and zero-shot LLM news sentiment (LLaMA 3.2 1B Instruct log-probability differences) provide orthogonal features that guide the RL agent's timing.

### Research interpretation

The alpha reward fundamentally alters the exploration landscape of deep reinforcement learning agents in trending asset classes. In a strong bull market, standard RL agents trained on raw returns learn a "lazy long" policy because holding the underlying asset trivially accumulates positive rewards, reinforcing positive feedback even for suboptimal entry and exit timing. By enforcing a baseline return of zero for passive holding, the alpha reward forces the policy to earn its reward purely through active market timing (reducing exposure or going flat ahead of downturns, and entering short positions when downward momentum is confirmed).

However, the empirical evidence also illustrates a structural vulnerability in reinforcement learning applied to non-stationary financial data: **regime-shift misallocation**. When policies are selected via validation Sharpe ratio over a sustained bull market recovery (2023–2024), value-based off-policy learners like Deep Q-Learning (DQL) overfit to aggressive upward drift. When the market regime switches to a sustained bear trend (as BTC did in the 2025–2026 test period), policies optimized for bull momentum experience severe drawdowns, whereas actor-critic architectures with continuous action spaces and replay buffers (DDPG) demonstrate greater resilience by smoothly shifting continuous policy outputs toward cash and short allocations.

## Signal

### State Feature Representation (15-Dimensional Vector)

Each daily decision step $t$ conditions on a 15-dimensional state vector $\mathbf{s}_t \in \mathbb{R}^{15}$ composed of four groups (`source-reported`):

1. **Price & Portfolio State (2 features):**
   - Immediate price change: LogReturn = $\log(c_t / c_{t-1}) \in \mathbb{R}$
   - Previous agent allocation: Position $p_{t-1} \in \{-1, 0, 1\}$ (enables the policy to learn execution inertia and avoid churning when expected edge is below transaction cost $\delta = 0.002$)
2. **Cyclical Calendar Features (6 features):**
   - Day of Week (DoW): $\sin(2\pi \cdot \text{DoW} / 7)$, $\cos(2\pi \cdot \text{DoW} / 7) \in [-1, 1]$
   - Day of Month (DoM): $\sin(2\pi \cdot \text{DoM} / 31)$, $\cos(2\pi \cdot \text{DoM} / 31) \in [-1, 1]$
   - Month of Year (MoY): $\sin(2\pi \cdot \text{MoY} / 12)$, $\cos(2\pi \cdot \text{MoY} / 12) \in [-1, 1]$
3. **Normalized Technical Indicators (6 features):**
   - Short-term trend: $\text{EMA}_{10} / c_t - 1 \in \mathbb{R}$
   - Medium-term trend: $\text{EMA}_{50} / c_t - 1 \in \mathbb{R}$
   - Momentum oscillator: $\text{RSI}_{14} / 50 - 1 \in [-1, 1]$ (neutral at 0, overbought > 0.4, oversold < -0.4)
   - Trend acceleration: Normalized MACD histogram $(\text{EMA}_{12} - \text{EMA}_{26} - \text{signal}_9) / c_t \in \mathbb{R}$
   - Adaptive volatility band: $\text{BollingerB} = (c_t - \text{SMA}_{20}) / (2 \sigma_{20}) \in \mathbb{R}$
   - Volume shift: $\text{LogVolumeChange} = \log(V_t / V_{t-1}) \in \mathbb{R}$
4. **LLM Zero-Shot Sentiment Score (1 feature):**
   - Model: LLaMA 3.2 1B Instruct (`source-reported`)
   - Text conditioning: Article headline + lede truncated to the first 300 words (`source-reported`)
   - Prompt format: Structured classification prompt prompting the model to categorize the tone of the article as positive, negative, or neutral for the target asset (`source-reported`)
   - Log-probability extraction: Logits extracted at the final token position across BPE variants with/without leading space and case variants; softmax applied over class token unions to obtain $P(\text{positive})$, $P(\text{negative})$, and $P(\text{neutral})$ (`source-reported`)
   - Daily score: $\text{Sentiment}_i = P(\text{positive}) - P(\text{negative}) \in [-1, 1]$ for article $i$; aggregated as the daily mean across all filtered articles on trading day $t$ (`source-reported`)

### Trading Action Space & Execution Mapping

- **Discrete Action Space:** $\mathcal{A} = \{\text{short } (-1), \text{flat } (0), \text{long } (1)\}$ (`source-reported`).
- **DDPG Policy Discretization:**
  - DDPG actor network $\mu_\theta(\mathbf{s}_t)$ outputs a continuous scalar $a_t \in [-1, 1]$.
  - Discretization rule (`source-reported`):
    $$p_t = \begin{cases} -1 & \text{if } a_t < -0.33 \quad (\text{short}) \\ +1 & \text{if } a_t > 0.33 \quad (\text{long}) \\ 0 & \text{if } -0.33 \le a_t \le 0.33 \quad (\text{flat / cash}) \end{cases}$$
  - The threshold value $1/3 \approx 0.33$ partitions the actor output range $[-1, 1]$ into three equal-width intervals, ensuring symmetric prior probability mass without directional bias (`source-reported`).
- **DQL Policy Selection:**
  - $p_t = \arg\max_{a \in \{-1, 0, 1\}} Q(s_t, a; \theta)$ (`source-reported`).
- **Cadence & Holding Period:** Daily rebalancing. Positions are held until the policy outputs a different state.
- **Position Sizing:** Fixed discrete allocation: $100\%$ long, $100\%$ short, or $100\%$ cash/flat (`source-reported`). Continuous fractional Kelly scaling or volatility targeting is omitted in the primary paper (`research-proposed` enhancement).

## Required data

- **Instruments:**
  - Bitcoin spot: BTC-USD (`source-reported`)
  - Tesla common stock: TSLA (`source-reported`)
- **Venues / Data Sources:**
  - Price & Volume: Yahoo Finance (`yfinance` API) (`source-reported`)
  - News Articles: Brian Ferrell's Financial News Multi-Source dataset on Hugging Face; CLEF Task 3 Hugging Face dataset (`source-reported`)
- **Timeframes & Data Splits:**
  - Training Period:
    - TSLA: 2010-06-29 to 2022-12-30 (2,835 trading days; 57,741 filtered news articles) (`source-reported`)
    - BTC: 2014-09-17 to 2022-12-30 (2,664 trading days; 29,307 filtered news articles) (`source-reported`)
  - Validation Period:
    - TSLA: 2023-01-01 to 2024-08-01 (324 trading days; 7,089 filtered news articles) (`source-reported`)
    - BTC: 2023-01-01 to 2024-08-01 (457 trading days; 2,861 filtered news articles) (`source-reported`)
  - Test Period (CLEF Task 3 Official Evaluation Window):
    - 2025 to 2026-04-12 (256 trading days for both assets) (`source-reported`)
- **Point-in-Time & Information Alignment:**
  - TSLA Equity: All article timestamps recorded in UTC. Articles published after 16:00 UTC (U.S. market close) are shifted to day $t+1$ (`source-reported`).
  - BTC Crypto: 24/7 continuous session anchored to 00:00–23:59:59 UTC calendar date; articles timestamped on day $t$ linked to day $t$ close (`source-reported`).
  - Warmup Window: Initial 60 days discarded from training to initialize rolling indicators (EMA50); last 60 days of validation prepended to test set for warmup then truncated prior to evaluation (`source-reported`).
- **Text Filtering & Deduplication:**
  - Regex keyword filter requires $\ge 2$ mentions of target asset (Tesla/TSLA or Bitcoin/BTC) across the text or $\ge 1$ mention in the first 100 words (the lede) (`source-reported`).
  - MD5 hash of lowercased, punctuation-stripped text used to remove duplicates; metadata-rich entries prioritized (`source-reported`).
- **Missing Data Handling:**
  - If zero news articles pass filters on day $t$, daily sentiment score defaults to $0.0$ (`research-proposed`).

## Execution assumptions

- **Portfolio Multiplicative Transition:**
  $$V_t = V_{t-1} \cdot (1 + p_{t-1} \cdot \text{return}_t) \cdot (1 - \delta \cdot \mathbf{1}_{\{a_t \neq p_{t-1}\}})$$
  where $\text{return}_t = (c_t - c_{t-1}) / c_{t-1}$ (`source-reported`).
- **Transaction Costs ($\delta$):**
  - Training: $\delta = 0.002$ ($20 \text{ bps}$ per position flip) applied during training episodes to penalize churning (`source-reported`).
  - Evaluation / Test Backtest: $\delta = 0.0$ ($0 \text{ bps}$) during test evaluation to strictly comply with the CLEF Task 3 competition protocol (`source-reported`; explicitly cited by authors as an external validity limitation).
- **Execution Price:** Executed on daily close price $c_t$; order placed based on information available at $t$, taking effect for period $t \to t+1$ (`source-reported`).
- **Shorting Mechanism:** Assumes frictionless symmetric shorting where short return equals $-1 \cdot \text{return}_t$ (`source-reported`). No borrow fee, margin interest, or short rebate modeled (`source-reported`).
- **Slippage & Market Impact:** Not modeled; assumes infinite liquidity at closing price (`source-reported`).

## Evidence

### Source-reported

Empirical results from Neagu, Khan, and Kosseim (arXiv:2607.16028, CLEF 2026 FinMMEval Lab Task 3):

#### 1. Baseline Market Regimes across Splits (Table 2 in source)

| Asset | Split | Period | Days | Articles | Cumul. Ret. (%) | Ann. Ret. (%) | Ann. Vol. (%) | Sharpe Ratio |
|---|---|---|---|---|---|---|---|---|
| **TSLA** | Training | 2010–2022 | 2,835 | 57,741 | +7,634.2% | 47.2% | 60.3% | 0.94 |
| | Validation | 2023–2024 | 324 | 7,089 | +105.9% | 75.4% | 60.2% | 1.24 |
| | Test | 2025–2026 | 256 | — | +16.5% | 16.2% | 34.9% | 0.61 |
| **BTC** | Training | 2014–2022 | 2,664 | 29,307 | +3,518.3% | 40.4% | 65.0% | 0.85 |
| | Validation | 2023–2024 | 457 | 2,861 | +288.7% | 111.4% | 43.3% | 1.95 |
| | Test | 2025–2026 | 256 | — | -34.3% | -33.8% | 39.1% | -0.87 |

#### 2. Test Set Performance Comparison (Table 10 in source, 256 test days)

| Asset | Model | Test CR (%) | Test SR | Val CR (%) | Val SR | MDD (%) | Daily Vol (%) | Ann. Vol (%) |
|---|---|---|---|---|---|---|---|---|
| **TSLA** | **Buy & Hold (B&H)** | 16.45% | 0.61 | 105.94% | 1.24 | 29.93% | 2.19% | 34.80% |
| | **Policy Gradient (PG)** | 13.96% | 0.55 | 101.76% | 1.21 | 29.93% | 2.19% | 34.74% |
| | **PPO** | 2.54% | 0.24 | 169.50% | 1.75 | 28.38% | 2.01% | 31.93% |
| | **DQL** | 52.62% | 1.38 | 830.30% | 3.29 | 35.76% | 2.19% | 34.69% |
| | **DDPG (Discretized)** | **54.96%** | **1.44** | 262.10% | 2.03 | **19.20%** | 2.15% | 34.09% |
| **BTC** | **Buy & Hold (B&H)** | -34.27% | -0.87 | 288.69% | 1.95 | 49.72% | 2.46% | 39.00% |
| | **Policy Gradient (PG)** | -14.53% | -0.33 | 109.33% | 1.43 | **29.98%** | 1.98% | 31.51% |
| | **PPO** | -33.80% | -0.85 | 190.07% | 1.58 | 59.18% | 2.46% | 39.00% |
| | **DQL** | -23.22% | -0.55 | 276.71% | 2.11 | 37.41% | 2.25% | 35.72% |
| | **DDPG (Discretized)** | **+1.58%** | **0.23** | 259.53% | 1.87 | 35.30% | 2.40% | 38.12% |

#### 3. Key Empirical Findings
- **DDPG Dominance:** DDPG ranked first on both assets in Test Cumulative Return and Test Sharpe Ratio. On TSLA, it achieved $+54.96\%$ vs $+16.45\%$ B&H with a reduced maximum drawdown ($19.20\%$ vs $29.93\%$). On BTC, DDPG was the only algorithm to deliver a positive return ($+1.58\%$, SR $0.23$) during a severe bear market where B&H fell $-34.27\%$ (SR $-0.87$).
- **PPO Training Overfitting:** PPO reported astronomical training-episode returns ($+114,462\%$ on TSLA, $+256,989\%$ on BTC), but collapsed on out-of-sample evaluation ($+2.54\%$ on TSLA, $-33.80\%$ on BTC), demonstrating severe path-memorization failure.
- **Regime-Shift Generalization Gap:** DQL achieved the highest validation Sharpe ratio on both TSLA ($3.29$) and BTC ($2.11$) and was selected a priori as the competition submission model. While DQL performed strongly on TSLA ($52.62\%$), it collapsed on BTC ($-23.22\%$, SR $-0.55$), revealing that bull-market validation checkpoints fail when deployed into bear-market test regimes.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Cost-Free Test Evaluation Bias:** Test results were computed with zero transaction costs ($\delta = 0$) per CLEF Task 3 rules. If realistic crypto/equity execution costs (5–10 bps per trade) and continuous turnover are deducted, DDPG's modest $+1.58\%$ return on BTC over 256 days would likely be erased.
- **Validation-to-Test Regime Brittleness:** Selecting models solely on validation Sharpe ratio over a bull regime (2023–2024) selected DQL, which suffered a $-23.22\%$ loss during the BTC bear test regime. Single-window validation fails to protect against macro regime shifts.
- **Failure of Recurrent On-Policy RL:** Neither recurrent PG nor PPO generated positive returns on BTC, with PPO matching the bear market drawdown ($-59.18\%$ MDD vs $-49.72\%$ B&H).
- **Missing Feature Ablation:** The paper did not perform ablation experiments removing sentiment scores or technical indicators. Consequently, the incremental alpha contribution of LLaMA 3.2 1B sentiment versus the 14 price/volume/calendar features remains unproven.

## Falsification plan

To falsify the hypothesis that sentiment-augmented DRL with alpha-reward formulation generates persistent risk-adjusted excess returns, the following empirical tests are specified:

1. **Feature Ablation Test (Sentiment Value-Add):**
   - Retrain DDPG under the identical Ray Tune search budget using only the 14 market/calendar features (setting sentiment to constant zero).
   - `research-defined falsification threshold`: If the technical-only DDPG achieves equal or higher out-of-sample Sharpe ratio than the sentiment-augmented model over a 3-year rolling window, the hypothesis that LLM news sentiment provides incremental alpha is falsified.
2. **Transaction Cost & Slippage Hurdle Test:**
   - Re-evaluate test episodes applying realistic institutional fee structures: 5 bps maker/taker fee + 5 bps linear slippage per position flip ($\delta = 0.001$).
   - `research-defined falsification threshold`: If DDPG net cumulative return on BTC drops below $-10.0\%$ or TSLA net return falls below buy-and-hold, the tradability of the active signal is falsified as a cost-frictional illusion.
3. **Walk-Forward Cross-Validation (Regime Invariance Test):**
   - Implement a 5-fold rolling walk-forward cross-validation spanning bull (2020–2021), bear (2022), and recovery (2023–2024) regimes.
   - `research-defined falsification threshold`: If DDPG produces negative annualized Sharpe ratios on $\ge 40\%$ of out-of-sample test folds, the claim of cross-regime learning stability is falsified.
4. **Placebo / Shuffled Sentiment Test:**
   - Randomly permute daily sentiment scores across dates while keeping price/volume series synchronized.
   - `research-defined falsification threshold`: If a policy trained on shuffled sentiment achieves test Sharpe within $0.10$ of the true sentiment policy ($p > 0.10$ via two-tailed t-test over 10 random seeds), the sentiment signal is falsified as spurious noise fitting.
5. **Alpha Reward vs. Raw Log-Return Control Test:**
   - Train DDPG using raw log-return $r_t = \log(V_t / V_{t-1})$ under identical hyperparameter seeds.
   - `research-defined falsification threshold`: If raw reward training converges in the same number of gradient steps and achieves equal validation stability, the theoretical variance-reduction advantage of the alpha reward is falsified in practice.

## Crypto portability

**Portability Classification:** `adapted`

The primary paper evaluates Bitcoin (BTC-USD) directly, but treats it using daily closing prices in an idealized spot framework without modeling the structural mechanics of real-world cryptocurrency markets. Porting this strategy to institutional crypto execution requires addressing key market microstructure differences:

1. **Spot vs. Perpetual Swap Dynamics:** Institutional active crypto trading primarily utilizes perpetual swaps. Holding short or long positions introduces 8-hour funding rate payments. During prolonged bull regimes, long positions incur negative carry from high positive funding; during bear runs, short positions receive funding. These cash flows are completely omitted in the paper's equation (`research-proposed`).
2. **24/7 Session & Timestamp Boundary:** BTC trades 24/7/365 without market closes. The paper anchors daily bars to 00:00 UTC. Intra-day volatility spikes and liquidity cycles across Asian, European, and US sessions can significantly alter execution timing relative to fixed daily prints (`research-proposed`).
3. **Exchange Fragmentation & Mark Price Liquidation:** Unlike TSLA listed on NASDAQ, BTC trading is fragmented across Binance, Bybit, OKX, and Coinbase. Order execution must model basis spreads between mark price, index price, and order book depth (`research-proposed`).
4. **Execution Slippage & Market Impact:** In high-volatility regimes (e.g., market corrections where BTC daily drops exceed 10%), instantaneous liquidity vanishes, rendering closing-price fills unrealistic (`research-proposed`).

## Limitations

- **Underspecified Code Release:** Preprocessing regex strings, exact deduplication scripts, and random trial seeds are scheduled for release upon formal paper acceptance; exact reproduction requires wait for open-source repository release.
- **Cost-Free Test Evaluation:** Testing under zero execution fees artificially inflates returns of active rebalancing strategies relative to passive buy-and-hold.
- **Single Bull-Market Validation Split:** Validating on 2023–2024 induced severe bull-market bias, causing the a priori chosen competition model (DQL) to suffer severe losses during the BTC bear regime.
- **Coarse Action Space:** Discrete $\{-1, 0, 1\}$ action mapping prevents dynamic risk targeting, position scaling, or volatility-adjusted exposure.
- **1B Parameter LLM Limitation:** LLaMA 3.2 1B Instruct zero-shot log-probability difference over truncated 300-word ledes is a relatively coarse sentiment proxy that may miss subtle multi-paragraph financial context.

## Implementation status

`not-implemented`

This strategy has not been implemented or validated in our quantitative backtesting stack (`nautilus-quant-system` or `PyBroker`). It is documented here strictly as normalized research material.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

This record is an upstream academic research capture. Inclusion in this repository does not constitute evidence of live profitability, approval for production implementation, or permission for paper, testnet, or live trading deployment.

## Related Wiki records

- `[[quant/finsmart-market-aligned-reinforcement-learning-sentiment-alpha-2026-09-02]]` — Market-aligned reinforcement learning with sentiment rewards, but using FinBERT and continuous trading actions without alpha excess return identity.
- `[[quant/crypto-hourly-bitcoin-walk-forward-cost-aware-execution-2026-09-01]]` — Evaluates walk-forward ML forecasting on BTC with transaction cost sensitivity.
- `[[quant/sentiment-vader-technical-indicator-mean-variance-crypto-portfolio-2026-09-04]]` — Combines sentiment scores with classical technical indicators in cryptocurrency portfolio optimization.
- `[[quant/webcryptoagent-web-informatics-two-tier-agentic-crypto-2026-09-05]]` — Two-tier agentic architecture combining strategic LLM reasoning and high-frequency risk controls for crypto trading.

## Sources

1. Andrei Neagu, Eeham Khan, Leila Kosseim. "CLaC@FinMMEval 2026 Task 3: Sentiment-Augmented Deep Reinforcement Learning for Active Trading -- An Alpha-Reward Approach." arXiv:2607.16028v1 [cs.LG, q-fin.TR], submitted 17 July 2026. CLEF 2026 FinMMEval Lab Task 3 Merit Award. URL: `https://arxiv.org/abs/2607.16028` / `https://arxiv.org/html/2607.16028`.
2. TheFinAI / CLEF Task 3 Trading Dataset. Hugging Face dataset repository: `https://huggingface.co/datasets/TheFinAI/CLEF_Task3_Trading`. Reference: Xie et al. (2026b), "Overview of the FinMMEval 2026 task 3: financial decision making," CLEF 2026 Working Notes.
3. Brian Ferrell. "Financial-news-multisource Dataset." Hugging Face repository: `https://huggingface.co/datasets/Brianferrell787/financial-news-multisource`, revision `b509ef6`, DOI: `10.57967/hf/6432` (2025).
