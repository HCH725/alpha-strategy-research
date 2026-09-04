---
schema: strategy-research-record-v1
title: "STN-TGAT: Top-K Portfolio Construction via Prior-Guided Graph Attention with Learnable Soft-Threshold Sparsification (Guo, Lu, & Zhang 2026)"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - graph-neural-network
  - transformer
  - stock-ranking
  - mutual-information
  - portfolio-optimization
status: research-only
confidence: medium
source_as_of: 2026-07-23
sources:
  - "Haoran Guo, Yutong Lu, and Li Zhang, 'STN-TGAT: Top-K Portfolio Construction via Prior-Guided Graph Attention with Learnable Soft-Threshold Sparsification', arXiv:2607.19385v1 [cs.LG], July 23, 2026. https://arxiv.org/abs/2607.19385"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# STN-TGAT: Top-K Portfolio Construction via Prior-Guided Graph Attention with Learnable Soft-Threshold Sparsification

## Provenance

- **Paper Title:** STN-TGAT: Top-K Portfolio Construction via Prior-Guided Graph Attention with Learnable Soft-Threshold Sparsification
- **Authors:**
  - Haoran Guo (Institute of Financial Technology, University College London, London, UK; `haoran.guo.24@ucl.ac.uk`)
  - Yutong Lu (University of Oxford, Oxford, UK; `yutong.lu@institute2.ac.uk`)
  - Li Zhang (Institute of Financial Technology, University College London, London, UK; corresponding author: `ucesl07@ucl.ac.uk`)
- **Identifier:** arXiv:2607.19385v1 [cs.LG], submitted July 23, 2026.
- **Digital Object Identifier (DOI):** [10.48550/arXiv.2607.19385](https://doi.org/10.48550/arXiv.2607.19385)
- **Primary Source URLs:**
  - Abstract: [https://arxiv.org/abs/2607.19385](https://arxiv.org/abs/2607.19385)
  - PDF: [https://arxiv.org/pdf/2607.19385](https://arxiv.org/pdf/2607.19385)
  - HTML Source: [https://arxiv.org/html/2607.19385v1](https://arxiv.org/html/2607.19385v1)
  - TeX Source Package: [https://arxiv.org/src/2607.19385](https://arxiv.org/src/2607.19385) (extracted and inspected `main.tex` directly)
- **Target Conference / Venue:** Prepared under Springer LNCS template for ECML PKDD 2026 proceedings.
- **Investable Universe:** 50 largest constituents of the S&P 500 index by market capitalization selected at the start of the sample period (2022-01-03) to mitigate survivorship bias.
- **Sample Period:** 752 NYSE trading days spanning January 3, 2022 to December 30, 2024. Partitioned chronologically into training (80%), validation (10%), and out-of-sample testing (10%, approximately 75 trading days in late 2024).
- **Source Data As-Of:** July 23, 2026.

## Economic mechanism

### Source-reported

In quantitative asset management, daily equity portfolio construction is naturally formulated as a repeated Top-$K$ selection problem: on each trading day, an investable universe is cross-sectionally ranked, and capital is concentrated into a small subset of the highest-ranked assets ($K=5$) under transaction costs and portfolio rebalancing constraints. In this decision-centric setting, minimizing global pointwise prediction error (such as Mean Squared Error across all assets) is misaligned with the real investment objective, as realized portfolio returns are driven almost entirely by relative ranking precision at the top of the distribution.

Existing quantitative forecasting approaches face structural limitations:
1. **Independent time-series neglect cross-sectional dependencies:** Standard linear models (ARIMA, GARCH) and deep sequential models (LSTM, GRU) process each asset's sequence independently, ignoring cross-asset co-movements induced by common sector membership, supply chains, shared factor exposures, and macro shocks.
2. **Dense graph noise and over-smoothing:** Applying Graph Neural Networks (GNNs) directly over unconstrained or fully connected dependency graphs leads to rapid over-smoothing and noise propagation. Conversely, static graphs or heuristic hard-thresholding techniques (such as arbitrary correlation cutoffs or minimum spanning trees) are fragile under market regime shifts and discard subtle yet informative relational channels.
3. **Objective mismatch in standard loss functions:** Standard pointwise loss functions (MSE) calibrate average return levels rather than relative ranks. Standard ListNet ranking losses align the entire distribution equally, whereas Top-$K$ selection cares almost exclusively about discrimination in the top decile.

The authors propose the **Soft-Thresholded NMI-prior Transformer Graph Attention Network (STN-TGAT)** to solve these challenges through three synchronized mechanisms:
- **Nonlinear Dependence Prior (NMI):** An adjacency prior constructed from Normalized Mutual Information (NMI) over historical log returns captures complex, nonlinear co-dependencies that linear correlation misses.
- **Learnable Soft-Threshold Sparsification:** A differentiable sigmoid gating mechanism adaptively attenuates weak and noisy edges based on a jointly learned threshold $t_g$ and sharpness $eta$, while graph sparsity regularization keeps global connectivity well-conditioned.
- **Decision-Aligned Head-Weighted ListNet Objective:** A listwise ranking loss that applies geometrically decaying position weights to prioritize ranking precision in the upper tail of the cross-section, paired with an auxiliary MSE loss that anchors score magnitudes to enable conviction-weighted portfolio allocation.

### Research interpretation

The hypothesized economic mechanism is **adaptive nonlinear structural filtering of cross-sectional information spillovers**:
1. **Heterogeneous information diffusion among mega-caps:** Large-cap equities exhibit shared operational, macroeconomic, and factor exposures that transmit with varying speeds and non-linear dependencies. High pairwise mutual information indicates genuine co-dependence channels (e.g., tech platform ecosystems, semiconductor supply chains).
2. **Structural pruning as signal extraction:** The vast majority of pairwise equity correlations in a 50-stock universe reflect transient statistical noise or market beta rather than persistent informational relationships. Learnable soft-thresholding acts as an end-to-end data filter, suppressing spurious inter-stock connections that cause GAT attention weights to disperse across uninformative neighbors.
3. **Tail-concentrated payoff asymmetry:** For a concentrated long-only Top-5 equity portfolio, ordering errors among the bottom 45 stocks have exactly zero economic consequence on realized portfolio returns. Head-weighted listwise optimization concentrates parameter updates on separating top-performing outliers from the rest of the pack, maximizing the information ratio where capital is actually allocated.

## Signal

### Mathematical formulation (Source-reported)

1. **Input Representation:**
   For trading day $t$, input features for $N = 50$ stocks across lookback window length $L$ and feature dimension $F$ form tensor:
   $$\mathbf{X} \in \mathbb{R}^{N \times L \times F}$$
   The $i$-th stock's temporal feature sequence is $\mathbf{X}_i \in \mathbb{R}^{L \times F}$.

2. **NMI-based Dependence Graph Initialization:**
   Let $r_i = \{\Delta \log P_{\tau,i}\}_{\tau=1}^T$ denote the historical return series of stock $i$ over the training window. Mutual information is estimated using histogram-based equal-width binning with $k_b$ bins:
   $$\mathrm{NMI}(r_i, r_j) = \frac{2\,I(r_i; r_j)}{H(r_i) + H(r_j)} \in [0, 1]$$
   where $I(r_i; r_j)$ is mutual information and $H(\cdot)$ is Shannon entropy. This yields initial dense adjacency matrix $\mathbf{A}_0 \in \mathbb{R}^{N \times N}$ with $(\mathbf{A}_0)_{ij} = \mathrm{NMI}(r_i, r_j)$.

3. **Learnable Soft-Threshold Sparsification:**
   A differentiable gating matrix $\mathbf{G} = [g_{ij}] \in (0,1)^{N \times N}$ is defined by:
   $$g_{ij} = \sigma\big(\beta ((\mathbf{A}_0)_{ij} - t_g)\big)$$
   where $\sigma(\cdot)$ is the sigmoid function, $\beta > 0$ controls transition sharpness, and $t_g \in (0,1)$ is a learnable threshold parameter optimized end-to-end.
   The sparsified adjacency is computed by Hadamard modulation:
   $$\mathbf{A}_\phi = \mathbf{A}_0 \odot \mathbf{G}$$
   followed by symmetrization, global max-scaling, and diagonal self-connection shift:
   $$\mathbf{A}_\phi \leftarrow \frac{1}{2}(\mathbf{A}_\phi + \mathbf{A}_\phi^\top), \quad \mathbf{A}_\phi \leftarrow \frac{\mathbf{A}_\phi}{\max_{i,j}(\mathbf{A}_\phi)_{ij}}, \quad \mathbf{A}_\phi \leftarrow \mathbf{A}_\phi + \delta \mathbf{I}$$

4. **Temporal Transformer Encoder:**
   Temporal features undergo linear projection and sinusoidal positional encoding:
   $$\bar{\mathbf{X}} = \mathbf{X}\mathbf{W}^{(I)} + \mathbf{PE}$$
   where $\mathbf{W}^{(I)} \in \mathbb{R}^{F \times d}$. An encoder-only Transformer processes $\bar{\mathbf{X}}$ into hidden states $\mathbf{H} \in \mathbb{R}^{N \times L \times d}$.
   Temporal attention pooling extracts fixed-size daily stock representations $\mathbf{z}_i \in \mathbb{R}^d$ using learnable query $\mathbf{q} \in \mathbb{R}^d$:
   $$a_{i,t} = \frac{\exp(\langle \mathbf{h}_{i,t}, \mathbf{q} \rangle)}{\sum_{k=1}^L \exp(\langle \mathbf{h}_{i,k}, \mathbf{q} \rangle)}, \quad \mathbf{z}_i = \sum_{t=1}^L a_{i,t} \mathbf{h}_{i,t}$$
   stacking into cross-sectional matrix $\mathbf{Z} \in \mathbb{R}^{N \times d}$.

5. **GAT with Injected NMI Prior:**
   Let $\mathbf{H}^{(0)} = \mathbf{Z}$. In layer $\ell$ and attention head $h$, each node $i$ attends to its $K_{\text{nbr}}$ strongest neighbors $\mathcal{N}(i)$ under $\mathbf{A}_\phi$. Attention logits inject the structural prior directly:
   $$e_{ij}^{(\ell,h)} = \frac{\mathrm{LeakyReLU}\big(\mathbf{a}^{(\ell,h)\top}[\mathbf{H}_i^{(\ell,h)} \,\|\, \mathbf{H}_j^{(\ell,h)}]\big)}{\tau_{\text{a}}} + \lambda \log\big((\mathbf{A}_\phi)_{ij} + \varepsilon\big)$$
   where $\mathbf{a}^{(\ell,h)} \in \mathbb{R}^{2d_h}$ is learnable, $\tau_{\text{a}} > 0$ controls attention temperature, $\varepsilon > 0$ is a stability constant, and $\lambda \in (0,1)$ governs structural prior strength.
   Attention weights are normalized via softmax over $\mathcal{N}(i)$:
   $$\alpha_{ij}^{(\ell,h)} = \frac{\exp(e_{ij}^{(\ell,h)})}{\sum_{k \in \mathcal{N}(i)} \exp(e_{ik}^{(\ell,h)})}$$
   Multi-head aggregations are combined with residual connections and layer normalization across $L_g$ layers to produce $\mathbf{H}^{(L_g)} \in \mathbb{R}^{N \times d}$.

6. **Prediction Head:**
   Stock-level alpha scores $s_i$ are generated by a shared linear output projection:
   $$s_i = \mathbf{w}_{\text{out}}^\top \mathbf{H}_i^{(L_g)} + b, \quad \mathbf{s} \in \mathbb{R}^N$$

7. **Multi-Objective Loss Function:**
   $$\mathcal{L} = \mathcal{L}_{\mathrm{list}} + \mathcal{L}_{\mathrm{mse}} + \mathcal{L}_{\mathrm{graph}}$$
   - **Head-Weighted ListNet:**
     Student distribution: $P_i = \frac{\exp(s_i)}{\sum_{j=1}^N \exp(s_j)}$.
     Teacher distribution: $Q_i = \frac{\exp(y_i^{\mathrm{rank}} / \tau_{\mathrm{rank}})}{\sum_{j=1}^N \exp(y_j^{\mathrm{rank}} / \tau_{\mathrm{rank}})}$, where $y_i^{\mathrm{rank}} = (r_{i,t} - \mu_t)/\sigma_t$.
     Geometrically decaying position weights:
     $$w_i = \frac{\max(\gamma^{\mathrm{pos}(i)}, w_{\min})}{\sum_{j=1}^N \max(\gamma^{\mathrm{pos}(j)}, w_{\min})}$$
     Weighted ranking loss: $\mathcal{L}_{\mathrm{list}} = \sum_{i=1}^N w_i Q_i (\log Q_i - \log P_i)$.
   - **Auxiliary MSE Loss:**
     $$\mathcal{L}_{\mathrm{mse}} = \frac{1}{N}\sum_{i=1}^N (s_i - y_i)^2$$
     where $y_i = r_{i,t} = \log P_{i,t} - \log P_{i,t-1}$.
   - **Graph Sparsity Regularization:**
     $$\mathcal{L}_{\mathrm{graph}} = \frac{1}{N(N-1)}\sum_{i \ne j}(\mathbf{A}_\phi)_{ij} + \left(\frac{1}{N(N-1)}\sum_{i \ne j} g_{ij} - \rho\right)^2$$
     where $\rho \in (0,1)$ is the target graph sparsity level.

8. **Portfolio Construction & Allocation:**
   - On day $t$, select the Top-$K$ assets ($K=5$):
     $$\mathcal{S} = \operatorname{TopK}(\mathbf{s}, 5)$$
   - Conviction-Weighted Softmax Allocation (Table 4 optimal):
     $$w_i = \frac{\exp(s_i)}{\sum_{j \in \mathcal{S}} \exp(s_j)}, \quad \forall i \in \mathcal{S}$$
   - Equal-Weighted Alternative: $w_i = 1/K = 0.20$.

### Operational Specifications & Parameter Classifications

- **Formation Timestamp:** Daily, calculated at the market close of trading day $t$ using features observed through day $t$.
- **Execution Timestamp / Order Timing:** Stated as daily close-to-close rebalancing. `research-proposed` Market-On-Close (MOC) execution on day $t$ or Market-On-Open (MOO) on day $t+1$ ($T_{\text{exec}} = t+1\text{ Open}$).
- **Holding Period:** Daily rebalancing (1 trading day holding period per rebalance step).
- **Universe & Sample Definition (Source-reported):** Top 50 S&P 500 constituents by market capitalization as of 2022-01-03.
- **Lookback Window ($L$):** Paper specifies rolling window length $L$, but numeric value is omitted from primary submission text due to appendix omission. `research-proposed` $L = 20$ trading days (1 calendar month).
- **Feature Dimension ($F$):** Stated as daily OHLCV from Yahoo Finance ($F=5$). `research-proposed` includes normalized returns and volume ratios.
- **Histogram Bin Count ($k_b$):** Omitted in primary text. `research-proposed` $k_b = 10$ equal-width bins over training-window return distributions.
- **Graph Gating Sharpness ($\beta$):** Omitted in primary text. `research-proposed` $\beta = 10.0$.
- **Graph Sparsity Target ($\rho$):** Omitted in primary text. `research-proposed` $\rho = 0.15$ (retaining top 15% edge density).
- **GAT Neighbor Count ($K_{\text{nbr}}$):** Omitted in primary text. `research-proposed` $K_{\text{nbr}} = 10$ nearest neighbors.
- **Prior Logit Weight ($\lambda$):** Omitted in primary text. `research-proposed` $\lambda = 0.5$.
- **ListNet Position Decay ($\gamma, w_{\min}$):** Omitted in primary text. `research-proposed` $\gamma = 0.85, w_{\min} = 0.05$.
- **Teacher Sharpness ($\tau_{\mathrm{rank}}$) & Attention Temperature ($\tau_{\text{a}}$):** Omitted in primary text. `research-proposed` $\tau_{\mathrm{rank}} = 1.0, \tau_{\text{a}} = 1.0$.
- **Diagonal Self-Shift ($\delta$):** Omitted in primary text. `research-proposed` $\delta = 1.0$.

## Required data

- **Universe:** 50 largest S&P 500 common stocks by market cap as of 2022-01-03.
- **Venue:** NYSE and NASDAQ.
- **Market Type:** US cash equities.
- **Timeframe:** Daily bars (OHLCV).
- **Data Source:** Yahoo Finance aligned with NYSE trading calendar.
- **Required Fields:** Open, High, Low, Close, Volume, and split/dividend-adjusted closing prices.
- **Target Variables:**
  - Realized log return: $r_{i,t} = \log P_{i,t} - \log P_{i,t-1}$.
  - Standardized ranking target: $y_{i,t}^{\mathrm{rank}} = (r_{i,t} - \mu_t)/\sigma_t$.
- **Point-in-Time & Leakage Controls (Source-reported):**
  - Features are winsorized at 3 standard deviations.
  - Standardization parameters ($\mu, \sigma$) computed strictly on training split (first 80% of chronological sample, 2022-01-03 to mid-2024).
  - Train/Validation/Test split is strictly chronological (8:1:1), avoiding walk-forward look-ahead.
- **Missing Data Handling:** `research-proposed` Trading suspensions or missing price bars forward-filled using last available adjusted close; stocks suspended for $>5$ consecutive days removed from that day's candidate ranking.

## Execution assumptions

- **Rebalance Cadence:** Daily rebalance (close-to-close).
- **Portfolio Constraints (Source-reported):** Long-only, Top-5 selection ($K=5$) from $N=50$ stocks.
- **Leverage & Margin:** 1.0x gross leverage (100% long equity, 0% short exposure, fully funded).
- **Transaction Costs & Fees:**
  - Primary paper states backtest is "evaluated using net-of-fee returns with proportional turnover costs" (Section 5.3, Table 1).
  - *Provenance Gap:* The exact fee schedule (basis points per turnover) was relegated to the omitted Appendix.
  - `research-proposed` Baseline transaction cost assumption: 5.0 bps one-way (10 bps round-trip) including institutional exchange fees, broker commissions, and bid-ask spread crossing for mega-cap US equities.
- **Fill Model:** `research-proposed` MOC (Market-On-Close) or MOO (Market-On-Open) executions assumed fully filled at print, justified by extreme liquidity in Top-50 S&P 500 equities where Top-5 portfolio trade sizes represent $<0.05\%$ of Average Daily Volume (ADV).
- **Borrow & Shorting:** Not applicable (long-only portfolio).

## Evidence

### Source-reported

All performance figures below are transcribed directly from Tables 1, 2, 3, and 4 in the primary paper (`main.tex`):
- **Sample:** 752 NYSE trading days (2022-01-03 to 2024-12-30), 8:1:1 split (test set $\approx 75$ trading days).
- **Metrics:** Mean Reciprocal Rank (MRR), Rank-Biased Overlap (RBO), Mean Squared Error (MSE), Cumulative Return (IRR), Annualized Sharpe Ratio, Maximum Drawdown (MDD).

#### 1. Benchmark Comparison (Table 1)

Evaluated across classical time-series (ARIMA), recurrent deep neural networks (GRU, LSTM), and GNN extensions (GRU-GCN, GRU-GAT) against STN-TGAT:

| Model | MRR $\uparrow$ | RBO $\uparrow$ | MSE $\downarrow$ | IRR (Return) $\uparrow$ | Sharpe Ratio $\uparrow$ | MDD (Drawdown) $\downarrow$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **ARIMA** | 0.1079 $\pm$ 0.0000 | 0.0316 $\pm$ 0.0000 | **0.0017 $\pm$ 0.0000** | 0.0426 $\pm$ 0.0000 (4.26%) | 1.1145 $\pm$ 0.0000 | **0.0456 $\pm$ 0.0066 (4.56%)** |
| **GRU** | 0.2120 $\pm$ 0.0059 | 0.0580 $\pm$ 0.0014 | 0.5142 $\pm$ 0.2321 | 0.1341 $\pm$ 0.0359 (13.41%) | 2.6553 $\pm$ 0.5632 | 0.0585 $\pm$ 0.0099 (5.85%) |
| **LSTM** | **0.2222 $\pm$ 0.0119** | **0.0601 $\pm$ 0.0024** | 0.2720 $\pm$ 0.4558 | 0.1143 $\pm$ 0.0377 (11.43%) | 2.1899 $\pm$ 0.6187 | 0.0719 $\pm$ 0.0086 (7.19%) |
| **GRU-GCN** | 0.0768 $\pm$ 0.0332 | 0.0193 $\pm$ 0.0117 | 1.0727 $\pm$ 1.3167 | -0.0435 $\pm$ 0.0166 (-4.35%) | -1.4598 $\pm$ 0.6272 | 0.0799 $\pm$ 0.0075 (7.99%) |
| **GRU-GAT** | 0.1760 $\pm$ 0.0127 | 0.0468 $\pm$ 0.0037 | 0.5013 $\pm$ 0.3264 | -0.0012 $\pm$ 0.0347 (-0.12%) | 0.0035 $\pm$ 0.7847 | 0.0799 $\pm$ 0.0075 (7.99%) |
| **STN-TGAT** | 0.1879 $\pm$ 0.0345 | 0.0509 $\pm$ 0.0118 | 0.3115 $\pm$ 0.4176 | **0.1807 $\pm$ 0.1176 (18.07%)** | **2.9940 $\pm$ 1.3287** | 0.0634 $\pm$ 0.0130 (6.34%) |

*Key finding:* While LSTM achieves slightly higher raw ranking accuracy metrics across the full cross-section (MRR 0.2222 vs 0.1879), STN-TGAT achieves substantially higher economic returns and risk-adjusted Sharpe (Sharpe 2.9940 vs 2.1899 for LSTM and 2.6553 for GRU) under net-of-fee backtesting.

#### 2. Loss Function Ablation (Table 2)

Isolating the contribution of the Head-Weighted ListNet objective, auxiliary MSE loss, and alternative ranking losses:

| Loss Configuration | RBO $\uparrow$ | MRR $\uparrow$ | IRR $\uparrow$ | Sharpe Ratio $\uparrow$ | MDD $\downarrow$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **ListNet + MSE** | 0.0516 $\pm$ 0.0127 | 0.1875 $\pm$ 0.0378 | 0.2132 $\pm$ 0.1309 (21.32%) | 3.3130 $\pm$ 1.5240 | **0.0618 $\pm$ 0.0136 (6.18%)** |
| **ListNet-only** | **0.0519 $\pm$ 0.0135** | **0.1904 $\pm$ 0.0401** | **0.2161 $\pm$ 0.1326 (21.61%)** | **3.3160 $\pm$ 1.5250** | 0.0646 $\pm$ 0.0142 (6.46%) |
| **MSE-only** | 0.0372 $\pm$ 0.0077 | 0.1263 $\pm$ 0.0195 | 0.0395 $\pm$ 0.0730 (3.95%) | 0.7570 $\pm$ 1.7100 | 0.0779 $\pm$ 0.0122 (7.79%) |
| **Spearman + MSE** | 0.0487 $\pm$ 0.0048 | 0.1643 $\pm$ 0.0245 | 0.0945 $\pm$ 0.0145 (9.45%) | 2.3560 $\pm$ 0.3300 | 0.0744 $\pm$ 0.0058 (7.44%) |
| **Pairwise + MSE** | 0.0407 $\pm$ 0.0076 | 0.1583 $\pm$ 0.0168 | 0.0646 $\pm$ 0.0543 (6.46%) | 1.4740 $\pm$ 1.0780 | 0.0812 $\pm$ 0.0227 (8.12%) |

*Key finding:* Models lacking the listwise ranking objective suffer severe degradation in investment performance: MSE-only achieves Sharpe of only 0.7570 (vs 3.3130 for ListNet+MSE), and Pairwise+MSE achieves only 1.4740.

#### 3. Relational Prior & Sparsification Ablation (Table 3)

Evaluating the impact of removing the NMI prior, replacing it with a linear graphical prior (GLASSO), and disabling soft-threshold sparsification:

| Model Variant | RBO $\uparrow$ | MRR $\uparrow$ | MSE $\downarrow$ | IRR $\uparrow$ | Sharpe Ratio $\uparrow$ | MDD $\downarrow$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Transformer-GAT (no prior)** | 0.0413 $\pm$ 0.0053 | 0.1521 $\pm$ 0.0214 | 0.5192 $\pm$ 0.3942 | 0.0863 $\pm$ 0.0692 (8.63%) | 1.8932 $\pm$ 1.2710 | 0.0574 $\pm$ 0.0093 (5.74%) |
| **Transformer-GAT (no sparsity)** | 0.0413 $\pm$ 0.0056 | 0.1514 $\pm$ 0.0266 | **0.3073 $\pm$ 0.3239** | 0.1152 $\pm$ 0.0551 (11.52%) | 2.5884 $\pm$ 0.9710 | **0.0520 $\pm$ 0.0116 (5.20%)** |
| **Transformer-GAT (GLASSO)** | 0.0406 $\pm$ 0.0072 | 0.1462 $\pm$ 0.0226 | 0.6019 $\pm$ 0.5262 | 0.0381 $\pm$ 0.0672 (3.81%) | 0.7480 $\pm$ 1.5070 | 0.0622 $\pm$ 0.0133 (6.22%) |
| **STN-TGAT (full framework)** | **0.0509 $\pm$ 0.0118** | **0.1879 $\pm$ 0.0345** | 0.3115 $\pm$ 0.4176 | **0.1807 $\pm$ 0.1176 (18.07%)** | **2.9940 $\pm$ 1.3287** | 0.0634 $\pm$ 0.0130 (6.34%) |

*Key finding:* Replacing the nonlinear NMI prior with a linear GLASSO prior collapses Sharpe from 2.9940 to 0.7480. Disabling learnable sparsification admits noisy edges, reducing Sharpe from 2.9940 to 2.5884.

#### 4. Allocation Scheme Ablation (Table 4)

Comparing within-Top-5 equal weighting vs conviction score weighting:

| Allocation Scheme | IRR $\uparrow$ | Sharpe Ratio $\uparrow$ | MDD $\downarrow$ |
| :--- | :---: | :---: | :---: |
| **Top-5 Equal Weight** | 0.1521 $\pm$ 0.1119 (15.21%) | 2.5595 $\pm$ 1.3979 | 0.0636 $\pm$ 0.0132 (6.36%) |
| **Top-5 Score Weight** | **0.1807 $\pm$ 0.1176 (18.07%)** | **2.9940 $\pm$ 1.3287** | **0.0634 $\pm$ 0.0130 (6.34%)** |

### Independently reproduced

`not independently reproduced`

### Negative evidence

1. **Unconstrained GNN Failure:** Standard GNN baselines without adaptive soft-thresholding catastrophically fail in portfolio evaluation: GRU-GCN produces negative return (-4.35%) and a Sharpe of -1.4598; GRU-GAT barely breaks even (+0.0035 Sharpe, -0.12% IRR). Dense graph propagation induces severe over-smoothing and noise amplification.
2. **Linear Prior Inadequacy:** Injecting a graphical LASSO (GLASSO) linear covariance prior yields worse results than having no graph prior at all (Sharpe 0.7480 for GLASSO vs 1.8932 for no prior), indicating that naive linear correlation maps introduce deceptive topology into neural attention layers.
3. **High Return Volatility Across Seeds:** STN-TGAT exhibits substantial variance across random seeds (IRR $18.07\% \pm 11.76\%$, Sharpe $2.9940 \pm 1.3287$). In unfavorable initialization regimes, portfolio performance drops sharply.
4. **Transaction Cost Sensitivity:** Daily rebalancing across a concentrated Top-5 basket creates high portfolio turnover. Although net-of-fee returns are reported, if execution costs exceed large-cap institutional levels (>15-20 bps round-trip), net Sharpe would deteriorate substantially.

## Falsification plan

The following empirical tests are defined to disconfirm the proposed STN-TGAT mechanism:

1. **Placebo Shuffled-Topology Test:**
   - *Procedure:* Randomly permute the stock labels in the pre-computed NMI matrix $\mathbf{A}_0$ while preserving its marginal weight distribution, then retrain the STN-TGAT architecture under identical seeds.
   - *Decision Rule:* `research-defined falsification threshold` If the model trained on the scrambled topology retains $\ge 80\%$ of the real-graph Sharpe ratio (i.e., test Sharpe $\ge 2.40$), falsify the hypothesis that the NMI dependency topology conveys genuine economic relation alpha.
2. **Multi-Regime Out-of-Sample Stress Test:**
   - *Procedure:* Backtest the model over a severe bear or volatility spike regime (e.g., 2020 COVID crash or 2022 Fed rate-hiking cycle).
   - *Decision Rule:* `research-defined falsification threshold` If annualized test Sharpe falls below $0.50$ or maximum drawdown exceeds $20.0\%$, falsify the claim that soft-thresholded relational representations provide stable downside protection across market regimes.
3. **Transaction Fee Slippage Stress:**
   - *Procedure:* Increment transaction cost assumptions from 5 bps up to 25 bps round-trip in 5 bps increments.
   - *Decision Rule:* `research-defined falsification threshold` If the net Sharpe ratio drops below $1.00$ at $10\text{ bps}$ round-trip costs, reject the strategy as an unviable high-turnover artifact.
4. **Execution Delay (Close-to-Open Timing Audit):**
   - *Procedure:* Enforce a realistic execution lag where scores generated from day $t$ close are executed at day $t+1$ VWAP or Open rather than idealized day $t$ close-to-close.
   - *Decision Rule:* `research-defined falsification threshold` If more than $40\%$ of cumulative IRR is eliminated under $t+1$ Open execution, classify the primary reported return as unexecutable close-to-close mark leakage.

## Crypto portability

**Adapted / Unproven**

The core mechanisms—nonlinear dependency modeling, learnable graph sparsification, and head-weighted listwise ranking—are conceptually portable to cryptocurrency markets. However, crypto market microstructure presents severe structural hurdles:

- **Ecosystem Network Construction (`research-proposed`):** Instead of S&P 500 equity returns, the crypto NMI dependence graph must be estimated over a universe of top liquid perpetual futures (e.g., top 30 Binance/Bybit perps). Alternatively, on-chain token flow or liquidity pool co-deposits can supplement returns.
- **24/7 Continuous Trading & Rebalance Timing:** Equities benefit from clean 16:00 EST daily closing auctions. In crypto, 24/7 trading requires choosing an arbitrary daily cut-off timestamp (e.g., 00:00 UTC) or transitioning to 8-hour funding rate interval rebalancing.
- **Extreme Cross-Asset Beta & Tail Co-Movement:** Crypto assets exhibit significantly higher pairwise correlations and market-wide beta to Bitcoin than S&P 500 equities. Under market sell-offs, cross-sectional NMI matrices tend to collapse into a single dominant factor, potentially causing the gating threshold $t_g$ to saturate and nullify graph sparsification benefits.
- **Funding Rate & Borrow Drag:** Top-5 long-only perpetual portfolios incur continuous funding rate payments during bullish speculative regimes, creating an additional performance drag not modeled in equity cash backtests.
- **Status:** Unproven. The primary paper presents zero empirical cryptocurrency experiments; all crypto porting remains an exploratory research hypothesis.

## Limitations

- **Omission of Primary Appendix:** The submitted paper omitted its Appendix, leaving exact numerical configurations for several hyperparameters ($k_b, K_{\text{nbr}}, \beta, \rho, \lambda, \tau_a, \tau_{\mathrm{rank}}, \gamma, L$) and the exact basis point fee schedule unspecified in the primary text. These remain a material provenance gap.
- **Short Evaluation Horizon:** The test split covers approximately 75 trading days (10% of 752 days) situated in late 2024. This evaluation window is too short to prove multi-year robustness across varied macroeconomic regimes.
- **High Variance Across Seeds:** A standard deviation of $\pm 1.3287$ on an annualized Sharpe of $2.9940$ indicates meaningful sensitivity to model weight initialization and stochastic training runs.
- **High Portfolio Concentration Risk:** Holding only 5 stocks (20% average allocation each) creates high idiosyncratic exposure to single-stock earnings surprises or black swan events.
- **Computational Overhead:** Training a coupled Transformer-GAT with pairwise NMI computation requires substantial GPU memory and compute, hindering rapid real-time re-estimation.
- **Not Independently Reproduced:** No physical replication of the codebase or data pipeline has been conducted in our research stack.

## Implementation status

`not-implemented`

No code, neural architecture definitions, NMI graph builders, or backtest harnesses for STN-TGAT have been integrated into PyBroker, NautilusTrader, or our research workflows. The strategy exists strictly as a normalized research record.

## Adoption boundary

This record is research material only. It does **not** constitute:
- Verified or profitable alpha in our operational universe.
- Authorization for paper trading, testnet deployment, or live capital allocation.
- Implementation in Nautilus or PyBroker without prior multi-year walk-forward backtesting, transaction fee stress audits, and execution timing verification.

## Related Wiki records

- `[[quant/dynamic-knowledge-graph-community-gated-signal-propagation-2026-09-04]]` (Dynamic knowledge graphs and community-gated signal propagation)
- `[[quant/graph-neural-network-volatility-minimum-variance-portfolio-2026-09-03]]` (Graph neural networks for covariance and portfolio optimization)
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` (Cross-validation and information leakage protections)

## Sources

1. Haoran Guo, Yutong Lu, and Li Zhang, "STN-TGAT: Top-K Portfolio Construction via Prior-Guided Graph Attention with Learnable Soft-Threshold Sparsification", arXiv:2607.19385v1 [cs.LG], submitted July 23, 2026. Available at: [https://arxiv.org/abs/2607.19385](https://arxiv.org/abs/2607.19385).
2. Primary TeX source bundle: `arXiv:2607.19385v1` (`main.tex`, inspected directly for Tables 1, 2, 3, 4 and Equations 1–13). Available at: [https://arxiv.org/src/2607.19385](https://arxiv.org/src/2607.19385).
