---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven Bollinger edge-fade lower-reclaim long-flat on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/bb_fade.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven Bollinger edge-fade lower-reclaim long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-inside-bar-breakout-continuation`, `forven-williams-ema-reclaim`, `forven-linreg-channel-breakout`, `forven-zscore-mean-reversion`, `forven-adl-ema-cross`, `forven-atr-volume-breakout`, `forven-aroon-up-down-cross`, `forven-ema-rsi-pullback-reclaim`, `forven-double-bottom-neckline-break`, `forven-vwap-rolling-cross`, `forven-chaikin-mf-threshold-cross`, `forven-elder-ray-bull-power-cross`, `forven-adx-trend-pulse-reclaim`, `forven-dema-cross`, `forven-trix-signal-cross-zero-gate`, `forven-ultimate-oscillator-cross-gated`, `forven-bollinger-s00120-rsi-breakout`, `forven-three-bar-reversal-decline-gated`, `forven-atr-breakout-channel`, `forven-pivot-s1-bounce-r1-exit`, `forven-volatility-contraction-breakout`, `forven-connors-rsi-oversold-recross`, `forven-kdj-dual-gate`, and `forven-heikin-ashi-color-change` records).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T16:50:18Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/bb_fade.py`.
- GitHub blob SHA at the pinned commit: `184e5886437e46b2a0d4ec9f159555e165b4b237`, size 1798 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 1798 bytes, 49 lines, SHA-256 `cc749c2465403100e90295d882ffb7d9d157cc6d7d44194de72e6132b8dfed0f`, identical to the GitHub blob (`git hash-object` reproduces `184e5886…65b4b237`) — the entire file was retrieved and inspected.
- Registration: the file self-registers via `STRATEGY_CLASS = BBFadeStrategy`, `TYPE_NAME = "bb_fade"`, and the `STRATEGIES = [("TOMB-BBFADE", BBFadeStrategy, {"_asset": "BTC"})]` roster pin. This record pins the `TOMB-BBFADE` roster leg.
- The file's own words (quoted for gate evidence, never extended): module docstring `Bollinger Band Edge Fade strategy.`; `default_params` returns exactly `{ "bb_period": 20, "bb_std": 2.5, "leverage": 3.0 }`; `describe()` returns `Mean reversion: fades moves that pierce the outer Bollinger Bands during a ranging market.`; `compatible_regimes` returns `{"RANGE_BOUND"}` (metadata never read by the signal path); `parameter_space()` returns `{ "bb_period": (15, 25, 5), "bb_std": (2.0, 3.0, 0.5) }` (a documented search surface only — this record pins the defaults 20/2.5 and runs no search).
- Single decision path (verified by `def` census): the file defines one signal method, `generate_signal()` — no `generate_signals` vectorized twin exists anywhere in the file (0 matches), no scalar delegate, no second decision logic exists to diverge. The `confidence` value (`1.0` constant) and the single `indicators` field (`bb_lower`) are diagnostic echoes — neither ever enters any predicate.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (blob `27508a2a6b8c546e21adefdb97fc0144fabf881b`) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults, `direction: str = "long"` default, plus `__post_init__` coercion that refuses non-Boolean flags — flags arriving as strict booleans (as here, via `bool(...)`) pass through unchanged, and the `direction="long"` literal resolves to its book.
- Full-file token census (verified by search over the 49 lines this cycle): 0 `direction="short"` (the single `direction="long"` literal is the only direction in the file); 0 `sell` / 0 `stop` / 0 `limit` / 0 `profit` / 0 `qty` (no order arguments, no risk legs of any kind); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 3.0` default); 0 `volume` / 0 `funding` / 0 `request` / 0 `security` / 0 `barstate` / 0 `timeframe` in any line; 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` (no position-aware state conditions any signal); 0 `ema` / 0 `ewm` / 0 `crossover` / 0 `crossunder` (both edges are direct strict-inequality comparisons, never an ambiguous cross builtin). The only `df["…"]` read anywhere is `df["close"]` — no `open`/`high`/`low`/`volume` series is read by any line.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the BTC roster asset, the 20-bar/2.5σ Bollinger construction on closes, the strict-pierce-then-reclaim lower-band entry, the midline-level exit, the long-only book, and the no-stop posture — but ships no venue spelling, no timeframe, no fill-timing flag, no position-sizing rule, no warmup floor, and no same-bar both-legs ordering beyond its own two comparisons. Researcher-declared adaptations are exactly five: (1) research market/timeframe `BTCUSDT` `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC` and the 1h frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close — and the admitted inside-bar, williams-ema-reclaim, linreg, zscore, adl, atr-volume, aroon, ema-rsi-pullback, double-bottom, vwap-cross, chaikin-mf, elder-ray, adx-trend-pulse, dema-cross, trix-signal-cross, ultimate-oscillator, bollinger-s00120, three-bar-reversal, atr-breakout-channel, pivot-s1-bounce, volatility-contraction, connors-rsi, kdj-dual-gate, and heikin-ashi-color-change records establish same-bar-close as the pinned-Hummingbot-compatible lane primitive for this exact repository family; derivation disclosed, never presented as the Forven engine's own timing); (3) single-unit position pin with an explicit same-bar both-legs ordering rule (the source returns both flags with no ordering; the record pins flat+Both→long and positioned+Both→flat with no same-bar reopen — pin disclosed, never presented as source-native semantics; see Signal); (4) house sizing/capital/costs replacing the bare `leverage: 3.0` default; (5) a 21-bar record-rule warmup with pre-warmup bars flat (the source ships no length guard at all — only an implicit two-bar `iloc[-2]` read; the 20-bar Bollinger seed plus the one-bar edge lookback motivates 21 — disclosed derivation, never a source claim).

Pre-write dedup (2026-10-19): working-tree filename/content search for `bb_fade` / `TOMB-BBFADE` / `BBFadeStrategy` / `bb edge fade` returns zero strategy records citing this source file. No closed `research/*` PR ever carried this file (merged Scout PRs #270–294 are WorldQuant/PVI/Mayer/PGO/Caporale-Plastun/wick/Ehlers/Caporale and twenty-four other Forven files through heikin-ashi #294). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. The pool's nearest band neighbours are fenced as different constructions in Negative evidence 8 — none trades a strict-pierce lower-reclaim entry with a midline-level exit at 20/2.5σ and no regime gate. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its sentences print: it fades moves that pierce the outer Bollinger Bands during a ranging market — a mean-reversion dip-buy at the lower edge. No behavioural, structural, or risk-premium channel is claimed anywhere in the 49 lines. The file ships no performance number of any kind — this record claims no source-reported performance (see Evidence).

### Research interpretation

Strict-pierce edge-fade machine, long-only, edge-triggered entry with a level exit. Unlike breakout records (bollinger-band-breakout, s00120: price must cross ABOVE the upper rail — momentum continuation), this system buys only after price has printed strictly BELOW the lower rail and then reclaimed it — it fades the extension, never chases it. Unlike the nearest lower-reclaim cousin (sideways-dmi: same lower-rail reclaim event but gated by a DMI sideways filter, exited only at the far upper rail, at 2.0σ), this machine carries no regime gate, exits at the midline (a much shorter round-trip by construction), and uses wider 2.5σ rails (pierces are rarer and deeper). Unlike joint-condition records (chartart: RSI-50 turn AND rail reclaim on 200-bar rails, two-sided always-in), no oscillator appears anywhere here — the reclaim edge alone fires, long-only, with a flat resting state. The coded consequence is a patient fade: entries print only on bars where an overshoot below a wide lower rail proves itself reversed by the same bar's close, and every position ends at the first touch of the mean — it never rides to the opposite rail.

## Signal

Exact rule as pinned (any other period, sigma multiple, strictness, exit level, fill, frame, book, or ordering is a different, unpinned rule). All identifiers below are the program's own; the single `generate_signal` path is the single source of truth:

```text
bb_mid[t]   = mean(close[t-19 .. t])                        // rolling 20, pandas sample stdev (ddof=1)
bb_std[t]   = stdev(close[t-19 .. t])                       // pandas rolling .std(), deterministic
bb_lower[t] = bb_mid[t] - 2.5 * bb_std[t]
entry       = (close[t-1] < bb_lower[t-1]) AND (close[t] > bb_lower[t])   // strict pierce, then strict reclaim
exit_       = (close[t] >= bb_mid[t])                                     // midline level, not a cross edge
guard       = first 21 completed bars flat by record rule (see Required data)
```

- Trade events: `entry_signal=True` with `direction="long"` on strict-pierce-plus-reclaim bars; otherwise `entry_signal=False` with `exit_signal=bool(exit_)` on the same return. The exit is a STATE level, not an edge — while positioned and parked above the midline, the exit leg stays true every bar (close-and-hold-flat); on a flat book those legs are no-ops.
- Exact boundaries (pinned semantics): entry needs a STRICT pierce (`prev_close < prev_lower` — a touch landing exactly on the rail fires nothing) and a STRICT reclaim (`curr_close > curr_lower` — a close landing exactly on the rail fires nothing). The exit admits equality (`curr_close >= mid` — a close landing exactly on the midline exits). At zero variance (`bb_std == 0`, twenty identical closes) the lower rail equals the midline equals the close: entry is impossible by strictness, exit reads true (a no-op on a flat book) — fenced, never divided (the construction subtracts sigma, never divides by it, so no zero-guard is needed).
- Same-bar both-legs ordering (predeclared researcher pin — the source returns both flags with no ordering): a bar satisfying BOTH legs (a one-bar snap from strictly below the lower rail to at or above the midline) resolves by pre-bar book — a flat book OPENS long at the close (the exit leg is a no-op without a position); a positioned book CLOSES to flat at the close with NO same-bar reopen (re-entry re-arms on the next qualifying reclaim bar). Single-leg bars follow their leg; no-leg bars hold. No hidden Hummingbot default is relied upon.
- Direction: long-only with an explicit pre-first-signal flat state plus the warmup flat. Zero `direction="short"` literals ship anywhere; a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the midline-level leg is the sole position-ending path. Stop loss, take profit, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `confidence` (constant `1.0`) and the single `indicators` field (`bb_lower` echo) are diagnostic — neither conditions any order line.
- Position rule (predeclared researcher pin): single-unit; a positioned book treats further entry-only bars as hold-no-ops (no pyramiding, no averaging); a flat book treats exit-only legs as no-ops; re-entry re-arms on any qualifying reclaim bar after any exit subject to the both-legs rule above (no cooldown specified — explicitly none, not invented). Pre-first-signal and warmup bars are flat by record rule. No `position_size` / `position_avg_price` / `openprofit` / `opentrades` reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close` (band construction plus two strict comparisons); no bar `open`/`high`/`low`/`volume`, no funding/OI/mark-price read, no `request.*`, `security()`, `timeframe*`, `barstate.*`, session/calendar call, or stop/limit order argument anywhere in the order-gating path (verified by the census above returning zero matches). The bands use pandas rolling `mean`/`std` (sample stdev, `ddof=1`) — deterministic given the pinned pandas semantics; this differs from Pine `stdev` population semantics by construction, disclosed — this record never claims Pine equivalence. The `compatible_regimes` set is metadata never read by the signal path (which takes only `df`); treating the label as a gate would be a different, unpinned rule.

## Required data

- Completed `1h` bars of BTCUSDT: `close` ONLY — for the Bollinger construction and both comparisons. No bar `open`/`high`/`low`/`volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (0 `request` / 0 `security` anywhere; 0 `timeframe` tokens in the whole file).
- Single decision timeframe `1h` (researcher pin, disclosed — the file names no timeframe). One evaluation per completed bar; all windows (the 20-bar rolling bands over the decision bar and its causal past, the one-bar reclaim lookback) read the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close (`price=round(curr_close, 4)`, pinned derived rule).
- Warmup: the source ships NO length guard (only an implicit two-bar `iloc[-2]` read). This record adopts a 21-bar record-rule warmup with pre-warmup bars flat (disclosed derivation — 20 bars for the Bollinger seed plus one bar for the reclaim lookback): at 21+ bars every window and every prior-bar read is defined. Before that, leading-`NaN` band legs compare false by construction (`NaN` comparisons are `False`), so no leg can fire early — coded behaviour, disclosed. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice of the `TOMB-BBFADE` roster leg — the source roster pins `_asset BTC` for this leg; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills (`price=round(curr_close, 4)` — the decision bar's own close), compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same lane primitive the twenty-four admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders, sequenced by the predeclared both-legs ordering rule (see Signal) — no ambiguous same-bar fill order is left to the engine.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its `leverage: 3.0` default is replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all), with the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position at any time; reclaim bars while positioned hold without adds; any midline-touch bar closes the open side in full; re-entry after an exit needs only the next qualifying reclaim bar subject to the both-legs rule (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (49 lines: module docstring with the edge-fade rule, `TYPE_NAME`, `default_params` with the 20/2.5 pair, the rolling-mean/std lower-rail construction, the strict-pierce-plus-reclaim entry, the midline-level exit, the `direction="long"` literal and the `round(curr_close, 4)` price echo, the `TOMB-BBFADE` roster pin). It ships zero adopted performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Guard behaviour fenced: the source ships no guard; before the record-rule 21 bars, `bb_lower`/`bb_mid` legs are `NaN` and every strict comparison returns `False`, so every pre-warmup bar is flat by coded behaviour — disclosed, not repaired. A shorter warmup would admit `NaN`-flat bars only (never spurious events), but the 21-bar floor is still pinned so the first trusted bar has fully defined windows.
2. Exact-touch rule fenced: a prior close landing exactly on the lower rail (`==`, not `<`) is NOT a pierce and starts nothing; a current close landing exactly on the lower rail (`==`, not `>`) is NOT a reclaim and enters nothing; a close landing exactly on the midline (`>=` admits equality) DOES exit. Strictness is preserved throughout — disclosed, not smoothed.
3. Both-legs snap fenced: a one-bar snap from strictly below the lower rail to at/above the midline fires both legs and resolves by the predeclared book rule (flat→long, positioned→flat with no same-bar reopen) — disclosed researcher pin, not source semantics. The patience cost — missing the middle of the snap on a positioned book — is the prescribed posture, disclosed as a principal limitation.
4. Above-midline loiter fenced: while positioned and parked above the midline, the exit leg stays true every bar — the engine closes on the first such bar and later legs are flat-book no-ops. There is no edge requirement on the exit, so no "exit signal missed" state can strand a position: any bar at/above the mean ends it.
5. Zero-variance fenced: twenty identical closes pin `bb_std = 0`, `bb_lower = bb_mid = close` — entry strictly impossible, exit leg true (no-op on flat). No division by sigma exists anywhere, so no zero-guard is needed — disclosed, not repaired.
6. Confidence diagnostic fenced: the constant `1.0` never enters any predicate — an engine that skips computing confidence reaches identical events. The `bb_lower` indicator echo duplicates the predicate value and likewise changes no event when skipped.
7. Source basis fenced: the source names no market beyond `_asset BTC` and no timeframe at all. The BTCUSDT-`1h` choice, same-bar-close fills, single-unit pin, both-legs ordering, 21-bar warmup, and house sizing/costs are researcher choices, disclosed; this record is therefore never evidence that any source-market deployment passes.
8. Cousin records fenced as different constructions (none trades a strict-pierce lower-reclaim entry with a midline-level exit at 20/2.5σ and no gate): the admitted sideways-dmi-bollinger-breakout sibling reclaims the same lower rail but at 2.0σ, behind a DMI sideways gate, and exits only at the FAR upper rail via a crossunder edge (a full band-traverse round-trip — different exit construction, different gate, different sigma, different source); the admitted bollinger-band-breakout sibling breaks the UPPER rail for momentum continuation with a midline-cross exit (opposite side of the band, opposite posture); the admitted forven-bollinger-s00120-rsi-breakout sibling breaks the UPPER rail only while RSI(14) reads oversold on BNB with a dual mid-band-or-overbought exit (upper-side breakout plus oscillator gate, different asset); the admitted chartart-bollinger-rsi sibling needs a joint RSI(6)-50 turn AND a rail reclaim on 200-bar rails, two-sided always-in (joint oscillator condition, 10× lookback, different direction handling); the admitted vwap-bounce-band-reversal sibling reclaims a session-anchored VWAP percentage band behind an EMA-50 regime gate, two-sided (volume-weighted session math, not SMA/std rails). Not a threshold re-tuning of any of them: moving the rails to 2.0σ, adding a DMI/RSI/EMA gate, switching the exit to the far rail, or widening the lookback to 200 would each be a different, unpinned rule — none is admitted here.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-`1h` market choice, the same-bar-close fills, the position-state pin, the both-legs ordering, the 21-bar warmup, and house sizing/costs — all predeclared above; the 20/2.5 construction, the strict-pierce requirement, the strict-reclaim entry, the midline-level exit, the long-only stance, and the no-stop/no-target/no-trailing/no-time-exit/no-cooldown stance are source-verbatim. The pandas sample-stdev (`ddof=1`) band arithmetic is the file's own execution semantic — a Pine-population-stdev reading would be a different, unpinned rule.
10. The 20-bar period, the 2.5σ multiple, the strict pierce, the strict reclaim, the midline-level exit, the long-only stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: re-tuning the period/sigma, softening strictness to touches, converting the level exit to a cross edge, adding a stop/target/filter/cooldown/gate, adding a short leg, or sizing partially instead of single-unit would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 20/2.5 construction as written / strict pierce / strict reclaim entry / midline-level exit / both-legs ordering / single-unit long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Reclaim relevance: entering on every bar strictly below the lower rail (no reclaim required, same exit) must not improve net expectancy; fail ⇒ the reclaim confirmation adds nothing over buying each overshoot bar.
- F2 — Exit relevance: replacing the midline-level exit with the far-upper-rail exit (same entry) must not improve net expectancy; fail ⇒ exiting at the mean adds nothing over riding to the opposite rail.
- F3 — Band relevance: trading the identical pierce-plus-reclaim structure on a fixed percentage distance below a 20-bar SMA (same entry/exit/pins, sigma replaced by a distance leg) must not reproduce-or-beat net expectancy; fail ⇒ the 2.5σ stdev rail adds nothing over a fixed-distance dip and the record is a label variant of one.

## Crypto portability

Direct for the long leg on either venue type: single-venue BTCUSDT perpetual `1h` completed bars with the `close` field only. No session calendar (crypto trades continuously; the 20-bar rolling windows and the one-bar reclaim lookback need no session-gap semantics), no corporate actions, no dividends, no funding/OI reads, no cross-venue state. 24/7 continuity means every lookback bar is always the immediately prior print — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; the record's 4-decimal price echo is display precision only and changes no event. Leverage/margin follow the house overlay, not the source's bare `3.0` default. The long-only book expresses identically on spot (no margin needed) and on perpetual under the house overlay; it is the same rule on both.

## Limitations

- The source ships no fill-timing flag: same-bar-close fills are a disclosed researcher derivation, never a source claim. An engine filling at next-open would print different event prices on identical bars.
- The source ships no timeframe: the `1h` frame is a disclosed researcher choice. Other frames re-tune nothing in the rule text but produce different event streams; they are different, unpinned evaluations.
- The source ships no costs: all economics come from the house overlay. No realized-funding claim is made; modeled funding is never reported as canonical.
- The source ships no position semantics and no both-legs ordering: single-unit bookkeeping with the flat→long / positioned→flat same-bar rule is a predeclared researcher pin, never a source claim; the Forven engine's own ordering may differ — this record is not evidence of source-engine behaviour.
- The source ships no length guard at all: the adopted 21-bar record-rule warmup blinds early evaluation bars to Bollinger-seed `NaN` windows (fenced in Negative evidence 1); a shorter warmup would admit undefined-window bars.
- Overshoots that never reclaim never trade, and V-shaped snaps that clear the midline in one bar close a positioned book by construction (Negative evidence 3); a tape that grinds along the rail without a strict pierce prints nothing.
- The bands use pandas sample stdev (`ddof=1`), not TradingView population stdev — cross-platform rail values differ slightly by construction; this record claims only the file's own arithmetic.
- Not independently reproduced; no live, Paper, Testnet, or profitability claim of any kind. Admission is engineering capability only.

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/bb_fade.py
- https://github.com/judder659/Forven
