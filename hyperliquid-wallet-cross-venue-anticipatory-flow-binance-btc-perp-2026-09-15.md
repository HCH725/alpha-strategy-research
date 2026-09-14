---
schema: strategy-research-record-v1
title: "Lim — Wallet-level cross-venue anticipatory informed flow on Hyperliquid vs Binance BTC perps"
created: 2026-09-15
updated: 2026-09-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - microstructure
  - cross-venue
  - informed-trading
  - wallet-level
status: research-only
confidence: medium
source_as_of: "2026-07-05"
sources:
  - "https://doi.org/10.21203/rs.3.rs-10147582/v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Lim — Wallet-level cross-venue anticipatory informed flow on Hyperliquid vs Binance BTC perps

## Provenance

- **Author:** Boon Chuan Lim (Independent Researcher)
- **Title:** "Binance Leads, but Some Wallets Anticipate: Wallet-Level Cross-Venue Informed Flow in BTC Perpetual Futures"
- **Preprint server:** Research Square (not peer-reviewed; under revision)
- **DOI:** `10.21203/rs.3.rs-10147582/v1`
- **Version:** v1, posted 05 Jul 2026
- **Sample period:** 25 May 2026 – 22 June 2026 (29 days)
- **Instruments:** BTC perpetual futures on Binance (USDT-margined) and Hyperliquid (on-chain CLOB)
- **Data:** Public Binance USD-margined futures WebSocket market streams; Hyperliquid WebSocket subscriptions including buyer/seller wallet addresses. ~13.2 million Hyperliquid BTC trades within the analysis window (~0.48 million/day). Binance top-of-book at ~1 s spacing (mean 1.05 s; 95.5% coverage); Hyperliquid book at ~4 s spacing after cleaning.
- **Source URL:** https://doi.org/10.21203/rs.3.rs-10147582/v1
- **Repository deduplication audit:** Searched all `.md` records in `alpha-strategy-research` for `10147582`, `Boon Chuan Lim`, `wallet-level cross-venue`, `anticipatory wallet`, and `Binance leads some wallets anticipate`. Zero prior records cite this paper. The same author's Bitcoin ETF flow paper (SSRN 6592830) is captured in a separate record; this paper is materially distinct in mechanism (wallet-level cross-venue informed flow vs. ETF net-flow drift).

## Economic mechanism

### Source-reported

Binance dominates aggregate price discovery for BTC perpetual futures. However, Hyperliquid's on-chain transparency (wallet addresses visible on every trade) reveals that a persistent minority of wallets on Hyperliquid trades ahead of subsequent Binance mid-price movements. The aggregate informed cohort follows Binance on average, but the per-wallet distribution is wide, with ~24% of cohort wallets showing a lead tilt and ~9% satisfying a stricter clean-anticipator definition. Split-sample tests confirm this leadership persists out of sample: the strongest first-half lead-score quintile remains the only quintile with positive out-of-sample lead across all horizons.

The author interprets this as evidence that venue-level price-discovery analysis can mask trader-level heterogeneity: a venue that follows on average may still host wallets whose flow carries forward-looking information about the dominant venue's price.

### Research interpretation

The hypothesis is that on-chain wallet transparency on Hyperliquid creates an observable information asymmetry: a subset of traders execute on Hyperliquid before Binance moves. The mechanism could involve:

- **Cross-venue information processing:** Some traders process information faster or have lower-latency access to Binance order flow, allowing them to act on Hyperliquid before the information is fully incorporated into Binance prices.
- **Informed order flow:** Wallets with private information (e.g., knowledge of upcoming large Binance orders, OTC flows, or liquidation events) trade on Hyperliquid first.
- **Statistical arbitrage / cross-venue execution:** Traders who observe Binance order-book imbalances or flow patterns execute on Hyperliquid (where they have an on-chain identity) before the information propagates to Binance mid-price.

The alpha hypothesis is: **By identifying and following the anticipatory wallet cohort on Hyperliquid, a trader could capture the forward Binance price movement (~0.5–0.8 bps) as the information is incorporated into Binance mid-prices.**

## Signal

The signal is constructed as follows (research-proposed operationalization of the paper's findings):

1. **Wallet identification (formation period):** Rank Hyperliquid wallets by market-adjusted signed forward-return markout (gross mid-price). Select the top quintile (informed cohort).
2. **Direction mapping:** Observe the cohort's trade direction on Hyperliquid (aggressor side from trade messages).
3. **Entry:** When the informed cohort trades on Hyperliquid, take the same direction on Hyperliquid (or, research-proposed, on Binance ahead of the expected move).
4. **Exit / holding period:** The measured lead is at 2–10 second horizons. The paper does not specify an exit rule; the signal is a high-frequency market-state indicator, not a standalone trading strategy.
5. **Persistence check:** Only wallets in the top lead-score quintile from the first half of the sample are used for second-half trading (split-sample).

**Parameters:**
- Horizon: 2 s, 5 s, 10 s (paper tests all three)
- Cohort size: 658 wallets (top quintile of 3,294 persistent wallets)
- Clean-anticipator threshold: pre < 0.3 bps, post > 0.5 bps (research-defined falsification threshold)
- Split-sample: half-1 formation, half-2 evaluation

**Note:** The paper does not present this as a standalone trading strategy. It is a microstructure measurement study. The operationalization above is research-proposed.

## Required data

- **Instrument:** BTC perpetual futures (Binance USDT-margined + Hyperliquid on-chain)
- **Venue:** Binance (WebSocket market stream) + Hyperliquid (WebSocket subscriptions)
- **Market type:** Perpetual futures
- **Timeframe:** Event-time aligned at 5-second grid; raw data at ~1 s (Binance) and ~4 s (Hyperliquid)
- **Fields:** Top-of-book bid/ask (both venues); Hyperliquid trade messages with buyer/seller wallet addresses, aggressor direction, price, size, event timestamp
- **Timestamp:** Event timestamps (not receipt timestamps); Binance median receive-lag ~0 ms; Hyperliquid median ~479 ms
- **Point-in-time:** Trades and book updates are point-in-time. Wallet addresses are observable on-chain in real time.
- **Missing data:** Binance coverage begins 29 May 2026 (4.5% of seconds have gaps). Hyperliquid book updates are sparse (~4 s spacing).
- **Data gap:** The paper does not specify how wallet persistence (requiring >= 100 trades in each half) is defined in terms of minimum active days or trading frequency thresholds.

## Execution assumptions

- **Signal-to-order timing:** The paper measures cross-venue lead at 2–10 s horizons. Execution at these horizons requires sub-second latency and direct WebSocket feeds. research-proposed.
- **Order type:** Not specified. The paper uses mid-price markouts, not actual fills. research-proposed.
- **Fill model:** Not modeled. All markouts are gross mid-price, not realized fills. data gap.
- **Fees:** Not included. Binance taker fee ~5 bps; Hyperliquid maker/taker fees vary. data gap.
- **Slippage / spread:** Not included. The signal magnitudes (0.45–0.78 bps for the top quintile out of sample) are below typical round-trip costs. data gap.
- **Funding:** Not modeled. data gap.
- **Market impact:** Not modeled. data gap.
- **Latency:** Requires co-located or low-latency WebSocket connections to both venues. The measured lead is at 5 s grid resolution; sub-5 s leads cannot be resolved. data gap.
- **Capacity:** The anticipator effect is small in basis-point terms. At high turnover, the group-level persistence could be meaningful, but individual-wallet prediction is not reliable. data gap.

## Evidence

### Source-reported

All figures below are from Lim (2026), Research Square preprint `rs-10147582/v1`.

**Venue-level (Table 2):**
- Binance leads Hyperliquid in every event-time-aligned window.
- Peak cross-correlation: +0.497 to +0.732 at the Binance-leading grid point (5 s).
- Hasbrouck information share: Binance [55.5%, 100.0%] across four windows; Hyperliquid [0.0%, 44.5%].
- Rolling analysis: Of 580 non-overlapping 1-hour windows, Binance leads in 400 (69.0%), contemporaneous in 177 (30.5%), Hyperliquid leads in 3 (0.5%).

**Wallet-level informedness (Table 3):**
- Markout spread (p90 – p10): 1.85 → 6.05 bps at 10 s → 300 s.
- Half-1 vs half-2 Spearman correlation of informedness: +0.141, p < 0.001.

**Pooled cohort follows Binance (Table 4):**
- Cohort: 658 wallets, 2,337,051 trades.
- Binance move BEFORE cohort trade > AFTER at every horizon:
  - 2 s: +1.731 bps before, +0.604 bps after (diff: −1.127 bps, 95% CI [−1.198, −1.056])
  - 5 s: +2.043 bps before, +0.654 bps after (diff: −1.388 bps, 95% CI [−1.478, −1.301])
  - 10 s: +2.371 bps before, +0.720 bps after (diff: −1.651 bps, 95% CI [−1.760, −1.547])

**Per-wallet heterogeneity (Table 5):**
- 156 / 644 wallets (24%) show a lead tilt (post > pre, post > 0).
- 59 / 644 wallets (9%) satisfy clean-anticipator definition (pre < 0.3 bps, post > 0.5 bps).
- Lead-score range: −17.54 to +12.43 bps.

**Out-of-sample persistence (Table 6):**
- Spearman rho (half-1 vs half-2 lead): +0.477 (2 s), +0.548 (5 s), +0.532 (10 s).
- Q5 (top quintile) half-2 leads: +0.45 (2 s), +0.78 (5 s), +0.73 (10 s) bps.
- Half-1 anticipators: half-2 mean leads +0.70, +0.75, +0.79 bps; ~51–56% still leading in half 2.
- Non-anticipator benchmark: −1.04, −1.56, −2.21 bps.

**Robustness (Section 4.6):** Half-1-formed cohort tested on half-2 trades reproduces the follows-on-average pattern (pre > post at every horizon, n = 835,861). 23.2% of half-1 cohort wallets still anticipate in half 2.

**All markouts are gross mid-price markouts; they do not represent realised trading profits after fees, spread, funding, or inventory costs** (stated in Section 4.2).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The aggregate informed cohort follows Binance on average; the anticipatory signal is a minority effect within the cohort.
- The anticipator magnitudes are small (< 1 bps out of sample for the top quintile), raising the question of whether they survive realistic transaction costs.
- The paper notes that wallet addresses are not legal identities: one trader may control multiple wallets, and one wallet may represent multiple strategies.
- The sample is limited to one instrument (BTC) and one 29-day window. Results may differ for other assets, volatility regimes, or venue pairs.
- The clean-anticipator thresholds are fixed cut-offs designed for conservative classification, not structural estimates.

None identified as a formal falsification; the paper itself presents the limitations above.

## Falsification plan

1. **Cost sensitivity (research-defined):** If the top-quintile out-of-sample lead (~0.78 bps at 5 s) does not survive a round-trip taker cost of 4–10 bps (Binance + Hyperliquid combined), the anticipator alpha is not monetizable as a directional taker strategy. The signal may still be useful for execution timing or quote skewing (research-proposed).
2. **Extended sample:** Replicate across BTC (different volatility regimes), ETH, SOL, and other liquid perps on both venues over 6+ months. If the anticipatory minority disappears or shrinks below statistical significance in a longer sample, the effect may be regime-specific (research-defined falsification threshold).
3. **Wallet-sybil test:** If the anticipator wallets can be linked to a small number of underlying entities (via on-chain clustering), the "persistent minority" may be a single actor, not a distributed phenomenon. This would change the economic interpretation but not the signal. research-proposed.
4. **Venue-pair variation:** Replicate on other CEX-DEX pairs (e.g., Binance vs. dYdX, OKX vs. Hyperliquid). If the anticipatory signal is specific to Hyperliquid's on-chain transparency (i.e., the wallet-level data is the alpha, not the trading), the mechanism differs from the stated hypothesis.
5. **Horizon sensitivity:** If the lead collapses below 2 s resolution (i.e., the effect is an artifact of the 5 s grid), the signal is not exploitable at practical latencies.

## Crypto portability

**adapted** — The paper studies crypto perpetual futures directly. The mechanism (cross-venue informed flow on on-chain venues) is crypto-native. Portability to other crypto venue pairs is unproven but plausible. The key portability requirement is wallet-level transparency (available on on-chain venues like Hyperliquid, Drift, etc.) combined with a dominant CEX reference price. The signal is not directly portable to traditional markets where trader identities are not publicly observable.

**Crypto-specific risks:**
- Hyperliquid's on-chain transparency is a structural feature not shared by all DEX venues.
- The 479 ms median receive-lag on Hyperliquid vs ~0 ms on Binance creates an inherent information disadvantage for Hyperliquid-based execution.
- Funding rate settlements every 8 hours add cost to holding positions on perpetual futures.
- 24/7 trading means the signal must be monitored continuously.

## Limitations

- **Sample size:** 29-day window, single instrument (BTC perpetual). Not enough for regime-robust conclusions.
- **Gross markouts only:** All performance figures are gross of fees, spread, funding, and slippage. The signal magnitudes (< 1 bps) are likely below realistic round-trip costs for most participants.
- **Not independently reproduced.**
- **Preprint, not peer-reviewed.** Under revision as of July 2026.
- **Wallet identity ambiguity:** One trader may control multiple wallets; one wallet may represent multiple strategies.
- **Grid resolution constraint:** The 5 s grid cannot resolve sub-5 s leads. The actual lead length is unknown.
- **Data gap:** The paper does not report the cost of maintaining real-time WebSocket feeds to both venues or the infrastructure requirements for sub-second cross-venue execution.
- **Selection bias:** The informed cohort is formed using in-sample markout, then tested out of sample. While the split-sample design mitigates this, the within-half formation still involves sorting on the same metric used for the lead test.

## Implementation status

Not implemented. This is a microstructure measurement study, not a strategy backtest. The operationalization (following anticipatory wallets) is research-proposed and has not been tested in any execution framework.

## Adoption boundary

This record represents research material only. It does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

The anticipatory wallet signal is a microstructure finding about cross-venue information flow. Converting it into a trading strategy requires solving the execution, cost, and capacity challenges documented in the Limitations section.

## Related Wiki records

- `[[quant/crypto-world-order-flow-cross-sectional-quintile-weekly-2026-08-31]]` — World order flow as a cross-sectional predictor of crypto returns; different mechanism (cross-sectional factor vs. wallet-level cross-venue anticipation).
- `[[quant/hyperliquid-sunshine-trading-adverse-selection-liquidity-extraction-2026-09-01]]` — Barone & Lillo (2026) on Hyperliquid sunshine trading; shares the Hyperliquid venue but studies visible vs. hidden execution, not wallet-level anticipation.
- `[[quant/crypto-short-horizon-15min-mean-reversion-taker-flow-2026-09-01]]` — Kitron & Wengrowicz (2026) on short-horizon mean reversion in crypto; shares the taker-flow theme but operates at 15-minute horizons, not sub-second cross-venue.

## Sources

1. Boon Chuan Lim, "Binance Leads, but Some Wallets Anticipate: Wallet-Level Cross-Venue Informed Flow in BTC Perpetual Futures," Research Square preprint, DOI: `10.21203/rs.3.rs-10147582/v1`, posted 05 Jul 2026 (under revision). https://doi.org/10.21203/rs.3.rs-10147582/v1
