---
schema: strategy-research-record-v1
title: OI + Funding Z-Score Extreme Reversal
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-20
sources:
  - https://www.tradingview.com/script/1Jcmc88C/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# OI + Funding Z-Score Extreme Reversal

## Provenance

Public TradingView open-source script **oi + funding oscillator cryptosmart**, author/page identity `edwardflores194`, published 2025-09-16. Stable source: https://www.tradingview.com/script/1Jcmc88C/ . Source reviewed as of 2026-09-20.

Repository deduplication before capture found no record citing this canonical TradingView source. Search also found no materially identical record explicitly normalizing the joint interaction of OI rate-of-change and funding into one smoothed z-score extreme oscillator with threshold-exit reversal logic. Adjacent repository records using OI, funding, OI-RSI, or aggregated funding remain distinct hypotheses/data constructions.

## Economic mechanism
### Source-reported

The author describes the oscillator as a crypto-derivatives sentiment tool combining the rate of change in Open Interest (OI) with Funding Rates, normalizing the combination with a z-score and smoothing it around zero. Upper extremes are described as overheated/high-leverage conditions with risk of a long squeeze; lower extremes are described as panic/deleveraging conditions with potential for a market bottom. The source presents a cross back below the upper critical zone as a potential sell signal and a cross back above the lower critical zone as a potential buy signal. It states that 1-hour and 4-hour charts showed the highest effectiveness, while lower timeframes are better used as confirmation. These are source-reported claims, not independently verified results.

### Research interpretation

The falsifiable hypothesis is that **joint leverage expansion/contraction (OI change) and carry/crowding pressure (funding) contain interaction information that improves short-horizon reversal conditioning beyond either input alone**. The proposed mechanism is crowded positioning followed by partial exhaustion or deleveraging: an extreme composite state alone is not the event; the source's threshold-exit condition attempts to wait for the extreme to begin normalizing.

A competing hypothesis is continuation: strongly positive/negative composite states may simply identify persistent directional regimes rather than exhaustion. A third possibility is that the oscillator is only a volatility/crowding proxy with no directional information.

## Signal

Source-supported normalized logic:

- Inputs: OI rate of change and Funding Rate.
- Transformation: the two inputs are blended into a z-score-normalized, smoothed oscillator around zero.
- Long candidate: oscillator exits the lower critical/oversold zone by crossing upward through its lower threshold.
- Short candidate: oscillator exits the upper critical/overheated zone by crossing downward through its upper threshold.
- Source-preferred context: 1h and 4h; lower timeframes are described as confirmation use rather than standalone signals.

**Underspecified by the public source description:** exact OI lookback, exact z-score lookback, exact blend/weighting equation, smoothing function/length, critical-zone numerical thresholds, funding venue/symbol construction, signal-to-order timing, exit, holding period, re-entry, position sizing, and stop/target rules.

Any later selection of those missing values is `research-proposed` and must not be represented as source logic.

## Required data

- Crypto perpetual/futures market with point-in-time OI and funding observations.
- Timestamp-aligned OI and funding series at the tested signal timeframe.
- OHLCV for forward-return measurement and execution simulation.
- Venue and contract identifiers sufficient to prevent mixing economically different contracts.
- Funding observations must distinguish realized/settled values from predicted/current values if the provider exposes both.
- OI observations must be available as they were known at each signal timestamp; revised or future-filled data are not acceptable.

The TradingView page does not unambiguously specify the exact venue set or data symbols used by the script; this is a data gap that must be resolved from a reproducible implementation before testing.

## Execution assumptions

The source describes signal states rather than a complete executable strategy. It does not specify same-bar versus next-bar fills, market/limit orders, fees, spread, slippage, impact, funding cash flows, leverage/margin, partial fills, or capacity.

For research, execution must therefore be modeled separately and labeled `research-proposed`. A conservative baseline should form the signal only from information available at bar close and execute no earlier than the next tradable observation; this is a research control, not a source-reported rule.

## Evidence
### Source-reported

The source states that the oscillator is most effective on 1h and 4h and describes lower-timeframe use as a confluence factor. No traceable Sharpe, CAGR, drawdown, win rate, sample period, trade count, or formal backtest statistic is provided on the reviewed public page, so no quantitative performance claim is recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No formal negative empirical result is reported on the reviewed source page. The author explicitly warns that lower timeframes contain more noise and recommends not using those signals in isolation. Absence of other negative evidence is not evidence of robustness.

## Falsification plan

1. Reconstruct a leakage-safe composite only after the exact public-source calculation can be independently resolved; otherwise test clearly labeled `research-proposed` variants without claiming source replication.
2. Compare composite threshold-exit signals against OI-change-only, funding-only, price momentum/reversal, realized-volatility, and random-timestamp controls.
3. Component ablation: OI only -> funding only -> equal-weight normalized combination -> source-faithful combination if reconstructable. The composite thesis fails if it does not add stable out-of-sample information beyond the strongest single component.
4. Competing direction test: measure both reversal and continuation returns after upper/lower extreme exits. Reject the reversal interpretation if sign-adjusted reversal performance is not distinguishable from controls after costs.
5. Test 1h and 4h separately, then lower timeframes only as robustness checks; do not pool horizons to manufacture significance.
6. Use walk-forward/OOS evaluation with thresholds and normalization parameters fitted only on prior data. Include bull, bear, sideways, high-volatility, and deleveraging regimes.
7. Audit funding timestamps/settlement conventions and OI availability. Any future-filled funding/OI or use of a final-bar value before it was observable invalidates the result.
8. Apply realistic fees, spread, slippage, and actual funding cash flows. If the edge disappears under plausible costs, reject it as tradable alpha.
9. Test venue robustness where comparable OI/funding history exists; failure outside one venue should materially lower confidence in a market-wide crowding interpretation.

## Crypto portability

direct

The source is explicitly designed for crypto derivatives. Portability is still contract- and venue-sensitive because funding methodology, settlement cadence, OI denomination, contract type, and data availability differ across exchanges. A signal built from one venue must not be silently interpreted as market-wide positioning.

## Limitations

- `underspecified`: exact composite formula, weights, lookbacks, smoothing, thresholds, venue set, and full trading lifecycle are not exposed in the reviewed page text.
- `not independently reproduced`: no local or repository backtest was performed by this Scout.
- `data gap`: precise TradingView derivative symbols and historical availability require resolution before source-faithful implementation.
- Source statements about preferred timeframes are qualitative and unsupported by traceable performance statistics on the reviewed page.
- Z-score extremes can be regime-dependent; fixed thresholds may drift as leverage structure and funding conventions change.
- OI direction does not identify long versus short initiators by itself; causal labels such as "new longs" or "new shorts" require additional evidence.

## Implementation status

Research capture only. No implementation or backtest in the quantitative research stack has been completed.

## Adoption boundary

This record is research material only. It is not evidence of profitability, validated alpha, implementation approval, paper-trading approval, testnet approval, or live-trading approval.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted by this GitHub-only Scout.

## Sources

- TradingView — **oi + funding oscillator cryptosmart**, `edwardflores194`, published 2025-09-16; reviewed 2026-09-20: https://www.tradingview.com/script/1Jcmc88C/
