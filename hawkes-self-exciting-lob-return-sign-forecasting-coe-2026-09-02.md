---
schema: strategy-research-record-v1
title: "Hawkes Self-Exciting LOB Return Sign Forecasting via COE Model in Cryptocurrency Markets"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - hawkes-processes
  - limit-order-book
  - microstructure
  - return-forecasting
  - point-process
  - self-exciting
  - coe-model
status: research-only
confidence: medium
source_as_of: 2023-12-21
sources:
  - "Raffaele Giuseppe Cestari, Filippo Barchi, Riccardo Busetto, Daniele Marazzina, Simone Formentin, 'Hawkes-based cryptocurrency forecasting via Limit Order Book data', arXiv:2312.16190v1 [q-fin.ST, cs.CE, cs.LG], December 2023. https://arxiv.org/abs/2312.16190"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Hawkes Self-Exciting LOB Return Sign Forecasting via COE Model in Cryptocurrency Markets

## Provenance

- **Repository URL:** https://arxiv.org/abs/2312.16190v1
- **Full arXiv ID:** 2312.16190v1
- **Authors:** Raffaele Giuseppe Cestari, Filippo Barchi, Riccardo Busetto, Daniele Marazzina, Simone Formentin
- **Published:** 2023-12-21
- **Categories:** q-fin.ST, cs.CE, cs.LG
- **Data source:** Centralized cryptocurrency exchange, USDT/USD pair, LOB measurements
- **Source PDF:** https://arxiv.org/pdf/2312.16190v1

## Economic mechanism

### Source-reported

The authors propose that cryptocurrency LOB event arrivals (trade and limit order events) exhibit self-exciting dynamics — a burst of activity tends to trigger further activity — which can be captured by a Hawkes self-exciting point process. By modeling these event intensities and coupling them with a Continuous Output Error (COE) neural network model, the approach forecasts future return signs (direction) by leveraging predictions of future financial interactions (order flow). The non-uniformly sampled structure of LOB event data is preserved rather than aggregated into fixed-interval bars, preserving the temporal information content of inter-arrival times.

### Research interpretation

The hypothesized alpha mechanism is **order-flow self-excitation leading to short-horizon return predictability**: in cryptocurrency markets, a surge in aggressive buying (selling) events self-excites further aggressive buying (selling) due to herding, reflexivity, or latency-sensitive algorithmic responses. The Hawkes process captures this self-excitation, and the COE model translates predicted event intensities into a directional return forecast. This is a microstructure-level momentum/herding signal operating at the sub-second to multi-second timescale, distinct from longer-horizon price momentum. The economic channel assumes that cryptocurrency LOB participants (retail, market makers, HFT) react to observed order flow with predictable delays, creating transient directional pressure.

**Component roles:**
- Hawkes process: models self-exciting dynamics of LOB event arrivals (trades, limit orders)
- COE model: maps Hawkes-predicted future event intensities to return sign forecasts
- Non-uniform sampling: preserves inter-arrival time information lost in bar aggregation

## Signal

- **Formation timestamp:** Signal is formed at each LOB event arrival; the Hawkes intensity is updated in real time as new events arrive. The COE model outputs a return sign forecast (up/down) with a defined forecast horizon.
- **Lookback:** The Hawkes process uses an exponentially decaying kernel with a learned decay parameter; the lookback is effectively the kernel's characteristic timescale (not explicitly stated as a fixed window). The COE model uses a sliding window of recent Hawkes intensity predictions as input features.
- **Long entry:** Enter long when the COE model forecasts a positive return sign (price increase) with sufficient confidence. Exact confidence threshold is not specified in the abstract; the full paper details are required for the precise threshold.
- **Short entry:** Enter short when the COE model forecasts a negative return sign.
- **Exit:** Not explicitly specified in the abstract. The trading environment likely uses a fixed holding period or next-signal reversal; the full paper should be consulted for exact exit logic.
- **Holding period:** Short-horizon; the signal targets next-event or near-future return direction. Exact holding period requires the full paper.
- **Parameters:**
  - Hawkes kernel decay: learned from data (not specified as fixed)
  - COE model architecture: neural network with continuous output; exact architecture requires full paper
  - Forecast horizon: not specified in abstract
  - Confidence threshold for trade entry: not specified in abstract
  - **All thresholds and model architecture details are research-proposed and require full paper consultation for exact values.**

**Underspecified items:** The abstract does not provide exact entry/exit thresholds, holding period, COE model architecture details, Hawkes kernel parameters, or position-sizing logic. The signal is partially reproducible from the methodology description but requires the full paper for complete reconstruction.

## Required data

- **Instrument:** USDT/USD (Tether against US Dollar) on a centralized cryptocurrency exchange
- **Universe:** Single pair; no cross-asset universe specified
- **Venue:** Centralized cryptocurrency exchange (name not specified in abstract; full paper required)
- **Timeframe:** LOB event-level data (tick-level, not bar-aggregated); non-uniformly sampled
- **Fields:** Limit order book events — trade events (aggressor side, price, size) and limit order events (add, cancel, modify); inter-arrival times between events
- **Point-in-time:** Real-time LOB data; no look-ahead specified
- **Timestamp:** High-precision timestamps required for inter-arrival time computation; timezone depends on exchange
- **Missing-data:** Not explicitly addressed in abstract; LOB data completeness depends on exchange data feed quality
- **Funding/fee/spread needs:** Not explicitly specified in abstract; trading environment fees likely modeled but details require full paper

## Execution assumptions

- **Signal-to-order timing:** Signal formed at LOB event; order placement assumed to be near-real-time (latency-dependent)
- **Execution model:** Not explicitly specified in abstract. Likely market orders given the short-horizon directional nature.
- **Fill model:** Not specified; assumed instantaneous at LOB best price for modeling purposes
- **Fees:** Not specified in abstract; full paper required for fee treatment
- **Slippage/spread:** Not specified in abstract; LOB data inherently contains spread information
- **Latency:** Critical — the self-excitation signal decays rapidly; execution latency directly impacts alpha capture
- **Leverage/margin:** Not specified
- **Position sizing:** Not specified

## Evidence

### Source-reported

- The strategy surpasses benchmark models in both prediction accuracy (return sign classification) and cumulative profit in backtested trading environments.
- Validated through Monte Carlo simulations across 50 scenarios.
- Results are based on LOB data from a centralized cryptocurrency exchange (USDT/USD pair).
- Specific Sharpe ratios, win rates, or CAGR figures are not provided in the abstract; full paper required for quantitative claims.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan

1. **Out-of-sample test:** Run Hawkes+COE model on a different cryptocurrency pair (e.g., BTC/USDT) or different exchange to test cross-asset/cross-venue generalization. **Failure rule:** If out-of-sample return sign prediction accuracy drops below baseline (random walk or simple volume-weighted features), the self-excitation mechanism is not portable.
2. **Parameter perturbation:** Vary Hawkes kernel decay parameter and COE model architecture. **Failure rule:** If performance is sensitive to exact parameter choices (overfitting), the mechanism is fragile.
3. **Fee/stress test:** Apply realistic taker fees (0.04–0.10%), spread, and latency delays. **Failure rule:** If cumulative profit is erased under realistic costs, the signal does not survive transaction friction.
4. **Regime breakdown:** Test during high-volatility vs. low-volatility regimes separately. **Failure rule:** If the self-excitation signal only works in one regime, it is regime-dependent and not universally applicable.
5. **Capacity/liquidity:** Test with position size scaled up. **Failure rule:** If market impact at realistic position sizes eliminates profits, the strategy is capacity-constrained.
6. **Baseline comparison:** Compare against simple LOB features (e.g., order imbalance, trade flow toxicity/VPIN). **Failure rule:** If simple features achieve similar accuracy, the Hawkes self-excitation component adds no incremental value.

## Crypto portability

**adapted**

The paper is natively about cryptocurrency (USDT/USD on a centralized exchange), so the mechanism is directly demonstrated in crypto. However, portability to other crypto pairs and venues requires:
- **Spot vs. perpetual:** The paper uses spot USDT/USD; perpetual futures have funding rates, mark prices, and different microstructure dynamics that may alter self-excitation patterns.
- **24/7 session structure:** No session boundaries; self-excitation may be more continuous but also noisier.
- **Venue fragmentation:** Different exchanges have different LOB dynamics, participant mixes, and latency profiles; cross-venue generalization is untested.
- **Liquidity:** USDT/USD is highly liquid; smaller-cap pairs may have different self-excitation characteristics.
- **On-chain dependencies:** None; purely exchange LOB data.

## Limitations

- **Underspecified:** Entry/exit thresholds, holding period, COE model architecture, and Hawkes kernel parameters are not provided in the abstract; full paper required for exact reconstruction.
- **Not independently reproduced:** No third-party replication found.
- **Single pair:** Results are demonstrated only on USDT/USD; cross-asset generalization is untested.
- **Latency sensitivity:** The self-excitation signal likely decays within seconds; real-world execution latency may significantly degrade performance.
- **Publication bias:** The paper reports positive results; no discussion of failure cases or parameter sensitivity in the abstract.
- **Data quality:** LOB data quality varies by exchange; the specific exchange is not named in the abstract.
- **Model complexity:** Hawkes+COE is substantially more complex than simple LOB feature models; the incremental value over simpler approaches is not demonstrated in the abstract.

## Implementation status

No implementation in our research stack. The paper provides a theoretical framework and backtested results; no production code or live trading evidence is available.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[quant/hawkes-driven-otc-market-making-volterra-riccati-2026-09-01]] — Uses Hawkes processes for OTC market-making quote optimization (different mechanism: optimal control under self-excitation vs. return sign forecasting from self-excitation)
- [[quant/crypto-volume-synchronized-probability-of-toxicity-vpin-microstructure-2026-08-31]] — Related LOB microstructure signal (VPIN toxicity vs. Hawkes self-excitation)

## Sources

1. Raffaele Giuseppe Cestari, Filippo Barchi, Riccardo Busetto, Daniele Marazzina, Simone Formentin, "Hawkes-based cryptocurrency forecasting via Limit Order Book data", arXiv:2312.16190v1 [q-fin.ST, cs.CE, cs.LG], December 2023. https://arxiv.org/abs/2312.16190
