---
schema: strategy-research-record-v1
title: "Hawkes Order-Flow Imbalance and Trade-Arrival Self-Excitation: Empirical Cross-Capture Microstructure Predictability and the Transaction-Cost Friction Barrier in BTCUSDT"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-microstructure
  - hawkes-processes
  - order-flow-imbalance
  - limit-order-book
  - point-process
  - crypto
  - btcusdt
  - leave-one-capture-out
  - falsification
  - transaction-costs
status: research-only
confidence: high
source_as_of: 2026-09-04
sources:
  - "https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/tree/656c923b51d36735bba496909d992b6894aa7116"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Hawkes Order-Flow Imbalance and Trade-Arrival Self-Excitation: Empirical Cross-Capture Microstructure Predictability and the Transaction-Cost Friction Barrier in BTCUSDT

## Provenance

- **Author:** Rattandeep Singh (`Rattandeep0500`).
- **Title:** "Hawkes–OFI Market Microstructure: BTCUSDT market-microstructure research using Hawkes processes, order-flow imbalance, and strict cross-capture out-of-sample validation"
- **Primary Source Repository:** [https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure)
- **Immutable Commit SHA:** `656c923b51d36735bba496909d992b6894aa7116` (`source-reported`).
- **Date / As-Of:** 2026-09-04 (`source-reported`).
- **License:** Public Open-Source Research Repository (`source-reported`).
- **Key Audited Artifacts in Repository:**
  - Research Monograph and Protocol: [`README.md`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/README.md) (`source-reported`).
  - Bivariate Hawkes Point-Process Estimator: [`src/models/bivariate_hawkes.py`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/src/models/bivariate_hawkes.py), [`src/models/binned_hawkes.py`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/src/models/binned_hawkes.py) (`source-reported`).
  - Trade Process Classification: [`src/models/trade_process.py`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/src/models/trade_process.py) (`source-reported`).
  - Order-Book Reconstruction & Synchronization: [`src/data/reconstruct_live_book.py`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/src/data/reconstruct_live_book.py), [`src/data/sync_orderbook.py`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/src/data/sync_orderbook.py) (`source-reported`).
  - Cont-Kukanov-Stoikov Level-1 to Level-10 OFI: [`src/data/ofi.py`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/src/data/ofi.py), [`src/data/multi_level_ofi.py`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/src/data/multi_level_ofi.py) (`source-reported`).
  - Multi-Capture Trade Alignment: [`experiments/build_multi_capture_trades.py`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/experiments/build_multi_capture_trades.py) (`source-reported`).
  - Leave-One-Capture-Out Cross-Validation Harness: [`experiments/leave_one_capture_out.py`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/experiments/leave_one_capture_out.py) (`source-reported`).
  - Statistical Hypothesis Testing & Block-Bootstrap: [`experiments/final_statistical_test.py`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/experiments/final_statistical_test.py) (`source-reported`).
  - Temporal-Resolution Sensitivity Harness: [`experiments/hawkes_resolution_prediction.py`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/experiments/hawkes_resolution_prediction.py) (`source-reported`).
  - Independent MATLAB Exact-Grid Replication: [`matlab/fit_hawkes_bivariate.m`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/matlab/fit_hawkes_bivariate.m) (`source-reported`).
- **Repository Deduplication Audit:** A comprehensive audit of all existing markdown strategy records in `alpha-strategy-research` confirmed zero pre-existing records citing `Rattandeep0500` or `hawkes-ofi-market-microstructure`. Other Hawkes-related records in the repository (e.g. `hawkes-self-exciting-lob-return-sign-forecasting-coe-2026-09-02.md` based on Cestari et al. 2023, `order-flow-two-layer-hawkes-core-reaction-rough-impact-2026-09-02.md` based on Muhle-Karbe et al. 2026, and `clusterlob-order-flow-imbalance-trader-behavior-clustering-2026-09-03.md`) investigate qualitative return signs under the COE model, rough market impact equilibrium theory, or K-means clustering on order books. Rattandeep Singh's work provides an independent, empirical high-frequency study on Binance BTCUSDT combining bivariate Hawkes self-excitation with multi-level Cont-Kukanov-Stoikov OFI under strict leave-one-capture-out out-of-sample evaluation, dual-engine Python/MATLAB validation, and an explicit quantification of the transaction-cost friction barrier.

## Economic mechanism

### Source-reported

Conventional microstructure models often treat trade arrivals as memoryless Poisson processes and model price impact through static Order-Flow Imbalance (OFI, Cont, Kukanov, and Stoikov 2014) computed across best quote depths. However, empirical trade arrivals in modern cryptocurrency order books exhibit severe temporal clustering (overdispersion, Fano factor 184.82 vs 1.0 for a Poisson process), driven by algorithmic execution of institutional metaorders (Bouchaud et al. 2004, Lillo and Farmer 2004) and reactive high-frequency order flows.

To capture this history-dependent dynamic, Singh formulates a bivariate self-exciting point process where buy and sell trade intensities ($\lambda_{\text{buy}}(t)$ and $\lambda_{\text{sell}}(t)$) are driven by baseline rates and exponential self-excitation kernels. From these conditional intensities, a signed **Hawkes pressure** statistic is derived:

$$\text{Hawkes pressure } H_t = \lambda_{\text{buy}}(t) - \lambda_{\text{sell}}(t)$$

Positive pressure indicates relatively stronger conditional buy clustering; negative pressure indicates relatively stronger conditional sell clustering.

Across three independent Binance BTCUSDT market episodes evaluated under leave-one-capture-out cross-validation:
1. **Predictive Information Beyond OFI:** While contemporaneous Level-1 OFI strongly tracks current price changes, its out-of-sample predictive power for future returns is non-existent ($R^2 = -0.19\%$ at 1 second, $+0.01\%$ at 5 seconds). In contrast, Hawkes pressure achieves positive out-of-sample $R^2$ across all held-out folds ($+1.12\%$ at 1 second, $+1.62\%$ at 5 seconds), demonstrating that temporal trade clustering contains genuinely predictive directional information about short-horizon returns.
2. **Subsumption of OFI:** Adding L1 OFI to Hawkes pressure does not improve performance ($R^2$ drops slightly from $+1.12\%$ to $+1.03\%$ at 1s, and from $+1.62\%$ to $+1.54\%$ at 5s), indicating that trade-arrival self-excitation subsumes static depth-based order flow imbalance at these horizons.
3. **Monotonic Return Response:** Sorting observations into within-capture Hawkes-pressure deciles yields a monotonic response in 5-second future mid-price returns, spanning from $-0.31\text{ bps}$ in the lowest decile to $+0.37\text{ bps}$ in the highest decile.

### Research interpretation

The empirical findings clarify the boundary between statistical microstructure predictability and tradable operational alpha:
- **Causal Mechanism:** Aggressive trade arrivals cluster because liquidity takers slice large parent orders into rapid child orders or because momentum algorithms react simultaneously to order-book imbalance. This concentrated demand depletes resting liquidity on one side of the book faster than market makers can replenish it, inducing short-term directional drift in the mid-price over 1 to 5 seconds.
- **The Microstructure Friction Barrier:** While the Hawkes pressure signal exhibits robust out-of-sample predictability and passes leave-one-capture-out validation, the **gross economic return between the top and bottom deciles is only $+0.68\text{ bps}$ over a 5-second horizon**.
- In cryptocurrency spot markets (such as Binance BTCUSDT), standard taker trading fees are $4.0\text{--}5.0\text{ bps}$ for retail VIP 0 (and $1.5\text{--}2.0\text{ bps}$ for institutional VIP 9), plus a typical bid-ask half-spread of $0.25\text{--}0.50\text{ bps}$. Round-trip transaction costs of $3.5\text{--}10.0\text{ bps}$ are **5 to 15 times larger than the entire gross signal edge**.
- **Operational Takeaway:** As a standalone active taker trading strategy, the hypothesis is economically falsified by transaction frictions. However, the signal possesses legitimate economic value for:
  1. *Passive Market Making / Adverse Selection Mitigation:* Skewing quoting spreads or cancelling resting quotes when opposing Hawkes pressure spikes, avoiding toxic fills.
  2. *Optimal Execution Scheduling:* Pacing metaorder execution schedules by conditioning order submission on favorable or neutral Hawkes pressure regimes.

## Signal

The signal extraction and predictive framework operates on an aligned discrete time grid with recursive state updates:

### 1. Data Alignment & Discrete Event Grid
- **Time Bin Resolution ($\Delta t$):** $100\text{ ms}$ ($0.1\text{ seconds}$) uniform discrete bins (`BIN_SIZE = 0.1`) (`source-reported`).
- **Trade Classification:** Classified into buy or sell using the Binance trade stream buyer market-maker flag `m`:
  $$\text{side}_i = \begin{cases} \text{sell}, & \text{if } m_i = \text{True} \\ \text{buy}, & \text{if } m_i = \text{False} \end{cases} \quad \text{(`source-reported`)}$$
- **Bin Aggregation:** Number of trades $N_{\text{buy}}[t]$ and $N_{\text{sell}}[t]$ in bin $t$; mid-price $P_{\text{mid}}[t]$ sampled at the end of each bin (`source-reported`).

### 2. Bivariate Self-Exciting Hawkes Estimator
- **Conditional Intensities:**
  $$\lambda_{\text{buy}}(t) = \mu_{\text{buy}} + \alpha_{\text{buy}} \sum_{t_k < t, \text{buy}} e^{-\beta (t - t_k)} \quad \text{(`source-reported`)}$$
  $$\lambda_{\text{sell}}(t) = \mu_{\text{sell}} + \alpha_{\text{sell}} \sum_{t_k < t, \text{sell}} e^{-\beta (t - t_k)} \quad \text{(`source-reported`)}$$
  with diagonal excitation (same-side self-excitation) and shared exponential decay rate $\beta > 0$ (`source-reported`).
- **Branching Ratios & Stationarity:**
  $$\eta_{\text{buy}} = \frac{\alpha_{\text{buy}}}{\beta}, \quad \eta_{\text{sell}} = \frac{\alpha_{\text{sell}}}{\beta} \quad \text{(`source-reported`)}$$
  Stationarity constraint: $\max(\eta_{\text{buy}}, \eta_{\text{sell}}) < 0.999$, parameterized via logistic sigmoid $\eta = 0.999 \cdot \text{expit}(x)$ (`source-reported`).
- **Discrete Recursive State Update:**
  Using an exact exponential recursive filter (`scipy.signal.lfilter`), the lagged excitation state evolves as:
  $$S_{\text{buy}}[t] = e^{-\beta \Delta t} S_{\text{buy}}[t-1] + N_{\text{buy}}[t-1] \quad \text{(`source-reported`)}$$
  $$S_{\text{sell}}[t] = e^{-\beta \Delta t} S_{\text{sell}}[t-1] + N_{\text{sell}}[t-1] \quad \text{(`source-reported`)}$$
  Conditional expected bin counts under binned Poisson likelihood:
  $$\Lambda_{\text{buy}}[t] = \mu_{\text{buy}} \Delta t + \eta_{\text{buy}} (1 - e^{-\beta \Delta t}) S_{\text{buy}}[t] \quad \text{(`source-reported`)}$$
  $$\Lambda_{\text{sell}}[t] = \mu_{\text{sell}} \Delta t + \eta_{\text{sell}} (1 - e^{-\beta \Delta t}) S_{\text{sell}}[t] \quad \text{(`source-reported`)}$$
  Instantaneous intensities:
  $$\lambda_{\text{buy}}[t] = \frac{\Lambda_{\text{buy}}[t]}{\Delta t}, \quad \lambda_{\text{sell}}[t] = \frac{\Lambda_{\text{sell}}[t]}{\Delta t} \quad \text{(`source-reported`)}$$
- **Optimization:** Minimization of Poisson negative log-likelihood across multiple starts using L-BFGS-B (`source-reported`).

### 3. Hawkes Pressure Signal
$$\text{Hawkes pressure } H_t = \lambda_{\text{buy}}[t] - \lambda_{\text{sell}}[t] \quad \text{(`source-reported`)}$$

### 4. Benchmark Cont-Kukanov-Stoikov Order Flow Imbalance (OFI)
Computed from reconstructed best bid $P_B(t)$, best ask $P_A(t)$, bid size $q_B(t)$, and ask size $q_A(t)$ (`source-reported`):
$$\Delta W_B(t) = \begin{cases} q_B(t), & \text{if } P_B(t) > P_B(t-1) \\ -q_B(t-1), & \text{if } P_B(t) < P_B(t-1) \\ q_B(t) - q_B(t-1), & \text{if } P_B(t) = P_B(t-1) \end{cases} \quad \text{(`source-reported`)}$$
$$\Delta W_A(t) = \begin{cases} -q_A(t), & \text{if } P_A(t) > P_A(t-1) \\ q_A(t-1), & \text{if } P_A(t) < P_A(t-1) \\ q_A(t-1) - q_A(t), & \text{if } P_A(t) = P_A(t-1) \end{cases} \quad \text{(`source-reported`)}$$
$$\text{OFI}_1(t) = \Delta W_B(t) + \Delta W_A(t) \quad \text{(`source-reported`)}$$

### 5. Return Target & Predictive Model
- **Target:** Future log mid-price return over horizon $h \in \{1\text{ s} \ (10\text{ bins}), 5\text{ s} \ (50\text{ bins})\}$:
  $$r_{t, t+h} = \ln(P_{\text{mid}}[t+h]) - \ln(P_{\text{mid}}[t]) \quad \text{(`source-reported`)}$$
- **Model:** Ridge regression ($\alpha = 1.0$) on z-score standardized training features with intercept unpenalized (`source-reported`).

### 6. Operational Trading Rules (Research-Proposed Translation)
To translate the predictive signal into a concrete benchmark trading strategy:
- **Long Entry:** Triggered when $H_t$ is in the top decile of rolling trailing 60-second Hawkes pressure (or $z(H_t) \ge 1.5$) (`research-proposed`).
- **Short Entry:** Triggered when $H_t$ is in the bottom decile of rolling trailing 60-second Hawkes pressure (or $z(H_t) \le -1.5$) (`research-proposed`).
- **Holding Horizon:** Exactly 5 seconds ($50$ bins) or upon Hawkes pressure crossing zero (`research-proposed`).
- **Execution Timing:** Signal formed at bin $t$ close is submitted for execution at $t+1$ ($100\text{ ms}$ execution lag) (`research-proposed`).
- **Position Sizing:** Fixed $1.0\times$ notional allocation or inverse historical volatility (`research-proposed`).

## Required data

- **Instrument:** `BTCUSDT` spot (`source-reported`).
- **Venue:** Binance Centralized Exchange (`source-reported`).
- **Market Type:** Spot Central Limit Order Book (CLOB) (`source-reported`).
- **Data Streams:**
  - WebSocket Diff Depth Stream: `btcusdt@depth` receiving incremental order-book changes (`source-reported`).
  - REST Snapshot: Initial 1000-level depth snapshot to seed the local book (`source-reported`).
  - WebSocket Trade Stream: `btcusdt@trade` receiving individual fill events with trade ID `t`, execution time `T`, price `p`, size `q`, and maker flag `m` (`source-reported`).
- **Reconstruction Invariants:** Verification of depth update sequence continuity (`last_update_id`, `final_update_id`), trade deduplication by `trade_id`, and exact timestamp synchronization (`source-reported`).
- **Sample Episodes:** Three independent live capture episodes (`capture_02`, `capture_03`, `capture_04`), each approximately 10 minutes (~600 seconds) in duration, totaling ~1,800 seconds, 39,442 trades, and 18,002 book states (`source-reported`).

## Execution assumptions

- **Source Evaluation Mode:** The primary source investigates mid-price predictability and linear regression out-of-sample $R^2$; it does not execute live simulated orders with order routing or fill matching (`source-reported`).
- **Taker Execution Assumptions (Active Trading):**
  - Order Type: Market orders crossing the spread at prevailing best bid/ask (`research-proposed`).
  - Trading Fees: $4.0\text{--}5.0\text{ bps}$ per side (Binance VIP 0 spot rate) or $1.5\text{--}2.0\text{ bps}$ (VIP 9) (`research-proposed`).
  - Bid-Ask Half-Spread: $0.25\text{--}0.50\text{ bps}$ ($0.50\text{--}1.00\text{ bps}$ full spread on BTCUSDT spot) (`research-proposed`).
  - Execution Latency: $10\text{--}50\text{ ms}$ WebSocket round-trip lag (`research-proposed`).
  - Slippage & Market Impact: Modeled at $0.5\text{ bps}$ for $0.1\text{ BTC}$ order size (`research-proposed`).
- **Passive Quoting Assumptions (Market Making):**
  - Order Type: Post-only limit orders resting at the best bid and ask (`research-proposed`).
  - Maker Fee: $0.0\text{--}1.0\text{ bps}$ (`research-proposed`).
  - Adverse Selection Filtering: If Hawkes pressure $H_t$ opposes resting quote (e.g. $H_t \gg 0$ on ask quote), cancel or widen quote by 1 tick (`research-proposed`).

## Evidence

### Source-reported

All figures below are directly extracted from the open-source repository commit `656c923b51d36735bba496909d992b6894aa7116` (Rattandeep Singh, September 2026):

#### 1. Dataset & High-Frequency Characteristics
- **Total Duration:** ~1,800 seconds across 3 independent episodes.
- **Total Trades:** 39,442 trades (21,952 buys, 17,490 sells).
- **Episode Breakdown:**
  - `capture_02`: 600 s duration, 13,117 trades, 21.89 trades/s, 62.38% buys, 37.62% sells.
  - `capture_03`: 600 s duration, 18,595 trades, 31.01 trades/s, 47.99% buys, 52.00% sells.
  - `capture_04`: 600 s duration, 7,730 trades, 12.89 trades/s, 62.68% buys, 37.32% sells.
- **Poisson Benchmark Rejection (Fano Overdispersion):**
  - Pooled 1-second trade count mean: $21.91\text{ trades/s}$.
  - Pooled 1-second trade count variance: $4,049.85$.
  - Pooled Fano factor ($\text{Var} / \text{Mean}$): **$184.82$** (vs $1.00$ for Poisson).
  - Capture Fano factors: `capture_02` = $227.87$, `capture_03` = $176.38$, `capture_04` = $120.37$.

#### 2. Hawkes Parameter Estimates Across Captures
- `capture_02`: $\mu_{\text{buy}} = 7.538$, $\mu_{\text{sell}} = 7.074$, $\beta = 5.175$, $\eta_{\text{buy}} = 0.447$, $\eta_{\text{sell}} = 0.140$, spectral radius $\rho = 0.447$.
- `capture_03`: $\mu_{\text{buy}} = 6.138$, $\mu_{\text{sell}} = 10.575$, $\beta = 3.057$, $\eta_{\text{buy}} = 0.587$, $\eta_{\text{sell}} = 0.344$, spectral radius $\rho = 0.587$.
- `capture_04`: $\mu_{\text{buy}} = 3.374$, $\mu_{\text{sell}} = 2.820$, $\beta = 1.032$, $\eta_{\text{buy}} = 0.582$, $\eta_{\text{sell}} = 0.417$, spectral radius $\rho = 0.582$.
- All estimated processes are stationary ($\rho < 1.0$), with buy branching consistently higher than sell branching across all captures.

#### 3. Leave-One-Capture-Out Out-of-Sample (OOS) Performance
Models trained on two full captures and evaluated exclusively on the held-out third capture:
- **Mean Out-of-Sample $R^2$:**
  - 1-second horizon: L1 OFI = **$-0.19\%$**, Hawkes pressure = **$+1.12\%$**, OFI + Hawkes = **$+1.03\%$**.
  - 5-second horizon: L1 OFI = **$+0.01\%$**, Hawkes pressure = **$+1.62\%$**, OFI + Hawkes = **$+1.54\%$**.
  - Average OOS $R^2$ improvement of Hawkes over L1 OFI: $\approx 1.31$ percentage points at 1s, and $\approx 1.61$ percentage points at 5s.
- **Mean Prediction / Return Correlation:**
  - 1-second horizon: L1 OFI = $0.060$, Hawkes pressure = **$0.122$**, OFI + Hawkes = $0.121$.
  - 5-second horizon: L1 OFI = $0.060$, Hawkes pressure = **$0.161$**, OFI + Hawkes = $0.159$.
- **Hawkes Pressure Sign Consistency:** Hawkes pressure OOS $R^2$ is strictly positive in every held-out fold at both forecast horizons.

#### 4. Decile Return Monotonicity & Economic Return Spread
Observations ranked into within-capture Hawkes pressure deciles:
- Lowest Decile (Extreme Sell Pressure): Mean future 5-second return = **$-0.31\text{ bps}$**.
- Highest Decile (Extreme Buy Pressure): Mean future 5-second return = **$+0.37\text{ bps}$**.
- Low-to-High Decile Return Spread: **$+0.68\text{ bps}$**.

#### 5. Temporal-Resolution Sensitivity
- **1-Second Horizon:**
  - $50\text{ ms}$: OOS $R^2$ = **$4.71\%$**, correlation = **$0.226$**.
  - $100\text{ ms}$: OOS $R^2$ = $3.38\%$, correlation = $0.143$.
  - $250\text{ ms}$: OOS $R^2$ = $2.45\%$, correlation = $0.101$.
  - $500\text{ ms}$: OOS $R^2$ = $1.79\%$, correlation = $0.074$.
- **5-Second Horizon:**
  - $50\text{ ms}$: OOS $R^2$ = $2.24\%$, correlation = $0.125$.
  - $100\text{ ms}$: OOS $R^2$ = $6.49\%$, correlation = $0.160$.
  - $250\text{ ms}$: OOS $R^2$ = **$6.54\%$**, correlation = $0.138$.
  - $500\text{ ms}$: OOS $R^2$ = $6.25\%$, correlation = $0.128$.

#### 6. Dual-Engine Python / MATLAB Independent Exact-Grid Replication
Independent implementation of the same binned likelihood and exact 100-ms grid in MATLAB (`fit_hawkes_bivariate.m`):
- Capture 04 Python estimates:
  $$\mu_{\text{buy}} = 3.3742947465, \quad \mu_{\text{sell}} = 2.8201315938, \quad \beta = 1.0316796766$$
  $$\eta_{\text{buy}} = 0.5820871370, \quad \eta_{\text{sell}} = 0.4165226456, \quad -\ln L = 28,784.4782933165$$
- MATLAB reproduces these estimates to within $10^{-7}$ relative error and matches the negative log-likelihood to machine numerical precision.

### Independently reproduced

`not independently reproduced`.

### Negative evidence

The empirical evidence from Singh's repository conclusively falsifies the viability of an active directional taker strategy based on Hawkes pressure:
1. **The Transaction-Cost Friction Barrier:** The gross low-to-high decile return spread is $+0.68\text{ bps}$ over a 5-second horizon. Even assuming the most favorable institutional VIP 9 taker fee ($1.5\text{ bps}$) and zero slippage, a round-trip taker trade costs $3.0\text{ bps} + 0.5\text{ bps spread} = 3.5\text{ bps}$, producing a net per-trade loss of $-2.82\text{ bps}$. For standard VIP 0 retail accounts ($5.0\text{ bps}$ fee), net loss is $-9.82\text{ bps}$ per trade.
2. **Failure of Static Level-1 OFI Out-of-Sample:** While Cont-Kukanov-Stoikov Level-1 OFI is widely cited for contemporaneous price impact, its out-of-sample predictive power is negative ($R^2 = -0.19\%$) at the 1-second horizon and indistinguishable from zero ($+0.01\%$) at 5 seconds.
3. **Decay Parameter Non-Stationarity:** The decay rate $\beta$ varies five-fold across the three captures (ranging from $1.032$ in `capture_04` to $5.175$ in `capture_02`), demonstrating that high-frequency market memory is highly non-stationary and sensitive to intraday volatility regimes.

## Falsification plan

To test whether Hawkes pressure can be adapted into an economically positive operational quantitative system:
1. **Passive Market-Making Adverse Selection Avoidance Test:**
   - Operational Setup: Simulate a passive market-making agent placing post-only limit orders at best bid/ask. Compare standard inventory-quoting vs Hawkes-gated quoting (cancelling resting bids when $H_t < -\tau$, and cancelling resting asks when $H_t > \tau$, where $\tau = 1.5\sigma_H$).
   - Metric: Post-fill 5-second adverse selection (realized spread).
   - Failure Rule: If Hawkes-gated quoting fails to improve realized spread by at least $0.50\text{ bps}$ net of cancellation latency, or if it reduces total fill rate by $> 30\%$, the passive market-making hypothesis is rejected (`research-defined falsification threshold`).
2. **Active Alpha Fee-Coverage Falsification Threshold:**
   - Operational Setup: Test whether any multi-feature combination (e.g. Hawkes pressure + multi-level OFI + depth-weighted spread) can achieve a top-decile return spread exceeding $6.0\text{ bps}$ at any horizon up to 60 seconds.
   - Failure Rule: If the gross return spread across extreme deciles remains $< 6.0\text{ bps}$, the active directional trading hypothesis is formally and permanently rejected as unviable under taker fee structures (`research-defined falsification threshold`).
3. **Cross-Asset & Regime Stability Test:**
   - Operational Setup: Replicate the leave-one-capture-out pipeline on ETHUSDT and SOLUSDT over 24-hour continuous captures.
   - Failure Rule: If Hawkes pressure produces negative out-of-sample $R^2$ in more than $30\%$ of rolling 1-hour test windows, the universal microstructure hypothesis is rejected (`research-defined falsification threshold`).

## Crypto portability

- **Portability Classification:** `direct` for Binance BTCUSDT spot CLOB markets; `adapted` / `unproven` for crypto perpetual futures, decentralized order books, and altcoin pairs.
- **Crypto-Specific Market Microstructure Dynamics:**
  - *Perpetual Futures Liquidations:* Perpetual futures feature forced liquidation engine orders. These programmatic market orders trigger violent, self-reinforcing Hawkes cascades that are substantially more severe than spot markets. Applying the model to perpetuals requires isolating liquidation trade tags from organic taker flow (`research-proposed`).
  - *Binance Trade Stream Timestamping:* Binance WebSocket trade events provide execution time `T` and engine time `E`. Out-of-order message arrival and network buffering can distort 100-ms binning unless sequenced strictly by `trade_id` (`source-reported`).
  - *Fee Structure Asymmetry:* Crypto spot taker fees ($4\text{--}5\text{ bps}$ retail) are significantly higher than traditional US equities ($0.3\text{--}1.0\text{ bps}$ taker fees), making the friction barrier far more punitive in crypto spot.

## Limitations

- `not independently reproduced`: Findings reflect direct code and empirical output audit from open-source repository commit `656c923b51d36735bba496909d992b6894aa7116`.
- `friction barrier`: Gross signal edge ($+0.68\text{ bps}$) is completely overwhelmed by exchange taker fees ($4.0\text{--}5.0\text{ bps}$ on Binance VIP 0).
- `data gap`: The empirical evaluation is based on three 10-minute captures (~30 minutes total). While dense in events (39,442 trades), it does not cover macro announcements, high-volatility flash crashes, or multi-day regime transitions.
- `regime instability`: Hawkes decay $\beta$ varies by $> 500\%$ across episodes, indicating that fixed parameter calibrations quickly degrade out of sample.
- `underspecified`: Limit order fill probabilities, queue position dynamics, and adverse selection under passive quoting were not explicitly backtested in the original study.

## Implementation status

- `not-implemented`.

This research record documents an external open-source market-microstructure study. No implementation in NautilusTrader, PyBroker, or any internal execution system has been performed. No paper, testnet, or live trading is authorized.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

This document serves as an empirical research and falsification capture on high-frequency order-flow self-excitation. Ingestion into Hermes Wiki Brain does not constitute approval for trading.

## Related Wiki records

- `[[quant/hawkes-self-exciting-lob-return-sign-forecasting-coe-2026-09-02]]` — Documents Hawkes self-exciting LOB return sign forecasting using the COE model on cryptocurrency data.
- `[[quant/order-flow-two-layer-hawkes-core-reaction-rough-impact-2026-09-02]]` — Theoretical two-layer Hawkes framework separating exogenous core orders from endogenous high-frequency reactions.
- `[[quant/clusterlob-order-flow-imbalance-trader-behavior-clustering-2026-09-03]]` — Unsupervised clustering of order flow imbalance for intraday return forecasting.
- `[[quant/deep-rl-market-making-regime-switching-bocpd-scenario-bandit-2026-09-11]]` — Deep RL market making under regime-switching order flow with Bayesian online change-point detection.
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Canonical standard for leakage-safe validation and out-of-sample partitioning.

## Sources

1. Rattandeep Singh (`Rattandeep0500`). *"Hawkes–OFI Market Microstructure: BTCUSDT market-microstructure research using Hawkes processes, order-flow imbalance, and strict cross-capture out-of-sample validation"*. Public GitHub repository, commit `656c923b51d36735bba496909d992b6894aa7116`, committed September 4, 2026.
   - Repository URL: [https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure)
   - Commit Tree: [https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/tree/656c923b51d36735bba496909d992b6894aa7116](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/tree/656c923b51d36735bba496909d992b6894aa7116)
   - Monograph / README: [`README.md`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/README.md)
   - Bivariate Hawkes Python Models: [`src/models/bivariate_hawkes.py`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/src/models/bivariate_hawkes.py), [`src/models/binned_hawkes.py`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/src/models/binned_hawkes.py)
   - Order Flow Imbalance Models: [`src/data/ofi.py`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/src/data/ofi.py), [`src/data/multi_level_ofi.py`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/src/data/multi_level_ofi.py)
   - Cross-Capture Validation Experiments: [`experiments/leave_one_capture_out.py`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/experiments/leave_one_capture_out.py), [`experiments/final_statistical_test.py`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/experiments/final_statistical_test.py), [`experiments/hawkes_resolution_prediction.py`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/experiments/hawkes_resolution_prediction.py)
   - MATLAB Exact-Grid Replication: [`matlab/fit_hawkes_bivariate.m`](https://github.com/Rattandeep0500/hawkes-ofi-market-microstructure/blob/656c923b51d36735bba496909d992b6894aa7116/matlab/fit_hawkes_bivariate.m)
2. Rama Cont, Arseniy Kukanov, and Sasha Stoikov. *"The Price Impact of Order Book Events"*. Journal of Financial Econometrics, 12(1):47–88, 2014. DOI: [10.1093/jjfinec/nbt003](https://doi.org/10.1093/jjfinec/nbt003).
3. Jean-Philippe Bouchaud, Yuval Gefen, Marc Potters, and Matthieu Wyart. *"Fluctuations and response in financial markets: the subtle nature of 'random' price changes"*. Quantitative Finance, 4(2):176–190, 2004. DOI: [10.1088/1469-7688/4/2/007](https://doi.org/10.1088/1469-7688/4/2/007).
4. Fabrizio Lillo and J. Doyne Farmer. *"The long memory of the efficient market"*. Studies in Nonlinear Dynamics & Econometrics, 8(3), 2004. DOI: [10.2202/1558-3708.1222](https://doi.org/10.2202/1558-3708.1222).
