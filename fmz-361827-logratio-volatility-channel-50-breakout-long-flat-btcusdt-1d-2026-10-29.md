---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "FMZ 361827 log-ratio volatility-index 50-channel breakout with midline reclaim exit — independent BTC-USDT spot long-flat derivative"
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2022-05-08
sources:
  - https://www.fmz.com/strategy/361827
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Log-ratio volatility-index channel breakout with midline reclaim exit — independent long-flat derivative

## Provenance

**Primary source (directly read 2026-10-29):** FMZ public strategy **361827**, *吕神简易波动率策略Pine语言版本* (Lyu simple volatility strategy, Pine version), author handle **QCoder** (displayed as 发明者量化-小小梦), type 通用策略, 创建日期 **2022-05-08 15:41:01**, https://www.fmz.com/strategy/361827 . Live page fetched this cycle over HTTPS (HTTP 200, **736,675 bytes**, title `吕神简易波动率策略Pine语言版本 | 发明者量化`): the complete Pine decision text is embedded in the served page stream blob without any login — every decision-critical literal below was verified in the live blob this cycle (`N = input(50`, `math.log(close) / math.log(close[N-1]) - 1`, `ta.sma(vix, N)`, `ta.highest(vix_ma, N)` / `ta.lowest(vix_ma, N)`, the `strategy.position_size == 0` gate, both `strategy.entry` legs, both `strategy.close_all()` exit legs, the `plot`/`fill` display lines, and the `/*backtest` header pinning `period: 1d`, `exchanges: [{"eid":"Bitfinex","currency":"BTC_USD"}]`, window 2021-05-16 → 2022-05-15). Token census over the live page: `strategy.entry` ×2 / `strategy.close_all` ×2 / `strategy.exit` 0 / `strategy.order` 0 / `strategy.cancel` 0 / `pyramiding` 0 / `process_orders_on_close` 0 / `request.` 0 / `security(` 0 / `crossover` 0 / `crossunder` 0 / `ta.ema` 0 / `ta.rsi` 0. The page also renders a generic `登录后查看完整代码` login-overlay button, but the decision source is fully present in the served blob; the overlay truncates only a display duplicate, not the rule text.

來源內容版本指紋：以頁面串流內相鄰兩份相同副本中的單份決策原文（不含顯示層重複、不做 trim 與換行正規化）計算 UTF-8 SHA-256，單份 `860` chars，內容指紋為 `7c794b87d0674a88f2a9c57e83d1ef2a8e343ecb99023aa63724cb9269599490`。此指紋固定本紀錄所引來源的內容版本，並非宣稱 FMZ 網頁永不變動；它也不是原碼封存下載位址。日後來源若變動，須先核對此指紋，不可把新頁面內容默認為本版本。研究者已宣告的衍生規則與來源／衍生邊界不變。

**Independent derived strategy, NOT source-native reconstruction:** preserve the source's log-ratio index construction (`ln(C[t])/ln(C[t-49]) - 1`, exactly as written — not "corrected" to `ln(C[t]/C[t-49])`), the 50-bar SMA midline, the 50-bar highest/lowest channel of that midline, the strict-inequality breakout entry, and the midline-recross exit with its exact bar-lag structure. Researcher-defined alterations: (a) disable the short leg entirely (LONG/FLAT only); (b) port Bitfinex `BTC_USD` to Binance BTC-USDT **spot** 1d (no perpetual, no funding leg by construction); (c) fix the research input `N = 50` (the source default; no sweep); (d) replace the equity-compounding `round(equity/close, 2)` sizing with a fixed 0.001 BTC order (the source sizing is a simulated-equity path function and is not reproducible as a pinned rule); (e) evaluate signals on the fully completed prior bar and simulate MARKET fills at the current completed bar's close, rather than Pine's default next-bar-open fills; (f) fix a hypothetical 0.1% per-side fee, a 200-bar warmup, and explicit pending/fill state conventions. Pine's `ta.sma` seed convention and float bit-identity are not claimed; the derivative pins the stated arithmetic as its own executable rule.

**Immutable derivative identity:** `FMZ:361827|QCoder:2022-05-08|independent-derived-v1-lvratio50-channel-midline|BinanceSpot:BTC-USDT:1d|N50|0.001BTC|prior-complete-signal-next-complete-close-MARKET|fee0.001|warmup200|2026-10-29`. Changing any formula, threshold, timing, market, risk, cost or direction creates a different derivative.

## Economic mechanism

### Source-reported

The page prose describes a simplified volatility strategy: a log-ratio "vix" index with its own moving average and upper/lower envelope; long when the index breaks above the envelope, short when it breaks below, and flat again when the index recrosses its midline. No source performance metric is adopted.

### Research interpretation

This is a **breakout of a volatility gauge against its own trailing envelope, with a midline-reclaim exit** — the traded object is not price but a log-ratio dispersion index, and the envelope is the trailing extreme of that index's own average rather than a price band. The `ln(C[t])/ln(C[t-49]) - 1` construction makes the index a slow-moving relative-displacement gauge (50 trading days of memory); the SMA-50 midline smooths it further; the highest/lowest-50 channel means a position is taken only when the gauge prints a 50-bar extreme *of its own smoothed path*. The exit fires on the first midline recross, so a winning trade is held only while the gauge stays stretched. The failure mode is plain: in a grinding one-way move the gauge can hug the envelope edge and print repeated entries after each midline-touch exit, and in a choppy market the index can flick across the channel edge for one-bar whipsaws. No profitability is asserted.

## Signal

**Gate 1 — exact researcher-pinned arithmetic.** Index completed UTC daily bars by `t=0,1,...`. Use real Binance BTC-USDT spot `O[t],H[t],L[t],C[t]`; only closes are read. A bar with missing/nonfinite/non-positive close is invalid; never interpolate.

1. `N = 50` (pinned; the source `input(50)` default, no sweep).
2. `vix[t] = ln(C[t]) / ln(C[t-49]) - 1` for `t >= 49`, requiring `C[t] > 0`, `C[t-49] > 0`, and `ln(C[t-49]) != 0`; otherwise `vix[t]` is undefined and that bar yields no signal. The division-of-logs form is preserved verbatim; it is **not** rewritten as a log of ratios.
3. `vix_ma[t] = mean(vix[t-49] .. vix[t])` for `t >= 98` (all 50 inputs defined; simple arithmetic mean).
4. `up[t] = max(vix_ma[t-49] .. vix_ma[t])`, `dn[t] = min(vix_ma[t-49] .. vix_ma[t])` for `t >= 147`.
5. On simulator bar `t` **only after its close**, evaluate with the already-completed **previous** bar `u = t-1`. `entryLong = (vix[u] > up[u] and vix[u-1] <= up[u-1])`, requiring all four referenced values finite. No current-bar `t` indicator may influence the action; `C[t]` is solely the modeled fill price and cash check.
6. If confirmed FLAT and not pending, `entryLong` creates one BUY of 0.001 BTC at simulated `C[t]` subject to warmup/affordability. The exit predicate is not consulted while FLAT.
7. If confirmed LONG and not pending, `exitLong = (vix[u] < vix_ma[u] and vix[u-1] >= vix_ma[u-1])` (all four values finite) creates one SELL of the confirmed 0.001 BTC at simulated `C[t]`. The entry predicate is not consulted while LONG. Never reverse or re-enter on the same bar.
8. There is no short leg, no fixed SL/TP, no trailing order, no time exit, no safety order, no scale-out, no cooldown, and no end-of-sample forced liquidation. An unclosed final position remains open, marked at the last observed valid price only. The source's `plot`/`fill` display lines have no decision function.

**Gate 2:** LONG/FLAT on Binance BTC-USDT **spot**, leverage 1, short side explicitly disabled. **Gate 3:** complete channel-breakout entry, midline-recross exit, and intentionally absent further risk legs as specified above (verified absent in source: zero `strategy.exit`/`strategy.order`/`strategy.cancel`).

## Position, risk and state

**Gate 4:** starting research cash `10,000 USDT`, initial inventory `0 BTC`, fixed single-unit order quantity `Decimal("0.001") BTC`, maximum one open position and one pending action. State is `FLAT -> BUY_PENDING -> LONG -> SELL_PENDING -> FLAT` **only after an observed filled executor**, not on signal submission. The source's own `strategy.position_size == 0` gate is the explicit single-position state machine (no reliance on any absent `pyramiding=` default). Reject unaffordable BUY if `cash < 0.001*C[t]*(1+0.001)`; no negative spot cash, leverage, fractional extra unit, compounding or partial-position trading. If no valid positive close exists, no order. Failed/unfilled actions must not create phantom inventory; maintain pending state until a documented fill or failure is reconciled, with no automatic retry. A failed BUY returns to FLAT only after explicit failure; a failed SELL retains LONG and waits for a new exit predicate. No explicit cooldown after a confirmed exit beyond the no-same-bar-reentry rule. Pyramiding, DCA, simultaneous strategies and safety orders are disabled.

The fixed size is a backtest design, not an assertion of exchange lot/min-notional viability. The midline exit bounds neither loss nor profit; gap risk across daily closes is real and undisguised.

## Required data and causality

**Gate 6:** require at least **200 consecutive fully completed** UTC 1d OHLCV bars before the first signal/fill; the structural minimum is 149 (first definable signal bar is index 148: `vix` from 49, `vix_ma` from 98, `up/dn` from 147, plus the one-bar cross lag). A Binance daily bar opening at `T[t]` is not complete before `T[t]+86400 seconds`. Predicates computed on completed bars `u=t-1` and `u-1` are known before bar `t` completes; the modeled fill at `C[t]` is assigned **effective time** `T[t]+86400`, never the raw Kline opening label `T[t]`. A completed-close MARKET simulator fill is a bounded historical modeling convention, **not** a claim that a live order can execute at a known historical close. No future prices, higher-timeframe partial bars, repainting pivots, full-sample fitted values, negative shifts, hindsight optimization or imputed candles. The header's `basePeriod: 1h` is inert: no decision line reads a second timeframe (zero `request.`/`security(`), so the derivative pins a single 1d decision frame and discloses the header value as unused.

Every bar must have a strictly consecutive UTC daily timestamp and valid OHLCV. On a missing/invalid/out-of-sequence bar, generate no new signal or fill and **retain** any confirmed existing spot position; do not synthesize an exit. After continuity is restored, resume decisions only after a fresh 200-bar warmup. The controller must never use the current bar's still-forming close to construct a signal. The `ln(C[t-49]) == 0` (price exactly 1 unit) and non-positive-close cases deterministically yield no signal — no invented tie-break.

## Execution assumptions

**Gate 5 — actual inspected pinned engine path (re-verified this cycle at source commit, not a generic API assertion):** admission package `20260920` (policy label, see disclosure), Hummingbot VERSION `dev-2.17.0` (read this cycle from `hummingbot/VERSION` at the pinned commit), source commit `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This cycle fetched the pinned tree over HTTPS and verified: `backtesting_engine_base.py` (39,071 bytes), `backtesting_data_provider.py` (8,823 bytes), `order_executor_simulator.py` (3,913 bytes), `BinanceSpotCandles` feed (3,924 bytes), feed `constants` (REST `https://api.binance.com` + `CANDLES_ENDPOINT /api/v3/klines` + `INTERVALS` including `1d`). No claim is made about a different engine build.

- **Market/data:** `BinanceSpotCandles` exposes REST Kline fields with timestamp and O/H/L/C/V parsed from actual Kline rows (pinned feed lines 80–85) plus websocket Kline fields (lines 99–108); `get_exchange_trading_pair` strips `-` (lines 64–65), so `BTC-USDT` maps to the exchange symbol. Pin `connector_name="binance"`, `trading_pair="BTC-USDT"`, one 1d feed, no secondary timeframe, cross-asset join, funding, mark price or order-book requirement.
- **Controller:** a strategy-specific `ControllerBase` implementation (not yet written) computes the exact log-ratio/channel arithmetic and prior-bar predicates on completed candles. `BacktestingEngineBase.run_backtesting` (pinned line 225, `trade_cost` parameter) runs `simulate_execution` (line 241/269), which per row calls `determine_executor_actions` (line 284) and dispatches `CreateExecutorAction` with `OrderExecutorConfig(side=BUY/SELL, position_action=OPEN/CLOSE, amount=Decimal("0.001"), execution_strategy=MARKET, leverage=1)`. The generic executor does **not** compute the index or implement this controller automatically.
- **Fill/clock:** inspected `OrderExecutorSimulator.simulate` (line 10) sets MARKET fill timestamp to the **first supplied row** (lines 22–24) and fill price to that row's **close** (line 56); `cum_fees_quote = trade_cost * amount_quote` (line 62); `CloseType.POSITION_HOLD` is emitted on fill (line 70). Here row `t` uses only signal inputs from `t-1`/`t-2`, and the simulator's fill `C[t]` is effective only at `T[t]+86400`. The engine's raw `timestamp_bt` and backward `merge_asof` (lines 466–470) are bar-**open** labels; interpreting them as completed-bar decision or fill times would be future leakage. An implementation failing to normalize effective close times is **not** compliant.
- **Fill-confirmed position:** the engine nets opposite BUY/SELL base fills into a hold ledger with weighted entry cost, gross realized PnL and `cum_fees_quote`. The default terminated-executor controller visibility is bounded in seconds (constructor line 164); use `BacktestingEngineBase(terminated_executors_window=None)` (line 319) or a durable equivalent plus a controller-side pending/fill ledger. `positions_held` can lag an executor's fill by a controller tick; no duplicate BUY/SELL while a prior MARKET fill is pending reconciliation. Never infer a fill from action creation alone. The exit maps to a plain MARKET close on a completed bar — no stop/limit legs, no intrabar ordering, no position-executor TP/SL machinery, hence no novel execution primitive beyond the representative MARKET OrderExecutor path reviewed in merged Alpha PR #414.
- **Cash/fees:** `run_backtesting(trade_cost=0.001)` is a **hypothetical 0.1% fee on each filled side**, charged in quote currency as `trade_cost * amount * fill_close`. For buy price `Pb`, sell `Ps` and `Q=0.001`, modeled net realized quote PnL = `Q*(Ps-Pb) - 0.001*Q*(Pb+Ps)`; quote cash is decremented by buy notional plus fee and credited by sell notional minus fee. Gross PnL and fee accumulators are separate, so a gross PnL series is **not** fee-inclusive net equity. This fee is **not** the source's, user's or Binance account's realized tariff.
- **No fabricated economics:** spot has no perpetual funding payment; this is **not** a claim of zero perpetual funding. The inspected MARKET simulator does not independently reproduce order-book spread, impact, slippage, latency, partial fills or exchange minimums. Those remain unverified real costs and execution constraints, not assumed real-world zeros. `BacktestingDataProvider.get_price_by_type` falls back to `Decimal("1")` when price is missing (pinned lines 132–140): this fallback must be explicitly rejected for BTC price/cash/fill accounting. Use actual positive finite `C[t]` only. Maintain Decimal ledger quantities and reconcile any simulator float roundoff; no fabricated prices.

**Capability boundary and package disclosure:** a single spot daily candle feed and MARKET completed-close fill model with a position-hold ledger is supported by the pinned inspected path. The source's Bitfinex venue, its equity-compounding sizing, its Pine-default next-bar-open fills, exact Pine float semantics and real fills are **not** claimed. The `20260920` package label is retained as a policy label only: this cycle verified behavior at source commit `8b0e067` and invents no package-to-commit mapping; sibling PASS records are engine-path evidence only, never proof of this derivative. This derivative is not a source-native equivalence assertion.

## Evidence

### Source-reported

FMZ 361827, QCoder, 2022-05-08: log-ratio index `ln(close)/ln(close[49]) - 1` with `N = 50`; 50-bar SMA midline; 50-bar highest/lowest envelope of that midline; long on strict upward breakout (`vix > up and vix[1] <= up[1]`), short on strict downward breakout, each gated on `position_size == 0`; full close on midline recross (`close_all`); `round(equity/close, 2)` sizing; no stop/target/trailing/time machinery. Original venue Bitfinex BTC_USD, demo window 2021-05-16 → 2022-05-15, decision `period: 1d`. No source performance metric adopted.

### Independently reproduced

**No independent performance or Pine-parity backtest reproduced.** This cycle read the live FMZ page blob (736,675 bytes, HTTP 200) and the pinned Hummingbot sources (VERSION, engine base, data provider, order-executor simulator, spot candle feed + constants — sizes and cited lines verified above), but ran no Qlib/Hummingbot backtest, no market replay, and no strategy controller. Six-gate PASS is the Scout's **proposed research admission assessment**, subject to the independent Hermes Auditor; it is not an auditor verdict, Survivor designation, economic performance claim or trading approval.

### Negative evidence

Exact Pine float bit-identity with `math.log`/`ta.sma`/`ta.highest`/`ta.lowest` is not reproduced here; the derivative pins the stated formulas as its own executable rule. Actual Binance fees, lot/tick constraints, real partial fills, package wheel byte identity, and future implementation correctness remain unverified. Any controller that reads bar `t` index values while claiming a `t-1` decision, treats raw bar-open labels as close timestamps, silently uses a missing-price fallback, double-counts position holds, "corrects" the division-of-logs into a log-of-ratios, or converts the midline-recross exit into an intrabar stop/limit order fails the stated Gate 5/6 contract. The short leg, Bitfinex venue, equity-compounding sizing, Pine next-open fills and Pine float exactness are explicitly out of scope, not silently preserved.

**Six-gate summary:** (1) pinned N=50 log-ratio index, SMA-50 midline, highest/lowest-50 envelope, strict-inequality breakout/recross with one-bar confirmation; (2) spot LONG/FLAT, shorts disabled; (3) exact entry, single predicate exit, deliberately disabled further legs; (4) fixed one-unit, fill-confirmed pending state, explicit single-position gate, no DCA/pyramiding; (5) inspected pinned spot daily candle → custom controller → MARKET OrderExecutor → POSITION_HOLD and quote-fee ledger with price/time guards, no novel primitive; (6) 200 contiguous completed bars (structural 149), two-bar-lag predicates, no future-data use.

## Dedup and falsification plan

At pre-write `main` SHA `ae81d7360349014913bfce3d7c729726fb3f95e7`, 427 root-level strategy Markdown records matched README's 427. No record cites FMZ `strategy/361827`, the `QCoder`/小小梦 authorship, or this log-ratio-channel identity (`grep -rl 361827` and case-insensitive `vix_ma` mechanism searches return zero strategy records — the single `log-ratio` prose hit is `chop-zone-dmi-psar-reversal`, whose Dreiss CHOP log-ratio index with ADX-25/PSAR state machine is a different mechanism class, fenced here as different). Closest shape neighbours, all fenced as different: `bollinger-band-breakout-long-midline-exit-btcusdt-1d-2026-10-11.md` (price breaks a price band, exits at a price midline — here price never enters the decision; the envelope is the trailing extreme of the index's own average, not MA±kσ); `wilder-volatility-system-sic-stop-reverse-two-sided-btcusdt-1d-2026-10-14.md` (price vs ATR stop-reverse, always-in — here index-vs-own-envelope breakout with flat states and a recross exit); `forven-zscore-mean-reversion-long-flat-btcusdt-1h-2026-10-17.md` (raw-close sample-σ z fade — different statistic, different trigger, no envelope). No pool record computes `ln(C)/ln(C[n])` or channels an indicator's own average. Open `research/*` PRs (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353) cover Williams-channel, Gaussian-StochRSI, SuperTrend, Chandelier, SSL, Swift-MA, forven CCI, AdxSmas, ClucMay, Heracles lanes — different mechanisms and sources.

Future tests (not performed): hand-calculate index/midline/channel transitions on frozen consecutive bars; test the `ln(C[t-49]) == 0` and non-positive-close no-signal guards; test entry/exit co-conditions across the FLAT/LONG boundary, missing-bar warmup reset and cash guard; reconcile fill effective timestamps, BUY/SELL sides, position netting and each fee against the pinned simulator. Only after representative Hummingbot/Qlib event-level execution-path parity may this strategy path enter mass Qlib screening. This is **not** a new admission gate or a requirement for each candidate to rerun generic primitive validation.

## Limitations and adoption boundary

This is an independent derived hypothesis, not a faithful reproduction of the FMZ Pine source. It inherits a slow gauge's whipsaw: the 50+50+50 memory stack means the envelope adapts sluggishly, so a range expansion can print breakout entries just as the move exhausts, and the midline recross can exit a fresh entry one bar later in chop. The division-of-logs index is nonstandard (it is not a return, not a z-score, not a volatility in the statistical sense); its level drifts with the price level's log scale and is preserved here exactly as the source wrote it, quirks included. A completed-close MARKET simulator is a bounded research abstraction; real gaps across daily closes bypass the modeled exit price with no slippage accounting. No positive return, real trading viability, Qlib parity, OOS result, Survivor/HB Certified status, Paper/Testnet/Live authorization or deployment is asserted. Optional campaign coins/timeframes, DCA BO/SO 6/6/6 and futures leverage are not entry requirements and are not part of this derivative.

**Implementation status:** `not-implemented`. **Adoption:** `not-approved`. **Approval scope:** `research-only`. Independent Hermes Auditor GitHub Webhook Review alone owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS closure. This Scout does not approve, merge or alter `main`.

## Related Wiki records

None.

## Sources

- FMZ primary source: https://www.fmz.com/strategy/361827 (QCoder/发明者量化-小小梦; 创建日期 2022-05-08; backtest header `period: 1d`/Bitfinex BTC_USD; full Pine decision text in served page blob read 2026-10-29, HTTP 200, 736,675 bytes).
- Pinned Hummingbot engine: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting (VERSION `dev-2.17.0`; `backtesting_engine_base.py` 39,071 bytes, `backtesting_data_provider.py` 8,823 bytes, `executors_simulator/order_executor_simulator.py` 3,913 bytes, spot candle feed 3,924 bytes + feed constants with `/api/v3/klines` and `1d` interval — sizes and cited lines directly verified this cycle).
- Prior independently merged pinned-engine capability evidence: https://github.com/HCH725/alpha-strategy-research/pull/414 (engine-path evidence only, not proof of this derivative's signals or performance).
