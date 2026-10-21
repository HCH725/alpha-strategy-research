---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade MultiMa TEMA-stack trend-state long-flat on BTCUSDT 4h bars
created: 2026-10-21
updated: 2026-10-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/MultiMa.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade MultiMa TEMA-stack trend-state long-flat on BTCUSDT 4h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (official open-source Freqtrade strategy collection; the lane that already supplied the admitted `freqtrade-hlhb`, `freqtrade-quickie`, `freqtrade-simple-macd-bb-rsi`, `freqtrade-cofibit`, and `freqtrade-strategy005` records at this same pin — this record pins ONLY the MultiMa literals below, and no reviewer repair may substitute a sibling constant).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/MultiMa.py`.
- GitHub blob SHA at the pinned commit: `dd398f7f54ddf921678d63329c8612450d2b4bcf`, size 3464 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3464 bytes, 99 lines, SHA-256 `cae77a6c8f983377e392a2c66bfc541e7c1400fae03c3a413194902b2eda6626`, identical to the GitHub blob (`git hash-object` reproduces `dd398f7f…b4bcf`) — the entire file was retrieved and inspected.
- Registration: the file defines class `MultiMa(IStrategy)` (the only class in the file), `INTERFACE_VERSION = 3`, framework column contract `populate_entry_trend` / `populate_exit_trend` (`enter_long` / `exit_long`, never the old `buy`/`sell` plumbing). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path plus pin, all unique. Every other `user_data/strategies/*.py` sibling is a different pin with different constants.
- The file's own words (quoted for gate evidence, never extended): `timeframe = "4h"`; `minimal_roi = { "0": 0.523, "1553": 0.123, "2332": 0.076, "3169": 0 }`; `stoploss = -0.345`; `trailing_stop = False` (with `trailing_stop_positive = None`, `trailing_stop_positive_offset = 0.0`, `trailing_only_offset_is_reached = False` present-but-disabled); `count_max = 20`, `gap_max = 100`; frozen hyperopt file literals `buy_params = { "buy_ma_count": 4, "buy_ma_gap": 15 }` and `sell_params = { "sell_ma_count": 12, "sell_ma_gap": 68 }`; entry reduction `reduce(lambda x, y: x & y, conditions)` (AND); exit reduction `reduce(lambda x, y: x | y, conditions)` (OR). The docstring attribution (`MultiMa Strategy V2 / Author: @Mablue`) is lineage only.
- Out-of-file calls pinned (all resolved by name, all standard defaults): `ta.TEMA(dataframe, timeperiod=int(count*gap))` (TA-Lib abstract triple-EMA over the default `close` input — the ONLY indicator family in the file); `functools.reduce` (pure boolean folding, no state); `print(" ", metadata['pair'], end="\t\r")` (stdout side effect once per pair per evaluation — display leftover with no gate effect, fenced). `qtpylib` is imported and never called (display leftover — fenced, not repaired). No DB, no network, no `request.*`, no `security()` in the file.
- Full-file token census (verified over the 99 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `volume` (no volume read of any kind); 0 `resample` / 0 `merge_informative_pair` / 0 `informative` beyond the absent stub (no informative pair is ever declared — single-frame by construction); 0 `position_adjustment` / 0 `max_open_trades` / 0 `startup_candle_count` / 0 `process_only_new_candles` / 0 `use_exit_signal` / 0 `exit_profit_only` / 0 `order_types` / 0 `can_short` / 0 `leverage` / 0 `funding` / 0 `mark_price` (all such execution/position/economic semantics are predeclared researcher pins below, never file semantics); 0 `fillna` / 0 `ffill` / 0 `interpolate` (no NaN patching anywhere — strict NaN comparisons simply stay false); 0 `shift` (no bar offset anywhere — both legs read the decision bar only); 0 `crossed_above` / 0 `crossed_below` (both legs are level prints, never edges); 4 `Parameter` tokens (the four `IntParameter` declarations plus the `buy_params`/`sell_params` freeze — the optimize-spaces are fenced out, the frozen file literals are the rule, see Signal); 0 `position_size` reads; 0 `syminfo` (the file names no market).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. The file is causal as written (no full-sample scalar, no repainting primitive, no multi-timeframe merge, no external package — no repair site exists). Researcher-declared adaptations are exactly five: (1) research market `BTCUSDT` (the source names no market); (2) completed-bar decisions with same-bar-close market fills; (3) single-unit/no-add/no-cooldown position pin plus an 800-bar researcher warmup pin (covers the 748-bar longest TEMA seed with margin); (4) framework-default execution semantics pinned as derived behaviour (signal exits enabled, firing at any close; ROI/stop legs bar-close-evaluated — disclosed, never presented as file literals); (5) the house cost/capital overlay replaces the absent source economics. Every threshold, every lookback, the frozen hyperopt literals, the entry AND, the exit OR, the ROI ladder, and the stop are untouched.

Pre-write dedup (2026-10-21): working-tree filename/content search for `MultiMa`, `buy_ma_count`, `buy_ma_gap`, `sell_ma_count`, `sell_ma_gap` returns zero strategy records — the single `MultiMa` hit pool-wide is a prose sibling-fence mention in the admitted HLHB record (which pins `hlhb.py`, never this file). No TEMA-stack count-times-gap record exists anywhere on `main`. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas) trades a TEMA-stack system. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims no behavioural channel anywhere in the 99 lines beyond its code: stack Triple-EMAs so that the shorter averages sit above the longer ones, enter the bar where the 15/30/45-bar TEMA ladder stands bullishly stacked, and stand aside to flat when any rung of the wider 68-step TEMA ladder inverts — behind a decaying take-profit ladder (52.3% immediately down to breakeven after ~52.8 h) and a −34.5% stop. The one pasted hyperopt comment (`18 trades … 73.30%`) ships no pair list, window, dates, or cost basis and is quoted here as file text only — this record claims no source-reported performance from it.

### Research interpretation

Slow-stack trend-state follower, long-only, with a hair-trigger OR exit. Unlike single-MA cross systems that flip on one pair of averages, the entry demands a full three-rung TEMA ladder in bullish order (15 above 30 above 45 — a persistent trend state, not a momentary cross), so chop that merely wiggles one average prints nothing. Unlike trailing-stop exits, the exit is a ten-rung inversion watch: any longer TEMA rising back above its shorter neighbour (136 over 68, 204 over 136, … up to 748 over 680) closes the book — the position survives only while every watched rung of the slow ladder stays bearishly ordered under the fast side. The coded consequence is a buyer of established TEMA-stack trends that harvests the slow-ladder persistence, the decaying ROI ladder, or the wide stop — and that exits fast at the first slow-rung inversion rather than waiting for the fast stack itself to flip.

## Signal

Exact rule as pinned (any other hyperopt literal, lookback, threshold, average family, reduction, ROI rung, stop, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
TEMA(p)[t] = TA-Lib TEMA(close, timeperiod=p) for every integer p = count*gap > 1
             with count in 0..19, gap in 0..99  // indicator bank; frozen legs read p in {15,30,45} and {68..748}
entry = (TEMA30[t] < TEMA15[t]) AND (TEMA45[t] < TEMA30[t])   // enter_long = 1 (2-condition AND)
exit_sig = (TEMA136[t] > TEMA68[t]) OR (TEMA204[t] > TEMA136[t]) OR (TEMA272[t] > TEMA204[t])
        OR (TEMA340[t] > TEMA272[t]) OR (TEMA408[t] > TEMA340[t]) OR (TEMA476[t] > TEMA408[t])
        OR (TEMA544[t] > TEMA476[t]) OR (TEMA612[t] > TEMA544[t]) OR (TEMA680[t] > TEMA612[t])
        OR (TEMA748[t] > TEMA680[t])                           // exit_long = 1 (10-condition OR)
risk = decaying take-profit minimal_roi {"3169":0,"2332":0.076,"1553":0.123,"0":0.523};
       fixed stop at -34.5% (stoploss -0.345); trailing_stop False (None/0.0/False present-but-disabled)
guard = leading-window bars: NaN comparisons false (see Required data)
```

- Derivation of the frozen legs (pinned arithmetic, verified this cycle — not a reviewer repair site): entry iterates `ma_count` over `range(4)` with gap 15: `ma_count=0` yields `past_key=-15` (fails the `past_key > 1` guard — skipped); `ma_count=1` yields `past_key=0` (period 0 is never computed since products must exceed 1 — skipped); `ma_count=2,3` yield the two quoted legs, AND-folded. Exit iterates `ma_count` over `range(12)` with gap 68: `ma_count=0,1` skip by the same guards; `ma_count=2..11` yield the ten quoted legs, OR-folded. Adopting any other `buy_ma_count`/`buy_ma_gap`/`sell_ma_count`/`sell_ma_gap` point — including the `IntParameter` defaults (7/7/7/94) — would be a different, unpinned rule.
- Trade events: `enter_long=1` on any bar printing the two-conjunct stack state, `direction` long-only; `exit_long=1` on bars printing any of the ten inversion rungs. Both legs are STATE prints (persist while true — close-and-hold-flat); either leg can reprint across consecutive bars (no one-shot latch in code). New-interface `enter_long`/`exit_long` columns read as enter-long/exit-long directly.
- Hyperopt freeze (pinned file literals, never tuned here): entry uses `buy_ma_count=4`, `buy_ma_gap=15` exactly as printed in `buy_params`; exit uses `sell_ma_count=12`, `sell_ma_gap=68` exactly as printed in `sell_params`. The `IntParameter(1, count_max)` / `IntParameter(1, gap_max)` ranges are unfrozen search scaffolding — excluded from the rule. The author's code comment on `range(self.buy_ma_count.value)` vs `.range` is implementation trivia explaining the frozen iteration — quoted, never extended.
- Exact boundaries (pinned semantics): strict throughout (`<`, `>` exactly as coded — a TEMA landing exactly on its neighbour fires nothing on that rung). The `20` / `100` / `4` / `15` / `12` / `68` literals are never tuned here.
- Same-bar co-print pin (possible, resolved by position pin — disclosed, not repaired): entry reads periods {15,30,45} while exit reads {68..748} — disjoint period sets, so one bar CAN print both the bullish fast stack and a slow-rung inversion. No engine ordering is invented: under the single-unit position pin, a flat book treats any residual co-print bar as entry (the exit leg needs a position and is a no-op without one — no same-bar round-trip), while a positioned book treats it as exit-close. ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
- Direction: long-only. Zero `short` tokens ship anywhere — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the ten-rung inversion signal exit, the four-rung decaying ROI ladder, and the −34.5% stop are the complete position-closing set. No trailing (`trailing_stop = False` file literal — the `None`/`0.0`/`False` values are present-but-disabled, never to be enabled by repair), no time exit beyond the ladder, no breakeven move — explicitly none, not invented. Signal-exit/profit-gating and ROI-on-entry-bar semantics ride the predeclared derived behaviour (Execution assumptions), never a file invention.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment`/`max_open_trades` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying stack bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (TEMA internals — the sole indicator family) with fixed non-negative window offsets (no bar-shift edge anywhere — both legs read the decision bar only, no forward reference) — no volume/funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `4h` bars of BTCUSDT: `close` only, for the entire TEMA bank (periods up to 748). No `high`/`low`/`volume`, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `4h` (source-native — the file prints `timeframe = "4h"`). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 800 four-hour bars held flat (~133.3 days). Covers the 748-bar longest TEMA seed (the exit's outermost rung), the 680-bar neighbour seed, the 45-bar entry seed, and the full indicator-bank construction with margin. Coded behaviour underneath: TA-Lib seeds print NaN until windowed (every strict NaN comparison false — no leg can fire early; no `fillna`/`ffill` exists to smear them). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, signal exit, and ROI/stop legs are all bar-close-evaluated; the Signal co-print rule leaves no ambiguous same-bar fill order to the engine beyond the disclosed position pin.
- Interval precedent (exact, disclosed): an exact-`4h` PASS record already sits on `main` (the admitted HLHB EMA-RSI-ADX quad-gated record — `4h` Freqtrade-sourced long-flat at this same repository pin) — this record rides the same specified single-frame completed-bar `4h` Binance candle path, not an assumed one. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the same specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding. The close-only feed is a strict subset of that path's candle (no volume leg exists here at all).
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentage are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the stack-state entry opens the full unit on a flat book; any inversion rung, any ROI rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying stack bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (99 lines: the TEMA-bank indicator loop, the two-conjunct AND entry with its frozen count/gap literals, the ten-rung OR exit with its frozen count/gap literals, the `timeframe`/`minimal_roi`/`stoploss`/`trailing_stop` literals, the `buy_params`/`sell_params` freeze, and the `MultiMa(IStrategy)` class pin). The pasted hyperopt comment (`111/2000: 18 trades … 733.01234143 USDT (73.30%)`) ships no pair list, evaluation window, dates, or cost basis — this record claims no source-reported performance and no reproduced performance from it.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib TEMA seeds print NaN until windowed (every strict NaN comparison false — no early entry, no early exit; no `fillna`/`ffill` exists to smear seeds forward). The 800-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict `<`/`>` fires nothing on equality on every rung; a TEMA landing exactly on its neighbour holds flat — disclosed, not smoothed.
3. Co-print arithmetic fenced (possible, resolved — disclosed, not repaired): entry periods {15,30,45} and exit periods {68..748} are disjoint, so one bar can print both states. The position pin resolves any residual (flat → enter, positioned → exit-close, never a same-bar round-trip). ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
4. Zero-variance fenced: flat tape pins every TEMA onto the flat line (all strict level legs fail on exact equality — neither entry nor exit can print). No division by zero exists anywhere in the gating path (all legs are comparisons; multi-pass EMA arithmetic lives inside the library call, never in a gate denominator) — disclosed, not repaired.
5. Dead-column plumbing fenced: `qtpylib` is imported and never called; `print` emits stdout per pair with no gate effect; the `IntParameter` ranges, the `default=7/7/7/94` defaults, and the `count_max=20`/`gap_max=100` scaffolding never govern under the `buy_params`/`sell_params` freeze — this record never conditions on them and no reviewer repair may promote any of them into a leg. Adopting any other point of the declared 1..20 / 1..100 spaces would be a different, unpinned rule.
6. Cousin records fenced as different constructions (none trades a count-times-gap TEMA ladder with an AND-stack entry and an OR-rung exit): the admitted Quickie sibling trades a single TEMA(9) slope against the Bollinger midline with an ADX gate and an SMA200 regime filter on `5m` old-interface `buy`/`sell` rails (single-average slope-plus-band construction, never a multi-rung stack; different timeframe, different risk); the admitted HLHB sibling trades an RSI-50/EMA5-6/ADX25 quad-gated cross-state on `4h` (cross edges, never TEMA levels); the admitted strategy001–005 siblings trade HA-EMA-cross / hammer / RSI-Fisher-MFI / ADX-CCI / volume-surge-Fisher systems (no TEMA anywhere). Not a threshold re-tuning of any of them: changing any count, gap, rung, reduction, or risk literal would each be a different, unpinned rule — none is admitted here.
7. Sibling-file fence: every other `user_data/strategies/*.py` sibling is a separate pin — its constants must never be substituted into this record.
8. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the five declared adaptations (BTCUSDT market choice, same-bar-close fills, single-unit/no-add/no-cooldown position pin with 800-bar warmup floor, derived signal-exit/profit-gating execution semantics, house sizing/costs) — all predeclared above. The `4h` frame, the TEMA bank, the frozen two-conjunct AND entry, the frozen ten-rung OR exit, the ROI ladder, the −34.5% stop, the disabled trailer, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: two-conjunct stack entry / all counts, gaps, TEMA periods, reductions, frozen hyperopt literals / ten-rung OR exit / ROI ladder / −34.5% stop / single-unit long-only / `4h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Stack relevance: replacing the two-conjunct AND stack with a single-rung level (same exit/risk) must not improve net expectancy; fail ⇒ the full ladder adds nothing over one TEMA pair.
- F2 — OR-exit relevance: replacing the ten-rung OR exit with ROI/stop-only exits (same entry, same risk) must not improve net expectancy; fail ⇒ the inversion watch adds nothing over fixed risk alone.
- F3 — Slow-rung relevance: dropping the three outermost exit rungs (612/680/748-side legs; same entry, same risk) must not improve net expectancy; fail ⇒ the slowest watch adds nothing over the inner rungs.

## Crypto portability

BTCUSDT Binance perpetual `4h` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. Only the `close` candle field is read (venue close-definition differences move only TEMA inputs, disclosed). Funding is declared nowhere in the source and modeled only downstream by house assumptions. The per-pair `print` ships no market semantics.

## Limitations

- TA-Lib TEMA internals live in their library outside the pinned file — pinned by call with explicit periods, not re-derived; exact reproduction inherits that module's seeding and rolling semantics alongside the file-local count-times-gap wiring, under the disclosed 800-bar floor.
- Hyperopt scaffolding is frozen, not searched: the `IntParameter` ranges, defaults, and the author's `range(.value)` iteration comment never execute as search under this record; only the `buy_ma_count=4` / `buy_ma_gap=15` / `sell_ma_count=12` / `sell_ma_gap=68` literals govern. Any re-optimization would be a different, unpinned rule.
- The indicator bank computes TEMA columns for every count-times-gap product (up to period 1881 in principle) while the frozen legs read only {15,30,45} and {68..748} — the unread columns are computation leftovers with no gate effect; a reader must not mistake bank width for signal.
- No trailing, no breakeven, no time exit beyond the ROI ladder, no short leg, no cooldown — all explicitly absent, never to be added by repair. Signal-exit profit-gating rides the predeclared derived behaviour — disclosed as the record's principal execution risk.
- The file declares no order-type plumbing at all — fills are wholly under the derived same-bar-close convention; this record makes no claim about any live-order behaviour.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/MultiMa.py
- https://github.com/freqtrade/freqtrade-strategies
