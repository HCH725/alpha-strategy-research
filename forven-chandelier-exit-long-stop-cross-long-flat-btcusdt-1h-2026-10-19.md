---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven chandelier-exit long-stop cross long-flat on BTCUSDT 1h bars
created: 2026-10-19
updated: 2026-10-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/chandelier_exit.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven chandelier-exit long-stop cross long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-engulfing-body-cover-volume`, `forven-stddev-cross-swing`, `forven-hma-cross`, `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, and twenty-eight other admitted Forven records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`, verified via the GitHub commits API this cycle; verified as the repository HEAD via `git ls-remote` against both `HEAD` and `refs/heads/main` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/chandelier_exit.py`.
- GitHub blob SHA at the pinned commit: `6cd475fcc393ae86bf1196e9210db57044b330dd`, size 4752 bytes.
- Byte-identity check: the file retrieved from `raw.githubusercontent.com` at the pinned commit is 4752 bytes, 150 lines, SHA-256 `b77f00c650c85f729b7920eff6038a37b2776a325fbcd8989b1915ce81725d2f`, and `git hash-object` reproduces the GitHub blob (`6cd475f…b330dd`) — the entire file was retrieved twice and inspected (both fetches byte-identical).
- Registration: the file self-registers via `STRATEGY_CLASS = ChandelierExitStrategy` (line 146), `TYPE_NAME = "chandelier_exit"` (line 12), and the `STRATEGIES = [("PREBUILT-CHANDELIER", ChandelierExitStrategy, {"_asset": "BTC"})]` roster pin (lines 148–150). Repo-wide, no other builtin file carries this `TYPE_NAME` or roster name; working-tree search for `builtin/chandelier` / `PREBUILT-CHANDELIER` / `ChandelierExitStrategy` / `TYPE_NAME = "chandelier_exit"` returns zero strategy records citing this source file.
- The file's own words (quoted for gate evidence, never extended): module docstring `Chandelier Exit strategy.` with `Entry: price rises above highest_high - atr_mult * ATR (uptrend start)` and `Exits: price falls below highest_high - atr_mult * ATR (trailing stop hit)` (lines 1–6); class docstring `The chandelier exit hangs a stop-loss from the highest high of the lookback period at a distance of atr_mult * ATR. Entry is signalled when price crosses above the chandelier line (new uptrend) and exit fires when price crosses below it (stop hit).` (lines 16–22); `describe()` returns `Chandelier stop at highest_high(22) - 3.0 * ATR(22). Enters when price crosses above the stop (uptrend). Exits when price crosses below it (stop hit).` (lines 52–59, with defaults); `default_params` returns exactly `{ "atr_period": 22, "atr_mult": 3.0, "lookback": 22, "leverage": 1.0 }` (lines 40–46); `compatible_regimes` returns `{"TREND_UP"}` (lines 48–50, metadata never read by the signal path); `parameter_space()` returns `{ "atr_period": (14, 28, 2), "atr_mult": (2.0, 4.0, 0.5), "lookback": (14, 28, 2) }` (lines 138–143, a documented search surface only — this record pins the defaults and runs no search). No performance phrase of any kind ships anywhere in the 150 lines — this record adopts no source-reported performance (see Evidence).
- Single decision path, verified complete: `generate_signal()` (lines 61–136) is the sole signal method — no `generate_signals` vectorized twin exists anywhere in the 150 lines, so no twin-selection ambiguity exists. The method pins its constants (`atr_period` 22, `atr_mult` 3.0, `lookback` 22, lines 63–65), applies its own short-frame guard (lines 70–79), builds the True Range and its rolling-mean ATR in-file (lines 81–92), builds the highest-high and both chandelier lines in-file (lines 94–100), reads the last two closes against the last two long-line prints (lines 102–108), evaluates the cross-above entry and cross-below exit on the single long line (lines 110–114), and returns a single `Signal` (lines 124–136).
- Zero out-of-file indicator dependencies: the file imports only `pandas` and `forven.strategies.base` (lines 8–10). No `forven.strategies.indicators` facade import exists — the ATR is hand-rolled True-Range arithmetic with a plain rolling mean (line 92), never Wilder RMA, never a shared helper; no `rsi`/`stoch`/`ema`/`adx`/`macd`/`supertrend` call conditions any order line (there is nothing to fence here).
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (12238 bytes, blob `27508a2a6b8c546e21adefdb97fc0144fabf881b`, identical to the blob pinned by the admitted `forven-engulfing-body-cover-volume`, `forven-rsi-s00139`, `forven-bb-edge-fade-reclaim`, and `forven-stddev-cross-swing` records) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults, `direction: str = "long"` default, plus `__post_init__` coercion and `_normalize_signal_direction` mapping the `"long"` literal back to `"long"` — the short-frame guard (lines 72–79, side `"long"`) therefore resolves to `"long"` on every pre-guard bar, and the live `direction = "long"` literal (line 116) survives untouched on every evaluated bar.
- Full-file token census (verified by search over the 150 lines this cycle): `direction` occurs exactly three times (guard line 76 literal `"long"`, live line 116 literal `"long"`, constructor line 128 passing the variable — no short leg exists anywhere); 0 `sell` / 0 `stop=` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` as order arguments (the words `stop`/`stop-loss`/`stop hit` occur only inside prose docstrings and the `describe()` sentence, never as an order leg); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default, replaced by the house overlay — see Execution assumptions); 0 `funding` / 0 `mark_price` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any line; 0 `rsi` / 0 `ema` / 0 `adx` / 0 `vwap` / 0 `stoch` / 0 `macd` / 0 `supertrend` / 0 `ichimoku` (no smoothing beyond the hand-rolled ATR mean, no regime filter, no second indicator); 0 `open` / 0 `volume` reads (the rule consumes `close`/`high`/`low` only — lines 66–68 are the sole `df[` reads); 0 `isna` / 0 `isnull` / 0 `nan` guards (NaN behaviour disclosed in Negative evidence 3, never invented); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` / 0 `cooldown` (no position-aware state conditions any signal); `len(df)` occurs exactly once (the line-71 guard — the file's own warmup floor, adopted verbatim, never invented).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the 22-bar highest-high anchor, the 22-bar hand-rolled SMA-ATR scaled by 3.0, the single-line cross-above entry and cross-below exit, the long-only stance, the no-stop posture, and its own 24-bar short-frame guard — but ships no venue spelling, no timeframe, no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the thirty-plus admitted Forven records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit position pin with hold-no-op semantics with the source's own 24-bar guard adopted verbatim as the warmup floor (an already-positioned book treats further cross-above bars as hold-no-ops, a flat book treats cross-below bars as no-ops, re-entry re-arms on any qualifying cross-above bar after any exit with no cooldown, pre-guard bars flat by the source's own rule — see Signal); (4) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal).

Pre-write dedup (2026-10-19): working-tree filename/content search for `builtin/chandelier` / `PREBUILT-CHANDELIER` / `ChandelierExitStrategy` returns zero strategy records — no record cites this source file. The word `chandelier` occurs in the pool only inside open-PR fence mentions of PR #89 (see Negative evidence 6), never as an admitted mechanism. No open `research/*` PR carries this source file (open PRs are only #48/#49/#63/#89/#92/#251/#304 — different mechanisms, indicators, and sources; #89 is fenced as a different construction in Negative evidence 6). Not a duplicate, paraphrase, or trivial parameter variant: a single-line high/low-extremum SMA-ATR cross machine is a different signal construction from a dual-ratcheted close-extremum Wilder-ATR priority state machine — different anchor × different estimator × different trigger logic × different frame × different immutable source file.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: a `Chandelier Exit ATR-based trailing stop strategy` where `Entry is signalled when price crosses above the chandelier line (new uptrend) and exit fires when price crosses below it (stop hit)`, with the line hung `from the highest high of the lookback period at a distance of atr_mult * ATR`. No behavioural, structural, or risk-premium channel is claimed anywhere in the 150 lines. The file ships no backtest numbers of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Volatility-scaled extremum-reclaim entry, long-only, state-holding. The system buys only the exact bar the close crosses back above a trailing line hung 3 ATRs beneath the 22-bar highest high — unlike raw-breakout systems, a fresh-range high that never lost the line fires nothing, and unlike oscillator systems, no momentum rotation can trigger anything: only a close through the volatility line flips state. The exit is the same line crossed the other way, so the stop is the trailing risk line and the entry trigger in one object. The failure mode is plain: a V-turn that bottoms more than 3 ATRs under the old high enters strictly late (the line must first decay or the high must reset), chop that flickers across the line whipsaws the book with no stop and no cooldown, and a position in a grinding advance is held with no profit-taking leg until the line itself is crossed.

## Signal

Exact rule as pinned (any other anchor, estimator, multiple, window, trigger polarity, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own; `generate_signal` (lines 61–136) is the single source of truth — no second decision logic exists:

```text
inputs (defaults, frozen): atr_period = 22, atr_mult = 3.0, lookback = 22
TR_t   = max(high_t - low_t, |high_t - close_{t-1}|, |low_t - close_{t-1}|)  // lines 82-90
ATR_t  = mean(TR over the last 22 bars ending at bar t, plain rolling mean) // line 92
HH_t   = max(high over the last 22 bars ending at bar t)                    // line 95
CL_t   = HH_t - 3.0 * ATR_t   // single long line, lines 94-96
entry  = (close_{t-1} <= CL_{t-1}) AND (close_t > CL_t)    // line 111
exit_  = (close_{t-1} >= CL_{t-1}) AND (close_t < CL_t)    // line 114
```

- Guard (source-verbatim): `len(df) < 24` (line 70–71, `max(atr_period, lookback) + 2`) returns the explicit no-signal guard (lines 72–79, side resolved to the base `"long"` default); pre-guard bars are flat by the source's own rule, adopted verbatim as the warmup floor (see Required data). The guard returns the unrounded `float(close.iloc[-1])` (line 75) while the live path returns `round(curr_close, 4)` (line 127) — price-field formatting only, never an order-gating input.
- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (hardcoded literal on the live path line 116, base default on the guard path — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. Both legs are edge crosses (fire once on the crossing bar — refires require a fresh cross back through the line), not level holds; treating either leg as a level-hold would be a different, unpinned rule.
- Mutual-exclusion proof (no tie-break pin required): entry requires `close_t > CL_t` while exit requires `close_t < CL_t` on the same two prints — the strict close-vs-line inequalities are pairwise opposite, unsatisfiable on every bar. A touch (`close_t == CL_t`) fails both strict conjuncts and fires nothing; a shared prior-bar equality (`close_{t-1} == CL_{t-1}`) satisfies both prior conjuncts yet the current-bar conjuncts remain contradictory. The reviewer is never asked to invent an ordering.
- Exits and risk (explicit): the cross-below of the same long line is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence` (lines 118–122, ATR-distance ratio guarded by `curr_atr > 0`) and the `indicators={chandelier_long, chandelier_short, highest_high, atr}` dict (lines 130–135) are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying cross-above bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close`/`high`/`low` with fixed non-negative offsets (last two closes against the last two line prints, plus trailing 22-bar windows ending at the decision bar), exact cross comparisons, and one guarded division (`curr_atr > 0` before the confidence ratio — no division-by-zero; the order legs divide nothing). No `request.*`, `security()`, `timeframe*`, `barstate.*`, `open`/`volume` read, EMA/RMA/WMA/RSI/MFI/ADX/Stochastic/MACD/Supertrend smoothing, session/calendar call, or stop/limit order argument exists anywhere in the file (verified by the census above returning zero matches). The `compatible_regimes == {"TREND_UP"}` set is metadata never read by the signal path (which takes only `df`/`params` for the three pinned literals), so no regime model gates any order. Substituting Wilder-RMA smoothing, close extremums, a dual-line state machine, or any second gate would be a different, unpinned rule.
- Warmup: 30 completed `1h` bars flat by record rule — structural minimum is the 24th completed bar (22-bar ATR seed plus the 22-bar extremum window plus the source's own `max + 2` guard — plus margin). Pre-warmup bars are flat by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (every window reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Required data

- `close`/`high`/`low` on `BTCUSDT` `1h` completed bars only (sole reads: lines 66–68; `high`/`low` enter the True-Range arithmetic and the highest-high/lowest-low windows, `close` enters the TR gaps and both cross comparisons). No `open`, no `volume`, no external feed, no funding/OI/mark-price leg, no calendar, no multi-asset input.
- Warmup: 30 completed `1h` bars flat by record rule (structural minimum the 24th completed bar — 22-bar ATR seed plus the 22-bar extremum window plus the source's own guard — plus margin).
- Point-in-time: every window is trailing over completed bars ending at the decision bar (the extremum/ATR windows are unshifted but the decision bar is completed before evaluation — no future bar, no unfinished-bar read, no repainting); the decision bar's own `close` is both the last input and (via the derived same-bar-close pin, `price=round(curr_close, 4)`) the fill price basis.

## Execution assumptions

- Derived lane (all four pins predeclared in Provenance): `BTCUSDT` `1h`, completed-bar decisions with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), single-unit position with hold-no-op semantics, house sizing/capital/costs replacing the bare `leverage: 1.0` default.
- Pinned-engine path (same lane primitive as the thirty-plus admitted Forven siblings on this exact repository family): the pinned Hummingbot package `20260920` / `dev-2.17.0` backtest model prices one market order at the decision bar's own close on `BTCUSDT` `1h` with declared house fees/funding/slippage overlay; single-line extremum-minus-ATR cross arithmetic over completed `close`/`high`/`low` on a single frame with same-bar-close fills is the already-verified subset for this family — no new execution primitive, no multi-asset synchronization, no shared-capital contention, no lower-timeframe alignment, no non-OHLCV input, no next-open/maker/intrabar fill is required by this record.
- Sizing/capital (stated plainly to the #89 precedent): the admitted version trades exactly one fixed unit — a flat book enters one unit on an entry bar, a long book exits the whole unit on an exit bar, same-direction refires are hold-no-ops, no pyramiding, no averaging, no safety orders, no cooldown. The downstream house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus modeled funding/slippage with explicit limitations; modeled funding is never reported as realized funding) apply to the derived evaluation here and change no trade event under the predeclared single-unit rule — DCA is a downstream execution experiment, never an admission leg of this version. No capital-dependent forced-close state beyond the standard isolated-margin accounting is admitted.
- No stop/limit/trailing/time leg is modelled because none exists in source — explicitly disabled, never defaulted. Missing trade prices are never fabricated (pre-warmup and missing bars stay flat).

## Evidence

### Source-reported

The source ships the full construction (frozen `atr_period 22` / `atr_mult 3.0` / `lookback 22` inputs with a hand-rolled True-Range rolling-mean ATR, 22-bar highest-high anchor, single-line cross-above entry and cross-below exit, fixed long-only stance with the literal `"long"` direction token, no risk legs) and the `PREBUILT-CHANDELIER` BTC roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No twin-signal ambiguity: full-file search returns exactly one `def generate_signal` and zero `def generate_signals` — there is no second decision path to select between.
2. No out-of-file indicator risk: the file's imports are `pandas`/`base` only — the ATR is hand-rolled True-Range truth plus a plain rolling mean (lines 81–92), so no facade-resolved estimator variant exists to pin or fence.
3. NaN determinism, stated plainly: the file ships no `isna` guard (verified zero matches), so a `NaN` line print or ATR print can only meet the strict cross inequalities as `False` on both legs — NaN bars emit no signal by construction, never a spurious order. On complete data the 24-bar guard already covers both 22-bar seeds, so no NaN reaches any order line in the admitted configuration; missing bars stay flat and are never fabricated.
4. Equality boundaries fire nothing: both legs use strict `<` / `>` on the current-bar comparison (lines 111/114); a close that merely touches the line holds the prior state by construction. The `<=` / `>=` prior-bar conjuncts admit touch equality only as a setup, never as a standalone trigger.
5. Same-bar double-fire is impossible (mutual-exclusion proof in Signal) — no ordering assumption, invented or otherwise, is required.
6. Open-PR fence (#89 FMZ Chandelier), stated plainly: PR #89 carries FMZ 437792 (ChaoZhang) — close-extremum anchors (`ta.highest(close, 22)` / `ta.lowest(close, 22)`), Wilder-RMA `ta.atr(22)`, dual one-sided-ratcheted stop lines with a priority-ordered `dir` state machine and flip-only triggers, derived `1d` frame. This record trades high/low-extremum anchors with a hand-rolled SMA rolling-mean ATR, a single unratcheted long line with direct cross triggers and no state variable, on derived `1h` bars, from immutable file `builtin/chandelier_exit.py` — different anchor × different estimator × different trigger logic × different frame × different immutable source file. This record is therefore never evidence for that rule, and that record is never this rule's provenance.
7. Pool trailing-stop cousins fenced, stated plainly: `ut-bot-atr-trailing-stop-flip` (two-sided ATR-band flip), `psar-flip-stop-reverse` (parabolic-SAR flip), the two Alorse SuperTrend records (median-`hl2`-anchored SuperTrend bands with RSI/StochRSI gates), and `alphatrend-mfi-atr-trailing-reversal` (Alphatrend-plus-MFI construction) each trade a different stop arithmetic, a different smoothing, or a different direction handling — none evaluates a single highest-high-minus-3×SMA-ATR line with long-flat cross triggers.
8. Pool breakout cousins fenced, stated plainly: `donchian-20-10-breakout` (raw prior-20-high breakout entry with a prior-10-low exit) and the ATR/breakout siblings fire on the raw extremum itself; this record fires only on the cross of the extremum-minus-volatility line — a V-recovery that reclaims the line without printing a fresh 22-bar high trades here and fires nothing there, so the trade-event sets differ by construction.
9. Variant menus fenced, stated plainly: the `parameter_space()` surface (`atr_period` 14–28, `atr_mult` 2.0–4.0, `lookback` 14–28) is a documented search grid the code never runs — this record freezes the `22/3.0/22` defaults as written; adopting any grid point, switching to Wilder smoothing, switching extremums to closes, or adding a ratchet/state machine would each be a different, unpinned rule.
10. Diagnostic quarantine, stated plainly: `chandelier_short`, `lowest_low`, `highest_high`, `atr`, `confidence`, and the `compatible_regimes == {"TREND_UP"}` set are computed into the indicators dict, the confidence field, or class metadata and read by zero order-gating comparisons — treating any of them as a gate, filter, exit leg, or sizing input would be a different, unpinned rule.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `22/3.0/22` single-line high/low-extremum SMA-ATR cross / long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Line relevance: replacing the extremum-minus-ATR line cross with the raw 22-bar highest-high breakout (same cross-below-line exit) must not improve net expectancy on the frozen 42-cell campaign; fail ⇒ the volatility offset adds nothing over the bare breakout.
- F2 — Anchor relevance: replacing high/low extremums with close extremums (same SMA-ATR arithmetic, same triggers) must not improve net expectancy; fail ⇒ the wick-anchored construction adds nothing over its close-anchored twin.
- F3 — Estimator relevance: replacing the hand-rolled SMA rolling-mean ATR with Wilder-RMA ATR (same anchors, same multiple, same triggers) must not improve net expectancy; fail ⇒ the pinned estimator carries no advantage over the classic smoother.

## Crypto portability

Direct: `BTCUSDT` perpetual/spot `1h` OHLCV on Binance — the rule consumes completed-bar `close`/`high`/`low` only, needs no venue-specific microstructure, no funding input, and no spot-vs-perp distinction in its arithmetic. The long-only no-stop posture expresses fully on spot; perps add no required leg. House costs (fees/funding/slippage) are overlaid downstream per the research campaign; modeled funding is never reported as realized funding.

## Limitations

- Late entries by construction: the line hangs up to 3 ATRs under the 22-bar high, so V-turns that bottom far beneath the old high enter strictly after the recovery is underway — disclosed lag profile.
- Chop whipsaw: closes that flicker across the line print repeated enter-then-exit round trips with no cooldown and no structural filter — disclosed chop profile.
- No risk leg: no stop loss, take profit, trailing-stop order, or time limit exists in source — recorded as explicitly disabled; adverse excursions after a cross-above entry have no capital guardrail besides the eventual cross-below print.
- No profit-taking disposition: a grinding advance is held with no target — the line cross is the sole exit and there is no time stop; opportunity cost accrues, disclosed.
- Single-market scope: derived pin is `BTCUSDT` `1h` only; portability to other symbols/timeframes is untested and claimed nowhere in this record.
- Research overlay dependence: fills, sizing, and costs follow the derived lane pins and the downstream house model — not the source engine's own semantics.

## Implementation status

`not-implemented` — no dedicated Qlib/Hummingbot executable artifact exists for this record. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream refusal; if formally selected for execution without a reproducible recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline stage), never a second admission flag.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write is performed by the Scout lane.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/chandelier_exit.py (primary source — executable Python strategy, 150 lines, fetched live 2026-10-19 at pinned HEAD commit, 4,752 bytes, SHA-256 `b77f00c650c85f729b7920eff6038a37b2776a325fbcd8989b1915ce81725d2f`, blob `6cd475f…b330dd`; no performance figure ships anywhere in the file)
- https://github.com/judder659/Forven (repository context; pinned HEAD `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` verified this cycle)
- `forven/strategies/base.py` at the same commit (supporting semantics — `Signal` defaults and direction normalization, 12,238 bytes, blob `27508a2a…fabf881`, identical to the blob pinned by admitted sibling records)
