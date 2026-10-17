---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven Williams %R EMA-reclaim exhaustion-exit long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/williams_ema_reclaim.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven Williams %R EMA-reclaim exhaustion-exit long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the three admitted Pine-demo records S01508 EMA 20/50 cross, S01509 Donchian 20/10 breakout, S01512 Monday drift, and the admitted `forven-inside-bar-breakout-continuation` record).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/williams_ema_reclaim.py`.
- GitHub blob SHA at the pinned commit: `e50099d1713b9a7b859364088886dea6b46af7a8`, size 3766 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3766 bytes, 107 lines, SHA-256 `8040aa39c00243743f573c011f9b8ee408940e8fe2060d87cbc19cb17466d829` — the entire file was retrieved and inspected; no rule lives anywhere else (the strategy is fully self-contained: its Williams %R helper is defined inline at the top of this same file, unlike sibling files that import shared facades).
- The file's own words (quoted for gate evidence, never extended): docstring `Williams %R recovery strategy with EMA support filter.`; `describe()` returns `Buy when Williams %R(14) recovers through -70.0 while price is above EMA(21); exit near momentum exhaustion at -25.0.`; roster entry `("PREBUILT-WILLIAMS-EMA-RECLAIM-BTC", WilliamsEMAReclaimStrategy, {"_asset": "BTC"})`; `default_params` returns exactly `{ "wr_period": 14, "ema_period": 21, "wr_entry": -70.0, "wr_exit": -25.0, "leverage": 2.0 }`; `compatible_regimes` returns `{"RANGE_BOUND", "TREND_UP"}`; `parameter_space()` returns `{ "wr_entry": (-85, -55, 5), "wr_exit": (-35, -10, 5), "ema_period": (10, 34, 3) }` (a documented search surface only — this record pins the defaults and runs no search).
- Full-file token census (verified by search over the 107 lines this cycle): 0 `strategy.entry` / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` (Pine order calls do not exist in this Python file — order intent is carried only by the `entry_signal` / `exit_signal` booleans of the returned `Signal`, quoted below); 0 `short` / 0 `sell` (no short path anywhere — direction is the literal `"long"`); 0 `volume` / 0 `open` / 0 `time` / 0 `request` / 0 `security` / 0 `timeframe` (only `high` / `low` / `close` series are read); 0 `pyramid` / 0 `position_size` / 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` / 0 `fee` / 0 `slippage` / 0 `commission` (no order arguments, no economics beyond the `leverage: 2.0` default); 1 `leverage` (that default); 1 `compatible_regimes` property (metadata set only); 1 `confidence` (a deterministic function of the current Williams %R value, never a gate).
- Dual implementation, mutually confirming: the file ships both `generate_signal` (scalar, latest-bar) and `generate_signals` (vectorized, full-frame) with identical edge logic — entry `(wr.shift(1) < wr_entry) & (wr >= wr_entry) & support_ok`, exit `((wr.shift(1) > wr_exit) & (wr <= wr_exit)) | (close < ema)` plus `.fillna(False)` — so the rule is pinned twice in the same file, not once.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the Williams %R(14) construction, the EMA(21) construction, the -70 reclaim entry with EMA-support conjunction, the dual exit (exhaustion cross through -25 OR EMA loss), the long-only stance, and the no-stop posture — but ships no venue, no timeframe, no fill-timing flag, and no position-sizing rule inside this file. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue; the roster pins `_asset BTC` and the four admitted sibling Forven records all execute Binance `BTC/USDT-1h` — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(close, 4)` — the close — and the admitted S01508, inside-bar-failure-fade, and forven-inside-bar records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) an adopted 30-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 15th completed bar — 14-bar Williams %R seed plus one shift row — plus margin; see Required data); (4) house sizing/capital/costs replacing the bare `leverage: 2.0` default (see Execution assumptions; the 2.0 default sits inside the house 3x/5x overlay range and changes no event). The reclaim entry, the EMA conjunction, the dual exit, the long-only stance, the entry/exit mutual exclusivity, and the no-stop/no-target/no-time-exit posture are source-verbatim and unmodified.

Pre-write dedup (2026-10-17): working-tree case-insensitive content search for `williams_ema_reclaim` / `ema-reclaim` / `ema reclaim` / `wr_entry` / `PREBUILT-WILLIAMS` returns zero strategy records. Filename search for `williams` returns exactly three records — `williams-r-level-cross-mean-reversion-long-btcusdt-1d-2026-10-09.md` (raw WR14 cross-up-through-80 entry / cross-down-through-20 exit, no EMA gate, no second exit leg, different thresholds, different source), `williams-fractal-ema-band-fixed-rr-two-sided-btcusdt-1d-2026-10-10.md` (fractal breakout with fixed risk-reward, a different mechanism class), and `alorse-williams-vix-fix-dual-reversal-bb-20261016.md` (Williams VIX Fix, a different indicator) — fenced in Negative evidence 7. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: the EMA-support conjunction plus the disjunctive dual exit is a different signal construction from the raw level-cross record, not a threshold re-tuning (fenced in Negative evidence 7–8).

## Economic mechanism

### Source-reported

The source claims only what its two sentences print: a `Williams %R recovery strategy with EMA support filter` that buys `when Williams %R(14) recovers through -70.0 while price is above EMA(21)` and exits `near momentum exhaustion at -25.0`. No behavioural, structural, or risk-premium channel is claimed anywhere in the 107 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Oversold-recovery with trend-support veto, long-only, edge-triggered. Williams %R(14) pinned below -70 marks a close hugging the 14-bar low; the cross back up through -70 is the recovery edge, but it fires only while the close holds above its own EMA(21) — recoveries printed beneath the trend filter are vetoed outright. The position then rides until either momentum rolls over (Williams %R crossing back down through -25, the exhaustion leg) or the trend support itself breaks (close below EMA(21), the safety leg). Unlike the admitted raw level-cross record (which takes every -80 reclaim and holds until a -20 rollover with no other condition), this rule trades a strict subset of those bars — only supported recoveries — and can exit earlier via the EMA-loss leg. Unlike RSI-reclaim systems there is no Wilder smoothing anywhere: Williams %R is a pure 14-bar position-within-range ratio, so the trigger reacts on the bar the range position flips, with no averaging lag beyond the EMA(21) gate itself. Unlike band-fade systems there is no dispersion denominator — the oscillator is range-normalized to [-100, 0] by construction. The failure mode is plain: chop around the -70 rail prints repeated reclaim-then-rollover round trips, and a vertical drop through the EMA exits late at the same-bar close with no guardrail beyond the two signal legs.

## Signal

Exact rule as pinned (any other periods, thresholds, gate polarity, exit legs, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own:

```text
highest_high = high.rolling(14).max()     // 14-bar highest high
lowest_low   = low.rolling(14).min()      // 14-bar lowest low
wr           = -100 * (highest_high - close) / (highest_high - lowest_low)
ema          = close.ewm(span=21, adjust=False).mean()
support_ok   = close[-1] >= ema[-1]
entry        = (wr[-2] < -70.0) and (wr[-1] >= -70.0) and support_ok
exit_        = ((wr[-2] > -25.0) and (wr[-1] <= -25.0)) or (close[-1] < ema[-1])
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (literal — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops.
- Direction: long-only. The short side is absent by construction (0 `short` / 0 `sell` in the file) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the dual signal exit (exhaustion cross OR EMA loss) is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence=round(min(1.0, abs(wr)/100.0), 4)` is a deterministic passenger of the current Williams %R value and `indicators={"wr","ema","support_ok"}` is diagnostic — neither conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on the next reclaim bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Conflict priority (provably irrelevant): entry and exit cannot fire on the same bar. Entry requires `wr[-2] < -70.0`; the exhaustion exit leg requires `wr[-2] > -25.0` — no value (and no NaN, for which both strict comparisons are false) satisfies both. Entry requires `close[-1] >= ema[-1]`; the EMA-loss exit leg requires `close[-1] < ema[-1]` — mutually exclusive on every print. Hence every bar resolves to at most one of {entry, exit, neither}. No priority rule is needed and none is missing.
- Determinism note for the reviewer: the rule reads only `high` / `low` / `close` with causal rolling extrema (default `min_periods`, no negative shift), a causal `ewm(adjust=False)` recursion, and one `.shift(1)` previous-row read — no `request.*`, `security()`, `timeframe*`, `barstate.*`, volume-weighted logic, session/calendar call, or stop/limit order argument anywhere in the file (verified by the census above returning zero matches). The scalar `generate_signal` and the vectorized `generate_signals` (with `.fillna(False)`) agree edge-for-edge, so NaN-seed rows fire nothing under both paths. The `compatible_regimes` set is metadata never read by either signal path (both take only `df`/`params`), so no regime model gates any order.

## Required data

- `1h` bars of one pair: `high` + `low` (Williams %R range rails), `close` (range position, EMA(21) construction, support tests). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade/aggressor, L2/order-book, on-chain, options/Greeks, sentiment/news, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; every test reads trailing completed bars of the same three series, never a second feed).
- Warmup: 30 completed `1h` bars flat by record rule — structural minimum is the 15th completed bar (14-bar rolling extrema seed plus one shift row; pre-seed rows are NaN and every strict comparison on NaN is false, so no edge can fire pre-seeding; verified against both signal paths). Pre-warmup bars are flat by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (every window reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance `1h` under the house overlay (researcher pin per the declaration — the file names no venue/timeframe; the roster pins `_asset BTC` and all four admitted sibling Forven records execute Binance `BTC/USDT-1h`; no source-market equivalence is claimed).
- Order timing (predeclared derivation): completed-bar decisions with same-bar-close market fills for entries and exits — the file returns `price=round(close, 4)` (the close), and the identical primitive is already admitted on the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) by the sibling S01508, inside-bar-failure-fade, and forven-inside-bar records. This record claims no other fill convention: no perfect-open print, no maker-touch, no intrabar-path-dependent fill. Zero stop/limit legs exist, and entry/exit are proved mutually exclusive per bar, so there is no same-bar TP/SL ordering ambiguity.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing/time orders by record rule. No hidden Hummingbot stop-order defaults are relied upon.
- Sizing/capital/costs: the file ships no sizing, capital, fee, or slippage concept beyond the bare `leverage: 2.0` backtest default (quoted verbatim; inside the house 3x/5x overlay range). The explicit house overlay (single-unit frame, pinned house taker fees both legs, modeled funding while long, nothing while flat) applies to the derived evaluation here, never presented as source-native behavior. Funding is never zero-claimed: longs held across the `00:00`/`08:00`/`16:00 UTC` stamps carry modeled funding.
- Concurrency: at most one single-asset long position at any time; an exit closes it in full. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (pinned commit `e9a6c09`, file `forven/strategies/builtin/williams_ema_reclaim.py`, blob `e50099d1`, 3766 bytes / 107 lines, HEAD re-confirmed via `ls-remote` this cycle): the `Williams %R recovery strategy with EMA support filter.` docstring; the `Buy when Williams %R(14) recovers through -70.0 while price is above EMA(21); exit near momentum exhaustion at -25.0.` describe string; the `PREBUILT-WILLIAMS-EMA-RECLAIM-BTC` / `_asset BTC` roster tuple; the `{ "wr_period": 14, "ema_period": 21, "wr_entry": -70.0, "wr_exit": -25.0, "leverage": 2.0 }` defaults; the `{"RANGE_BOUND", "TREND_UP"}` metadata set; the `{"wr_entry": (-85, -55, 5), "wr_exit": (-35, -10, 5), "ema_period": (10, 34, 3)}` parameter surface (disclosed, unused); the verbatim Williams %R helper, EMA construction, entry/exit boolean lines in both `generate_signal` and `generate_signals`. This record claims no source-reported performance number of any kind — the file ships no table, figure, return, win rate, trade count, or cost model — and no reproduced performance exists.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 stop/limit/profit/loss/qty/fee/slippage/commission/pyramid/position-size tokens in the file — the dual signal exit is the sole position-ending path by construction, and the file promises no stop or target.
2. Entry/exit mutual exclusivity proved in Signal (previous-bar Williams %R cannot be both `< -70.0` and `> -25.0`; current close cannot be both `>=` and `<` the EMA — NaN satisfies neither side) — no same-bar entry-vs-exit ordering ambiguity exists to resolve.
3. Strict edges, pinned: a touch without crossing (`wr[-2] == -70.0`, `wr[-1] == -25.0`), a hold below/above without an edge, and NaN-seed rows fire nothing under both signal paths; a zero-range 14-bar window (`highest == lowest`) yields NaN, never a signal. Ties are dead bars, pinned, not smoothed.
4. Flat-state and held-state determinism: exit bars while flat are no-ops; entry bars while long are no-ops under the predeclared single-unit rule; the seed bars satisfy no order condition by themselves (every edge needs the previous row).
5. Metadata fenced, admitted plainly: `compatible_regimes`, the `confidence` passenger, and the `wr`/`ema`/`support_ok` indicator flags are never read by any order-gating line — a reviewer must not graft a regime filter, confidence gate, or alternate exit onto this record.
6. Derivation boundary fenced: the only non-source-native behaviors are the BTCUSDT-`1h` research frame, same-bar-close fills, the 30-bar warmup, single-unit no-pyramid booking, and house sizing/costs — all predeclared above; every edge, strictness, conjunction, direction scope, and risk posture is source-verbatim. This record is therefore never evidence that the Forven engine's own timing or sizing passes.
7. Overlap fences, admitted plainly: the admitted `williams-r-level-cross-mean-reversion-long` record takes raw WR(14) cross-up-through-80 entries to cross-down-through-20 exits with no gate of any kind on `1d` (every deep reclaim fires there, and only the exhaustion cross exits); this record takes only EMA-supported -70 reclaims with a second EMA-loss exit leg on `1h` (unsupported reclaims fire nothing here; EMA-loss bars exit here but never there) — different entry subsets, different exit structure, different thresholds, different timeframe, different source. The admitted `williams-fractal-ema-band-fixed-rr` record trades fractal breakouts with fixed risk-reward (a breakout-plus-bracket mechanism, no oscillator edge, no exhaustion exit); `alorse-williams-vix-fix-dual-reversal-bb` trades the Williams VIX Fix (a volatility-spike oscillator, no %R range-position edge). Shared `Williams` naming is not shared signal.
8. No hidden variants admitted: any other periods, thresholds, gate polarity, single-exit simplification, other frame, fill, venue, or book is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: WR(14) / EMA(21) / -70 reclaim-with-support entry / dual exhaustion-or-EMA-loss exit / long-only / `1h` BTCUSDT / same-bar-close fills / no-stop posture are frozen.

- F1 — Gate relevance: a raw-Williams twin (same -70/-25 edges, no EMA-support conjunction, no EMA-loss exit leg — same book, fills) must not improve net expectancy; fail ⇒ the EMA-support construction adds nothing over the raw oscillator edge here.
- F2 — Dual-exit relevance: a single-exit twin (exhaustion cross only, no EMA-loss leg — same entries, book, fills) must not improve net expectancy; fail ⇒ the EMA-loss safety leg adds nothing over the pure exhaustion exit on this market.
- F3 — Threshold relevance: a -80/-20 twin (the admitted level-cross calibration applied inside this record's EMA-gated structure — same gate, exits, book, fills) must not improve net expectancy; fail ⇒ the -70/-25 calibration adds nothing over the admitted calibration here.

## Crypto portability

Pinned to BTCUSDT Binance `1h` under the house overlay. The rule reads completed hourly bars only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (crypto trades 24/7; Williams %R range rails form purely on printed highs/lows, and the file reads no `open`, so session-gap behavior is simply absent rather than approximated). The geometry is denomination-free (a range ratio plus a price-vs-average test — no USDT-scale threshold to dwarf or reweight). The rule is long-only, so a spot deployment expresses every firing bar while no short leg ever needs a venue (never silently converted). No warmup history beyond 30 `1h` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop: a recovery that reverses vertically is held until an exhaustion cross or an EMA-loss close prints — the record's principal risk, carried over exactly from source.
- EMA-loss exit lag (disclosed): the safety leg triggers on closes, so a gap-through-EMA bar exits at the same-bar close after the full adverse excursion — the coded cost of the literal implementation, not a designed stop.
- Chop grind: sideways `1h` regimes print repeated -70 rail touches whose reclaims reverse immediately, exercising the entry-then-exhaustion-exit path often — expected behavior, not a bug.
- Derived fill timing and frame: same-bar-close fills and the `1h` BTCUSDT frame are researcher pins (the file stamps neither); backtest economics under any other timing or frame differ by construction.
- Single-venue port residual: Forven backtest prints/fees/funding/margin mechanics beyond the house model are unclaimed, disclosed.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest (the file's `parameter_space()` documents a search surface this record never enters).
- Author scope: Forven ships backtest demos as research objects, not a vetted retail trading system — this record is research-only and claims no live suitability.

## Implementation status

- `not-implemented`. No Hummingbot/Qlib/n8n/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `research-only`, `not-approved`. Admission of this record would mean only that its core signal and causal trade-event semantics are losslessly expressible under the pinned backtester with the labeled house overlay — not profitability, survival, or any trading approval.

## Related Wiki records

- None. No Wiki Brain write was performed for this cycle.

## Sources

- Immutable program file at pinned commit (all rules): https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/williams_ema_reclaim.py
- Repository (project context): https://github.com/judder659/Forven
