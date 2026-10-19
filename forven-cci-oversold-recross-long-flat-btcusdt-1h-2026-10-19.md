---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven CCI 20 oversold-recross long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/cci.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven CCI 20 oversold-recross long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the thirty-three admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-cross`, `forven-chaikin-mf-threshold-cross`, `forven-elder-ray-bull-power-cross`, `forven-adx-trend-pulse-reclaim`, `forven-dema-cross`, `forven-trix-signal-cross`, `forven-ultimate-oscillator-cross-gated`, `forven-bollinger-s00120`, `forven-three-bar-reversal-decline-gated`, `forven-atr-breakout-channel`, `forven-pivot-s1-bounce-r1-exit`, `forven-volatility-contraction-breakout`, `forven-connors-rsi-oversold-recross`, `forven-kdj-dual-gate`, `forven-heikin-ashi-color-change`, `forven-bb-edge-fade-reclaim`, `forven-rsi-s00139-washout-cross`, `forven-obv-ema-cross-sma-gated`, `forven-mfi-threshold-cross`, `forven-williams-r-adx-gated`, `forven-rsi-boundary-rejection`, `forven-ema-cross-adx-regime`, `forven-vwap-pullback-distance`, and `forven-hma-cross` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` against both `HEAD` and `refs/heads/main` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/cci.py`.
- File history: the file last changed in the repository's initial public release (`d1bfff6341dbbdee4fcb7817c611b77ef91952aa`, `2026-06-21T22:24:09Z`, verified via the commits API for this path this cycle) and is byte-identical at the pinned HEAD — no later edit touches any rule.
- GitHub blob SHA at the pinned commit: `5a11554174917cb071687049e112c167719f06fc`, size 3186 bytes.
- Byte-identity check: the file retrieved from `raw.githubusercontent.com` at the pinned commit is 3186 bytes, 116 lines, SHA-256 `609492abb1092e084586693a2cda7951bd706ff0b076d6eaafd205b0ad7b808b`, and `git hash-object` reproduces the GitHub blob (`5a11554…bf881`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = CCIStrategy` (line 112), `TYPE_NAME = "cci"` (line 13), and the `STRATEGIES = [("PREBUILT-CCI", CCIStrategy, {"_asset": "BTC"})]` roster pin (lines 114–116). Repo-wide, no other builtin file carries this `TYPE_NAME`; working-tree search for `builtin/cci.py` / `PREBUILT-CCI` / `CCIStrategy` returns zero strategy records citing this source file.
- The file's own words (quoted for gate evidence, never extended): module docstring `CCI (Commodity Channel Index) strategy.` with `Entry: CCI crosses above -100 from below (oversold bounce)` / `Exit: CCI crosses below +100 from above` (lines 1–6); class docstring `CCI = (Typical Price - SMA(TP)) / (0.015 * Mean Deviation)` with `Entry when CCI crosses above oversold from below; exit when CCI crosses below overbought from above.` (lines 17–22); `describe()` returns `Enters when CCI(20) crosses above -100 (oversold bounce). Exits when CCI crosses below 100.` (lines 49–54); `default_params` returns exactly `{ "cci_period": 20, "oversold": -100, "overbought": 100, "leverage": 1.0 }` (lines 37–43); `compatible_regimes` returns `{"RANGE_BOUND", "TREND_UP"}` (lines 46–47, metadata never read by the signal path); `parameter_space()` returns `{ "cci_period": (10, 30, 5), "oversold": (-150, -50, 25), "overbought": (50, 150, 25) }` (lines 104–109, a documented search surface only — this record pins the defaults and runs no search). No performance phrase of any kind ships anywhere in the 116 lines — this record adopts no source-reported performance (see Evidence).
- Single decision path, verified complete: `generate_signal()` (lines 56–102) is the sole signal method — no `generate_signals` vectorized twin exists anywhere in the 116 lines (zero matches), so no twin-selection ambiguity exists. The CCI arithmetic is in-file (typical price line 71, SMA line 72, mean deviation lines 73–75, oscillator line 76 — no out-of-file average conditions any order); the method reads `close`/`high`/`low` (lines 59, 71), applies its own short-frame guard (lines 61–69), evaluates the threshold-recross pair (lines 85–86), and returns a single `Signal` (lines 92–102).
- Base-class semantics pinned at the same commit (byte-verified): `forven/strategies/base.py` (12238 bytes, blob `27508a2…abf881`, size re-verified via the contents API this cycle — identical to the prior-cycle full read) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults, `direction: str = "long"` default, plus `__post_init__` coercion; `_normalize_signal_direction` maps the `"long"` literal back to `"long"` on entry and non-entry bars alike — both `direction="long"` literals in this file (guard line 66, live line 96) therefore survive untouched on every bar.
- Full-file token census (verified by search over the 116 lines this cycle): `direction=` occurs exactly twice (both `"long"` — guard line 66 and live line 96; no short leg exists); 0 `sell` / 0 `stop` / 0 `limit` / 0 `profit` / 0 `qty` / 0 `trail` (no order arguments, no live risk legs of any kind); 0 `fee` / 0 `funding` / 0 `mark_price` (no economics beyond the `leverage: 1.0` default, replaced by the house overlay — see Execution assumptions); 0 `request` / 0 `security` / 0 `timeframe` / 0 `barstate`, and 0 `open`-series reads plus 0 `volume` reads anywhere (order-gating reads are `high`/`low`/`close` only — typical price needs no `open`, no participation print); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` / 0 `cooldown` (no position-aware state conditions any signal); 0 `short` (case-insensitive — no short path exists); `len(df)` occurs exactly once (the line-61 guard — the file's own warmup floor, adopted verbatim, never invented).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the typical-price CCI(20) construction, the −100 recross-up entry, the +100 recross-down exit, the long-only stance, the no-stop posture, and its own `period + 2` short-frame guard — but ships no venue spelling, no timeframe, no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the thirty-three admitted Forven records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit position pin with hold-no-op semantics with the source's own 22-bar guard adopted verbatim as the warmup floor (an already-positioned book treats same-direction recross-up bars as hold-no-ops, a flat book treats recross-down bars as no-ops, re-entry re-arms on any qualifying recross-up after any exit with no cooldown, pre-guard bars flat by the source's own rule — see Signal); (4) house sizing/capital/costs replacing the bare `leverage: 1.0` default (see Execution assumptions; sizing changes no event under the predeclared single-unit rule). No tie-break pin is needed: entry and exit are provably mutually exclusive on every bar (see Signal).

Pre-write dedup (2026-10-19): working-tree filename/content search for `builtin/cci.py` / `PREBUILT-CCI` / `CCIStrategy` returns zero strategy records — no record cites this source file. No open or closed `research/*` PR ever carried this source file (closed-PR title/branch search for `cci` over the 100 most recent closed PRs returns zero). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. The pool's two CCI cousins are fenced as different constructions in Negative evidence 6 (FMZ triple-gate CCI+RSI-cross+EMA-filter with trailing stop; Eterna close-only CCI with ±200 extreme-reversal legs, two-sided, `4h` — neither trades a bare typical-price CCI(20) ±100 recross pair, long-flat, from this file). Not a duplicate, paraphrase, or trivial parameter variant: a bare single-oscillator threshold-recross pair on typical-price CCI (no gate, no filter, no extreme legs, no stop), long-flat, from immutable file `builtin/cci.py`, is a different signal construction from a triple-gated system or a two-sided extreme-reversal system — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: a `CCI (Commodity Channel Index) strategy` that `Enters when CCI(20) crosses above -100 (oversold bounce). Exits when CCI crosses below 100.` No behavioural, structural, or risk-premium channel is claimed anywhere in the 116 lines. The file ships no backtest numbers of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Oversold-bounce mean reversion on a mean-deviation oscillator, long-only, state-holding. CCI measures the typical price's distance from its 20-bar mean in units of mean absolute deviation, so the −100 recross-up buys the exact bar exhaustion releases (not the deep-oversold bar itself — the oscillator must first print at or under −100 and then print back above it), and the +100 recross-down surrenders the unit on the exact bar overbought pressure releases. There is no gate, no filter, and no holding leg: a market that whipsaws across −100 prints repeated full round-trips with no flat state to rest in (whipsaw profile, disclosed), while a leg whose reverse cross never prints is held indefinitely. Unlike stop-based systems there is no fixed-distance risk leg — the overbought recross is the sole risk control by construction. Unlike the pool's FMZ CCI sibling (CCI ±50 gate over an RSI cross under an EMA filter with a trailing ratchet), this system fires on two bare threshold comparisons with no confirmation and no guardrail — strictly earlier and more frequent on identical bars, not a re-parameterization of the same rule. Unlike the pool's Eterna CCI sibling (close-only CCI with ±200 extreme-reversal legs, two-sided), this system reads typical price, carries no extreme legs, and never shorts — strictly different inputs, legs, and direction handling on identical bars.

## Signal

Exact rule as pinned (any other period, input series, threshold, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own; lines 71–76 are in-file and `generate_signal` (lines 56–102) is the single source of truth — no second decision logic exists:

```text
TP[t]             = (high[t] + low[t] + close[t]) / 3.0          // typical price, causal
SMA[t]            = mean(TP[t-19..t])                            // 20-bar rolling mean
MD[t]             = mean(|TP[t-19..t] − SMA[t]|)                 // 20-bar mean absolute deviation
CCI[t]            = (TP[t] − SMA[t]) / (0.015 · MD[t])
guard             = len(df) < 22 → both signals false (source's own floor)
long_entry        = CCI[t-1] <= -100 and CCI[t] > -100           // strict recross-up edge
long_exit         = CCI[t-1] >= +100 and CCI[t] < +100           // strict recross-down edge
```

- Trade events: `entry_signal=True` with `direction="long"` on recross-up bars (lines 85, 93); otherwise `entry_signal=False` with `exit_signal=bool(recross-down)` (lines 86, 94). Entry and exit legs are provably mutually exclusive (Negative evidence 3), so no bar ever fires both legs and no ordering assumption exists to verify.
- Exact boundaries (pinned semantics): entry needs a strict current-bar inequality (`CCI[t] > -100` — a bar closing with `CCI == -100` to the tick fires neither leg and holds by code); the prior-bar branch admits equality (`<=` / `>=`), so a flat-tied prior bar still admits a genuine current-bar break. Equality on the current bar is a hold, never an entry or an exit. `confidence` (lines 88–90) and the `indicators={cci, prev_cci}` echo (lines 98–101) are diagnostic constants per bar — neither conditions any predicate.
- Direction: long-only with an explicit pre-guard flat state (lines 61–69 return both-false). The file's `direction="long"` literals survive the base-class normalizer untouched on every bar (verified in `base.py`); a two-sided reading would contradict the shipped rule, and no short path exists. The long leg is spot-compatible; no margin short is ever required.
- Exits and risk (explicit): the overbought recross is the sole position-ending path. Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence` and the indicators echo are diagnostic — neither conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further recross-up bars as hold-no-ops (no pyramiding, no averaging); a flat book treats recross-down bars as no-ops; re-entry re-arms on any qualifying recross-up after any exit (no cooldown specified — explicitly none, not invented). Pre-guard bars are flat by the source's own rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close` for every order-gating comparison, with fixed non-negative offsets (trailing 20-bar folds plus a one-bar recross lookback — no shifts, no negative indices); no `open`-series read, no `volume` read, no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). All windows are trailing and deterministic given the pinned pandas/numpy semantics. The `compatible_regimes` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule. The `parameter_space` range is optimizer metadata, never read by any predicate.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` only (typical price, both rolling folds, the recross read, and the `price` echo). No `open`-series read, no bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; every window reads the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close (`price=round(curr_close, 4)`, pinned derived rule).
- Warmup: the source ships its own guard — `period + 2 = 22` completed bars, shorter frames returning both-signals-false — adopted verbatim as the warmup floor, flat by record rule (predeclared: the deepest live window is the 20-bar rolling fold plus the one-bar recross lookback, i.e. 21 bars of data, so the 22-bar guard covers seeding with a one-bar margin; no researcher length is invented). No repainting, no negative shift, no future bars/extrema, no full-sample normalization. Rolling-apply seeding resolves inside the guard: no evaluated bar reads an unseeded window.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice of the `PREBUILT-CCI` roster leg — the source roster pins `_asset BTC` for this leg; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the thirty-three admitted Forven records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders, and no bar ever co-fires both legs (see Signal), so no ordering assumption exists to verify.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 1.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one long position at any time; same-direction recross-up bars hold without adds; recross-down bars on a flat book are no-ops; any open long ends on the first recross-down bar. Re-entry after an exit needs only the next qualifying recross-up (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (116 lines: module docstring with the cross rule, `TYPE_NAME`, in-file typical-price/SMA/mean-deviation arithmetic, `default_params` with the 20/−100/+100 set, the recross-up entry, the recross-down exit, the fixed long-only stance with the literal `"long"` direction tokens, its own 22-bar short-frame guard, the `round(curr_close, 4)` price echo, the `PREBUILT-CCI` roster pin, plus the total absence of any risk leg). It ships no performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Guard adopted verbatim, not repaired: the file's own `len(df) < period + 2 = 22` check returns both-signals-false on shorter frames — pre-guard bars are flat by the source's own rule, and the 20-bar rolling folds seed inside the guard with a one-bar margin. An engine evaluating from bar 0 without the guard would print NaN-comparison bars (all false) and then start firing recross events from barely-seeded folds — disclosed, never load-bearing past the guard.
2. Zero-dispersion fence: when all 20 typical prices in the fold are tick-identical, `MD[t] = 0` — but then `TP[t] == SMA[t]` too, so the oscillator prints `0/0 = NaN`, and every strict NaN comparison is false, firing neither leg. No division-by-nonzero-dispersion path can print an infinite CCI from real bars (a nonzero numerator with a zero denominator is arithmetically impossible here since a zero deviation forces every fold value onto the mean). Deterministic on every bar, disclosed.
3. Co-fire impossibility proven: entry needs `CCI[t] > -100` while exit needs `CCI[t] < +100`, and jointly needs `CCI[t-1] <= -100` with `CCI[t-1] >= +100` — the prior-bar pair is jointly unsatisfiable on any real print, and on NaN prints every strict comparison is false, so a NaN leg fires neither side. No tiebreak is needed and none is missing.
4. Exact-touch rules fenced: `CCI[t] == -100` (resp. `+100`) to the tick fires neither leg regardless of history (hold by code); prior-bar equality (`<=` / `>=`) still admits a genuine current-bar break. Strictness is preserved throughout — disclosed, not smoothed.
5. Regime metadata fenced: `compatible_regimes == {"RANGE_BOUND", "TREND_UP"}` is defined once and never called by the decision path (which takes only `df`/`params`); treating the label as an entry gate would be a different, unpinned rule.
6. Cousin records fenced as different constructions (none trades a bare typical-price CCI(20) ±100 recross pair, long-flat, on `1h` BTC bars from this file): the admitted `forven-rsi-s00139-washout-cross` sibling is the closest structural cousin (oversold-washout recross entry, overbought-recross exit, long-flat, same lane) but trades Wilder's RSI, not CCI — different oscillator, different inputs, different file; the admitted `cci-ema-rsi-cross-trailing-stop` record trades an FMZ 362029 triple-gate system (CCI ±50 gate over a fast/slow RSI cross under a slow-EMA price filter, with a ratcheting close-evaluated trailing stop, `1h`) — gated versus bare, stop versus no-stop, different source; the admitted `cci-threshold-extreme-reversal-two-sided` record trades an Eterna close-only CCI(20) with ±100 crosses *plus* ±200 extreme-reversal legs, two-sided with opposite-signal entries, on `4h` — close-input versus typical-price input, extreme legs versus none, two-sided versus long-flat, different frame, different source. The pool's `williams-r-level-cross-mean-reversion` (highest/lowest-range oscillator, fixed-RR exits) and `mfi-threshold-cross` (volume-weighted) read different statistics entirely. Not a re-tuning of any of them: swapping the oscillator, the input series, the direction handling, or adding extreme legs/a stop would each be a different, unpinned rule — none is admitted here.
7. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-`1h` market choice, the same-bar-close fills, the single-unit/hold-no-op position pin, and house sizing/costs — all predeclared above; the in-file typical-price/CCI arithmetic, the 20/−100/+100 set, the strict recross boundaries, the recross-down exit, the long-only stance, the no-stop/no-target/no-trailing/no-time-exit/no-cooldown stance, and the 22-bar guard floor are source-verbatim effective behaviour. The position pin changes no single-leg event: bars firing exactly one leg reach the same fill under either bookkeeping.
8. The 20/−100/+100 set, the typical-price construction, the strict recross boundaries, the recross-down exit, the single-unit long-only stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: re-tuning the period, converting the recross edge to a level, gating with a regime/volume/RSI filter, adding extreme-reversal legs, adding a stop/target/cooldown, enabling a short leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: typical-price CCI(20) ±100 strict recross pair / recross-down exit / single-unit long-only / `1h` BTCUSDT / same-bar-close fills / 22-bar guard floor are frozen.

- F1 — Oscillator relevance: replacing the CCI legs with a same-period SMA20 close-vs-average cross (SMA20 recross-up entry, recross-down exit, same guard/pins) must not improve net expectancy; fail ⇒ the mean-deviation construction adds nothing over a plain average cross.
- F2 — Exit relevance: replacing the +100 recross-down exit with a fixed 8-bar time exit (same recross entries, same guard/pins) must not improve net expectancy; fail ⇒ the overbought-release exit adds nothing over a clock exit.
- F3 — Input relevance: replacing typical-price CCI with close-only CCI(20) at the same ±100 thresholds (Eterna-style input, same guard/pins) must not improve net expectancy; fail ⇒ the high/low typical-price input adds nothing over close alone.

## Crypto portability

Direct for the long leg, no margin short ever required: single-venue BTCUSDT perpetual `1h` completed bars with standard high/low/close prints (the rule reads `high`/`low`/`close` for every order-gating comparison — no `open`, no `volume`, no funding/OI reads in any order leg). No session calendar (crypto trades continuously; the trailing 20-bar folds need no session-gap semantics), no corporate actions, no dividends, no cross-venue state. 24/7 continuity means the rolling windows are always the immediately prior prints — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; the record's 4-decimal price echo is display precision only and changes no event. Leverage/margin follow the house overlay, not the source's bare `1.0` default; the long-only stance is spot-compatible, and no deployment here needs a short venue.

## Limitations

- The source ships no timeframe: the `1h` frame is a disclosed researcher choice. Other frames re-tune nothing in the rule text but produce different event streams; they are different, unpinned evaluations.
- The source ships no fill-timing flag: same-bar-close fills are a disclosed researcher derivation, never a source claim. An engine filling at next-open would print different event prices on identical bars.
- The source ships no position semantics: single-unit/hold-no-op bookkeeping is a predeclared researcher pin, never a source claim; the Forven engine's own ordering may differ — this record is not evidence of source-engine behaviour. The 22-bar guard floor is source-verbatim, not a researcher pin.
- The source ships no costs: all economics come from the house overlay; the Forven engine's own fills may differ — this record is not evidence of source-engine economics.
- The `parameter_space` optimizer range names the period/threshold search surface — disclosed; the rule reads only the `cci_period=20` / `oversold=-100` / `overbought=100` defaults and exercises no search; unread regime metadata (Negative evidence 5).
- Not independently reproduced; no live, Paper, Testnet, or profitability claim of any kind. Admission is engineering capability only.

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/cci.py
- https://github.com/judder659/Forven
