---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: WorldQuant Alpha101 intraday range-normalized momentum two-sided on BTCUSDT 1d bars
created: 2026-10-17
updated: 2026-10-17
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

# WorldQuant Alpha101 intraday range-normalized momentum two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read end to end during this cycle (2026-10-17), pinned:

- Paper (live-fetch arXiv PDF this cycle, 22 pages / 47,293 chars extracted, sha256 `1f9c21afe32dcb3ee77b31548acdaea00451fbfa1c0ee10c907867bcc736fce9`): `Zura Kakushadze`, `101 Formulaic Alphas`, arXiv `1601.00991` (manuscript dated `December 9, 2015` — record `source_as_of` is that manuscript date, never a fetch date; the paper states the formulas `are also computer code` once the operators are defined). Alpha#101 prints in Appendix A as `((close - open) / ((high - low) + .001))`. Operator pins from the paper's own §A.1 Functions and Operators: `abs(x), log(x), sign(x) = standard definitions`, same for `+ - * / > < ==`; inputs `open, close, high, low, volume = standard definitions for daily price and volume data` (Alpha#101 reads no volume). Timing pin from §2: `delay-1 means that the alpha is traded on the day subsequent to the date of the most recent data used in computing it` (e.g. traded today `starting at the open`); footnote 11 names exactly four delay-0 alphas (`42, 48, 53 and 54`, traded at or as close as possible to the close) — Alpha#101 is not among them, so it is delay-1 by the paper's own exclusion. Direction pin from the §2 worked example, which is Alpha#101 itself: `Alpha#101 ... is a delay-1 momentum alpha: if the stock runs up intraday (i.e., close > open and high > low), the next day one takes a long position` — a positive score maps to long, a negative score to short (see Negative evidence 1 for the exact strength of this pin).
- Audited pinned implementation (fetched live this cycle, verified byte-identical to the local audit copy): repository `https://github.com/OctopusTakopi/toraniko-alpha101`, head commit `4fc0627d2a720fd8d583708ef051b9d48d98aacd` (confirmed still the repository head via the GitHub commits API this cycle), exact file `toraniko/alpha101.py`: `def alpha101` returns `_safe_div(self.close - self.open, self.high - self.low + 0.001)` (lines 730–731). The `+ 0.001` guard is printed in both the paper and the code, so the divisor is strictly positive on every valid bar (`high >= low` implies divisor `>= 0.001`) and the quotient is always finite for finite inputs — no NaN branch exists anywhere in this formula.

Licence and rights: the paper is a public arXiv preprint; the implementation is public research software. This record cites and normalizes the rule (single-line formula and operator definitions only for gate evidence) and reproduces no source block beyond single-line facts.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the paper. The paper prints the Alpha#101 formula, the operator/input definitions, the delay-1 timing class, and the positive-score→long convention, but ships no venue, no symbol, no single-asset side mapping (its own evaluation is cross-sectional), no order/fill semantics beyond the delay-1 open class, no warmup seed, and no risk leg. Researcher-declared adaptations are exactly four: (1) research market/timeframe `BTCUSDT` Binance USDT-M perpetual `1d` (the paper is daily U.S. equities with no venue — frame/venue pin disclosed, never a source claim; perpetual is the minimal realistic venue because the short leg needs margin); (2) completed-bar decisions with next-bar-open market fills (the paper's delay-1 class trades `on the day subsequent to the date of the most recent data`, `starting at the open` — deviation class identical to the admitted caporale-plastun, ehlers-cg, worldquant-alpha6 and worldquant-alpha12 records' bar-port, disclosed, never an advantage claim); (3) an adopted 5-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 1st completed bar — single-bar construction with zero delay/delta calls — plus margin per the admitted worldquant-alpha54 precedent; see Required data); (4) house sizing/costs with modeled funding while held (the paper ships no sizing, capital, fee, or slippage concept — never presented as source-native behavior). The range-normalized formula, the `+ 0.001` guard, the exact-zero flat tie, the delay-1 next-day execution, the positive→long / negative→short mapping, the reversal-or-flatten exits, and the no-stop/no-target risk posture are source-grounded and unmodified.

Pre-write dedup (2026-10-17): working-tree case-insensitive searches for `alpha101`, `alpha#101`, `alpha-101`, and the `(close - open) / ((high - low)` object return zero strategy records embodying this rule — the eight sibling `worldquant-alpha*` records cite the paper's Alpha#101 worked example only as their direction pin, never as their signal. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state reversal), and #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Closed-reviewer precedents (#6 WaveTrend tie semantics, #10 golden-cross spot/short, #17 MACD-hist seeding, #20 Ichimoku-RSI always-in-market funding) are different rules. This is the ninth WorldQuant-101 record in the pool family, not a parameter variant of any admitted rule.

## Economic mechanism

### Source-reported

Coarse mean-reversion/momentum building blocks. The paper frames its universe coarsely: `one can think of alpha signals as based on mean-reversion or momentum`, where `a mean-reversion alpha has a sign opposite to the return on which it is based`, and adds that `in complex alphas elements of mean-reversion and momentum can be mixed`. Alpha#101 is a single delay-1 momentum block in one line: the score is the bar's open-to-close move scaled by its own range. When the close prints above the open the score is positive; when below, negative. The paper ships no behavioural, structural, or risk-premium mechanism beyond this measurement construction, and no stop, target, or risk leg of any kind.

### Research interpretation

Single-bar intraday-momentum sign book, two-sided, threshold-free. Unlike sibling worldquant-alpha53 (a 9-bar change of a `(close - low)`-denominator close-location ratio, delay-0 same-close) and sibling worldquant-alpha54 (a delay-0 power-scaled level, short-flat only), this rule has no change, no lookback, no exponent, and no long-side amputation — every defined bar's sign trades on the next open. Unlike sibling worldquant-alpha12 (a volume-change-signed 1-day close product) this rule never reads volume; unlike sibling worldquant-alpha6 (a 10-day open-volume correlation) it has no window and no statistic. Unlike pool `cmf-velocity`/`chaikin-oscillator` (which divide `(close - low) - (high - close)` by `(high - low)` and then smooth or volume-weight into oscillator objects) this rule divides the plain `(close - open)` body by the range with the printed `+ 0.001` guard and trades the raw sign with no smoothing. Unlike pool caporale-plastun (a 30-day band-gated abnormal-return breakout scanned on 1h bars) there is no trailing band and no gate — the single bar alone decides. The failure mode is plain: a bar closing a tick above its open fires long into what may be pure noise, and a steadily trending tape pins the book to one side with no scaling and no guardrail — disclosed, not upgraded.

## Signal

Exact rule as pinned (any other series, divisor, guard, negation, threshold, fill, frame, book, or tie treatment is a different, unpinned rule):

- Inputs (paper A.2): `open[t]`, `high[t]`, `low[t]`, `close[t]` on completed `1d` bars. No `volume`, no vwap/adv/returns/market-cap/sector, no cross-sectional rank, no second asset or timeframe is read by any order-gating line.
- Score (paper Appendix A, pinned impl lines 730–731): `score[t] = (close[t] - open[t]) / ((high[t] - low[t]) + 0.001)` — same-bar construction. The divisor is strictly positive on every valid bar, so the score is always finite for finite inputs; `score[t] == 0` prints exactly when `close[t] == open[t]` (doji bar). Never seeded, never backfilled.
- Direction mapping (source-grounded, fenced in Negative evidence 1): `score[t] > 0` → long signal; `score[t] < 0` → short signal; `score[t] == 0` → flat signal (exact-zero doji print — deterministic flat, never a held conviction). The entry fills at the next bar's open, one single unit, only if the book does not already carry that side (see position rule).
- Exit: the first opposite signal reverses the full unit in one step (close plus opposite entry at the same next-bar-open fill); a zero print flattens the full unit at the next open — reversal-or-flatten is the sole exit path by construction. No stop-loss, no take-profit, no trailing, no time exit (the paper ships no risk leg — carried over exactly, disclosed in Provenance adaptation (4), never upgraded into a source claim).
- Direction: two-sided (long leg and short leg are both native). Shorts are native to USDT-M margin (no uptick rule, no borrow desk).
- Position rule (predeclared researcher pin): single-unit; an already-long book treats further long-signal bars as no-ops (no pyramiding, no averaging), and symmetrically for shorts; flat-regime bars while already flat are no-ops. Re-entry re-arms on the next opposite or flat-exit signal only (no cooldown specified — explicitly none, not invented). Pre-first-signal bars are flat.

## Required data

- Completed `1d` bars of BTCUSDT: `open`, `high`, `low`, `close` only (the score's four inputs). No `volume`, no funding-signal, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (no multi-timeframe call, no cross-sectional ranking — one asset, one frame; the score reads the same single bar, never a second feed).
- Warmup: 5 completed `1d` bars flat by record rule — structural minimum is the 1st completed bar (single-bar construction with zero delay/delta calls in lines 730–731, each value needing 1 completed bar — pinned by code absence), plus margin per the admitted worldquant-alpha54 precedent. Pre-warmup bars are flat by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (score reads completed bars only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance USDT-M perpetual under the house overlay (researcher choice — the paper names no venue and evaluates U.S. equities; no source-market equivalence is claimed; perpetual is the minimal realistic venue because the short leg needs margin).
- Order timing (paper-grounded derivation): completed-bar decision with next-bar-open market fills for entries, reversals, and flat-exits — the paper's delay-1 class trades `on the day subsequent to the date of the most recent data`, `starting at the open`, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) on the same verified primitive as the admitted caporale-plastun, ehlers-cg, worldquant-alpha6, and worldquant-alpha12 records' entries (verified this cycle's base). This record claims no other fill convention: no perfect-open print, no maker-touch, no intrabar-path-dependent fill.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing orders by record rule. No hidden Hummingbot stop-order defaults are relied upon, and with no stop/limit legs there is no same-bar TP/SL ordering ambiguity.
- Sizing/capital/costs: the paper ships no sizing, capital, fee, or slippage concept. The explicit house overlay (single-unit frame, pinned house taker fees both legs, modeled funding while held) applies to the derived evaluation here, never presented as source-native behavior. Funding is never zero-claimed: two-sided holds span the `00:00`/`08:00`/`16:00 UTC` funding stamps, so every held bar carries modeled funding.
- Concurrency: at most one single-asset engine position at any time; an opposite signal closes-and-reverses in one step and a zero signal closes-to-flat. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (live-fetch arXiv PDF bytes this cycle, read end to end): the `are also computer code` formula status; the Alpha#101 line `((close - open) / ((high - low) + .001))`; the A.1 operator definitions (standard arithmetic, `rank/delay/correlation` standards — none of which Alpha#101 invokes); the A.2 input definitions (`open, close, high, low, volume = standard definitions for daily price and volume data`); the §2 delay-1 definition and the footnote-11 delay-0 exclusion list (`42, 48, 53 and 54` — Alpha#101 absent, hence delay-1); the §2 mixed building-block framing; the §2 Alpha#101 direction sentence itself (`if the stock runs up intraday (i.e., close > open and high > low), the next day one takes a long position`). With exact implementation provenance (pinned commit `4fc0627d`, file `toraniko/alpha101.py` lines 730–731, head re-confirmed via the commits API this cycle): the executable `_safe_div(close - open, high - low + 0.001)` semantics. This record claims no source-reported performance number of any kind — no return, no win rate, no trade count, no per-alpha table figure is carried into the derived specification — and no reproduced performance exists.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Direction words fenced, admitted plainly: the paper prints `takes a long position` for the runs-up case and never prints an explicit short sentence for Alpha#101. The negative→short leg rests on the paper's symmetric momentum framing (a momentum alpha continues the signed move — the §2 equation-(3) log-momentum twin is traded the same way on either sign) together with the implementation report's long-top / short-bottom construction — not on an order verb attached to Alpha#101's down case. A reviewer must not graft any other direction convention onto this record.
2. Timeframe and venue fenced: the paper is daily U.S. equities and names no venue. `1d` BTCUSDT-perpetual is the disclosed researcher pin (Provenance adaptation (1)); a reviewer must not cite the paper as evidence for any frame or venue.
3. Risk silence fenced: the paper contains no stop, target, trailing, time exit, or risk paragraph for Alpha#101 — the no-guardrail posture is carried over exactly, never upgraded, never presented as a tested safety choice.
4. Cross-sectional machinery fenced: the paper's own evaluation ranks scores across thousands of stocks. Alpha#101's formula contains no `rank(`, no `IndNeutralize`, no `scale(`, no `vwap`, no `adv`, and no sector/industry term (verified by programmatic filter over all 101 lines in the audit lineage) — the single-asset sign map drops the cross-sectional portfolio layer entirely, disclosed as adaptation, never presented as the paper's traded portfolio.
5. Exact-zero determinism fenced: `score[t] == 0` requires `close[t] == open[t]` exactly (the divisor can never be zero by the printed guard). The flat treatment is a predeclared record rule (total and mutually exclusive with the long/short branches), not a paper sentence — without it the doji print would be ambiguous, so it is pinned here rather than left to the reviewer.
6. Overlap fences, admitted plainly: sibling `worldquant-alpha53` trades a 9-bar change of a `(close - low)`-denominator location ratio at delay-0 same-close (different object, different timing); sibling `worldquant-alpha54` trades a power-scaled level short-flat at delay-0 (different object, amputated book); sibling `worldquant-alpha12` trades a volume-change-signed close product (never reads the range, reads volume); sibling `worldquant-alpha6` trades a 10-day open-volume correlation (window statistic, reads volume); pool `cmf-velocity`/`chaikin-oscillator` smooth or volume-weight a `(high - low)`-denominator multiplier (never a raw single-bar sign); pool `caporale-plastun` gates on a 30-day trailing band scanned on 1h bars (different event, different frame); pool `bitcoin-intraday-first-last-halfhour` times 30m session momentum (different construction, different frame). Shared `intraday`/`momentum`/`close-minus-open` vocabulary is not shared signal.
7. No hidden variants admitted: any other divisor, any guard other than `+ 0.001`, any threshold, any stop/target/filter/cooldown, any other frame, fill, venue, or book is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `(close - open) / ((high - low) + 0.001)` / exact-zero flat / two-sided / delay-1 next-open fills / no-stop posture / `1d` BTCUSDT perpetual are frozen.

- F1 — Range-normalization relevance: an unscaled twin (`score = sign(close[t] − open[t])` — same book, grid, fills) must not improve net expectancy; fail ⇒ the `(high - low) + 0.001` normalization adds nothing over the raw body sign on this market.
- F2 — Direction-mapping relevance: a fade twin (short on positive score, long on negative score — same formula, grid, fills, and reversal book) must not improve net expectancy; fail ⇒ the paper's positive→long mapping adds nothing over fading the signal on this market.
- F3 — Horizon relevance: a smoothed twin (sign of the 3-bar sum of scores — same construction averaged over three bars with a 7-bar adopted warmup) must not improve net expectancy; fail ⇒ the single-bar horizon adds nothing over the same construction at triple the scale, and the record is a horizon label rather than a horizon edge.

## Crypto portability

Pinned to BTCUSDT Binance USDT-M perpetual under the house overlay (declared port of a venue-free daily-equity formula). The rule reads completed daily bars only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (the paper's split/dividend close adjustment touches only delay-0 open-anchored alphas — a non-issue for this single-bar close-anchored score on crypto, disclosed, not modeled). The score is scale-free (a body-to-range ratio whose side alone trades) yet range-scale behaviour differs across venues — the OHLC read is the kline print as-is with no normalization to invent. The rule is two-sided, so a spot-only deployment expresses only long-firing bars while short-firing bars stay venue-gated (never silently converted) — a spot-only variant would be a different, unpinned claim. No warmup history beyond 5 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop: adverse excursion after a noise-fired single-bar signal has no guardrail before the opposite signal, by the carried-over paper design — the record's principal risk.
- Doji-whipsaw exposure: when closes print near opens, the book flips long-short on microstructure noise at the worst prints of each swing — the paper provides no buffer band and this record invents none.
- Persistent-regime pin risk: a steadily trending tape pins the book to one side for extended stretches with no scaling — the raw-sign construction cuts both ways, disclosed.
- Exact-zero note: the flat branch fires only on exact-doji bars — rare on BTCUSDT, so the book is effectively always-in-market, disclosed.
- Single-venue port residual: paper-regime U.S. equities vs Binance perpetual execution (prints, fees, funding, range-definition, margin mechanics beyond the house model) is unclaimed, disclosed.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest.
- Author scope: the paper presents production formulaic alphas as research objects, not a vetted retail trading system — this record is research-only and claims no live suitability.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Kakushadze, Z., `101 Formulaic Alphas`, arXiv:1601.00991 (manuscript December 9, 2015 — Alpha#101 formula, A.1 operator/input definitions, §2 delay-1 definition with footnote-11 delay-0 exclusion, §2 Alpha#101 direction sentence — live-fetch PDF bytes read end to end 2026-10-17, sha256 `1f9c21afe32dcb3ee77b31548acdaea00451fbfa1c0ee10c907867bcc736fce9`): https://arxiv.org/abs/1601.00991
- Same paper, PDF (formula appendix, operator/input definitions, empirical sections — read 2026-10-17): https://arxiv.org/pdf/1601.00991
- OctopusTakopi `toraniko-alpha101` (independent audited implementation — `alpha101` at `toraniko/alpha101.py` lines 730–731 — pinned to commit `4fc0627d2a720fd8d583708ef051b9d48d98aacd`, head re-confirmed via the GitHub commits API and byte-identical to the audit copy 2026-10-17): https://github.com/OctopusTakopi/toraniko-alpha101
