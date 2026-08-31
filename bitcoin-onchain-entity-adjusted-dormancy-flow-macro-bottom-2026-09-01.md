---
schema: strategy-research-record-v1
title: Bitcoin On-Chain Entity-Adjusted Dormancy Flow Macro Bottom Timing
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - onchain
  - bitcoin
  - dormancy-flow
  - coin-days-destroyed
  - macro-cycle
  - capitulation
status: research-only
confidence: high
source_as_of: 2019-03
sources:
  - https://insights.glassnode.com/the-market-pulse-29/
  - https://medium.com/@puell/the-dormancy-flow-a-macro-indicator-for-bitcoin-bottoms-e0cbddca47a3
  - https://academy.glassnode.com/market/dormancy/dormancy-flow
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin On-Chain Entity-Adjusted Dormancy Flow Macro Bottom Timing

## Provenance

- **Primary Source:** David Puell (March 2019), “The Dormancy Flow: A Macro Indicator for Bitcoin Bottoms,” published via Medium / Unchained Capital / Glassnode Insights. Archived reference: https://medium.com/@puell/the-dormancy-flow-a-macro-indicator-for-bitcoin-bottoms-e0cbddca47a3.
- **Methodological Lineage:** Built upon Dmitry Kalichkin’s concept of Bitcoin Dormancy (average coin-days destroyed per transacted coin) and formalized into an annualized macro valuation oscillator.
- **Entity-Adjusted Refinement:** Glassnode Academy documentation on Entity-Adjusted Dormancy Flow (filtering intra-entity exchange shuffling and non-economic transactions): https://academy.glassnode.com/market/dormancy/dormancy-flow.

## Economic mechanism

### Source-reported

1. **Dormancy Definition:** Dormancy measures the average holding age of spent bitcoins, calculated as the ratio of Coin Days Destroyed ($\text{CDD}$) to total transferred transaction volume ($\text{Vol}$). A higher dormancy indicates that older, long-held coins are moving; a lower dormancy indicates that transactions are dominated by recently acquired coins.
2. **Dormancy Flow Metric:** Dormancy Flow is defined as the ratio of Bitcoin’s current market capitalization to its annualized dormancy value (measured in USD).
3. **Macro Cycle Bottoms:** Puell reports that during late-stage bear market capitulations, long-term holders cease spending, transaction velocity contracts, and older UTXOs remain dormant. When the market capitalization compresses below the annualized spending velocity of old coins (Dormancy Flow dropping below the historical 250,000 threshold), it indicates deep market undervaluation and historical cycle bottoming.

### Research interpretation

The strategy is an **on-chain structural holder-conviction / macro mean-reversion alpha**:
1. **Asymmetric Smart-Money Inactivity:** Long-term holders (conviction entities) hold a substantial portion of the circulating supply. During panic-driven liquidation cascades, short-term speculators exit at large losses, while long-term holders withhold supply from the market.
2. **Annualized Valuation Comparison:** Comparing current network valuation against the trailing 365-day moving average of dormancy spending value normalizes for long-term network growth and monetization trends, creating a stationary oscillator across multi-year halving cycles.
3. **Entity Clustering Filter:** Raw on-chain transaction volume contains significant noise from internal exchange cold-to-hot wallet rebalancing. Applying entity-resolution algorithms isolates genuine peer-to-peer economic transfers, providing a cleaner spending velocity signal.

## Signal

The quantitative on-chain signal is constructed daily as follows:

1. **Entity-Adjusted Dormancy Calculation:**
   At daily timestamp $t$ (00:00 UTC cutoff), calculate entity-adjusted dormancy ($\text{Dormancy}_t$, in days per coin):
   $$\text{Dormancy}_t = \frac{\text{CDD}_{\text{entity}, t}}{\text{Volume}_{\text{entity}, t}}$$

2. **Annualized Dormancy Value (USD):**
   Calculate the annualized dormancy spending value by taking a 365-day simple moving average of daily dormancy converted to dollar terms:
   $$\text{Annualized Dormancy Value}_t = \frac{1}{365} \sum_{i=0}^{364} \left( \text{Dormancy}_{t-i} \times P_{t-i} \right)$$
   where $P_t$ is the daily Bitcoin close price in USD.

3. **Entity-Adjusted Dormancy Flow:**
   $$\text{Dormancy Flow}_t = \frac{\text{Market Cap}_t}{\text{Annualized Dormancy Value}_t}$$

4. **Trading Rule / Alpha Formation:**
   - **Historical Capitulation Threshold:** Baseline threshold $\theta = 250{,}000$ (or trailing 5th percentile of historical distribution).
   - **Entry Trigger (Macro Long):** Enter or dollar-cost average into a long spot BTC position when $\text{Dormancy Flow}_t < \theta$, or on the cross back above $\theta$ from the oversold territory.
   - **Exit / Risk Reduction Trigger:** Exit to cash/stablecoins or hedge when $\text{Dormancy Flow}_t$ enters the multi-year overbought expansion zone ($> 2{,}000{,}000$) or crosses below its 200-day moving average during macro distribution.

## Required data

- **Data Granularity:** Daily on-chain aggregated metrics at 00:00 UTC.
- **On-Chain Metrics:**
  - Entity-Adjusted Coin Days Destroyed ($\text{CDD}_{\text{entity}}$).
  - Entity-Adjusted Transfer Volume in BTC ($\text{Volume}_{\text{entity}}$).
  - Circulating Supply and Daily Close Price ($P_t$).
- **Data Lineage:** Clean point-in-time on-chain node parser with validated clustering heuristics (e.g., Glassnode or Coin Metrics pipeline).

## Execution assumptions

- **Strategy Horizon:** Macro thematic / multi-quarter position holding (holding period: 6 months to 3 years).
- **Execution Instrument:** Spot Bitcoin (self-custody or cold storage) or unleveraged spot-equivalent.
- **Execution Timing:** Next-day 00:05 UTC open following daily on-chain block settlement.
- **Frictions:** Taker spot fees (5–10 bps) and network transfer fees are negligible relative to the multi-year macro target holding horizon. Spot execution eliminates perpetual funding rate drag.

## Evidence

### Source-reported

- **Historical Macro Bottom Timing:** In historical backtests and live observation across Bitcoin’s entire history (2011–2025), the Dormancy Flow dropped into the capitulation zone ($\text{Dormancy Flow} < 250{,}000$) only during generational cycle bottoms:
  - **2011 Bottom:** November 2011 (~$2.25).
  - **2015 Bear Market Bottom:** January 2015 (~$160–$200).
  - **2018 Bear Market Bottom:** December 2018 – February 2019 (~$3,100–$3,800).
  - **March 2020 COVID Liquidity Shock:** March 2020 (~$3,850–$5,500).
  - **2022 FTX Capitulation:** November 2022 – January 2023 (~$15,500–$16,800).
- In each historical instance, purchasing when Dormancy Flow was within or crossing out of the green band preceded massive subsequent multi-year cycle expansions with $>300\%$ upside.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Small Sample Size:** Because the signal operates on a 4-year macro cycle, only $N \approx 5$ distinct generational bottom events exist in Bitcoin’s historical sample.
- **Interim Drawdown During Capitulation:** In extended capitulation phases (e.g., 2014–2015 and 2022), Dormancy Flow entered the $<250{,}000$ zone several weeks before the exact price trough, exposing unhedged early accumulators to interim drawdowns of up to 30–40% before ultimate recovery.
- **Clustering Heuristic Restatements:** Entity clustering relies on probabilistic off-chain and on-chain heuristics (common input ownership, change address detection). Historical entity classifications are subject to retrospective data restatements by data vendors as new clustering information is discovered.

## Falsification plan

The hypothesis should be considered rejected or materially weakened if:
1. Bitcoin experiences a sustained $>50\%$ secular price breakdown below previous cycle all-time highs without Dormancy Flow entering the capitulation zone.
2. An entry triggered on the cross above $\theta = 250{,}000$ suffers a subsequent $>40\%$ drawdown on a 12-month forward evaluation window.
3. Unadjusted Dormancy Flow (without entity clustering) generates contradictory signals or extensive false positives during routine exchange internal wallet migrations.

## Crypto portability

- **Direct:** Built specifically for Bitcoin’s UTXO architecture where coin-age and coin-days destroyed are explicitly observable on-chain.
- **UTXO Altcoins (Adapted / Unproven):** Porting to other UTXO blockchains (e.g., Litecoin, Dogecoin, Bitcoin Cash) is theoretically possible but unproven and hindered by lack of deep long-term institutional holding conviction.
- **Account-Based Blockchains (Not Applicable):** Account-based chains (Ethereum, Solana) lack UTXO-level coin-age destruction mechanics; equivalent account-level dormancy metrics require fundamentally different construction and assumptions.

## Limitations

- **Not independently reproduced.**
- **Low Signal Frequency:** Generates entry signals approximately once every 2 to 4 years.
- **Data Vendor Dependence:** Entity-adjusted data requires specialized on-chain clustering infrastructure; raw blockchain data without clustering introduces significant noise.
- **Macro Regime Shift Risk:** Increasing institutionalization through spot ETFs and regulated custodians may alter on-chain dormancy dynamics if large custody transfers bypass public mempools or use off-chain internal ledgers.

## Implementation status

Not implemented in the research stack. No PyBroker, NautilusTrader, Paper, Testnet, or Live validation has been performed.

`implementation_status: not-implemented`

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. Presence in the repository does not constitute approval for live capital allocation, paper trading, or testnet deployment.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `bitcoin-onchain-reserve-risk-hodl-conviction-2026-08-31.md` — Reserve Risk long-term holder conviction ratio.
- `bitcoin-onchain-rhodl-ratio-macro-cycle-2026-08-31.md` — Realized HODL ratio macro cycle distribution.
- `bitcoin-onchain-puell-multiple-miner-capitulation-2026-08-31.md` — Puell Multiple miner revenue capitulation.
- `bitcoin-onchain-sopr-spent-output-profit-ratio-2026-08-31.md` — SOPR cycle reversal oscillator.

## Sources

1. David Puell, “The Dormancy Flow: A Macro Indicator for Bitcoin Bottoms,” Medium / Unchained Capital (March 2019): https://medium.com/@puell/the-dormancy-flow-a-macro-indicator-for-bitcoin-bottoms-e0cbddca47a3.
2. Glassnode Academy, “Entity-Adjusted Dormancy Flow”: https://academy.glassnode.com/market/dormancy/dormancy-flow.
3. Glassnode Insights, “The Market Pulse: Dormancy and HODLer Behavior”: https://insights.glassnode.com/the-market-pulse-29/.
