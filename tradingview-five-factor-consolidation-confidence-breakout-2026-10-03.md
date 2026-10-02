---
schema: strategy-research-record-v1
title: TradingView Five-Factor Consolidation Confidence Breakout
created: 2026-10-03
updated: 2026-10-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-03
sources:
  - https://www.tradingview.com/script/D521qQHe-AlphaX-Consolidation-Engine-Squeeze-Detection-Breakout-Signals/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Five-Factor Consolidation Confidence Breakout

## Provenance

Public TradingView open-source indicator **AlphaX Consolidation Engine Squeeze Detection Breakout Signals**, author **AlphaX-Trade**, canonical source identity `D521qQHe`. Stable source: https://www.tradingview.com/script/D521qQHe-AlphaX-Consolidation-Engine-Squeeze-Detection-Breakout-Signals/ . Source reviewed as of 2026-10-03.

The source describes an indicator rather than a fully specified executable strategy. This record therefore preserves the source-reported state machine and treats any backtest mapping beyond those statements as `research-proposed`.

## Economic mechanism

### Source-reported

The author frames the setup as volatility compression followed by expansion. A five-factor consolidation score combines ATR percentile, Bollinger Band Width, TTM Squeeze state, linear-regression slope, and ADX. When consolidation is recognized, the script tracks an active high/low range. A breakout is signaled when price closes beyond that range with an ATR buffer and sufficient confidence; confidence incorporates squeeze quality, consolidation quality/duration, relative volume and volume bias, momentum alignment, and candle quality. The script also identifies post-breakout retests and failed breakouts.

The author states that calculations are non-repainting and signals are confirmed on bar close.

### Research interpretation

The falsifiable hypothesis is that **a close beyond a range formed during independently measured low-volatility/low-trend conditions contains more continuation information than an otherwise identical generic range breakout, and that pre-breakout compression quality plus contemporaneous volume/momentum/candle confirmation adds incremental information beyond the price breakout itself**.

Component roles:

- Regime / formation: five-factor compression score.
- Primary signal: confirmed close beyond the tracked consolidation high/low plus ATR buffer.
- Confirmation: confidence score using squeeze persistence, range quality/duration, relative volume/volume bias, momentum alignment and candle body quality.
- Secondary entry context: retest of the broken boundary.
- Thesis failure / exit context: re-entry into the original range, opposite breakout, or ATR trailing-stop event.

The source's "institutional" language is not treated as evidence of institutional activity. A simpler explanation is that the construction repackages ordinary volatility compression, breakout magnitude, trend and volume information without incremental alpha.

## Signal

Source-reported signal sequence:

1. On each completed bar, compute five consolidation components: ATR percentile, Bollinger Band Width compression, TTM Squeeze, linear-regression slope flatness, and ADX ranging condition.
2. Combine them into a 0-100 consolidation score. The source states a default consolidation threshold of 50.
3. While consolidation is active, track the range high and range low.
4. After the range exists, a bullish/bearish breakout requires a bar close beyond the corresponding boundary plus an ATR threshold. Candle-body quality, optional volume confirmation and a minimum breakout-confidence score condition the signal.
5. The source states a default minimum breakout confidence of 35%. Its described score includes squeeze quality (up to 20 points), consolidation quality (up to 15), duration (up to 10), volume confirmation (up to 15), momentum alignment (up to 17), candle quality (up to 5), and penalty deductions for RSI overextension, contradicting volume bias and EMA trend conflict.
6. A retest signal may occur when price returns to the broken boundary within a configurable window, holds it, and confirms with a directionally aligned candle.
7. Source-described invalidation/exit markers include ATR trailing stop, re-entry into the original range, and an opposite breakout.

Source-described discretionary entry mapping is breakout-label close for an aggressive entry or retest-label confirmation for a conservative entry. Exact executable order semantics are not specified.

Underspecified by the public description: exact ATR/BB/KC periods, percentile lookbacks, component scoring formula, LR slope threshold, ADX threshold, minimum consolidation bars, breakout ATR multiplier, volume-ratio threshold, RSI/MACD/EMA periods, retest window/tolerance, exact confidence aggregation, and all order-fill/re-entry semantics.

Any fixed choices for those gaps in a future implementation are `research-proposed`, not source-reported.

## Required data

- OHLCV bars.
- Sufficient point-in-time history for ATR percentile, Bollinger/Keltner calculations, linear-regression slope, ADX, RSI, MACD, EMA and relative-volume calculations.
- Volume is required for volume confirmation/bias; the source warns that volume bias may be less accurate where only tick volume is available.
- Timestamp-consistent completed bars; signals must use information available by the relevant bar close.
- The source says defaults are tuned for XAUUSD and major indices on 5-minute bars. Crypto is mentioned as requiring parameter adjustment, not as demonstrated crypto evidence.

No order-book, trades/aggressor-side, funding, open-interest or options data is source-required.

## Execution assumptions

The source describes bar-close confirmation but does not specify a reproducible fill model, spread, fees, slippage, market impact, latency, partial fills, leverage/margin, shorting constraints or capacity.

For future falsification, a `research-proposed` implementation should prevent same-bar lookahead: compute the signal only after the completed bar and use a causally available next executable price unless a separately justified bar-close fill model is tested. Costs should be applied explicitly rather than inferred from the indicator.

Stops below a breakout candle or opposite range boundary are mentioned as usage guidance, while the indicator also exposes an ATR trailing stop. Position sizing is not specified as alpha logic.

## Evidence

### Source-reported

The source describes the indicator logic and configurable defaults but provides no independently auditable profitability statistic in the reviewed public description. It states that the default configuration is tuned for XAUUSD and major indices on 5-minute bars and that crypto should use higher ATR thresholds and a larger trailing-stop multiple. These are author usage claims, not crypto validation.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source explicitly notes that signal accuracy/profitability is not guaranteed, volume bias can be less accurate where true volume is unavailable, and frequent failed breakouts indicate continued ranging conditions. The public description provides no controlled comparison showing that the five-factor score or confidence layer improves on simpler compression/breakout rules.

The large number of configurable components creates substantial multiple-testing and overfitting risk. The stated default tuning for XAUUSD/indices also creates portability risk for crypto.

## Falsification plan

Use a point-in-time implementation with frozen parameters and untouched out-of-sample periods.

Required controls and ablations:

- Baseline A: generic range breakout using the same range geometry but no five-factor compression requirement.
- Baseline B: simple single-factor compression breakout, such as ATR-percentile or BB-width compression, with the same breakout rule.
- Ablate each consolidation component (ATR percentile, BB width, TTM squeeze, LR slope, ADX) one at a time and jointly compare the composite against simpler subsets.
- Hold the primary breakout geometry fixed and remove the confidence layer; then add volume, momentum and candle-quality terms separately to measure incremental contribution.
- Compare initial breakout entry versus retest-conditioned entry without changing the underlying range definition.
- Compare source-inspired ranges against equal-length/placebo ranges to test whether the consolidation state itself matters.
- Stress fees, spread and slippage, especially on 5-minute crypto data.
- Segment trending, ranging, high-volatility and low-volatility regimes and test stability across multiple liquid crypto instruments.

Any numerical pass/fail cutoff selected for future testing is a `research-defined falsification threshold`. The hypothesis is materially weakened if the composite fails to improve out-of-sample, after costs, over simpler compression/breakout controls, or if performance depends on a narrow parameter neighborhood.

## Crypto portability

`adapted`

The source explicitly mentions crypto as an instrument class requiring parameter changes, but its stated defaults are tuned for XAUUSD and major indices rather than demonstrated crypto evidence. Crypto trades 24/7, has venue fragmentation and different volume quality across spot/perpetual venues; perpetual implementations also introduce funding, mark/index-price and liquidation effects absent from the source logic.

Any crypto-specific session boundary, venue aggregation, funding treatment or parameter retuning is `research-proposed`.

## Limitations

- Not independently reproduced.
- Exact indicator formulas and many parameter defaults are `underspecified` in the reviewed public description.
- Source is an indicator, not a complete executable strategy.
- No source-reported controlled evidence that the five-factor composite beats simpler compression measures.
- Confidence scoring combines many correlated technical features and may overfit.
- Crypto effectiveness is `unproven`.
- Execution and transaction-cost model is a `data gap`.
- "Institutional" terminology is narrative framing, not verified order-flow evidence.

## Implementation status

Not implemented in the research stack. No Qlib full backtest, survivor validation, Paper, Testnet or Live verification has been performed.

## Adoption boundary

Research-only and not approved. Presence in this repository does not mean the record passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor, demonstrated profitability, or received implementation, Paper, Testnet or Live approval.

## Related Wiki records

No stable Hermes Wiki Brain record is asserted from this GitHub-only Scout run.

## Sources

- TradingView — AlphaX-Trade, **AlphaX Consolidation Engine Squeeze Detection Breakout Signals**, public open-source indicator, reviewed 2026-10-03: https://www.tradingview.com/script/D521qQHe-AlphaX-Consolidation-Engine-Squeeze-Detection-Breakout-Signals/
