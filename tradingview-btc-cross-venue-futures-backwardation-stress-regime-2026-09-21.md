---
schema: strategy-research-record-v1
title: BTC Cross-Venue Futures Backwardation Stress Regime
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
  - https://www.tradingview.com/script/jvhRyOes-BTC-Futures-Basis/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BTC Cross-Venue Futures Backwardation Stress Regime

## Provenance

Public TradingView open-source script **BTC Futures Basis**, author `daylad`, published 2022-01-11. Stable source URL: https://www.tradingview.com/script/jvhRyOes-BTC-Futures-Basis/. Reviewed 2026-09-21.

The source describes historical BTC futures basis across BitMEX, Binance, Deribit, OKEx and FTX March/June contracts, plus CME continuous next contract. It states that contract symbols are customizable and require periodic updating as futures expire. FTX is defunct and the historical venue list must not be treated as a current executable universe.

## Economic mechanism

### Source-reported

The author presents futures basis as a measure of bullish/bearish sentiment and states that market-wide backwardation usually occurs during heavy sell-offs such as liquidation cascades. The script includes customizable alerts for backwardation events.

### Research interpretation

The falsifiable hypothesis is that **simultaneous BTC futures backwardation across multiple independent venues identifies an unusually severe derivatives stress regime rather than an idiosyncratic contract dislocation**. If broad backwardation reflects forced deleveraging and urgent demand to exit leveraged longs, its onset or subsequent normalization may contain incremental information about short-horizon continuation versus exhaustion/reversal after controlling for spot returns and volatility.

Cross-venue breadth, normalization rules, and any trading action are `research-proposed`; they are not claimed by the source.

## Signal

Source-supported elements:

- Instrument: Bitcoin futures basis.
- Historical venue set named by the source: BitMEX, Binance, Deribit, OKEx and FTX March/June futures; CME continuous next contract is displayed separately.
- State of interest: backwardation.
- The source provides a customizable backwardation alert and recommends a 1-minute chart for alerts.
- CME is explicitly excluded from the source alert logic to avoid false triggers.
- Futures symbols must be updated as contracts expire.

Underspecified by the public description:

- exact basis formula and annualization convention;
- default alert threshold;
- minimum number of venues/contracts required to call an event market-wide;
- entry, exit, holding period, re-entry, sizing, and stop logic;
- whether the intended response to backwardation is continuation, contrarian reversal, or regime-only filtering.

`research-proposed` operationalization for later testing:

1. Compute causally aligned basis for active BTC dated futures against a contemporaneous BTC spot/index reference, using only currently live venues and contracts at each timestamp.
2. Define cross-venue backwardation breadth as the fraction of eligible venue-contract observations with basis below zero; also retain median basis magnitude.
3. Test event onset and subsequent normalization separately. Do not assume direction in advance: compare (a) downside continuation during broadening/deepening backwardation with (b) rebound after backwardation breadth/magnitude peaks and begins to normalize.
4. Form signals only after all component prices required for that timestamp are observable. No historical FTX observations may be used as if FTX remained tradeable after its closure.

## Required data

- Point-in-time BTC dated-futures prices by venue and contract expiry.
- Contemporaneous BTC spot or index reference price with a documented construction.
- Contract expiry timestamps and specifications sufficient to distinguish active contracts and time-to-expiry.
- Venue availability/lifecycle metadata to prevent survivorship and stale-symbol errors.
- UTC-normalized timestamps and explicit handling of asynchronous venue updates.
- For stronger falsification: perpetual funding, open interest, liquidation data, spot returns and realized volatility as controls rather than prerequisites to the core basis signal.

## Execution assumptions

The source does not specify an executable trading strategy, order type, fill model, fees, spread, slippage, impact, leverage, margin, position sizing, or exit logic.

Any later test should use next-observable-bar execution after signal formation, venue-specific fees/spreads and conservative slippage. A cross-venue indicator must not imply that every displayed contract is directly tradeable by the same account or under identical margin rules.

## Evidence

### Source-reported

The source states that market-wide backwardation usually occurs during heavy sell-offs such as liquidation cascades and presents the indicator as useful for tracking BTC futures sentiment. It reports no Sharpe ratio, win rate, CAGR, drawdown, or independently audited performance statistic.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source's displayed venue universe is historically stale: it includes FTX, and dated futures symbols expire and require maintenance. The source itself notes the symbol-maintenance requirement and excludes CME from its alert logic. No source-reported evidence establishes that backwardation predicts continuation or reversal rather than merely coinciding with an already-observed sell-off.

## Falsification plan

1. **Point-in-time reconstruction:** build the eligible venue/contract set as it actually existed at each timestamp; reject any test that backfills today's venue universe into history.
2. **Baseline:** compare cross-venue backwardation breadth/magnitude against spot return, realized volatility, drawdown and a single-venue basis signal. The composite must add information beyond an already-large sell-off.
3. **Breadth ablation:** single venue -> median basis -> backwardation breadth -> median + breadth. Drop the composite if breadth adds no stable OOS value.
4. **Venue robustness:** leave one venue out at a time and separate CME from crypto-native venues because the source itself treats CME differently in alerts.
5. **Horizon competition:** test downside continuation and post-stress reversal over multiple predeclared short horizons rather than choosing direction after observing results.
6. **Liquidation-mechanism check:** where reliable liquidation/OI data exist, test whether broad backwardation is associated with contemporaneous forced deleveraging and whether that association explains any predictive effect.
7. **Timestamp placebo:** shift basis inputs forward/backward and reject results that depend on non-causal alignment.
8. **Cost sensitivity:** apply realistic fees, spreads and slippage. Reject a tradeable interpretation if gross predictability disappears after conservative costs.
9. **OOS requirement:** parameters, breadth thresholds and horizon selection must be frozen before holdout evaluation. If the cross-venue construction cannot outperform the simpler price/volatility or strongest single-venue baseline in leakage-safe OOS tests, reject the added complexity.

## Crypto portability

direct

The source itself studies BTC futures. Portability across crypto derivatives remains exposed to venue fragmentation, different contract specifications, expiry calendars, index/mark construction, funding/perpetual-vs-dated differences, asynchronous timestamps and exchange lifecycle risk.

## Limitations

- `underspecified`: public description does not expose a complete executable trading rule or exact alert threshold.
- `not independently reproduced`.
- `data gap`: robust historical point-in-time dated-futures data and venue lifecycle metadata are required.
- The historical source universe includes FTX and therefore cannot be copied into a current implementation.
- Backwardation may be contemporaneous stress measurement rather than forward alpha.
- Cross-venue breadth and normalization are `research-proposed`.

## Implementation status

Research-only. No implementation in the research stack and no Qlib full backtest has been completed.

## Adoption boundary

Presence in this repository does not mean this record passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received Paper, Testnet, or Live approval.

## Related Wiki records

No stable Hermes Wiki Brain record is asserted from this GitHub-only Scout run.

## Sources

- TradingView — daylad, **BTC Futures Basis**, published 2022-01-11, reviewed 2026-09-21: https://www.tradingview.com/script/jvhRyOes-BTC-Futures-Basis/
