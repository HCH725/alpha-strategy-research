---
schema: strategy-research-record-v1
title: Binance perpetual OI-premium divergence regime veto filter
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-19
sources:
  - https://www.tradingview.com/script/GW7YDJ9o/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Binance perpetual OI-premium divergence regime veto filter

## Provenance

Public TradingView open-source indicator **Crypto Derivatives Dashboard v1**, author `ngenise`. Stable source URL: https://www.tradingview.com/script/GW7YDJ9o/. The page displays publication date `Mar 5`; the year is not stated in the reviewed page text, so it is not inferred here. Source reviewed 2026-09-19.

The source is explicitly an indicator/context layer rather than a self-contained entry/exit strategy. This record therefore preserves it as a falsifiable **veto-filter alpha hypothesis**, not as a complete trading system.

## Economic mechanism

### Source-reported

The source characterizes combinations of perpetual price and open-interest direction as derivatives-market regimes. Rising price with rising OI is described as a healthy trend; rising price with falling OI as short-covering/exhaustion; falling price with rising OI as shorts building; and falling price with falling OI as long liquidation. It also treats extreme positive premium-index z-scores as crowded-long risk, extreme negative values as potential short-squeeze context, and disagreement between normalized OI and price momentum as structural divergence.

The source explicitly proposes these measures as a veto/confirmation layer for another strategy rather than as standalone entry and exit signals.

### Research interpretation

Hypothesis: a long-side primary signal may have better conditional forward-return economics when Binance perpetual participation confirms the move — OI and price trends are both positive — while premium is not extremely positive and no bearish OI/price divergence is active. Conversely, signals occurring during short-covering, liquidation, shorts-building, crowded-long, or bearish-divergence states may have weaker conditional expectancy.

Potential mechanism: OI expansion during price appreciation can proxy fresh leveraged participation rather than position closure, while extreme premium can proxy crowded positioning vulnerable to reversal. These interpretations are hypotheses, not independently established facts.

Component roles:

- Regime: joint OI-trend and price-trend state.
- Crowding filter: Binance premium-index z-score.
- Confirmation/veto: OI-versus-price normalized ROC divergence.
- Output: GO/WAIT contextual flag for an external long signal.

The incremental value of each component must be tested by ablation; indicator stacking alone is not evidence of alpha.

## Signal

Source-reported normalized logic:

- Supported asset selector: BTC, ETH, SOL, BNB, XRP, PEPE, mapped to Binance USDT perpetual data; the source notes special ticker construction for PEPE.
- OI change lookback default: 14.
- OI z-score uses SMA length 20 by default.
- OI rate of change uses a configurable lookback.
- Premium index is requested at 1H resolution and normalized with a default z-score lookback of 50.
- Premium extreme thresholds: +2.0 and -2.0 by default.
- Divergence compares normalized ROC of OI and price; default divergence z-score threshold is 1.5.
- Bearish divergence: price rises while OI does not confirm.
- Bullish divergence: OI rises faster than price.
- Regime states are classified from OI trend versus price trend.
- Long-side `GO` occurs only when the regime is healthy, funding/premium is not extreme, and no bearish divergence is active; otherwise the indicator is used as a wait/veto context.
- Source says the indicator is optimized for D1, though it can operate on other timeframes.

Underspecified from the reviewed public description:

- exact formulas and smoothing used to define OI trend and price trend;
- exact normalization formula for OI-versus-price ROC divergence;
- exact Boolean treatment of negative premium extremes inside the `GO` rule;
- signal formation/finality semantics when the chart timeframe differs from the 1H premium series;
- re-entry/cooldown behavior;
- any complete primary entry, exit, holding-period, sizing, or short-side trading rule.

No missing rule is filled in by this Scout.

## Required data

Source-reported data dependencies:

- Venue: Binance.
- Market type: USDT perpetuals.
- Instruments: BTC, ETH, SOL, BNB, XRP, PEPE as supported by the source.
- Price: `BINANCE:{ASSET}USDT.P` perpetual close.
- Open interest: `BINANCE:{ASSET}USDT.P_OI`.
- Premium proxy: `BINANCE:{ASSET}USDT_PREMIUM`, requested at 1H resolution.
- Timeframe: source says D1 is the optimized context; other chart timeframes are permitted.

Point-in-time requirement: all OI, price, and premium observations used for a decision must have been finalized and available at the decision timestamp. Higher/lower-timeframe alignment must not leak unfinished 1H premium bars or future D1 information.

The source explicitly states that the premium index is a funding proxy, not exact funding, and that its implementation is Binance-only rather than cross-exchange aggregated.

## Execution assumptions

The source does not define a complete executable strategy. It explicitly positions the output as a veto filter used alongside another primary strategy.

Therefore the following are underspecified: signal-to-order delay, market versus limit orders, fill model, fees, spread, slippage, impact/capacity, actual funding cash flows, leverage/margin, partial fills, and the primary strategy's exits and sizing.

For later research, the veto state must be computed using only information available before the primary strategy's order decision. Any execution model belongs to the primary strategy under test and must be held identical between filtered and unfiltered controls.

## Evidence

### Source-reported

The reviewed TradingView description provides the indicator construction, default parameters, supported Binance perpetual assets, regime labels, and intended GO/WAIT use. It does not provide a traceable backtest with Sharpe, CAGR, drawdown, win rate, or conditional forward-return statistics for the veto filter. No profitability claim is recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself identifies several limitations: Binance-only derivatives data, premium index as a proxy rather than exact funding, absence of native funding-rate/long-short-ratio/liquidation/taker-volume series in this implementation, and lag from smoothed regime classification near turning points.

No independent negative empirical result was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

Test the filter only as an overlay on one or more fixed primary long strategies; do not tune the primary strategy jointly with the filter.

1. Baseline: execute every primary long signal with identical execution and risk rules.
2. Full filter: accept only signals satisfying the source-defined healthy-regime + non-extreme-premium + no-bearish-divergence condition.
3. Ablations: OI/price regime only; premium only; divergence only; and leave-one-component-out variants.
4. Measure conditional forward returns, trade expectancy, Sharpe, drawdown, hit rate, turnover, opportunity loss, and net results after identical costs.
5. Evaluate BTC/ETH separately from smaller supported perpetuals and require out-of-sample persistence across multiple market regimes.
6. Test threshold stability around the source defaults rather than selecting a single ex-post optimum.
7. Compare premium proxy against exact historical funding where point-in-time exact funding data is available; failure of the proxy to preserve the effect weakens the mechanism.
8. Audit multi-timeframe timestamp alignment explicitly, especially D1 decisions using 1H premium observations.

The hypothesis is materially weakened if the full veto does not improve risk-adjusted or net conditional expectancy over the unfiltered primary strategy out of sample, if improvement disappears after realistic costs/opportunity loss, or if ablations show that the composite adds no stable incremental information.

## Crypto portability

`direct`

The cited source itself is built for Binance crypto perpetuals and names BTC, ETH, SOL, BNB, XRP, and PEPE. Portability beyond Binance is unproven because OI construction, premium/funding conventions, liquidity, contract specifications, candle boundaries, and positioning can differ across venues.

## Limitations

- Not independently reproduced.
- No standalone entry/exit strategy is supplied; this is a contextual veto hypothesis.
- Exact trend and divergence formulas are underspecified in the reviewed public description.
- Premium index is not exact funding.
- Binance-only positioning may not represent aggregate crypto derivatives positioning.
- Smoothed state variables may lag reversals.
- Multi-timeframe alignment can create look-ahead bias if reconstructed incorrectly.
- Default thresholds may reflect source selection and require out-of-sample stability testing.

## Implementation status

Research-only. No implementation or backtest in our research stack has been completed. No PyBroker, Nautilus, paper, testnet, or live verification is claimed.

## Adoption boundary

This record is normalized external research material only. It is not evidence that the filter is profitable or validated alpha and is not approval for implementation, paper trading, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted from this GitHub-only Scout run.

## Sources

- TradingView — `ngenise`, **Crypto Derivatives Dashboard v1**: https://www.tradingview.com/script/GW7YDJ9o/ — reviewed 2026-09-19.
