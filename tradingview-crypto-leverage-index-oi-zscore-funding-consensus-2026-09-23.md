---
schema: strategy-research-record-v1
title: Crypto Leverage Index — OI Z-Score, Funding Extremes, and Multi-Exchange Consensus
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-23
sources:
  - https://www.tradingview.com/script/WYQCG1z3-Crypto-Leverage-Index-OI-Norm-FR/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Leverage Index — OI Z-Score, Funding Extremes, and Multi-Exchange Consensus

## Provenance

- Source: TradingView open-source script, `Crypto Leverage Index(OI Norm. + FR)` by `sanbangaje`.
- Stable URL: https://www.tradingview.com/script/WYQCG1z3-Crypto-Leverage-Index-OI-Norm-FR/
- Originally published: 2025-12-11.
- Source update reviewed: 2025-12-29 multi-exchange OI consensus update.
- Source reviewed / as-of: 2026-09-23.
- Public and traceable at review time; TradingView labels the script open-source.

## Economic mechanism

### Source-reported

The author treats open interest as a measure of outstanding leverage and funding as a measure of directional positioning pressure. The source proposes that unusually high or low OI relative to its recent distribution, together with extreme positive or negative funding, can identify speculative leverage extremes and possible liquidation/squeeze reversal zones. A later update adds cross-exchange OI-extreme confirmation so that an isolated venue spike is distinguished from a broader market-wide leverage condition.

### Research interpretation

The falsifiable hypothesis is that **cross-venue agreement in standardized OI extremes contains incremental information about market-wide leverage crowding, and that conditioning this state on funding-rate direction/extremity improves prediction of subsequent squeeze, liquidation, reversal, or continuation behavior relative to single-venue OI or funding alone**.

The mechanism has three separable components:

1. **Leverage load:** rolling OI z-score identifies unusual outstanding-position levels relative to the instrument's own recent history.
2. **Directional crowding:** funding-rate sign and extremity proxy which side is paying to maintain perpetual exposure.
3. **Breadth / consensus:** simultaneous OI extremes across multiple venues attempt to reject exchange-specific noise and isolate market-wide leverage buildup or unwind.

The source's reversal language is a hypothesis, not an established result. High leverage can precede continuation as well as liquidation; both directions must be tested.

## Signal

### Source-specified construction

- Market type: crypto perpetual futures / swaps with Open Interest data.
- Primary OI statistic: `OI Z-Score = (OI - rolling mean(OI)) / rolling StDev(OI)`.
- OI lookback `Period`: default 50 bars.
- OI extreme threshold: default `+2.0` for high / premium leverage and `-2.0` for low / discount leverage.
- Funding: source approximates funding from a TWAP of perpetual-futures premium combined with a standard 0.01% interest-rate component.
- Abnormal funding threshold: source gives default/example magnitude `0.03%`; positive extreme represents excessive long positioning and negative extreme excessive short positioning.
- Multi-exchange OI consensus update checks Binance, OKX, Bybit, plus the current chart exchange. Venues without valid OI are ignored.
- Each valid venue contributes one count when its OI z-score breaches the configured threshold. A consensus is reached when the count meets a user-defined `Consensus Min Count`.
- Current-chart OI remains the primary plotted z-score; cross-venue agreement changes the visual emphasis of an extreme.

### Trading lifecycle

The source is an indicator/context tool rather than a complete trading strategy. It does not specify a complete entry, exit, holding-period, re-entry, sizing, stop, or take-profit lifecycle. Those elements are **underspecified**.

### Research-proposed operationalization

For falsification only, not source-reported trading rules:

- Form all signals only after the relevant bar and venue data are point-in-time available.
- Encode separately: single-venue OI extreme, cross-venue OI consensus extreme, funding extreme, and their conjunctions.
- Test high-OI consensus + positive funding and high-OI consensus + negative funding separately; do not collapse long and short crowding.
- Test both continuation and reversal forward-return hypotheses over multiple predeclared horizons rather than assuming an extreme must mean-revert.
- Treat low-OI / negative-z states separately from high-OI crowding; low outstanding leverage is not mechanically the inverse of high crowded leverage.

## Required data

- Crypto perpetual/swap instruments with point-in-time OI feeds.
- OI for Binance, OKX, Bybit, and the contemporaneous chart venue when available.
- Perpetual and relevant spot/index pricing needed to reproduce the source-compatible funding approximation.
- OHLCV for forward-return and price/OI-state controls.
- Venue identifiers and contract specifications.
- Bar timestamps and exchange publication/update timestamps.
- Point-in-time venue availability map: a venue missing OI must be distinguished from a non-extreme observation.
- Funding settlement conventions and units must be normalized across venues before comparison.

The source is chart-timeframe dependent; no single mandatory chart timeframe is stated in the reviewed description. This is an **underspecified** dimension.

## Execution assumptions

The source does not specify signal-to-order timing, market versus limit execution, fills, fees, spread, slippage, impact/capacity, leverage, margin, funding cash-flow accounting, latency, partial fills, or failures.

Any future test must use next-available-bar execution after signal formation, include fees/slippage and realized funding where relevant, and avoid same-bar knowledge unavailable at decision time. These are **research-proposed** assumptions, not source-reported rules.

## Evidence

### Source-reported

The source describes the indicator as a tool for detecting speculative leverage extremes and potential squeeze/liquidation reversal zones. It states that the 2025-12-29 update added multi-exchange OI consensus to reduce exchange-specific noise. The reviewed source does not provide a traceable Sharpe ratio, CAGR, drawdown, win rate, controlled out-of-sample test, or other independently auditable profitability result.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-reported controlled negative result was identified. Absence is not evidence of no negative result.

Mechanistically, an OI level z-score is not direction by itself: every open derivative position has counterparties, and elevated OI can accompany persistent trends rather than imminent liquidation. Funding can also remain extreme for prolonged periods. Cross-exchange consensus may therefore identify a leverage regime without determining the subsequent price direction.

## Falsification plan

1. **Incremental-information test:** compare the full consensus/funding construction against raw OI change, single-venue OI z-score, aggregate OI z-score, funding alone, funding z-score, price momentum, volatility, and volume. Reject added complexity if it provides no stable OOS information.
2. **Consensus ablation:** compare one-venue, any-two-venue, configurable minimum-count consensus, and simple cross-venue aggregate OI. The discrete vote must beat or add information to simpler aggregation to justify itself.
3. **Direction test:** evaluate reversal and continuation symmetrically after high positive and high negative OI z-score states. Reject any blanket reversal interpretation if continuation dominates or signs are unstable.
4. **Funding interaction:** test OI extreme alone, funding extreme alone, and OI × funding conjunctions. Require the interaction to add information beyond both marginal signals.
5. **Price/OI state control:** condition on price-up/OI-up, price-down/OI-up, price-down/OI-down, and price-up/OI-down states so the z-score is not credited for information already contained in contemporaneous price/OI direction.
6. **Parameter neighborhood:** test nearby OI lookbacks and z thresholds around source defaults (50 bars, ±2) without selecting a single ex-post optimum. Funding threshold neighborhoods must likewise be predeclared.
7. **Venue robustness:** leave-one-venue-out tests, explicit venue-availability tracking, and contract/unit normalization. Fail if the result is driven by one exchange or silent missing-data changes.
8. **Point-in-time audit:** reproduce actual OI/funding availability delays and funding settlement timing; fail any result that requires revised, synchronized, or future-known cross-venue observations.
9. **Walk-forward / regime robustness:** require stable sign and economically meaningful net-of-cost effect across bull, bear, high-volatility, low-volatility, and major deleveraging episodes.
10. **Complexity kill rule:** if multi-exchange consensus plus funding does not materially outperform a simpler OI/funding baseline OOS after costs, reject the composite layer rather than adding filters.

## Crypto portability

direct

The source is explicitly designed for crypto perpetual/swap markets. Portability still depends on venue-specific OI definitions, quote/contract units, funding methodology, funding intervals, fragmented liquidity, 24/7 candle boundaries, and point-in-time feed availability.

## Limitations

- Not independently reproduced.
- Indicator, not a fully specified trading strategy.
- Complete entry/exit/holding/sizing lifecycle is underspecified.
- Chart timeframe is underspecified.
- The funding calculation is source-specific and may differ from exchange-native realized funding.
- OI units and contract specifications differ across venues and require normalization.
- Multi-exchange consensus can be distorted by changing venue availability.
- OI extremes identify leverage state, not trader direction by themselves.
- Funding extremes may persist and need not immediately mean-revert.
- Source-reported reversal/squeeze interpretation is unverified.

## Implementation status

Research-only. No implementation in the research stack has been completed. No Qlib full backtest or independent reproduction has been performed.

## Adoption boundary

This record is normalized external research only. Its presence does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

- `tradingview-crypto-open-interest-bollinger-extremes-2026-09-23.md` — related OI-extreme family; Bollinger/statistical extreme construction without this source's cross-venue consensus + funding interaction.
- `crypto-perpetual-oi-rsi-fractal-divergence-funding-crowding-filter-2026-09-14.md` — related OI/funding family using OI-RSI and price/OI divergence rather than OI-level z-score breadth.
- `tradingview-binance-perpetual-oi-premium-divergence-veto-filter-2026-09-19.md` — related price/OI regime interpretation.
- `tradingview-multi-exchange-perp-spot-twap-funding-crowding-2026-09-21.md` — related multi-exchange funding/crowding construction without this source's OI-z consensus gate.

## Sources

1. sanbangaje. `Crypto Leverage Index(OI Norm. + FR)`. TradingView open-source script. Published 2025-12-11; multi-exchange OI consensus update 2025-12-29. Reviewed 2026-09-23. https://www.tradingview.com/script/WYQCG1z3-Crypto-Leverage-Index-OI-Norm-FR/
