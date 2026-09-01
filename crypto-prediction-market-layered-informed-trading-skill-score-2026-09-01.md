---
schema: strategy-research-record-v1
title: Layered Informed Trading Surveillance: Event-Level Sign-Randomization Skill Decomposition and Information Front-Loading in Decentralized Prediction Markets
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - prediction-markets
  - polymarket
  - informed-trading
  - sign-randomization
  - information-leakage
  - order-flow
  - market-microstructure
status: research-only
confidence: high
source_as_of: 2026-05
sources:
  - "Maksym Nechepurenko, 'Per-Market Information Leakage and Order-Flow Skill: Two Methodological Lenses on Informed Trading in Decentralized Prediction Markets', arXiv:2605.02287v2 [q-fin.TR, cs.CY], May 2026. DOI: 10.48550/arXiv.2605.02287. https://arxiv.org/abs/2605.02287"
  - "Mark Gomez-Cram, Vyacheslav Gorbenko, and Bryan T. Kelly, 'Who Knows What, and When? Information and Skill in Prediction Markets', SSRN Working Paper 5227845, April 2026. https://ssrn.com/abstract=5227845"
  - "Ian Mitts and Justin Ofir, 'Anomalous Profits and Informed Trading in Decentralized Prediction Markets', Columbia Law & Economics Working Paper, April 2026"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Layered Informed Trading Surveillance: Event-Level Sign-Randomization Skill Decomposition and Information Front-Loading in Decentralized Prediction Markets

## Provenance

- **Primary Source:** Maksym Nechepurenko (ForesightFlow / Quantitative Microstructure), "Per-Market Information Leakage and Order-Flow Skill: Two Methodological Lenses on Informed Trading in Decentralized Prediction Markets", arXiv:2605.02287v2 [q-fin.TR, cs.CY], May 2026. DOI: [10.48550/arXiv.2605.02287](https://doi.org/10.48550/arXiv.2605.02287). Full text: [https://arxiv.org/html/2605.02287v2](https://arxiv.org/html/2605.02287v2).
- **Core Constituent Methodologies Synthesized:**
  1. **Event-Level Sign-Randomization Skill Classifier & Lifecycle Heuristic:** Mark Gomez-Cram, Vyacheslav Gorbenko, and Bryan T. Kelly (Yale SOM / Chicago Booth / AQR), "Who Knows What, and When? Information and Skill in Prediction Markets", SSRN Working Paper 5227845, April 2026. Evaluated on the complete transaction history of Polymarket covering 1.72 million accounts, 210,322 markets, and $13.76 billion in trading volume across 2023–2025.
  2. **Composite Anomalous Profit Screen:** Ian Mitts and Justin Ofir (Columbia Law School), "Anomalous Profits and Informed Trading in Decentralized Prediction Markets", April 2026. Evaluated on >210,000 wallet-market pairs, documenting $143 million in aggregate anomalous profit.
  3. **Information Leakage Score (ILS / ILSdl):** Maksym Nechepurenko, "Information Leakage Score in Binary Prediction Markets", ForesightFlow Preprint, April 2026; empirical validation on the 2026 U.S.–Iran conflict cluster ($832M volume).
- **External Ground-Truth Benchmark:** U.S. Department of Justice (DOJ) / CFTC federal indictment of Master Sergeant Gannon Van Dyke (April 23, 2026; unsealed criminal indictment for trading on classified Operation Absolute Resolve intelligence, realizing $409,881 across 13 Polymarket trades).

## Economic mechanism

### Source-reported

1. **Three Orthogonal Methodological Layers:** Informed trading detection in decentralized prediction markets cannot be solved by a single metric. The literature demonstrates three structurally distinct layers:
   - **Layer 1 (Multi-Event Skill vs. Luck):** Event-level sign-randomization testing across accounts with $\ge 10$ events. Classifies 3.14% (54,477 accounts) as "skilled winners" who capture >30% of total platform profits and demonstrate 44% out-of-sample skill persistence (vs. ~10% for equity fund managers).
   - **Layer 2 (Single-Event Lifecycle & Conviction):** Heuristic screening of one-shot informed accounts (new wallet creation within 48h, high capital concentration, single-event trading, post-resolution dormancy; flags 1,950 accounts).
   - **Layer 3 (Per-Market Information Front-Loading):** Information Leakage Score ($ILS_{dl}$) measuring the fraction of terminal price discovery priced into a specific contract prior to the article-derived public event timestamp $T_{\text{event}}$.
2. **Category Heterogeneity:** Platform-wide pooling obscures mechanism: sports markets reflect algorithmic / statistical modeling skill; political/macro markets reflect private information leakage; crypto threshold markets reflect cross-venue options mispricing.

### Research interpretation

The falsifiable thesis is an **informed order-flow decomposition and adverse selection avoidance mechanism**:
1. **Directional Alpha from Skilled Order Flow:** Order flow from the top 3.14% sign-randomization "skilled winner" cohort contains persistent predictive alpha for both next-period price drift and terminal contract resolution.
2. **Adverse Selection Filter for Liquidity Providers:** Prediction market automated market makers and limit order providers who fade or widen spreads against flagged Layer 2 lifecycle wallets avoid toxic one-shot insider execution, significantly reducing LP drawdown.
3. **Cross-Layer Pipeline Alpha:** Combining Stage 1 category-conditioned account scoring with Stage 2 per-market $ILS_{dl}$ front-loading identifies genuine informed positioning while rejecting sports-betting statistical noise and market-maker inventory rebalancing.

## Signal

### 1. Sign-Randomization Skill Classifier ($S_i$)

- **Population Filter:** Wallets $i$ with trading activity across $K_i \ge 10$ distinct events.
- **Observed Metric:** Total realized profit $\Pi_i = \sum_{k=1}^{K_i} \pi_{i,k}$.
- **Null Distribution Generation:** For each wallet $i$, perform $B = 10{,}000$ Monte Carlo simulations where trade sign $s_{i,k} \in \{-1, +1\}$ is randomized at the event level ($p = 0.5$):
  $$\Pi_i^{(b)} = \sum_{k=1}^{K_i} s_{i,k}^{(b)} \cdot |\pi_{i,k}|, \quad b \in \{1, \dots, B\}$$
- **Statistical Significance ($p$-value):**
  $$p_i = \frac{1}{B} \sum_{b=1}^B \mathbf{1}_{\{\Pi_i^{(b)} \ge \Pi_i\}}$$
- **Classification:** Wallet $i$ is classified as a "Skilled Winner" if $p_i < 0.01$ (one-tailed 99% confidence).

### 2. Single-Event Lifecycle-and-Conviction Heuristic ($H_{\text{insider}}$)

Wallet $j$ trading event $E$ is flagged as a suspected one-shot informed trader if all four conditions hold:
1. **Account Recency:** $\text{Age}_j = t_{\text{first\_trade}} - t_{\text{wallet\_creation}} < 48\text{ hours}$.
2. **Single-Event Concentration:** $\frac{\text{Volume}_{j, E}}{\sum_e \text{Volume}_{j, e}} > 0.80$.
3. **High Relative Conviction:** $\text{PositionSize}_{j, E} > \text{Quantile}_{95}(\text{Market Trade Sizes})$.
4. **Post-Event Dormancy:** Zero transaction activity for $\tau_{\text{post}} \ge 14\text{ days}$ following contract settlement.

### 3. Deadline Information Leakage Score ($ILS_{dl}$)

For a binary contract with opening price $P_0$, price at article-derived public event timestamp $P(T_{\text{event}})$, and terminal resolution payout $P_{\text{res}} \in \{0, 1\}$:
$$ILS_{dl} = \frac{P(T_{\text{event}}) - P_0}{P_{\text{res}} - P_0}$$
- **Operational Scope Conditions:**
  1. $P_{\text{res}} \neq P_0$ (non-zero terminal information movement).
  2. $T_{\text{event}}$ identified via external, time-stamped public news arrival.
  3. Stable pre-event liquidity depth (minimum $10{,}000 USDC open interest).

### 4. Combined Alpha / Surveillance Signal

$$\text{InformedSignal}_{E, t} = \sum_{i \in \text{Skilled}} w_i \cdot \text{Sign}_{i, E, t} + \gamma \cdot \mathbf{1}_{\{\exists j \in H_{\text{insider}} \text{ active in } E\}}$$
where $w_i = 1 - p_i$ is the skill-confidence weight.

## Required data

- **On-Chain Prediction Market Data:**
  - Polymarket Conditional Tokens Framework (CTF) and NegRisk contract transaction logs via Polygon RPC / Goldsky indexer.
  - Wallet addresses, block timestamps, USDC gross volumes, token outcome IDs (YES/NO).
- **Order Book Microstructure Data:**
  - Polymarket CLOB REST/WebSocket L2 book snapshots, bid-ask quotes, trade aggressor flags.
- **External Event Timestamps ($T_{\text{event}}$):**
  - High-precision timestamped news feeds (GDELT, Bloomberg Terminal, Reuters wire) for geopolitical, economic, and corporate event definitions.

## Execution assumptions

- **Venue:** Polymarket CLOB / AMM on Polygon PoS.
- **Transaction Costs:** Polygon gas fees ($< \$0.01$ per transaction); Polymarket CLOB maker fee 0%, taker fee 0% (standard) / dynamic fee tiers on crypto series.
- **Slippage & Depth:** Execution capped at 5% of top-of-book depth to prevent market impact in illiquid political markets.

## Evidence

### Source-reported

- **Skill Persistence & Concentration (Gomez-Cram et al., 2026):**
  - Analyzed 1.72M accounts across $13.76B volume.
  - 3.14% (54,477 accounts) classified as skilled winners.
  - Skilled winners + market makers capture >30% of total platform PnL.
  - 44% of skilled accounts maintain their classification out-of-sample on randomly held-out test splits.
  - Lifecycle heuristic flagged 1,950 accounts as single-event insiders.
- **Anomalous Profit Scale (Mitts & Ofir, 2026):**
  - Identified $143M anomalous profit across 210,000 wallet-market pairs using multi-factor composite screening.
- **Empirical Ground-Truth Alignment (DOJ Indictment & Nechepurenko, 2026):**
  - On the January 2026 Venezuela / Maduro cluster, the Gomez-Cram lifecycle heuristic flagged three accounts whose realized PnL matched the DOJ Master Sergeant Gannon Van Dyke indictment ($409,881) to the dollar on the lead account.

### Independently reproduced

- `not independently reproduced`.

### Negative evidence

- **Category-Pooling Confound:** Pooling sports, crypto, and political markets without conditioning leads to severe false positives. High-frequency sports market-making strategies achieve significant sign-randomization $p$-values purely through latency/rebate capture without possessing fundamental private information.
- **Denominator Instability in $ILS_{dl}$:** When $P_0 \approx P_{\text{res}}$ (market opens near terminal outcome), $ILS_{dl}$ suffers from denominator explosion and yields noisy, over-unity values requiring explicit truncation.

## Falsification plan

1. **Out-of-Sample Skilled Order Flow Tracking:**
   - **Sample:** Polymarket out-of-sample test window (May 2026 – December 2026).
   - **Strategy:** Replicate directional trades of the top 3.14% skilled cohort on binary political/macro markets within 60 seconds of order execution.
   - **Metric:** Brier score improvement relative to market consensus price, and net trade PnL after 25 bps slippage.
   - **Falsification Threshold:** If the replicated portfolio achieves negative net PnL (Sharpe $< 0.0$) or directional accuracy does not beat the contemporaneous market mid-price ($p > 0.10$), reject the skilled order-flow alpha thesis.
2. **Category Ablation:** Compare alpha persistence when trained purely on politics vs. sports vs. crypto sub-universes.

## Crypto portability

- **Portability:** `direct`.
- **Crypto-Specific Alignment:** Directly engineered for blockchain-based decentralized prediction markets (Polymarket on Polygon), on-chain wallet tracking, and CTF smart contract accounting.

## Limitations

- **Anonymous Sybil / Multi-Wallet Fragmentation:** Sophisticated informed traders can split trades across dozens of freshly funded wallets, evading single-wallet conviction thresholds.
- **Execution Slippage in Thin Markets:** Many long-tail prediction contracts possess $<\$5{,}000$ in order book liquidity, severely limiting strategy capacity.

## Implementation status

- `not-implemented` in our production quant stack.
- Research capture only; no PyBroker or Nautilus execution files created.

## Adoption boundary

- `research-only`, `not-approved`.
- This record provides a theoretical and empirical foundation for prediction market order-flow surveillance and microstructural alpha research. It does not authorize live or paper trading.

## Related Wiki records

- `[[quant/crypto-short-horizon-prediction-market-settlement-push-reversal-2026-09-01]]`
- `[[quant/crypto-cross-platform-binary-threshold-mispricing-polymarket-binance-2026-09-01]]`
- `[[quant/prediction-market-optimal-market-making-latent-belief-hjb-2026-09-01]]`

## Sources

- Maksym Nechepurenko, "Per-Market Information Leakage and Order-Flow Skill: Two Methodological Lenses on Informed Trading in Decentralized Prediction Markets", arXiv:2605.02287v2 [q-fin.TR, cs.CY], May 2026. DOI: [10.48550/arXiv.2605.02287](https://doi.org/10.48550/arXiv.2605.02287). https://arxiv.org/abs/2605.02287.
- Mark Gomez-Cram, Vyacheslav Gorbenko, and Bryan T. Kelly, "Who Knows What, and When? Information and Skill in Prediction Markets", SSRN Working Paper 5227845, April 2026. https://ssrn.com/abstract=5227845.
- Ian Mitts and Justin Ofir, "Anomalous Profits and Informed Trading in Decentralized Prediction Markets", Columbia Law & Economics Working Paper, April 2026.
- U.S. Department of Justice, "U.S. Army Master Sergeant Indicted for Insider Trading in Decentralized Prediction Markets", Press Release, April 23, 2026.
