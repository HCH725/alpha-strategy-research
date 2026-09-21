---
schema: strategy-research-record-v1
title: Bitcoin ETF Issuer-Normalized Flow Z-Score
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-22
sources:
  - https://www.tradingview.com/script/zyVhpYmQ/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin ETF Issuer-Normalized Flow Z-Score

## Provenance

Public TradingView open-source script **Bitcoin ETF Flows Z-Score | Astral Vision** by `AstralVision`. Stable source: https://www.tradingview.com/script/zyVhpYmQ/ . Source reviewed as of 2026-09-22.

Repository deduplication was performed against current `main` before capture by canonical TradingView source and normalized signal. No record for this canonical source was found. The repository already contains `bitcoin-us-spot-etf-net-flow-next-day-drift-2026-09-01.md`, which tests aggregate raw ETF net-flow drift. This record is materially distinct because its primary hypothesis is cross-issuer normalization: each ETF flow is standardized against that issuer's own history before aggregation, testing breadth/unusualness rather than raw-dollar flow magnitude.

## Economic mechanism

### Source-reported

The source argues that raw ETF flows are dominated by the largest products and that the more informative quantity may be how unusual each issuer's flow is relative to its own historical distribution. It standardizes each ETF's daily flow by its rolling mean and standard deviation, then aggregates issuer-level Z-scores. The source describes this as a way to detect broad institutional demand shifts without allowing the largest ETF to mechanically dominate the signal.

### Research interpretation

Falsifiable hypothesis: **issuer-normalized ETF-flow breadth contains incremental information about subsequent BTC returns or risk regime beyond aggregate raw ETF net flow and BTC price momentum.** A broad positive normalized shock may represent unusually strong creation demand across products; a broad negative shock may represent unusually strong redemption pressure. The competing explanation is that ETF flows are endogenous responses to prior BTC returns and that issuer normalization adds no predictive information.

## Signal

- Formation frequency: daily; evaluate only after all required ETF flow inputs for that session are point-in-time available.
- Per issuer: compute daily ETF flow, then rolling Z-score `(flow - rolling_mean) / rolling_std` over a configurable lookback.
- Aggregate: combine the issuer-level normalized readings into one aggregate Z-score signal; the source reports a 7-day smoothed aggregate oscillator.
- Extreme zones: configurable upper and lower thresholds are exposed by the source; exact threshold defaults are not reliably established from the reviewed public description and are therefore `underspecified`.
- The source also reports three configurable rolling-average windows in its table.
- Long/short entry, exit, holding period, sizing and re-entry rules are not specified as a complete executable strategy.
- `research-proposed`: test positive aggregate Z-score shocks as continuation and extreme positive/negative readings separately as potential exhaustion/reversal events. These competing directions must be pre-specified and evaluated independently rather than selected ex post.

## Required data

- Point-in-time daily flow data for the ten U.S. spot Bitcoin ETFs represented by the source, with issuer identity preserved.
- BTC spot price/returns for response variables and controls.
- ETF launch dates and point-in-time active-product universe; do not backfill products before inception.
- Exact publication/availability timestamp for each day's ETF input to prevent same-day look-ahead.
- TradingView/source flow construction should be independently audited before use because historical revisions or differing flow definitions can alter the signal.

## Execution assumptions

The source is an indicator, not a complete execution strategy. Order type, signal-to-fill delay, fees, spread, slippage, impact, capacity, leverage, funding, borrow/shorting, partial fills and failure handling are not specified.

For falsification, any directional implementation should use only information known at signal formation and execute no earlier than the next defensible tradable timestamp after flow availability (`research-proposed`).

## Evidence

### Source-reported

The source describes per-issuer rolling Z-score normalization, aggregation across ten U.S. spot Bitcoin ETFs, a 7-day smoothed aggregate oscillator, configurable extreme thresholds, and three rolling-average horizons. It provides no reviewed Sharpe, CAGR, maximum drawdown, hit rate, or independently audited predictive-performance statistic.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- U.S. spot Bitcoin ETFs only provide a short post-January-2024 history, limiting regime diversity and effective sample size.
- ETF flow can chase BTC returns, creating reverse-causality/endogeneity risk.
- Equalizing issuers by Z-score can overweight small products whose economically tiny flows are statistically unusual.
- Flow estimates and their timestamps may be revised or delayed.
- None of the reviewed source material establishes net-of-cost trading profitability.

## Falsification plan

1. Reconstruct all issuer flows point-in-time and freeze each product's inception date and availability timestamp.
2. Compare, without look-ahead: BTC-only momentum/volatility baseline; aggregate raw ETF net flow; largest-issuer-only flow; equal-weight issuer sign breadth; issuer-normalized aggregate Z-score; and issuer-normalized Z-score plus 7-day smoothing.
3. Run ablations for normalization, smoothing, issuer breadth, and leave-one-issuer-out stability. In particular, test whether the result survives removal of the dominant issuer and whether small-ETF Z-scores create false influence.
4. Control for lagged BTC returns and volatility to distinguish incremental flow information from return-chasing.
5. Test continuation and exhaustion/reversal hypotheses separately across fixed next-day and multi-day horizons (`research-proposed`).
6. Use walk-forward/OOS evaluation and threshold/lookback neighborhoods rather than optimizing one historical parameter set.
7. Apply timestamp-placebo tests: artificially advance flow availability; any material performance improvement is evidence of leakage.
8. Reject the normalized composite if it does not deliver stable OOS incremental information over the strongest simpler raw-flow or BTC-only baseline. Do not add filters to rescue a failed result.

## Crypto portability

direct

The source is explicitly Bitcoin/spot-ETF research. Portability risks include U.S. market hours versus BTC 24/7 trading, ETF holidays, delayed flow publication, issuer launches/closures, and differences between ETF creation/redemption activity and exchange spot/perpetual price discovery.

## Limitations

- `not independently reproduced`
- `underspecified`: exact default Z-score lookback and extreme thresholds are not preserved unless explicitly verified from the public source.
- Short structural history since U.S. spot BTC ETF launch.
- Flow measurement and publication-time definitions require point-in-time audit.
- The source does not specify a complete trading rule or execution model.

## Implementation status

Research record only. No implementation or Qlib full backtest has been completed by this Scout.

## Adoption boundary

This artifact is research-only. Its presence does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor/leaderboard entry, demonstrated profitable alpha, or received Paper/Testnet/Live approval.

## Related Wiki records

- `[[quant/bitcoin-us-spot-etf-net-flow-next-day-drift-2026-09-01]]` — related raw aggregate ETF-flow hypothesis; materially different normalization construction.

## Sources

1. AstralVision, **Bitcoin ETF Flows Z-Score | Astral Vision**, TradingView open-source script: https://www.tradingview.com/script/zyVhpYmQ/ (reviewed 2026-09-22).
