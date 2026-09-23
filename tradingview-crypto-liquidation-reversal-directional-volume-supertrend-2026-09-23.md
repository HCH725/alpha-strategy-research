---
schema: strategy-research-record-v1
title: Crypto Liquidation-Reversal Directional-Volume Supertrend Confirmation
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
  - https://www.tradingview.com/script/vOwc3W80-Liquidation-Reversal-Signals-AlgoAlpha/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Liquidation-Reversal Directional-Volume Supertrend Confirmation

## Provenance

- Public TradingView open-source script: `Liquidation Reversal Signals [AlgoAlpha]`.
- Author/page identity: `AlgoAlpha`.
- Published/updated: 2025-11-07 according to the reviewed TradingView page.
- Stable source URL: https://www.tradingview.com/script/vOwc3W80-Liquidation-Reversal-Signals-AlgoAlpha/
- Source reviewed as of 2026-09-23.
- Deduplication on current `main` found no record for this canonical TradingView source and no materially identical normalized rule combining lower-timeframe directional-volume z-score extremes with a subsequent Supertrend regime flip inside a bounded confirmation window.

## Economic mechanism

### Source-reported

The source describes a liquidation-reversal detector that combines statistical extremes in lower-timeframe up/down volume with a Supertrend trend-state change. It interprets unusually high up-volume while the prevailing Supertrend is bearish as potential short-liquidation/squeeze activity, and unusually high down-volume while Supertrend is bullish as potential long-liquidation activity. A reversal signal is marked only if a Supertrend flip follows the detected volume event within an allowed timeout window. The author frames this as an exhaustion/reversal setup rather than direct observation of exchange liquidation records.

### Research interpretation

The falsifiable mechanism is **forced-flow exhaustion followed by price-regime confirmation**.

If an unusually large directional-volume impulse occurs against the prevailing trend, it may represent forced closing by the losing leveraged side rather than durable new information. If price subsequently flips its trend state within a short, pre-specified window, the conjunction may contain more reversal information than either abnormal volume or Supertrend alone.

The key hypothesis is therefore:

> Conditional on the prevailing Supertrend state, an opposite-direction lower-timeframe volume z-score extreme followed by a Supertrend flip within a bounded window predicts greater subsequent reversal magnitude or probability than matched Supertrend flips without the preceding volume extreme.

The liquidation attribution is a hypothesis, not observed participant identity. Standard OHLCV directional-volume proxies cannot by themselves prove that forced liquidations occurred.

## Signal

### Source-supported logic

- Use lower-timeframe volume to separate/estimate up-volume and down-volume activity.
- Normalize directional volume using a z-score to identify statistical extremes.
- During a bearish Supertrend, an extreme up-volume observation is treated as a potential short-liquidation/squeeze event.
- During a bullish Supertrend, an extreme down-volume observation is treated as a potential long-liquidation event.
- After such an event, monitor for a Supertrend regime flip.
- Confirm a reversal signal only when the trend flip occurs within the source's allowed timeout window.

The reviewed public description does not expose enough detail to record the exact lower timeframe, z-score lookback/threshold, Supertrend ATR length/multiplier, or timeout value without inspecting/copying source code; those values are therefore **underspecified** here rather than invented. Entry fill, exit, holding period, re-entry, sizing, stop and take-profit lifecycle are also underspecified.

### Research-proposed operationalization

For later falsification only, reconstruct the source-compatible event sequence from parameters traceable to the public script, then compare the conjunction against its components. If exact source parameters cannot be recovered in a reproducible and public-safe way, do not silently substitute optimized values. Any parameter neighborhood, forward-return horizon, trade mapping, holding period, or sizing rule introduced by downstream research is `research-proposed`.

## Required data

- Crypto instrument with reliable OHLCV and sufficient lower-timeframe history; the source is presented as a chart indicator rather than a venue-specific liquidation feed.
- Main-chart OHLC for Supertrend construction.
- Lower-timeframe OHLCV required for the source's directional-volume estimate.
- Timestamp alignment between lower-timeframe observations and the main chart bar.
- Point-in-time data only; lower-timeframe bars must be closed/available before their information is used.
- If later testing claims actual liquidation causality, independent exchange-native liquidation data is required; OHLCV alone is insufficient.
- For perpetual implementation, mark/index price, funding and contract/venue metadata should be retained separately from the signal proxy.

## Execution assumptions

The source does not specify a complete executable lifecycle, fee model, spread/slippage model, impact model, leverage, margin, borrow, partial-fill behavior or position sizing.

A leakage-safe test must not enter at the earlier directional-volume spike after observing the later Supertrend flip. Signal formation occurs only once the confirming flip is known; executable entry must be no earlier than the next eligible observable price after confirmation. Any later perpetual implementation must include fees, spread, slippage, funding and event-state impact because liquidation/squeeze regimes can have unusually poor execution quality.

## Evidence

### Source-reported

The TradingView page describes lower-timeframe up/down-volume z-score extremes, prevailing Supertrend state, a bounded timeout, and subsequent Supertrend flips as the components used to flag probable liquidation-driven reversals. The reviewed page does not provide a traceable Sharpe, CAGR, drawdown, fixed-sample hit rate, transaction-cost result or independent OOS statistic; none is recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The indicator estimates probable liquidation pressure from directional volume; it does not observe exchange liquidation records or trader leverage directly.
- Abnormal directional volume can arise from information arrival, discretionary aggressive trading, rebalancing or venue-specific activity rather than forced liquidation.
- Supertrend confirmation is delayed by construction, so apparent reversal quality can disappear after realistic signal timing and execution costs.
- Lower-timeframe aggregation can create timestamp/boundary sensitivity and may behave differently across venues and 24/7 candle conventions.
- None identified in the reviewed source establishes net profitability after costs; absence is not evidence of no negative result.

## Falsification plan

1. **Source-compatible reconstruction gate:** recover only publicly traceable source parameters/logic. If the event sequence cannot be reproduced unambiguously, keep the hypothesis unimplemented rather than optimizing a replacement.
2. **Component ablation:** compare (a) Supertrend flips alone, (b) directional-volume z-score extremes alone, and (c) the conjunction. Reject the conjunction layer if it adds no stable OOS information.
3. **Liquidation-causality check:** where exchange-native liquidation prints are available, test whether proxy events coincide with actual forced-liquidation intensity more often than matched high-volume controls. Failure weakens the liquidation interpretation even if a generic reversal effect remains.
4. **Matched-event control:** match candidate events on absolute return, realized volatility and total volume. Test whether directional-volume extremeness contributes beyond simply selecting violent bars.
5. **Timing audit:** form the signal only after the Supertrend flip is observable. Compare immediate-next-bar and delayed execution; reject results dependent on retroactive fills at the initial spike.
6. **Timeout robustness:** test a small pre-registered neighborhood around the source timeout. Knife-edge dependence on one timeout weakens the thesis.
7. **Z-score/Supertrend robustness:** test small pre-registered neighborhoods around source parameters without selecting the best test-set combination. Compare against simple volume percentile and price-trend baselines.
8. **Direction symmetry:** test short-squeeze and long-liquidation cases separately. Do not average away a one-sided failure.
9. **Venue/timeframe portability:** evaluate major liquid crypto venues and multiple predeclared timeframes with consistent candle boundaries; use leave-one-venue-out checks where data permits.
10. **Costs and event impact:** apply fees, spread, slippage and adverse event-state impact. For perpetuals include funding. Reject executable-alpha claims if the edge does not survive realistic costs.
11. **Walk-forward/OOS:** select parameters only on training windows and evaluate untouched chronological OOS periods spanning trend, range, high-volatility and quiet regimes.

Material failure criterion: if the volume-extreme-plus-flip conjunction does not provide stable incremental OOS information over Supertrend flips and matched volatility/volume controls after correct confirmation timing and costs, reject the added liquidation-proxy layer rather than adding more filters.

## Crypto portability

`direct`

The source explicitly targets liquidation-style behavior in leveraged crypto trading. However, portability across spot and perpetual markets is not automatic: true liquidation mechanics occur in leveraged derivatives, while spot OHLCV may only reflect transmitted price/volume effects. Venue leverage limits, maintenance-margin schedules, contract specifications, funding, mark/index prices, liquidity and 24/7 candle boundaries can materially change results.

## Limitations

- `not independently reproduced`
- `underspecified`: exact lower timeframe, z-score lookback/threshold, Supertrend parameters and timeout are not stated in the reviewed public description.
- `underspecified`: no complete entry, exit, holding, sizing or re-entry lifecycle.
- `data gap`: OHLCV directional-volume estimates do not identify actual forced liquidations.
- `unproven`: incremental alpha beyond Supertrend, volatility and volume controls.
- Confirmation lag can create substantial execution decay during fast squeeze/liquidation events.

## Implementation status

Research-only normalization of a public TradingView hypothesis. No implementation in the research stack, Qlib full backtest or independent reproduction was performed in this Scout cycle.

## Adoption boundary

This record is external research material only. Repository presence does not mean it passed Research Intake Review, entered Hermes Wiki Brain, entered the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received implementation, Paper, Testnet or Live approval.

## Related Wiki records

No stable Hermes Wiki Brain record is asserted from this GitHub-only Scout. Related repository families include volume-extreme, liquidation-proxy and Supertrend research, but no Wiki link is fabricated.

## Sources

1. TradingView, `Liquidation Reversal Signals [AlgoAlpha]`, author `AlgoAlpha`, published/updated 2025-11-07, reviewed 2026-09-23: https://www.tradingview.com/script/vOwc3W80-Liquidation-Reversal-Signals-AlgoAlpha/
