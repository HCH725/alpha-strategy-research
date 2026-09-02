---
schema: strategy-research-record-v1
title: "STRATA: Staggered-Timescale Selective State-Space Architecture for Cross-Sectional Return Ranking from Raw Intraday Bars with Zero-Sum Causal Stem and Style Residualization"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional-ranking
  - selective-state-space
  - mamba
  - raw-intraday-bars
  - zero-sum-convolution
  - style-residualization
  - market-microstructure
  - execution-timing
status: research-only
confidence: high
source_as_of: 2026-08-28
sources:
  - "Mingju Chen, Enze Zhang, et al. (Baidu Inc.), 'A Compact Selective State-Space Model for Cross-Sectional Stock Return Ranking from Raw Intraday Bars', arXiv preprint arXiv:2608.28060v1 [cs.LG], August 28, 2026. DOI: 10.48550/arXiv.2608.28060. Stable URL: https://arxiv.org/abs/2608.28060"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# STRATA: Staggered-Timescale Selective State-Space Architecture for Cross-Sectional Return Ranking from Raw Intraday Bars with Zero-Sum Causal Stem and Style Residualization

## Provenance

- **Primary Source:** Mingju Chen (Baidu Inc.) and Enze Zhang (Baidu Inc.), *"A Compact Selective State-Space Model for Cross-Sectional Stock Return Ranking from Raw Intraday Bars"*, arXiv preprint `arXiv:2608.28060v1 [cs.LG]`, submitted August 28, 2026. DOI: [10.48550/arXiv.2608.28060](https://doi.org/10.48550/arXiv.2608.28060). Stable URL: [https://arxiv.org/abs/2608.28060](https://arxiv.org/abs/2608.28060).
- **Primary Subject Area:** Machine Learning (`cs.LG`), Computational Finance (`q-fin.CP`), Trading and Market Microstructure (`q-fin.TR`).
- **Context & Motivation:** Quantitative equity alpha systems typically operate in two decoupled stages: domain experts engineer large libraries of formulaic indicators (moving average spreads, price momentum, volume ratios, order-flow imbalance formulas), and a supervised model (e.g., LightGBM or MLP) is trained on those engineered features. Feeding raw price and order-book bars directly into neural sequence models has historically failed due to two fundamental obstacles:
  1. *Scale and level non-stationarity:* Nominal share prices differ across stocks by orders of magnitude (e.g., $5 to $500) and drift over time, causing unconstrained neural networks to latch onto price levels rather than return dynamics.
  2. *Style confounding:* Raw rank correlations are easily dominated by common risk factors (market capitalization, realized volatility, market beta); an algorithm that simply tilts toward small-caps or high-beta stocks can report spurious alpha without possessing genuine stock-picking skill.
  Chen and Zhang introduce STRATA (Staggered-Timescale Residual Architecture), a compact 244,633-parameter selective state-space model that takes 5 days of unadjusted raw 5-minute bars ($F=25$ features) and maps them directly to cross-sectional ranking scores through a level-robust zero-sum convolutional stem and staggered selective state-space layers, evaluating performance strictly after residualizing against eight price-volume style factors.

## Economic mechanism

### Source-reported

1. **Self-Referential Stem as a Learnable High-Pass Filter:** Instead of relying on hand-crafted first differences or rolling z-scores, STRATA constructs four learnable causal depthwise convolutional branches whose kernels are strictly initialized to sum to zero ($\sum k = 0$). By subtracting a channel's own causally smoothed moving average across multiple horizons ($\mathcal{S} = \{3, 12, 48\}$ five-minute bars, corresponding to 15-minute, 1-hour, and 1-day memory), the stem eliminates the "direct current" price level component while allowing gradient descent to adaptively tune the high-pass frequency response. A fifth branch applies a cross-field linear contrast matrix $W^c \in \mathbb{R}^{F \times F}$ within each time step to capture instantaneous order-flow and spread interactions.
2. **Selective State-Space Filtering across Staggered Timescales:** The backbone uses four selective state-space blocks (SSMs) evaluated via log-depth associative parallel scans ($\mathcal{O}(\log T)$ depth). Decay biases $\beta_\ell$ are staggered linearly from $1.0$ down to $-1.5$ across the 4-layer stack, initializing effective memory half-lives from $0.53$ bars ($\approx 2.6$ minutes) at the shallow layer to $3.44$ bars ($\approx 17.2$ minutes) at the deep layer. Input-dependent gating allows the network to dynamically flush stale microstructure states during volatility bursts while preserving persistent multi-day order accumulation trends.
3. **Style-Neutralized Cross-Sectional Sorting:** Cross-sectional rank correlations are explicitly residualized against eight orthogonal price-volume risk factors (size, non-linear size, liquidity, residual volatility, medium-term momentum, market beta, short-term reversal, and intraday volatility). This ensures that predictive power reflects idiosyncratic relative mispricing rather than passive factor harvesting.
4. **Overnight Drift vs. Executable Intraday Breakdown:** The authors decompose the next-day close-to-close return $y_{i,t} = \frac{C_{i,t+1}^{\text{adj}}}{C_{i,t}^{\text{adj}}} - 1$ into an overnight jump $\frac{O_{i,t+1}}{C_{i,t}} - 1$ and an executable daytime session $\frac{C_{i,t+1}}{O_{i,t+1}} - 1$. The economic mechanism reveals that the raw model score accurately forecasts overnight price adjustment driven by non-trading-hour news and auction imbalance, but exhibits intraday mean-reversion at market open that neutralizes the long-short spread if execution is delayed to the open.

### Research interpretation

The falsifiable thesis is that **a compact selective state-space model equipped with zero-sum causal difference convolutions extracts genuine, non-linear intraday microstructure alpha directly from raw bars, achieving statistically significant style-residualized Rank IC ($0.0728$, $p < 0.001$) over standard RNN, TCN, and Transformer baselines; however, the predictive edge is heavily concentrated in the overnight gap ($+75.6\text{ bps/day}$) and fails to yield a statistically profitable long-short spread ($-1.6\text{ bps/day}$, $t = -0.37$) when execution is delayed to next-day open auction prices**:
- The model successfully solves the representation learning problem for raw financial series without manual feature engineering, confirming that structured state spaces (SSMs) are superior to Transformers for dense financial bar sequences due to linear token complexity and exact causal recursive state tracking.
- Crucially, the paper provides a negative trading verdict on close-to-close signal backtests: close-to-close predictive models cannot be claimed as executable trading strategies unless the overnight gap can be monetized via pre-market matching or closing auction participation.

## Signal

### 1. Temporal Protocol and Input Representation

For stock $i$ on signal day $t$, the input tensor $X_{i,t} \in \mathbb{R}^{B \times F \times T}$ spans $D=5$ trading days of $B=48$ five-minute bars per day, yielding a sequence length of $T = D \cdot B = 240$ time steps.
- **Input Channels ($F=25$ raw fields):** Open, High, Low, Close, Volume, Turnover, Trade Count, and 3 levels of Bid/Ask quotes:
  $$\{P_{\text{bid}}^{(k)}, V_{\text{bid}}^{(k)}, N_{\text{bid}}^{(k)}, P_{\text{ask}}^{(k)}, V_{\text{ask}}^{(k)}, N_{\text{ask}}^{(k)}\}_{k=1}^3$$
- **Causality & Normalization:** All inputs are unadjusted raw values (no retroactively applied split/dividend factors). Preprocessing applies fixed unit scaling, $\log(1+x)$ transform on price and size channels, and standardization using train-split-only global mean and standard deviation:
  $$\tilde{x}_{f} = \frac{\log(1 + c_f x_f) - \mu_f^{\text{train}}}{\sigma_f^{\text{train}}}$$
  Missing values are imputed with zeros post-standardization.

### 2. Self-Referential Stem Architecture

Preprocessed input $h \in \mathbb{R}^{B \times F \times T}$ passes through $2 + S$ parallel branches ($S=3$):
1. *Causal First Difference Branch:* Depthwise 1D convolution with kernel $k^d \in \mathbb{R}^{F \times 1 \times 2}$, left-padded by 1, initialized to $[-1, 1]$.
2. *Cross-Field Contrast Branch:* Bias-free linear transformation $W^c \in \mathbb{R}^{F \times F}$ applied independently at each time step $t$:
   $$\text{con}_t = W^c x_t$$
3. *Multi-Scale Deviation-from-Self Branches ($S=3$ scales):* For window sizes $w \in \mathcal{S} = \{3, 12, 48\}$ bars (15 min, 1 hour, 1 day), a depthwise causal kernel $k^{(w)} \in \mathbb{R}^{F \times 1 \times w}$ is initialized uniformly to $1/w$. The branch output is the residual between the current value and the causal moving average, scaled by a learnable positive gain $\gamma_f^{(w)} = \text{softplus}(\rho_f^{(w)})$:
   $$\text{dev}_t^{(w)} = \gamma^{(w)} \odot \left( h_t - \sum_{j=0}^{w-1} k_j^{(w)} h_{t-j} \right)$$
   At initialization, the effective kernel $\delta_{\text{last}} - k^{(w)}$ has a zero sum ($\sum = 0$), acting as a multi-scale high-pass filter.
The $F(2+S) = 25 \times 5 = 125$ output channels are projected to hidden dimension $d=96$ via $\text{Linear}(125 \to 96) \to \text{LayerNorm} \to \text{GELU} \to \text{Dropout}(0.1)$.

### 3. Staggered Selective State-Space Backbone

The backbone consists of $L=4$ residual selective state-space blocks. Each block $\ell \in \{1, 2, 3, 4\}$ applies:
$$a_t = \sigma(W_a x_t + \beta_\ell), \quad b_t = W_b x_t, \quad c_t = W_c x_t$$
where $\beta_\ell$ is a per-channel bias initialized linearly across layers from $1.0$ (fast decay, bottom layer) to $-1.5$ (slow decay, top layer).
The hidden state evolves via the selective linear recursion:
$$h_t = a_t \odot h_{t-1} + b_t$$
$$y_t = W_y (c_t \odot h_t) + x_t$$
Evaluated causally using the Hillis-Steele associative scan in $\lceil \log_2 240 \rceil = 8$ parallel passes with $\mathcal{O}(T \log T)$ work and $\mathcal{O}(\log T)$ critical depth.

### 4. Four-Path Readout and Ranking Head

Final block output $u \in \mathbb{R}^{B \times T \times d}$ passes through LayerNorm and is aggregated into four parallel summary vectors:
1. Mean over time: $\bar{u} = \frac{1}{T} \sum_{t=1}^T u_t$.
2. Gated terminal step: $\sigma(g) \odot u_T$, where scalar gate $g$ is initialized to $-1.0$.
3. Fast exponential decay average: $\sum_{t=1}^T w_t^{(1)} u_t$ with weights $w_t \propto \lambda_1^{T-1-t}$, decay $\lambda_1 = \sigma(\theta_1)$ initialized to $0.50$.
4. Slow exponential decay average: $\sum_{t=1}^T w_t^{(2)} u_t$ with decay $\lambda_2 = \sigma(\theta_2)$ initialized to $0.88$.
The concatenated vector $v \in \mathbb{R}^{4d} = \mathbb{R}^{384}$ is divided by its root-mean-square, normalized by LayerNorm, and mapped to scalar score $s_{i,t}$ via a 3-layer MLP: $\text{Linear}(384 \to 96) \to \text{GELU} \to \text{Linear}(96 \to 48) \to \text{GELU} \to \text{Linear}(48 \to 1)$.

### 5. Multi-Objective Training Loss

Trained in daily batches representing the cross-section $n \approx 1000$ stocks. The loss combines four objectives:
$$\mathcal{L} = \text{MSE}(\hat{p}, y) - c_t \cdot \text{SoftSpearman}(\tilde{r}_p, \tilde{r}_y) - \text{Pearson}(\hat{p}, y) + 0.05 \cdot [\text{Kurtosis}(\hat{p}) - 3]_+$$
where $c_t$ ramps from $0.03$ to $0.30$ along a cosine schedule over training epochs, and $\tilde{r}_p$ is a differentiable soft-ranking proxy computed via pairwise sigmoids over a sub-sample of $\le 1300$ names.

## Required data

- **Universe:** Mid-capitalization Chinese A-shares (historical constituents of the CSI 1000 index), covering 2019-01-02 through 2024-12-31 ($1,456$ trading days, $878\text{--}999$ stocks/day, point-in-time membership, survivorship-bias free).
- **Timeframe & Bar Structure:** 5-minute intraday bars, exactly 48 bars per session ($09:30\text{--}11:30$, $13:00\text{--}15:00$ CST). Input tensor covers 5 consecutive trading days ($T=240$ bars).
- **Fields per Bar ($F=25$):**
  - OHLCV: Open, High, Low, Close, Volume, Turnover (CNY), Trade Count.
  - L2 Order Book Depth: 3 levels of Bid/Ask prices ($P_{\text{bid}}^{1..3}, P_{\text{ask}}^{1..3}$), Bid/Ask sizes ($V_{\text{bid}}^{1..3}, V_{\text{ask}}^{1..3}$), and Bid/Ask order counts ($N_{\text{bid}}^{1..3}, N_{\text{ask}}^{1..3}$).
- **Style Factor Regressors (8 Controls):**
  1. `size`: $\log(\text{mean 20-day turnover})$.
  2. `sizenl`: Cube of cross-sectional z-score of `size`.
  3. `liquidity`: $\log(\text{mean 5-day turnover}) - \log(\text{mean 60-day turnover})$.
  4. `resvol`: 20-day standard deviation of past log returns.
  5. `momentum`: 100-day cumulative log return ending 20 days prior ($t-120$ to $t-20$).
  6. `beta`: 60-day rolling regression slope against equal-weight market index.
  7. `strev`: 5-day cumulative log return reversal.
  8. `intravol`: 20-day average of daily mean high-low bar range normalized by close.

## Execution assumptions

- **Benchmark Prediction Target (Close-to-Close):** Next-day backward-adjusted close-to-close return $y_{i,t} = \frac{C_{i,t+1}^{\text{adj}}}{C_{i,t}^{\text{adj}}} - 1$.
- **Executable Target (Open-to-Close):** Next-day open-to-close return $y_{i,t}^{\text{exec}} = \frac{C_{i,t+1}}{O_{i,t+1}} - 1$.
- **Rebalancing Cadence:** Daily cross-sectional rebalance after market close ($15:00$ CST).
- **Portfolio Construction:** Decile long-short portfolio: equal-weighted Top $10\%$ minus equal-weighted Bottom $10\%$ based on style-residualized scores.
- **Frictional Costs:** Baseline diagnostic reports zero transaction costs, zero slippage, unconstrained shorting, and frictionless rebalancing.

## Evidence

### Source-reported

All quantitative figures below are directly reported by Chen, Zhang, et al. (arXiv:2608.28060v1, August 2026), evaluated on the held-out 2024 test year ($241$ trading days, $239,591$ stock-days):

1. **Test-Year Benchmark Comparison (Style-Residualized Metrics, 3 Random Seeds):**
   - **STRATA (244,633 parameters):**
     - **Rank IC:** $\mathbf{0.0728 \pm 0.0016}$ (**$+14.9\%$** above strongest baseline GRU).
     - **IC_IR:** $\mathbf{1.128 \pm 0.093}$ (vs GRU: $0.995 \pm 0.160$).
     - **Signal Long-Short Sharpe:** $\mathbf{12.85 \pm 0.77}$ (**$+17.7\%$** above strongest baseline GRU: $10.92 \pm 1.05$).
     - **Stress IC_IR (55 stress days):** $\mathbf{1.030 \pm 0.038}$ (**$+13.4\%$** above GRU: $0.909 \pm 0.081$).
   - **Baseline Comparisons (Matched to $244\text{k} \pm 5\%$ parameters):**
     - *MLP (247,873 params):* Rank IC $= 0.0485$, IC_IR $= 0.748$, Signal Sharpe $= 8.52$, Stress IC_IR $= 0.613$.
     - *TCN (246,145 params):* Rank IC $= 0.0586$, IC_IR $= 0.898$, Signal Sharpe $= 9.61$, Stress IC_IR $= 0.841$.
     - *Transformer (245,665 params):* Rank IC $= 0.0601$, IC_IR $= 0.909$, Signal Sharpe $= 10.37$, Stress IC_IR $= 0.875$.
     - *LSTM (244,993 params):* Rank IC $= 0.0612$, IC_IR $= 0.963$, Signal Sharpe $= 10.45$, Stress IC_IR $= 0.824$.
     - *Mamba (244,317 params, standard linear stem + mean/last pool):* Rank IC $= 0.0615$, IC_IR $= 0.960$, Signal Sharpe $= 10.38$, Stress IC_IR $= 0.812$.
     - *GRU (244,513 params):* Rank IC $= 0.0634$, IC_IR $= 0.995$, Signal Sharpe $= 10.92$, Stress IC_IR $= 0.909$.
   - **Statistical Significance:** Day-level paired Newey-West $t$-statistics (Bartlett, lag 5) between STRATA and all 6 baselines range from $\mathbf{4.40}$ to $\mathbf{6.29}$, all rejecting the null hypothesis at $\mathbf{p < 0.001}$.
   - **Component Contribution:** The gap between STRATA ($0.0728$) and Mamba ($0.0615$) confirms that the zero-sum convolutional stem, staggered decay biases, and 4-path readout provide an **$18.5\%$ relative performance boost** over the bare selective state-space backbone.

2. **Style Factor Exposure ($R^2_{\text{style}}$):**
   - STRATA's scores have an $R^2_{\text{style}}$ of only $\mathbf{0.172}$ against the 8 price-volume controls.
   - All five competitive sequence baselines exhibit higher style entanglement ($R^2_{\text{style}} \in [0.180, 0.220]$: GRU $0.207$, LSTM $0.218$, Transformer $0.180$, Mamba $0.203$). STRATA's superior IC is therefore not driven by hidden factor bets.

3. **Execution Timing Decomposition (Overnight vs. Executable Session):**
   - *Full Close-to-Close Spread:* $\mathbf{+73.9\text{ bps/day}}$ (STRATA).
   - *Overnight Gap Alone ($C_t \to O_{t+1}$):* $\mathbf{+75.6\text{ bps/day}}$ (Overnight captures $>100\%$ of the total spread).
   - *Executable Session ($O_{t+1} \to C_{t+1}$):*
     - Top decile daily return: $+6.0\text{ bps/day}$.
     - Bottom decile daily return: $+7.5\text{ bps/day}$.
     - **Net Long-Short Spread:** $\mathbf{-1.6\text{ bps/day}}$ (Newey-West $t = \mathbf{-0.37}$, statistically indistinguishable from zero).
     - Executable Rank IC remains positive ($\mathbf{0.0215}$, $+32.7\%$ over GRU: $0.0162$), but price reversal at the open completely eliminates trading profits.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Complete Failure of Executable Long-Short Trading:** When evaluated on actual executable prices (buying at Open and selling at Close on day $t+1$), the decile long-short spread collapses from $+73.9\text{ bps/day}$ to $-1.6\text{ bps/day}$ ($t=-0.37$). Stocks in the bottom decile gap down overnight but rebound strongly after the open ($+7.5\text{ bps}$), outperforming the top decile ($+6.0\text{ bps}$).
- **China A-Share Trading Constraints:** The paper explicitly acknowledges that Chinese A-shares prohibit intraday short-selling for most mid-caps, enforce strict $\pm 10\%$ daily price limits (which bind exactly on the strongest signal days, preventing execution), and levy stamp duty taxes ($0.05\%\text{--}0.10\%$) that would convert any marginal edge into severe losses.
- **Sensitivity to Overnight Gaps:** Any quantitative strategy claiming Sharpe $>10.0$ on daily bars from close-to-close targets is exploiting non-tradable overnight mark differences rather than executable alpha.

## Falsification plan

1. **Intraday Execution Timing Stress:** Implement delayed execution at 09:35, 10:00, and 14:30 CST (VWAP execution over the first 30 minutes). If the long-short spread remains negative or zero after deducting $5\text{ bps}$ round-trip transaction costs, the strategy is falsified as an executable equity alpha.
2. **Ablation of Zero-Sum Constraint:** Re-train STRATA by removing the zero-sum initialization constraint on the stem convolutions (using standard He/Glorot initialization). If style-residualized Rank IC drops to baseline Mamba levels ($\le 0.062$), the zero-sum high-pass mechanism is confirmed as the sole driver of level robustness.
3. **Turnover & Cost Hurdle:** Measure daily portfolio turnover. At an expected daily turnover of $40\%\text{--}80\%$, calculate net PnL under realistic bid-ask spread and commission schedules ($8\text{ bps}$ one-way). If net annualized Sharpe falls below $0.5$, reject deployment.
4. **Rejection Criterion:** Falsify and reject the trading model if out-of-sample executable open-to-close Rank IC drops below $0.01$ or if realized trading costs exceed the gross decile spread.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **24/7 Continuous Trading Advantage:** Unlike equity markets with artificial overnight gaps ($15:00$ to $09:30$), crypto perpetual markets trade continuously 24/7. The structural flaw of STRATA—where predictive edge sits in non-tradable overnight gaps—may be mitigated in crypto, because signals can be executed continuously at the exact close of every 5-minute candle.
- **Adaptation of Stem Kernel Scales:**
  - In equities, $\mathcal{S} = \{3, 12, 48\}$ bars represents 15m, 1h, and 1 full 4-hour trading session.
  - In crypto (where 1 day $= 288$ five-minute bars), the scale set must be adapted to $\mathcal{S}_{\text{crypto}} = \{12, 72, 288\}$ bars, representing 1 hour, 6 hours, and 24 hours.
- **Input Channels in Crypto:** The $F=25$ input channels map directly to crypto L2 order-book snapshots: Binance/Bybit provide top 5 bid/ask levels, trade counts, taker buy volume, and funding rates.
- **Execution Risks in Crypto:** High-frequency taker fees ($2\text{--}4\text{ bps}$) on Binance or Hyperliquid will erode rapid 5-minute signal turnover unless execution utilizes passive maker orders with queue estimation.

## Limitations

- **Prediction Benchmark vs. Tradable Strategy Gap:** The primary reported results (Sharpe $12.85$, Rank IC $0.0728$) are derived from an unexecutable close-to-close return target.
- **Absence of Fundamental & Alternative Controls:** The 8 style regressors are limited to price-volume metrics; industry classification, book-to-market, earnings quality, and institutional flow controls were omitted.
- **Single Market & Fixed Parameter Budget:** The model was tested exclusively on CSI 1000 Chinese equities; universality across US equities, foreign exchange, or crypto remains unproven.

## Implementation status

`not-implemented` in the quantitative production stack.

## Adoption boundary

Research capture only. A record being present in this repository does not constitute authorization for deployment, implementation in PyBroker/Nautilus, or allocation of capital in paper, testnet, or live trading.

## Related Wiki records

- `[[quant/phase8-regularized-nonlinear-ml-toolbox-2026-08-28]]`
- `[[quant/phase8-financial-ml-sample-leakage-contract-2026-08-28]]`
- `[[quant/phase9-factor-taxonomy-and-cross-sectional-sorts-2026-08-28]]`
- `[[quant/alpha-transforms-decay-neutralization-2026-08-28]]`
- `[[quant/backtest-overfitting-pbo-cscv-2026-08-27]]`

## Sources

1. Mingju Chen and Enze Zhang, *"A Compact Selective State-Space Model for Cross-Sectional Stock Return Ranking from Raw Intraday Bars"*, arXiv preprint `arXiv:2608.28060v1 [cs.LG]`, August 28, 2026. DOI: [10.48550/arXiv.2608.28060](https://doi.org/10.48550/arXiv.2608.28060). Stable URL: [https://arxiv.org/abs/2608.28060](https://arxiv.org/abs/2608.28060).
