---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven 20-bar range breakout long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/breakout_range.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven 20-bar range breakout long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-ema-cross-adx-regime`, `forven-dema-cross`, `forven-tema-cross`, `forven-hma-cross`, `forven-macd-cross-adx-regime`, `forven-ppo-zero-gated-cross`, `forven-roc-zero-cross-momentum`, `forven-donchian-regime-breakout`, `forven-keltner-adx-gated-breakout`, `forven-parabolic-sar-cross`, `forven-rsi-boundary-rejection`, and thirty-eight further Forven-sibling records on `main`).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`, verified via the GitHub commits API this cycle; verified as the repository HEAD via `git ls-remote` against both `HEAD` and `refs/heads/main` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/breakout_range.py`.
- GitHub blob SHA at the pinned commit: `4ecabc8872477c2b6363894ec9d314f818cbf2a8`, size 3019 bytes.
- Byte-identity check: the file retrieved from `raw.githubusercontent.com` at the pinned commit is 3019 bytes, 108 lines, SHA-256 `57e51242a4f824458e0e807fa84e18c890af6c384a331d5dee10b39021eed7d6` (dual-fetch byte-identical this cycle), and `git hash-object` reproduces the GitHub blob (`4ecabc88…18cbf2a8`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = BreakoutRangeStrategy` (line 104), `TYPE_NAME = "breakout_range"` (line 11), and the single-leg `STRATEGIES = [("PREBUILT-BREAKOUT-RANGE", BreakoutRangeStrategy, {"_asset": "BTC"})]` roster pin (lines 106–108). No pool record cites this source file (see pre-write dedup below).
- The file's own words (quoted for gate evidence, never extended): module docstring `N-bar high/low breakout strategy.` with `Enters when close breaks above the highest high of the last N bars.` / `Exits when close drops below the lowest low of the last N bars.` (lines 1–5); class docstring `N-bar range breakout strategy.` (line 15); `describe()` returns `N-bar breakout: enters when close exceeds the {period}-bar highest high, exits below the {period}-bar lowest low.` at defaults (lines 40–45); `default_params` returns exactly `{ "lookback": 20, "leverage": 1.0 }` (lines 30–34); `compatible_regimes` returns `{"BREAKOUT", "TREND_UP", "TREND_DOWN"}` (lines 36–38, metadata never read by the signal path — `generate_signal` takes only `df` and reads only the `lookback` key); `parameter_space()` returns `{ "lookback": (10, 50, 5) }` (lines 100–101, a documented search surface only — this record pins the default 20 and runs no search). No performance phrase of any kind ships anywhere in the 108 lines — this record adopts no source-reported performance (see Evidence).
- In-source length guard: `if len(df) < period + 2` (line 51, i.e. 20 + 2 = 22 bars) returns a flat `Signal(entry False, exit False, direction "long", confidence 0.0)` (lines 51–58). A second NaN guard `if pd.isna(hh) or pd.isna(ll)` returns the same flat posture (lines 67–74). Both guards are source-verbatim behaviour, fenced inside the researcher warmup (see Signal).
- Single decision path: the file ships only the scalar `generate_signal()` (lines 47–98) — there is no vectorized `generate_signals` twin (zero hits), so no twin-consistency question exists at all.
- Base-class semantics pinned at the same commit (same-pin lineage as the admitted siblings): `forven/strategies/base.py` (blob `27508a2a6b8c546e21adefdb97fc0144fabf881b`, 12238 bytes, verified via the contents API this cycle) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults, `direction: str = "long"` default, plus `__post_init__` coercion; the file's three `direction="long"` literals (guard return line 56, NaN-guard return line 72, main return line 91) therefore survive untouched on every bar.
- Full-file token census (verified by search over the 108 lines this cycle): `direction=` occurs exactly three times (all `"long"` — guard, NaN-guard, and main returns; no short leg exists); 0 `short` anywhere; 0 `sell` anywhere; 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `qty` / 0 `trail` (no order arguments, no live risk legs of any kind); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default, replaced by the house overlay — see Execution assumptions); 0 `funding` / 0 `mark_price` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any line; 0 `open`-series reads and 0 `volume` reads anywhere (the rule reads `close` once at line 49, `high` once at line 61, `low` once at line 62 — the 13 `high` / 16 `low` substring hits are the `highest_high` / `lowest_low` identifier prose plus the two rolling lines, never extra bar reads); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` / 0 `cooldown` (no position-aware state conditions any signal); 0 `ewm` / 0 `mean` / 0 `rsi` / 0 `stoch` / 0 `vwap` / 0 `supertrend` / 0 `ichimoku` / 0 `atr` / 0 `adx` / 0 `ema` / 0 `sma` (no smoothing, no auxiliary indicator chain of any kind — the two `rolling(` hits at lines 61–62 are the high/low window operators themselves); `rolling(` exactly twice; `shift` exactly three times (two code `.shift(1)` calls plus the line-60 comment `shift to avoid lookahead`); `len(df)` exactly once (the source guard itself); `generate_signal` exactly once and `generate_signals` zero times; the 10 `return` hits are Python return statements (six property/method returns plus the guard, NaN-guard, and main `Signal` returns plus `describe`/`parameter_space`).
- Param fence: the predicate reads only the key present in `default_params` (`lookback`, via `int(self.params.get("lookback", 20))` / `period`) — treating any other key as live would be a different, unpinned rule, and no optimizer range is exercised by this record.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the PREBUILT-BREAKOUT-RANGE BTC roster leg, the 20-bar symmetric high/low construction with the `.shift(1)` lookahead fence, the strict-inequality level-cross entry/exit pair, the 22-bar source guard plus NaN guard, and the long-only stance — but ships no venue spelling, no timeframe, no fill-timing flag, no position-sizing rule, and no entry/exit evaluation ordering beyond its own level comparisons. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted macd-cross, ema-cross-adx-regime, tema-cross, dema-cross, hma-cross, ppo-zero-gated-cross, roc-zero-cross, and sibling records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 60-bar researcher warmup pin (the file carries no position reference; the 60-bar pin covers the 22-bar source guard plus margin over the 20-bar rolling window and the one-bar shift lookback, following the Forven-sibling convention — an already-positioned book treats same-side entry bars as hold-no-ops, a flat book treats exit-level bars as no-ops, re-entry re-arms on the next qualifying close-above-high with no cooldown, pre-first-signal and warmup bars flat by pin); (4) the house cost/capital overlay replaces the file's bare `leverage: 1.0` default (the file declares no fee, funding, or margin treatment at all — house assumptions are modeled costs, and modeled funding is never reported as realized funding; see Execution assumptions).

Pre-write dedup (2026-10-20): working-tree filename/content search for `builtin/breakout_range` / `BreakoutRangeStrategy` / `PREBUILT-BREAKOUT-RANGE` returns zero strategy records citing this source file. No closed `research/*` PR ever carried this source file (merged Scout PRs through #317 are WorldQuant/PVI/Mayer/PGO plus forty-six Forven files through ROC cross #317, none of them breakout-range). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), #251 (Swift 2-year MA multiplier zone-state long-flat), and #304 (Forven CCI oversold-recross long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: an unfiltered symmetric 20-bar high/low level-cross pair with a same-bar low-level exit is a different normalized signal with strictly different entry events from any regime-gated asymmetric Donchian rotation, not a lookback re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: an N-bar range breakout that buys when the bar close breaks above the highest high of the last N bars and exits the long when the close drops below the lowest low of the last N bars, with the lookback window explicitly shifted one bar to avoid lookahead. No behavioural, structural, or risk-premium channel is claimed anywhere in the 108 lines. The file ships no backtest numbers of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Naked price-level breakout machine, long-only, single symmetric pair. Unlike the admitted `forven-donchian-regime-breakout` sibling (asymmetric 55-bar entry / 20-bar exit Donchian rotation gated by a 200-bar EMA trend filter plus an ADX(14) >= 25 regime veto on `1d` bars), this system applies no filter of any kind — every close printing strictly above the prior 20-bar highest high enters while flat, and every close printing strictly below the prior 20-bar lowest low exits while positioned, so entries fire strictly more often and strictly earlier than any EMA-plus-ADX-gated cousin reading the same tape. Unlike volatility-band cousins (Bollinger, Keltner, ATR-breakout, linreg-channel), the traded levels are raw rolling extrema of `high`/`low` with no mean, no standard deviation, and no average-true-range anywhere — a level break here is a range extreme, never a sigma event. Unlike oscillator zero-cross cousins (ROC, PPO, MACD, AO), no spread, ratio, or average of any kind is computed — the signal is the close's position against two trailing price levels. Unlike stop-carrying records, the sole risk control is the ungated low-level exit — a position opened on a range break is cut the first bar the close prints strictly below the trailing 20-bar lowest low, with no stop, no target, and no equality-triggered exit.

## Signal

Exact rule as pinned (any other lookback, gate, exit leg, fill, frame, book, or ordering is a different, unpinned rule). All identifiers below are the program's own; `generate_signal` (lines 47–98) is the single source of truth and no twin exists:

```text
hh[t]            = max(high[t-20 .. t-1])          // rolling(20).max().shift(1)
ll[t]            = min(low[t-20 .. t-1])           // rolling(20).min().shift(1)
long_entry      = close[t] > hh[t]
long_exit       = close[t] < ll[t]                // unconditional, ungated
guard           = source len(df) < 20 + 2 = 22 bars flat + NaN-guard flat (fenced inside researcher 60-bar pin)
```

- Trade events: `entry_signal=True` with `direction="long"` on close-above-high bars (line 88); otherwise `entry_signal=False` with `exit_signal=bool(close < ll)` (lines 79–80, 88–89). A bar printing exactly equal to a level fires neither leg on that side.
- Exact boundaries (pinned semantics): both legs demand strict separation (`>` / `<`) — a close printing exactly equal to the highest high admits no entry, and a close printing exactly equal to the lowest low triggers no exit (hold by code). The two levels satisfy `ll <= hh` on every evaluated bar by construction (both windows cover the same trailing 20 bars), so a single close cannot print strictly above the high and strictly below the low at once — co-fire is arithmetically impossible and no ordering assumption exists to verify.
- Direction: long-only with an explicit pre-first-signal flat state plus the warmup flat. All three `direction="long"` literals survive the base-class normalizer untouched on every bar (verified in `base.py`); a two-sided reading would contradict the shipped rule, and no short-equivalent path exists. The long leg is spot-compatible; no margin short is ever required.
- Exits and risk (explicit): the ungated low-level cross is the sole position-ending path. Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence` (`min((close - hh) / hh * 100, 1.0)` on entries, `0.0` elsewhere, lines 82–85) and the `indicators` echo (`highest_high`, `lowest_low`, `lookback`) are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; a positioned book treats same-side entry bars as hold-no-ops (no pyramiding, no averaging); a flat book treats low-level exit bars as no-ops; re-entry re-arms on any qualifying close-above-high after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and warmup bars are flat by pin. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (both level comparisons), `high` (highest-high window only), and `low` (lowest-low window only) — no `open`-series read, no bar `volume`, no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, ewm smoothing, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). The only lookback operators are the two trailing `rolling(20)` windows each followed by `.shift(1)` with default NaN semantics — the first 20 prints of each window are NaN by construction, already fenced by the 22-bar source guard plus the explicit NaN guard (the evaluated `hh`/`ll` sit at valid floats on every non-guard bar), so no seed-dominated early values exist here at all — the 60-bar researcher warmup is pure margin (Negative evidence 1). The `compatible_regimes` set is metadata never read by the signal path (which takes only `df`); treating the label as a gate would be a different, unpinned rule. The `parameter_space` range is optimizer metadata, never read by any predicate.

## Required data

- Completed `1h` bars of BTCUSDT: `close` (both level comparisons and the fill echo), `high` (highest-high window only), `low` (lowest-low window only). No bar `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` anywhere; 0 `timeframe` tokens in the whole file).
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; both rolling windows plus the one-bar shift read the decision bar's causal past only — no shift tricks, no future reference; fills land on the decision bar's own close (`price=round(curr_close, 4)`, pinned derived rule).
- Warmup: the source ships its own 22-bar length guard (`lookback + 2`) plus an explicit NaN guard, and this record predeclares a 60-bar researcher warmup pin that covers both guards plus margin over the 20-bar window and the one-bar shift lookback (following the Forven-sibling convention). The pin covers both rolling windows and the shift; the first 60 completed bars are flat by pin. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice of the `PREBUILT-BREAKOUT-RANGE` roster leg — the source roster pins `_asset BTC` for this leg; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders, and no bar ever co-fires both legs (see Signal), so no ordering assumption exists to verify.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 1.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one long position at any time; same-side entry bars hold without adds; low-level bars on a flat book are no-ops; any open long ends on the first close-below-low bar regardless of any other print. Re-entry after an exit needs only the next qualifying close-above-high (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (108 lines: module docstring with the entry/exit pair, `TYPE_NAME`, `default_params` with the 20-bar set, the dual rolling-window plus shift arithmetic, the strict-inequality level comparisons, the unconditional low-level exit, the 22-bar source guard plus NaN guard, the three `direction="long"` literals and the `round(curr_close, 4)` price echo, the single scalar decision path, the `PREBUILT-BREAKOUT-RANGE` roster pin, plus the total absence of any risk leg). It ships no performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Warmup fenced with a pin, not a repair: the only lookback operators are the two `rolling(20)` windows each followed by `.shift(1)` with default NaN semantics — the first 20 prints of each window are NaN by construction, already fenced by the 22-bar source guard plus the explicit `pd.isna` guard (both evaluated levels sit at valid floats on every non-guard bar). No ewm seeding exists here at all (0 `ewm` hits), so unlike the MACD/PPO/TEMA siblings there are no seed-dominated early values to fence — the 60-bar researcher warmup is pure disclosed margin over the window plus shift, and pre-warmup bars are flat by pin. An engine evaluating from bar 0 without the pin reaches different early events — disclosed, never load-bearing past warmup.
2. No-smoothing fenced: both levels are computed directly on raw `high`/`low` extrema with no average of any kind (0 `ewm` / 0 `mean` / 0 `sma` / 0 `ema`) — break timing inherits the full bar-to-bar jump of the trailing range edge, unlike the admitted Bollinger/Keltner siblings whose band arithmetic smooths every edge through a basis average. Disclosed as the shipped arithmetic, not converted to a band variant.
3. Diagnostic-only values fenced: `confidence` (`min((close - hh) / hh * 100, 1.0)`), and the `indicators` echo (`highest_high`, `lowest_low`, `lookback`) condition no predicate — deleting all three reaches identical events on every bar.
4. Regime metadata fenced: `compatible_regimes == {"BREAKOUT", "TREND_UP", "TREND_DOWN"}` is defined once and never called by the decision path (which takes only `df`); treating the label as an entry gate would be a different, unpinned rule.
5. Single-path simplicity fenced: unlike the stochastic/KDJ/ichimoku siblings' scalar/vectorized twins, this file ships one decision path only (zero `generate_signals` hits) — no twin-selection ambiguity exists here by construction, disclosed, not repaired.
6. Co-fire impossibility proven: `ll <= hh` holds on every evaluated bar (same trailing 20-bar window), so `close > hh` and `close < ll` jointly true is impossible; an exactly-on-level print fires neither leg on that side. No tiebreak is needed and none is missing.
7. Exact-touch rules fenced: both legs demand strict separation; equality on either level holds any open side by code. Strictness is preserved throughout — disclosed, not smoothed.
8. Cousin records fenced as different constructions (none trades an unfiltered symmetric 20-bar high/low level-cross pair with an unconditional low-level exit, long-only, on `1h` BTC bars from this file): the admitted `forven-donchian-regime-breakout` sibling trades an asymmetric 55-bar-entry / 20-bar-exit Donchian rotation gated by a 200-bar EMA trend filter plus ADX(14) >= 25 on `1d` bars from `donchian_regime.py` (regime-gated durable-trend machine versus this naked 20-bar range machine — every chop-break this record enters, the gated cousin skips unless trend-plus-ADX agree); the admitted `forven-bb-squeeze-breakout`, `forven-keltner-adx-gated-breakout`, `forven-atr-breakout-channel`, and `forven-linreg-channel-breakout` records trade sigma/ATR/regression bands around a smoothed basis, never raw rolling extrema; the admitted `forven-inside-bar-breakout-continuation`, `forven-three-bar-reversal-decline-gated`, `forven-engulfing-body-cover-volume`, and `forven-double-bottom-neckline-break` records trade single-bar range/pattern geometry, never a 20-bar trailing extreme; the admitted `turtle-system-2-55d-breakout` record trades a 55-day entry / 20-day exit dual-scale system with N-stop sizing on `1d` bars from a different author, never a symmetric single-scale 20-bar level pair on `1h`. Not a re-tuning of any of them: swapping any window, adding any EMA/ADX/volatility gate, splitting the exit scale, or changing the strictness, exit, or direction handling would each be a different, unpinned rule — none is admitted here.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-`1h` market choice, the same-bar-close fills, the position-state plus 60-bar warmup pins, and house sizing/costs — all predeclared above; the 20-bar set, the dual-window-plus-shift arithmetic, the strict level boundaries, the 22-bar source guard plus NaN guard, the unconditional low-level exit, the long-only stance, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown stance are source-verbatim effective behaviour. The position pin changes no single-leg event: bars firing exactly one leg reach the same fill under either bookkeeping.
10. The 20-bar lookback, the strict level comparisons, the unconditional exit, the single-unit long-only stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: re-tuning the window, converting either level cross to a state, gating the exit, adding a stop/target/filter/cooldown, enabling a short leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 20 / strict boundaries / level-cross entry / unconditional low-level exit / single-unit long-only / `1h` BTCUSDT / same-bar-close fills / 60-bar warmup are frozen.

- F1 — Level relevance: replacing the high/low level pair with a close-SMA(20) trend-state pair (enter on any bar with close above its trailing 20-bar close average while flat, exit on any bar below it, same guard/pins) must not improve net expectancy; fail ⇒ the trailing-extreme construction adds nothing over its average-state twin.
- F2 — Exit relevance: replacing the low-level exit with a high-touch exit (close the long the first bar close prints at-or-below the trailing highest high, same entries, same guard/pins) must not improve net expectancy; fail ⇒ the asymmetric low-level exit adds nothing over a symmetric touch exit.
- F3 — Horizon relevance: replacing the 20-bar window with a 55-bar window (same symmetric construction, same guard/pins) must not improve net expectancy; fail ⇒ the 20-bar horizon adds nothing over the 55-bar horizon.

## Crypto portability

Direct for the long leg, no margin short ever required: single-venue BTCUSDT perpetual `1h` completed bars with standard high/low/close prints. No session calendar (crypto trades continuously; the trailing 20-bar windows plus one-bar shift need no session-gap semantics), no corporate actions, no dividends, no funding/OI reads, no cross-venue state. 24/7 continuity means every rolling window and shift reference is always the immediately prior prints — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; the record's 4-decimal price echo is display precision only and changes no event. Leverage/margin follow the house overlay, not the source's bare `1.0` default; the long-only stance is spot-compatible, and no deployment here needs a short venue.

## Limitations

- The source ships no timeframe: the `1h` frame is a disclosed researcher choice. Other frames re-tune nothing in the rule text but produce different event streams; they are different, unpinned evaluations.
- The source ships no fill-timing flag: same-bar-close fills are a disclosed researcher derivation, never a source claim. An engine filling at next-open would print different event prices on identical bars.
- The source ships a 22-bar guard plus NaN guard but no evaluation margin: the 60-bar warmup is a disclosed researcher pin. Pre-warmup window behaviour (Negative evidence 1) is fenced flat, never evaluated.
- The source ships no costs and no position semantics: all economics come from the house overlay, and single-unit/hold-no-op bookkeeping is a predeclared researcher pin, never a source claim; the Forven engine's own ordering may differ — this record is not evidence of source-engine behaviour.
- Raw-extreme chop carries no smoothing of any kind (Negative evidence 2); the `parameter_space` optimizer range is in-file metadata — disclosed; the rule reads only the `lookback` key and exercises no search range; unread regime metadata (Negative evidence 4); diagnostic-only confidence/indicators echo (Negative evidence 3).
- Not independently reproduced; no live, Paper, Testnet, or profitability claim of any kind. Admission is engineering capability only.

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/breakout_range.py
- https://github.com/judder659/Forven
