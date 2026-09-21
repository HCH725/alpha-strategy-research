---
schema: strategy-research-record-v1
title: "Bitcoin Adaptive MVRV + Weekly RSI Weighted DCA"
created: 2026-09-21
updated: 2026-09-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-21
sources:
  - https://www.tradingview.com/script/oVuTxgUS-Adaptive-MVRV-RSI-Strategy-V6-Dynamic-Thresholds/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Adaptive MVRV + Weekly RSI Weighted DCA

## Provenance

- Public TradingView open-source strategy: `Adaptive MVRV & RSI Strategy V6 (Dynamic Thresholds)`.
- Author/page identity: `wjstienstra`.
- Publication date shown by TradingView: 2025-08-17.
- Stable source URL: https://www.tradingview.com/script/oVuTxgUS-Adaptive-MVRV-RSI-Strategy-V6-Dynamic-Thresholds/
- Source reviewed as of 2026-09-21.
- The source is Bitcoin-specific and explicitly describes a DCA strategy combining MVRV and weekly RSI with adaptive thresholds and conviction-weighted scaling.

## Economic mechanism

### Source-reported

The author describes MVRV as a long-cycle valuation signal and weekly RSI as a momentum/overbought-oversold signal. Rather than fixed cutoffs, buy and sell zones are derived from each indicator's long-term two-year moving average and standard deviation. The stated motivation is adaptation to Bitcoin's changing volatility and market structure. Trade size increases as the combined indicators move further into undervalued or overvalued zones.

### Research interpretation

This is a hybrid valuation-plus-momentum allocation hypothesis rather than a simple MVRV threshold rule:

- **Valuation component:** MVRV measures price relative to aggregate realized cost basis.
- **Momentum/cycle component:** weekly RSI measures whether long-horizon price momentum is unusually weak or strong.
- **Regime adaptation:** rolling two-year location/dispersion attempts to normalize secular changes in indicator distributions instead of assuming invariant absolute thresholds.
- **Allocation component:** signal extremity maps to gradual scaling rather than binary all-in/all-out timing.

The falsifiable proposition is that adaptive normalization plus the second RSI dimension improves leakage-safe out-of-sample allocation quality over simpler MVRV-only, RSI-only, fixed-threshold, and passive DCA baselines. The mechanism could fail if the adaptive bands merely overfit past Bitcoin cycles or if MVRV and RSI contain mostly redundant information.

## Signal

Source-supported logic:

- Instrument: Bitcoin.
- MVRV ratio supplies the on-chain valuation dimension.
- Weekly RSI supplies the momentum dimension.
- Each indicator's dynamic buy/sell zones use a long-term two-year moving average and standard deviation rather than fixed thresholds.
- Purchases scale upward as MVRV and RSI move deeper into their undervalued zones.
- Sales scale upward as the indicators move deeper into overvalued territory.

The public description does not expose enough detail to claim exact weighting coefficients, exact standard-deviation multipliers, cash-step schedule, rebalance cadence, conflict resolution when MVRV and RSI disagree, or complete execution rules. Those details are therefore **underspecified** here and are not invented.

Research-proposed operationalization for later testing, not source-reported: evaluate each component as a strictly point-in-time rolling standardized score, combine only after component-level ablation, and map score quantiles to monotonic DCA weights. Any such mapping must be frozen before holdout evaluation.

## Required data

- Bitcoin spot/index price history with daily data sufficient to construct weekly RSI without look-ahead.
- Point-in-time Bitcoin MVRV or the inputs required to reconstruct it, including realized capitalization/cost-basis data.
- At least two years of prior observations before an adaptive threshold becomes eligible.
- Timestamped source availability for on-chain observations; publication/revision latency must be respected.
- Portfolio cash and position state for weighted DCA simulation.

## Execution assumptions

The source describes scaling in and out but the reviewed public description does not fully specify order type, signal-to-order delay, fees, spread, slippage, custody, tax effects, minimum trade size, or exact rebalance cadence.

For research, same-bar fills should not be assumed. A conservative implementation should form signals only from data known at the decision timestamp and execute no earlier than the next eligible bar. Fees, spread/slippage and finite cash must be modeled. These are **research-proposed** assumptions, not source claims.

## Evidence

### Source-reported

The TradingView page presents the strategy rationale and component design but the reviewed public description does not provide a traceable Sharpe, CAGR, drawdown, win rate, or other performance statistic suitable for preservation here. No performance precision is inferred from the chart or strategy-report UI.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independently verified negative result was identified in the reviewed source. Important prior risks are parameter/data-mining across a small number of Bitcoin macro cycles, correlation between MVRV and price-derived RSI, revision/availability bias in on-chain data, and the possibility that passive DCA captures most of the apparent benefit.

## Falsification plan

1. Reconstruct MVRV and weekly RSI strictly point-in-time, including realistic on-chain publication latency; reject any implementation that uses revised/future data.
2. Freeze the adaptive rule using only training history, then use walk-forward or expanding-window evaluation with untouched later regimes.
3. Compare against passive periodic DCA, buy-and-hold, MVRV-only adaptive allocation, RSI-only adaptive allocation, and fixed-threshold variants.
4. Ablate in order: MVRV only -> + weekly RSI -> + adaptive two-year normalization -> + conviction-weighted sizing. Retain a layer only if it adds robust out-of-sample value.
5. Sweep reasonable neighborhoods around the two-year normalization horizon. A result that depends narrowly on the stated horizon is weak evidence.
6. Test the competing hypothesis that MVRV and weekly RSI are redundant by measuring incremental predictive/allocation value after conditioning on each component separately.
7. Evaluate multiple Bitcoin regimes, including deep bear markets, rapid recoveries, low-volatility consolidations and post-ETF market structure. Do not infer robustness from a handful of cycle turning points.
8. Include realistic fees/slippage and finite-cash constraints. Compare turnover and maximum drawdown as well as return/risk metrics.
9. Failure criterion: if adaptive MVRV+RSI does not materially and consistently improve leakage-safe OOS risk-adjusted allocation versus the strongest simpler baseline, reject the extra layers rather than adding more filters.

## Crypto portability

**direct** for Bitcoin because the source itself is explicitly a Bitcoin strategy and MVRV is Bitcoin on-chain data.

Portability to other crypto assets is **unproven**. Realized-value methodology, chain structure, market age, liquidity, token issuance and holder behavior differ materially across assets.

## Limitations

- Not independently reproduced.
- Exact source implementation parameters beyond the public description are underspecified here.
- MVRV point-in-time availability/revision handling is a material data-risk area.
- Two-year adaptive normalization may still be a fitted design choice rather than a structural horizon.
- Bitcoin has few independent macro cycles, so conventional backtest sample size can overstate confidence.
- Weighted DCA requires path-dependent cash/position accounting; comparisons must use identical capital constraints.

## Implementation status

Research record only. No implementation or Qlib full-backtest validation has been completed as part of this Scout cycle.

## Adoption boundary

This record is research-only. Its presence does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor/leaderboard entry, demonstrated profitable alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

- `[[bitcoin-onchain-mvrv-zscore-cycle-reversal-2026-08-31]]` — simpler MVRV-family valuation/cycle baseline already represented in this repository.
- `[[bitcoin-onchain-sth-mvrv-dynamic-support-mean-reversion-2026-09-01]]` — short-term-holder MVRV variant with a different holder cohort and mechanism.

## Sources

- TradingView — `Adaptive MVRV & RSI Strategy V6 (Dynamic Thresholds)`, author `wjstienstra`, published 2025-08-17, reviewed 2026-09-21: https://www.tradingview.com/script/oVuTxgUS-Adaptive-MVRV-RSI-Strategy-V6-Dynamic-Thresholds/
