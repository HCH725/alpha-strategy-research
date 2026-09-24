---
schema: strategy-research-record-v1
title: TradingView Ehlers Fourier-Series Self-Tuning Cycle Reversal
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-24
sources:
  - https://www.tradingview.com/script/PDe533if-blackcat-L2-Ehlers-Fourier-Series-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Ehlers Fourier-Series Self-Tuning Cycle Reversal

## Provenance

Public TradingView open-source script: **[blackcat] L2 Ehlers Fourier Series Strategy**, author/page identity `blackcat1402`. The page shows original publication `Dec 27, 2020` and update `Apr 16, 2025`. Stable source URL: https://www.tradingview.com/script/PDe533if-blackcat-L2-Ehlers-Fourier-Series-Strategy/. Source reviewed as of 2026-09-24.

The author describes the implementation as a translation of John F. Ehlers' Fourier Series Strategy and explicitly provides the principal trading rules and current default indicator parameters. This record relies only on the public TradingView page, not on the referenced book/article as an independently reviewed source.

## Economic mechanism

### Source-reported

The source describes a cycle model built from three harmonic band-pass filters: fundamental, second harmonic, and third harmonic. It says the model is intended to identify a security's primary cycle period. The trading rule is self-tuning in the sense that the entry does not use a fixed oversold threshold: it looks for the FourierSeries(20) to reach a new 200-bar low and then turn upward. The source says the exit at the highest two-bar high is intended to capture small gains when the market is due for an upside move while reducing exposure.

### Research interpretation

The falsifiable hypothesis is that **an extreme-and-turn condition in a harmonic band-pass cycle representation contains incremental short-horizon reversal information beyond a simple price/return extreme-and-turn rule**. The 200-bar rolling extreme makes the threshold adaptive to recent history rather than fixed, while the Fourier construction attempts to isolate cyclic structure before applying the reversal trigger.

A critical ablation is therefore whether the Fourier layer adds information at all. If a raw return, detrended-price, or simple oscillator 200-bar extreme followed by an upturn performs equivalently out of sample, the harmonic construction has not demonstrated incremental alpha.

## Signal

Source-supported long-side rule:

- Indicator construction uses three harmonic band-pass filters: fundamental, second harmonic, and third harmonic.
- Current page defaults: price source `HL2`, fundamental period `20`, bandwidth `0.1`.
- Long entry condition: FourierSeries(20) reaches a new 200-bar low and then turns up.
- Order timing: buy at the **next bar market open** after that condition.
- Long exit: sell using a limit price equal to the **highest two-bar high**.
- The page also identifies `ROC` as the fast line and `Trigger` as the slow line and mentions crossover monitoring in the 2025 update.

Underspecified or ambiguous from the reviewed public page:

- exact mathematical equations and state initialization of the three band-pass filters are not reproduced in the public description reviewed here;
- exact formal definition of “turns up,” including equality handling;
- whether the two-bar-high limit is recomputed every bar while the position is open, and precise order persistence/cancellation semantics;
- position sizing, re-entry behavior, maximum holding period, stop-loss, and handling of unfilled exit limits;
- the 2022 release note says a short strategy was added, but the reviewed public description does not specify the short entry/exit state machine sufficiently to normalize it without guessing.

No short rule is invented here. Any later formalization of the ambiguous items above must be labeled `research-proposed`.

## Required data

Timestamped OHLC bars. `HL2` requires high and low; next-bar-open execution requires open; the rolling extreme and two-bar-high exit require historical bar data. The reviewed source does not require volume, funding, order book, trades/aggressor side, open interest, or options data.

The source does not constrain venue, instrument universe, or one mandatory timeframe. All rolling calculations must be point-in-time and must exclude future bars.

## Execution assumptions

One material execution detail is source-reported: the long entry is at next-bar market open. The long exit is described as a limit at the highest two-bar high.

The source page does not specify commissions, spread, slippage, market impact/capacity, leverage/margin, borrow, funding, latency, partial fills, gap handling, limit-order queue priority, or what happens when the exit limit remains unfilled. Those are data gaps, not zero-cost assumptions.

For crypto portability, perpetual funding and short mechanics would matter only if a short implementation were later defined; they are not supplied by this source.

## Evidence

### Source-reported

The author states that the script is a translation of Ehlers' Fourier Series Strategy and explains the long entry/exit rules. The 2025 update describes three harmonic band-pass filters and current defaults (`HL2`, fundamental `20`, bandwidth `0.1`).

No source-reported Sharpe, CAGR, drawdown, win rate, statistically tested alpha, or auditable performance table was identified in the reviewed public page text.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The author explicitly says they did not find a way to improve the indicator's performance because it was “not so good” relative to their expectation. The page also states that performance may vary between trending and ranging markets. The public description leaves material exit-order and short-side semantics unspecified, and no transaction-cost or fill analysis is supplied. These points materially weaken any presumption of profitability and make independent reconstruction necessary.

## Falsification plan

1. Reconstruct the harmonic estimator point-in-time from the public implementation before evaluating returns; reject any implementation that requires future bars or retrospective cycle selection.
2. Test the exact source-supported long rule with next-bar-open entry and realistic limit-fill logic, including conservative gap and queue assumptions.
3. Compare against simple controls using the same 200-bar adaptive-extreme idea: raw/detrended price, standardized return, RSI-like oscillator, and a single band-pass component. This is the primary ablation of whether the Fourier/harmonic layer contributes incremental information.
4. Ablate second and third harmonics individually and together. If the fundamental-only version is equivalent or better OOS, reject the added harmonic complexity.
5. Test the self-tuning 200-bar extreme against fixed historical thresholds and alternate past-only rolling windows; do not optimize the window on the evaluation sample.
6. Evaluate chronologically separated out-of-sample periods across trend, range, high-volatility, and low-volatility regimes, with parameters frozen using past-only information.
7. Stress fees, spread, slippage and adverse limit-fill assumptions. Reject or materially weaken the hypothesis if the apparent edge is not stable OOS, disappears under realistic costs/fills, or is matched by simpler extreme-and-turn controls.

## Crypto portability

**unproven**

The construction is OHLC-derived and can mechanically be evaluated on crypto bars, but the reviewed TradingView page does not provide crypto-specific validation. Crypto testing must account for 24/7 sessions, exchange-specific candle boundaries, venue fragmentation, spot/perpetual differences, perpetual funding where applicable, variable liquidity, and next-bar-open semantics in a continuously traded market.

The source's cycle assumptions should not be presumed stationary across crypto assets or timeframes.

## Limitations

- Exact filter equations/state initialization from the implementation: not independently reconstructed in this run.
- “Turns up” equality/state semantics: **underspecified**.
- Exit-limit persistence/fill behavior: **underspecified**.
- Short-side lifecycle: **underspecified** despite the source noting a short-strategy update.
- Position sizing, re-entry, maximum holding period and stop logic: **underspecified**.
- Cost/capacity model: **data gap**.
- Crypto evidence: **unproven**.
- Performance: **not independently reproduced**.

## Implementation status

Not implemented in the research stack. No Qlib full backtest, survivor promotion, leaderboard entry, Paper, Testnet, or Live validation is implied.

## Adoption boundary

Research-only. Presence in this repository does not mean the hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor, demonstrated profitability, or received implementation/Paper/Testnet/Live approval.

## Related Wiki records

No Wiki Brain lookup or write was performed because this Scout is GitHub-only. No Wiki relationship is asserted. Repository-level comparison families for later research include cycle/band-pass, spectral, oscillator-reversal, and adaptive-threshold strategies; similarity alone is not adoption evidence.

## Sources

- TradingView — blackcat1402, **[blackcat] L2 Ehlers Fourier Series Strategy** (public open-source script; published 2020-12-27; updated 2025-04-16; reviewed 2026-09-24): https://www.tradingview.com/script/PDe533if-blackcat-L2-Ehlers-Fourier-Series-Strategy/
