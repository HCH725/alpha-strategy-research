---
schema: strategy-research-record-v1
title: TradingView RSI-Filtered Jaws VWAP Mean Reversion
created: 2026-09-26
updated: 2026-09-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2026-09-26
sources:
  - https://www.tradingview.com/script/WeAMGj9j/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView RSI-Filtered Jaws VWAP Mean Reversion

## Provenance

Public TradingView open-source strategy page: **HYE Mean Reversion VWAP [Strategy]**, author **HYE0619**. Published 2021-07-01 and updated 2021-07-27. Stable source: https://www.tradingview.com/script/WeAMGj9j/ . Reviewed 2026-09-26.

The source says this is an RSI-filtered version of PJ Sutherland's Jaws Mean Reversion algorithm, substituting period-based VWAP for SMA, and credits @neolao's "VWAP with period" indicator.

## Economic mechanism
### Source-reported

The source presents a mean-reversion rule in which a short-horizon 2-period VWAP becomes at least 3% displaced from a 5-period VWAP while a smoothed short RSI is extreme. It exits when the fast VWAP crosses back through the slow VWAP.

### Research interpretation

The falsifiable hypothesis is that a large short-versus-slower volume-weighted price displacement, conditioned on short-horizon momentum exhaustion, contains subsequent mean-reversion information. VWAP displacement is the location/extension component; smoothed RSI is the exhaustion confirmation. The hypothesis is distinct from the author's SMA version because volume weighting changes the signal's data dependency and potentially the timing and identity of extremes.

Neither component should be assumed to add alpha without ablation.

## Signal

Source-reported normalized rules:

- Signal evaluation: on the close.
- Fast price measure: 2-period VWAP.
- Slow price measure: 5-period VWAP.
- RSI component: 2-period RSI smoothed with a 5-period exponential average.
- Long entry: fast VWAP closes at least 3% below slow VWAP and the smoothed RSI is below 30.
- Long exit: fast VWAP closes above slow VWAP.
- Short entry: fast VWAP closes at least 3% above slow VWAP and the smoothed RSI is above 70.
- Short exit: fast VWAP closes below slow VWAP.
- Direction is configurable as Long Only, Short Only, or Both; source default is Long Only.
- The displacement percentage, VWAP periods, and RSI levels are configurable.

The reviewed public description does not specify pyramiding/re-entry behavior, exact order-fill timing after the close signal, or whether the period-based VWAP implementation has any reset/session convention beyond its stated periods. Those details are **underspecified** and must not be inferred.

## Required data

- OHLCV sufficient to calculate the source's period-based VWAP and RSI.
- Bar timeframe: **underspecified** by the reviewed source.
- Instrument/universe and venue: **underspecified**.
- Timestamp/timezone and session handling: **underspecified**.
- Point-in-time requirement: calculations must use only information available through the signal close.

No funding, order-book, open-interest, options, or aggressor-side trade data are specified by the source.

## Execution assumptions

The source states that entry and exit conditions occur "on the close," but the actual executable fill convention is not described. Same-close versus next-bar execution is therefore **underspecified**.

Order type, fees, spread, slippage, market impact/capacity, leverage/margin, short availability/borrow, partial fills, latency, and position sizing are not specified. Any later operational choices for these fields must be labeled `research-proposed`.

## Evidence
### Source-reported

The reviewed TradingView description provides the rule and adjustable parameters but no source-traceable performance statistic used in this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independently verified negative result was identified in the reviewed source. Material concerns are parameter flexibility, unspecified market/timeframe, and the possibility that the 3% displacement is highly scale- and volatility-dependent. Absence of reported negative evidence is not evidence of robustness.

## Falsification plan

1. Reconstruct the source rule point-in-time and compare it with a simple fast/slow VWAP-cross baseline.
2. Ablate the RSI filter while holding VWAP displacement constant; separately test RSI extremes without the VWAP displacement.
3. Compare the VWAP construction against the author's adjacent SMA formulation using identical markets, horizons, costs, and validation splits. Reject a claimed VWAP-specific contribution if it does not improve held-out behavior.
4. Test the source defaults and a small predeclared neighborhood of displacement/VWAP/RSI parameters; treat a narrow optimum as evidence against robustness.
5. Evaluate trend, range, high-volatility, and low-volatility regimes with chronological out-of-sample or walk-forward validation.
6. Apply realistic fee, spread, and slippage sensitivity and reject the trading hypothesis if any gross edge is not robust to plausible costs.
7. Because the source does not identify a market or timeframe, require multi-asset and multi-horizon evidence rather than selecting the best ex post combination.

Any acceptance cutoff introduced during later testing is a **research-defined falsification threshold**, not source-reported.

## Crypto portability

**unproven**

The reviewed source does not demonstrate the rule specifically in crypto. The OHLCV-based construction is technically portable, but crypto testing must account for 24/7 candle boundaries, spot versus perpetual volume, venue fragmentation, funding and mark/index-price differences where relevant. A crypto implementation would be a ported hypothesis, not source-provided crypto evidence.

## Limitations

- Not independently reproduced.
- Source market, instrument, timeframe, costs, and fill model are underspecified.
- The source permits substantial parameter adjustment, creating data-mining risk.
- The 3% displacement threshold is not volatility-normalized.
- Exact implementation semantics of the credited period-based VWAP should be verified before reproduction rather than silently inferred.
- No source-reported performance figures are relied upon here.

## Implementation status

Research-only external material. No implementation in the research stack and no Qlib full-backtest validation has been completed.

## Adoption boundary

Presence in this repository does not mean this record passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor/leaderboard entry, demonstrated profitable or validated alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No stable Hermes Wiki Brain record was resolved in this GitHub-only Scout run; no Wiki link is fabricated.

## Sources

- TradingView — **HYE Mean Reversion VWAP [Strategy]**, HYE0619: https://www.tradingview.com/script/WeAMGj9j/ (published 2021-07-01; updated 2021-07-27; public open-source strategy page; reviewed 2026-09-26).
