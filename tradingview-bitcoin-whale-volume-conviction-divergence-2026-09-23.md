---
schema: strategy-research-record-v1
title: TradingView Bitcoin Whale-Volume Conviction Divergence
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
  - https://www.tradingview.com/script/NB9Gzlb3/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Bitcoin Whale-Volume Conviction Divergence

## Provenance

Public TradingView open-source script `Whale Accumulation Index | Astral Vision` by `AstralVision`, published 2026-05-21. Stable source: https://www.tradingview.com/script/NB9Gzlb3/ . Source reviewed as of 2026-09-23.

## Economic mechanism
### Source-reported

The source separates Bitcoin on-chain transaction volume into large-transaction volume and total transaction volume using CoinMetrics data. It interprets the ratio of large volume to total volume as the share of network flow attributable to whale-scale transactions. Its `Conviction` mode compares momentum in that whale-volume share with price momentum: whale activity accelerating faster than price is described as accumulation/leading participation, while price accelerating faster than whale activity is described as distribution or weak large-holder participation.

### Research interpretation

Falsifiable hypothesis: the relative acceleration of large-transaction share versus BTC price contains incremental information about subsequent BTC returns beyond price momentum, total on-chain volume, and the whale-share level alone. The proposed behavioral mechanism is lead-lag in participant composition: unusually strong growth in large-transfer share before equivalent price acceleration may identify informed or high-conviction positioning, while price strength unsupported by comparable large-transfer-share acceleration may be less persistent.

This interpretation does not assume that every large on-chain transfer is a directional buy or sell. The signal is a statistical divergence in activity composition, not direct proof of whale accumulation or distribution.

## Signal

Source-reported construction:

- Base data frequency: daily.
- Base ratio: large Bitcoin on-chain transaction volume in USD divided by total Bitcoin on-chain transaction volume in USD, using CoinMetrics feeds.
- The ratio is smoothed by a configurable SMA before subsequent calculations.
- `Z-Score` mode standardizes the smoothed ratio against its rolling mean and standard deviation over a configurable lookback: `Z = (ratio - mean(ratio, N)) / stdev(ratio, N)`.
- `Conviction` mode computes proportional rate of change for price and whale ratio over a configurable lookback: `(current - past) / abs(past)`.
- Price ROC and whale-ratio ROC are independently Z-score normalized.
- Conviction signal: `whale ROC Z-score - price ROC Z-score`.
- Positive Conviction means whale activity is accelerating faster than price; negative Conviction means price is accelerating faster than whale activity.
- The source exposes configurable upper/lower extreme thresholds, Z-score window, smoothing period, and Conviction ROC length.

The reviewed TradingView page does not state fixed default numeric values for the large-transaction size cutoff, smoothing period, normalization window, Conviction ROC length, or extreme thresholds. It also does not specify a complete executable lifecycle for entry, exit, holding period, re-entry, stop, or position sizing. These fields are underspecified and must not be inferred.

Research-proposed operationalization for testing only: evaluate subsequent BTC returns conditional on predeclared Conviction quantiles or standardized extremes, separately for positive and negative divergences. Test signal level, first threshold crossing, and persistence as separate hypotheses rather than selecting the best event definition retrospectively.

## Required data

- Bitcoin daily reference/spot price with stable UTC candle boundaries.
- Daily CoinMetrics-compatible Bitcoin total on-chain transaction volume in USD.
- Daily CoinMetrics-compatible large-transaction volume in USD using the same definition and threshold as the source feed.
- Point-in-time availability timestamps for both on-chain series, or a conservative publication lag.
- Sufficient trailing observations for the chosen smoothing, ROC, and Z-score windows.
- Missing-data and source-revision handling that prevents revised/backfilled on-chain observations from being treated as contemporaneously known.

A material data gap remains until the exact CoinMetrics large-transaction series identity and its size-threshold definition are verified for implementation. The source description establishes the concept but the reviewed page text does not expose the exact threshold value.

## Execution assumptions

The TradingView source is an analytical indicator, not a fully specified trading strategy. It does not define signal-to-order timing, order type, fill model, fees, spread, slippage, impact, leverage, margin, funding, shorting mechanics, or position sizing.

Research-proposed testing should form the daily signal only after both price and on-chain inputs for that date would have been available and execute no earlier than the next tradable bar after the assumed data-publication lag. If mapped to perpetuals, funding and realistic trading costs must be included separately from the alpha signal.

## Evidence
### Source-reported

The source states that positive Conviction readings have historically been associated with accumulation ahead of price moves and that negative readings have been associated with distribution or weak institutional participation. It does not provide a reproducible backtest, Sharpe ratio, CAGR, drawdown, hit rate, or formal statistical test on the reviewed TradingView page. These remain qualitative source-reported claims.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself states that past performance is not indicative of future results. More importantly, large on-chain transfers are not synonymous with purchases or sales: exchange reshuffling, custody migration, internal transfers, UTXO consolidation, OTC settlement, and other non-directional activity can change large-transaction share. No independent negative-result study was established during this Scout capture; absence is not evidence of no negative result.

## Falsification plan

1. First resolve the exact point-in-time CoinMetrics series and large-transaction threshold used by the source. If the source-compatible series cannot be reconstructed without guessing, stop rather than substitute a materially different whale definition.
2. Reconstruct daily whale-share ratio, smoothing, ROC, and Z-score calculations with explicit data-publication lag and no future revisions.
3. Freeze a small, predeclared parameter set for smoothing, ROC, and normalization windows; any Scout/research-chosen values are `research-proposed`, not source defaults.
4. Test the Conviction signal against controls: BTC price ROC/momentum alone, raw whale-share level, whale-share ROC alone, total on-chain volume growth, realized volatility, and drawdown.
5. Ablate the composite explicitly: `whale ROC Z`, `price ROC Z`, and `whale ROC Z - price ROC Z`. If the difference term does not add OOS information beyond its components, reject the Conviction layer.
6. Use walk-forward and regime-separated evaluation across bull, bear, high-volatility, low-volatility, and major exchange/custody migration periods.
7. Run event filters or sensitivity checks for known large exchange/custodian wallet reorganizations where identifiable; test whether apparent alpha is dominated by operational transfers rather than directional positioning.
8. Test realistic availability lags and timestamp placebos. If predictive performance disappears after conservative on-chain publication timing, classify the result as timing/leakage sensitive.
9. Use predeclared forward-return horizons and report overlapping and non-overlapping event samples separately. Any acceptance/failure cutoff selected by research is a `research-defined falsification threshold`.
10. If converted into a tradable rule, require net-of-fee/slippage/funding results and parameter-neighborhood stability before downstream consideration.

## Crypto portability

direct for Bitcoin only: the cited source explicitly uses Bitcoin on-chain transaction data. Extension to other chains is unproven because transaction-size distributions, account/UTXO models, exchange/custody behavior, stablecoin activity, and the economic meaning of a large transfer differ materially.

## Limitations

- `underspecified`: no complete trading lifecycle is supplied by the source.
- `not independently reproduced`.
- `data gap`: exact source-compatible large-transaction series identity and size threshold are not stated in the reviewed page text.
- Large transfers are not equivalent to directional whale buying or selling.
- On-chain USD volume can be affected by self-transfers, exchange/custody operations, batching, UTXO consolidation, and changes in market price.
- Configurable thresholds and lookbacks create overfitting risk if selected on the full sample.
- Third-party on-chain series may be revised or have publication latency, creating look-ahead risk if historical final values are used naively.

## Implementation status

Research capture only. No implementation or Qlib full-backtest validation has been completed.

## Adoption boundary

Research-only. Presence in this repository does not mean the record passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No stable Hermes Wiki Brain links are asserted from this GitHub-only Scout run.

Repository-adjacent research includes a Whale Alert transfer-event leader/follower record, but that is event-based transfer classification. The present record instead studies the daily proportion of large on-chain transaction volume and its normalized momentum divergence versus price.

## Sources

- TradingView — AstralVision, `Whale Accumulation Index | Astral Vision`, published 2026-05-21, reviewed 2026-09-23: https://www.tradingview.com/script/NB9Gzlb3/
