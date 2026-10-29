---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "freqtrade Diamond high-shifted price/volume cross with ROI ladder and trailing stop; independent BTC-USDT spot 5m long-flat derivative"
created: 2026-10-29
updated: 2026-10-29
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Diamond.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Diamond high-shifted price/volume cross — independent derivative

## Provenance and immutable identity

- **Primary source:** public freqtrade strategy collection `freqtrade/freqtrade-strategies`, file `user_data/strategies/Diamond.py` (author @Mablue), read in full at immutable commit **`f3340ce11f5bdf62f598522e64d1f5638eaa13f5`** (2026-09-08): https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Diamond.py . Verified bytes this run: **155 lines, 9411 bytes**, SHA256 `98f108f9df8f22b4b9be921b912ada3eff7669b25fc9ec455992ec902a385902`, Git blob SHA `fedeb862478aaab58ba18ea069b6a739486c675d` matching the GitHub API blob SHA. No login, no paywall.
- **Source facts actually verified:** pure-OHLCV entry `crossed_above(high.shift(7), volume * 0.942)` with pinned `buy_params` (`buy_fast_key=high`, `buy_horizontal_push=7`, `buy_slow_key=volume`, `buy_vertical_push=0.942`); exit `crossed_below(high.shift(10), low * 1.184)` with pinned `sell_params` (`sell_fast_key=high`, `sell_horizontal_push=10`, `sell_slow_key=low`, `sell_vertical_push=1.184`); ROI ladder `{0: 0.242, 13: 0.044, 51: 0.02, 170: 0}` (freqtrade minutes); `stoploss = -0.271`; `trailing_stop = True`, `trailing_stop_positive = 0.011`, `trailing_stop_positive_offset = 0.054`, `trailing_only_offset_is_reached = False`; `timeframe = 5m`; `INTERFACE_VERSION = 3`. The file contains **no** `can_short`, `position_adjustment_enable`, `use_custom_stoploss`, `protections`, `startup_candle_count`, `leverage`, or `order_types` attributes; only `enter_long`/`exit_long` columns are ever set (long side only). Cross edge semantics verified against the maintained framework fork (`freqtrade/technical`, `technical/vendor/qtpylib/indicators.py`, read 2026-10-29): `crossed_above = (s1 > s2) & (s1.shift(1) <= s2.shift(1))`, `crossed_below = (s1 < s2) & (s1.shift(1) >= s2.shift(1))`; this record pins the identical boolean formulas explicitly below so it is self-contained.
- **Independent researcher-defined executable derivative (NOT source-native):** source pair list is agnostic, so pin single-asset Binance **BTC-USDT spot 5m**; freqtrade intrabar stop/ROI/trailing evaluation is adapted to **completed-bar-close evaluation with pinned priority stop-level → ROI → exit-signal**; ROI minutes map to completed post-fill 5m bars by ceiling division (13→3, 51→11, 170→34); trailing follows the source `only_offset False` literally (active from the fill bar, so the 0.054 offset binds nothing — recorded for lineage only); fills are next-completed-bar-close historical MARKET fills; fixed `Q = Decimal("0.001")` BTC, 10,000 USDT starting cash, 0.1% hypothetical per-side fee, 30-bar warmup, exact-Decimal ledger with fail-closed reconciliation. These researcher choices change trade events and economics.
- **Frozen identity:** `FT:Diamond.py|f3340ce|Mablue|independent-derived-v1-20261029|BinanceSpot-BTC-USDT-UTC5m|Hshift7-vs-0.942V-crossAbove|Hshift10-vs-1.184L-crossBelow|ROI24.2/4.4@3/2.0@11/0@34-gross|stopmax(-27.1pct,hwm*(1-0.011))|next-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-each-side|warmup30|Decimal-ledger`. Any signal, timing, cost or position change creates a different derivative.

## Economic mechanism

**Source-reported:** the author's header states the strategy is deliberately indicator-free and uses only raw OHLCV cross relations; embedded comments carry hyperopt anecdotes from several loss functions. Those anecdotes are **not traceable table/figure evidence and are not relied upon here**.

**Research hypothesis only:** a high price persisting several bars above a volume-scaled level (volume capitulation fade), exited when highs fall back below a low-scaled level, with a wide far stop plus tight high-water trailing and a decaying profit ladder. No performance, profitability, Qlib parity or historical Survivor claim.

## Signal — fully pinned independent rules (Gate 1, 2, 3, 4)

- **Market and clock:** one continuous, UTC-aligned Binance **BTC-USDT spot 5m** OHLCV sequence. Bar index `t` has exchange **open** timestamp `T[t]`; its complete O/H/L/C/V become decision-available only at `E[t] = T[t] + 300 seconds`. Only complete historical bars are eligible; no future, partially formed or higher-timeframe candles.
- **Input validation:** strictly increasing, gap-free 300-second UTC open timestamps; finite positive O/H/L/C, `H >= max(O,C)`, `L <= min(O,C)`, `H >= L`, finite `V >= 0`, no duplicate bars. **Abort the research run** on any missing, invalid, duplicate or discontinuous candle; do not forward-fill, interpolate, fabricate prices, quietly skip a gap, or emit synthetic fills/mark prices.
- **Entry predicate (completed bars only):** `A[t] = H[t-7]`, `B[t] = Decimal("0.942") * V[t]`; `ENTER[t] = (A[t] > B[t]) and (A[t-1] <= B[t-1])` where `A[t-1] = H[t-8]`, `B[t-1] = 0.942 * V[t-1]`. Strict `>` on the current bar, `<=` on the prior bar: any other relation fails. Zero volume is a valid deterministic input (then `B = 0`), not an error; the source defines no volume guard and none is invented.
- **Exit-signal predicate:** `C[t] = H[t-10]`, `D[t] = Decimal("1.184") * L[t]`; `EXITSIG[t] = (C[t] < D[t]) and (C[t-1] >= D[t-1])`. Strict `<` current, `>=` prior.
- **Warmup:** first **30** valid fully completed 5m bars, indices 0–29, are data-only, FLAT, and never emit orders. First decision may occur at index 30 (covers the deepest lookback `H[t-11]` for the exit edge plus the cross prior-bar shift). No optimizer, ML, external feed, negative shift, future extremum, repaint or fitted parameter at research time; hyperopt Parameter spaces in the source file are inert — only the pinned `buy_params`/`sell_params` constants above bind.
- **BUY state:** initial `FLAT`, 0 BTC, 10,000 USDT cash. At eligible `E[t]` (`t >= 30`), if FLAT with no pending order and `ENTER[t]` true, queue exactly one fixed `Q = Decimal("0.001")` BTC MARKET BUY for the **next completed bar** `f = t+1`; do not use bar f's data to decide at t. At `E[f]`, use actual finite `C[f]` as the idealized simulator fill, if `cash >= Q*C[f]*(1+fee)` in exact Decimal. If insufficient cash, consume the signal, remain FLAT, and do not invent a partial fill or deferred order. A confirmed full fill sets LONG, records fill price `P = C[f]` and `fill_index = f`. No signal or exit evaluation on the fill bar.
- **LONG exits (evaluated at each `E[t]`, `t > f`, in fixed priority; at most one exit per bar):** (1) **stop-level:** `hwm[t] = max(C[f..t])`, `stop_level[t] = max(P*(1-0.271), hwm[t]*(1-0.011))`; exit if `C[t] <= stop_level[t]`; (2) **ROI ladder** on fee-exclusive gross `(C[t]-P)/P` with post-fill bar age `a = t-f`: `>= 0.242` at any `a >= 1`, `>= 0.044` at `a >= 3`, `>= 0.02` at `a >= 11`, `>= 0` at `a >= 34`; exit if the age-eligible threshold holds; (3) **exit-signal:** exit if `EXITSIG[t]` true. The winning exit queues exactly one MARKET SELL for the next completed bar `s = t+1` at real `C[s]`, sells the full Q, sets FLAT. No exit executes if its required future bar is absent; the pending order stays unfilled at sample end. No evaluation on the SELL fill bar; earliest re-entry decision is a later eligible bar.
- **State priority and exclusions:** at most one pending action and one position; a pending order takes precedence over new signals. There is no cooldown, pyramiding, DCA/safety orders, averaging, partial sizing, shorts, borrowing, leverage, margin, shared-capital concurrency, session filter, intrabar stop/limit/maker, or end-of-sample forced liquidation. An open LONG at the end is valued at the last **actual valid close**, never synthetically liquidated. Same-bar entry/exit exclusion holds by construction: entries act only from FLAT, exits only while LONG, and fill bars evaluate nothing.
- **Exact Decimal ledger (position truth):** all research accounting uses `Decimal(str(x))` for observed closes (never `Decimal(float)`), exact `Q`, exact products. BUY debits `Q*P*(1+fee)` USDT and credits exactly Q BTC; SELL debits exactly Q BTC and credits `Q*P*(1-fee)` USDT. `FLAT` holds **iff** ledger BTC `== Decimal("0")` exactly — arithmetically guaranteed since the identical Q added at fill is subtracted at close; no epsilon exists anywhere. Round-trip net is `Q*(P_sell-P_buy) - fee*Q*(P_buy+P_sell)`. Simulator quote/fee outputs are cross-checked only: if `|sim_quote - Q*P| > max(1e-8, 1e-12*Q*P)` or the fee check fails, or side/amount disagree, **abort the run as ENGINE_MISMATCH** — never round, never absorb dust, never infer state from the simulator. `positions_held`, float-derived dust and the terminated-executor window are never read for state; the controller-side ledger alone drives FLAT/LONG.

## Required data and causal timing (Gate 6)

Only actual Binance BTC-USDT spot UTC 5m O/H/L/C/V. Indicator-free predicates use bar t's **completed** inputs at `E[t]`; the queued order's fill at `E[t+1]` is not used retroactively. Stop-level high-water mark and ROI age start at the **confirmed full-fill** index, not the signal bar. No higher/lower timeframe, funding rate, order book, multi-asset feed, external sentiment or ML inference. Missing/invalid bars abort rather than silently continuing an inconsistent ledger.

## Execution assumptions and pinned-engine evidence (Gate 5)

- **Pinned contract:** Hummingbot package **`20260920`**, `hummingbot/VERSION = dev-2.17.0` (bytes read at the bounded commit this run), bounded source commit **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`**. This cycle verified: `VERSION` file content `dev-2.17.0`; `binance_spot_candles/constants.py` `INTERVALS` maps **`5m`** (line 15) and `1h`; `_parse_rest_candles` maps REST `row[0]` to the **open** timestamp and `row[1..5]` to OHLCV (so completed-bar decision availability is normalized to `E[t]`, never mistaking row open time for close/volume availability); `backtesting_data_provider.py:140` returns `Decimal("1")` when price is absent — **never** used for fills or marking, actual positive closes required; `order_executor_simulator.py:56` MARKET takes the supplied row's real `close` as `entry_price`, line 59 computes `float(config.amount) * entry_price`, line 70 returns `CloseType.POSITION_HOLD`. The float line is exactly why this record's position truth is the independent Decimal ledger, never simulator auto-netting. No wheel re-download/hash this cycle; prior independently reviewed alpha PR **#414** reports 902/902 matching wheel Python files and SHA256 `ea5a929c...a148`; the independent Auditor must confirm that evidence applies to the pinned package and path.
- **Controller/executor:** `BacktestingEngineBase.simulate_execution` iterates feature rows, updates state, then calls `controller.determine_executor_actions()` and processes `CreateExecutorAction`. A **future dedicated controller is not implemented**; it must queue the previous completed signal and emit `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=TradeType.BUY/SELL, amount=Decimal("0.001"), position_action=OPEN/CLOSE, execution_strategy=ExecutionStrategy.MARKET, price=None, leverage=1)` on the designated fill row, without using that row to decide the preceding signal. No claim of a deployed controller or exchange-accepted order.
- **Actual fill path:** MARKET uses the first supplied row's real `close`; sets `filled_amount_quote = float(amount)*close`, `cum_fees_quote = trade_cost * filled_amount_quote`; returns `POSITION_HOLD`. The engine's raw row timestamp is bar-open; this research model reports the **effective historical fill event** as `E[fill_row]`, not a claim a real order could execute at the completed close. A delayed controller dispatch on row `t+1` is required. The simulator does not independently verify live latency, spread, partial fills, tick/lot/min-notional or exchange acceptance; any such failure aborts per the ledger rule instead of rounding.
- **Missing price and economic limitations:** no **additional modeled** slippage is included in this idealized MARKET-close research convention; this is **not** a claim of zero real slippage. The 0.1% fee is an explicit research assumption, **not** a verified Binance tier. Spot unleveraged BTC/USDT has no perpetual funding or liquidation cash flow; this does **not** assume perpetual funding is zero. Real exchange fees, liquidity, precision and market impact are unverified.
- **Reused capability boundary:** this uses only the already reviewed single-pair Binance spot OHLCV → controller action → MARKET-close `OrderExecutorSimulator` → POSITION_HOLD primitive, as previously documented in alpha PRs **#414** and **#550**. The new strategy changes only controller-side cross predicates, the ROI/stop/trailing bar-close stack and the Decimal ledger; not the data/executor market path. No Hummingbot or Qlib test is performed in this Scout. If a new execution primitive is required, one representative Hummingbot↔Qlib event-level parity validation is required **before mass screening**, not as a profitability admission gate.

## Six-gate summary for independent Auditor

1. **G1 deterministic:** pinned file/commit/bytes, exact shift/scale cross formulas with verified edge semantics, pinned buy/sell params, ROI ages, stop/trailing formulas, warmup, no invented guards.
2. **G2 direction:** BTC-USDT unleveraged spot LONG/FLAT; only `enter_long`/`exit_long` exist in source; shorts explicitly disabled.
3. **G3 entries/exits/risk:** complete cross entry, prioritized stop-level/ROI-ladder/exit-signal exits, no hidden stop/target/trailing or opposite-signal exit; inert offset disclosed.
4. **G4 position:** Q=0.001 BTC, cash=10,000 USDT, single pending action/position, no DCA/pyramiding/cooldown, explicit re-entry, last-bar and insufficient-cash handling.
5. **G5 pinned engine:** exact pinned Binance spot 5m feed, MARKET close simulator, controller/action path, effective-time normalization, exact Decimal cash/BTC ledger with fail-closed ENGINE_MISMATCH reconciliation, dust/positions_held/window explicitly never used for state, unsupported economics flagged. Package/source provenance relies on prior reviewed wheel correspondence, not a new wheel hash.
6. **G6 causality:** 30 completed-bar warmup; signal at E[t], queued fill at E[t+1], stop/ROI age from confirmed fill, no future leakage, no fabricated gap/price.

## Evidence, dedup and falsification

**Source-reported:** the pinned `Diamond.py` bytes support every constant cited above. The file's hyperopt comment anecdotes are not traceable evidence and support no performance claim.

**Independently reproduced:** **none** for this candidate's freqtrade trades, Hummingbot/Qlib events, performance, OOS or realized fees. Only the pinned strategy bytes, framework cross semantics and pinned-engine source paths above were inspected; prior PR engine proof is referenced with limitations.

**Dedup 2026-10-29:** pre-write `main@dccbcd21` has **443** root-level strategy records and README counter **443** (full non-truncated tree, excluding two READMEs). No main record contains `0.942`, `1.184` or `horizontal_push`; filename search for `diamond`/`mablue`/`godstra`/`trendrider` returns no strategy record (the sole prose mention is a sibling-file fence line in the HLHB record). Closed-PR search returns no Diamond/GodStra/TrendRider proposal; the eleven open `research/*` PRs were inspected by source/title/body and none use this source or the high-shifted price/volume cross plus ROI-ladder/trailing stack. Nearest pool neighbors (`freqtrade-strategy005-volume-surge-...`, `freqtrade-multima-tema-stack-...`, `freqtrade-hlhb-...`) use indicator-gated or dip-buy signals, not a price-vs-volume-level cross. This is not a parameter-only clone.

**Falsification plan (future authorized research only):** cross edge-equality cases on both legs, zero-volume bars, warmup 29/30 boundary, signal t versus fill f, stop-level versus ROI versus exit-signal priority ties, ROI age boundaries 1/3/11/34, insufficient cash, last-bar pending, full-fill fee ledger, `Decimal(str())` versus float reconciliation, ENGINE_MISMATCH abort path. No backtest, trading, deployment or cron change here.

## Implementation and adoption boundary

`implementation_status: not-implemented`, `status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. `hb_ready_status: PASS` is a **Scout six-gate proposal awaiting independent Hermes Auditor**, not independent approval, Qlib parity, Survivor, Hummingbot Certified, profitability or Paper/Testnet/Live authorization. Auditor alone may source-fact remediate exact head, merge on verified PASS, or close NOT_LOSSLESS. The existing signed GitHub webhook receiver alone performs post-merge README bookkeeping; Scout does not touch main/README or any workflow.

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Diamond.py — @Mablue, *Diamond*, pinned commit 2026-09-08 (155 lines, 9411 bytes, SHA256 `98f108f9…85902`, blob `fedeb862…c675d`).
- https://github.com/freqtrade/technical/blob/master/technical/vendor/qtpylib/indicators.py — maintained `crossed_above`/`crossed_below` edge semantics, read 2026-10-29.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine source inspected through connected GitHub app.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — prior independent pinned wheel/source and MARKET primitive evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/550 — prior bounded spot MARKET-close research execution evidence.
