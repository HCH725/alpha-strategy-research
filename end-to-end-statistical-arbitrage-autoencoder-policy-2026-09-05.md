---
schema: strategy-research-record-v1
title: "End-to-End Policy Learning of a Statistical Arbitrage Autoencoder Architecture: Direct Portfolio Optimization over Non-Linear Latent Residuals"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - autoencoder
  - policy-learning
  - end-to-end-learning
  - deep-learning
  - mean-reversion
  - portfolio-optimization
  - equities
status: research-only
confidence: high
source_as_of: 2024-02-13
sources:
  - "Fabian Krause and Jan-Peter Calliess, 'End-to-End Policy Learning of a Statistical Arbitrage Autoencoder Architecture', arXiv:2402.08233v1 [cs.LG], February 13, 2024. https://arxiv.org/abs/2402.08233"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# End-to-End Policy Learning of a Statistical Arbitrage Autoencoder Architecture: Direct Portfolio Optimization over Non-Linear Latent Residuals

## Provenance

- **Primary Academic Source:** Fabian Krause and Jan-Peter Calliess (Department of Engineering, University of Oxford, Oxford, United Kingdom), *"End-to-End Policy Learning of a Statistical Arbitrage Autoencoder Architecture"*, arXiv preprint `arXiv:2402.08233v1 [cs.LG]`, submitted February 13, 2024; accepted to the International Conference on Machine Learning (ICML 2024).
  - Canonical arXiv Abstract: [https://arxiv.org/abs/2402.08233](https://arxiv.org/abs/2402.08233)
  - Canonical DOI: [https://doi.org/10.48550/arXiv.2402.08233](https://doi.org/10.48550/arXiv.2402.08233)
  - Full-Text HTML: [https://arxiv.org/html/2402.08233v1](https://arxiv.org/html/2402.08233v1)
  - Authors' Affiliation: Department of Engineering Science, University of Oxford. Corresponding author email: `lina3477@ox.ac.uk`.
- **Pre-Write Deduplication & Identity Verification:** An exhaustive scan across all 370+ markdown strategy captures in `alpha-strategy-research` confirmed zero existing records matching `2402.08233`, `Fabian Krause`, or `Autoencoder Policy StatArb`. Existing statistical arbitrage records in the repository focus on classical cointegration, convex-concave moving bands (`cvxstatarb`), two-layer LSTM factor replication (`Adamczyk & Dąbrowski 2025`), SPONGE graph Laplacian clustering (`Korniejczuk & Ślepaczuk 2024`), or rank-space CNN/transformer hybrids; none explore end-to-end differentiable policy optimization uniting non-linear autoencoder factor discovery directly with risk-adjusted portfolio backpropagation.

## Economic mechanism

### Source-reported

1. **Alignment Failure of Two-Stage StatArb Pipelines:** In classical statistical arbitrage (e.g., Avellaneda & Lee 2010; Gatev et al. 2006), the trading workflow is fundamentally decoupled into two sequential stages:
   - *Stage 1 (Asset Pricing Model)*: Estimating cross-sectional factor models (observable Fama-French factors, or latent factors via Principal Component Analysis) to describe asset price movement and isolate idiosyncratic residuals.
   - *Stage 2 (Signal Extraction & Portfolio Sizing)*: Fitting a univariate mean-reversion time-series process (e.g., Ornstein-Uhlenbeck) to the residuals and executing trades based on heuristic deviation thresholds (s-scores).
   Krause & Calliess emphasize that this disjoint pipeline introduces severe *modeling risk and objective misalignment*: asset pricing models are mathematically designed to maximize variance explanation across asset returns ($\min \text{MSE}$), *not* to generate residuals that exhibit fast, tradable mean-reversion properties. The mean-reversion characteristic is merely an incidental byproduct.
2. **Autoencoders as Non-Linear Factor Generalization:** Autoencoders naturally extend PCA (Oja 1982) by allowing non-linear bottleneck representations of cross-sectional asset returns. The authors explore whether basic Autoencoders can generate superior residuals for traditional Ornstein-Uhlenbeck trading compared to PCA and Fama-French multi-factor baselines.
3. **End-to-End Policy Learning:** To eliminate the multi-stage friction entirely, the authors propose embedding the Autoencoder directly into a neural policy network. The network takes standardized cross-sectional returns, passes them through a non-linear latent bottleneck, computes internal residuals via an architectural skip-connection, and directly outputs normalized portfolio allocations $w_t$. The entire network is trained end-to-end via backpropagation using a dual-objective loss function that jointly minimizes return reconstruction error and maximizes next-day risk-adjusted portfolio return (annualized Sharpe ratio).

### Research interpretation

1. **Objective Alignment via Direct Sharpe Backpropagation:** By making the portfolio allocation weights $w_t$ differentiable with respect to the factor weights $W^{(0)}, W^{(1)}$ and the policy layer $W^{(2)}$, the network parameters are updated according to their marginal contribution to the portfolio Sharpe ratio. If a particular latent factor fails to produce mean-reverting residuals that translate into trading alpha, the gradient updates down-weight or reshape that factor representation, directly resolving the objective mismatch of classical asset pricing.
2. **Skip-Connection as Idiosyncratic Filter:** The subtraction layer $\hat{Z}_t - Z_t$ serves as a structural prior: the policy network is explicitly constrained to trade the *unexplained* component of returns rather than trading raw momentum or market beta. This enforces factor-neutral statistical arbitrage within the architecture while allowing the policy layer $W^{(2)} \in \mathbb{R}^{N \times N}$ to capture cross-sectional mean-reversion spillover across assets.
3. **Turnover vs. Alpha Tradeoff:** While the end-to-end architecture achieves a reported pre-cost Sharpe ratio of 1.81 (outperforming PCA OU at 0.96 and FF5 Mom at 0.52), daily re-training and unconstrained tanh policy updates induce high portfolio turnover. The economic validity of this alpha rests entirely on whether the gross Sharpe premium can survive realistic transaction fees, bid-ask spreads, and execution latency.

## Signal

The strategy operates through a single integrated, end-to-end trainable neural network policy evaluated daily.

### Network Architecture (`source-reported`)

Let $N$ be the number of active eligible stocks at date $t$, and $Z_t \in \mathbb{R}^{N \times 1}$ be the vector of standardized daily returns:

1. **Encoder (Latent Factor Compression):**
   $$F_t = \text{enc}(Z_t) = \text{ReLU}\left(W^{(0)} Z_t + b^{(0)}\right)$$
   where:
   - $Z_t \in \mathbb{R}^{N \times 1}$ is the input standardized return vector (`source-reported`).
   - $W^{(0)} \in \mathbb{R}^{l \times N}$ and $b^{(0)} \in \mathbb{R}^{l \times 1}$ (`source-reported`).
   - $l$ is the number of latent factors ($l \in \{3, 5, 6, 8, 10, 15, 20, 30, 50\}$, with $l = 15$ optimal; `source-reported`).
2. **Decoder (Cross-Sectional Factor Return Reconstruction):**
   $$\hat{Z}_t = \text{dec}(F_t) = \tanh\left(W^{(1)} F_t + b^{(1)}\right) = \tanh\left(W^{(1)} \left(\text{ReLU}\left(W^{(0)} Z_t + b^{(0)}\right)\right) + b^{(1)}\right)$$
   where:
   - $W^{(1)} \in \mathbb{R}^{N \times l}$ and $b^{(1)} \in \mathbb{R}^{N \times 1}$ (`source-reported`).
   - The $\tanh$ activation reconstructs bounded standardized returns (`source-reported`).
3. **Idiosyncratic Residual Skip-Layer:**
   $$\epsilon_t = \hat{Z}_t - Z_t$$
   Calculates the difference between decoded (common factor) returns and input standardized returns (`source-reported`).
4. **Trading Policy Layer (Direct Portfolio Allocation):**
   $$\tilde{w}_t = \tanh\left(W^{(2)} (\hat{Z}_t - Z_t)\right)$$
   where $W^{(2)} \in \mathbb{R}^{N \times N}$ contains no bias term (`source-reported`).
5. **Gross Leverage Normalization:**
   $$w_t = \frac{\tilde{w}_t}{\|\tilde{w}_t\|_1}$$
   Enforces a constant gross portfolio leverage of 1 ($\sum_{i=1}^N |w_{i,t}| = 1$) (`source-reported`).
   *(Note: Equation 9 in the primary text writes $\sum_{i=1}^n w_{i,t} = 1$, but Equation 8 and Section 3.3 explicitly define the constraint as targeting constant leverage 1 via the $L_1$ norm $\|w_t\|_1 = 1$, with both long and short positions allowed).*

### Joint Optimization Objective (`source-reported`)

The entire parameter set $\theta = \{W^{(0)}, W^{(1)}, W^{(2)}, b^{(0)}, b^{(1)}\}$ is optimized by minimizing a composite loss combining reconstruction fidelity and negative risk-adjusted returns:

$$\min_\theta \quad \mathcal{L}(\theta) = \lambda \cdot \text{MSE}(Z_t, \hat{Z}_t) + (1 - \lambda) \cdot \left(- \text{Sharpe}(w_t, R_{t+1})\right)$$

where:
- $\lambda = 0.5$ is the gearing hyperparameter balancing reconstruction versus Sharpe maximization (`source-reported`).
- $\text{MSE}(Z_t, \hat{Z}_t) = \frac{1}{N} \sum_{i=1}^N (Z_{i,t} - \hat{Z}_{i,t})^2$ (`source-reported`).
- The portfolio Sharpe ratio policy is defined over the historical evaluation window:
  $$\text{Sharpe} = \sqrt{252} \cdot \frac{\mu_{p,t}}{\sigma_{p,t}}$$
  $$\mu_{p,t} = \frac{1}{T} \sum_{\tau=1}^T r_{p, t-\tau}, \quad \sigma_{p,t} = \sqrt{\frac{1}{T} \sum_{\tau=1}^T \left(r_{p, t-\tau} - \mu_{p,t}\right)^2}$$
  with daily realized portfolio return $r_{p,t} = \sum_{i=1}^N w_{i,t} r_{i,t+1}$ (`source-reported`).

### Training & Inference Schedule (`source-reported`)

- **Training Lookback Window:** Rolling historical window of $T_\tau = 252$ trading days (1 trading year) of standardized returns (`source-reported`).
- **Retraining Frequency:** A fresh model is trained every trading day (`source-reported`).
- **Training Epochs & Optimizer:** 10 epochs using Adam optimizer with learning rate $\alpha = 0.001$ (`source-reported`).
- **Prediction:** Out-of-sample portfolio weights $w_t$ are generated at the close of day $t$ and executed for day $t+1$ (`source-reported`).

### Operational Extensions (`research-proposed`)

- **Turnover Regularization Penalty:** To address high turnover from daily unconstrained weight rebalancing, augment the loss function with an $\ell_1$ weight change penalty:
  $$\mathcal{L}_{\text{reg}}(\theta) = \mathcal{L}(\theta) + \gamma_{\text{turnover}} \cdot \|w_t - w_{t-1}\|_1$$
  with $\gamma_{\text{turnover}} = 0.05$ (`research-proposed`).
- **Inference-Only Cadence:** Instead of full daily retraining (which incurs severe model weight instability and heavy compute overhead), freeze the model and retrain weekly (every 5 trading days) or monthly (every 21 trading days), updating $w_t$ daily through forward inference: `research-proposed`.

## Required data

- **Asset Universe:** US-traded common equities, restricted strictly to primary listings from CRSP (January 2000 to December 2022, comprising 5,787 daily observations; `source-reported`).
  - Total raw universe: 13,610 companies (`source-reported`).
  - Monthly Screened Universe: Stocks filtered at the end of each calendar month using three criteria (`source-reported`):
    1. Closing price $P_t \ge \$5.00$;
    2. 20-day median rolling market capitalization $\ge \$1\text{bn}$;
    3. 20-day median rolling trading dollar volume $\ge \$1\text{m}$.
  - Filtered Universe Size: 5,188 total unique companies over the full 2000–2022 sample, with an average of 1,470 active stocks per month (`source-reported`).
- **Timeframe & Aggregation:** Daily total returns adjusted for dividends and stock splits (`source-reported`).
- **Return Standardization:**
  $$Z_{i, t-\tau} = \frac{r_{i, t-\tau} - \mu_{i, t-T_\tau:t}}{\sigma_{i, t-T_\tau:t}}, \quad \text{for } \tau = 0, \dots, T_\tau - 1$$
  where $T_\tau = 252$ trading days. Standardized returns $Z_{i,t}$ are capped at $\pm 3.0$ standard deviations to prevent outlier distortion (`source-reported`).
- **Missing Data Handling:** Only stocks with zero missing return observations throughout the full 252-day lookback window are included in the daily optimization matrix (`source-reported`).
- **Benchmark Data:** Daily Fama-French factor returns (Market, SMB, HML, RMW, CMA, MOM) and daily risk-free rate from Kenneth French's data library (`source-reported`).

## Execution assumptions

- **Timing & Fill Horizon:**
  - Portfolio weights $w_t$ are generated at the end of trading day $t$ using return information up to the close of day $t$ (`source-reported`).
  - Positions are assumed taken at the beginning of day $t+1$ and held until the end of day $t+1$, capturing return $r_{p,t} = \sum_{i=1}^N w_{i,t} r_{i,t+1}$ (`source-reported`).
- **Transaction Costs & Frictions:**
  - *Source-Reported Baseline*: All reported performance figures in the primary paper are strictly **gross returns before transaction costs** (`source-reported`). The primary authors explicitly cite transaction cost drag as an open limitation in Section 6 and Section 7.
  - *Research-Proposed Execution Model*: Institutional execution simulation with:
    - 5 bps one-way trading fee (10 bps round trip) for large-cap US equities (`research-proposed`);
    - 10 bps one-way trading fee (20 bps round trip) for mid-cap equities (`research-proposed`);
    - Short borrow fee of 0.50% annualized on all negative weights (`research-proposed`).
- **Fill Price Model:** Execution at open of day $t+1$ ($P_{t+1}^{\text{open}}$) or daily VWAP rather than assuming frictionless close-to-close returns (`research-proposed`).
- **Capacity & Participation:** Participation capped at 1.0% of 20-day median daily volume per stock to limit market impact (`research-proposed`).

## Evidence

### Source-reported

All quantitative figures below trace directly to Krause and Calliess (`arXiv:2402.08233v1`, February 2024), evaluated on 5,188 eligible US equities over the 2000–2022 period (5,787 daily periods). All figures represent gross excess returns before transaction costs:

#### 1. End-to-End Autoencoder Policy Performance across Latent Dimensions (Table 3)

| Latent Dimension ($l$) | Annualized Sharpe Ratio (Gross) | Mean Annual Return ($\mu$) | Annual Volatility ($\sigma$) |
| :--- | :--- | :--- | :--- |
| **$l = 3$** | 1.51 | 5.56% | 3.69% |
| **$l = 5$** | 1.42 | 5.08% | 3.58% |
| **$l = 6$** | 1.67 | 5.66% | 3.40% |
| **$l = 8$** | 1.73 | 6.20% | 3.58% |
| **$l = 10$** | 1.75 | 5.89% | 3.37% |
| **$l = 15$** *(Optimal)* | **1.81** | **6.24%** | **3.46%** |
| **$l = 20$** | 1.50 | 5.34% | 3.55% |
| **$l = 30$** | 1.43 | 5.28% | 3.68% |
| **$l = 50$** | 1.58 | 5.68% | 3.60% |

*Key Findings from Authors:* The optimal number of latent factors is $l = 15$ (SR 1.81), aligning with the broader empirical asset pricing literature where 10 to 15 statistical factors capture the majority of systematic equity cross-sectional variance.

#### 2. Benchmark Asset Pricing Models with Ornstein-Uhlenbeck (OU) Extraction (Tables 2 & 4)

Standard two-stage pipeline using Avellaneda & Lee (2010) Ornstein-Uhlenbeck signal extraction (long entry $s < -1.25$, short entry $s > 1.25$, exit long $s > -0.50$, exit short $s < 0.75$, $R^2 \ge 0.25$):

| Model Class | Variant / Latent Components | Annualized Sharpe Ratio | Mean Return ($\mu$) | Annual Volatility ($\sigma$) |
| :--- | :--- | :--- | :--- | :--- |
| **Fama-French OU** | CAPM (1 factor) | 0.13 | 1.31% | 10.17% |
| **Fama-French OU** | FF 3 (Mkt, SMB, HML) | 0.30 | 2.07% | 6.89% |
| **Fama-French OU** | FF 5 (+ RMW, CMA) | 0.33 | 2.22% | 6.78% |
| **Fama-French OU** | FF 5 + Momentum | 0.52 | 3.39% | 6.56% |
| **PCA OU** | PCA 1 | 0.44 | 2.92% | 6.64% |
| **PCA OU** | PCA 3 | 0.74 | 4.04% | 5.48% |
| **PCA OU** | PCA 5 | 0.76 | 3.88% | 5.07% |
| **PCA OU** | PCA 6 | 0.88 | 4.33% | 4.93% |
| **PCA OU** | PCA 8 *(Best PCA)* | **0.96** | **4.55%** | **4.74%** |
| **PCA OU** | PCA 10 | 0.92 | 4.30% | 4.66% |
| **PCA OU** | PCA 15 | 0.87 | 3.94% | 4.53% |
| **PCA OU** | PCA 20 | 0.88 | 3.91% | 4.43% |

#### 3. Two-Stage Autoencoder Residuals with OU Extraction (Tables 4 & 5)

When Autoencoders are used *only* as a stage-1 residual generator (without end-to-end policy learning):
- **Option 1 (Direct Residual Subtraction $Z - \hat{Z}$ into OU):** All 10 Autoencoder architectural variants yielded **negative Sharpe ratios** ranging from -0.18 to -0.29 (Table 4). Direct autoencoder residuals without regression fail completely under OU thresholding.
- **Option 2 (Latent Factor Encoder Regression into OU):** Best variant (Variant 1: 3 layers, tanh, dropout 0.25) achieved Sharpe 0.34 ($\mu = 5.76\%, \sigma = 16.96\%$).
- **Option 3 (Volatility-Scaled Latent Factor Regression into OU):** Best variant (Variant 6: 3 layers, relu, dropout 0.25) achieved Sharpe 0.42 ($\mu = 6.93\%, \sigma = 16.52\%$).
- **OU + Feed-Forward Network (FFN) Signal Extraction (Table 5):** When a 3-layer FFN replaces heuristic OU thresholds, performance degraded across all models (FF OU+FFN SR -0.31 to 0.11; PCA OU+FFN SR -0.31 to -0.04; AE OU+FFN SR -0.30 to 0.12).

*Core Theoretical Conclusion:* Traditional two-stage decoupling fails when applying non-linear neural networks to factor generation. Only the unified end-to-end policy optimization that aligns the representation directly with the Sharpe objective produces statistically superior alpha.

### Independently reproduced

`Not independently reproduced.` The mathematical equations, loss functions, network dimensions, and empirical baseline tables have been audited directly from the primary LaTeX source of `arXiv:2402.08233v1`, but the full 23-year CRSP dataset backtest has not been executed within our internal research environment.

### Negative evidence

1. **Catastrophic Failure of Decoupled Autoencoder Residuals:** Naively replacing PCA with an Autoencoder in a standard two-stage StatArb pipeline produces negative returns (Sharpe -0.29 to -0.18 for Option 1). Non-linear autoencoders trained strictly on reconstruction error do not inherently extract mean-reverting residuals.
2. **Extreme Turnover Drag:** The end-to-end policy retrains daily without an explicit turnover penalty. A portfolio of ~1,470 stocks whose weights are reshuffled daily by an unregularized $\tanh$ layer generates high turnover. The primary authors explicitly warn that without turnover penalties or smoothing layers, transaction costs will severely degrade net performance.
3. **Absence of Net-of-Cost Evaluation:** The primary paper reports zero transaction cost, slippage, or bid-ask spread simulations. For high-turnover daily statistical arbitrage, gross returns of 6.24% with 3.46% volatility can be completely eliminated by 10 bps round-trip friction.
4. **Computational Complexity of Daily Retraining:** Fitting a full autoencoder with $W^{(2)} \in \mathbb{R}^{N \times N}$ ($1,470 \times 1,470 \approx 2.16$ million weights) for 10 epochs every single trading day across 5,787 days requires massive GPU infrastructure and risks overfitting small sample regimes.

## Falsification plan

1. **Transaction Cost & Turnover Attrition Test:**
   Apply realistic execution costs to the daily rebalanced portfolio: 5 bps, 10 bps, and 20 bps round-trip per traded dollar.
   - `research-defined falsification threshold`: If the net annualized Sharpe ratio drops below 0.50 under a conservative 10 bps round-trip cost assumption, the end-to-end policy is falsified as an economically tradable standalone equity strategy.
2. **1-Bar Execution Delay (Next-Day Open vs. Close):**
   The primary paper assumes positions are taken at the beginning of day $t+1$ and capture full $t+1$ close-to-close returns. Re-run execution using next-day VWAP or market-on-open (MOO) prices with an enforced 30-minute execution lag.
   - `research-defined falsification threshold`: If post-lag net Sharpe drops by more than 50% relative to the simultaneous execution baseline, the apparent alpha is rejected as an artifact of execution timing look-ahead.
3. **Retraining Frequency Degradation (Weekly vs. Daily):**
   Compare daily retraining against weekly (5-day) and monthly (21-day) retraining schedules while keeping daily forward inference.
   - `research-defined falsification threshold`: If weekly retraining reduces gross annualized return by more than 40%, the strategy relies on transient overfitting to daily return noise rather than persistent structural factor relationships.
4. **Shuffled Cross-Section Placebo Test:**
   Randomly permute the cross-sectional return vector $Z_t$ across stocks before feeding it into the Autoencoder policy network, destroying contemporaneous factor correlation while preserving individual asset return distributions.
   - `research-defined falsification threshold`: If the placebo model achieves an out-of-sample Sharpe ratio exceeding 0.40, the policy optimization is falsified as fitting spurious statistical artifacts.
5. **Ablation of Idiosyncratic Skip-Layer:**
   Remove the skip-connection $\hat{Z}_t - Z_t$ and feed raw decoded factors $\hat{Z}_t$ or latent representation $F_t$ directly into the policy layer $w_t = \tanh(W^{(2)} F_t)$.
   - `research-defined falsification threshold`: If the network without the residual skip-layer achieves comparable or higher Sharpe, the hypothesis that the strategy harvests *mean-reverting idiosyncratic residuals* is falsified in favor of generic factor momentum/beta timing.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`. The primary paper evaluates exclusively US equities from 2000 to 2022. The application of end-to-end autoencoder policies to crypto assets is an unproven research interpretation.
- **Crypto Market Structure Adaptations:**
  - *Universe Selection*: In equities, the authors utilize an average of 1,470 stocks. In crypto, the liquid universe of perpetual futures on top exchanges (Binance, Bybit, OKX) is restricted to approximately 50 to 150 assets with reliable liquidity. A policy layer with $N \approx 100$ requires estimating only $100 \times 100 = 10,000$ policy weights, drastically reducing parameter count and overfitting risk.
  - *Continuous 24/7 Trading & Intraday Horizon*: Equities feature discrete overnight gaps and 16:00 EST market closes. In crypto, mean-reversion horizons are significantly shorter (hours rather than days). The architecture should be adapted to 1-hour or 4-hour bar aggregations:
    $$Z_{i, t} = \frac{r_{i, t}^{\text{4h}} - \mu_i^{\text{4h}}}{\sigma_i^{\text{4h}}}$$
  - *Perpetual Futures Funding Rate Drag*: In crypto perpetuals, long and short positions pay or receive funding every 8 hours. Holding persistent directional positions in high-funding altcoins generates severe negative drift. The loss function must be modified to include funding-adjusted returns:
    $$r_{p,t}^{\text{crypto}} = \sum_{i=1}^N w_{i,t} \left( r_{i,t+1} - \text{FundingRate}_{i,t} \right) \quad (\text{research-proposed})$$
  - *Cross-Sectional Market Beta Dominance*: In crypto, Bitcoin and Ethereum typically drive 60–80% of total market variance. A small latent bottleneck ($l = 3$ to $l = 5$) will primarily capture market-wide BTC/ETH movements, allowing the residual layer $\hat{Z}_t - Z_t$ to isolate pure token-specific idiosyncratic mean reversion.

## Limitations

- `not independently reproduced`: Primary results are transcribed directly from Krause & Calliess (2024); independent verification on raw tick/CRSP data has not been performed.
- `gross return reporting gap`: The primary study completely omits transaction costs, execution commissions, and bid-ask spreads, presenting a major provenance gap for real-world viability.
- `high turnover sensitivity`: Daily portfolio rebalancing without turnover regularization creates extreme turnover that could eliminate gross alpha.
- `high parameter dimensionality`: The unconstrained dense policy weight matrix $W^{(2)} \in \mathbb{R}^{N \times N}$ scales quadratically with universe size $N^2$. For $N = 1,470$, this introduces over 2.1 million parameters in the policy layer alone, requiring strong regularization or low-rank factorizations to prevent overfitting.
- `unproven in crypto`: Transferability to 24/7 crypto perpetual futures with funding rates and liquidation cascades is completely unverified empirically.

## Implementation status

- `not-implemented`: This research capture does not modify `nautilus-quant-system`, create PyBroker/Nautilus strategy families, or authorize paper, testnet, or live trading.
- All mathematical rules, loss equations, and empirical tables reflect direct extraction from the primary text and LaTeX source of Krause & Calliess (`arXiv:2402.08233v1`, 2024).

## Adoption boundary

- `status`: `research-only`
- `adoption`: `not-approved`
- `approval_scope`: `research-only`
- Research capture is strictly separated from trading authorization. This strategy record is staged exclusively for ChatGPT Research Intake Review and downstream hypothesis generation; it is not approved for execution, capital allocation, or paper trading.

## Related Wiki records

- `[[quant/moving-band-statistical-arbitrage-convex-concave-markowitz-2026-09-05]]`
- `[[quant/statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05]]`
- `[[quant/sponge-graph-clustering-ensemble-signal-quality-statistical-arbitrage-2026-09-05]]`
- `[[quant/statistical-arbitrage-rank-space-cnn-transformer-hybrid-atlas-2026-09-02]]`
- `[[quant/cross-asset-futures-vsn-xlstm-sharpe-optimal-portfolio-2026-09-03]]`
- `[[quant/strategy-research-record-spec-v1]]`

## Sources

1. **Fabian Krause and Jan-Peter Calliess**, *"End-to-End Policy Learning of a Statistical Arbitrage Autoencoder Architecture"*, arXiv preprint `arXiv:2402.08233v1 [cs.LG]`, February 13, 2024. Accepted to ICML 2024.
   - Canonical URL: [https://arxiv.org/abs/2402.08233](https://arxiv.org/abs/2402.08233)
   - DOI: [https://doi.org/10.48550/arXiv.2402.08233](https://doi.org/10.48550/arXiv.2402.08233)
   - Full-Text HTML: [https://arxiv.org/html/2402.08233v1](https://arxiv.org/html/2402.08233v1)
2. **Marco Avellaneda and Jeong-Hyun Lee**, *"Statistical Arbitrage in the US Equities Market"*, *Quantitative Finance*, Vol. 10, No. 7, pp. 761–782, 2010. [https://doi.org/10.1080/14697680903124632](https://doi.org/10.1080/14697680903124632)
3. **Eugene F. Fama and Kenneth R. French**, *"Common Risk Factors in the Returns on Stocks and Bonds"*, *Journal of Financial Economics*, Vol. 33, No. 1, pp. 3–56, 1993. [https://doi.org/10.1016/0304-405X(93)90023-5](https://doi.org/10.1016/0304-405X(93)90023-5)
4. **Erkki Oja**, *"Simplified Neuron Model as a Principal Component Analyzer"*, *Journal of Mathematical Biology*, Vol. 15, No. 3, pp. 267–273, 1982. [https://doi.org/10.1007/BF00275687](https://doi.org/10.1007/BF00275687)
