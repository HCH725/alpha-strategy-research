---
schema: strategy-research-record-v1
title: RAML Regime-Aware Multi-Modal Fusion of Social Sentiment and Technical Features for Bitcoin Direction Prediction
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - multimodal
  - sentiment
  - machine-learning
status: research-only
confidence: medium
source_as_of: "2026-07-25"
sources:
  - "Muhammad Abdullah Haroon, 'Bitcoin Price Direction Prediction via Regime-Aware Multi-Modal Fusion of Social Sentiment and Technical Features', arXiv:2607.23370v1 [cs.LG], July 25, 2026. https://arxiv.org/abs/2607.23370"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RAML: Regime-Aware Multi-Modal Fusion of Social Sentiment and Technical Features for Bitcoin Direction Prediction

## Provenance

- **Primary Source:** Muhammad Abdullah Haroon (Department of Computer Science, FAST-NUCES, Lahore, Pakistan), "Bitcoin Price Direction Prediction via Regime-Aware Multi-Modal Fusion of Social Sentiment and Technical Features," arXiv:2607.23370v1 [cs.LG], submitted July 25, 2026.
- **Canonical arXiv URL:** https://arxiv.org/abs/2607.23370
- **Canonical HTML URL:** https://arxiv.org/html/2607.23370
- **Source Data As-Of:** 14-month hourly dataset spanning July 2024 to September 2025 (3,491 aligned hourly observations). Chronological partition: training window July 2024 – June 2025 (2,146 observations); out-of-distribution test window July 2025 – September 2025 (1,345 observations).
- **Pre-Write Deduplication Audit:** A repository-wide regex and string search for `arXiv:2607.23370`, `RAML`, `Regime-Aware Multi-Modal Learning`, and author `Haroon` found zero existing records. Related repository records examine multimodal fusion on daily horizons (`colas-multimodal-corroboration-latent-asset-signals-crypto-trading-2026-09-04.md`), reinforcement learning futures routing (`fineft-risk-aware-ensemble-rl-vae-routing-crypto-futures-2026-09-03.md`), and macro sentiment EMA contrarian models (`crypto-macro-sentiment-contrarian-fear-greed-ema-2026-09-03.md`). None investigate the volatility-regime gated adaptive fusion mechanism between technical OHLCV sequences and FinBERT Reddit sentiment on sub-daily (3h and 6h) horizons.

## Economic mechanism

### Source-reported

In cryptocurrency markets, social discourse on platforms such as Reddit (/r/Bitcoin) and Twitter carries Granger-causal predictive information for near-term price direction, consistent with noise-trader theory (DeLong et al., 1990): retail investors form herds, propagate emotional sentiment through social networks, and exert directional pressure before institutional arbitrage can correct the dislocation. However, the informativeness of crowd sentiment is fundamentally non-stationary and regime-dependent (Baker & Wurgler, 2007; Tetlock, 2007). During calm, trending periods governed by institutional order flow or technical momentum, crowd sentiment contains high noise and minimal predictive signal. Conversely, during high-volatility, crash, or speculative breakout episodes, retail crowd emotion surges and becomes highly predictive of short-term market trajectory.

Conventional machine-learning approaches combine technical OHLCV features and sentiment metrics via static feature concatenation. This static approach applies identical implicit weights across all market conditions, diluting technical signals with sentiment noise during calm regimes and under-weighting crowd sentiment during market stress.

### Research interpretation

The core hypothesis is that an adaptive, regime-conditioned gate that dynamically modulates the weight of social sentiment embeddings relative to technical price embeddings based on rolling 24-hour return volatility will improve directional calibration and prevent majority-class collapse on intraday horizons (3-hour and 6-hour forward).

The economic intuition is that volatility acts as an observable state proxy for noise-trader activity and market uncertainty. When rolling volatility exceeds its historical median ($r_t = 1$), the learnable gate $w_t = \sigma(\theta_r \cdot r_t)$ shifts weight toward the sentiment embedding ($w_t > 0.5$ when $\theta_r > 0$). When volatility is low ($r_t = 0$), the gate evaluates to $w_t = \sigma(0) = 0.5$, allowing the structured technical price embedding to dominate classification. By parameterising the gate with a single scalar $\theta_r$ trained end-to-end via backpropagation, the model learns the optimal balance between modalities without overfitting or requiring separate models for each regime.

## Signal

- **Signal Formation Timestamp:** Formed at each UTC hour boundary $t$ using the trailing 24-hour window $[t-23, t]$. Output signal is evaluated for trading at the close of hour $t$.
- **Lookback Windows:**
  - Input sequence length: $L = 24$ hours for both price and sentiment branches.
  - Rolling volatility window: 24 hours of hourly log-returns ($r_t = \frac{c_t - c_{t-1}}{c_{t-1}}$).
  - Relative Strength Index (RSI): 14 hours with exponential weighting.
  - Moving averages: 7-hour ($MA^{(7)}$) and 30-hour ($MA^{(30)}$) simple moving averages.
- **Price Branch Architecture:**
  - Input: 10-dimensional feature vector $\mathbf{x}^{(p)}_t = [\text{open}, \text{high}, \text{low}, \text{close}, \text{volume}, r_t, \sigma_t, \text{RSI}_t, \text{MA}^{(7)}_t, \text{MA}^{(30)}_t]^\top \in \mathbb{R}^{10}$.
  - Encoder: 2-layer Bidirectional LSTM (BiLSTM) with hidden dimension $d=64$ per direction (concatenated representation $\mathbf{h}^{(p)}_t \in \mathbb{R}^{128}$). Dropout $p_d = 0.3$ between layers.
  - Projection: Compact 32-dimensional price embedding $\mathbf{e}^{(p)}_t = \text{ReLU}(\mathbf{W}_p \mathbf{h}^{(p)}_t + \mathbf{b}_p) \in \mathbb{R}^{32}$.
- **Sentiment Branch Architecture:**
  - Input: 5-dimensional feature vector $\mathbf{x}^{(s)}_t = [\bar{f}_t, \bar{b}^+_t, \bar{b}^-_t, \bar{s}_t, n_t]^\top \in \mathbb{R}^{5}$, comprising mean FinBERT composite score, mean bullish probability, mean bearish probability, mean sentiment strength, and post count per hour.
  - Encoder: Symmetric 2-layer BiLSTM ($d=64$, output $\mathbf{h}^{(s)}_t \in \mathbb{R}^{128}$), dropout $p_d = 0.3$.
  - Projection: 32-dimensional sentiment embedding $\mathbf{e}^{(s)}_t = \text{ReLU}(\mathbf{W}_s \mathbf{h}^{(s)}_t + \mathbf{b}_s) \in \mathbb{R}^{32}$.
- **Regime Detection & Adaptive Gating:**
  - Rolling volatility calculation: $\sigma_t = \sqrt{\frac{1}{24}\sum_{k=0}^{23}(r_{t-k} - \bar{r}_t)^2}$.
  - Binary regime label: $r_t = 1$ if $\sigma_t > \text{median}(\boldsymbol{\sigma})$, else $0$.
  - Learnable adaptive gate weight: $w_t = \sigma(\theta_r \cdot r_t)$, where $\theta_r \in \mathbb{R}$ is a single learnable scalar parameter.
  - Fused embedding: $\mathbf{e}^{(\text{fused})}_t = w_t \cdot \mathbf{e}^{(s)}_t + (1 - w_t) \cdot \mathbf{e}^{(p)}_t \in \mathbb{R}^{32}$.
- **Classification Head:**
  - Two-layer feedforward network: $\hat{y}_t = \sigma(\mathbf{w}_2^\top \text{ReLU}(\mathbf{W}_1 \mathbf{e}^{(\text{fused})}_t + \mathbf{b}_1) + b_2)$, where $\mathbf{W}_1 \in \mathbb{R}^{16 \times 32}$, $\mathbf{w}_2 \in \mathbb{R}^{16}$, $b_2 \in \mathbb{R}$.
  - Objective: Binary cross-entropy $\mathcal{L} = -\frac{1}{N}\sum_{t=1}^N [y_t \log \hat{y}_t + (1 - y_t) \log(1 - \hat{y}_t)]$.
- **Directional Decision Rule:**
  - Long signal (Up): $\hat{y}_t > 0.50$.
  - Neutral / Short signal (Down): $\hat{y}_t \le 0.50$.
- **Holding Period & Prediction Horizon:** Evaluated at two distinct forward horizons: $h = 3$ hours and $h = 6$ hours ($y^{(h)}_t = 1$ if $c_{t+h} > c_t$, else $0$). Positions are re-evaluated hourly.
- **Training Hyperparameters:** Sequence length $L=24$, batch size 32, Adam optimizer, learning rate $1 \times 10^{-3}$, 30 training epochs. Total trainable parameters $\approx 218,000$.

## Required data

- **Instrument:** BTC-USD (Bitcoin spot vs US Dollar).
- **Universe:** Single asset (Bitcoin).
- **Venue:** Market data retrieved via Yahoo Finance (`yfinance`); social sentiment retrieved from Reddit (/r/Bitcoin and adjacent cryptocurrency subreddits via PRAW API) processed through `ProsusAI/FinBERT`.
- **Market Type:** Spot cryptocurrency.
- **Timeframe:** Hourly bars ($1\text{h}$).
- **Fields:**
  - Market OHLCV: Open, High, Low, Close, Volume.
  - Derived technicals: Hourly log-return $r_t$, 24h rolling volatility $\sigma_t$, 14-period RSI, 7-hour SMA, 30-hour SMA.
  - Social sentiment: FinBERT composite score, bullish probability, bearish probability, sentiment strength, hourly post count.
- **Point-in-Time & Splits:**
  - Strict chronological non-overlapping split: Training set July 2024 – June 2025 (2,146 observations); held-out test set July 2025 – September 2025 (1,345 observations).
  - No random shuffling or lookahead leakage.
  - Target labels strictly offset by $h \in \{3, 6\}$ hours into the future.
- **Timestamp Alignment:** UTC timestamp matching on hourly boundaries via inner join across sources.
- **Missing Data Handling:** Rolling window initialisation periods dropped; missing hours from sentiment or market feeds omitted via inner join (effective dataset contains 3,491 aligned hours).
- **Cost/Funding Fields:** None modeled in the primary research source.

## Execution assumptions

- **Execution Timing:** Assumed instantaneous fill at the hourly bar close upon model inference.
- **Order Type:** Market order assumed implicitly; no limit order book queuing or slippage model.
- **Frictions & Costs:** The primary paper reports classification accuracy, F1, and ROC-AUC exclusively. No transaction fees (e.g. Binance 2–5 bps maker/taker), bid-ask spreads, or slippage are subtracted.
- **Funding & Borrow:** Spot trading assumed; no perpetual swap funding rates or margin borrow fees considered.
- **Capacity & Turnover:** Rebalancing occurs hourly across 3-hour or 6-hour holding windows. At high turnover, transaction costs represent the primary operational bottleneck.

## Evidence

### Source-reported

All empirical figures below trace directly to Muhammad Abdullah Haroon (arXiv:2607.23370v1, Tables II, IV, and V):

- **Dataset Characteristics (Table II):** Total observations: 3,491 hours (July 2024 – September 2025). Training rows: 2,146 (61.5%); Test rows: 1,345 (38.5%). Label balance in test set: 3-hour horizon: 51.6% Up / 48.4% Down; 6-hour horizon: 52.1% Up / 47.9% Down. Test set regime distribution: 59.4% volatile, 40.6% stable.
- **Baseline Model Comparison (Table IV):**
  - **3-Hour Prediction Horizon:**
    - B1 (Price-only BiLSTM): Accuracy 0.4883, Precision 0.4991, Recall 0.4044, F1 0.4468, AUC 0.4968.
    - B2 (Sentiment-only FF): Accuracy 0.5190, Precision 0.5162, Recall 0.9067, F1 0.6579, AUC 0.4938. (High F1 is degenerate: recall is 0.9067 but AUC < 0.50, indicating inverted probability ranking).
    - B3 (Static Concatenation BiLSTM): Accuracy 0.5019, Precision 0.5172, Recall 0.3778, F1 0.4366, AUC 0.4939.
    - **RAML (Proposed Architecture):** Accuracy 0.5117, Precision 0.5200, Recall 0.5778, **F1 0.5474**, **AUC 0.5084**. (RAML is the only model achieving AUC > 0.50 and balanced recall on the 3-hour task).
  - **6-Hour Prediction Horizon:**
    - B1 (Price-only BiLSTM): Accuracy 0.4852, Precision 0.5339, Recall 0.0916, F1 0.1563, AUC 0.5210. (Exhibits severe recall collapse to 0.0916).
    - B2 (Sentiment-only FF): Accuracy 0.5123, Precision 0.5271, Recall 0.6501, F1 0.5822, AUC 0.5170.
    - B3 (Static Concatenation BiLSTM): Accuracy 0.5284, Precision 0.5316, Recall 0.6489, F1 0.5844, AUC 0.5253.
    - **RAML (Proposed Architecture):** Accuracy 0.4837, Precision 0.5036, Recall 0.6090, **F1 0.5513**, AUC 0.4902.
- **Ablation Study (Table V):**
  - **3-Hour Horizon:**
    - RAML (Full Model): Acc 0.5117, Prec 0.5200, Rec 0.5778, F1 0.5474, AUC 0.5084.
    - A1 (No Sentiment Branch): Acc 0.4580, Prec 0.4666, Rec 0.4237, F1 0.4441, AUC 0.4766 ($\Delta \text{F1} = -0.1033$, $\Delta \text{AUC} = -0.0318$).
    - A2 (No Regime Gate, fixed equal weighting $w_t=0.5$): Acc 0.5011, Prec 0.5076, Rec 0.7896, F1 0.6180, AUC 0.4841. (Higher F1 is an artifact of degenerate high recall; AUC drops to 0.4841).
    - A3 (No Fusion Weighting, direct concatenation of 32d embeddings): Acc 0.4966, Prec 0.5048, Rec 0.7822, F1 0.6136, AUC 0.4797.
  - **6-Hour Horizon:**
    - RAML (Full Model): Acc 0.4837, Prec 0.5036, Rec 0.6090, F1 0.5513, AUC 0.4902.
    - A1 (No Sentiment Branch): Acc 0.4875, Prec 0.5188, Rec 0.2209, F1 0.3099, AUC 0.4721 ($\Delta \text{F1} = -0.2414$).
    - A2 (No Regime Gate): Acc 0.4739, Prec 0.4916, Rec 0.2965, F1 0.3699, AUC 0.4799 ($\Delta \text{F1} = -0.1814$).
    - A3 (No Fusion Weighting): Acc 0.4777, Prec 0.4914, Rec 0.0828, F1 0.1418, AUC 0.4608 (Catastrophic collapse: recall drops to 0.0828, $\Delta \text{F1} = -0.4095$).
- **Component Contribution Summary:** Removing adaptive fusion weighting causes catastrophic failure on the 6h task ($\Delta \text{F1} = -0.4095$); removing sentiment degrades F1 across both horizons ($\Delta \text{F1}_{3h} = -0.1033$, $\Delta \text{F1}_{6h} = -0.2414$); removing regime gating degrades AUC below random ($\Delta \text{AUC} = -0.0243$ at 3h).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- On the 6-hour horizon, RAML's AUC drops to 0.4902 (below random walk 0.50), indicating that while it prevents recall collapse (F1: 0.5513), its probability ranking is miscalibrated at longer intraday horizons.
- Static concatenation (B3) outperforms RAML on the 6-hour horizon in raw Accuracy (0.5284 vs 0.4837) and AUC (0.5253 vs 0.4902), showing that simple volatility gating does not uniformly dominate across all holding horizons.
- Asymmetry in directional error: The full RAML model exhibits poor specificity on downward price movements (specificity 44.6%, correctly identifying only 294 of 659 down hours in the test set).
- Modest absolute edge: AUC of 0.5084 and accuracy of 51.17% on 3h indicate a very thin statistical edge that would likely be fully eroded under realistic exchange taker fees (e.g., 2–5 bps per trade) and hourly turnover.

## Falsification plan

1. **Transaction Friction & Fee Stress Test:** Simulate an hourly rebalanced execution strategy with realistic Binance BTCUSDT perpetual trading fees (4 bps taker fee + 1 bp slippage round trip). **Failure threshold:** Net Sharpe ratio $\le 0.0$ or net annualized return underperforming buy-and-hold BTC over the test period.
2. **Temporal Out-of-Sample Validation:** Re-evaluate the frozen RAML architecture on out-of-sample hourly Bitcoin data from October 2025 through August 2026. **Failure threshold:** Out-of-sample AUC $< 0.500$ and directional accuracy $< 50.0\%$.
3. **Placebo / Shuffled Sentiment Test:** Break the temporal alignment of the Reddit sentiment stream by randomly permuting sentiment rows while keeping price OHLCV intact. **Failure threshold:** If the shuffled-sentiment model achieves comparable or superior AUC/F1 to the original model, the claimed sentiment-driven economic mechanism is falsified.
4. **Continuous Volatility / GARCH Benchmark:** Replace the binary median-split volatility gate with a continuous volatility scalar or an EGARCH conditional volatility proxy. **Failure threshold:** If the binary gate fails to match or exceed the performance of a standard continuous volatility control, the binary thresholding mechanism is falsified as sub-optimal.
5. **Cross-Asset Generalization Test:** Train and evaluate the RAML architecture on ETH-USD and SOL-USD using the identical protocol. **Failure threshold:** If RAML experiences recall collapse ($< 0.20$) or AUC $< 0.490$ across altcoins, the mechanism is falsified as a generalizable crypto alpha.

## Crypto portability

**Direct (Demonstrated in Crypto)**

The paper is explicitly designed for and tested on Bitcoin (BTC-USD). However, portability into an operational trading framework requires addressing several crypto-specific frictions:

- **Spot vs Perpetual Swaps:** The paper evaluates spot BTC-USD. In crypto perpetuals, 8-hour funding rates must be factored into the holding cost of 3h and 6h positions.
- **24/7 Market vs Diurnal Social Attention:** Bitcoin trades continuously 24/7, but Reddit social media volume displays strong diurnal patterns tied to US daylight hours. During Asian and European trading sessions, Reddit post counts drop significantly, introducing temporal sparsity in the sentiment branch.
- **Execution Venue Fragmentation:** Sourcing data from yfinance aggregates across various price feeds. In live crypto trading, execution occurs on centralized exchange order books (Binance, Bybit, OKX) where microstructural spread, order book depth, and queue priority govern fill quality.

## Limitations

- **Small Effective Sample:** Only 3,491 hourly observations total (14 months), with 2,146 in training. This constrained sample size limits the representation learning capacity of the dual-branch BiLSTM.
- **Single-Asset Scope:** Validated only on BTC-USD; no multi-asset or cross-sectional validation was performed.
- **Absence of Transaction Costs:** All reported metrics are pure classification scores. With hourly rebalancing, realistic transaction costs would severely impact practical viability.
- **Coarse Binary Regime Classification:** Splitting volatility by a global dataset median provides a crude binary signal that ignores trending vs mean-reverting states, structural volatility shifts, or multi-regime dynamics.
- **Intra-Hour Post Aggregation:** The arithmetic mean of FinBERT scores discards the arrival timing of posts within each hour.

## Implementation status

`not-implemented`. Research capture only. No model weights, data ingestion pipelines, or execution logic have been integrated into NautilusTrader, PyBroker, paper trading, or live trading systems.

## Adoption boundary

`research-only`. `adoption: not-approved`. `approval_scope: research-only`. A record being present in this repository does not imply statistical significance under transaction costs, execution feasibility, or approval for live capital deployment.

## Related Wiki records

- `[[colas-multimodal-corroboration-latent-asset-signals-crypto-trading-2026-09-04]]`: Multimodal corroboration across price, news, indicators, and sentiment for daily crypto and equity returns using spectral alignment.
- `[[fineft-risk-aware-ensemble-rl-vae-routing-crypto-futures-2026-09-03]]`: Risk-aware ensemble reinforcement learning and VAE routing for crypto futures.
- `[[crypto-macro-sentiment-contrarian-fear-greed-ema-2026-09-03]]`: Contrarian crypto macro sentiment using daily Fear & Greed index.
- `[[tda-persistent-homology-finbert-sentiment-portfolio-optimization-2026-09-02]]`: Topological data analysis and FinBERT sentiment for equity portfolio construction.
- `[[bitcoin-rolling-fpca-hourly-return-direction-2026-09-03]]`: Functional PCA for hourly Bitcoin directional return forecasting.

## Sources

- Muhammad Abdullah Haroon, "Bitcoin Price Direction Prediction via Regime-Aware Multi-Modal Fusion of Social Sentiment and Technical Features," arXiv:2607.23370v1 [cs.LG], submitted July 25, 2026. Canonical URL: https://arxiv.org/abs/2607.23370. Full text HTML: https://arxiv.org/html/2607.23370.
- J. B. DeLong, A. Shleifer, L. H. Summers, and R. J. Waldmann, "Noise trader risk in financial markets," *Journal of Political Economy*, vol. 98, no. 4, pp. 703–738, 1990.
- M. Baker and J. Wurgler, "Investor sentiment in the stock market," *Journal of Economic Perspectives*, vol. 21, no. 2, pp. 129–151, 2007.
- P. C. Tetlock, "Giving content to investor sentiment: The role of media in the stock market," *The Journal of Finance*, vol. 62, no. 3, pp. 1139–1168, 2007.
- Y. Liu, "FinBERT: A pre-trained financial language representation model for financial text mining," arXiv:1908.10063, 2019.
- S. McNally, J. Roche, and S. Caton, "Predicting the price of Bitcoin using machine learning," in *Proc. 26th Euromicro Int. Conf. Parallel, Distributed and Network-based Processing*, Cambridge, UK, 2018, pp. 339–343.
- J. Abraham, D. Higdon, J. Nelson, and J. Ibarra, "Cryptocurrency price prediction using tweet volumes and sentiment analysis," *SMU Data Science Review*, vol. 1, no. 3, 2018.
- A. Urquhart, "The inefficiency of Bitcoin," *Economics Letters*, vol. 148, pp. 80–82, 2016.
