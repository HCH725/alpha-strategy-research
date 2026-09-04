---
schema: strategy-research-record-v1
title: "Machine Learning Enhanced Multi-Factor Quantitative Trading: A Cross-Sectional Portfolio Optimization Approach with Bias Correction"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional-equity
  - machine-learning
  - china-a-shares
  - bias-correction
  - mask-first
  - upstream-contamination
  - portfolio-optimization
  - markowitz-ledoit-wolf
  - adjusted-mse
  - data-augmentation
status: research-only
confidence: high
source_as_of: 2026-09-03
sources:
  - "https://arxiv.org/abs/2507.07107"
  - "https://doi.org/10.48550/arXiv.2507.07107"
  - "https://github.com/initial-d/ml-quant-trading"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Machine Learning Enhanced Multi-Factor Quantitative Trading: A Cross-Sectional Portfolio Optimization Approach with Bias Correction

## Provenance

- **Author:** Yimin Du (University of Science and Technology of China / independent researcher; contact: `sa613403@mail.ustc.edu.cn`, GitHub: `initial-d`)
- **arXiv ID:** `arXiv:2507.07107v2 [q-fin.PM, cs.CE]`
- **Title:** *Machine Learning Enhanced Multi-Factor Quantitative Trading: A Cross-Sectional Portfolio Optimization Approach with Bias Correction*
- **Primary DOI:** [10.48550/arXiv.2507.07107](https://doi.org/10.48550/arXiv.2507.07107)
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Primary Code Implementation:** [https://github.com/initial-d/ml-quant-trading](https://github.com/initial-d/ml-quant-trading)
- **Canonical Implementation Commit:** `c78e27bad025e8317a08d330d2f49b529d85de17` (as-of 2026-09-03T08:33:44Z; MIT License)
- **Key Code Modules Verified:**
  - `src/mlquant/features/bias.py` (tradability mask and return proxy)
  - `src/mlquant/features/tensor_factors.py` (18 GPU-vectorized mask-aware rolling primitives)
  - `src/mlquant/models/losses.py` (`AdjMSELoss`, $\gamma=0.1$, 11:1 wrong-sign penalty ratio)
  - `src/mlquant/models/nets.py` (Factor-axis Transformer and MLP architectures)
  - `src/mlquant/training/augment.py` (Block-bootstrap 21-day Geometric Brownian Motion augmentation)
  - `src/mlquant/portfolio/markowitz.py` (Markowitz-Ledoit-Wolf QP with warm-start caching)
  - `src/mlquant/backtest/engine.py` (Lagged-weight cost-aware vector backtest engine)
  - `configs/paper.yaml` (Authoritative experiment configuration)

**Primary Source Verification:** The primary preprint full text (`https://arxiv.org/html/2507.07107v2`), paper configuration (`configs/paper.yaml`), and repository code were retrieved and examined directly. All mathematical formulations, parameter values, baseline comparisons, ablation deltas, and empirical performance metrics are traced directly to the primary text and source repository without intermediate secondary summarization.

**Repository Deduplication Check:** Prior to committing this record, full-text repository searches confirmed that neither `arXiv:2507.07107`, author Yimin Du, the repository `initial-d/ml-quant-trading`, nor the concepts "upstream contamination" and "AdjMSE" exist in any previous strategy record or in `coverage_manifest.csv`. While `china-ashare-xgboost-treeshap-behavioral-factor-decomposition-2026-09-04.md` explores China A-share equity return predictability using TreeSHAP attribution on monthly baostock data (Han et al., `arXiv:2606.12843`), the present record targets a fundamentally distinct problem and strategy architecture: daily rolling-window microstructure bias correction (mask-first propagation), a 213-factor PyTorch tensor pipeline, an asymmetric sign-weighted loss function, block-bootstrap data augmentation, and regularized quadratic portfolio optimization.

## Economic mechanism

### Source-reported

In Chinese A-share equity markets, regulatory daily price-move limits ($\pm 10\%$ on main boards, $\pm 20\%$ on STAR and ChiNext markets) create institutional fill-gap friction:
1. **The Upstream Contamination Problem:** When a stock hits its upper price limit, unmatched buy orders accumulate in queue and no new buy orders can execute; recorded closing prices do not represent tradeable equilibrium values. Standard quantitative research workflows apply post-hoc row deletion (dropping limit days after factor calculation). However, rolling-window operators (e.g., rolling means, moving correlations, cross-sectional ranks, and EWMA) ingest the non-executable price before row filtering occurs. That contaminated value silently propagates through all downstream aggregates over the entire lookback window $w$ (days $t$ through $t + w - 1$).
2. **The IC-Sharpe Paradox:** Ignoring upstream contamination causes models to learn spurious predictability: limit-up stocks mechanically exhibit high returns in cross-sectional training data, which inflates apparent Information Coefficient (IC) by $+18\%$ ($0.049 \to 0.058$). However, because these stocks cannot actually be purchased during live execution, the strategy's realized Sharpe ratio collapses by $-0.44$ points ($2.05 \to 1.61$ on synthetic data), and maximum drawdown doubles ($11.4\% \to 22.8\%$ on real data).
3. **Asymmetric Economic Loss (Direction vs. Magnitude):** Standard Mean Squared Error (MSE) penalizes all estimation residuals equally. However, downstream portfolio managers incur severe drawdowns from directional errors (predicting $+2\%$ when the true return is $-1\%$, causing capital loss) compared to magnitude sizing errors (predicting $+2\%$ when the true return is $+4\%$, merely under-allocating).
4. **Covariance Conditioning and Small Sample Sizes:** Historical equity return series in China cover relatively short empirical periods ($\sim 2,500$ daily bars) with periodic structural regime shifts. Sample covariance matrices for large universes ($N \ge 1,000$ stocks) over standard trailing windows ($T_{\text{lb}} = 120$ days) are severely ill-conditioned ($N \gg T_{\text{lb}}$). Regularization via Ledoit-Wolf analytical shrinkage stabilizes portfolio weights and suppresses turnover-induced transaction cost drag.

### Research interpretation

The strategy addresses a structural data-engineering and portfolio-construction alpha wedge:
- **Execution-Conditioned Feature Formation:** Alpha cannot be separated from execution feasibility. When rolling features are computed across non-clearing prices, factor scores reflect phantom liquidity rather than economic supply/demand imbalances. Enforcing a strict mask-first contract at data ingestion guarantees that no factor contains information that could not have been converted into an executable position.
- **Direction-Dominant Utility Alignment:** By penalizing sign errors 11 times more heavily than magnitude errors ($\gamma = 0.1$), the predictive model shifts parameter focus toward correct binary classification of cross-sectional return signs, directly matching the convex utility curve of long-only portfolio construction where shorting is legally restricted or prohibitively expensive.
- **Factor-Axis Interaction Extraction:** Rather than using time-axis attention, tokenizing factors along the feature axis allows a Transformer architecture to capture nonlinear conditional interactions (e.g., short-term mean-reversion Alpha012 firing effectively in low-volatility regimes but failing in high-volatility liquidity shocks).

## Signal

The system processes a 213-dimensional factor tensor through a deep learning model to output continuous expected next-day return predictions $\hat{\mu} \in \mathbb{R}^N$, which are subsequently fed into a constrained quadratic optimizer.

### Factor Library Composition (213 Factors)

1. **Alpha101 Curated Subset (9 factors):** [source-reported]
   - Re-implemented directly with mask-aware tensor primitives (avoiding degraded or co-linear formulas):
     - `Alpha001`: Momentum rank
     - `Alpha002`: Volume-intraday price correlation
     - `Alpha003` & `Alpha006`: Open-volume divergence
     - `Alpha004`: Low-rank reversion
     - `Alpha007`: Mean-deviation
     - `Alpha012`: Volume-change reversal
     - `Alpha053`: Close-location change
     - `Alpha101`: Intraday range position
2. **Legacy Factor Families (204 factors):** [source-reported]
   - Developed across 9 families capturing A-share specific microstructure:
     - Volume-Weighted Average Price (VWAP) spreads and deviations
     - Turnover velocity and volume acceleration
     - Intraday high-low volatility and shadow/wick metrics
     - Order-flow pressure and limit-move exhaustion proxies
3. **Cross-Sectional Neutralization:** [source-reported]
   - Per-date OLS residualization against 29 CSI industry dummy variables and log market capitalization via `torch.linalg.lstsq`:
     $$f_{t,i}^{\text{neutral}} = f_{t,i} - X_{t,i} (X_t^\top X_t)^{-1} X_t^\top f_t$$
   - Followed by cross-sectional standardization ($z$-scoring) across valid (unmasked) stocks.

### Mask-Aware Tensor Primitives

All operators accept and return explicit Boolean masks [source-reported]:
$$\text{op}(x: \text{Tensor}[T, N], \text{mask}: \text{Tensor}[T, N]) \to (\text{Tensor}[T, N], \text{Tensor}[T, N])$$
- **Zero-on-Mask:** Output value is strictly zero where output mask is `False`.
- **Independence:** Output value does not depend on any input value at a masked cell.
- **Propagation:** Output mask is `False` whenever any input cell in the backward dependency window is masked.
- **Rolling Correlation (`ts_corr`):** Computed via `torch.unfold(dim=0, size=w, step=1)`. Output mask is the logical AND of all cells in the window; if any cell hit a limit or was halted, the entire window is masked.
- **Cross-Sectional Rank (`cs_rank`):** Masked cells are set to $+\infty$ so they sort to the end, then zeroed. Denominator is the exact count of active, unmasked stocks on that date (not total universe $N$), preventing halt-rate distortion.
- **EWMA (`ewma`):** Evaluated in `float64` precision to eliminate accumulation drift over long time series ($\sim 3,000$ bars). On masked cells, previous accumulator value is retained without reset.

### Model Architectures & Loss Function

- **Adjusted-MSE Loss (`AdjMSELoss`):** [source-reported]
  $$\mathcal{L}_{\text{adj}}(\hat{y}, y) = \begin{cases} \gamma (\hat{y} - y)^2 & \text{if } \text{sign}(\hat{y}) \cdot \text{sign}(y) > 0 \\ (1 + \gamma) (\hat{y} - y)^2 & \text{if } \text{sign}(\hat{y}) \cdot \text{sign}(y) \le 0 \end{cases}$$
  - Selected parameter: $\gamma = 0.1$ [source-reported].
  - Effective wrong-sign penalty ratio: $(1 + 0.1) / 0.1 = 11:1$ [source-reported].
- **Model Architecture (Factor-Axis Transformer):** [source-reported]
  - Input: 213-dimensional factor vector projected to $\mathbb{R}^{64}$ via a shared linear layer.
  - Learned positional embedding added per factor position, prepended with a `[CLS]` token (sequence length 214).
  - 2 Transformer encoder layers (4 attention heads, feedforward dimension 256, GELU activation).
  - `[CLS]` token output projected to scalar return prediction $\hat{y}_{t+1,i}$.
  - Parameter count: $\sim 220\text{K}$ parameters [source-reported].
- **Baseline Architecture (MLP):** [source-reported]
  - 2 hidden layers (128 units each, GELU, dropout 0.1), linear scalar output.
  - Parameter count: $\sim 44\text{K}$ parameters [source-reported].
- **Bidirectional Training Filter:** [source-reported]
  - Observation $(x_t, y_{t+1})$ enters dataset if and only if $M_{t,i} = 1$ AND $M_{t+1,i} = 1$. If a stock hits a limit at $t+1$, the return label is non-executable and dropped from training.

### Portfolio Optimization & Position Sizing

At each trading date $t$, the system solves a constrained Mean-Variance Quadratic Program (QP) [source-reported]:
$$\max_{w} \quad \mu^\top w - \alpha \, w^\top \Sigma w \quad \text{s.t.} \quad \mathbf{1}^\top w = 1.0 - w_{\text{cash}}, \quad 0 \le w_i \le w_{\max}$$
- Risk aversion parameter: $\alpha = 10.0$ [source-reported].
- Position weight cap: $w_{\max} = 0.03$ ($3.0\%$ single-stock cap) [source-reported].
- Long-only constraint: $w_i \ge 0$ (reflecting A-share short-selling prohibition) [source-reported].
- Cash reserve: $w_{\text{cash}} = 0.0$ [source-reported].
- Covariance estimator: Ledoit-Wolf analytical shrinkage over a 120-day historical window ($T_{\text{lb}} = 120$) [source-reported].
- Numerical conditioning: Covariance projection to Positive Semi-Definite (PSD) via eigenvalue clamping at $\lambda_{\min} = 10^{-10}$ [source-reported].
- Solver implementation: `cvxpy` with `SCS` solver and parameterized warm-start caching ($6\times$ speedup: $0.2\text{s}$ vs. $1.2\text{s}$ per cross-section) [source-reported].

## Required data

### Market & Universe Specifications

- **Primary Universe:** All liquid Chinese A-share common stocks listed on Shanghai (SSE) and Shenzhen (SZSE) exchanges ($\sim 3,000$ to $3,500$ names) [source-reported].
- **Benchmark Universe:** CSI 300 Index constituents ($\sim 300$ names) evaluated in public validation pipelines [source-reported].
- **Synthetic Panel:** Calibrated 3,000-stock $\times$ 3,500-day panel generated via single-factor Geometric Brownian Motion ($\beta = 0.55$, annual drift $7\%$, annual vol $32\%$, halt probability $1\%$, price limit $\pm 10\%$, seed 42) [source-reported].
- **Data Vendor / Source:** Tushare Pro (real A-share historical panel, 2015-01-04 through 2024-12-31); AkShare / Baostock public data loaders integrated in open-source repository [source-reported].
- **Timeframe:** Daily trading bars ($1\text{D}$).

### Required Input Fields

- Standard OHLCV: `open`, `high`, `low`, `close`, `volume` [source-reported].
- A-Share Specific Fields: `vwap` (Volume-Weighted Average Price), `amount` (turnover in RMB), `last_close` (previous trading day close) [source-reported].
- Microstructure Limit Fields: `limit_up`, `limit_down` (exchange-published upper/lower limit prices) [source-reported].
- Sector Metadata: 29 CSI first-level industry category dummy vectors [source-reported].
- Fundamental Metadata: Total market capitalization (`mkt_cap`) for residualization [source-reported].

### Point-in-Time & Tradability Mask Construction

The Boolean tradability mask tensor $M \in \{0, 1\}^{T \times N}$ is evaluated at data load time [source-reported]:
- **Real Limit Regime:**
  $$M_{t,i} = \mathbb{I}\left( \text{close}_{t,i} < \text{limit\_up}_{t,i} - \varepsilon \quad \text{and} \quad \text{close}_{t,i} > \text{limit\_down}_{t,i} + \varepsilon \right) \land \text{mask}_{t,i}^{\text{active}}$$
  with tolerance $\varepsilon = 10^{-3}$ [source-reported].
- **Proxy Return Regime (when explicit limit bands are absent):**
  $$M_{t,i} = \mathbb{I}\left( \left| \frac{\text{close}_{t,i}}{\text{close}_{t-1,i}} - 1 \right| \le 0.098 \right) \land \text{mask}_{t,i}^{\text{active}}$$
  where threshold is set at $9.8\%$ ($0.098$) to flag limit moves safely [source-reported].
- Day 0 is strictly masked `False` because no prior close is available [source-reported].

## Execution assumptions

- **Execution Cadence & Timing:** Signals formed at the close of trading day $t$ using data available up to $t$ are submitted for execution at day $t+1$ [source-reported].
- **Order Timing & Lag:** One-day execution lag enforced ($w_{t-1}^\top r_t$); weights decided at $t-1$ earn the simple return from $t-1$ to $t$ [source-reported].
- **Order Type & Fill Model:** Assumes full fills at daily bar execution price minus linear transaction costs [source-reported].
- **Transaction Costs:** Linear cost model deducting $c = 5.0$ to $8.0$ basis points per unit of $L_1$ portfolio turnover [source-reported]:
  $$r_t^{\text{net}} = w_{t-1}^\top r_t - c \cdot \|w_t - w_{t-1}\|_1$$
  Baseline backtest uses $c = 8.0\text{ bps}$ ($0.08\%$) in `configs/paper.yaml` and $c = 5.0\text{ bps}$ in core engine, matching retail commissions plus half-spread on liquid names [source-reported].
- **Short Selling / Borrow:** Long-only; no short selling, borrowing, or margin leverage utilized ($0 \le w_i \le 0.03$, $\sum w_i = 1.0$) [source-reported].
- **Intraday Latency & Convex Market Impact:** Not modeled in daily vector engine; linear cost model is acknowledged by the author as optimistic for large portfolios [source-reported gap noted].

## Evidence

### Source-reported

All figures below are transcribed directly from arXiv:2507.07107v2 and the official repository validation records:

#### 1. Headline Strategy Performance (Table 2 of Paper)

- **Calibrated Synthetic Panel (3,000 stocks $\times$ 3,500 dates, 2010–2024; Test: Years 12–14, $\sim 756$ days):**
  - Annualized Return: $28.4\%$ [source-reported]
  - Annualized Sharpe Ratio: $2.05$ [source-reported]
  - Maximum Drawdown: $11.4\%$ [source-reported]
  - Deflated Sharpe Ratio (DSR): $0.994$ (99.4% probability of true Sharpe $> 0$ after deflating for $N \approx 50$ trials) [source-reported]
- **Real A-Share Panel (Tushare, 2015–2024, $\sim 3,200$ active stocks; Test: 2022–2024, $\sim 756$ days):**
  - Annualized Return: $21.8\%$ [source-reported]
  - Annualized Sharpe Ratio: $1.63$ [source-reported]
  - Maximum Drawdown: $14.6\%$ [source-reported]
  - Deflated Sharpe Ratio (DSR): $0.978$ ($97.8\%$ significance against selection threshold $\widehat{\text{SR}}_0 \approx 0.93$, with empirical return skewness $\hat{\gamma}_3 = -0.31$, kurtosis $\hat{\gamma}_4 = 4.7$) [source-reported]

#### 2. Component Ablation Breakdown (Synthetic Panel)

| Component Removed / Modified | Resulting Sharpe | Sharpe Delta ($\Delta \text{SR}$) | Apparent IC | Realizable IC | Max Drawdown |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Full System** | **2.05** | **Baseline** | **0.049** | **0.049** | **11.4%** |
| Remove Tradability Mask (Unmasked) | 1.61 | **-0.44** | 0.058 (+18%) | 0.036 | 22.8% |
| Replace AdjMSE ($\gamma=0.1$) with Standard MSE | 1.78 | **-0.27** | 0.047 | 0.047 | 14.1% |
| Remove GBM Augmentation ($n_s = 0$) | 1.86 | **-0.19** | 0.043 | 0.043 | 13.5% |
| Replace Ledoit-Wolf with Sample Covariance | 1.87 | **-0.18** | 0.049 | 0.049 | 15.2% |
| Replace Transformer with MLP | 1.89 | **-0.16** | 0.045 | 0.045 | 13.8% |

- *The Mask Effect:* Removing the mask produces an artificial $+18\%$ surge in apparent IC ($0.049 \to 0.058$), while realized Sharpe drops by $0.44$ points and drawdown doubles from $11.4\%$ to $22.8\%$ [source-reported].
- *Loss Function Sensitivity:* Sweeping $\gamma \in \{0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 5.0\}$ established $\gamma = 0.1$ as optimal. AdjMSE achieved $53.8\%$ sign accuracy versus $51.2\%$ for MSE, adding $+0.27$ Sharpe [source-reported].
- *Factor Count Contribution:* The first 58 factors account for $\sim 60\%$ of total alpha improvement; the remaining 155 factors contribute the remaining $40\%$ [source-reported].

#### 3. Real-Market Stress Case Studies (2022–2024 Test Window)

- **April 2022 (Shanghai Lockdown):** Market declined $15\%$ in 3 weeks; limit-down events tripled to $\sim 300$ stocks/day. Strategy drawdown: $8.7\%$ with mask versus $14.2\%$ without mask [source-reported].
- **September 2024 (Policy Stimulus Rally):** Market surged $+25\%$ in 2 weeks; limit-up events reached $8\%$ of universe. Strategy return: $+11\%$ (underperformed market because unpurchasable limit-up stocks were strictly excluded) [source-reported].
- **Q1 2023 (AI Theme Rotation):** Factor-axis Transformer captured the volume-surge $\times$ momentum interaction, achieving Q1 Sharpe $2.4$ versus $1.8$ for MLP [source-reported].

#### 4. Maintained Public AkShare CSI 300 Snapshot (2021-01-04 to 2024-12-31, 969 dates, 7 bps cost)

- Equal Weight Daily: Ann. Return $17.75\%$, Sharpe $0.882$, Max DD $25.76\%$, Turnover $0.10\%$ [source-reported]
- Naive Factor Mean Daily: Ann. Return $15.80\%$, Sharpe $0.701$, Max DD $32.51\%$, Turnover $36.27\%$ (Cost Drag $49.16\%$) [source-reported]
- Buffered Factor Mean Daily: Ann. Return $22.20\%$, Sharpe $0.919$, Max DD $27.76\%$, Turnover $13.97\%$ (Cost Drag $18.94\%$) [source-reported]

### Independently reproduced

Not independently reproduced in our execution stack.

### Negative evidence

The paper documents multiple operational vulnerabilities and negative findings:
1. **Unconstrained Factor Pipelines Overstate Alpha:** Standard row-filtering after factor computation produces false alpha (apparent IC $+18\%$ higher than realizable IC).
2. **Euphoric Rally Underperformance:** During sharp stimulus rallies (e.g., September 2024 $+25\%$ index surge), the strategy underperformed the market ($+11\%$ vs. $+25\%$) because it strictly refused to chase unfillable limit-up names.
3. **Turnover Degradation in Naive Ranking:** On public CSI 300 data, naive daily factor-rank rebalancing suffered a catastrophic $49.16\%$ cumulative cost drag at 7 bps, reducing Sharpe from a gross $31.57\%$ return down to a net Sharpe of $0.701$ (inferior to passive equal-weight $0.882$).
4. **Float32 Numerical Drift:** Computing EWMA in `float32` resulted in a $0.3\%$ relative drift over 2,500 bars, degrading factor IC by $0.005$.
5. **Transformer Overfitting Without Augmentation:** Without GBM augmentation, the 220K-parameter Transformer overfit the training set severely (training IC $0.12$ vs. test IC $0.03$).

## Falsification plan

### Operational Tests

1. **Mask Ablation & Realizability Wedge Test:**
   - Run the factor calculation with and without the mask-first tensor primitive contract.
   - **Research-defined falsification threshold:** If apparent IC without the mask is greater than realizable IC by $> 15\%$, and net Sharpe drops by $> 0.30$ under execution-constrained simulation, the reported edge of standard unmasked pipelines is falsified as look-ahead artifact.
2. **Asymmetric Loss vs. Quadratic Utility Test:**
   - Train the Factor-axis Transformer using standard MSE loss, pure cross-entropy sign loss, and AdjMSE ($\gamma=0.1$).
   - **Research-defined falsification threshold:** If AdjMSE fails to outperform standard MSE by at least $+0.15$ annualized Sharpe after 8 bps round-trip costs across a walk-forward split, the hypothesis that directional loss weighting improves downstream MVO utility is falsified.
3. **Ledoit-Wolf vs. Sample Covariance Turnover Stress:**
   - Compare Ledoit-Wolf regularized covariance against raw sample covariance and diagonal risk parity across a 120-day trailing window.
   - **Research-defined falsification threshold:** If Ledoit-Wolf fails to reduce annualized portfolio turnover by $\ge 15\%$ or fails to improve net Sharpe by $\ge 0.10$, shrinkage regularization is rejected as non-critical.
4. **Execution Delay & Next-Open Fill Test:**
   - Shift the execution timestamp from day $t+1$ close/VWAP to day $t+1$ open and day $t+2$ open.
   - **Research-defined falsification threshold:** If net Sharpe degrades by $> 50\%$ when moving execution from $t+1$ close to $t+1$ open, the factor signal relies on intraday mean-reversion rather than persistent cross-sectional mispricing.

## Crypto portability

**Portability Status: Adapted / Unproven.** [research-proposed]

The core mechanism was developed and empirically validated on Chinese A-share equity equities. Porting to cryptocurrency perpetual and spot markets represents an adapted research hypothesis rather than verified crypto evidence:

- **Fill-Gap Equivalence (Perpetual Liquidation & Volatility Halts):** While crypto markets lack exchange-mandated $\pm 10\%$ daily price bands, analogous microstructure non-executability occurs during:
  1. ADL (Auto-Deleveraging) events and liquidation cascade queue freezes.
  2. Exchange API rate-limit throttling and matching-engine dropouts during extreme volatility spikes.
  3. De-pegging stablecoins or wrapped assets hitting circuit breakers.
  Implementing the mask-first contract in crypto would flag bars where taker slippage exceeds a threshold (e.g., $> 50\text{ bps}$) or where open interest collapses by $> 10\%$ in one bar [research-proposed].
- **24/7 Session vs. Daily Close:** Crypto lacks an official 15:00 CST market close. Rolling windows must be defined over fixed hourly or 8-hour funding intervals (e.g., 240-minute bars) rather than calendar dates [research-proposed].
- **Perpetual Funding Rate Drag:** In crypto perpetuals, holding long-biased cross-sectional baskets carries variable 8-hour funding costs (often $20\text{--}50\%\text{ APR}$ during bull regimes). The long-only Markowitz optimization must incorporate funding yields directly into the expected return vector $\mu$ [research-proposed].
- **Long-Short Feasibility:** Unlike A-shares where shorting is restricted, crypto perpetuals allow symmetric shorting. The QP formulation can be expanded to dollar-neutral long/short portfolios with funding-rate arbitrage overlays [research-proposed].

## Limitations

- **Short Out-of-Sample Window:** The empirical test on real A-share data spans only 3 calendar years (2022–2024, $\sim 756$ trading days), covering one major bear market, a sideways recovery, and a short stimulus rally. Multi-cycle stability remains unproven over a decade-long historical span.
- **Linear Transaction Cost Assumption:** The $5\text{--}8\text{ bps}$ linear cost model does not capture square-root market impact or liquidity depletion for assets with Assets Under Management (AUM) $> \$10\text{M}$.
- **Long-Only Constraint:** Constraining weights to $w_i \ge 0$ forfeits short-side alpha and makes the strategy dependent on market beta ($\beta \approx 0.55\text{--}0.80$).
- **Proprietary Real Data:** The Tushare real data feed cannot be redistributed publicly, though the synthetic generator and AkShare public scripts reproduce the full algorithmic pipeline.
- **Static Factor Universe:** The 213-factor registry is fixed; no automated factor discovery or retirement mechanism is included to prevent factor decay.

## Implementation status

- `not-implemented`: No implementation exists in our PyBroker or NautilusTrader pipelines.
- Research material only.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

This record is an empirical research capture and algorithmic design benchmark. It does not authorize strategy deployment, paper trading, testnet, or live execution.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Canonical standard for leakage prevention, embargoing, and point-in-time integrity.
- `[[quant/llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04]]` — Framework for Deflated Sharpe Ratio evaluation and look-ahead detection.
- `[[quant/china-ashare-xgboost-treeshap-behavioral-factor-decomposition-2026-09-04]]` — Companion study on China A-share behavioral factor hierarchies and TreeSHAP attribution.
- `[[quant/cross-market-alpha191-short-term-trading-factors-double-selection-lasso-2026-09-03.md]]` — Short-term alpha factor screening via double-selection Lasso.

## Sources

1. **Yimin Du**, "Machine Learning Enhanced Multi-Factor Quantitative Trading: A Cross-Sectional Portfolio Optimization Approach with Bias Correction," *arXiv preprint* `arXiv:2507.07107v2 [q-fin.PM, cs.CE]`, submitted July 2025, revised 2026. DOI: [10.48550/arXiv.2507.07107](https://doi.org/10.48550/arXiv.2507.07107). Full text: https://arxiv.org/abs/2507.07107.
2. **Yimin Du (initial-d)**, "ml-quant-trading: PyTorch research stack for ML multi-factor trading: 213 factors, bias correction, portfolio optimization, and vectorized backtesting," *GitHub Repository*, commit `c78e27bad025e8317a08d330d2f49b529d85de17`, MIT License, September 2026. URL: https://github.com/initial-d/ml-quant-trading.
3. **David H. Bailey and Marcos López de Prado**, "The Deflated Sharpe Ratio: Correcting for selection bias, backtest overfitting, and non-normality," *Journal of Portfolio Management*, 40(5):94–107, 2014. DOI: [10.3905/jpm.2014.40.5.094](https://doi.org/10.3905/jpm.2014.40.5.094).
4. **Olivier Ledoit and Michael Wolf**, "A well-conditioned estimator for large-dimensional covariance matrices," *Journal of Multivariate Analysis*, 88(2):365–411, 2004. DOI: [10.1016/S0047-259X(03)00096-4](https://doi.org/10.1016/S0047-259X(03)00096-4).
5. **Zura Kakushadze**, "101 Formulaic Alphas," *Wilmott*, 2016(84):72–81, 2016. DOI: [10.1002/wilm.10526](https://doi.org/10.1002/wilm.10526).
