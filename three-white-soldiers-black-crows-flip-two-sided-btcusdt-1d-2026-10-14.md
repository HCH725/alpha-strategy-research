---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TA-Lib three-white-soldiers three-black-crows flip two-sided on BTCUSDT 1d bars
created: 2026-10-14
updated: 2026-10-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-14
sources:
  - https://raw.githubusercontent.com/TA-Lib/ta-lib/v0.8.1/src/ta_func/ta_CDL3WHITESOLDIERS.c
  - https://raw.githubusercontent.com/TA-Lib/ta-lib/v0.8.1/src/ta_func/ta_CDL3BLACKCROWS.c
  - https://github.com/TA-Lib/ta-lib/releases/tag/v0.8.1
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TA-Lib three-white-soldiers three-black-crows flip two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (four raw files fetched over HTTPS during this cycle from the pinned `v0.8.1` tag of the canonical `TA-Lib/ta-lib` repository):

- Soldiers artifact: `src/ta_func/ta_CDL3WHITESOLDIERS.c` at tag `v0.8.1` (48,126 bytes as fetched) — batch function `TA_CDL3WHITESOLDIERS`, streaming twin `TA_CDL3WHITESOLDIERS_StepImpl`, lookback `TA_CDL3WHITESOLDIERS_Lookback`.
- Crows artifact: `src/ta_func/ta_CDL3BLACKCROWS.c` at tag `v0.8.1` (31,800 bytes as fetched) — batch function `TA_CDL3BLACKCROWS` (all three code-generation variants carry the identical predicate conjunction), streaming twin `TA_CDL3BLACKCROWS_StepImpl`, lookback `TA_CDL3BLACKCROWS_Lookback`.
- Settings artifact: `src/ta_common/ta_global.c` at tag `v0.8.1` — `TA_RestoreCandleDefaultSettings` with the full commented defaults table (each row pins range type, average period, and factor in prose, quoted below).
- Primitives artifact: `src/ta_func/ta_utility.h` at tag `v0.8.1` — `TA_REALBODY` / `TA_UPPERSHADOW` / `TA_LOWERSHADOW` / `TA_HIGHLOWRANGE` / `TA_CANDLERANGE` / `TA_CANDLEAVERAGE` macro definitions plus the streaming mirrors (commented as required bit-exact).
- Release pin: `https://github.com/TA-Lib/ta-lib/releases/tag/v0.8.1` (latest release at fetch time, resolved live via the GitHub releases API during this cycle). `source_as_of` is the read date of the pinned tag, not a paper date — there is no paper here; the code is the specification.
- Licence and rights: the files carry the TA-LIB BSD-style header (`Copyright (c) 1999-2026, Mario Fortier` — redistribution in source and binary forms permitted with retained copyright notice). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pinned rule content (verified line by line, batch and streaming variants agree):

- Soldiers `Must have` comment (verbatim): `three white candlesticks with consecutively higher closes`; `Greg Morris wants them to be long, Steve Nison doesn't; anyway they should not be short`; `each candle opens within or near the previous white real body`; `each candle must have no or very short upper shadow`; `to differentiate this pattern from advance block, each candle must not be far shorter than the prior candle`; `The meanings of "not short", "very short shadow", "far" and "near" are specified with TA_SetCandleSettings`.
- Soldiers output comment (verbatim): `outInteger is positive (1 to 100): advancing 3 white soldiers is always bullish; the user should consider that 3 white soldiers is significant when it appears in downtrend, while this function does not consider it`. Output is `100` on the pattern, `0` otherwise, evaluated at the close of bar `i` over bars `i-2..i`.
- Crows `Must have` comment (verbatim): `three consecutive and declining black candlesticks`; `each candle must have no or very short lower shadow`; `each candle after the first must open within the prior candle's real body`; `the first candle's close should be under the prior white candle's high`; `The meaning of "very short" is specified with TA_SetCandleSettings`.
- Crows output comment (verbatim): `outInteger is negative (-1 to -100): three black crows is always bearish; the user should consider that 3 black crows is significant when it appears after a mature advance or at high levels, while this function does not consider it`. Output is `-100` on the pattern, `0` otherwise, evaluated at the close of bar `i` over bars `i-3..i`.
- Causality comment (verbatim, present in both files): `add the current range and subtract the first range: this is done after the pattern recognition when avgPeriod is not 0, that means "compare with the previous candles" (it excludes the current candle)` — every trailing average compared at bar `i` is computed over strictly prior bars. No future reference, no repainting: outputs depend only on closed bars `≤ i`.
- Pinned defaults table (verbatim rows with their comments): `{ TA_BodyShort, TA_RangeType_RealBody, 10, 1.0 }` (`real body is short when it's shorter than the average of the 10 previous candles' real bodies`); `{ TA_ShadowVeryShort, TA_RangeType_HighLow, 10, 0.1 }` (`shadow is very short when it's shorter than 10% the average of the 10 previous candles' high-low range`); `{ TA_Near, TA_RangeType_HighLow, 5, 0.2 }` (`"near" means "<= 20% of the average of the 5 previous candles' high-low range"`); `{ TA_Far, TA_RangeType_HighLow, 5, 0.6 }` (`"far" means ">= 60% of the average of the 5 previous candles' high-low range"`).
- Pinned primitives (verbatim): `TA_REALBODY(IDX)` = `fabs(close-open)`; `TA_UPPERSHADOW(IDX)` = `high - max(close,open)`; `TA_LOWERSHADOW(IDX)` = `min(close,open) - low`; `TA_HIGHLOWRANGE(IDX)` = `high - low`; `TA_CANDLEAVERAGE(SET,SUM,IDX)` = `factor * (avgPeriod != 0 ? SUM/avgPeriod : range)`.
- Pinned lookbacks: soldiers `return max(max(ShadowVeryShort_avgPeriod,BodyShort_avgPeriod),max(Far_avgPeriod,Near_avgPeriod)) + 2` = `max(10,10,5,5)+2` = **12** under defaults; crows `return ShadowVeryShort_avgPeriod + 3` = **13** under defaults. Any non-default `TA_SetCandleSettings` call would be a different, unpinned rule — this record pins defaults only.
- Performance census: the two pinned pattern files contain no return, Sharpe, win-rate, profit-factor, trade-count, or backtest figure of any kind — TA-Lib ships pattern detectors, not systems. This record claims no source-reported performance and no reproduced performance.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — TA-Lib's two directional three-candle detectors wired into a two-sided flip book on one crypto asset — not a lossless reproduction of anything TA-Lib deploys (TA-Lib deploys nothing; it detects). Researcher-declared adaptations are exactly six: (1) research market/timeframe BTCUSDT `1d` single-frame (the code is timeframe-agnostic array logic — the daily grid is the declared deployment, never implied); (2) bar-close decision with next-bar-open market fills (the code outputs at the close of bar `i`; it ships no fill convention, so the sequential next-open fill is declared, never implied); (3) an adopted 25-bar warmup with pre-warmup bars flat by record rule (the code's structural need is 13 bars of pattern span plus 10 bars of average seeding — see Required data for the rationale); (4) house sizing/capital/costs replacing the code's complete absence of economics (the single-unit, never-add posture is the declared port of having exactly one output leg per bar); (5) the flip-only book with researcher-declared no-stop/no-target/no-trailing/no-time-exit posture (TA-Lib ships detections, never position management — the sole position-changing paths are contra-pattern flips, predeclared here); (6) two-sided direction mapping with the short leg explicit (soldiers `+100` targets long, crows `-100` targets short — the code's own signed output polarity). The predicate conjunctions, strict/weak edges, default settings, lookbacks, causal averaging, pre-first-signal flat state, and every exclusion are source-native and unmodified.

Pre-write dedup (2026-10-14): working-tree case-insensitive searches for `white soldier`, `black crow`, `morning.?star`, `evening.?star`, `abandoned baby`, `harami`, `tasuki`, `kicker`, `belt.?hold`, `three soldiers`, `soldiers`, `cdl3`, `ta-lib`, `talib` return zero strategy records built on any TA-Lib candle function (the sole `talib` prose hits are dead-import quarantines inside the TD-sequential record, whose signal path is pure pandas run-counting with zero `ta.` call sites). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI breakout long), #63 (SuperTrend ATR-flip long), #89 (Chandelier Exit stop-flip long), #92 (SSL channel reversal two-sided) — different mechanisms, indicators, and sources. Closest pool record differs on every axis: `three-down-three-up-consec-close-long-btcusdt-1h-2026-10-07.md` buys three consecutive lower closes as a long-only fade and exits to flat on three higher closes (close-count snap-back, `1h`, FMZ Pine v6 source, same-bar-close fills, long-only, flat-book). Five-axis distinction: mechanism differs (structured three-candle with-trend continuation flip — soldiers fires after three rising closes to go/stay long — versus against-the-move fade that buys washed-out declines); signal construction differs (real-body / open-location / shadow predicates against trailing adaptive averages with four pinned default settings, versus bare close-vs-prior-close chains that read `close` only); exits differ (contra-pattern flip-only book, always-in-market after the first signal with explicitly no stop/target/trailing/time leg, versus 3-up-count exit-to-flat); source identity differs (TA-Lib `v0.8.1` immutable C detectors versus FMZ 482589 Pine v6); frame/fills/direction differ (`1d` next-open two-sided versus `1h` same-close long-only).

## Economic mechanism

### Source-reported

Three-candle advance/decline persistence with quality filters (mirror titles `Three White Soldiers` / `Three Black Crows`): soldiers demands three white candles with consecutively higher closes whose opens sit within-or-near the prior white body, whose upper shadows are negligible against the trailing range, whose bodies do not shrink abruptly (advance-block rejection), and whose final body is not short against the trailing body average; crows demands a white candle followed by three black candles with consecutively declining closes, each opening strictly inside the prior black body, the first black closing under the white candle's high, each with negligible lower shadow. The code's own comments frame soldiers as `always bullish` and crows as `always bearish`, while warning that significance properly depends on preceding trend maturity (downtrend for soldiers, mature advance/high levels for crows) — a conditioning `this function does not consider`.

### Research interpretation

With-trend three-candle continuation speculation on a single 24/7 instrument, both sides coded. Unlike the pool's 3-down/3-up fade (which buys only washed-out declines and exits to flat on recovery counts), this system buys strength confirmed across three structured candles and sells weakness confirmed across three structured candles — entries ride persistence rather than fading exhaustion, and the book never rests flat after the first signal. Unlike oscillator-cross systems it reads no normalized momentum at all — only raw OHLC geometry plus trailing adaptive averages that scale every tolerance to recent volatility (a `0.1×` shadow in a compressed tape is an objectively smaller shadow than in an expanded one). Unlike raw-channel breakouts the trigger is microstructure-shaped (bodies, opens, shadows) rather than level-shaped. The bet is that TA-Lib-exact three-candle advance/decline structure on daily BTCUSDT carries continuation information net of the declared costs — with the source's own trend-maturity caveat deliberately left unmodeled and fenced (see Negative evidence 1).

## Signal

Exact rule as pinned (default settings, strict/weak edges as coded — any other setting, tolerance, or form is a different, unpinned rule):

- Notation: bars indexed `i`; `O/H/L/C` = open/high/low/close; `RB = |C−O|`; `HL = H−L`. Trailing averages (all exclude the evaluated bar, per the pinned causality comment): `avg10RB[k]` = mean `RB` over the 10 bars strictly before `k`; `avg10HL[k]` = mean `HL` over the 10 bars strictly before `k`; `avg5HL[k]` = mean `HL` over the 5 bars strictly before `k`.
- Soldiers fire `S[i]` (code output `+100`) iff ALL of (bars `i-2,i-1,i`):
  - S1 three white: `C[j] >= O[j]` for `j ∈ {i-2,i-1,i}` (doji counts white — the `>=` edge is pinned, not smoothed);
  - S2 very short upper shadows: `H[j] − max(C[j],O[j]) < 0.1 × avg10HL[j]` for all three;
  - S3 consecutive higher closes: `C[i] > C[i-1] > C[i-2]` (strict);
  - S4 opens within-or-near prior body: `O[i-1] > O[i-2]` and `O[i-1] <= C[i-2] + 0.2 × avg5HL[i-2]`; `O[i] > O[i-1]` and `O[i] <= C[i-1] + 0.2 × avg5HL[i-1]` (weak `<=` edge plus `0.2` tolerance — pinned asymmetry with crows, disclosed);
  - S5 not far shorter (advance-block filter): `RB[i-1] > RB[i-2] − 0.6 × avg5HL[i-2]` and `RB[i] > RB[i-1] − 0.6 × avg5HL[i-1]`;
  - S6 final body not short: `RB[i] > avg10RB[i]`;
  - else `0`. Evaluated at the close of completed bar `i`; needs bars back to `i-12` structurally.
- Crows fire `C[i]` (code output `-100`) iff ALL of (bars `i-3..i`):
  - C1 colors: `C[i-3] >= O[i-3]` (prior white) and `C[j] < O[j]` for `j ∈ {i-2,i-1,i}` (strict black — doji is not black, pinned);
  - C2 opens strictly within prior body (no tolerance — pinned asymmetry with soldiers, disclosed): `O[i-1] < O[i-2]` and `O[i-1] > C[i-2]`; `O[i] < O[i-1]` and `O[i] > C[i-1]`;
  - C3 first black under prior high: `H[i-3] > C[i-2]` (strict);
  - C4 three declining: `C[i-2] > C[i-1] > C[i]` (strict);
  - C5 very short lower shadows: `min(C[j],O[j]) − L[j] < 0.1 × avg10HL[j]` for all three black bars;
  - else `0`. Evaluated at the close of completed bar `i`; needs bars back to `i-13` structurally.
- Position target (pinned flip book): at the close of each completed bar `i` (post-warmup), the target for the next bar is long iff `S[i]` fired, short iff `C[i]` fired, else unchanged (hold current side; flat only before the first-ever fire). Orders fire for the next bar's open: flat→long buys at next open on `S`; flat→short sells at next open on `C`; long-held + `C` flips full long to full short in one step at next open; short-held + `S` flips full short to full long in one step at next open. Same-side refire is ignored (single-unit, no adds — declared port of one-output-per-bar). At most one order event per bar boundary; no intrabar evaluation, no intrabar orders, no partials.
- Mutual exclusion (proven, not assumed): `S[i]` requires bars `i-2..i` white (`C >= O`); `C[i]` requires the same bars strictly black (`C < O`). No bar triple satisfies both, so both legs can never fire on the same close and no priority ruling is owed.
- Degenerate tape (proven, not assumed): a zero-range day (`H = L`, hence `O = C = H = L`) cannot fire `S` (S3/S6 need strict rising closes and a body above a non-negative average — `0 > 0` is false) nor `C` (C1/C4 need strict black/declining closes). A fully flat history can therefore never print a first signal; the flat-until-first-fire state needs no extra guard.
- Risk legs (declared researcher posture, TA-Lib ships no position management): no stop-loss, no take-profit, no trailing, no time exit — the sole position-changing paths are contra-pattern flips. A vertical adverse move on/after the entry bar is held in full until the opposite triple prints. This is the coded trade, disclosed, not a tunable parameter here.
- Direction: two-sided flip system, always-in-market after the first signal, flat before it by construction.

## Required data

- Completed `1d` bars of BTCUSDT only: `open`, `high`, `low`, `close` (colors, bodies, shadows, opens-locations, closes-chains, trailing averages, and next-open fills). No `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: daily bars. One evaluation per bar at its close; fills land on the next daily bar's open. All inputs are completed-bar values — no provisional intrabar value is ever used; every trailing average excludes the evaluated bar by coded construction.
- Warmup: the structural need is the 13-bar crows span plus 10 bars of average seeding (soldiers needs 12 + 10). The adopted warmup is the first 25 completed `1d` bars flat by record rule (predeclared researcher choice — covers the deeper 13+10 seeding path with margin, so the first post-warmup evaluation prices every average over full windows). No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port; TA-Lib is venue-agnostic array logic — no cross-venue equivalence is claimed beyond OHLC arithmetic).
- Order timing (predeclared derivation; the code outputs at bar close and ships no fill convention): completed-bar-close decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per bar boundary and mutual exclusion is proven, so there is no same-bar dual-fire to sequence; each flip is one net fill step at a single open price.
- Cash leg: flat earns nothing by record rule (flat exists only before the first signal). No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted.
- Sizing/capital/costs: the code ships no portable economics — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3×/5×) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — long bars carry realized funding, short bars carry realized funding, pre-first-signal flat bars carry none) replace them here, never presented as source-native behavior. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one single-unit position (long or short) at any time after the first signal; every position-changing event flips in full in one step; no cooldown specified — explicitly none, not invented (re-entry requires the opposite triple, so a cooldown would only delay coded flips). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue. Safety orders: explicitly none.

## Evidence

### Source-reported

The pinned files ship the full construction (both predicate conjunctions with strict/weak edges, the four commented default settings, the macro primitives, both lookback functions, the post-recognition average-update causality, the `+100`/`0`/`-100` output scheme, the Morris-vs-Nison design note, and both trend-maturity caveats). They ship zero performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Trend-maturity caveats left unmodeled, quoted plainly: soldiers is `significant when it appears in downtrend` and crows after `a mature advance or at high levels`, while the detectors `do[] not consider it`. This record wires the raw detector outputs with no regime filter of any kind — mid-trend triples fire exactly like mature ones by construction. Adding any trend gate would be a different, unpinned rule — none is admitted here.
2. No risk layer of any kind, admitted plainly (researcher-declared posture, not source behavior): the flip-only book holds every adverse excursion until the opposite triple prints, and a vertical move on the entry bar itself has no guardrail. Adding any stop would be a different, unpinned rule — none is admitted here.
3. Chop whipsaw, admitted plainly: alternating soldiers/crows triples in a range flip the full unit back and forth with no stop, target, or cooldown to dampen it; triples that share bars can alternate faster than the 3-bar structure suggests. Widening any tolerance would be a different, unpinned rule — none is admitted here.
4. Asymmetric open tolerance, admitted plainly: soldiers opens may sit up to `0.2 × avg5HL` above the prior close (`<=` edge); crows opens must sit strictly inside the prior body with zero tolerance. This asymmetry is TA-Lib's coded choice, never harmonized here — harmonizing either side would be a different, unpinned rule.
5. Morris-vs-Nison compromise, admitted plainly: the code requires bodies `not short` against the trailing average rather than strictly `long` — weak-body triples that satisfy S6 still fire. Demanding long bodies via `TA_SetCandleSettings` would be a different, unpinned rule — none is admitted here.
6. Warmup cost, admitted plainly: the first 25 daily bars are flat by record rule, so any triple completing inside warmup is deliberately untraded — pinned, not recovered.
7. Close-to-open seams, admitted plainly: every entry and flip fills at the next bar's open — gap-through moves across signal edges are taken at post-move opens, never at the signal close.
8. Derivation boundary fenced: the only non-code behaviors in this record are the BTCUSDT-`1d` deployment frame, next-open fills, the adopted 25-bar warmup with record-rule pre-warmup flat, house sizing/costs, and the flip-only risk posture — all predeclared above; both predicate conjunctions, edges, default settings, lookbacks, causal averaging, signed output polarity, pre-first-signal flat state, and every exclusion are source-native. This record is therefore never evidence that any TA-Lib deployment passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: both pinned predicate conjunctions / strict-weak edges / four default settings / lookbacks 12+13 / flip-only book / two-sided / `1d` BTCUSDT / next-open fills / 25-bar warmup are frozen.

- F1 — Structure relevance: a bare-count twin (long-target on three white rising closes, short-target on three black declining closes, no body/open/shadow predicates, same book/frame/fills) must not improve net expectancy; fail ⇒ the real-body, open-location, shadow, and advance-block predicates add nothing over naked three-close chains.
- F2 — Flip relevance: a flat-book twin (each contra triple exits to flat instead of opening the contra unit, re-entering only on the next same-direction triple, same frame/fills) must not improve net expectancy; fail ⇒ staying perpetually exposed through flips adds nothing over pattern-and-hold episodes.
- F3 — Shadow relevance: a no-shadow twin (S2 and C5 predicates dropped, all else identical) must not improve net expectancy; fail ⇒ the very-short-shadow quality filters add nothing over unfiltered triples.
- F4 — Selectivity relevance: buy-and-hold over the same sample must not improve net expectancy; fail ⇒ sitting out non-triple stretches costs more in missed drift than it saves in avoided exposure.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` bar closes; fills at next-bar opens; no venue-specific read). The OHLC arithmetic ports across perpetual venues without structural change; the 24/7 market needs no session approximation (patterns read bar geometry only, never wall-clock sessions). Both sides are explicit legs, so a spot-only deployment expresses the long half only while every flip-to-short stays venue-gated (short permission unused, never silently converted) — a spot-only variant would be a different, unpinned claim. No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session template, no cross-venue state. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived frame and fill timing: the code outputs at bar close over abstract arrays with no market, venue, or fill convention; this record decides on completed `1d` bars with next-open fills. Backtest economics of other framings or timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about any other configuration.
- No source cost declaration of any kind: no fee, slippage, or funding assumption ships anywhere usable — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Always-in-market exposure: after the first signal the book is never flat by rule, so adverse drift between contra triples is held in full — long unhedged stretches are the coded trade, disclosed, not smoothed.
- Static trailing windows: the 10-bar and 5-bar average windows are TA-Lib defaults, not tuned here — regime shifts in volatility rescale tolerances with a fixed memory, disclosed, not adapted.
- Unmodeled trend context: per the code's own caveats, triple significance depends on preceding trend maturity that the detectors ignore — this record inherits that blindness exactly as coded.
- Warmup cost: the first 25 daily bars are flat by record rule, so a triple completing inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`, bar-close decision on completed `1d` bars, next-open market fills, single-asset two-sided flip book) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. PASS means the declared derived strategy is causally expressible under the pinned Hummingbot model — not profitable, not Qlib-paritied, not source-equivalent, not live-tradable.

## Related Wiki records

None.

## Sources

- TA-Lib `ta-lib@v0.8.1`, `src/ta_func/ta_CDL3WHITESOLDIERS.c` — soldiers predicate conjunction, `+100`/`0` outputs, lookback `max(10,10,5,5)+2 = 12`, Morris-vs-Nison note, downtrend-maturity caveat. https://raw.githubusercontent.com/TA-Lib/ta-lib/v0.8.1/src/ta_func/ta_CDL3WHITESOLDIERS.c (fetched live 2026-10-14, 48,126 bytes)
- TA-Lib `ta-lib@v0.8.1`, `src/ta_func/ta_CDL3BLACKCROWS.c` — crows predicate conjunction, `-100`/`0` outputs, lookback `10+3 = 13`, mature-advance caveat. https://raw.githubusercontent.com/TA-Lib/ta-lib/v0.8.1/src/ta_func/ta_CDL3BLACKCROWS.c (fetched live 2026-10-14, 31,800 bytes)
- TA-Lib `ta-lib@v0.8.1`, `src/ta_common/ta_global.c` — `TA_RestoreCandleDefaultSettings` defaults table (BodyShort 10/1.0 RealBody; ShadowVeryShort 10/0.1 HighLow; Near 5/0.2 HighLow; Far 5/0.6 HighLow). https://raw.githubusercontent.com/TA-Lib/ta-lib/v0.8.1/src/ta_common/ta_global.c
- TA-Lib `ta-lib@v0.8.1`, `src/ta_func/ta_utility.h` — `TA_REALBODY`/`TA_UPPERSHADOW`/`TA_LOWERSHADOW`/`TA_HIGHLOWRANGE`/`TA_CANDLERANGE`/`TA_CANDLEAVERAGE` definitions and the exclude-current-candle averaging construction. https://raw.githubusercontent.com/TA-Lib/ta-lib/v0.8.1/src/ta_func/ta_utility.h
- TA-Lib release pin `v0.8.1` (latest release at fetch time, resolved via GitHub releases API 2026-10-14). https://github.com/TA-Lib/ta-lib/releases/tag/v0.8.1
