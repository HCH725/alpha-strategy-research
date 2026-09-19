---
schema: strategy-research-record-v1
title: CVD-OI Anomaly Participation-State Alpha
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
  - https://www.tradingview.com/script/dNpNQvgs/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# CVD-OI Anomaly Participation-State Alpha

## Provenance

- Public TradingView open-source script: **CVD & Open Interest Dashboard** by Kina_jp.
- TradingView page shows publication date as Jul 20; year is not exposed unambiguously in the reviewed page, so it is not invented here.
- Stable URL: https://www.tradingview.com/script/dNpNQvgs/
- Reviewed as of 2026-09-20.

## Economic mechanism

### Source-reported

The source combines cumulative volume delta (CVD) with net open-interest change. It flags abnormal OI surges using a configurable anomaly multiplier and cross-references them with CVD. It also classifies price/OI states as long build-up (price up/OI up), short cover (price up/OI down), short build-up (price down/OI up), and long liquidation (price down/OI down). A rolling bull/bear gauge aggregates significant aggressive-volume actions.

### Research interpretation

The falsifiable hypothesis is that an OI anomaly contains more short-horizon directional or volatility information when conditioned on contemporaneous aggressive-flow direction than either OI change or CVD alone. The mechanism is participation quality: OI measures expansion/contraction of outstanding derivatives exposure while CVD proxies aggressive flow. Their interaction may distinguish leverage-backed moves from position-closing moves, but it does not uniquely identify trader intent.

## Signal

Source-supported components:

- CVD can use lower-timeframe data; the source describes a 10-second high-precision mode and a chart-timeframe normal mode.
- Track net OI change and flag abnormal OI surges with a user-configurable anomaly multiplier.
- Cross-reference OI anomalies with CVD direction.
- Classify price/OI direction into four participation states.
- The default OI ticker shown by the source is Binance BTC perpetual OI, with user-selectable alternatives such as Bybit or OKX.

Canonical anomaly threshold, CVD decision threshold, smoothing parameters, entry, exit, holding period, re-entry and sizing are **underspecified**.

Research-proposed operationalization: form signals only from completed, point-in-time bars; freeze an OI-anomaly flag from a trailing-only normalization; condition it on same-bar or pre-specified lagged CVD sign; then measure fixed-horizon forward return and absolute return. Test the four price/OI states separately. All numerical windows, thresholds and horizons introduced later are `research-proposed`.

## Required data

- Crypto perpetual/futures OHLCV.
- Point-in-time OI series for the selected venue and contract.
- Volume-delta/CVD data; if reconstructed from lower-timeframe bars, retain the exact lower timeframe and aggregation rule.
- Timestamp-aligned price, OI and CVD without forward filling unavailable OI across gaps.
- Venue and contract identity, including linear/inverse specification and OI units.

## Execution assumptions

The source is an indicator, not a fully specified trading strategy. Signal-to-order timing, market/limit choice, fills, fees, spread, slippage, impact, funding, leverage, margin, latency and partial fills are underspecified. Any trading test should execute no earlier than the first feasible price after the causal signal is observable.

## Evidence

### Source-reported

The source describes CVD/OI combinations as a way to distinguish participation and liquidation-related market states and presents qualitative interpretations of abnormal OI spikes. No source-verified Sharpe, CAGR, drawdown, win rate or other performance statistic is used in this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source's directional labels are interpretive rather than uniquely identified from OI and CVD: OI does not reveal whether new exposure is net long or short, and CVD does not reveal the inventory motive of counterparties. The source also describes a green OI spike as potentially aggressive long initiation **or short liquidation**, although liquidation/position closure would ordinarily tend to reduce rather than increase aggregate OI; this ambiguity is a reason to test the state variables rather than accept the label semantics. No independent predictive evidence was established during this Scout cycle.

## Falsification plan

1. Compare `OI anomaly + CVD` against OI-anomaly-only, CVD-only, price momentum/reversal and realized-volatility baselines.
2. Test interaction incrementality out of sample; reject the composite claim if the interaction adds no stable information.
3. Separate directional-return prediction from volatility prediction so a volatility event is not mislabeled directional alpha.
4. Test the four price/OI states independently and against matched price-return controls.
5. Compare lower-timeframe CVD construction with chart-timeframe approximation; reject effects that exist only under one fragile reconstruction.
6. Run single-venue tests for Binance, Bybit and OKX where point-in-time data exist; do not infer multi-venue robustness from one venue.
7. Use regime-matched timestamp placebos and shuffled CVD signs to test whether apparent interaction value exceeds event-selection effects.
8. Require walk-forward/OOS validation and realistic fees, spread, slippage and funding. Reject or materially weaken the trading hypothesis if the effect disappears OOS or after costs.

## Crypto portability

direct

The source is explicitly designed for crypto derivatives. Risks include venue fragmentation, differing OI units, contract specifications, 24/7 candle boundaries, lower-timeframe data availability and funding effects.

## Limitations

- Not independently reproduced.
- Canonical trading rule and numerical thresholds are underspecified.
- OI and CVD do not uniquely identify trader intent or counterparty inventory.
- Lower-timeframe CVD availability may differ historically and by account/data tier.
- Venue-specific OI histories can contain gaps and contract-definition changes.
- The source's liquidation/initiation labels should be treated as hypotheses, not ground truth.

## Implementation status

Research-only normalization. No implementation or backtest in the research stack has been completed.

## Adoption boundary

This record is research material only. It is not evidence of profitable alpha and is not approved for implementation, paper trading, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain record is cited in this GitHub-only Scout cycle.

## Sources

- TradingView — Kina_jp, **CVD & Open Interest Dashboard**, public open-source script, reviewed 2026-09-20: https://www.tradingview.com/script/dNpNQvgs/
