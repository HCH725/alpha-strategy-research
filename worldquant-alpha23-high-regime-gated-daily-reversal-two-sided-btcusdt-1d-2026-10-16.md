---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: WorldQuant Alpha23 high-regime-gated daily reversal two-sided on BTCUSDT 1d bars
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

# WorldQuant Alpha23 high-regime-gated daily reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read and re-verified end to end during this cycle (2026-10-16), pinned:

- Paper (local text extraction of the arXiv PDF, key passages re-verified this cycle): `Zura Kakushadze`, `101 Formulaic Alphas`, arXiv `1601.00991` (manuscript dated `December 9, 2015` — record `source_as_of` is that manuscript date, never a fetch date; the paper states the formulas `are also computer code` once the operators are defined). Alpha#23 prints in Appendix A.1 as `(((sum(high, 20) / 20) < high) ? (-1 * delta(high, 2)) : 0)`. Operator pins from the paper's own definitions section: `delay(x, d) = value of x d days ago`; `delta(x, d) = today's value of x minus the value of x d days ago`; inputs `open, close, high, low, volume = standard definitions for daily price and volume data`. Timing pin from §2: `delay-1 means that the alpha is traded on the day subsequent to the date of the most recent data used in computing it` (e.g. traded today `starting at the open`); footnote 11 names exactly four delay-0 alphas (`42, 48, 53 and 54`, traded at or as close as possible to the close of the computed day) — Alpha#23 is not among them, so it is delay-1 by the paper's own exclusion. Direction pin from the §2 worked example: `Alpha#101 ... is a delay-1 momentum alpha: if the stock runs up intraday (i.e., close > open and high > low), the next day one takes a long position` — a positive score maps to long, a negative score to short (see Negative evidence 1 for the exact strength of this pin).
- Audited pinned implementation (fetched live this cycle, verified byte-identical to the local audit copy, sha256 `b54a820ca35fc06359f023cb590015ff4d4cd818c077322d587dc4e9cbf70316`): repository `https://github.com/OctopusTakopi/toraniko-alpha101`, head commit `4fc0627d2a720fd8d583708ef051b9d48d98aacd` (2026-07-17, `Fix Alpha101 report correctness`, confirmed still the repository head via the GitHub commits API this cycle), exact file `toraniko/alpha101.py`: `def alpha023` computes `mean_high = sma(self.high, 20)` then `_if_else(mean_high < self.high, -delta(self.high, 2), 0.0, mean_high, self.high)` (lines 335–337, matching the printed ternary branch order); `def delta` is `x - delay(x, period)` (lines 81–82, undefined before the 3rd bar by construction); `def sma` is a full-window trailing mean (lines 100–101, undefined before the 20th bar — no partial-window seeding); `_if_else` preserves undefined condition inputs as undefined rather than guessing a branch (lines 192–199). The pinned neutralization manifest covers other alphas (48, 58, 59, 63, 67, 69, 70, 76, 79, 80, 82, 87, 89, 90, 91, 93, 97, 100) — never #23, so Alpha#23 needs no sector/industry/subindustry class. Alpha#23 needs no rank, no scale, no adv, no vwap, no division of any kind, and no threshold beyond the single printed strict comparison: every input is finite once the 20-bar high window exists, and an exact-zero print is a deterministic flat.

Licence and rights: the paper is a public arXiv preprint; the implementation is public research software. This record cites and normalizes the rule (single-line formula and operator definitions only for gate evidence) and reproduces no source block beyond single-line facts.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the paper. The paper prints the Alpha#23 formula, the operator definitions, the delay-1 timing class, and the positive-score→long convention, but ships no venue, no symbol, no single-asset side mapping (its own evaluation is cross-sectional quintile), no order/fill semantics, no warmup seed, and no risk leg. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` Binance USDT-M perpetual `1d` (the paper is daily U.S. equities with no venue — frame/venue pin disclosed, never a source claim; perpetual is the minimal realistic venue because the short leg needs margin); (2) completed-bar decisions with next-bar-open market fills (the paper trades delay-1 `on the day subsequent to the date of the most recent data`, `starting at the open` — deviation class identical to the admitted caporale-plastun, ehlers-cg, worldquant-alpha6, worldquant-alpha9, and worldquant-alpha12 records' bar-port, disclosed, never an advantage claim); (3) an adopted 25-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 20th completed bar — the 20-bar high mean needs 20 closes and the 2-bar high change needs 3, pinned by the operator code above — plus margin; see Required data); (4) house sizing/costs with modeled funding while held (the paper ships no sizing, capital, fee, or slippage concept — never presented as source-native behavior). The level gate, the strict comparison, the negated 2-bar high-change payoff, the explicit zero flat regime, the delay-1 next-day execution, the positive→long / negative→short mapping, the reversal-or-flatten exits, and the no-stop/no-target risk posture are source-grounded and unmodified.

Pre-write dedup (2026-10-16): working-tree case-insensitive searches for `worldquant`, `kakushadze`, `1601.00991`, `alpha023`, `alpha#23`, and `sum(high, 20)` return zero strategy records except the siblings `worldquant-alpha6` (negated 10-day open-volume correlation statistic — no level gate, no high series), `worldquant-alpha12` (volume-change-signed 1-day close product — a same-bar companion-series gate, never a level gate), and `worldquant-alpha9` (5-bar delta-sign streak ternary on closes — a sign-purity gate, never a level gate, see Negative evidence 6). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long — EMA-channel object, long-only), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Closed-reviewer precedents (#6 WaveTrend tie semantics, #10 golden-cross spot/short, #17 MACD-hist seeding, #20 Ichimoku-RSI always-in-market funding) are different rules. This is the fourth WorldQuant-101 record in the pool family, not a parameter variant of any admitted rule.

## Economic mechanism

### Source-reported

Coarse mean-reversion/momentum building blocks. The paper frames its universe coarsely: `one can think of alpha signals as based on mean-reversion or momentum`, where `a mean-reversion alpha has a sign opposite to the return on which it is based`. Alpha#23 is a level-gated mean-reversion block: only when the current high prints above its own trailing 20-bar average does the book take the opposite side of the trailing 2-bar high change; below that level the score is exactly zero. The paper ships no behavioural, structural, or risk-premium mechanism beyond this measurement construction, and no stop, target, or risk leg of any kind.

### Research interpretation

High-regime-gated 2-bar reversal, two-sided, with an explicit flat regime. The gate (`high > SMA20(high)`) is a level object — a price-against-its-own-average comparison — while the payoff (`−delta(high, 2)`) is a change object; the two never share a series role. Unlike the sibling worldquant-alpha9 record (whose gate is the sign purity of the close-change history itself, always-in-market), this rule stands down completely whenever highs sit at or below their 20-bar average — the flat regime is source-printed (`: 0`), not a researcher invention. Unlike the sibling worldquant-alpha12 record (whose reversal leg is gated by the sign of the 1-day volume change — a same-bar companion-series gate), this rule never reads volume. Unlike the pool `donchian-20-10` record (rolling highest-high/lowest-low extremes — a memory-of-extrema object with a 10-bar trailing exit), nothing here remembers extremes and there are no legs — the gate is a mean, and the exit is the next signal. The failure mode is plain: highs oscillating around their own average whipsaw the book between the reversal leg and flat, while the 2-bar high change itself is raw noise — disclosed, not upgraded.

## Signal

Exact rule as pinned (any other window, series, comparison, fill, frame, book, or tie treatment is a different, unpinned rule):

- Inputs (paper A.2): `high[t]` on completed `1d` bars only. No `open`, no `close`, no `low`, no `volume`, no vwap/adv/sector, no cross-sectional rank, no second asset or timeframe is read by any order-gating line.
- Level gate (paper Appendix A.1, pinned impl lines 335–337): `avg[t] = sum(high, 20)[t] / 20` — full-window trailing mean, undefined before the 20th completed bar, never seeded or backfilled.
- Payoff (paper A.1, pinned impl lines 81–82, 335–337): `d[t] = delta(high, 2)[t] = high[t] − high[t−2]`. Undefined before the 3rd completed bar by construction.
- Score (paper Appendix A.1, pinned impl lines 335–337, branch order source-printed): `score[t] = −d[t]` if `avg[t] < high[t]` (high above its own 20-bar average — both signs possible); else `score[t] = 0.0` (at-or-below-average regime — deterministic flat, never a held conviction). No division, no rank, no scale, no floor, no threshold beyond the single printed strict comparison exists anywhere in this formula.
- Direction mapping (source-grounded, fenced in Negative evidence 1): `score[t] > 0` → long signal; `score[t] < 0` → short signal; `score[t] == 0` → flat signal. The entry fills at the next bar's open, one single unit, only if the book does not already carry that side (see position rule).
- Exit: the first opposite signal reverses the full unit in one step (close plus opposite entry at the same next-bar-open fill); a zero print flattens the full unit at the next open — reversal-or-flatten is the sole exit path by construction. No stop-loss, no take-profit, no trailing, no time exit (the paper ships no risk leg — carried over exactly, disclosed in Provenance adaptation (4), never upgraded into a source claim).
- Direction: two-sided (long leg and short leg are both native). Shorts are native to USDT-M margin (no uptick rule, no borrow desk).
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further long-signal bars as no-ops (no pyramiding, no averaging), and symmetrically for shorts; flat-regime bars while already flat are no-ops. Re-entry re-arms on the next opposite or flat-exit signal only (no cooldown specified — explicitly none, not invented). Pre-first-signal bars are flat.

## Required data

- Completed `1d` bars of BTCUSDT: `high` only (the sole series the formula reads). No `open`/`close`/`low`/`volume`, no funding-signal, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; the gate and the payoff read the same single series, never a second feed).
- Warmup: 25 completed `1d` bars flat by record rule — structural minimum is the 20th completed bar (the 20-bar high mean needs 20 completed highs per the full-window `sma` code; the 2-bar change needs 3 — pinned by operator code, not by a test sentence), plus margin per the admitted balance-of-power precedent. Pre-warmup bars are flat by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (gate and payoff read completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance USDT-M perpetual under the house overlay (researcher choice — the paper names no venue and evaluates U.S. equities; no source-market equivalence is claimed; perpetual is the minimal realistic venue because the short leg needs margin).
- Order timing (paper-grounded derivation): completed-bar decision with next-bar-open market fills for entries, reversals, and flat-exits — the paper's delay-1 class trades `on the day subsequent to the date of the most recent data`, `starting at the open`, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) on the same verified primitive as the admitted caporale-plastun, ehlers-cg, worldquant-alpha6, worldquant-alpha9, and worldquant-alpha12 records' entries (verified this cycle's base). This record claims no other fill convention: no perfect-open print, no maker-touch, no intrabar-path-dependent fill.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing orders by record rule. No hidden Hummingbot stop-order defaults are relied upon, and with no stop/limit legs there is no same-bar TP/SL ordering ambiguity.
- Sizing/capital/costs: the paper ships no sizing, capital, fee, or slippage concept. The explicit house overlay (single-unit frame, pinned house taker fees both legs, modeled funding while held) applies to the derived evaluation here, never presented as source-native behavior. Funding is never zero-claimed: two-sided holds span the `00:00`/`08:00`/`16:00 UTC` funding stamps, so every held bar carries modeled funding.
- Concurrency: at most one single-asset engine position at any time; an opposite signal closes-and-reverses in one step and a zero signal closes-to-flat. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (arXiv 1601.00991 text, key passages re-verified this cycle): the `are also computer code` formula status; the Alpha#23 line `(((sum(high, 20) / 20) < high) ? (-1 * delta(high, 2)) : 0)`; the A.1 operator definitions (`delay(x, d)`, `delta(x, d)`, `abs/log/sign` standards); the A.2 input definitions (`open, close, high, low, volume = standard definitions for daily price and volume data`); the §2 delay-1 definition and the footnote-11 delay-0 exclusion list (`42, 48, 53 and 54` — Alpha#23 absent, hence delay-1); the §2 mixed building-block framing; the §2 Alpha#101 worked example pinning positive-score→long. With exact implementation provenance (pinned commit `4fc0627d`, file `toraniko/alpha101.py` lines 81–82, 100–101, 192–199, and 335–337, plus the neutralization manifest in `toraniko/tests/test_alpha101.py` covering other alphas but never #23): the executable mean-gate/change-payoff/conditional semantics, the full-window-undefined convention, the undefined-preserving conditional, and the 20th-bar first-signal convention. This record claims no source-reported performance number of any kind — no return, no win rate, no trade count, no per-alpha table figure is carried into the derived specification — and no reproduced performance exists.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Direction words fenced, admitted plainly: the paper never prints `buy`, `sell`, `long`, or `short` for Alpha#23. The positive→long / negative→short mapping rests on the §2 Alpha#101 worked example (a positive intraday score takes `a long position` the next day) together with the implementation report's long-top-quintile / short-bottom-quintile construction — not on any order verb attached to Alpha#23 itself. A reviewer must not graft any other direction convention onto this record.
2. Timeframe and venue fenced: the paper is daily U.S. equities and names no venue. `1d` BTCUSDT-perpetual is the disclosed researcher pin (Provenance adaptation (1)); a reviewer must not cite the paper as evidence for any frame or venue.
3. Risk silence fenced: the paper contains no stop, target, trailing, time exit, or risk paragraph for Alpha#23 — the no-guardrail posture is carried over exactly, never upgraded, never presented as a tested safety choice.
4. Cross-sectional machinery fenced: the paper's own evaluation ranks scores across thousands of stocks and industry-neutralizes many alphas. Alpha#23's formula contains no `rank(`, no `IndNeutralize`, no `scale(`, no `vwap`, no `adv`, no division, and no sector/industry term (verified by programmatic filter over all 101 lines this cycle; the pinned neutralization manifest covers other alphas, never #23) — the single-asset sign map drops the cross-sectional portfolio layer entirely, disclosed as adaptation, never presented as the paper's traded portfolio.
5. Exact-zero determinism fenced: `score[t] == 0` fires either when the gate is false (at-or-below-average regime — structural flat) or when the gated 2-bar high change prints exactly zero. Both are predeclared record-rule flats (total and mutually exclusive with the long/short branches), not paper sentences — without them the zero prints would be ambiguous, so they are pinned here rather than left to the reviewer.
6. Overlap fences, admitted plainly: sibling `worldquant-alpha9` gates on 5-bar delta-sign purity with an always-in-market book (a history-purity object — this record has no streak window and stands flat half the time); sibling `worldquant-alpha12` trades a volume-change-signed 1-day close product (a same-bar companion-series gate — this record never reads volume); sibling `worldquant-alpha6` trades a negated 10-day open-volume correlation (a two-series window statistic — no gate, no payoff split); pool `donchian-20-10` breaks rolling 20-bar highest-high/lowest-low extremes with a 10-bar trailing exit (a memory-of-extrema object with exit legs — this record's gate is a mean and it has no legs); pool `three-down-three-up` counts strict close chains long-only on 1h (a trigger, never a level-gated reversal book); open PR #48 streak-gates a 3-EMA channel long-only (an average-channel object with a chain gate, never a level-vs-mean comparison). Shared `high`/`average`/`reversal` vocabulary is not shared signal.
7. Twins fenced: the paper's Alpha#46/#49/#51 family trades the same 20/10-day close-slope quantity at different thresholds (a slope object on closes — never a high level gate); none is substituted here. A reviewer must not swap any other alpha's window, series, threshold, or branch into this record.
8. No hidden variants admitted: any other window, any other series, any other comparison direction or payoff, any threshold, any stop/target/filter/cooldown, any other frame, fill, venue, or book is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 20-bar high mean gate / strict comparison / negated 2-bar high-change payoff / explicit zero flat / two-sided / delay-1 next-open fills / no-stop posture / `1d` BTCUSDT perpetual are frozen.

- F1 — Gate relevance: an always-on twin (score `= −delta(high, 2)` every bar — same payoff, grid, fills, no gate) must not improve net expectancy; fail ⇒ the 20-bar high level gate adds nothing over an unconditional 2-bar high reversal.
- F2 — Payoff relevance: a displacement twin (score `= sign(high − SMA20(high))`, i.e. trade the level gate itself as a breakout book — same gate, grid, fills) must not improve net expectancy; fail ⇒ the 2-bar reversal payoff adds nothing over trading the gate as a trend-following displacement.
- F3 — Horizon relevance: a long-window twin (same construction at window 40 with a 45-bar adopted warmup — same gate object, same payoff form, same book, grid, fills) must not improve net expectancy; fail ⇒ the 20-bar horizon adds nothing over the same construction at twice the scale, and the record is a horizon label rather than a horizon edge.

## Crypto portability

Pinned to BTCUSDT Binance USDT-M perpetual under the house overlay (declared port of a venue-free daily-equity formula). The rule reads completed daily bars only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (the paper's split/dividend close adjustment is a non-issue on crypto — disclosed, not modeled). The score is a dollar high-change whose side alone trades — scale-free in direction, yet high-change magnitudes differ across venues, disclosed without normalization to invent. The rule is two-sided, so a spot-only deployment expresses only long-firing bars while short-firing bars stay venue-gated (never silently converted) — a spot-only variant would be a different, unpinned claim. No warmup history beyond 25 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop: an above-average regime rides waterfalls and melt-ups with no guardrail before the first at-or-below-average print, by the carried-over paper design — the record's principal risk.
- Gate-boundary churn: highs oscillating around their own 20-bar average flip the book between the reversal leg and flat on level noise — the paper provides no buffer band and this record invents none.
- Two-bar high noise: the payoff is a raw 2-bar high difference with no smoothing — single-print wicks move the book, disclosed.
- Flat-regime opportunity cost: below-average stretches hold no position at all — the book sits out trends that never lift highs above their average, disclosed.
- Single-venue port residual: paper-regime U.S. equities vs Binance perpetual execution (prints, fees, funding, high-definition, margin mechanics beyond the house model) is unclaimed, disclosed.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest.
- Author scope: the paper presents production formulaic alphas as research objects, not a vetted retail trading system — this record is research-only and claims no live suitability.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Kakushadze, Z., `101 Formulaic Alphas`, arXiv:1601.00991 (manuscript December 9, 2015 — Alpha#23 formula, A.1 operator definitions, A.2 daily price/volume inputs, §2 delay-1 definition with footnote-11 delay-0 exclusion, §2 Alpha#101 direction worked example — key passages re-verified via text extraction 2026-10-16): https://arxiv.org/abs/1601.00991
- Same paper, PDF (formula appendix, operator/input definitions, empirical sections — read 2026-10-16): https://arxiv.org/pdf/1601.00991
- OctopusTakopi `toraniko-alpha101` (independent audited implementation — `alpha023` at `toraniko/alpha101.py` lines 335–337, `delta` at lines 81–82, `sma` at lines 100–101, `_if_else` at lines 192–199, neutralization manifest in `toraniko/tests/test_alpha101.py` — pinned to commit `4fc0627d2a720fd8d583708ef051b9d48d98aacd`, verified live 2026-10-16): https://github.com/OctopusTakopi/toraniko-alpha101
