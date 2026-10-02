---
schema: strategy-research-record-v1
title: TradingView Kangaroo Tail Structure Liquidity-Sweep Rejection
created: 2026-10-02
updated: 2026-10-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-02
sources:
  - https://www.tradingview.com/script/D5QnLQlC-GProf-Kangaroo-Tail/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Kangaroo Tail Structure Liquidity-Sweep Rejection

## Provenance

Public TradingView open-source indicator `GProf - Kangaroo Tail` by `GProfTrades`, published 2026-07-25 and reviewed 2026-10-02. Stable source URL: https://www.tradingview.com/script/D5QnLQlC-GProf-Kangaroo-Tail/ . Canonical TradingView script identity: `D5QnLQlC`.

## Economic mechanism

### Source-reported

The author describes a liquidity-sweep reversal event in which price makes a fresh multi-hour extreme through a meaningful pre-existing level, then rejects the excursion within the same candle. The setup requires rejection-candle anatomy plus structural confluence rather than treating a wick pattern alone as sufficient.

### Research interpretation

The falsifiable hypothesis is that a fresh-extreme sweep and same-bar rejection carries more short-horizon reversal information when the swept price is an already-mature structural level than a visually similar rejection candle without such level confluence. Component roles are: long lookback = freshness/congestion filter; wick/body geometry = rejection evidence; session/Camarilla/custom level = structural reference; level maturity = protection against treating a newly created extreme as prior structure. Whether each component adds incremental alpha is unproven and requires ablation.

## Signal

Source-reported normalized logic:

- Formation: detection is confirmed only at bar close.
- Short-side freshness: candle high is a new high versus a long lookback; default lookback is 78 bars, described as about 6.5 hours on 5-minute data. Long side is the mirror at a fresh low.
- Rejection anatomy: for a short, the entire candle body must lie in the bottom third of the candle range; the opposite wick is capped and the sweep wick must exceed a configurable percentage of completed daily ATR subject to a tick floor. Long logic is mirrored.
- Optional context: the body may be required to sit inside the prior candle's range. A large prior same-direction candle creates a caution tag rather than suppressing the signal.
- Structural level is mandatory. Eligible source-reported levels are PMH/PML, YH/YL, PDC, WH/WL, Camarilla R3/R4 for shorts and S3/S4 for longs, plus up to three user-supplied custom levels.
- The structural level must lie inside the sweep wick. If multiple levels lie inside the wick, the source names the one nearest the wick tip.
- Running levels such as WH/WL and live PMH/PML must remain untouched for a configurable maturity period before becoming eligible.
- Source-reported reference trade geometry is a trigger one tick beyond the completed rejection candle's extreme in the rejection direction, stop one tick beyond the sweep wick, and a 1:1 target. The indicator itself does not place trades or issue recommendations.
- Source states futures roll the "yesterday" reference at 18:00 ET and equities at the next regular-session open in Auto mode.
- Exact opposite-wick cap, sweep-wick ATR percentage, tick floor, level proximity/maturity defaults, session-window defaults, large-prior-candle threshold, and custom-level construction are not fully specified in the reviewed page and remain **underspecified**. They must not be inferred.

## Required data

- Intraday OHLC data with tick-size metadata.
- Completed daily OHLC/ATR inputs; the source states ATR uses completed daily bars.
- Historical bars sufficient for the fresh-extreme lookback.
- Venue/session timestamps and exchange timezone sufficient to construct PMH/PML, YH/YL, PDC, WH/WL and session rollover causally.
- Prior RTH high/low/close for Camarilla levels.
- Optional user-supplied higher-timeframe custom levels, whose causal construction would need separate specification.
- Source is built for index and commodity futures and says it can operate on liquid symbols. No crypto sample or crypto performance evidence is reported.
- Point-in-time constraint: only completed-bar information and structural levels that existed and had satisfied maturity at the signal timestamp may be used.

## Execution assumptions

The source states detection confirms on bar close and supplies reference geometry of entry one tick beyond the rejection candle extreme, stop one tick beyond the wick, and 1:1 target. It does not establish order type, gap handling, intrabar ordering, fill probability, fees, spread, slippage, impact/capacity, latency, partial fills, leverage/margin, or crypto funding. Those items are **underspecified**. A later implementation must predeclare them rather than assume frictionless fills.

## Evidence

### Source-reported

The source describes the rule construction and states that detection is non-repainting, uses completed daily ATR, and builds session levels without lookahead. No Sharpe, CAGR, drawdown, win rate, profit factor, or other performance statistic is reported or adopted here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source explicitly says the indicator is a candle pattern at a level rather than a trading recommendation and that a rejection candle does not guarantee future price behavior. No independent negative-result study was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

Research-proposed tests:

1. Compare the full structure-conditioned sweep/rejection signal against the same rejection-candle anatomy with no structural-level requirement.
2. Compare against a plain fresh-extreme sweep/reclaim baseline without body/wick anatomy filters.
3. Ablate level maturity, fresh-extreme lookback, prior-candle containment, and ATR-scaled wick requirement separately.
4. Separate session levels, Camarilla levels, and custom higher-timeframe levels rather than pooling them before their individual contribution is known.
5. Enforce point-in-time level availability, completed daily ATR, and bar-close confirmation with no retrospective swing/session leakage.
6. Stress trigger-stop geometry under next-tradable-price execution, gaps, spread, fees and slippage.
7. For crypto adaptation, test multiple 24/7 session boundaries and remove equity/futures-specific session semantics unless explicitly reconstructed.
8. Require chronological out-of-sample testing across multiple liquid instruments and volatility regimes.
9. **Research-defined falsification threshold:** materially weaken/reject the hypothesis if structural-level conditioning does not improve cost-adjusted, tail-aware out-of-sample results over the matched anatomy-only and sweep/reclaim baselines with stable direction across reasonable parameter neighborhoods.

## Crypto portability

adapted

The source is built for index and commodity futures and does not provide crypto evidence. The observable sweep/rejection mechanism can be ported to liquid crypto, but PMH/PML, RTH-derived Camarilla levels and "yesterday" rollover are session-dependent constructs that do not transfer directly to 24/7 markets. A crypto study must predeclare candle/session boundaries and distinguish spot from perpetual execution; perpetual tests additionally require funding and mark/index accounting.

## Limitations

- Not independently reproduced.
- No source-reported performance evidence.
- Several anatomy, maturity and proximity thresholds are **underspecified**.
- The causal liquidity-sweep interpretation is unproven; the directly observable event is a fresh-extreme wick through prior structure followed by same-bar rejection.
- Session-level semantics are native to futures/equities and require adaptation for 24/7 crypto.
- User-supplied custom levels are not independently reconstructable unless their generation rule is separately specified.
- Reference 1:1 trade geometry is not evidence that the indicator has positive expectancy.

## Implementation status

Research-only normalization. No implementation in the research stack and no Qlib full backtest has been completed.

## Adoption boundary

This record is research material only. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, is profitable or validated alpha, or is approved for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

No canonical Wiki link is asserted from this GitHub-only Scout cycle.

## Sources

- GProfTrades, `GProf - Kangaroo Tail`, TradingView, published 2026-07-25, reviewed 2026-10-02: https://www.tradingview.com/script/D5QnLQlC-GProf-Kangaroo-Tail/
