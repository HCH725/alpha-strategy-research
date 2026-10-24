---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradingView connorgeary150 RSI14 momentum cross 55 entry / 50 exit, derived BTCUSDT spot 1h long-flat
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
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

# TradingView RSI14 momentum cross 55 / 50 — independently specified derived BTCUSDT spot long-flat, 1h

## Provenance

**Immutable identity of this proposed research rule:** `TV:OMfjRHLz / connorgeary150 / BTC-Momentum-Trading-RSI-Cross / derived-long-flat-v1 / BTCUSDT-spot-1h / 2026-10-25`. All decision-critical researcher settings are frozen in this record; changing a threshold, side, RSI seed, execution convention, or market creates a different strategy identity. This identity is NOT an immutable copy of the publisher's Pine source.

- **TradingView primary source:** https://www.tradingview.com/script/OMfjRHLz-BTC-Momentum-Trading-RSI-Cross/ ; author **connorgeary150**, public page dated **2026-02-23** (page displays “Feb 23”; its text reports a 2026-02-16–23 test). Script title **BTC Momentum Trading - RSI Cross**, category **Strategy**, labeled **OPEN-SOURCE SCRIPT**. Source facts inspected on 2026-10-25 from the publisher's own public page.
- **Verifiable source-native decision rules in the page description:** RSI(14) crosses **above 55** to enter long; crosses **below 45** to enter short; a held long exits when RSI crosses **below 50**; a held short exits when RSI crosses **above 50**. The publisher reports BTCUSD at 10-minute resolution for 2026-02-16–23, with 1,284 trades, 27.92% profitable, PF 0.886 and drawdown 2.13%; these are **source-reported only**, with no independent replay, costs audit, or reproducible sample furnished here.
- **Evidence boundary:** the public description supplies the four numerical event conditions above, but the rendered page does **not** expose the Pine source bytes, the RSI input price/seed implementation, order-fill declaration, sizing, fees, or complete risk-order census. Thus this record does **not** assert source-native/lossless Pine equivalence, source-native absence of stops, or reproduction of those backtest figures. “Open-source” labeling alone is not a source-code verification.
- **Explicit independent derivation (all alterations):** (1) disable the publisher's short side entirely, retaining only its long entry and long exit conditions; (2) choose BTCUSDT Binance **spot**, unleveraged, instead of the page's BTCUSD study; (3) choose the pinned **1h** decision interval instead of its 10-minute study; (4) define RSI as the exact close-price Wilder calculation and flat-price edge cases below (the description does not pin the price/seed); (5) adopt the completed-bar same-bar-close MARKET backtest convention, not a claim about the publisher's Pine fill timing; (6) choose one fixed 0.001 BTC unit, no DCA/pyramiding, controller-memory state, 100-bar warmup, no SL/TP/trailing/time exits, and explicit fee/slippage modeling below. These are researcher-designed rules and **not** represented as source facts. No undisclosed source risk/execution features are inherited.
- **Version boundary:** TradingView's script ID is stable as an identifier but the public description is not a content-addressed, immutable Pine artifact. The rule *defined in this Markdown* is the frozen derived version to audit. Source author and date are descriptive provenance, not a guarantee the public page can never change.

## Economic mechanism

### Source-reported
A momentum system responds to RSI threshold crossings, rather than oversold mean reversion. The page explicitly distinguishes entry levels 55/45 from midline exits at 50.

### Derived research hypothesis
On a BTCUSDT spot 1h chart, a completed-bar RSI14 **upcross through 55** buys one fixed unit; a subsequent completed-bar RSI14 **downcross through 50** liquidates it. There is no short side and no protective stop: a held long may suffer losses until the exit cross occurs. This is a deliberately minimal long-flat momentum timer, not an assertion of positive expectancy.

## Signal — fully pinned derived rules (Gate 1 and Gate 2)

- Data: contiguous, valid **completed Binance BTCUSDT spot 1h candles**, UTC-aligned, sorted ascending with unique open timestamps and finite strictly positive close values. No interpolated or synthetic prices. Reject a dataset with gaps, duplicates, invalid prices, or insufficient history rather than filling missing bars or manufacturing trades.
- Indicator: close-price Wilder RSI(14), using `delta[t] = close[t] - close[t-1]`, `gain[t]=max(delta[t],0)`, `loss[t]=max(-delta[t],0)`. The first averages are the arithmetic means of the **first 14 completed price differences**, then `avgGain[t]=(13*avgGain[t-1]+gain[t])/14` and `avgLoss[t]=(13*avgLoss[t-1]+loss[t])/14` on each subsequent bar. `RSI[t]=100-100/(1+avgGain[t]/avgLoss[t])` when both averages are positive. If loss average is zero and gain average positive, RSI=100; if gain zero and loss positive, RSI=0; if both zero, RSI=50 (explicit **derived** flat-tape convention, not a Pine-source claim). Calculations use unrounded float64 values; never round RSI for predicates.
- Long entry edge on completed bar t: `RSI[t-1] <= 55 AND RSI[t] > 55`. Equality at the previous bar is allowed; equality at the current bar is not. This is an **upward crossing**, not a persistent `RSI>55` condition.
- Long exit edge on completed bar t: `RSI[t-1] >= 50 AND RSI[t] < 50`. Equality at the previous bar is allowed; equality at the current bar is not. This is a **downward crossing**, not a persistent `RSI<50` condition.
- Short entries/exits are explicitly **disabled**. The original page's RSI downcross 45 short and upcross 50 short exit are provenance facts only; they never generate orders in this derivative.
- No indicator gates beyond those predicates. No MA, volume, ATR, market regime, news, portfolio cross-sectional rank, MTF, order book, funding, OI, mark price, or future extrema enter a decision.

## Execution assumptions and position state (Gate 3 and Gate 4)

- State starts `FLAT`. On each eligible completed bar: `FLAT + entry` creates one MARKET BUY for exactly **0.001 BTC** and sets the controller's own state to `LONG(0.001 BTC)` after the modeled fill; `LONG + exit` creates one MARKET SELL for **0.001 BTC** and returns to `FLAT` after the modeled fill. `LONG + entry` is a hold/no-op; `FLAT + exit` is a no-op. Never short, reverse, or carry multiple positions.
- Entry and exit cannot coincide on one bar: `RSI[t] > 55` and `RSI[t] < 50` are mutually exclusive. No arbitrary same-bar signal priority is needed. No pending-order stacking: the specified backtest MARKET path fills at the decision row; if a fill cannot be evidenced at a valid price, **halt that run**, do not advance controller state by pretending it filled.
- Exactly one active long at most. **Pyramiding: off. DCA/SO: zero. BO: one fixed 0.001 BTC unit.** No leverage, no margin borrowing, no liquidation model, no simultaneous other market. No cooldown. Re-entry only on a *fresh* RSI upcross through 55 after a completed exit; remaining above 55 is not a new entry.
- **All other exits disabled by derived design:** no stop loss, take profit, trailing stop, breakeven, time limit, partial exit, funding exit, profit-based or price-touch order, and no opposite-side reversal. If an RSI exit never arrives, the book remains long to the research horizon; terminal unrealized value is reported separately, not silently counted as a fill.
- Signal checks are independent of fees and account PnL; fees cannot secretly alter entry/exit triggers. No compound sizing, no shared portfolio capital state. Available spot cash sufficient for one 0.001 BTC purchase plus modeled fees is a required run precondition, not a fabricated account balance.

## Pinned Hummingbot compatibility and accounting (Gate 5)

**Actual pinned code inspected through GitHub**: repository `HCH725/hummingbot`, commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`, corresponding to admission package `20260920`, VERSION `dev-2.17.0`. These are pinned model capabilities, not a claim this specific derived controller is already deployed. Relevant immutable paths and verified behaviors:

1. `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` (blob `6d505dff42b60b356931df13eeeecd1e28b426f9`) includes **1h** in `INTERVALS`. `binance_spot_candles.py` (blob `5d0c938af574aca5f8dcba5ba28121797eae4dd0`) sends `interval=self.interval` to the Binance spot kline endpoint and maps REST `row[0]` to the candle **open** timestamp. The venue is `binance`, trading pair `BTC-USDT`; this is one supported single-pair spot feed, not a cross-market synchronization claim.
2. `hummingbot/strategy_v2/executors/order_executor/data_types.py` defines `OrderExecutorConfig` with `connector_name`, `trading_pair`, `side`, positive base `amount`, explicit `execution_strategy=ExecutionStrategy.MARKET` and `leverage=1`. This record needs **BUY/SELL MARKET OrderExecutor** actions only, not PositionExecutor TP/SL, maker touch, intrabar sequencing, leverage, or a perpetual funding model.
3. `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` (blob `3b4e82e91896db9074295ca2a8a087dde2499eab`, lines 21–24, 55–70) sets MARKET fill to the creation row's timestamp, `entry_price=df_filtered.loc[fill_timestamp,'close']`, quote filled to `float(config.amount)*entry_price`, and `cum_fees_quote=trade_cost*amount_quote`, then terminates as `POSITION_HOLD`. **No slippage or maker-queue mechanics** are applied by this simulator. This is the actual bar-close backtest fill convention, not a claim about real-time executable prices.
4. `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` (blob `7d1e552dd7ee62df4f83f10950b8d593cd1106e6`), `BacktestPositionHold` lines 65–123, nets BUY and SELL by base quantity, realizes price-difference PnL on a reducing SELL, and separately accumulates `cum_fees_quote`; `get_position_summary` exposes realized, unrealized and fees separately. `simulate_execution` lines 279–303 calls `update_state`, then controller actions, then executor simulation on the current row; it flushes last-row executions. The controller MUST use its **own confirmed-fill state** for signal gating, not rely on the lagged `positions_held` view or terminated-executor retention window.
5. **Causality/timestamps:** Binance REST candle timestamps are **open** times, not decision times. For a contiguous 1h bar with open timestamp `u`, the derived decision is valid **only at effective time `u+3600s`**, when its close and RSI are available. The backtest simulator's row label remains `u`; reports must explicitly map that row's simulated fill to effective bar-close time `u+3600s`. Never present raw `u` as a causal real-world signal/fill timestamp. Same-bar-close is a declared *simulation convention*, not guaranteed live executable timing. If this effective-time mapping cannot be preserved by the eventual strategy-specific implementation, it is an engineering capability HOLD before screening, not a license to use the bar's close at its open.
6. **Costs:** `trade_cost=0.001` per side is a **declared hypothetical research fee rate** (0.10% of each fill's quote notional), NOT a sourced actual Binance tier or independently verified paid fee. Simulator fill slippage is **0 in this specific modeled path**, NOT a claim of zero market slippage. Spot funding is **not applicable** (no perpetual contract, no funding settlement); do not invent or report a realized zero-funding series. No mark/index/funding/margin path is required. No source-native Pine fee or fill claim is inferred.
7. **Precision/economics:** the pinned simulator converts base amount to float for `filled_amount_quote`, and position-hold bookkeeping divides quote by price using Decimal; small float/Decimal residuals are possible. No claim of exact decimal base cancellation, venue lot-size enforcement, exchange minimum notional, or real exchange fee tier is made. For research reporting, `gross realized = sum((sell_price - matched_average_buy_price)*matched_base)`; `modeled net realized = gross realized - sum(all BUY and SELL cum_fees_quote)`; mark-to-close unrealized PnL is a separate component. Do not label `net_pnl_quote` fee-inclusive unless independently reconciled. An actual exchange deployment would require separate venue-precision, liquidity, and fee verification, outside HB_READY.
8. **Controller materialization:** a strategy-specific controller implementing the two predicates and the above one-unit ledger is **not implemented** (`implementation_status: not-implemented`). The cited pinned engine contains the necessary single-feed, MARKET order, fill, position-hold and cost primitives. This admission is a bounded model-expressibility claim, NOT a claim of a completed executable controller, Qlib parity, profitability, Paper/Testnet/Live authorization, or existing runtime integration.

## Point-in-time causality and warmup (Gate 6)

- The first **100 contiguous completed 1h bars** are warmup and are held flat by explicit derived rule; this covers the 14 price-difference RSI seed and further RMA settling. No signal or fill before the warmup floor. RSI[t-1] must be available as well as RSI[t].
- RSI uses only closes with indices `<=t`; no negative shift, repainting pivot, future candle, full-sample normalization, fitted parameter, ML training, or incomplete HTF bar. A valid decision is made only after the decision bar closes at `u+3600s`. The engine's open-timestamp convention is explicitly re-labeled for causal reporting as above; any implementation unable to do so fails this record's timing requirement.
- The data validation precondition rejects missing candles/invalid prices instead of replacing them with guessed fills or forward-filled RSI inputs. No TP/SL intra-candle path is involved, hence no OHLC order-of-events assumption.

## Six-gate evidence checklist

1. **Deterministic:** fixed close-price Wilder RSI14 including seed and zero cases, 55/50 strict edge rules, 100-bar warmup, single contiguous 1h feed.
2. **Direction:** long/flat only; source short side explicitly removed as a derived alteration.
3. **Entries/exits/risk:** exact upcross 55 entry, downcross 50 exit; all stop/target/trailing/time exits expressly disabled, no hidden defaults.
4. **Position:** one 0.001 BTC unit, zero SO/DCA, no pyramiding or cooldown, exact re-entry edge and no-op states.
5. **Pinned engine:** exact Hummingbot commit, Binance spot 1h candle feed, MARKET OrderExecutor close fill, BacktestPositionHold netting and fee ledger, explicit hypothetical costs and timestamp mapping; no unsupported futures/maker/intrabar path claimed.
6. **Causality:** completed bars only, effective `open+3600s` decision/fill time, no future inputs, gap rejection, warmup floor.

## Evidence

**Source-reported, not reproduced:** the TradingView author's RSI thresholds and four event rules; its BTCUSD 10m 2026-02-16–23 performance figures (1,284 trades, 27.92% win rate, PF 0.886, DD 2.13%) are neither this derivative's results nor independently verified.

**Independently reproduced:** **none**. No Hummingbot or Qlib backtest, synthetic execution test, real fill, account ledger or parity run was performed by this Scout.

**Dedup at main `b4c1f85340b807293f01c15111c5d1dcde86ab61` (2026-10-25):** the 308 root-level strategy filenames were inspected from the current Git tree, and GitHub code search returned no `OMfjRHLz` source citation; search of open `research/*` PRs (10 results) and all PRs for `OMfjRHLz` returned no same-source candidate. Closest main neighbors differ materially: `rsi-classic-level-reversal` enters on persistent RSI<30 and exits on RSI>60 (oversold mean-reversion level rules, not momentum edge 55/50); `cumulative-rsi-dual-threshold` uses RSI3 summed over 3 bars and cross-up 60/282 (different indicator and both edge polarities); `forven-rsi-boundary-rejection` uses a 3-bar RSI30 touch, RSI35 recovery and EMA200 trend filter, with EMA-side exit; `drm-dynamic-rsi-momentum` uses an adaptive 20–50-period RSI and two-sided 30/70 signals. None is the fixed RSI14 55-upcross entry/50-downcross long-flat state machine with this TradingView identity. This is not a parameter-only clone of any of those mechanisms.

**Limitations and admission boundary:** Source Pine bytes and source-native execution defaults were not accessible from the rendered TradingView page; only its explicit public IF/THEN rules are attributed to the author. All missing execution details are **newly and transparently defined in this independent derived strategy**; no unverified source behavior is labeled source-native. The pinned backtester offers bar-close modeled fills but does not validate actual market impact, fees, liquidity, exchange precision or Qlib parity. This is research admission only; before large-scale Qlib screening of a new execution path, require representative Qlib/Hummingbot event-level parity. Never interpret this PASS as a live-trading or profitability verdict.
