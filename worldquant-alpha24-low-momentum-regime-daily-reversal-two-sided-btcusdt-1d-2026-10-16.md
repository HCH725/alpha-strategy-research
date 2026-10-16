---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: WorldQuant Alpha24 low-momentum-regime daily reversal two-sided on BTCUSDT 1d bars
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

# WorldQuant Alpha24 low-momentum-regime daily reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read and re-verified end to end during this cycle (2026-10-16), pinned:

- Paper (local text extraction of the arXiv PDF fetched this cycle, `/tmp/wq101.pdf` 22 pages / 239 KB, key passages re-verified this cycle): `Zura Kakushadze`, `101 Formulaic Alphas`, arXiv `1601.00991` (manuscript dated `December 9, 2015` — record `source_as_of` is that manuscript date, never a fetch date; the paper states the formulas `are also computer code` once the operators are defined). Alpha#24 prints in Appendix A.1 as `((((delta((sum(close, 100) / 100), 100) / delay(close, 100)) < 0.05) || ((delta((sum(close, 100) / 100), 100) / delay(close, 100)) == 0.05)) ? (-1 * (close - ts_min(close, 100))) : (-1 * delta(close, 3)))` (i.e. `trend <= 0.05` picks the low-regime leg, else the 3-day reversal leg). Operator pins from the paper's own definitions section: `delay(x, d) = value of x d days ago`; `delta(x, d) = today's value of x minus the value of x d days ago`; `rank(x) = cross-sectional rank`; inputs `open, close, high, low, volume = standard definitions for daily price and volume data`. Timing pin from §2: `delay-1 means that the alpha is traded on the day subsequent to the date of the most recent data used in computing it` (e.g. traded today `starting at the open`); footnote 11 names exactly four delay-0 alphas (`42, 48, 53 and 54`, traded at or as close as possible to the close of the computed day) — Alpha#24 is not among them, so it is delay-1 by the paper's own exclusion. Direction pin from the §2 worked example: `Alpha#101 ... is a delay-1 momentum alpha: if the stock runs up intraday (i.e., close > open and high > low), the next day one takes a long position` — a positive score maps to long, a negative score to short (see Negative evidence 1 for the exact strength of this pin).
- Audited pinned implementation (fetched live this cycle, verified byte-identical to the pinned audit bytes, sha256 `b54a820ca35fc06359f023cb590015ff4d4cd818c077322d587dc4e9cbf70316`): repository `https://github.com/OctopusTakopi/toraniko-alpha101`, head commit `4fc0627d2a720fd8d583708ef051b9d48d98aacd` (2026-07-17, `Fix Alpha101 report correctness`, confirmed still the repository head via the GitHub commits API this cycle), exact file `toraniko/alpha101.py`: `def alpha024` computes `trend = _safe_div(delta(sma(self.close, 100), 100), delay(self.close, 100))` then `_if_else(trend <= 0.05, -(self.close - ts_min(self.close, 100)), -delta(self.close, 3), trend)` (lines 339–341, matching the printed ternary with the `||` pair folded into one `<=`); `def delay` is the d-bar-ago value with NaN before the d-th bar (lines 74–79); `def delta` is `x - delay(x, period)` (lines 81–82); `def sma` / `ts_sum` / `ts_min` are full-window trailing operators undefined before the window fills (lines 85–101, 108–109 — no partial-window seeding); `_safe_div` maps every non-finite quotient to NaN rather than guessing a number (lines 185–190); `_if_else` preserves undefined condition inputs as undefined rather than guessing a branch (lines 192–199). The pinned neutralization manifest covers other alphas (48, 58, 59, 63, 67, 69, 70, 76, 79, 80, 82, 87, 89, 90, 91, 93, 97, 100) — never #24, so Alpha#24 needs no sector/industry/subindustry class. Alpha#24 needs no rank, no scale, no adv, no vwap, no returns, no market-cap, and no threshold beyond the single printed `0.05` comparison: the sole division is guarded to NaN (flat by record rule, never a fabricated score).

Licence and rights: the paper is a public arXiv preprint; the implementation is public research software. This record cites and normalizes the rule (single-line formula and operator definitions only for gate evidence) and reproduces no source block beyond single-line facts.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the paper. The paper prints the Alpha#24 formula, the operator definitions, the delay-1 timing class, and the positive-score→long convention, but ships no venue, no symbol, no single-asset side mapping (its own evaluation is cross-sectional quintile), no order/fill semantics, no warmup seed, and no risk leg. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` Binance USDT-M perpetual `1d` (the paper is daily U.S. equities with no venue — frame/venue pin disclosed, never a source claim; perpetual is the minimal realistic venue because the short leg needs margin); (2) completed-bar decisions with next-bar-open market fills (the paper trades delay-1 `on the day subsequent to the date of the most recent data`, `starting at the open` — deviation class identical to the admitted caporale-plastun, ehlers-cg, worldquant-alpha6, worldquant-alpha9, worldquant-alpha12, and worldquant-alpha23 records' bar-port, disclosed, never an advantage claim); (3) an adopted 210-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 200th completed bar — the 100-bar close mean needs 100 closes, and its 100-bar change needs the mean at both ends, pinned by the operator code above — plus margin; see Required data); (4) house sizing/costs with modeled funding while held (the paper ships no sizing, capital, fee, or slippage concept — never presented as source-native behavior). The momentum-ratio gate, the strict `<= 0.05` comparison, the low-regime distance-to-100-day-low payoff, the high-regime negated 3-bar close-change payoff, the delay-1 next-day execution, the positive→long / negative→short mapping, the reversal-or-flatten exits, and the no-stop/no-target risk posture are source-grounded and unmodified.

Pre-write dedup (2026-10-16): working-tree case-insensitive searches for `alpha24`, `ts_min(close, 100)`, `sum(close, 100)`, and `delta(close, 3)` return zero strategy records; the siblings are `worldquant-alpha6` (negated 10-day open-volume correlation statistic — no gate, no payoff split), `worldquant-alpha12` (volume-change-signed 1-day close product — a same-bar companion-series gate, never a momentum-ratio gate), `worldquant-alpha9` (5-bar delta-sign streak ternary on closes — a sign-purity gate, never a momentum-ratio gate), and `worldquant-alpha23` (20-bar high-mean level gate with a negated 2-bar high-change payoff — a level object on highs, never a 100-day momentum ratio on closes, see Negative evidence 6). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. This is the fifth WorldQuant-101 record in the pool family, not a parameter variant of any admitted rule.

## Economic mechanism

### Source-reported

Coarse mean-reversion/momentum building blocks. The paper frames its universe coarsely: `one can think of alpha signals as based on mean-reversion or momentum`, where `a mean-reversion alpha has a sign opposite to the return on which it is based`. Alpha#24 is a two-regime block keyed by a 100-day SMA momentum ratio: at or below `0.05` the book takes the opposite side of the distance above the trailing 100-day low; above `0.05` it takes the opposite side of the trailing 3-bar close change. The paper ships no behavioural, structural, or risk-premium mechanism beyond this measurement construction, and no stop, target, or risk leg of any kind.

### Research interpretation

Low-momentum-regime distance book spliced to a high-momentum 3-day reversal book, two-sided overall, with a structural long impossibility inside the low regime. The gate (`delta(SMA100,100) / close[t−100] <= 0.05`) is a slow-momentum object — a 100-day mean against its own 100-day-ago value, scaled by the 100-day-ago close — while the two payoffs never share a form: Branch A (`MIN100 − close`) is a distance-to-trailing-low object that by construction can only print zero or negative (close can never print below its own trailing minimum, so Branch A never goes long — the book shorts above the 100-day low and sits flat exactly at it); Branch B (`close[t−3] − close[t]`) is a 3-day change object that is genuinely two-sided. Unlike sibling worldquant-alpha23 (a high level gate on the high series with a flat regime below the mean), this rule has no flat regime by formula — every defined bar fires one leg or the other, and undefined bars alone go flat by record rule. Unlike sibling worldquant-alpha9 (a sign-purity gate, always-in-market), the regime here is a slow momentum ratio, not a streak count. Unlike sibling worldquant-alpha12 (a volume-signed 1-day product), this rule never reads volume. The failure mode is plain: a grinding low-momentum selloff keeps Branch A short with size equal to the full distance above a falling 100-day low, while a steep high-momentum trend keeps Branch B fading every 3-day push with no guardrail — disclosed, not upgraded.

## Signal

Exact rule as pinned (any other window, series, comparison, threshold, fill, frame, book, or tie treatment is a different, unpinned rule):

- Inputs (paper A.2): `close[t]` on completed `1d` bars only. No `open`, no `high`, no `low`, no `volume`, no vwap/adv/returns/market-cap/sector, no cross-sectional rank, no second asset or timeframe is read by any order-gating line.
- Slow gate (paper Appendix A.1, pinned impl lines 339–341): `sma100[t] = sum(close, 100)[t] / 100` — full-window trailing mean, undefined before the 100th completed bar, never seeded or backfilled; `trend[t] = (sma100[t] − sma100[t−100]) / close[t−100]` — guarded division (non-finite → NaN → flat by record rule, never a fabricated score). Structural first-defined gate bar is the 200th completed bar.
- Branch A — low-regime leg (paper A.1, pinned impl lines 339–341): if `trend[t] <= 0.05`, `score[t] = −(close[t] − MIN100[t]) = MIN100[t] − close[t]`, where `MIN100[t] = ts_min(close, 100)[t]` is the full-window trailing 100-bar minimum, undefined before the 100th completed bar. By construction `score[t] <= 0` always (short-or-flat leg; long is structurally impossible in this branch — disclosed in Research interpretation, never patched).
- Branch B — high-regime leg (paper A.1, pinned impl lines 81–82, 339–341): else `score[t] = −delta(close, 3)[t] = close[t−3] − close[t]`. Undefined before the 4th completed bar by construction; genuinely two-sided.
- Direction mapping (source-grounded, fenced in Negative evidence 1): `score[t] > 0` → long signal; `score[t] < 0` → short signal; `score[t] == 0` → flat signal (fires when Branch A sits exactly at the 100-day low, or when the Branch B 3-bar change prints exactly zero). The entry fills at the next bar's open, one single unit, only if the book does not already carry that side (see position rule).
- Exit: the first opposite signal reverses the full unit in one step (close plus opposite entry at the same next-bar-open fill); a zero print flattens the full unit at the next open — reversal-or-flatten is the sole exit path by construction. No stop-loss, no take-profit, no trailing, no time exit (the paper ships no risk leg — carried over exactly, disclosed in Provenance adaptation (4), never upgraded into a source claim).
- Direction: two-sided overall (the short leg fires in both branches; the long leg fires only via Branch B — predeclared asymmetry, never smoothed over).
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further long-signal bars as no-ops (no pyramiding, no averaging), and symmetrically for shorts; flat-regime bars while already flat are no-ops. Re-entry re-arms on the next opposite or flat-exit signal only (no cooldown specified — explicitly none, not invented). Pre-first-signal and any NaN-score bars are flat by record rule.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (the sole series the formula reads). No `open`/`high`/`low`/`volume`, no funding-signal, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; the gate and both payoffs read the same single series, never a second feed).
- Warmup: 210 completed `1d` bars flat by record rule — structural minimum is the 200th completed bar (the 100-bar close mean needs 100 completed closes per the full-window `sma` code, and its 100-bar change needs the mean at both ends per the `delta`/`delay` code; the 100-bar minimum needs 100 and the 3-bar change needs 4 — pinned by operator code, not by a test sentence), plus margin per the admitted worldquant-alpha23 precedent (20→25). Pre-warmup and any NaN-score bars are flat by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (gate and payoffs read completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance USDT-M perpetual under the house overlay (researcher choice — the paper names no venue and evaluates U.S. equities; no source-market equivalence is claimed; perpetual is the minimal realistic venue because the short leg needs margin).
- Order timing (paper-grounded derivation): completed-bar decision with next-bar-open market fills for entries, reversals, and flat-exits — the paper's delay-1 class trades `on the day subsequent to the date of the most recent data`, `starting at the open`, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) on the same verified primitive as the admitted caporale-plastun, ehlers-cg, worldquant-alpha6, worldquant-alpha9, worldquant-alpha12, and worldquant-alpha23 records' entries (verified this cycle's base). This record claims no other fill convention: no perfect-open print, no maker-touch, no intrabar-path-dependent fill.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing orders by record rule. No hidden Hummingbot stop-order defaults are relied upon, and with no stop/limit legs there is no same-bar TP/SL ordering ambiguity.
- Sizing/capital/costs: the paper ships no sizing, capital, fee, or slippage concept. The explicit house overlay (single-unit frame, pinned house taker fees both legs, modeled funding while held) applies to the derived evaluation here, never presented as source-native behavior. Funding is never zero-claimed: two-sided holds span the `00:00`/`08:00`/`16:00 UTC` funding stamps, so every held bar carries modeled funding.
- Concurrency: at most one single-asset engine position at any time; an opposite signal closes-and-reverses in one step and a zero signal closes-to-flat. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (arXiv 1601.00991 text extracted from the PDF fetched this cycle, key passages re-verified this cycle): the `are also computer code` formula status; the Alpha#24 line `((((delta((sum(close, 100) / 100), 100) / delay(close, 100)) < 0.05) || ((delta((sum(close, 100) / 100), 100) / delay(close, 100)) == 0.05)) ? (-1 * (close - ts_min(close, 100))) : (-1 * delta(close, 3)))`; the A.1 operator definitions (`delay(x, d)`, `delta(x, d)`, `rank(x) = cross-sectional rank`); the A.2 input definitions (`open, close, high, low, volume = standard definitions for daily price and volume data`); the §2 delay-1 definition and the footnote-11 delay-0 exclusion list (`42, 48, 53 and 54` — Alpha#24 absent, hence delay-1); the §2 mixed building-block framing; the §2 Alpha#101 worked example pinning positive-score→long. With exact implementation provenance (pinned commit `4fc0627d`, file `toraniko/alpha101.py` lines 74–82, 85–101, 108–109, 185–199, and 339–341, plus the neutralization manifest covering other alphas but never #24): the executable momentum-ratio gate / distance-vs-reversal payoff / conditional semantics, the full-window-undefined convention, the guarded division, the undefined-preserving conditional, and the 200th-bar first-signal convention. This record claims no source-reported performance number of any kind — no return, no win rate, no trade count, no per-alpha table figure is carried into the derived specification — and no reproduced performance exists.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Direction words fenced, admitted plainly: the paper never prints `buy`, `sell`, `long`, or `short` for Alpha#24. The positive→long / negative→short mapping rests on the §2 Alpha#101 worked example (a positive intraday score takes `a long position` the next day) together with the top-quintile / bottom-quintile construction — not on any order verb attached to Alpha#24 itself. A reviewer must not graft any other direction convention onto this record.
2. Timeframe and venue fenced: the paper is daily U.S. equities and names no venue. `1d` BTCUSDT-perpetual is the disclosed researcher pin (Provenance adaptation (1)); a reviewer must not cite the paper as evidence for any frame or venue.
3. Risk silence fenced: the paper contains no stop, target, trailing, time exit, or risk paragraph for Alpha#24 — the no-guardrail posture is carried over exactly, never upgraded, never presented as a tested safety choice.
4. Cross-sectional machinery fenced: the paper's own evaluation ranks scores across thousands of stocks and industry-neutralizes many alphas. Alpha#24's formula contains no `rank(`, no `IndNeutralize`, no `scale(`, no `vwap`, no `adv`, no `returns`, no market-cap, and no sector/industry term (verified by programmatic filter over all 101 implementations this cycle; the pinned neutralization manifest covers other alphas, never #24) — the single-asset sign map drops the cross-sectional portfolio layer entirely, disclosed as adaptation, never presented as the paper's traded portfolio.
5. Exact-zero and NaN determinism fenced: `score[t] == 0` fires when Branch A sits exactly at the 100-day low or when the Branch B 3-bar change prints exactly zero; any NaN gate, NaN division, or pre-warmup bar is flat by record rule. All three are predeclared record-rule flats, not paper sentences — without them the zero/undefined prints would be ambiguous, so they are pinned here rather than left to the reviewer.
6. Overlap fences, admitted plainly: sibling `worldquant-alpha23` gates on a 20-bar high-vs-mean level with a negated 2-bar high-change payoff and an explicit formula flat regime (a level object on highs — this record's gate is a 100-day momentum ratio on closes with no formula flat regime); sibling `worldquant-alpha9` gates on 5-bar delta-sign purity with an always-in-market book (a history-purity object — this record has no streak window); sibling `worldquant-alpha12` trades a volume-change-signed 1-day close product (a same-bar companion-series gate — this record never reads volume); sibling `worldquant-alpha6` trades a negated 10-day open-volume correlation (a two-series window statistic — no gate, no payoff split); pool `donchian-20-10` breaks rolling 20-bar highest-high/lowest-low extremes with a 10-bar trailing exit (a memory-of-extrema object with exit legs — this record's low leg reads a trailing minimum as a distance anchor with no legs, and its gate is a momentum ratio); pool `balance-of-power-cross` trades body-to-range pressure (a single-bar shape object — never a 100-day momentum gate); open PR #251 zone-states a 2-year MA multiplier long-flat (a level-zone object, never a momentum-ratio splice). Shared `close`/`average`/`minimum`/`reversal` vocabulary is not shared signal.
7. Twins and neighbours fenced: the paper's Alpha#46/#49/#51 family trades the same 20/10-day close-slope quantity at different thresholds (a slope object on closes — never a 100-day momentum ratio; none is substituted here); Alpha#53/#54 are delay-0 single-print constructions (a different timing class — never substituted); Alpha#101 is the body-to-range ratio already embodied by the pool balance-of-power record (not repeated here). A reviewer must not swap any other alpha's window, series, threshold, or branch into this record.
8. No hidden variants admitted: any other window, any other series, any other comparison direction or threshold, any stop/target/filter/cooldown, any other frame, fill, venue, or book is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 100-day SMA momentum-ratio gate / `<= 0.05` comparison / low-regime distance-to-100-day-low payoff / high-regime negated 3-bar close-change payoff / two-sided-overall book / delay-1 next-open fills / no-stop posture / `1d` BTCUSDT perpetual are frozen.

- F1 — Gate relevance: an always-on twin (score `= −delta(close, 3)` every bar — same payoff, grid, fills, no gate, no MIN leg) must not improve net expectancy; fail ⇒ the 100-day momentum gate adds nothing over an unconditional 3-day close reversal.
- F2 — Low-leg relevance: a low-regime-only twin (score `= MIN100 − close` when `trend <= 0.05`, else flat — same gate, grid, fills, Branch B removed) must not improve net expectancy; fail ⇒ the high-regime 3-day reversal leg adds nothing over the pure low-momentum distance book.
- F3 — Horizon relevance: a half-horizon twin (same construction at window 50 — `sma(close, 50)` momentum ratio with the same `0.05` threshold and `ts_min(close, 50)` distance leg, same `-delta(close, 3)` high leg, same book/grid/fills, 110-bar adopted warmup) must not improve net expectancy; fail ⇒ the 100-day horizon adds nothing over the same construction at half the scale, and the record is a horizon label rather than a horizon edge.

## Crypto portability

Pinned to BTCUSDT Binance USDT-M perpetual under the house overlay (declared port of a venue-free daily-equity formula). The rule reads completed daily bars only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (the paper's split/dividend close adjustment is a non-issue on crypto — disclosed, not modeled). The score mixes a dollar distance (Branch A) with a dollar change (Branch B) whose side alone trades — scale-free in direction, yet distance/change magnitudes differ across venues, disclosed without normalization to invent. The rule is two-sided overall with a short-or-flat low leg, so a spot-only deployment expresses only long-firing Branch B bars while every short-firing bar stays venue-gated (never silently converted) — a spot-only variant would be a different, unpinned claim. No warmup history beyond 210 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop: a grinding low-momentum selloff rides Branch A shorts sized at the full distance above a falling 100-day low, and a steep high-momentum trend fades every 3-day push via Branch B, both with no guardrail before the next regime print, by the carried-over paper design — the record's principal risk.
- Gate-boundary churn: the `trend == 0.05` neighbourhood flips the book between a distance leg and a reversal leg on slow-ratio noise — the paper provides no buffer band and this record invents none.
- Branch-A long impossibility: while `trend <= 0.05` the book can never go long by construction, so V-shaped recoveries that never lift the gate sit out the entire long side — disclosed structural asymmetry, not a bug fix.
- Three-bar close noise: Branch B is a raw 3-bar close difference with no smoothing — single-print spikes move the book, disclosed.
- 100-day-low staleness: a flat 100-day low struck months ago anchors Branch A size to ancient history — the paper provides no lookback decay and this record invents none.
- Single-venue port residual: paper-regime U.S. equities vs Binance perpetual execution (prints, fees, funding, close-definition, margin mechanics beyond the house model) is unclaimed, disclosed.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest.
- Author scope: the paper presents production formulaic alphas as research objects, not a vetted retail trading system — this record is research-only and claims no live suitability.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Kakushadze, Z., `101 Formulaic Alphas`, arXiv:1601.00991 (manuscript December 9, 2015 — Alpha#24 formula, A.1 operator definitions, A.2 daily price/volume inputs, §2 delay-1 definition with footnote-11 delay-0 exclusion, §2 Alpha#101 direction worked example — key passages re-verified via PDF text extraction 2026-10-16): https://arxiv.org/abs/1601.00991
- Same paper, PDF (formula appendix, operator/input definitions, empirical sections — read 2026-10-16): https://arxiv.org/pdf/1601.00991
- OctopusTakopi `toraniko-alpha101` (independent audited implementation — `alpha024` at `toraniko/alpha101.py` lines 339–341, `delay` at lines 74–79, `delta` at lines 81–82, `sma` at lines 100–101, `ts_min` at lines 108–109, `_safe_div` at lines 185–190, `_if_else` at lines 192–199, neutralization manifest covering other alphas but never #24 — pinned to commit `4fc0627d2a720fd8d583708ef051b9d48d98aacd`, verified live 2026-10-16): https://github.com/OctopusTakopi/toraniko-alpha101
