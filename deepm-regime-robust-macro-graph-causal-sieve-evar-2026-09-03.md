---
schema: strategy-research-record-v1
title: "DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management via Macro Graph Prior, Directed Delay Causal Sieve, and SoftMin EVaR Optimization"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - deep-learning
  - macro-futures
  - graph-neural-network
  - transfer-entropy
  - causal-sieve
  - entropic-value-at-risk
  - portfolio-optimization
status: research-only
confidence: medium
source_as_of: 2026-03-19
sources:
  - "https://arxiv.org/abs/2601.05975"
  - "https://arxiv.org/html/2601.05975v1"
  - "https://doi.org/10.48550/arXiv.2601.05975"
  - "https://github.com/kieranjwood/deepm/commit/94aa148295d9147f6533f877256b663b918ed2e6"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management via Macro Graph Prior, Directed Delay Causal Sieve, and SoftMin EVaR Optimization

## Provenance

- **Primary Source:** Kieran Wood (Department of Engineering Science & Oxford-Man Institute of Quantitative Finance, University of Oxford), Stephen J. Roberts (Department of Engineering Science & Oxford-Man Institute of Quantitative Finance, University of Oxford), and Stefan Zohren (Department of Engineering Science & Oxford-Man Institute of Quantitative Finance, University of Oxford), *"DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"*, arXiv preprint `arXiv:2601.05975v1 [q-fin.PM, cs.LG]`, submitted January 9, 2026.
- **Canonical Digital Object Identifiers & Preprints:**
  - arXiv Identifier: `arXiv:2601.05975v1`
  - arXiv DOI: [10.48550/arXiv.2601.05975](https://doi.org/10.48550/arXiv.2601.05975)
  - Stable Abstract URL: [https://arxiv.org/abs/2601.05975](https://arxiv.org/abs/2601.05975)
  - Full-Text HTML URL: [https://arxiv.org/html/2601.05975v1](https://arxiv.org/html/2601.05975v1)
- **Primary Source Public Code Repository:**
  - Repository URL: [https://github.com/kieranjwood/deepm](https://github.com/kieranjwood/deepm)
  - Immutable Commit SHA: `94aa148295d9147f6533f877256b663b918ed2e6` (committed March 19, 2026)
  - Key Implementation Modules:
    - `deepm/models/deepm.py` (Complete hierarchical architecture and forward pipeline)
    - `deepm/models/deepm_layers.py` (V-VSN, Causal Sieve cross-attention, Macro Graph GAT layer)
    - `deepm/training/` (Two-pass exact microbatching and SoftMin loss implementation)
    - `configs/` (Detailed hyperparameters and asset universe mapping)
- **Empirical Dataset & Historical Coverage:**
  - 50 diversified global liquid futures and FX contracts sourced from the Pinnacle Data Corp CLC database (ratio-adjusted / "Panama" continuous contracts preserving relative percentage returns and volatility structure).
  - Walk-forward historical window spanning 1990 to 2025, with an out-of-sample test window spanning 2010 to 2025 (inclusive), covering both the low-volatility "CTA Winter" of the 2010s and the post-2020 macro volatility/rate shock regime.

## Economic mechanism

### Source-reported

Systematic macro and Commodity Trading Advisor (CTA) strategies historically rely on two foundational return drivers: trend-following (momentum) and mean reversion. However, traditional implementations exhibit three structural pathologies:
1. **Asynchronous Information ("Ragged Filtration"):** Global macro assets trade across non-overlapping trading sessions (e.g., Nikkei 225 closes many hours before New York markets open). Standard machine learning models that stack contemporaneous daily data create subtle, illusory look-ahead bias by allowing later-closing markets to inform earlier-closing decisions, or by fitting spurious contemporaneous correlations rather than tradable causal signals.
2. **Error Maximization in Two-Stage Pipelines:** Classical "predict-then-optimize" frameworks (e.g., forecasting returns via regression/ML and feeding forecasts into Markowitz Mean-Variance Optimization) amplify estimation error during covariance inversion ($\Sigma^{-1}$), producing high turnover, unstable weights, and severe post-cost degradation.
3. **Regime Fragility & The Inertia Trap:** Objectives targeting pooled average performance (such as unregularized Sharpe ratio) overfit to prolonged calm bull markets while concentrating ruinous drawdowns into brief, turbulent regime transitions. When models attempt to optimize Sharpe without tail-risk regularization, they frequently collapse into an "inertia trap" (holding static low-turnover positions to avoid fees, forfeiting adaptability).

To solve these challenges, the authors propose **DeePM (Deep Portfolio Manager)**, an end-to-end structured deep-learning portfolio manager that incorporates three domain-specific inductive biases:
1. **The Causal Sieve (Directed Delay):** Cross-sectional attention is enforced with a strict one-day lag ($t-1 \to t$). By forcing cross-asset attention to use strictly historical states from the prior close, the model is compelled to learn Transfer Entropy (Granger causality) and predictive impulse-response functions rather than instantaneous, unhedged co-movements.
2. **Macroeconomic Graph Prior:** Latent embeddings are projected onto a fixed 50-node graph $\mathcal{G} = (\mathcal{V}, \mathcal{E})$ encoding deterministic economic transmission channels (intra-sector cliques, risk-on/risk-off linkages, inflation triangles, sovereign carry channels, and regional triangles). An anisotropic Graph Attention Network (GAT) acts as a Bayesian structural prior (Gaussian Markov Random Field), regularizing the high-capacity temporal network and preventing noise memorization in low signal-to-noise environments.
3. **Distributionally Robust SoftMin (EVaR) Optimization:** The network is trained directly on realized net portfolio returns using a combined objective of pooled Sharpe ratio plus a differentiable SoftMin penalty on rolling sub-period Sharpe ratios. This is proven to be mathematically isomorphic to the dual representation of Entropic Value-at-Risk (EVaR), playing an implicit minimax game against an adversary that reweights historical windows to penalize tail stress periods.
4. **Ensemble-Induced Cost Convexity:** By proving that transaction costs are convex in position sequences ($\mathcal{C}(\bar{\mathbf{p}}) \le \frac{1}{K}\sum \mathcal{C}(\mathbf{p}^{(k)})$ via Jensen's inequality), the authors establish that ensembling across diverse seeds structurally dampens turnover, allowing the explicit training penalty scaler to be relaxed ($\gamma = 0.5$) to capture higher-frequency alpha without suffering fee drag.

### Research interpretation

The falsifiable mechanism is an **end-to-end multi-asset inductive bias hierarchy**:
- **Causal Transfer Entropy vs Spurious Co-movement:** In financial markets, contemporaneous cross-sectional correlation $I(X_t; Y_t)$ is symmetric and prone to breakdown under structural shocks. Directed Delay transforms multi-head attention into a non-linear estimator of Transfer Entropy $\mathcal{T}_{j \to i}$, isolating directional information flow (e.g., US sovereign yields leading emerging market currencies). The primary source proves that maximizing information freshness (cascading same-day closes) degrades out-of-sample Sharpe from 0.93 to 0.84, confirming that causal delay is empirically superior to latency minimization in macro horizons.
- **Topological Shrinkage:** High-capacity deep models (Transformers, LSTMs) possess sufficient parameters to overfit noise. Imposing a fixed graph Laplacian penalty $\operatorname{Tr}(Z^\top \mathcal{L} Z)$ enforces smoothness across economically linked assets unless the data likelihood strongly overrides the prior.
- **Convexity of Execution Frictions:** Individual neural network seeds output noisy, high-frequency position fluctuations. Averaging positions across $K=25$ independent seeds before order submission cancels idiosyncratic noise trades, shrinking executed turnover while preserving directional conviction.

## Signal

### Source-reported construction

The strategy generates daily bounded portfolio weights $\mathbf{p}_t = [p_{1,t}, \dots, p_{N,t}]^\top \in [-1, 1]^N$ across $N=50$ continuous futures contracts:

#### 1. Input Stationarization & Preprocessing
For each asset $i$ at day $t$, the input feature vector $x_{i,t} \in \mathbb{R}^F$ is constructed from daily closing prices $P_{i,t}$:
- **Ex-Ante Volatility Normalization:** Compute daily variance $\hat{s}_{i,t}^2$ using a 63-day span Exponentially Weighted Moving Average (EWMA):
  $$\hat{\sigma}_{i,t} = \sqrt{\hat{s}_{i,t}^2}$$
- **Feature Representations:**
  - *Raw Momentum Subset (Baseline):*
    - Volatility-normalized returns over multi-scale lookback horizons $h \in \{1, 21, 63, 252\}$ days:
      $$r_{i,t-h:t}^{\text{norm}} = \frac{P_{i,t} / P_{i,t-h} - 1}{\hat{\sigma}_{i,t} \sqrt{h}}$$
    - Rolling price $Z$-scores over horizons $\ell \in \{21, 252\}$ days:
      $$Z_{i,t,\ell} = \frac{\ln(P_{i,t}) - \mu_{\ell}(P_i)}{\sigma_{\ell}(P_i)}$$
  - *Signal-Based Subset (Evaluated in Table 1 & 2):*
    - 1-day return $r_{1d}$, price $Z$-scores, and multi-scale Moving Average Convergence Divergence (MACD) filters across fast/slow spans $(S,L) \in \{(8,24), (16,48), (32,96)\}$:
      $$\operatorname{MACD}_{i,t}^{(S,L)} = \frac{\operatorname{EWM}_S(P_i) - \operatorname{EWM}_L(P_i)}{\hat{\sigma}_{i,t}}$$
      mapped through a sigmoidal squashing function $\phi(x) = \frac{x e^{-x^2/4}}{0.89}$ and standardized by rolling 252-day standard deviation.
- **Robust Outlier Control:** Each feature $f_{i,t}$ is clipped without lookahead using rolling 252-day median ($m_t$) and Median Absolute Deviation ($\text{MAD}_t$):
  $$f_{i,t}^{\text{clipped}} = \operatorname{clip}\left(f_{i,t}, \, m_t - 5 \times 1.48 \times \text{MAD}_t, \, m_t + 5 \times 1.48 \times \text{MAD}_t\right)$$

#### 2. Network Architecture (DeePM Pipeline)
The model processes the cross-section through three hierarchical layers:
- **Temporal Backbone (Per-Asset):**
  1. *Vectorized Variable Selection Network (V-VSN):* Employs linear projection layers and Gated Residual Networks (GRNs) conditioned on a learned categorical ticker embedding $e_i \in \mathbb{R}^{d_{\text{embed}}}$ to produce dynamic feature selection weights.
  2. *Local Recurrence (LSTM):* A 1-layer LSTM with hidden dimension $d_{\text{model}} \in \{64, 128\}$ models local path dependency and short-term volatility regimes.
  3. *Temporal Multi-Head Attention:* Self-attention across an 84-day sequence window (with 21-day burn-in during training and 63-day burn-in during out-of-sample backtesting) with ReZero residual scaling ($\alpha_{\text{temp}} = 0$ initialization).
- **Cross-Sectional Interaction (Causal Sieve):**
  - Permutation-equivariant Multi-Head Attention across the asset dimension $N$.
  - *Directed Delay Protocol:* Enforces strictly lagged conditioning:
    $$\tilde{H}_t = H_{t-1}$$
    Queries $Q_t$ are generated from the contemporaneous asset state at $t$, but Keys $K_{t-1}$ and Values $V_{t-1}$ are drawn strictly from $t-1$. This guarantees that no intraday or asynchronous information leaks across markets.
- **Structural Regularization (Macro Graph GAT):**
  - The cross-sectional representations are processed by a Graph Attention Network (GAT) masked by the 50-node adjacency matrix $A \in \{0, 1\}^{50 \times 50}$:
    $$\alpha_{ij,t} = \frac{\exp\left( \frac{\langle Q_i, K_j \rangle}{\sqrt{d}} + \ln(A_{ij}) \right)}{\sum_{k \in \mathcal{N}(i)} \exp\left( \frac{\langle Q_i, K_k \rangle}{\sqrt{d}} + \ln(A_{ik}) \right)}$$
    where non-edges ($A_{ij} = 0$) receive $\ln(A_{ij}) \to -\infty$, enforcing strict topology-constrained message passing.
  - Residual connection with ReZero gating:
    $$H_t^{\text{graph}} = H_t^{\text{cross}} + \alpha_{\text{gnn}} \operatorname{GAT}(H_t^{\text{cross}})$$

#### 3. Action Mapping & Volatility-Targeted Position Sizing
- **Raw Action Output:** A final linear projection maps $h_{i,t}^{\text{graph}}$ to a scalar action squashed to $[-1, 1]$:
  $$p_{i,t} = \tanh(\tilde{a}_{i,t})$$
- **Ex-Ante Volatility Allocation:** Raw risk weights $p_{i,t}$ are converted to notional capital weights $w_{i,t}$ targeting an annualized portfolio volatility $\sigma_{\text{tgt}} = 0.10$ (10%):
  $$v_{i,t} = \frac{\sigma_{\text{tgt}} / \sqrt{N_t}}{\hat{\sigma}_{i,t} + \varepsilon}, \qquad w_{i,t} = p_{i,t} \cdot v_{i,t}$$
  where $N_t$ is the number of active/valid assets on day $t$.
- **Ensemble Aggregation:** The executable portfolio is formed by averaging the position weights of the Top $K=25$ models (selected from 50 random seeds based on smoothed validation Sharpe ratio):
  $$\bar{\mathbf{w}}_t = \frac{1}{K} \sum_{k=1}^K \mathbf{w}_t^{(k)}$$

#### 4. Loss Function & Exact Optimization Protocol
The model is trained end-to-end on realized net return series $R_t^{\text{net}} = \sum_i w_{i,t} y_{i,t+1} - \gamma \sum_i c_i |w_{i,t} - w_{i,t-1}|$ using a combined objective:
$$\mathcal{L} = \mathcal{L}_{\text{pool}} + \lambda \mathcal{L}_{\text{soft}}$$
- **Pooled Sharpe Loss:**
  $$\mathcal{L}_{\text{pool}} = -\sqrt{252} \cdot \frac{\hat{\mu}_{\text{pool}}}{\hat{\sigma}_{\text{pool}} + \varepsilon_{\sigma}}$$
- **SoftMin Tail Loss (Differentiable EVaR Proxy):** Partitioning the training sequence into $B$ non-overlapping quarterly blocks with Sharpe ratios $\text{SR}_b$:
  $$\mathcal{L}_{\text{soft}} = \tau \ln\left( \frac{1}{B} \sum_{b=1}^B \exp\left( \frac{-\text{SR}_b}{\tau} \right) \right)$$
  Optimal hyperparameter values: temperature $\tau = 0.2$ (with $\tau=0.5$ in baseline ablations), scalar $\lambda = 0.1$ (or $0.2$).
- **Cost Regularizer:** $\gamma = 0.5$ (training with half-costs prevents the model from freezing into the inertia trap while allowing the ensemble to structurally eliminate turnover).
- **Two-Pass Exact Microbatching:** To optimize non-separable batch Sharpe statistics on limited GPU memory without approximation error, training uses a two-pass algorithm: Phase 1 accumulates sufficient statistics ($\sum R_t, \sum R_t^2$), and Phase 2 evaluates analytical upstream gradients $\nabla_R \mathcal{L}$ injected directly into the backward graph.

## Required data

- **Universe:** 50 liquid continuous futures and FX contracts across 6 macro groups:
  1. *Sovereign Rates (9):* US 2yr Note (`TU`), US 5yr Note (`FV`), US 10yr Note (`TY`), US 30yr Bond (`US`), Euro Schatz (`DU`), German Bobl (`OE`), Euro Bund (`RX`), Long Gilt (`G`), Canada 10yr Bond (`CN`).
  2. *Equities (9):* S&P 500 (`ES`), Nasdaq 100 (`EN`), Dow Jones (`YM`), Russell 2000 (`RTY`), EuroStoxx 50 (`VG`), FTSE 100 (`Z`), CAC 40 (`CF`), Nikkei 225 (`NK`), Hang Seng (`HI`).
  3. *Foreign Exchange (7):* Dollar Index (`DX`), EUR/USD (`EU`), JPY/USD (`JY`), GBP/USD (`BP`), CAD/USD (`CD`), AUD/USD (`AD`), CHF/USD (`SF`), Mexican Peso (`PE`).
  4. *Energy Commodities (5):* WTI Crude (`CL`), Brent Crude (`CO`), RBOB Gasoline (`XB`), Gasoil (`QS`), Natural Gas (`NG`).
  5. *Metals Commodities (5):* Gold (`GC`), Silver (`SI`), Platinum (`PL`), Palladium (`PA`), High Grade Copper (`HG`).
  6. *Agriculture & Livestock (14):* Corn (`C`), Soybeans (`S`), Soybean Meal (`SM`), Soybean Oil (`BO`), Wheat (`W`), KC Wheat (`KW`), Sugar (`SB`), Coffee (`KC`), Cocoa (`CC`), Cotton (`CT`), Orange Juice (`JO`), Live Cattle (`LC`), Feeder Cattle (`FC`), Lean Hogs (`LH`).
- **Data Source & Continuity:** Daily closing prices from Pinnacle Data Corp CLC Database. Continuous roll stitching via ratio-adjusted ("Panama") methodology to preserve volatility and return scaling across contract expirations.
- **Timeframe & Granularity:** Daily bars ($t$), 252 trading days per calendar year.
- **Point-in-Time Integrity:** Strict Directed Delay ($H_{t-1} \to H_t$) ensures decisions executed for day $t+1$ use only data available through day $t-1$ for cross-sectional operations, eliminating any asynchronous session-timing leakage.
- **Missing Data & Universe Masking:** Availability mask $m_{i,t} \in \{0, 1\}$ and key-padding mask in cross-sectional attention; forward-filled price data is masked out during loss calculation.

## Execution assumptions

- **Execution Timing & Return Accounting:** Next-day close-to-close arithmetic returns:
  $$y_{i,t+1} = \frac{P_{i,t+1} - P_{i,t}}{P_{i,t}} \cdot \frac{1}{\hat{\sigma}_{i,t}}$$
- **Order Model:** Execution assumed at closing price of day $t$ (or open of $t+1$), with positions held until the subsequent rebalance.
- **Structural Minimum Cost Model:** Frictions $c_i = C_{\text{struct}} \times \lambda_i$ incorporate exchange minimum price variation (tick size) and institutional depth/session impact scalars:
  - *0.25 bps:* Ultra-Liquid benchmark contracts (`TU`, `FV`, `DU`, `ES`, `EN`, `YM`, `EU`, `GC`).
  - *0.50 bps:* Very Liquid contracts (`RX`, `G`, `CN`, `RTY`, `Z`, `CF`, `DX`, `JY`, `BP`, `CD`, `AD`, `SF`).
  - *0.75 bps:* Liquid physical commodities and benchmark notes (`TY`, `HI`, `CL`, `CO`, `HG`).
  - *1.00 bps:* Standard liquidity contracts (`VG`, `PE`, `SI`).
  - *1.50 bps:* Mid-liquidity rates and energy products (`US`, `OE`, `NK`, `XB`, `QS`, `PL`, `S`, `BO`, `LC`).
  - *2.50 bps:* High-cost volatile agricultural and livestock products (`NG`, `C`, `SM`, `W`, `KW`, `SB`, `KC`, `CT`, `FC`, `LH`).
  - *6.00 bps:* Thin order book / "Roach Motel" contracts (`PA` Palladium, `CC` Cocoa).
  - *15.00 bps:* Distressed / "widowmaker" liquidity contract (`JO` Orange Juice).
- **Leverage & Volatility Target:** Total portfolio notionals scaled daily to maintain an annualized portfolio volatility target $\sigma_{\text{tgt}} = 0.10$ (10%).

## Evidence

### Source-reported

All quantitative figures below are transcribed directly from Kieran Wood, Stephen J. Roberts, and Stefan Zohren (arXiv:2601.05975v1, Tables 1, 2, 3, 4, and 5) evaluated out-of-sample over 2010–2025:

#### 1. Out-of-Sample Performance (Full 15-Year Test Window: 2010–2025)
*All strategies scaled to 10% annualized target volatility; net metrics include full structural transaction costs (Table 1):*

| Strategy / Specification | Gross SR | Net SR | HAC $t$-stat | CAGR (%) | Calmar Ratio | Max Drawdown (%) | Implied Holding Period (Days) | Net IR (vs Bench.) | Alpha $t$-stat ($t_\alpha$) | Correlation vs Bench. ($\rho$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **DeePM (Proposed Ensemble, Top 25)** | **1.29** | **0.93** | **3.69** | **9.2%** | **0.58** | **-16.0%** | **7.1** | **0.44** | **1.85** | **0.52** |
| DeePM (MACD features) | 1.10 | 0.84 | 3.26 | 8.2% | 0.49 | -16.9% | 10.4 | 0.38 | 1.57 | 0.61 |
| *Baselines* | | | | | | | | | | |
| Passive Equal Risk (Bench.) | 0.50 | 0.50 | 1.90 | 4.6% | 0.17 | -27.1% | $\infty$ | - | - | 1.00 |
| Trend (TSMOM 12M) | 0.51 | 0.45 | 1.75 | 4.1% | 0.21 | -19.8% | 32.2 | -0.03 | -0.10 | 0.02 |
| Risk Managed Trend | 0.49 | 0.39 | 1.50 | 3.5% | 0.13 | -26.8% | 14.6 | -0.07 | -0.26 | 0.02 |
| MVO Trend (Two-stage) | 0.55 | -0.07 | -0.26 | -1.2% | -0.02 | -51.4% | 5.1 | -0.41 | -1.56 | 0.05 |
| MVO-TP Trend ($\kappa=10$) | 0.59 | 0.47 | 1.79 | 4.3% | 0.15 | -28.8% | 15.1 | -0.01 | -0.05 | 0.06 |
| Risk Parity Trend (ERC) | 0.35 | 0.18 | 0.75 | 1.4% | 0.04 | -32.2% | 9.9 | -0.22 | -0.83 | 0.04 |
| MACD Multi-Scale | 0.28 | 0.25 | 1.00 | 2.0% | 0.08 | -23.8% | 38.5 | -0.17 | -0.66 | -0.05 |
| Risk Managed MACD | 0.26 | 0.20 | 0.81 | 1.5% | 0.05 | -27.9% | 16.0 | -0.20 | -0.80 | -0.04 |
| MVO-TP MACD | 0.24 | 0.15 | 0.61 | 1.0% | 0.04 | -23.6% | 16.6 | -0.24 | -0.97 | 0.01 |
| Momentum Transformer ($\gamma=0$) | 1.10 | 0.60 | 2.44 | 5.6% | 0.21 | -26.3% | 4.0 | 0.10 | 0.42 | 0.45 |
| Momentum Transformer ($\gamma=0.5$) | 1.02 | 0.66 | 2.54 | 6.2% | 0.20 | -31.9% | 5.0 | 0.15 | 0.60 | 0.39 |

#### 2. Key Architectural & Objective Ablations (2010–2025, Table 1)
- **Filtration Protocol:**
  - *Directed Delay ($t-1$, Proposed):* Net SR 0.93, MDD -16.0%, Hold 7.1 days.
  - *Cascading Lag (Same-day where closed earlier):* Net SR drops to 0.84, MDD worsens to -18.7%, Hold 7.5 days. Enforcing causal delay outperforms maximizing information freshness.
- **Cross-Sectional Structure & Graph Prior:**
  - *Independent (No cross-sectional structure):* Net SR 0.83, MDD -17.0%.
  - *No Graph (Cross-Attn Only):* Net SR drops to 0.79, MDD worsens to -19.8%. Unconstrained attention overfits spurious cross-sectional noise.
  - *No Cross-Attn (Graph Only):* Net SR 0.84, MDD -18.4%. Static economic priors alone lack dynamic regime adaptation.
  - *Flipped Order (Graph then Cross-Attn):* Net SR drops to 0.87, MDD worsens to -19.8%. The graph functions best as an output denoiser/regularizer.
  - *Isotropic GCN (Fixed degree weights):* Net SR drops to 0.81, confirming the necessity of anisotropic GAT attention.
  - *No ReZero:* Net SR drops to 0.71, MDD -17.0%, Hold 14.5 days.
- **Objective Function & Robustness:**
  - *No SoftMin (Pooled Sharpe Only):* Net SR drops sharply from 0.93 to 0.68 (-27%), Hold expands to 18.4 days. Without worst-window EVaR penalties, the optimizer collapses into the "inertia trap."
  - *SoftMin $\tau = 1.0$ (Loose/Soft):* Net SR drops to 0.85, MDD -15.5%.
  - *SoftMin $\tau = 0.05$ (Hard Minimax):* Net SR drops to 0.83, MDD -16.7%.
- **Cost Scaling Factor ($\gamma$):**
  - *Zero Cost ($\gamma = 0$):* Gross SR 1.17, Net SR collapses to 0.56, MDD -32.1%, Hold 4.9 days (severe noise overtrading).
  - *Full Cost ($\gamma = 1.0$):* Net SR 0.70, MDD -16.4%, Hold 19.0 days (excessively suppressed turnover).
  - *Intermediate Cost ($\gamma = 0.5$, Proposed):* Optimal Net SR 0.93, Hold 7.1 days.
- **Ensemble Size:**
  - *Best Single Seed ($K=1$):* Net SR 0.72 ($t = 2.88$), MDD -16.8%, Hold 6.6 days.
  - *Top 10 Seeds ($K=10$):* Net SR 0.93 ($t = 3.63$), MDD -16.3%, Hold 6.7 days.
  - *Top 25 Seeds ($K=25$, Baseline):* Net SR 0.93 ($t = 3.69$), MDD -16.0%, Hold 7.1 days.
  - *All 50 Seeds ($K=50$):* Net SR 0.86 ($t = 3.33$), MDD -14.7%, Hold 10.7 days.
  - *100-Seed Search ($K=50$):* Net SR 0.93 ($t = 3.64$), MDD -16.9%, Hold 7.6 days, $t_\alpha = 1.93$ ($p \approx 0.05$).

#### 3. Post-2020 Regime Resilience (Table 2: 2020–2025)
*Evaluates performance across the COVID-19 shock, inflation spikes, and global central bank rate-hiking cycles:*
- **DeePM (Proposed):** Gross SR 1.07, Net SR 0.79 ($t = 1.84$), CAGR 7.7%, Calmar 0.56, MDD -13.8%, Hold 8.0 days, Net IR 0.45, $t_\alpha = 1.16$, $\rho = 0.57$.
- **DeePM (MACD features):** Gross SR 1.16, Net SR 0.97 ($t = 2.20$), CAGR 9.6%, Calmar 0.65, MDD -14.9%, Hold 11.4 days, Net IR 0.68, $t_\alpha = 1.67$, $\rho = 0.62$.
- **Passive Equal Risk:** Net SR 0.37 ($t = 0.84$), CAGR 3.2%, MDD -18.8%, Calmar 0.17.
- **TSMOM:** Net SR 0.38 ($t = 0.89$), CAGR 3.3%, MDD -18.9%, Calmar 0.18.
- **Momentum Transformer ($\gamma=0.5$):** Net SR 0.38 ($t = 0.87$), CAGR 3.3%, MDD -20.7%, Calmar 0.16.

### Independently reproduced

Not independently reproduced. All empirical performance figures are transcribed directly from arXiv:2601.05975v1 and the author's public code repository.

### Negative evidence

- **Catastrophic Failure of Unregularized Two-Stage Optimization:** Traditional Mean-Variance Optimization (MVO Trend) delivered a negative Net Sharpe ratio of -0.07 ($t = -0.26$) with a catastrophic Maximum Drawdown of -51.4% and an implied holding period of 5.1 days, corroborating Michaud's "error maximization" critique under realistic transaction costs.
- **Failure of Unconstrained Attention (No Graph):** Removing the macroeconomic graph prior degrades Net Sharpe from 0.93 to 0.79 and increases MDD from -16.0% to -19.8%, proving that unconstrained multi-head attention across financial assets overfits spurious correlations.
- **Failure of Maximizing Information Freshness (Cascading Filtration):** Conditioned on same-day closing data from earlier-closing markets, Net Sharpe fell to 0.84 with deeper MDD (-18.7%), confirming that intraday market co-movements act as non-stationary noise that corrupts causal signal extraction.
- **Inertia Trap Under Standard Sharpe Loss:** Without the SoftMin tail-risk penalty ($\mathcal{L}_{\text{soft}}$), the model retreated to an inactive holding pattern (holding period expanding from 7.1 days to 18.4 days), dropping Net Sharpe from 0.93 to 0.68.
- **Sensitivity to Zero Cost Training ($\gamma=0$):** Training without an explicit turnover penalty caused immediate over-trading (holding period collapsed to 4.9 days), destroying net returns (Net Sharpe dropped from 1.29 gross to 0.56 net).

## Falsification plan

The following operational tests would refute or materially weaken the DeePM hypothesis:
1. **Topological Graph Permutation / Placebo Test:** Randomly shuffle the 50-node adjacency matrix $A$ (destroying sector and macroeconomic transmission edges while preserving node degree distribution). If the randomized graph achieves Net Sharpe $\ge 0.90$ or matches the true macro graph, the hypothesis that economic domain structure provides genuine inductive bias is falsified.
2. **Causal Direction Inversion:** Invert the Directed Delay protocol such that time $t$ queries attend to future states $t+1$ (in-sample leakage verification) or swap Query and Key roles. Furthermore, test against a synchronous synthetic benchmark: if synchronous attention outperforms Directed Delay when tested in an environment with zero latency, the "Transfer Entropy" hypothesis is weakened.
3. **Transaction Cost Stress & Spread Multiplication:** Scale the structural cost multiplier $\lambda_i$ by $2.0\times$ and $3.0\times$. If the net performance collapses below passive equal risk (Net SR $< 0.50$), the strategy's operational edge is an artifact of cost underestimation.
4. **Out-of-Sample Horizon Expansion (Post-2025):** Evaluate on live, untouched daily data from 2026 onwards without retraining. If Net Sharpe drops below 0.30 or maximum drawdown exceeds -25%, the learned representations failed to generalize across newly emerging macroeconomic regimes.
5. **Ablation of SoftMin EVaR Objective:** Train the exact architecture using standard MSE return forecasting followed by quadratic programming, or using unweighted pooled Sharpe. If the resulting policy matches the performance and stability of SoftMin training, the mathematical necessity of EVaR minimax optimization is refuted.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Portability Justification & Gaps:**
  - *No Crypto Evidence in Primary Source:* The authors evaluated exclusively traditional macroeconomic futures (sovereign bonds, equity indices, commodity futures, fiat FX). They did not evaluate cryptocurrency spot or perpetual markets.
  - *24/7 Continuous Trading vs Asynchronous Session Closes:* Traditional markets have discrete, geographically fragmented session closes (Tokyo 15:00 JST, London 16:30 GMT, New York 16:00 EST). In 24/7 crypto markets, session boundaries are synthetic (e.g., UTC 00:00). The "Causal Sieve" delay must be adapted to discrete multi-hour or daily snapshot intervals.
  - *Macroeconomic Graph Topology in Crypto:* Traditional channels (Sovereign Rates $\to$ FX Carry, Crude $\to$ Agriculture) do not directly exist in crypto. A crypto graph prior would need to represent Layer-1 ecosystems (e.g., ETH, SOL, AVAX), DeFi liquidity infrastructure, exchange utility tokens, and BTC beta transmission channels. Specifying an ex-ante graph prior without lookahead or curve-fitting is significantly more difficult in crypto.
  - *Perpetual Funding Drag & Liquidations:* Crypto perpetuals incur continuous 8-hour funding payments and extreme cascade liquidation risks. Sizing models must incorporate funding rates directly into the net return formulation $R_t^{\text{net}}$.
  - *Extreme Tail Risk:* Crypto daily return distributions exhibit much higher excess kurtosis than traditional macro futures; the SoftMin temperature $\tau$ and burn-in length would require re-calibration to avoid premature model collapse.

## Limitations

- **Source Ambiguity & Implementation Gaps:**
  - Historical backtests rely on Pinnacle continuous Panama-adjusted contracts; differences in rollover conventions (open interest vs volume rollover) can introduce tracking discrepancies in live implementation.
  - While transaction costs model tick size and liquidity scalars rigorously, they omit execution slippage from high-participation market impact during liquidity crises (e.g., March 2020 flash crash).
- **Ensemble Compute Requirement:**
  - Achieving the headline Net Sharpe of 0.93 requires training 50 independent neural network seeds and executing the averaged positions of the Top 25 seeds. Single-model performance drops to Net Sharpe 0.72 ($t=2.88$), introducing substantial operational complexity and GPU compute overhead during retraining.
- **Fixed Graph Subjectivity:**
  - The 50-node macro graph prior $\mathcal{G}$ was hand-constructed from economic theory. Although specified ex-ante, there remains subjective discretion in edge assignments (e.g., classifying specific agricultural commodities into input-cost cliques).
- **Status Markers:**
  - `not independently reproduced`
  - `adapted` (for crypto applications)
  - `not-implemented` in internal production stack

## Implementation status

- `not-implemented`
- This record represents an upstream academic research capture. No code has been integrated into `nautilus-quant-system`, PyBroker, or NautilusTrader, and no historical verification on internal institutional tick data has been performed.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`
- This record is strictly research material. Its presence in this repository does **not** constitute authorization for paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- [[quant/entropic-value-at-risk-tempered-stable-levy-portfolio-optimization-2026-09-02]]
- [[quant/volatility-targeting-risk-parity-constrained-2026-08-28]]
- [[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]
- [[quant/execution-impact-capacity-almgren-square-root-2026-08-28]]
- [[quant/futures-volatility-normalized-tick-size-trend-following-filter-2026-09-02]]
- [[quant/portfolio-covariance-and-shrinkage-2026-08-28]]
- [[quant/phase8-financial-ml-sample-leakage-contract-2026-08-28]]

## Sources

1. **Primary Academic Preprint:** Kieran Wood, Stephen J. Roberts, and Stefan Zohren (Department of Engineering Science & Oxford-Man Institute of Quantitative Finance, University of Oxford), *"DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"*, arXiv preprint `arXiv:2601.05975v1 [q-fin.PM, cs.LG]`, submitted January 9, 2026. DOI: [https://doi.org/10.48550/arXiv.2601.05975](https://doi.org/10.48550/arXiv.2601.05975). Stable URL: [https://arxiv.org/abs/2601.05975](https://arxiv.org/abs/2601.05975). Full-text HTML: [https://arxiv.org/html/2601.05975v1](https://arxiv.org/html/2601.05975v1).
2. **Primary Source Code Repository:** Kieran Wood, *"DeePM: Official PyTorch Implementation"*, GitHub repository: [https://github.com/kieranjwood/deepm](https://github.com/kieranjwood/deepm). Immutable Commit SHA: `94aa148295d9147f6533f877256b663b918ed2e6` (committed March 19, 2026).
3. **Foundation Frameworks Cited by Primary Source:**
   - Bryan Lim, Stefan Zohren, and Stephen Roberts, *"Enhancing time-series momentum strategies using deep neural networks"*, *The Journal of Financial Data Science*, Vol. 1, No. 4, pp. 19–38, 2019. DOI: [10.3905/jfds.2019.1.015](https://doi.org/10.3905/jfds.2019.1.015).
   - Kieran Wood, Sven Giegerich, Stephen Roberts, and Stefan Zohren, *"Trading with the Momentum Transformer: An Intelligent and Interpretable Architecture"*, arXiv:2112.08534, 2021 / *Journal of Financial Data Science*, 2023.
   - Thomas N. Kipf and Max Welling, *"Semi-Supervised Classification with Graph Convolutional Networks"*, *ICLR*, 2017. arXiv:1609.02907.
   - Petar Veličković, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro Liò, and Yoshua Bengio, *"Graph Attention Networks"*, *ICLR*, 2018. arXiv:1710.10903.
   - Arash Ahmadi-Javid, *"Entropic value-at-risk: a new coherent risk measure"*, *Journal of Optimization Theory and Applications*, Vol. 155, No. 3, pp. 1105–1123, 2012. DOI: [10.1007/s10957-011-9978-2](https://doi.org/10.1007/s10957-011-9978-2).
   - Thomas Schreiber, *"Measuring Information Transfer"*, *Physical Review Letters*, Vol. 85, No. 2, pp. 461–464, 2000. DOI: [10.1103/PhysRevLett.85.461](https://doi.org/10.1103/PhysRevLett.85.461).
