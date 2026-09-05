---
schema: strategy-research-record-v1
title: "Forward-Oriented Causal Observables via Kalman-Stabilized Multi-Feature Aggregation and Adaptive Phase-Lead Derivative Operator on High-Frequency EURUSDT"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - causal-inference
  - high-frequency
  - signal-engineering
  - kalman-filter
  - phase-lead-operator
  - technical-indicators
  - momentum
  - mean-reversion
  - non-stationary
  - regime-shift
  - forex-crypto
status: research-only
confidence: medium
source_as_of: 2025-12-31
sources:
  - "Lucas A. Souza, 'Forward-Oriented Causal Observables for Non-Stationary Financial Markets', arXiv:2512.24621v1 [q-fin.CP], December 31, 2025. https://arxiv.org/abs/2512.24621"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forward-Oriented Causal Observables via Kalman-Stabilized Multi-Feature Aggregation and Adaptive Phase-Lead Derivative Operator on High-Frequency EURUSDT

## Provenance

- **Primary Source:** Lucas A. Souza (Instituto de Física, Universidade de São Paulo, Brazil; email: `lasouza@if.usp.br`), *"Forward-Oriented Causal Observables for Non-Stationary Financial Markets"*, arXiv preprint `arXiv:2512.24621v1 [q-fin.CP]`, submitted December 31, 2025. Target journal: *Physica A: Statistical Mechanics and its Applications*.
- **Canonical arXiv Abstract URL:** [https://arxiv.org/abs/2512.24621](https://arxiv.org/abs/2512.24621)
- **Canonical DOI:** [https://doi.org/10.48550/arXiv.2512.24621](https://doi.org/10.48550/arXiv.2512.24621)
- **Full-Text HTML Source:** [https://arxiv.org/html/2512.24621v1](https://arxiv.org/html/2512.24621v1)
- **Primary Source Package Audit:** Direct audit of unpacked source tarball `arXiv:2512.24621` (`main.tex`, `bib.bib`, `indicators.pdf`, `pnl_F_vs_bnh.pdf`, `cumulative_returns_target_horizons.pdf`). All mathematical definitions, indicator parameters, Kalman equations, finite-difference scalings, empirical table values, and figures trace directly to the author's primary LaTeX source and vector figure data.
- **Pre-Write Deduplication & Identity Audit:** Exhaustive search across all repository records in `alpha-strategy-research` confirmed zero matching records for `2512.24621`, `Lucas A. Souza`, `causal observable`, or `EURUSDT`. While existing records explore Granger-causal directed networks (`crypto-time-dependent-weighted-directed-network-granger-causality-2026-09-01.md`) or macro causal sieves (`deepm-regime-robust-macro-graph-causal-sieve-evar-2026-09-03.md`), none investigate online causal centering, 1D Kalman signal stabilization, and state-dependent phase-lead derivative mixing for short-horizon directional trading under strict non-anticipative constraints.

## Economic mechanism

### Source-reported

In non-stationary financial markets, market participants operate under physical and structural information constraints where price dynamics emerge from the collective interaction of heterogeneous agents across multiple timescales. Standard technical indicators (momentum, volume pressure, trend acceleration, and volatility-normalized location) and black-box machine learning models frequently suffer from two severe failure modes:
1. **Look-Ahead Contamination:** Common preprocessing operations—such as batch normalization, two-sided rolling smoothing, and forward-looking target engineering—unintentionally inject future information ($t + \tau$) into decision inputs at time $t$, creating illusory backtest outperformance that collapses in live execution.
2. **Phase Lag in Causal Smoothing:** Strictly causal filters (e.g., standard moving averages or low-pass filters) introduce unavoidable phase delays. When indicators fluctuate around transition regions (zero crossings), this phase lag causes late entries and exits, capturing the tail of a move rather than its inception.
3. **The Phase-Lead Derivative Solution:** In physical and dynamical systems, the first derivative $\dot{x}(t)$ provides local directional velocity and phase-lead information. For an oscillatory or wave-like signal, the derivative acts as an anticipatory phase-shifted proxy. Souza hypothesizes that an adaptive forward-like operator—mixing a stabilized composite signal $\mathscr{F}_0(t)$ with a smoothed causal finite-difference derivative $\widetilde{\partial_t \mathscr{F}_0}(t)$—can supply forward-oriented predictive structure without violating online computability:
   - When $|\mathscr{F}_0(t)|$ is large (persistent directional trend), the observable relies primarily on the level $\mathscr{F}_0(t)$.
   - When $|\mathscr{F}_0(t)| \approx 0$ (critical regime transition or consolidation boundary), the level carries little directional bias; here, the derivative term dominates, capturing local acceleration before the price level has fully diverged.

### Research interpretation

The proposed strategy is an **engineered composite technical alpha with an adaptive phase-lead anticipatory operator**. Economically, it relies on short-term order-flow momentum and liquidity rebalancing in the 1-minute FX/stablecoin market (EURUSDT).

The architecture decomposes into a four-layer signal pipeline:
1. **Causal Non-Parametric Centering:** Eliminates baseline drift without look-ahead by subtracting the causal median of historical indicator values up to time $t-1$.
2. **Orthogonal Dimensional Aggregation:** Aggregates four complementary market dimensions (relative price momentum via RSI, volume-weighted buying/selling pressure via MFI, short-term trend acceleration via MACD histogram, and volatility-normalized price location via Bollinger %B).
3. **State-Space Denoising:** A 1D Kalman filter treats the raw composite signal as a hidden random walk corrupted by Gaussian observation noise, stripping high-frequency microstructural tick noise without future smoothing.
4. **Nonlinear Phase-Lead Blending:** A state-dependent $\tanh$ gating mechanism transitions dynamically between trend-following (level-dominated) and anticipatory turning-point detection (derivative-dominated).
5. **Hysteresis Threshold Execution:** A two-state finite state machine with a deadband neutral zone $[-\theta, +\theta]$ prevents churn during choppy ranging regimes.

Because the underlying source tests EURUSDT under active Forex session masks without transaction costs, the strategy represents an idealized signal-engineering blueprint. In real-world market execution, high turnover (~1,000 trades/month) makes the alpha highly sensitive to exchange fees, bid-ask spreads, and execution latency.

## Signal

### Mathematical Specification

#### 1. Input Features and Parameterizations (`source-reported`)
The system computes four classical technical indicators at each 1-minute bar $t$ using strictly causal past and contemporaneous data up to bar close $t$:
- **Relative Strength Index ($\text{RSI}_t$):** Standard 14-period Wilder RSI (`source-reported`):
  $$\text{RSI}_t = 100 \left(1 - \frac{1}{1 + \frac{G_t}{L_t}}\right)$$
  where $G_t$ and $L_t$ denote 14-period exponential moving averages of gains and losses.
- **Money Flow Index ($\text{MFI}_t$):** Standard 14-period volume-weighted momentum (`source-reported`):
  $$\text{Typical Price}_t = \frac{\text{High}_t + \text{Low}_t + \text{Close}_t}{3}$$
  $$\text{Raw Money Flow}_t = \text{Typical Price}_t \times \text{Volume}_t$$
  $$\text{MFI}_t = 100 \left(1 - \frac{1}{1 + \frac{\text{Positive Money Flow}_t}{\text{Negative Money Flow}_t}}\right)$$
- **Moving Average Convergence Divergence Difference ($\text{MACD Diff}_t$):** Standard (12, 26, 9) MACD histogram (`source-reported`):
  $$\text{MACD Diff}_t = \left(\text{EMA}_{12}(P_t) - \text{EMA}_{26}(P_t)\right) - \text{EMA}_9\left(\text{EMA}_{12}(P_t) - \text{EMA}_{26}(P_t)\right)$$
- **Bollinger Band Percent ($\text{BB\%}_t$):** Standard 20-period, 2-standard-deviation Bollinger Band location (`source-reported`):
  $$\text{BB\%}_t = \frac{P_t - (\mu_{20,t} - 2\sigma_{20,t})}{(\mu_{20,t} + 2\sigma_{20,t}) - (\mu_{20,t} - 2\sigma_{20,t})} = \frac{P_t - \mu_{20,t} + 2\sigma_{20,t}}{4\sigma_{20,t}}$$

#### 2. Causal Median Centering (`source-reported`)
To eliminate arbitrary level offsets without incorporating future information, each indicator series $I_t^{(k)}$ ($k \in \{\text{MFI}, \text{RSI}, \text{BB}\%, \text{MACD}\}$) is centered using an expanding causal median operator:
$$\tilde I_t^{(k)} = I_t^{(k)} - \operatorname{median}\{ I_\tau^{(k)} : \tau < t \}$$
*Scout note on operational implementation:* In practice, an expanding median over very long histories may incur high computational complexity; a rolling window median (e.g., $W = 1440$ minutes / 1 day) or an efficient order-statistic tree is a `research-proposed` operational approximation.

#### 3. Linear Feature Aggregation (`source-reported`)
The centered features are linearly aggregated using fixed dimensional normalizers:
$$\mathscr{F}_0^{\text{raw}}(t) = \frac{1}{4} \sum_{k=1}^4 \alpha_k \tilde I_t^{(k)} = \frac{1}{4}\left(\alpha_{\text{MFI}} \tilde I_t^{(\text{MFI})} + \alpha_{\text{RSI}} \tilde I_t^{(\text{RSI})} + \alpha_{\text{BB}\%} \tilde I_t^{(\text{BB}\%)} + \alpha_{\text{MACD}} \tilde I_t^{(\text{MACD})}\right)$$
The exact scaling coefficients $\alpha_k$, audited directly from `indicators.pdf` in the primary source package, are:
- $\alpha_{\text{MFI}} = \frac{1}{200} = 0.005$ (`source-reported`)
- $\alpha_{\text{RSI}} = \frac{1}{100} = 0.010$ (`source-reported`)
- $\alpha_{\text{BB}\%} = \frac{1}{3} \approx 0.33333$ (`source-reported`)
- $\alpha_{\text{MACD}} = \frac{1}{3 \times 10^{-4}} = \frac{10000}{3} \approx 3333.33$ (`source-reported`)

#### 4. Causal Denoising via 1D Kalman Filter (`source-reported`)
The raw composite signal $\mathscr{F}_0^{\text{raw}}(t)$ is processed through a recursive one-dimensional Kalman filter to obtain the stabilized observable $\mathscr{F}_0(t)$.
- **Latent State Model:**
  $$x_t = x_{t-1} + w_t, \qquad w_t \sim \mathcal{N}(0, q)$$
- **Measurement Model:**
  $$z_t = x_t + v_t, \qquad v_t \sim \mathcal{N}(0, r)$$
  where measurement $z_t = \mathscr{F}_0^{\text{raw}}(t)$.
- **Hyperparameters (`source-reported`):**
  - Process noise variance: $q = 0.01$
  - Measurement noise variance: $r = 0.1$
- **Online Recursive Update Equations (`source-reported`):**
  1. Time Update (Prediction):
     $$\hat{x}_{t|t-1} = \hat{x}_{t-1|t-1}$$
     $$P_{t|t-1} = P_{t-1|t-1} + q$$
  2. Measurement Update (Correction):
     $$K_t = \frac{P_{t|t-1}}{P_{t|t-1} + r}$$
     $$\hat{x}_{t|t} = \hat{x}_{t|t-1} + K_t \left(z_t - \hat{x}_{t|t-1}\right)$$
     $$P_{t|t} = (1 - K_t) P_{t|t-1}$$
- **Initialization:** $\hat{x}_{0|0} = z_0$, $P_{0|0} = 1.0$ (`research-proposed`).
- **Filtered Observable:** $\mathscr{F}_0(t) = \hat{x}_{t|t}$ (`source-reported`). Strictly forward recursion, zero backward smoothing.

#### 5. Approximate Forward-Oriented Operator (`source-reported`)
To inject local phase-lead without look-ahead, the paper constructs:
$$\mathscr{F}(t) = c_1(t) \mathscr{F}_0(t) + 2 c_2(t) \widetilde{\partial_t \mathscr{F}_0}(t)$$
where:
- **Causal Derivative:** $\mathscr{F}'_0(t) = \mathscr{F}_0(t) - \mathscr{F}_0(t-1)$ (first-order backward difference).
- **Smoothed Derivative:** $\widetilde{\partial_t \mathscr{F}_0}(t)$ is a 4-period causal simple moving average of $\mathscr{F}'_0(t)$:
  $$\widetilde{\partial_t \mathscr{F}_0}(t) = \frac{1}{4} \sum_{j=0}^3 \mathscr{F}'_0(t-j) = \frac{\mathscr{F}_0(t) - \mathscr{F}_0(t-4)}{4}$$
- **Fixed Derivative Scale Factor:** Constant multiplier $2$ (`source-reported`) balances the empirical volatility of the derivative against the level.
- **State-Dependent Mixing Gating Weights (`source-reported`):**
  $$c_1(t) = \tanh\left(|\mathscr{F}_0(t)|\right)$$
  $$c_2(t) = 1 - \tanh\left(\left|\frac{\mathscr{F}_0(t)}{2}\right|\right)$$
  When $|\mathscr{F}_0(t)| \to \infty$, $c_1 \to 1$ and $c_2 \to 0$ (pure trend tracking). When $|\mathscr{F}_0(t)| \to 0$, $c_1 \to 0$ and $c_2 \to 1$ (pure derivative phase lead).

#### 6. Two-State Hysteresis Decision Functional (`source-reported`)
Let $s_t = \mathscr{F}(t)$ denote the decision observable at 1-minute bar $t$. The position state $p_t \in \{0, 1\}$ represents an active long position ($p_t = 1$) or a flat position ($p_t = 0$):
$$p_t = \begin{cases}
1, & \text{if } p_{t-1} = 0 \text{ and } s_t > \theta \\
0, & \text{if } p_{t-1} = 1 \text{ and } s_t < -\theta \\
p_{t-1}, & \text{otherwise}
\end{cases}$$
- **Decision Threshold:** $\theta = 0.06$ (`source-reported`), chosen as a fixed moderate percentile of the empirical distribution of $\mathscr{F}(t)$ without performance optimization.
- **Neutral Band:** $[-\theta, +\theta] = [-0.06, +0.06]$. While within the band, the prior state $p_{t-1}$ is retained.
- **Execution Timing:** Strictly one-step delayed execution: the position applied during bar interval $(t, t+1]$ is $p_t$, yielding realized period return $R_{t+1} = p_t r_{t+1}$ where $r_{t+1} = \frac{P_{t+1} - P_t}{P_t}$ (`source-reported`).

## Required data

### Data Specifications (`source-reported`)
- **Instrument:** EURUSDT (Euro / Tether USD spot or perpetual).
- **Timeframe:** 1-minute ($1\text{m}$) OHLCV bars.
- **Required Fields:** `timestamp`, `open`, `high`, `low`, `close`, `volume`.
- **Session Filter (`source-reported`):**
  - Active Forex trading hours filter: Saturdays removed entirely.
  - Sundays before 18:00 (local exchange time) removed.
  - Fridays after 18:00 (local exchange time) removed.
  - Bars within the active session must be contiguous.
- **Sample Period in Primary Source:** January 2023 through approximately early 2026 (over 3 years of 1-minute data).
- **Missing Data Handling (`research-proposed`):** Forward-fill missing 1-minute ticks within active session; flag missing spans exceeding 5 consecutive minutes as data outage and force state $p_t = 0$.

## Execution assumptions

### Source-Reported Setup
- **Frictionless Baseline:** The source explicitly reports all performance **without transaction costs**, bid-ask spread, or slippage. The author explicitly states:
  > *"Importantly, all results in this section are computed without transaction costs. This isolates the intrinsic economic relevance of the proposed causal observable from market frictions; the implications of even minimal fees are discussed in the concluding section... Given the high turnover, even small frictions would materially reduce net performance, so the reported outcomes should be interpreted as evidence of predictive structure under idealized conditions rather than as an execution-ready trading strategy."*
- **Order Timing:** Bar-close decision at $t$, executed at the open of bar $t+1$ (one-step lag $p_t r_{t+1}$).
- **Position Allocation:** Binary long/flat ($p \in \{0, 1\}$). No shorting evaluated in source.

### Operational Reality & Research-Proposed Execution Layer
To evaluate this strategy in a realistic quantitative execution engine (e.g., NautilusTrader / PyBroker), the following `research-proposed` parameters must be enforced:
- **Order Type:** Passive maker limit order with 1-bar cancel/replace, or aggressive taker order at $t+1$ open.
- **Fee Model (`research-proposed`):** VIP / institutional taker fee of $1.5\text{ bps}$ ($0.015\%$) or VIP maker rebate of $-0.5\text{ bps}$.
- **Slippage & Spread Model (`research-proposed`):** Average EURUSDT bid-ask spread is $\sim 0.5 - 1.0\text{ bps}$ ($0.00005 - 0.00010$).
- **Turnover Drag:** At $\sim 1,055$ trades/month (approx. 35 trades/day), a round-trip fee of $3\text{ bps}$ ($0.03\%$) amounts to:
  $$1,055 \times 0.03\% \approx 31.65\% \text{ fee drag per month}$$
  This confirms the author's caveat: raw frictionless returns are completely erased by taker execution costs unless execution is heavily filtered or passive limit order capture is achieved.

## Evidence

### Source-reported

Source: Lucas A. Souza, arXiv:2512.24621v1, Table 1 and Figures 2–3.
- **Subperiod 1 (January 2023 – September 2024, ~21 months):**
  - Final Equity $V$: $3.14$ (initial capital $V_0 = 1.0$)
  - Cumulative Return: $+214\%$
  - Maximum Drawdown (MDD): $-4\%$
  - Monthly Activity: $959\text{ trades/month}$
- **Subperiod 2 (Post-September 2024 – early 2026, ~15 months):**
  - Final Equity $V$: $2.74$ (normalized from $V_0 = 1.0$ at regime change)
  - Cumulative Return: $-13\%$
  - Maximum Drawdown (MDD): $-17\%$
  - Monthly Activity: $1,117\text{ trades/month}$
- **Full Period Summary:**
  - Average Monthly Turnover: $1,055\text{ trades/month}$ for $\mathscr{F}(t)$ vs. $1,170\text{ trades/month}$ for raw $\mathscr{F}_0(t)$.
  - Total State Transitions: $> 35,000$ trades over the 3-year evaluation window.
  - Benchmark Comparison: Substantially outperformed Buy-and-Hold during Subperiod 1 ($+214\%$ vs. modest single-digit FX drift), but plateaued and decayed post-September 2024 while turnover remained high.
  - Component Contribution: Direct comparison against raw composite $\mathscr{F}_0(t)$ (without the adaptive forward derivative operator) showed that $\mathscr{F}_0(t)$ exhibited much lower cumulative growth, earlier saturation, and failed to capture turning points in transition regions.

### Independently reproduced

`Not independently reproduced.` The strategy has not been tested in our local backtesting stack (`pybroker` or `nautilus_trader`).

### Negative evidence

1. **Severe Regime Breakdown Post-September 2024 (`source-reported`):** As documented in Table 1, the strategy experienced an out-of-sample regime degradation post-September 2024, yielding $-13\%$ cumulative return and a $-17\%$ maximum drawdown while trading frequency increased to $1,117\text{ trades/month}$.
2. **Turnover Friction Asphyxiation:** Generating $\sim 1,000$ trades per month without explicit cost-aware filtering or minimum holding period creates extreme vulnerability to transaction costs. Even a tiny round-trip friction of 2–3 bps will turn the $+214\%$ gross gain into substantial negative net returns.
3. **Fixed Hyperparameter Rigidity:** The Kalman parameters ($q=0.01, r=0.1$), threshold ($\theta = 0.06$), derivative scaling ($2$), and derivative span ($4$) are static and uncalibrated, offering no adaptive response to macro volatility clustering.

## Falsification plan

To falsify the claim that the forward-oriented causal operator captures genuine structural phase-lead alpha, the following operational tests must be executed:

### Test 1: Friction & Slippage Threshold Hurdle (`research-proposed`)
- **Hypothesis:** The phase-lead observable produces net positive economic value beyond bid-ask bounce and broker fees.
- **Protocol:** Backtest on tick-level or 1-minute EURUSDT data across the 2023–2026 period under realistic taker fees ($2\text{ bps}$ each way) and $0.5\text{ bps}$ slippage.
- **Decision Rule (`research-defined falsification threshold`):** If the annualized Net Sharpe Ratio drops below $0.0$ or Net Cumulative Return is negative across the full 2023–2026 window, the strategy is falsified as an executable standalone trading system.

### Test 2: Derivative Operator Ablation Test (`research-proposed`)
- **Hypothesis:** The phase-lead derivative term $2 c_2(t) \widetilde{\partial_t \mathscr{F}_0}(t)$ contributes statistically significant incremental information over pure $\mathscr{F}_0(t)$.
- **Protocol:** Run parallel backtests of (a) full $\mathscr{F}(t)$, (b) pure $\mathscr{F}_0(t)$ with optimal threshold, and (c) phase-shuffled derivative $\widetilde{\partial_t \mathscr{F}_0}(t)$.
- **Decision Rule (`research-defined falsification threshold`):** If the Information Ratio of $\mathscr{F}(t)$ relative to $\mathscr{F}_0(t)$ is less than $0.30$ or two-sided t-statistic on return differentials has $p > 0.05$, reject the forward-operator hypothesis.

### Test 3: Causal Centering vs. Static Normalization Audit (`research-proposed`)
- **Hypothesis:** The causal median operator prevents look-ahead bias without inducing severe lag distortions.
- **Protocol:** Compare causal expanding median against full-sample static median and rolling window medians ($W \in \{720, 1440, 2880\}\text{ minutes}$).
- **Decision Rule (`research-defined falsification threshold`):** If full-sample static median produces $> 200\%$ higher Sharpe than causal median, confirm that past published results were inflated by look-ahead information leakage.

### Test 4: Cross-Asset Portability Stress Test (`research-proposed`)
- **Hypothesis:** The mathematical mechanism (Kalman-filtered multi-indicator aggregation with phase-lead derivative) generalizes beyond EURUSDT.
- **Protocol:** Evaluate on BTCUSDT, ETHUSDT, and SOLUSDT 1-minute data over 2023–2026.
- **Decision Rule (`research-defined falsification threshold`):** If the strategy experiences $> 35\%$ drawdown or negative gross Sharpe on major crypto assets, reject broad cross-asset validity and classify as an FX-specific artifact.

## Crypto portability

**Portability Classification:** `Adapted / Unproven`

While the test instrument is `EURUSDT` (which trades on cryptocurrency spot and perpetual venues such as Binance, Bybit, and OKX), the primary source filtered data specifically to match **traditional Forex trading hours** (removing weekends and off-hour periods). Porting this framework to native 24/7 cryptocurrency markets involves material structural adaptations:

1. **24/7 Continuous Trading:** Unlike Forex markets, crypto spot and perpetual markets never close on weekends. Removing Saturdays and Sundays would introduce artificial bar gaps and discard high-volatility weekend flow. The causal median and Kalman filter must run continuously without weekend session masking (`research-proposed`).
2. **Volatilities and Parameter Scaling:** EURUSDT is a low-volatility FX peg/cross with annualized volatility typically between $6\%$ and $9\%$. Crypto majors (BTCUSDT, ETHUSDT) exhibit annualized volatilities of $50\% - 85\%$. Consequently:
   - The threshold $\theta = 0.06$ is tightly scaled to EURUSDT signal amplitudes. For BTC/ETH, $\theta$ must be recalibrated or normalized by rolling ATR (`research-proposed`).
   - The indicator scaling constants $\alpha_k$ (especially $\alpha_{\text{MACD}} = 3333.33$) depend heavily on the absolute price scale and volatility of the underlying asset. For BTC at \$60,000–\$100,000, raw MACD differences are orders of magnitude larger, requiring percentage or return-based MACD normalization (`research-proposed`).
3. **Funding Rate Friction in Perpetuals:** If traded on perpetual futures, long positions held during positive funding regimes will incur funding drag every 8 hours, impacting net return accumulation.
4. **Microstructure & MEV:** In high-frequency 1-minute decentralized or centralized order books, toxic flow, front-running, and adverse selection at signal zero-crossings can degrade fill rates.

## Limitations

1. **Zero Transaction Costs in Baseline:** The primary paper assumes zero fees, zero slippage, and zero spread. Given $> 1,000$ trades per month, the gross return of $+214\%$ is completely eroded under standard retail or institutional taker fee schedules.
2. **Regime Fragility:** Demonstrates severe breakdown post-September 2024 ($-13\%$ return, $-17\%$ drawdown), proving that a static linear aggregation cannot adapt to structural market shifts without active regime conditioning or dynamic thresholding.
3. **Arbitrary Indicator Weights:** Scaling coefficients $\alpha_{\text{MFI}} = 0.005, \alpha_{\text{RSI}} = 0.010, \alpha_{\text{BB}\%} = 0.33333, \alpha_{\text{MACD}} = 3333.33$ are heuristic fixed constants rather than mathematically derived optimal weights.
4. **Long-Only Binary State Machine:** The source evaluates only $p_t \in \{0, 1\}$ (invested vs. flat). It omits short positions, leaving the strategy unhedged against macro downtrends except by going flat.
5. **Kalman Hyperparameter Sensitivity:** The author explicitly notes that the choice of $q=0.01$ and $r=0.1$ was fixed without systematic sensitivity analysis; misspecified noise covariances may cause oversmoothing or excessive lag.

## Implementation status

- `not-implemented` in internal quantitative repository (`nautilus-quant-system` / `pybroker`).
- This record represents an upstream research capture for ChatGPT Research Intake Review and Hermes Wiki Brain ingestion. No NautilusTrader actor, PyBroker script, or execution harness has been generated or authorized.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`
- **Boundary Policy:** This record is cataloged strictly for exploratory signal synthesis, causal filter design benchmarking, and phase-lead operator research. It does not authorize paper trading, Binance testnet deployment, or live capital allocation.

## Related Wiki records

- `[[quant/crypto-time-dependent-weighted-directed-network-granger-causality-2026-09-01]]`
- `[[quant/deepm-regime-robust-macro-graph-causal-sieve-evar-2026-09-03]]`
- `[[quant/crypto-hourly-bitcoin-walk-forward-cost-aware-execution-2026-09-01]]`
- `[[quant/microstructure-mean-reversion-optimal-symmetric-band-waiting-option-2026-09-02]]`

## Sources

- **Primary Paper:** Lucas A. Souza, *"Forward-Oriented Causal Observables for Non-Stationary Financial Markets"*, arXiv preprint `arXiv:2512.24621v1 [q-fin.CP]`, December 31, 2025. [https://arxiv.org/abs/2512.24621](https://arxiv.org/abs/2512.24621).
- **Primary Source Code & LaTeX Files:** Unpacked arXiv package `arXiv:2512.24621` (`main.tex`, `indicators.pdf`, `pnl_F_vs_bnh.pdf`, `cumulative_returns_target_horizons.pdf`, `bib.bib`).
- **Foundational Citations in Source:**
  - R. E. Kalman, *"A new approach to linear filtering and prediction problems"*, Transactions of the ASME–Journal of Basic Engineering 82, pp. 35–45 (1960). [https://doi.org/10.1115/1.3662552](https://doi.org/10.1115/1.3662552).
  - J. W. Wilder, *"New concepts in technical trading systems"*, Trend Research (1978).
  - G. Appel, *"The moving average convergence–divergence trading method: advanced techniques for operating in bull and bear markets"*, Financial Publishing Company (1979).
  - J. J. Murphy, *"Technical analysis of the financial markets"*, New York Institute of Finance (1999).
