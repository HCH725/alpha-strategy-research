---
schema: strategy-research-record-v1
title: Bitcoin Mayer Multiple Macro Valuation Bands and Cycle Mean Reversion
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - valuation-ratios
  - macro-cycle
  - mean-reversion
status: research-only
confidence: medium
source_as_of: 2024-06
sources:
  - "https://www.themayermultiple.com"
  - "https://charts.woobull.com/bitcoin-mayer-multiple"
  - "https://studio.glassnode.com/metrics?m=market.PriceMayerMultiple"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Mayer Multiple Macro Valuation Bands and Cycle Mean Reversion

## Provenance

- **Primary Source:** Trace Mayer (2015), who introduced the Mayer Multiple ($MM = \text{Price} / \text{SMA}_{200}$) as an empirical macro valuation ratio to identify cyclical overextension and undervaluation in Bitcoin.
- **Data & Metric Documentation:**
  - The Mayer Multiple Portal: [https://www.themayermultiple.com](https://www.themayermultiple.com)
  - Woobull Charts: [https://charts.woobull.com/bitcoin-mayer-multiple](https://charts.woobull.com/bitcoin-mayer-multiple)
  - Glassnode Studio: [https://studio.glassnode.com/metrics?m=market.PriceMayerMultiple](https://studio.glassnode.com/metrics?m=market.PriceMayerMultiple)

The Mayer Multiple represents one of the earliest widely tracked macro valuation metrics in cryptocurrency quantitative analysis, measuring the distance between current spot price and its 200-day simple moving average.

## Economic mechanism

### Source-reported

Trace Mayer hypothesized that Bitcoin’s price tends to mean-revert around its 200-day moving average, which acts as a proxy for the long-term cost basis and trend consensus of the market. Historical analysis showed that whenever Bitcoin rose beyond 2.4 times its 200-day moving average, the market was in an unsustainable speculative mania that culminated in significant cycle tops and subsequent multi-year drawdowns. Conversely, values below 1.0 (and especially below 0.6–0.8) represented cyclical capitulation and optimal accumulation regimes.

### Research interpretation

The falsifiable hypothesis is that **long-term moving average anchoring and cyclical leverage exhaustion create bounded macro mean-reversion dynamics**:

1. **200-Day SMA as Consensus Equilibrium:** The 200-day moving average spans approximately 6.5 months of continuous 24/7 trading, capturing the smoothed cost basis of active market participants and smoothing out short-term narrative volatility.
2. **Speculative Overextension Threshold ($MM > 2.4$):** Extreme price divergence from the 200-day SMA ($> 140\%$ premium) is accompanied by excessive leverage in derivatives markets, unsustainable funding costs, and retail FOMO. When marginal buying power exhausts, mean reversion toward the 200-day trend is rapid and severe.
3. **Capitulation Discount ($MM < 0.8$):** A 20%+ discount below the 200-day SMA typically reflects broad market panic, miner distress, and forced liquidations, creating high-conviction asymmetric accumulation zones for long-term capital.

## Signal

The rule set can be implemented as a tiered multi-regime capital allocation model:

1. **Metric Definition:**
   For daily closing price $P_t$ at UTC 00:00:
   $$SMA_{200}(P)_t = \frac{1}{200} \sum_{k=0}^{199} P_{t-k}$$
   $$MM_t = \frac{P_t}{SMA_{200}(P)_t}$$

2. **Historical Threshold Tiers:**
   - **Deep Bear / Capitulation Accumulation ($MM_t < 0.8$):** Allocate maximum capital weight (e.g. $1.25\times$ to $1.5\times$ target exposure).
   - **Fair Value / Bull Expansion ($0.8 \le MM_t < 1.5$):** Maintain base target exposure ($1.0\times$).
   - **Elevated Valuation / De-risking ($1.5 \le MM_t < 2.4$):** Scale down exposure (e.g. $0.5\times$ target exposure).
   - **Euphoric Cycle Top / Extreme Overheat ($MM_t \ge 2.4$):** Exit to cash / stablecoins or initiate hedging ($0.0\times$ exposure).

3. **Rebalancing Frequency:** Evaluated and rebalanced at the daily UTC 00:00 boundary.

## Required data

- Daily spot Bitcoin price history (OHLCV) with at least 200 consecutive daily bars prior to signal formation.
- Reliable UTC 00:00 daily closing prices from major aggregate spot indices (e.g. Coinbase, Binance, Bitstamp).

## Execution assumptions

- Daily rebalancing at next-bar open (UTC 00:01).
- Spot market execution or 1x unleveraged perpetual futures (to eliminate liquidation risk during macro bear drawdowns).
- Slippage and taker fees for daily/weekly low-turnover adjustments are minimal (typically $< 5$ bps per trade).

## Evidence

### Source-reported

- Trace Mayer's simulations demonstrated that buying and holding only when $MM < 2.4$ avoided catastrophic peak-to-trough drawdowns during the 2011, 2013, and 2017 bear markets while capturing the vast majority of cyclical bull run gains.
- Historical distribution data on Woobull and Glassnode indicates that the all-time median Mayer Multiple is approximately **1.30–1.40**, with values exceeding 2.4 occurring on less than 5% of historical days, predominantly coinciding with parabolic cycle blow-offs.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Cycle Volatility Compression:** As Bitcoin's market capitalization has grown and institutional participation expanded, cyclical peak Mayer Multiples have trended downward (e.g., peak MM in the 2021 bull market reached ~2.4–2.5 briefly, whereas earlier cycles reached 4.0–6.0). Static thresholds like 2.4 risk missing cycle peaks in lower-volatility regimes.
- **Whipsaws around 1.0:** In extended sideways consolidation markets, the metric may oscillate repeatedly around 1.0, generating unnecessary rebalancing turnover if narrow bands are used without hysteresis.

## Falsification plan

1. **Static vs Rolling Percentile Test:** Compare the fixed $2.4$ threshold against a rolling 3-year 95th percentile threshold across 2011–2026 data. If rolling percentile adaptation significantly outperforms static thresholds, reject static threshold validity.
2. **Benchmark Comparison:** Test whether Mayer Multiple timing generates statistically significant risk-adjusted alpha over a simple 200-day trend-following SMA crossover strategy and a static buy-and-hold benchmark.
3. **Sub-Period Decay Analysis:** Evaluate Sharpe ratio and maximum drawdown reduction across post-2020 data to test whether institutional ETF flows have structurally altered 200-day moving average divergence dynamics.

## Crypto portability

Direct. The metric was formulated and developed specifically for Bitcoin market cycle analysis.

## Limitations

- **Low-Frequency Macro Signal:** Operates on multi-month/multi-year cycle horizons with low annual trade counts, requiring decade-long backtest samples to observe statistically meaningful cycle counts.
- **Threshold Sensitivity:** The choice of 2.4 was empirically derived from early Bitcoin cycles and may require recalibration for maturing market structures.

## Implementation status

Not implemented. No PyBroker, NautilusTrader, paper, testnet, or live trading implementation exists for this repository.

## Adoption boundary

Research-only. This record is staging material for review and does not constitute an approved or profitable trading strategy.

## Related Wiki records

- `[[quant/bitcoin-onchain-mvrv-zscore-cycle-reversal-2026-08-31]]`
- `[[quant/bitcoin-onchain-balanced-and-terminal-price-valuation-bands-2026-09-01]]`
- `[[quant/bitcoin-onchain-net-unrealized-profit-loss-nupl-macro-cycle-2026-09-01]]`
- `[[quant/bitcoin-onchain-cumulative-value-days-destroyed-cvdd-floor-2026-09-01]]`

## Sources

- The Mayer Multiple Portal. (2015–2024). *The Mayer Multiple: Bitcoin Valuation*. [https://www.themayermultiple.com](https://www.themayermultiple.com)
- Woobull Charts. (2024). *Bitcoin Mayer Multiple*. [https://charts.woobull.com/bitcoin-mayer-multiple](https://charts.woobull.com/bitcoin-mayer-multiple)
- Glassnode Studio. (2024). *Price Mayer Multiple Metric Guide*. [https://studio.glassnode.com/metrics?m=market.PriceMayerMultiple](https://studio.glassnode.com/metrics?m=market.PriceMayerMultiple)
