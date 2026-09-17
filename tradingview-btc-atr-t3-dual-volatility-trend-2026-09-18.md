---
schema: strategy-research-record-v1
title: "TradingView BTC Dual-ATR T3 Trend-Following Strategy"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - https://www.tradingview.com/script/XUUH8oiL-ATR-and-T3-strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView BTC Dual-ATR T3 Trend-Following Strategy

## Provenance

Public TradingView open-source strategy **ATR and T3 strategy**, author `CryptoJoncis`, published 2018-09-08. Stable source URL: https://www.tradingview.com/script/XUUH8oiL-ATR-and-T3-strategy/ . Source reviewed as of 2026-09-18. The author identifies Bitcoin on the 12-hour timeframe as the preferred use case and states that other timeframes require settings adjustment.

GitHub dedup against current `main` found no record matching canonical TradingView source ID `XUUH8oiL`, author/source identity `CryptoJoncis`, or the normalized combination of dual ATR directional agreement with a Tillson T3 band breakout/exit.

## Economic mechanism

### Source-reported

The author describes T3 Moving Average as smoother than traditional moving averages and suitable for trending markets. The strategy combines two ATR-derived trend states with a Tillson T3 moving-average band. The stated intent is trend following with relatively low turnover, using agreement between the two ATR trend states to confirm direction and the T3 band to gate entries and exits.

### Research interpretation

The falsifiable hypothesis is that **agreement between two volatility-derived trend states reduces false T3-band breakouts**, while the smoother T3 band retains exposure to persistent Bitcoin trends. The components have separate roles:

- Regime / confirmation: both ATR trend states must agree on direction.
- Primary entry: bar close breaks beyond the corresponding T3 band.
- Exit: `hl2` crosses to the opposite side of the opposing T3 band.

The key empirical question is whether requiring dual-ATR agreement improves out-of-sample risk-adjusted performance or false-breakout behavior relative to a T3-band breakout alone after accounting for reduced trade count and realistic costs.

## Signal

Source-reported normalized logic:

- Preferred instrument / horizon: Bitcoin, 12-hour bars.
- Long entry: both ATR components are in uptrend and the bar closes above the **upper Tillson moving-average band**.
- Long exit: `hl2` is below the **lower Tillson moving-average band**.
- Short entry: both ATR components are in downtrend and the bar closes below the **lower Tillson moving-average band**.
- Short exit: `hl2` is above the **upper Tillson moving-average band**.
- The author characterizes the strategy as low-turnover trend following, approximately 6–10 trades per year; this is a source-reported characterization, not independently reproduced evidence.

The reviewed public description does not expose the exact two ATR formulas, ATR lookbacks/multipliers, T3 length, T3 volume factor, band-construction formula, re-entry rules, pyramiding behavior, position sizing, or whether exit comparisons require a confirmed close. Those details are **underspecified** and are not invented here.

## Required data

Minimum source-implied inputs are timestamped OHLC bars sufficient to calculate the two ATR trend states, Tillson T3 bands, bar close, and `hl2`. The preferred source-reported configuration is Bitcoin on 12-hour bars. Venue and market type (spot, perpetual, futures) are **underspecified**.

Point-in-time construction must use only information available by the signal timestamp. Candle boundary and timezone must be fixed before reproduction because Bitcoin trades continuously and 12-hour bars can differ by venue or data vendor.

## Execution assumptions

The entry description explicitly refers to the **bar closing** beyond the T3 band, so a leakage-safe implementation must not assume that confirmation was known before that close. Exact signal-to-order timing is not stated. `research-proposed`: if the public Pine source does not establish another causal order, execute confirmed close-based entries no earlier than the next tradable bar/event.

Order type, fill model, spread, fees, slippage, market impact, latency, partial fills, leverage, margin, borrow/shorting, funding and liquidation mechanics are not specified by the reviewed source. These must be modeled explicitly for later testing, particularly if implemented on Bitcoin perpetuals.

## Evidence

### Source-reported

The author states that the preferred configuration is Bitcoin on 12H and characterizes the system as suitable for patient trend followers with roughly 6–10 trades per year. The source description does not provide a traceable Sharpe ratio, CAGR, drawdown, win rate or other quantitative performance statistic that is safe to carry into this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The reviewed source does not provide independent evidence that dual-ATR confirmation adds value over the T3 breakout alone. The strategy is explicitly trend-following, so range-bound or rapidly reversing regimes are a plausible failure environment to test rather than assume away. Parameter definitions needed for exact reproduction are incomplete in the reviewed prose. No additional negative empirical evidence was identified in the reviewed source; absence is not evidence of robustness.

## Falsification plan

1. Recover exact ATR and T3/band definitions from the public Pine source before claiming exact reproduction; otherwise retain unresolved values as `underspecified` or explicitly `research-proposed`.
2. Primary ablation: compare the full `dual ATR agreement + T3 breakout` rule against the same T3 entry/exit without ATR confirmation.
3. Secondary ablation: compare one ATR confirmation versus two to test whether the second volatility state adds incremental information.
4. Evaluate Bitcoin 12H first because that is the source-reported preferred configuration, then test neighboring horizons without optimizing broadly after observing results.
5. Require chronological out-of-sample testing across bull, bear, high-volatility range and low-volatility range regimes.
6. Stress fees, spread and slippage; include funding and mark/index conventions for perpetual implementations.
7. The core hypothesis is materially weakened if dual-ATR agreement fails to improve out-of-sample risk-adjusted return, drawdown, or false-breakout behavior versus the simpler T3 baseline after accounting for reduced trade count.

## Crypto portability

`direct`. The cited source explicitly identifies Bitcoin as the preferred use case and recommends the 12-hour timeframe.

Implementation remains market-structure dependent: spot cannot natively execute the short leg without borrowing or derivatives; perpetuals add funding and liquidation mechanics; 24/7 candle boundaries must be standardized; and liquidity/slippage assumptions depend on venue and order size.

## Limitations

- Exact ATR formulas, lengths and multipliers are **underspecified** in the reviewed public description.
- Exact Tillson T3 parameters and upper/lower band construction are **underspecified**.
- Venue and market type are **underspecified**.
- Entry fill timing and exit confirmation semantics are **underspecified**.
- Position sizing, leverage, pyramiding and re-entry behavior are **underspecified**.
- The source-reported low trade frequency has not been independently reproduced.
- Not independently reproduced.

## Implementation status

`not-implemented`.

No implementation or backtest in the user's quantitative research stack was performed in this Scout cycle.

## Adoption boundary

Research material only. Presence in this repository does not imply profitable alpha, successful validation, implementation approval, paper/testnet/live approval, or authorization to trade.

## Related Wiki records

No Hermes Wiki Brain record was consulted or fabricated in this GitHub-only Scout cycle.

## Sources

- TradingView — `CryptoJoncis`, **ATR and T3 strategy**: https://www.tradingview.com/script/XUUH8oiL-ATR-and-T3-strategy/ (published 2018-09-08; public open-source strategy page; reviewed 2026-09-18).
