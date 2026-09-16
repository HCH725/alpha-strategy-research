---
schema: strategy-research-record-v1
title: "TradingView Choppiness-Gated Donchian Breakout Filter"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-16
sources:
  - https://www.tradingview.com/script/tH2V90Ay-Choppiness-Breakout-Filter-forexobroker/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Choppiness-Gated Donchian Breakout Filter

## Provenance

Public TradingView open-source indicator by `forexobroker`, titled **Choppiness Breakout Filter [forexobroker]**, published May 24 (TradingView page observed 2026-09-16). Stable public source URL: https://www.tradingview.com/script/tH2V90Ay-Choppiness-Breakout-Filter-forexobroker/ . This record normalizes the published description rather than reproducing the Pine source.

## Economic mechanism

### Source-reported

The source gates Donchian-channel breaks with the Choppiness Index (CI): a Donchian break is eligible when CI classifies the market as trending and is suppressed when CI classifies the market as choppy. It also supports a second entry mode in which a qualifying breakout establishes directional bias and a later close crossing a reclaim EMA triggers the signal.

### Research interpretation

The falsifiable hypothesis is that breakout continuation is conditional on recent directional structure. A prior-bar Donchian break supplies the price-discovery event, while low CI acts as a regime filter intended to remove range-bound breaks. In the optional reclaim mode, the EMA cross delays entry until price reasserts direction after the breakout. The key incremental question is whether the CI gate improves net breakout quality relative to an otherwise identical Donchian baseline rather than merely reducing trade count.

## Signal

Source-reported logic:

- Compute CI over `Choppiness Length`, default 14: `100 * log10(sum(true range, length) / (highest high - lowest low)) / log10(length)`.
- Trending regime: CI below `Trend CI Threshold`, default 45.0.
- Choppy regime: CI above `Chop CI Threshold`, default 61.8; entering this regime resets directional bias to flat.
- Build the Donchian breakout levels from the **prior bar's** highest high / lowest low over `Breakout Lookback`, default 20. This makes the broken level fixed before the confirming bar.
- Up-break: trending regime and current close above prior-bar Donchian high; sets bias `+1`.
- Down-break: trending regime and current close below prior-bar Donchian low; sets bias `-1`.
- `Break-Only` mode: the confirmed filtered break bar itself is the signal.
- Reclaim mode: with prevailing `+1` bias, long signal occurs when close crosses above the reclaim EMA; with `-1` bias, short signal occurs when close crosses below it. Default reclaim EMA length is 9.
- Signals require bar-close confirmation, position not already locked in the same direction, and the cooldown to have elapsed. Default cooldown is 5 bars.
- Optional session restriction exists; it is off by default.

The source describes signal/position locking but does not specify a complete executable portfolio exit, stop-loss, profit target, sizing, or reversal accounting contract. Those elements are therefore **underspecified** and must not be invented during later implementation.

## Required data

- OHLCV bars for the selected TradingView instrument and timeframe.
- High/low/close sufficient for Donchian levels and CI range.
- True range inputs, requiring high/low and prior close.
- Timestamps/session information only if the optional session restriction is enabled.
- Point-in-time requirement: Donchian extremes must exclude the current signal bar exactly as described by the source; CI and EMA must use only information available through the confirmed signal-bar close.

The source does not require funding, order book, open interest, or options data.

## Execution assumptions

Source-reported signal timing is bar-close confirmation (`barstate.isconfirmed`), so signals are acknowledged only after the break/reclaim bar closes. The source does not specify actual order type, next-bar versus close-price fill, fees, spread, slippage, market impact, funding, leverage, margin, partial fills, or latency. These are **underspecified** and must be explicit in any future backtest rather than silently defaulted.

## Evidence

### Source-reported

The TradingView publication describes the rule mechanics and limitations but does not provide a traceable performance statistic that is suitable for promotion here as verified evidence.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source explicitly notes that CI is a filter rather than a predictor; the first CI-length bars are unreliable warm-up, default thresholds may require retuning in very low/high volatility regimes, and bar-close confirmation introduces lag. The repository also contains broader negative evidence that simple technical breakout families can fail null-control testing; this record therefore treats the CI gate as an empirical hypothesis, not established alpha.

## Falsification plan

Research-defined falsification tests:

1. Compare the CI-gated Donchian rule against the same Donchian breakout without the CI gate using identical universe, timestamps, execution, costs, and parameter schedule.
2. Run an ablation of Break-Only versus EMA-reclaim entry while preserving the same breakout/bias definition.
3. Test the published defaults without retrospective optimization first: CI length 14, trend threshold 45.0, chop threshold 61.8, Donchian lookback 20, reclaim EMA 9, cooldown 5.
4. Require leakage-safe out-of-sample evaluation across multiple crypto market regimes and liquid symbols/timeframes.
5. Stress fees, spread, slippage, and perpetual funding where applicable.
6. Treat the hypothesis as weakened if the CI gate fails to improve a predeclared risk-adjusted or cost-adjusted metric versus the ungated Donchian control, or if any apparent advantage disappears out of sample. Exact acceptance thresholds are research-defined and must be declared before the test, not selected after observing results.

## Crypto portability

**unproven**. The signal uses standard OHLCV-derived features and is mechanically portable to liquid crypto spot or perpetual bars, but the cited TradingView source does not establish crypto-specific empirical alpha. A crypto test must account for 24/7 candle boundaries, venue-specific volume/liquidity, fees, slippage, and perpetual funding when relevant.

## Limitations

- Not independently reproduced.
- Complete trade exit and portfolio accounting are underspecified.
- CI thresholds are source defaults, not demonstrated universal constants.
- Bar-close confirmation can materially change fills versus intrabar breakout assumptions.
- A lower number of false-looking breaks is not itself evidence of higher net alpha; trade-count reduction and regime exposure must be controlled in comparison.
- Crypto profitability is unproven.

## Implementation status

Research record only. No implementation or backtest in the user's quantitative research stack has been completed as part of this Scout cycle.

## Adoption boundary

`research-only`; `not-implemented`; `not-approved`. Presence in this repository does not imply validated alpha or approval for implementation, paper trading, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain link was verified in this GitHub-only Scout cycle; none is fabricated.

## Sources

- TradingView — forexobroker, **Choppiness Breakout Filter [forexobroker]**: https://www.tradingview.com/script/tH2V90Ay-Choppiness-Breakout-Filter-forexobroker/ (public open-source script page; observed 2026-09-16).
