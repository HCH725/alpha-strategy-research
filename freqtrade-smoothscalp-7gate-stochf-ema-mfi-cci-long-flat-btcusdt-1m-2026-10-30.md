---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "freqtrade SmoothScalp 7-gate STOCHF-rail-ADX-MFI-CCI long with CCI-gated exit; independent BTC-USDT spot 1m long-flat derivative v2"
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
source_as_of: 2022-07-10
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/7f91ff52bb664423ae673092a6a18d76c50c2c29/user_data/strategies/berlinguyinca/SmoothScalp.py
  - https://github.com/TA-Lib/ta-lib/blob/v0.6.4/src/ta_func/ta_MFI.c
  - https://github.com/freqtrade/technical/blob/78061e943282152344c6f774347d18b19e20b7e3/technical/vendor/qtpylib/indicators.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SmoothScalp 7-gate rail-oscillator long — independent derivative v2

## Provenance

- **Primary source:** public freqtrade strategy collection `freqtrade/freqtrade-strategies`, file `user_data/strategies/berlinguyinca/SmoothScalp.py` (class `SmoothScalp(IStrategy)`, the only class in the file; docstring idea: small frequent gains, recommends many parallel trades at config level), read in full at immutable commit **`7f91ff52bb664423ae673092a6a18d76c50c2c29`** (2022-07-10, latest commit touching this file — an interface-version addition; no signal line changed by it): https://github.com/freqtrade/freqtrade-strategies/blob/7f91ff52bb664423ae673092a6a18d76c50c2c29/user_data/strategies/berlinguyinca/SmoothScalp.py . Verified bytes this run: **102 lines, 3861 bytes**, SHA256 `e32a8f758d8d57876210d479576e7e415ff924400b8d037bb0f30799cd801a5b`, Git blob SHA `9d0718b04aad27e8bc989b2362a22934485e9520` matching the GitHub API blob SHA at the pinned commit (same blob SHA/size the prior v1 record cited at a later repo HEAD — the file itself is unchanged). No login, no paywall.
- **Source facts actually verified (effective literals):** `INTERFACE_VERSION = 3`; `timeframe = '1m'`; `minimal_roi = {"0": 0.01}` (single 1% rung); `stoploss = -0.5`. Entry is the seven-way AND of `open < ema_low(5)`, `adx > 30`, `mfi < 30`, `fastk < 30`, `fastd < 30`, `crossed_above(fastk, fastd)`, `cci < -150` (`enter_long = 1`). Exit is `((open >= ema_high(5)) OR crossed_above(fastk, 70) OR crossed_above(fastd, 70)) AND (cci > 150)` (`exit_long = 1`). Indicator construction: `ta.EMA(price='high'/'close'/'low', timeperiod=5)`, `ta.STOCHF(dataframe, 5, 3, 0, 3, 0)` (fastk_period 5, fastd_period 3, both matype 0), `ta.ADX` (default 14), `ta.MFI` (default 14), `ta.CCI` assigned twice — first `timeperiod=20`, then overwritten by default-period `ta.CCI(dataframe)` — so the **effective CCI is period 14** and the period-20 column is dead (fenced below). Full-file token census this run: 1 `short` (comment prose "the shorter the better" only — no short leg, no short identifier in code); 0 `trailing`; 0 `startup_candle_count`; 0 `use_exit_signal` / `exit_profit_only` / `ignore_roi` overrides (framework defaults True/False/False apply — exits fire even at a loss, disclosed defaults, never file literals); 0 `order_types` / `order_time_in_force`; 0 `protection`; 0 `resample` / `informative` (body; the lone `merge` token is a dead import, never called); 0 `position_adjustment` / `pyramiding` / `cooldown` / `max_open_trades` in code (the "60 parallel trades" sentence is config-level prose, never a file semantic — this record pins single-unit); 0 `leverage` / `can_short` / `funding` / `mark_price`; 0 `volume` (no volume column is ever named or read — entry fires regardless of volume, literal source behavior, disclosed); 0 `hyperopt` / 0 `*Parameter` (no fitted spaces); 0 `fillna` / `ffill` / `interpolate`; 0 negative shifts.
- **Dead columns fenced (computed, never gated):** `ema_close`, `rsi` (RSI14), `bb_lowerband`/`bb_upperband`/`bb_middleband` (BB20 close, graphing-only), `macd`/`macdsignal`/`macdhist` (MACD defaults), and the first `cci` (period-20, overwritten). Dead imports fenced: `Dict`, `List`, `reduce`, `DatetimeIndex`, `merge`, `numpy`. No reviewer repair may enable a fenced column or substitute a sibling constant.
- **Prior proposal of this same source:** PR **#566** (`research/hermes-smoothscalp-20261028-1941`) was closed `NOT_LOSSLESS` with exactly three blockers: (1) the six-conjunct entry **omitted the `cci < -150` seventh gate** while claiming source-verbatim entry — an undeclared event-changing deletion; (2) declared **Binance PERPETUAL isolated 3x/5x with historical funding** on an unverified perpetual executor path; (3) timestamps/accounting asserted but **not specified** on the declared route. This v2 record is a **new researcher-specified derivative** answering all three with explicit choices: (1) the literal **seven-conjunct entry including `cci(14) < -150`** (the CCI-20 overwrite disclosed above, effective period 14 pinned); (2) **Binance SPOT, leverage 1, fixed `Q = 0.001` BTC, hypothetical 0.1% per-side fee, no funding leg** (spot has none — not a zero-funding claim about perpetuals); (3) fully specified decision/fill timestamps (`E[t] = T[t] + 60s`, next-completed-bar-close MARKET fills), controller gating, and an exact-Decimal confirmed-fill ledger with fail-closed reconciliation. The #566 branch/history is preserved and untouched.
- **Independent researcher-defined executable derivative (NOT source-native):** source pair list is agnostic, so pin single-asset Binance **BTC-USDT spot 1m**; freqtrade intrabar stop/ROI evaluation is adapted to **completed-bar-close evaluation with pinned priority stop-level → ROI → exit-signal**; ROI `{"0": 0.01}` maps to gross `>= 0.01` at post-fill bar age `a >= 1`; the −50% stop evaluates on completed closes as `C[t] <= P*0.5`; fills are next-completed-bar-close historical MARKET fills; fixed `Q = Decimal("0.001")` BTC, 10,000 USDT starting cash, 0.1% hypothetical per-side fee, 60-bar researcher warmup pin (the file ships no `startup_candle_count`; 60 covers the ADX14 seed, the dead MACD/BB seeds, and all live 14/5-period seeds with margin); single-unit/no-add/no-cooldown position pin; exact-Decimal ledger with fail-closed reconciliation. These researcher choices change trade events and economics.
- **Frozen identity:** `FT:SmoothScalp.py|7f91ff5|independent-derived-v2-20261030|BinanceSpot-BTC-USDT-UTC1m|E7(open<emaL5,adx14>30,mfi14<30,stochF5-3<30,crossUp,cci14<-150)|X3rail-or-stoch70-AND-cci14>150|ROI1pct@a1-gross|stop-50pct|next-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-each-side|warmup60|Decimal-ledger`. Any signal, timing, cost or position change creates a different derivative.

## Economic mechanism

### Source-reported

The file's docstring reports a small-gain scalping idea (many potential buys, tiny profit each — author anecdote, **not traceable table/figure evidence and not relied upon here**). The coded mechanism: buy only the bar where price rails below its 5-bar low-EMA while trend strength (ADX14 above 30), money flow (MFI14 below 30), fast-oscillator position (both StochF legs below 30 with a fresh fastk-over-fastd cross), and price-location extremity (CCI14 below −150) all agree; stand aside to flat when price reclaims its 5-bar high-EMA or either StochF leg crosses back above 70, but only while CCI14 confirms overheating above +150 — behind a single 1% ROI rung and a −50% disaster stop.

### Research interpretation

A seven-gate dip-catcher with a CCI-gated two-sided exit, long-only. Unlike pure rail-touch records (price-vs-EMA alone), the entry refuses to buy weak rails: ADX demands a real trend to fade, MFI demands absent buying pressure, the StochF cross demands a fresh fast turn, and CCI−150 demands genuine extremity — frequency comes from the 1m frame, selectivity from the conjunction. Unlike single-oscillator exits, the exit demands extremity proof (CCI above +150) on top of any reclaim/turn arm, so chop that mean-reverts without overheating is held, not banked. The coded consequence is a buyer of confirmed-extreme micro-dips that harvests only overheated recoveries, with a wide disaster stop and a 1% first-profit rung. No performance, profitability, Qlib parity or Survivor claim.

## Signal

Exact rules as pinned (any other EMA length, StochF tuple, ADX/MFI/CCI period, threshold, strictness, rail pairing, ROI rung, stop, fill, frame, book, or leg combination is a different, unpinned rule):

```text
emaL[t]  = TA-Lib EMA5(low); emaH[t] = TA-Lib EMA5(high)        // explicit timeperiod 5
fk[t], fd[t] = TA-Lib STOCHF(fastk_period 5, fastd_period 3, both matype 0)
adx[t]   = TA-Lib ADX14 (default)                              // high/low/close
mfi[t]   = TA-Lib MFI14 rolling-sum (100*pos/(pos+neg), total<1.0 -> 0.0)
cci[t]   = TA-Lib CCI14 (default; the file's CCI20 assign is overwritten — dead)
XUP(a,b)[t] = (a[t]>b[t]) AND (a[t-1]<=b[t-1])                  // qtpylib.crossed_above, scalar-broadcast
ENTER[t] = (O[t]<emaL[t]) AND (adx[t]>30) AND (mfi[t]<30)
         AND (fk[t]<30) AND (fd[t]<30) AND XUP(fk,fd)[t] AND (cci[t]<-150)
EXITSIG[t] = ((O[t]>=emaH[t]) OR XUP(fk,70)[t] OR XUP(fd,70)[t]) AND (cci[t]>150)
```

- **CCI pin (answers #566 blocker 1):** the seventh entry conjunct `cci < -150` is restored literally, and the exit's `cci > 150` gate is kept literally. The file computes CCI twice; only the second (default period 14) survives in the column, so **both CCI legs read CCI14** — disclosed column shadowing, never repaired, never tuned. The MFI leg is the true TA-Lib rolling-sum construction (same `TA-Lib/ta-lib@v0.6.4/src/ta_func/ta_MFI.c` pin as the admitted Bandtastic v2 record: ring-buffer flows, `pos+neg < 1.0 → 0.0`); degenerate states fully specified (all-up flow → 100; dust flow → 0.0; no division by zero).
- **crossed_above pin:** byte-verified this run against `freqtrade/technical@78061e9` vendor `indicators.py` (`crossed`: `(s1 > s2) & (s1.shift(1) <= s2.shift(1))`, scalars broadcast to the series index) — two-bar causal edge, never redefined. The two scalar-70 arms ride the same primitive.
- **Mutual-exclusion proof (no tie-break pin required):** entry needs `cci[t] < -150` while every exit arm needs `cci[t] > 150` — the CCI legs are strictly exclusive on every bar, NaN or otherwise, so entry and signal-exit never co-fire. ROI/stop cannot co-fire with entry on the fill bar (zero distance at fill). The reviewer is never asked to invent an ordering.
- **Exact boundaries:** strict throughout except the exit's `>=` rail (`<`, `>`, `OR` exactly as coded — an open exactly on `emaL`, any oscillator exactly on 30, ADX exactly on 30, or CCI exactly on ∓150 fires nothing on that conjunct; an open exactly on `emaH` fires the rail arm). `open` legs read the completed bar's own open — point-in-time at the decision, never intrabar. No volume guard exists — zero-volume bars fire literally, disclosed.
- **Warmup:** first **60** valid fully completed 1m bars, indices 0–59, are data-only, FLAT, and never emit orders (researcher pin — the file ships no `startup_candle_count`; 60 covers the ADX14 seed, the dead MACD-35/BB20 seeds, and every live 14/5-period seed with margin). First decision may occur at index 60. NaN-leading comparisons and edges are false, so pre-seed bars could never fire in any case. No optimizer, ML, external feed, negative shift, future extremum, repaint or fitted parameter at research time.
- **BUY state:** initial `FLAT`, 0 BTC, 10,000 USDT cash. At eligible `E[t]` (`t >= 60`), if FLAT with no pending order and `ENTER[t]` true, queue exactly one fixed `Q = Decimal("0.001")` BTC MARKET BUY for the **next completed bar** `f = t+1`; do not use bar f's data to decide at t. At `E[f]`, use actual finite `C[f]` as the idealized simulator fill, if `cash >= Q*C[f]*(1+fee)` in exact Decimal. If insufficient cash, consume the signal, remain FLAT, and do not invent a partial fill or deferred order. A confirmed full fill sets LONG, records fill price `P = C[f]` and `fill_index = f`. No signal or exit evaluation on the fill bar.
- **LONG exits (evaluated at each `E[t]`, `t > f`, in fixed priority; at most one exit per bar):** (1) **stop:** exit if `C[t] <= P*0.5`; (2) **ROI** on fee-exclusive gross `(C[t]-P)/P`: exit if `>= 0.01` at post-fill bar age `a = t-f >= 1`; (3) **exit-signal:** exit if `EXITSIG[t]` true (`use_exit_signal` True / `exit_profit_only` False framework defaults — fires even at a loss, disclosed defaults). The winning exit queues exactly one MARKET SELL for the next completed bar `s = t+1` at real `C[s]`, sells the full Q, sets FLAT. No exit executes if its required future bar is absent; the pending order stays unfilled at sample end. No evaluation on the SELL fill bar; earliest re-entry decision is a later eligible bar.
- **State priority and exclusions:** at most one pending action and one position; a pending order takes precedence over new signals. There is no cooldown, pyramiding, DCA/safety orders, averaging, partial sizing, shorts, borrowing, leverage, margin, shared-capital concurrency, session filter, intrabar stop/limit/maker, or end-of-sample forced liquidation. An open LONG at the end is valued at the last **actual valid close**, never synthetically liquidated. Same-bar entry/exit exclusion holds by construction: entries act only from FLAT, exits only while LONG, and fill bars evaluate nothing.
- **Exact Decimal ledger (position truth):** all research accounting uses `Decimal(str(x))` for observed closes (never `Decimal(float)`), exact `Q`, exact products. BUY debits `Q*P*(1+fee)` USDT and credits exactly Q BTC; SELL debits exactly Q BTC and credits `Q*P*(1-fee)` USDT. `FLAT` holds **iff** ledger BTC `== Decimal("0")` exactly — arithmetically guaranteed since the identical Q added at fill is subtracted at close; no epsilon exists anywhere. Simulator quote/fee outputs are cross-checked only: if `|sim_quote - Q*P| > max(1e-8, 1e-12*Q*P)` or the fee check fails, or side/amount disagree, **abort the run as ENGINE_MISMATCH** — never round, never absorb dust, never infer state from the simulator. The controller-side ledger alone drives FLAT/LONG.

## Required data

Only actual Binance BTC-USDT spot UTC 1m O/H/L/C/V (volume read for validation only — no signal leg reads it). Indicator-plus-rail predicates use bar t's **completed** inputs at `E[t] = T[t] + 60 seconds` (T[t] the exchange open timestamp); the queued order's fill at `E[t+1]` is not used retroactively. Stop high-water/age accounting starts at the **confirmed full-fill** index, not the signal bar. No higher/lower timeframe, funding rate, order book, multi-asset feed, external sentiment or ML inference. Input validation: strictly increasing, gap-free 60-second UTC open timestamps; finite positive O/H/L/C, `H >= max(O,C)`, `L <= min(O,C)`, `H >= L`, finite `V >= 0`, no duplicate bars. **Abort the research run** on any missing, invalid, duplicate or discontinuous candle; do not forward-fill, interpolate, fabricate prices, quietly skip a gap, or emit synthetic fills/mark prices.

## Execution assumptions

- **Pinned contract:** Hummingbot package **`20260920`**, `hummingbot/VERSION = dev-2.17.0` (bytes read at the bounded commit this run), bounded source commit **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`**. This cycle verified: `VERSION` file content `dev-2.17.0`; `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` `INTERVALS` maps **`1m`** (with `1s`/`3m`/`5m`/`15m`/`30m`/`1h`/`2h`/`4h` and higher); `backtesting_data_provider.py` returns `Decimal("1")` when price is absent — **never** used for fills or marking, actual positive closes required; `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py:22` branches MARKET, `:56` takes the fill row's real `close` as `entry_price`, `:59` computes `float(config.amount) * entry_price`, `:60-62` writes quote/fees, `:70` returns `CloseType.POSITION_HOLD`. The float line is exactly why this record's position truth is the independent Decimal ledger, never simulator auto-netting. No wheel re-download/hash this cycle; prior independently reviewed alpha PR **#414** reports 902/902 matching wheel Python files and SHA256 `ea5a929c...a148`; the independent Auditor must confirm that evidence applies to the pinned package and path.
- **Controller/executor:** `BacktestingEngineBase.simulate_execution` iterates feature rows, updates state, then calls `controller.determine_executor_actions()` and processes `CreateExecutorAction`. A **future dedicated controller is not implemented**; it must queue the previous completed signal and emit `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=TradeType.BUY/SELL, amount=Decimal("0.001"), position_action=OPEN/CLOSE, execution_strategy=ExecutionStrategy.MARKET, price=None, leverage=1)` on the designated fill row, without using that row to decide the preceding signal. No claim of a deployed controller or exchange-accepted order.
- **Actual fill path:** MARKET uses the first supplied row's real `close`; sets `filled_amount_quote = float(amount)*close`, `cum_fees_quote = trade_cost * filled_amount_quote`; returns `POSITION_HOLD`. The engine's raw row timestamp is bar-open; this research model reports the **effective historical fill event** as `E[fill_row]`, not a claim a real order could execute at the completed close. A delayed controller dispatch on row `t+1` is required. The simulator does not independently verify live latency, spread, partial fills, tick/lot/min-notional or exchange acceptance; any such failure aborts per the ledger rule instead of rounding.
- **Missing price and economic limitations:** no **additional modeled** slippage is included in this idealized MARKET-close research convention; this is **not** a claim of zero real slippage. The 0.1% fee is an explicit research assumption, **not** a verified Binance tier. Spot unleveraged BTC/USDT has no perpetual funding or liquidation cash flow; this does **not** assume perpetual funding is zero. Real exchange fees, liquidity, precision and market impact are unverified.
- **Reused capability boundary:** this uses only the already reviewed single-pair Binance spot OHLCV → controller action → MARKET-close `OrderExecutorSimulator` → POSITION_HOLD primitive, as previously documented in alpha PRs **#414** and **#550** (plus the admitted 1m LowBB spot record's bounded path). The new strategy changes only controller-side StochF/EMA-rail/ADX/MFI/CCI predicates, the single-rung ROI/stop bar-close stack and the Decimal ledger; not the data/executor market path. No Hummingbot or Qlib test is performed in this Scout. If a new execution primitive is required, one representative Hummingbot↔Qlib event-level parity validation is required **before mass screening**, not as a profitability admission gate.

## Evidence

### Source-reported

The pinned `SmoothScalp.py` bytes support every constant cited above (timeframe, ROI rung, stop, the seven entry conjuncts with `cci < -150`, the three-arm CCI-gated exit, `INTERFACE_VERSION`). The file's parallel-trades sentence is config prose, not a coded semantic, and supports no sizing claim. The `technical@78061e9` vendor `indicators.py` bytes support the `crossed_above` transcription cited above. The TA-Lib `ta_MFI.c` v0.6.4 bytes support the rolling-sum formula, the `total < 1.0 → 0.0` guard, and the flat-TP `(0,0)` ring-slot behavior.

### Independently reproduced

**None** for this candidate's freqtrade trades, Hummingbot/Qlib events, performance, OOS or realized fees. Only the pinned strategy bytes, the TA-Lib MFI source, the framework edge semantics and pinned-engine source paths above were inspected; prior PR engine proof is referenced with limitations.

### Negative evidence

Pre-write dedup 2026-10-30 against `main@315b9004` (**448** root-level strategy records, README counter **448** — full tree, excluding two READMEs): filename/content search for `smoothscalp`, `smooth_scalp`, and the `mfi < 30`-with-`cci ∓ 150` conjunction returns **zero strategy records** — no pool record cites this source file or conjoins a StochF-rail-ADX-MFI entry with a CCI-gated reclaim exit. The eleven open `research/*` PRs (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593) were inspected by source/title/branch and none uses this source or the seven-gate rule. Closed-PR search returns only this source's own prior v1 (#566, NOT_LOSSLESS, whose three blockers are answered above as explicit researcher choices — not source facts the reviewer must invent). Nearest pool neighbors use different mechanisms: `freqtrade-cofibit-stochf-ema-rail-adx-gated` (the five-conjunct StochF-rail-ADX subset WITHOUT the MFI30 and CCI∓150 gates, 5m, four-rung ROI ladder, −25% stop — this record's extra money-flow/extremity gates, 1m frame and single-rung/−50% risk change trade events materially); `haehnchen-cci-washout-excursion` (4-bar CCI slice washout scan with SMA/EMA200 regime, 1m — window-scan construction, never rail-cross conjunctions); `fmz-482880-rsi-bb-imi-mfi-quad-confluence` (RSI/BB/IMI/MFI quad state, 1h — different legs, different frame). This is not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

Future authorized research only (no backtest, trading, deployment or cron change here): CCI20-vs-CCI14 shadowing (effective-14 proof); MFI rolling-vs-Wilder divergence at the 30 boundary; ADX-exactly-30 / oscillator-exactly-30 / CCI-exactly-∓150 no-fire boundaries; rail-equality (`open == emaL` no-fire, `open == emaH` fires); zero-volume bars firing literally; NaN-leading pre-seed silence; warmup 59/60 boundary; signal t versus fill f; stop versus ROI versus exit-signal priority ties; ROI age-1 boundary; insufficient cash; last-bar pending; full-fill fee ledger; `Decimal(str())` versus float reconciliation; ENGINE_MISMATCH abort path.

## Crypto portability

Binance BTC-USDT spot, 1m, unleveraged long-flat. The long-only book expresses unchanged on a spot venue with no borrowing, no leverage and no funding leg. No perpetual, margin, multi-asset, or cross-venue dependency is introduced. Real venue precision (tick/lot/min-notional), fees and liquidity must still abort-or-verify per the ledger rule before any execution use.

## Limitations

- Idealized next-completed-bar-close MARKET fills; no claim a live order achieves the completed close; no slippage model beyond the assumed 0.1% per-side fee (not a verified Binance tier).
- Freqtrade intrabar stop/ROI evaluation is adapted to completed-bar-close evaluation with the disclosed priority; trade events differ from a literal freqtrade backtest.
- Exact-Decimal indicator arithmetic is pinned for reproducibility; bit-identity with any particular TA-Lib float build is not claimed — threshold-boundary sensitivity is disclosed.
- The file's config-level "parallel trades" prose is not adopted; single-unit pin is a researcher choice, disclosed.
- PASS here means pinned-engine expressibility of this fully specified derivative, not profitability, Qlib parity, Survivor status, source-native equivalence, or any live/Paper/Testnet authorization.

## Implementation status

`implementation_status: not-implemented`. No controller, executor config, backtest, Qlib recipe, or deployment artifact is created here. If this candidate is formally selected for execution without a reproducible executable recipe, the engineering route is `IMPLEMENTATION_NEEDED` (minimal strategy-specific implementation, then the same 01–05), never a second admission flag.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. `hb_ready_status: PASS` is a **Scout six-gate proposal awaiting independent Hermes Auditor review**, not independent approval, Qlib parity, Survivor, Hummingbot Certified, profitability or Paper/Testnet/Live authorization. The Auditor alone may source-fact remediate the exact head, merge on verified PASS, or close NOT_LOSSLESS. The existing signed GitHub webhook receiver alone performs post-merge README bookkeeping; Scout does not touch main/README or any workflow.

## Related Wiki records

None. This Scout cycle writes no Wiki Brain records.

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/7f91ff52bb664423ae673092a6a18d76c50c2c29/user_data/strategies/berlinguyinca/SmoothScalp.py — berlinguyinca, *SmoothScalp*, pinned commit 2022-07-10 (102 lines, 3861 bytes, SHA256 `e32a8f75…01a5b`, blob `9d0718b0…85e9520`).
- https://github.com/TA-Lib/ta-lib/blob/v0.6.4/src/ta_func/ta_MFI.c — first-party TA-Lib rolling-sum MFI with ring-buffer flows and the `total < 1.0 → 0.0` guard, read 2026-10-30.
- https://github.com/freqtrade/technical/blob/78061e943282152344c6f774347d18b19e20b7e3/technical/vendor/qtpylib/indicators.py — maintained `crossed`/`crossed_above`/`bollinger_bands` helpers, read 2026-10-30.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine source inspected (VERSION, 1m INTERVALS, MARKET-close simulator path).
- https://github.com/HCH725/alpha-strategy-research/pull/414 — prior independent pinned wheel/source and MARKET primitive evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/550 — prior bounded spot MARKET-close research execution evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/566 — this source's prior v1 proposal, closed NOT_LOSSLESS with three exact blockers answered in this v2 record.
