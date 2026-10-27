---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TS_Indie W%R14 EMA20/50 pullback with close-triggered 2R bracket BTC-USDT spot 4h independent derivative
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-11-22
sources:
  - https://www.tradingview.com/script/D9dkKBUh-W-R-Pullback-EMA-Trend-TS-Indie/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TS_Indie W%R pullback / EMA dual-trend close-bracket — independent derivative v1

## Provenance

**Primary public TradingView source:** Truth_Strategy_Indie, *W%R Pullback+EMA Trend [TS_Indie]*, stable public script ID **D9dkKBUh**, originally published **2025-11-08**, updated **2025-11-22** (TradingView first-party description and release notes inspected 2026-10-27): https://www.tradingview.com/script/D9dkKBUh-W-R-Pullback-EMA-Trend-TS-Indie/ . The page labels the script open-source, but its **complete Pine code and property defaults were not retrieved**. No source-native/lossless Pine equivalence is asserted.

**Verified source-described decision rules, not researcher inventions:** For long entry, the author's fast EMA must exceed the slow EMA; previous-bar Williams %R must have been below -80 and current-bar %R must cross back above -80; close must exceed the fast EMA. The author describes entry at the signal-bar close, a stop at the lower of the current/previous candle lows, and a target at entry plus a configurable multiple of entry-to-stop distance. The source separately describes a short-side -20 recross, a stop at the higher of two highs, optional ATR stop buffer, adjustable EMA/W%R periods, configurable sessions/dates and a risk/reward input. The visible description **does not establish** the EMA lengths, W%R length, risk/reward default, exact Pine calculations, actual historical fills, fees, or strategy order-state defaults.

**Explicitly independent researcher-defined executable derivative:** Freeze Binance BTC-USDT **spot 4h**, LONG/FLAT only; EMA(20)/EMA(50), W%R(14), strict -80 recovery, fixed 2R target, the described two-candle-low stop anchor, **completed-close threshold exits instead of exchange/intrabar protective orders**, a one-bar-later **next-bar-close historical MARKET fill**, 0.001 BTC per trade, and a declared 0.02% modeled fee per filled side. Disable shorts, ATR stop buffer, session/date gating, source close-of-signal fill, intrabar stop/target and all unspecified features. These are deliberate **derived changes**, not purported source defaults.

**Immutable candidate identity:** `TV:D9dkKBUh | TSINDIE-DERIVED-V1-20261027 | BINANCE-BTC-USDT-SPOT-UTC4H | EMA20-50-SMA-SEED | WPR14-RECROSS-80 | 2R-CLOSE-BRACKET | NEXT-BAR-CLOSE | 0.001BTC | FEE0.0002`. Altering any named rule, direction, fill, market or sizing creates a different research candidate.

## Signal

**Single source of data and clock:** One actual Binance BTC-USDT spot 4h UTC OHLCV series, indexed `t=0,1,...` with strictly increasing **14,400-second contiguous candle-open timestamps** `T[t]`. Candle `t` is complete only at `T[t]+14400`. All O/H/L/C must be finite and positive, H >= max(O,C), L <= min(O,C), V finite and nonnegative. No interpolation, synthetic prices, current unfinished candles, or future bars.

**Pinned researcher mathematics (not claimed as the source's exact Pine internals):**

1. `EMA_n[n-1] = mean(C[0..n-1])`, for `n in {20,50}`; for `t>=n`, `EMA_n[t] = (2/(n+1))*C[t] + (1-2/(n+1))*EMA_n[t-1]`. Undefined before the seed.
2. `HH14[t]=max(H[t-13..t])`, `LL14[t]=min(L[t-13..t])`, `WPR14[t]=-100*(HH14[t]-C[t])/(HH14[t]-LL14[t])` if `HH14>LL14`; otherwise undefined. No epsilon substitution.
3. `RECOVER[t]=(WPR14[t-1]<-80 && WPR14[t]>-80)`. Both strict comparisons are frozen; equality is **not** a signal. `TREND[t]=(EMA20[t]>EMA50[t] && C[t]>EMA20[t])`. `BUY_SIGNAL[t]=RECOVER[t] && TREND[t]`.
4. Warmup: require **80 contiguous fully completed valid candles**, valid EMA20/50 and valid current/prior WPR14 before any decision. Initial state `FLAT`, no inherited inventory. An undefined required value after warmup invalidates the research run; do not invent a zero oscillator or forward-fill.
5. **FLAT state:** on `BUY_SIGNAL[t]` at the completed close of `t`, remember `anchor=min(L[t-1],L[t])` and schedule one BUY of exactly `0.001 BTC` on the **following candle `t+1`** using the pinned simulator's MARKET-at-first-row-close convention. No action if there is no actual next candle. The order is created on row `t+1` using **only features through t**; no current-row close may influence the decision. At confirmed modeled BUY fill `Pbuy=C[t+1]`, require `Pbuy>anchor`; otherwise mark the sample **non-claimable** and STOP rather than silently change the stop or pretend a trade was skipped. Freeze `SL=anchor` and `TP=Pbuy+2*(Pbuy-anchor)`.
6. **LONG state:** after a confirmed BUY, evaluate completed candles `j>=t+2` in order. If `C[j]<=SL`, schedule a full 0.001 BTC SELL on the next candle `j+1` at its modeled close. Otherwise if `C[j]>=TP`, schedule the same SELL. Stop has priority (a single close cannot satisfy both positive-distance brackets). Otherwise hold. These are **close-triggered exit signals**, not intrabar touches, resting protective orders, guaranteed stop prices or fills at SL/TP. A gap can make the actual simulated exit price materially worse/better than the trigger level.
7. **Order/state machine:** at most one pending action and one position. A BUY or SELL request never changes inventory by itself; only a confirmed full `POSITION_HOLD` modeled fill updates FLAT/LONG. A missing, rejected, failed, partial or zero-price fill makes the research sample **non-claimable**, with no phantom position, retry, or fabricated price. After a SELL fill, return to FLAT; re-entry requires a **fresh later** WPR recross and a new trend check. No same-candle exit/re-entry, no pyramiding, no cooldown beyond this new-edge requirement. An exit while flat is a no-op.
8. **End-of-sample:** if a position remains open or an exit signal occurs without a real next candle, do not invent a liquidation SELL; record remaining quantity and unrealized gross PnL at the last actual valid observed close, separately from accumulated entry fees. No terminal return claim from a fictional fill.
9. **Explicitly disabled:** SHORT, futures/perpetuals, leverage, margin, funding, BO/SO/DCA, averaging, partial fills, compounding, multiple positions, shared portfolio capital, intrabar/next-open/maker/limit execution, ATR buffer, trailing stop, time exit, additional trend-loss exit, session/date gate, end-of-sample liquidation, and hidden Hummingbot stop/target defaults. There is **no intrabar protective stop**. A missing/duplicate/out-of-order candle aborts the research sample rather than bridging a gap.

## Required data

Only actual Binance spot BTC-USDT **4h OHLCV** and its UTC candle-open timestamps. H/L/C drive WPR, EMA uses C, and the stop anchor uses two known lows. O and V are validated but do not gate orders. No multi-timeframe, cross-symbol, order-book, mark/index, fitted ML, news, open-interest or funding input; no source backtest table is an input. The author's original gold/5m examples are **not** the market/timeframe of this derivative.

## Execution assumptions

**Gate 5 — actual pinned Hummingbot source path inspected via GitHub connector:** Hummingbot package `20260920`, VERSION `dev-2.17.0`; pinned source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` with `hummingbot/VERSION` read as `dev-2.17.0` on 2026-10-27. Package/image digest equivalence to that source commit is **not independently established**; this is a bounded source-path capability claim, not a verified deployed binary.

- **Feed/market:** `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` parses actual Binance `/api/v3/klines` timestamps, O/H/L/C/V; its pinned `constants.py` includes `4h`. Use `connector_name=binance`, `trading_pair=BTC-USDT`, `interval=4h`, spot only. No short or leverage route is assumed.
- **Controller/executor:** A strategy-specific `ControllerBase` implementation would compute the frozen lagged signals and `determine_executor_actions` would return `CreateExecutorAction(OrderExecutorConfig(...))`: `ExecutionStrategy.MARKET`, `TradeType.BUY` + `PositionAction.OPEN` on entry, `TradeType.SELL` + `PositionAction.CLOSE` on exit, `amount=Decimal("0.001")`, `leverage=1`. No controller has been implemented in this Scout. `BacktestingEngineBase.run_backtesting` → `prepare_market_data` → `update_state` → `determine_executor_actions` → `simulate_executor` → `OrderExecutorSimulator.simulate` is directly present in the pinned source. The simulator's MARKET path fills the **first supplied candle row at its actual `close`**, emits `CloseType.POSITION_HOLD`, and accumulates quote fees; this is the declared historical close-fill model, **not** a live executable quote guarantee.
- **Time availability:** Binance Kline `timestamp` is the **bar open**, while `prepare_market_data` uses backward `merge_asof` on those raw timestamps. A correct controller MUST shift decision inputs by one complete 4h bar: on engine row `t+1`, use only `t` and earlier completed candles; never read `close_bt` for `t+1` as a signal or for sizing. A MARKET order created at row `t+1` is simulated at that row's close; report the effective fill time `T[t+1]+14400`, **not** the row's opening label. Same lag applies to exit triggers. A controller that consumes current-row close as already known at row-open time is **not compatible**.
- **Position ledger:** `BacktestPositionHold` in `backtesting_engine_base.py` nets filled BUY/SELL base quantity, weighted cost and realized gross quote PnL, while retaining `cum_fees_quote` separately. Set `terminated_executors_window=None` or equivalently preserve the complete fill-confirmed ledger; the default 3600-second terminated view is shorter than 4h and is insufficient as the sole state source. Use confirmed fills, not submitted orders, for position state. The engine does not establish a real exchange wallet/cash solvency constraint; no account-level performance or live order-size approval is claimed.
- **Prices and economics:** Require an actual finite positive candle close for every modeled fill; **never** accept the provider's `get_price_by_type` fallback `Decimal("1")` as a missing BTC price. Pin `run_backtesting(trade_cost=0.0002)`: hypothetical **0.02% per filled side**, `fee_quote=0.0002*0.001*Pfill`. For a fully closed trade, modeled net quote PnL is `0.001*(Psell-Pbuy)-0.0002*0.001*(Pbuy+Psell)`. Gross `pnl_timeseries` is not silently net-of-fee. Spot funding is **not applicable**, not an assumed zero futures funding rate. Slippage, spread, partial fills, exchange lot/tick/min-notional, actual account fee tier and executable close prices are **unverified/not simulated**, never described as real zero costs.
- **Capability boundary:** This derivative needs only the inspected single-spot-asset 4h candle, delayed completed-bar decision, MARKET historical close-fill and POSITION_HOLD ledger route. It does **not** require unverified intrabar bracket, maker queue, next-open, multi-asset synchronization, perpetual funding or real protective stops. If the controller cannot enforce the lag, fee ledger, fill-confirmed state or valid-price guard, Gate 5/6 fails in implementation; PASS here is a research-specification proposal subject to independent audit.

## Evidence

**Source-reported:** The first-party TradingView page supplies EMA-fast/slow trend, -80 Williams %R recovery, close-above-fast entry, two-candle-low long stop, configurable RR target, short counterpart, and optional ATR/session/date/period choices. It does **not** supply the pinned numeric periods/RR, exact Pine internals, source fill record, or a validated crypto backtest. None are attributed to the author.

**Independently reproduced:** None. No TradingView-vs-derived replay, Hummingbot/Qlib backtest, event-level parity, PnL, win rate, Sharpe or Survivor claim was performed. The pinned GitHub source-code inspection supports a **proposed** six-gate expressibility claim, pending independent Hermes Auditor review.

**Six-gate evidence:**
1. Explicit EMA SMA-seed recursions, WPR range formula, strict cross, fixed periods/thresholds, validation, priority and immutable derivative identity.
2. Binance spot LONG/FLAT only; short is explicitly disabled.
3. Entry and frozen 2R close-triggered stop/target, no hidden stop orders or unspecified exits; invalid bracket halts.
4. Single 0.001 BTC fill-confirmed position, one pending order, no DCA/concurrency/pyramiding, new-edge re-entry, no same-bar reversal.
5. Direct pinned `BinanceSpotCandles` 4h → `ControllerBase` → MARKET `OrderExecutorSimulator` → `BacktestPositionHold` path; quote fees, timestamps, real-price guard and economic exclusions specified.
6. 80 completed-bar warmup, no future extrema, no incomplete-bar reads, explicit one-bar signal lag and effective next-close fill clock.

**Negative evidence / dedup:** The full Pine block is unavailable, so this record does not assert original execution equivalence. Existing pool entries for Williams %R level-cross, Forven Williams-EMA reclaim, and BullByte WPR/EMA/CHOP differ materially: this candidate requires **EMA20>EMA50 AND close>EMA20 AND strict -80 recovery**, then exits on a **two-candle-low-derived close-triggered fixed 2R bracket**, not on an oscillator exhaustion or EMA-loss exit. The first-party script ID and the rule tuple were searched against main and open research PRs on 2026-10-27 with no matching source or materially identical candidate found.

## Falsification plan

Before downstream research, verify a frozen historical candle sample's EMA/WPR values, delayed signal timestamps, modeled BUY/SELL close fills, stop/target anchors, one-position state and both-side fee ledger. Test equality at -80, a flat 14-bar range, malformed/missing 4h bars, entry fill below anchor, a stop-trigger close followed by a gap, last-bar exit signal, and no duplicate entry while LONG. Any new execution primitive must pass representative Qlib/Hummingbot event-level validation **before** mass Qlib screening; this Scout performed no test or backtest.

## Crypto portability

This derivative is pinned only to BTC-USDT spot 4h. Applying its author-described signal to another pair, timeframe, futures short, DCA or 3x/5x campaign overlay would be a **separate declared experiment** with its own fill, funding, margin, cost and causal checks; none are HB_READY prerequisites here.

## Limitations

The source's exact Pine, default EMA/WPR periods, risk/reward input and execution behavior were not obtained. The source describes same-signal-close entry and a stop/target; this derivative **changes both fill timing and bracket semantics**. A close-triggered exit one full candle later is not protective and may incur large loss beyond the anchor. Simulated historical close fills, a hypothetical fee and continuous base-quantity accounting do not establish real Binance executable prices, liquidity, tick/lot validity, actual costs or account equity. Package digest matching and a strategy-specific controller implementation remain unverified. No profitability, Qlib parity, HB Certified or trading authorization is claimed.

## Implementation status

**Not implemented.** No controller, backtest, container, Qlib workflow, Paper/Testnet/Live order, deployment or strategy adoption was changed. This is a six-gate research admission proposal only, not an executable artifact.

## Adoption boundary

**Research-only; not approved.** Independent Hermes Auditor GitHub Webhook Review must verify source facts and all six gates against the **exact PR head** before any PASS merge. A genuine unverified/unsupported gate must result in `HB_READY: NOT_LOSSLESS` and closure of this Scout PR, never an unsafe relabel. Only the existing signed webhook receiver reconciles README count after a confirmed merge.

## Sources

- TradingView first-party public source: https://www.tradingview.com/script/D9dkKBUh-W-R-Pullback-EMA-Trend-TS-Indie/
- Pinned Hummingbot source and VERSION: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
