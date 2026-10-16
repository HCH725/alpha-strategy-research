---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven inside-bar breakout-continuation long-flat on BTCUSDT 1h bars
created: 2026-10-17
updated: 2026-10-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/inside_bar.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven inside-bar breakout-continuation long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the three admitted Pine-demo records S01508 EMA 20/50 cross, S01509 Donchian 20/10 breakout, and S01512 Monday drift).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (merge of PR #205, committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` twice during this cycle, including immediately before writing — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/inside_bar.py`.
- GitHub blob SHA at the pinned commit: `073a47340af49c30949014232d73474d32ea3581`, size 1561 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 1561 bytes, 42 lines, SHA-256 `58b6ed2f581bb4bdaf7ce55abdf614fab10ffa52949ded1af92b6cbb7d95a6d8` — the entire file was retrieved and inspected; no rule lives anywhere else.
- The file's own words (quoted for gate evidence, never extended): docstring `Inside Bar Breakout strategy.`; `describe()` returns `Pure price action: enters on the breakout of an inside bar pattern.`; roster entry `("TOMB-INSIDEBAR", InsideBarStrategy, {"_asset": "BTC"})`; `default_params` returns exactly `{ "leverage": 3.0 }`; `compatible_regimes` returns `{"TREND_UP", "TREND_DOWN"}`; `parameter_space()` returns `{}` (no optimization surface of any kind).
- Full-file token census (verified by search over the 42 lines this cycle): 0 `strategy.entry` / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` (Pine order calls do not exist in this Python file — order intent is carried only by the `entry_signal` / `exit_signal` booleans of the returned `Signal`, quoted below); 0 `short` / 0 `sell` (no short path anywhere — direction is the literal `"long"`); 0 `volume` / 0 `open` / 0 `time` / 0 `request` / 0 `security` / 0 `timeframe` (only `high` / `low` / `close` series are read); 0 `pyramid` / 0 `position_size` / 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` / 0 `fee` / 0 `slippage` / 0 `commission` (no order arguments, no economics beyond the `leverage: 3.0` default); 1 `leverage` (that default); 1 `regime` (the metadata set only); 1 `confidence` (a constant `1.0`, never a gate).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the signal booleans, the long-only stance, the containment/breakout/low-exit geometry, and the no-stop posture — but ships no venue, no timeframe, no fill-timing flag, and no position-sizing rule inside this file. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue; the roster pins `_asset BTC` and the three admitted sibling Forven records all execute Binance `BTC/USDT-1h` — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the close — and the admitted S01508 and inside-bar-failure-fade records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) an adopted 5-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 3rd completed bar — `iloc[-3]` — plus margin; see Required data); (4) house sizing/capital/costs replacing the bare `leverage: 3.0` default (see Execution assumptions; the 3.0 default sits inside the house 3x/5x overlay range and changes no event). The containment test, the breakout entry, the low exit, the long-only stance, the entry/exit mutual exclusivity, and the no-stop/no-target/no-time-exit posture are source-verbatim and unmodified.

Pre-write dedup (2026-10-17): working-tree case-insensitive filename search for `inside` returns exactly one strategy record — `inside-bar-failure-fade-time-exit-two-sided-btcusdt-1d-2026-10-13.md` (FMZ ChaoZhang failure-fade, two-sided, `1d`, 3-bar time exit — the opposite mechanism: it enters only when the probe FAILS back inside and never follows a breakout; fenced in Negative evidence 7). Content search for `inside_bar` / `is_inside` hits only that record's prose plus unrelated dedup sentences — no second record embodies this rule. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Nearest pool neighbours (`nr7-price-breakout-long`, `donchian-20-10-breakout`, `darvas-box-breakout-long`, `turtle-system-2-55d-breakout`, `turtle-soup-donchian-fade-bracket`, dual-EMA `engulfing`) differ in contraction definition, exit, direction scope, or mechanism class (fenced in Negative evidence 7–8). Not a duplicate, paraphrase, or trivial parameter variant: opposite entry logic (follow vs fade), different exit (signal low vs 3-bar clock), different direction scope (long-only vs two-sided), different timeframe (`1h` vs `1d`), different source.

## Economic mechanism

### Source-reported

The source claims only what its two sentences print: `Inside Bar Breakout strategy` that `enters on the breakout of an inside bar pattern`. No behavioural, structural, or risk-premium channel is claimed anywhere in the 42 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Two-bar balance plus confirmed breakout, long-only, event-driven. An inside bar (prior bar's full range contained in the bar before it) prints a completed two-sided auction with no new information; a subsequent close above the inside high confirms the balance resolved upward, and the rule rides that resolution until a close back below the trailing two-bar-ago low ends it. Unlike the admitted failure-fade record (which bets probes fail and fades them both ways with a 3-bar clock), this rule bets the confirmed breakout continues and holds without any clock — the two records fire on mutually exclusive bars by construction (a close cannot be both back-inside and broken-out). Unlike every band/channel breakout record in the pool (Donchian rolling extrema, Darvas boxes, Turtle 55-day highs, NR7 narrowest-of-seven, Bollinger bands) there is no lookback window, no average, no dispersion, and no band — the reference rails are exactly two specific historical bars, never a rolling statistic. Unlike oscillator-cross systems there is no level, no smoothing, and no secondary line. The failure mode is plain: chop prints repeated inside bars whose breakouts reverse immediately, grinding the book through breakout-then-low-break round trips with no guardrail beyond the trailing low exit.

## Signal

Exact rule as pinned (any other bar offsets, strictness, exit reference, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own:

```text
high_1, low_1 = high[-2], low[-2]   // previous completed bar
high_2, low_2 = high[-3], low[-3]   // bar before it
curr_close    = close[-1]           // latest completed-bar close
is_inside_bar = (high_1 < high_2) and (low_1 > low_2)   // strict containment
breakout_up   = is_inside_bar and (curr_close > high_1) // close-confirmed break
entry         = breakout_up
exit_         = curr_close < low_1                       // close below trailing low
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (literal — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops.
- Exit character (disclosed, not smoothed): `low_1` is the rolling two-bars-ago low, not the entry bar's low — the exit trails by construction. A rising two-bar-ago low ratchets the exit upward; a falling one loosens it. This is implemented literally as coded, never replaced with an entry-anchored stop.
- Direction: long-only. The short side is absent by construction (0 `short` / 0 `sell` in the file) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the signal exit (`curr_close < low_1`) is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence=1.0` is a constant passenger and `indicators={"inside_bar": ...}` is diagnostic — neither conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on the next breakout bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Conflict priority (provably irrelevant): entry and exit cannot fire on the same bar. Entry requires `curr_close > high_1`; exit requires `curr_close < low_1`; every printed bar satisfies `high_1 >= low_1`, so both jointly true would require the close strictly above and strictly below two levels in non-increasing order — impossible; when the close equals either rail (`== high_1` or `== low_1`) both strict tests are false. No priority rule is needed and none is missing.
- Determinism note for the reviewer: the rule reads only `high` / `low` / `close` with integer offsets `-1/-2/-3` plus strict `>` / `<` / `and` — no `request.*`, `security()`, `timeframe*`, `barstate.*`, volume-weighted logic, session/calendar call, or stop/limit order argument anywhere in the file (verified by the census above returning zero matches). The `compatible_regimes` set is metadata never read by `generate_signal` (which takes only `df`), so no regime model gates any order.

## Required data

- `1h` bars of one pair: `high` (containment rails and breakout test), `low` (containment rails and trailing exit), `close` (breakout confirmation and exit test). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade/aggressor, L2/order-book, on-chain, options/Greeks, sentiment/news, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; every test reads trailing completed bars of the same three series, never a second feed).
- Warmup: 5 completed `1h` bars flat by record rule — structural minimum is the 3rd completed bar (`iloc[-3]` is the deepest read), plus margin. Pre-warmup bars are flat by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (every offset reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance `1h` under the house overlay (researcher pin per the declaration — the file names no venue/timeframe; the roster pins `_asset BTC` and all three admitted sibling Forven records execute Binance `BTC/USDT-1h`; no source-market equivalence is claimed).
- Order timing (predeclared derivation): completed-bar decisions with same-bar-close market fills for entries and exits — the file returns `price=round(curr_close, 4)` (the close), and the identical primitive is already admitted on the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) by the sibling S01508 record and the inside-bar-failure-fade record. This record claims no other fill convention: no perfect-open print, no maker-touch, no intrabar-path-dependent fill. Zero stop/limit legs exist, so there is no same-bar TP/SL ordering ambiguity.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing/time orders by record rule. No hidden Hummingbot stop-order defaults are relied upon.
- Sizing/capital/costs: the file ships no sizing, capital, fee, or slippage concept beyond the bare `leverage: 3.0` backtest default (quoted verbatim; inside the house 3x/5x overlay range). The explicit house overlay (single-unit frame, pinned house taker fees both legs, modeled funding while long, nothing while flat) applies to the derived evaluation here, never presented as source-native behavior. Funding is never zero-claimed: longs held across the `00:00`/`08:00`/`16:00 UTC` stamps carry modeled funding.
- Concurrency: at most one single-asset long position at any time; an exit closes it in full. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (pinned commit `e9a6c09`, file `forven/strategies/builtin/inside_bar.py`, blob `073a4734`, 1561 bytes / 42 lines, HEAD re-confirmed via `ls-remote` this cycle): the `Inside Bar Breakout strategy` docstring; the `enters on the breakout of an inside bar pattern` describe string; the `TOMB-INSIDEBAR` / `_asset BTC` roster tuple; the `{ "leverage": 3.0 }` default; the `{"TREND_UP", "TREND_DOWN"}` metadata set; the empty `parameter_space()`; and the verbatim entry/exit boolean lines. This record claims no source-reported performance number of any kind — the file ships no table, figure, return, win rate, trade count, or cost model — and no reproduced performance exists.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 stop/limit/profit/loss/qty/fee/slippage/commission/pyramid/position-size tokens in the file — the trailing-low signal exit is the sole position-ending path by construction, and the file promises no stop or target.
2. Entry/exit mutual exclusivity proved in Signal (shared `high_1 >= low_1` rail ordering with strict opposite inequalities) — no same-bar entry-vs-exit ordering ambiguity exists to resolve.
3. Strict containment and strict breaks: equality on any rail (`high_1 == high_2`, `low_1 == low_2`, `curr_close == high_1`, `curr_close == low_1`) fires nothing; a zero-range bar can still be contained only if strictly smaller on both rails. Ties are dead bars, pinned, not smoothed.
4. Flat-state and held-state determinism: exit bars while flat are no-ops; entry bars while long are no-ops under the predeclared single-unit rule; the seed bars satisfy no order condition by themselves (every edge needs bars `-2` and `-3`).
5. Metadata fenced, admitted plainly: `compatible_regimes`, `confidence=1.0`, and the `inside_bar` indicator flag are never read by any order-gating line — a reviewer must not graft a regime filter, confidence gate, or alternate exit onto this record.
6. Derivation boundary fenced: the only non-source-native behaviors are the BTCUSDT-`1h` research frame, same-bar-close fills, the 5-bar warmup, single-unit no-pyramid booking, and house sizing/costs — all predeclared above; every edge, strictness, ordering, direction scope, and risk posture is source-verbatim. This record is therefore never evidence that the Forven engine's own timing or sizing passes.
7. Overlap fences, admitted plainly: the admitted `inside-bar-failure-fade` record fades failed probes both ways with a 3-bar clock on `1d` (entries require the close back INSIDE; clean follow-through breakouts fire nothing there); this record follows confirmed close-breakouts long-only with a trailing-low exit on `1h` (fade bars fire nothing here) — mutually exclusive entry bars, different exits, different direction scope, different timeframe, different source. Sibling `nr7-price-breakout-long` buys the narrowest-range-of-seven breakout (7-bar contraction gate, 10-day time exit plus ATR stop — no containment precondition); `donchian-20-10-breakout` buys every rolling-20-high close (no containment, 10-bar-low exit); `darvas-box-breakout-long` follows confirmed box breakouts (box, not 2-bar containment); `turtle-system-2-55d-breakout` follows 55-day breakouts with 2N stops and adds; `turtle-soup-donchian-fade-bracket` fades Donchian false breakouts (a fade, like the inside fade — this record is the follow side). Shared `breakout` vocabulary is not shared signal.
8. No hidden variants admitted: any other bar offsets, touch-inclusive containment, entry-anchored stop, stop/target/time-exit addition, other frame, fill, venue, or book is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 2-bar strict containment / close-confirmed breakout entry / rolling two-bar-ago-low signal exit / long-only / `1h` BTCUSDT / same-bar-close fills / no-stop posture are frozen.

- F1 — Fade relevance: a failure-fade twin (the admitted fade rule's direction logic on this frame — enter on failed probes, same book, fills) must not improve net expectancy; fail ⇒ breakout-continuation adds nothing over fading the same inside bars here.
- F2 — Exit relevance: a 3-bar time-exit twin (the admitted fade record's clock applied to these breakout entries — same entries, book, fills) must not improve net expectancy; fail ⇒ the trailing-low exit adds nothing over a fixed time box on this market.
- F3 — Containment relevance: admitting rail-touch bars (`<=` / `>=`) as inside bars instead of the strict containment must not improve net expectancy; fail ⇒ the strict two-bar balance definition adds nothing over loose range-overlap trading.

## Crypto portability

Pinned to BTCUSDT Binance `1h` under the house overlay. The rule reads completed hourly bars only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (crypto trades 24/7; inside bars form purely on printed range containment, and the file reads no `open`, so session-gap behavior is simply absent rather than approximated). The geometry is denomination-free (pure inequalities — no USDT-scale threshold to dwarf or reweight). The rule is long-only, so a spot deployment expresses every firing bar while no short leg ever needs a venue (never silently converted). No warmup history beyond 5 `1h` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop: a breakout that reverses vertically is held until a close prints below the trailing two-bar-ago low — the record's principal risk, carried over exactly from source.
- Trailing-exit looseness (disclosed): because the exit references the moving two-bar-ago low rather than the entry bar's low, a falling-low stretch loosens the exit even as the trade goes against it — the coded cost of the literal implementation, not a designed ratchet.
- Chop grind: range-bound `1h` regimes print repeated inside bars whose breakouts fail immediately, exercising the entry-then-next-bar-exit path often — expected behavior, not a bug.
- Derived fill timing and frame: same-bar-close fills and the `1h` BTCUSDT frame are researcher pins (the file stamps neither); backtest economics under any other timing or frame differ by construction.
- Single-venue port residual: Forven backtest prints/fees/funding/margin mechanics beyond the house model are unclaimed, disclosed.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest (the file's `parameter_space()` is empty).
- Author scope: Forven ships backtest demos as research objects, not a vetted retail trading system — this record is research-only and claims no live suitability.

## Implementation status

- `not-implemented`. No Hummingbot/Qlib/n8n/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `research-only`, `not-approved`. Admission of this record would mean only that its core signal and causal trade-event semantics are losslessly expressible under the pinned backtester with the labeled house overlay — not profitability, survival, or any trading approval.

## Related Wiki records

- None. No Wiki Brain write was performed for this cycle.

## Sources

- Immutable program file at pinned commit (all rules): https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/inside_bar.py
- Repository (project context): https://github.com/judder659/Forven
