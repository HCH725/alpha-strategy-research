---
schema: strategy-research-record-v1
title: "TradingView Momentum Squeeze Breakout Engine"
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
  - https://www.tradingview.com/script/bN8jxMy5-Momentum-Squeeze-Breakout-Engine/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Momentum Squeeze Breakout Engine

## Provenance

Public TradingView open-source strategy **Momentum Squeeze Breakout Engine**, published by `Pridarasx`. Stable source URL: https://www.tradingview.com/script/bN8jxMy5-Momentum-Squeeze-Breakout-Engine/. The public page is dated `Jun 25`; the year is not inferred because the reviewed page does not expose it unambiguously. Source reviewed 2026-09-18. TradingView script identity: `bN8jxMy5`.

GitHub dedup against current `main` found no record containing this canonical script identity and no materially same normalized combination of Bollinger/Keltner squeeze state, EMA200 macro filter, cumulative intra-bar location bias, 3-period ROC confirmation, and three-bar post-squeeze breakout window.

## Economic mechanism
### Source-reported

The author describes a trend-following breakout strategy intended to capture directional expansion after volatility compression. Compression is identified when Bollinger Bands contract inside Keltner Channels. A 200-period EMA supplies macro trend direction. A cumulative intra-bar bias measure is intended to distinguish accumulation from weak price drift by evaluating where closes fall within their bars over a structural lookback. A 3-period rate-of-change filter requires immediate positive velocity before a long breakout is accepted.

### Research interpretation

The falsifiable hypothesis is that a volatility-release breakout has higher continuation quality when four distinct conditions align: prior compression, long-horizon trend direction, recent bar-location pressure, and short-horizon momentum acceleration. The components have separate roles rather than being treated as interchangeable confirmations: BB-inside-KC = regime/formation; EMA200 = macro directional gate; cumulative bar-location bias = directional pressure confirmation; ROC(3) = immediate velocity confirmation.

The key empirical question is whether these confirmations add out-of-sample information beyond a simpler squeeze-release breakout after accounting for reduced trade count and execution costs.

## Signal

Source-reported long-side logic:

- **Compression:** Bollinger Bands contract inside Keltner Channels.
- **Recency window:** a compression zone must have broken out within the previous 3 bars.
- **Primary trigger:** price crosses above the upper Bollinger Band.
- **Macro filter:** price must be above the 200-period EMA.
- **Bias confirmation:** cumulative holistic bias must be positive (`cumBias > 0`). The source says this bias evaluates close location relative to each bar's high-low range over a structural lookback.
- **Momentum confirmation:** 3-period rate of change must be positive (`priceROC > 0`).
- **Exit:** price crosses below the lower Bollinger Band following a squeeze, or holistic bias turns negative.
- **Cooldown:** 15 bars between signals.
- **Intended timeframe:** 1-hour chart.
- **Intended assets:** high-liquidity markets including major crypto pairs such as BTC and ETH, plus equities, indices and major FX.

The reviewed public description presents an explicit BUY rule but does not specify a symmetric short-entry rule. This record therefore does not invent one.

Exact Bollinger length/deviation, Keltner length/multiplier/basis, EMA source, holistic-bias structural lookback and aggregation formula, whether `crosses` requires confirmed bar close, and detailed squeeze-release state transitions are **underspecified** in the reviewed prose. They must be recovered from the public Pine source before exact reproduction or explicitly labeled `research-proposed` in later research.

The source reports a 100% equity allocation default for backtest transparency. That is position sizing, not alpha, and is not adopted here.

## Required data

Minimum source-implied inputs are timestamped OHLC bars sufficient to calculate Bollinger Bands, Keltner Channels, EMA200, close location within each bar, and ROC(3). Keltner construction normally requires range/ATR-like information, but the exact source implementation is underspecified and must be recovered before exact reproduction.

The source explicitly names major crypto pairs including BTC and ETH as suitable high-liquidity assets and states an intended 1-hour timeframe. No specific crypto venue or market type is mandated. Volume, funding, open interest, order-book data and aggressor-side trades are not part of the stated signal.

Point-in-time research must compute every feature only from information available by its signal timestamp. For 24/7 crypto, venue/data-vendor candle boundaries must be fixed before testing.

## Execution assumptions

The source uses phrases such as price `crosses above` and `crosses below`, but exact signal confirmation and fill timing are **underspecified**. Same-bar knowledge/fills must not be assumed without verifying causal order in the public Pine source.

Order type, fees, spread, slippage, latency, market impact, partial fills, leverage/margin and shorting mechanics are not specified in the reviewed description. Funding is not discussed and must be modeled if the later test uses perpetual futures. The source's 100% equity allocation is a backtest sizing default rather than evidence that such sizing is appropriate.

`research-proposed` causal convention if exact Pine timing cannot be recovered: calculate indicators on completed bars and execute no earlier than the next bar. This is not source-reported.

## Evidence
### Source-reported

The author describes the strategy as intended to avoid false breakouts by combining volatility compression, EMA200 structural direction, cumulative intra-bar bias and ROC momentum. The source states that the intended timeframe is 1H and that major crypto pairs such as BTC and ETH are among the high-liquidity assets for which it is suited.

No source-reported Sharpe, CAGR, drawdown, win rate, profit factor or other quantitative performance statistic is carried into this record because the reviewed public description does not provide a traceable figure required to state the hypothesis.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independent negative study was reviewed in this Scout cycle. The source itself does not establish that each confirmation contributes incremental alpha, and the multi-filter design can reduce trade count or create delayed entries after a volatility release. Exact channel and holistic-bias parameters remain underspecified. Absence of additional negative evidence is not evidence of robustness.

## Falsification plan

1. Recover exact public-source Bollinger, Keltner and holistic-bias definitions before claiming exact reproduction.
2. Compare the complete rule against a plain BB-inside-KC squeeze-release breakout using identical universe, timeframe, execution and costs.
3. Predeclare ablations for EMA200, holistic bias and ROC(3), individually and jointly, to measure incremental contribution rather than assuming every filter adds alpha.
4. Test the three-bar post-squeeze recency window and 15-bar cooldown against nearby fixed alternatives only as robustness checks, not as unconstrained optimization.
5. Evaluate out-of-sample across trending, ranging, high-volatility and low-volatility regimes and across multiple liquid crypto assets.
6. Stress fees, spread and slippage; include funding for perpetuals.
7. The composite thesis is materially weakened if its filters do not improve out-of-sample risk-adjusted continuation or false-breakout behavior relative to the simpler squeeze baseline after accounting for lower trade count and costs.

## Crypto portability

`direct` for the broad hypothesis because the cited source explicitly includes major crypto pairs such as BTC and ETH among its intended high-liquidity assets.

Crypto-specific testing must still account for 24/7 candle boundaries, venue fragmentation, liquidity/slippage, and—if perpetual futures are used—funding, mark/index pricing and liquidation mechanics. Direct source applicability is not evidence of crypto profitability.

## Limitations

- Exact Bollinger and Keltner parameters are **underspecified** in the reviewed public prose.
- Exact holistic-bias lookback and formula are **underspecified**.
- Entry/exit confirmation and fill timing are **underspecified**.
- Only explicit BUY-side entry logic was recovered from the reviewed description; no short-entry rule is invented.
- No independent reproduction was performed.
- No source-reported quantitative performance figure was carried into this record.
- Multi-filter complexity creates a material ablation requirement before attributing alpha to the composite.
- Not independently reproduced.

## Implementation status

`not-implemented`.

No implementation or backtest in the user's quantitative research stack was performed in this Scout cycle.

## Adoption boundary

Research material only. Presence in this repository does not imply profitable alpha, successful validation, implementation approval, paper/testnet/live approval, or authorization to trade.

## Related Wiki records

No stable Hermes Wiki Brain record was consulted or fabricated in this GitHub-only Scout cycle.

## Sources

- TradingView — `Pridarasx`, **Momentum Squeeze Breakout Engine**: https://www.tradingview.com/script/bN8jxMy5-Momentum-Squeeze-Breakout-Engine/ (public open-source strategy page; reviewed 2026-09-18; page date label `Jun 25`).
