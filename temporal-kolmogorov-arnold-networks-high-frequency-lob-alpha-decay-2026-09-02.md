---
schema: strategy-research-record-v1
title: "Temporal Kolmogorov-Arnold Networks (T-KAN) for High-Frequency Limit Order Book Forecasting: Efficiency, Interpretability, and Alpha Decay"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - limit-order-book
  - market-microstructure
  - high-frequency-trading
  - kolmogorov-arnold-networks
  - machine-learning
  - deep-learning
  - alpha-decay
status: research-only
confidence: high
source_as_of: 2026-01-05
sources:
  - "Ahmad Makinde, 'Temporal Kolmogorov-Arnold Networks (T-KAN) for High-Frequency Limit Order Book Forecasting: Efficiency, Interpretability, and Alpha Decay', arXiv:2601.02310v1 [q-fin.CP], January 5, 2026. DOI: 10.48550/arXiv.2601.02310. https://arxiv.org/abs/2601.02310"
  - "AhmadMak/Temporal-Kolmogorov-Arnold-Networks-T-KAN-for-High-Frequency-Limit-Order-Book-Forecasting, commit 4a1b96cfcc64e6371cdd4979138de0f21c2dff76, path: Temporal_Kolmogorov_Arnold_Networks_(T_KAN)_for_High_Frequency_Limit_Order_Book_Forecasting_Efficiency,_Interpretability,_and_Alpha_Decay.ipynb. https://github.com/AhmadMak/Temporal-Kolmogorov-Arnold-Networks-T-KAN-for-High-Frequency-Limit-Order-Book-Forecasting"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Temporal Kolmogorov-Arnold Networks (T-KAN) for High-Frequency Limit Order Book Forecasting: Efficiency, Interpretability, and Alpha Decay

## Provenance

- **Primary Paper Source:** Ahmad Makinde, *"Temporal Kolmogorov-Arnold Networks (T-KAN) for High-Frequency Limit Order Book Forecasting: Efficiency, Interpretability, and Alpha Decay"*, arXiv preprint `arXiv:2601.02310v1 [q-fin.CP]`, submitted January 5, 2026. DOI: [10.48550/arXiv.2601.02310](https://doi.org/10.48550/arXiv.2601.02310). Full HTML text: [https://arxiv.org/html/2601.02310v1](https://arxiv.org/html/2601.02310v1). Abstract: [https://arxiv.org/abs/2601.02310](https://arxiv.org/abs/2601.02310).
- **Primary Code Source:** Public GitHub repository `https://github.com/AhmadMak/Temporal-Kolmogorov-Arnold-Networks-T-KAN-for-High-Frequency-Limit-Order-Book-Forecasting`. Immutable commit SHA: `4a1b96cfcc64e6371cdd4979138de0f21c2dff76`. Key audit files: `Temporal_Kolmogorov_Arnold_Networks_(T_KAN)_for_High_Frequency_Limit_Order_Book_Forecasting_Efficiency,_Interpretability,_and_Alpha_Decay.ipynb`, `Visualisations/final_metrics.csv`, and `README.md`.
- **Benchmark Data Setting:** The empirical validation is conducted on the FI-2010 Benchmark Dataset (Ntakaris et al., 2018), comprising high-frequency limit order book (LOB) event sequences from 5 Finnish equities traded on NASDAQ Nordic over 10 consecutive trading days (June 1–14, 2010; ~4.5 million event transitions).

## Economic mechanism

### Source-reported

High-frequency trading (HFT) environments generate massive streams of non-linear and noisy limit order book events. Traditional deep learning architectures (such as CNN-LSTM models like DeepLOB) suffer from rapid alpha decay as the forecast horizon $k$ increases, losing predictive edge beyond short horizons. Furthermore, standard neural network layers rely on fixed point-wise activation functions (e.g., ReLU, LeakyReLU, Sigmoid) with static linear weight matrices. Under the Universal Approximation Theorem, capturing localized oscillations and state-dependent liquidity dynamics in microsecond microstructure data requires immense network depth, which leads to overfitting, high parameter overhead, and performance collapse under realistic execution friction.

By replacing fixed linear weight transformations with learnable univariate B-spline activation functions on the edges (grounded in the Kolmogorov-Arnold Representation Theorem), the network learns the functional *shape* of market signals rather than just linear scaling coefficients. The learned splines autonomously develop flat "dead-zones" around near-zero inputs—effectively filtering out bid-ask bounce and micro-noise—while non-linearly magnifying high-conviction order flow imbalances and liquidity exhaustion events.

### Research interpretation

The core falsifiable hypothesis is that **parameterizing neural activation functions as learnable localized B-splines rather than static affine transformations allows a recurrent sequence model to decouple high-frequency microstructure noise from genuine directional order flow momentum, thereby mitigating alpha decay across longer event horizons ($k = 100$ ticks) and preserving positive net profitability after a 1.0 bps execution drag**:

1. **Noise Gating via Learned S-Curve Dead-Zones:** In continuous double auctions, small price fluctuations and oscillating limit order cancels around the touch represent transient inventory rebalancing and quote flicker. Standard linear weights transmit this variance into hidden states, triggering spurious trading signals. A B-spline activation can parameterize zero derivatives $\phi'(x) \approx 0$ for $|x| < \delta$ (a dead-zone) while providing steep gradients for $|x| \ge \delta$, effectively performing automated non-linear denoising.
2. **Persistence Over Longer Horizons (Alpha Decay Resistance):** At short horizons ($k = 10$), spatial LOB depth features dominate because quotes at the inside spread dictate immediate execution. At longer horizons ($k = 100$ events), spatial features decay and path-dependent temporal order flow dynamics dominate. B-spline functional edges preserve the topological manifold of multi-step order flow transitions better than rigid CNN kernels.
3. **Profitability Density per Parameter:** While learnable splines increase parameter count relative to simple linear layers, the concentration of capacity on functional transformations rather than wider matrix dimensions provides higher return density per parameter, enabling the model to clear execution friction.

*Ported Hypothesis Note:* The empirical evidence is established exclusively on equities in the NASDAQ Nordic FI-2010 benchmark. Any application to crypto perpetual or spot order books is an adapted, unproven research interpretation.

## Signal

### 1. State Formulation and Sliding Window Unit
- **LOB Snapshot Vector:** At event timestamp $t$, the raw state comprises 10 levels of bid/ask prices and volumes:
  $$\mathcal{L}_t = \{P_t^{(b, i)}, V_t^{(b, i)}, P_t^{(a, i)}, V_t^{(a, i)}\}_{i=1}^{10} \in \mathbb{R}^{40}$$
- **Feature Extraction & Normalization:** Features are expanded into the standardized 144-dimensional representation $\hat{\mathcal{L}}_t \in \mathbb{R}^{144}$ (following Ntakaris et al., 2018), incorporating order flow imbalances, relative spreads, price differences across levels, and accumulated depth.
- **Sliding Window:** Input tensor $X_t \in \mathbb{R}^{T \times 144}$ has lookback window $T = 10$ consecutive order book events:
  $$X_t = [\hat{\mathcal{L}}_{t-T+1}, \dots, \hat{\mathcal{L}}_t]$$

### 2. Prediction Target and Directional Labeling
- The prediction target is the direction of the smoothed mid-price $m_t = (P_t^{(a, 1)} + P_t^{(b, 1)}) / 2$ over forward horizon $k = 100$ events (also evaluated at $k \in \{10, 20, 50\}$).
- Forward mid-price return:
  $$r_t^{(k)} = \frac{m_{t+k} - m_t}{m_t}$$
- Directional label $y_t \in \{-1, 0, +1\}$ (mapped to $\{0, 1, 2\}$ for classification):
  $$y_t = \begin{cases} +1 (\text{Up}) & \text{if } r_t^{(k)} > \alpha \\ 0 (\text{Stationary}) & \text{if } |r_t^{(k)}| \le \alpha \\ -1 (\text{Down}) & \text{if } r_t^{(k)} < -\alpha \end{cases}$$
  with stationary threshold $\alpha = 0.002$ (or benchmark-standard FI-2010 threshold yielding ~65% neutral class prevalence).

### 3. Kolmogorov-Arnold Formulation
- Under the Kolmogorov-Arnold representation theorem, a multivariate continuous function on a bounded domain satisfies:
  $$f(x_1, \dots, x_n) = \sum_{q=1}^{2n+1} \Phi_q\left(\sum_{p=1}^n \phi_{q, p}(x_p)\right)$$
- Each univariate activation $\phi(x)$ is parameterized as a linear combination of a base activation function (SiLU) and a B-spline:
  $$\phi(x) = w_b b(x) + w_s \text{Spline}(x), \quad b(x) = \frac{x}{1 + e^{-x}}$$
  $$\text{Spline}(x) = \sum_{i} c_i B_{i, k}(x)$$
  where $B_{i, k}(x)$ are order-$k$ B-splines defined over a grid of knots $\{t_i\}$ via the Cox-de Boor recursion.

### 4. Network Architecture and Implementation Discrepancy Note
- **Paper Theoretical Specification:** Equations (7)–(12) in Section 2.3 formulate a recurrent T-KAN cell where each LSTM gate ($i_t, f_t, g_t, o_t$) replaces linear projections with KAN layers:
  $$i_t = \sigma(KAN_i([x_t, h_{t-1}])), \quad f_t = \sigma(KAN_f([x_t, h_{t-1}])), \quad g_t = \tanh(KAN_g([x_t, h_{t-1}])), \quad o_t = \sigma(KAN_o([x_t, h_{t-1}]))$$
- **Repository Implementation Code:** In the author's audited evaluation notebook (`Temporal_Kolmogorov_Arnold_Networks_(T_KAN)...ipynb`, cells 17 & 19), the evaluated model architecture utilizes:
  - 2-layer standard LSTM encoder (input size 144, hidden size 64, `batch_first=True`);
  - KAN-approximating projection head operating on the final hidden state $h_T$: `nn.Sequential(nn.Linear(64, 256), nn.SiLU(), nn.Linear(256, 3))`.
  *(Researchers reconstructing this pipeline must note that while the paper derives the full internal-gate KAN-LSTM cell, the published codebase checkpoint pairs an LSTM sequence encoder with a non-linear SiLU/spline projection head).*

### 5. Loss Function and Class Imbalance Weighting
- To address severe class imbalance in the auction dataset (neutral class accounts for 65.3% of events: distribution $\{36533, 138391, 37135\}$), an inverse-frequency-weighted cross-entropy loss is applied:
  $$\mathcal{L} = -\frac{1}{N} \sum_{i=1}^N \sum_{c=1}^3 w_c \cdot y_{i, c} \log(\hat{y}_{i, c}), \quad w_c = \frac{N}{3 \cdot n_c}$$
  yielding calibrated class weights:
  $$w = [1.93, 0.51, 1.90]$$

### 6. Trading Rule and Order Trigger
- At each event $t$, if the model output probability $P(\text{Up}) > \theta_{\text{entry}}$ (and $P(\text{Up}) > P(\text{Down})$), enter Long 1 unit.
- If $P(\text{Down}) > \theta_{\text{entry}}$, enter Short 1 unit.
- If $P(\text{Stationary}) > \max(P(\text{Up}), P(\text{Down}))$ or a sign flip occurs, flatten position to cash.
- Positions are evaluated over the forward holding interval of $k = 100$ events.

## Required data

- **Instrument Universe:** 5 actively traded Finnish equities on NASDAQ Nordic (Outokumpu, Sampo, Rautaruukki, Wartsila, YIT).
- **Venue:** NASDAQ Nordic (Helsinki).
- **Market Type:** Cash equity limit order book.
- **Timeframe / Sampling:** Event-driven tick time; consecutive order book updates (new limit order, modification, cancellation, or execution).
- **Data Fields:** 10 levels of bid/ask prices and volumes ($P^{(b, 1..10)}, V^{(b, 1..10)}, P^{(a, 1..10)}, V^{(a, 1..10)}$), normalized into 144 features including order flow imbalances, micro-spreads, depth differences, and rolling auction Z-scores.
- **Point-in-Time Hygiene:** Inputs are strictly lagged $t-9$ to $t$; prediction target is forward $t+k$ with non-overlapping evaluation chunks to prevent target leakage.
- **Data Completeness:** Normalized benchmark files (`Train_Dst_Auction_ZScore_CF_7.txt`, `Test_Dst_Auction_ZScore_CF_7.txt`).

## Execution assumptions

- **Execution Reference Price:** Mid-price $m_t = (P_t^{(a, 1)} + P_t^{(b, 1)}) / 2$ at event $t$.
- **Transaction Costs:** Flat 1.0 bps (0.01%) per executed turn (subtracted from cumulative gross returns).
- **Slippage & Impact:** The source backtest assumes immediate fill at mid-price without modeling queue priority, quote fading, or price impact of aggressive market orders.
- **Order Timing:** Instantaneous event-to-order execution (zero modeled latency delay between event arrival and execution).
- **Position Sizing:** Fixed unit position (Long +1, Flat 0, Short -1); no dynamic leverage or fractional compounding.

## Evidence

### Source-reported

All figures below are directly reported by Ahmad Makinde (arXiv:2601.02310v1, January 2026) and verified against the repository's `Visualisations/final_metrics.csv` and backtest logs on the FI-2010 benchmark dataset at forecast horizon $k = 100$:

| Metric | DeepLOB Baseline | T-KAN (Proposed) | Reported Relative Improvement |
| :--- | :---: | :---: | :---: |
| **Precision** | 0.4604 | **0.5343** | +16.0% |
| **Recall** | 0.4329 | **0.4748** | +9.7% |
| **F1-Score** | 0.3354 | **0.3995** | **+19.1%** |
| **Net Terminal Return (1.0 bps cost)** | -82.76% | **+132.48%** | **+215.2% delta** |
| **Model Parameters** | 58,211 | 104,451 (backtest model) / 532,675 (unpruned) | +79.4% capacity |

- **Alpha Decay Persistence:** Figure 5 in the paper documents that while DeepLOB's information coefficient (IC) drops sharply between $k = 20$ and $k = 100$, T-KAN exhibits a flatter decay profile, retaining significant predictive power at $k = 100$.
- **Economic Viability:** Under 1.0 bps execution drag, DeepLOB experiences consistent capital erosion (-82.76%), whereas T-KAN achieves a positive upward-sloping equity trajectory (+132.48%), indicating that its directional signals exceed execution friction.

### Independently reproduced

`not independently reproduced`.

### Negative evidence

- The source backtest evaluates executions at the *mid-price*, which understates true trading costs: an aggressive trader executing via market orders must cross the spread (paying half-spread plus exchange fees), while a passive maker incurs execution latency and adverse selection (fill rate bias).
- The author notes in Section 5.1 that T-KAN entails a 79.4% higher parameter footprint (104,451 vs 58,211), which increases computational latency unless implemented on specialized hardware.
- None identified in the reviewed sources regarding out-of-sample failure on other venues; absence is not evidence of no negative result.

## Falsification plan

1. **Spread-Crossing Execution Audit:** Replace mid-price execution with realistic bid/ask execution ($P_{\text{buy}} = P_t^{(a, 1)}, P_{\text{sell}} = P_t^{(b, 1)}$). If the net return collapses from +132% to negative, the apparent alpha is an artifact of the mid-price assumption.
2. **Latency Insertion Stress Test:** Introduce a 10 ms to 100 ms execution delay between the trigger event $t$ and order fill. If directional accuracy degrades below random classification, the edge is purely ultra-low-latency queue-dependent.
3. **Architecture Ablation Test:** Evaluate an identical 2-layer LSTM connected to a standard MLP head with identical parameter count (104,451 parameters). If the standard MLP achieves comparable F1-score and return, the performance gain is attributable to network capacity rather than Kolmogorov-Arnold B-splines.
4. **Cross-Asset / Crypto Out-of-Sample Test:** Evaluate the pre-trained and retrained T-KAN on Binance BTCUSDT and ETHUSDT L2/L3 order book feeds. Failure to achieve an F1-score > 0.38 or positive net returns after 2-4 bps taker fees falsifies portability to crypto microstructure.

## Crypto portability

- **Classification:** `adapted` / `unproven`.
- **Portability Rationale:** The mechanism (non-linear filtering of micro-oscillations via learnable spline dead-zones) is theoretically asset-agnostic and applies naturally to crypto perpetual order books.
- **Crypto-Specific Frictions & Obstacles:**
  - **Higher Transaction Costs:** Spot and perpetual exchanges (Binance, Bybit) impose taker fees of 2.0 to 5.0 bps (VIP0), which is 2x–5x higher than the 1.0 bps hurdle tested in the paper. A 2.0+ bps drag would likely eliminate the reported net return unless traded on VIP maker tiers.
  - **Cancel/Replace Velocity:** Crypto LOBs experience intense quote stuffing and cancel-to-fill ratios exceeding 95%, meaning 10 consecutive event updates ($T = 10$) may span less than a millisecond, shifting the required lookback from event counts to wall-clock time windows.
  - **Exchange Fragmentation:** Global crypto price discovery is split across multiple venues (Binance, OKX, Bybit, Coinbase); a single-venue LOB model may suffer adverse selection from cross-venue lead-lag toxic flow.

## Limitations

- **Underspecified Code vs Theory Gap:** The paper formulates KAN layers embedded directly into the LSTM internal gating recurrence (Eq. 7–12), whereas the repository's evaluation scripts utilize a standard LSTM encoder followed by a SiLU/spline projection head.
- **Mid-Price Execution Shortcut:** Fill assumptions do not account for bid-ask spread crossing, order queue position, or market impact.
- **Narrow Sample Period:** Evaluated only on 10 trading days in June 2010 across 5 equities on NASDAQ Nordic; regime stability across modern market structures has not been verified.
- **Hardware Dependency:** Localized B-spline evaluations require specialized FPGA / HLS pipelines to achieve sub-millisecond execution speeds in production.

## Implementation status

- `not-implemented`: No implementation or backtest has been performed within this repository's research pipeline, PyBroker, or NautilusTrader.
- The concept remains exploratory research material only.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- This record serves solely to capture the mathematical formulation, empirical claims, and known limitations of the T-KAN microstructure model. It does not constitute authorization for live trading, testnet deployment, or paper trading.

## Related Wiki records

- [[quant/hawkes-self-exciting-lob-return-sign-forecasting-coe-2026-09-02]]
- [[quant/sequential-lob-heavy-tailed-liquidity-crossover-depth-2026-09-02]]
- [[quant/order-flow-two-layer-hawkes-core-reaction-rough-impact-2026-09-02]]
- [[quant/passive-market-impact-optimal-execution-mlofi-2026-09-02]]

## Sources

1. Ahmad Makinde, *"Temporal Kolmogorov-Arnold Networks (T-KAN) for High-Frequency Limit Order Book Forecasting: Efficiency, Interpretability, and Alpha Decay"*, arXiv preprint `arXiv:2601.02310v1 [q-fin.CP]`, January 5, 2026. DOI: [10.48550/arXiv.2601.02310](https://doi.org/10.48550/arXiv.2601.02310). Stable URL: [https://arxiv.org/abs/2601.02310](https://arxiv.org/abs/2601.02310). Full HTML: [https://arxiv.org/html/2601.02310v1](https://arxiv.org/html/2601.02310v1).
2. GitHub Repository: AhmadMak/Temporal-Kolmogorov-Arnold-Networks-T-KAN-for-High-Frequency-Limit-Order-Book-Forecasting. Immutable commit SHA: `4a1b96cfcc64e6371cdd4979138de0f21c2dff76`. URL: [https://github.com/AhmadMak/Temporal-Kolmogorov-Arnold-Networks-T-KAN-for-High-Frequency-Limit-Order-Book-Forecasting](https://github.com/AhmadMak/Temporal-Kolmogorov-Arnold-Networks-T-KAN-for-High-Frequency-Limit-Order-Book-Forecasting).
3. A. Ntakaris, M. Magris, J. Kanniainen, M. Gabbouj, and A. Iosifidis, *"Benchmark dataset for mid-price forecasting of limit order book data with machine learning methods"*, Journal of Forecasting, 37(8), pp. 852–866, 2018. DOI: [10.1002/for.2543](https://doi.org/10.1002/for.2543).
