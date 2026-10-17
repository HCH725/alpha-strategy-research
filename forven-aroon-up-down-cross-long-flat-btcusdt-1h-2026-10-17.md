---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven Aroon Up-Down cross trend long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/aroon.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven Aroon Up-Down cross trend long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, and `forven-atr-volume-breakout` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/aroon.py`.
- GitHub blob SHA at the pinned commit: `0452697308803e7f87a517660db2a5e7b1a85bd6`, size 3551 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3551 bytes, 117 lines, SHA-256 `8b340cc0aab3f89327ec73bd32f0906cf6cd89d71c79b02dea82302a4c48ab18`, identical to the GitHub blob (`git hash-object` reproduces `04526973…85bd6`) — the entire file was retrieved and inspected; the order-gating rule lives in this one file plus exactly one pinned pure helper (the ATR call below, which is a diagnostic passenger only).
- The file's own words (quoted for gate evidence, never extended): module docstring `Aroon strategy.`; class docstring `Entry: Aroon Up crosses above Aroon Down AND Aroon Up > upper threshold.` / `Exit: Aroon Down crosses above Aroon Up.`; `describe()` returns `Enters when Aroon Up (25) crosses above Aroon Down and Aroon Up > 70. Exits when Aroon Down crosses above Aroon Up.`; `default_params` returns exactly `{ "aroon_period": 25, "upper_threshold": 70, "lower_threshold": 30, "leverage": 1.0 }`; roster entry `("PREBUILT-AROON", AroonStrategy, {"_asset": "BTC"})`; `compatible_regimes` returns `{"TREND_UP", "TREND_DOWN"}`; `parameter_space()` returns `{ "aroon_period": (15, 35, 5), "upper_threshold": (60, 80, 10), "lower_threshold": (20, 40, 10) }` (a documented search surface only — this record pins the defaults and runs no search).
- ATR helper provenance (the file's only out-of-file call): line 51 `from forven.strategies.indicators import atr` resolves through that module's PEP-562 `__getattr__` facade (`_FACADE_NAMES` includes `"atr"`, verified at lines 864–880 of `indicators.py` at the pinned commit) to `forven/scanner.py` `def atr(df, period=14)`: true range `max(high - low, |high - prev_close|, |low - prev_close|)` with `ATR = TR.rolling(14).mean()` — a simple rolling mean, not Wilder smoothing (quoted body read this cycle). The helper is pure pandas over the passed frame (no DB, no network, no global state in the quoted body); `scanner.py` at the pinned commit is 464565 bytes, blob `9a1d77b90bf214c03aa230a5f46775aab94748bd`. The computed `atr_14` series is returned only inside the diagnostic `indicators` dict and conditions zero order lines (see Negative evidence 5).
- Full-file token census (verified by search over the 117 lines this cycle): 1 `direction` literal, `"long"` (hardcoded on every return — the sole order-direction token); 0 `short` / 0 `sell` (no short path anywhere); 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` (no order arguments, no risk legs); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default); 0 `open` / 0 `time` / 0 `request` / 0 `security` / 0 `timeframe` / 0 `barstate` / 0 `funding` (order-gating reads are `high`, `low`, `close`, plus `high`/`low`/`close` inside the quoted ATR helper — zero reads of any other column, no `volume` read anywhere); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal). Imports are only `pandas` plus the local `BaseStrategy, Signal` base — no cross-asset import, no second feed.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the Aroon(25) two-line construction, the Up-cross-Down-plus-Up-above-70 entry, the Down-cross-Up exit, the long-only stance, and the no-stop posture — but ships no venue, no timeframe, no fill-timing flag, and no position-sizing rule inside this file. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(close, 4)` — the decision bar's own close — and the admitted S01508, inside-bar, williams-ema-reclaim, linreg, zscore, adl, and atr-volume records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) an adopted 30-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 27th completed bar — the 26-bar rolling window plus the one-prior-bar cross read — plus margin for the ATR seeding; see Required data); (4) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal). The Aroon arithmetic, the cross-plus-threshold entry, the cross exit, the long-only stance, and the no-stop/no-target/no-time-exit posture are source-verbatim and unmodified.

Pre-write dedup (2026-10-17): working-tree filename/content search for `builtin/aroon` / `PREBUILT-AROON` / `AroonStrategy` returns zero strategy records — no record cites this source file. Content search for Aroon-family records returns only pool cousins fenced as different mechanisms in Negative evidence 8 (FMZ-438795 Aroon-oscillator midline/rail two-sided system; Alorse BB-lower-crossunder gated by AroonUp(288)). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a two-line Aroon Up/Down cross conjoined with an Up-strength threshold and exited on the opposite cross is a different signal construction from a single-line Up-minus-Down oscillator against asymmetric rails, or from a Bollinger-band crossunder with an Aroon recency filter — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: an `Aroon indicator trend-following strategy` of `Enters when Aroon Up (25) crosses above Aroon Down and Aroon Up > 70. Exits when Aroon Down crosses above Aroon Up.` No behavioural, structural, or risk-premium channel is claimed anywhere in the 117 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Recency-persistence trend capture, long-only, state-holding. The Aroon pair asks how recently each side printed its extreme inside 26 bars — not how far price moved — so the signal is a pure timing statistic immune to gap-size distortion. The entry demands both a fresh turn (Up crossing above Down) and proven persistence (Up already above 70, i.e. the window high sits within the most recent ~8 bars), which keeps late-chop crosses from firing. The exit is the mirror cross with no threshold, so a position survives mid-range drift and closes only when the low side demonstrably retakes recency leadership. Unlike level-hold systems there is no repeated-entry pressure: crosses are one-bar edge events, and the predeclared single-unit rule turns any same-side refire into a no-op. The failure mode is plain: a range that whips recency leadership back and forth prints repeated cross-then-cross round trips with no stop and no profit-taking leg, and a slow grind-up whose window high never refreshes within 8 bars never enters at all (opportunity cost, disclosed).

## Signal

Exact rule as pinned (any other period, threshold, average variant, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own:

```text
aroon_up      = ((25 - (25 - argmax(high[-26:])))/25)*100   // % of window since highest high, causal
aroon_down    = ((25 - (25 - argmin(low[-26:])))/25)*100    // mirror on lowest low, causal
up_cross      = (prev_up <= prev_down) and (curr_up > curr_down)
down_cross    = (prev_down <= prev_up) and (curr_down > curr_up)
entry         = up_cross and (curr_up > 70)
exit_         = down_cross
```

- Trade events: `entry_signal=bool(entry)`, `exit_signal=bool(exit_)`, `direction="long"` (hardcoded literal — no short emission exists anywhere in the file, verified by full-file search). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar. Entries while already long are no-ops under the predeclared single-unit rule (see position rule); exits while flat are deterministic no-ops. Crosses are one-bar edge events (strict inequalities on the prior/current pair), so no level-refire pressure exists by construction.
- Mutual-exclusion proof (no tie-break pin required): entry implies `curr_up > curr_down`; exit implies `curr_down > curr_up` — no single bar satisfies both, including the exact-equality boundary (strict comparisons fire nothing on ties). The reviewer is never asked to invent an ordering.
- Direction: long-only. The short side is absent by construction (0 `short` / 0 `sell` in the file) and recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the Down-cross-Up edge is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence=min(1.0, curr_up/100)` on entry bars (else `0.0`) and `indicators={aroon_up, aroon_down, atr_14}` are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying cross after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close` with fixed non-negative offsets (a trailing 26-bar rolling window plus a one-prior-bar cross read) — no `request.*`, `security()`, `timeframe*`, `barstate.*`, volume, funding/OI/mark-price read, session/calendar call, or stop/limit order argument anywhere in the file (verified by the census above returning zero matches). The `len(df) < period + 2` guard returns both signals false on short frames; every pre-seed window prints NaN and every NaN strict comparison is false, so pre-seed bars deterministically print neither signal. Rolling-`argmax`/`argmin` ties resolve to the first occurrence by library semantics — deterministic, identical on every replay. The `compatible_regimes == {"TREND_UP", "TREND_DOWN"}` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule.

## Required data

- `1h` bars of one pair: `high` (Aroon-Up path), `low` (Aroon-Down path), `close` (fill reference only — no close-derived indicator gates any signal). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade/aggressor, L2/order-book, on-chain, options/Greeks, sentiment/news, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; every test reads trailing bars of the same series, never a second feed).
- Warmup: 30 completed `1h` bars flat by record rule — structural minimum is the 27th completed bar (the 26-bar rolling window plus the one-prior-bar cross read; the file's own `period + 2` guard). The extra 3 bars are adopted margin covering the passenger ATR(14) seeding; pre-warmup bars are flat by record rule. Missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (every window reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar. The short-frame `price=0.0` return path is dormant on the declared venue (frames are always full) and can never fill — flat by record rule regardless.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the file names no venue; the roster pins `_asset BTC` — the Binance/BTCUSDT pin is a researcher market choice, disclosed, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The file returns `price=round(close, 4)` — the decision bar's own close — and the admitted S01508, inside-bar, williams-ema-reclaim, linreg, zscore, adl, and atr-volume records establish same-bar-close as the pinned-compatible lane primitive for this exact repository family. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and entry/exit can never co-fire (proven above), so no intrabar ordering assumption is needed at all.
- Engine path for `1h` (gate 5, stated plainly): `1h` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1h` candles (`high`/`low`/`close`) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no volume/funding/OI/mark-price leg. That is the same single-frame completed-bar path as the admitted `1h` siblings from this source family. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the source ships only a bare `leverage: 1.0` default with no capital, fee, slippage, funding, or margin assumption (quoted verbatim in census; the absences are disclosed, never read as zero cost) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior. Under the predeclared single-unit rule the sizing overlay changes no trade event.
- Concurrency: single-unit long-flat book — at most one open long; the Down-cross-Up edge closes the whole unit, and re-entry is allowed on any qualifying cross after any exit (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (Aroon(25) two-line recency pair over a 26-bar window, Up-cross-Down conjoined with Up-above-70, Down-cross-Up exit, fixed long-only stance with the literal `"long"` direction token, no risk legs) and the `PREBUILT-AROON` roster pin. It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` — the sole position-closing path is the coded Down-cross-Up edge. The absence is coded (the signal block ends with the two comparisons and only the diagnostic return follows).
2. Variant menu fenced, stated plainly: the `parameter_space()` surface (`aroon_period` 15–35 step 5, `upper_threshold` 60–80 step 10, `lower_threshold` 20–40 step 10) is a documented search grid the code never runs — this record freezes the `25` / `70` defaults as written; adopting any grid point would be a different, unpinned rule.
3. Edge-trigger fires as written, stated plainly: entry prints only on the cross bar (strict prior/current inequalities), not on every bar holding Up above Down — adding a level-hold posture would be a different, unpinned rule (tested as F2, never adopted).
4. No averaging down, stated plainly: the file is stateless (no position-aware branch exists to implement anything else) — an already-long book treats further entry bars as no-ops under the predeclared single-unit rule.
5. Regime/metadata/passenger quarantine, stated plainly: `confidence`, the three `indicators` fields (including the computed-but-never-gating `atr_14`), and the `compatible_regimes == {"TREND_UP", "TREND_DOWN"}` set are returned inside diagnostic fields or class metadata and read by zero order-gating comparisons — treating any of them as a gate, filter, or sizing input would be a different, unpinned rule. The `lower_threshold: 30` default is declared but never read by any line (dead menu item, disclosed — unlike an exit leg, its absence changes no event).
6. Short-frame path fenced, stated plainly: frames shorter than 27 bars return `price=0.0` with both signals false — flat by record rule, and the zero price can never become a fill on the declared venue (frames are always full length).
7. Co-fire impossibility fenced with proof, stated plainly: entry requires `curr_up > curr_down`, exit requires `curr_down > curr_up` — no bar, including exact-equality boundaries and NaN seed bars (all strict comparisons false), can satisfy both. No tie-break, no ordering assumption, and no reviewer invention is required anywhere in this record.
8. Pool-cousin fence (Aroon-family records), stated plainly: `aroon-oscillator-midline-rail-exit-btcusdt-1d-2026-10-09.md` trades the single-line oscillator `Up − Down` against asymmetric rails (midline −25 entries, 75/−85 rail-turn exits), two-sided with reversal, on BTCUSDT `1d` from FMZ source 438795; `alorse-bb-aroon-lower-cross-under-long-20261016.md` enters on a Bollinger lower-band crossunder gated by `AroonUp(288) > 90` (mean-reversion dip-buy, exits on regained bands or `AroonUp < 70`), from an Alorse Pine source. This record crosses two separate Aroon lines with a strength-threshold conjunction and exits on the opposite cross, long-flat, on BTCUSDT `1h`, from immutable file `builtin/aroon.py` — different input construction × different trigger × different gate × different exit × different direction scope × different source file. This record is therefore never evidence for those rules, and those records are never this rule's provenance.
9. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT market pin, the `1h` frame adoption, same-bar-close fills (with live intrabar behavior scoped out), the adopted 30-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the Aroon arithmetic, the cross-plus-threshold entry, the cross exit, the order stance, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, timing, input set, or the Forven engine's own execution semantics passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: Aroon(25) two-line cross / Up-above-70 conjunction / Down-cross-Up exit / long-only / BTCUSDT `1h` / same-bar-close fills are frozen.

- F1 — Threshold relevance: dropping the `curr_up > 70` conjunction (pure Up-cross-Down entry, same exit) must not improve net expectancy; fail ⇒ the coded persistence gate adds nothing over its ungated twin.
- F2 — Edge relevance: replacing the cross-edge entry with a level-hold entry (Up above Down on every such bar, same threshold, same exit) must not improve net expectancy; fail ⇒ the coded edge adds nothing over its level twin.
- F3 — Construction relevance: replacing the Aroon cross with a same-structure fast/slow EMA cross (same edge entry shape, same opposite-cross exit) must not reproduce-or-beat net expectancy; fail ⇒ the record is a moving-average-cross variant wearing a recency label.

## Crypto portability

Pinned to BTCUSDT Binance futures `1h` under the house overlay (market pin is a researcher choice following the file's `_asset BTC` roster pin; the file itself is venue-agnostic). The rule reads no `volume` tape and no funding/OI/mark-price leg, so venue volume-definition differences cannot move any gate — stated plainly as a portability strength with a boundary: cross-venue porting without re-verification would still be a different, unpinned claim, disclosed. The rule is long-only with no stop leg, so a spot-only deployment expresses it fully, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the file returns the decision bar's own close but ships no explicit fill-timing flag; this record evaluates completed bars only and executes same-bar-close on BTCUSDT `1h`. Any live intrabar behavior is out of scope.
- Derived market pin: the file names no venue and no timeframe (roster pins `_asset BTC` only) — BTCUSDT `1h` is a researcher market/frame choice for the house universe, never a source claim.
- Source economics are leverage-only: beyond the bare `leverage: 1.0` default the source ships no capital sizing, no fee, no slippage, no funding, and no margin assumption — derived evaluation must carry the full house cost load (fees plus historical funding; no hypothetical zero funding claimed), and this record reports no net performance of its own.
- No price stop, no time stop: adverse excursion after placement has no guardrail beyond the opposite cross; a range that whips recency leadership prints repeated entry-then-exit round trips by construction, and a grind-up whose window high never refreshes within 8 bars never enters (opportunity cost, disclosed). This is the coded posture, disclosed as the record's principal risk.
- Seed bars: the 26-bar rolling window plus the one-prior-bar cross read dominate early bars; the first 30 `1h` bars are flat by record rule, so early-history signals never enter any evaluation. Substituting a seeded/warm-started average would move every early print and is a different, unpinned rule.
- Dead menu item: `lower_threshold: 30` is declared but never read — disclosed in Negative evidence 5; a future reader must not mistake it for a gate.
- No co-fire corner exists: see Negative evidence 7 — entry and exit are mutually exclusive by construction on every bar, so no tie-break pin was adopted.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record; the six-gate claim is pinned-engine expressibility of the declared rule, never a profitability, parity, or trading authorization.

## Adoption boundary

Research-only, not approved. No live, Paper, or Testnet authorization follows from this record. Any downstream standardized overlay (house DCA/capital/leverage), Qlib screening, or Hummingbot re-validation is a separate, explicitly authorized step outside this record.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/aroon.py (primary source — executable Python strategy, 117 lines, fetched live 2026-10-17 at pinned HEAD commit, 3,551 bytes, SHA-256 `8b340cc0…4c48ab18`; ATR helper `forven/scanner.py` read at the same commit, 464,565 bytes, blob `9a1d77b9`, diagnostic passenger only; no performance figure ships anywhere in either file)
- https://github.com/judder659/Forven (repository home; HEAD verified `e9a6c09` by `git ls-remote` this cycle)
