---
schema: strategy-research-record-v1
title: TradingView Price and Volume Breakout with Moving-Average Trend Filter
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
  - https://www.tradingview.com/script/jc2hs2qK-Price-and-Volume-Breakout-Buy-Strategy-TradeDots/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Price and Volume Breakout with Moving-Average Trend Filter

## Provenance

Public TradingView open-source strategy `Price and Volume Breakout Buy Strategy [TradeDots]` by `tradedots`, originally published 2024-05-06 and updated 2024-05-17. Stable source: https://www.tradingview.com/script/jc2hs2qK-Price-and-Volume-Breakout-Buy-Strategy-TradeDots/ . Source reviewed 2026-09-18.

Canonical TradingView script ID: `jc2hs2qK`.

The source describes a concurrent price-and-volume breakout over configurable examination windows, gated by a moving-average trend condition. The 2024-05-17 release notes add selectable long, short, or long-and-short direction and bearish price/volume breakout logic.

## Economic mechanism

### Source-reported

The author describes the strategy as targeting highly volatile assets with significant momentum spikes. The stated rationale is that simultaneous price and volume breakouts can indicate significant market movement, while the moving-average condition aligns entries with the prevailing trend. Bitcoin and Ethereum are explicitly named as suitable high-volatility applications; the source says the approach may be less effective in broader markets such as the S&P 500 where price and volume shifts are less pronounced.

### Research interpretation

The falsifiable hypothesis is that a price breakout has greater continuation value when participation also reaches an unusually strong contemporaneous volume extreme and the move is aligned with the prevailing moving-average trend. The components have distinct roles:

- Primary signal: closing-price breakout versus the prior examination window.
- Participation confirmation: volume breakout versus its examination window.
- Regime filter: price relative to a designated moving average.
- Direction extension: bearish price-and-volume breakout for short operation, introduced in the source update.

The mechanism is therefore joint price discovery plus participation confirmation, rather than volume or trend filtering alone. Whether simultaneous price/volume maxima add incremental alpha beyond a conventional price breakout is unproven and should be tested by ablation.

## Signal

Source-supported normalized logic:

- Formation: evaluated from chart-bar closing price and bar volume.
- Lookback: a configurable number of candlesticks is used as the examination window for price and volume; the exact default length is not stated in the reviewed page text and is `underspecified`.
- Long entry: the closing price and trading volume both surpass the maximum values observed over their predetermined examination windows, while price is above the designated moving average.
- Short capability: the 2024-05-17 source update explicitly adds bearish price-and-volume breakout logic and direction options `Long`, `Short`, and `Long and Short`; the exact bearish inequality and moving-average condition are not fully described in the reviewed prose and are therefore `underspecified`.
- Exit / holding: not specified in the reviewed source description.
- Re-entry: not specified.
- Moving-average type and length: not specified in the reviewed prose.
- Position sizing: source default setup states 70% equity per trade.

Causal implementation details such as whether the rolling maxima exclude the signal bar, and whether orders fill on the signal close or next bar, are not stated. No values are inferred for those fields.

## Required data

- OHLCV bars; the described signal specifically requires closing price and volume.
- A configurable rolling price/volume history sufficient for the examination windows.
- Moving-average input derived from bar prices.
- Source explicitly discusses Bitcoin and Ethereum as applications but does not bind the rule to one venue, market type, or timeframe.
- Timestamp/candle-boundary convention is not specified.
- For crypto, venue-specific volume must be treated as venue data rather than universal market volume.

## Execution assumptions

Source-reported default backtest settings include:

- commission: 0.01%;
- initial capital: USD 10,000;
- equity per trade: 70%.

The source does not specify market versus limit orders, same-bar versus next-bar fill semantics, spread, slippage, impact/capacity, leverage, funding, borrow/short mechanics, latency, or partial-fill handling. These remain `underspecified` and must not be silently supplied.

## Evidence

### Source-reported

The source says the strategy is particularly suited to highly volatile assets such as Bitcoin and Ethereum and notes that higher timeframes can sometimes yield fewer than 100 backtest trades because entries are stringent and holding periods can be long. It does not provide a traceable Sharpe, CAGR, drawdown, win rate, or other performance statistic in the reviewed page text.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself states that the approach may be less effective for broader markets such as the S&P 500 because price and volume shifts are less pronounced. No independent negative evidence was established during this Scout cycle; absence is not evidence of no negative result.

## Falsification plan

Test the source-supported joint-breakout hypothesis against simpler controls on liquid crypto markets:

1. Price breakout only.
2. Price breakout + moving-average regime filter.
3. Price breakout + volume breakout without the moving-average filter.
4. Full price breakout + volume breakout + moving-average filter.

`research-proposed`: use only causally available prior-bar rolling extrema when operationalizing the source's examination windows, and execute no earlier than after signal formation. The exact operational choice must be recorded before testing because the source prose does not resolve current-bar inclusion or fill timing.

Evaluate long and short directions separately, multiple volatility regimes, multiple liquid crypto instruments, realistic fees/slippage, and out-of-sample periods. The hypothesis is materially weakened if the volume-breakout condition fails to improve net out-of-sample continuation or drawdown characteristics versus the price-breakout controls across reasonable neighboring parameter settings.

## Crypto portability

direct

The source explicitly identifies Bitcoin and Ethereum as intended applications. Portability still depends on venue-specific volume, 24/7 candle boundaries, spot-versus-perpetual microstructure, and funding/mark-index accounting when perpetual contracts are tested.

## Limitations

- Exact examination-window defaults are `underspecified` in the reviewed page text.
- Moving-average type and length are `underspecified`.
- Exact bearish rule is `underspecified` beyond the source's explicit addition of bearish price/volume breakout capability.
- Exit and re-entry logic are `underspecified`.
- Signal-bar inclusion and execution timing are `underspecified`.
- No independently reproduced evidence.
- The source's qualitative attribution to smart-money activity is not independently established and should not be treated as a verified causal mechanism.

## Implementation status

Not implemented in the research stack. No backtest, runtime integration, paper trading, testnet, or live verification was performed by this Scout.

## Adoption boundary

Research-only. Presence in this repository does not imply profitable alpha, validation, implementation approval, paper/testnet approval, or live-trading approval.

## Related Wiki records

No stable related Hermes Wiki record was resolved in this GitHub-only Scout cycle; none is fabricated.

## Sources

- TradingView — `Price and Volume Breakout Buy Strategy [TradeDots]`, `tradedots`, published 2024-05-06, updated 2024-05-17: https://www.tradingview.com/script/jc2hs2qK-Price-and-Volume-Breakout-Buy-Strategy-TradeDots/
