---
schema: strategy-research-record-v1
title: Funding-Aware Optimal Market Making for Perpetual DEXs
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-making
  - perpetual-futures
  - funding-rate
  - stochastic-control
  - hjb
  - hyperliquid
status: research-only
confidence: medium
source_as_of: 2026-05
sources:
  - https://arxiv.org/abs/2605.06405
  - https://doi.org/10.1080/14697680701698146
  - https://doi.org/10.1137/130946256
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Funding-Aware Optimal Market Making for Perpetual DEXs

## Provenance

Primary source: Nam Anh Le, “Funding-Aware Optimal Market Making for Perpetual DEXs,” *arXiv preprint arXiv:2605.06405* (Quantitative Finance - Mathematical Finance [q-fin.MF]), published May 2026. URL: https://arxiv.org/abs/2605.06405.

Foundational and related literature:
- Marco Avellaneda and Sasha Stoikov, “High-frequency trading in a limit order book,” *Quantitative Finance* 8(3), 217–224 (2008). DOI: https://doi.org/10.1080/14697680701698146.
- Álvaro Cartea, Sebastian Jaimungal, and Jason Penalva, *Algorithmic and High-Frequency Trading*, Cambridge University Press / SIAM (2015). DOI: https://doi.org/10.1137/130946256.

The primary study investigates high-frequency liquidity provision in perpetual futures order books on decentralized exchanges (calibrated using Hyperliquid tick-level order book and trade data for ETH, BTC, and SOL across 2025–2026).

## Economic mechanism

### Source-reported

In classical market making (e.g., Avellaneda & Stoikov 2008), inventory is penalized exclusively due to terminal mark-to-market price variance risk. However, in perpetual futures contracts, holding open inventory incurs an endogenous, state-dependent cash flow through periodic funding rate payments. 

When the market is in a sustained long-premium regime (positive funding rate), long inventory incurs a running cost paid to short holders, whereas short inventory generates positive cash-flow yield. When funding is negative, long inventory collects funding while short inventory is penalized. 

The author shows that classical inventory penalty models fail to account for the magnitude and sign of this cash flow, resulting in suboptimal quote placement. By treating the funding rate as a continuous stochastic state variable coupled with inventory, the market maker derives dynamic bid and ask spreads that actively skew quotes to harvest funding yield when advantageous and widen quotes to deter accumulating inventory in adverse funding states.

### Research interpretation

The hypothesized mechanism is stochastic control-based inventory risk management augmented with funding carry optimization:
1. Perpetual futures inventory creates dual risk exposures: directional price variance and stochastic funding cash-flow yield.
2. Modeling the funding rate as an Ornstein-Uhlenbeck (OU) mean-reverting diffusion allows solving the market maker's value function via a monotone finite-difference Hamilton-Jacobi-Bellman (HJB) scheme.
3. The optimal quote offsets dynamically widen the bid and tighten the ask when funding is positive (discouraging costly long inventory and encouraging short carry accumulation), and vice-versa when funding is negative.
4. This yields superior risk-adjusted spread capture and reduced inventory volatility compared to funding-blind Avellaneda-Stoikov quoting.

## Signal

1. **State variables**:
   - Mid-price $S_t$.
   - Inventory position $q_t \in [q_{\min}, q_{\max}]$ (discrete inventory grid).
   - Cash-scaled fractional funding rate state $f_t \approx S_t F_t$, modeled via Ornstein-Uhlenbeck diffusion:
     $$df_t = \kappa (\bar{f} - f_t) dt + \sigma_f dW_t^f$$
     with correlation $\rho = \text{Corr}(dW_t^S, dW_t^f)$.

2. **HJB Value Function Formulation**:
   - Solve the value function $V(t, q, f)$ over horizon $T$ under CARA utility with risk-aversion parameter $\gamma$ and inventory penalty parameter $\phi$:
     $$\partial_t V + \kappa (\bar{f} - f) \partial_f V + \frac{1}{2} \sigma_f^2 \partial_{ff} V - \frac{1}{2} \gamma \sigma_S^2 q^2 + q f + H^b(q, f, \partial_q V) + H^a(q, f, \partial_q V) = 0$$
   - where Hamiltonian terms incorporate Poisson fill intensities $\Lambda(\delta) = A e^{-k \delta}$.

3. **Quote offset generation**:
   - Compute optimal bid offset $\delta_t^{b,*}$ and ask offset $\delta_t^{a,*}$ from discrete inventory value differences:
     $$\delta_t^{b,*}(q, f) = \frac{1}{k} + V(t, q, f) - V(t, q+1, f)$$
     $$\delta_t^{a,*}(q, f) = \frac{1}{k} + V(t, q, f) - V(t, q-1, f)$$

4. **Execution / Quoting rule**:
   - Place limit buy order at $P_t^b = S_t - \delta_t^{b,*}(q, f)$.
   - Place limit sell order at $P_t^a = S_t + \delta_t^{a,*}(q, f)$.
   - Boundary enforcement: If $q = q_{\max}$, suppress bid ($\delta^{b,*} = \infty$); if $q = q_{\min}$, suppress ask ($\delta^{a,*} = \infty$).

5. **Specification status**: **fully specified** mathematically for the reduced HJB formulation; **underspecified** regarding exact fill latency and queue-position dynamics on live DEX chains.

## Required data

- High-frequency Level 2 order book snapshots (depth, top of book bid/ask) for perpetual futures contracts.
- Trade prints with aggressor side markers to estimate arrival rate intensity parameters ($A, k$).
- 1-minute to 1-hour historical funding rate time series for OU parameter calibration ($\kappa, \bar{f}, \sigma_f, \rho$).
- Mid-price volatility $\sigma_S$ from high-frequency returns.
- Venue: Decentralized perpetual exchange order books (e.g. Hyperliquid L1/L2) or major CEX perpetuals (Binance, Bybit).

## Execution assumptions

- Passive quoting: Orders placed as post-only limit orders to capture maker fee rebates and avoid crossing spread.
- Continuous cancellation/replacement: Quotes updated whenever mid-price moves or funding state shifts materially.
- Fill intensity model: Order fills assumed to follow Poisson point process $\Lambda(\delta) = A e^{-k \delta}$ calibrated from historical fill-distance empirical data.
- Inventory capacity: Constrained within fixed finite bounds (e.g. $[-Q, +Q]$ contracts) to avoid margin liquidation.

## Evidence

### Source-reported

Nam Anh Le (2026) reports:
- Across 100-seed holdout backtest simulations on Hyperliquid ETH, BTC, and SOL perpetuals:
  - The funding-aware HJB model consistently achieves higher terminal PnL and lower inventory root-mean-square (RMS) deviations compared to classical Avellaneda-Stoikov quoting on ETH and BTC.
  - ETH inventory RMS is reduced by 14–22% while net Sharpe ratio increases by 0.35–0.60 across multiple fill proxy calibrations.
  - On SOL, the funding-aware strategy demonstrates positive alpha over baseline AS, though gains are non-Pareto unless explicit volatility scaling is incorporated due to higher jump intensity.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Funding rate distributions in crypto exhibit fat tails and discontinuous jump processes (e.g. during sudden market deleveraging events) that exceed standard Gaussian OU diffusion assumptions.
- Taker latency front-running (toxic flow / oracle latency arbitrage) on DEXs can selectively fill quotes immediately before adverse mark-price moves, eroding spread capture.

## Falsification plan

The strategy hypothesis should be considered falsified if:
1. In high-frequency backtesting with realistic queue-position simulation, the funding-aware quote skew produces lower net PnL than a symmetric Avellaneda-Stoikov model after maker/taker fees.
2. In regimes with near-zero funding rate volatility ($\sigma_f \to 0$), the HJB model fails to collapse to standard inventory control.
3. Holdout evaluation on out-of-sample altcoin perpetuals reveals that inventory accumulation during sudden funding rate regime shifts causes unhedged drawdown exceeding 2x the inventory penalty threshold.

## Crypto portability

**Direct**: The model is purpose-built for crypto perpetual futures contracts where funding rates are paid continuously or on 1h/8h intervals.

Portability adaptations:
- Applicable to both DEX order books (Hyperliquid, dYdX, Aevo) and CEX perpetuals (Binance Futures, Bybit).
- On venues with 8-hour discrete funding payments vs continuous funding (e.g. Hyperliquid continuous 1h EWMA vs Binance 8h discrete), the cash flow term $q f$ must incorporate the time-to-settlement decay function.

## Limitations

- **not independently reproduced**: Requires execution-level backtesting within high-frequency simulation framework.
- **jump-diffusion omission**: Baseline Gaussian OU does not account for discontinuous funding spikes during market liquidations.
- **queue position simplification**: Poisson arrival intensity approximates fill dynamics but omits exact L2 queue queue-priority mechanics.

## Implementation status

No implementation in PyBroker, NautilusTrader, or any internal research/backtesting pipeline has been performed.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material only. It does not represent a validated production strategy, an execution authorization, or approval for Paper, Testnet, or Live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

- `[[crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31]]`
- `[[crypto-cex-dex-cross-venue-funding-spread-carry-2026-08-31]]`
- `[[crypto-multilevel-order-flow-imbalance-intraday-2026-08-31]]`

## Sources

1. Nam Anh Le, “Funding-Aware Optimal Market Making for Perpetual DEXs,” *arXiv preprint arXiv:2605.06405* (2026). URL: https://arxiv.org/abs/2605.06405
2. Marco Avellaneda and Sasha Stoikov, “High-frequency trading in a limit order book,” *Quantitative Finance* 8(3), 217–224 (2008). DOI: https://doi.org/10.1080/14697680701698146
3. Álvaro Cartea, Sebastian Jaimungal, and Jason Penalva, *Algorithmic and High-Frequency Trading*, Cambridge University Press (2015). DOI: https://doi.org/10.1137/130946256
