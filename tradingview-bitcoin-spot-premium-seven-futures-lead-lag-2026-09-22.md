---
schema: strategy-research-record-v1
title: Bitcoin Spot-Premium vs Futures Basket Lead-Lag Regime
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
  - https://www.tradingview.com/script/wFYxVeN2-Bitcoin-Spot-Premium/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Spot-Premium vs Futures Basket Lead-Lag Regime

## Provenance

Public TradingView open-source indicator **Bitcoin Spot Premium**, author **ImaWrknMan**, originally published 2022-03-20 and updated 2023-05-18. Stable source URL: https://www.tradingview.com/script/wFYxVeN2-Bitcoin-Spot-Premium/ . Source reviewed as of 2026-09-22.

The source states that it plots the difference between Bitcoin spot price and the average of seven futures prices. Its 2023 update notes several perpetual-symbol migrations, including Bybit, BitMEX, OKX, Phemex and Binance examples. The reviewed public description does not expose a complete current seven-contract basket unambiguously, so the exact basket is preserved as **underspecified** rather than reconstructed from inference.

## Economic mechanism
### Source-reported

The author states the idea that spot leads the market: when Bitcoin spot trades significantly above the futures basket, price should increase, and vice versa. The page suggests three qualitative uses: sharp premium changes as possible reversal context, persistently large premium as trend-continuation confirmation, and divergences as possible trend-exhaustion evidence.

### Research interpretation

The falsifiable mechanism is **spot-versus-derivatives price discovery**. If unlevered spot demand moves first while leveraged futures lag, a positive spot-minus-futures premium may contain short-horizon continuation information until derivatives catch up. Conversely, an extreme or rapidly reversing premium may represent temporary segmentation, liquidity stress, or exhaustion and therefore mean-revert.

Continuation and reversal are competing hypotheses. The record does not assume either direction is profitable.

## Signal

Source-supported construction:

- Target asset: Bitcoin.
- Core variable: Bitcoin spot price minus the average price of seven futures/perpetual markets.
- Positive premium: spot above the futures basket.
- Negative premium: spot below the futures basket.
- Source-proposed interpretations: persistent premium for trend confirmation; sharp premium change for reversal context; price/premium divergence for exhaustion context.

Underspecified by the reviewed public description:

- exact spot venue/ticker used in every source revision;
- complete current seven-contract basket and weighting details beyond the stated average;
- premium normalization (absolute versus percentage) for any executable threshold;
- quantitative threshold for “significantly” positive/negative premium;
- exact divergence definition;
- entry, exit, holding period, re-entry, stop, take-profit and sizing rules.

Research-proposed operationalization:

1. Reconstruct point-in-time spot and futures/perpetual baskets using only contracts live at each timestamp.
2. Compare raw spread with percentage-normalized and volatility-normalized premium, without treating those transformations as source-reported.
3. Test three predeclared event families separately: premium persistence/continuation, premium shock/reversal, and price-versus-premium divergence/exhaustion.
4. Form signals only after synchronized source bars are complete and evaluate forward returns at fixed horizons.

## Required data

- Point-in-time BTC spot OHLC or mid/close from the source-compatible spot venue.
- Point-in-time BTC futures/perpetual prices for the constituent basket.
- Contract metadata sufficient to distinguish linear/inverse contracts, quote currency, expiry versus perpetual structure, listing/delisting dates and symbol migrations.
- Synchronized timestamps and consistent candle boundaries, preferably UTC-normalized.
- Missing constituent observations and venue outages must remain explicit; do not silently forward-fill or substitute future-known venues.
- For mechanism controls: optional spot/futures volume, open interest, funding and basis data may be used as research-proposed diagnostics, not as source-required inputs.

## Execution assumptions

The source is an indicator rather than a complete trading strategy. It does not specify signal-to-order timing, market/limit order choice, fills, fees, spread, slippage, market impact, funding, leverage/margin, borrow, latency, partial fills or capacity.

Any later executable test should form the premium from data actually available at bar close and execute no earlier than the next feasible timestamp unless intrabar availability is explicitly modeled. Perpetual funding and all trading costs must be included when the tested position uses derivatives.

## Evidence
### Source-reported

The TradingView page reports qualitative interpretations only. No traceable Sharpe, CAGR, drawdown, win rate, statistical significance or audited profitability result was identified. No performance figure is promoted here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source does not establish that spot always leads derivatives, that the lead is stable across regimes, or that the premium survives costs. Cross-venue spreads can arise mechanically from quote-currency differences, stale/asynchronous bars, venue-specific liquidity, contract design, funding/basis, outages, or temporary market segmentation rather than predictive information.

The source itself required symbol updates as exchanges and contract names changed, demonstrating material point-in-time universe risk. No reviewed source evidence establishes a profitable net-of-cost rule.

## Falsification plan

1. **Price-only baseline:** compare every premium rule against BTC return/momentum and reversal baselines at the same horizon.
2. **Basket ablation:** test each available futures venue individually, equal-weight basket, median basket, and leave-one-venue-out variants. Reject aggregation if it adds no robust OOS information.
3. **Direction competition:** predeclare continuation after persistent premium and reversal after premium shocks as separate hypotheses; do not select the winning sign in-sample and relabel it as the original thesis.
4. **Divergence test:** define divergence mechanically before testing and compare it with simple price momentum/reversal controls.
5. **Normalization:** raw price spread versus percentage and volatility-normalized versions. Robust evidence should not depend on one arbitrary scale transformation.
6. **Quote/contract controls:** separate USD versus stablecoin quote effects, inverse versus linear perpetuals, dated futures versus perpetuals, and funding/basis effects where data permit.
7. **Point-in-time universe:** reconstruct historical listings and symbol migrations. Never backfill a modern seven-venue basket into periods when constituents did not exist.
8. **Timestamp placebo:** shift one side of the spread by one bar and deliberately desynchronize venue timestamps. Apparent alpha that survives or improves under these placebos is evidence of a data-alignment artifact.
9. **Regime robustness:** bull/bear, high/low realized volatility, high/low funding, weekend/weekday and high/low liquidity regimes.
10. **OOS and costs:** require chronological out-of-sample evaluation with fees, spread, slippage and funding. If spot-premium features do not add robust net-of-cost information beyond price-only and simple basis controls, reject the hypothesis rather than adding filters.

## Crypto portability

direct

The source is explicitly a Bitcoin spot-versus-crypto-futures construction. Portability across venues or other crypto assets remains dependent on comparable spot liquidity, derivative coverage, quote currency, funding, contract specification and synchronized 24/7 timestamps.

## Limitations

- Complete current seven-contract basket is underspecified in the reviewed public description.
- Exact executable premium threshold is underspecified.
- Exact divergence rule is underspecified.
- The page provides no complete entry/exit/holding/sizing strategy.
- Venue and symbol migrations create substantial survivorship and point-in-time risks.
- Spot/futures spreads may reflect mechanical basis or quote effects rather than lead-lag information.
- Not independently reproduced.

## Implementation status

Research-only normalization. No implementation in the research stack and no Qlib full backtest has been completed for this record.

## Adoption boundary

This record is external research material only. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

Potential conceptual relatives include crypto basis, cross-venue price discovery, spot/perpetual segmentation, funding and derivatives crowding. No Wiki lookup was performed because this Scout run is GitHub-only.

## Sources

- TradingView — ImaWrknMan, **Bitcoin Spot Premium**: https://www.tradingview.com/script/wFYxVeN2-Bitcoin-Spot-Premium/ (public open-source indicator; published 2022-03-20; updated 2023-05-18; reviewed 2026-09-22).
