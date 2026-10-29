---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "fightpm BB80 upper-breakout with dual SMA slope filter — independent BTC-USDT spot daily long-flat derivative"
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
status: research-only
confidence: medium
source_as_of: 2025-06-12
sources:
  - https://www.tradingview.com/script/h0ePZA90/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# fightpm BB80 + SMA200 dual-slope breakout — independent spot long-flat derivative

## Provenance

**Primary source, directly inspected 2026-10-29:** fightpm, *Daily Bollinger Band Strategy*, public TradingView open-source strategy, stable script ID h0ePZA90, originally published **2025-04-09**, last described update **2025-06-12**: https://www.tradingview.com/script/h0ePZA90/ . The first-party English and Japanese descriptions both specify: daily bars; Bollinger default period 80 and multiplier 1 standard deviation; 200-day trend moving average; long entry when price crosses above the upper +1-sigma band AND both the Bollinger middle band and 200-day moving average slope upward; long exit when price crosses below the middle band; mirror-image short rules; orders at **the following day's market open**; ATR-based position sizing using a 1% capital-risk budget, 2 x ATR, and rounded share units; no pyramiding, partial exits or stop-and-reverse. The June revision describes configurable indicator periods, ATR length default 20 and altered capital/share settings. The author lists zero brokerage fees for the illustrative backtest and reports historical Nikkei 225 results; **none of those historical returns or zero-fee assumptions are independently reproduced or adopted here**.

**Source accessibility and version caveat:** The first-party description and revision notes were readable, but full original Pine source bytes, exact indicator implementation/variance, order flags, and the exact June revision code were not recovered. This record is **NOT a source-native or lossless Pine reproduction**. It pins a separately identified, complete, executable *independent derivative* using only the source-described core signal topology. The stable TradingView script ID is the source lineage; the frozen derivative identity below is the implementation identity.

**Researcher-defined alterations (all material):** (1) translate the Nikkei daily-share strategy to Binance BTC-USDT spot daily UTC bars; (2) disable the author's short side; (3) choose completed CLOSE crossing rather than an unspecified intrabar price event; (4) explicitly choose close-SMA80 with population standard deviation and SMA200 on close; (5) change the source's **next-day-open** MARKET fill to a **next-completed-day CLOSE** historical MARKET simulator fill, not a live order guarantee; (6) replace ATR20 / 1%-risk / share-lot sizing with one fixed 0.001 BTC order and 10,000 USDT initial cash; (7) replace source illustrative zero brokerage fees with an explicitly hypothetical 0.1% per filled side; (8) set 250 completed daily-bar warmup and exact state/priority/invalid-data rules; (9) disable all unspecified protective stops, targets, time exits, trailing exits, DCA, partial fills, additional filters and cooldown. The source describes **no separate protective stop order**; a 1%-risk sizing budget is not a guaranteed 1%-loss stop. All altered timing, sizing and disabled legs can change trade events and outcomes. No original-equivalent backtest or live-performance claim is made.

**Immutable research identity:** TV:h0ePZA90|fightpm|published-2025-04-09|updated-2025-06-12|independent-derived-v1-2026-10-29|BinanceSpot-BTC-USDT-UTC1d|SMA80-popSD1-upper-close-crossup+SMA80-up+SMA200-up|close-crossdown-SMA80-exit|long-flat-fixed0.001BTC-cash10000|signal-Et-fill-next-Et1-MARKET-row-close|fee0.001-side|warmup250|no-DCA-no-short. Any change in signal, data, market, timing, size, fees, or state requires a new frozen derivative identity.

**Dedup at main SHA 094202e17eb2037f1f099a799945ebe6e4ed42b5:** nontruncated root tree contains 439 strategy Markdown records, and README says 439. Connected GitHub code search for h0ePZA90 and all-state PR search for h0ePZA90/fightpm returned none; open research PRs were checked and none cites this source. Closest main record, *bollinger-band-breakout-long-midline-exit-btcusdt-1d-2026-10-11.md*, uses **20-period, 1.5-sigma** upper-breakout and midline exit with **no** dual-upward-slope gate. This derivative requires BOTH SMA80 and SMA200 increasing at entry, uses **80/1** bands, and has a separate first-party source, so it is not the same decision rule or a cosmetic parameter variant. Other RSI+BB and lower-band-reclaim records have materially different entry and exit topology.

## Economic mechanism

### Source-reported

A close above the +1-sigma Bollinger rail is interpreted as a trend breakout only when both the 80-day band center and the 200-day trend average are rising. A downward cross of the band center marks loss of that intermediate trend. The source trades Japanese equities on daily bars and uses ATR-adjusted share sizing. It does not establish that this design is profitable on BTC, nor that its stated Nikkei returns survive fees or the derivative's timing change.

### Research interpretation

The dual slope test filters upper-band breaks against a flat or falling long-term trend. The midline cross exit can retain exposure through drawdowns; with no protective stop this is not a capped-loss strategy. BTC market portability and effectiveness are untested hypotheses, not asserted facts.

## Signal

**Gate 1 — deterministic, fully pinned formulas.** Use a single chronological Binance BTC-USDT Spot UTC 1d candle series, index t=0,1,...; C[t] is the actual strictly positive, finite CLOSE of a completed daily candle. Calculate in float64 in ascending time order; no fit, optimization, full-sample statistic, or future data. Define for each t >=79:

- B80[t] = (sum of C[t-79] through C[t]) / 80.
- S80[t] = sqrt( (sum over i=t-79..t of (C[i]-B80[t]) squared) / 80 ). **Population** standard deviation (researcher-defined).
- U80[t] = B80[t] + S80[t]; lower band B80-S80 is not an order input.
- For t>=199, M200[t] = (sum of C[t-199] through C[t]) / 200.
- Rising80[t] = (B80[t] > B80[t-1]); Rising200[t] = (M200[t] > M200[t-1]). Equality is NOT rising.
- UpperCross[t] = (C[t-1] <= U80[t-1]) AND (C[t] > U80[t]); strict crossing, no repeated level-state entries, touch alone does not count.
- MidCrossDown[t] = (C[t-1] >= B80[t-1]) AND (C[t] < B80[t]); equality at current bar does not exit.
- LongEntry[t] = UpperCross[t] AND Rising80[t] AND Rising200[t]. This is the source-described **dual-slope** breakout translated to explicit close-price calculations.

**Gate 2 — direction:** long/flat ONLY on Binance BTC-USDT spot; no short, borrowing, perpetual, isolated/cross margin, leverage, liquidation, hedging or simultaneous second asset. Leverage is 1x cash spot; spot funding payments are inapplicable.

**Gate 3 — entry/exit/risk:** From FLAT, an eligible completed t with LongEntry true schedules one BUY. From LONG, an eligible completed t with MidCrossDown true schedules a full SELL; no additional trend condition is required for exit. EXIT has priority over ENTRY if an unexpected logical overlap occurs, but a standard upper-band breakout and midline crossdown cannot co-occur on the same completed bar with nonnegative band width. No price-based stop, take-profit, trailing stop, time exit, volatility exit, terminal forced liquidation, intrabar order, market-session filter or extra signal. Do not misrepresent the removed 1%-ATR source sizing as protective stop coverage.

**Gate 4 — complete position state:** Initial cash 10,000 USDT, BTC inventory 0; exactly 0.001 BTC per BUY/SELL. States FLAT -> BUY_PENDING -> LONG -> SELL_PENDING -> FLAT. One pending order maximum. No DCA, safety order, scaling, pyramiding, partial planned close, concurrent entry, compounding, rebalancing or cooldown. A signal is consumed when queued, never duplicated. On the fill bar, do not evaluate a second entry/exit from that same bar's indicators. A fresh entry requires a NEW upper-band cross on a later completed bar after SELL is confirmed; no immediate reversal. If a fill fails, is partial, violates available quote balance, precision/lot/min-notional rules, has a missing price or has an invalid/duplicate timestamp, abort research rather than silently alter size or assume success. If a SELL is not filled, remain LONG with exit intent pending and no new entry. At dataset end, pending actions remain unfilled; any open BTC is marked at the last validated real close, never force-sold.

## Required data and causality

**Gate 6:** Require at least **250 prior completed, contiguous, nonduplicated UTC daily candles** before the first eligible signal at t=250; B80, M200 and their t-1 slopes are then defined. Raw Binance candle timestamp T[t] is its UTC **opening** time; the completed candle is not available until E[t]=T[t]+86400 seconds. Validate strict daily T[t+1]-T[t]=86400, valid finite positive OHLC, H>=max(O,C), L<=min(O,C), finite nonnegative volume and actual real CLOSE on every signal/fill/mark row. No gap fill, forward fill, interpolation, substitute price, negative shift, partial daily candle, unconfirmed higher timeframe, future pivot, or future label. Only completed t or earlier may generate LongEntry[t] or MidCrossDown[t]. The next-row fill price is not used to decide the prior signal. The engine's own dropna preparation must NOT be allowed to hide missing raw candles: validate before feeding it. No external data, cross-asset synchronization, session anchor, model training or order-book feed.

## Execution assumptions

**Gate 5 — pinned executable historical path, static source verified with connected GitHub on 2026-10-29:**

- Admission contract package **20260920**, Hummingbot VERSION **dev-2.17.0**; inspected source repository **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3**. VERSION blob fa1dd206a0e288710d6d68e195d4f030960fc6fb. Accepted Alpha PR #414 previously reported 902/902 byte-identical wheel/source mapping; this Scout did NOT rehash the wheel or assert an installed environment was inspected. If the actual installed package differs, revalidate the path before using it.
- Binance Spot 1d candles: hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py blob 6d505dff42b60b356931df13eeeecd1e28b426f9 lists 1d and /api/v3/klines; binance_spot_candles.py blob 5d0c938af574aca5f8dcba5ba28121797eae4dd0 parses opening timestamp and actual OHLCV. This is data support only, not a fill claim.
- Controller/executor: strategy-specific ControllerV2 carries a completed t signal in a one-row-delayed pending state. backtesting_engine_base.py blob 7d1e552dd7ee62df4f83f10950b8d593cd1106e6 prepares real candle rows, calls update_state(row), then determine_executor_actions(), then simulate_executor() on the current row slice. The Controller must dispatch the t decision only when processing row t+1, never when t was first observed.
- Exact order path: OrderExecutorConfig in order_executor/data_types.py blob 67715e3d14a1edf636defa95a7bbe5c73b8cff90 accepts connector binance, trading_pair BTC-USDT, TradeType.BUY or SELL, amount Decimal("0.001"), PositionAction.OPEN/CLOSE, leverage 1 and ExecutionStrategy.MARKET. OrderExecutorSimulator in order_executor_simulator.py blob 3b4e82e91896db9074295ca2a8a087dde2499eab uses the **first supplied row's actual CLOSE** for a MARKET fill, not that row's open, and computes filled_amount_quote=amount*close and cum_fees_quote=trade_cost*amount*close; the executor terminates as POSITION_HOLD. No next-open or intrabar path is asserted compatible.
- **Two clocks must be kept distinct:** the simulator's row/fill timestamp is T[t+1] (opening timestamp), while the actual C[t+1] price becomes observable at E[t+1]. For causal research interpretation, record both raw simulator timestamp and economic fill-availability E[t+1]. This is a historical next-completed-close convention, **not** a claim that a live MARKET order could be placed at E[t+1] and guaranteed the same C[t+1]. On fill row t+1 no fresh signal is evaluated; a new signal can first be evaluated on t+2.
- Position/cost: BacktestPositionHold in backtesting_engine_base.py accumulates matching BUY/SELL base units and gross realized PnL and **tracks fees separately**. Explicit quote-cash and BTC-inventory ledger must reconcile every confirmed fill: BUY reduces cash by 0.001*P*(1+0.001) and adds 0.001 BTC; SELL removes 0.001 BTC and adds 0.001*S*(1-0.001). Matched net PnL=0.001*(S-P)-0.001*0.001*(P+S). Research trade_cost=0.001 per filled side is a **hypothetical** fee, not a measured Binance fee. Do not use gross BacktestPositionHold realized PnL or summarize_results net_pnl_quote alone as net-of-fee profit; explicitly subtract its separately recorded fees. No funding/margin leg for spot. Actual maker/taker tiers, spread, latency, market impact and slippage remain unverified/unmodeled, NOT observed zeros.
- BacktestingDataProvider get_price_by_type in backtesting_data_provider.py blob e3d3e087b4da7c0381fac9621d1a04dcb8de81cf can return Decimal("1") for a missing price. For this derivative, **never** use that fallback: require a separately validated real positive close for each fill and mark, otherwise abort. Verify initialized Binance spot trading rules for lot step, min notional, amount precision and balance before accepting any 0.001 BTC fill; no fabricated precision, fill, fee or price.

**Gate 5 boundary:** This is a fully specified, statically mapped **research-only derivative** on a narrow pinned Binance Spot/1d/MARKET-close historical path, not a generic assertion that all Hummingbot fills, all next-open strategies, all markets, or live orders work. No engine run, Qlib parity, backtest or trade occurred in this Scout. Independent Auditor must verify exact-head source facts, path semantics and fee/position ledger. A new unverified execution primitive must receive representative Qlib/Hummingbot event-level parity evidence before mass Qlib screening; HB_READY itself is not profitability or Qlib parity.

## Evidence

### Source-reported

First-party TradingView description (fightpm, 2025-04-09 and updated 2025-06-12) explicitly states 80/1 Bollinger, 200-day slope trend filter, **both** moving averages rising for long entry, upper-rail cross entry, midline cross exit, daily timeframe, **next-open** orders, short mirror and ATR/1%-risk share sizing. No claim that the original Pine code or revision is byte-verified.

### Independently reproduced

Only source-document reading, GitHub policy/main-tree/dedup and pinned Hummingbot **static source inspection** were performed. No strategy backtest, no actual fill replay, no return, no win rate, no fee observation, no wheel rehash, and no Qlib/Hummingbot parity were independently reproduced in this cycle.

### Negative evidence / falsification

The author's next-open fill, ATR-sized risk budget, short leg and zero-brokerage illustrative assumptions are **not** retained. Source performance is not portable to BTC by assumption. Audit exact Bollinger variance/seed, slope equality, upper-cross edge, midline exit, one-bar delayed action, two-clock handling, cash/fee ledger and missing-price fail-closed behavior. Reject this PASS proposal if the claimed pinned historical close path or deterministic state cannot be demonstrated. No hidden default or automatic adaptation is authorized.

## Limitations

No original Pine byte-for-byte proof; the first-party page is mutable, while this derivative identity is frozen to the described 2025-06-12 defaults. Source-native trade timing and sizing are materially changed and could change all trade statistics. No fixed protective stop: a loss can exceed the author's 1%-risk budget. Exchange precision and live fees must be validated against actual rules when used; no claims about real slippage, real fills or funding costs. Only one Binance BTC-USDT spot UTC 1d research path is claimed, not a downstream campaign restriction.

## Implementation status

**not-implemented.** No strategy-specific ControllerV2 has been deployed. The exact state machine, data requirements and pinned simulator path are specified for independent six-gate admission review, not for immediate Qlib execution or trading. HB_READY PASS is an admission proposal, not HB Certified, profitable, survivor, Qlib-parity, Paper, Testnet or Live authorization.

## Adoption boundary

**status: research-only; adoption: not-approved; approval_scope: research-only.** Hermes Auditor GitHub Webhook Review alone owns source-fact remediation, independent exact-head six-gate review, merge or NOT_LOSSLESS close. README bookkeeping after an accepted merge is owned by the existing signed webhook receiver.

## Sources

- fightpm, Daily Bollinger Band Strategy, TradingView, published 2025-04-09, revised 2025-06-12: https://www.tradingview.com/script/h0ePZA90/
- Pinned engine source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior wheel/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
- Canonical admission contract: README.md and .github/HB_READY_REVIEW.md on main 094202e17eb2037f1f099a799945ebe6e4ed42b5.
