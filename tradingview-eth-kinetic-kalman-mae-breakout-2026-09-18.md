---
schema: strategy-research-record-v1
title: ETH Kinetic Kalman MAE Breakout
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
  - https://www.tradingview.com/script/nd8EpyQ5-Kinetic-Kalman-Breakout/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ETH Kinetic Kalman MAE Breakout

## Provenance

Public TradingView open-source strategy: **Kinetic Kalman Breakout**, author `egoigor1976`, published Mar 17, source identity `nd8EpyQ5`. Stable source: https://www.tradingview.com/script/nd8EpyQ5-Kinetic-Kalman-Breakout/. Source reviewed as of 2026-09-18.

The reviewed TradingView page describes the strategy logic and selected parameters but does not expose enough formula detail in its prose to reproduce the complete Kalman implementation exactly from this record alone.

## Economic mechanism

### Source-reported

The author describes an adaptive Kalman filter as an estimate of underlying price trend that separates random volatility from trend. Adaptive volatility bands are constructed around that estimate using Mean Absolute Error (MAE). A close beyond a band is treated as a volatility breakout, and the strategy remains continuously positioned, reversing when the detected trend phase changes.

### Research interpretation

Hypothesis: a state-space trend estimate can reduce short-horizon observation noise while an MAE-scaled envelope normalizes breakout distance to recent forecast error. A close outside that adaptive envelope may therefore identify a persistent directional displacement rather than ordinary noise. The falsifiable contribution is the combination of Kalman trend estimation and MAE-normalized breakout boundaries; neither component should be assumed to add alpha without ablation.

Component roles:

- Regime/trend estimate: adaptive Kalman filtered price.
- Primary signal: close crossing outside the MAE-derived volatility envelope.
- Position behavior: always-in-market directional state, flipping when the opposite phase is triggered.

## Signal

Source-reported logic:

- Target configuration: ETH/USDT on 15-minute bars.
- Trend/reference series: adaptive Kalman-filter estimate of price.
- Envelope: adaptive volatility bands around the Kalman estimate using MAE.
- Band lookback: 200 bars.
- Long entry/state: price closes above the upper volatility band.
- Short entry/state: price closes below the lower volatility band.
- Position behavior: always in market; flip position when the trend phase changes.
- The source says process-noise settings are calibrated for ETH medium-term momentum but the reviewed prose does not state their numerical values.

Underspecified from the reviewed source prose:

- exact Kalman state-transition and observation equations;
- process-noise and measurement-noise values/formulas;
- exact MAE formula and band multiplier;
- whether opposite-band crossing is the sole reversal condition in the implementation;
- precise order-fill timing after the qualifying close.

No missing parameter or execution rule is inferred here. Any later choice needed to operationalize an underspecified field must be labeled `research-proposed`.

## Required data

Minimum source-supported inputs are ETH/USDT 15-minute OHLC price bars sufficient to calculate the Kalman estimate and 200-bar MAE envelope. The source page does not identify a required venue, spot-versus-perpetual market type, volume input, funding input, or order-book input.

Point-in-time implementation must use only information available at each completed signal bar. Venue, market type, candle-boundary convention, and missing-data handling remain data gaps unless established from the implementation or chosen later as research-proposed test conditions.

## Execution assumptions

Source-reported money-management settings are initial capital USD 10,000, fixed USD 1,000 order size, and 0.05% commission. These are source-reported test settings, not evidence that they are appropriate for deployment.

The page specifies signals on price closes beyond the adaptive bands but does not unambiguously state same-close versus next-bar fills, order type, spread, slippage, market impact, funding, leverage/margin, partial-fill handling, latency, or failure handling. These remain underspecified. A causal backtest execution convention would need to be introduced explicitly as `research-proposed` rather than attributed to the source.

## Evidence

### Source-reported

The author states that the ETH/USDT 15-minute parameterization was tuned using an extensive backtest of more than 200,000 candles spanning more than six years. The reviewed page does not provide sufficient independent evidence here to treat that tuning statement as validation, and this record does not reproduce any performance statistic.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source describes parameters as specifically tuned for ETH/USDT 15-minute data, creating an explicit overfitting/portability concern. Always-in-market reversal can also make the strategy sensitive to transaction costs and whipsaw during non-trending regimes. No independent negative study was reviewed in this Scout cycle; absence is not evidence of robustness.

## Falsification plan

Test the source-supported ETH/USDT 15-minute hypothesis with point-in-time signals and realistic costs, separating development and untouched out-of-sample periods. Compare against simple baselines such as buy-and-hold and a conventional trend/breakout rule.

Required ablations should isolate: (1) Kalman estimate versus a simpler moving trend estimate, and (2) MAE-adaptive bands versus a conventional volatility envelope. The hypothesis is materially weakened if any apparent advantage disappears out of sample, after realistic turnover costs, or when the Kalman/MAE components fail to improve on simpler baselines. Any numerical acceptance cutoff selected during testing is a `research-defined falsification threshold`, not a source claim.

## Crypto portability

**direct** for the source-stated ETH/USDT 15-minute research configuration because the source explicitly targets that crypto pair.

Portability beyond the source configuration is unproven. Spot versus perpetual implementation, venue fragmentation, 24/7 candle boundaries, funding, mark/index pricing, liquidity and fee schedules can materially change results and must be specified in later experiments.

## Limitations

- `underspecified`: exact Kalman equations and noise parameters are absent from the reviewed prose.
- `underspecified`: exact MAE envelope construction and multiplier are absent from the reviewed prose.
- `underspecified`: exact fill timing and several execution assumptions are absent.
- `not independently reproduced`: no Scout backtest or code reproduction was performed.
- `unproven`: source-described tuning on ETH/USDT 15-minute history may not generalize out of sample or to other markets.

## Implementation status

Not implemented in the research stack. No Qlib, paper, testnet, or live verification has been performed by this Scout.

## Adoption boundary

Research-only. Presence in this repository does not establish profitability, validated alpha, implementation approval, paper/testnet approval, or live-trading approval.

## Related Wiki records

None identified with a stable Wiki path during this GitHub-only Scout cycle. No Wiki lookup was performed.

## Sources

- TradingView — egoigor1976, **Kinetic Kalman Breakout**, public open-source strategy, published Mar 17; reviewed 2026-09-18: https://www.tradingview.com/script/nd8EpyQ5-Kinetic-Kalman-Breakout/
