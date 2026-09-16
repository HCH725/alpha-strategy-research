---
schema: strategy-research-record-v1
title: "EXAONE Finance 1.0: Attention-Free Causal Convolution and Group-Aware Pooling Time Series Foundation Model (Lee et al. 2026)"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - foundation-model
  - time-series
  - attention-free
  - causal-convolution
  - group-pooling-mlp
  - finverse
  - cross-sectional-ranking
  - portfolio-backtest
status: research-only
confidence: high
source_as_of: 2026-09-08
sources:
  - "Seunghan Lee, Jaehoon Lee, Jun Seo, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Minjae Kim, Sungdong Yoo, Junhyeok Kang, Sangjun Han, Soonyoung Lee, and Wonbin Ahn, 'EXAONE Finance 1.0: An Attention-free Time Series Foundation Model for Financial Time Series', arXiv preprint arXiv:2609.04239v2 [cs.AI, cs.LG], revised September 8, 2026 (v1 submitted September 4, 2026). DOI: 10.48550/arXiv.2609.04239. https://arxiv.org/abs/2609.04239"
  - "LGAI-Research, 'EXAONE-Forecast', official open-source code repository, LG AI Research, 2026. https://github.com/LGAI-Research/EXAONE-Forecast"
  - "LG AI Research, 'EXAONE-Finance-1.0', model weights on Hugging Face, 2026. https://huggingface.co/LG-AI-Research/EXAONE-Finance-1.0"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# EXAONE Finance 1.0: Attention-Free Causal Convolution and Group-Aware Pooling Time Series Foundation Model (Lee et al. 2026)

## Provenance

- **Primary Source:** Seunghan Lee, Jaehoon Lee, Jun Seo, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Minjae Kim, Sungdong Yoo, Junhyeok Kang, Sangjun Han, Soonyoung Lee, and Wonbin Ahn (LG AI Research), *"EXAONE Finance 1.0: An Attention-free Time Series Foundation Model for Financial Time Series"*, arXiv preprint `arXiv:2609.04239v2 [cs.AI, cs.LG]`, revised September 8, 2026 (v1 submitted September 4, 2026) (`source-reported`).
  - Stable Abstract URL: https://arxiv.org/abs/2609.04239
  - Full-Text HTML URL: https://arxiv.org/html/2609.04239v2
  - Full-Text PDF URL: https://arxiv.org/pdf/2609.04239
  - Canonical DOI: [10.48550/arXiv.2609.04239](https://doi.org/10.48550/arXiv.2609.04239) (`source-reported`).
  - License: Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (`CC BY-NC-ND 4.0`).
- **Official Open-Source Artifacts:**
  - Official Code Repository: LG AI Research, `EXAONE-Forecast`, https://github.com/LGAI-Research/EXAONE-Forecast (`source-reported`).
  - Pretrained Model Weights: LG AI Research, `EXAONE-Finance-1.0`, Hugging Face Hub, https://huggingface.co/LG-AI-Research/EXAONE-Finance-1.0 (`source-reported`).
- **Primary Source Inspection:** Directly retrieved and verified against the full-text manuscript and mathematical formulations of `arXiv:2609.04239v2`. Every network parameter, operator equation, complexity bound, synthetic pretraining family, evaluation protocol tier, and comparative benchmark ranking traces directly to Sections 1 through 6, Equations (1) through (13), and Tables 1 through 7 of the primary text.
- **Repository Deduplication Audit:** Pre-write search across all 644 records in `alpha-strategy-research` confirmed zero existing records citing `arXiv:2609.04239`, EXAONE Finance, FinVerse, Seunghan Lee, or LG AI Research.

## Economic mechanism

### Source-reported

1. **Failure of General-Purpose Time Series Foundation Models (TSFMs) in Finance:**
   - General-domain TSFMs (e.g., Chronos, TimesFM, Moirai, Toto) rely on self-attention mechanisms whose computational complexity scales quadratically with sequence length $L$ ($\mathcal{O}(L^2 d)$) and variate count $C$ ($\mathcal{O}(C^2 d)$), making long, many-channel financial panels computationally intractable (`source-reported`).
   - General TSFMs assume contiguous, fully observed inputs and fail when confronted with market closures, trading halts, and unreported intervals (`source-reported`).
   - Standard TSFM pretraining corpora are dominated by non-financial physical and industrial datasets that under-represent heavy tails, low signal-to-noise ratios, volatility clustering, and regime shifts (`source-reported`).

2. **Attention-Free Linear-Time Architecture:**
   - EXAONE Finance replaces self-attention with two linear-time operators:
     - *Temporal Mixing:* A stack of causal 1D convolutions ($\mathcal{O}(L \cdot d \cdot c \cdot k)$) ensuring strictly causal time dependencies (`source-reported`).
     - *Variate Mixing:* A group-aware pooling multi-layer perceptron (MLP) ($\mathcal{O}(C \cdot d)$) that averages representations within predefined asset or channel groups ($\Gamma_{ij} = \mathbb{1}[g_i = g_j]$) to allow information sharing without order dependence (`source-reported`).
   - A masked-context augmentation ($\rho = 0.25$ contiguous masking) trains the network to forecast through missing observation spans without imputation (`source-reported`).

3. **Domain-Specific Synthetic Pretraining:**
   - EXAONE Finance is pretrained exclusively on synthetic financial time series generated by superimposing six families of empirical financial regularities: temporal dependence (trend, seasonality, ARMA, Ornstein-Uhlenbeck mean reversion, momentum, fractional Gaussian noise), conditional variance (base volatility, GARCH clustering, heteroskedasticity), marginal distributions (Student-$t$ fat tails, skewness, mixture-of-normals), discontinuities and regimes (compound-Poisson jumps, rare shocks, Markov-switching parameters, structural breaks), cross-series structure (factor models, dynamic conditional correlation, lead-lag, cointegration), and observation liquidity proxies (`source-reported`).
   - The model observes zero real historical market data during pretraining, mitigating historical path memorization (`source-reported`).

### Research interpretation

1. **Inductive Bias Against Overfitting Spurious Cross-Asset Correlations:**
   - In financial markets characterized by low signal-to-noise ratios, unconstrained all-to-all attention across asset channels ($C^2$ attention) readily fits transient in-sample correlations that rapidly decay out-of-sample. Group-aware pooling acts as a severe structural regularizer: assets interact only through their group mean, mirroring multi-factor pricing theory where idiosyncratic return residuals remain uncoupled while common factor shocks are pooled.
2. **Synthetic Priors Over Empirical Path Fitting:**
   - Pretraining on stochastic differential equations and econometric processes (GARCH, OU, jump-diffusion) instills an explicit prior for mean-reverting and heavy-tailed dynamics. This allows zero-shot transfer across asset classes because the network learns general structural invariants of financial mathematics rather than historical macro regimes that may never recur.
3. **Cross-Sectional Rank-Order Alpha:**
   - In cross-sectional portfolio construction (Tier 2 and Tier 3), absolute point forecast accuracy is secondary to relative rank fidelity. The model's median quantile forecast $\hat{y}_{q_{50}}$ provides a monotonic rank-ordering signal for cross-sectional relative value and momentum strategies.

## Signal

### Input Representation & Normalization (`source-reported`)

- **Context Window:** Length $L$ historical observations $\bm{x}^{\mathrm{ctx}} = (x_{t-L+1}, \dots, x_t) \in \mathbb{R}^L$ (`source-reported`).
  - Standard geometry: Daily $L=260$; Weekly $L=52$; Monthly $L=12$; Quarterly $L=4$; Annual $L=10$ (`source-reported`).
- **Instance Normalization:** Computed exclusively on non-missing historical observations (`source-reported`):
  $$\hat{\bm{x}} = \frac{\bm{x}^{\mathrm{ctx}} - \mu}{\sigma}$$
- **Heavy-Tail Compression:** Area hyperbolic sine transform (`source-reported`):
  $$\tilde{\bm{x}} = \operatorname{arcsinh}(\hat{\bm{x}})$$
  Compresses extreme tail outliers logarithmically while preserving sign and linear behavior near zero (`source-reported`).
- **Patch Embedding:** Non-overlapping patches of size $P=16$ (stride $P$) (`source-reported`). Each token concatenates relative time encoding $\bm{e}_\tau$, patched values $\tilde{\bm{x}}_\tau$, and observation mask $\bm{m}_\tau$ ($3P$ dimensions total), projected to model dimension $d=1024$ via residual MLP ($d_{\mathrm{ff}}=4096$) (`source-reported`).

### Architecture & Mixing Operators (`source-reported`)

- **Model Dimensions:** $N=12$ encoder blocks, hidden dimension $d=1024$, feed-forward dimension $d_{\mathrm{ff}}=4096$, dropout $0.1$, total parameter count $202\text{M}$ (`source-reported`).
- **Temporal Mixing (Causal 1D CNN):**
  - Convolution channels $c=512$, kernel size $k=7$, layers $n=2$ (`source-reported`).
  - Left-only padding of $k-1 = 6$ positions ensures strict causality ($\tau' \le \tau$) (`source-reported`):
    $$\bm{H}^{(l, \text{time})} = \bm{H}^{(l-1)} + \operatorname{Conv1D}_{1\times 1}\Big(\operatorname{CausalConv1D}_{k, c}\big(\operatorname{LN}(\bm{H}^{(l-1)})\big)\Big)$$
- **Variate Mixing (Group-Aware Pooling MLP):**
  - Maximum groups $G=16$, projection dimension $d_v=512$ (`source-reported`).
  - Group mask $\Gamma_{ij} = \mathbb{1}[g_i = g_j]$ (`source-reported`).
  - Group mean $\bar{\bm{H}}_i = \frac{1}{\sum_j \Gamma_{ij}} \sum_j \Gamma_{ij} \bm{H}_j$ (`source-reported`).
  - Representation augmented with group mean: $\bm{H}'_i = \bm{H}_i + \operatorname{MLP}([\bm{H}_i; \bar{\bm{H}}_i])$ (`source-reported`).
- **Forecasting Head:** Non-autoregressive residual MLP decoding last $\lceil H/P \rceil$ tokens into $Q=21$ quantiles: $\{0.01, 0.05, 0.1, \dots, 0.9, 0.95, 0.99\}$ (`source-reported`).
- **Decision Variable:** Median quantile forecast $\hat{y}_{q_{50}}$ evaluated across horizon $H$ (`source-reported`).

### Portfolio Strategy Rules

- **Predicted Change Metric (`source-reported`):**
  For asset $s$ at forecast origin $t$, evaluate the predicted relative change over horizon $h$:
  $$\Delta^{\mathrm{pred}}_s(t) = \frac{\hat{y}_{q_{50}, s, t+h} - x_{s, t}}{x_{s, t}}$$
  *(Note: In FinVerse Tier 1/2 change definitions, base value $x_{s, t-p}$ is measured $p$ periods prior; for real-time forward execution, $p=0$ / current close $x_{s, t}$ is `research-proposed`).*
- **Cross-Sectional Ranking (`source-reported`):** Rank all eligible universe assets descending by $\Delta^{\mathrm{pred}}_s(t)$.
- **Portfolio Construction (`source-reported`):** Select the Top-$K\%$ assets into an equal-weighted long-only basket.
  - *Top-$K\%$ cutoff:* Benchmark-defined in FinVerse; `research-proposed` default is $K=20\%$ (top quintile).
  - *Market-neutral extension (`research-proposed`):* Long Top-$K\%$ (highest predicted return) and short Bottom-$K\%$ (lowest predicted return), equal-weighted, dollar-neutral.
- **Holding Period & Rebalancing:** Rebalance cadence matches forecast horizon $h$ (e.g., $h=5$ days for short-term daily or $h=20$ days for monthly cycle) (`source-reported`).
- **Execution Timestamp (`research-proposed`):** Signal formed at completed bar close $t$; executable market or limit orders submitted for execution at bar $t+1$ open.

## Required data

- **Universe:** Cross-sectional asset panels across equities, exchange-traded funds (ETFs), foreign exchange (FX), commodities, crypto-assets, and fixed-income securities (`source-reported`).
- **Sampling Frequencies:** Daily ($L=260$, $H \in \{5, 20, 65, 130, 260\}$), Weekly ($L=52$, $H \in \{1, 4, 12, 26, 52\}$), Monthly ($L=12$, $H \in \{1, 3, 6, 12, 24\}$), Quarterly ($L=4$, $H \in \{1, 2, 4, 8\}$), Annual ($L=10$, $H \in \{1, 2, 5, 10\}$) (`source-reported`).
- **Input Channels:** Univariate price series or multi-channel grouped representations (e.g., Open, High, Low, Close, Volume for single assets, or joint asset panels) with associated binary observation mask $\bm{m} \in \{0, 1\}^L$ (`source-reported`).
- **Point-in-Time Discipline:** All context representations $\bm{x}^{\mathrm{ctx}}$ must terminate strictly at timestamp $t$. Instance normalization mean $\mu$ and scale $\sigma$ must be computed exclusively over historical context timestamps without future leakage (`source-reported`).
- **Missing Data Handling:** Non-trading days, session breaks, and missing values are natively masked with $m_\tau = 0$; zero imputation or synthetic forward-filling is applied (`source-reported`).

## Execution assumptions

- **Source-Reported Framework:** FinVerse Tier 3 multi-start overlapping backtest evaluating annualized return, annualized volatility, Sharpe ratio, and maximum drawdown (MDD) (`source-reported`).
- **Friction & Fill Semantics (`research-proposed`):**
  - The primary technical report focuses on comparative model ranking across benchmarks and does not publish an explicit transaction fee schedule, slippage model, or fill-delay parameter.
  - Realistic validation requires explicit modeling of:
    - Maker/taker execution fees: $\ge 5$ bps per side for equities/ETFs, $\ge 5$ bps for crypto spot/perpetual.
    - Bid-ask spread crossing: half-spread deduction based on prevailing top-of-book depth.
    - Execution latency: minimum 1-bar delay between signal observation ($t$ close) and execution ($t+1$ open).
- **Capacity & Liquidity Constraints (`research-proposed`):** Restrict universe to assets with median daily dollar volume $\ge \$10\text{M}$ to prevent non-executable allocations in illiquid tail names.

## Evidence

### Source-reported

1. **Overall FinVerse Benchmark Supremacy:**
   - Evaluated against 43 public TSFM baselines (44 models total) spanning attention-based, RNN/SSM, and MLP architectures (including Chronos-2, TimesFM 2.5, Moirai 2.0, Toto-2.0, TiRex, TTM, PatchTST-FM, Sundial, and Reverso) (`source-reported`).
   - EXAONE Finance ranks **#1 across all three evaluation tiers**:
     - *Tier 1 (Point Accuracy):* Rank #1 (`source-reported`).
     - *Tier 2 (Cross-Sectional Information Coefficient, IC):* Rank #1 (`source-reported`).
     - *Tier 3 (Portfolio Backtest - Return, Sharpe, MDD):* Rank #1 (`source-reported`).
   - Overall headline rank-sum is **3** (perfect score: $1+1+1$), compared to **14** for the nearest competitor (`source-reported`).
2. **Head-to-Head Pairwise Dominance:**
   - EXAONE Finance is the only model among all 44 tested whose pairwise win rate is strictly $> 0.50$ across all 43 competing baselines (`source-reported`).
   - Opponent win rates range from $0.51$ to $0.90$ (`source-reported`).
   - Closest competitors: TiRex-2-pretrain and TiRex-1.1 (win rate $0.51$), Chronos-2 Synthetic, and Reverso Small (`source-reported`).
3. **Parameter Efficiency & Scaling Behavior:**
   - Total model size is $202\text{M}$ parameters (`source-reported`).
   - Sits on the Pareto frontier of performance vs. model size, outperforming models an order of magnitude larger (e.g., billion-parameter Toto-2.0 variants) (`source-reported`).
   - Across the benchmark, larger model parameter scale does not correlate with improved financial ranking, indicating standard LLM scaling laws do not hold directly in financial time series (`source-reported`).
4. **Scope Robustness:**
   - Traces a near-maximal envelope across the FinVerse scope $\times$ tier grid, ranking in the 95th–100th percentile in 10 out of 11 populated scope $\times$ tier cells across inter-country, country, sector, and individual asset scopes (`source-reported`).

### Independently reproduced

- Not independently reproduced. All figures and benchmark ranks are third-party results reported by Lee et al. (LG AI Research, arXiv:2609.04239v2, September 2026). No internal backtest or inference pipeline has been executed in PyBroker or NautilusTrader.

### Negative evidence

- **SSM/RNN Parity in Short Horizons:** TiRex (based on xLSTM/recurrent SSM architectures) achieves a $0.49$ win rate against EXAONE Finance (0.51 win rate for EXAONE), indicating that state-space recurrent models perform comparably on raw point-accuracy tasks (`source-reported`).
- **Baseline Tier Instability:** The paper demonstrates that standard models exhibit severe tier dissociation: models that achieve high point accuracy (Tier 1) frequently degrade on portfolio returns (Tier 3), confirming that low MSE/MASE does not imply economic alpha (`source-reported`).
- **No Direct Live Track Record:** All results are pro-forma zero-shot evaluations on historical benchmark windows; live production trading performance under execution stress is unverified (`source-reported`).

## Falsification plan

### Research-Proposed Falsification Tests

1. **Transaction Cost & Turnover Attrition Test:**
   - *Test:* Run the Tier 3 Top-$K\%$ portfolio backtest with explicit round-trip execution friction of $5$, $10$, and $20$ basis points.
   - *Research-defined falsification threshold:* If portfolio net Sharpe drops below $0.50$ or net annualized return degrades by $> 60\%$ relative to frictionless backtest at $h=5$ days, reject the hypothesis that the foundation model provides net tradeable alpha over passive benchmarks.
2. **Post-Publication Walk-Forward OOS Test:**
   - *Test:* Evaluate zero-shot predictions on market data strictly generated after 2026-09-08 across equity and crypto universes.
   - *Research-defined falsification threshold:* Reject if cross-sectional Spearman IC drops to $\le 0.015$ ($t$-stat $< 2.0$) or if the overall model rank drops outside the top 5 relative to simple cross-sectional momentum baselines.
3. **Group-Aware Pooling Ablation (Placebo Test):**
   - *Test:* Randomize group assignment vector $\bm{g}$ across unrelated asset classes (e.g., pairing crypto with sovereign debt).
   - *Research-defined falsification threshold:* If random group pooling achieves cross-sectional IC within $5\%$ of true sector/asset-class groupings, falsify the claim that group-aware pooling captures meaningful inter-asset economic co-dependence.
4. **Synthetic Pretraining Ablation:**
   - *Test:* Compare zero-shot transfer of the model pretrained on the synthetic financial corpus against an identical architecture trained solely on Gaussian random walks or KernelSynth.
   - *Research-defined falsification threshold:* If the financial synthetic prior does not improve cross-sectional IC by at least $15\%$ over domain-agnostic synthetic pretraining, falsify the economic necessity of the 6-family financial generator.

## Crypto portability

**Classification: adapted / unproven**

- **Portability Assessment:**
  - While FinVerse includes crypto-assets as one of its evaluation asset scopes, the primary model pretraining uses synthetic series, and evaluation relies primarily on standardized daily-close snapshots (`source-reported`).
  - Adapting the model to live cryptocurrency markets (spot and perpetual futures) represents a ported research hypothesis rather than verified production evidence (`research-proposed`).
- **Crypto Microstructure Challenges:**
  - *24/7 Session Boundaries:* Unlike equities with distinct daily closing auctions, crypto markets trade continuously. Partitioning contexts into 24-hour windows at 00:00 UTC vs. regional exchange boundaries introduces arbitrary windowing effects.
  - *Perpetual Funding Rate Drag:* Long-only Top-$K\%$ allocation in high-beta crypto perpetuals will incur substantial funding costs during bullish regimes, which can exceed gross predicted drift.
  - *Extreme Volatility & Liquidation Cascades:* Although the model incorporates $\operatorname{arcsinh}$ transforms and Student-$t$ synthetic pretraining, live crypto order-book cascades and depegging events exhibit fat-tail distributions exceeding synthetic jump-diffusion parameters.

## Limitations

- **No Public Live Trading Verification:** Empirical validation is based on pro-forma zero-shot benchmark tests (`FinVerse`); real-money execution is unverified.
- **Underspecified Execution Friction:** The primary report does not quantify bid-ask spread crossing, market impact, exchange fee tiers, or latency slippage in its Tier 3 backtest.
- **Fixed Quantile Decision Rule:** Evaluating solely the median forecast $q_{50}$ discards the remaining 20 predicted quantiles, ignoring predictive distribution asymmetry, skewness, and tail risk.
- **Top-$K\%$ Cutoff Underspecified:** The exact numerical value of $K$ in FinVerse is governed by benchmark configuration rather than economic capacity optimization.
- **Inference Latency on Large Panels:** Although linear in $L$ and $C$, running a 202M-parameter model repeatedly across hundreds of assets requires GPU inference infrastructure, limiting ultra-low-latency deployment.

## Implementation status

- `not-implemented`: No implementation of the EXAONE Finance architecture, inference runtime, or portfolio selection engine has been integrated into the user's research, PyBroker, or NautilusTrader codebases. This record represents external research normalization only.

## Adoption boundary

- `research-only`: This record is captured for quantitative research and hypothesis generation.
- `not-approved`: Presence in this repository does not constitute authorization for strategy implementation, paper trading, demo/testnet trading, or live capital allocation.

## Related Wiki records

- `[[quant/foundation-models-time-series-cross-sectional-alpha]]`
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/cross-sectional-equity-crypto-momentum-validation-2026-08-30]]`

## Sources

- Seunghan Lee, Jaehoon Lee, Jun Seo, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Minjae Kim, Sungdong Yoo, Junhyeok Kang, Sangjun Han, Soonyoung Lee, and Wonbin Ahn, *"EXAONE Finance 1.0: An Attention-free Time Series Foundation Model for Financial Time Series"*, arXiv preprint `arXiv:2609.04239v2 [cs.AI, cs.LG]`, submitted September 4, 2026, revised September 8, 2026. Stable URL: https://arxiv.org/abs/2609.04239 . Full text HTML: https://arxiv.org/html/2609.04239v2 . Canonical DOI: [10.48550/arXiv.2609.04239](https://doi.org/10.48550/arXiv.2609.04239).
- LGAI-Research, *"EXAONE-Forecast"*, official open-source GitHub repository, 2026: https://github.com/LGAI-Research/EXAONE-Forecast.
- LG AI Research, *"EXAONE-Finance-1.0"*, official model weights repository, Hugging Face Hub, 2026: https://huggingface.co/LG-AI-Research/EXAONE-Finance-1.0.
