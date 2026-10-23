---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven naked Donchian-20 prior-band breakout long-flat on BTCUSDT 1d bars
created: 2026-10-24
updated: 2026-10-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-23
sources:
  - https://github.com/judder659/Forven/blob/81d40ebc2ca065d949f0343491b2a9cdade8b581/forven/strategies/builtin/donchian.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven naked Donchian-20 prior-band breakout long-flat on BTCUSDT 1d bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the forty-nine admitted Forven records, including the `forven-donchian-regime-breakout` sibling that pins this exact helper file).
- Pinned commit SHA: `81d40ebc2ca065d949f0343491b2a9cdade8b581` (committed `2026-10-23T17:51:51Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/donchian.py`.
- GitHub blob SHA at the pinned commit: `840b9897a7ed542f6ca131d03bd5ad22f6ca7171`, size 4226 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 4226 bytes, 131 lines, SHA-256 `277397dfe525e19882d37b4fff497b4417854a3a8546101c529b427bf7149a58`, identical to the GitHub blob (`git hash-object` reproduces `840b9897…ca7171`) — the entire file was retrieved and inspected, and the hash independently matches the SHA-256 quoted for this same file by the admitted `forven-donchian-regime-breakout` record.
- Registration: the file defines class `DonchianStrategy(BaseStrategy)` (the only class in the file) with `TYPE_NAME = "donchian"` and a one-row roster `STRATEGIES = [("SXXX-DONCHIAN-BTC", DonchianStrategy, {"_asset": "BTC"})]` — venue spelling is the bare `"BTC"` asset label only, no timeframe override. Identity here is class plus file path plus `TYPE_NAME`, all unique.
- The file's own words (quoted for gate evidence, never extended): `default_params` returns exactly `{ "period": 20, "leverage": 3.0 }`; bands are `upper = df["high"].rolling(period).max().shift(1)`, `lower = df["low"].rolling(period).min().shift(1)`, `middle = (upper + lower) / 2.0` with the helper docstring `Return prior-bar Donchian bands to avoid lookahead in both live and backtest paths`; entry is `prev_close <= upper_value and curr_close > upper_value`; exit is `prev_close >= lower_value and curr_close < lower_value`; short-frame guard `len(df) < period + 2` returns the explicit no-signal `Signal`; NaN bands return the explicit no-signal `Signal`; every return hardcodes `direction="long"`; the vectorized twin returns `(close_prev <= upper_prev) & (close > upper_prev)` and `(close_prev >= lower_prev) & (close < lower_prev)` with `.fillna(False)`. No performance phrase of any kind ships anywhere in the 131 lines.
- Param resolver pinned in-file (actually read): `resolve_donchian_period` (lines 11–20: `donchian_period` > `period` > 20, floored at 2). Under pinned defaults the resolver returns 20 deterministically — the defaults carry no `donchian_period` key. `parameter_space()` returns `{"period": (10, 40, 5)}` — a tuning grid read by zero signal lines (fenced in Negative evidence).
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (12238 bytes, blob `27508a2a6b8c546e21adefdb97fc0144fabf881b` — byte-identical to the blob pinned by four admitted Forven siblings) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults and `direction: str = "long"` default. The file's explicit `direction="long"` on every return needs no default reading.
- Full-file token census (verified over the 131 lines this cycle): `def generate_signal` exactly twice (the per-bar path and the vectorized twin — no third path); 0 `short` (no short leg, no short identifier anywhere); 0 `open` / 0 `volume` (sole `df[` reads are `close`/`high`/`low`); 0 `funding` / 0 `mark_price`; 0 `request` / 0 `security`; 0 `resample` / 0 `informative`; 0 `hyperopt` / 0 `*Parameter` import (the single case-insensitive `parameter` hit is the `parameter_space` def line only — a grid menu, never a signal input); 0 `trailing` / 0 `stoploss` / 0 `startup`; 0 `order_types`; 0 `pyramid` / 0 `position_` / 0 `cooldown` / 0 `max_open_trades` (the position pin below is a predeclared researcher rule, never a file semantic); 0 `timeframe` / 0 `data_requirements` (the file declares no frame — the `1d` pin below is a disclosed researcher choice); 0 `rsi` / 0 `stoch` / 0 `macd`; exactly 3 `shift` (the two band `shift(1)` lags plus the twin's `close.shift(1)` — fixed one-bar causal offsets, no forward reference); 2 `fillna` (the twin's two Series resolves); 3 `isna` (the explicit NaN-to-neutral guards); 6 `round` (price/indicator formatting only — never an order-gating input); 10 `middle` (helper construction plus diagnostic echo — never inside the entry/exit predicate, fenced below). The single `leverage` token is the `"leverage": 3.0` defaults entry — a framework hint explicitly not adopted (see Execution assumptions).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Forven deployment. The source pins the 20-bar prior-band construction, the prior-close-cross entry and exit, the long-only stance, the short-frame/NaN neutral guards, and the no-stop posture — but ships no venue spelling beyond `"BTC"`, no frame, no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market/frame `BTCUSDT` spot `1d` (the roster names `"BTC"` and the file declares no frame; venue spelling and the `1d` decision-frame pin are disclosed, never a source claim); (2) completed-bar decisions at effective time `timestamp + 86400s` with MARKET fills at the decision bar's own close on the cited pinned-engine path (the file returns `price=round(curr_close, 4)` — the decision bar's own close; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit `0.001` BTC position pin with controller-memory state machine plus a 60-bar researcher warmup floor (covers the source's own 22-bar guard plus the twin/guard agreement transient with margin; see Required data); (4) the pinned research cost model below (fee 0.001/side post-hoc, slippage 0, funding not applicable on spot, no rounding in-path) replacing the absent source economics, with the file's `"leverage": 3.0` hint explicitly not adopted. This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-24): working-tree filename/content search for `donchian.py`, `DonchianStrategy`, `SXXX-DONCHIAN-BTC`, and `TYPE_NAME = "donchian"` returns zero strategy records citing this source file — the admitted `forven-donchian-regime-breakout` record cites `donchian_regime.py` (a different file) and pins this file only as a supporting helper. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades a naked Donchian breakout. Not a duplicate, paraphrase, or trivial parameter variant: a naked 20/20 prior-band edge-cross, long-flat, on `1d` bars from this immutable file is fenced against every Donchian-geometry pool-mate in Negative evidence 6–10.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar whose close crosses above the highest high of the prior 20 bars; stand back to flat on the bar whose close crosses below the lowest low of the prior 20 bars. Bands are prior-bar by construction (`shift(1)`, `to avoid lookahead in both live and backtest paths`). No stop, no target, no trailing, no time exit, no sizing, no cost basis ships anywhere — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Naked Turtle-style breakout timer, long-only, edge-triggered, no veto. The 20-bar extremes are raw prior prints with no volatility normalization and no regime gate: any fresh 20-bar-high close enters, however weak the trend, and any fresh 20-bar-low close exits, however shallow the pullback. Unlike the pool's regime-gated sibling (55-bar trigger AND-gated with EMA200-plus-ADX25 — veto-failed breakouts fire there never), flat here means only "no fresh extreme printed", never "vetoed". Unlike oscillator-turn systems, there is no mean-reversion leg and no heat gauge — a vertical advance is held with no profit-taking, and a grinding bleed is exited only at the slow 20-bar low. The failure mode is plain: consecutive fresh-high closes in a ramp re-fire the entry edge bar after bar (held as no-ops under the single-unit pin — disclosed, not smoothed); chop that alternates fresh highs and fresh lows whipsaws the book with no cooldown; a crash that skips from a fresh high straight through the 20-bar low exits one bar later with no stop to front-run it.

## Signal

Exact rule as pinned (any other entry/exit length, band construction, trigger polarity, frame, fill, book, or risk posture is a different, unpinned rule). `upper_t`, `lower_t` are the pinned prior-bar bands:

```text
upper_t = max(high_{t-20..t-1})      // rolling(20).max().shift(1), causal prior-bar
lower_t = min(low_{t-20..t-1})       // rolling(20).min().shift(1), causal prior-bar
ready   = positional index >= 22     // source guard len(df) < period+2 → neutral
entry_t = (close_{t-1} <= upper_t) AND (close_t > upper_t) AND ready AND band-defined
exit_t  = (close_{t-1} >= lower_t) AND (close_t < lower_t) AND ready AND band-defined
```

- Trade events: `entry_signal` on a fresh-20-high-close bar, `direction` long-only; `exit_signal` on a fresh-20-low-close bar. Both legs are one-bar edge crosses (refires require a fresh cross back through the band). A flat book enters one full unit (`0.001` BTC) on an entry bar; a long book exits the full unit on the first exit-leg bar.
- Exact boundaries (pinned semantics): strict current-bar comparisons (`>`, `<`) with setup legs (`<=`, `>=`) exactly as coded — a close exactly on `upper_t` fires no entry (`close > upper` fails); a close exactly on `lower_t` fires no exit; touches hold the prior state. `middle_t`, `confidence`, the `indicators={upper, lower, middle}` echo, and `price=round(curr_close, 4)` are diagnostic/formatting — read by zero order-gating comparisons (fenced, never promoted).
- Mutual-exclusion proof (no tie-break pin required): every bar has `upper_t >= lower_t` (a max over 20 prior highs vs a min over 20 prior lows; each bar has `high >= low`). Entry requires `close_t > upper_t`; exit requires `close_t < lower_t <= upper_t < close_t` — jointly unsatisfiable on every bar, degenerate or otherwise. Empirically confirmed this cycle: the real rule's twin evaluated over 60 synthetic bars prints zero co-print bars. The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero `short` tokens ship anywhere and every return hardcodes `direction="long"` — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the fresh-20-low cross is the sole position-ending path. Stop loss, take profit, ROI ladder, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, never defaulted — adverse excursions have no capital guardrail besides the eventual 20-bar-low exit (disclosed principal risk). No exit leg reads net profit, fees, or funding — costs change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit (`0.001` BTC fixed base quantity), at most one open position; a positioned book treats further entry-edge bars (including consecutive ramp refires) as hold-no-ops — no pyramiding, no averaging; a flat book treats exit-leg bars as no-ops; re-entry re-arms on any qualifying fresh-high cross after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / open-trade reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (both trigger legs) and `high`/`low` (inside the pinned prior-bar bands) with fixed non-positive offsets (one-bar shifts only — no forward reference); the decision bar's own `open` and `volume` are never read (census zero). No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. The `compatible_regimes` set is class metadata read by zero signal lines.

## Required data

- Completed `1d` bars of BTCUSDT spot: `close` (both trigger legs), `high`/`low` (inside the pinned prior-bar bands only). No `open` read, no volume, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1d` (researcher pin, disclosed — the file declares no frame; the rule is pure bar-count logic so any fixed interval preserves the predicates; `1d` rides the `forven-donchian-regime-breakout` `1d` precedent — no novel-interval confirmation burden attaches).
- Availability mapping (pinned-engine support, not assumed): Binance spot REST kline row `timestamp` is the bar OPEN time (`binance_spot_candles.py` `_parse_rest_candles`, `row[0]`, same pinned engine commit below); the decision/fill effective time for row `t` is `timestamp_t + 86400s` (the bar's close time — exact for contiguous fixed-interval klines). At that instant every input bar `≤ t` is complete and `close_t` is the current market print: signals read no future, fills take no future. Contiguity rule (deterministic data rule, disclosed): a bar whose `timestamp` does not equal the previous bar's `timestamp + 86400s` (a gap) carries no decision and no fill — the book holds its prior state across the gap; prices are never fabricated, missing bars are never interpolated.
- Warmup (researcher pin, disclosed): 60 completed `1d` bars held flat. Covers the source's own 22-bar guard plus the per-bar/twin agreement transient (the twin resolves shift-NaN rows via `.fillna(False)` while the per-bar path returns explicit neutral — both agree from bar 22 on complete data) with margin. Coded behaviour underneath: rolling windows print NaN until seeded and the file's explicit `isna` guards collapse such rows to neutral — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization. One evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT spot, unleveraged (researcher choice — the roster names `"BTC"` only; the file's `"leverage": 3.0` defaults hint is explicitly not adopted; no source-market equivalence is claimed).
- Pinned-engine path (verified this cycle against immutable source, not assumed): Hummingbot package `20260920`, VERSION `dev-2.17.0`, engine commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` (`HCH725/hummingbot`): spot connector `binance` + `BinanceSpotCandles` feed (`interval` passed straight to the venue, `_get_rest_candles_params`; `"1d"` is a member of the pinned `INTERVALS` map) + `OrderExecutor` MARKET + `BacktestPositionHold` netting. MARKET executors fill at the creation row's close (`order_executor_simulator.py`: `fill_timestamp = df['timestamp'].iloc[0]`, `entry_price = close` at that row, `POSITION_HOLD` termination) — the decision bar's own close at its effective close time, causally available. No maker-touch, queue, or intrabar-path-dependent fill.
- Controller state machine (derived, fully specified — no engine default is relied on for decisions): the controller keeps its own fill ledger (created BUY executor ids with base qty) with states flat/long(Q). On row `t` it evaluates the source predicates over completed bars `≤ t`; flat+entry creates one MARKET BUY for `Q = 0.001` BTC and records long(Q); long+exit creates one MARKET SELL for `Q` and records flat; long+entry is a hold-no-op; flat+exit is a no-op. Exit sizing comes from the controller's own ledger, never from engine timing. Engine `positions_held`/`executors_info` timing (including the one-row hold-conversion lag inside `update_state` and the 3600s terminated-executor view window, `DEFAULT_TERMINATED_EXECUTORS_WINDOW = 3600`) never gates a decision — the design is window-independent by construction, which is exactly what the `1d` (86400s) spacing requires. A strategy-specific controller artifact itself is downstream `IMPLEMENTATION_NEEDED` work, never an admission leg; what is demonstrated here is that every required primitive exists on the cited path.
- Sizing/capital/costs (pinned research cost model — defined here, never punted downstream): fee `0.001`/side passed as the engine `trade_cost` and accumulated per fill as `cum_fees_quote` (order sim line 62); slippage `0.0` pinned (fills land exactly on the engine close); funding not applicable (spot has no funding leg; the file reads no funding — census zero); precision: the cited path applies no quantity or price rounding (`amount × close` floats, no lot/tick step in-path) and `Q = 0.001` BTC is exactly representable, so no rounding event exists in the admission model. Trade economics identity: `net = Σ realized_gross − Σ cum_fees_quote`, both primitives produced by the cited path (`BacktestPositionHold.add_executor` accumulates both; `summarize_results` reports them separately). Explicitly fenced: the engine `net_pnl_quote` summary field is gross-only (it does not deduct hold fees) and `update_state total_pnl` excludes closed holds — neither label is used here as fee-inclusive equity or closed-trade cash; economics come only from the stated identity. No hypothetical zero funding is reported as realized funding — there is no funding on spot to report.
- Leverage/margin/liquidation: none exists on the specified path — spot, unleveraged, no margin account, no liquidation branch, no forced-close state. The file's leverage hint is not adopted and no perps/isolated-margin accounting is admitted.
- Concurrency: at most one position at any time; single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (131 lines: the `donchian_bands` helper with its anti-lookahead docstring, the `resolve_donchian_period` resolver, the lockstep `generate_signal`/`generate_signals` twins, the `TYPE_NAME`/roster registration, and the `{"period": 20, "leverage": 3.0}` defaults). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Representative engine-primitive validation executed this cycle (2026-10-24, `/opt/homebrew/bin/python3` venv with pandas/pydantic): the REAL `OrderExecutorSimulator.simulate`, the REAL `ExecutorSimulation`, the REAL `BacktestPositionHold` class (AST-extracted from the pinned file, unmodified), and the REAL `donchian_bands`/`generate_signals` rule (with a minimal `BaseStrategy`/`Signal` stand-in for the `forven.strategies.base` import only) — hummingbot enum/config names carried by minimal stand-ins (`TradeType`, `CloseType`, `RunnableStatus`, `ExecutionStrategy`, `ExecutorInfo`, `OrderExecutorConfig`), no behavioural stubbing. 57 asserts, all passing:

- V1 MARKET-fill primitive (5 asserts): BUY `0.001` base fills at the creation row's close, `POSITION_HOLD`, `filled_quote = amount × close` exact, `cum_fees = trade_cost × quote` exact, engine `net_pnl_quote` stays `0` (gross-only label, as fenced).
- V2 hold-netting primitive (4 asserts): BUY `0.001 @ 100000` then SELL `0.001 @ 110000` at cost `0.001`/side → closed (`net_base = 0`), gross `10.0`, `cum_fees 0.21`, `net = gross − fees = 9.79` — the stated economics identity on engine primitives.
- V3 causality/exclusion (42 asserts): twin predicates evaluated on every truncated prefix `df[:k+1]` equal the full-frame evaluation at `k` for all 39 eligible bars (no future read by construction); zero entry/exit co-print bars; contiguity predicate holds on the synthetic `1d` grid; `t_end = ts + 86400s` mapping asserted.
- V4 code-evidence asserts (6 asserts): `DEFAULT_TERMINATED_EXECUTORS_WINDOW = 3600` literal present; `collect_executors_ledger` completeness docstring present; prune scope touches the controller view only (holds never pruned); MARKET-first-candle comment present; `summarize_results` gross/fee split present. Not a performance backtest, not a deployment — a primitive capability check, exactly the once-per-new-requirement validation the contract calls for.

### Negative evidence

1. Leading-window behaviour fenced: rolling seeds print NaN until windowed; the file's explicit `isna` guards plus the twin's `.fillna(False)` collapse every undecided row to neutral. The 60-bar researcher floor additionally holds all pre-seed bars flat — disclosed, not repaired. Per-bar guard and twin agree from bar 22 on complete data; the floor covers the transient.
2. Exact-touch rule fenced: entry demands strict `close > upper` with setup `close_prev <= upper`; exit demands strict `close < lower` with setup `close_prev >= lower`. Touches hold the prior state — disclosed, not smoothed.
3. `middle`-band quarantine fenced: `middle = (upper + lower) / 2.0` is computed every bar and echoed into the diagnostic `indicators` dict, but the entry/exit predicate reads `upper`/`lower` only — promoting `middle` into a leg (e.g. a midline exit) would be a different, unpinned rule with different trade events.
4. Diagnostic quarantine fenced: `confidence` (1.0 on entry bars else 0.0), `price=round(curr_close, 4)`, and the `indicators` dict are envelope decoration read by zero order-gating comparisons; `compatible_regimes` is class metadata read by zero signal lines; the `SXXX-DONCHIAN-BTC` roster row is an asset label, not a rule.
5. Variant menus fenced: `parameter_space()` (`period` 10–40 step 5) and the legacy `donchian_period` resolver key are each a different, unpinned rule — this record freezes canonical `period = 20` as written; adopting any grid point or alias would change trade events and is never claimed here.
6. Pool naked-Donchian sibling fenced: `donchian-20-10-breakout-btcusdt-1h-2026-10-06` (Pine naked prior-20-high / prior-10-low on `1h`) differs on exit length (10 vs 20), frame (`1h` vs `1d`), and immutable source — a 20-bar-low breakdown bar exits here and nothing there; not a re-tuning (changing this record's exit to 10 would be a different, unpinned rule).
7. Pool regime-gated sibling fenced: `forven-donchian-regime-breakout-long-flat-btcusdt-1d-2026-10-19` (same repo, different file: 55-bar entry / 20-bar exit AND-gated with close-above-EMA200 plus ADX14 ≥ 25) differs on entry length (55 vs 20), gate (veto vs none — a veto-failed 55-breakout fires there never, while any veto-failed 20-breakout fires here), exit (20-low-or-sub-EMA vs 20-low only), and source file. Neither record is the other's provenance.
8. Pool Donchian-geometry cousins fenced: `turtle-soup-donchian-fade-bracket` (fades the extreme — opposite side), `eterna-donchian-20-1-midline-two-sided` (two-sided midline machine on `4h`), `turtle-system-2-55d-breakout-2n-stop-half-n-add` (55-day system with ATR stops and pyramiding), and open PR #353 Heracles (Keltner-Donchian band-ratio state, not a breakout) each trade a different construction — none evaluates a naked 20/20 prior-band edge-cross long-flat.
9. Engine-label fences (answers to known review findings, pre-declared so no repair is ever needed): fee-inclusive cash is never claimed from `net_pnl_quote`; closed-trade equity is never claimed from `update_state total_pnl`; availability is never claimed from open-time labels without the `+86400s` mapping; fills are never claimed intrabar; the 3600s terminated view is never relied on for position state.
10. Derivation boundary fenced: the only non-source-native behaviours are the BTCUSDT-spot-`1d` market/frame pin, the effective-time MARKET-close fills, the single-unit/controller-memory/warmup pin, the pinned cost model with leverage explicitly not adopted, and the `+86400s`/gap data rule — all predeclared above. The 20-bar prior bands, the prior-close-cross entry/exit with all strictness, the guards, the long-only stance, and the no-stop posture are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: Donchian-20 prior bands / prior-close-cross entry-exit pair with pinned strictness / long-only / no-stop posture / single-unit `0.001` BTC / `1d` BTCUSDT spot / effective-time close fills are frozen.

- F1 — Exit-length relevance: replacing the 20-bar exit low with a 10-bar low (same entries, same posture) must not improve net expectancy; fail ⇒ the slow exit adds nothing over the pool's naked 20/10 pair and the record is a label variant of one.
- F2 — Entry-length relevance: replacing the 20-bar entry high with the sibling's veto-gated 55-bar high (same 20-bar exit) must not reproduce-or-beat net expectancy; fail ⇒ the fast naked trigger adds nothing over the admitted regime machine.
- F3 — Edge-vs-level relevance: entering on every bar closing above the prior 20-bar high (level-hold instead of the prior-close cross edge, same exit) must not improve net expectancy; fail ⇒ the cross-edge timing adds nothing over a persistent breakout state.

## Crypto portability

BTCUSDT spot `1d` is the research pin (roster names `"BTC"` only). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting and no leverage. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. Spot has no funding leg, so the funding portability question does not arise; fees/slippage ride the pinned research model, never a venue schedule claim.

## Limitations

- Late entries by construction: the 20-bar high sits above price after any pullback, so V-turn recoveries are entered strictly after the recovery prints a fresh-high close — disclosed lag profile.
- Chop whipsaw: alternating fresh highs and fresh lows print repeated enter-then-exit round trips with no cooldown and no structural filter — disclosed chop profile (consecutive ramp refires are safe hold-no-ops; alternating extremes are real round trips).
- Crash-through blindness: a bar that gaps from a fresh high straight through the 20-bar low exits one bar later — there is no stop order to front-run it, disclosed.
- No risk leg: no stop loss, take profit, ROI rung, trailing-stop order, or time limit exists in source — recorded as explicitly disabled; adverse excursions have no capital guardrail besides the 20-bar-low exit.
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

- https://github.com/judder659/Forven/blob/81d40ebc2ca065d949f0343491b2a9cdade8b581/forven/strategies/builtin/donchian.py
- https://github.com/judder659/Forven
