---
schema: strategy-research-record-v1
title: "BTCUSDT 1H Multi-Timeframe Engulfing Trend-Following with SL-Flip and Winner Pyramiding"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-14
sources:
  - "https://www.tradingview.com/script/GoUoySJs-BTC-MTF-Engulfing-Flip-Pyramid-Strategy-1H-2X/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BTCUSDT 1H Multi-Timeframe Engulfing Trend-Following with SL-Flip and Winner Pyramiding

## Provenance

- **Primary source:** TradingView public open-source strategy page: https://www.tradingview.com/script/GoUoySJs-BTC-MTF-Engulfing-Flip-Pyramid-Strategy-1H-2X/
- **Author/page identity:** Jagadeesh Manne (`jagadeeshmanne`), “BTC MTF Engulfing Flip + Pyramid Strategy (1H, 2X)”.
- **Publication/update information:** source page shows April 17, 2026 release/update material and subsequent V3 release notes on the same public page.
- **Source as-of:** 2026-09-14.
- **Public-use status:** TradingView labels the script open-source. This record normalizes the public description and does not reproduce the Pine source code.
- **Deduplication:** no repository record was found for TradingView source `GoUoySJs`, Jagadeesh Manne, this specific SL-flip construction, or this exact multi-timeframe engulfing + winner-pyramiding rule. Materially related records include `crypto-perpetual-regime-aligned-right-tail-trend-cost-hurdle-2026-09-13.md`, `crypto-perpetual-supertrend-wpr-trend-following-cost-gate-falsification-2026-09-12.md`, and the recent TradingView squeeze records. Those share trend/regime or right-tail themes but not the stop-loss-triggered reverse trade plus single winner add architecture.

## Economic mechanism

### Source-reported

The source describes a BTCUSDT perpetual-futures trend-following system designed to accept frequent small losses in exchange for a small number of large trend winners. Entry selectivity is created by requiring agreement across three timeframes: a daily EMA trend regime, 4-hour RSI momentum, and a 1-hour engulfing-candle trigger confirmed by RSI, MACD, expanding ATR, and elevated volume. The source states that only about 1% of engulfing candles pass all filters.

The source adds two path-dependent extensions to the base trend-following thesis:

1. **SL-flip:** when the main trade is stopped, wait one hour and open the opposite direction with a tighter stop, on the premise that a failed high-conviction breakout can reveal a genuine reversal rather than random noise.
2. **Winner pyramiding:** when a main trade reaches +3R, add 50% of the original notional once, on the premise that the move has been sufficiently confirmed and that the strategy’s economics are dominated by fat-tail winners.

The author explicitly characterizes the system as low-win-rate / right-tail-dependent and warns that missing one or two large trends can materially reduce CAGR.

### Research interpretation

The falsifiable thesis has three separable mechanisms rather than one generic indicator stack:

- **Regime alignment:** daily EMA50 and 4H RSI attempt to suppress counter-trend 1H signals.
- **Selective continuation trigger:** the engulfing pattern is admitted only when 1H momentum, volatility expansion, and participation all align.
- **Path-dependent payoff shaping:** stop-loss-triggered delayed reversal seeks to monetize failed breakouts, while pyramiding seeks to increase exposure only after positive excursion confirms a rare trend tail.

The main incremental value versus existing repository trend-following records is therefore not RSI/MACD/EMA usage. It is the combination of **failed-breakout reversal after a one-hour delay** and **one-time +3R pyramiding into already-profitable main trades**. These two extensions should be ablated independently because either may alter payoff geometry without adding independent predictive information.

The source’s V1→V2→V3 tuning history is also a material alternative explanation: the same long historical sample was used repeatedly to tune partial-profit behavior, pyramiding, RSI length, and ATR length. This creates substantial multiple-testing / selection-bias risk despite the reported improvements.

## Signal

**Signal reconstruction status: underspecified in several execution details and internally inconsistent in one pyramiding stop rule.** The public page provides unusually detailed normalized logic, but exact Pine order-processing semantics, fee/slippage assumptions, some higher-timeframe availability handling, and one post-pyramid stop update are not unambiguous. Missing details are not promoted into source-reported facts.

### Formation timestamp and timeframe dependencies

- **Chart / decision timeframe:** 1-hour bars; source warns results require the chart to be set explicitly to 1H.
- **Daily regime:** long only when daily close is above daily EMA50; short only when below.
- **4H momentum:** RSI(14) > 50 for long and < 50 for short in the main description.
- **1H trigger:** all listed 1H conditions must hold on the same bar.
- **Point-in-time availability:** exact `request.security()` bar-merging/lookahead convention is not stated in the reviewed public description; this is underspecified and must be audited before reproduction.

### Main entry

**Long** requires:

1. Daily close > daily EMA50.
2. 4H RSI(14) > 50.
3. 1H RSI above the long-zone threshold.
4. 1H MACD(12,26,9) line above its signal line.
5. Bullish engulfing candle whose body is larger than the prior candle body; source setting lists engulf body multiplier 1.0×.
6. ATR above its moving average, indicating volatility expansion.
7. Volume > 1.5 × SMA(volume, 20).

**Short** mirrors the rule:

1. Daily close < daily EMA50.
2. 4H RSI(14) < 50.
3. 1H RSI below the short-zone threshold.
4. MACD line below signal line.
5. Bearish engulfing candle with body > prior body.
6. ATR above its moving average.
7. Volume > 1.5 × SMA(volume, 20).

### Current / versioned parameter ambiguity

The main V2 description uses 1H RSI(14) and ATR(14), with RSI long/short zones 45 / 55 and ATR MA length 50. Later V3 release notes on the same source page state that the 1H RSI period was changed from 14 to **21** and ATR period from 14 to **20**, while everything else remains the same. Because the public page preserves both versions, this record treats V3 as the latest source-reported variant but preserves V2 metrics separately rather than merging them.

### Main-trade stop and exits

- **Initial SL:** pattern-based using the tighter of a structure stop around the current/prior-bar extreme with 0.1% buffer and a maximum 2.5% distance from entry, according to the source description.
- **Partial TP:** at +6R favorable excursion, close 15% of the position.
- **After partial TP:** move the remaining-position stop to entry +0.1% according to the main description.
- **Opposite-direction qualified signal:** close the current position; do not immediately open the opposite trade merely because an opposite signal appears.
- **Drawdown circuit breaker:** a 25% decline from equity peak halts trading for 7 days.
- **Generic post-exit cooldown:** 2 hours.
- **Same-direction cooldown after SL:** 24 hours.

### SL-flip extension

After a **main-trade stop-loss**:

1. wait 1 hour;
2. open the opposite direction;
3. use a tighter 1.5% stop cap versus 2.5% for main trades;
4. source states the flip stop also references the swing high/low over the last 10 bars, using the tighter placement;
5. enforce a 24-hour time stop;
6. do not permit flip-on-flip cascades;
7. flips remain subject to the drawdown halt and generic cooldown;
8. no pyramiding on flip trades.

Exact same-bar order timing, entry price reference after the one-hour wait, and precedence if a new main signal occurs while a flip is queued are not fully specified in the public description; underspecified.

### Winner pyramiding

For main trades only:

- At +3R favorable excursion, add **50% of original notional** once.
- Total position becomes 150% of original notional.
- Maximum one add per trade.
- No pyramiding on flip trades.
- Source states effective exposure rises from normal 2× to about 2.7× during the pyramided state and recommends a 4× exchange leverage ceiling.

**Internal source inconsistency:** the main explanation/changelog says the original stop moves to **break-even** when the pyramid add fires, while one release-note block says it moves to **entry +0.5R**. This record does not choose between them. The post-pyramid stop rule is therefore `underspecified` until the current Pine code is audited directly.

### Position sizing / overlap

- Source states normal notional = equity × 2× leverage, effectively deploying full stated leverage per main trade.
- Source separately lists “risk per trade: 1%” as a dashboard-display setting, but the public description does not clearly reconcile that display metric with full-leverage notional sizing. Position-risk interpretation is therefore underspecified.
- Pyramiding permits one add to the current main position. Broader simultaneous-position behavior across competing signals is not fully specified in the public description.

## Required data

- **Instrument:** BTCUSDT perpetual futures; source explicitly limits its validation claim to BTCUSDT perpetuals.
- **Venue:** source says the authoritative full backtest uses Binance futures historical data.
- **Market type:** perpetual futures.
- **Timeframe:** 1H execution bars plus 4H and daily derived features.
- **Fields:** OHLCV sufficient for engulfing bodies, EMA50, RSI, MACD, ATR, ATR moving average, volume SMA, structure stops, and swing-high/low lookup.
- **Sample for headline Python evidence:** September 2019 through April 2026 (~6.5 years), per source.
- **Point-in-time requirement:** higher-timeframe values must be available without future-bar leakage at each 1H decision timestamp. Exact Pine HTF availability semantics are not documented on the public page and require code audit.
- **Timestamp / session:** crypto trades 24/7; Binance/TradingView bar boundary and timezone convention must be frozen for reproduction.
- **Missing-data handling:** not specified by source; no imputation should be introduced without a predeclared research protocol.
- **Funding / fees / spread:** perpetual funding is economically relevant but the reviewed public page does not report an explicit funding model. Exact commission, spread, slippage and market-impact settings for the Python headline numbers are not exposed in the reviewed description; treat performance as execution-cost-underspecified.

## Execution assumptions

### Source-reported

- Tested only on BTCUSDT perpetual futures, 1H, 2× normal leverage.
- Main stop capped at 2.5%; flip stop capped at 1.5%.
- One-hour delay before SL-flip entry.
- Partial TP 15% at +6R; remaining position continues with protective stop adjustment.
- One +50% pyramid add at +3R on main trades only.
- Flip positions have 24h time stop.
- Drawdown halt: -25% from peak for 168 hours.
- Cooldowns: 24h same-direction after SL, 2h generic after exit.

### Research interpretation

Execution is not sufficiently specified to treat the source-reported CAGR/PF as reproducible trading evidence. Before independent reproduction, freeze:

- same-close versus next-bar entry semantics;
- stop/target same-bar precedence;
- exact stop reference for engulfing structure;
- the conflicting post-pyramid stop rule;
- taker/maker fee schedule and whether fees apply per fill, including pyramid and partial exits;
- bid/ask spread and slippage;
- perpetual funding;
- mark-price versus last-price stop behavior;
- liquidation/margin model at 2×–2.7× effective exposure;
- partial-fill and order-failure handling.

The source itself warns that real slippage, partial fills, latency, and regime shifts will differ from backtest results.

## Evidence

### Source-reported

The TradingView page reports the following **Python backtest on Binance futures historical data** over approximately September 2019–April 2026. These are source claims, not independently verified results.

- **V2** (15%@6R partial + BE handling + SL-flip + +3R pyramiding): $5,000 → $420,395; +8,308% cumulative; CAGR 142.8%; max drawdown -20.3%; profit factor 5.54; win rate 34.2% (25 wins / 48 losses); 73 trades, including 9 flips.
- **V1** without pyramiding: $5,000 → $181,943; CAGR 105.3%; max drawdown -19.7%; profit factor 4.63; win rate 41.9%; 74 trades.
- **V3 release notes** report slower 1H indicators (RSI 21 and ATR 20) with $5,000 → $572,000, CAGR 158%, max drawdown -20.6%, profit factor 7.29, and 62 trades, versus the V2 figures above.
- The author reports that the system averages roughly 15 trades/year, that about 55% of trades are stopped, and that a few +10R-or-larger winners drive much of the outcome.
- The source explicitly states TradingView’s displayed backtest may cover a shorter history because of loaded-bar limits and treats the Python Binance-data backtest as authoritative.

The page also documents extensive tuning history on the same broad historical sample: baseline changes, addition of SL-flip, breakeven adjustment, partial-profit tuning, pyramiding at +3R, then V3 RSI/ATR period tuning.

### Independently reproduced

not independently reproduced

### Negative evidence

- **Multiple-testing / tuning risk:** the source explicitly describes repeated grid/search and parameter changes over the same multi-year historical window. Reported V1→V2→V3 gains therefore carry substantial selection-bias risk unless a genuinely untouched forward sample confirms them.
- **Small effective sample:** only 62–74 trades across ~6.5 years depending on version; tail-performance estimates are dominated by very few observations.
- **Fat-tail dependence:** source warns that missing one or two major winners can halve expected CAGR. This makes latency, fills, outages, and venue-specific price paths unusually consequential.
- **Execution-cost gap:** the public description does not expose a complete fee/slippage/funding/impact model for the headline Python results.
- **Internal rule inconsistency:** pyramid stop movement is described both as break-even and as entry +0.5R in different blocks on the same source page.
- **Version drift:** the page title/body prominently describes V2 while later release notes define V3 RSI/ATR changes. Reproduction must pin an exact version rather than combining statistics and parameters across versions.
- **Higher-timeframe leakage risk:** daily/4H filters require explicit completed-bar availability rules; the public description does not state Pine lookahead/barmerge semantics.
- **No independent out-of-sample reproduction** was identified in the reviewed TradingView source.

## Falsification plan

All failure cutoffs below are `research-defined falsification threshold` unless explicitly source-reported.

1. **Untouched forward / walk-forward test**
   - Data: Binance BTCUSDT perpetual 1H with 4H/daily aggregates, using a predeclared post-tuning holdout not used to select V3.
   - Metric: net profit factor, CAGR, max DD, trade count, and return contribution of top 1/3/5 trades.
   - Failure rule: reject the claimed robust right-tail edge if net PF ≤ 1.0 or CAGR ≤ 0 after realistic costs on the untouched segment; materially weaken it if >50% of net PnL comes from a single trade.
   - Action: retain only as historical hypothesis / negative evidence if failed.

2. **Component ablation: base entry vs SL-flip vs pyramiding**
   - Compare four fixed variants: base MTF entry only; base + flip; base + pyramid; base + flip + pyramid.
   - Metric: OOS expectancy per trade, PF, DD, skew, turnover, and top-tail concentration.
   - Failure rule: if neither flip nor pyramid improves OOS expectancy/PF without worsening DD materially, reject those extensions as in-sample payoff engineering.

3. **Failed-breakout flip placebo**
   - Compare the source’s one-hour post-stop reversal against randomized 0–6h delays and against “no flip”.
   - Metric: flip-trade expectancy after costs and bootstrap confidence interval.
   - Failure rule: if the 1h delay is not superior to the delay-placebo distribution or flip expectancy ≤ 0 net, reject the failed-breakout reversal mechanism.

4. **Pyramiding trigger perturbation**
   - Test fixed +2R, +3R, +4R, +5R adds with identical 50% size and one-add limit.
   - Metric: OOS PF/CAGR/DD and marginal PnL from added exposure.
   - Failure rule: if +3R advantage disappears under nearby thresholds or added exposure has non-positive net expectancy, classify +3R as tuned rather than structural.

5. **HTF leakage / timestamp audit**
   - Recompute daily EMA50 and 4H RSI only from bars fully closed and available at each 1H signal time.
   - Metric: signal parity and performance delta versus source-like implementation.
   - Failure rule: any use of future higher-timeframe close invalidates the corresponding backtest evidence.

6. **Realistic friction stress**
   - Include Binance perpetual taker/maker fees, bid/ask spread, slippage, funding, partial exits, pyramid fills, and adverse stop execution.
   - Stress baseline costs at 1×, 1.5× and 2×.
   - Failure rule: if PF falls ≤1.0 at baseline realistic costs or ≤1.1 at 1.5× costs, reject practical tradability.

7. **Tail concentration / missed-winner stress**
   - Remove the best 1, 2, and 3 trades from each evaluation window.
   - Metric: CAGR and PF.
   - Failure rule: if removing one trade turns total net return negative, classify the strategy as too path-dependent for a stable alpha claim.

8. **Version-lock replication**
   - Reproduce V2 and V3 separately with pinned parameters and one explicit post-pyramid stop rule each.
   - Failure rule: if the source-reported metrics require mixing V2/V3 parameters or contradictory stop logic, mark the headline evidence non-reproducible.

## Crypto portability

**direct** for the stated source thesis because the source explicitly targets BTCUSDT perpetual futures on Binance-style crypto derivatives data.

Crypto-specific requirements remain material:

- 24/7 1H/4H/daily candle boundaries must be pinned.
- Perpetual funding can materially affect multi-day right-tail trades.
- Venue fragmentation means engulfing candles, stop hits, and +3R/+6R paths may differ across Binance, Bybit, OKX, etc.
- Stop and liquidation behavior depends on mark/index/last-price rules and maintenance margin.
- Stablecoin collateral and exchange outages add risks absent from OHLCV-only backtests.
- Pyramiding raises margin utilization precisely during large trends, so liquidation and funding stress must be modeled jointly with the add-on leg.

Direct portability does not imply profitability or authorization to implement.

## Limitations

- TradingView public source; not peer-reviewed and not independently reproduced.
- `underspecified` exact Pine order-processing / higher-timeframe availability semantics.
- `underspecified` complete fee, spread, slippage, funding, impact and liquidation model for headline Python results.
- `underspecified` post-pyramid stop rule because the page contains conflicting BE versus entry+0.5R descriptions.
- V1/V2/V3 tuning was performed on overlapping historical data, creating strong data-snooping risk.
- Small trade count and extreme right-tail concentration reduce statistical confidence.
- Single symbol / single core venue evidence; no demonstrated cross-asset or cross-venue robustness.
- Full source code was not copied into this record; reproduction must audit the current public Pine source directly.

## Implementation status

`not-implemented`. No implementation in the local research stack, historical reproduction, PyBroker/Nautilus validation, Paper, Testnet, or Live workflow was performed by this Scout cycle.

## Adoption boundary

`research-only` / `not-implemented` / `not-approved` / `approval_scope: research-only`.

This record captures a public TradingView hypothesis and source-reported evidence only. It does not establish profitable alpha, authorize strategy implementation, or permit Paper/Testnet/Live execution. Any implementation or adoption decision requires separate review and independent historical validation.

## Related Wiki records

Repository-local related records reviewed for deduplication:

- `crypto-perpetual-regime-aligned-right-tail-trend-cost-hurdle-2026-09-13.md` — right-tail trend following with explicit cost hurdle and macro regime filter; no SL-flip/pyramid path architecture.
- `crypto-perpetual-supertrend-wpr-trend-following-cost-gate-falsification-2026-09-12.md` — multi-timeframe crypto-perp trend/pullback family with different trigger and falsification framework.
- `btc-30m-wyckoff-squeeze-multilayer-trend-momentum-2026-09-14.md` — TradingView BTC squeeze/trend confluence; different entry mechanism and no stop-triggered reverse trade.
- `eth-2h-squeeze-volume-adaptive-regime-breakout-2026-09-14.md` — TradingView volatility breakout with regime-dependent exit geometry; different mechanism.

No known stable Hermes Wiki Brain page was fabricated or linked.

## Sources

- TradingView, Jagadeesh Manne, “BTC MTF Engulfing Flip + Pyramid Strategy (1H, 2X)”: https://www.tradingview.com/script/GoUoySJs-BTC-MTF-Engulfing-Flip-Pyramid-Strategy-1H-2X/ (public open-source strategy page; source as-of 2026-09-14).
