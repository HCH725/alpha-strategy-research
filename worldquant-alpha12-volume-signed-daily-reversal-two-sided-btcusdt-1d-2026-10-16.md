---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: WorldQuant Alpha12 volume-change-signed daily reversal two-sided on BTCUSDT 1d bars
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

# WorldQuant Alpha12 volume-change-signed daily reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read end to end during this cycle (2026-10-16), pinned:

- Paper (local text extraction of the arXiv PDF, read end to end this cycle): `Zura Kakushadze`, `101 Formulaic Alphas`, arXiv `1601.00991` (manuscript dated `December 9, 2015` — record `source_as_of` is that manuscript date, never a fetch date; the paper states the formulas `are also computer code` once the Subsection A.2 operators are defined). Alpha#12 prints in Appendix A.1 as `(sign(delta(volume, 1)) * (-1 * delta(close, 1)))`. Operator pins from the paper's own definitions section: `sign(x) = standard definitions`; `delta(x, d) = today's value of x minus the value of x d days ago`; `delay(x, d) = value of x d days ago`; inputs `open, close, high, low, volume = standard definitions for daily price and volume data`. Timing pin from §2: `delay-1 means that the alpha is traded on the day subsequent to the date of the most recent data used in computing it` (e.g. traded today `starting at the open` on yesterday's data); footnote 11 names exactly four delay-0 alphas (`42, 48, 53 and 54`, traded at the close of the computed day) — Alpha#12 is not among them, so it is delay-1 by the paper's own exclusion. Direction pin from the §2 worked example: `Alpha#101 ... is a delay-1 momentum alpha: if the stock runs up intraday (i.e., close > open and high > low), the next day one takes a long position` — a positive score maps to long, a negative score to short (see Negative evidence 1 for the exact strength of this pin).
- Audited pinned implementation (fetched live this cycle, verified byte-identical to the local audit copy): repository `https://github.com/OctopusTakopi/toraniko-alpha101`, head commit `4fc0627d2a720fd8d583708ef051b9d48d98aacd` (2026-07-17, `Fix Alpha101 report correctness`, verified via the GitHub commits API this cycle), exact file `toraniko/alpha101.py`: `def alpha012` returns `np.sign(delta(self.volume, 1)) * -delta(self.close, 1)` (lines 288–289); `def delta` is `x - delay(x, period)` with `def delay` emitting the value shifted by the lookback (lines 74–82, first row undefined by construction). Operator-convention evidence from the pinned test suite `toraniko/tests/test_alpha101.py` (same commit): full-window warmup emits undefined values before the window is full (`test_correlation_uses_full_trailing_window`), a defined window with zero variance reads as zero rather than undefined (`test_correlation_of_constant_defined_window_is_zero`), fractional lookbacks truncate by floor (`test_fractional_windows_use_paper_floor_rule`), and conditional alphas emit no signal before warmup (`test_conditional_alphas_do_not_emit_signals_before_warmup`). Alpha#12 needs no floor, no window, and no zero-variance branch of its own: after the 1-day deltas exist every input is finite and `sign(0) = 0` is standard.

Licence and rights: the paper is a public arXiv preprint; the implementation is public research software. This record cites and normalizes the rule (single-line formula and operator definitions only for gate evidence) and reproduces no source block beyond single-line facts.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the paper. The paper prints the Alpha#12 formula, the operator definitions, the delay-1 timing class, and the positive-score→long convention, but ships no venue, no symbol, no single-asset side mapping (its own evaluation is cross-sectional quintile), no order/fill semantics, no warmup seed, and no risk leg. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` Binance USDT-M perpetual `1d` (the paper is daily U.S. equities with no venue — frame/venue pin disclosed, never a source claim; perpetual is the minimal realistic venue because the short leg needs margin); (2) completed-bar decisions with next-bar-open market fills (the paper trades delay-1 `starting at the open` on the subsequent day — deviation class identical to the admitted caporale-plastun and ehlers-cg records' bar-port, disclosed, never an advantage claim); (3) an adopted 5-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 2nd completed bar — one prior bar feeds both 1-day deltas — plus margin; see Required data); (4) house sizing/costs with modeled funding while held (the paper ships no sizing, capital, fee, or slippage concept — never presented as source-native behavior). The `sign(delta(volume,1)) × (−delta(close,1))` formula, the `sign(0) = 0` flat tie, the delay-1 next-day execution, the positive→long / negative→short mapping, the reversal-only exits, and the no-stop/no-target risk posture are source-grounded and unmodified.

Pre-write dedup (2026-10-16): working-tree case-insensitive searches for `worldquant`, `kakushadze`, `1601.00991`, `alpha012`, `alpha#12`, `sign(delta(volume`, and `delta(volume, 1)` return zero strategy records — no admitted rule uses this source, author, paper, formula, or operator construction. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Closed-reviewer precedents (#6 WaveTrend tie semantics, #10 golden-cross spot/short, #17 MACD-hist seeding, #20 Ichimoku-RSI always-in-market funding) are different rules. This is a new family (first WorldQuant-101 record in the pool), not a parameter variant.

## Economic mechanism

### Source-reported

Mixed mean-reversion/momentum building blocks gated by volume change. The paper frames its universe coarsely: `one can think of alpha signals as based on mean-reversion or momentum`, where `a mean-reversion alpha has a sign opposite to the return on which it is based`, and adds that `in complex alphas elements of mean-reversion and momentum can be mixed`. Alpha#12 is such a mix in one line: when volume expands day over day (`sign(delta(volume,1)) = +1`), the score is the contrarian daily move (`−delta(close,1)` — long the down day, short the up day, fading the volume-backed move); when volume contracts (`sign = −1`), the double negation turns the score into the raw daily move (`+delta(close,1)` — long the up day, short the down day, following the thin move). The paper ships no behavioural, structural, or risk-premium mechanism beyond this measurement construction, and no stop, target, or risk leg of any kind.

### Research interpretation

Volume-gated daily reversal switch, two-sided. Unlike unconditional fade records (connors-rsi2, lehmann-weekly, three-down-three-up, eight-day-run — fades armed by streaks, extremes, or oscillators with no volume vote), the reversal here only fires against volume-backed moves and flips into continuation when the move printed on shrinking volume — the volume-change sign is the entire gate, and there is no streak window, no oscillator, and no threshold anywhere. Unlike volume-flow oscillators (obv-ema, pvo-signal-cross, cmf-velocity, klinger, force-index, mfi — accumulated or smoothed transforms of volume and price), nothing accumulates: the score is a 1-day bilinear product recomputed from two closes and two volumes, with no average, no ranking, and no memory beyond one bar. Unlike the ehlers-correlation-trend record (rolling correlation of closes against a deterministic ramp), no window statistic is ever computed. The failure mode is plain: a volume-backed trend day is faded in full size with no guardrail, and a volume number that stutters sign day to day whipsaws the book long-short with the reversal as the only exit — disclosed, not upgraded.

## Signal

Exact rule as pinned (any other lookback, gate, threshold, fill, frame, book, or tie treatment is a different, unpinned rule):

- Inputs (paper A.3): `close[t]`, `volume[t]` on completed `1d` bars. No `open`, no `high`, no `low`, no vwap/adv/sector, no cross-sectional rank, no second asset or timeframe is read by any order-gating line.
- Deltas (paper A.2, pinned impl lines 74–82): `dC[t] = close[t] − close[t−1]`; `dV[t] = volume[t] − volume[t−1]`. Both are undefined on the first bar (no prior bar) and finite on every later bar.
- Score (paper Appendix A.1, pinned impl lines 288–289): `score[t] = sign(dV[t]) × (−dC[t])`, with `sign` the standard definition (`sign(0) = 0`). No division, no window, no floor, no zero-variance branch exists anywhere in this formula.
- Direction mapping (source-grounded, fenced in Negative evidence 1): `score[t] > 0` → long signal; `score[t] < 0` → short signal; `score[t] == 0` → flat signal (exact-zero prints when the close or the volume prints unchanged to the tick — deterministic flat, never a held conviction). The entry fills at the next bar's open, one single unit, only if the book does not already carry that side (see position rule).
- Exit: the first opposite signal reverses the full unit in one step (close plus opposite entry at the same next-bar-open fill); a zero print flattens the full unit at the next open — reversal-or-flatten is the sole exit path by construction. No stop-loss, no take-profit, no trailing, no time exit (the paper ships no risk leg — carried over exactly, disclosed in Provenance adaptation (4), never upgraded into a source claim).
- Direction: two-sided (long leg and short leg are both native). Shorts are native to USDT-M margin (no uptick rule, no borrow desk).
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further long-signal bars as no-ops (no pyramiding, no averaging), and symmetrically for shorts. Re-entry re-arms on the next opposite or flat-exit signal only (no cooldown specified — explicitly none, not invented). Pre-first-signal bars are flat.

## Required data

- Completed `1d` bars of BTCUSDT: `close` and `volume` only (both deltas' inputs). No `open`, no `high`, no `low`, no funding-signal, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line. The `volume` read is the kline's printed base-asset volume as-is — no dollar-volume normalization exists in this formula (no `adv` term), so no quote conversion is modeled.
- Single decision timeframe `1d` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; both deltas read the same series one bar back, never a second feed).
- Warmup: 5 completed `1d` bars flat by record rule — structural minimum is the 2nd completed bar (both 1-day deltas need exactly one prior bar), plus margin per the admitted balance-of-power precedent. Pre-warmup bars are flat by record rule; missing bars are skipped on available completed bars only — prices and volumes are never fabricated. No repainting (deltas read completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance USDT-M perpetual under the house overlay (researcher choice — the paper names no venue and evaluates U.S. equities; no source-market equivalence is claimed; perpetual is the minimal realistic venue because the short leg needs margin).
- Order timing (paper-grounded derivation): completed-bar decision with next-bar-open market fills for entries, reversals, and flat-exits — the paper's delay-1 class trades `on the day subsequent to the date of the most recent data`, `starting at the open`, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) on the same verified primitive as the admitted caporale-plastun and ehlers-cg records' entries (verified this cycle's base). This record claims no other fill convention: no perfect-open print, no maker-touch, no intrabar-path-dependent fill.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing orders by record rule. No hidden Hummingbot stop-order defaults are relied upon, and with no stop/limit legs there is no same-bar TP/SL ordering ambiguity.
- Sizing/capital/costs: the paper ships no sizing, capital, fee, or slippage concept. The explicit house overlay (single-unit frame, pinned house taker fees both legs, modeled funding while held) applies to the derived evaluation here, never presented as source-native behavior. Funding is never zero-claimed: two-sided holds span the `00:00`/`08:00`/`16:00 UTC` funding stamps, so every held bar carries modeled funding.
- Concurrency: at most one single-asset engine position at any time; an opposite signal closes-and-reverses in one step and a zero signal closes-to-flat. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (arXiv 1601.00991 text, read end to end this cycle): the `are also computer code` formula status; the Alpha#12 line `(sign(delta(volume, 1)) * (-1 * delta(close, 1)))`; the A.2 operator definitions (`sign`, `delta`, `delay`, standard daily price/volume inputs); the §2 delay-1 definition and the footnote-11 delay-0 exclusion list (`42, 48, 53, 54` — Alpha#12 absent, hence delay-1); the §2 mixed building-block framing; the §2 Alpha#101 worked example pinning positive-score→long. With exact implementation provenance (pinned commit `4fc0627d`, file `toraniko/alpha101.py` lines 74–82 and 288–289, plus the named operator-convention tests): the executable delta/delay/sign semantics and the undefined-before-warmup convention. This record claims no source-reported performance number of any kind — no return, no win rate, no trade count, no per-alpha table figure is carried into the derived specification — and no reproduced performance exists.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Direction words fenced, admitted plainly: the paper never prints `buy`, `sell`, `long`, or `short` for Alpha#12. The positive→long / negative→short mapping rests on the §2 Alpha#101 worked example (a positive intraday score takes `a long position` the next day) together with the implementation report's long-top-quintile / short-bottom-quintile construction — not on any order verb attached to Alpha#12 itself. A reviewer must not graft any other direction convention onto this record.
2. Timeframe and venue fenced: the paper is daily U.S. equities and names no venue. `1d` BTCUSDT-perpetual is the disclosed researcher pin (Provenance adaptation (1)); a reviewer must not cite the paper as evidence for any frame or venue.
3. Risk silence fenced: the paper contains no stop, target, trailing, time exit, or risk paragraph for Alpha#12 — the no-guardrail posture is carried over exactly, never upgraded, never presented as a tested safety choice.
4. Cross-sectional machinery fenced: the paper's own evaluation ranks scores across thousands of stocks and industry-neutralizes many alphas. Alpha#12's formula contains no `rank(`, no `IndNeutralize`, no `scale(`, no `vwap`, no `adv`, and no sector/industry term (verified by programmatic filter over all 101 lines this cycle) — the single-asset sign map drops the cross-sectional portfolio layer entirely, disclosed as adaptation, never presented as the paper's traded portfolio.
5. Exact-zero determinism fenced: `score[t] == 0` requires `close[t] == close[t−1]` or `volume[t] == volume[t−1]` to the tick. The flat treatment is a predeclared record rule (total and mutually exclusive with the long/short branches), not a paper sentence — without it the zero print would be ambiguous, so it is pinned here rather than left to the reviewer.
6. Overlap fences, admitted plainly: pool `balance-of-power-cross` trades the single-bar body-to-range ratio `(close−open)/(high−low)` against fixed ±0.8 threshold crosses (range-normalized pressure with rails — this record reads no range, no open/high/low, and has no threshold); pool `connors-rsi2`/`lehmann-weekly`/`three-down-three-up`/`eight-day-run` fade streaks or oscillator extremes with no volume vote (this record's gate is the volume-change sign, never a streak); pool `obv-ema`/`pvo`/`cmf`/`klinger`/`force-index`/`mfi` accumulate or smooth volume-price interaction (this record has no accumulation, no average, no ranking — a 1-day product); pool `ehlers-correlation-trend` correlates closes against a deterministic ramp (different second series, windowed statistic — this record computes no statistic); pool `turtle-soup`/`donchian` fade range breakouts (different event). Shared `reversal`/`volume`/`delta` vocabulary is not shared signal.
7. No hidden variants admitted: any other lookback, any smoothed or ranked volume gate, any threshold, any stop/target/filter/cooldown, any other frame, fill, venue, or book is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `sign(delta(volume,1)) × (−delta(close,1))` / standard sign with zero-flat / two-sided / delay-1 next-open fills / no-stop posture / `1d` BTCUSDT perpetual are frozen.

- F1 — Volume-gate relevance: an unconditional-fade twin (score `= −delta(close,1)`, ignoring the volume sign — same book, grid, fills) must not improve net expectancy; fail ⇒ the volume-change gate adds nothing over a plain daily fade.
- F2 — Direction-mapping relevance: a fade twin (short on positive score, long on negative score — same formula, grid, fills, and reversal book) must not improve net expectancy; fail ⇒ the paper's positive→long mapping adds nothing over fading the signal on this market.
- F3 — Horizon relevance: a weekly twin (`sign(delta(volume,5)) × (−delta(close,5))` — same construction at a 5-day horizon with a 6-bar adopted warmup) must not improve net expectancy; fail ⇒ the 1-day horizon adds nothing over the same construction at weekly scale, and the record is a horizon label rather than a horizon edge.

## Crypto portability

Pinned to BTCUSDT Binance USDT-M perpetual under the house overlay (declared port of a venue-free daily-equity formula). The rule reads completed daily bars only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (the paper's split/dividend close adjustment is a non-issue on crypto — disclosed, not modeled). The score is scale-free in price (a sign times a price difference whose side alone trades) yet volume-scale behavior differs across venues — the volume read is the kline print as-is with no normalization to invent. The rule is two-sided, so a spot-only deployment expresses only long-firing bars while short-firing bars stay venue-gated (never silently converted) — a spot-only variant would be a different, unpinned claim. No warmup history beyond 5 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop: adverse excursion after a volume-backed fade has no guardrail before the opposite signal, by the carried-over paper design — the record's principal risk.
- Whipsaw switch exposure: in a market where the volume-change sign alternates daily, the book flips long-short on consecutive bars at the worst prints of each swing — the paper provides no filter and this record invents none.
- Thin-move trend risk: when volume contracts, the rule follows the daily move rather than fading it, so a low-volume drift is ridden, not faded — the mixed building-block character cuts both ways, disclosed.
- Exact-zero rarity note: the flat branch is near-unreachable on BTCUSDT (tick-exact unchanged close or volume) — the book is effectively always-in-market, disclosed.
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

- Kakushadze, Z., `101 Formulaic Alphas`, arXiv:1601.00991 (manuscript December 9, 2015 — Alpha#12 formula, A.2 operator definitions, A.3 daily price/volume inputs, §2 delay-1 definition with footnote-11 delay-0 exclusion, §2 Alpha#101 direction worked example — read end to end via text extraction 2026-10-16): https://arxiv.org/abs/1601.00991
- Same paper, PDF (formula appendix, operator/input definitions, empirical sections — read 2026-10-16): https://arxiv.org/pdf/1601.00991
- OctopusTakopi `toraniko-alpha101` (independent audited implementation — `alpha012` at `toraniko/alpha101.py` lines 288–289, `delay`/`delta` at lines 74–82, operator-convention tests in `toraniko/tests/test_alpha101.py` — pinned to commit `4fc0627d2a720fd8d583708ef051b9d48d98aacd`, verified live 2026-10-16): https://github.com/OctopusTakopi/toraniko-alpha101
