---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "freqtrade Bandtastic 1σ typical-price lower touch with MFI46-gated 2σ upper exit; independent BTC-USDT spot 15m long-flat derivative v2"
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Bandtastic.py
  - https://github.com/TA-Lib/ta-lib/blob/v0.6.4/src/ta_func/ta_MFI.c
  - https://github.com/freqtrade/technical/blob/78061e943282152344c6f774347d18b19e20b7e3/technical/vendor/qtpylib/indicators.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bandtastic 1σ/2σ band MFI-gated touch — independent derivative v2

## Provenance

- **Primary source:** public freqtrade strategy collection `freqtrade/freqtrade-strategies`, file `user_data/strategies/Bandtastic.py` (author Robert Roman, `__version__ = "1.0"`, class `Bandtastic(IStrategy)`, the only class in the file), read in full at immutable commit **`f3340ce11f5bdf62f598522e64d1f5638eaa13f5`** (2026-09-08): https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Bandtastic.py . Verified bytes this run: **163 lines, 7310 bytes**, SHA256 `15dcb60d49a3681241cd39645f0fe8e6dc247687bf878c2026f37bb1c5790b57`, Git blob SHA `f7710c76ae1e4ac7aff90857a647e4c2143baf9f` matching the GitHub API blob SHA at the pinned commit. No login, no paywall.
- **Source facts actually verified (effective defaults):** `INTERFACE_VERSION = 3`; `timeframe = '15m'`; `minimal_roi = {"0": 0.162, "69": 0.097, "229": 0.061, "566": 0}` (freqtrade minutes); `stoploss = -0.345`; `startup_candle_count = 999`; `trailing_stop = True`, `trailing_stop_positive = 0.01`, `trailing_stop_positive_offset = 0.058`, `trailing_only_offset_is_reached = False`. Entry-leg defaults: `buy_rsi_enabled = False`, `buy_mfi_enabled = False`, `buy_ema_enabled = False`, `buy_trigger = "bb_lower1"` — so the effective entry is `close < bb_lowerband1` plus the file's `volume > 0` guard. Exit-leg defaults: `sell_rsi_enabled = False`, `sell_mfi_enabled = True` (`sell_mfi = 46`), `sell_ema_enabled = False`, `sell_trigger = "sell-bb_upper2"` — so the effective exit is `mfi > 46` AND `close > bb_upperband2` plus `volume > 0`. Indicator construction: `ta.RSI`, `ta.MFI` (both TA-Lib defaults, 14 periods, pinned by call), four typical-price Bollinger sets `qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=1..4)`, and an EMA union over the hyperopt ranges (max period 365) that is computed but never read by any order line (fenced below). Full-file token census this run: 0 `short` (case-insensitive — no short leg or short identifier anywhere, so `can_short` is absent and long-only holds); 0 `protection`; 0 `resample` / `informative` / `request` / `security`; 0 `position_adjustment` / `pyramiding` / `cooldown` / `max_open_trades`; 0 `leverage` / `order_types` / `order_time_in_force` / `funding` / `mark_price`; 0 `use_exit_signal` / `exit_profit_only` / `ignore_roi` overrides. The hyperopt `*Parameter` spaces carry the pinned `default=` values above; only those defaults bind this record.
- **Dead columns fenced (computed, never gated):** `rsi` (both RSI guards default False), every `EMA_{period}` (both EMA guards default False), `bb_middleband*`, `bb_upperband1`, and the entire `bb_*band2/3/4` sets except `bb_upperband2`, plus `bb_lowerband2/3/4` (triggers pin only `bb_lower1` / `sell-bb_upper2`). No reviewer repair may substitute a sibling trigger or enable a fenced guard.
- **Prior proposal of this same source:** PR **#453** (`research/hermes-bandtastic-dualbb-mfi-20261026-0145`) was closed `NOT_LOSSLESS` with exactly three blockers: (1) a Wilder-smoothed MFI mislabeled as TA-Lib MFI (threshold-counterexample at MFI 46); (2) an internally contradictory zero-volatility no-op claim on the entry leg; (3) an incompletely defined MFI denominator for the positive-only-flow state. This v2 record is a **new researcher-specified derivative** that answers all three with explicit choices: (1) the true TA-Lib **rolling-sum** MFI pinned formula-for-formula against `ta_MFI.c` v0.6.4 (ring-buffer sums, `100*pos/(pos+neg)`, `total < 1.0 → 0.0`); (2) the **literal** entry predicate with no SD veto — the flat-typical-price/low-close bar deterministically fires, disclosed as specified behavior; (3) fully specified degenerate MFI values (`neg == 0` with `pos ≥ 1 → 100`; `pos + neg < 1.0 → 0.0`; no division by zero exists). Unlike #453 (which dropped the risk legs), this v2 **keeps the full source risk stack** (ROI ladder, −34.5% stop, trailing triple) as a Diamond-style bar-close derivative, predeclared below. The #453 branch/history is preserved and untouched.
- **Independent researcher-defined executable derivative (NOT source-native):** source pair list is agnostic, so pin single-asset Binance **BTC-USDT spot 15m**; freqtrade intrabar stop/ROI/trailing evaluation is adapted to **completed-bar-close evaluation with pinned priority stop-level → ROI → exit-signal**; ROI minutes map to completed post-fill 15m bars by ceiling division (69→5, 229→16, 566→38); the trailing leg uses `max(P*(1-0.345), hwm*(1-0.01))` from the fill bar, with no offset switch. This is NOT literal freqtrade trailing semantics: official stoploss documentation states that `trailing_only_offset_is_reached = False` permits trailing before the offset, while `trailing_stop_positive_offset` still controls switching from the ordinary stoploss distance to the positive trailing distance. Thus omitting the source 0.058 switch and applying 0.01 immediately is an additional event-changing difference already fixed by this derivative formula, not a source-preserved fact; fills are next-completed-bar-close historical MARKET fills; fixed `Q = Decimal("0.001")` BTC, 10,000 USDT starting cash, 0.1% hypothetical per-side fee, 999-bar warmup (the file's own `startup_candle_count`), exact-Decimal ledger with fail-closed reconciliation. These researcher choices change trade events and economics.
- **Frozen identity:** `FT:Bandtastic.py|f3340ce|RobertRoman-v1.0|independent-derived-v2-20261030|BinanceSpot-BTC-USDT-UTC15m|C-lowerBB20x1-touch-volpos|MFI14roll>46-and-C-upperBB20x2-volpos|ROI16.2/9.7@5/6.1@16/0@38-gross|stopmax(-34.5pct,hwm*(1-0.01))|next-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-each-side|warmup999|Decimal-ledger`. Any signal, timing, cost or position change creates a different derivative.

## Economic mechanism

### Source-reported

The file's header reports a Sharpe-optimized 15m dip system (199/40000 hyperopt line: 30918 trades, +119.93% total — an author anecdote, **not traceable table/figure evidence and not relied upon here**). The coded mechanism: buy the bar where the close undercuts the 1σ typical-price lower band on positive volume (a shallow-band touch, no oscillator gate — all entry guards default off); stand aside to flat when money flow overheats (rolling MFI14 above 46) while the close over-extends above the 2σ upper band, behind a decaying four-rung ROI ladder (16.2% → 9.7% → 6.1% → 0%), a −34.5% disaster stop, and a 1% high-water trailing leg.

### Research interpretation

A shallow-touch fade machine with a money-flow-gated profit exit, long-only. Unlike deep-penetration dip records (2σ–4σ breaks, RSI washouts), the 1σ touch fires on ordinary band kisses — frequency comes from the trigger, selectivity from the exit: the MFI46-plus-2σ-upper conjunction refuses to bank chop that never attracted real money flow. Unlike pure oscillator exits (RSI-70 prints alone), the exit demands price-location proof (close above the wide upper rail) AND flow proof (MFI above 46) on the same bar. The coded consequence is a buyer of minor band weakness that harvests only flow-confirmed over-extension, with a wide disaster stop and a tight high-water ratchet behind every position. No performance, profitability, Qlib parity or Survivor claim.

## Signal

Exact rules as pinned (any other band window, sigma, lookback, threshold, price basis, ROI rung, stop, fill, frame, book, or leg combination is a different, unpinned rule):

```text
TP[t]   = (H[t] + L[t] + C[t]) / 3                                   // exact Decimal
mid[t]  = mean(TP[t-19 .. t])                                         // 20-bar
sd[t]   = sample std, ddof=1, of TP[t-19 .. t]                        // 20-bar
L1[t]   = mid[t] - 1*sd[t]                                            // entry rail
U2[t]   = mid[t] + 2*sd[t]                                            // exit rail
MF[i]   = TP[i]*V[i]; d[i] = TP[i] - TP[i-1]
pos[t]  = Σ MF[i] over i in t-13..t with d[i] > 0                     // rolling, TA-Lib
neg[t]  = Σ MF[i] over i in t-13..t with d[i] < 0                     // rolling, TA-Lib
MFI[t]  = 100*pos[t]/(pos[t]+neg[t]) if pos[t]+neg[t] >= 1.0 else 0.0
ENTER[t]   = (C[t] < L1[t]) AND (V[t] > 0)                            // enter_long = 1
EXITSIG[t] = (MFI[t] > 46) AND (C[t] > U2[t]) AND (V[t] > 0)          // exit_long = 1
```

- **MFI pin (answers #453 blocker 1 and 3):** this is the true TA-Lib rolling-sum construction verified line-for-line against `TA-Lib/ta-lib@v0.6.4/src/ta_func/ta_MFI.c` (ring-buffer `(positive, negative)` per-bar flows, `MFI = 100*(posSum/(posSum+negSum))` per the file's own "second equation" comment, `posSum+negSum < 1.0 → 0.0`) — explicitly **not** Wilder smoothing. Degenerate states are fully specified: all-up flow (`neg == 0`, `pos ≥ 1`) → `100`; no/epsilon flow (`pos + neg < 1.0`) → `0.0`; flat-TP bars contribute `(0, 0)` to their ring slot. No division by zero exists anywhere. First defined MFI needs 14 comparisons (index ≥ 14); the 999-bar warmup covers it with margin.
- **BB pin:** self-contained transcription of the maintained-framework `bollinger_bands(typical_price, window=20, stds=k)` (`freqtrade/technical@78061e943282152344c6f774347d18b19e20b7e3`, `technical/vendor/qtpylib/indicators.py`: `typical_price = (H+L+C)/3`, `ma`/`std` via `rolling(window=20, min_periods=1)` mean/std with pandas default ddof=1). Post-warmup windows are always full (999 ≫ 20), so the `min_periods=1` early path never binds a decision — disclosed, not relied upon.
- **Literal entry (answers #453 blocker 2):** no SD veto is added. A bar with flat trailing typical prices (`sd == 0`, `L1 == TP`) but `C < TP` and `V > 0` **fires** `ENTER` deterministically. That is specified behavior of this derivative, not a contradiction and not a no-op clause.
- **Mutual-exclusion proof (no tie-break pin required):** when `sd[t] > 0`, `L1[t] < U2[t]` strictly, so `C < L1` and `C > U2` cannot co-print; when `sd[t] == 0`, `L1 == U2 == mid`, so the strict price comparisons remain mutually exclusive, but are not necessarily both false: `C < mid` with `V > 0` still fires ENTER, as specified above. No zero-SD veto is implied. Entry and signal-exit never co-fire on any bar. ROI/stop cannot co-fire with entry on the fill bar (zero distance at fill).
- **Exact boundaries:** strict throughout (`<`, `>` — a close exactly on a rail, volume exactly zero, or MFI exactly 46 fires nothing). Strictness preserved, never smoothed.
- **Warmup:** first **999** valid fully completed 15m bars, indices 0–998, are data-only, FLAT, and never emit orders (the file's own `startup_candle_count`). First decision may occur at index 999 (covers the 20-bar band seed, the 14-comparison MFI seed, and the 365-bar EMA span that is computed-but-fenced). No optimizer, ML, external feed, negative shift, future extremum, repaint or fitted parameter at research time; hyperopt `*Parameter` spaces are inert — only the pinned `default=` constants above bind.
- **BUY state:** initial `FLAT`, 0 BTC, 10,000 USDT cash. At eligible `E[t]` (`t >= 999`), if FLAT with no pending order and `ENTER[t]` true, queue exactly one fixed `Q = Decimal("0.001")` BTC MARKET BUY for the **next completed bar** `f = t+1`; do not use bar f's data to decide at t. At `E[f]`, use actual finite `C[f]` as the idealized simulator fill, if `cash >= Q*C[f]*(1+fee)` in exact Decimal. If insufficient cash, consume the signal, remain FLAT, and do not invent a partial fill or deferred order. A confirmed full fill sets LONG, records fill price `P = C[f]` and `fill_index = f`. No signal or exit evaluation on the fill bar.
- **LONG exits (evaluated at each `E[t]`, `t > f`, in fixed priority; at most one exit per bar):** (1) **stop-level:** `hwm[t] = max(C[f..t])`, `stop_level[t] = max(P*(1-0.345), hwm[t]*(1-0.01))`; exit if `C[t] <= stop_level[t]`; (2) **ROI ladder** on fee-exclusive gross `(C[t]-P)/P` with post-fill bar age `a = t-f`: `>= 0.162` at any `a >= 1`, `>= 0.097` at `a >= 5`, `>= 0.061` at `a >= 16`, `>= 0` at `a >= 38`; exit if the age-eligible threshold holds; (3) **exit-signal:** exit if `EXITSIG[t]` true. The winning exit queues exactly one MARKET SELL for the next completed bar `s = t+1` at real `C[s]`, sells the full Q, sets FLAT. No exit executes if its required future bar is absent; the pending order stays unfilled at sample end. No evaluation on the SELL fill bar; earliest re-entry decision is a later eligible bar.
- **State priority and exclusions:** at most one pending action and one position; a pending order takes precedence over new signals. There is no cooldown, pyramiding, DCA/safety orders, averaging, partial sizing, shorts, borrowing, leverage, margin, shared-capital concurrency, session filter, intrabar stop/limit/maker, or end-of-sample forced liquidation. An open LONG at the end is valued at the last **actual valid close**, never synthetically liquidated. Same-bar entry/exit exclusion holds by construction: entries act only from FLAT, exits only while LONG, and fill bars evaluate nothing.
- **Exact Decimal ledger (position truth):** all research accounting uses `Decimal(str(x))` for observed closes (never `Decimal(float)`), exact `Q`, exact products. BUY debits `Q*P*(1+fee)` USDT and credits exactly Q BTC; SELL debits exactly Q BTC and credits `Q*P*(1-fee)` USDT. `FLAT` holds **iff** ledger BTC `== Decimal("0")` exactly — arithmetically guaranteed since the identical Q added at fill is subtracted at close; no epsilon exists anywhere. Round-trip net is `Q*(P_sell-P_buy) - fee*Q*(P_buy+P_sell)`. Simulator quote/fee outputs are cross-checked only: if `|sim_quote - Q*P| > max(1e-8, 1e-12*Q*P)` or the fee check fails, or side/amount disagree, **abort the run as ENGINE_MISMATCH** — never round, never absorb dust, never infer state from the simulator. `positions_held`, float-derived dust and the terminated-executor window are never read for state; the controller-side ledger alone drives FLAT/LONG.

## Required data

Only actual Binance BTC-USDT spot UTC 15m O/H/L/C/V. Indicator-free-plus-indicator predicates use bar t's **completed** inputs at `E[t] = T[t] + 900 seconds` (T[t] the exchange open timestamp); the queued order's fill at `E[t+1]` is not used retroactively. Stop-level high-water mark and ROI age start at the **confirmed full-fill** index, not the signal bar. No higher/lower timeframe, funding rate, order book, multi-asset feed, external sentiment or ML inference. Input validation: strictly increasing, gap-free 900-second UTC open timestamps; finite positive O/H/L/C, `H >= max(O,C)`, `L <= min(O,C)`, `H >= L`, finite `V >= 0`, no duplicate bars. **Abort the research run** on any missing, invalid, duplicate or discontinuous candle; do not forward-fill, interpolate, fabricate prices, quietly skip a gap, or emit synthetic fills/mark prices.

## Execution assumptions

- **Pinned contract:** Hummingbot package **`20260920`**, `hummingbot/VERSION = dev-2.17.0` (bytes read at the bounded commit this run), bounded source commit **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`**. This cycle verified: `VERSION` file content `dev-2.17.0`; `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` `INTERVALS` maps **`15m`** (with `1m`/`5m`/`1h`/`4h`/`1d`); `backtesting_data_provider.py:140` returns `Decimal("1")` when price is absent — **never** used for fills or marking, actual positive closes required; `order_executor_simulator.py:56` MARKET takes the supplied row's real `close` as `entry_price`, line 59 computes `float(config.amount) * entry_price`, line 70 returns `CloseType.POSITION_HOLD`. The float line is exactly why this record's position truth is the independent Decimal ledger, never simulator auto-netting. No wheel re-download/hash this cycle; prior independently reviewed alpha PR **#414** reports 902/902 matching wheel Python files and SHA256 `ea5a929c...a148`; the independent Auditor must confirm that evidence applies to the pinned package and path.
- **Controller/executor:** `BacktestingEngineBase.simulate_execution` iterates feature rows, updates state, then calls `controller.determine_executor_actions()` and processes `CreateExecutorAction`. A **future dedicated controller is not implemented**; it must queue the previous completed signal and emit `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=TradeType.BUY/SELL, amount=Decimal("0.001"), position_action=OPEN/CLOSE, execution_strategy=ExecutionStrategy.MARKET, price=None, leverage=1)` on the designated fill row, without using that row to decide the preceding signal. No claim of a deployed controller or exchange-accepted order.
- **Actual fill path:** MARKET uses the first supplied row's real `close`; sets `filled_amount_quote = float(amount)*close`, `cum_fees_quote = trade_cost * filled_amount_quote`; returns `POSITION_HOLD`. The engine's raw row timestamp is bar-open; this research model reports the **effective historical fill event** as `E[fill_row]`, not a claim a real order could execute at the completed close. A delayed controller dispatch on row `t+1` is required. The simulator does not independently verify live latency, spread, partial fills, tick/lot/min-notional or exchange acceptance; any such failure aborts per the ledger rule instead of rounding.
- **Missing price and economic limitations:** no **additional modeled** slippage is included in this idealized MARKET-close research convention; this is **not** a claim of zero real slippage. The 0.1% fee is an explicit research assumption, **not** a verified Binance tier. Spot unleveraged BTC/USDT has no perpetual funding or liquidation cash flow; this does **not** assume perpetual funding is zero. Real exchange fees, liquidity, precision and market impact are unverified.
- **Reused capability boundary:** this uses only the already reviewed single-pair Binance spot OHLCV → controller action → MARKET-close `OrderExecutorSimulator` → POSITION_HOLD primitive, as previously documented in alpha PRs **#414** and **#550**. The new strategy changes only controller-side band/MFI predicates, the ROI/stop/trailing bar-close stack and the Decimal ledger; not the data/executor market path. No Hummingbot or Qlib test is performed in this Scout. If a new execution primitive is required, one representative Hummingbot↔Qlib event-level parity validation is required **before mass screening**, not as a profitability admission gate.

## Evidence

### Source-reported

The pinned `Bandtastic.py` bytes support every constant cited above (defaults, ROI ladder, stop, trailing triple, startup count, trigger names, volume guards). The file's hyperopt anecdote line is not traceable evidence and supports no performance claim. The TA-Lib `ta_MFI.c` v0.6.4 bytes support the rolling-sum formula, the `total < 1.0 → 0.0` guard, and the flat-TP `(0,0)` ring-slot behavior cited above. The `technical@78061e9` vendor `indicators.py` bytes support the `typical_price` and `bollinger_bands` transcription cited above.

### Independently reproduced

**None** for this candidate's freqtrade trades, Hummingbot/Qlib events, performance, OOS or realized fees. Only the pinned strategy bytes, the TA-Lib MFI source, the framework band semantics and pinned-engine source paths above were inspected; prior PR engine proof is referenced with limitations.

### Negative evidence

Pre-write dedup 2026-10-30 against `main@fa1d7900` (**446** root-level strategy records, README counter **446** — full tree, excluding two READMEs): filename/content search for `bandtastic`, `bb_lowerband1`, `sell-bb_upper2`, `0.058`, and `startup_candle_count` with 999 returns **zero strategy records** — the only `bandtastic` hits pool-wide are sibling-file fence prose lines (in the CrossEMA, Diamond, HLHB and erendev-harami records), never a Bandtastic-sourced rule. The eleven open `research/*` PRs (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593) were inspected by source/title/branch and none uses this source or the 1σ-touch/MFI46-gated-2σ rule. Closed-PR search returns only this source's own prior v1 (#453, NOT_LOSSLESS, whose three blockers are answered above as explicit researcher choices — not a source fact the reviewer must invent). Nearest pool neighbors use different mechanisms: `freqtrade-bband-rsi-dip-buy` (RSI<30 AND 2σ penetration entry, RSI-70 exit, no MFI, no trailing, 1h), `freqtrade-low-bb-98-sub-band` (sub-band fraction dip, 1m), `fmz-483087-triple-bollinger` (triple-band simultaneous breach, 1h), `freqtrade-crossema-28-48` (dual-EMA alignment plus raw StochRSI threshold, 1h) — none conjoins a 1σ typical-price lower touch with a rolling-MFI46-gated 2σ upper exit under this ROI/stop/trailing stack on 15m. This is not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

Future authorized research only (no backtest, trading, deployment or cron change here): MFI rolling-vs-Wilder divergence cases at the 46 boundary; all-up-flow → 100 and dust-flow → 0.0 degenerate bars; zero-SD band bars with `C < TP` firing entry; rail-equality and MFI-exactly-46 no-fire boundaries; `sd == 0` mutual-exclusion (entry may still fire); warmup 998/999 boundary; signal t versus fill f; stop-level versus ROI versus exit-signal priority ties; ROI age boundaries 1/5/16/38; insufficient cash; last-bar pending; full-fill fee ledger; `Decimal(str())` versus float reconciliation; ENGINE_MISMATCH abort path.

## Crypto portability

Binance BTC-USDT spot, 15m, unleveraged long-flat. The long-only book expresses unchanged on a spot venue with no borrowing, no leverage and no funding leg. No perpetual, margin, multi-asset, or cross-venue dependency is introduced. Real venue precision (tick/lot/min-notional), fees and liquidity must still abort-or-verify per the ledger rule before any execution use.

## Limitations

- Idealized next-completed-bar-close MARKET fills; no claim a live order achieves the completed close; no slippage model beyond the assumed 0.1% per-side fee (not a verified Binance tier).
- The 0.058 trailing-offset switch is omitted by researcher choice (disclosed above); trade events differ from literal freqtrade trailing.
- Exact-Decimal band/MFI arithmetic is pinned for reproducibility; bit-identity with any particular TA-Lib float build is not claimed — threshold-boundary sensitivity is disclosed.
- `min_periods=1` early-window framework behavior is fenced as never binding post-warmup, not re-derived.
- PASS here means pinned-engine expressibility of this fully specified derivative, not profitability, Qlib parity, Survivor status, source-native equivalence, or any live/Paper/Testnet authorization.

## Implementation status

`implementation_status: not-implemented`. No controller, executor config, backtest, Qlib recipe, or deployment artifact is created here. If this candidate is formally selected for execution without a reproducible executable recipe, the engineering route is `IMPLEMENTATION_NEEDED` (minimal strategy-specific implementation, then the same 01–05), never a second admission flag.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. `hb_ready_status: PASS` is a **Scout six-gate proposal awaiting independent Hermes Auditor review**, not independent approval, Qlib parity, Survivor, Hummingbot Certified, profitability or Paper/Testnet/Live authorization. The Auditor alone may source-fact remediate the exact head, merge on verified PASS, or close NOT_LOSSLESS. The existing signed GitHub webhook receiver alone performs post-merge README bookkeeping; Scout does not touch main/README or any workflow.

## Related Wiki records

None. This Scout cycle writes no Wiki Brain records.

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Bandtastic.py — Robert Roman, *Bandtastic* v1.0, pinned commit 2026-09-08 (163 lines, 7310 bytes, SHA256 `15dcb60d…0b57`, blob `f7710c76…43baf9f`).
- https://github.com/TA-Lib/ta-lib/blob/v0.6.4/src/ta_func/ta_MFI.c — first-party TA-Lib rolling-sum MFI with ring-buffer flows and the `total < 1.0 → 0.0` guard, read 2026-10-30.
- https://github.com/freqtrade/technical/blob/78061e943282152344c6f774347d18b19e20b7e3/technical/vendor/qtpylib/indicators.py — maintained `typical_price` / `bollinger_bands` / rolling helpers, read 2026-10-30.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine source inspected (VERSION, 15m INTERVALS, MARKET-close simulator path).
- https://github.com/HCH725/alpha-strategy-research/pull/414 — prior independent pinned wheel/source and MARKET primitive evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/550 — prior bounded spot MARKET-close research execution evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/453 — this source's prior v1 proposal, closed NOT_LOSSLESS with three exact blockers answered in this v2 record.
- https://www.freqtrade.io/en/stable/stoploss/#trailing-stop-loss-different-positive-loss — official first-party clarification of ordinary trailing versus the positive-distance offset switch; corrects source attribution only, not the derivative formulas.
