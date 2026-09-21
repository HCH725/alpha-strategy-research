---
schema: strategy-research-record-v1
title: "Bitcoin Realized-Price Cost-Basis Bands Regime"
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
  - https://www.tradingview.com/script/h5ebKajh-BTC-Realized-Price-Bands/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Realized-Price Cost-Basis Bands Regime

## Provenance

- Public TradingView open-source indicator: `BTC Realized Price Bands`.
- Author/page identity: `AriSaiQuant`.
- TradingView page shows original publication on Feb 25 and update on Feb 28; the reviewed page does not expose the year unambiguously, so no year is invented here.
- Stable URL: https://www.tradingview.com/script/h5ebKajh-BTC-Realized-Price-Bands/
- Source reviewed as of 2026-09-21.

## Economic mechanism

### Source-reported

The author defines Bitcoin Realized Price as Realized Market Cap divided by circulating supply and interprets it as a proxy for aggregate holder acquisition cost. The indicator multiplies that anchor by configurable proportional bands. The source presents the bands as a higher-timeframe structural valuation framework: below Realized Price represents aggregate unrealized loss, while progressively higher multiples represent increasing expansion above aggregate holder cost basis. The author explicitly states that the tool does not predict tops or bottoms and is not intended as a short-term timing signal.

### Research interpretation

The falsifiable hypothesis is that **Bitcoin's proportional distance from a point-in-time aggregate holder cost-basis anchor contains incremental information about subsequent medium/long-horizon returns and regime transitions beyond price-only trend, drawdown and volatility controls**.

This is materially different from a volatility envelope: the denominator is an on-chain cost-basis proxy rather than recent price dispersion. The source's fixed multiples can therefore be treated as valuation-state partitions whose predictive content must be tested rather than assumed.

Competing mechanisms should be kept separate:

- **Mean reversion / accumulation:** unusually low price-to-realized-price ratios may reflect broad unrealized losses and capitulation.
- **Trend persistence:** sustained movement above intermediate multiples may identify expansion regimes rather than immediate overvaluation reversals.
- **Exhaustion:** very high multiples may eventually identify distribution/euphoria, but the source warns that price can remain extended for long periods.

## Signal

Source-supported construction:

- `Realized Price = BTC_MARKETCAPREAL / BTC_SUPPLY`.
- Both on-chain series are requested through TradingView and aligned to the chart timeframe.
- Default proportional bands are `0.75x`, `1.0x`, `1.5x`, `2.0x`, `3.0x`, and `3.5x` Realized Price.
- The source uses `INDEX:BTCUSD` for price-zone bar coloring.
- All multipliers are configurable.
- The source describes a macro valuation framework, not a complete trading strategy. It does not specify entry, exit, holding period, re-entry, sizing or short rules.

Research-proposed operationalization for later testing: use `price / realized_price` as a continuous state variable and separately evaluate zone-entry, zone-exit and cross-zone transition events. Test continuation and reversal hypotheses independently at multiple forward horizons. Any trade mapping, holding period, sizing or threshold not listed above is **research-proposed**.

## Required data

- Bitcoin price history, with `INDEX:BTCUSD` as the source-aligned reference or a documented investable proxy.
- Point-in-time Bitcoin Realized Market Cap corresponding to TradingView `BTC_MARKETCAPREAL` or a documented equivalent.
- Point-in-time Bitcoin circulating supply corresponding to `BTC_SUPPLY` or a documented equivalent.
- Timestamp and data-availability metadata sufficient to prevent use of on-chain observations before publication/availability.
- Daily or higher-timeframe history is most consistent with the source's structural-use description; exact research timeframe remains to be specified during testing.

## Execution assumptions

The source supplies no executable trading system. Signal-to-order timing, market/limit choice, fees, spread, slippage, impact, funding, leverage, shorting, sizing and holding period are unspecified.

Any later position rule is research-proposed. To avoid same-bar leakage, a backtest should use only realized-cap and supply observations demonstrably available at the decision timestamp and execute no earlier than the next eligible bar. Perpetual implementations must separately model funding and venue basis.

## Evidence

### Source-reported

The source labels `0.75x` as extreme undervaluation, `1.0x` as aggregate cost basis, `1.5x` as early-bull territory, `2.0x` as mid-cycle, `3.0x` as late-cycle/overheated and `3.5x` as extreme overvaluation. These are source interpretations of heuristic proportional bands, not independently verified performance results. The source explicitly says the multipliers are heuristic rather than statistically optimized and provides no traceable Sharpe, CAGR, drawdown, hit rate or other strategy-performance statistic.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself states that the indicator does not predict tops or bottoms, price can remain above upper bands for prolonged periods, and the framework is not intended for short-term timing. The fixed multipliers are heuristic. Realized Price also depends on the interpretation that last on-chain movement approximates acquisition cost, which can be distorted by self-transfers, custody movements and other non-economic UTXO activity.

The repository already contains MVRV, NUPL, STH-MVRV and other realized-cap/cost-basis families. Their existence is not evidence for these specific proportional bands; this record must demonstrate incremental information rather than inherit credibility from neighboring on-chain metrics.

## Falsification plan

1. Reconstruct Realized Price point-in-time and audit publication/availability timing. Run one-bar/day timestamp-shift placebos to detect hidden look-ahead.
2. Test the continuous `price / realized_price` ratio before testing categorical bands. If discretization adds no OOS value, reject the band layer.
3. Compare against price-only controls: long-horizon momentum/trend, drawdown, realized volatility, moving-average distance and simple log-price normalization.
4. Compare against related realized-cap controls, especially MVRV/MVRV-Z and NUPL. The proportional-band representation must add stable leakage-safe OOS information to justify a separate family.
5. Ablate `realized price -> +0.75/1.0 boundaries -> +1.5/2.0 boundaries -> +3.0/3.5 boundaries`. Do not retain a band merely because it looks historically descriptive.
6. Test competing effects separately: low-zone mean reversion, intermediate-zone trend persistence, and high-zone exhaustion/reversal. Do not combine opposite horizons into one score before establishing each effect.
7. Stress-test multiplier neighborhoods around each source default. Narrow dependence on exact round-number multiples is evidence of instability.
8. Evaluate forward returns and risk over multiple predeclared horizons using walk-forward or expanding-window OOS evaluation. Include all available Bitcoin regimes rather than selecting visually favorable cycles.
9. Compare source-aligned TradingView series with an independent on-chain provider where licensing/data access permits. Material disagreement weakens reproducibility.
10. Research-defined failure criterion: if the ratio/bands do not provide stable incremental leakage-safe OOS predictive or allocation value over the strongest simpler price/on-chain baseline after realistic costs, reject this formulation rather than adding filters.

## Crypto portability

**direct** for Bitcoin because the source and required on-chain series are explicitly Bitcoin-specific.

Portability to other cryptoassets is **unproven**. UTXO/accounting structure, realized-cap methodology, supply definition, chain activity, custody patterns and market maturity differ across assets.

## Limitations

- Not independently reproduced.
- The displayed multiplier levels are heuristic, not statistically optimized.
- The source does not specify a complete trading rule.
- Realized-cap observations require strict point-in-time availability handling.
- Last on-chain movement is an imperfect proxy for economic acquisition price.
- Upper-band residence can persist, creating substantial timing risk for naive contrarian use.
- Any entry/exit, holding period, sizing or additional threshold is research-proposed.

## Implementation status

Research record only. No implementation or Qlib full-backtest validation has been completed as part of this Scout cycle.

## Adoption boundary

This record is research-only. Its presence does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor/leaderboard entry, demonstrated profitable alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

- `[[bitcoin-onchain-mvrv-zscore-cycle-reversal-2026-08-31]]` — related realized-cap valuation family using market value versus realized value and statistical normalization.
- `[[bitcoin-onchain-net-unrealized-profit-loss-nupl-macro-cycle-2026-09-01]]` — related aggregate unrealized-profit/loss regime family.
- `[[bitcoin-onchain-sth-mvrv-dynamic-support-mean-reversion-2026-09-01]]` — related holder-cost-basis family focused on short-term holders.

## Sources

- TradingView — `BTC Realized Price Bands`, author `AriSaiQuant`, public open-source script; page shows Feb 25 publication and Feb 28 update, reviewed 2026-09-21: https://www.tradingview.com/script/h5ebKajh-BTC-Realized-Price-Bands/
