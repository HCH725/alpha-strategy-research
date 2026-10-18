---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven classic pivot S1-bounce R1-target long-flat on BTCUSDT 1h bars
created: 2026-10-18
updated: 2026-10-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/pivot_point.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven classic pivot S1-bounce R1-target long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-rolling-cross`, `forven-chaikin-mf-threshold-cross`, `forven-elder-ray-bull-power-cross`, `forven-adx-trend-pulse-reclaim`, `forven-dema-cross`, `forven-trix-signal-cross-zero-gate`, `forven-ultimate-oscillator-cross-gated`, `forven-bollinger-s00120-rsi-breakout`, `forven-three-bar-reversal-decline-gated`, and `forven-atr-breakout-channel` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/pivot_point.py`.
- GitHub blob SHA at the pinned commit: `8ba19bf7588317c470cab91ac404f21852d65eb3`, size 2457 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 2457 bytes, 81 lines, SHA-256 `20680b93eb5cef5392735d8dc7750fc3d1cc7529a77c178eae75840198eebdf8`, identical to the GitHub blob (`git hash-object` reproduces `8ba19bf7…d65eb3`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = PivotPointStrategy`, `TYPE_NAME = "pivot_point"` (line 14), and the `STRATEGIES = [("PREBUILT-PIVOT", PivotPointStrategy, {"_asset": "BTC"})]` roster pin (line 81).
- The file's own words (quoted for gate evidence, never extended): module docstring `Pivot Point Support/Resistance Bounce strategy.` / `Calculates classic pivot points (Pivot, S1, R1) from the previous bar's high, low, and close. Enters long when price bounces off S1 and exits at R1.` (lines 1–6); `describe()` returns `Classic pivot point strategy using a {lb}-bar lookback. Enters long on a bounce off S1 and targets R1 for exit.` (lines 31–35); `default_params` returns exactly `{ "lookback": 1, "leverage": 1.0 }` (lines 26–28); `compatible_regimes` returns `{"RANGE_BOUND"}` (lines 30, metadata never read by the signal path); `parameter_space()` returns `{ "lookback": (1, 5, 1) }` (lines 78–79, a documented search surface only — this record pins the 1 default and runs no search).
- Single decision path (verified line by line): `generate_signal()` (lines 37–76) is the sole signal method — no `generate_signals` vectorized twin exists anywhere in the file (0 matches), no scalar delegate, no second decision logic exists to diverge. The `confidence` computation (line 68) and the three `indicators` fields (`pivot`, `s1`, `r1`, lines 69–73) are diagnostic echoes of levels that already gate the predicates — the confidence value itself never enters any predicate.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults (lines 69–70), `direction: str = "long"` default (line 72), plus `__post_init__` coercion that refuses non-Boolean flags and resolves direction labels (`_normalize_signal_flag`, `_normalize_signal_direction`, lines 140–178) — flags arriving as strict booleans (as here, via `bool(...)` at lines 62–63) pass through unchanged, and the constant `direction="long"` (line 67) resolves to the long book.
- Full-file token census (verified by search over the 81 lines this cycle): `direction="long"` constant (line 67 — the ONLY direction literal in the file); 0 `short` / 0 `sell` / 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` (no short leg, no order arguments, no risk legs of any kind); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default); 0 `volume` / 0 `funding` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any line, and 0 `open`-series reads anywhere (direct reads are exactly `prev["high"]` / `prev["low"]` / `prev["close"]` for the level arithmetic plus `df["close"]` and `df["low"]` for the decision bar — see Signal); 0 `ema` / 0 `ewm` / 0 `sma` / 0 `rsi` / 0 `atr` / 0 `macd` / 0 `stoch` / 0 `supertrend` / 0 `donchian` (no average, no oscillator, no volatility, no trailing construction of any kind — the sole arithmetic is the three-line floor-pivot formula); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the BTC roster asset, the 1-bar floor-pivot construction, the S1 dip-bounce entry, the R1 target exit, the 3-bar short-frame guard, and the no-stop posture — but ships no venue spelling, no timeframe, no fill-timing flag, no position-sizing rule, and no same-bar entry/exit ordering. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, chaikin-mf, elder-ray, adx-trend-pulse, dema-cross, trix-signal-cross, ultimate-oscillator, bollinger-s00120, three-bar-reversal, and atr-breakout-channel records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit position pin with entry-then-close same-bar ordering (the file carries no position reference and no ordering; an already-long book treats further entry bars as no-ops, a flat book treats exit bars as no-ops, and a bar firing both legs resolves entry first then exit so every co-fire bar ends flat — the Kaufman pivot-breakout sibling establishes entry-then-close as the pinned-Hummingbot-compatible ordering primitive for pivot-family co-fires; pin disclosed, never presented as source-native semantics); (4) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). The 1-bar lookback, the floor-pivot formula, the S1-bounce entry, the R1 exit, the strict/weak boundary mix, the long-only book, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown posture are source-verbatim.

Pre-write dedup (2026-10-18): working-tree filename/content search for `pivot_point` / `PivotPoint` / `PREBUILT-PIVOT` returns zero strategy records citing this source file. The pool's pivot cousins are fenced as different constructions in Negative evidence 9 (Kaufman swing-pivot breakout with `ta.pivothigh/low(3,3)` level registers and high/low-break entries two-sided; Camarilla narrow-band `pC ± pR×(1.1/12)` sticky-state rail system two-sided; no pool record computes classic floor `(H+L+C)/3` with `S1 = 2P−H` / `R1 = 2P−L` dip-bounce logic). No closed `research/*` PR ever carried this source file. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a prev-bar floor-pivot S1 dip-bounce entry with R1 target exit is a different signal construction from any swing-pivot breakout, Camarilla rail, Donchian extreme, or volatility-envelope system — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: classic pivot support/resistance where the previous bar's high, low, and close define the pivot, `S1` is support to bounce from, and `R1` is the target to exit at. No behavioural, structural, or risk-premium channel is claimed anywhere in the 81 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Overnight-level mean-reversion, long-only, state-holding. Unlike swing-pivot breakouts (Kaufman: trade the break of confirmed fractal highs/lows) or Camarilla rails (trade the hold/flip of narrow computed bands), this system trades the classic floor-pivot geography: yesterday's range prints today's support (`S1`) and today's target (`R1`). Entry buys the bar that proves support — an intrabar dip to or through `S1` that still reclaims it by the close — rather than buying a close above resistance. The exit is the symmetric geography completion — a close at or above `R1` banks the full pivot range rather than waiting for a breakdown. There is no stop leg and no profit leg beyond `R1`: a bounce that grinds sideways between `S1` and `R1` without touching the target is held indefinitely, while a bar that spans the whole geography (dip to `S1`, close above `R1`) round-trips flat on the same close under the predeclared ordering rather than holding an already-targeted position.

## Signal

Exact rule as pinned (any other lookback, formula, boundary, fill, frame, book, or ordering is a different, unpinned rule). All identifiers below are the program's own; the single `generate_signal` path (lines 37–76) is the single source of truth:

```text
prev            = bar[t-1]                                   // lookback=1: exactly the prior completed bar
pivot           = (high[t-1] + low[t-1] + close[t-1]) / 3.0
s1              = 2.0 * pivot - high[t-1]
r1              = 2.0 * pivot - low[t-1]                     // r1 - s1 = high[t-1] - low[t-1] >= 0
bounce_off_s1   = low[t] <= s1 and close[t] > s1             // dip-touch plus close reclaim
hit_r1          = close[t] >= r1                             // target touch
short_frame     = fewer than 3 completed bars → flat by source guard
```

- Trade events: `entry_signal=bool(bounce_off_s1)`, `exit_signal=bool(hit_r1)`, direction constant `long` (line 67 — zero short tokens anywhere, verified by the census above). A flat book enters one full unit on an entry bar; a long book exits the full unit on an exit bar.
- Same-bar ordering, predeclared (no reviewer invention beyond the disclosed pin): `r1 >= s1` always (they differ by exactly `high[t-1] − low[t-1]`), so a wide-range bar with `low[t] <= s1` and `close[t] >= r1` fires BOTH legs. The record pins entry-then-close evaluation (the Kaufman pivot-breakout sibling's ordering primitive for pivot-family co-fires): from flat the bar opens long then closes it on the same close (one zero-holding round trip at the same fill price); from long the same-id entry is a no-op (no pyramiding) while the close fires → flat. Every co-fire bar therefore ends flat under both book states, and no third state exists. A flat-range prior bar (`high[t-1] == low[t-1]`) collapses `r1 == s1 == pivot`, and any bar with `low[t] <= pivot` and `close[t] > pivot` co-fires under the same ordering — disclosed, not repaired.
- Exact boundaries (pinned semantics): the dip test is weak (`low[t] <= s1` — a low exactly touching `S1` counts as a touch), the reclaim test is strict (`close[t] > s1` — a close exactly on `S1` enters nothing), and the target test is weak (`close[t] >= r1` — a close exactly on `R1` exits). Pre-guard bars are flat by source rule.
- Direction: long-only. No short-entry path exists anywhere in the file (zero `short` tokens in all 81 lines), and the short side is recorded as explicitly disabled. Spot-compatible (no naked shorting required).
- Exits and risk (explicit): the `R1` touch is the sole position-ending path. Opposite-signal exit is not applicable (no short leg exists). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence = clip((r1 − s1) / close, 0, 1)` (line 68, i.e. the prior bar's range over the decision close) and the three `indicators` fields (`pivot`, `s1`, `r1`) are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further entry bars as no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops. Re-entry re-arms on any qualifying bounce bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and short-frame bars are flat by source rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close` (levels plus dip/close tests); no `open`-series read, no bar `volume`, no indicator call of any kind (the pivot is inline arithmetic: one `iloc[-(lookback+1)]` fetch, three divisions-free linear combinations), no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). The `compatible_regimes == {"RANGE_BOUND"}` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` of the single prior bar for the pivot/`S1`/`R1` arithmetic; `low`/`close` of the decision bar for the dip-bounce and target tests. No `open`-series read, no bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` anywhere; 0 `timeframe` tokens in the whole file).
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; the current bar's dip uses only its own low plus the prior-bar levels (no shift tricks beyond the causal 1-bar fetch); fills land on the decision bar's own close (`price=round(curr_close, 4)`, pinned derived rule).
- Warmup: the source ships its own length guard — `min_bars = lookback + 2 = 3`, and shorter frames return an explicit all-flat Signal (lines 39–46, via `Signal(price=...)` defaults `entry_signal=False, exit_signal=False`). The 3-bar floor covers the 1-bar level fetch with margin. The record adopts this guard verbatim as its flat rule — no researcher warmup pin is needed and none is pretended. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source roster pins `_asset BTC`; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the nineteen admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders. Co-fire bars sequence entry-then-exit at the same close price (one round trip from flat, one close from long — predeclared ordering, Kaufman precedent).
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 1.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add/noop-on-repeat position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one long position at any time; re-entry after an exit needs only the next qualifying bounce bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The disabled short side requires no margin-short modeling.

## Evidence

### Source-reported

The file ships the full construction (81 lines: module docstring with the S1-bounce/R1-target sentences, `TYPE_NAME`, `default_params` at lookback 1 / `leverage 1.0`, the floor-pivot/`S1`/`R1`/bounce/target arithmetic, the 3-bar guard, the constant `direction="long"` and the `round(curr_close, 4)` price echo, the `PREBUILT-PIVOT` roster pin). It ships zero adopted performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` ship anywhere — the sole position-closing path is the `R1` touch. The absence of any stop is coded absence, disclosed, not a tunable parameter here.
2. Co-fire ambiguity fenced with a predeclared primitive: a spanning bar fires both legs (proven above — `r1 >= s1` always, equality at zero-range priors). Unlike mutual-exclusion records that need no ordering pin, this record pins entry-then-close (Kaufman precedent): every co-fire bar ends flat from either book state. Any engine evaluating entries before exits on one close reaches the same single end state.
3. Zero-range collapse fenced: an exactly flat prior bar pins `r1 == s1 == pivot`, and any uptick bar with a low at or below the pivot both enters and co-fires. Strictness is preserved (`close == pivot` still enters nothing and — since `r1 == pivot` — exits nothing on an exact-touch close without reclaim), but selectivity collapses with volatility — disclosed, not repaired.
4. Sideways-hold fenced: a bounce that drifts between `S1` and `R1` without printing an `R1` close is held indefinitely — no time exit, no profit leg, no trailing guardrail exists to end it. Disclosed, not repaired.
5. Confidence diagnostic fenced: `(r1 − s1) / close` (the prior range over the decision close, clipped to [0,1]) never enters any predicate — an engine that skips computing confidence reaches identical events. The `pivot`/`s1`/`r1` indicator echoes duplicate the predicate levels and likewise change no event when skipped.
6. Short-frame behaviour fenced: frames shorter than 3 bars resolve all-flat by the source's own guard (explicit `Signal(price=...)` defaults, lines 39–46) — a coded behaviour, disclosed; no engine path ever passes an empty frame (backtests feed full history; the record floor starts at bar 1).
7. Source basis fenced: the source names no market beyond `_asset BTC` and no timeframe at all. The BTCUSDT-`1h` choice, same-bar-close fills, single-unit/no-add/noop pin, entry-then-close ordering pin, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-market deployment passes.
8. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-`1h` market choice, the same-bar-close fills, the position-state pin, the entry-then-close ordering pin, and house sizing/costs — all predeclared above; the 1-bar lookback, the floor-pivot formula, the S1 dip-bounce entry, the R1 target exit, the weak/strict/weak boundary mix, the long-only book, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown stance are source-verbatim. The ordering pin changes no single-leg event: bars firing exactly one leg reach the same fill under either order.
9. Cousin records fenced as different constructions (none computes classic floor `(H+L+C)/3` with `S1 = 2P−H` / `R1 = 2P−L` dip-bounce logic): the admitted Kaufman pivot-breakout sibling extracts swing pivots via `ta.pivothigh/low(3,3)` 7-bar确认 registers and enters on `high > lastHigh` / exits on `low < lastLow` two-sided (fractal-breakout school, no S1/R1 arithmetic); the admitted Camarilla sibling computes narrow bands `pC ± pR×(1.1/12)` with a sticky `close`-vs-band state machine two-sided (no dip-low test, no reclaim test, no `2P−H` formula); Donchian breaks raw multi-bar extremes with no pivot normalization; Keltner/SuperTrend/Chandelier trail average- or extreme-anchored volatility bands, never prior-bar floor pivots. Not a threshold re-tuning of any of them.
10. The 1 lookback literal, the floor-pivot formula, the `2.0` coefficients, the dip-plus-reclaim conjunction, the `R1` target, the weak/strict/weak boundaries, the single-unit long-only stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning lookback, re-anchoring on swings or Camarilla fractions, reducing the entry to a close-cross, adding a stop/target/filter/cooldown/gate, adding a short entry leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 1-bar floor pivot / S1 dip-bounce / R1 target / weak-strict-weak boundaries / single-unit long-only / entry-then-close ordering / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Support relevance: replacing the S1 dip-bounce entry with a plain prior-close reclaim entry (`close[t] > close[t-1]` with the same R1 exit) must not improve net expectancy; fail ⇒ the S1 geography adds nothing over a naive uptick.
- F2 — Target relevance: replacing the R1 target exit with a pivot-midline (`pivot`) recross exit must not improve net expectancy; fail ⇒ the full-range `R1` distance adds nothing over a plain mean give-back.
- F3 — Dip requirement: replacing the dip-plus-reclaim conjunction with a close-only test (`close[t] > S1`, ignoring `low[t]`) must not improve net expectancy; fail ⇒ the intrabar-dip confirmation adds nothing over a close-level rule.

## Crypto portability

Direct: single-venue BTCUSDT perpetual `1h` completed bars with standard OHLC fields. No session calendar (crypto trades continuously; the 1-bar pivot needs no session gap semantics), no corporate actions, no dividends, no funding/OI reads, no cross-venue state. 24/7 continuity means the anchor bar `t−1` is always the immediately prior print — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; the record's 4-decimal price echo is display precision only and changes no event. Leverage/margin follow the house overlay, not the source's bare `1.0` default.

## Limitations

- The source ships no fill-timing flag: same-bar-close fills are a disclosed researcher derivation, never a source claim. An engine filling at next-open would print different event prices on identical bars.
- The source ships no timeframe: the `1h` frame is a disclosed researcher choice. Other frames re-tune nothing in the rule text but produce different event streams; they are different, unpinned evaluations.
- The source ships no costs: all economics come from the house overlay. No realized-funding claim is made; modeled funding is never reported as canonical.
- The source ships no ordering: entry-then-close co-fire resolution is a predeclared researcher pin (Kaufman precedent), never a source claim; the Forven engine's own ordering may differ — this record is not evidence of source-engine behaviour.
- Zero-range priors collapse selectivity (Negative evidence 3); sideways bounces are held without guardrail (Negative evidence 4); confidence is skipped without event change (Negative evidence 5).
- Not independently reproduced; no live, Paper, Testnet, or profitability claim of any kind. Admission is engineering capability only.

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/pivot_point.py
- https://github.com/judder659/Forven
