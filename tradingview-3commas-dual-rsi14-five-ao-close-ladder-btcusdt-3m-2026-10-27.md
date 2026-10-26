---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "3Commas dual-RSI14 five-level DCA close-ladder — independent BTC-USDT spot 3m long-flat derivative"
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
  - derived
status: research-only
confidence: medium
source_as_of: 2026-05-20
sources:
  - https://www.tradingview.com/script/qgofvS9I-Dual-RSI-DCA-Long-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# 3Commas dual-RSI14 five-level DCA close-ladder — BTC-USDT spot 3m research derivative

**Immutable derived strategy identity:** `TV:qgofvS9I | 3Commas | published:2026-05-20 | independently-derived-v1:2026-10-27 | Binance BTC-USDT spot 3m | RSI14 cross-up 31 BO / cross-down 69 and >=2.4% gross average-price exit | 90 USDT BO + five geometric 110x1.25^(k-1) USDT AOs | cumulative 1.3%x1.3 deviations | completed-close one-action-per-bar | research fee 0.08%/side`. This identifies the **frozen derived rule set**, not a frozen copy of inaccessible Pine bytes.

## Provenance

**Primary source:** [Dual RSI DCA - Long Strategy](https://www.tradingview.com/script/qgofvS9I-Dual-RSI-DCA-Long-Strategy/) by **3Commas**, published **2026-05-20**, public TradingView script ID `qgofvS9I`; source description inspected 2026-10-27. The page labels the script **open-source**, but the complete executable Pine, exact Pine version, its historical revision bytes, all broker-emulator settings, and exact intrabar fill priority were **not retrieved**. Do not claim lossless reproduction.

**Verified source-description facts:** long-only, base entry when 3m RSI(14) crosses **up** through 31, full exit when RSI(14) crosses **down** through 69 **and** current price is at least 2.4% above the weighted average entry; five sequential averaging orders at cumulative deviations from the base entry of approximately 1.30%, 2.99%, 5.19%, 8.04%, 11.76%; initial AO quote size 110 USDT multiplied by 1.25 each level; deviation increments start at 1.3% and grow by 1.3; base order 90 USDT on a 10,000 USDT reference account. No stop-loss. One open DCA cycle. Source describes a BYBIT:HYPEUSDT.P perpetual 3m study, 0.08% commission and 3 ticks slippage, a market/limit base toggle, and TradingView `security()` behavior. Those source market, fill, slippage and timeframe-join semantics are **not** represented as verified for this derivative.

**Researcher-authored, material differences:** change HYPE perpetual to **Binance BTC-USDT spot**; use native single 3m bars (no `security()` join), exact Wilder RSI initialization, explicit cash/fee/precision rules, **completed-close MARKET fills** for BO/AOs/exit instead of any unverified intrabar ladder/limit/broker behavior; at most one order per completed bar, oldest unfilled AO first, no multi-AO gap catch-up on one candle; model no separate slippage (rather than source's 3 ticks); fixed 100-bar no-trade warmup and full-history research window; exact exit-before-AO priority and reentry/reset rules. The five source-described AO levels, quote sizes, RSI thresholds and profit gate are retained as *research parameters*, not as a claim of identical source trade events. BTC may exhibit fewer cycles than HYPE; no original performance transfers.

**Dedup on main SHA `ddb1f9e4cc12ad18c52e3bc26411e38da6785723`:** main root has 369 strategy Markdown records and README declares 369; no count drift. GitHub main code search for `qgofvS9I` and `3Commas` returned no matching strategy record; root filenames include no `dual-rsi`, `dca` or `ladder` strategy record. Open `research/*` PR list and exact source/dual-RSI PR searches showed no match. Nearest related `tradingview-burbinlee-rsi14-three-daily-close-legs-btcusdt-1d-2026-10-25.md` uses a *different* TradingView script (`LS6Jsy63`), RSI cross **below** 30, only three fixed-BTC daily buys on scheduled days and a +4%/-3% close bracket; this candidate uses cross **above** 31, five *price-deviation-triggered* quote-size AOs on 3m and a cross **down** 69 plus profit gate with no stop. It is not a parameter-only clone. Search indexing is not a substitute for immutable Pine verification. Root frontmatter of all 369 existing records was not independently reaudited by this Scout; numeric agreement is not claimed as that proof.

## Economic mechanism

The research hypothesis is a bounded **capital-deployment** mean-reversion ladder: an oversold RSI recovery opens a small long; successively deeper close-price discounts accumulate a larger base amount at lower prices; an overbought rotation closes the *entire* weighted-cost position only after a minimum positive price margin. The ladder caps **additional committed capital**, **not downside loss**: after the fifth AO, a collapse can produce prolonged or effectively total position loss. No profitability claim or observed fill is made.

## Signal and deterministic state machine

1. **Market/data:** one `BTC-USDT` Binance spot `3m` series. Let `C[t]` be the finite positive **completed** candle close at chronological index `t` and `T[t]` its UTC candle-open timestamp. No other asset, timeframe, order book, index/mark, external signal, training data, or future data. All formulas use chronological prefixes only. Indicator arithmetic is deterministic float64 in bar order; position and cash arithmetic use Decimal with precision 28.
2. **Wilder RSI(14):** `delta[t]=C[t]-C[t-1]`, `gain=max(delta,0)`, `loss=max(-delta,0)`. At `t=14` seed `avgGain` and `avgLoss` by arithmetic means of deltas `1..14`; thereafter `avgGain[t]=(13*avgGain[t-1]+gain[t])/14` and likewise for loss. `RSI=100-100/(1+avgGain/avgLoss)`; if loss=0/gain>0 return 100; gain=0/loss>0 return 0; both zero return 50. No alternative TA library seed, lookahead or cross-bar interpolation.
3. **Warmup:** compute the RSI on all available bars but keep FLAT for the first **100 complete 3m candles** (`t=0..99`). First eligible action at `t=100`. A positive RSI regime already present during warmup is **not** a fresh cross. Any gap or invalid row aborts the contiguous segment; never silently compress ladder spacing.
4. **Base trigger:** while FLAT, `RSI[t-1] <= 31 AND RSI[t] > 31`, with both defined, emits one BO BUY at that completed bar's modeled MARKET close. Strict current `>`, previous `<=`. An unaffordable/rejected BO is not queued; a new genuine cross is required. Record the **actual modeled BO fill close** `P0` as the immutable ladder anchor for the cycle.
5. **AO levels:** for `k=1..5`, the *cumulative* fractional drawdown is `D[k]=0.013 * sum(1.3^j for j=0..k-1)`. Threshold `L[k]=P0*(1-D[k])`, not a drawdown from the changing weighted average. Nominal quote budget `B[k]=110*(1.25^(k-1))` USDT. In an open cycle, after checking exit, if `k` is the smallest not-yet-filled AO and `C[t] <= L[k]`, emit **exactly one** BUY at `C[t]`. Do not fill AO2–AO5 simultaneously even if the same close breaches multiple levels; evaluate the next level only on a **later** complete bar. An AO that fails affordability or simulator acceptance is skipped for that bar and remains the next pending level, without inventing a fill or advancing the counter. A level can be filled later only on a new completed bar still at/below its threshold. All five AOs are optional; BO plus AOs are a **single** long position, not concurrent independent deals.
6. **Quote-to-base sizing:** nominal BO `B[0]=90` USDT; AO budgets as above. For a BUY on bar `t`, request base amount `Q=floor((B[k]/C[t])*10^8)/10^8 BTC` as Decimal, rounded **down** to eight base decimals. Actual simulated quote notional is `Q*C[t]`, not exactly `B[k]` after rounding; cash debit is `Q*C[t]*(1+0.0008)`. Require `Q>0`, available nonborrowed cash >= full debit, and a successful simulated fill. This eight-decimal grid is a **research arithmetic convention**, not a verified live Binance LOT_SIZE/precision permission. Failed or zero-quantity actions never change cash, filled inventory, weighted cost or AO index. Maximum **nominal** ladder spend before fees is `90+110*(1+1.25+1.25^2+1.25^3+1.25^4)=992.7734375` USDT (9.927734375% of initial 10,000 USDT); actual notional can be slightly lower after rounding.
7. **Exit:** while LONG, on every **later** completed bar, compute `A=(sum(Q_i*P_i))/(sum(Q_i))` over **successfully filled** BO/AOs, excluding fees from the average and tracking them separately. If `RSI[t-1] >= 69 AND RSI[t] < 69 AND C[t] >= 1.024*A`, emit **one full SELL** of the actually held base amount at `C[t]`; credit `Q_total*C[t]*(1-0.0008)`, clear BO anchor/AO schedule/position state and return FLAT. The 2.4% is a **gross price-above-average gate**, not guaranteed net return. A crossdown without the simultaneous profit condition is discarded, not armed for a later profitable bar. No fixed take-profit order exists.
8. **Priority and re-entry:** on each bar with LONG, test full exit first; if no exit, test only the next pending AO; otherwise hold. On FLAT, test only fresh BO cross. Never exit and re-enter or add and exit on the same bar. After a full exit, a *later* fresh cross-up 31 is required; no timed cooldown. RSI events while LONG do not start additional cycles.
9. **Risk/disabled behaviors:** **no stop-loss**, no maximum holding time, no trailing, no partial TP, no forced terminal liquidation, no discretionary manual close, no hedge, no short, no futures, no leverage, no margin, no additional AO beyond five, no dynamic quote sizing or compounding, no multiple pairs, no hidden Hummingbot DCA-controller defaults. One outstanding action maximum; no synthetic position while an order is unfilled. Terminal open inventory is marked to the last *observed* close as unrealized equity, without a fictitious closing fill.

## Required data and causality

- Binance spot UTC `3m` complete OHLCV: open timestamps strictly increasing in steps of **180 seconds**, with no duplicate/missing candle. Validate O/H/L/C finite and positive, `high >= max(open,close) >= min(open,close) >= low`, and volume finite/nonnegative **before** feature merging or `dropna`. Reject malformed rows, gaps, stale last partial bars or missing close prices; never interpolate, forward-fill, fabricate prices, or shift a signal to another candle. A fresh research segment starts FLAT with 100 completed bars of warmup.
- `T[t]` is candle **open time** from the pinned feed. Effective signal/decision and modeled fill time is **`E[t]=T[t]+180 seconds`** only after the candle completes. The pinned simulator labels MARKET fills with `T[t]` despite using `C[t]`; correct the event-time label for research reporting. A historical close-fill at `E[t]` is a **simulator accounting convention**, not proof that a live order submitted after close could execute at that past close. There is no intrabar AO fill, next-open promise, lookahead security join, partial HTF read or use of future candles.

## Execution assumptions — demonstrated pinned model path

**Hummingbot admission baseline:** package `20260920`, VERSION `dev-2.17.0`, immutable inspected source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. The connected GitHub app **read** `hummingbot/VERSION`, the exact Binance spot 3m feed, the `OrderExecutorConfig` schema, `OrderExecutorSimulator`, and `BacktestingEngineBase` / `BacktestPositionHold` in this cycle. Wheel-to-source byte equivalence was previously reported in independently accepted Alpha PR #414 (902/902 files), **not** rehashed in this Scout.

- **Feed/market:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` explicitly maps `"3m": "3m"`; `binance_spot_candles.py::_parse_rest_candles` maps REST kline `row[0]` to candle **open** seconds, `row[1..5]` to OHLCV. Research connector `binance`, pair `BTC-USDT`, spot LONG/FLAT, leverage `1`. Native same-timeframe 3m input removes the source's `security()` alignment dependency; do not claim source-native HYPE perpetual execution.
- **Controller/action path:** a not-yet-implemented dedicated strategy-specific controller computes the exact RSI, BO/AO/exit state and cash/precision gates from **validated completed** candles. `BacktestingEngineBase.simulate_execution` iterates `prepare_market_data()` rows, calls `update_state` then `determine_executor_actions`, and handles `CreateExecutorAction` via `simulate_executor`. `prepare_market_data` uses `merge_asof` and `dropna`, so input completeness must be verified **before** this path; neither routine is proof of point-in-time availability by itself.
- **Real pinned fill primitive:** each BO/AO uses `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=BUY, amount=Decimal(Q), execution_strategy=MARKET, price=None, leverage=1)`; a full SELL uses the actually held BTC amount. `OrderExecutorSimulator.simulate` MARKET branch selects the first processed row, fills at that row's **close**, sets `filled_amount_quote=amount*close` and `cum_fees_quote=trade_cost*notional`, and returns `CloseType.POSITION_HOLD`. Each AO is a separate MARKET executor action on a different 3m bar; no claim is made that Hummingbot's DCA executor can reproduce source intrabar limit fills. The controller needs an immediate post-action simulated-fill ledger and one-in-flight guard; a pre-action `positions_held` view can lag, and the default terminated-executor window can expire before later decisions.
- **Weighted DCA cost and exits:** `BacktestPositionHold._process_order` explicitly adds same-side BUY amount and quote cost into a volume-weighted average; opposite-side SELL reduces the net amount and books **gross** realized PnL. `add_executor` separately accumulates per-side `cum_fees_quote`. The backtest final-flush path reconciles last-bar POSITION_HOLD fills. Controller's own filled-inventory/cash/fee ledger must agree with this position-hold route; no phantom fills, duplicate AOs, negative spot holdings, or position inferred from unfilled executor configs.
- **Research economics:** `trade_cost=0.0008` **per executed BUY or SELL side**, taken from the source's **reported** 0.08% research commission and frozen here as an **assumption**, **not** a live Binance fee quote. No extra modeled slippage: this deliberately **drops** the source's 3-tick slippage; it is a limitation, not evidence of zero market spread/impact. Spot funding is **not applicable** (not hypothetical zero-funded futures). Track `cash + heldBTC*last_valid_close` equity; realized **net** quote PnL is gross matched PnL minus all paid entry/AO/exit fees. Engine gross `realized_pnl_quote` alone is not net. The MARKET simulator's full-close fills, float arithmetic, and research eight-decimal sizing do **not** verify actual Binance exchange filters, minimums, partial fills, latency or tradeable closing prices.
- **Bounded capability claim:** this record relies on the inspected **3m spot, sequential MARKET-close, POSITION_HOLD weighted-cost and quote-fee** path only. It does not claim source-native HYPE futures, 3-tick slippage, live limit ladder, real funding, realistic same-close trading, implementation, profitability, or Qlib parity. Any such different requirement needs separate representative engine validation before mass screening.

### Six HB_READY gates — Scout proposal, independent review required

1. **Deterministic signals:** complete Wilder RSI14 seed, strict cross operators, fixed 31/69 levels, 2.4% gross gate, five exact cumulative 1.3x price deviations, quote-size 1.25x progression, 100-bar warmup, tie/invalid-data handling and action priority.
2. **Direction:** explicit Binance BTC-USDT spot **LONG/FLAT** only; short, borrowing, perpetual margin and hedge disabled.
3. **Entry/exits/risk:** cross-up BO, sequential close-threshold AOs, cross-down 69 **and** gross +2.4% full exit; **no SL** or time/trailing/partial exit, even in prolonged drawdown.
4. **Position/state:** one cycle, one action per 3m bar, max BO+five AOs, eight-decimal base rounding, actual-fill weighted average, cash/fee ledger, pending AO index, failed-action handling and fresh-cross-only reentry.
5. **Pinned engine:** directly inspected 3m Binance spot feed, `CreateExecutorAction`/`OrderExecutorConfig` MARKET close-fill, separate successive weighted BUY position-hold accumulation, full SELL reduction, modeled quote fees and open-time timestamp caveat at immutable `8b0e067`; not merely an API-name inference.
6. **Point-in-time:** validated complete contiguous UTC 3m bars, 100-bar flat warmup, prefix-only RSI, no MTF join or future extrema, one action per completed bar and explicit `open+180s` effective-time correction. Historical same-close fill is labeled a research convention, not executable at that known past price.

`hb_ready_status: PASS` is the **Scout's proposed model-expressibility assessment**, **not** an independent audit, verified original Pine equivalence, source profitability, Hummingbot implementation, or authorization to merge. Hermes Auditor must independently review the **exact PR head**.

## Evidence

### Source-reported

TradingView `qgofvS9I` by 3Commas (2026-05-20) publicly describes the two RSI(14) threshold crosses, 2.4% profit gate, five geometric AOs, 90/110 USDT BO/AO sizes, 1.3% initial cumulative deviation, 1.3/1.25 multipliers, long-only stance, no stop, original HYPE perpetual 3m example and 0.08% commission / 3-tick slippage. Its posted historical return/win rate/profit factor are **author-reported only** and are **not reproduced or transferred** to this BTC spot derivative.

### Independently reproduced

**None.** No TradingView/Hummingbot/Qlib backtest, event-level parity, realized fill, strategy profitability, Sharpe, drawdown, or execution result was generated. This Scout only inspected public TradingView text and pinned Hummingbot **source code**.

### Negative evidence

No full original Pine code/revision hash; no source-native broker fill ordering, maker/limit AO execution, actual 3-tick slippage, venue fees or funding, live Binance precision/partial fills, deployed controller, representative 3m DCA event-level Qlib/Hummingbot parity, or out-of-sample performance. These are explicitly **not** inferred from the public open-source badge or the backtester API. The 3m BTC spot adaptation and one-AO-per-close ordering may materially change source events and are independently specified, never silent corrections.

## Falsification plan

After separate approval to implement (not this Scout), replay a short **representative** 3m series with RSI cross-up, a gap across several AO levels, one-AO-per-bar sequencing, weighted average updates, an unprofitable crossdown 69, a later profitable crossdown, and fee/cash reconciliation. Compare controller action times, BUY/SELL quantities, quote notionals, AO indices, net PnL and `T+180s` event labels between Qlib and the pinned Hummingbot model **before** large-scale screening that uses this execution path. Falsify the mechanism if the frozen model's net expectancy fails under the same declared research cost assumptions; do not retune on OOS.

## Crypto portability

Only BTC-USDT Binance **spot 3m** and this independent quote-sized five-AO derivative are admitted for research consideration. The author's BYBIT:HYPEUSDT.P perpetual source, other pairs, higher timeframes, 3x/5x futures, 6/6/6 house DCA, real funding, next-open or intrabar fills are **separate declared research/execution variants**, not prerequisites and not automatically PASS.

## Limitations

No hard stop or automatic rescue from deep loss. Maximum ladder quote deployment is not a bound on PnL loss. Low BTC 3m volatility can reduce signal and AO counts. Same-close fills are historical simulator conventions, not guaranteed tradeable closes. Research fee is hypothetical; modeled omission of slippage differs from source and real market. No strategy-specific implementation or independent parity exists. Pine source bytes unavailable, so no lossless claim.

## Implementation status

`not-implemented`: this Markdown is a frozen research specification, not a Hummingbot controller, Qlib executable, deployable bot or live trading approval. Only a later authorized minimal implementation and representative engine-event check may materialize it for screening; no new admission flag, compiler, registry, or workflow is introduced.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. Only an independent Hermes Auditor six-gate PASS on the exact PR head may permit merge to the PASS-only main pool. The **existing signed webhook receiver** alone owns deterministic post-merge README count bookkeeping. No Scout merge, README modification, backtest, trading, container or cron change.

## Related Wiki records

None created or modified.

## Sources

- TradingView primary public source: https://www.tradingview.com/script/qgofvS9I-Dual-RSI-DCA-Long-Strategy/ (3Commas; 2026-05-20).
- Pinned Hummingbot VERSION: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION
- Pinned 3m feed: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py
- Pinned Binance spot candle parser: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py
- Pinned MARKET close-fill: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py
- Pinned position-hold and action loop: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/backtesting_engine_base.py
- Pinned order config: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/executors/order_executor/data_types.py
- Previously accepted package/source evidence (not rehashed here): https://github.com/HCH725/alpha-strategy-research/pull/414
