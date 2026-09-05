---
schema: strategy-research-record-v1
title: "ISEPT: Image-Based Selection and Execution Framework for Pair Trading (Kim et al. 2025)"
created: 2026-09-06
updated: 2026-09-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - pairs-trading
  - convolutional-autoencoder
  - computer-vision
  - candlestick-images
  - multi-layer-perceptron
  - feedback-loop
status: research-only
confidence: medium
source_as_of: 2025-11-18
sources:
  - "Nayoung Kim, Jangwook Lee, and Yuncheol Kang. 'ISEPT: Image-Based Selection and Execution Framework for Pair Trading'. In Proceedings of the 6th ACM International Conference on AI in Finance (ICAIF '25), November 15–18, 2025, Singapore, pages 413–421. ACM, New York, NY, USA. DOI: 10.1145/3768292.3770346."
  - "Nayoung Kim (dudskrla). Official source code repository: dudskrla/ISEPT, commit 4533320eda07c135c3aed305dc175926bad5ea1d (code implementation commit c2dff16623c58690bdf70cfe625ad6f8fa2ae142), November 2025. https://github.com/dudskrla/ISEPT"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ISEPT: Image-Based Selection and Execution Framework for Pair Trading

## Provenance

- **Primary Source Authors:** Nayoung Kim, Jangwook Lee, and Yuncheol Kang (Department of Industrial and Systems Engineering, Ewha Womans University, Seoul, Republic of Korea).
- **Paper Title:** *"ISEPT: Image-Based Selection and Execution Framework for Pair Trading"*
- **Publication Venue:** *Proceedings of the 6th ACM International Conference on AI in Finance (ICAIF '25)*, November 15–18, 2025, Singapore, pages 413–421.
- **Permanent Digital Object Identifier (DOI):** [10.1145/3768292.3770346](https://doi.org/10.1145/3768292.3770346)
- **Primary Source Code Repository:**
  - GitHub: [https://github.com/dudskrla/ISEPT](https://github.com/dudskrla/ISEPT)
  - Canonical Head Commit SHA: `4533320eda07c135c3aed305dc175926bad5ea1d`
  - Implementation Tree Commit SHA: `c2dff16623c58690bdf70cfe625ad6f8fa2ae142`
  - Exact file paths inspected: `README.md`, `main_ours_gatev.py`, `main_ours_vidyamurthy.py`, `mlp.py`, `average_results.ipynb`, `MODEL/model_utils/CAE.py`, `MODEL/model_utils/MLP.py`, `MODEL/model_utils/Pair_Trading.py`, and `MODEL/model_utils/Image_CAE.py`.
- **Primary Source Verification:** The complete public source implementation, model architectures, hyperparameter dictionaries, image generation pipelines, loss formulations, and backtesting simulation code were directly read and verified from the official author repository (`dudskrla/ISEPT`).
- **Repository Deduplication Audit:** A full-text grep audit across `alpha-strategy-research` confirmed zero pre-existing records referencing `ISEPT`, DOI `10.1145/3768292.3770346`, authors Nayoung Kim, Jangwook Lee, or Yuncheol Kang, or repository `dudskrla/ISEPT`. Adjacent statistical arbitrage records in this repository explore copula cointegration (`crypto-pairs-trading-copula-cointegration-2026-08-31.md`), optimal stopping reinforcement learning (`exploratory-reinforcement-learning-sequential-optimal-stopping-pairs-trading-2026-09-05.md`), maximum weight graphical matching (`graphical-matching-pairs-trading-maximum-weight-matching-2026-09-05.md`), and path-signature decomposition (`path-signature-decomposition-segmented-levy-area-futures-pair-trading-2026-09-03.md`), but none utilize 2D candlestick image visual representations combined with a closed-loop forward Sharpe-ratio feedback mechanism.

## Economic mechanism

### Source-reported

The paper identifies two fundamental structural deficiencies in classical pairs trading literature:
1. **Separation of Pair Selection and Execution:** Conventional statistical arbitrage frameworks (e.g., Gatev et al. 2006 distance method, Vidyamurthy 2004 cointegration method) decouple the pair identification phase from the trade execution phase. Pairs are selected based purely on historical formation-window statistical similarity (such as Euclidean distance / sum of squared differences or cointegration p-values) without incorporating whether those pairs historically generated positive risk-adjusted returns during execution. This decoupling leads to parameter overfitting, susceptibility to structural breaks, and selection of pairs whose spreads diverge irreversibly upon entry.
2. **Information Loss from 1D Price Aggregation:** Traditional time-series methods rely on daily closing prices or normalized return series, discarding intraday price action, range volatility, and candlestick geometry (shadows, body size, gap structures). Financial traders visual inspection relies heavily on candlestick chart patterns to discern equilibrium shifts and support/resistance boundaries.
3. **Adaptive Closed-Loop Learning:** By predicting the out-of-sample forward Sharpe ratio using visual representations of candlestick charts and continuously feeding realized trading performance back into model retraining at each month-end, the framework establishes a dynamic feedback loop that adapts to shifting volatility regimes and structural breaks.

### Research interpretation

The strategy operates as a two-stage hybrid statistical arbitrage engine:
- **Visual Representation Compression (CAE):** A deep Convolutional Autoencoder compresses 21-day rolling candlestick chart images into low-dimensional latent embeddings, capturing spatial and geometric relationships across open, high, low, and close coordinates that are lost in 1D scalar closing-price series.
- **Cross-Asset Interaction & Sharpe Regression (MLP):** Concatenating the latent visual representations of two equities maps the joint co-movement space into an expected forward Sharpe ratio $\hat{S}_{t+1}$. This acts as an empirical filter that discards statistically cointegrated but un-tradable pairs (e.g., pairs with excessive divergence risk or inadequate mean-reverting speed).
- **Regime-Adaptive Execution Feedback:** Monthly retraining on realized trading outcomes acts as an online policy update, penalizing pair structures that deteriorated during recent macro environments and prioritizing pairs whose mean-reverting properties remain intact.

## Signal

The signal and pair-selection pipeline comprises four sequential stages (`source-reported`):

```text
Daily OHLCV Data (Formation Window: 12 months, T = 12)
        ↓
Stage 1: Candlestick Image Rendering (21-day rolling windows, 64×64 RGB, log-scaled)
        ↓
Stage 2: Convolutional Autoencoder (CAE) Encoding (Latent vector z ∈ R^16384 → Average over T=12 → PCA to 512 dims)
        ↓
Stage 3: Pair Formulation & Sharpe Regressor (Concat z_A and z_B → 1024 dims → 4-layer MLP → Predicted Sharpe S_hat)
        ↓
Stage 4: Dynamic Top-K Selection & Z-Score Mean-Reversion Execution (Next-day entry, k_entry=2.0σ, k_exit=0.0σ)
        ↓
Closed Loop: Monthly Realized Sharpe Ratios fed back into MLP Retraining Dataset
```

### 1. Candlestick Image Generation (`source-reported`)
- **Input Timeframe:** Daily bars for each stock $i$ over the 12-month formation period.
- **Window Size:** Sliding 21 trading days ($\approx 1$ calendar month).
- **Rendering:** Rendered as $64 \times 64$ RGB images via `mplfinance`/`matplotlib`.
- **Scaling:** Log-price scaling applied across the 21-day window to eliminate nominal price-level distortion across heterogeneous tickers.

### 2. Convolutional Autoencoder (CAE) Architecture (`source-reported`)
- **Input:** $x \in \mathbb{R}^{3 \times 64 \times 64}$.
- **Encoder:**
  - Block 1: `Conv2d(3, 64, kernel_size=3, padding=1)` $\to$ `BatchNorm2d(64)` $\to$ `PReLU()` $\to$ `MaxPool2d(2, 2)` (Output: $64 \times 32 \times 32$).
  - Block 2: `Conv2d(64, 128, kernel_size=3, padding=1)` $\to$ `BatchNorm2d(128)` $\to$ `PReLU()` $\to$ `MaxPool2d(2, 2)` (Output: $128 \times 16 \times 16$).
  - Block 3: `Conv2d(128, 256, kernel_size=3, padding=1)` $\to$ `BatchNorm2d(256)` $\to$ `PReLU()` $\to$ `MaxPool2d(2, 2)` (Output: $256 \times 8 \times 8 = 16,384$ units).
- **Decoder:**
  - Block 1: `Conv2d(256, 256, kernel_size=3, padding=1)` $\to$ `BatchNorm2d(256)` $\to$ `PReLU()` $\to$ `Upsample(scale_factor=2, mode='nearest')`.
  - Block 2: `Conv2d(256, 128, kernel_size=3, padding=1)` $\to$ `BatchNorm2d(128)` $\to$ `PReLU()` $\to$ `Upsample(scale_factor=2, mode='nearest')`.
  - Block 3: `Conv2d(128, 64, kernel_size=3, padding=1)` $\to$ `BatchNorm2d(64)` $\to$ `PReLU()` $\to$ `Upsample(scale_factor=2, mode='nearest')`.
  - Final: `Conv2d(64, 3, kernel_size=3, padding=1)` $\to$ `Sigmoid()`.
- **Training Hyperparameters:** Batch size $= 2048$, Epochs $= 20$, Early stopping patience $= 3$, Initial learning rate $= 1 \times 10^{-4}$, StepLR scheduler (`step_size=5`, $\gamma=0.5$), Train/Val ratio $= 0.70/0.30$.
- **Stock Representation:** The latent tensor $z \in \mathbb{R}^{16384}$ is extracted from the encoder bottleneck for each 21-day window and averaged across the $T = 12$ monthly windows in the formation period.
- **Dimensionality Reduction:** IncrementalPCA / PCA reduces the 16,384-dimensional averaged vector to $d = 512$ dimensions (`PCA_DIM = 512`).

### 3. Sharpe Regressor (MLP) Architecture (`source-reported`)
- **Pair Representation:** For candidate pair $(A, B)$, the pair embedding vector is formed by horizontal concatenation:
  $$\mathbf{x}_{\text{pair}} = [\mathbf{z}_A \,\|\, \mathbf{z}_B] \in \mathbb{R}^{1024}$$
- **Network Layers:**
  - `LayerNorm(1024)`
  - `Linear(1024, 1024)` $\to$ `ReLU()` $\to$ `Dropout(p=0.5)`
  - `Linear(1024, 512)` $\to$ `ReLU()` $\to$ `Dropout(p=0.5)`
  - `Linear(512, 128)` $\to$ `ReLU()`
  - `Linear(128, 1)` $\to$ scalar predicted Sharpe ratio $\hat{S}_{A,B}$.
- **Loss Function & Training:** Mean Squared Error (MSE) loss against realized historical Sharpe ratio. Batch size $= 512$, Adam optimizer, learning rate $= 1 \times 10^{-3}$, weight decay $= 1 \times 10^{-5}$, Epochs $= 50$, Patience $= 5$.

### 4. Pair Selection and Execution Rules (`source-reported`)
- **Pair Ranking:** In each rebalancing month, candidate pairs are ranked in descending order of predicted Sharpe ratio $\hat{S}$.
- **Portfolio Selection:** Top $K$ pairs are selected:
  - Training / Warm-start: $K = 100$ (`TOP_K_TRAIN = 100`).
  - Out-of-Sample Testing: $K = 30$ (`TOP_K_TEST = 30`), aggregated across top $K = 20$ in reporting (`TOP_K = 20`).
- **Normalized Price Series:**
  $$s_i(t) = \frac{P_i(t)}{P_i(t_0)}$$
  where $t_0$ is the first valid trading day of the 12-month formation period.
- **Spread & Formation Statistics:**
  $$\text{spread}(t) = s_A(t) - s_B(t)$$
  $$\mu = \frac{1}{N_{\text{form}}} \sum_{\tau \in \text{Formation}} \text{spread}(\tau), \quad \sigma = \sqrt{\frac{1}{N_{\text{form}}} \sum_{\tau \in \text{Formation}} (\text{spread}(\tau) - \mu)^2}$$
- **Deviation Metric:** $\text{dev}(t) = \text{spread}(t) - \mu$.
- **Long/Short Entry Trigger:** Next-day market order generated when absolute deviation crosses the entry barrier:
  $$|\text{dev}(t)| \ge k_{\text{entry}} \times \sigma, \quad k_{\text{entry}} = 2.0$$
  - If $\text{dev}(t) > 0$ ($A$ overvalued relative to $B$): Short $A$, Long $B$.
  - If $\text{dev}(t) < 0$ ($A$ undervalued relative to $B$): Long $A$, Short $B$.
- **Execution Timing:** Next-day execution (`source-reported`, `main_ours_gatev.py` lines 185–198: signal formed at day $t$ close $\to$ executed on day $t+1$).
- **Exit Trigger:**
  - Mean-reversion exit: $|\text{dev}(t)| \le k_{\text{exit}} \times \sigma$ where $k_{\text{exit}} = 0.0$ (spread crosses the formation mean $\mu$).
  - Holding period expiration: Forced liquidation at the end of the 6-month trading period (`FORCE_CLOSE`).
  - Delisting / missing-data exit: Immediate liquidation if either ticker ceases trading or prints NaN (`DELIST_CLOSE`).
- **Closed-Loop Feedback:** At each month-end, the realized Sharpe ratios of traded pairs are appended to the training dataset, and the Sharpe Regressor is incrementally retrained.

## Required data

- **Universe:** S&P 500 constituents (`source-reported`, `SNP500_UNIVERSE.xlsx`).
- **Asset Class:** US Equities (`source-reported`).
- **Timeframe:** Daily OHLC bars (`source-reported`).
- **Data Fields:** Open, High, Low, Close (`source-reported`). Volume is not utilized in the core image generator (`Image_CAE.py`).
- **Lookback Windows:**
  - Formation period: 12 months preceding trade month ($T = 12$) (`source-reported`).
  - Trading period: 6 months following formation (`source-reported`).
  - Minimum formation overlap: 120 valid trading days (`min_days = 120`) (`source-reported`).
- **Missing Data Handling:** Pairs with non-overlapping formation dates or $< 120$ overlapping days are dropped. If NaN occurs during active trading, the position is immediately liquidated at the last available mark (`DELIST_CLOSE`) (`source-reported`).

## Execution assumptions

- **Order Timing:** Daily close signal generation $\to$ next-day execution (`source-reported`).
- **Fill Model:** Immediate full fill at observed day $t+1$ prices without partial fills or queueing (`source-reported`).
- **Position Sizing:** Equal-dollar gross exposure: $\$1.0$ long and $\$1.0$ short per active pair ($\$2.0$ total gross exposure per pair, `GROSS_EXPOSURE = 2.0`) (`source-reported`). Share count: $q_{\text{long}} = 1.0 / P_{\text{long}}$, $q_{\text{short}} = 1.0 / P_{\text{short}}$ (`source-reported`).
- **Transaction Costs:** Fixed commission rate of $1\text{ bp}$ ($0.0001$ or $0.01\%$) per trade notional ($P_{\text{long}} + P_{\text{short}}$) deducted upon entry and upon exit (`source-reported`, `Pair_Trading.py` line 23).
- **Slippage Model:** Zero slippage modeled in primary source (`source-reported`). A realistic institutional slippage assumption of $2\text{ to }5\text{ bps}$ half-spread per leg is `research-proposed`.
- **Borrow / Shorting Availability:** Unrestricted shorting with zero borrow fee assumed in primary source (`source-reported`). Incorporating standard hard-to-borrow fees ($25\text{–}100\text{ bps}$ annualized) is `research-proposed`.
- **Capital Capacity:** Primary code simulates unit dollar bets without market impact (`source-reported`). An institutional portfolio capacity limit of $\$25\text{M}$ AUM or max $1\%$ of 20-day Average Daily Volume (ADV) is `research-proposed`.

## Evidence

### Source-reported

- **Sample Period:** Full sample January 1990 – June 2024 (34.5 years).
  - Training & In-Sample Warm-Start: January 1991 – December 2003 (156 months / 13 years).
  - Out-of-Sample Evaluation: January 2004 – June 2024 (246 monthly evaluation cycles / 20.5 years).
- **Evaluated Strategy Variants:**
  1. Classical Gatev (Distance / SSD method, Gatev et al. 2006).
  2. Classical Vidyamurthy (Cointegration method, Vidyamurthy 2004).
  3. ISEPT + Gatev (`2_GATEV`).
  4. ISEPT + Vidyamurthy (`2_VIDYAMURTHY`).
- **Empirical Findings Summary:**
  The authors report that ISEPT-selected pairs substantially outperform classical distance and cointegration baselines across both Return on Investment (ROI) and risk-adjusted metrics (Sharpe ratio, Sortino ratio, and Calmar ratio) over the 2004–2024 out-of-sample period (ICAIF '25 paper Table 1 and repository README).
- **Provenance Gap / Data Disclosure:**
  While the exact Python code, neural network architecture, and evaluation notebook (`average_results.ipynb`) are fully open-source in the GitHub repository, the pre-computed summary CSV files containing the exact decimal values of Table 1 are not checked into the Git repository (they reside in gitignored local output folders), and the ACM Digital Library proceeding is behind an access paywall. Therefore, exact published decimal statistics (e.g., specific annualized Sharpe to two decimal places) are not reproduced here to avoid fabricating precision.

### Independently reproduced

`Not independently reproduced.`

### Negative evidence

- **Computational Overhead:** Generating $64 \times 64$ candlestick chart images for all S&P 500 constituents across sliding 21-day windows requires significant disk storage and image rendering time, creating an operational bottleneck compared to vectorized 1D mathematical operations.
- **Dimensionality Bottleneck:** Flattening the CAE bottleneck to 16,384 dimensions requires an intermediate PCA compression step to 512 dimensions before feeding into the MLP. Loss of spatial information during PCA projection may discard subtle geometric cues.
- **Regime Vulnerability:** In prolonged trending or market crash regimes (e.g., 2008 GFC, March 2020 COVID crash), statistical divergence across equity pairs frequently widens beyond the $2.0\sigma$ threshold without reverting before the 6-month force-close boundary, causing tail drawdowns.
- **Absence of Real-World Friction:** The 1 bp commission assumption significantly underestimates real-world small-cap equity trading costs, where bid-ask spreads, borrow fees on the short leg, and execution slippage can erode statistical arbitrage margins.

## Falsification plan

To falsify the hypothesis that 2D candlestick image representations and closed-loop Sharpe feedback generate superior risk-adjusted alpha over classical 1D pairs trading:

1. **Ablation Test 1 (Image vs. 1D Numerical Returns):** Replace the CAE image embedding with a 1D Temporal Convolutional Network (TCN) or 1D Autoencoder trained directly on raw normalized OHLCV time series. If the 1D model achieves equal or superior out-of-sample Sharpe and ROI, the hypothesis that visual 2D candlestick rendering adds unique orthogonal information is falsified (`research-defined falsification threshold: difference in OOS Sharpe < 0.10`).
2. **Ablation Test 2 (Feedback Loop vs. Open Loop):** Compare ISEPT against an "open-loop" variant where the Sharpe Regressor is trained once on the 1991–2003 warm-start period and never updated with realized trading results. If the closed-loop feedback variant fails to outperform the open-loop model by at least $15\%$ in out-of-sample Sharpe, the dynamic adaptive feedback thesis is falsified (`research-defined falsification threshold: Sharpe_closed / Sharpe_open <= 1.15`).
3. **Transaction Cost Stress Test:** Evaluate the strategy under realistic equity execution costs ($5\text{ bps}$ commission $+ 5\text{ bps}$ half-spread slippage $+ 50\text{ bps}$ annualized short borrow fee). If net annualized Sharpe drops below $0.50$, the strategy is commercially unviable (`research-defined falsification threshold: net OOS Sharpe < 0.50`).
4. **Permutation / Placebo Test:** Randomly shuffle candlestick images across non-matching tickers during embedding generation. If the shuffled model produces performance indistinguishable from the true model, the signal represents spurious statistical fitting (`research-defined falsification threshold: p > 0.05 on paired t-test of returns`).

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Research Interpretation:** The primary source investigates exclusively US equities (S&P 500). Porting the ISEPT framework to cryptocurrency markets requires substantial structural adaptation (`research-proposed`):
  1. **Continuous 24/7 Trading:** Crypto operates continuously without daily market open/close auctions. A 21-day sliding window must use standardized UTC cutoffs (e.g., 00:00 UTC) to render candlestick images.
  2. **Perpetual Futures & Funding Rates:** In crypto perpetual pairs (e.g., BTC/USDT vs. ETH/USDT, or layer-1 altcoin baskets), holding a long/short pair incurs asymmetric 8-hour funding payments. If the short leg trades at a negative funding rate or the long leg pays high funding, carry drag can erode the statistical arbitrage spread.
  3. **High Volatility & Tail Risk:** Crypto pairs exhibit higher volatility and frequent regime shifts compared to large-cap equities. A $k_{\text{entry}} = 2.0\sigma$ threshold may lead to premature entry during systemic market-wide beta deleveraging events, necessitating dynamic ATR-based or volatility-scaled entry bands (`research-proposed`).
  4. **Liquidity & Venue Fragmentation:** Cross-pair trading in altcoins is constrained by order-book depth and taker slippage on centralized exchanges (Binance, Bybit, OKX).

## Limitations

- **Source Provenance Gap:** Pre-computed decimal performance tables from Table 1 are not stored as plain text in the public Git repository, precluding exact tabular citation without licensed ACM proceeding access.
- **Execution Idealization:** Next-day market execution assumes zero price impact and immediate liquidity at daily bar boundaries, which is unrealistic for large institutional capital.
- **Short Borrow Cost Omission:** The backtesting model omits borrow fees and locate constraints on short equity legs.
- **Underspecified PCA Convergence:** IncrementalPCA / PCA dimensionality reduction depends on the initial batch ordering, which may introduce minor numerical variability across training runs.

## Implementation status

- `not-implemented`: No implementation of ISEPT or its CAE/MLP pipeline exists in `nautilus-quant-system` or PyBroker research stacks.
- This document constitutes an upstream research capture and does not authorize live or paper deployment.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Research capture does not imply strategy adoption, backtest verification, or execution approval.

## Related Wiki records

- `[[quant/crypto-pairs-trading-copula-cointegration-2026-08-31]]` — Classical bivariate statistical arbitrage and copula dependence.
- `[[quant/exploratory-reinforcement-learning-sequential-optimal-stopping-pairs-trading-2026-09-05]]` — Reinforcement learning optimal stopping for statistical arbitrage pair execution.
- `[[quant/graphical-matching-pairs-trading-maximum-weight-matching-2026-09-05]]` — Combinatorial optimization and maximum weight matching for cross-sectional pair selection.
- `[[quant/path-signature-decomposition-segmented-levy-area-futures-pair-trading-2026-09-03]]` — Path signature and rough path theory for pair trading co-movement.
- `[[quant/dynamic-johansen-deep-weighted-ensemble-cryptocurrency-pairs-2026-09-05]]` — Dynamic cointegration and deep weighted ensemble for digital asset pairs.

## Sources

1. **Conference Proceedings:**
   Nayoung Kim, Jangwook Lee, and Yuncheol Kang. 2025. "ISEPT: Image-Based Selection and Execution Framework for Pair Trading." In *Proceedings of the 6th ACM International Conference on AI in Finance (ICAIF '25)*, November 15–18, 2025, Singapore, pages 413–421. ACM, New York, NY, USA.
   DOI: [10.1145/3768292.3770346](https://doi.org/10.1145/3768292.3770346).
2. **Primary Code Repository:**
   Nayoung Kim (`dudskrla`). Official source implementation: `dudskrla/ISEPT`.
   GitHub: [https://github.com/dudskrla/ISEPT](https://github.com/dudskrla/ISEPT).
   Canonical Head Commit SHA: `4533320eda07c135c3aed305dc175926bad5ea1d`.
   Code Implementation Commit SHA: `c2dff16623c58690bdf70cfe625ad6f8fa2ae142`.
