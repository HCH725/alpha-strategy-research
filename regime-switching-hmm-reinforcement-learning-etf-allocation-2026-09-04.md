---
schema: strategy-research-record-v1
title: "Regime-Based Tactical ETF Allocation via Hidden Markov Models and Tabular Reinforcement Learning"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - asset-allocation
  - regime-switching
  - hidden-markov-models
  - reinforcement-learning
  - dynamic-programming
  - safe-haven-assets
  - vix
  - spy
  - tlt
  - gld
status: research-only
confidence: medium
source_as_of: 2026-05-27
sources:
  - https://arxiv.org/abs/2605.27848
  - https://arxiv.org/pdf/2605.27848
  - https://doi.org/10.48550/arXiv.2605.27848
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Regime-Based Tactical ETF Allocation via Hidden Markov Models and Tabular Reinforcement Learning

## Provenance

- **Primary Source:** Ajay Kumar Verma (Independent Researcher), Nunik Srikandi Putri (Aenimatica Tech Research and Development, Independent Researcher), and Neo Paul Lesupi (Independent Researcher), *"Regime-Based Portfolio Allocation Using Hidden Markov Models and Reinforcement Learning"*, arXiv preprint `arXiv:2605.27848v1 [q-fin.PM, q-fin.ST]`, submitted May 27, 2026 (paper dated November 2025 in preprint manuscript). DOI: `10.48550/arXiv.2605.27848`. Stable abstract URL: `https://arxiv.org/abs/2605.27848`. Full PDF: `https://arxiv.org/pdf/2605.27848`.
- **Target Universe & Data Sample:** Daily closing prices for SPY (SPDR S&P 500 ETF Trust), TLT (iShares 20+ Year Treasury Bond ETF), GLD (SPDR Gold Shares), and CBOE Volatility Index (VIX) retrieved from Yahoo Finance spanning 2004 to 2025 (over 21 calendar years). Daily returns are converted to log-returns $r_t = \ln(P_t/P_{t-1})$ for additivity and aggregation properties. Volatility shocks are captured through daily changes in the VIX index ($\Delta\text{VIX}_t = \text{VIX}_t - \text{VIX}_{t-1}$).
- **Evaluation & Walk-Forward Protocol:** Chronological split of 70% in-sample training window and 30% strictly out-of-sample test window. Strategy execution is modeled at daily frequency with a strict one-day execution lag (actions determined at time $t$ based on predicted regimes are applied to returns realized over $t+1$) to prevent look-ahead bias.
- **Repository Deduplication:** Repository-wide grep on 2026-09-04 verifies zero existing records matching `arXiv:2605.27848` or authors Ajay Kumar Verma, Nunik Srikandi Putri, or Neo Paul Lesupi. Existing asset allocation records in the repository (`deep-portfolio-optimization-attention-lstm-omega-cvar-risk-parity-2026-09-03.md`, `continuous-macro-timing-growth-defensive-style-allocation-2026-09-02.md`, `continuous-cash-overlay-growth-defensive-slow-tail-vshape-max-cash-2026-09-03.md`, `dynamic-portfolio-optimization-cvar-stochastic-control-hjb-2026-09-02.md`, `regime-adaptive-continual-learning-portfolio-management-recap-2026-09-02.md`) address neural surrogate losses (Omega/CVaR), continuous growth-vs-defensive macro timing filters, cash overlay brake mechanisms, continuous-time HJB stochastic control, or continual learning drift adaptation on NAS100 equities. This record uniquely captures a discrete two-stage hybrid framework: an interpretable 3-state Gaussian HMM segments market regimes from daily volatility innovations ($\Delta\text{VIX}$), and a tabular reinforcement learning agent via Bellman policy iteration learns an optimal mapping from latent regimes to asset weights across equities, long-term bonds, and gold—empirically demonstrating that gold dominates Treasuries as a safe-haven hedge in high-volatility regimes and Treasuries receive zero weight under recent inflation-correlated regimes.

## Economic mechanism

### Source-reported

1. **Time-Varying Regimes and Structural Breaks:** Financial markets exhibit non-stationary return and risk dynamics driven by shifting investor risk appetite, volatility clustering, and macroeconomic disruptions. Static asset allocation frameworks (such as equal weight or fixed 60/40) fail to adapt when cross-asset correlations tighten or invert during market stress.
2. **State-Conditional Payoff Asymmetries:**
   - In low-volatility regimes (State 0), equities (SPY) exhibit the highest expected returns ($+0.1295\%$ daily) and lowest return dispersion ($0.005511$), providing an optimal environment for full equity exposure.
   - In transitional regimes (State 1), equities remain mildly positive ($+0.0014\%$ daily) while gold ($+0.0335\%$) and bonds ($+0.0228\%$) offer moderate stability, rewarding sustained equity risk-taking.
   - In high-volatility crisis regimes (State 2), equity returns become sharply negative ($-0.4749\%$ daily) with heightened variance ($0.033809$), while safe-haven assets (GLD at $+0.0476\%$ and TLT at $+0.1673\%$) provide positive expected returns.
3. **Decoupling of Treasury Hedging Efficacy:** Classical portfolio theory relies heavily on long-term Treasuries (TLT) to offset equity drawdowns. However, during inflationary stress periods (such as 2022), positive stock-bond correlations reduce Treasury hedging effectiveness (Baele et al., 2023). In contrast, gold (GLD) demonstrates more consistent safe-haven properties across equity crises (Baur & Lucey, 2010; Zaremba & Idzorek, 2023).
4. **Reinforcement Learning vs. Heuristic Rotation:** Purely heuristic rules (e.g. 100% allocation to the highest state-conditional mean asset) suffer from turnover friction and whipsaw drawdowns at regime boundaries. An RL policy using Bellman optimality explicitly internalizes state transition probabilities $P(s, s')$ and future expected values, producing a stable, robust policy that protects against adverse transitions.

### Research interpretation

The overarching mechanism is **dynamic downside tail truncation and safe-haven substitution guided by volatility innovations**:
1. **Latent State Filtering from Volatility Shocks ($\Delta\text{VIX}$):** By modeling changes in implied volatility ($\Delta\text{VIX}$) via a Gaussian HMM rather than trailing realized price volatility, the framework detects shifts in market fear and pricing uncertainty with minimal filter lag, avoiding the delay inherent in rolling lookback windows.
2. **Endogenous Elimination of Duration Risk (Zero TLT Allocation):** When the tabular Bellman operator evaluates expected returns over the full sample including recent inflationary rate shocks, long-term Treasuries yield negative risk-adjusted utility in low-volatility regimes and inferior stability relative to gold in high-volatility regimes. Consequently, the optimal RL policy $\pi^*$ endogenously assigns 0% weight to TLT across all states, pruning duration risk entirely.
3. **Asymmetric Equity Downside Truncation:** By executing an immediate 100% rotation into physical gold (GLD) upon transitioning into State 2, the strategy sidesteps the heavy left-tail drawdowns of equities ($-0.475\%$ mean daily return in crisis states) while remaining 100% invested in equities during calm and transitional growth states.

## Signal

The strategy operates as a discrete daily tactical asset allocation system across SPY, TLT, and GLD:

### Signal Formation Timestamp
- **Observation Frequency:** Daily.
- **Signal Formation:** End of trading day $t$, evaluated at the market close (16:00 ET).
- **Execution Timing:** Executed for returns over trading day $t+1$ (modeled with a strict 1-day execution lag: the action selected at time $t$ based on predicted regime $S_t$ applies to returns realized at $t+1$).
- **Calendar & Timezone:** US Eastern Time (UTC-5 / UTC-4 EDT); New York Stock Exchange and CBOE market calendar.

### Regime Identification via Gaussian HMM
1. **Input Feature:** Daily change in CBOE Volatility Index:
   $$\Delta\text{VIX}_t = \text{VIX}_t - \text{VIX}_{t-1}$$
2. **Model Formulation:** A 3-state continuous-emission Gaussian Hidden Markov Model:
   $$y_t = \Delta\text{VIX}_t \mid (S_t = i) \sim \mathcal{N}(\mu_i, \sigma_i^2), \quad i \in \{0, 1, 2\}$$
3. **Estimation Protocol:** Expectation-Maximization (EM / Baum-Welch) algorithm on the 70% in-sample training window.
4. **Filtering Recursion (Hamilton Forward Filter):**
   $$\xi_{t|t}(i) = \frac{\xi_{t|t-1}(i) f(y_t \mid S_t = i)}{\sum_{j=0}^2 \xi_{t|t-1}(j) f(y_t \mid S_t = j)}$$
5. **Model Selection Criteria (Table 1):**
   - 2-state HMM: $\log L = -8,975, k = 7, \text{AIC} = 17,964, \text{BIC} = 18,010$
   - 3-state HMM: $\log L = -8,632, k = 14, \text{AIC} = 17,293, \text{BIC} = 17,385$
   - Selected: 3-state HMM based on lower AIC and BIC and clear economic separation between calm, transitional, and crisis states.
6. **In-Sample Estimated Parameters (Table 2 & 2b):**
   - **State 0 (Low Volatility / Bullish Expansion):** $\mu_0 = -0.0606$, $\sigma_0 = 0.6076$ (active 50.83% of time).
   - **State 1 (Transitional / Moderate Volatility):** $\mu_1 = -0.0146$, $\sigma_1 = 1.7132$ (active 42.98% of time).
   - **State 2 (High Volatility / Crisis Stress):** $\mu_2 = 0.6120$, $\sigma_2 = 5.9255$ (active 6.18% of time).
   - **Transition Probability Matrix $P$:**
     $$P = \begin{pmatrix} 0.9386 & 0.0614 & 0.0000 \\ 0.0726 & 0.9093 & 0.0181 \\ 0.0001 & 0.1260 & 0.8740 \end{pmatrix}$$

### State-Conditional Asset Payoffs (Table 3)
- **State 0 (50.83% of time):**
  - SPY: Mean daily log-return $= +0.001295$ ($+0.1295\%$), Daily Std Dev $= 0.005511$
  - GLD: Mean daily log-return $= +0.000458$ ($+0.0458\%$), Daily Std Dev $= 0.009375$
  - TLT: Mean daily log-return $= -0.000119$ ($-0.0119\%$), Daily Std Dev $= 0.007456$
- **State 1 (42.98% of time):**
  - SPY: Mean daily log-return $= +0.000014$ ($+0.0014\%$), Daily Std Dev $= 0.012092$
  - GLD: Mean daily log-return $= +0.000335$ ($+0.0335\%$), Daily Std Dev $= 0.011445$
  - TLT: Mean daily log-return $= +0.000228$ ($+0.0228\%$), Daily Std Dev $= 0.009656$
- **State 2 (6.18% of time):**
  - SPY: Mean daily log-return $= -0.004749$ ($-0.4749\%$), Daily Std Dev $= 0.033809$
  - GLD: Mean daily log-return $= +0.000476$ ($+0.0476\%$), Daily Std Dev $= 0.020023$
  - TLT: Mean daily log-return $= +0.001673$ ($+0.1673\%$), Daily Std Dev $= 0.017325$

### Tabular Reinforcement Learning Policy Iteration
- **State Space:** $\mathcal{S} = \{0, 1, 2\}$ representing the current HMM-predicted regime.
- **Action Space:** $\mathcal{A}$ comprises seven discrete portfolio weight combinations $(w_{\text{TLT}}, w_{\text{GLD}}, w_{\text{SPY}})$ satisfying $\sum w_i = 1$ and $w_i \ge 0$.
- **Objective Function:** Bellman optimality equation for state-action values:
  $$Q(s, a) = R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s, s') V(s')$$
  where $R(s, a) = \sum_i w_i(a) \cdot \mathbb{E}[r_i \mid s]$ is the expected return of the portfolio in regime $s$, $P(s, s')$ is the HMM transition matrix, and $\gamma$ is the discount factor.
- **Learned Optimal Policy $\pi^*$ (Table 5):**
  - **State 0:** Action ID 3 -> Weights $(w_{\text{TLT}}=0.0, w_{\text{GLD}}=0.0, w_{\text{SPY}}=1.00)$ — 100% Equities (persistent low-volatility expansion).
  - **State 1:** Action ID 3 -> Weights $(w_{\text{TLT}}=0.0, w_{\text{GLD}}=0.0, w_{\text{SPY}}=1.00)$ — 100% Equities (moderate regime with continuing momentum).
  - **State 2:** Action ID 2 -> Weights $(w_{\text{TLT}}=0.0, w_{\text{GLD}}=1.00, w_{\text{SPY}}=0.0)$ — 100% Gold (high-volatility regime safe-haven).

### Rule-Based Rotation Benchmarks (Table 4)
- **Top-1 Rotation:**
  - State 0: 100% SPY
  - State 1: 100% GLD
  - State 2: 100% TLT
- **60/40 Rotation:**
  - State 0: 60% SPY, 40% GLD
  - State 1: 60% GLD, 40% TLT
  - State 2: 60% TLT, 40% GLD

### Underspecified Rules
- The exact numeric value of the discount factor $\gamma$ in the Bellman equation is omitted in the paper text.
- The full list of all seven candidate actions in $\mathcal{A}$ is not fully enumerated; only Action 2 $(0, 1, 0)$ and Action 3 $(0, 0, 1)$ are detailed in Table 5.
- The precise calendar date dividing the 70% in-sample and 30% out-of-sample periods is not stated explicitly (corresponds approximately to mid-2018 based on the 2004–2025 range).

## Required data

- **Instruments:**
  - SPY (SPDR S&P 500 ETF Trust, NYSE Arca)
  - TLT (iShares 20+ Year Treasury Bond ETF, NASDAQ)
  - GLD (SPDR Gold Shares, NYSE Arca)
  - ^VIX (CBOE Volatility Index)
- **Universe & Survivorship:** Fixed 4-ticker universe. SPY, TLT, and GLD are among the most liquid ETFs globally with inception dates prior to or during 2004 (SPY 1993, TLT 2002, GLD Nov 2004). No survivorship bias across the 2004–2025 window.
- **Timeframe & Sampling:** Daily closing prices ($P_t$).
- **Fields:** Daily split- and dividend-adjusted close prices for ETF return calculations; daily closing index level for VIX.
- **Point-in-Time & Lagging:** Strict 1-day execution lag. Regime is predicted at time $t$ using close-to-close data available at $t$; trades are executed for realization over day $t+1$. No look-ahead leakage.
- **Missing Data Handling:** Sessions where any instrument is missing (e.g. partial holiday closures) are inner-joined across common trading dates.

## Execution assumptions

- **Order Execution:** Daily close-to-close or open-to-open holding with 1-day execution lag.
- **Fill Model:** Full fill assumed at recorded daily prices. Deep secondary market liquidity in SPY, TLT, and GLD (each trading tens to hundreds of millions in daily turnover) permits execution at negligible bid-ask spreads for standard portfolio sizes.
- **Transaction Costs:** Explicitly assumed zero ($0.0$ bps commissions and $0.0$ bps slippage) in the primary baseline study.
- **Leverage & Shorting:** Long-only ($w_i \ge 0, \sum w_i = 1$). No leverage or short borrow required.

## Evidence

### Source-reported

All performance statistics below are directly reported by Ajay Kumar Verma, Nunik Srikandi Putri, and Neo Paul Lesupi (arXiv:2605.27848v1, May 2026):

#### 1. Full Sample Performance (2004–2025, Daily, Table 6):
- **Top-1 Rotation:** Cumulative Return 407.8%, Annualized Return 8.1%, Volatility 15.4%, Sharpe Ratio 0.52, Max Drawdown -28.3%
- **60/40 Rotation:** Cumulative Return 317.0%, Annualized Return 7.1%, Volatility 12.1%, Sharpe Ratio 0.58, Max Drawdown -29.3%
- **Equal-Weight (Monthly):** Cumulative Return 376.1%, Annualized Return 7.7%, Volatility 9.7%, Sharpe Ratio 0.80, Max Drawdown -24.0%
- **Buy & Hold SPY:** Cumulative Return 476.3%, Annualized Return 8.7%, Volatility 19.1%, Sharpe Ratio 0.46, Max Drawdown -59.6%

#### 2. 30% Out-of-Sample Test Window Performance (Table 7):
- **RL Policy $\pi^*$ (net):** Cumulative Return 131.4%, Annualized Return 14.3%, Volatility 17.3%, Sharpe Ratio 0.83, Max Drawdown -23.5%
- **Top-1 Rotation:** Cumulative Return 110.4%, Annualized Return 12.6%, Volatility 16.0%, Sharpe Ratio 0.79, Max Drawdown -21.8%
- **60/40 Rotation:** Cumulative Return 86.9%, Annualized Return 10.5%, Volatility 12.8%, Sharpe Ratio 0.82, Max Drawdown -29.3%
- **Equal-Weight (Monthly):** Cumulative Return 72.5%, Annualized Return 9.1%, Volatility 11.0%, Sharpe Ratio 0.83, Max Drawdown -24.0%
- **Buy & Hold SPY:** Cumulative Return 118.4%, Annualized Return 13.2%, Volatility 20.5%, Sharpe Ratio 0.65, Max Drawdown -35.7%

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Zero Transaction Cost Bias:** The primary backtest models zero transaction costs and zero bid-ask spread impact. Because the strategy switches 100% of portfolio capital between SPY and GLD upon regime shifts, high turnover around choppy regime boundaries will degrade realized Sharpe and return.
2. **Failure of Treasury Hedging:** TLT produced negative average daily returns in State 0 ($-0.0119\%$) and failed to protect equities during the 2022 inflationary drawdown, forcing the RL model to assign 0% allocation to bonds across all states.
3. **Gaussian Emission Misspecification:** Gaussian HMM emissions do not account for empirical financial return stylized facts, including fat tails, skewness, and volatility jumps (Cont, 2001). Under extreme sudden shocks, the Gaussian assumption may delay regime transition identification.

## Falsification plan

1. **Transaction Cost Sensitivity Stress:** Apply realistic turnover penalties of 2 bps, 5 bps, 10 bps, and 20 bps per half-turn. If transaction costs reduce the out-of-sample Sharpe ratio of RL $\pi^*$ below the buy-and-hold SPY benchmark (0.65) or Equal-Weight (0.83), the economic viability of discrete regime switching is falsified.
2. **Static Threshold Ablation:** Replace the Gaussian HMM with simple static VIX level rules (e.g., if VIX > 25 then GLD else SPY) or trailing 20-day VIX moving-average crossovers. If static heuristics achieve comparable Sharpe ratios and drawdowns without the HMM/RL dynamic programming machinery, the HMM component fails the test of incremental explanatory power.
3. **Subperiod & Crisis Disaggregation:** Partition the 30% out-of-sample test window into distinct market phases: pre-2020 expansion, Q1 2020 COVID shock, 2022 rate-hiking cycle, and 2023–2025 AI expansion. Test whether the RL policy achieved drawdown reduction across multiple independent crises or if performance was driven by a single isolated event.
4. **Non-Gaussian Robustness (Student-t HMM):** Re-fit the HMM using Student-t emission distributions to accommodate heavy tails. If the estimated state transition matrix or policy mapping alters materially and degrades out-of-sample performance, the model is fragile to distribution specification.

## Crypto portability

Portability status: `adapted / unproven`.

- **Conceptual Portability:** The thesis of regime-dependent tactical asset allocation and safe-haven rotation is portable to digital assets, but cannot be applied directly:
  - **Equity Proxy:** Bitcoin (BTC) or Ethereum (ETH) acts as the primary risk/growth asset (analogous to SPY).
  - **Volatility Feature:** CBOE VIX has no direct single exchange equivalent; crypto implementations must use Deribit Bitcoin Volatility Index (DVOL) or high-frequency realized volatility innovations ($\Delta\text{RV}_{24\text{h}}$).
  - **Safe-Haven Proxy:** Gold (GLD) can be substituted with tokenized gold (PAXG/XAUT) or interest-bearing USD stablecoins (USDT/USDC). Long-term Treasuries (TLT) have no native on-chain equivalent outside tokenized US Treasury products (e.g. Ondo USDY, BlackRock BUIDL).
- **Crypto-Specific Frictions:**
  - **24/7 Market Structure:** Crypto trades continuously without market closes. HMM filtering must be adapted to rolling 8-hour or 24-hour windows.
  - **Jump Severity & Speed:** Cryptocurrency market crashes often materialize within minutes to hours rather than days. A daily-frequency HMM with a 1-day execution lag risks severe slippage and drawdown before the regime switch executes.
  - **Stablecoin Counterparty Risk:** Cash and safe-haven assets in crypto introduce smart contract, collateral, and depegging risks not present in physical GLD or cash Treasuries.

## Limitations

- **Frictionless Backtest:** Zero transaction costs, commissions, or slippage are modeled in the reported empirical backtest.
- **Discrete Coarse Action Space:** The tabular reinforcement learning algorithm evaluates only 7 discrete portfolio weight triples rather than a continuous weight simplex.
- **Sample Regime Specificity:** The evaluation spans a prolonged US bull market interrupted by few crisis episodes, during which gold maintained strong demand; regimes where both equities and gold decline simultaneously (liquidity crunches) pose unhedged downside risk.
- **Underspecified Hyperparameters:** The exact numerical discount factor $\gamma$ in the Bellman equation is not reported in the source text.

## Implementation status

Not implemented. No prototype, backtest, or live code exists in NautilusTrader, PyBroker, or any other execution stack.

## Adoption boundary

Research-only. Not approved for implementation, paper trading, testnet, or live trading.

## Related Wiki records

- `[[quant/continuous-macro-timing-growth-defensive-style-allocation-2026-09-02]]` — Continuous macro timing on Growth vs Defensive sleeves using economic indicators (arXiv:2605.20636).
- `[[quant/continuous-cash-overlay-growth-defensive-slow-tail-vshape-max-cash-2026-09-03]]` — Defensive cash overlay combining slow-tail risk and fast crash brakes (arXiv:2606.09025).
- `[[quant/deep-portfolio-optimization-attention-lstm-omega-cvar-risk-parity-2026-09-03]]` — Deep neural network optimizing differentiable financial risk surrogates (arXiv:2605.28853).
- `[[quant/regime-adaptive-continual-learning-portfolio-management-recap-2026-09-02]]` — Continual learning portfolio adaptation comparing CUSUM and HMM regime detection (arXiv:2606.00143).
- `[[quant/dynamic-portfolio-optimization-cvar-stochastic-control-hjb-2026-09-02]]` — Continuous-time dynamic portfolio optimization under CVaR constraints via HJB equations (arXiv:2608.20179).

## Sources

- Ajay Kumar Verma, Nunik Srikandi Putri, and Neo Paul Lesupi, *"Regime-Based Portfolio Allocation Using Hidden Markov Models and Reinforcement Learning"*, arXiv preprint `arXiv:2605.27848v1 [q-fin.PM, q-fin.ST]`, submitted May 27, 2026. DOI: `10.48550/arXiv.2605.27848`.
  - Stable Abstract URL: `https://arxiv.org/abs/2605.27848`
  - Direct PDF URL: `https://arxiv.org/pdf/2605.27848`
  - Primary Tables Audited:
    - Table 1: HMM Model Selection: Log-Likelihood, AIC, and BIC (2 states vs 3 states).
    - Table 2: State-Dependent Parameters for 3-State HMM ($\mu_i, \sigma_i$).
    - Table 2(b): Transition Matrix $P$ for 3-State HMM.
    - Table 3: State-Conditional Mean and Standard Deviation of ETF Returns (SPY, TLT, GLD).
    - Table 4: State-Allocation Mapping for Rule-Based Top-1 and 60/40 Rotation.
    - Table 5: RL Optimal Policy $\pi^*$ (Training Sample).
    - Table 6: Performance Summary (Full Sample, 2004–2025).
    - Table 7: Performance Comparison — RL vs. Rotation Benchmarks (30% Out-of-Sample Test Window).\n