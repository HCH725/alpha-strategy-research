---
schema: strategy-research-record-v1
title: F2Agent Multimodal Agentic Adaptive Fusion Consistency Regularization
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - multimodal
  - agentic-ai
  - machine-learning
  - crypto
  - bitcoin
status: research-only
confidence: medium
source_as_of: "2026-08-07"
sources:
  - "Changshuo Liu, Yanzheng Jin, Shangfeng Cai, Peng Fang, Xiaokui Xiao, and Beng Chin Ooi, 'F^2Agent: Financial Fusion of Agentic Intelligence for Multimodal Trading', arXiv:2608.05668v1 [cs.MA], August 7, 2026. https://arxiv.org/abs/2608.05668"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# F2Agent: Financial Fusion of Agentic Intelligence for Multimodal Trading

## Provenance

- **Primary Source:** Changshuo Liu, Yanzheng Jin, Shangfeng Cai, Peng Fang, Xiaokui Xiao, and Beng Chin Ooi (National University of Singapore, Huazhong University of Science and Technology, Zhejiang University), "F$^2$Agent: Financial Fusion of Agentic Intelligence for Multimodal Trading," arXiv:2608.05668v1 [cs.MA], submitted August 7, 2026.
- **Canonical arXiv URL:** https://arxiv.org/abs/2608.05668
- **Canonical HTML URL:** https://arxiv.org/html/2608.05668v1
- **Primary Source Data Periods:**
  - Training window: 2023-10-01 to 2024-09-30 (12 months).
  - Validation window: 2024-10-01 to 2025-03-31 (6 months).
  - Primary evaluation window: 2025-04-01 to 2025-09-30 (6 months).
  - Extended evaluation window: 2025-04-01 to 2026-03-20 (~12 months).
- **Pre-Write Deduplication Audit:**
  - A full repository search for `arXiv:2608.05668`, `F2Agent`, `F^2Agent`, and author `Changshuo Liu` returned zero matching records.
  - Distinct from `colas-multimodal-corroboration-latent-asset-signals-crypto-trading-2026-09-04.md` (arXiv:2607.28446v1): CoLAS employs singular value maximization (SVM) spectral alignment and instance-wise regularization across static latent representations, whereas F2Agent designs an agentic system with four specialized LLM/Transformer agents, a dynamic modality-aware adaptive attention fusion module with learned modality priors ($r_m$), and an explicit noise-robust consistency regularization ($R_{\mathrm{rob}}$) enforcing logit consistency under random modality perturbation.
  - Distinct from `raml-regime-aware-multimodal-bitcoin-sentiment-fusion-2026-09-04.md` (arXiv:2607.23370v1): RAML uses an hourly dual-branch BiLSTM with a scalar volatility regime gate for 3h/6h Bitcoin direction forecasting, whereas F2Agent operates on daily multi-asset equity and crypto horizons with a multi-agent Transformer and LLM architecture.

## Economic mechanism

### Source-reported

Financial markets aggregate diverse and heterogeneous information sources, spanning quantitative historical price series to qualitative news and sentiment narratives (Fama, 1970; Feng et al., 2021). While both technical time-series patterns and textual narratives drive price formation, combining them naively faces severe structural challenges:
1. **Modality Gap and Textual Dominance:** Conventional LLM-based trading agents rely on prompt-level token concatenation (translating numerical tables into prompt text). This unstructured concatenation induces textual bias, drowning out subtle quantitative momentum, volatility, and volume signals.
2. **Noise and Transient Disconnects:** Financial text feeds are filled with speculative rumors, exaggerated headlines, and "sell-the-news" reversals (Tetlock, 2007), where positive sentiment masks an impending distribution phase. When agents process modalities in isolation or through shallow concatenation, they chase noisy sentiment traps.
3. **Information Asymmetry across Modalities:** Different modalities operate at varying signal-to-noise ratios. Quantitative OHLCV data reflects real capital allocation but suffers from non-stationary regimes, whereas unstructured news captures strategic catalysts and regime shifts but carries high semantic noise.

F2Agent resolves these issues by decoupling information extraction across a hierarchy of specialized agents (Market, Technical, News, Sentiment), mapping representations into an aligned latent space, and applying an adaptive attention fusion mechanism governed by learned modality priors and noise-robust consistency regularization.

### Research interpretation

The core hypothesis is that **modality-aware attention with learned modality priors and noise-robust consistency regularization** improves risk-adjusted trading returns over simple concatenation or single-modality models by dynamically modulating the relative weight of textual narratives versus quantitative price dynamics according to market context.

The economic intuition is that during periods of narrative-driven turbulence (e.g. speculative product rumors or regulatory headlines), the consistency regularizer suppresses excessive reliance on volatile or unconfirmed textual cues unless corroborated by technical volume and price structure. Conversely, when significant fundamental catalysts alter structural trends, the news agent's reasoning features break technical inertia. By formalizing modality-specific projection, learned modality priors, and attention suppression under perturbation, the system mitigates both textual hallucination and technical lag.

## Signal

The trading signal generation workflow operates as follows:

### 1. Hierarchy of Specialized Agents

The system deploys four distinct agents to extract modality representations for an asset $s$ at date $t$:
- **Market Analysis Agent ($f_{\mathrm{MA}}$):**
  - Input: Trailing $T$-day lookback window of OHLCV data:
    $$\mathbf{X}^{\mathrm{MA}}_{s,t} = [\mathbf{x}^{\mathrm{MA}}_{s,t-T}, \dots, \mathbf{x}^{\mathrm{MA}}_{s,t-1}] \in \mathbb{R}^{T \times F_{\mathrm{MA}}}$$
    containing Open, High, Low, Adjusted Close, and Volume.
  - Architecture: Causal Transformer encoder with $L_{\mathrm{MA}}$ masked self-attention blocks preventing look-ahead leakage.
  - Fixed-length summary: Extracted from the $[\text{CLS}]$ token representation $\mathbf{h}^{\mathrm{MA}}_{s,t} \in \mathbb{R}^{d_{\mathrm{MA}}}$.
- **Technical Analysis Agent ($f_{\mathrm{TA}}$):**
  - Input: Trailing $T$-day window of expression-based technical alpha factors:
    $$\mathbf{X}^{\mathrm{TA}}_{s,t} = [\mathbf{x}^{\mathrm{TA}}_{s,t-T}, \dots, \mathbf{x}^{\mathrm{TA}}_{s,t-1}] \in \mathbb{R}^{T \times F_{\mathrm{TA}}}$$
    including Moving Average Convergence Divergence (MACD), Relative Strength Index (RSI), Simple Moving Average (SMA), and Z-score Mean Reversion (ZMR).
  - Architecture: Causal Transformer encoder with $L_{\mathrm{TA}}$ masked self-attention blocks.
  - Fixed-length summary: $[\text{CLS}]$ token representation $\mathbf{h}^{\mathrm{TA}}_{s,t} \in \mathbb{R}^{d_{\mathrm{TA}}}$.
- **Sentiment Analysis Agent ($f_{\mathrm{SA}}$):**
  - Input: Daily news and social media items $\mathbf{X}^{\mathrm{SA}}_{s,t} = \{n_{s,t,1}, \dots, n_{s,t,K_{s,t}}\}$ filtered by a News Summarizer.
  - Model: DeepSeek-R1 (Distill-Llama-8B) generating binary sentiment polarity $\hat{c}_{s,t,j} \in \{0, 1\}$ and rationale $\hat{q}_{s,t,j}$.
  - Fixed-length summary: Last-token pooling over last-layer hidden states $\mathbf{u}_{s,t,j} = \mathbf{H}^{\mathrm{SA}}_{s,t,j}(L_{s,t,j})$, aggregated across daily items:
    $$\mathbf{h}^{\mathrm{SA}}_{s,t} = \frac{1}{K_{s,t}} \sum_{j=1}^{K_{s,t}} \mathbf{u}_{s,t,j} \in \mathbb{R}^{d_{\mathrm{SA}}}$$
- **News Analysis Agent ($f_{\mathrm{NA}}$):**
  - Input: Top-$K_{s,t}$ deduplicated news summaries $\mathbf{X}^{\mathrm{NA}}_{s,t}$ retrieved via semantic vector search from Alpaca and New York Times APIs.
  - Model: Qwen2.5-7B-Instruct fine-tuned in two stages (topic-focused QA and simulated market trading trajectories) with Chain-of-Thought (CoT) prompting to generate an auxiliary directional signal $\hat{c}^{\mathrm{NA}}_{s,t} \in \{\text{UP}, \text{DOWN}\}$, confidence score $\hat{p}^{\mathrm{NA}}_{s,t} \in [0, 1]$, and natural language explanation $\hat{e}^{\mathrm{NA}}_{s,t}$.
  - Objective during fine-tuning:
    $$\mathcal{L}_{\mathrm{ft}} = \mathcal{L}_{\mathrm{lm}}(\mathcal{P}, \mathcal{Y}) + \lambda \mathcal{L}_{\mathrm{cls}}(\mathbf{y}, \hat{\mathbf{y}})$$
  - Fixed-length summary: Last-token pooling over last-layer hidden states $\mathbf{h}^{\mathrm{NA}}_{s,t} \in \mathbb{R}^{d_{\mathrm{NA}}}$.

### 2. Modality Alignment and Adaptive Attention Fusion

- **Linear Projection to Shared Latent Space:**
  Each agent summary $\mathbf{h}_m(x) \in \mathbb{R}^{\tilde{d}_m}$ is projected into a shared $d$-dimensional space via learnable weight $\mathbf{P}_m \in \mathbb{R}^{d \times \tilde{d}_m}$:
  $$\mathbf{e}_m = \mathbf{P}_m \mathbf{h}_m(x) \in \mathbb{R}^d, \quad \forall m \in \{\mathrm{MA}, \mathrm{TA}, \mathrm{SA}, \mathrm{NA}\}$$
- **Queries, Keys, and Values:**
  $$\mathbf{Q}_m = \mathbf{e}_m \mathbf{W}_Q^{(m)}, \quad \mathbf{K}_m = \mathbf{e}_m \mathbf{W}_K^{(m)}, \quad \mathbf{V}_m = \mathbf{e}_m \mathbf{W}_V^{(m)}$$
  A concatenated joint query is formed: $\mathbf{Q}_{\mathrm{all}} = [\mathbf{Q}_1; \dots; \mathbf{Q}_M] \in \mathbb{R}^{M \cdot d_k}$.
- **Learned Modality Prior Injection ($M_P$):**
  To inject inductive modality-level biases beyond instance-level attention, a learnable modality vector $\mathbf{r}_m = \mathbf{u}_m \mathbf{A}$ is added to each modality key and value:
  $$\tilde{\mathbf{K}}_m = \mathbf{K}_m + \mathbf{r}_m, \quad \tilde{\mathbf{V}}_m = \mathbf{V}_m + \mathbf{r}_m$$
  where $\mathbf{A}$ is a shared projection matrix and $\mathbf{u}_m$ is the modality vector.
- **Attention Weight Computation:**
  $$\alpha_m = \mathrm{softmax}_m \left( \frac{\mathbf{Q}_{\mathrm{all}} \tilde{\mathbf{K}}_m^\top}{\sqrt{d}} \right)$$
  The fused representation is:
  $$\mathbf{R}_{\mathrm{final}} = \sum_{m=1}^M \alpha_m \tilde{\mathbf{V}}_m \in \mathbb{R}^d$$
- **Modality Diversity Regularization:**
  Pairwise $\ell_2$ repulsion prevents modality vectors from collapsing to identical representations:
  $$R_{\mathrm{mod}} = - \sum_{m \neq n} \|\mathbf{r}_m - \mathbf{r}_n\|_2^2$$

### 3. Noise-Robust Consistency Regularization ($M_R$)

To ensure stability against noisy, corrupted, or missing modalities:
- A modality $m^\star \in \{1, \dots, M\}$ is randomly selected and perturbed with Gaussian noise to yield perturbed embeddings $\{\mathbf{e}'_m\}$.
- Let $\mathbf{s}(x)$ and $\mathbf{s}(x')$ denote predicted class logits, and $\alpha_m$, $\alpha'_m$ denote attention weights for clean and perturbed inputs.
- The robustness regularizer penalizes logit discrepancy and suppresses attention allocation to the corrupted modality:
  $$R_{\mathrm{rob}} = \|\mathbf{s}(x) - \mathbf{s}(x')\|_2^2 + \gamma \max(0, \alpha'_{m^\star} - \alpha_{m^\star})^2$$
  where $\gamma > 0$ governs attention suppression.

### 4. Overall Training Objective

$$\mathcal{L}_{\mathrm{total}} = \mathcal{L}_{\mathrm{task}}(\hat{\mathbf{p}}(x), \mathbf{y}) + \lambda_{\mathrm{mod}} R_{\mathrm{mod}} + \lambda_{\mathrm{rob}} R_{\mathrm{rob}}$$
where $\mathcal{L}_{\mathrm{task}}$ is cross-entropy loss over binary movement label set $L = \{\text{UP}, \text{DOWN}\}$.

### 5. Execution Decision Rule

- Supervised label: $Y_t = 1$ if $p_t^{\mathrm{close}} \ge p_{t-1}^{\mathrm{close}}$, else $0$.
- Downstream trading policy: Long-or-flat trading rule:
  - If predicted class is $\text{UP}$ and currently flat: Execute $\text{BUY}$ at day $t+1$.
  - If predicted class is $\text{UP}$ and already long: $\text{HOLD}$.
  - If predicted class is $\text{DOWN}$ and currently long: Execute $\text{SELL}$ (full liquidation to cash) at day $t+1$.
  - If predicted class is $\text{DOWN}$ and currently flat: Maintain cash ($\text{HOLD}$).

## Required data

- **Instruments Evaluated in Source:**
  - Primary assets (6): Apple Inc. (AAPL), Amazon.com Inc. (AMZN), Alphabet Inc. (GOOG), Microsoft Corp. (MSFT), Tesla Inc. (TSLA), and Bitcoin spot (BTCUSD).
  - Extended assets (7): Grab Holdings (GRAB), Alibaba Group (BABA), The Coca-Cola Company (KO), Johnson & Johnson (JNJ), United Parcel Service (UPS), Upwork (UPWK), Sprouts Farmers Market (SFM).
- **Venues & Data Feeds:**
  - Market OHLCV: Yahoo Finance (\`yfinance\`) and Alpha Vantage API.
  - Financial & General News: Alpaca News API (ticker-annotated financial news) and New York Times API (general news retrieved via semantic vector search).
  - Sentiment Streams: FinHub API processed via DeepSeek-R1.
- **Market Type:** Spot equity and spot cryptocurrency.
- **Timeframe:** Daily bars ($1\text{D}$).
- **Input Fields:**
  - OHLCV: Open, High, Low, Adjusted Close, Volume.
  - Technical alpha factors: MACD line and signal, RSI (14-day), SMA, Z-score mean reversion indicator.
  - Textual fields: Daily news headline and body text, condensed to top 3 articles by impact rating.
- **Data Partitions (Strict Chronological Split):**
  - Training: 2023-10-01 to 2024-09-30 (12 months).
  - Validation: 2024-10-01 to 2025-03-31 (6 months).
  - Primary Test: 2025-04-01 to 2025-09-30 (6 months).
  - Extended Test: 2025-04-01 to 2026-03-20 (~12 months).
- **Hyperparameters:**
  - Lookback window: $T = 30$ trading days.
  - Batch size: 64; Optimizer: Adam ($\text{lr} = 2 \times 10^{-3}$); Maximum training epochs: 100 with early stopping (patience 10).
  - LLM inference: Generation temperature 0.5, repetition penalty 1.1.
  - Compute infrastructure: Six NVIDIA A40 GPUs.

## Execution assumptions

- **Execution Timing:** Low-frequency daily rebalance. A signal generated on day $t$ close is executed on day $t+1$, preventing same-bar look-ahead bias.
- **Order Model:** Market order execution assumed at the next-day price.
- **Position Sizing:** Discrete integer shares calculated as $\text{shares} = \lfloor \text{cash} / \text{price} \rfloor$, with unallocated residual held in cash.
- **Transaction Costs:** A uniform transaction fee of $0.003$ ($30\text{ bps}$) is deducted on every rebalance across all benchmark methods.
- **Shorting & Leverage:** Long-or-flat only (no short positions, no margin borrowing, no margin maintenance fees).
- **Execution Omissions:** No limit order book queue modeling, bid-ask spread crossing, slippage function, or market impact model. No perpetual funding fees modeled.

## Evidence

### Source-reported

All quantitative figures below trace directly to Changshuo Liu et al. (arXiv:2608.05668v1, Tables 1, 2, 3, 14, 16, 17, 18, and 19):

#### 1. Primary Evaluation Benchmark Results (Table 1)

Six-asset evaluation over the test period (2025-04-01 to 2025-09-30) under a uniform 30 bps transaction fee:

| Asset | Model Category | Selected Model | Annualized Return (ARR %) | Sharpe Ratio (SR) | Max Drawdown (MDD %) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AAPL** | Market | Buy & Hold | 27.95% | 0.61 | 22.99% |
| | Rule-based | ZMR | 15.79% | 0.96 | 4.06% |
| | ML/DL | Transformer | 32.90% | 0.72 | 13.77% |
| | Financial LLM | DeepFund | 33.83% | 0.74 | 15.86% |
| | Financial LLM | FinAgent | 33.77% | 0.90 | 13.16% |
| | **Ours** | **F2Agent** | **50.08%** | **1.22** | **7.83%** |
| **TSLA** | Market | Buy & Hold | 131.28% | 1.32 | 21.54% |
| | Financial LLM | FinAgent | 116.87% | 1.24 | 24.43% |
| | General LLM | GPT-5-mini | 105.17% | 1.55 | 19.44% |
| | **Ours** | **F2Agent** | **148.41%** | **1.94** | **12.60%** |
| **GOOG** | Market | Buy & Hold | 106.38% | 1.98 | 7.98% |
| | Financial LLM | FinAgent | 108.16% | 2.00 | 7.98% |
| | **Ours** | **F2Agent** | **120.48%** | **2.55** | **7.01%** |
| **MSFT** | Market | Buy & Hold | 70.52% | 1.76 | 8.03% |
| | Financial LLM | DeepFund | 80.60% | 2.07 | 5.94% |
| | **Ours** | **F2Agent** | **84.14%** | **2.08** | **8.03%** |
| **AMZN** | Market | Buy & Hold | 28.51% | 0.63 | 14.64% |
| | RL | PPO | 29.03% | 0.70 | 12.93% |
| | **Ours** | **F2Agent** | **40.87%** | **1.18** | **5.57%** |
| **BTCUSD** | Market | Buy & Hold | 43.76% | 1.27 | 11.70% |
| | Rule-based | MACD | 29.92% | 1.40 | 8.29% |
| | ML/DL | Transformer | 26.35% | 1.18 | 8.26% |
| | Financial LLM | FinAgent | 50.07% | 1.47 | 14.82% |
| | Financial LLM | TradingAgents | 38.96% | 1.37 | 8.74% |
| | Financial LLM | DeepFund | 8.05% | 0.38 | 16.11% |
| | **Ours** | **F2Agent** | **53.57%** | **1.52** | **9.79%** |

- **Cross-Asset Superiority:** F2Agent achieved an Average Rank of **1.00** in ARR across all six assets, compared to FinAgent (3.17), Buy & Hold (3.50), Transformer (7.00), and DeepFund (8.67).
- Relative ARR improvements over the best baseline: AAPL +48.03%, AMZN +40.79%, GOOG +11.39%, MSFT +4.39%, TSLA +13.05%, BTCUSD +6.99%.

#### 2. Component Ablation Study (Table 2)

Evaluating the impact of adaptive fusion ($M_F$), modality prior ($M_P$), and robustness regularizer ($M_R$):

| Asset | Variant | $M_F$ | $M_P$ | $M_R$ | ARR (%) | Sharpe (SR) | MDD (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **AAPL** | Concat. Fusion | ✗ | ✗ | ✗ | 19.21% | 0.33 | 22.99% |
| | w/o $M_P, M_R$ | ✓ | ✗ | ✗ | 27.28% | 0.57 | 22.99% |
| | w/o $M_R$ | ✓ | ✓ | ✗ | 34.77% | 0.86 | 8.46% |
| | w/o $M_P$ | ✓ | ✗ | ✓ | 38.04% | 0.80 | 10.69% |
| | **Full F2Agent** | **✓** | **✓** | **✓** | **50.08%** | **1.22** | **7.83%** |
| **BTCUSD** | Concat. Fusion | ✗ | ✗ | ✗ | 7.18% | 0.40 | 10.76% |
| | w/o $M_P, M_R$ | ✓ | ✗ | ✗ | 15.32% | 0.72 | 16.28% |
| | w/o $M_R$ | ✓ | ✓ | ✗ | 32.45% | 1.20 | 9.79% |
| | w/o $M_P$ | ✓ | ✗ | ✓ | 46.22% | 1.16 | 11.70% |
| | **Full F2Agent** | **✓** | **✓** | **✓** | **53.57%** | **1.52** | **9.79%** |

On BTCUSD, removing the adaptive fusion framework collapses ARR from 53.57% to 7.18% (a 46.39 percentage point loss) and Sharpe from 1.52 to 0.40.

#### 3. Modality Sensitivity and Robustness (Table 3)

Evaluating performance as modalities are progressively added ($N = \text{News}$, $M = \text{Market}$, $T = \text{Technical}$, $S = \text{Sentiment}$) on BTCUSD:
- News only ($N$): ARR 41.68%, SR 1.27, MDD 9.79%.
- News + Market ($N+M$): ARR 28.63%, SR 1.08, MDD 11.88%.
- News + Technical ($N+T$): ARR 22.00%, SR 1.04, MDD 8.48%.
- News + Sentiment ($N+S$): ARR 43.57%, SR 1.71, MDD 8.67%.
- News + Market + Technical ($N+M+T$): ARR 47.10%, SR 1.58, MDD 11.27%.
- Full Multimodal ($N+M+T+S$): ARR **53.57%**, SR **1.52**, MDD **9.79%**.
In contrast, FinAgent degrades on BTCUSD when integrating all modalities compared to single-modality configurations.

#### 4. Extended Horizon Evaluation (Table 14: 2025-04-01 to 2026-03-20)

Under prolonged market stress and regime shifts across 12 months:
- **AAPL:** F2Agent ARR **30.15%**, SR **1.02**, MDD 20.05% vs Buy & Hold ARR 12.00%, SR 0.36, MDD 22.99%.
- **GOOG:** F2Agent ARR **108.75%**, SR **2.88**, MDD **8.85%** vs Buy & Hold ARR 97.15%, SR 2.31, MDD 13.51%.
- **TSLA:** F2Agent ARR **78.49%**, SR **1.47**, MDD **15.32%** vs Buy & Hold ARR 43.49%, SR 0.65, MDD 22.37%.
- **BTCUSD:** F2Agent ARR **12.58%**, Cumulative Return **18.06%**, SR **0.84**, MDD **12.90%** vs Buy & Hold ARR **-12.32%**, CR **-16.78%**, SR **-0.38**, MDD **47.55%**.
F2Agent avoided the severe -16.78% drawdown regime in Bitcoin, improving ARR by 24.43 percentage points over the strongest alternative (TradingAgents ARR 10.11%).

#### 5. Random-Seed Robustness & Statistical Significance (Tables 16, 17, 18)

Across 3 random seeds (seeds 42, 43, 44):
- **AAPL ARR:** F2Agent $51.09\% \pm 4.09\%$ vs Transformer $31.20\% \pm 7.68\%$ vs Concat Fusion $14.64\% \pm 16.17\%$.
  - Paired t-test vs Transformer: $+19.89\%$ mean improvement, 95% CI $[9.33, 30.44]$, $p = 0.0149$ (statistically significant).
  - Paired t-test vs Concat Fusion: $+36.45\%$ mean improvement, 95% CI $[5.05, 67.84]$, $p = 0.0378$ (statistically significant).
- **BTCUSD ARR:** F2Agent $50.33\% \pm 3.80\%$ vs Transformer $28.80\% \pm 5.40\%$ vs Concat Fusion $8.40\% \pm 6.12\%$.
  - Paired t-test vs Concat Fusion: $+41.93\%$ mean improvement, 95% CI $[18.54, 65.33]$, $p = 0.0164$ (statistically significant).
  - Paired t-test vs Transformer: $+21.54\%$ mean improvement, 95% CI $[-0.81, 43.88]$, $p = 0.0535$ (marginal positive trend, not statistically significant at $\alpha = 0.05$).

#### 6. Stock Movement Directional Enhancement (Table 19)

Comparing binary prediction metrics with and without the Multi-agent Fusion (MaF) module:
- **AAPL:** Accuracy $53.02\% \to 57.94\%$, MCC $0.0431 \to 0.2122$.
- **AMZN:** Accuracy $50.30\% \to 55.56\%$, MCC $-0.0044 \to 0.1055$.
- **MSFT:** Accuracy $51.70\% \to 57.14\%$, MCC $0.0159 \to 0.1840$.
- **BTCUSD:** Accuracy $51.67\% \to 53.55\%$, MCC $0.0261 \to 0.0599$.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Marginal Statistical Significance on BTCUSD:** While F2Agent significantly outperforms Concat Fusion ($p = 0.0164$), its outperformance against a purely quantitative causal Transformer on BTCUSD yields $p = 0.0535$ (95% CI includes $-0.81\%$). In crypto markets, quantitative price sequences capture substantial momentum information that limits the marginal statistical edge of LLM agents at daily frequency.
- **Modest Directional Classification Edge on Bitcoin:** On BTCUSD, directional accuracy is only $53.55\%$ and MCC is $0.0599$ (Table 19). Although better than the un-fused baseline ($51.67\%$ ACC, $0.0261$ MCC), this thin statistical edge leaves limited room for transaction cost slippage in live trading.
- **Sub-Modality Instability:** On BTCUSD (Table 3), combining News + Technical indicators yields an ARR of only $22.00\%$ (lower than News alone at $41.68\%$), demonstrating that conflicting technical and fundamental signals can induce noise unless full multimodal regularization is active.
- **Heavy Compute Footprint:** Training requires 6 NVIDIA A40 GPUs, and inference utilizes DeepSeek-R1 and Qwen2.5-7B-Instruct, creating computational latency and deployment costs that rule out sub-minute execution.

## Falsification plan

1. **Exchange Fee & Slippage Stress Test:** Re-evaluate F2Agent signals on BTCUSDT perpetual contracts using Binance VIP0 trading costs (4 bps taker fee + 1.5 bps average half-spread + market impact model). **Failure threshold:** Net Sharpe ratio $\le 0.0$ or net annualized return underperforming Buy & Hold BTC over the 2025–2026 test window.
2. **Placebo / Shuffled News Narrative Test:** Break temporal alignment by randomly shuffling the daily news summaries and sentiment scores across dates while leaving OHLCV and technical sequences unchanged. **Failure threshold:** If the model trained on shuffled text achieves $\ge 90\%$ of the ARR or Sharpe ratio of the true model, the hypothesis that textual agentic reasoning provides exploitable alpha is falsified as spurious representation fitting.
3. **Out-of-Sample Walk-Forward Extension (2026 Q2–Q4):** Apply frozen F2Agent weights to fresh out-of-sample data collected between April 2026 and December 2026. **Failure threshold:** Out-of-sample directional MCC $\le 0.01$ or cumulative return $< 0.0\%$.
4. **Cross-Asset Altcoin Generalization Test:** Test F2Agent on high-beta liquid cryptocurrencies (ETHUSDT, SOLUSDT, DOGEUSDT) using the identical architecture. **Failure threshold:** If average ARR across altcoins falls below zero or MDD exceeds $35\%$, the claim of generalizable multimodal robustness in digital assets is falsified.
5. **Inference Latency & Fill Quality Test:** Evaluate execution delay induced by running the multi-agent LLM pipeline (retrieval + DeepSeek-R1 summarization + Qwen2.5-7B inference) against live order books. **Failure threshold:** Execution delay exceeding 3 minutes resulting in $> 20\text{ bps}$ average adverse price slippage at market open.

## Crypto portability

**Adapted (Demonstrated in Spot Crypto; Unproven in Derivatives)**

The primary paper evaluates F2Agent directly on spot Bitcoin (`BTCUSD`) alongside US equities. However, deploying the framework in production crypto systems requires addressing key structural differences:
- **Perpetual Swap Funding Frictions:** The paper implements a long-or-flat cash spot model. In crypto derivatives markets, holding long exposure during bull markets incurs 8-hour funding rate payments to shorts. A daily strategy holding positions through multi-week runups must incorporate funding yield drag.
- **24/7 Continuous Trading vs Daily Equity Closes:** US equities have discrete overnight sessions and fixed 16:00 EST closes, giving news summarizers a clear cutoff window. Crypto markets operate continuously 24/7; fixing a daily boundary (e.g. 00:00 UTC) risks missing intraday narrative shifts that unfold during Asian or European sessions.
- **Social Discourse Dispersion:** Equity news is concentrated in regulated filings and established outlets (Alpaca, NYT). Crypto sentiment is heavily driven by decentralized platforms (Twitter/X, Telegram, Discord, Reddit) and on-chain protocol alerts, which are not captured by mainstream financial APIs.
- **Liquidity Fragmentation & Mark Price Disconnects:** Spot BTC prices from Yahoo Finance obscure the fragmentation across Binance, OKX, Bybit, and Coinbase, where liquidation cascades and order book depth variations dominate short-term execution.

## Limitations

- **Not Independently Reproduced:** All performance metrics originate from the primary publication and have not been replicated on independent infrastructure.
- **Data & Execution Gaps:** No order book microstructure, bid-ask spreads, slippage curves, or borrow costs are modeled. The 30 bps flat fee does not capture adverse selection during volatile breakout bars.
- **Small Sample Horizon:** The primary test period covers only 6 months (April–September 2025), with an extended test of 12 months. This limited sample spans primarily bull and consolidation regimes.
- **Long-or-Flat Execution Constraint:** The backtesting engine only executes long or cash positions. It fails to exploit downward alpha through short selling, discarding half the theoretical information content of the binary prediction.
- **High Resource Requirements:** Generating daily trading signals requires querying multiple external news APIs, running semantic embeddings, and prompting two large language models (DeepSeek-R1 and Qwen2.5-7B), creating significant operational overhead.

## Implementation status

`not-implemented`. Research capture only. No components of the F2Agent architecture, modality encoders, or backtesting logic have been implemented in NautilusTrader, PyBroker, paper trading, or live execution systems.

## Adoption boundary

`research-only`. `adoption: not-approved`. `approval_scope: research-only`. A record in this repository serves strictly as normalized research material and does not constitute authorization for live capital allocation, strategy deployment, or paper trading.

## Related Wiki records

- `[[colas-multimodal-corroboration-latent-asset-signals-crypto-trading-2026-09-04]]`: Multimodal corroboration across price, news, indicators, and sentiment for daily crypto and equity returns using singular value maximization spectral alignment.
- `[[raml-regime-aware-multimodal-bitcoin-sentiment-fusion-2026-09-04]]`: Volatility-regime gated adaptive fusion between technical OHLCV sequences and FinBERT Reddit sentiment on intraday Bitcoin horizons.
- `[[tradingmoe-query-key-sparse-expert-routing-llm-trading-2026-09-03]]`: Sparse Mixture-of-Experts routing for financial trading using market context queries.
- `[[finsmart-market-aligned-reinforcement-learning-sentiment-alpha-2026-09-02]]`: Financial sentiment analysis for algorithmic trading via market-aligned reinforcement learning.
- `[[retrieval-augmented-llm-expert-switching-portfolio-management-2026-09-03]]`: Retrieval-augmented LLM expert switching across macro regimes.

## Sources

- Changshuo Liu, Yanzheng Jin, Shangfeng Cai, Peng Fang, Xiaokui Xiao, and Beng Chin Ooi, "F$^2$Agent: Financial Fusion of Agentic Intelligence for Multimodal Trading," arXiv:2608.05668v1 [cs.MA], submitted August 7, 2026. Canonical URL: https://arxiv.org/abs/2608.05668. Full text HTML: https://arxiv.org/html/2608.05668v1.
- E. F. Fama, "Efficient capital markets: A review of theory and empirical work," *The Journal of Finance*, vol. 25, no. 2, pp. 383–417, 1970.
- P. C. Tetlock, "Giving content to investor sentiment: The role of media in the stock market," *The Journal of Finance*, vol. 62, no. 3, pp. 1139–1168, 2007.
- F. Feng, M. Li, C. Luo, R. Ng, and T.-S. Chua, "Hybrid learning to rank for financial event ranking," in *Proc. 44th International ACM SIGIR Conf. Research and Development in Information Retrieval*, 2021, pp. 233–243.
- R. Cont, "Empirical properties of asset returns: Stylized facts and statistical issues," *Quantitative Finance*, vol. 1, no. 2, pp. 223–236, 2001.
- Z. Kakushadze, "101 formulaic alphas," *Wilmott*, vol. 2016, no. 84, pp. 72–81, 2016.
- G. Zerveas, S. Jayaraman, D. Patel, A. Bhamidipaty, and C. Eickhoff, "A transformer-based framework for multivariate time series representation learning," in *Proc. 27th ACM SIGKDD Conf. Knowledge Discovery & Data Mining*, 2021, pp. 2114–2124.
- D. Guo et al., "DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning," arXiv:2501.12948, 2025.
- Qwen Team, "Qwen2 technical report," arXiv:2407.10671, 2024.
- W. Zhang et al., "A multimodal foundation agent for financial trading: Tool-augmented, diversified, and generalist," in *Proc. 30th ACM SIGKDD Conf. Knowledge Discovery and Data Mining*, 2024, pp. 4314–4325.
- Y. Xiao, E. Sun, D. Luo, and W. Wang, "TradingAgents: Multi-agents LLM financial trading framework," arXiv:2412.20138, 2024.
- Y. Yu et al., "FinMEM: A performance-enhanced LLM trading agent with layered memory and character design," *IEEE Transactions on Big Data*, 2025.
