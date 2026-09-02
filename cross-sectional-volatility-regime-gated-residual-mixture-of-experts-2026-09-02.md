---
schema: strategy-research-record-v1
title: "Cross-Sectional Volatility Forecasting via Regime-Gated Residual Mixture-of-Experts (RG-ResMoE): Frozen Base Anchoring, Soft State-Dependent Routing, and Downside VaR Calibration"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - volatility-forecasting
  - mixture-of-experts
  - residual-learning
  - cross-sectional-volatility
  - regime-gating
  - value-at-risk
  - machine-learning
status: research-only
confidence: high
source_as_of: 2026-08-12
sources:
  - "Junyi Ye and Gargi Vijay Borde, 'Regime-Gated Residual Mixture-of-Experts for Cross-Sectional Volatility Forecasting', arXiv:2608.12251v1 [q-fin.ST], August 12, 2026. DOI: 10.48550/arXiv.2608.12251. https://arxiv.org/abs/2608.12251"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Sectional Volatility Forecasting via Regime-Gated Residual Mixture-of-Experts (RG-ResMoE): Frozen Base Anchoring, Soft State-Dependent Routing, and Downside VaR Calibration

## Provenance

- **Primary Source:** Junyi Ye and Gargi Vijay Borde (Department of Information Management and Business Analytics, Feliciano School of Business, Montclair State University), *"Regime-Gated Residual Mixture-of-Experts for Cross-Sectional Volatility Forecasting"*, arXiv preprint `arXiv:2608.12251v1 [q-fin.ST]`, published August 12, 2026. DOI: [10.48550/arXiv.2608.12251](https://doi.org/10.48550/arXiv.2608.12251). Full text: [https://arxiv.org/abs/2608.12251](https://arxiv.org/abs/2608.12251).
- **Primary Subject Area:** Statistical Finance (`q-fin.ST`).
- **Context:** Financial market nonstationarity means relationships between historical price features and future realized volatility shift across calm, crisis, and recovery regimes. While prior literature incorporates macro/market regime variables by directly concatenating them to neural forecasting inputs or using discrete regime switching, this often induces severe optimization instability, gradient explosion/vanishing, and test-set degradation. Ye and Borde isolate the *point of regime integration* within neural architectures, demonstrating that nonstationary regime indicators should only guide continuous soft routing over zero-initialized residual correction experts anchored to a frozen base predictor.

## Economic mechanism

### Source-reported

1. **Nonstationary Regime Dynamics in Volatility:** The predictive mapping from historical stock features to future realized volatility is regime-dependent. In calm regimes, volatility exhibits strong autoregressive persistence; during market crashes or crisis recoveries, cross-asset correlations surge and idiosyncratic signals break down.
2. **Pathological Degradation from Direct Input Concatenation:** Appending macro/regime state variables ($z_t$) directly to predictor inputs forces the forecasting network to learn joint high-dimensional interactions across nonstationary states. This destabilizes parameter optimization across rolling walk-forward windows and leads to severe out-of-sample forecast collapse.
3. **Decoupled Residual Gating Mechanism:** Decomposing volatility prediction into a global baseline $\hat{y}_{\mathrm{base}}(x)$ and gated residual corrections $r_k(x)$ allows specialized experts to model state-dependent nonlinear deviations without destabilizing the core level forecast.
4. **Continuous Soft Modulation vs. Hard Discretization:** Market regime transitions are continuous rather than discrete. Smooth state-dependent reweighting through a softmax gating network avoids the boundary estimation errors and sample-splitting inefficiencies inherent in hard regime partitions.

### Research interpretation

The falsifiable thesis is that **the primary value of Mixture-of-Experts in financial time-series forecasting is not expanding parameter capacity, but controlling the entry pathway of nonstationary regime context**:
- Treating regime state variables as predictive inputs contaminates baseline representations with nonstationary macro noise.
- Restricting regime variables to a gating network that routes zero-initialized residual corrections regularizes the predictive hypothesis space, preserving base stability while providing localized non-linear adjustments during extreme market distress.

## Signal

### 1. Feature Representation

For stock $i$ on day $t$:
- **Stock-Level Feature Vector ($x_{i,t} \in \mathbb{R}^{16}$):**
  - Realized volatility over trailing 5, 20, and 60 trading days ($RV_{i,t}^{(5)}, RV_{i,t}^{(20)}, RV_{i,t}^{(60)}$).
  - Cumulative log returns over trailing 5 and 20 trading days ($R_{i,t}^{(5)}, R_{i,t}^{(20)}$).
  - 14-day Relative Strength Index ($RSI_{i,t}^{(14)}$).
  - Ten most recent daily log returns ($r_{i,t}, r_{i,t-1}, \dots, r_{i,t-9}$).
  - All features normalized using rolling z-scores estimated strictly within the training fold.
- **Regime State Variables ($z_{i,t} \in \mathbb{R}^2$):**
  - *Market Volatility:* 20-day rolling annualized realized volatility of the equal-weighted market return $r_{m,t}$.
  - *Idiosyncratic Volatility:* 20-day rolling volatility of the CAPM residual return $e_{i,t} = r_{i,t} - \beta_{i,t} r_{m,t}$, where beta $\beta_{i,t}$ is estimated via 120-day trailing OLS regression.

### 2. RG-ResMoE Network Architecture

- **Shared MLP Block:** Two-hidden-layer MLP with hidden width $H=16$, GELU non-linear activations $\phi$, and dropout rate $p=0.10$ after each hidden layer:
  $$\mathrm{MLP}(q) = W_3 \phi(W_2 \phi(W_1 q + b_1) + b_2) + b_3$$
- **Two-Stage Training Protocol:**
  1. *Stage 1 (Base Model):* Train a single shared MLP base predictor $f_{\theta_b}(x)$ on stock features $x_{i,t}$ using full-batch Adam to minimize MSE against forward realized volatility. Freeze $\theta_b$.
  2. *Stage 2 (Residual Experts & Soft Gate):* Instantiate $K=4$ residual correction expert MLPs $\{g_{\theta_k}(x)\}_{k=1}^K$ (each $H=16$) with zero-initialized final linear projection layers ($W_3^{(k)} = 0, b_3^{(k)} = 0 \implies r_k(x) \equiv 0$ at step 0).
  3. *Soft Gating Network:* A routing network $g_{\psi}(u)$ where $u = (x, z)$ observes both stock features and regime state variables, computing continuous weights:
     $$\pi(u) = \operatorname{softmax}(g_{\psi}(u)) \in \Delta^{K-1}$$
  4. *Final Aggregate Volatility Forecast:*
     $$\hat{y}_{i,t} = f_{\theta_b}(x_{i,t}) + \sum_{k=1}^K \pi_k(x_{i,t}, z_{i,t}) \cdot g_{\theta_k}(x_{i,t})$$

### 3. Regularized Training Objective

Stage 2 parameters $(\{\theta_k\}_{k=1}^K, \psi)$ are optimized via:
$$\mathcal{L} = \frac{1}{B}\sum_{i=1}^B \left( y_{i,t} - \hat{y}_{i,t} \right)^2 + \alpha \cdot \frac{1}{B}\sum_{i=1}^B \left( \sum_{k=1}^K \pi_k(u_{i,t}) g_{\theta_k}(x_{i,t}) \right)^2 + \lambda_{\mathrm{LB}} \sum_{k=1}^K \left( \bar{\pi}_k - \frac{1}{K} \right)^2$$
where:
- $\alpha > 0$ enforces shrinkage of residual corrections toward the frozen base forecast.
- $\lambda_{\mathrm{LB}} > 0$ penalizes routing collapse away from uniform allocation $\bar{\pi}_k = \frac{1}{B}\sum_{i=1}^B \pi_k(u_{i,t})$.
- Full-batch Adam optimization with early stopping evaluated on validation fold loss.

## Required data

- **Universe:** 
  - Main Panel: 1,027 U.S. equities (spanning S&P 1500 large, mid, and small-cap across all 11 GICS sectors; $\ge 6$ years price history, Yahoo Finance).
  - Cross-Market Panel: 1,552 Japanese equities covering the Tokyo Stock Exchange (TSE) Prime segment.
- **Timeframe:** Daily OHLCV price series spanning December 2015 to November 2025.
- **Target Variable:** 5-day forward annualized realized volatility:
  $$RV_{i,t:t+5} = \sqrt{\frac{252}{5} \sum_{k=1}^5 r_{i,t+k}^2}$$
- **Data Alignment & Leakage Controls:**
  - Rolling walk-forward protocol: 504 trading days (2 years) development window (first 85% training, final 15% validation) followed by 63 trading days (1 quarter) non-overlapping out-of-sample test window.
  - Step size: 63 trading days, yielding 30 non-overlapping out-of-sample test windows from April 2018 to October 2025 (~1.9 million out-of-sample forecasts).
  - Strict point-in-time calculation of rolling betas (120 days) and regime indicators (20 days).

## Execution assumptions

- **Execution Mode:** Cross-sectional volatility forecast serving as alpha signal or risk overlay for volatility targeting, dispersion trading, or Value-at-Risk (VaR) position sizing.
- **Signal-to-Order Timing:** Forecast generated at day $t$ market close; trades executed at next-day market open ($t+1$) or utilized for $t+1$ portfolio margin / risk constraints.
- **Transaction Costs & Turnover:** 
  - Volatility forecasts updated on a daily/weekly rolling basis.
  - Sizing overlays must incorporate execution friction and bid-ask spreads when rebalancing equity derivative or delta-hedging books.

## Evidence

### Source-reported

All figures trace directly to Ye & Borde (arXiv:2608.12251v1, Tables 3, 4, 5, 6, 7, 8, 9):

1. **Main U.S. Panel Forecasting Performance (30 Seeds, Walk-Forward 2018–2025):**
   - **RG-ResMoE:** Highest Information Coefficient ($\mathrm{IC} = 0.5469$), lowest Root Mean Squared Error ($\mathrm{RMSE} = 0.1691$), highest out-of-sample $R^2 = 0.4482$, highest Information Ratio ($\mathrm{ICIR} = 2.128$), and lowest Quasi-Likelihood loss ($\mathrm{QLIKE} = -0.5821$).
   - **Capacity-Matched MLP-L ($H=44$):** Achieves $\mathrm{IC} = 0.5421$, $\mathrm{RMSE} = 0.1704$, $R^2 = 0.4398$, $\mathrm{ICIR} = 2.054$, $\mathrm{QLIKE} = -0.5694$.
   - **Diebold-Mariano Statistical Significance:** Pairwise Newey-West adjusted tests confirm RG-ResMoE outperformance over MLP-L is statistically significant ($p < 10^{-4}$ for IC and RMSE; $p = 0.001$ for QLIKE).
2. **Integration Pathway Comparison & Training Stability:**
   - Appending regime variables to inputs ($\mathrm{MLP}\text{-}\mathrm{L}(+z)$) degrades performance and induces training failure: $\mathrm{MLP}\text{-}\mathrm{L}(+z)$ collapsed in **24 of 30 random seeds** (defined as mean test $\mathrm{QLIKE} > 2.0$).
   - Standard un-anchored MoE without frozen base collapsed in **24 of 30 seeds**.
   - Proposed **RG-ResMoE completed all 30 seeds with 0 collapses**.
3. **Soft Routing vs. Hard Routing Ablation:**
   - Soft gate ($\mathrm{IC} = 0.5469$) strictly outperformed all hard routing alternatives: Learned Top-1 Gate ($\mathrm{IC} = 0.5448$), Volatility Quantile Partition ($\mathrm{IC} = 0.5435$), GICS Sector Split ($\mathrm{IC} = 0.5439$), and Market-Vol $\times$ Idiosyncratic-Vol Matrix Split ($\mathrm{IC} = 0.5441$), all differences significant at $p < 10^{-4}$.
4. **Crisis & Elevated Volatility Amplification:**
   - In the highest market-volatility decile, RG-ResMoE's IC advantage over MLP-L expands from $+0.0048$ (full sample) to **$+0.0207$** ($4.3\times$ amplification).
   - During the COVID-19 crash, the IC advantage reached **$+0.0322$** ($6.7\times$ full sample).
5. **Value-at-Risk (VaR) Calibration:**
   - Evaluated via Kupiec's unconditional coverage test at 5% and 1% levels. RG-ResMoE achieved lowest rejection rates across 5 of 6 regime-VaR combinations, significantly outperforming MLP baselines during high-volatility regimes.
6. **Cross-Market Replication (Japanese TSE Prime Panel):**
   - Evaluated on 1,552 Japanese equities: RG-ResMoE achieved $\mathrm{IC} = 0.5184$ vs. MLP-L $\mathrm{IC} = 0.5141$ ($+0.0043$ gain, $p < 10^{-4}$).
   - Direct input concatenation $\mathrm{MLP}\text{-}\mathrm{L}(+z)$ collapsed in **28 of 30 seeds** on the Japanese panel.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- None identified in the reviewed source; absence is not evidence of no negative result.
- However, the source explicitly documents that traditional Mixture-of-Experts architectures without frozen base anchoring and standard MLP networks with concatenated regime inputs suffer extreme optimization fragility (collapsing in $80\%\text{--}93\%$ of initializations).

## Falsification plan

1. **Shuffled-Regime Placebo Test:** Permute the temporal sequence of regime variables $z_t$ across training and test windows. If RG-ResMoE retains its IC advantage over MLP-L under permuted regime inputs, the routing gain is an artifact of ensemble capacity rather than regime conditioning.
2. **Out-of-Sample Horizon Sensitivity:** Extend the forecasting horizon from 5-day to 20-day and 60-day realized volatility. If residual expert gating fails to maintain positive ICIR across longer horizons, the mechanism is restricted to high-frequency micro-regimes.
3. **Execution & Volatility Dispersion Test:** Implement a long-short cross-sectional equity volatility dispersion strategy (buying high-forecast IV/RV, selling low-forecast IV/RV). If net transaction costs from option bid-ask spreads erase the $+0.0048$ IC advantage, the alpha is non-tradable in liquid derivatives markets.
4. **Failure Threshold:** If out-of-sample IC falls below benchmark linear Ridge regression ($\mathrm{IC} < 0.5310$) in $\ge 3$ consecutive quarterly test windows, reject model deployment.

## Crypto portability

**Portability Status:** `adapted` / `unproven`.

- **Mechanism Portability:** Crypto asset markets exhibit extreme nonstationarity, regime shifts between high-volatility liquidation cascades and low-volatility consolidation ranges, and heavy idiosyncratic dispersion across altcoins. The principle of using a frozen baseline with regime-gated residual experts is directly applicable.
- **Adaptation Requirements:**
  - *Regime Indicators:* Replace traditional market equity volatility with crypto-native regime metrics: 20-day rolling Bitcoin/Ethereum realized volatility, aggregate perpetual funding rate z-scores, market-wide Open Interest (OI) percentage changes, and aggregate liquidation volume.
  - *24/7 Session Structure:* Crypto trading lacks discrete daily market closes. Volatility targets must be defined on rolling 8-hour or 24-hour UTC windows.
  - *Data Frequency:* High-frequency tick and minute data in crypto enable intraday realized kernel or Parkinson volatility estimation rather than coarse close-to-close returns.
- **Portability Risks:** High idiosyncratic token turnover, exchange-level liquidation engine dynamics, and venue fragmentation may require more frequent retraining or dynamic regularization weights ($\alpha, \lambda_{\mathrm{LB}}$).

## Limitations

- **Model Capacity:** Evaluated on compact MLP backbones ($H=16$); scalability to deep transformer architectures or state-space models (Mamba) remains unverified.
- **Survivorship Bias in Panel:** The U.S. equity panel requires 6+ years of history, introducing mild survivorship bias into the historical universe.
- **Data Gap:** The model assumes reliable daily close prices; in fragmented markets (crypto/DEX), stale pricing or flash liquidity drops require robust pre-filtering.

## Implementation status

`not-implemented`

No implementation has been conducted in the local research repository, PyBroker, NautilusTrader, paper, testnet, or live trading systems.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

This record is an upstream research capture. It does not authorize strategy implementation, backtesting promotion, or production deployment.

## Related Wiki records

- `[[equity-cross-regime-bayesian-optimisation-xgboost-tabnet-hybrid-2026-09-02]]`
- `[[neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02]]`
- `[[path-portfolio-optimization-signature-defect-lift-2026-09-02]]`

## Sources

- Junyi Ye and Gargi Vijay Borde, *"Regime-Gated Residual Mixture-of-Experts for Cross-Sectional Volatility Forecasting"*, arXiv preprint `arXiv:2608.12251v1 [q-fin.ST]`, submitted August 12, 2026. DOI: `10.48550/arXiv.2608.12251`. URL: [https://arxiv.org/abs/2608.12251](https://arxiv.org/abs/2608.12251).
