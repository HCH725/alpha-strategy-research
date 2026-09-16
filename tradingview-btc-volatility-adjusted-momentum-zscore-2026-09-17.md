---
schema: strategy-research-record-v1
title: "TradingView BTC Volatility-Adjusted Momentum Z-Score Regime"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-17
sources:
  - https://www.tradingview.com/script/WGWJ1Qzl-DurdenBTCs-Dual-Signal-Trend-Sentinel/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView BTC Volatility-Adjusted Momentum Z-Score Regime

## Provenance

Public TradingView protected-source strategy page: **DurdenBTCs Dual Signal Trend Sentinel**, by **DurdensBitcoinLedger**. The page shows an initial publication dated January 15 and updates dated January 18 and January 19; the reviewed public page was accessed/as-of 2026-09-17. The source code is protected, so this record normalizes only rules and claims exposed on the public TradingView page and does not reproduce Pine code.

Stable source URL: https://www.tradingview.com/script/WGWJ1Qzl-DurdenBTCs-Dual-Signal-Trend-Sentinel/

## Economic mechanism

### Source-reported

The author describes the strategy as a Bitcoin-specific Volatility Adjusted Momentum (VAMS) system intended to reduce the whipsaw associated with ordinary moving-average crossovers. The stated idea is to measure price displacement from a 63-period trend baseline in standard-deviation units and classify the market into bullish, bearish, and neutral regimes. The author characterizes the 63-period lookback as approximately a quarterly cycle for Bitcoin.

### Research interpretation

The falsifiable hypothesis is that **volatility-normalized distance from a medium-horizon BTC trend baseline contains more persistent directional information than raw distance from that baseline**. Standardizing displacement by contemporaneous dispersion may make the trigger adaptive across changing volatility regimes: a +0.5 standardized displacement is intended to represent comparable trend strength when absolute BTC volatility is high or low.

The source's claim that 63 periods correspond to quarterly flows is a rationale, not established evidence. Whether 63 observations actually represent a quarterly horizon depends on chart timeframe, which the reviewed page does not specify.

## Signal

Source-reported normalized logic:

- Universe: Bitcoin.
- Lookback: 63 periods for the trend baseline and associated dispersion calculation.
- Volatility adjustment: standard deviation of price around the baseline.
- State variable: a VAMS/Z-score representing price distance from the baseline in standard-deviation units.
- Bullish regime: VAMS/Z-score > +0.5.
- Long entry: enter long when the strategy enters the bullish regime.
- Bearish regime: VAMS/Z-score < -0.5.
- Exit: close all positions when the strategy enters the bearish regime.
- Neutral regime: -0.5 <= VAMS/Z-score <= +0.5; the source describes this as a noise zone and says behavior there can be customized.
- Directionality: the publicly described core is long/flat; no source-reported short entry rule is exposed on the reviewed page.
- Holding behavior: remain in the position until the bearish close-all condition, subject to any neutral-zone customization.
- Confirmation: later release notes distinguish pending versus confirmed signals, display the date a signal last changed, warn when a live-bar signal is changing, and provide alerts on confirmed signal changes.

**Underspecified:** the reviewed public description does not expose the exact mathematical definition/type of the 63-period trend baseline; the formula rendered on the page is not available as reconstructable text. It also does not unambiguously specify chart timeframe, price input, standard-deviation convention, exact bar-close/confirmation implementation, neutral-zone default behavior, same-bar re-entry behavior, or whether any additional implementation details exist inside the protected source.

Research-proposed operationalization for later testing, not source-reported: compare causal variants using a 63-bar SMA and 63-bar EMA baseline separately, with rolling standard deviation computed only from information available through the completed signal bar. Do not select the better baseline ex post without nested/OOS control.

## Required data

Source-reported requirements visible from the public description are Bitcoin price history sufficient to form a 63-period baseline and standard deviation.

For a reproducible research implementation, point-in-time OHLC data with explicit venue, market type, timeframe, candle boundary/timezone, and missing-bar policy would be required. The reviewed source does not specify whether its intended BTC instrument is spot, perpetual, futures, or a particular venue, nor does it expose the chart timeframe used for the stated results.

## Execution assumptions

The source describes entering on a bullish regime and closing all on a bearish regime, but does not specify order type, next-bar versus same-bar fill, spread, slippage, market impact, leverage/margin, funding, partial fills, or venue-specific fees.

The release notes' distinction between live-bar pending signals and confirmed signal changes suggests that confirmation timing matters materially. A later implementation must prevent intrabar state changes from being treated as historical confirmed signals unless that behavior is explicitly reproduced and point-in-time safe.

## Evidence

### Source-reported

The January 18 release notes state that a separate Python backtest using a separate dataset independently confirmed the TradingView results for 2014-2026 and report CAGR 65.92%, maximum drawdown 26.79%, profit factor 3.26, and win rate 47%. The same source claims performance approximately twice buy-and-hold.

These are **author-reported figures from the TradingView page**, not results reproduced by this Scout. The public page does not expose enough dataset, venue, timeframe, fee/slippage, benchmark-construction, or Python methodology detail in the reviewed description to independently audit those figures.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independent negative study was identified in the reviewed source. The source itself warns that past performance does not guarantee future results and notes that the win rate is 47%. More importantly for research validity, the public page omits several implementation and cost assumptions needed to determine whether the reported backtest is reproducible.

## Falsification plan

1. Reconstruct the signal causally on BTC using predeclared baseline variants necessitated by the source ambiguity; do not choose a variant based on full-sample performance.
2. Test multiple liquid BTC market representations (at minimum a major spot series and a major perpetual series) with explicit candle boundaries and point-in-time data.
3. Compare against simple controls: BTC buy-and-hold, a 63-bar baseline long/flat rule without volatility normalization, and a raw 63-bar momentum rule.
4. Ablate the volatility normalization. The VAMS thesis is weakened if the z-score version does not improve OOS risk-adjusted behavior or regime robustness versus the unnormalized trend control after costs.
5. Test the +0.5/-0.5 thresholds on untouched OOS periods and across volatility regimes rather than optimizing them on the full history.
6. Include realistic fees, spread/slippage, and perpetual funding where applicable.
7. Explicitly test confirmed-bar versus intrabar signal formation. Reject any apparent advantage that depends on information unavailable at the declared decision timestamp.
8. Treat failure to reproduce the source-reported performance as evidence against the published implementation claim, while separately judging whether the normalized hypothesis retains incremental OOS value.

## Crypto portability

**direct**

The source explicitly presents the strategy as Bitcoin-specific. Portability is therefore direct for the BTC hypothesis, but not automatically for other crypto assets. Venue fragmentation, spot-versus-perpetual differences, funding, 24/7 candle boundaries, and the unspecified chart timeframe can materially alter the 63-period interpretation and signal turnover.

## Limitations

- Protected-source implementation: normalized from the public description only.
- Exact 63-period baseline formula/type: **underspecified**.
- Chart timeframe and intended BTC venue/market type: **underspecified**.
- Confirmation/bar timing: partially described but exact implementation **underspecified**.
- Neutral-zone default behavior and re-entry details: **underspecified**.
- Trading costs and execution model behind the reported statistics: **data gap**.
- Source-reported backtest: **not independently reproduced**.
- The 63-period "quarterly flow" interpretation is **unproven** without a specified timeframe.

## Implementation status

No implementation in the research stack has been completed. No PyBroker or other formal backtest was run by this Scout.

## Adoption boundary

Research material only. Presence in this repository does not imply profitability, validated alpha, implementation approval, paper/testnet approval, or live-trading approval.

## Related Wiki records

None linked; no stable Hermes Wiki Brain page was established from GitHub-visible information in this run.

## Sources

- TradingView — DurdensBitcoinLedger, **DurdenBTCs Dual Signal Trend Sentinel**: https://www.tradingview.com/script/WGWJ1Qzl-DurdenBTCs-Dual-Signal-Trend-Sentinel/ (public page; initial publication shown as Jan 15, updates Jan 18 and Jan 19; accessed/as-of 2026-09-17).
