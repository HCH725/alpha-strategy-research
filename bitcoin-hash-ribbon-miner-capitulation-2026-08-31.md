---
schema: strategy-research-record-v1
title: Bitcoin Hash Ribbon Miner Capitulation
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://www.lookintobitcoin.com/charts/hash-ribbons/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Hash Ribbon Miner Capitulation

## Provenance

- **Source:** LookIntoBitcoin (Hash Ribbons Indicator by Charles Edwards)
- **URL:** https://www.lookintobitcoin.com/charts/hash-ribbons/
- **Data As-Of:** 2026-08-31
- **Relevance:** Commonly cited macro network indicator used as a long-term bottoming signal for Bitcoin.

## Economic mechanism
### Source-reported

The source claims that when Bitcoin price declines significantly or mining difficulty increases, inefficient miners become unprofitable and are forced to shut off their rigs (miner capitulation). This causes the Bitcoin network hash rate to drop. Once the weak miners are shaken out, the hash rate stabilizes and recovers, signaling the end of the capitulation phase and historically marking macro market bottoms. The strategy aims to buy after the capitulation is over and hash rate momentum turns positive.

### Research interpretation

The hypothesized mechanism is a supply-side shock exhaustion. Miners are compulsory sellers of Bitcoin (to cover electricity and hardware costs). During capitulation, distressed miners dump their holdings and shut down, creating a temporary spike in selling pressure. Once this pressure is exhausted and hash rate recovers (indicating remaining miners are profitable and expanding), the structural selling pressure is reduced, allowing positive price momentum to take hold. This is a fundamental/network regime filter combined with a momentum confirmation.

## Signal

- **Network Metric:** Bitcoin Network Hash Rate.
- **Lookback:** 30-day Simple Moving Average (SMA) and 60-day SMA of Hash Rate.
- **Capitulation Phase (Regime Filter):** 30-day SMA crosses below 60-day SMA.
- **Recovery/Buy Signal:** 30-day SMA crosses back above 60-day SMA.
- **Price Confirmation:** Source indicates waiting for positive price momentum confirmation, but exact indicators are underspecified.
- **Exit:** Underspecified.
- **Holding Period:** Underspecified.

## Required data

- **Instrument:** Bitcoin (BTC).
- **Timeframe:** Daily.
- **Network Data:** Daily Bitcoin Network Hash Rate.
- **Market Data:** Daily BTC/USD OHLCV (if using price confirmation filters).
- **Point-in-time:** True historical hash rate data without lookahead bias.

## Execution assumptions

- **Execution Timing:** Underspecified.
- **Market Type:** Underspecified.
- **Slippage & Impact:** Underspecified.
- **Fees:** Underspecified.

## Evidence
### Source-reported

The source presents the transition from miner capitulation to hash-rate recovery, together with improving Bitcoin price, as a long-term accumulation opportunity and notes historical association with macro lows.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed source; absence is not evidence of no negative result. The number of distinct historical miner-capitulation regimes is limited, so statistical confidence should be treated cautiously.

## Falsification plan

- **Required Sample:** Backtest over all available Bitcoin history, separating price-driven capitulations from external shock capitulations.
- **Baseline:** Compare returns against a simple buy-and-hold strategy and a standard trend-following baseline (e.g., 200-day SMA crossover).
- **Failure Metric:** If the strategy fails to provide a higher risk-adjusted return (Sharpe/Sortino) or lower maximum drawdown than buy-and-hold over multiple market cycles.
- **Ablation Test:** Test the signal with and without the price momentum confirmation filter to isolate the value of the network data vs. simple price trend.

## Crypto portability

direct

Directly applicable to Bitcoin. May be adapted to other Proof-of-Work cryptocurrencies (e.g., Dogecoin, Litecoin) if their miner economics mirror Bitcoin's, but largely inapplicable to Proof-of-Stake assets like Ethereum.

## Limitations

- sample size very small
- underspecified exit rules
- not independently reproduced

## Implementation status

not-implemented

## Adoption boundary

research-only

## Related Wiki records

## Sources

- https://www.lookintobitcoin.com/charts/hash-ribbons/
