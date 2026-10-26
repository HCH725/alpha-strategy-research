---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "connorgeary150 RSI14 cross-up 55 / cross-down 50 momentum — independent BTC-USDT spot 1d long-flat derivative"
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
  - derived
status: research-only
confidence: medium
source_as_of: 2026-02-23
sources:
  - https://www.tradingview.com/script/OMfjRHLz-BTC-Momentum-Trading-RSI-Cross/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RSI14 cross-up 55 / cross-down 50 — independent long-flat momentum derivative

## Provenance and immutable identity

**Primary public TradingView source:** connorgeary150, *BTC Momentum Trading - RSI Cross*, published 2026-02-23, public script ID **OMfjRHLz**: https://www.tradingview.com/script/OMfjRHLz-BTC-Momentum-Trading-RSI-Cross/. Public first-party indexed page content was read on 2026-10-26; it labels the script open-source and gives the following complete **high-level trade predicates**: RSI(14) crosses above 55 to enter long; RSI(14) crosses below 45 to enter short; an existing long closes when RSI crosses below 50; an existing short closes when RSI crosses above 50. The author describes a BTCUSD **10-minute** study for 2026-02-16 through 2026-02-23. These are source-reported facts only. The full executable Pine bytes, publication revision hash, RSI initialization, order-fill flags, sizing, cost, stop and pyramiding properties were **not** accessible from the fetched text. An open-source badge is not proof of having inspected executable Pine.

**Explicitly independent derivative, NOT a source-native Pine reproduction:** preserve only the source-described **long entry** and **long exit** predicates; deliberately disable all short entries and short exits. The researcher independently fixes Binance BTC-USDT **unleveraged spot UTC 1d** rather than the author's 10m BTCUSD chart; Wilder RSI14 seed and exact cross comparisons; completed-bar-close historical MARKET simulation; 0.001 BTC unit, 10,000 USDT starting quote cash, modeled 0.001 per-side fee, 60-bar warmup, pending/fill state, invalid-data handling, no DCA/stop/target, and all execution/accounting rules below. These are deliberate material alterations, not attributed to connorgeary150. No claim of original trade-event equivalence or replicated author statistics.

**Frozen derived identity:** TV:OMfjRHLz:connorgeary150:published-2026-02-23 | derived-v1:2026-10-26 | BinanceSpot:BTC-USDT:UTC1d | WilderRSI14(close):cross-up55-entry:cross-down50-exit | LONG/FLAT:0.001BTC:no-DCA | completed-close-MARKET | 60bar-warmup | trade_cost=0.001-per-filled-side. A changed threshold, RSI seed, timeframe, direction, order timing, risk leg or cost convention is a different research derivative.

**Dedup before writing:** current main snapshot SHA bab14c1d80a1b08bead5e425c88e733a84e74343 contained 361 root-level strategy Markdown files and static README count 361. GitHub connector code search found no script ID OMfjRHLz; ten open research/* PR titles/bodies were inspected and none referenced this source or its rule. Closest records differ materially: RSI Classic 30/60 is an **oversold level** buy / recovery level sell (not 55/50 momentum cross); DRM uses **adaptive-length** RSI and 30/70 edges; connorgeary150's separate 95JBkzXV source is an **RSI<30 AND Bollinger lower-band dip**, with RSI>50 **OR** midline-reclaim exit; Forven RSI momentum requires EMA trend gates and other conditions. This candidate uses a standalone **upward momentum ignition above 55** and an independent **downward midpoint-cross exit**, no BB/EMA/ADX gate. It is not a trivial retuning of an existing source's identical rule. Count equality is not a re-audit of all 361 earlier PASS frontmatters.

## Mechanism

**Source-reported:** trade momentum transitions rather than overbought/oversold fades. Long is opened only on a new RSI14 upward cross of 55; long is closed only on a later RSI14 downward cross of 50. The separate short leg exists in the author's strategy but is disabled here.

**Research hypothesis (not a proven result):** RSI crossing 55 indicates upward strength; crossing back below 50 indicates lost momentum. This derivative tests an asymmetric hysteresis interval (55 entry, 50 exit) on completed daily spot candles. No profitability or risk-adjusted performance is inferred.

## Deterministic signal and state

1. Input is one uninterrupted series of actual, fully completed Binance Spot BTC-USDT UTC **daily** candles with strictly increasing daily-open timestamps exactly 86,400 seconds apart; each O/H/L/C finite and positive, H>=max(O,C), L<=min(O,C), H>=L. Only close enters the RSI. No multi-symbol, lower/higher timeframe, order book, funding, ML or external series.
2. For close C[t], delta[t]=C[t]-C[t-1], gain=max(delta,0), loss=max(-delta,0). At the first 14 valid deltas (t=14), seed avgGain/avgLoss with their **arithmetic mean**. Subsequently use Wilder recursion avg[t]=(13*avg[t-1]+current[t])/14. RSI=100-100/(1+avgGain/avgLoss); if loss=0,gain>0 => 100; gain=0,loss>0 => 0; both zero => 50. No TA-Lib/Pine initialization equivalence is asserted beyond this derivative's fixed definition.
3. **ENTRY** while FLAT and no pending action: RSI14[t] > 55 AND RSI14[t-1] <= 55. Strict current crossing; equality on prior bar is allowed. No entry merely because RSI remains above 55.
4. **EXIT** while LONG and no pending action: RSI14[t] < 50 AND RSI14[t-1] >= 50. Strict downward crossing; equality on prior bar is allowed. No exit merely because RSI remains below 50. No opposite/short order is generated.
5. Evaluate EXIT first only if already LONG at bar start; evaluate ENTRY only if FLAT at bar start. No same-bar entry/exit, reversal, re-entry or repeated order while an action is pending. On fill-confirmed BUY enter LONG(0.001 BTC); on fill-confirmed full SELL become FLAT. If a BUY fails/unfills, return FLAT and wait for a **future fresh entry crossover**. If SELL fails/unfills, keep LONG and latch the exit intent, retrying one full SELL at the next valid completed bar until fill confirmation, even if the cross no longer holds. Do not infer a fill from an action submission.
6. One position only, one pair only, maximum one pending MARKET action. Fixed 0.001 BTC per buy; no pyramiding, partial exit, averaging, DCA, BO/SO, simultaneous positions, shared capital, hedge, leverage, borrowing, short, cooldown, date gate or time-based forced exit. Re-entry is allowed only on a **later fresh upward 55 cross** after confirmed full liquidation. No implicit stop-loss, take-profit, trailing stop, breakeven, volatility stop, intrabar trigger, or forced terminal liquidation. An open position at sample end is marked to the last **observed** close, not falsely booked as realized.
7. **Warmup:** first 60 consecutive, valid, completed 1d bars are flat/no orders; first possible decision is bar 61 (1-based), with RSI[t] and RSI[t-1] valid. On any missing, duplicate, out-of-order or invalid candle, suspend all new decisions and simulated fills; never interpolate or forward-fill missing prices. Resume decisions only after 60 new contiguous valid completed bars. Existing LONG and any unconfirmed pending order remain in the ledger for explicit reconciliation, never silently liquidated.

## Pinned Hummingbot execution and causality — Gate 5

**Pinned benchmark read through GitHub connector on 2026-10-26:** HCH725/hummingbot commit **8b0e067e80ab62f10846d518dcb5a8218527ddb3**, package label **20260920**, file hummingbot/VERSION = **dev-2.17.0**. The source-to-wheel 902/902 byte identity is previously reported in independently reviewed Alpha PR #414; this Scout **did not independently rehash the wheel**.

- Binance SpotCandles source paths: hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py lists **1d**; binance_spot_candles.py::_parse_rest_candles reads the Binance kline's **OPEN timestamp** at row[0] and actual OHLC at row[1..4]. The daily close C[t] is unavailable until effective decision time D[t]=open_timestamp[t]+86,400 seconds. Preserve the raw open timestamp for continuity validation, then normalize the engine decision/fill timestamp to **D[t]**; do not act at the candle's open or treat an incomplete bar as complete.
- Pinned backtesting_engine_base.py::simulate_execution iterates prepared rows, updates controller state, invokes controller.determine_executor_actions, and passes a forward slice **starting at the current row** to the executor simulator. The proposed strategy-specific ControllerV2 (not implemented) emits CreateExecutorAction(OrderExecutorConfig) with connector_name="binance", trading_pair="BTC-USDT", execution_strategy=ExecutionStrategy.MARKET, side=BUY/SELL, amount=Decimal("0.001"), leverage=1, no limit price. OrderExecutorConfig/ExecutionStrategy fields were inspected in the pinned order_executor/data_types.py.
- Pinned executors_simulator/order_executor_simulator.py: MARKET uses the **first actual supplied row timestamp** and that row's **close** as historical fill price, filled_amount_quote=amount*close, cum_fees_quote=trade_cost*filled_amount_quote; close_type=POSITION_HOLD. Thus the derivative's close-effective historical simulation has a concrete supported row-close path, **not** a guarantee of a real post-close exchange fill at the prior close. No maker, next-open, intrabar stop or funding simulation is claimed.
- Pinned backtesting_engine_base.py::BacktestPositionHold nets BUY/SELL in base units, computes weighted average entry and **gross** matched realized PnL, and tracks cum_fees_quote **separately**. A strategy-specific cash/fill-confirmation ledger is needed to enforce unborrowed spot cash and one-position state. Use terminated_executors_window=None so daily POSITION_HOLD fills remain visible to the controller beyond the default one-hour window; the full run ledger and held-position summaries must be reconciled, including last-row fill. Do not treat total_pnl as fee-inclusive net PnL without explicitly subtracting fees.
- Pinned backtesting_data_provider.py::get_price_by_type can return Decimal("1") when a pair key is absent. **Explicitly reject** that fallback and any missing/nonfinite actual candle price; never simulate a fabricated price or fill. Validate original UTC daily continuity **before** any engine dropna/feature preparation. No real venue order-book/partial-fill/precision/min-notional guarantees are inferred from a simulator.

**Research economic convention:** initial cash=10,000 USDT, base inventory=0 BTC, fixed Q=0.001 BTC. Model f=0.001 (0.1%) of actual simulated quote notional **on each confirmed BUY and SELL fill**; this is a declared hypothetical research cost, **not a measured Binance fee**. BUY requires cash >= Q*actual_close*(1+f), then cash -= Q*P*(1+f), inventory += Q. SELL requires confirmed inventory Q, then cash += Q*P*(1-f), inventory -= Q. Matched net realized PnL = Q*(P_sell-P_buy) - f*Q*P_buy - f*Q*P_sell; unrealized equity = cash+inventory*last_actual_close, without inventing terminal SELL fees. Simulator close-price fills assume no additional modeled spread, slippage or latency, which is **not evidence those costs are zero in reality**. Spot is unborrowed and has no perpetual funding contract; no zero-realized-funding claim for futures. Actual exchange fees, partial fills, precision, min notional and executable timing are unverified and require separate authorization/validation.

## Six-gate Scout evidence — independent Auditor must review exact PR head

1. **Determinism:** pinned Wilder RSI14 seed, daily completed close, strict 55/50 crossing semantics, 60-bar warmup and invalid-data rules.
2. **Direction:** one unleveraged Binance BTC-USDT spot long/flat position; source short leg explicitly disabled as derivative.
3. **Entry/exit/risk:** distinct entry cross and exit cross, failed-SELL latch; all stops, targets, trailing and time exits explicitly disabled.
4. **Position/state:** fixed Q=0.001 BTC, cash guard, fill-confirmed FLAT/PENDING/LONG transitions, no DCA/pyramiding/concurrency, future-cross re-entry only.
5. **Engine/data:** pinned real 1d SpotCandles, OrderExecutor MARKET close-row fill, ControllerV2 action path, POSITION_HOLD ledger and modeled fees, with explicit timestamp/fallback/window/cost constraints and #414 wheel-binding precedent.
6. **Causality:** 60 contiguous completed UTC daily candles, only current/prior RSI, effective decision time T+86,400, no future extrema, lookahead, repaint, missing-price substitution or intrabar fills.

**Proposed PASS is a Scout research admission assertion, NOT self-approval.** The independent Hermes Auditor owns source-fact verification, exact-head six-gate PASS merge or NOT_LOSSLESS close. HB_READY is neither profitability nor Qlib parity, Survivor/HB Certified status, executable implementation, or Paper/Testnet/Live permission. Reuse previously verified engine primitives; any new unverified primitive requires one representative Hummingbot/Qlib event-level validation before mass Qlib screening.

## Evidence, limitations and falsification

**Source-reported only:** connorgeary150 reports 1,284 trades, 27.92% profitable, PF 0.886 and 2.13% drawdown on a BTCUSD 10m chart during 2026-02-16..23. **None** is a reproduced result, forecast, or performance assertion for this BTC-USDT 1d derivative. Full Pine source and original execution flags were not obtained; author version metadata beyond public 2026-02-23 publication was not independently frozen.

**This Scout did not run** a TradingView, Qlib or Hummingbot backtest, download market data, perform live execution, validate actual fills/fees or reproduce source PnL. Historical close-price simulation may materially diverge from executable fills, especially on fast signals. Without a stop, a long may remain exposed to an arbitrarily large adverse price move until the specified exit or retry. A gap can delay decisions while exposure persists. The 361/361 count agreement is not proof that every historical record was re-audited for PASS in this cycle.

**Future authorized falsification:** compare this frozen 55/50 momentum hysteresis to separately declared 55/55 or 50/50 exits, and to the full two-sided source concept; do not silently change this immutable derivative or optimize against OOS. Before large-scale Qlib screening of a new execution path, require representative event-level Hummingbot/Qlib parity.
