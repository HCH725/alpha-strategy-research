---
schema: strategy-research-record-v1
title: TradingView System 0530 Multi-Timeframe Stochastic RSI Confirmation
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-29
sources:
  - https://www.tradingview.com/script/FZmYNaYN-System-0530-Stoch-RSI-Strategy-with-ATR-filter/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView System 0530 Multi-Timeframe Stochastic RSI Confirmation

## Provenance

Public TradingView open-source strategy by Archertoria: "System 0530 - Stoch RSI Strategy with ATR filter", stable script ID `FZmYNaYN`. First published 2025-06-02 and updated 2025-06-04. Source reviewed as of 2026-09-29.

The 2025-06-04 release notes materially extend the earlier description, so this record treats the updated release description as the current source-reported strategy behavior rather than combining incompatible versions.

## Economic mechanism

### Source-reported

The source describes a multi-timeframe Stochastic RSI strategy intended to use a short timeframe for momentum-reversal initiation and a 15-minute timeframe for confirmation. An ATR filter is intended to avoid very-low-volatility conditions, while a same-direction cooldown is intended to reduce repeated signals.

### Research interpretation

Hypothesis: a short-horizon Stochastic RSI reversal from an extreme has higher continuation/reversal value when a higher-timeframe Stochastic RSI remains directionally aligned but has not yet fully left its corresponding extreme region. The ATR gate is a volatility-regime filter rather than the primary alpha signal, and the cooldown is execution/frequency control rather than predictive alpha.

This is a hybrid signal:
- Primary trigger: 5-minute Stochastic RSI K/D reversal from an extreme.
- Confirmation: 15-minute Stochastic RSI directional alignment and level constraint.
- Regime filter: minimum ATR in ticks.
- Frequency control: same-direction cooldown.
- Risk/exit: entry-bar stop and staged Stochastic-RSI take-profit logic in the updated release.

## Signal

Source-reported current-release logic:

- Operating chart: 5-minute; confirmation timeframe: 15-minute.
- Long trigger: 5-minute Stochastic RSI K crosses above D while K is below the configurable long trigger level.
- Short trigger: 5-minute Stochastic RSI K crosses below D while K is above the configurable short trigger level.
- After a trigger, wait up to `wait_window_5min_bars` for 15-minute confirmation.
- Long confirmation: 15-minute K is strictly greater than D and K is below `stoch_15min_long_entry_level`.
- Short confirmation: 15-minute K is strictly less than D and K is above `stoch_15min_short_entry_level`.
- No new entry signal is generated while a position is already open.
- A configurable same-direction cooldown applies.
- Earlier source text gives default 5-minute trigger levels of 30/70 and a default confirmation window of five 5-minute bars; it gives 15-minute confirmation thresholds of 40/60. The updated release notes describe these inputs but do not restate all defaults. These defaults therefore belong to the earlier published version and require source-code verification before treating them as unchanged current-release defaults.
- Stochastic RSI RSI length, Stochastic length, K smoothing, D smoothing, ATR period, ATR minimum, cooldown length, TP extreme thresholds, TP2 wait, and leverage multiplier are configurable; exact current defaults are not fully enumerated in the visible updated description and are therefore underspecified here.
- Entry: the source states an entry order is placed when trigger, confirmation and filters are satisfied. Exact same-bar/next-bar fill semantics are not stated in prose.
- Updated stop: entry 5-minute bar low for longs / high for shorts; a later 5-minute close beyond that level closes the position. Stop checks have priority over take-profit checks.
- Updated TP1: close 50% when either 5-minute or 15-minute Stochastic K reaches the configured extreme; alternatively, if that extreme condition is absent, use an opposing 5-minute K/D cross plus a confirming reversal in 15-minute K.
- Updated TP2: after TP1, another qualifying extreme starts a configurable waiting period; close the remaining 50% if the extreme persists through that wait. A zero-bar wait triggers immediately.
- Re-entry after a completed position is governed by the trigger/confirmation process and cooldown; additional lifecycle details are underspecified.

Point-in-time requirement: higher-timeframe Stochastic RSI values must be formed only from information available at the 5-minute decision timestamp. Whether the source implementation uses completed 15-minute bars or a developing 15-minute bar is not established by the reviewed prose and is a material data gap.

## Required data

- Source instrument context: the updated release says the strategy was specifically fine-tuned for SPY.
- Market type: U.S. equity/ETF context in the source; exact venue is not specified.
- Timeframes: 5-minute OHLCV chart plus 15-minute data.
- Fields: OHLC sufficient for price/stop logic; Stochastic RSI requires close history; ATR requires OHLC.
- Tick size is required if reproducing the ATR-in-ticks filter.
- Timestamp alignment between 5-minute and 15-minute bars is required.
- Point-in-time higher-timeframe availability must be modeled without future 15-minute information.
- Session/calendar convention and missing-bar handling are not specified.

## Execution assumptions

The source describes TradingView strategy entries but does not state a prose-level fill model, order type, commission, spread, slippage, market impact, latency, borrow/shorting assumptions, partial-fill handling, or capacity model.

The leverage multiplier is described by the source as primarily affecting theoretical TradingView backtest position sizing and not as a simulation of actual leveraged-trading risk.

For research reproduction, any chosen signal-to-order timing, completed-vs-developing 15-minute-bar convention, cost model, short-borrow model, or crypto execution convention must be labeled `research-proposed`.

## Evidence

### Source-reported

The source describes the rule set and says the updated strategy was specifically fine-tuned for SPY. No source-reported Sharpe, CAGR, drawdown, win rate, or other quantitative performance statistic is used in this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself warns that performance can vary across instruments and market conditions and suggests exploring alternative exits because the extreme-K TP2 can exit prematurely in trends.

The visible prose does not establish point-in-time semantics for the 15-minute series, creating a material look-ahead/repainting risk until verified.

No independently reproduced performance or transaction-cost evidence was found in the reviewed source.

## Falsification plan

1. Reconstruct the current source logic from point-in-time 5-minute and 15-minute bars and verify that no future 15-minute close leaks into a 5-minute decision.
2. Alpha ablation: compare the full 5m-trigger + 15m-confirmation signal against 5m-only Stochastic RSI and 15m-only directional controls at matched signal frequency.
3. ATR ablation: compare with and without the ATR gate to test whether the volatility filter adds predictive value rather than merely lowering turnover.
4. Cooldown ablation: hold the alpha signal fixed and test whether cooldown changes only turnover or materially changes conditional returns.
5. Exit separation: evaluate entry alpha under a fixed neutral holding/exit rule before attributing performance to the staged TP/SL overlay.
6. Test multiple non-overlapping regimes and a frozen out-of-sample period without retuning.
7. Apply realistic spread, fees, slippage and shorting assumptions; reject the hypothesis if any apparent edge is dependent on frictionless fills.
8. Test parameter stability around trigger/confirmation levels and the confirmation-window length rather than accepting a single fine-tuned SPY setting.
9. For any crypto adaptation, test spot and perpetual separately and include funding where applicable.

No numeric acceptance cutoff is asserted here; any future Scout-chosen cutoff would be a `research-defined falsification threshold`.

## Crypto portability

`adapted`

The momentum-confirmation mechanism is instrument-agnostic enough to test in crypto, but the source explicitly says the updated strategy was fine-tuned for SPY and provides no crypto empirical evidence.

Crypto adaptation must account for 24/7 candle boundaries, venue fragmentation, spot versus perpetual structure, funding, tick-size differences, fees/spread/slippage, and the chosen 15-minute point-in-time convention. Crypto profitability is unproven.

## Limitations

- Not independently reproduced.
- Current parameter defaults are partly underspecified in the visible updated description.
- Higher-timeframe point-in-time semantics are underspecified.
- Fill timing and execution costs are a data gap.
- Source is fine-tuned for SPY; portability is unproven.
- The initial 2025-06-02 description said exits were primarily reversing signals with no explicit stop/take-profit, while the 2025-06-04 release notes add explicit stop and two-stage take-profit behavior. This record follows the later release and does not merge the obsolete exit description into current logic.

## Implementation status

Research capture only. No implementation in the research stack and no Qlib full backtest has been completed as part of this Scout cycle.

## Adoption boundary

This record is research-only, not-implemented, and not-approved. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor/leaderboard entry, demonstrated profitable alpha, or received Paper, Testnet, or Live approval.

## Related Wiki records

No stable related Wiki record was resolved in this GitHub-only run; no Wiki link is fabricated.

## Sources

- TradingView, Archertoria, "System 0530 - Stoch RSI Strategy with ATR filter", public open-source strategy, published 2025-06-02, updated 2025-06-04, reviewed 2026-09-29: https://www.tradingview.com/script/FZmYNaYN-System-0530-Stoch-RSI-Strategy-with-ATR-filter/
