---
schema: strategy-research-record-v1
title: "Market-Informed Network Hüsler–Reiss Models for Financial Extremes: Joint Extremes Adjacency Matrix (JEAM) Regularization and Intraday Tail Risk Forecasting"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - extreme-value-theory
  - husler-reiss
  - network-models
  - joint-extremes-adjacency-matrix
  - jeam
  - high-frequency-trading
  - score-matching
  - tail-risk-forecasting
  - asymmetric-dependence
status: research-only
confidence: high
source_as_of: 2026-09-11
sources:
  - "Ayla Jungbluth, Johannes Lederer, and Simon Trimborn, 'Market-Informed Networks for Modeling and Forecast Evaluation of Financial Extremes', arXiv:2609.11575v1 [stat.ME, q-fin.ST], submitted September 10, 2026, listed September 11, 2026. Stable URLs: https://arxiv.org/abs/2609.11575, https://arxiv.org/html/2609.11575v1, https://arxiv.org/pdf/2609.11575v1; DOI: 10.48550/arXiv.2609.11575 (CC BY 4.0)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Market-Informed Network Hüsler–Reiss Models for Financial Extremes: Joint Extremes Adjacency Matrix (JEAM) Regularization and Intraday Tail Risk Forecasting

## Provenance

- **Primary Research Paper:** Ayla Jungbluth, Johannes Lederer, and Simon Trimborn, *"Market-Informed Networks for Modeling and Forecast Evaluation of Financial Extremes"*, arXiv preprint `arXiv:2609.11575v1 [stat.ME]`, submitted September 10, 2026, announced September 11, 2026 (`source-reported`).
  - Author Affiliations:
    - Ayla Jungbluth: Department of Mathematics, Ruhr-University Bochum, Bochum, Germany (`ayla.jungbluth@rub.de`)
    - Johannes Lederer: Department of Mathematics, Computer Science, and Natural Sciences, University of Hamburg, Hamburg, Germany (`johannes.lederer@uni-hamburg.de`)
    - Simon Trimborn: Amsterdam School of Economics & Tinbergen Institute, University of Amsterdam, Amsterdam, Netherlands (`simon.trimborn@uva.nl`)
  - Canonical arXiv Abstract: `https://arxiv.org/abs/2609.11575`
  - Canonical Full-Text HTML: `https://arxiv.org/html/2609.11575v1`
  - Canonical Full-Text PDF: `https://arxiv.org/pdf/2609.11575v1`
  - Canonical DOI: [10.48550/arXiv.2609.11575](https://doi.org/10.48550/arXiv.2609.11575)
  - License: Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Primary Source Verification:** Direct inspection and auditing of the full-text manuscript, mathematical equations (1)–(13), simulation tables (Tables 1, 5, 6), and out-of-sample empirical forecast evaluation tables (Tables 2, 3, 4) in `arXiv:2609.11575v1`. No secondary search snippets, AI aggregator summaries, or synthetic extrapolations were used to formulate strategy mechanics or empirical figures.
- **Repository Deduplication Audit:** A comprehensive audit of all existing records in `alpha-strategy-research` confirmed zero prior records citing `arXiv:2609.11575`, Ayla Jungbluth, Johannes Lederer, Simon Trimborn, or the Joint Extremes Adjacency Matrix (JEAM) framework. An adjacent record, `crypto-dynamic-conditional-tail-dependence-husler-reiss-extremal-graph-2026-09-01.md` (based on Mallela & Leonelli 2026, arXiv:2606.16840), examined static rolling bivariate extremal graphical models on daily cryptocurrency returns without temporal lag vectors, without score matching, and without market-informed network regularization. JEAM constitutes an independent, source-complete research capture.

## Economic mechanism

### Source-reported

1. **The Local vs. Global Extremes Paradox in High-Frequency Finance:**
   Hüsler–Reiss distributions are the canonical multivariate max-stable distributions arising as limits of componentwise maxima of multivariate normal random vectors. In high-frequency time series applications, data are partitioned into equidistant temporal blocks (e.g., 5-minute blocks), and the local maximum or minimum within each block is extracted as an extreme value. However, during calm market regimes, a locally extreme observation within a 5-minute window is not extreme relative to the full marginal distribution across months or years; it represents ordinary bid-ask bounce or noise. Fitting unregularized Hüsler–Reiss models to local extremes distorts parameter estimates, introducing severe bias during non-crisis periods while failing to capture true structural shifts during crisis cascades.
2. **Systemic Joint Extreme Clustering:**
   Financial asset returns exhibit pronounced tail clustering: extreme losses (and extreme gains) frequently co-occur across multiple equities and sectors simultaneously due to macroeconomic news releases, sudden institutional order-flow imbalances, and liquidation cascades. Conversely, in the center of the return distribution, asset co-movements reflect ordinary sector factor loadings. Standard multivariate models with time-invariant parameters fail to distinguish between idiosyncratic local fluctuations and coordinated systemic co-jumps.
3. **Market-Informed Network Regularization (The JEAM Paradigm):**
   To resolve the local vs. global paradox, the authors introduce a time-dependent network Hüsler–Reiss framework estimated via score matching. Instead of treating every observed vector equally, a dynamic adjacency vector $\mathbf{a}_t \in [0, 1]^{d\ell}$ regularizes the score function. The Joint Extremes Adjacency Matrix (JEAM) determines the weight of an observation by forming a convex combination of two distinct economic signals:
   - *Individual Marginal Extremeness:* Evaluated through the asset's empirical cumulative distribution function (ECDF) across all past observations ($F_j(x_{t,j})$).
   - *Systemic Pattern Similarity:* Evaluated through cosine similarity between the current multi-asset extreme vector $\mathbf{x}_t$ and historical clusters of simultaneous cross-sectional extreme co-occurrences ($\mathcal{C}_t$).
   This allows the model to dynamically up-weight observations that represent true global systemic shocks while down-weighting isolated, local noise fluctuations.

### Research interpretation

- **Asymmetric Tail Risk Gating & Regime-Dependent Beta Neutralization:**
   The economic rationale for quantitative portfolio management is that downside co-dependence is structural and sticky during market panics (assets "crash together"), whereas upside co-dependence is more dispersed. By estimating separate time-dependent Hüsler–Reiss precision matrices for lower-tail block minima (losses) and upper-tail block maxima (gains), a quantitative desk can track the real-time degree of systemic fragility. When the JEAM systemic similarity metric $\max_{c \in \mathcal{C}_t} \text{sim}(\mathbf{x}_t, \mathbf{p}_c)$ spikes in the lower tail, cross-asset diversification vanishes into a single dense risk block; holding unhedged long beta results in severe portfolio drawdown.
- **Dispersion Alpha in Decoupled Tail Regimes:**
   When the estimated network precision matrix indicates lower-tail independence (low systemic co-movement), cross-sectional idiosyncratic momentum, statistical arbitrage, and pairs-trading strategies can operate at full capacity without fear of common factor liquidations. Conversely, when upper-tail systemic similarity spikes across a sector, momentum continuation is coordinated, allowing trend-following overlays to participate in concentrated sector rallies.

## Signal

The predictive signal pipeline operates on 5-minute block extrema extracted from 1-minute intraday returns (`source-reported`):

```text
[1-minute High-Frequency OHLCV Return Panel: d assets]
                          ↓
[Block Extremum Extraction: 5-minute non-overlapping blocks]
  - Lower Tail (Minima Run): x_(t,j) = |min_(s in block) r_(s,j)|
  - Upper Tail (Maxima Run): x_(t,j) = max_(s in block) r_(s,j)
                          ↓
[Standardized Pareto Transformation for Hüsler-Reiss Modeling]
                          ↓
[Stacked Temporal Lag Vector: x_t^(ell) in R^(d*ell)]
  - x_t^(ell) = [x_(t-ell+1, 1), ..., x_(t-ell+1, d), ..., x_(t, 1), ..., x_(t, d)]^T
                          ↓
[Joint Extremes Adjacency Matrix (JEAM) Computation: a_t^(3) in [0, 1]^(d*ell)]
  - Marginal ECDF: F_j(x_(t,j)) = (1 / (t-1)) * sum_(s=1)^(t-1) 1_{x_(s,j) <= x_(t,j)}
  - Historical Joint Cluster Set: C_t = {s <= t-w-1 : (1/d) * sum_j 1_{F_j(x_(s,j)) > p} > kappa}
  - Characteristic Cluster Pattern: p_c = (1 / card(W_c)) * sum_(s in W_c) x_s
  - Cosine Pattern Similarity: sim(x_t, p_c) = (x_t^T * p_c) / (||x_t||_2 * ||p_c||_2)
  - Convex Combination: a_(t,j)^(3) = g * max(0, max_(c in C_t) sim(x_t, p_c)) + (1-g) * F_j(x_(t,j))
                          ↓
[Score-Matching Optimization with Adjacency Weighting]
  - min_(mu, Lambda) sum_(t=1)^T o[mu, Lambda, x_t^(ell), a_t]
  - Extract Hüsler-Reiss Precision Matrix: Theta = Lambda + Lambda^T - diag(Lambda*1 + Lambda^T*1)
                          ↓
[One-Step-Ahead Probabilistic Forecast & Systemic Risk Gating Evaluation]
```

### 1. Mathematical Formulation (`source-reported`)

#### Stacked Temporal Extremes Vector
For $d$ time series observed over consecutive blocks, the lagged and contemporaneous extreme vectors are defined as:
$$\mathbf{x}_t^{(\ell)} := [x_{t-\ell+1, 1}, \dots, x_{t-\ell+1, d}, \dots, x_{t, 1}, \dots, x_{t, d}]^\top \in \mathbb{R}_+^{d\ell}$$
where $\ell \in \mathbb{N}$ denotes the autoregressive lag length selected via the Akaike Information Criterion (AIC).

#### Hüsler–Reiss Parameterization and Precision Matrix
The density of $\mathbf{x}_t^{(\ell)}$ is parameterized by a location vector $\boldsymbol{\mu} \in \mathbb{R}^{d\ell}$ and a variogram matrix $\boldsymbol{\Lambda} \in \mathbb{R}^{d\ell \times d\ell}$:
$$h[\mathbf{x}_t^{(\ell)}; \boldsymbol{\mu}, \boldsymbol{\Lambda}] = \frac{1}{c_{\boldsymbol{\mu}, \boldsymbol{\Lambda}}} \left(\prod_{k=1}^{d\ell} \frac{1}{x_{t,k}^{(\ell)}}\right) \exp\left(\boldsymbol{\mu}^\top \log[\mathbf{x}_t^{(\ell)}] - \frac{1}{2} \log[\mathbf{x}_t^{(\ell)}]^\top \boldsymbol{\Theta} \log[\mathbf{x}_t^{(\ell)}]\right)$$
where the precision matrix $\boldsymbol{\Theta} \in \mathbb{R}^{d\ell \times d\ell}$ is given by:
$$\boldsymbol{\Theta} = \boldsymbol{\Lambda} + \boldsymbol{\Lambda}^\top - \text{diag}\left(\boldsymbol{\Lambda}\mathbf{1} + \boldsymbol{\Lambda}^\top\mathbf{1}\right)$$

#### Score-Matching Estimation with Adjacency Regularization
Direct maximum likelihood is computationally intractable in high dimensions. The authors employ score matching (Hyvärinen 2005; Lederer & Oesting 2024), where the score function is regularized by the time-varying adjacency vector $\mathbf{a}_t \in [0, 1]^{d\ell}$:
$$s_k[\mathbf{x}_t^{(\ell)}; \boldsymbol{\mu}, \boldsymbol{\Lambda}, \mathbf{a}_t] = \frac{a_{t,k}\mu_k - 1 - \left(\boldsymbol{\Theta}(\mathbf{a}_t \circ \log[\mathbf{x}_t^{(\ell)}])\right)_k}{x_{t,k}^{(\ell)}}$$
The score-matching estimator minimizes the convex objective:
$$\hat{\boldsymbol{\mu}}, \hat{\boldsymbol{\Lambda}} = \arg\min_{\boldsymbol{\mu}, \boldsymbol{\Lambda}} \sum_{t=1}^T o[\boldsymbol{\mu}, \boldsymbol{\Lambda}, \mathbf{x}_t^{(\ell)}, \mathbf{a}_t]$$
where:
$$o[\boldsymbol{\mu}, \boldsymbol{\Lambda}, \mathbf{x}_t^{(\ell)}, \mathbf{a}_t] := \left\|\left(\boldsymbol{\mu} - \mathbf{1} - \boldsymbol{\Theta}(\mathbf{a}_t \circ \log[\mathbf{x}_t^{(\ell)}])\right) \circ \mathbf{f}_1[\mathbf{x}_t^{(\ell)}]\right\|_2^2 + \left(\boldsymbol{\mu} - \mathbf{1} - \boldsymbol{\Theta}(\mathbf{a}_t \circ \log[\mathbf{x}_t^{(\ell)}])\right)^\top \mathbf{f}_2[\mathbf{x}_t^{(\ell)}] - \text{trace}\left(\boldsymbol{\Theta}(\mathbf{a}_t \circ \mathbf{F}[\mathbf{x}_t^{(\ell)}])\right)$$
with logarithmic weight function $m(u) = \log(u)$, yielding:
$$\mathbf{f}_1[\mathbf{x}_t^{(\ell)}] = [\log(x_{t,1}^{(\ell)}), \dots, \log(x_{t,d\ell}^{(\ell)})]^\top$$
$$\mathbf{f}_2[\mathbf{x}_t^{(\ell)}] = [2\log(x_{t,1}^{(\ell)})^2 + 4\log(x_{t,1}^{(\ell)}), \dots, 2\log(x_{t,d\ell}^{(\ell)})^2 + 4\log(x_{t,d\ell}^{(\ell)})]^\top$$
$$\mathbf{F}[\mathbf{x}_t^{(\ell)}] = \text{diag}\left(2\log(x_{t,1}^{(\ell)})^2, \dots, 2\log(x_{t,d\ell}^{(\ell)})^2\right)$$

#### Adjacency Matrix Specifications (`source-reported`)
1. **Binary Adjacency Matrix ($\mathbf{a}_t^{(1)}$):**
   $$a_{t,j}^{(1)} = \mathbf{1}_{\{x_{t,j} > \bar{x}_{t,j}^{(w)}\}}, \quad \bar{x}_{t,j}^{(w)} = \frac{1}{w}\sum_{s=t-w}^{t-1} x_{s,j}$$
2. **ECDF Weighted Adjacency Matrix ($\mathbf{a}_t^{(2)}$):**
   $$a_{t,j}^{(2)} = F_j(x_{t,j}) = \frac{1}{t-1}\sum_{s=1}^{t-1} \mathbf{1}_{\{x_{s,j} \le x_{t,j}\}}$$
3. **Joint Extremes Adjacency Matrix (JEAM, $\mathbf{a}_t^{(3)}$):**
   Identifies historical time points $\mathcal{C}_t$ where a proportion exceeding $\kappa$ of assets simultaneously exceed their empirical percentile threshold $p$:
   $$\mathcal{C}_t = \left\{s \in \{1, \dots, t-w-1\} : \frac{1}{d}\sum_{j=1}^d \mathbf{1}_{\{F_j(x_{s,j}) > p\}} > \kappa\right\}$$
   For each $c \in \mathcal{C}_t$, a characteristic pattern vector is computed over symmetric window $W_c = \{c - \lfloor w/2 \rfloor, \dots, c + \lfloor w/2 \rfloor\}$:
   $$\mathbf{p}_c = \frac{1}{\text{card}(W_c)}\sum_{s \in W_c} \mathbf{x}_s$$
   Cosine similarity between current vector $\mathbf{x}_t$ and historical pattern $\mathbf{p}_c$:
   $$\text{sim}(\mathbf{x}_t, \mathbf{p}_c) = \frac{\mathbf{x}_t^\top \mathbf{p}_c}{\|\mathbf{x}_t\|_2 \|\mathbf{p}_c\|_2}$$
   JEAM weights are formed as the convex combination:
   $$a_{t,j}^{(3)} = g \cdot \max\left(0, \max_{c \in \mathcal{C}_t} \text{sim}(\mathbf{x}_t, \mathbf{p}_c)\right) + (1-g) \cdot F_j(x_{t,j})$$
   Optimal baseline hyperparameters identified across both simulated and empirical data: $p = 0.75$, $w = 5$, $g = 0.5$, $\kappa = 0.7$ (`source-reported`).

### 2. Operational Trading Rule Translation (`research-proposed`)

*The cited primary paper develops the econometric estimation and verifies probabilistic log scores out-of-sample; it does not formulate an execution order model, position-sizing rule, or stop-loss trigger. The following operational trading framework represents a `research-proposed` translation:*

- **Observation Cadence:** Evaluated at the close of every 5-minute bar (e.g., 9:35, 9:40, ..., 15:55 US/Eastern) on a universe of liquid equities (`research-proposed`).
- **Real-Time Systemic Risk State Indicator ($S_t$):**
  $$S_t := \max_{c \in \mathcal{C}_t} \text{sim}(\mathbf{x}_t, \mathbf{p}_c) \in [0, 1]$$
  derived from the Lower Tail (Minima Run) model (`research-proposed`).
- **Tail-Risk Hedging Overlay Trigger (`research-proposed`):**
  - If $S_t > \theta_{\text{hedge}}$ (with trigger threshold $\theta_{\text{hedge}} = 0.65$, `research-proposed`), indicating that an emergent multi-asset loss co-movement matches historical systemic cascade patterns, immediately execute a short hedge via index futures (e.g., CME E-mini / Micro E-mini S&P 500 futures) sized to neutralize portfolio dollar beta:
    $$\Delta_{\text{hedge}} = -\beta_{\text{portfolio}} \cdot \text{NAV}$$
  - **De-Hedging Exit Trigger (`research-proposed`):** When $S_t$ drops below $0.30$ and remains below $0.30$ for 3 consecutive 5-minute blocks (15 minutes), unwind the short index hedge.
- **Cross-Sectional Alpha Allocation Gating (`research-proposed`):**
  - **Dispersion Regime ($S_t \le 0.30$):** Idiosyncratic tail risk dominates; deploy long-short equity mean-reversion / pairs-trading strategies at $1.0\times$ normal gross leverage (`research-proposed`).
  - **Fragile / Clustered Regime ($S_t > 0.65$):** Systemic factor contagion dominates; reduce all long-short pairs leverage to $0.0\times$ (halt new entries, exit active pairs at market) to avoid factor-driven divergence losses (`research-proposed`).
- **Position Sizing & Exposure Limits (`research-proposed`):**
  Maximum gross exposure capped at $1.0\times$ portfolio equity; individual stock position limits capped at $5\%$ of NAV. Stop-loss on hedge overlay triggered if cumulative intraday basis drag between individual basket and index hedge exceeds $1.0\%$ (`research-proposed`).

## Required data

- **Asset Universe:** High-frequency intraday constituents from three primary sectors of the S&P 100: Information Technology, Health Care, and Finance (`source-reported`).
- **Sampling Frequency:** 1-minute intraday bars aggregated into 5-minute non-overlapping blocks (`source-reported`).
- **Historical Horizon:** 2021 to 2024 (spanning 4 full calendar years across multiple market cycles) (`source-reported`).
- **Input Fields Required:** 1-minute Open, High, Low, Close prices and trading volume. Block minima (largest percentage loss) and block maxima (largest percentage gain) are extracted per 5-minute interval (`source-reported`).
- **Preprocessing & Transformations:**
  - Block maxima/minima extraction (Gumbel 1958) (`source-reported`).
  - Standardized Pareto transformation for Hüsler–Reiss modeling (`source-reported`).
  - Absolute values taken for both loss (minima) and gain (maxima) series (`source-reported`).
- **Estimation & Walk-Forward Protocol:**
  - Rolling window design: 3-month estimation window, advanced weekly (`source-reported`).
  - Evaluation window: Hold-out subsequent week (one-step-ahead probabilistic forecasts updated at each time step) (`source-reported`).
  - Autoregressive lag length $\ell \in \mathbb{N}$ selected dynamically via AIC in each rolling window (`source-reported`).

## Execution assumptions

- **Source Modeling Assumption:** The primary paper is an econometric forecasting and probabilistic evaluation study. **Transaction commissions, exchange fees, bid-ask spread crossing, market impact, borrow costs, and execution slippage are NOT modeled in the primary source** (`source-reported`).
- **Research-Proposed Execution Model:**
  - Execution Vehicle: Equity orders routed via aggressive limit orders pegged to the national best bid/offer (NBBO) or CME E-mini / Micro E-mini S&P 500 futures for hedging overlays (`research-proposed`).
  - Commissions & Exchange Fees: $0.005 per share (or ~0.5 bps) for equities; $0.50 per contract for Micro E-mini futures (`research-proposed`).
  - Slippage & Spread Drag: 1.5 to 2.5 bps per one-way equity transaction; 0.5 bps for index futures hedges (`research-proposed`).
  - Execution Latency: Signal computed at the end of the 5-minute block; execution completed within $< 500\text{ ms}$ at the open of the subsequent bar (`research-proposed`).
  - Capacity Estimate: S&P 100 mega-cap equities and CME index futures support estimated strategy capacity of $\$50\text{M} - \$150\text{M}$ before market impact degrades 5-minute execution fills (`research-proposed`).

## Evidence

### Source-reported

All quantitative performance figures, AIC scores, and out-of-sample log scores reported below trace directly to Jungbluth, Lederer, and Trimborn (`arXiv:2609.11575v1`, Tables 1, 2, 3, 4, 5, 6):

#### 1. Out-of-Sample Empirical Forecast Evaluation Across S&P 100 Sectors (2021–2024)

Out-of-sample performance is measured by the average negative log-predictive score (lower is better):

$$\text{Log Score} = -\frac{1}{N_{\text{test}}} \sum_{t=1}^{N_{\text{test}}} \log h\left[\mathbf{x}_t^{(\ell)}; \hat{\boldsymbol{\mu}}, \hat{\boldsymbol{\Lambda}}, \mathbf{a}_t\right]$$

##### Table 2: Healthcare Sector Out-of-Sample Results
| Model Specification | Lower Tail (Losses) $\downarrow$ | Upper Tail (Gains) $\downarrow$ | Relative Improvement (Lower) | Relative Improvement (Upper) |
|:---|:---:|:---:|:---:|:---:|
| **Baseline: HR TimeDep** | 3.289 | 3.601 | Benchmark | Benchmark |
| **HR Binary: w3** | 3.012 | 3.345 | +8.42% | +7.11% |
| **HR Binary: w5** | 2.967 | 3.256 | +9.79% | +9.58% |
| **HR Binary: w10** | 3.078 | 3.412 | +6.42% | +5.25% |
| **HR JEAM: p70 w5** | 2.945 | 3.267 | +10.46% | +9.27% |
| **HR JEAM: p75 w3** | 2.923 | 3.212 | +11.13% | +10.80% |
| **HR JEAM: p75 w5 (Best)** | **2.878** | **3.189** | **+12.50%** | **+11.44%** |
| **HR JEAM: p75 w10** | 2.934 | 3.234 | +10.79% | +10.19% |
| **HR JEAM: p80 w5** | 2.901 | 3.223 | +11.80% | +10.50% |
| **HR JEAM: p90 w5** | 2.945 | 3.267 | +10.46% | +9.27% |

##### Table 3: Finance Sector Out-of-Sample Results
| Model Specification | Lower Tail (Losses) $\downarrow$ | Upper Tail (Gains) $\downarrow$ | Relative Improvement (Lower) | Relative Improvement (Upper) |
|:---|:---:|:---:|:---:|:---:|
| **Baseline: HR TimeDep** | 3.478 | 3.812 | Benchmark | Benchmark |
| **HR Binary: w3** | 3.212 | 3.556 | +7.65% | +6.72% |
| **HR Binary: w5** | 3.145 | 3.478 | +9.57% | +8.76% |
| **HR Binary: w10** | 3.289 | 3.645 | +5.43% | +4.38% |
| **HR JEAM: p70 w5** | 3.145 | 3.478 | +9.57% | +8.76% |
| **HR JEAM: p75 w3** | 3.056 | 3.423 | +12.13% | +10.20% |
| **HR JEAM: p75 w5 (Best)** | **3.023** | **3.367** | **+13.08%** | **+11.67%** |
| **HR JEAM: p75 w10** | 3.078 | 3.445 | +11.50% | +9.63% |
| **HR JEAM: p80 w5** | 3.034 | 3.423 | +12.77% | +10.20% |
| **HR JEAM: p90 w5** | 3.078 | 3.434 | +11.50% | +9.92% |

##### Table 4: Information Technology (IT) Sector Out-of-Sample Results
| Model Specification | Lower Tail (Losses) $\downarrow$ | Upper Tail (Gains) $\downarrow$ | Relative Improvement (Lower) | Relative Improvement (Upper) |
|:---|:---:|:---:|:---:|:---:|
| **Baseline: HR TimeDep** | 3.589 | 3.945 | Benchmark | Benchmark |
| **HR Binary: w3** | 3.267 | 3.601 | +8.97% | +8.72% |
| **HR Binary: w5** | 3.178 | 3.489 | +11.45% | +11.56% |
| **HR Binary: w10** | 3.334 | 3.667 | +7.11% | +7.05% |
| **HR JEAM: p70 w5** | 3.245 | 3.578 | +9.58% | +9.30% |
| **HR JEAM: p75 w3** | 3.145 | 3.389 | +12.37% | +14.09% |
| **HR JEAM: p75 w5 (Best)** | **3.101** | **3.356** | **+13.60%** | **+14.93%** |
| **HR JEAM: p75 w10** | 3.167 | 3.478 | +11.76% | +11.84% |
| **HR JEAM: p80 w5** | 3.112 | 3.445 | +13.29% | +12.67% |
| **HR JEAM: p90 w5** | 3.167 | 3.467 | +11.76% | +12.12% |

#### 2. Simulation Study Across 4,800 Heavy-Tailed Parameter Configurations (Table 1, $T=750$)
Simulation of $\alpha$-stable financial returns ($\alpha \in \{1.5, 1.7, 1.9, 2.0\}$), evaluating AIC across dimensions $d \in \{5, 10, 20, 30\}$ (lower AIC = superior fit):
- For $d=10, \alpha=1.5$ (heavy tails characteristic of high-frequency returns):
  - Baseline HR TimeDep AIC: **-186,123**
  - HR Binary (w3) AIC: **-192,212**
  - HR JEAM ($g=0$, w5) AIC: **-193,810**
  - HR JEAM ($g=0.5, p=0.75, w=5$) AIC: **-211,378** (approximately **15% AIC improvement** over baseline)
- Key Finding: Across all 4,800 configurations and sample lengths ($T \in \{250, 500, 750\}$), the JEAM specification with $g=0.5, p=0.75, \kappa=0.7$ universally dominated both unregularized baselines and pure binary adjacency matrices.

### Independently reproduced

- `Not independently reproduced.` The empirical findings and statistical log scores cited above reflect direct extraction from Jungbluth, Lederer, and Trimborn (`arXiv:2609.11575v1`, September 2026). No internal backtest or simulation has been conducted in `nautilus-quant-system`, PyBroker, or NautilusTrader.

### Negative evidence

1. **Failure of Unregularized Time-Dependent Hüsler–Reiss Models:**
   The unregularized baseline (HR TimeDep) produced the worst out-of-sample log scores across all three sectors and both tail directions without exception, trailing the best JEAM model by 0.41 to 0.59 log score units (`source-reported`). Fitting tail models directly on local block extrema without market-informed network filtering introduces severe estimation distortion.
2. **Degradation of Binary Adjacency Matrices in High Dimensions:**
   While binary adjacency matrices ($a_{t,j}^{(1)} \in \{0, 1\}$) improve upon the unregularized baseline in low dimensions ($d=5$), their performance degrades substantially as dimension grows ($d \ge 20$). Binary switches cannot capture the intensity, co-movement magnitude, or historical similarity of extreme events (`source-reported`).
3. **Over-Filtering Degradation at Extreme Quantiles ($p \ge 0.90$):**
   Restricting the joint extreme cluster threshold too aggressively (e.g., $p=0.90$) discards valuable historical co-movement data, resulting in sub-optimal AIC and log scores relative to $p=0.75$ (`source-reported`).
4. **Execution Drag in High-Frequency Rebalancing (`research-proposed`):**
   Because 5-minute block extrema in liquid equities have median percentage magnitudes of $0.15\% - 0.35\%$, any trading strategy executing high-frequency signals based on 5-minute updates is vulnerable to execution drag. If round-trip trading friction exceeds 4.0 bps, gross alpha from tail-dispersion trades is largely eroded (`research-proposed`).

## Falsification plan

To falsify the hypothesis that JEAM network regularization extracts genuine, tradeable tail-risk predictability from financial extremes, the following tests are defined:

1. **Placebo Shuffled-Time Matrix Test (`research-defined falsification threshold`):**
   - *Protocol:* Randomly permute the historical time order of the 5-minute block extrema $\mathbf{x}_t$ across dates while keeping contemporaneous cross-sectional correlations intact, destroying temporal lead-lag and clustering patterns. Re-estimate JEAM and compute out-of-sample log scores.
   - *Falsification Condition:* If the time-shuffled JEAM model achieves $> 80\%$ of the log score improvement observed in the unshuffled model (i.e. log score improvement over baseline $\ge 10.0\%$) (`research-defined falsification threshold`), reject the hypothesis that temporal extremal clustering drives the predictive advantage.
2. **Cross-Sector and Mid/Small-Cap Generalization Test (`research-defined falsification threshold`):**
   - *Protocol:* Apply the calibrated JEAM parameters ($p=0.75, w=5, g=0.5, \kappa=0.7$) to 50 non-S&P 100 Russell 2000 small/mid-cap equities over the same 2021–2024 horizon.
   - *Falsification Condition:* If out-of-sample log scores fail to improve over the unregularized baseline by at least $5.0\%$ in both lower and upper tails (`research-defined falsification threshold`), classify the framework as overfitted to mega-cap index liquidity regimes.
3. **Latency & Execution Drag Stress Test (`research-defined falsification threshold`):**
   - *Protocol:* Introduce synthetic execution delays of 1, 2, and 5 minutes between signal generation and hedge placement, and apply round-trip transaction costs varying from 2.0 to 8.0 bps.
   - *Falsification Condition:* If the simulated tail-hedging overlay fails to reduce portfolio maximum drawdown by at least $15\%$ net of 4.0 bps round-trip transaction costs (`research-defined falsification threshold`), classify the strategy as non-viable paper alpha.
4. **Classical GGM / Pearson Covariance Benchmark Ablation (`research-defined falsification threshold`):**
   - *Protocol:* Replace the time-dependent network Hüsler–Reiss precision matrix with an exponentially weighted moving average (EWMA) or graphical Lasso (GLASSO) Gaussian precision matrix.
   - *Falsification Condition:* If a standard Gaussian graphical model achieves equivalent or superior out-of-sample tail log scores (within $\pm 2.0\%$) (`research-defined falsification threshold`), reject the necessity of the Hüsler–Reiss extreme-value theoretical apparatus.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
  The primary study evaluates listed US mega-cap equities across three S&P 100 sectors during regular market hours (2021–2024). Porting the mechanism to cryptocurrency spot and perpetual futures markets is an adapted research hypothesis (`research-proposed`).
- **Cryptocurrency Microstructure Nuances:**
  1. *24/7 Continuous Trading & Sessionless Boundaries:* Cryptocurrency venues operate continuously without opening crosses, closing auctions, or weekend halts. Defining 5-minute blocks is natural, but clustering patterns $\mathcal{C}_t$ must account for distinct liquidity regimes (e.g., US market hours vs. Asian trading sessions) (`research-proposed`).
  2. *Extreme Tail Heaviness ($\alpha \approx 1.2 - 1.5$):* In the simulation study (Table 1), JEAM showed its largest performance advantage under heavy tails ($\alpha = 1.5$, improving AIC by 15%). Cryptocurrency returns exhibit notoriously fat tails and frequent multi-standard-deviation liquidation spikes, making them theoretically ideal candidates for JEAM regularization (`research-proposed`).
  3. *Perpetual Futures Liquidation Spirals & Funding Dislocations:* Unlike equities where down-moves are constrained by circuit breakers and margin calls over days, crypto perpetuals undergo sub-minute cascade liquidations. A crypto JEAM implementation must incorporate open interest changes and funding rate deviations into the cluster identification set $\mathcal{C}_t$ (`research-proposed`).
  4. *Cross-Venue Fragmentation:* Liquidity is fragmented across Binance, OKX, Bybit, and Hyperliquid. Input vectors $\mathbf{x}_t$ must be synthesized from composite volume-weighted median prices across venues to prevent single-exchange bad prints from triggering false joint extreme clusters (`research-proposed`).
- **Portability Failure Risk:** Moderate to High. Liquidation cascades in crypto frequently lead to exchange API rate-limiting or matching engine delays precisely during extreme events, impairing real-time hedge execution.

## Limitations

1. **Absence of Trading Execution Layer:** The primary source is an econometric and probabilistic modeling paper that evaluates AIC and log scores; it does not simulate actual trading PnL, slippage, order routing, or borrow costs (`source-reported`).
2. **Computational Overhead of Rolling Score Matching:** Minimizing the score-matching objective $o[\boldsymbol{\mu}, \boldsymbol{\Lambda}, \mathbf{x}_t^{(\ell)}, \mathbf{a}_t]$ for large panels ($d > 50$) with multi-step lag lengths requires solving non-trivial convex optimization problems at each rolling window update (`source-reported`).
3. **Horizon Limitation:** Tested on a 4-year panel (2021–2024); long-term performance across prolonged multi-year deflationary bear markets or structural liquidity crises (such as 2008) is not empirically demonstrated (`source-reported`).
4. **Heuristic Cosine Similarity Metric:** The use of cosine similarity for multi-asset extreme pattern comparison treats all asset deviations symmetrically, ignoring differences in asset volatility scaling or market capitalization weights (`research-proposed`).
5. **Data Gap for Low-Liquidity Assets:** In illiquid tokens or small-cap stocks, 5-minute blocks frequently contain zero volume or unchanged prices, violating continuous Pareto marginal distribution assumptions (`research-proposed`).

## Implementation status

- `not-implemented`.
- No implementation has been created in `nautilus-quant-system`, PyBroker, or NautilusTrader.
- No historical backtest campaign, paper-trading instance, testnet experiment, or live-trading deployment has been authorized or conducted.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- This record serves strictly as a structured research capture of third-party empirical findings and mathematical methodology. Inclusion in this repository does not constitute validation, commercial adoption, or authorization for live capital allocation.

## Related Wiki records

- `[[quant/crypto-dynamic-conditional-tail-dependence-husler-reiss-extremal-graph-2026-09-01]]` — Dynamic Hüsler–Reiss extremal graphical models applied to daily cryptocurrency returns.
- `[[quant/extreme-value-alpha-disclosure-network-rewiring-structural-tails-2026-09-04]]` — Extreme value alpha disclosure network rewiring and structural tail risk.
- `[[quant/expected-shortfall-factor-model-common-tail-loss-severity-2026-09-11]]` — Expected Shortfall factor models and common tail loss pricing.
- `[[quant/entropic-factor-model-robust-portfolio-replication-circuit-breaker-2026-09-04]]` — Entropic factor model with circuit-breaker tail regularization.
- `[[quant/duration-aware-bocpd-lognormal-order-flow-regime-2026-09-11]]` — Duration-aware Bayesian online changepoint detection for high-frequency microstructure regimes.

## Sources

1. **Primary Research Paper:**
   Ayla Jungbluth, Johannes Lederer, and Simon Trimborn, *"Market-Informed Networks for Modeling and Forecast Evaluation of Financial Extremes"*, arXiv preprint `arXiv:2609.11575v1 [stat.ME, q-fin.ST]`, submitted September 10, 2026, announced September 11, 2026.
   - Stable arXiv URL: `https://arxiv.org/abs/2609.11575`
   - Canonical HTML: `https://arxiv.org/html/2609.11575v1`
   - Canonical PDF: `https://arxiv.org/pdf/2609.11575v1`
   - Canonical DOI: [10.48550/arXiv.2609.11575](https://doi.org/10.48550/arXiv.2609.11575)
   - License: CC BY 4.0
2. **Methodological Foundations Cited in Paper:**
   - J. Hüsler and R.-D. Reiss (1989), "Maxima of normal random vectors: between independence and complete dependence", *Statistics & Probability Letters*, 7(4):283–286.
   - A. Hyvärinen (2005), "Estimation of non-normalized statistical models by score matching", *Journal of Machine Learning Research*, 6:695–709.
   - S. Engelke and A. S. Hitz (2020), "Graphical models for extremes", *Journal of the Royal Statistical Society: Series B*, 82(4):871–932.
   - J. Lederer and M. Oesting (2024), "Extremes in high dimensions: Methods and scalable algorithms", *arXiv:2303.04258*.
   - F. Longin and B. Solnik (2001), "Extreme correlation of international equity markets", *Journal of Finance*, 56(2):649–676.
