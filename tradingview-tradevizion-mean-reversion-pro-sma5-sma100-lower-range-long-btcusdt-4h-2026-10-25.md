---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradingView tradeviZion Mean Reversion Pro SMA5/SMA100 lower-range long-flat — independent BTCUSDT spot 4h derivative
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-01-18
sources:
  - https://www.tradingview.com/script/zt9TPsTS-Mean-Reversion-Pro-Strategy-tradeviZion/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Mean Reversion Pro lower-range SMA-reversion — independently derived research strategy

## Provenance and frozen identity

- **TradingView primary source:** **Mean Reversion Pro Strategy [tradeviZion]**, author **TradeVizion**, public script ID `zt9TPsTS`, publication **2025-01-18**, public open-source listing; the source page includes release notes dated 2025-01-14. URL: https://www.tradingview.com/script/zt9TPsTS-Mean-Reversion-Pro-Strategy-tradeviZion/ (author description checked 2026-10-25). The full Pine source was **not** recovered in a form allowing byte-level code inspection; Pine language/version and exact source implementation details are not asserted.
- **Source-description facts only:** default fast/slow SMA 5/100, default long-only mode, long entry requires price below fast SMA, in the bottom 20% of the current candle range, above slow SMA, and no existing position. The author describes long exit when price crosses above fast SMA; no fixed TP or SL, at most one position, default 10% equity size, daily chart, 0.01% commission and 2-point slippage. The author also describes a separately configurable short mode, which this derivative disables. Author's description does **not** resolve all exact Pine boundary and execution semantics.
- **Explicit independent derivative — NOT a lossless reproduction:** This record defines the previously ambiguous “price below 20% of current bar range” as the **completed candle close location** `close < low + 0.20*(high-low)`; fixes all SMA inputs, exact cross boundaries, close-confirmed decision/fill convention, 120-bar warmup, Binance BTC-USDT **spot 4h** (rather than author's daily example), fixed **0.001 BTC** size (rather than 10% equity), disabled short mode, missing-data policy, costs, end-of-sample treatment and controller state. These are researcher-selected alterations, not alleged source defaults or author backtest results.
- **Immutable research identity:** `TV-zt9TPsTS | independent-derived-v1-SMA5-SMA100-lower20-close-cross-exit | BinanceSpot-BTC-USDT-4h | 2026-10-25`. Any change to source, 20% interpretation, signal, market, clock, costs, size or exits creates a different derivative.

## Economic mechanism and limitations

Hypothesis only: a completed candle closing in its bottom 20% while below a short SMA but still above a long SMA may identify a temporary dip within a positive longer-term price regime; a subsequent cross above the short SMA is the reversion exit. This is not a demonstrated edge. No stop-loss is provided: a held position may experience severe drawdown. No original TradingView performance statistic is claimed or independently reproduced.

## Signal — exact derivative specification (Gates 1–4)

- **Data:** one standard Binance BTC-USDT spot OHLCV stream of consecutive UTC **4h** candles. Bar `t` is labeled by open epoch `T[t]` (aligned to 14,400 seconds) and is decision-available only at `T[t]+14,400`. All computations use **completed** candles only. A valid bar has finite positive `open/high/low/close`, `high >= max(open,close)`, `low <= min(open,close)`, finite nonnegative `volume`, and the exact expected open-time increment. No synthetic bars, forward fill, future prices, other symbols or data feeds.
- **SMA:** `SMA5[t] = (close[t]+...+close[t-4])/5`; `SMA100[t] = (close[t]+...+close[t-99])/100`. These are arithmetic simple moving averages of **close**, not EMA, smoothed/seeded alternatives, or OHLC4.
- **Candle location:** `range[t]=high[t]-low[t]`. If `range[t] == 0`, the lower-range gate is false. Otherwise `lower20[t] = close[t] < low[t]+0.20*range[t]`. Strict inequality: exactly 20% is false. This definition is **researcher-selected**; the author page's prose alone does not prove the original Pine expression.
- **Entry at bar t:** `FLAT && close[t] < SMA5[t] && close[t] > SMA100[t] && lower20[t]`. Both price/SMA inequalities are strict; equality blocks entry. This is a **level condition**, not a cross of the entry filters. A first eligible flat bar can enter after warmup.
- **Exit at bar t:** `LONG && close[t-1] <= SMA5[t-1] && close[t] > SMA5[t]`. This is the strictly defined **upcross** of completed close above completed SMA5, with prior equality qualifying and current equality not qualifying. The slow SMA and lower20 gate do **not** constrain exits. If close is already above SMA5 without an upcross on a later bar, the derivative remains LONG until a new valid upcross; no hidden level exit is added.
- **State and priority:** initialize FLAT; after **120 consecutive valid completed 4h candles**, on each valid eligible bar evaluate the state carried into the bar. If FLAT and entry true, issue one MARKET BUY for exactly **0.001 BTC** at the model's same-row close and enter LONG. If LONG and exit true, issue one MARKET SELL for the entire **0.001 BTC** at the model's same-row close and become FLAT. Otherwise HOLD. The FLAT entry requires `close<SMA5`, whereas LONG exit requires `close>SMA5`; no same-bar reversal, double action, or same-bar re-entry. An exit bar cannot also open a new position. The next later qualifying entry may re-enter without a cooldown.
- **Position and disabled behaviors:** at most one LONG and one pair, exactly 0.001 BTC per trade, no pyramiding, no safety orders, no DCA, no partial fills or partial exit in the simulator, no short, no leverage, no margin, no multi-asset/shared-capital rules, no compounding, no stop-loss, no take-profit, no trailing stop, no time-based exit, no intrabar touch, no maker/limit orders, no calendar gate, no forced terminal liquidation. At end of data, a remaining LONG is held and marked at last valid close, **not** sold at an invented terminal fill.
- **Gaps/invalid bars:** an invalid or missing bar breaks the 120-consecutive-bar warmup and suppresses *both* entry and exit signals until 120 new consecutive completed valid bars exist. Any already held position stays open while signals are suspended; no fabricated fill, carried-forward candle, or zero price is substituted. This is an explicit researcher-designed fail-closed rule. A valid zero-range bar counts toward warmup but cannot pass the lower20 entry gate.

## Causality and point-in-time data (Gate 6)

At decision time `T[t]+14400`, the current OHLCV and both SMAs, current range location, and the preceding completed close/SMA for the exit are known. No `request.security`, incomplete higher-frame candle, negative shift, future extrema, centered indicator, full-sample fitting, ML, or lookahead is used. Warmup is 120 completed contiguous bars, exceeding SMA100 and the extra previous-SMA observation required for cross. The raw Binance candle open timestamp must **not** be reported as the strategy decision time. The declared effective fill timestamp is the completed candle's close, and the close-price fill is a **pinned research simulator convention**, not a real-market guarantee that an order placed after seeing the close would execute at that price.

## Execution assumptions and pinned Hummingbot model (Gate 5)

- **Policy baseline:** Hummingbot package label `20260920`, `hummingbot/VERSION=dev-2.17.0`; pinned code repository `HCH725/hummingbot` at commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`. The VERSION, Binance spot 4h candle constants/parser, backtesting engine, OrderExecutorConfig, MARKET OrderExecutorSimulator and BacktestPositionHold source were read through the connected GitHub app this cycle. The policy's package label is retained as declared; the commit's `setup.py` separately contains a Python distribution `version="20260729"`. These are **different identifiers**, not proof of a package build digest. The independent reviewer must not silently equate them; if exact deployed package-to-code identity is a required missing fact, reject rather than fabricate it.
- **Feed and features:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` includes `"4h":"4h"`; `binance_spot_candles.py` maps REST Kline row[0..5] to open timestamp and OHLCV. `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` exposes backtesting OHLCV columns `open_bt/high_bt/low_bt/close_bt/volume_bt`. The strategy-specific, not-yet-implemented controller would calculate both SMAs and lower20 on this single native feed, with no unverified external data or alignment primitive.
- **Controller and execution:** `backtesting_engine_base.py` calls controller `determine_executor_actions()` for each processed row and routes `CreateExecutorAction` / `OrderExecutorConfig` to `order_executor_simulator.py`. MARKET mode uses the **first supplied row's close** for a full-amount fill; `OrderExecutorConfig` declares connector, trading pair, side, amount, `execution_strategy=MARKET`, leverage 1. This is an expressibility argument for the **existing** single-feed, completed-bar MARKET-close path, not a claim that this candidate has an implementation or has been backtested.
- **Clock and processed features:** the engine uses `timestamp_bt` open-time labels, `prepare_market_data()` uses backward `merge_asof` for features and `dropna`; therefore an implementation must build **causally valid** features only from already completed bars, verify continuous 4h labels, and normalize effective decision/fill events to open+14400. A generic backward merge alone is not proof of feature availability. Missing or invalid bars suppress events rather than permitting `dropna` to join distant rows. No same-close price claim is made for real execution.
- **Position/cost ledger:** the MARKET simulator sets `filled_amount_quote = amount * close` and `cum_fees_quote = trade_cost * filled_amount_quote`, with `POSITION_HOLD`. `BacktestPositionHold` nets BUY/SELL quantities, tracks average cost, realized gross PnL and cumulative fees. Fix research `trade_cost=0.001` (0.1% **per fill side**), `Q=0.001 BTC`, Binance spot, no funding (spot **not applicable**, not a realized zero funding series), no futures margin or liquidation. Model BUY as cash decrease `Q*buy_close + 0.001*Q*buy_close`; model SELL as cash increase `Q*sell_close - 0.001*Q*sell_close`. Net realized PnL = matched gross PnL minus **both** BUY and SELL fees; open-position cash+BTC mark-to-last-close includes prior fees. Do not equate native `summarize_results.net_pnl_quote` or `update_state.total_pnl` with fee-inclusive cash/equity without reconstructing the fill ledger.
- **Verified reusable capability evidence:** the same immutable pinned spot 4h OHLCV / MARKET-close / POSITION_HOLD accounting path was independently reviewed for admitted TradingView PR **#421**, exact head `e5e4cd8b6db015b081e5dfd897992a08ec445293` (review 2026-10-24 UTC); that review additionally exercised a synthetic BUY/SELL accounting fixture. This is *representative engine-path evidence*, not a backtest or a candidate-specific Qlib/HB parity claim. No new engine primitive is requested here.
- **Model limitations:** no exchange-validated min-notional, precision/lot rounding, real bid/ask spread, market impact, partial fills, latency, liquidity, realized commissions or production order acceptance. The modeled simulator has **no separate slippage** (zero *modeled* slippage by convention only). This is a reproducible research cost convention, not evidence of real zero slippage. No Testnet/Live authorization or profit guarantee.

## Six-gate admission claim for independent audit

1. **Determinism:** explicit close SMA5/100, strict lower-20% close location, precise entry/exit cross, equality and zero-range rules, 120-bar warmup, no guessed source code.
2. **Direction:** Binance BTC-USDT spot, LONG/FLAT, short explicitly disabled.
3. **Entry/exit/risk:** full bar-close signal conditions, cross exit, all alternative stops, targets and timers explicitly disabled.
4. **Position/state:** fixed 0.001 BTC single exposure, no DCA/pyramiding, deterministic re-entry and missing-data suspension.
5. **Engine:** fixed policy package/VERSION and code ref, 4h spot OHLCV, actual MARKET-close fill, fee/position ledger, effective timestamps, source-proven limitations and representative admitted path #421; independent reviewer must resolve any material build-identity concern, not infer from a generic API.
6. **Causality:** completed 4h bars, 120-bar warmup, no future information, effective close timestamp and fail-closed gap handling.

**This frontmatter PASS is the Scout's proposed research-only six-gate claim, not an independent review.** Only the existing Hermes Auditor GitHub Webhook Review may decide exact-head PASS/merge or NOT_LOSSLESS/close. No strategy backtest, Qlib parity, implementation, trading, cron change or deployment occurred.

## Dedup, falsification and evidence limits

- At current-main SHA `44bc03534d5493cfdb3460adb72337ce98a9887b` (2026-10-25 Asia/Taipei), README reports **314** and root tree has **314** strategy Markdown records. Independent reviewer of PR #421 checked all 313 preceding main strategy frontmatters PASS; the only intervening strategy addition is PR #421, independently PASS-reviewed, plus a separate README count update. This does not claim this Scout itself reread all 314 records or reaudited historical source facts.
- GitHub code search for `zt9TPsTS` and issue search for `Mean Reversion Pro` found no existing record/PR; 10 current open PRs were inspected for duplicate source/rules. Nearby `etf-3day-reversion-ema5` and `ibs-mean-reversion-short` families have different signals, holding and exit mechanics. The specific **SMA5/SMA100 plus completed-bar bottom-20%-range filter and SMA5 upcross exit** is not an existing admitted strategy by name or source ID.
- **Unverified:** original Pine source, source-code parity, exact author candle-location expression, author's performance, deployed package image digest, exchange precision, and real execution economics. This independent derivative makes no source-native equivalence or profitability claim.
- **Downstream falsification only, not run:** compare this frozen lower20 gate against an otherwise identical SMA-only dip entry on a predetermined IS/OOS split, without tuning on OOS; before mass Qlib screening of a new execution path require representative Qlib/Hummingbot event-level parity. This is a later research step, not an admission gate or authorization to trade.
