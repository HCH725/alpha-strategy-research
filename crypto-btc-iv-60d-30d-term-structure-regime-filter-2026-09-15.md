---
schema: strategy-research-record-v1
title: "BTC 60D-30D Implied-Volatility Term-Structure Regime Filter"
created: 2026-09-15
updated: 2026-09-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - options
  - volatility
status: research-only
confidence: medium
source_as_of: 2026-09-15
sources:
  - https://www.tradingview.com/script/DXWQJLmZ-BTC-IV-Term-Structure-60D-30D/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BTC 60D-30D Implied-Volatility Term-Structure Regime Filter

## Provenance

Public TradingView open-source indicator **BTC IV Term Structure (60D - 30D)** by **LeafAlgo**, published August 20, reviewed 2026-09-15. Stable public source: https://www.tradingview.com/script/DXWQJLmZ-BTC-IV-Term-Structure-60D-30D/ . The TradingView page identifies the script as open-source and describes its intended use as a volatility-regime/context filter rather than a standalone entry system.

Pre-write repository search found no record for TradingView source identity `DXWQJLmZ`. Materially related records include `crypto-options-volatility-risk-premium-zscore-2026-08-31.md` (IV minus realised-volatility premium), `crypto-options-dvol-iv-premium-shock-spot-predictor-2026-09-13.md` (DVOL shock / IV-RV directional hypothesis), and `crypto-futures-term-structure-roll-yield-carry-2026-08-31.md` (futures-price curve carry). This record is distinct because its signal variable is the **cross-tenor BTC options implied-volatility slope, 60D IV minus 30D IV**, not IV-RV spread, a single-tenor DVOL shock, or futures basis.

## Economic mechanism

### Source-reported

The source interprets positive 60D-minus-30D IV as contango/calm conditions in which longer-dated uncertainty is priced above near-term uncertainty. Negative spread is described as backwardation: near-term implied volatility has become richer than longer-dated volatility, consistent with an active stress event such as a selloff, macro catalyst, or liquidation cascade. It further claims that unusually deep backwardation tends to mean-revert after the catalyst clears, while unusually strong contango can represent complacency before volatility expands.

The author recommends the indicator primarily as a **filter layered on another entry signal**, not as a standalone trade trigger. An extreme-backwardation state accompanying an independent long signal is described as corroborating a fear/mean-reversion setup; extreme contango is described as a reason to avoid aggressive new long exposure.

### Research interpretation

The falsifiable hypothesis is that the BTC options term-structure slope contains incremental state information beyond spot OHLCV and single-tenor implied volatility. A negative 60D-30D slope represents concentrated demand for near-term convexity/insurance; an extreme negative slope may identify forced-risk-transfer episodes whose spot impact subsequently mean-reverts. Conversely, unusually positive slope may identify underpriced near-term event risk or complacency.

This is a **regime/filter hypothesis**, not yet a complete trading strategy. The incremental research question is whether conditioning an independently specified directional signal on the term-structure state improves out-of-sample expectancy after costs without merely selecting high-volatility rebounds ex post.

## Signal

**Signal status: underspecified.** The public source describes the construction and qualitative use but does not expose enough parameter detail in the reviewed page text to reconstruct every operational field without guessing.

- **Primary variable [source-reported]:** `spread_t = IV_60D,t - IV_30D,t` for Bitcoin implied volatility.
- **Regime [source-reported]:** spread above zero = contango; spread below zero = backwardation.
- **Extreme state [source-reported]:** raw spread outside its rolling mean plus/minus one standard-deviation band. The reviewed source text does not state the exact rolling window.
- **Transition context [source-reported]:** an EMA smooths the raw spread; crossing from below zero to above zero or vice versa is described as a regime transition. The reviewed source text does not state the EMA length.
- **Percentile context [source-reported]:** last-bar percentile rank contextualizes the spread against approximately the prior year; exact bar-count/window implementation is not stated in the reviewed source text.
- **Directional use [source-reported]:** extreme backwardation may corroborate a separate long signal; extreme contango may veto aggressive long exposure. The separate directional signal is not defined by this source.
- **Formation timestamp / tradability:** underspecified. The page does not state the exact IV feed, update timestamp, timezone, or whether decisions must wait for a confirmed bar.
- **Entry / exit / holding / rebalance / sizing:** underspecified because the source explicitly presents this as context/filter logic rather than a standalone entry/exit strategy.
- **Scout operationalization:** none. No missing entry, exit, holding period, EMA length, rolling window, or percentile rule is silently supplied.

## Required data

- **Instrument / market:** Bitcoin options-implied volatility term structure.
- **Required fields [source-reported]:** 30-day BTC implied volatility and 60-day BTC implied volatility.
- **Venue / vendor / exact TradingView symbols:** underspecified in the reviewed public page text; these must be recovered from the public Pine source or independently defined before implementation.
- **Timeframe:** underspecified; the page does not declare a mandatory host-chart timeframe.
- **Point-in-time requirement:** both tenor observations must be available at the signal timestamp with no future interpolation or revised data leaking backward.
- **Timestamp / timezone:** underspecified.
- **Missing data:** source does not specify stale/missing-tenor handling. No imputation should be assumed.
- **Costs:** a regime filter itself does not trade, but any downstream strategy must model the actual traded instrument's fees, spread, slippage, funding/borrow where applicable, and latency.

## Execution assumptions

The source does not specify order type, fill model, latency, leverage, margin, participation cap, slippage, spread, impact, partial-fill handling, or failure handling because the indicator is not presented as a standalone execution strategy.

Any later experiment must freeze a separate base strategy first, form the IV filter only from point-in-time available data, and apply the filter before the base strategy's order decision. Choosing next-bar execution, same-bar execution, or any specific cost model would be **research-proposed**, not source-reported.

## Evidence

### Source-reported

The TradingView author qualitatively reports that deep negative spread/extreme backwardation tends to mean-revert after the catalyst clears and that extreme positive spread can mark complacency preceding volatility expansion. The page does **not** provide a traceable backtest sample, return series, Sharpe ratio, CAGR, drawdown, hit rate, transaction costs, or out-of-sample statistics. Those qualitative statements therefore remain hypotheses, not verified performance evidence.

### Independently reproduced

not independently reproduced

### Negative evidence

No direct negative empirical result is reported on the reviewed TradingView page. However, the source explicitly warns by construction that the indicator should be used as context rather than a standalone entry trigger, and it does not provide performance evidence. `none identified in the reviewed sources; absence is not evidence of no negative result`.

## Falsification plan

1. **Incremental-filter OOS test.** Data: point-in-time BTC 30D and 60D IV plus a pre-frozen BTC directional baseline. Sample: multiple bull, bear, crash, and low-volatility regimes with chronological train/test separation. Metric: net OOS Sharpe and mean trade return of baseline versus baseline+filter. **Research-defined falsification threshold:** reject incremental alpha if the filter does not improve OOS Sharpe by at least 0.10 and does not improve net mean trade return in the held-out sample.
2. **Term-structure versus level ablation.** Compare `IV60-IV30` against 30D-IV level alone, 60D-IV level alone, and a realised-volatility control. **Research-defined falsification threshold:** weaken the mechanism if the slope adds no incremental predictive information after controlling for IV level and realised volatility.
3. **Parameter perturbation.** Test plausible rolling-band, EMA, and percentile windows only after the source defaults are recovered; perturb each by ±25%. **Research-defined falsification threshold:** reject a parameter-specific edge if sign or economic magnitude collapses under neighboring windows.
4. **Placebo timing test.** Shift the term-structure state forward/backward by several bars and compare to the causal version. **Research-defined falsification threshold:** reject if future-shifted/non-causal variants materially outperform the point-in-time signal, indicating alignment or leakage problems.
5. **Venue/data-source robustness.** Reconstruct comparable 30D/60D ATM IV from an independent crypto-options source where feasible. **Research-defined falsification threshold:** weaken the thesis if regime labels materially disagree at major stress events or results exist only on one vendor construction.
6. **Cost/latency stress.** Apply realistic fees, spread, slippage and one-bar signal latency to the downstream traded strategy. **Research-defined falsification threshold:** reject tradability if any apparent incremental return is erased under conservative executable costs.
7. **Regime breakdown.** Evaluate crisis, trending bull, trending bear, and low-volatility periods separately. **Research-defined falsification threshold:** reject a claimed general filter if all benefit is concentrated in one isolated episode without stability elsewhere.

Failure means the filter remains descriptive volatility context only and must not advance toward implementation/adoption on the basis of this record.

## Crypto portability

**direct.** The source is explicitly a Bitcoin implied-volatility term-structure indicator. Crypto-specific risks include 24/7 timestamp alignment, options-market concentration/fragmentation, changing maturity liquidity, interpolation methodology for constant 30D/60D tenors, stablecoin/USD quote differences, and venue-specific index construction. If the eventual traded leg is a perpetual rather than spot, funding and mark/index conventions must also be modeled.

## Limitations

- `underspecified`: exact 30D/60D TradingView symbols or IV vendor, rolling-band window, EMA length, percentile implementation, formation timestamp, and confirmed-bar convention were not available in the reviewed page text.
- `underspecified`: no standalone entry, exit, holding period, rebalance cadence, sizing, or execution model is defined.
- `not independently reproduced`.
- No source-reported quantitative performance sample or OOS evidence.
- The qualitative term-structure narrative can be confounded by the absolute IV level, scheduled events, maturity interpolation, and option-liquidity changes.
- A filter can appear beneficial through data-snooping if the base strategy or thresholds are retuned after observing filtered results; the base strategy and acceptance criteria must be frozen before testing.

## Implementation status

`not-implemented`. No implementation, backtest, runtime modification, Paper, Testnet, or Live verification was performed by this Scout cycle.

## Adoption boundary

`research-only`; `adoption: not-approved`; `approval_scope: research-only`. This record captures a public hypothesis for later research. It does not establish profitable alpha, authorize implementation, or permit Paper/Testnet/Live use.

## Related Wiki records

No stable Hermes Wiki Brain path was fabricated. Materially related staging records reviewed for deduplication:

- `crypto-options-volatility-risk-premium-zscore-2026-08-31.md`
- `crypto-options-dvol-iv-premium-shock-spot-predictor-2026-09-13.md`
- `crypto-futures-term-structure-roll-yield-carry-2026-08-31.md`

## Sources

- LeafAlgo, **BTC IV Term Structure (60D - 30D)**, TradingView public open-source indicator, published August 20, reviewed 2026-09-15: https://www.tradingview.com/script/DXWQJLmZ-BTC-IV-Term-Structure-60D-30D/
