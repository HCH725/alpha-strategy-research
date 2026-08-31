---
schema: strategy-research-record-v1
title: Bitcoin On-Chain Reserve Risk Long-Term Holder Conviction Ratio
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
  - reserve-risk
  - hodl-bank
  - conviction
  - macro-cycle
status: research-only
confidence: medium
source_as_of: 2024-10
sources:
  - https://lookintobitcoin.com/charts/reserve-risk/
  - https://academy.glassnode.com/market/reserve-risk
  - https://medium.com/ikigai-asset-management/reserve-risk-a-new-metric-for-bitcoin-f975b9f7dd93
  - https://doi.org/10.1016/j.irfa.2021.101861
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin On-Chain Reserve Risk Long-Term Holder Conviction Ratio

## Provenance

- **Original Conceptual Creator:** Hans Hauge (Ikigai Asset Management, 2019), introducing Reserve Risk to evaluate the risk-to-reward ratio of Bitcoin by measuring the opportunity cost and conviction of long-term holders.
- **Primary Methodological Reference:** LookIntoBitcoin, "Reserve Risk Historical Chart and Methodology" (2019–2024). [https://lookintobitcoin.com/charts/reserve-risk/](https://lookintobitcoin.com/charts/reserve-risk/).
- **Standardized Industry Reference:** Glassnode Academy, "Reserve Risk Documentation and Calculation Specification" (2019–2024). [https://academy.glassnode.com/market/reserve-risk](https://academy.glassnode.com/market/reserve-risk).
- **Original Source Publication:** Hans Hauge, "Reserve Risk: A New Metric for Bitcoin," Ikigai Asset Management (May 2019). [https://medium.com/ikigai-asset-management/reserve-risk-a-new-metric-for-bitcoin-f975b9f7dd93](https://medium.com/ikigai-asset-management/reserve-risk-a-new-metric-for-bitcoin-f975b9f7dd93).
- **Academic Context:** Daniel Felix Ahelegbey, Paolo Giudici, and Simone Ingrassia, “Cryptocurrency valuation and on-chain metrics,” *International Review of Financial Analysis*, Volume 78, Article 101861 (2021). DOI: [10.1016/j.irfa.2021.101861](https://doi.org/10.1016/j.irfa.2021.101861).

## Economic mechanism

### Source-reported

Hans Hauge (2019) conceptualized Reserve Risk as a measure of long-term holder conviction relative to market price. Every day an investor holds Bitcoin without selling, they accumulate "coin-days" and choose not to realize cash gains at current market prices, incurring an unspent opportunity cost.

1. **HODL Bank (Accumulated Conviction):** The "HODL Bank" is modeled as the cumulative sum of the daily median opportunity cost (daily market price minus the median value of coin-days destroyed). When long-term holders resist selling across prolonged market periods, the HODL Bank expands, signaling high market conviction and reduced circulating supply.
2. **Reserve Risk Ratio ($P / \text{HODL Bank}$):**
   - **Low Reserve Risk (Green Zone, $< 0.002$):** When price is low and HODL Bank conviction is high, market participants have low incentive to sell, while long-term holders demonstrate maximum conviction. Historically, this corresponds to generational accumulation bottoms with an attractive risk-to-reward asymmetry.
   - **High Reserve Risk (Red Zone, $> 0.020$):** When price is high and long-term holders actively spend dormant coins (destroying coin-days), HODL Bank growth stalls while market price escalates. This indicates that long-term conviction has been monetized into late-cycle liquidity, signaling macro distribution tops and unattractive risk/reward.

### Research interpretation

The falsifiable quantitative thesis is that **Bitcoin price is constrained over multi-year horizons by the aggregate opportunity cost of its long-term holder base**:

1. **Behavioral Inaction as Revealed Conviction:** Holding coins through volatile market drawdowns and bull expansions reflects strong structural conviction. The unspent coin-day accumulation serves as a fundamental proxy for market supply-side tightness.
2. **Macro Divergence Detection:** During euphoric speculative tops, old dormant coins move on-chain to centralized venues at unprecedented velocity. This coin destruction rapidly outpaces organic HODL Bank compounding, driving the Reserve Risk ratio upward.
3. **Asymmetric Risk/Reward Regime Classification:** By comparing the spot incentive to sell against the cumulative opportunity cost, Reserve Risk provides a continuous, non-price-only cycle valuation metric that filters out short-term speculative noise.

## Signal

The normalized trading rule defines macro regime bands and tactical exposure:

1. **On-Chain Metric Ingestion:**
   For each daily close timestamp $t$ (00:00:00 UTC):
   - $P_t$: Bitcoin daily close price in USD.
   - $\text{CDD}_t$: Coin Days Destroyed on day $t$ (number of coins transacted multiplied by the number of days since they were last moved).
   - $S_t$: Circulating supply of Bitcoin on day $t$.
   - $\text{Supply-Adjusted CDD}_t = \frac{\text{CDD}_t}{S_t}$.

2. **HODL Bank Formulation:**
   - Daily Value of Coin Days Destroyed:
     $$\text{VOCDD}_t = P_t \times \text{Supply-Adjusted CDD}_t$$
   - 30-Day Moving Median of VOCDD (smoothing daily transaction noise):
     $$\text{MVOCDD}_t = \text{Median}(\{\text{VOCDD}_{t-d}\}_{d=0}^{29})$$
   - Daily Opportunity Cost:
     $$\Delta \text{HODL Bank}_t = P_t - \text{MVOCDD}_t$$
   - Cumulative HODL Bank:
     $$\text{HODL Bank}_t = \sum_{\tau=1}^t \Delta \text{HODL Bank}_\tau$$

3. **Reserve Risk Calculation:**
   $$\text{Reserve Risk}_t = \frac{P_t}{\text{HODL Bank}_t}$$

4. **Macro Regime Allocation Rules:**
   - **Macro Value / High Conviction Accumulation Regime:**
     $$\text{If } \text{Reserve Risk}_t \le 0.0020:$$
     Scale long exposure to maximum allocation (e.g., 100%–150% spot/perp long) or initiate systematic accumulation tranches.
   - **Macro Overbought / High Risk Derisking Regime:**
     $$\text{If } \text{Reserve Risk}_t \ge 0.0200:$$
     Scale spot exposure down to defensive allocation (e.g., 0%–25%) or initiate linear perpetual short hedge.
   - **Neutral Band:**
     $$\text{If } 0.0020 < \text{Reserve Risk}_t < 0.0200:$$
     Maintain benchmark baseline allocation (e.g., 50%–100%).

5. **Underspecified Nuances:**
   Original sources present chart overlays and static threshold bands ($0.002$ and $0.020$) rather than fully specified algorithmic execution models. Sizing curves between bands, adjusted rolling variants (e.g., dividing by a 300-day moving average), and explicit risk invalidation triggers represent empirical research choices.

## Required data

- **Asset:** Bitcoin (BTC).
- **Frequency:** Daily on-chain ledger aggregations at 00:00:00 UTC.
- **Fields:**
  - BTC Daily Close Price ($P_t$).
  - Coin Days Destroyed ($\text{CDD}_t$).
  - Circulating Supply ($S_t$).
- **Point-in-Time Requirement:** Full ledger finality across UTC day $t$ prior to signal formation for day $t+1$.
- **Availability:** Supported natively via Bitcoin core indexers and standard on-chain analytics providers (Glassnode, LookIntoBitcoin, CryptoQuant).

## Execution assumptions

- **Execution Cadence:** Daily rebalance at 00:00:00 UTC or weekly macro regime alignment.
- **Instrument:** BTC spot for long accumulation; BTC linear perpetual futures for hedging/underweighting.
- **Order Execution:** Passive TWAP limit orders executed over a 1-hour window following the daily close.
- **Turnover & Friction:** Extremely low annual turnover (holding periods span several months to years), resulting in minimal fee drag (< 15 bps annualized).

## Evidence

### Source-reported

- Hans Hauge (2019) and Glassnode analytics demonstrate that Reserve Risk successfully bounded historical Bitcoin cycles:
  - Generational bottom entries into the green zone ($\le 0.0020$) in 2011, early 2015, December 2018–early 2019, March 2020, and late 2022 (FTX collapse).
  - Cycle top entries into the red zone ($\ge 0.0200$) during the 2011, 2013, and late 2017 bull peaks.
- In the 2021 bull run, Reserve Risk reached the upper boundary in early 2021 before rolling over, correctly signaling distribution prior to the November 2021 double top.
- Academic literature on on-chain age-weighted metrics (Ahelegbey et al., 2021) validates that Coin Days Destroyed and dormancy-derived metrics contribute statistically significant explanatory power for long-term cryptocurrency return dynamics.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Cumulative Downward Drift:** Because HODL Bank is a cumulative sum that monotonically expands over multi-year periods as the network matures, the unadjusted Reserve Risk metric exhibits a structural secular downward drift. In later cycles (e.g., 2021–2024), the metric failed to reach historical peak values (> 0.03), requiring heuristic "Adjusted Reserve Risk" normalizations.
- **Lost and Inactive Coins:** Millions of early coins (including the Satoshi Nakamoto coins and lost private keys) permanently accumulate coin-days and are never destroyed. This inflates the denominator and creates a permanent non-economic baseline in HODL Bank calculations.
- **Entity Consolidation Artifacts:** Large centralized exchange internal cold-storage migrations or UTXO consolidations can cause massive spurious spikes in Coin Days Destroyed ($\text{CDD}_t$), creating artificial transitory drops in the HODL Bank that do not reflect genuine market selling pressure.

## Falsification plan

The Reserve Risk hypothesis should be rejected or revised if:
1. Backtesting on 2018–2026 data shows that an allocation strategy driven by Reserve Risk (or Adjusted Reserve Risk) fails to outperform a buy-and-hold BTC benchmark on a Sharpe, Sortino, or Calmar ratio basis.
2. Stationarity and cointegration tests show that the ratio's predictive power is entirely degraded in post-2021 data without arbitrary parameter rescaling, confirming structural non-stationarity.
3. Spurious UTXO consolidation events (filtering out known exchange cold-storage transactions) alter the regime classification by more than 20%, indicating unacceptable fragility to non-economic on-chain noise.
4. Adding an on-chain MVRV or simple 200-day trend filter completely subsumes the alpha of Reserve Risk in multivariate regression ($t < 1.65$).

## Crypto portability

- **Direct** for UTXO-based public blockchains with explicit coin age tracking (e.g., Bitcoin, Litecoin, Bitcoin Cash, Dogecoin).
- **Adapted / Unproven** for account-based blockchains (e.g., Ethereum, Solana) where token balances are fungible state accounts rather than discrete unspent transaction outputs with determinable creation timestamps.
- **Crypto-Specific Considerations:** Metric is uniquely crypto-native, as traditional equity and commodity markets lack transparent, per-unit holding duration ledgers.

## Limitations

- **Not independently reproduced.**
- **Low Signal Frequency:** Macro cycle indicator generating only 1–2 regime transitions per market cycle.
- **Secular Drift:** Unadjusted cumulative HODL Bank causes threshold decay across successive market cycles.
- **Exchange UTXO Noise:** Susceptible to false CDD spikes caused by exchange wallet reorganization rather than actual market distribution.

## Implementation status

Not implemented in the research stack. No PyBroker, NautilusTrader, Paper, Testnet, or Live validation has been performed.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. Presence in the Alpha Strategy Pool does not imply profitable alpha, validated predictability, implementation approval, paper-trading approval, testnet approval, or live-trading approval.

## Related Wiki records

- `bitcoin-onchain-mvrv-zscore-cycle-reversal-2026-08-31.md` — on-chain market value to realized value macro cycle reversal.
- `bitcoin-onchain-rhodl-ratio-macro-cycle-2026-08-31.md` — on-chain realized HODL ratio macro cycle metric.
- `bitcoin-onchain-sopr-spent-output-profit-ratio-2026-08-31.md` — spent output profit ratio market sentiment indicator.
- `bitcoin-onchain-nvt-signal-macro-cycle-2026-08-31.md` — on-chain network value to transactions signal.
- `bitcoin-onchain-puell-multiple-miner-capitulation-2026-08-31.md` — on-chain Puell Multiple miner capitulation indicator.

## Sources

1. Hans Hauge, “Reserve Risk: A New Metric for Bitcoin,” Ikigai Asset Management / Medium (May 2019). URL: https://medium.com/ikigai-asset-management/reserve-risk-a-new-metric-for-bitcoin-f975b9f7dd93
2. LookIntoBitcoin, “Reserve Risk Historical Chart and Indicator Methodology,” (2019–2024). URL: https://lookintobitcoin.com/charts/reserve-risk/
3. Glassnode Academy, “Reserve Risk Documentation and Technical Calculation,” Glassnode Insights (2019–2024). URL: https://academy.glassnode.com/market/reserve-risk
4. Daniel Felix Ahelegbey, Paolo Giudici, and Simone Ingrassia, “Cryptocurrency valuation and on-chain metrics,” *International Review of Financial Analysis*, Volume 78, Article 101861 (2021). DOI: https://doi.org/10.1016/j.irfa.2021.101861
