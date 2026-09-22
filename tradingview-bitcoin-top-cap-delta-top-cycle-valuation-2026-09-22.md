---
schema: strategy-research-record-v1
title: "Bitcoin Top Cap and Delta Top Cycle-Valuation Extremes"
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
  - https://www.tradingview.com/script/w2JdVwO4-Bitcoin-Cycle-Master-InvestorUnknown/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Top Cap and Delta Top Cycle-Valuation Extremes

## Provenance

- Public TradingView open-source script: `Bitcoin Cycle Master [InvestorUnknown]`.
- Author/page identity: `InvestorUnknown`.
- TradingView page publication date: 2024-09-29.
- Stable URL: https://www.tradingview.com/script/w2JdVwO4-Bitcoin-Cycle-Master-InvestorUnknown/
- Source reviewed as of 2026-09-22.

## Economic mechanism

### Source-reported

The source combines several long-horizon Bitcoin cycle metrics. For the hypothesis normalized here, the relevant components are **Top Cap** and **Delta Top**. The author describes Top Cap as 35 times an Average Cap derived from cumulative Bitcoin price divided by Bitcoin age in days, intended as an upper boundary for speculative cycle peaks. Delta Top is described as seven times the difference between Realized Cap and Average Cap and as a historically useful cycle-top signal. The author explicitly cautions that Top Cap's historical peak behavior may not remain relevant in future cycles.

The same source also displays Terminal Price, Realized Price, CVDD and Balanced Price. Those components are not silently folded into the present signal because the repository already contains neighboring realized-price, CVDD and balanced/terminal-price families and because their inclusion would change the core hypothesis.

### Research interpretation

The falsifiable hypothesis is that **two structurally different long-horizon valuation anchors—an age-normalized cumulative-price Top Cap and a realized-cap-minus-average-cap Delta Top—contain incremental point-in-time information about Bitcoin cycle-top risk beyond simpler price trend, drawdown, realized-cap valuation and time-since-halving controls**.

The potential mechanism is not that a fixed line mechanically causes reversal. Instead, prolonged price appreciation may move market value toward historically extreme valuation envelopes while realized-cap expansion captures the degree to which gains have migrated into holder cost basis. Agreement or disagreement between the two envelopes may therefore distinguish broad speculative overextension from a price-only extreme. This interpretation is a research hypothesis, not a source-verified causal result.

## Signal

Source-supported construction:

- `Top Cap = 35 × Average Cap`.
- The source describes `Average Cap` as cumulative Bitcoin price divided by Bitcoin age in days; the exact implementation details should be reconstructed from the public script before any backtest rather than inferred beyond the description.
- `Delta Top = 7 × (Realized Cap - Average Cap)`.
- The source uses these as long-horizon cycle-top valuation references.
- The source does not specify an executable entry, exit, holding period, re-entry, position-sizing or short-selling rule.

Research-proposed operationalization for later testing:

- reconstruct both anchors point-in-time;
- express spot price distance to each anchor as scale-free ratios or log distances;
- test each anchor independently before testing an agreement/confluence state;
- evaluate whether proximity/crossing predicts subsequent downside risk or lower forward returns at predeclared medium/long horizons.

Any proximity threshold, crossing rule, holding horizon, trade mapping or sizing rule is **research-proposed**.

## Required data

- Bitcoin spot/index price history with a documented continuous reference series.
- Bitcoin age in days and an unambiguous genesis/start convention matching the reconstructed source logic.
- Point-in-time Bitcoin Realized Cap for Delta Top.
- Timestamp and publication/availability metadata for the on-chain series.
- Sufficient historical coverage to evaluate multiple Bitcoin cycles without using future data to initialize cumulative quantities.
- Optional controls for realized volatility, drawdown, MVRV/MVRV-Z, halving age and realized-price distance.

## Execution assumptions

The source is an indicator, not a complete trading strategy. Signal-to-order timing, market/limit execution, fees, spread, slippage, impact, leverage, funding, shorting, sizing and holding period are unspecified.

Any later implementation is research-proposed. A causal test must use only inputs available at the decision timestamp and should execute no earlier than the next eligible bar. If expressed through perpetual futures, funding and venue basis must be modeled separately.

## Evidence

### Source-reported

The source states that Top Cap historically provided reliable cycle-peak signals but explicitly warns that it may not remain relevant in the future. It describes Delta Top as historically reliable for Bitcoin market-cycle tops. The page provides no traceable Sharpe, CAGR, drawdown, hit rate, p-value or other strategy-performance statistic, so none is recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself supplies material negative evidence by warning that Top Cap's historical peak behavior may not remain relevant. The constants `35` and `7` are fixed multipliers whose stability across future market-cap, liquidity and market-structure regimes is unverified. Cumulative-price and realized-cap constructions are also strongly nonstationary, and visually fitting a small number of Bitcoin cycles creates substantial multiple-testing and hindsight risk.

## Falsification plan

1. Reconstruct Top Cap and Delta Top from point-in-time inputs and verify exact agreement with the public TradingView construction before evaluating alpha. If reconstruction cannot be made unambiguous, stop rather than substitute a lookalike formula.
2. Test Top Cap and Delta Top separately. A confluence rule is allowed only if each component or their interaction adds stable OOS information.
3. Compare against simple baselines: long-horizon momentum/trend, drawdown, realized volatility, log-price age trend, time-since-halving and realized-price distance.
4. Compare against neighboring on-chain valuation controls, especially MVRV/MVRV-Z, NUPL, realized-price bands, Balanced Price, Terminal Price and CVDD. This formulation must add information rather than inherit apparent success from the same cycle episodes.
5. Stress-test the source multipliers around `35` and `7`. If results depend narrowly on the exact constants, treat that as parameter instability rather than evidence of a structural law.
6. Use walk-forward or expanding-window evaluation by cycle. Parameters or thresholds chosen using a later cycle must not be back-projected into earlier decisions.
7. Run timestamp-shift and data-vintage tests on Realized Cap. Any benefit that disappears under realistic publication lag is rejected as leakage.
8. Evaluate both continuous distance-to-anchor and discrete touch/cross events. If discretization adds no OOS value, reject the threshold/event layer.
9. Test whether the signal predicts future returns, maximum adverse excursion, drawdown probability or volatility separately; do not relabel a risk-state indicator as directional alpha without evidence.
10. Research-defined failure criterion: if neither anchor nor their interaction provides stable leakage-safe incremental OOS information over the strongest simpler baseline across held-out cycles, reject this formulation rather than adding filters.

## Crypto portability

**direct** for Bitcoin because the source is explicitly Bitcoin-specific and uses Bitcoin age and Realized Cap.

Portability to other cryptoassets is **unproven**. Different genesis histories, supply schedules, realized-cap semantics, liquidity structures and cycle lengths make direct reuse of the constants or construction unjustified.

## Limitations

- Not independently reproduced.
- No complete trading lifecycle is source-specified.
- Exact Average Cap implementation must be verified from the public script before testing.
- Fixed multipliers `35` and `7` may be historically fitted and nonstationary.
- Only a small number of independent Bitcoin macro cycles exist, creating severe sample-size and overfitting risk.
- Realized Cap requires strict point-in-time availability handling.
- Any threshold, holding horizon, trade mapping or sizing rule beyond the source description is research-proposed.

## Implementation status

Research record only. No implementation or Qlib full-backtest validation has been completed as part of this Scout cycle.

## Adoption boundary

This record is research-only. Its presence does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor/leaderboard entry, demonstrated profitable alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

- `[[bitcoin-onchain-balanced-and-terminal-price-valuation-bands-2026-09-01]]` — neighboring cycle-valuation family using Balanced and Terminal Price.
- `[[bitcoin-onchain-cumulative-value-days-destroyed-cvdd-floor-2026-09-01]]` — neighboring coin-days-destroyed valuation family.
- `[[bitcoin-onchain-mvrv-zscore-cycle-reversal-2026-08-31]]` — realized-cap valuation extreme family.
- `[[bitcoin-onchain-net-unrealized-profit-loss-nupl-macro-cycle-2026-09-01]]` — aggregate unrealized-profit/loss cycle family.
- `[[tradingview-bitcoin-realized-price-cost-basis-bands-2026-09-21]]` — TradingView realized-price proportional-band family.

## Sources

- TradingView — `Bitcoin Cycle Master [InvestorUnknown]`, author `InvestorUnknown`, public open-source script, published 2024-09-29, reviewed 2026-09-22: https://www.tradingview.com/script/w2JdVwO4-Bitcoin-Cycle-Master-InvestorUnknown/
