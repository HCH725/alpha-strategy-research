---
schema: strategy-research-record-v1
title: "TradingView Crypto Range Breakout with ATR Expansion and Three-Day Hold Cap"
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - crypto
  - breakout
  - atr
status: research-only
confidence: medium
source_as_of: 2026-09-27
sources:
  - https://www.tradingview.com/script/uYuaS5nh-ATR-Breakout-v1/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Crypto Range Breakout with ATR Expansion and Three-Day Hold Cap

## Provenance

- Public TradingView protected-source strategy page: **ATR Breakout v1** by **truenordiccapital**.
- Published: 2026-03-15.
- Canonical TradingView script identity: `uYuaS5nh`.
- Stable source URL: https://www.tradingview.com/script/uYuaS5nh-ATR-Breakout-v1/
- Source reviewed as of 2026-09-27.
- The Pine implementation is protected; this record normalizes only the public strategy description and does not reproduce source code.

## Economic mechanism

### Source-reported

The author describes the edge as a price breakout beyond a defined lookback range that is confirmed by ATR expansion. The stated rationale is that ATR expansion distinguishes a momentum-backed breakout from a weaker range escape. The strategy imposes a hard maximum holding period of three days so failed or stale breakouts are not held indefinitely.

### Research interpretation

The falsifiable hypothesis is that a range break contains more directional continuation information when contemporaneous realized-range volatility is expanding. The range breakout is the primary directional signal; ATR expansion is a confirmation filter intended to select higher-energy transitions from consolidation or prior range behavior. The three-day cap is exit/risk logic, not an independent alpha signal.

## Signal

Source-supported normalized logic:

1. Operate on 15-minute bars.
2. Form a lookback price range. The public description does not disclose the exact lookback length or exact high/low construction.
3. Long entry condition: price breaks above the defined lookback range and ATR expansion confirms momentum.
4. Short entry condition: price breaks below the defined lookback range and ATR expansion confirms momentum.
5. ATR confirmation uses a fixed ATR multiplier according to the source, but the ATR length, multiplier value, comparison baseline, and exact expansion algebra are not publicly specified.
6. Exit: every trade has a hard maximum holding period of three days. The public description does not establish whether an earlier stop, opposite signal, or other exit can also close the position.
7. The source exposes a **Standard** preset for SOL/ETH/1000PEPE and a separate **INJ** variant, but does not publicly disclose the parameter differences.

Signal-bar confirmation, intrabar-versus-close breakout semantics, order timing, re-entry, pyramiding, and any earlier exit rules are **underspecified**. No missing operational value is inferred here.

## Required data

- Source-targeted instruments: SOLUSDT, ETHUSDT, 1000PEPEUSDT, and INJUSDT.
- Timeframe: 15 minutes.
- Required fields supported by the public description: timestamp and OHLC sufficient to construct price ranges and ATR.
- Venue: the performance description references "Bybit costs", but the public page does not unambiguously identify the exact Bybit instrument/contract for each symbol.
- Market type (spot versus perpetual/futures): **data gap**.
- Candle timezone/boundary convention: **data gap**.
- Point-in-time requirement: the lookback range and ATR confirmation must use only information available when the entry decision is formed.
- Funding, mark/index price, and contract metadata requirements cannot be resolved until market type is specified.

## Execution assumptions

The source does not specify:

- signal-to-order timing;
- same-bar versus next-bar fill;
- market versus limit orders;
- fill price model;
- spread or slippage;
- exact commission schedule despite saying reported results include "Bybit costs";
- impact/capacity;
- leverage/margin;
- funding treatment;
- liquidation assumptions;
- partial fills or failures.

These are data gaps, not zero-cost assumptions. A future implementation must preserve causal bar timing rather than choosing a favorable fill convention retrospectively.

## Evidence

### Source-reported

The TradingView page labels the strategy "Crypto 15m | Walk-Forward Validated" and states that its continuous backtests span more than three years with "Bybit costs." It reports:

- SOL: +$825K, profit factor 1.689.
- 1000PEPE: +$1,101K, profit factor 1.596.
- ETH: +$169K, profit factor 1.191.
- INJ: +$464K, profit factor 1.154.
- The author states that all legs passed a PF > 1.10 quality gate and remained profitable without outlier trades.

These are source-reported claims from the TradingView page only. The public description does not expose the initial capital, exact sample dates, walk-forward window construction, exact Bybit fee assumptions, trade counts, drawdowns, return percentages, parameter-selection history, or outlier-test method. The dollar P&L figures therefore cannot be normalized into comparable returns from the public information alone.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The reviewed page does not provide enough public methodology to audit its "walk-forward validated" label or reconstruct the reported performance. Profit factor is lowest for INJ (1.154) and ETH (1.191) among the four source-reported legs, leaving relatively little gross margin above 1 before any mismatch between the source's unspecified cost model and a future implementation.

No independent negative empirical source was identified in this cycle; absence is not evidence of robustness.

## Falsification plan

All acceptance cutoffs below are **research-defined falsification thresholds**, not source-reported rules.

- First reconstruct only source-supported semantics; unresolved range length, ATR formula/multiplier, and fill timing must remain explicit implementation blockers rather than optimized guesses.
- Once a reproducible specification exists, compare range breakout + ATR confirmation against the identical range breakout without ATR confirmation. Reject the claimed incremental ATR mechanism if it does not improve out-of-sample net expectancy or risk-adjusted performance across multiple assets.
- Ablate the three-day cap against shorter and longer fixed caps to determine whether reported performance depends narrowly on that exit choice.
- Use chronological out-of-sample or walk-forward evaluation with parameters frozen before each test segment.
- Require robustness across neighboring lookback and ATR parameter values; reject a variant whose edge exists only at an isolated optimum.
- Report SOL, ETH, 1000PEPE, and INJ separately and pooled; do not let one high-P&L leg conceal failures elsewhere.
- Apply explicit venue-appropriate fees, spread, slippage, and—if perpetuals—funding. Reject the trading hypothesis if plausible costs remove positive out-of-sample expectancy.
- Inspect trade-count and return concentration. Reject claims of broad robustness if performance is dominated by a small number of extreme moves.
- Verify causal range and ATR construction bar by bar and reject any implementation with look-ahead or same-bar fill leakage.

## Crypto portability

**direct** for the hypothesis, because the source explicitly targets crypto and names SOLUSDT, ETHUSDT, 1000PEPEUSDT, and INJUSDT on 15-minute bars.

Implementation portability remains incomplete because the exact venue instruments and market type are not specified. Crypto-specific risks include 24/7 candle boundaries, venue fragmentation, spot-versus-perpetual differences, funding, mark/index conventions, differing fee tiers, and materially different liquidity in SOL, ETH, 1000PEPE, and INJ.

## Limitations

- Protected Pine source prevents direct inspection of the implementation.
- Exact range lookback/construction is **underspecified**.
- Exact ATR length, multiplier, expansion test, and preset differences are **underspecified**.
- Entry fill timing, earlier exits, re-entry, and position sizing are **underspecified**.
- Exact Bybit fee/cost assumptions are a **data gap**.
- Walk-forward methodology and sample boundaries are a **data gap**.
- Source-reported dollar P&L lacks disclosed initial capital on the public page.
- Not independently reproduced.
- The source's reported results do not establish that the mechanism will survive independent point-in-time reconstruction or current transaction costs.

## Implementation status

Research record only. No implementation, backtest, parameter recovery, or Qlib validation was performed in this Scout cycle.

## Adoption boundary

`research-only`. Presence in this repository does not mean this strategy passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, is profitable, or is approved for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

No stable Hermes Wiki Brain link was verified in this GitHub-only workflow; none is fabricated.

## Sources

- truenordiccapital, **ATR Breakout v1**, TradingView, published 2026-03-15, reviewed 2026-09-27: https://www.tradingview.com/script/uYuaS5nh-ATR-Breakout-v1/
