---
schema: strategy-research-record-v1
title: Hyperliquid Sunshine Trading: Adverse Selection Redistribution and Liquidity Extraction via Visible vs Hidden Execution
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - microstructure
  - order-flow
  - adverse-selection
  - liquidity-provision
  - execution
  - DEX
  - Hyperliquid
status: research-only
confidence: high
source_as_of: 2026-06-14
sources:
  - https://arxiv.org/abs/2606.15715
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Hyperliquid Sunshine Trading: Adverse Selection Redistribution and Liquidity Extraction via Visible vs Hidden Execution

## Provenance

- Paper: Davide Barone and Fabrizio Lillo, "Trading in the Sunshine or in the Shade: Market Impact and Adverse Selection on Hyperliquid," arXiv:2606.15715v1 (q-fin.TR), June 2026.
- URL: https://arxiv.org/abs/2606.15715
- Data: 4.3 million hidden metaorders and 465,000 visible TWAP executions on Hyperliquid, reconstructed from address-level on-chain data.
- Venue: Hyperliquid (fully on-chain limit order book for cryptocurrency perpetual futures).
- The paper studies Hyperliquid's protocol-native TWAP orders, which disclose their terms from inception and remain visible while active — a natural form of "sunshine trading" (Admati and Pfleiderer, 1991).

## Economic mechanism

### Source-reported

Sunshine trading theory predicts that publicly disclosing trading intentions can reduce adverse selection and attract liquidity provision, lowering execution costs. Evidence in traditional markets is scarce because explicit preannouncement of large orders is rare. Hyperliquid's protocol-native TWAP orders provide a natural experiment: they disclose their full terms (direction, size, duration) from inception and remain visible while active.

The authors find that:
1. Visible TWAPs face lower execution costs (measured by implementation shortfall and spread-based metrics) than comparable hidden metaorders.
2. Visible TWAPs leave a smaller permanent price impact than hidden metaorders.
3. Hidden metaorders executed alongside already-visible same-direction TWAP flow incur **higher** permanent costs — adverse selection costs shift toward non-announcers.
4. Visible TWAP programs elicit liquidity provision: while active, displayed depth rises and the book tilts toward the absorbing side, more so for larger announced orders.

Hidden metaorders follow front-loaded, U-shaped execution schedules consistent with transient-impact optimal execution (Almgren-Chriss style), whereas TWAPs trade nearly uniformly.

### Research interpretation

The alpha hypothesis is: on crypto perpetual DEX order books with visible execution programs, the presence of visible TWAP flow creates a **liquidity extraction opportunity** for informed or contrarian participants. Specifically:

1. **Adverse Selection Redistribution:** When a visible TWAP is active, the order book tilts toward the TWAP's direction. Liquidity providers are drawn in, creating temporary depth. However, this depth is asymmetrically informed — the TWAP's terms are known, so the book tilt is predictable. Hidden metaorders trading in the same direction as the visible TWAP face higher adverse selection because liquidity providers already anticipate the TWAP's demand.

2. **Liquidity Extraction from Visibility:** A participant who observes the visible TWAP can predict the direction of liquidity provision and the likely price impact trajectory. This creates two exploitable micro-edges:
   - **Liquidity provision alongside the TWAP:** Posting limit orders on the side where the TWAP will consume liquidity, capturing the spread as the TWAP lifts resting orders.
   - **Front-running the TWAP's exhaustion:** The TWAP's uniform schedule means its remaining demand is predictable. Near the end of the TWAP window, the absorbing side loses its demand catalyst, creating a potential reversal.

3. **Hidden Order Toxicity Amplification:** Non-announcers (hidden metaorders) trading alongside visible TWAP flow face increased adverse selection. The visible TWAP's presence signals demand to the market, and hidden flow attempting to exploit this is detected and front-run by informed liquidity providers.

This is a microstructure-based alpha: the mechanism is adverse selection redistribution driven by asymmetric information about execution intent. The alpha is extractable by participants who can observe the visible TWAP and position accordingly.

## Signal

- **Primary Signal: Visible TWAP Detection and Tracking**
  - On Hyperliquid, visible TWAP orders are protocol-native and publicly observable on-chain.
  - Parameters to track: direction (buy/sell), total size, remaining size, time elapsed, execution rate.
  - The TWAP's uniform execution schedule makes remaining demand fully predictable.

- **Secondary Signal: Order Book Imbalance Response**
  - During an active visible TWAP, monitor the order book tilt (bid-ask depth imbalance) toward the TWAP's direction.
  - The depth increase is proportional to TWAP size and inversely proportional to the asset's baseline liquidity.

- **Entry Signal (Liquidity Provision):**
  - Post limit orders on the side where the visible TWAP will consume liquidity (i.e., the TWAP's target side).
  - Set price at or near the top of book on the absorbing side.
  - The TWAP will mechanically lift resting orders at the prevailing spread.

- **Entry Signal (Contrarian at Exhaustion):**
  - Near the end of the visible TWAP window, when remaining size approaches zero, consider a contrarian position anticipating the reversal as the demand catalyst expires.

- **Parameters:**
  - TWAP window duration: protocol-defined (Hyperliquid TWAPs have configurable durations).
  - Book depth threshold: research-proposed minimum depth to ensure the TWAP has material impact.
  - Exhaustion timing: research-proposed trigger at <10% remaining TWAP size.
  - These thresholds are research-proposed and not specified by the source.

## Required data

- **Instrument:** Cryptocurrency perpetual futures on Hyperliquid (BTC, ETH, SOL, and other actively traded pairs).
- **Venue:** Hyperliquid (fully on-chain order book DEX).
- **Market type:** Perpetual futures (USDC-margined).
- **Data needed:**
  - On-chain order book depth (bid/ask levels, sizes).
  - On-chain trade flow (aggressor side, price, size, timestamp).
  - Visible TWAP order metadata (direction, total size, remaining size, start time, end time, execution history).
  - Hidden metaorder reconstruction (requires address-level trade clustering).
- **Timestamp:** On-chain block timestamps; millisecond-level precision may not be available (depends on Hyperliquid's block time).
- **Point-in-time:** TWAP terms are visible from inception; no look-ahead bias for visible TWAP detection.

## Execution assumptions

- **Signal-to-order timing:** The visible TWAP is observable in real-time on-chain; orders can be placed immediately upon detection.
- **Execution model:** Limit orders posted to Hyperliquid's on-chain order book.
- **Fill model:** Maker orders subject to queue priority and fill probability.
- **Fees:** Hyperliquid maker/taker fee schedule (typically 0.01% maker / 0.035% taker for BTC perps; verify current schedule).
- **Slippage:** On-chain execution may have variable latency depending on Hyperliquid's block production.
- **Impact / capacity:** The strategy's capacity is bounded by the visible TWAP's size and the order book's depth. Large hidden metaorders may face diminishing returns.
- **Latency:** On-chain latency (~0.2-0.5s per Hyperliquid block) limits high-frequency execution. The strategy is medium-frequency.
- **Leverage:** The source does not specify leverage assumptions. Research-proposed: conservative leverage (≤3x) to avoid liquidation during adverse moves.
- **Funding:** Continuous funding on Hyperliquid (1h EWMA); the strategy may earn or pay funding depending on position direction.

## Evidence

### Source-reported

- Visible TWAPs face lower execution costs than comparable hidden metaorders (measured across multiple cost metrics).
- Visible TWAPs leave smaller permanent price impact than hidden metaorders.
- Hidden metaorders alongside same-direction visible TWAP flow incur higher permanent costs (adverse selection shift).
- Visible TWAP programs elicit liquidity provision: displayed depth rises proportionally to TWAP size.
- 4.3 million hidden metaorders and 465,000 visible TWAP executions analyzed across multiple crypto perpetual pairs on Hyperliquid.
- The paper provides empirical support for Admati and Pfleiderer (1991) sunshine trading theory in a crypto DEX setting.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan

- **Required sample:** Sufficient visible TWAP events across multiple assets and market regimes (trending, ranging, high-vol, low-vol).
- **Baseline:** Compare strategy returns to: (a) random limit order placement, (b) passive market making without TWAP awareness, (c) following the TWAP direction as a market order.
- **Ablation tests:**
  - Test liquidity provision strategy in isolation (without exhaustion reversal).
  - Test exhaustion reversal in isolation (without liquidity provision).
  - Test whether the edge survives after accounting for Hyperliquid's fee schedule.
- **Cost sensitivity:** Model the impact of maker fees, taker fees, and potential slippage on the observed edge.
- **Out-of-sample requirement:** Test on TWAP events not used in the original study's data period.
- **Failure metric:** If the strategy's Sharpe ratio (research-proposed threshold: >0.5 annualized after fees) is not achieved across the full sample, the alpha hypothesis is materially weakened.
- **What action follows failure:** The sunshine trading mechanism may still hold, but the edge may be too small to capture after costs, or the strategy may require faster execution than on-chain latency permits.

## Crypto portability

direct

This is a native crypto DEX strategy. The mechanism is specific to on-chain limit order books with protocol-native visible execution programs. It does not directly transfer to CEXs (where TWAPs are typically hidden ICEBERG orders) or to traditional markets (where preannouncement is rare).

However, the underlying adverse selection theory (Admati and Pfleiderer, 1991) is generalizable. If other DEX venues adopt visible execution protocols, the same mechanism would apply. Additionally, on CEXs where TWAP execution patterns can be statistically detected (even if not explicitly visible), a related but weaker signal may exist.

Crypto-specific portability considerations:
- **On-chain latency:** Block production latency on Hyperliquid limits the strategy's speed. Higher-frequency variants may not be feasible.
- **TWAP protocol design:** The strategy depends on Hyperliquid's specific TWAP implementation. Changes to the protocol (e.g., making TWAPs hidden) would eliminate the alpha.
- **DEX fragmentation:** Hyperliquid is one of many perpetual DEX venues; cross-venue TWAP coordination is unlikely but possible.

## Limitations

- **Protocol-specific:** The strategy depends on Hyperliquid's specific visible TWAP implementation. If the protocol changes, the edge may disappear.
- **On-chain latency:** Block production latency limits execution speed and may reduce the strategy's edge in fast-moving markets.
- **Not independently reproduced:** The findings are based on a single paper's dataset.
- **Survivorship bias:** The dataset covers a specific period; TWAP behavior may differ in different market regimes.
- **Capacity constraints:** The strategy's capacity is bounded by visible TWAP sizes and order book depth.
- **Research-proposed thresholds:** The entry/exit parameters and Sharpe threshold are research-proposed and not validated.

## Implementation status

Not implemented. No implementation in PyBroker, Nautilus, paper trading, testnet, or live trading has been completed.

## Adoption boundary

This record represents normalized research material only. A record being present in this repository does **not** mean:
- The strategy is profitable.
- The alpha has been validated.
- The strategy is approved for implementation.
- The strategy is approved for paper trading, testnet, or live trading.

## Related Wiki records

- [[crypto-uniswap-v3-just-in-time-jit-liquidity-provision-price-impact-2026-09-01]] — JIT liquidity on Uniswap V3 (different mechanism: concentrated liquidity vs order book).
- [[contrarian-market-making-fill-probability-order-flow-2026-09-01]] — Contrarian market making via order-flow features (related: adverse selection management in order books).
- [[funding-aware-market-making-perpetual-dex-2026-08-31]] — Funding-aware liquidity provision on Hyperliquid (overlapping venue, different mechanism).

## Sources

1. Barone, D. and Lillo, F. (2026). "Trading in the Sunshine or in the Shade: Market Impact and Adverse Selection on Hyperliquid." arXiv:2606.15715v1 [q-fin.TR]. https://arxiv.org/abs/2606.15715
2. Admati, A. R. and Pfleiderer, P. (1991). "Sunshine Trading and Financial Market Announcements." *Journal of Financial Intermediation*, 1(3), 233-257. [Referenced in the source paper; not independently verified.]
