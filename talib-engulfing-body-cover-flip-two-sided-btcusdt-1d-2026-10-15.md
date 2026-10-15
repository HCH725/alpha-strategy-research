---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TA-Lib engulfing body-cover flip two-sided on BTCUSDT 1d bars
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
  - https://raw.githubusercontent.com/TA-Lib/ta-lib/v0.8.1/src/ta_func/ta_CDLENGULFING.c
  - https://github.com/TA-Lib/ta-lib/releases/tag/v0.8.1
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TA-Lib engulfing body-cover flip two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (one raw file fetched over HTTPS during this cycle from the pinned `v0.8.1` tag of the canonical `TA-Lib/ta-lib` repository, all 508 lines):

- Engulfing artifact: `src/ta_func/ta_CDLENGULFING.c` at tag `v0.8.1` (20,084 bytes as fetched) — batch function `TA_CDLENGULFING`, float twin `TA_S_CDLENGULFING`, lookback `TA_CDLENGULFING_Lookback`, streaming twin `TA_CDLENGULFING_StepImpl`, plus `Open`/`Peek`/`Update` mirrors carrying the identical predicate conjunction (all four firing paths verified token by token).
- Release pin: `https://github.com/TA-Lib/ta-lib/releases/tag/v0.8.1` (tag page re-fetched HTTP 200 during this cycle; the raw file re-fetched HTTP 200 at the same pin). `source_as_of` is the read date of the pinned tag, not a paper date — there is no paper here; the code is the specification. No "latest release" is claimed (the releases API was unreachable from this host during this cycle, so latest-ness is unstated rather than asserted).
- Licence and rights: the file carries the TA-LIB BSD-style header (`Copyright (c) 1999-2026, Mario Fortier` — redistribution in source and binary forms permitted with retained copyright notice). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.
- Change history (verbatim): `102404 AC Creation`; `040309 AC Increased flexibility to allow real bodies matching on one end (Greg Morris - "Candlestick charting explained")` — the 80-output exists because Morris contemplates the one-end-match case.

Pinned rule content (verified line by line, batch/float/streaming/peek agree):

- `Must have` comment (verbatim): `first: black (white) real body`; `second: white (black) real body that engulfs the prior real body`.
- Output comment (verbatim): `outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish`; `100 is returned when the second candle's real body begins before and ends after the first candle's real body`; `80 is returned when the two real bodies match on one end (Greg Morris contemplate this case in his book "Candlestick charting explained")`.
- Trend caveat (verbatim): `The user should consider that an engulfing must appear in a downtrend if bullish or in an uptrend if bearish, while this function does not consider it`.
- Pinned lookback: `TA_CDLENGULFING_Lookback` returns `2` — the first output at index 2 reads bars `0..2`; three completed bars are the full structural need.
- Pinned absence of settings: the file contains zero `TA_SetCandleSettings`, zero `TA_CANDLEAVERAGE`, zero `REALBODY`/`Shadow` tokens anywhere in any firing path. `inHigh[]`/`inLow[]` appear only in function signatures and `NULL` guards — they are never read by any firing predicate. The detector is pure open/close geometry: no trailing average, no configurable tolerance, no shadow test, no volume test, nothing to seed.
- Causality: every firing predicate reads only bars `i-1` and `i`; no average, no shift, no future reference, no repainting. Outputs depend only on closed bars `≤ i`.
- Performance census: the pinned file contains no return, Sharpe, win-rate, profit-factor, trade-count, or backtest figure of any kind — TA-Lib ships pattern detectors, not systems. This record claims no source-reported performance and no reproduced performance.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — TA-Lib's symmetric two-bar engulfing detector wired into a two-sided flip book on one crypto asset — not a lossless reproduction of anything TA-Lib deploys (TA-Lib deploys nothing; it detects). Researcher-declared adaptations are exactly six: (1) research market/timeframe BTCUSDT `1d` single-frame (the code is timeframe-agnostic array logic — the daily grid is the declared deployment, never implied); (2) bar-close decision with next-bar-open market fills (the code outputs at the close of bar `i`; it ships no fill convention, so the sequential next-open fill is declared, never implied); (3) an adopted 5-bar warmup with pre-warmup bars flat by record rule (the code's structural need is 3 bars — lookback 2 with zero averages to seed — see Required data for the rationale); (4) house sizing/capital/costs replacing the code's complete absence of economics (the single-unit, never-add posture is the declared port of having exactly one output leg per bar); (5) the flip-only book with researcher-declared no-stop/no-target/no-trailing/no-time-exit posture (TA-Lib ships detections, never position management — the sole position-changing paths are contra-pattern flips, predeclared here); (6) two-sided direction mapping with the short leg explicit (positive outputs target long, negative outputs target short — the code's own signed output polarity; `80` and `100` magnitudes fire identically with no strength gate, predeclared here). The predicate conjunctions, strict/weak edges, 100/80 distinction, lookback, causal two-bar reads, unused-high/low construction, pre-first-signal flat state, and every exclusion are source-native and unmodified.

Pre-write dedup (2026-10-15): working-tree filename searches for `engulf` return exactly one record (`dual-ema-engulfing-volume-long-btcusdt-1h-2026-10-07.md`); content searches for `CDLENGULFING` return zero records; filename searches for `harami`, `morning-star`, `doji` return zero records. Content-level `ta-lib`/`talib` prose hits are only the soldiers record below, the TD-sequential dead-import quarantines (pure pandas run-counting, zero `ta.` call sites), and a prose mention inside the three-line-break dedup paragraph (whose signal is close-only line-run construction, never a candle function). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI breakout long), #63 (SuperTrend ATR-flip long), #89 (Chandelier Exit stop-flip long), #92 (SSL channel reversal two-sided) — different mechanisms, indicators, and sources. Closed NOT_LOSSLESS precedents (#6 WaveTrend, #10 golden-cross, #17 MACD-hist, #20 Ichimoku-RSI) contain no engulfing system. Closest pool records differ on every axis: `dual-ema-engulfing-volume-long-btcusdt-1h-2026-10-07.md` is a four-gate long-only conjunction (dual-EMA regime AND engulfing geometry AND body-ratio AND 1.2x volume) on `1h` FMZ Pine v6 with same-bar-close fills and a regime-flip-or-bearish exit to flat; `three-white-soldiers-black-crows-flip-two-sided-btcusdt-1d-2026-10-14.md` fires on three-candle body/open/shadow predicates against four trailing default averages (lookbacks 12/13, shadow-gated, advance-block filter). Five-axis distinction: mechanism differs (symmetric two-bar body-cover reversal flip — either leg fires only against the opposite color — versus trend-gated conjunction entry and versus three-candle with-trend continuation); signal construction differs (six open/close comparisons over two bars with zero averages, zero settings, zero volume, zero shadows, versus EMA/volume/body-ratio gates and versus averaged shadow/body predicates); exits differ (contra-fire flip-only always-in-market book versus exit-to-flat legs); source identity differs (TA-Lib `v0.8.1` immutable C detector versus FMZ 434564 Pine); frame/fills differ (`1d` next-open two-sided versus `1h` same-close long-only).

## Economic mechanism

### Source-reported

Two-bar real-body cover with Morris one-end-match tolerance: a white body that covers the prior black body (strict extension on at least one end) prints bullish; a black body that covers the prior white body prints bearish. Full strict cover scores `100`; exact match on exactly one end scores `80`; an exact both-ends body swap scores `0` (proven from the disjuncts, never assumed). The code's own comments frame positive outputs as bullish and negative as bearish, while warning that a bullish engulfing properly belongs in a downtrend and a bearish one in an uptrend — a conditioning `this function does not consider`.

### Research interpretation

Two-candle reversal speculation on a single 24/7 instrument, both sides coded, with no regime, volume, shadow, or trend-maturity filter of any kind. Unlike the pool's dual-EMA engulfing long (which buys only expansion bars inside coded uptrends and rests flat otherwise), this system trades every detector fire including mid-trend covers — entries ride immediate two-bar rejection rather than filtered persistence, and the book never rests flat after the first signal. Unlike the soldiers/crows continuation flip it reads no trailing average at all — tolerances are absolute price comparisons, not volatility-scaled, so the identical bar pair fires identically in compressed and expanded tapes. Unlike channel breakouts the trigger is body-geometry-shaped rather than level-shaped. The bet is that TA-Lib-exact two-bar body cover on daily BTCUSDT carries reversal information net of the declared costs — with the source's own trend-maturity caveat deliberately left unmodeled and fenced (see Negative evidence 1).

## Signal

Exact rule as pinned (strict/weak edges as coded — any other tolerance, gate, or form is a different, unpinned rule):

- Notation: bars indexed `i`; `O/H/L/C` = open/high/low/close. Color edges (pinned): white `W[j] := C[j] >= O[j]` (a doji counts white); black `B[j] := C[j] < O[j]` (strict — a doji is never black).
- Bullish fire `E bull[i]` (code output `+100` or `+80`) iff ALL of (bars `i-1..i`):
  - B1 colors: `B[i-1]` and `W[i]` (black engulfed by white);
  - B2 cover (at least one strict end — pinned disjunction): `(C[i] >= O[i-1] && O[i] < C[i-1]) || (C[i] > O[i-1] && O[i] <= C[i-1])`;
  - magnitude: `+100` iff `O[i] != C[i-1] && C[i] != O[i-1]` (strict both ends); `+80` iff exactly one end matches (Morris case); both ends exactly swapped is `0`, never a fire (the disjunction excludes `C[i]==O[i-1] && O[i]==C[i-1]`).
- Bearish fire `E bear[i]` (code output `-100` or `-80`) iff ALL of (bars `i-1..i`):
  - C1 colors: `W[i-1]` and `B[i]` (white engulfed by black — a doji prior counts white, disclosed asymmetry);
  - C2 cover: `(O[i] >= C[i-1] && C[i] < O[i-1]) || (O[i] > C[i-1] && C[i] <= O[i-1])`;
  - magnitude: `-100` iff `O[i] != C[i-1] && C[i] != O[i-1]`; `-80` iff exactly one end matches; exact both-ends swap is `0`.
- Both magnitudes fire identically here (no strength gate — predeclared researcher mapping; the `80`/`100` distinction is reported, never traded on).
- Evaluated at the close of completed bar `i`; needs bars back to `i-2` structurally (lookback 2, zero seeding).
- Position target (pinned flip book): at the close of each completed bar `i` (post-warmup), the target for the next bar is long iff a bullish fire printed, short iff a bearish fire printed, else unchanged (hold current side; flat only before the first-ever fire). Orders fire for the next bar's open: flat→long buys at next open on bullish; flat→short sells at next open on bearish; long-held + bearish flips full long to full short in one step at next open; short-held + bullish flips full short to full long in one step at next open. Same-side refire is ignored (single-unit, no adds — declared port of one-output-per-bar). At most one order event per bar boundary; no intrabar evaluation, no intrabar orders, no partials.
- Mutual exclusion (proven, not assumed): bullish requires `W[i]`; bearish requires `B[i]` (`C[i] < O[i]`). No bar satisfies both, so both legs can never fire on the same close and no priority ruling is owed.
- Degenerate tape (proven, not assumed): any fire needs a strictly-black bar (bullish: the prior; bearish: the current), and a bullish fire with a doji current bar is algebraically impossible (both disjuncts contradict `O[i]==C[i]` against a strictly-black prior). A fully flat/doji history can therefore never print a first signal; the flat-until-first-fire state needs no extra guard. A doji may serve as the white prior of a bearish fire (pinned `>=` edge, disclosed, never smoothed).
- Risk legs (declared researcher posture, TA-Lib ships no position management): no stop-loss, no take-profit, no trailing, no time exit — the sole position-changing paths are contra-pattern flips. A vertical adverse move on/after the entry bar is held in full until the opposite cover prints. This is the coded trade, disclosed, not a tunable parameter here.
- Direction: two-sided flip system, always-in-market after the first signal, flat before it by construction.

## Required data

- Completed `1d` bars of BTCUSDT only: `open` and `close` gate every order (cover comparisons, color edges, 100/80 magnitude). `high`/`low` are accepted by the venue feed but never read by any firing predicate (signature/NULL-guard presence only, verified) — no shadow, range, or wick value influences any signal. No `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: daily bars. One evaluation per bar at its close; fills land on the next daily bar's open. All inputs are completed-bar values — no provisional intrabar value is ever used; there is no average to seed and no shift anywhere.
- Warmup: the structural need is 3 completed bars (lookback 2, first output index 2). The adopted warmup is the first 5 completed `1d` bars flat by record rule (predeclared researcher choice — covers the structural need with margin although no average exists to seed). No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port; TA-Lib is venue-agnostic array logic — no cross-venue equivalence is claimed beyond open/close arithmetic).
- Order timing (predeclared derivation; the code outputs at bar close and ships no fill convention): completed-bar-close decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per bar boundary and mutual exclusion is proven, so there is no same-bar dual-fire to sequence; each flip is one net fill step at a single open price.
- Cash leg: flat earns nothing by record rule (flat exists only before the first signal). No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted.
- Sizing/capital/costs: the code ships no portable economics — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3×/5×) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — long bars carry realized funding, short bars carry realized funding, pre-first-signal flat bars carry none) replace them here, never presented as source-native behavior. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one single-unit position (long or short) at any time after the first signal; every position-changing event flips in full in one step; no cooldown specified — explicitly none, not invented (re-entry requires the opposite cover, so a cooldown would only delay coded flips). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue. Safety orders: explicitly none.

## Evidence

### Source-reported

The pinned file ships the full construction (two-sided color edges with the doji-counts-white `>=` asymmetry, both cover disjunctions with strict/weak ends, the 100/80 magnitude rule with the Morris one-end-match note and its 040309 change-history entry, the lookback-2 function, the four agreeing code variants, the high/low-accepted-but-unread construction, the `+100/+80/0/-80/-100` output scheme, and the trend-maturity caveat). It ships zero performance numbers of any kind — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Trend-maturity caveat left unmodeled, quoted plainly: bullish belongs in a downtrend and bearish in an uptrend, while the detector `does not consider it`. This record wires the raw detector outputs with no regime filter of any kind — mid-trend covers fire exactly like mature ones by construction. Adding any trend gate would be a different, unpinned rule — none is admitted here.
2. No risk layer of any kind, admitted plainly (researcher-declared posture, not source behavior): the flip-only book holds every adverse excursion until the opposite cover prints, and a vertical move on the entry bar itself has no guardrail. Adding any stop would be a different, unpinned rule — none is admitted here.
3. Chop whipsaw, admitted plainly: alternating covers in a range flip the full unit back and forth with no stop, target, or cooldown to dampen it; two-bar structure alternates faster than any three-candle system. Adding any confirmation bar would be a different, unpinned rule — none is admitted here.
4. Absolute (unscaled) geometry, admitted plainly: with zero trailing averages, the identical bar pair fires identically in compressed and expanded volatility — a 1-tick cover counts exactly like a 10% cover. Normalizing against ATR or range would be a different, unpinned rule — none is admitted here.
5. Doji asymmetry, admitted plainly: a doji counts white, so it can serve as the engulfed white prior of a bearish fire but can never be the black leg of either fire, and a bullish fire can never print on a doji current bar (proven). Harmonizing the edges would be a different, unpinned rule — the code's edges are inherited exactly.
6. 80-fires trade equal, admitted plainly: Morris one-end-match covers (`80`) open and flip the full unit exactly like strict covers (`100`). Strength-gating to `100`-only would be a different, unpinned rule — none is admitted here.
7. Warmup cost, admitted plainly: the first 5 daily bars are flat by record rule, so any cover completing inside warmup is deliberately untraded — pinned, not recovered.
8. Close-to-open seams, admitted plainly: every entry and flip fills at the next bar's open — gap-through moves across signal edges are taken at post-move opens, never at the signal close.
9. Derivation boundary fenced: the only non-code behaviors in this record are the BTCUSDT-`1d` deployment frame, next-open fills, the adopted 5-bar warmup with record-rule pre-warmup flat, house sizing/costs, the flip-only risk posture, and the 80-equals-100 fire mapping — all predeclared above; both predicate conjunctions, color edges, cover disjunctions, magnitude rule, lookback, causal two-bar reads, high/low-unread construction, signed output polarity, pre-first-signal flat state, and every exclusion are source-native. This record is therefore never evidence that any TA-Lib deployment passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: both pinned cover conjunctions / strict-weak edges / 100-80 mapping / lookback 2 / flip-only book / two-sided / `1d` BTCUSDT / next-open fills / 5-bar warmup are frozen.

- F1 — Morris relevance: a strict-only twin (fires on `100` only, `80` covers ignored, same book/frame/fills) must not improve net expectancy; fail ⇒ the one-end-match tolerance adds nothing over strict covers.
- F2 — Flip relevance: a flat-book twin (each contra cover exits to flat instead of opening the contra unit, re-entering only on the next same-direction cover, same frame/fills) must not improve net expectancy; fail ⇒ staying perpetually exposed through flips adds nothing over cover-and-hold episodes.
- F3 — Geometry relevance: a bare-color twin (long-target on white-after-black two-bar color flip, short-target on black-after-white, no cover comparisons, same book/frame/fills) must not improve net expectancy; fail ⇒ the body-cover comparisons add nothing over naked two-bar color alternation.
- F4 — Selectivity relevance: buy-and-hold over the same sample must not improve net expectancy; fail ⇒ sitting out non-cover stretches costs more in missed drift than it saves in avoided exposure.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` bar closes; fills at next-bar opens; no venue-specific read). The open/close arithmetic ports across perpetual venues without structural change; the 24/7 market needs no session approximation (covers read bar geometry only, never wall-clock sessions). Both sides are explicit legs, so a spot-only deployment expresses the long half only while every flip-to-short stays venue-gated (short permission unused, never silently converted) — a spot-only variant would be a different, unpinned claim. No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no shadow-dependent leg, no session template, no cross-venue state. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived frame and fill timing: the code outputs at bar close over abstract arrays with no market, venue, or fill convention; this record decides on completed `1d` bars with next-open fills. Backtest economics of other framings or timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about any other configuration.
- No source cost declaration of any kind: no fee, slippage, or funding assumption ships anywhere usable — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Always-in-market exposure: after the first signal the book is never flat by rule, so adverse drift between contra covers is held in full — long unhedged stretches are the coded trade, disclosed, not smoothed.
- Absolute geometry: with no trailing average anywhere, fixed tick-level covers and range-expansion covers are treated identically — regime shifts in volatility change the economic meaning of a fire without changing its detection, disclosed, not adapted.
- Unmodeled trend context: per the code's own caveat, cover significance depends on preceding trend maturity that the detector ignores — this record inherits that blindness exactly as coded.
- Warmup cost: the first 5 daily bars are flat by record rule, so a cover completing inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`, bar-close decision on completed `1d` bars, next-open market fills, single-asset two-sided flip book) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. PASS means the declared derived strategy is causally expressible under the pinned Hummingbot model — not profitable, not Qlib-paritied, not source-equivalent, not live-tradable.

## Related Wiki records

None.

## Sources

- TA-Lib `ta-lib@v0.8.1`, `src/ta_func/ta_CDLENGULFING.c` — two-sided color edges, both cover disjunctions, 100/80 magnitude rule, lookback `2`, Morris one-end-match note with 040309 history, trend-maturity caveat, zero settings/averages. https://raw.githubusercontent.com/TA-Lib/ta-lib/v0.8.1/src/ta_func/ta_CDLENGULFING.c (fetched live 2026-10-15, 20,084 bytes, tag page HTTP 200)
- TA-Lib release pin `v0.8.1`. https://github.com/TA-Lib/ta-lib/releases/tag/v0.8.1
