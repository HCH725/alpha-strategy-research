---
schema: strategy-research-record-v1
title: Crypto Cross-Platform Binary Threshold Mispricing and Delta-Hedged Arbitrage (Polymarket vs Binance Options)
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - options
  - prediction-markets
  - cross-venue
  - arbitrage
  - relative-value
  - bitcoin
status: research-only
confidence: high
source_as_of: 2026-06-17
sources:
  - https://arxiv.org/abs/2606.19517
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Platform Binary Threshold Mispricing and Delta-Hedged Arbitrage (Polymarket vs Binance Options)

## Provenance

Primary source:
- Victoria Portnaya. "Do Prediction Markets Match Option Prices? Bitcoin Threshold Evidence from Binance and Polymarket." arXiv:2606.19517v1 [q-fin.TR / q-fin.PR / q-fin.CP], June 17, 2026.
- arXiv URL: https://arxiv.org/abs/2606.19517
- DOI: https://doi.org/10.48550/arXiv.2606.19517

Data sources evaluated in the study:
1. **Binance Option Data:** Historical bid and ask quotes from the public `EOHSummary` archive at end-of-hour frequency for listed Bitcoin option contracts.
2. **Binance Spot Data:** Historical hourly bar data from Binance public archives for BTC/USDT.
3. **Polymarket Prediction Market Data:** Transaction-level trade data and historical hourly prices for matched threshold contracts.
4. **Deribit Extension:** Deribit historical order book and trade data for BTC and ETH vanilla options across matching strikes and expirations.

Matched contracts:
- Primary contract: Polymarket "BTC above $27,000 at end of September?" (Market ID `252196`) matched to Binance European call option `BTC-230929-27000-C` (214 aligned hourly observations).
- Pooled Bitcoin sample: Primary September 2023 contract plus two August 2023 contracts matched to `BTC-230901-28000-C` and `BTC-230901-26000-C` (287 aligned hourly observations).
- Deribit extension: Same three Bitcoin contracts evaluated against Deribit call options (2,585 aligned hourly observations).
- Supplementary Ethereum exercise: Four Polymarket "ETH above $1,700" contracts matched to Deribit ETH options across February–March 2023 (2,737 hourly observations).

## Economic mechanism

### Source-reported

Portnaya (2026) evaluates whether blockchain-based prediction markets (Polymarket) and centralized crypto-option exchanges (Binance and Deribit) agree on the valuation of identical state-contingent binary claims $\mathbf{1}\{S_T > K\}$.

Under standard no-arbitrage pricing with constant short rate $r$, the theoretical risk-neutral value of a cash-or-nothing binary call option that pays 1 unit if $S_T > K$ is:

$$P_{fair,t} = e^{-r\tau} \Phi(d_2)$$

where:
$$d_1 = \frac{\ln(S_t / K) + (r + \frac{1}{2}\sigma^2)\tau}{\sigma \sqrt{\tau}}, \quad d_2 = d_1 - \sigma \sqrt{\tau}$$

and $\sigma = \hat{\sigma}_t$ is the implied volatility inverted from the listed vanilla call option price $C_{mkt,t}$ on the same underlying, strike $K$, and time to maturity $\tau = T - t$.

The author documents a systematic, persistent positive pricing gap:

$$D_t = P_{poly,t} - P_{fair,t} > 0$$

where Polymarket Yes prices trade significantly above the option-implied risk-neutral binary fair value. The author attributes this wedge to three interrelated economic mechanisms:
1. **Demand-Side Speculative Overpricing / Longshot Bias:** Retail participants on prediction markets exhibit a strong preference for low-probability, high-payoff lottery bets (analogous to the favourite-longshot bias in parimutuel wagering and cumulative prospect theory), bidding up out-of-the-money Yes contracts above their option-implied probabilities.
2. **Market Segmentation and Slow-Moving Capital:** Capital constraints, cross-chain friction, KYC/regulatory boundaries, and venue fragmentation prevent instantaneous arbitrage between centralized derivatives order books and decentralized prediction AMM/CLOB contracts.
3. **Mean-Reverting Dynamic Wedge:** The pricing discrepancy exhibits an AR(1) half-life of ~4.2 hours, confirming that while cross-venue arbitrage capital is slow, prices eventually converge toward parity as expiration approaches.

### Research interpretation

The hypothesis is that **structural market segmentation between decentralized prediction markets (Polymarket) and centralized options markets (Binance/Deribit) creates persistent, mean-reverting cross-venue mispricings in binary threshold contracts**.

Trading hypothesis:
1. When $D_t = P_{poly,t} - P_{fair,t}$ exceeds transaction costs and statistical uncertainty bands ($|D_t| > SE(P_{fair,t}) + TF_t$), short the overpriced Polymarket Yes contract (or buy the No contract at $1 - P_{poly,t}$) and construct a synthetic long digital call using the corresponding centralized vanilla call option and underlying spot hedge.
2. Specifically, neutralize vega exposure by buying $q_0 = \mathcal{V}^D_{t_0} / \mathcal{V}^C_{t_0}$ units of the vanilla call, and neutralize residual delta exposure by trading $x_{t_0} = \Delta^D_{t_0} - q_0 \Delta^C_{t_0}$ units of underlying spot.
3. Rebalance the spot delta hedge dynamically and exit upon mean reversion of the pricing gap $D_t \to 0$ or contract settlement at expiry $T$.

## Signal

Normalized trading and delta-hedged arbitrage specification:

1. **Implied Volatility & Fair Value Inversion:**
   - At each hourly observation $t$, retrieve spot price $S_t$, listed vanilla call price $C_{mkt,t}$, strike $K$, risk-free rate $r$, and time to expiration $\tau_t = T - t$.
   - Invert Black-Scholes formula numerically to recover implied volatility $\hat{\sigma}_t$ satisfying $C_{BS}(S_t, K, r, \tau_t, \hat{\sigma}_t) = C_{mkt,t}$.
   - Compute the risk-neutral digital fair price:
     $$P_{fair,t} = e^{-r\tau_t} \Phi(d_{2,t}(\hat{\sigma}_t))$$

2. **Uncertainty & Friction Band Calculation:**
   - Calculate delta-method standard error of the binary benchmark:
     $$SE(P_{fair,t}) = \frac{|\mathcal{V}_t^D|}{\mathcal{V}_t^C} \cdot \hat{\varsigma}_{C,t}$$
     where $\mathcal{V}_t^D = -e^{-r\tau_t} \phi(d_{2,t}) \frac{d_{1,t}}{\hat{\sigma}_t}$ is binary vega, $\mathcal{V}_t^C = S_t \phi(d_{1,t}) \sqrt{\tau_t}$ is vanilla call vega, and $\hat{\varsigma}_{C,t} = \max\{(C_{high,t} - C_{low,t})/2, 0.01 |C_{mkt,t}|, 10^{-10}\}$.
   - Compute total transaction friction band:
     $$TF_t = \text{Fee}_{poly} + \frac{|\mathcal{V}_t^D|}{\mathcal{V}_t^C} \cdot \text{Fee}_{call} + |\Delta_t^D - q_t \Delta_t^C| \cdot \text{Fee}_{spot} + \frac{\text{Spread}_{poly}}{2}$$

3. **Entry Rule:**
   - Calculate discrepancy $D_t = P_{poly,t} - P_{fair,t}$.
   - If $D_t > SE(P_{fair,t}) + TF_t$:
     - Short 1 unit of Polymarket Yes (or buy 1 unit of Polymarket No at $1 - P_{poly,t}$).
     - Long $q_t = \frac{\mathcal{V}_t^D}{\mathcal{V}_t^C}$ units of listed vanilla call option.
     - Enter spot delta hedge $x_t = \Delta_t^D - q_t \Delta_t^C$ units of BTC/USDT spot, where $\Delta_t^D = \frac{e^{-r\tau_t} \phi(d_{2,t})}{S_t \hat{\sigma}_t \sqrt{\tau_t}}$ and $\Delta_t^C = \Phi(d_{1,t})$.
   - If $D_t < -(SE(P_{fair,t}) + TF_t)$:
     - Long 1 unit of Polymarket Yes, short $q_t$ units of vanilla call, short/long adjusted spot delta hedge.

4. **Dynamic Hedging & Exit Rule:**
   - Rebalance the spot position $x_t$ hourly as delta drifts.
   - Close entire arbitrage position when $D_t$ crosses zero (mean reversion) or hold until contract expiry $T$.

## Required data

- **Prediction Market Data:** Polymarket hourly prices, transaction quotes, and contract specifications (underlying token, threshold strike $K$, settlement timestamp $T$, oracle resolution mechanism).
- **Options Market Data:** Binance / Deribit hourly bid/ask/mid quotes, contract open interest, strike $K$, expiration $T$, and intraday high/low range ($C_{high}, C_{low}$) for uncertainty scaling.
- **Spot Market Data:** Binance / Deribit hourly BTC/USDT OHLCV and spot mark price.
- **Risk-Free Rate:** Short-term USD / stablecoin risk-free interest rate $r$ (e.g. SOFR or US Treasury yield).
- **Synchronization:** Strict timestamp matching at hourly boundaries with zero forward-looking leakage.

## Execution assumptions

- **Execution Timing:** Hourly rebalancing and trade execution based on end-of-hour aligned bars.
- **Transaction Costs:**
  - Polymarket: 0–20 bps taker fee / CLOB spread crossing.
  - Binance Options: 2–3 bps contract fee plus bid-ask half-spread.
  - Spot Hedging: 2–5 bps maker/taker spot fee.
- **Margin & Capital Efficiency:** Requires collateral allocated simultaneously across Polymarket (USDC on Polygon), Binance (USDT/USDC margin), and spot exchange accounts.
- **Settlement Oracle:** Polymarket binary options settle via UMA Optimistic Oracle / Chainlink feed, whereas Binance options settle against 30-minute index TWAP at 08:00 UTC on expiry date.

## Evidence

### Source-reported

All quantitative figures below are directly reported by Victoria Portnaya (arXiv:2606.19517v1, 2026):

1. **Main Market Discrepancy (September 2023 BTC $27,000 Contract):**
   - Sample: 214 aligned hourly observations.
   - Mean Polymarket Yes price: $\bar{P}_{poly} = 0.2872$.
   - Mean Binance risk-neutral fair price: $\bar{P}_{fair} = 0.2314$.
   - Mean pricing gap: $\bar{D} = 0.0558$ (5.58 percentage points, standard deviation $s_D = 0.1264$).
   - Statistical inference: One-sample $t$-statistic $t = 6.46$ ($p < 10^{-9}$), Newey-West HAC 95% CI: $[0.038, 0.073]$, circular block-bootstrap 95% CI: $[0.037, 0.075]$.
   - Time series dynamics: AR(1) persistence coefficient $\phi = 0.847$, implied half-life $h_{1/2} = 4.2$ hours. ADF test statistic $t = -3.74$ ($p = 0.004$), confirming stationarity.

2. **Pooled Three-Market Bitcoin Panel:**
   - Sample: 287 aligned hourly observations across September 2023 ($27k) and August 2023 ($26k, $28k) contracts.
   - Pooled mean gap: $\bar{D} = 0.0630$ (6.30 percentage points, $s_D = 0.1296$).
   - Statistical inference: One-sample $t = 8.24$ ($p = 6.26 \times 10^{-15}$), Newey-West HAC 95% CI: $[0.046, 0.080]$, block-bootstrap 95% CI: $[0.046, 0.080]$.
   - Outlier robustness: Median discrepancy $0.0642$, 10% trimmed mean $0.0576$, sign test positive rate $68.6\%$ ($p = 2.45 \times 10^{-10}$).

3. **Cross-Sectional Regression ($R^2 = 0.221, n = 287$):**
   - Option-implied probability coefficient: $\beta = -0.312$ ($t = -5.48, p < 10^{-6}$), confirming that the overpricing wedge is significantly larger when option-implied event probability is low (longshot bias).
   - Time-to-expiry coefficient: $\beta = +0.0041$ per day ($t = 2.89, p = 0.004$), showing that overpricing expands with time horizon.

4. **Delta-Hedged Arbitrage Proxy Backtest:**
   - Total trades executed: 16 trades across pooled sample.
   - Gross cumulative PnL: $1.649$ units of notional.
   - Net cumulative PnL: $1.113$ units after all transaction costs.
   - Net trade win rate: $69\%$.
   - Median trade holding period: $3.5$ hours.
   - Pooled net alpha: $0.067$ ($6.7\%$ mean net return relative to deployed notional, $t = 2.10, p = 0.053$, Newey-West HAC CI: $[-0.008, 0.143]$).

5. **Deribit & Ethereum Extensions:**
   - Deribit 3-market pooled BTC panel ($n = 2,585$): Mean discrepancy $\bar{D} = 0.1105$ (11.05 percentage points, HAC CI: $[0.074, 0.147]$).
   - Ethereum 4-market pooled panel ($n = 2,737$): Mean discrepancy $\bar{D} = 0.0129$ (1.29 percentage points, HAC CI: $[-0.000, 0.026]$), showing regime heterogeneity across individual monthly contracts.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Sample Size Limitation:** The exact Binance-compatible Bitcoin matched sample comprises only 3 contracts and 287 hourly observations from 2023. While the Deribit panel provides 2,585 observations, the sample represents specific market regimes.
- **Statistical Precision of Arbitrage Net Alpha:** Net alpha in the delta-hedged backtest achieves $t = 2.10$ ($p = 0.053$), which is marginally significant at the 10% level but misses the strict 5% significance threshold once conservative HAC intervals are applied ($[-0.008, 0.143]$).
- **Cross-Contract Heterogeneity in Ethereum:** The Ethereum exercise shows unstable discrepancy signs across contracts (negative in February 2023, positive in March 2023), indicating that mispricing is not uniformly positive across all crypto assets or time periods.

## Falsification plan

1. **Multi-Year Out-of-Sample Test (2024–2026):** Collect matched Polymarket and Binance/Deribit BTC and ETH threshold contracts across 2024–2026. The overpricing hypothesis is falsified if the mean pricing wedge $\bar{D}_t$ converges to zero within bid-ask bands ($|\bar{D}| < 1.0\%$, $t < 1.96$).
2. **Execution Friction Stress Test:** Apply realistic taker fees (20 bps Polymarket, 5 bps options, 5 bps spot) with 10–20 bps slippage per rebalance. If net arbitrage PnL turns negative, the apparent mispricing represents an unexploitable limit-to-arbitrage band rather than actionable alpha.
3. **Stochastic Volatility / Jump Robustness:** Replace Black-Scholes inversion with a local volatility or Bates jump-diffusion model calibrated to the full option smile. If model-implied binary prices match Polymarket prices ($D_t^{Bates} \approx 0$), the observed wedge was an artifact of Black-Scholes skew omission.

## Crypto portability

direct

The study is conducted directly on cryptocurrency derivatives (Binance European options, Deribit options, and Polymarket blockchain prediction markets) for Bitcoin and Ethereum.

## Limitations

- **Not independently reproduced.**
- **Model-Dependent Benchmark:** Uses Black-Scholes implied volatility inversion as the baseline; while conservative with respect to positive skew, extreme tail jumps could alter the theoretical binary price.
- **Oracle vs Exchange Settlement Discrepancy:** Polymarket contracts resolve via decentralized oracle feeds (e.g. UMA), whereas exchange options settle on calculated spot index TWAPs, introducing basis/dispute risk during extreme volatility spikes.
- **Capital Fragmentation:** Executing a 3-leg trade (Polymarket binary + centralized vanilla call + spot delta hedge) requires maintaining margin across multiple on-chain and centralized venues.

## Implementation status

No implementation in our research stack has been completed.

## Adoption boundary

Research material only.

A record being present in this repository does NOT mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

## Related Wiki records

- `[[quant/bitcoin-options-implied-volatility-risk-reversal-skew-2026-09-01]]`
- `[[quant/crypto-deribit-options-volatility-of-volatility-vov-realized-quarticity-2026-09-01]]`
- `[[quant/crypto-options-volatility-risk-premium-zscore-2026-08-31]]`
- `[[quant/defi-on-chain-options-mispricing-hegic-arbitrum-2026-09-01]]`
- `[[quant/crypto-cex-dex-cross-venue-funding-spread-carry-2026-08-31]]`
- `[[quant/cross-exchange-crypto-spatial-arbitrage-2026-08-31]]`

## Sources

1. Portnaya, Victoria. "Do Prediction Markets Match Option Prices? Bitcoin Threshold Evidence from Binance and Polymarket." arXiv:2606.19517v1 [q-fin.TR], June 17, 2026.
   - URL: https://arxiv.org/abs/2606.19517
   - Key tables & sections: Section 2.2 (contract mapping & sample), Section 3 (analytical benchmark & delta-method standard errors, Propositions A.1–A.5), Section 4 (Tables 2, 3, 4, 5: main market $t=6.46$, pooled panel $t=8.24$, cross-sectional regression), Section 5 (Table 6: delta-hedged proxy backtest, 16 trades, net PnL 1.113, net alpha 0.067), Section 6 (Tables 7: Deribit extension mean gap 11.05%, Ethereum exercise).
2. Binance Data Archive: Historical options and spot archives (`EOHSummary`, BTCUSDT hourly bars): https://data.binance.vision
3. Polymarket: Public transaction-level trade data and resolution archives: https://polymarket.com
