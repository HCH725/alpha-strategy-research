---
schema: strategy-research-record-v1
title: "Continuous Timing Signals for Growth-Defensive Style Allocation: Macro Conditioning, Risk Matching, and Walk-Forward Evidence"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - style-allocation
  - dynamic-asset-allocation
  - factor-timing
  - macro-momentum
  - etf-portfolios
  - walk-forward-validation
  - risk-budgeting
status: research-only
confidence: high
source_as_of: 2026-05-29
sources:
  - "Zheli Xiong, 'Continuous Timing Signals for Growth-Defensive Style Allocation: Factor Attribution, Risk Matching, Out-of-Sample Evidence, and a Bond/Credit Incremental Extension', arXiv:2605.20636v2 [q-fin.PM], May 29, 2026. DOI: 10.48550/arXiv.2605.20636. https://arxiv.org/abs/2605.20636"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Continuous Timing Signals for Growth-Defensive Style Allocation: Macro Conditioning, Risk Matching, and Walk-Forward Evidence

## Provenance

- **Primary Paper Source:** Zheli Xiong (University of Science and Technology of China, USTC), *"Continuous Timing Signals for Growth–Defensive Style Allocation: Factor Attribution, Risk Matching, Out-of-Sample Evidence, and a Bond/Credit Incremental Extension"*, arXiv preprint `arXiv:2605.20636v2 [q-fin.PM]`, May 20, 2026 (version 2 revised May 29, 2026). DOI: [10.48550/arXiv.2605.20636](https://doi.org/10.48550/arXiv.2605.20636). Stable URL: [https://arxiv.org/abs/2605.20636](https://arxiv.org/abs/2605.20636). Full HTML text: [https://arxiv.org/html/2605.20636v2](https://arxiv.org/html/2605.20636v2).
- **Author Contact:** Corresponding author: Zheli Xiong (`zlxiong@mail.ustc.edu.cn`).
- **Research Setting:** The study examines dynamic asset allocation between a growth/technology basket ($G$) and a defensive income/value basket ($D$) using observable macro-market signals. The empirical analysis covers June 28, 2017 to May 15, 2026, evaluating 10 bps transaction costs across expanding and rolling walk-forward cross-validation windows.

## Economic mechanism

### Source-reported

Dynamic style rotation strategies often rely on heuristic binary state switches (such as discrete "bull/bear" regime labels or moving average crossovers) that introduce whipsaw costs, arbitrary parameter cutoffs, and sudden portfolio reallocations. 

Fama-French five-factor plus momentum attribution reveals that the long-short growth-versus-defensive spread portfolio ($G - D$) is a recognizable factor bundle rather than an unexplained return anomaly: it exhibits a market beta of 0.273, an HML (value) beta of -0.552, a momentum beta of 0.117, and an annualized alpha of 1.95% with a Newey-West t-statistic of only 0.81. Because the spread does not generate statistically significant standalone alpha, the objective is not anomaly discovery, but rather systematic risk timing of known style exposures.

The author proposes replacing discrete regime switches with a continuous smooth scoring framework:
1. **Rate Relief ($r_t$):** Falling 10-year Treasury yields ($\Delta TNX$) alleviate discount rate pressure on long-duration growth cash flows.
2. **Equity Drawdown ($d_t$):** Deeper SPY drawdowns signal oversold broad-market conditions where high-beta growth assets exhibit asymmetric rebound elasticity.
3. **Volatility Stress Relief ($i_1, i_2$):** Blending elevated VIX percentiles with falling 21-day VIX changes captures the transition from acute panic to volatility normalization.
4. **Growth Crowding Penalty ($i_3, i_4$):** Extended medium-term growth outperformance ($g126$) during subdued volatility (low VIX) and quiet rate regimes signals crowded speculative positioning vulnerable to violent factor unwinds.

### Research interpretation

The core falsifiable hypothesis is that **modulating growth versus defensive allocations through a continuous, softplus-smoothed macro composite score yields higher risk-adjusted returns (Sharpe 1.01 vs 0.91) and superior drawdown protection (-31.63% vs -33.59%) relative to a 50/50 baseline, while preserving growth participation during post-crisis recoveries without incurring excessive turnover drag**:

- **Continuous Softplus Regularization:** Standard indicator combinations suffer from discontinuous cliff effects around arbitrary thresholds. Using $softplus(x) = \log(1 + e^x)$ provides non-negative, continuously differentiable exposure scaling, preventing discrete turnover spikes.
- **Asymmetric Factor Timing:** Long-duration growth stocks are fundamentally exposed to discount rate shocks and speculative crowding. Penalizing allocation when growth is extended under low-volatility conditions prevents holding peak valuation risk, while tilting toward growth during rate cuts and post-drawdown recoveries captures multiple expansion.
- **Incremental Credit Channel:** Credit spreads (e.g., Baa minus 10-year Treasury) reflect corporate refinancing stress. Interacting rate cuts with credit relief confirms whether low interest rates stem from healthy monetary easing or distressed credit flight.

*Ported Hypothesis Note:* This mechanism was evaluated on US equity ETFs and macro fixed income/volatility indices. Any application to cryptocurrency sectors (e.g. Layer-1 speculative tokens vs Bitcoin/stablecoin reserve assets) is an adapted, unproven research interpretation.

## Signal

### 1. Asset Basket Construction
- **Growth/Technology Basket ($G$):** Equal-weighted daily basket of 5 liquid ETFs:
  $$G = \frac{1}{5}(\text{QQQ} + \text{XLK} + \text{VGT} + \text{SPYG} + \text{VUG})$$
- **Defensive Income Basket ($D$):** Equal-weighted daily basket of 5 income/value ETFs:
  $$D = \frac{1}{5}(\text{SCHD} + \text{VYM} + \text{VTV} + \text{FDVV} + \text{COWZ})$$
- **Relative Spread Return:** $R_t^{G-D} = R_t^G - R_t^D$.

### 2. Direction-Normalized Input Features
At market close on day $t$, continuous standardized inputs are computed:
- **Rate Relief:**
  $$r_t = -z(\Delta TNX_{21, t})$$
  where $\Delta TNX_{21, t} = TNX_t - TNX_{t-21}$ is the 21-day change in the 10-year Treasury yield, and $z(\cdot)$ is an expanding-window Z-score.
- **SPY Drawdown Depth:**
  $$d_t = -z(SPYDrawdown_t), \quad SPYDrawdown_t = \frac{SPY_t}{\max_{s \le t} SPY_s} - 1 \le 0$$
- **High VIX Percentile:**
  $$vh_t = z(VIXPercentile_{756, t})$$
  where $VIXPercentile_{756, t}$ is the percentile rank of $VIX_t$ over a 756-day (3-year) rolling window.
- **VIX Relief:**
  $$vr_t = -z(\Delta VIX_{21, t}), \quad \Delta VIX_{21, t} = VIX_t - VIX_{t-21}$$
- **Growth Extension (126-day Trailing Momentum):**
  $$g126_t = z(GDTrailing126_t), \quad GDTrailing126_t = \frac{G_t / G_{t-126}}{D_t / D_{t-126}} - 1$$

### 3. Smooth Component Transformations
Using $softplus_\tau(x) = \tau \log(1 + \exp(x / \tau))$ with scale parameter $\tau = 1.0$:
- $HighVIX_t = softplus(vh_t)$
- $VIXRelief_t = softplus(vr_t)$
- $LowVIX_t = softplus(-vh_t)$
- $GrowthExt_t = softplus(g126_t)$
- $RateQuiet_t = \exp(-0.5 r_t^2)$

### 4. Non-Linear Interaction Terms
- **Stress Relief Terms:**
  $$i1_t = r_t \cdot vh_t$$
  $$i2_t = HighVIX_t \cdot VIXRelief_t$$
- **Crowded Growth Penalties:**
  $$i3_t = GrowthExt_t \cdot LowVIX_t$$
  $$i4_t = GrowthExt_t \cdot LowVIX_t \cdot RateQuiet_t$$

### 5. Composite Score Aggregation
- **Core Score:**
  $$CoreScore_t = \alpha r_t + (1 - \alpha) d_t$$
- **Stress Score:**
  $$StressScore_t = 0.5 z(i1_t) + 0.5 z(i2_t)$$
- **Crowded Score:**
  $$CrowdedScore_t = 0.5 z(i3_t) + 0.5 z(i4_t)$$
- **Raw Policy Score:**
  $$RawScore_t = CoreScore_t + \lambda_s StressScore_t - \lambda_c CrowdedScore_t$$
- The raw score is standardized via an expanding Z-score to produce $\widetilde{Score}_t$.

### 6. Target Allocation Mapping & EWMA Smoothing
- **Target Weight in Growth Basket $G$:**
  $$w_{G, t}^{\text{target}} = 0.5 + MaxTilt \cdot \tanh\left(\frac{\widetilde{Score}_t}{\tau_w}\right)$$
  where target weight in Defensive Basket $D$ is $w_{D, t}^{\text{target}} = 1 - w_{G, t}^{\text{target}}$.
- **EWMA Realized Weight Smoothing:**
  $$w_{G, t} = (1 - \eta) w_{G, t-1} + \eta w_{G, t}^{\text{target}}$$
  $$w_{D, t} = 1 - w_{G, t}$$

### 7. Optimal Calibrated Parameters
From the expanded parameter sensitivity grid (Section 6.2, Table 6):
- Rate/Drawdown weight: $\alpha = 0.50$
- Stress relief multiplier: $\lambda_s = 0.50$
- Crowding penalty multiplier: $\lambda_c = 0.05$
- Maximum active tilt: $MaxTilt = 50\%$ (allowing $w_G \in [0.0, 1.0]$)
- Tanh temperature scale: $\tau_w = 0.75$
- EWMA smoothing rate: $\eta = 0.05$

### 8. Optional Incremental Bond/Credit Overlay
In Section 11, adding Moody's Baa minus 10-year Treasury credit spread ($CS_t$) via:
$$CreditScore_t = \lambda_{\text{credit}} z(- \Delta CS_{21, t}) + \lambda_{r \times cs} z(r_t \cdot z(CS_t))$$
with $\lambda_{\text{credit}} = 0.10$ and $\lambda_{r \times cs} = 0.50$.

## Required data

- **Instruments:**
  - Growth ETFs: QQQ, XLK, VGT, SPYG, VUG (US Equities).
  - Defensive ETFs: SCHD, VYM, VTV, FDVV, COWZ (US Equities).
  - Benchmark & Conditioning Assets: SPY, CBOE VIX Index, 10-Year US Treasury Yield (TNX), Moody's Seasoned Baa Corporate Bond Yield (FRED: BAA10Y).
- **Venue:** US Equity and Index Markets (NYSE / NASDAQ / CBOE).
- **Timeframe:** Daily close-to-close bars.
- **Fields:** Adjusted closing prices, daily returns, rolling index values.
- **Point-in-Time Hygiene:** Scores are formed strictly using information available at the market close of day $t$; weights are updated and trades executed at open/close of day $t+1$. All Z-scores use expanding windows to eliminate lookahead bias.

## Execution assumptions

- **Rebalancing Cadence:** Daily weight adjustment based on smoothed EWMA target $w_{G, t}$.
- **Transaction Costs:** Flat 10 bps (0.10%) per two-way trade volume:
  $$Cost_t = 2 |\Delta w_{G, t}| \times \frac{10}{10000}$$
  Stress-tested at 20 bps in sensitivity tables.
- **Slippage & Market Impact:** Modeled as covered by the 10 bps transaction fee assumption; ETFs evaluated have average daily volume exceeding $100M, ensuring high capacity.
- **Borrow & Leverage:** Long-only portfolio ($w_G + w_D = 1.0$, $w_G \ge 0, w_D \ge 0$); no leverage, margin borrowing, or shorting required.

## Evidence

### Source-reported

All performance figures below are directly reported by Zheli Xiong (arXiv:2605.20636v2, May 2026) across the aligned sample period from June 28, 2017 to May 15, 2026 under 10 bps transaction costs:

#### Table 7: Aligned Strategy Comparison (2017-06-28 to 2026-05-15, 10bp Cost)

| Strategy / Benchmark | Final Wealth | CAGR | Volatility | Sharpe Ratio | Sortino Ratio | Max Drawdown | Annual Turnover | Average $G$ Weight |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Selected Smooth Score** | **4.71** | **19.24%** | 19.29% | **1.01** | **1.22** | **-31.63%** | 469.67% | 45.06% |
| Matched TNX-only | 4.23 | 17.80% | 19.33% | 0.94 | 1.13 | -31.31% | 566.69% | 47.48% |
| Matched Core-only | 4.25 | 17.84% | 18.94% | 0.96 | 1.15 | -31.98% | 410.19% | 37.18% |
| Fixed-Structure 50% Tilt | 4.64 | 19.02% | 19.45% | 0.99 | 1.20 | -31.72% | 465.87% | 46.92% |
| 50/50 G/D Benchmark | 4.02 | 17.12% | 19.34% | 0.91 | 1.08 | -33.59% | 0.00% | 50.00% |
| 100% Growth ($G$) | 5.49 | 21.34% | 23.53% | 0.94 | 1.17 | -34.35% | 0.00% | 100.00% |
| 100% Defensive ($D$) | 2.80 | 12.42% | 17.53% | 0.76 | 0.86 | -36.71% | 0.00% | 0.00% |
| SPY Benchmark | 3.49 | 15.25% | 18.74% | 0.85 | 0.98 | -33.72% | 0.00% | – |

#### Table 9: Risk-Matched Comparison
- When 100% $G$ is volatility-matched to the Smooth Strategy's 19.29% annualized volatility (requiring an 81.95% scaling weight):
  - **Vol-Matched 100% $G$:** CAGR 17.66%, Sharpe 0.94, Max DD -28.73%.
  - **Selected Smooth Score:** CAGR 19.24%, Sharpe 1.01, Max DD -31.63% (**+1.58% annual excess return over vol-matched growth**).

#### Table 10 & 11: Out-of-Sample Walk-Forward Validations
- **Full OOS Walk-Forward (2018-06-28 to 2026-05-15):**
  - Expanding Walk-Forward: CAGR 18.64%, Sharpe 0.96, Max DD -32.93%, Turnover 332.21% (improves over 50/50 G/D: CAGR 17.10%, Sharpe 0.89, Max DD -33.59%, and SPY: CAGR 15.45%, Sharpe 0.84).
- **Post-2022 Regime Validation (2022-01-03 to 2026-05-15):**
  - Expanding Walk-Forward: CAGR 15.30%, Sharpe 0.90, Max DD -19.89% (nearly matches 100% $G$'s 15.45% CAGR while cutting maximum drawdown by **14.03 percentage points** from -33.92% to -19.89%).

#### Table 12: Incremental Credit Extension
- Adding the Baa/Aaa credit spread overlay improves the Best Local policy:
  - CAGR rises from 19.24% to **19.80%**;
  - Sharpe rises from 1.01 to **1.04**;
  - Annual turnover drops from 469.67% to **410.23%**.

### Independently reproduced

`not independently reproduced`.

### Negative evidence

- The dynamic strategy does **not** outperform pure 100% $G$ in unadjusted raw CAGR (19.24% vs 21.34%). In secular bull runs driven by large-cap tech multiple expansion, static high growth exposure outperforms any timing strategy.
- Annual turnover is substantial (410% to 470%), meaning that if transaction costs or execution slippage exceed 25 bps, the net Sharpe ratio converges to the static 50/50 benchmark.
- Replacement-style credit models (attempting to use credit variables in place of equity/rate signals) underperformed the original core score (Sharpe 0.94 vs 1.01), proving that credit spreads are only useful as a minor secondary overlay ($\lambda = 0.10$).

## Falsification plan

1. **Stationary Random Placebo Test:** Replace actual $TNX$, $VIX$, and $SPYDrawdown$ signals with drift-matched synthetic random walks. If the resulting synthetic score generates a Sharpe ratio $\ge 0.98$, the empirical outperformance is an artifact of curve fitting on the expanding Z-score.
2. **Cost Stress Boundary Test:** Increase assumed transaction fees from 10 bps to 25 bps and 40 bps. If net CAGR drops below 17.12% (the static 50/50 return), the strategy's trading velocity is unviable under institutional trading friction.
3. **Parameter Perturbation Grid:** Perturb parameters $\alpha \in [0.3, 0.7]$, $\lambda_s \in [0.2, 0.6]$, $\tau_w \in [0.5, 1.2]$, and $\eta \in [0.02, 0.08]$. A drop in Sharpe of greater than 0.20 indicates fragile parameter tuning.
4. **Subperiod Breakdown:** Evaluate across the 2022 rate hike regime exclusively. The strategy must maintain a maximum drawdown strictly shallower than -25% (versus -33.9% for 100% $G$). Failure to protect drawdown during rising yield regimes disconfirms the discount-rate timing thesis.

## Crypto portability

- **Classification:** `adapted` / `unproven`.
- **Portability Thesis:** The economic intuition (timing high-beta speculative growth assets vs low-beta defensive stores of value) translates to crypto portfolio management by constructing:
  - Speculative/Growth Basket $G_{\text{crypto}}$: High-beta Layer-1 / DeFi tokens (e.g. SOL, AVAX, NEAR, SUI).
  - Defensive Basket $D_{\text{crypto}}$: Bitcoin (BTC) + USD stablecoins (USDT/USDC).
- **Macro Proxy Replacements:**
  - Replace 10-year Treasury yields ($TNX$) with annualized crypto perpetual funding rates or decentralized lending rates (Aave USDC supply APY).
  - Replace VIX with Bitcoin Deribit Implied Volatility Index (DVOL).
  - Replace SPY Drawdown with BTC Drawdown from all-time highs.
- **Crypto-Specific Obstacles:**
  - **Absence of True Defensive Equities:** During acute crypto liquidity crunches (e.g. March 2020, November 2022), correlations across all crypto tokens converge to 1.0, eliminating defensive basket diversification unless allocated significantly to cash/stablecoins.
  - **High Rebalancing Friction:** Daily rebalancing across a 10-token crypto universe incurs on-chain gas costs or CEX taker fees that may erode alpha at 400%+ annual turnover.

## Limitations

- **Benchmarking Distinction:** The strategy timed an existing factor spread ($G - D$) and did not discover a novel orthogonal anomaly ($t = 0.81$ on Fama-French alpha).
- **Turnover Overhead:** Requires daily portfolio adjustments yielding ~470% annual turnover.
- **Regime Dependence:** A significant portion of outperformance stems from sidestepping the 2022 tech drawdown; in uninterrupted one-way bull markets, the strategy lags static growth exposure.
- **Survivorship in ETF Baskets:** ETF selection was established retrospectively using prominent liquid funds; while liquid today, newer funds (COWZ, FDVV) have shorter histories prior to 2016.

## Implementation status

- `not-implemented`: No implementation or backtest has been performed within this repository's research pipeline, PyBroker, or NautilusTrader.
- The concept remains exploratory research material only.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- This record serves solely to capture the mathematical formulation, empirical claims, and known limitations of the continuous style allocation model. It does not authorize paper trading, live trading, or testnet deployment.

## Related Wiki records

- [[quant/cross-sectional-crypto-momentum-2026-08-31]]
- [[quant/futures-trend-following-autocorrelation-drift-decomposition-2026-09-02]]
- [[quant/dynamic-portfolio-optimization-cvar-stochastic-control-hjb-2026-09-02]]
- [[quant/sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02]]

## Sources

1. Zheli Xiong, *"Continuous Timing Signals for Growth–Defensive Style Allocation: Factor Attribution, Risk Matching, Out-of-Sample Evidence, and a Bond/Credit Incremental Extension"*, arXiv preprint `arXiv:2605.20636v2 [q-fin.PM]`, May 20, 2026 (revised May 29, 2026). DOI: [10.48550/arXiv.2605.20636](https://doi.org/10.48550/arXiv.2605.20636). Stable URL: [https://arxiv.org/abs/2605.20636](https://arxiv.org/abs/2605.20636). Full HTML: [https://arxiv.org/html/2605.20636v2](https://arxiv.org/html/2605.20636v2).
2. Fama, E. F., & French, K. R. (2015). *"A five-factor asset pricing model"*, Journal of Financial Economics, 116(1), pp. 1–22.
3. Carhart, M. M. (1997). *"On persistence in mutual fund performance"*, The Journal of Finance, 52(1), pp. 57–82.
