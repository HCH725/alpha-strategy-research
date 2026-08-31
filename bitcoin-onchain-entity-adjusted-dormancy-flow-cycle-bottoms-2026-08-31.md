---
schema: strategy-research-record-v1
title: Bitcoin On-Chain Entity-Adjusted Dormancy Flow Macro Cycle Bottom Timing
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
  - dormancy-flow
  - coin-days-destroyed
  - macro-cycle
  - capitulation
  - long-term-holders
status: research-only
confidence: medium
source_as_of: 2024-10
sources:
  - https://lookintobitcoin.com/charts/dormancy-flow/
  - https://academy.glassnode.com/market/dormancy-flow
  - https://medium.com/@msantoriESQ/dormancy-flow-a-new-bitcoin-metric-773a985f4017
  - https://doi.org/10.1016/j.irfa.2021.101861
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin On-Chain Entity-Adjusted Dormancy Flow Macro Cycle Bottom Timing

## Provenance

- **Original Conceptual Creator:** David Puell (March 2019), introducing Dormancy Flow as a macro market cycle oscillator based on UTXO lifespan dynamics and coin dormancy.
- **Underlying Metric Antecedent:** Reginald Smith (2018), “Bitcoin Dormancy,” establishing the formalization of average coin dormancy using Coin Days Destroyed (CDD) divided by transaction volume.
- **Industry Reference Implementation:** Glassnode Studio & Academy, “Entity-Adjusted Dormancy Flow Documentation” (2019–2024). [https://academy.glassnode.com/market/dormancy-flow](https://academy.glassnode.com/market/dormancy-flow).
- **Macro Cycle Charting Reference:** LookIntoBitcoin, “Dormancy Flow Live Chart and Historical Cycle Methodology” (2019–2024). [https://lookintobitcoin.com/charts/dormancy-flow/](https://lookintobitcoin.com/charts/dormancy-flow/).
- **Academic Context:** Daniel Felix Ahelegbey, Paolo Giudici, and Simone Ingrassia, “Cryptocurrency valuation and on-chain metrics,” *International Review of Financial Analysis*, Volume 78, Article 101861 (2021). DOI: [10.1016/j.irfa.2021.101861](https://doi.org/10.1016/j.irfa.2021.101861).

## Economic mechanism

### Source-reported

David Puell (2019) conceptualized Dormancy Flow to quantify the spending behavior of long-term Bitcoin holders relative to aggregate network market capitalization.

1. **Coin Days Destroyed (CDD) & Average Dormancy:** When a transaction spends a UTXO that has remained dormant for $D$ days, it "destroys" $D \times \text{Amount}$ coin days. Average Dormancy ($\text{CDD} / \text{Volume}$) measures the average holding duration of coins moving on-chain on a given day. High dormancy indicates that "old hands" (long-term holders / smart money) are actively liquidating or moving inventory; low dormancy indicates transactions are dominated by "young coins" (short-term speculative traders).
2. **Annualized Dormancy Value in USD:** Multiplying daily average dormancy by total transacted volume and the prevailing Bitcoin price yields the instantaneous dollar value of destroyed dormancy ($\text{DormancyUSD}_t = P_t \times \text{CDD}_t$). Taking the 365-day moving average of this daily dormancy value establishes the baseline annualized rate of long-term holder liquidation.
3. **Macro Capitulation Bottoms (Dormancy Flow < 250,000):** Dormancy Flow is defined as current Market Capitalization divided by the Annualized USD Dormancy Value. When Dormancy Flow drops to extreme lows (< 250,000 in standard calibration), current market cap is extraordinarily discounted relative to the spending baseline of veteran holders. This condition indicates either that long-term holders have completely stopped selling at depressed prices or that final distressed capitulation of ancient coins has concluded, historically marking generational accumulation zones.
4. **Entity Adjustment:** Glassnode's entity-adjusted variant filters out internal wallet reshuffling within the same entity (e.g., exchange cold-to-hot wallet rebalancing), isolating genuine economic changes in ownership.

### Research interpretation

The falsifiable quantitative thesis is that **unrealized UTXO holding durations act as an asymmetric state variable for macro market cycle bottoms**:

1. **Information Asymmetry Between Old and Young Supply:** Long-term holders possess higher conviction and lower time preference than short-term momentum traders. When market price drops and dormancy flow compresses into extreme oversold territory, the marginal supply available for sale is exhausted.
2. **Asymmetric Risk-Reward at Cycle Extremes:** When market capitalization falls below the annualized long-term holder dormancy spend, price is structurally underpricing the historical capital retention of the network, creating an asymmetric macro mean-reversion opportunity.
3. **Macro Regime Switching:** Rather than generating high-frequency entry/exit signals, Dormancy Flow serves as a low-turnover regime filter to aggressively scale into long exposure during cycle accumulation windows and de-risk during extended overheated periods.

## Signal

The normalized quantitative strategy defines on-chain macro regime detection and position scaling:

1. **On-Chain Daily Ledger Ingestion (00:00:00 UTC):**
   - $P_t$: Bitcoin daily close price in USD.
   - $\text{Supply}_t$: Total circulating Bitcoin supply.
   - $\text{MC}_t = P_t \times \text{Supply}_t$: Bitcoin market capitalization in USD.
   - $\text{CDD}_t$: Total entity-adjusted Coin Days Destroyed on day $t$:
     $$\text{CDD}_t = \sum_{u \in \text{Spent UTXOs}_t} \text{Value}(u) \times \text{AgeDays}(u)$$
   - $\text{DormancyUSD}_t = P_t \times \text{CDD}_t$

2. **Dormancy Flow Calculation:**
   - Compute the 365-day moving average of daily USD dormancy:
     $$\text{AnnualizedDormancyUSD}_t = \frac{1}{365} \sum_{d=0}^{364} \text{DormancyUSD}_{t-d}$$
   - Calculate Dormancy Flow ($\text{DF}_t$):
     $$\text{DF}_t = \frac{\text{MC}_t}{\text{AnnualizedDormancyUSD}_t}$$

3. **Macro Regime Allocation Rules:**
   - **Deep Value / Historical Bottom Accumulation Regime:**
     $$\text{If } \text{DF}_t \le 250,000:$$
     Scale long exposure to maximum allocation (e.g., 100%–150% spot or long perpetual exposure).
   - **Baseline Holding / Neutral Regime:**
     $$\text{If } 250,000 < \text{DF}_t \le 2,000,000:$$
     Maintain benchmark long exposure (e.g., 50%–100%).
   - **Overheated / Distribution Regime:**
     $$\text{If } \text{DF}_t > 2,000,000 \quad (\text{or macro euphoria threshold } > 3,000,000):$$
     Scale exposure down to defensive allocation (e.g., 0%–25%) or initiate systematic delta hedges.

4. **Underspecified Nuances:**
   - The primary literature presents historical threshold bands (e.g., 250,000) for visual cycle analysis rather than a complete algorithmic execution specification. Dynamic sizing transition curves, trailing stop-losses, and specific re-entry rules upon exiting the accumulation zone represent active research parameters.

## Required data

- **Asset:** Bitcoin (BTC).
- **Frequency:** Daily UTXO ledger aggregations at 00:00:00 UTC.
- **Fields:**
  - Daily USD Close Price ($P_t$).
  - Circulating Supply ($\text{Supply}_t$).
  - Daily Entity-Adjusted Coin Days Destroyed ($\text{CDD}_t$).
  - Daily On-Chain Transacted Volume ($\text{Volume}_t$).
  - Entity-clustering heuristics metadata.
- **Point-in-Time Requirement:** Full on-chain UTXO confirmation for UTC day $t$ before executing on day $t+1$.
- **Availability:** Glassnode, CryptoQuant, Coin Metrics, or customized full-node UTXO indexers.

## Execution assumptions

- **Rebalancing Cadence:** Daily check at 00:00:00 UTC with low-frequency position adjustments (trades occur only during macro regime transitions).
- **Execution Mechanism:** Passive limit orders / TWAP executed over a 1-hour window following daily UTC close.
- **Instruments:** Spot BTC for long accumulation; linear BTC perpetual futures for hedging.
- **Turnover & Costs:** Extremely low annual turnover (< 1 rebalance per year on average), resulting in negligible transaction friction (< 10 bps annualized).

## Evidence

### Source-reported

- David Puell (2019), LookIntoBitcoin, and Glassnode historical analytics document that Dormancy Flow plunged below the 250,000 threshold during every major macro Bitcoin cycle bottom:
  - 2011 bear market bottom (< 200,000);
  - January 2015 capitulation bottom (< 220,000);
  - December 2018 bear market bottom (< 180,000);
  - March 2020 COVID liquidity crash (< 240,000);
  - November–December 2022 FTX collapse (< 200,000).
- In each historical occurrence, the signal identified generational accumulation windows ahead of multi-hundred percent subsequent cyclical advances.
- Ahelegbey, Giudici, and Ingrassia (2021) empirically confirm that coin age and destruction metrics contain statistically significant explanatory power for long-term cryptocurrency valuation.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Entity-Clustering Fragility:** Unadjusted Coin Days Destroyed can be corrupted by large internal exchange wallet reorganizations or custodial migrations, creating artificial spikes in $\text{CDD}_t$ that distort the 365-day moving average denominator.
- **Institutional Off-Chain Migration:** As a substantial fraction of Bitcoin spot trading moves to regulated ETFs, institutional custodians, and centralized derivative venues, UTXO movements on the base blockchain represent a diminishing share of total market price discovery.
- **Low Signal Granularity:** Provides no actionable short-term tactical information during multi-year trending phases between regime extremes.

## Falsification plan

The Dormancy Flow macro hypothesis should be rejected or revised if:
1. Historical backtesting on 2018–2026 data shows that a regime-switching strategy based on the 250,000 threshold fails to achieve higher risk-adjusted return (Sortino/Sharpe) or lower maximum drawdown than a passive buy-and-hold BTC benchmark.
2. An ablation test demonstrates that raw, unclustered CDD yields equivalent or superior performance, indicating that proprietary entity-clustering heuristics introduce look-ahead or over-fitting bias.
3. In modern market cycles, Bitcoin reaches a major multi-year bear market bottom without Dormancy Flow dropping below 250,000 (or, conversely, drops below 250,000 and continues downward for > 12 months with > 50% further drawdown), demonstrating structural parameter instability.
4. A simple price-based 200-day or 365-day moving average discount rule achieves identical or superior cycle bottom timing without requiring complex UTXO age indexation.

## Crypto portability

- **Direct:** For UTXO-based proof-of-work and proof-of-stake blockchains with transparent transaction histories and observable coin ages (e.g., Bitcoin, Litecoin, Dogecoin, Bitcoin Cash).
- **Adapted / Unproven:** For account-based blockchains (e.g., Ethereum, Solana) where tokens reside in mutable balances rather than distinct unspent transaction outputs, requiring synthetic token-age tracking or balance-dormancy approximations.
- **Not Applicable:** For traditional financial assets where individual share holding durations are obscured by custodial street-name registration.

## Limitations

- **Not independently reproduced.**
- **Extreme Low Frequency:** Indicator triggers macro accumulation regimes only once every 2 to 4 years.
- **Sensitivity to Clustering Algorithms:** Dependent on accurate, bias-free entity clustering to eliminate internal custodial transfers.
- **Diminishing Base-Layer Transaction Representation:** Growing institutional ETF holding structures may attenuate on-chain UTXO spending sensitivity.

## Implementation status

Not implemented in the research stack. No PyBroker, NautilusTrader, Paper, Testnet, or Live validation has been performed.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. Presence in the Alpha Strategy Pool does not imply profitable alpha, validated predictability, implementation approval, paper-trading approval, testnet approval, or live-trading approval.

## Related Wiki records

- `bitcoin-onchain-reserve-risk-hodl-conviction-2026-08-31.md` — Reserve Risk HODL conviction indicator.
- `bitcoin-onchain-rhodl-ratio-macro-cycle-2026-08-31.md` — Realized HODL ratio macro cycle metric.
- `bitcoin-onchain-puell-multiple-miner-capitulation-2026-08-31.md` — Puell Multiple miner revenue cycle timing.
- `bitcoin-onchain-sopr-spent-output-profit-ratio-2026-08-31.md` — Spent Output Profit Ratio cycle sentiment.
- `bitcoin-onchain-mvrv-zscore-cycle-reversal-2026-08-31.md` — Market Value to Realized Value cycle reversal.

## Sources

1. LookIntoBitcoin, “Dormancy Flow Live Chart and Indicator Methodology,” (2019–2024). URL: https://lookintobitcoin.com/charts/dormancy-flow/
2. Glassnode Academy, “Entity-Adjusted Dormancy Flow Documentation,” Glassnode Insights (2019–2024). URL: https://academy.glassnode.com/market/dormancy-flow
3. David Puell, “Dormancy Flow: A New Bitcoin Metric,” Cryptolab / Medium Research (March 2019). URL: https://medium.com/@msantoriESQ/dormancy-flow-a-new-bitcoin-metric-773a985f4017
4. Daniel Felix Ahelegbey, Paolo Giudici, and Simone Ingrassia, “Cryptocurrency valuation and on-chain metrics,” *International Review of Financial Analysis*, Volume 78, Article 101861 (2021). DOI: https://doi.org/10.1016/j.irfa.2021.101861
5. Reginald Smith, “Bitcoin Dormancy: A Measure of Bitcoin Inactivity and Spent Coin Age,” Research Notes (2018).
