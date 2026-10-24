---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven ORB 4-bar trailing-channel level-breakout long-flat on BTCUSDT 1d bars
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
  - https://github.com/judder659/Forven/blob/0e35d7dd3f84a8ef6d8d7a3b131ff366585a451e/forven/strategies/builtin/orb.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven ORB 4-bar trailing-channel level-breakout long-flat on BTCUSDT 1d bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the fifty-three admitted Forven records, including the `forven-ichimoku-tenkan-kijun-cross` sibling admitted 2026-10-24 that pins the identical base-class blob below).
- Pinned commit SHA: `0e35d7dd3f84a8ef6d8d7a3b131ff366585a451e` (verified as the repository HEAD via `git rev-parse` on a fresh clone during this cycle — record `source_as_of` is the cycle date, never a fetch date).
- Exact file path: `forven/strategies/builtin/orb.py`.
- GitHub blob SHA at the pinned commit: `73e8cb8c50ba787ad5070f42c8bc7a28bbf97079`, size 1914 bytes.
- Byte-identity check: the file on disk at the pinned commit is 1914 bytes, 51 lines, `git hash-object` reproduces `73e8cb8c…97079` — the entire file was retrieved and inspected.
- Registration: the file defines class `ORBStrategy(BaseStrategy)` (the only class in the file) with `TYPE_NAME = "orb"` and a one-row roster `STRATEGIES = [("TOMB-ORB", ORBStrategy, {"_asset": "BTC"})]` — venue spelling is the bare `"BTC"` asset label only, no timeframe override. Identity here is class plus file path plus `TYPE_NAME`, all unique.
- The file's own words (quoted for gate evidence, never extended): module docstring `Opening Range Breakout strategy.`; `describe()` returns `Trades the breakout of the high/low established in the first N bars of the session.`; `default_params` returns exactly `{ "range_bars": 4, "leverage": 3.0 }`; vectorized twin (`generate_signals`, docstring: `Vectorized twin of generate_signal — the SINGLE source of entry/exit logic`) computes `recent_high = df["high"].rolling(n).max().shift(1)`, `recent_low = df["low"].rolling(n).min().shift(1)`, `entry = close > recent_high`, `exit_ = close < recent_low`, both `fillna(False)`; per-bar path delegates (`entries, exits = self.generate_signals(df)`) and returns `price=round(curr_close, 4)`, hardcoded `direction="long"`, `confidence=1.0`, `indicators={"orb_high": round(recent_high, 4)}`. No performance phrase of any kind ships anywhere in the 51 lines.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (12238 bytes, blob `27508a2a6b8c546e21adefdb97fc0144fabf881b` — byte-identical to the blob pinned by the admitted Ichimoku sibling) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults and `direction: str = "long"` default, and `BaseStrategy.__init__(strategy_id, params)` merging `{**default_params, **params}`. The file's explicit `direction="long"` needs no default reading.
- Full-file token census (verified over the 51 lines this cycle): 0 `short` (no short leg, no short identifier anywhere); 0 `df["open"]` / 0 `df['open']` reads (the two case-insensitive `open` hits are the `Opening` prose word in the module docstring and the `name` property only — display prose, never a data read); 0 `volume`; 0 `funding` / 0 `mark_price`; 0 `request` / 0 `security`; 0 `resample` / 0 `informative`; 0 `hyperopt`; 0 `trailing` / 0 `stoploss` / 0 `stop_loss` / 0 `take_profit`; 0 `pyramid` / 0 `position_` / 0 `cooldown` / 0 `max_open_trades` (the position pin below is a predeclared researcher rule, never a file semantic); 0 `timeframe` / 0 `calendar`; 0 `order_types` / 0 `startup` / 0 `can_short`; 1 `session` (the `describe()` display string `first N bars of the session` — prose only, zero session/calendar logic anywhere, see the session fence below); 2 `.shift(1)` (both positive lags, zero `shift(-`); 2 `fillna(False)` on the single twin return line; 1 `direction` (`direction="long"`); 1 `leverage` (the `"leverage": 3.0` defaults entry — an unused bare default replaced below, never a margin claim).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Forven deployment. The source pins the 4-bar trailing high/low channel construction, the level-breakout entry and level-breakdown exit with all strictness, the long-only stance, the no-stop posture, and the `TOMB-ORB` / `BTC` roster identity — but ships no venue spelling beyond `"BTC"`, no frame, no fill-timing flag, no guard/warmup rule, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market/frame `BTCUSDT` spot `1d` (the roster names `"BTC"` and the file declares no frame; venue spelling and the `1d` decision-frame pin are disclosed, never a source claim); (2) completed-bar decisions at effective time `timestamp + 86400s` with MARKET fills at the decision bar's own close on the cited pinned-engine path (the file returns `price=round(curr_close, 4)` — the decision bar's own close; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit `0.001` BTC position pin with controller-memory state machine plus a 30-bar researcher warmup floor (covers the uncapped 4-bar seeding with 26 bars of margin; see Required data); (4) the pinned research cost model below (fee 0.001/side post-hoc, slippage 0, funding not applicable on spot, no exchange lot/tick quantization in-path) replacing the bare `"leverage": 3.0` defaults entry, which carries no fee/funding/margin concept and is adopted here as unleveraged spot (precedent: the admitted `forven-bollinger-s026` record likewise replaces the same bare `3.0` default with an explicit house overlay). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-24): working-tree filename/content search for `builtin/orb.py`, `ORBStrategy`, `TOMB-ORB`, and `TYPE_NAME = "orb"` returns zero strategy records citing this source file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades a 4-bar trailing-channel level-breakout rule. Not a duplicate, paraphrase, or trivial parameter variant: a 4-bar micro-channel with level (state) triggers from this immutable file is fenced against every Donchian-family pool-mate in Negative evidence 6–8.

## Economic mechanism

### Source-reported

The source claims only what its code prints: hold long exposure on any bar whose close prints strictly above the trailing 4-bar highest high, stand back to flat on any bar whose close prints strictly below the trailing 4-bar lowest low. The bands are pure trailing-bar high/low extremes with no volatility normalization, no trend gate, and no session logic despite the `describe()` prose. No stop, no target, no trailing, no time exit, no sizing, no cost basis ships anywhere — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Micro-breakout holder, long-only, state-triggered, zero-gate. Any close beyond the 4-bar extreme holds long, however thin the margin, and any close beneath the opposite extreme exits — the book has no memory beyond the current bar's position relative to the two 4-bar levels. Unlike edge-triggered Donchian systems (a fresh cross fires once, then silence), this rule re-affirms every bar: a vertical ramp holds with a fresh entry stamp on each bar (absorbed as hold-no-ops by the position pin), and chop that straddles a 4-bar extreme whipsaws the book with no cooldown. Unlike the pool's gated breakout siblings (EMA200 trend line, ADX strength floor), there is no regime veto — a 4-bar extreme is tradable in chop, in trend, and off a single wick. The failure mode is plain: the 4-bar window turns every minor range expansion into a position and every minor contraction into an exit, so sideways tape prints repeated enter-then-exit round trips at full cost.

## Signal

Exact rule as pinned (any other window length, band construction, trigger polarity, gate, frame, fill, book, or risk posture is a different, unpinned rule). `HH(n)/LL(n)` are trailing highest-high/lowest-low:

```text
recent_high_t = max(high_{t-4..t-1})      // rolling(4).max().shift(1), causal prior-bar
recent_low_t  = min(low_{t-4..t-1})       // rolling(4).min().shift(1), causal prior-bar
entry_t  = (close_t > recent_high_t)      // LEVEL: true on every beyond-band bar
exit_t   = (close_t < recent_low_t)       // LEVEL: true on every beneath-band bar
```

- Trade events: `entry_signal` on every bar closing above the trailing 4-bar high; `direction` long-only; `exit_signal` on every bar closing below the trailing 4-bar low. Both legs are bar-state levels (refires require nothing beyond the close holding beyond the band — consecutive entry bars are the normal ramp case, verified this cycle). A flat book enters one full unit (`0.001` BTC) on an entry bar; a long book exits the full unit on the first exit-leg bar.
- Exact boundaries (pinned semantics): strict current-bar comparisons (`>`, `<`) exactly as coded — a close print exactly on `recent_high` fires no entry; a close exactly on `recent_low` fires no exit; touches hold the prior state. `price=round(curr_close, 4)`, `confidence=1.0`, and the `indicators={"orb_high": ...}` echo are diagnostic/formatting — read by zero order-gating comparisons (fenced, never promoted).
- Mutual-exclusion proof (no tie-break pin required): every bar has `recent_high_t >= recent_low_t` (a max over 4 prior highs vs a min over 4 prior lows; each bar has `high >= low`). Entry requires `close_t > recent_high_t`; exit requires `close_t < recent_low_t <= recent_high_t < close_t` — jointly unsatisfiable on every bar, degenerate or otherwise. Empirically confirmed this cycle: the real rule evaluated over a 300-bar synthetic tape prints zero co-print bars. The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero `short` tokens ship anywhere and the sole return hardcodes `direction="long"` — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the beneath-band level is the sole position-ending path. Stop loss, take profit, ROI ladder, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, never defaulted — adverse excursions have no capital guardrail besides the eventual beneath-band exit (disclosed principal risk). No exit leg reads net profit, fees, or funding — costs change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit (`0.001` BTC fixed base quantity), at most one open position; a positioned book treats further entry-level bars (including consecutive ramp refires) as hold-no-ops — no pyramiding, no averaging; a flat book treats exit-level bars as no-ops; re-entry re-arms on any qualifying beyond-band bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / open-trade reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low` (inside the band construction) and `close` (both trigger legs) with fixed non-positive offsets (`.shift(1)` only — no forward reference); the decision bar's own `open` and `volume` are never read (zero `df["open"]` reads, zero `volume` tokens). The `session` word in `describe()` is display prose: zero session/calendar logic, zero resample, zero date-gating branch exists anywhere in the 51 lines — the effective rule is a pure trailing 4-bar channel on 24/7 tape (disclosed adaptation of the prose, never a source claim about sessions). No funding/OI/mark-price read, no `request.*`, `security()`, hyperopt parameter, or stop/limit order argument anywhere in the gating path. The `compatible_regimes` set (`VOLATILE`/`TREND_UP`) is class metadata read by zero signal lines.

## Required data

- Completed `1d` bars of BTCUSDT spot: `high`/`low` (band construction), `close` (both trigger legs). No `open` read, no volume, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1d` (researcher pin, disclosed — the file declares no frame; the rule is pure bar-count logic so any fixed interval preserves the predicates; `1d` rides the `forven-naked-donchian-20` `1d` precedent — no novel-interval confirmation burden attaches).
- Availability mapping (pinned-engine support, not assumed): Binance spot REST kline row `timestamp` is the bar OPEN time (`binance_spot_candles.py` `_parse_rest_candles`, `row[0]`, same pinned engine commit below); the decision/fill effective time for row `t` is `timestamp_t + 86400s` (the bar's close time — exact for contiguous fixed-interval klines). At that instant every input bar `≤ t` is complete and `close_t` is the current market print: signals read no future, fills take no future. Contiguity rule (deterministic data rule, disclosed): a bar whose `timestamp` does not equal the previous bar's `timestamp + 86400s` (a gap) carries no decision and no fill — the book holds its prior state across the gap; prices are never fabricated, missing bars are never interpolated.
- Warmup (researcher pin, disclosed): 30 completed `1d` bars held flat. Covers the uncapped 4-bar band seeding (first defined band at index 4, verified this cycle) with 26 bars of margin. Coded behaviour underneath: rolling windows print NaN until seeded and every IEEE NaN comparison in the gating path is False, and the twin resolves such rows via `fillna(False)` — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization. One evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT spot, unleveraged (researcher choice — the roster names `"BTC"` only; the file's bare `"leverage": 3.0` defaults entry is explicitly replaced by this unleveraged pin as declared above; no source-market equivalence is claimed).
- Pinned-engine path (verified this cycle against immutable source, not assumed): Hummingbot package `20260920`, VERSION `dev-2.17.0`, engine commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` (`HCH725/hummingbot`; verified ancestor of that repository's current HEAD this cycle): spot connector `binance` + `BinanceSpotCandles` feed (`interval` passed straight to the venue, `_get_rest_candles_params`; `"1d"` is a member of the pinned `INTERVALS` map) + `OrderExecutor` MARKET + `BacktestPositionHold` netting. MARKET executors fill at the creation row's timestamp and close (`order_executor_simulator.py`: `fill_timestamp = df['timestamp'].iloc[0]`, `entry_price = close` at that row, `POSITION_HOLD` termination) — the decision bar's own close at its effective close time, causally available. No maker-touch, queue, or intrabar-path-dependent fill.
- Controller state machine (derived, fully specified — no engine default is relied on for decisions): the controller keeps its own fill ledger (created BUY executor ids with base qty) with states flat/long(Q). On row `t` it evaluates the source predicates over completed bars `≤ t`; flat+entry creates one MARKET BUY for `Q = 0.001` BTC and records long(Q); long+exit creates one MARKET SELL for `Q` and records flat; long+entry is a hold-no-op (the normal ramp case for level triggers); flat+exit is a no-op. Exit sizing comes from the controller's own ledger, never from engine timing. Engine `positions_held`/`executors_info` timing (including the one-row hold-conversion lag inside `update_state` and the 3600s terminated-executor view window, `DEFAULT_TERMINATED_EXECUTORS_WINDOW = 60 * 60` in `backtesting_engine_base.py`, which is exactly what the `1d` (86400s) spacing requires) never gates a decision — the design is window-independent by construction. A strategy-specific controller artifact itself is downstream `IMPLEMENTATION_NEEDED` work, never an admission leg; what is demonstrated here is that every required primitive exists on the cited path.
- Sizing/capital/costs (pinned research cost model — defined here, never punted downstream): fee `0.001`/side passed as the engine `trade_cost` and accumulated per fill as `cum_fees_quote` (order sim fee line); slippage `0.0` pinned (fills land exactly on the engine close); funding not applicable (spot has no funding leg; the file reads no funding — census zero); precision: the cited path applies no quantity or price rounding (`amount × close` floats, no lot/tick step in-path) and the configured quantity is `Q = 0.001` BTC. The simulator explicitly converts `config.amount` to binary float before multiplying by the close, and `ExecutorSimulation` converts the resulting float quote amounts to `Decimal`; binary floating-point rounding and tiny residual base balances after netting are therefore possible. Exact decimal representability and exact net-zero engine holds are not claimed. As specified above, controller-memory flat/long state, not the engine hold `is_closed` flag, governs decisions. Trade economics identity: `net = Σ realized_gross − Σ cum_fees_quote`, both primitives produced by the cited path (`BacktestPositionHold.add_executor` accumulates both; `get_position_summary` reports them separately). Explicitly fenced: the engine `net_pnl_quote` summary field is gross-only (it does not deduct hold fees) and `update_state total_pnl` mixes open-hold unrealized with executor realized — neither label is used here as fee-inclusive equity or closed-trade cash; economics come only from the stated identity. No hypothetical zero funding is reported as realized funding — there is no funding on spot to report.
- Leverage/margin/liquidation: none exists on the specified path — spot, unleveraged, no margin account, no liquidation branch, no forced-close state. The file's `3.0` bare default is replaced exactly as declared above and no perps/isolated-margin accounting is admitted.
- Concurrency: at most one position at any time; single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (51 lines: the 4-bar trailing-band twin, the delegating scalar path with the hardcoded `direction="long"` and the `round(curr_close, 4)` price echo, the `TYPE_NAME`/roster registration, and the `{"range_bars": 4, "leverage": 3.0}` defaults). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Representative engine-primitive validation executed this cycle (2026-10-24, `qlib-tests` venv with pandas/numpy): the REAL `OrderExecutorSimulator.simulate`, the REAL `BacktestPositionHold` class (AST-extracted from the pinned file, unmodified), and the REAL `orb.py` rule running on the REAL `forven/strategies/base.py` (byte-identical blob) — hummingbot enum/config names carried by minimal stand-ins with identical member names/values (`TradeType`, `ExecutionStrategy`, `OrderExecutorConfig`, `ExecutorSimulation`, `ExecutorInfo`, `PositionSummary`), no behavioural stubbing. 46 asserts, all passing:

- A1–A6 source identity (6 asserts): forven HEAD equals the pinned commit; `orb.py` blob `73e8cb8c`, 1914 bytes, 51 lines; `base.py` blob equals the sibling-pinned `27508a2a`, 12238 bytes.
- R1 defaults+roster pin (2 asserts): strategy resolves `range_bars 4 / leverage 3.0` under pinned defaults; `TYPE_NAME "orb"`, roster `TOMB-ORB` / `_asset BTC`.
- R2–R9 rule causality (10 asserts): twin length; zero entry/exit co-print bars over a 300-bar synthetic tape; prefix evaluation equals full-frame point-in-time levels on 24 prefixes (no future read by construction); per-bar `generate_signal` agrees with the vectorized twin on 6 prefixes; 4-bar frames neutral with boundary evaluation (first entry exactly at index 4); consecutive refires on a monotonic ramp (level, not edge); both legs fire on synthetic tape (pinned seed 7); long-only on every sampled bar; flat tape holds neutral.
- R10 census (11 asserts): zero `short`; zero `df["open"]` reads with `open` surviving only inside the two `Opening` prose words; zero `volume`/`funding`; zero risk/order/session-logic tokens (the single `session` hit is the `describe()` display string); exactly 1 `direction` and 1 `leverage` token; `.shift(1)` twice with zero negative shift; `fillna(False)` twice on the twin return; band construction literals present.
- V1 MARKET-fill primitive (5 asserts): BUY `0.001` base fills at the creation row's timestamp and close, `POSITION_HOLD`, `filled_quote = amount × close` (1e-9), `cum_fees = trade_cost × quote` (1e-12), engine `net_pnl_quote` stays `0` (gross-only label, as fenced).
- V2 hold-netting primitive (4 asserts): BUY `0.001 @ 100000` then SELL `0.001 @ 110000` at cost `0.001`/side → closed (`net_base = 0`), gross `10.0` exact, `cum_fees ≈ 0.21` (1e-9 — binary-float dust disclosed), `net = gross − fees ≈ 9.79` — the stated economics identity on engine primitives.
- V3 code-evidence asserts (8 asserts): `DEFAULT_TERMINATED_EXECUTORS_WINDOW = 60 * 60` literal present; `collect_executors_ledger` present; MARKET-first-candle comment present; hold realized/fee accumulation split present; `INTERVALS` contains `1d`; REST parse uses `row[0]` open-time; `timestamp + 86400s` mapping asserted on a synthetic `1d` grid; engine commit verified ancestor of the repository HEAD. Not a performance backtest, not a deployment — a primitive capability check, exactly the once-per-new-requirement validation the contract calls for.

### Negative evidence

1. Leading-window behaviour fenced: rolling seeds print NaN until the 4-bar window fills and every IEEE NaN comparison in the gating path is False; the twin's `fillna(False)` collapses pre-seeded rows to neutral. The 30-bar researcher floor additionally holds all pre-seed bars flat — disclosed, not repaired.
2. Exact-touch rule fenced: entry demands strict `close > recent_high`; exit demands strict `close < recent_low`. A close print exactly on either band fires neither leg — touches hold the prior state, disclosed, not smoothed.
3. Level-refire scope fenced: entry is true on EVERY beyond-band bar, not just fresh crosses — consecutive ramp bars re-stamp entry (verified R6c) and are absorbed as hold-no-ops by the position pin. Converting the entry to a fresh-cross edge would be a different, unpinned rule with different trade events (see Falsification F3).
4. Diagnostic quarantine fenced: `confidence=1.0` (constant, entry context only), `price=round(curr_close, 4)`, and the `indicators={"orb_high": ...}` dict are envelope decoration read by zero order-gating comparisons; `compatible_regimes` (`VOLATILE`/`TREND_UP`) is class metadata read by zero signal lines; the `TOMB-ORB` roster row is an asset label, not a rule.
5. Prose/site fences: the `Opening` word (module docstring + `name`) and the single `session` word (`describe()`: `first N bars of the session`) are display prose only — zero `df["open"]` reads, zero session/calendar/resample logic anywhere. The effective rule is a trailing 4-bar channel, disclosed, not re-timed to any session grid.
6. Pool naked-Donchian-20 sibling fenced: `forven-naked-donchian-20-breakout-long-flat-btcusdt-1d-2026-10-24` trades a 20-bar prior-band construction with fresh-cross EDGES on both legs plus an explicit 22-bar guard, from immutable file `donchian.py` — a 5x-slower swing horizon whose edge entry fires once per breakout where this 4-bar level entry re-stamps every beyond-band bar. Different file, different window, different trigger polarity, different guard posture; neither record is the other's provenance.
7. Pool breakout-range-20 sibling fenced: `forven-breakout-range-20bar-long-flat-btcusdt-1h-2026-10-20` is the closest structural cousin (level triggers on a trailing channel) but pins a 20-bar window on `1h` perps under the house DCA overlay, from immutable file `breakout_range.py` with its own guard and single-source (twin-less) construction. A 4-bar micro-channel on `1d` spot breaks on noise the 20-bar band never touches — materially different trade events on the same tape, different horizon/regime, different file lineage.
8. Pool Donchian-regime sibling fenced: `forven-donchian-regime-breakout-long-flat-btcusdt-1d-2026-10-19` AND-gates a 55-bar entry band with an EMA(200) trend line and a scanner-ADX(14) ≥ 25 strength floor, with a 202-bar guard, from `donchian_regime.py` — a veto-gated swing system whose ADX/EMA-vetoed bars fire there never, while any beyond-band bar fires here. Different construction, different gate, different guard, different file.
9. Engine-label fences (answers to known review findings, pre-declared so no repair is ever needed): fee-inclusive cash is never claimed from `net_pnl_quote`; closed-trade equity is never claimed from `update_state total_pnl`; availability is never claimed from open-time labels without the `+86400s` mapping; fills are never claimed intrabar; the 3600s terminated view is never relied on for position state; the bare `leverage: 3.0` default is never presented as margin treatment.
10. Derivation boundary fenced: the only non-source-native behaviours are the BTCUSDT-spot-`1d` market/frame pin, the effective-time MARKET-close fills, the single-unit/controller-memory/warmup pin, the pinned cost model with `3.0` replaced by unleveraged spot, and the `+86400s`/gap data rule — all predeclared above. The 4-bar trailing-channel construction, the level-breakout entry and level-breakdown exit with all strictness, the long-only stance, and the no-stop posture are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 4-bar trailing-channel construction / level-breakout entry and level-breakdown exit with pinned strictness / long-only / no-stop posture / single-unit `0.001` BTC / `1d` BTCUSDT spot / effective-time close fills are frozen.

- F1 — Window relevance: replacing the 4-bar window with the 20-bar window (same level triggers, same exit, same posture) must not improve net expectancy; fail ⇒ the 4-bar micro-horizon adds nothing over its swing cousin and the record is a label variant of one.
- F2 — Exit-leg relevance: dropping the beneath-band exit entirely (entries only, never exiting — buy-and-hold from the first beyond-band close) must not improve net expectancy; fail ⇒ the exit leg carries no weight beyond decoration.
- F3 — Level-vs-edge relevance: converting the entry to a fresh-cross edge (entry only when the prior close sat at-or-inside the band) must not improve net expectancy; fail ⇒ the level refire carries no weight beyond the first cross.

## Crypto portability

BTCUSDT spot `1d` is the research pin (roster names `"BTC"` only). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting and no leverage. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape (the `session` prose word is display only, as fenced). Spot has no funding leg, so the funding portability question does not arise; fees/slippage ride the pinned research model, never a venue schedule claim.

## Limitations

- Chop whipsaw by construction: the 4-bar window turns minor range expansions into entries and minor contractions into exits with no cooldown and no structural filter — disclosed chop profile, harsher than any 20-bar cousin.
- Late exits on reversals: a bar that gaps from beyond-band-high to deeply beneath-band-low exits one bar later — there is no stop order to front-run it, disclosed.
- Single-wick sensitivity: one extreme wick resets the band for the next four bars, so isolated prints gate four bars of entries/exits — disclosed micro-window profile.
- No risk leg: no stop loss, take profit, ROI rung, trailing-stop order, or time limit exists in source — recorded as explicitly disabled; adverse excursions have no capital guardrail besides the beneath-band exit.
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

- https://github.com/judder659/Forven/blob/0e35d7dd3f84a8ef6d8d7a3b131ff366585a451e/forven/strategies/builtin/orb.py
- https://github.com/judder659/Forven
