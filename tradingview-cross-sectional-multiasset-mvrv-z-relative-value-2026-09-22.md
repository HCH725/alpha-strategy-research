---
schema: strategy-research-record-v1
title: Cross-Sectional Multiasset MVRV-Z Relative-Value Hypothesis
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
  - https://www.tradingview.com/script/ddUrhdPk-Multiasset-MVRVZ-MVRVZ-for-Multiple-Crypto-Assets-Da-Prof/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Sectional Multiasset MVRV-Z Relative-Value Hypothesis

## Provenance

- Public TradingView open-source script: `Multiasset MVRVZ - MVRVZ for Multiple Crypto Assets [Da_Prof]` by `Da_Prof`.
- Stable URL: https://www.tradingview.com/script/ddUrhdPk-Multiasset-MVRVZ-MVRVZ-for-Multiple-Crypto-Assets-Da-Prof/
- Published: 2025-01-22.
- Reviewed/source as-of: 2026-09-22.
- The source exposes MVRV-Z for the chart asset and a selectable comparison asset when Coin Metrics data are available.

## Economic mechanism

### Source-reported

The source describes MVRV-Z as `(market cap - realized cap) / stdev(market cap)`. It interprets relatively high readings as possible overvaluation and relatively low readings as possible undervaluation. It notes historical top/bottom associations for some assets such as BTC, but does not claim a tested cross-sectional trading strategy.

### Research interpretation

The materially distinct research hypothesis is cross-sectional rather than BTC cycle timing: among crypto assets with point-in-time comparable realized-cap data, relative MVRV-Z dispersion may encode differences in aggregate holder unrealized profit/loss and therefore subsequent relative returns. A falsifiable version is that assets with unusually low MVRV-Z relative to peers subsequently outperform unusually high-MVRV-Z peers after controlling for momentum, volatility, liquidity, size and asset age.

This cross-sectional portfolio interpretation is `research-proposed`; it is not a source-reported strategy.

## Signal

Source-supported measurement:

- MVRV-Z = `(market cap - realized cap) / stdev(market cap)`.
- The indicator computes on weekly data and displays consistently on weekly and lower chart timeframes.
- The source uses a fixed prior-week window for the standard-deviation calculation; default is approximately two years of weekly data.
- The chart asset can be compared with a second selectable asset; BTC is the default comparison series.

`research-proposed` operationalization for falsification only:

1. At each weekly formation timestamp, form a point-in-time universe containing only assets whose market-cap and realized-cap series were actually available then.
2. Reconstruct each asset's MVRV-Z using only information available by that timestamp and a predeclared rolling weekly window.
3. Cross-sectionally rank MVRV-Z. Test both continuous rank spreads and coarse low-versus-high portfolios rather than fitting source-unsupported thresholds.
4. Evaluate forward relative returns over predeclared weekly horizons with delayed execution after data availability.
5. Rebalance weekly in the primary test; alternative horizons are robustness checks, not independent discoveries.

Long/short thresholds, portfolio weights, holding horizon, re-entry and risk sizing are underspecified by the source and therefore must not be treated as source rules.

## Required data

- Point-in-time market capitalization and realized capitalization for each eligible crypto asset.
- Weekly timestamps aligned to the source measurement convention.
- Tradable spot/perpetual prices for subsequent-return measurement, with explicit venue mapping.
- Point-in-time asset eligibility, data-start dates and delisting history.
- Liquidity, market-cap/size, momentum and realized-volatility controls.
- Data-vintage/revision metadata where available.
- Missing observations must not be forward-filled across periods where the on-chain series was unavailable.

## Execution assumptions

The source is an indicator and does not specify executable orders, fees, spread, slippage, impact, leverage, funding, borrow, partial fills or portfolio capacity.

For research, signals must be lagged until the underlying on-chain observation is demonstrably available. Any long-short test must include realistic spot/perpetual implementation costs, funding/borrow constraints and survivorship-safe eligibility. These are `research-proposed` assumptions.

## Evidence

### Source-reported

The source states that MVRV-Z historically associates high values with tops and low values with bottoms for some assets such as BTC. It does not report a cross-sectional backtest, Sharpe ratio, CAGR, drawdown, win rate or statistical significance for the relative-value hypothesis recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-reported cross-sectional evidence was identified. The source itself only visualizes multiple assets and therefore does not establish that MVRV-Z levels are comparable across assets with different histories, token economics, supply accounting or realized-cap semantics. Absence of reported negative results is not evidence that none exist.

## Falsification plan

1. **Baseline:** compare cross-sectional MVRV-Z rank against simple price momentum, market-cap/size, realized-volatility and raw MVRV baselines.
2. **BTC-cycle control:** neutralize or condition on BTC market regime to test whether the apparent spread is merely common crypto beta/cycle exposure.
3. **Within-asset versus cross-sectional ablation:** compare each asset's own historical MVRV-Z percentile with peer-relative rank. Reject the cross-sectional layer if it adds no stable OOS information.
4. **Normalization ablation:** compare the source-style rolling MVRV-Z with raw MVRV and expanding/alternative predeclared rolling windows. Reject if results depend on one narrow window choice.
5. **Universe integrity:** reconstruct point-in-time availability and delistings. Reject results that disappear after survivorship-safe universe formation.
6. **Data-timing test:** lag on-chain observations by conservative availability delays and run timestamp placebo tests. Reject if alpha requires same-period information that was not demonstrably available.
7. **Asset-family robustness:** test BTC/ETH separately from younger or structurally different networks; do not pool incomparable realized-cap definitions merely to increase sample size.
8. **Cost/capacity:** require the relative-return spread to survive realistic turnover, fees, spread, slippage, funding/borrow and liquidity screens.
9. **OOS requirement:** use walk-forward evaluation with parameters fixed from prior data. Failure to show stable incremental OOS information over the controls rejects the hypothesis.

## Crypto portability

`direct` for the measurement because the source itself applies MVRV-Z to multiple crypto assets. The cross-sectional trading interpretation remains `unproven`.

Portability risks include heterogeneous realized-cap methodology, token issuance/burn mechanics, staking and bridged supply, exchange/liquidity fragmentation, shortability, perpetual funding, differing data histories and the possibility that MVRV-Z is not cardinally comparable across networks.

## Limitations

- `underspecified`: no source-defined portfolio construction, entry/exit, holding period or risk sizing.
- `not independently reproduced`.
- `data gap`: point-in-time Coin Metrics/TradingView availability and revision history must be established before testing.
- `unproven`: displaying two assets does not demonstrate cross-sectional predictive power.
- Cross-network realized-cap semantics may be structurally non-comparable.
- A two-year rolling normalization can produce unstable ranks for young assets or regime changes.

## Implementation status

Research record only. No implementation or Qlib full-backtest validation has been completed for this hypothesis.

## Adoption boundary

`research-only / not-implemented / not-approved`.

Presence in this repository does not mean the hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor/leaderboard entry, is profitable, or is approved for Paper, Testnet or Live trading.

## Related Wiki records

- `[[quant/bitcoin-onchain-mvrv-zscore-cycle-reversal-2026-08-31]]` — related BTC time-series MVRV-Z cycle hypothesis; this record instead tests peer-relative cross-sectional information.

## Sources

- TradingView, `Multiasset MVRVZ - MVRVZ for Multiple Crypto Assets [Da_Prof]`, author `Da_Prof`, published 2025-01-22, reviewed 2026-09-22: https://www.tradingview.com/script/ddUrhdPk-Multiasset-MVRVZ-MVRVZ-for-Multiple-Crypto-Assets-Da-Prof/
