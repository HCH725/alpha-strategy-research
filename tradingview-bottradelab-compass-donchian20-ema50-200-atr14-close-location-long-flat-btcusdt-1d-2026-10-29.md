---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: BotTradeLab Crypto Breakout Compass B+ entry B- exit derived long-flat BTCUSDT spot 1d
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-29
sources:
  - https://www.tradingview.com/script/Hc39wy0X/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BotTradeLab Crypto Breakout Compass — independently derived B+ entry / B- exit LONG-FLAT BTCUSDT spot 1d

## Provenance

Primary public TradingView open-source indicator listing: **Crypto Breakout Compass**, author **BotTradeLab**, stable ID `Hc39wy0X`, https://www.tradingview.com/script/Hc39wy0X/ ; inspected **2026-10-29**. The page displays **Sep 11** without an explicit year; its own study extends through 2026-09-10, but the publication year is **not independently asserted**. The publicly readable first-party description provides exact default signal inequalities, channel/EMA/ATR lengths, candle-location, extension and shared signal cooldown. Full immutable Pine source bytes were **not** retrieved, and no Pine event-by-event equivalence is claimed.

**Source-native fact:** this is an **indicator, not an order strategy**. It prints B+ and B- markers, expressly supplies **no order entries, exits, stop, target or size**. The source describes a 20-prior-bar Donchian-like channel, EMA50/EMA200 trend alignment and EMA200 five-bar slope, ATR14 volatility and one-ATR extension filters, 70%/30% candle-close location, 10-bar shared signal cooldown, and closed-bar-only decisions.

**Independent derived executable strategy (NOT source-native):** use source-described B+ as a **long entry** and source-described B- as a **long exit**; disable shorting; pin Binance BTC-USDT unleveraged spot UTC **1d**, fixed 0.001 BTC, initial 10000 USDT, deterministic EMA/ATR initialization, exactly 205 previous complete bars of warmup, historical MARKET fill on the **next completed daily bar close**, hypothetical 0.1% per-side fee, no DCA/SL/TP/trailing/time exit, and explicit cash/position/pending-order state. These trading and implementation choices belong to this research derivative, not to BotTradeLab. Replacing the author's *next-open-to-ten-day-close event study* with position-holding B+/B- trades materially changes economic events and is not described as a reproduction.

**Immutable derivative identity:** `TV:Hc39wy0X|BotTradeLab|source-read-20261029|independent-derived-v1-20261029|BinanceSpot-BTC-USDT-UTC1d|prior20-high-low-cross|EMA50-EMA200-slope5|WilderATR14-cap12pct-extension1ATR|close-location70-30|shared-signal-cooldown10|Bplus-buy-Bminus-sell|next-completed-close-MARKET|qty0p001BTC-cash10000USDT-fee0p001|long-flat-noDCA-noSLTP|warmup205prior`.

Dedup at main `094202e17eb2037f1f099a799945ebe6e4ed42b5`: 439 root strategy Markdown files and README counter 439. Connected GitHub main searches for `Hc39wy0X`, `Crypto Breakout Compass` and `BotTradeLab` found no matching record; all-state PR search for `Hc39wy0X` returned none; open research PR titles were inspected. Existing Donchian/channel breakouts do not implement this same **20-prior-bar crossing + EMA50/200 rising-five-bar + ATR cap/extension + close-location + shared B+/B- cooldown** conjunction and its B+ entry/B- exit state. This is a distinct signal qualification mechanism, not a trivial parameter retune. Eleven spread root records were sampled for PASS; this is not an exhaustive 439-file status audit.

## Economic mechanism

### Source-reported

A price-channel breakout is considered more convincing when long-term EMA alignment/slope, limited ATR volatility, bounded breakout extension and a strong candle close agree. The author's 2024-2025 event study reports mixed outcomes and expressly disclaims portfolio-level fills, stops, leverage and realized costs; none of those numbers are adopted as verified profitability.

### Research interpretation

Hold a single spot long only after a qualified bullish breakout, then liquidate only after a separately qualified bearish breakout. This is an intentionally slow, potentially high-drawdown trend-following hypothesis. Because B- needs a bearish EMA regime and is subject to the shared cooldown, the exit may occur very late or never within a sample. No protective stop is implied.

## Signal

Only **contiguous, fully completed** UTC daily Binance spot OHLCV bars. Index `t` is the latest complete bar; `t-1` and earlier are available at decision time. Reject NaN, infinite, missing, zero/negative OHLC, invalid high/low geometry, negative volume or timestamp gaps. No future values, intrabar execution or external series.

- `U[t] = max(high[t-20] ... high[t-1])`; `L[t] = min(low[t-20] ... low[t-1])`. The current bar is **excluded**. For the preceding crossing test use `U[t-1]` and `L[t-1]` computed from their own 20 preceding bars.
- `EMA_N` is recursively `alpha=2/(N+1)`, seeded at its first valid observation with SMA of the first N closes, then updated only on completed closes. Compute `E50[t]`, `E200[t]`, and `E200[t-5]`. This seed choice is **researcher-defined**, not an assertion about inaccessible Pine initialization.
- `TR[t]=max(high[t]-low[t],abs(high[t]-close[t-1]),abs(low[t]-close[t-1]))`; `ATR14` is Wilder RMA seeded with SMA of the first 14 valid TR values and updated by `(13*previous+TR[t])/14`. `ATR[t]>0` is mandatory. No invented zero ATR.
- For `high[t]>low[t]`, `CL[t]=(close[t]-low[t])/(high[t]-low[t])`. Zero-range bars have neutral `CL=0.5` and cannot pass either default strength filter; reject inconsistent OHLC.
- Shared prerequisites: `ATR[t]/close[t] <= 0.12`, finite indicators, warmup complete, and `last_marker` absent or `t-last_marker >= 10`. `last_marker` tracks **all emitted B+/B- indicator markers**, independent of position, and is updated on each qualifying marker. A rejected setup is not queued or retroactively admitted.
- **B+ marker** at complete `t` iff `close[t]>U[t]` AND `close[t-1]<=U[t-1]` AND `close[t]>E50[t]>E200[t]` AND `E200[t]>E200[t-5]` AND `CL[t]>=0.70` AND `0<close[t]-U[t]<=ATR[t]`, plus shared prerequisites.
- **B- marker** at complete `t` iff `close[t]<L[t]` AND `close[t-1]>=L[t-1]` AND `close[t]<E50[t]<E200[t]` AND `E200[t]<E200[t-5]` AND `CL[t]<=0.30` AND `0<L[t]-close[t]<=ATR[t]`, plus shared prerequisites.
- B+ and B- cannot simultaneously qualify for valid candles. Strict inequalities are strict; ATR cap, extension bound and candle-location bounds are inclusive as written. No arbitrary alternate signals, retracement entry or delayed requalification.

**Derived trading rule:** if FLAT and no pending action, B+ at t queues one BUY for completed bar t+1. If LONG and no pending action, B- at t queues one full-quantity SELL for completed bar t+1. While LONG, ignore B+ for trading (but count it for the indicator's shared cooldown); while FLAT, ignore B- for trading (but count it for cooldown). No other exits. Marker cooldown is **not** a separate post-exit trading cooldown; re-entry requires a fresh B+ and no pending/held position. No short position or reversal order.

## Required data

Single `binance` BTC-USDT spot `1d` OHLCV stream with UTC-aligned, gap-free daily open timestamps. Validate OHLC geometry and finite positive actual close before every fill; base volume is present but not a signal input. Binance REST `/api/v3/klines` row[0] is candle **open** timestamp, not a decision timestamp. Use effective event time `open_timestamp+86400` for each completed UTC daily candle, excluding the currently forming day. A signal using t is not available before t's effective close; a queued action cannot fill before t+1's effective close.

Warmup requires **205 completed previous daily bars** before the first eligible signal (index t>=205 with zero-based indexing). On a gap, invalidate/reset indicators and marker state; do not emit/fill new orders until 205 fresh contiguous prior bars are available. A pending order whose next bar is missing is cancelled without a fictitious fill. An existing long remains exposed during data outages; never invent a price, liquidation or stop. Resume a valid B- exit only after signal state is warm again. The source's own indicator says at least 205 prior bars; researcher-defined seed choices and all trading assumptions are disclosed.

## Execution assumptions

**Pinned Hummingbot path inspected via connected GitHub:** package `20260920`, `hummingbot/VERSION=dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. Directly inspected `backtesting_engine_base.py`, `backtesting_data_provider.py`, `executors_simulator/order_executor_simulator.py`, Binance spot candles `binance_spot_candles.py` and `constants.py`, and `order_executor/data_types.py`. `setup.py` says `20260729`, **not** the reported packaged distribution version; previous independent PR #414 reports 902/902 wheel Python files byte-identical to this source and package `20260920`. Wheel bytes were **not** rehashed in this cycle. Auditor must verify the prior binding if necessary.

**Supported bounded simulation model:** `BinanceSpotCandles` supports `1d` and REST OHLCV; a strategy-specific `DirectionalTradingController` can emit `CreateExecutorAction(OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY or SELL,amount=Decimal("0.001"),execution_strategy=MARKET,leverage=1))`. `BacktestingEngineBase.simulate_execution` processes per-row controller actions. `OrderExecutorSimulator` MARKET uses **first supplied row's actual close**, with `filled_amount_quote=amount*close` and `cum_fees_quote=trade_cost*filled_amount_quote`, terminating as `POSITION_HOLD`. To implement the declared **t signal → t+1 completed-close fill**, controller must retain t's signal and emit the MARKET action on the next **completed** row only, with effective close timestamps aligned for both features and execution rows. No same-signal-bar close fill or assumed next-open capability.

**State and accounting:** `FLAT -> PENDING_BUY -> LONG -> PENDING_SELL -> FLAT`; one confirmed full-size position and at most one queued order, no pyramiding, BO/SO, DCA, scale-out, simultaneous orders, partial fills or same-fill-bar re-entry. Process pending fill before evaluating new signals; no signal can create a second action on a fill bar. `BacktestPositionHold` nets MARKET BUY and SELL `POSITION_HOLD` fills by quantity and average cost. Confirm unique executor/fill IDs and reconcile actual close price, 0.001 BTC inventory and cumulative fees; do **not** infer position from a truncated terminated-executor view. Use `terminated_executors_window=None` or independent persistent fill-state, and include the engine's final POSITION_HOLD flush. PnL must subtract `cum_fees_quote` from realized quote PnL; `summarize_results.net_pnl_quote` alone is not treated as fee-net without reconciliation.

**Economics:** starting cash 10000 USDT; on BUY, require `cash >= 0.001*actual_fill_close*(1+0.001)` and debit notional plus modeled fee; on SELL require exactly 0.001 BTC confirmed inventory and credit `0.001*actual_fill_close*(1-0.001)`. `trade_cost=0.001` per fill is **hypothetical research taker fee**, not observed Binance fee. Model assumes no additional slippage because this simulator uses candle close, **not** because actual fills have zero slippage. No futures, margin, borrowing, leverage, liquidation or perpetual funding: spot has no perpetual funding cashflow. Venue precision/min-notional/lot size and actual fillability are **not** verified; no live authorization. The provider's `get_price_by_type` can default to `Decimal("1")`: this is **forbidden** for this strategy; require validated real bar closes and fail closed on missing prices. No hidden synthetic price or fee.

## Evidence

### Source-reported

The primary source precisely describes B+/B- channel crossing, EMA50/200 alignment and five-bar EMA200 slope, ATR14 <=12% of close, <=1 ATR extension, 70%/30% close location, 10-bar shared marker cooldown, at least 205 prior bars and closed-candle causality. The page explicitly states that this is an indicator without order rules. Its historical directional event study is **not** an independent strategy backtest.

### Independently reproduced

**Not independently reproduced.** The pinned engine source path and deterministic formula/position mapping were inspected, but no candidate strategy run, actual wheel rehash, Hummingbot/Qlib parity, fee/funding realization or source-Pine event replication occurred. Prior PR #414's independent wheel/source proof is cited rather than misrepresented as work repeated here.

### Negative evidence

No source-native order execution or 10-bar event-study equivalence; B+ buy/B- sell and fixed quantity/cost/next-close fill are researcher-derived. EMA and ATR seed choices may differ from Pine. No protective stop, TP, trailing, time exit, DCA or shorts. B- can arrive too late, cooldown can suppress an otherwise valid B- exit, and prolonged long exposure can lose most of invested notional. No live precision/fill/fee, backtest performance or profitability claims.

## Falsification plan

Future separate research may compare this exact frozen B+/B- holding rule against the source's directional 10-day event window, a bare 20-bar channel crossover and a version without close-location/ATR extension filters, keeping costs and event timing consistent. Report every skipped marker, exit latency, flat exposure, unrealized loss, drawdown and modeled fees. New execution primitives require one representative Qlib/Hummingbot event-level capability parity check before mass Qlib screening. **No tests executed in this Scout cycle.**

## Crypto portability

Frozen candidate: BTC-USDT Binance spot UTC daily, LONG/FLAT. Source studied multiple crypto USD series; that is **not** evidence of venue portability. Other pairs, intervals, shorting, futures and DCA are separate disclosed downstream research experiments, not admission prerequisites.

## Limitations

Full immutable Pine bytes not obtained; only the public author's decision-critical default signal description was read. This is an independently specified **derived** trading strategy, not source-native Pine reconstruction. No executable controller exists yet; source inspection demonstrates a compatible bounded engine path, not an implemented strategy or tested market execution. Raw candle timestamps require explicit close-time alignment. The version string in source setup.py differs from the reported wheel package; wheel/source mapping rests on prior PR #414. No guarantee of loss limit, profitability, fills, or Qlib parity.

## Implementation status

`not-implemented`. Proposed `hb_ready_status: PASS` is a Scout six-gate **submission**, subject to independent Hermes Auditor review of source facts, exact pinned engine path, fill timing, ledger and costs. No approval for live use and no dedicated strategy-specific implementation is asserted.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. No merge, backtest, Qlib/Hummingbot run, trade, cron or environment changes in this Scout.

## Related Wiki records

None; no Wiki change.

## Sources

- https://www.tradingview.com/script/Hc39wy0X/
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- https://github.com/HCH725/alpha-strategy-research/pull/414
