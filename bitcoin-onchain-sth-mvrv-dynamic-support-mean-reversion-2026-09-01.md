---
schema: strategy-research-record-v1
title: Bitcoin On-Chain STH-MVRV Dynamic Support and Mean Reversion
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - on-chain
  - bitcoin
  - sth-mvrv
  - cost-basis
  - mean-reversion
  - regime-switching
status: research-only
confidence: high
source_as_of: 2024-06-01
sources:
  - "Glassnode Insights & Academy (Checkmate / James Check), 'Short-Term Holder MVRV (STH-MVRV) and Realized Price as Dynamic Market Support/Resistance' (2020–2024)"
  - "Lennart Ante, 'On-chain indicators for cryptocurrency valuation', FinTech 2(1), 71-87 (2023). DOI: 10.3390/fintech2010005"
  - "Daniel Felix Ahelegbey, Paolo Giudici, and Simone Ingrassia, 'Cryptocurrency valuation and on-chain metrics', International Review of Financial Analysis 78, 101861 (2021). DOI: 10.1016/j.irfa.2021.101861"
  - "Murad Mahmudov and David Puell, 'Bitcoin Market-Value-to-Realized-Value (MVRV) Ratio and Z-Score' (2018)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin On-Chain STH-MVRV Dynamic Support and Mean Reversion

## Provenance

- **Primary Conceptual Developers:** Glassnode Research & Engineering team (specifically documented by James Check / Checkmate, 2020–2024), establishing the 155-day coin-age heuristic threshold that separates Short-Term Holders (STH) from Long-Term Holders (LTH).
- **Academic Valuation Foundations:**
  - Lennart Ante, "On-chain indicators for cryptocurrency valuation", *FinTech*, Volume 2, Issue 1, Pages 71–87 (2023). DOI: [10.3390/fintech2010005](https://doi.org/10.3390/fintech2010005).
  - Daniel Felix Ahelegbey, Paolo Giudici, and Simone Ingrassia, "Cryptocurrency valuation and on-chain metrics", *International Review of Financial Analysis*, Volume 78, Article 101861 (2021). DOI: [10.1016/j.irfa.2021.101861](https://doi.org/10.1016/j.irfa.2021.101861).
  - Murad Mahmudov and David Puell, "Bitcoin Market-Value-to-Realized-Value (MVRV) Ratio and Z-Score" (2018).
- **Target Asset:** Bitcoin (BTC/USD, BTC/USDT spot and linear perpetual futures).

## Economic mechanism

### Source-reported

In standard aggregate on-chain analysis, the Market-Value-to-Realized-Value (MVRV) ratio aggregates all unspent transaction outputs (UTXOs) across the entire lifespan of Bitcoin. However, aggregate Realized Price is heavily weighed down by lost coins, early miner genesis block outputs, and multi-year dormant supply that does not participate in active day-to-day market pricing.

Glassnode introduced the **Short-Term Holder Realized Price ($\text{STH-RP}$)** and **Short-Term Holder MVRV ($\text{STH-MVRV}$)** by filtering the UTXO set strictly to coins moved within the past 155 days. Econometrically, unspent outputs younger than 155 days represent the active, price-sensitive marginal buyers and speculative capital in the current market cycle. 

The source documents two structural behavioral regimes:
1. **Bull Trend Equilibrium Support ($\text{STH-MVRV} = 1.0$):** During macro bull expansions, pullbacks where spot price retests $\text{STH-RP}$ ($\text{STH-MVRV} \approx 1.00$) represent the average acquisition break-even level of recent buyers. At this level, seller exhaustion occurs, recent market entrants defend their cost basis, and strong organic accumulation resumes.
2. **Bull Market Euphoria / Overextension ($\text{STH-MVRV} > 1.20\text{--}1.40$ or $+1\sigma / +2\sigma$):** When short-term holders sit on aggregate unrealized profits exceeding $+20\%$ to $+40\%$, the incentive to lock in short-term speculative gains surges, increasing liquid sell-side pressure and creating local cycle tops.
3. **Bear Market Resistance ($\text{STH-MVRV} = 1.0$):** In sustained macro downtrends, relief rallies that approach $\text{STH-RP}$ from below encounter intense distribution as trapped, underwater short-term holders rush to exit at break-even ("get-evenitis").

### Research interpretation

The strategy is a **regime-conditioned on-chain cost-basis mean-reversion and trend-continuation engine**:

1. **Marginal Price-Setter Isolation:** By removing LTH coins ($\ge 155$ days lifespan), STH-MVRV strips away structural non-circulating supply, isolating the marginal buyer's dollar cost basis.
2. **Asymmetric Cost-Basis Psychology:**
   - When $\text{STH-MVRV} \in [0.95, 1.02]$ within an established uptrend ($\text{Price} > \text{200-day EMA}$), downward volatility is bounded by cost-basis defense, providing a high risk-adjusted entry point for trend continuation.
   - When $\text{STH-MVRV}$ crosses $+1.0$ or $+2.0$ standard deviation rolling statistical bands ($Z_{\text{STH}} > 1.5$), profit realization creates predictable local pullbacks.
3. **Regime Switching:** The strategy couples a macro trend filter ($\text{Price} > \text{200-day EMA}$ and $\text{LTH-MVRV} > 1.20$) with intraday/daily STH-MVRV threshold triggers to alternate between leveraged long dip-buying in bull regimes and capital preservation / short hedging in bear regimes.

## Signal

- **UTXO Cohort Partitioning:**
  Let $\mathcal{U}_t$ be the set of active unspent transaction outputs at UTC close of day $t$.
  An output $u \in \mathcal{U}_t$ is classified as Short-Term Holder if:
  $$\text{Age}_t(u) = t - \text{Timestamp}(u) < 155\text{ days}$$

- **STH Realized Capitalization & Realized Price:**
  $$\text{Cap}_{\text{STH}, t} = \sum_{u \in \mathcal{U}_t, \text{Age}_t(u) < 155\text{d}} \text{Amount}(u) \times P_{\text{creation}}(u)$$
  $$\text{Supply}_{\text{STH}, t} = \sum_{u \in \mathcal{U}_t, \text{Age}_t(u) < 155\text{d}} \text{Amount}(u)$$
  $$\text{STH-RP}_t = \frac{\text{Cap}_{\text{STH}, t}}{\text{Supply}_{\text{STH}, t}}$$

- **STH-MVRV Ratio & Standardized Z-Score:**
  $$\text{STH-MVRV}_t = \frac{P_t}{\text{STH-RP}_t}$$
  $$\mu_{\text{STH}, t} = \text{SMA}(\text{STH-MVRV}_t, 90\text{ days})$$
  $$\sigma_{\text{STH}, t} = \text{StdDev}(\text{STH-MVRV}_t, 90\text{ days})$$
  $$Z_{\text{STH}, t} = \frac{\text{STH-MVRV}_t - \mu_{\text{STH}, t}}{\sigma_{\text{STH}, t}}$$

- **Macro Regime Classification:**
  - $\text{Regime}_t = \text{BULL}$ if $P_t > \text{EMA}(P_t, 200\text{ days})$ and $\text{LTH-MVRV}_t \ge 1.0$.
  - $\text{Regime}_t = \text{BEAR}$ otherwise.

- **Trading Execution Rules:**
  1. **Bull Regime Dip Entry (Long BTC):**
     - Condition: $\text{Regime}_t == \text{BULL}$.
     - Trigger: When $\text{STH-MVRV}_t$ tests the dynamic support band $\text{STH-MVRV}_t \in [0.96, 1.02]$ (or rebounds across $1.00$ with $P_t > P_{t-1}$).
     - Target Position: $100\%$ Long BTC spot / linear perpetual futures.
  2. **Bull Regime Overextension Exit / De-risking:**
     - Condition: $\text{Regime}_t == \text{BULL}$.
     - Tier 1 Trim: If $\text{STH-MVRV}_t \ge 1.25$ or $Z_{\text{STH}, t} \ge +1.50$, reduce long exposure to $50\%$.
     - Tier 2 Exit / Cash: If $\text{STH-MVRV}_t \ge 1.40$ or $Z_{\text{STH}, t} \ge +2.00$, exit remaining long to USD/USDT stablecoins.
  3. **Bear Regime Rejection (Short / Neutral Cash):**
     - Condition: $\text{Regime}_t == \text{BEAR}$.
     - Trigger: If $\text{STH-MVRV}_t$ rallies toward $[0.98, 1.03]$ from below and fails ($P_t < P_{t-1}$), hold $100\%$ cash/stablecoins or initiate a $1\times$ short perpetual position.
     - Deep Capitulation Re-entry: When $\text{STH-MVRV}_t < 0.80$ and crosses back above $0.85$, initiate starter long spot position ($25\%$).

## Required data

- **Asset:** Bitcoin (BTC/USD, BTC/USDT).
- **Timeframe:** Daily on-chain UTXO aggregated series (evaluated at 00:00:00 UTC).
- **Fields:**
  - Bitcoin Spot Closing Price ($P_t$).
  - Short-Term Holder Realized Value ($\text{Cap}_{\text{STH}, t}$).
  - Short-Term Holder Supply ($\text{Supply}_{\text{STH}, t}$).
  - Long-Term Holder Realized Value ($\text{Cap}_{\text{LTH}, t}$).
  - 200-day Exponential Moving Average of spot price.
- **Data Availability & Quality:** Node-level UTXO calculation or certified point-in-time on-chain data providers (Glassnode API, CryptoQuant, CoinMetrics) strictly finalized at UTC midnight without retroactive cluster re-tagging.

## Execution assumptions

- **Execution Cadence:** Daily rebalancing at 00:05 UTC following daily on-chain ledger confirmation.
- **Instrument Types:** BTC spot for long holdings; liquid linear USDT/USDC perpetual futures for shorting / hedging.
- **Fee Model:** Standard VIP / retail fee tiers (2–5 bps taker, 0–2 bps maker).
- **Slippage & Impact:** Negligible for BTC spot/perpetual markets at moderate capital scale ($< 3$ bps).
- **Funding & Margin:** Long spot incurs 0 funding cost; short perpetual legs during bear relief rejections collect positive or neutral funding rates.

## Evidence

### Source-reported

- Glassnode Research (Checkmate / James Check, 2021–2024) reports that during the 2016–2017, 2020–2021, and 2023–2024 Bitcoin bull cycles, every major mid-cycle correction (including the July 2021 consolidation, January 2024 post-ETF dip, and May 2024 pullbacks) bottomed within the $\text{STH-MVRV} \in [0.95, 1.02]$ range.
- Glassnode on-chain empirical reports demonstrate that $+1.0\sigma$ ($\text{STH-MVRV} \approx 1.20\text{--}1.25$) and $+2.0\sigma$ ($\text{STH-MVRV} \approx 1.35\text{--}1.45$) levels statistically demarcate local profit-taking regimes with high historical hit rates ($> 75\%$).
- Lennart Ante (2023, *FinTech*) and Ahelegbey et al. (2021, *IRFA*) confirm that segmented on-chain valuation ratios contain statistically significant predictive power for future cryptocurrency returns relative to unsegmented naive market metrics.

All claims above are source-reported and have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Prolonged Submersion During Structural Bear Transitions:** When a macro bull trend breaks down into a deep bear market (e.g., November 2021–January 2022, November 2022 FTX collapse), spot price breaks below STH-RP and fails to recover, causing STH-MVRV to remain suppressed in the $0.70\text{--}0.90$ region for months. Blindly buying the $\text{STH-MVRV} = 1.0$ touch without macro trend filtering ($\text{Price} > \text{200-day EMA}$) results in severe drawdowns.
- **ETF / Off-Chain Netting Dilution:** With the launch of US spot Bitcoin ETFs (January 2024), significant institutional buying occurs off-chain in centralized custodial omnibus wallets (Coinbase Custody), which may alter the velocity and responsiveness of raw UTXO creation dates.

## Falsification plan

1. **Ablation vs. Simple 200-Day Trend Following:** Compare the STH-MVRV regime strategy against a simple 200-day SMA price crossover baseline. If the addition of STH-MVRV does not increase the Information Ratio by at least $+0.25$ and reduce maximum drawdown by at least $15\%$, reject the hypothesis that on-chain UTXO segmentation provides unique incremental alpha.
2. **Cohort Age Boundary Robustness Test:** Test sensitivity to the 155-day threshold by sweeping age thresholds across $K \in [60, 90, 120, 155, 180, 210\text{ days}]$. If the strategy performance is hyper-sensitive to the exact 155-day parameter and collapses at 120 or 180 days, reject the rule as overfitted.
3. **Out-of-Sample Post-ETF Validation:** Test performance exclusively on post-2023 data. If the hit rate of $\text{STH-MVRV} = 1.0$ support bounces drops below $50\%$, falsify the metric for post-ETF market microstructure.

## Crypto portability

**Direct**: Exclusively designed for and native to the Bitcoin UTXO blockchain architecture.

Portability adaptations:
- Applicable to UTXO chains with transparent transaction history (BTC, LTC, DOGE).
- Partially adaptable to account-based networks (Ethereum) via wallet balance age-tiering, though smart contract pools introduce accounting noise.
- Not applicable to traditional asset classes without public ledger settlement.

## Limitations

- **not independently reproduced**: Internal multi-cycle backtest on raw UTXO data is pending.
- **UTXO publication lag**: On-chain metrics require finalized daily blocks; real-time execution must account for node propagation delays.
- **custodial omnibus wallet distortion**: Institutional ETF flows and centralized exchange internal transfers do not produce UTXO movements on every trade.
- **regime filter dependency**: Dip-buying performance relies heavily on the accuracy of the macro regime classification filter.

## Implementation status

No internal implementation in PyBroker, NautilusTrader, or live execution engines has been performed.

`implementation_status: not-implemented`

## Adoption boundary

Research material only. Does not constitute trading advice, production validation, or authorization for Paper, Testnet, or Live deployment.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `[[bitcoin-onchain-mvrv-zscore-cycle-reversal-2026-08-31]]`
- `[[bitcoin-onchain-net-unrealized-profit-loss-nupl-macro-cycle-2026-09-01]]`
- `[[bitcoin-onchain-sopr-spent-output-profit-ratio-2026-08-31]]`
- `[[bitcoin-onchain-cointime-aviv-ratio-true-market-mean-2026-09-01]]`
- `[[bitcoin-onchain-reserve-risk-hodl-conviction-2026-08-31]]`

## Sources

1. Glassnode Insights & Academy (Checkmate / James Check), "Short-Term Holder MVRV (STH-MVRV) and Realized Price as Dynamic Market Support/Resistance" (2020–2024). URL: [https://academy.glassnode.com/market/mvrv/sth-mvrv](https://academy.glassnode.com/market/mvrv/sth-mvrv)
2. Lennart Ante, "On-chain indicators for cryptocurrency valuation", *FinTech*, Volume 2, Issue 1, Pages 71–87 (2023). DOI: [10.3390/fintech2010005](https://doi.org/10.3390/fintech2010005)
3. Daniel Felix Ahelegbey, Paolo Giudici, and Simone Ingrassia, "Cryptocurrency valuation and on-chain metrics", *International Review of Financial Analysis*, Volume 78, Article 101861 (2021). DOI: [10.1016/j.irfa.2021.101861](https://doi.org/10.1016/j.irfa.2021.101861)
4. Murad Mahmudov and David Puell, "Bitcoin Market-Value-to-Realized-Value (MVRV) Ratio and Z-Score" (2018). URL: [https://lookintobitcoin.com/charts/mvrv-zscore/](https://lookintobitcoin.com/charts/mvrv-zscore/)
