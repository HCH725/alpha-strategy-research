---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven ROC 12 zero-cross momentum long-flat on BTCUSDT 1h bars
created: 2026-10-20
updated: 2026-10-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/roc.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven ROC 12 zero-cross momentum long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-ema-cross-adx-regime`, `forven-dema-cross`, `forven-tema-cross`, `forven-hma-cross`, `forven-macd-cross-adx-regime`, `forven-ppo-zero-gated-cross`, `forven-donchian-regime-breakout`, `forven-keltner-adx-gated-breakout`, `forven-parabolic-sar-cross`, `forven-rsi-boundary-rejection`, and thirty-eight further Forven-sibling records on `main`).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`, verified via the GitHub commits API this cycle; verified as the repository HEAD via `git ls-remote` against both `HEAD` and `refs/heads/main` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/roc.py`.
- GitHub blob SHA at the pinned commit: `1f12f9f5d7904196efb5c45325df8168ae0f151c`, size 2737 bytes.
- Byte-identity check: the file retrieved from `raw.githubusercontent.com` at the pinned commit is 2737 bytes, 107 lines, SHA-256 `fbfffc21b427a9f69133ec34067d8719d1f61512e6b956d71d61f1997c9b9cf9` (dual-fetch byte-identical this cycle), and `git hash-object` reproduces the GitHub blob (`1f12f9f5…0f151c`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = ROCStrategy` (line 103), `TYPE_NAME = "roc"` (line 9), and the single-leg `STRATEGIES = [("PREBUILT-ROC", ROCStrategy, {"_asset": "BTC"})]` roster pin (lines 105–107). No pool record cites this source file (see pre-write dedup below).
- The file's own words (quoted for gate evidence, never extended): module docstring `ROC (Rate of Change) strategy.` with `Entry: ROC crosses above 0 (upward momentum)` / `Exit: ROC crosses below 0` / `Compatible Regimes: TREND_UP, TREND_DOWN` (lines 1–6); class docstring pins the arithmetic `ROC = (close - close[n]) / close[n] * 100` with `Entry when ROC crosses above threshold; exit when ROC crosses below threshold.` (lines 14–22); `describe()` returns `Enters when ROC(12) crosses above 0.0. Exits when ROC crosses below 0.0.` at defaults (lines 45–52); `default_params` returns exactly `{ "roc_period": 12, "threshold": 0.0, "leverage": 1.0 }` (lines 33–38); `compatible_regimes` returns `{"TREND_UP", "TREND_DOWN"}` (lines 40–43, metadata never read by the signal path — `generate_signal` takes only `df` and reads only `self.params`); `parameter_space()` returns `{ "roc_period": (6, 20, 2), "threshold": (-2.0, 2.0, 0.5) }` (lines 97–101, a documented search surface only — this record pins the defaults and runs no search). No performance phrase of any kind ships anywhere in the 107 lines — this record adopts no source-reported performance (see Evidence).
- In-source length guard: `if len(df) < period + 2` (line 60, i.e. 12 + 2 = 14 bars) returns a flat `Signal(entry False, exit False, direction "long", confidence 0.0, indicators {})` (lines 60–67). The guard is source-verbatim behaviour, fenced inside the researcher warmup (see Signal).
- Single decision path: the file ships only the scalar `generate_signal()` (lines 54–95) — there is no vectorized `generate_signals` twin (zero hits), so no twin-consistency question exists at all.
- Base-class semantics pinned at the same commit (same-pin lineage as the admitted siblings): `forven/strategies/base.py` (blob `27508a2a6b8c546e21adefdb97fc0144fabf881b`, 12238 bytes, verified via the contents API this cycle) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults, `direction: str = "long"` default, plus `__post_init__` coercion; the file's two `direction="long"` literals (guard return line 64, main return line 88) therefore survive untouched on every bar.
- Full-file token census (verified by search over the 107 lines this cycle): `direction=` occurs exactly twice (both `"long"` — guard and main returns; no short leg exists); 0 `short` anywhere; 0 `sell` / 0 `crossover` / 0 `crossunder` (no display prose, no order-gating synonyms); 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` / 0 `trail` (no order arguments, no live risk legs of any kind); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default, replaced by the house overlay — see Execution assumptions); 0 `volume` / 0 `funding` / 0 `mark_price` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any line, and 0 `open`-series reads plus 0 `high` reads anywhere (the rule reads `close` only — the single `df["close"]` at line 57; not even `high`/`low` enter this file — the 3 `low` substring hits are the prose word "below" in the docstring/describe lines 4, 19, 51); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` / 0 `cooldown` (no position-aware state conditions any signal); 0 `ewm` / 0 `mean` / 0 `min_periods` / 0 `adjust` (no smoothing, no seeding recursion — the single `.shift(period)` at line 69 is the only lookback operator); 0 `rsi` / 0 `stoch` / 0 `vwap` / 0 `supertrend` / 0 `ichimoku` / 0 `rolling(` (no foreign indicator, no lookback helper of its own); 0 `atr` / 0 `adx` (no auxiliary chain at all — the family's purest unsmoothed close-only momentum file); `len(df)` exactly once (the source guard itself); the 9 `return` hits are Python return statements (five property/method returns plus the two `Signal` returns plus `describe`/`parameter_space`).
- Param fence: the predicate reads only keys present in `default_params` (`roc_period`, `threshold`, via `p["roc_period"]` / `p["threshold"]`) — treating any other key as live would be a different, unpinned rule, and no optimizer range is exercised by this record.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the PREBUILT-ROC BTC roster leg, the 12-bar/0.0-threshold construction, the cross-edge entry/exit conjunctions, the 14-bar source guard, and the long-only stance — but ships no venue spelling, no timeframe, no fill-timing flag, no position-sizing rule, and no entry/exit evaluation ordering beyond its own conjunctions. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted macd-cross, ema-cross-adx-regime, tema-cross, dema-cross, hma-cross, ppo-zero-gated-cross, and sibling records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 60-bar researcher warmup pin (the file carries no position reference; the 60-bar pin covers the 14-bar source guard plus margin over the 12-bar shift lookback, following the admitted pool ROC record's own 60-bar pin and the Forven-sibling convention — an already-positioned book treats same-side entry bars as hold-no-ops, a flat book treats cross-below exit bars as no-ops, re-entry re-arms on the next qualifying cross-above with no cooldown, pre-first-signal and warmup bars flat by pin); (4) the house cost/capital overlay replaces the file's bare `leverage: 1.0` default (the file declares no fee, funding, or margin treatment at all — house assumptions are modeled costs, and modeled funding is never reported as realized funding; see Execution assumptions).

Pre-write dedup (2026-10-20): working-tree filename/content search for `builtin/roc` / `ROCStrategy` / `PREBUILT-ROC` returns zero strategy records citing this source file. The pool's bare-ROC cousin is fenced as a different construction in Negative evidence 8 (TradingView-Pine-sourced 30-bar ROC sign-state long-flat on `1d` BTC bars — a 30-day-horizon level-state machine from an unrelated script author versus this 12-hour-horizon cross-edge machine from an immutable GitHub file). No closed `research/*` PR ever carried this source file (merged Scout PRs through #316 are WorldQuant/PVI/Mayer/PGO plus forty-five Forven files through PPO cross #316, none of them ROC). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), #251 (Swift 2-year MA multiplier zone-state long-flat), and #304 (Forven CCI oversold-recross long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: an unsmoothed 12-bar return-ratio zero-cross edge with a same-bar cross-below exit is a different normalized signal with strictly different entry events from any 30-bar level-state hold, not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: raw 12-bar return-ratio momentum that buys when the Rate of Change crosses above the zero line (upward momentum onset) and exits the long when it crosses back below zero. No behavioural, structural, or risk-premium channel is claimed anywhere in the 107 lines. The file ships no backtest numbers of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Naked unsmoothed momentum-edge machine, long-only, single cross pair. Unlike the pool's Pine-derived ROC record (30-bar level-state: long on ANY bar printing `ROC(30) > 0`, flat on ANY bar printing `ROC <= 0` — a state machine that re-asserts the posture every bar), this system fires only on transition bars: the entry needs the previous print at-or-below zero with the current print strictly above, so a run of consecutive positive prints enters once on the crossing bar and holds silently after — strictly fewer, strictly later entry events than any level-state reader of the same series. Unlike the admitted `forven-ppo-zero-gated-cross` sibling (percentage-normalized double-EMA ratio against its own 9-bar signal line plus a zero veto), the trigger here divides nothing and smooths nothing — it is the raw 12-bar price ratio itself against the fixed zero line, so entries fire earlier and choppier than any second-order oscillator rotation, at the cost of every whipsaw the smoothing siblings filter out. Unlike price-average cross cousins (EMA 20/50, DEMA, TEMA, HMA), entries fire on a return-ratio edge rather than a moving-average rotation — no average of any kind is computed anywhere in the 107 lines. Unlike stop-carrying records, the sole risk control is the ungated cross-below exit — a position opened on momentum onset is cut the first bar the 12-bar return prints strictly negative, with no stop, no target, and no zero-print early exit.

## Signal

Exact rule as pinned (any other period, threshold, gate, exit leg, fill, frame, book, or ordering is a different, unpinned rule). All identifiers below are the program's own; `generate_signal` (lines 54–95) is the single source of truth and no twin exists:

```text
roc[t]          = (close[t] - close[t-12]) / close[t-12] * 100.0
cross_up        = prev_roc <= 0.0 AND curr_roc > 0.0
cross_down      = prev_roc >= 0.0 AND curr_roc < 0.0
long_entry      = cross_up
long_exit       = cross_down                          // unconditional, ungated
guard           = source len(df) < 12 + 2 = 14 bars flat (fenced inside researcher 60-bar pin)
```

- Trade events: `entry_signal=True` with `direction="long"` on cross-up bars (line 88); otherwise `entry_signal=False` with `exit_signal=bool(cross_down)` (lines 80–84). Entry and exit legs are provably mutually exclusive (Negative evidence 6), so no bar ever fires both legs and no ordering assumption exists to verify.
- Exact boundaries (pinned semantics): cross legs admit previous-bar equality (`<=` / `>=`) but demand strict current-bar separation (`>` / `<`) — a series printing exactly unchanged fires neither leg. `roc == 0.0` admits no entry and, the exit being cross-only, holds any open side by code. A bar with both prints exactly equal fires neither entry nor exit regardless of position.
- Direction: long-only with an explicit pre-first-signal flat state plus the warmup flat. Both `direction="long"` literals survive the base-class normalizer untouched on every bar (verified in `base.py`); a two-sided reading would contradict the shipped rule, and no short-equivalent path exists. The long leg is spot-compatible; no margin short is ever required.
- Exits and risk (explicit): the ungated cross-below is the sole position-ending path. Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence` (`min(1.0, abs(curr_roc) / 5.0)` on entries, `0.0` elsewhere, lines 76–78) and the `indicators` echo (`roc`, `prev_roc`) are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; a positioned book treats same-side entry bars as hold-no-ops (no pyramiding, no averaging); a flat book treats cross-below exit bars as no-ops; re-entry re-arms on any qualifying cross-above after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and warmup bars are flat by pin. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (ratio arithmetic, both cross legs, zero comparison) — no `open`-series read, no `high`/`low` read, no bar `volume`, no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, ewm smoothing, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). The only lookback operator is a single trailing `.shift(12)` with default NaN semantics — the first 12 prints are NaN by construction, and the 14-bar source guard already fences them (both `iloc[-1]` and `iloc[-2]` sit at valid positions on every evaluated bar), so no seed-dominated early values exist here at all, unlike the ewm-seeded siblings — the 60-bar researcher warmup is pure margin (Negative evidence 1). The `compatible_regimes` set is metadata never read by the signal path (which takes only `df`); treating the label as a gate would be a different, unpinned rule. The `parameter_space` ranges are optimizer metadata, never read by any predicate.

## Required data

- Completed `1h` bars of BTCUSDT: `close` only (the 12-bar return ratio, both cross legs, the zero comparison). No bar `open`, no `high`/`low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` anywhere; 0 `timeframe` tokens in the whole file). This is the family's purest unsmoothed close-only record.
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; the shift and the two-bar cross read the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close (`price=round(curr_close, 4)`, pinned derived rule).
- Warmup: the source ships its own 14-bar length guard (`roc_period + 2`), and this record predeclares a 60-bar researcher warmup pin that covers the guard plus margin over the 12-bar shift lookback (following the admitted pool ROC record's own 60-bar pin and the Forven-sibling convention). The pin covers the shift window and the two-bar cross lookback; the first 60 completed bars are flat by pin. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice of the `PREBUILT-ROC` roster leg — the source roster pins `_asset BTC` for this leg; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders, and no bar ever co-fires both legs (see Signal), so no ordering assumption exists to verify.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 1.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one long position at any time; same-side entry bars hold without adds; cross-below bars on a flat book are no-ops; any open long ends on the first cross-below bar regardless of any other print. Re-entry after an exit needs only the next qualifying cross-above (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (107 lines: module docstring with the entry/exit/regime triple, `TYPE_NAME`, `default_params` with the 12/0.0 set, the shift-ratio arithmetic, the cross-edge conjunctions, the unconditional cross-below exit, the 14-bar source guard, the two `direction="long"` literals and the `round(curr_close, 4)` price echo, the single scalar decision path, the `PREBUILT-ROC` roster pin, plus the total absence of any risk leg). It ships no performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Warmup fenced with a pin, not a repair: the only lookback operator is `close.shift(12)` with default NaN semantics — the first 12 prints are NaN by construction, already fenced by the 14-bar source guard (both cross legs read valid floats on every evaluated bar). No ewm seeding exists here at all (`adjust=False` appears nowhere; 0 `ewm` hits), so unlike the MACD/PPO/TEMA siblings there are no seed-dominated early values to fence — the 60-bar researcher warmup is pure disclosed margin over the shift window, and pre-warmup bars are flat by pin. An engine evaluating from bar 0 without the pin reaches different early events — disclosed, never load-bearing past warmup.
2. No-smoothing fenced: the ratio is computed directly on raw closes with no average of any kind (0 `ewm` / 0 `mean` / 0 `rolling(`) — cross timing inherits the full bar-to-bar chop of the 12-bar return, unlike the admitted PPO/MACD siblings whose EMA smoothing delays every edge. Disclosed as the shipped arithmetic, not converted to a smoothed variant.
3. Diagnostic-only values fenced: `confidence` (`min(1.0, abs(curr_roc) / 5.0)`), and the `indicators` echo (`roc`, `prev_roc`) condition no predicate — deleting all three reaches identical events on every bar.
4. Regime metadata fenced: `compatible_regimes == {"TREND_UP", "TREND_DOWN"}` is defined once and never called by the decision path (which takes only `df`); treating the label as an entry gate would be a different, unpinned rule.
5. Single-path simplicity fenced: unlike the stochastic/KDJ siblings' scalar/vectorized twins, this file ships one decision path only (zero `generate_signals` hits) — no twin-selection ambiguity exists here by construction, disclosed, not repaired.
6. Co-fire impossibility proven: `cross_up` needs current ROC strictly above zero while `cross_down` needs it strictly below — both jointly true is impossible; an exactly-zero print fires neither. The threshold admits previous-bar equality only. No tiebreak is needed and none is missing.
7. Exact-touch rules fenced: previous-bar equality admits a cross leg (`<=` / `>=`), current-bar equality kills both legs; `roc == 0.0` admits no entry and triggers no exit (hold by code). Strictness is preserved throughout — disclosed, not smoothed.
8. Cousin records fenced as different constructions (none trades an unsmoothed 12-bar close-ratio zero-cross edge pair with an unconditional cross-below exit, long-only, on `1h` BTC bars from this file): the admitted `roc-sign-state-long-flat` record pins a TradingView Pine mirror plus the `CCrPAfmV` script page — a 30-bar `ta.roc` level-state machine (long on ANY positive bar, flat on ANY non-positive bar) on `1d` BTC bars, i.e. a 30-day-horizon state reader from an unrelated author versus this 12-hour-horizon cross-edge machine from an immutable GitHub file (every multi-bar positive run this record enters once, the state reader re-asserts every bar; the exact-zero print exits there and holds here); the admitted `forven-ppo-zero-gated-cross` sibling crosses a percentage-normalized double-EMA ratio against its own 9-bar signal line with a zero veto (smoothed second-order rotation, different series, different gate); the admitted `forven-macd-cross-adx-regime` sibling crosses the absolute EMA-gap against its signal with ADX-plus-EMA gates (no division — its cross timing shifts with the price level); the admitted `kst-signal-cross-trend`, `pmo-signal-cross-reversal`, `tsi-signal-cross-reversal`, `trix-dual-band-trend`, and `coppock-curve-zero-state` records trade four-horizon weighted sums, custom-smoothed momentum, double-smoothed fractions, triple-smoothed bands, and WMA-smoothed ROC-sum states — never a raw `(close[t] - close[t-12]) / close[t-12] * 100` edge pair. Not a re-tuning of any of them: swapping the smoothing, any period, the threshold, the strictness, the exit, or the direction handling would each be a different, unpinned rule — none is admitted here.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-`1h` market choice, the same-bar-close fills, the position-state plus 60-bar warmup pins, and house sizing/costs — all predeclared above; the 12/0.0 set, the shift-ratio arithmetic, the strict cross boundaries, the 14-bar source guard, the unconditional cross-below exit, the long-only stance, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown stance are source-verbatim effective behaviour. The position pin changes no single-leg event: bars firing exactly one leg reach the same fill under either bookkeeping.
10. The 12-bar period, the zero threshold, the cross-edge conjunctions, the unconditional exit, the single-unit long-only stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: re-tuning any period or threshold, converting either cross edge to a level state, gating the exit, adding a stop/target/filter/cooldown, enabling a short leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 12 / 0.0 / strict boundaries / cross-edge entry / unconditional cross-below exit / single-unit long-only / `1h` BTCUSDT / same-bar-close fills / 60-bar warmup are frozen.

- F1 — Edge relevance: replacing the cross-edge trigger with a pure level-state trigger (enter on any bar with ROC > 0 while flat, exit on any bar with ROC <= 0, same guard/pins) must not improve net expectancy; fail ⇒ the edge construction adds nothing over the state reader.
- F2 — Exit relevance: replacing the cross-below exit with a zero-print exit (close the long the first bar ROC prints at-or-below 0, same edge entries, same guard/pins) must not improve net expectancy; fail ⇒ the strict cross-below exit adds nothing over a touch exit.
- F3 — Horizon relevance: replacing the 12-bar lookback with the pool ROC record's 30-bar lookback (same edge construction, same guard/pins) must not improve net expectancy; fail ⇒ the 12-bar horizon adds nothing over the 30-bar horizon.

## Crypto portability

Direct for the long leg, no margin short ever required: single-venue BTCUSDT perpetual `1h` completed bars with standard close prints (the rule reads `close` alone — no `open`, no `high`/`low`, no `volume` dependency at all). No session calendar (crypto trades continuously; the two-bar cross needs no session-gap semantics), no corporate actions, no dividends, no funding/OI reads, no cross-venue state. 24/7 continuity means every shift-1 and shift-12 reference is always the immediately prior prints — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; the record's 4-decimal price echo is display precision only and changes no event. Leverage/margin follow the house overlay, not the source's bare `1.0` default; the long-only stance is spot-compatible, and no deployment here needs a short venue.

## Limitations

- The source ships no timeframe: the `1h` frame is a disclosed researcher choice. Other frames re-tune nothing in the rule text but produce different event streams; they are different, unpinned evaluations.
- The source ships no fill-timing flag: same-bar-close fills are a disclosed researcher derivation, never a source claim. An engine filling at next-open would print different event prices on identical bars.
- The source ships a 14-bar guard but no evaluation margin: the 60-bar warmup is a disclosed researcher pin. Pre-warmup shift-window behaviour (Negative evidence 1) is fenced flat, never evaluated.
- The source ships no costs and no position semantics: all economics come from the house overlay, and single-unit/hold-no-op bookkeeping is a predeclared researcher pin, never a source claim; the Forven engine's own ordering may differ — this record is not evidence of source-engine behaviour.
- Raw-ratio chop carries no smoothing of any kind (Negative evidence 2); the `parameter_space` optimizer ranges are in-file metadata — disclosed; the rule reads only `default_params` keys and exercises no search range; unread regime metadata (Negative evidence 4); diagnostic-only confidence/indicators echo (Negative evidence 3).
- Not independently reproduced; no live, Paper, Testnet, or profitability claim of any kind. Admission is engineering capability only. (The pool's Pine-derived ROC cousin is a 30-bar daily level-state system with its own evidence — cited as that record's evidence, not this rule's; this 12-bar cross-edge rule's expectancy is unmeasured.)

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/roc.py
- https://github.com/judder659/Forven
