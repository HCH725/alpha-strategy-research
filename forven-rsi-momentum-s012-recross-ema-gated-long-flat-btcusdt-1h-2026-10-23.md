---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven RSI-momentum S012 40-recross dual-EMA-gated long-flat on BTCUSDT 1h bars
created: 2026-10-23
updated: 2026-10-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-22
sources:
  - https://github.com/judder659/Forven/blob/fb5581411d616d8951385c9e330d040d57c6116c/forven/strategies/builtin/rsi_momentum.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven RSI-momentum S012 40-recross dual-EMA-gated long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source Forven crypto strategy collection; the same lane that supplied the admitted `forven-bb-edge-fade`, `forven-ema-cross-adx-regime`, `forven-macd-cross-adx-regime`, `forven-donchian-regime`, `forven-rsi-s00139`, and `forven-td-sequential` records — this is a further record in that lane, and the first pinned to this exact file).
- Pinned commit SHA: `fb5581411d616d8951385c9e330d040d57c6116c` (committer date `2026-10-22T23:51:57Z`, merge PR #265; verified via the GitHub commits API this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/rsi_momentum.py`.
- GitHub blob SHA at the pinned commit: `f66f0905c5c32b5850a3261fed69c03915bfcc89`, size 5272 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 5272 bytes, 149 lines, SHA-256 `09befeece1ece8817a8ebaf21e6f915f1b5f263bef3aee4970774732648a6d72`, identical to the GitHub blob (`git hash-object` reproduces `f66f0905…15bfcc89`) — the entire file was retrieved and inspected.
- Registration: the file defines class `RSIMomentumStrategy` with `TYPE_NAME = "rsi_momentum"` and the `STRATEGIES` roster (lines 146–148) `[("S012-ETH", …), ("S012-SOL", …), ("S012-BTC", …)]`. The `TYPE_NAME` string is shared with `builtin/rsi_momentum_s00139.py` (S00139) and the strategy template — an on-record registry-collision fact already fenced by the admitted S00139 record — so identity here is class plus file path plus the pinned `S012-BTC` roster leg, all unique. This record pins ONLY this file's literals below, and no reviewer repair may substitute a sibling constant, a sibling gate, or a sibling threshold.
- The file's own words (quoted for gate evidence, never extended): `default_params` are `rsi_period: 14`, `rsi_entry: 40`, `rsi_exit: 60`, `ema_fast: 50`, `ema_slow: 200`, `adx_period: 14`, `adx_min: 0`, `leverage: 3.0`; `generate_signals` is declared "the SINGLE source of entry/exit logic"; entry `(prev_rsi < oversold) & (rsi_val >= oversold) & trend_ok & adx_ok` (line 89) with `trend_ok = (close > ema_fast) & (close > ema_slow)` and `adx_ok = adx_val >= p["adx_min"]`; exit `(prev_rsi >= overbought) & (rsi_val < overbought)` (line 90); `generate_signal` delegates both flags from `generate_signals` (`entries.iloc[-1]`, `exits.iloc[-1]`, lines 120–121) with the single `direction="long"` literal; `prev_rsi = rsi_val.shift(1)` is the only in-file lag (one bar, causal); both legs end in `.fillna(False)`.
- Out-of-file calls pinned (resolved by name through the lazy facade): `from forven.strategies.indicators import adx, rsi` hits the `_FACADE_NAMES` set (line 864, `"rsi"`/`"adx"`/`"atr"` among nine names) plus the PEP-562 `__getattr__` hook (line 879), which re-exports the canonical `forven.scanner` implementations — a single implementation, never redefined. `scanner.rsi` (lines 1918–1931) is Wilder's RMA (`alpha=1/14`, `adjust=False`, `min_periods=14`, `1e-9` loss floor — NaN for the first 13 bars); `scanner.adx` (lines 1933–1947) is the TR/±DM/DX `ewm(span=14, adjust=False)` chain with `1e-9` division floors and no `min_periods` (defined from bar 0, transient while seeding); `scanner.atr` (line 1950, trailing `rolling(14).mean`) is imported only for the display-only `atr_14` indicator echo, never for any gating line. No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no hyperopt parameter, no informative-pair call anywhere in the gating path.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (12238 bytes, blob `27508a2a6b8c546e21adefdb97fc0144fabf881b` — the identical blob the admitted S00139 record verified at the older commit, so unchanged) defines `Signal` with `entry_signal: bool = False` / `exit_signal: bool = False` defaults (lines 69–70), `direction: str = "long"` default (line 72), plus `__post_init__` strict-Boolean coercion (lines 77–80) — flags arriving as strict booleans (as here, via `bool(...)`) pass through unchanged.
- Full-file token census (verified over the 149 lines this cycle): 1 `direction="long"` (the only direction literal) and 0 `direction="short"`; 0 `sell` / 0 `stop` / 0 `limit` / 0 `profit` / 0 `qty` / 0 `trail` (no order arguments, no risk legs of any kind); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the scoped-out `leverage: 3.0` default); 0 `volume` / 0 `funding` / 0 `mark_price` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any order-gating line; 0 `df["open"]` / 0 `df["volume"]` reads anywhere (the gating path reads `close` for RSI/EMAs/comparisons and `high`/`low`/`close` inside ADX/ATR only); 0 `pyramid` / 0 `position_size` / 0 `position_adjust` / 0 `opentrades` / 0 `cooldown` (no position-aware state conditions any signal); 0 `resample` / 0 `merge` / 0 `informative` / 0 `Parameter` / 0 `hyperopt` (no tuning surface, no second frame); 1 `shift` (the single `prev_rsi` one-bar lag — the scanner-internal causal lags live in the pinned scanner, never in this file). `_asset` appears only in the `name`/`asset` label properties (line 18, roster lines 146–148 — never in `generate_signals`); `compatible_regimes` (line 35) is harness metadata never read by the signal path (which takes only `df`/`params`); `parameter_space` (line 135) is optimizer ranges, unused; `atr_14`/`confidence` are display echoes, never gates (fenced in Negative evidence).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Forven deployment. The source pins the RSI(14) 40-recross-up entry with its dual-EMA(50/200) price-position gate and vacuous ADX floor, the RSI(14) 60-cross-down single exit, the one-bar edge forms, the long-only stance, and the no-stop/no-target/no-trailing/no-time-exit posture — but ships no venue spelling, no timeframe, no fill-timing flag, no warmup guard, and no position-sizing rule. Researcher-declared adaptations are exactly five: (1) research market BTCUSDT on Binance spot (the file is pair-agnostic and venue-agnostic; `_asset` is a label only, and no source-market equivalence is claimed); (2) decision frame `1h` (the file names no timeframe — disclosed researcher choice, never a file semantic); (3) the completed-bar tick map below — `1m` execution resolution (the engine default), close-timestamped features, market `CreateExecutorAction` entries and `StopExecutorAction` signal exits on the pinned engine path (disclosed, never presented as the source harness's timing); (4) single-unit position pin with hold-no-op semantics, `cooldown_time = 3600`, and a 250-bar researcher warmup pin (the file carries no position reference and no length guard — disclosed, never presented as source-native behaviour); (5) admission capital/costs ride `total_amount_quote = 1000`, `leverage = 1`, continuous quantities and `trade_cost = 0.0002`, while the house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x, historical funding) is downstream-only experiment, never admission (see Execution assumptions). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-23): working-tree filename/content search for `builtin/rsi_momentum.py` (excluding the S00139 cousin, which only mentions this file in its registry-collision fence), `RSIMomentumStrategy` (excluding `RSIMomentumS00139Strategy`), and `S012-BTC` returns zero strategy records citing this source file, class, or roster leg. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades an RSI-threshold-recross rule. The pool's RSI neighbours are fenced as different constructions in Negative evidence 9. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy when 14-bar Wilder RSI recrosses up through 40 while the close stands above both its 50-bar and 200-bar exponential averages (with a vacuous ADX >= 0 floor that is always true once seeded); sell when RSI crosses back down through 60. The file ships no stop, no target, no trailing, no time exit, no sample, no window, no trade count, and no cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Oversold-recross momentum machine with a slow-trend passport, long-only. Unlike washout systems that buy deep-oversold prints, this one buys the *return* trip: RSI must first print below 40 and then cross back up — a market that never dips below 40 never qualifies no matter how strong the trend, and a market that stays pinned under 40 never fires either. The dual-EMA gate (close above both the 50-bar and the 200-bar averages) passports only uptrends, so the book never bottom-fishes a cascade that keeps printing fresh lows under a falling 200-bar rail. The exit is deliberately asymmetric and impatient: any cross down through 60 — far above the entry line — closes the leg, so winners are cut at the first momentum rollover, not trailed. With no stop anywhere, the failure modes are plain: an entry whose RSI keeps climbing without ever crossing back under 60 is held to the sample end, and a qualified recross that immediately fails back under 40 whipsaws the book across consecutive edges with no cooldown to damp the round trips (disclosed as the principal friction).

## Signal

Exact rule as pinned (any other RSI period, threshold, gate, edge-vs-state pairing, exit leg, frame, or book is a different, unpinned rule). All indicator variants are pinned by call with explicit periods, never library defaults:

```text
rsi[t]    = Wilder RMA-14 of close (scanner.rsi, min_periods=14)
ema50[t]  = close.ewm(span=50, adjust=False).mean()
ema200[t] = close.ewm(span=200, adjust=False).mean()
adx[t]    = scanner chain, period 14 (ewm span=14, no min_periods)
entry = (rsi[t-1] < 40) & (rsi[t] >= 40) & (close[t] > ema50[t])
          & (close[t] > ema200[t]) & (adx[t] >= 0)
exit_ = (rsi[t-1] >= 60) & (rsi[t] < 60)
floor = leading-window bars: NaN comparisons false, then .fillna(False)
```

- Trade events: `entry` fires on the recross-up bar only (one-bar edge, not a persistent state — a book already positioned treats it as a hold-no-op under the position pin below); `exit_` fires on the cross-down bar only. `direction` long-only; the single `direction="long"` literal plus zero short-leg tokens is the complete direction set.
- Exact boundaries (pinned semantics): entry is strict-below then inclusive-at-or-above (`< 40` / `>= 40`) — a bar printing exactly `rsi == 40.0` after a sub-40 print FIRES the entry; exit is inclusive-at-or-above then strict-below (`>= 60` / `< 60`) — a bar printing exactly `rsi == 60.0` from above does NOT fire the exit. Strictness preserved throughout, disclosed, never smoothed. `close == close[4]`-style equality resets exist nowhere here — equality only matters at the two pinned lines above.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `rsi[t-1] < 40` while any exit bar has `rsi[t-1] >= 60` — mutually exclusive on every bar, degenerate or otherwise, so entry and signal-exit never co-print on the same decision bar. The engine's create-before-stop tick order is therefore a never-activated backstop, disclosed, never a live path.
- The ADX floor is constructed-vacuous: `adx_min = 0` with ADX non-negative by construction, so `adx_ok` is true on every seeded bar (source-verbatim threshold, disclosed as inert-by-construction, never deleted and never tightened by repair). Early-bar NaNs compare false and `fillna(False)` holds them flat — coded behaviour, disclosed.
- Exits and risk (explicit): the 60-cross-down signal leg is the complete position-closing set. No stop, no target, no trailing, no time exit — explicitly none further, matching the file's zero risk-leg census, not invented. No exit leg reads net profit, fees, or funding — fees change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry-edge bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit-edge bars as no-ops; re-entry re-arms on any qualifying recross bar after any exit (no source cooldown exists — explicitly none, not invented; the `cooldown_time = 3600` engine pin is moot by construction, see Execution assumptions). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (RSI/EMAs/comparisons) and `high`/`low`/`close` (ADX chain; ATR echo is display-only) with fixed non-negative offsets — one explicit one-bar lag plus trailing smoothers, no forward reference. No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `1h` bars of BTCUSDT: `close` (RSI, both EMAs, all comparisons) plus `high`/`low` (ADX chain only; the ATR echo reads them too but gates nothing). No `open` read, no bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar: the researcher-defined features frame carries exactly one row per completed `1h` bar stamped at that bar's CLOSE time (the availability map), and every window reads the decision bar's causal past only (plus the decision bar's own completed print).
- Warmup (researcher pin, disclosed): the first 250 completed `1h` bars held flat. Covers the 200-bar EMA seed plus RSI/ADX seeding margin with room. The file ships no length guard except the single-shot `len(df) < 3` early-return (not the vectorized semantic — the vectorized `generate_signals` twin is the pinned rule, and its `fillna(False)` holds unseeded bars flat regardless). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT on Binance spot (researcher choice — the source is pair-agnostic and venue-agnostic; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed). Connector pin `binance_spot` (the controller default is `binance_perpetual` — overridden); pair spelling `BTC-USDT`; `leverage = 1` (the config default is 20 — overridden for spot).
- Pinned engine (read line by line this cycle, never assumed): Hummingbot package `20260920` / VERSION `dev-2.17.0` per the repository contract; code pin `HCH725/hummingbot@fac3a7f8c4adfd9f07f462cfaad9e2ed9e8b6467` (committed 2026-09-20, matching the package date; the commit's sole file change is `setup.py` — verified via the commits API — so backtest/controller/simulator semantics equal its parent; `VERSION` reads `dev-2.17.0` at this commit; the newer October DCA-fix commits are explicitly NOT used, so no silent capability broadening). Blobs reproduced this cycle via `git hash-object`: engine `7d1e552d…1106e6` (727 lines), directional controller `b2381bba…899cc` (224 lines), position simulator `5539f0d2…c1396c` (88 lines), simulator base `f77fc610…1222a5`, provider `bdp` excerpt, spot candles `5d0c938a…e4dd0` (109 lines).
- Order timing (derived, disclosed, code-mapped tick by tick): `backtesting_resolution = "1m"` (the engine default — a pin of the default, never an invention). (T1) Execution candles are the `1m` Binance spot klines (`get_candles_df` at resolution, open-label timestamps preserved from kline row[0] by `_parse_rest_candles`). (T2) Every such label is treated strictly as an OPEN label — never as availability: the researcher features frame stamps each completed `1h` bar at its CLOSE time, and the `merge_asof(…direction="backward")` join makes that bar's signal visible only on `1m` ticks at or after the close — no forming-bar `high`/`low`/`close` is ever read at its open label. (T3) On each tick the controller time is the row timestamp and `MidPrice` is that row's `close_bt` (update path), while the strategy rule reads only the merged completed-bar signal. (T4) Entry: entry-edge visible, flat book, `can_create_executor` (single-unit count gate plus the pinned `cooldown_time = 3600`) → `CreateExecutorAction` with a MARKET opener (controller-stock triple-barrier default); the market fill is the engine-verbatim slice-first-close primitive — `start_timestamp` is the creation tick `T` and `entry_price` is the close of the `1m` candle `[T, T+1m)`. Wall-clock honesty clause: the signal is known at `T`, the fill price completes at most 60 s later, and the ledger labels position-state from `T` — this `1m` execution granularity is the engine's own market convention, adopted verbatim and never claimed as same-instant causality. (T5) Signal exit: exit-edge visible while positioned → `StopExecutorAction` with `keep_position = False` → `EARLY_STOP` booked at the current-row close-based PnL (pinned handler path) — the signal exit therefore needs no intrabar touch semantics of any kind. (T6) Entry-while-positioned is a hold-no-op (count gate); exit-while-flat is a no-op; entry and exit never co-fire (proof in Signal).
- Risk legs (all explicitly disabled to match the source's zero-leg census): `stop_loss = None` (default 0.03 — overridden), `take_profit = None` (default 0.02 — overridden), `trailing_stop = None` (stock default), `time_limit = None` (default 2700 — overridden). With all barriers `None`, the position simulator runs each unit from its creation tick to the signal stop; a unit never stopped by sample end closes as `TIME_LIMIT` truncation at the last index — disclosed as truncation, never as a rule. (A fixed-percentage stop of the Bandtastic/ATR-stop form is deliberately NOT added: the reviewer must never invent risk, and neither does this researcher.)
- Cooldown mootness (stated plainly): `max_executors_per_side = 1` (default 2 — overridden) with `cooldown_time = 3600`. While positioned the count gate already blocks; once flat the active set is empty so the cooldown comparison degrades to `time − 0 > 3600` and always passes — hence re-entry re-arms on the first entry-edge tick after any exit, exactly the source's no-cooldown stance. The 3600 pin exists only to satisfy the engine's `gt=0` field constraint with a frame-natural value, disclosed.
- Sizing/capital/costs (admission only): `total_amount_quote = 1000` (the base default is 100 — overridden to the sibling-standard 1000); `amount = 1000 / price / 1` continuous base quantity per the stock creation path — `quantize_order_amount`/`quantize_order_price` exist on the provider but are never called by the creation path or the position simulator (verified absence), so the record declares a pure continuous-quantity model with NO venue-precision or min-notional enforcement claim; `trade_cost = 0.0002` (engine default) with the engine-verbatim round-trip `2 × trade_cost` on full notional. No funding term exists anywhere on this spot path — none claimed, none defaulted to zero-economics: spot funding absence is the disclosed derived boundary. The house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x, historical funding) is a downstream-only experiment, never admission: no DCA/grid executor appears anywhere in this path (Position executor only), so no safety tranche can activate under the single-unit/no-add pin and sizing changes no event.
- Concurrency: at most one position per market at any time; single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (149 lines: dual-threshold RSI edges, dual-EMA price-position gate, vacuous ADX floor, long-only flags, roster, defaults) and the documented facade resolution to the canonical scanner indicators. It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: RSI prints NaN for its first 13 bars (`min_periods=14`) and every strict NaN comparison is false; EMA/ADX seed transiently but causally; `fillna(False)` holds all of them flat. The 250-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no warmup literal, so the floor is purely a researcher pin, never misattributed.
2. Vacuous-gate fence: `adx_min = 0` makes `adx_ok` true on every seeded bar by construction — the gate is source-verbatim and preserved, never tightened into a live filter and never deleted as dead code. Tightening it to any positive floor would be a different, unpinned rule.
3. Threshold-strictness fence: entry needs `rsi[t-1] < 40` with `rsi[t] >= 40` (an exact `40.0` print after a sub-40 print fires); exit needs `rsi[t-1] >= 60` with `rsi[t] < 60` (an exact `60.0` print from above does not fire). Strictness preserved throughout — disclosed, not smoothed.
4. No-edge-confusion fence: both legs are one-bar cross edges on the RSI line with the single `shift(1)` lag — converting either leg to a persistent state (or vice versa) would be a different, unpinned rule with different trade events (states would re-fire across consecutive bars; edges fire once).
5. Dead-code fence: `atr_14`, `confidence = min(1, adx/40)`, the `indicators` echo dict, `parameter_space` ranges, the `compatible_regimes` label, the `leverage: 3.0` default, the `_asset` label, and the `len(df) < 3` single-shot guard gate nothing — none of them conditions any order-gating line under default params. The `_get_oversold/_get_overbought` alternate-name branches are inactive under the pinned defaults (they resolve to 40/60) — disclosed, never exercised.
6. Session/prose fence: the strategy carries no session, calendar, or `timeframe` concept anywhere (census zero) — 24/7 crypto tape needs no session-gap semantics, and every lookback bar is always the immediately prior print.
7. Prose-vs-code fence: `describe()` narrates the rule in words, but the coded `generate_signals` legs govern — the docstring's "SINGLE source" declaration is honoured literally here.
8. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-spot market choice, the `1h` frame, the `1m`-resolution close-timestamped tick map with market-create/stop-exit actions, the single-unit/no-add/no-effective-cooldown position pin, the 250-bar warmup floor, the `total_amount_quote = 1000` / `leverage = 1` / continuous-quantity / `trade_cost = 0.0002` admission economics, and house sizing/costs held downstream-only — all predeclared above. The RSI(14) Wilder construction, the 40/60 thresholds with pinned strictness, the EMA(50/200) gate, the vacuous ADX floor, the edge forms, the long-only stance, and the no-risk-leg posture are source-verbatim effective behaviour.
9. Cousin records fenced as different constructions (none trades an RSI(14) 40-recross-up entry behind a dual-EMA(50/200) price-position gate with a single RSI 60-cross-down exit, long-flat, no stop): the admitted `forven-rsi-s00139-washout-cross` pool-mate trades an RSI(14) washout-cross at 25 behind an SMA(20) gate with a dual exit (75-cross OR trend-loss) on the BTC roster (a market at RSI 35 fires nothing there but everything here; a market losing its SMA-20 exits there but holds here); the admitted `forven-connors-rsi-oversold-recross` pool-mate trades a 3-component ConnorsRSI composite (different oscillator entirely); the admitted `forven-rsi-boundary-rejection` pool-mate is two-sided (different direction handling); the admitted `forven-ema-rsi-pullback-reclaim` pool-mate reclaims RSI through the 45 midline inside a dual-EMA(12/34) stack with a rollover-under-62 exit on the SOL roster (midline-reclaim trigger, different gate, different exit pair); the admitted `forven-ema-cross-adx-regime` and `forven-macd-cross-adx-regime` pool-mates share the gate family (EMA-200 + ADX floor) but trade line-cross signals, never threshold recrosses (a flat-lined RSI oscillating 45↔55 fires edges here and nothing there). Not a threshold re-tuning of any of them: moving either line, dropping either EMA leg, arming the ADX floor, converting either edge to a state, or adding any stop/target would each be a different, unpinned rule — none is admitted here.
10. Sibling-file fence: `rsi_momentum_s00139.py`, `ema_cross.py`, `macd.py`, `bollinger.py`, `donchian.py`, and every other Forven builtin are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: RSI(14) Wilder / 40-recross entry with pinned strictness / dual-EMA(50/200) gate / vacuous ADX floor / single 60-cross-down exit / one-bar edges / long-only single-unit / `1h` BTCUSDT / `1m`-resolution close-timestamped tick map are frozen.

- F1 — Gate relevance: entering on every 40-recross without the dual-EMA conjunct (same exits otherwise) must not improve net expectancy; fail ⇒ the coded trend passport adds nothing over its ungated twin.
- F2 — Threshold relevance: replacing the 40/60 pair with a 50-midline cross pair (same gates, same exits form) must not improve net expectancy; fail ⇒ the coded oversold/overbought geometry adds nothing over its midline twin.
- F3 — Exit-leg relevance: holding entries to sample end (no 60-cross-down leg, same entries) must not improve net expectancy; fail ⇒ the coded rollover exit adds nothing over buy-and-hold.

## Crypto portability

BTCUSDT on Binance spot `1h` is the research pin (source names no market; the `1h` frame is a researcher choice on a timeframe-free source). Long-only with full-unit open/close expresses identically on a perpetual venue under the downstream overlay — no short-side approximation is needed or claimed. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. Bar volume is never read, so venue volume-definition differences cannot move any leg. Funding is declared nowhere in the source and exists nowhere on the admission spot path; downstream funding rides house assumptions only.

## Limitations

- The `1h` frame is a researcher choice on a timeframe-free source — no novel-interval confirmation burden attaches beyond the admitted `1h` sibling lane, but other frames would produce different event streams and are different, unpinned evaluations (see Execution assumptions).
- Execution-candle granularity: the fill price completes at most 60 s after the decision tick on the pinned `1m` default resolution; the ledger labels position-state from the creation tick. This is the engine-verbatim market primitive, disclosed with wall-clock honesty, never claimed as same-instant causality. A finer or coarser `backtesting_resolution` would be a different, unverified claim — none is admitted here.
- A position whose 60-cross-down print never arrives is held to sample-end truncation (bounded by nothing but the data end); a winning leg keeps running with no profit-taking leg. This is the coded posture (zero risk legs), disclosed as the record's principal risk.
- Consecutive-edge whipsaw (recross-up, cross-down, recross-up across adjacent bars) exits and re-enters with no effective cooldown — disclosed as the principal friction; the 3600 s engine pin binds only while positioned, where the count gate already blocks.
- The ADX floor is vacuous by construction (`>= 0`) — a dovish researcher must not mistake it for trend protection; it is preserved verbatim, disclosed as inert.
- Vendored indicator internals (RMA seeding, `min_periods` NaN propagation, ewm transients) live in the pinned scanner outside the strategy file — pinned by facade call with explicit periods, never re-derived; exact reproduction inherits that seeding alongside the 250-bar floor.
- No trailing, no stop, no target, no time exit, no short leg — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/judder659/Forven/blob/fb5581411d616d8951385c9e330d040d57c6116c/forven/strategies/builtin/rsi_momentum.py
- https://github.com/judder659/Forven
