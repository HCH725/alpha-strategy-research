---
schema: strategy-research-record-v1
title: Bitcoin On-Chain Spent Output Profit Ratio (SOPR) Cycle Reversal and Support/Resistance Regime Oscillator
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - on-chain
  - utxo
  - sopr
  - sentiment
  - cycle-reversal
status: research-only
confidence: high
source_as_of: 2024-06
sources:
  - "Renato Shirakashi, 'Introducing SOPR: Spent Output Profit Ratio' (2019). Glassnode Insights."
  - "Glassnode Academy, 'Adjusted SOPR (aSOPR) and Short-Term Holder SOPR (STH-SOPR)' (2020-2024)."
  - "Checkmate, 'The Mechanics of On-Chain Realized Value and Spent Output Profitability', Glassnode Research (2021-2023)."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin On-Chain Spent Output Profit Ratio (SOPR) Cycle Reversal and Support/Resistance Regime Oscillator

## Provenance

- **Primary Source:** Renato Shirakashi, "Introducing SOPR: Spent Output Profit Ratio" (April 2019), Glassnode Insights / Medium research.
- **Methodological Extensions:** Glassnode Research & Academy, "Adjusted SOPR (aSOPR) and Short-Term Holder SOPR (STH-SOPR)" (2020–2024), documenting UTXO lifespan segmentation (filtering < 1 hour noise and partitioning coins by < 155 days lifespan).
- **Underlying Ledger Architecture:** Full Bitcoin unspent transaction output (UTXO) history, evaluating coin creation price (acquisition cost basis) against coin spent price (realized liquidation value).

## Economic mechanism

### Source-reported
SOPR measures the aggregate profit/loss ratio of all Bitcoin moved on-chain over a specified time window ($SOPR = \frac{\sum \text{Value}_{\text{spent}}}{\sum \text{Value}_{\text{created}}}$). The baseline value of $1.0$ represents the aggregate break-even equilibrium.

In a bull market regime, participants are psychologically reluctant to realize losses; therefore, price pullbacks where SOPR touches or slightly undercuts $1.0$ represent seller exhaustion where only participants willing to sell at cost basis or loss are capitulating, forming strong dynamic support. Conversely, in a bear market regime, rallies where SOPR approaches $1.0$ trigger profit-neutral exit selling by underwater market participants eager to recover their capital, turning $1.0$ into dynamic resistance.

### Research interpretation
The economic thesis is **behavioral reference point anchoring, prospect theory, and on-chain liquidity exhaustion**:
1. **Cost Basis Anchoring:** Market participants experience asymmetric risk preferences (disposition effect). In an uptrend, selling at a loss ($SOPR < 1.0$) is avoided, meaning that when SOPR reaches $1.0$, selling pressure dries up naturally as remaining holders refuse further loss realization.
2. **Capitulation Reset:** In cyclical bull trends, brief excursions where Short-Term Holder SOPR ($STH\text{-}SOPR$) dips below $1.0$ (e.g. $0.97–0.995$) flush out speculative leverage and weak hands. A subsequent recovery back above $1.0$ signals the resumption of organic buying demand.
3. **Cohort Isolation (STH vs LTH):** Raw SOPR can be distorted by ancient coins moved for security or institutional custody migration. STH-SOPR restricts the sample to coins with age $\in [1\text{ hour}, 155\text{ days}]$, directly isolating the marginal price-setting speculative cohort.

## Signal

- **UTXO Valuation:**
  For each spent transaction output $j$ on day $t$:
  $$P_{\text{spent}, j} = \text{BTC/USD price at spend timestamp } t$$
  $$P_{\text{created}, j} = \text{BTC/USD price at creation/receipt timestamp } t_{\text{created}, j}$$
- **Adjusted SOPR ($aSOPR_t$):**
  $$aSOPR_t = \frac{\sum_{j \in \text{Spent}(t), \text{Lifespan}_j \ge 1\text{h}} (P_{\text{spent}, j} \times \text{Amount}_j)}{\sum_{j \in \text{Spent}(t), \text{Lifespan}_j \ge 1\text{h}} (P_{\text{created}, j} \times \text{Amount}_j)}$$
- **Short-Term Holder SOPR ($STH\text{-}SOPR_t$):**
  $$STH\text{-}SOPR_t = \frac{\sum_{j \in \text{Spent}(t), 1\text{h} \le \text{Lifespan}_j \le 155\text{d}} (P_{\text{spent}, j} \times \text{Amount}_j)}{\sum_{j \in \text{Spent}(t), 1\text{h} \le \text{Lifespan}_j \le 155\text{d}} (P_{\text{created}, j} \times \text{Amount}_j)}$$
- **Smoothed Indicator:**
  $$EMA\text{-}SOPR_t = EMA(STH\text{-}SOPR_t, \text{span}=7\text{ days})$$
- **Regime Filter:**
  $$Regime_t = \begin{cases} \text{BULL} & \text{if } P_{\text{BTC}, t} > SMA(P_{\text{BTC}}, 200\text{d})_t \text{ and } MVRV_t > 1.0 \\ \text{BEAR} & \text{otherwise} \end{cases}$$
- **Trading Rules:**
  - **Bull Regime Long Entry:** If $Regime_t == \text{BULL}$, when $STH\text{-}SOPR$ dips into capitulation territory ($STH\text{-}SOPR < 1.0$) and crosses back above $1.00$ with daily positive return confirmation ($P_t > P_{t-1}$), enter Long BTC.
  - **Bull Regime Long Exit:** Exit to cash when $STH\text{-}SOPR > 1.08$ (extreme euphoria/distribution) or when $STH\text{-}SOPR$ crosses below its 14-day EMA.
  - **Bear Regime Cash/Short Entry:** If $Regime_t == \text{BEAR}$, when $STH\text{-}SOPR$ rallies toward $1.00$ ($STH\text{-}SOPR \in [0.995, 1.015]$) and turns downward ($STH\text{-}SOPR_t < STH\text{-}SOPR_{t-1}$), enter Short BTC or remain 100% in USD/stablecoins.

## Required data

- **Universe:** Bitcoin (BTC/USD or BTC/USDT spot and perpetual contracts).
- **Timeframe:** Daily on-chain aggregated UTXO spend metrics (00:00 UTC finalization).
- **Fields:** Bitcoin daily OHLCV, UTXO spend volume, realized spend value, creation realized value, coin age distribution (STH/LTH buckets), 200-day price moving average, MVRV ratio.
- **Availability:** Point-in-time on-chain data with minimum 2-hour confirmation lag buffer to prevent reorganization/mempool bias.

## Execution assumptions

- **Execution Timing:** Daily execution at 00:00 UTC plus 2 hours for on-chain block finalization (02:00 UTC execution).
- **Order Types:** Limit orders or 15-minute TWAP on liquid BTC spot/perpetual venues (Binance, Coinbase, OKX).
- **Fees & Slippage:** 2–5 bps taker fee; 1–2 bps slippage on BTC deep order books.
- **Shorting Mechanism:** CME Bitcoin futures or perpetual swap contracts for the bear regime short leg.

## Evidence

### Source-reported
- Renato Shirakashi (2019) and Glassnode Research document that across Bitcoin's historical market cycles (2012–2024), SOPR $= 1.0$ acted as rigid floor support during structural bull runs (e.g. 2013, 2016–2017, late 2020, 2023–2024). Bullish pullbacks resetting to SOPR $\approx 1.0$ yielded $>70\%$ positive 30-day forward returns.
- During structural bear phases (e.g. 2014–2015, 2018, 2022), relief rallies consistently stalled as SOPR reached $1.00–1.01$, marking optimal macro distribution and hedging points.

### Independently reproduced
Not independently reproduced.

### Negative evidence
- **Structural Bear Submersion:** In severe capitulation events (e.g. November 2018 BCH fork hash war, March 2020 liquidity shock, November 2022 FTX collapse), STH-SOPR can remain deeply suppressed below $1.0$ ($0.88–0.95$) for multiple weeks. Unconditioned dip-buying without macro trend filters incurs severe drawdowns.
- **Reporting Latency:** On-chain metrics require finalized daily block states, precluding sub-daily high-frequency execution.

## Falsification plan

1. **Regime Filter Ablation:** Evaluate the strategy without the 200-day MA / MVRV macro regime filter. If unconditioned SOPR dip-buying generates a negative Sharpe ratio or maximum drawdown exceeding 45% over the 2015–2026 backtest sample, confirm that SOPR is an asymmetric regime-conditional indicator rather than an unconstrained mean-reverting oscillator.
2. **Cohort Segmentation Comparison:** Compare strategy performance using raw SOPR vs aSOPR vs STH-SOPR. If STH-SOPR does not yield a statistically significant improvement in Information Ratio ($p > 0.05$), falsify the Short-Term Holder cohort isolation hypothesis.
3. **Out-of-Sample Finalization Buffer:** Introduce simulated 24-hour and 48-hour reporting delays. If strategy returns decay by more than 25%, reject operational viability under delayed on-chain indexing.

## Crypto portability

**Direct**: SOPR is a native cryptographic on-chain metric derived specifically from the UTXO accounting model of the Bitcoin blockchain. It is directly applicable to Bitcoin and adaptable to other UTXO-based chains (e.g., Litecoin, Dogecoin).

## Limitations

- **not independently reproduced**: Historical validation in our NautilusTrader/PyBroker environment is pending.
- **single-asset concentration**: Primarily applicable to Bitcoin (and major UTXO networks); does not apply directly to account-based smart contract blockchains (Ethereum, Solana) without complex balance-tracking approximations.
- **data provider dependency**: Requires reliable on-chain indexing infrastructure (e.g. Glassnode, CryptoQuant, CoinMetrics, or self-hosted Bitcoin Core indexer).

## Implementation status

No internal implementation in PyBroker, NautilusTrader, or live execution engines has been completed.

`implementation_status: not-implemented`

## Adoption boundary

Research material only. Does not constitute trading advice, production validation, or authorization for Paper, Testnet, or Live deployment.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `[[bitcoin-onchain-mvrv-zscore-cycle-reversal-2026-08-31]]`
- `[[bitcoin-hash-ribbon-miner-capitulation-2026-08-31]]`
- `[[crypto-cross-sectional-onchain-user-activity-growth-2026-08-31]]`

## Sources

1. Renato Shirakashi, "Introducing SOPR: Spent Output Profit Ratio", *Glassnode Insights* (April 2019). URL: [https://insights.glassnode.com](https://insights.glassnode.com)
2. Glassnode Academy, "Adjusted SOPR (aSOPR) and Short-Term Holder SOPR (STH-SOPR) Methodology" (2020–2024). URL: [https://academy.glassnode.com/market/sopr](https://academy.glassnode.com/market/sopr)
3. Checkmate, "The Mechanics of On-Chain Realized Value and Spent Output Profitability", *Glassnode Research* (2021–2023).
