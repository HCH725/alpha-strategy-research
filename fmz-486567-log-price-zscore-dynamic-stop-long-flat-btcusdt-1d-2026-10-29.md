---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "FMZ 486567 log-price 7-bar z-score with exp-mean target and volatility-ratchet stop — independent BTC-USDT spot long-flat derivative"
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-03-14
sources:
  - https://www.fmz.com/strategy/486567
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Log-price z-score fade with mean target and ratchet stop — independent long-flat derivative

## Provenance

**Primary source (directly read 2026-10-29):** FMZ public strategy **486567**, *对数价格均值回归动态止损策略 / Logarithmic Price Mean Reversion Dynamic Stop Loss Strategy*, author handle **ianzeng123**, 创建日期 **2025-03-14 09:39:36**, https://www.fmz.com/strategy/486567 . Live page fetched this cycle over HTTPS (HTTP 200, 770,530 bytes, saved as `fmz486567_page.html`): the FMZ backtest header pins `period: 1d`, `basePeriod: 1d`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`, window 2024-03-14 → 2025-03-12. The page carries a login-overlay button, but the complete Pine v5 strategy text is embedded in the served page JSON blob without any login: every decision-critical literal was verified in the live blob this cycle (`window = input.int(7`, thresholds `-1.825` / `1.825` / `-2.125` / `2.125`, `math.log(close)`, `ta.sma(log_price, window)`, `ta.stdev(log_price, window)`, `take_profit_price = math.exp(rolling_mean)`, `strategy.entry` long + short legs, `strategy.close` TP/SL legs with comments, the `math.min`/`math.max` stop-ratchet lines, and the three `plot(` lines). Token census over the live page: 0 `strategy.exit` / 0 `strategy.order` / 0 `strategy.cancel` / 0 `pyramiding` / 0 `process_orders_on_close` / 0 `request.` / 0 `security(` / 0 `crossover` / 0 `crossunder` / 0 `ta.cross`. The absence of `pyramiding=` means the Pine v5 documented default (`pyramiding=0`, single same-direction entry) applies; the absence of `process_orders_on_close` means its documented default (`false`) applies — neither default is relied upon below, because the derivative pins its own state machine and fill timing.

來源內容版本指紋（獨立審查補全）：2026-10-29 直接取得 FMZ 486567 官方頁面回傳的完整 Pine 原始字串；依序 JSON 解碼頁面串流與其資料陣列，取以 `/*backtest` 起首且含策略名稱的唯一原始字串。不做 trim、換行正規化或 Markdown 包裝；以原字串 UTF-8 位元組計算 SHA-256，長度為 `3365` bytes（包含結尾 LF），內容指紋為 `0f0391fbbe0e746a6aa5c37f0703b120fe7e79288e5b2a7d52b8fb0740f24816`。此指紋固定本紀錄所引來源的內容版本，並非宣稱 FMZ 網頁永不變動；它也不是原碼封存下載位址。日後來源若變動，須先核對此指紋，不可把新頁面內容默認為本版本。研究者已宣告的衍生規則與來源／衍生邊界不變。

**Mirror cross-check (not provenance):** the local FMZ mirror copy of this page holds a 3,366-char code block whose full 335-token stream is a verified contiguous subsequence of this cycle's live page blob (424 tokens over the header→plots span). The mirror is corroboration only; every rule citation below comes from the live page.

**Independent derived strategy, NOT source-native reconstruction:** preserve the source's log-price 7-bar z-score construction, the `-1.825` long-entry level, the `exp(trailing mean)` profit target, and the volatility-ratcheted stop leg with its exact `min`/`max` update ordering and TP-before-SL check priority. Researcher-defined alterations: (a) disable the short leg entirely (LONG/FLAT only); (b) port Futures_Binance BTC 1d to Binance BTC-USDT **spot** 1d (no perpetual, no funding leg by construction); (c) evaluate signals on the fully completed prior bar and simulate MARKET fills at the current completed bar's close, rather than Pine's default next-bar-open fills; (d) fix size at 0.001 BTC over 10,000 USDT cash with a hypothetical 0.1% per-side fee, a 60-bar warmup, and explicit pending/fill state conventions. Pine's `ta.stdev` is pinned as the population estimator (biased divisor ÷7, per the printed v5/v6 reference equivalent `sqrt(sumOfSquareDeviations / length)`); this matches the source's undecorated `ta.stdev(log_price, window)` call.

**Immutable derivative identity:** `FMZ:486567|ianzeng123:2025-03-14|independent-derived-v1-logz7-pop-meanTP-ratchetSL|BinanceSpot:BTC-USDT:1d|0.001BTC|prior-complete-signal-next-complete-close-MARKET|fee0.001|warmup60|2026-10-29`. Changing any formula, threshold, timing, market, risk, cost or direction creates a different derivative.

## Economic mechanism

### Source-reported

The author's page prose (Chinese + English) describes exactly this record's mechanism: log-price rolling mean/std over a 7-bar window, z-score distance in sigma units, long below `-1.825` / short above `+1.825`, profit target at `exp(rolling_mean)` (reversion to the statistical mean), and a dynamic stop that loosens when volatility rises and tightens when it falls. No source performance metric is adopted.

### Research interpretation

This is a **log-space oversold fade with a moving fair-value target and a volatility-aware stop**, not a naked level-hold. The log transform makes the z-score a relative-distance gauge (a 2% dip scores the same at any price level); the 7-bar window makes it a fast, local washout detector rather than a regime anchor. The `exp(mean)` target moves with the market, so the trade is paid for reversion toward a *current* local mean, while the ratchet stop (`min` when dispersion widens, `max` when it narrows) gives adverse excursions a bounded, adaptive exit instead of an indefinite hold. The failure mode is plain: a genuine breakdown that keeps printing `z <= -1.825` re-arms immediately after each stopped exit, and a slow bleed where price tracks the sliding mean never reaches the target while the stop ratchets down bar after bar. No profitability is asserted.

## Signal

**Gate 1 — exact researcher-pinned arithmetic.** Index completed UTC daily bars by `t=0,1,...`. Use real Binance BTC-USDT spot `O[t],H[t],L[t],C[t]` with `C[t]` finite and positive; reject incomplete/malformed bars; never interpolate.

1. `L[t] = ln(C[t])` (natural log; `C[t] > 0` required).
2. For `t >= 6`, `mean[t] = (L[t-6] + ... + L[t]) / 7` and `std[t] = sqrt(sum((L[t-k]-mean[t])^2 for k=0..6) / 7)` — population divisor 7. If any of the 7 closes is missing/nonfinite/non-positive, or `std[t]` is zero/nonfinite, `z[t]` is undefined and that bar yields no signal.
3. `z[t] = (L[t]-mean[t]) / std[t]` when defined. `TP[t] = exp(mean[t])`.
4. On simulator bar `t` **only after its close**, evaluate with the already-completed **previous** bar `u = t-1`. `entryPrev = (z[u] finite and z[u] <= -1.825)`. No current-bar `t` indicator may influence the action; `C[t]` is solely the modeled fill price and cash check.
5. If confirmed FLAT and not pending, `entryPrev` creates one BUY of 0.001 BTC at simulated `C[t]` subject to warmup/affordability. The TP/SL predicates are **not** entry vetoes.
6. If confirmed LONG and not pending, first ratchet the stop register: `ns = exp(L[u] - 2.125*std[u])` (requires finite `L[u]`, `std[u]`; if either is nonfinite, hold position with the existing stop and evaluate exits against it); if `std[u] > estd` then `stop := min(stop, ns)`; else if `std[u] < estd` then `stop := max(stop, ns)`; on equality hold. Then `exitTP = (C[u] >= TP[u])`, `exitSL = (C[u] <= stop)` — **TP checked first**, source `if/elif` order; either creates one SELL of the confirmed 0.001 BTC at simulated `C[t]`. The entry predicate is not consulted while LONG. Never reverse or re-enter on the same bar.
7. At entry, `stop := exp(L[u] - 2.125*std[u])` and `estd := std[u]` (both finite whenever `entryPrev` fired, since finite `z[u]` implies `std[u] > 0`).
8. Zero-dispersion determinism: a `std[u] = 0` bar while LONG gives `TP[u] = exp(mean[u]) = C[u]`, so `exitTP` (`C[u] >= TP[u]`) fires deterministically — no invented tie-break, no hold-by-default.
9. There is no short leg, no fixed SL/TP beyond the two coded predicates, no trailing order, no time exit, no safety order, no scale-out, and no end-of-sample forced liquidation. An unclosed final position remains open, marked at the last observed valid price only.

**Gate 2:** LONG/FLAT on Binance BTC-USDT **spot**, leverage 1, short side explicitly disabled. **Gate 3:** complete log-z entry, dual predicate exits with coded priority, and intentionally absent further risk legs as specified above.

## Position, risk and state

**Gate 4:** starting research cash `10,000 USDT`, initial inventory `0 BTC`, fixed single-unit order quantity `Decimal("0.001") BTC`, maximum one open position and one pending action. State is `FLAT -> BUY_PENDING -> LONG -> SELL_PENDING -> FLAT` **only after an observed filled executor**, not on signal submission. Reject unaffordable BUY if `cash < 0.001*C[t]*(1+0.001)`; no negative spot cash, leverage, fractional extra unit, compounding or partial-position trading. If no valid positive close exists, no order. Failed/unfilled actions must not create phantom inventory; maintain pending state until a documented fill or failure is reconciled, with no automatic retry. A failed BUY returns to FLAT only after explicit failure; a failed SELL retains LONG (with its `stop`/`estd` registers intact) and waits for a new exit predicate. No explicit cooldown after a confirmed exit beyond the no-same-bar-reentry rule. Pyramiding, DCA, simultaneous strategies and safety orders are disabled.

The fixed size is a backtest design, not an assertion of exchange lot/min-notional viability. The stop leg bounds single-trade loss only in the completed-close model; gap risk across daily closes is real and undisguised.

## Required data and causality

**Gate 6:** require at least **60 consecutive fully completed** UTC 1d OHLCV bars before the first signal/fill; the structural minimum is 8 (7-bar seed plus the one-bar lag). A Binance daily bar opening at `T[t]` is not complete before `T[t]+86400 seconds`. Predicates computed on completed bar `u=t-1` are known before bar `t` completes; the modeled fill at `C[t]` is assigned **effective time** `T[t]+86400`, never the raw Kline opening label `T[t]`. A completed-close MARKET simulator fill is a bounded historical modeling convention, **not** a claim that a live order can execute at a known historical close. No future prices, higher-timeframe partial bars, repainting pivots, full-sample fitted values, negative shifts, hindsight optimization or imputed candles.

Every bar must have a strictly consecutive UTC daily timestamp and valid OHLCV. On a missing/invalid/out-of-sequence bar, generate no new signal or fill, freeze the `stop`/`estd` registers, reset the 60-bar contiguous warmup, and **retain** any confirmed existing spot position; do not synthesize an exit. After continuity is restored, resume decisions only after a fresh warmup. The controller must never use the current bar's still-forming close to construct a signal.

## Execution assumptions

**Gate 5 — actual inspected pinned engine path (re-verified this cycle, not a generic API assertion):** admission package `20260920` (policy label, see disclosure), Hummingbot VERSION `dev-2.17.0`, source commit `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This cycle fetched the pinned tree (non-truncated) and raw file bytes: `backtesting_engine_base.py` (39,071 bytes), `executors_simulator/order_executor_simulator.py` (3,913 bytes), `backtesting_data_provider.py` (8,823 bytes), `binance_spot_candles.py` (3,924 bytes), `binance_spot_candles/constants.py` (993 bytes), `controllers/controller_base.py` (38,335 bytes), `VERSION` (`dev-2.17.0`). No claim is made about a different engine build.

- **Market/data:** `BinanceSpotCandles` reads `/api/v3/klines` (pinned constants) and exposes `1d`, with timestamp and O/H/L/C/V parsed from actual Kline fields (pinned feed lines 82/99–108). Pin `connector_name="binance"`, `trading_pair="BTC-USDT"`, one 1d feed, no secondary timeframe, cross-asset join, funding, mark price or order-book requirement.
- **Controller:** a strategy-specific `ControllerBase` implementation (not yet written) computes the exact log-z arithmetic and prior-bar predicates on completed candles. `BacktestingEngineBase.run_backtesting` (pinned line 221, `trade_cost` parameter at line 225) runs `simulate_execution` (line 269), which per row calls `update_state` then `determine_executor_actions` (lines 283–284) and dispatches `CreateExecutorAction` with `OrderExecutorConfig(side=BUY/SELL, position_action=OPEN/CLOSE, amount=Decimal("0.001"), execution_strategy=MARKET, leverage=1)`. The generic executor does **not** compute log-z or implement this controller automatically.
- **Fill/clock:** inspected `OrderExecutorSimulator.simulate` (line 10) sets MARKET fill timestamp to the **first supplied row** (lines 24/27) and fill price to that row's **close** (line 56); `cum_fees_quote = trade_cost * amount_quote` (line 62); `CloseType.POSITION_HOLD` is emitted on fill (line 70). Here row `t` uses only signal inputs from `t-1`, and the simulator's fill `C[t]` is effective only at `T[t]+86400`. The engine's raw `timestamp_bt` and backward `merge_asof` (lines 466–470) are bar-**open** labels; interpreting them as completed-bar decision or fill times would be future leakage. An implementation failing to normalize effective close times is **not** compliant.
- **Fill-confirmed position:** the engine nets opposite BUY/SELL base fills into a hold ledger with weighted entry cost, gross realized PnL and `cum_fees_quote` (verified pattern in the inspected simulator). The default terminated-executor controller visibility is bounded in seconds (constructor line 164); use `BacktestingEngineBase(terminated_executors_window=None)` (line 319) or a durable equivalent plus a controller-side pending/fill ledger. `positions_held` can lag an executor's fill by a controller tick; no duplicate BUY/SELL while a prior MARKET fill is pending reconciliation. Never infer a fill from action creation alone. Both exit predicates map to plain MARKET closes on completed bars — no stop/limit legs, no intrabar ordering, no position-executor TP/SL machinery, hence no novel execution primitive beyond the representative MARKET OrderExecutor path reviewed in merged Alpha PR #414.
- **Cash/fees:** `run_backtesting(trade_cost=0.001)` is a **hypothetical 0.1% fee on each filled side**, charged in quote currency as `trade_cost * amount * fill_close`. For buy price `Pb`, sell `Ps` and `Q=0.001`, modeled net realized quote PnL = `Q*(Ps-Pb) - 0.001*Q*(Pb+Ps)`; quote cash is decremented by buy notional plus fee and credited by sell notional minus fee. Gross PnL and fee accumulators are separate, so a gross PnL series is **not** fee-inclusive net equity. This fee is **not** the source's, user's or Binance account's realized tariff.
- **No fabricated economics:** spot has no perpetual funding payment; this is **not** a claim of zero perpetual funding. The inspected MARKET simulator does not independently reproduce order-book spread, impact, slippage, latency, partial fills or exchange minimums. Those remain unverified real costs and execution constraints, not assumed real-world zeros. `BacktestingDataProvider.get_price_by_type` falls back to `Decimal("1")` when price is missing (pinned lines 132–140): this fallback must be explicitly rejected for BTC price/cash/fill accounting. Use actual positive finite `C[t]` only. Maintain Decimal ledger quantities and reconcile any simulator float roundoff; no fabricated prices.

**Capability boundary and package disclosure:** a single spot daily candle feed and MARKET completed-close fill model with a position-hold ledger is supported by the pinned inspected path. The source's futures venue, its Pine-default next-bar-open fills, exact Pine float semantics and real fills are **not** claimed. The `20260920` package label is retained as a policy label only: this cycle verified behavior at source commit `8b0e067` (whose tree predates that label) and invents no package-to-commit mapping; sibling PASS records are engine-path evidence only, never proof of this derivative. This derivative is not a source-native equivalence assertion.

## Evidence

### Source-reported

FMZ 486567, ianzeng123, 2025-03-14: log-price 7-bar SMA mean / population-std z-score; long at `z <= -1.825`, short at `z >= +1.825`; profit target `exp(rolling_mean)`; entry-anchored stop at `exp(log ± 2.125*std)` ratcheted by `min` (widening dispersion) / `max` (narrowing dispersion); TP checked before SL each bar; `position` state gate with Pine-default single-entry posture; no TP/SL bracket orders, no MTF, no cross functions. Original venue Futures_Binance BTC 1d, demo window 2024-03-14 → 2025-03-12. No source performance metric adopted.

### Independently reproduced

**No independent performance or Pine-parity backtest reproduced.** This cycle read the live FMZ page blob and the pinned Hummingbot sources, and ran the mirror-vs-live token cross-check, but ran no Qlib/Hummingbot backtest, no market replay, and no strategy controller. Six-gate PASS is the Scout's **proposed research admission assessment**, subject to the independent Hermes Auditor; it is not an auditor verdict, Survivor designation, economic performance claim or trading approval.

### Negative evidence

Exact Pine float bit-identity with `ta.sma`/`ta.stdev`/`math.log`/`math.exp` is not reproduced here; the derivative pins the stated population formulas as its own executable rule. Actual Binance fees, lot/tick constraints, real partial fills, package wheel byte identity, and future implementation correctness remain unverified. Any controller that reads bar `t` log-z while claiming a `t-1` decision, treats raw bar-open labels as close timestamps, silently uses a missing-price fallback, double-counts position holds, or converts the TP/SL predicates into intrabar stop/limit orders fails the stated Gate 5/6 contract. The short leg, futures margin/funding, Pine next-open fills and Pine float exactness are explicitly out of scope, not silently preserved.

**Six-gate summary:** (1) pinned log-price 7-bar population z-score, ±1.825/±2.125 constants, exp-mean target, min/max ratchet with TP priority; (2) spot LONG/FLAT, shorts disabled; (3) exact entry, dual predicate exits with priority, deliberately disabled further legs; (4) fixed one-unit, fill-confirmed pending state, stop/estd registers, no DCA/pyramiding; (5) inspected pinned spot daily candle → custom controller → MARKET OrderExecutor → POSITION_HOLD and quote-fee ledger with price/time guards, no novel primitive; (6) 60 contiguous completed bars, one-bar lag, no future-data use.

## Dedup and falsification plan

At pre-write `main` SHA `70e7ba4c8d5ad67cce2947efb94b466d8ab47b48`, 420 root-level strategy Markdown records matched README's 420. No record cites FMZ `strategy/486567` or this log-z + exp-mean-target + ratchet-stop identity. The same author handle (ianzeng123) appears on main only under different strategy IDs with different mechanisms (483504 balance-of-power cross, 482833 CMO14-BB20 crossunder, 482890 quantile-band trigger, 483087 triple-bollinger breach, 501679 Livermore pivot, 521670 wavelet slope, 482784 IBS) — same author, different sources, no identity collision. Closest mechanism neighbours, all fenced as different: `forven-zscore-mean-reversion-long-flat-btcusdt-1h-2026-10-17.md` (raw-close 20-bar sample-σ z, entry `z < -2.0`, single mean-reclaim level exit, no stop leg, 1h); `forven-zscore-mean-reclaim-long-flat-ethusdt-1h-2026-10-19.md` (level-reclaim exit, no target/stop machinery); `tradingview-tradedots-stoch-zscore80-14-7-long-btcusdt-1d-2026-10-25.md` (stochastic-gated z-score, different trigger); `qrs-penalized-rsrs-zscore-timing-long-flat-btcusdt-1d-2026-10-16.md` (regression-slope statistic, rail-cross timing); `tradingview-melkani-logweighted-five-ma-strength-long-flat-btcusdt-1d-2026-10-26.md` (log-weighted MA-strength sign cross — log appears only as a moving-average weight, no z-score, no mean target, no stop); closed-unmerged PR #526 (FMZ 435887 log-*volatility* impulse deadband — volatility impulse, not price z-score). None combines a log-price z entry with an `exp(mean)` price target and a dispersion-ratcheted stop. Open `research/*` PRs (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353) cover Williams-channel, Gaussian-StochRSI, SuperTrend, Chandelier, SSL, Swift-MA, CCI, AdxSmas, ClucMay, Heracles lanes — different mechanisms and sources.

Future tests (not performed): hand-calculate log-z, target and ratchet transitions on frozen consecutive bars; test flat-7 (std=0) entry block and in-position zero-dispersion TP exit; test TP/SL co-fire priority, missing-bar register freeze, warmup reset and cash guard; reconcile fill effective timestamps, BUY/SELL sides, position netting and each fee against the pinned simulator. Only after representative Hummingbot/Qlib event-level execution-path parity may this strategy path enter mass Qlib screening. This is **not** a new admission gate or a requirement for each candidate to rerun generic primitive validation.

## Limitations and adoption boundary

This is an independent derived hypothesis, not a faithful reproduction of the FMZ Pine source. It inherits a fast 7-bar fade's whipsaw: choppy sideways markets can print repeated `-1.825` entries that exit for small losses, and the moving `exp(mean)` target can recede as fast as price approaches it in a grind. A completed-close MARKET simulator is a bounded research abstraction; real gaps across daily closes bypass the modeled stop price with no slippage accounting. No positive return, real trading viability, Qlib parity, OOS result, Survivor/HB Certified status, Paper/Testnet/Live authorization or deployment is asserted. Optional campaign coins/timeframes, DCA BO/SO 6/6/6 and futures leverage are not entry requirements and are not part of this derivative.

**Implementation status:** `not-implemented`. **Adoption:** `not-approved`. **Approval scope:** `research-only`. Independent Hermes Auditor GitHub Webhook Review alone owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS closure. This Scout does not approve, merge or alter `main`.

## Related Wiki records

None.

## Sources

- FMZ primary source: https://www.fmz.com/strategy/486567 (ianzeng123; 创建日期 2025-03-14; backtest header 1d/basePeriod 1d/Futures_Binance BTC_USDT; full Pine text in served page blob read 2026-10-29).
- Pinned Hummingbot engine: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting (VERSION `dev-2.17.0`; `backtesting_engine_base.py`, `executors_simulator/order_executor_simulator.py`, `backtesting_data_provider.py`, `binance_spot_candles.py` + `constants.py`, `controllers/controller_base.py` directly inspected this cycle).
- Pine `ta.stdev` population-divisor reference: https://pineify.app/pine-script/reference/ta/stdev (biased default true; printed equivalent divides by `length`).
- Prior independently merged pinned-engine capability evidence: https://github.com/HCH725/alpha-strategy-research/pull/414 (engine-path evidence only, not proof of this derivative's signals or performance).
