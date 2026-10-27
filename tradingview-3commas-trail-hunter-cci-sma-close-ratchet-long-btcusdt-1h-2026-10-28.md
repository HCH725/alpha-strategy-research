---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "3Commas Trail Hunter SMA24/31 CCI11 close-ratchet long-flat BTC-USDT 1h (independent derivative)"
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-28
sources:
  - https://www.tradingview.com/script/d117dN6D-3Commas-Trail-Hunter-Reversal-Long/
  - https://www.tradingview.com/script/Qgoi5jEL-3Commas-Trail-Hunter-Indicator/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# 3Commas Trail Hunter dual-cross close-ratchet — independent research derivative

## Provenance and frozen identity

**Primary TradingView source:** 3Commas, *[3Commas] Trail Hunter - Reversal Long*, public open-source **strategy**, script ID `d117dN6D`, first-party publication read 2026-10-28: https://www.tradingview.com/script/d117dN6D-3Commas-Trail-Hunter-Reversal-Long/ . TradingView displays **May 12** for publication/update but does not expose the year in the retrieved page text; the author's cited reference study ends **2026-05-12**. No unverified publication year, original Pine revision hash, or source-code identity is claimed. The full Pine source bytes were **not** retrieved; only the detailed first-party description and defaults were verified. The companion open-source **indicator**, `Qgoi5jEL`, independently describes the same signal framework; it is **not** claimed to place trades.

**Source-native facts, not independently reproduced:** The author's 1h long-only framework uses an SMA(24) cross **below** SMA(31) and CCI(11) cross **below -80**, AND-aligned within a default three-bar keep-alive window. Source exits are a **price/high-based** trailing take-profit activated at +1.5% with 0.05% deviation, or an intrabar -3.25% hard stop; one entry per cycle, no safety orders. The author's reference is COINBASE:BTCUSD 1h, 41.55858 quote-currency base order, 0.055% commission and 5-tick slippage. These original fills, fees, backtest statistics and source event sequence have NOT been reproduced or inherited.

**Explicit independent derivative, NOT source-native/lossless:** Preserve the distinctive SMA/CCI dual-cross and three-bar confluence, but deliberately (1) pin the CCI source to HLC3 and its precise formula, (2) use Binance BTC-USDT **spot 1h**, (3) use fixed **0.001 BTC** per trade and 10,000 USDT initial unborrowed cash, (4) replace the source's **intrabar high-based trailing and stop fills** with fully specified **completed-close** signal thresholds and historical MARKET-close fills, (5) replace the source's cost model with **hypothetical 0.1% per filled side** and no simulated impact, (6) define warmup, gap-failure, latch-reset and event priority below, and (7) disable date limits, webhook/DCA-bot integration and any unspecified order feature. These changes materially alter trade events and economics; no TradingView parity or profitability is claimed.

**Immutable derivative identity:** `TV:d117dN6D:3Commas:public-description-inspected-2026-10-28 | independent-derived-v1:CCI-HLC3-11:SMA24x31:CCI-cross-below-minus80:AND-3completed-bars | close-only-stop3.25pct:activation1.5pct:close-peak-trail0.05pct | BinanceSpot:BTC-USDT:UTC1h:LONG-FLAT:Q0.001BTC | Hummingbot-MARKET-close:cost0.001-per-side | warmup64`. Any altered source facts, indicators, thresholds, market, event order, price convention or cost constitutes a different derivative.

## Economic mechanism

Falsifiable hypothesis only: simultaneous exhaustion of a fast-versus-slow SMA regime and a negative CCI extreme may identify a short-term long mean-reversion entry. A completed-close profit ratchet may capture rebound persistence but **does not** implement the source's protective intrabar trail. No evidence of positive expectancy is asserted.

## Signal — fully defined derived rules

- Input: exactly one Binance BTC-USDT **spot 1h UTC** OHLCV series. Candle `t` is labeled by **open** timestamp `T[t]`, closes and becomes available at `T[t]+3600` seconds. Use only **completed** candles. Require consecutive hourly timestamps, finite OHLCV, `high>=max(open,close)>=min(open,close)>=low>0`, `volume>=0`. Any missing, duplicate, non-hourly, NaN, nonpositive price or otherwise invalid bar **aborts the research run**; do not interpolate, forward-fill or invent a trade price.
- `SMA24[t]` and `SMA31[t]` are arithmetic means of the latest 24 and 31 completed **closes** respectively. `maCross[t]=(SMA24[t-1]>=SMA31[t-1]) AND (SMA24[t]<SMA31[t])`; strict current inequality, prior equality qualifies.
- `typical[t]=(high[t]+low[t]+close[t])/3`. `mean11[t]=sum(typical[t-i],i=0..10)/11`; `mad11[t]=sum(abs(typical[t-i]-mean11[t]),i=0..10)/11`; `CCI11[t]=(typical[t]-mean11[t])/(0.015*mad11[t])`. If `mad11[t]=0`, CCI is undefined and no CCI cross can fire. This HLC3, mean-absolute-deviation variant is a **researcher pin**, not a verified original Pine default.
- `cciCross[t]=(CCI11[t-1]>=-80) AND (CCI11[t]<-80)`, only when both CCI values are defined. Strict current threshold, prior equality qualifies. A zero-deviation bar invalidates the comparison but not the entire run.
- While FLAT, store the latest completed `maCross` and `cciCross` bar indices, if any. A **fresh dual-confluence event** fires on bar `t` only when **at least one** of the two crosses occurs **at t** and both last-cross indices are in `{t,t-1,t-2}`. This is the declared interpretation of a **three-bar inclusive** window; no repeated signal solely because two old latches remain true. Latches expire after two subsequent bars and are cleared on entry or exit.
- **Warmup:** consume at least **64 consecutive completed 1h bars** before the first signal; no entry during warmup. Lookbacks include only current and earlier completed bars. Start FLAT with no armed latches. No historical pre-warmup signal is carried forward.
- **Entry:** when FLAT and fresh dual-confluence occurs, issue exactly one BUY for **0.001 BTC** at the completed signal bar's **close** under the pinned historical MARKET-close simulation. Confirm fill; set LONG, `entry_price=close[t]`, `trail_armed=false`, `peak_close=undefined`; clear both latches. The entry bar is **not** evaluated for stop or trailing exit.
- **LONG stop:** on each subsequent completed candle, **first** test `close[t]<=entry_price*(1-0.0325)`. If true, SELL all 0.001 BTC at that completed close, clear trailing state and latches, return FLAT. This is a **close-triggered loss signal**, NOT an exchange protective stop or a guarantee of maximum -3.25% realized loss.
- **LONG profit ratchet:** only if stop did not fire: if not armed and `close[t]>=entry_price*(1+0.015)`, arm the trail and set `peak_close=close[t]`; do **not** exit on the activation bar. On each **later** completed candle while armed, first set `peak_close=max(previous_peak_close,close[t])`, then if `close[t]<=peak_close*(1-0.0005)`, SELL all 0.001 BTC at the same completed close, reset state to FLAT and clear latches. Equality triggers exit. A new peak cannot simultaneously trigger a retrace.
- **State/priority:** stop precedes ratchet, exit precedes any entry consideration. Ignore both cross signals while LONG. After a full exit, no same-bar re-entry; future entry requires fresh post-exit dual crosses. One spot long or flat only; no short, pyramiding, averaging, DCA/safety orders, partial fills, partial take-profit, timed cooldown, forced final liquidation, independent intrabar high/low touch, exchange stop/trailing order, maker/limit, leverage, margin, funding, cross-asset state or portfolio shared-capital allocation. No terminal trade is fabricated if LONG at the last bar; mark the open position at the last close for reporting.
- On any missing/failed MARKET fill, insufficient **modeled** cash, nonfinite fee/price, or position-book mismatch outside the tolerance below, **abort the run** rather than inventing an order, cash balance, or missing price. No optimization or parameter search is performed in this record.

## Execution assumptions — demonstrated pinned-engine path and bounded model

**Pinned benchmark:** Hummingbot package `20260920`, `hummingbot/VERSION=dev-2.17.0`, GitHub repository `HCH725/hummingbot` at immutable commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`. The following real code paths were read via GitHub on 2026-10-28; this is **static capability evidence**, not a strategy backtest:

1. **Data/clock:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` declares `1h`; `binance_spot_candles.py` maps Binance `/api/v3/klines` open-time `row[0]` and OHLCV `row[1..5]` (websocket `k.t/o/h/l/c/v`). `backtesting_engine_base.py` exposes `open_bt/high_bt/low_bt/close_bt/volume_bt` as processed candle columns. SMA, CCI and close-only ratchet need no hidden feed or unsupported higher/lower-frame synchronization.
2. **Controller/executor:** `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` iterates `update_state(row)`, `controller.determine_executor_actions()`, `CreateExecutorAction`, then `simulate_executor`. A **strategy-specific, not-yet-implemented controller** can hold the explicitly defined latches and trailing-close peak, issuing `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=BUY/SELL, amount=Decimal("0.001"), execution_strategy=MARKET, leverage=1)`. This is a research expressibility argument, **not** a claim that an executable controller already exists.
3. **Fill and causal clock:** `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` chooses the **first supplied candle** for MARKET, fills at its `close`, records `filled_amount_quote=float(amount)*close`, charges `trade_cost*filled_amount_quote`, and returns `CloseType.POSITION_HOLD`. `backtesting_engine_base.py` aggregates those holds. The raw simulator `fill_timestamp` is the candle's **open-time label**; all derivative decisions/fills are explicitly reported at **open timestamp + 3600 seconds**, never represented as available at candle open. Same-close fills are a **historical zero-latency modeling convention**, not an achievable post-close exchange guarantee; there is no next-open, maker, high/low touch or external stop primitive hidden in this derivative.
4. **Spot position and research costs:** Initial modeled cash **10,000 USDT**, position either **0** or **0.001 BTC**. A BUY at price `p` reduces exact Decimal research cash by `0.001*p*(1+0.001)`; a SELL increases it by `0.001*p*(1-0.001)`. The fixed **0.1% per-side fee is a hypothetical research input**, not the source's 0.055% or verified Binance fee. `trade_cost=0.001` is passed to the simulator. Realized net quote PnL = sell proceeds minus buy cost; open equity = cash + 0.001*last_close. The pinned `BacktestPositionHold` computes gross matched PnL and accumulated quote fees; reconcile both with this independent exact-Decimal cash/inventory ledger. Spot funding is **not applicable**, not a fabricated realized zero-funding stream. No margin or liquidation.
5. **Float/Decimal caveat and fail-closed bound:** `OrderExecutorSimulator` uses float for filled quote, while `BacktestPositionHold.add_executor` converts filled quote back to base quantity by division and `is_closed` tests exact zero. Consequently a tiny engine residual is possible even after equal 0.001 BTC BUY/SELL. The derived controller must use its **explicit confirmed-order 0/0.001 BTC state**, never infer re-entry eligibility solely from the engine's exact-zero `positions_held` flag. On each fill reconcile engine net base with exact research inventory, and engine gross PnL/fees with Decimal ledger, allowing at most **1e-10 BTC base residual** and **1e-6 USDT quote rounding discrepancy**; larger deviations, negative modeled cash or an unaccounted fill **abort**, not silently reclassify exposure. These are **research diagnostic bounds**, not claims of exchange lot precision or a fix to the engine.
6. **Capability boundary:** This path models completed 1h OHLCV, one spot pair, historical MARKET-close fills and quote-fee accounting only. It does **not** verify exchange tick/lot/min-notional rules, real order acceptance, market liquidity, actual commission tiers, slippage, partial fills or live trail/stop execution. Simulator modeled price impact/slippage is absent; that is **not** evidence that actual slippage is zero. The source's 5-tick slippage and intrabar exit outcomes are deliberately **not** carried over. If any of these unmodeled capabilities becomes materially required, Gate 5 must be reassessed before research expansion.

## Six-gate admission evidence (subject to independent Hermes Auditor)

1. **Determinism:** exact SMA/CCI equations, 3-bar latch window, strict comparisons, CCI zero-denominator behavior, 64-bar warmup, trailing close-peak update order, missing-data fail-closed and all parameters frozen.
2. **Direction:** Binance BTC-USDT spot LONG/FLAT; short, leverage and margin disabled.
3. **Entry/exit/risk:** dual-cross entry, completed-close -3.25% stop, +1.5%-armed 0.05% close-peak retrace, stop-first priority, no undeclared protective/exit orders.
4. **State:** exact 0.001 BTC, one position, no DCA, no stacking, latch clearing, no same-bar re-entry, no fixed cooldown, final open position unliquidated.
5. **Pinned compatibility:** verified `1h` Binance spot feed, actual controller/action/MARKET/POSITION_HOLD path, candle-open timestamp normalization, research fees, Decimal ledger plus engine reconciliation and fail-closed precision diagnostics; no unsupported intrabar fill primitive assumed.
6. **Causality:** completed bars only; decision timestamp at 1h close; no future reads, repainting, full-sample fit, incomplete higher-timeframe bar or synthetic price; same-close simulator assumption explicitly bounded as historical research only.

## Dedup, negative evidence, and downstream boundary

- GitHub main snapshot `2245b98f4d5603421938df0e894e6ae5ba7722a1`: **392** root-level strategy Markdown records; README count **392**. The newest added Oberon record and selected existing frontmatters were read as PASS; a matching count is **not** a fresh full-file status audit. No same TradingView source ID `d117dN6D` or `Qgoi5jEL` appeared in current main code search; current open `research/*` PRs and search for this mechanism/source showed no duplicate.
- A separate existing 3Commas **dual-RSI/DCA** record is a different source and mechanism; a generic CCI threshold-cross or MA crossover alone is **not** this three-bar SMA/CCI conjunction with post-activation close-ratchet.
- **Negative evidence:** no complete original Pine bytes, no immutable original Pine revision, no original order-fill or intrabar path verified. The author's reference statistics are **not independently reproduced**; no backtest was run. This derivative's stop can exceed 3.25% loss after a gap, and 0.05% completed-close trailing can behave radically differently from the source's intrabar high-based trailing. PASS here is the researcher's **six-gate submission claim**, not independent approval, implementation, Qlib parity, Survivor, profitability or Paper/Testnet/Live authorization.
- A representative Qlib/Hummingbot event-level parity check is required **before mass screening of any new/unverified execution primitive**, not as an invented seventh admission gate. Independent Hermes Auditor must verify source facts and all six gates at the exact PR head before any merge. No trading, backtest, deployment or scheduling change is requested.
