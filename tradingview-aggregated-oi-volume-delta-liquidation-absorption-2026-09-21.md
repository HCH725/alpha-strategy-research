---
schema: strategy-research-record-v1
title: Aggregated OI + Volume-Delta Liquidation and Absorption Events
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
  - https://www.tradingview.com/script/ZpFcfJy3-Aggregated-Open-interest-Volume-Delta/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Aggregated OI + Volume-Delta Liquidation and Absorption Events

## Provenance

Public TradingView open-source script **Aggregated Open interest + Volume Delta**, by **AghaInvst**, published Feb 9 and reviewed as of 2026-09-21. Canonical source: https://www.tradingview.com/script/ZpFcfJy3-Aggregated-Open-interest-Volume-Delta/ . The source aggregates Binance and Bybit perpetual open interest and combines significant OI changes with volume delta for positioning classification.

## Economic mechanism
### Source-reported

The author argues that open-interest direction identifies whether positions are being added or removed, while volume delta is preferable to candle color for classifying the side responsible for a significant positioning event. The source labels large OI increases as aggressive positioning, large OI decreases as position unwinds, detects two-or-more-bar large-OI-decrease sequences as liquidation cascades, and describes large OI increases with small candle bodies as absorption.

### Research interpretation

The falsifiable hypothesis is that **joint OI shock + signed volume-flow state contains incremental information about subsequent returns or volatility beyond price direction and OI change alone**. A large OI decrease paired with delta may distinguish long versus short forced unwind; sequential large decreases may identify deleveraging cascades whose post-event behavior can be tested for continuation versus exhaustion reversal. Separately, large OI additions with unusually small price displacement may represent absorption: substantial positioning flow that fails to move price, potentially preceding either defended-level reversal or delayed breakout.

These are competing hypotheses, not assumed trading facts.

## Signal

Source-supported components:

- Aggregate OI OHLC from Binance USDT/USD perpetuals and Bybit USDT/USD perpetuals.
- Per-bar OI delta: OI close minus OI open.
- Adaptive significance threshold based on an SMA window; source default lookback is **300 bars** and threshold multiplier is **5.0**.
- Significant-event classes: Aggressive Longs, Aggressive Shorts, Rekt Longs, Rekt Shorts, using OI direction plus volume delta rather than candle direction.
- Liquidation cascade: at least **2 consecutive bars** with large OI decrease.
- Absorption: large OI increase with a small candle body.
- Source suggests 5m, 15m, 1H and 4H as useful timeframes and exposes a configurable source-selection set.

The exact volume-delta construction and exact mathematical definition of the adaptive OI threshold / small-body absorption condition are not fully specified in the reviewed descriptive text; they are **underspecified** here rather than inferred.

Research-proposed operationalization for testing, not source-reported trading rules:

1. Reconstruct OI-shock events using only information available at each bar close.
2. Classify event side with a reproducible signed-volume-delta definition; compare against candle-color classification as a baseline.
3. Test event-time forward returns and realized volatility after isolated OI shocks, 2+ bar OI-decrease cascades, and absorption states over multiple fixed horizons.
4. Test both continuation and reversal outcomes rather than hard-coding either direction.
5. No source-supported entry, exit, holding period, re-entry rule, stop, take-profit or position sizing was identified; all such choices remain research-proposed.

## Required data

- Crypto perpetual futures for the tested base asset.
- Point-in-time Binance and Bybit perpetual OI series, with contract/quote denomination handled consistently.
- OHLCV at the tested timeframe.
- A reproducible volume-delta series; if true aggressor-side trades are unavailable and delta is estimated from bars/lower-timeframe data, that limitation must be explicit.
- UTC-normalized timestamps and synchronized venue bars.
- Venue listings and symbol mappings as they existed at each historical timestamp.
- Missing OI observations must not be silently forward-filled across outages or listing gaps.

## Execution assumptions

The TradingView source is an analytical indicator, not a fully specified executable strategy. It does not provide a complete signal-to-order model, order type, fill model, fees, spread, slippage, impact/capacity, funding treatment, leverage/margin policy, latency, partial-fill behavior, stop logic or sizing rule.

For research, event formation must use confirmed data available by the bar close; any trade simulation should execute no earlier than the next feasible timestamp unless the tested implementation explicitly models intrabar availability. Fees, spread, slippage and funding must be included in any later executable test.

## Evidence
### Source-reported

The source describes the indicator mechanics and qualitative use cases but does not provide a traceable Sharpe, CAGR, drawdown, win rate, statistical test, or independently audited performance result. No performance figure is promoted here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source's directional interpretation depends on the quality of its volume-delta proxy and OI feeds. OI is not intrinsically directional because every open derivative contract has both a long and short side; directional labels are an inference from joint flow state. A multi-venue aggregate can also be distorted by contract denomination, missing venues, symbol coverage changes, timestamp mismatch, or exchange-specific OI methodology.

No source-backed evidence was identified showing that the labeled events produce positive net-of-cost alpha. Absence of such evidence is not evidence that no effect exists.

## Falsification plan

1. **Baseline ablation:** price/return only -> OI delta only -> OI + candle direction -> OI + volume delta -> + sequential-cascade state -> + absorption state. Require incremental out-of-sample information at each added layer.
2. **Direction test:** compare the source-inspired delta classification against candle-color classification and, where available, true aggressor-side trade delta. If delta classification does not improve event discrimination, reject that incremental mechanism.
3. **Cascade competition:** after 2+ significant OI-decrease bars, test continuation and exhaustion reversal at fixed horizons. Do not select the winning direction in-sample and relabel it as the original hypothesis.
4. **Absorption test:** condition large OI increases on normalized candle-body displacement and test whether small-displacement events differ from equally large OI events with normal/large displacement.
5. **Threshold robustness:** sweep the 300-bar / 5.0 source defaults and nearby values. A result that exists only at a narrow tuned threshold is weak evidence.
6. **Venue ablation:** Binance-only, Bybit-only, and aggregate; leave-one-source-out where the underlying TradingView feeds permit it.
7. **Placebos:** randomize delta sign within volatility/time-of-day buckets and shift OI timestamps by one bar. Genuine event information should degrade materially under these controls.
8. **Regimes:** evaluate bull/bear, high/low realized volatility, high/low funding, and liquid/less-liquid assets separately.
9. **OOS and costs:** require chronological out-of-sample evaluation and realistic fees, spread, slippage and funding before any profitability claim.
10. Failure action: if the joint flow labels do not outperform simpler OI/price baselines robustly out of sample, reject the added classification layer rather than adding more filters.

## Crypto portability

direct

The source is explicitly designed for crypto perpetuals and aggregates Binance and Bybit OI. Portability is nevertheless venue- and data-dependent: OI units, inverse versus linear contracts, quote currencies, venue outages, funding, 24/7 candle boundaries and exchange listing histories must be normalized point-in-time.

## Limitations

- Exact source implementation of volume delta is underspecified in the reviewed descriptive text.
- Exact adaptive-threshold formula beyond the stated SMA lookback/multiplier is underspecified here.
- Exact small-candle-body threshold for absorption is underspecified.
- OI directional labels are inferred states, not direct observation of trader identity or intent.
- No complete entry/exit/holding/sizing strategy is source-specified.
- Multi-venue historical coverage and contract normalization can introduce data gaps and survivorship bias.
- Not independently reproduced.

## Implementation status

Research-only normalization. No implementation in the research stack and no Qlib full backtest has been completed for this record.

## Adoption boundary

This record is external research material only. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

Potential conceptual relatives include open-interest positioning, liquidation/deleveraging, order-flow delta, absorption, and multi-venue derivatives-flow research. No Wiki lookup was performed because this Scout run is GitHub-only.

## Sources

- TradingView — AghaInvst, **Aggregated Open interest + Volume Delta**: https://www.tradingview.com/script/ZpFcfJy3-Aggregated-Open-interest-Volume-Delta/ (public open-source script; reviewed 2026-09-21).
