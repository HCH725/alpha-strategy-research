---
schema: strategy-research-record-v1
title: "BTC Perpetual Multi-Confluence Signal with Pseudo-Derivatives Proxy Source-Code Audit"
created: 2026-09-15
updated: 2026-09-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - crypto
  - perpetual-futures
  - confluence
  - source-code-audit
status: research-only
confidence: low
source_as_of: 2026-09-15
sources:
  - "https://www.tradingview.com/script/SRokfUaf-BTC-Perp-Strategy-Long-Short-Signals/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The TradingView page and Pine header advertise an OI Proxy, but the reviewed 259-line Pine source contains no open-interest input, request, calculation, or scoring component; the six scored components are EMA regime, RSI divergence, liquidity sweep, candle-signed volume proxy, VWAP cross, and a price-deviation proxy."
  - "The source labels close minus its 14-bar SMA, standardized by the rolling standard deviation of that deviation, as a Funding Rate Proxy; it does not use funding-rate, mark-price, index-price, spot-perpetual basis, or premium-index data."
  - "The source labels a 20-bar average of whole-bar volume signed only by close-versus-open direction as CVD/Volume Delta; it does not use aggressor-side buy/sell volume or true cumulative volume delta."
---

# BTC Perpetual Multi-Confluence Signal with Pseudo-Derivatives Proxy Source-Code Audit

## Provenance

- **Primary source:** `skullopener`, **BTC Perp Strategy Long/Short Signals**, public TradingView open-source Pine Script v6 indicator.
- **Stable public URL:** https://www.tradingview.com/script/SRokfUaf-BTC-Perp-Strategy-Long-Short-Signals/
- **Publication information:** TradingView displays `Mar 30` on the public page as reviewed 2026-09-15; no additional publication timestamp is asserted here beyond what the page exposes.
- **Source inspection:** the public description and complete current 259-line Pine source were inspected directly on 2026-09-15. This record normalizes the logic and does not reproduce the Pine script.
- **Deduplication:** repository and Hermes Wiki Brain searches found no record for TradingView identity `SRokfUaf`, author `skullopener`, or the same six-vote confluence construction. Adjacent records study genuine funding, open interest, order flow, CVD, VWAP, and liquidity sweeps using materially different data and mechanisms.
- **Incremental value:** the main contribution is negative/source-integrity evidence. Three advertised derivatives/order-flow concepts are absent or materially weaker proxies in the executable source: OI is absent, funding is own-price mean deviation, and volume delta is candle-direction-signed total volume.

## Economic mechanism

### Source-reported

The publication presents a BTC perpetual entry indicator that combines multiple forms of confirmation: RSI divergence, VWAP reclaim, liquidity sweep, OI proxy, funding-rate proxy, volume delta, and EMA regime filtering. The intended premise is that a directional entry is more credible when independent trend, reversal, crowding, liquidity, and flow signals agree.

### Research interpretation

The falsifiable hypothesis in the actual source is narrower. A **majority vote among six OHLCV-derived conditions** may identify bars where trend state, local rejection, momentum non-confirmation, VWAP crossing, signed-volume direction, and standardized price displacement align. However, the implementation does not supply genuine OI or funding information and does not measure true trade-side volume delta. Therefore any apparent edge must be attributed to the observable OHLCV transforms actually used, not to derivatives-positioning or funding-crowding information.

The source-integrity question is itself testable: if replacing the pseudo-derivatives proxies with genuine point-in-time OI, funding/premium, and aggressor-side delta materially changes signal quality, then the advertised mechanism is not equivalent to the current Pine implementation.

## Signal

**Specification status: entry-event logic is reconstructable; executable strategy lifecycle is underspecified.** The source is `indicator()`, not `strategy()`, and defines no position exit, sizing, order type, cost model, or holding period.

### Source-code-defined inputs and components

Default parameters in the reviewed source:

- EMA regime length: `200`; display-only fast EMA: `50`.
- RSI length: `14`; overbought `70`; oversold `30`; divergence lookback `20` bars.
- VWAP source: `hlc3` using TradingView `ta.vwap`.
- Liquidity-sweep lookback: `10` bars; minimum wick/body ratio `1.5`.
- Price-deviation proxy lookback: `14` bars; extreme threshold `2.0 ×` rolling standard deviation.
- Minimum confluence score: `3` of `6`.

The six long votes are:

1. **Regime:** `close > EMA(200)`.
2. **RSI divergence proxy:** current low is below the minimum low of the prior 20 bars, current RSI is above the minimum RSI of the prior 20 bars, and current RSI is below `45`.
3. **Liquidity sweep:** current low breaks the prior 10-bar low, closes back above that level, and lower wick is greater than `1.5 ×` candle body.
4. **CVD proxy:** current close is below close 20 bars ago while the 20-bar SMA of candle-signed whole-bar volume is positive, where each bar contributes `+volume` if `close >= open`, otherwise `-volume`.
5. **VWAP reclaim:** close crosses above session/chart VWAP.
6. **Funding proxy:** `close - SMA(close,14)` is below `-2 × stdev(close - SMA(close,14),14)`.

Short votes mirror the six conditions.

**Long signal:** `long_score >= 3` and `short_score < 3`.

**Short signal:** `short_score >= 3` and `long_score < 3`.

The signal is plotted and exposed via `alertcondition`. The reviewed expressions are not gated by `barstate.isconfirmed`, so realtime/intrabar signal stability is **underspecified** unless alert frequency is fixed to bar close.

### Material source-code audit findings

- **No OI component exists.** Despite the page/header advertising `OI Proxy`, the reviewed source contains no open-interest series or OI-derived vote. The score contains exactly six components listed above.
- **“Funding Rate Proxy” is not funding or basis.** It is standardized deviation of the same chart close from its 14-bar SMA. No funding, premium index, mark price, index price, or spot-perpetual pair is queried.
- **“CVD Proxy” is not true CVD.** The entire bar volume receives one sign from candle direction, then is averaged. No aggressor-side trade classification or buy/sell volume decomposition is used.
- The displayed 50 EMA does not contribute a seventh vote; regime direction is determined by close versus EMA200.

### Holding / exit / rebalance

The source does not define a trade lifecycle. There is no source-defined exit, stop, take profit, maximum holding period, rebalance rule, pyramiding behavior, overlap policy, or position sizing. Those fields are `underspecified` and must not be inferred from plotted entry labels.

Any later conversion from these entry events into trades is **research-proposed**, not source-reported.

## Required data

### Current source parity

- Chart OHLCV and timestamps.
- Sufficient history for EMA200 and rolling 20-bar calculations.
- TradingView VWAP/session semantics for the selected symbol and timeframe.
- No actual OI, funding, mark/index price, spot-perpetual basis, or aggressor-side volume data is required by the current Pine source.

### Genuine-derivatives audit extension

A separately labeled `research-proposed` test would require point-in-time:

- perpetual open interest;
- actual funding rate and settlement interval;
- mark/index or premium-index series, or synchronized spot/perpetual prices;
- aggressor-side buy/sell volume or trade-level data for genuine volume delta;
- exact exchange timestamps and symbol mapping.

These additional fields are not source parity and must not be silently substituted into a reproduction.

### Point-in-time constraints

All rolling extrema and oscillators must use only bars available through the evaluation time. For a conservative historical event study, treat an entry signal as known only after the chart bar has completed. A realtime study must separately measure intrabar signal flicker because the source does not require confirmed bars.

## Execution assumptions

The source is an indicator and supplies no broker-emulator execution assumptions.

`underspecified`: order type, signal-to-fill delay, spread, commission, slippage, market impact, participation limit, leverage, margin, liquidation, funding payments, partial fills, latency, and venue-failure behavior.

For later testing, a conservative **research-proposed** mapping should enter no earlier than the next executable event after a completed signal bar and apply explicit exchange-specific costs. Perpetual funding must be modeled for any holding interval that crosses funding settlements. None of this is source-reported.

## Evidence

### Source-reported

The public TradingView page identifies the indicator as a BTC perpetual multi-confluence entry framework and lists RSI divergence, VWAP reclaim, liquidity sweep, OI proxy, funding-rate proxy, volume delta, and EMA regime filtering as its components. The public Pine source supplies the exact six-vote score, default thresholds, and alert logic described above.

The reviewed source provides **no Sharpe ratio, CAGR, profit factor, drawdown, win rate, transaction-cost result, walk-forward study, frozen out-of-sample result, or independently validated performance series**. No profitability claim is accepted as evidence.

### Independently reproduced

not independently reproduced

### Negative evidence

1. **Advertised OI is absent:** no OI data or OI-derived calculation appears in the reviewed scoring logic.
2. **Funding-label mismatch:** standardized close-versus-SMA deviation is a price-extremeness transform, not a funding-rate measurement and not a spot-perpetual basis measurement.
3. **CVD-label mismatch:** signing the entirety of bar volume by candle direction can diverge materially from true aggressor-side delta, especially on bars with substantial two-way trading.
4. **Potential pseudo-diversification:** several votes derive from the same OHLCV information and may be strongly correlated. A 3-of-6 score should not be interpreted as six independent evidence sources.
5. **No confirmed-bar gate on final alerts:** historical close-state signals do not establish that unrestricted realtime alerts are stable intrabar.
6. **No executable lifecycle:** there is no source-defined exit or cost model, so the indicator cannot support a strategy-level return claim without additional research assumptions.
7. **Publication-selection risk:** a public TradingView indicator is a hypothesis source, not controlled OOS evidence.

## Falsification plan

All protocols below are `research-proposed`; thresholds are `research-defined falsification threshold` values.

1. **Source-parity event reconstruction.** Reproduce every six component boolean and final score on frozen TradingView-equivalent OHLCV for BTCUSDT. Require exact completed-bar signal agreement after warm-up. Any systematic disagreement invalidates subsequent testing until resolved.

2. **Confluence-ablation test.** Evaluate each component alone and leave-one-component-out variants using identical chronological samples and next-bar execution. Reject the “confluence adds value” hypothesis if the 3-of-6 rule fails to improve median OOS net Sharpe by at least `0.15` over the best prespecified single component or fails to reduce max drawdown by at least `10%` relative.

3. **True-OI substitution audit.** Replace the nonexistent advertised OI concept with a separately labeled genuine OI feature, without changing the original source-parity result. Reject the claim that current source signals encode meaningful OI information if conditioning on true OI changes forward-return ordering materially while source scores have negligible correlation with true OI changes.

4. **Funding-proxy validity test.** Compare the source price-deviation vote with actual point-in-time funding and premium/basis extremes. Reject the funding interpretation if absolute rank correlation with genuine funding/premium is `< 0.20` and genuine funding conditioning produces materially different signal outcomes.

5. **CVD-proxy validity test.** Compare candle-signed total volume with genuine aggressor-side cumulative delta on trade data. Reject the CVD interpretation if sign agreement is `< 60%` or if genuine delta divergence and the proxy produce non-overlapping forward-return effects.

6. **Realtime stability test.** Reconstruct lower-timeframe/tick evolution inside each chart bar and record provisional versus completed-bar signals. Reject unrestricted realtime use if more than `5%` of provisional alerts disappear before bar close; thereafter require bar-close-only handling.

7. **Cost and execution stress.** Apply maker/taker fees, observed spread, 5/10/20 bps round-trip slippage stress, and actual perpetual funding. Reject practical tradability if median OOS net Sharpe is `<= 0` at 10 bps round-trip friction before funding.

8. **Cross-venue/regime stability.** Test BTC and ETH perpetuals on at least two liquid venues across high/low volatility and bull/bear regimes. Reject broad portability if after-cost positive expectancy is confined to one venue or one narrow regime.

If the source-parity signal fails predictive, robustness, or cost gates, retain this record as negative/source-integrity evidence rather than retuning after observing OOS results.

## Crypto portability

**direct in intended market, but empirically unproven.** The publication explicitly targets BTC perpetual trading. Mechanical portability to other crypto pairs is straightforward for the OHLCV-only source, but that does not establish economic portability.

Material risks include venue-specific VWAP/session semantics, 24/7 candle boundaries, fragmented volume, stablecoin quote differences, perpetual funding and liquidation mechanics omitted by the source, and the mismatch between OHLCV-derived proxies and genuine derivatives/order-flow data.

## Limitations

- `contested`: advertised component names materially overstate the data used by the current source.
- `not independently reproduced`.
- `underspecified`: no exit, holding rule, sizing, order type, or execution-cost model.
- no genuine OI input despite advertised OI Proxy.
- no genuine funding/basis input despite Funding Rate Proxy label.
- no aggressor-side volume data despite CVD/Volume Delta label.
- no source-reported OOS, walk-forward, cross-venue, or capacity evidence.
- final signal/alert expressions are not confirmed-bar-gated.
- equal-weight vote counts can hide strong dependence among OHLCV-derived components.

## Implementation status

`not-implemented`. No quantitative runtime change, strategy implementation, backtest, Paper, Testnet, or Live activity was created or executed in this Scout cycle.

## Adoption boundary

This staging artifact is `research-only`; `adoption: not-approved`; `approval_scope: research-only`.

It records a falsifiable TradingView hypothesis and source-code integrity audit. It is not evidence of validated profitability and does not authorize implementation or trading.

## Related Wiki records

No exact Hermes Wiki Brain record matching TradingView source `SRokfUaf`, author `skullopener`, or this six-vote construction was found in the pre-write search. Existing Wiki records using genuine funding, OI, or order-flow data are materially different and should serve as comparators rather than duplicates.

## Sources

1. `skullopener`, **BTC Perp Strategy Long/Short Signals**, TradingView public open-source Pine Script v6 indicator; public page and complete current 259-line source reviewed 2026-09-15. https://www.tradingview.com/script/SRokfUaf-BTC-Perp-Strategy-Long-Short-Signals/
