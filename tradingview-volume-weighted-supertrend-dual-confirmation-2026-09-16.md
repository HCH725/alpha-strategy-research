---
schema: strategy-research-record-v1
title: "TradingView Volume-Weighted Supertrend Dual Confirmation"
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
  - https://www.tradingview.com/script/wIqc0VyB-Volume-Weighted-Supertrend-Strategy-wbburgin/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Volume-Weighted Supertrend Dual Confirmation

## Provenance

Public TradingView open-source strategy by `wbburgin`, published 2023-06-23: `Volume-Weighted Supertrend Strategy [wbburgin]`.

Stable source URL: https://www.tradingview.com/script/wIqc0VyB-Volume-Weighted-Supertrend-Strategy-wbburgin/

Source reviewed as of 2026-09-16. The source page describes the strategy logic and configurable inputs; this record normalizes that description without reproducing the Pine source code.

## Economic mechanism

### Source-reported

The source combines two Supertrend-style directional states. The first applies Supertrend logic to a rolling VWAP rather than a conventional raw price source. The second applies analogous Supertrend logic to volume itself using a custom ATR construction for non-OHLC data. The volume-derived Supertrend acts as confirmation: a long signal requires both states to be up, while a sell signal requires both states to be down. The author states that the approach is intended for trending, high-volume assets and may work less well on lower timeframes.

### Research interpretation

This is a dual-confirmation trend-persistence hypothesis. The rolling-VWAP component asks whether volume-weighted price has established a volatility-adjusted directional regime; the volume component asks whether participation dynamics independently agree with that regime. The falsifiable claim is that requiring price/volume-state agreement filters some weak trend transitions that a price-only Supertrend would accept.

The volume confirmation should not be assumed to add alpha merely because it is an additional filter; an ablation against the VWAP-Supertrend alone is required.

## Signal

Source-normalized rule:

- Primary state: calculate a Supertrend from a rolling VWAP price source.
- Confirmation state: calculate a second Supertrend from volume using the author's custom non-OHLC ATR/Supertrend construction.
- Long / buy condition: VWAP-based Supertrend is trending up AND volume-based Supertrend is trending up.
- Short / sell condition: VWAP-based Supertrend is trending down AND volume-based Supertrend is trending down.
- Configurable inputs include volume length, ATR length, Supertrend multiplier, and the price source used by the price-side construction.
- The source reports strategy entries/exits can be displayed or hidden; hiding their visual markers does not change the underlying strategy logic.

Formation and causal timing: the public description establishes directional-state agreement but does not fully specify, in prose, every bar-indexing detail of the rolling VWAP, custom volume ATR, state-transition implementation, order timing, or how an existing opposite position is handled. Those details are therefore `underspecified` in this normalized record and must be resolved from the public source implementation before an exact reproduction.

The source does not define an independent stop-loss rule. Do not silently add one as part of the alpha signal.

## Required data

Minimum source-implied inputs:

- OHLC data needed by the price-side Supertrend construction;
- traded volume;
- bar timestamps;
- a chosen instrument and timeframe.

The rolling VWAP and volume-Supertrend states must be computed point-in-time using only information available through the signal bar. Exact venue, market type, session treatment, candle boundaries, missing-volume behavior, and volume comparability across venues are not specified by the source.

## Execution assumptions

The author's stated default strategy-report settings include 5% equity per trade, pyramiding of 5, and commission of 0.08% per trade. These are source-reported test settings, not independently validated recommendations.

The source explicitly states that the strategy does not include stops. Signal-to-order timing, same-bar versus next-bar execution, spread, slippage, market impact, funding, leverage/margin, partial fills, and shorting constraints are otherwise underspecified in the public description.

For later research, execution assumptions must be declared before evaluating performance rather than inferred from TradingView headline results.

## Evidence

### Source-reported

The author states that the strategy works best on trending assets with high volume and may perform less well on lower timeframes. The source page exposes a TradingView strategy report, but no performance statistic is promoted here as evidence because this Scout did not independently verify a stable, reproducible statistic/sample from the source.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The author explicitly identifies lower-timeframe use as potentially weaker and states that the strategy has no built-in stops. The trend-following construction also implies a testable vulnerability to choppy state flipping, but that latter point is research interpretation rather than a source-reported empirical result.

## Falsification plan

Test the hypothesis against a price-side VWAP-Supertrend baseline using identical universe, timestamps, execution assumptions, and costs.

Required comparisons:

1. VWAP-Supertrend alone versus dual VWAP + volume-Supertrend confirmation.
2. Trending versus range/choppy regimes.
3. High-volume versus lower-volume instruments/regimes.
4. Multiple predeclared timeframes, including lower timeframes where the source warns performance may degrade.
5. Gross versus realistic fee/slippage assumptions.

The volume-confirmation hypothesis is weakened if the dual-confirmation variant fails to improve out-of-sample risk-adjusted performance or drawdown/false-transition behavior relative to the primary VWAP-Supertrend baseline after accounting for its lower trade count and costs. Exact numeric acceptance thresholds are research-defined and must be predeclared in the downstream experiment rather than invented here.

## Crypto portability

`adapted`

The source presents a generic TradingView strategy and mentions trending/high-volume assets rather than demonstrating a dedicated crypto empirical study. Crypto is a plausible test venue because OHLCV is readily available and the market trades continuously, but portability remains unproven.

Crypto-specific risks include exchange-specific volume, spot-versus-perpetual volume differences, venue fragmentation, 24/7 candle boundaries, funding on perpetuals, and the possibility that a volume state computed on one venue does not represent market-wide participation.

## Limitations

- Not independently reproduced.
- Exact Pine-level state-transition and bar-indexing semantics are underspecified in the prose description.
- The source does not specify a stop-loss rule.
- The incremental value of the volume-derived Supertrend is unproven and requires ablation.
- Source-reported preferred market conditions are qualitative rather than a validated regime classifier.
- Crypto portability is unproven.

## Implementation status

No implementation or backtest in the user's research stack has been completed. This record only normalizes a public TradingView research hypothesis.

## Adoption boundary

Research material only. This record does not establish profitability, validated alpha, implementation approval, or authorization for paper, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain link was resolved in this GitHub-only Scout cycle; none is fabricated here.

## Sources

- TradingView — `Volume-Weighted Supertrend Strategy [wbburgin]`, wbburgin, published 2023-06-23: https://www.tradingview.com/script/wIqc0VyB-Volume-Weighted-Supertrend-Strategy-wbburgin/
