---
schema: strategy-research-record-v1
title: Bitcoin On-Chain Puell Multiple Miner Capitulation and Cycle Timing
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - on-chain
  - bitcoin
  - puell-multiple
  - miner-economics
  - capitulation
  - macro-cycle
status: research-only
confidence: medium
source_as_of: 2024-10
sources:
  - https://lookintobitcoin.com/charts/puell-multiple/
  - https://academy.glassnode.com/market/puell-multiple
  - https://doi.org/10.1016/j.irfa.2021.101861
  - https://medium.com/@msantoriESQ/the-puell-multiple-a-new-bitcoin-metric-94f4c2c54432
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin On-Chain Puell Multiple Miner Capitulation and Cycle Timing

## Provenance

- **Original Conceptual Creator:** David Puell (March 2019), introducing the Puell Multiple to explore Bitcoin market cycles from the perspective of mining revenue and supply-side selling pressure.
- **Primary Methodological Reference:** LookIntoBitcoin, "The Puell Multiple Historical Chart and Methodology" (2019–2024). [https://lookintobitcoin.com/charts/puell-multiple/](https://lookintobitcoin.com/charts/puell-multiple/).
- **Standardized Industry Reference:** Glassnode Academy, "The Puell Multiple Documentation" (2019–2024). [https://academy.glassnode.com/market/puell-multiple](https://academy.glassnode.com/market/puell-multiple).
- **Academic Peer-Reviewed Literature:** Daniel Felix Ahelegbey, Paolo Giudici, and Simone Ingrassia, “Cryptocurrency valuation and on-chain metrics,” *International Review of Financial Analysis*, Volume 78, Article 101861 (2021). DOI: [10.1016/j.irfa.2021.101861](https://doi.org/10.1016/j.irfa.2021.101861).

## Economic mechanism

### Source-reported

David Puell (2019) conceptualized the metric around the structural role of proof-of-work miners as "compulsory sellers." Because miners incur substantial fiat-denominated operating expenditures—primarily electricity costs, hardware depreciation, facility maintenance, and hosting fees—they must regularly liquidate a significant portion of their freshly minted Bitcoin to cover cash liabilities.

1. **Miner Capitulation & Market Bottoms (Puell Multiple < 0.5):** When daily miner revenues drop drastically below their 365-day moving average, miner profitability collapses. High-cost, inefficient mining operations are forced into insolvency and must power down their rigs (triggering hashrate drops). Once distressed miners liquidate their remaining inventory and shut down, compulsory supply selling pressure from the mining cohort becomes exhausted, historically marking multi-year macro cycle accumulation bottoms.
2. **Miner Windfall & Market Tops (Puell Multiple > 2.0 to 4.0):** When daily miner revenues surge to multiples of their yearly average during parabolic bull markets, mining profitability becomes extraordinarily high. This incentivizes miners to aggressively harvest profits and expand treasury liquidation into market strength, adding heavy structural overhead supply that historically coincides with macro cycle distribution tops.

### Research interpretation

The falsifiable quantitative thesis is that **miner cash-flow distress and structural selling flow act as an equilibrium anchor for Bitcoin cycle regimes**:

1. **Supply-Side Flow Equilibrium:** Daily block reward issuance represents a continuous flow of newly minted coins entering the market. While circulating float is large, newly issued coins represent un-hedged, immediate fiat-seeking sell volume.
2. **Cost-of-Production Floor:** When market price approaches or breaches the aggregate marginal cost of production, daily revenue drops below the 365-day baseline. The subsequent shutdown of unprofitable rigs reduces total network difficulty and hash cost, resetting the miner cohort to efficient low-cost operators and removing distressed liquidation pressure.
3. **Macro Rebalancing Signal:** Tracking the ratio of instantaneous daily issuance value to the 365-day moving average isolates periods of extreme supply distress (undervaluation) and extreme supply surplus (overvaluation), providing an asymmetric signal for counter-cyclical exposure scaling.

## Signal

The normalized trading rule defines macro regime boundaries and position scaling:

1. **On-Chain Daily Issuance Ingestion:**
   For each daily close timestamp $t$ (00:00:00 UTC):
   - $P_t$: Bitcoin daily close price in USD.
   - $\text{Issuance}_{t}$: Total newly minted Bitcoins (block subsidies) generated on day $t$.
   - $\text{FeesUSD}_{t}$: Total USD value of on-chain transaction fees on day $t$ (optional in standard formulation, included in total miner revenue variant).
   - $\text{Rev}_{\text{USD}, t} = \text{Issuance}_{t} \times P_t$ (baseline issuance value).

2. **Puell Multiple Formulation:**
   $$\text{SMA}_{365}(\text{Rev}_{\text{USD}})_t = \frac{1}{365} \sum_{d=0}^{364} \text{Rev}_{\text{USD}, t-d}$$
   $$\text{Puell Multiple}_t = \frac{\text{Rev}_{\text{USD}, t}}{\text{SMA}_{365}(\text{Rev}_{\text{USD}})_t}$$

3. **Macro Regime Allocation Rules:**
   - **Capitulation / Maximum Accumulation Regime:**
     $$\text{If } \text{Puell Multiple}_t \le 0.50:$$
     Scale long exposure to maximum allocation (e.g., 100%–150% spot/perp long) or trigger dollar-cost accumulation.
   - **Overheated / Euphoric Take-Profit Regime:**
     $$\text{If } \text{Puell Multiple}_t \ge 2.00 \quad (\text{or severe top threshold } \ge 3.00):$$
     Scale spot exposure down to defensive allocation (e.g., 0%–25%) or initiate a systematic linear short hedge.
   - **Neutral / Trend-Holding Regime:**
     $$\text{If } 0.50 < \text{Puell Multiple}_t < 2.00:$$
     Maintain benchmark neutral exposure (e.g., 50%–100%).

4. **Underspecified Nuances:**
   Original sources provide chart overlays and historical threshold bands (0.5 and 2.0/3.0) rather than a complete production execution algorithm. Dynamic trade sizing curves, halving step-down adjustments, and explicit stop-loss rules are not specified by the original author and represent active research parameters.

## Required data

- **Asset:** Bitcoin (BTC).
- **Frequency:** Daily block ledger aggregations at 00:00:00 UTC.
- **Fields:**
  - BTC Daily Close Price ($P_t$).
  - Daily BTC block reward issuance ($\text{Issuance}_t$).
  - Daily transaction fee revenue ($\text{Fees}_t$).
- **Point-in-Time Requirement:** Full on-chain block finality across day $t$ (UTC) prior to signal generation for day $t+1$.
- **Availability:** Readily available from full Bitcoin core nodes, Glassnode, Coin Metrics, or CryptoQuant APIs.

## Execution assumptions

- **Execution Cadence:** Daily rebalance at 00:00:00 UTC or weekly macro regime alignment.
- **Instrument:** BTC spot for long accumulation; BTC linear perpetual futures for hedging/underweighting.
- **Order Model:** Passive TWAP limit order execution over a 1-hour window following the daily close.
- **Turnover & Costs:** Extremely low annual turnover (holding periods span months to years), incurring minimal transaction fee friction (< 15 bps annualized).

## Evidence

### Source-reported

- David Puell (2019), LookIntoBitcoin, and Glassnode historical analytics document that the Puell Multiple successfully tagged every major macro Bitcoin cycle bottom:
  - 2011 bear market bottom (~0.20);
  - 2015 bear market bottom (~0.33);
  - December 2018 capitulation bottom (~0.28);
  - March 2020 liquidity shock (~0.35);
  - November–December 2022 FTX collapse bottom (~0.35).
- Historical macro tops in 2011, 2013, and December 2017 were characterized by Puell Multiple readings surging above 3.0–4.0.
- Ahelegbey, Giudici, and Ingrassia (2021) confirm via VAR and network connectedness models that miner revenue and coin creation metrics exhibit statistically significant predictive relationships with Bitcoin market capitalization.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Halving Step-Down Distortion:** Because Bitcoin's block subsidy is cut by 50% every 210,000 blocks (~4 years), daily issuance mechanically drops by half overnight. This creates an immediate downward step in the numerator, while the 365-day denominator takes a full year to adjust, artificially depressing the Puell Multiple following halving events regardless of miner health.
- **Declining Miner Issuance Dominance:** As the circulating supply grows past 19.7 million BTC and secondary exchange volume expands to tens of billions of dollars per day, daily newly minted Bitcoin (e.g., 450 BTC/day post-2024 halving) represents an increasingly small percentage (< 0.1%) of total market turnover, potentially weakening the direct price impact of miner structural selling.
- **Fee Spikes Distorting Issuance Logic:** Transitory transaction fee spikes (e.g., Ordinals, Runes, high network congestion) can sharply elevate total miner revenue for short windows without reflecting genuine sustained macro cycle expansions.

## Falsification plan

The Puell Multiple macro hypothesis should be rejected or revised if:
1. Backtesting on 2018–2026 data shows that a regime-switching strategy based on the 0.5/2.0 thresholds fails to achieve higher risk-adjusted return (Sharpe/Sortino) or lower maximum drawdown than a passive buy-and-hold BTC benchmark.
2. Halving-adjusted variations of the metric (normalizing for the programmed step-down) fail to outperform unadjusted metrics, proving the signal is dominated by arbitrary denominator lag.
3. In modern market regimes (post-2024 halving), price drops below estimated production cost without triggering miner capitulation or subsequent price recovery, demonstrating that institutional ETF flows and derivatives dominate price discovery over miner flows.
4. Replacing on-chain miner revenue with a simple 200-day or 365-day price moving average generates identical or superior timing accuracy without on-chain data.

## Crypto portability

- **Direct** for Proof-of-Work (PoW) cryptocurrencies with observable block issuance and fixed emission schedules (e.g., Bitcoin, Litecoin, Dogecoin, Bitcoin Cash).
- **Not applicable** for Proof-of-Stake (PoS) networks (e.g., Ethereum post-Merge, Solana) where staking yield and validator dynamics differ fundamentally from capital-intensive PoW mining operations.
- **Crypto-Specific Considerations:** Metric is entirely native to decentralized PoW blockchains; traditional assets do not feature algorithmically enforced, transparent issuance schedules.

## Limitations

- **Not independently reproduced.**
- **Low Signal Frequency:** Macro indicator producing only a few actionable cycle entry/exit regimes per 4-year halving cycle.
- **Halving Artifact:** Mechanically distorted for 6–12 months following each quadrennial halving event.
- **Structural Diminution:** Diminishing economic weight of newly minted supply relative to aggregate secondary market liquidity.

## Implementation status

Not implemented in the research stack. No PyBroker, NautilusTrader, Paper, Testnet, or Live validation has been performed.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. Presence in the Alpha Strategy Pool does not imply profitable alpha, validated predictability, implementation approval, paper-trading approval, testnet approval, or live-trading approval.

## Related Wiki records

- `bitcoin-hash-ribbon-miner-capitulation-2026-08-31.md` — hash rate moving average miner capitulation indicator.
- `bitcoin-onchain-mvrv-zscore-cycle-reversal-2026-08-31.md` — on-chain market value to realized value macro cycle reversal.
- `bitcoin-onchain-nvt-signal-macro-cycle-2026-08-31.md` — on-chain network value to transactions signal.
- `bitcoin-onchain-rhodl-ratio-macro-cycle-2026-08-31.md` — on-chain realized HODL ratio macro cycle metric.
- `bitcoin-onchain-sopr-spent-output-profit-ratio-2026-08-31.md` — spent output profit ratio market sentiment indicator.

## Sources

1. LookIntoBitcoin, “The Puell Multiple Historical Chart and Indicator Methodology,” (2019–2024). URL: https://lookintobitcoin.com/charts/puell-multiple/
2. Glassnode Academy, “Puell Multiple Documentation and Technical Specification,” Glassnode Insights (2019–2024). URL: https://academy.glassnode.com/market/puell-multiple
3. Daniel Felix Ahelegbey, Paolo Giudici, and Simone Ingrassia, “Cryptocurrency valuation and on-chain metrics,” *International Review of Financial Analysis*, Volume 78, Article 101861 (2021). DOI: https://doi.org/10.1016/j.irfa.2021.101861
4. David Puell, “The Puell Multiple: A New Bitcoin Metric,” Cryptolab / Medium Research (March 2019). URL: https://medium.com/@msantoriESQ/the-puell-multiple-a-new-bitcoin-metric-94f4c2c54432
