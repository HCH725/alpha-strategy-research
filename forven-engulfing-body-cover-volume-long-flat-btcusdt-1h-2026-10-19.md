---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven engulfing body-cover volume-gated long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/engulfing.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven engulfing body-cover volume-gated long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-stddev-cross-swing`, and thirty other admitted Forven records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`, verified via the GitHub commits API this cycle; verified as the repository HEAD via `git ls-remote` against both `HEAD` and `refs/heads/main` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/engulfing.py`.
- GitHub blob SHA at the pinned commit: `7d4609cddb64c060cb025fcb251f8dcbf82789d9`, size 3544 bytes.
- Byte-identity check: the file retrieved from `raw.githubusercontent.com` at the pinned commit is 3544 bytes, 109 lines, SHA-256 `1f01ee158c8e4cee81a2054ad69fe0c9f609f4efa369360ac4eb18dc7080a1a1`, and `git hash-object` reproduces the GitHub blob (`7d4609c…f82789d9`) — the entire file was retrieved twice and inspected (both fetches byte-identical).
- Registration: the file self-registers via `STRATEGY_CLASS = EngulfingStrategy` (line 108), `TYPE_NAME = "engulfing"` (line 12), and the `STRATEGIES = [("PREBUILT-ENGULFING", EngulfingStrategy, {"_asset": "BTC"})]` roster pin (line 109). Repo-wide, no other builtin file carries this `TYPE_NAME` or roster name; working-tree search for `builtin/engulfing` / `PREBUILT-ENGULFING` / `EngulfingStrategy` / `TYPE_NAME = "engulfing"` returns zero strategy records citing this source file.
- The file's own words (quoted for gate evidence, never extended): module docstring `Bullish / Bearish Engulfing pattern strategy with volume confirmation.` with `Detects a bullish engulfing candle (current green body completely covers the previous red body) confirmed by above-average volume, and enters long.` (lines 1–5); class docstring is the bare `Engulfing Pattern ({asset})` name (lines 15–18); `describe()` returns `Bullish engulfing pattern strategy requiring volume >= 1.5x the 20-bar average volume for confirmation.` (lines 39–44, with defaults); `default_params` returns exactly `{ "volume_mult": 1.5, "leverage": 1.0 }` (lines 28–33); `compatible_regimes` returns `{"TREND_UP", "RANGE_BOUND"}` (lines 35–37, metadata never read by the signal path); `parameter_space()` returns `{ "volume_mult": (1.0, 2.5, 0.5) }` (lines 102–105, a documented search surface only — this record pins the default and runs no search). No performance phrase of any kind ships anywhere in the 109 lines — this record adopts no source-reported performance (see Evidence).
- Single decision path, verified complete: `generate_signal()` (lines 46–100) is the sole signal method — no `generate_signals` vectorized twin exists anywhere in the 109 lines, so no twin-selection ambiguity exists. The method pins its constants (`vol_mult` 1.5, `vol_period` 20, `min_bars` 22, lines 47–49), applies its own short-frame guard (lines 50–51), reads the last two bars' `open`/`close`/`volume` (lines 53–59, 74–75), evaluates the body-cover geometry on both bars (lines 61–71), gates the bullish leg on the trailing volume multiple (lines 74–78), evaluates the ungated bearish leg for exit (lines 81–84), and returns a single `Signal` (lines 86–100).
- Zero out-of-file indicator dependencies: the file imports only `numpy`, `pandas`, and `forven.strategies.base` (lines 7–10). No `forven.strategies.indicators` facade import exists — no `atr`/`adx`/`rsi`/`stochastic` diagnostic call conditions any order line (there is nothing to fence here).
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (12238 bytes, blob `27508a2a6b8c546e21adefdb97fc0144fabf881b`, identical to the blob pinned by the admitted `forven-rsi-s00139`, `forven-bb-edge-fade-reclaim`, and `forven-stddev-cross-swing` records) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults (lines 69–70), `direction: str = "long"` default (line 72), plus `__post_init__` coercion (lines 77–80) and `_normalize_signal_direction` (line 160) mapping the `"long"` literal back to `"long"` — the short-frame guard (line 51, `Signal(price=...)` with no side argument) therefore resolves to the `"long"` default on every pre-guard bar, and the live `direction="long"` literal (line 90) survives untouched on every evaluated bar.
- Full-file token census (verified by search over the 109 lines this cycle): `direction` occurs exactly once (live line 90 literal `"long"`; the guard carries no side token and resolves to the base default — no short leg exists anywhere); 0 `short` / 0 `sell` (no short path anywhere); 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` (no order arguments, no risk legs); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default, replaced by the house overlay — see Execution assumptions); 0 `funding` / 0 `mark_price` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any line; 0 `rsi` / 0 `ema` / 0 `atr` / 0 `adx` / 0 `vwap` (no smoothing, no regime filter, no trailing stop); 0 `high` / 0 `low` reads in any order-gating line (the cover geometry is pure `open`/`close` body comparison — no wick is read); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` / 0 `cooldown` (no position-aware state conditions any signal); `df[` reads are exactly two (`df["close"]` guard line 51, `df["volume"]` line 74 — the `open`/`close`/`volume` bar fields are otherwise read via the `df.iloc[-1]` / `df.iloc[-2]` row handles, lines 53–54); `len(df)` occurs exactly once (the line-50 guard — the file's own warmup floor, adopted verbatim, never invented).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the two-bar body-cover geometry, the 1.5x trailing-20-bar volume gate on the entry leg only, the ungated bearish-cover exit leg, the long-only stance, the no-stop posture, and its own 22-bar short-frame guard — but ships no venue spelling, no timeframe, no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the thirty-plus admitted Forven records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit position pin with hold-no-op semantics with the source's own 22-bar guard adopted verbatim as the warmup floor (an already-positioned book treats further bullish-gated bars as hold-no-ops, a flat book treats bearish-cover bars as no-ops, re-entry re-arms on any qualifying gated engulfing bar after any exit with no cooldown, pre-guard bars flat by the source's own rule — see Signal); (4) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal).

Pre-write dedup (2026-10-19): working-tree filename/content search for `builtin/engulfing` / `PREBUILT-ENGULFING` / `EngulfingStrategy` returns zero strategy records — no record cites this source file. Mechanism search returns the pool neighbour `dual-ema-engulfing-volume-long-btcusdt-1h-2026-10-07.md` (FMZ 434564 dual-EMA-regime-gated wick-cover engulfing with 1.2x prior-bar volume, long-only `1h` — fenced as a different construction in Negative evidence 6), the closed unmerged Scout PR #219 (TA-Lib `CDLENGULFING` pure-geometry two-sided flip on `1d` with next-open fills, closed `NOT_LOSSLESS` on Gate 4/5 record-writing blockers — different source, direction, volume, frame, and fills, fenced in Negative evidence 7), and single-bar/triple-bar candle cousins (`1-3-1-red-green-candle-reversal`, `wick-reversal-hammer-shooting-star-long-flat`, `three-white-soldiers-black-crows-flip` — one-bar wick and three-bar soldiers constructions, never two-bar body-cover). No open `research/*` PR carries this source file (open PRs are only #48/#49/#63/#89/#92/#251/#304 — different mechanisms, indicators, and sources). Not a duplicate, paraphrase, or trivial parameter variant: a pure two-bar body-cover with a trailing-average volume gate and no trend filter is a different signal construction from a dual-EMA-regime-gated wick-cover with a prior-bar volume multiple — different geometry × different volume construction × different gating × different exit legs × different immutable source file.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: a `Bullish / Bearish Engulfing pattern strategy with volume confirmation` that `Detects a bullish engulfing candle (current green body completely covers the previous red body) confirmed by above-average volume, and enters long.` No behavioural, structural, or risk-premium channel is claimed anywhere in the 109 lines. The file ships no backtest numbers of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Participation-confirmed reversal-entry, long-only, state-holding. The system buys only the exact bar a red body is fully covered by a larger green body *and* that bar's volume clears 1.5x its own trailing 20-bar average — unlike pure-pattern systems, a textbook engulfing print on thin volume fires nothing; unlike regime-gated systems, no EMA, ADX, or slope filter can veto a gated print even inside a vertical downtrend. The exit is deliberately asymmetric: any bearish body-cover (no volume test) closes the unit, so the book demands participation to enter but accepts a bare pattern to leave. The failure mode is plain: chop that alternates gated-bullish and bare-bearish covers whipsaws the book with no stop and no cooldown, and a gated entry whose follow-through never prints a bearish cover is held indefinitely with no profit-taking leg until the pattern itself reverses.

## Signal

Exact rule as pinned (any other pattern definition, volume multiple, averaging window, gate polarity, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own; `generate_signal` (lines 46–100) is the single source of truth — no second decision logic exists:

```text
inputs (defaults, frozen): volume_mult = 1.5, vol_period = 20
prev_open/prev_close = open/close of bar t-1; curr_open/curr_close = open/close of bar t
prev_body = [min(prev_open,prev_close), max(prev_open,prev_close)]
curr_body = [min(curr_open,curr_close), max(curr_open,curr_close)]
body_engulfs = (curr_body_bot <= prev_body_bot) AND (curr_body_top >= prev_body_top)  // lines 61-69, 83
bullish      = (prev_close < prev_open) AND (curr_close > curr_open) AND body_engulfs  // line 71
avg_vol      = mean(volume[t-21 .. t-1])   // 20 bars ending at the prior bar, line 74
vol_ok       = (curr_volume >= avg_vol * 1.5) if avg_vol > 0 else False                // line 76
entry        = bullish AND vol_ok                                                       // line 78
exit_        = (prev_close > prev_open) AND (curr_close < curr_open) AND body_engulfs   // lines 81-84
```

- Guard (source-verbatim): `len(df) < 22` (line 50 — `vol_period + 2`) returns the explicit no-signal guard (line 51, side resolved to the base `"long"` default); pre-guard bars are flat by the source's own rule, adopted verbatim as the warmup floor (see Required data).
- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (hardcoded literal on the live path, base default on the guard path — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. Both legs are one-bar patterns (fire once on the printing bar — refires require a fresh two-bar print), not levels; treating either leg as a level-hold would be a different, unpinned rule.
- Mutual-exclusion proof (no tie-break pin required): entry requires `prev_close < prev_open` AND `curr_close > curr_open` while exit requires `prev_close > prev_open` AND `curr_close < curr_open` on the same two prints — the strict color inequalities are pairwise opposite, unsatisfiable on every bar. Doji bars (`prev_close == prev_open` or `curr_close == curr_open`) fail both color conjuncts and fire nothing; the shared `body_engulfs` conjunct cannot reunite legs whose color halves already disagree. The reviewer is never asked to invent an ordering.
- Exits and risk (explicit): the bare bearish body-cover is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence = np.clip(curr_volume / (avg_volume * vol_mult), 0.0, 1.0)` on every evaluated bar (lines 91–93) and the `indicators={bullish_engulfing, vol_confirmed, curr_volume, avg_volume}` dict (lines 94–99) are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying gated-engulfing bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `open`/`close`/`volume` with fixed non-negative offsets (last two bars plus a trailing 20-bar mean ending at the prior bar), exact body comparisons, and one guarded volume division (`avg_vol > 0 else False` — no division-by-zero, no NaN propagation into any order line). No `request.*`, `security()`, `timeframe*`, `barstate.*`, high/low read, EMA/RMA/WMA/VWMA/RSI/MFI/ADX/ATR smoothing, session/calendar call, or stop/limit order argument exists anywhere in the file (verified by the census above returning zero matches). The `compatible_regimes == {"TREND_UP", "RANGE_BOUND"}` set is metadata never read by the signal path (which takes only `df`/`params`), so no regime model gates any order. Substituting a wick-cover geometry, a prior-bar volume multiple, or any trend gate would be a different, unpinned rule.
- Warmup: 30 completed `1h` bars flat by record rule — structural minimum is the 22nd completed bar (20-bar trailing volume seed ending at the prior bar plus the two-bar pattern window and the source's own `len < 22` guard — plus margin). Pre-warmup bars are flat by record rule; missing bars are skipped on available completed bars only — prices and volumes are never fabricated. No repainting (every window reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Required data

- `open`/`close`/`volume` on `BTCUSDT` `1h` completed bars only (sole reads: guard `df["close"]`, trailing `df["volume"]` mean, and the last-two-bar `open`/`close`/`volume` row fields). No `high`/`low`, no external feed, no funding/OI/mark-price leg, no calendar, no multi-asset input.
- Warmup: 30 completed `1h` bars flat by record rule (structural minimum the 22nd completed bar — 20-bar volume seed plus the two-bar pattern plus the source's own guard — plus margin).
- Point-in-time: every window is trailing over completed bars; the decision bar's own `open`/`close`/`volume` are both the last inputs and (via the derived same-bar-close pin, `price=round(curr_close, 4)`) the fill price basis — no future bar, no unfinished-bar read, no repainting.

## Execution assumptions

- Derived lane (all four pins predeclared in Provenance): `BTCUSDT` `1h`, completed-bar decisions with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), single-unit position with hold-no-op semantics, house sizing/capital/costs replacing the bare `leverage: 1.0` default.
- Pinned-engine path (same lane primitive as the thirty-plus admitted Forven siblings on this exact repository family): the pinned Hummingbot package `20260920` / `dev-2.17.0` backtest model prices one market order at the decision bar's own close on `BTCUSDT` `1h` with declared house fees/funding/slippage overlay; two-bar body-cover arithmetic over completed `open`/`close` plus a trailing volume mean on a single frame with same-bar-close fills is the already-verified subset for this family — no new execution primitive, no multi-asset synchronization, no shared-capital contention, no lower-timeframe alignment, no non-OHLCV input, no next-open/maker/intrabar fill is required by this record.
- Sizing/capital (stated plainly to the #219 precedent): the admitted version trades exactly one fixed unit — a flat book enters one unit on an entry bar, a long book exits the whole unit on an exit bar, same-direction refires are hold-no-ops, no pyramiding, no averaging, no safety orders, no cooldown. The downstream house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus modeled funding/slippage with explicit limitations; modeled funding is never reported as realized funding) apply to the derived evaluation here and change no trade event under the predeclared single-unit rule — DCA is a downstream execution experiment, never an admission leg of this version. No capital-dependent forced-close state beyond the standard isolated-margin accounting is admitted.
- No stop/limit/trailing/time leg is modelled because none exists in source — explicitly disabled, never defaulted. Missing trade prices and missing volumes are never fabricated (pre-warmup and missing bars stay flat).

## Evidence

### Source-reported

The source ships the full construction (frozen `volume_mult 1.5` input with a hardcoded 20-bar trailing mean, two-bar body-cover geometry for both legs, volume gate on the entry leg only, fixed long-only stance with the literal `"long"` direction token, no risk legs) and the `PREBUILT-ENGULFING` BTC roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No twin-signal ambiguity: full-file search returns exactly one `def generate_signal` and zero `def generate_signals` — there is no second decision path to select between.
2. No out-of-file indicator risk: the file's imports are `numpy`/`pandas`/`base` only — no facade-resolved `atr`/`adx`/`rsi` call exists to pin or fence.
3. Zero-volume determinism: a 20-bar window with `avg_vol == 0` maps `vol_ok` to `False` (line 76 ternary) — dead-volume bars emit no entry; no division-by-zero, no NaN propagation into any order line.
4. Equality boundaries fire nothing: both color legs use strict `<` / `>` on the two prints; a doji on either bar holds the prior state by construction. The `<=` / `>=` cover conjuncts admit touch equality only inside the body geometry, never as a standalone trigger.
5. Same-bar double-fire is impossible (mutual-exclusion proof in Signal) — no ordering assumption, invented or otherwise, is required.
6. Pool-cousin fence (dual-EMA engulfing record), stated plainly: `dual-ema-engulfing-volume-long-btcusdt-1h-2026-10-07.md` (FMZ 434564) trades a dual-EMA-regime-gated (EMA15/30 alignment) wick-cover engulfing geometry (`low < low[1] and high > high[1]`) with a body-ratio filter on both bars and a 1.2x prior-bar volume multiple, exiting on regime-flip OR bearish wick-cover. This record trades a pure two-bar body-cover (`curr_body` covers `prev_body` on `open`/`close` only, no wick read, no ratio, no EMA) with a 1.5x trailing-20-bar-average volume gate on the entry leg only, exiting on bare bearish body-cover only, from immutable file `builtin/engulfing.py` — different geometry × different volume construction × ungated vs regime-gated × different exit legs × different immutable source file. This record is therefore never evidence for that rule, and that record is never this rule's provenance.
7. Closed-PR fence (#219 TA-Lib engulfing), stated plainly: PR #219 carried TA-Lib `CDLENGULFING` pure-geometry detection wired as a two-sided flip book on `1d` with next-bar-open fills and no volume leg, closed `NOT_LOSSLESS` on Gate 4 sizing-ambiguity and Gate 5 engine-path/cost/funding blockers (review `2026-10-15T02:48:08Z`). This record is long-flat (short side absent by construction), volume-gated (1.5x trailing mean), `1h`, same-bar-close, from Forven immutable commit `e9a6c09`, with the Gate 4 single-unit pin and the Gate 5 sibling-lane engine path plus house cost/funding limitations predeclared above. Different source × direction × volume × frame × fills × record template. This record is therefore never a relitigation of that PR.
8. Candle-cousin fence, stated plainly: `1-3-1-red-green-candle-reversal-fixed-rr-long` (three-bar color sequence with fixed RR), `wick-reversal-hammer-shooting-star-long-flat` (single-bar wick rejection), and `three-white-soldiers-black-crows-flip` (three-bar soldiers) trade different bar counts and different geometries — none evaluates a two-bar body-cover with a trailing volume mean.
9. Variant menus fenced, stated plainly: the `parameter_space()` surface (`volume_mult` 1.0–2.5) is a documented search grid the code never runs — this record freezes the `1.5` default as written; adopting any grid point, adding a trend gate, switching to wick-cover, or moving the volume window would each be a different, unpinned rule.
10. Regime/metadata quarantine, stated plainly: `confidence`, `bullish_engulfing`, `vol_confirmed`, `curr_volume`, `avg_volume`, and the `compatible_regimes == {"TREND_UP", "RANGE_BOUND"}` set are returned inside diagnostic fields or class metadata and read by zero order-gating comparisons — treating any of them as a gate, filter, or sizing input would be a different, unpinned rule.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `1.5x/20-bar` gated body-cover entry / bare bearish-cover exit / long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Volume-gate relevance: dropping the 1.5x trailing-mean gate (pure body-cover entry, same exit) must not improve net expectancy on the frozen 42-cell campaign; fail ⇒ the participation gate adds nothing over the bare pattern.
- F2 — Geometry relevance: replacing body-cover with wick-cover (same volume gate, same exit polarity) must not improve net expectancy; fail ⇒ the body-cover construction adds nothing over its wick twin.
- F3 — Asymmetry relevance: gating the exit leg on the same 1.5x volume test (symmetric volume-gated exits) must not improve net expectancy; fail ⇒ the coded bare-pattern exit adds nothing over its symmetric twin.

## Crypto portability

Direct: `BTCUSDT` perpetual/spot `1h` OHLCV on Binance — the rule consumes completed-bar `open`/`close`/`volume` only, needs no venue-specific microstructure, no funding input, and no spot-vs-perp distinction in its arithmetic. The long-only no-stop posture expresses fully on spot; perps add no required leg. House costs (fees/funding/slippage) are overlaid downstream per the research campaign; modeled funding is never reported as realized funding.

## Limitations

- Chop whipsaw: alternating gated-bullish and bare-bearish body-covers in a range prints repeated enter-then-exit round trips with no cooldown and no structural filter — disclosed chop profile.
- No risk leg: no stop loss, take profit, trailing stop, or time limit exists in source — recorded as explicitly disabled; adverse excursions after a gated entry have no capital guardrail besides the eventual bearish-cover print.
- Indefinite-hold disposition: a position whose follow-through never prints a bearish body-cover is held forever — the pattern exit is the sole exit and there is no time stop; opportunity cost accrues, disclosed.
- Thin-volume blindness: the 1.5x trailing-mean gate suppresses entries in genuinely illiquid tapes even when the pattern is textbook — the gate is pinned as written, disclosed.
- Single-market scope: derived pin is `BTCUSDT` `1h` only; portability to other symbols/timeframes is untested and claimed nowhere in this record.
- Research overlay dependence: fills, sizing, and costs follow the derived lane pins and the downstream house model — not the source engine's own semantics.

## Implementation status

`not-implemented` — no dedicated Qlib/Hummingbot executable artifact exists for this record. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream refusal; if formally selected for execution without a reproducible recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline stage), never a second admission flag.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write is performed by the Scout lane.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/engulfing.py (primary source — executable Python strategy, 109 lines, fetched live 2026-10-19 at pinned HEAD commit, 3,544 bytes, SHA-256 `1f01ee158c8e4cee81a2054ad69fe0c9f609f4efa369360ac4eb18dc7080a1a1`, blob `7d4609c…f82789d9`; no performance figure ships anywhere in the file)
- https://github.com/judder659/Forven (repository context; pinned HEAD `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` verified this cycle)
- `forven/strategies/base.py` at the same commit (supporting semantics — `Signal` defaults and direction normalization, 12,238 bytes, blob `27508a2a…fabf881`, identical to the blob pinned by admitted sibling records)
