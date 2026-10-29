---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "freqtrade PatternRecognition bearish high-wave print with ROI ladder and trailing stop; independent BTC-USDT spot 1d long-flat derivative"
created: 2026-10-30
updated: 2026-10-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - freqtrade
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/PatternRecognition.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# PatternRecognition bearish high-wave — independent derivative

## Provenance

- **Primary source:** public freqtrade strategy collection `freqtrade/freqtrade-strategies`, file `user_data/strategies/PatternRecognition.py` (author @Mablue), read in full at immutable commit **`f3340ce11f5bdf62f598522e64d1f5638eaa13f5`** (2026-09-08T16:42:47Z): https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/PatternRecognition.py . Verified bytes this run: **88 lines, 2674 bytes**, SHA256 `cce61e4af8ed3cb8e78a5d9713aba7891ec08d1bdb1da9911c3f550424db795d`, Git blob SHA `c4c9d2e925a56eba39c9cff31ba532c446818f5d` matching the GitHub API blob SHA. No login, no paywall.
- **Source facts actually verified:** `buy_params = {"buy_pr1": "CDLHIGHWAVE", "buy_vol1": -100}` (pinned constants; the `CategoricalParameter` hyperopt spaces are inert — only these constants bind); entry `dataframe[buy_pr1.value] == buy_vol1.value` sets `enter_long = 1`; **all sell-pattern legs are commented out** and the remaining `populate_exit_trend` statement assigns `exit_long` over an empty selection — i.e. the shipped file contains **no active signal-exit rule**; `minimal_roi = {"0": 0.936, "5271": 0.332, "18147": 0.086, "48152": 0}` (freqtrade minute keys); `stoploss = -0.288`; `trailing_stop = True`, `trailing_stop_positive = 0.032`, `trailing_stop_positive_offset = 0.084`, `trailing_only_offset_is_reached = True`; `timeframe = '1d'`; `INTERFACE_VERSION = 3`. The file contains **no** `can_short`, `position_adjustment_enable`, `use_custom_stoploss`, `protections`, `startup_candle_count`, `leverage`, or `order_types` attributes; only `enter_long`/`exit_long` columns are ever set (long side only). The header hyperopt anecdote (`510 trades ... 542.13%`) is not traceable table/figure evidence and is not relied upon anywhere below.
- **Signal-formula provenance (primary C source, read this run):** `CDLHIGHWAVE` is the deterministic TA-Lib pattern function. Core condition from `ta-lib/ta-lib` `src/ta_func/ta_CDLHIGHWAVE.c` (batch path): a bar prints `±100` iff `|C-O| < CANDLEAVERAGE(BodyShort)` **and** upper shadow `> CANDLEAVERAGE(ShadowVeryLong)` **and** lower shadow `> CANDLEAVERAGE(ShadowVeryLong)`, signed `(C >= O) ? +100 : -100`. Averaging macro from `src/ta_func/ta_utility.h`: `CANDLEAVERAGE(SET,SUM,IDX) = FACTOR × (AVGPERIOD ≠ 0 ? SUM/AVGPERIOD : CANDLERANGE(SET,IDX))`, divided by 2 only for `Shadows` range type. Defaults from `src/ta_common/ta_global.c` `TA_CANDLE_DEFAULT_SETTINGS`: `BodyShort = (RealBody, 10, 1.0)` → short means below the mean real body of the **10 previous bars excluding the current**; `ShadowVeryLong = (RealBody, 0, 2.0)` → with period 0 the macro collapses to `2.0 × the current bar's own real body`. Lookback `max(10, 0) = 10`. The exact self-contained transcription is pinned in Signal below; no TA-Lib dependency is required at research time.
- **Independent researcher-defined executable derivative (NOT source-native):** source pair list is agnostic, so pin single-asset Binance **BTC-USDT spot 1d**; freqtrade intrabar stop/ROI/trailing evaluation on high/low is adapted to **completed-bar-close evaluation with pinned priority stop-level → ROI → (no signal leg)**; ROI minute keys map to completed post-fill 1d bars by ceiling division (5271→4, 18147→13, 48152→34); freqtrade fee-aware ROI is adapted to fee-exclusive gross ROI (declared below); fills are next-completed-bar-close historical MARKET fills; fixed `Q = Decimal("0.001")` BTC, 10,000 USDT starting cash, 0.1% hypothetical per-side fee, 11-bar warmup, exact-Decimal ledger with fail-closed reconciliation. These researcher choices change trade events and economics.
- **Frozen identity:** `FT:PatternRecognition.py|f3340ce|Mablue|independent-derived-v1-20261030|BinanceSpot-BTC-USDT-UTC1d|CDLHIGHWAVE==-100-bearish|no-signal-exit|ROI93.6@1/33.2@4/8.6@13/0@34-gross|stopmax(-28.8pct,hwm*(1-0.032)-after-+8.4pct)|next-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-each-side|warmup11|Decimal-ledger`. Any signal, timing, cost or position change creates a different derivative.

## Economic mechanism

### Source-reported

The file ships no mechanism prose: it is a bare pattern-recognition harness that computes all 61 TA-Lib candlestick codes and trades exactly one — the bearish high-wave print — with a time-decaying ROI ladder, a −28.8% disaster stop and an offset-gated trailing stop behind every position. No behavioural, structural, or risk-premium channel is claimed anywhere in the 88 lines.

### Research interpretation

A single-bar indecision print with teeth: the rule buys only a bar whose body is small versus its own recent history **and** whose both shadows each exceed twice that small body, closing down — i.e. a failed sell-off that could not hold either extreme into the close — then harvests only via time-decayed profit targets and a high-water trailing stop, never via a reversal signal. Unlike oscillator-gated dip records, there is no oversold context leg; unlike multi-bar pattern records (stars, soldiers, engulfing), the trigger is one bar's self-scaled geometry. The failure mode is plain: a high-wave print inside a continuing waterfall holds the full further excursion until the far stop, the trailing leg, or the 34-bar zero-profit backstop releases it.

## Signal — fully pinned independent rules (Gate 1, 2, 3, 4)

- **Market and clock:** one continuous, UTC-aligned Binance **BTC-USDT spot 1d** OHLCV sequence. Bar index `t` has exchange **open** timestamp `T[t]`; its complete O/H/L/C become decision-available only at `E[t] = T[t] + 86400 seconds`. Only complete historical bars are eligible; no future, partially formed or higher-timeframe candles.
- **Input validation:** strictly increasing, gap-free 86400-second UTC open timestamps; finite positive O/H/L/C, `H >= max(O,C)`, `L <= min(O,C)`, `H >= L`, no duplicate bars. **Abort the research run** on any missing, invalid, duplicate or discontinuous candle; do not forward-fill, interpolate, fabricate prices, quietly skip a gap, or emit synthetic fills/mark prices.
- **Entry predicate (completed bars only):** `body[t] = |C[t]-O[t]|`; `bodyAvg[t] = mean(|C[k]-O[k]|, k = t-10..t-1)`; `upper[t] = H[t]-max(C[t],O[t])`; `lower[t] = min(C[t],O[t])-L[t]`; `ENTER[t] = (body[t] < bodyAvg[t]) and (upper[t] > 2*body[t]) and (lower[t] > 2*body[t]) and (C[t] < O[t])`. All comparisons strict; any other relation fails. Degenerate bars are deterministic, never errors: `body[t] = 0` can never satisfy `upper/lower > 0` together with `C < O`; a zero `bodyAvg[t]` after ten flat bars fails `body < 0` for any live bar. The source defines no volume or volatility guard and none is invented.
- **Signal exits:** **none by record rule** — faithful to the shipped file, whose every sell-pattern leg is commented out. There is no opposite-signal, time-limit, or pattern-based exit leg to omit silently; the omission is the declared rule.
- **Warmup:** first **11** valid fully completed 1d bars, indices 0–10, are data-only, FLAT, and never emit orders. First decision may occur at index 11 (covers the 10-bar body average plus one conservative bar; the TA-Lib lookback is 10). No optimizer, ML, external feed, negative shift, future extremum, repaint or fitted parameter at research time; the source hyperopt spaces are inert.
- **BUY state:** initial `FLAT`, 0 BTC, 10,000 USDT cash. At eligible `E[t]` (`t >= 11`), if FLAT with no pending order and `ENTER[t]` true, queue exactly one fixed `Q = Decimal("0.001")` BTC MARKET BUY for the **next completed bar** `f = t+1`; do not use bar f's data to decide at t. At `E[f]`, use actual finite `C[f]` as the idealized simulator fill, if `cash >= Q*C[f]*(1+fee)` in exact Decimal. If insufficient cash, consume the signal, remain FLAT, and do not invent a partial fill or deferred order. A confirmed full fill sets LONG, records fill price `P = C[f]` and `fill_index = f`. No signal or exit evaluation on the fill bar.
- **LONG exits (evaluated at each `E[t]`, `t > f`, in fixed priority; at most one exit per bar):** (1) **stop-level:** `hwm[t] = max(C[f..t])`; trailing activates once `hwm[t] >= P*1.084`; `stop_level[t] = max(P*(1-0.288), hwm[t]*(1-0.032))` after activation, `P*(1-0.288)` before; exit if `C[t] <= stop_level[t]` (the max is provably redundant post-activation since `1.084*0.968 = 1.049 > 0.712`, kept explicit); (2) **ROI ladder** on fee-exclusive gross `(C[t]-P)/P` with post-fill bar age `a = t-f`: `>= 0.936` at any `a >= 1`, `>= 0.332` at `a >= 4`, `>= 0.086` at `a >= 13`, `>= 0` at `a >= 34`; exit if the age-eligible threshold holds (the 34-bar rung is a first-non-negative-close release, not a forced liquidation at a fabricated price). The winning exit queues exactly one MARKET SELL for the next completed bar `s = t+1` at real `C[s]`, sells the full Q, sets FLAT. No exit executes if its required future bar is absent; the pending order stays unfilled at sample end. No evaluation on the SELL fill bar; earliest re-entry decision is a later eligible bar.
- **State priority and exclusions:** at most one pending action and one position; a pending order takes precedence over new signals. There is no cooldown, pyramiding, DCA/safety orders, averaging, partial sizing, shorts, borrowing, leverage, margin, shared-capital concurrency, session filter, intrabar stop/limit/maker, or end-of-sample forced liquidation. An open LONG at the end is valued at the last **actual valid close**, never synthetically liquidated. Same-bar entry/exit exclusion holds by construction: entries act only from FLAT, exits only while LONG, and fill bars evaluate nothing.
- **Exact Decimal ledger (position truth):** all research accounting uses `Decimal(str(x))` for observed closes (never `Decimal(float)`), exact `Q`, exact products. BUY debits `Q*P*(1+fee)` USDT and credits exactly Q BTC; SELL debits exactly Q BTC and credits `Q*P*(1-fee)` USDT. `FLAT` holds **iff** ledger BTC `== Decimal("0")` exactly — arithmetically guaranteed since the identical Q added at fill is subtracted at close; no epsilon exists anywhere. Round-trip net is `Q*(P_sell-P_buy) - fee*Q*(P_buy+P_sell)`. Simulator quote/fee outputs are cross-checked only: if `|sim_quote - Q*P| > max(1e-8, 1e-12*Q*P)` or the fee check fails, or side/amount disagree, **abort the run as ENGINE_MISMATCH** — never round, never absorb dust, never infer state from the simulator. `positions_held`, float-derived dust and the terminated-executor window are never read for state; the controller-side ledger alone drives FLAT/LONG.

## Required data

Only actual Binance BTC-USDT spot UTC 1d O/H/L/C. The entry predicate uses bar t's **completed** inputs at `E[t]`; the queued order's fill at `E[t+1]` is not used retroactively. Stop-level high-water mark and ROI age start at the **confirmed full-fill** index, not the signal bar. No higher/lower timeframe, funding rate, order book, multi-asset feed, external sentiment or ML inference. Missing/invalid bars abort rather than silently continuing an inconsistent ledger.

## Execution assumptions

- **Pinned contract:** Hummingbot package **`20260920`**, `hummingbot/VERSION = dev-2.17.0`, bounded source commit **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`**. This cycle did not re-read engine bytes; it reuses exactly two already-reviewed primitives and no new one: (a) the single-pair Binance spot OHLCV → controller action → MARKET-close `OrderExecutorSimulator` → POSITION_HOLD primitive with the independent Decimal ledger, as reviewed in alpha PRs **#414** and **#550** and reused this week by the same-source-repo `freqtrade-diamond-high-volume-cross-trailing` record (same pinned commit `f3340ce`, same trailing-stop-on-close stack); (b) the **1d spot** feed with completed-bar decision timing, as reviewed in the PASS `wick-reversal-hammer-shooting-star` 1d and `fmz-521670` 1d records. The independent Auditor must confirm that evidence applies to the pinned package and path.
- **Controller/executor:** `BacktestingEngineBase.simulate_execution` iterates feature rows, updates state, then calls `controller.determine_executor_actions()` and processes `CreateExecutorAction`. A **future dedicated controller is not implemented**; it must queue the previous completed signal and emit `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=TradeType.BUY/SELL, amount=Decimal("0.001"), position_action=OPEN/CLOSE, execution_strategy=ExecutionStrategy.MARKET, price=None, leverage=1)` on the designated fill row, without using that row to decide the preceding signal. No claim of a deployed controller or exchange-accepted order.
- **Actual fill path:** MARKET uses the first supplied row's real `close`; sets `filled_amount_quote = float(amount)*close`, `cum_fees_quote = trade_cost * filled_amount_quote`; returns `POSITION_HOLD`. The engine's raw row timestamp is bar-open; this research model reports the **effective historical fill event** as `E[fill_row]`, not a claim a real order could execute at the completed close. A delayed controller dispatch on row `t+1` is required. The simulator does not independently verify live latency, spread, partial fills, tick/lot/min-notional or exchange acceptance; any such failure aborts per the ledger rule instead of rounding.
- **Missing price and economic limitations:** no **additional modeled** slippage is included in this idealized MARKET-close research convention; this is **not** a claim of zero real slippage. The 0.1% fee is an explicit research assumption, **not** a verified Binance tier. Source ROI is fee-aware while this derivative evaluates fee-exclusive gross ROI — a declared event-changing difference. Spot unleveraged BTC/USDT has no perpetual funding or liquidation cash flow; this does **not** assume perpetual funding is zero. Real exchange fees, liquidity, precision and market impact are unverified.
- **Reused capability boundary:** this uses only already-reviewed primitives. The new strategy changes only the controller-side entry predicate (TA-Lib-transcribed high-wave formula), the no-signal-exit posture, and the ROI/stop/trailing bar-close stack; not the data/executor market path. No Hummingbot or Qlib test is performed in this Scout. If a new execution primitive is required, one representative Hummingbot↔Qlib event-level parity validation is required **before mass screening**, not as a profitability admission gate.

## Evidence

### Source-reported

The pinned 88-line file supports every constant cited above. It ships zero performance evidence for this rule beyond the header hyperopt anecdote, which is not traceable and supports no claim here.

### Independently reproduced

Signal-formula verification only (no trade, Hummingbot/Qlib, performance, OOS or fee reproduction): the transcribed formula was checked against TA-Lib 0.8.1 `CDLHIGHWAVE` over 3,361 real Binance BTCUSDT 1d bars (2017-08-17→2026-10-29) with **0 mismatching bars**; this run re-verified the transcribed formula emits **266 events (7.91%)**, median gap 9 days, max gap 82 days, with events in every year 2017–2026 — a non-degenerate, every-regime signal, not a one-sample curiosity. These are researcher verification figures, not source facts and not performance evidence.

### Negative evidence

No contradictory source claims found. Pre-write dedup at `main@3d12592a` (453 root-level strategy records, README counter 453): `CDLHIGHWAVE`, `HIGHWAVE`, `high-wave`, `high wave`, `PatternRecognition`, `48152`, `18147`, `get_function_groups` return **zero** content hits pool-wide. `Mablue` appears only as sibling-file references inside three other-file records (`freqtrade-diamond-high-volume-cross-trailing`, `freqtrade-universalmacd`, `freqtrade-multima-tema-stack`), never this file. The 11 open `research/*` PRs were inspected by source/title/body — none uses this source or a candlestick-pattern-recognition signal. Closed-PR search returns only different-pattern proposals (#627 Harmonic XABCD, #556 longleg-doji anchored breakout, #484 five-bar doji, #484-adjacent family). Nearest pool neighbors differ in mechanism: `freqtrade-strategy002` (CDLHAMMER **ANDed** with RSI<30, Stoch %K<20, lower-band penetration and SAR/Fisher exits, 5m), `wick-reversal-hammer-shooting-star` (Pine wick fractions gated by 15-bar ±5% momentum context with shooting-star exits), `tradingview-kingshukghosh71-longleg-doji` (doji-anchored breakout), `tradingview-dipalishah94-morning-evening-star` (3-bar star ratios) — none trades a bare single-bar self-scaled high-wave print with ROI-ladder/trailing-only exits and no signal exit. Not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

Future authorized research only: zero-body and zero-average degenerate bars, warmup 10/11 boundary, signal t versus fill f separation, stop-level versus ROI priority ties, ROI age boundaries 1/4/13/34, trailing activation at exactly +8.4%, insufficient cash, last-bar pending, full-fill fee ledger, `Decimal(str())` versus float reconciliation, ENGINE_MISMATCH abort path. No backtest, trading, deployment or cron change here.

## Crypto portability

Pinned to Binance BTC-USDT spot 1d only. Any other pair, venue, or timeframe replays a different event stream and is a different derivative, not covered by this record. The 24/7 market has no session gaps; the rule uses no session, gap, or funding input, so no calendar portability adjustment exists to disclose. A perpetual-ported variant would need the full funding/cost load and is not specified here.

## Limitations

- Close-based stop/ROI/trailing evaluation and next-completed-close fills are declared adaptations of freqtrade's intrabar-high/low, next-open semantics — event-changing, not lossless.
- Source ROI is fee-aware; the derivative uses fee-exclusive gross ROI — declared difference.
- No slippage is modeled; the 0.1% fee is a research assumption, not a verified tier.
- TA-Lib itself is not a pinned runtime dependency; the signal is fully specified by the transcribed formula above, with TA-Lib C source as formula provenance only.
- Engine evidence is by reviewed-primitive lineage (#414/#550, Diamond, wick/fmz-521670 1d records), not a new wheel hash or controller implementation this cycle.
- Long-only spot: no statement about short-side or margined behavior is made or implied.

## Implementation status

`implementation_status: not-implemented`, `status: research-only`. `hb_ready_status: PASS` is a **Scout six-gate proposal awaiting independent Hermes Auditor review**, not independent approval, Qlib parity, Survivor, Hummingbot Certified, profitability or Paper/Testnet/Live authorization. Auditor alone may source-fact remediate exact head, merge on verified PASS, or close NOT_LOSSLESS. The existing signed GitHub webhook receiver alone performs post-merge README bookkeeping; Scout does not touch main/README or any workflow.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`. No live, Paper, Testnet, deployment, or downstream screening authorization is granted or implied by this record.

## Related Wiki records

None — the Scout performs no Wiki Brain write in this lane.

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/PatternRecognition.py — @Mablue, *PatternRecognition*, pinned commit 2026-09-08 (88 lines, 2674 bytes, SHA256 `cce61e4a…795d`, blob `c4c9d2e9…18f5d`).
- https://github.com/ta-lib/ta-lib/blob/main/src/ta_func/ta_CDLHIGHWAVE.c — `TA_CDLHIGHWAVE` batch condition and lookback `max(10,0)`, read 2026-10-30.
- https://github.com/ta-lib/ta-lib/blob/main/src/ta_func/ta_utility.h — `TA_CANDLEAVERAGE` / `TA_CANDLERANGE` macros, read 2026-10-30.
- https://github.com/ta-lib/ta-lib/blob/main/src/ta_common/ta_global.c — `TA_CANDLE_DEFAULT_SETTINGS` (`BodyShort` 10/1.0, `ShadowVeryLong` 0/2.0, RealBody), read 2026-10-30.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine source, inspected in prior reviewed cycles (see lineage above), not re-read this cycle.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — prior independent pinned wheel/source and MARKET primitive evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/550 — prior bounded spot MARKET-close research execution evidence.
- https://www.freqtrade.io/en/stable/stoploss/#trailing-stop-loss-different-positive-loss — official first-party trailing/offset-switch semantics referenced for the `trailing_only_offset_is_reached = True` posture.
