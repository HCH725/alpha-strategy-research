---
schema: strategy-research-record-v1
title: "Public Wallet Identity, Persistent Trader Informativeness, and Adverse Selection Avoidance"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - market-microstructure
  - trader-identity
  - wallet-tracking
  - adverse-selection
  - order-flow-imbalance
  - limit-order-book
  - hyperliquid
status: research-only
confidence: medium
source_as_of: 2026-08-01
sources:
  - "Daojing Zhai, 'Public Trader Identity: Adverse Selection and Return Predictability', arXiv:2608.04373v1 [q-fin.TR, q-fin.PR], August 2026. https://arxiv.org/abs/2608.04373"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Public Wallet Identity, Persistent Trader Informativeness, and Adverse Selection Avoidance

## Provenance

- **Paper URL:** https://arxiv.org/abs/2608.04373
- **Full arXiv ID:** arXiv:2608.04373v1 [q-fin.TR, q-fin.PR]
- **Author:** Daojing Zhai (Baruch College, City University of New York)
- **Submitted Date:** August 2026
- **Primary Categories:** Quantitative Finance - Trading and Market Microstructure (`q-fin.TR`), Pricing of Securities (`q-fin.PR`)
- **Dataset / Venue:** Reconstructed full-depth Limit Order Book (LOB) from Level-4 message streams on Hyperliquid perpetual DEX during July 2026; 17.1 billion order-status and book-diff messages, 14.3 million aggressive taker orders from 147,113 unique pseudonymous wallets, representing $84.3 billion in taker notional.

## Economic mechanism

### Source-reported

In traditional market microstructure theory (e.g., Kyle 1985, Glosten-Milgrom 1985), informed traders require pseudonymity/anonymity to "hide" among uninformed noise traders to extract informational rents without revealing their identities. On decentralized limit order book exchanges (such as Hyperliquid), every order placement, cancellation, rejection, and execution is broadcast with a persistent pseudonymous wallet address.

The author establishes that:
1. **Persistent Informativeness:** A trader's "informativeness" (measured by post-trade price drift following their aggressive orders) is a persistent, stable attribute. Ranking wallets by post-trade price impact over a 10-day estimation window demonstrates a Spearman rank correlation of **0.52** over the subsequent 10-day out-of-sample window.
2. **Identity Increment to Return Predictability:** Conditioning short-horizon return predictions on wallet identity metrics delivers an out-of-sample $R^2$ of **12.31%** for 1-second price changes, representing a **13.2% relative gain ($t = 9.2$)** over standard anonymous benchmarks that utilize only price, quote, and aggregate order flow imbalance (OFI).
3. **Trade-Event Concentration:** At the exact moment of realized aggressive trades (rather than regular time-sampled intervals), the incremental $R^2$ provided by trader identity increases from **1.43 percentage points to 2.47 percentage points**.

### Research interpretation

This paper reveals two distinct systematic trading mechanisms in transparent-identity DEX environments:
1. **Adverse-Selection-Aware Liquidity Provision (Defensive Alpha):**
   - Market makers quoting passive limit orders suffer from adverse selection when filled by top-decile "toxic" (informed) wallets.
   - By maintaining a real-time rolling ledger of wallet informativeness scores, a passive market maker can dynamically widen spreads, reduce depth, or send immediate order cancellations when an aggressive incoming order originates from a high-ranked informed wallet.
2. **Informed Order-Flow Momentum & Shadowing (Offensive Alpha):**
   - Aggressive taker orders from top-decile informativeness wallets generate persistent short-horizon (1s–10s) directional price drift.
   - Systematic takers can co-trade or shadow aggressive orders initiated by persistent alpha wallets, capturing post-trade continuation before passive quotes adjust.

## Signal

### Signal A: Wallet Informativeness Score ($WIS$)
- **Formation Timestamp:** Updated on a rolling 10-day lookback cadence at daily close (00:00:00 UTC).
- **Metric Formulation:**
  For each active wallet $w$ with $N_w \ge 50$ aggressive trades over the past 10 days:
  $$WIS_{w, t} = \frac{1}{N_w} \sum_{i=1}^{N_w} \text{Sign}_i \cdot \frac{P_{i + 1\text{s}} - P_i}{P_i}$$
  where $\text{Sign}_i \in \{+1, -1\}$ denotes aggressive buy vs. sell, $P_i$ is fill price, and $P_{i + 1\text{s}}$ is the midprice 1 second post-execution.
- **Quantile Bucket Assignment:** Wallets are sorted into deciles $D_1$ (most uninformed/noise) to $D_{10}$ (highest informativeness/toxic).

### Signal B: Real-Time Identity-Aware Order Flow Imbalance ($I\text{-}OFI$)
- **Lookback:** Rolling 1-second micro-window.
- **Formula:**
  $$I\text{-}OFI_t = \sum_{k \in \text{Trades}_{t-1\text{s}, t}} \text{Sign}_k \cdot \text{Size}_k \cdot \omega(WIS_{\text{wallet}(k)})$$
  where $\omega(WIS) = \mathbf{1}_{\{w \in D_{10}\}} \cdot 2.0 + \mathbf{1}_{\{w \in D_1..D_9\}} \cdot 1.0 - \mathbf{1}_{\{w \in D_1\}} \cdot 0.5$.
- **Offensive Directional Entry:**
  - Long: $I\text{-}OFI_t > \theta_{\text{long}}$ accompanied by an aggressive buy from a $D_{10}$ wallet.
  - Short: $I\text{-}OFI_t < -\theta_{\text{short}}$ accompanied by an aggressive sell from a $D_{10}$ wallet.
- **Defensive Cancellation Trigger:**
  - If a resting maker bid is matched or immediately preceded by an order from a $D_{10}$ wallet, instantly pull remaining maker inventory on that side.
- **Exit / Holding Period:** 1 to 5 seconds (microstructure high-frequency horizon). Take profit on mean reversion of spread; hard stop at $1.0 \times \text{spread}$.

## Required data

- **Instrument:** Perpetual futures contracts on transparent DEXs (e.g., BTC-PERP, ETH-PERP, SOL-PERP on Hyperliquid).
- **Universe:** Liquid perpetual pairs with high taker volume and active wallet turnover.
- **Venue:** Decentralized L2/L3 order book venues exposing on-chain or peer-to-peer event streams with persistent address tags (Hyperliquid, dYdX v4, Paradex).
- **Timeframe:** Sub-second tick-level order book event streams (Level-4 order lifecycles: placement, cancel, fill, reject).
- **Fields:**
  - Transaction hash / event sequence ID.
  - Trader wallet public address (`sender_address`).
  - Order type (market / aggressive taker vs. passive maker limit).
  - Price, size, side (buy/sell).
  - L2 full-depth bids/asks and midprice at $t, t+1\text{s}, t+5\text{s}, t+10\text{s}$.
- **Point-in-time:** True real-time websocket feed; strictly causal wallet history aggregation (10-day lookback prior to $t$).

## Execution assumptions

- **Order Type:**
  - Defensive: Ultra-low latency cancellation requests (`cancel_order` / `cancel_all`).
  - Offensive: Aggressive IOC limit orders or rapid taker orders placed within 5–20ms of detecting informative wallet prints.
- **Fill Model:** Immediate taker execution at top-of-book; 1–3 bps estimated adverse selection slippage.
- **Fees:** VIP DEX taker fee (0.02%–0.035%) or maker rebate (0.00%–0.005%). Note: Offensive taker strategy requires gross price drift > round-trip taker fees (4–7 bps), or execution via maker limit orders pegged ahead of the queue.
- **Latency:** Colocated or low-latency RPC connection to validator nodes (< 20ms) required.

## Evidence

### Source-reported

- **Empirical Dataset:** Reconstructed Level-4 limit order book from Hyperliquid perpetual DEX during July 2026 (17.1 billion messages, 14.3 million aggressive orders, 147,113 unique wallets, $84.3 billion taker notional).
- **Rank Persistence:** Spearman rank correlation of **0.52** for wallet informativeness scores across non-overlapping adjacent 10-day observation windows.
- **Predictive Performance:** Out-of-sample $R^2 = 12.31\%$ for 1-second price changes using a linear model with wallet identity features, compared to anonymous OFI and quote benchmarks, yielding a **13.2% relative improvement ($t = 9.2$)**.
- **Realized Event Boost:** Incremental $R^2$ contributed by wallet identity increases from **1.43 percentage points** at time-sampled intervals to **2.47 percentage points** at the exact timestamps of realized trades.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Sybil Attacks / Address Churn:** Sophisticated informed traders who detect that their wallet is being shadowed or faded may rotate to fresh, unranked wallet addresses to mask order flow, degrading the 10-day persistence metric.
- **Taker Fee Friction:** A 1-second gross price drift of 2–5 bps is insufficient to cover standard non-VIP taker fees (3–5 bps each way), meaning direct offensive taker copying is unprofitable without zero-fee tiers or market-making rebate status.
- **Exchange Anonymization Risk:** Centralized exchanges (Binance, OKX, Bybit) conceal counterparty wallet identities, rendering this specific identity-based signal completely unobservable on CEX venues.

## Falsification plan

1. **Subsample Rank Stability Decay Test:** Measure the autocorrelation and Spearman rank correlation of wallet informativeness scores across rolling 1-day, 3-day, 7-day, and 14-day horizons. **Failure rule:** If rank correlation drops below 0.20 for horizons $\ge 3$ days, persistent informativeness is falsified as fleeting noise.
2. **Fee-Adjusted Shadowing Backtest:** Simulate directional taker entry shadowing top-decile ($D_{10}$) wallets across all Hyperliquid pairs with realistic 5 bps round-trip taker fees and 20ms execution delay. **Failure rule:** If net strategy Sharpe ratio $< 0.0$, the offensive copy-trading interpretation is rejected.
3. **Sybil / Address Rotation Survival:** Track the proportion of top-decile volume migrating to newly initialized zero-history wallets over time. **Failure rule:** If $> 50\%$ of informed volume shifts to unranked addresses within 72 hours of identification, static 10-day wallet scoring is invalid.

## Crypto portability

**direct**

The mechanism relies fundamentally on the open, persistent pseudonymous wallet architecture native to decentralized cryptocurrency limit order book exchanges (such as Hyperliquid, dYdX, and Solana DEXs).
- **Public Ledger Visibility:** Unlike traditional equity and futures exchanges where broker IDs are masked or cleared anonymously through DTCC/CME, on-chain and sovereign-rollup DEXs broadcast cryptographic signatures and wallet addresses in cleartext.
- **Cross-Venue Invariance:** The signal is directly portable across any transparent L3/L4 DEX architecture, but not directly portable to anonymous centralized exchanges (Binance/Coinbase) unless exchange-level trader IDs are leaked or exposed via VIP program telemetry.

## Limitations

- **Exchange Specificity:** Dependent entirely on DEXs that publish full L4/order-lifecycle messages with persistent wallet identifiers.
- **Adversarial Adaptation:** High susceptibility to address recycling / Sybil generation by informed institutional market participants.
- **High-Frequency Infrastructure Requirement:** Requires real-time L4 state reconstruction engines capable of processing billions of messages per month.

## Implementation status

No implementation in our research stack. The underlying source paper (Zhai, August 2026) provides empirical findings from Hyperliquid production telemetry; no automated live or paper trading execution pipeline has been deployed.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[quant/hyperliquid-sunshine-trading-adverse-selection-liquidity-extraction-2026-09-01]] — Sunshine trading vs. hidden TWAP adverse selection on Hyperliquid
- [[quant/crypto-multilevel-order-flow-imbalance-intraday-2026-08-31]] — Order flow imbalance modeling without identity features
- [[quant/crypto-perpetual-lob-explainable-catboost-gmadl-microstructure-2026-09-01]] — Machine learning models on limit order book microstructure features

## Sources

1. Daojing Zhai, "Public Trader Identity: Adverse Selection and Return Predictability", arXiv:2608.04373v1 [q-fin.TR, q-fin.PR], August 2026. URL: https://arxiv.org/abs/2608.04373.
