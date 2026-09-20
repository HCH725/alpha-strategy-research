---
schema: strategy-research-record-v1
title: Pivot-Confirmed Orderflow Delta Divergence Alpha
created: 2026-09-21
updated: 2026-09-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-21
sources:
  - https://www.tradingview.com/script/E1ADFAMv-Pivot-Orderflow-Delta/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Pivot-Confirmed Orderflow Delta Divergence Alpha

## Provenance

Public TradingView open-source indicator **Pivot Orderflow Delta**, author/page identity `AustrianTradingMachine`, originally published 2025-11-01 and updated 2026-02-07. Stable source: https://www.tradingview.com/script/E1ADFAMv-Pivot-Orderflow-Delta/ . Source reviewed as of 2026-09-21.

Repository deduplication was performed against current `main` before capture by canonical TradingView source identity and normalized signal family. No record for this canonical source was found. Existing repository order-flow/CVD research is materially broader or uses different constructions; this record specifically tests **pivot-confirmed price versus continuous volume-profile-delta divergence**, including divergence-class and price/delta pivot-confluence structure.

## Economic mechanism

### Source-reported

The source constructs a continuous Cumulative Volume Profile Delta (CVPD) from lower-timeframe intrabar volume-profile estimates, then compares price pivots with delta pivots. It identifies Regular (Class A), Hidden (Class B), and Exaggerated (Class C) divergences, distinguishes price-only, delta-only, and simultaneous pivots, and maintains a dynamic `Impulse Start` baseline that updates when price pivots are confirmed. The source also exposes delta/volume agreement and disagreement observations.

The source explicitly states that pivots require right-side confirmation bars, creating lag, and that current unclosed bars update as new intrabar data arrives; signals should be considered final only after the main chart bar closes.

### Research interpretation

The falsifiable hypothesis is that **a confirmed mismatch between price structure and accumulated intrabar-estimated directional volume contains incremental information about subsequent returns beyond price pivots alone**.

Two competing mechanisms should be tested rather than assumed:

1. **Reversal / exhaustion:** regular or exaggerated divergence indicates that a new price extreme lacks corresponding directional-volume confirmation and therefore has elevated reversal probability.
2. **Continuation / hidden divergence:** hidden divergence indicates order-flow persistence beneath a price retracement and therefore elevated continuation probability.

The dynamic pivot baseline and price/delta pivot-confluence categories are candidate context variables, not presumed alpha. Their incremental contribution must survive ablation.

## Signal

Source-reported construction:

- For each chart bar, build a higher-resolution volume profile from a configurable lower intrabar timeframe.
- Use statistical/PDF allocation and a dynamic classifier to estimate buy versus sell pressure.
- Accumulate the estimated delta continuously into delta candles.
- Delta-candle open equals prior cumulative delta; close equals the new cumulative total; high/low represent intrabar cumulative-delta extrema.
- Confirm price and delta pivots only after the configured `Pivot Right Bars` have elapsed.
- Detect Regular (A), Hidden (B), and Exaggerated (C) divergences between price and delta-candle extrema.
- Classify pivots as price-only, delta-only, or simultaneous.
- Update the dynamic `Impulse Start` baseline when a new price pivot is confirmed.
- The 2026-02-07 source update added a selectable pivot algorithm and logarithmic-profile option.

The public description does not unambiguously specify the exact PDF allocation formula, dynamic buy/sell classifier, all pivot defaults, divergence thresholds, canonical entry/exit rules, holding period, re-entry logic, sizing, or executable portfolio mapping. These remain **underspecified**.

`research-proposed` operationalization for falsification only:

- Use only signals known after the main chart bar closes **and** after the required right-side pivot-confirmation bars have elapsed.
- Timestamp the signal at confirmation time, never at the historical pivot bar.
- Test each divergence class separately before any composite rule.
- Test price-only, delta-only, and simultaneous-pivot contexts as interaction terms rather than mandatory filters.
- Evaluate forward returns over predeclared horizons beginning after confirmation; do not backdate exposure to the pivot timestamp.

## Required data

- Crypto spot or perpetual OHLCV on the main decision timeframe.
- Lower-timeframe OHLCV / intrabar observations sufficient to reconstruct the source's volume-profile-delta approximation.
- Explicit timestamp, timezone, and chart/intrabar candle-boundary conventions.
- Point-in-time availability of all lower-timeframe observations used by each completed main bar.
- If using perpetuals: mark/index price and funding data for later executable tests.
- True aggressor-side trade data is not required by the TradingView source construction, but should be retained as an independent validation benchmark where available.

## Execution assumptions

The source is an indicator, not a complete trading strategy. It does not specify signal-to-order timing, order type, fill model, fees, spread, slippage, impact, leverage, funding, shorting, partial fills, or failures.

Any later executable test must label these independently as `research-proposed`. The minimum leakage-safe assumption is decision after pivot confirmation and completed main-chart bar, with execution no earlier than the next tradable observation.

## Evidence

### Source-reported

The source describes the CVPD construction, three divergence classes, dynamic pivot baseline, price/delta pivot-confluence markers, and explicit confirmation lag. It does not report a traceable Sharpe, CAGR, drawdown, win rate, or audited strategy backtest in the reviewed description, so none is claimed here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself identifies two material limitations: pivot signals are delayed by right-side confirmation, and current unclosed-bar intrabar values update dynamically. Those properties can create severe look-ahead/repainting errors if historical pivots are treated as tradable at the pivot bar.

No independent source-specific negative performance result was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

1. **Leakage-safe event timing:** reconstruct every pivot/divergence event at its actual confirmation timestamp. Reject any apparent edge that exists only when exposure is backdated to the pivot bar.
2. **Price baseline:** compare price-pivot reversal/continuation alone against price + CVPD divergence. Delta must add OOS information beyond the underlying price structure.
3. **Delta-construction ablation:** compare chart-bar volume proxies, lower-timeframe tick-rule delta where available, the reconstructed volume-profile delta, and true aggressor-side delta where available. Reject claims specific to CVPD if simpler or true-flow measures contradict it.
4. **Divergence-class separation:** test Regular A, Hidden B, and Exaggerated C separately with predeclared expected direction; do not select the best class after observing outcomes.
5. **Pivot-confluence ablation:** price-only versus delta-only versus simultaneous pivots. Reject the confluence layer if it does not improve OOS discrimination.
6. **Impulse-baseline ablation:** divergence-only versus divergence + dynamic `Impulse Start` context.
7. **Parameter robustness:** lower timeframe, profile rows, pivot-left/right confirmation, pivot algorithm, and logarithmic-profile option. Reject results dependent on a narrow parameter island.
8. **Placebo:** randomize delta sign within local blocks and timestamp-shift the delta series while preserving price pivots. The real alignment should outperform placebo distributions.
9. **Regime robustness:** trend/range, high/low volatility, high/low liquidity, and spot/perpetual samples.
10. **Execution robustness:** apply next-observation execution plus realistic fees, spread, slippage and funding where applicable.
11. **Failure criterion:** reject or materially weaken the hypothesis if CVPD divergence adds no stable OOS predictive value over price pivots alone, if performance disappears under confirmation-time accounting, or if results are not robust to reasonable delta/pivot constructions.

## Crypto portability

**direct** — the indicator is market-generic and the hypothesis can be tested directly on crypto OHLCV/intrabar data; no traditional-asset empirical result is being ported as crypto evidence.

Crypto-specific risks include 24/7 candle boundaries, venue fragmentation, heterogeneous reported volume, spot/perpetual microstructure differences, funding, thin intrabar data on smaller assets, and differences between TradingView's estimated directional volume and exchange-native aggressor-side trades.

## Limitations

- **underspecified:** exact statistical/PDF allocation, dynamic classification formula, all pivot defaults, divergence thresholds, entry/exit, holding, sizing and execution.
- **confirmation lag:** pivot signals are only known after right-side bars have elapsed.
- **intrabar repaint risk:** the source states current-bar values update until the chart bar closes.
- **proxy-data risk:** reconstructed directional volume is not equivalent to exchange-native aggressor-side trade classification.
- **not independently reproduced:** no replication was performed during this Scout run.
- **unproven:** no validated alpha or profitability is claimed.

## Implementation status

Not implemented in the research stack. No Qlib full backtest, survivor promotion, leaderboard entry, Paper, Testnet, or Live validation has occurred.

## Adoption boundary

Research-only. Presence in this repository does not mean the record passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor / leaderboard strategy, is profitable, or is approved for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

No stable Hermes Wiki Brain links are asserted from this GitHub-only Scout run.

## Sources

- TradingView — **Pivot Orderflow Delta**, `AustrianTradingMachine`, published 2025-11-01, updated 2026-02-07: https://www.tradingview.com/script/E1ADFAMv-Pivot-Orderflow-Delta/ (reviewed 2026-09-21).
