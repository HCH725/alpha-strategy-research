---
schema: strategy-research-record-v1
title: Cryptocurrency Option Pricing and Volatility-of-Volatility Risk Premium Harvesting with Realized Quarticity
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - options
  - deribit
  - volatility-of-volatility
  - realized-quarticity
  - affine-garch
  - relative-value
  - bitcoin
status: research-only
confidence: high
source_as_of: 2024-07-31
sources:
  - https://doi.org/10.1002/fut.70029
  - https://ideas.repec.org/a/wly/jfutmk/v45y2025i11p2066-2091.html
  - https://doi.org/10.1016/S0304-4076(01)00115-4
  - https://doi.org/10.1093/rfs/hhp029
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cryptocurrency Option Pricing and Volatility-of-Volatility Risk Premium Harvesting with Realized Quarticity

## Provenance

Primary source:

- Lingshan Du and Ji Shen. "Pricing Cryptocurrency Options With Volatility of Volatility." *Journal of Futures Markets*, Volume 45, Issue 11 (November 2025), pages 2066–2091. First published online August 2025.
- DOI: https://doi.org/10.1002/fut.70029
- RePEc/IDEAS bibliographic entry: `RePEc:wly:jfutmk:v:45:y:2025:i:11:p:2066-2091` (https://ideas.repec.org/a/wly/jfutmk/v45y2025i11p2066-2091.html)

Foundational and related econometric literature:

- Tim Bollerslev, George Tauchen, and Hao Zhou. "Expected Stock Returns and Variance Risk Premia." *Review of Financial Studies*, Volume 22, Issue 11 (2009), pages 4463–4492. DOI: https://doi.org/10.1093/rfs/hhp029.
- Torben G. Andersen, Tim Bollerslev, Francis X. Diebold, and Paul Labys. "The Distribution of Realized Exchange Rate Volatility." *Journal of the American Statistical Association*, Volume 96, Issue 453 (2001), pages 42–55. DOI: https://doi.org/10.1198/016214501750332966.
- Ole E. Barndorff-Nielsen and Neil Shephard. "Econometric Analysis of Realized Volatility and Its Use in Estimating Stochastic Volatility Models." *Journal of the Royal Statistical Society: Series B (Statistical Methodology)*, Volume 64, Issue 2 (2002), pages 253–280. DOI: https://doi.org/10.1111/1467-9868.00336.

The empirical sample in Du and Shen (2025) comprises transaction-level tick data and end-of-day implied volatility surfaces for Bitcoin European inverse options traded on the Deribit exchange between November 1, 2017, and July 31, 2024, representing 349 weekly cross-sections and over 2,500 trading days.

## Economic mechanism

### Source-reported

Cryptocurrency option markets are characterized by heavy-tailed return innovations, abrupt volatility spikes, and pronounced time-varying volatility clustering. Standard single-factor stochastic volatility and conventional GARCH-type models frequently misprice deep out-of-the-money (OTM) options and short-dated volatility smiles because they assume that the volatility of the volatility process itself (VOV) is either constant or deterministically coupled to the level of volatility.

Du and Shen (2025) develop the Affine Realized Volatility-of-Volatility (ARVOV) option pricing framework, which explicitly establishes dual latent stochastic state variables:
1. Instantaneous Return Volatility ($h_t$);
2. Volatility-of-Volatility ($q_t$).

To update these latent states efficiently without noisy unobservable filters, the authors incorporate two high-frequency intraday realized measures:
- **Realized Variance ($RV_t$):** capturing the daily level of return variance;
- **Realized Quarticity ($RQ_t$):** capturing the asymptotic dispersion / variance of realized variance (acting as the empirical proxy for time-varying VOV).

Using Fourier transform inversion, the authors derive closed-form European option valuation equations under the risk-neutral measure $\mathbb{Q}$, pricing both the market price of volatility risk ($\lambda_h$) and the market price of VOV risk ($\lambda_q$). The authors demonstrate that the ARVOV model reduces out-of-sample implied volatility valuation errors across Deribit options by **8.55%** relative to benchmark Affine Realized Volatility (ARV) models.

### Research interpretation

The strategy captures an economically grounded **volatility and volatility-of-volatility (VOV) relative-value mispricing premium**:

1. **Market Mispricing Source:** Market participants on Deribit price options using static Black-76 implied volatility surfaces or ad-hoc local volatility heuristics, leading to systematic over- or under-pricing of tail-risk contracts (OTM calls and puts) when the underlying market transitions between volatility-of-volatility regimes (e.g., transition from quiet consolidation to high-kurtosis explosive regimes).
2. **Empirical Filtering via High-Frequency Intraday Data:** By calculating daily 5-minute Realized Variance ($RV_t$) and Realized Quarticity ($RQ_t$), the econometric engine dynamically tracks current $h_{t+1}$ and $q_{t+1}$ ahead of the slow-moving consensus IV surface.
3. **Delta-Hedged Relative-Value Capture:**
   - Underpriced Options ($IV^{\text{market}} < IV^{\text{ARVOV}} - \text{buffer}$): Buy option contract, sell underlying perpetual futures to achieve delta-neutrality ($\Delta \approx 0$).
   - Overpriced Options ($IV^{\text{market}} > IV^{\text{ARVOV}} + \text{buffer}$): Sell option contract, buy underlying perpetual futures to achieve delta-neutrality.
4. **Payoff Profile:** The delta-hedged position captures the convergence between market implied volatility and econometric fair value, alongside the harvest of the structural crypto Variance Risk Premium (VRP) and VOV Risk Premium (VOV-RP).

## Signal

The strategy operates as a daily/intraday options surface relative-value trading engine:

### 1. High-Frequency Realized Measure Computation
Using 5-minute intraday log-returns $r_{t,i} = \ln(S_{t,i}) - \ln(S_{t,i-1})$ for $i = 1, \dots, N$ ($N = 288$ intervals per 24-hour UTC crypto session):
- **Daily Realized Variance ($RV_t$):**
  $$RV_t = \sum_{i=1}^N r_{t,i}^2$$
- **Daily Realized Quarticity ($RQ_t$):**
  $$RQ_t = \frac{N}{3} \sum_{i=1}^N r_{t,i}^4$$

### 2. State-Space Latent Variable Update (ARVOV System)
Under the physical measure $\mathbb{P}$:
$$h_{t+1} = \omega_h + \beta_h h_t + \alpha_h RV_t$$
$$q_{t+1} = \omega_q + \beta_q q_t + \alpha_q RQ_t$$

Where parameters $(\omega_h, \beta_h, \alpha_h, \omega_q, \beta_q, \alpha_q)$ are estimated via quasi-maximum likelihood (QMLE) over a rolling calibration window (e.g., 250 days).

### 3. Risk-Neutral Valuation & Theoretical Implied Volatility
- Map the state variables $(h_{t+1}, q_{t+1})$ to the risk-neutral measure $\mathbb{Q}$ using the market price of risk parameters $(\lambda_h, \lambda_q)$.
- Evaluate the conditional characteristic function $\Psi(u; h_{t+1}, q_{t+1}, \tau)$ of log-price at maturity $\tau = T - t$.
- Compute theoretical European call and put prices via Fourier inversion:
  $$C^{\text{ARVOV}}(S_t, K, \tau) = S_t \Pi_1 - K e^{-r\tau} \Pi_2$$
- Invert Black-76 formula to solve for the model theoretical implied volatility $IV^{\text{ARVOV}}(K, \tau)$.

### 4. Signal Discrepancy & Trade Selection
For every active strike $K$ and maturity $\tau$ on Deribit:
$$\text{Discrepancy}_{K, \tau, t} = IV^{\text{market}}_{K, \tau, t} - IV^{\text{ARVOV}}_{K, \tau, t}$$

- **Long Volatility Entry (Underpriced Option):**
  - Trigger when $\text{Discrepancy}_{K, \tau, t} \le -\theta_{\text{entry}}$ (e.g., market IV is $> 3.5$ percentage points below model fair value).
  - Buy option contract; compute analytical Black-76 delta $\Delta_j$; sell $\Delta_j$ notional of BTC perpetual futures.
- **Short Volatility Entry (Overpriced Option):**
  - Trigger when $\text{Discrepancy}_{K, \tau, t} \ge +\theta_{\text{entry}}$ (e.g., market IV is $> 3.5$ percentage points above model fair value).
  - Sell option contract; buy $\Delta_j$ notional of BTC perpetual futures.

### 5. Delta Rebalancing & Position Exit
- **Dynamic Delta-Hedge:** Rebalance perpetual hedge whenever portfolio aggregate net delta exceeds threshold $|\Delta_{\text{net}}| > 0.05 \text{ BTC}$.
- **Convergence Exit:** Close option and associated delta-hedge when $|\text{Discrepancy}_{K, \tau, t}| \le 0.50 \text{ vol points}$.
- **Time-Decay Exit:** Close all positions $\tau \le 2 \text{ days}$ prior to expiry to eliminate gamma tail risk and pin risk.

## Required data

- **Deribit Options Order Book & Trade Data:** Tick and 1-minute resolution order books (best bid, ask, implied volatility, delta, gamma, vega, open interest) for BTC inverse options across all available strike grids and expiries.
- **Deribit & CEX Spot / Perpetual Tick Feeds:** 5-minute OHLCV price series for Deribit BTC-USD perpetual, Binance BTCUSDT perpetual, and Coinbase BTC-USD spot to compute $RV_t$ and $RQ_t$.
- **Interest Rate / Yield Curve:** Synthetic risk-free rate derived from Deribit BTC futures term structure or USD stablecoin borrow rates.

## Execution assumptions

- **Inverse Options Mechanics:** Deribit options are inverse contracts denominated and margined in BTC. Dollar delta must be scaled by underlying spot price:
  $$\Delta_{\text{BTC}} = \frac{\Delta_{\text{dollar}}}{S_t}$$
- **Execution Cost:**
  - Deribit options taker fee: 3 bps of underlying ($0.03\% \times S_t$), capped at 12.5% of the option mark price; maker rebate: 0.5–1.0 bps.
  - Deribit / Binance perpetual futures fee: 2–4 bps taker, 0–1 bps maker.
  - Bid-ask spread crossing: options width modeled at 1.0–2.5 vol points for liquid strikes.
- **Margin & Portfolio Margin (PM):** Unified Portfolio Margin enabled on Deribit to allow net delta, gamma, and vega offsets between short/long options and perpetual futures, preventing excessive capital drag.

## Evidence

### Source-reported

Du and Shen (2025) report the following empirical findings using Deribit Bitcoin option data from November 2017 to July 2024:
- **Out-of-Sample Pricing Accuracy:** The ARVOV model achieves an **8.55% reduction in root mean squared implied volatility errors (RMSIVE)** compared to traditional affine realized volatility (ARV) benchmark models across the entire cross-section of options.
- **Priced VOV Risk Premium:** The estimated market price of VOV risk ($\lambda_q$) is statistically significant at the 1% level ($p < 0.01$) across the full multi-year sample, confirming that volatility-of-volatility is an independently priced risk dimension in cryptocurrency derivatives.
- **Moneyness and Maturity Robustness:** The pricing improvement is most pronounced for out-of-the-money (OTM) options and during market stress periods, demonstrating that incorporating Realized Quarticity ($RQ$) effectively captures tail risk and asymmetric volatility smiles.

### Independently reproduced

Not independently reproduced in the user's research stack.

### Negative evidence

- **Discrete Jump Regime Breakdown:** In extreme sudden crash events (such as March 12, 2020, or May 19, 2021), continuous diffusion and affine GARCH approximations underestimate sudden non-linear jump discontinuities, causing delta-hedged short options portfolios to experience sharp gamma drawdowns.
- **Hedging Drag in High-Funding Regimes:** Long delta-hedged options strategies that maintain continuous short perpetual futures positions suffer carry drag during prolonged bull runs where perpetual funding rates exceed 20–30% annualized.
- **Liquidity Gaps in Far-OTM Strikes:** Wide bid-ask spreads in illiquid, far-dated Deribit option strikes can exceed the 3.5 vol point model discrepancy buffer, eroding theoretical mispricing profits.

## Falsification plan

The VOV risk premium harvesting hypothesis should be rejected or restructured if:

1. **Net Alpha Failure:** Delta-hedged trading simulations over a multi-year backtest (2024–2026) produce an annualized Information Ratio or Sharpe ratio $< 0.60$ after subtracting Deribit maker/taker fees, spread crossing, and perpetual funding costs.
2. **Quarticity Incremental Value Rejection:** In out-of-sample testing, an ablation test removing Realized Quarticity ($RQ_t$) yields no statistically significant increase in implied volatility forecast errors ($p > 0.10$).
3. **Execution Drag Dominance:** Gamma rebalancing turnover costs systematically exceed the gross volatility convergence spread.

## Crypto portability

**Direct**, as the ARVOV framework is explicitly designed and calibrated on Deribit cryptocurrency inverse options.

Portability considerations:
- **Ethereum (ETH) Options:** Directly portable to Deribit ETH options and OKX ETH options; realized quarticity values in ETH are typically higher due to greater idiosyncratic jump frequency.
- **Solana / Altcoin Options:** Portable to emerging centralized and decentralized options platforms (OKX, Bybit, Zeta Markets), though lower liquidity and wider spreads require larger entry discrepancy thresholds ($\theta_{\text{entry}} \ge 5.0\text{ vol points}$).

## Limitations

- **Not independently reproduced** in this research stack.
- **Computational Complexity:** Requires real-time Fourier inversion and rolling non-linear econometric calibration.
- **Tail Jump Risk:** Unhedged higher-order moments (gamma, vanna, volga) remain exposed to discrete gap events that bypass continuous delta-hedging.
- **Counterparty & Custody Risk:** Requires maintaining collateral on offshore centralized derivatives exchanges (Deribit).

## Implementation status

No implementation in PyBroker, NautilusTrader, the strategy registry, any data pipeline, Paper, Testnet, Demo, or Live trading has been created or modified.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material in the Alpha Strategy Pool only. It is not evidence of validated alpha, not an implementation task, and not approval for Paper, Testnet, Demo, or Live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

- `[[bitcoin-options-implied-volatility-risk-reversal-skew-2026-09-01]]`
- `[[crypto-options-volatility-risk-premium-zscore-2026-08-31]]`
- `[[crypto-options-implied-correlation-dispersion-2026-08-31]]`
- `[[defi-on-chain-options-mispricing-hegic-arbitrum-2026-09-01]]`

## Sources

1. Lingshan Du and Ji Shen, "Pricing Cryptocurrency Options With Volatility of Volatility," *Journal of Futures Markets*, Volume 45, Issue 11, November 2025, pages 2066–2091. DOI: https://doi.org/10.1002/fut.70029
2. RePEc/IDEAS bibliographic entry for Du and Shen (2025): https://ideas.repec.org/a/wly/jfutmk/v45y2025i11p2066-2091.html
3. Tim Bollerslev, George Tauchen, and Hao Zhou, "Expected Stock Returns and Variance Risk Premia," *Review of Financial Studies*, Volume 22, Issue 11, 2009, pages 4463–4492. DOI: https://doi.org/10.1093/rfs/hhp029
4. Torben G. Andersen, Tim Bollerslev, Francis X. Diebold, and Paul Labys, "The Distribution of Realized Exchange Rate Volatility," *Journal of the American Statistical Association*, Volume 96, Issue 453, 2001, pages 42–55. DOI: https://doi.org/10.1198/016214501750332966
5. Ole E. Barndorff-Nielsen and Neil Shephard, "Econometric Analysis of Realized Volatility and Its Use in Estimating Stochastic Volatility Models," *Journal of the Royal Statistical Society: Series B (Statistical Methodology)*, Volume 64, Issue 2, 2002, pages 253–280. DOI: https://doi.org/10.1111/1467-9868.00336
