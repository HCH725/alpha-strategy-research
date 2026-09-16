---
schema: strategy-research-record-v1
title: TradingView BTC Donchian Breakout Continuation with ATR, ADX and EMA200
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
  - https://www.tradingview.com/script/tuC7aGNI/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView BTC Donchian Breakout Continuation with ATR, ADX and EMA200

## Provenance

Public TradingView open-source strategy **Strategy 432 BTC - Donchian Breakout Continuation**, published by **Fran_Pineda**. TradingView displays the publication date as May 5; the page reviewed on 2026-09-16 identifies the intended market as BTC/USDT and timeframe as 4H.

Stable source: https://www.tradingview.com/script/tuC7aGNI/

## Economic mechanism

### Source-reported

The author describes a BTC trend-following continuation thesis: sufficiently large directional breakouts may persist when they occur in an already confirmed trend environment. The strategy therefore combines a Donchian breakout with volatility-normalized breakout magnitude, trend-strength confirmation and a long-horizon trend filter rather than fading the move.

### Research interpretation

The falsifiable hypothesis is that **BTC/USDT 4H closes that escape the prior Donchian range by a sufficiently large ATR-normalized distance have positive continuation conditional on strong ADX and alignment with EMA200**.

Component roles:

- Primary signal: previous-candle Donchian channel breakout.
- Breakout-quality filter: breakout distance relative to ATR.
- Regime / trend-strength filter: ADX.
- Macro-direction filter: EMA200.
- Exit / risk logic: fixed maximum holding time and opposite Donchian break.

The filters should be ablated independently. Their coexistence in the source does not establish that each contributes incremental alpha.

## Signal

Source-described target configuration:

- Instrument: BTC/USDT.
- Timeframe: 4H.
- Formation: evaluated from completed price bars; the source explicitly describes a long trigger when price **closes** above the previous Donchian high.
- Long entry: close above the previous Donchian high, breakout distance sufficiently large relative to ATR, ADX confirms trend strength, and price is above EMA200.
- Short entry: optional and disabled by default; the source states that short-side logic exists for testing, but the reviewed page does not expose a complete normalized short rule beyond the symmetric conceptual setup.
- Exit: fixed number of bars and/or opposite Donchian-channel break.
- Re-entry: not specified on the reviewed page.
- Position sizing: not specified on the reviewed page.

Important underspecification: the reviewed public description does not state the exact Donchian lookback, ATR lookback or minimum breakout-distance multiplier, ADX lookback/threshold, fixed holding-bar count, or precise order-fill semantics. Those values must be recovered from the public Pine source or treated as research parameters before implementation; they are not invented here.

## Required data

Minimum research data:

- BTC/USDT OHLCV, 4H bars.
- High/low/close history sufficient for the Donchian lookback.
- OHLC history sufficient to calculate ATR, ADX and EMA200.
- Consistent timestamp and candle-boundary convention.

The source does not establish a specific exchange/venue or spot-versus-perpetual contract on the reviewed description. Venue and market type must therefore be fixed explicitly in any reproduction.

## Execution assumptions

The source specifies a close-based long trigger but the reviewed description does not specify whether the simulated order fills at that same close, next-bar open, or another price. Fees, spread, slippage, market impact, funding, leverage, margin, partial fills and latency are not specified in the reviewed description.

A leakage-safe implementation must calculate the previous Donchian boundary without including the breakout bar itself and must avoid same-bar fill assumptions that use information unavailable before the close.

## Evidence

### Source-reported

The author states that the strategy is designed specifically for BTC/USDT 4H and that the original BTC research favored the long side, which is why shorts are disabled by default. The author also warns that results may vary significantly on other assets or timeframes.

No exact return, Sharpe, win rate, CAGR, drawdown or other performance statistic is recorded here because no such figure is traceable from the reviewed public description.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself warns that portability across assets and timeframes may be poor. Breakout systems are also structurally exposed to false breaks and transaction-cost sensitivity; these are research risks, not source-verified failure statistics. No independent contrary result was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

1. Reconstruct the exact public Pine parameters before claiming source parity; fail closed on parameters that cannot be recovered.
2. Test BTC/USDT 4H with point-in-time Donchian boundaries and realistic next-actionable-price execution.
3. Compare against a bare Donchian breakout baseline.
4. Ablate ATR magnitude, ADX and EMA200 filters individually and jointly to test whether they add information rather than merely reduce trade count.
5. Test long-only versus symmetric long/short rules separately.
6. Use chronological OOS and multiple BTC market regimes, including bull trends, bear trends and prolonged ranges.
7. Apply realistic fees/slippage and, if using perpetuals, funding.
8. Reject or materially weaken the hypothesis if net OOS continuation disappears after costs, is concentrated in one historical episode, or the confirmation filters fail to improve risk-adjusted OOS behavior versus the simpler breakout baseline.

## Crypto portability

**direct** for the source's stated BTC/USDT 4H target, subject to venue/market-type reconstruction.

Portability to other crypto assets or timeframes is **unproven**. For perpetual implementation, funding and mark/index conventions must be added. Crypto trades 24/7, so the 4H candle boundary and exchange timezone convention must be frozen before comparison.

## Limitations

- Not independently reproduced.
- Exact Donchian, ATR and ADX parameters are underspecified in the reviewed page description.
- Exact fixed-bar exit horizon is underspecified.
- Venue and spot/perpetual market type are unspecified.
- Fill timing, fees and slippage are unspecified.
- Source-reported preference for long-only is not independent evidence of persistent long-side alpha.

## Implementation status

No implementation or validation in the research stack has been completed. No PyBroker, Nautilus, paper, testnet or live verification is implied.

## Adoption boundary

Research material only. Presence in this repository does not mean profitable, validated alpha, approved for implementation, or approved for paper, testnet or live trading.

## Related Wiki records

No stable related Hermes Wiki Brain record is asserted here.

## Sources

- TradingView — Fran_Pineda, **Strategy 432 BTC - Donchian Breakout Continuation**: https://www.tradingview.com/script/tuC7aGNI/ (public open-source strategy; reviewed 2026-09-16).
