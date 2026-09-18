---
schema: strategy-research-record-v1
title: EMA-Slope RSI No-Trade-Zone Momentum Strategy
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - https://www.tradingview.com/script/RNxThUtE-EMA-Slope-RSI-Oscillator-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# EMA-Slope RSI No-Trade-Zone Momentum Strategy

## Provenance

Public TradingView open-source strategy **EMA Slope - RSI Oscillator Strategy** by **xvelox_**, originally published 2026-03-31 and showing updates through 2026-05-04 in the reviewed public page. Stable source URL: https://www.tradingview.com/script/RNxThUtE-EMA-Slope-RSI-Oscillator-Strategy/. Reviewed as of 2026-09-18.

## Economic mechanism

### Source-reported

The source combines a normalized long-moving-average slope with centered RSI. EMA slope is transformed with an arctangent normalization so its magnitude approaches a centered +/-50 scale comparable with RSI minus 50. A global No Trade Zone (NTZ) blocks new entries while slope momentum is weak. The source offers several entry modules, including NTZ crosses, slope acceleration, RSI divergence, slope-RSI divergence, and an RSI-slope oscillator, with entry-type-specific trailing management.

The source states that the NTZ is intended to suppress weak-momentum entries and that default values were tested on BTCUSDT 15-minute data. It also gives crypto-oriented guidance of faster moving averages (20/80) and an NTZ around 6-7, while emphasizing that parameter combinations should be backtested for each market and timeframe.

### Research interpretation

The primary falsifiable hypothesis is that normalized trend slope contains useful directional persistence only once its magnitude escapes a neutral region, while centered RSI can add timing information about momentum continuation or reversal. The NTZ is therefore a regime gate rather than a standalone alpha signal.

This record treats the strategy as a composite family rather than assuming every optional module contributes alpha. The economically cleanest base hypothesis for later ablation is: normalized EMA-slope regime gate + RSI/slope directional confirmation. Divergence, acceleration, stretch, higher-timeframe confirmation, and specialized exits should be tested as incremental components rather than presumed improvements.

## Signal

Source-reported structure:

- Trend/momentum state: change in a long moving average is normalized with an arctangent transform to a centered range asymptotically approaching +/-50.
- Momentum comparator: centered RSI is `RSI - 50`.
- Regime gate: when enabled, the global NTZ blocks all new entries while normalized slope is inside the neutral zone; exits remain possible.
- NTZ-cross entry module: entries may be generated when normalized slope crosses out of the NTZ.
- Acceleration module: the source scales absolute bar-to-bar slope change to a 0-50 range; values above a configurable threshold can trigger an acceleration setup. The page reports a default threshold of 38.
- RSI divergence module: pivot-based price/RSI divergence can produce reversal entries; the source describes a configurable sensitivity with lookback expressed as `16 - sensitivity`.
- RSI-slope oscillator module: arms when centered RSI crosses normalized slope outside the NTZ, then waits for RSI and slope to continue in the same direction within a timeout window.
- Position behavior: same-direction stacking is blocked; opposite-direction entries may reverse an existing position.
- Exit/risk logic: standard, divergence, and RSI-slope oscillator entries can use separate ATR-based trailing factors and grace periods. The source also describes optional NTZ re-entry and RSI-slope-cross exits.
- Source market guidance: BTCUSDT 15m is explicitly cited for default testing; crypto guidance includes 20/80 moving averages and NTZ 6-7.

The exact arctangent scaling formula, complete Boolean conditions for every optional entry module, all current default inputs, position-sizing formula, and exact order-fill semantics are underspecified in the reviewed public description. They must not be inferred from the prose.

## Required data

- OHLCV bars for the traded instrument.
- Moving-average and RSI inputs derived point-in-time from completed bars.
- True range / ATR inputs for trailing management when enabled.
- Pivot history for divergence modules when enabled.
- Optional higher-timeframe bars if trend confirmation is enabled.
- BTCUSDT 15m is the explicitly cited crypto test context; the source also discusses other markets and timeframes.
- Point-in-time handling is mandatory for pivot/divergence features so future pivot confirmation is not leaked backward into the signal timestamp.

No order-book, trade-aggressor, funding, open-interest, or options data is specified by the source.

## Execution assumptions

The source describes strategy signals and trailing management but does not establish a realistic exchange fill model. Exact signal-to-order timing, same-bar versus next-bar fills, order type, spread, slippage, market impact, fees, funding, leverage/margin, latency, partial fills, and venue-specific execution behavior are underspecified.

Any later implementation of those items is `research-proposed` unless directly recovered from the primary source code and provenance-preserved.

## Evidence

### Source-reported

The source states that default values were tested on BTCUSDT 15m and supplies market/timeframe guidance, but the reviewed public description does not provide a traceable Sharpe ratio, CAGR, drawdown, win rate, or other performance statistic suitable for recording as evidence here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself acknowledges market-specific parameter adjustment and recommends backtesting combinations for the target market/timeframe. The multi-module design also creates substantial overfitting and multiple-testing risk: apparent performance can arise from selecting among NTZ, acceleration, divergence, oscillator, filters, and entry-specific exit parameters after observing the sample.

Pivot-based divergence additionally carries a point-in-time risk because a pivot requires future-bar confirmation unless signal timing is handled explicitly.

## Falsification plan

1. Implement a minimal point-in-time base model first: normalized EMA slope + NTZ + centered-RSI directional confirmation. Do not begin with every optional module enabled.
2. Verify signal timestamps, especially divergence pivots, against a causal bar-by-bar implementation.
3. Test BTCUSDT 15m over multiple non-overlapping regimes with fees, spread, slippage, and perpetual funding where applicable.
4. Compare against simple controls: moving-average trend following alone, RSI alone, and slope without the NTZ.
5. Ablate the NTZ, RSI confirmation, acceleration, divergence, higher-timeframe trend filter, and each specialized exit independently.
6. Require out-of-sample stability across neighboring MA/NTZ settings rather than accepting a single optimized parameter point.
7. `research-defined falsification threshold`: reject the incremental module if its out-of-sample risk-adjusted performance fails to improve the simpler parent after realistic costs or if its advantage disappears under nearby parameter perturbations.

## Crypto portability

direct

The cited source explicitly discusses crypto settings and BTCUSDT 15m. Portability still depends on venue-specific OHLCV, 24/7 candle boundaries, spot-versus-perpetual differences, fees, spread/slippage, and funding for perpetual contracts.

## Limitations

- Not independently reproduced.
- Exact normalized-slope formula and several module-level Boolean rules are underspecified in the reviewed prose.
- Complete current default parameter set is not reconstructed here.
- Execution and transaction-cost assumptions are underspecified.
- Divergence modules require explicit causal pivot timing.
- Many optional modules and tunable parameters create material data-snooping / overfitting risk.
- Source-reported BTCUSDT testing is not independent evidence of robust alpha.

## Implementation status

Not implemented in our research stack. No independent backtest, robustness test, paper-trading test, testnet test, or live validation has been performed for this record.

## Adoption boundary

Research material only. Presence in this repository does not mean profitable, validated alpha, approved for implementation, approved for paper trading, approved for testnet, or approved for live trading.

## Related Wiki records

No stable related Wiki record identified in this GitHub-only Scout cycle.

## Sources

- TradingView — **EMA Slope - RSI Oscillator Strategy**, xvelox_: https://www.tradingview.com/script/RNxThUtE-EMA-Slope-RSI-Oscillator-Strategy/ (public open-source strategy; reviewed 2026-09-18)
