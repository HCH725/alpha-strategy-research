---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: R-Breaker 7-level breakout-reversal flip two-sided on BTCUSDT 1h bars
created: 2026-10-14
updated: 2026-10-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2020-06-02
sources:
  - https://fmz.com/digest-topic/5707
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# R-Breaker 7-level breakout-reversal flip two-sided on BTCUSDT 1h bars

## Provenance

Primary source read end to end (FMZ digest page fetched over HTTPS during this cycle, 654423-byte landing HTML):

- Canonical page: https://fmz.com/digest-topic/5707 (page title `Commodity Futures R-Breaker Strategy | FMZ`, `Created 2020-06-02 08:57:10`, `Updated 2025-01-14 20:39:56` — Created adopted as `source_as_of`).
- Attribution as printed: developed by Richard Saidenberg, published 1994. The page carries one un-tabled magazine-ranking lineage sentence (no table, figure, metric, sample, backtest report, Sharpe, annualized return, win rate, or trade count anywhere on the page — census over the fetched HTML: `Sharpe` 0, `win rate` 0, annualized/胜率/收益率/回报 0; the `profit` hits are prose adjectives (`large profits`, `take profit`) and the code's `Profit` position-field reads). This record claims no source-reported performance and no reproduced performance.
- Pinned rule artifact = the article's prose formulas (seven level equations) plus its executable JS backtest block: the `backtest` header (`start: 2019-01-01 00:00:00`, `end: 2020-01-01 00:00:00`, `period: 5m`, `exchanges: [{"eid":"Futures_CTP","currency":"FUTURES"}]`), `bars_arr = exchange.GetRecords(PERIOD_D1)` with a `len(bars_arr) < 2` guard, the `bars_arr[-2]` prior-day `Open`/`High`/`Low`/`Close` reads (`yesterday_open` is read but never referenced by any order-gating line — dead read, fenced here), the seven level assignments, the developing-day `today_high`/`today_low` reads off `bars_arr[-1]`, tick-`current_price` comparisons with strict `>`/`<` edges, one-lot `Buy`/`Sell` legs, and the `Sleep(1000)` polling loop. Single-line declarations quoted for gate evidence: `pivot = (yesterday_high + yesterday_close + yesterday_low) / 3`, `r1 = 2 * pivot - yesterday_low`, `r2 = pivot + (yesterday_high - yesterday_low)`, `r3 = yesterday_high + 2 * (pivot - yesterday_low)`, `s1 = 2 * pivot - yesterday_high`, `s2 = pivot - (yesterday_high - yesterday_low)`, `s3 = yesterday_low - 2 * (yesterday_high - pivot)`; flat legs `if current_price > r3` buy / `if current_price < s3` sell; holding-long leg `if today_high > r2 and current_price < r1 or current_price < s3` close-long-then-open-short; holding-short leg `if today_low < s2 and current_price > s1 or current_price > r3` close-short-then-open-long.
- Prose-vs-code r3 disclosure (fenced, not hidden): the prose equation prints `yesterday's highest price + 2 * (center price - yesterday's lowest price) / 2` (which would halve the extension arm), while the article's own executable block prints `r3 = yesterday_high + 2 * (pivot - yesterday_low)` with no divisor. Four independent public reconstructions agree with the code form (the FMZ sibling article's code `Senter=High+2*(Pivot-Low)`, the mathquant.net code dump, the financeppl derivation, the deepwiki formula table). This record pins the code form and never claims the prose form.
- Sibling link printed on the page (not fetched, not a rule source here): `https://www.fmz.com/strategy/187009` (`Copy complete strategy`).
- Author-confirmed demo boundary (Summary section): the article strategy is `only for demonstration, without optimizing the appropriate parameters and varieties`, and `the complete strategy must also include the stop loss function` — i.e. the pinned artifact ships no stop, no target, no trailing, and no time leg. Those absences are source-coded posture, never researcher invention.
- Licence and rights: the canonical page is a public FMZ digest publication with no licence header in the artifact. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) research market/timeframe BTCUSDT `1h` single-frame (the source trades CTP commodity-futures varieties on `5m` decisions over `PERIOD_D1` rails — the daily-rail basis is preserved as prior-UTC-day H/L/C, the `5m`/tick timing is superseded); (2) completed-bar evaluation with same-bar-close fills (the source reads the forming day's developing high/low plus tick `current_price` with `+1`/`-1` slip legs — this record latches on completed-bar highs/lows and decides/fills at the completed-bar close; no maker-touch, queue, or intrabar-path-dependent fill is claimed); (3) an adopted 48-bar warmup with pre-warmup bars flat by record rule (the source guards only `len(bars) < 2` — see Required data for the 2×-structural-need rationale); (4) house sizing/capital/costs replacing the one-lot `Buy/Sell(..., 1)` placeholder (the single-unit, never-add posture is preserved as the no-pyramiding rule); (5) UTC-day session mapping for the 24/7 crypto market (the source assumes day-session commodity trading; positions persist across UTC midnight with recomputed levels — no end-of-day flat is invented, and the developing-day high/low is defined over completed bars of the current UTC day). The seven code-form level equations, the strict comparison edges, the flip-only book (including stop-legs that flip rather than flatten), two-sided direction, the pre-first-signal flat state, and every no-stop/no-target/no-trailing exclusion are source-native and unmodified.

Pre-write dedup (2026-10-14): working-tree case-insensitive searches for `breaker`, `r-breaker`, `rbreaker`, `senter`, `ssetup`, `benter`, `bsetup`, `bboop`, `5707`, and `187009` return zero strategy records using any prior-day-grid breakout-reversal construction. The pool's `pivot-point-breakout-kaufman` record breaks confirmed swing-pivot extremes long-only with no level grid and no reversal leg; the pool's `dual-thrust` record anchors two open-relative rails with a reversal-only book and no observation/reversal ladder; Donchian/Darvas/NR7/Keltner/Turtle records are raw-channel, box, contraction, ATR-envelope, or entry-pyramid constructions. Open `research/*` PRs are only #48 (Larry Williams streak long), #49 (Gaussian StochRSI long), #63 (SuperTrend long), #89 (Chandelier long), #92 (SSL two-sided) — different mechanisms, indicators, and sources. Five-axis distinction: mechanism differs (seven-level prior-day grid with a dual mode — flat-book breakout entries at the outer pair plus holding-book reversal flips at the inner pair, where even the stop legs flip rather than flatten), signal construction differs (strict close-vs-level events gated by a developing-day extreme latch, versus open-anchored rails, confirmed pivots, or raw channels), exits differ (flip-only book with explicitly no stop/target/trailing/time leg — no pool breakout record shares this exact risk posture on this construction), source identity differs (FMZ digest 5707, Jun-2020, versus FMZ strategy pages or TV/GitHub authors), and direction handling differs (two-sided flip system, always-in-market after the first signal with an explicit pre-first-signal flat state).

## Economic mechanism

### Source-reported

Prior-day-range grid trading (mirror title `Commodity Futures R-Breaker Strategy`): seven lines are drawn once a day from yesterday's high/low/close; a flat book chases fresh extremes through the outer pair (trend mode — breakout entries), while a held book reverses through the inner pair once the developing day's extreme has probed the observation line and price falls back (reversal mode — failed-extension flips); support and resistance roles swap on penetration. The article claims the blend harvests both trend alpha and reversal alpha in one session (page prose; no number attached).

### Research interpretation

Ladder-gated dual-mode speculation on a single 24/7 instrument. Unlike the pool's Dual Thrust record (which buys distance from the current bar's open and reverses on any contra cross), this system buys distance from yesterday's auction: nothing fires until price leaves the entire prior-day value area plus an extension arm, so slow grinds inside yesterday's range are ignored no matter how persistent, while a single range-expansion day fires immediately. Unlike Donchian/Turtle breakouts (one level, hold-or-stop), the inner ladder turns failed extensions into contra entries automatically — the system never holds a breakout that round-trips; it joins the round-trip. Unlike oscillator-cross systems it reads no normalized momentum at all — only raw prior-day geometry plus the developing day's extreme. The bet is on day-scale expansion/rejection persistence of the prior auction's extremes, not on any moving average, band, calendar effect, or volume flow. The observation latch (r2/s2 probe before the inner flip) is a noise filter bought with missed V-reversals that never probe far enough; the flip-instead-of-stop posture is bought with whipsaw in chop (see Negative evidence).

## Signal

Exact rule as pinned (seven code-form equations, strict edges — any other value or form is a different, unpinned rule):

- Day frame: UTC day `D`. Levels for `D` are computed from the 24 completed `1h` bars of `D-1`: `H[D]` = highest high, `L[D]` = lowest low, `C[D]` = last close of `D-1`.
- `P = (H+L+C)/3`; `r3 = H + 2*(P-L)` (breakout-buy); `r2 = P + (H-L)` (observe-sell); `r1 = 2*P - L` (reverse-sell); `s1 = 2*P - H` (reverse-buy); `s2 = P - (H-L)` (observe-buy); `s3 = L - 2*(H-P)` (breakout-sell). Ladder invariant: `r3 >= r2 >= r1 >= P >= s1 >= s2 >= s3` always, because each step down differs by `P-L >= 0` or `H-P >= 0` (both hold since `L <= C <= H`); strict unless the degenerate `H = L` day, when all seven collapse to one price.
- Developing-day extremes on each completed `1h` bar `t` of day `D(t)`: `hiD[t]` = highest high over completed bars of `D(t)` up to and including `t`; `loD[t]` = lowest low likewise. Latches reset at every UTC-day boundary.
- Flat-book entries (breakout mode, evaluated at the completed-bar close): `close[t] > r3` → open long at `close[t]`; `close[t] < s3` → open short at `close[t]`. Mutually exclusive by construction (`r3 - s3 = 3*(H-L) >= 0`, so no close can satisfy both; on a degenerate day both equal the single level and a close exactly at it fires nothing).
- Long-held flips (one net fill step at `close[t]` — close the full long and open the full short at the same single close price): `((hiD[t] > r2) and (close[t] < r1)) or (close[t] < s3)` → flip to short. Single outcome whichever OR-leg fires, so no same-bar ordering ambiguity exists (this mirrors the coded `and`/`or` precedence exactly).
- Short-held flips (mirror): `((loD[t] < s2) and (close[t] > s1)) or (close[t] > r3)` → flip to long at `close[t]`.
- Same-bar latch-plus-trigger is declared legal and deterministic: bar `t`'s own high may both set the latch (`high[t] > r2`) and arm the trigger (`close[t] < r1`) — evaluation order is latch-on-high first, trigger-on-close second, one outcome.
- No adds, no partials, no same-side refire (a held long ignores `close > r3`; the single-unit rule is the ported one-lot posture). Flat before the first signal by construction; always-in-market after it (the flip-only book has no flat leg).
- Direction: two-sided flip system. Risk legs (pinned absences, author-confirmed): no stop-loss, no take-profit, no trailing, no time exit — the sole position-changing paths are breakout entries from flat and contra flips while held, exactly as coded.

## Required data

- Completed `1h` bars of BTCUSDT: `close` (comparisons, decisions, fills), `high`/`low` (prior-day `H`/`L` extremes and the developing-day `hiD`/`loD` latches), prior-day last `close` (`C`). No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h` (declared research frame per the derivation; the source's `5m`/tick timing is superseded — the derived strategy is single-frame by construction, with daily levels arithmetically derived from 24 hourly bars, so no second subscription exists).
- Warmup: the structural need is one full prior UTC day (24 completed bars) before levels exist. The adopted warmup is the first 48 completed `1h` bars flat by record rule (predeclared researcher choice — 2× the structural need, guaranteeing one complete prior UTC day whatever the history-start alignment). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar; levels never read the forming day.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (declared port; the source venue `Futures_CTP` commodity futures is a different venue family — no cross-venue equivalence is claimed beyond OHLC arithmetic).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution for entries and flips, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is `5m`-decision/tick-execution on FMZ with `+1`/`-1` slip legs (no execution-timing override ships anywhere portable); this record does not claim source fills. No maker-touch, queue, or intrabar-path-dependent fill: with one decision price per bar and a single flip outcome per bar, there is no same-bar entry ordering ambiguity.
- Sizing/capital/costs: the one-lot `Buy/Sell(..., 1)` legs ship no portable economics — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) replace them here, never presented as source-native behavior.
- Concurrency: at most one single-unit position (long or short) at any time after the first signal; every position-changing event flips in full in one step; no cooldown specified — explicitly none, not invented. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

The page ships the full construction (seven prose equations, seven matching code assignments modulo the fenced prose-r3 divisor slip, the `PERIOD_D1`/`bars_arr[-2]` rail basis, the developing-day high/low reads, the strict flat-book legs, the latch-gated flip legs with stop-legs that flip, the one-lot sizing, the Sep-2019→Jan-2020 `5m` CTP backtest header, the title/Created/Updated stamps, and the sibling-strategy link). It ships zero performance numbers: no return, no Sharpe, no win rate, no profit factor, no trade count, no tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Prose/code r3 split, admitted plainly: the prose `/ 2` form would place breakout entries much closer (at `H + (P-L)`); this record pins the code form `H + 2*(P-L)` with four-way corroboration and disclaims the prose form. Adopting the prose form would be a different, unpinned rule — none is admitted here.
2. No risk layer of any kind, admitted plainly (author-confirmed demo posture): a trend that grinds against the position without ever printing a flip condition is held in full, and a vertical adverse move on the entry bar itself has no guardrail. Adding any stop would be a different, unpinned rule — none is admitted here.
3. Outer-pair whipsaw, admitted plainly: chop oscillating across `r3`/`s3` flips the full unit bar after bar (breakout entries from each flat moment, immediate flips on rejection), with no stop, target, or cooldown to dampen it. Widening any arm would be a different, unpinned rule — none is admitted here.
4. Degenerate-day collapse, admitted plainly: a zero-range prior day (`H = L`, hence `C = H`) collapses all seven levels to one price, degrading the system to a pure close-vs-level cross for that day. Structural, disclosed, and unencounterable on `1h` BTCUSDT outside a venue outage.
5. Stop-legs flip, admitted plainly: the `close < s3` long-leg and `close > r3` short-leg open contra positions rather than flattening, so after the first signal the book is never flat by rule — adverse drift between flips and multi-day Eiichiro-style give-back are the coded trade, disclosed, not smoothed.
6. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1h` single research frame (superseding `5m`/tick CTP timing), completed-bar latch evaluation with same-bar-close fills, the adopted 48-bar warmup with record-rule pre-warmup flat, house sizing/costs, and the UTC-day session mapping — all predeclared above; the seven code-form equations, strict edges, latch-plus-flip logic, flip-only book, two-sided direction, pre-first-signal flat state, and every no-stop/no-target/no-trailing exclusion are source-native. This record is therefore never evidence that the original CTP deployment passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: seven code-form equations / strict edges / latch-plus-flip logic / flip-only book / two-sided / `1h` BTCUSDT / same-bar-close fills / 48-bar warmup are frozen.

- F1 — Grid relevance: replacing the seven-level grid with raw prior-day extremes (long on close above prior-day high, short on close below prior-day low, same flip-only book, same frame/fills) must not improve net expectancy; fail ⇒ the extension arms plus observation ladder add nothing over a plain prior-day breakout.
- F2 — Flip relevance: replacing the always-in-market flip book with a flat-after-close book (each flip leg closes to flat instead of opening the contra unit, re-entering only on the next same-direction event) must not improve net expectancy; fail ⇒ staying perpetually exposed through flips adds nothing over breakout-and-hold episodes.
- F3 — Observation-latch relevance: dropping the developing-day latch (long flips on `close < r1` alone, short flips on `close > s1` alone, stop-flips unchanged) must not improve net expectancy; fail ⇒ the probe-before-flip filter adds nothing over bare inner-level crosses.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (declared port of a CTP-commodity source context). The OHLC arithmetic ports across perpetual venues without structural change; the 24/7 market needs no session approximation beyond the UTC-day mapping, which is fully specified above. Both sides are explicit legs, so a spot-only deployment expresses the long half only while every flip-to-short stays venue-gated (short permission unused, never silently converted) — a spot-only variant would be a different, unpinned claim. No funding-dependent leg, no stablecoin-specific assumption, no cross-venue state. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived frame and fill timing: the source decides on `5m`/tick CTP flow with `+1`/`-1` slip legs; this record decides on completed `1h` bars with same-bar-close fills. Backtest economics of the two framings, timings, and venues differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source configuration's performance.
- No source cost declaration beyond one-lot legs: no fee, slippage, or funding assumption ships anywhere usable — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Always-in-market exposure: after the first signal the book is never flat by rule, so adverse drift between flips is held in full — long unhedged stretches are the coded trade, disclosed, not smoothed.
- Static intraday ladder: levels freeze at the UTC boundary, so a runaway trend day enters once at the outer pair and never adds (no pyramiding by construction) — capped winners on trend days are the coded trade, disclosed, not smoothed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical digest page (Created 2020-06-02 08:57:10; Updated 2025-01-14 20:39:56): https://fmz.com/digest-topic/5707
