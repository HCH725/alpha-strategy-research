---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "FMZ 504075 SMA 8/30 pullback with ATR-multiple exits — independent BNB-USDT spot long-flat 3d derivative"
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-08-07
sources:
  - https://www.fmz.com/strategy/504075
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SMA 8/30 pullback with ATR-multiple exits — independent long-flat derivative

## Provenance

來源語義補充（獨立審查）：公開頁面所附完整 Pine 的 ATR14 是逐根更新的 series；持有多倉期間，每次計算都以當時 ATR 與 position_avg_price 重新計算並提交 SL/TP，並非只在入場時凍結 ATR。本文既有衍生版則固定使用訊號根 ATR[u] 與 C[u]，整筆交易不更新 SL/TP；這同時改變參考價格與波動距離更新規則，不只是把 intrabar stop/limit 換成 close-evaluated MARKET。完整解碼來源快照 SHA256：6cd459a51a223a2f33d63a9402b3c55f98a78518dc7e9b11c416d32ad837a0a1。既有衍生規則、識別與原始來源紀錄均保留。

**Primary source (directly read 2026-10-29):** FMZ public strategy **504075**, *多周期均线回调与ATR动态止盈止损策略 | Multi-Timeframe SMA Pullback with ATR Dynamic Exit Strategy*, author handle **ianzeng123** (same author as merged Alpha records FMZ 512203 and FMZ 482829), type 通用策略, 创建日期 **2025-08-07 11:14:27**, last-modified label shown only as relative **1 年前** on the live page, tags `ATR,SMA,TP/SL,移动平均线,回调策略,动态止损`, https://www.fmz.com/strategy/504075 . Live page fetched this cycle over HTTPS (**736,512 bytes** served): the complete Pine v6 decision text is embedded in the served page stream blob without any login (the login overlay truncates only the display copy, not the rule text — same pattern as merged Alpha records FMZ 512203/482829). The full listing (1,600 chars decoded, ending cleanly on the second `plot(` visuals line) was read end to end this cycle, from the `/*backtest` header through both entry/exit pairs.

**Declaration-line census on the verbatim program:** 1 `strategy(` (`"8/30 SMA Pullback + ATR Exits (Crypto)"`, `overlay=true`, `default_qty_type=strategy.percent_of_equity`, `default_qty_value=100`, `initial_capital=200`); 2 `strategy.entry` (`"Long"`/`strategy.long`, `"Short"`/`strategy.short`); 2 `strategy.exit` (`"Exit Long"`/`"Exit Short"`, each with both `stop=` and `limit=`); 0 `strategy.close` / 0 `strategy.order` / 0 `strategy.close_all`; 0 `pyramiding` / 0 `process_orders_on_close` / 0 `calc_on_every_tick` / 0 `commission_` / 0 `slippage` (Pine defaults govern: no pyramiding, confirmed-bar calculation, next-bar-open market fills, no modeled cost); 4 `input.*` (`smaFastLen=8`, `smaSlowLen=30`, `atrMultSL=1.2`, `atrMultTP=2.0`; ATR length fixed at 14 in code, not an input); 2 `ta.sma` / 1 `ta.atr`; 0 `request.*` / 0 `security(` / 0 `timeframe.` / 0 `volume` / 0 `nz(` / 0 `na(`. The `/*backtest` header pins `period: 3d`, `basePeriod: 3d`, `exchanges: [{"eid":"Futures_Binance","currency":"BNB_USDT"}]` (Binance **perpetual futures**, demo window 2024-08-07 → 2025-08-05). The page title claims "Multi-Timeframe", but the verbatim code reads a single frame with zero higher-timeframe machinery — pinned below as a source-title misnomer, not a second timeframe.

**Independent derived strategy, NOT source-native reconstruction:** preserve the exact pullback construction (price below fast SMA while fast SMA is above slow SMA, and mirror) with the fixed 8/30 lengths, the ATR-14 multiple exits (1.2× stop, 2.0× target off the entry reference), and the single-frame 3d decision rhythm. Researcher-defined alterations: (a) disable the short leg entirely (LONG/FLAT only); (b) port `Futures_Binance BNB_USDT` to Binance BNB-USDT **spot** 3d (no perpetual, no funding leg by construction; frame and coin unchanged); (c) fix all four source-default inputs (no sweep; ATR length pinned at 14); (d) replace Pine full-equity sizing with a fixed 0.2 BNB order; (e) evaluate signals on the fully completed prior bar and simulate MARKET fills at the next completed bar's close, rather than Pine's default next-bar-open fills; (f) convert the intrabar stop/limit exits into bar-close-evaluated MARKET exits against entry-frozen SL/TP levels with stop-first priority (same conversion class as merged Alpha PRs #590/#592); (g) pin the Pine-default no-pyramiding behavior as an explicit single-position gate with flat-gated re-entry and no same-bar reverse/re-enter; (h) model a hypothetical 0.1%-per-side fee (the source declares no commission; this fee is a researcher assumption, not a source fact); (i) fix a 100-bar warmup and explicit pending/fill state conventions. Pine's `ta.sma`/`ta.atr` seed bit-identity is not claimed; the derivative pins the stated arithmetic (SMA-seeded, Wilder ATR) as its own executable rule.

**Immutable derivative identity:** `FMZ:504075|ianzeng123:2025-08-07|independent-derived-v1-sma8-30-pullback-atr14x12x20|BinanceSpot:BNB-USDT:3d|LONG-FLAT|0.2BNB|prior-complete-signal-next-complete-close-MARKET|SL-TP-frozen-stopfirst|fee0.001|warmup100|2026-10-29`. Changing any formula, threshold, timing, market, risk, cost or direction creates a different derivative.

## Economic mechanism

### Source-reported

The page prose presents a trend-plus-pullback entry priced by two SMAs: the fast/slow SMA stack names the trend, and a close on the "wrong" side of the fast SMA is read as a discounted with-trend entry rather than a reversal. Each position then carries a volatility-scaled bracket — stop at 1.2× ATR against the entry, target at 2.0× ATR with it — for a theoretical 1.67:1 reward-to-risk per trade. No source performance metric is adopted.

### Research interpretation

This is a **discounted-trend-entry with a volatility bracket**: the traded thesis is that buying a pullback under a still-rising fast SMA captures the prevailing drift at a better price than chasing, while the ATR bracket standardizes every trade's risk in volatility units so that choppy and trending tapes risk comparable amounts per entry. The fixed 2.0/1.2 multiple makes expectancy hinge on the win rate clearing roughly 37.5% net of the modeled fee, not on catching long trends — winners are cut at a fixed multiple, so a slow grind that never reaches +2 ATR units round-trips into the stop. The failure mode is plain: in a range, the SMA stack whipsaws and every "pullback" is actually the start of the opposite leg, printing repeated fee-paying entries that stop out; a gap across 3d closes jumps clean over both frozen levels. No profitability is asserted.

## Signal

來源對照：原始 Pine 在每根持倉計算時以該根 ATR14 更新相對平均入場價的 1.2 倍止損與 2.0 倍止盈；以下第 6／7 點則是研究者已宣告的訊號根 ATR 凍結版本，不聲稱保留來源的逐根 ATR 更新行為。本補充不改動以下任何公式、優先序或狀態。

**Gate 1 — exact researcher-pinned arithmetic.** Index completed UTC 3-day bars by `t=0,1,...`. Use real Binance BNB-USDT spot `O[t],H[t],L[t],C[t]`; volume is not read. A bar with missing/nonfinite/non-positive close, or with `H<max(O,C)` / `L>min(O,C)`, is invalid; never interpolate.

1. Pinned inputs: `FAST=8`, `SLOW=30`, `ATRLEN=14`, `MULT_SL=1.2`, `MULT_TP=2.0`. No other parameter exists; the ATR length is pinned at 14 exactly as coded.
2. `SMA_N[t]` is undefined for `t < N-1`; `SMA_N[N-1]=mean(C[0..N-1])`; for later bars the standard rolling mean of the prior N closes. `smaFast=SMA_8`, `smaSlow=SMA_30`; both defined iff `t >= 29`.
3. True range `TR[t]=max(H[t]-L[t],|H[t]-C[t-1]|,|L[t]-C[t-1]|)` for `t>=1` (`TR[0]=H[0]-L[0]`). `ATR[t]` undefined for `t < 14`; `ATR[14]=mean(TR[1..14])`; for later bars Wilder recurrence `ATR[t]=(13*ATR[t-1]+TR[t])/14`. A non-positive ATR is degenerate (see guard 6).
4. On simulator bar `t` **only after its close**, evaluate with the already-completed **previous** bar `u = t-1`. `longSignal[u] = (C[u] < smaFast[u]) and (smaFast[u] > smaSlow[u])`, requiring all three series defined at `u`. This mirrors confirmed-bar semantics: no current-bar `t` indicator may influence the action; `C[t]` is solely modeled fill-price/cash-check data, never a signal input.
5. If confirmed FLAT and not pending, `longSignal[u]` queues one BUY of 0.2 BNB at simulated `C[t]` subject to warmup/affordability/guards below. No exit predicate is consulted while FLAT.
6. At entry computation, freeze off the signal bar: `SL = C[u] - MULT_SL*ATR[u]`; `TP = C[u] + MULT_TP*ATR[u]`. Entry guards (all required): `ATR[u]` finite and `> 0`; `TP > C[u] > SL` strictly; otherwise queue nothing. With `ATR>0` this holds structurally; the guard exists only for degenerate zero-range bars. The source computes its levels off the fill average price; freezing off `C[u]` is a disclosed researcher simplification (same class as merged Alpha PR #592).
7. If confirmed LONG and not pending: on completed bar `t` with `u = t-1`, (i) if `C[u] <= SL`, queue one SELL of the confirmed 0.2 BNB at simulated `C[t]` (stop, checked **first** — pinned stop-first priority when both levels are touched by the same close); (ii) else if `C[u] >= TP`, queue the same SELL at simulated `C[t]` (take-profit). Never re-enter on the same bar a SELL is queued. The entry predicate is not consulted while LONG.
8. There is no opposite-signal exit (short leg disabled), no trailing order, no time exit, no scale-out, no cooldown, no pyramiding, and no end-of-sample forced liquidation. An unclosed final position remains open, marked at the last observed valid price only. Both `plot(` visuals have no decision function and are pinned as display-only.

**Gate 2:** LONG/FLAT on Binance BNB-USDT **spot**, leverage 1, short side explicitly disabled. **Gate 3:** complete pullback entry, frozen ATR-multiple stop exit, frozen ATR-multiple take-profit exit, and intentionally absent further risk legs as specified above (verified dual `stop=`+`limit=` in source: two `strategy.exit` lines, zero `strategy.close`/`strategy.order`).

## Position, risk and state

**Gate 4:** starting research cash `10,000 USDT`, initial inventory `0 BNB`, fixed single-unit order quantity `Decimal("0.2") BNB`, maximum one open position and one pending action. State is `FLAT -> BUY_PENDING -> LONG -> SELL_PENDING -> FLAT` **only after an observed filled executor**, not on signal submission. The source's Pine-default no-pyramiding is preserved as an explicit single-position gate (same strictness as source, disclosed). Reject unaffordable BUY if `cash < 0.2*C[t]*(1+0.001)`; no negative spot cash, leverage, fractional extra unit, compounding or partial-position trading. If no valid positive close exists, no order. Failed/unfilled actions must not create phantom inventory; maintain pending state until a documented fill or failure is reconciled, with no automatic retry. A failed BUY returns to FLAT only after explicit failure; a failed SELL retains LONG (with unchanged frozen SL/TP) and waits for a new exit predicate. No explicit cooldown after a confirmed exit beyond the no-same-bar-reentry rule. Pyramiding, DCA, simultaneous strategies and safety orders are disabled.

The fixed size is a backtest design, not an assertion of exchange lot/min-notional viability. Frozen SL/TP levels do not trail: gap risk across 3d closes jumping over both levels is real and undisguised (a close beyond TP after a close beyond SL still exits as a stop under the pinned priority only when evaluated on the same bar; sequential closes apply in order).

## Required data and causality

**Gate 6:** require at least **100 consecutive fully completed** UTC 3-day OHLCV bars before the first signal/fill; the structural minimum is 32 (SMA-30 clearance plus the one-bar signal lag plus the one-bar signal-to-fill lag; ATR clears at 14). A Binance 3-day bar opening at `T[t]` is not complete before `T[t]+259200 seconds`. Predicates computed on completed bar `u=t-1` are known before bar `t` completes (confirmed-bar semantics); the modeled fill at `C[t]` is assigned **effective time** `T[t]+259200`, never the raw Kline opening label `T[t]`. A completed-close MARKET simulator fill is a bounded historical modeling convention, **not** a claim that a live order can execute at a known historical close. No future prices, higher-timeframe partial bars, repainting pivots, full-sample fitted values, negative shifts, hindsight optimization or imputed candles. The header's `basePeriod: 3d` equals the single decision frame; no second timeframe is read (zero `request.`/`security(`), so the derivative pins a single 3d frame despite the source title's "Multi-Timeframe" wording. No volume or external feed is read.

Every bar must have a strictly consecutive UTC 3-day timestamp and valid OHLC. On a missing/invalid/out-of-sequence bar, generate no new signal or fill and **retain** any confirmed existing spot position; do not synthesize an exit. After continuity is restored, resume decisions only after a fresh 100-bar warmup. The controller must never use the current bar's still-forming close to construct a signal. Undefined SMA/ATR, non-positive closes and degenerate zero-range bars deterministically yield no signal — no invented tie-break.

## Execution assumptions

來源／衍生執行邊界補充：原始 stop/limit 價格會隨每根當時 ATR 重新提交；本文已宣告的 MARKET close 出場使用入場計算時凍結的 C[u] ± ATR[u] 倍數。凍結 ATR 距離本身也可能改變出場事件，即使先隔離成交時序與參考價格差異亦然；不得把本模型視為來源動態 ATR bracket 的忠實重現。

**Gate 5 — actual inspected pinned engine path (re-verified this cycle at source commit, not a generic API assertion):** admission package `20260920` (policy label, see disclosure), Hummingbot VERSION `dev-2.17.0` (read this cycle from `hummingbot/VERSION` at the pinned commit, 11 bytes), source commit `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This cycle fetched the pinned tree over HTTPS and verified: `backtesting_engine_base.py` (39,071 bytes), `backtesting_data_provider.py` (8,823 bytes), `order_executor_simulator.py` (3,913 bytes), `binance_spot_candles.py` feed (3,924 bytes), feed `constants.py` (993 bytes; REST `https://api.binance.com` + `CANDLES_ENDPOINT /api/v3/klines` + `INTERVALS` including **`3d`**, so the source-native 3d frame needs no timeframe adaptation). No claim is made about a different engine build.

- **Market/data:** `BinanceSpotCandles` exposes REST Kline O/H/L/C rows; `get_exchange_trading_pair` strips `-`, so `BNB-USDT` maps to the exchange symbol. Pin `connector_name="binance"`, `trading_pair="BNB-USDT"`, one 3d feed, no secondary timeframe, cross-asset join, funding, mark price or order-book requirement. No volume feed is needed (this derivative reads no volume).
- **Controller:** a strategy-specific `ControllerBase` implementation (not yet written) computes the exact SMA/pullback/SL/TP arithmetic and prior-bar predicates on completed candles. `BacktestingEngineBase.run_backtesting` (pinned line 225, `trade_cost` parameter) runs `simulate_execution` (line 241/269), which per row calls `determine_executor_actions` (line 284) and dispatches `CreateExecutorAction` with `OrderExecutorConfig(side=BUY/SELL, position_action=OPEN/CLOSE, amount=Decimal("0.2"), execution_strategy=MARKET, leverage=1)`. The generic executor does **not** compute the pullback gate or implement this controller automatically.
- **Fill/clock:** inspected `OrderExecutorSimulator.simulate` (line 10) sets MARKET fill timestamp to the **first supplied row** (lines 22–24) and fill price to that row's **close** (line 56); `cum_fees_quote = trade_cost * amount_quote` (line 62); `CloseType.POSITION_HOLD` is emitted on fill (line 70). Here row `t` uses only signal inputs from `t-1`, and the simulator's fill `C[t]` is effective only at `T[t]+259200`. The engine's raw `timestamp_bt` and backward `merge_asof` are bar-**open** labels; interpreting them as completed-bar decision or fill times would be future leakage. An implementation failing to normalize effective close times is **not** compliant.
- **Fill-confirmed position:** the engine nets opposite BUY/SELL base fills into a hold ledger with weighted entry cost, gross realized PnL and `cum_fees_quote`. The default terminated-executor controller visibility is bounded in seconds (constructor line 164); use `BacktestingEngineBase(terminated_executors_window=None)` or a durable equivalent plus a controller-side pending/fill ledger. `positions_held` can lag an executor's fill by a controller tick; no duplicate BUY/SELL while a prior MARKET fill is pending reconciliation. Never infer a fill from action creation alone. Both exits map to plain MARKET closes on completed bars — the intrabar stop/limit pair is converted to close-evaluated MARKET exits, so no stop/limit legs, no intrabar ordering, no position-executor TP/SL machinery, hence no novel execution primitive beyond the representative MARKET OrderExecutor path reviewed in merged Alpha PR #414 (same conversion class as merged Alpha PRs #590/#592).
- **Cash/fees:** `run_backtesting(trade_cost=0.001)` is a **hypothetical 0.1% fee on each filled side** (researcher assumption; the source declares no commission), charged in quote currency as `trade_cost * amount * fill_close`. For buy price `Pb`, sell `Ps` and `Q=0.2`, modeled net realized quote PnL = `Q*(Ps-Pb) - 0.001*Q*(Pb+Ps)`; quote cash is decremented by buy notional plus fee and credited by sell notional minus fee. Gross PnL and fee accumulators are separate, so a gross PnL series is **not** fee-inclusive net equity. This fee is **not** the user's or Binance account's realized tariff.
- **No fabricated economics:** spot has no perpetual funding payment; this is **not** a claim of zero perpetual funding. The inspected MARKET simulator does not independently reproduce order-book spread, impact, slippage, latency, partial fills or exchange minimums. Those remain unverified real costs and execution constraints, not assumed real-world zeros. `BacktestingDataProvider.get_price_by_type` falls back to `Decimal("1")` when price is missing (pinned lines 132–140): this fallback must be explicitly rejected for BNB price/cash/fill accounting. Use actual positive finite `C[t]` only. Maintain Decimal ledger quantities and reconcile any simulator float roundoff; no fabricated prices.

**Capability boundary and package disclosure:** a single spot 3-day candle feed and MARKET completed-close fill model with a position-hold ledger is supported by the pinned inspected path. The source's Pine-default next-bar-open fills, intrabar stop/limit touch semantics, full-equity sizing, short leg, futures venue and exact Pine float semantics are **not** claimed. The `20260920` package label is retained as a policy label only: this cycle verified behavior at source commit `8b0e067` and invents no package-to-commit mapping; sibling PASS records are engine-path evidence only, never proof of this derivative. This derivative is not a source-native equivalence assertion.

## Evidence

### Source-reported

FMZ 504075, ianzeng123, created 2025-08-07 (modified label relative-only on the live page): SMA-8/SMA-30 stack with price-vs-fast-SMA pullback triggers (`close < smaFast and smaFast > smaSlow` long / mirror short), ATR-14 × 1.2 stop and × 2.0 target as `stop=`/`limit=` exits off the entry average price, fixed four defaults, no close/order machinery. Original venue Binance perpetual-futures BNB_USDT, demo window 2024-08-07 → 2025-08-05, decision `period: 3d`/`basePeriod: 3d`. No source performance metric adopted.

### Independently reproduced

**No independent performance or Pine-parity backtest reproduced.** This cycle read the live FMZ page stream (736,512 bytes served over HTTPS; full 1,600-char Pine v6 listing decoded end to end) and the pinned Hummingbot sources (VERSION, engine base, data provider, order-executor simulator, spot candle feed + constants — sizes and cited lines verified above, including `3d` in `INTERVALS`), but ran no Qlib/Hummingbot backtest, no market replay, and no strategy controller. Six-gate PASS is the Scout's **proposed research admission assessment**, subject to the independent Hermes Auditor; it is not an auditor verdict, Survivor designation, economic performance claim or trading approval.

### Negative evidence

Exact Pine float bit-identity with `ta.sma`/`ta.atr` is not reproduced here; the derivative pins the stated formulas (SMA-seeded means, Wilder ATR, completed-bar pullback predicates) as its own executable rule. Actual Binance fees, lot/tick constraints, real partial fills, package wheel byte identity, and future implementation correctness remain unverified. Any controller that reads bar `t` close while claiming a `t-1` decision, treats raw bar-open labels as close timestamps, silently uses a missing-price fallback, double-counts position holds, "corrects" the pullback into a cross-above-fast-SMA breakout, converts the frozen close-evaluated stop/TP back into intrabar stop/limit orders, re-enables the short leg or pyramiding, trails SL/TP after entry, or reads a second timeframe under the source title's "Multi-Timeframe" wording fails the stated Gate 5/6 contract. The short leg, full-equity sizing, intrabar fills, Pine float exactness and both display-only plots are explicitly out of scope, not silently preserved.

**Six-gate summary:** (1) pinned SMA-8/30 pullback plus ATR-14 1.2×/2.0× arithmetic, fixed four defaults, completed-bar predicates, flat-gated entries; (2) spot LONG/FLAT, shorts disabled; (3) exact pullback entry, frozen ATR stop plus frozen ATR target with pinned stop-first priority, deliberately disabled further legs; (4) fixed one-unit 0.2 BNB, fill-confirmed pending state, explicit single-position gate, no DCA/pyramiding; (5) inspected pinned spot 3d candle → custom controller → MARKET OrderExecutor → POSITION_HOLD and quote-fee ledger with price/time guards, no novel primitive; (6) 100 contiguous completed bars (structural 32), one-bar-lag predicates, no future-data use.

## Dedup and falsification plan

At pre-write `main` SHA `14086580a973c92742ae3a400751cf6e00120652`, 431 root-level strategy Markdown records matched README's pool count. No record cites FMZ `strategy/504075` or this rule identity (`504075` search returns zero strategy records; `8/30` SMA-pair search returns zero). Closest shape neighbours, all fenced as different: `tradingview-duchu-ema50-200-pullback-rsi-sma-one-shot-long-btcusdt-1h-2026-10-25.md` (EMA-50/200 cross plus RSI-plus-distance gate, one-shot long-only — different trend construction, different gate, no ATR bracket); `forven-ema-rsi-pullback-reclaim-long-flat-solusdt-1h-2026-10-17.md` and `forven-vwap32-ema96-rsi-gated-pullback-long-flat-ethusdt-15m-2026-10-24.md` (RSI-gated EMA/VWAP reclaim, no SMA-stack pullback, no ATR-multiple bracket); `double-seven-connors-pullback-long-btcusdt-1d-2026-10-09.md` (Connors RSI pullback ladder — different entry family); `rvi-swma-cross-ema-stack-atr-stop-target-two-sided-btcusdt-1h-2026-10-11.md` (RVI cross trigger with an EMA stack — different trigger statistic); `tradingview-jbdorji-sma50-rsi30-volume20-atr14-close-bracket-long-btcusdt-1d-2026-10-27.md` (SMA-50/RSI-30/volume-gated bracket — different gate and no pullback construction). No pool record enters on price deviating from a fast SMA inside an SMA-stack trend with a dual ATR-multiple bracket. Open `research/*` PRs (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593) cover Williams-channel, Gaussian-StochRSI, SuperTrend, Chandelier, SSL, Swift-MA, forven CCI, AdxSmas, ClucMay, Heracles and Vinicius-Supertrend lanes — different mechanisms and sources.

Future tests (not performed): hand-calculate SMA/pullback/SL/TP transitions on frozen consecutive bars; test the `ATR==0`, undefined-SMA, non-positive-close and missing-bar no-signal guards; test stop-first priority on a bar touching both frozen levels, missing-bar warmup reset and cash guard; reconcile fill effective timestamps, BUY/SELL sides, position netting and each fee against the pinned simulator. Only after representative Hummingbot/Qlib event-level execution-path parity may this strategy path enter mass Qlib screening. This is **not** a new admission gate or a requirement for each candidate to rerun generic primitive validation.

## Crypto portability

This derivative is specified for Binance BNB-USDT spot 3d only. The SMA-8/30 stack rhythm and the ATR-14 × 1.2/2.0 bracket are calibrated to BNB-scale volatility and 3d bar geometry; no transfer to other symbols, timeframes or venues is asserted. The 6/6/6 campaign DCA overlay, futures leverage and multi-coin universe are not part of this derivative.

## Limitations and adoption boundary

來源差異補充：原始 ATR bracket 是逐根隨 ATR 擴張／收縮，並非入場固定風險距離；本衍生版刻意凍結 ATR[u]，因此失去這項來源適應性，與參考價格改用 C[u]、收盤判斷及延後成交是不同的事件差異。例如隔離其他差異，參考價 100、入場 ATR 10、後續 ATR 5 時，來源當根 TP 為 110，而凍結版本 TP 仍為 120；close=112 對兩者的 TP 判斷不同。此為公式反例，不是成交模擬或績效證據。

This is an independent derived hypothesis, not a faithful reproduction of the FMZ Pine source. It inherits a stack-whipsaw weakness: in ranges the fast/slow SMA stack flips repeatedly and each "pullback" entry is faded by the opposite leg, printing fee-paying round trips that stop out; the frozen 2.0× target further demands roughly a 37.5% win rate net of fees that ranging markets rarely supply. The close-evaluated stop/TP conversion lags the source intrabar exits by up to a full 3d bar, so fast reversals give back more than the source backtest implies, and 3d gaps jump over both frozen levels with no slippage accounting. Freezing SL/TP off the signal close rather than the fill average price (source semantics) shifts both levels whenever the fill bar gaps. The fixed 0.2 BNB size does not transfer to other symbols. No positive return, real trading viability, Qlib parity, OOS result, Survivor/HB Certified status, Paper/Testnet/Live authorization or deployment is asserted. Optional campaign coins/timeframes, DCA BO/SO 6/6/6 and futures leverage are not entry requirements and are not part of this derivative.

**Implementation status:** `not-implemented`. **Adoption:** `not-approved`. **Approval scope:** `research-only`. Independent Hermes Auditor GitHub Webhook Review alone owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS closure. This Scout does not approve, merge or alter `main`.

## Implementation status

`not-implemented`: no controller, executor config, replay recipe or backtest artifact exists for this derivative. HB_READY PASS here is research admission only (see Evidence); the `IMPLEMENTATION_NEEDED` engineering route applies if this record is ever selected for execution, without redoing HB_READY.

## Adoption boundary

`not-approved`, `approval_scope: research-only`. No live, Paper, Testnet or deployment authorization is granted or implied. Downstream use is limited to model-consistent research under the pinned engine path stated above.

## Related Wiki records

None.

## Sources

- FMZ primary source: https://www.fmz.com/strategy/504075 (ianzeng123; 创建日期 2025-08-07, modified label relative-only on live page; backtest header `period: 3d`/`basePeriod: 3d`/Futures_Binance BNB_USDT 2024-08-07→2025-08-05; full Pine v6 decision text in served page stream read 2026-10-29, 736,512 bytes served, 1,600-char listing decoded end to end).
- Pinned Hummingbot engine: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles (VERSION `dev-2.17.0`; `backtesting_engine_base.py` 39,071 bytes, `backtesting_data_provider.py` 8,823 bytes, `executors_simulator/order_executor_simulator.py` 3,913 bytes, `binance_spot_candles.py` 3,924 bytes + `constants.py` 993 bytes with `https://api.binance.com`, `/api/v3/klines` and `3d` interval — sizes and cited lines directly verified this cycle).
- Prior independently merged pinned-engine capability evidence: https://github.com/HCH725/alpha-strategy-research/pull/414 (MARKET OrderExecutor path), https://github.com/HCH725/alpha-strategy-research/pull/590 and https://github.com/HCH725/alpha-strategy-research/pull/592 (close-evaluated stop conversion class) — engine-path evidence only, not proof of this derivative's signals or performance.
