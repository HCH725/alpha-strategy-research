---
schema: strategy-research-record-v1
title: TradingView BTC 21:00-23:00 UTC intraday seasonality
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
  - https://www.tradingview.com/script/IzFZxayj/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView BTC 21:00-23:00 UTC intraday seasonality

## Provenance

Public TradingView open-source strategy: **Customizable BTC Seasonality Strategy**, published 2024-10-30 by EdgeTools. Canonical source: https://www.tradingview.com/script/IzFZxayj/. Source reviewed as of 2026-09-18.

The TradingView description attributes the underlying seasonality claim to Padysak & Vojtko (2022), *Seasonality, Trend-following, and Mean reversion in Bitcoin*. This Scout cycle is TradingView-only, so the paper was not independently used to fill or verify strategy details.

Repository deduplication on current `main` found no record with canonical TradingView source `IzFZxayj` or the same normalized 21:00-23:00 UTC fixed-window long signal. Existing intraday-seasonality records concern materially different clock structures or signals.

## Economic mechanism

### Source-reported

The TradingView author states that Bitcoin has historically exhibited higher-than-average returns from 21:00 UTC to 23:00 UTC, when major traditional exchanges are closed, and proposes that reduced competing traditional-market activity may contribute to the effect.

### Research interpretation

This is a deterministic clock-time seasonality hypothesis rather than a price-conditioned technical signal. The falsifiable mechanism is that Bitcoin return distribution during the 21:00-23:00 UTC window differs positively from other hours because cross-market participation and liquidity conditions change when major traditional exchanges are closed. The causal explanation is unproven by this Scout cycle and should be separated from the observable time-of-day anomaly.

## Signal

Source-specified default rule:

- Instrument: Bitcoin.
- Direction: long only.
- Formation/entry timing: enter at a user-configurable UTC time; source default is 21:00 UTC.
- Exit timing: exit at a user-configurable UTC time; source default is 23:00 UTC.
- Default holding period: two hours.
- Price, momentum, trend, volume, or volatility filters: none described by the source.
- Re-entry: the description implies the time-window rule recurs by day, but exact order-state/re-entry semantics are **underspecified**.
- Exact bar-resolution requirements and same-bar versus next-bar fill semantics are **underspecified**.

No missing operational details are silently supplied.

## Required data

- Bitcoin price series with timestamps sufficient to identify 21:00 and 23:00 UTC exactly.
- OHLC data at a resolution capable of representing the entry/exit times without look-ahead.
- Venue/market type: **underspecified** by the reviewed TradingView description.
- Timestamp normalization must be UTC and point-in-time safe.
- A downstream crypto test should preserve venue-specific 24/7 candles rather than importing equity-session boundaries.

## Execution assumptions

The source specifies the clock times but does not specify order type, exact fill convention, bid/ask spread, slippage, fees, market impact, capacity, leverage, margin, or partial-fill handling. These are **underspecified** and must be modeled explicitly in later research.

A downstream implementation must not assume a frictionless fill at the displayed clock price merely because the source describes entry at 21:00 and exit at 23:00 UTC.

## Evidence

### Source-reported

The TradingView page attributes the 21:00-23:00 UTC anomaly to Padysak & Vojtko (2022). It also reports a 33% annualized return, 20.93% volatility, and -22.45% maximum drawdown for the described seasonality approach. These figures are third-party/source-reported claims from the TradingView page and were not independently verified in this cycle.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independent negative evidence was reviewed in this TradingView-only cycle. The source-reported effect may be sample-, venue-, timezone-, or regime-dependent; absence of contrary evidence in the reviewed page is not evidence of robustness.

## Falsification plan

Research-proposed validation should test the fixed 21:00-23:00 UTC long window against all other two-hour UTC windows using point-in-time Bitcoin data across multiple non-overlapping regimes and venues. Compare gross and net returns, hit rate, volatility, drawdown, and risk-adjusted return after realistic fees and spread/slippage.

`research-defined falsification threshold`: reject or materially weaken the hypothesis if the 21:00-23:00 UTC window does not retain a positive and economically meaningful out-of-sample net-return advantage over alternative clock windows after costs, or if the apparent advantage is concentrated in a narrow historical subperiod or single venue.

Also test sensitivity to daylight-saving changes in traditional-market schedules; the TradingView rule itself is fixed in UTC, while the proposed explanatory mechanism references traditional exchanges whose local opening/closing times can shift relative to UTC.

## Crypto portability

direct

The source itself is explicitly a Bitcoin seasonality strategy. Portability across Bitcoin spot versus perpetual venues remains unproven. Perpetual testing additionally requires funding and mark/index accounting, while venue fragmentation can alter realized intraday liquidity and execution costs.

## Limitations

- The causal explanation linking the anomaly to traditional-market closure is **unproven** in this Scout cycle.
- Venue, market type, bar resolution, and execution semantics are **underspecified**.
- The source-reported performance statistics are **not independently reproduced**.
- The cited underlying paper was not independently reviewed because this cycle is constrained to TradingView-only research.
- Time-of-day anomalies are vulnerable to data-mining, regime drift, timezone mistakes, and transaction-cost erosion.

## Implementation status

Not implemented in the research stack. No backtest, runtime implementation, paper trading, testnet, or live validation was performed in this Scout cycle.

## Adoption boundary

Research-only. Presence in this repository does not establish profitable alpha, independent validation, implementation approval, paper/testnet approval, or live-trading authorization.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted in this GitHub-only Scout cycle.

## Sources

- TradingView — EdgeTools, **Customizable BTC Seasonality Strategy**, published 2024-10-30: https://www.tradingview.com/script/IzFZxayj/ (reviewed 2026-09-18).
