---
schema: strategy-research-record-v1
title: TradingView Permutation-Entropy Structure-Rank Regime Filter
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
  - https://www.tradingview.com/script/Jm9cPu9E-Permutation-Entropy-Regime-Jayadev-Rana/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Permutation-Entropy Structure-Rank Regime Filter

## Provenance

Public TradingView open-source indicator **Permutation Entropy Regime [Jayadev Rana]**, published by `bluealgocapital` and visible as of 2026-09-24:

https://www.tradingview.com/script/Jm9cPu9E-Permutation-Entropy-Regime-Jayadev-Rana/

The source describes a closed-bar, non-future-looking regime indicator based on Bandt-Pompe-style permutation entropy of ordinal close patterns. This record normalizes the public description rather than redistributing the Pine script.

## Economic mechanism

### Source-reported

The source proposes that recent price action alternates between more ordered/structured and more random regimes. It uses permutation entropy to measure whether the six possible rank orderings of three consecutive closes are concentrated or approximately equiprobable. Low normalized entropy implies greater structure; high entropy implies more random-walk-like behavior. The source explicitly presents the tool as a context/filter layer rather than a standalone buy/sell signal.

### Research interpretation

The falsifiable hypothesis is that **ordinal-pattern concentration contains incremental information about strategy suitability beyond ordinary volatility, trend strength, and price efficiency**. If a low-entropy/high-Structure-Rank state genuinely identifies more persistent structure, a simple trend or breakout baseline should perform differently conditional on that state; conversely, a high-entropy/chop state should weaken directional follow-through. The value of the hypothesis lies in the entropy state itself, not in treating the source's regime labels as verified alpha.

A secondary, explicitly `research-proposed` hypothesis is that the source's `Structured Range` state may condition simple mean-reversion rules. This is not independently established by the source.

## Signal

Source-described construction:

1. Use rolling close data and form every group of three consecutive closes.
2. Assign each triplet to one of the six possible ordinal rank patterns; embedding dimension is fixed at 3.
3. Build the pattern-frequency histogram over an **Entropy Window**.
4. Compute Shannon entropy of that distribution and normalize it to `[0,1]`.
5. Define raw predictability as `(1 - normalized entropy) * 100` and optionally smooth it with an EMA (`Predictability Smoothing`).
6. Percentile-rank current predictability against its recent history over the **Structure Rank Lookback**, producing a 0-100 Structure Rank.
7. Compute a separate drift bias from the net share of up versus down closes across the window.
8. At confirmed bar close, classify:
   - `Structured Up`: Structure Rank >= Structured Level and positive drift bias;
   - `Structured Down`: Structure Rank >= Structured Level and negative drift bias;
   - `Structured Range`: high Structure Rank with drift near zero;
   - `Neutral`: Structure Rank between the two regime levels;
   - `Random / Chop`: Structure Rank <= Chop Level.

The public description exposes the parameter roles but does not state numeric defaults for Entropy Window, Predictability Smoothing, Structure Rank Lookback, Structured Level, Chop Level, or Drift Bias Threshold. Those values are therefore **underspecified** here and must not be invented.

Signal formation is confirmed bar close. The source states that historical closed-bar values do not repaint, uses no higher-timeframe requests, and uses no future-looking access. Ties among equal closes use a consistent rule, but the public description does not specify that exact tie-breaking implementation.

No complete entry, exit, holding-period, re-entry, position-sizing, stop, or portfolio lifecycle is source-specified. The source recommends using the state as a filter around an independent strategy.

## Required data

- Instrument/universe: source states symbol- and timeframe-agnostic; crypto applicability is therefore a hypothesis, not source-reported crypto evidence.
- Required field: close prices; timestamps sufficient to construct the selected bars.
- Timeframe: intraday or higher, according to the source.
- Rolling historical depth sufficient for the entropy window, smoothing, and Structure Rank percentile lookback.
- Point-in-time requirement: only information available through each confirmed bar close may be used.
- Missing bars and equal-close/tie handling must be deterministic and documented in any reproduction.
- For cross-venue crypto tests, candle boundary and venue must be fixed in advance.

## Execution assumptions

The source is a regime/context indicator, not an executable trading strategy, and does not specify order type, fills, fees, spread, slippage, impact, capacity, funding, leverage, borrow, latency, or partial-fill handling.

Any downstream test must separate regime measurement at bar close from subsequent execution. A minimal `research-proposed` implementation should condition a predeclared baseline signal at bar `t` and execute no earlier than the next executable observation after `t`, with venue-appropriate costs. Same-bar hindsight fills are not justified.

## Evidence

### Source-reported

The source explains the ordinal-pattern/entropy construction and states that it is intended to distinguish structured regimes from random/choppy conditions. It explicitly warns that structure is not direction quality, order-3 permutation entropy is coarse, small windows are noisy, large windows react slowly, and repeated equal closes in illiquid/low-volatility markets can bias the histogram.

No source-reported Sharpe ratio, CAGR, drawdown, win rate, predictive coefficient, or independently audited backtest result is relied upon in this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself states that the indicator describes current/past structure rather than predicting future prices and that a structured regime does not guarantee follow-through. Order-3 entropy discards amplitude information and may therefore collapse economically different paths into the same ordinal motif distribution. The adaptive percentile rank can also make an asset appear relatively structured even when its absolute predictability remains low.

No independent negative study specific to this TradingView implementation was identified in this Scout cycle; absence is not evidence of no negative result.

## Falsification plan

1. **Reconstruct first, trade second.** Independently reproduce the six-pattern histogram, normalized permutation entropy, predictability, smoothing, percentile rank, drift bias, and bar-close state transitions before testing returns. Resolve the exact tie rule and source defaults from auditable source material; otherwise pre-register research-proposed values rather than attributing them to the author.
2. **Baseline trend test.** Use a deliberately simple directional baseline (for example, predeclared price momentum or breakout) and compare unconditional OOS performance with performance conditioned on high Structure Rank. The entropy layer fails if it does not improve OOS risk-adjusted or hit-rate behavior after costs in a stable way.
3. **Incremental-information controls.** Compare the entropy gate with simpler controls using realized volatility, ADX/trend strength, Kaufman-style efficiency ratio, absolute return, and ordinary directional persistence. If permutation entropy adds no stable incremental information, reject the added complexity.
4. **Component ablation.** Test raw normalized entropy, smoothed predictability, percentile-ranked Structure Rank, and Structure Rank + drift separately. This determines whether any effect comes from ordinal entropy or merely from adaptive ranking/drift.
5. **Direction leakage control.** Because drift bias explicitly uses up/down closes, compare Structure Rank alone against Structure Rank + drift. Do not attribute directional alpha to entropy if the effect disappears without drift.
6. **Regime mapping test.** Predeclare forward horizons and test whether `Structured Up/Down` improves directional continuation and whether `Structured Range` improves a simple mean-reversion baseline. Treat these as separate hypotheses and correct for multiple testing.
7. **Parameter robustness.** Sweep reasonable entropy windows and Structure Rank lookbacks without selecting on the final test set. Require a broad stable region rather than a single optimum.
8. **Ordinal placebo.** Shuffle return signs/order within local blocks while approximately preserving volatility distribution. A purported entropy edge that survives destruction of ordinal sequence structure is evidence against the proposed mechanism.
9. **Crypto robustness.** Repeat across BTC/ETH and a predeclared liquid-alt universe, multiple venues where data permit, and several bar horizons. Test UTC candle-boundary shifts because 24/7 markets have no natural session close.
10. **Cost and latency sensitivity.** Apply realistic fees/spread/slippage to the independent baseline being gated. If apparent benefit comes only from hindsight bar-close execution or excessive switching, reject operational usefulness.

Failure action: if the permutation-entropy/Structure-Rank layer does not add stable OOS information over simpler regime controls, reject the layer rather than adding further filters.

## Crypto portability

**unproven**

The source states that the construction is symbol- and timeframe-agnostic, but the reviewed page does not provide crypto-specific empirical validation. Crypto testing must account for 24/7 candle boundaries, exchange fragmentation, spot-versus-perpetual differences, venue-specific missing bars, and potentially frequent equal closes on illiquid pairs. For perpetuals, funding and derivatives microstructure may affect the baseline strategy even though they are not inputs to the entropy measure itself.

## Limitations

- `not independently reproduced`
- `underspecified`: numeric source defaults are not stated in the reviewed public description.
- `data gap`: exact equal-close tie-breaking implementation is not specified in the reviewed description.
- `unproven`: no source-reported crypto OOS evidence is relied upon.
- Order-3 ordinal patterns are deliberately coarse and discard return magnitude.
- Percentile ranking is relative to recent history and can obscure low absolute predictability.
- The source is a regime filter, not a complete trading lifecycle.
- Multiple regime labels create multiple-testing risk if downstream researchers opportunistically choose the best mapping.

## Implementation status

No implementation or Qlib full-backtest reproduction has been completed in our research stack. This record is normalized external research only.

## Adoption boundary

Research-only. Presence in this repository does not mean this hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, is profitable or validated alpha, or is approved for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

No canonical Wiki link is asserted from this GitHub-only Scout cycle. Conceptually related families include entropy/regime filtering, trend-versus-mean-reversion regime selection, and volatility/market-efficiency conditioning; similarity alone is not equivalence.

## Sources

- TradingView — `bluealgocapital`, **Permutation Entropy Regime [Jayadev Rana]**, public open-source indicator, published 2026-07-14; accessed/as-of 2026-09-24: https://www.tradingview.com/script/Jm9cPu9E-Permutation-Entropy-Regime-Jayadev-Rana/
