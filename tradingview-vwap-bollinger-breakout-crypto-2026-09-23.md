---
schema: strategy-research-record-v1
title: TradingView VWAP-Bollinger breakout for crypto
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
  - https://www.tradingview.com/script/wUN7ZnGM-VWAP-Bollinger-Bands/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView VWAP-Bollinger breakout for crypto

## Provenance

Public TradingView open-source strategy **VWAP-Bollinger Bands**, author/page identity `Wayne-o`, originally published 2021-04-19 and updated 2023-06-19. Stable source: https://www.tradingview.com/script/wUN7ZnGM-VWAP-Bollinger-Bands/ . Source reviewed as of 2026-09-23.

The source explicitly discusses crypto and gives a crypto daily-chart default of 30 periods. This record normalizes the public description rather than reproducing or redistributing the Pine source.

## Economic mechanism
### Source-reported

The author describes a Bollinger-style breakout strategy in which VWAP is used as the band source. A high crossing the upper band is a buy signal and a low crossing the lower band is a sell signal. The source says the defaults target daily charts and uses 30 periods for crypto, approximately aligning the window with a month.

### Research interpretation

The falsifiable hypothesis is that a volatility-band breakout measured around a volume-weighted price reference captures persistent directional repricing better than either a conventional price-centered Bollinger breakout or a simple VWAP location rule. The proposed mechanism is trend/volatility expansion after price moves sufficiently far from recent volume-weighted consensus.

This interpretation must not assume that VWAP contributes incremental alpha. The key research question is whether the VWAP-centered construction adds information beyond ordinary breakout and momentum baselines.

## Signal

Source-supported normalized rule:

- Intended default timeframe: daily.
- Crypto lookback: 30 periods.
- Center/source: VWAP used as the Bollinger-band source.
- Long entry: bar high crosses the upper band.
- Short/sell entry: bar low crosses the lower band.
- The source mentions position sizes between 1% and 10% of equity in its reported testing context and a 0.1% fee assumption aligned by the author with Binance fees; these are source-reported test assumptions, not recommended sizing or current fee facts.
- Exact Bollinger deviation multiplier, VWAP anchoring/reset convention, exit/reversal semantics, pyramiding behavior, order timing, and whether an opposite signal closes and/or reverses an existing position are underspecified in the public description reviewed here.

No missing rule is inferred from the source code. Any future completion of the lifecycle must be labeled `research-proposed` unless verified against the source.

## Required data

- Crypto OHLCV.
- Daily bars for the source-described default use case.
- Volume sufficient to construct a source-compatible VWAP.
- Point-in-time bar timestamps with a documented daily candle boundary.
- A source-compatible definition of VWAP anchoring/reset is a data/implementation gap that must be resolved before faithful reproduction.

## Execution assumptions

The source reports a 0.1% fee assumption in its testing context and mentions 1%-10% equity per trade. It does not sufficiently specify spread, slippage, impact, same-bar versus next-bar fills, market versus limit orders, funding, borrow/short mechanics, leverage, latency, partial fills, or failure handling.

Because entries depend on intrabar high/low crossing a band, a bar-close implementation can materially differ from an intrabar implementation. A future test must avoid assuming fills at the crossing price without a justified execution model.

## Evidence
### Source-reported

The author states that they had seen good results in crypto and stocks and reports using 1%-10% equity per trade with a 0.1% fee in the described testing context. No traceable Sharpe, CAGR, drawdown, sample dates, trade count, or other quantitative performance statistic is provided on the reviewed page, so none is recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-specific negative empirical result was identified on the reviewed TradingView page; absence is not evidence of no negative result. The strategy is vulnerable to breakout whipsaw, intrabar fill ambiguity, VWAP-anchor ambiguity, and transaction-cost sensitivity.

## Falsification plan

Research-proposed:

1. Reconstruct the source-compatible daily crypto rule only after the VWAP anchor/reset and band multiplier are verified; otherwise classify the test as an adaptation rather than reproduction.
2. Use liquid crypto spot and/or perpetual cohorts with point-in-time OHLCV and explicit candle boundaries; keep market types separate.
3. Compare against at least: buy-and-hold/short-neutral controls as applicable, simple price momentum, Donchian/high-low breakout, conventional close-centered Bollinger breakout, and a simple price-above/below-VWAP rule.
4. Ablate the VWAP-centered band construction. If conventional Bollinger or simple momentum explains the result, reject the claim of incremental information from the VWAP layer.
5. Test the source 30-period crypto window plus a small predeclared neighborhood rather than optimizing a broad grid.
6. Test both bar-close/next-bar execution and a conservative intrabar-cross approximation. Do not use same-bar favorable fills that require unavailable path information.
7. Apply realistic fee, spread and slippage sensitivity. For perpetuals, include funding separately.
8. Require walk-forward or chronological out-of-sample stability across multiple crypto regimes and venues where data permit.
9. Reject the hypothesis if net OOS performance is not economically meaningful after costs, is dominated by simpler baselines, depends on one asset/regime, or disappears under conservative crossing/fill assumptions.

## Crypto portability

direct

The source explicitly describes a crypto configuration. Portability remains sensitive to 24/7 daily-bar boundaries, venue-specific volume, VWAP construction, spot versus perpetual market structure, funding for perpetuals, and exchange fragmentation.

## Limitations

- Exit/reversal lifecycle: underspecified.
- Bollinger deviation multiplier: underspecified in the reviewed public description.
- VWAP anchoring/reset convention: underspecified/data gap.
- Intrabar crossing and fill semantics: underspecified.
- Source-reported performance is qualitative and not independently reproduced.
- The strategy can collapse to a generic volatility breakout if the VWAP layer adds no incremental information.

## Implementation status

Research-only normalization. No implementation or Qlib full-backtest validation has been completed for this record.

## Adoption boundary

This record is research material only. It has not passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib full-backtest validation, become a frozen survivor or leaderboard entry, or received Paper, Testnet, or Live approval. It is not evidence of profitability or validated alpha.

## Related Wiki records

- `tradingview-btc-rsi-bollinger-mean-reversion-2026-09-17.md` — adjacent Bollinger family with materially different mean-reversion logic and RSI confirmation.
- `rsi-mean-reversion_ohlcv-2026-08-31.md` — adjacent VWAP/reversal family; not the same breakout construction.

## Sources

- TradingView, Wayne-o, **VWAP-Bollinger Bands**, published 2021-04-19, updated 2023-06-19, reviewed 2026-09-23: https://www.tradingview.com/script/wUN7ZnGM-VWAP-Bollinger-Bands/
