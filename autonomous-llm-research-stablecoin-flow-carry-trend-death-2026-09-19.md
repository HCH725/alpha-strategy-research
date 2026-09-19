---
schema: strategy-research-record-v1
title: "Autonomous LLM Research Loop with On-Chain Stablecoin-Flow Overlay and Out-of-Window Death"
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - on-chain
  - stablecoin
  - autonomous-research
  - negative-result
  - carry
  - trend
status: research-only
confidence: high
source_as_of: 2026-09-19
sources:
  - "Bryan Vine, 'On-Chain Liquidity and the Crypto Premia: An Autonomous Search and an Honest Out-of-Window Death', Alpha Research Paper 8, https://bryanvine.github.io/alpha-research/paper8.html (2026)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Autonomous LLM Research Loop with On-Chain Stablecoin-Flow Overlay and Out-of-Window Death

## Provenance

- **Primary source:** Bryan Vine, "On-Chain Liquidity and the Crypto Premia: An Autonomous Search and an Honest Out-of-Window Death", Alpha Research Paper 8, published 2026. URL: https://bryanvine.github.io/alpha-research/paper8.html
- **Author:** Bryan Vine (same author as Papers 1–7 in the Alpha Research series)
- **Code repository:** https://github.com/bryanvine/alpha-research (same repo as prior papers)
- **DeFiLlama API:** https://defillama.com/docs/api (free, keyless on-chain data source)
- **Sample period:** In-window: 2023–2026 (~1,263 days); Extended: 2020–2026 (2,359 days)
- **Universe:** Crypto perpetual futures (Binance USD-M); carry and trend sleeves from Papers 2 and 4
- **Primary source reviewed:** Full HTML text of Paper 8, including Tables 1, Figures 1–3, and all sections

## Economic mechanism

### Source-reported

Vine builds an autonomous research loop — an LLM agent that rewrites a single strategy file (`factor.py`), scores it through a fixed rigor protocol, and iterates. The agent never sees or runs the scorer; a fixed harness owns the evaluation and global trial count, preventing deflated-Sharpe and PBO gaming.

The system surfaced one promising lead from DeFiLlama on-chain data: a stablecoin-flow overlay that rotates between the crypto carry sleeve (Paper 2: short high-funding / low-funding perps) and trend sleeve (Paper 4) based on a lagged, standardized stablecoin-liquidity score. The economic hypothesis is:
- **Stablecoin minting = fresh dollars entering crypto** → favor trend continuation as new money chases winners
- **Stablecoin contraction = capital leaving** → favor the funding-carry sleeve, where crowded leverage unwinds

The overlay keeps the crypto book fully invested but rotates relative sleeve selection — never a directional exposure bet.

### Research interpretation

This is a **regime-conditional overlay hypothesis**: on-chain stablecoin supply dynamics serve as a macro-liquidity state variable that predictably shifts the relative attractiveness of carry vs. trend premia. The mechanism posits that capital flow into stablecoins signals risk-on conditions favoring momentum, while outflows signal risk-off conditions favoring carry harvesting.

However, the paper's core finding is that this mechanism **does not survive out-of-sample extension**. The headline result is a methodological contribution: autonomous search paired with honest out-of-window testing kills fits before human attachment can form.

## Signal

### Formation timestamp
- Stablecoin-liquidity score: daily, lagged one day (no contemporaneous information)
- Standardized against trailing history
- Sleeve rotation: daily rebalance

### Lookback
- Trailing standardized window for stablecoin-liquidity score: not explicitly stated; standardized against trailing history (research-proposed)
- Carry and trend sleeve construction follows Papers 2 and 4

### Long entry
- When lagged standardized stablecoin-liquidity score is high (expanding on-chain liquidity): allocate more to trend sleeve
- When lagged standardized stablecoin-liquidity score is low (contracting on-chain liquidity): allocate more to carry sleeve

### Short entry
- Dollar-neutral within each sleeve (long low-funding / short high-funding for carry; long winners / short losers for trend)

### Exit
- Daily rebalance based on updated stablecoin-liquidity score

### Holding period
- Daily rebalance; positions held until next rebalance

### Parameters
- Sleeve allocation: 50/50 equal-weight between carry and trend when unconditioned; overlay rotates between them
- Stablecoin-liquidity score: source-reported; exact formula and standardization window **underspecified** in Paper 8 (the agent's `factor.py` was not published)
- All parameters are source-reported from the autonomous loop; none are Scout-proposed

### Position-sizing logic
- Dollar-neutral within each sleeve; gross exposure 1.0 (source-reported)
- No leverage specified

### Overspecification markers
- The exact stablecoin-liquidity score formula is not published (agent-edited `factor.py` was not shared)
- Standardization window is not specified
- Rotation allocation weights between sleeves are not specified

## Required data

- **Instrument:** Binance USD-M perpetual futures (carry and trend sleeves)
- **Venue:** Binance
- **Market type:** USDT-margined perpetual futures
- **Timeframe:** Daily
- **On-chain data:** DeFiLlama API — total stablecoin supply, DeFi TVL, protocol fees (free, keyless)
- **Funding rates:** Binance USD-M funding history (8-hour intervals, aggregated to daily)
- **Price data:** Binance spot/perp daily
- **Timestamp:** UTC
- **Missing data:** DeFiLlama API is free and keyless; data availability assumed continuous for 2020–2026

## Execution assumptions

- **Signal-to-order timing:** Daily rebalance; exact execution time not specified
- **Fill model:** Not specified; assumed taker execution
- **Fees:** Not explicitly stated in Paper 8; the carry and trend sleeves from Papers 2 and 4 use 6 bp/side taker+slippage costs
- **Slippage:** Not specified for this overlay
- **Spread:** Not specified
- **Funding:** Carry sleeve explicitly harvests funding; trend sleeve is directional
- **Capacity:** Not discussed; likely constrained by smaller perp books in the carry sleeve

## Evidence

### Source-reported

**In-window (2023–2026, ~1,263 days):**
- Overlay OOS Sharpe: 1.18 vs 0.66 for unconditioned 50/50 book
- All 18 configurations in pre-registered grid positive (0.97–1.19)
- Deflated Sharpe: 0.97
- PBO: 0.11
- Five-day mechanism rank-IC: 0.17, t=3.22
- Overlay daily t: 2.21

**Extended window (2020–2026, 2,359 days) — the kill:**
- Five-day mechanism t: 3.22 → 0.48
- Overlay OOS Sharpe: 1.18 → 1.42
- Equal-weight OOS Sharpe: 0.66 → 1.26
- Overlay edge over EW: +0.52 → +0.16
- PBO: 0.11 → 0.51 (failed)
- Year-by-year IC flips sign at random
- Verdict: "a fit"

**Autonomous loop statistics:**
- 0 of ~90 candidates passed the rigor gate
- 5 campaigns tested: surviving premia conditioning, open-ended sweep, equity point-in-time fundamentals (SEC EDGAR), futures positioning (CFTC COT), on-chain data (DeFiLlama)

All figures directly reported by Vine (Alpha Research Paper 8, bryanvine.github.io/alpha-research/paper8.html).

### Independently reproduced

`Not independently reproduced.`

### Negative evidence

This paper IS a negative result. The autonomous loop found one promising lead, and an out-of-window test killed it. The paper explicitly concludes that in-sample significance is not robustness, even when deflated, walk-forward, and mechanism-confirmed. The cheapest and most decisive rigor test remains: get more data and look again.

## Falsification plan

The paper itself provides the falsification:
1. **Out-of-window extension:** Backfill crypto sleeves to 2020 and re-run. Result: mechanism collapses, PBO fails. **FALSIFIED.**
2. **Year-by-year IC stability:** Information coefficient should be consistently signed. Result: flips sign at random. **FALSIFIED.**
3. **Deflated Sharpe under extended sample:** Should remain above program threshold. Result: not reported separately, but PBO failure implies deflated Sharpe degradation.

Additional research-proposed falsification thresholds:
- If the stablecoin-flow mechanism does not replicate on a forward out-of-window period (post-2026), the hypothesis is abandoned.
- If the mechanism survives on a different venue (e.g., Hyperliquid, OKX) with independent stablecoin-flow data, the hypothesis would be revived.

## Crypto portability

`direct` — the research is native to crypto perpetual futures and on-chain data.

## Limitations

- **Sample is short:** Even extended, the crypto sleeves span 2020–2026 with thin pre-2023 cross-section; 2020–2022 is a single bull-then-bear regime.
- **In-sample fit:** The most promising lead was a 2023–2026 window fit, killed by a single out-of-window test.
- **Autonomous search as multiple-comparisons machine:** Global deflation guards within a campaign, but cross-campaign and within-turn exploration are only partly accounted for.
- **Agent code not published:** The `factor.py` written by the LLM agent was not shared, making the exact stablecoin-flow formula unverifiable.
- **Local-model runs weaker:** When frontier-model quota ran out, open-source fallback build-failed more often and leaned toward beta tilts.
- **Single venue:** Binance only; no cross-venue validation.

## Implementation status

`not-implemented`. The paper is a methodological contribution (autonomous search + honest out-of-window kill), not a tradeable strategy. No implementation exists in our research stack.

## Adoption boundary

This record represents research material only. It is not a validated alpha, not approved for implementation, and not approved for paper/testnet/live trading. The paper's own conclusion is that the system's value is the honest kill, not the find.

## Related Wiki records

- `[[crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11]]` — Bryan Vine Paper 2 (carry sleeve used in this overlay)
- `[[crypto-adaptive-trend-following-asymmetric-portfolio-2026-09-01]]` — trend following (trend sleeve domain)
- `[[stablecoin-dry-powder-volatility-targeting-copula-2026-09-01]]` — stablecoin as dry powder hypothesis

## Sources

1. Bryan Vine. "On-Chain Liquidity and the Crypto Premia: An Autonomous Search and an Honest Out-of-Window Death." Alpha Research Paper 8, 2026. https://bryanvine.github.io/alpha-research/paper8.html
2. DeFiLlama. Open on-chain data API — stablecoin supply, TVL, protocol fees. https://defillama.com/docs/api
3. Bailey, D. & López de Prado, M. (2014). "The Deflated Sharpe Ratio." Journal of Portfolio Management 40(5).
4. Bailey, D., Borwein, J., López de Prado, M. & Zhu, Q. (2017). "The Probability of Backtest Overfitting." Journal of Computational Finance 20(4).
5. Karpathy, A. (2026). autoresearch. https://github.com/karpathy/autoresearch
