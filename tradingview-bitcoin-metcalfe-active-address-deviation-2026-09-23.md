---
schema: strategy-research-record-v1
title: TradingView Bitcoin Metcalfe Active-Address Valuation Deviation
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-23
sources:
  - https://www.tradingview.com/script/ytgjQixU/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Bitcoin Metcalfe Active-Address Valuation Deviation

## Provenance

Public TradingView open-source script `BTC - Metcalfes Law (Deviation)` by `Rob_Maths`, published 2025-12-19. Stable source: https://www.tradingview.com/script/ytgjQixU/ . Source reviewed as of 2026-09-23.

## Economic mechanism
### Source-reported

The author frames Bitcoin network value through Metcalfe-style network utility: market capitalization should be related to active users, proxied by active addresses. The script seeks periods when market capitalization is unusually high or low relative to network activity and interprets those deviations as overvaluation or undervaluation.

### Research interpretation

Falsifiable hypothesis: a point-in-time residual from a rolling log-log relationship between Bitcoin market capitalization and smoothed active addresses contains incremental information about subsequent BTC returns beyond price momentum, valuation ratios, and active-address growth alone. The proposed mechanism is adoption-linked valuation mean reversion: market value can temporarily detach from observable network usage, with sufficiently extreme residuals later correcting.

This is materially different from using active-address growth directly: the signal is the valuation residual conditional on network activity, not user-growth momentum.

## Signal

Source-reported construction:

- Intended timeframe: daily.
- Active addresses are smoothed with a 30-day SMA.
- Default regression window: 730 days; the source also mentions 1460 days as a longer alternative.
- Regression relationship: `ln(Market Cap) = alpha + beta * ln(Active Addresses)`.
- Default `Enforce Metcalfe` mode fixes `beta = 2.0`; an alternate dynamic-fit mode estimates beta from the historical window.
- Signal is the log deviation of observed market capitalization from modeled fair value.
- `0.0` represents modeled fair value.
- Source marks deviation `> 1.0` as an overvaluation zone and `< -0.25` as an undervaluation zone.
- Source describes the upper zone as a warning of potential major correction and the lower zone as a potential accumulation/buy condition.

The source does not specify a complete executable lifecycle for entry timing, exit, holding period, re-entry, stop, or position sizing. Those fields are underspecified and must not be inferred from the visual zones.

Research-proposed operationalization for testing only: evaluate forward returns after first confirmed daily closes entering each extreme zone; separately test zone entry, persistence, and exit/cross-back events over predeclared horizons. Compare fixed-beta and rolling-estimated-beta variants without choosing between them using full-sample results.

## Required data

- Bitcoin daily spot/reference price and circulating supply or a point-in-time market-cap series.
- Daily Bitcoin active-address count; the source defaults to `GLASSNODE:BTC_ACTIVEADDRESSES`.
- At least 730 prior daily observations after any data-availability lag for the default specification.
- Timestamp alignment between price/market cap and active-address observations.
- Point-in-time availability timestamps or a conservative lag for on-chain data; revised/backfilled values must not be treated as if known contemporaneously.

## Execution assumptions

The TradingView source is an indicator rather than a fully specified execution strategy. It does not define order type, signal-to-order timing, fill model, fees, spread, slippage, impact, leverage, margin, or position sizing.

Research-proposed testing should form the signal only after all daily inputs for the observation are available and execute no earlier than the next tradable bar after the assumed data-publication lag. Cost assumptions must be applied if the valuation state is converted into trades.

## Evidence
### Source-reported

The source states that historical positive-deviation peaks correspond to speculative bubbles/cycle tops and that negative-deviation `Utility Floors` have marked profitable accumulation zones. It does not provide a reproducible backtest, Sharpe ratio, CAGR, drawdown, hit rate, or formal statistical test on the TradingView page. These statements therefore remain source-reported qualitative claims.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself notes that markets can remain irrational longer than valuation metrics can predict and that the indicator depends on third-party on-chain data. Active addresses are an imperfect user proxy: exchange batching, address reuse, wallet behavior, spam, and changes in network usage can alter the address-to-user mapping. No independent negative-result study was established during this Scout capture; absence is not evidence of no negative result.

## Falsification plan

1. Reconstruct the metric point-in-time on daily BTC data with explicit active-address publication lag and no revised future values.
2. Freeze the default 30-day smoothing, 730-day window, beta=2, and source thresholds before the first test; do not optimize them on the full sample.
3. Test forward BTC excess/absolute returns after upper and lower extreme entries across predeclared horizons, with non-overlapping-event and overlapping-event versions reported separately.
4. Compare against controls: active-address growth alone, market-cap/active-address simple ratios, BTC momentum, drawdown, realized volatility, MVRV/MVRV-Z where point-in-time data exist, and a simple rolling price/market-cap z-score.
5. Ablate fixed `beta=2` versus rolling OLS beta. For dynamic beta, estimate alpha and beta strictly from the trailing window and verify that the current/future observation never enters estimation.
6. Stress the 730-day window with a small predeclared neighborhood including 1460 days, and stress the 30-day address smoothing without selecting the best setting retrospectively.
7. Use walk-forward and leave-one-cycle-out evaluation. A result concentrated in one Bitcoin cycle or dependent on the exact `1.0` / `-0.25` thresholds materially weakens the thesis.
8. Test whether residual magnitude adds OOS predictive information after active-address growth and standard valuation controls. If it does not, reject the Metcalfe-deviation layer rather than retaining extra complexity.
9. Run timestamp/data-vintage placebo tests. If performance disappears under realistic on-chain publication lag, treat the historical result as leakage/data-timing sensitive.
10. If converted into a trading rule, require net-of-fee/slippage results and parameter-neighborhood stability before any downstream consideration.

## Crypto portability

direct for Bitcoin only: the cited source explicitly constructs the metric on Bitcoin. Extension to other cryptoassets is unproven because address semantics, account models, chain usage, batching, and economic activity differ materially across networks.

## Limitations

- `underspecified`: no complete trading lifecycle is supplied by the source.
- `not independently reproduced`.
- Active addresses are a noisy proxy for distinct economic users.
- The source's fixed thresholds may be historically fitted; no independent threshold-validation evidence is supplied.
- A rolling OLS relationship can be nonstationary across adoption, fee-market, scaling, custody, and off-chain-activity regimes.
- The source requires third-party on-chain data, and historical revisions/availability can create look-ahead risk.
- Metcalfe's beta=2 is a modeling assumption, not established here as a Bitcoin structural constant.

## Implementation status

Research capture only. No implementation or Qlib full-backtest validation has been completed.

## Adoption boundary

Research-only. Presence in this repository does not mean the record passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No stable Hermes Wiki Brain links are asserted from this GitHub-only Scout run.

Repository-adjacent research includes active-address/user-adoption and fundamental-network-factor records, but this record's normalized signal is specifically the rolling time-series market-cap residual conditional on active addresses.

## Sources

- TradingView — Rob_Maths, `BTC - Metcalfes Law (Deviation)`, published 2025-12-19, reviewed 2026-09-23: https://www.tradingview.com/script/ytgjQixU/
