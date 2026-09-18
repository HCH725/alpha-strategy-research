---
schema: strategy-research-record-v1
title: TradingView BTC Momentum Breakout with EMA/RSI Confirmation
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
  - https://www.tradingview.com/script/MAcKqYlk-RTB-Momentum-Breakout-Strategy-V3/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView BTC Momentum Breakout with EMA/RSI Confirmation

## Provenance

- Platform: TradingView.
- Public open-source strategy: `RTB - Momentum Breakout Strategy V3`.
- Author/page identity: `Ramtraderbook`.
- Stable public source: https://www.tradingview.com/script/MAcKqYlk-RTB-Momentum-Breakout-Strategy-V3/
- Publication date shown by TradingView: 2025-04-29.
- Source reviewed as of: 2026-09-18.
- The TradingView page describes a directional breakout strategy using EMA trend confirmation, RSI momentum confirmation, recent support/resistance breakout levels, and ATR-based risk management. Large Pine source passages are not reproduced here.

## Economic mechanism

### Source-reported

The author describes the strategy as a momentum-based directional breakout system. Recent support/resistance levels define breakout opportunities; EMA and RSI conditions are intended to confirm trend and momentum before entry. ATR is used for dynamic stop-loss and trailing-stop management.

The author reports testing the default configuration on BTCUSDT Futures (Bybit), 4-hour bars, with 0.05% commission per trade.

### Research interpretation

The falsifiable alpha hypothesis is that a break beyond a recent price boundary has greater continuation probability when the broader EMA-defined direction and RSI-defined momentum agree with the breakout. The proposed mechanism is trend persistence after a locally constrained price level is breached; EMA and RSI act as conditioning variables intended to reject weak or counter-regime breakouts.

ATR-based stops and trailing exits are risk/exit logic, not independent evidence of predictive alpha. A later test should therefore ablate the EMA and RSI confirmations separately from the breakout signal and from ATR trade management.

## Signal

Source-supported normalized logic:

- Primary signal family: directional breakout of recent support/resistance.
- Trend confirmation: exponential moving average condition(s).
- Momentum confirmation: RSI condition(s).
- Risk/exit component: ATR-based stop-loss and trailing-stop levels.
- Source-reported test context: BTCUSDT Futures on Bybit, 4-hour timeframe.

The reviewed TradingView description does not expose enough detail to state the exact EMA lengths, RSI thresholds, support/resistance lookback, breakout comparison semantics, ATR period/multipliers, precise long/short Boolean expressions, re-entry behavior, or exact order timing without inspecting/copying implementation details beyond the normalized public description. These fields are therefore `underspecified` here rather than guessed.

No additional operationalization is introduced in this record. Any future choice of missing parameters or causal order timing must be labeled `research-proposed` before testing.

## Required data

Source-supported requirements:

- Instrument/test context: BTCUSDT Futures on Bybit.
- Timeframe/test context: 4-hour bars.
- Bar data sufficient to derive recent support/resistance, EMA, RSI, and ATR; therefore OHLC is required.
- Trading commission is material; the source-reported backtest context uses 0.05% commission per trade.

Volume, funding, mark/index prices, open interest, order book, aggressor-side trades, and other derivatives fields are not stated as signal inputs in the reviewed description. Exact candle timezone/boundary and missing-data handling are `underspecified`.

## Execution assumptions

Source-reported:

- ATR-based stop-loss and trailing-stop levels are part of trade management.
- The described backtest uses 0.05% commission per trade.

Underspecified by the reviewed source description:

- same-bar versus next-bar execution;
- market versus limit orders;
- fill model;
- spread and slippage;
- market impact/capacity;
- funding treatment;
- leverage and margin assumptions;
- latency, partial fills, and order failures;
- exact position-sizing rule.

No missing execution assumption is silently filled.

## Evidence

### Source-reported

The author states that the strategy was backtested with default parameters on BTCUSDT Futures (Bybit), 4-hour timeframe, with 0.05% commission per trade. The reviewed public description does not provide a sufficiently traceable performance statistic that should be promoted into this record as verified evidence.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independent negative evidence was established in this Scout cycle. Mechanistically, breakout systems can be vulnerable to range-bound whipsaw and parameter sensitivity, but those are research risks to test rather than source-established failures. Absence of identified negative evidence is not evidence of robustness.

## Falsification plan

A later research implementation should test the normalized hypothesis against a plain recent-level breakout baseline on BTCUSDT perpetual/futures data and across multiple market regimes. Required ablations should include: breakout alone; breakout + EMA; breakout + RSI; breakout + EMA + RSI; and the same predictive variants under common exit logic so ATR trade management is not mistaken for signal alpha.

Any exact lookbacks, thresholds, order timing, cost assumptions beyond the source-reported 0.05% commission context, or acceptance thresholds selected by our research process are `research-proposed`; any Scout/research-team acceptance cutoff must be labeled `research-defined falsification threshold` before use. The hypothesis is weakened if the confirmation layers fail to improve out-of-sample continuation quality or cost-adjusted performance versus the simpler breakout baseline.

## Crypto portability

`direct`

The source itself reports a BTCUSDT Futures / Bybit / 4-hour test context, so the mechanism is directly framed for crypto derivatives rather than ported from a traditional-asset sample. Cross-venue portability remains unproven. Later testing must account for venue-specific candles, fees, spread/slippage, perpetual funding where applicable, and mark/index versus traded-price differences.

## Limitations

- `underspecified`: exact EMA parameters and condition semantics.
- `underspecified`: RSI period/threshold logic.
- `underspecified`: support/resistance lookback and breakout comparison semantics.
- `underspecified`: ATR period, multipliers, and exact stop/trailing mechanics.
- `underspecified`: position sizing and exact order timing.
- `not independently reproduced`.
- Source-reported testing context does not establish robustness across venues, assets, timeframes, or unseen regimes.

## Implementation status

`not-implemented`

No implementation or backtest in our research stack was performed in this Scout cycle.

## Adoption boundary

`research-only` / `not-approved`

Presence in this repository means only that the public TradingView hypothesis has been normalized for later research. It is not evidence of validated alpha and is not approval for implementation, paper trading, testnet, or live trading.

## Related Wiki records

None asserted. No Wiki link is fabricated.

## Sources

- TradingView — Ramtraderbook, `RTB - Momentum Breakout Strategy V3`: https://www.tradingview.com/script/MAcKqYlk-RTB-Momentum-Breakout-Strategy-V3/ (published 2025-04-29; reviewed 2026-09-18).
