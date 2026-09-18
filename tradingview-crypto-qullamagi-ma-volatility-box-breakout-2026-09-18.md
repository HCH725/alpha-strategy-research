---
schema: strategy-research-record-v1
title: "TradingView Crypto Qullamagi MA-Stack Volatility-Box Breakout"
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
  - https://www.tradingview.com/script/0rVYn2c4/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Crypto Qullamagi MA-Stack Volatility-Box Breakout

## Provenance

Public TradingView open-source strategy `Qullamagi EMA Breakout Autotrade (Crypto Futures L+S)` by `asefzxizexvsadf`, originally published 2025-11-14 and updated 2025-11-28. Stable source: https://www.tradingview.com/script/0rVYn2c4/. Reviewed 2026-09-18.

## Economic mechanism
### Source-reported
The author frames the strategy as crypto trend continuation: require an ordered moving-average trend, wait for volatility contraction, then enter a range breakout supported by abnormal volume. Optional higher-timeframe trend alignment is intended to reduce counter-trend entries.

### Research interpretation
The falsifiable hypothesis is that a breakout from recent volatility contraction has greater continuation probability when (1) multiple moving averages establish directional persistence and (2) volume expands at the breakout. The MA stack is a regime filter, the contraction box defines the primary setup, volume is confirmation, and ATR/MA exits are risk management rather than alpha evidence.

## Signal

Source-reported strict-mode long logic: `Close > EMA10 > EMA20 > SMA50 > SMA100 > SMA200`, with the moving averages sloping upward; require a tight volatility box constrained using ATR, a volume spike above an SMA of volume times a multiplier, and a breakout above the box high. Short logic mirrors these conditions. An optional higher-timeframe filter requires higher-timeframe close above/below its 200-SMA (default HTF 1D). Strict mode is described for 1H-4H; loose mode relaxes the stack/filters for 15m-30m.

The 2025-11-28 update also describes a preferred experimental MA set of 5/15/67/200/350 and adds pullback entries after a breakout. Exact box length, ATR threshold, volume SMA length/multiplier, slope definition, breakout same-bar/intrabar semantics, pullback Boolean rule, cooldown, and all preset values not explicitly stated on the public page are **underspecified** and must not be inferred.

## Required data

Crypto futures/perpetual OHLCV; source names BTC, ETH and major altcoins and venues including Binance, Bybit and OKX. Bar timeframe is 1H-4H for strict mode or 15m-30m for loose mode. Higher-timeframe OHLC is additionally required when the optional HTF filter is enabled. Timestamp/candle-boundary convention and point-in-time venue-data handling are not specified.

## Execution assumptions

The source permits breakout detection by close or intrabar and is webhook/autotrade oriented, but exact signal-to-order timing and fill semantics are underspecified. Fees, spread, slippage, latency, funding, leverage/margin, partial-fill behavior and market/limit order choice are not fixed by the public description. The source explicitly recommends including commissions and slippage in backtests.

## Evidence
### Source-reported
The author states that their own testing found ETHUSDT.P on Binance at 1H with MA lengths 5/15/67/200/350 to be the most consistent/robust configuration they observed. No exact performance statistic is relied upon here, and this statement is not independent evidence.

### Independently reproduced
Not independently reproduced.

### Negative evidence
No independent negative result was identified in the reviewed source. The author's recommendation to retune MA lengths, ATR/box settings and volume multipliers by symbol/exchange itself indicates material parameter and venue sensitivity; absence of reported failures is not evidence of robustness.

## Falsification plan

1. Recover or predeclare the exact box, ATR, volume and slope rules before testing; do not optimize missing definitions after seeing results.
2. Test strict long/short logic separately on BTC and ETH perpetuals across multiple venues with point-in-time bars and realistic fees, spread, slippage and funding.
3. Compare against a plain volatility-box breakout under identical execution assumptions.
4. Ablate MA-stack, volume confirmation and HTF filter separately to determine whether each contributes incremental out-of-sample value.
5. Keep the source-preferred ETH 1H / 5-15-67-200-350 configuration as a source-selected specification, not an unbiased discovery sample; require separate OOS periods and nearby-parameter stability.
6. Reject or materially weaken the hypothesis if net OOS continuation/expectancy disappears under realistic costs or depends narrowly on one venue, one parameter tuple or one regime.

## Crypto portability

direct. The source explicitly targets crypto futures/perpetuals. Portability risks include venue-specific volume, funding, 24/7 candle boundaries, liquidity, contract specifications and differences between last/mark/index prices.

## Limitations

Several implementation-critical parameters and timing semantics are underspecified. The strategy contains multiple filters and tunable parameters, creating substantial multiple-testing/overfitting risk. Source-reported preferred settings are not independently reproduced.

## Implementation status

Research capture only. No implementation or backtest in our research stack has been completed.

## Adoption boundary

Research-only; not approved for implementation, paper trading, testnet or live trading. Presence in this repository is not evidence of profitable or validated alpha.

## Related Wiki records

None linked; no stable Hermes Wiki Brain record was established from GitHub-visible evidence, and no Wiki access was used.

## Sources

- TradingView, `Qullamagi EMA Breakout Autotrade (Crypto Futures L+S)`, `asefzxizexvsadf`, updated 2025-11-28: https://www.tradingview.com/script/0rVYn2c4/
