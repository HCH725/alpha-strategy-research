---
schema: strategy-research-record-v1
title: "Agent-Based Genetic Algorithm for Crypto Trading Strategy Optimization: Coordinated Multi-Agent Parameter Evolution for Microstructure Adaptation"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - genetic-algorithm
  - multi-agent-systems
  - parameter-optimization
  - scalping
  - rsi-crossover
  - non-stationary-regimes
status: research-only
confidence: medium
source_as_of: "2025-10-09"
sources:
  - "Qiushi Tian, Churong Liang, Kairan Hong, and Runnan Li, 'Agent-Based Genetic Algorithm for Crypto Trading Strategy Optimization', arXiv preprint arXiv:2510.07943v1 [cs.AI], October 9, 2025. https://arxiv.org/abs/2510.07943"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Agent-Based Genetic Algorithm for Crypto Trading Strategy Optimization: Coordinated Multi-Agent Parameter Evolution for Microstructure Adaptation

## Provenance

- **Title:** Agent-Based Genetic Algorithm for Crypto Trading Strategy Optimization
- **Authors:** Qiushi Tian, Churong Liang, Kairan Hong, and Runnan Li (Corresponding author)
- **Affiliation:** Beijing University of Posts and Telecommunications, Beijing, China
- **Preprint Identifier:** arXiv:2510.07943v1 [cs.AI], submitted October 9, 2025 (`source-reported`)
- **Digital Object Identifier (DOI):** [10.48550/arXiv.2510.07943](https://doi.org/10.48550/arXiv.2510.07943) (`source-reported`)
- **Canonical Abstract URL:** [https://arxiv.org/abs/2510.07943](https://arxiv.org/abs/2510.07943)
- **Canonical Full-Text HTML URL:** [https://arxiv.org/html/2510.07943v1](https://arxiv.org/html/2510.07943v1)
- **Canonical PDF URL:** [https://arxiv.org/pdf/2510.07943](https://arxiv.org/pdf/2510.07943)
- **Subject Classifications:** Artificial Intelligence (`cs.AI`), Computational Finance (`q-fin.CP`) (`source-reported`)
- **Primary Source Inspection:** Audited directly from the complete 6-page primary source manuscript of `arXiv:2510.07943v1`, including mathematical formulation, multi-agent architecture (Section 3), experimental setup on 5-minute cryptocurrency data (Section 4), and quantitative comparison tables (Tables 1 & 2).
- **Pre-Write Deduplication & Identity Verification:** An exhaustive scan across all records in `alpha-strategy-research` confirmed zero existing records citing `2510.07943`, `Qiushi Tian`, `Churong Liang`, `CGA-Agent`, or `Scalping Strategy(SS)`. Existing evolutionary or multi-agent records in the repository examine formulaic alpha factor synthesis with genetic programming for daily Bitcoin (`bitcoin-ga-alpha-factor-sentiment-stacking-ensemble-2026-09-01.md`, citing Yang 2024 [6]), anti-overfitting objective gates (`gt-score-anti-overfitting-objective-multi-metric-gate-2026-09-05.md`), or LLM-agent factor mining (`alphalogics-market-logic-multi-agent-factor-generation-2026-09-05.md`); none capture a distributed 6-agent cooperative architecture (Analysis, Generation, Evaluation, Selection, Crossover, Mutation) dedicated to high-frequency (5-minute) dynamic strategy parameter adaptation across rolling windows.

## Economic mechanism

### Source-reported

Cryptocurrency markets exhibit extreme price volatility, pronounced downside and tail risks, non-stationary dynamics, and complex herding behaviors (Baur & Dimpfl 2018; Dobrynskaya 2024; Ahelegbey et al. 2021; Bouri et al. 2019). These features render traditional, static parameter optimization methods fundamentally inadequate, as fixed parameters optimized over a past window rapidly decay as market regimes change.

Traditional Genetic Algorithms (GAs) provide global, gradient-free search across non-linear multimodal objective landscapes, but standard implementations operate within static parameter spaces and fixed fitness functions. They lack mechanisms to integrate real-time market intelligence and dynamic strategy performance feedback into evolutionary operators.

To overcome this limitation, the authors introduce **Crypto Genetic Algorithm Agent (CGA-Agent)**, which decomposes the parameter optimization problem into a coordinated Multi-Agent System (MAS) comprising six specialized agents:
1. **Analysis Agent ($\mathcal{A}_{\text{anal}}$):** Evaluates prevailing market data and strategy structure to define parameter search directions and boundary constraints (`source-reported`).
2. **Generate Agent ($\mathcal{A}_{\text{gen}}$):** Creates candidate parameter chromosomes based on the analytical directions and default baseline values (`source-reported`).
3. **Evaluate Agent ($\mathcal{A}_{\text{eval}}$):** Executes automated strategy backtests and computes a composite fitness score across 11 financial metrics (`source-reported`).
4. **Choose Agent ($\mathcal{A}_{\text{cho}}$):** Retains elite parameter configurations (top 20%) and selects remaining genes via fitness-proportional roulette sampling (`source-reported`).
5. **Crossover Agent ($\mathcal{A}_{\text{cross}}$):** Combines parameter traits from elite configurations using quantitative market heuristics and predefined crossover templates (`source-reported`).
6. **Mutation Agent ($\mathcal{A}_{\text{mut}}$):** Introduces localized parameter perturbations based on advantageous features of historical top performers (`source-reported`).

By executing this multi-agent cycle periodically on a rolling window ($\Delta t = 30$ trading days), the strategy parameters dynamically track shifts in market microstructure without manual intervention (`source-reported`).

### Research interpretation

The economic foundation of the CGA-Agent Scalping Strategy is **regime-conditional parameter adaptation** applied to high-frequency momentum and mean-reversion filters:
1. **Dual RSI Crossover:** Faster RSI oscillators capture short-term microstructure momentum bursts, while slower RSI baselines establish the intermediate trend. In ranging regimes, narrow RSI spans over-trade and suffer churn; in trending regimes, wider spans lag and enter late (`research-proposed`).
2. **Filter Stack Interaction:**
   - Fast Moving Average Filter (FMAF) gates entry on short-term trend alignment (`research-proposed`).
   - Slow Moving Average Filter (SMAF) prevents fighting higher-timeframe momentum (`research-proposed`).
   - Slope Filter (SF) uses ATR normalization ($\frac{\Delta MA}{ATR}$) to enforce that trades are only executed when directional volatility expansion is confirmed (`research-proposed`).
3. **Regime Switching Evidence:** The empirical parameter shift observed on ETH at Day 60 demonstrates how the system adapts: when directional momentum becomes well-established, the algorithm activates the Slow Moving Average Filter (`SMAF: False -> True`) while deactivating the Slope Filter (`SF: True -> False`), and fine-tunes RSI lengths ($28 \to 25$ for fast RSI, $6 \to 7$ for slow RSI) (`source-reported`).
4. **Overfitting & Noise Vulnerability:** High-frequency (5-minute) parameter re-optimization across 30-day windows inherently risks fitting in-sample noise rather than persistent structural dynamics. Without strict walk-forward embargoes or transaction cost hurdles, the reported gross Sharpe ratios may fail out-of-sample once realistic taker fees and bid-ask slippage are applied (`research-proposed`).

## Signal

### Mathematical Problem Formulation

Consider a parametric trading strategy $\mathcal{S}(\boldsymbol{\theta})$, where $\boldsymbol{\theta} \in \Theta \subset \mathbb{R}^d$ denotes the $d$-dimensional strategy parameter vector and $\Theta$ represents the practical parameter domain (`source-reported`).

The rolling dynamic optimization problem is formulated as:
$$\boldsymbol{\theta}^*_{t+\Delta t} = \arg\max_{\boldsymbol{\theta} \in \Theta} \mathcal{F}(\mathcal{S}(\boldsymbol{\theta}), \mathcal{D}_{t:\Delta t}) \quad \text{(`source-reported`)}$$
where:
- $\boldsymbol{\theta}^*_{t+\Delta t}$ is the optimal parameter configuration for the forward period (`source-reported`).
- $\mathcal{D}_{t:\Delta t}$ is a rolling window of recent market data of length $\Delta t = 30$ trading days (`source-reported`).
- $\mathcal{F}(\cdot)$ is the multi-metric fitness function (`source-reported`).

The fitness function aggregates 11 backtest performance metrics:
$$\mathcal{F}(\mathcal{S}(\boldsymbol{\theta}), \mathcal{D}) = \sum_{j=1}^{11} w_j \cdot \phi_j(\mathcal{S}(\boldsymbol{\theta}), \mathcal{D}) \quad \text{(`source-reported`)}$$
where $\phi_j(\cdot)$ denotes the score of an individual metric (including Sharpe Ratio, Annualized Return, Win Rate, Returns Volatility, Sortino Ratio, and Risk-Return Ratio) and $w_j$ represents the weight of metric $j$ (`source-reported`).

### Multi-Agent Coordination Mechanisms

1. **Initialization Phase:**
   - $\mathcal{A}_{\text{anal}}$ determines parameter optimization directions using strategy characteristics and market state (`source-reported`).
   - $\mathcal{A}_{\text{gen}}$ instantiates initial parameter gene population using default values perturbed along specified directions (`source-reported`).
2. **Evaluation & Elite Selection:**
   - $\mathcal{A}_{\text{eval}}$ evaluates each parameter chromosome $\mathbf{g}_j$ via backtesting, derives fitness score $s_j = \mathcal{F}(\mathcal{S}(\boldsymbol{\theta}_j), \mathcal{D})$, and maintains the global best parameter record (`source-reported`).
   - $\mathcal{A}_{\text{cho}}$ sorts chromosomes in descending fitness order. Chromosomes in the top 20% are directly admitted to the elite pool (`source-reported`).
   - The remaining genes are sampled probabilistically with weights:
     $$w_j = s_j - s_{\min} + 1 \quad \text{(`source-reported`)}$$
     $$P(\mathbf{g}_j) = \frac{w_j}{\sum_{i=1}^k w_i} \quad \text{(`source-reported`)}$$
     where $s_{\min}$ is the minimum fitness score in the current population (`source-reported`).
3. **Crossover & Mutation Loop:**
   - $\mathcal{A}_{\text{cross}}$ combines parameter traits from the elite pool using quantitative prior knowledge and crossover templates (`source-reported`).
   - $\mathcal{A}_{\text{mut}}$ samples offspring at a predefined percentage, identifies advantageous parameter traits of historical top performers, and executes template-based mutations (`source-reported`).
   - The loop iterates until convergence or termination criteria are satisfied (`source-reported`).

### Baseline Scalping Strategy (SS) Architecture

The underlying trading logic is a high-frequency Scalping Strategy governed by a Dual RSI Crossover with three trend-confirmation filters:
- **Primary Entry Signals:**
  - **Long Entry / Buy Signal:** Fast RSI crosses above Slow RSI ($RSI_{\text{fast}} > RSI_{\text{slow}}$) (`source-reported`).
  - **Short Entry / Sell Signal:** Fast RSI crosses below Slow RSI ($RSI_{\text{fast}} < RSI_{\text{slow}}$) (`source-reported`).
- **Confirmation Filter Stack:**
  1. **Fast Moving Average Filter (FMAF):** Confirms short-term trend alignment (`source-reported`).
  2. **Slow Moving Average Filter (SMAF):** Confirms long-term trend alignment (`source-reported`).
  3. **Slope Filter (SF):** Measures trend acceleration normalized by the Average True Range ($ATR$) (`source-reported`).
- **Operational Rules & Timing (`research-proposed`):**
  - Bar formation: 5-minute closed bars (`source-reported`).
  - Signal evaluation: At the close of bar $t$ (`research-proposed`).
  - Order execution: Market order fill at the open of bar $t+1$ (`research-proposed`).
  - Position sizing: 100% equity allocation per instrument, no leverage (`research-proposed`).
  - Position holding: Maintained until an opposite crossover occurs or stop criteria trigger (`research-proposed`).
  - Underspecification: The exact vector of 11 fitness weights $(w_1, \dots, w_{11})$, the exact MA periods for FMAF/SMAF, and the numeric ATR slope thresholds are not explicitly tabulated in the paper text (`source provenance gap`).

## Required data

- **Instruments:** Bitcoin (`BTC/USDT`), Ethereum (`ETH/USDT`), Binance Coin (`BNB/USDT`) (`source-reported`).
- **Venue:** Centralized cryptocurrency exchange with liquid 5-minute order book trading (e.g., Binance) (`source-reported`).
- **Market Type:** Spot or USD-M Perpetual Futures (`research-proposed`).
- **Timeframe:** 5-minute candlestick bars (`5m` OHLCV) (`source-reported`).
- **Sample Period:** December 25, 2024 to September 1, 2025 (252 total days) (`source-reported`).
- **Required Fields:** Open, High, Low, Close, Volume (`source-reported`).
- **Derived Features:**
  - Fast RSI ($RSI_1$, length calibrated dynamically, e.g. 25–28) (`source-reported`).
  - Slow RSI ($RSI_2$, length calibrated dynamically, e.g. 6–7) (`source-reported`).
  - Fast Moving Average (FMA) (`source-reported`).
  - Slow Moving Average (SMA) (`source-reported`).
  - Average True Range ($ATR$) and MA slope (`source-reported`).
- **Point-in-Time & Window Structure:** Rolling 30-day lookback window ($\Delta t = 30$ trading days) for parameter re-optimization (`source-reported`).

## Execution assumptions

- **Order Execution:** Market orders executed at the open of the bar immediately following a crossover signal (`research-proposed`).
- **Execution Delay / Latency:** 5-minute bar execution implies latency tolerance on the order of 100–500 ms, feasible on standard exchange REST/WebSocket APIs (`research-proposed`).
- **Transaction Costs & Slippage:**
  - *Source Assumption:* The primary source paper does not specify explicit fee tiers, exchange commissions, or slippage models (`source provenance gap`).
  - *Research-Proposed Baseline:* On Binance VIP0 spot, maker/taker fee is 10 bps (0.10%), or 2 bps / 5 bps on USD-M perpetual futures. For a high-frequency 5m scalping strategy, round-trip costs of 5 to 10 bps represent a critical drag that could consume a substantial portion of reported total PnL (`research-proposed`).
- **Borrow / Financing:** Long/short positions assumed symmetrical; on spot markets, shorting requires margin borrowing, whereas perpetual futures allow native symmetrical shorting without borrow friction (`research-proposed`).
- **Capital Allocation:** Single-asset allocation per sub-backtest; no cross-asset portfolio netting in reported results (`source-reported`).

## Evidence

### Source-reported

All performance figures below are directly transcribed from Tian, Liang, Hong, and Li (`arXiv:2510.07943v1`, October 2025, Section 4.3, Tables 1 & 2), evaluated over 252 days of 5-minute data (December 25, 2024 to September 1, 2025):

#### 1. Multi-Asset Comparative Performance (Table 1)

| Asset | Strategy | Total PnL (%) | Returns Volatility | Sharpe Ratio | Sortino Ratio | Risk-Return Ratio |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **BTC** | Scalping Strategy (Baseline) | 1.68% | 0.12 | 1.36 | 2.81 | 0.035 |
| **BTC** | **CGA-Agent-SS (Proposed)** | **2.17%** | 0.17 | 1.26 | 2.51 | **0.025** |
| **ETH** | Scalping Strategy (Baseline) | 0.64% | 0.14 | 0.46 | 0.80 | 0.013 |
| **ETH** | **CGA-Agent-SS (Proposed)** | **4.16%** | 0.20 | **2.09** | **4.11** | **0.031** |
| **BNB** | Scalping Strategy (Baseline) | 3.44% | 0.25 | 1.35 | 2.61 | 0.044 |
| **BNB** | **CGA-Agent-SS (Proposed)** | **9.27%** | 0.30 | **2.99** | **6.55** | **0.054** |

- **Reported Relative Improvements:**
  - **BTC:** Total PnL increased by +29.17% relative to baseline; Risk-Return Ratio improved (decreased) by ~28.57% (`source-reported`).
  - **ETH:** Total PnL increased by +550.00% (from 0.64% to 4.16%); Sharpe Ratio increased by +354.35% (from 0.46 to 2.09); Sortino Ratio increased by +413.75% (from 0.80 to 4.11); Returns Volatility increased by +42.86% (`source-reported`).
  - **BNB:** Total PnL increased by +169.48% (from 3.44% to 9.27%); Sharpe Ratio increased by +121.48% (from 1.35 to 2.99); Sortino Ratio increased by +150.96% (from 2.61 to 6.55); Returns Volatility rose by +20.00% (`source-reported`).

#### 2. Parameter Adaptation on Day 60 for ETH (Table 2)

| Parameter | Baseline / Old Value | Adapted / New Value | Qualitative Adaptation Mechanism |
| :--- | :---: | :---: | :--- |
| **RSI1 Length** | 28 | 25 | Faster response time to short-term momentum shifts (`source-reported`) |
| **RSI2 Length** | 6 | 7 | Slightly smoothed baseline threshold (`source-reported`) |
| **SMAF (Slow MA Filter)** | False | True | Activated long-term trend filter to suppress counter-trend whipsaws (`source-reported`) |
| **SF (Slope Filter)** | True | False | Deactivated ATR slope constraint to allow trend continuation entries (`source-reported`) |

### Independently reproduced

`Not independently reproduced.` The multi-agent coordination codebase, prompt templates, and backtest simulator have not been independently implemented or executed within our internal research environment.

### Negative evidence

1. **Sharpe Ratio Degradation on Bitcoin:** In the BTC scenario, although total PnL increased from 1.68% to 2.17%, the Sharpe Ratio dropped from 1.36 to 1.26 (-7.35%) and the Sortino Ratio dropped from 2.81 to 2.51 (-10.68%) due to a 41.7% surge in returns volatility (0.12 to 0.17). This proves that genetic parameter adaptation can increase downside volatility and produce suboptimal risk-adjusted performance on certain assets (`source-reported`).
2. **Gross Return vs. Trading Friction Sensitivity:** The absolute total returns reported over 252 days are modest: 2.17% for BTC, 4.16% for ETH, and 9.27% for BNB. In a 5-minute scalping strategy that executes frequent trades, round-trip exchange fees (e.g., 4–10 bps) and slippage could easily exceed the total cumulative return, turning all three scenarios net-negative (`research-proposed`).
3. **Absence of Cost Modeling:** The omission of transaction cost analysis in high-frequency crypto scalping is a major vulnerability, indicating potential paper-return illusion (`research-proposed`).

## Falsification plan

To falsify the claim that multi-agent genetic optimization produces durable out-of-sample alpha:

1. **Transaction Cost & Slippage Drag Test (`research-defined falsification threshold`):**
   - *Test:* Implement tiered transaction costs: Tier 1 (2 bps maker / 4 bps taker), Tier 2 (5 bps taker + 2 bps slippage = 7 bps one-way), Tier 3 (10 bps spot).
   - *Threshold / Decision Rule:* If net Sharpe Ratio drops below 0.50 or net cumulative PnL turns negative under Tier 1 (4 bps round-trip) across BTC and ETH, the strategy is falsified as an unviable paper artifact that cannot survive real-world crypto frictions.
2. **Purged Walk-Forward Embargo Test (`research-defined falsification threshold`):**
   - *Test:* Re-run the 30-day rolling calibration with a 3-day embargo (purging) before the out-of-sample test window to eliminate serial correlation leakage.
   - *Threshold / Decision Rule:* If out-of-sample Sharpe decays by more than 50% relative to the in-sample fitness score, the multi-agent optimization is rejected as an overfitted curve-fitting engine.
3. **Agent Ablation vs. Classical Optimization Benchmark (`research-defined falsification threshold`):**
   - *Test:* Compare CGA-Agent against: (a) Static baseline parameters; (b) Single-agent genetic algorithm (standard DEAP/scikit-opt); (c) Rolling Bayesian optimization (Tree-structured Parzen Estimator).
   - *Threshold / Decision Rule:* If CGA-Agent does not achieve a statistically significant improvement ($t$-statistic $> 2.0$ on Information Ratio) over rolling Bayesian optimization, the 6-agent LLM/heuristic complexity is deemed superfluous.
4. **Out-of-Sample Market Regime Shift Test (`research-defined falsification threshold`):**
   - *Test:* Evaluate across an extended multi-year backtest covering severe bear markets (e.g. 2022 crypto winter) and high-volatility flash crashes.
   - *Threshold / Decision Rule:* If Maximum Drawdown exceeds 25% on any asset or the strategy suffers more than 60 consecutive days of drawdown, parameter adaptation is ruled ineffective against structural regime shocks.

## Crypto portability

- **Portability Status:** `direct` (`source-reported`). The strategy and multi-agent framework were designed, tested, and evaluated natively on major cryptocurrency pairs (BTC, ETH, BNB).
- **Perpetual vs. Spot Mechanics:**
  - On spot markets, short signals cannot be executed without margin borrow facilities, incurring borrow interest and liquidation risk (`research-proposed`).
  - On perpetual futures markets, shorting is native, but funding rate payments (typically exchanged every 8 hours) could erode scalping returns if holding positions across funding timestamps against prevailing sentiment (`research-proposed`).
- **24/7 Session & Microstructure:** Cryptocurrency trading operates continuously with no market closes, eliminating overnight gap risk but requiring continuous 24/7 algorithmic execution and robust error handling for exchange WebSocket disconnections (`research-proposed`).
- **Venue Fragmentation & Latency:** Spreads and liquidity vary widely between Binance, Bybit, Coinbase, and OKX. Porting to lower-tier exchanges would amplify slippage beyond the strategy's thin margin of profitability (`research-proposed`).

## Limitations

1. **Omission of Transaction Costs (`source provenance gap`):** The paper does not incorporate exchange fees, bid-ask spread, or execution slippage into the backtesting engine. In a 5-minute scalping regime, this is the single greatest threat to live viability.
2. **Underspecified Fitness Function Weights (`source provenance gap`):** The exact numeric values for the 11 weights $w_j$ in Equation (2) are omitted, requiring research estimation to reconstruct.
3. **Underspecified Moving Average Specifications (`source provenance gap`):** The exact calculation types (SMA, EMA, WMA) and parameter bounds for FMAF, SMAF, and SF are not fully tabulated.
4. **Limited Backtest Duration:** The evaluation covers 252 days (December 2024 to September 2025), which is a relatively short temporal sample that does not span a full multi-year market cycle.
5. **Computational Overhead:** Running a 6-agent multi-agent cycle every 30 days incurs significant computational latency and potential LLM API cost if agents utilize generative models for analysis and mutation.

## Implementation status

- `not-implemented`. This record represents an external research capture and normalized evaluation. No implementation in NautilusTrader, PyBroker, paper trading, or live execution has been performed.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`
- This record serves exclusively as normalized upstream research intelligence for Hermes Loop A hypothesis generation. It is not approved for live trading, testnet deployment, paper execution, or production implementation.

## Related Wiki records

- `[[quant/bitcoin-ga-alpha-factor-sentiment-stacking-ensemble-2026-09-01]]` — Genetic algorithm alpha factor construction with sentiment stacking ensemble for Bitcoin daily trend (citing Yang 2024).
- `[[quant/gt-score-anti-overfitting-objective-multi-metric-gate-2026-09-05]]` — Multi-metric gated anti-overfitting objective for evolutionary and systematic parameter selection.
- `[[quant/crypto-walk-forward-window-optimization-double-oos-momentum-2026-09-04]]` — Double out-of-sample walk-forward parameter optimization on BTC, ETH, and BNB.
- `[[quant/crypto-drl-execution-overlay-multi-pair-trading-2026-09-01]]` — Dynamic multi-pair crypto trading with reinforcement learning and adaptive execution overlays.
- `[[quant/alphalogics-market-logic-multi-agent-factor-generation-2026-09-05]]` — Multi-agent system for market logic discovery and formulaic alpha factor generation.

## Sources

1. **Primary Research Paper:**
   - Qiushi Tian, Churong Liang, Kairan Hong, and Runnan Li, *"Agent-Based Genetic Algorithm for Crypto Trading Strategy Optimization"*, arXiv preprint `arXiv:2510.07943v1 [cs.AI]`, submitted October 9, 2025.
   - Canonical URL: [https://arxiv.org/abs/2510.07943](https://arxiv.org/abs/2510.07943)
   - DOI: [10.48550/arXiv.2510.07943](https://doi.org/10.48550/arXiv.2510.07943)
   - HTML Full-Text: [https://arxiv.org/html/2510.07943v1](https://arxiv.org/html/2510.07943v1)
   - Primary PDF: [https://arxiv.org/pdf/2510.07943](https://arxiv.org/pdf/2510.07943)
2. **Foundational Predecessors & Baselines Cited in Primary Source:**
   - Franklin Allen and Risto Karjalainen, *"Using genetic algorithms to find technical trading rules"*, *Journal of Financial Economics*, 51(2):245–271, 1999. DOI: `10.1016/S0304-405X(98)00052-X`.
   - Quechen Yang, *"Blending ensemble for classification with genetic-algorithm generated alpha factors and sentiments (GAS)"*, arXiv preprint `arXiv:2411.03035`, 2024. URL: [https://arxiv.org/abs/2411.03035](https://arxiv.org/abs/2411.03035).
   - Dirk G. Baur and Thomas Dimpfl, *"Asymmetric volatility in cryptocurrencies"*, *Economics Letters*, 173:148–151, 2018. DOI: `10.1016/j.econlet.2018.09.008`.
   - Victoria Dobrynskaya, *"Is downside risk priced in cryptocurrency market?"*, *International Review of Financial Analysis*, 91:102947, 2024. DOI: `10.1016/j.irfa.2023.102947`.
   - David F. Ahelegbey, Paolo Giudici, and Fatemeh Mojtahedi, *"Tail risk measurement in crypto-asset markets"*, *International Review of Financial Analysis*, 73:101604, 2021. DOI: `10.1016/j.irfa.2020.101604`.
