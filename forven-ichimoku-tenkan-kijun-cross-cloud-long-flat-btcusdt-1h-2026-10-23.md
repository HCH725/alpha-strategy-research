---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven Ichimoku 9/26 tenkan-kijun cross cloud-filtered long-flat on BTCUSDT 1h spot
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
  - https://github.com/judder659/Forven/blob/8e79afa86e6f80a7f5a83eb50742059a9215ca6a/forven/strategies/builtin/ichimoku.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven Ichimoku 9/26 tenkan-kijun cross cloud-filtered long-flat on BTCUSDT 1h spot

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-breakout-range-20bar`, `forven-stochastic-20-recross`, `forven-td-sequential-setup9`, and forty-plus further Forven-sibling records on `main`).
- Pinned commit SHA: `8e79afa86e6f80a7f5a83eb50742059a9215ca6a` (committed `2026-10-22T19:15:55Z`, verified via the GitHub commits API this cycle; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/ichimoku.py`.
- GitHub blob SHA at the pinned commit: `14fb8825e2ccfe041014db200441e89f9c8bd2c6`, size 5871 bytes.
- Byte-identity check: the file retrieved from `raw.githubusercontent.com` at the pinned commit is 5871 bytes, SHA-256 `906207511ebb31e6bdb0cc48cd8e76291992013446f1f81d0eb4887d642cc2a4`, and `git hash-object` reproduces the GitHub blob (`14fb8825…f9c8bd2c6`) — the entire file was retrieved and inspected.
- Registration: the file sets `TYPE_NAME = "ichimoku"` (line 7), `STRATEGY_CLASS = IchimokuStrategy` (line 155), and a single-leg `STRATEGIES` roster (lines 157–159): `("PREBUILT-ICHIMOKU", IchimokuStrategy, {"_asset": "BTC"})`. This record pins exactly that leg. No pool record cites this source file (see pre-write dedup below).
- Out-of-file lineage (actually read at the same pin): the file imports only `pandas` and `forven.strategies.base` (`BaseStrategy, Signal`, line 5). The base module at the same pin (`forven/strategies/base.py`, blob `27508a2a6b8c546e21adefdb97fc0144fabf881b`, 12238 bytes, 361 lines) defines `Signal` with `entry_signal: bool = False` / `exit_signal: bool = False` defaults and `direction: str = "long"` default (lines 66–72), plus `DirectionalSignals` with `long_entries` / `long_exits` and the `empty(index)` all-flat constructor (lines 217–232). The scalar path additionally imports `atr` from `forven.strategies.indicators` (line 86) and uses it ONLY for the `confidence` metadata number (lines 111, 118, 127, 143) — it gates no leg (see Negative evidence 5).
- The file's own words (quoted for gate evidence, never extended): class docstring `Entry: Tenkan-sen crosses above Kijun-sen AND price is above the cloud (Senkou Span A & B). Exit: Tenkan-sen crosses below Kijun-sen.` (lines 11–15); `default_params` returns exactly `{ "tenkan_period": 9, "kijun_period": 26, "senkou_b_period": 52, "leverage": 1.0 }` (lines 29–36); `compatible_regimes` returns `{"TREND_UP", "TREND_DOWN"}` (lines 38–40, metadata never read by the signal path); `describe()` returns `Buys when Tenkan-sen (9) crosses above Kijun-sen (26) and price is above the Ichimoku cloud. …` (lines 42–48); the vectorized twin's docstring `Vectorized twin of generate_signal — the SINGLE source of entry/exit logic.` (line 51) with the scalar delegating to it (`entries, exits = self.generate_signals(df)`, line 123); `parameter_space()` returns `{ "tenkan_period": (7, 12, 1), "kijun_period": (20, 30, 2), "senkou_b_period": (44, 60, 4) }` (lines 147–152, a documented search surface only — this record pins the defaults and runs no search). No performance phrase of any kind ships anywhere in the file — this record adopts no source-reported performance (see Evidence).
- Full-file token census (verified by search over the file this cycle): 0 `short` anywhere (no short leg, no short identifier — long-only is the coded posture); 0 `volume` reads and 0 `open`-series reads (the signal path reads `high`/`low`/`close` only); 0 `funding` / 0 `mark_price` / 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the bare `leverage: 1.0` default, replaced by the spot pin — see Execution assumptions); 0 `trailing` / 0 `pyramid` / 0 `position_adjust` / 0 `cooldown` / 0 `max_open` (no position-aware state conditions any signal); 0 `resample` / 0 `informative` / 0 `request.` / 0 `security` / 0 `startup` / 0 `process_only` / 0 `order_type` / 0 `can_short` / 0 `crossed`; `leverage` exactly once (the default only); `.shift(` exactly six times (twin: two senkou forward-displacements plus two 1-bar cross lookbacks; scalar: the same two senkou displacements — all non-negative, listed in Signal); `iloc[-2]` zero times in the scalar (it reads only the decision bar's own print plus the twin series). The 10 `iloc[-1]` hits are decision-bar reads of already-computed causal series.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the PREBUILT-ICHIMOKU roster leg, the 9/26/52 Ichimoku construction with 26-bar cloud displacement, the cross-up-plus-above-cloud entry, the cross-down signal exit, the long-only stance, and the 80-bar seed guard — but ships no venue spelling, no timeframe, no fill-timing flag, no position-sizing rule, and no execution-resolution pin. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` spot `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) the hardened completed-bar execution model of Execution assumptions E1–E4 — availability-stamped feature rows, execution resolution pinned to `1h`, decision row T trading the completed bar T−1h, market fills at the decision row's own close (next-bar-close relative to the signal bar), signal exits via StopExecutorAction (the file returns `price=round(curr_close, 4)` — informational metadata echoing the decision bar's own close, never a fill claim; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 120-bar researcher warmup pin (the file carries no position reference; the 120-bar pin covers the file's own 80-bar guard plus margin — an already-positioned book treats same-side entry bars as hold-no-ops, a flat book treats exit bars as no-ops, re-entry re-arms on the next qualifying cross with no cooldown, pre-first-signal and warmup bars flat by pin); (4) the house cost/capital overlay replaces the file's bare `leverage: 1.0` default (the file declares no fee, funding, or margin treatment — the pinned engine's `trade_cost` primitive applies; modeled funding is never reported as realized, and spot carries no funding leg at all). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-23): working-tree filename/content search for `builtin/ichimoku` / `IchimokuStrategy` / `PREBUILT-ICHIMOKU` returns zero strategy records citing this source file or roster leg. The last-100-closed-PR scan returns zero ichimoku attempts. Open `research/*` PRs are only #48 (Larry Williams streak), #49 (Gaussian StochRSI), #63 (SuperTrend flip), #89 (Chandelier Exit), #92 (SSL channel), #251 (Swift 2YMA), #304 (Forven CCI oversold-recross), #331 (AdxSmas cross), #350 (ClucMay72018 BB-discount), #353 (Heracles band-ratio) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a Tenkan/Kijun CROSS edge gated by displaced-cloud position, long-flat, is a different normalized signal from every pool cousin (see Negative evidence 7).

## Economic mechanism

### Source-reported

The source claims only what its sentences print: an Ichimoku Cloud trend-following system that buys when the 9-bar Tenkan-sen crosses above the 26-bar Kijun-sen while price prints above the displaced cloud (Senkou A/B shifted forward 26 bars), and exits when Tenkan-sen crosses back below Kijun-sen. No behavioural, structural, or risk-premium channel is claimed anywhere in the file.

### Research interpretation

Displaced-cloud-gated conversion/base cross machine, long-only, edge-in plus edge-out. Unlike state systems (which stay positioned while one line rides above the other), both legs here are one-bar cross EDGES — a market that crosses up and then rides Tenkan-above-Kijun for fifty bars holds the unit the whole way with no further entry event, and a market that never crosses prints nothing. The 26-bar forward displacement means the cloud filter judges the entry bar against trend geometry computed from data at least 26 bars old: the gate is deliberately stale-side confirmation, not a coincident momentum read. Two asymmetries are stated plainly. First, entry is stricter than exit: longs need the cross AND the above-cloud print, while the exit needs only the cross-down (a cross-down that prints above the cloud still exits). Second, there is no stop, no target, no trailing, and no time exit — a crossed-up leg whose cross-down never arrives is held indefinitely, and a winning leg keeps running with no profit-taking leg. The bet is on displaced-cloud-confirmed conversion/base crosses resolving upward at frozen 9/26/52 geometry on `1h` BTCUSDT spot, not on oscillators, bands, volume prints, calendar effects, or any second timeframe.

## Signal

Exact rule as pinned (any other period, displacement, boundary, edge-vs-state pairing, exit leg, fill, frame, book, or ordering is a different, unpinned rule). The vectorized twin (lines 50–83) is the single source of truth; the scalar (lines 85–145) delegates to it (line 123):

```text
tenkan[t]   = (max(high[t-8..t]) + min(low[t-8..t])) / 2        // 9-bar midpoint, causal
kijun[t]    = (max(high[t-25..t]) + min(low[t-25..t])) / 2      // 26-bar midpoint, causal
senkou_a[t] = ((tenkan + kijun) / 2)[t-26]                      // displaced +26: reads t-26 state, causal
senkou_b[t] = ((max(high52)+min(low52)) / 2)[t-26]              // displaced +26: reads t-26 state, causal
cloud_top[t]= max(senkou_a_eff[t], senkou_b_eff[t])             // NaN legs fall back to close[t] (twin L71-72)
above[t]    = close[t] > cloud_top[t]                           // strict
cross_up[t] = (tenkan[t-1] <= kijun[t-1]) & (tenkan[t] > kijun[t])
cross_dn[t] = (tenkan[t-1] >= kijun[t-1]) & (tenkan[t] < kijun[t])
entry       = cross_up[t] & above[t]                            // enter_long = 1, one-bar edge
exit_sig    = cross_dn[t]                                       // exit_long = 1, one-bar edge, no cloud leg
floor       = len(df) < 80 flat (file guard: senkou_b 52 + kijun 26 + 2, line 97)
```

- Trade events: `cross_up & above_cloud` opens the long unit; `cross_down` closes it in full. Each print is a one-bar edge, not a persistent state — a book already positioned treats further entry-edge bars as hold-no-ops under the position pin, and a flat book treats exit-edge bars as no-ops.
- Exact boundaries (pinned semantics): the cross legs are half-inclusive (`<=`/`>=` on the prior bar, strict `>`/`<` on the decision bar) — a bar with `tenkan == kijun` on both bars fires neither leg; the cloud leg is strict (`>`). Rolling-window NaNs compare False and the twin returns `fillna(False)` (line 83); the scalar additionally refuses below 80 bars (lines 97–100, `price=0.0` metadata). No leg can print before real history accumulates.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `tenkan[t] > kijun[t]` while any signal-exit bar has `tenkan[t] < kijun[t]` — mutually exclusive on every bar, degenerate or otherwise, so entry and signal-exit never co-print. NaN bars print neither. The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere and the scalar hardcodes `direction="long"` (lines 66, 72, 99, 135) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the cross-down signal exit is the complete position-closing set. No take-profit, no stop-loss, no trailing stop, no time limit — explicitly none, not invented; the Execution section configures zero barrier legs so no engine default can add one. No exit leg reads net profit, fees, or funding — fees change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry-edge bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit-edge bars as no-ops; re-entry re-arms on any qualifying cross-up-plus-cloud bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close` through fixed non-negative offsets (rolling maxima/minima plus `.shift(1)`/`.shift(26)`); the 26-bar senkou displacement moves past-computed values to later indices, so the cloud at bar `t` is a function of bars ≤ `t−26` — displacement, never a forward read. No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, volume/`open` read, or stop/limit order argument anywhere in the gating path. The `atr(df, 14)` call in the scalar feeds only the `confidence` metadata number, never a gate.

## Required data

- Completed `1h` bars of BTCUSDT spot: `high`/`low` (Tenkan/Kijun/Senkou construction) plus `close` (cloud-top comparison, NaN fallback, and price metadata). No `open` read, no volume read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (researcher pin following the admitted Forven `1h` siblings — the file names no timeframe). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the decision bar's own completed print); fills land on the decision row's own close under the derived model below.
- Warmup (researcher pin, disclosed): the first 120 one-hour bars held flat. Covers the file's own 80-bar seed guard (52-bar Senkou-B window + 26-bar displacement + 2) with margin for the cross lookback. The file ships no `startup_candle_count` — the 80-bar floor is the file's coded `min_bars` guard, the extra 40 bars are purely a researcher pin, never misattributed. Coded behaviour underneath: rolling windows print NaN until seeded and every NaN comparison is False — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

Pinned engine for every verifiable claim below (each line read this cycle): `hummingbot/hummingbot@fac3a7f8c4adfd9f07f462cfaad9e2ed9e8b6467` — `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` (run/simulation core), `hummingbot/strategy_v2/backtesting/executors_simulator/position_executor_simulator.py` (market-fill and barrier semantics), `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` (candle timestamp semantics). Live Binance kline schema additionally verified by a real `api.binance.com` kline fetch this cycle (row[0] = open time, row[6] = close time, exactly 1h apart on `1h`).

- Research market: BTCUSDT spot on Binance (researcher choice — the source names no venue spelling; the roster pins `_asset BTC`; the `1h` frame follows the admitted Forven `1h` siblings; no source-market equivalence is claimed). Long-only expresses fully on spot. Spot carries no perpetual-funding leg — a stated venue boundary, never hypothetical zero funding reported as realized.
- E1 — availability mapping (researcher pin, stated plainly): engine candle `timestamp` is the bar's OPEN-time label — the REST parser takes `row[0]` (`binance_spot_candles.py` line 82; the live fetch confirms `row[0]` is kline open time and `row[6]` is kline close time), and a bar's high/low/close are complete only at its close time. The derived pipeline therefore stamps every strategy feature row with its AVAILABILITY timestamp (bar close time = open-label + 1h). `prepare_market_data` attaches features to execution rows with `pd.merge_asof(left_on="timestamp_bt", right_on="timestamp", direction="backward")` (engine lines 466–468) and resets `timestamp = timestamp_bt` (line 470), while controller time is set to the row timestamp (line 367). Hence the feature attached at execution row T is exactly the bar that closed at T (bar S = T−1h) — the just-completed bar, never the forming bar. The open label is never claimed as an availability time.
- E2 — resolution and once-per-bar (researcher pin, stated plainly): `backtesting_resolution` is pinned to `"1h"` for this derived evaluation (overriding the `"1m"` default at engine line 224); execution candles are built at that resolution (lines 259–265), so execution rows ARE `1h` bars 1:1 with decision bars — no finer sub-rows exist that could read the attached feature early. The simulation loop evaluates each execution row once (lines 282–284). Entry and signal-exit are mutually exclusive on every bar (proof in Signal), and the single-position pin allows at most one net action per row — no intrabar ordering assumption is needed anywhere.
- E3 — entries: the derived controller issues `CreateExecutorAction` (PositionExecutor, market open-order type — derived, disclosed; the file's `price` field is informational metadata only) on the first execution row T whose attached signal prints the entry edge (completed signal bar S = T−1h). The simulator receives the slice from row T (engine line 287) and, for market orders, fills at `df.loc[start_timestamp, 'close']` with `start_timestamp = df['timestamp'].min()` (simulator lines 15 and 40, both read this cycle) — i.e. the decision row's own close (next-bar-close relative to the signal bar). Close-to-close economics accrue from there minus `2 * trade_cost` round-trip (simulator lines 43–46, 49); the pinned `trade_cost = 0.0002` run default (engine line 225) is the coded cost primitive, with house cost assumptions applied downstream. No maker-touch, queue, or intrabar-path-dependent fill is claimed: the fill price is not known at decision time (true of every market order) and is not claimed to be.
- E4 — exits: zero barrier legs are configured (`take_profit` None, `stop_loss` None, no trailing, no time limit — matching the file's complete absence of risk legs), so the barrier scan can produce no TP/SL touch (simulator lines 57–66) and no TP/SL tie-break can arise. The derived controller issues `StopExecutorAction` on the first execution row R whose attached signal prints the exit edge; the engine terminates the executor `EARLY_STOP` at that row's timestamp and books the slice economics through R (engine lines 290–291 and 568–599, read this cycle). No intrabar extreme can pre-empt the signal exit because no barrier exists to trigger on one.
- E5 — sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept (its `leverage: 1.0` default is replaced by the spot pin) — sizing and costs ride the explicit house overlay with the pinned engine cost primitive above, under the single-unit/no-add position pin from Signal, so position events are fully determined by the edge legs above and sizing changes no event, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the cross-up-plus-cloud edge opens the full unit on a flat book; the cross-down edge closes it in full; re-entry after an exit needs only the next qualifying edge bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (the 9/26/52 rolling-midpoint block, the 26-bar senkou displacement legs, the half-inclusive cross-up/cross-down edges, the strict above-cloud gate with close-fallback, the `PREBUILT-ICHIMOKU` roster leg, the 80-bar seed guard, and the `IchimokuStrategy(BaseStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare False and the twin returns `fillna(False)` (twin has no length guard of its own — the `False` fill IS the guard); the scalar additionally refuses below 80 bars. The 120-bar record-rule floor holds every pre-seed bar flat on top — disclosed, not repaired. The file ships no `startup_candle_count`, so the extra 40 bars are purely a researcher pin, never misattributed.
2. Displacement-causality fence: `.shift(26)` on the senkou spans moves past-computed midpoints to later indices — the cloud at bar `t` is a function of bars ≤ `t−26`. This is backward displacement, never a forward read: no negative shift, no `.iloc[-1]`-anchored future window, no second timeframe ships anywhere. Removing the displacement (or lengthening it) would be a different, unpinned rule.
3. Twin/scalar parity fenced: both compute the identical 9/26/52 block with identical NaN→close fallback (twin lines 70–73; scalar lines 116–117) and the scalar's booleans come from the twin (line 123). The scalar-only extras (`atr` number, `confidence` formula, `indicators` dict, `price` rounding, `name`/`describe` strings) are metadata only — none feeds any gate, and the record's fills come from the engine lines in E3, never from the file's `price` field.
4. Dead-search-surface fence: `parameter_space` (lines 147–152) and `compatible_regimes` (lines 38–40) are never read by any gating line — this record pins the defaults and exercises no search and no regime branch. Any non-default period triple is a different, unpinned rule.
5. `atr`/confidence fence: `atr(df, 14)` enters only through the scalar's line-86 import and exits only through the confidence number (lines 127, 143) — thresholding, gating, or reporting on it would be a different, unpinned rule. Confidence 0.0-vs-nonzero changes no event.
6. No-edge-substitution fence: the file contains zero `crossed_*` helpers and zero state legs — both signal legs are inline half-inclusive cross edges on the decision bar's own Tenkan/Kijun prints. Converting either leg to a persistent state (or vice versa) would be a different, unpinned rule with different trade events.
7. Cousin records fenced as different constructions (none trades a Tenkan/Kijun cross edge gated only by displaced-cloud position, long-flat, on `1h` spot): the admitted `ichimoku-rsi-gated-reversal` pool-mate trades a four-leg Pine AND (Tenkan/Kijun STATE, Chikou momentum vs close-25, Kumo position, RSI-14 50-gate) two-sided on `1d` from a different source — a market that crosses up above the cloud with RSI above 50 fires an entry here but nothing there; a market riding Tenkan-above-Kijun state with no fresh cross fires entries there but nothing here; the admitted `ichimoku-cloud-adx-trend-filter` pool-mate adds a DMI/ADX triple gate from the same Coinrule family; the admitted `octa-ema-ichimoku-trend-long` pool-mate is an EMA-ribbon system with an Ichimoku-variant filter and no cross edge at all. Not a threshold re-tuning of any of them: moving any period, dropping the displacement, adding any Chikou/RSI/ADX leg, converting either edge to a state, or changing the frame, sides, or exits would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: every other file in `forven/strategies/builtin/` (including the same-night `donchian`, `supertrend`, `awesome_oscillator`, `adx_trend`, `orb`, and `rsi_momentum` attempts, all closed unmerged) is a separate pin — their constants, legs, exits, frames, and risk postures must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-spot market/`1h` frame pin, the E1–E5 execution model (availability-stamped features, pinned `1h` execution resolution, decision-row-T/next-bar-close fills, StopExecutorAction exits, zero barrier legs), the single-unit/no-add/no-cooldown position pin, the 120-bar warmup floor, and house sizing/costs — all predeclared above. The 9/26/52 construction, the 26-bar displacement, the half-inclusive cross edges with all their literals and strictness, the strict above-cloud gate with close-fallback, the cross-down-only exit, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 9/26/52 periods / 26-bar displacement / half-inclusive cross edges / strict above-cloud gate / cross-down-only exit / single-unit long-only / `1h` BTCUSDT spot / decision-row-T fills are frozen.

- F1 — Cloud-gate relevance: entering on every Tenkan/Kijun cross-up without the above-cloud conjunct (same exit otherwise) must not improve net expectancy; fail ⇒ the coded cloud filter adds nothing over its unfiltered twin.
- F2 — Edge-vs-state relevance: entering on the Tenkan-above-Kijun persistent state plus above-cloud (instead of the one-bar cross edge, same exit otherwise) must not improve net expectancy; fail ⇒ the coded edge adds nothing over its state twin.
- F3 — Signal-vs-exposure relevance: buy-and-hold over the same evaluation span (same fills, no signal legs) must not improve net expectancy; fail ⇒ the cross system adds nothing over blind exposure.

## Crypto portability

BTCUSDT spot `1h` is the research pin (source names no market or venue; roster pins `_asset BTC`). Long-only with full-unit open/close expresses unchanged on any spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame plus a fixed 26-bar displacement, portable across 24/7 crypto tape. The rule reads completed-bar `high`/`low`/`close` only, so venue volume-definition differences cannot move any leg (no volume read exists to differ). Funding is not read, not modelled as realized, and not needed — spot has no funding leg. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the file returns `price=round(curr_close, 4)` as informational metadata — this record never claims it as a fill. Fills are the decision row's own close per the pinned market-fill lines (E3), i.e. next-bar-close relative to the signal bar; backtest economics of the timings differ from any live/limit-order behaviour by construction — the adaptation is disclosed, not hidden. Any live/limit-order/queue behaviour is out of scope.
- Derived market/frame pin: the file names no symbol, venue, or timeframe — BTCUSDT spot on `1h` is a researcher choice for the house universe, never a source claim.
- Signal-only risk: there is no stop, no target, no trailing, and no time exit — a leg whose cross-down never arrives is held indefinitely (a gap through any hypothetical level changes nothing, since no level exists); a winning leg keeps running with no profit-taking leg. This is the coded posture, disclosed as the record's principal risk.
- Stale-cloud gate: the cloud filter judges each entry bar against trend geometry computed from data ≥ 26 bars old — late-cycle crosses that arrive after the cloud has already flipped back print nothing; whipsaw of the Tenkan/Kijun pair around equality can exit and re-enter across consecutive bars, disclosed as the principal friction.
- Source economics are runtime-default-only: beyond the pinned engine `trade_cost` primitive the file ships no capital sizing, no slippage, no funding, and no margin assumption — derived evaluation must carry the full house cost load (fees; spot has no funding leg), and this record reports no net performance of its own. The file carries no performance figure, so no figure is kept or transferred.
- Seed bars: the 52-bar window plus 26-bar displacement dominate early bars; the first 120 `1h` bars are flat by record rule, so early-history signals never enter any evaluation.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/judder659/Forven/blob/8e79afa86e6f80a7f5a83eb50742059a9215ca6a/forven/strategies/builtin/ichimoku.py
- https://github.com/judder659/Forven
