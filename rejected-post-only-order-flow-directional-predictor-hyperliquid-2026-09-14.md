---
schema: strategy-research-record-v1
title: "Rejected Post-Only Order Flow as Directional Predictor: Hyperliquid Level-4 Evidence"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-microstructure
  - order-book
  - crypto
  - hyperliquid
status: research-only
confidence: medium
source_as_of: 2026-02-16
sources:
  - "Jakob Albers, Mihai Cucuringu, Sam Howison, Alexander Y. Shestopaloff, 'The Price Impact of Nothing: Rejected Orders as Predictors of Future Returns', SSRN 6250378, February 16, 2026. https://ssrn.com/abstract=6250378"
  - "Jakob Albers, Mihai Cucuringu, Sam Howison, Alexander Y. Shestopaloff, 'The Neutrinos of the Order Book: Pervasive, Weakly Interacting Order Flow and its Consequences', SSRN 6250738, February 2026. https://ssrn.com/abstract=6250738"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Rejected Post-Only Order Flow as Directional Predictor: Hyperliquid Level-4 Evidence

## Provenance

- **Primary Source (predictive finding):** Jakob Albers (University of Oxford, Department of Statistics), Mihai Cucuringu (University of California, Los Angeles), Sam Howison (University of Oxford, Mathematical Institute), Alexander Y. Shestopaloff (Queen Mary University of London). *"The Price Impact of Nothing: Rejected Orders as Predictors of Future Returns"*, SSRN Electronic Journal, February 16, 2026. DOI: [10.2139/ssrn.6250378](https://doi.org/10.2139/ssrn.6250378). SSRN ID: 6250378. Stable URL: https://ssrn.com/abstract=6250378.
- **Primary Source (market-making mechanics):** Jakob Albers, Mihai Cucuringu, Sam Howison, Alexander Y. Shestopaloff. *"The Neutrinos of the Order Book: Pervasive, Weakly Interacting Order Flow and its Consequences"*, SSRN Electronic Journal, February 2026. SSRN ID: 6250738. Stable URL: https://ssrn.com/abstract=6250738. Presented at Oxford Mathematical Institute seminar, February 19, 2026.
- **Supporting Dataset:** *"An Open Book: Level 4 Order Book Data from the Hyperliquid Exchange"*, SSRN 6465720, 2026. Zenodo open-license release (~196 GB). Includes full order lifecycle events (submission, cancellation, fill, rejection) for BTC, ETH, and SOL perpetual contracts on Hyperliquid, December 2025.
- **Source/Data As-Of:** December 2025 (Hyperliquid blockchain data); paper published February 2026.
- **Pre-Write Deduplication Audit:** Repository-wide search confirmed zero matches for `6250378`, `6250738`, `Price Impact of Nothing`, `Neutrinos of the Order Book`, `Albers` (as author), `rejected.*order.*predictor`, or `queue.*priority.*rejected` in existing strategy-research records. The same authors' earlier paper *"The Market Maker's Dilemma"* (arXiv:2502.18625v2, November 2025) is captured in `contrarian-market-making-fill-probability-order-flow-2026-09-01.md`, but operates through a fundamentally different mechanism (fill probability vs. post-fill returns trade-off at the touch, not rejected-order predictive power). These are independent research captures under the dedup criteria.

## Economic mechanism

### Source-reported

Rejected post-only limit orders — orders submitted to the "wrong" (aggressive) side of the book that would cross the spread — are mechanically bounced by the matching engine and never enter the order book. They are invisible to all other market participants. The authors document that these rejected orders are significantly correlated with subsequent price movements. Standard price-impact regression models yield statistically significant and non-trivial coefficients for measures of rejected order flow. The authors interpret this as evidence that rejected and accepted orders alike are responses to a common information set: informed traders submit post-only orders aggressively as part of a queue-priority capture strategy (the "Neutrinos" mechanism described in the companion paper), and the directional intent embedded in these rejected submissions reveals private information about expected price moves (`source-reported`).

### Research interpretation

The hypothesized alpha channel is **informed order submission revealing directional intent through rejected post-only flow**. On Hyperliquid, where the full order lifecycle (including rejections) is publicly observable on-chain, a small cohort of traders bombards the exchange with post-only limit orders on the aggressive side. ~60-89% of all order-status events are such rejections. When the price moves in transit, the rare accepted submission captures top queue priority, securing the best position for subsequent fills. The pattern and direction of these rejected submissions constitutes a persistent, exploitable signal that reveals informed positioning before it becomes visible in standard order-book data. For a participant with access to Hyperliquid's on-chain rejection data (Level 4), the aggregate rejected flow direction is a leading indicator of short-term price movement.

Components:
- **Signal source:** Aggregate rejected post-only order flow direction (net aggressive-side rejections across wallets).
- **Mechanism:** Informed traders reveal directional intent through rejected submissions that are invisible on standard feeds but observable on-chain.
- **Market frictions exploited:** Queue-priority advantage; information asymmetry between participants with and without access to rejection data.

## Signal

- **Formation timestamp:** Continuous — rejected orders are timestamped to nanosecond precision on the Hyperliquid blockchain. Aggregate signal computed over a rolling window (specific window not stated in abstract; `data gap`).
- **Lookback:** Not specified in the abstract. The companion "Neutrinos" paper analyzes a one-month sample (December 2025) with ~4.5 billion messages total and ~880 million order-status events per day across BTC, ETH, and SOL.
- **Long entry:** When aggregate rejected post-only flow is predominantly on the buy side (aggressive buy rejections exceed aggressive sell rejections), indicating informed traders positioning for upward price movement. (`source-reported`: rejected orders correlate with subsequent price movements in the direction of the rejected flow; `research-proposed` specific entry threshold not specified by source.)
- **Short entry:** When aggregate rejected post-only flow is predominantly on the sell side. (`research-proposed`.)
- **Exit:** Not specified by the source (`data gap`). Research-proposed candidates: fixed holding period, or signal reversal (rejected flow direction flips).
- **Holding period:** Short-horizon (the paper studies short-term price movements at high frequency). Exact horizon not specified in abstract (`data gap`).
- **Parameters:** The specific regression specification, rolling window, net-flow threshold, and position-sizing rules are not available from the abstract alone (`data gap`; requires access to the full SSRN paper). The QuantSeeker secondary summary characterizes directional accuracy as ~72%, but this figure is not verified from the primary source's abstract.
- **Position-sizing:** Not specified (`data gap`).
- **Multi-timeframe dependencies:** Not specified (`data gap`).
- **Fully specified:** No — the signal is directionally specified but operational parameters (thresholds, windows, sizing) are underspecified from available sources.

## Required data

- **Instrument:** BTC-USDT, ETH-USDT, SOL-USDT perpetual futures on Hyperliquid (and potentially all 250+ Hyperliquid perpetual contracts).
- **Venue:** Hyperliquid decentralized perpetual futures exchange.
- **Market type:** Perpetual futures (on-chain).
- **Timeframe:** High-frequency (nanosecond-order-event resolution).
- **Fields required:**
  - Full order-status events including **rejections** (specifically `badAloPxRejected` — post-only orders that would cross the spread).
  - Order submission side (buy/sell), timestamp, wallet identity.
  - Accepted order submissions and cancellations (for context).
  - Trade execution data.
  - Top-of-book price data (for return calculation).
- **Point-in-time:** Rejection data is available in real-time on the Hyperliquid blockchain. No look-ahead concerns for on-chain data.
- **Timestamp:** Nanosecond precision, on-chain timestamped.
- **Missing-data assumptions:** Requires running a Hyperliquid non-validating node to capture rejection events (not available through standard market data APIs). The dataset is published on Zenodo (~196 GB for one month).
- **Funding/fee/spread needs:** Hyperliquid fee schedule: taker ~4.5 bps, maker rebate ~0.3 bps at top tier; order submissions and cancellations are gasless. Spread and slippage modeling required for execution simulation (`data gap` for specific cost assumptions in the paper).

## Execution assumptions

- **Signal-to-order timing:** Not specified (`data gap`). Research-proposed: signal computed from aggregate rejected flow, order placed immediately upon signal threshold breach.
- **Next-bar vs same-bar execution:** Not specified (`data gap`).
- **Market / limit order:** Not specified (`data gap`). Research-proposed: limit orders at or near mid to minimize taker fees.
- **Fill model:** Not specified (`data gap`).
- **Fees:** Hyperliquid: ~4.5 bps taker, ~0.3 bps maker (top tier); gasless submissions/cancellations (`source-reported` from dataset description, not from the strategy paper's cost model).
- **Spread:** Variable; Hyperliquid is one of the most liquid on-chain perpetual venues.
- **Slippage:** Not specified (`data gap`).
- **Impact / capacity:** Not specified (`data gap`). Capacity likely limited by the signal's short horizon and the specific asset set.
- **Funding:** Perpetual funding payments apply; not incorporated into the signal (`data gap`).
- **Leverage / margin:** Not specified (`data gap`).
- **Borrow / shorting:** Perpetual futures — no borrow required for shorting.
- **Latency:** Extremely low latency required to observe and aggregate rejection events in real-time; on-chain data has block-time granularity.
- **Partial fills / failures:** Not specified (`data gap`).

## Evidence

### Source-reported

- The abstract states that rejected post-only orders are "significantly correlated with subsequent price movements" and that "regression models of the type commonly used to measure price impact yield statistically significant and non-trivial coefficients for measures of rejected order flow" (`source-reported` from SSRN 6250378 abstract).
- The companion "Neutrinos" paper (SSRN 6250738) documents that ~60% of all message traffic on Hyperliquid (4.5 billion messages in a one-month sample) consists of rejected post-only orders, and that a small cohort of traders uses this mechanism to capture queue priority. The strategy is described as profitable by the authors (`source-reported` from Oxford seminar abstract).
- A secondary summary (QuantSeeker) characterizes rejected orders as correctly forecasting the direction of the next price change "about 72% of the time." This figure is **not verified from the primary source's abstract** and should be treated as `data gap` pending access to the full paper.
- The aligrithm.com analysis confirms that ~89% of the ~880 million daily order-status events across BTC/ETH/SOL are rejections, and that the rejected flow "predicts future returns" (`source-reported` from secondary analysis of the dataset).

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result.

Key caveats from the source: The authors explicitly note the result is "seemingly paradoxical" and emphasize that the correlation does not imply direct causation — rejected orders do not cause price changes but are responses to a common information set. The paper's framing highlights the need for careful causal interpretation, not a simple trading-strategy conclusion.

## Falsification plan

1. **Out-of-sample replication on Hyperliquid:** Apply the rejected-order-flow directional signal to a different time period (e.g., January-March 2026) on the same venue. Expected: rejected flow direction should maintain statistically significant correlation with subsequent returns (regression t-stat > 2). **Failure:** t-stat < 2 or sign flip → mechanism does not persist.
2. **Cross-venue transfer:** Test whether the same signal structure exists on other on-chain perpetual exchanges with transparent order rejection data (e.g., dYdX v4 if rejection data is accessible). Expected: weaker or absent signal if the queue-priority strategy is venue-specific to Hyperliquid's fee structure. **Failure:** no signal on other venues → Hyperliquid-specific, not generalizable.
3. **Cost sensitivity:** Simulate strategy returns under realistic Hyperliquid fee tiers (taker 4.5 bps, maker 0.3 bps) with realistic fill rates and slippage. **Failure:** net-of-cost Sharpe < 0.5 or negative net returns → signal is not tradable at retail/institutional fee tiers.
4. **Regime breakdown:** Test signal performance during high-volatility vs. low-volatility regimes, and during periods of elevated vs. depressed Hyperliquid trading activity. **Failure:** signal disappears in specific regimes → conditional, not universal.
5. **Capacity / decay test:** Monitor signal strength over time as more participants gain access to on-chain rejection data. **Failure:** signal decays to noise within months → competitive erosion eliminates edge.
6. **Placebo test:** Randomly shuffle rejection timestamps while preserving daily totals. Expected: shuffled signal should show no correlation with returns. **Failure:** shuffled signal also predicts → spurious correlation from confound (e.g., time-of-day effects).

## Crypto portability

**Direct** — the mechanism is inherently crypto-native:
- Rejection data is only publicly observable on on-chain exchanges (currently Hyperliquid). Centralized exchanges do not publish rejection data.
- The queue-priority capture strategy depends on Hyperliquid's gasless submission model and specific fee structure (maker rebate vs. taker cost). Different fee structures on other venues would alter the economics.
- 24/7 trading and continuous on-chain settlement make the signal continuously available.
- On-chain transparency is a prerequisite — this is not portable to venues without public order lifecycle data.

Portability risks:
- Venue-specific: The strategy exploits Hyperliquid's unique combination of gasless submissions, on-chain transparency, and maker-taker fee differential.
- Competitive erosion: As more participants observe rejection data, the queue-priority strategy may become crowded, reducing the signal's edge.
- Regulatory: On-chain order-flow transparency may face regulatory scrutiny as HFT on decentralized venues evolves.

## Limitations

- **Data access barrier:** Requires running a Hyperliquid non-validating node (~100 GB/day of raw blockchain data) or accessing the Zenodo dataset. Not available through standard market data APIs.
- **Full paper not reviewed:** The quantitative results (specific regression coefficients, R², t-stats, sample period details, and the ~72% directional accuracy figure) are not verified from the primary source's abstract. All performance claims should be treated as `data gap` pending access to the full SSRN paper.
- **Not independently reproduced.**
- **Causal interpretation caveat:** The authors explicitly warn against interpreting the correlation as direct price impact. The signal reflects common information, not causal order flow.
- **Venue-specific:** Currently only observable on Hyperliquid; portability to CFX or other on-chain venues is unproven.
- **Competitive landscape:** If the strategy is profitable, rational competitors will erode the edge. The paper does not address capacity or competitive dynamics.
- **Single-month sample for the "Neutrinos" companion paper:** The detailed mechanics analysis covers December 2025 only; robustness across longer periods is not established from available sources.
- **Funding, slippage, and execution costs** are not modeled in the available abstract-level description.

## Implementation status

`not-implemented`. No implementation in our research stack. The signal requires Hyperliquid on-chain data infrastructure that is not currently part of our data pipeline.

## Adoption boundary

This record represents **research-only** material. It does not mean:
- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

The finding is a statistical correlation between rejected order flow and subsequent returns, observed on a single venue (Hyperliquid) during a specific sample period. Replication, cost analysis, and capacity assessment are required before any implementation consideration.

## Related Wiki records

- `[[quant/contrarian-market-making-fill-probability-order-flow-2026-09-01]]` — Same authors' "Market Maker's Dilemma" paper (arXiv:2502.18625v2); examines fill probability vs. post-fill returns trade-off at the touch. Different mechanism: the Dilemma paper studies accepted maker orders at the best bid/ask, while this record studies rejected aggressive post-only orders that never reach the book. Complementary but independent findings from the same Hyperliquid dataset.

## Sources

1. Jakob Albers, Mihai Cucuringu, Sam Howison, Alexander Y. Shestopaloff. *"The Price Impact of Nothing: Rejected Orders as Predictors of Future Returns"*. SSRN Electronic Journal, February 16, 2026. DOI: [10.2139/ssrn.6250378](https://doi.org/10.2139/ssrn.6250378). SSRN: https://ssrn.com/abstract=6250378.
2. Jakob Albers, Mihai Cucuringu, Sam Howison, Alexander Y. Shestopaloff. *"The Neutrinos of the Order Book: Pervasive, Weakly Interacting Order Flow and its Consequences"*. SSRN Electronic Journal, February 2026. SSRN: https://ssrn.com/abstract=6250738.
3. Oxford Mathematical Institute seminar presentation: *"The Neutrinos of the Order Book: what do rejected orders tell us?"*, Prof. Sam Howison, February 19, 2026. https://maths.ox.ac.uk/node/79871.
4. *"An Open Book: Level 4 Order Book Data from the Hyperliquid Exchange"*. SSRN 6465720, 2026. Zenodo open-license dataset.
5. QuantSeeker weekly research recap (secondary source; **not** primary verification). Summarizes the paper's directional accuracy claim (~72%). https://www.quantseeker.com/p/weekly-research-recap-12f.
6. Aligrithm.com analysis of the Hyperliquid L4 dataset (secondary source). Confirms ~89% rejection rate and ~880M daily order-status events. https://aligrithm.com/an-open-l4-order-book-what-hyperliquid-data-unlocks/.
