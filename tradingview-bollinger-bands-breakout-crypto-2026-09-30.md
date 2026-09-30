---
schema: strategy-research-record-v1
title: TradingView Bollinger Bands Breakout Strategy for Crypto
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
  - https://www.tradingview.com/script/sTFw2fOj/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Bollinger Bands Breakout Strategy for Crypto

## Provenance

- Public TradingView open-source strategy: `Bollinger Bands - Breakout Strategy` by `TheSocialCryptoClub`.
- Stable source: https://www.tradingview.com/script/sTFw2fOj/
- Published 2023-05-01; source reviewed as of 2026-09-30.
- TradingView identifies the intended market as crypto, with long/short operation on futures or long-only operation on spot.
- The page is public and labels the script open-source. This record normalizes the public description rather than redistributing the Pine source.

## Economic mechanism

### Source-reported

The author describes a short-term crypto trend-following strategy whose primary trigger is price crossing outside Bollinger Bands. The page states that the strategy is intended for trending markets and offers optional trend, volatility, rate-of-change, and trade-direction filters.

### Research interpretation

The falsifiable alpha hypothesis is volatility-adjusted price breakout persistence: a close/price crossing beyond a Bollinger envelope may identify directional expansion that continues over an intraday horizon. The optional trend, volatility, and rate-of-change filters should be treated as confirmations whose incremental alpha is unproven until ablated separately.

Component roles:

- Primary signal: Bollinger Bands upper/lower breakout.
- Confirmation/regime: optional trend filter, volatility filter, and rate-of-change filter.
- Direction control: optional trade-direction filter.
- Risk/exit: opposite cross, profit target, trailing stop, or stop loss; these are not assumed to create alpha.

## Signal

Source-reported normalized rules:

- Intended timeframe: 2H, 3H, 4H, or 5H.
- Long entry: price crosses above the upper Bollinger Band, subject to enabled filters.
- Short entry: price crosses below the lower Bollinger Band, subject to enabled filters; shorting is described for futures, not spot.
- Exit choices: opposite cross, profit target, trailing stop, or stop loss.
- Configurable inputs include Bollinger period/deviation, trend filter, volatility filter, trade-direction filter, rate-of-change filter, date filter, and long/short TP/SL/trailing-stop settings.
- The source does not expose the exact defaults or Boolean algebra for the optional trend, volatility, and rate-of-change filters in the reviewed page. These details are **underspecified**.
- Exact signal formation timing, same-bar versus completed-bar semantics, re-entry behavior, and holding-period cap are **underspecified**.

Research-proposed operationalization for later testing, not source-reported: evaluate signals only after a completed bar and execute no earlier than the next tradable bar to avoid same-bar look-ahead ambiguity.

## Required data

- Market: crypto.
- Venue in the source-reported backtest example: Binance.
- Example instrument: BTCUSDT perpetual/futures notation `BTCUSDT.P`.
- Timeframes: 2H, 3H, 4H, 5H; source-reported example uses 4H.
- Required base fields: OHLCV sufficient to derive Bollinger Bands, rate of change, and common price/volatility/trend filters.
- Exact inputs needed by the optional filters are a **data gap** because their formulas are not fully exposed in the reviewed description.
- Candle timestamps and venue/timeframe boundaries must be point-in-time consistent. The source does not state timezone/candle-boundary conventions.

## Execution assumptions

Source-reported backtest example:

- Exchange: Binance.
- Pair: BTCUSDT.P.
- Timeframe: 4H.
- Fee: 0.025%.
- Slippage: 1 (unit semantics are not stated on the reviewed page).
- Initial capital: 10,000 USDT.
- Position sizing: 10% of equity.
- Backtest start: 2019-09-19.
- Source labels data from 2022-12-23 onward as out-of-sample.
- Bar magnifier: on.
- Maximum intraday loss is available as a risk-management feature.

Not specified by the reviewed source: market versus limit orders, exact fill price, spread model, market impact, capacity, funding charges, leverage/margin settings, liquidation treatment, latency, partial fills, or failure handling. Same-bar versus next-bar order timing is also underspecified.

## Evidence

### Source-reported

The source presents this as a crypto trend-following backtest strategy and provides the Binance BTCUSDT.P 4H test configuration above. No exact performance statistic is carried into this record because the reviewed public description does not provide a traceable numeric return, Sharpe, CAGR, drawdown, or win-rate figure.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The author states the strategy is particularly suited to trending markets, implying regime sensitivity and potential weakness in range-bound conditions.
- The primary trigger is a generic Bollinger breakout, so false breakouts and transaction-cost sensitivity are material risks.
- Optional filters add degrees of freedom and therefore overfitting risk unless tested with frozen parameters and ablations.
- The source-reported backtest example is one venue/instrument/timeframe configuration; portability across crypto assets and venues is unproven.
- Several execution and filter semantics are underspecified.
- No independently reproduced performance evidence was generated in this Scout run.

## Falsification plan

1. Reconstruct only source-specified behavior first; keep all missing operational choices explicitly research-proposed.
2. Compare the Bollinger breakout alone against buy-and-hold and a simple price-momentum/breakout baseline.
3. Ablate trend, volatility, and rate-of-change filters individually and jointly; reject the claim that a filter adds alpha if it does not improve out-of-sample risk-adjusted performance after costs.
4. Test 2H/3H/4H/5H separately across BTC and a predeclared liquid-crypto universe rather than selecting the best asset/timeframe after observing results.
5. Use chronological train/validation/out-of-sample partitions and a frozen forward test.
6. Stress fees, spread, slippage, and perpetual funding where applicable.
7. Separate spot long-only from perpetual long/short results.
8. Research-defined falsification threshold: reject further promotion if the normalized strategy fails to outperform the declared baseline out of sample after realistic costs, or if apparent performance is concentrated in a narrow parameter/timeframe slice that does not survive neighboring-parameter and regime checks.

## Crypto portability

**direct**

The cited source itself targets crypto, including Binance BTCUSDT.P in its example. Portability is still not automatic across spot and perpetual markets: shorting, funding, leverage/liquidation mechanics, venue fragmentation, 24/7 candle boundaries, and fee/slippage schedules can materially alter results.

## Limitations

- **underspecified:** exact optional-filter formulas/defaults and Boolean composition.
- **underspecified:** exact signal-to-order and fill timing.
- **data gap:** funding, spread, impact, capacity, leverage/margin, liquidation, latency, and partial-fill assumptions.
- **unproven:** robustness across crypto instruments, venues, timeframes, and regimes.
- **not independently reproduced:** no backtest or code execution was performed in this Scout run.

## Implementation status

Research record only. No implementation in the research stack has been completed. No Qlib full backtest was run.

## Adoption boundary

This artifact is research material only. Its presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor or leaderboard entry, demonstrated profitable alpha, or received Paper, Testnet, or Live approval.

## Related Wiki records

No stable related Hermes Wiki Brain record was verified in this GitHub-only run; no Wiki link is fabricated.

## Sources

- TradingView, TheSocialCryptoClub, `Bollinger Bands - Breakout Strategy`: https://www.tradingview.com/script/sTFw2fOj/ — published 2023-05-01; reviewed 2026-09-30.
