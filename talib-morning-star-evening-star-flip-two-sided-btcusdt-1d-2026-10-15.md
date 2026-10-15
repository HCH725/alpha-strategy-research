---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TA-Lib morning-star evening-star gap-penetration flip two-sided on BTCUSDT 1d bars
created: 2026-10-15
updated: 2026-10-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-15
sources:
  - https://raw.githubusercontent.com/TA-Lib/ta-lib/v0.8.1/src/ta_func/ta_CDLMORNINGSTAR.c
  - https://raw.githubusercontent.com/TA-Lib/ta-lib/v0.8.1/src/ta_func/ta_CDLEVENINGSTAR.c
  - https://github.com/TA-Lib/ta-lib/releases/tag/v0.8.1
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TA-Lib morning-star evening-star gap-penetration flip two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read end to end (four raw files fetched over HTTPS during this cycle from the pinned `v0.8.1` tag of the canonical `TA-Lib/ta-lib` repository; both pattern files HTTP 200 with byte sizes confirmed against the fetched copies):

- Morning artifact: `src/ta_func/ta_CDLMORNINGSTAR.c` at tag `v0.8.1` (32,265 bytes as fetched) — batch function `TA_CDLMORNINGSTAR`, stateful twin `TA_S_CDLMORNINGSTAR`, streaming twin `TA_CDLMORNINGSTAR_StepImpl` carrying the identical predicate conjunction, lookback `TA_CDLMORNINGSTAR_Lookback`.
- Evening artifact: `src/ta_func/ta_CDLEVENINGSTAR.c` at tag `v0.8.1` (32,170 bytes as fetched) — batch function `TA_CDLEVENINGSTAR`, stateful twin, streaming twin `TA_CDLEVENINGSTAR_StepImpl` with the identical mirrored conjunction, lookback `TA_CDLEVENINGSTAR_Lookback`.
- Settings artifact: `src/ta_common/ta_global.c` at tag `v0.8.1` (10,248 bytes as fetched) — `TA_RestoreCandleDefaultSettings` with the full commented defaults table (each row pins range type, average period, and factor in prose, quoted below).
- Primitives artifact: `src/ta_func/ta_utility.h` at tag `v0.8.1` (11,349 bytes as fetched) — `TA_REALBODY` / `TA_CANDLERANGE` / `TA_CANDLEAVERAGE` macro definitions plus the streaming mirrors (commented as required bit-exact).
- Release pin: tag `v0.8.1`, full commit `5e766ddf650bbd4f5b49ac3c03489559ee094f28` (resolved live via `git ls-remote` during this cycle): https://github.com/TA-Lib/ta-lib/releases/tag/v0.8.1. `source_as_of` is the read date of the pinned tag, not a paper date — there is no paper here; the code is the specification.
- Licence and rights: the files carry the TA-LIB BSD-style header (`Copyright (c) 1999-2026, Mario Fortier` — redistribution in source and binary forms permitted with retained copyright notice). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pinned rule content (verified line by line; batch and streaming variants agree on every predicate):

- Morning `Must have` comment (verbatim): `first candle: long black real body`; `second candle: star (Short real body gapping down)`; `third candle: white real body that moves well within the first candle's real body`; `The meaning of "short" and "long" is specified with TA_SetCandleSettings`; `The meaning of "moves well within" is specified with optInPenetration`. Output comment (verbatim): `outInteger is positive (1 to 100): morning star is always bullish; the user should consider that a morning star is significant when it appears in a downtrend, while this function does not consider the trend`. Output is `100` on the pattern, `0` otherwise, evaluated at the close of bar `i` over bars `i-2..i`.
- Evening `Must have` comment (verbatim): `first candle: long white real body`; `second candle: star (short real body gapping up)`; `third candle: black real body that moves well within the first candle's real body`. Output comment (verbatim): `outInteger is negative (-1 to -100): evening star is always bearish; the user should consider that an evening star is significant when it appears in an uptrend, while this function does not consider the trend`. Output is `-100` on the pattern, `0` otherwise, evaluated at the close of bar `i` over bars `i-2..i`.
- Pinned penetration default (verbatim, both files): `if( optInPenetration == TA_REAL_DEFAULT ) optInPenetration = 0.3`. Any other penetration value is a different, unpinned rule.
- Pinned defaults table (verbatim rows with their comments): `{ TA_BodyLong, TA_RangeType_RealBody, 10, 1.0 }` (`real body is long when it's longer than the average of the 10 previous candles' real body`); `{ TA_BodyShort, TA_RangeType_RealBody, 10, 1.0 }` (`real body is short when it's shorter than the average of the 10 previous candles' real bodies`). Both ranges are `RealBody`, so high/low volume never enter any predicate — only opens and closes are read.
- Pinned primitives (verbatim): `TA_REALBODY(IDX)` = `fabs(close-open)`; `TA_CANDLEAVERAGE(SET,SUM,IDX)` = `factor * (avgPeriod != 0 ? SUM/avgPeriod : range)`.
- Causality comment (verbatim, both files): `add the current range and subtract the first range: this is done after the pattern recognition when avgPeriod is not 0, that means "compare with the previous candles" (it excludes the current candle)` — every trailing average compared at bar `i` is computed over strictly prior bars. No future reference, no repainting.
- Pinned lookbacks: both return `max(BodyShort_avgPeriod, BodyLong_avgPeriod) + 2` = `max(10,10)+2` = **12** under defaults. Any non-default `TA_SetCandleSettings` call would be a different, unpinned rule — this record pins defaults only.
- Performance census: the two pinned pattern files contain no return, Sharpe, win-rate, profit-factor, trade-count, or backtest figure of any kind — TA-Lib ships pattern detectors, not systems. This record claims no source-reported performance and no reproduced performance.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — TA-Lib's two directional three-candle star detectors wired into a two-sided flip book on one crypto asset — not a lossless reproduction of anything TA-Lib deploys (TA-Lib deploys nothing; it detects). Researcher-declared adaptations are exactly six: (1) research market/timeframe BTCUSDT `1d` single-frame (the code is timeframe-agnostic array logic — the daily grid is the declared deployment, never implied); (2) bar-close decision with same-bar-close market fills (the code outputs at the close of bar `i` and ships no fill convention, so the same-close fill is declared, never implied); (3) an adopted 25-bar warmup with pre-warmup bars flat by record rule (the code's structural need is a 12-bar span plus 10 bars of average seeding — see Required data); (4) house sizing/capital/costs replacing the code's complete absence of economics (position size is exactly the house Base Order per flip leg; Safety Orders explicitly disabled — see Execution assumptions); (5) the flip-only book with researcher-declared no-stop/no-target/no-trailing/no-time-exit posture (TA-Lib ships detections, never position management — the sole position-changing paths are contra-pattern flips, predeclared here); (6) two-sided direction mapping with the short leg explicit (morning `+100` targets long, evening `-100` targets short — the code's own signed output polarity). The predicate conjunctions, strict/weak edges, default settings, penetration default, lookbacks, causal averaging, pre-first-signal flat state, and every exclusion are source-native and unmodified.

Pre-write dedup (2026-10-15): working-tree case-insensitive searches for `morning.?star`, `evening.?star`, `CDLMORNING`, `CDLEVENING`, `abandoned baby`, `doji.?star`, `harami`, `piercing`, `dark.?cloud`, `tasuki`, `kicker`, `belt.?hold` return zero strategy records built on any star-pattern detector (the sole `morning.?star` / `evening.?star` prose hits sit inside the three-soldiers record's own dedup-negation paragraph, which names these families only to report their absence). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI breakout long), #63 (SuperTrend ATR-flip long), #89 (Chandelier Exit stop-flip long), #92 (SSL channel reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ on every axis (see Negative evidence 9).

## Economic mechanism

### Source-reported

Three-candle star reversal with gap-and-penetration quality filters: morning demands a long black body, then a short-bodied star gapping strictly below the first body, then a white body closing well inside the first body by the `0.3` penetration rule; evening is the exact mirror (long white, star gapping above, black close penetrating down). The code's own comments frame morning as `always bullish` and evening as `always bearish`, while warning that significance properly depends on preceding trend maturity (downtrend for morning, uptrend for evening) — a conditioning `this function does not consider`.

### Research interpretation

Exhaustion-and-reclaim speculation on a single 24/7 instrument, both sides coded. Unlike the pool's soldiers/crows continuation system (which rides three structured with-trend candles and reads shadows and open locations but no gap and no penetration), this system fires only when the middle candle detaches from the first body and the third reclaims a measured fraction of it — entries buy reclaim, not persistence, and the book never rests flat after the first signal. Unlike oscillator-cross systems it reads no normalized momentum at all — only raw open/close geometry plus trailing adaptive averages that scale the long/short/longer-than-short tolerances to recent body size. Unlike breakout systems the trigger is microstructure-shaped (bodies, body-gaps, penetration fraction) rather than level-shaped. The bet is that TA-Lib-exact star geometry on daily BTCUSDT carries reversal information net of the declared costs — with the source's own trend-maturity caveat deliberately left unmodeled and fenced (see Negative evidence 1).

## Signal

Exact rule as pinned (default settings, penetration `0.3`, strict/weak edges as coded — any other setting, tolerance, or form is a different, unpinned rule):

- Notation: bars indexed `i`; `O/H/L/C` = open/high/low/close; `RB = |C−O|`. Trailing averages (all exclude the evaluated bar, per the pinned causality comment): `avg10RB[k]` = mean `RB` over the 10 bars strictly before `k`, with three pinned windows — `W12[k]` over `[k-12, k-3]` (first-candle long test), `W11[k]` over `[k-11, k-2]` (star short test), `W10[k]` over `[k-10, k-1]` (third-candle longer-than-short test).
- Morning fire `M[i]` (code output `+100`) iff ALL of (bars `i-2,i-1,i`):
  - M1 first black (strict — doji is not black, pinned): `C[i-2] < O[i-2]`;
  - M2 third white (doji counts white — the `>=` edge is pinned, not smoothed): `C[i] >= O[i]`;
  - M3 star gapping down (body-gap, pinned): `max(O[i-1],C[i-1]) < min(O[i-2],C[i-2])`;
  - M4 penetration (pinned `fma` single-rounding form): `C[i] > fma(|O[i-2]−C[i-2]|, 0.3, C[i-2])`;
  - M5 first long: `RB[i-2] > W12[i-2]`;
  - M6 star short: `RB[i-1] <= W11[i-1]`;
  - M7 third longer-than-short: `RB[i] > W10[i]`;
  - else `0`. Evaluated at the close of completed bar `i`; needs bars back to `i-12` structurally.
- Evening fire `E[i]` (code output `-100`) iff ALL of (bars `i-2,i-1,i`):
  - E1 first white (doji counts white, pinned): `C[i-2] >= O[i-2]`;
  - E2 third black (strict, pinned): `C[i] < O[i]`;
  - E3 star gapping up (body-gap, pinned): `min(O[i-1],C[i-1]) > max(O[i-2],C[i-2])`;
  - E4 penetration (pinned multiply-subtract form — the coded asymmetry with M4, disclosed): `C[i] < C[i-2] − |O[i-2]−C[i-2]| × 0.3`;
  - E5 first long: `RB[i-2] > W12[i-2]`;
  - E6 star short: `RB[i-1] <= W11[i-1]`;
  - E7 third longer-than-short: `RB[i] > W10[i]`;
  - else `0`. Evaluated at the close of completed bar `i`; needs bars back to `i-12` structurally.
- Position target (declared flip book, same-bar-close fills): at the close of each completed bar `i` (post-warmup), the position for bar `i`'s close is long iff `M[i]` fired, short iff `E[i]` fired, else unchanged (hold current side; flat only before the first-ever fire). Flat→long buys at bar `i`'s close on `M`; flat→short sells at bar `i`'s close on `E`; long-held + `E` flips full long to full short in one atomic step at that close; short-held + `M` flips full short to full long in one atomic step at that close. Same-side refire is ignored (no adds — declared port of one-output-per-bar). At most one order event per bar close; no intrabar evaluation, no intrabar orders, no partials.
- Mutual exclusion (proven, not assumed): `M[i]` requires bar `i-2` strictly black and bar `i` white-or-doji; `E[i]` requires bar `i-2` white-or-doji and bar `i` strictly black. No bar triple satisfies both, so both legs can never fire on the same close and no priority ruling is owed.
- Degenerate tape (proven, not assumed): a zero-range day (`H = L`, hence `O = C`) cannot fire `M` (M1 needs a strict black body and M5 needs a body above a non-negative average — `0 > 0` is false) nor `E` (mirror). A fully flat history can therefore never print a first signal; the flat-until-first-fire state needs no extra guard.
- High/low/volume irrelevance (proven, not assumed): both `BodyLong` and `BodyShort` pin `TA_RangeType_RealBody`, so every average is a mean of `|C−O|`; no predicate references `H`, `L`, or `V`. Wicks and traded volume never gate an order.
- Risk legs (declared researcher posture, TA-Lib ships no position management): no stop-loss, no take-profit, no trailing, no time exit — the sole position-changing paths are contra-pattern flips. A vertical adverse move on/after the entry bar is held in full until the opposite star prints. This is the coded trade, disclosed, not a tunable parameter here.
- Direction: two-sided flip system, always-in-market after the first signal, flat before it by construction.

## Required data

- Completed `1d` bars of BTCUSDT only: `open` and `close` (colors, bodies, body-gaps, penetration, trailing averages, and same-close fills). No `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: daily bars. One evaluation per bar at its close; fills land on that same close. All inputs are completed-bar values — no provisional intrabar value is ever used; every trailing average excludes the evaluated bar by coded construction.
- Warmup: the structural need is the 12-bar pattern span plus 10 bars of average seeding (deepest reach `i-12` for the first-candle long window). The adopted warmup is the first 25 completed `1d` bars flat by record rule (predeclared researcher choice — covers the 12+10 seeding path with margin, so the first post-warmup evaluation prices every average over full windows). No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port; TA-Lib is venue-agnostic array logic — no cross-venue equivalence is claimed beyond open/close arithmetic).
- Order timing (predeclared derivation; the code outputs at bar close and ships no fill convention): completed-bar-close decision with same-bar-close market fills on the pinned Hummingbot backtesting model (package `20260920`, VERSION `dev-2.17.0`) with the Binance USDT-M perpetual connector and the completed-`1d`-candle feed. No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order event exists per bar close and mutual exclusion is proven, so there is no same-bar dual-fire to sequence; each flip is one net-fill event at a single close price, and with no stop/limit legs anywhere there is no same-bar TP/SL ordering ambiguity. Each bar's outcome is a single deterministic event (hold, open, or atomic reversal). This path uses only the already-verified primitive subset (completed-bar signal, market fill, full-quantity transition — no multi-timeframe, no intrabar, no maker, no multi-asset, no external feed); per the README admission contract, per-candidate event-level parity is required only before mass screening, and only a new unverified primitive needs one representative validation — this record introduces none.
- Cash leg: flat earns nothing by record rule (flat exists only before the first signal and under the warmup rule). No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted.
- Sizing/capital (declared, no hidden defaults): each flip leg opens exactly the house Base Order — 6% of initial capital notional, Isolated margin; the 3×/5× leverage settings scale the margin backing only, never the signal. The contra flip closes the full leg and opens the full contra leg in one atomic step. Safety Order 1 and Safety Order 2 are explicitly DISABLED in this admitted version (DCA off — permitted; the downstream DCA matrix is a separately declared experiment, never strategy behavior here). Absolute USDT capital is a run-manifest runtime input pinned per the baseline capital rule with min-notional/min-qty/step-size preflight (no silent order drops). No rule in Signal reads capital, size, margin, equity, or fill history — position state is {flat, long, short} only.
- Research cost model (explicit, disclosed, not realized): (a) fees — Binance USDⓈ-M Futures non-VIP standard schedule, with the exact maker/taker rates locked in the run manifest per baseline §4 (this record pins no rate and claims no realized cost figure); every fill here is a market (taker) fill by construction. (b) funding — NOT claimed and NOT modeled: per baseline §4 the pinned simulator has not proven historical-funding implementation, so funding is an excluded/unsupported economic term in this record (flagged openly; never reported as realized, never silently zeroed, never modeled-as-realized). The signal reads opens/closes only, so no funding-dependent leg exists that could change trade events. (c) slippage — 0 bps by explicit model assumption (disclosed limit, not a market claim). (d) precision — min-notional/min-qty/step-size preflight per the baseline capital rule.
- Concurrency: single-position machine — at most one open leg; same-state bars while positioned are no-ops; the opposite star reverses in full (one atomic event); re-entry requires the contra star (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

The pinned files ship the full construction (both predicate conjunctions with strict/weak edges, the `0.3` penetration default, the two commented default settings, the macro primitives, both lookback functions, the post-recognition average-update causality, the `+100`/`0`/`-100` output scheme, and both trend-maturity caveats). They ship zero performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Trend-maturity caveats left unmodeled, quoted plainly: morning is `significant when it appears in a downtrend` and evening `when it appears in an uptrend`, while each detector `does not consider the trend`. This record wires the raw detector outputs with no regime filter of any kind — mid-trend stars fire exactly like mature ones by construction. Adding any trend gate would be a different, unpinned rule — none is admitted here.
2. No risk layer of any kind, admitted plainly (researcher-declared posture, not source behavior): the flip-only book holds every adverse excursion until the opposite star prints, and a vertical move on the entry bar itself has no guardrail. Adding any stop would be a different, unpinned rule — none is admitted here.
3. Chop whipsaw, admitted plainly: alternating morning/evening stars in a range flip the full leg back and forth with no stop, target, or cooldown to dampen it. Widening any tolerance would be a different, unpinned rule — none is admitted here.
4. Penetration-form asymmetry, admitted plainly: morning uses exact single-rounding `fma(body, 0.3, close)` while evening uses two-rounding `close − body × 0.3`. Both are deterministic IEEE-754 double operations on identical inputs; neither side is harmonized here — harmonizing either would be a different, unpinned rule.
5. Doji-edge asymmetry, admitted plainly: first candles are strict (`<` / mirror), so a doji can never open a star; third candles are inclusive (`>=` / mirror), so a doji third leg still fires; star middles satisfy `<=` average, so exact doji middles qualify. These edges are TA-Lib's coded choice, never harmonized here.
6. Third-candle window, admitted plainly: the longer-than-short test prices its average over `[i-10, i-1]` (the `Total2` window ending one bar before the evaluated close), while the star test uses `[i-11, i-2]` and the first-long test `[i-12, i-3]` — three staggered 10-bar windows, never recentered here.
7. Warmup cost, admitted plainly: the first 25 daily bars are flat by record rule, so any star completing inside warmup is deliberately untraded — pinned, not recovered.
8. Star-identity fence, admitted plainly: the middle candle needs only a short body (`<=` average), not a doji — this is the classic star, never the doji-star/abandoned-baby family (separate TA-Lib functions, unused here). The body-gap is a real-body gap, never a high/low session gap — no wall-clock session logic exists anywhere in the rule.
9. Family-overlap fence, admitted plainly: the pool's soldiers/crows record trades three structured with-trend candles with shadow/open-location predicates and no gap and no penetration test; the 1-3-1 red-green record trades bare close-color chains with fixed risk-reward, long-only, `1h`; the dual-EMA-engulfing record gates a 2-bar cover on EMA stack plus volume, long-only, `1h`. No pool record and no open `research/*` PR wires a body-gap plus penetration-fraction three-candle star into a two-sided flip book. Shared candle input is not shared signal.
10. Derivation boundary fenced: the only non-code behaviors in this record are the BTCUSDT-`1d` deployment frame, same-bar-close fills, the adopted 25-bar warmup with record-rule pre-warmup flat, house sizing/costs with Safety Orders disabled, and the flip-only risk posture — all predeclared above; both predicate conjunctions, edges, default settings, the `0.3` penetration, lookbacks, causal averaging, signed output polarity, pre-first-signal flat state, and every exclusion are source-native. This record is therefore never evidence that any other market, frame, parameter set, penetration value, or timing of the source passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: both pinned predicate conjunctions / strict-weak edges / two default settings / penetration `0.3` / lookbacks 12+12 / flip-only book / two-sided / `1d` BTCUSDT / same-bar-close fills / 25-bar warmup are frozen.

- F1 — Gap relevance: a no-gap twin (M3/E3 dropped, all else identical) must not improve net expectancy; fail ⇒ the body-gap detachment adds nothing over attached three-candle sequences.
- F2 — Penetration relevance: a mere-inside twin (M4/E4 dropped, third close required only inside the first body) must not improve net expectancy; fail ⇒ the `0.3` reclaim fraction adds nothing over any-inside closes.
- F3 — Flip relevance: a flat-book twin (each contra star exits to flat instead of opening the contra leg, re-entering only on the next same-direction star, same frame/fills) must not improve net expectancy; fail ⇒ staying perpetually exposed through flips adds nothing over star-and-hold episodes.
- F4 — Selectivity relevance: buy-and-hold over the same sample must not improve net expectancy; fail ⇒ sitting out non-star stretches costs more in missed drift than it saves in avoided exposure.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` bar closes; fills at the same close; no venue-specific read). The open/close arithmetic ports across perpetual venues without structural change; the 24/7 market needs no session approximation (the body-gap reads bar geometry only, never wall-clock sessions — day-boundary body detachments occur routinely on calendar-cut daily bars). Both sides are explicit legs, so a spot-only deployment expresses the long half only while every flip-to-short stays venue-gated (short permission unused, never silently converted) — a spot-only variant would be a different, unpinned claim. No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session template, no cross-venue state. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived frame and fill timing: the code outputs at bar close over abstract arrays with no market, venue, or fill convention; this record decides and fills on completed `1d` bar closes. Backtest economics of other framings or timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about any other configuration.
- No source cost declaration of any kind: no fee, slippage, or funding assumption ships anywhere usable — derived evaluation must carry the full house cost load per the disclosed research cost model, and this record reports no net performance of any kind. Funding is an excluded term per baseline §4, flagged, never zeroed silently.
- Always-in-market exposure: after the first signal the book is never flat by rule, so adverse drift between contra stars is held in full — long unhedged stretches are the coded trade, disclosed, not smoothed.
- Static trailing windows: the 10-bar average windows are TA-Lib defaults, not tuned here — regime shifts in body size rescale tolerances with a fixed memory, disclosed, not adapted.
- Unmodeled trend context: per the code's own caveats, star significance depends on preceding trend maturity that the detectors ignore — this record inherits that blindness exactly as coded.
- Warmup cost: the first 25 daily bars are flat by record rule, so a star completing inside warmup is deliberately untraded — pinned, not recovered.
- Signal rarity unclaimed: no frequency, hit-rate, or expectancy claim of any kind is made for the pinned core — body-gap plus penetration stars may print rarely on any given tape; rarity is neither promised nor required for admission.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`, bar-close decision on completed `1d` bars, same-bar-close market fills, single-asset two-sided flip book) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, or Live trading. PASS means the declared derived strategy is causally expressible under the pinned Hummingbot model — not profitable, not Qlib-paritied, not source-equivalent, not live-tradable.

## Related Wiki records

None.

## Sources

- TA-Lib `v0.8.1` morning-star detector, commit `5e766ddf650bbd4f5b49ac3c03489559ee094f28` (predicate conjunction, `0.3` penetration default, lookback, causality, trend caveat verified live in the fetched file during this cycle; zero crypto claims): https://raw.githubusercontent.com/TA-Lib/ta-lib/v0.8.1/src/ta_func/ta_CDLMORNINGSTAR.c
- TA-Lib `v0.8.1` evening-star detector, same commit (mirrored conjunction, streaming-twin agreement, lookback verified live during this cycle; zero crypto claims): https://raw.githubusercontent.com/TA-Lib/ta-lib/v0.8.1/src/ta_func/ta_CDLEVENINGSTAR.c
- TA-Lib `v0.8.1` release pin: https://github.com/TA-Lib/ta-lib/releases/tag/v0.8.1
