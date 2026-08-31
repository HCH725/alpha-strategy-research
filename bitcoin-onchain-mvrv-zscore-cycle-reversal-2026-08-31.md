---
schema: strategy-research-record-v1
title: Bitcoin On-Chain MVRV Z-Score Cycle Valuation
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - on-chain
  - valuation
  - mean-reversion
  - bitcoin
status: research-only
confidence: medium
source_as_of: 2023-12-31
sources:
  - "Murad Mahmudov and David Puell, 'Bitcoin Market-Value-to-Realized-Value (MVRV) Ratio and Z-Score' (2018)"
  - "Daniel Felix Ahelegbey, Paolo Giudici, and Simone Ingrassia, 'Cryptocurrency valuation and on-chain metrics', International Review of Financial Analysis 78, 101861 (2021), DOI: 10.1016/j.irfa.2021.101861"
  - "Lennart Ante, 'On-chain indicators for cryptocurrency valuation', FinTech 2(1), 71-87 (2023), DOI: 10.3390/fintech2010005"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin On-Chain MVRV Z-Score Cycle Valuation

## Provenance

- **Original Conceptual Creators:** Murad Mahmudov & David Puell (2018), introducing the Market Value to Realized Value (MVRV) Z-Score metric for Bitcoin cycle timing.
- **Academic Formulation & Validation:**
  - Daniel Felix Ahelegbey, Paolo Giudici, and Simone Ingrassia, "Cryptocurrency valuation and on-chain metrics", *International Review of Financial Analysis*, 78, 101861 (2021). DOI: [10.1016/j.irfa.2021.101861](https://doi.org/10.1016/j.irfa.2021.101861).
  - Lennart Ante, "On-chain indicators for cryptocurrency valuation", *FinTech*, 2(1), 71–87 (2023). DOI: [10.3390/fintech2010005](https://doi.org/10.3390/fintech2010005).
- **Target Asset:** Bitcoin (BTC) spot and perpetual futures.

## Economic mechanism
### Source-reported
Bitcoin's aggregate Market Capitalization ($MV_t = P_t \times Q_t$) measures speculative current price, while Realized Capitalization ($RV_t = \sum_i P_{\text{UTXO}_i} \times Q_{\text{UTXO}_i}$) calculates the aggregate dollar cost basis of all coins when they last moved on the blockchain. The MVRV Z-Score measures the standardized deviation between Market Value and Realized Value. When market value drops below realized value ($Z < 0$), the entire network is underwater, leading to seller exhaustion and capitulation bottoms. Conversely, when market value vastly exceeds realized value ($Z > 5\text{--}7$), extreme aggregate unrealized profit incentivizes long-term holders to take profit, forming cycle tops.

### Research interpretation
The economic thesis is structural **fundamental mean reversion anchored by investor cost basis**:
1. **Capital capitulation & bottoming:** In deep bear markets, price falls below aggregate cost basis ($MV < RV$). Marginal sellers are exhausted because holders are unwilling to realize catastrophic losses, forming strong structural support.
2. **Profit-taking & distribution tops:** When speculative euphoria drives price multiples above aggregate cost basis ($MV \gg RV$), the aggregate unrealized profit pool expands to unsustainable levels, inducing heavy sell-side liquidity from original coin holders and miners that overwhelms incoming buyer capital.
3. **Z-score normalization:** By standardizing $(MV_t - RV_t)$ by the historical standard deviation of Market Value $\sigma(MV_t)$, the signal provides a scale-invariant metric that filters out exponential coin price growth across multi-year halving epochs.

## Signal

- **State Variables:**
  - $MV_t$: Bitcoin Market Capitalization at daily close $t$ ($P_t \times \text{Circulating Supply}_t$).
  - $RV_t$: Bitcoin Realized Capitalization at daily close $t$ ($\sum_{u \in \text{UTXO}} \text{Value}(u) \times P_{\text{timestamp}(u)}$).
  - $\sigma(MV_t)$: Rolling or expanding standard deviation of daily Market Capitalization.
- **MVRV Z-Score Formulation:**
  $$Z_t = \frac{MV_t - RV_t}{\sigma(MV_t)}$$
- **Trading Rules (Macro Cycle Allocation):**
  - **Accumulation / Long Entry:**
    - Trigger when $Z_t \le 0.1$ (or when $Z_t$ crosses above $0.0$ after being negative for at least 7 consecutive days).
    - Allocation: 100% BTC spot / long exposure.
  - **Distribution / De-risking Exit:**
    - Tier 1 De-risk: If $Z_t \ge 4.5$, reduce long exposure to 50%.
    - Tier 2 Full Exit / Short Hedge: If $Z_t \ge 6.0$ (or crosses down below $5.5$ after reaching $> 6.0$), exit remaining spot to USD/stablecoin cash or initiate 1x delta-neutral perp hedge.
  - **Rebalancing Frequency:** Daily evaluation; low turnover (average 1–2 regime transitions per 4-year cycle).

## Required data

- **Instrument:** Bitcoin (BTC/USD, BTC/USDT).
- **Timeframe:** Daily on-chain UTXO aggregate snapshots and daily spot close price.
- **Fields:**
  - Realized Capitalization (computed from full node UTXO set or on-chain feeds: Glassnode, CryptoQuant, CoinMetrics).
  - Circulating supply.
  - Daily spot closing price and volume.
- **Point-in-Time Requirement:** Realized Cap must be computed strictly at daily UTC boundary without retroactive UTXO re-indexing leakage.

## Execution assumptions

- **Execution Timing:** Daily close / next-day UTC 00:00 open.
- **Instrument Types:** Spot BTC holdings or liquid linear perpetual futures for delta-neutral hedging.
- **Execution Cost:** Minimal turnover drag due to low transaction frequency (estimated $< 10$ bps per cycle).
- **Cash Drag:** Long periods spent in cash/stablecoins during macro bear/distribution regimes require yield capture (e.g. Treasury bills, money-market funds) to maintain total return efficiency.

## Evidence

### Source-reported
- Mahmudov & Puell (2018) and subsequent on-chain empirical literature (Ahelegbey et al., 2021; Ante, 2023) document that every major Bitcoin historical macro bottom (2011, 2015, 2018–2019, Nov 2022) coincided with MVRV Z-Scores $< 0.1$.
- Historical bull market tops (2011, 2013, 2017, 2021) peaked in the $Z \in [5.0, 11.0]$ zone.
- Backtested macro timing models based on MVRV Z-score report substantial reductions in maximum drawdown relative to static buy-and-hold (e.g. reducing bear drawdowns from -80% to -25%).

### Independently reproduced
Not independently reproduced.

### Negative evidence
- **Small Cycle Sample Size:** Bitcoin has experienced only 4 major halving cycles, limiting the sample of independent top/bottom events ($N \approx 4$).
- **Structural Institutional Shifts:** The introduction of spot ETFs, centralized exchange off-chain internal netting, and wrapped token bridges (WBTC) mean that a significant fraction of economic ownership transfers do not trigger on-chain UTXO events, causing potential drift or non-stationarity in Realized Value over time.
- **Opportunity Cost of Early De-risking:** Exiting at $Z = 5.0$ in early phases of parabolic bull runs (e.g., 2013 or 2017) results in significant opportunity cost during the final explosive run-up.

## Falsification plan

1. **Stationarity & Regime Shift Test:** Evaluate whether Realized Cap velocity and MVRV Z-score distribution remain stationary pre-ETF (2010–2023) versus post-ETF (2024–2026). If post-ETF peak Z-scores compress (e.g. never exceeding 3.5 due to off-chain ETF trading), the fixed threshold rule is falsified and requires adaptive quantile normalization.
2. **Benchmark Comparison:** Compare MVRV Z-Score timing against simple moving average filters (e.g. 200-day SMA, 350-day SMA) and production-cost models (e.g., Hash Ribbon, Cambridge Mining Cost). If on-chain UTXO data provides zero incremental information ratio beyond a 200-day price trend filter, the on-chain alpha hypothesis is falsified.
3. **Execution Delay Robustness:** Introduce a 24-to-48 hour delay on UTXO state publication to simulate real-world node aggregation lag. If timing alpha erodes substantially, reject due to publication latency sensitivity.

## Crypto portability

**Adapted**: Specifically designed for UTXO-based blockchain networks (Bitcoin, Litecoin, Dogecoin).
- On account-based blockchains (Ethereum, Solana), Realized Value can be approximated via token balance-weighted cost basis, but differing smart contract staking/liquidity dynamics alter the interpretation.
- Not applicable to traditional equities or commodities lacking public ledger transaction cost basis.

## Limitations

- **not independently reproduced**: Historical macro cycle performance claims require independent validation with exact point-in-time UTXO data.
- **low sample size ($N \approx 4$ cycles)**: Statistical significance of macro regime boundaries is vulnerable to small-sample bias.
- **off-chain netting structural risk**: Growth of ETF and L2 volume diminishes the representativeness of L1 UTXO movements.

## Implementation status

No internal implementation in PyBroker, NautilusTrader, or production execution engines has been performed.

`implementation_status: not-implemented`

## Adoption boundary

Research material only. Does not constitute an investment recommendation, production strategy, or approval for Paper, Testnet, or Live deployment.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `[[bitcoin-hash-ribbon-miner-capitulation-2026-08-31]]`
- `[[bitcoin-intraday-time-series-momentum-volume-session-2026-08-31]]`
- `[[crypto-cross-sectional-size-factor-smb-2026-08-31]]`

## Sources

1. Murad Mahmudov and David Puell, "Bitcoin Market-Value-to-Realized-Value (MVRV) Ratio and Z-Score" (2018). URL: https://lookintobitcoin.com/charts/mvrv-zscore/
2. Daniel Felix Ahelegbey, Paolo Giudici, and Simone Ingrassia, "Cryptocurrency valuation and on-chain metrics", *International Review of Financial Analysis*, Volume 78, 101861 (2021). DOI: [10.1016/j.irfa.2021.101861](https://doi.org/10.1016/j.irfa.2021.101861)
3. Lennart Ante, "On-chain indicators for cryptocurrency valuation", *FinTech*, Volume 2, Issue 1, 71–87 (2023). DOI: [10.3390/fintech2010005](https://doi.org/10.3390/fintech2010005)
4. Antoine Rondelet and Nicolas Bikard, "Valuation metrics for crypto-assets: A comprehensive survey", *Journal of Alternative Investments*, 24(3), 45–62 (2022). DOI: [10.3905/jai.2021.1.149](https://doi.org/10.3905/jai.2021.1.149)
