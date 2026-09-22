---
schema: strategy-research-record-v1
title: Bitcoin CME Weekend Gap First-Touch Fill Hypothesis
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-22
sources:
  - https://www.tradingview.com/script/9dIsa3gG-BTC-CME-Gap-detector-single-signals/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin CME Weekend Gap First-Touch Fill Hypothesis

## Provenance

Public TradingView open-source script **BTC CME Gap – detector & single signals** by `Greg_deVril`, published 2025-08-25. Stable source: https://www.tradingview.com/script/9dIsa3gG-BTC-CME-Gap-detector-single-signals/ . Source reviewed as of 2026-09-22.

The source defines a Bitcoin CME weekend gap from `CME:BTC1!` daily data using Monday open versus the previous Friday close, with `barmerge.lookahead_off`. It turns the gap into a zone and emits one-time `ENTER` and `FILL` events. No source-reported backtest statistics were identified on the reviewed page.

## Economic mechanism

### Source-reported

The author describes CME weekend gaps as potential price "magnets" associated with mean reversion, stop-runs, or liquidity grabs. The page notes that outcomes can include a quick Monday fill, a staged fill after partial rejection, or a delayed fill during later consolidation. These are source-reported interpretations, not verified empirical facts.

### Research interpretation

The falsifiable hypothesis is narrower: after BTC first re-enters a newly formed CME weekend gap, price may have conditional continuation toward the prior Friday CME close beyond an unconditional BTC baseline. A possible mechanism is discontinuity reconciliation between a weekday/session-limited institutional futures venue and continuously trading crypto spot/perpetual markets.

The existence of a gap is not itself treated as alpha. The incremental question is whether **first touch of the gap zone** contains predictive information about subsequent completion to the Friday-close edge after controlling for gap size, weekend return, volatility, trend and ordinary mean reversion.

## Signal

### Source-specified event construction

- Reference instrument: `CME:BTC1!`.
- Gap timeframe: daily by default.
- Gap formation: on Monday, compare Monday open with the previous Friday close.
- Gap zone: `max(Monday open, Friday close)` to `min(Monday open, Friday close)`.
- `ENTER`: first bar that enters the gap zone.
- `FILL`: first bar that touches the previous Friday close.
- Each new Monday gap replaces the previous displayed box/signals in the source implementation.
- The source states that CME daily data are requested with lookahead off and that the gap does not repaint once the Monday daily bar is confirmed.

### Research-proposed operationalization

For testing only, treat the first confirmed `ENTER` event as time zero and test whether subsequent price reaches the Friday-close edge faster/more often than matched controls. A directional trade mapping, if tested, is **research-proposed**: after first touch, direction is from the touch toward the Friday close, with execution no earlier than the next executable bar after the signal is known.

Holding horizons, timeout rules, minimum gap-size filters, trend filters, stop losses, sizing and re-entry are not specified by the source and therefore remain **research-proposed** if introduced. No such choice should be attributed to the author.

The source is fully specified for its displayed gap/ENTER/FILL event semantics but underspecified as a complete executable trading strategy.

## Required data

- CME Bitcoin futures continuous series consistent with `CME:BTC1!`, including daily open/close and session calendar.
- BTC execution-market OHLCV for any spot or perpetual venue used in a portability test.
- Accurate timestamps, timezone conversion, CME holiday/session calendar and daylight-saving handling.
- Point-in-time contract/continuous-series construction sufficient to avoid revised back-adjustment leakage.
- For matched controls: realized volatility, weekend return, trend/momentum and liquidity/volume data as available at signal time.

## Execution assumptions

The source defines indicator events rather than an executable order model. It does not specify fees, spread, slippage, market versus limit orders, latency, impact/capacity, leverage, funding, partial fills, stop loss, position sizing or a timeout.

Any backtest must avoid same-bar hindsight: the research-proposed trade may execute only after the first-touch signal is observable. Perpetual implementations must additionally account for venue fees, spread/slippage and funding. CME calendar and daylight-saving boundaries must be reconstructed point in time rather than approximated with a fixed UTC weekend window.

## Evidence

### Source-reported

The source describes CME weekend gaps as possible mean-reversion/liquidity-reference zones and defines explicit first-touch and fill events. It provides no reviewed Sharpe, CAGR, win rate, fill-rate statistic, drawdown or other performance result.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source explicitly notes that a gap is not guaranteed to resolve immediately: it may fill quickly, fill in stages after rejection, or remain delayed into later consolidation. No independent negative-result study was reviewed for this record; absence is not evidence of no negative result.

## Falsification plan

1. Reconstruct every eligible BTC CME weekend gap point in time using the actual CME calendar and no lookahead; timestamp when Monday open and each subsequent first-touch event become knowable.
2. Measure first-touch-to-Friday-close completion probability and time-to-fill at fixed, predeclared horizons. Horizon choices are **research-defined falsification thresholds**.
3. Compare against matched non-gap price zones with similar distance-to-target, volatility, trend, weekend return and liquidity. Also compare against unconditional same-direction BTC mean reversion.
4. Separate gap-up and gap-down events; test whether any apparent effect is merely generic reversal after large weekend returns.
5. Ablate first-touch conditioning: compare all newly formed gaps versus only gaps after first entry. If first touch adds no incremental information, reject that component.
6. Bucket by gap size normalized by contemporaneous ATR/realized volatility; any bucket cutoffs are **research-defined falsification thresholds**.
7. Test CME-native fill measurement separately from spot/perpetual execution-market price behavior to avoid conflating cross-venue basis with actual gap closure.
8. Apply walk-forward/out-of-sample evaluation across multiple BTC regimes and include realistic execution costs for any research-proposed tradable mapping.
9. Run timing placebos by shifting gap/event timestamps and target levels. A similar result under placebo timing materially weakens the structural-session hypothesis.
10. Reject the alpha hypothesis if first-touch conditioning does not produce stable out-of-sample incremental target-reaching behavior versus matched controls after costs; do not rescue it by stacking additional filters post hoc.

## Crypto portability

**direct** for Bitcoin: the source itself uses CME Bitcoin futures and states that the gap logic can be viewed on BTC spot or futures charts.

Portability is still venue-sensitive. CME is session-limited while crypto spot/perpetual venues trade 24/7; futures basis, perpetual funding, fragmented liquidity, continuous-contract construction, holiday schedules and daylight-saving changes can shift the apparent gap relative to the execution venue.

## Limitations

- **not independently reproduced**.
- **underspecified** as a complete trading strategy; the source defines events, not full execution/risk rules.
- **data gap:** no source-reported historical fill-rate or performance sample was identified on the reviewed page.
- A CME continuous futures series can embed roll/back-adjustment conventions unsuitable for naive historical target levels.
- Each new Monday gap replaces the previous displayed source box/signals, so the source is not designed to preserve multiple unresolved historical gaps; any multi-gap persistence model would be **research-proposed**.
- The economic language around "magnets," stop-runs and liquidity grabs is a hypothesis, not proof of causal mechanism.

## Implementation status

Not implemented in the research stack. No Qlib full backtest, independent reproduction, frozen-survivor validation, Paper, Testnet or Live validation has been performed.

## Adoption boundary

Research-only. Presence in this repository does not mean the hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor/leaderboard entry, is profitable, is validated alpha, or is approved for implementation, paper trading, testnet or live trading.

## Related Wiki records

No stable related Hermes Wiki Brain link was identified from the GitHub-only research context; none is fabricated.

## Sources

- Greg_deVril, **BTC CME Gap – detector & single signals**, TradingView open-source script, published 2025-08-25, reviewed 2026-09-22: https://www.tradingview.com/script/9dIsa3gG-BTC-CME-Gap-detector-single-signals/
