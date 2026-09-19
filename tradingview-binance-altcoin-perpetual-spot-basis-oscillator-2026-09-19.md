---
schema: strategy-research-record-v1
title: Binance Altcoin Perpetual-Spot Basis Oscillator
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-19
sources:
  - https://www.tradingview.com/script/I0xAWNQa-BABI-Binance-Altcoin-Basis-Indicator/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Binance Altcoin Perpetual-Spot Basis Oscillator

## Provenance

Public TradingView open-source indicator page, **BABI - Binance Altcoin Basis Indicator**, author/page identity `Gokubro`. The page states an original publication date of 2022-03-31 and an update on 2022-04-01. Stable source: https://www.tradingview.com/script/I0xAWNQa-BABI-Binance-Altcoin-Basis-Indicator/ . Source reviewed as of 2026-09-19.

The source describes an oscillator formed from the basis between Binance altcoin perpetual-futures contracts and spot-market indexes, smoothed with a basic moving average. The published version explicitly lists BTC, ETH, LTC, ICP, SOL, LUNA, GRT, ATOM, ADA, XRP, ETC, and AVAX as supported USDT pairs; current symbol availability must be verified point-in-time rather than assumed from that historical list.

## Economic mechanism

### Source-reported

The author states that the indicator measures the basis between altcoin perpetual futures and spot-market indexes on Binance and smooths that series with a moving average. The author interprets spot premium as generally bullish and derivatives premium as generally bearish, and suggests that sufficiently high or low oscillator values could define buy/sell areas.

### Research interpretation

The falsifiable hypothesis is that **perpetual-versus-spot dislocation contains positioning information beyond price alone**. A derivatives premium may reflect crowded leveraged demand and therefore predict weaker subsequent returns or mean reversion, while relative spot strength may reflect less leveraged demand and therefore predict stronger subsequent returns. This is a positioning/basis hypothesis, not an established fact.

A competing explanation is that basis simply co-moves with contemporaneous momentum or funding and adds no incremental predictive information. Another is that extreme basis is continuation rather than reversal during persistent directional regimes.

## Signal

Source-supported construction:

1. Select a supported crypto asset.
2. Obtain its Binance perpetual-futures price and corresponding spot-market/index price.
3. Form a basis series between those two markets.
4. Smooth the basis with a basic moving average.
5. Interpret sufficiently extreme oscillator values as potential buy/sell areas; the source states that spot premium is generally bullish and derivatives premium generally bearish.

The exact basis formula/sign convention, moving-average type and length, numerical extreme thresholds, signal-formation timestamp, long/short Boolean rules, entry timing, exit, holding period, re-entry rule, and position sizing are **underspecified** on the reviewed public page.

Any later conversion of the oscillator into explicit quantile/z-score thresholds, cross-sectional ranks, fixed holding periods, or trading rules is **research-proposed** unless separately traced to the source.

## Required data

- Instrument/universe: crypto assets with both Binance spot/index and perpetual-futures series; the historical source lists BTC, ETH, LTC, ICP, SOL, LUNA, GRT, ATOM, ADA, XRP, ETC, and AVAX.
- Venue: Binance according to the source.
- Market type: spot/index plus perpetual futures.
- Fields: synchronized price observations for both legs; OHLC if implemented bar-wise.
- Timeframe: **underspecified**.
- Moving-average input/history sufficient for the selected smoothing window; exact window is **underspecified**.
- Point-in-time requirement: both legs must be aligned to information available at signal formation. Delistings, symbol migrations, contract changes, index construction, and historical venue availability must be handled without survivorship leakage.
- Funding is not stated as an input by the source, but should be retained as a control variable in later research because it can overlap economically with perpetual-spot basis.

## Execution assumptions

The reviewed source is an indicator, not a fully specified executable strategy. It does not establish signal-to-order timing, same-bar versus next-bar execution, order type, fill model, fees, spread, slippage, impact/capacity, funding treatment, leverage/margin, borrow/shorting, latency, or partial-fill behavior.

A later test must define these explicitly. If a two-leg basis trade is tested rather than a directional trade inferred from the oscillator, both-leg execution and funding/carry accounting are material and must be modeled separately.

## Evidence

### Source-reported

The source describes the basis oscillator and its qualitative bullish/bearish interpretation but does not provide a traceable Sharpe ratio, CAGR, drawdown, win rate, or other quantitative performance statistic on the reviewed page. No such precision is inferred here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No explicit negative empirical result is reported on the reviewed source page. Absence is not evidence of no negative result. The source is dated 2022, and the listed symbol universe and Binance market structure may not remain unchanged.

## Falsification plan

1. Reconstruct point-in-time Binance spot/index and perpetual prices for a survivorship-aware liquid-crypto universe.
2. First establish the exact basis sign convention and test both raw and smoothed basis without tuning thresholds to the full sample.
3. Compare the basis signal against simple price momentum/reversal, funding rate, and perpetual-only momentum baselines. Reject the incremental-alpha claim if basis adds no stable out-of-sample information beyond these controls.
4. Test competing directional hypotheses separately: extreme derivatives premium as subsequent reversal versus continuation, and relative spot premium as subsequent strength versus reversal.
5. Run asset-level and pooled tests rather than relying on a single coin. Report whether effects are concentrated in BTC/ETH or persist in liquid altcoins.
6. Use walk-forward/out-of-sample evaluation with parameters selected only from prior data. Stress multiple smoothing windows and threshold definitions; instability under modest parameter changes materially weakens the hypothesis.
7. Separate directional use of the oscillator from a market-neutral two-leg convergence trade. They have different exposures and execution economics and must not be conflated.
8. Apply realistic fees, spreads, slippage and, where perpetual positions are held, funding. Reject economically insignificant effects that disappear under plausible costs.
9. Stratify by volatility, trend, liquidity, and funding regimes. A signal that works only in one short historical episode should not be generalized.
10. Verify that all spot/perpetual observations were simultaneously available at signal time and that no current-symbol survivorship or index revision leaks into history.

## Crypto portability

**direct** — the source itself is explicitly constructed for Binance crypto spot/index and perpetual-futures markets and includes multiple crypto assets.

Portability across exchanges remains unproven. Venue-specific basis, funding mechanics, liquidity, index definitions, contract specifications, and candle boundaries can change the signal. A Binance result must not automatically be generalized to Bybit, OKX, Coinbase, or other venues.

## Limitations

- **underspecified:** exact basis equation/sign, smoothing parameters, thresholds, timeframe, entry, exit, holding period, re-entry, and sizing.
- **not independently reproduced.**
- **data gap:** the reviewed page does not provide a traceable performance study.
- Historical symbol support from 2022 must not be treated as a current tradable universe.
- Basis can be mechanically related to funding and contemporaneous momentum; incremental information is unproven.
- A qualitative statement that spot premium is bullish and derivatives premium bearish does not establish predictive alpha.

## Implementation status

No implementation in the research stack has been completed for this record. No backtest, formal validation, paper trading, testnet, or live verification is claimed.

## Adoption boundary

Research material only. Presence in this repository does not mean profitable, validated alpha, approved for implementation, approved for paper trading, approved for testnet, or approved for live trading.

## Related Wiki records

No stable Hermes Wiki Brain record is asserted from this GitHub-only Scout run.

## Sources

- TradingView — Gokubro, **BABI - Binance Altcoin Basis Indicator**: https://www.tradingview.com/script/I0xAWNQa-BABI-Binance-Altcoin-Basis-Indicator/ (published 2022-03-31; updated 2022-04-01; reviewed 2026-09-19).
