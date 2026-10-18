---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven Heikin-Ashi flip-confirmation color-change long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/heikin_ashi.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven Heikin-Ashi flip-confirmation color-change long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-rolling-cross`, `forven-chaikin-mf-threshold-cross`, `forven-elder-ray-bull-power-cross`, `forven-adx-trend-pulse-reclaim`, `forven-dema-cross`, `forven-trix-signal-cross-zero-gate`, `forven-ultimate-oscillator-cross-gated`, `forven-bollinger-s00120-rsi-breakout`, `forven-three-bar-reversal-decline-gated`, `forven-atr-breakout-channel`, `forven-pivot-s1-bounce-r1-exit`, `forven-volatility-contraction-breakout`, `forven-connors-rsi-oversold-recross`, and `forven-kdj-dual-gate` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/heikin_ashi.py`.
- GitHub blob SHA at the pinned commit: `5fc78c13eedda553427e9fc2421c9e0396817e6a`, size 3160 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3160 bytes, 94 lines, SHA-256 `d05eb491444b48cd197548f06c03998a5d4ec86f734e115ad2b5006bf076383e`, identical to the GitHub blob (`git hash-object` reproduces `5fc78c13…6817e6a`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = HeikinAshiStrategy` (line 93), `TYPE_NAME = "heikin_ashi"` (line 13), and the `STRATEGIES = [("PREBUILT-HEIKIN-ASHI", HeikinAshiStrategy, {"_asset": "BTC"})]` roster pin (line 94). This record pins the `PREBUILT-HEIKIN-ASHI` roster leg.
- The file's own words (quoted for gate evidence, never extended): module docstring `Computes Heikin-Ashi candles (HA_close, HA_open) and enters when the candle color flips from red to green for a configurable number of confirmation bars.` (lines 1–6); `default_params` returns exactly `{ "confirmation_bars": 2, "leverage": 1.0 }` (lines 30–31); `describe()` returns `Heikin-Ashi color-change strategy requiring {cb} consecutive green bars after a red-to-green flip to confirm trend entry.` (lines 37–42); `compatible_regimes` returns `{"TREND_UP", "TREND_DOWN"}` (lines 34–35, metadata never read by the signal path); `parameter_space()` returns `{ "confirmation_bars": (1, 5, 1) }` (lines 89–90, a documented search surface only — this record pins the default 2 and runs no search).
- Single decision path (verified by `def` census): the file defines exactly eight methods (`name`, `asset`, `strategy_type`, `default_params`, `compatible_regimes`, `describe`, `generate_signal`, `parameter_space`) — `generate_signal()` (lines 44–87) is the sole signal method; no `generate_signals` vectorized twin exists anywhere in the file (0 matches), no scalar delegate, no second decision logic exists to diverge. The `confidence` value (lines 79–81) and the three `indicators` fields (`ha_close`, `ha_open`, `ha_green`, lines 82–86) are diagnostic echoes — none ever enters any predicate.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults (lines 69–70), `direction: str = "long"` default (line 72), plus `__post_init__` coercion that refuses non-Boolean flags and resolves direction labels (`_normalize_signal_flag`, `_normalize_signal_direction`, lines 140–180) — flags arriving as strict booleans (as here, via `bool(...)` at lines 75–76) pass through unchanged, and the `direction="long"` literal resolves to its book. The short-guard path (lines 47–48) constructs `Signal(price=…)` with no flags, so it inherits the all-flat defaults.
- Full-file token census (verified by search over the 94 lines this cycle): 0 `direction="short"` (the single `direction="long"` literal at line 78 is the only direction in the file); 0 `sell` / 0 `stop` / 0 `limit` / 0 `profit` / 0 `qty` (no order arguments, no risk legs of any kind); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 1.0` default); 0 `volume` / 0 `funding` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any line; 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal). The `open` series is read only inside the Heikin-Ashi transform itself (`(df["open"] + df["high"] + df["low"] + df["close"]) / 4.0` at line 51 and the recursion seed `(open[0] + close[0]) / 2.0` at line 53) — the only columns read anywhere are `open`/`high`/`low`/`close`, and `open` never acts as a timing or gap-trading leg (see Signal).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the BTC roster asset, the Heikin-Ashi recursion, the strict-green color rule, the red-to-green flip plus 2-consecutive-green entry, the first-red exit, the long-only book, and the 5-bar length guard — but ships no venue spelling, no timeframe, no fill-timing flag, no position-sizing rule, and no entry/exit evaluation ordering beyond its own two comparisons. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, chaikin-mf, elder-ray, adx-trend-pulse, dema-cross, trix-signal-cross, ultimate-oscillator, bollinger-s00120, three-bar-reversal, atr-breakout-channel, pivot-s1-bounce, volatility-contraction, connors-rsi, and kdj-dual-gate records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit position pin (the file carries no position reference; an already-positioned book treats same-side entry bars as hold-no-ops and a flat book treats exit bars as no-ops — pin disclosed, never presented as source-native semantics); (4) house sizing/capital/costs replacing the bare `leverage: 1.0` default, plus an adopted 60-bar record-rule warmup over the source's 5-bar length guard (the Heikin-Ashi open recursion is infinite-memory — see Required data; warmup pin disclosed, never presented as source-native semantics; the source declares no funding treatment at all and modeled funding is never reported as realized).

Pre-write dedup (2026-10-19): working-tree filename/content search for `builtin/heikin_ashi` / `PREBUILT-HEIKIN` / `ha_close` / `confirmation_bars` returns zero strategy records citing this source file — the pool's only Heikin-Ashi-signal record is fenced as a different construction in Negative evidence 8 (heikin-ashi-ema-trend-state: FMZ Heikin-Ashi-Trend source, EMA77/EMA21 Heikin-Ashi-context spread latch, two-sided always-in-market, no flip event, no confirmation count, no first-red exit — different source, different math, different direction handling). No closed `research/*` PR ever carried this file (merged Scout PRs #270–293 are WorldQuant/PVI/Mayer/PGO/Caporale-Plastun/wick/Ehlers/Caporale and twenty-three other Forven files through KDJ #293). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant: a flip-plus-confirmation-count raw-color machine (red-to-green edge AND two consecutive greens to enter, first red to exit) is a different signal construction from any spread-latch, cross, level, or band-break rule — not a threshold re-tuning.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: it computes Heikin-Ashi candles and enters when the candle color flips from red to green for a configurable number of confirmation bars, in up or down trends. No behavioural, structural, or risk-premium channel is claimed anywhere in the 94 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Flip-plus-confirmation color machine, long-only, edge-triggered with a count gate. Unlike latch records (heikin-ashi-ema-trend-state: the sign of an EMA77-minus-EMA21 Heikin-Ashi-context spread re-asserted every bar, always-in-market two-sided), this system never holds a standing state — its only tradable voice is the two-bar confirmation edge after a genuine red-to-green flip, so a tape that stays green prints exactly one entry and then rests, and a tape that flips red-to-green but prints only one green before reddening again trades nothing at all. Unlike single-cross records (dema-cross, trix-signal-cross: one cross event with no confirmation), the flip alone is insufficient — the two-green count is a second, independent leg that deletes one-bar whipsaw flips by construction. Unlike level-reclaim records (forven-ema-rsi-pullback: RSI reclaim of 45 under an EMA trend filter), no oscillator, no average, and no level appears anywhere — the Heikin-Ashi recursion is the entire signal, and the exit is the first red candle, not a rollover, band, or average loss. The coded consequence is a patient machine: entries cluster only on bars where a smoothed trend flip proves itself for two consecutive closes, and every position ends on the first smoothed contradiction.

## Signal

Exact rule as pinned (any other confirmation count, color strictness, seed, fill, frame, book, or ordering is a different, unpinned rule). All identifiers below are the program's own; the single `generate_signal` path (lines 44–87) is the single source of truth:

```text
ha_close[t] = (open[t] + high[t] + low[t] + close[t]) / 4
ha_open[0]  = (open[0] + close[0]) / 2
ha_open[t]  = (ha_open[t-1] + ha_close[t-1]) / 2   for t >= 1
green[t]    = ha_close[t] > ha_open[t]             // strict; equality reads red
entry       = (NOT green[t-2]) AND green[t-1] AND green[t]   // red-to-green flip + 2 consecutive greens
exit_       = NOT green[t]                          // first red candle
guard       = fewer than 5 completed bars → flat by source rule (record-rule 60-bar warmup adopted, see Required data)
```

- Trade events: `entry_signal=True` with `direction="long"` on flip-confirmation bars (lines 74–76); otherwise `entry_signal=False` with `exit_signal=bool(exit_)` on the same return. Entry and exit can never co-fire (entry requires `green[t]` true through the two-bar run; exit requires `green[t]` false on the same bar — strictly exclusive by the shared current-bar color) — no ordering pin is needed and none is pretended.
- Exact boundaries (pinned semantics): green is strict `ha_close > ha_open` (line 58) — a candle landing exactly equal (`ha_close == ha_open`) reads red: it can neither complete a confirmation run nor avoid an exit. The pre-run bar must be strictly red (`was_red`, line 63) — a two-green run preceded by a green bar enters nothing (continuation, not a flip).
- Direction: long-only with an explicit pre-first-signal flat state plus the guard flat. Zero `direction="short"` literals ship anywhere; a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the first-red leg is the sole position-ending path (`exit_`, line 68). Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence` (`clip(abs(ha_close - ha_open) / close, 0, 1)` on every bar, lines 79–81) and the three `indicators` fields are diagnostic — none conditions any order line.
- Position rule (predeclared researcher pin): single-unit; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — a continued green run cannot refire anyway since the pre-run bar is then green, so the pin only matters across exit-and-reflip sequences); a flat book treats exit bars as no-ops; re-entry re-arms on any qualifying flip-confirmation bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `open`/`high`/`low`/`close` (the four-bar-average close leg, the two-seed open recursion, and a three-bar color lookback); no bar `volume`, no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). The `open` read is causal point-in-time data (known since the bar's own open; the decision evaluates at the bar's close) — it feeds only the Heikin-Ashi smoothing transform, never a gap, session, or open-timing leg. The `compatible_regimes` set is metadata never read by the signal path (which takes only `df`); treating the label as a gate would be a different, unpinned rule.

## Required data

- Completed `1h` bars of BTCUSDT: `open`/`high`/`low`/`close` — for the Heikin-Ashi close average, the open recursion seed and chain, and the raw `close` price echo. No bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` anywhere; 0 `timeframe` tokens in the whole file).
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; all windows (the HA recursion over the decision bar and its causal past, the three-bar color lookback) read the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close (`price=round(curr_close, 4)`, pinned derived rule).
- Warmup: the source ships a length guard — `confirmation_bars(2) + 3 = 5`, and shorter frames return an explicit all-flat Signal (lines 47–48). Because the `ha_open` recursion is infinite-memory (each bar carries half the previous open), the 5-bar floor leaves seed-convergence residue: deterministic and reproducible, but not yet seed-free. This record therefore adopts a 60-bar record-rule warmup with pre-warmup bars flat (disclosed derivation — the source's 5-bar guard is preserved inside it, never contradicted): after 60 bars the seed weight `(1/2)^59` sits below float noise, so admitted events are seed-independent. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice of the `PREBUILT-HEIKIN-ASHI` roster leg — the source roster pins `_asset BTC` for this leg; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the twenty-three admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders, and no bar ever co-fires both legs (see Signal), so no ordering assumption exists to verify.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 1.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position at any time; continued-green bars hold without adds (the flip requirement makes refires impossible mid-run in any case); any first-red bar closes the open side in full; re-entry after an exit needs only the next qualifying flip-confirmation bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (94 lines: module docstring with the flip-plus-confirmation rule, `TYPE_NAME`, `default_params` with the 2-bar confirmation, the Heikin-Ashi close/open recursion, the strict-green color rule, the red-to-green-plus-two-greens entry, the first-red exit, the 5-bar guard, the `direction="long"` literal and the `round(curr_close, 4)` price echo, the `PREBUILT-HEIKIN-ASHI` roster pin). It ships zero adopted performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Guard/seed behaviour fenced: inside the guard every bar is flat by explicit source rule (lines 47–48, via the `Signal` all-flat defaults). Past the guard the HA series carries no NaN by construction (the recursion seeds bar 0 arithmetically and chains forward), so no NaN branch can fire a spurious event. The adopted 60-bar warmup additionally holds seed-convergence residue flat — disclosed, not repaired.
2. Exact-touch rule fenced: a candle with `ha_close == ha_open` reads red (`>` strict, line 58) — it can neither complete a confirmation run nor dodge an exit. Strictness is preserved throughout — disclosed, not smoothed.
3. Co-fire impossibility fenced: entry requires the current bar green, exit requires the current bar red — no bar satisfies both, so the single return statement (lines 74–87) never faces a both-legs-true bar. No tiebreak exists to specify.
4. Continuation-hold fenced: a green run longer than two bars enters only on its second bar (every later bar sees a green pre-run bar, so `was_red` is false) — the machine holds without refiring, and the single-unit pin changes no event on those bars. Disclosed, not repaired.
5. One-bar-flip deletion fenced: a red-to-green flip followed by a single green and then red trades nothing (the confirmation count is never met) and the reddening bar fires only an exit leg (a no-op on a flat book). The patience cost — missed V-shaped reversals — is the prescribed posture, disclosed as a principal limitation.
6. Confidence diagnostic fenced: the every-bar `clip(abs(ha_close - ha_open) / close, 0, 1)` never enters any predicate — an engine that skips computing confidence reaches identical events. The three indicator echoes duplicate the predicate values and likewise change no event when skipped.
7. Source basis fenced: the source names no market beyond `_asset BTC` and no timeframe at all. The BTCUSDT-`1h` choice, same-bar-close fills, single-unit pin, 60-bar warmup, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-market deployment passes.
8. Cousin records fenced as different constructions (none trades a flip-plus-confirmation raw HA color): the admitted heikin-ashi-ema-trend-state sibling trades the sign of an EMA77-minus-EMA21 Heikin-Ashi-context spread as an every-bar latch, two-sided always-in-market, off an FMZ Heikin-Ashi-Trend source (no flip event, no confirmation count, no first-red exit, different math, different source, different direction handling); the pool's flip records (psar-flip-stop-reverse, supertrend-flip PR #63) trade accelerating-stop or ATR-band flips with no Heikin-Ashi transform and no confirmation count; the pool's confirmation-count records, if any, count raw-candle or oscillator bars, never HA-color bars. Not a threshold re-tuning of any of them.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-`1h` market choice, the same-bar-close fills, the position-state pin, the 60-bar warmup, and house sizing/costs — all predeclared above; the HA recursion, the strict-green rule, the 2-bar confirmation, the flip requirement, the first-red exit, the long-only stance, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown stance are source-verbatim. The position pin changes no single-leg event: bars firing exactly one leg reach the same fill under either bookkeeping.
10. The 2-bar confirmation, the strict-green color rule, the flip requirement, the first-red exit, the long-only stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: re-tuning the confirmation count, converting the edge to a green-state hold, dropping the flip requirement, adding a stop/target/filter/cooldown/gate, adding a short leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: HA recursion as written / strict green / flip-plus-2-confirmation entry / first-red exit / single-unit long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Confirmation relevance: replacing the flip-plus-2-confirmation entry with the bare red-to-green flip (single green after red enters, same exit) must not improve net expectancy; fail ⇒ the confirmation count adds nothing over trading every flip.
- F2 — Exit relevance: replacing the first-red exit with a fixed research-defined holding period (same entry) must not improve net expectancy; fail ⇒ exiting on the first smoothed contradiction adds nothing over time exits.
- F3 — HA relevance: trading the identical flip-plus-2-confirmation structure on raw-candle color (`close > open` green, same entry/exit/pins) must not reproduce-or-beat net expectancy; fail ⇒ the Heikin-Ashi smoothing adds nothing over raw candle color and the record is a label variant of one.

## Crypto portability

Direct for the long leg on either venue type: single-venue BTCUSDT perpetual `1h` completed bars with the `open`/`high`/`low`/`close` fields only. No session calendar (crypto trades continuously; the HA recursion and the three-bar color lookback need no session-gap semantics), no corporate actions, no dividends, no funding/OI reads, no cross-venue state. 24/7 continuity means every recursion bar is always the immediately prior print — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; the record's 4-decimal price echo is display precision only and changes no event. Leverage/margin follow the house overlay, not the source's bare `1.0` default. The long-only book expresses identically on spot (no margin needed) and on perpetual under the house overlay; it is the same rule on both.

## Limitations

- The source ships no fill-timing flag: same-bar-close fills are a disclosed researcher derivation, never a source claim. An engine filling at next-open would print different event prices on identical bars.
- The source ships no timeframe: the `1h` frame is a disclosed researcher choice. Other frames re-tune nothing in the rule text but produce different event streams; they are different, unpinned evaluations.
- The source ships no costs: all economics come from the house overlay. No realized-funding claim is made; modeled funding is never reported as canonical.
- The source ships no position semantics: single-unit bookkeeping is a predeclared researcher pin, never a source claim; the Forven engine's own ordering may differ — this record is not evidence of source-engine behaviour.
- The source ships a 5-bar length guard, not seed-independence: the adopted 60-bar record-rule warmup blinds early evaluation bars to HA-recursion seed residue (fenced in Negative evidence 1); a shorter warmup would admit seed-dependent events.
- One-bar flips never trade and V-shaped reversals are missed by construction (Negative evidence 5); a run that reddens mid-confirmation strands no position but also banks nothing.
- Not independently reproduced; no live, Paper, Testnet, or profitability claim of any kind. Admission is engineering capability only.

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/heikin_ashi.py
- https://github.com/judder659/Forven
