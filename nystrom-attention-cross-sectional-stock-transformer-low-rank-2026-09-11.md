---
schema: strategy-research-record-v1
title: "Nyström Low-Rank Attention for Cross-Sectional Stock Transformers: Spectral Decomposition, Anti-Correlation Routing, and Large-Scale Scale Boundaries"
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional-equity
  - transformer
  - attention-mechanism
  - nystrom-attention
  - master-architecture
  - low-rank-approximation
  - alpha-prediction
  - spectral-analysis
  - market-microstructure
status: research-only
confidence: high
source_as_of: 2026-09-08
sources:
  - "Kunhan Guo, 'Nyström Attention Matches Full Attention for Cross-Sectional Stock Prediction', arXiv:2609.08106v1 [cs.LG, q-fin.ST], September 8, 2026. https://arxiv.org/abs/2609.08106"
  - "T. Li, Z. Liu, Y. Shen, X. Wang, H. Chen, and S. Huang, 'MASTER: Market-Guided Stock Transformer for Stock Price Forecasting', in Proc. AAAI 2024, pages 162–170. https://github.com/SJTU-DMT/MASTER"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Nyström Low-Rank Attention for Cross-Sectional Stock Transformers: Spectral Decomposition, Anti-Correlation Routing, and Large-Scale Scale Boundaries

## Provenance

- **Primary Source:** Kunhan Guo, *"Nyström Attention Matches Full Attention for Cross-Sectional Stock Prediction"*, arXiv preprint `arXiv:2609.08106v1 [cs.LG, q-fin.ST]`, submitted September 8, 2026 (short version under review at the TS-LIMITS workshop, NeurIPS 2026).
  - Stable arXiv URL: https://arxiv.org/abs/2609.08106
  - Full-text HTML: https://arxiv.org/html/2609.08106v1
  - Full-text PDF: https://arxiv.org/pdf/2609.08106v1
  - Canonical DOI: [10.48550/arXiv.2609.08106](https://doi.org/10.48550/arXiv.2609.08106)
- **Primary Model Baseline:** Market-Guided Stock Transformer (MASTER; Li et al., AAAI 2024, [Proc. AAAI, 38(1):162–170](https://doi.org/10.1609/aaai.v38i1.27789); public codebase: `https://github.com/SJTU-DMT/MASTER`).
- **Investigated Pipeline Module:** Step ➂ of MASTER (inter-stock multi-head attention), accounting for 329,216 parameters (42.5% of total model parameters) and 25.3% of model predictive IC (`source-reported`).
- **Empirical Evaluation Samples:**
  - CSI300: ~300 Chinese A-share stocks with 222 features (158 Alpha158 technical factors, 63 market features, 1 label), 619 test trading days (2019–2020) (`source-reported`).
  - CSI800: ~800 Chinese A-share stocks with matching architecture across 10 random seeds (`source-reported`).
  - Full A-Share Market: ~3,486 stocks per day average, 17 features computed from raw OHLCV, 383 test trading days (2019–2020) across 4 random seeds (`source-reported`).
- **Repository Deduplication:** Audited all existing `.md` records in `alpha-strategy-research`. Zero prior records cite `arXiv:2609.08106`, Kunhan Guo, or Nyström cross-stock attention. Adjacent records (`maple-multi-alpha-position-aware-listwise-ensembling-2026-09-04.md`, `finatom-head-free-token-generation-etf-allocation-dapo-grpo-2026-09-04.md`) cite MASTER only as an external benchmark table entry.

## Economic mechanism

### Source-reported

Cross-sectional equity forecasting models rank an asset universe to capture relative mispricings. State-of-the-art Transformer architectures such as MASTER introduce pairwise multi-head attention across stocks at each timestep (Step ➂) under the explicit premise of capturing "momentary and cross-time stock correlations."

Guo systematically decomposes this inter-stock attention module and uncovers a fundamental architectural paradox:
1. **The Paradox of Uniform Attention:** The learned attention matrix is nearly uniform across the entire stock cross-section. The mean per-row attention entropy is 5.63 nats (against $\ln(300) = 5.70$ nats for a perfectly uniform distribution, a gap of only 1.2%), yielding an effective perplexity of 278 out of 300 stocks (`source-reported`). However, forcing exact uniformity ($\alpha_{uv} = 1/N$) collapses predictive performance (IC drops from 0.0646 to 0.0491, Rank IC from 0.0685 to 0.0514; `source-reported`), demonstrating that the tiny 1.2% deviation carries all cross-sectional predictive information.
2. **Deviation Energy Decomposition:** Decomposing the module output into uniform and deviation components:
   $$z_u = \underbrace{\frac{1}{N}\sum_{v=1}^N V_v}_{z_{\text{uniform}}} + \underbrace{\sum_{v=1}^N \left(\alpha_{uv} - \frac{1}{N}\right) V_v}_{z_{\text{deviation}, u}}$$
   reveals that $z_{\text{uniform}}$ accounts for 98.7% of output energy but has zero cross-sectional variance (identical rank-1 broadcast for all stocks), while $z_{\text{deviation}, u}$ contains only 1.3% of output energy but carries 100% of the cross-sectional ranking variance (`source-reported`).
3. **Anti-Correlation and Complementarity Routing:** The learned pairwise attention anti-correlates strongly with empirical return correlation: Spearman $\rho = -0.614$ ($p \approx 0, n = 73,910$ pairs; `source-reported`). Controlling for same-industry membership, beta difference, and volatility difference yields a partial $\rho = -0.627$ (`source-reported`). Same-industry pairs receive significantly less attention than cross-industry pairs ($b = -0.011, p = 3 \times 10^{-4}$; `source-reported`). The module does not perform "correlation mining"; rather, it seeks cross-sectional information diversification / complementarity.
4. **Low-Rank Structure of Attention Deviations:** Singular value decomposition of the deviation matrix $D = A - \frac{1}{N}\mathbf{1}\mathbf{1}^\top$ demonstrates an effective rank of ~65 (out of 300 stocks), with the top-10 singular values capturing 96.5% of Frobenius norm energy ($\|D\|_F^2$) (`source-reported`). This low-rankness is inherent to softmax attention over large cross-sections (untrained random-init models exhibit effective rank $59 \pm 7$ and top-10 energy $95.6 \pm 0.9\%$; `source-reported`).
5. **Implicit Multi-Factor Model:** Mapping the top singular vectors of $D$ to financial characteristics shows that attention deviations implicitly reconstruct canonical risk factors without explicit supervision:
   - Mode 1 (79.5% energy): Cross-sectional volatility dispersion ($\rho = +0.48$ with realized volatility, $\eta^2 = 0.12$; `source-reported`).
   - Mode 4 (2.0% energy): Defensive vs. cyclical industry separation ($\rho = -0.53$ with market beta, $\rho = -0.69$ with volatility, $\eta^2 = 0.48$; `source-reported`).
   - Modes 2, 3, 5, 7: Momentum, old vs. new economy, liquidity/turnover, and reversal (`source-reported`).

Because the true structure is low-rank and near-global, sparse graph methods (GraphMask, TopK) destroy the global factor subspace and fail, whereas low-rank Nyström attention ($m=32$ landmarks) preserves the entire factor geometry at $O(mN)$ complexity (`source-reported`).

### Research interpretation

The economic significance of Guo's findings extends far beyond computational efficiency:
1. **Factor Demeaning vs. Graph Propagation:** In cross-sectional equity returns, the dominant variation is driven by low-dimensional systematic factor risk (market mode, volatility regimes, sector rotations), while idiosyncratic alpha lives in the residual orthogonal subspace. Inter-stock attention does not function as a relational knowledge graph connecting supply-chain partners; rather, it acts as an end-to-end, dynamic latent factor estimator. The uniform component isolates the market common mode, while the low-rank deviation estimates the asset's dynamic factor loadings.
2. **Why Anti-Correlation Generates Alpha:** A stock's idiosyncratic return cannot be identified by comparing it to identical co-movers; it must be benchmarked against contrasting assets across the factor frontier to isolate whether its movement is systematic factor drift or genuine idiosyncratic mispricing. Attention to anti-correlated assets provides the baseline contrast necessary for cross-sectional rank ordering.
3. **The Limits of Large-Scale Cross-Stock Attention:** At smaller universes ($N = 300$ to $800$), stocks possess high signal-to-noise ratios and well-defined factor loadings. At market scale ($N \approx 3,500$), the vast influx of illiquid, noisy micro-cap stocks contaminates the global attention pooling, creating high estimation variance that prevents the cross-stock module from outperforming an independent per-stock temporal model (PureLSTM).

## Signal

### Prediction Pipeline & Model Architecture

The strategy operates a five-stage hybrid deep neural network based on MASTER with Nyström cross-stock attention (`source-reported`):

1. **Step ➀: Market-Guided Gating:**
   Dynamically rescales stock input feature vectors using market index features to inject broad macroeconomic context (`source-reported`).
2. **Step ➁: Intra-Stock Temporal Attention:**
   A Transformer encoder operating independently per stock across $T = 8$ daily lookback timesteps (`source-reported`):
   $$H_u = \text{TemporalTransformer}(X_u) \in \mathbb{R}^{T \times d_{\text{model}}}$$
   with $d_{\text{model}} = 256$, $n_{\text{head}} = 2$ (`source-reported`).
3. **Step ➂: Inter-Stock Nyström Multi-Head Attention:**
   Applied across all $N$ stocks at each timestep $t \in \{1,\ldots,T\}$. Instead of calculating full $N \times N$ attention, $m = 32$ landmark stocks are sampled uniformly at random on each forward pass (`source-reported`):
   - Project stock representations to queries $Q \in \mathbb{R}^{N \times d}$, keys $K \in \mathbb{R}^{N \times d}$, values $V \in \mathbb{R}^{N \times d}$.
   - Landmark subsets: $\widetilde{Q}, \widetilde{K} \in \mathbb{R}^{m \times d}$ selected from $Q, K$.
   - Compute landmark kernel matrices:
     $$A_1 = \text{softmax}\left(\frac{Q \widetilde{K}^\top}{\sqrt{d}}\right) \in \mathbb{R}^{N \times m}$$
     $$A_2 = \text{softmax}\left(\frac{\widetilde{Q} \widetilde{K}^\top}{\sqrt{d}}\right) \in \mathbb{R}^{m \times m}$$
     $$A_3 = \text{softmax}\left(\frac{\widetilde{Q} K^\top}{\sqrt{d}}\right) \in \mathbb{R}^{m \times N}$$
   - Compute Moore-Penrose pseudo-inverse $A_2^+$ via 6 Newton-Schulz iterations:
     $$Z_{k+1} = Z_k (2I - A_2 Z_k)$$
     avoiding materialization of any $N \times N$ matrix (`source-reported`).
   - Nyström attention output:
     $$\widetilde{z}_u = A_1 A_2^+ (A_3 V) \in \mathbb{R}^{N \times d}$$
     followed by LayerNorm, feed-forward network (FFN), and residual connection (`source-reported`).
4. **Step ➃: Temporal Aggregation:**
   Collapses the temporal dimension $T$ using query-key attention where the final timestep $T$ queries all previous timesteps (`source-reported`).
5. **Step ➄: Linear Prediction Head:**
   Linear layer mapping the pooled representation to scalar predicted forward return $\widehat{y}_{u,t}$ (`source-reported`).

### Target Formulation & Signal Construction

- **Forecast Target:** 4-day forward return with a 1-day execution gap (`source-reported`):
  $$\text{target}_{u,t} = \frac{\text{close}_{u,t+5}}{\text{close}_{u,t+1}} - 1$$
- **Signal Formation Timestamp:** Daily at post-close (15:00 CST / 07:00 UTC) upon calculation of daily OHLCV and factor libraries (`source-reported`).
- **Cross-Sectional Rank Signal:**
  For each active stock $u \in \{1, \ldots, N_t\}$, compute the normalized cross-sectional percentile rank:
  $$\text{RankScore}_{u,t} = \frac{\text{rank}(\widehat{y}_{u,t}) - 1}{N_t - 1} \in [0, 1]$$
  (`research-proposed` operational standardization).

### Portfolio Construction & Execution Logic

- **Long Portfolio Selection:** Stocks with $\text{RankScore}_{u,t} \ge 0.80$ (top quintile) (`research-proposed`).
- **Short Portfolio Selection:** Stocks with $\text{RankScore}_{u,t} \le 0.20$ (bottom quintile) for long-short market-neutral research evaluation; long-only benchmarked against CSI300 index for production execution (`research-proposed`).
- **Position Sizing:** Equal-weighted across quintile members, or rank-score weighted with portfolio leverage normalized to 1.0 gross exposure (`research-proposed`).
- **Holding Period & Rebalancing:** 4 trading days, implemented via 4 staggered daily tranches (25% portfolio rebalance daily) to eliminate rebalancing day timing luck (`research-proposed`).

## Required data

- **Universe:**
  - CSI300: ~300 largest and most liquid Chinese A-share stocks (`source-reported`).
  - CSI800: ~800 Chinese A-share stocks (`source-reported`).
  - Full A-Share Market: ~3,486 active stocks per day (`source-reported`).
- **Market Type:** Cash Equities (Shanghai Stock Exchange, Shenzhen Stock Exchange) (`source-reported`).
- **Timeframe:** Daily OHLCV bars (`source-reported`).
- **Input Features:**
  - CSI300/CSI800 Universe: 222 features consisting of Alpha158 technical factor library (158 price-volume formulas including rolling momentum, volatility, volume-price correlation, moving-average spreads) plus 63 market-level index features (CSI300 aggregate volume, turnover, market momentum) (`source-reported`).
  - Full A-Share Market: 17 engineered features derived directly from raw OHLCV (`source-reported`).
- **Sample Split:**
  - CSI300 Primary Split: Training 2010–2017, Validation 2017–2018, Test 2019–2020 (619 test trading days) (`source-reported`).
  - Full A-Share Split: Training 2010–2017, Test 2019–2020 (383 test trading days) (`source-reported`).
- **Point-in-Time Integrity:**
  - Strict 1-day execution gap: Features computed through day $t$; label measures return from close of day $t+1$ to close of day $t+5$ (`source-reported`). Orders execute at close of day $t+1$ (or open of day $t+2$), preventing look-ahead leakage.
- **Normalization:**
  - Standard setup: Qlib global robust z-score normalization (`source-reported`).
  - Alternative setup: Per-day cross-sectional z-score normalization (`source-reported`).

## Execution assumptions

- **Execution Timing:** Signal calculated post-close day $t$; orders dispatched for execution at the close of trading day $t+1$ (`source-reported`).
- **Order Type:** Market-on-Close (MOC) or VWAP over the closing 30 minutes of day $t+1$ (`research-proposed`).
- **Fill Model:** Full fill assumed at recorded closing price in paper backtests (`source-reported`).
- **Frictional Costs:**
  - Primary source reports frictionless metrics (zero commissions, zero slippage, zero borrow fees, zero market impact) (`source-reported`).
  - Production A-share friction model: Stamp duty of 0.05% on stock sales, brokerage commission of 0.025% two-sided, and estimated slippage of 0.05% per side, totaling ~0.15% round-trip friction (`research-proposed`).
- **Short-Selling Constraints:**
  - In Chinese A-shares, short-selling via margin lending (融券) is heavily constrained by inventory quotas and regulatory restrictions (`source-reported` institutional caveat).
  - Unconstrained long-short return figures represent theoretical alpha capacity; practical institutional deployment requires either a long-only top-quintile overlay or index futures (IF/IC) hedging (`research-proposed`).

## Evidence

### Source-reported

1. **MASTER Full Pipeline Ablation (CSI300, Seed 0):**
   - Full MASTER: IC $0.0646$, Rank IC $0.0685$, Parameters: $775,041$ (`source-reported`).
   - No Step ➀ (market gating): IC $0.0622$, Rank IC $0.0673$ ($\Delta \text{IC} = -3.6\%$) (`source-reported`).
   - No Step ➁ (temporal attention): IC $0.0612$, Rank IC $0.0671$ ($\Delta \text{IC} = -5.2\%$) (`source-reported`).
   - **No Step ➂ (inter-stock attention):** IC $0.0482$, Rank IC $0.0514$ ($\mathbf{\Delta \text{IC} = -25.3\%}$, dominant predictive contributor) (`source-reported`).
   - No Step ➃ (temporal pooling): IC $0.0605$, Rank IC $0.0722$ ($\Delta \text{IC} = -6.3\%$, Rank IC $+5.4\%$) (`source-reported`).

2. **Nyström Equivalence vs. Full Attention (CSI300, 5 Seeds):**
   - Full Attention $O(N^2)$: IC $0.058 \pm 0.007$, Rank IC $0.066 \pm 0.003$, ICIR $0.386$, Rank ICIR $0.429$ (`source-reported`).
   - **Nyström ($m=32$, $O(32N)$):** IC $0.059 \pm 0.002$, Rank IC $0.066 \pm 0.003$, ICIR $0.389$, Rank ICIR $0.416$ (`source-reported`).
   - Two One-Sided Tests (TOST) Equivalence Certification:
     - At margin $\delta = \pm 0.005$: Rank IC is certified equivalent ($p = 0.003$), IC $p = 0.099$ (`source-reported`).
     - At margin $\delta = \pm 0.008$: IC is certified equivalent ($p = 0.028$) (`source-reported`).
     - $90\%$ Confidence Intervals: IC $[-0.005, +0.007]$, Rank IC $[-0.002, +0.001]$ (`source-reported`).
   - Seed-to-seed variance: Nyström exhibits $3.5\times$ lower IC variance ($0.002$ vs. $0.007$) (`source-reported`).

3. **CSI800 Scaling Equivalence (10 Seeds):**
   - Full Attention ($n=10$): IC $0.047 \pm 0.004$, Rank IC $0.059 \pm 0.004$ (`source-reported`).
   - Nyström ($m=32$, $n=10$): IC $0.045 \pm 0.004$, Rank IC $0.059 \pm 0.006$ (`source-reported`).
   - TOST Equivalence at $\delta = \pm 0.005$: IC certified equivalent ($p = 0.038$), Rank IC certified equivalent ($p = 0.034$) (`source-reported`).
   - Increasing landmarks to $m=80$ (matching 10% CSI300 ratio) does not improve metrics, confirming $m \approx 32$ is scale-invariant (`source-reported`).

4. **Computational & Memory Scaling (Tesla T4, 16 GB GPU, $d=256, h=2, T=8$):**
   - $N=300$: Full attention $1.65\,\text{ms}$, Nyström $5.90\,\text{ms}$ ($0.3\times$ speedup due to $\sim 4\,\text{ms}$ fixed Newton-Schulz overhead) (`source-reported`).
   - Crossover Threshold: $N^* \approx 1,300$ stocks (`source-reported`).
   - $N=3,500$: Full attention $48.66\,\text{ms}$, Nyström $8.92\,\text{ms}$ ($\mathbf{5.5\times}$ speedup; memory $1,350\,\text{MB}$ vs. $298\,\text{MB}$, $\mathbf{4.5\times}$ memory savings) (`source-reported`).
   - $N=9,000$: Full attention $339.5\,\text{ms}$, Nyström $23.17\,\text{ms}$ ($\mathbf{14.7\times}$ speedup; memory $8,194\,\text{MB}$ vs. $732\,\text{MB}$, $\mathbf{11.2\times}$ memory savings) (`source-reported`).
   - $N=12,000$: Full attention Out-of-Memory (OOM, $>16\,\text{GB}$); Nyström executes in $30.46\,\text{ms}$ consuming only $974\,\text{MB}$ (`source-reported`).

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Failure of Graph-Guided Sparsification:**
   - GraphMask + Return Correlation: Drops IC to $0.045 \pm 0.004$ and Rank IC to $0.049 \pm 0.002$ (4 seeds), performing **worse than removing the module entirely** (No Step ➂: IC $0.050 \pm 0.001$, Rank IC $0.052 \pm 0.002$; paired $t$-test $p = 0.040$; `source-reported`).
   - GraphMask + Industry: IC drops to $0.0437$, Rank IC $0.0458$ (`source-reported`).
   - GCN Replacement + Return Correlation: IC drops to $0.0487$, Rank IC $0.0570$ (`source-reported`).
   - TopK Sparsity ($K=16$): IC drops to $0.052 \pm 0.004$, retaining less than 50% of the cross-sectional alpha contribution (`source-reported`).
2. **Failure of Static Attention Routing:**
   - Freezing attention to time-averaged oracle matrix $\bar{A}$ (computed on test set) drops IC to $0.0497$ and Rank IC to $0.0595$, recovering only ~9% of IC value above floor (`source-reported`).
   - End-to-end trained static low-rank baseline (`LearnedLowRank`, $r=32$) completely collapses to the no-attention floor (IC $0.0478 \approx 0.0482$, Rank IC $0.0500$; `source-reported`). Dynamic data-dependent routing is mandatory.
3. **Non-Monotonic Landmark Profile:**
   - Sweeping $m \in \{8, 16, 24, 32, 48, 64, 96, 128\}$ peaks at $m=32$ ($0.059 \pm 0.002$). Increasing to $m=48$ or $m=64$ degrades performance ($m=64$ IC drops to $0.0554$, Rank IC $0.0603$; `source-reported`). Oversizing landmarks destabilizes the pseudo-inverse conditioning.
4. **Failure to Outperform Per-Stock Baselines at Market Scale ($N \approx 3,500$):**
   - Across 4 random seeds on full A-shares:
     - PureLSTM (per-stock baseline): IC $0.043 \pm 0.002$, Rank IC $0.056 \pm 0.003$, Sharpe $5.6 \pm 0.5$ (`source-reported`).
     - MASTER + Nyst32: IC $0.037 \pm 0.008$, Rank IC $0.050 \pm 0.016$, Sharpe $5.6 \pm 1.1$ (`source-reported`).
     - LSTM + GCN: IC $0.034 \pm 0.008$, Rank IC $0.063 \pm 0.009$, Sharpe $4.1 \pm 1.5$ (`source-reported`).
   - Paired $t$-tests confirm that cross-stock attention does **not** significantly outperform a per-stock LSTM (IC $p = 0.27$, Rank IC $p = 0.53$; `source-reported`).
5. **Preprocessing Sensitivity:**
   - Under per-day cross-sectional z-score normalization, full attention IC improves by $+0.005$ with $5.8\times$ lower seed variance, while Nyström IC is unchanged, causing the TOST Rank IC equivalence to weaken from $p = 0.003$ to $p = 0.120$ (`source-reported`).

## Falsification plan

1. **Permutation & Shuffled Landmark Audit:**
   - Replace dynamic Nyström landmarks with randomly scrambled cross-sectional indices or shuffled cross-sectional target returns.
   - *Falsification Criterion:* If cross-sectional Rank IC does not drop to the no-attention floor ($\le 0.0514$) upon cross-sectional scrambling, reject the claim that dynamic inter-stock information redistribution is the mechanism (`research-defined falsification threshold`).
2. **Dense Factor Subspace Ablation:**
   - Project stock representations onto the top-5 explicit PCA return modes prior to Step ➂. If explicit orthogonal factor demeaning achieves equivalent Rank IC to full/Nyström attention without learning, the claim of deep non-linear inter-stock representation learning is falsified in favor of linear factor demeaning (`research-defined falsification threshold`).
3. **Transaction Cost & Turnover Stress:**
   - Apply realistic A-share trading frictions (0.15% round-trip) and liquidity constraints to the 4-day rebalanced portfolio.
   - *Falsification Criterion:* If daily portfolio turnover exceeds 25% and transaction friction reduces annualized net Sharpe ratio below $1.0$ (or below buy-and-hold CSI300), the alpha hypothesis is rejected as economically unexecutable (`research-defined falsification threshold`).
4. **Out-of-Sample Regime Verification (2021–2026):**
   - Evaluate model checkpoints trained on 2010–2017 across post-2020 regimes (regulatory restructuring, real estate deleveraging, high-volatility macro shifts).
   - *Falsification Criterion:* If out-of-sample monthly Rank IC drops below $0.020$ for $>3$ consecutive months, retire the model from production candidacy (`research-defined falsification threshold`).

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Cross-Asset Translation Mechanics:**
  - The primary study investigates Chinese A-share cash equities exclusively. The mechanism has not been demonstrated in cryptocurrency markets by the cited source.
  - In liquid cryptocurrency perpetual futures (e.g., Binance / Bybit USDT perpetuals), the tradeable universe is typically $N \approx 100 - 300$ active tokens. In this universe size, full attention is computationally trivial ($1.65\,\text{ms}$), while Nyström incurs the $\sim 4\,\text{ms}$ Newton-Schulz pseudo-inverse overhead without providing efficiency advantages.
  - Furthermore, crypto returns exhibit overwhelming market-beta dominance (Bitcoin driving 60–80% of aggregate cross-sectional variance), which directly matches Mode 1 of the deviation matrix (79.5% volatility/market mode energy).
  - Cross-sectional attention could theoretically isolate idiosyncratic token alpha from macro BTC momentum, but requires adapting inputs from Alpha158 to 24/7 crypto features: funding rate spreads, open interest momentum, spot-perp basis, and cross-venue taker volume.
- **Portability Risks:**
  - Dynamic universe reconstitution: Crypto tokens experience rapid listing, liquidity decay, and delisting, disrupting fixed-dimensional cross-sectional matrices.
  - High idiosyncratic jump hazard: Low-liquidity altcoin manipulation and flash liquidations create extreme outliers that can distort global softmax attention normalization.

## Limitations

1. **Underspecified Execution Friction:** The primary paper reports purely frictionless returns and Sharpe ratios, omitting transaction costs, borrow fees, slippage, and short-sale availability constraints (`source-reported` limitation).
2. **Architecture Specificity:** All empirical findings are derived within the MASTER framework. Whether the low-rank deviation property and Nyström equivalence hold across alternative architectures (e.g., StockMixer, FinMamba, PatchTST) remains unproven (`source-reported` limitation).
3. **Scale Invalidation:** Cross-stock attention fails to outperform an independent per-stock LSTM when scaled to the full market ($N \approx 3,500$), indicating that cross-stock attention is brittle in the presence of noisy, illiquid micro-caps (`source-reported` empirical limitation).
4. **Preprocessing Boundary:** The statistical equivalence of Nyström narrows significantly when input features undergo per-day cross-sectional z-score normalization ($p=0.120$), showing that optimal feature conditioning enables full attention to extract fine-grained signals that low-rank approximation misses (`source-reported`).

## Implementation status

- **Current Repository Status:** `not-implemented`.
- No prototype, backtest runner, PyBroker script, NautilusTrader integration, paper trading, or live execution has been implemented in this repository or associated execution engines.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- Recording this research artifact documents empirical properties of cross-sectional attention mechanisms for quantitative research and hypothesis generation. It does not constitute verification of trading profitability or authorization for paper, testnet, or live trading deployment.

## Related Wiki records

- `[[quant/cross-sectional-equity-ridge-percentile-rank-alpha-2026-09-03]]`
- `[[quant/maple-multi-alpha-position-aware-listwise-ensembling-2026-09-04]]`
- `[[quant/finatom-head-free-token-generation-etf-allocation-dapo-grpo-2026-09-04]]`
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`

## Sources

- Kunhan Guo, *"Nyström Attention Matches Full Attention for Cross-Sectional Stock Prediction"*, arXiv preprint `arXiv:2609.08106v1 [cs.LG, q-fin.ST]`, September 8, 2026. Stable arXiv URL: https://arxiv.org/abs/2609.08106; HTML: https://arxiv.org/html/2609.08106v1; DOI: `10.48550/arXiv.2609.08106`.
- T. Li, Z. Liu, Y. Shen, X. Wang, H. Chen, and S. Huang, *"MASTER: Market-Guided Stock Transformer for Stock Price Forecasting"*, Proceedings of the AAAI Conference on Artificial Intelligence (AAAI 2024), 38(1):162–170, 2024. Code: `https://github.com/SJTU-DMT/MASTER`.
- Y. Xiong, Z. Zeng, R. Chakraborty, M. Tan, G. Fung, Y. Li, and V. Singh, *"Nyströmformer: A Nyström-Based Algorithm for Approximating Self-Attention"*, in Proc. AAAI 2021.
