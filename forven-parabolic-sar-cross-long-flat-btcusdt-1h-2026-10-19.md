---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven parabolic-SAR cross long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/parabolic_sar.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven parabolic-SAR cross long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-chandelier-exit-long-stop-cross`, `forven-engulfing-body-cover-volume`, `forven-stddev-cross-swing`, `forven-hma-cross`, `forven-zscore-mean-reclaim`, `forven-ttm-squeeze-momentum-release`, and thirty other admitted Forven records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`, verified via the GitHub commits API this cycle; verified as the repository HEAD via `git ls-remote` against both `HEAD` and `refs/heads/main` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/parabolic_sar.py`.
- GitHub blob SHA at the pinned commit: `2e6b70e74b28031aaec4fe3a5d4a42f51f223f4f`, size 5158 bytes.
- Byte-identity check: the file retrieved from `raw.githubusercontent.com` at the pinned commit is 5158 bytes, 161 lines, SHA-256 `f2420bf2e823d4207f307c8dd2d38c4998818421bd5efc940f92b7bf3e7b359f`, and `git hash-object` reproduces the GitHub blob (`2e6b70e7…223f4f`) — the entire file was retrieved twice and inspected (both fetches byte-identical, matching the earlier directory-listing fetch).
- Registration: the file self-registers via `STRATEGY_CLASS = ParabolicSARStrategy` (line 159), `TYPE_NAME = "parabolic_sar"` (line 9), and the `STRATEGIES = [("TOMB-SAR", ParabolicSARStrategy, {"_asset": "BTC"})]` roster pin (line 161). Repo-wide, no other builtin file carries this `TYPE_NAME` or roster name; working-tree search for `TOMB-SAR` / `parabolic_sar` / `ParabolicSARStrategy` returns zero strategy records citing this source file.
- The file's own words (quoted for gate evidence, never extended): module docstring `Parabolic SAR strategy.` (line 1); `describe()` returns `Trend following using Parabolic SAR (step 0.02, max 0.2).` (lines 106–108, with defaults); `default_params` returns exactly `{ "step": 0.02, "max_step": 0.2, "leverage": 3.0 }` (lines 98–100); `compatible_regimes` returns `{"TREND_UP", "TREND_DOWN"}` (lines 102–104, metadata never read by the signal path); `parameter_space()` returns `{ "step": (0.01, 0.05, 0.01), "max_step": (0.1, 0.3, 0.1) }` (lines 155–156, a documented search surface only — this record pins the defaults and runs no search). No performance phrase of any kind ships anywhere in the 161 lines — this record adopts no source-reported performance (see Evidence).
- Twin decision paths, verified lockstep: `generate_signal()` (lines 110–139, per-bar) and `generate_signals()` (lines 141–153, vectorized) both consume the single in-file `parabolic_sar_series()` helper (lines 28–82). The per-bar path reads `sar.iloc[-1]` / `sar.iloc[-2]` against `close.iloc[-1]` / `close.iloc[-2]`; the vectorized path reads the same series with `close.shift(1)` / `sar.shift(1)` plus `.fillna(False)`. For every frame with `len > 1`, `iloc[-2]` ≡ `shift(1)` row-for-row and the entry/exit booleans are algebraically identical; on degenerate frames the per-bar `len(df) < 3` guard returns all-`False` and the vectorized shift-NaN rows resolve to `False` via `fillna(False)`. No third path, no facade import, no sibling-module import anywhere in the file. This record pins the per-bar `generate_signal` as canonical and the twin as lockstep-equivalent — never two rules to choose between.
- Zero out-of-file indicator dependencies: the file imports only `pandas` and `forven.strategies.base` (lines 5–7). No `forven.strategies.indicators` facade import exists — the SAR is a self-contained explicit recursion loop (lines 28–82), never a shared-helper estimator variant; no `rsi`/`stoch`/`ema`/`adx`/`macd`/`supertrend`/`vwap`/`atr` call conditions any order line (there is nothing to fence here).
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (12238 bytes, blob `27508a2a6b8c546e21adefdb97fc0144fabf881b`, identical to the blob pinned by the admitted `forven-chandelier-exit-long-stop-cross`, `forven-zscore-mean-reclaim`, `forven-ttm-squeeze-momentum-release`, and `forven-bb-squeeze-breakout` records) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults, `direction: str = "long"` default, plus direction normalization mapping the `"long"` literal back to `"long"`.
- Full-file token census (verified by search over the 161 lines this cycle): `def generate_signal` occurs exactly twice (`generate_signal` + `generate_signals`, the lockstep twins above — no third path); `direction` occurs exactly twice (guard line 118 literal `"long"`, live line 136 literal `"long"` — no short leg exists anywhere, verified 0 `short` tokens in the entire file); `long` occurs exactly twice (the same two literals); 0 `sell` / 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` anywhere in the 161 lines (no stop/trailing order leg exists, not even in prose); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 3.0` default, replaced by the house overlay — see Execution assumptions); 0 `funding` / 0 `mark_price` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any line; 0 `rsi` / 0 `ema` / 0 `adx` / 0 `vwap` / 0 `stoch` / 0 `macd` / 0 `supertrend` / 0 `ichimoku` / 0 `atr` / 0 `rolling` / 0 `ewm` (the SAR is a raw high/low loop — no smoother, no second indicator, no regime filter); 0 `open` / 0 `volume` reads (the rule consumes `high`/`low`/`close` only — lines 33–35, 111, and 145 are the sole `df[` reads); 0 `isna` / 0 `isnull` guards (NaN behaviour disclosed in Negative evidence 3, never invented); 0 `pyramid` / 0 `position_` / 0 `opentrades` / 0 `cooldown` (no position-aware state conditions any signal); `.shift(` twice plus `.fillna(` once (vectorized twin only); `len(df)` occurs exactly once (the line-113 guard).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the self-contained SAR recursion, the `0.02/0.2` AF pair, the cross-above entry and cross-below exit on the same SAR line, the long-only stance, the no-stop posture, and its own 3-bar short-frame guard — but ships no venue spelling, no timeframe, no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the thirty-plus admitted Forven records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit long-flat position pin with hold-no-op semantics plus a 30-bar researcher warmup floor (an already-positioned book treats further cross-above bars as hold-no-ops, a flat book treats cross-below bars as no-ops, re-entry re-arms on any qualifying cross-above bar after any exit with no cooldown, pre-warmup bars flat by record rule — the floor covers the source's 3-bar guard plus the SAR AF/EP seeding transient in one disclosed rule; see Required data); (4) house sizing/capital/costs replacing the bare `leverage: 3.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal).

Pre-write dedup (2026-10-19): working-tree filename/content search for `TOMB-SAR` / `parabolic_sar` / `ParabolicSARStrategy` returns zero strategy records — no record cites this source file. The word `parabolic` occurs in the pool only inside the admitted `psar-flip-stop-reverse` record and `chop-zone` prose/fences (see Negative evidence 6–7 for the multi-axis fence against both). No open `research/*` PR carries this source file (open PRs are only #48/#49/#63/#89/#92/#251/#304 — different mechanisms, indicators, and sources; #63 SuperTrend and #89 Chandelier are fenced as different stop arithmetics in Negative evidence 8). Not a duplicate, paraphrase, or trivial parameter variant: a self-contained AF-ratcheted extreme-point SAR cross machine traded long-flat on `1h` bars is a different position-state machine from an always-in two-sided SAR reversal on `1d` bars — different direction handling × different exposure posture × different frame × different immutable source file.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: `Parabolic SAR strategy.` / `Trend following using Parabolic SAR (step 0.02, max 0.2).` — an accelerating trailing-dot trend follower with a cross-above entry and a cross-below exit. No behavioural, structural, or risk-premium channel is claimed anywhere in the 161 lines. The file ships no backtest numbers of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Accelerating-stop cross timing, long-only, state-holding. The SAR dot starts far from price and accelerates toward it as the trend extends (AF stepping 0.02 → 0.20 cap, extreme point ratcheting each bar with a two-bar low/high clamp), so a close crossing from below to above the dot reads as trend-start confirmation in a single event, and the cross back below is the entire risk control. Unlike channel-flip records (Donchian/Hilo/SuperTrend), the trail is not a fixed-lookback extreme or a volatility multiple: it is path-dependent, accelerating with trend age and resetting to the prior extreme on every flip, so whipsaw cost concentrates in sideways markets (rapid cross pairs) while trending markets ride one side with a tightening implicit stop. Unlike its admitted always-in SAR sibling (which reverses short on every down-flip and never rests flat), this machine exits to flat and sits out downtrends entirely — flat is a first-class state, and the short side is explicitly disabled, never merely untriggered. The failure mode is plain: chop that flickers across the dot whipsaws the book with no stop and no cooldown; a vertical advance that never prints a cross-below is held with no profit-taking leg; a grinding decline is watched from flat with no short participation by construction.

## Signal

Exact rule as pinned (any other AF value, clamp, seed, trigger polarity, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own; `parabolic_sar_series` (lines 28–82) is the single construction both twins share:

```text
inputs (defaults, frozen): step = 0.02, max_step = 0.2
seed: bull = (close_1 >= close_0); psar_0 = low_0 (bull) else high_0; ep = high_0 (bull) else low_0; af = step
bull bar t:  next = psar_{t-1} + af * (ep - psar_{t-1}), clamped at/below low_{t-1} and low_{t-2}
             flip to bear iff low_t < next (psar_t = ep; ep = low_t; af = step)
             else hold bull; new high_t > ep ratchets ep = high_t, af = min(af + step, max_step)
bear bar t:  mirror with high_{t-1} / high_{t-2} clamp; flip to bull iff high_t > next
entry  = (close_{t-1} <= psar_{t-1}) AND (close_t > psar_t)    // line 129
exit_  = (close_{t-1} >= psar_{t-1}) AND (close_t < psar_t)    // line 130
```

- Guard (source-verbatim): `len(df) < 3` (line 113) returns the explicit no-signal guard (lines 114–120, side resolved to the literal `"long"`); pre-guard bars are flat by the source's own rule, extended to the 30-bar researcher floor below (see Required data). The guard returns `round(curr_close, 4)` (line 117), identical formatting to the live path (line 134) — price-field formatting only, never an order-gating input. Empty-frame note, stated plainly: the guard reads `close.iloc[-1]` before the length check, so a zero-bar frame would raise rather than return — evaluation in the admitted configuration always starts from completed-bar history past the 30-bar floor, so the empty frame is unreachable; missing bars are skipped on available completed bars only, never fabricated.
- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (hardcoded literal on the live path line 136, guard path line 118 — no short emission exists anywhere in the file, verified by zero `short` tokens). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. Both legs are edge crosses (fire once on the crossing bar — refires require a fresh cross back through the dot), not level holds; treating either leg as a level-hold would be a different, unpinned rule.
- Mutual-exclusion proof (no tie-break pin required): entry requires `close_t > psar_t` while exit requires `close_t < psar_t` on the same two prints — the strict close-vs-dot inequalities are pairwise opposite, unsatisfiable on every bar. A touch (`close_t == psar_t`) fails both strict conjuncts and fires nothing; a shared prior-bar equality (`close_{t-1} == psar_{t-1}`) satisfies both prior conjuncts yet the current-bar conjuncts remain contradictory. The reviewer is never asked to invent an ordering.
- Exits and risk (explicit): the cross-below of the same SAR dot is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence` (`1.0 if entry else 0.0`, line 137) and the `indicators={psar}` dict (line 138) are diagnostic — neither conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying cross-above bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `opentrades` / `openprofit` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close`/`high`/`low` with fixed non-negative offsets (last two closes against the last two SAR prints; the SAR loop itself reads `high`/`low`/`close` at offsets 0/−1/−2 only), exact cross comparisons, one guarded clamp pair (`min`/`max` parameter clamps in `_resolve_psar_params`, lines 23–24 — no division anywhere in the order legs). `pd.to_numeric(errors="coerce")` (lines 33–35, 111, 145) maps malformed prints to NaN, and NaN meets every strict cross inequality as `False` — NaN bars emit no signal by construction, never a spurious order (see Negative evidence 3). No `request.*`, `security()`, `timeframe*`, `barstate.*`, `open`/`volume` read, EMA/RMA/WMA/RSI/MFI/ADX/Stochastic/MACD smoothing, session/calendar call, or stop/limit order argument exists anywhere in the file (verified by the census above returning zero matches). The `compatible_regimes == {"TREND_UP", "TREND_DOWN"}` set is metadata never read by the signal path (which takes only `df`/`params` for the two pinned literals), so no regime model gates any order. Substituting Wilder's textbook seed, a latch-state machine, a third AF leg, or any second gate would be a different, unpinned rule.
- Warmup: 30 completed `1h` bars flat by record rule — structural minimum is the 3rd completed bar (the source's own `len < 3` guard) plus margin covering the SAR AF/EP seeding transient (AF starts at 0.02 and needs sustained extreme ratchets to reach its 0.20 cap; the bull/bear seed reads bars 0–1). Pre-warmup bars are flat by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (every read is a completed bar at a non-negative offset), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Required data

- `close`/`high`/`low` on `BTCUSDT` `1h` completed bars only (sole reads: lines 33–35, 111, 145; `high`/`low` enter the SAR recursion and its two-bar clamp, `close` enters the seed comparison and both cross comparisons). No `open`, no `volume`, no external feed, no funding/OI/mark-price leg, no calendar, no multi-asset input.
- Warmup: 30 completed `1h` bars flat by record rule (structural minimum the 3rd completed bar — the source's own guard — plus margin for the AF/EP seeding transient).
- Point-in-time: every read is a completed bar at a fixed non-positive offset (the SAR loop looks back at most two bars for its clamp; the cross compares the last two prints); the decision bar's own `close` is both the last input and (via the derived same-bar-close pin, `price=round(curr_close, 4)`) the fill price basis.

## Execution assumptions

- Derived lane (all four pins predeclared in Provenance): `BTCUSDT` `1h`, completed-bar decisions with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), single-unit long-flat position with hold-no-op semantics, house sizing/capital/costs replacing the bare `leverage: 3.0` default.
- Pinned-engine path (same lane primitive as the thirty-plus admitted Forven siblings on this exact repository family): the pinned Hummingbot package `20260920` / `dev-2.17.0` backtest model prices one market order at the decision bar's own close on `BTCUSDT` `1h` with declared house fees/funding/slippage overlay; explicit-loop trailing-dot cross arithmetic over completed `close`/`high`/`low` on a single frame with same-bar-close fills is the already-verified subset for this family — no new execution primitive, no multi-asset synchronization, no shared-capital contention, no lower-timeframe alignment, no non-OHLCV input, no next-open/maker/intrabar fill is required by this record.
- Sizing/capital (stated plainly to the #89 precedent): the admitted version trades exactly one fixed unit — a flat book enters one unit on an entry bar, a long book exits the whole unit on an exit bar, same-direction refires are hold-no-ops, no pyramiding, no averaging, no safety orders, no cooldown. The downstream house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus modeled funding/slippage with explicit limitations; modeled funding is never reported as realized funding) apply to the derived evaluation here and change no trade event under the predeclared single-unit rule — DCA is a downstream execution experiment, never an admission leg of this version. No capital-dependent forced-close state beyond the standard isolated-margin accounting is admitted.
- No stop/limit/trailing/time leg is modelled because none exists in source — explicitly disabled, never defaulted. Missing trade prices are never fabricated (pre-warmup and missing bars stay flat).

## Evidence

### Source-reported

The source ships the full construction (frozen `step 0.02` / `max_step 0.2` inputs with a self-contained high/low SAR recursion, explicit extreme-point ratchet with AF stepping and two-bar clamp, cross-above entry and cross-below exit on the same dot, fixed long-only stance with the literal `"long"` direction token, no risk legs) and the `TOMB-SAR` BTC roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No twin-signal ambiguity: full-file search returns exactly `def generate_signal` plus `def generate_signals` — the two lockstep twins sharing the single `parabolic_sar_series` helper (see Provenance). Both evaluate the same booleans from the same series; no third path exists to select between.
2. No out-of-file indicator risk: the file's imports are `pandas`/`base` only — the SAR is a hand-rolled explicit recursion loop (lines 28–82) with pinned seed/clamp/ratchet arithmetic, so no facade-resolved estimator variant exists to pin or fence.
3. NaN determinism, stated plainly: the file ships no `isna` guard (verified zero matches), but every order-gating comparison is a strict `<` / `>` / `<=` / `>=` cross conjunct — a `NaN` SAR print or close (including `to_numeric` coercion output) meets each as `False` on both legs, so NaN bars emit no signal by construction, never a spurious order. On complete data the 3-bar guard plus the 30-bar researcher floor already cover seeding, so no NaN reaches any order line in the admitted configuration; missing bars stay flat and are never fabricated. The zero-bar frame raises (see Signal) and is unreachable past the floor.
4. Equality boundaries fire nothing: both legs use strict `<` / `>` on the current-bar comparison (lines 129–130); a close that merely touches the dot holds the prior state by construction. The `<=` / `>=` prior-bar conjuncts admit touch equality only as a setup, never as a standalone trigger.
5. Same-bar double-fire is impossible (mutual-exclusion proof in Signal) — no ordering assumption, invented or otherwise, is required.
6. Pool SAR sibling fenced, stated plainly: `psar-flip-stop-reverse-btcusdt-1d-2026-10-09` (admitted) trades the FMZ/ChaoZhang mirror of everget's Pine `sar(0.02, 0.02, 0.2)` study as an always-in two-sided reversal on `1d` bars — after the first flip the book is never flat and the short side is live. This record trades Forven's self-contained `TOMB-SAR` Python recursion (step/max_step pair, close-seeded bull, two-bar clamp) as a long-flat cross machine on `1h` bars — the short side is explicitly disabled, flat is a first-class resting state, and the exit is a cross-to-flat, never a reversal. Different direction handling × different exposure posture (flat exists vs always-in) × different frame × different immutable source file and SAR implementation. This record is therefore never evidence for that rule, and that record is never this rule's provenance. (Stated honestly: both rules test the same two-bar dot-side change event — the cross spelling and the latch-flip spelling coincide on complete bars — so the fence rests on the position-state machine, the frame, and the source/implementation identity, never on a pretended trigger difference.)
7. Pool composite-SAR cousin fenced, stated plainly: `chop-zone-dmi-psar-reversal-two-sided` fires only on CHOP-zone edges confirmed by ADX > 25 and the PSAR trend state (PSAR triple `0.015/0.001/0.2`, PSAR as one gate among four), two-sided with three close paths. This record fires on the bare SAR cross alone with no zone, no DMI/ADX leg, no second indicator, AF pair `0.02/0.2`, long-only — a zone-edge bar that never crosses the dot fires there and nothing here, and a bare cross in a low-ADX chop fires here and nothing there, so the trade-event sets differ by construction.
8. Pool trailing-stop cousins fenced, stated plainly: `forven-chandelier-exit-long-stop-cross` (single highest-high-minus-3×SMA-ATR line), open PR #89's FMZ Chandelier (dual ratcheted close-extremum Wilder-ATR state machine), open PR #63's SuperTrend (ATR-multiplier bands), the two Alorse SuperTrend records (median-anchored bands with RSI/StochRSI gates), and `ut-bot-atr-trailing-stop-flip` (ATR-band flip) each trade a different stop arithmetic — none evaluates an AF-accelerated extreme-point SAR recursion with a two-bar clamp, and none shares this file's seed/ratchet/AF structure.
9. Variant menus fenced, stated plainly: the `parameter_space()` surface (`step` 0.01–0.05, `max_step` 0.1–0.3) is a documented search grid the code never runs — this record freezes the `0.02/0.2` defaults as written; adopting any grid point, adding a third AF leg, switching the seed, or adding a gate/filter would each be a different, unpinned rule. The `_resolve_psar_params` clamps (lines 23–24) are pinned input sanitation, never a trading rule.
10. Diagnostic quarantine, stated plainly: `confidence` and the `indicators={psar}` dict are computed into the `Signal` envelope and read by zero order-gating comparisons — treating either as a gate, filter, exit leg, or sizing input would be a different, unpinned rule. The `compatible_regimes == {"TREND_UP", "TREND_DOWN"}` set is class metadata read by zero signal lines.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `0.02/0.2` AF pair / self-contained SAR recursion / long-only cross machine / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Acceleration relevance: replacing the AF-accelerated SAR dot with a fixed-distance trailing dot (AF frozen at 0.02, same seed/clamp/cross machine) must not reproduce-or-beat net expectancy on the frozen 42-cell campaign; fail ⇒ the acceleration adds nothing over a plain trailing-dot cross.
- F2 — Flat-state relevance: holding the long leg as an always-in two-sided reversal (short on every cross-below, same dot) must not improve net expectancy; fail ⇒ the long-flat posture with its flat rests adds nothing over the reversal.
- F3 — SAR relevance: trading close-vs-own-average crosses (plain SMA cross with a research-defined length, same long-flat posture) must not reproduce-or-beat net expectancy; fail ⇒ the SAR construction adds nothing over a basic trend-cross and the record is a label variant of one.

## Crypto portability

Direct: `BTCUSDT` perpetual/spot `1h` OHLCV on Binance — the rule consumes completed-bar `close`/`high`/`low` only, needs no venue-specific microstructure, no funding input, and no spot-vs-perp distinction in its arithmetic. The long-only no-stop posture expresses fully on spot; perps add no required leg. House costs (fees/funding/slippage) are overlaid downstream per the research campaign; modeled funding is never reported as realized funding.

## Limitations

- Late entries by construction: the dot accelerates toward price but starts far, so V-turns that reverse far from the old extreme enter strictly after the recovery is underway — disclosed lag profile.
- Chop whipsaw: closes that flicker across the dot print repeated enter-then-exit round trips with no cooldown and no structural filter — disclosed chop profile.
- No risk leg: no stop loss, take profit, trailing-stop order, or time limit exists in source — recorded as explicitly disabled; adverse excursions after a cross-above entry have no capital guardrail besides the eventual cross-below print.
- No profit-taking disposition: a grinding advance is held with no target — the dot cross is the sole exit and there is no time stop; opportunity cost accrues, disclosed.
- Downtrend blindness: declines are watched from flat with no short participation — the disabled side is a posture choice with a return cost in sustained downtrends, disclosed.
- Single-market scope: derived pin is `BTCUSDT` `1h` only; portability to other symbols/timeframes is untested and claimed nowhere in this record.
- Research overlay dependence: fills, sizing, and costs follow the derived lane pins and the downstream house model — not the source engine's own semantics.

## Implementation status

`not-implemented` — no dedicated Qlib/Hummingbot executable artifact exists for this record. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream refusal; if formally selected for execution without a reproducible recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline stage), never a second admission flag.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write is performed by the Scout lane.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/parabolic_sar.py (primary source — executable Python strategy, 161 lines, fetched live 2026-10-19 at pinned HEAD commit, 5,158 bytes, SHA-256 `f2420bf2e823d4207f307c8dd2d38c4998818421bd5efc940f92b7bf3e7b359f`, blob `2e6b70e7…223f4f`; no performance figure ships anywhere in the file)
- https://github.com/judder659/Forven (repository context; pinned HEAD `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` verified this cycle)
- `forven/strategies/base.py` at the same commit (supporting semantics — `Signal` defaults and direction normalization, 12,238 bytes, blob `27508a2a…fabf881`, identical to the blob pinned by admitted sibling records)
