---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Wilder Volatility System SIC stop-and-reverse flip two-sided on BTCUSDT 1d bars
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
  - https://www.incrediblecharts.com/indicators/volatility_stops.php
  - https://download.esignal.com/products/workstation/help/charts/studies/wilders_volatility.htm
  - https://news.cqg.com/blogs/coding/2019/06/volatility-stop-and-volatility-system
  - https://www.lizardindicators.com/volatility-stop/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Wilder Volatility System SIC stop-and-reverse flip two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read end to end (all four fetched live over HTTPS as HTML during this cycle):

- Exit/SAR artifact: Incredible Charts (Colin Twiggs), `Volatility Stops` (`.../indicators/volatility_stops.php`, 30,084 bytes HTML as fetched) — Wilder's 7-day ATR / 3.0-multiple setup, Significant Close doctrine, close-based stop-and-reverse feature, day-7/day-8 seeding cadence, exit-signal wiring, trend-filter entry example, and the two stated weaknesses, all quoted verbatim below.
- Deterministic-spec artifact: eSignal workstation help, `Wilder's Volatility` (`.../wilders_volatility.htm`, 13,028 bytes HTML as fetched) — True Range definition, ATR(n), ARC constant band with Workstation default, initial-position rule with worked 7-day arithmetic, initial SIC/SAR construction, the complete four-branch subsequent state machine, period default, literature pointer to Wilder (1978), and the non-signal framing caveat, all quoted verbatim below (two comparison glyphs dropped by the page's own markup are recovered in place and flagged).
- Paradigm artifact: CQG official blog, `Volatility Stop and Volatility System` (Helmut Mueller, 2019-06-18, 36,687 bytes HTML as fetched) — VolSys as Wilder's trend-following stop-and-reverse system over a smoothed range average anchored to extreme closes, quoted verbatim below.
- Corroboration artifact: Lizard Indicators, `The Wilder Volatility Stop` (161,702 bytes HTML as fetched) — default 3× ATR over a 7-bar lookback plus Wilder's own SIC phrasing, quoted verbatim below.

Pinned rule content (all four rule sources agree on construction; verbatim quotes):

- Wilder setup (verbatim, Incredible): `Welles Wilder used 7-day Average True Range and a multiple of 3.` / `Welles Wilder's system uses Closing Price and incorporates a stop-and-reverse feature (as with his Parabolic SAR).`
- Significant Close (verbatim, Incredible): `the highest close reached in an up-trend or the lowest close in a down-trend` / (verbatim, Lizard, Wilder's own phrasing): `the extreme favorable close price reached while in a trade`.
- Seeding cadence (verbatim, Incredible): `The first stop is calculated in day 7 and plotted for day 8` / `If an up-trend, the first stop is SIC - 3 * ATR, otherwise SIC + 3 * ATR for a down-trend` / `Repeat each day until price closes below the stop (or above in a down-trend)` / `Set SIC equal to the latest Close, reverse the trend and continue.`
- True Range (verbatim, eSignal): `defined as the highest difference in value among today's daily high minus today's daily low; today's daily high minus yesterday's closing price; and today's low minus yesterday's closing price.`
- ARC band (verbatim, eSignal): `ARC t = ATR t * k` / `where constant (k) is between 2.8 and 3.1 (Workstation uses a default of 3.0)`.
- Initial position (verbatim, eSignal): `Determine if initial-position (chronologically) is long or short. FutureSource assumes a short position if the close prior to the initial-position is less than the chronological-first close.` / `in a 7-Day calculation: if Day_8_Close < Day_1_Close, then position for Day 9 is short.` / `Day_8_Close (vs. day 7) is used because True Range cannot be calculated until day 2, therefore ATR [based on TR] cannot be calculated until day 8 and the current position is dependent on the prior day's values.` The complementary Long branch glyph was dropped by the page markup (`Pi = Long if C(t-1) [glyph] C((t-n)-1)`); the complement (`>=`) is the only consistent reading and is pinned as such below, flagged.
- Initial SIC/SAR (verbatim, eSignal): `Determine Initial Significant Close - based on all prior closes (i.e. in a 7-Day calculation, the MIN or MAX of Day_1_Close through Day_8_Close to determine the SIC for Day-9)` / `If Pi = Short, then SICi = MIN(...)` / `If Pi = Long, then SICi = MAX(...)` / `If Pi = Long, then SICi - ARC t-1` / `If Pi = Short, then SICi + ARC t-1`.
- Subsequent state machine (verbatim, eSignal; hold-branch glyphs dropped by markup, recovered as complements and flagged): `If P t-1 = Long, and if C t-1 < SAR t-1 then: P t changes to Short; SIC t = C t-1; SAR t = SIC t + ARC t-1` / `If P t-1 = Long, and if C t-1 [>=] SAR t-1 then: P t remains Long; SIC t = MAX(C t-1, C t-2 ... C t-L); SAR t = SIC t - ARC t-1` / `If P t-1 = Short, and if C t-1 > SAR t-1 then: P t changes to Long; SIC t = C t-1; SAR t = SIC t - ARC t-1` / `If P t-1 = Short and If C t-1 [<=] SAR t-1 then: P t remains Short; SIC t = MIN(C t-1, C t-2 ... C t-L); SAR t = SIC t + ARC t-1` (`L = length of current position`).
- Seeding honesty (verbatim, eSignal): `FutureSource's technique differs slightly from Wilder's discussion.` This record ports the FutureSource technique exactly as specified, disclosed, never presented as Wilder's literal text.
- Period default (verbatim, eSignal): `Period: The number of bars in a chart... Workstation uses a default value of 7.` / (verbatim, Lizard): `By default the indicator applies a ATR multiple of 3 for a 7 bar lookback period.`
- Stop-and-reverse paradigm (verbatim, CQG): `The Volatility System study was developed by J. Welles Wilder Jr.` / `The Volatility System is a trend-following system.` / `The paradigm is a stop and reverse trading system with a smoothed moving average of the ranges of previous bars.` / `This average is added to the lowest close (for a buy stop) or subtracted from the highest close (for a sell stop), which occurred while the stop was active.`
- Non-signal framing (verbatim, eSignal, fenced as disclosed tension): `Wilder's Volatility System alone cannot trigger any trade signals, which means it must be used in conjunction with other indicator systems.` This record trades the SAR reversal book anyway under CQG's stop-and-reverse paradigm — the tension is declared, not hidden (see Negative evidence).
- Entry-filter alternative fenced (verbatim, Incredible): `Signals are used for exits: Exit your long position (sell) when price crosses below the Volatility Stop. Exit your short position (buy) when price crosses above the Volatility Stop.` / `While not conventional, they can also be used to signal entries — in conjunction with a trend filter.` The 63-day-EMA trend-filter entry example on that page is a different, unpinned rule and is not adopted here.
- Whipsaw admission (verbatim, Incredible): `SAR assumes that the trend has changed every time that your stop is hit.` / `Most traders will find that their stops are regularly hit without the trend changing — price merely retraces through your stops and then resumes` / `Stops may move lower during an up-trend if Average True Range widens`.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — Wilder's 7-day / 3.0-multiple SIC-anchored stop-and-reverse state machine wired into a two-sided flip book on one crypto asset — not a lossless reproduction of any source deployment (no source trades BTCUSDT, ships fills, sizing, costs, or a venue). Researcher-declared adaptations are exactly seven: (1) research market/timeframe BTCUSDT `1d` single-frame (all rule sources are venue-agnostic daily-bar price logic — the daily grid is the declared deployment, never implied); (2) constant pinned at the defaults `k = 3.0` (eSignal default, Incredible's Wilder-original, Lizard default — the `[2.8, 3.1]` band is fenced, any other `k` is a different, unpinned rule); (3) Wilder RMA bootstrapped from an SMA of the first seven TRs (the sources pin only `smoothed` averaging — the bootstrap is the canonical Wilder normalization, declared); (4) equality-hold tie closure (`>=` / `<=` hold is the complement of the sources' strict `<` / `>` reversal legs — deterministic closure, flagged, never a third branch); (5) bar-close decision with next-bar-open market fills (strictly conservative sequential port of eSignal's day-indexed positions, never implied); (6) an adopted 30-bar warmup with pre-warmup bars flat by record rule (the structural need is 8 closes — the warmup is the declared margin, see Required data); (7) house sizing/capital/costs replacing the sources' complete absence of economics (the single-unit, never-add posture is the declared port of one-event-per-bar-boundary). The TR definition, SIC doctrine, seeding cadence, initial-position comparison, MIN/MAX seeding, all four SAR branches, the stop-and-reverse book, pre-warmup flat state, and every exclusion are source-normalized. This record is therefore never evidence that any source deployment passes.

Pre-write dedup (2026-10-14): working-tree case-insensitive filename searches for `wilder-volatility`, `volsys`, `volatility-system`, `sic-stop`, `stop-and-reverse` return zero strategy records built on Wilder's Volatility System; working-tree phrase search for `significant close` / `volatility system` / `volsys` / `stop and reverse` returns exactly one file — `bookstaber-atr-momentum-breakout-reversal-btcusdt-1d-2026-10-05.md` — and only inside its own dedup paragraph (prose mention of an FMZ strategy literally named `Volatility System`, a 1-bar close-change vs ATR-multiple breakout with no SIC anchor, no SAR state, and no reversal book). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI breakout long), #63 (SuperTrend ATR-flip long), #89 (Chandelier Exit stop-flip long), #92 (SSL channel reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ on every axis: `psar-flip-stop-reverse-btcusdt-1d-2026-10-09.md` reverses on a time-accelerated parabolic SAR of extreme prices (AF step-up, no ATR, no close anchor, no SIC ratchet); `bookstaber-...` fires on a single-bar close-change exceeding an ATR multiple (stateless breakout, no SIC, no SAR memory); `chande-kroll-stop-...` / `ut-bot-atr-trailing-...` / `nick-rypock-trailing-reverse-...` / open PR #89 anchor stops to range extremes (highest-high / lowest-low) with gates or ratchets that never reference the extreme favorable close. Five-axis distinction: mechanism differs (SIC close-anchored ATR-multiple SAR state machine with four pinned branches, versus parabolic acceleration, versus stateless breakout, versus high/low-anchored trailing stops); signal construction differs (prior close versus prior SAR with SIC ratcheted to the extreme favorable close of the current leg, versus EP-penetration, versus 1-bar change threshold, versus extreme-range penetration); entries differ (only SAR-reversal bars flip the book — SAR approaches that stop short of the line are explicit no-ops); exits differ (the SAR itself is the sole stop, exit, and re-entry — no TP, no trailing leg, no time exit, no cooldown); risk posture differs (always-in-market stop-and-reverse by paradigm, versus gated or trailing-stop books). No duplicate, paraphrase, or trivial parameter variant exists.

## Economic mechanism

### Source-reported

Close-anchored volatility breakout speculation (mirror the source titles): because the stop trails the `extreme favorable close price reached while in a trade` by a smoothed-range multiple, sideways chop inside `3 * ATR` prints no reversal at all, while a close beyond the line forces the full stop-and-reverse — CQG's paradigm in one sentence: `a stop and reverse trading system with a smoothed moving average of the ranges of previous bars` added to `the lowest close` / subtracted from `the highest close ... while the stop was active`. Incredible converts the same line into the exit pair — sell longs crossing below, cover shorts crossing above — and warns the SAR fires on mere retracements too.

### Research interpretation

SIC-ratchet breakout capture on a single 24/7 instrument, both sides coded. Unlike the pool's PSAR flip (whose stop accelerates toward price with each new extreme and eventually forces a flip by time decay alone), this system's stop can only tighten when the close itself prints a new leg extreme, and it actively loosens when ATR widens (`Stops may move lower during an up-trend if Average True Range widens`, inherited undisguised). Unlike the pool's high/low-anchored trailing stops (which key off wicks), this system keys off closes only — a long-leg day with a deep low wick but a firm close never moves the SAR adversely. The bet is that closes clearing a 3-ATR cushion off the leg's best close precede multi-day directional drift often enough to survive the source-admitted retracement whipsaw, with no target, trailing leg, or cooldown to dampen it.

## Signal

Exact rule as pinned (`n = 7`, `k = 3.0`, Wilder TR + Wilder RMA, strict reversal / hold-on-equality — any other period, constant, averaging, anchor, tie rule, filter, or stop is a different, unpinned rule):

- Notation: completed daily bars with high `H[i]` / low `L[i]` / close `C[i]`, 1-based bar index.
- True Range (source verbatim, index form): `TR[i] = max(H[i] − L[i], |H[i] − C[i−1]|, |L[i] − C[i−1]|)` for `i ≥ 2`.
- ATR (Wilder RMA with declared SMA bootstrap): `ATR[8] = mean(TR[2..8])`; `ATR[i] = (ATR[i−1] × 6 + TR[i]) / 7` for `i ≥ 9`. `ARC[i] = 3.0 × ATR[i]`.
- Seeding (eSignal/FutureSource, source-normalized): at the close of bar 8 — `P[9] = Short` iff `C[8] < C[1]`, else Long (complement `>=`, flagged glyph recovery); `SIC[9] = MIN(C[1..8])` if Short else `MAX(C[1..8])`; `SAR[9] = SIC[9] + ARC[8]` if Short else `SIC[9] − ARC[8]`.
- Per subsequent day `t ≥ 10`, evaluated once at the close of bar `t−1` from completed values only:
  - If `P[t−1] == Long` and `C[t−1] < SAR[t−1]` (strict): `P[t] = Short`; `SIC[t] = C[t−1]`; `SAR[t] = SIC[t] + ARC[t−1]`.
  - If `P[t−1] == Long` and `C[t−1] >= SAR[t−1]` (hold, flagged complement): `P[t] = Long`; `SIC[t] = MAX` closes over the current long leg (leg start through `C[t−1]`); `SAR[t] = SIC[t] − ARC[t−1]`.
  - If `P[t−1] == Short` and `C[t−1] > SAR[t−1]` (strict): `P[t] = Long`; `SIC[t] = C[t−1]`; `SAR[t] = SIC[t] − ARC[t−1]`.
  - If `P[t−1] == Short` and `C[t−1] <= SAR[t−1]` (hold, flagged complement): `P[t] = Short`; `SIC[t] = MIN` closes over the current short leg; `SAR[t] = SIC[t] + ARC[t−1]`.
- Position target (paradigm wired to the flip book): at the close of each completed bar `i ≥ 8` (post-warmup), the target for the next bar is `P[i+1]`; orders fire for the next bar's open: flat→long buys at next open when the first post-warmup target is Long; flat→short sells at next open when it is Short; long-held + `P = Short` flips full long to full short in one step at next open; short-held + `P = Long` flips full short to full long in one step at next open. Non-crossing bars are no-ops (single-unit, no adds — declared port of one-event-per-bar-boundary). At most one order event per bar boundary; no intrabar evaluation, no intrabar orders, no partials.
- Mutual exclusion (proven, not assumed): the four branches partition on (`P[t−1]`, `C[t−1]` vs `SAR[t−1]`) with strict-reversal / hold-on-equality edges — exactly one branch fires per day, both legs can never fire on the same close, and no priority ruling is owed.
- Degenerate tape (proven, not assumed): a zero-range constant history gives `TR = 0`, `ATR = 0`, `SAR = SIC`; the `C[8] < C[1]` seed is false so `P[9] = Long` by the pinned complement, and every later close equals SAR so the hold branch persists with no flip and no order after the initial adoption; no extra guard is owed.
- Risk legs (declared researcher posture, matching the paradigm's shipped absence of risk): no take-profit, no trailing leg beyond the SAR itself, no time exit — the SAR reversal is simultaneously the stop, the exit, and the re-entry. A vertical adverse move on/after the entry bar is held in full until the opposite SAR cross prints. The Incredible 63-day-EMA entry filter and any `k` inside `[2.8, 3.1]` other than `3.0` are explicitly not adopted. This is the coded trade, disclosed, not a tunable parameter here.
- Direction: two-sided flip system, always-in-market after warmup adoption, flat before it by construction.

## Required data

- Completed `1d` bars of BTCUSDT only: `high`/`low`/`close` feed TR/ATR/SIC/SAR; `open` of the next bar prices fills. No `volume` (no rule gates on it), no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: daily bars. One evaluation per bar at its close; fills land on the next daily bar's open. All inputs are completed-bar values — no provisional intrabar value is ever used; positions, SICs, and SARs are append-only and never revised by later bars. eSignal's day-indexing (`P t` from `C t-1` vs `SAR t-1`) is preserved exactly, ported to bar opens only at the fill step.
- Warmup: the structural need is 8 closes (TR from bar 2, ATR seed over `TR[2..8]`, initial comparison `C[8]` vs `C[1]`, first position `P[9]`). The adopted warmup is the first 30 completed `1d` bars flat by record rule (predeclared researcher choice — covers seeding, ATR bootstrap, and first-leg SAR formation with margin). No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port; all rule sources are venue-agnostic daily-bar price logic — no cross-venue equivalence is claimed beyond high/low/close arithmetic).
- Order timing (predeclared derivation): completed-bar-close decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per bar boundary and mutual exclusion is proven, so there is no same-bar dual-fire to sequence; each flip is one net fill step at a single open price.
- Cash leg: flat earns nothing by record rule (flat exists only before warmup adoption). No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted.
- Sizing/capital/costs: the sources ship no portable economics — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3×/5×) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — long bars carry realized funding, short bars carry realized funding, pre-adoption flat bars carry none) replace them here, never presented as source-native behavior. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one single-unit position (long or short) at any time after warmup adoption; every position-changing event flips in full in one step; no cooldown specified — explicitly none, not invented (re-entry requires the opposite SAR cross, so a cooldown would only delay coded flips). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue. Safety orders: explicitly none.

## Evidence

### Source-reported

The four rule sources ship the full specification (Wilder 7-day / 3.0-multiple setup, close-based stop-and-reverse paradigm, SIC doctrine with Wilder's own phrasing, TR definition, ATR/ARC construction with the `[2.8, 3.1]` band and `3.0` default, day-7/day-8 seeding cadence, the `C[8]`-vs-`C[1]` initial comparison with its TR-availability rationale, MIN/MAX initial SIC, the complete four-branch SAR state machine, period default 7, and the exit-signal wiring) plus one illustrative chart (Incredible's RJ CRB late-2008 down-trend with `S`/`X` markers under a 3×21-day-ATR / 63-day-EMA configuration — a display example only, with no tabulated return, win rate, profit factor, trade count, or sample statistics of any kind). No rule source ships any performance number, table, or figure for the traded 7-day / 3.0 stop-and-reverse book — this record therefore claims no source-reported performance whatsoever.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Zero performance evidence anywhere, stated plainly: no source reports any return, win rate, profit factor, trade count, or sample for the specified 7-day / 3.0 SAR book. This record inherits no performance character from anywhere and reports none.
2. Source-admitted retracement whipsaw on exactly the traded mechanism, stated plainly: the SAR `assumes that the trend has changed every time that your stop is hit`, `stops are regularly hit without the trend changing`, and `Stops may move lower during an up-trend if Average True Range widens`. Every such cross flips the full unit with no filter, target, or cooldown to dampen it.
3. Non-signal framing tension, stated plainly: eSignal declares the system `alone cannot trigger any trade signals` and demands conjunction with other systems, while this record trades the SAR book under CQG's `stop and reverse` paradigm — the paradigm conflict is disclosed here, and the conjunction variants (Volatility Breakout System, trend-filter entries) are fenced as different, unpinned rules.
4. Seeding provenance gap, stated plainly: the initial-position technique `differs slightly from Wilder's discussion` by its own admission — this record ports the specified technique exactly, and makes no claim to Wilder's literal text for the seed.
5. Constant-band choice, stated plainly: `k` is admitted anywhere in `[2.8, 3.1]`; pinning the `3.0` default (with Incredible's and Lizard's corroboration) is the declared normalization — any band-edge re-tuning would be a different, unpinned rule.
6. Conservative fill timing, admitted plainly: SAR crosses completing on close extremes fill at the next bar's open — gap-through-SAR moves are taken at post-move opens, never at the SAR line.
7. Warmup and adoption cost, admitted plainly: the first 30 daily bars are flat by record rule and the post-warmup side is adopted, not signaled — SAR crosses completing inside warmup are deliberately untraded, pinned, not recovered.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: the pinned `n = 7` / `k = 3.0` / Wilder-TR-RMA / SIC-ratchet / four-branch / flip-only book / two-sided / `1d` BTCUSDT / next-open fills / 30-bar warmup are frozen.

- F1 — Constant relevance: a `k = 2.0` twin (tighter cushion, faster switching, same anchor/book/frame/fills) must not improve net expectancy; fail ⇒ the 3.0 width adds nothing over a hair-trigger.
- F2 — Anchor relevance: a range-extreme twin (highest-high `− 3×ATR` / lowest-low `+ 3×ATR` ratchet, same `n`/`k`/book/frame/fills) must not improve net expectancy; fail ⇒ the extreme-favorable-close anchor adds nothing over wick extremes.
- F3 — Flip relevance: a flat-book twin (each SAR cross exits to flat, re-entering the new side only at the next SAR cross, same frame/fills) must not improve net expectancy; fail ⇒ staying perpetually exposed through flips adds nothing over cross-and-wait episodes.
- F4 — Selectivity relevance: buy-and-hold over the same sample must not improve net expectancy; fail ⇒ sitting out pre-adoption and sub-cushion stretches costs more in missed drift than it saves in avoided exposure.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` bar closes; fills at next-bar opens; the state machine reads high/low/close only). Close-anchoring is the source's own answer to gap robustness (TR's `|H − prevC|` / `|L − prevC|` terms already price gap jumps into the cushion, and the 24/7 market rarely gaps at all); the 24/7 market needs no session approximation (bars are exchange `1d` klines, never wall-clock sessions). Both sides are explicit legs, so a spot-only deployment expresses the long half only while every flip-to-short stays venue-gated (short permission unused, never silently converted) — a spot-only variant would be a different, unpinned claim. No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session template, no cross-venue state. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived frame, constant, bootstrap, tie closure, and fill timing: the sources define daily-bar price logic with a `[2.8, 3.1]` constant band, `smoothed` averaging, strict-inequality branches, and day-indexed positions; this record decides on completed `1d` bars at `k = 3.0` with an SMA-seeded Wilder RMA, hold-on-equality closure, and next-open fills. Backtest economics of other framings, constants, seeds, tie rules, or timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about any other configuration.
- No source cost declaration of any kind: no fee, slippage, or funding assumption ships anywhere usable — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Always-in-market exposure: after warmup adoption the book is never flat by rule, so adverse drift between contra SAR crosses is held in full — long unhedged stretches are the coded trade, disclosed, not smoothed.
- Static cushion: the 7-day / 3.0-multiple setting is the source-default pair, frozen here, not tuned — volatility regimes that cross the cushion routinely versus rarely are inherited as-is, disclosed, not adapted.
- Whipsaw exposure: unlike filtered systems there is no trendless fence — the sources themselves declare the stop fires on mere retracements, disclosed, not fenced.
- Warmup and adoption cost: the first 30 daily bars are flat by record rule and the post-warmup side is adopted outright, so SAR crosses completing inside warmup are deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`, bar-close decision on completed `1d` bars, next-open market fills, single-asset two-sided flip book) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. PASS means the declared derived strategy is causally expressible under the pinned Hummingbot model — not profitable, not Qlib-paritied, not source-equivalent, not live-tradable.

## Related Wiki records

None.

## Sources

- Incredible Charts (Colin Twiggs), `Volatility Stops` — Wilder 7-day ATR / 3.0-multiple setup, SIC doctrine, close-based stop-and-reverse feature, day-7/day-8 seeding, exit-signal wiring, trend-filter entry example (unadopted), both stated weaknesses. https://www.incrediblecharts.com/indicators/volatility_stops.php (fetched live 2026-10-14, 30,084 bytes HTML)
- eSignal workstation help, `Wilder's Volatility` — TR definition, ATR(n), ARC constant band with 3.0 default, initial-position rule with worked 7-day arithmetic, MIN/MAX initial SIC, initial SAR, complete four-branch state machine, period default 7, FutureSource-vs-Wilder seeding admission, non-signal framing caveat, Wilder (1978) literature pointer. https://download.esignal.com/products/workstation/help/charts/studies/wilders_volatility.htm (fetched live 2026-10-14, 13,028 bytes HTML)
- CQG official blog (Helmut Mueller, 2019-06-18), `Volatility Stop and Volatility System` — VolSys as Wilder's trend-following stop-and-reverse system over a smoothed range average anchored to extreme closes. https://news.cqg.com/blogs/coding/2019/06/volatility-stop-and-volatility-system (fetched live 2026-10-14, 36,687 bytes HTML)
- Lizard Indicators, `The Wilder Volatility Stop` — default 3× ATR over 7-bar lookback, Wilder's extreme-favorable-close SIC phrasing. https://www.lizardindicators.com/volatility-stop/ (fetched live 2026-10-14, 161,702 bytes HTML)
