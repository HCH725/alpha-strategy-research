---
schema: strategy-research-record-v1
title: "Bitcoin Inverse Option Pricing and Fast Volatility Surface Calibration via the Rough Bergomi Model"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - options
  - rough-volatility
  - deribit
  - inverse-options
  - calibration
  - pricing
status: research-only
confidence: medium
source_as_of: 2026-08-27
sources:
  - "University of Padova Department of Mathematics 'Tullio Levi-Civita' (Supervised by Prof. Giorgia Callegaro), 'Pricing and Calibration of Bitcoin Inverse Options via the Rough Bergomi Model', arXiv:2608.27575v1 [q-fin.PR, q-fin.CP, q-fin.MF], August 27, 2026. https://arxiv.org/abs/2608.27575"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Inverse Option Pricing and Fast Volatility Surface Calibration via the Rough Bergomi Model

## Provenance

- **Primary Paper:** *"Pricing and Calibration of Bitcoin Inverse Options via the Rough Bergomi Model"*, arXiv preprint `arXiv:2608.27575v1 [q-fin.PR, q-fin.CP, q-fin.MF]`, published August 27, 2026. URL: https://arxiv.org/abs/2608.27575.
- **Academic Origin:** Department of Mathematics "Tullio Levi-Civita", University of Padova (Master's thesis research supervised by Prof. Giorgia Callegaro).
- **Primary Categories:** Pricing of Securities (`q-fin.PR`), Computational Finance (`q-fin.CP`), Mathematical Finance (`q-fin.MF`).
- **Dataset / Venue:** 30 empirical implied volatility (IV) surfaces extracted from trade-level order flow and quotes on the Deribit cryptocurrency derivatives exchange between May 2022 and March 2025, covering baseline calm regimes as well as major market stress episodes (Terra/Luna collapse, FTX insolvency, ETF approvals).

## Economic mechanism

### Source-reported

Cryptocurrency options traded on major venues like Deribit are predominantly **inverse options** (coin-margined contracts): payoffs are denominated in USD but settled physically in Bitcoin (BTC). The inverse call payoff is given by:
$$\Phi(S_T) = \max\left(\frac{S_T - K}{S_T}, 0\right) = \max\left(1 - \frac{K}{S_T}, 0\right)$$
This non-linear payoff structure alters risk-neutral dynamics and currency exposure.

Furthermore, empirical cryptocurrency volatility exhibits extreme "roughness"—the log-volatility behaves not like a standard Brownian motion ($H = 0.5$) or continuous Markovian diffusion, but like a fractional Brownian motion with a very small Hurst parameter ($H \ll 0.5$). Standard stochastic volatility models (Heston, SABR) fail to match the steep power-law blowup of the at-the-money (ATM) volatility skew $\partial \sigma_{\text{IV}} / \partial k \sim T^{H - 1/2}$ at ultra-short maturities without introducing unrealistic parameter jumps.

The **rough Bergomi (rBergomi)** model models the forward variance curve $\xi_0(t)$ modulated by a Volterra fractional process:
$$v_t = \xi_0(t) \exp\left(\eta \tilde{W}_t^H - \frac{1}{2} \eta^2 t^{2H}\right)$$
where $\tilde{W}_t^H = \sqrt{2H} \int_0^t (t-s)^{H-1/2} dW_s^1$. 

By integrating this fractional volatility driver with the inverse payoff, the paper demonstrates that Bitcoin volatility surfaces can be accurately priced and calibrated using an ultra-fast simulation pipeline (Hybrid Scheme + Mixed Estimator), achieving realistic skew fits with consistent Hurst parameter estimates $H \in [0.01, 0.06]$.

### Research interpretation

This research yields two distinct systematic trading applications on crypto options:
1. **Delta-Neutral Volatility Arbitrage (Relative Value / Skew Trading):**
   - Traditional market makers quoting crypto options with Black-76 or Heston overprice short-dated out-of-the-money (OTM) puts and calls relative to rough volatility dynamics, or misprice the wing skew.
   - A quantitative desk calibrating the rBergomi model in real-time can identify mispriced strikes where $\Delta \text{IV} = \text{IV}_{\text{market}} - \text{IV}_{\text{rBergomi}}$ exceeds quoting bid-ask spreads, executing delta-hedged volatility spreads (e.g., straddles, strangles, or risk reversals).
2. **Improved Dynamic Delta-Hedging:**
   - Because standard Black-76 delta ignores the correlation between spot returns and instantaneous rough variance ($\rho \approx -0.4$ to $-0.7$), standard deltas suffer from high tracking error. rBergomi-implied deltas reduce hedging variance over extreme volatility regimes.

## Signal

### 1. Model Calibration Pipeline
- **Inputs:**
  - Market forward variance curve $\xi_0(T)$ bootstrapped from Deribit ATM implied volatilities.
  - Option surface grid: Strikes $K_j \in [0.5 S_0, 2.0 S_0]$, Expiries $T_i \in [1\text{d}, 180\text{d}]$.
- **Parameter Vector:** $\Theta = (H, \eta, \rho)$
  - $H \in [0.01, 0.50]$: Hurst exponent (roughness parameter).
  - $\eta > 0$: Volatility of volatility.
  - $\rho \in [-1, 1]$: Spot-volatility correlation (leverage effect).
- **Fast Calibration Algorithm (Hybrid Scheme + Mixed Estimator):**
  - Discretize the fractional kernel using the Hybrid Scheme (Bennedsen et al., 2017) over $N = 100$ time steps.
  - Compute option price expectations via the Mixed Monte Carlo Estimator (combining conditional Black-Scholes formula on the Brownian path $W^2$ conditioned on $W^1$).
  - Minimize the unweighted root-mean-square error (RMSE) against market implied volatilities:
    $$\hat{\Theta} = \arg\min_{\Theta} \sqrt{\frac{1}{M} \sum_{k=1}^M \left(\sigma_{\text{IV}}^{\text{market}}(K_k, T_k) - \sigma_{\text{IV}}^{\text{rBergomi}}(K_k, T_k; \Theta)\right)^2}$$

### 2. Systematic Volatility Arbitrage Signal
- **Signal Formation:** Computed at hourly intervals or on receipt of full Deribit order book snapshots.
- **Strike-Level Mispricing Spread:**
  $$\Delta \text{IV}(K, T) = \sigma_{\text{IV}}^{\text{market}}(K, T) - \sigma_{\text{IV}}^{\text{rBergomi}}(K, T; \hat{\Theta})$$
- **Trading Entry Rules:**
  - **Overpriced Option (Sell Volatility):** If $\Delta \text{IV}(K, T) > \theta_{\text{sell}} = 1.5 \times \text{Spread}_{\text{IV}}(K, T)$, sell option contract via resting maker limit order.
  - **Underpriced Option (Buy Volatility):** If $\Delta \text{IV}(K, T) < -\theta_{\text{buy}} = -1.5 \times \text{Spread}_{\text{IV}}(K, T)$, buy option contract via resting maker limit order.
- **Hedging Rule:** Immediately hedge spot delta exposure using Deribit BTC-PERP or spot market:
  $$\Delta_{\text{hedge}} = -\frac{\partial C^{\text{inv}}}{\partial S}$$
  Rebalance delta hedge when spot moves by $> 1.0 \times \text{dynamic band}$ (e.g., Whalley-Wilmott band).
- **Exit Rule:** Close option position when $\left|\Delta \text{IV}(K, T)\right| < 0.25 \times \text{Spread}_{\text{IV}}$, or at $T - 2\text{ hours}$ before expiry.

## Required data

- **Instrument:** Deribit Bitcoin inverse option contracts (BTC-USD options, all strikes and expiries) and BTC-PERP.
- **Universe:** BTC options across maturities from 1 day to 6 months.
- **Venue:** Deribit (primary crypto options venue, >85% market share).
- **Timeframe:** 1-minute to 1-hour implied volatility surface snapshots.
- **Fields:**
  - Strike price ($K$), Expiration timestamp ($T$).
  - Option type (Call / Put).
  - Bid, Ask, Mark Implied Volatility ($\sigma_{\text{IV}}$).
  - Index price / Underlier Spot price ($S_0$).
  - Order book depth at top 5 levels.
- **Point-in-time:** Real-time WebSocket ticker and mark price feeds; strictly causal parameter estimation.

## Execution assumptions

- **Execution Venue:** Deribit API / WebSocket.
- **Order Types:**
  - Options Leg: Passive maker limit orders placed inside the spread (maker rebate of 0.00% to -0.01% or low fee tier).
  - Delta-Hedge Leg: Aggressive IOC limit orders or low-latency maker orders on BTC-PERP.
- **Execution Latency:** 20–100ms API roundtrip. Fast calibration must complete in < 20 seconds to remain tradable across hourly mark cycles.
- **Collateral / Margin:** Account collateral held in BTC; portfolio margin enabled to offset option gamma against perpetual futures hedges.

## Evidence

### Source-reported

- **Empirical Dataset:** 30 historical implied volatility surfaces from Deribit spanning May 2022 to March 2025.
- **Roughness Finding:** Calibrated Hurst exponent $H$ consistently clusters between **0.01 and 0.06** across all 30 surfaces, confirming extreme roughness in crypto volatility (substantially rougher than equity indices where $H \approx 0.10$).
- **Computational Benchmark Performance:**
  - **Hybrid Scheme + Mixed Estimator:** Mean unweighted RMSE of **22.83 percentage points**; calibration execution time of **17 seconds** per surface.
  - **Cholesky + Plain Log-Euler Benchmark:** Mean RMSE of **31.45 percentage points**; calibration execution time of **350 seconds** per surface.
  - **Speedup:** The Hybrid+Mixed pipeline delivers a **20-fold computational speed-up** while reducing pricing RMSE by ~8.6 percentage points.
- **Volatility Scaling Error:** Calibration error was observed to scale approximately linearly with the absolute level of ATM implied volatility.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Coin-Margining Currency Risk:** Because inverse option accounts hold margin collateral in BTC, an unhedged or delta-hedged long options position loses collateral equity during severe Bitcoin market crashes, increasing liquidation risk despite positive option intrinsic value.
- **Illiquid Far-OTM Spreads:** Far OTM options on Deribit frequently suffer from wide bid-ask spreads (100–300 bps IV spread), which can exceed the theoretical pricing edge $\Delta \text{IV}$.
- **Monte Carlo Estimation Variance:** Even with the Mixed Estimator, small sampling noise in Monte Carlo simulations can induce false-positive arbitrage signals if the threshold $\theta$ is set too tightly.

## Falsification plan

1. **Out-of-Sample Surface Forecasting Test:** Calibrate rBergomi parameters on surface $t$ and predict option prices at $t + 1\text{ hour}$. **Failure rule:** If rBergomi pricing error exceeds standard SABR or SVI (Stochastic Volatility Inspired) parametric fit RMSE on out-of-sample quotes, the structural rough volatility hypothesis is rejected as computationally inefficient.
2. **Delta-Hedge Variance Reduction Test:** Simulate continuous delta-hedging of BTC straddles using rBergomi delta vs. Black-76 delta over a 1-year historical period. **Failure rule:** If rBergomi delta does not reduce total hedging PnL variance by at least $15\%$ relative to Black-76, the operational value of rough volatility hedging is falsified.
3. **Execution-Aware PnL Test:** Simulate the relative-value strategy with full Deribit taker fees (3 bps underlying notional) and realistic order-queue fill probabilities. **Failure rule:** If net strategy Sharpe ratio $< 0.50$, the strategy is deemed non-tradable due to bid-ask friction.

## Crypto portability

**direct**

This research directly models cryptocurrency derivatives market microstructure:
- **Crypto-Native Architecture:** The paper specifically formulates its mathematics around the **inverse payoff** $\max(1 - K/S_T, 0)$ native to Deribit and coin-margined crypto options.
- **Exchange Calibration:** Directly calibrated on Deribit BTC options empirical telemetry.
- **Cross-Asset Extension:** The methodology directly extends to Ethereum (ETH) and Solana (SOL) inverse and linear options on Deribit and Bybit.

## Limitations

- **Calibration Latency:** Even at 17 seconds per surface, real-time tick-by-tick calibration requires GPU acceleration (CUDA) or pre-trained neural network surrogates.
- **Linear Volatility Error Scaling:** Model error increases during extreme market panics when ATM IV surpasses 100%.
- **Concentration in BTC:** Deribit liquidity is concentrated in monthly and quarterly maturities; ultra-short (< 24h) 0DTE crypto options may exhibit intraday jump dynamics not fully captured by pure fractional Brownian continuous paths.

## Implementation status

No implementation in our research stack. The paper provides theoretical formulations, numerical simulation schemes, and empirical calibration statistics; no live or paper-trading execution pipeline has been deployed.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[quant/crypto-deribit-options-volatility-of-volatility-vov-realized-quarticity-2026-09-01]] — Volatility-of-volatility dynamics on Deribit
- [[quant/crypto-options-implied-volatility-risk-reversal-skew-2026-09-01]] — Implied volatility skew and risk reversal strategies
- [[quant/crypto-bitcoin-option-dynamic-hedging-whalley-wilmott-no-trade-band-2026-09-01]] — Dynamic delta hedging with transaction cost bands

## Sources

1. University of Padova Department of Mathematics "Tullio Levi-Civita" (Supervised by Prof. Giorgia Callegaro), "Pricing and Calibration of Bitcoin Inverse Options via the Rough Bergomi Model", arXiv preprint arXiv:2608.27575v1 [q-fin.PR, q-fin.CP, q-fin.MF], August 27, 2026. URL: https://arxiv.org/abs/2608.27575.
