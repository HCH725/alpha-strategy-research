---
schema: strategy-research-record-v1
title: Bitcoin On-Chain Illiquid Supply Shock Ratio (ISSR) Supply Inelasticity Drift
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - onchain
  - supply-inelasticity
  - entity-adjusted
  - supply-shock
status: research-only
confidence: medium
source_as_of: 2021-06
sources:
  - "https://woobull.com/bitcoin-supply-shock-ratios/"
  - "https://insights.glassnode.com/quantifying-bitcoin-liquid-supply/"
  - "https://studio.glassnode.com/metrics?m=supply.LiquidIlliquidRatio"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin On-Chain Illiquid Supply Shock Ratio (ISSR) Supply Inelasticity Drift

## Provenance

- **Primary Source:** Willy Woo and William Clemente, "Bitcoin Supply Shock Ratios," Woobull Research & Blockware Intelligence (2021). [https://woobull.com/bitcoin-supply-shock-ratios/](https://woobull.com/bitcoin-supply-shock-ratios/).
- **Underlying On-Chain Liquidity Clustering Methodology:**
  - Rafael Schultze-Kraft and Glassnode Research, "Quantifying Bitcoin's Liquid and Illiquid Supply," *Glassnode Insights* (December 2020). [https://insights.glassnode.com/quantifying-bitcoin-liquid-supply/](https://insights.glassnode.com/quantifying-bitcoin-liquid-supply/).
  - Glassnode Studio Metric Reference: `supply.LiquidIlliquidRatio` / `supply.Illiquid` / `supply.Liquid`. [https://studio.glassnode.com/metrics?m=supply.LiquidIlliquidRatio](https://studio.glassnode.com/metrics?m=supply.LiquidIlliquidRatio).

The Illiquid Supply Shock Ratio ($ISSR$) models the structural availability of circulating Bitcoin by quantifying the ratio of coins locked in low-velocity investor entities relative to coins actively circulating in liquid exchange venues.

## Economic mechanism

### Source-reported

Glassnode (2020) defines an entity's liquidity $\Lambda$ as the ratio of cumulative historical outflows to cumulative historical inflows:
$$\Lambda = \frac{\sum \text{Outflows}}{\sum \text{Inflows}}$$

Entities are categorized into three liquidity classes:
1. **Highly Liquid:** $\Lambda > 0.75$ (e.g., centralized exchanges, high-frequency market makers, OTC trading desks).
2. **Liquid:** $0.25 < \Lambda \le 0.75$ (e.g., active traders, occasional spenders).
3. **Illiquid:** $\Lambda \le 0.25$ (e.g., long-term HODLers, cold storage institutional custodians).

Woo and Clemente (2021) formulated the Illiquid Supply Shock Ratio as:
$$ISSR = \frac{\text{Illiquid Supply}}{\text{Liquid Supply} + \text{Highly Liquid Supply}}$$

They report that when $ISSR$ increases, available floating supply on exchanges shrinks, causing market supply to become highly inelastic. If fiat demand remains constant or expands, price undergoes a positive upward adjustment ("supply shock"). Divergences between rising $ISSR$ and sideways/falling price historically signaled impending bullish mean-reversion catch-up rallies.

### Research interpretation

The falsifiable hypothesis is that **structural shifts in entity-adjusted supply liquidity create inventory depletion that leads spot price appreciation**:

1. **Microstructure Order Book Depletion:** As coins are transferred from exchange wallets (Liquid/Highly Liquid) into non-spending cold storage wallets (Illiquid), the aggregate depth of standing ask limit orders thins across trading venues.
2. **Supply-Side Inelasticity:** When active market buy flows meet a depleted liquid inventory, marginal price impact increases exponentially, driving upward drift.
3. **Distribution Leading Indicator:** When long-dormant entities begin moving coins back to exchanges, $ISSR$ flattens or rolls over before spot price tops, providing an early warning of impending supply overhang.

## Signal

The normalized signal computation is defined as follows:

1. **Daily Liquidity Supply Aggregation:**
   For day $t$, aggregate total circulating Bitcoin supply across entity classifications:
   - $S_{illiquid, t}$: Total BTC held by entities with $\Lambda \le 0.25$.
   - $S_{liquid\_total, t} = S_{liquid, t} + S_{high\_liquid, t}$: Total BTC held by entities with $\Lambda > 0.25$.

2. **ISSR Metric Calculation:**
   $$ISSR_t = \frac{S_{illiquid, t}}{S_{liquid\_total, t}}$$

3. **Normalized Shock Signal ($Z$-Score):**
   Calculate a rolling $N$-day ($N = 90$ or $180$ days) standardized $Z$-score of the ratio to detect structural acceleration:
   $$\mu_{ISSR, t} = \frac{1}{N} \sum_{k=0}^{N-1} ISSR_{t-k}$$
   $$\sigma_{ISSR, t} = \sqrt{\frac{1}{N} \sum_{k=0}^{N-1} (ISSR_{t-k} - \mu_{ISSR, t})^2}$$
   $$Z_{ISSR, t} = \frac{ISSR_t - \mu_{ISSR, t}}{\sigma_{ISSR, t}}$$

4. **Strategy Position Rules:**
   - **Bullish Regime (Supply Shock Absorption):** If $Z_{ISSR, t} > +1.0$, maintain or increase Long allocation (1.0x).
   - **Neutral Regime:** If $-1.0 \le Z_{ISSR, t} \le +1.0$, maintain base holding (0.5x).
   - **Bearish / Distribution Regime (Supply Inundation):** If $Z_{ISSR, t} < -1.0$, reduce allocation to 0.0x (cash/stablecoins) or hedge.

## Required data

- Entity-adjusted on-chain supply data (`supply.Illiquid`, `supply.Liquid`, `supply.HighlyLiquid`) sampled daily at UTC 00:00.
- Daily Bitcoin OHLCV price series.
- Strict point-in-time clustering snapshots without lookahead clustering updates.

## Execution assumptions

- Daily rebalancing evaluated and executed at UTC 00:00.
- Low-turnover spot execution or unleveraged perpetual futures holding.
- Execution slippage and taker fees are minimal ($< 5$ bps per adjustment).

## Evidence

### Source-reported

- Woo and Clemente (2021) reported that $ISSR$ led major Bitcoin price rallies in late 2020 and early 2021, showing high correlation with forward cycle valuations.
- Glassnode Research (2020) documented that over 14.5 million BTC (78% of circulating supply at the time) was held by illiquid entities, establishing that only a small fraction of circulating supply actively determines marginal market pricing.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Entity Clustering Restatement Risk:** On-chain clustering algorithms identify wallet clusters heuristically. As new clustering heuristics or transaction graph links are discovered, entity boundaries can be retroactively adjusted, introducing lookahead bias if raw point-in-time snapshots are not preserved.
- **Institutional Custody Noise:** Structural reorganizations (e.g. ETF custodians shifting coins between internal cold storage accounts or multi-sig vault rotations) can cause discrete spikes in illiquid supply without representing true market accumulation.

## Falsification plan

1. **Point-in-Time Backtest:** Test $Z_{ISSR}$ on immutable point-in-time daily on-chain snapshots from 2021 to 2026 without retroactive clustering modifications.
2. **Cross-Factor Spanning Regression:** Test whether $Z_{ISSR}$ provides statistically significant incremental predictive power for forward 30-day and 60-day Bitcoin returns when controlling for Exchange Net Inflow, MVRV Z-Score, and 30-day Price Momentum.
3. **Custody Reorganization Filtering:** Implement an anomaly filter to detect single-day entity reclassifications exceeding $50,000$ BTC; test if signal performance degrades when large non-market vault transfers are excluded.

## Crypto portability

Direct. The metric is native to the Bitcoin UTXO and entity clustering structure.

## Limitations

- **Heuristic Sensitivity:** Entity clustering depends on proprietary heuristics (e.g. change-address detection, common-input-ownership heuristics).
- **Macro Horizon:** Evaluates structural supply trends over multi-week to multi-month windows; ineffective for intraday or short-term momentum trading.

## Implementation status

Not implemented. No PyBroker, NautilusTrader, paper, testnet, or live trading implementation exists for this repository.

## Adoption boundary

Research-only. This record is staging material for review and does not constitute an approved or profitable trading strategy.

## Related Wiki records

- `[[quant/bitcoin-onchain-cointime-aviv-ratio-true-market-mean-2026-09-01]]`
- `[[quant/bitcoin-onchain-reserve-risk-hodl-conviction-2026-08-31]]`
- `[[quant/bitcoin-onchain-rhodl-ratio-macro-cycle-2026-08-31]]`
- `[[quant/ethereum-exchange-net-inflow-bearish-drift-1h-6h-2026-09-01]]`

## Sources

- Woo, W., & Clemente, W. (2021). *Bitcoin Supply Shock Ratios*. Woobull Research. [https://woobull.com/bitcoin-supply-shock-ratios/](https://woobull.com/bitcoin-supply-shock-ratios/)
- Schultze-Kraft, R., & Glassnode Research. (2020). *Quantifying Bitcoin's Liquid and Illiquid Supply*. Glassnode Insights. [https://insights.glassnode.com/quantifying-bitcoin-liquid-supply/](https://insights.glassnode.com/quantifying-bitcoin-liquid-supply/)
- Glassnode Studio. (2024). *Liquid to Illiquid Supply Ratio Guide*. [https://studio.glassnode.com/metrics?m=supply.LiquidIlliquidRatio](https://studio.glassnode.com/metrics?m=supply.LiquidIlliquidRatio)
