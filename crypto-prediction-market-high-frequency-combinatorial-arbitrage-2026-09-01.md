---
schema: strategy-research-record-v1
title: Decentralized Prediction Market High-Frequency Combinatorial Arbitrage and Retail Liquidity Bottlenecks
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - prediction-markets
  - polymarket
  - clob
  - market-microstructure
  - combinatorial-arbitrage
  - limits-to-arbitrage
  - polygon
  - high-frequency-trading
status: research-only
confidence: high
source_as_of: 2026-04
sources:
  - "Cheng, G., Yang, J., & Zou, H. (2026). Arbitrage Analysis in Polymarket NBA Markets. arXiv preprint arXiv:2605.00864v1 [q-fin.TR]. https://arxiv.org/abs/2605.00864"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Decentralized Prediction Market High-Frequency Combinatorial Arbitrage and Retail Liquidity Bottlenecks

## Provenance

- **Primary Source:** Guang Cheng, Jiaxin Yang, and Haoxuan Zou (University of California, Los Angeles), *"Arbitrage Analysis in Polymarket NBA Markets"*, arXiv preprint `arXiv:2605.00864v1 [q-fin.TR]`, submitted April 22, 2026. URL: https://arxiv.org/abs/2605.00864, DOI: https://doi.org/10.48550/arXiv.2605.00864.
- **Foundational & Contextual Literature:**
  - Saguillo, O., Ghafouri, V., Kiffer, L., & Suarez-Tangil, G. (2025). "Unravelling the probabilistic forest: arbitrage in prediction markets." arXiv preprint `arXiv:2508.03474`.
  - Shleifer, A., & Vishny, R. W. (1997). "The Limits of Arbitrage." *Journal of Finance*, 52(1), 35–55. DOI: https://doi.org/10.1111/j.1540-6261.1997.tb03807.x.
  - Tsang, K. P., & Yang, Z. (2026). "The anatomy of Polymarket: evidence from the 2024 presidential election." Working Paper.
  - Ng, H., Peng, L., Tao, Y., & Zhou, D. (2025). "Price discovery and trading in prediction markets." SSRN Electronic Journal, SSRN 5331995.
- **Empirical Dataset:** Point-in-time Level 1 (top-of-book) Limit Order Book (LOB) snapshots sampled via the Polymarket Central Limit Order Book (CLOB) API on the Polygon blockchain across 173 NBA games (comprising 3,042 distinct markets and 75,088,497 LOB snapshots) between February 4, 2026, and March 4, 2026.
- **Public-Use Status:** Open-access academic publication / arXiv preprint distributed under the arXiv perpetual non-exclusive license.

## Economic mechanism

### Source-reported

In decentralized prediction platforms such as Polymarket, binary outcome tokens (ERC-1155) are fully collateralized by locked USDC ($1.00 per complementary Yes/No pair). Because outcomes are mutually exclusive and collectively exhaustive, market prices represent collective risk-neutral probabilities bounded between $0.00 and $1.00.

1. **Single-Market Inefficiency:**
   Within an isolated binary market (e.g., Moneyline for Team A vs. Team B), the combined cost of complementary tokens must sum to $1.00:
   - **Buy Path (Long Arbitrage):** $\text{Ask}_A + \text{Ask}_B < 1.00$ allows purchasing guaranteed $1.00 payout for $< \$1.00$.
   - **Mint-and-Sell Path (Short Arbitrage):** $\text{Bid}_A + \text{Bid}_B > 1.00$ allows locking $1.00 USDC to mint share pairs and immediately selling both for $> \$1.00$.

2. **Combinatorial Structural Dependency & Synthetic Shorting:**
   Multiple related markets trade concurrently for a single event (Moneyline, Spreads, Over/Under totals). Let final point differential be $\Delta = S_A - S_B$. Because basketball games cannot end in a tie ($\Delta \in \mathbb{Z} \setminus \{0\}$), the Spread contract $Sp_A$ (requiring $\Delta > h$ with handicap $h \ge 1$) is a strict mathematical subset of the Moneyline contract $ML_A$ (requiring $\Delta \ge 1$):
   $$\{\Delta > h\} \subset \{\Delta \ge 1\} \implies P(Sp_A) \le P(ML_A)$$
   Because Polymarket lacks direct uncollateralized short selling, an overpriced spread ($\text{Bid}(Sp_A) > \text{Ask}(ML_A)$) is monetized by constructing a **synthetic short**: buying the complementary underdog spread token $Sp_B$ ($\Delta < h$). A risk-free combinatorial arbitrage exists whenever:
   $$\text{Ask}(ML_A) + \text{Ask}(Sp_B) < 1.00$$

3. **The "Middle" Jackpot Asymmetry:**
   If the terminal point differential lands precisely within the handicap gap ($1 \le \Delta < h$, e.g., $\Delta = 1$ for a $+1.5$ spread), both $ML_A$ and $Sp_B$ resolve to Yes, yielding a double payout of $2.00 on a sub-$1.00 cost basis.

4. **Limits to Arbitrage & Liquidity Bottleneck:**
   While combinatorial pricing dislocations occur frequently during live play, shallow order book depth acts as a binding capital friction (Shleifer & Vishny, 1997). The available resting liquidity at top-of-book is rapidly exhausted, restricting risk-free extraction strictly to retail size ($< \$15$ per episode).

### Research interpretation

The alpha hypothesis is **High-Frequency In-Game Combinatorial Prediction Market Arbitrage**:
1. Live-game scoring runs induce asynchronous probability updates across isolated order books, temporarily breaking the subset monotonicity condition between Moneyline and Spread books.
2. Low-latency bots can exploit these dislocations by atomically buying $ML_A$ and $Sp_B$ via off-chain CLOB matching whenever combined ask $< 0.990$ (capturing $\ge 100\text{ bps}$ risk-free margin).
3. The theoretical "Middle" double-payout jackpot should be priced as a zero-value lottery ticket ($0\%$ realization probability in practice) rather than relied upon for expected return.
4. Capital deployment must be throttled to small, distributed execution tickets ($\le \$15$ per leg) to avoid crossing wider spreads and suffering catastrophic adverse selection.

## Signal

The normalized quantitative rules for the high-frequency combinatorial arbitrage engine operate as follows:

1. **Order Book Ingestion & Desynchronization Filter:**
   - Stream top-of-book quotes for Moneyline ($\text{Ask}(ML_A), \text{Bid}(ML_A)$) and Point Spread ($\text{Ask}(Sp_B), \text{Bid}(Sp_B)$) contracts via Polymarket CLOB WebSocket / REST API (`GET /book`).
   - Apply a dynamic 500 ms time-clustering window to algorithmically synchronize API responses and filter out 2–50 ms serialization timestamp lag artifacts.

2. **Phase Filter:**
   - Active only during **Live In-Game Phase** (from tip-off timestamp $T_{\text{start}}$ to final whistle $T_{\text{end}}$).
   - Reject all signals during **Post-Game Phase** (where median spreads explode to $> 7{,}500\text{ bps}$ due to market-maker quote withdrawal prior to oracle settlement).

3. **Entry Trigger & Execution Rules:**
   - Evaluate synthetic cost condition at discrete timestamp $t$:
     $$C_{\text{combo}}(t) = \text{Ask}(ML_A, t) + \text{Ask}(Sp_B, t)$$
   - Check risk-free yield threshold:
     $$\text{Yield}(t) = 1.00 - C_{\text{combo}}(t) \ge \theta_{\text{min}}, \quad \text{with } \theta_{\text{min}} = 0.0050 \text{ (50 bps)}$$
   - Check available executable liquidity depth:
     $$Q_{\text{avail}}(t) = \min \left( \text{Depth}(\text{Ask}(ML_A)), \text{Depth}(\text{Ask}(Sp_B)) \right) \ge \$10.00 \text{ USDC}$$
   - If conditions hold, execute immediate dual-leg taker market order (IOC) sized at:
     $$Q_{\text{order}} = \min \left( Q_{\text{avail}}(t), \$100.00 \right)$$

4. **Exit / Settlement:**
   - Hold paired positions until smart contract oracle resolution on Polygon ($1.00 payout guaranteed for any terminal outcome).
   - If $\Delta \in [1, h)$, collect $2.00 jackpot settlement.

## Required data

- **Venues & Market Type:** Polymarket CLOB (Polygon Layer-2); binary prediction event contracts across sports (NBA Moneyline, Spread $+1.5$ to $+15.5$, Totals).
- **Fields:** Top-of-book (Level 1) Best Bid price, Best Ask price, Bid Size, Ask Size, server update timestamp, orderbook cryptographic state hash.
- **Timeframe & Cadence:** Continuous high-frequency LOB snapshots (sub-second WebSocket feed or $< 5\text{ s}$ polling loop).
- **Point-in-Time Integrity:** Strict exclusion of post-game states; forward-fill state reconstruction with zero future look-ahead.

## Execution assumptions

- **Order Types & Latency:** Off-chain matching engine IOC (Immediate-Or-Cancel) limit/market orders; execution latency $< 200\text{ ms}$ (network round-trip ~171 ms).
- **Fees & Friction:** Zero trading fees on Polymarket CLOB matching; zero gas costs for off-chain order submission; gas costs incurred only upon batch USDC minting/redeeming on Polygon.
- **Execution Bottleneck:** Strictly constrained by Level 1 book depth; walking deeper into the book is prohibited due to high cancellation rates and severe illiquidity ($> 1{,}000\text{ bps}$ spread).

## Evidence

### Source-reported

Cheng, Yang, & Zou (2026) report empirical results across 75,088,497 LOB snapshots from 173 NBA games (Feb 4 – Mar 4, 2026):

1. **Single-Market Arbitrage Efficiency:**
   - Across 3,042 markets, only **7 valid in-game episodes** were detected (time-in-arbitrage: $0.0001\%$).
   - Median episode duration was **3.614 seconds**, aligning with the mechanical API polling cycle.
   - Aggregate profit capped at $100 per episode was **$210.19** (uncapped theoretical profit: $4,418.44), with a median yield of **11.0%** ($11.01 per episode).
   - Spread markets generated $194.08 capped profit (3 episodes) compared to $5.10 for Moneyline (3 episodes), showing deeper liquidity vacuums in spread markets.

2. **Combinatorial Arbitrage Frequency & Dynamics:**
   - Across 8.59 million evaluated combinatorial states, **290 active, executable episodes** occurred after excluding 233 post-game stale artifacts.
   - 96.2% of episodes (279) occurred during live in-game play, heavily concentrated in the final minutes of the 4th quarter as terminal probabilities underwent abrupt repricing.
   - Median episode duration was **16.0 seconds** (17.2% lasted $\le 4.0\text{ s}$).

3. **Profitability & The Limits-to-Arbitrage Ceiling:**
   - Combinatorial execution delivered a median yield of **101.01 basis points** ($1.01\%$ per trade).
   - Aggregate profit under a $100 budget cap was **$559.59** (uncapped theoretical profit: $2,032.75).
   - **Severe Liquidity Bottleneck:** In **76.9% of all episodes**, the $100 budget could not be filled; average executable size was restricted to just **14.79 synthetic shares (~$14.80)**.
   - **Zero "Middle" Jackpot Realization:** In $100\%$ of the 290 candidate episodes, the final outcome resolved to the baseline $1.00 payout; the theoretical $2.00 jackpot had **0 empirical occurrences** ($0.0\%$).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Post-Game Spread Blowout:** 81.1% of raw single-market signals and 44.5% of raw combinatorial signals occurred post-game, where median spreads exploded to $7{,}532.65\text{ bps}$ due to market-maker quote cancellation. Trading these phantom signals resulted in immediate execution failure.
- **Non-Scalability:** Capital capacity is severely bounded; deploying institutional capital ($> \$1{,}000$) immediately exhausts top-of-book depth and pushes execution into deeply negative territory.

## Falsification plan

The hypothesis that prediction market combinatorial mispricing yields systematic risk-free alpha will be falsified if:
1. **Execution Lag & Slippage Loss:** Real-world API execution against the CLOB suffers from fill latency $> 500\text{ ms}$, resulting in partial-fill execution (one leg fills while the other cancels) that creates unhedged directional losses exceeding gross arbitrage gains.
2. **Oracle Settlement Risk:** Ambiguous event resolution or dispute delays on Polygon lock collateral for $> 30\text{ days}$, eroding the annualized return below the risk-free USDC lending rate.
3. **Market Maker Synchronization:** Polymarket introduces unified cross-market margin engines or automated liquidity linking, reducing the occurrence of live combinatorial dislocations to $< 5\text{ episodes per 100 games}$.
4. **Placebo State Shuffle:** Randomly pairing uncorrelated event contracts produces identical combinatorial yield distributions, demonstrating that the observed returns stem from random bid-ask noise rather than structural subset mispricing.

## Crypto portability

**Direct**: The mechanism and empirical findings are derived natively from decentralized prediction market infrastructure on the Polygon blockchain (Polymarket CLOB ERC-1155 tokens).

Portability considerations:
- Direct applicability to emerging decentralized prediction platforms (Polymarket, Azuro, Drift BET, SX Network).
- Cross-application to traditional sports betting exchanges (Betfair) and centralized prediction venues (Kalshi, PredictIt), subject to regulatory and commission adjustments.

## Limitations

- **not independently reproduced**;
- **1-month sample window:** empirical data covers 173 NBA games over February–March 2026; generalizability to non-sports contracts (political, macro, crypto events) with longer holding durations remains unproven;
- **polling latency lower bound:** 3.6–5.5 second polling cycles may miss sub-second flash arbitrages captured by co-located searchers;
- **capital capacity:** strictly confined to retail ticket sizes ($\le \$15$–$100$).

## Implementation status

not-implemented

No implementation in PyBroker, NautilusTrader, or internal live trading pipelines has been completed.

## Adoption boundary

research-only

This record is research material only. It does not constitute investment advice, a validated trading strategy, or authorization for Paper, Testnet, or Live execution.

## Related Wiki records

- [[quant/crypto-short-horizon-prediction-market-settlement-push-reversal-2026-09-01]] — prediction market settlement dynamics.
- [[quant/crypto-cross-platform-binary-threshold-mispricing-polymarket-binance-2026-09-01]] — cross-platform prediction market pricing.
- [[quant/crypto-kalshi-prediction-market-macro-repricing-volatility-forecasting-2026-09-01]] — prediction market macro volatility forecasting.

## Sources

1. Cheng, G., Yang, J., & Zou, H. (2026). "Arbitrage Analysis in Polymarket NBA Markets." *arXiv preprint arXiv:2605.00864v1 [q-fin.TR]*, submitted 22 April 2026. URL: https://arxiv.org/abs/2605.00864. DOI: https://doi.org/10.48550/arXiv.2605.00864.
2. Saguillo, O., Ghafouri, V., Kiffer, L., & Suarez-Tangil, G. (2025). "Unravelling the probabilistic forest: arbitrage in prediction markets." *arXiv preprint arXiv:2508.03474*. URL: https://arxiv.org/abs/2508.03474.
3. Shleifer, A., & Vishny, R. W. (1997). "The Limits of Arbitrage." *Journal of Finance*, 52(1), 35–55. DOI: https://doi.org/10.1111/j.1540-6261.1997.tb03807.x.
4. Tsang, K. P., & Yang, Z. (2026). "The anatomy of Polymarket: evidence from the 2024 presidential election." Working Paper.
5. Ng, H., Peng, L., Tao, Y., & Zhou, D. (2025). "Price discovery and trading in prediction markets." *SSRN Electronic Journal*, SSRN 5331995. DOI: https://dx.doi.org/10.2139/ssrn.5331995.
