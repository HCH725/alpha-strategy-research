---
schema: strategy-research-record-v1
title: Crypto Intraday State-Dependent Momentum and Jump Reversal Timing
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - intraday
  - momentum
  - reversal
  - jumps
  - state-dependent
  - microstructure
status: research-only
confidence: medium
source_as_of: 2022-11
sources:
  - "https://doi.org/10.1016/j.najef.2022.101733"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Intraday State-Dependent Momentum and Jump Reversal Timing

## Provenance

- **Primary Source:** Zhuzhu Wen, Elie Bouri, Yahua Xu, and Yang Zhao, "Intraday return predictability in the cryptocurrency markets: Momentum, reversal, or both," *The North American Journal of Economics and Finance*, Volume 62, Article 101733 (November 2022). DOI: [10.1016/j.najef.2022.101733](https://doi.org/10.1016/j.najef.2022.101733).
- **Core Subject:** High-frequency intraday return predictability and market state conditioning across Bitcoin (BTC), Ethereum (ETH), Litecoin (LTC), and Ripple (XRP) spanning March 3, 2013 to May 31, 2020.

## Economic mechanism

### Source-reported

Wen, Bouri, Xu, and Zhao (2022) document that return predictability in cryptocurrency intraday markets is not uniformly monotonic momentum or reversal, but exhibits distinct state-dependent regime shifts:

1. **Intraday Momentum in Calm Regimes:** Under regular continuous trading intervals with low-to-moderate volatility, price changes exhibit positive serial correlation (momentum). The authors attribute this continuation to the trading actions of late-informed investors who gradually incorporate new information into market prices.
2. **Intraday Reversal Following Jump Events:** When markets experience large, discrete intraday price jumps or severe liquidity dislocations, returns exhibit immediate and statistically significant mean reversion. The authors link this reversal to investor overconfidence and behavioral overreaction to non-fundamental noise shocks.
3. **Macroeconomic and Liquidity Conditioning:** The authors find that intraday predictability dynamics are sensitive to macroeconomic announcements (such as FOMC releases), prevailing market liquidity, and systemic stress events (e.g. the March 2020 COVID-19 liquidity shock).

### Research interpretation

The falsifiable hypothesis is that **information diffusion and liquidity replenishment operate across distinct intraday regimes**:

1. **Continuous Flow vs Discrete Shock Dichotomy:** Continuous order flow reflects gradual price discovery, generating short-term trend persistence over subsequent 15-minute to 60-minute intervals.
2. **Liquidity Vacuum and Overshooting Rebound:** Discontinuous price jumps exhaust available resting liquidity at top book levels, creating temporary pricing overshoots. As passive liquidity providers replenish the order book and aggressive directional flow subsides, prices mechanically mean-revert toward equilibrium.
3. **State-Dependent Filter:** A combined rule that switches between momentum (in diffusive continuous regimes) and contrarian reversal (in jump regimes) captures regime-specific alpha while avoiding trend-following into exhausted momentum spikes.

## Signal

The normalized state-dependent intraday timing signal is structured as follows:

1. **Intraday Sampling & Return Calculation:**
   For a given crypto asset $i$, sample prices at high-frequency intervals $\Delta t$ (e.g. 15-minute, 30-minute, or 60-minute bars):
   $$r_{i,t} = \ln\left(\frac{P_{i,t}}{P_{i,t-1}}\right)$$

2. **Local Volatility & Jump Metric:**
   Estimate rolling local intraday volatility $\sigma_{i,t}$ using a backward-looking window of $N$ intervals (e.g. 96 intervals of 15-minute bars for a 24-hour baseline, or realized bipower variation):
   $$\sigma_{i,t} = \sqrt{\frac{1}{N-1}\sum_{k=0}^{N-1} (r_{i,t-k} - \bar{r}_{i,t})^2}$$
   Compute the standardized jump test metric:
   $$J_{i,t} = \frac{|r_{i,t}|}{\sigma_{i,t}}$$

3. **State-Dependent Directional Decision Rule:**
   Define a jump threshold $\tau_{\text{jump}}$ (e.g. $\tau_{\text{jump}} = 2.5$ standard deviations):
   - **Continuous Regime ($J_{i,t} \le \tau_{\text{jump}}$):** Follow intraday momentum:
     $$S_{i,t+1} = \text{sign}(r_{i,t})$$
   - **Jump / Overreaction Regime ($J_{i,t} > \tau_{\text{jump}}$):** Fade the jump (contrarian reversal):
     $$S_{i,t+1} = -\text{sign}(r_{i,t})$$

4. **Execution & Rebalancing:**
   - Position $S_{i,t+1} \in \{-1, +1\}$ is entered at bar boundary $t$ (open of bar $t+1$).
   - The position is held for duration $\Delta t$ and updated at the close of bar $t+1$.

## Required data

- High-frequency intraday trade/candle data (1-minute, 5-minute, 15-minute, 30-minute, 60-minute OHLCV) for liquid cryptocurrencies (BTC, ETH, LTC, XRP, and major perpetual futures).
- Timestamps aligned to UTC without session gaps (24/7 continuous crypto markets).
- Bid-ask spread and order book depth data (for slippage evaluation).

## Execution assumptions

The source paper focuses on econometric predictability and empirical timing utility; institutional execution constraints remain **underspecified** in the primary publication:

- **Turnover & Frequency:** High-frequency intraday rebalancing (e.g. 15-min or 30-min intervals) generates substantial annual turnover.
- **Transaction Costs:** Full taker fee schedules (2–5 bps per trade) and bid-ask spreads are not deducted in raw benchmark regressions.
- **Execution Timing:** Assumes immediate next-bar execution at prevailing market prices without fill delays.
- **Shorting Mechanics:** Short exposure requires access to liquid perpetual futures contracts with stable borrow/funding rates.

## Evidence

### Source-reported

Wen, Bouri, Xu, and Zhao (2022) report:
- Statistically significant evidence of both intraday momentum and intraday reversal in Bitcoin returns across the 2013–2020 sample.
- Predictability extends out-of-sample and holds across other major digital assets (Ethereum, Litecoin, Ripple).
- Dynamic market-timing strategies exploiting state-dependent switching generate superior risk-adjusted economic value relative to static buy-and-hold and always-long benchmark strategies.
- Predictability patterns systematically shift during major volatility shocks (e.g., COVID-19 market panic) and FOMC announcements.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- High execution fees (especially retail taker tiers) can rapidly erode gross intraday timing profitability.
- Microstructure friction, exchange API latency, and bid-ask bounce at high frequencies can introduce spurious jump triggers if noise filters are not applied.
- Funding rate friction on perpetual contracts during strong market-wide trending regimes may penalize counter-trend reversal positions.

## Falsification plan

1. **Out-of-Sample Validation:** Test the state-dependent jump/momentum rule on out-of-sample 2021–2026 data across top 20 liquid Binance/Bybit perpetual contracts.
2. **Transaction Cost Stress Test:** Apply realistic fee tiers (0 bps maker, 2 bps taker, plus 1 bp simulated slippage). If net Sharpe ratio falls below 0.6, reject the strategy for production implementation.
3. **Parameter Stability & Ablation:** Evaluate performance across varying sampling frequencies ($\Delta t \in \{5\text{m}, 15\text{m}, 30\text{m}, 60\text{m}\}$) and jump thresholds ($\tau_{\text{jump}} \in [1.5, 3.5]$). If alpha exists only at a single narrow threshold, reject as overfitted.
4. **Benchmark Comparison:** Compare net risk-adjusted returns against a simple continuous time-series momentum (TSMOM) baseline and a simple sign-reversal baseline.

## Crypto portability

Direct. The primary study directly evaluates cryptocurrency market data (BTC, ETH, LTC, XRP).

## Limitations

- **Underspecified cost friction:** Primary source reports gross academic timing performance without comprehensive modeling of taker fees or exchange latency.
- **High turnover:** Frequent intraday position flipping requires high capital efficiency and automated algorithmic execution.
- **Unproven in live trading:** The model has not been validated in live production trading or in institutional-grade backtesting engines (e.g., NautilusTrader).

## Implementation status

Not implemented. No PyBroker, NautilusTrader, paper, testnet, or live trading implementation exists for this repository.

## Adoption boundary

Research-only. This record is staging material for research intake review and does not constitute an approved or profitable trading strategy.

## Related Wiki records

- `[[quant/bitcoin-intraday-time-series-momentum-volume-session-2026-08-31]]`
- `[[quant/crypto-intraday-sign-mean-reversion-15m-walk-forward-2026-09-01]]`
- `[[quant/crypto-cross-sectional-jump-diffusion-variance-decomposition-2026-08-31]]`
- `[[quant/crypto-cross-sectional-realized-signed-jump-good-bad-volatility-2026-09-01]]`

## Sources

- Wen, Z., Bouri, E., Xu, Y., & Zhao, Y. (2022). Intraday return predictability in the cryptocurrency markets: Momentum, reversal, or both. *The North American Journal of Economics and Finance*, 62, 101733. DOI: [https://doi.org/10.1016/j.najef.2022.101733](https://doi.org/10.1016/j.najef.2022.101733)
