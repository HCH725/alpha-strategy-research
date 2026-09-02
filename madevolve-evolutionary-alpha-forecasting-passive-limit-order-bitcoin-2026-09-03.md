---
schema: strategy-research-record-v1
title: "MadEvolve: Multi-Horizon Alpha Forecasting and Impact-Aware Passive Limit Order Execution for Bitcoin"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - limit-order-book
  - market-microstructure
  - execution-algorithm
  - evolutionary-optimization
  - alpha-forecasting
status: research-only
confidence: medium
source_as_of: 2026-05-31
sources:
  - "Yurii Kvasiuk, Tianyi Li, Owen Colegrove, Moritz Münchmeyer, 'MadEvolve: Evolutionary Optimization of Trading Systems with Large Language Models', arXiv:2605.23007v1 [q-fin.TR], May 2026. https://arxiv.org/abs/2605.23007"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MadEvolve: Multi-Horizon Alpha Forecasting and Impact-Aware Passive Limit Order Execution for Bitcoin

## Provenance

- **Source Paper:** *MadEvolve: Evolutionary Optimization of Trading Systems with Large Language Models*
- **Authors:** Yurii Kvasiuk, Tianyi Li, Owen Colegrove, Moritz Münchmeyer
- **ArXiv Identifier:** arXiv:2605.23007v1 [q-fin.TR, cs.AI, cs.LG, q-fin.PM]
- **DOI / Canonical URL:** https://doi.org/10.48550/arXiv.2605.23007 | https://arxiv.org/abs/2605.23007
- **Submission Date:** May 2026 (source as-of 2026-05-31)
- **Data & Instrument:** BTCUSD 1-minute historical bar data (OHLCV) from Polygon; market impact model calibrated to Hyperliquid BTC-USD perpetuals.
- **Data Splits:**
  - In-Sample Training (alpha model fitting only): 2022-01-01 to 2023-12-31 (730 days)
  - Validation Split (evolution / strategy selection): 2024-01-01 to 2024-12-31 (366 days)
  - Out-of-Sample Test Split (unseen evaluation): 2025-01-01 to 2025-10-10 (283 days)

## Economic mechanism

### Source-reported

The paper investigates the application of an LLM-driven evolutionary optimization framework (MadEvolve, derived from Alpha-Evolve principles) to algorithmic trading in Bitcoin markets, separating the trading system into two interacting problem classes:
1. **Financial Forecasting (Alpha Generation):** Predicting short-to-medium-term cumulative log returns (horizons of 1, 10, 100, and 1,000 minutes) from 1-minute OHLCV data using a multi-scale feature pipeline and Ridge regression ($L_2$ regularization $\alpha = 0.5$).
2. **Algorithm & Execution Optimization:** Converting continuous alpha predictions into target inventory positions and executing them exclusively via passive limit orders within a discrete 1-minute decision interval, subject to exchange taker/maker fee thresholds, inventory holding constraints, and square-root propagator market impact.

The source reports the discovery of several key algorithmic mechanisms through evolutionary search:
- **Multi-Scale Band-Pass Feature Decomposition:** Replacing simple price momentum with three tiered band-pass filters (short, medium, long halflives) that filter out high-frequency noise and low-frequency macroeconomic drift, isolating the predictable 10-minute return cycle.
- **Microstructure-Adaptive Limit Order Pricing:** Evolving an expected utility quoting depth that anchors limit orders to an alpha-adjusted fair value mid-price ($\hat{m}_t = m_t(1 + \omega_\alpha \alpha)$), tightening spreads when quoting with the signal and widening spreads when opposing it to minimize adverse selection.
- **Dynamic Impact-Aware Hysteresis (No-Trade Band):** Suppressing turnover churn by setting a variable deadband based on recent turnover, inventory utilization, and signal dispersion, preventing trades where expected edge fails to clear fees and market impact.
- **Nonlinear Conviction Sizing:** Applying super-linear power-law scaling ($1 + 3.0 |\alpha_z|^{1.25}$) to trade sizes under high-conviction signals while enforcing smooth tanh-saturation against inventory limits.
- **Alpha-to-Execution Calibration Coupling:** Demonstrating empirically that an evolved alpha model with superior predictive metrics (doubled $R^2$, +50% IC/ICIR) severely underperformed the baseline in realized PnL when dropped into an uncalibrated execution module, but delivered a +475% increase in out-of-sample PnL ($27,842 \to \$159,967) once execution parameters (quoting depth, sizing, no-trade bands) were recalibrated via Bayesian optimization (Optuna TPE).

### Research interpretation

The falsifiable core hypothesis is: **In high-frequency passive crypto execution, alpha returns cannot be realized as economic profits without jointly matching quoting depth, no-trade deadbands, and inventory penalty curvatures to the specific scale, half-life, and error dispersion of the underlying alpha predictor.**

The strategy operates as a multi-component hybrid:
```text
Alpha Signal: Multi-scale band-pass momentum + order-flow proxy + mean-reversion state -> Ridge multi-horizon return forecast
Regime / Volatility Filter: Ratio of fast-to-slow realized volatility + log range stress proxy
Cost / Churn Gate: Dynamic hysteresis deadband scaled by fee rate, turnover EMA, and alpha volatility
Position Sizing: Nonlinear power-law conviction scaling with tanh inventory saturation
Quoting & Execution: Fair-value mid anchoring + asymmetric quoting depth + realized pickoff penalty
```

Economic drivers:
- **Adverse Selection Protection:** Quoting passively at the top of the book exposes the strategy to informed order flow ("toxic fills"). Asymmetric quoting depth forces the counterparty to cross a wider spread when trading against the strategy's predicted direction.
- **Inventory Mean-Reversion Pressure:** Holding non-zero inventory incurs market risk. The strategy applies a cubic/parabolic inventory penalty that softly dampens trading as inventory nears capacity without abrupt cliff-like stops.
- **Frictional Haircut Avoidance:** The dynamic no-trade band internalizes exchange fees (1.5 bps) and superlinear market impact, filtering out marginal signals that generate negative net PnL after friction.

## Signal

The system decomposes into two stages: the **Alpha Forecaster** and the **Passive Executor**.

### 1. Alpha Forecaster
- **Input:** 1-minute OHLCV bars.
- **Baseline Feature Set:** Demeaned exponential moving averages (EMA) of 1-minute returns with spans of 1, 5, and 10 minutes:
  $$\text{ema\_ret\_k} = \text{EMA}(r_t, \text{span}=k)$$
- **Evolved Feature Set (Run 4 / Run 5):** 77 features spanning roughly 20 families:
  - *Multi-scale band-pass momentum:* Halflives arranged in a Fibonacci progression ($h \in \{1, 2, 3, 5, 8, 13, 21, 34, 55, 89\}$ minutes) demeaned against longer windows (e.g. 20, 60, 240 minutes) to attenuate noise and secular trend.
  - *Mean-reversion state:* Price deviation from 60-minute EMA: $z_{60} = m_t - \text{EMA}(m_t, 60)$, and velocity $\Delta z_{60} = \text{EMA}(z_{60}, 5) - \text{EMA}(z_{60}, 20)$.
  - *Order-flow / volume proxies:* Log volume impulse $\log(V_t / \text{EMA}(V_t, 45))$, signed volume flow $\text{EMA}(r_t \cdot \log V_t, 12)$, and signed flow divergence $\text{EMA}(r_t \cdot V_t / \text{EMA}(V, 45), 10) - \text{EMA}(\dots, 45)$.
  - *Volatility regime & stress:* Ratio of fast to slow volatility $\text{vol}_{\text{fast}} / \text{vol}_{\text{slow}}$ ($h=5$ vs $h=66$), squared volatility deviation $(\text{vol\_ratio} - 1)^2$, and range stress $\log(H_t / L_t) / \text{vol}_{\text{slow}} - \text{EMA}(\dots, 30)$.
  - *Stability Winsorization:* All constructed features winsorized globally at $\pm 5\sigma$ (or bounded ranges like volatility ratio in $[0.2, 5.0]$) to protect downstream regressions from outlier distortion.
- **Model:** Ridge regression with regularization parameter $\alpha = 0.5$, predicting cumulative log returns at horizons of 1, 10, 100, and 1,000 minutes:
  $$y_\tau = \ln(C_{t+\tau} / C_t), \quad \tau \in \{1, 10, 100, 1000\}$$
- **Primary Signal:** The 10-minute horizon forecast $\alpha_t$ and its rolling standard deviation $\sigma_\alpha$.

### 2. Passive Limit Order Execution Logic
Every minute $t$:
1. **Stale Information & Realized Price Correction:**
   $$\alpha_{\text{corr}} = \alpha_t - c \cdot \ln(m_t^{\text{book}} / m_t)$$
   where $m_t^{\text{book}}$ is the current mid-book price, $m_t$ is the mid at alpha publication, and $c$ is a context correction factor (default 0 in baseline, evolved in Run 3/5). In Run 3, if the realized move already absorbed the alpha direction, $\alpha_{\text{corr}}$ is shrunk by up to 95% (exhaustion correction).
2. **Effective Alpha with Inventory Penalty:**
   $$\alpha_{\text{eff}} = \alpha_{\text{corr}} - 1.8 \cdot q_r \cdot \sigma_\alpha \cdot (1 + 1.5 |q_r|)$$
   where $q_r = q_{\text{usd}} / q_{\max} \in [-1, 1]$ is the normalized inventory ratio ($q_{\max} = \$200,000$).
3. **Dynamic Hysteresis / No-Trade Band:**
   $$\text{deadband} = f_{\text{exp}} \cdot \left(1.2 + 0.5 \frac{\alpha_{\text{vol}}}{\sigma_\alpha}\right)$$
   where $f_{\text{exp}} = \max(0.00015 - \text{depth}, 0.00005)$ is the expected net fee. If $|\alpha_{\text{eff}}| < \text{deadband}$ and position opposes alpha, risk reduction is engaged; otherwise no new risk-adding order is submitted.
4. **Target Position Calculation:**
   $$\text{target\_pos\_usd} = q_{\max} \cdot \tanh(s \cdot \ell)$$
   where $s = \alpha_{\text{eff}} / \sigma_\alpha$ is signal conviction, and $\ell = 1.3 - 0.3 |q_r|$ is inventory-tapered leverage.
   - Sizing Conviction Boost: In Run 5, effective trade size scales superlinearly: $1 + 3.0 |\alpha_z|^{1.25}$ (capped at 3.8).
   - Hysteresis Buffer: Target updates only if $|\text{target}_{\text{new}} - \text{target}_{\text{cached}}| > 0.025 \cdot q_{\max}$.
5. **Turnover Governor:**
   - Tracks 1-minute EMA of traded USD notional. If the EMA exceeds $0.15 \cdot q_{\max}$, non-risk-reducing trade sizes are halved.
6. **Passive Order Pricing (Limit Price):**
   - Anchored to Fair Value Mid:
     $$\hat{m}_t = m_t^{\text{book}} \cdot (1 + \omega_\alpha \alpha_t), \quad \omega_\alpha \approx 0.6$$
   - Quoting Depth ($d$): Volatility-scaled base depth adjusted by conviction and side:
     $$d = z_p \cdot \text{std} \cdot (1.15 - 0.7 \tanh(|s|)) \cdot \text{clip}(1 + 1.4 q_r \cdot \text{side}, 0.15, 2.8)$$
     When quoting in the direction of alpha, $d$ tightens; when opposing, $d$ widens.
   - Limit Price:
     $$p_t^{\text{limit}} = m_t^{\text{book}} \cdot \exp(-\text{side\_multiplier} \cdot d)$$
     where $\text{side\_multiplier} = +1$ for BUY and $-1$ for SELL.

## Required data

- **Instrument:** Bitcoin (BTCUSD).
- **Venue:** Polygon aggregated crypto feed (minute bars); Hyperliquid BTC-USD perpetuals (used for propagator impact calibration).
- **Market Type:** Spot / Perpetual Futures equivalent (tested on cash USD-denominated BTC bars).
- **Timeframe:** 1-minute discrete bars ($T = 1\text{ min}$).
- **Data Fields:** Open, High, Low, Close, Volume (OHLCV).
- **Point-in-Time Separation:** Strictly enforced chronological splits:
  - Alpha Fitting (Train): 2022-01-01 to 2023-12-31.
  - Evolutionary Search & Parameter Selection (Validation): 2024-01-01 to 2024-12-31.
  - Out-of-Sample Backtest (Test): 2025-01-01 to 2025-10-10.
- **Look-Ahead Protections:** Features computed strictly from historical candle close; labels shifted forward ($t+\tau$).
- **Missing Data:** Filled with 0 / forward fill in feature matrix; invalid limit prices ($\text{NaN}$) suppress order placement.

## Execution assumptions

- **Decision Cadence:** Exactly 1 decision per 1-minute candle.
- **Order Lifecycle:** Single resting limit order at any given time. Each minute:
  1. `exchange_response()` checks whether the resting order filled during the candle range.
  2. Portfolio inventory is updated: $q_{t+1} = q_t + \Delta q_t^{\text{fill}}$.
  3. `cancel_open_orders()` cancels remaining open orders.
  4. Strategy computes new target quantity and new limit price.
  5. `submit_order()` places the new resting limit order.
- **Fill Logic:**
  - Buy order fills if candle $\text{Low} < p_t^{\text{limit}}$.
  - Sell order fills if candle $\text{High} > p_t^{\text{limit}}$.
  - Execution occurs at the limit price $p_t^{\text{limit}}$ (no favorable price improvement, zero adverse slippage beyond limit price).
  - Executed quantity: $\Delta q_t^{\text{fill}} = \text{hit\_ratio} \cdot \Delta q_t^{\text{ord}}$ (default $\text{hit\_ratio} = 1.0$).
- **Transaction Fees:** Fixed at 1.5 basis points ($0.00015 \cdot m_t \cdot |\Delta q_t^{\text{fill}}|$) per filled trade.
- **Market Impact Model:** Propagator square-root impact model with power-law temporal decay:
  $$D(t_i) = \sum_{j \le i} s_j G(t_i - t_j), \quad s_j = \text{sign}(Q_j) \cdot c_I \left(\frac{|Q_j|}{V_{\text{daily}}}\right)^{0.5}, \quad G(\tau) = \left(1 + \frac{\tau}{\tau_0}\right)^{-\beta}$$
  Calibrated to Hyperliquid BTC-USD perpetuals. Conservative full self-impact charged ($G(0) = 1$).
- **Capital & Position Caps:** Maximum position size $q_{\max} = \$200,000$; maximum single limit order size $\$100,000$; maximum trade fraction per interval $\text{max\_trade\_frac} = 0.20$ ($20\%$ of $q_{\max}$).

## Evidence

### Source-reported

All quantitative figures below are cited directly from the paper (Table 1, Table 2, Table 3, Table 5, Section 5, and Section 5.7):

#### 1. Strategy Evolution Performance (Table 1 & Table 3)
Evaluated across 2024 Validation Split (IS) and 2025 Test Split (OOS):

| Configuration | Val Sharpe | Val PnL ($K) | Val Traded Vol ($M) | Test Sharpe (OOS) | Test PnL ($K, OOS) | Test Win Rate |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Baseline (shared)** | **4.81** | **$83** | **$502** | **3.82** | **$47** | **60.1%** |
| Run 1 (Target only) | 4.83 (1.00x) | $533 (6.42x) | $3,336 (6.65x) | 4.45 (1.16x) | $271 (5.77x) | 55.1% (0.92x) |
| Run 2 (Order only) | 6.49 (1.35x) | $2,238 (27.0x) | $10,289 (20.5x) | 5.12 (1.34x) | $1,205 (25.6x) | 61.1% (1.02x) |
| Run 3 (Joint Target+Order) | 6.51 (1.35x) | $973 (11.8x) | $4,449 (8.86x) | 5.11 (1.34x) | $473 (10.1x) | 53.0% (0.88x) |
| Run 5 (Joint Feature+Strategy) | 8.85 (1.84x) | $1,855 (22.3x) | $7,318 (14.6x) | **5.65 (1.48x)** | $724 (15.4x) | 49.8% (0.83x) |

- **Pure Sizing Disproof:** The paper disproves that PnL gains were artifacts of pure position scaling. The counterfactual sizing ratio $\text{PnL}_{\text{evolved}} / \text{PnL}_{\text{sized}}$ (which accounts for $k^{1.5}$ impact cost scaling) exceeds $1.0$ across all runs ($1.2\times$ to $2.9\times$ on test, $1.4\times$ to $4.1\times$ on validation). Scale-invariant Calmar ratio improved across all runs out-of-sample ($2.1\times$ to $3.0\times$).

#### 2. Feature Evolution for Alpha Forecasting (Run 4, Table 2)
Scored by composite metric $0.5 R^2 + 0.3 \text{IC} + 0.2 (\text{ICIR}/5)$:
- **Combined Score:** $0.085 \to 0.128$ (+51% relative gain).
- **Mean Daily Spearman IC:** Validation: $0.074 \to 0.110$; Test (OOS): $0.059 \to 0.099$.
- **Information Coefficient Information Ratio (ICIR):** Validation: $1.03 \to 1.56$; Test (OOS): $0.99 \to 1.35$.
- **10-minute Return $R^2$:** Validation: $0.0021 \to 0.0043$; Test (OOS): $0.0017 \to 0.0034$.

#### 3. Hyperparameter Recalibration & Alpha-Execution Coupling (Section 5.7, Table 5)
Evaluated using Optuna TPE (120 trials: 30 random + 90 guided) on validation set, tested once on 2025 OOS:
- **Baseline Forecaster:**
  - Default execution params: Test PnL = $46,791, Test Sharpe = 3.82.
  - Calibrated execution params: Test PnL = $103,089 (+120%), Test Sharpe = 4.15.
- **Evolved Forecaster (Run 4):**
  - Default execution params: Test PnL = **$27,842** (a $-40.5\%$ drop relative to baseline, despite superior IC and $R^2$).
  - Calibrated execution params: Test PnL = **$159,967** (a **+475%** increase over uncalibrated), beating the calibrated baseline by $\approx \$57,000$ on the test set.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Uncalibrated Forecaster Collapse:** Swapping a higher-quality alpha forecaster (doubled $R^2$) into an execution policy tuned for a weaker alpha caused out-of-sample PnL to drop from $\$46,791$ to $\$27,842$. High-accuracy predictors without calibrated execution fail out-of-sample.
- **Win Rate Erosion in Joint Optimization:** In Run 5, the win rate degraded from $68.6\%$ in-sample to $49.8\%$ out-of-sample (an 18.8 percentage-point drop), indicating that the strategy shifted from reliable small captures to volatile tail captures.
- **PnL Retention Gap:** Run 5 exhibited the lowest validation-to-test PnL retention ($39\%$, compared to $49\text{--}54\%$ for component runs), reflecting multiple-testing overfitting from the larger search space.
- **Rugged Search Landscape in Joint Strategy Evolution:** Run 3 per-generation best PnL frequently collapsed near zero during evolution before recovering, showing severe instability when modifying sizing and pricing simultaneously.
- **Exchange Aggregation Artifacts:** The paper explicitly acknowledges that Polygon BTCUSD minute bars aggregate across multiple venues, creating synthetic microstructure patterns (elevated $R^2$) that do not exist on any single venue's order book.

## Falsification plan

1. **Exchange-Specific LOB Walk-Forward Audit:** Re-evaluate the evolved execution logic on native, non-aggregated Binance or Bybit BTCUSDT 1-minute order book data. If the out-of-sample Sharpe drops below $1.5$ after maker fees and tick-level queue priority, reject the passive execution edge as an aggregation artifact.
2. **Ablation of Dynamic Hysteresis Deadband:** Set the deadband to a static fee threshold ($f_{\text{exp}} = 0.00015$) without turnover/volatility scaling. If turnover increases by $>50\%$ and net PnL drops by $>30\%$, confirm the deadband as an essential alpha-preservation mechanism.
3. **Ablation of Fair Value Mid Anchoring:** Set $\omega_\alpha = 0$ (quote symmetrically around mid-book). If adverse selection (measured as post-fill price drift against inventory) increases by $>2\text{ bps}$, confirm fair value skewing as a necessary defense.
4. **Parameter Perturbation Test:** Perturb the power-law sizing exponent ($1.25 \pm 0.25$) and inventory penalty power ($2.2 \pm 0.4$). If out-of-sample Sharpe degrades by $>40\%$, classify the sizing formulation as over-parameterized.
5. **Decoupled Forecaster Execution Test:** Pair the evolved Run 4 forecaster with random/uncalibrated execution parameters across 50 Monte Carlo seeds. If the median PnL is negative, confirm that alpha predictability is strictly conditional on execution calibration.

## Crypto portability

**Portability Status:** `direct`

- **Native Evaluation:** The source research directly developed, parameterized, and backtested the strategy on Bitcoin (BTCUSD) 1-minute candle data with execution fees (1.5 bps) and market impact calibrated to Hyperliquid BTC-USD perpetuals.
- **Perpetual vs Spot Considerations:**
  - The backtest models cash/USD-denominated spot BTC without 8-hour funding rates. In a live perpetual setting (e.g. Binance/Bybit BTCUSDT or Hyperliquid BTC-USD), funding payments must be added to the inventory penalty function.
  - 24/7 continuous session is natively assumed by the 1-minute bar continuous simulation.
- **Venue Fragmentation Risk:** Polygon aggregates multiple spot exchanges. Real-world implementation on a single venue requires handling venue-specific order queue priority, cancel-replace rate limits, and latency spikes.

## Limitations

- **Not independently reproduced.**
- **Aggregated Data Bias:** Using cross-exchange aggregated minute bars oversimplifies order fill mechanics; true limit order fills depend on local order book queue position, not just candle range $(L < p^{\text{limit}} < H)$.
- **Omission of Funding Rates:** The simulation does not charge or credit perpetual funding rates.
- **Fixed Fee Model:** A flat 1.5 bps fee was assumed; modern VIP maker tiers on Binance or Bybit often offer 0.0 bps or rebates, which would substantially alter the optimal quoting depth $z_p$.
- **Full Evolved Feature Code Not Fully Printed:** While the 20 feature families, mathematical formulations, and baseline code are fully documented, the exact code for all 77 evolved features in Run 4 is partially summarized rather than completely listed line-by-line.

## Implementation status

Not implemented. No PyBroker, NautilusTrader, Paper, Testnet, or Live verification has been performed.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- The strategy is profitable on live venues.
- The alpha has been validated under real-world tick queues.
- The strategy is approved for paper trading, testnet, or live deployment.

No implementation or trading authorization is granted.

## Related Wiki records

No stable Hermes Wiki Brain link is added in this Scout cycle.

Related existing research records in the repository examine limit order book microstructure and reinforcement learning execution overlays (e.g. `multi-level-market-making-logistic-normal-deep-sets-2026-09-02.md`, `crypto-drl-execution-overlay-multi-pair-trading-2026-09-01.md`, and `fineft-risk-aware-ensemble-rl-vae-routing-crypto-futures-2026-09-03.md`). This record is preserved independently because its core mechanism—joint evolutionary co-design of multi-scale band-pass momentum forecasting with impact-aware passive limit order execution, fair-value mid anchoring, and Bayesian alpha-execution recalibration—is structurally and methodologically distinct.

## Sources

1. Yurii Kvasiuk, Tianyi Li, Owen Colegrove, Moritz Münchmeyer. *MadEvolve: Evolutionary Optimization of Trading Systems with Large Language Models*. arXiv:2605.23007v1 [q-fin.TR], May 2026. DOI: https://doi.org/10.48550/arXiv.2605.23007. URL: https://arxiv.org/abs/2605.23007
