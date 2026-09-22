---
schema: strategy-research-record-v1
title: Bitcoin Dominance Excluding Stablecoins as a BTC-vs-Alt Relative-Strength Signal
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-04-12
sources:
  - https://www.tradingview.com/script/ekdRLga4-BTC-Dominance-Excluding-Stablecoins/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Dominance Excluding Stablecoins as a BTC-vs-Alt Relative-Strength Signal

## Provenance

TradingView public open-source indicator **BTC Dominance Excluding Stablecoins**, author `Crypto-KDuB`, stable URL https://www.tradingview.com/script/ekdRLga4-BTC-Dominance-Excluding-Stablecoins/ . The page states publication in 2025 and an update dated 2025-04-12; reviewed 2026-09-22.

Repository deduplication was performed against current `main` before capture using both the canonical TradingView URL and normalized signal terms. No record for this canonical source or this stablecoin-excluded BTC-dominance construction was found. Existing stablecoin-dominance and liquidity records use stablecoin share itself as the signal; this hypothesis instead asks whether removing stablecoins from the denominator improves measurement of Bitcoin's relative share of the volatile crypto market.

## Economic mechanism

### Source-reported

The source argues that standard Bitcoin dominance can be distorted by stablecoin market capitalization. It constructs an adjusted dominance measure intended to represent Bitcoin's market share against the non-stable crypto market by subtracting USDT and USDC capitalization from total crypto market capitalization.

### Research interpretation

The falsifiable mechanism is a denominator-composition effect. Stablecoin issuance, redemption, or parking demand can move standard BTC dominance even when relative valuation between Bitcoin and volatile altcoins has not changed proportionally. If so, stablecoin-excluded BTC dominance may be a cleaner state variable for BTC-versus-altcoin relative strength or rotation.

This does not imply that stablecoin flows are noise in general; they may carry independent liquidity information. The test is specifically whether excluding them improves the dominance measure for forecasting **relative BTC versus altcoin returns**, after controlling for standard BTC dominance and stablecoin dominance separately.

## Signal

**Source-supported observable:**

- Bitcoin market capitalization: `CRYPTOCAP:BTC`.
- Total crypto market capitalization: `CRYPTOCAP:TOTAL`.
- Stablecoin adjustment: subtract `CRYPTOCAP:USDT` and `CRYPTOCAP:USDC` market capitalizations from total market capitalization.
- Adjusted BTC dominance: `BTC market cap / (TOTAL market cap - USDT market cap - USDC market cap) * 100`.
- The source notes daily or higher timeframes as preferable for smoother readings.

The source does not provide a complete systematic entry, exit, holding, re-entry, sizing, or shorting rule. Those elements are **underspecified**.

**Research-proposed operationalization:** compare trailing changes and trailing-only standardized deviations of adjusted BTC dominance with the same transforms of standard BTC.D. Test whether rising adjusted dominance forecasts positive subsequent BTC-minus-altcoin-basket relative returns and falling adjusted dominance forecasts the converse. Lookbacks, rebalance frequency, signal thresholds, holding horizons, and portfolio construction must be selected ex ante and are `research-proposed`, not source-reported.

## Required data

- Point-in-time `CRYPTOCAP:BTC`, `CRYPTOCAP:TOTAL`, `CRYPTOCAP:USDT`, and `CRYPTOCAP:USDC` market-cap series.
- Standard `BTC.D` for the direct baseline.
- BTC price returns and a point-in-time altcoin basket or broad alt-market-cap return proxy for the relative-return target.
- Timestamps and documented availability/revision behavior for all CRYPTOCAP series.
- Point-in-time stablecoin composition for robustness tests; the source's formula excludes only USDT and USDC and therefore does not represent all historical stablecoins.

## Execution assumptions

The source is an indicator, not an executable strategy, and does not specify order type, signal-to-order timing, fees, spread, slippage, market impact, capacity, funding, borrow availability, leverage, margin, partial fills, or latency.

For research, any tradable BTC-versus-altcoin implementation should use next-observation/next-bar execution after all market-cap inputs are available, with explicit fees and slippage. A long-short implementation must account for perpetual funding or spot borrow/short constraints. These are `research-proposed` assumptions.

## Evidence

### Source-reported

The TradingView page documents the formula and qualitative motivation but reports no backtest, Sharpe ratio, CAGR, win rate, drawdown, or other verified performance statistic. It notes that TradingView CRYPTOCAP feeds may have delays or variations and that the implementation currently excludes USDT and USDC only.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-reported performance evidence was provided. The denominator can still be composition-sensitive because stablecoins other than USDT/USDC remain in `TOTAL`, and market-cap indices may have constituent, supply, or historical-revision effects. Absence of a reported failure is not evidence that the hypothesis works.

## Falsification plan

1. **Primary baseline:** compare predictive information for future BTC-minus-altcoin relative returns from standard BTC.D versus stablecoin-excluded BTC dominance using identical trailing transforms and horizons.
2. **Incremental-information test:** regress or rank future relative returns on standard BTC.D change, stablecoin dominance/change, and adjusted-dominance change. Reject the incremental thesis if the adjusted term is unstable or adds no leakage-safe OOS value.
3. **Denominator ablation:** test no exclusion, USDT-only, USDC-only, USDT+USDC, and a point-in-time broader stablecoin basket where historically available. If apparent alpha depends on one arbitrary denominator definition, weaken or reject the mechanism.
4. **Composition control:** reconstruct constituent availability point-in-time and avoid applying today's stablecoin set retroactively. Test periods around major stablecoin launches, contractions, and depegs separately.
5. **Target control:** test BTC versus equal-weight and liquidity-weighted point-in-time alt baskets, plus a broad alt-market-cap proxy. A result confined to one survivorship-biased basket is insufficient.
6. **Regime robustness:** separate bull, bear, high-volatility, low-volatility, and stablecoin stress/depeg regimes.
7. **Timing placebo:** lag the market-cap inputs by realistic availability delays and compare against intentionally shifted signals. Performance that requires unavailable same-timestamp data fails.
8. **Cost/OOS requirement:** any tradable rotation or long-short formulation must survive realistic fees, spread, slippage, funding/borrow where applicable, and walk-forward OOS evaluation.
9. **Failure action:** if adjusted dominance does not consistently outperform or add information beyond standard BTC.D plus stablecoin dominance, reject the stablecoin-exclusion layer and retain the simpler baselines.

## Crypto portability

`direct` — the source and all core inputs are crypto-native.

Portability across venues is indirect because the signal is market-cap based rather than venue-specific, while execution occurs on particular spot or derivative venues. A tradable test must therefore separate index timestamp/availability from executable venue prices and account for 24/7 trading, funding, borrow, liquidity, and venue fragmentation.

## Limitations

- `underspecified`: no complete trading lifecycle is source-reported.
- `not independently reproduced`.
- `data gap`: point-in-time CRYPTOCAP constituent and revision policy must be established before historical testing.
- USDT and USDC are the only stablecoins explicitly removed by the source; historical stablecoin composition changes materially.
- Market-cap dominance is a ratio and can move because of numerator, denominator, supply, or price changes; interpreting it literally as capital flow would be too strong.
- The source provides a measurement construction, not evidence of profitable alpha.

## Implementation status

No implementation or backtest in the research stack has been completed. This record only normalizes a public TradingView hypothesis for later Research Intake Review.

## Adoption boundary

Research-only. Presence in this repository does not mean this record passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, demonstrated profitable or validated alpha, or received approval for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

No Hermes Wiki lookup was performed because this Scout is GitHub-only. Repository-adjacent concepts include stablecoin dominance, stablecoin liquidity regimes, BTC dominance, and crypto rotation signals.

## Sources

- TradingView — `Crypto-KDuB`, **BTC Dominance Excluding Stablecoins**, public open-source indicator, updated 2025-04-12: https://www.tradingview.com/script/ekdRLga4-BTC-Dominance-Excluding-Stablecoins/ (reviewed 2026-09-22).
