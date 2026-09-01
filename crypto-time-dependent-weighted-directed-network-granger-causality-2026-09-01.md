---
schema: strategy-research-record-v1
title: Time-Dependent Weighted Directed Networks of Cryptocurrency Interaction from High-Frequency Returns
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - market-microstructure
  - network-centrality
  - granger-causality
  - lead-lag
  - high-frequency
  - information-spillover
status: research-only
confidence: high
source_as_of: 2026-06
sources:
  - https://arxiv.org/abs/2606.25466
  - https://doi.org/10.48550/arXiv.2606.25466
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Time-Dependent Weighted Directed Networks of Cryptocurrency Interaction from High-Frequency Returns

## Provenance

- **Primary Academic Source:** Shubhangam Shukla, Mahesh Peyyala, and Abhijit Chakraborty, "Time-dependent weighted directed networks of cryptocurrency interaction from high-frequency returns," *arXiv preprint arXiv:2606.25466v2* [q-fin.TR / physics.soc-ph], June/July 2026. DOI: [10.48550/arXiv.2606.25466](https://doi.org/10.48550/arXiv.2606.25466).
- **Core Methodology:** Time-varying directed and weighted network construction based on pairwise Granger causality tests with Benjamini-Hochberg (BH) False Discovery Rate (FDR) control for multiple hypothesis testing.
- **Dataset / Universe:** High-frequency 1-minute log-return time series of major cryptocurrencies across the 2020–2025 period.

## Economic mechanism

### Source-reported

Shukla, Peyyala, and Chakraborty (2026) investigate the dynamic organization and directional transmission of information across cryptocurrency markets at high temporal resolution. They find:
1. **Network Heterogeneity & Power-Law Influence:** Link weights and nodal strengths in the high-frequency return network exhibit extreme heterogeneity. A small, elite subset of cryptocurrencies exerts a disproportionately large directional influence over the broader market.
2. **Evolving Influence Hierarchy (ETH Dominance over BTC):** The directional hierarchy of information flow is dynamic rather than static. Across the 2020–2025 sample, Ethereum (ETH) consistently acts as the primary information transmitter (highest out-degree and nodal influence strength), while Bitcoin (BTC) displays a gradual relative decline in directional dominance.
3. **Temporal Instability:** The global ranking of influential assets shows continuous reconfiguration, confirming that cryptocurrency interaction networks are highly competitive and non-stationary.
4. **Fat-Tailed Fluctuations:** High-frequency normalized returns exhibit heavy-tailed distributions and intermittent clustering, which govern the burstiness of directional causality links.

### Research interpretation

This finding establishes an empirical foundation for a **Dynamic Directed Network Information-Spillover Alpha**:
1. **Directional Hub-and-Spoke Lead-Lag:** Rather than assuming symmetric correlation or a static BTC-led market, high-frequency price discovery originates in dynamically identified "transmitter hubs" (high out-strength in the Granger causal graph). Information diffuses with a brief latency (1 to 15 minutes) to "receiver nodes" (high in-strength, low out-strength).
2. **Dynamic Centrality Overlay:** Tokens that exhibit statistically significant incoming Granger causal links from current market hubs will systematically lag the price innovations of the hub. By monitoring rolling 1-minute Granger causal graphs with FDR thresholding, quantitative strategies can position in lagging receiver tokens ahead of complete price equilibration.

## Signal

The normalized signal framework constructs a dynamic directed graph to generate high-frequency cross-asset directional bets:

1. **High-Frequency Return Formulation:**
   - Sample 1-minute closing prices $P_{i,t}$ across universe $i \in \{1, \dots, N\}$.
   - Calculate 1-minute log-returns:
     $$r_{i,t} = \ln\left(rac{P_{i,t}}{P_{i,t-1}}ight)$$

2. **Rolling Pairwise Granger Causality with FDR Correction:**
   - Over rolling window $W$ (e.g., $W = 1440$ minutes / 1 day or $W = 10,080$ minutes / 7 days):
   - For every directed pair $(i, j)$ where $i 
eq j$, fit a vector autoregressive model of lag order $p$ (e.g., $p \in \{1, 3, 5\}$ minutes):
     $$r_{j,t} = lpha_j + \sum_{k=1}^p eta_{jk} r_{j,t-k} + \sum_{k=1}^p \gamma_{ijk} r_{i,t-k} + \epsilon_{j,t}$$
   - Test null hypothesis $H_0: \gamma_{ij1} = \dots = \gamma_{ijp} = 0$ via F-test, obtaining p-value $p_{ij}$.
   - Apply Benjamini-Hochberg (BH) procedure at significance level $lpha = 0.05$ across all $N(N-1)$ pairs to determine the set of active directed edges $E_t$.
   - Assign edge weight $w_{ij,t} = F_{ij,t}$ for rejected nulls, and $0$ otherwise.

3. **Nodal Influence Metrics:**
   - Compute Out-Strength ($S_{	ext{out},i,t}$) and In-Strength ($S_{	ext{in},i,t}$):
     $$S_{	ext{out},i,t} = \sum_{j 
eq i} w_{ij,t}, \quad S_{	ext{in},i,t} = \sum_{j 
eq i} w_{ji,t}$$
   - Compute Net Influence Centrality:
     $$\Delta S_{i,t} = S_{	ext{out},i,t} - S_{	ext{in},i,t}$$

4. **Trading Rule (Lagged Information Capture):**
   - Identify top transmitter tokens (e.g., ETH, highest $S_{	ext{out}}$) and identify receiver tokens $j$ that have significant incoming edges from transmitter $i$ ($w_{ij,t} > 0$).
   - When transmitter $i$ experiences a cumulative 5-minute return shock exceeding threshold $	heta_{	ext{shock}}$ ($|R_{i,[t-5,t]}| > 1.5 \sigma_i$):
     - If receiver $j$ has not yet moved proportionally ($|R_{j,[t-5,t]}| < 0.5 eta_{ij} R_{i,[t-5,t]}$):
     - Enter directional trade on receiver $j$ matching the sign of transmitter $i$'s shock: $	ext{Position}_j = 	ext{sign}(R_{i,[t-5,t]})$.
   - Holding period: 5 to 15 minutes, or until the price gap $\epsilon_{j,t} = R_{j} - eta_{ij} R_i$ closes.

## Required data

- **Universe:** 20 to 50 liquid cryptocurrencies traded on major centralized exchanges (Binance, OKX, Bybit).
- **Timeframe:** 1-minute OHLCV candle data and tick/trade feeds.
- **Fields:** Timestamp, Open, High, Low, Close, Volume.
- **Latency / Timestamps:** Synchronized exchange millisecond timestamps to prevent artificial lead-lag measurement error.

## Execution assumptions

- **Holding Period:** 5 to 15 minutes.
- **Execution Timing:** Immediate taker execution or tight passive limit order inside top-2 book levels upon transmitter trigger event.
- **Frictions:** High-frequency turnover demands ultra-low fee tiers (VIP taker $\le 2	ext{ bps}$ or maker rebates).
- **Slippage:** Estimated at 1 to 3 bps for liquid receivers; unviable for illiquid long-tail tokens where spread exceeds the 5-minute lead-lag alpha window.

## Evidence

### Source-reported

All empirical results below are directly reported by Shukla, Peyyala, and Chakraborty (arXiv:2606.25466v2, 2026) using 1-minute data from 2020 to 2025:
1. **Network Connectivity & Causality:** Statistically significant Granger causal connections exist across major cryptocurrency pairs after rigorous Benjamini-Hochberg False Discovery Rate multiple-testing correction.
2. **Ethereum Lead Dominance:** ETH exhibits the highest sustained out-degree and weighted out-strength across the network over the 2020–2025 period, functioning as the primary price discovery anchor.
3. **Bitcoin Relative Decay:** While BTC remains central in raw capitalization, its net directional information spillover centrality ($\Delta S_{	ext{BTC}}$) shows a measurable downward trend relative to ETH and ecosystem leaders over the multi-year sample.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- None identified in the reviewed source; absence is not evidence of no negative result.
- General microstructure literature indicates that lead-lag arbitrage in centralized crypto exchanges suffers rapid decay due to low-latency colocation HFTs, which can compress informational lag windows below 1 second.

## Falsification plan

1. **Ablation vs Static Lead-Lag Matrix:** Compare the out-of-sample PnL of the dynamic Granger network model against a static correlation lead-lag benchmark. If dynamic network re-estimation does not improve predictive accuracy, the time-varying network model is falsified.
2. **Latency Sensitivity Test:** Simulate execution delays of 100ms, 1s, 5s, 30s, and 60s. If net Sharpe ratio drops below zero at realistic latency ($\ge 1	ext{s}$), the alpha is unviable as an off-exchange strategy.
3. **Fee Hurdle:** If gross returns fail to cover a 4 bps round-trip fee hurdle at the 15-minute horizon, reject deployment.

## Crypto portability

- **Direct:** The underlying empirical model is built specifically on high-frequency cryptocurrency exchange return data (2020–2025).
- **Crypto-specific factors:** 24/7 continuous trading avoids overnight jumps, but cross-exchange latency fragmentation (e.g. Binance vs OKX vs Bybit) introduces spatial noise into global lead-lag graphs.

## Limitations

- **Latency Decay:** 1-minute granularity may capture only residual low-frequency lead-lag; the fastest arbitrageurs operate at millisecond/sub-second scales.
- **Multiple Testing:** Pairwise testing over $N$ assets scales as $O(N^2)$, requiring stringent FDR corrections that may introduce false negatives.
- **Regime Shifts:** High-volatility news events cause brief structural breaks that temporarily violate VAR stationarity assumptions.

## Implementation status

No implementation in our research stack has been completed. Not implemented in PyBroker or NautilusTrader.

## Adoption boundary

Research material only. A record being present in this repository does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

## Related Wiki records

- `crypto-cross-cryptocurrency-lead-lag-adaptive-lasso-10m-2026-09-01.md`
- `crypto-community-network-intercrypto-momentum-spillover-daily-2026-08-31.md`
- `crypto-perpetual-spot-cross-venue-lead-lag-vecm-2026-09-01.md`

## Sources

1. Shubhangam Shukla, Mahesh Peyyala, and Abhijit Chakraborty, "Time-dependent weighted directed networks of cryptocurrency interaction from high-frequency returns," *arXiv preprint arXiv:2606.25466v2* [q-fin.TR / physics.soc-ph], June/July 2026.
   - URL: https://arxiv.org/abs/2606.25466
   - DOI: https://doi.org/10.48550/arXiv.2606.25466
