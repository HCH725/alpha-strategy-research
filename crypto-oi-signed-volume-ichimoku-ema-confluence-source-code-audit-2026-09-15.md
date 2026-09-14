---
schema: strategy-research-record-v1
title: "Crypto OI + Signed-Volume / Ichimoku EMA Confluence Source-Code Audit"
created: 2026-09-15
updated: 2026-09-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-15
sources:
  - "https://www.tradingview.com/script/6NrWx3Fi-OI-CVD-Ichimoku-PRO-Strategy/"
  - "https://www.tradingview.com/pine-script-docs/concepts/strategies/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The publication describes an OI + CVD order-flow confirmation layer, but the executable Pine combines OI change and the so-called CVD with OR, so either branch alone can satisfy the order-flow filter."
  - "The executable Pine labels an EMA of whole-bar volume signed only by close-versus-open direction as CVD; it is neither cumulative volume delta nor aggressor-side buy/sell volume delta."
  - "The input 'Number of TPs (1 or 2)' changes TP2 plotting but does not gate the TP2 strategy.exit order; the TP2 exit is submitted even when tp_count is 1."
  - "Stop and take-profit prices are computed from the signal bar close, while the strategy declaration does not enable process_orders_on_close; under TradingView's default broker-emulator semantics, a market entry created at bar close fills no earlier than the next available tick, normally the following bar open."
---

# Crypto OI + Signed-Volume / Ichimoku EMA Confluence Source-Code Audit

## Provenance

- **Primary source:** `egoigor1976`, **OI+CVD+Ichimoku PRO Strategy**, public TradingView open-source Pine Script v6 strategy.
- **Stable public URL:** https://www.tradingview.com/script/6NrWx3Fi-OI-CVD-Ichimoku-PRO-Strategy/
- **Publication timestamp shown by TradingView:** 2026-06-28 16:01 UTC.
- **Latest update shown by TradingView at review time:** 2026-08-02 08:55 UTC; release note: `Update Ichimoku Cloud`.
- **Source reviewed as of:** 2026-09-15.
- **Author/page identity:** TradingView user `egoigor1976`.
- **Public-use status:** TradingView labels the script open-source. This record does not reproduce the Pine script; it normalizes the executable rule and audits material source-description/code mismatches.
- **Deduplication:** repository search found no record for TradingView identity `6NrWx3Fi` or this exact EMA-cross + OI-change-or-signed-volume + displaced-Ichimoku construction. Materially related records include `crypto-perp-aggregated-oi-volume-delta-conviction-filter-2026-09-14.md`, which studies genuine aggregate OI expansion **and** lower-timeframe volume delta, and `crypto-btc-perp-multiconfluence-pseudo-derivatives-proxy-source-code-audit-2026-09-15.md`, which documents a different six-vote OHLCV proxy system. The current source adds distinct negative/source-integrity evidence: an advertised OI+CVD confluence is implemented as an OR gate, the CVD label maps to candle-direction-signed total volume, and a configurable TP count is not respected by exit-order logic.

## Economic mechanism

### Source-reported

The TradingView publication describes a three-tier confirmation system intended to combine:

1. a fast/slow EMA trend cloud (defaults 13/25);
2. an order-flow filter described as Open Interest plus Cumulative Volume Delta, intended to confirm that a move is backed by new capital and directional flow; and
3. an Ichimoku-cloud trend filter.

The source presents the approach as a way to reduce false momentum signals in sideways conditions. It specifically describes the system as suitable for liquid cryptocurrency futures such as BTC/USDT and mentions 5-minute, 15-minute, and 1-hour charts as recommended timeframes. These are source claims, not independently verified performance evidence.

### Research interpretation

The executable source supports a narrower falsifiable hypothesis than the publication wording suggests: **an EMA crossover may have better forward continuation when price is on the corresponding side of a causally aligned Ichimoku cloud and either open interest changes in the crossover direction or recent candle-direction-signed volume is directionally positive/negative.**

The order-flow interpretation requires caution:

- the OI branch does use a requested OI series and one-bar OI change;
- the second branch is not true CVD. It applies the whole candle's volume a positive sign when `close > open`, otherwise a negative sign, then takes an EMA over 14 bars by default;
- because the branches are joined with **OR**, the executable strategy does not require both OI and volume confirmation.

Accordingly, any later empirical edge must be attributed to the actual variables and Boolean construction, not to a stronger claim that independent OI and genuine aggressor-side CVD jointly confirm institutional participation.

## Signal

**Reconstruction status:** the current public Pine is exact enough to reconstruct its chart-timeframe rule. Live execution costs, venue mapping, OI feed completeness, and production fill behavior remain underspecified.

### Source-reported executable construction

- **Chart timeframe:** user-selected; the publication recommends 5m, 15m, or 1h.
- **Price inputs:** chart OHLCV.
- **EMA trend trigger:** EMA(13) crossing EMA(25).
- **OI input:** TradingView requests `syminfo.ticker + ".P_OI"` at the chart timeframe and computes one-bar OI change as current OI close minus previous OI close. Invalid OI symbols are ignored by the request.
- **OI threshold:** default `0`; user-adjustable in steps of 100.
- **Signed-volume proxy labeled CVD:** EMA(14) of `volume × sign`, where sign is +1 only when `close > open`, otherwise -1. This is a directional volume proxy, not cumulative or aggressor-classified delta.
- **Ichimoku:** Tenkan 9, Kijun 26, Senkou B 52, displacement 26. The filter compares current close with the cloud values calculated 26 bars earlier, corresponding to the cloud visually projected to the current bar. The filter is enabled by default.
- **Bullish filter:** `(OI change > OI threshold OR signed-volume EMA > 0) AND close > current visible cloud top`.
- **Bearish filter:** `(OI change < -OI threshold OR signed-volume EMA < 0) AND close < current visible cloud bottom`.
- **Long entry condition:** EMA(13) crosses above EMA(25) and the bullish filter is true.
- **Short entry condition:** EMA(13) crosses below EMA(25) and the bearish filter is true.
- **Position sizing:** 10% of strategy equity per `strategy.entry`; initial capital is 1000 in the source declaration.

### Exit and holding behavior

On every qualifying entry signal, the script freezes stop/target levels from the **signal bar close**:

- default stop: 1.5 × ATR(14) from the signal close; alternatively a fixed 1.5% stop if ATR mode is disabled;
- TP1: 1.5 × ATR(14) from the signal close;
- TP2: 3.0 × ATR(14) from the signal close;
- TP1 exit requests 50% of the entry position;
- TP2 exit is also submitted by the executable source.

The UI exposes `Number of TPs (1 or 2)`, default 2. However, in the reviewed Pine, `tp_count` is used to decide whether TP2 is **plotted**, not whether the TP2 `strategy.exit` order is created. Therefore selecting one TP does not, in the source code reviewed, suppress the TP2 exit order.

An opposite qualified `strategy.entry` can reverse an open position under TradingView strategy semantics. No independent time exit is defined. Maximum holding period is therefore not fixed by the source.

### Formation timestamp and availability

The strategy uses default bar-close calculation behavior. Treat completed chart-bar values as the historical signal-formation state. OI must be available for the corresponding chart bar; if it is unavailable, the source's `ignore_invalid_symbol=true` plus `nz(oid, 0)` handling can leave the signed-volume branch capable of passing the OR gate.

## Required data

- **Instrument / universe:** publication targets liquid crypto futures, explicitly giving BTC/USDT as an example; the Pine itself is chart-symbol driven.
- **Market type:** intended cryptocurrency futures/perpetual context where an OI series is available.
- **Venue:** chart/exchange dependent; no single production venue is mandated by the source.
- **Timeframe:** chart timeframe; publication recommends 5m, 15m, or 1h.
- **Fields:** chart OHLCV; TradingView open-interest close for the constructed `.P_OI` symbol.
- **No true CVD data are consumed:** no individual trades, aggressor flag, bid/ask classification, or lower-timeframe buy/sell decomposition is requested.
- **Timestamp:** chart/exchange bar timestamps as provided by TradingView. Cross-venue timezone normalization is not source-specified.
- **Point-in-time:** use only completed chart-bar OHLCV and OI available by the decision timestamp. OI gaps and symbol-resolution failures must be preserved rather than backfilled from future observations.
- **Missing data:** OI request is configured to ignore an invalid symbol; source does not define a separate stale-data or missing-OI rejection rule.
- **Costs:** fees, spread, slippage, market impact and perpetual funding are not specified in the strategy declaration and are required for any tradability test.

## Execution assumptions

### Source-reported / source-defined

- Entries are generated through `strategy.entry`, i.e. market-entry orders in TradingView's broker emulator unless the user changes strategy properties externally.
- Stop-loss and profit exits use `strategy.exit` with stop/limit prices.
- Position sizing defaults to 10% of equity.
- Stop/target reference prices are calculated from the signal bar close.
- The Pine declaration does not specify commission, slippage, `process_orders_on_close`, or custom intrabar calculation behavior.

### Research interpretation of TradingView default semantics

TradingView's current official Pine strategy documentation states that, with default bar-close calculation and `process_orders_on_close=false` (the default), an order generated on a bar's closing tick can fill no earlier than the next available tick, normally the next bar open in historical simulation. Therefore the source's stop/TP geometry is **signal-close anchored rather than actual-entry-fill anchored** unless the fill happens to equal the signal close. This distinction must be preserved in source-parity reproduction before any research-proposed correction is tested.

`research-proposed` production testing should separately evaluate exits anchored to actual fill price, explicit taker/maker fees, half-spread, slippage, funding, latency, partial-fill behavior, leverage/margin and liquidation rules. None of these corrections are source-reported.

## Evidence

### Source-reported

The publication supplies the intended component roles, recommended timeframes, and the public Pine implementation described above. It does **not** provide a traceable source-reported Sharpe ratio, CAGR, win rate, drawdown, t-statistic, fixed sample period, cost-adjusted result, walk-forward result, or independent out-of-sample result on the reviewed public page.

The source describes the order-flow layer as OI + CVD confirmation and says it is intended to validate momentum moves with actual market money flow. Those statements are mechanism claims, not verified empirical evidence.

### Independently reproduced

not independently reproduced

### Negative evidence

1. **CVD semantic mismatch:** the executable source does not calculate cumulative volume delta or aggressor-side volume delta. It smooths whole-bar volume signed by candle direction.
2. **Confluence mismatch:** the executable OI and signed-volume branches are joined with OR, so one can pass without the other. This is weaker than interpreting the publication's OI+CVD confirmation language as joint independent confirmation.
3. **Missing-OI degradation:** because invalid OI symbols are ignored and missing OI change is normalized to zero before the OR gate, the strategy can continue to trade from the signed-volume branch rather than fail closed when OI is absent.
4. **TP-count control mismatch:** `tp_count` controls TP2 visualization but not TP2 order creation. A setting of one take-profit therefore does not produce a one-TP executable order set in the reviewed source.
5. **Entry/exit reference mismatch:** stop and targets are frozen from the signal close, while default market-entry fills occur on the next available tick. Gaps or fast bars can materially change realized risk/reward relative to the displayed ATR multiples.
6. **Existing adjacent negative evidence:** `retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md` reports that tested one-minute crypto CVD/order-flow momentum and related retail microstructure signals did not survive realistic transaction costs. That does not directly test this EMA/Ichimoku hybrid, but it weakens any assumption that a volume-delta label itself supplies robust tradable alpha.
7. The reviewed TradingView source provides no OOS, cross-venue, cost, capacity, or funding evidence.

## Falsification plan

1. **Exact source-parity reconstruction**
   - **Data:** TradingView-equivalent OHLCV and OI for at least BTC perpetual on each source-recommended timeframe (5m, 15m, 1h), with frozen bar timestamps.
   - **Sample:** at least one contiguous 12-month period containing high- and low-volatility regimes.
   - **Metric:** completed-bar equality for EMA cross, OI branch, signed-volume branch, Ichimoku gate, entry direction and submitted stop/target prices after warm-up.
   - **Failure rule:** any systematic signal mismatch or unexplained order-level mismatch invalidates downstream performance testing until resolved.
   - **Action:** remediate source parity only; do not retune alpha parameters.

2. **OI incremental-value ablation**
   - **Data/sample:** same point-in-time perpetual sample with OI completeness explicitly measured.
   - **Controls:** original OR gate versus signed-volume-only versus OI-only versus an AND gate. The AND gate is `research-proposed`, not source-reported.
   - **Metrics:** OOS net Sharpe, net return, turnover, hit rate and next-bar/next-N-bar conditional return.
   - **Research-defined falsification threshold:** weaken the claimed OI contribution if removing OI changes OOS net Sharpe by less than 0.10 and changes median forward return by less than 1 basis point while preserving at least 90% of source entries.
   - **Action:** treat OI as non-incremental for this construction if failed.

3. **True-CVD substitution / semantic validity test**
   - **Data:** trade-level or venue-native aggressor-side buy/sell volume aligned point-in-time with the chart bars.
   - **Comparison:** source candle-signed-volume EMA versus genuine cumulative/aggressor delta variants, without changing the EMA/Ichimoku portions.
   - **Metrics:** sign agreement, rank correlation, entry overlap and OOS forward-return ordering.
   - **Research-defined falsification threshold:** reject the source's CVD interpretation if sign agreement is below 60% or absolute rank correlation is below 0.20 and genuine delta produces materially different entry ordering.
   - **Action:** preserve the original variable only as a candle-signed-volume proxy.

4. **TP-count executable parity test**
   - **Data:** source-parity replay with `tp_count=1` and `tp_count=2`.
   - **Metric:** number and price of submitted TP orders.
   - **Failure rule:** if any TP2 order exists when `tp_count=1`, the public control cannot be interpreted as selecting a one-TP execution mode.
   - **Action:** retain this as source-code negative evidence; any corrected implementation must be labeled `research-proposed` and tested separately.

5. **Signal-close versus fill-price exit anchoring test**
   - **Data:** causal next-tick/next-bar fills with OHLC or finer execution data.
   - **Comparison:** exact source signal-close-anchored exits versus `research-proposed` actual-fill-anchored exits.
   - **Metrics:** realized initial risk in ATR units, target distance in ATR units, stop/target sequencing and net PnL.
   - **Research-defined falsification threshold:** classify source execution geometry as materially distorted if more than 10% of entries differ from intended initial stop distance by over 0.25 ATR after the actual entry fill.
   - **Action:** do not use source strategy-report performance as an execution-faithful result without resolving the difference.

6. **Walk-forward and cost stress**
   - **Data:** at least two liquid perpetual venues where equivalent OHLCV/OI can be aligned without survivorship leakage.
   - **Split:** pre-declared chronological train/calibration and untouched forward OOS segments; no parameter selection on the final OOS segment.
   - **Costs:** observed/venue-specific taker fees, half-spread, slippage and funding; latency stress at one bar and at a realistic order-routing delay.
   - **Metrics:** net Sharpe, net return, max drawdown, turnover and trade count by venue/regime.
   - **Research-defined falsification threshold:** reject tradable-alpha interpretation if OOS net Sharpe is <= 0 or total OOS net return is <= 0 on both independent venues under baseline costs.
   - **Action:** retain only as descriptive/negative research evidence if failed.

7. **Parameter and placebo robustness**
   - **Parameters:** perturb EMA lengths, OI threshold, signed-volume smoothing, Ichimoku windows/displacement and ATR stop/targets around source defaults without selecting the best post hoc cell.
   - **Placebo:** shuffle the OI-change and signed-volume states within volatility/time blocks while retaining EMA crossover timing.
   - **Metrics:** distribution of OOS net Sharpe and conditional forward returns.
   - **Research-defined falsification threshold:** reject a stable-mechanism interpretation if the source default sits in an isolated performance spike or does not outperform at least 90% of block-preserving placebo outcomes.
   - **Action:** no unconstrained retuning after failure.

## Crypto portability

**direct** for the intended hypothesis because the publication explicitly targets liquid cryptocurrency futures/perpetual-style markets and consumes crypto open interest.

Portability remains venue-sensitive:

- OI symbol availability and contract definitions differ by exchange/feed;
- true volume delta requires venue-specific trade/aggressor data that this source does not consume;
- perpetual funding must be included whenever a position spans funding settlements;
- 24/7 bar boundaries and exchange timestamps must be held constant across research and live execution;
- mark/index price, liquidation, margin and contract-size conventions can change realized risk even when chart-close signals match;
- cross-venue OI is not aggregated by this source, so single-feed positioning noise can dominate.

## Limitations

- `not independently reproduced` as a strategy result.
- No source-reported Sharpe, CAGR, win rate, drawdown, fixed sample, OOS, cross-venue or capacity evidence.
- The variable labeled CVD is not cumulative/aggressor-side volume delta.
- OI and signed-volume confirmation are OR-gated rather than jointly required.
- OI feed availability/failure is not fail-closed in the trading rule.
- The one-versus-two TP input does not control TP2 order submission in the reviewed source.
- Source stop/target geometry is based on signal close rather than verified entry fill.
- Fees, spread, slippage, impact, funding, leverage, margin, liquidation and latency are omitted/underspecified.
- Publication statements about reducing fakeouts or representing institutional participation are hypotheses, not validated facts.

## Implementation status

`not-implemented`

No implementation, backtest, PyBroker campaign, Nautilus validation, paper trading, testnet, or live execution has been performed by this Scout. This record is a normalized source-code audit and research hypothesis only.

## Adoption boundary

`research-only`; `not-approved`.

Presence in this staging repository does not establish profitability, validated alpha, implementation authorization, or permission for Paper, Testnet, or Live use. Any corrected CVD definition, AND-style confluence, OI fail-closed gate, TP-count repair, or actual-fill-anchored risk logic would be a separate research-proposed implementation choice requiring explicit review and validation.

## Related Wiki records

- [[quant/retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]] — adjacent negative evidence on retail-accessible crypto CVD/order-flow, OI-conditioned liquidation and funding signal families after realistic costs.
- No exact Wiki Brain record for TradingView identity `6NrWx3Fi` was found in the pre-write search.

Repository-only adjacent records used for deduplication, not asserted as already-ingested Wiki paths:

- `crypto-perp-aggregated-oi-volume-delta-conviction-filter-2026-09-14.md`
- `crypto-btc-perp-multiconfluence-pseudo-derivatives-proxy-source-code-audit-2026-09-15.md`

## Sources

1. `egoigor1976`, **OI+CVD+Ichimoku PRO Strategy**, TradingView public open-source Pine Script v6 strategy; publication shown 2026-06-28 16:01 UTC, updated 2026-08-02 08:55 UTC; complete current 98-line public source reviewed 2026-09-15. https://www.tradingview.com/script/6NrWx3Fi-OI-CVD-Ichimoku-PRO-Strategy/
2. TradingView, **Pine Script Strategy concepts**, current official documentation reviewed 2026-09-15; used only to interpret broker-emulator default order-creation/fill timing and `process_orders_on_close` behavior. https://www.tradingview.com/pine-script-docs/concepts/strategies/
