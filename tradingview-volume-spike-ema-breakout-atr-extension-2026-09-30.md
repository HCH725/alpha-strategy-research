---
schema: strategy-research-record-v1
title: TradingView Volume Spike + EMA Trend + Breakout with ATR Extension Filter
created: 2026-09-30
updated: 2026-09-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-30
sources:
  - https://www.tradingview.com/script/LrW6COj6-Volume-Breakout/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Volume Spike + EMA Trend + Breakout with ATR Extension Filter

## Provenance

Public TradingView open-source indicator `Volume Breakout` by `ADXAE`. Stable URL: https://www.tradingview.com/script/LrW6COj6-Volume-Breakout/ . Canonical TradingView script ID: `LrW6COj6`.

The TradingView page labels the script May 31 and an update Jun 2; it was reviewed as of 2026-09-30. The reviewed public page states that the Jun 2 update changed settings documentation but did not change the core signal logic.

This is an indicator, not an automated strategy. The source explicitly says it does not place trades or provide backtested performance. This record therefore preserves the source's setup logic as a falsifiable research hypothesis without upgrading its reference levels into executed orders.

## Economic mechanism

### Source-reported

The source separates bullish volume events into three contexts. `REV` marks strong bullish volume near the lower part of a recent range before a bullish EMA trend is established. `VOL` applies the same raw volume-spike logic when the EMA trend is already bullish. `BUY` is the most selective setup: a valid `VOL` must additionally satisfy enabled breakout, risk, ATR-extension, and cooldown filters.

The author presents the layered construction as a way to distinguish early reversal pressure, volume participation inside an established trend, and a confirmed breakout-style setup. The source also warns that volume signals can be unreliable on illiquid or abnormal-news bars, breakout filters can still generate false breakouts, ATR filters can reject valid moves, and EMA filters lag.

### Research interpretation

The primary falsifiable hypothesis is continuation, not the displayed stop/target mechanics: an unusually strong bullish participation shock should have greater forward continuation value when it occurs inside an already established bullish EMA regime and simultaneously clears recent resistance, provided the signal candle is not excessively extended relative to current ATR.

Component roles:

- Participation signal: bullish candle whose volume is both a recent-window maximum and above a configurable volume-average multiple.
- Candle-quality confirmation: minimum body-size requirement plus RSI constrained to a configurable accepted range.
- Regime: price above both fast and slow EMAs, with fast EMA above slow EMA.
- Price confirmation: close above the highest high of a configurable breakout lookback when enabled.
- Extension filter: reject a BUY when candle range is too large relative to ATR when enabled.
- Risk/setup controls: maximum candle high-to-low risk percentage and cooldown when enabled.
- Reference-only risk/exit display: BUY-candle high as entry reference, BUY-candle low as stop reference, and risk-reward multiples for target references.

The incremental alpha contribution of each component is unproven. The combination is economically coherent as participation-confirmed trend continuation, but it may also be indicator stacking that reduces sample size without adding predictive information.

## Signal

Source-supported normalized logic:

1. Formation is bar-based. The source describes a bullish candle, its volume, body size, RSI, EMA state, breakout close, ATR-relative candle range, and cooldown state.
2. Raw bullish volume spike requires:
   - bullish candle;
   - volume is the highest within the selected volume lookback;
   - volume exceeds the selected moving-average multiple;
   - candle body meets the selected minimum body percentage;
   - RSI lies inside the selected acceptable range.
3. `REV` additionally requires price near the lower zone of the recent lookback range and the defined bullish EMA trend condition to be absent.
4. `VOL` requires the raw volume-spike logic while the bullish EMA condition is present. The bullish trend condition is price above the fast EMA, price above the slow EMA, and fast EMA above slow EMA.
5. `BUY` requires a valid `VOL` plus any enabled breakout, risk, ATR-extension, and cooldown filters.
6. When breakout confirmation is enabled, price must close above the highest high of the selected breakout lookback.
7. When the ATR extension filter is enabled, BUY is blocked if the candle range is too large relative to ATR.
8. When the risk filter is enabled, the high-to-low risk percentage of the BUY candle must be below the selected maximum.
9. Cooldown requires a minimum selected number of bars since the previous BUY.

The public description exposes configurable inputs for volume lookback, volume-MA length and multiple, minimum body percentage, fast/slow EMA, RSI length and accepted range, cooldown, REV low-zone settings, breakout lookback, maximum risk percentage, ATR length and maximum candle-range/ATR ratio, and risk-reward display. Numeric defaults are not stated in the reviewed public description and are therefore `underspecified`.

The source does not define an executed long entry, short signal, actual fill rule, holding period, position sizing, or strategy exit. Its BUY-candle high/low and target levels are explicitly reference levels rather than orders. Any conversion from BUY into a trade is therefore `research-proposed`, not source-reported.

## Required data

- Reliable OHLCV bars for the tested instrument.
- Sufficient point-in-time history for the selected volume-high window, volume moving average, EMA calculations, RSI, breakout-high lookback, and ATR.
- Candle boundaries and timestamps consistent with the selected TradingView market/timeframe.
- The source says the indicator can be used across liquid stocks, crypto, forex, indices, and futures, but cautions that volume quality differs across markets.
- For crypto, venue-specific traded volume must not be treated as universal market volume.
- No funding, mark/index, basis, order-book/depth, aggressor-side trades, open interest, liquidation, or options data is required by the stated signal.

## Execution assumptions

The source explicitly states that the indicator does not place trades or simulate orders. It provides only setup/reference levels.

Source-reported reference construction:
- entry reference: high of the BUY candle;
- stop reference: low of the BUY candle;
- target reference(s): entry plus selected risk-reward multiple(s).

`research-proposed`: for a causal backtest, evaluate the complete BUY condition only after all required signal-bar fields are available and permit execution no earlier than the next tradable event after signal confirmation. The exact order type and fill model must be frozen before testing.

Fees, spread, slippage, impact/capacity, funding, leverage/margin, borrow/shorting, latency, partial fills, and failure handling are not specified by the source and remain `underspecified`.

## Evidence

### Source-reported

The source provides no backtested performance results and explicitly says the indicator is not a strategy. It states that the tool is intended for liquid markets with reliable volume and that behavior may differ materially where volume is broker-dependent or tick-based.

No Sharpe, CAGR, drawdown, win rate, profitability statistic, or independently verified crypto performance claim is reported in the reviewed page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself identifies several failure risks: unreliable volume on illiquid symbols, abnormal-news candles, inconsistent volume feeds, false breakouts despite the breakout filter, valid moves blocked by the ATR filter, weak moves still passing it, and lag from EMA trend filters.

A nearby repository record already captures a simpler price-and-volume breakout with a moving-average trend filter. That adjacency raises a material redundancy risk: the extra RSI/body/ATR/risk/cooldown components must demonstrate incremental value rather than merely increase selectivity.

## Falsification plan

Test the BUY continuation hypothesis on liquid crypto instruments using causally available completed-bar data.

Required ablations:
1. Price breakout only.
2. Breakout + raw volume spike.
3. Breakout + raw volume spike + EMA regime.
4. Add body-size and RSI confirmation.
5. Add ATR-extension filter.
6. Add risk and cooldown filters.
7. Full source-described BUY construction.

Use multiple liquid venues or venue feeds where feasible to test whether the result is robust to volume-source dependence, and separate spot from perpetual markets. Include realistic fees, spread/slippage, and perpetual funding where applicable.

`research-defined falsification threshold`: reject or materially downgrade the full construction if it fails to improve net out-of-sample continuation quality versus the simpler breakout + volume + EMA control across the pre-registered test universe, or if any apparent advantage disappears under realistic cost sensitivity or a second reliable volume feed. Exact numeric acceptance thresholds must be frozen before backtesting rather than selected after observing results.

## Crypto portability

direct

The source explicitly lists crypto among intended liquid markets and relies on OHLCV-derived features available on crypto venues. Direct applicability does not imply validated crypto alpha.

Crypto-specific risks include fragmented venue volume, 24/7 candle-boundary choices, spot-versus-perpetual volume differences, funding and mark/index mechanics for perpetuals, exchange outages, and unusually large liquidation/news candles that can satisfy volume conditions while producing adverse continuation.

## Limitations

- Numeric input defaults are `underspecified` in the reviewed public description.
- The source is an indicator, not a strategy; executed entry, fill timing, exit, holding period, re-entry, and position sizing are `underspecified`.
- The BUY-candle entry/stop/target lines are reference levels only.
- No short-side setup is described.
- Exact source-code implementation details were not independently reproduced during this run.
- Venue, ticker, timeframe, and market type are not fixed by the source.
- Volume is venue/feed dependent.
- Hybrid-filter complexity creates a substantial overfitting/selectivity risk.
- Not independently reproduced.

## Implementation status

Not implemented in the research stack. No backtest, Qlib validation, runtime change, paper trading, testnet, or live verification was performed by this Scout.

## Adoption boundary

Research-only. Presence in this repository does not mean the record passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No stable Hermes Wiki Brain page was resolved or accessed in this GitHub-only Scout cycle; none is fabricated.

Repository-adjacent research record: `tradingview-price-volume-breakout-ma-trend-2026-09-18.md` captures a simpler price-and-volume breakout with moving-average trend filtering and should be used as an ablation/dedup control, not treated as a Wiki link.

## Sources

- TradingView — `Volume Breakout`, `ADXAE`, public open-source indicator, page dated May 31 with updates through Jun 2, reviewed 2026-09-30: https://www.tradingview.com/script/LrW6COj6-Volume-Breakout/
