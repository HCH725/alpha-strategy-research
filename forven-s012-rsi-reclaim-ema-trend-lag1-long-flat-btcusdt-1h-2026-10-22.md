---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven S012-BTC RSI-reclaim EMA50/200 trend lag-1 position-executor long-flat on BTCUSDT 1h bars
created: 2026-10-22
updated: 2026-10-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-21
sources:
  - https://github.com/judder659/Forven/blob/0a8b07fd02ac6864c0102fec08b6ae7ebfa32875/forven/strategies/builtin/rsi_momentum.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven S012-BTC RSI-reclaim EMA50/200 trend lag-1 position-executor long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source Forven systematic strategy library).
- Pinned commit SHA: `0a8b07fd02ac6864c0102fec08b6ae7ebfa32875` (committed `2026-10-21T13:26:22Z`; record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/rsi_momentum.py`.
- GitHub blob SHA at the pinned commit: `f66f0905c5c32b5850a3261fed69c03915bfcc89`, size 5272 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 5272 bytes, 149 lines, SHA-256 `09befeece1ece8817a8ebaf21e6f915f1b5f263bef3aee4970774732648a6d72`, and `git hash-object` reproduces `f66f0905c…03915bfcc89` — the entire file was retrieved and inspected.
- Registration: the file's `STRATEGIES` roster pins `("S012-BTC", RSIMomentumStrategy, {"_asset": "BTC"})` — the ONLY override is the `_asset` label; every numeric rule literal is the file's `default_params`. `TYPE_NAME = "rsi_momentum"`, class `RSIMomentumStrategy(BaseStrategy)`. Sibling roster entries `S012-ETH` / `S012-SOL` differ only in the `_asset` label with identical numerics — this record pins ONLY the BTC registration's market mapping below, and no reviewer repair may substitute a sibling label, file, or constant.
- The file's own words (quoted for gate evidence, never extended): `default_params` = `{"rsi_period": 14, "rsi_entry": 40, "rsi_exit": 60, "ema_fast": 50, "ema_slow": 200, "adx_period": 14, "adx_min": 0, "leverage": 3.0}`; `generate_signals` docstring: "Entry: RSI crosses up through the oversold threshold while price is above both EMAs and ADX clears its floor. Exit: RSI crosses down through the overbought threshold."; coded legs `entry = (prev_rsi < oversold) & (rsi_val >= oversold) & trend_ok & adx_ok` with `trend_ok = (close > ema_fast) & (close > ema_slow)` and `adx_ok = adx_val >= p["adx_min"]`; `exit_ = (prev_rsi >= overbought) & (rsi_val < overbought)`; both columns `fillna(False)`; `generate_signal` returns `direction="long"` hardcoded. No stoploss, no ROI ladder, no trailing, no time exit, no short column ships anywhere in the signal path.
- Indicator lineage pinned (all resolved, all deterministic): `generate_signals` imports `rsi, adx` from `forven.strategies.indicators`, which exposes them lazily via module `__getattr__` (`_FACADE_NAMES`, blob `fdda8b77429e133372482e25cdff8ea31bd59b2a`, 35784 bytes) re-exported from their canonical home in `forven/scanner.py` (blob `78ab0403ac2fa46f700f206957f49f049a4a22ad`, 472181 bytes). Scanner `rsi` (lines 1917–1930): Wilder RMA — `delta.clip(lower=0).ewm(alpha=1.0/n, adjust=False, min_periods=n)`, mirrored loss leg, `100-(100/(1+rs))` with `loss.clip(lower=1e-9)`; first valid print at index 14 for period 14 (diff-NaN bar plus 13 bars short of `min_periods`), verified by execution this cycle. Scanner `adx` (lines 1932–1947): Wilder-style directional movement on `high`/`low`/`close` with `ewm(span=period, adjust=False)` smoothing, `1e-9` denominator clips; single NaN at index 0, valid and non-negative from index 1 on, verified by execution this cycle. EMAs are inline `close.ewm(span, adjust=False).mean()` (spans 50/200, seeded from bar 0, never NaN). No DB, no network, no enrichment call, no order-flow stream in the signal path (`generate_signals` reads `df["close"]`/`df["high"]`/`df["low"]` only).
- Full-file token census (verified over the 149 lines this cycle): 0 `short` (case-insensitive — no short leg anywhere); 0 `volume`; 0 `resample` / 0 `informative` / 0 `request` / 0 `security`; 0 `stoploss` / 0 `minimal_roi` / 0 `trailing` / 0 `take_profit` / 0 `time_limit` (no risk leg of any kind ships — the position-closing set is the signal exit alone); 0 `position_adjustment` / 0 `cooldown` / 0 `pyramid`; `leverage` exactly once (the `3.0` default-params literal, scoped out below — never read by any signal line); `parameter_space` (an optimization grid, never read by `generate_signals`); `compatible_regimes = {"TREND_UP"}` (scanner-universe metadata, never read by `generate_signals`); `confidence` / `atr_14` / `price` rounding (per-bar display plumbing inside `generate_signal`, never gating). `generate_signal` delegates its booleans to `generate_signals` ("Single source of truth … keeps per-bar and vectorized in lockstep", lines 104–105) — one rule, quoted twice, never two rules.
- Prior-submission disclosure: Scout PR #361 specified this same source file but was closed NOT_LOSSLESS on two engine-path blockers (open-time timestamp/causality mapping; POSITION_HOLD fee accounting). This record re-verifies the identical source rules (same pin, same bytes) and re-specifies execution from scratch on the PositionExecutor-plus-controller-stop path with line-pinned code evidence; it adopts no finding by reference and re-proves every gate below.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Forven deployment. The source pins the S012-BTC registration, the RSI-14 reclaim-40 entry with EMA50/200 trend and ADX14 floor, the RSI-60 rollover exit, the long-only posture, and the Wilder/RMA indicator lineage — but ships no venue spelling, no fill-timing flag, no warmup guard, no sizing rule, and no risk leg. Researcher-declared adaptations are exactly five: (1) research market BTCUSDT on Binance spot (the scanner's own enrich convention implies `{asset}/USDT` spelling; venue normalization is the only market step, and no source-market equivalence is claimed); (2) lag-1 completed-bar decisions with decision-row-close MARKET fills on the pinned PositionExecutor path (the source evaluates signal-bar booleans; decision/execution timing is the researcher binding, disclosed, never presented as the source engine's own timing); (3) fixed 0.01 BTC base-amount sizing at leverage 1, unlevered (the source `leverage: 3.0` default is scoped out — it never enters the signal path and this version models no leverage anywhere); (4) a 250-bar researcher warmup pin held flat (the file carries no warmup guard — disclosed, never presented as source-native behaviour); (5) absent source economics ride an explicit fixed cost model (`trade_cost = 0.001` per side; spot structurally has no funding — stated as structural absence, never as realized zero funding). The house BO 6% + SO 6% + SO 6% overlay is explicitly EXCLUDED from this admission version (downstream experiment only — see Execution assumptions E8). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-22): working-tree searches for `S012-BTC` and `builtin/rsi_momentum.py` return zero strategy records — no pool record cites this source file or registration (the two `rsi_momentum`-mentioning pool files pin the DIFFERENT files `rsi_momentum_s00139.py` and `rsi_boundary_rejection.py`, fenced in Negative evidence 8). No open `research/*` PR (#48, #49, #63, #89, #92, #251, #304 Forven CCI oversold-recross, #331 AdxSmas, #350 ClucMay72018, #353 Heracles) touches this file, registration, or an RSI-reclaim-plus-dual-EMA-plus-ADX-floor conjunction. Closed Scout PRs #360 (Forven supertrend), #361 (this file's prior engine spec), #362 (Forven ORB) are not open and merge nothing. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the single bar where 14-period Wilder RSI crosses up through 40 while that bar's close stands above both its 50- and 200-bar EMAs and 14-period ADX reads at or above its floor (0); sell the single bar where RSI crosses down through 60. The file ships no sample, window, trade count, stop, profit target, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Reclaim-plus-trend machine, long-only, signal-in/signal-out with no risk legs. The RSI-reclaim leg supplies the timing (a washout that turns on this exact bar) while the dual-EMA leg vetoes reclaims printed beneath a weak tape — so an RSI turn from below 40 without both trend filters prints nothing, and an above-trend bar without the reclaim prints nothing either. The ADX floor at 0 is coded but always true (verified: ADX non-negative wherever valid) — an inert conjunct kept verbatim, never deleted, never counted as a live gate. The exit is deliberately asymmetric and ungated: any RSI rollover through 60 closes the book with no trend or ADX condition — the system is strict to enter and unconditional to leave. Unlike persistent-state records (trade every qualifying bar), each leg fires at most on its crossing bar — a positioned book treats further entry bars as hold-no-ops until a qualifying exit bar. There is deliberately no stop, no profit target, no trailing, no time exit: a position whose RSI never rolls over is held to the end of data (disclosed tail, see Limitations).

## Signal

Exact rule as pinned (any other RSI/EMA/ADX period, threshold, strictness, edge-vs-state pairing, frame, or book is a different, unpinned rule). All identifiers below are the program's own:

```text
rsi[t]      = Wilder RMA RSI(close, 14)   // scanner lines 1917-1930; min_periods=14; first valid index 14
ema50[t]    = close.ewm(span=50, adjust=False).mean()    // seeded bar 0, never NaN
ema200[t]   = close.ewm(span=200, adjust=False).mean()   // seeded bar 0, never NaN
adx[t]      = scanner ADX(high, low, close, 14)          // lines 1932-1947; NaN only at index 0; >= 0 after
SRC_ENTRY[t] = (rsi[t-1] < 40) AND (rsi[t] >= 40) AND (close[t] > ema50[t]) AND (close[t] > ema200[t]) AND (adx[t] >= 0)
SRC_EXIT[t]  = (rsi[t-1] >= 60) AND (rsi[t] < 60)
ENTRY_D[i]   = SRC_ENTRY[i-1]   // lag-1 decision binding (see Execution E3)
EXIT_D[i]    = SRC_EXIT[i-1]    // lag-1 decision binding
floor        = leading-window bars: NaN comparisons false + fillna(False); 250-bar record-rule flat (see Required data)
```

- Trade events: `ENTRY_D = 1` on the first decision row after a bar printing the reclaim-plus-trend conjunction, `direction` long-only; `EXIT_D = 1` on the first decision row after a bar printing the RSI rollover. Each print is a one-bar edge, not a persistent state — a positioned book treats non-exit rows (including further entry edges) as hold-no-ops under the position pin below.
- Exact boundaries (pinned semantics): entry strict on previous RSI (`< 40`), inclusive on current RSI (`>= 40`), strict on both trend legs (`close > ema`, equality holds nothing); exit inclusive on previous RSI (`>= 60`), strict on current (`< 60`); ADX inclusive (`>= 0`, inert-true wherever valid). A bar with `rsi == 40` on both sides fires neither entry conjunct on the strict leg; a bar with `rsi == 60` exactly satisfies the exit previous-bar leg. All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required, executed this cycle on 600 synthetic bars): any entry bar has `rsi[t-1] < 40` while any exit bar has `rsi[t-1] >= 60` — mutually exclusive on every bar, degenerate or otherwise, so `SRC_ENTRY` and `SRC_EXIT` never co-print; the lag-1 shift preserves exclusion (`ENTRY_D`/`EXIT_D` never co-print either, asserted). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere and `generate_signal` hardcodes `direction="long"` — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the signal exit is the ONLY position-closing leg. No stop, no ROI ladder, no trailing, no time exit ships anywhere — explicitly none further, not invented. The inert 0-floor ADX conjunct is not a risk leg.
- Position rule (predeclared researcher pin, consistent with the source's single-position scanner posture): single-unit, at most one open position per market; a positioned book treats further entry edges as hold-no-ops (no pyramiding, no averaging — no such hook ships anywhere); a flat book treats exit legs as no-ops; re-entry re-arms on any qualifying lag-1 entry decision after any close (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup rows are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `close`/`high`/`low` (Wilder RMA plus EMA recursions with fixed non-negative offsets, plus the one-bar reclaim/rollover lookback) with no forward reference; seed rows degrade to False/0-hold and `fillna(False)` pins both columns boolean — no leg can fire early. No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, enrichment, or stop/limit order argument anywhere in the gating path. `parameter_space`, `compatible_regimes`, `confidence`, `atr_14`, and price rounding are display/optimization metadata, never gating (fenced in Negative evidence).

## Required data

- Completed `1h` bars of BTCUSDT: `close` (RSI, both EMAs, both reclaim/rollover comparisons), `high`/`low` (ADX directional movement only). No `open` read, no bar `volume` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (researcher frame pin — the file names no timeframe; `1h` rides existing admission precedent on `main` via the ADXMomentum, AwesomeMacd, and BbandRsi records, and the lag-1/causality proof below is frame-agnostic). One evaluation per completed bar; every window reads the decision row's causal past only (plus the one-bar reclaim/rollover lookback and the one-row decision lag); fills land on the decision row's own close under the derived binding below.
- Warmup (researcher pin, disclosed): the first 250 one-hour bars held flat. Covers the Wilder RSI seed (first valid index 14, executed), the single-bar ADX seed NaN, and the 200-span EMA transient with margin. The file ships no warmup guard — quoted absence, never filled in from elsewhere. Coded behaviour underneath: NaN comparisons are False and both columns are `fillna(False)` — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- E1 — Pinned engine (no sibling-precedent substitution): Hummingbot package `20260920`, VERSION `dev-2.17.0`, source commit `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (committed `2026-09-20T12:10:22Z`). Every file/line cited below was read at that immutable commit: `strategy_v2/backtesting/executors_simulator/position_executor_simulator.py` (blob `5539f0d2…1396c943`, 88 lines), `strategy_v2/backtesting/backtesting_engine_base.py` (blob `7d1e552d…1106e`, 727 lines), `strategy_v2/backtesting/executor_simulator_base.py` (blob `f77fc610…1222a`), `strategy_v2/executors/position_executor/data_types.py` (blob `32bf8313…1a515af`), `data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` (blob `5d0c938a…ae4dd`, 3924 bytes).
- E2 — Feed timestamps and causal availability (Gates 5/6, stated plainly): the spot candles parser keeps `row[0]` — the Binance kline OPEN time — as the row timestamp (candles file lines 80–85); `prepare_market_data` backward-merges features onto `timestamp_bt` and sets `timestamp = timestamp_bt` (engine-base lines 455–480); `update_state` publishes provider price `close_bt` at that row timestamp (lines 364–367). Therefore a same-row read of row `i`'s own final `close` at row `i`'s timestamp (its OPEN time) would be a forward read — this record never does that. The lag-1 binding (E3) reads only rows `<= i-1`, every one of them a completed bar at row `i`'s timestamp. Availability is proved from the cited parser lines, never asserted as "availability equals row time".
- E3 — Decision binding (derived, disclosed): `ENTRY_D[i] = SRC_ENTRY[i-1]`, `EXIT_D[i] = SRC_EXIT[i-1]` for all rows `i` past the 250-bar floor; rows without a predecessor signal row decide nothing. A reclaim/rollover bar's signal is therefore acted on at the next row, using only completed-bar prints.
- E4 — Entry action (exact config, no `None` fills): on a row `i` with `ENTRY_D[i] = 1` and a flat book, the binding emits the equivalent of a `CreateExecutorAction` carrying `PositionExecutorConfig(connector_name="binance", trading_pair="BTCUSDT" (venue spelling normalized to the connector pair format as pure plumbing), side=BUY, amount=Decimal("0.01") (FIXED base amount, known at submit — never a notional-divided quantity), entry_price=Decimal(str(close[i-1])) (mechanical placeholder satisfying the simulator's unconditional `float(config.entry_price)` at simulator line 35; the EFFECTIVE fill is the decision-row close per simulator line 40 — both stated, the placeholder is never presented as the fill), timestamp=row-`i` timestamp, leverage=1, triple_barrier_config={open_order_type=MARKET, take_profit=None, stop_loss=None, trailing_stop=None, time_limit=None})`. The config validators it must satisfy are quoted from the pinned types file: positive amount, positive entry price, directional side, leverage ≥ 1 (lines 76–99). Simulation follows the engine's own calling convention — `simulate_executor(config, processed_features.loc[i:max_ts], trade_cost)` (engine-base lines 282–289, 482–499) with `trade_cost = 0.001`. MARKET open starts at the decision row (simulator lines 11–15); the effective entry price is `df.loc[start_timestamp, 'close']`, i.e. close[`i`] (simulator line 40). No maker-touch, queue, or intrabar-path-dependent fill is claimed: the fill lands at the decision row's close by simulator mechanics — one bar after the signal bar's close — disclosed as the research-model fill timing, not as a live-trading claim.
- E5 — Open-position economics (exact formulas, unlevered, fee-included): from simulator lines 43–49, for a BUY opened at row `i` with fill `C[i]`: `net_pnl_pct[t] = (C[t]/C[i] − 1) − 2×0.001` for every row `t ≥ i`; `filled_amount_quote = 0.01 × C[i]`; `net_pnl_quote[t] = net_pnl_pct[t] × filled_amount_quote`; `cum_fees_quote = 2×0.001×filled_amount_quote`. The simulator has NO leverage term anywhere in its 88 lines — with `leverage=1` the math is unlevered price return net of both-side fees, and any 3x/5x reading would contradict the cited code. With all barriers `None`, `tl_timestamp` falls back to the last row (simulator line 26): an unexited position rides to the end of data and closes TIME_LIMIT — disclosed tail, never a live-hold claim.
- E6 — Signal-exit action (fee-consistent, POSITION_HOLD never touched): on a row `j` with `EXIT_D[j] = 1` and a position open, the binding emits the equivalent of a `StopExecutorAction(executor_id, keep_position=False)` at row `j`'s timestamp. Pinned mechanics (engine-base lines 580–599): the executor info is read at that timestamp — whose `net_pnl_quote`/`cum_fees_quote` are the simulation row values (base-simulator lines 29–56) — then with `keep_position=False` the close type is EARLY_STOP (never POSITION_HOLD) and `_executor_realized_pnl += net_pnl_quote` books the fee-included close-to-close PnL immediately; `summarize_results` sums exactly the non-hold executors' `net_pnl_quote` into `executor_pnl` and reports `cum_fees_quote` separately (lines 602–624). No gross-PnL/fee-split accounting gap: fees are inside every booked number by construction (E5), and the hold ledger is never entered. Realized exit economics for an entry at row `i`, exit at row `j`: `net_quote = ((C[j]/C[i] − 1) − 0.002) × 0.01 × C[i]`.
- E7 — ROI/stop-return basis (explicit, no reviewer choice): there are no ROI/stop barriers in this version, so no basis ambiguity exists beyond E5–E6: every booked number is unlevered close-to-close price return minus `2×0.001`, computed on a fixed 0.01 BTC base. Costs are an explicit fixed research model: `0.001` per side keyed to the Binance spot regular taker schedule; slippage 0 (modeled, disclosed); funding structurally absent on a spot venue (stated as structural absence, never as realized zero funding). Nothing is left "to be pinned downstream".
- E8 — House-overlay exclusion (no DCA contradiction): this admission version trades single fixed-base-amount legs with no Safety Orders, no averaging, no leverage, and no shared-capital contention — at most one open executor per market (E4 single-unit pin). The house BO 6% + SO 6% + SO 6% / Isolated 3x/5x campaign overlay is a downstream experiment, explicitly NOT part of this version's trade events; if it is ever applied, that evaluation is a separately declared derivative, never this record.
- E9 — Quantization (code-verified absence, disclosed): the PositionExecutor path applies no lot-size quantization — `config.amount` flows directly into `filled_amount_quote` (simulator line 47); the only quantization hook in the engine file (`get_trading_rules`) belongs to the GridExecutor branch (engine-base lines 501–507), which this record never invokes. Amount 0.01 is exactly representable; exchange minimum/precision conformance is scoped out as a disclosed research-model limitation, never claimed as proven.
- E10 — Controller scope (no invented machinery): no named controller class is assumed. The complete execution binding is E3 (deterministic decision columns) + E4 (exact config construction) + E5–E6 (pinned simulator/accounting lines) + E8 (single-unit state) — reproducible call-for-call against the pinned package following the engine's own per-row action loop (engine-base lines 282–289). Anything beyond that loop (live order books, queue positions, rest limits) is out of scope, disclosed.

## Evidence

### Source-reported

The file ships the full construction (149 lines: S012-BTC registration with defaults, the `generate_signals` twin with both conjunct legs and `fillna(False)`, the `direction="long"` posture, the Wilder/RMA indicator lineage, and the absence of every risk leg). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Logic asserts executed this cycle against the pinned formulas (600-bar synthetic tape, dependency-free): mutual exclusion of `SRC_ENTRY`/`SRC_EXIT` on every bar; lag-1 exclusion of `ENTRY_D`/`EXIT_D`; RSI first-valid index 14; ADX single-NaN-at-0 then non-negative; no entry possible before the RSI seed. All asserts passed. No performance backtest was run and none is claimed.

### Negative evidence

1. Leading-window behaviour fenced: RSI NaN through index 13, ADX NaN at index 0, EMAs seeded-but-transient — all compare False / `fillna(False)`; the 250-bar record-rule floor additionally holds every pre-seed row flat. The file ships no warmup guard, so the floor is purely a researcher pin, never misattributed.
2. Inert-gate fence: `adx_min = 0` with a provably non-negative ADX makes `adx_ok` always true wherever valid — kept verbatim as coded, never deleted, never counted as a live filter. Removing it would be a different, unpinned rule.
3. Leverage fence: the `3.0` default literal never enters any signal line — this unlevered spot version scopes it out by predeclared derivation (E4/E5), never by silent redefinition.
4. Non-gating metadata fence: `parameter_space` (optimization grid), `compatible_regimes` (universe label), `confidence`/`atr_14`/price rounding (display plumbing) — none is read by `generate_signals`; treating any of them as a gate would be a different, unpinned rule.
5. Trailing-signal fence: a reclaim/rollover bar printed on the final data row has no following decision row and is untradable — fenced, never filled by assumption.
6. Held-to-end fence: with no risk legs, a position whose RSI never rolls over rides to the last row and closes TIME_LIMIT at the final close — the coded posture of this binding, disclosed as its principal risk (see Limitations).
7. Placeholder fence: `entry_price = close[i-1]` exists only to satisfy the simulator's unconditional `float()` (line 35); the effective fill is the decision-row close (line 40). Presenting the placeholder as the fill would misread the cited code — disclosed here.
8. Cousin-file fence: `rsi_momentum_s00139.py`, `rsi_boundary_rejection.py`, `supertrend.py`, `orb.py`, and every other file under `forven/strategies/builtin/` at the pinned commit are separate pins — their constants, legs, exits, and risk pairs must never be substituted into this record. Pool records touching RSI/EMA/ADX in other constructions (naked crosses, CCI conjunctions, single-EMA states) trade different conjunctions with different strictness — none trades this file's reclaim-plus-dual-trend-plus-floor conjunction with this asymmetric ungated exit.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT spot market choice, the lag-1 decision binding with decision-row-close MARKET fills, the fixed 0.01 BTC base amount at leverage 1, the 250-bar warmup floor, the fixed `0.001`/side cost model with structural spot no-funding, and the PositionExecutor-plus-controller-stop execution binding — all predeclared above. The S012-BTC numerics, the reclaim/rollover legs with all strictness, the Wilder/RMA lineage, the long-only posture, and the signal-exit-only closing set are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: RSI(14) Wilder / EMA(50,200) / ADX(14, floor 0) / reclaim-40 plus dual-trend conjunction / rollover-60 exit with pinned strictness / one-bar-edge legs / lag-1 binding / single-unit long-only / `1h` BTCUSDT spot / decision-row-close fills / fixed 0.01 base / `0.001` costs are frozen.

- F1 — Trend-gate relevance: dropping both EMA legs (naked RSI-reclaim entry with the inert ADX conjunct kept, same exit) must not improve net expectancy; fail ⇒ the dual-trend veto adds nothing over reclaim timing.
- F2 — Exit-asymmetry relevance: gating the exit with the same dual-trend condition as entry (exit only on rollover bars that also satisfy the trend pair, same entries otherwise) must not improve net expectancy; fail ⇒ the coded unconditional-exit asymmetry adds nothing over its symmetric twin.
- F3 — Threshold relevance: widening entry to reclaim-45 / exit to rollover-65 (same construction otherwise) must not improve net expectancy; fail ⇒ the coded 40/60 geometry adds nothing over its neighbour thresholds.

## Crypto portability

BTCUSDT Binance spot `1h` is the research pin (the scanner's own `{asset}/USDT` enrich convention supports the BTC→BTCUSDT spelling; venue normalization is plumbing). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting and no margin. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. No volume field is consumed at all. No funding leg exists on a spot venue — structural, disclosed.

## Limitations

- Derived fill timing: the source evaluates signal-bar booleans with no execution statement; this record decides at the next row and fills at that row's close (one bar after the signal bar's close) by pinned simulator mechanics. Backtest economics of the timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about any other timing's performance. Any live/limit-order/queue behaviour is out of scope.
- Derived market pin: the file names no symbol or venue beyond the `_asset` label — BTCUSDT on Binance spot is a researcher market choice, never a source claim.
- No risk legs: there is no stop, profit target, trailing, or time exit — a leg whose RSI never rolls over is held to the end of data (bounded only by the data window); a winning leg keeps running with no profit-taking leg. This is the binding's posture, disclosed as its principal risk.
- Held-to-end tail: never-exited positions close TIME_LIMIT at the final close by simulator fallback (line 26) — a data-window artefact, not an economic exit, disclosed.
- Unquantized research model: the pinned path applies no lot-size quantization (code-verified absence); exchange minimum/precision conformance is scoped out, disclosed.
- Source leverage excluded: the file's `3.0` default plays no role in this unlevered version — a levered evaluation would be a separately declared derivative.
- House overlay excluded: BO/SO sizing, isolated margin, and 3x/5x leverage are downstream-only and form no part of this version's events.
- Seed rows: the RSI 14-bar seed plus EMA transient dominate early bars; the first 250 `1h` bars are flat by record rule, so early-history signals never enter any evaluation.
- Framework defaults: none assumed — every simulator/validator behaviour cited above is a pinned file line, not a default.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/judder659/Forven/blob/0a8b07fd02ac6864c0102fec08b6ae7ebfa32875/forven/strategies/builtin/rsi_momentum.py
- https://github.com/judder659/Forven
