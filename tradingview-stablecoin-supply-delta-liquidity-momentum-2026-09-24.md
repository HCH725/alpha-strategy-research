---
schema: strategy-research-record-v1
title: TradingView Stablecoin Supply-Delta Liquidity Momentum Hypothesis
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-24
sources:
  - https://www.tradingview.com/script/7U1m55qP-Crypto-USD-Liquidity-Delta-tedtalksmacro/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Stablecoin Supply-Delta Liquidity Momentum Hypothesis

## Provenance

- Public TradingView open-source script: `Crypto USD Liquidity Delta [tedtalksmacro]`.
- Author/page identity: `tedtalksmacro`.
- Stable URL: https://www.tradingview.com/script/7U1m55qP-Crypto-USD-Liquidity-Delta-tedtalksmacro/
- Published 2023-10-22; public release notes reviewed through 2024-02-18.
- Source reviewed as of 2026-09-24.
- Repository deduplication on current `main` found no artifact for this canonical TradingView source. A related SSR record exists, but its normalized construction is a Bitcoin-price-to-stablecoin-supply ratio/oscillator; this record isolates changes in aggregate stablecoin supply as the explanatory variable, so the signal construction and data dependency are materially distinct.

## Economic mechanism

### Source-reported

The source measures percentage changes in aggregate USD stablecoin liquidity over multiple horizons and, in its 2024-02-18 release note, describes week-on-week stablecoin-supply change as a gauge of overall crypto-market interest. It states that positive inflows typically correlate with higher Bitcoin/crypto prices and negative flows with lower prices.

### Research interpretation

The falsifiable hypothesis is that point-in-time expansion or contraction in aggregate stablecoin supply contains incremental information about subsequent crypto returns because stablecoins are deployable quote/collateral liquidity. A positive supply delta may precede or accompany risk deployment; contraction may indicate liquidity withdrawal.

Correlation is not assumed to imply lead-lag alpha. Stablecoin issuance may react to crypto prices, reflect treasury/chain migration, or be contemporaneous rather than predictive. The hypothesis survives only if lagged supply changes add OOS information beyond price momentum, volatility, and stablecoin-price/depeg effects.

## Signal

Source-reported construction:

- Aggregate stablecoin liquidity is measured through stablecoin supplies.
- The original publication describes week-on-week (WoW), month-on-month (MoM), quarter-on-quarter (QoQ), and year-on-year (YoY) percentage changes in aggregate stablecoin liquidity.
- A 2023-12-22 release note says the visualization was updated to toggle YoY, QoQ and MoM changes.
- The 2024-02-18 release note specifically frames week-on-week USD stablecoin-supply delta as a gauge of crypto-market interest.
- Positive versus negative changes are interpreted directionally by the source, but the public page does not specify a complete executable entry/exit lifecycle.

The reviewed public page does not unambiguously expose the exact stablecoin constituent list, constituent data vendors/symbols, timestamp at which supply observations become available, entry timestamp, exit, holding period, re-entry, sizing, stop, take-profit, or execution venue. These fields are `underspecified` and are not invented here.

Research-proposed operationalization for later testing only: construct point-in-time aggregate stablecoin supply, compute predeclared WoW/MoM/QoQ changes, lag the signal by verified data-availability time, and measure subsequent BTC and liquid-crypto returns over fixed horizons. Test both sign and magnitude without optimizing thresholds in-sample.

## Required data

- Point-in-time circulating/issued supply histories for the stablecoins included in the reconstructed aggregate.
- Verified publication/availability timestamps for each supply series; revised historical values must not leak into earlier observations.
- BTC and liquid-crypto OHLCV for target-return measurement.
- Stablecoin USD prices to distinguish supply changes from depeg/valuation effects where relevant.
- Consistent timestamp/timezone and missing-data rules across constituent series.
- Constituent-history handling for stablecoins that launch, disappear, migrate chains, or materially lose relevance.

## Execution assumptions

The source does not specify order type, signal-to-order timing, same-bar versus next-bar execution, fill model, fees, spread, slippage, impact, leverage, funding, borrow, latency, partial fills, or failures.

Any later tradable implementation should act only after the underlying supply observation was actually available and should use realistic costs. Using revised supply history or same-period price information before publication would create look-ahead bias.

## Evidence

### Source-reported

The source qualitatively states that positive stablecoin inflows typically correlate with higher Bitcoin/crypto pricing and negative flows with lower pricing. The reviewed public page provides no traceable Sharpe, CAGR, win rate, drawdown, t-statistic, sample result, or independent backtest supporting predictive alpha.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-reported negative empirical result was identified on the reviewed page; absence is not evidence of no negative result. The stated relationship is correlation, not demonstrated predictive causality. Stablecoin supply can change for reasons unrelated to immediate crypto risk deployment, and constituent/data-vendor changes can create artificial deltas.

## Falsification plan

1. Reconstruct aggregate supply point-in-time and verify observation availability before any return alignment.
2. Compare lagged WoW/MoM/QoQ supply delta against price-momentum-only, realized-volatility, and no-signal baselines.
3. Test whether supply delta predicts future returns rather than merely moving contemporaneously with them; include lead/lag reversal tests.
4. Run constituent ablations (major stablecoins individually versus aggregate) and leave-one-stablecoin-out tests. Reject an aggregate effect driven by one unstable constituent unless that dependency is robust and economically explainable.
5. Control for depeg episodes, stablecoin migrations/redemptions, broad USD liquidity regimes, and major crypto market shocks.
6. Test BTC and a predeclared liquid-crypto universe across bull, bear, high-volatility and low-volatility regimes using walk-forward/OOS evaluation.
7. Apply realistic execution costs for any directional implementation. If predictive information is absent OOS or disappears after point-in-time alignment/costs, reject the alpha hypothesis rather than add filters.
8. Compare directly with the existing SSR-style price/supply ratio construction. The pure supply-delta signal must demonstrate incremental information to justify remaining a separate research family.

All operational thresholds, target horizons, controls, and acceptance criteria above are `research-proposed`; any eventual numerical cutoff is a `research-defined falsification threshold`.

## Crypto portability

`direct`: the cited TradingView source explicitly studies aggregate crypto stablecoin liquidity and relates its changes to Bitcoin/crypto pricing. Portability across historical periods remains unproven because stablecoin composition, chains, regulation, market share, collateral use, and data availability change materially over time.

## Limitations

- `underspecified`: exact constituent universe/data symbols and complete trading lifecycle are not exposed by the reviewed public page.
- `data gap`: point-in-time supply availability and revision policy must be independently established before testing.
- `not independently reproduced`.
- `unproven`: the source reports qualitative correlation, not verified predictive alpha.
- Aggregate supply growth does not identify whether newly issued stablecoins are actually deployed into crypto assets.

## Implementation status

Research record only. No implementation or Qlib full-backtest validation has been completed for this record.

## Adoption boundary

`research-only / not-implemented / not-approved`.

Presence in this repository does not mean the hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor/leaderboard entry, is profitable, or is approved for Paper, Testnet, or Live trading.

## Related Wiki records

No stable Hermes Wiki Brain links are asserted from this GitHub-only Scout run.

## Sources

- TradingView — `Crypto USD Liquidity Delta [tedtalksmacro]`, author `tedtalksmacro`: https://www.tradingview.com/script/7U1m55qP-Crypto-USD-Liquidity-Delta-tedtalksmacro/ (published 2023-10-22; release notes through 2024-02-18; reviewed 2026-09-24).
