---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: BVLabs Alpha Supertrend Vector flip plus CHOP14 ADX14 with ATR-percent Plug close-bracket - independent BTCUSDT 1d long-flat derivative
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-08-10
sources:
  - https://www.tradingview.com/script/AR2MUnwH-Alpha-Supertrend-Vector/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alpha Supertrend Vector — independently specified ST/CHOP/ADX filtered LONG/FLAT derivative

## Provenance

**First-party public TradingView script:** BVLabs, *Alpha Supertrend Vector >_*, stable public script ID `AR2MUnwH`, published **2026-04-10**, updated **2026-08-10** (release note 08/10/2026). URL: https://www.tradingview.com/script/AR2MUnwH-Alpha-Supertrend-Vector/ . The publicly readable author description was directly inspected 2026-10-26. It labels the script open-source, but **the complete Pine source bytes, source revision hash, and numerical default input values were not retrievable** through the accessible first-party page; none are claimed to have been verified.

**Author-described mechanism, and only those source facts:** enter on a Supertrend **direction flip** rather than continuing trend state; a bearish-to-bullish flip is the long candidate and bullish-to-bearish is short. At the flip, require **Choppiness Index below** its threshold and **ADX above** its minimum; the description names `ta.dmi()` for directional strength. Freeze entry ATR as a percentage of price; calculate an ATR%-multiple take-profit and stop from average entry price; additionally apply a fixed-percentage "Plug" hard stop and choose the **tighter** of the ATR stop and Plug. The source describes stop/target orders on each bar and both sides, but does not publish verified complete executable Pine conditions or all input defaults in the accessible description. Its performance is not independently reproduced.

**Explicit, independently designed derivative — NOT a lossless or source-native implementation.** Researcher-defined changes are: (1) BTC-USDT Binance **spot 1d** instead of unspecified author market/timeframe; (2) **LONG/FLAT only**, SHORT disabled; (3) researcher-selected Supertrend ATR14 multiplier **3**, CHOP14 threshold **38.2**, Wilder ADX14 threshold **25**, locked ATR stop **1.5×**, target **3×**, Plug **3%**, and the exact seeds/recurrences below (none are asserted as author defaults); (4) evaluate the **previous completed bar's** flip/filter/exit signal on the next engine row and fill at that next row's observed close — a **one-completed-bar delayed-close** MARKET simulation, NOT original Pine fill/stop behavior; (5) stop/target are **close-triggered exit decisions**, not native intrabar stop orders, with fixed levels from the actual simulated entry fill; (6) fixed 0.001 BTC single position, 10,000 USDT initial research cash, 0.1% per-side assumed simulator cost, no DCA, 100-bar warmup, explicit pending/failure/re-entry state; (7) no opposite-flip exit, trailing, end-of-test liquidation or hidden controller defaults. These are material changes to trade events and economics. The author script itself is **not** represented as HB_READY PASS.

**Immutable derived identity:** `TV:AR2MUnwH:BVLabs:2026-08-10 | independent-v1-ST-ATR14x3-CHOP14lt38p2-ADX14gt25 | long-flip-only | close-bracket-ATR1p5-TP3-Plug3pct | prior-bar-signal-next-bar-close-fill | BTC-USDT:BinanceSpot:1d:Q0p001:fee0p001 | 2026-10-26`. Any change to arithmetic, state, delay, fee, risk or market is a different derived strategy.

**Dedup check:** At main `4f39f8d7c4941c12b9beb1bcf8b5b3665f9e0a99`, a complete nontruncated Git tree listed **365** root strategy Markdown records, excluding the two READMEs, and README stated **365**. Connected GitHub default-branch code search for exact script ID `AR2MUnwH` returned no match; PR search for ID, title, and Supertrend/ADX/Choppiness returned none. The open `research/*` PR list was inspected: the existing unmerged SuperTrend ATR-flip record is based on a **different** TradingView script `VLRj2sG9`, without this source's conjunctive CHOP+ADX gate and locked ATR%-Plug bracket. Existing BVLabs `1BJZkv2N` is a TRIX zero-cross, not Supertrend flip. Existing Supertrend+RSI/EMA variants likewise use different signals. This is a distinct triple-gated regime-flip plus fixed dual-stop mechanism, not a trivial multiplier retune. Count agreement alone is not asserted to be an independent frontmatter audit of every pre-existing record.

## Economic mechanism

The source hypothesizes that an ATR-band Supertrend **transition**, only when CHOP suggests a trending regime and ADX indicates directional strength, may capture an early trend leg. A fixed entry-volatility-based target and the tighter of two adverse-exit levels bound the **model's close-threshold exit rule**. The independently defined delayed-close spot implementation tests this hypothesis; neither source profitability nor realistic stop-loss protection is claimed.

## Signal

**Input and clock.** Exactly one real Binance BTC-USDT spot UTC **daily OHLCV** series. Bar `t` has Binance **open timestamp** `T[t]`; the whole bar becomes available at `T[t]+86400` seconds, which equals `T[t+1]` for consecutive daily bars. Require `T[t+1]-T[t]=86400`, no duplicate/missing bars, finite strictly positive O/H/L/C, `H>=max(O,C)`, `L<=min(O,C)`, finite V>=0. Never forward-fill or synthesize missing prices. All calculations below on **fully completed** bars only, using `<=t` data. Float/Decimal implementation must use fixed deterministic arithmetic and equality semantics; indicator outputs undefined when any required source input is invalid.

**Pinned mathematical definitions (all researcher-selected, not attributed to unretrieved Pine):**

1. `TR[0]=H[0]-L[0]`; for `t>=1`, `TR[t]=max(H[t]-L[t],abs(H[t]-C[t-1]),abs(L[t]-C[t-1]))`. For any nonnegative series `x`, `RMA14(x)[13]=mean(x[0..13])`, then `RMA14(x)[t]=(13*RMA14(x)[t-1]+x[t])/14` for `t>=14`. `ATR14=RMA14(TR)`, undefined before t=13.
2. `up[t]=H[t]-H[t-1]`, `down[t]=L[t-1]-L[t]`; `+DM[t]=up[t]` iff `up[t]>down[t] && up[t]>0`, else 0; `-DM[t]=down[t]` iff `down[t]>up[t] && down[t]>0`, else 0. Seed `+DM[0]=-DM[0]=0`. `DIplus[t]=100*RMA14(+DM)[t]/ATR14[t]` and `DIminus[t]=100*RMA14(-DM)[t]/ATR14[t]` when ATR>0; otherwise undefined. `DX[t]=100*abs(DIplus[t]-DIminus[t])/(DIplus[t]+DIminus[t])`; if the DI sum is zero but ATR>0, define DX=0. `ADX14[26]=mean(DX[13..26])`, then `ADX14[t]=(13*ADX14[t-1]+DX[t])/14`. ADX undefined before t=26. The named `DIminus` is a nonnegative minus-directional index, never the negation of `DIplus`.
3. `CHOP14[t]=100*log10(sum(TR[t-13..t])/(max(H[t-13..t])-min(L[t-13..t])))/log10(14)`, for t>=13 and strictly positive 14-bar high-low range and TR sum; otherwise undefined. Require `CHOP14<38.2` strictly.
4. Supertrend bands: `mid[t]=(H[t]+L[t])/2`, `BU[t]=mid[t]+3*ATR14[t]`, `BL[t]=mid[t]-3*ATR14[t]`. At t=13 seed `FU[13]=BU[13]`, `FL[13]=BL[13]`, `dir[13]=+1` (**bearish**). For t>=14: `FU[t]=BU[t]` if `BU[t]<FU[t-1] || C[t-1]>FU[t-1]`, else `FU[t-1]`; `FL[t]=BL[t]` if `BL[t]>FL[t-1] || C[t-1]<FL[t-1]`, else `FL[t-1]`. If `dir[t-1]=+1`, `dir[t]=-1` iff `C[t]>FU[t]`, else +1; if `dir[t-1]=-1`, `dir[t]=+1` iff `C[t]<FL[t]`, else -1. Thus `-1` means bullish. All comparisons are strict; equality retains previous direction. This is a **declared deterministic Supertrend variant**, not a claim of byte-identical `ta.supertrend` semantics.
5. For each fully completed **signal bar s**, `LongFlip[s] = (dir[s-1]==+1 && dir[s]==-1 && CHOP14[s]<38.2 && ADX14[s]>25 && ATR14[s]>0)`. Invalid/undefined indicator => no signal. **At least 100 consecutive valid completed bars** must exist through s (s>=99 in a zero-based contiguous series) before any signal is eligible. Historical initial position FLAT; no inherited inventory.
6. **Critical lag/causality:** a qualifying signal at completed bar **s** may produce a BUY action only when the pinned engine processes the **following row t=s+1**. The action uses indicator and state information through **s only**, not the current t OHLCV. The pinned MARKET simulator fills at the actual `C[t]` (the first supplied row's close); effective economic fill time is `T[t]+86400`, not the raw candle-open timestamp `T[t]` used by the engine index. This is deliberately **one full daily bar later** than the signal close; it is not a claimed next-open or same-signal-close fill. A last-bar signal with no following row has **no fill**.
7. Upon a confirmed full BUY fill, set `entry_price=C[t]`, `entry_atr_pct=ATR14[s]/C[s]` (ATR% frozen at **signal bar s**), `stop_atr=entry_price*(1-1.5*entry_atr_pct)`, `stop_plug=entry_price*(1-0.03)`, `stop=max(stop_atr,stop_plug)`, and `target=entry_price*(1+3*entry_atr_pct)`. Require `entry_atr_pct>0`, `stop<entry_price<target`; otherwise abort entry as invalid. The **actual modeled fill** anchors the levels; no imaginary fill price or `strategy.position_avg_price` is imported from TradingView.
8. While confirmed LONG, on engine row `t` inspect only the **previous completed bar's** close `C[t-1]`. If `C[t-1]<=stop`, issue SELL for all held BTC; else if `C[t-1]>=target`, issue SELL for all held BTC; otherwise HOLD. Exit fills at actual `C[t]` with effective time `T[t]+86400`. A source-native intrabar `strategy.exit` stop/limit is **NOT** claimed. Stop takes priority (the two thresholds are disjoint for valid levels); no opposite-flip exit. After confirmed SELL, reset frozen levels and return FLAT. On the exit row never enter, even if a new flip exists.
9. From FLAT, BUY only on the new `LongFlip[t-1]` and only if no pending order. **Never inspect C[t] to gate an order before the t-close fill:** C[t] is unknown at the t-open decision instant. At the simulated fill, debit the actual observed `0.001*C[t]*(1+0.001)`; if that exceeds available cash, **invalidate/abort the research run** rather than borrow, assume a fill, or use future prices to suppress the action. A signal cannot be converted into a guaranteed fill when price is absent. At most one action per bar; no implicit queued entry after an exit. A later entry requires a fresh new bearish-to-bullish Supertrend flip after return to FLAT.
10. Fill-confirmed state machine: `FLAT -> BUY_PENDING -> LONG -> SELL_PENDING -> FLAT`. A submitted action never changes inventory. BUY success confirms full 0.001 BTC; failed/rejected/unfilled BUY returns FLAT without retry (wait for another new flip). SELL failure leaves confirmed LONG and **retries at the next eligible engine row** regardless of whether the exit predicate persists; no phantom fill. On partial fill, invalid price, insufficient cash or unexpected executor status, halt research and flag unsupported state rather than invent a fill. Cooldown is **zero** after confirmed exit, but the fresh-flip edge rule prevents level-triggered immediate re-entry.
11. Explicitly disabled: SHORT, inverse contracts, perpetuals, leverage, borrowing, margin, funding, pyramiding, simultaneous positions, DCA/BO/SO, partial closes, intrabar orders, maker/limit/next-open fills, trailing stop, opposite-signal close, discretionary exits, same-row entry+exit, end-of-data forced liquidation, compounding and any controller-default risk behavior. No terminal forced close; mark remaining spot inventory at the **actual last available close** for research-only unrealized equity.

## Execution assumptions

**Pinned Hummingbot admission baseline:** package `20260920`, VERSION `dev-2.17.0`, pinned source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. During this Scout cycle, the connected GitHub app directly read that commit's `binance_spot_candles/constants.py`, `binance_spot_candles.py`, `strategy_v2/backtesting/backtesting_engine_base.py`, `strategy_v2/backtesting/backtesting_data_provider.py`, `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, `strategy_v2/executors/order_executor/data_types.py`, and `strategy_v2/models/executor_actions.py`. The repository's independent PR #414 earlier documented a 902/902 Python-file wheel/source identity check at this pin; this Scout did **not** rehash the wheel/image or verify installed runtime.

- **Data/market:** `BinanceSpotCandles` for `binance`, `BTC-USDT`, `1d` (the pinned constants include `1d`). Its REST parser maps Binance kline `row[0]` to the **OPEN** timestamp, with observed OHLCV in `row[1..5]`. Never confuse that timestamp with candle completion. The engine's `prepare_market_data()` maps historical `close_bt` into `close`, and `dropna()` can silently remove missing rows; therefore independently validate complete consecutive candles **before** running the engine and reject gaps rather than treat dropped rows as adjacent days.
- **Actual pinned controller/executor route:** a **strategy-specific, currently NOT implemented** `DirectionalTradingController` can calculate prior-bar indicators and issue `CreateExecutorAction(OrderExecutorConfig(...,connector_name="binance",trading_pair="BTC-USDT",side=BUY or SELL,amount=Decimal("0.001"),position_action=OPEN or CLOSE,execution_strategy=MARKET,price=None,leverage=1))`. The pinned engine iterates `update_state(row)` then `determine_executor_actions()` and passes `processed_features.loc[i:max_ts]` to `OrderExecutorSimulator`. This is a verified **model primitive**, not a claim that this strategy-specific controller has already been built.
- **Real simulator fill and costs:** the pinned `OrderExecutorSimulator` `MARKET` path fills on the **first supplied row's observed close**, records `filled_amount_quote=amount*close` and `cum_fees_quote=trade_cost*filled_amount_quote`, and terminates as `POSITION_HOLD`. Set `trade_cost=0.001` as a **researcher-selected 0.1% quote-notional per side**, NOT the author's fee, a Binance tariff, or observed execution. Modeled slippage is **zero by the simulator's idealized close-fill assumption**, not measured zero real-world slippage. No fabricated price, fill, tick-size, min-notional or spread is treated as real.
- **Position/fee ledger:** pinned `BacktestPositionHold` in `backtesting_engine_base.py` nets BUY/SELL filled base quantities, tracks weighted average cost and **gross** realized quote PnL, and accumulates quote fees separately. Cash ledger starts 10,000 USDT; BUY debit `0.001*Pb*(1+0.001)`; SELL credit `0.001*Ps*(1-0.001)`; matched roundtrip **net** `0.001*(Ps-Pb)-0.001*0.001*(Pb+Ps)`. Use actual observed close for mark-to-market. Do **not** call engine gross `total_pnl` or executor gross `net_pnl_quote` fee-inclusive net returns. Spot funding is **not applicable**, not a fabricated zero perpetual-funding cash flow.
- **State/visibility:** `BacktestingEngineBase(terminated_executors_window=None)` retains controller-visible terminated fill history; the default 3600-second window can hide daily-bar confirmations. Controller must still keep its own persistent fill-confirmed pending/position ledger and not infer holdings from action submission. The pinned final flush books last-tick `POSITION_HOLD` exposure. `BacktestingDataProvider.get_price_by_type` has a fallback `Decimal("1")` when a price is absent: this strategy **forbids** that fallback and requires the actual validated candle close, otherwise fail the run.
- **Causality limitation and explicit repair:** the engine labels each fill with **candle OPEN** timestamp even though the simulated price is that row's **CLOSE**. This derivative prevents lookahead in signal decisions by reading **only bar t-1** at engine row t, and defines economic fill time as **open[t]+86400**. Any later event replay/parity must use that effective fill time; if the implementation mistakenly treats the raw `timestamp[t]` as the economic fill time or uses `C[t]` in its signal decision, Gate 5/6 fails. This does not assert that a real order sent at open[t] could guarantee a fill at close[t]. It is a bounded, idealized daily-close simulator, with no cross-asset/timeframe synchronization, maker, intrabar or futures dependency.
- **Research authorization:** no actual controller, executable recipe, Qlib run, Paper/Testnet/Live, fees measured from Binance, or event-level Qlib/Hummingbot parity exists in this record. Existing MARKET/POSITION_HOLD primitives are reused; any newly required primitive must undergo representative engineering validation before mass screening. PASS here is a proposed six-gate **expressibility** assessment, subject to independent Hermes Auditor review, not self-certification or adoption.

## Evidence

### Source-reported
First-party BVLabs public description (2026-04-10; 2026-08-10 update): Supertrend **flip** gated by CHOP below threshold and ADX above threshold, locked entry ATR%, ATR-relative stop/target and tighter fixed-percentage Plug. Original has both directions and `strategy.exit` stop/target behavior. It supplies no verified numerical defaults or complete Pine bytes through the accessible view.

### Independently reproduced
**No strategy backtest or Pine-vs-Hummingbot replay was performed.** This cycle directly inspected the pinned Hummingbot source for actual Binance spot 1d candle interval/parser, MARKET close-fill, POSITION_HOLD netting, fee accumulation, action ordering, terminated-executor visibility and missing-price fallback. The current record is a reproducible **research specification**, not a deployed implementation.

### Negative evidence
- The native Pine code, its precise Supertrend implementation and numerical defaults were **not** verified; every derived parameter, seed, state, one-bar lag and close-based bracket is disclosed as a researcher choice.
- Intrabar source stop/target and short orders are **not** carried over; this derivative may suffer losses far beyond its nominal stop during overnight or rapid market moves.
- Similar main records trade Supertrend+RSI/EMA or BVLabs TRIX+CHOP+ADX; this version uniquely requires a Supertrend **flip** AND CHOP AND ADX and locks an ATR%-Plug exit. The open SuperTrend PR #63 cites different source ID `VLRj2sG9`.
- Neither TradingView author's returns nor any Sharpe, ROI, drawdown, profitability, Qlib parity, Survivor, HB Certified, wheel hash or live execution claim is reproduced.
- The raw candle-open timestamp is **not** evidence of same-bar-close causality. Any controller failing the declared one-bar signal lag or effective-fill-time mapping is incompatible with this identity.

## Falsification plan

If admitted and later selected, implement only the minimal strategy-specific controller using the already verified MARKET/hold primitive; verify (a) seeded RMA/DMI/ADX and Supertrend flip edges, (b) CHOP zero-range invalidity, (c) prior-bar signal vs following-row close fill time, (d) Plug tighter-stop precedence and frozen ATR%, (e) missing daily bars, rejected/partial fills and fee-inclusive cash. Compare one representative Qlib/Hummingbot event sequence **before** mass screening if this exact path introduces a new unverified execution primitive; otherwise reuse the previously verified primitive and reserve strategy-specific event parity for downstream HB certification. No test or workflow modification was performed by this Scout.

## Crypto portability

The defined research instrument is one unleveraged BTC-USDT Binance spot 1d stream; this is a bounded **choice**, not a single-pair or timeframe admission ban. The separate 7-coin / 1h-4h-1d / isolated 3x-5x / BO6-SO6-SO6 campaign would be a new declared derivative and needs independent futures accounting/cost compatibility; it is **not** a prerequisite to this record's HB_READY status.

## Limitations

Pine source-byte unavailability, author defaults, original fill semantics, real spreads, slippage, lot/tick constraints, latency, stop-order guarantees, actual trading fees and installed-wheel identity are unverified. The one-bar lag is conservative for point-in-time signal evaluation but the historical next-bar close is an idealized simulator price. A controller must never pretend its raw open-index fill timestamp is the real close time. A source-native Pine strategy is **not** established; only the explicit derivative is proposed for independent six-gate review.

## Implementation status

`not-implemented`. A PASS strategy record is **not** an executable controller, Qlib recipe or trading permission. Downstream selection with missing executable materialization follows the existing `IMPLEMENTATION_NEEDED` route, without inventing a new admission flag, registry or service.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Only the independent Hermes Auditor GitHub Webhook Review may remediate source-verifiable facts and exact-head PASS merge or close NOT_LOSSLESS. Scout never self-approves, merges or edits README.

## Related Wiki records

None; no Wiki write.

## Sources

- TradingView BVLabs first-party publication: https://www.tradingview.com/script/AR2MUnwH-Alpha-Supertrend-Vector/
- Pinned engine source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Earlier pinned-wheel evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
