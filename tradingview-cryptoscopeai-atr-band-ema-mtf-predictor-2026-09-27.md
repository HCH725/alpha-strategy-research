---
schema: strategy-research-record-v1
title: CryptoScopeAI ATR Bands, EMA & Multi-Timeframe Trend Predictor
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-27
sources:
  - https://www.tradingview.com/script/G6jXOmkU-CryptoScopeAI-ATR-Bands-EMA-Trend-Predictor-LONG-SHORT/
  - https://www.tradingview.com/script/crTK0Gc3-CryptoScopeAI-Strategy-v11/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# CryptoScopeAI ATR Bands, EMA & Multi-Timeframe Trend Predictor

## Provenance

Public TradingView strategy by `cryptoscopeai30`. The current public v12 page is `G6jXOmkU`; the public v11 predecessor is `crTK0Gc3`. The script is protected/closed-source but publicly viewable and usable on TradingView; this record normalizes only the publicly described rules and does not reproduce Pine code. Source reviewed as of 2026-09-27.

## Economic mechanism

### Source-reported

The author describes a trend-following system in which an ATR envelope around an EMA identifies volatility expansion, a separate EMA confirms follow-through, and an independently timed ATR predictor supplies directional regime information. The v12 description also adds a batch-majority trend state and optional filters.

### Research interpretation

The falsifiable thesis is that an extreme move beyond a volatility-scaled EMA envelope can become a continuation signal when subsequent closes confirm direction, and that a slower multi-timeframe ATR-break regime can reduce counter-trend entries. The core alpha claim is therefore volatility-normalized directional persistence, not the stop-loss, sizing, or alert machinery.

The combined configuration is a hybrid:
- Primary signal: close beyond an EMA-centered ATR band, followed by directional Signal-EMA confirmation.
- Regime: multi-timeframe ATR Trend Predictor.
- Optional confirmation: EMA trend, ADX, weekend/session, volume, RSI and other gates.
- Risk / exit: percentage TP/SL, opposite ATR-band close, predictor flip, break-even, time stop, or warning-zone exits.

Whether the predictor or optional filters add incremental alpha must be tested by ablation rather than assumed.

## Signal

Source-reported standard band/EMA mode:
- Mid band: EMA of configurable length.
- Outer bands: mid band plus/minus ATR times a configurable multiplier.
- Long trigger: price closes below the lower ATR band, then must register a configured number of closes above a separate Signal EMA within a three-bar confirmation window.
- Short trigger: price closes above the upper ATR band, then must register the configured number of closes below the Signal EMA within the same confirmation window.
- The required confirmation closes are explicitly non-consecutive.
- Entry occurs once the confirmation condition is satisfied.

Source-reported v12 predictor:
- The ATR Trend Predictor runs on its own selectable timeframe (15m, 1H, 4H, 8H or 1D).
- Direction begins from a close beyond its upper/lower ATR band and uses configurable asymmetric grace-candle settings before flipping regime.
- Predictor mode trades flips directly; Combined mode allows either standard band/EMA entry or predictor-flip entry, whichever fires first.
- The ATR Batch Counter sets a trend state from the majority of bullish versus bearish closes in fixed batches of N candles, then resets.

Source-reported BTCUSD starting defaults on the v12 page:
- Combined mode.
- Mid-band EMA 15; ATR multiplier 1.0; Signal EMA 13.
- Required closes: long 8, short 4.
- TP 4%; percentage SL enabled at 7.5%; ATR-band SL disabled.
- Warning-zone exit #1 enabled at 10 consecutive closes.
- EMA50 trend filter enabled.
- ADX filter enabled.
- Weekend filter enabled, blocking Saturday only.
- ATR Trend Predictor enabled on 4H with grace settings 12/15 and used as a trade filter.

The public description does not unambiguously expose the ATR length used by every component, exact predictor band algebra, ADX threshold/default, precise warning-zone boundaries, same-bar ordering when multiple triggers/exits coincide, or all re-entry semantics. Those are underspecified and are not inferred here.

## Required data

Source-supported:
- BTCUSD is the bundled-default target; author states the strategy can be applied to other assets/timeframes.
- OHLCV sufficient for EMA, ATR, ADX, RSI, candle direction, volatility and volume filters.
- Multi-timeframe OHLC data when the predictor or higher-timeframe confirmation is enabled.
- Calendar/day-of-week and UTC/session timestamps for weekend/session filters.

Data gaps:
- The exact BTCUSD venue/feed and market type used for the tuned defaults are not identified in the reviewed description.
- Spot versus perpetual/futures contract semantics are therefore underspecified.
- Candle-boundary/timezone handling for higher-timeframe aggregation is not fully specified.
- No order-book, funding, open-interest or true aggressor-side data is required by the stated core rule. The optional “Volume Delta (Taker Ratio Proxy)” is explicitly a candle-derived proxy rather than true taker-flow data.

Point-in-time requirement: all multi-timeframe and filter inputs must use only information available at the decision timestamp; the public description does not independently establish a leakage-safe implementation.

## Execution assumptions

Source-reported strategy properties for the v12 BTCUSD starting configuration: initial capital 100,000; fixed cash order size 10,000; non-compounding; commission 0.05%; pyramiding 0; slippage 0.

Material gaps: market versus limit order behavior, signal-to-fill timestamp, same-bar fill ordering, spread, market impact, latency, partial fills, venue-specific fee tier, funding, leverage/margin and shorting mechanics are not fully specified. Slippage being configured as zero is a source setting, not evidence that real slippage is zero.

## Evidence

### Source-reported

The source describes the rules and BTCUSD starting defaults but does not provide a sufficiently traceable performance table on the reviewed v12 page to support a return, Sharpe, CAGR, drawdown, win-rate or profit-factor claim here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The author explicitly says the defaults are a starting point and should be re-tuned for each asset/timeframe. The default configuration includes zero slippage and an unspecified BTCUSD venue/market type, which weakens direct execution realism. The system also contains many optional filters and asymmetric tuned parameters, creating substantial specification-search and overfitting risk. No independent out-of-sample evidence was identified in the reviewed source.

## Falsification plan

1. Reconstruct only source-specified semantics; unresolved execution details must remain explicit research-proposed choices rather than silently inferred.
2. Use chronological train/validation/OOS splits and freeze all tuned parameters before the final OOS segment.
3. Compare the standard ATR-band + EMA-confirmation rule against simple EMA trend and ATR-breakout baselines.
4. Ablate the 4H predictor, EMA50 filter, ADX filter, weekend filter and warning-zone exit one at a time and jointly. The hybrid thesis is weakened if the full filter stack does not improve OOS risk-adjusted performance after costs relative to the simpler core.
5. Test both long and short legs separately because the source defaults use asymmetric confirmation counts and grace settings.
6. Run realistic fee, spread, slippage and funding sensitivity appropriate to the chosen crypto market.
7. Test multiple crypto venues and candle-boundary conventions to detect feed-specific dependence.
8. Treat any acceptance cutoff chosen during downstream research as a `research-defined falsification threshold`; none is asserted by this Scout.

## Crypto portability

direct

The source explicitly targets crypto and bundles BTCUSD defaults. Portability across crypto venues is nevertheless unproven because the reviewed source does not identify the exact BTCUSD feed/contract. Spot/perpetual differences, funding, 24/7 weekend liquidity, venue fragmentation, mark/index pricing and candle boundaries must be modeled when applicable.

## Limitations

- Protected source: normalized from the public TradingView description, not audited Pine source.
- Underspecified exact ATR lengths/algebra for all components and several optional-filter defaults.
- Data gap for exact venue, contract type, fill semantics, spread/slippage realism and funding.
- Many configurable filters increase researcher degrees of freedom.
- Source-reported BTCUSD defaults are tuned starting parameters, not validated alpha.
- Not independently reproduced.
- Profitability is unproven.

## Implementation status

Research-only. No implementation in the research stack has been completed. No Qlib full backtest, survivor promotion, Paper, Testnet or Live validation has occurred.

## Adoption boundary

This record is normalized external research only. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, is profitable or validated alpha, or is approved for implementation, Paper, Testnet or Live trading.

## Related Wiki records

No stable related Hermes Wiki Brain record is asserted by this GitHub-only Scout.

## Sources

- https://www.tradingview.com/script/G6jXOmkU-CryptoScopeAI-ATR-Bands-EMA-Trend-Predictor-LONG-SHORT/ — public TradingView v12 strategy page by `cryptoscopeai30`, reviewed 2026-09-27.
- https://www.tradingview.com/script/crTK0Gc3-CryptoScopeAI-Strategy-v11/ — public TradingView v11 predecessor/release-history page by `cryptoscopeai30`, reviewed 2026-09-27.
