---
schema: strategy-research-record-v1
title: Cross-Exchange Crypto Spatial Arbitrage
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - arbitrage
  - cross-exchange
  - spatial-arbitrage
  - market-microstructure
  - limits-to-arbitrage
status: research-only
confidence: high
source_as_of: 2020-02
sources:
  - https://doi.org/10.1016/j.jfineco.2019.07.001
  - https://doi.org/10.1111/j.1540-6261.1997.tb03807.x
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Exchange Crypto Spatial Arbitrage

## Provenance

Primary source: Igor Makarov and Antoinette Schoar, “Trading and arbitrage in cryptocurrency markets,” *Journal of Financial Economics* 135(2), 293–319 (2020). DOI: https://doi.org/10.1016/j.jfineco.2019.07.001.

Foundational and related literature:
- Andrei Shleifer and Robert W. Vishny, “The Limits of Arbitrage,” *The Journal of Finance* 52(1), 35–55 (1997). DOI: https://doi.org/10.1111/j.1540-6261.1997.tb03807.x.
- Carol Alexander and Daniel Heck, “Price discovery in Bitcoin: Spot or derivatives?,” *Journal of International Money and Finance* 109, 102247 (2020). DOI: https://doi.org/10.1016/j.jinfom.2020.102247.

The primary study provides an empirical and theoretical analysis of persistent price deviations across 34 cryptocurrency exchanges globally, documenting recurring arbitrage spreads driven by capital controls, fiat payment processing friction, and market segmentation.

## Economic mechanism

### Source-reported

Makarov and Schoar (2020) show that cryptocurrency prices across major exchanges worldwide often deviate substantially from the law of one price. While Bitcoin is an identical digital asset, price spreads between exchanges in different geographic regions frequently reach several percentage points (and over 10–20% during high-volatility retail runs, such as the Korean Kimchi Premium).

The authors demonstrate that:
1. Deviations are primarily driven by localized retail order flow imbalances on regional exchanges (e.g. Korea, Japan, Europe vs US).
2. The spreads do not immediately close because of severe *limits to arbitrage*: capital controls, anti-money laundering fiat transfer delays, exchange counterparty risk, and blockchain transaction finality latency.
3. Arbitrageurs who maintain pre-funded balances on multiple exchanges can earn recurring spatial arbitrage returns by buying on the discounted exchange and selling on the premium exchange.

### Research interpretation

The hypothesized mechanism is spatial cross-venue price divergence under localized order flow pressure and structural capital-mobility frictions:
1. When an exchange experiences a sudden surge in uncoordinated retail buying/selling, its local order book shifts away from the global consensus fair value.
2. If the net spread $S_{A,B}$ between Exchange B (premium) and Exchange A (discount) exceeds the sum of maker/taker trading fees, fiat FX conversion costs, and capital opportunity costs, a risk-neutral arbitrageur can capture the spread.
3. In a *statistical inventory rebalancing* mode, the arbitrageur maintains standing inventory of base crypto and quote fiat/stablecoins on both venues, executing simultaneous opposing fills without waiting for on-chain block transfers.
4. When inventory becomes skewed across venues, inventory is periodically rebalanced during low-volatility or negative-spread intervals.

## Signal

1. **Exchange Pair Definition**:
   - Pair of exchanges $(A, B)$ trading the same asset (e.g. BTC/USDT on Binance vs BTC/USD on Coinbase, or BTC/KRW on Upbit converted to USD at the interbank FX rate).

2. **Real-time Net Spread Calculation**:
   - Let $P_A^{\text{ask}}$ be the best ask price on Exchange A (cost to buy).
   - Let $P_B^{\text{bid}}$ be the best bid price on Exchange B (revenue to sell).
   - Compute the gross percentage spread:
     $$S_{A,B}(t) = \frac{P_B^{\text{bid}}(t) - P_A^{\text{ask}}(t)}{P_A^{\text{ask}}(t)}$$
   - Total friction threshold:
     $$\Theta_{A,B} = \text{Fee}_A^{\text{taker}} + \text{Fee}_B^{\text{taker}} + \text{Slippage}_A + \text{Slippage}_B + \text{FXSpread} + \text{HedgeBuffer}$$

3. **Entry Signal**:
   - Trigger simultaneous BUY on A and SELL on B when:
     $$S_{A,B}(t) > \Theta_{A,B} + \epsilon_{\text{hurdle}}$$
   - where $\epsilon_{\text{hurdle}} > 0$ is a safety hurdle (e.g., 15–30 bps).

4. **Position Sizing and Order Routing**:
   - Maximum trade size $Q_t = \min(Q_A^{\text{depth}}(P_A^{\text{ask}}), Q_B^{\text{depth}}(P_B^{\text{bid}}), \text{AvailableFiat}_A / P_A, \text{AvailableCrypto}_B)$.
   - Fills executed via IOC (Immediate-Or-Cancel) or FOK (Fill-Or-Kill) limit orders to prevent leg-out execution risk.

5. **Inventory Unwind / Convergence**:
   - Spread convergence to $|S_{A,B}(t)| < \Theta_{\text{exit}}$ locks in PnL.
   - Cross-exchange rebalancing transfers initiated via fast layer-1/layer-2 networks or OTC settlement networks (e.g., Fireblocks / Copper ClearLoop) when inventory imbalances exceed 70% of capacity.

6. **Specification status**: **fully specified** for spatial spread measurement and simultaneous execution; **underspecified** regarding dynamic inter-exchange liquidity rebalancing schedules.

## Required data

- Sub-second Level 2 order book feeds (top 10 levels of depth) from target exchange venues.
- WebSocket trade feeds for fill and latency monitoring.
- Real-time interbank fiat foreign exchange rates (e.g. KRW/USD, EUR/USD, JPY/USD) where cross-currency pairs are traded.
- Dynamic fee tier schedule metadata for maker/taker fees and on-chain withdrawal gas fees.

## Execution assumptions

- Pre-positioned inventory: Capital must be split across venues; no waiting for blockchain confirmation during trade entry.
- Sub-50ms round-trip API latency to minimize leg execution failure (one leg filling while the other moves).
- Fiat/stablecoin fungibility: Assumes USDT/USDC/USD parity or explicitly includes basis adjustment.

## Evidence

### Source-reported

Makarov and Schoar (2020) document:
- Cross-exchange Bitcoin price deviations frequently averaged 1–3% between major international exchanges (e.g. Bitfinex, Coinbase, Kraken, Bitstamp) during 2017–2018.
- Deviations between Korean exchanges (e.g. Bithumb, Coinone) and US exchanges regularly reached 10% to 20% due to strict Korean capital control regulations (Foreign Exchange Transactions Act).
- Volume on premium exchanges was positively correlated with the magnitude of the spread, indicating demand shocks rather than thin-order-book noise.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Legging risk (execution slippage on leg 2) can turn an apparently profitable spread negative if the opposing venue's order book moves during order transit.
- Capital drag / inventory opportunity cost: Holding split unhedged fiat and crypto buffers across multiple venues lowers overall portfolio capital efficiency.
- Exchange counterparty and withdrawal-freeze risk (e.g., historical exchange insolvency events during market stress).

## Falsification plan

The strategy hypothesis should be considered falsified or economically unviable if:
1. Real-time net spread after accounting for maker/taker fees (e.g. 5–10 bps per side) and real-time slippage rarely exceeds the total friction hurdle ($< 5$ occurrences per week for top-tier pairs).
2. The cost of periodic inter-exchange inventory rebalancing (withdrawal fees, network gas, capital lockup during transfer) exceeds the gross spatial arbitrage capture.
3. Adverse selection on taker fills results in a negative realized post-fee spread in over 40% of executed pairs.

## Crypto portability

**Direct**: The strategy is natively derived from cryptocurrency exchange microstructure and fragmentation.

Portability adaptations:
- CEX-to-CEX spot vs spot.
- CEX-to-CEX spot vs perpetual futures (where short leg is executed via perp short without requiring physical spot inventory).
- CEX-to-DEX spatial arbitrage (e.g., CEX vs Uniswap/Hyperliquid), subject to blockchain block-inclusion latency.

## Limitations

- **not independently reproduced**: requires empirical tick-level order book analysis across paired venues.
- **capital fragmentation**: requires substantial pre-funded capital allocated across multiple custodial venues.
- **leg-out execution risk**: latency discrepancies between venue APIs can cause unhedged market exposure.

## Implementation status

No implementation in PyBroker, NautilusTrader, or any internal research/backtesting pipeline has been performed.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material only. It does not represent a validated production strategy, an execution authorization, or approval for Paper, Testnet, or Live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

- `[[crypto-cex-dex-cross-venue-funding-spread-carry-2026-08-31]]`
- `[[crypto-perpetual-no-arbitrage-deviation-2026-08-31]]`
- `[[crypto-multilevel-order-flow-imbalance-intraday-2026-08-31]]`

## Sources

1. Igor Makarov and Antoinette Schoar, “Trading and arbitrage in cryptocurrency markets,” *Journal of Financial Economics* 135(2), 293–319 (2020). DOI: https://doi.org/10.1016/j.jfineco.2019.07.001
2. Andrei Shleifer and Robert W. Vishny, “The Limits of Arbitrage,” *The Journal of Finance* 52(1), 35–55 (1997). DOI: https://doi.org/10.1111/j.1540-6261.1997.tb03807.x
3. Carol Alexander and Daniel Heck, “Price discovery in Bitcoin: Spot or derivatives?,” *Journal of International Money and Finance* 109, 102247 (2020). DOI: https://doi.org/10.1016/j.jinfom.2020.102247
