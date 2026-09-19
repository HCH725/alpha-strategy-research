---
schema: strategy-research-record-v1
title: Open-Interest Spike/Drop Zones as Crypto Volatility-Event Signals
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-20
sources:
  - https://www.tradingview.com/script/hdU51jdP-open-interest-screener-fixed-zones/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Open-Interest Spike/Drop Zones as Crypto Volatility-Event Signals

## Provenance

Public TradingView open-source indicator **Open Interest Screener (Fixed Zones)**, author/page identity `artemka3091`, published 2025-07-28. Stable public URL: https://www.tradingview.com/script/hdU51jdP-open-interest-screener-fixed-zones/ . Source reviewed as of 2026-09-20.

The source describes scanning percentage changes in open interest across selected derivatives venues and marking unusually large OI increases or decreases as chart zones. The reviewed page names BitMEX USD, BitMEX USDT, and Kraken USD as supported sources and states that lookback and percentage threshold are configurable.

## Economic mechanism

### Source-reported

The author presents large OI increases as fresh positioning that may precede breakout setups, while large OI decreases may indicate liquidation events or position unwinds. The stated purpose is to detect unusual positioning changes that may precede volatility events.

### Research interpretation

The falsifiable hypothesis is narrower than a directional trading claim: an unusually large point-in-time change in derivatives open interest may identify a **conditional volatility regime** because rapid leverage creation or destruction represents an abrupt change in market participation and inventory risk.

Direction is deliberately left unresolved. An OI increase can accompany either long or short position creation, and an OI decrease can accompany either side closing. Therefore OI-change sign alone should first be tested as an event/volatility signal. Directional continuation or reversal should be treated as competing conditional hypotheses only after conditioning on contemporaneous price direction or another independently specified variable.

This mechanism is materially distinct from projected-liquidation-price research: the signal here is the observed OI shock itself, not an inferred future liquidation level.

## Signal

Source-supported components:

- Compute OI percentage change over a configurable **Bars to Look Back** window.
- **Spike Up:** OI increases by more than a configurable threshold percentage.
- **Spike Down:** OI decreases by more than a configurable threshold percentage.
- Mark the event with a dynamic chart zone; the source describes zone height as price high/low ±5% and a configurable minimum zone spacing.
- Source-recommended chart contexts are 15m, 1h, and 4h; these are author guidance, not independently validated optimal horizons.

The reviewed source does not establish a canonical trade entry, exit, holding period, position size, stop, or profit target. Those elements are **underspecified**.

Research-proposed operationalization for falsification only:

1. At each completed bar, compute the OI percentage change using only information available by that bar close.
2. Define an event when the absolute OI change exceeds a predeclared threshold or a rolling historical percentile estimated without future data.
3. Primary target: subsequent realized volatility over fixed forward horizons. This tests the source's volatility-event thesis without inventing direction.
4. Secondary competing directional tests: condition OI-up/OI-down events on contemporaneous price-return sign and compare continuation versus reversal outcomes.
5. Do not treat the source's ±5% visual zone geometry as predictive unless separately tested; it is primarily a visualization rule on the reviewed page.

Any threshold grid, percentile, forward horizon, entry, or execution rule introduced above is `research-proposed`, not source-reported.

## Required data

- Crypto derivatives instruments with reliable point-in-time open-interest history.
- Source-named venues: BitMEX USD, BitMEX USDT, Kraken USD where TradingView provides the required OI series.
- Timestamped OI and OHLCV at the tested bar frequency.
- Venue/symbol mapping and contract-unit metadata so OI changes are not accidentally mixed across incompatible definitions.
- Point-in-time availability timestamps for OI observations; no revised or later-filled values may be back-propagated.
- For multi-venue variants, explicit missing-venue handling and no silent survivorship substitution.

## Execution assumptions

The source is an indicator rather than a fully specified execution strategy. It does not specify signal-to-order timing, market versus limit orders, fill model, fees, spread, slippage, impact, funding treatment, leverage, margin, latency, partial fills, or failure handling.

For any later directional implementation, a leakage-safe baseline should form the signal only after the relevant bar and OI observation are available and execute no earlier than the next executable observation unless a defensible intrabar timestamp model exists. This is `research-proposed`.

## Evidence

### Source-reported

The source states that unusual OI changes are intended to highlight positioning changes that may precede volatility events and interprets large OI increases as possible fresh-positioning/breakout contexts and large decreases as possible liquidation/unwind contexts. No source-reported Sharpe, CAGR, drawdown, win rate, or independently audited backtest statistic was identified on the reviewed page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

OI direction is not trader-direction information: increasing OI does not by itself reveal whether newly opened risk is net bullish or bearish, and decreasing OI does not identify which side closed. The source also depends on exchange OI-feed availability and uses a fixed percentage-change threshold whose stability across assets, venues, and volatility regimes is unproven.

No independent negative-result study was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

1. **Primary event test:** compare forward realized volatility after OI-shock events with unconditional volatility and matched non-event bars from the same asset/time-of-day/regime.
2. **Simple baselines:** compare OI shock against price absolute-return shock, volume shock, and realized-volatility shock. Reject incremental-information claims if OI adds no out-of-sample value beyond these simpler observables.
3. **Directional competition:** after conditioning on contemporaneous price sign, test continuation and reversal symmetrically rather than assuming either outcome.
4. **Ablation:** OI-up and OI-down separately; single venue versus multi-venue confirmation; fixed percentage threshold versus leakage-safe rolling percentile.
5. **Placebo:** randomly shift event timestamps within matched volatility regimes. A valid signal should outperform timestamp-placebo distributions.
6. **Horizon robustness:** test the source-mentioned 15m, 1h, and 4h contexts plus fixed forward volatility horizons without selecting only the best ex post combination.
7. **Venue robustness:** require effects not to depend entirely on one venue or a known feed discontinuity.
8. **Point-in-time audit:** reject any result that relies on OI values unavailable at signal formation time or on retroactively filled observations.
9. **Out-of-sample requirement:** predeclare parameters on a training interval and evaluate untouched later periods. Material decay to baseline weakens or rejects the hypothesis.
10. **Costs for directional variants:** if converted into trades, require survival after realistic fees, spread, slippage, and perpetual funding.

Failure of the OI event to improve forward-volatility discrimination over price/volume/volatility baselines should reject the primary thesis rather than trigger additional indicator stacking.

## Crypto portability

direct

The source itself targets crypto derivatives with OI data. Portability nevertheless depends on venue-specific OI definitions, contract denomination, feed coverage, 24/7 candle boundaries, liquidity, and the possibility that exchange outages or symbol migrations create artificial OI jumps.

## Limitations

- Canonical entry/exit/holding/sizing logic: **underspecified**.
- Exact default lookback and threshold values were not relied upon here unless explicitly available from the reviewed page; parameter choice remains a research question.
- OI change does not identify long-versus-short initiation or closure.
- The source's chart zones are visualization constructs and are not evidence that those price bands themselves have predictive power.
- Multi-venue aggregation/confirmation rules are not fully specified by the reviewed source.
- Data quality and point-in-time OI availability are material risks.
- Not independently reproduced.

## Implementation status

No implementation or backtest in our research stack has been completed. This record only normalizes a public hypothesis for later falsification.

## Adoption boundary

Research material only. Presence in this repository does not imply profitability, validated alpha, implementation approval, paper-trading approval, testnet approval, or live-trading approval.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted from this GitHub-only Scout run.

## Sources

- TradingView — `artemka3091`, **Open Interest Screener (Fixed Zones)**, public open-source indicator, published 2025-07-28, reviewed 2026-09-20: https://www.tradingview.com/script/hdU51jdP-open-interest-screener-fixed-zones/
