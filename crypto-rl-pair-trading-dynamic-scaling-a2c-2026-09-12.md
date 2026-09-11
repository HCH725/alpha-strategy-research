---
schema: strategy-research-record-v1
title: "Reinforcement Learning Pair Trading with Continuous Dynamic Scaling: Empirical Validation and Algorithmic Fragility on High-Frequency Crypto Pairs"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - statistical-arbitrage
  - pair-trading
  - reinforcement-learning
  - dynamic-scaling
  - continuous-action-space
  - advantage-actor-critic
  - transaction-costs
  - high-frequency
status: research-only
confidence: high
source_as_of: 2024-12-11
sources:
  - "Hongshen Yang and Avinash Malik, 'Reinforcement Learning Pair Trading: A Dynamic Scaling Approach', Journal of Risk and Financial Management (JRFM) 2024, 17(12), 555; DOI: 10.3390/jrfm17120555; arXiv:2407.16103v2 [q-fin.TR] (submitted July 23, 2024, accepted December 6, 2024, published December 11, 2024); Primary data: Binance Exchange 1-minute historical archives (https://data.binance.vision/)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Reinforcement Learning Pair Trading with Continuous Dynamic Scaling: Empirical Validation and Algorithmic Fragility on High-Frequency Crypto Pairs

## Provenance

- **Primary Source:** Published peer-reviewed research article in the *Journal of Risk and Financial Management* (JRFM), 2024, Volume 17, Issue 12, Article 555.
- **Authors:** Hongshen Yang and Avinash Malik (Department of Electrical, Computer, and Software Engineering, The University of Auckland, Auckland 1010, New Zealand).
- **Persistent Identifiers:**
  - DOI: `10.3390/jrfm17120555` (`https://doi.org/10.3390/jrfm17120555`)
  - arXiv Canonical URL: `https://arxiv.org/abs/2407.16103` (`arXiv:2407.16103v2 [q-fin.TR]`)
- **Primary Data Source:** Binance cryptocurrency exchange public historical tick and minute candlestick archives (`https://data.binance.vision/`, accessed November 8, 2024).
- **Source Publication and Data Window:** Received November 8, 2024; revised November 28, 2024; accepted December 6, 2024; published December 11, 2024. Data collection spans October 1, 2023 to December 31, 2023.
- **Deduplication Audit:** Audited all 482 existing strategy research records in `alpha-strategy-research`. Zero existing records reference Yang & Malik (2024), DOI `10.3390/jrfm17120555`, arXiv `2407.16103`, or high-frequency pair trading across Bitcoin cross-fiat quote pairs (`BTCEUR` vs. `BTCGBP`) using continuous dynamic scaling reinforcement learning. Existing repository records on statistical arbitrage (`crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12.md` and `statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05.md`) focus on daily altcoin cross-sectional residuals and equity LSTM factor replication, establishing clear independence.

## Economic mechanism

### Source-reported

1. **Statistical Arbitrage and Mean Reversion in Cross-Currency Crypto Pairs:**
   Cryptocurrency pair trading is a relative-value arbitrage technique that exploits temporary price discrepancies between statistically cointegrated assets. When two liquid instruments share common underlying economic exposure—such as Bitcoin denominated in Euro (`BTCEUR`) and British Pound (`BTCGBP`) on Binance—their price series exhibit a stable long-term equilibrium relationship driven by foreign exchange cross-rates and unified order book arbitrage. Localized liquidity imbalances, retail flow fragmentation, and discrete order arrivals cause the normalized price spread to temporarily deviate from its equilibrium mean. Arbitrageurs sell the relatively overpriced asset and buy the relatively underpriced asset, capturing profit as the spread mean-reverts.

2. **Inadequacy of Traditional Rule-Based and Static Pair Trading in High-Frequency Crypto:**
   Classical pair trading (à la Gatev, Goetzmann, and Rouwenhorst, 2006) operates on rigid, predefined thresholds (e.g., open at $\pm 2.0\sigma$, close at $0.0\sigma$) and executes fixed, binary capital allocations (either 100% in or 100% in cash). In volatile, 24/7 cryptocurrency markets, fixed thresholds fail to adjust to shifting volatility regimes, leading to prolonged drawdowns during regime shifts or missed opportunities during compressed volatility.

3. **Failure of Dynamic-Threshold-Only Reinforcement Learning (Kim & Kim, 2019):**
   Prior reinforcement learning pair trading literature (notably Kim and Kim, 2019) trained RL agents to adaptively predict upcoming entry/exit/stop-loss thresholds while retaining fixed-size trade execution. The source shows that this approach fails in cryptocurrency markets (yielding negative cumulative returns and negative Sharpe ratios across all tested algorithms), because threshold adjustment without position scaling cannot handle extreme volatility bursts where fixed-size bets are severely penalized by whipsaws.

4. **Continuous Dynamic Scaling Mechanism:**
   The paper introduces a novel dynamic scaling continuous MDP formulation ($\text{RL}_2$) where the RL agent simultaneously controls:
   - **Timing:** Selecting the exact bar to enter, adjust, or exit;
   - **Continuous Quantity Allocation ($A \in [-1, 1]$):** Sizing the portfolio allocation continuously based on opportunity quality and expected reversion probability.
   Rather than treating position management as binary all-or-nothing switches, the agent utilizes three execution modes: `open position`, `adjust position`, and `close position`. Under `adjust position`, when an existing position is open and the agent changes its target exposure (e.g., from $+0.70$ to $+0.80$), only the marginal delta ($0.10$ notional) is executed in the market. This structural innovation minimizes unnecessary portfolio churn, conserves transaction fees, and scales exposure up during high-conviction spread extremes.

### Research interpretation

- **Microstructure Basis in Triangulated Crypto-Fiat Order Books:**
  `BTCEUR` and `BTCGBP` represent identical underlying collateral (BTC) quoted against two fiat currencies. On a single exchange (Binance), deviations between $\frac{P(\text{BTCEUR})}{P(\text{BTCGBP})}$ and the prevailing EUR/GBP foreign exchange rate are bounded by triangular arbitrage and cross-currency market makers. High-frequency 1-minute deviations reflect temporary inventory imbalances across fiat order books rather than fundamental crypto valuation divergence.
- **The Turnover-Cost Drag Trap in Financial RL:**
  High-frequency RL agents frequently succumb to hyperactive churning: because reward functions award small incremental gains, naive policy gradient or Q-learning agents (such as PPO, DQN, and SAC) trade thousands of times per month, resulting in transaction costs completely devouring gross trading returns.
- **Selective Conviction Filtering via Advantage Actor-Critic (A2C):**
  A key empirical finding of this research is that among evaluated RL algorithms, only Advantage Actor-Critic (A2C) successfully converges to a conservative, high-conviction policy. A2C executes fewer trades ($229$ actions over $31$ days) with a high average win size ($+\$90.94$ USD vs. $-\$21.00$ USD loss), demonstrating that continuous dynamic scaling coupled with transaction-penalty reward shaping forces the neural policy to act as an opportunistic hurdle filter that only trades when expected mean reversion comfortably clears the round-trip fee barrier.

## Signal

The strategy signal pipeline consists of five operational stages (`source-reported`):

```text
[Stage 1: Pair Formation]
  - Pearson Correlation: rho(X, Y) >= 0.8
  - Engle-Granger Two-Step Cointegration Test: ADF test on residuals (p < 0.05)
            ↓
[Stage 2: Rolling Spread & Z-Score]
  - Rolling OLS regression over window W = 900 bars: p_i = beta_0 + beta_1 * p_j + s_i
  - Spread Z-score normalization: Z_t = (s_t - mean(s)) / std(s)
            ↓
[Stage 3: Parameter Selection (Grid Search on In-Sample Window)]
  - Optimal parameters: Window W = 900 min, Open Threshold = 1.8 sigma, Close Threshold = 0.4 sigma
            ↓
[Stage 4: State-Space Observation & Zone Mapping]
  - State Vector: <Position in [-1, 1], Spread Z in R, Zone in {1, 2, 3, 4, 5}>
            ↓
[Stage 5: Continuous Dynamic Action & Execution]
  - Action A in [-1, 1] via A2C policy network
  - Execution mode: Open, Adjust (delta |A - P| transacted), or Close
```

### 1. Pair Formation and Cointegration Filtering

- **Formation Lookback Window:** 2 months (October 1, 2023 to November 30, 2023) (`source-reported`).
- **Pearson Correlation:**
  $$\rho_{X,Y} = \frac{\text{cov}(X,Y)}{\sigma_X \sigma_Y}$$
  evaluated across 1-minute, 3-minute, and 5-minute sampling frequencies (`source-reported`).
- **Engle-Granger Two-Step Cointegration Test:**
  1. OLS regression of price series:
     $$Y_t = \alpha + \beta X_t + \epsilon_t$$
  2. Augmented Dickey-Fuller (ADF) unit-root test on residuals $\epsilon_t$:
     $$\Delta \epsilon_t = \gamma \epsilon_{t-1} + \sum_{i=1}^p \delta_i \Delta \epsilon_{t-i} + \nu_t$$
     If $\gamma$ is statistically significantly negative (rejecting unit root), the residuals are stationary $I(0)$, confirming cointegration (`source-reported`).
- **Candidate Screening Table:**

| Candidate Pair | 1m Coint (p-val batch) | 1m Corr | 3m Coint | 3m Corr | 5m Coint | 5m Corr |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **BTCEUR–BTCGBP** | **0.5667** | **0.8758** | **0.4667** | **0.8759** | **0.4667** | **0.8754** |
| BTCEUR–BTCRUB | 0.3333 | 0.8417 | 0.3333 | 0.8417 | 0.3167 | 0.8416 |
| BTCEUR–BTCUSD | 0.1667 | 0.9328 | 0.2000 | 0.9327 | 0.2000 | 0.9329 |
| BTCGBP–BTCRUB | 0.3500 | 0.7606 | 0.3333 | 0.7608 | 0.3333 | 0.7603 |
| BTCGBP–BTCUSD | 0.4833 | 0.8404 | 0.4167 | 0.8403 | 0.4000 | 0.8403 |
| BTCRUB–BTCUSD | 0.4000 | 0.8538 | 0.3333 | 0.8539 | 0.3500 | 0.8543 |

`BTCEUR` and `BTCGBP` at 1-minute intervals exhibited the strongest long-term statistical cointegration (0.5667) and robust correlation (0.8758), and were selected as the primary trading universe (`source-reported`).

### 2. Moving Window Spread and Z-Score Calculation

- At each 1-minute interval $t$, a rolling retrospective moving window of length $W$ bars is evaluated (`source-reported`).
- **Spread Equation:**
  $$p_{i,t} = \beta_0 + \beta_1 p_{j,t} + s_{i,t}, \quad s_{i,t} \sim \mathcal{N}(0, \sigma^2)$$
  where $p_i$ is `BTCEUR` price and $p_j$ is `BTCGBP` price (`source-reported`).
- **Z-Score Normalization:**
  $$Z_t = \frac{s_{i,t} - \bar{s}}{\sigma_s}$$
  where $\bar{s}$ and $\sigma_s$ are the empirical sample mean and sample standard deviation of the residual spread over window $W$ (`source-reported`).

### 3. In-Sample Parameter Calibration via Grid Search

- Calibrated on the 2-month training period (October–November 2023) by maximizing Total Compound Return:
  $$\text{RTOT} = \left(\frac{V'_p}{V_p}\right)^{1/t} - 1 \times 100\%$$
- **Optimal Hyperparameters Selected:**
  - Rolling Window Size $W = 900$ 1-minute intervals ($15.0$ hours) (`source-reported`).
  - Open Threshold $OT = 1.8\sigma$ (`source-reported`).
  - Close Threshold $CT = 0.4\sigma$ (`source-reported`).
  - Training in-sample RTOT achieved: $3.0565\%$ (`source-reported`).

### 4. Spread Zone Discretization

The continuous $Z$-score is mapped into five operational zones (`source-reported`):
1. **Short Zone:** $+1.8 < Z_t < +\infty$ (Spread deviates beyond upper open threshold) (`source-reported`).
2. **Neutral Short Zone:** $+0.4 < Z_t \le +1.8$ (Spread between close and open thresholds) (`source-reported`).
3. **Close Zone:** $-0.4 \le Z_t \le +0.4$ (Spread reverted within close boundaries) (`source-reported`).
4. **Neutral Long Zone:** $-1.8 \le Z_t < -0.4$ (Spread between lower open and close thresholds) (`source-reported`).
5. **Long Zone:** $-\infty < Z_t < -1.8$ (Spread deviates below lower open threshold) (`source-reported`).

### 5. Reinforcement Learning State Space ($\mathcal{S}$)

At each 1-minute step $t$, the agent observes a 3-element state vector (`source-reported`):
$$\mathcal{S}_t = \langle \text{Position}_t, Z_t, \text{Zone}_t \rangle$$
- **$\text{Position}_t \in [-1, 1]$:** Realized portfolio allocation direction and magnitude. $+1.0$ represents 100% long leg (long `BTCEUR`, short `BTCGBP`); $-1.0$ represents 100% short leg (short `BTCEUR`, long `BTCGBP`); $0.0$ represents 100% unallocated cash (`source-reported`).
- **$Z_t \in \mathbb{R}$:** Continuous normalized spread $z$-score (`source-reported`).
- **$\text{Zone}_t \in \{1, 2, 3, 4, 5\}$:** Categorical zone index corresponding to the current spread deviation (`source-reported`).

### 6. Continuous Action Space ($\mathcal{A}_2$) and Execution Logic

In the primary $\text{RL}_2$ dynamic scaling framework (`source-reported`):
- **Action Space:** Continuous scalar $A_t \in [-1, 1]$ output by the neural policy (`source-reported`).
- **Execution Modalities:**
  - **Open Position:** Triggered when $\text{Position}_{t-1} = 0$ and $A_t \neq 0$. Allocates $|A_t| \times \text{Portfolio Value}$ to the long leg ($A_t > 0$) or short leg ($A_t < 0$) (`source-reported`).
  - **Close Position:** Triggered when $\text{Position}_{t-1} \neq 0$ and $A_t = 0$. Fully liquidates active legs back to cash (`source-reported`).
  - **Adjust Position:** Triggered when $\text{Position}_{t-1} \neq 0$ and $A_t \neq 0$. If the agent adjusts exposure (e.g., from $+0.70$ to $+0.80$), only the incremental delta $|A_t - \text{Position}_{t-1}| = 0.10$ notional is submitted to the market, leaving existing positions untouched (`source-reported`).

### 7. Reward Shaping Engine

The step reward $r_2(s_t, a_t)$ integrates three distinct economic signals (`source-reported`):
$$r_2(s_t, a_t) = \text{Portfolio Reward} + \text{Action Reward} - \text{Transaction Punishment}$$
1. **Portfolio Profit Reward:**
   $$\text{Profit Reward} = V_p - V'_p$$
   realized when a position cycle closes, where $V'_p$ is initial capital and $V_p$ is capital post-exit (`source-reported`).
2. **Action Reward:**
   A domain-guided heuristic reward rewarding zone-congruent behaviors to prevent exploratory degeneration during early training (`source-reported`):
   - In Short Zone: rewards Short leg action ($A < 0$).
   - In Neutral Short Zone: rewards Short leg ($A < 0$) or Close ($A = 0$).
   - In Close Zone: rewards Close ($A = 0$).
   - In Neutral Long Zone: rewards Long leg ($A > 0$) or Close ($A = 0$).
   - In Long Zone: rewards Long leg ($A > 0$).
3. **Transaction Punishment:**
   Penalizes excessive portfolio churn and high-frequency position jumping:
   $$\text{Transaction Punishment} = c(|a_t|) \propto |\text{Position}_t - A_t|$$
   penalizing the distance between current position and target action (`source-reported`).
- **RL Algorithm:** Advantage Actor-Critic (A2C) implemented via Stable-Baselines3 (Raffin et al., 2021) (`source-reported`). Discount factor $\gamma$ applied to future expected rewards (`source-reported`).

## Required data

- **Exchange Venue:** Binance spot market (`source-reported`).
- **Trading Pairs:**
  - Primary Pair: `BTCEUR` and `BTCGBP` (`source-reported`).
  - Evaluated Candidate Panel: `BTCEUR`, `BTCGBP`, `BTCUSD`, `BTCRUB` (`source-reported`).
- **Data Timeframes:** 1-minute Candlestick intervals (primary); 3-minute and 5-minute intervals evaluated for cointegration sensitivity (`source-reported`).
- **Data Attributes:** 1-minute Close prices, Volume (`source-reported`).
- **Sample Windows:**
  - Formation & In-Sample Training: October 1, 2023 to November 30, 2023 ($61$ days, $121,500$ 1-minute bars) (`source-reported`).
  - Out-of-Sample Testing: December 1, 2023 to December 31, 2023 ($31$ days, $44,640$ 1-minute test bars) (`source-reported`).
  - Total Analyzed Dataset: $n = 263,520$ 1-minute data points across base and quote instruments (`source-reported`).
- **Missing Data Handling:** Low-volume intervals are explicitly exempted from correlation and cointegration calculations (`source-reported`). Imputation of missing bars is not performed (`source-reported`).

## Execution assumptions

- **Transaction Costs (Commission):**
  - **Baseline:** $0.02\%$ ($2.0\text{ bps}$) flat commission per transaction leg based on Binance's standard fee schedule (`source-reported`).
  - Total round-trip cost per full pair leg (buy asset $i$ and sell asset $j$, then close both): $4 \times 0.02\% = 0.08\%$ ($8.0\text{ bps}$) (`source-reported`).
  - Under `Adjust Position`, fee applies only to the net fractional change $|A_t - \text{Position}_{t-1}|$ (`source-reported`).
  - **Fee Sensitivity Tiers:** Tested across $0.05\%$ ($5\text{ bps}$ retail), $0.02\%$ ($2\text{ bps}$ baseline), $0.01\%$ ($1\text{ bp}$ VIP), and $0.00\%$ ($0\text{ bps}$ promotional zero-fee) (`source-reported`).
- **Execution Fill Model:** Assumes immediate fill at the 1-minute bar close price (`source-reported`).
- **Risk-Free Interest Rate:** Set to $5.5\%$ annualized (Federal Reserve benchmark rate as of June 13, 2024) for Sharpe ratio calculations (`source-reported`).
- **Borrowing / Shorting Constraints:** The study models spot trading and assumes symmetric ability to short either currency pair (`BTCEUR` or `BTCGBP`) without explicit spot borrow interest or margin haircuts (`source-reported provenance gap`).
- **Execution Frictions (Unmodeled):** Bid-ask spread, order book depth, market impact, slippage, and execution network latency are omitted from the backtest simulator (`source-reported provenance gap`).

## Evidence

### Source-reported

All empirical results below trace directly to Tables 4, 5, and 6 in the primary source (Yang & Malik, JRFM 2024, 17(12), 555), evaluated on the out-of-sample test period (December 1, 2023 to December 31, 2023) under a baseline $0.02\%$ ($2\text{ bps}$) commission fee.

#### 1. Baseline Performance Comparison (Out-of-Sample, December 2023, 2 bps fee)

| Metric | Gatev et al. (2006) Traditional Rule | Kim & Kim (2019) Adaptive PPO | Kim & Kim (2019) Adaptive A2C | Kim & Kim (2019) Adaptive DQN | RL$_1$ (Timing) PPO | RL$_1$ (Timing) A2C | RL$_1$ (Timing) DQN | RL$_2$ (Dynamic Scaling) PPO | **RL$_2$ (Dynamic Scaling) A2C** | RL$_2$ (Dynamic Scaling) SAC |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Cumulative Return** | +8.33% | -0.16% | -35.16% | -35.79% | +1.89% | +9.94% | -31.99% | -77.81% | **+31.53%** | -87.12% |
| **CAGR** | +195.12% | -2.19% | -99.71% | -99.75% | +30.05% | +278.72% | -99.56% | -100.00% | **+3974.65%** | -100.00% |
| **Sharpe Ratio** | 25.91 | -1.67 | -2.04 | -2.60 | 5.44 | 32.74 | -8.77 | -1.99 | **94.34** | -1.93 |
| **Total Actions** | 490 | 43 | 1,248 | 1,062 | 1,304 | 249 | 879 | 3,443 | **229** | 2,798 |
| **Won Actions** | 284 | 24 | 600 | 503 | 578 | 240 | 232 | 842 | **162** | 917 |
| **Lost Actions** | 206 | 19 | 648 | 559 | 726 | 9 | 647 | 2,601 | **67** | 1,881 |
| **Win/Loss Action Ratio** | 1.38 | 1.26 | 0.93 | 0.90 | 0.80 | 26.67 | 0.36 | 0.32 | **2.42** | 0.49 |
| **Max Win Action (USD)**| $75.35 | $163.52 | $606.75 | $606.75 | $43.72 | $121.74 | $70.59 | $307.78 | **$648.87** | $160.15 |
| **Max Loss Action (USD)**| -$27.73 | -$187.86 | -$763.70 | -$553.25 | -$108.51 | -$21.33 | -$282.84 | -$389.22 | **-$64.97** | -$1,456.43 |
| **Avg Win Action (USD)**| $14.50 | $41.72 | $38.68 | $37.47 | $5.51 | $17.77 | $11.30 | $15.88 | **$90.94** | $8.03 |
| **Avg Loss Action (USD)**| -$2.90 | -$54.68 | -$58.75 | -$60.78 | -$3.28 | -$7.06 | -$24.95 | -$17.78 | **-$21.00** | -$23.49 |
| **Volatility (ann.)** | 6.01% | 3.93% | 51.43% | 40.43% | 3.61% | 6.30% | 11.92% | 53.04% | **27.30%** | 54.66% |
| **Skew** | 1,840 | -54 | -358 | -358 | -874 | 2,673 | -1,899 | -374 | **4,314** | -3,048 |
| **Kurtosis** | 48,145 | 135 | 4,138 | 4,201 | 133,603 | 114,944 | 54,808 | 12,987 | **254,283** | 138,851 |

*(Note: Sharpe ratios and annualized figures reported by the authors reflect monthly extrapolation without capacity constraints or bid-ask friction; they are reported strictly as comparative benchmarks between models).*

#### 2. Transaction Cost Sensitivity Across Four Fee Tiers (Table 6 in primary source)

| Transaction Fee Tier | Metric | Gatev et al. (2006) | Kim & Kim (2019) PPO | RL$_1$ (Timing) A2C | **RL$_2$ (Dynamic Scaling) A2C** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0.05% (5 bps)** | Cumulative Profit | +5.02% | -0.26% | +5.76% | **+7.40%** |
| | Sharpe Ratio | 14.60 | -2.34 | 21.00 | **7.82** |
| | Total Actions | 490 | 43 | 154 | **207** |
| | Won / Lost Actions | 246 / 244 | 23 / 20 | 152 / 2 | **110 / 97** |
| | Win/Loss Ratio | 1.01 | 1.15 | 76.00 | **1.13** |
| **0.01% (1 bp)** | Cumulative Profit | +9.43% | -1.13% | +9.88% | **+33.99%** |
| | Sharpe Ratio | 29.84 | -7.07 | 33.24 | **104.40** |
| | Total Actions | 490 | 43 | 251 | **181** |
| | Won / Lost Actions | 317 / 173 | 20 / 23 | 242 / 9 | **149 / 32** |
| | Win/Loss Ratio | 1.83 | 0.87 | 26.89 | **4.66** |
| **0.00% (0 bps)** | Cumulative Profit | +10.54% | -2.00% | +9.94% | **+80.92%** |
| | Sharpe Ratio | 33.90 | -5.76 | 32.74 | **2,668.86** |
| | Total Actions | 483 | 43 | 249 | **429** |
| | Won / Lost Actions | 363 / 120 | 23 / 20 | 240 / 9 | **342 / 87** |
| | Win/Loss Ratio | 3.02 | 1.15 | 26.67 | **3.93** |

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Catastrophic Failure of Common RL Algorithms (PPO, DQN, SAC):**
   The study uncovers extreme algorithmic brittleness. While A2C succeeded, other standard deep RL algorithms failed completely:
   - In discrete RL$_1$, DQN generated a catastrophic $-31.99\%$ loss (CAGR $-99.56\%$, Sharpe $-8.77$).
   - In continuous RL$_2$, PPO lost $-77.81\%$ (executing $3,443$ trades) and SAC lost $-87.12\%$ ($2,798$ trades), suffering total portfolio destruction from overtrading fees.
   This proves that dynamic scaling RL is not intrinsically robust; its empirical success is strictly conditional on algorithm-specific policy entropy regularization and gradient stability present in A2C.
2. **Empirical Invalidation of Kim & Kim (2019) Dynamic Thresholding:**
   The state-of-the-art benchmark from the literature (Kim & Kim, 2019), which dynamically shifts entry/exit thresholds using RL, produced negative returns across every single RL architecture (PPO: $-0.16\%$, A2C: $-35.16\%$, DQN: $-35.79\%$) and across all transaction fee tiers ($-0.26\%$ to $-2.00\%$). Dynamic thresholding without continuous position scaling destabilizes under crypto market regimes.
3. **Severe Small-Sample and Single-Regime Exposure:**
   The out-of-sample backtest is restricted to exactly one calendar month (December 2023, during an upward trending Bitcoin market). The strategy was not evaluated during prolonged bear regimes (e.g., 2022), structural exchange decoupling events, or across a multi-year walk-forward test.

## Falsification plan

To disconfirm or falsify the reported alpha hypothesis, the following sequential falsification battery is designed:

1. **Order Book Microstructure and Half-Spread Stress Test (`research-proposed`):**
   - *Test:* Replay the 1-minute `BTCEUR` and `BTCGBP` test trades against tick-level Binance `aggTrades` or L2 depth snapshots, replacing the bar-close fill assumption with an empirical bid-ask half-spread and taker fee ($5.0\text{ bps}$ taker + $2.0\text{ bps}$ effective half-spread $= 7.0\text{ bps}$ one-way).
   - *Decision Rule (`research-defined falsification threshold`):* If net cumulative return drops below $0.0\%$ or annualized Sharpe drops below $0.50$, the strategy's apparent edge is falsified as execution-friction leakage.
2. **Multi-Year Walk-Forward and Regime Invariance Test (`research-proposed`):**
   - *Test:* Execute an expanding-window walk-forward re-training across 36 non-overlapping months spanning diverse market regimes (e.g., 2022 crypto winter, 2023 recovery, 2024–2026 expansion).
   - *Decision Rule (`research-defined falsification threshold`):* If the strategy experiences a maximum peak-to-trough drawdown exceeding $25.0\%$ or if fewer than $50\%$ of out-of-sample test months produce positive net returns, reject the hypothesis of temporal stability.
3. **Random-Pair Placebo Falsification (`research-proposed`):**
   - *Test:* Fit the RL$_2$ A2C agent on randomly paired, non-cointegrated synthetic or real crypto assets (e.g., assets failing the Engle-Granger test with $p > 0.50$).
   - *Decision Rule (`research-defined falsification threshold`):* If the agent achieves similar apparent profitability on non-cointegrated pairs, the reward shaping is proved to be overfitting in-sample noise rather than exploiting true cointegration mean reversion.
4. **Seed Stability and Algorithmic Sensitivity Audit (`research-proposed`):**
   - *Test:* Train the A2C RL$_2$ agent across 20 distinct random initialization seeds.
   - *Decision Rule (`research-defined falsification threshold`):* If more than $20\%$ of seeds fail to achieve positive out-of-sample net returns or if return variance across seeds exceeds $15.0\%$, classify the strategy as unreliably fragile.

## Crypto portability

- **Portability Classification:** Direct (`source-reported`).
- **Empirical Demonstration:** The cited study was designed, trained, and tested directly on cryptocurrency spot market pairs on Binance (`BTCEUR` and `BTCGBP`).
- **Crypto-Specific Operational Differences:**
  - **Spot vs. Perpetual Futures:** In spot markets, shorting requires margin borrowing or holding active fiat balances in both EUR and GBP, incurring interest or fiat conversion fees (`research-proposed`).
  - **Porting to Crypto Perpetual Pairs (`research-proposed`):** If ported to USD-margined or USDT-margined perpetual pairs (e.g., `BTCUSDT` vs. `ETHUSDT` or altcoin relative-value spreads), the two legs will incur divergent 8-hour funding rates. If the short leg is charged funding while the long leg receives none, funding drift could erode the statistical arbitrage spread.
  - **Quote-Currency FX Exposure:** Because `BTCEUR` and `BTCGBP` are quoted in different fiat currencies, holding an unhedged long/short pair exposes the portfolio to the underlying EUR/GBP foreign exchange rate. If the Euro depreciates against the Pound during the holding window, the spread will widen due to fiat currency movement rather than Bitcoin mispricing (`research-proposed`).

## Limitations

- **Single-Month Out-of-Sample Window:** The empirical evaluation spans only December 2023 ($31$ days). A 1-month test window is insufficient to confirm multi-year regime robustness (`source-reported`).
- **Absence of Order Book Depth & Slippage Modeling:** Trades were filled at bar closes without modeling bid-ask spread crossing, market impact, or latency (`source-reported provenance gap`).
- **Unhedged Foreign Exchange Risk:** The pair strategy embeds EUR/GBP currency exchange rate drift into the spread calculation (`research-proposed`).
- **Severe Algorithm Fragility:** Three out of four standard RL algorithms (PPO, DQN, SAC) failed catastrophically, highlighting high sensitivity to policy gradient optimization dynamics (`source-reported`).
- **Unstated Neural Hyperparameters:** While the codebase uses Stable-Baselines3 defaults, explicit learning rates, layer sizes, and training batch timesteps were not reported in the text (`source-reported provenance gap`).

## Implementation status

- Frontmatter status: `not-implemented`.
- No component of this strategy has been implemented in `nautilus-quant-system`, PyBroker, or NautilusTrader.
- No live, paper, or testnet trading has been executed or authorized.

## Adoption boundary

- Status: `research-only`.
- Adoption: `not-approved`.
- Approval Scope: `research-only`.
- A strategy record being present here indicates only that it has been normalized for research intake review. It does not constitute validation, approval for capital allocation, or authorization for live/paper trading.

## Related Wiki records

- `[[quant/statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05]]`
- `[[quant/crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12]]`
- `[[quant/crypto-short-horizon-15min-mean-reversion-taker-flow-2026-09-01]]`
- `[[quant/crypto-funding-carry-fade-turnover-cost-dissipation-falsification-2026-09-12]]`

## Sources

- **Primary Source:** Hongshen Yang and Avinash Malik, "Reinforcement Learning Pair Trading: A Dynamic Scaling Approach", *Journal of Risk and Financial Management* (JRFM), Vol. 17, No. 12, Article 555, December 11, 2024.
  - DOI: `https://doi.org/10.3390/jrfm17120555`
  - arXiv ID: `arXiv:2407.16103v2 [q-fin.TR]`, `https://arxiv.org/abs/2407.16103`
  - Data Archive: Binance Exchange Public Data Archives, `https://data.binance.vision/`
- **Benchmarked Literature Cited by Primary Source:**
  - Gatev, E., Goetzmann, W.N., and Rouwenhorst, K.G. (2006). "Pairs Trading: Performance of a Relative-Value Arbitrage Rule." *The Review of Financial Studies*, 19(3), 797–827. `https://doi.org/10.1093/rfs/hhj020`.
  - Kim, T., and Kim, H.Y. (2019). "Optimizing the Pairs-Trading Strategy Using Deep Reinforcement Learning with Trading and Stop-Loss Boundaries." *Complexity*, 2019, e3582516. `https://doi.org/10.1155/2019/3582516`.
  - Raffin, A., Hill, A., Gleave, A., Kanervisto, A., Ernestus, M., and Dormann, N. (2021). "Stable-Baselines3: Reliable Reinforcement Learning Implementations in Python." *Journal of Machine Learning Research*, 22(268), 1–8.
