---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven SuperTrend 10-3.0 flip-state long-flat on BTCUSDT 1d bars
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
  - https://github.com/judder659/Forven/blob/0e35d7dd3f84a8ef6d8d7a3b131ff366585a451e/forven/strategies/builtin/supertrend.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven SuperTrend 10-3.0 flip-state long-flat on BTCUSDT 1d bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the fifty-three admitted Forven records, including the `forven-awesome-oscillator-zero-cross` and `forven-ichimoku-tenkan-kijun-cross-cloud-gated` siblings admitted 2026-10-24 that pin the identical base-class blob below).
- Pinned commit SHA: `0e35d7dd3f84a8ef6d8d7a3b131ff366585a451e` (verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/supertrend.py`.
- GitHub blob SHA at the pinned commit: `9cd80b4057299acad92a52c9fbee6752c37c20e7`, size 2970 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 2970 bytes, 74 lines, SHA-256 `b20e5bcde7d1f679a3d79ec9d5b5e2c48ce273d2d47b21e542e1f6756f138ab2`, identical to the GitHub blob (`git hash-object` reproduces `9cd80b40…37c20e7`) — the entire file was retrieved and inspected.
- Registration: the file defines class `SuperTrendStrategy(BaseStrategy)` (the only class in the file) with `TYPE_NAME = "supertrend"` and a one-row roster `STRATEGIES = [("TOMB-SUPERTREND", SuperTrendStrategy, {"_asset": "BTC"})]` — venue spelling is the bare `"BTC"` asset label only, no timeframe override. Identity here is class plus file path plus `TYPE_NAME`, all unique.
- The file's own words (quoted for gate evidence, never extended): module docstring `SuperTrend strategy.`; `describe()` returns `Buys when price crosses above SuperTrend (atr_period, multiplier), sells when crosses below.`; `default_params` returns exactly `{ "atr_period": 10, "multiplier": 3.0, "leverage": 3.0 }`; the vectorized twin (`generate_signals`, docstring: `the SINGLE source of entry/exit logic`) calls `compute_indicator(df, {"id": "st", "kind": "supertrend", "params": {"length": atr_period, "mult": multiplier}})`, reads `direction = out["st_dir"]`, `prev_dir = direction.shift(1)`, and returns `entry = (prev_dir < 0) & (direction > 0)`, `exit_ = (prev_dir > 0) & (direction < 0)`, both `fillna(False)`; the per-bar path imports `atr` for the indicators echo only, reads `curr_close = float(close.iloc[-1])`, delegates gating to `entries, exits = self.generate_signals(df)`, and returns `entry_signal=bool(entries.iloc[-1])`, `exit_signal=bool(exits.iloc[-1])`, `price=round(curr_close, 4)`, `direction="long"`, `confidence=1.0`, `indicators={"atr": ...}`. No performance phrase of any kind ships anywhere in the 74 lines.
- Indicator provenance (verified this cycle, never assumed): `forven/strategies/indicators.py` at the same pinned commit (35784 bytes, blob `fdda8b77429e133372482e25cdff8ea31bd59b2a` — byte-verified via download plus `git hash-object`) defines `_f_supertrend` (Wilder-ATR final-band trend state machine over `high`/`low`/`close` only, forward loop `k` reading `close[k]`, `close[k-1]`, current basic bands and prior final bands — no future reference), `_atr_wilder` (RMA of true range), and the `compute_indicator` dispatcher resolving `kind: supertrend` through the indicator REGISTRY. The twin's `{"length": atr_period, "mult": multiplier}` spec resolves to exactly this implementation with pinned `10 / 3.0`. The per-bar `atr` import resolves through the module's PEP 562 lazy facade to the same canonical Wilder helper and feeds the indicators echo only (fenced, never promoted).
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (12238 bytes, blob `27508a2a6b8c546e21adefdb97fc0144fabf881b` — byte-identical to the blob pinned by the admitted AO/Ichimoku siblings) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults and `direction: str = "long"` default, and `BaseStrategy.__init__(strategy_id, params)` merging `{**default_params, **params}`. The file's explicit `direction="long"` return needs no default reading.
- Full-file token census (verified over the 74 lines this cycle): `def generate_signals` once plus `def generate_signal` once (per-bar path delegates its gating lines to the twin — a single shared edge, no second rule); 0 `short` (no short leg, no short identifier anywhere — the English word `sells` in the describe prose means exit-to-flat, fenced); 0 `open` / 0 `volume` (sole `df` reads are `close` directly and `high`/`low`/`close` inside the indicator); 0 `funding` / 0 `mark_price`; 0 `request` / 0 `security`; 0 `resample` / 0 `informative`; 0 `hyperopt` (the single case-insensitive `parameter` hit is the `parameter_space` def line only — a grid menu, never a signal input); 0 `trailing` / 0 `stoploss` / 0 `startup`; 0 `order_types`; 0 `pyramid` / 0 `position_` / 0 `cooldown` / 0 `max_open_trades` (the position pin below is a predeclared researcher rule, never a file semantic); 0 `timeframe` / 0 `data_requirements` (the file declares no frame — the `1d` pin below is a disclosed researcher choice); 1 `shift` (`direction.shift(1)` — a one-bar lag, never a forward reference); 2 `fillna` (the twin's `entry.fillna(False)` / `exit_.fillna(False)`); 0 `ffill` / 0 `interpolate` / 0 `dropna` / 0 `merge` / 0 `can_short` / 0 `nan_to_num`; 5 `direction` (four local state-machine variable uses plus the single `direction="long"` return); the single `leverage` token is the `"leverage": 3.0` defaults entry — an unadopted leverage hint explicitly replaced by unleveraged spot below (see Execution assumptions).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Forven deployment. The source pins the 10/3.0 Wilder-ATR final-band construction, the flip-up entry and flip-down exit with all strictness, the long-only stance, and the no-stop posture — but ships no venue spelling beyond `"BTC"`, no frame, no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market/frame `BTCUSDT` spot `1d` (the roster names `"BTC"` and the file declares no frame; venue spelling and the `1d` decision-frame pin are disclosed, never a source claim); (2) completed-bar decisions at effective time `timestamp + 86400s` with MARKET fills at the decision bar's own close on the cited pinned-engine path (the file returns `price=round(curr_close, 4)` — the decision bar's own close; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit `0.001` BTC position pin with controller-memory state machine plus a 60-bar researcher warmup floor (covers ATR-10 seeding, the state-machine seed, and the one-bar edge with margin; see Required data); (4) the pinned research cost model below (fee 0.001/side post-hoc, slippage 0, funding not applicable on spot, no exchange lot/tick quantization in-path) replacing the absent source economics, with the file's `"leverage": 3.0` hint explicitly NOT adopted — this record is unleveraged spot, disclosed. This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-24): working-tree filename/content search for `builtin/supertrend.py`, `SuperTrendStrategy`, `TOMB-SUPERTREND`, and `TYPE_NAME = "supertrend"` returns zero strategy records citing this source file. The pool's three SuperTrend-worded neighbours are fenced in Negative evidence 6–7 (two Alorse Pine systems plus open PR #63 — different immutable sources, mechanisms, and gates). No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend ATR-flip Pine, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades the Forven final-band flip edge. Not a duplicate, paraphrase, or trivial parameter variant: a Wilder-ATR final-band direction-flip edge, long-flat, on `1d` bars from this immutable file is fenced against every trend pool-mate in Negative evidence 6–8.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar on which the SuperTrend state machine flips from down (`-1`) to up (`+1`) — price crossing above its trailing final band; stand back to flat on the bar on which the machine flips from up to down — price crossing below its trailing final band. The bands are pure trailing-bar arithmetic (Wilder ATR over true range, hl2-centred, prior-bar-gated finals) with no volatility normalization beyond the ATR itself and no regime gate. No stop, no target, no trailing, no time exit, no sizing, no cost basis ships anywhere — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Classic ATR-banded trend timer, long-only, edge-triggered, no veto. Any fresh flip-up enters, however thin the close above the final upper band, and any fresh flip-down exits, however shallow the fade below the final lower band. Unlike the pool's Pine SuperTrend siblings (flip AND-gated with RSI/StochRSI legs — veto-failed flips fire there never), flat here means only "no fresh flip printed", never "vetoed". Unlike oscillator-level systems (RSI threshold holds), there is no overbought profit-taking leg — a vertical advance is held with no exit while direction stays `+1`, and a grinding bleed is exited only at the flip-down bar with no stop to front-run it. The failure mode is plain: chop that alternates closes across the tightening bands whipsaws the book with no cooldown; a crash that gaps direction from `+1` to `-1` exits one bar later with no stop to front-run it. The 10-bar Wilder memory plus band stickiness lags every V-turn — recoveries are entered strictly after the flip prints.

## Signal

Exact rule as pinned (any other atr length, multiplier, price input, trigger polarity, frame, fill, book, or risk posture is a different, unpinned rule). `TR` is the true range, `ATR10` its Wilder RMA:

```text
TR_t    = max(high_t - low_t, |high_t - close_{t-1}|, |low_t - close_{t-1}|)
ATR10_t = RMA(TR, 10)[t]                       // Wilder smoothing, min_periods 10
basicU_t = hl2_t + 3.0 * ATR10_t   hl2_t = (high_t + low_t) / 2
basicL_t = hl2_t - 3.0 * ATR10_t
finalU_t = basicU_t if (basicU_t < finalU_{t-1} or close_{t-1} > finalU_{t-1}) else finalU_{t-1}
finalL_t = basicL_t if (basicL_t > finalL_{t-1} or close_{t-1} < finalL_{t-1}) else finalL_{t-1}
dir_t   = -1 if close_t < finalL_t (when prev +1) else +1 / +1 if close_t > finalU_t (when prev -1) else -1
          // seeded dir = -1; NaN warmup rows hold -1
entry_t = (dir_{t-1} < 0) AND (dir_t > 0)
exit_t  = (dir_{t-1} > 0) AND (dir_t < 0)
```

- Trade events: `entry_signal` on a fresh flip-up bar, `direction` long-only; `exit_signal` on a fresh flip-down bar. Both legs are one-bar state edges (refires require a fresh flip back). A flat book enters one full unit (`0.001` BTC) on an entry bar; a long book exits the full unit on the first exit-leg bar.
- Exact boundaries (pinned semantics): strict direction comparisons (`< 0`, `> 0`) exactly as coded — there is no zero direction value, so no touch ambiguity; NaN warmup rows collapse through `fillna(False)` to neutral. `price=round(curr_close, 4)`, `confidence=1.0`, and the `indicators={"atr": ...}` echo are diagnostic/formatting — read by zero order-gating comparisons (fenced, never promoted).
- Mutual-exclusion proof (no tie-break pin required): entry requires `dir_t > 0`; exit requires `dir_t < 0` — jointly unsatisfiable on every bar, degenerate or otherwise. Empirically confirmed this cycle: the real rule evaluated over a 300-bar synthetic tape prints zero co-print bars. The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero `short` tokens ship anywhere and the single return hardcodes `direction="long"` — a two-sided reading would contradict the file (`sells` in the describe prose means exit-to-flat, disclosed). The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the fresh flip-down is the sole position-ending path. Stop loss, take profit, ROI ladder, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, never defaulted — adverse excursions have no capital guardrail besides the eventual flip-down exit (disclosed principal risk). No exit leg reads net profit, fees, or funding — costs change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit (`0.001` BTC fixed base quantity), at most one open position; a positioned book treats further flip-up bars as hold-no-ops — no pyramiding, no averaging; a flat book treats flip-down bars as no-ops; re-entry re-arms on any qualifying fresh flip-up after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / open-trade reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close` (ATR/band construction plus flip comparisons) with fixed non-positive offsets (`.shift(1)` plus the state loop's `k-1` reads — lags only, no forward reference); the decision bar's own `open` and `volume` are never read (census zero). No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. The `compatible_regimes` set is class metadata read by zero signal lines.

## Required data

- Completed `1d` bars of BTCUSDT spot: `high`/`low`/`close` (ATR/band/flip construction; `close` doubles as the diagnostic price echo — the entry/exit predicate reads direction state, never a close level). No `open` read, no volume, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1d` (researcher pin, disclosed — the file declares no frame; the rule is pure bar-count logic so any fixed interval preserves the predicates; `1d` rides the `forven-naked-donchian-20` / AO / Ichimoku `1d` precedent — no novel-interval confirmation burden attaches).
- Availability mapping (pinned-engine support, not assumed): Binance spot REST kline row `timestamp` is the bar OPEN time (`binance_spot_candles.py` `_parse_rest_candles`, `row[0]`, same pinned engine commit below); the decision/fill effective time for row `t` is `timestamp_t + 86400s` (the bar's close time — exact for contiguous fixed-interval klines). At that instant every input bar `≤ t` is complete and `close_t` is the current market print: signals read no future, fills take no future — the fill is the decision bar's OWN close, never the next bar's close (whose completion lies a further 86400s ahead). Contiguity rule (deterministic data rule, disclosed): a bar whose `timestamp` does not equal the previous bar's `timestamp + 86400s` (a gap) carries no decision and no fill — the book holds its prior state across the gap; prices are never fabricated, missing bars are never interpolated.
- Warmup (researcher pin, disclosed): 60 completed `1d` bars held flat. Covers ATR-10 Wilder seeding (`min_periods=10`), the `-1` state-machine seed, and the one-bar flip edge with wide margin. Coded behaviour underneath: basic bands print NaN until seeded, direction holds `-1` through warmup, and the twin's `fillna(False)` collapses every pre-seeded edge to neutral — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization. One evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT spot, unleveraged (researcher choice — the roster names `"BTC"` only; the file's `"leverage": 3.0` defaults hint is explicitly NOT adopted and is replaced by unleveraged spot; no source-market equivalence is claimed).
- Pinned-engine path (verified this cycle against immutable source, not assumed): Hummingbot package `20260920`, VERSION `dev-2.17.0`, engine commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` (`HCH725/hummingbot`; verified ancestor of that repository's current HEAD this cycle): spot connector `binance` + `BinanceSpotCandles` feed (`interval` passed straight to the venue; `"1d"` is a member of the pinned constants `INTERVALS` map) + `OrderExecutor` MARKET + `BacktestPositionHold` netting. MARKET executors fill at the creation row's timestamp and close (`order_executor_simulator.py`: `fill_timestamp = df['timestamp'].iloc[0]`, `entry_price = close` at that row, `POSITION_HOLD` termination) — the decision bar's own close at its effective close time, causally available (`fill_price_available_at == effective_fill_time == timestamp_t + 86400s`; the next bar's close, available only at `timestamp_t + 172800s`, is never used). No maker-touch, queue, or intrabar-path-dependent fill.
- Controller state machine (derived, fully specified — no engine default is relied on for decisions): the controller keeps its own fill ledger (created BUY executor ids with base qty) with states flat/long(Q). On row `t` it evaluates the source predicates over completed bars `≤ t`; flat+flip-up creates one MARKET BUY for `Q = 0.001` BTC and records long(Q); long+flip-down creates one MARKET SELL for `Q` and records flat; long+flip-up is a hold-no-op; flat+flip-down is a no-op. Exit sizing comes from the controller's own ledger, never from engine timing. Engine `positions_held`/`executors_info` timing (including the one-row hold-conversion lag inside `update_state` and the 3600s terminated-executor view window, `DEFAULT_TERMINATED_EXECUTORS_WINDOW = 60 * 60`) never gates a decision — the design is window-independent by construction, which is exactly what the `1d` (86400s) spacing requires. A strategy-specific controller artifact itself is downstream `IMPLEMENTATION_NEEDED` work, never an admission leg; what is demonstrated here is that every required primitive exists on the cited path.
- Sizing/capital/costs (pinned research cost model — defined here, never punted downstream): fee `0.001`/side passed as the engine `trade_cost` and accumulated per fill as `cum_fees_quote` (order sim fee line); slippage `0.0` pinned (fills land exactly on the engine close); funding not applicable (spot has no funding leg; the file reads no funding — census zero); precision: the cited path applies no quantity or price rounding (`amount × close` floats, no lot/tick step in-path) and the configured quantity is `Q = 0.001` BTC. The simulator explicitly converts `config.amount` to binary float before multiplying by the close, and `ExecutorSimulation` converts the resulting float quote amounts to `Decimal`; binary floating-point rounding and tiny residual base balances after netting are therefore possible. Exact decimal representability and exact net-zero engine holds are not claimed. As specified above, controller-memory flat/long state, not the engine hold `is_closed` flag, governs decisions. Trade economics identity: `net = Σ realized_gross − Σ cum_fees_quote`, both primitives produced by the cited path (`BacktestPositionHold.add_executor` accumulates both; `get_position_summary` reports them separately). Explicitly fenced: the engine `net_pnl_quote` summary field is gross-only (it does not deduct hold fees) and `update_state total_pnl` mixes open-hold unrealized with executor realized — neither label is used here as fee-inclusive equity or closed-trade cash; economics come only from the stated identity. No hypothetical zero funding is reported as realized funding — there is no funding on spot to report.
- Leverage/margin/liquidation: none exists on the specified path — spot, unleveraged, no margin account, no liquidation branch, no forced-close state. The file's `3.0` leverage hint is explicitly not adopted and no perps/isolated-margin accounting is admitted.
- Concurrency: at most one position at any time; single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (74 lines: the `compute_indicator` twin, the one-bar flip entry/exit, the `TYPE_NAME`/roster registration, and the `{"atr_period": 10, "multiplier": 3.0, "leverage": 3.0}` defaults). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Representative engine-primitive validation executed this cycle (2026-10-24, local pandas/numpy venv): the REAL `OrderExecutorSimulator.simulate`, the REAL `BacktestPositionHold` class (AST-extracted from the pinned file, unmodified), and the REAL `supertrend.py` rule running on the REAL `forven/strategies/base.py` (byte-identical blob) with the REAL `_f_supertrend`/`_atr_wilder` arithmetic wired as the `compute_indicator(supertrend)` target — hummingbot enum/config names carried by minimal stand-ins with identical member names/values (`TradeType`, `CloseType`, `ExecutionStrategy`, `OrderExecutorConfig`, `ExecutorSimulation`, `ExecutorInfo`), no behavioural stubbing. 56 asserts, all passing:

- S1–S8 source identity (8 asserts): file 2970 bytes / 74 lines / SHA-256 pinned / `git hash-object` reproduces blob `9cd80b40…37c20e7`; `base.py` 12238 bytes reproduces sibling-pinned `27508a2a`; Forven HEAD equals the pinned commit via `git ls-remote`; engine commit is a verified ancestor of the Hummingbot HEAD.
- S9–S21 census pins (13 asserts): 0 `short`/`open`/`volume`/`funding`/`mark_price`/`request`/`security`/`resample`/`informative`/`hyperopt`/`trailing`/`stoploss`/`startup`/`order_types`/`pyramid`/`position_`/`cooldown`/`max_open_trades`/`timeframe`/`data_requirements`; exactly 1 `shift` (one-bar lag) and 2 `fillna` (entry+exit); single `leverage` token is the `"leverage": 3.0` hint; `direction="long"` only.
- R1 defaults pin (2 asserts): strategy resolves `atr_period 10 / multiplier 3.0 / leverage 3.0` under pinned defaults; roster `TOMB-SUPERTREND` / `TYPE_NAME supertrend`.
- R2–R11 rule causality (11 asserts): twin lengths exact; zero entry/exit co-print bars over the 300-bar synthetic tape (`entries=3 exits=2`); short-frame neutral on 5-bar frames; long-only on every sampled bar; prefix evaluation equals full-frame point-in-time edges on all 288 eligible prefixes (no future read by construction); per-bar `generate_signal` agrees with the twin on 12 prefixes; flat 60-bar tape holds neutral; monotonic 120-bar ramp prints exactly 1 entry edge (bounded ≤ 2); no negative shift anywhere.
- V1 MARKET-fill primitive (5 asserts): BUY `0.001` base fills at the creation row's timestamp and close, `POSITION_HOLD`, `filled_quote = amount × close` (1e-9), `cum_fees = trade_cost × quote` (1e-12), engine `net_pnl_quote` stays `0` (gross-only label, as fenced).
- V2 hold-netting primitive (5 asserts): BUY `0.001 @ 100000` then SELL `0.001 @ 110000` at cost `0.001`/side → closed (`net_base = 0`), gross `10.0` exact, `cum_fees ≈ 0.21` (1e-9), `net = gross − fees ≈ 9.79` — the stated economics identity on engine primitives.
- V3 code-evidence asserts (7 asserts): `DEFAULT_TERMINATED_EXECUTORS_WINDOW = 60 * 60` literal present; `collect_executors_ledger` present; MARKET-first-candle comment present; hold realized/fee accumulation split present; `INTERVALS` contains `1d`; REST parse uses `row[0]` open-time; engine sources read at the pinned commit. Not a performance backtest, not a deployment — a primitive capability check, exactly the once-per-new-requirement validation the contract calls for.
- V4 availability inequality (4 asserts, answers the prior-cycle timing finding directly): on the synthetic `1d` grid, `effective_fill_time == fill_price_available_at == timestamp_t + 86400s` (verified `E=1775952000`); the next bar's close is available only at `timestamp_t + 172800s`, strictly later; the simulator fill on the first real entry bar equals the decision bar's OWN close to 1e-9 (`98253.44704…`) and differs from the next bar's close — the record never takes a not-yet-completed price. Verified timeline instance: signal-bar open 2026-04-11 00:00 UTC → decision/fill 2026-04-12 00:00 UTC (close available) → next close 2026-04-13 00:00 UTC (never used).

### Negative evidence

1. Leading-window behaviour fenced: basic bands print NaN until the Wilder ATR seeds (`min_periods=10`) and direction seeds `-1`; the twin's two `fillna(False)` collapse every pre-seeded edge to neutral. The 60-bar researcher floor additionally holds all pre-seed bars flat — disclosed, not repaired.
2. Seed-direction rule fenced: direction seeds `-1`, so the first flip can only be an entry edge, never an exit — warmup bars cannot smuggle an exit through the gate; a print exactly on a band resolves through the strict `<`/`>` flip comparisons, disclosed, not smoothed.
3. `close`-level quarantine fenced: `close` enters only the band/flip construction and the diagnostic `price=round(curr_close, 4)` echo — the entry/exit predicate reads direction state, never a close level. Promoting any close level (e.g. a close-above-MA gate) into a leg would be a different, unpinned rule with different trade events.
4. Diagnostic quarantine fenced: `confidence=1.0`, `price=round(curr_close, 4)`, the `indicators={"atr": ...}` echo, and the `atr` facade import are envelope decoration read by zero order-gating comparisons; `compatible_regimes` (`TREND_UP`/`TREND_DOWN`) is class metadata read by zero signal lines; the `TOMB-SUPERTREND` roster row is an asset label, not a rule.
5. Variant menus fenced: `parameter_space()` (`atr_period` 10–20 step 5, `multiplier` 2.0–4.0 step 0.5) is a tuning grid read by zero signal lines — this record freezes canonical `10/3.0` as written; adopting any grid point would change trade events and is never claimed here.
6. Pool Pine SuperTrend siblings fenced: `alorse-supertrend-rsi50-cross-rsi72-exit-long-20261016` (Alorse Pine source with RSI50-cross entry and RSI72 exit) and `alorse-stochrsi-supertrend-ema200-long-20261016` (Alorse Pine source AND-gating SuperTrend with StochRSI and EMA200) differ on immutable source, gate (veto vs none — a veto-failed flip fires there never, while any veto-failed flip fires here), and exit construction. Neither record is the other's provenance.
7. Open Pine SuperTrend PR fenced: open `research/*` PR #63 (`SuperTrend ATR-flip trend long on BTCUSDT 1d`, Pine source) is a different immutable lineage with its own ATR-period/multiplier semantics — not this file, not this mechanism; no open PR trades the Forven final-band flip edge.
8. Pool MA/ Russell cousins fenced: `forven-dema/tema/hma-cross` and `forven-ema-cross-adx-regime` records trade price-line crossings of moving averages, never a Wilder-ATR final-band direction state machine — none evaluates `st_dir` flip edges; the pool's `forven-obv-ema-cross` cousin crosses a volume-derived line through its own average (different primitive and data). None is this construction.
9. Engine-label fences (answers to known review findings, pre-declared so no repair is ever needed): fee-inclusive cash is never claimed from `net_pnl_quote`; closed-trade equity is never claimed from `update_state total_pnl`; availability is never claimed from open-time labels without the `+86400s` mapping; fills are never claimed intrabar or from the next bar's not-yet-completed close (V4 proves the inequality); the 3600s terminated view is never relied on for position state.
10. Derivation boundary fenced: the only non-source-native behaviours are the BTCUSDT-spot-`1d` market/frame pin, the effective-time MARKET-close fills at the decision bar's own close, the single-unit/controller-memory/warmup pin, the pinned cost model with leverage `3.0` explicitly replaced by unleveraged spot, and the `+86400s`/gap data rule — all predeclared above. The 10/3.0 Wilder-ATR final-band construction, the flip-up entry and flip-down exit with all strictness, the long-only stance, and the no-stop posture are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: SuperTrend 10/3.0 final-band construction / flip-up entry and flip-down exit with pinned strictness / long-only / no-stop posture / single-unit `0.001` BTC / `1d` BTCUSDT spot / effective-time own-close fills are frozen.

- F1 — Band-width relevance: replacing the 3.0 multiplier with 2.0 (same ATR-10, same edges, same posture) must not improve net expectancy; fail ⇒ the wide 3.0 band memory adds nothing over a tighter band and the record is a label variant of one.
- F2 — Exit-leg relevance: dropping the flip-down exit entirely (entries only, never exiting — buy-and-hold from the first flip) must not improve net expectancy; fail ⇒ the exit leg carries no weight beyond decoration.
- F3 — Edge-vs-level relevance: entering on every bar with direction `+1` (level-hold instead of the prior-bar flip edge, same exit) must not improve net expectancy; fail ⇒ the flip-edge timing adds nothing over a persistent trend state.

## Crypto portability

BTCUSDT spot `1d` is the research pin (roster names `"BTC"` only). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting and no leverage. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count plus a causal state loop on the decision frame, portable across 24/7 crypto tape. Spot has no funding leg, so the funding portability question does not arise; fees/slippage ride the pinned research model, never a venue schedule claim.

## Limitations

- Late entries by construction: the Wilder ATR plus sticky final bands lag price after any V-turn, so recoveries are entered strictly after the flip prints — disclosed lag profile.
- Chop whipsaw: alternating closes across tightening bands print repeated flip-up/flip-down round trips with no cooldown and no structural filter — disclosed chop profile (3 entries / 2 exits per 300 synthetic bars shows how sparse flips are, not how profitable).
- Crash-through blindness: a bar that gaps direction from `+1` to deeply `-1` exits one bar later — there is no stop order to front-run it, disclosed.
- No risk leg: no stop loss, take profit, ROI rung, trailing-stop order, or time limit exists in source — recorded as explicitly disabled; adverse excursions have no capital guardrail besides the flip-down exit.
- Downtrend blindness: declines are watched from flat with no short participation — the zero-`short` posture is a stance choice with a return cost in sustained downtrends, disclosed.
- Single-market scope: derived pin is BTCUSDT spot `1d` only; portability to other symbols/timeframes is untested and claimed nowhere in this record.
- Research overlay dependence: fills, sizing, and costs follow the derived pins and the stated economics identity — not the source engine's own semantics, and not the engine summary labels fenced above.
- No trailing, no breakeven, no short leg, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/judder659/Forven/blob/0e35d7dd3f84a8ef6d8d7a3b131ff366585a451e/forven/strategies/builtin/supertrend.py
- https://github.com/judder659/Forven
