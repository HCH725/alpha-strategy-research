---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: WorldQuant Alpha9 streak-gated daily reversal-continuation two-sided on BTCUSDT 1d bars
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2015-12-09
sources:
  - https://arxiv.org/abs/1601.00991
  - https://arxiv.org/pdf/1601.00991
  - https://github.com/OctopusTakopi/toraniko-alpha101
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# WorldQuant Alpha9 streak-gated daily reversal-continuation two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read end to end during this cycle (2026-10-16), pinned:

- Paper (local text extraction of the arXiv PDF, read end to end this cycle): `Zura Kakushadze`, `101 Formulaic Alphas`, arXiv `1601.00991` (manuscript dated `December 9, 2015` — record `source_as_of` is that manuscript date, never a fetch date; the paper states the formulas `are also computer code` once the operators are defined). Alpha#9 prints in Appendix A.1 as `((0 < ts_min(delta(close, 1), 5)) ? delta(close, 1) : ((ts_max(delta(close, 1), 5) < 0) ? delta(close, 1) : (-1 * delta(close, 1))))`. Operator pins from the paper's own definitions section: `delay(x, d) = value of x d days ago`; `delta(x, d) = today's value of x minus the value of x d days ago`; `correlation(x, y, d) = time-serial correlation of x and y for the past d days`; `abs(x), log(x), sign(x) = standard definitions`; inputs `open, close, high, low, volume = standard definitions for daily price and volume data`. Timing pin from §2: `delay-1 means that the alpha is traded on the day subsequent to the date of the most recent data used in computing it` (e.g. traded today `starting at the open`); footnote 11 names exactly four delay-0 alphas (`42, 48, 53 and 54`, traded at or as close as possible to the close of the computed day) — Alpha#9 is not among them, so it is delay-1 by the paper's own exclusion. Direction pin from the §2 worked example: `Alpha#101 ... is a delay-1 momentum alpha: if the stock runs up intraday (i.e., close > open and high > low), the next day one takes a long position` — a positive score maps to long, a negative score to short (see Negative evidence 1 for the exact strength of this pin).
- Audited pinned implementation (fetched live this cycle, verified byte-identical to the local audit copy): repository `https://github.com/OctopusTakopi/toraniko-alpha101`, head commit `4fc0627d2a720fd8d583708ef051b9d48d98aacd` (2026-07-17, `Fix Alpha101 report correctness`, verified via the GitHub commits API this cycle), exact file `toraniko/alpha101.py`: `def alpha009` computes `change = delta(self.close, 1)`, `minimum, maximum = ts_min(change, 5), ts_max(change, 5)`, then the nested conditional `minimum > 0 → change` else `maximum < 0 → change` else `-change` (lines 271–275, matching the printed ternary branch order); `def delay` emits the value shifted by the lookback and `def delta` is `x - delay(x, period)` (lines 74–82, first rows undefined by construction); `def ts_min/ts_max` are full-window trailing rolling minima/maxima (lines 108–113, undefined before the window is full); `_if_else` preserves undefined condition inputs as undefined rather than guessing a branch (lines 192–199). Operator-convention evidence from the pinned test suite `toraniko/tests/test_alpha101.py` (same commit): conditional alphas emit no signal before warmup — `alpha009` undefined for `date < 5`, i.e. first defined on the 6th bar (`test_conditional_alphas_do_not_emit_signals_before_warmup`). The same test file pins the sibling Alpha#24 at 200 bars and records the neutralization manifest (Alpha#9 needs no sector/industry/subindustry class — absent from the manifest). Alpha#9 needs no rank, no scale, no adv, no vwap, no division, and no zero-division branch of its own: every input is finite once the 5-bar delta window exists, and an exact-zero print is a deterministic flat.

Licence and rights: the paper is a public arXiv preprint; the implementation is public research software. This record cites and normalizes the rule (single-line formula and operator definitions only for gate evidence) and reproduces no source block beyond single-line facts.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the paper. The paper prints the Alpha#9 formula, the operator definitions, the delay-1 timing class, and the positive-score→long convention, but ships no venue, no symbol, no single-asset side mapping (its own evaluation is cross-sectional quintile), no order/fill semantics, no warmup seed, and no risk leg. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` Binance USDT-M perpetual `1d` (the paper is daily U.S. equities with no venue — frame/venue pin disclosed, never a source claim; perpetual is the minimal realistic venue because the short leg needs margin); (2) completed-bar decisions with next-bar-open market fills (the paper trades delay-1 `on the day subsequent to the date of the most recent data`, `starting at the open` — deviation class identical to the admitted caporale-plastun, ehlers-cg, worldquant-alpha6, and worldquant-alpha12 records' bar-port, disclosed, never an advantage claim); (3) an adopted 10-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 6th completed bar — delta needs 2 closes and the 5-bar streak window needs 5 defined deltas, pinned by the test above — plus margin; see Required data); (4) house sizing/costs with modeled funding while held (the paper ships no sizing, capital, fee, or slippage concept — never presented as source-native behavior). The streak-gated ternary, the branch order, the strict-zero comparisons, the exact-zero flat tie, the delay-1 next-day execution, the positive→long / negative→short mapping, the reversal-only exits, and the no-stop/no-target risk posture are source-grounded and unmodified.

Pre-write dedup (2026-10-16): working-tree case-insensitive searches for `worldquant`, `kakushadze`, `1601.00991`, `alpha009`, `alpha#9`, and `ts_min(delta` return zero strategy records except the siblings `worldquant-alpha6` (negated 10-day open-volume correlation statistic — no delta, no streak, no branch) and `worldquant-alpha12` (volume-change-signed 1-day product — different gate object, no streak window, see Negative evidence 6). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long — EMA-channel object, long-only), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Closed-reviewer precedents (#6 WaveTrend tie semantics, #10 golden-cross spot/short, #17 MACD-hist seeding, #20 Ichimoku-RSI always-in-market funding) are different rules. This is the third WorldQuant-101 record in the pool family, not a parameter variant of any admitted rule.

## Economic mechanism

### Source-reported

Coarse mean-reversion/momentum building blocks. The paper frames its universe coarsely: `one can think of alpha signals as based on mean-reversion or momentum`, where `a mean-reversion alpha has a sign opposite to the return on which it is based`, and adds that `in complex alphas elements of mean-reversion and momentum can be mixed`. Alpha#9 is that mixture in one line: five straight up-days (every trailing 1-day change positive) scores the latest change itself — momentum continuation; five straight down-days likewise continues; any mixed window negates the latest change — mean-reversion. The paper ships no behavioural, structural, or risk-premium mechanism beyond this measurement construction, and no stop, target, or risk leg of any kind.

### Research interpretation

Streak-gated reversal with continuation override, two-sided, threshold-free. On most bars the trailing 5-day change window is mixed, so the book is a plain 1-day close reversal (`-delta(close, 1)`); only a perfect 5-bar sign streak flips that bar into continuation. Unlike the sibling worldquant-alpha12 record (whose reversal leg is gated by the sign of the 1-day volume change — a same-bar companion-series gate), this rule never reads volume: its gate is the sign purity of the close-change history itself. Unlike the pool `eight-day-run` record (closes measured against a moving SMA5 reference with first-recross entry/exit legs), nothing here references an average and there are no legs — an always-in sign book flips or holds every bar. Unlike the pool `three-down-three-up` record (strict close-vs-prior-close chains, long-only, 1h), the streak here is measured on signed deltas with a continuation payoff rather than a reversal trigger, and the mixed-window reversal covers every non-streak bar. The failure mode is plain: continuation bars ride waterfalls and melt-ups without a stop, while mixed-window bars churn the book on 1-day noise — disclosed, not upgraded.

## Signal

Exact rule as pinned (any other window, series, branch order, comparison, fill, frame, book, or tie treatment is a different, unpinned rule):

- Inputs (paper A.2): `close[t]` on completed `1d` bars only. No `open`, no `high`, no `low`, no `volume`, no vwap/adv/sector, no cross-sectional rank, no second asset or timeframe is read by any order-gating line.
- One-day change (paper A.1, pinned impl lines 74–82): `d[t] = delta(close, 1)[t] = close[t] − close[t−1]`. Undefined before the 2nd completed bar by construction.
- Streak window (paper Appendix A.1, pinned impl lines 108–113, 271–275): `m[t] = ts_min(d, 5)[t]` and `M[t] = ts_max(d, 5)[t]` — trailing minima/maxima over the past 5 defined changes inclusive. Undefined before the 6th completed bar (pinned test convention), never seeded or backfilled.
- Score (paper Appendix A.1, pinned impl lines 271–275, branch order source-printed): `score[t] = d[t]` if `m[t] > 0` (five straight up-days — strictly positive latest change by construction, so this branch can only print long); else `score[t] = d[t]` if `M[t] < 0` (five straight down-days — strictly negative latest change, so this branch can only print short); else `score[t] = −d[t]` (mixed window — both signs possible). No division, no rank, no scale, no floor, no threshold beyond the two printed strict-zero comparisons exists anywhere in this formula.
- Direction mapping (source-grounded, fenced in Negative evidence 1): `score[t] > 0` → long signal; `score[t] < 0` → short signal; `score[t] == 0` → flat signal (exact-zero prints when the mixed-branch change is exactly zero, i.e. `−0.0` — deterministic flat, never a held conviction). The entry fills at the next bar's open, one single unit, only if the book does not already carry that side (see position rule).
- Exit: the first opposite signal reverses the full unit in one step (close plus opposite entry at the same next-bar-open fill); a zero print flattens the full unit at the next open — reversal-or-flatten is the sole exit path by construction. No stop-loss, no take-profit, no trailing, no time exit (the paper ships no risk leg — carried over exactly, disclosed in Provenance adaptation (4), never upgraded into a source claim).
- Direction: two-sided (long leg and short leg are both native). Shorts are native to USDT-M margin (no uptick rule, no borrow desk).
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further long-signal bars as no-ops (no pyramiding, no averaging), and symmetrically for shorts. Re-entry re-arms on the next opposite or flat-exit signal only (no cooldown specified — explicitly none, not invented). Pre-first-signal bars are flat.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (the sole series the formula reads). No `open`/`high`/`low`/`volume`, no funding-signal, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; the streak window reads the same single series, never a second feed).
- Warmup: 10 completed `1d` bars flat by record rule — structural minimum is the 6th completed bar (the 5-bar streak window needs 5 defined 1-day changes: bars 2–6 — pinned by `test_conditional_alphas_do_not_emit_signals_before_warmup`), plus margin per the admitted balance-of-power precedent. Pre-warmup bars are flat by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (streak window reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance USDT-M perpetual under the house overlay (researcher choice — the paper names no venue and evaluates U.S. equities; no source-market equivalence is claimed; perpetual is the minimal realistic venue because the short leg needs margin).
- Order timing (paper-grounded derivation): completed-bar decision with next-bar-open market fills for entries, reversals, and flat-exits — the paper's delay-1 class trades `on the day subsequent to the date of the most recent data`, `starting at the open`, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) on the same verified primitive as the admitted caporale-plastun, ehlers-cg, worldquant-alpha6, and worldquant-alpha12 records' entries (verified this cycle's base). This record claims no other fill convention: no perfect-open print, no maker-touch, no intrabar-path-dependent fill.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing orders by record rule. No hidden Hummingbot stop-order defaults are relied upon, and with no stop/limit legs there is no same-bar TP/SL ordering ambiguity.
- Sizing/capital/costs: the paper ships no sizing, capital, fee, or slippage concept. The explicit house overlay (single-unit frame, pinned house taker fees both legs, modeled funding while held) applies to the derived evaluation here, never presented as source-native behavior. Funding is never zero-claimed: two-sided holds span the `00:00`/`08:00`/`16:00 UTC` funding stamps, so every held bar carries modeled funding.
- Concurrency: at most one single-asset engine position at any time; an opposite signal closes-and-reverses in one step and a zero signal closes-to-flat. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (arXiv 1601.00991 text, read end to end this cycle): the `are also computer code` formula status; the Alpha#9 line `((0 < ts_min(delta(close, 1), 5)) ? delta(close, 1) : ((ts_max(delta(close, 1), 5) < 0) ? delta(close, 1) : (-1 * delta(close, 1))))`; the A.1 operator definitions (`delay(x, d)`, `delta(x, d)`, `correlation(x, y, d) = time-serial correlation`, `abs/log/sign` standards); the A.2 input definitions (`open, close, high, low, volume = standard definitions for daily price and volume data`); the §2 delay-1 definition and the footnote-11 delay-0 exclusion list (`42, 48, 53 and 54` — Alpha#9 absent, hence delay-1); the §2 mixed building-block framing; the §2 Alpha#101 worked example pinning positive-score→long. With exact implementation provenance (pinned commit `4fc0627d`, file `toraniko/alpha101.py` lines 74–82, 108–113, 192–199, and 271–275, plus the named warmup test): the executable delta/streak/conditional semantics, the full-window-undefined convention, the undefined-preserving conditional, and the 6th-bar first-signal convention. This record claims no source-reported performance number of any kind — no return, no win rate, no trade count, no per-alpha table figure is carried into the derived specification — and no reproduced performance exists.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Direction words fenced, admitted plainly: the paper never prints `buy`, `sell`, `long`, or `short` for Alpha#9. The positive→long / negative→short mapping rests on the §2 Alpha#101 worked example (a positive intraday score takes `a long position` the next day) together with the implementation report's long-top-quintile / short-bottom-quintile construction — not on any order verb attached to Alpha#9 itself. A reviewer must not graft any other direction convention onto this record.
2. Timeframe and venue fenced: the paper is daily U.S. equities and names no venue. `1d` BTCUSDT-perpetual is the disclosed researcher pin (Provenance adaptation (1)); a reviewer must not cite the paper as evidence for any frame or venue.
3. Risk silence fenced: the paper contains no stop, target, trailing, time exit, or risk paragraph for Alpha#9 — the no-guardrail posture is carried over exactly, never upgraded, never presented as a tested safety choice.
4. Cross-sectional machinery fenced: the paper's own evaluation ranks scores across thousands of stocks and industry-neutralizes many alphas. Alpha#9's formula contains no `rank(`, no `IndNeutralize`, no `scale(`, no `vwap`, no `adv`, and no sector/industry term (verified by programmatic filter over all 101 lines this cycle; the pinned neutralization manifest covers other alphas, never #9) — the single-asset sign map drops the cross-sectional portfolio layer entirely, disclosed as adaptation, never presented as the paper's traded portfolio.
5. Exact-zero determinism fenced: `score[t] == 0` requires the mixed-branch change to print exactly zero (`−0.0`). The flat treatment is a predeclared record rule (total and mutually exclusive with the long/short branches), not a paper sentence — without it the zero print would be ambiguous, so it is pinned here rather than left to the reviewer. Streak-branch sides need no tie rule: `m[t] > 0` forces the latest change positive (long-only branch) and `M[t] < 0` forces it negative (short-only branch) by construction.
6. Overlap fences, admitted plainly: sibling `worldquant-alpha12` trades a volume-change-signed 1-day product `sign(delta(volume,1)) × (−delta(close,1))` (different gate object — a same-bar companion series, never a streak window — and no continuation branch); sibling `worldquant-alpha6` trades a negated 10-day open-volume correlation (a window statistic over two level series — no delta, no streak, no conditional); pool `eight-day-run` gates entries on 8+ closes on one side of SMA5 with first-recross legs (a moving-average reference object with entry/exit legs — this record has no average and no legs, only a sign book); pool `three-down-three-up` counts strict close chains long-only on 1h (a trigger, never a mixed-window reversal book); pool `connors-rsi2`/`double-seven` fade oscillator/range extremes (level objects, never delta-sign purity); pool `caporale-plastun` trades one-day abnormal returns on 1h; open PR #48 streak-gates a 3-EMA channel long-only (an average-channel object, never a delta window). Shared `streak`/`reversal`/`delta` vocabulary is not shared signal.
7. Twin fenced: the paper's Alpha#10 wraps the same streak core at window 4 inside a cross-sectional `rank(...)` — universe-dependent and excluded here by the programmatic filter, never silently substituted. A reviewer must not swap #10's window, rank, or any other alpha's parameter into this record.
8. No hidden variants admitted: any other window, any other series, any other branch order or comparison, any threshold, any stop/target/filter/cooldown, any other frame, fill, venue, or book is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 5-bar delta streak window / branch order / strict-zero comparisons / exact-zero flat / two-sided / delay-1 next-open fills / no-stop posture / `1d` BTCUSDT perpetual are frozen.

- F1 — Streak-gate relevance: a plain 1-day-reversal twin (score `= −delta(close, 1)` every bar — same book, grid, fills) must not improve net expectancy; fail ⇒ the 5-bar streak gate adds nothing over an unconditional daily reversal.
- F2 — Continuation-override relevance: a never-continue twin is identical to F1 by construction, so instead a streak-only twin (mixed-window bars flat instead of reversing — continuation legs only, same entries/fills) must not improve net expectancy; fail ⇒ the mixed-window reversal leg adds nothing over trading continuation streaks alone.
- F3 — Horizon relevance: a long-window twin (same ternary at window 10 with a 15-bar adopted warmup — same construction, same book, grid, fills) must not improve net expectancy; fail ⇒ the 5-bar horizon adds nothing over the same construction at twice the scale, and the record is a horizon label rather than a horizon edge.

## Crypto portability

Pinned to BTCUSDT Binance USDT-M perpetual under the house overlay (declared port of a venue-free daily-equity formula). The rule reads completed daily bars only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (the paper's split/dividend close adjustment is a non-issue on crypto — disclosed, not modeled). The score is a dollar change whose side alone trades — scale-free in direction, yet close-change magnitudes differ across venues, disclosed without normalization to invent. The rule is two-sided, so a spot-only deployment expresses only long-firing bars while short-firing bars stay venue-gated (never silently converted) — a spot-only variant would be a different, unpinned claim. No warmup history beyond 10 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop: a 5-bar continuation streak rides waterfalls and melt-ups with no guardrail before the first mixed print, by the carried-over paper design — the record's principal risk.
- Mixed-window churn: most bars are mixed, so the book is usually a raw 1-day reversal flipping on close-change noise — the paper provides no buffer band and this record invents none.
- Streak rarity skew: perfect 5-bar sign streaks are rare, so the continuation override fires infrequently — the record is dominated by its reversal leg, disclosed.
- Exact-zero note: the flat branch fires on exact-zero mixed-branch prints only — rare on BTCUSDT, so the book is effectively always-in-market, disclosed.
- Single-venue port residual: paper-regime U.S. equities vs Binance perpetual execution (prints, fees, funding, volume-definition, margin mechanics beyond the house model) is unclaimed, disclosed.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest.
- Author scope: the paper presents production formulaic alphas as research objects, not a vetted retail trading system — this record is research-only and claims no live suitability.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Kakushadze, Z., `101 Formulaic Alphas`, arXiv:1601.00991 (manuscript December 9, 2015 — Alpha#9 formula, A.1 operator definitions, A.2 daily price/volume inputs, §2 delay-1 definition with footnote-11 delay-0 exclusion, §2 Alpha#101 direction worked example — read end to end via text extraction 2026-10-16): https://arxiv.org/abs/1601.00991
- Same paper, PDF (formula appendix, operator/input definitions, empirical sections — read 2026-10-16): https://arxiv.org/pdf/1601.00991
- OctopusTakopi `toraniko-alpha101` (independent audited implementation — `alpha009` at `toraniko/alpha101.py` lines 271–275, `delay`/`delta` at lines 74–82, `ts_min`/`ts_max` at lines 108–113, `_if_else` at lines 192–199, warmup convention in `toraniko/tests/test_alpha101.py` — pinned to commit `4fc0627d2a720fd8d583708ef051b9d48d98aacd`, verified live 2026-10-16): https://github.com/OctopusTakopi/toraniko-alpha101
