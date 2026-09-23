---
schema: strategy-research-record-v1
title: TradingView Pairwise Relative-Strength Matrix Rotation
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-04-27
sources:
  - https://www.tradingview.com/script/rw2AWQlR-Relative-Strength-Matrix/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Pairwise Relative-Strength Matrix Rotation

## Provenance

Public TradingView open-source indicator page, **Relative Strength Matrix**, author/page identity `kendis6969`, first published 2025-04-11 and updated through 2025-04-27. Stable source: https://www.tradingview.com/script/rw2AWQlR-Relative-Strength-Matrix/ . Source reviewed 2026-09-24.

The source describes a matrix that compares up to 10 selected assets using pairwise price ratios, applies the same strength criterion to every pair, and aggregates the pairwise outcomes into a ranked dominance score. The default criterion is momentum-based RSI. The source explicitly presents crypto baskets as a supported use case and frames the ranking as useful for identifying leaders, laggards, and rotation.

## Economic mechanism

### Source-reported

The author presents pairwise relative performance as a way to identify assets that are consistently stronger or weaker than the rest of a selected basket. Each asset is compared against every other asset rather than only against one benchmark, and the resulting dominance score is intended to expose leaders, laggards, and changes in market leadership.

### Research interpretation

The falsifiable hypothesis is that **broad pairwise momentum dominance contains incremental cross-sectional information about subsequent crypto returns beyond ordinary standalone momentum or performance versus BTC**. An asset that is strong against many peers simultaneously may represent broader demand leadership rather than a move driven only by the common crypto market factor.

A second interpretation is possible but must not be assumed: changes in dominance rank may capture rotation before absolute-price momentum baselines do. Both continuation and rank-reversal alternatives should therefore be tested rather than presuming that a high score must be bought.

The executable portfolio mapping below is not supplied by the source and is `research-proposed`.

## Signal

Source-supported construction:

- Universe: user-selected basket of up to 10 assets.
- For each asset pair, construct the price ratio.
- Apply a common strength criterion to each pairwise ratio.
- Default criterion: RSI-based momentum.
- Aggregate the pairwise comparisons into a total dominance score for each asset.
- Rank assets by dominance score.
- The source states that the criterion is customizable and can be replaced by other valuation logic.

Underspecified by the public description:

- exact default RSI lookback;
- exact pairwise win/loss or scoring threshold;
- tie handling;
- portfolio formation timestamp;
- long/short entry thresholds;
- holding/rebalance interval;
- exits and re-entry;
- position sizing;
- fees, spread, slippage, funding, and turnover controls.

`research-proposed` operationalization for falsification only:

1. Freeze a point-in-time liquid crypto universe before each formation timestamp.
2. Reconstruct the source's pairwise RSI/dominance calculation from the open-source logic before testing predictive performance.
3. At each formation time, rank assets by dominance score.
4. Test both continuation (long leaders / short laggards, or long leaders versus cash/BTC) and reversal mappings separately.
5. Evaluate multiple predeclared holding/rebalance horizons without selecting the best horizon in-sample.
6. Compare directly with standalone asset momentum and asset-versus-BTC relative momentum using the same universe, formation times, holding periods, and cost model.

The source is an indicator, not a fully specified trading strategy. The lifecycle is therefore **underspecified**.

## Required data

- Point-in-time crypto universe membership and liquidity eligibility.
- Synchronized price series for every asset in the basket.
- Consistent quote currency or an explicit normalization policy.
- Identical timestamp/candle boundaries across assets and venues.
- Sufficient history to calculate the reconstructed RSI criterion without warm-up leakage.
- If perpetual futures are tested: contract mapping, mark/index conventions, funding, and delisting history.
- Point-in-time availability is mandatory; current top-market-cap constituents must not be projected backward into historical tests.

## Execution assumptions

The source does not specify an executable order model.

For research, signals must be formed only after all component bars used by every pair are complete. Execution should occur no earlier than the next tradable observation unless an independently justified same-bar model is available. Fees, bid/ask spread, slippage, funding for perpetuals, turnover, liquidity, and short availability must be charged explicitly.

Because one asset participates in many pairwise ratios, missing or stale data can distort multiple matrix cells simultaneously. A deterministic missing-data policy must be fixed before testing rather than filled opportunistically.

## Evidence

### Source-reported

The TradingView page describes the matrix as a framework for relative-strength monitoring and rotation and states that it can be used on crypto baskets. It does not report a traceable Sharpe ratio, CAGR, drawdown, win rate, transaction-cost analysis, or out-of-sample predictive test for the dominance ranking.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-reported negative empirical study was identified on the reviewed TradingView page. Absence is not evidence of no negative result.

The public description itself leaves material strategy and parameter details unspecified, and it supplies no independent evidence that the pairwise matrix adds predictive information beyond simpler momentum rankings.

## Falsification plan

1. **Reconstruction gate:** independently reconstruct the exact pairwise score from the public open-source logic before any performance claim. If the source construction cannot be reproduced unambiguously, stop and classify the hypothesis as technically incomplete rather than tuning a substitute.
2. **Primary baseline:** compare against ordinary cross-sectional momentum using each asset's own trailing return/RSI.
3. **BTC-control baseline:** compare against each asset's relative performance versus BTC only. The matrix must add information beyond using BTC as a single common benchmark.
4. **Pairwise-ablation:** compare full all-pairs dominance with randomly reduced pair sets and simple average relative return. This tests whether the matrix topology itself adds information.
5. **Direction test:** test leader continuation and leader reversal separately. Reject a narrative that is supported only after choosing direction ex post.
6. **Universe robustness:** use point-in-time universes with liquidity and listing-age rules; test sensitivity to basket membership and leave-one-asset-out perturbations.
7. **Common-factor control:** neutralize or condition on BTC/market beta to determine whether the score is merely repackaged market exposure.
8. **Timing robustness:** test predeclared formation/holding horizons and shifted candle boundaries. Do not optimize a single lucky rebalance time.
9. **Cost sensitivity:** apply realistic fees, spread, slippage, funding, and turnover. Pairwise rank churn that disappears net of costs falsifies tradability even if a gross signal remains.
10. **OOS requirement:** parameter choices and universe rules must be frozen before final out-of-sample evaluation.

The hypothesis is materially weakened or rejected if the full pairwise dominance score fails to provide stable out-of-sample incremental information versus simpler standalone momentum and BTC-relative baselines, or if any gross advantage is consumed by realistic turnover and costs. Failure should lead to rejection of the pairwise layer, not additional indicator stacking.

## Crypto portability

**direct** for the research hypothesis: the source explicitly identifies crypto baskets as a use case.

Material crypto-specific risks remain:

- 24/7 candle-boundary choices can alter synchronized ratios and RSI values;
- venue fragmentation can make nominally identical symbols non-comparable;
- newly listed assets create unequal history and survivorship risk;
- stablecoin quote differences can contaminate relative ratios;
- perpetual-futures funding and contract changes can dominate small relative-strength edges;
- a fixed present-day basket would create severe look-ahead/survivorship bias.

## Limitations

- `underspecified`: exact default RSI length and pairwise scoring threshold are not stated in the public description reviewed here.
- `underspecified`: no complete entry/exit/holding/sizing lifecycle is supplied.
- `data gap`: no source-reported cost-aware or out-of-sample performance evidence was found on the reviewed page.
- `unproven`: incremental predictive value versus simpler momentum controls is unknown.
- `not independently reproduced`: neither the Pine calculation nor predictive performance was reproduced in this Scout cycle.
- Any portfolio mapping described above is `research-proposed`, not source-reported.

## Implementation status

No implementation in the research stack has been completed. No backtest was run in this Scout cycle.

## Adoption boundary

Research material only. Presence in this repository does not mean the record passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, demonstrated profitable or validated alpha, or received approval for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

No stable related Hermes Wiki Brain record is asserted here; GitHub-only Scout operation does not query or fabricate Wiki links.

## Sources

- TradingView, `kendis6969`, **Relative Strength Matrix**, public open-source script, published 2025-04-11, updated through 2025-04-27: https://www.tradingview.com/script/rw2AWQlR-Relative-Strength-Matrix/
