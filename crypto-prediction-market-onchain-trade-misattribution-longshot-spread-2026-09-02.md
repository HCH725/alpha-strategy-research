---
schema: strategy-research-record-v1
title: "Decentralized Prediction Market Microstructure: Trade Direction Misattribution and Longshot Spread Premium"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - prediction-markets
  - polymarket
  - market-microstructure
  - trade-classification
  - longshot-bias
  - bid-ask-spread
  - order-flow-imbalance
status: research-only
confidence: medium
source_as_of: 2026-05-01
sources:
  - "Philipp D. Dubach, 'The Anatomy of a Decentralized Prediction Market: Microstructure Evidence from the Polymarket Order Book', arXiv:2604.24366v2 [q-fin.TR], May 2026. https://arxiv.org/abs/2604.24366"
  - "Philipp D. Dubach, 'polymarket-microstructure' GitHub replication repository. https://github.com/philippdubach/polymarket-microstructure"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Decentralized Prediction Market Microstructure: Trade Direction Misattribution and Longshot Spread Premium

## Provenance

- **Paper URL:** https://arxiv.org/abs/2604.24366
- **Full arXiv ID:** arXiv:2604.24366v2 [q-fin.TR]
- **Author:** Philipp D. Dubach (University of Zurich / ETH Zurich)
- **Submitted / Revised:** April 27, 2026 / May 2026
- **Replication Package:** https://github.com/philippdubach/polymarket-microstructure (Zenodo DOI: `10.5281/zenodo.19811426`)
- **Empirical Dataset:** Pre-registered stratified panel of 600 Polymarket binary prediction markets over a 52-day continuous observation window. Continuous tick-level archive of 30 billion public order-book events merged with Polygon on-chain ground truth `OrderFilled` contract logs.

## Economic mechanism

### Source-reported

Decentralized prediction markets (such as Polymarket) differ structurally from continuous double auctions on traditional equity or centralized crypto futures venues. The author establishes eight empirical stylized facts (SF1–SF8) governing decentralized prediction market microstructure:

1. **Trade Classification Breakdown (Off-Chain vs. On-Chain Divergence):** Standard trade-direction classification algorithms (such as the Lee-Ready tick test) applied to the public off-chain WebSocket order-book feed achieve only **~59% agreement (panel mean 61.5%)** with the true on-chain `OrderFilled` settlement ground truth. This is dramatically inferior to the ~80% accuracy observed in equity markets (e.g., Nasdaq), driven by off-chain message drops, batch execution on Polygon, and latency asymmetries between off-chain matching engines and on-chain state finality.
2. **SF1: Longshot Spread Premium:** Effective and quoted bid-ask spreads widen drastically in extreme probability tails (probabilities $p < 0.10$ or $p > 0.90$), reaching **1,300 to 1,800 basis points** compared to 200–400 bps in central probability regions ($0.40 \le p \le 0.60$).
3. **SF2: Geometric/Uniform Depth Profile:** Unlike traditional equities where depth is heavily concentrated at the best bid and offer (Level 1), prediction market depth is distributed uniformly or geometrically across outer price ticks.
4. **SF4 & SF7: Maker Concentration and Low Wash Trading:** Polymarket demonstrates wide maker-wallet diversity with a concentrated institutional tail; self-counterparty wash trading is observed at a median of **1.0%** (with a 95th percentile upper tail of 22.0%), significantly lower than figures historically reported on unregulated centralized crypto spot venues.
5. **SF8: Depth Decay Near Resolution:** Depth decay is driven predominantly by price level and cumulative volume rather than purely calendar time-to-close.

### Research interpretation

These findings enable two concrete systematic trading and market-making strategies:
1. **On-Chain Ground-Truth Order Flow Imbalance Arbitrage (Offensive Alpha):**
   - Because public WebSocket feed consumers experience a ~41% misattribution rate in trade direction, naive off-chain market makers quote stale or mispriced levels based on phantom order flow.
   - A latency-optimized market participant listening directly to Polygon mempool / on-chain `OrderFilled` events reconstructs true directional signed order flow imbalance ($OFI_{\text{onchain}}$) and trades against stale off-chain quotes before public market data feeds reflect the true taker direction.
2. **Skew-Aware Longshot Liquidity Provision (Market Making Alpha):**
   - The structural **1,300–1,800 bps spread premium** in longshot contracts ($p < 0.10$) represents an overcompensation for inventory holding costs when conditioned on non-imminent settlement.
   - By quoting wide passive bid-ask brackets on longshot contracts while hedging net binary delta across complementary outcome tokens, a systematic market maker captures elevated spread premiums while avoiding toxic event-resolution sweeps.

## Signal

### Signal A: On-Chain Ground-Truth OFI Lead-Lag Divergence
- **Observation Frequency:** Sub-second Polygon event blocks (median block interval ~2.0s).
- **True On-Chain Flow:**
  $$OFI_{\text{onchain}, t} = \sum_{k \in \text{OrderFilled}_{(t-\Delta t, t)}} \text{Sign}_k \cdot \text{Amount}_k$$
- **Off-Chain Naive Flow:**
  $$OFI_{\text{offchain}, t} = \sum_{j \in \text{WS\_Trades}_{(t-\Delta t, t)}} \text{Sign}_{\text{LeeReady}}(j) \cdot \text{Amount}_j$$
- **Divergence Discrepancy Metric:**
  $$\Delta OFI_t = OFI_{\text{onchain}, t} - OFI_{\text{offchain}, t}$$
- **Entry Logic:**
  - Long Entry: When $\Delta OFI_t > +\theta_{\text{flow}}$ (indicating heavy on-chain buyer taker flow misclassified or dropped by off-chain feeds), enter aggressive limit buy at off-chain ask before off-chain book updates.
  - Short Entry: Symmetric for $\Delta OFI_t < -\theta_{\text{flow}}$.
- **Exit:** Immediate mean reversion exit upon off-chain midprice adjustment (holding period 1 to 10 seconds).

### Signal B: Longshot Spread Capture with Skew Filter
- **Filter Condition:** Token implied probability $p_t \in (0.01, 0.09)$ or $p_t \in (0.91, 0.99)$ and market maturity $\tau > 72\text{ hours}$.
- **Spread Threshold:** Quoted spread $S_t \ge 1,200\text{ bps}$.
- **Quote Placement:** Post passive limit buy at Bid $+ 1\text{ tick}$ and limit sell at Ask $- 1\text{ tick}$.
- **Delta Neutralization:** Automatically mint/redeem complete outcome sets (Yes + No = $1.00 USDC) to lock in realized spread and neutralize event outcome risk.
- **Exit:** Inventory rebalancing when spread compresses below 400 bps or position held $> 6\text{ hours}$.

## Required data

- **Instrument:** Binary outcome tokens (ERC-1155 / CTF conditional tokens, e.g., Polymarket USDC outcome tokens).
- **Universe:** 600+ active Polymarket prediction markets across politics, macroeconomics, crypto milestones, and sports.
- **Venue:** Polymarket CTF Exchange on Polygon network and Central Limit Order Book (CLOB).
- **Timeframe:** Tick-by-tick order-book updates (WebSocket) and on-chain Polygon block event logs (`OrderFilled`, `OrdersMatched`).
- **Fields:**
  - On-chain event fields: `maker`, `taker`, `makerAssetId`, `takerAssetId`, `makerAmountFilled`, `takerAmountFilled`, `fee`.
  - Off-chain CLOB fields: Level-2 bids/asks, order IDs, price ticks, timestamp, side.
- **Point-in-time:** Block-indexed event logs; strictly causal ingestion without future block knowledge.

## Execution assumptions

- **Order Types:**
  - Lead-lag arbitrage: Aggressive IOC limit orders routed to Polymarket CLOB API.
  - Longshot MM: Passive post-only limit orders (`maker_only = True`).
- **Fill Model:** Immediate fill on passive levels if crossed; on-chain settlement gas fee modeled at standard Polygon gas prices (30–80 Gwei / ~$0.01–$0.05 per fill).
- **Fees:** 0.00% maker / taker fee on standard Polymarket CLOB; liquidity provider reward incentives (rebates) earned on qualifying markets.
- **Latency:** Sub-50ms connection to Polymarket CLOB matching engine; direct Polygon RPC node access (< 100ms) for event monitoring.

## Evidence

### Source-reported

- **Empirical Scope:** 600 pre-registered markets across 52 days, evaluating 30 billion order-book messages joined to Polygon on-chain transaction records.
- **Trade Classification Accuracy:** Public WebSocket feed trade direction agrees with on-chain ground truth only **58.7% to 59.2% of the time (panel mean 61.5%)**, demonstrating extreme fragility in applying standard equity/CEX tick tests.
- **Spread Premium:** Empirically documented longshot spread premium of **1,300 to 1,800 basis points** in contracts with $p < 0.10$, dropping to 200–400 bps in central contracts ($p \approx 0.50$).
- **Wash Share:** Self-counterparty wash trading identified at median **1.0%** (95th percentile upper tail 22.0%).
- **Replication Code:** Fully verifiable open-source pipeline published at `philippdubach/polymarket-microstructure` (DOI: 10.5281/zenodo.19811426).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Toxic Settlement Sniping:** Longshot contracts ($p < 0.10$) are vulnerable to catastrophic jump risk (sudden outcome resolution or headline news), where informed traders sweep the entire book, generating catastrophic tail losses that exceed cumulative spread profits.
- **Mempool Front-Running / MEV:** Public Polygon blockchain transactions are visible to searchers; on-chain lead-lag arbitrage can be front-run by MEV bots if orders are routed publicly rather than via private RPC or direct API endpoints.

## Falsification plan

1. **On-Chain vs. Off-Chain Information Edge Test:** Measure the 10-second price prediction accuracy ($R^2$ and AUC) of $OFI_{\text{onchain}}$ versus $OFI_{\text{offchain}}$ on out-of-sample Polymarket event series. **Failure rule:** If $OFI_{\text{onchain}}$ does not outperform $OFI_{\text{offchain}}$ by at least 5.0 percentage points in directional accuracy, the misattribution alpha thesis is falsified.
2. **Longshot Market Making Sharpe / Tail Risk Test:** Simulate delta-neutral quoting on contracts with $p \in (0.02, 0.08)$ across 100 resolved markets, incorporating real event-resolution jumps. **Failure rule:** If realized Sharpe ratio $< 1.0$ or maximum drawdown exceeds $25\%$, the longshot spread premium is insufficient to cover tail resolution risk.
3. **Fee and Gas Sensitivity:** Model strategy profitability across Polygon gas price spikes (up to 300 Gwei). **Failure rule:** If net PnL becomes negative at 100 Gwei, the operational micro-arbitrage is economically unviable.

## Crypto portability

**direct**

The mechanism and empirical phenomena are native to decentralized prediction markets and Polygon/EVM smart contract settlement architectures.
- **Unique Hybrid Microstructure:** The coexistence of an off-chain central limit order book matching engine with asynchronous on-chain batch settlement creates a market microstructure dynamic unique to Web3 prediction venues (Polymarket, SX Bet, Azuro).
- **Binary Outcome Structure:** Outcome payoffs bounded strictly in $[0, 1]$ USDC create mathematical spread and depth dynamics distinct from unbounded continuous asset pairs.

## Limitations

- **Platform Risk & Oracle Resolution:** Dependent on Polymarket and UMA Optimistic Oracle resolution integrity.
- **Market Liquidity Discrepancies:** While top presidential/macro markets have millions in daily volume, niche category markets have thin books with high inventory holding risk.
- **Off-Chain Feed Latency Tail:** WebSocket message latency exhibits multi-second tails during extreme traffic spikes.

## Implementation status

No implementation in our research stack. The underlying source (Dubach, May 2026) provides empirical analysis, replication datasets, and open-source data pipeline scripts; no systematic trading bot has been implemented.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[quant/crypto-prediction-market-layered-informed-trading-skill-score-2026-09-01]] — Informed trading and order-flow skill scores on prediction markets
- [[quant/crypto-prediction-market-high-frequency-combinatorial-arbitrage-2026-09-01]] — Combinatorial multi-outcome parity arbitrage
- [[quant/prediction-market-optimal-market-making-latent-belief-hjb-2026-09-01]] — Continuous-time stochastic control for prediction market making

## Sources

1. Philipp D. Dubach, "The Anatomy of a Decentralized Prediction Market: Microstructure Evidence from the Polymarket Order Book", arXiv:2604.24366v2 [q-fin.TR], May 2026. URL: https://arxiv.org/abs/2604.24366.
2. Philipp D. Dubach, "polymarket-microstructure" GitHub replication repository. URL: https://github.com/philippdubach/polymarket-microstructure. Zenodo DOI: 10.5281/zenodo.19811426.
