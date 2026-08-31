---
schema: strategy-research-record-v1
title: Crypto Sentiment Extremity Bid-Ask Spread and Adverse Selection Premium
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - market-microstructure
  - sentiment-extremity
  - bid-ask-spread
  - adverse-selection
  - fear-and-greed
status: research-only
confidence: medium
source_as_of: 2026-07
sources:
  - https://arxiv.org/abs/2602.07018
  - https://doi.org/10.48550/arXiv.2602.07018
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Sentiment Extremity Bid-Ask Spread and Adverse Selection Premium

## Provenance

Primary source: Murad Farzulla (Dissensus AI and King's College London), "The Extremity Premium: Sentiment Regimes and Adverse Selection in Cryptocurrency Markets", arXiv preprint arXiv:2602.07018 [q-fin.TR], first submitted February 2026, revised v3 July 2026. DOI: https://doi.org/10.48550/arXiv.2602.07018. Under review at *Computational Economics*.

The research analyzes the empirical relationship between market-wide investor sentiment regimes and market microstructure liquidity across Bitcoin (BTC/USDT) and Ethereum (ETH/USDT) from February 2018 to January 2026, utilizing the Alternative.me Crypto Fear & Greed Index (CFGI) and high-low effective spread estimators.

## Economic mechanism

### Source-reported

Farzulla (2026) documents an "extremity premium" in cryptocurrency markets: periods characterized by extreme investor sentiment—both extreme fear and extreme greed—exhibit systematically wider bid-ask spreads than neutral sentiment periods. The author demonstrates that sentiment extremity predicts excess uncertainty in market-maker spread setting that persists even after controlling for realized volatility. 

The primary mechanism is adverse selection and inventory risk management by liquidity providers. During extreme sentiment regimes, market makers face heightened uncertainty regarding information quality and one-sided directional order flow (panic selling during extreme fear or FOMO buying during extreme greed). In response, market makers widen quoted spreads or withdraw depth to protect against toxic informed flow and rapid inventory depletion. The paper finds that the intensity of sentiment (distance from neutral), rather than its directional polarity, drives this liquidity contraction.

### Research interpretation

The falsifiable hypothesis is that **market maker quoting behavior and execution costs in crypto are non-linearly governed by sentiment extremity $|\text{CFGI}_t - 50|$ independently of trailing realized volatility**:

1. **U-Shaped Microstructure Spread Function**: Quoted and effective spreads $S_t$ expand symmetrically when sentiment deviates significantly from neutrality ($S_t = f(|\text{CFGI}_t - 50|)$).
2. **Adverse Selection & Toxicity Filter**: In extreme sentiment regimes ($\text{CFGI}_t < 25$ or $\text{CFGI}_t > 75$), passive liquidity provision suffers elevated adverse selection, whereas taker execution incurs structural spread penalties.
3. **Regime-Conditioned Strategy Architecture**:
   - **Market Making / Liquidity Provision**: Widen quote offsets and reduce position inventory limits during extreme sentiment regimes to capture higher spread compensation while mitigating inventory skew.
   - **Execution Cost Mitigation**: Defer non-urgent portfolio rebalancing orders during extreme sentiment regimes to avoid paying peak liquidity premiums.
   - **Volatility / Spread Expansion Alpha**: Take long volatility or straddle positions when sentiment shifts rapidly from neutral into extreme regimes.

## Signal

Normalized source-faithful signal and regime definitions:

1. **Sentiment Metric**: Daily Crypto Fear & Greed Index $\text{CFGI}_t \in [0, 100]$.
2. **Sentiment Extremity Score ($E_t$)**:
   $$E_t = \frac{|\text{CFGI}_t - 50|}{50} \in [0, 1]$$
3. **Sentiment Regimes**:
   - *Extreme Fear*: $\text{CFGI}_t \in [0, 25)$ (or lowest quintile $Q_1$)
   - *Fear*: $\text{CFGI}_t \in [25, 45)$
   - *Neutral*: $\text{CFGI}_t \in [45, 55]$ (baseline)
   - *Greed*: $\text{CFGI}_t \in (55, 75]$
   - *Extreme Greed*: $\text{CFGI}_t \in (75, 100]$ (or highest quintile $Q_5$)
4. **Effective Spread Estimation (Corwin–Schultz High-Low Estimator)**:
   $$\beta_t = \sum_{j=0}^1 \left[\ln\left(\frac{H_{t-j}}{L_{t-j}}\right)\right]^2$$
   $$\gamma_t = \left[\ln\left(\frac{\max(H_t, H_{t-1})}{\min(L_t, L_{t-1})}\right)\right]^2$$
   $$\alpha_t = \frac{\sqrt{2\beta_t} - \sqrt{\beta_t}}{3 - 2\sqrt{2}} - \sqrt{\frac{\gamma_t}{3 - 2\sqrt{2}}}$$
   $$S_t^{\text{CS}} = \frac{2(e^{\alpha_t} - 1)}{1 + e^{\alpha_t}}$$
5. **Operational Signal Rules**:
   - **Liquidity Provision Regime**: When $E_t > 0.50$ ($\text{CFGI}_t < 25$ or $\text{CFGI}_t > 75$), expand quoting spread multiplier by $1.5\times - 2.0\times$ and tighten inventory hold time.
   - **Taker Execution Filter**: When $E_t > 0.50$, restrict rebalance execution to limit/maker orders only; defer taker market orders until $E_t \le 0.50$.
   - **Spread Compression Mean-Reversion**: If $S_t^{\text{CS}}$ is at top decile while $E_t$ begins mean-reverting toward 0, enter mean-reverting tight-spread market-making posture.

Exact quantitative quoting parameters and rebalancing thresholds not explicitly detailed in the source paper remain **underspecified**.

## Required data

- **Sentiment Data**: Daily Crypto Fear & Greed Index (CFGI) time series from Alternative.me or equivalent aggregated sentiment index.
- **Microstructure / Price Data**: Daily and intraday (1m / 1s / tick) OHLCV prices, high-low series, and order book depth (L2/L3) for major crypto pairs (BTC/USDT, ETH/USDT).
- **Spread Metrics**: Quoted bid-ask spread, effective spread, and Corwin–Schultz high-low spread estimates.
- **Timestamp Synchronization**: Alignment between daily CFGI index publication timestamp (00:00 UTC) and exchange market data.

## Execution assumptions

- Continuous 24/7 centralized spot and perpetual exchange execution (e.g. Binance BTC/USDT, ETH/USDT).
- Signal-to-order timing: Daily rebalance / regime classification applied at 00:05 UTC post-index release.
- Order types: Passive limit orders for liquidity provision; taker avoidance rules during extreme regimes.
- Transaction costs: Modeling of VIP maker/taker fee tiers (e.g., 0–2 bps maker, 2–4 bps taker) and adverse selection slippage.

## Evidence

### Source-reported

- Evaluated on Bitcoin daily data from February 2018 to January 2026, with out-of-sample robustness checks on Ethereum.
- Bid-ask spreads (estimated via Corwin–Schultz) are statistically significantly wider during both Extreme Fear and Extreme Greed regimes compared to Neutral regimes.
- Within-volatility-quintile stratification confirms that the extremity premium is not an artifact of contemporaneous realized volatility: across low, medium, and high volatility quintiles, spreads remain elevated in extreme sentiment states.
- Non-parametric tests and Granger causality confirm predictive power of sentiment extremity on subsequent spread widening.
- The author notes that while non-parametric stratification robustly preserves the extremity premium, extensive parametric regression specifications can absorb regime coefficients, indicating non-linear threshold dynamics.

All empirical findings above are **source-reported** by Farzulla (2026) and have not been independently verified.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed primary source.

Absence of reported negative evidence is not evidence of absence. Potential failure modes include:
- In linear parametric models without threshold splits, sentiment extremity coefficients may attenuate due to collinearity with high-frequency realized volatility spikes.
- CFGI is an aggregate daily composite; intraday flash crashes or sudden sentiment shifts intra-day will lag by up to 24 hours.
- Spreads on institutional venues (CME futures, institutional OTC) may behave differently from retail-dominated spot order books.

## Falsification plan

The hypothesis should be weakened or rejected if an independent point-in-time test demonstrates:

1. High-frequency L2 order book spreads (quoted and effective) on BTC/USDT show no statistically significant difference ($t < 2.0$) between extreme sentiment days ($E_t > 0.50$) and neutral days ($E_t < 0.10$) when controlling for 24-hour realized variance.
2. A market-making strategy adjusting quote widths based on $E_t$ yields lower risk-adjusted PnL or higher adverse selection than a standard volatility-only quoting model (e.g. Avellaneda–Stoikov).
3. The extremity premium fails to replicate across an expanded multi-asset altcoin panel or alternative crypto exchanges (e.g. OKX, Bybit, Coinbase).

## Crypto portability

**Direct**, as the phenomenon is specifically documented and analyzed on cryptocurrency spot pairs (BTC/USDT, ETH/USDT) using crypto-native sentiment indices.

Key operational considerations:
- CFGI index calculation methodology includes volatility, volume/momentum, social media, surveys, dominance, and Google trends; changes in index composition could alter regime stability.
- Perpetual futures funding rate dislocations often coincide with extreme sentiment regimes, compounding inventory carrying costs.

## Limitations

- **Not independently reproduced.**
- **Preprint status:** Working paper under review at *Computational Economics* (arXiv:2602.07018v3, July 2026).
- **underspecified:** Exact operational market-making quote offsets and dynamic inventory penalty functions are not fully parameterized in the source and must be calibrated in simulation.
- **Frequency mismatch:** Sentiment index is updated daily (once per 24 hours), limiting its responsiveness to sub-daily microstructure shocks.

## Implementation status

No implementation in our research stack has been completed.

## Adoption boundary

Research material only.

A record being present in this repository does **not** mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

## Related Wiki records

- `[[quant/market-microstructure-order-flow-imbalance]]`
- `[[quant/crypto-cross-sectional-sentiment-risk-beta-premium-2026-09-01]]`
- `[[quant/crypto-high-frequency-kyles-lambda-price-impact-reversal-2026-08-31]]`

## Sources

- Murad Farzulla, "The Extremity Premium: Sentiment Regimes and Adverse Selection in Cryptocurrency Markets", arXiv preprint arXiv:2602.07018 [q-fin.TR], July 2026. URL: https://arxiv.org/abs/2602.07018. DOI: https://doi.org/10.48550/arXiv.2602.07018.
- Alternative.me Crypto Fear & Greed Index API: https://alternative.me/crypto/fear-and-greed-index/.
