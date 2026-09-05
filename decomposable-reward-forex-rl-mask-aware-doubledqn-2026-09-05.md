---
schema: strategy-research-record-v1
title: "Decomposable Multi-Component Reward Modeling with Anti-Lookahead Execution and Legal-Action Masked Double DQN"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reinforcement-learning
  - forex
  - double-dqn
  - reward-shaping
  - action-masking
  - execution-frictions
status: research-only
confidence: medium
source_as_of: 2026-04-01
sources:
  - "arXiv:2604.00031v1 [q-fin.TR, cs.LG]"
  - "https://github.com/NabeelAhmad9/frl_trading_framework/commit/08aaee1d4583b0dba21b93712855c2f2f29b3968"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Decomposable Multi-Component Reward Modeling with Anti-Lookahead Execution and Legal-Action Masked Double DQN

## Provenance

- **Primary Research Paper:** Nabeel Ahmad Saidd, *"Decomposable Reward Modeling and Realistic Environment Design for Reinforcement Learning-Based Forex Trading"*, arXiv preprint `arXiv:2604.00031v1 [q-fin.TR, cs.LG]`, submitted March 20, 2026 (announced April 1, 2026). Canonical URL: [https://arxiv.org/abs/2604.00031](https://arxiv.org/abs/2604.00031). Direct HTML: [https://arxiv.org/html/2604.00031v1](https://arxiv.org/html/2604.00031v1).
- **Primary Open-Source Implementation:** Nabeel Ahmad Saidd, *FRL Trading Framework*, GitHub repository: [https://github.com/NabeelAhmad9/frl_trading_framework](https://github.com/NabeelAhmad9/frl_trading_framework), full immutable commit SHA: `08aaee1d4583b0dba21b93712855c2f2f29b3968` (March 20, 2026).
- **Verification Basis:** The mathematical formulation, 11-component reward functions, 10-action discrete interface, anti-lookahead test specifications (`paper/appendix/app_antilookahead.tex`), algorithmic implementations (`src/environment/trading_env.py`, `src/environment/legal_action_mask.py`, `src/reward/reward_factory.py`, `src/agents/doubledqn/doubledqn_agent.py`), and empirical ablation tables (`paper/tables/tab01_dataset.tex` through `tab12_action_definitions.tex`) were directly inspected from the immutable repository commit and full-text preprint.

## Economic mechanism

### Source-reported

In deep reinforcement learning (RL) applied to financial markets, learned policies often exhibit severe brittleness, excessive turnover, and catastrophic drawdown upon deployment. Saidd (2026) attributes this failure mode to three structural design defects common across prior academic literature:
1. *Unrealistic execution environments and lookahead leakage:* Simulators frequently assume simultaneous observation and fill timestamps ($t$), zero transaction costs, infinite liquidity, and absence of margin constraints, allowing agents to harvest phantom arbitrage.
2. *Scalar reward opacity and non-monotonic component interactions:* Standard scalar rewards (e.g. differential Sharpe or raw PnL) obscure which specific market frictions drive policy decisions. Naively appending single penalty terms (such as raw transaction costs) frequently causes pathological behavior (e.g. freezing into zero activity or paradoxical turnover surges).
3. *Unconstrained action representations:* Allowing unconstrained continuous sizing or unmasked discrete actions forces the policy to learn physical market boundaries (margin sufficiency, position limits) through trial-and-error penalty signals, leading to high sample inefficiency and instability.

To resolve these defects, Saidd (2026) introduces a framework integrating:
- A friction-aware Gymnasium environment enforcing strict anti-lookahead timing (observe at $\text{close}_t$, execute at $\text{open}_{t+1}$, mark-to-market at $\text{close}_{t+1}$) with realistic broker costs (half-spread, deterministic slippage, round-trip commissions, overnight rollover financing, and margin liquidation).
- An 11-component decomposable reward architecture with fixed weights and per-step diagnostic attribution.
- A 10-action discrete execution interface governed by dynamic topological legal-action masking that mathematically prevents invalid order dispatch before Q-value maximization.

### Research interpretation

The proposed framework represents an engineered regularized policy-optimization setup for high-frequency/intraday algorithmic trading. Economically, the agent is not simply attempting to predict the next-period price direction; rather, it solves a constrained Markov Decision Process (MDP) where expected trend/momentum drift is traded off against fixed transaction costs (spread + slippage + commission) and financing decay (rollover swap).

The economic viability of the strategy depends on two mechanisms:
1. *Friction-Conditioned Selective Entry:* By penalizing transaction costs ($w_5 = 0.10$) and local turnover frequency ($w_6 = 0.02$) directly within the Bellman objective, the policy learns to suppress marginal trades during low-volatility chop, entering positions only when feature constellations indicate strong multi-hour directional expansion.
2. *Asymmetric Dynamic Risk Control:* The reward function imposes an asymmetric penalty structure on position scaling—penalizing pyramiding into winning positions moderately ($w_7 = 0.05$) while heavily penalizing martingale averaging-down into losing positions ($w_8 = 0.12$) and penalizing incremental drawdown quadratically ($w_4 = 0.05$). This structural penalty forces the learned policy to exhibit classic institutional risk discipline: cutting losses quickly, holding profitable runs, and strictly limiting tail-risk exposure.

## Signal

### Signal Architecture & Timing Semantics

- **Observation Timestamp:** Step $t$, formed at the completed close of hourly bar $t$ ($\text{close}_t$).
- **Execution Timestamp:** Step $t+1$, strictly filled at the opening print of bar $t+1$ ($\text{open}_{t+1}$).
- **Marking & Reward Timestamp:** Formed at the close of bar $t+1$ ($\text{close}_{t+1}$) using bar $t+1$ price path and costs; no information from bar $t+2$ or beyond is accessible.
- **Lookback Window:** $L = 24$ hourly bars.

### Observation Space

The observation at step $t$ is a dictionary vector composed of four subspaces:
1. `market` ($[24 \times d_{\text{feat}}]$): Rolling 24-hour window of technical and microstructure indicators:
   - *Technical features:* Simple Moving Averages (SMA 10, 20, 50), Exponential Moving Averages (EMA 10, 20, 50), Relative Strength Index (RSI 14), Moving Average Convergence Divergence (MACD 12/26/9), Bollinger Bands (window 20, $2\sigma$), 20-bar rolling return volatility, and 1-step log return.
   - *Microstructure features:* High-Low ratio spread proxy ($(\text{High} - \text{Low})/\text{Close}$), 20-bar realized volatility, 5-bar price change rate, and hourly session indicators.
   - *Normalization:* Fitted strictly on the training split using `StandardScaler` and clipped to $[-5.0, +5.0]$ to eliminate outliers.
2. `portfolio` ($d_{\text{port}} = 10$): Normalized account state:
   $$\mathbf{s}_{\text{port}} = \left[ \frac{\text{cash}}{C_0}, \frac{\text{equity}}{C_0}, \frac{\text{unrealized\_pnl}}{C_0}, \frac{\text{used\_margin}}{C_0}, \frac{\text{free\_margin}}{C_0}, \text{dir}, \text{lots}, \text{pyr\_lvl}, \text{mart\_step}, \text{current\_dd} \right]$$
   where $C_0 = \$100,000$, $\text{dir} \in \{-1.0, 0.0, 1.0\}$, $\text{lots}$ is total open lot exposure, $\text{pyr\_lvl} \in [0, 3]$, $\text{mart\_step} \in [0, 2]$, and $\text{current\_dd} \in [0, 1]$.
3. `mask` ($n_a$ dimensions): Binary vector $m_t \in \{0, 1\}^{n_a}$ indicating feasible actions.
4. `flat` ($[24 \cdot d_{\text{feat}} + 10 + n_a]$): Flattened concatenated representation feeding the MLP Q-network.

### Action Spaces & Legality Preconditions

The framework supports two alternative action interfaces:
1. **Extended 10-Action Interface ($n_a = 10$):**
   - Action 0: `HOLD` (Always legal; maintain current exposure).
   - Action 1: `OPEN_LONG` (Legal iff flat ($\text{dir}=0$) and free margin $\ge$ margin required for base lot 1.0).
   - Action 2: `OPEN_SHORT` (Legal iff flat ($\text{dir}=0$) and free margin $\ge$ margin required for base lot 1.0).
   - Action 3: `PYRAMID_LONG` (Legal iff long ($\text{dir}=1$), unrealized profit $> 0$, pyramid level $< 3$, and margin allows $+0.5$ lots).
   - Action 4: `PYRAMID_SHORT` (Legal iff short ($\text{dir}=-1$), unrealized profit $> 0$, pyramid level $< 3$, and margin allows $+0.5$ lots).
   - Action 5: `MARTINGALE_LONG` (Legal iff long ($\text{dir}=1$), adverse price move, martingale steps $< 2$, and margin allows $1.5\times$ lot scaling).
   - Action 6: `MARTINGALE_SHORT` (Legal iff short ($\text{dir}=-1$), adverse price move, martingale steps $< 2$, and margin allows $1.5\times$ lot scaling).
   - Action 7: `REDUCE_POSITION` (Legal iff non-flat; closes $50\%$ of current exposure).
   - Action 8: `CLOSE_POSITION` (Legal iff non-flat; fully closes current exposure to flat).
   - Action 9: `REVERSE_POSITION` (Legal iff non-flat and margin allows closing current and opening opposite base lot).
2. **Simplified 3-Action Interface ($n_a = 3$):**
   - Action 0: `HOLD` (Maintain position).
   - Action 1: `TARGET_LONG` (Open long if flat, reverse if short, hold if long).
   - Action 2: `TARGET_SHORT` (Open short if flat, reverse if long, hold if short).

### Decomposable 11-Component Reward Formulation

The per-step scalar reward $r_t$ is computed as the clipped sum of 11 weighted components:
$$r_t^{\text{raw}} = \sum_{i=1}^{11} w_i \cdot c_i(\tau_t), \quad r_t = \text{clip}(r_t^{\text{raw}}, -5.0, +5.0)$$

1. **Post-Cost PnL ($w_1 = 1.00$):** Gross period return $\Delta \text{equity}_{\text{gross}} / \text{equity}_t$ before explicit cost penalties.
2. **Holding Incentive ($w_2 = 0.03$):** Small positive bonus $+0.1$ awarded iff position is profitable ($\text{unrealized\_pnl} > 0$) and drawdown is low ($< 5\%$).
3. **Volatility Penalty ($w_3 = 0.01$):** Negative term proportional to rolling 20-step equity return standard deviation: $-\text{std}(\text{returns}_{t-20:t})$.
4. **Drawdown Penalty ($w_4 = 0.05$):** Incremental drawdown growth penalty plus non-linear penalty for severe drawdown:
   $$c_4 = -\left(\Delta \text{drawdown}_t + \max(0, \text{current\_drawdown}_t - 0.15) \times 5.0\right)$$
5. **Transaction Burden ($w_5 = 0.10$):** Normalized friction penalty: $-\text{total\_friction\_cost}_t / C_0$ (encompassing spread, slippage, commission, and rollover).
6. **Overtrading Penalty ($w_6 = 0.02$):** Bounded quadratic penalty when trade count in rolling 20-bar window exceeds 10 trades:
   $$c_6 = -0.02 \times \left(\frac{\text{trades\_in\_window} - 10}{20}\right)^2$$
7. **Pyramiding Penalty ($w_7 = 0.05$):** Mild penalty proportional to active pyramid depth, capped at $-0.02$ per step.
8. **Martingale Penalty ($w_8 = 0.12$):** Substantially harsher penalty proportional to martingale averaging-down depth, capped at $-0.02$ per step.
9. **Margin Utilization Penalty ($w_9 = 0.05$):** Quadratic penalty $-(\text{margin\_utilization} - 5.0)^2$ triggered when leverage exceeds conservative thresholds.
10. **Liquidation Penalty ($w_{10} = 2.00$):** Severe catastrophic event penalty ($-1.0$, scaled by weight to $-2.0$) applied upon forced account liquidation.
11. **Constraint Violation Penalty ($w_{11} = 0.10$):** Penalty $-\max(0.02, \text{invalid\_penalty})$ applied if an agent attempts an illegal action proposal.

### Double DQN Learning Architecture

- **Q-Network Architecture:** Multi-Layer Perceptron (MLP) with layer dimensions `[512, 512, 256]`, ReLU non-linearities, and linear Q-head.
- **Mask-Aware Greedy Policy:**
  $$a_t^* = \arg\max_{a:\, m_t[a]=1} Q_\theta(s_t, a)$$
- **Mask-Aware Bellman Target:**
  $$y_i = r_i + \gamma (1 - d_i) Q_{\theta^-}\left(s'_i, \arg\max_{a:\, m'_i[a]=1} Q_\theta(s'_i, a)\right)$$
- **Loss Function:** Huber loss $\mathcal{L} = \frac{1}{B} \sum_{i=1}^B \text{Huber}(Q_\theta(s_i, a_i) - y_i)$.
- **Training Hyperparameters:** Adam optimizer ($lr = 2.5 \times 10^{-4}$), batch size 128, replay buffer size 40,000 transitions, learning start 10,000 steps, update frequency every 4 steps, target network hard synchronization every 2,000 steps, gradient clipping norm 10.0, discount factor $\gamma = 0.99$, exploration schedule $\epsilon$ decaying linearly from 1.0 to 0.01 over 30,000 steps, total training duration 1,000,000 environment timesteps.

## Required data

- **Universe / Instrument:** Spot/Margin Foreign Exchange currency pairs: EURUSD (primary benchmark), GBPUSD, USDJPY, AUDUSD.
- **Venue:** Consolidated OTC interbank spot forex pricing.
- **Timeframe:** 1-hour OHLCV sampled bars.
- **Data Period:** 25,000 hourly bars total (January 1, 2022 to January 1, 2026); partitioned into training split (20,000 bars, 2022-01-01 to 2025-01-01) and held-out split (5,000 bars, 2025-01-01 to 2026-01-01).
- **Required Fields:** Open, High, Low, Close, Volume, Timestamp (UTC).
- **Point-in-Time Guarantees:** Chronological sequence processing. Feature scaling parameters (`StandardScaler`) are fitted exclusively on the 20,000-bar training split and applied without revision. No future bar data is exposed to observation construction.

## Execution assumptions

- **Execution Timing:** Next-bar execution; decisions formed at $\text{close}_t$ are filled at $\text{open}_{t+1}$ (`source-reported`).
- **Order Fill Model:** Simulated market order with immediate deterministic fill (`source-reported`).
- **Base Slippage:** Fixed 0.5 pips ($0.00005$ price units) added against trade direction on every executed order (`source-reported`).
- **Commissions:** USD 3.50 per standard lot ($100,000$ base units) round-trip (`source-reported`).
- **Spread:** Bid-ask spread calculated via High-Low ratio spread proxy, with broker minimum spread enforced (`source-reported`).
- **Rollover Financing:** Overnight swap financing debited daily at 22:00 UTC, with triple rollover debited on Wednesday (`source-reported`).
- **Account Capital & Leverage:** Initial equity USD 100,000; maximum leverage 30x; maintenance margin liquidation triggered if equity falls below 25% of required margin (`source-reported`).
- **Position Sizing:** Base entry lot size 1.0 ($100,000$ units); pyramid increments 0.5 lots; martingale multiplier $1.5\times$ (`source-reported`).
- **Market Impact & Capacity:** Model assumes zero temporary or permanent market impact beyond fixed 0.5-pip slippage (`research-proposed limitation`).

## Evidence

### Source-reported

All figures below are cited directly from Saidd (2026), *arXiv:2604.00031v1* and the companion repository tables.

#### 1. Global Performance Benchmark on EURUSD (Train Split, 20,000 bars, 2022–2025)

*Source: Saidd (2026), Table 9 (`tab09_benchmarks.tex`):*

| Strategy / Method | Sharpe Ratio | Cumulative Return (%) | Max Drawdown (%) | Win Rate (%) | Annualized Turnover | Total Trades |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Random Policy** | -13.380 | -34.58 | 34.70 | 25.99 | 2199.98 | 13,728 |
| **Buy-and-Hold** | -0.358 | -1.05 | 2.08 | 0.00 | 0.11 | 1 |
| **Momentum Benchmark** | -1.355 | -3.82 | 4.05 | 23.62 | 186.28 | 1,715 |
| **Mean-Reversion Benchmark** | -0.807 | -1.67 | 2.34 | 24.64 | 157.67 | 1,469 |
| **DQN (Full Reward r7)** | 0.369 | 24.56 | 8.72 | 34.12 | 1316.51 | 11,240 |
| **Double DQN (Full Reward r7)** | **0.765** | **57.09** | **2.31** | **33.15** | **1156.51** | **8,415** |

*Note: In annualized risk diagnostics (Table 8), Double DQN achieved an Annualized Return of 14.82%, Annualized Volatility of 4.11%, and Sortino ratio of 4.771.*

#### 2. Reward Component Ablation Study on EURUSD (Double DQN)

*Source: Saidd (2026), Table 3 (`tab03_ablation.tex`):*

| Variant & Components Enabled | Sharpe | Sortino | Cum. Ret (%) | Max DD (%) | Win Rate (%) | Turnover | Avg Pyr | Avg Mart |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **r1: Profit-only core** | 0.412 | 0.573 | 27.79 | 10.48 | 35.18 | 1592.83 | 0.113 | 0.121 |
| **r2: + Transaction penalty** | 0.237 | 0.353 | 12.20 | 8.60 | 31.85 | 1741.58 | 0.187 | 0.127 |
| **r3: + Drawdown penalty** | 0.638 | 0.979 | 41.20 | 5.44 | 31.53 | 1488.67 | 0.165 | 0.138 |
| **r4: + Volatility penalty** | 0.687 | 1.029 | 43.21 | 5.68 | 30.99 | 1344.47 | 0.197 | 0.144 |
| **r5: + Overtrading penalty** | 0.589 | 0.822 | 41.74 | 4.12 | 31.07 | 1350.00 | 0.172 | 0.156 |
| **r6: + Scaling penalty** | 0.410 | 0.539 | 24.58 | 7.70 | 27.38 | 1200.32 | 0.132 | 0.089 |
| **r7: Full reward (all 11)** | **0.765** | **1.117** | **57.09** | **2.31** | **33.15** | **1156.51** | **0.173** | **0.169** |

#### 3. Action-Space Comparison (Extended 10-Action vs. Simplified 3-Action)

*Source: Saidd (2026), Table 4 (`tab04_action_space.tex`):*

| Action Space | Sharpe | Cum. Ret (%) | Max DD (%) | Win Rate (%) | Turnover |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Extended (10 Actions)** | 0.765 | 57.09 | 2.31 | 33.15 | 1156.51 |
| **Simplified (3 Actions)** | 2.433 | 33.21 | 0.29 | 68.13 | 528.65 |

*Author finding:* The simplified 3-action adapter achieved a much higher Sharpe ratio (2.433 vs. 0.765) and lower drawdown (0.29% vs. 2.31%) under identical 1M training step budgets, demonstrating that the extended 10-action space introduces severe exploration overhead that requires larger training sample efficiency.

#### 4. Scaling Strategy Analysis

*Source: Saidd (2026), Table 5 (`tab05_scaling.tex`):*

| Scaling Variant | Sharpe | Cum. Ret (%) | Max DD (%) | Avg Pyr | Avg Mart | Turnover |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **s1: No scaling** | -1.568 | -16.54 | 16.74 | 0.000 | 0.000 | 1440.09 |
| **s2: Pyramiding only** | -0.136 | -2.48 | 5.73 | 0.083 | 0.000 | 1394.52 |
| **s3: Martingale only** | 0.319 | 8.94 | 4.63 | 0.000 | 0.122 | 1273.71 |
| **s4: Both (Pyramid + Martingale)** | **0.355** | **13.08** | **6.79** | **0.086** | **0.096** | **1483.55** |

#### 5. Cross-Pair Robustness (Train Split, Double DQN Full Reward r7)

*Source: Saidd (2026), Table 7 (`tab08_cross_pair.tex`):*

| Pair | Agent Architecture | Sharpe Ratio | Sortino Ratio | Cum. Return (%) | Max Drawdown (%) | Win Rate (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **EURUSD** | Double DQN | 0.765 | 1.117 | 57.09 | 2.31 | 33.15 |
| **GBPUSD** | Double DQN | 0.759 | 0.969 | 83.19 | 3.14 | 31.90 |
| **USDJPY** | Double DQN | 1.115 | 1.615 | 115.01 | 4.44 | 33.69 |
| **AUDUSD** | Double DQN | 0.811 | 1.222 | 52.98 | 4.91 | 32.16 |

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Non-Monotonic Reward Penalty Interactions:** In the ablation experiment (Table 3), naively adding transaction penalties ($r_2$) without drawdown or volatility penalties collapsed the Sharpe ratio from 0.412 to 0.237 and increased annualized turnover from 1,592.83 to 1,741.58. The author notes that isolated cost penalties induce severe policy instability where the agent struggles to amortize fixed transaction friction.
2. **Failure of No-Scaling Policies:** Completely restricting position scaling (variant `s1_no_scaling`, Table 5) produced disastrous performance: Sharpe -1.568, cumulative return -16.54%, and maximum drawdown 16.74%. Rigid unit-lot exposure prevented the agent from adjusting position risk dynamically.
3. **Severe Training-Set Evaluation Bias:** All empirical figures reported in Saidd (2026) were computed exclusively on the **training split** ($N_{\text{train}} = 20,000$ bars, 2022–2025). As explicitly admitted by the author in Section 4.1 and Section 7.1, the 5,000-bar held-out split (2025–2026) was left un-evaluated in the manuscript to focus strictly on optimization dynamics. Out-of-sample generalization across unseen market regimes remains completely unverified.

## Falsification plan

To empirically validate or refute whether the multi-component reward and legal-masking framework generates genuine out-of-sample alpha rather than overfitted training-set artifacts, the following pre-declared falsification tests are established:

1. **Held-Out Out-of-Sample Evaluation Test:**
   - *Protocol:* Load checkpointed weights trained on the 2022–2025 EURUSD split and execute deterministic evaluation ($\epsilon = 0$) on the untouched 5,000-bar held-out split (2025-01-01 to 2026-01-01) under identical transaction costs (0.5 pips slippage, $3.50/lot commission, rollover swap).
   - *Failure Rule:* `research-defined falsification threshold`: If the out-of-sample Sharpe ratio drops below $0.15$ or maximum drawdown exceeds $10.0\%$, falsify the claim that the policy learned generalizable market microstructure structure.
2. **Transaction Cost & Slippage Stress Sensitivity:**
   - *Protocol:* Evaluate the trained Double DQN policy across varying cost multipliers: $1\times$ (baseline), $2\times$ (1.0 pip slippage, $7.00/lot commission), and $3\times$ (1.5 pips slippage, $10.50/lot commission).
   - *Failure Rule:* `research-defined falsification threshold`: If the strategy's cumulative net return turns negative or net Sharpe drops below $0.00$ at $2\times$ baseline costs (1.0 pip slippage), classify the strategy as an execution-sensitive artifact unviable for institutional production.
3. **Ablation of Legal Action Masking:**
   - *Protocol:* Retrain Double DQN without topological action masking, allowing the network to output all 10 actions unconstrained and relying solely on the negative constraint-violation penalty ($w_{11} = 0.10$).
   - *Failure Rule:* `research-defined falsification threshold`: If unmasked training fails to achieve within $30\%$ of the masked variant's Sharpe ratio (i.e. Sharpe $< 0.53$) or experiences forced liquidation during training, confirm that explicit topological masking is an indispensable structural invariant.
4. **Synthetic White-Noise / Placebo Shuffle Test:**
   - *Protocol:* Randomly permute the hourly return series while preserving empirical variance and recalculate technical features. Train Double DQN on the shuffled dataset across 1,000,000 timesteps.
   - *Failure Rule:* `research-defined falsification threshold`: If the shuffled-data policy achieves a Sharpe ratio $\ge 0.30$ or cumulative return $\ge 15\%$, reject the hypothesis that the network is extracting genuine price-action predictive signals.

## Crypto portability

- **Portability Classification:** `adapted/unproven` (research interpretation; primary research is demonstrated exclusively in G10 Forex markets: EURUSD, GBPUSD, USDJPY, AUDUSD).
- **Structural Portability Challenges in Cryptocurrency Derivatives:**
  1. **Session & Rollover Swap Differences:** In Forex, trading halts over weekends and financing is settled via daily interbank rollover swap at 22:00 UTC (with triple swap on Wednesday). Crypto perpetual futures trade continuously 24/7/365 without weekend closures, and financing is settled via 8-hour funding rates ($\text{funding\_rate} \times \text{position\_value}$). Porting requires replacing the fixed rollover model with dynamic 8-hour exchange funding rate feeds.
  2. **Liquidation Mechanics & Maintenance Margins:** Traditional FX margin utilizes conservative leverage caps (e.g. 30x) with broker margin-call buffers. Crypto perpetual platforms (Binance, Bybit, OKX, Hyperliquid) utilize exchange-specific multi-tier maintenance margin schedules and automated liquidations via order-book sweeps or insurance funds. Pyramiding and martingale scaling in crypto entail non-linear liquidation acceleration during flash crashes.
  3. **Spread & Slippage Regime Shifts:** Spot FX exhibits tight, continuous spreads ($0.1$ to $0.5$ pips) during liquid market sessions. Crypto perpetuals frequently exhibit sudden book thinning and spread blowouts during volatility spikes; fixed 0.5-pip slippage assumptions must be adapted to non-linear order-book depth models.
  4. **Stablecoin Quote Collateral:** FX accounts settle in USD. Crypto perpetuals are collateralized in USDT, USDC, or inverse coin margin (BTC/ETH), exposing portfolio equity to collateral depegging or underlying coin volatility.

## Limitations

- **Omission of Out-of-Sample Empirical Results:** The primary publication documents performance exclusively on in-sample training data (`data gap / unproven out-of-sample`).
- **Exploration Overhead in Extended Action Spaces:** The 10-action interface significantly underperformed the 3-action adapter on Sharpe ratio (0.765 vs. 2.433) under a 1M-step budget, indicating that high-cardinality action spaces require substantial compute scaling (`source-reported limitation`).
- **Absence of Market Impact Modeling:** Fills assume perfect limit-order absorption at `open_{t+1}` plus fixed 0.5-pip slippage without market impact or participation rate penalties (`research-proposed limitation`).
- **High Turnover Dependency:** Annualized turnover exceeding 1,150 turns per year exposes the policy to severe fee drag under adverse broker spread widening (`research-proposed limitation`).

## Implementation status

- `implementation_status: not-implemented`
- Neither the 11-component reward engine nor the 10-action masked Double DQN trading environment has been implemented or benchmarked in our quantitative stack (`nautilus-quant-system`, PyBroker, or NautilusTrader).
- No historical backtest, paper trading, testnet, or live trading has been conducted or authorized.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- This document functions solely as normalized research capture documenting a peer-reviewed reinforcement learning execution architecture and empirical ablation study. It does not constitute approval for capital allocation or execution.

## Related Wiki records

- `crypto-drl-execution-overlay-multi-pair-trading-2026-09-01.md` (Deep reinforcement learning execution overlay in multi-pair crypto trading)
- `model-free-statistical-arbitrage-empirical-mean-reversion-time-reinforcement-learning-2026-09-05.md` (Reinforcement learning for empirical mean reversion and statistical arbitrage)
- `partial-information-regime-filtering-ddpg-ornstein-uhlenbeck-pairs-trading-2026-09-05.md` (DDPG reinforcement learning for regime-filtered pairs trading)
- `questrader-self-supervised-auxiliary-task-discovery-rl-trading-2026-09-02.md` (Self-supervised auxiliary tasks for RL trading agents)
- `sinkhorn-robust-rl-high-frequency-market-making-2026-09-02.md` (Distributionally robust reinforcement learning for high-frequency quoting)

## Sources

1. **Primary Research Preprint:** Nabeel Ahmad Saidd, *"Decomposable Reward Modeling and Realistic Environment Design for Reinforcement Learning-Based Forex Trading"*, arXiv:2604.00031v1 [q-fin.TR, cs.LG], submitted March 20, 2026 (announced April 1, 2026). Stable abstract: [https://arxiv.org/abs/2604.00031](https://arxiv.org/abs/2604.00031). Direct HTML: [https://arxiv.org/html/2604.00031v1](https://arxiv.org/html/2604.00031v1).
2. **Primary Code Repository:** Nabeel Ahmad Saidd, *FRL Trading Framework*, GitHub repository: [https://github.com/NabeelAhmad9/frl_trading_framework](https://github.com/NabeelAhmad9/frl_trading_framework), full commit SHA: `08aaee1d4583b0dba21b93712855c2f2f29b3968`.
3. **Core LaTeX Tables and Experiment Configurations in Source Commit `08aaee1`:**
   - `paper/tables/tab01_dataset.tex` (Dataset statistics, hourly EURUSD/GBPUSD/USDJPY/AUDUSD 2022–2026)
   - `paper/tables/tab02_hyperparams.tex` (Hyperparameters, interface dimensions, and environment settings)
   - `paper/tables/tab03_ablation.tex` (Reward ablation table, variants r1 through r7)
   - `paper/tables/tab04_action_space.tex` (Action space comparison, Extended 10 vs. Simplified 3)
   - `paper/tables/tab05_scaling.tex` (Scaling strategy analysis, variants s1 through s4)
   - `paper/tables/tab08_cross_pair.tex` (Cross-pair DQN vs. Double DQN results)
   - `paper/tables/tab09_benchmarks.tex` (Benchmark comparison against Random, Buy-and-Hold, Momentum, Mean-Reversion)
   - `paper/tables/tab10_observation_schema.tex` (Observation schema dimensions)
   - `paper/tables/tab11_reward_components.tex` (11-component reward definitions and weights)
   - `paper/tables/tab12_action_definitions.tex` (Action semantics and legality preconditions)
   - `paper/appendix/app_antilookahead.tex` (Formal anti-lookahead timing definition and test cases)
