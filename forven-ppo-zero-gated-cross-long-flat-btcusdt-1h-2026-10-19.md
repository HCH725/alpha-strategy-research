---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven PPO 12/26/9 zero-gated signal cross long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/ppo.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven PPO 12/26/9 zero-gated signal cross long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-ema-cross-adx-regime`, `forven-dema-cross`, `forven-tema-cross`, `forven-hma-cross`, `forven-macd-cross-adx-regime`, `forven-donchian-regime-breakout`, `forven-keltner-adx-gated-breakout`, `forven-parabolic-sar-cross`, `forven-rsi-boundary-rejection`, and thirty-seven further Forven-sibling records on `main`).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`, verified via the GitHub commits API this cycle; verified as the repository HEAD via `git ls-remote` against both `HEAD` and `refs/heads/main` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/ppo.py`.
- GitHub blob SHA at the pinned commit: `5f9a46c9917b8a985964d3d4b424b0396ae7a340`, size 3346 bytes.
- Byte-identity check: the file retrieved from `raw.githubusercontent.com` at the pinned commit is 3346 bytes, 119 lines, SHA-256 `27fd8e4cf8dac731c3c4e19ddc7e58f323d5d861bbbe28c516d6fd4c46137f43` (dual-fetch byte-identical this cycle), and `git hash-object` reproduces the GitHub blob (`5f9a46c9…ae7a340`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = PPOStrategy` (line 115), `TYPE_NAME = "ppo"` (line 12), and the single-leg `STRATEGIES = [("PREBUILT-PPO", PPOStrategy, {"_asset": "BTC"})]` roster pin (lines 117–119). No pool record cites this source file (see pre-write dedup below).
- The file's own words (quoted for gate evidence, never extended): module docstring `PPO (Percentage Price Oscillator) strategy.` with `Entry: PPO crosses above signal line AND PPO > 0` / `Exit: PPO crosses below signal line` / `Compatible Regimes: TREND_UP, TREND_DOWN` (lines 1–6); class docstring pins the arithmetic `PPO = (EMA_fast - EMA_slow) / EMA_slow * 100` and `Signal = EMA(PPO, signal_period)` with `Entry when PPO crosses above signal and PPO > 0; exit when PPO crosses below signal.` (lines 15–22); `describe()` returns `Enters when PPO(12/26) crosses above its 9-bar signal line while PPO > 0. Exits when PPO crosses below signal.` at defaults (lines 49–55); `default_params` returns exactly `{ "fast": 12, "slow": 26, "signal": 9, "leverage": 1.0 }` (lines 38–44); `compatible_regimes` returns `{"TREND_UP", "TREND_DOWN"}` (lines 46–47, metadata never read by the signal path — `generate_signal` takes only `df` and reads only `self.params`); `parameter_space()` returns `{ "fast": (8, 16, 2), "slow": (20, 30, 2), "signal": (5, 12, 1) }` (lines 108–113, a documented search surface only — this record pins the defaults and runs no search). No performance phrase of any kind ships anywhere in the 119 lines — this record adopts no source-reported performance (see Evidence).
- In-source length guard (unlike the guard-free MACD/EMA-cross siblings): `if len(df) < slow + p["signal"] + 2` (line 63, i.e. 26 + 9 + 2 = 37 bars) returns a flat `Signal(entry False, exit False, direction "long", confidence 0.0, indicators {})` (lines 63–71). The guard is source-verbatim behaviour, fenced inside the researcher warmup (see Signal).
- Single decision path: the file ships only the scalar `generate_signal()` (lines 57–106) — there is no vectorized `generate_signals` twin (zero hits), so no twin-consistency question exists at all.
- Base-class semantics pinned at the same commit (same-pin lineage as the admitted siblings): `forven/strategies/base.py` (blob `27508a2a6b8c546e21adefdb97fc0144fabf881b`, 12238 bytes, verified via the contents API this cycle) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults, `direction: str = "long"` default, plus `__post_init__` coercion; the file's two `direction="long"` literals (guard return line 68, main return line 98) therefore survive untouched on every bar.
- Full-file token census (verified by search over the 119 lines this cycle): `direction=` occurs exactly twice (both `"long"` — guard and main returns; no short leg exists); 0 `short` anywhere; 0 `sell` / 0 `crossover` (no display prose, no order-gating synonyms); 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` / 0 `trail` (no order arguments, no live risk legs of any kind); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default, replaced by the house overlay — see Execution assumptions); 0 `volume` / 0 `funding` / 0 `mark_price` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any line, and 0 `open`-series reads anywhere (the rule reads `close` only — the single `df["close"]` at line 59; not even `high`/`low` enter this file); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` / 0 `cooldown` (no position-aware state conditions any signal); 0 `rsi` / 0 `stoch` / 0 `vwap` / 0 `supertrend` / 0 `ichimoku` / 0 `rolling(` (no foreign indicator, no lookback helper of its own); 0 `atr` / 0 `adx` (no auxiliary chain at all — the closest file in the family to a pure close-only oscillator); `len(df)` exactly once (the source guard itself); the 9 `return` hits are Python return statements (six property/method returns plus the two `Signal` returns plus `parameter_space`).
- Param fence: the predicate reads only keys present in `default_params` (`fast`, `slow`, `signal`) — treating any other key as live would be a different, unpinned rule, and no optimizer range is exercised by this record.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the PREBUILT-PPO BTC roster leg, the 12/26/9 construction, the PPO-greater-than-zero entry conjunction, the unconditional cross-below exit, the 37-bar source guard, and the long-only stance — but ships no venue spelling, no timeframe, no fill-timing flag, no position-sizing rule, and no entry/exit evaluation ordering beyond its own conjunction. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted macd-cross, ema-cross-adx-regime, tema-cross, dema-cross, hma-cross, and sibling records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 60-bar researcher warmup pin (the file carries no position reference; the 60-bar pin covers the 37-bar source guard plus the span-26/span-9 ewm seeding margin, following the admitted pool PPO record's own 60-bar pin — an already-positioned book treats same-side entry bars as hold-no-ops, a flat book treats cross-below exit bars as no-ops, re-entry re-arms on the next qualifying zero-gated cross with no cooldown, pre-first-signal and warmup bars flat by pin); (4) the house cost/capital overlay replaces the file's bare `leverage: 1.0` default (the file declares no fee, funding, or margin treatment at all — house assumptions are modeled costs, and modeled funding is never reported as realized). The 12/26/9 periods, the `* 100 / slow` normalization, the zero-gate conjunction, the unconditional cross-below exit, the long-only stance, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown stance are source-verbatim effective behaviour.

Pre-write dedup (2026-10-19): working-tree filename/content search for `builtin/ppo` / `PPOStrategy` / `PREBUILT-PPO` returns zero strategy records citing this source file (the `S030` hits in the MACD sibling are that file's own roster tag, and the remaining `S0304` hits are Grinblatt-paper DOI substrings inside unrelated records, verified forven-free). The pool's PPO cousin is fenced as a different construction in Negative evidence 8 (StockCharts-docs-sourced naked 12/26/9 two-sided always-in reversal on `1d` BTC bars — every below-zero cross this record vetoes trades there, and every exit here reverses to short there). No closed `research/*` PR ever carried this source file (merged Scout PRs through #315 are WorldQuant/PVI/Mayer/PGO plus forty-four Forven files through MACD cross #315, none of them PPO). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), #251 (Swift 2-year MA multiplier zone-state long-flat), and #304 (Forven CCI oversold-recross long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: percentage-normalized gap rotation (ratio of double-EMA structure) plus a zero-level entry veto is a different normalized signal with strictly different entry events from any absolute-gap cross, not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: percentage-normalized momentum rotation that buys when the 12/26/9 PPO crosses above its signal line while PPO reads above zero (normalized strength agreement), and exits the long when PPO crosses back below its signal line. No behavioural, structural, or risk-premium channel is claimed anywhere in the 119 lines. The file ships no backtest numbers of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Zero-vetoed normalized rotation machine, long-only, single conjunctive gate. Unlike the pool's naked-cross PPO record (StockCharts 12/26/9: every rotation enters, including rotations printed below the zero line where the normalized gap says the slow leg still dominates, and every death cross reverses to short), this system fires on the identical 12/26/9 arithmetic but spends one veto before every entry: the `PPO > 0` leg vetoes crosses fired while the fast leg still trails the slow leg in percentage terms — and it never shorts, so vetoed or reversed bars leave the book flat instead of reversed. Unlike the admitted `forven-macd-cross-adx-regime` sibling (absolute-gap rotation with ADX-plus-EMA200 gates), the trigger here divides the EMA gap by the slow leg first, so identical momentum shapes print identical crosses at any price level — level-dependence is divided out before the cross is even evaluated — and the only gate is the zero line itself, not an external trend or strength filter. Unlike price-average cross cousins (EMA 20/50, DEMA, TEMA, HMA), entries fire on second-order rotation of a derived ratio series — strictly later and smoother than first-order price crosses, at the cost of deeper lag into V-turns. Unlike stop-carrying records, the sole risk control is the ungated cross-below exit — a position opened under normalized-strength agreement is still cut the first bar the oscillator lines re-cross, with no stop, no target, and no zero-loss early exit.

## Signal

Exact rule as pinned (any other average variant, period, threshold, gate, exit leg, fill, frame, book, or ordering is a different, unpinned rule). All identifiers below are the program's own; `generate_signal` (lines 57–106) is the single source of truth and no twin exists:

```text
ema_fast[t]   = close.ewm(span=12, adjust=False).mean()
ema_slow[t]   = close.ewm(span=26, adjust=False).mean()
ppo[t]        = (ema_fast[t] - ema_slow[t]) / ema_slow[t] * 100.0
ppo_sig[t]    = ppo.ewm(span=9, adjust=False).mean()
cross_up      = prev_ppo <= prev_ppo_sig AND curr_ppo > curr_ppo_sig
cross_down    = prev_ppo >= prev_ppo_sig AND curr_ppo < curr_ppo_sig
zero_ok       = curr_ppo > 0
long_entry    = cross_up AND zero_ok
long_exit     = cross_down                            // unconditional, ungated
guard         = source len(df) < 26 + 9 + 2 = 37 bars flat (fenced inside researcher 60-bar pin)
```

- Trade events: `entry_signal=True` with `direction="long"` on zero-gated cross-up bars (line 98); otherwise `entry_signal=False` with `exit_signal=bool(cross_down)` (lines 95–97). Entry and exit legs are provably mutually exclusive (Negative evidence 6), so no bar ever fires both legs and no ordering assumption exists to verify.
- Exact boundaries (pinned semantics): cross legs admit previous-bar equality (`<=` / `>=`) but demand strict current-bar separation (`>` / `<`) — oscillator lines printing exactly equal fire neither leg. `zero_ok` is strict (`>` — `ppo == 0.0` admits no entry and, the exit being cross-only, holds any open side by code). A bar with both oscillator lines exactly equal fires neither entry nor exit regardless of the zero print.
- Direction: long-only with an explicit pre-first-signal flat state plus the warmup flat. Both `direction="long"` literals survive the base-class normalizer untouched on every bar (verified in `base.py`); a two-sided reading would contradict the shipped rule, and no short-equivalent path exists. The long leg is spot-compatible; no margin short is ever required.
- Exits and risk (explicit): the ungated cross-below is the sole position-ending path. Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence` (`min(1.0, abs(curr_ppo - curr_sig) / 1.0)` on gated entries, `0.0` elsewhere, lines 90–93) and the full `indicators` echo (`ppo`, `ppo_signal`, `ppo_hist`) are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; a positioned book treats same-side entry bars as hold-no-ops (no pyramiding, no averaging); a flat book treats cross-below exit bars as no-ops; re-entry re-arms on any qualifying zero-gated cross after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and warmup bars are flat by pin. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (EMA seeds, PPO arithmetic, signal smoothing, both cross legs, zero comparison) — no `open`-series read, no `high`/`low` read, no bar `volume`, no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). All windows (ewm seeds, one-bar shifts, cross lookback) are trailing and deterministic given the pinned pandas semantics; ewm series carry no `min_periods`, so every value from bar 0 is seed-defined rather than NaN-gated — the 60-bar researcher warmup exists precisely to fence that seeding alongside the 37-bar source guard (Negative evidence 1). The `compatible_regimes` set is metadata never read by the signal path (which takes only `df`); treating the label as a gate would be a different, unpinned rule. The `parameter_space` ranges are optimizer metadata, never read by any predicate.

## Required data

- Completed `1h` bars of BTCUSDT: `close` only (both EMAs, the PPO ratio, the signal smoothing, both cross legs, the zero comparison). No bar `open`, no `high`/`low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` anywhere; 0 `timeframe` tokens in the whole file). This is the family's purest close-only record.
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; all seeds, shifts, and the two-bar cross read the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close (`price=round(curr_close, 4)`, pinned derived rule).
- Warmup: the source ships its own 37-bar length guard (`slow + signal + 2`), and this record predeclares a 60-bar researcher warmup pin that covers the guard plus the span-26/span-9 ewm seeding margin (following the admitted pool PPO record's own 60-bar pin for the same 12/26/9 arithmetic). The pin covers the EMA26 seed, the signal-smoothing seed, and the two-bar cross lookback; the first 60 completed bars are flat by pin. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice of the `PREBUILT-PPO` roster leg — the source roster pins `_asset BTC` for this leg; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders, and no bar ever co-fires both legs (see Signal), so no ordering assumption exists to verify.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 1.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one long position at any time; same-side entry bars hold without adds; cross-below bars on a flat book are no-ops; any open long ends on the first cross-below bar regardless of the zero print. Re-entry after an exit needs only the next qualifying zero-gated cross (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (119 lines: module docstring with the entry/exit/regime triple, `TYPE_NAME`, `default_params` with the 12/26/9 set, the PPO-ratio/signal arithmetic, the zero-gated conjunction, the unconditional cross-below exit, the 37-bar source guard, the two `direction="long"` literals and the `round(curr_close, 4)` price echo, the single scalar decision path, the `PREBUILT-PPO` roster pin, plus the total absence of any risk leg). It ships no performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Seeding fenced with a pin, not a repair: every series the file touches is ewm-seeded from bar 0 (`adjust=False`, no `min_periods`) — so values on the earliest bars are seed-dominated even past the 37-bar source guard. The 60-bar researcher warmup (source guard plus seeding margin, per the admitted pool PPO precedent) fences exactly that: pre-warmup bars are flat by pin, post-warmup events are seed-stable. An engine evaluating from bar 0 without the pin reaches different early events — disclosed, never load-bearing past warmup.
2. Normalization fenced: the `* 100.0 / ema_slow` ratio divides the EMA gap by the slow leg before any comparison — cross timing is price-level-free by construction, unlike the admitted MACD sibling's absolute gap. Disclosed as the shipped arithmetic, not converted to an absolute difference.
3. Diagnostic-only values fenced: `confidence` (`min(1.0, abs(curr_ppo - curr_sig) / 1.0)`), the full `indicators` echo (`ppo`, `ppo_signal`, `ppo_hist`), and the histogram itself condition no predicate — deleting all three reaches identical events on every bar.
4. Regime metadata fenced: `compatible_regimes == {"TREND_UP", "TREND_DOWN"}` is defined once and never called by the decision path (which takes only `df`); treating the label as an entry gate would be a different, unpinned rule.
5. Single-path simplicity fenced: unlike the MACD sibling's scalar/vectorized twins, this file ships one decision path only (zero `generate_signals` hits) — no twin-selection ambiguity exists here by construction, disclosed, not repaired.
6. Co-fire impossibility proven: `cross_up` needs current PPO strictly above current signal while `cross_down` needs it strictly below — both jointly true is impossible; both-lines-equal fires neither. The zero gate only narrows entries further. No tiebreak is needed and none is missing.
7. Exact-touch rules fenced: previous-bar equality admits a cross leg (`<=` / `>=`), current-bar equality kills both legs; `ppo == 0.0` admits no entry and triggers no exit (hold by code). Strictness is preserved throughout — disclosed, not smoothed.
8. Cousin records fenced as different constructions (none trades a 12/26/9 percentage-normalized gap/signal cross conjunction-gated by PPO > 0 with an unconditional cross-below exit, long-only, on `1h` BTC bars from this file): the admitted `ppo-signal-cross-reversal` record pins StockCharts/WealthCharts documentation — a naked 12/26/9 rotation with zero confirmation legs, two-sided always-in-market reversal on `1d` BTC bars (every below-zero cross this record vetoes trades there, and every exit here reverses to short there); the admitted `macd-signal-cross-reversal` record crosses the absolute difference `12-EMA minus 26-EMA` against its signal (no division — its cross timing shifts with the price level); the admitted `forven-macd-cross-adx-regime` sibling shares only the cross idiom over an absolute gap with ADX-plus-EMA200 gates (different signal series, different gate family, different market); the admitted `pvo-signal-cross-volume-momentum` record crosses two volume-derived lines (reads no close at all); the admitted `kst-signal-cross-trend`, `pmo-signal-cross-reversal`, `tsi-signal-cross-reversal`, `trix-dual-band-trend`, and `coppock-curve-zero-state` records trade ROC composites, custom-smoothed momentum, double-smoothed fractions, triple-smoothed bands, and ROC-sum states — never a `100 x (EMA12 - EMA26) / EMA26` ratio with a 9-EMA signal cross. Not a re-tuning of any of them: swapping the normalization, any period, the zero threshold, the strictness, the exit, or the direction handling would each be a different, unpinned rule — none is admitted here.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-`1h` market choice, the same-bar-close fills, the position-state plus 60-bar warmup pins, and house sizing/costs — all predeclared above; the 12/26/9 set, the ratio normalization, the strict cross/zero boundaries, the 37-bar source guard, the unconditional cross-below exit, the long-only stance, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown stance are source-verbatim effective behaviour. The position pin changes no single-leg event: bars firing exactly one leg reach the same fill under either bookkeeping.
10. The 12/26/9 periods, the ratio normalization, the zero-gate conjunction, the unconditional exit, the single-unit long-only stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: re-tuning any period or threshold, converting the zero conjunction to a disjunction, gating the exit, adding a stop/target/filter/cooldown, enabling a short leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 12/26/9 / strict boundaries / zero-gated entry / unconditional cross-below exit / single-unit long-only / `1h` BTCUSDT / same-bar-close fills / 60-bar warmup are frozen.

- F1 — Zero-gate relevance: dropping the `PPO > 0` leg (naked signal-line cross, exit unchanged) must not improve net expectancy; fail ⇒ the zero veto adds nothing over the naked rotation machine.
- F2 — Exit relevance: replacing the cross-below exit with a zero-loss exit (close the long the first bar PPO prints below 0, same gated entries, same guard/pins) must not improve net expectancy; fail ⇒ the signal-recross exit adds nothing over a zero-loss exit.
- F3 — Signal-line relevance: replacing the signal-line cross trigger with a pure zero-line cross trigger (enter when PPO crosses above 0, exit when PPO crosses below 0, same guard/pins) must not improve net expectancy; fail ⇒ the 9-EMA signal line adds nothing over the zero line alone.

## Crypto portability

Direct for the long leg, no margin short ever required: single-venue BTCUSDT perpetual `1h` completed bars with standard close prints (the rule reads `close` alone — no `open`, no `high`/`low`, no `volume` dependency at all). No session calendar (crypto trades continuously; the two-bar cross needs no session-gap semantics), no corporate actions, no dividends, no funding/OI reads, no cross-venue state. 24/7 continuity means every shift-1 reference is always the immediately prior print — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; the record's 4-decimal price echo is display precision only and changes no event. Leverage/margin follow the house overlay, not the source's bare `1.0` default; the long-only stance is spot-compatible, and no deployment here needs a short venue.

## Limitations

- The source ships no timeframe: the `1h` frame is a disclosed researcher choice. Other frames re-tune nothing in the rule text but produce different event streams; they are different, unpinned evaluations.
- The source ships no fill-timing flag: same-bar-close fills are a disclosed researcher derivation, never a source claim. An engine filling at next-open would print different event prices on identical bars.
- The source ships a 37-bar guard but no seeding margin: the 60-bar warmup is a disclosed researcher pin. Pre-warmup seeding behaviour (Negative evidence 1) is fenced flat, never evaluated.
- The source ships no costs and no position semantics: all economics come from the house overlay, and single-unit/hold-no-op bookkeeping is a predeclared researcher pin, never a source claim; the Forven engine's own ordering may differ — this record is not evidence of source-engine behaviour.
- Ewm seeding uses pandas `adjust=False` recursion seeded from the first close (Negative evidence 1); the `parameter_space` optimizer ranges are in-file metadata — disclosed; the rule reads only `default_params` keys and exercises no search range; unread regime metadata (Negative evidence 4); diagnostic-only confidence/histogram echo (Negative evidence 3).
- Not independently reproduced; no live, Paper, Testnet, or profitability claim of any kind. Admission is engineering capability only. (The pool's naked-cross PPO cousin is a two-sided daily reversal system with its own evidence — cited as that record's evidence, not this rule's; this zero-gated long-flat rule's expectancy is unmeasured.)

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/ppo.py
- https://github.com/judder659/Forven
