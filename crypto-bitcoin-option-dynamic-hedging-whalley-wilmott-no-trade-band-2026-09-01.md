---
schema: strategy-research-record-v1
title: Bitcoin Option Dynamic Hedging with Whalley-Wilmott Asymptotic No-Trade Bands under Transaction Costs
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto-options
  - deribit
  - delta-hedging
  - deep-hedging
  - whalley-wilmott
  - transaction-costs
  - cvar-optimization
status: research-only
confidence: high
source_as_of: 2026-08
sources:
  - "Sheryan Kumar, 'Deep Hedging Under Realistic Market Frictions: A Regime-Conditional Empirical Study of Dynamic Option Hedging on Bitcoin Options', arXiv:2608.29025v1 [q-fin.CP, q-fin.TR], August 2026. DOI: 10.48550/arXiv.2608.29025. https://arxiv.org/abs/2608.29025"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Option Dynamic Hedging with Whalley-Wilmott Asymptotic No-Trade Bands under Transaction Costs

## Provenance

- **Primary Source:** Sheryan Kumar, "Deep Hedging Under Realistic Market Frictions: A Regime-Conditional Empirical Study of Dynamic Option Hedging on Bitcoin Options", arXiv:2608.29025v1 [q-fin.CP, q-fin.TR], August 29, 2026. DOI: [10.48550/arXiv.2608.29025](https://doi.org/10.48550/arXiv.2608.29025). Full text: [https://arxiv.org/html/2608.29025v1](https://arxiv.org/html/2608.29025v1).
- **Dataset:** Deribit historical BTC options order-book-derived tick-level options chain snapshots via Tardis.dev, covering 61 monthly first-of-month snapshots from January 2020 through December 2024.
- **Sample Filtering:** Starting from 892,912 raw hourly rows across 22,866 unique instruments:
  1. Two-sided market liquidity filter (dropped rows lacking both bid and ask quotes, removing 27.0% of data).
  2. Moneyness filter ($S/K \in [0.70, 1.30]$, retaining liquid near-the-money options, dropping deep OTM/ITM contracts where bid-ask spreads frequently exceed 50% of mid-price).
  3. Time-to-maturity filter ($T \in [1\text{ day}, 90\text{ days}]$).
  4. Non-zero open interest filter ($OI > 0$).
- **Partition:** Total 23,988 valid hedging episodes of 24 hourly rebalancing steps:
  - Training set: January 2020 to December 2022 (36 sampled days, 8,922 episodes).
  - Validation set: January 2023 to August 2023 (8 sampled days, 3,520 episodes).
  - Out-of-sample test set: September 2023 to December 2024 (16 sampled days, 11,546 episodes).

## Economic mechanism

### Source-reported

1. **Continuous Delta Hedging Drag:** Under classical Black-Scholes delta hedging, an option seller rebalances continuously at every time interval $\Delta t$. In the presence of proportional transaction costs $k > 0$, total transaction costs scale as $\mathcal{O}(1/\sqrt{\Delta t})$, rendering continuous rebalancing prohibitively expensive and economically suboptimal.
2. **Leland Volatility Adjustment vs. Asymptotic No-Trade Bands:** Leland (1985) attempts to absorb transaction costs by inflating volatility ($\sigma_{\mathrm{adj}} = \sigma\sqrt{1 + \sqrt{2/\pi} \frac{k}{\sigma\sqrt{\Delta t}}}$), but continues to rebalance at every discrete step without reducing turnover. Whalley & Wilmott (1997) derive an asymptotic optimal impulse control policy that establishes a state-dependent no-trade band around the Black-Scholes delta: rebalancing is executed only when the tracking error breaches the boundary, trading strictly to the nearest band edge.
3. **Deep Hedging Over-Trading Failure:** Deep reinforcement learning / neural network hedging policies (Buehler et al., 2019) parameterized with LSTM and feedforward networks lack structural inductive bias toward sparsity. When trained on empirical crypto options data under CVaR loss, unconstrained neural networks fail to learn discrete no-trade regions, over-trading into crypto volatility bursts and achieving trade counts statistically indistinguishable from naive continuous rebalancing (~20.4 out of 24 hourly steps).

### Research interpretation

The falsifiable thesis is a **frictional gamma-cost optimization mechanism for crypto options market makers and delta hedgers**:
1. **Microstructure Noise vs. Fundamental Delta:** In crypto markets with high volatility and frequent microstructure price oscillation, continuous hourly delta adjustments track high-frequency noise rather than true directional drift.
2. **Explicit Gamma-Scaled Thresholding:** The Whalley-Wilmott band half-width $H = \left(\frac{3 k S^2 \Gamma^2}{2 \lambda}\right)^{1/3}$ expands during high underlying spot prices $S$ and high option gamma $\Gamma$, effectively suppressing small, costly rebalances when gamma is elevated unless the displacement exceeds the cost penalty.
3. **Sparsity as an Inductive Bias:** Model-free neural policies without hard-coded action deadbands overfit gradient paths and incur severe transaction cost drag (mean cost 9.43–9.97 vs. 7.91 for Whalley-Wilmott), proving that structural analytical no-trade bands dominate unconstrained deep hedging under realistic crypto exchange fees.

## Signal

### 1. Classical Delta & Gamma Formulation

For a short European option with strike $K$, time-to-maturity $T$ (years), spot price $S_t$, implied volatility $\sigma = \text{mark\_iv}$, and crypto risk-free rate $r = 0$:
$$d_1 = \frac{\ln(S/K) + (\sigma^2 / 2) T}{\sigma \sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}$$
$$\delta_{\mathrm{BS}} = \begin{cases} \Phi(d_1) & \text{for Call} \\ \Phi(d_1) - 1 & \text{for Put} \end{cases}, \quad \Gamma = \frac{\phi(d_1)}{S \sigma \sqrt{T}}$$

### 2. Whalley-Wilmott Asymptotic No-Trade Band Policy

Given round-trip transaction cost rate $k = 0.0005$ (5 bps) and risk aversion $\lambda = 60$, compute the dynamic half-width $H_t$:
$$H_t = \left(\frac{3 k S_t^2 \Gamma_t^2}{2 \lambda}\right)^{1/3}$$
- Lower band: $\underline{\delta}_t = \delta_{\mathrm{BS}, t} - H_t$
- Upper band: $\bar{\delta}_t = \delta_{\mathrm{BS}, t} + H_t$

**Rebalancing Rule at hourly step $t$ given current hedge position $\delta_{t-1}$:**
$$\delta_t = \begin{cases}
\underline{\delta}_t & \text{if } \delta_{t-1} < \underline{\delta}_t \quad (\text{buy underlying to lower boundary}) \\
\bar{\delta}_t & \text{if } \delta_{t-1} > \bar{\delta}_t \quad (\text{sell underlying to upper boundary}) \\
\delta_{t-1} & \text{if } \underline{\delta}_t \le \delta_{t-1} \le \bar{\delta}_t \quad (\text{no-trade zone: hold existing position})
\end{cases}$$

### 3. Deep Hedging Benchmark Architectures (Evaluated in Study)

- **Input State ($d=5$):** Moneyness $S_t/K$, time-to-maturity $T_t$, implied volatility $\sigma_t$ (capped at 300%), contemporaneous $\delta_{\mathrm{BS}, t}$, and current hedge position $\delta_{t-1}$.
- **Network Configurations:**
  - **LSTM v1:** 2-layer LSTM (hidden size 64) trained with CVaR loss: $\mathcal{L}_{\mathrm{CVaR}}(\Pi) = \text{CVaR}_{0.95}(-\Pi)$.
  - **LSTM v2:** Same LSTM with added turnover penalty: $\mathcal{L} = \mathcal{L}_{\mathrm{CVaR}}(\Pi) + \beta \sum_{t=1}^T |\delta_t - \delta_{t-1}|$.
  - **Feedforward:** 3-layer MLP with 4-step lookback window and $20\times$ turnover penalty weight.

## Required data

- **Instruments:** Deribit BTC options (Call and Put contracts across all listed strikes and expiries) and BTC spot / perpetual price feeds.
- **Quotes & Greeks:** Hourly order book snapshots (bid, ask, mid-price $V_t$, quoted mark implied volatility $\text{mark\_iv}$, open interest).
- **Timeframe:** Hourly sampling cadence ($\Delta t = 1/8760\text{ year} \approx 1\text{ hour}$), 24 hourly steps per daily hedging episode.
- **Risk-Free Rate:** $r = 0$ (standard crypto derivatives market convention).

## Execution assumptions

- **Exposure:** Short single option position (seller perspective).
- **Hedging Instrument:** BTC underlying spot or linear perpetual futures.
- **Transaction Cost Model:** Proportional round-trip cost $k = 5\text{ bps}$ ($0.0005$), applied as half-rate $k/2 = 2.5\text{ bps}$ per single execution leg:
  $$C_t = |\delta_t - \delta_{t-1}| S_t \frac{k}{2}$$
- **P&L Formulation:**
  - Option mark-to-market: $\text{P\&L}_{\mathrm{opt}, t} = -(V_t - V_{t-1})$
  - Hedge asset P&L: $\text{P\&L}_{\mathrm{hedge}, t} = \delta_{t-1} (S_t - S_{t-1})$
  - Net Episode Terminal Error: $\Pi = \sum_{t=1}^T (\text{P\&L}_{\mathrm{opt}, t} + \text{P\&L}_{\mathrm{hedge}, t} - C_t)$
- **Execution Timing:** Next-bar mid-price fill at discrete hourly step boundaries.

## Evidence

### Source-reported

All figures below are directly reported by Sheryan Kumar (arXiv:2608.29025v1, August 2026) across 11,546 out-of-sample test episodes (September 2023 – December 2024, 16 sampled trading day blocks):

#### 1. Out-of-Sample Performance Summary (Table 1, 11,546 Episodes)

| Strategy | Mean P&L (USD) | 95% CVaR (USD) | Mean Cost (USD) | Mean Turnover | Mean # Trades / Episode |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Whalley-Wilmott (WW)** | **-30.16** | **-864.23** | **7.91** | **0.545** | **2.47** |
| **Black-Scholes Delta** | -38.82 | -885.24 | 9.70 | 0.668 | 20.40 |
| **Leland Adjusted Vol** | -38.91 | -886.36 | 9.68 | 0.666 | 20.41 |
| **Deep Hedge (LSTM v1)** | -47.34 | -966.23 | 9.97 | 0.685 | 20.44 |
| **Deep Hedge (LSTM v2)** | -47.24 | -976.87 | 9.43 | 0.647 | 20.44 |
| **Deep Hedge (Feedforward)** | -50.90 | -994.85 | 9.63 | 0.664 | 20.44 |

#### 2. Block Bootstrap Statistical Significance (Table 2 & Table 3, 5,000 Resamples, 16 Day Blocks)

- **Whalley-Wilmott vs. BS Delta Cost:** Mean cost difference $-1.79\text{ USD}$, 95% CI $[-2.21, -1.39]$, $p < 0.0001$ (statistically significant cost reduction).
- **Whalley-Wilmott vs. BS Delta P&L:** Mean P&L difference $+8.66\text{ USD}$, 95% CI $[-3.36, 20.74]$, $p = 0.164$.
- **Whalley-Wilmott vs. Leland P&L:** Mean P&L difference $+8.75\text{ USD}$, 95% CI $[-2.95, 20.73]$, $p = 0.154$.
- **LSTM v2 vs. Whalley-Wilmott P&L:** Mean P&L difference $-17.08\text{ USD}$, 95% CI $[-30.39, -4.91]$, $p = 0.0044$ (LSTM v2 significantly underperforms WW).
- **LSTM v2 vs. Whalley-Wilmott Cost:** Mean cost difference $+1.52\text{ USD}$, 95% CI $[1.14, 1.92]$, $p < 0.0001$ (LSTM v2 incurs significantly higher friction).
- **Feedforward vs. Whalley-Wilmott P&L:** Mean P&L difference $-20.74\text{ USD}$, 95% CI $[-33.72, -7.31]$, $p = 0.0044$.
- **Feedforward vs. LSTM v2 P&L:** Mean P&L difference $-3.66\text{ USD}$, 95% CI $[-14.89, 8.07]$, $p = 0.506$ (architecture change does not rescue deep hedging).

#### 3. Validation Set Baseline Check (Table 4, Jan–Aug 2023, 3,520 Episodes)

- In the calmer validation period:
  - BS delta: Mean P&L $-4.94$, 95% CVaR $-353.55$, Mean cost $4.02$, Mean trades $18.08$.
  - Leland: Mean P&L $-4.81$, 95% CVaR $-352.87$, Mean cost $4.02$, Mean trades $18.08$.
  - Whalley-Wilmott: Mean P&L $-5.06$, 95% CVaR $-358.26$, Mean cost $3.50$, Mean trades $2.06$.
  - Result: In calm regimes, Whalley-Wilmott maintains its massive trade frequency and cost reduction (2.06 vs 18.08 trades) with near-identical P&L/CVaR, while in volatile trending regimes (test set) its cost savings generate superior net P&L.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Unconstrained Deep Hedging Failure:** Across all three neural configurations (LSTM v1, LSTM v2 with turnover penalty, Feedforward with $20\times$ penalty), deep hedging policies converged to trading ~20.44 out of 24 hourly steps, failing to discover the no-trade band and underperforming classical benchmarks on P&L, CVaR, turnover, and cost.
- **Leland Volatility Adjustment Ineffectiveness:** Leland's continuous formula achieved negligible cost reduction (9.68 vs 9.70 USD) and identical trade count (20.41 vs 20.40) compared to raw Black-Scholes, because adjusting volatility without introducing a no-trade band does not reduce rebalancing turnover.
- **Data Scarcity for Neural Approximators:** Training on 8,922 empirical episodes (vs. $10^5\text{--}10^6$ synthetic paths in theoretical deep hedging literature) proved insufficient for gradient descent to learn sparse activation boundaries without hard-coded threshold priors.

## Falsification plan

1. **Transaction Cost Sensitivity Threshold:** Run Whalley-Wilmott vs. Black-Scholes across a transaction cost sweep $k \in [0.5\text{ bps}, 20\text{ bps}]$. If Whalley-Wilmott's net P&L advantage degrades below zero when $k \ge 3\text{ bps}$, reject the thesis that no-trade bands provide robust friction mitigation in crypto.
2. **Risk-Aversion Parameter Ablation:** Sweep $\lambda \in [10, 300]$. If hedging variance / 95% CVaR explodes non-linearly for $\lambda \in [40, 100]$, invalidate the empirical calibration of $\lambda = 60$.
3. **High-Frequency Intraday Sampling (5-Minute / 1-Minute Grid):** Test Whalley-Wilmott on 5-minute Deribit order book feeds. If the band triggers rapid chattering at the boundaries due to microstructure bid-ask bounce, verify whether hysteresis bands ($\underline{\delta} - \epsilon, \bar{\delta} + \epsilon$) are required.
4. **Structural Deep Hedging Gating Test:** Implement an explicit Hard-Threshold / Gated Neural Policy (e.g., parameterized policy with learned band width $H_{\theta}(S, \Gamma)$). If the gated network fails to match Whalley-Wilmott P&L and cost, reject the hypothesis that lack of structural inductive bias was the primary cause of deep hedging underperformance.

## Crypto portability

`direct`

The mechanism and empirical results are established directly on Deribit Bitcoin options:
- **Inverse Settlement vs. Cash Settlement:** Deribit BTC options are coin-margined (settled in BTC). Hedging short call/put positions with BTC spot or perpetual futures introduces non-linear margin currency exposure ($V_{\mathrm{BTC}} = V_{\mathrm{USD}} / S_t$). Delta formulas must account for the inverse numeraire or hedge directly via linear USD-margined contracts (e.g., Binance BTCUSDT perpetual).
- **Perpetual Funding Rate Drag:** When hedging short options using perpetual futures instead of spot BTC, hourly funding rate payments accrue, shifting the optimal band offset toward negative funding carry.
- **24/7 Liquidity Gaps & Extreme Jumps:** Crypto options experience sudden implied volatility regime jumps and discontinuous spot gaps (e.g., liquidations, macro announcements). Asymptotic continuous diffusion approximations understate tail gamma risk during gap events.

## Limitations

- **Not independently reproduced.**
- **Sampled-Day Structure:** Dataset consists of 61 first-of-month 24-hour snapshots (16 unique days in test set), limiting cross-day path dependency and effective degrees of freedom in block bootstrapping.
- **Fixed Cost Assumption:** Fixed 5 bps round-trip cost ignores order-book depth depletion, spread widening during volatility spikes, and maker rebate opportunities.
- **Heuristic Risk-Aversion Calibration:** The parameter $\lambda = 60$ was chosen by inspection rather than estimated via formal maximum likelihood or utility-indifference calibration.

## Implementation status

Not implemented. No PyBroker, NautilusTrader, paper, testnet, or live trading implementation.

## Adoption boundary

Research material only. Does not constitute trading advice, production validation, or authorization for live trading.

## Related Wiki records

- `[[quant/crypto-options-volatility-risk-premium-zscore-2026-08-31]]`
- `[[quant/crypto-options-implied-correlation-dispersion-2026-08-31]]`
- `[[quant/defi-everlasting-options-proactive-market-making-delta-hedge-2026-09-01]]`
- `[[quant/defi-amm-continuous-installment-options-lvr-delta-hedge-2026-09-01]]`

## Sources

1. Sheryan Kumar, "Deep Hedging Under Realistic Market Frictions: A Regime-Conditional Empirical Study of Dynamic Option Hedging on Bitcoin Options", arXiv:2608.29025v1 [q-fin.CP, q-fin.TR], August 29, 2026. DOI: [10.48550/arXiv.2608.29025](https://doi.org/10.48550/arXiv.2608.29025). https://arxiv.org/abs/2608.29025.
2. Full article text and tables: https://arxiv.org/html/2608.29025v1.
3. Whalley, A. E., & Wilmott, P. (1997). "An asymptotic analysis of an optimal hedging strategy for option portfolios with transaction costs." *Mathematical Finance*, 7(4), 407–424.
4. Leland, H. E. (1985). "Option pricing and replication with transactions costs." *The Journal of Finance*, 40(5), 1283–1301.
