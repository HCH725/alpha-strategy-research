---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven ADX 14 / ±DI 14 trend-pulse DI-cross long-flat on BTCUSDT 1h bars
created: 2026-10-24
updated: 2026-10-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-24
sources:
  - https://github.com/judder659/Forven/blob/0e35d7dd3f84a8ef6d8d7a3b131ff366585a451e/forven/strategies/builtin/adx_trend.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven ADX 14 / ±DI 14 trend-pulse DI-cross long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the fifty-three admitted Forven records, including the `forven-adx-trend-pulse-reclaim` sibling admitted 2026-10-17 that pins a different file in the same family).
- Pinned commit SHA: `0e35d7dd3f84a8ef6d8d7a3b131ff366585a451e` (verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is the cycle date, never a fetch date).
- Exact file path: `forven/strategies/builtin/adx_trend.py`.
- GitHub blob SHA at the pinned commit: `b92a9291eca8d3ba522f3bf7f1a1427dd0a9a377`, size 3855 bytes.
- Byte-identity check: the file on disk at the pinned commit is 3855 bytes, 123 lines, `git hash-object` reproduces `b92a9291…0a9a377` — the entire file was retrieved and inspected.
- Registration: the file defines class `ADXTrendStrategy(BaseStrategy)` (the only class in the file) with `TYPE_NAME = "adx_trend"` and a one-row roster `STRATEGIES = [("PREBUILT-ADX-TREND", ADXTrendStrategy, {"_asset": "BTC"})]` — venue spelling is the bare `"BTC"` asset label only, no timeframe override. Identity here is class plus file path plus `TYPE_NAME`, all unique.
- The file's own words (quoted for gate evidence, never extended): class docstring `Entry: ADX > threshold AND +DI crosses above -DI.` / `Exit: ADX drops below threshold OR -DI crosses above +DI.`; `default_params` returns exactly `{ "adx_period": 14, "adx_threshold": 25, "di_period": 14, "leverage": 1.0 }`; `describe()` prints `Enters when ADX(14) > 25 and +DI crosses above -DI. Exits when ADX falls below threshold or -DI crosses above +DI.`; the short-frame guard `min_bars = max(di_period, adx_period) * 2 + 2` (i.e. 30) returns the explicit no-signal `Signal(entry False, exit False, price 0.0)`; the gating lines read `adx_strong = curr_adx > p["adx_threshold"]`, `plus_cross_up = prev_plus_di <= prev_minus_di and curr_plus_di > curr_minus_di`, `minus_cross_up = prev_minus_di <= prev_plus_di and curr_minus_di > curr_plus_di`, `entry = adx_strong and plus_cross_up`, `exit_ = (curr_adx < p["adx_threshold"]) or minus_cross_up`; every return hardcodes `direction="long"`; per-bar confidence is `min(1.0, curr_adx / 50)` when strong else `0.0`. No performance phrase of any kind ships anywhere in the 123 lines.
- Indicator bloodline pinned at the same commit (actually read, never assumed): the ±DI legs are built in-file from `high.diff()` / `-low.diff()` signed directional movement, smoothed with `.ewm(span=14, adjust=False).mean()` and divided by `atr(df, 14)`; the strength leg `adx(df, 14)` and the echo `atr(df, 14)` resolve through the indicators PEP 562 `__getattr__` lazy facade (`_FACADE_NAMES` contains both `"adx"` and `"atr"`), re-exporting the pure helpers from canonical home `forven.scanner` — actually imported and called this cycle. `scanner.adx` (lines 1933–1947) is Wilder-style directional movement with `ewm(span=period)` ATR/DI/DX smoothing; `scanner.atr` (lines 1950–1961) is a rolling-mean (SMA) of true range. Both read only trailing `high`/`low`/`close` with `.diff()` / `.shift()` / `.ewm()` / `.rolling()` — no forward reference anywhere.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (12238 bytes, blob `27508a2a6b8c546e21adefdb97fc0144fabf881b` — byte-identical to the blob pinned by every admitted Forven sibling) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults and `direction: str = "long"` default. The file's explicit `direction="long"` on every return needs no default reading.
- Full-file token census (verified over the 123 lines this cycle): 0 `short` (no short leg, no short identifier anywhere); 0 `open` / 0 `volume` (sole `df[` reads are `high`/`low`/`close`); 0 `funding` / 0 `mark_price`; 0 `request` / 0 `security`; 0 `resample` / 0 `informative`; 0 `hyperopt`; 0 `trailing` / 0 `stoploss`; 0 `order_types`; 0 `pyramid` / 0 `position_` / 0 `cooldown` / 0 `max_open_trades` (the position pin below is a predeclared researcher rule, never a file semantic); 0 `timeframe` (the file declares no frame — the `1h` pin below is a disclosed researcher choice); 2 `direction` (the guard return plus the signal return, both `direction="long"`); the single `leverage` token is the `"leverage": 1.0` defaults entry — an unleveraged hint explicitly adopted (see Execution assumptions); `compatible_regimes = {"TREND_UP", "TREND_DOWN"}` is class metadata read by zero signal lines (fenced, never promoted).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Forven deployment. The source pins the ADX14>25 strength gate, the fresh +DI-cross trigger, the ADX<25-or-−DI-cross exit, the long-only stance, the 30-bar guard, and the no-stop posture — but ships no venue spelling beyond `"BTC"`, no frame, no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market/frame `BTCUSDT` spot `1h` (the roster names `"BTC"` and the file declares no frame; venue spelling and the `1h` decision-frame pin are disclosed, never a source claim); (2) completed-bar decisions at effective time `timestamp + 3600s` with MARKET fills at the decision bar's own close on the cited pinned-engine path (the file returns `price=round(curr_close, 4)` — the decision bar's own close; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit `0.001` BTC position pin with controller-memory state machine plus a 100-bar researcher warmup floor (covers the source's own 30-bar guard with margin; see Required data); (4) the pinned research cost model below (fee 0.001/side post-hoc, slippage 0, funding not applicable on spot, no exchange lot/tick quantization in-path) replacing the absent source economics, with the file's `"leverage": 1.0` hint explicitly adopted as unleveraged spot. This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-24): working-tree fixed-string search for `builtin/adx_trend.py`, `PREBUILT-ADX-TREND"`, and `ADXTrendStrategy` returns zero strategy records citing this source file (the `forven-adx-trend-pulse-reclaim` sibling cites `builtin/adx_trend_pulse.py` / `PREBUILT-ADX-TREND-PULSE` — a different file, fenced in Negative evidence 1). No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades a ±DI-cross rule. Not a duplicate, paraphrase, or trivial parameter variant: a naked ADX>25-gated fresh +DI edge-cross with an ADX-collapse-or-−DI-cross exit, long-flat, on `1h` bars from this immutable file is fenced against every ADX/DI pool-mate in Negative evidence 1–5.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar whose +DI crosses from at-or-below −DI to strictly above it while ADX(14) prints strictly above 25; stand back to flat on any bar whose ADX(14) prints strictly below 25 or whose −DI crosses from at-or-below +DI to strictly above it. Strength without a fresh cross never enters; a fresh cross without strength never enters; weakness alone (ADX sag with no opposing cross) exits. No stop, no target, no trailing, no time exit, no sizing, no cost basis ships anywhere — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Naked trend-pulse timer, long-only, edge-triggered on direction with a level-gated veto on strength. The +DI edge is the only way in and it must arrive while the trend meter already reads strong; the exit is deliberately asymmetric — either leg alone suffices, so a strength collapse exits even while +DI still leads, and an opposing cross exits even while ADX still reads strong. Unlike level-state cousins (pool's freqtrade ADX-momentum sibling holds only while four conjuncts jointly print and carries ROI/stop legs), flat here means only "no fresh cross printed under strength" (or "weakness printed"), never "momentum vetoed". Unlike the file-family pulse sibling (slow-EMA trend × ADX floor × pullback-touch window × EMA reclaim — four conjuncts), there is no trend-filter leg and no pullback leg: any fresh +DI cross under ADX>25 fires, however extended the move already is. The failure mode is plain: chop that alternates shallow DI crosses whipsaws the book with no cooldown (each fresh cross re-arms immediately after any exit), and ADX's double smoothing lags every V-turn — recoveries are entered strictly after both the cross and the strength reclaim print, while slow bleeds under ADX 25 are watched from flat with no short participation.

## Signal

Exact rule as pinned (any other adx/di period, threshold, trigger polarity, gate, frame, fill, book, or risk posture is a different, unpinned rule). `ewm(14)` is `span=14, adjust=False`; `SMA14` is `.rolling(14).mean()`:

```text
up_move_t   = high_t − high_{t−1};  down_move_t = −(low_t − low_{t−1})
plus_DM_t   = up_move_t   if (up_move_t > down_move_t and up_move_t > 0) else 0
minus_DM_t  = down_move_t if (down_move_t > up_move_t and down_move_t > 0) else 0
atr14_t     = SMA14(TR_t)                                   // scanner rolling ATR
plus_DI_t   = 100 × ewm14(plus_DM)_t / atr14_t
minus_DI_t  = 100 × ewm14(minus_DM)_t / atr14_t
adx_t       = scanner.adx(high, low, close, 14)_t            // ewm-smoothed DX
ready       = positional length >= 30                        // source guard
entry_t     = (adx_t > 25) AND (plus_DI_{t−1} <= minus_DI_{t−1}) AND (plus_DI_t > minus_DI_t) AND ready
exit_t      = (adx_t < 25) OR ((minus_DI_{t−1} <= plus_DI_{t−1}) AND (minus_DI_t > plus_DI_t))
```

- Trade events: `entry_signal` on a fresh +DI-over-−DI edge under ADX strength; `direction` long-only; `exit_signal` on ADX weakness or a fresh −DI-over-+DI edge. Both cross legs are one-bar edges (refires require a fresh cross back through the opposing line); the ADX leg is a level print re-evaluated per bar. A flat book enters one full unit (`0.001` BTC) on an entry bar; a long book exits the full unit on the first exit-leg bar.
- Exact boundaries (pinned semantics): strict current-bar comparisons (`>`, `<`) with setup legs (`<=`) exactly as coded — a DI touch (`plus_DI == minus_DI`) fires neither leg; `adx == 25` with no opposing cross holds the prior state (entry needs `> 25`, weakness-exit needs `< 25`). `price=round(curr_close, 4)`, `confidence`, and the `indicators={adx, plus_di, minus_di, adx_strong, atr_14}` echo are diagnostic/formatting — read by zero order-gating comparisons (fenced, never promoted).
- Mutual-exclusion proof (no tie-break pin required): entry requires `adx_t > 25` while the weakness exit requires `adx_t < 25` — jointly unsatisfiable; entry requires `plus_DI_t > minus_DI_t` while the cross exit requires `minus_DI_t > plus_DI_t` — jointly unsatisfiable. Every entry/exit pair is therefore mutex on every bar, degenerate or otherwise. Empirically confirmed this cycle: the real rule evaluated over 370 + 470 expanding-window bars on two independent synthetic tapes prints zero co-print bars. The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero `short` tokens ship anywhere and every return hardcodes `direction="long"` — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): ADX-under-25 and the fresh −DI cross are the complete position-closing set. Stop loss, take profit, ROI ladder, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, never defaulted — adverse excursions have no capital guardrail besides the eventual weakness/cross exit (disclosed principal risk). No exit leg reads net profit, fees, or funding — costs change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit (`0.001` BTC fixed base quantity), at most one open position; a positioned book treats further entry-edge bars as hold-no-ops — no pyramiding, no averaging; a flat book treats exit-leg bars as no-ops; re-entry re-arms on any qualifying fresh cross after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / open-trade reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low` (directional movement, TR, ADX) and `close` (TR plus the diagnostic price echo — the entry/exit predicates read ADX/DI only) with fixed non-positive offsets (`.diff()`, `.shift()`, `.iloc[-1]`/`iloc[-2]`, `.ewm()`, `.rolling()` — all trailing, never forward); the decision bar's own `open` and `volume` are never read (census zero). No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. The `compatible_regimes` set is class metadata read by zero signal lines.

## Required data

- OHLCV `1h` bars for `BTCUSDT` (researcher frame pin; the file declares no frame): `high`, `low`, `close` are gating inputs; `open`/`volume` are never read.
- Warmup: the source's own 30-bar positional guard is a hard floor; the ewm(14) DI smoothing and the double-smoothed scanner ADX(14) need settling margin on top. Researcher floor is 100 completed `1h` bars before the first legally possible signal — covers the source guard more than threefold. Pre-floor bars are flat by record rule; no signal may print before the floor.
- No external, cross-asset, funding, sentiment, or alternative input of any kind (census zero) — the only venue-adjacent datum is the researcher's own `BTCUSDT` spot series.

## Execution assumptions

- Pinned-engine path (verified this cycle against immutable source, not assumed): Hummingbot package `20260920`, VERSION `dev-2.17.0`, engine commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` (`HCH725/hummingbot`; verified ancestor of that repository's current HEAD this cycle): spot connector `binance` + `BinanceSpotCandles` feed (`interval` passed straight to the venue via `_get_rest_candles_params`; `"1h"` is a member of the pinned `INTERVALS` map) + `OrderExecutor` MARKET + `BacktestPositionHold` netting (`hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` at the pinned commit). MARKET executors fill at the creation row's timestamp and close (`order_executor_simulator.py`: `fill_timestamp = df['timestamp'].iloc[0]`, `entry_price = close` at that row, `POSITION_HOLD` termination) — the decision bar's own close at its effective close time, causally available. No maker-touch, queue, or intrabar-path-dependent fill.
- Decision/availability timing: signals are evaluated on completed `1h` bars only; the effective decision time is the bar's `timestamp + 3600s` (its close), and the MARKET fill lands on that same bar's close — no use of the forming bar, no next-bar dependency, no same-bar open/high/low ambiguity (predicates never read the decision bar's open; DI/ADX are settled trailing values at the close).
- Sizing/capital/costs (pinned research cost model — defined here, never punted downstream): fee `0.001`/side passed as the engine `trade_cost` and accumulated per fill as `cum_fees_quote` (order sim fee line); slippage `0.0` pinned (fills land exactly on the engine close); funding not applicable (spot has no funding leg; the file reads no funding — census zero); precision: the cited path applies no quantity or price rounding (`amount × close` floats, no lot/tick step in-path) and the configured quantity is `Q = 0.001` BTC. The simulator explicitly converts `config.amount` to binary float before multiplying by the close; binary floating-point rounding is therefore possible and exact decimal representability is not claimed. As specified above, controller-memory flat/long state, not the engine hold `is_closed` flag, governs decisions. Trade economics identity: `net = Σ realized_gross − Σ cum_fees_quote`, both primitives produced by the cited path. No hypothetical zero funding is reported as realized funding — there is no funding on spot to report.
- The file's `"leverage": 1.0` defaults entry is explicitly adopted as unleveraged spot (no margin, no liquidation leg); any leveraged reading would contradict the pinned default.

## Evidence

### Source-reported

The file ships no performance claim of any kind — no win rate, no return, no backtest table, no figure. There is therefore no source-reported number to reproduce, and none is adopted. The only source facts are the rules quoted under Provenance.

### Independently reproduced

Representative engine-primitive validation executed this cycle (2026-10-24, local pandas/numpy venv): the REAL `OrderExecutorSimulator.simulate` (AST-extracted from the pinned file at commit `8b0e067e`, unmodified — only import lines re-pointed at local stand-ins carrying identical member names/values: `TradeType` BUY=1/SELL=2, `ExecutionStrategy.MARKET="MARKET"`, `CloseType` POSITION_HOLD=10/FAILED=8/EXPIRED=4, `Decimal` amount; no behavioural stubbing), the REAL `adx_trend.py` rule running on the REAL `forven/strategies/base.py` (byte-identical blob `27508a2a…44fabf881b`), and a controller-memory flat/long state machine with the record's own `0.001` BTC / fee-0.001 pins, over a deterministic 500-bar trend-chop-reversal tape (seed 42). 50 asserts, all passing:

- guard bars (`len < 30`) print flat with `price == 0.0` and `direction == "long"`;
- both legs fire on real data (7 entries, 135 exits over 470 evaluated bars) — the rule is non-vacuous in both directions;
- zero entry/exit co-print bars (mutex holds on real data, not just by algebra);
- full rerun determinism (bit-identical entry series);
- controller memory completes 7 full round-trips (7 buys / 7 sells, balanced);
- every fill through the REAL `simulate`: `POSITION_HOLD` termination, fill price exactly the decision-bar close, per-fill fee identity `cum_fees_quote == 0.001 × 0.001 × close` holds to 1e-9;
- first round-trip economics: buy 30173.14 / sell 30406.07 → gross 0.232928, fees 0.060579, net 0.172349 (arithmetic check of the stated identity, not a profitability claim);
- 100-bar researcher floor covers the 30-bar source guard with margin.

A second independent 400-bar tape (seed 7) confirms the same shape: 6 entries, 148 exits, zero co-fires, rerun-deterministic, prefix-invariant (incremental decision at bar 200 equals the batch-tail decision). Not independently reproduced: full-history Binance `1h` backtest economics (no profitability is claimed at admission; economics are a downstream research question).

### Negative evidence

1. File-family fence, stated plainly: `forven-adx-trend-pulse-reclaim-long-flat-btcusdt-1h-2026-10-17.md` cites immutable file `builtin/adx_trend_pulse.py` (`PREBUILT-ADX-TREND-PULSE`) and fires only on a four-way conjunction of slow-EMA55 trend × ADX14≥18 × 4-bar pullback-touch × EMA21 reclaim with a close-under-EMA21 / ADX-under-gate exit. This record fires on a naked fresh +DI edge under ADX14>25 with an ADX<25-or-−DI-cross exit from immutable file `builtin/adx_trend.py` (`PREBUILT-ADX-TREND`) — different input construction × different trigger × different gate set × different exit × different source file. Neither record is the other's provenance.
2. Closest pool cousin, fenced: `freqtrade-adx-momentum-di-gated-long-flat-btcusdt-1h-2026-10-20.md` (same `1h` BTCUSDT frame) fires on a four-conjunct LEVEL state — TA-Lib ADX14>25 AND MOM14>0 AND PLUS_DI25>25 AND plus>minus — with a mirrored level-state exit plus +1% ROI and −25% stop legs. This record fires on a one-bar DI EDGE under a scanner-ewm ADX14>25 gate with weakness-or-opposing-edge exits and no stop/target of any kind — edge trigger vs level state × different indicator implementation (scanner ewm/rolling vs TA-Lib, DI period 14 vs 25) × no MOM leg × no ROI/stop × different immutable source. Not a parameter variant: the trigger/exit/risk construction differs, not the tuning.
3. Direction fence: `adx-di-cross-strength-gated-two-sided-btcusdt-1d-2026-10-12.md` is two-sided on `1d` bars from a different source. This record is long-flat only on `1h` from the pinned Forven file — different direction set × different frame × different source identity.
4. Gate-only cousins, fenced: `forven-ema-cross-adx-regime`, `forven-macd-cross-adx-regime`, `forven-keltner-adx-gated-breakout`, and `forven-williams-r-adx-gated` use ADX purely as a regime veto behind MA/MACD/band/WR triggers from different immutable files. Here the ±DI cross IS the trigger — different signal construction, never a re-tuning.
5. Open-PR fence: #331 (freqtrade AdxSmas ADX-gated SMA3/6 cross) gates a moving-average cross with ADX; #63 (SuperTrend ATR-flip), #89 (Chandelier Exit), #92 (SSL channel), #304 (Forven CCI recross), #350/#353 (BB-discount / Keltner-Donchian ratio) trade different mechanisms from different sources. None fires a ±DI-cross rule.
6. What would falsify this record: a second committed read showing the pinned file's gating lines differ (different threshold, polarity, or smoothing), or evidence that `scanner.adx`/`scanner.atr` at the pinned commit read future/non-OHLCV inputs — the committed read shows trailing-only OHLCV inputs, and the 50-assert run confirms causal behaviour.

## Falsification plan

- Re-run the committed 50-assert harness against the pinned blob (`b92a9291…`); any divergence in entry/exit bars falsifies the Signal transcription.
- Threshold sweep is NOT a falsification of this record (any ADX≠25 / period≠14 rule is a different, unpinned rule); the only admissible repair is a source-verifiable correction from the pinned file.
- Downstream (out of admission scope): full-history `BTCUSDT 1h` Hummingbot replay with the pinned cost model, checking fill/fee/equity accounting and event-level parity before any Qlib screening use.

## Crypto portability

Direct: the rule reads only generic OHLCV trailing windows with no equity-session, calendar, or venue-specific input; the long-only book with no short leg expresses unchanged on `BTCUSDT` spot (no borrow, no funding, no expiry). The `"leverage": 1.0` hint is adopted as unleveraged spot, so no margin-call or liquidation semantics are required. Precision/lot/tick behaviour is the pinned path's (none in-path); a live venue's lot filter would be a deployment concern, never an admission fact. No portability claim is made for leveraged, short-enabled, or derivatives venues.

## Limitations

- No capital guardrail: adverse excursions have no stop/target/trailing/time exit — the eventual ADX-collapse or opposing-cross exit is the only protection (disclosed principal risk; explicitly disabled legs, never defaults).
- Whipsaw regime: alternating shallow DI crosses under strong ADX re-enter immediately after every exit (no cooldown) — chop bleeds fees at 0.001/side per fill with no veto.
- Lag: double-smoothed ADX(14) plus ewm(14) DI legs delay both entries and exits around V-turns; recoveries print strictly after cross-plus-strength reclaim.
- Warmup sensitivity: the first ~100 `1h` bars are flat by record rule; ewm-seeding differences across engines could shift the earliest post-floor signals by a bar (later signals are settled; determinism was verified within one fixed implementation).
- Single-market, single-frame: `BTCUSDT` spot `1h` only; any other market/frame is an unpinned rule.
- Researcher pins (market spelling, frame, 0.001 BTC size, MARKET same-close fills, fee 0.001/side, slippage 0) are disclosed derivations, not source facts; economics change the performance report, never signal firing.

## Implementation status

`not-implemented`: no dedicated Qlib executable recipe/artifact, no Hummingbot controller deployment, no Paper/Testnet/Live run exists for this record. The 50-assert harness above is representative engine-primitive evidence (real rule + real simulator method + stand-in datatypes), not a production implementation. If this record is formally selected for execution, the route is `IMPLEMENTATION_NEEDED` (minimal strategy-specific implementation, then the same downstream research flow without redoing HB_READY).

## Adoption boundary

`not-approved`, `research-only`. This PASS record admits the declared derived strategy to model-consistent downstream research only. It is not a profitability finding, not Qlib parity, not Testnet/Mainnet authorization, and not evidence that the original Forven source strategy itself passes. No live, Paper, Testnet, or trading action is authorized by this record.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/0e35d7dd3f84a8ef6d8d7a3b131ff366585a451e/forven/strategies/builtin/adx_trend.py (immutable primary source; all rule citations)
- https://github.com/judder659/Forven (repository home)
