---
schema: strategy-research-record-v1
title: "DeepSeekMath Meets Order Book — Group-Aware Policy Optimization (GRPO/GSPO) for High-Frequency LOB Directional Trading"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - limit-order-book
  - order-flow-imbalance
  - reinforcement-learning
  - grpo
  - gspo
  - high-frequency-trading
status: research-only
confidence: medium
source_as_of: 2026-05-25
sources:
  - https://arxiv.org/abs/2605.25527
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# DeepSeekMath Meets Order Book — Group-Aware Policy Optimization (GRPO/GSPO) for High-Frequency LOB Directional Trading

## Provenance

- **Paper:** Sayak Chakrabarty, Souradip Pal. *"DeepSeekMath Meets Order Book: Group-Aware Policy Optimization for High-Frequency Directional Trading"*
- **arXiv ID:** `arXiv:2605.25527v1 [q-fin.TR]`
- **Submission Date:** 25 May 2026
- **Authors & Affiliations:**
  - Sayak Chakrabarty (Department of Computer Science, Northwestern University, Evanston, IL, USA)
  - Souradip Pal (School of Electrical and Computer Engineering, Purdue University, West Lafayette, IN, USA)
  - Both authors contributed equally.
- **Primary Source URL:** https://arxiv.org/abs/2605.25527 (PDF: https://arxiv.org/pdf/2605.25527)
- **Primary Text Examined:** Full author-provided LaTeX package (`template.tex`, `references.bib`, figures) unpacked from official arXiv source e-print archive `2605.25527.tar.gz`.
- **Pre-write Deduplication Audit:**
  - Canonical identifier check: `2605.25527` does not exist in any existing repository file.
  - Author search: Neither Sayak Chakrabarty nor Souradip Pal appears in existing repository records.
  - Title/concept check: No record exists analyzing Group Relative Policy Optimization (GRPO) or Group Sequence Policy Optimization (GSPO) applied to limit-order-book (LOB) order-flow imbalance (OFI) directional trading. Existing repository records citing GRPO (`trading-r1`, `llm-news-sentiment`, `janus-q`, `finsmart`) focus on LLM text reasoning, news sentiment NLP extraction, or ETF portfolio weights, whereas this paper investigates critic-free group-normalized policy gradients directly on high-frequency microstructural LOB state transitions without language models.

## Economic mechanism

### Source-reported

The paper investigates autonomous directional trading in electronic limit order books using reinforcement learning (RL). Electronic LOBs operate via first-in-first-out (FIFO) matching, where resting limit orders are filled by opposing market orders. Because the raw LOB state is high-dimensional and non-stationary, prior RL approaches face three key structural bottlenecks:
1. **Critic instability:** Actor-critic methods and standard Proximal Policy Optimization (PPO) require training a secondary value network (critic), which is computationally expensive on high-frequency event streams and notoriously unstable under noisy, sparse, and delayed market rewards.
2. **State representation:** Raw price/volume levels contain excessive noise. Following Jaddu & Vyetrenko (2023), the authors extract piecewise Order-Flow Imbalance (OFI) across 10 book levels to capture instantaneous net liquidity replenishment versus consumption.
3. **Reward variance and drawdown risk:** Value-based methods (e.g., tabular Q-learning) struggle with high return variance and state discretization errors.

To address these limitations, the authors adapt two recent group-aware policy optimization algorithms from large language model alignment:
- **Group Relative Policy Optimization (GRPO)** (from DeepSeekMath; Shao et al., 2024): Discards the critic network entirely. Instead of estimating advantages through a learned value function, GRPO samples a group of $G$ complete episodes per update, calculates the mean and standard deviation of episode returns across the group, and normalizes episode advantages against this empirical update-level baseline.
- **Group Sequence Policy Optimization (GSPO)** (from Qwen / Alibaba Inc.): Extends group-level advantage estimation by replacing per-step token/action importance clipping with sequence-level (trajectory-level) importance ratio clipping, constraining policy divergence across entire trading episodes.

The authors evaluate whether these group-aware objectives improve net PnL returns, win rates (profitability %), profit-to-loss ratios, and downside risk (maximum drawdown) compared to PPO and tabular Q-learning in a directional trading simulator.

### Research interpretation

The proposed strategy is a **hybrid multi-stage alpha system**:
1. **Microstructural feature extraction:** 10-level piecewise Order-Flow Imbalance (OFI) capturing short-horizon supply/demand imbalance.
2. **Supervised forecasting front-end (state compressor):** A frozen 4-layer Multi-Layer Perceptron (MLP) mapping 10-dimensional OFI to a 6-horizon return forecast vector $\hat{\alpha}_t \in \mathbb{R}^6$.
3. **Markov Decision Process (MDP) state:** Concatenation of the 6-horizon forecast vector with the agent's previous trading action: $s_t = [\hat{\alpha}_t; a_{t-1}] \in \mathbb{R}^7$.
4. **Group-aware policy execution:** A policy network $\pi_\theta(a_t | s_t)$ trained via GRPO or GSPO that outputs directional market orders.

The hypothesized economic alpha mechanism is **order-flow imbalance momentum and mean reversion at microstructural event scales**:
- Aggressive order arrival and cancellations shift the balance of resting depth. Persistent positive OFI reflects net aggressive buying or ask queue depletion, predicting positive subsequent mid-price revisions over near-term event intervals.
- The mechanistic benefit of GRPO and GSPO in financial trading is **variance reduction without value-function bias**:
  - In financial time series, returns are heavy-tailed and non-stationary. A learned critic network frequently suffers from non-stationary target drift, destabilizing policy updates.
  - GRPO's group-level centering ($R_i - \bar{R}$) standardizes returns against contemporaneous batch realizations, effectively acting as an empirical control variate that insulates the policy gradient from broader market-wide trends or volatility shocks occurring during that update batch.
  - GSPO's trajectory-level importance clipping prevents single erratic high-variance trajectories from disproportionately warping the policy.

## Signal

The strategy operates in event time, triggered on order book message arrivals from the NASDAQ TotalView-ITCH feed.

### 1. Order-Flow Feature Extraction
At event step $t$, observable quantities are prices and aggregated volumes across the first 10 non-empty levels: $\{a_t^i, v_t^{i,a}, b_t^i, v_t^{i,b}\}_{i=1}^{10}$.
Per-level ask order flow ($a\mathrm{OF}_{t,i}$) and bid order flow ($b\mathrm{OF}_{t,i}$) are calculated piecewise:
$$a\mathrm{OF}_{t,i} = \begin{cases} v_t^{i,a}, & \text{if } a_t^i < a_{t-1}^i \\ v_t^{i,a} - v_{t-1}^{i,a}, & \text{if } a_t^i = a_{t-1}^i \\ -v_{t-1}^{i,a}, & \text{if } a_t^i > a_{t-1}^i \end{cases}$$
$$b\mathrm{OF}_{t,i} = \begin{cases} v_t^{i,b}, & \text{if } b_t^i > b_{t-1}^i \\ v_t^{i,b} - v_{t-1}^{i,b}, & \text{if } b_t^i = b_{t-1}^i \\ -v_{t-1}^{i,b}, & \text{if } b_t^i < b_{t-1}^i \end{cases}$$

Level-wise Order-Flow Imbalance is defined as:
$$\mathrm{OFI}_t = b\mathrm{OF}_t - a\mathrm{OF}_t \in \mathbb{R}^{10}$$
Sample-level normalized feature vector:
$$x_t \leftarrow \frac{\mathrm{OFI}_t}{\max(1, \|\mathrm{OFI}_t\|_\infty)}$$

### 2. Multi-Horizon Supervised Forecaster ($f_\theta$)
- **Architecture:** 4-hidden-layer MLP with hidden layer width 2048.
- **Input:** $x_t \in \mathbb{R}^{10}$.
- **Target returns:** $y_t^{(h)} = \frac{m_{t+h} - m_t}{m_t}$, where $m_t = \frac{a_t^1 + b_t^1}{2}$ is mid-price, for horizons $\mathcal{H} = \{h_1, \dots, h_6\}$ ($H=6$ horizons measured in event steps).
- **Output:** Predicted multi-horizon return vector $\hat{\alpha}_t = f_\theta(x_t) \in \mathbb{R}^6$.
- **Training objective:** $\mathcal{L}_{\mathrm{sup}}(\theta) = \frac{1}{N}\sum_{t=1}^N \sum_{h \in \mathcal{H}} (\hat{y}_t^{(h)} - y_t^{(h)})^2$.
- **Training protocol:** Adam optimizer, per-instrument learning rates, weight decay, early stopping on validation loss up to 100 epochs. Best checkpoint retained and frozen.

### 3. Reinforcement Learning MDP State and Actions
- **State:** $s_t = [\hat{\alpha}_t; a_{t-1}] \in \mathbb{R}^7$.
- **Action space:** Discrete directional trading actions. (`research-proposed` concrete action mapping: $a_t \in \{-1, 0, 1\}$ representing short, neutral/flat, and long directional positions, as the paper text designates "discrete directional trading actions" without enumerating exact integer labels).
- **Reward:** Computed based on the change in mid-price after the action is taken, scaled by a factor depending on the bid-ask spread ($a_t^1 - b_t^1$). (`research-proposed` operational reward formulation: $r_t = a_t \cdot \frac{m_{t+1} - m_t}{a_t^1 - b_t^1}$, capturing spread-scaled directional mid-price increments).

### 4. Policy Optimization Objectives
- **GRPO Objective:**
  For a batch of $G$ complete episodes $\{\tau_1, \dots, \tau_G\}$, with episode return $R_i = \sum_{t \in \tau_i} r_t$:
  $$\bar{R} = \frac{1}{G}\sum_{i=1}^G R_i, \qquad \sigma_R^2 = \frac{1}{G}\sum_{i=1}^G (R_i - \bar{R})^2$$
  Standardized group advantage:
  $$A_i^{\mathrm{grp}} = \frac{R_i - \bar{R}}{\sigma_R + \varepsilon}$$
  Clipped surrogate objective applied across pooled timesteps:
  $$L^{\mathrm{GRPO}}(\theta) = \mathbb{E}_{\tau_i, t}\left[\min\left(\rho_t(\theta) A_i^{\mathrm{grp}}, \operatorname{clip}(\rho_t(\theta), 1-\epsilon, 1+\epsilon) A_i^{\mathrm{grp}}\right)\right]$$
  where $\rho_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{\mathrm{old}}}(a_t|s_t)}$.
- **GSPO Objective:**
  Trajectory-level importance ratio:
  $$\rho_i(\theta) = \exp\left(\sum_{t \in \tau_i} \log \pi_\theta(a_t|s_t) - \sum_{t \in \tau_i} \log \pi_{\theta_{\mathrm{old}}}(a_t|s_t)\right)$$
  Sequence-level clipped surrogate:
  $$L^{\mathrm{GSPO}}(\theta) = \frac{1}{G}\sum_{i=1}^G \min\left(\rho_i(\theta) A_i^{\mathrm{grp}}, \operatorname{clip}(\rho_i(\theta), 1-\epsilon, 1+\epsilon) A_i^{\mathrm{grp}}\right)$$

### 5. Identified Specification Gaps
- **Underspecified horizon integers:** The exact integer step values for the $H=6$ horizons $\{h_1, \dots, h_6\}$ are not explicitly tabulated in the paper text (`research-proposed` candidate grid: $h \in \{1, 5, 10, 20, 50, 100\}$ events).
- **Underspecified spread-scaling coefficient:** The exact algebraic formula relating the bid-ask spread to reward scaling is stated in words ("scaled by a factor depending on the bid-ask spread") but omitted in symbolic form.
- **Underspecified group size and episode length:** The exact batch size $G$ (number of grouped episodes) and episode length $T$ (number of event steps per episode) are omitted from the text (`research-proposed`: $G=16, T=100$).
- **Underspecified instrument scaling constants:** The metric evaluation references $c_{\mathrm{instr}} = \mathrm{PRICE\_TO\_PNL}[\mathrm{instrument}]$, but ticker-specific scaling constants are not provided in text.

## Required data

- **Instrument Universe:** 3 US Large-Cap Equities: Amazon (`AMZN`), Apple (`AAPL`), Google (`GOOG`).
- **Venue:** NASDAQ (via TotalView-ITCH feed preprocessed by LOBSTER).
- **Market Type:** Cash Equities / Limit Order Book.
- **Depth:** Level-10 full book depth (prices and aggregated sizes for top 10 bid and ask tiers).
- **Timestamp Resolution:** Decimal precision of at least milliseconds and up to nanoseconds.
- **Sample Period:** June 21, 2013, morning trading session (09:30 to 10:30 EST, 1 hour).
  - AMZN: 269,748 usable event transitions.
  - AAPL: 400,391 usable event transitions.
  - GOOG: 147,916 usable event transitions.
- **Partitioning:** Chronological split at the episode level: 80% Train, 10% Validation (early stopping on MSE / validation loss), 10% Held-Out Test (evaluation).
- **Data Gap:** Extremely narrow time sample (single 1-hour morning window from one trading day in 2013). Does not capture varying market regimes, macro announcements, or afternoon/closing dynamics.

## Execution assumptions

- **Execution Model:** Directional position execution at the mid-price $m_t = \frac{a_t^1 + b_t^1}{2}$. The agent acts as a directional trader selecting discrete directional actions based on forecast states.
- **Order Timing:** Evaluated at each preprocessed event step.
- **Omitted Microstructural Frictions (Source Provenance Gap):**
  - **Transaction Fees:** Zero exchange maker/taker fees or SEC/FINRA transaction fees modeled.
  - **Slippage / Market Impact:** No temporary or permanent market impact model; trades do not consume resting liquidity or move book queues.
  - **Queue Position & FIFO Fills:** Orders are not simulated resting in the LOB; no FIFO queue delay or cancellation risk is evaluated.
  - **Latency:** Zero latency assumed between observation of book state, policy inference, and order execution.
  - **Borrow / Shorting Constraints:** Symmetric long/short execution assumed without borrow fees or locate requirements.
- **Operational Reality:** In practical high-frequency trading, executing at mid-price without crossing the spread requires passive quoting, which introduces adverse selection (fills occur predominantly when the market moves against the quote). Crossing the spread via market orders incurs the full bid-ask spread plus taker fees, which typically dwarfs short-horizon OFI return predictability.

## Evidence

### Source-reported

Backtest results over the held-out one-hour test window (June 21, 2013, 10% test split) across AMZN, AAPL, and GOOG (Table 2, Section 3.4 of Chakrabarty & Pal, 2026):

| Ticker | Method | Avg Return | Volatility | Avg P/L Ratio | Profitability (%) | Max Drawdown |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **AMZN** | Tabular Q-Learning | -10.40 | 2,061.59 | 7.99 | 10.90% | -92,352.93 |
| | PPO | -49.31 | 1,567.98 | 2.16 | 29.06% | -9,293.30 |
| | **GRPO** | 1,796.64 | 10,745.69 | **5,341.55** | 62.12% | **-715.42** |
| | **GSPO** | **1,815.45** | 10,864.15 | 767.52 | 62.24% | -733.42 |
| **AAPL** | Tabular Q-Learning | 19.24 | 1,404.80 | 5.61 | 15.41% | -53,564.33 |
| | PPO | -44.33 | 1,538.85 | 1.66 | 34.98% | -12,346.35 |
| | **GRPO** | **1,925.01** | 6,408.17 | **97.69** | **72.86%** | **-1,235.17** |
| | **GSPO** | 1,835.91 | 6,059.83 | 51.82 | 70.82% | -1,428.34 |
| **GOOG** | Tabular Q-Learning | -63.75 | 2,462.16 | 4.16 | 18.46% | -94,733.55 |
| | PPO | -5.25 | 1,498.13 | 2.02 | 32.73% | -8,364.61 |
| | **GRPO** | 2,069.98 | 5,575.11 | **668.53** | **68.86%** | **-749.61** |
| | **GSPO** | **2,077.68** | 5,721.89 | 187.62 | 66.86% | -1,128.92 |

*Performance figures trace directly to Table 2 of arXiv:2605.25527v1. The source authors explicitly caution that these numbers should be viewed as indicative rather than conclusive due to the lack of repeated-seed uncertainty, bootstrap confidence intervals, and broader market regimes.*

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Failure of Standard RL Baselines:** Tabular Q-Learning failed to produce positive average returns on 2 out of 3 assets (AMZN: -10.40; GOOG: -63.75) and suffered massive drawdowns exceeding -90,000 on both tickers, demonstrating that state discretization severely degrades microstructural signal fidelity.
2. **PPO Underperformance:** Standard PPO generated negative average returns across all three instruments (AMZN: -49.31; AAPL: -44.33; GOOG: -5.25) with win rates ranging between 29.06% and 34.98%, confirming severe training instability when fitting a value-function critic to noisy high-frequency financial rewards.
3. **Elevated Policy Volatility:** GRPO and GSPO exhibited substantial return volatility (10,745–10,864 on AMZN vs 1,568 for PPO), indicating that while group normalization eliminates the critic, trajectory returns remain highly dispersed.
4. **Friction Fragility:** Because the backtest assumes frictionless mid-price fills without fee or slippage deductions, high event-cadence directional turnover would face severe degradation in live execution where crossing the spread incurs half-spread costs and exchange taker fees.

## Falsification plan

To falsify or establish the boundary conditions of this strategy family:

1. **Transaction Cost & Slippage Stress Test:**
   - Simulate execution with realistic NASDAQ equity fees (e.g., 0.30 cents/share taker fee or 0.5–2.0 bps equivalent) plus 1 tick adverse slippage.
   - *Research-defined falsification threshold:* Net average return $\le 0$ or net Sharpe ratio $\le 0$ across the 3 assets after deducting 1.0 bps round-trip transaction costs.
2. **Execution Latency Injection:**
   - Inject realistic inference and message-transmission latency ($\Delta \tau \in [1\text{ ms}, 50\text{ ms}]$) between order-book observation $t$ and fill event.
   - *Research-defined falsification threshold:* Strategy loses $>50\%$ of gross profitability at 5 ms latency, indicating signal alpha decays within the queue latency envelope.
3. **Multi-Seed Stability Audit:**
   - Train and evaluate 10 independent random seeds for GRPO, GSPO, and PPO under identical hyperparameters.
   - *Research-defined falsification threshold:* Inter-seed standard deviation of average return exceeds the mean return, or $>30\%$ of seeds fail to beat the zero-return benchmark.
4. **Out-of-Sample Regime & Breadth Generalization:**
   - Evaluate across a multi-month sample (e.g., 60 consecutive trading days across 2024–2026) encompassing high-volatility, low-volatility, trend, and range-bound regimes across an expanded universe of 20 liquid equities.
   - *Research-defined falsification threshold:* Out-of-sample win rate drops below $50.0\%$ or annualized Sharpe ratio drops below $0.50$.
5. **Ablation Against Simpler Forecast Baselines:**
   - Compare GRPO/GSPO against a non-RL parametric benchmark that simply trades directional signs: $a_t = \operatorname{sign}(\hat{\alpha}_t^{(h_1)})$ with fixed threshold $\theta_{\mathrm{entry}}$.
   - *Research-defined falsification threshold:* GRPO/GSPO fails to outperform the sign-threshold baseline by at least $15\%$ in net risk-adjusted return, indicating the complex RL machinery adds no incremental alpha over the supervised forecaster.

## Crypto portability

**Portability Classification:** `adapted` / `unproven`

### Crypto Porting Considerations
1. **Microstructural Alignment:**
   - Modern centralized cryptocurrency perpetual futures exchanges (e.g., Binance, OKX, Bybit) and high-throughput decentralized exchanges (e.g., Hyperliquid) stream Level-2 and Level-3 order books via high-speed WebSockets, allowing direct calculation of 10-level piecewise Order-Flow Imbalance ($\mathrm{OFI}_t$).
2. **Session and Market Differences:**
   - Unlike the 09:30–10:30 EST opening hour of NASDAQ equities, crypto operates 24/7/365 without formal open/close auctions. Volume and volatility patterns follow global timezone overlaps rather than exchange bells.
3. **Fee Hurdle:**
   - Crypto retail and VIP tier taker fees (typically 2.0 to 5.0 bps on perpetuals) are significantly wider than equity institutional tick fractions. A high-frequency directional strategy that flips positions on short-horizon event signals would rapidly be consumed by taker fees unless constrained to passive quoting or multi-second holding horizons.
4. **Funding Rate & Mark Price Risk:**
   - Perpetual futures introduce 8-hour / 4-hour / 1-hour funding rates and mark-price-based liquidations. Positions held across funding timestamps face cash-flow drag, and rapid order-book flash wicks can trigger exchange liquidation engines.
5. **API Latency Bottlenecks:**
   - While NASDAQ co-located HFT firms operate at sub-microsecond latencies, public crypto WebSocket/REST APIs have latency distributions between 5 ms and 100 ms with stringent IP rate limits (e.g., 50–100 orders/sec on Binance), which may prevent high-cadence event-level policy execution.
6. **Required Adaptation:**
   - Porting must be treated as `adapted` and `unproven`:
     - Retrain the 4-layer MLP forecaster on crypto perpetual LOBSTER-equivalent tick data (e.g., Binance tick/depth archives).
     - Incorporate funding rate and spread penalty into the RL reward function (`research-proposed`).
     - Limit action updates to minimum holding thresholds ($\ge 5$–10 seconds) to control fee burn.

## Limitations

- **Severely Constrained Sample:** Evaluated on only 1 single trading hour (June 21, 2013, 9:30–10:30 AM) across 3 US equities (`data gap`).
- **Underspecified Implementation Parameters:**
  - The exact numerical values for the 6 forecasting horizons $\{h_1, \dots, h_6\}$ are omitted (`underspecified`).
  - The exact algebraic formula for spread-scaled rewards is omitted (`underspecified`).
  - The group batch size $G$ and episode step horizon $T$ are omitted (`underspecified`).
  - Ticker-specific `PRICE_TO_PNL` scaling multipliers are omitted (`underspecified`).
- **Frictionless Simulation:** Omission of transaction fees, slippage, market impact, execution latency, and queue queueing dynamics makes reported returns heavily optimistic (`underspecified`).
- **Lack of Statistical Confidence Intervals:** No multi-seed runs, bootstrap standard errors, or p-values are reported; results represent single training runs per ticker (`underspecified`).
- **Unproven in Crypto:** No cryptocurrency testing was performed by the authors (`unproven`).

## Implementation status

`not-implemented`

No implementation of the OFI feature pipeline, 4-layer MLP multi-horizon forecaster, GRPO/GSPO training loops, or LOBSTER directional trading harness exists in `nautilus-quant-system`, PyBroker pipelines, or NautilusTrader harnesses.

## Adoption boundary

This record is research material only. A record being present in this repository does **not** mean:
- The strategy has demonstrated positive net alpha after realistic transaction costs and market impact;
- The RL policy generalizes across distinct market regimes, assets, or time periods;
- The strategy is approved for PyBroker implementation, NautilusTrader execution, paper trading, testnet, or live trading.

Implementation and adoption decisions require independent primary-source verification, full parameter resolution, and explicit review in downstream systems.

## Related Wiki records

- `[[quant/trading-r1-curricular-reinforcement-learning-llm-reasoning-2026-09-05]]` — Curricular reinforcement learning with GRPO for financial reasoning.
- `[[quant/llm-news-sentiment-direct-rl-crypto-trading-ddqn-grpo-2026-09-06]]` — Direct RL trading with GRPO on sentiment features.
- `[[quant/viperq-auction-market-theory-amt-rl-state-representation-2026-09-15]]` — Order flow pattern recognition via Auction Market Theory for RL trading.
- `[[quant/point-in-time-audit-btc-perp-negative-matched-budget-2026-08-26]]` — Point-in-time data audit and negative matched-budget evaluation for crypto perpetuals.
- `[[quant/strategy-research-record-spec-v1]]` — Current canonical strategy research schema specification.

## Sources

1. Sayak Chakrabarty, Souradip Pal. *"DeepSeekMath Meets Order Book: Group-Aware Policy Optimization for High-Frequency Directional Trading"*. arXiv preprint `arXiv:2605.25527v1 [q-fin.TR]`, submitted 25 May 2026. https://arxiv.org/abs/2605.25527
   - **Authors:** Sayak Chakrabarty (Northwestern University), Souradip Pal (Purdue University).
   - **Sample Period & Universe:** June 21, 2013 (09:30–10:30 AM); NASDAQ Level-10 LOBSTER data for AMZN (269,748 events), AAPL (400,391 events), GOOG (147,916 events).
   - **Primary Empirical Claims:** Table 2 held-out test split results showing GRPO (AMZN Avg Return 1796.64, Profitability 62.12%, Max DD -715.42; AAPL Avg Return 1925.01, Profitability 72.86%, Max DD -1235.17; GOOG Avg Return 2069.98, Profitability 68.86%, Max DD -749.61) and GSPO (AMZN Avg Return 1815.45, Profitability 62.24%, Max DD -733.42; AAPL Avg Return 1835.91, Profitability 70.82%, Max DD -1428.34; GOOG Avg Return 2077.68, Profitability 66.86%, Max DD -1128.92) vs Q-Learning and PPO.
2. Z. Shao et al. *"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"*. arXiv preprint `arXiv:2402.03300`, 2024. (Foundational reference for Group Relative Policy Optimization, GRPO).
3. R. Huang, T. Polak. *"LOBSTER: Limit Order Book System - The Efficient Reconstructor"*. Available at SSRN 1977201, 2011. (Primary data source protocol).
4. S. Jaddu, S. Vyetrenko. *"Combining Deep Learning and Order Flow Imbalance for Mid-Price Prediction"*. IEEE Conference on Computational Intelligence for Financial Engineering & Economics (CIFEr), 2023. (Primary reference for 10-level piecewise OFI feature extraction).
