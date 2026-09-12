---
schema: strategy-research-record-v1
title: "Market-Regime Routed Specialist GBTs with Regime-Asymmetric Dual-Threshold Hysteresis and Volatility Targeting"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equity-timing
  - regime-switching
  - random-forest
  - gradient-boosted-trees
  - hysteresis
  - volatility-targeting
  - drawdown-protection
status: research-only
confidence: high
source_as_of: 2026-09-12
sources:
  - "https://github.com/davidxu277/alpha-timing"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Market-Regime Routed Specialist GBTs with Regime-Asymmetric Dual-Threshold Hysteresis and Volatility Targeting

## Provenance

- **Primary Source:** Shuyao Xu (Department of Industrial Systems Engineering and Management / School of Computing, National University of Singapore, NUS; `davidxu277`).
- **Primary Repository:** Public GitHub repository `https://github.com/davidxu277/alpha-timing`
- **Immutable Commit SHA:** `299db752becd7023d2b5360f1c6e238572d60e3e` (Committed September 12, 2026 UTC, `source-reported`).
- **Exact Code Paths:**
  - [`regime_trading.py`](https://github.com/davidxu277/alpha-timing/blob/299db752becd7023d2b5360f1c6e238572d60e3e/regime_trading.py): Full pipeline containing feature engineering, nowcaster training, 4 specialist GBT regressions, Calmar-based threshold grid search, ablation suite, and SPY out-of-universe transfer backtest.
  - [`build_models.py`](https://github.com/davidxu277/alpha-timing/blob/299db752becd7023d2b5360f1c6e238572d60e3e/build_models.py): Model training and serialisation script for the nowcaster and 4 specialist regressors.
  - [`docs/update_signals.py`](https://github.com/davidxu277/alpha-timing/blob/299db752becd7023d2b5360f1c6e238572d60e3e/docs/update_signals.py): Daily production inference pipeline for SPY, QQQ, AAPL, NVDA, MSFT, and GOOGL.
  - [`docs/data/track_record.jsonl`](https://github.com/davidxu277/alpha-timing/blob/299db752becd7023d2b5360f1c6e238572d60e3e/docs/data/track_record.jsonl): Public append-only hash-chained ledger logging daily out-of-sample paper trading recommendations and NAV.
  - [`README.md`](https://github.com/davidxu277/alpha-timing/blob/299db752becd7023d2b5360f1c6e238572d60e3e/README.md): System documentation, theoretical premise, empirical ablation metrics, and transfer backtest tables.
- **Repository Deduplication Audit:** A thorough audit of all existing `.md` files in `alpha-strategy-research` confirmed zero matching records for `davidxu277/alpha-timing`, Shuyao Xu, or this implementation. Related regime-based captures in the repository (`regime-switching-hmm-reinforcement-learning-etf-allocation-2026-09-04.md`, `two-level-uncertainty-cross-sectional-ranker-regime-trust-gate-tail-cap-2026-09-05.md`, `simple-dynamic-stock-bond-gold-markowitz-volatility-control-2026-09-11.md`, `staged-short-term-drawdown-reversal-ml-timing-overlay-2026-09-12.md`) investigate Markov-regime RL allocation, trust-gated cross-sectional ranking, static multi-asset volatility targeting, or ML draw-down reversal overlays; none formulate a supervisory decoupled architecture routing daily feature vectors to specialist GBT models trained exclusively on regime-conditional subsets, nor do they employ Calmar-optimized regime-asymmetric dual-threshold hysteresis.

## Economic mechanism

### Source-reported

1. **Behavioral Stationarity of Market Regimes:**
   The strategy operationalizes the foundational premise of technical and behavioral finance that human fear and greed generate recurring, identifiable market macro-states (Bull, Bear, Sideways, Crisis). Rather than forecasting regime transitions into the future, the system formulates a **nowcasting** classification problem: identifying the current latent state of the market on day $t$ using trailing technical indicators and macroeconomic series (`source-reported`).
2. **Specialist Inductive Bias Under Low Signal-to-Noise Ratios:**
   In financial return prediction, true directional edge typically accounts for only ~2% of daily return variance (median absolute factor Information Coefficients |IC| ≈ 0.02–0.06). When a single pooled machine learning model is trained across all historical data, contradictory behavioral patterns cancel each other out: for example, a sharp price decline represents a dip-buying opportunity in a secular bull market, but a catastrophic falling knife in a liquidity crisis. By segregating the training sample into regime-specific subsets, four specialist gradient-boosted decision tree (`HistGradientBoostingRegressor`) models learn regime-congruent conditional return distributions without polluting each other parameter spaces (`source-reported`).
3. **Regime-Asymmetric Dual-Threshold Hysteresis:**
   Continuous directional return forecasts exhibit high-frequency daily noise. Converting raw predictions into binary or continuous positions using a single zero-crossing threshold triggers severe turnover and transaction cost attrition. The system implements a dual-threshold hysteresis band $(\tau_{\text{in}}, \tau_{\text{out}})$ where positions are entered only upon crossing an upper threshold and exited only when dropping below a lower threshold. Crucially, validation grid search establishes an economically intuitive asymmetry:
   - *Risk-on Regimes (Bull / Sideways):* "Easy in, hard out" ($\tau_{\text{in}} = +0.1\%, \tau_{\text{out}} = -0.3\%$) to maintain market exposure during positive drift.
   - *Risk-off Regimes (Bear / Crisis):* "Hard in, fast out" ($\tau_{\text{in}} = +0.3\%, \tau_{\text{out}} = 0.0\%$) to demand high conviction before entering and exit immediately upon signal degradation (`source-reported`).
4. **Thermostatic Volatility Targeting:**
   Independent of directional return forecasts, position sizing is modulated by a continuous volatility thermostat:
   $$\text{position} = \min\left(1.0, \frac{25\%}{\sigma_{\text{ann}}}\right)$$
   where $\sigma_{\text{ann}}$ is the annualized 20-day rolling return volatility. As market uncertainty and volatility escalate during turbulent regimes, dollar exposure mechanically scales down, pre-emptively curtailing portfolio risk before directional models trigger an outright exit (`source-reported`).

### Research interpretation

- **Drawdown Avoidance as Geometric Compounding Driver:**
   Long-term equity returns are geometrically constrained by severe left-tail drawdowns. A 50% decline requires a 100% recovery to break even. By successfully rotating into cash during major bear market regimes (such as the 2022 market decline, where the system posted -1.6% vs -19.0% for buy-and-hold), the strategy generates superior risk-adjusted alpha over full market cycles, even if it incurs modest tracking error or cash-drag during runaway bull markets.
- **De-aliasing Supervision Targets:**
   A critical design strength is the decoupling of the supervision targets: the nowcaster is trained on categorical regime labels, whereas the specialists are trained on forward excess returns. This prevents the classifier from collapsing into an unstable return predictor, anchoring it instead to structural macroeconomic and volatility regimes.

## Signal

The trading logic is completely specified in the primary source (`regime_trading.py`):

### 1. Data Ingestion and Feature Engineering

At the close of each trading day $t$, two distinct feature matrices are constructed using strictly trailing data:

#### A. 12 Volatility-Normalized Specialist Factors ($\mathbf{f}_t \in \mathbb{R}^{12}$)
Calculated on daily adjusted closing prices $C$:
1. Realized volatility: $\sigma_{20, t} = \text{std}_{20}(r_\tau)$, $\sigma_{60, t} = \text{std}_{60}(r_\tau)$, where $r_\tau = C_\tau / C_{\tau-1} - 1$.
2. Volatility-scaled momentum:
   $$\text{mom}_{k, t} = \frac{C_t / C_{t-k} - 1}{\sigma_{20, t} \sqrt{k}} \quad \text{for } k \in \{5, 20, 60, 120\}$$
3. Moving average deviations (Z-scores):
   $$\text{ma}_{20\_z, t} = \frac{C_t / \text{SMA}_{20}(C)_t - 1}{\sigma_{20, t}}$$
   $$\text{ma}_{60\_z, t} = \frac{C_t / \text{SMA}_{60}(C)_t - 1}{\sigma_{20, t} \sqrt{3}}$$
   $$\text{ma}_{200\_z, t} = \frac{C_t / \text{SMA}_{200}(C)_t - 1}{\sigma_{20, t} \sqrt{10}}$$
4. Volatility dynamics:
   $$\text{vol}_{20, t} = \sigma_{20, t}, \qquad \text{vol\_ratio}_t = \frac{\sigma_{20, t}}{\sigma_{60, t}}$$
5. Drawdown from 60-day peak:
   $$\text{dd}_{60, t} = \frac{C_t / \max_{\tau \in [t-59, t]}(C_\tau) - 1}{\sigma_{20, t} \sqrt{20}}$$
6. 20-day Stochastic Oscillator:
   $$\text{stoch}_{20, t} = \frac{C_t - \min_{\tau \in [t-19, t]}(C_\tau)}{\max_{\tau \in [t-19, t]}(C_\tau) - \min_{\tau \in [t-19, t]}(C_\tau)}$$
7. Normalized 14-day RSI:
   $$\text{RSI}_{14, t} = \frac{1}{50} \left( 100 - \frac{100}{1 + \text{RS}_{14, t}} - 50 \right) \in [-1, 1]$$
   where $\text{RS}_{14, t} = \text{SMA}_{14}(\max(\Delta C, 0)) / \text{SMA}_{14}(\max(-\Delta C, 0))$.

#### B. 16 Regime Nowcaster Features ($\mathbf{x}_t \in \mathbb{R}^{16}$)
1. Trailing returns: $\text{ret}_1, \text{ret}_5, \text{ret}_{20}, \text{ret}_{60}$.
2. Price-to-moving-average ratios: $C / \text{SMA}_k(C) - 1$ for $k \in \{20, 60, 200\}$.
3. Volatility measures: $\sigma_{20}, \sigma_{60}$.
4. Price-to-high ratios: $C / \max_k(C) - 1$ for $k \in \{20, 60\}$.
5. Normalized stochastic: $\text{stoch}_{20}$.
6. Macroeconomic features (point-in-time daily observations):
   - `vix`: CBOE Volatility Index.
   - `fed_funds_rate`: Federal funds effective rate (%).
   - `unemployment_rate`: US civilian unemployment rate (%).
   - `yield_spread`: US 10-Year Treasury Yield minus 2-Year Treasury Yield ($10\text{y} - 2\text{y}$).

### 2. Model Inference Pipeline

1. **Regime Nowcast:**
   $$\widehat{R}_t = \text{Classifier}(\mathbf{x}_t) \in \{\text{Bull}, \text{Bear}, \text{Sideways}, \text{Crisis}\}$$
   implemented via `RandomForestClassifier(n_estimators=300, min_samples_leaf=50, class_weight="balanced", random_state=7)` (`source-reported`).
2. **Feature Standardization:**
   $$\widetilde{\mathbf{f}}_t = \text{StandardScaler}(\mathbf{f}_t)$$
   using parameters fit strictly on the pre-2013 training split (`source-reported`).
3. **Specialist Return Prediction:**
   Evaluate the specialist corresponding to $\widehat{R}_t$:
   $$\widehat{y}_t = \text{Specialist}_{\widehat{R}_t}(\widetilde{\mathbf{f}}_t)$$
   where each specialist is a `HistGradientBoostingRegressor(max_depth=3, learning_rate=0.05, max_iter=300, random_state=7)` predicting the 5-day excess return target:
   $$y_{\text{fwd}, t} = \frac{C_{t+5} - C_t}{C_t} - 5 \cdot r_{f, d, t}$$
   with $r_{f, d, t} = (1 + \text{fed\_funds\_rate}_t / 100)^{1/252} - 1$ (`source-reported`).

### 3. Decision Layer & Position Sizing

1. **Regime Grouping:**
   $$\text{RiskOff}_t = \mathbb{I}\{\widehat{R}_t \in \{\text{Bear}, \text{Crisis}\}\}$$
2. **Threshold Assignment:**
   $$(\tau_{\text{in}, t}, \tau_{\text{out}, t}) = \begin{cases} (+0.3\%, 0.0\%) & \text{if } \text{RiskOff}_t = 1 \\ (+0.1\%, -0.3\%) & \text{if } \text{RiskOff}_t = 0 \end{cases}$$
   *(Selected via grid search maximizing Calmar ratio over the 2013–2018 validation period, `source-reported`).*
3. **Hysteresis State Machine:**
   Let $p_{t-1} \in \{0.0, 1.0\}$ be yesterday binary regime position:
   $$p_t = \begin{cases} 1.0 & \text{if } p_{t-1} = 0.0 \text{ and } \widehat{y}_t > \tau_{\text{in}, t} \\ 0.0 & \text{if } p_{t-1} = 1.0 \text{ and } \widehat{y}_t < \tau_{\text{out}, t} \\ p_{t-1} & \text{otherwise} \end{cases}$$
4. **Volatility Target Overlay:**
   Calculate daily target volatility scaling:
   $$\sigma_{\text{target}, d} = \frac{0.25}{\sqrt{252}} \approx 0.015749$$
   $$\text{volscale}_t = \text{clip}\left(\frac{\sigma_{\text{target}, d}}{\max(\sigma_{20, t}, 10^{-6})}, 0.0, 1.0\right)$$
5. **Final Net Position:**
   $$\text{Exposure}_t = p_t \cdot \text{volscale}_t \in [0.0, 1.0]$$
   *(Long-only, capped at 100% gross exposure; no leverage permitted, `source-reported`).*

## Required data

- **Asset Universe:** Tested primarily on SPY (S&P 500 ETF, dividends included). The underlying model stack was trained across a 35-stock US equity universe (excluding index tickers) and evaluated on 6 core liquid symbols (SPY, QQQ, AAPL, NVDA, MSFT, GOOGL) (`source-reported`).
- **Data Frequency:** Daily bar closes ($t$).
- **Pricing Fields:** Adjusted daily `open`, `high`, `low`, `close`, `volume` (`source-reported`).
- **Macroeconomic Series:**
  - VIX Index (`^VIX`)
  - Effective Federal Funds Rate (FRED: `FEDFUNDS`)
  - Civilian Unemployment Rate (FRED: `UNRATE`)
  - 10-Year Treasury Constant Maturity Yield (FRED: `DGS10`)
  - 2-Year Treasury Constant Maturity Yield (FRED: `DGS2`)
- **Point-in-Time Availability:** All technical features are computed trailing at bar close $t$. Macroeconomic indicators are synchronized on day $t$. In historical data, monthly series (unemployment) carry their latest publicly known value forward without look-ahead (`source-reported`).
- **Warm-Up Window:** Minimum 200 trading days for the longest technical indicator (`ma200_z`), with a recommended 320 trading days to initialize path-dependent hysteresis (`source-reported`).

## Execution assumptions

- **Execution Timing:** Positions determined at the close of day $t$ earn the return from close $t$ to close $t+1$ (`source-reported`).
- **Trading Costs:** 5 basis points ($0.05\%$) deducted on the absolute difference of position changes:
  $$\text{Cost}_t = 0.0005 \times |\text{Exposure}_t - \text{Exposure}_{t-1}|$$
- **Cash Return:** Idle portfolio cash ($1.0 - \text{Exposure}_t$) earns interest daily:
  - In training/validation: Effective Federal Funds rate ($r_{f, d, t}$).
  - In SPY test: Fixed $4.0\%$ per annum ($1.04^{1/252} - 1$) (`source-reported`).
- **Shorting / Borrow:** None. The strategy is strictly long-or-cash ($\text{Exposure} \in [0, 1]$) (`source-reported`).
- **Fill Model:** Frictionless execution at the published adjusted close price net of the fixed 5 bps turnover fee (`source-reported`).
- **Source Gap:** The primary codebase does not incorporate execution latency models, bid-ask spread expansion during volatility crises, or market impact functions for institutional order sizes (`source-gap`).

## Evidence

### Source-reported

All quantitative figures below trace directly to the audited source code, tables, and serialized logs of `davidxu277/alpha-timing` (commit `299db752becd7023d2b5360f1c6e238572d60e3e`):

1. **Out-of-Universe SPY Transfer Test (Nov 2021 to 2026):**
   Evaluated on the final 20% chronological holdout of SPY daily data (Nov 2021 through 2026), incorporating 5 bps transaction costs and 4% cash interest on unallocated capital. **Zero parameters were fit or tuned on SPY data** (models fit on 35-stock training universe pre-2013; thresholds selected on 2013–2018 validation set):

| Strategy | Total Return | Sharpe Ratio | Max Drawdown | Annual Volatility | Time in Market |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Alpha Timing (System)** | **+83.8%** | **1.05** | **-13.9%** | **14.7%** | **79%** |
| Buy & Hold (SPY) | +56.5% | 0.69 | -24.5% | 17.8% | 100% |
| Benchmark MA20>60 | +28.7% | 0.59 | -17.2% | 11.2% | 65% |

2. **Yearly Return Attribution (System vs. SPY Buy & Hold):**
   Demonstrates that the strategy alpha is generated by capital preservation during severe downturns rather than aggressive upside capture:
   - **2022 (Bear Market):** System **-1.6%** vs. Buy & Hold **-19.0%** (Excess: **+17.4 percentage points**).
   - **2023 (Bull Market):** System **+21.7%** vs. Buy & Hold **+26.0%** (Excess: **-4.3 percentage points**).
   - **2024 (Bull Market):** System **+30.1%** vs. Buy & Hold **+25.3%** (Excess: **+4.8 percentage points**).
   - **2025 (Bull Market):** System **+14.0%** vs. Buy & Hold **+18.2%** (Excess: **-4.2 percentage points**).

3. **Ablation Study on Model Routing & Asymmetric Hysteresis:**
   A systematic ablation experiment (`regime_trading.py --ablation`) verifies whether the regime nowcaster and routing mechanism provide genuine incremental value over pooled baselines:

| Architecture Variant | Total Return | Sharpe Ratio | Max Drawdown | Time in Market | Role of Classifier |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **A · Full System (4 specialists + regime thresholds)** | **+83.8%** | **1.05** | **-13.9%** | **79%** | Fully utilized |
| **C · Single Pooled GBT + Regime Thresholds** | +55.4% | 0.78 | -15.4% | 76% | Only sets defensive thresholds |
| **B · Single Pooled GBT + Single Symmetric Threshold** | +52.6% | 0.80 | -15.7% | 78% | Classifier removed entirely |
| **Buy & Hold (Baseline)** | +56.5% | 0.69 | -24.5% | 100% | — |

   *Source Finding:* Removing specialist routing collapses the Sharpe ratio from **1.05 to ~0.78–0.80**, demonstrating that regime specialization accounts for over 25% of the total risk-adjusted edge.

4. **Nowcaster Classification Accuracy:**
   The balanced Random Forest nowcaster achieves approximately **88% out-of-sample accuracy** in identifying the four canonical market regimes across the multi-stock testing split.

### Independently reproduced

`not independently reproduced`. All metrics and empirical ablation results cited above represent third-party reported findings from Shuyao Xu (`davidxu277/alpha-timing`).

### Negative evidence

- **Bull Market Tracking Drag:** During strong trending bull market years (e.g. 2023 and 2025), the strategy underperforms pure buy-and-hold by 4.2 to 4.3 percentage points due to periodic cash stepping and volatility-targeting constraints.
- **Failure of Direct Deep Reinforcement Learning:** The author reported that an initial per-regime Deep Q-Network (DQN) implementation was abandoned during development because high policy variance and non-stationary reward surfaces prevented reliable out-of-sample convergence (`source-reported`).
- **Fragility of Single Pooled Models:** Training a single un-routed regression model fails to capture regime-dependent behavior, causing performance to degrade toward the passive buy-and-hold baseline.

## Falsification plan

To falsify the hypothesis that regime-routed specialist GBTs provide genuine market timing alpha:

1. **Cross-Asset Transfer Falsification Test:**
   - *Protocol:* Execute the exact frozen model stack (trained on pre-2013 US equities) out-of-universe on non-US equity indices (Nikkei 225, DAX 40, Hang Seng) and commodities (Gold, Crude Oil) across 2018–2026 with 5 bps transaction costs.
   - *Decision Rule (`research-defined falsification threshold`):* If the strategy fails to achieve a positive annualized Sharpe improvement ($\Delta \text{Sharpe} > 0.15$) and a lower maximum drawdown relative to the underlying buy-and-hold benchmark across at least 3 of the 5 test assets, the universal validity of the regime-specialist mechanism is falsified.
2. **Transaction Cost & Slippage Stress Test:**
   - *Protocol:* Simulate the strategy while parametrically increasing round-trip transaction costs from 5 bps to 10 bps, 15 bps, and 20 bps.
   - *Decision Rule (`research-defined falsification threshold`):* If net annualized Sharpe drops below 0.70 (matching the passive buy-and-hold baseline) at transaction costs $\le 10$ bps, the strategy is falsified as a cost-fragile artifact of frictionless assumptions.
3. **Placebo Regime Routing Test (Shuffled-Regime Null):**
   - *Protocol:* Randomly permute the predicted regime labels $\widehat{R}_t$ prior to routing to specialists and applying hysteresis thresholds, repeating across 1,000 bootstrap runs.
   - *Decision Rule (`research-defined falsification threshold`):* If the true model net Sharpe ratio (1.05) falls within the 90th percentile of the shuffled-routing distribution ($p > 0.10$), the claim that specialist routing provides true structural alpha is falsified.
4. **Macroeconomic Reporting Lag Test:**
   - *Protocol:* Re-evaluate the nowcaster introducing realistic publication delays for macroeconomic data (e.g., lagging unemployment rate by 30 days and GDP/growth indicators by 45 days).
   - *Decision Rule (`research-defined falsification threshold`):* If Sharpe ratio drops by more than 0.20 when lagging monthly macro series to their actual historical announcement dates, the strategy is falsified as containing point-in-time leakage.

## Crypto portability

- **Portability Status:** `adapted` / `unproven`.
- **Primary Source Domain:** Traditional US cash equities and macroeconomic series (`source-reported`). Porting to cryptocurrency markets is a research-proposed hypothesis and has not been demonstrated by the original author.
- **Structural Portability Adjustments (`research-proposed`):**
  1. *24/7 Continuous Trading:* Crypto markets lack the 16:00 EST equity market close. Daily candles must be anchored to 00:00 UTC. Feature lookbacks and rolling standard deviations must adjust to continuous 365-day trading years rather than 252 trading days.
  2. *Macroeconomic Feature Substitution:* US macroeconomic series (Fed Funds, Unemployment) update monthly or intermittently and exhibit weak intraday transmission to altcoins. For crypto perpetuals, replace macro features with native crypto state variables:
     - `vix` $\to$ Deribit Volatility Index (`DVOL`) or 30-day realized volatility (`research-proposed`).
     - `fed_funds_rate` $\to$ 8-hour annualized perpetual funding rate (`research-proposed`).
     - `yield_spread` $\to$ 3-month annualized basis spread (Futures minus Spot) (`research-proposed`).
     - `unemployment_rate` $\to$ Aggregate exchange stablecoin net inflow/outflow ratio (`research-proposed`).
  3. *Volatility Target Calibration:* The 25% annual volatility target designed for US equities is excessively restrictive for crypto, where baseline annual volatility often exceeds 60–90%. Sizing would permanently pin exposure at $\sim 25\text{--}35\%$. The target must be recalibrated to $50\%\text{--}70\%$ for crypto assets (`research-proposed`).
  4. *Funding Cost Friction:* In perpetual futures, staying in cash or maintaining long positions incurs variable funding payments that must be factored into the idle cash return model.

## Limitations

- **Equities-Only Empirical Sample:** The primary author validation is conducted exclusively on large-cap US equities and index ETFs (SPY); performance on fragmented or highly volatile crypto assets is unverified (`source-gap`).
- **Macroeconomic Publication Delay Vulnerability:** The nowcaster ingests monthly unemployment rates without modeling real-time Bureau of Labor Statistics (BLS) revision cycles (`source-gap`).
- **Path-Dependent Hysteresis Sensitivity:** The state machine relies on continuous execution. Missing daily data or running on disconnected segments requires a 320-day warmup period to guarantee that the hysteresis state matches historical trajectory (`source-reported`).
- **Execution Fill Assumption:** T+1 close-to-close returns assume fill execution without market impact or spread slippage, which may degrade live performance during violent volatility regime transitions (`source-gap`).

## Implementation status

`not-implemented`. This record represents an upstream research capture. No model code has been integrated into `nautilus-quant-system`, PyBroker, or NautilusTrader, and no paper or testnet deployment is authorized.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- **Boundary Notice:** Inclusion in this repository does not authorize live execution, paper trading, or capital allocation. Any potential live adoption requires rigorous out-of-sample reproduction, point-in-time publication auditing, and formal quantitative approval.

## Related Wiki records

- `[[quant/regime-switching-hmm-reinforcement-learning-etf-allocation-2026-09-04]]` — Markov-switching regime models coupled with reinforcement learning for ETF timing.
- `[[quant/two-level-uncertainty-cross-sectional-ranker-regime-trust-gate-tail-cap-2026-09-05]]` — Dual-level regime trust gating and tail-risk exposure clipping.
- `[[quant/simple-dynamic-stock-bond-gold-markowitz-volatility-control-2026-09-11]]` — Volatility-targeted dynamic risk balancing across asset classes.
- `[[quant/staged-short-term-drawdown-reversal-ml-timing-overlay-2026-09-12]]` — Machine learning overlays for drawdown reversal timing.

## Sources

1. Shuyao Xu. *"Alpha Timing: Regime-Aware Quantitative Trading."* GitHub repository `davidxu277/alpha-timing`, commit `299db752becd7023d2b5360f1c6e238572d60e3e`, September 12, 2026.
   - Repository URL: [https://github.com/davidxu277/alpha-timing](https://github.com/davidxu277/alpha-timing)
   - Live Dashboard: [https://davidxu277.github.io/alpha-timing/](https://davidxu277.github.io/alpha-timing/)
   - Code entry point: [`regime_trading.py`](https://github.com/davidxu277/alpha-timing/blob/299db752becd7023d2b5360f1c6e238572d60e3e/regime_trading.py)
   - Daily track record ledger: [`docs/data/track_record.jsonl`](https://github.com/davidxu277/alpha-timing/blob/299db752becd7023d2b5360f1c6e238572d60e3e/docs/data/track_record.jsonl)
2. James D. Hamilton. *"A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle."* Econometrica, Vol. 57, No. 2, pp. 357–384, 1989.
3. Andrew Ang and Geert Bekaert. *"International Asset Allocation with Regime Shifts."* The Review of Financial Studies, Vol. 15, No. 4, pp. 1137–1187, 2002.
4. Charles M. C. Lee and Bhaskaran Swaminathan. *"Price Momentum and Trading Volume."* The Journal of Finance, Vol. 55, No. 5, pp. 2017–2069, 2000.
