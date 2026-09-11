---
schema: strategy-research-record-v1
title: "Explainable Deep Learning Price-Trade Dynamics — SHAP-Derived Nonlinear Microstructure Model (Naviglio & Lillo 2026)"
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-microstructure
  - price-trade-dynamics
  - order-flow
  - high-frequency
  - shapley-values
  - deep-learning
  - non-linear-parametric
status: research-only
confidence: high
source_as_of: 2026-09-11
sources:
  - "arXiv:2609.06085v1 [q-fin.TR], submitted 5 September 2026 — Manuel Naviglio and Fabrizio Lillo, 'Explainable Deep Learning for Price-Trade Dynamics: From Black-Box Forecasts to Effective Parametric Models'"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Explainable Deep Learning Price-Trade Dynamics — SHAP-Derived Nonlinear Microstructure Model (Naviglio & Lillo 2026)

## Provenance

- **arXiv:** [arXiv:2609.06085v1](https://arxiv.org/abs/2609.06085) [q-fin.TR] (cross-listed: cs.AI, physics.data-an)
- **Authors:** Manuel Naviglio and Fabrizio Lillo
- **Title:** "Explainable Deep Learning for Price-Trade Dynamics: From Black-Box Forecasts to Effective Parametric Models"
- **Submitted:** 5 September 2026 (UTC: 2026-09-05T13:25:40Z)
- **Primary source verified:** Yes — full text, equations, tables (Tables 1–6), figures, and appendices inspected directly from primary source text.
- **Dataset / Venue:** LOBSTER Level 3 limit order book data from NASDAQ.
- **Universe:** 10 US equities spanning two distinct microstructure tick regimes:
  - Large-tick (spread ~ 1 tick): BAC (1.16), INTC (1.16), CSCO (1.18), CMCSA (1.19), PFE (1.20).
  - Small-tick (spread > 1 tick): AMZN (1.70), AAPL (1.82), GILD (2.03), TSLA (3.69), NVDA (6.27).
- **Sample period:** June 2024.
- **Data partition:** First 50% chronological split for training; remaining 50% reserved for out-of-sample evaluation.

## Economic mechanism

### Source-reported

In high-frequency market microstructure, returns and order flow interact through nonlinear, state-dependent mechanisms that traditional linear Vector Autoregressive (VAR) models (such as Hasbrouck 1991) fail to fully capture. While deep neural networks (DNN) can approximate arbitrary nonlinear dependencies and improve forecasting accuracy, their black-box nature obscures the underlying financial mechanics.

Naviglio and Lillo use a deep feed-forward neural network (3 hidden dense layers with 64, 64, and 32 neurons, $\tanh$ activations, trained via Adam on MSE loss) on event-time midpoint price returns $r_t$ and signed trading volume $v_t$. Using SHAP (DeepExplainer) Shapley value decomposition, they identify that:
1. **Concentration of predictive importance:** Explanatory power is overwhelmingly concentrated at the most recent lag ($\ell = 1$), with power decaying rapidly toward zero for higher lags.
2. **Signed volume response:** Lagged signed volume $v_{t-1}$ produces a sign-preserving, saturating contribution on both predicted return and predicted volume, modeled as an odd saturating function $\Phi_v^a(v) = A_v^a \tanh(\beta_v^a v)$. This captures nonlinear price impact in the return equation and order-flow persistence in the volume equation.
3. **Return state as an interaction switch:** Lagged returns $r_{t-1}$ act as a state variable governing order-flow transmission:
   - When the previous trade does not move the price ($r_{t-1} = 0$), the quote has not yet absorbed the order flow; the model reinforces the directional signal of $v_{t-1}$ (continuation).
   - When a price change occurs ($|r_{t-1}| > 0$), price adjustment attenuates or reverses the directional order-flow signal, captured by $\Phi_r^a(r, v) = \operatorname{sign}(v_{t-1}) [A_r^a - B_r^a \tanh(\lambda_r^a |r_{t-1}|)]$.
   - Under $B_r^a > A_r^a > 0$, there exists a finite critical threshold $|r|^\star = \frac{1}{\lambda_r^a} \operatorname{arctanh}(A_r^a / B_r^a)$ above which the response reverses direction.

Building on these insights, the authors derive a parsimonious SHAP-inspired nonlinear parametric model:
- **One-lag reduced parametric model:**
  $$\begin{aligned}
  r_t &= \alpha_r + A_v^r \tanh(\beta_v^r v_{t-1}) + \operatorname{sign}(v_{t-1}) \left[ A_r^r - B_r^r \tanh(\lambda_r^r |r_{t-1}|) \right] + u_t^r \\
  v_t &= \alpha_v + A_v^v \tanh(\beta_v^v v_{t-1}) + \operatorname{sign}(v_{t-1}) \left[ A_r^v - B_r^v \tanh(\lambda_r^v |r_{t-1}|) \right] + u_t^v
  \end{aligned}$$
- **Multi-lag parametric model with geometric memory decay:**
  $$\begin{aligned}
  r_t &= \alpha_r + A_{rv} \sum_{\ell=1}^p \rho_{rv}^{\ell-1} \tanh(\beta_{rv} v_{t-\ell}) + \sum_{\ell=1}^p \rho_{rr}^{\ell-1} \operatorname{sign}(v_{t-\ell}) \left[ A_{rr} - B_{rr} \tanh(\lambda_{rr} |r_{t-\ell}|) \right] + \varepsilon_t^r \\
  v_t &= \alpha_v + A_{vv} \sum_{\ell=1}^p \rho_{vv}^{\ell-1} \tanh(\beta_{vv} v_{t-\ell}) + \sum_{\ell=1}^p \rho_{vr}^{\ell-1} \operatorname{sign}(v_{t-\ell}) \left[ A_{vr} - B_{vr} \tanh(\lambda_{vr} |r_{t-\ell}|) \right] + \varepsilon_t^v
  \end{aligned}$$
  where $0 < \rho < 1$, sharing nonlinear shape parameters across lags to avoid overparameterization.
- **Residual contemporaneous price impact:** Removing predictable lagged components leaves residuals $u_t^r, u_t^v$. A triangular structural decomposition $u_t^v = \epsilon_t^v$, $u_t^r = \phi(u_t^v) + \epsilon_t^r$ isolates the instantaneous nonlinear impact function $\phi(\cdot)$, which explains 16%–18% of the residual return variance ($R_\phi^2$).

### Research interpretation

The hypothesized alpha mechanism is **order-flow state-dependent quote continuation and bounce**:
1. When aggressive orders arrive without displacing the bid/ask quote (zero midprice return), the order-book queue depth absorbs the trade without repricing. The remaining directional pressure carries into the subsequent trade, creating high-frequency price continuation drift.
2. When aggressive orders sweep liquidity and force a quote step ($|r| > |r|^\star$), the immediate order-flow pressure is exhausted, and liquidity replenishment on the opposite side triggers bid-ask bounce or adverse selection exhaustion, producing predictable short-horizon mean reversion.
3. This explainability-driven formulation translates black-box neural-network representations into a closed-form parametric signal with 6 to 8 parameters, achieving equal or superior out-of-sample predictability compared to a 20-lag deep neural network while maintaining interpretability and mathematical stability.

## Signal

### Formation timestamp

- Observations are defined in **event time**, recorded immediately upon the execution of each visible limit order.
- In accordance with the Transient Impact Model (TIM) convention (Bouchaud et al. 2004), the reference price is defined as the mid-price of the limit order book immediately preceding the execution of a visible order.
- Lagged forecast $\widehat{r}_t^{\,\mathrm{lagged}} = f_r(\mathcal{X}_t)$ is formed using information strictly available up to event $t-1$.

### Lookback window

- **One-lag reduced model:** $p = 1$ event lag ($(r_{t-1}, v_{t-1})$).
- **Multi-lag model:** $p = 20$ event lags, with geometrically decaying weights $\rho^{\ell-1}$.
- **Benchmark VAR and DNN:** $p = 20$ event lags.

### Entry logic (Research-proposed)

The primary source constructs an econometric conditional expectation model $\widehat{r}_t$. The operational trading rules below are `research-proposed`:
- Compute one-step-ahead expected return $\widehat{r}_t^{\,\mathrm{lagged}}$ from the calibrated parametric equation.
- **Long entry:** Execute buy order when $\widehat{r}_t^{\,\mathrm{lagged}} > +\theta_r$ (`research-proposed threshold`, e.g., $\theta_r = 0.5 \times \text{tick size}$).
- **Short entry:** Execute sell order when $\widehat{r}_t^{\,\mathrm{lagged}} < -\theta_r$ (`research-proposed threshold`, e.g., $\theta_r = 0.5 \times \text{tick size}$).
- **Regime conditioning:**
  - If $r_{t-1} = 0$: Trade in the direction of $v_{t-1}$ (continuation regime).
  - If $|r_{t-1}| > |r|^\star = \frac{1}{\lambda_r^r} \operatorname{arctanh}(A_r^r / B_r^r)$: Trade in the direction opposite to $\operatorname{sign}(v_{t-1})$ (exhaustion / mean-reversion regime).

### Exit logic (Research-proposed)

- **Holding horizon:** Single-event holding period ($t+1$) or until the expected return $\widehat{r}_{t+k}$ falls below the cost threshold (`research-proposed`).
- **Stop-loss / Time-exit:** Exit immediately if midprice moves adverse by more than $1.5 \times \text{tick size}$ or if no execution event occurs within 30 seconds (`research-proposed`).

### Parameters

- Return equation parameters: $\alpha_r$, $A_v^r > 0$, $\beta_v^r > 0$, $A_r^r > 0$, $B_r^r > A_r^r$, $\lambda_r^r > 0$, $\rho_{rv} \in (0, 1)$, $\rho_{rr} \in (0, 1)$.
- Volume equation parameters: $\alpha_v$, $A_v^v > 0$, $\beta_v^v > 0$, $A_r^v > 0$, $B_r^v > A_r^v$, $\lambda_r^v > 0$, $\rho_{vv} \in (0, 1)$, $\rho_{vr} \in (0, 1)$.
- Parameter constraints: Positivity enforced by reparametrization; $B_r^a > A_r^a$ enforced via $B_r^a = A_r^a + \operatorname{softplus}(\delta_r^a)$.
- Calibration: Nonlinear Least Squares (NLS) minimizing MSE over the training sample.

### Position sizing (Research-proposed)

- Fixed lot sizing scaled inversely by instantaneous bid-ask spread: $\text{Size} \propto \frac{1}{\text{Spread}_t}$ (`research-proposed`).

### Underspecified elements

- The source paper establishes econometric predictive power ($R^2$) on NASDAQ LOBSTER data, but omits an operational order execution algorithm, fee structure, order routing logic, and position sizing. These are labeled `research-proposed`.

## Required data

- **Instrument:** US cash equities (ordinary common stocks).
- **Universe:** 10 NASDAQ-listed stocks (BAC, INTC, CSCO, CMCSA, PFE, AMZN, AAPL, GILD, TSLA, NVDA).
- **Venue:** NASDAQ.
- **Market type:** Spot cash equity market (continuous limit order book).
- **Timeframe:** Event time (per visible order execution).
- **Fields:**
  - Event type ("Execution of a visible limit order", hidden orders excluded).
  - High-precision timestamp (nanosecond/microsecond).
  - LOB mid-price immediately before visible order execution: $P_t^{\mathrm{mid}} = \frac{P_{t}^{\mathrm{ask}} + P_{t}^{\mathrm{bid}}}{2}$.
  - Midpoint return: $r_t = \frac{P_t^{\mathrm{mid}} - P_{t-1}^{\mathrm{mid}}}{\Delta_{\mathrm{tick}}}$ (or log return).
  - Executed order size (shares).
  - Trade aggressor sign: $q_t \in \{+1, -1\}$ ($+1$ for buyer-initiated, $-1$ for seller-initiated).
  - Signed trading volume: $v_t = q_t \times \text{Volume}_t$.
- **Filtering / Outlier treatment:**
  - Same-timestamp, same-sign order executions are aggregated.
  - Exclude first 30 minutes (09:30–10:00 ET) and last 30 minutes (15:30–16:00 ET) of trading to avoid auction distortions.
  - Apply quantile filter removing observations outside $[0.005, 0.995]$ quantile range.
  - Standardize/normalize training inputs.

## Execution assumptions

- **Signal-to-order timing:** Signal evaluated at trade event $t-1$; executed at trade event $t$ (`research-proposed`).
- **Order type:** Passive limit order at the near touch or aggressive taker order when expected edge exceeds the half-spread plus taker fee (`research-proposed`).
- **Fees & Slippage:** Omitted in source paper. Source evaluates out-of-sample MSE $R^2$. Realistic US equity maker rebates (~10–20 mils/share) or taker fees (~30 mils/share) must be applied (`research-proposed`).
- **Spread:** Documented in source Table 1:
  - Large-tick stocks: 1.16 to 1.20 ticks (BAC 1.16, INTC 1.16, CSCO 1.18, CMCSA 1.19, PFE 1.20).
  - Small-tick stocks: 1.70 to 6.27 ticks (AMZN 1.70, AAPL 1.82, GILD 2.03, TSLA 3.69, NVDA 6.27).
- **Latency / Infrastructure:** Ultra-high frequency execution requirement. In event time, trade-to-order turnaround must occur within sub-millisecond to millisecond latencies (`research-proposed`).

## Evidence

### Source-reported

1. **Out-of-sample $R^2$ for Return Forecasting ($R^2_{\mathrm{out}}(r)$):**
   - Source: Naviglio & Lillo (2026), Table 2, Table 4, and Table 5.
   - **Large-tick stocks (June 2024 out-of-sample test split):**
     - **BAC:** Linear VAR ($p=20$) = 0.0494; DNN ($p=20$) = 0.0591; Reduced 1-lag = 0.0934; Multi-lag ($p=20$) = 0.0945.
     - **INTC:** Linear VAR ($p=20$) = 0.0814; DNN ($p=20$) = 0.1217; Reduced 1-lag = 0.1065; Multi-lag ($p=20$) = 0.1073.
     - **CSCO:** Linear VAR ($p=20$) = 0.0764; DNN ($p=20$) = 0.0982; Reduced 1-lag = 0.1156; Multi-lag ($p=20$) = 0.1168.
     - **CMCSA:** Linear VAR ($p=20$) = 0.0604; DNN ($p=20$) = 0.0859; Reduced 1-lag = 0.1020; Multi-lag ($p=20$) = 0.1031.
     - **PFE:** Linear VAR ($p=20$) = 0.0356; DNN ($p=20$) = 0.0367; Reduced 1-lag = 0.0845; Multi-lag ($p=20$) = 0.0855.
   - **Small-tick stocks (June 2024 out-of-sample test split):**
     - **AMZN:** Linear VAR ($p=20$) = 0.0246; DNN ($p=20$) = 0.0341; Reduced 1-lag = 0.0528; Multi-lag ($p=20$) = 0.0529.
     - **AAPL:** Linear VAR ($p=20$) = 0.0643; DNN ($p=20$) = 0.0951; Reduced 1-lag = 0.0858; Multi-lag ($p=20$) = 0.0866.
     - **GILD:** Linear VAR ($p=20$) = 0.0499; DNN ($p=20$) = 0.0429; Reduced 1-lag = 0.0723; Multi-lag ($p=20$) = 0.0731.
     - **TSLA:** Linear VAR ($p=20$) = 0.0433; DNN ($p=20$) = 0.0906; Reduced 1-lag = 0.0826; Multi-lag ($p=20$) = 0.0826.
     - **NVDA:** Linear VAR ($p=20$) = 0.0166; DNN ($p=20$) = 0.0454; Reduced 1-lag = 0.0498; Multi-lag ($p=20$) = 0.0498.

2. **Out-of-sample $R^2$ for Signed Volume Forecasting ($R^2_{\mathrm{out}}(v)$):**
   - Source: Naviglio & Lillo (2026), Table 2, Table 4, and Table 5.
   - **Large-tick stocks:**
     - **BAC:** VAR = 0.0299; DNN = 0.0215; Reduced 1-lag = 0.0623; Multi-lag = 0.0623.
     - **INTC:** VAR = 0.0198; DNN = 0.0288; Reduced 1-lag = 0.0644; Multi-lag = 0.0651.
     - **CSCO:** VAR = 0.0328; DNN = 0.0273; Reduced 1-lag = 0.0735; Multi-lag = 0.0745.
     - **CMCSA:** VAR = 0.0350; DNN = 0.0486; Reduced 1-lag = 0.0820; Multi-lag = 0.0828.
     - **PFE:** VAR = 0.0183; DNN = 0.0091; Reduced 1-lag = 0.0478; Multi-lag = 0.0479.
   - **Small-tick stocks:**
     - **AMZN:** VAR = 0.0685; DNN = 0.0705; Reduced 1-lag = 0.0892; Multi-lag = 0.1047.
     - **AAPL:** VAR = 0.1147; DNN = 0.1372; Reduced 1-lag = 0.1421; Multi-lag = 0.1552.
     - **GILD:** VAR = 0.1055; DNN = 0.1173; Reduced 1-lag = 0.1165; Multi-lag = 0.1248.
     - **TSLA:** VAR = 0.1115; DNN = 0.1475; Reduced 1-lag = 0.1475; Multi-lag = 0.1589.
     - **NVDA:** VAR = 0.0872; DNN = 0.1068; Reduced 1-lag = 0.0967; Multi-lag = 0.1141.

3. **Contemporaneous Residual Structural Shock Decomposition ($R_\phi^2$, Table 3):**
   - Instantaneous order-flow innovation explains 16%–18% of the residual return variance:
     - Large-tick average $R_\phi^2 = 0.162$ (BAC 0.163, CMCSA 0.117, CSCO 0.148, INTC 0.178, PFE 0.205).
     - Small-tick average $R_\phi^2 = 0.179$ (AAPL 0.143, AMZN 0.266, GILD 0.222, NVDA 0.146, TSLA 0.116).

4. **Residual Linear Correlation Reduction (Table 6):**
   - Pearson correlation between $u_t^v$ and $u_t^r$ falls from 0.289 (LT avg) and 0.34+ (ST avg) before structural projection to 0.0113 (LT avg) and 0.009–0.012 (ST avg) after projection, demonstrating that the structural function $\phi$ effectively purges contemporaneous directional co-movement.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The paper reports purely statistical predictive performance (MSE and $R^2$), without a trading simulation, execution fill model, or transaction-cost adjusted PnL.
- On small-tick stocks with wider bid-ask spreads (AAPL and TSLA), the 20-lag DNN maintains a moderate $R^2$ advantage over the 1-lag parametric model (AAPL: 0.0951 vs 0.0858; TSLA: 0.0906 vs 0.0826), indicating unmodeled higher-order nonlinearities or asymmetric response curves.
- The model enforces symmetric responses with respect to $|r_{t-1}|$; the authors note that empirical order book profiles exhibit mild asymmetries between up-moves and down-moves that are neglected by the baseline formulation.

## Falsification plan

1. **Transaction cost hurdle test:** Simulate event-time trading with realistic maker rebate and taker fee tiers. `Research-defined falsification threshold`: if net realized Sharpe ratio $< 0.5$ or average net gain per round-trip trade $< 0.10 \times \text{Spread}$, the strategy fails as an implementable alpha.
2. **Execution latency degradation test:** Inject artificial execution delay ($1\text{ ms}$, $5\text{ ms}$, $10\text{ ms}$, $50\text{ ms}$) between signal generation and order fill. `Research-defined falsification threshold`: if return predictability $R^2$ drops by more than $60\%$ at $5\text{ ms}$ latency, the strategy is falsified for non-colocated execution.
3. **Threshold sign inversion test:** Calibrate $B_r^r$ and $A_r^r$ across out-of-sample subperiods. `Research-defined falsification threshold`: if estimated $B_r^r \le A_r^r$ (eliminating the finite critical threshold $|r|^\star$ and the reversal mechanism), the structural hypothesis is falsified.
4. **Subperiod & volatility stress test:** Split evaluation into calm vs high-volatility trading days (e.g., macro announcement days). `Research-defined falsification threshold`: out-of-sample $R^2 < 0.0$ in high-volatility regimes.

## Crypto portability

**Adapted / unproven** — the primary paper evaluates exclusively NASDAQ equity data and does NOT study cryptocurrency markets.

Crypto microstructure adaptations:
- **Tick size regimes:** Major perpetual futures (e.g., BTCUSDT, ETHUSDT on Binance) operate in an ultra-fine tick regime where spread is almost permanently 1 tick (large-tick regime in the paper's taxonomy), making the large-tick parametric specification ($p=1$ reduced model) directly applicable. Lower-liquidity altcoins display wide multi-tick spreads resembling small-tick equities.
- **Continuous 24/7 trading:** Crypto markets lack 09:30/16:00 auction boundaries; the 30-minute opening/closing data exclusion is not applicable, but funding-fee settlement hours (every 8 hours or 1 hour) create periodic volume spikes.
- **Cross-venue fragmentation:** In crypto, order flow is split across Binance, Bybit, OKX, and Coinbase. Single-venue LOB modeling risks missing toxic flow originating on external venues.
- **Ported research hypothesis:** Fitting the SHAP-inspired parametric model to Binance BTCUSDT trade-by-trade feeds will reveal whether unmoving quote trades predict continuation and large quote sweeps predict mean reversion. This remains an unproven research hypothesis until empirical calibration is conducted.

## Limitations

- **No transaction cost backtest:** Source demonstrates high $R^2$ out-of-sample, but does not verify whether the edge survives the bid-ask spread and trading fees.
- **Event-time latency requirement:** Operating at the transaction level requires colocation and sub-millisecond execution capabilities.
- **Single-venue NASDAQ LOBSTER data:** The empirical study covers one month (June 2024) on NASDAQ visible orders only.
- **Symmetry assumption:** The model assumes identical response for positive and negative price moves ($|r_{t-1}|$).

## Implementation status

Not implemented. Captured strictly as a normalized research record. No code in PyBroker, NautilusTrader, paper trading, testnet, or live environments has been created or modified.

## Adoption boundary

Research-only. Not approved for implementation, paper trading, testnet, or live execution. This record serves as a theoretical and empirical microstructure reference for Loop A hypothesis generation.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]`
- `quant/duration-aware-bocpd-lognormal-order-flow-regime-2026-09-11.md`
- `quant/deep-rl-market-making-regime-switching-bocpd-scenario-bandit-2026-09-11.md`
- `quant/clusterlob-order-flow-imbalance-trader-behavior-clustering-2026-09-03.md`
- `quant/edgeflow-composite-lob-microstructure-alpha-binance-spot-2026-09-09.md`

## Sources

1. Naviglio, Manuel, and Fabrizio Lillo. "Explainable Deep Learning for Price-Trade Dynamics: From Black-Box Forecasts to Effective Parametric Models." arXiv preprint arXiv:2609.06085v1 [q-fin.TR], submitted 5 September 2026. https://arxiv.org/abs/2609.06085
2. Hasbrouck, Joel. "Measuring the Information Content of Stock Trades." *Journal of Finance* 46, no. 1 (1991): 179–207.
3. Bouchaud, Jean-Philippe, Yuval Gefen, Marc Potters, and Matthieu Wyart. "Fluctuations and Response in Financial Markets: The Subtle Nature of ‘Random’ Price Changes." *Quantitative Finance* 4, no. 2 (2004): 176–190.
4. Lundberg, Scott M., and Su-In Lee. "A Unified Approach to Interpreting Model Predictions." *Advances in Neural Information Processing Systems (NeurIPS)* 30 (2017): 4765–4774.
