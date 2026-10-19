---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven VWAP pullback distance long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/vwap_pullback.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven VWAP pullback distance long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-cross`, `forven-chaikin-mf-threshold-cross`, `forven-elder-ray-bull-power-cross`, `forven-adx-trend-pulse-reclaim`, `forven-dema-cross`, `forven-trix-signal-cross`, `forven-ultimate-oscillator-cross-gated`, `forven-bollinger-s00120-rsi-breakout`, `forven-three-bar-reversal-decline-gated`, `forven-atr-breakout-channel`, `forven-pivot-s1-bounce-r1-exit`, `forven-volatility-contraction-breakout`, `forven-connors-rsi-oversold-recross`, `forven-kdj-dual-gate`, `forven-heikin-ashi-color-change`, `forven-bb-edge-fade-reclaim`, `forven-rsi-s00139-washout-cross`, `forven-obv-ema-cross-sma-gated`, `forven-mfi-threshold-cross`, `forven-williams-r-adx-gated`, `forven-rsi-boundary-rejection`, and `forven-ema-cross-adx-regime` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` against both `HEAD` and `refs/heads/main` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/vwap_pullback.py`.
- GitHub blob SHA at the pinned commit: `de2ff64ad8e5b4da8d14c6433fe83bf4e9580b3d`, size 1702 bytes.
- Byte-identity check: the file retrieved from `raw.githubusercontent.com` at the pinned commit is 1702 bytes, 46 lines, SHA-256 `dbb32cfc98f17ecf39742143f188acb991920ed5edf19bc072bd299d36b77f00`, and `git hash-object` reproduces the GitHub blob (`de2ff6…9580b`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = VWAPPullbackStrategy` (line 45), `TYPE_NAME = "vwap_pullback"` (line 5), and the `STRATEGIES = [("TOMB-VWAP", VWAPPullbackStrategy, {"_asset": "BTC"})]` roster pin (line 46). Repo-wide, no other builtin file carries this `TYPE_NAME`; working-tree search for `vwap_pullback` / `TOMB-VWAP` / `distance_pct` returns zero strategy records citing this source file.
- The file's own words (quoted for gate evidence, never extended): module docstring `VWAP Pullback strategy.` (line 1); class `describe()` returns `Trades pullbacks to the VWAP baseline after an aggressive spike.` (lines 20–21); `default_params` returns exactly `{ "distance_pct": 0.02, "leverage": 3.0 }` (line 16); `compatible_regimes` returns `{"TREND_UP", "RANGE_BOUND"}` (lines 18–19, metadata never read by the signal path); `parameter_space()` returns `{ "distance_pct": (0.01, 0.05, 0.01) }` (lines 42–43, a documented search surface only — this record pins the default and runs no search). No performance phrase of any kind ships anywhere in the 46 lines — this record adopts no source-reported performance (see Evidence).
- Single decision path, verified complete: `generate_signal()` (lines 22–41) is the sole signal method — no `generate_signals` vectorized twin exists anywhere in the 46 lines, so no twin-selection ambiguity exists. The method reads `close` (line 23), `volume` with fallback (line 24), `high`/`low`/`close` for the typical price (line 26), builds the 20-bar rolling VWAP (line 27), evaluates the distance and the reclaim exit (lines 32–35), and returns a single `Signal` (lines 37–41).
- No external helpers pinned or needed: the file imports only `pandas` plus `BaseStrategy, Signal` from `forven.strategies.base` (lines 2–3) — no `forven.strategies.indicators` import, no `scanner` import, no `request`/`security` import anywhere. The VWAP is an inline causal rolling fold (line 27), fully self-contained.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (12238 bytes) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults, `direction: str = "long"` default, plus `__post_init__` coercion; `_normalize_signal_direction` maps the `"long"` literal back to `"long"` on entry and non-entry bars alike — the file's single `direction="long"` literal (line 39) therefore survives untouched on every bar.
- Full-file token census (verified by search over the 46 lines this cycle): `direction=` occurs exactly once (`"long"` — no short leg exists); 0 `sell` / 0 `stop` / 0 `limit` / 0 `profit` / 0 `qty` / 0 `trail` (no order arguments, no live risk legs of any kind); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 3.0` default, replaced by the house overlay — see Execution assumptions); 0 `funding` / 0 `mark_price` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any line, and 0 `open`-series reads anywhere (order-gating reads are `high`/`low`/`close`/`volume` only); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` / 0 `cooldown` (no position-aware state conditions any signal); 0 `len(df)` (the file ships no length guard — the 30-bar warmup in Required data is a predeclared researcher pin, never a source claim); 0 `short` (case-insensitive, direction line excluded — no short path exists).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the TOMB-VWAP BTC roster leg, the 20-bar rolling-VWAP construction, the 2% distance entry level, the VWAP-reclaim exit level, and the long-only stance — but ships no venue spelling, no timeframe, no fill-timing flag, no length guard, no position-sizing rule, and no entry/exit evaluation ordering beyond its own level pair. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, chaikin-mf, elder-ray, adx-trend-pulse, dema-cross, trix-signal-cross, ultimate-oscillator, bollinger-s00120, three-bar-reversal, atr-breakout-channel, pivot-s1-bounce, volatility-contraction-breakout, connors-rsi, kdj, heikin-ashi, bb-edge-fade, rsi-s00139, obv-ema-cross, mfi-threshold-cross, williams-r-adx-gated, rsi-boundary-rejection, and ema-cross-adx-regime records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit position pin with hold-no-op semantics plus a 30-bar researcher warmup pin (the file carries no position reference and no length guard — an already-positioned book treats same-level entry bars as hold-no-ops, a flat book treats reclaim-level exit bars as no-ops, re-entry re-arms on any qualifying distance bar after any exit with no cooldown, and the first 30 completed bars are flat by pin — see Signal and Required data); (4) house sizing/capital/costs replacing the source's bare `leverage: 3.0` default (see Execution assumptions — never presented as source economics, and no hypothetical zero funding is claimed as realized funding).

Pre-write dedup (2026-10-19): working-tree filename/content search for `vwap_pullback` / `TOMB-VWAP` / `distance_pct` returns zero strategy records — no record cites this source file. Roster-name search for `TOMB-VWAP` returns this record only. The pool's VWAP/VWMA cousins are fenced as different constructions in Negative evidence 8 (rolling-VWAP cross, session-VWAP band bounce, VWMA-band breakout — none trades a 2%-below-rolling-VWAP distance level with a VWAP-reclaim exit, long-only). No closed `research/*` PR ever carried this source file (closed VWAP-title PR #280 is the rolling-VWAP centerline cross — a different file and rule; #278 is the EMA-RSI pullback; #246 is a BB/RSI pullback). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a distance-level pullback entry is a different normalized signal from a centerline cross or a band-breakout, with strictly different entry events, not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: pullback-to-mean trading that buys when price stretches far below its 20-bar volume-weighted baseline after an aggressive spike, and sells when price reclaims the baseline. No behavioural, structural, or risk-premium channel is claimed anywhere in the 46 lines. The file ships no backtest numbers of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Distance-level mean-reversion machine, long-only, both legs levels. Unlike the pool's rolling-VWAP cross record (which needs a strict prior/current cross pair and fires exactly on the crossing bar), this system fires entry on any bar printing more than 2% below the trailing VWAP — a persistent oversold-state leg that re-asserts every stretched bar, not a one-bar edge event. Unlike the pool's session-VWAP bounce record (session-anchored accumulator, 0.5% bands, EMA-50 regime gate, wick-touch confirmation, two-sided), this system uses a rolling 20-bar accumulator with no session reset, no regime gate, no band, and no wick test — the trigger is a single arithmetic distance, so the system fires earlier in waterfalls and holds through chop that the bounce record would gate out. Unlike stop-carrying records, the sole risk control is the reclaim exit — a position opened 2% under water is cut only when the close returns to the baseline, with no stop, no target, and no time limit. The coded consequence is a patience book: entries cluster in downdrafts, exits print only on round-trip recoveries, and flat stretches (price within 2% under VWAP or above it while flat) hold by code.

## Signal

Exact rule as pinned (any other window, distance, exit leg, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own; `generate_signal` (lines 22–41) is the single source of truth and no second decision logic exists:

```text
typ_price[t]  = (high[t] + low[t] + close[t]) / 3
vwap[t]       = sum(typ_price[i]*volume[i], i=t-19..t) / sum(volume[i], i=t-19..t)  // rolling 20-bar, causal
dist[t]       = (vwap[t] - close[t]) / vwap[t]
long_entry    = dist[t] > 0.02                  // strict, level (re-asserts every stretched bar)
long_exit     = close[t] >= vwap[t]             // reclaim level (re-asserts every reclaimed bar)
guard         = none in source — first 30 completed bars flat by researcher pin
```

- Trade events: `entry_signal=True` with `direction="long"` on distance-stretched bars (line 38); otherwise `entry_signal=False` with `exit_signal=bool(close >= vwap)` (lines 38–39). Entry and exit legs are provably mutually exclusive (Negative evidence 5), so no bar ever fires both legs and no ordering assumption exists to verify.
- Exact boundaries (pinned semantics): entry is strict (`>` — `dist` printing exactly 0.02 admits no entry and, the exit needing `close >= vwap`, holds any open side by code). Exit admits equality (`>=` — `close == vwap` closes any open side and admits no entry since `dist` is then 0). A bar with `close` exactly 2% below VWAP fires neither leg regardless of history. `confidence=1.0` on every bar (line 39) and the `indicators={"vwap"}` echo (line 40) are diagnostic constants — neither conditions any predicate.
- Volume fallback (line 24): `vol = df.get("volume", close*0+1)` — on a frame without a `volume` column the accumulator degrades to a 20-bar SMA of the typical price, deterministically. On Binance `1h` the column exists, so the live leg is the volume-weighted form as written; the fallback is disclosed, never exercised here.
- Direction: long-only with an explicit pre-first-signal flat state plus the 30-bar warmup flat. The file's single `direction="long"` literal survives the base-class normalizer untouched on every bar (verified in `base.py`); a two-sided reading would contradict the shipped rule, and no `strategy.short`-equivalent path exists. The long leg is spot-compatible; no margin short is ever required.
- Exits and risk (explicit): the VWAP-reclaim level is the sole position-ending path. Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence` and the `vwap` echo are diagnostic — neither conditions any order line.
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further distance-stretched bars as hold-no-ops (no pyramiding, no averaging); a flat book treats reclaim-level bars as no-ops; re-entry re-arms on any qualifying distance bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and warmup bars are flat by pin. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close`/`volume` with fixed non-negative offsets (a trailing 20-bar rolling fold, no shifts, no cross lookback) — no `open`-series read, no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). All windows are trailing and deterministic given the pinned pandas semantics; the first 19 bars print NaN VWAP and every NaN strict comparison is false, so pre-seed bars deterministically print neither signal — the 30-bar researcher warmup additionally holds them flat. The `compatible_regimes` set is metadata never read by the signal path (which takes only `df`/`params`); treating the label as a gate would be a different, unpinned rule. The `parameter_space` range is optimizer metadata, never read by any predicate.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` (typical-price construction) and bar `volume` (read inside the rolling-VWAP accumulator — the rule's mean reference is volume-weighted, disclosed; no standalone volume threshold leg ships). No `open`-series read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` anywhere; 0 `timeframe` tokens in the whole file).
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; every window reads the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close (`price=round(curr_close, 4)`, pinned derived rule).
- Warmup: the source ships no length guard, so this record predeclares a 30-bar researcher warmup pin — the 20-bar rolling fold needs the 20th completed bar, plus 10 bars of seeding margin; the first 30 completed bars are flat by pin. No repainting, no negative shift, no future bars/extrema, no full-sample normalization. A zero-volume 20-bar window prints NaN VWAP and both strict comparisons resolve false — deterministic no-signal, disclosed.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice of the `TOMB-VWAP` roster leg — the source roster pins `_asset BTC` for this leg; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the thirty-one admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders, and no bar ever co-fires both legs (see Signal), so no ordering assumption exists to verify.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 3.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one long position at any time; same-level entry bars hold without adds; reclaim-level bars on a flat book are no-ops; any open long ends on the first reclaim bar. Re-entry after an exit needs only the next qualifying distance bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (46 lines: module docstring with the pullback rule, `TYPE_NAME`, `default_params` with the 0.02 set, the typical-price plus rolling-VWAP fold, the distance-plus-reclaim level pair, the `direction="long"` literal and the `round(curr_close, 4)` price echo, the `TOMB-VWAP` roster pin, plus the total absence of any risk leg). It ships no performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Missing-guard fenced with a pin, not a repair: the file contains zero `len(df)` checks, and the rolling VWAP prints NaN on the first 19 bars — without a pin an engine would evaluate NaN comparisons (all false) and then start firing distance events from the 20th bar with a barely-seeded baseline. The 30-bar researcher warmup fences exactly that: pre-warmup bars are flat by pin, post-warmup events use a fully-formed 20-bar fold. An engine evaluating from bar 0 without the pin reaches different early events — disclosed, never load-bearing past warmup.
2. Volume fallback fenced: `df.get("volume", close*0+1)` degrades to a typical-price SMA when no volume column exists. On the pinned `1h` Binance path the column exists, so the evaluated rule is the volume-weighted form; the fallback is disclosed, never exercised here, and treating the SMA form as this record would be a different, unpinned rule.
3. Zero-volume window fenced: a 20-bar window summing to zero volume prints NaN VWAP (0/0) and both strict comparisons resolve false — deterministic no-signal, never a crash (pandas fold, not Python division). Deleting the guard changes no event because no guard exists to delete.
4. Diagnostic-only values fenced: `confidence=1.0` and the `indicators={"vwap"}` echo condition no predicate — deleting both reaches identical events on every bar.
5. Co-fire impossibility proven: entry needs `close < vwap*0.98` (dist > 0.02 with positive VWAP) while exit needs `close >= vwap` — both jointly true is impossible on any bar with positive prices, including exact-equality boundaries (strict entry kills the 2%-exact bar; reclaim admits the equality bar only as an exit). No tiebreak is needed and none is missing. Negative/zero VWAP prints (impossible on positiveHong prints) would still resolve by the same strict inequalities, never both-true.
6. Exact-touch rules fenced: `dist` exactly 0.02 admits no entry and triggers no exit (hold by code); `close == vwap` exits any open side and admits no entry. Strictness is preserved throughout — disclosed, not smoothed.
7. Regime metadata fenced: `compatible_regimes == {"TREND_UP", "RANGE_BOUND"}` is defined once and never called by the decision path (which takes only `df`/`params`); treating the label as an entry gate would be a different, unpinned rule.
8. Cousin records fenced as different constructions (none trades a 2%-below-rolling-20-bar-VWAP distance level with a VWAP-reclaim exit, long-only, on `1h` BTC bars from this file): the admitted `forven-vwap-rolling-cross` sibling trades a strict prior/current centerline cross pair (edge events on the crossing bar only — a stretched bar that never crosses fires nothing there but fires entry here); the admitted `vwap-bounce-band-reversal` record trades a session-anchored VWAP with 0.5% bands, an EMA-50 regime gate, wick-touch confirmation, and two-sided reversals (different accumulator, different threshold, different gates, different direction handling); the admitted `gkv-adaptive-vwma-band-breakout` record trades VWMA-14 band breakouts with a Garman-Klass volatility multiplier on `1d` (different average, different bands, breakout vs pullback, level semantics on opposite rails); the pool's `bollinger-band-breakout`, `keltner-momentum-breakout`, and `starc-band-breakout` records trade SMA/EMA-anchored bands, never a volume-weighted typical-price baseline. Not a re-tuning of any of them: swapping the window, the distance, the accumulator, the exit, or the direction handling would each be a different, unpinned rule — none is admitted here.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-`1h` market choice, the same-bar-close fills, the position-state plus 30-bar warmup pins, and house sizing/costs — all predeclared above; the 20-bar rolling VWAP, the 0.02 distance, the strict level boundaries, the reclaim exit, the long-only stance, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown stance are source-verbatim effective behaviour. The position pin changes no single-leg event: bars firing exactly one leg reach the same fill under either bookkeeping.
10. The 20-bar window, the 0.02 distance, the strict level boundaries, the reclaim exit, the single-unit long-only stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: re-tuning the window or distance, converting the distance level to a cross edge, gating with a regime/volume/ADX filter, adding a stop/target/cooldown, enabling a short leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 20-bar rolling VWAP / 0.02 distance / strict boundaries / reclaim exit / single-unit long-only / `1h` BTCUSDT / same-bar-close fills / 30-bar warmup are frozen.

- F1 — Distance relevance: tightening the entry to 3% below VWAP (exit unchanged) must not improve net expectancy; fail ⇒ the 2%-stretch leg adds nothing over a deeper-pullback machine.
- F2 — Exit relevance: replacing the reclaim exit with a fixed 8-bar time exit (same distance entries, same guard/pins) must not improve net expectancy; fail ⇒ the baseline-reclaim exit adds nothing over a clock exit.
- F3 — Baseline relevance: replacing the 20-bar rolling VWAP with a 20-bar SMA of closes (same 0.02 distance, same reclaim shape, same guard/pins) must not improve net expectancy; fail ⇒ volume-weighting adds nothing over a price-only mean.

## Crypto portability

Direct for the long leg, no margin short ever required: single-venue BTCUSDT perpetual `1h` completed bars with standard high/low/close/volume prints (the rule reads `high`/`low`/`close` for the typical price plus `volume` inside the accumulator — no `open`, no funding/OI reads). No session calendar (crypto trades continuously; the rolling 20-bar fold needs no session-gap semantics — unlike session-anchored VWAP systems, no daily reset exists to normalize), no corporate actions, no dividends, no cross-venue state. 24/7 continuity means the rolling window is always the immediately prior 20 prints — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; the record's 4-decimal price echo is display precision only and changes no event. Leverage/margin follow the house overlay, not the source's bare `3.0` default; the long-only stance is spot-compatible, and no deployment here needs a short venue.

## Limitations

- The source ships no timeframe: the `1h` frame is a disclosed researcher choice. Other frames re-tune nothing in the rule text but produce different event streams; they are different, unpinned evaluations.
- The source ships no fill-timing flag: same-bar-close fills are a disclosed researcher derivation, never a source claim. An engine filling at next-open would print different event prices on identical bars.
- The source ships no length guard: the 30-bar warmup is a disclosed researcher pin. Pre-warmup seeding behaviour (Negative evidence 1) is fenced flat, never evaluated.
- The source ships no costs and no position semantics: all economics come from the house overlay, and single-unit/hold-no-op bookkeeping is a predeclared researcher pin, never a source claim; the Forven engine's own ordering may differ — this record is not evidence of source-engine behaviour.
- Volume dependence (Negative evidence 2–3); diagnostic-only confidence/VWAP echo (Negative evidence 4); unread regime metadata (Negative evidence 7).
- The `parameter_space` optimizer range names the distance search surface — disclosed; the rule reads only the `distance_pct=0.02` default and exercises no search.
- Not independently reproduced; no live, Paper, Testnet, or profitability claim of any kind. Admission is engineering capability only.

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/vwap_pullback.py
- https://github.com/judder659/Forven
