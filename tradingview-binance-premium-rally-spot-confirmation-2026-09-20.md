---
schema: strategy-research-record-v1
title: TradingView Binance Premium Rally Spot-Flow Confirmation
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
  - https://www.tradingview.com/script/ojbKQFLu-Basic-Binance-Premium-Index/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Binance Premium Rally Spot-Flow Confirmation

## Provenance

Public TradingView open-source indicator page, **Basic Binance Premium Index**, author/page identity `Gokubro`, originally published 2022-03-30 and updated 2022-06-10. Stable source: https://www.tradingview.com/script/ojbKQFLu-Basic-Binance-Premium-Index/ . Source reviewed as of 2026-09-20.

The source explicitly describes a Binance-futures premium measure constructed from the perpetual price and a volume-weighted spot price. It lists BTC, ETH, LTC, ICP, BNB, ADA, and DOGE and notes that the BTC/ETH/LTC perpetual references were changed to USDT pairs in the 2022-06-10 update.

## Economic mechanism

### Source-reported

The author interprets a rally in which the perpetual trades above the volume-weighted spot reference as being driven more by perpetual-futures demand and therefore potentially bearish/fragile. Conversely, a rally in which spot trades above the perpetual is described as being backed by spot buying and therefore potentially bullish. This is the author's interpretation, not independently established evidence.

### Research interpretation

The falsifiable hypothesis is that **the sign and magnitude of Binance perpetual-versus-volume-weighted-spot premium contains incremental information about rally quality**. A price advance accompanied by relatively stronger spot pricing may represent less leverage-dependent demand and exhibit greater continuation, while a price advance accompanied by relatively stronger perpetual pricing may represent leveraged crowding and exhibit weaker continuation or greater reversal risk.

This is materially different from a generic basis mean-reversion hypothesis: the proposed object is the interaction between contemporaneous price trend and spot/perpetual leadership, not unconditional convergence of the premium toward zero.

## Signal

Source-specified premium calculation:

`premium_pct = (futures_price / vwap(spot_price) - 1) * 100`

Source-supported interpretation during a rally:

- positive premium (perpetual above volume-weighted spot) is interpreted by the author as weaker spot confirmation / potentially bearish price action;
- negative premium (spot above perpetual) is interpreted as stronger spot participation / potentially bullish price action;
- an optional smoothed moving-average display is available, but the source page does not specify a canonical smoothing length in its description.

The source does **not** specify a canonical rally lookback, entry trigger, premium threshold, exit, holding period, re-entry rule, position sizing, or executable strategy.

For later testing only, a `research-proposed` operationalization should define price-trend formation independently of the premium and compare forward returns conditional on premium sign/quantile. Any lookback, threshold, smoothing window, holding horizon, or trade rule introduced for that purpose is `research-proposed`, not source-reported.

Rule completeness: **underspecified as a trading strategy; sufficiently specified as a premium/spot-confirmation hypothesis.**

## Required data

- Binance crypto spot and corresponding perpetual-futures prices for matched base assets.
- Source-listed universe: BTC, ETH, LTC, ICP, BNB, ADA, DOGE; historical availability must be audited rather than assumed.
- Perpetual last price.
- Spot price and volume sufficient to construct the source's volume-weighted spot reference.
- OHLCV for defining any `research-proposed` rally/trend condition.
- Synchronized timestamps and explicit candle boundaries across spot and perpetual feeds.
- Point-in-time symbol availability and contract mapping, including historical symbol changes.
- Funding is not required by the source formula but should be retained as a control in falsification because premium and funding can reflect related derivatives crowding.

## Execution assumptions

The source is an indicator, not an execution specification. Signal-to-order timing, next-bar versus same-bar execution, order type, fill model, fees, spread, slippage, market impact, funding treatment, leverage/margin, latency, and partial fills are all **underspecified**.

Any eventual backtest must form the premium only from information available at the decision timestamp and execute after signal formation. Same-bar use of a completed-bar VWAP without an appropriate lag would require an explicit leakage audit.

## Evidence

### Source-reported

The TradingView page provides the formula and qualitative spot-versus-perpetual interpretation. It does not report a backtest, Sharpe ratio, win rate, CAGR, drawdown, statistical significance, or other empirical performance evidence.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-reported negative empirical test was identified. The author's directional interpretation is qualitative and could fail because spot/perpetual premium can reflect funding expectations, temporary basis mechanics, venue-specific flow, liquidity differences, or liquidation effects rather than durable directional information. Absence of reported negative evidence is not evidence of robustness.

## Falsification plan

1. Construct the premium point-in-time using synchronized Binance spot/perpetual data and reproduce the source formula before testing returns.
2. Define several simple, predeclared `research-proposed` rally conditions (for example positive trailing return over fixed horizons) without optimizing them jointly with the premium threshold.
3. Compare forward returns for rally observations with negative versus positive premium; also test continuous premium rank/quantile rather than relying only on zero-crossing.
4. Baselines: price trend alone, raw spot return alone, perpetual return alone, conventional spot-perpetual basis, and funding where available.
5. Ablation: price trend only → premium only → trend × premium interaction. The interaction must improve out-of-sample discrimination to support the specific rally-quality thesis.
6. Test both competing outcomes: continuation from spot leadership and reversal/underperformance from perpetual leadership. Reject a one-sided narrative if signs are unstable across horizons.
7. Separate BTC/ETH from smaller source-listed assets; require robustness across assets rather than allowing one dominant symbol to determine the conclusion.
8. Test raw premium versus source-permitted smoothing using predeclared windows; reject smoothing choices that work only after parameter search.
9. Control for realized volatility, volume shock, funding, and large liquidation episodes to determine whether premium adds information beyond generic leveraged-market stress.
10. Use chronological out-of-sample evaluation, realistic fees/funding/slippage, and point-in-time symbol availability. Material decay after costs or unstable sign across OOS windows weakens/rejects the hypothesis.

## Crypto portability

**direct** — the source is explicitly a crypto Binance spot/perpetual indicator.

Portability beyond Binance is unproven. Venue fragmentation, different spot-index construction, contract specifications, stablecoin quote differences, funding schedules, mark/index methodology, liquidity, and timestamp alignment can materially change the premium. The source's qualitative interpretation should not be assumed to transfer to other venues without separate validation.

## Limitations

- No source-reported empirical validation.
- Trading strategy timing and execution are **underspecified**.
- Rally definition is **underspecified**.
- Canonical smoothing length is **underspecified** on the reviewed source page.
- The source formula uses a volume-weighted spot reference whose exact historical construction must be reproduced carefully.
- Binance-specific source; cross-venue portability is **unproven**.
- Premium may proxy for funding/crowding or microstructure effects rather than independent spot-flow confirmation.
- Not independently reproduced.

## Implementation status

Research record only. No implementation or backtest in the research stack has been completed.

## Adoption boundary

`research-only / not-implemented / not-approved`.

Presence in this repository does not imply profitable alpha, successful validation, approval for implementation, paper trading, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted from this GitHub-only Scout run.

## Sources

- Gokubro, **Basic Binance Premium Index**, TradingView open-source script, published 2022-03-30, updated 2022-06-10, reviewed 2026-09-20: https://www.tradingview.com/script/ojbKQFLu-Basic-Binance-Premium-Index/
