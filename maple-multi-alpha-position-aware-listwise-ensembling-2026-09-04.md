---
schema: strategy-research-record-v1
title: "MAPLE: Multi-Alpha Position-Aware Listwise Ensembling for Diverse Cross-Sectional Stock Selection and Portfolio Construction"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional-equity
  - deep-learning
  - learning-to-rank
  - multi-alpha
  - ensemble
  - diversity-regularization
  - extreme-rank-loss
status: research-only
confidence: medium
source_as_of: 2026-07-27
sources:
  - "Den, Y.-C., Chen, K.-Y., Vincent, K., & Chang, T.-H. (2026). MAPLE: Efficient and Diverse Multi-Alpha Generation for Portfolio Construction. arXiv:2607.24131v1 [cs.LG, cs.CE]. https://arxiv.org/abs/2607.24131"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MAPLE: Multi-Alpha Position-Aware Listwise Ensembling for Diverse Cross-Sectional Stock Selection and Portfolio Construction

## Provenance

- **Primary Source:** Yu-Chen Den, Kuan-Yu Chen, Kendro Vincent, and Tien-Hao Chang, *"MAPLE: Efficient and Diverse Multi-Alpha Generation for Portfolio Construction"*, arXiv preprint `arXiv:2607.24131v1 [cs.LG, cs.CE]`, submitted July 27, 2026.
- **Canonical DOI:** [10.48550/arXiv.2607.24131](https://doi.org/10.48550/arXiv.2607.24131)
- **Stable URL:** [https://arxiv.org/abs/2607.24131](https://arxiv.org/abs/2607.24131)
- **Full Text (HTML):** [https://arxiv.org/html/2607.24131v1](https://arxiv.org/html/2607.24131v1)
- **Institutional Affiliations:** SinoPac Securities and National Chengchi University, Taiwan.
- **License:** CC BY-NC-ND 4.0.
- **Sample Universe & Period:**
  - CSI300 (China A-shares large-cap, 295 stocks)
  - CSI500 (China A-shares small/mid-cap, 514 stocks)
  - NI225 (Japan Nikkei 225, 209 stocks)
  - S&P 500 (United States large-cap, 525 stocks)
  - Training period: 2008-01-01 to 2019-12-31 (12 years)
  - Validation period: 2020-01-01 to 2020-12-31 (1 year)
  - Out-of-sample test period: 2021-01-01 to 2024-12-31 (4 years)

## Economic mechanism

### Source-reported

In classical quantitative portfolio management, combining multiple weakly correlated alpha signals is fundamental to improving risk-adjusted returns and mitigating exposure to regime shifts (citing Fama & French 2018; Goldstein & Yang 2015; Acharya et al. 2017; Tulchinsky 2019). However, recent deep learning approaches for cross-sectional stock ranking typically generate only a single predictive score per stock. To boost performance, prior studies have introduced increasingly complex architectures (e.g., Transformers with graph attention, hypergraphs, or diffusion-based Mixture-of-Experts), which yield diminishing returns at steep computational expense.

Prior attempts to achieve multi-alpha diversity have relied on multi-model ensembles (training independent networks with different seeds), explicit routing mechanisms, or multi-stage knowledge distillation. These approaches multiply computational training cost without explicitly controlling pairwise correlation between alpha signals.

MAPLE (Multi-Alpha Position-aware Listwise Ensembling) proposes to resolve this limitation within a single model and a single end-to-end training pass by combining:
1. A unified prediction head that pairs a capacity-scaled intra-stock MLP with a lightweight inter-stock multi-head attention module operating directly in prediction space (prediction-level residual aggregation);
2. A trainable position-aware listwise ranking loss (Extreme-Rank Weighted Spearman Loss) that concentrates learning on the extreme tails of the return distribution;
3. An explicit diversity regularizer that penalizes pairwise absolute rank correlation across alpha heads;
4. Dynamic capacity scaling across alpha heads to prevent representation bottlenecks as the number of alphas ($N_\alpha$) scales.

### Research interpretation

The core mechanism is a regularized multi-signal cross-sectional ranking ensemble that explicitly harvests diversification benefits across heterogeneous prediction heads within a shared feature representation:
- **Extreme-Rank Asymmetry:** In systematic long-only portfolio construction, ranking errors in the broad middle of the asset universe have negligible economic consequence because capital is deployed only into the top-$k$ deciles. Standard global listwise rank correlation (e.g., unweighted Spearman loss) penalizes misrankings uniformly across all $S$ stocks. When paired with a diversity penalty, an unweighted ranking loss forces alpha heads to differentiate across irrelevant center stocks, destroying top-$k$ selection precision.
- **Tail-Constrained Diversity Optimization:** By anchoring the listwise ranking objective to extreme ranks via a continuous sigmoidal distance weighting from the distribution median, diversity regularization is restricted to finding orthogonal signals *within the profitable tail*. This produces distinct non-overlapping subsets of winning stocks rather than arbitrary noise dispersion.
- **Orthogonal Gradient Flow via Prediction-Level Residuals:** Summing intra-stock and inter-stock outputs directly in prediction space ($\hat{\bm{Y}} = \hat{\bm{Y}}_{\text{intra}} + \hat{\bm{Y}}_{\text{inter}}$) rather than through standard hidden-layer Transformer residuals prevents the relational attention mechanism from monopolizing the shared representation, preserving balanced gradient flow and enabling natural signal decorrelation before any explicit regularizer is applied.

## Signal

### Feature Normalization & Inputs
For each stock $s \in \{1, \ldots, S\}$ on trading day $t$, an 8-dimensional feature vector is formed from:
- 5 standardized OHLCV series: $z_{\text{close}}^t = \frac{x_{\text{close}}^t - \bar{x}_{\text{close}}^{[t-19:t]}}{\sigma_{x_{\text{close}}}^{[t-19:t]}}$ (and analogously for open, high, low, volume over a rolling 20-day window).
- 3 moving-average deviation indicators: $z_{d_k}^t = \frac{\frac{1}{k}\sum_{i=0}^{k-1} x_{\text{close}}^{t-i}}{x_{\text{close}}^t} - 1$ for lookback windows $k \in \{5, 10, 20\}$.
- Temporal lookback: sequence length $T = 20$ daily bars.

### Network Architecture
1. **Intra-Stock Temporal Encoder ($t_\theta$):**
   - Default: 2-layer causal Transformer encoder (hidden dimension $D=64$, 8 attention heads, FFN dimension 256 with ReLU, dropout 0.1).
   - Generates hidden representation $\bm{H} \in \mathbb{R}^{S \times D}$ from the final time step.
   - Layer normalization applied across the hidden dimension: $\tilde{\bm{H}} = \mathrm{LayerNorm}(\bm{H}) \in \mathbb{R}^{S \times D}$.
2. **Multi-Alpha Generation Head ($g_\theta$):**
   - **Intra-Stock Path:** Two-layer MLP with ReLU:
     $$\hat{\bm{Y}}_{\text{intra}} = \mathrm{MLP}(\tilde{\bm{H}}) \in \mathbb{R}^{S \times N_\alpha}$$
     with hidden dimension scaled proportionally to $\lfloor D \cdot (N_\alpha / 8) \rfloor$.
   - **Inter-Stock Attention Path:** Multi-head cross-sectional attention across stocks with $h = N_\alpha$ heads:
     $$\bm{Q} = \tilde{\bm{H}}\bm{W}_Q, \quad \bm{K} = \tilde{\bm{H}}\bm{W}_K, \quad \bm{V} = \tilde{\bm{H}}\bm{W}_V$$
     where $\bm{W}_Q, \bm{W}_K \in \mathbb{R}^{D \times d_{\text{emb}}}$, $d_{\text{emb}} = \lfloor 2 \cdot D \cdot (N_\alpha / 8) \rfloor$, $d_k = d_{\text{emb}} / N_\alpha$, and $\bm{W}_V \in \mathbb{R}^{D \times N_\alpha}$.
     For each head $i \in \{1, \ldots, N_\alpha\}$:
     $$\bm{A}^{(i)} = \mathrm{softmax}\left(\frac{\bm{Q}^{(i)}{\bm{K}^{(i)}}^\top}{\sqrt{d_k}}\right)\bm{V}^{(i)} \in \mathbb{R}^{S \times 1}$$
     $$\hat{\bm{Y}}_{\text{inter}} = \mathrm{Concat}\left(\bm{A}^{(1)}, \ldots, \bm{A}^{(N_\alpha)}\right) \in \mathbb{R}^{S \times N_\alpha}$$
   - **Prediction-Level Residual Aggregation:**
     $$\hat{\bm{Y}} = \hat{\bm{Y}}_{\text{intra}} + \hat{\bm{Y}}_{\text{inter}} \in \mathbb{R}^{S \times N_\alpha}$$
     where each column $\hat{\bm{y}}_i \in \mathbb{R}^S$ ($i = 1, \ldots, N_\alpha$) represents the $i$-th alpha prediction across all $S$ stocks.

### Training Objective
- Target: forward $q=5$ day return $y_t = \frac{x_{\text{close}}^{t+q} - x_{\text{close}}^t}{x_{\text{close}}^t}$.
- Differentiable rank surrogate (Fang et al. 2019):
  $$\phi(\bm{x}) = \mathrm{sigmoid}\left(1.83 \cdot \frac{\bm{x} - \mathrm{mean}(\bm{x})}{2 \cdot \mathrm{std}(\bm{x}) + \epsilon}\right)$$
  normalized via demeaning and $\ell_2$-normalization: $\tilde{\phi}(\bm{x}) = \frac{\phi(\bm{x}) - \mathrm{mean}(\phi(\bm{x}))}{\|\phi(\bm{x}) - \mathrm{mean}(\phi(\bm{x}))\|_2 + \epsilon}$.
1. **Global Spearman Loss ($\mathscr{L}_{\text{spr}}$):**
   $$\mathscr{L}_{\text{spearman}} = -\frac{1}{N_\alpha} \sum_{i=1}^{N_\alpha} \rho\left(\phi(\hat{\bm{y}}_i),\, \phi(\bm{y})\right)$$
2. **Extreme-Rank Weighted Spearman Loss ($\mathscr{L}_{\text{ext}}$):**
   - Let $r_s \in \{0, \ldots, S-1\}$ be the true descending rank of stock $s$ in target $\bm{y}$ ($r_s=0$ for the top return stock).
   - Let $c = (S-1)/2$ be the center index. Distance $d_s = \max(0, c - r_s)$.
   - Each alpha $i$ has learnable sharpness $\xi^{(i)} > 0$ (initialized to 10.0) and margin scale $\gamma^{(i)} \in (0,1)$ (initialized to 0.8), defining transition margin $\delta^{(i)} = \gamma^{(i)} c$.
   - Position weight: $z_s = \mathrm{sigmoid}\left(\xi^{(i)} (d_s - \delta^{(i)})\right)$, $v_s^{(i)} = \frac{z_s}{\max(z) + \epsilon}$.
   - Coverage ratio factor: $C^{(i)} = 1 + \frac{2\delta^{(i)}}{S}$.
   $$\mathscr{L}_{\text{extreme}} = -\frac{1}{N_\alpha} \sum_{i=1}^{N_\alpha} C^{(i)} \sum_{s=1}^S \tilde{\phi}(\hat{\bm{y}}_i)_s \cdot \tilde{\phi}(\bm{y})_s \cdot v_s^{(i)}$$
3. **Diversity Regularizer ($\mathscr{L}_{\text{div}}$):**
   $$\mathscr{L}_{\text{diversity}} = \frac{1}{N_\alpha(N_\alpha - 1)} \sum_{i \ne j} \left|\rho\left(\phi(\hat{\bm{y}}_i),\, \phi(\hat{\bm{y}}_j)\right)\right|$$
4. **Composite Objective:**
   $$\mathscr{L} = \mathscr{L}_{\text{spearman}} + \mathscr{L}_{\text{extreme}} + \lambda \mathscr{L}_{\text{diversity}}$$
   where $\lambda = 0.1$ by default, and default $N_\alpha = 24$.

### Inference & Portfolio Construction
- Staggered multi-phase evaluation over $W = 5$ days:
  - For each formation day $d$, each alpha $a \in \{1, \ldots, N_\alpha\}$ selects its top $k=5$ stocks: $\mathcal{S}^{(d,a)} = \operatorname{arg\,top\text{-}k}_s \bm{P}[d,s,a]$.
  - Softmax weighting within each sub-portfolio: $w_s^{(d,a)} = \frac{\exp(\bm{P}[d,s,a])}{\sum_{j \in \mathcal{S}^{(d,a)}} \exp(\bm{P}[d,j,a])}$.
  - Sub-portfolio holding return at offset $\tau \in \{0, \ldots, W-1\}$: $r_\tau^{(d,a)} = \sum_{s \in \mathcal{S}^{(d,a)}} w_s^{(d,a)} \bm{R}[d+\tau, s]$.
  - Equal-weighted ensemble combination across all $N_\alpha$ alphas:
    $$r_\tau^{(d)} = \frac{1}{N_\alpha} \sum_{a=1}^{N_\alpha} r_\tau^{(d,a)}$$
  - Phase assignment: day $d$ maps to phase $w = d \bmod W$. Cumulative returns and metrics are computed per phase and averaged across all $W=5$ phases.

## Required data

- **Universe:** 
  - CSI300 (295 constituents)
  - CSI500 (514 constituents)
  - NI225 (209 constituents)
  - S&P 500 (525 constituents)
- **Venue:** China (SSE/SZSE), Japan (TSE), United States (NYSE/NASDAQ).
- **Market Type:** Spot cash equities.
- **Timeframe:** Daily frequency, end-of-day bars.
- **Fields:** Open, High, Low, Close, Volume.
- **Point-in-Time:** Standardized rolling 20-day trailing statistics for features; strictly forward 5-day return targets for labels. No backward look-ahead leakage.
- **Missing Data Handling:** Fixed universes per evaluation set; survivorship bias handling not explicitly audited in the source paper beyond standard Qlib/academic dataset baselines.

## Execution assumptions

- **Execution Cadence:** Every $W=5$ trading days per rebalancing phase (staggered across 5 circular phases).
- **Order Timing:** Formed at day $d$ close, executed for holding offsets $\tau = 0, \ldots, 4$.
- **Position Allocation:** Long-only, top $k=5$ names per alpha; union of selected names across $N_\alpha = 24$ heads is held with weights proportional to softmax conviction summed across heads.
- **Transaction Costs (Appendix C.1 & Table 7):**
  - CSI300 & CSI500: ~0.006% buy, ~0.056% sell (total round-trip 0.062%, yielding ~3.12% annualized drag at 100% 5-day turnover).
  - NI225: ~0.002% both sides (total round-trip 0.004%, yielding ~0.20% annualized drag).
  - S&P 500: modeled as 0.0% (assumed negligible institutional cost in the paper; recognized as an execution gap).
- **Slippage & Impact:** Not explicitly modeled beyond fixed basis-point cost deductions.
- **Shorting / Borrow:** Not applicable (long-only equity framework).

## Evidence

### Source-reported

All figures trace directly to Den, Chen, Vincent, & Chang (arXiv:2607.24131v1, Tables 1, 2, 3, 4, 7, 8, and Appendix D):

#### Main Out-of-Sample Performance (2021–2024, Without Costs, Table 1):
| Market | Metric | MAPLE ($N_\alpha=24$) | RankLSTM | MASTER | AlphaMix | MERA | DHMoE | TIPS |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CSI300** | Sharpe Ratio (SR) | **1.851** | 0.753 | 0.991 | 0.708 | 1.075 | 0.961 | 1.343 |
| | Calmar Ratio (CR) | **2.062** | 0.663 | 0.879 | 0.584 | 1.055 | 0.977 | 1.523 |
| **CSI500** | Sharpe Ratio (SR) | **2.161** | 0.869 | 1.198 | 1.064 | 0.677 | 1.716 | 2.010 |
| | Calmar Ratio (CR) | 1.961 | 0.699 | 1.044 | 0.959 | 0.472 | **2.490** | 2.466 |
| **NI225** | Sharpe Ratio (SR) | **0.991** | 0.610 | 0.730 | 0.543 | 0.769 | 0.679 | 0.958 |
| | Calmar Ratio (CR) | 0.783 | 0.447 | 0.616 | 0.458 | 0.554 | 0.585 | **0.784** |
| **SP500** | Sharpe Ratio (SR) | **1.758** | 1.414 | 1.477 | 1.574 | 1.117 | 0.980 | 1.506 |
| | Calmar Ratio (CR) | **3.896** | 2.138 | 2.398 | 2.486 | 1.131 | 0.680 | 2.965 |
| **4-Mkt Avg** | **Sharpe Ratio (SR)** | **1.690** | 0.912 | 1.099 | 0.972 | 0.910 | 1.084 | 1.454 |
| | **Calmar Ratio (CR)** | **2.175** | 0.987 | 1.234 | 1.122 | 0.828 | 1.222 | 1.934 |

#### Efficiency Performance (Table 1):
- Parameters: MAPLE uses **186,480** parameters (vs. DHMoE: 10,284,722; MERA: 1,460,017; MASTER: 726,601; TIPS: 104,897; RankLSTM: 52,289).
- Training Time: **3.601 s/epoch** (vs. TIPS: 7.236 s; MERA: 8.932 s; CI-STHPAN: 9.001 s; DHMoE: 4.499 s).
- Inference Computational Cost: **0.130 GFLOPs**, **38.142 MB** GPU memory, **1.685 ms** latency.

#### Main Out-of-Sample Performance With Transaction Costs (Table 7):
| Market | Metric | MAPLE | RankLSTM | MASTER | AlphaMix | MERA | DHMoE | TIPS |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CSI300** | SR / CR | **1.786** / **1.990** | 0.658 / 0.548 | 0.811 / 0.719 | 0.588 / 0.485 | 0.967 / 0.949 | 0.709 / 0.721 | 1.260 / 1.428 |
| **CSI500** | SR / CR | **2.118** / 1.922 | 0.792 / 0.605 | 1.019 / 0.888 | 0.960 / 0.866 | 0.614 / 0.428 | 1.458 / 2.115 | 1.949 / **2.392** |
| **NI225** | SR / CR | **0.985** / 0.778 | 0.603 / 0.441 | 0.721 / 0.608 | 0.536 / 0.452 | 0.761 / 0.548 | 0.669 / 0.577 | 0.952 / **0.779** |
| **SP500** | SR / CR | **1.758** / **3.896** | 1.414 / 2.138 | 1.477 / 2.398 | 1.574 / 2.486 | 1.117 / 1.131 | 0.980 / 0.680 | 1.506 / 2.965 |
| **4-Mkt Avg** | **SR / CR** | **1.662** / **2.146** | 0.867 / 0.933 | 1.007 / 1.153 | 0.915 / 1.072 | 0.865 / 0.764 | 0.954 / 1.023 | 1.417 / 1.891 |

#### Component Ablation (Table 2, 4-Market Average):
- Vanilla Transformer ($N_\alpha=1$): AR 0.865, SR 1.402, CR 1.713.
- (a) + Multi-Alpha ($N_\alpha=8$, intra-only): AR 0.923, SR 1.434, CR 1.779.
- (b) + Lightweight Attention: AR 0.509, SR 1.414, CR 1.676.
- (b) + Prediction-level Residual Aggregation: AR 0.633, SR 1.483, CR 1.826.
- (c) Vanilla Spearman + Diversity (Counter-example): AR 0.443, SR 1.415, CR 1.590.
- (c) + Extreme-Rank Loss ($\mathscr{L}_{\text{ext}}$): AR 1.035, SR 1.510, CR 1.856.
- (c) + Diversity Control ($\lambda=0.1$): AR 0.830, SR 1.579, CR 1.996.
- (d) + Capacity Scaling: AR 1.208, SR 1.660, CR 2.031.
- (e) Full MAPLE ($N_\alpha=24$): **AR 1.297**, **SR 1.690**, **CR 2.175**.

#### Generalizability Across 5 Backbones (Table 8, 4-Market Average):
- **TCN:** Baseline SR 1.160 / CR 1.108 $\to$ +MAPLE **SR 1.311** / **CR 1.484** (+13.0% SR, +33.9% CR).
- **GRU:** Baseline SR 1.280 / CR 1.406 $\to$ +MAPLE **SR 1.580** / **CR 2.013** (+23.4% SR, +43.2% CR).
- **LSTM:** Baseline SR 1.225 / CR 1.232 $\to$ +MAPLE **SR 1.485** / **CR 1.727** (+21.2% SR, +40.2% CR).
- **Mamba:** Baseline SR 1.272 / CR 1.425 $\to$ +MAPLE **SR 1.403** / **CR 1.671** (+10.3% SR, +17.3% CR).
- **Transformer:** Baseline SR 1.402 / CR 1.713 $\to$ +MAPLE **SR 1.690** / **CR 2.175** (+20.5% SR, +27.0% CR).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Catastrophic Failure of Global Spearman + Diversity:** When standard Spearman loss is combined with diversity regularization without extreme-rank weighting, annual return drops sharply from 0.633 to 0.443 and Sharpe drops from 1.483 to 1.415 (Table 2). Table 4 proves that this failure occurs because diversity regularization without extreme anchoring blows out the union selection size to 21.39 stocks (from 7.53) while collapsing precision at top-50 from 0.223 to 0.203.
- **Standalone Extreme Loss Toxicity:** Training solely with $\mathscr{L}_{\text{ext}}$ without global Spearman ($\mathscr{L}_{\text{spr}}$) results in the highest raw return ($\mu_r = 0.49\%$) but the highest daily volatility ($\sigma_r = 0.058$), producing the lowest return-to-volatility ratio (0.084 vs. baseline 0.100 and full MAPLE 0.112, Table 4). Extreme loss alone over-concentrates all heads onto the same extreme names (overlap ratio 0.930, union size 5.92), destroying ensemble diversification.
- **Over-regularization Collapse ($\lambda > 0.2$):** Figure 5 and Table 9 show that increasing the diversity weight beyond $\lambda = 0.2$ causes monotonic degradation in Calmar Ratio across all configurations (dropping from peak 2.175 at $\lambda=0.1$ to 1.767 at $\lambda=0.4$). The diversity penalty overwhelms ranking accuracy when forced beyond naturally emerging correlation floors.
- **CSI500 Drawdown Underperformance:** On CSI500, MAPLE's Calmar Ratio (1.961) is beaten by DHMoE (2.490) and TIPS (2.466), indicating that in highly speculative mid/small-cap environments, diffusion or distillation architectures may constrain tail drawdowns more effectively than listwise ranking decorrelation.
- **Frictionless US Modeling Gap:** S&P 500 transaction costs are set to 0.0% in Table 7, creating an unverified friction gap for US equities under actual broker commissions and bid-ask spreads.

## Falsification plan

1. **Market-Neutral Long/Short Verification:**
   - *Test:* Form a dollar-neutral portfolio by going long the top $k=5$ and short the bottom $k=5$ stocks per alpha head.
   - *Failure Criteria:* Annualized alpha $< 5.0\%$ or Sharpe ratio $< 0.8$ after deducting borrowing/lending fees and transaction costs, disproving the claim that learned representations capture symmetric relative-value information rather than long-only market drift.
2. **Extreme-Rank Parameter Perturbation:**
   - *Test:* Perturb the initialization of sharpness $\xi \in \{2, 5, 20\}$ (default 10) and margin scale $\gamma \in \{0.5, 0.7, 0.9\}$ (default 0.8).
   - *Failure Criteria:* Learned transition margins fail to converge or test Sharpe ratio drops by $> 15\%$ on CSI300/SP500, indicating parameter sensitivity and fragility of the sigmoidal coverage correction.
3. **Diversity Regularizer Ablation ($\lambda = 0$ Baseline):**
   - *Test:* Train the model with $\lambda = 0.0$ (no diversity penalty) at $N_\alpha = 24$.
   - *Failure Criteria:* If the $\lambda = 0.0$ model matches or exceeds the $\lambda = 0.1$ model's out-of-sample Calmar ratio ($\ge 2.175$), then the diversity regularizer contributes no distinct economic value beyond multi-head random parameter initialization.
4. **Execution Friction & Turnover Stress:**
   - *Test:* Impose realistic institutional US equity transaction costs of 5 to 10 bps per half-turn on S&P 500.
   - *Failure Criteria:* If net annualized Sharpe ratio falls below 1.20 (a decline $> 30\%$), the reported outperformance is an artifact of frictionless trading assumptions.
5. **Cross-Sectional Decoupling Test:**
   - *Test:* Shuffle the stock ordering input to the inter-stock attention module $\bm{W}_Q, \bm{W}_K$ at inference time while keeping temporal embeddings intact.
   - *Failure Criteria:* If performance degradation is statistically indistinguishable from zero ($p > 0.05$), the inter-stock attention mechanism provides no genuine relational cross-sectional alpha.

## Crypto portability

- **Portability Status:** **Adapted / unproven**.
- **Asset-Class Divergence:** The primary paper evaluates exclusively equity index components (CSI300, CSI500, NI225, S&P 500). Applying MAPLE to cryptocurrency markets is an unproven research hypothesis.
- **Cross-Sectional Universe Scale:**
  - Equity universes contain hundreds of liquid names ($S \in [209, 525]$). Crypto perpetual futures have a much smaller liquid universe ($S \in [30, 80]$ liquid pairs on Binance/Bybit).
  - High inter-asset correlation in crypto (systemic Bitcoin beta $> 0.7$ for most altcoins) restricts the degree of true cross-sectional signal decorrelation that $N_\alpha = 24$ heads can extract.
- **Continuous 24/7 Session & Rebalancing Costs:**
  - Equities feature discrete daily closes. Crypto perpetuals trade continuously with 8-hour funding rate cycles.
  - Holding multi-day positions ($W = 5$ days) in crypto perpetuals exposes the portfolio to funding rate drag, which frequently offsets gross cross-sectional momentum or ranking premia.
- **Liquidity & Market Impact:**
  - Smaller altcoins suffer from severe order book depth decay. A top-5 equal-weight or softmax-weighted portfolio could incur prohibitive slippage during high-volatility liquidations.
- **Required Adaptations for Crypto Testing:**
  - Restrict universe to top-30 perpetual futures by 30-day average daily volume.
  - Shorten the forecasting horizon from $q=5$ days to $q \in \{8\text{h}, 24\text{h}\}$.
  - Incorporate funding rate payments directly into the training return target: $y_t^{\text{net}} = y_t - \sum \text{funding\_rate}$.

## Limitations

- **Equities-Only Empirical Scope:** Empirical evidence is restricted to four national stock indices; no validation on commodities, FX, fixed income, or crypto.
- **Unverified US Execution Frictions:** S&P 500 results assume 0.0% transaction costs; net institutional returns remain unverified under real-world slippage and commissions.
- **Single Forecast Horizon ($q=5$):** All experiments utilize a fixed 5-day return target; interactions across heterogeneous holding periods or multi-horizon ensembles are unexamined.
- **Heuristic Coverage Correction:** The coverage factor $C^{(i)} = 1 + \frac{2\delta^{(i)}}{S}$ is an empirical first-order compensation rather than an exact analytical normalization.
- **Shared Temporal Encoder Bottleneck:** All $N_\alpha$ alpha heads share a single temporal backbone $t_\theta$, bounding the architectural and semantic diversity achievable compared to genuine multi-model ensembles.
- **Survivorship & Restructuring Bias:** Dataset construction details in Qlib baselines rely on static constituent lists over extended periods, potentially introducing survivorship bias.

## Implementation status

Not implemented. This record captures external research and architectural designs from arXiv:2607.24131v1. No implementation exists in our PyBroker or NautilusTrader repositories.

## Adoption boundary

Research-only. This document does not authorize strategy adoption, model training in production pipelines, paper trading, testnet deployment, or live capital allocation. Any progression toward backtesting or implementation requires independent review and validation against our execution standards.

## Related Wiki records

- `[[quant/alphacrafter-harness-multi-agent-cross-sectional-equity-alpha-2026-09-03]]` — Multi-agent cross-sectional equity alpha generation and ranking framework.
- `[[quant/fineft-risk-aware-ensemble-rl-vae-routing-crypto-futures-2026-09-03]]` — Risk-aware ensemble reinforcement learning and mixture routing.
- `[[quant/cross-sectional-equity-ridge-percentile-rank-alpha-2026-09-03]]` — Cross-sectional equity percentile ranking and linear factor models.
- `[[quant/lstm-learnable-sector-embeddings-cross-sectional-reversal-2026-09-02]]` — Cross-sectional equity conditioning via learnable sector embeddings.

## Sources

- Den, Y.-C., Chen, K.-Y., Vincent, K., & Chang, T.-H. (2026). MAPLE: Efficient and Diverse Multi-Alpha Generation for Portfolio Construction. arXiv preprint arXiv:2607.24131v1 [cs.LG, cs.CE], submitted July 27, 2026. DOI: [10.48550/arXiv.2607.24131](https://doi.org/10.48550/arXiv.2607.24131). URL: [https://arxiv.org/abs/2607.24131](https://arxiv.org/abs/2607.24131). Full text (HTML): [https://arxiv.org/html/2607.24131v1](https://arxiv.org/html/2607.24131v1).
