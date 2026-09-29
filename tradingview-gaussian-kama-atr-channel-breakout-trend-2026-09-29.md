---
schema: strategy-research-record-v1
title: Gaussian-smoothed KAMA ATR-channel breakout trend hypothesis
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
  - https://www.tradingview.com/script/KpfB5jB8-Q-KAMA-Clarity-Trend/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Gaussian-smoothed KAMA ATR-channel breakout trend hypothesis

## Provenance

Primary source: public TradingView open-source indicator **Q KAMA Clarity Trend**, published by **Quantora** on 2025-05-07. Stable TradingView script identity: `KpfB5jB8`. Source reviewed as of 2026-09-29.

The public page describes Gaussian pre-smoothing, KAMA, and an ATR-channel breakout mode. This record normalizes that public description rather than redistributing the Pine source.

## Economic mechanism

### Source-reported

The author presents KAMA as an adaptive trend line, with Gaussian smoothing applied before KAMA to reduce noise. The default trend logic changes state when price breaks above or below a KAMA-centered ATR channel; a faster alternative uses direct price/KAMA crosses.

### Research interpretation

Hypothesis: Gaussian pre-smoothing may suppress high-frequency price noise, KAMA may adapt its response to directional efficiency, and requiring price to clear a volatility-scaled ATR envelope may reject small fluctuations around the adaptive trend estimate. The combined rule is therefore a volatility-normalized trend-initiation / persistence hypothesis, not evidence that each component independently adds alpha.

Component roles:

- Pre-filter: Gaussian smoothing of price.
- Adaptive reference: KAMA.
- Primary signal: breakout above/below KAMA plus/minus an ATR-scaled channel.
- Alternative source mode: direct price/KAMA cross; this is a separate faster specification and is not the primary hypothesis normalized here.
- Exit/risk: not specified by the source page.

## Signal

Primary source-described mode:

- Signal formation: when price breaks above the upper `KAMA + ATR channel` boundary, trend state changes bullish; when price breaks below the lower `KAMA - ATR channel` boundary, trend state changes bearish.
- Price source: configurable; source page states default is close.
- KAMA length: configurable; exact default value is not stated on the reviewed page.
- ATR length and multiplier: configurable; exact default values are not stated on the reviewed page.
- Gaussian filter length and sigma: configurable; exact default values are not stated on the reviewed page.
- Long entry operationalization: **research-proposed** — enter long on the next bar after a completed-bar bullish ATR-channel breakout.
- Short entry operationalization: **research-proposed** — enter short on the next bar after a completed-bar bearish ATR-channel breakout.
- Exit: underspecified by the source. **Research-proposed** for testing: exit/reverse only on a confirmed opposite channel breakout.
- Holding period: underspecified; under the research-proposed state-reversal implementation, hold until the opposite confirmed state.
- Re-entry: underspecified.
- Position sizing: not specified.
- Timeframe: not fixed by the source page.
- The rule is partially specified; parameter defaults and executable order semantics remain data gaps.

## Required data

- OHLC data sufficient to form the selected price source, KAMA, ATR, and Gaussian-smoothed input.
- Instrument/universe: not fixed by source.
- Venue and market type: not fixed by source.
- Timeframe: configurable/not fixed by source.
- Volume, funding, open interest, order book and options data: not required by the described signal.
- Timestamp/candle boundaries must be point-in-time consistent.
- For the research-proposed next-bar implementation, only completed-bar information may enter the signal.

## Execution assumptions

The TradingView page describes trend-state signals, not a complete execution model.

- Signal-to-order timing: not specified; next-bar execution is **research-proposed**.
- Order type and fill model: not specified.
- Fees, spread, slippage, impact/capacity: not specified.
- Funding, leverage/margin and borrow/shorting: not specified.
- Latency, partial fills and failures: not specified.

These omissions must not be interpreted as zero costs.

## Evidence

### Source-reported

The source describes the indicator's construction and intended trend-identification behavior. No source-reported performance statistic is relied upon in this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed source; absence is not evidence of no negative result. The construction is vulnerable to lag from sequential Gaussian/KAMA smoothing, whipsaw near channel boundaries, parameter sensitivity, and execution-cost erosion; these are research risks, not source-demonstrated failures.

## Falsification plan

1. Reconstruct the primary channel-breakout specification without guessing source defaults; parameter choices used in testing must be explicitly research-proposed.
2. Compare against simple price/KAMA cross, unsmoothed KAMA+ATR channel, fixed moving-average+ATR channel, and buy-and-hold/flat directional controls.
3. Ablate Gaussian smoothing and ATR gating separately to test whether either component adds incremental out-of-sample value.
4. Use leakage-safe chronological out-of-sample evaluation across multiple liquid crypto instruments and materially different volatility/trend regimes.
5. Apply realistic fee/spread/slippage and, for perpetuals, funding sensitivity.
6. Sweep KAMA, Gaussian and ATR parameters broadly rather than validating only a single tuned combination.
7. **Research-defined falsification threshold:** reject the alpha hypothesis if the combined construction fails to improve risk-adjusted out-of-sample performance over the simpler KAMA control after realistic costs, or if any apparent advantage depends on a narrow parameter island.

## Crypto portability

**unproven**

The mechanism uses generic price/volatility data and is technically portable to crypto, but the reviewed source page does not provide crypto-specific empirical validation. A crypto test must account for 24/7 candle boundaries, venue fragmentation, spot-versus-perpetual behavior, funding for perpetuals, and realistic execution costs.

## Limitations

- Not independently reproduced.
- Parameter defaults are underspecified on the reviewed source page.
- Entry/exit order semantics are underspecified.
- No source-backed trading-cost model.
- No source-backed crypto performance evidence.
- The source is an indicator description rather than a complete executable trading strategy.
- Incremental value of Gaussian smoothing, KAMA adaptation, and ATR gating is unproven.

## Implementation status

Research-only capture. No implementation in the research stack and no Qlib full-backtest validation has been completed.

## Adoption boundary

This record is research material only. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor/leaderboard entry, demonstrated profitable or validated alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No stable related Hermes Wiki Brain page was established during this GitHub-only Scout run; no Wiki link is fabricated.

## Sources

- Quantora, **Q KAMA Clarity Trend**, TradingView, published 2025-05-07, reviewed 2026-09-29: https://www.tradingview.com/script/KpfB5jB8-Q-KAMA-Clarity-Trend/
