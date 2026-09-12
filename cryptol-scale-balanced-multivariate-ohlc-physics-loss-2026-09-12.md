---
schema: strategy-research-record-v1
title: "CryptoL: Scale-Balanced Multivariate OHLC Cryptocurrency Forecasting via Two-Phase RevIN, Channel-Dependent Affine Normalization, and Physics-Constrained Candle Loss"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cryptocurrency
  - multivariate-time-series
  - foundation-models
  - revin
  - physics-informed-ml
  - ohlc-constraints
  - scale-heterogeneity
status: research-only
confidence: high
source_as_of: 2026-09-11
sources:
  - "https://arxiv.org/abs/2609.11206"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# CryptoL: Scale-Balanced Multivariate OHLC Cryptocurrency Forecasting via Two-Phase RevIN, Channel-Dependent Affine Normalization, and Physics-Constrained Candle Loss

## Provenance

- **Primary Source:** Yalda Taheri, Mohammad Hassan Heydari, Armon Rasooli, Maryam Amirshahkarami, Mohammad Ebrahim Mahdavi, and Hossein Karshenas (Department of Computer Science and Engineering, Sharif University of Technology; School of Electrical and Computer Engineering, College of Engineering, University of Tehran; and Department of Computer Science, University of Texas at Dallas).
- **Publication & Version:** arXiv preprint `arXiv:2609.11206v1 [cs.AI, cs.CE, cs.LG]`, submitted September 2026, listed September 11, 2026 (`source-reported`).
- **Stable Identifiers:**
  - Stable arXiv Abstract: [https://arxiv.org/abs/2609.11206](https://arxiv.org/abs/2609.11206)
  - Full-Text HTML: [https://arxiv.org/html/2609.11206v1](https://arxiv.org/html/2609.11206v1)
  - Full-Text PDF: [https://arxiv.org/pdf/2609.11206v1](https://arxiv.org/pdf/2609.11206v1)
  - Canonical DOI: [10.48550/arXiv.2609.11206](https://doi.org/10.48550/arXiv.2609.11206)
- **Primary Source Verification:** All mathematical derivations, loss formulations, configuration parameters, and empirical baseline comparisons (Timer, Timer-XL, Time-MoE across 16 Binance cryptocurrency assets spanning 15.5 million observations) were retrieved and inspected directly from the primary preprint text and mathematical appendices.
- **Repository Deduplication Audit:** A comprehensive search of all existing records in `alpha-strategy-research` confirmed zero matching records for `arXiv:2609.11206`, "CryptoL", Yalda Taheri, or Mohammad Hassan Heydari. Prior foundation model and deep learning captures in the repository (e.g., `frozen-timesfm-hybrid-bilinear-residual-learning-2026-09-12.md`, `chronos-foundation-transformer-factor-residual-stat-arb-2026-09-11.md`, `strata-selective-state-space-intraday-raw-bars-cross-sectional-ranking-2026-09-02.md`) explore uni-dimensional price forecasting or zero-shot time-series foundation models; none formulate scale-balanced two-phase instance normalization across 12 orders of magnitude of crypto quoted values, channel-dependent order-preserving affine transforms, or normalized-space candlestick inequality constraints.

## Economic mechanism

### Source-reported

1. **Cross-Asset Scale Heterogeneity and Optimization Domination:**
   Cryptocurrency markets exhibit extreme cross-sectional nominal price dispersion. Within a single shared trading universe, quoted prices range from micro-penny tokens ($10^{-7}$ for meme coins such as PEPE) to large-cap assets ($10^5$ for Bitcoin). When multi-asset deep learning models or time-series foundation models are trained jointly across the universe using standard Mean Squared Error (MSE), high-priced assets generate gradients that are orders of magnitude larger than those of low-priced assets.
2. **The RevIN Inverse-Normalization Distortion Trap:**
   Reversible Instance Normalization (RevIN; Kim et al., 2021) standardizes input sequences $\mathbf{X}_n$ by removing context mean $\bm{\mu}_n$ and scaling by standard deviation $\mathbf{S}_n = \text{diag}(s_{n,c})$. However, standard RevIN practices restore predictions to physical units ($\widehat{\mathbf{Y}}_n = \mathbf{1}_H \bm{\mu}_n^\top + \widehat{\mathbf{Z}}_n \mathbf{S}_n$) *before* computing the training loss. The resulting objective:
   $$\mathcal{L}_{\text{R}}(\bm{\theta}) = \frac{1}{2N} \sum_{n=1}^N \|\widehat{\mathbf{Y}}_n - \mathbf{Y}_n\|_F^2 = \frac{1}{2N} \sum_{n=1}^N \|(\widehat{\mathbf{Z}}_n - \mathbf{Z}_n)\mathbf{S}_n\|_F^2$$
   mechanically re-introduces an explicit squared scale factor $s_{n,c}^2 \approx \sigma_{n,c}^2$ into the parameter gradient. As proven in the paper's Hessian and Jacobian analysis (Theorems B.14–B.18), this scales the condition number of the Gauss-Newton curvature matrix by:
   $$\kappa(\mathbf{G}^{\text{Raw}}) = \frac{\max_a \pi_a s_a^2 \lambda_a}{\min_a \pi_a s_a^2 \lambda_a} \gg \kappa(\mathbf{G}^{\text{TP}}) = \frac{\max_a \pi_a \lambda_a}{\min_a \pi_a \lambda_a}$$
   starving low-priced assets of parameter updates and causing optimization instability.
3. **Channel-Independent vs. Channel-Dependent Normalization and Order Inversion:**
   Candlestick data possesses strict geometric properties: by definition, $\text{High} \ge \text{Open}$, $\text{High} \ge \text{Close}$, $\text{Low} \le \text{Open}$, and $\text{Low} \le \text{Close}$. Standard channel-independent (CI) RevIN applies separate affine transforms to Open, High, Low, and Close using individual channel statistics $(\mu_c, s_c)$. Because $s_{\text{Open}} \ne s_{\text{High}} \ne s_{\text{Low}} \ne s_{\text{Close}}$, CI normalization violates order preservation in normalized space: a valid physical candle can become an inverted, invalid candle in normalized latent space. Channel-dependent (CD) normalization computes a single joint mean and variance across both time and the four OHLC channels, guaranteeing that affine order relations are strictly preserved.
4. **Physical Candlestick Feasibility and Constraint Degradation:**
   Unconstrained neural network forecasting models regularly generate physically impossible candles (e.g., predicted Low > predicted High or predicted Close > predicted High). Structural post-processing approaches (such as the unconstrained space projection by Wang et al., 2021) mathematically enforce validity but degrade forecasting accuracy by orders of magnitude (exploding MAE from 34.77 to 3307.53). CryptoL resolves this dilemma by introducing a normalized-space soft auxiliary penalty that penalizes geometric violations directly during gradient descent.

### Research interpretation

- **Multi-Asset Cross-Learning Without Scale Distortion:**
  In quantitative crypto research, training individual isolated models for every token prevents the architecture from learning universal market dynamics (e.g., market-wide liquidation cascades, volatility spikes, and cross-asset beta propagation). However, joint training traditionally failed because BTC and ETH monopolized parameter updates. Two-Phase RevIN (TP-RevIN) allows shared foundation backbones to learn joint representations while treating every token's standardized variance equally.
- **Structural Priors as Regularization Against Overfitting:**
  Penalizing candlestick geometric violations acts as an inductive bias that constrains the neural hypothesis space. Rather than memorizing unconstrained trajectory noise, the network is forced to find trajectories whose intra-bar extreme excursions (High/Low) remain envelope-consistent with end-of-bar boundaries (Open/Close).
- **Scale-Invariant Microstructure Signal Construction:**
  Dynamic epsilon ($\epsilon^{\text{dyn}} \propto \mu^2$) guarantees that numerical stabilizers do not distort low-priced altcoins, ensuring that generated forecast returns $\widehat{R}_{i, t, H} = (\widehat{C}_{i, t+H} - C_{i, t}) / C_{i, t}$ reflect genuine predicted drift rather than floating-point artifacts.

## Signal

The primary source establishes the multi-channel forecasting architecture; the explicit trading signal rules, entry triggers, position allocation, and portfolio rebalancing schedule below are formulated as a standardized systematic trading strategy (`research-proposed`):

### 1. Data Ingestion & Context Formation
- **Sampling Frequency:** Evaluated across 5m, 15m, 30m, 1h, 2h, 4h, and 1d intervals (`source-reported`). Base operational execution uses 30m or 1h candle bars (`research-proposed`).
- **Lookback Window:** Context window length $L = 96$ bars (for standard forecasting) or $L = 480$ bars (for multi-horizon physical consistency evaluations) (`source-reported`).
- **Channel Vector:** At each bar timestamp $t$, input matrix $\mathbf{X}_{i, t} \in \mathbb{R}^{L \times 4}$ consists of $[O_{i, \tau}, H_{i, \tau}, L_{i, \tau}, C_{i, \tau}]$ for $\tau \in [t - L + 1, t]$.

### 2. Normalization & Dynamic Epsilon
- **Shared Sample Statistics (CD Mode):**
  $$\mu_{i, t}^{\text{CD}} = \frac{1}{4L} \sum_{\tau=1}^L \sum_{c=1}^4 X_{i, \tau, c}, \qquad v_{i, t}^{\text{CD}} = \frac{1}{4L} \sum_{\tau=1}^L \sum_{c=1}^4 \left(X_{i, \tau, c} - \mu_{i, t}^{\text{CD}}\right)^2$$
- **Dynamic Numerical Stabilizer:**
  $$\epsilon_{i, t}^{\text{dyn}} = 10^{-5} \left( (\mu_{i, t}^{\text{CD}})^2 + 10^{-12} \right)$$
  $$s_{i, t}^{\text{CD}} = \sqrt{v_{i, t}^{\text{CD}} + \epsilon_{i, t}^{\text{dyn}}}$$
- **Normalized Context:**
  $$\widetilde{\mathbf{X}}_{i, t} = \frac{\mathbf{X}_{i, t} - \mu_{i, t}^{\text{CD}}\mathbf{1}_L \mathbf{1}_4^\top}{s_{i, t}^{\text{CD}}}$$

### 3. Forecasting Inference & Physical Restitution
- **Forward Pass:** The decoder backbone (Timer-XL or Time-MoE) produces normalized predictions for horizon $H \in \{5, 15, 30\}$ steps:
  $$\widehat{\mathbf{Z}}_{i, t} = f_{\bm{\theta}}(\widetilde{\mathbf{X}}_{i, t}) \in \mathbb{R}^{H \times 4}$$
- **Physical Scale Restoration (Inference Phase):**
  $$\widehat{\mathbf{Y}}_{i, t} = \mu_{i, t}^{\text{CD}}\mathbf{1}_H \mathbf{1}_4^\top + \widehat{\mathbf{Z}}_{i, t} \cdot s_{i, t}^{\text{CD}}$$
  yielding forecast paths $[\widehat{O}_{i, t+\tau}, \widehat{H}_{i, t+\tau}, \widehat{L}_{i, t+\tau}, \widehat{C}_{i, t+\tau}]$ for $\tau \in \{1, \dots, H\}$.

### 4. Alpha Signal Generation (`research-proposed`)
- **Directional Expected Return:**
  $$\widehat{r}_{i, t, H} = \frac{\widehat{C}_{i, t+H} - C_{i, t}}{C_{i, t}}$$
- **Candlestick Validity Quality Filter (PHY Gate):**
  $$\text{PHY}_{i, t} = \frac{1}{H} \sum_{\tau=1}^H \Bigl( [\widehat{O}_{i, \tau} - \widehat{H}_{i, \tau}]_+ + [\widehat{C}_{i, \tau} - \widehat{H}_{i, \tau}]_+ + [\widehat{L}_{i, \tau} - \widehat{O}_{i, \tau}]_+ + [\widehat{L}_{i, \tau} - \widehat{C}_{i, \tau}]_+ + [\widehat{L}_{i, \tau} - \widehat{H}_{i, \tau}]_+ \Bigr)$$
  If $\text{PHY}_{i, t} > \theta_{\text{phy}}$ (where $\theta_{\text{phy}} = 0.01$ in normalized units, `research-proposed`), the asset's prediction is flagged as physically deformed, and its trade allocation is zeroed for the current rebalance (`research-proposed`).

### 5. Cross-Sectional Portfolio Construction (`research-proposed`)
- **Eligible Universe:** Binance perpetual futures contracts passing liquidity screens (median 30-day volume > $20M).
- **Ranking & Sizing:**
  - Rank all candidate tokens cross-sectionally by $\widehat{r}_{i, t, H}$.
  - **Long Basket:** Top quintile ($Q_5$) if $\widehat{r}_{i, t, H} > +1.0\%$.
  - **Short Basket:** Bottom quintile ($Q_1$) if $\widehat{r}_{i, t, H} < -1.0\%$.
  - **Weights:** Inverse-volatility weighted or equal-weighted within quintile baskets, normalized to target 100% gross exposure (dollar-neutral long/short).
- **Holding Period:** Rebalance every $H$ bars (e.g., every 5 bars = 2.5 hours on 30m candles, or held until sign reversal / stop trigger) (`research-proposed`).

## Required data

- **Instruments:** 16 liquid cryptocurrency assets evaluated in the source: `ADAUSDT`, `BCHUSDT`, `BNBUSDT`, `BTCUSDT`, `DOGEUSDT`, `ETHUSDT`, `LINKUSDT`, `LTCUSDT`, `PEPEUSDT`, `SHIBUSDT`, `SOLUSDT`, `SUIUSDT`, `TONUSDT`, `TRXUSDT`, `XLMUSDT`, `XRPUSDT` (`source-reported`).
- **Venue:** Binance Spot / Perpetual Futures (`source-reported`).
- **Temporal Resolution:** OHLC bar data sampled at 5m, 15m, 30m, 1h, 2h, 4h, 1d intervals (`source-reported`).
- **Required Fields:** `open`, `high`, `low`, `close`, `timestamp` (`source-reported`).
- **Point-in-Time Availability:** Strictly bar-close synchronized; forecasts for $[t+1, t+H]$ are generated using closed bar data through timestamp $t$. No future leak across lookback boundaries.
- **Data Volume:** Approximately 15,487,000 observations across all 16 assets and 7 resolutions (`source-reported`).

## Execution assumptions

- **Execution Timing:** Market or limit orders placed at the open of bar $t+1$ following model inference at the close of bar $t$ (`research-proposed`).
- **Execution Cost:** Assumed taker fee of 4 bps (0.04%) per trade with an estimated 3 bps slippage buffer (total round-trip friction 14 bps) (`research-proposed`).
- **Shorting Mechanism:** Evaluated on USDT perpetual futures contracts; borrow/shorting is native with 8-hour funding rates accounted for (`research-proposed`).
- **Participation & Liquidity:** Position sizing capped at $\le 1.0\%$ of 30-minute bar volume to prevent adverse market impact on mid-cap tokens (`research-proposed`).
- **Source Gap:** The primary paper evaluates predictive error metrics (MSE, MAE, MAPE, PHY violation rate) across model backbones; it does not simulate an order-level backtest with fee schedules or slippage models (`source-gap`).

## Evidence

### Source-reported

All empirical figures below trace directly to the audited text and tables of Taheri et al. (`arXiv:2609.11206v1`, Tables 1, 2, 3, 4, 10):

1. **Failure of Raw Price Training (Scale Collapse):**
   - In Table 1 and Table 10, models trained without RevIN (`w/o RevIN`) completely fail:
     - 5m timeframe, Horizon 5: Time-MoE MSE $= 5.7 \times 10^8$, MAE $= 6325.3$, PHY $= 1.312$; Timer-XL MSE $= 5.2 \times 10^8$, MAE $= 6571.64$, PHY $= 5.536$.
     - 30m timeframe, Horizon 5: Timer-XL MSE $= 7.66 \times 10^8$, MAE $= 8367.45$.
     - Optimization is dominated entirely by BTC/ETH price scales, yielding massive forecast errors for lower-priced coins.
2. **Superiority of Two-Phase RevIN (TP-RevIN):**
   - On the 5m timeframe at Horizon 5:
     - Time-MoE with standard CI RevIN: MSE $= 9890.9$, MAE $= 19.03$, PHY $= 0.0040$.
     - Time-MoE with Two-Phase CI RevIN: MSE $= 6610.0$ (-33.2%), MAE $= 15.25$ (-19.9%), PHY $= 0.0010$ (-75.0%).
   - On the 30m timeframe at Horizon 15:
     - Time-MoE standard CI RevIN: MSE $= 1.56 \times 10^5$, MAE $= 86.77$.
     - Time-MoE Two-Phase CI RevIN: MSE $= 1.14 \times 10^5$ (-26.9%), MAE $= 72.48$ (-16.5%).
     - Timer-XL standard CI RevIN: MSE $= 8.29 \times 10^4$, MAE $= 59.11$.
     - Timer-XL Two-Phase CI RevIN: MSE $= 7.34 \times 10^4$ (-11.5%), MAE $= 55.10$ (-6.8%).
3. **Meme-Coin Dynamic Epsilon Breakthrough (Table 3):**
   - Under standard fixed epsilon ($\epsilon^{\text{fix}} = 10^{-5}$), small-scale coins suffer catastrophic percentage error:
     - SHIB (Time-MoE, RevIN): Horizon 5 / 30 MAPE $= 17,362.6\% / 12,894.9\%$.
     - SHIB (Timer-XL, RevIN): Horizon 5 / 30 MAPE $= 181.5\% / 3,003.3\%$.
     - SHIB (Timer, RevIN): Horizon 5 / 30 MAPE $= 471.4\% / 5,346.9\%$.
   - Replacing fixed epsilon with Dynamic Epsilon ($\epsilon^{\text{dyn}} = 10^{-5}(\mu^2 + 10^{-12})$) eliminates the distortion:
     - SHIB (Time-MoE, RevIN): MAPE drops to $1.89\% / 4.12\%$.
     - SHIB (Timer-XL, RevIN): MAPE drops to $1.48\% / 3.20\%$.
     - SHIB (Timer, RevIN): MAPE drops to $1.45\% / 2.97\%$.
     - Combining TP-RevIN with Dynamic Epsilon yields the best overall performance: Time-MoE SHIB MAPE $= 1.87\% / 3.51\%$; Timer-XL SHIB MAPE $= 1.40\% / 2.74\%$; Timer SHIB MAPE $= 1.38\% / 2.72\%$.
4. **Physical Constraint Loss vs. Unconstrained Structural Projection (Table 4):**
   - The "Unconstrained Space" projection baseline (Wang et al., 2021) achieves $\text{PHY} = 0.0$ by structural construction, but destroys predictive accuracy:
     - Timer-XL (30m, Horizon 5): MAE $= 3307.53$ (compared to $34.77$ for TP-RevIN CI).
     - Timer-XL (1h, Horizon 5): MAE $= 1492.80$ (compared to $52.10$ for TP-RevIN CI).
   - In contrast, TP-RevIN trained with normalized-space auxiliary physics loss ($\mathcal{L}_{\text{phy}}$) reduces physical violations to near zero ($\text{PHY} = 2.0 \times 10^{-6}$ for 30m H5; $\text{PHY} = 1.0 \times 10^{-7}$ for 1h H5) while maintaining superior MAE ($34.77$ and $52.10$).

### Independently reproduced

`not independently reproduced`. All metrics and empirical ablation results cited above represent third-party empirical findings reported by Taheri et al. (`arXiv:2609.11206v1`).

### Negative evidence

- **Horizon Decay:** Forecasting error escalates rapidly as horizon extends from $H = 5$ to $H = 30$ bars. For example, Timer-XL 1h MAE increases from $52.10$ ($H=5$) to $105.5$ ($H=30$).
- **Channel-Dependent vs. Channel-Independent Tradeoff:** While CD normalization mathematically guarantees candle order preservation ($L \le O, C \le H$), CI normalization frequently achieves marginally lower MSE/MAE in unconstrained evaluations because it allows the model greater degrees of freedom across channels.
- **Computational Overhead:** Training large decoder-only foundation models (Timer-XL, Time-MoE) requires significant GPU compute (tested on NVIDIA RTX 3090 / A100 infrastructure), making real-time sub-minute retraining challenging without pre-computed frozen checkpoints.

## Falsification plan

To falsify the hypothesis that CryptoL provides genuine predictive edge and structurally superior multi-asset crypto signals:

1. **Information Coefficient (IC) Decay Test:**
   - *Protocol:* Compute the rank information coefficient (Spearman Rank IC) between predicted forward return $\widehat{r}_{i, t, H}$ and realized return $r_{i, t, H}$ across the 16-asset universe over a 12-month walk-forward out-of-sample window.
   - *Decision Rule (`research-defined falsification threshold`):* If mean Rank IC is less than $+0.02$ or Rank IC IR (mean/std) is less than $0.5$, the directional predictive edge is falsified.
2. **Transaction Cost Attrition Gate:**
   - *Protocol:* Simulate the quintile long/short strategy with realistic Binance VIP-0 taker fees (4 bps) and market slippage (3 bps).
   - *Decision Rule (`research-defined falsification threshold`):* If net annualized Sharpe ratio after costs drops below $0.0$, the strategy fails the tradability gate.
3. **Ablation vs. Simple Cross-Sectional Momentum Baseline:**
   - *Protocol:* Compare the net performance of CryptoL against a simple trailing 96-bar return cross-sectional momentum benchmark.
   - *Decision Rule (`research-defined falsification threshold`):* If the complex foundation model does not achieve a statistically significant Sharpe improvement ($p < 0.05$ under block-bootstrap testing) over the simple momentum benchmark, the complex model's economic contribution is falsified.
4. **Candle Feasibility Degradation Test:**
   - *Protocol:* Monitor real-time inference candle violation rate $\text{PHY}_{i, t}$.
   - *Decision Rule (`research-defined falsification threshold`):* If more than $5\%$ of generated forward paths violate basic OHLC inequality constraints ($\text{PHY} > 0.05$), the physics-informed constraint loss is considered ineffective.

## Crypto portability

- **Portability Status:** `direct`.
- **Rationale:** The entire methodology, dataset, and empirical evaluation in `arXiv:2609.11206v1` are native to cryptocurrency assets (16 Binance spot and perpetual pairs from 2017 to 2025).
- **Perpetual Futures Integration:**
  - *Funding Rate Friction:* Perpetual swap holding costs must be deducted from multi-day horizon holding returns.
  - *24/7 Continuous Session:* Crypto markets lack opening/closing auction gaps; dynamic context windows $L=96$ or $L=480$ slide continuously across midnight UTC boundaries.
  - *Extreme Scale Range:* The dynamic epsilon formulation ($\epsilon^{\text{dyn}}$) is essential for crypto universes containing both mega-cap coins ($BTC \approx \$60,000$) and micro-tokens ($PEPE \approx \$0.00001$).

## Limitations

- **Source Gap on Order-Level Backtesting:** The primary source is a computer science machine learning paper focusing on time-series forecasting metrics (MSE, MAE, MAPE, PHY violation rate); it does not include an explicit financial portfolio backtest, Sharpe ratio, or drawdown accounting (`source-gap`).
- **High Computational Latency:** Generating full autoregressive decoder predictions across an entire exchange universe requires inference infrastructure that may exceed latency budgets for high-frequency execution.
- **Hyperparameter Sensitivity of $\lambda_{\text{phy}}$:** The balance between pure MSE minimization and candle geometric feasibility depends on tuning $\lambda_{\text{phy}}$. Excessive penalty weights degrade MAE, while insufficient weights allow inverted candles.

## Implementation status

`not-implemented`. This record represents an upstream research capture. No code has been merged into `nautilus-quant-system`, PyBroker, or NautilusTrader, and no live or testnet execution is active.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- **Boundary Notice:** Presence of this record in the repository does not constitute approval for live capital deployment, testnet execution, or paper trading. Any subsequent implementation requires independent validation and formal approval.

## Related Wiki records

- `[[quant/sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12]]` — Multivariate relative value and structural time-series modeling.
- `[[quant/frozen-timesfm-hybrid-bilinear-residual-learning-2026-09-12]]` — Foundation model adaptation for financial time-series forecasting.
- `[[quant/chronos-foundation-transformer-factor-residual-stat-arb-2026-09-11]]` — Pretrained probabilistic transformer backbones and turnover-cost fragility.
- `[[quant/strata-selective-state-space-intraday-raw-bars-cross-sectional-ranking-2026-09-02]]` — State-space neural sequence processing of intraday raw bars.

## Sources

1. Yalda Taheri, Mohammad Hassan Heydari, Armon Rasooli, Maryam Amirshahkarami, Mohammad Ebrahim Mahdavi, and Hossein Karshenas. *"CryptoL: Towards Scale Dominance and Physics Constraints Mitigation in Financial Multivariate Time Series Forecasting."* arXiv preprint `arXiv:2609.11206v1 [cs.AI, cs.CE, cs.LG]`, submitted September 2026, listed September 11, 2026.
   - Stable arXiv URL: [https://arxiv.org/abs/2609.11206](https://arxiv.org/abs/2609.11206)
   - HTML version: [https://arxiv.org/html/2609.11206v1](https://arxiv.org/html/2609.11206v1)
   - PDF version: [https://arxiv.org/pdf/2609.11206v1](https://arxiv.org/pdf/2609.11206v1)
   - Canonical DOI: [10.48550/arXiv.2609.11206](https://doi.org/10.48550/arXiv.2609.11206)
2. Taeyoung Kim, Jinhee Kim, Yunwon Tae, Cheonbok Park, Jin-Hwa Choi, and Jaegul Choo. *"Reversible Instance Normalization for Accurate Time-Series Forecasting against Distribution Shift."* In *International Conference on Learning Representations (ICLR)*, 2022.
3. Yong Liu, Tengge Hu, Haoran Zhang, Hengdong Wu, Shiyu Wang, Lintao Ma, and Mingsheng Long. *"Timer: Transformers for Large-scale Time Series Pre-training."* In *International Conference on Machine Learning (ICML)*, 2024.
4. Yong Liu, Haoran Zhang, Chenyu Li, Xiangdong Huang, Jianmin Wang, and Mingsheng Long. *"Timer-XL: Long-Context Transformers for Unified Time Series Forecasting."* *arXiv preprint arXiv:2410.04801*, 2025.
5. Xiaoming Shi, Shiyu Wang, Zhengyang Zhou, Pengkun Wang, and Yang Chen. *"Time-MoE: Billion-Scale Time Series Foundation Models with Mixture of Experts."* *arXiv preprint arXiv:2409.16040*, 2025.
6. Dawei Wang, Jinwen Zhang, and Yunjun Gao. *"Forecasting the Candlestick Signals with Unconstrained Spaces."* In *IEEE Transactions on Knowledge and Data Engineering*, 2021.
