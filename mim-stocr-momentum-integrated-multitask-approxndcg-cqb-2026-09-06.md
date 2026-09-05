---
schema: strategy-research-record-v1
title: "MiM-StocR: Momentum-Integrated Multi-Task Stock Recommendation with Adaptive-k ApproxNDCG Ranking and Converge-Based Quad-Balancing (Wang et al. 2025/2026)"
created: 2026-09-06
updated: 2026-09-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - multi-task-learning
  - stock-recommendation
  - momentum-line
  - approxndcg
  - listwise-ranking
  - converge-based-quad-balancing
  - cross-sectional-equity
  - qlib
status: research-only
confidence: medium
source_as_of: 2026-01-24
sources:
  - "Hao Wang, Jingshu Peng, Yanyan Shen, Xujia Li, Quanqing Xu, Chuanhui Yang, and Lei Chen. 'Momentum-integrated Multi-task Stock Recommendation with Converge-based Optimization'. arXiv preprint: arXiv:2509.10461v2 [q-fin.ST, cs.LG], revised January 24, 2026. URL: https://arxiv.org/abs/2509.10461."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MiM-StocR: Momentum-Integrated Multi-Task Stock Recommendation with Adaptive-k ApproxNDCG Ranking and Converge-Based Quad-Balancing

## Provenance

- **Primary Source Authors:** Hao Wang (1), Jingshu Peng (2), Yanyan Shen (3), Xujia Li (1, 2), Quanqing Xu (4), Chuanhui Yang (4), and Lei Chen (1, 2).
  - (1) Hong Kong University of Science and Technology (Guangzhou), China.
  - (2) Hong Kong University of Science and Technology, Hong Kong, China.
  - (3) Shanghai Jiao Tong University, China.
  - (4) OceanBase, Ant Group, China.
- **Paper Title:** *"Momentum-integrated Multi-task Stock Recommendation with Converge-based Optimization"*
- **Preprint Identifier:** arXiv preprint `arXiv:2509.10461v2 [q-fin.ST, cs.LG]`.
- **First Submitted:** August 5, 2025 (`2025-08-05T09:04:38Z`).
- **Last Revised:** January 24, 2026 (`2026-01-24T03:16:13Z`).
- **Canonical arXiv URL:** [https://arxiv.org/abs/2509.10461](https://arxiv.org/abs/2509.10461)
- **Primary Source Verification:** The complete text of `arXiv:2509.10461v2` (10 pages) was retrieved and audited directly via PDF text extraction. All mathematical definitions (Equations 1–21), neural architectures (LSTM, GATs, HIST), loss objectives (MSE, Adaptive-$k$ ApproxNDCG), optimization mechanics (CQB with dynamic forgetting rate $\beta_n$ and dynamic $L_2$ weight decay), benchmark datasets (SEE50, CSI 100, CSI 300), and empirical tables (Tables 1–4, Figures 2–7) were verified against primary text.
- **Provenance Gaps & Code Availability:** The paper includes a footnote referencing an anonymous code repository (`https://anonymous.4open.science/r/MiM-StocR-E6BA`). As of September 2026 audit, the 4open hosting page returns `{"error":"repository_expired"}`. Consequently, reproduction relies on the explicit equations and architecture specifications published in the arXiv paper rather than external repository scripts.
- **Repository Deduplication Audit:** A search across `alpha-strategy-research` confirmed zero pre-existing records referencing `arXiv:2509.10461`, `MiM-StocR`, `ApproxNDCG`, `Quad-Balancing`, or the author cohort. Adjacent records in the repository study multi-task learning for commodity/futures momentum (`spatio-temporal-momentum-multitask-shrinkage-turnover-regularization-2026-09-06.md`), multi-alpha listwise ensembling (`maple-multi-alpha-position-aware-listwise-ensembling-2026-09-04.md`), discrete vector-quantized latent factor stock ranking (`prism-vq-vector-quantized-discrete-latent-factor-stock-ranking-2026-09-04.md`), or institutional price-volume correlation momentum (`quantaalpha-institutional-price-volume-correlation-intraday-momentum-2026-09-05.md`). None investigate multi-task supervision joining continuous return forecasting with 5-class discrete momentum-line trajectory classification, Adaptive-$k$ ApproxNDCG with cluster-aware boundary preservation, and relative convergence ratio ($V_n = \Delta L_{\text{valid}} / \Delta L_{\text{train}}$) dynamic gradient forgetting.

## Economic mechanism

### Source-reported

In quantitative equity markets, deep learning models for stock recommendation face two fundamental structural challenges:
1. **Label Noise in Directional Classification:** Binary rise-or-fall labels ($y \in \{0, 1\}$) are notoriously noisy and volatile over short horizons. Idiosyncratic microstructure noise often creates pseudo-random fluctuations around zero, obscuring underlying asset trajectories and leading to unstable neural representations.
2. **Task Imbalance and Asynchronous Overfitting in Multi-Task Learning:** Standard multi-task learning (MTL) combines continuous return regression with directional classification. However, different objective functions converge at different speeds and suffer from severe scale disparity in gradient magnitudes. Under non-stationary financial distributions, task-specific losses frequently diverge: test/validation losses begin increasing while training losses continue descending (manifesting severe overfitting) after relatively few epochs.

To resolve these issues, Wang et al. propose **MiM-StocR** based on three integrated mechanisms:
- **Structured Trend Classification via Momentum Lines:** Instead of predicting noisy instantaneous sign flips, the model tracks multi-point momentum trajectories discretized into five economic regimes: *Bounce* (inflection from negative to positive), *Positive* (sustained positive drift), *Volatile* (oscillation around zero), *Negative* (sustained downward drift), and *Sink* (inflection from positive to negative). This captures short-term trend persistence rooted in classical momentum theory (Jegadeesh & Titman 1993, Asness et al. 2014) while filtering high-frequency microstructure jitter.
- **Listwise Ranking Optimization with Boundary Preservation:** Cross-entropy and pairwise classification fail to emphasize top-tier cross-sectional portfolio candidates. MiM-StocR introduces *Adaptive-$k$ ApproxNDCG*, replacing discrete non-differentiable rank indicators with a smooth sigmoid function and adaptively expanding the truncation cutoff $k$ to encompass all stocks sharing the same discrete momentum tier ($k \ge \tau$, where $\tau = 20\%$ of the asset universe). This ensures consistent ranking supervision without arbitrary truncation splits among economically tied assets.
- **Dynamic Gradient De-weighting via Relative Convergence Dynamics:** Standard optimizers (such as Adam or fixed-weight MTL algorithms like DB-MTL and CAGrad) cannot detect when a specific task starts overfitting. Wang et al. introduce *Converge-based Quad-Balancing (CQB)*, which monitors the ratio of validation loss change to training loss change ($V_n = \Delta L_{\text{valid}} / \Delta L_{\text{train}}$). When overfitting begins ($V_n < 0$), the optimizer dynamically raises the exponential moving average (EMA) forgetting rate $\beta_n$, giving greater weight to pre-overfitting historical gradients, and simultaneously scales up $L_2$ weight decay, effectively damping noisy and overfitted parameter updates.

### Research interpretation

From a quantitative finance and alpha generation perspective, MiM-StocR functions as a **regularized cross-sectional ranker**:
- **Economic Source of Alpha:** The alpha originates from capitalizing on short-term trend continuation and inflection points across equity cross-sections. By distinguishing pure noise oscillations from genuine trajectory shifts (*Bounce* vs. *Sink*), the model isolates stocks experiencing institutional flow accumulation.
- **Mitigating the Optimizer Curse in Machine Learning Alpha:** In quantitative finance, complex neural networks frequently achieve high in-sample regression fit that collapses out-of-sample due to non-stationarity and low signal-to-noise ratio. CQB introduces an automated, closed-loop feedback mechanism between validation divergence and parameter updates. When a network starts memorizing training noise, CQB deterministically throttles current gradient influence and forces gradient alignment between tasks.
- **Listwise Preference Alignment:** Mean Squared Error (MSE) penalizes errors uniformly across all assets in the universe, expending model capacity on predicting whether median/bottom assets move by $\pm 0.1\%$. However, an active long-short or long-only strategy only allocates capital to the extreme deciles or quintiles. Combining MSE with ApproxNDCG explicitly concentrates model expressiveness on the ordinal ordering of the top percentiles.
- **Methodological Boundaries:** The model was evaluated on Chinese A-shares (SEE50, CSI 100, CSI 300) within the Microsoft Qlib framework. While empirical IC and cumulative returns demonstrate robustness across equity indices, the strategy relies on daily cross-sectional rebalancing of top-50 constituents. In real-world deployment, transaction costs, execution timing, and turnover could significantly erode reported gross alpha if unconstrained.

## Signal

### 1. Prediction Target and Continuous Return Formulation (`source-reported`)

Let $\text{price}_i^t$ denote the closing price of stock $i$ on trading day $t$ (`source-reported`).
The continuous prediction target is the one-day return ratio:
$$y_i^t = \frac{\text{price}_i^{t+1} - \text{price}_i^t}{\text{price}_i^t} \quad \text{(Eq. 1, source-reported)}$$

The primary regression task minimizes Mean Squared Error (MSE) between predicted scores $\hat{y}_i^t$ and realized returns $y_i^t$:
$$\mathcal{L}_r = \frac{1}{N} \sum_{i=1}^N (\hat{y}_i^t - y_i^t)^2 \quad \text{(source-reported)}$$

### 2. Momentum Line Trajectory Construction (`source-reported`)

The short-term price momentum with gap length $l$ at day $T$ is defined as:
$$m_T = \text{price}_T - \text{price}_{T-l} \quad \text{(Eq. 2, source-reported)}$$

To capture trajectory shape rather than a single scalar, a momentum line is formed over a sequence of $s$ consecutive momentum evaluations:
$$\mathcal{M}_T = \{ m_{T-s}, m_{T-s+1}, \dots, m_T \} \quad \text{(source-reported)}$$

Based on hyperparameter sensitivity analysis (Section 5.4, Figure 6), the default parameters are set to:
- Gap length: $l = 4$ trading days (`source-reported`).
- Line length: $s = 6$ trading days (`source-reported`).

Each momentum line $\mathcal{M}_T$ is mapped into one of five discrete trajectory classes $C \in \{1, 2, 3, 4, 5\}$ (`source-reported`):
1. **Bounce ($C=5$):** The line changes direction from negative to positive ($m_{T-k} < 0 \to m_T > 0$) (`source-reported`).
2. **Positive ($C=4$):** The line stays strictly positive ($m_t > 0, \forall t \in [T-s, T]$) (`source-reported`).
3. **Volatile ($C=3$):** The line oscillates around zero without sustained direction (`source-reported`).
4. **Negative ($C=2$):** The line stays strictly negative ($m_t < 0, \forall t \in [T-s, T]$) (`source-reported`).
5. **Sink ($C=1$):** The line changes direction from positive to negative ($m_{T-k} > 0 \to m_T < 0$) (`source-reported`).

### 3. Adaptive-$k$ ApproxNDCG Ranking Loss (`source-reported`)

The Normalized Discounted Cumulative Gain for ranking $\pi_{f, w}$ induced by scoring function $f$ with relevance weights $w$ is defined as:
$$\text{NDCG}(\pi_{f, w}) = \frac{\text{DCG}(\pi_{f, w})}{\text{DCG}(\pi^*_{f, w})} \quad \text{(Eq. 3, source-reported)}$$

where the Discounted Cumulative Gain (DCG) is:
$$\text{DCG}(\pi_{f, w}) = \sum_{i=1}^n \frac{2^{w_i} - 1}{\log_2(1 + \pi(i))} \quad \text{(Eq. 4, source-reported)}$$

with rank position:
$$\pi(i) \triangleq 1 + \sum_{j \neq i} \mathbb{I}_{f(i) < f(j)} \quad \text{(Eq. 5, source-reported)}$$

To enable gradient descent through discrete rank permutation, the step indicator $\mathbb{I}_{f(i) < f(j)}$ is relaxed to a smooth sigmoid approximation:
$$\mathbb{I}_{f(i) < f(j)} \approx \frac{1}{1 + e^{f(i) - f(j)}} \quad \text{(Eq. 6, source-reported)}$$

To prevent truncation bias where stocks within the same discrete momentum tier are arbitrarily split by a static cutoff, the truncation boundary $k$ is determined adaptively:
$$k = \sum_{j=4}^5 |G_j| \quad \text{subject to } k \ge \tau \quad \text{(Eq. 7, source-reported)}$$
where $|G_j|$ denotes the number of stocks in momentum tier $j$ (starting from highest tiers *Bounce* and *Positive*), and $\tau$ is a minimum lower-bound threshold set to $20\%$ of the active stock pool (`source-reported`). If $|G_5| + |G_4| < \tau$, lower tiers are iteratively included until $k \ge \tau$ (`source-reported`).

The listwise ranking loss is defined in exponential form:
$$\mathcal{L}_{\text{ndcg}} = e^{-\text{ApproxNDCG}(\pi_{w_{\text{pred}}}, w, k)} \quad \text{(Eq. 8, source-reported)}$$

The joint classification-ranking loss balances standard cross-entropy with listwise NDCG:
$$\mathcal{L}_c = \lambda_{\text{ce}} \mathcal{L}_{\text{ce}} + (1 - \lambda_{\text{ce}}) \mathcal{L}_{\text{ndcg}} \quad \text{(Eq. 9, source-reported)}$$
with trade-off parameter $\lambda_{\text{ce}} = 0.5$ (`source-reported`).

### 4. Converge-based Quad-Balancing (CQB) Optimization (`source-reported`)

CQB coordinates task gradients through four sequential balancing operations:
1. **Task-Specific Gradient EMA Smoothing:**
   $$\hat{g}_{r, \ell} = \beta \hat{g}_{r, \ell-1} + (1 - \beta) g_{r, \ell} \quad \text{(Eq. 10, source-reported)}$$
   $$\hat{g}_{c, \ell} = \beta \hat{g}_{c, \ell-1} + (1 - \beta) g_{c, \ell} \quad \text{(source-reported)}$$
   where $g_{r, \ell}$ and $g_{c, \ell}$ are raw gradients for regression and classification at iteration $\ell$, and $\beta$ is the forgetting rate (initialized to $\beta = 0.5$) (`source-reported`).
2. **$L_2$ Gradient Magnitude Normalization and Rescaling:**
   Task gradients are normalized to unit directional vectors:
   $$u_{r, \ell} = \frac{\hat{g}_{r, \ell}}{\|\hat{g}_{r, \ell}\|_2}, \quad u_{c, \ell} = \frac{\hat{g}_{c, \ell}}{\|\hat{g}_{c, \ell}\|_2} \quad \text{(Eq. 11, source-reported)}$$
   and recombined with magnitude anchored to the dominant task:
   $$\tilde{g}_\ell = \alpha_\ell (u_{r, \ell} + u_{c, \ell}), \quad \alpha_\ell = \max(\|\hat{g}_{r, \ell}\|_2, \|\hat{g}_{c, \ell}\|_2) \quad \text{(Eq. 12, source-reported)}$$
3. **Adaptive Forgetting Rate Control:**
   Overfitting dynamics are monitored via the relative convergence ratio:
   $$V_n = \frac{\Delta L_{\text{valid}}}{\Delta L_{\text{train}}} \quad \text{(Eq. 13, source-reported)}$$
   where smoothed loss change $\Delta L$ over window $b = 6$ epochs is:
   $$\Delta L = L_{n-1} - \text{mean}([L_{n-2b}, \dots, L_{n-b-1}]) \quad \text{(Eq. 14, source-reported)}$$
   For the initial 12 epochs ($n \le 12$), $V_n$ is fixed to $1.0$ (`source-reported`).
   For epoch $n > 12$, the dynamic forgetting rate is updated monotonically:
   $$\beta_n = \beta^{\sigma(V_n)} = \exp(\sigma(V_n) \ln \beta) \quad \text{(Eq. 15–16, source-reported)}$$
   where $\sigma(V_n) = \frac{1}{1 + e^{-V_n}}$. When overfitting occurs ($\Delta L_{\text{train}} < 0, \Delta L_{\text{valid}} \ge 0 \implies V_n < 0$), $\sigma(V_n) < 0.5$, causing $\beta_n$ to increase toward 1.0, which mathematically attenuates the weight of new overfitted gradients (proven in Eq. 17–20, `source-reported`).
4. **Adaptive $L_2$ Weight Decay Regularization:**
   $$\text{decay}_n = \text{decay}_0 \cdot \sigma(-\text{mean}(V_{n-1})) \quad \text{(Eq. 21, source-reported)}$$
   where initial weight decay $\text{decay}_0 = 10^{-3}$ (`source-reported`). As validation loss deteriorates ($V_{n-1} < 0$), $\sigma(-\text{mean}(V_{n-1})) > 0.5$, raising weight decay to penalize excessive parameter magnitudes (`source-reported`).

### 5. Operational Portfolio Construction & Execution (`research-proposed` vs. `source-reported`)

- **Universe Selection:** Evaluated on SEE50 (Shanghai 50), CSI 100, and CSI 300 (`source-reported`).
- **Stock Ranking:** At the close of trading day $t$, the trained model predicts return score $\hat{y}_i^t$ for all eligible universe constituents (`source-reported`).
- **Portfolio Selection:** Top 50 ranked stocks are selected for daily long positioning (`source-reported`, Qlib default Top50 strategy).
- **Position Sizing:** Equal-weighted across the Top 50 selected stocks ($w_i = 1/50 = 2.0\%$ per position) (`research-proposed`, standard Qlib default implementation).
- **Execution Timing:** Signals formed at close of day $t$; orders executed at next-day open ($t+1$ Open) or next-day close ($t+1$ Close) and held for 1 trading session (`research-proposed`, standard Qlib daily simulation; paper text notes "buys the top-ranked stocks daily and sells them on the next trading day").
- **Short Positions:** Long-only portfolio (`source-reported`, Qlib Top50 benchmark). Short sleeve is omitted in primary source backtest due to China A-share short-selling constraints (`research interpretation`).

## Required data

### 1. Data Schema & Feature Engineering (`source-reported`)

- **Data Package:** Microsoft Qlib Alpha360 dataset (`source-reported`).
- **Lookback Window:** 60 consecutive trading days of historical market data per stock (`source-reported`).
- **Features per Day:** 6 normalized daily fields: Open, High, Low, Close, Volume, VWAP (`source-reported`).
- **Total Feature Dimension:** $60 \times 6 = 360$ continuous numerical features per stock per date (`source-reported`).
- **Preprocessing:** Cross-sectional or temporal normalization standard in Qlib Alpha360 pipeline (`source-reported`).
- **Labels:** Realized close-to-close one-day return ratio $y_i^t$ (Eq. 1) and 5-class momentum line category $C_i^t$ (Eq. 2) (`source-reported`).

### 2. Time-Series Partitioning (`source-reported`)

- **Training Period:** 2007-01-01 through 2014-12-31 (8 calendar years) (`source-reported`).
- **Validation Period:** 2015-01-01 through 2016-12-31 (2 calendar years) (`source-reported`).
- **Test / Backtest Period:** 2017-01-01 through 2020-12-31 (4 calendar years) (`source-reported`).
- **Leakage Controls:** Strict chronological partitioning; no overlapping windows across train/validation/test splits (`source-reported`).

### 3. Market Universes (`source-reported`)

- **SEE 50 (SSE 50):** 50 largest, most liquid mega-cap stocks listed on the Shanghai Stock Exchange (`source-reported`).
- **CSI 100:** 100 largest capitalization stocks across Shanghai and Shenzhen exchanges (`source-reported`).
- **CSI 300:** 300 largest and most liquid A-share equities across Shanghai and Shenzhen exchanges (`source-reported`).

## Execution assumptions

- **Execution Venue:** Shanghai and Shenzhen Stock Exchanges (China A-Shares) (`source-reported`).
- **Rebalance Frequency:** Daily (`source-reported`).
- **Holding Horizon:** 1 trading day (positions opened daily, held 1 session, then rebalanced or exited) (`source-reported`).
- **Transaction Costs & Fees:** The primary source paper does not explicitly report fee, slippage, or stamp duty assumptions in the main text; it refers to "Qlib's default Top50 strategy" (`provenance gap, source-reported`).
  - *Research-Proposed Operational Baseline:* Standard A-share quantitative execution model requires modeling:
    - Brokerage commission: 2 to 3 bps (maker/taker) (`research-proposed`).
    - Transfer fees and regulatory charges: ~1 bp (`research-proposed`).
    - Stamp tax (China A-share sell-side): 5 to 10 bps (statutory rate historically 10 bps, reduced to 5 bps in Aug 2023) (`research-proposed`).
    - Execution slippage: 5 to 10 bps per one-way trade for CSI 300 large caps (`research-proposed`).
    - Total round-trip drag estimate: ~15 to 25 bps (`research-proposed`).
- **Order Type:** Market-on-open (MOO) or Time-Weighted Average Price (TWAP) execution across the opening window (`research-proposed`).
- **Short Selling / Borrow:** Long-only execution (`source-reported`); China A-share margin/borrow mechanisms are restricted for general quantitative funds (`research interpretation`).
- **Capital Capacity:** CSI 300 large caps offer substantial daily turnover (tens of billions RMB daily market volume), accommodating fund capacities of $10M–$50M USD without severe market impact at daily rebalancing frequency (`research-proposed`).

## Evidence

### Source-reported

All figures below are directly transcribed from Wang et al. (arXiv:2509.10461v2), Tables 1–4, Section 5.1–5.4, and Figure 4. Every experiment was repeated three times; mean and standard deviation ($\times 10^{-3}$) are reported:

#### 1. Information Coefficient (IC) and RankIC Performance (Table 1, `source-reported`)

| Backbone Architecture | Method | SEE 50 IC | SEE 50 RankIC | CSI 100 IC | CSI 100 RankIC | CSI 300 IC | CSI 300 RankIC |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **LSTM** | STL (Single-Task) | 0.0272 (0.6) | 0.0276 (1.3) | 0.0493 (2.9) | 0.0438 (2.6) | 0.0620 (2.0) | 0.0586 (1.7) |
| | EW (Equal Weight) | 0.0270 (0.6) | 0.0271 (1.1) | 0.0490 (1.9) | 0.0431 (2.8) | 0.0571 (1.2) | 0.0538 (1.5) |
| | DB-MTL (Lin et al. 2023) | 0.0272 (1.7) | 0.0279 (0.8) | 0.0470 (3.4) | 0.0415 (3.0) | 0.0567 (3.0) | 0.0543 (2.9) |
| | CAGrad (Liu et al. 2021) | 0.0267 (2.0) | 0.0300 (3.1) | 0.0469 (1.4) | 0.0422 (0.5) | 0.0551 (0.9) | 0.0528 (1.0) |
| | **MiM-StocR (Ours)** | **0.0362 (3.1)** | **0.0358 (3.6)** | **0.0522 (1.6)** | **0.0467 (1.5)** | **0.0632 (0.9)** | **0.0604 (1.4)** |
| **GATs** | STL (Single-Task) | 0.0258 (3.4) | 0.0261 (1.3) | 0.0421 (6.3) | 0.0360 (5.7) | 0.0575 (1.5) | 0.0546 (1.5) |
| | EW (Equal Weight) | 0.0269 (3.8) | 0.0280 (4.9) | 0.0386 (6.8) | 0.0339 (5.4) | 0.0588 (2.6) | 0.0556 (2.4) |
| | DB-MTL (Lin et al. 2023) | 0.0242 (2.6) | 0.0219 (4.0) | 0.0394 (5.7) | 0.0358 (5.3) | 0.0589 (3.2) | 0.0566 (2.7) |
| | CAGrad (Liu et al. 2021) | 0.0223 (3.1) | 0.0182 (5.0) | 0.0423 (3.5) | 0.0378 (2.6) | 0.0608 (1.8) | 0.0588 (1.2) |
| | **MiM-StocR (Ours)** | **0.0278 (4.8)** | **0.0266 (4.4)** | **0.0472 (8.7)** | **0.0443 (6.9)** | **0.0622 (1.5)** | **0.0590 (0.8)** |
| **HIST** | STL (Single-Task) | 0.0288 (0.8) | 0.0300 (1.7) | 0.0552 (1.8) | 0.0503 (1.2) | 0.0672 (2.3) | 0.0630 (2.3) |
| | EW (Equal Weight) | 0.0286 (0.5) | 0.0297 (1.2) | 0.0571 (2.4) | 0.0512 (2.2) | 0.0631 (1.5) | 0.0601 (1.4) |
| | DB-MTL (Lin et al. 2023) | 0.0278 (3.8) | 0.0289 (1.9) | 0.0565 (1.4) | 0.0517 (1.9) | 0.0631 (1.8) | 0.0599 (1.9) |
| | CAGrad (Liu et al. 2021) | 0.0301 (2.4) | 0.0292 (0.6) | 0.0560 (1.3) | 0.0507 (1.4) | 0.0638 (3.4) | 0.0611 (2.7) |
| | **MiM-StocR (Ours)** | **0.0393 (2.3)** | **0.0387 (3.6)** | **0.0605 (1.1)** | **0.0544 (2.0)** | **0.0667 (1.1)** | **0.0633 (1.0)** |

#### 2. Momentum Line vs. Binary Rise-or-Fall Classification (Table 2, `source-reported`)

On the CSI 300 benchmark under identical backbone settings, replacing the discrete 5-class momentum line with a traditional binary rise-or-fall classification label causes substantial drop in predictive correlation:
- **LSTM:** Rise-or-Fall achieves IC = 0.0457 (4.5), RankIC = 0.0436 (4.5) vs. Momentum IC = **0.0632 (0.9)**, RankIC = **0.0604 (1.4)** (`source-reported`).
- **GATs:** Rise-or-Fall achieves IC = 0.0501 (3.4), RankIC = 0.0484 (3.9) vs. Momentum IC = **0.0622 (1.5)**, RankIC = **0.0590 (0.8)** (`source-reported`).
- **HIST:** Rise-or-Fall achieves IC = 0.0519 (2.6), RankIC = 0.0507 (2.2) vs. Momentum IC = **0.0667 (1.1)**, RankIC = **0.0633 (1.0)** (`source-reported`).

#### 3. Top-N Ranking Precision (Table 3, `source-reported`)

Precision@N measures the fraction of the top $N$ stocks predicted by the model whose next-day return is positive:
- **Cross-entropy:** P@10 = 53.58%, P@20 = 53.98%, P@30 = 53.99%, P@50 = 53.67% (`source-reported`).
- **Pair-wise:** P@10 = 54.07%, P@20 = 54.15%, P@30 = 54.15%, P@50 = 53.82% (`source-reported`).
- **w/o Adaptive-$k$:** P@10 = 54.04%, P@20 = 54.01%, P@30 = 53.93%, P@50 = 53.64% (`source-reported`).
- **MiM-StocR:** P@10 = **54.42%**, P@20 = **54.33%**, P@30 = **54.15%**, P@50 = **53.84%** (`source-reported`).

#### 4. Component Ablation on CSI 300 (Table 4, `source-reported`)

Using the HIST backbone:
- **Objective Function Variants (RQ3):**
  - Cross-entropy alone: IC = 0.0640 (3.0), RankIC = 0.0612 (3.0) (`source-reported`).
  - Pair-wise loss: IC = 0.0657 (1.7), RankIC = 0.0625 (2.2) (`source-reported`).
  - w/o Adaptive-$k$ (fixed $k=50$): IC = 0.0649 (0.2), RankIC = 0.0618 (0.5) (`source-reported`).
- **CQB Multi-Objective Optimizer Variants (RQ4):**
  - w/o $\beta$ dynamic balancing (uniform $\beta$): IC = 0.0656 (1.0), RankIC = 0.0619 (1.1) (`source-reported`).
  - w/o $L_2$ dynamic balancing (fixed weight decay): IC = 0.0665 (2.3), RankIC = 0.0625 (2.4) (`source-reported`).
  - **Full MiM-StocR:** IC = **0.0667 (1.1)**, RankIC = **0.0633 (1.0)** (`source-reported`).

#### 5. Trading Simulation Profitability (Section 5.2 & Figure 4, `source-reported`)

- Backtest simulated on CSI 300 from 2017 to 2020 using Qlib default Top50 strategy (`source-reported`).
- The combination of LSTM and MiM-StocR achieves cumulative profit that is **11.6% higher than the benchmark CSI 300 index** (`source-reported`).
- MiM-StocR consistently achieves top investment returns across all evaluated backbones (LSTM, GATs, HIST), outperforming both the underlying index and baseline multi-task optimizers (EW, DB-MTL, CAGrad) (`source-reported`).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Noise Sensitivity of Binary Rise-or-Fall:** The authors' direct ablation (Table 2) demonstrates that training with binary directional labels leads to severe performance degradation across all three backbones (reducing RankIC by 1.2% to 1.7% in absolute terms), confirming that naive rise-or-fall supervision introduces destructive label noise into deep representation layers (`source-reported`).
- **Overfitting Vulnerability in Conventional MTL:** Visual analysis of training dynamics (Figure 5) reveals that standard multi-task frameworks (DB-MTL and CAGrad) consistently begin severe validation overfitting after approximately 25 epochs (test losses begin increasing while training losses continue descending) (`source-reported`). Without CQB's dynamic forgetting rate and adaptive regularization, multi-task models fail to maintain out-of-sample generalization.
- **Turnover and Transaction Cost Sensitivity:** The paper does not report gross vs. net returns after realistic broker commissions, stamp tax, and slippage (`provenance gap, research interpretation`). In a daily rebalancing Top-50 strategy, an annual turnover of 500%–1500% with round-trip frictions of 15–25 bps could significantly degrade the 11.6% cumulative outperformance over a 4-year test window unless turnover regularization or position inertia is introduced (`research interpretation`).

## Falsification plan

To falsify or establish the operational boundaries of the MiM-StocR mechanism, the following six targeted empirical stress tests are declared:

1. **Transaction Cost & Turnover Attrition Test:**
   - *Test Procedure:* Backtest the Top-50 equal-weighted portfolio on CSI 300 (2017–2020) while varying round-trip transaction costs across $c \in [0, 5, 10, 15, 20, 25, 30]$ bps.
   - *Failure Rule (`research-defined falsification threshold`):* If net annualized excess return relative to CSI 300 falls below 0.0% at a realistic transaction cost threshold of $c = 15$ bps, the hypothesis that MiM-StocR produces actionable post-cost alpha on daily rebalancing is falsified.
2. **Strict Chronological Walk-Forward Rolling Evaluation:**
   - *Test Procedure:* Replace the static 2007–2014 train / 2015–2016 val / 2017–2020 test split with an annually anchored expanding-window walk-forward schedule (e.g., train on $T-8$ to $T-2$, validate on $T-1$, test on year $T$ for $T \in [2017, \dots, 2026]$).
   - *Failure Rule (`research-defined falsification threshold`):* If average out-of-sample RankIC over the expanding rolling windows drops below $0.030$ or exhibits negative RankIC in more than 35% of testing years, the stability of the CQB optimization mechanism across changing macroeconomic regimes is falsified.
3. **Randomized Momentum Label Placebo Test:**
   - *Test Procedure:* Randomly permute the momentum line trajectory labels $C_i^t \in \{1, \dots, 5\}$ cross-sectionally across stocks while keeping the continuous return target $y_i^t$ intact. Train the multi-task model under CQB.
   - *Failure Rule (`research-defined falsification threshold`):* If the randomized-label model achieves an out-of-sample RankIC within $0.005$ of the true MiM-StocR model (i.e., RankIC $\ge 0.058$), the hypothesis that the 5-class momentum line trajectory provides genuine economic signal (rather than acting as arbitrary gradient noise injection) is falsified.
4. **Adaptive-$k$ Truncation Bound Sensitivity:**
   - *Test Procedure:* Perturb the minimum truncation threshold $\tau \in [5\%, 10\%, 15\%, 20\%, 25\%, 30\%, 40\%]$ and compare performance against fixed-$k$ baselines ($k \in [20, 50, 100]$).
   - *Failure Rule (`research-defined falsification threshold`):* If varying $\tau$ within $[10\%, 30\%]$ causes RankIC degradation greater than $15\%$ relative to default $\tau = 20\%$, the ranking mechanism is hyperparameter-overfitted and lacks operational structural robustness.
5. **CQB Convergence Ratio Delay Audit:**
   - *Test Procedure:* Evaluate the model when the convergence window $b$ is perturbed across $b \in [2, 4, 6, 8, 12]$ and the initialization delay varies across $[6, 12, 18]$ epochs.
   - *Failure Rule (`research-defined falsification threshold`):* If the model's test loss divergence fails to be suppressed across $b \in [4, 8]$, or if RankIC drops below STL baseline ($0.0586$), the theoretical claim that CQB's dynamic forgetting rate $\beta_n$ stabilizes multi-task optimization is disconfirmed.
6. **Cross-Market Generalization (US Large-Cap S&P 500 / Russell 1000):**
   - *Test Procedure:* Port the identical MiM-StocR architecture with Alpha360 features to the S&P 500 or Russell 1000 universe without altering $l=4, s=6, \tau=20\%, \lambda_{\text{ce}}=0.5$.
   - *Failure Rule (`research-defined falsification threshold`):* If out-of-sample RankIC on US equities fails to exceed $0.025$, the claim that MiM-StocR represents a universal market-agnostic multi-task stock recommendation framework is rejected.

## Crypto portability

- **Portability Status:** `adapted / unproven` (`research interpretation`).
- **Porting Rationale:** The primary source paper tested MiM-StocR exclusively on Chinese A-share equity universes (SEE50, CSI 100, CSI 300) characterized by $T+1$ trading rules, daily price-limit bands ($\pm 10\%$), distinct institutional retail order flows, and no continuous 24/7 sessions. The cited paper does not demonstrate the mechanism in cryptocurrency markets.
- **Structural Adaptations for Digital Asset Markets:**
  1. **Timeframe & Horizon Calibration:** Traditional equity daily bars (closing prices) must be adapted to continuous crypto perpetual futures sessions. Using 24-hour UTC cutoffs or 4-hour / 8-hour intervals ($l = 4 \times 8\text{h} = 32\text{h}$, $s = 6 \times 8\text{h} = 48\text{h}$) is required to match crypto momentum cycles.
  2. **Universe Definition & Survivorship:** Crypto markets exhibit high token turnover, delistings, and illiquid tails. The universe must be filtered dynamically to the Top 50 or Top 100 perpetual contracts by 30-day average daily volume (ADV $\ge \$10\text{M}$) on Binance/OKX/Bybit to avoid illiquid tokens where price manipulation distorts momentum lines.
  3. **Funding Rate & Carry Integration:** Crypto perpetual futures entail 8-hour funding payments. A cross-sectional long-only strategy holding high-momentum tokens during crowded speculative phases may incur massive negative funding fees. Funding rate yields must be incorporated as an additional input feature or cost penalty in portfolio optimization.
  4. **Long-Short Execution:** Unlike China A-shares where shorting is heavily restricted, crypto perpetual markets allow friction-free two-sided positioning. MiM-StocR can naturally be adapted to a market-neutral long-short quintile framework (Long Top 10%, Short Bottom 10%), mitigating Bitcoin beta exposure.
  5. **Extreme Volatility & Liquidation Whipsaws:** Crypto markets experience flash crashes and liquidation cascades where *Bounce* trajectories rapidly degenerate into catastrophic *Sink* cascades. Volatility scaling (ATR-based position sizing) and hard stop-loss thresholds (`research-proposed`) are essential.

## Limitations

- **Expired Code Repository (`provenance gap`):** The official anonymous code link (`https://anonymous.4open.science/r/MiM-StocR-E6BA`) is expired and inaccessible, preventing direct inspection of proprietary implementation nuances.
- **Omission of Explicit Transaction Cost Breakdown (`provenance gap`):** While the paper reports an 11.6% cumulative profit advantage over the CSI 300 index using Qlib's default Top50 strategy, it does not explicitly tabularize net performance curves under graded commission, stamp tax, and slippage assumptions.
- **Daily Rebalancing Turnover:** Top-50 daily portfolio reselection without turnover penalization or position inertia can induce high turnover, potentially transferring significant gross alpha to broker fees and exchange spreads.
- **Sample Period Ceiling (2020):** The reported empirical evaluation ends at December 31, 2020. Market performance during the subsequent 2021–2026 macro regime (rate hikes, sector rotations, regulatory interventions) is unverified in the primary paper.
- **Backbone Capacity Limits:** The authors report that backbones have fewer than 500M parameters and can be trained on a single RTX 3090 GPU in ~3 hours. While computationally efficient, scaling to full market cross-sections (e.g., all 5,000+ A-shares or thousands of crypto tokens) would require distributed graph scaling for GATs and HIST.

## Implementation status

`not-implemented`

- No implementation of MiM-StocR exists in this repository or the `nautilus-quant-system` production stack.
- This record represents a normalized research capture and theoretical audit.
- Implementation authorization requires formal evaluation through Loop A / Loop B (PyBroker experiment campaign and NautilusTrader backtest verification).

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`
- **Adoption Boundary Clarification:** The presence of this record does not constitute authorization for deployment, paper trading, testnet verification, or live capital allocation. Any future implementation or transition across the research-to-production boundary requires explicit review, complete codebase reconstruction, transaction-cost stress testing, and pipeline sign-off.

## Related Wiki records

- `[[quant/spatio-temporal-momentum-multitask-shrinkage-turnover-regularization-2026-09-06]]` — Multi-task learning architecture for time-series momentum with graphical shrinkage.
- `[[quant/maple-multi-alpha-position-aware-listwise-ensembling-2026-09-04]]` — Multi-alpha listwise learning-to-rank for cross-sectional stock portfolios.
- `[[quant/prism-vq-vector-quantized-discrete-latent-factor-stock-ranking-2026-09-04]]` — Discrete latent factor codebook for cross-sectional stock ranking.
- `[[quant/stn-tgat-nmi-soft-threshold-graph-attention-topk-ranking-2026-09-04]]` — Graph attention network with top-$k$ ranking optimization for equity alpha.
- `[[quant/quantaalpha-institutional-price-volume-correlation-intraday-momentum-2026-09-05]]` — Price-volume correlation intraday momentum factors on CSI 300.
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Methodological standards for leakage prevention and cross-validation in financial time series.

## Sources

- **Primary Paper:** Hao Wang, Jingshu Peng, Yanyan Shen, Xujia Li, Quanqing Xu, Chuanhui Yang, and Lei Chen. *"Momentum-integrated Multi-task Stock Recommendation with Converge-based Optimization"*. arXiv preprint: `arXiv:2509.10461v2 [q-fin.ST, cs.LG]`, submitted August 5, 2025, revised January 24, 2026. Available at: [https://arxiv.org/abs/2509.10461](https://arxiv.org/abs/2509.10461).
- **Primary Source Code Reference:** Anonymous GitHub / 4open repository cited in paper footnote 1: `https://anonymous.4open.science/r/MiM-StocR-E6BA` (repository link verified expired upon audit).
- **Underlying Benchmark & Factor References:**
  - Microsoft Qlib Quantitative Platform: [https://github.com/microsoft/qlib](https://github.com/microsoft/qlib)
  - Wentao Xu et al. *"HIST: A Graph-based Framework for Stock Trend Forecasting"*. IJCAI 2021.
  - Baijiong Lin et al. *"Dual-Balancing for Multi-Task Learning"*. arXiv:2305.15049, 2023.
  - Bo Liu et al. *"Conflict-Averse Gradient Descent for Multi-task Learning"*. NeurIPS 2021.
  - Tao Qin et al. *"A General Approximation Framework for Direct Optimization of Information Retrieval Measures"*. Information Retrieval 2010.
