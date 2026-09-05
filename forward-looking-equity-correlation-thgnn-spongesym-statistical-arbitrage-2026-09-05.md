---
schema: strategy-research-record-v1
title: "Forward-Looking Equity Correlation Forecasting via Temporal-Heterogeneous Graph Neural Networks and SPONGEsym Signed Graph Clustering in S&P 500 Statistical Arbitrage"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - graph-neural-network
  - transformer
  - graph-attention-network
  - thgnn
  - spongesym
  - correlation-forecasting
  - fisher-z-transform
  - histogram-matching-loss
  - mean-reversion
  - market-neutral
status: research-only
confidence: high
source_as_of: 2026-01-08
sources:
  - "Jack Fanshawe, Rumi Masih, and Alexander Cameron, 'Forecasting Equity Correlations with Hybrid Transformer Graph Neural Network', arXiv:2601.04602v1 [q-fin.CP, q-fin.TR], January 8, 2026. DOI: 10.48550/arXiv.2601.04602. https://arxiv.org/abs/2601.04602"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forward-Looking Equity Correlation Forecasting via Temporal-Heterogeneous Graph Neural Networks and SPONGEsym Signed Graph Clustering in S&P 500 Statistical Arbitrage

## Provenance

- **Primary Source:** Jack Fanshawe, Rumi Masih, and Alexander Cameron (Business School, Faculty of Business, Economics and Law, The University of Queensland, Australia), *"Forecasting Equity Correlations with Hybrid Transformer Graph Neural Network"*, arXiv preprint `arXiv:2601.04602v1 [q-fin.CP, q-fin.TR]`, submitted January 8, 2026.
- **Canonical arXiv URL:** [https://arxiv.org/abs/2601.04602](https://arxiv.org/abs/2601.04602)
- **Direct HTML Full Text:** [https://arxiv.org/html/2601.04602v1](https://arxiv.org/html/2601.04602v1)
- **Primary LaTeX Source Package:** Inspected directly from official arXiv source bundle `arXiv:2601.04602` containing `main.tex` (990 lines), `References.bib`, and all associated empirical result tables and figures. All mathematical formulas, network hyperparameters, loss components, grid searches, and empirical performance metrics in this record trace directly to this primary LaTeX source.
- **Pre-Write Deduplication & Identity Audit:** A comprehensive repository-wide audit verified zero matches for `2601.04602`, `Fanshawe`, `Masih`, or `THGNN` across all existing repository records. While the repository contains a record for the predecessor backward-looking framework (`graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05.md` based on Korniejczuk & Ślepaczuk 2024, arXiv:2406.10695v1), this record represents an independent, materially distinct research capture:
  1. It documents an independent empirical replication attempt of Korniejczuk & Ślepaczuk (2024) using survivorship-bias-free CRSP/Compustat WRDS data that **failed to reproduce** the reported profitability of the backward-looking ML-filtered strategy (crucial negative evidence).
  2. It replaces backward-looking rolling historical correlation estimation entirely with a 10-day forward-looking predictive framework based on a Temporal-Heterogeneous Graph Neural Network (THGNN) combining a 4-layer Transformer temporal encoder with an edge-aware 3-layer Graph Attention Network (GAT).
  3. It formulates correlation forecasting as residual learning in Fisher $z$-space combined with differentiable Gaussian soft-binning histogram-matching loss to prevent mode collapse and preserve cross-sectional dispersion.

## Economic mechanism

### Source-reported

In classical multi-asset statistical arbitrage and pairs trading (Gatev et al. 2006; Avellaneda & Lee 2008), equities are clustered into co-moving baskets based on historical correlation, cointegration, or fundamental industry classifications (such as Fama-French 48). When an individual security's short-term price deviates from its cluster equilibrium, contrarian long/short positions are entered under the expectation of mean reversion.

However, existing graph-based statistical arbitrage approaches—such as the Signed Positive Over Negative Generalized Eigenproblem ($\text{SPONGE}_{sym}$; Cartea, Cucuringu & Jin 2023; Korniejczuk & Ślepaczuk 2024)—suffer from an inherent structural defect: **backward-looking dependence estimation lag**.
- Rolling historical windows (e.g. 20 to 60 days) average past realized returns. Consequently, they reflect obsolete market regimes long after underlying conditions have shifted.
- In financial crises and systemic transitions (e.g. the COVID-19 shock of March 2020 or the geopolitical commodity spike of early 2022), cross-asset correlations shift within days, collapsing previously distinct clusters into a few highly correlated groups.
- Backward-looking clustering algorithms continue trading stale baskets while rolling windows slowly adjust over weeks, resulting in misallocated hedges, severe drawdowns, and persistent losses during market stress.

To overcome this lag, the source proposes **forward-looking correlation forecasting**. By treating cross-asset correlation not as a static historical summary but as a predictable dynamical state variable driven by macroeconomic shocks, volatility regimes, and cross-asset lead-lag relations, clusters can be constructed based on *anticipated* rather than *realized* market structure.

### Research interpretation

From a market-microstructure and asset-pricing perspective, the economic mechanism operates via two distinct channels:
1. **Regime-Adaptive Spectral Clustering:** The $\text{SPONGE}_{sym}$ algorithm minimizes within-cluster negative correlation while maximizing within-cluster positive correlation. When fed forward-looking correlation matrices $\hat{\rho}_{ij}^{t \to t+10}$, the eigenspace representation shifts proactively prior to regime breaks. This prevents the formation of "phantom clusters" where divergent assets are grouped together simply because their trailing 30-day returns were correlated prior to a structural break.
2. **Fisher $z$-Space Residual Dynamics & Macroeconomic Conditioning:** Cross-asset correlations exhibit high variance and heteroskedastic bounded behavior ($\rho \in [-1, 1]$). Modeling residual deviations $\Delta z_{ij}$ in Fisher $z$-space relative to a 30-day historical baseline anchors predictions to a robust empirical prior while allowing rapid adjustments driven by macro state variables (VIX, 10-year Treasury yields, crude oil, and trade-weighted dollar index). The resulting forward-looking baskets isolate pure idiosyncratic deviations, improving the signal-to-noise ratio of cluster-level mean reversion.

## Signal

The trading signal is evaluated at 10-day rebalance intervals across all eligible S&P 500 constituents.

### 1. Data Processing & Input Feature Construction
- **Sampling Frequency:** Daily closing prices.
- **Universe:** S&P 500 constituents with at least 30 trading days of data within the trailing 33-day calendar window (source-reported data completeness filter).
- **Feature Vector:** Each stock $i$ at date $t$ is represented by a sequence $X_{(i,t)} \in \mathbb{R}^{L \times F}$ across a lookback window of $L = 30$ trading days and $F = 37$ features:
  - *Price & Volume (2):* Closing price (PRC), trading volume (VOL).
  - *Technical Indicators (6):* Momentum (5-day, 20-day, 60-day), short-term reversal (5-day), Relative Strength Index ($RSI_{14}$), Average True Range ($ATR_{14}$).
  - *Firm Characteristics (2):* Market capitalization, book-to-market ratio.
  - *Factor Exposures (3):* Rolling betas to Fama-French three factors (Mkt-RF, SMB, HML).
  - *Macroeconomic & Risk Factors (10):* Excess market return, SMB, HML, risk-free rate, momentum factor (UMD), WTI crude oil price (`DCOILWTICO`), 10-year Treasury yield (`DGS10`), Trade-Weighted U.S. Dollar Index (`DTWEXBGS`), VIX index, GARCH(1,1) implied volatility.
  - *Return Measures (3):* Daily excess return, raw return, SPY return.
  - *Sector & Industry (2):* GICS sector code (`gsector`), GICS sub-industry code (`gsubind`).
  - *Correlation & Volatility Context (9):* Rolling market correlations (10-day, 21-day, 63-day), average 21-day correlation with sector and sub-industry, realized volatility with the sector (20-day) and sub-industry (20-day), 10-day realized market volatility, cross-sectional return dispersion.
- **Normalization:** Rolling 60-day z-score normalization across all features to prevent domination by high-variance features.

### 2. THGNN Architecture & Forward Correlation Forecasting
The model combines a temporal Transformer encoder with an edge-aware Graph Attention Network (GAT):
1. **Temporal Encoder (Transformer):**
   - Linear projection from $F = 37$ to $d_{\text{model}} = 128$.
   - Sinusoidal positional encodings added.
   - 4 pre-norm Transformer encoder layers with $H_{\text{trans}} = 8$ attention heads ($d_k = 16$), dropout $0.20$.
   - Output matrix $H_{(i,t)} \in \mathbb{R}^{30 \times 128}$ is flattened to $\mathbb{R}^{3840}$, then projected via LayerNorm-MLP to a 512-dimensional node embedding $h_i^{(0)} \in \mathbb{R}^{512}$.
2. **Graph Construction & Edge Sampling:**
   - Undirected, signed, weighted graph $G_t = (V, E_t, W_t)$.
   - Baseline correlation $\rho^{\text{base}}_{(ij,t)}$ computed over rolling 30-day window ending at date $t$.
   - For every stock $i$, edges are sampled to:
     - Top 50 highest correlations ($\rho^{\text{base}}$);
     - Bottom 50 lowest correlations ($\rho^{\text{base}}$);
     - 75 randomly sampled mid-strength partners from the $[0.20, 0.80]$ correlation percentile range.
   - Edge attributes $a_{(ij,t)}$: $\rho^{\text{base}}_{(ij,t)}$, $|\rho^{\text{base}}_{(ij,t)}|$, sign indicator (0 if $>0$, 1 otherwise), binary same-sector flag, binary same-subindustry flag.
   - Edge relation class $\tau_{ij} \in \{0, 1, 2\}$: discrete tertile label for low (bottom third), neutral (middle third), and high (top third) correlation.
3. **Relational Encoder (GAT):**
   - $L_g = 3$ graph attention layers, each with $H_{\text{gat}} = 4$ attention heads.
   - Edge-conditioned gate:
     $$m_{(ij)}^{(l,h)} = E^{(h)}_{\text{type}}(\tau_{ij}) + W_f^{(h)} f_{ij} + W_a^{(h)} a_{(ij,t)} + W_s^{(h)} e_{ij}^{(l)}$$
   - Multi-head attention coefficients computed via LeakyReLU on concatenated projected node states and edge gate, normalized over neighbors via softmax.
   - Pairwise edge embeddings formed at layer $L_g$: $u_{ij}^{\text{edge}} = [h_i^{(3)} \,||\, h_j^{(3)} \,||\, e_{ij}^{(3)}]$.
   - Routed to one of three specialized MLP expert heads based on $\tau_{ij} \in \{0, 1, 2\}$ (negative, neutral, positive correlation regimes).
4. **Fisher $z$-Space Residual Prediction:**
   - Each expert head outputs a scalar residual $\Delta \hat{z}_{ij}$.
   - Forward 10-day correlation prediction:
     $$\hat{z}_{(ij, t \to t+10)} = z_{(ij,t)}^{\text{base}} + \Delta \hat{z}_{ij}, \quad \text{where } z_{(ij,t)}^{\text{base}} = \text{atanh}(\rho_{(ij,t)}^{\text{base}})$$
     $$\hat{\rho}_{(ij, t \to t+10)} = \tanh\left(\hat{z}_{(ij, t \to t+10)}\right)$$
5. **Loss Function (Dual Objective):**
   - Edge loss: Smooth-L1 (Huber) loss on Fisher $z$-space residuals: $L_{\text{edge}} = \text{Huber}(\hat{z}_{(ij, t+10)}, z_{(ij, t+10)})$.
   - Histogram loss: Differentiable Gaussian soft-binning histogram matching loss ($L_{\text{hist}}$) comparing predicted and realized correlation distributions (6 bins for each of the 3 edge regimes, 15 bins globally; Gaussian width $\sigma$, scaled by $s = 7$).
   - Total loss: $L_{\text{total}} = 0.5 \cdot L_{\text{edge}} + 0.5 \cdot L_{\text{hist}}$.

### 3. SPONGEsym Clustering & Portfolio Construction
1. **Adjacency Decomposition:**
   - Predicted $N \times N$ correlation matrix $\hat{\rho}$ decomposed into positive and negative components: $A^+ = \max(\hat{\rho}, 0)$, $A^- = \max(-\hat{\rho}, 0)$.
   - Normalized Laplacians: $L_{\text{sym}}^+ = D_+^{-1/2} A^+ D_+^{-1/2}$, $L_{\text{sym}}^- = D_-^{-1/2} A^- D_-^{-1/2}$.
2. **Generalized Eigenproblem:**
   $$(L_{\text{sym}}^- + \tau^+ I) v = \lambda (L_{\text{sym}}^+ + \tau^- I) v$$
   - The optimal number of clusters $k$ is determined dynamically via the 90% explained variance eigenvalue criterion:
     $$k = \min \left\{ m : \frac{\sum_{i=1}^m \lambda_i}{\sum_{i=1}^N \lambda_i} \geq 0.90 \right\}$$
   - $k$-means++ is applied to the top-$k$ eigenvectors to partition stocks into $k$ clusters.
3. **Contrarian Position Sizing within Clusters:**
   - Within each cluster $k$, calculate the 5-day cumulative return of each stock $r_{i, 5\text{d}}$ and the cluster mean return $\bar{r}_{k, 5\text{d}}$.
   - Deviation: $\delta_i = r_{i, 5\text{d}} - \bar{r}_{k, 5\text{d}}$.
   - Direction: Long if $\delta_i < 0$ (underperformed cluster mean); Short if $\delta_i > 0$ (outperformed cluster mean).
4. **Machine Learning Signal Quality Filtering (Top 10% Gate):**
   - For every candidate position, an ensemble of 5 classifiers (HistGradientBoosting, AdaBoost, MLP, SGD, Logistic Regression) predicts probability of trade profitability:
     - Target label = 1 if cumulative trade return reaches +4% take-profit threshold during 10-day holding or exceeds round-trip transaction costs at rebalance; 0 otherwise.
     - Features for classifiers: Local vertex degree, global vertex degree, graph density, cluster size proportion, 5-day return deviation from cluster mean, long/short indicator, 10-day mean cluster return, 10-day mean stock return.
     - Aggregation: Soft-voting ensemble weighted by inverse Brier score (HGB receives double weight due to superior calibration).
   - Selection rule: Rank all candidate positions by ensemble predicted probability; trade only the **top 10%** highest-probability signals (yielding an average portfolio size of ~45 stocks).
5. **Position Sizing & Holding Period:**
   - Positions held for $H = 10$ trading days (source-reported).
   - Equal-weighted across the selected top 10% signals (source-reported).
   - Intraday exit: Early closeout if position reaches +4.0% profit barrier prior to 10-day expiration (source-reported).

## Required data

- **Universe:** S&P 500 constituents (survivorship-bias-free historical constituents sourced via CRSP/Compustat on WRDS).
- **Timeframe:** Daily OHLCV data.
- **Macroeconomic & Factor Inputs:**
  - VIX Index (CBOE).
  - WTI Crude Oil Spot Price (`DCOILWTICO`, FRED).
  - 10-Year Treasury Constant Maturity Rate (`DGS10`, FRED).
  - Trade-Weighted U.S. Dollar Index: Broad (`DTWEXBGS`, FRED).
  - Fama-French Three Factors (Mkt-RF, SMB, HML) and Momentum Factor (UMD) from Kenneth French Data Library.
  - Risk-free rate (3-month T-bill secondary market rate).
- **Metadata & Structural Data:** GICS Sector (`gsector`) and Sub-Industry (`gsubind`) identifiers.
- **Point-in-Time Availability:** Training on 2006–2018; out-of-sample evaluation on 2019-03-26 to 2024-10-04 (60 trading day buffer after 2019-01-01 strictly enforces no lookahead in 60-day rolling z-score normalizations).

## Execution assumptions

- **Rebalance Cadence:** Every 10 trading days (source-reported).
- **Signal-to-Order Timing:** Evaluated on daily closing bars; executed at next-day open or market-on-close (`research-proposed` operational fill assumption; paper evaluates on daily close-to-close series).
- **Transaction Costs:** 0.05% (5 bps) per trade applied in replication baseline (Section 5.2, Table 9) and incorporated into classifier profitability labeling (source-reported).
- **Slippage & Market Impact:** Not modeled in the primary source (`research-proposed` limitation explicitly identified by authors in Section 6).
- **Borrow & Short Availability:** Full borrow availability at 0 cost assumed for S&P 500 constituents (`research-proposed` operational assumption; borrow fees not modeled in source).
- **Capital Allocation:** Self-financing long/short dollar-neutral portfolio; cash buffer for margin requirements not explicitly modeled (`research-proposed`).

## Evidence

### Source-reported

All figures below are directly reported by Jack Fanshawe, Rumi Masih, and Alexander Cameron (arXiv:2601.04602v1, January 2026) over the out-of-sample evaluation period (April 2019 – October 2024; 269,121,442 edge predictions evaluated):

#### 1. Edge-Wise 10-Day Correlation Prediction Performance (Table 1)
- Evaluated across $269{,}121{,}442$ edge-day observations:
  - **MAE:** Reduced from $0.3071$ (20-day historical rolling baseline) to **$0.2302$** (THGNN), a decline of $-0.0769$ ($-25.0\%$).
  - **RMSE:** Reduced from $0.3852$ (persistence baseline) to **$0.2940$** (THGNN), a decline of $-0.0912$ ($-23.7\%$).
  - **Bias (Mean Signed Error):** Improved from $-0.0049$ to **$-0.0012$**.
  - **Pearson Correlation ($r$):** Increased from $0.310$ to **$0.778$** (variance explained $R^2$ rose from $9.6\%$ to $60.5\%$).
  - **Spearman Rank Correlation ($\rho$):** Increased from $0.314$ to **$0.795$** ($+153.2\%$ increase in rank ordering fidelity).

#### 2. Sector-Level Residual Generalization (Table 2)
Average absolute error between predicted and realized 10-day correlations is tightly clustered across all 11 GICS sectors:
- Real Estate: $0.298151$
- Financials: $0.300287$
- Materials: $0.302478$
- Industrials: $0.303522$
- Energy: $0.304135$
- Consumer Discretionary: $0.304656$
- Information Technology: $0.306587$
- Utilities: $0.310401$
- Communication Services: $0.314644$
- Health Care: $0.315660$
- Consumer Staples: $0.317321$

#### 3. Out-of-Sample Trading Performance (Table 3, April 2019 – October 2024)
- **Annualized Return (ARC):** **19.20%** (vs. S&P 500 Buy-and-Hold: 14.43%).
- **Annualized Standard Deviation (ASD):** **0.121** (12.1% vs. S&P 500: 20.4%).
- **Sharpe Ratio:** **1.837** (vs. S&P 500: 0.647).
- **Sortino Ratio:** **2.473** (vs. S&P 500: 0.786).
- **Maximum Drawdown (MDD):** **-9.43%** (vs. S&P 500: -33.93%).
- **Maximum Loss Duration (MLD):** **82 days** (vs. S&P 500: 512 days).
- **Calmar Ratio (CR):** **2.035** (vs. S&P 500: 0.425).
- **Information Ratio (IR):** **0.133** (vs. S&P 500 benchmark).
- **Ledoit-Wolf Bootstrap Sharpe Difference Test:**
  - One-sided $p$-value: **$0.0200$** (rejects null hypothesis of equal Sharpe at 5% level).
  - 95% Percentile Confidence Interval for $\Delta \text{Sharpe}$: $[0.054, 2.147]$.
  - 95% Studentized Confidence Interval: $[-0.123, 2.074]$.

#### 4. Feature Importance & Attention Diagnostics (Sections 5.4–5.5)
- Gradient $\times$ Input saliency indicates that embeddings are dominated by 5 primary features: VIX, crude oil (`DCOILWTICO`), 10-year Treasury yield (`DGS10`), trade-weighted dollar index (`DTWEXBGS`), and sub-industry classification (`gsubind`).
- During crisis regimes (March 2020 COVID shock), intra-sector attention within Energy spiked from $0.05$ to $0.35$, reflecting heightened self-dependence during commodity price collapse.

### Independently reproduced

Not independently reproduced in our execution stack.

### Negative evidence

The authors conducted an explicit empirical replication of Korniejczuk & Ślepaczuk's (2024) backward-looking SPONGEsym ML-filtered strategy over 2000–2024 (Section 5.2, Appendix A.4, Tables 9–10), revealing critical negative findings:
1. **Replication Failure of Backward-Looking ML SPONGEsym:**
   - Under a 0.05% (5 bps) transaction cost, the authors' replication of the original 3-day rebalanced SPONGEsym strategy yielded an Annualized Return of **-0.46%** (Sharpe **0.00**), whereas Korniejczuk & Ślepaczuk reported +2.44% (Sharpe 0.28). Without transaction costs, the authors obtained 8.27% (Sharpe 0.86) vs. the original reported 10.24% (Sharpe 1.17).
   - For the 10-day ML-filtered strategy, while the classifiers achieved identical Brier scores (0.223 vs 0.218 for HGB) and 90% probability thresholds (0.6072 vs 0.6020), the author's backtest **could not reproduce the large performance gains reported in the original paper**.
   - **Root Cause Identified (Survivorship Bias):** Korniejczuk & Ślepaczuk sourced data from Yahoo Finance, which silently drops delisted securities. The authors used WRDS/CRSP, which preserves delisted company return histories. When distressed stocks experience rapid declines into bankruptcy/delisting, survivorship-biased datasets produce artificial alpha that completely evaporates under realistic, point-in-time constituent data.
2. **Crisis Prediction Error Spikes:** While THGNN absolute correlation residuals ($0.20$–$0.30$) were consistently lower than historical persistence baselines ($0.30$–$0.40$), absolute errors still spiked significantly during March 2020 (COVID-19) and February–July 2022 (Russia-Ukraine war), confirming that even advanced deep relational architectures experience elevated error during black-swan structural breaks.
3. **Execution Drag & Omission of Slippage:** The authors explicitly note that no slippage or market impact model was included; given an average holding of 45 stocks rebalanced every 10 days, market impact during volatile regimes will erode reported margins.

## Falsification plan

To falsify or confirm the genuine edge of forward-looking THGNN correlation clustering over backward-looking baselines:
1. **Ablation Falsification (Forward vs. Backward Correlation):**
   - *Test:* Run identical SPONGEsym clustering and ML filtering using: (a) realized rolling 30-day correlation, (b) DCC-GARCH dynamic correlation, and (c) forward-looking THGNN correlation.
   - *Failure condition:* `research-defined falsification threshold`: If the forward-looking THGNN correlation matrix does not achieve a statistically significant Sharpe difference ($p < 0.05$ via Ledoit-Wolf bootstrap) or fails to reduce maximum drawdown by at least 30% relative to rolling correlation, falsify the hypothesis that forward correlation forecasting provides superior clustering alpha.
2. **Transaction Cost & Slippage Stress Test:**
   - *Test:* Apply conservative institutional cost models: 5 bps, 10 bps, 15 bps, and 20 bps round-trip transaction costs plus square-root temporary price impact.
   - *Failure condition:* `research-defined falsification threshold`: If net annualized Sharpe ratio drops below $0.75$ (S&P 500 benchmark Sharpe) under 10 bps total slippage and fee drag, classify the strategy as an execution-sensitive artifact incapable of institutional deployment.
3. **Point-in-Time Universe & Delisting Audit:**
   - *Test:* Evaluate strategy strictly on survivorship-bias-free CRSP data including all delisted returns and liquidation values.
   - *Failure condition:* `research-defined falsification threshold`: If inclusion of delisting returns degrades annualized return by $>4.0\%$ relative to active-only survivorship filtering, reject the portfolio formation rule as contaminated by lookahead or survivorship bias.
4. **Macro Feature Shuffling (Placebo Test):**
   - *Test:* Randomly permute the 10 macroeconomic/risk features across dates while keeping asset return features intact.
   - *Failure condition:* `research-defined falsification threshold`: If the macro-permuted THGNN achieves within 5% of the correlation prediction $R^2$ of the unpermuted model, falsify the claim that macroeconomic conditioning is the driver of regime adaptation.

## Crypto portability

- **Portability Classification:** `adapted/unproven` (research interpretation; the primary source demonstrates the mechanism exclusively in U.S. large-cap equities).
- **Portability Challenges & Structural Differences:**
  1. **Universe Breadth & Network Density:** S&P 500 provides 500 liquid constituents with 10+ years of stable balance sheet and GICS industry structure. Crypto perpetual futures markets have fewer established assets (~50–150 liquid tokens) and lack stable fundamental balance-sheet features (e.g. book-to-market). Sector classifications in crypto (DeFi, L1, AI, Meme) are highly subjective and fluid.
  2. **Correlation Non-Stationarity & Bitcoin Dominance:** Crypto asset cross-correlations are overwhelmingly dominated by BTC market beta (frequently exceeding $0.70$–$0.90$ across all altcoins). Residual return graphs would require rigorous orthogonalization against BTC and ETH market factors prior to graph construction.
  3. **Continuous 24/7 Trading & Funding Fragility:** Equities trade on daily discrete sessions. Crypto perpetuals incur 8-hour funding rates. A 10-day holding period with ~45 long/short positions would incur substantial funding drag if long positions concentrate in high-funding altcoins and short positions in negative-funding tokens.
  4. **Execution Latency & Fragmentation:** Cross-venue liquidity fragmentation across Binance, Bybit, OKX, and DEXs means that correlation breaks often manifest as latency-arbitrage opportunities rather than 10-day mean reversion cycles.

## Limitations

- **Underspecified Execution Timestamps:** The paper evaluates performance on daily close-to-close series without detailing exact order placement mechanisms (e.g. Market-On-Close vs. next-day Open) (`underspecified`).
- **Omission of Slippage and Borrow Costs:** No slippage or borrow fees were simulated in the backtest, which is critical for short positions in single-stock equities (`data gap`).
- **Absence of Architecture Ablations:** The authors did not compare THGNN against standard LSTM, GRU, or Temporal Fusion Transformer baselines for correlation prediction, leaving open whether the full graph attention module is necessary (`research-proposed limitation`).
- **Fixed Hyperparameter Calibration:** The model was trained under a single set of hyperparameters without cross-validation tuning, creating potential sensitivity to the specific $L=30$, $d_{\text{model}}=128$, and 75-epoch configuration (`unproven`).
- **High Turnover & Rebalance Sensitivity:** Rebalancing 45 positions every 10 days generates substantial turnover (~26 portfolio rebalances per year), making profitability vulnerable to widening bid-ask spreads during market sell-offs.

## Implementation status

- `implementation_status: not-implemented`
- No code has been implemented in our research stack (`nautilus-quant-system`, PyBroker, or NautilusTrader).
- No historical backtest, paper trading, or live execution has been performed.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- This record serves strictly as normalized research material documenting a peer-reviewed/preprint deep learning graph architecture and empirical replication critique. It does not constitute approval for trading, implementation, or capital allocation.

## Related Wiki records

- `graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05.md` (predecessor backward-looking SPONGEsym framework by Korniejczuk & Ślepaczuk 2024, which this paper replicates, critiques, and extends via forward correlation forecasting)
- `statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05.md` (deep learning factor replication statistical arbitrage in equities)
- `gaussian-boson-sampling-asset-clustering-statistical-arbitrage-2026-09-02.md` (photonic quantum graph clustering for statistical arbitrage portfolios)
- `graphical-matching-pairs-trading-maximum-weight-matching-2026-09-05.md` (graph-theoretic pairs trading via maximum weight matching)
- `path-signature-decomposition-segmented-levy-area-futures-pair-trading-2026-09-03.md` (path signature filtering in pairs trading)

## Sources

1. **Primary Research Paper:** Jack Fanshawe, Rumi Masih, and Alexander Cameron, *"Forecasting Equity Correlations with Hybrid Transformer Graph Neural Network"*, arXiv:2601.04602v1 [q-fin.CP, q-fin.TR], January 8, 2026. DOI: [10.48550/arXiv.2601.04602](https://doi.org/10.48550/arXiv.2601.04602). Canonical URL: [https://arxiv.org/abs/2601.04602](https://arxiv.org/abs/2601.04602). Direct HTML: [https://arxiv.org/html/2601.04602v1](https://arxiv.org/html/2601.04602v1).
2. **Underlying Baseline Paper:** Adam Korniejczuk and Robert Ślepaczuk, *"Statistical arbitrage in multi-pair trading strategy based on graph clustering algorithms in US equities market"*, arXiv:2406.10695v1 [q-fin.TR], June 2024. [https://arxiv.org/abs/2406.10695](https://arxiv.org/abs/2406.10695).
3. **SPONGE Algorithm Reference:** Álvaro Cartea, Mihai Cucuringu, and Qi Jin, *"Correlation matrix clustering for statistical arbitrage portfolios"*, Quantitative Finance / SSRN: [https://papers.ssrn.com/abstract=4560455](https://papers.ssrn.com/abstract=4560455), 2023.
