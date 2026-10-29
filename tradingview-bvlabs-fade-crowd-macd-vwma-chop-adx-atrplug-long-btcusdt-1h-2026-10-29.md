---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: BVLabs Fade The Crowd bearish MACD/VWMA consensus CHOP/ADX gated long-flat ATR-Plug close bracket BTCUSDT 1h
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-04-10
sources:
  - https://www.tradingview.com/script/AjvYpg19-Fade-The-Crowd-Protocol/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BVLabs Fade The Crowd — independently specified bearish-consensus fade LONG/FLAT on BTCUSDT 1h

## Provenance

Primary first-party public TradingView open-source listing: BVLabs, **Fade The Crowd Protocol >_**, published **2026-04-10**, stable script ID **AjvYpg19**, https://www.tradingview.com/script/AjvYpg19-Fade-The-Crowd-Protocol/ ; public description read 2026-10-29. The visible listing, not a fully retrieved immutable Pine source revision, says that a conventional bearish MACD crossover with negative histogram and low touching/below VWMA can be faded with a LONG; a bullish crossover with positive histogram and high at/above VWMA can be faded with a SHORT. Both directions require low CHOP, strong ADX, a post-exit cooldown, and a flat position. It describes ATR% fixed from trigger time, TP/SL anchored to average fill, and a tighter percentage Plug stop. It does **not** expose exact original numeric defaults, full Pine source, execution-time flags, broker fills or performance. No original-Pine event-equivalence or source-reported backtest reproduction is claimed.

**This is an independently designed derived executable strategy, NOT the author's source-native strategy.** Researcher-defined changes, explicitly disclosed rather than attributed to BVLabs: Binance BTC-USDT unleveraged spot **1h LONG/FLAT only** (original short leg disabled); MACD 12/26/9, VWMA20(close,volume), CHOP14 < 38.2, Wilder ADX14 > 25; fixed five-completed-bar cooldown; Wilder ATR14 with fixed 1.5x stop, 3.0x target and 3% Plug cap; all risk conditions evaluated on **completed CLOSE** rather than source-native resting/intrabar stop/limit orders; signal on bar t, historical MARKET fill at the following completed bar t+1 close; fixed 0.001 BTC, 10000 USDT starting cash, 0.1%/side hypothetical fee, 200-bar warmup and explicit state/invalid-data rules. Every change can alter trade events; original behavior is not relabeled PASS.

**Immutable derivative identity:** `TV:AjvYpg19|BVLabs|2026-04-10|independent-derived-v1-20261029|BinanceSpot-BTC-USDT-UTC1h|MACD12-26-9-bear-cross-hist-neg|VWMA20-low-touch|CHOP14-lt38p2|ADX14-gt25|ATR14-1p5SL-3TP-Plug3pct-close-only|cooldown5|signal-t-fill-tplus1-completed-close-MARKET|Q0p001BTC-cash10000USDT-fee0p001|long-flat-noDCA|warmup200`.

Dedup at prewrite main SHA `8b0db9e8a946a8b6cfa1675cece4a525ad69f018`: 433 root-level strategy records and README 433; 15 spread PASS frontmatter samples (not a full 433-file audit). Connected GitHub main search for `AjvYpg19` and `contrarian MACD VWMA` returned no match; all open `research/*` PRs and all-state PR search for this script ID/title showed no same-source PR. The BVLabs Alpha TRIX and Supertrend Vector records use trend-following TRIX/Supertrend triggers, not this bearish MACD/VWMA **contrarian** entry plus five-bar cooldown and Plug bracket. Existing VWMA crossover/band records do not use MACD bearish-consensus inversion. Not a trivial retune of those mechanisms.

## Economic mechanism

### Source-reported

The author proposes fading an apparently confirmed crowd trade rather than following it: MACD crossover/histogram plus a price touch of VWMA identify a conventional momentum consensus; CHOP/ADX gate the market regime; a cooldown discourages rapid re-entry; ATR-derived target/stop and a tighter fixed-percent Plug stop limit intended risk. This is a hypothesis, not established alpha.

### Research interpretation

A single-sided, event-triggered contrarian long after bearish crowd confirmation, in a still-trending regime. The fixed close-only bracket tests whether delayed reversals recover enough to reach a target before the adverse completed close reaches the tighter risk bound. Unlike source-native resting stops, completed-close exits can overshoot the nominal stop materially.

## Signal

All series use **only contiguous fully completed** Binance spot UTC 1h OHLCV bars. Index t is the most recently completed bar; no repaint, intrabar decision, fitted model, future bar or external feed. Invalid/NaN/inf inputs never become zero or a signal.

- EMA(N) uses alpha=2/(N+1), first defined value seeded by SMA of the first N valid observations, then forward recursion. MACD_t = EMA12(close)_t - EMA26(close)_t; Signal_t = EMA9(MACD)_t using the same seed rule on valid MACD values; Hist_t = MACD_t - Signal_t. **BearCross_t** iff MACD_(t-1) >= Signal_(t-1) AND MACD_t < Signal_t AND Hist_t < 0; equality on current bar does not cross. Only a fresh crossing is eligible; a negative histogram without a new crossing is insufficient.
- VWMA20_t = sum(close_i*volume_i for i=t-19..t)/sum(volume_i for i=t-19..t); require all 20 finite nonnegative volumes and a strictly positive denominator. **Touch_t** iff low_t <= VWMA20_t (equality allowed). VWMA is inclusive of the completed decision bar, not session-anchored VWAP.
- True range TR_t=max(high_t-low_t, abs(high_t-close_(t-1)), abs(low_t-close_(t-1))). ATR14 is Wilder RMA14 of valid TR: first SMA14 seed then (13*prev+TR_t)/14. CHOP14_t=100*log10(sum(TR_i,t-13..t)/(max(high_i,t-13..t)-min(low_i,t-13..t)))/log10(14). Require positive finite sum and strictly positive 14-bar high-low range; CHOP_t < 38.2 strictly.
- Wilder ADX14: up=high_t-high_(t-1), down=low_(t-1)-low_t; +DM=up iff up>down and up>0 else 0; -DM=down iff down>up and down>0 else 0; first 14 valid TR/+DM/-DM values seeded with SMA14 and thereafter Wilder RMA14; +DI=100*RMA(+DM)/RMA(TR), -DI likewise; DX=100*abs(+DI-(-DI))/(+DI+(-DI)); ADX14 is Wilder RMA14 of valid DX, first SMA14 seed. Any zero/invalid denominator yields undefined, never a fabricated zero; require ADX_t > 25 strictly.
- At completed t, **ENTRY_SIGNAL_t** iff FLAT, no pending order, BearCross_t, Touch_t, CHOP14_t<38.2, ADX14_t>25, ATR14_t>0, all values finite, and cooldown clear. Capture A=ATR14_t from this signal bar. No short signal is executable. Original bearish-consensus fade is preserved conceptually; all periods/thresholds and direction restriction above are researcher pins.
- After the confirmed BUY fill at following completed bar j=t+1 with actual modeled close P=close_j, set `stop=max(P-1.5*A, P*(1-0.03))` and `target=P+3.0*A`; require P>0, A>0, stop>0, target>P and stop<P. Both levels remain frozen until flat. If any guard fails, do not create a synthetic fill or position. The tighter Plug stop is a close-price comparison, **not** a guaranteed 3% maximum realized loss.
- **EXIT_SIGNAL_k** only for a LONG position on completed k>j when close_k <= stop OR close_k >= target. If close <= stop, label STOP; if close >= target, label TARGET. They are mutually exclusive for valid P,A. Exit order is queued for the **following** completed bar k+1 and sells the entire confirmed 0.001 BTC at that bar's actual modeled close. No exit fills at a touched high/low, no resting stop/limit, no stop-market, no intrabar or gap fill, no trailing/breakeven/time/opposite-MACD exit.
- Event priority: existing pending BUY/SELL is processed before any new signal; while LONG evaluate exit only; while FLAT evaluate entry only; on a fill bar no new decision may enqueue another order. At end of available data, an unfilled pending order is discarded with no invented price. An exit cannot precede its fill. No immediate stop/TP evaluation on the entry fill bar.
- State: FLAT -> PENDING_BUY -> LONG(frozen A/P/stop/target, quantity=0.001) -> PENDING_SELL -> FLAT. One position and one pending order maximum; full-fill-only historical model, no partial fill, pyramiding, averaging, BO/SO, DCA, multi-pair exposure or concurrent orders. Failed/invalid BUY remains FLAT and cannot reuse the original cross; failed/invalid SELL leaves LONG, with no duplicate SELL while pending. Exit fill at bar j sets `last_exit_bar=j`; bars j+1 through j+5 are blocked, so earliest new entry signal is j+6 if a fresh eligible BearCross prints. Initial state has no cooldown. No re-entry on exit bar.

## Required data

Single Binance BTC-USDT spot 1h stream: open timestamp, open, high, low, close, base volume, continuous 3600-second UTC intervals. Validate finite OHLC, positive OHLC prices, high>=max(open,close), low<=min(open,close), nonnegative finite volume and monotone gap-free timestamps. Indicators use high/low/close/volume only, but open is checked for candle integrity. First 200 contiguous completed bars are warmup-only, no orders. Indicator seed state is reset after a gap; block signals/fills until 200 new contiguous completed bars exist. A preexisting long remains long during missing-price gaps, with no fabricated stop, target, or forced price; this is a severe disclosed gap risk. Do not substitute `Decimal("1")` for missing prices.

Binance Spot REST klines label row[0] as the **open** timestamp. For strategy causality, convert each fully completed 1h bar to effective timestamp `open_timestamp+3600` before the engine's feature/action rows; exclude still-forming bars. A signal decided at E[t] can only be filled at E[t+1] (next completed close), never earlier. Bar t+1 close is not used to decide the original t signal. No multi-timeframe alignment, non-OHLCV feeds, funding, mark/index price, borrow, order book or futures inputs.

## Execution assumptions

**Pinned engine:** Hummingbot package `20260920`, literal `hummingbot/VERSION=dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. GitHub connector inspected that exact commit's `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`, `executors_simulator/order_executor_simulator.py`, `backtesting_data_provider.py`, `executor_simulator_base.py`, `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py`, `constants.py`, `hummingbot/strategy_v2/executors/order_executor/data_types.py`, and `hummingbot/VERSION`. Source `setup.py` contains version string `20260729`; this is not falsely represented as the installed wheel's distribution version. Earlier independently reviewed PR #414 reports 902/902 packaged Python files byte-identical to this commit with package `20260920`; the wheel was **not rehashed this cycle**, so Auditor must rely on or revalidate that separate proof.

**Verified applicable path:** BinanceSpotCandles `/api/v3/klines`, parser row[0] timestamp plus OHLCV and supported `1h`; one BTC-USDT DirectionalTradingController emitting `CreateExecutorAction(OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),execution_strategy=MARKET,leverage=1))`; `BacktestingEngineBase.simulate_execution` per-row controller/action loop; `OrderExecutorSimulator` MARKET first supplied row `close` fill, `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, `CloseType.POSITION_HOLD`; `BacktestPositionHold` nets BUY/SELL quantities and average cost/realized quote PnL. To implement **t signal -> t+1 close fill**, controller stores t's event, emits the MARKET action only on completed t+1; this is a declared retrospective close-fill simulation, NOT a live exchange order promise or Pine-native bracket fill.

**State visibility and accounting:** construct `BacktestingEngineBase(terminated_executors_window=None)` because default 3600-second terminated-executor view can prune older fills before controller sees them; maintain independent controller-memory pending and confirmed-fill ledger (not just the current executor list), and never infer FLAT from the bounded view. The pinned engine routes POSITION_HOLD fills into `BacktestPositionHold` on subsequent update and final flush; require unique fill IDs and reconcile quantity/price/fees. Net realized PnL is `BacktestPositionHold.realized_pnl_quote - BacktestPositionHold.cum_fees_quote`, not the OrderExecutor gross PnL nor unadjusted engine total_pnl. No synthetic close, missed confirmation or duplicated position. A strategy-specific controller is **not implemented**; this is verified capability evidence, not a claim of completed deployment.

**Economics:** initial cash 10000 USDT; on BUY require `cash >= 0.001*P*(1+0.001)` at actual modeled fill, debit notional+fee; on SELL require confirmed 0.001 BTC inventory, credit `0.001*P*(1-0.001)`; `trade_cost=0.001` per fill is a hypothetical research fee, not observed Binance taker fee. Modeled slippage=0 is an explicitly artificial simulator convention, not a real-market assertion. Unleveraged spot has no periodic perpetual funding; no borrowing, leverage, margin, liquidation, mark-price, futures or actual funding cashflows. This backtest path does not verify venue lot/tick/min-notional quantization or live fills, and close-price MARKET fill is idealized. Cash/inventory ledger must be checked against modeled POSITION_HOLD and fee ledger; precision residuals are not hidden. If missing price/invalid fill/cost prevents reconciliation, fail closed, never fabricate a fill.

## Evidence

### Source-reported

BVLabs's 2026-04-10 public TradingView page describes MACD histogram/cross + VWMA touch crowd signal, opposite-direction entries, ADX/CHOP regime filters, cooldown, trigger-bar ATR%, fill-anchored locked ATR TP/SL and tighter Plug stop. No complete accessible Pine program or numeric default settings in the visible listing. No author performance statistics adopted.

### Independently reproduced

GitHub connector read the pinned Hummingbot source files above, confirmed Binance Spot `1h` OHLCV/open-timestamp parser, controller row processing, MARKET first-row close fill, fee formula, POSITION_HOLD ledger, and terminated-view behavior. This is **source-path inspection**, not an executed strategy backtest, wheel rehash, parity test, or real exchange execution. PR #414 provides earlier independent wheel/source binding evidence.

### Negative evidence

- Original BVLabs short leg, source-native immediate entry, intrabar resting TP/SL, and broker-emulator behavior are **not** replicated; all are disabled/replaced in this independent derivative. Neither author defaults nor source-native losslessness is claimed.
- All 12/26/9, 20, 14, 38.2, 25, 1.5/3, 3%, 5 bars, 200 bars, 0.001 BTC, fee and fill-time pins are researcher choices, not author defaults.
- The Plug is **not** a guaranteed 3% loss cap under close-only execution; the next completed close can gap beyond it. Gaps can strand an open position.
- No real maker/intrabar/futures path, real exchange fee/precision, source backtest, Qlib parity, survivor profitability, or live authorization is demonstrated.

## Falsification plan

Later research only: freeze this exact identity; compare complete IS/OOS event sequences against (a) identical MACD/VWMA inversion without CHOP gate, (b) without ADX gate, and (c) no cooldown, holding the same cost/close-bracket semantics. Test whether regime/cooldown exclusions improve net results without overfitting; report all bars, skipped signals, stop overshoots, fees, drawdown and no-trade periods. Representative Qlib/Hummingbot event-level parity is required before mass Qlib screening on any unverified execution primitive. **No test was run in this Scout cycle.**

## Crypto portability

Only BTC-USDT Binance spot 1h is the frozen candidate; the original source describes both directions, but this independent derivative deliberately disables shorts. Other coins, timeframes, futures, DCA and leverage are optional downstream **new derivative experiments**, not HB_READY admission bans or implied compatibility.

## Limitations

Primary-source description rather than immutable Pine bytes; this is a fully specified researcher-derived mechanism, not a Pine clone. No actual fees, liquidity, fills, quantization, slippage or profitability proof. Close-only risk exits and data gaps can exceed the intended stop; no guaranteed capital protection. The pinned wheel/source mapping is inherited from PR #414 and not revalidated here; `setup.py` distribution-version literal differs from the previously reported installed wheel package label. Dedicated controller and Qlib executable recipe remain absent; if selected, use the existing IMPLEMENTATION_NEEDED route without inventing another admission flag.

## Implementation status

not-implemented. HB_READY PASS is a **Scout proposal** that the fully specified derivative is expressible with the cited pinned primitives, subject to independent Auditor source and six-gate review; it is not an executable artifact, strategy-specific parity, or approval to trade.

## Adoption boundary

status: research-only; implementation_status: not-implemented; adoption: not-approved; approval_scope: research-only. No Paper/Testnet/Live, merge, Qlib/Hummingbot run, cron, container or workflow change.

## Related Wiki records

None; no Wiki write.

## Sources

- https://www.tradingview.com/script/AjvYpg19-Fade-The-Crowd-Protocol/
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- https://github.com/HCH725/alpha-strategy-research/pull/414
