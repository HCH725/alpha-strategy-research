---
schema: strategy-research-record-v1
title: Crypto EMA200 Liquidity Sweep Reclaim with Reversal Confirmation
created: 2026-10-03
updated: 2026-10-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-03
sources:
  - https://www.tradingview.com/script/ZhJzjmAk-Crypto-Institutional-Liquidity-Sweep-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto EMA200 Liquidity Sweep Reclaim with Reversal Confirmation

## Provenance

Public TradingView open-source strategy, **Crypto Institutional Liquidity Sweep Strategy**, by **Danish7421** (page identity also displays "dany"). Stable TradingView URL: https://www.tradingview.com/script/ZhJzjmAk-Crypto-Institutional-Liquidity-Sweep-Strategy/. The page was reviewed as of 2026-10-03 and displays publication date Feb 4.

Only the public page description was normalized. No Pine source is reproduced here.

## Economic mechanism

### Source-reported

The author frames the setup as a stop-run/liquidity-grab reversal inside the dominant trend. A recent pivot high/low is pierced and then reclaimed; an EMA-200 directional filter, a selectable secondary confirmation, and reversal-candle anatomy are intended to distinguish a rejected liquidity sweep from a genuine breakout.

### Research interpretation

The falsifiable hypothesis is narrower than the author's institutional narrative: a **confirmed structural-level sweep and reclaim, conditioned on EMA-200 trend direction and same-bar rejection quality**, may contain short-horizon reversal/continuation information beyond a generic pivot reclaim.

Component roles:

- Regime/direction: price relative to EMA(200).
- Primary event: pierce a recent confirmed swing high/low and reclaim the level.
- Optional confirmation: either rising volatility-oscillator state or linear-regression-slope micro-structure alignment.
- Reversal confirmation: directional candle whose close is in the favorable 40% of its range.
- Risk logic: source reports ATR-scaled static stop and fixed 1:2 reward:risk.

Whether any component adds alpha is unverified and should be tested by ablation.

## Signal

Source-reported normalized logic:

- Long bias only when price is above EMA(200); short bias only when price is below EMA(200).
- An optional percentage buffer around EMA(200) may suppress trades near the moving average. The default/value is underspecified in the reviewed page.
- Structural liquidity pools are recent swing highs/lows identified from pivots. Pivot lookback/left-right confirmation parameters are underspecified in the reviewed page.
- Bullish event: price pierces below a recent structural low and then reclaims/rejects that level.
- Bearish event: price pierces above a recent structural high and then reclaims/rejects that level.
- A user-selectable secondary filter is required: either a rising volatility oscillator or linear-regression slope aligned with the macro trend. Exact oscillator construction, regression window, and thresholds are underspecified in the reviewed page.
- Long reversal candle must be bullish and close in the upper 40% of its total range. Short reversal candle must be bearish and close in the lower 40%.
- Source reports static stop-loss and take-profit levels locked at entry, with ATR determining stop distance and a fixed 1:2 reward:risk ratio. ATR length/multiplier and exact fill/order semantics are underspecified in the reviewed page.
- Holding period and re-entry/cooldown rules are underspecified.

Causal-timing requirement for research: pivots must become eligible only after their right-side confirmation is available; retrospective use of future-confirmed pivots would create look-ahead leakage. This is a research constraint derived from point-in-time validity, not a source-reported parameter.

## Required data

- Crypto OHLCV bars.
- EMA(200) from point-in-time closes.
- Confirmed pivot/swing highs and lows.
- ATR inputs.
- Inputs required by the selected secondary filter: volatility-oscillator inputs or price series for linear-regression slope.
- Bar timestamps with deterministic candle boundaries.
- Venue, instrument, market type (spot/perpetual), preferred timeframe, pivot parameters, and secondary-filter parameters are underspecified by the reviewed page.

## Execution assumptions

The source states that static stop and target levels are calculated and locked upon entry and that the stop distance is ATR-based with 1:2 reward:risk.

The reviewed page does not unambiguously specify signal-to-order timestamp, next-bar versus same-bar fill, market versus limit order, fees, spread, slippage, impact/capacity, funding, leverage/margin, partial fills, or latency. These remain underspecified and must not be silently filled.

For later testing, any chosen fill model or cost model is **research-proposed**.

## Evidence

### Source-reported

The reviewed TradingView page describes the rules and intended mechanism but provides no performance statistic that is sufficiently traceable in the reviewed text to record as evidence here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source's "liquidity grab" interpretation is narrative rather than independently established causality. Pivot confirmation can introduce lag, and any implementation that uses pivots before confirmation would be invalid. The EMA-200 filter can also suppress reversals counter to the prevailing trend. No independent negative-result study was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

1. Compare the full rule against a pivot sweep-and-reclaim baseline with no EMA, secondary filter, or candle-location confirmation.
2. Ablate EMA(200), the secondary filter, and the favorable-40%-close condition one at a time.
3. Test volatility-oscillator and regression-slope variants separately rather than pooling them.
4. Enforce point-in-time pivot confirmation and compare results with a deliberately retrospective diagnostic to quantify leakage sensitivity.
5. Evaluate multiple liquid crypto instruments and both trending/choppy regimes out of sample.
6. Stress realistic fees, spread, slippage, and—when perpetuals are tested—funding.
7. Test whether performance survives parameter perturbations around pivot settings, EMA buffer, ATR settings, and reversal-candle threshold once those rules are explicitly operationalized.
8. **Research-defined falsification threshold:** reject or materially weaken the incremental thesis if the full construction fails to improve risk-adjusted, cost-net OOS performance over the sweep/reclaim baseline across reasonable parameter neighborhoods, or if apparent improvement disappears under causal pivot timing.

## Crypto portability

**direct**

The source explicitly presents the strategy as crypto-focused. Portability across crypto venues remains unproven. Spot versus perpetual execution can differ through funding, leverage, mark/index mechanics, and liquidation risk; 24/7 candle boundaries and venue-specific liquidity can materially change pivots and sweeps.

## Limitations

- Not independently reproduced.
- Pivot parameters are underspecified.
- EMA buffer value is underspecified.
- Secondary-filter formulas/parameters are underspecified.
- ATR parameters and exact order/fill semantics are underspecified.
- Timeframe, venue, and market-type defaults are not established by the reviewed page.
- Execution costs and funding are a data/assumption gap.
- "Institutional liquidity" and "stop hunt" are source framing, not verified participant-level evidence.

## Implementation status

Research-only capture. No implementation in the research stack and no Qlib full backtest has been completed.

## Adoption boundary

This record is research material only. Its presence does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor/leaderboard entry, demonstrated profitable or validated alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No stable related Hermes Wiki Brain record was identified from the GitHub-only research context; no Wiki link is fabricated.

## Sources

- TradingView — Danish7421, **Crypto Institutional Liquidity Sweep Strategy**: https://www.tradingview.com/script/ZhJzjmAk-Crypto-Institutional-Liquidity-Sweep-Strategy/ (public open-source strategy page; reviewed 2026-10-03).
