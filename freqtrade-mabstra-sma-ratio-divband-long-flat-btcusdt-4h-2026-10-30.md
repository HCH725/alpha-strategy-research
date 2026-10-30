---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "freqtrade mabStra dual SMA-ratio div-band entry with dead signal-exit, ROI ladder and fixed stop; independent BTC-USDT spot 4h long-flat derivative"
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/mabStra.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# mabStra dual SMA-ratio div-band — independent derivative

## Provenance

- **Primary source:** public freqtrade strategy collection `freqtrade/freqtrade-strategies`, file `user_data/strategies/mabStra.py` (author @Mablue / Masoud Azizi, class `mabStra(IStrategy)`, the only class in the file), read in full at immutable commit **`f3340ce11f5bdf62f598522e64d1f5638eaa13f5`** (2026-09-08): https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/mabStra.py . Verified bytes this run: **97 lines, 4044 bytes**, SHA256 `1c483a549398a0244ca6d87f9736a76ed462056aca8a5ee9affd9aa65efd9393`, `git hash-object` `41615495115e491a6fbfd869d64bd3f8a2337008` matching the GitHub contents-API blob SHA at the pinned commit. No login, no paywall.
- **Source facts actually verified (effective defaults):** `INTERFACE_VERSION = 3`; `timeframe = '4h'`; `minimal_roi = {"0": 0.598, "644": 0.166, "3269": 0.115, "7289": 0}` (freqtrade minutes); `stoploss = -0.128`. Buy legs: `buy_mojo_ma_timeframe` default 7, `buy_fast_ma_timeframe` default 14, `buy_slow_ma_timeframe` default 28, `buy_div_min` default 0.29497, `buy_div_max` default 2.25446. Sell legs: `sell_mojo_ma_timeframe` default 7, `sell_fast_ma_timeframe` default 14, `sell_slow_ma_timeframe` default 28, `sell_div_max` default 1.54593, `sell_div_min` default 2.81436. Indicators are exactly six close-SMAs (`talib.abstract as ta`, `ta.SMA(dataframe, timeperiod=...)` on the frame's close); entry conjoins two mojo/fast/slow ratio bands; exit conjoins two inverted ratio bands. The file's ROI paste-block is the coded table above, not a separate claim.
- **Full-file token census this run:** 0 `short` / `can_short` / `startup_candle_count` / `process_only` / `trailing` / `use_custom_stoploss` / `protection` / `resample` / `informative` / `request` / `security` / `position_adjustment` / `pyramiding` / `cooldown` / `max_open_trades` / `leverage` / `order_types` / `order_time_in_force` / `funding` / `mark_price` / `use_exit_signal` / `exit_profit_only` / `ignore_roi` / `volume` / `obv` / `atr` / `macd` / `bbands` / `heikin` (the single case-insensitive `rsi` hit is the substring inside `INTERFACE_VERSION`, not an indicator; the single `ema` hit pattern likewise matches only schema prose — the file computes SMA columns only). Imports are exactly `IntParameter, DecimalParameter, IStrategy`, `DataFrame`, and `talib.abstract`. The hyperopt `*Parameter` spaces carry the pinned `default=` values above; only those defaults bind this record. The header's `DO NOT USE WITHOUT HYPEROPT` warning is an author usage note; the pasted hyperopt results ARE the coded defaults, so no rule is missing.
- **Dead signal-exit leg (verified source fact, not a gap):** the exit requires `ratio > sell_div_min (2.81436)` AND `ratio < sell_div_max (1.54593)` on the same ratio — an empty conjunction since `2.81436 > 1.54593`. Both exit legs are therefore mathematically dead: `exit_long` never prints under the pinned defaults. Exits under this source are the ROI ladder plus the fixed stoploss only. This record keeps that dead leg exactly as coded (evaluated, never firing) and discloses it, rather than deleting or repairing it.
- **Independent researcher-defined executable derivative (NOT source-native):** source pair list is agnostic, so pin single-asset Binance **BTC-USDT spot 4h**; freqtrade intrabar ROI/stoploss evaluation is adapted to **completed-bar-close evaluation with pinned priority stop-level → ROI** (the signal-exit leg is evaluated but dead by code); ROI minutes map to completed post-fill 4h bars by ceiling division (644→3, 3269→14, 7289→31); fills are next-completed-bar-close historical MARKET fills; fixed `Q = Decimal("0.001")` BTC, 10,000 USDT starting cash, 0.1% hypothetical per-side fee, 27-bar warmup (first bar where SMA-28 is defined; the file sets no `startup_candle_count`), exact-Decimal ledger with fail-closed reconciliation. These researcher choices change trade events and economics.
- **Frozen identity:** `FT:mabStra.py|f3340ce|Mablue|independent-derived-20261030|BinanceSpot-BTC-USDT-UTC4h|SMA7/14-in-(0.29497,2.25446)-AND-SMA14/28-in-(0.29497,2.25446)|signal-exit-DEAD(min2.81436>max1.54593)|ROI59.8/16.6@3/11.5@14/0@31-gross|stop-12.8pct|next-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-each-side|warmup27|Decimal-ledger`. Any signal, timing, cost or position change creates a different derivative.

## Economic mechanism

### Source-reported

The file's header reports a hyperopt-fitted 4h MA-ratio system (pasted ROI table only; no traceable trade table is relied upon here). The coded mechanism: enter when the short/intermediate/long SMA stack sits in a tight multiplicative band (both adjacent ratios inside 0.29497–2.25446 — a compression/alignment read, long-only, no oscillator, no volume gate); the coded signal-exit never fires (inverted bounds), so positions end on the decaying four-rung ROI ladder (59.8% → 16.6% → 11.5% → 0%) or the −12.8% fixed stop.

### Research interpretation

A moving-average compression fade-in with time-decayed profit harvesting, long-only. Unlike crossover records (which fire on edge crossings), this fires on stack *agreement inside a band* — the 1.0-centered window admits aligned stacks and refuses both splayed trends (ratio above 2.25446) and inverted stacks (ratio below 0.29497). Unlike oscillator-gated dips, there is no momentum veto at entry at all. The dead signal-exit is the record's honest quirk: the strategy as coded is entry-timed by alignment and exited purely by economics (ROI/stop), which makes its holding-time distribution a clean function of the ladder, not of a second signal. No performance, profitability, Qlib parity or Survivor claim.

## Signal

Exact rules as pinned (any other MA period, bound, price basis, ROI rung, stop, fill, frame, book, or leg combination is a different, unpinned rule):

```text
SMA_N[t] = mean(C[t-N+1 .. t])                                     // close SMA, exact Decimal
R1[t]    = SMA_7[t] / SMA_14[t]
R2[t]    = SMA_14[t] / SMA_28[t]
ENTER[t] = (R1[t] > 0.29497) AND (R1[t] < 2.25446)
       AND (R2[t] > 0.29497) AND (R2[t] < 2.25446)                  // enter_long = 1
EXITSIG[t] = (SMA_14[t]/SMA_7[t] > 2.81436) AND (SMA_14[t]/SMA_7[t] < 1.54593)
         AND (SMA_28[t]/SMA_14[t] > 2.81436) AND (SMA_28[t]/SMA_14[t] < 1.54593)
         = FALSE on every bar by construction                       // exit_long, dead leg
```

- **SMA pin:** `talib.abstract.SMA(dataframe, timeperiod=N)` on the frame defaults to the close series; the construction is the exact arithmetic mean over the trailing N closes, first defined at index N−1, NaN before (NaN comparisons are false, so pre-seed bars deterministically fire nothing). No smoothing variant, no Wilder factor, no unstable-period quirk exists for SMA.
- **Division safety:** the only divisions are the four MA ratios plus the fixed-window means. Post-warmup all MAs are means of strictly positive closes, hence strictly positive — no zero divisor is reachable; pre-seed NaN ratios fire nothing. Warmup removes every undefined branch.
- **Dead-leg proof:** each exit leg needs `x > 2.81436 ∧ x < 1.54593`, empty since `2.81436 > 1.54593`. `EXITSIG[t]` is identically false; it is still evaluated (not deleted) so the record matches the file leg-for-leg.
- **Liveness proof (entry is non-vacuous):** the entry band contains 1.0 strictly inside (0.29497, 2.25446), so an aligned stack (`SMA_7 ≈ SMA_14 ≈ SMA_28`) fires. The strategy can trade.
- **Exact boundaries:** strict throughout (`>`, `<` — a ratio exactly on a bound fires nothing). Strictness preserved, never smoothed.
- **Warmup:** first **27** valid fully completed 4h bars, indices 0–26, are data-only, FLAT, and never emit orders. First decision may occur at index 27 — the first bar where SMA-28 (the longest seed) is defined (SMA-7 needs index ≥ 6, SMA-14 index ≥ 13). No optimizer, ML, external feed, negative shift, future extremum, repaint or fitted parameter at research time; hyperopt spaces are inert — only the pinned defaults bind.
- **BUY state:** initial `FLAT`, 0 BTC, 10,000 USDT cash. At eligible `E[t]` (`t >= 27`), if FLAT with no pending order and `ENTER[t]` true, queue exactly one fixed `Q = Decimal("0.001")` BTC MARKET BUY for the **next completed bar** `f = t+1`; do not use bar f's data to decide at t. At `E[f]`, use actual finite `C[f]` as the idealized simulator fill, if `cash >= Q*C[f]*(1+fee)` in exact Decimal. If insufficient cash, consume the signal, remain FLAT, and do not invent a partial fill or deferred order. A confirmed full fill sets LONG, records fill price `P = C[f]` and `fill_index = f`. No signal or exit evaluation on the fill bar.
- **LONG exits (evaluated at each `E[t]`, `t > f`, in fixed priority; at most one exit per bar):** (1) **stop:** exit if `(C[t]-P)/P <= -0.128` fee-exclusive; (2) **ROI ladder** on fee-exclusive gross `(C[t]-P)/P` with post-fill bar age `a = t-f`: `>= 0.598` at any `a >= 1`, `>= 0.166` at `a >= 3`, `>= 0.115` at `a >= 14`, `>= 0` at `a >= 31`; exit if the age-eligible threshold holds; (3) **exit-signal:** evaluate `EXITSIG[t]` (identically false — documents the dead leg, never triggers). The winning exit queues exactly one MARKET SELL for the next completed bar `s = t+1` at real `C[s]`, sells the full Q, sets FLAT. No exit executes if its required future bar is absent; the pending order stays unfilled at sample end. No evaluation on the SELL fill bar; earliest re-entry decision is a later eligible bar.
- **State priority and exclusions:** at most one pending action and one position; a pending order takes precedence over new signals. There is no cooldown, pyramiding, DCA/safety orders, averaging, partial sizing, trailing, protections, shorts, borrowing, leverage, margin, shared-capital concurrency, session filter, intrabar stop/limit/maker, or end-of-sample forced liquidation. An open LONG at the end is valued at the last **actual valid close**, never synthetically liquidated. Same-bar entry/exit exclusion holds by construction: entries act only from FLAT, exits only while LONG, and fill bars evaluate nothing.
- **Exact Decimal ledger (position truth):** all research accounting uses `Decimal(str(x))` for observed closes, exact `Q`, exact products. BUY debits `Q*P*(1+fee)` USDT and credits exactly Q BTC; SELL debits exactly Q BTC and credits `Q*P*(1-fee)` USDT. `FLAT` holds **iff** ledger BTC `== Decimal("0")` exactly — arithmetically guaranteed since the identical Q added at fill is subtracted at close; no epsilon exists anywhere. Simulator quote/fee outputs are cross-checked only: if `|sim_quote - Q*P| > max(1e-8, 1e-12*Q*P)` or the fee check fails, or side/amount disagree, **abort the run as ENGINE_MISMATCH** — never round, never absorb dust, never infer state from the simulator. `positions_held`, float-derived dust and the terminated-executor window are never read for state; the controller-side ledger alone drives FLAT/LONG.

## Required data

Only actual Binance BTC-USDT spot UTC 4h O/H/L/C/V. Indicator predicates use bar t's **completed** inputs at `E[t] = T[t] + 14400 seconds` (T[t] the exchange open timestamp); the queued order's fill at `E[t+1]` is not used retroactively. ROI age starts at the **confirmed full-fill** index, not the signal bar. No higher/lower timeframe, funding rate, order book, multi-asset feed, external sentiment or ML inference. Input validation: strictly increasing, gap-free 14400-second UTC open timestamps; finite positive O/H/L/C, `H >= max(O,C)`, `L <= min(O,C)`, `H >= L`, finite `V >= 0`, no duplicate bars. **Abort the research run** on any missing, invalid, duplicate or discontinuous candle; do not forward-fill, interpolate, fabricate prices, quietly skip a gap, or emit synthetic fills/mark prices.

## Execution assumptions

- **Pinned contract:** Hummingbot package **`20260920`**, `hummingbot/VERSION = dev-2.17.0` (bytes read at the bounded commit this run), bounded source commit **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`**. This cycle verified: `VERSION` file content `dev-2.17.0`; `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` `INTERVALS` maps **`4h`** (with `1m`/`5m`/`15m`/`1h`/`1d`); `backtesting_data_provider.py:140` returns `Decimal("1")` when price is absent — **never** used for fills or marking, actual positive closes required; `executors_simulator/order_executor_simulator.py:22` MARKET branch, `:56` takes the fill row's real `close` as `entry_price`, `:59` computes `float(config.amount) * entry_price`, `:62` `cum_fees_quote = trade_cost * amount_quote`, `:70` returns `CloseType.POSITION_HOLD`. The float line is exactly why this record's position truth is the independent Decimal ledger, never simulator auto-netting. No wheel re-download/hash this cycle; prior independently reviewed alpha PR **#414** reports 902/902 matching wheel Python files and SHA256 `ea5a929c...a148`; the independent Auditor must confirm that evidence applies to the pinned package and path.
- **Controller/executor:** `BacktestingEngineBase.simulate_execution` (`backtesting_engine_base.py:269`) iterates feature rows, updates state, then calls `controller.determine_executor_actions()` (`:284`) and processes `CreateExecutorAction` (`:33` import, `:285` branch). A **future dedicated controller is not implemented**; it must queue the previous completed signal and emit `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=TradeType.BUY/SELL, amount=Decimal("0.001"), position_action=OPEN/CLOSE, execution_strategy=ExecutionStrategy.MARKET, price=None, leverage=1)` on the designated fill row, without using that row to decide the preceding signal. No claim of a deployed controller or exchange-accepted order.
- **Actual fill path:** MARKET uses the fill row's real `close`; sets `filled_amount_quote = float(amount)*close`, `cum_fees_quote = trade_cost * filled_amount_quote`; returns `POSITION_HOLD`. The engine's raw row timestamp is bar-open; this research model reports the **effective historical fill event** as `E[fill_row]`, not a claim a real order could execute at the completed close. A delayed controller dispatch on row `t+1` is required. The simulator does not independently verify live latency, spread, partial fills, tick/lot/min-notional or exchange acceptance; any such failure aborts per the ledger rule instead of rounding.
- **Missing price and economic limitations:** no **additional modeled** slippage is included in this idealized MARKET-close research convention; this is **not** a claim of zero real slippage. The 0.1% fee is an explicit research assumption, **not** a verified Binance tier. Spot unleveraged BTC/USDT has no perpetual funding or liquidation cash flow; this does **not** assume perpetual funding is zero. Real exchange fees, liquidity, precision and market impact are unverified.
- **Reused capability boundary:** this uses only the already reviewed single-pair Binance spot OHLCV → controller action → MARKET-close `OrderExecutorSimulator` → POSITION_HOLD primitive, as previously documented in alpha PRs **#414** and **#550**. The new strategy changes only controller-side SMA-ratio predicates, the ROI/stop bar-close stack and the Decimal ledger; not the data/executor market path. No Hummingbot or Qlib test is performed in this Scout. If a new execution primitive is required, one representative Hummingbot↔Qlib event-level parity validation is required **before mass screening**, not as a profitability admission gate.

## Evidence

### Source-reported

The pinned `mabStra.py` bytes support every constant cited above (timeframe, ROI ladder, stop, all six MA defaults, all four div bounds, trigger column names). The file's hyperopt paste-block is the coded default set, not traceable performance evidence, and supports no performance claim.

### Independently reproduced

**None** for this candidate's freqtrade trades, Hummingbot/Qlib events, performance, OOS or realized fees. Only the pinned strategy bytes and pinned-engine source paths above were inspected; prior PR engine proof is referenced with limitations.

### Negative evidence

Pre-write dedup 2026-10-30 against `main@a7edc722` (**464** root-level strategy records, README counter **464** — full tree, excluding two READMEs): filename/content search for `mabstra`, `buy-mojoMA`, `buy_div_min`, `0.29497`, and `sell_div_min` with `2.81436` returns **zero strategy records** — no pool record sources this file or its dual-ratio-band rule. The twelve open `research/*` PRs (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646) were inspected by source/title/branch and none uses this source or the SMA-ratio div-band rule. Nearest pool neighbors use different mechanisms: `freqtrade-multima-tema-stack` (stacked TEMA trend agreement, 4h — no ratio bands, no dead exit), `freqtrade-crossema-28-48` (dual-EMA alignment plus raw StochRSI threshold, 1h), `freqtrade-strategy003` (RSI/Fisher/MFI washout, 5m) — none conjoins dual close-SMA ratio bands with an inverted-bound dead signal-exit under this ROI/stop stack on 4h. This is not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

Future authorized research only (no backtest, trading, deployment or cron change here): aligned-stack liveness bar (ratios ≈ 1.0 firing); splayed-stack refusal above 2.25446 and inverted-stack refusal below 0.29497; bound-equality no-fire cases; dead-leg formal check (no `exit_long == 1` on any bar); pre-seed NaN no-fire bars; warmup 26/27 boundary; signal t versus fill f; stop versus ROI priority ties; ROI age boundaries 1/3/14/31; insufficient cash; last-bar pending; full-fill fee ledger; `Decimal(str())` versus float reconciliation; ENGINE_MISMATCH abort path.

## Crypto portability

Binance BTC-USDT spot, 4h, unleveraged long-flat. The long-only book expresses unchanged on a spot venue with no borrowing, no leverage and no funding leg. No perpetual, margin, multi-asset, or cross-venue dependency is introduced. Real venue precision (tick/lot/min-notional), fees and liquidity must still abort-or-verify per the ledger rule before any execution use.

## Limitations

- Idealized next-completed-bar-close MARKET fills; no claim a live order achieves the completed close; no slippage model beyond the assumed 0.1% per-side fee (not a verified Binance tier).
- The dead signal-exit is kept as coded (evaluated, never firing); trade events equal ROI/stop-only exits — disclosed, not repaired.
- Intrabar freqtrade ROI/stop timing is adapted to completed-bar-close with stop → ROI priority; trade events differ from live freqtrade semantics.
- Exact-Decimal SMA arithmetic is pinned for reproducibility; bit-identity with any particular TA-Lib float build is not claimed — threshold-boundary sensitivity is disclosed.
- The file sets no `startup_candle_count`; the 27-bar warmup is the researcher-specified full-seeding choice (first SMA-28 bar), not a source constant.
- PASS here means pinned-engine expressibility of this fully specified derivative, not profitability, Qlib parity, Survivor status, source-native equivalence, or any live/Paper/Testnet authorization.

## Implementation status

`implementation_status: not-implemented`. No controller, executor config, backtest, Qlib recipe, or deployment artifact is created here. If this candidate is formally selected for execution without a reproducible executable recipe, the engineering route is `IMPLEMENTATION_NEEDED` (minimal strategy-specific implementation, then the same 01–05), never a second admission flag.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. `hb_ready_status: PASS` is a **Scout six-gate proposal awaiting independent Hermes Auditor review**, not independent approval, Qlib parity, Survivor, Hummingbot Certified, profitability or Paper/Testnet/Live authorization. The Auditor alone may source-fact remediate the exact head, merge on verified PASS, or close NOT_LOSSLESS. The existing signed GitHub webhook receiver alone performs post-merge README bookkeeping; Scout does not touch main/README or any workflow.

## Related Wiki records

None. This Scout cycle writes no Wiki Brain records.
