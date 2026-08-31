---
schema: strategy-research-record-v1
title: Perpetual Inverse-Linear Margin Currency Funding Spread
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - funding-rate
  - perpetual-futures
  - relative-value
  - margin-currency
  - carry
status: research-only
confidence: medium
source_as_of: 2026-07-06
sources:
  - "BitMEX Research, 'Q2 Derivatives Report: 3 Sources of Funding Rate Alpha', 6 July 2026 — https://www.bitmex.com/blog/2026q2-derivatives-report"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Perpetual Inverse-Linear Margin Currency Funding Spread

## Provenance

- **Primary source:** Shang Wu (BitMEX Senior Research Analyst), "Q2 Derivatives Report: 3 Sources of Funding Rate Alpha," published 6 July 2026 on the BitMEX blog.
- **Source URL:** https://www.bitmex.com/blog/2026q2-derivatives-report
- **Specific contracts referenced:** BitMEX XBTUSD (inverse, bitcoin-margined perpetual) and XBTUSDT (linear, USDT-margined perpetual).
- **Data period cited:** 3.5+ years of historical funding rate data (approximately 2023–2026).
- **Empirical figures cited by source:** Inverse-minus-linear spread averages −3.93% annualised; negative in 94% of all 90-day rolling windows. XBTUSDT average ~+10% annualised funding; XBTUSD average ~+6% annualised funding.

## Economic mechanism

### Source-reported

The two perpetual contracts track the same underlying (BTC/USD) but differ only in collateral currency. The inverse contract (XBTUSD) is margined in bitcoin; the linear contract (XBTUSDT) is margined in USDT. This single design variable attracts structurally different trader populations:

- **Bitcoin-margined traders** already own BTC and post it as collateral. They tend to hedge or lean short, adding supply to the inverse book.
- **USDT-margined traders** deploy stablecoin capital and seek leverage on the long side, adding demand to the linear book.

Funding is paid by the crowded side. Because the linear book is persistently long-heavy and the inverse book is short-heavy, the linear contract pays structurally higher funding. The spread between the two contracts reflects this collateral-driven demand asymmetry.

### Research interpretation

This is a **structural carry trade** arising from segmented capital pools. The mechanism is:

1. Different collateral requirements create segmented trader populations.
2. BTC-margined participants are structurally shorter (hedging existing BTC exposure).
3. USDT-margined participants are structurally longer (deploying stablecoin dry powder for leverage).
4. The funding differential persists because collateral currencies are not fungible within a single exchange account — until multi-asset margining reduces this friction.

The hypothesised alpha source is: **collateral-driven positioning asymmetry creates a durable funding rate differential between inverse and linear perpetuals on the same underlying.**

This is a carry trade, not a directional bet. The position is delta-neutral (long inverse + short linear = zero net BTC exposure) and earns the funding spread.

## Signal

- **Signal formation:** Continuous (based on persistent structural difference in funding rates, not a timing signal).
- **Trade structure:** Long XBTUSD (inverse perpetual, pays ~6% annualised), short XBTUSDT (linear perpetual, collects ~10% annualised).
- **Net exposure:** Delta-neutral to BTC price; pure funding spread capture.
- **Holding period:** Structural carry — intended to be held continuously, not a short-term trade.
- **Re-entry rules:** Maintained as long as the spread persists; the source notes the spread can compress at quarter-end and that increased adoption of multi-asset margining may narrow it over time.
- **Position sizing:** Source describes this as a "sized, hedged regime carry" with basis and convexity risk.
- **Parameters:** Source reports historical average spread of −3.93% annualised (inverse minus linear) over 3.5 years. No specific entry/exit thresholds given.
- **Fully specified:** Partially. The trade logic is clear (long inverse, short linear), but no precise sizing, entry timing, or stop-loss rules are specified.

## Required data

- **Instrument:** BTC/USD perpetual futures (inverse and linear variants).
- **Venue:** BitMEX (XBTUSD and XBTUSDT specifically).
- **Market type:** Perpetual futures (inverse + linear).
- **Timeframe:** 8-hour funding intervals (standard for BitMEX).
- **Data needed:** Historical funding rates for both contracts; collateral margin requirements; multi-asset margining availability.
- **Timestamp requirements:** Funding settlement timestamps (typically 00:00, 08:00, 16:00 UTC).
- **Missing data:** Source does not provide raw funding rate time series; only summary statistics.

## Execution assumptions

- **Signal-to-order timing:** Continuous carry — positions held across funding intervals.
- **Execution:** Market or limit orders on both legs; must be simultaneous to avoid directional exposure.
- **Fees:** Trading fees on entry/exit for both legs; funding payments at each 8-hour interval.
- **Spread:** Source does not quantify bid-ask spread impact.
- **Slippage:** Not discussed; likely minimal for BTC on BitMEX given deep liquidity.
- **Leverage:** Source does not specify; position is delta-neutral so leverage affects capital efficiency but not directional risk.
- **Margin:** Historically required separate margin pools (BTC for inverse, USDT for linear). Multi-asset margining now allows single collateral pool, reducing capital fragmentation and liquidation risk on individual legs.
- **Funding:** The core P&L driver; net carry of ~4% annualised after offsetting funding payments.
- **Capacity:** Not discussed; likely limited by BitMEX-specific liquidity on both contracts.
- **Latency:** Not critical for structural carry; not a latency-sensitive strategy.

## Evidence

### Source-reported

- Over 3.5 years, the inverse-minus-linear funding spread averages −3.93% annualised.
- The spread is negative in 94% of all 90-day rolling windows.
- XBTUSDT (linear) averages ~+10% annualised funding; XBTUSD (inverse) averages ~+6% annualised funding.
- The spread compressed and briefly flipped positive at the right edge of the reported data (early-mid 2026).
- Multi-asset margining removes the capital fragmentation that previously made the trade operationally difficult.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The spread compressed and briefly flipped positive in the most recent data, suggesting regime dependence.
- Multi-asset margining makes the trade easier to hold, which paradoxically allows more traders to straddle both books and narrow the spread over time.
- The source explicitly warns: "Run it as a sized, hedged regime carry: the spread compressed at quarter-end, and the same Multi Asset Margining that makes it easy to hold also lets more traders close it over time."
- The ~4% annualised carry may be insufficient to cover trading fees, slippage, and capital costs for smaller participants.

## Falsification plan

- **Required sample:** At least 2 years of daily funding rate data for both XBTUSD and XBTUSDT.
- **Baseline:** Zero-cost carry of the funding spread minus trading fees and slippage.
- **Key test:** Does the inverse-minus-linear spread remain negative after transaction costs on a rolling 90-day basis?
- **Regime sensitivity:** Test across bull, bear, and sideways regimes; source notes quarter-end compression.
- **Ablation:** Compare against a simple spot-perp carry (already in the repo) to isolate the margin-currency-specific alpha.
- **Failure metric:** If the spread is positive (or net of costs is negative) in >40% of 90-day windows over a 2-year sample, the structural carry thesis weakens materially.
- **Action on failure:** Demote to reference material; the structural mechanism is theoretically sound but the carry may be too thin post-costs for most participants.

## Crypto portability

adapted

This strategy is specific to crypto perpetual futures (inverse vs linear contracts). It does not exist in traditional markets in the same form because TradFi futures use standardised margin (cash or treasuries), not asset-margined inverse contracts. The mechanism is crypto-native but venue-specific to BitMEX; other exchanges (e.g., OKX, Bybit) offer similar inverse/linear pairs but with different funding dynamics.

**Crypto-specific portability risks:**
- Exchange-specific: The spread is driven by BitMEX-specific trader demographics and contract design.
- Multi-asset margining is an exchange feature; not all venues offer it.
- Funding rate regimes can shift; the spread is not guaranteed to persist.
- Capacity constrained by BitMEX-specific liquidity.

## Limitations

- **Source-reported only:** All performance figures come from the BitMEX blog; no independent academic or third-party verification.
- **Venue-specific:** Strategy is specific to BitMEX contracts; may not generalise to other exchanges.
- **Regime-dependent:** The spread compressed and briefly flipped positive; not a constant carry.
- **Capacity unquantified:** No discussion of how much capital can be deployed before the spread narrows.
- **Fee sensitivity:** Net carry of ~4% annualised is thin; trading fees on two legs at each funding interval could erode a significant portion.
- **Cherry-picking risk:** The BitMEX report is authored by BitMEX's research team, who have a commercial interest in promoting activity on their platform.

## Implementation status

Not implemented in our research stack.

## Adoption boundary

This record represents research material only. Presence in this repository does not mean:
- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

## Related Wiki records

- [[crypto-cex-dex-cross-venue-funding-spread-carry-2026-08-31]] (related but different: cross-venue CEX-DEX spread, not intra-venue inverse-linear spread)
- [[crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31]] (related but different: spot-perp carry, not inverse-linear margin spread)
- [[funding-aware-market-making-perpetual-dex-2026-08-31]] (related: funding rate dynamics on DEX perps)

## Sources

1. Shang Wu, "Q2 Derivatives Report: 3 Sources of Funding Rate Alpha," BitMEX Blog, 6 July 2026. URL: https://www.bitmex.com/blog/2026q2-derivatives-report.
