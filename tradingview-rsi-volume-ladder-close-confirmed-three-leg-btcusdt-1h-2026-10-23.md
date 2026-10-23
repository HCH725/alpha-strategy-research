---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "TradingView RSI Volume Ladder: explicitly derived completed-bar three-leg spot mean reversion"
created: 2026-10-23
updated: 2026-10-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-23
sources:
  - https://www.tradingview.com/script/XuywwObg-RSI-Volume-Ladder/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView RSI Volume Ladder: explicitly derived completed-bar three-leg spot mean reversion

## Provenance

- **Primary strategy inspiration:** TradingView public open-source strategy "RSI Volume Ladder" by `wielkieef`, stable script identity `XuywwObg`, https://www.tradingview.com/script/XuywwObg-RSI-Volume-Ladder/. The public page displays publication date **May 10** without a year in the accessible rendering. Source/page checked **2026-10-23**. No immutable Pine revision or full Pine source text was available from the public page rendering used in this review; the page's detailed author description is the evidence for source-reported behavior. Do not assert source-code equivalence or claim an inspected immutable Pine revision.
- **Identity of this candidate:** an **independent, explicitly research-derived execution strategy**: `TV-XuywwObg / close-confirmed-spot-BTCUSDT-1h / derived-v1 / 2026-10-23`. It borrows the author-described RSI/volume entry, descending-fill gate, three-entry cap, average-price TP, lowest-fill SL, and asymmetric cooldown, but fixes its own market, bar timing, full-fill simulation, sizing, trigger evaluation and cost convention below. It is **not** a lossless replay of the original Pine strategy or its TradingView performance.
- **Original-to-derived differences:** author describes default 5%-of-equity per entry, intrabar OCO bracket behavior, `process_orders_on_close=true`, default 0.05% commission and development on crypto 5m/15m. This candidate instead chooses BTC-USDT **spot 1h**, fixed **0.001 BTC per leg**, completed-bar **close-triggered exits** (no intrabar OCO), signal-at-t / market-fill-at-(t+1)-close, and an explicitly declared **0.10% per-side simulator fee**. These are researcher-defined rules, not statements about the author's implementation.
- GitHub `main` canonical-source search for `XuywwObg` returned no match on 2026-10-23; open `research/*` PR source/title searches also returned no match. Related RSI and dip records do not combine **volume spike + successive-fill price-drop gate + average-cost TP + minimum-fill SL + exit-type cooldown** as this derived state machine.

## Economic mechanism

### Source-reported

The author proposes buying oversold RSI readings only when current volume exceeds its moving-average baseline; each additional buy requires another qualifying signal and a minimum drop below the most recent fill. Profits are taken relative to weighted average acquisition cost, whereas the protective level is anchored to the deepest filled leg. A stop-out imposes a longer cooldown than a profit exit. The author explicitly warns that averaging down during sustained declines is the major failure mode.

### Research interpretation

Falsifiable hypothesis: volume-confirmed oversold prints following progressively deeper pullbacks may contain short-horizon mean-reversion information, while the last-fill spacing gate and post-stop cooldown reduce correlated entries during a continuing selloff. The asymmetry between weighted-average TP and minimum-fill SL is a **risk construction**, not evidence of positive expectancy. The derived close-confirmed exit convention may materially worsen loss tails compared with intrabar brackets; this must be measured rather than assumed harmless.

## Signal

**All rules in this section define the research-derived v1; source-native parameters are explicitly distinguished above.** One market `binance BTC-USDT` spot, decision interval `1h`, **long-only**. Short orders, leverage and margin are disabled.

- On each fully completed bar `t`, use ordinary OHLCV from the same 1h feed. `RSI14_t` is Wilder RSI on `close`: price deltas, positive/negative parts, Wilder RMA with period 14 seeded by the arithmetic mean of the first 14 deltas. `volSMA20_t = mean(volume[t-19..t])`, including the completed current bar. If any input or derived value is missing/nonfinite, there is **no** signal; no backfill or synthetic price.
- Entry predicate `E_t = RSI14_t < 30 AND volume_t > 1.5 * volSMA20_t`. Both comparisons are strict. No RSI cross or EMA regime filter is silently added. For a **flat** state, `E_t` queues the first BUY only if cooldown is over. For an **open** state with fewer than three filled legs, `E_t AND close_t <= last_filled_price * 0.985` queues exactly one additional BUY. A pending order blocks all other entry/exit decisions until its fill or explicit failure; never queue two legs on one bar.
- Each successful BUY is exactly **0.001 BTC** base quantity, subject to the actual Binance spot amount increment and minimum-notional rules. If this exact size is not valid for the instrument at the intended fill, reject the proposed action and record the incompatibility; **do not** silently round it to a different size. There is no percent-equity resizing or compounding. Initial modeled quote capital is **10,000 USDT**; at most three legs (0.003 BTC) can be held, with no other asset or shared portfolio exposure. An execution exceeding available modeled quote cash including fee invalidates the action/run; the simulator must not manufacture a funded fill.
- After one or more confirmed fills, define `Q = sum(filled BTC)`, `avg = sum(fill_price_i * filled_BTC_i) / Q`, `low = min(fill_price_i)`, `TP = avg * 1.04`, `SL = low * 0.97`. All thresholds use **actual modeled fill prices**, not signal prices, and are recomputed after each additional fill.
- **Exit predicate, completed-bar only:** while holding, check `close_t <= SL` first (classify `SL`), else `close_t >= TP` (classify `TP`); otherwise hold. Queue one MARKET SELL of the entire actual filled `Q` for the next bar's close. A qualifying exit **always suppresses** a same-bar add. The exit classification is determined by the trigger at `t`, not retroactively by the eventual `t+1` fill price. No intrabar touch, OCO bracket, limit/maker, trailing stop, time stop, opposite signal, or liquidation stop is part of this derivative.
- Cooldown begins on the **exit fill bar index** `f`: after SL, completed bars `f+1,f+2,f+3` cannot queue new entries, so earliest new decision is `f+4`; after TP, zero blocked bars, so earliest decision is `f+1`. A failed/unfilled exit is **not** a completed exit and must not start cooldown. On full exit, clear fill stack, `avg`, `low`, and last-fill state; after a subsequent entry a fresh three-leg stack begins.
- Order priority/state machine: `PENDING_FILL` -> process fill or fail; `HELD` -> exit test before add test; `FLAT` -> cooldown test before first-entry test. No repeated same-side entry while an order is pending; one open long book, no short, no hedging, no extra safety orders. On missing next-bar data, **do not** fill at an invented price or advance the state as if a trade occurred.
- Warmup: require **21 consecutive completed 1h bars** (including at least 14 close deltas and a full 20-bar volume window) before the first signal. All earlier bars remain flat. Indicator values are calculated causally, never using future bars or a full-sample fit.

## Required data

- Historical Binance **spot** `BTC-USDT` 1h candles: timestamp, open, high, low, close and volume. Only close/volume enter decisions; open/high/low remain feed fields and are **not** used as simulated touch prices.
- Actual exchange trading rules for BTC-USDT: minimum base increment, minimum order size and notional. Price must be positive and a real observed close. A missing feed, trading rule, fill price or timestamp is a **hard data gap**, not a zero/one placeholder.
- No perpetual contract, leverage, funding, borrow, index/mark, liquidation, OI, L2, aggressor, macro, multi-timeframe, multi-asset or cross-venue input. **Spot funding is inapplicable**, not an assumed zero-valued futures funding series.

## Execution assumptions

**Pinned engine evidence (GitHub-source inspection, not an executed backtest):** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, `hummingbot/VERSION = dev-2.17.0`, matching the contract's 20260920 package vintage.

- `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`: `run_backtesting` accepts `backtesting_resolution` and explicit `trade_cost`; `prepare_market_data` exposes observed OHLCV and timestamped processed features; `simulate_execution` passes `CreateExecutorAction(OrderExecutorConfig)` to `simulate_executor`. `update_state` processes completed simulator rows; a strategy-specific controller must queue the **prior bar's** decision for action on the following completed row. This controller has **not** been implemented.
- `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`: `ExecutionStrategy.MARKET` fills at the **first available simulator row's actual `close`** and timestamp, with `filled_amount_quote = base_amount * fill_close`, `cum_fees_quote = trade_cost * filled_amount_quote`, and `POSITION_HOLD` result. The strategy's action must therefore be created only on `t+1` for a `t` decision. No assumption of an intrabar high/low touch, maker queue, partial fill or next-open price is made.
- `BacktestPositionHold._process_order` in that pinned engine nets sequential BUY additions at a quantity-weighted average entry and SELL reductions into realized PnL; `_update_positions_from_stopped_executors` aggregates filled `POSITION_HOLD` actions by connector/pair. Controller-local stack state preserves the **lowest individual fill**, which the aggregated average alone does not retain. An exit SELL of the complete base amount flattens the same spot position; no short sale is emitted.
- `backtesting_data_provider.py` supplies historical candles keyed `binance_BTC-USDT_1h`, `initialize_trading_rules('binance')`, and `quantize_order_amount`. The strategy requires the **exact** 0.001 BTC quantity to remain valid after quantization; otherwise it is ineligible for that market. The provider's fallback price behavior must **not** be used: fill must come from a present real candle close, with an explicit failure on missing data.
- Research cost model: set `trade_cost=0.001` **per filled side**, charged on actual filled quote notional; no claim this is an observed exchange fee tier. Source author describes 0.05%, which is **not** silently substituted. Spread, impact and slippage are **not modeled** by this close-fill simulator and therefore any reported returns would be simulator-only, not realized exchange economics. No funding is charged because this is spot, not a zero-funding perpetual assumption. No leverage, margin, liquidation, maker queue or futures position accounting is required.
- Existing version-pinned tests inspected (not run): `test/hummingbot/strategy_v2/backtesting/test_backtest_position_hold.py` covers buy/sell netting, full flattening and realized-PnL summaries; `test/hummingbot/strategy_v2/backtesting/test_backtesting_final_tick_ledger.py` covers `OrderExecutorConfig` and `POSITION_HOLD` final-row bookkeeping. This is **bounded primitive expressibility evidence**, not proof that a finished controller or live fill path exists.
- **Six-gate summary:** (1) exact RSI/volume/threshold/state definitions above; (2) long-only; (3) close-confirmed TP/SL and all disabled exits explicit; (4) fixed three-leg, one-action-at-a-time, cooldown and re-entry fully specified; (5) pinned Binance spot 1h candle + MARKET OrderExecutor + POSITION_HOLD netting + explicit research cost path as inspected above; (6) 21-bar warmup, prior-completed-bar decision, next-completed-close action, no lookahead. No unsupported futures or intrabar execution claim is smuggled into this PASS assessment. Independent Auditor must still review this exact PR head before any merge.

## Evidence

### Source-reported

The author describes RSI below 30, volume above 1.5 times SMA20, three long legs with 1.5% minimum drop from the previous fill, a +4% weighted-average TP, a -3% lowest-fill SL, and SL/TP cooldowns of 3/0 bars. The author reports `process_orders_on_close=true`, default 5%-equity per entry and 0.05% commission for the original. These are author statements from the TradingView page, **not** independently inspected Pine execution or independently reproduced performance. No ROI, Sharpe or win-rate is asserted.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The author's original OCO intrabar stop/target and this derivative's **completed-close trigger then next-close market exit** are not event-equivalent. A bar may cross the original SL intrabar and recover before close; this derivative holds. It can also fill well beyond its trigger on the next close. Never label this a source-native reproduction.
- Pyramiding into an extended selloff can accumulate three longs and remain underwater; a lowest-fill stop is not a guaranteed maximum loss under next-close fills.
- Source Pine body was not obtained in this cycle; no unsupported claim is made about exact Pine line order, exit-label implementation or the original backtest engine's trade sequence.
- The fixed 0.001 BTC spot sizing, 1h interval, 0.10% fee and 10,000 USDT starting cash are research-defined and may produce different outcomes from the original 5m/15m percent-equity futures/spot-unspecified examples.

## Falsification plan

- **F1, causal event replay (research-defined):** on frozen BTC-USDT 1h spot history, verify every signal uses only fully available data at `t`, every fill uses real `close[t+1]`, and no fill occurs on a missing candle. Fail if any order uses `t+1` information to decide at `t`, or if an entry occurs before warmup.
- **F2, ledger invariants (research-defined):** after each modeled fill, recompute `Q`, weighted average, lowest individual fill and TP/SL; require exact match with the emitted actions and net position. Fail on a fourth leg, duplicate pending action, partial/unfunded phantom fill, or an exit that leaves nonzero base quantity.
- **F3, state/priority tests (research-defined):** construct adversarial bar sequences for simultaneous oversold entry and SL trigger, three successive price-drop adds, a stop followed by three cooldown bars, and a TP followed by immediate next-bar eligibility. Require the priority and cooldown indices declared above.
- **F4, mechanism ablation (research-defined):** predeclare comparisons with (a) volume gate removed, (b) last-fill drop gate removed, and (c) SL cooldown removed, using identical 1h history and execution cost. No retrospective parameter tuning; a negative incremental net result after cost for the full model versus each simpler control challenges the purported edge.
- **F5, cost/market robustness (research-defined):** compare simulator 0.10% fee with higher explicit cost stress and report how omitted spread/slippage might erase any edge; freeze an IS/OOS split before examining results. No performance gate is an HB_READY admission requirement.

## Crypto portability

This derivative is **natively defined** for Binance BTC-USDT spot 1h candles. The original author's description mentions crypto majors and 5m/15m; it does not establish that this 1h spot derivative is profitable or equivalent. Applying the same logic to perpetuals, other pairs or BO/SO 6/6/6 would require a separately disclosed execution/cost derivative and the corresponding pinned-engine capability check. The optional seven-coin 1h/4h/1d campaign is not an admission whitelist.

## Limitations

No full Pine code was accessible from the page rendering; only the author's public description was used to identify source-native components. Derived trade events, fill prices and PnL can differ substantially from TradingView. The pinned backtester uses candle-close MARKET fills and a declared model fee, not actual spread/impact/partial-fill dynamics. A strategy-specific controller and actual strategy-level event parity have **not** been implemented or run; if the pinned primitive behaves differently on implementation, stop downstream screening and repair the engineering capability rather than claiming certification. Historical performance and Qlib/Hummingbot parity are not established.

## Implementation status

`not-implemented`. No backtest, controller deployment, Qlib implementation, engine mutation, order, Paper/Testnet/Live action, or capital authorization was performed. The inspected pinned engine primitives are existing software, not this strategy's implementation.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. `hb_ready_status: PASS` is a proposed six-gate expressibility assessment of this **declared derivative only**, subject to independent exact-head Auditor review. It is not proof of profitability, source-native equivalence, Qlib parity, HB Certified status or permission to trade.

## Related Wiki records

None. No Hermes Wiki read or write was performed.

## Sources

- TradingView primary inspiration and author-described parameters: https://www.tradingview.com/script/XuywwObg-RSI-Volume-Ladder/ (wielkieef; page shows May 10 without year; checked 2026-10-23).
- Pinned Hummingbot engine and spot backtest primitives (compatibility evidence only, **not** another strategy research source): https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Engine version: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION
- Engine simulator: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py
- Engine ledger: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/backtesting_engine_base.py
- Current admission contract: https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
