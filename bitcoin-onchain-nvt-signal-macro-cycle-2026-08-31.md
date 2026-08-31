---
schema: strategy-research-record-v1
title: Bitcoin On-Chain Network Value to Transactions (NVT) Signal Macro Mean Reversion
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
  - nvt-signal
  - valuation
  - macro-cycle
  - mean-reversion
status: research-only
confidence: medium
source_as_of: 2024-10
sources:
  - https://woobull.com/introducing-nvt-ratio-bitcoins-pe-ratio/
  - https://medium.com/cryptolab/rethinking-network-value-to-transactions-nvt-ratio-introducing-nvt-signal-25e24b7a0f69
  - https://doi.org/10.1016/j.irfa.2021.101861
  - https://academy.glassnode.com/market/nvt/nvt-signal
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin On-Chain Network Value to Transactions (NVT) Signal Macro Mean Reversion

## Provenance

- **Original Concept (NVT Ratio):** Willy Woo, “Introducing NVT Ratio (Bitcoin's PE Ratio),” Woobull Research (February 2017). [https://woobull.com/introducing-nvt-ratio-bitcoins-pe-ratio/](https://woobull.com/introducing-nvt-ratio-bitcoins-pe-ratio/).
- **Primary Methodological Source (NVT Signal):** Dmitry Kalichkin, “Rethinking Network Value to Transactions (NVT) Ratio: Introducing NVT Signal,” Cryptolab Capital (February 2018). [https://medium.com/cryptolab/rethinking-network-value-to-transactions-nvt-ratio-introducing-nvt-signal-25e24b7a0f69](https://medium.com/cryptolab/rethinking-network-value-to-transactions-nvt-ratio-introducing-nvt-signal-25e24b7a0f69).
- **Academic Peer-Reviewed On-Chain Valuation Literature:** Daniel Felix Ahelegbey, Paolo Giudici, and Simone Ingrassia, “Cryptocurrency valuation and on-chain metrics,” *International Review of Financial Analysis*, Volume 78, Article 101861 (2021). DOI: [10.1016/j.irfa.2021.101861](https://doi.org/10.1016/j.irfa.2021.101861).
- **Standardized Industry Reference:** Glassnode Academy, “NVT Signal (NVTS) Documentation and Calculation Methodology,” Glassnode Insights (2019–2024). [https://academy.glassnode.com/market/nvt/nvt-signal](https://academy.glassnode.com/market/nvt/nvt-signal).

## Economic mechanism

### Source-reported

Willy Woo (2017) conceptualized the Network Value to Transactions (NVT) ratio as an analog to the Price-to-Earnings (P/E) ratio for monetary and decentralized settlement networks. Since Bitcoin does not distribute corporate earnings, the USD value of economic transactions transmitted across the blockchain ledger serves as a fundamental proxy for network utility. 

Kalichkin (2018) showed that the original NVT ratio suffered from significant lag because raw daily transaction volumes were noisy, while moving-average smoothing of both market cap and volume introduced substantial phase distortion. Kalichkin introduced the **NVT Signal (NVTS)** by modifying the denominator to use a 90-day simple moving average of daily on-chain transaction volume while keeping daily market capitalization un-smoothed. 

The source-reported rationale states:
1. **Overvaluation / Speculative Euphoria:** When Bitcoin's market capitalization drastically outpaces its 90-day moving average transaction volume ($NVTS > 150$), market valuation is sustained purely by speculative momentum rather than underlying transactional settlement activity, signaling impending cycle tops and mean-reversion downturns.
2. **Undervaluation / Macro Accumulation:** When market capitalization is low relative to transactional throughput ($NVTS < 45$), the network is economically oversold relative to on-chain monetary utility, signaling macro accumulation zones and multi-month cycle bottoms.

### Research interpretation

The falsifiable quantitative hypothesis is that **Bitcoin market capitalization exhibits long-horizon cointegrating equilibrium with smoothed on-chain transaction throughput**:

1. **Metcalfe Settlement Utility:** On-chain transaction volume represents genuine economic velocity, settlement settlement finality, and liquidity demand on the base layer.
2. **Valuation Divergence:** During speculative mania phases, speculative derivatives leverage and retail sentiment push market capitalization well above the steady-state transactional capacity of the network. Because transaction volume cannot instantaneously expand to justify exponential price spikes, the NVTS metric surges to unsustainable levels.
3. **Macro Mean Reversion:** As speculative leverage exhausts and capital inflows slow, the valuation metric mean-reverts back toward its historical moving-average band, producing predictable multi-month asymmetric returns for counter-cyclical rebalancing and macro hedging strategies.

## Signal

The normalized trading rule defines macro regime filters and tactical exposure scaling:

1. **On-Chain Metric Ingestion:**
   For each daily close timestamp $t$ (00:00:00 UTC):
   - $MC_t$: Bitcoin daily market capitalization (or circulating supply $\times$ daily close price $P_t$).
   - $TxVolUSD_t$: Total entity-adjusted USD volume transmitted across the Bitcoin blockchain on day $t$.

2. **NVT Signal (NVTS) Calculation:**
   $$\text{SMA}_{90}(TxVolUSD)_t = \frac{1}{90} \sum_{d=0}^{89} TxVolUSD_{t-d}$$
   $$NVTS_t = \frac{MC_t}{\text{SMA}_{90}(TxVolUSD)_t}$$

3. **Rolling Normalized Z-Score Formulation (Stationarity Adjustment):**
   Because baseline on-chain settlement velocity may evolve across secular halving eras, compute a rolling 2-year (730-day) Z-score:
   $$\mu_{NVTS, t} = \frac{1}{730}\sum_{d=0}^{729} NVTS_{t-d}, \quad \sigma_{NVTS, t} = \sqrt{\frac{1}{730}\sum_{d=0}^{729} (NVTS_{t-d} - \mu_{NVTS, t})^2}$$
   $$Z_{NVTS, t} = \frac{NVTS_t - \mu_{NVTS, t}}{\sigma_{NVTS, t}}$$

4. **Regime and Exposure Rules:**
   - **Macro Overbought / Short Tilt / Take-Profit Regime:**
     $$\text{If } NVTS_t \ge 150 \quad (\text{or } Z_{NVTS, t} \ge +2.0):$$
     Scale spot exposure to minimum allocation (e.g., 0%–25%) or initiate linear perpetual short hedge.
   - **Macro Oversold / Long Accumulation Regime:**
     $$\text{If } NVTS_t \le 45 \quad (\text{or } Z_{NVTS, t} \le -1.5):$$
     Scale spot / perpetual long exposure to maximum allocation (e.g., 100%–150%).
   - **Neutral / Fair Value Band:**
     $$\text{If } 45 < NVTS_t < 150 \quad (\text{or } -1.5 < Z_{NVTS, t} < +2.0):$$
     Maintain benchmark baseline allocation (e.g., 50%–100%).

5. **Underspecified Implementation Nuances:**
   Original sources present historical chart overlays and threshold bands (45 and 150) rather than a complete algorithmic execution execution rule. Specific order sizing ramps, stop-loss invalidation thresholds, and dynamic hedging frequencies are not fixed by the original authors and represent research parameters.

## Required data

- **Asset:** Bitcoin (BTC).
- **Frequency:** Daily on-chain ledger aggregations and daily price closes at 00:00:00 UTC.
- **Fields:**
  - BTC Daily Close Price ($P_t$).
  - Circulating Supply ($S_t$).
  - Daily On-Chain Transaction Volume in USD ($TxVolUSD_t$).
- **Entity Adjustment:** Entity-adjusted transaction volume (filtering out internal change outputs, self-transfers, and exchange wallet consolidations) is strictly preferred to eliminate spurious on-chain volume artifacts.
- **Point-in-Time Requirement:** On-chain blocks and transactions for day $t$ must be fully finalized and consolidated before computing day $t$'s metric at $t+1$ execution.

## Execution assumptions

- **Execution Cadence:** Daily rebalancing at 00:00:00 UTC or weekly macro adjustment.
- **Instrument:** BTC spot for long accumulation; BTC/USDT or BTC/USDC linear perpetual futures for hedging or short exposure.
- **Order Execution:** Passive TWAP limit orders executed over a 1-hour window following the daily close.
- **Transaction Costs & Turnover:** Very low turnover (average trade holding period ranges from several weeks to several months), resulting in minimal fee drag (< 10 bps annualized).

## Evidence

### Source-reported

- Kalichkin (2018) demonstrates that NVTS successfully identified major Bitcoin cycle tops in 2013 and December 2017 (crossing above the 150 upper boundary) and major cycle accumulation bottoms in 2015 and early 2017 (touching or dipping below the 45 lower boundary).
- Glassnode historical analytics confirm that NVTS provides consistent lead-lag signaling around multi-month market turning points across the 2018–2022 market cycles.
- Ahelegbey, Giudici, and Ingrassia (2021) demonstrate in a vector autoregression (VAR) network model that on-chain transaction metrics and derived fundamental ratios exert statistically significant Granger-causal predictive relationships on Bitcoin market capitalization.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Off-Chain Volume Migration (Lightning & L2s):** As transaction volume migrates to off-chain scaling layers (e.g., Lightning Network, centralized exchange internal settlement, and wrapped BTC on Ethereum/Solana), base-layer on-chain transaction volume ($TxVolUSD$) may undercount true aggregate transactional utility, causing secular upward drift in raw NVTS.
- **Entity-Filtering Discrepancies:** Raw unadjusted transaction volume includes massive exchange wallet internal sweeps and change outputs, generating spurious drops in NVTS. Entity-clustering algorithms vary across data providers (e.g., Glassnode, CryptoQuant, Coin Metrics), leading to provider-dependent signal divergence.
- **Prolonged Euphoria in Super-Cycles:** During parabolic bull market legs (such as late 2017 or late 2020), NVTS can remain in the "overbought" (> 150) zone for several consecutive months before price peaks, resulting in premature exit or short-hedge drag during the most profitable segment of a bull trend.

## Falsification plan

The NVTS macro hypothesis should be rejected or revised if:
1. Historical backtesting on entity-adjusted data from 2018–2026 shows that an NVTS regime-switching strategy fails to outperform a simple buy-and-hold BTC benchmark on a risk-adjusted basis (Sharpe ratio and Calmar ratio).
2. Secular stationarity tests (e.g., Augmented Dickey-Fuller) confirm a structural break in the relationship between base-layer transaction volume and market cap due to off-chain layer adoption, rendering fixed threshold boundaries (45 / 150) obsolete.
3. Replacing entity-adjusted volume with raw unadjusted volume destroys the predictive capacity of the signal ($t < 1.65$), proving extreme fragility to data provider heuristics.
4. Adding an on-chain trend or momentum filter (e.g., 200-day SMA) provides strictly superior cycle-timing information without utilizing transaction volume metrics at all.

## Crypto portability

- **Direct** for UTXO-based native layer-1 monetary networks with public ledger transaction histories (e.g., Bitcoin, Litecoin, Bitcoin Cash).
- **Adapted / Unproven** for smart contract platforms (e.g., Ethereum, Solana, Avalanche) where on-chain volume is dominated by DeFi swaps, token mints, and MEV arbitrage rather than peer-to-peer monetary value transfers.
- **Crypto-Specific Considerations:** Metric is uniquely crypto-native, as traditional assets do not possess continuous, publicly verifiable transaction ledgers.

## Limitations

- **Not independently reproduced.**
- **Low Signal Frequency:** Macro cycle indicator generating only a few actionable regime transitions per 4-year halving cycle.
- **Provider Sensitivity:** Heavy reliance on proprietary or heuristic entity-clustering algorithms to isolate genuine economic transaction volume.
- **Off-Chain Utility Leakage:** Does not capture off-chain economic activity on centralized exchanges or secondary layers.

## Implementation status

Not implemented in the research stack. No PyBroker, NautilusTrader, Paper, Testnet, or Live validation has been performed.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. Presence in this repository does not constitute approval for capital allocation, paper trading, or live execution.

## Related Wiki records

- `bitcoin-onchain-mvrv-zscore-cycle-reversal-2026-08-31.md` — on-chain market value to realized value macro cycle reversal.
- `bitcoin-onchain-rhodl-ratio-macro-cycle-2026-08-31.md` — on-chain realized HODL ratio macro cycle metric.
- `bitcoin-onchain-sopr-spent-output-profit-ratio-2026-08-31.md` — spent output profit ratio market sentiment indicator.
- `crypto-cross-sectional-onchain-user-activity-growth-2026-08-31.md` — cross-sectional active address and transaction growth factor.

## Sources

1. Willy Woo, “Introducing NVT Ratio (Bitcoin's PE Ratio),” Woobull Research (February 2017). [https://woobull.com/introducing-nvt-ratio-bitcoins-pe-ratio/](https://woobull.com/introducing-nvt-ratio-bitcoins-pe-ratio/).
2. Dmitry Kalichkin, “Rethinking Network Value to Transactions (NVT) Ratio: Introducing NVT Signal,” Cryptolab Capital (February 2018). [https://medium.com/cryptolab/rethinking-network-value-to-transactions-nvt-ratio-introducing-nvt-signal-25e24b7a0f69](https://medium.com/cryptolab/rethinking-network-value-to-transactions-nvt-ratio-introducing-nvt-signal-25e24b7a0f69).
3. Daniel Felix Ahelegbey, Paolo Giudici, and Simone Ingrassia, “Cryptocurrency valuation and on-chain metrics,” *International Review of Financial Analysis*, Volume 78, Article 101861 (2021). DOI: [10.1016/j.irfa.2021.101861](https://doi.org/10.1016/j.irfa.2021.101861).
4. Glassnode Academy, “NVT Signal (NVTS) Documentation and Historical Indicator Methodology,” Glassnode Insights (2019–2024). [https://academy.glassnode.com/market/nvt/nvt-signal](https://academy.glassnode.com/market/nvt/nvt-signal).
