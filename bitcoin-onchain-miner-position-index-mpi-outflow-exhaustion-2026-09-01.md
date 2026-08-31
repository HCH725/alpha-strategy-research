---
schema: strategy-research-record-v1
title: Bitcoin On-Chain Miner Position Index (MPI) Outflow Exhaustion Reversal
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - on-chain
  - miners
  - supply-flow
  - macro-cycle
status: research-only
confidence: medium
source_as_of: 2020-2026
sources:
  - "https://cryptoquant.com/analytics/query/5ec82f54a86ce96f7cffcc5f"
  - "https://doi.org/10.3982/ECTA16972"
  - "https://doi.org/10.1515/rne-2019-0010"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin On-Chain Miner Position Index (MPI) Outflow Exhaustion Reversal

## Provenance

- **Primary Industry Source:** Ki Young Ju and CryptoQuant Research (2020), "Bitcoin Miner Position Index (MPI)", CryptoQuant Metrics Framework. Stable query reference: [CryptoQuant MPI Analytics](https://cryptoquant.com/analytics/query/5ec82f54a86ce96f7cffcc5f).
- **Academic Theoretical Foundations:**
  - Julien Prat and Benjamin Walter, "An Equilibrium Model of Miner Behavior in the Bitcoin Economy", *Econometrica*, Volume 89, Issue 6, Pages 2883–2917 (2021). DOI: [10.3982/ECTA16972](https://doi.org/10.3982/ECTA16972).
  - Jingyi Ma, Joshua S. Gans, and Rabee Tourky, "Market Structure and Transaction Costs in Proof-of-Work Blockchains", *Review of Network Economics*, Volume 18, Issue 3, Pages 135–158 (2018/2019). DOI: [10.1515/rne-2019-0010](https://doi.org/10.1515/rne-2019-0010).

The metric formalizes on-chain entity-clustered miner wallet outflows relative to their historical baseline, evaluating whether anomalous distribution spikes create systematic price pressure.

## Economic mechanism

### Source-reported

CryptoQuant defines the Miner Position Index (MPI) as the ratio of total daily Bitcoin outflows from all identified miner-affiliated wallets to centralized exchanges relative to the 365-day moving average of those outflows. 

Because Proof-of-Work (PoW) miners face continuous fiat-denominated operational expenditures (electricity bills, hosting contracts, hardware amortization, and debt service), they are structural net suppliers of Bitcoin to spot markets. When miners transfer substantially more Bitcoin than their annual average (typically indicated by an MPI reading greater than 2.0 standard deviations), it signals elevated selling intent, potential profit realization at market peaks, or distress-driven liquidations. Conversely, when MPI remains low or negative, miners are retaining their freshly minted and treasury coins, dampening structural spot sell pressure.

### Research interpretation

The falsifiable hypothesis is that **concentrated physical inventory transfers from capital-intensive network operators (miners) to centralized exchanges induce short-to-intermediate term negative price pressure via order-book absorption limits**:

1. **Spot Supply Overhang:** In an order-driven market, large discrete deposits from miner treasuries to spot exchange deposit addresses precede aggressive market orders or liquidity-consuming limit ask ladders.
2. **Asymmetric Flow Regimes:**
   - **Distribution at Cycle Peaks ($MPI > 2.0$ in Bull Regimes):** When BTC trades at elevated multiples and miner profit margins expand, sudden surges in miner outflow indicate institutional treasury realization, often exhausting marginal buyer liquidity at cycle tops.
   - **Capitulation Wash-out ($MPI > 2.0$ in Bear Regimes):** When BTC trades below miner production cost (e.g. hashprice troughs), an MPI spike marks capitulation (distressed miners dumping reserves to prevent insolvency), which typically forms the final liquidity flush before a macro accumulation bottom.
   - **HODL / Accumulation Regime ($MPI \le 0.0$):** Below-average miner outflows indicate that miners are leveraging balance-sheet financing or retained cash rather than selling BTC, reducing circulating float on spot exchanges.

## Signal

1. **Daily Miner Outflow Computation:**
   For day $t$, sum the total USD-equivalent volume of Bitcoin transferred from addresses classified as mining pools or miner entities to centralized exchange deposit clusters:
   $$MO_t = \sum_{j \in \mathcal{M}} \text{Outflow}_{j \to \text{Exchanges}, t} \times P_t$$
   where $\mathcal{M}$ represents the set of identified miner entity clusters and $P_t$ is the daily BTC/USD closing price.

2. **Rolling Baseline & Standard Deviation:**
   Compute the 365-day rolling arithmetic mean and sample standard deviation of daily miner outflows:
   $$\mu_{365, t} = \frac{1}{365} \sum_{k=0}^{364} MO_{t-k}$$
   $$\sigma_{365, t} = \sqrt{\frac{1}{364} \sum_{k=0}^{364} (MO_{t-k} - \mu_{365, t})^2}$$

3. **Standardized Miner Position Index ($MPI$ Z-Score):**
   $$MPI_t = \frac{MO_t - \mu_{365, t}}{\sigma_{365, t}}$$
   *(Note: The simple ratio formulation $MPI^{\text{ratio}}_t = \frac{MO_t}{\mu_{365, t}}$ is also used in baseline reporting, where a ratio value of $2.0$ serves as the trigger threshold).*

4. **Trading & Risk Regime Logic:**
   - **Distribution / Top-Exhaustion Warning:** If $MPI_t > 2.0$, signal an immediate risk-off state. Actions: close or reduce directional long exposure, tighten trailing stops, or open tactical short/delta-hedge positions on BTC perpetual futures for a 7-day to 30-day holding horizon.
   - **Capitulation Confirmation & Re-Entry:** If $MPI_t > 2.0$ occurs while BTC is trading below its 200-day moving average or below its Realized Price ($P_t < \text{Realized Price}$), register a Capitulation Event. Trigger long entry when $MPI_t$ subsequent mean-reverts back below $0.50$, indicating the forced selling cascade has completed.
   - **Trend Support Regime:** If $MPI_t \le 0.0$, permit full-sized long allocations in trend-following and momentum sub-strategies.

5. **Specification Status:**
   - **Fully specified:** Mathematical calculation of the rolling 365-day normalized z-score and ratio threshold triggers.
   - **Underspecified:** Real-time entity clustering heuristic updates (miners dynamically rotate deposit addresses) and exact execution execution timing (UTC 00:00 bar close vs intraday on-chain mempool alert).

## Required data

- **On-Chain Miner Entity Flows:** Point-in-time daily aggregate BTC volume transferred from miner/pool entity clusters to exchange deposit addresses.
- **Entity Attribution Database:** Heuristic clustering data (co-spend, change-address, direct Coinbase reward recipients) identifying major mining entities (e.g., Foundry USA, AntPool, F2Pool, ViaBTC, Binance Pool, Marathon Digital, Riot Platforms, Core Scientific).
- **Price Series:** Daily BTC/USD OHLCV from major spot exchanges (Binance, Coinbase, Kraken, Bitstamp) with UTC 00:00 boundary standardization.
- **Reference Benchmarks:** Daily Realized Price, Puell Multiple, and 200-day Simple Moving Average for macro regime conditioning.

## Execution assumptions

- **Signal Formation Timing:** Signals are evaluated at the UTC 00:00 daily candle boundary once the daily on-chain block history for day $t$ is fully indexed and confirmed (typically requiring a 10–30 minute data pipeline confirmation buffer).
- **Order Execution:** Executed at day $t+1$ 00:00 UTC open (or via a 1-hour TWAP from 00:00 to 01:00 UTC) using liquid BTC perpetual futures contracts (e.g., Binance, Bybit, OKX).
- **Execution Costs:** Round-trip maker/taker transaction fees assumed at 3–5 bps; bid-ask spread assumed at 1 bp in liquid BTC perpetuals; slippage modeled at 2 bps.
- **Funding & Margin:** Short hedge positions during $MPI > 2.0$ distribution warnings are subject to prevailing perpetual funding rates (positive funding collected when market is bullish/overheated).

## Evidence

### Source-reported

- CryptoQuant research reports that major historical cyclical tops (e.g., December 2017, early 2021) and sharp intermediate corrections were preceded by sustained $MPI > 2.0$ spikes as mining pools liquidated accumulated inventory directly into exchange liquidity pools.
- Prat and Walter (2021, *Econometrica*) demonstrate theoretically and empirically that miner exit and reserve liquidation decisions are tightly coupled with revenue-to-cost ratios, generating discrete aggregate flow shocks during extreme price movements.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Miner clustering heuristics are imperfect and subject to classification noise; large internal balance reorganizations (e.g., moving coins from hot mining wallets to cold institutional custodian vaults or OTC brokers) can be misclassified as exchange deposits if clustering graphs are not updated point-in-time.
- The proliferation of off-exchange institutional OTC desks and derivative-based hedging (e.g., miners selling covered call options or entering forward contracts) means that not all miner hedging passes directly through spot exchange deposit addresses.
- Following Bitcoin halving events (2020, 2024), nominal block rewards decrease by 50%, altering the structural baseline of miner inventory generation and potentially causing structural shifts in raw $MO_t$ series.

## Falsification plan

1. **Event Study Horizon Test:** Conduct an event study on all historical instances where $MPI_t > 2.0$ across the 2017–2026 period. Measure cumulative forward returns of BTC over 1-day, 7-day, 14-day, 30-day, and 60-day windows against an unconditional buy-and-hold baseline. If forward excess return is non-negative ($t\text{-stat} < 1.96$), reject the hypothesis that $MPI > 2.0$ predicts negative short-term price pressure.
2. **Ablation Against Total Exchange Netflow:** Test whether $MPI_t$ provides statistically significant incremental predictive power beyond aggregate exchange netflow (all user deposits minus withdrawals). Run linear and logistic regressions:
   $$\Delta P_{t+k} = \alpha + \beta_1 \text{Netflow}_t + \beta_2 MPI_t + \epsilon_t$$
   If $\beta_2$ is statistically indistinguishable from zero ($p > 0.05$), reject $MPI$ as an independent alpha signal.
3. **Clustering Stability Audit:** Re-evaluate signal performance using alternative third-party on-chain clustering providers (e.g., Glassnode vs CryptoQuant vs Coin Metrics) to test whether results are robust to entity labeling differences.

## Crypto portability

**direct** (Proof-of-Work on-chain mining flow mechanism native to Bitcoin).

Portability to other Proof-of-Work cryptocurrencies (e.g., Litecoin, Dogecoin, Kaspa) is theoretically possible where miner clusters are identifiable, but liquidity is significantly thinner. Not applicable to Proof-of-Stake protocols (e.g., Ethereum post-Merge, Solana), where validator staking rewards and unstaking queues follow different economic dynamics.

## Limitations

- **not independently reproduced**.
- **entity clustering risk:** Reliance on off-chain address attribution heuristics that can change retrospectively.
- **OTC leakage:** Large miners increasingly sell via bilateral OTC agreements rather than public exchange deposit addresses.
- **low frequency:** Daily on-chain signal suitable for macro swing hedging or regime switching, not high-frequency intraday execution.

## Implementation status

No implementation or validation in PyBroker, NautilusTrader, strategy registry, Paper, Testnet, or Live has been performed in this Scout cycle.

`implementation_status: not-implemented`

## Adoption boundary

This record is Alpha Strategy Pool research material only. Presence in this repository does not imply profitability, validated alpha, implementation approval, paper-trading approval, testnet approval, or live-trading approval.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain link was verified in this Scout cycle. Do not fabricate one.

Related strategy families in this repository include:
- `bitcoin-onchain-puell-multiple-miner-capitulation-2026-08-31.md` (Puell Multiple)
- `bitcoin-hash-ribbon-miner-capitulation-2026-08-31.md` (Hash Ribbon Miner Capitulation)
- `bitcoin-onchain-mvrv-zscore-cycle-reversal-2026-08-31.md` (MVRV Z-Score)

## Sources

1. Ki Young Ju and CryptoQuant Research, *Bitcoin Miner Position Index (MPI)*, CryptoQuant Metrics Framework (2020): https://cryptoquant.com/analytics/query/5ec82f54a86ce96f7cffcc5f
2. Julien Prat and Benjamin Walter, *An Equilibrium Model of Miner Behavior in the Bitcoin Economy*, *Econometrica* 89(6), pp. 2883–2917 (2021): https://doi.org/10.3982/ECTA16972
3. Jingyi Ma, Joshua S. Gans, and Rabee Tourky, *Market Structure and Transaction Costs in Proof-of-Work Blockchains*, *Review of Network Economics* 18(3), pp. 135–158 (2019): https://doi.org/10.1515/rne-2019-0010
